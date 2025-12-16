#!/usr/bin/env python3
"""
AMPEL360 Space-T Trace Link Integrity Validator
================================================
Version: 1.0
Date: 2025-12-16
Task: T3-AI (K06 ATA 00 Tasklist)

Validates trace link integrity for broken links and staleness detection.

Usage:
    python scripts/validate_trace_links.py --check-all
    python scripts/validate_trace_links.py --check-dir <directory>
    python scripts/validate_trace_links.py <file>

Exit codes:
    0: All trace links valid
    1: One or more trace links invalid (broken or stale)
    2: Script error

Consumes:
    - ATA 93 trace semantics (traceability graph)
    - Evidence link schema (evidence pack manifests)
"""

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple


@dataclass
class TraceLink:
    """Represents a trace link extracted from a file."""
    source_file: str
    target_path: str
    link_type: str  # 'file_reference', 'evidence_id', 'url'
    line_number: int
    original_text: str


@dataclass
class ValidationIssue:
    """Represents a validation issue with a trace link."""
    link: TraceLink
    issue_type: str  # 'broken', 'stale', 'invalid_format'
    message: str
    severity: str  # 'error', 'warning'


@dataclass
class ValidationResult:
    """Result of trace link validation for a file."""
    source_file: str
    links_found: int
    links_valid: int
    links_broken: int
    links_stale: int
    issues: List[ValidationIssue] = field(default_factory=list)

    @property
    def valid(self) -> bool:
        return all(issue.severity != 'error' for issue in self.issues)


