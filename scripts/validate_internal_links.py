#!/usr/bin/env python3
"""
AMPEL360 Space-T GATE-LINK-001: Internal Link Integrity Validator
===================================================================
Version: 1.0
Date: 2025-12-17
Standard: Nomenclature v6.0 R1.0
Gate ID: GATE-LINK-001

Validates internal links in Markdown files and provides fix capability.
This gate addresses KI-PR3-001 (Broken Internal Links after v6.0 migration).

Exit Codes:
    0 - Pass (no broken links)
    1 - Violations (broken links found, mode=block)
    2 - Runtime error

Usage:
    # Check only (warn mode)
    python scripts/validate_internal_links.py --scope repo --mode warn

    # Check and fix (update mode, dry-run)
    python scripts/validate_internal_links.py --scope repo --update --dry-run

    # Check and fix (execute)
    python scripts/validate_internal_links.py --scope repo --mode block --update

    # With database recording
    python scripts/validate_internal_links.py --scope repo --db plc_ontology.db

    # With report output
    python scripts/validate_internal_links.py --scope repo --report out/link_report.txt
"""

import argparse
import csv
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Set, Any
from collections import defaultdict


class LinkIntegrityGate:
    """
    GATE-LINK-001: Internal Link Integrity Gate
    
    Validates that all internal Markdown links resolve to existing files.
    Supports automatic fixing using rename maps from v5 and v6 migrations.
    """
    
    GATE_CODE = "GATE-LINK-001"
    GATE_NAME = "Link Integrity Check"
    
    # Excluded directories
    EXCLUDED_DIRS = {'.git', 'node_modules', '__pycache__', '.venv', 'venv', 'out', '.cache'}
    
    # Excluded files (exact match)
    EXCLUDED_FILES = {'LICENSE', 'README.md', 'EXAMPLES.md', 'STRUCTURE_SUMMARY.md'}
    
    # Template placeholder patterns - links to directories/files that are template placeholders
    TEMPLATE_PLACEHOLDER_PATTERNS = [
        r'^01_WBS/',
        r'^02_IDS_REGISTRY/',
        r'^03_SCHEMA/',
        r'^04_EXPORTS/',
        r'^05_CI_GATES/',
        r'^06_EVIDENCE/',
        r'^07_DECISIONS/',
        r'^08_TRACEABILITY/',
        r'^MONITORING/',
        r'^SCHEMAS/',
        r'^\./',  # relative current dir
        r'AMPEL360_SPACE-T/',  # External reference to non-existent dirs
        r'T-SIMTEST/',
        r'T-TECHNOLOGY/',
        r'T-CRAFT/',
        r'P-PROGRAM/',
        r'\.\./+(EVIDENCE|MONITORING|SCHEMAS)/',  # Relative references to planned directories (any depth)
        r'\.\./+ATA_TASKS/.*/EVIDENCE/',  # Relative references to ATA task evidence
        r'\{\{[A-Z_]+\}\}',  # Mustache/template placeholders like {{DESCRIPTION}}
        r'^(filename|path)$',  # Generic placeholder words
        r'^diagrams/',  # Diagrams placeholder
        r'k01-authority-pack-example-manifest',  # Example manifest files
    ]
    
    def __init__(
        self,
        repo_root: Path = Path('.'),
        rename_maps: Optional[List[str]] = None,
        db_path: Optional[str] = None
    ):
        """
        Initialize the link integrity gate.
        
        Args:
            repo_root: Repository root directory
            rename_maps: List of rename map CSV paths to load
            db_path: Optional path to PLC database
        """
        self.repo_root = repo_root.resolve()
        self.rename_map: Dict[str, str] = {}
        self.reverse_map: Dict[str, str] = {}  # For name-based matching
        self.db_path = db_path
        self.db = None
        
        # Load rename maps
        if rename_maps is None:
            rename_maps = ['rename_map_v6.csv', 'rename_map_v5.csv']
        
        for map_path in rename_maps:
            self._load_rename_map(map_path)
        
        # Initialize database if path provided
        if db_path:
            self._init_database()
        
        # Results
        self.broken_links: List[Dict[str, Any]] = []
        self.template_placeholders: List[Dict[str, Any]] = []  # Template placeholder links
        self.fixed_links: List[Dict[str, Any]] = []
        self.files_scanned: int = 0
        self.files_updated: int = 0
        self.run_id: Optional[int] = None
        self.ignore_placeholders: bool = True  # By default, ignore template placeholders
    
    def _is_template_placeholder(self, link_path: str) -> bool:
        """Check if a link is a template placeholder (to non-existent template structure)."""
        for pattern in self.TEMPLATE_PLACEHOLDER_PATTERNS:
            if re.search(pattern, link_path):
                return True
        return False
    
    def _load_rename_map(self, csv_path: str) -> None:
        """Load rename map from CSV file."""
        full_path = self.repo_root / csv_path
        if not full_path.exists():
            return
        
        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    old_path = row.get('old_path', '')
                    new_path = row.get('new_path', '')
                    if old_path and new_path and old_path != new_path:
                        self.rename_map[old_path] = new_path
                        # Also map by filename only for fuzzy matching
                        old_name = Path(old_path).name
                        new_name = Path(new_path).name
                        if old_name != new_name:
                            self.reverse_map[old_name] = new_path
        except Exception as e:
            print(f"Warning: Could not load rename map {csv_path}: {e}", file=sys.stderr)
    
    def _init_database(self) -> None:
        """Initialize database connection."""
        try:
            from scripts.plc_db import PLCDatabase
            self.db = PLCDatabase(self.db_path)
            # Initialize schema if not exists
            if not Path(self.db_path).exists():
                self.db.initialize_database()
        except ImportError:
            print("Warning: PLCDatabase not available, running without DB", file=sys.stderr)
            self.db = None
        except Exception as e:
            print(f"Warning: Could not initialize database: {e}", file=sys.stderr)
            self.db = None
    
    def _should_exclude(self, path: Path) -> bool:
        """Check if a path should be excluded from scanning."""
        # Check directory exclusions
        for part in path.parts:
            if part in self.EXCLUDED_DIRS:
                return True
        
        # Check file exclusions
        if path.name in self.EXCLUDED_FILES:
            return True
        
        return False
    
    def _get_markdown_files(self, scope: str = 'repo') -> List[Path]:
        """Get list of Markdown files to scan."""
        if scope == 'repo':
            md_files = list(self.repo_root.rglob('*.md'))
        elif scope == 'diff':
            # Get files changed in current PR/branch
            md_files = self._get_diff_files()
        else:
            md_files = list(self.repo_root.rglob('*.md'))
        
        # Filter excluded paths
        return [f for f in md_files if not self._should_exclude(f.relative_to(self.repo_root))]
    
    def _get_diff_files(self) -> List[Path]:
        """Get Markdown files changed in current diff."""
        import subprocess
        try:
            result = subprocess.run(
                ['git', 'diff', '--name-only', 'HEAD~1'],
                capture_output=True, text=True, cwd=self.repo_root
            )
            if result.returncode == 0:
                files = result.stdout.strip().split('\n')
                return [
                    self.repo_root / f for f in files
                    if f.endswith('.md') and (self.repo_root / f).exists()
                ]
        except Exception:
            pass
        return list(self.repo_root.rglob('*.md'))
    
    def _extract_links(self, content: str) -> List[Tuple[str, str, int]]:
        """
        Extract Markdown links from content.
        
        Returns:
            List of (link_text, link_path, line_number) tuples
        """
        links = []
        link_pattern = re.compile(r'\[([^\]]+)\]\(([^\)]+)\)')
        
        for line_num, line in enumerate(content.split('\n'), 1):
            for match in link_pattern.finditer(line):
                link_text = match.group(1)
                link_path = match.group(2)
                links.append((link_text, link_path, line_num))
        
        return links
    
    def _is_internal_link(self, link_path: str) -> bool:
        """Check if a link is an internal link (not external or anchor-only)."""
        if link_path.startswith(('http://', 'https://', 'mailto:', 'ftp://')):
            return False
        if link_path.startswith('#'):
            return False
        return True
    
    def _resolve_link(
        self,
        source_file: Path,
        link_path: str
    ) -> Tuple[bool, Optional[Path], Optional[str]]:
        """
        Resolve a link path and check if it exists.
        
        Args:
            source_file: The file containing the link
            link_path: The link path from the Markdown
            
        Returns:
            Tuple of (exists, resolved_path, suggested_fix)
        """
        # Handle anchor fragments
        anchor = None
        if '#' in link_path:
            link_path, anchor = link_path.split('#', 1)
        
        if not link_path:
            # Anchor-only link (validated separately)
            return True, None, None
        
        # Resolve relative path
        if link_path.startswith('/'):
            # Absolute from repo root
            target_path = self.repo_root / link_path.lstrip('/')
        else:
            # First try as relative to source file
            target_path = (source_file.parent / link_path).resolve()
            
            # If that doesn't exist, check if it's an absolute path from repo root (without leading /)
            if not target_path.exists():
                alt_target = self.repo_root / link_path
                if alt_target.exists():
                    # The link should be relative to source file, calculate proper relative path
                    try:
                        rel_path = os.path.relpath(alt_target, source_file.parent)
                        if anchor:
                            rel_path += f'#{anchor}'
                        return False, target_path, rel_path
                    except ValueError:
                        pass
        
        # Check if target exists
        if target_path.exists():
            return True, target_path, None
        
        # Try to find a fix using rename maps
        relative_path = str(link_path)
        link_name = Path(link_path).name
        
        # Check full path in rename map
        for old_path, new_path in self.rename_map.items():
            if relative_path.endswith(old_path) or old_path.endswith(relative_path):
                suggested_path = self.repo_root / new_path
                if suggested_path.exists():
                    # Calculate relative path from source file
                    try:
                        suggested_fix = os.path.relpath(suggested_path, source_file.parent)
                    except ValueError:
                        suggested_fix = new_path
                    if anchor:
                        suggested_fix += f'#{anchor}'
                    return False, target_path, suggested_fix
        
        # Check by filename only (fuzzy match)
        if link_name in self.reverse_map:
            suggested_path = self.repo_root / self.reverse_map[link_name]
            if suggested_path.exists():
                suggested_fix = self.reverse_map[link_name]
                if anchor:
                    suggested_fix += f'#{anchor}'
                return False, target_path, suggested_fix
        
        # Try to find file by name in the same directory or nearby
        suggested_fix = self._find_nearest_match(source_file, link_name, link_path)
        
        return False, target_path, suggested_fix
    
    def _extract_subject_from_filename(self, filename: str) -> Optional[str]:
        """Extract the SUBJECT field from a v6.0 filename (after __)."""
        if '__' in filename:
            # Format: ...__subject_TYPE_I01-R01_STATUS.ext
            after_double = filename.split('__', 1)[1]
            # Subject is before first underscore that looks like a TYPE code
            parts = after_double.split('_')
            if parts:
                return parts[0]  # e.g., "stakeholder-ai-entrypoint"
        return None
    
    def _find_nearest_match(
        self,
        source_file: Path,
        link_name: str,
        original_path: str
    ) -> Optional[str]:
        """Find the nearest matching file by name or SUBJECT field and return relative path."""
        # Search in same directory first, then portal, then repo root
        search_dirs = [
            source_file.parent,
            self.repo_root / 'AMPEL360-SPACE-T-PORTAL',
            self.repo_root,
        ]
        
        # Also add directories from the original path
        if '/' in original_path:
            base_parts = Path(original_path).parts[:-1]
            for i in range(len(base_parts)):
                search_dirs.append(source_file.parent.joinpath(*base_parts[:i+1]))
        
        def get_relative_path(match: Path) -> str:
            """Get relative path from source file."""
            try:
                return os.path.relpath(match, source_file.parent)
            except ValueError:
                return str(match.relative_to(self.repo_root))
        
        # First try exact name match
        for search_dir in search_dirs:
            if search_dir.exists():
                for match in search_dir.rglob(link_name):
                    if match.exists():
                        return get_relative_path(match)
        
        # Try SUBJECT-based matching for v6.0 nomenclature
        subject = self._extract_subject_from_filename(link_name)
        if subject:
            # Find files with same subject
            pattern = f'*__{subject}_*.md'
            for search_dir in search_dirs:
                if search_dir.exists():
                    for match in search_dir.rglob(pattern):
                        if match.exists():
                            return get_relative_path(match)
        
        # Try partial filename matching (for old format links)
        # Extract key parts from link name
        if '_' in link_name:
            # Try to match by the descriptive part of the filename
            # E.g., "stakeholder-ai-entrypoint" from full filename
            name_parts = link_name.replace('.md', '').split('_')
            # Look for kebab-case descriptive parts
            for part in name_parts:
                if '-' in part and len(part) > 10:
                    pattern = f'*{part}*.md'
                    for search_dir in search_dirs[:3]:  # Limit search scope
                        if search_dir.exists():
                            for match in search_dir.rglob(pattern):
                                if match.exists():
                                    return get_relative_path(match)
        
        return None
    
    def scan(self, scope: str = 'repo', ignore_placeholders: bool = True) -> List[Dict[str, Any]]:
        """
        Scan for broken internal links.
        
        Args:
            scope: 'repo' for full repository, 'diff' for changed files only
            ignore_placeholders: If True, ignore template placeholder links
            
        Returns:
            List of broken link records
        """
        self.broken_links = []
        self.template_placeholders = []
        self.files_scanned = 0
        self.ignore_placeholders = ignore_placeholders
        
        md_files = self._get_markdown_files(scope)
        
        for md_file in md_files:
            try:
                content = md_file.read_text(encoding='utf-8', errors='ignore')
                self.files_scanned += 1
                
                links = self._extract_links(content)
                
                for link_text, link_path, line_num in links:
                    if not self._is_internal_link(link_path):
                        continue
                    
                    exists, resolved_path, suggested_fix = self._resolve_link(md_file, link_path)
                    
                    if not exists:
                        relative_source = str(md_file.relative_to(self.repo_root))
                        
                        is_placeholder = self._is_template_placeholder(link_path)
                        
                        broken_link = {
                            'source_path': relative_source,
                            'target_link': link_path,
                            'target_resolved': str(resolved_path) if resolved_path else None,
                            'link_text': link_text,
                            'line_number': line_num,
                            'fixable': suggested_fix is not None,
                            'suggested_fix': suggested_fix,
                            'confidence': 0.8 if suggested_fix else 0.0,
                            'is_placeholder': is_placeholder,
                        }
                        
                        if is_placeholder and ignore_placeholders:
                            self.template_placeholders.append(broken_link)
                        else:
                            self.broken_links.append(broken_link)
                        
            except Exception as e:
                print(f"Warning: Error scanning {md_file}: {e}", file=sys.stderr)
        
        return self.broken_links
    
    def fix(self, dry_run: bool = True) -> int:
        """
        Apply fixes to broken links.
        
        Args:
            dry_run: If True, only show what would be changed
            
        Returns:
            Number of files modified
        """
        self.fixed_links = []
        self.files_updated = 0
        
        # Group fixes by file
        fixes_by_file: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
        
        for broken in self.broken_links:
            if broken['fixable'] and broken['suggested_fix']:
                fixes_by_file[broken['source_path']].append(broken)
        
        for source_path, fixes in fixes_by_file.items():
            file_path = self.repo_root / source_path
            
            try:
                content = file_path.read_text(encoding='utf-8')
                original_content = content
                
                for fix in fixes:
                    old_link = fix['target_link']
                    new_link = fix['suggested_fix']
                    
                    # Build regex pattern to match the link
                    # Match [text](old_link) and replace with [text](new_link)
                    pattern = re.compile(
                        r'\[([^\]]+)\]\(' + re.escape(old_link) + r'\)'
                    )
                    
                    content = pattern.sub(
                        r'[\1](' + new_link + ')',
                        content
                    )
                    
                    self.fixed_links.append({
                        'source_path': source_path,
                        'old_link': old_link,
                        'new_link': new_link,
                        'line_number': fix['line_number'],
                    })
                
                if content != original_content:
                    if not dry_run:
                        file_path.write_text(content, encoding='utf-8')
                    self.files_updated += 1
                    
                    action = "[DRY-RUN] Would update" if dry_run else "Updated"
                    print(f"  {action}: {source_path} ({len(fixes)} links)")
                    
            except Exception as e:
                print(f"Warning: Could not fix {source_path}: {e}", file=sys.stderr)
        
        return self.files_updated
    
    def record_to_db(
        self,
        passed: bool,
        git_ref: Optional[str] = None,
        git_sha: Optional[str] = None,
        pr_number: Optional[int] = None
    ) -> Optional[int]:
        """
        Record gate run and findings to database.
        
        Returns:
            run_id if successful, None otherwise
        """
        if not self.db:
            return None
        
        try:
            # Record gate run
            self.run_id = self.db.record_gate_run(
                gate_code=self.GATE_CODE,
                passed=passed,
                error_count=len([b for b in self.broken_links if not b['fixable']]),
                warning_count=len([b for b in self.broken_links if b['fixable']]),
                git_ref=git_ref,
                git_sha=git_sha,
                pr_number=pr_number,
                metadata={
                    'files_scanned': self.files_scanned,
                    'broken_links_total': len(self.broken_links),
                    'fixable_links': len([b for b in self.broken_links if b['fixable']]),
                    'fixed_links': len(self.fixed_links),
                    'files_updated': self.files_updated,
                }
            )
            
            # Clear previous link integrity records
            self.db.clear_link_integrity_records()
            
            # Record each broken link
            for broken in self.broken_links:
                self.db.record_broken_link(
                    source_path=broken['source_path'],
                    target_link=broken['target_link'],
                    target_resolved_path=broken.get('target_resolved'),
                    link_type='INTERNAL',
                    fixable=broken['fixable'],
                    suggested_fix=broken.get('suggested_fix')
                )
                
                # Also record as gate finding
                self.db.record_gate_finding(
                    run_id=self.run_id,
                    gate_code=self.GATE_CODE,
                    severity='WARN' if broken['fixable'] else 'ERROR',
                    message=f"Broken link: {broken['target_link']}",
                    artifact_path=broken['source_path'],
                    finding_code='BROKEN_LINK',
                    line_number=broken['line_number'],
                    details={
                        'suggested_fix': broken.get('suggested_fix'),
                        'confidence': broken.get('confidence'),
                    }
                )
            
            return self.run_id
            
        except Exception as e:
            print(f"Warning: Could not record to database: {e}", file=sys.stderr)
            return None
    
    def generate_report(self, output_path: Optional[str] = None) -> str:
        """
        Generate a human-readable report.
        
        Args:
            output_path: Optional file path to write report to
            
        Returns:
            Report content as string
        """
        lines = []
        lines.append("=" * 70)
        lines.append(f"GATE-LINK-001: Link Integrity Report")
        lines.append(f"Generated: {datetime.now().isoformat()}")
        lines.append("=" * 70)
        lines.append("")
        
        lines.append("## Summary")
        lines.append(f"  Markdown files scanned: {self.files_scanned}")
        lines.append(f"  Broken internal links: {len(self.broken_links)}")
        lines.append(f"  Template placeholders (ignored): {len(self.template_placeholders)}")
        
        fixable = [b for b in self.broken_links if b['fixable']]
        unfixable = [b for b in self.broken_links if not b['fixable']]
        
        lines.append(f"  Fixable (auto): {len(fixable)}")
        lines.append(f"  Unfixable (manual): {len(unfixable)}")
        lines.append(f"  Files updated: {self.files_updated}")
        lines.append(f"  Links fixed: {len(self.fixed_links)}")
        lines.append("")
        
        if self.broken_links:
            lines.append("## Broken Links")
            lines.append("")
            
            # Group by source file
            by_file: Dict[str, List[Dict]] = defaultdict(list)
            for broken in self.broken_links:
                by_file[broken['source_path']].append(broken)
            
            for source_path, links in sorted(by_file.items()):
                lines.append(f"### {source_path}")
                for link in links:
                    status = "FIXABLE" if link['fixable'] else "MANUAL"
                    lines.append(f"  - [{status}] Line {link['line_number']}: {link['target_link']}")
                    if link['suggested_fix']:
                        lines.append(f"    → Suggested: {link['suggested_fix']}")
                lines.append("")
        
        if self.fixed_links:
            lines.append("## Applied Fixes")
            lines.append("")
            for fix in self.fixed_links:
                lines.append(f"  - {fix['source_path']} (line {fix['line_number']})")
                lines.append(f"    {fix['old_link']} → {fix['new_link']}")
            lines.append("")
        
        lines.append("=" * 70)
        lines.append(f"Exit Code: {'0 (PASS)' if len(self.broken_links) == 0 else '1 (VIOLATIONS)'}")
        lines.append("=" * 70)
        
        report = '\n'.join(lines)
        
        if output_path:
            Path(output_path).parent.mkdir(parents=True, exist_ok=True)
            Path(output_path).write_text(report, encoding='utf-8')
            print(f"Report written to: {output_path}")
        
        return report