class TraceLinkValidator:
    """Validates trace link integrity for AMPEL360 Space-T documents."""
    
    # Patterns for extracting trace links from markdown
    MARKDOWN_LINK_PATTERN = re.compile(
        r'\[(?P<text>[^\]]+)\]\((?P<path>[^)]+)\)'
    )
    
    # Pattern for file references in text (backtick paths)
    BACKTICK_PATH_PATTERN = re.compile(
        r'`(?P<path>[^`]+\.(md|json|yaml|yml|py|csv))`'
    )
    
    # Pattern for evidence IDs (EVD-Kxx-xxx format)
    EVIDENCE_ID_PATTERN = re.compile(
        r'(?P<evd_id>EVD-K\d{2}-\d{3})'
    )
    
    # File extensions to scan for trace links
    SCANNABLE_EXTENSIONS = {'.md', '.json'}
    
    # Directories to exclude from scanning
    EXCLUDED_DIRS = {
        '.git', '.github', 'node_modules', '__pycache__',
        '.pytest_cache', '.venv', 'venv', 'dist', 'build'
    }
    
    # Default staleness threshold (days since last modified)
    DEFAULT_STALENESS_DAYS = 365
    
    def __init__(
        self,
        repo_root: Path,
        staleness_days: int = DEFAULT_STALENESS_DAYS,
        check_staleness: bool = True,
        strict: bool = False
    ):
        """
        Initialize the trace link validator.
        
        Args:
            repo_root: Root directory of the repository
            staleness_days: Number of days after which a linked file is stale
            check_staleness: Whether to check for stale links
            strict: If True, treat warnings as errors
        """
        self.repo_root = repo_root.resolve()
        self.staleness_days = staleness_days
        self.check_staleness = check_staleness
        self.strict = strict
        self._file_cache: Dict[Path, bool] = {}
        self._evidence_registry: Dict[str, Path] = {}
        self._build_evidence_registry()
    
    def _build_evidence_registry(self) -> None:
        """Build a registry of evidence IDs to their file locations."""
        for md_file in self.repo_root.rglob('*.md'):
            if self._is_excluded_path(md_file):
                continue
            try:
                content = md_file.read_text(encoding='utf-8')
                # Extract evidence ID definitions (EVD-Kxx-xxx in tables)
                for match in re.finditer(
                    r'\*\*(?P<evd_id>EVD-K\d{2}-\d{3})\*\*',
                    content
                ):
                    evd_id = match.group('evd_id')
                    if evd_id not in self._evidence_registry:
                        self._evidence_registry[evd_id] = md_file
            except (OSError, UnicodeDecodeError):
                # Silently skip files that cannot be read (permissions, encoding issues)
                # This is intentional to avoid blocking the registry build for a few bad files
                pass
    
    def _is_excluded_path(self, path: Path) -> bool:
        """Check if path should be excluded from scanning."""
        for parent in path.parents:
            if parent.name in self.EXCLUDED_DIRS:
                return True
        return path.name.startswith('.')
    
    def _file_exists(self, path: Path) -> bool:
        """Check if a file exists, with caching."""
        if path not in self._file_cache:
            self._file_cache[path] = path.exists() and path.is_file()
        return self._file_cache[path]
    
    def _resolve_path(self, source_file: Path, target_path: str) -> Optional[Path]:
        """
        Resolve a target path relative to the source file.
        
        Args:
            source_file: The file containing the link
            target_path: The target path from the link
            
        Returns:
            Resolved absolute path, or None if path is external
        """
        # Skip external URLs and anchor-only links
        if target_path.startswith(('http://', 'https://', 'mailto:', '#')):
            return None
        
        # Remove anchor from path
        clean_path = target_path.split('#')[0]
        if not clean_path:
            return None
        
        # Handle absolute paths (from repo root)
        if clean_path.startswith('/'):
            return self.repo_root / clean_path[1:]
        
        # Handle relative paths
        return (source_file.parent / clean_path).resolve()
    
    def _get_file_age_days(self, file_path: Path) -> int:
        """Get the age of a file in days since last modification."""
        try:
            mtime = datetime.fromtimestamp(file_path.stat().st_mtime)
            return (datetime.now() - mtime).days
        except OSError:
            return -1
    
    def extract_links_from_markdown(self, file_path: Path) -> List[TraceLink]:
        """
        Extract all trace links from a markdown file.
        
        Args:
            file_path: Path to the markdown file
            
        Returns:
            List of TraceLink objects
        """
        links: List[TraceLink] = []
        
        try:
            content = file_path.read_text(encoding='utf-8')
        except (OSError, UnicodeDecodeError) as e:
            return links
        
        lines = content.split('\n')
        
        for line_num, line in enumerate(lines, 1):
            # Extract markdown links [text](path)
            for match in self.MARKDOWN_LINK_PATTERN.finditer(line):
                target_path = match.group('path')
                links.append(TraceLink(
                    source_file=str(file_path.relative_to(self.repo_root)),
                    target_path=target_path,
                    link_type='file_reference',
                    line_number=line_num,
                    original_text=match.group(0)
                ))
            
            # Extract backtick paths `path/to/file.md`
            # Note: We check if the path already appears in a markdown link on
            # the same line to avoid duplicate reporting. This is a simple heuristic
            # that works for most cases.
            for match in self.BACKTICK_PATH_PATTERN.finditer(line):
                target_path = match.group('path')
                # Skip if already captured as markdown link on same line
                if f']({target_path})' not in line and f'({target_path})' not in line:
                    links.append(TraceLink(
                        source_file=str(file_path.relative_to(self.repo_root)),
                        target_path=target_path,
                        link_type='file_reference',
                        line_number=line_num,
                        original_text=match.group(0)
                    ))
            
            # Extract evidence IDs
            for match in self.EVIDENCE_ID_PATTERN.finditer(line):
                evd_id = match.group('evd_id')
                links.append(TraceLink(
                    source_file=str(file_path.relative_to(self.repo_root)),
                    target_path=evd_id,
                    link_type='evidence_id',
                    line_number=line_num,
                    original_text=evd_id
                ))
        
        return links
    
    def extract_links_from_json(self, file_path: Path) -> List[TraceLink]:
        """
        Extract trace links from a JSON evidence manifest.
        
        Args:
            file_path: Path to the JSON file
            
        Returns:
            List of TraceLink objects
        """
        links: List[TraceLink] = []
        
        try:
            content = file_path.read_text(encoding='utf-8')
            data = json.loads(content)
        except (OSError, json.JSONDecodeError, UnicodeDecodeError):
            return links
        
        # Extract file_path references from evidence_items
        if isinstance(data, dict) and 'evidence_items' in data:
            for item in data.get('evidence_items', []):
                if isinstance(item, dict) and 'file_path' in item:
                    links.append(TraceLink(
                        source_file=str(file_path.relative_to(self.repo_root)),
                        target_path=item['file_path'],
                        link_type='file_reference',
                        line_number=0,  # JSON doesn't have meaningful line numbers
                        original_text=f"file_path: {item['file_path']}"
                    ))
        
        return links
    
    def validate_link(self, link: TraceLink, source_path: Path) -> Optional[ValidationIssue]:
        """
        Validate a single trace link.
        
        Args:
            link: The trace link to validate
            source_path: Absolute path to the source file
            
        Returns:
            ValidationIssue if there's a problem, None otherwise
        """
        # Handle evidence IDs
        if link.link_type == 'evidence_id':
            if link.target_path not in self._evidence_registry:
                return ValidationIssue(
                    link=link,
                    issue_type='broken',
                    message=f"Evidence ID '{link.target_path}' not found in registry",
                    severity='warning'  # Warning because IDs might be defined elsewhere
                )
            return None
        
        # Handle file references
        resolved_path = self._resolve_path(source_path, link.target_path)
        
        # Skip external URLs
        if resolved_path is None:
            return None
        
        # Check if file exists
        if not self._file_exists(resolved_path):
            return ValidationIssue(
                link=link,
                issue_type='broken',
                message=f"File not found: {link.target_path}",
                severity='error'
            )
        
        # Check staleness if enabled
        if self.check_staleness:
            age_days = self._get_file_age_days(resolved_path)
            if age_days > self.staleness_days:
                return ValidationIssue(
                    link=link,
                    issue_type='stale',
                    message=f"Linked file is {age_days} days old (threshold: {self.staleness_days})",
                    severity='warning' if not self.strict else 'error'
                )
        
        return None
    
    def validate_file(self, file_path: Path) -> ValidationResult:
        """
        Validate all trace links in a file.
        
        Args:
            file_path: Path to the file to validate
            
        Returns:
            ValidationResult with findings
        """
        file_path = file_path.resolve()
        result = ValidationResult(
            source_file=str(file_path.relative_to(self.repo_root)),
            links_found=0,
            links_valid=0,
            links_broken=0,
            links_stale=0
        )
        
        # Extract links based on file type
        if file_path.suffix == '.md':
            links = self.extract_links_from_markdown(file_path)
        elif file_path.suffix == '.json':
            links = self.extract_links_from_json(file_path)
        else:
            return result
        
        # Deduplicate links by target_path and link_type to avoid
        # reporting the same broken/stale link multiple times when it appears
        # in the same file. This is intentional to reduce noise in reports.
        seen_links: Set[str] = set()
        unique_links: List[TraceLink] = []
        for link in links:
            link_key = f"{link.target_path}:{link.link_type}"
            if link_key not in seen_links:
                seen_links.add(link_key)
                unique_links.append(link)
        
        result.links_found = len(unique_links)
        
        # Validate each unique link
        for link in unique_links:
            issue = self.validate_link(link, file_path)
            if issue is None:
                result.links_valid += 1
            else:
                result.issues.append(issue)
                if issue.issue_type == 'broken':
                    result.links_broken += 1
                elif issue.issue_type == 'stale':
                    result.links_stale += 1
        
        return result
    
    def validate_directory(self, directory: Path) -> List[ValidationResult]:
        """
        Validate all trace links in files within a directory.
        
        Args:
            directory: Directory path to scan
            
        Returns:
            List of ValidationResult objects
        """
        results: List[ValidationResult] = []
        
        for file_path in directory.rglob('*'):
            if not file_path.is_file():
                continue
            if self._is_excluded_path(file_path):
                continue
            if file_path.suffix not in self.SCANNABLE_EXTENSIONS:
                continue
            
            result = self.validate_file(file_path)
            if result.links_found > 0:  # Only include files with links
                results.append(result)
        
        return results


def print_result(result: ValidationResult, verbose: bool = False) -> None:
    """Print validation result to console."""
    has_errors = any(i.severity == 'error' for i in result.issues)
    has_warnings = any(i.severity == 'warning' for i in result.issues)
    
    if result.valid and not verbose:
        return
    
    status = '✗' if has_errors else ('⚠' if has_warnings else '✓')
    print(f"{status} {result.source_file}")
    
    if verbose:
        print(f"  Links: {result.links_found} found, {result.links_valid} valid, "
              f"{result.links_broken} broken, {result.links_stale} stale")
    
    for issue in result.issues:
        icon = '✗' if issue.severity == 'error' else '⚠'
        print(f"  {icon} Line {issue.link.line_number}: {issue.message}")
        if verbose:
            print(f"    Link: {issue.link.original_text}")


def print_summary(results: List[ValidationResult]) -> Tuple[int, int]:
    """Print summary of all validation results. Returns (error_count, warning_count)."""
    total_files = len(results)
    total_links = sum(r.links_found for r in results)
    total_valid = sum(r.links_valid for r in results)
    total_broken = sum(r.links_broken for r in results)
    total_stale = sum(r.links_stale for r in results)
    
    print(f"\n{'='*60}")
    print("Trace Link Validation Summary")
    print(f"{'='*60}")
    print(f"Files scanned:      {total_files}")
    print(f"Total links found:  {total_links}")
    print(f"Valid links:        {total_valid}")
    print(f"Broken links:       {total_broken}")
    print(f"Stale links:        {total_stale}")
    print(f"{'='*60}")
    
    if total_broken == 0 and total_stale == 0:
        print("✅ All trace links are valid!")
    else:
        if total_broken > 0:
            print(f"❌ {total_broken} broken link(s) found")
        if total_stale > 0:
            print(f"⚠️  {total_stale} stale link(s) found")
    
    print(f"{'='*60}")
    
    return total_broken, total_stale