def main():
    """Main entry point for GATE-LINK-001."""
    parser = argparse.ArgumentParser(
        description='GATE-LINK-001: Internal Link Integrity Validator',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exit Codes:
  0 - Pass (no broken links or all fixed)
  1 - Violations (broken links exist, mode=block)
  2 - Runtime error

Examples:
  # Check all links (warn mode)
  %(prog)s --scope repo --mode warn

  # Check with detailed report
  %(prog)s --scope repo --report out/link_report.txt

  # Preview fixes (dry-run)
  %(prog)s --scope repo --update --dry-run

  # Apply fixes
  %(prog)s --scope repo --update

  # Check only changed files
  %(prog)s --scope diff --mode block

  # With database recording
  %(prog)s --scope repo --db plc_ontology.db
        """
    )
    
    parser.add_argument(
        '--scope',
        choices=['repo', 'diff'],
        default='repo',
        help='Scope of scan: repo (all files) or diff (changed files only)'
    )
    
    parser.add_argument(
        '--db',
        metavar='PATH',
        help='Path to PLC ontology database (optional)'
    )
    
    parser.add_argument(
        '--mode',
        choices=['warn', 'block'],
        default='warn',
        help='Execution mode: warn (exit 0) or block (exit 1 on violations)'
    )
    
    parser.add_argument(
        '--update',
        action='store_true',
        help='Apply safe rewrites to fix broken links'
    )
    
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Preview changes without modifying files (use with --update)'
    )
    
    parser.add_argument(
        '--report',
        metavar='PATH',
        help='Write report to specified path'
    )
    
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Show detailed output during scan'
    )
    
    parser.add_argument(
        '--rename-map',
        action='append',
        dest='rename_maps',
        help='Path to rename map CSV (can be specified multiple times)'
    )
    
    parser.add_argument(
        '--include-placeholders',
        action='store_true',
        help='Include template placeholder links in broken count (normally ignored)'
    )
    
    args = parser.parse_args()
    
    try:
        # Initialize gate
        gate = LinkIntegrityGate(
            repo_root=Path('.'),
            rename_maps=args.rename_maps,
            db_path=args.db
        )
        
        ignore_placeholders = not args.include_placeholders
        
        # Scan for broken links
        print(f"🔍 Scanning for broken internal links (scope: {args.scope})...")
        broken = gate.scan(scope=args.scope, ignore_placeholders=ignore_placeholders)
        
        # Display summary
        print(f"\n{'='*70}")
        print(f"GATE-LINK-001: Link Integrity Check")
        print(f"{'='*70}")
        print(f"Markdown files scanned: {gate.files_scanned}")
        print(f"Broken internal links: {len(broken)}")
        print(f"Template placeholders (ignored): {len(gate.template_placeholders)}")
        
        fixable = [b for b in broken if b['fixable']]
        unfixable = [b for b in broken if not b['fixable']]
        
        print(f"  Fixable (auto): {len(fixable)}")
        print(f"  Unfixable (manual): {len(unfixable)}")
        
        # Apply fixes if requested
        if args.update and fixable:
            print(f"\n{'='*70}")
            print(f"{'[DRY-RUN] ' if args.dry_run else ''}Applying fixes...")
            print(f"{'='*70}")
            
            files_updated = gate.fix(dry_run=args.dry_run)
            
            if not args.dry_run:
                # Re-scan to verify fixes
                print(f"\n{'='*70}")
                print(f"Verification scan...")
                print(f"{'='*70}")
                broken = gate.scan(scope=args.scope, ignore_placeholders=ignore_placeholders)
                print(f"Remaining broken links: {len(broken)}")
                print(f"Template placeholders (ignored): {len(gate.template_placeholders)}")
        
        # Generate report if requested
        if args.report:
            gate.generate_report(args.report)
        
        # Record to database if configured
        if gate.db:
            passed = len(broken) == 0
            gate.record_to_db(passed=passed)
            print(f"\n✓ Results recorded to database (run_id: {gate.run_id})")
        
        # Determine exit code
        remaining_broken = len(gate.broken_links)
        
        if remaining_broken == 0:
            print(f"\n✅ GATE-LINK-001: PASS - No broken internal links")
            return 0
        elif args.mode == 'warn':
            print(f"\n⚠️  GATE-LINK-001: WARN - {remaining_broken} broken link(s) found")
            return 0
        else:  # mode == 'block'
            print(f"\n❌ GATE-LINK-001: FAIL - {remaining_broken} broken link(s) found")
            return 1
            
    except Exception as e:
        print(f"\n❌ GATE-LINK-001: ERROR - {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return 2


if __name__ == '__main__':
    sys.exit(main())