def main() -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Validate trace link integrity in AMPEL360 Space-T documents',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --check-all
  %(prog)s --check-dir ./AMPEL360-SPACE-T-PORTAL
  %(prog)s 06_00_TRC_LC01_SPACET_ssot-traceability_v01.md
  %(prog)s --check-all --staleness-days 180
        """
    )
    
    parser.add_argument(
        'file',
        nargs='?',
        help='File to validate'
    )
    parser.add_argument(
        '--check-all',
        action='store_true',
        help='Check all files in current directory and subdirectories'
    )
    parser.add_argument(
        '--check-dir',
        metavar='DIR',
        help='Check all files in specified directory'
    )
    parser.add_argument(
        '--staleness-days',
        type=int,
        default=TraceLinkValidator.DEFAULT_STALENESS_DAYS,
        help=f'Days threshold for stale links (default: {TraceLinkValidator.DEFAULT_STALENESS_DAYS})'
    )
    parser.add_argument(
        '--no-staleness',
        action='store_true',
        help='Disable staleness checking'
    )
    parser.add_argument(
        '--strict',
        action='store_true',
        help='Treat warnings as errors'
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Show verbose output including valid files'
    )
    
    args = parser.parse_args()
    
    # Validate arguments
    if not any([args.file, args.check_all, args.check_dir]):
        parser.error('Must specify file, --check-all, or --check-dir')
    
    # Determine repository root based on mode
    if args.check_dir:
        repo_root = Path(args.check_dir).resolve()
    elif args.file:
        # For single file, use the file's directory as root to avoid path resolution errors
        file_path = Path(args.file).resolve()
        repo_root = file_path.parent
    else:
        repo_root = Path('.').resolve()
    
    # Create validator
    validator = TraceLinkValidator(
        repo_root=repo_root,
        staleness_days=args.staleness_days,
        check_staleness=not args.no_staleness,
        strict=args.strict
    )
    
    results: List[ValidationResult] = []
    
    try:
        if args.file:
            # Validate single file
            file_path = Path(args.file).resolve()
            if not file_path.exists():
                print(f"Error: File '{args.file}' not found", file=sys.stderr)
                return 2
            result = validator.validate_file(file_path)
            results = [result]
            print_result(result, verbose=args.verbose)
        elif args.check_dir:
            # Validate directory
            dir_path = Path(args.check_dir)
            if not dir_path.is_dir():
                print(f"Error: '{args.check_dir}' is not a directory", file=sys.stderr)
                return 2
            results = validator.validate_directory(dir_path)
            for result in results:
                print_result(result, verbose=args.verbose)
        elif args.check_all:
            # Validate current directory
            results = validator.validate_directory(Path('.'))
            for result in results:
                print_result(result, verbose=args.verbose)
        
        # Print summary
        error_count, warning_count = print_summary(results)
        
        # Return appropriate exit code
        if error_count > 0:
            return 1
        if args.strict and warning_count > 0:
            return 1
        return 0
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
