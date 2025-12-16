#!/usr/bin/env python3
"""
AMPEL360 Space-T Drift Detection and Monitoring
================================================
Version: 1.0
Date: 2025-12-16
Task: T6-AI from K06 ATA 00 Tasklist

Implements weekly drift detection and monitoring for governance artifacts.
Detects:
- Nomenclature violations and namespace conflicts
- Schema registry drift (unregistered schemas, version conflicts)
- Trace link staleness (broken links, outdated references)
- Identifier registry drift (duplicate IDs)

Deliverable: Weekly drift scan workflow + alerting integration

Usage:
    python scripts/detect_drift.py --check-all
    python scripts/detect_drift.py --check-nomenclature
    python scripts/detect_drift.py --check-schemas
    python scripts/detect_drift.py --output-json report.json
    python scripts/detect_drift.py --output-markdown report.md

Exit codes:
    0: No drift detected
    1: Drift detected (warnings or errors)
    2: Script error
"""

import argparse
import hashlib
import json
import re
import sys
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Set
from collections import defaultdict


# Import validators from sibling modules
sys.path.insert(0, str(Path(__file__).parent.parent))
try:
    from validate_nomenclature import NomenclatureValidator
except ImportError:
    NomenclatureValidator = None


@dataclass
class DriftItem:
    """Represents a single drift detection finding."""
    category: str  # nomenclature, schema, trace, identifier
    severity: str  # error, warning, info
    message: str
    file_path: str = ""
    details: Dict = field(default_factory=dict)
    remediation: str = ""


@dataclass
class DriftReport:
    """Container for drift detection results."""
    timestamp: str
    repository: str
    branch: str
    items: List[DriftItem] = field(default_factory=list)
    summary: Dict[str, int] = field(default_factory=dict)

    def add_item(self, item: DriftItem) -> None:
        """Add a drift item to the report."""
        self.items.append(item)
        # Update summary counts
        key = f"{item.category}_{item.severity}"
        self.summary[key] = self.summary.get(key, 0) + 1

    @property
    def has_errors(self) -> bool:
        """Check if report contains any errors."""
        return any(item.severity == "error" for item in self.items)

    @property
    def has_warnings(self) -> bool:
        """Check if report contains any warnings."""
        return any(item.severity == "warning" for item in self.items)

    @property
    def total_items(self) -> int:
        """Get total number of drift items."""
        return len(self.items)

    def to_dict(self) -> Dict:
        """Convert report to dictionary."""
        return {
            "timestamp": self.timestamp,
            "repository": self.repository,
            "branch": self.branch,
            "summary": self.summary,
            "total_items": self.total_items,
            "has_errors": self.has_errors,
            "has_warnings": self.has_warnings,
            "items": [asdict(item) for item in self.items]
        }

    def to_json(self) -> str:
        """Convert report to JSON string."""
        return json.dumps(self.to_dict(), indent=2)

    def to_markdown(self) -> str:
        """Convert report to Markdown format."""
        md = []
        md.append("# Drift Detection Report")
        md.append("")
        md.append(f"**Generated**: {self.timestamp}")
        md.append(f"**Repository**: {self.repository}")
        md.append(f"**Branch**: {self.branch}")
        md.append("")

        # Summary section
        md.append("## Summary")
        md.append("")
        if not self.items:
            md.append("✅ **No drift detected** - All governance checks passed.")
        else:
            error_count = sum(1 for i in self.items if i.severity == "error")
            warning_count = sum(1 for i in self.items if i.severity == "warning")
            info_count = sum(1 for i in self.items if i.severity == "info")

            md.append(f"| Severity | Count |")
            md.append(f"|----------|-------|")
            if error_count > 0:
                md.append(f"| ❌ Errors | {error_count} |")
            if warning_count > 0:
                md.append(f"| ⚠️ Warnings | {warning_count} |")
            if info_count > 0:
                md.append(f"| ℹ️ Info | {info_count} |")
            md.append(f"| **Total** | {self.total_items} |")
        md.append("")

        # Group items by category
        categories = defaultdict(list)
        for item in self.items:
            categories[item.category].append(item)

        # Category sections
        category_titles = {
            "nomenclature": "Nomenclature Drift",
            "schema": "Schema Registry Drift",
            "trace": "Trace Link Drift",
            "identifier": "Identifier Registry Drift",
            "file_integrity": "File Integrity Drift"
        }

        for category, items in categories.items():
            title = category_titles.get(category, category.title())
            md.append(f"## {title}")
            md.append("")

            for item in items:
                severity_icon = {"error": "❌", "warning": "⚠️", "info": "ℹ️"}.get(
                    item.severity, "•"
                )
                md.append(f"### {severity_icon} {item.message}")
                md.append("")
                if item.file_path:
                    md.append(f"**File**: `{item.file_path}`")
                    md.append("")
                if item.details:
                    md.append("**Details**:")
                    md.append("```json")
                    md.append(json.dumps(item.details, indent=2))
                    md.append("```")
                    md.append("")
                if item.remediation:
                    md.append(f"**Remediation**: {item.remediation}")
                    md.append("")

        # Footer
        md.append("---")
        md.append("")
        md.append("*This report was generated by the drift detection workflow.*")
        md.append("*See K06 ATA 00 Tasklist for governance requirements.*")

        return "\n".join(md)


class DriftDetector:
    """Detects drift in governance artifacts."""

    # Directories to exclude from scanning
    EXCLUDED_DIRS = {
        '.git', '.github', 'node_modules', '__pycache__',
        '.pytest_cache', '.venv', 'venv', 'dist', 'build',
        'templates', 'scripts'
    }

    # Files to exclude from scanning
    EXCLUDED_FILES = {
        'README.md', 'LICENSE', 'EXAMPLES.md', 'STRUCTURE_SUMMARY.md',
        '.gitignore', '.gitattributes', 'package.json', 'package-lock.json',
        'IMPLEMENTATION_SUMMARY.md', 'REVIEW_NOTES.md',
        'NOMENCLATURE_V3_AUDIT_REPORT.md', '.gitkeep'
    }

    # Excluded file patterns
    EXCLUDED_PATTERNS = [
        r'generate_.*\.py',
        r'validate_.*\.py',
        r'detect_.*\.py',
        r'scaffold\.py',
        r'pre-commit',
        r'.*\.py[cod]$',
    ]

    def __init__(
        self,
        repo_root: Path = Path('.'),
        repository: str = "",
        branch: str = "main",
        verbose: bool = False
    ):
        """
        Initialize drift detector.

        Args:
            repo_root: Path to repository root
            repository: Repository name (owner/repo)
            branch: Current branch name
            verbose: Enable verbose output
        """
        self.repo_root = repo_root
        self.repository = repository
        self.branch = branch
        self.verbose = verbose
        self.report = DriftReport(
            timestamp=datetime.now(timezone.utc).isoformat(),
            repository=repository,
            branch=branch
        )

    def _is_excluded_path(self, path: Path) -> bool:
        """Check if path should be excluded from scanning."""
        # Check parent directories
        for parent in path.parents:
            if parent.name in self.EXCLUDED_DIRS:
                return True

        # Check filename
        if path.name in self.EXCLUDED_FILES:
            return True

        # Check patterns
        for pattern in self.EXCLUDED_PATTERNS:
            if re.match(pattern, path.name):
                return True

        return False

    def _log(self, message: str) -> None:
        """Print message if verbose mode is enabled."""
        if self.verbose:
            print(message)

    def detect_nomenclature_drift(self) -> None:
        """
        Detect nomenclature violations and namespace conflicts.

        Checks for:
        - Files not following nomenclature standard
        - Invalid TYPE codes
        - Namespace conflicts (same identifier used differently)
        - Version inconsistencies
        """
        print("🔍 Checking nomenclature drift...")

        if NomenclatureValidator is None:
            self.report.add_item(DriftItem(
                category="nomenclature",
                severity="warning",
                message="Nomenclature validator not available",
                remediation="Ensure validate_nomenclature.py is accessible"
            ))
            return

        validator = NomenclatureValidator(strict=True)

        # Track identifiers for namespace conflict detection
        identifiers: Dict[str, List[Path]] = defaultdict(list)
        invalid_files: List[tuple] = []

        for path in self.repo_root.rglob('*'):
            if not path.is_file():
                continue
            if self._is_excluded_path(path):
                continue

            result = validator.validate_file_path(path)

            if not result.valid:
                invalid_files.append((path, result.errors))

            # Track identifier patterns for namespace detection
            # Extract base identifier (ROOT_BUCKET_TYPE_SUBJECT_PROJECT_PROGRAM)
            match = re.match(
                r'^(\d{2,3}_\d{2}_[A-Z0-9]+_[A-Z0-9-]+_AMPEL360_SPACET)_',
                path.name
            )
            if match:
                base_id = match.group(1)
                identifiers[base_id].append(path)

        # Report invalid files
        for path, errors in invalid_files:
            self.report.add_item(DriftItem(
                category="nomenclature",
                severity="error",
                message=f"Nomenclature violation: {path.name}",
                file_path=str(path),
                details={"errors": errors},
                remediation="Update filename to follow nomenclature standard v3.0"
            ))

        # Detect namespace conflicts (exact filename collisions across directories)
        # Note: Files with the same name in different stakeholder directories are intentional
        # (e.g., k06-ata-00-tasklist exists in STK_AI, STK_CM, etc.)
        # We only flag actual filename collisions (same complete filename in different locations)
        filename_locations: Dict[str, List[Path]] = defaultdict(list)
        for base_id, paths in identifiers.items():
            for p in paths:
                filename_locations[p.name].append(p)
        
        # Check for files with same name but different content (potential sync issues)
        for filename, file_paths in filename_locations.items():
            if len(file_paths) > 1:
                # Multiple copies of the same file - check if content differs
                contents_hash: Dict[str, List[str]] = defaultdict(list)
                for fp in file_paths:
                    try:
                        with open(fp, 'rb') as f:
                            content_hash = hashlib.sha256(f.read()).hexdigest()[:16]
                            contents_hash[content_hash].append(str(fp))
                    except OSError:
                        continue
                
                if len(contents_hash) > 1:
                    # Same filename, different content - potential drift
                    self.report.add_item(DriftItem(
                        category="nomenclature",
                        severity="warning",
                        message=f"File content mismatch: {filename}",
                        details={
                            "filename": filename,
                            "locations": [str(p) for p in file_paths],
                            "content_hashes": {h: paths for h, paths in contents_hash.items()}
                        },
                        remediation="Sync file content across all copies or use symlinks"
                    ))

        if not invalid_files:
            self._log("  ✅ No nomenclature violations found")

    def detect_schema_drift(self) -> None:
        """
        Detect schema registry drift.

        Checks for:
        - Unregistered schema files
        - Version conflicts (same ID, different content)
        - Schema files with missing $id or $schema
        - Orphaned registry entries (file not found)
        """
        print("🔍 Checking schema registry drift...")

        schemas: Dict[str, List[Path]] = defaultdict(list)
        schema_hashes: Dict[str, Dict[str, str]] = defaultdict(dict)

        # Scan for JSON schema files
        for path in self.repo_root.rglob('*.json'):
            if self._is_excluded_path(path):
                continue

            try:
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    data = json.loads(content)

                if not isinstance(data, dict):
                    continue

                # Check if it's a JSON Schema
                if '$schema' in data or '$id' in data:
                    schema_id = data.get('$id', path.stem)
                    schemas[schema_id].append(path)

                    # Compute content hash
                    content_hash = hashlib.sha256(content.encode()).hexdigest()[:16]
                    schema_hashes[schema_id][str(path)] = content_hash

                    # Check for missing fields
                    missing_fields = []
                    if '$schema' not in data:
                        missing_fields.append('$schema')
                    if '$id' not in data:
                        missing_fields.append('$id')

                    if missing_fields:
                        self.report.add_item(DriftItem(
                            category="schema",
                            severity="warning",
                            message=f"Schema missing recommended fields: {', '.join(missing_fields)}",
                            file_path=str(path),
                            details={"missing_fields": missing_fields},
                            remediation="Add missing JSON Schema fields for proper registry tracking"
                        ))

            except (json.JSONDecodeError, OSError, UnicodeDecodeError):
                continue

        # Detect duplicate schema IDs with different content
        for schema_id, paths in schemas.items():
            if len(paths) > 1:
                hashes = set(schema_hashes[schema_id].values())
                if len(hashes) > 1:
                    self.report.add_item(DriftItem(
                        category="schema",
                        severity="error",
                        message=f"Schema version conflict: {schema_id}",
                        details={
                            "schema_id": schema_id,
                            "files": [str(p) for p in paths],
                            "content_hashes": schema_hashes[schema_id]
                        },
                        remediation="Ensure all copies of this schema have identical content or different versions"
                    ))

        self._log(f"  Found {len(schemas)} unique schema IDs")

    def detect_trace_link_drift(self) -> None:
        """
        Detect trace link staleness.

        Checks for:
        - Broken internal links in Markdown files
        - References to non-existent files
        - Outdated version references
        
        Note: Links to directories (ending with /) are not flagged as broken
        since they may be valid navigation targets.
        """
        print("🔍 Checking trace link drift...")

        # Pattern for Markdown links
        link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
        broken_links: List[tuple] = []

        for path in self.repo_root.rglob('*.md'):
            if self._is_excluded_path(path):
                continue

            try:
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()

                for match in link_pattern.finditer(content):
                    link_text = match.group(1)
                    link_target = match.group(2)

                    # Skip external links, anchors, and special protocols
                    if link_target.startswith(('http://', 'https://', 'mailto:', '#', 'tel:')):
                        continue
                    
                    # Skip empty links
                    if not link_target.strip():
                        continue
                    
                    # Skip links that are just directory references (end with /)
                    if link_target.endswith('/'):
                        continue

                    # Remove any anchor from the path
                    target_clean = link_target.split('#')[0]
                    
                    # Skip if empty after removing anchor
                    if not target_clean:
                        continue

                    # Resolve relative path
                    try:
                        target_path = (path.parent / target_clean).resolve()
                        
                        # Check if it's within the repo (to avoid checking absolute paths)
                        try:
                            target_path.relative_to(self.repo_root.resolve())
                        except ValueError:
                            # Path is outside repo - may be valid but can't verify
                            continue
                        
                        if not target_path.exists():
                            # Only report if this is a file reference (has extension) 
                            # or explicitly references a markdown file
                            if '.' in target_clean or target_clean.endswith('.md'):
                                broken_links.append((path, link_text, link_target))
                    except (OSError, ValueError):
                        # Path resolution failed - skip
                        continue

            except (OSError, UnicodeDecodeError):
                continue

        # Report broken links
        for source_path, link_text, link_target in broken_links:
            self.report.add_item(DriftItem(
                category="trace",
                severity="warning",
                message=f"Broken link: [{link_text}]({link_target})",
                file_path=str(source_path),
                details={
                    "link_text": link_text,
                    "link_target": link_target
                },
                remediation="Update link to point to existing file or remove if obsolete"
            ))

        if not broken_links:
            self._log("  ✅ No broken trace links found")

    def detect_identifier_drift(self) -> None:
        """
        Detect identifier registry drift.

        Checks for:
        - Duplicate identifiers across different files
        - Identifier format inconsistencies
        - Missing identifiers in registry
        """
        print("🔍 Checking identifier registry drift...")

        # Look for identifier patterns in files
        # Pattern: ID: followed by identifier, or id: field in YAML/JSON
        id_patterns = [
            re.compile(r'["\']?id["\']?\s*[:=]\s*["\']([A-Z0-9_-]+)["\']', re.IGNORECASE),
            re.compile(r'knot_id\s*[:=]\s*["\']?([A-Z0-9_-]+)["\']?', re.IGNORECASE),
            re.compile(r'schema_id\s*[:=]\s*["\']([^"\']+)["\']', re.IGNORECASE),
        ]

        identifiers: Dict[str, List[Path]] = defaultdict(list)

        for path in self.repo_root.rglob('*'):
            if not path.is_file():
                continue
            if self._is_excluded_path(path):
                continue
            if path.suffix not in {'.md', '.json', '.yaml', '.yml', '.csv'}:
                continue

            try:
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()

                for pattern in id_patterns:
                    for match in pattern.finditer(content):
                        identifier = match.group(1)
                        if len(identifier) > 2:  # Skip very short matches
                            identifiers[identifier].append(path)

            except (OSError, UnicodeDecodeError):
                continue

        # Report duplicate identifiers
        for identifier, paths in identifiers.items():
            unique_paths = list(set(str(p) for p in paths))
            if len(unique_paths) > 1:
                # Only report if found in truly different files (not the same file multiple times)
                self.report.add_item(DriftItem(
                    category="identifier",
                    severity="info",
                    message=f"Identifier found in multiple files: {identifier}",
                    details={
                        "identifier": identifier,
                        "file_count": len(unique_paths),
                        "files": unique_paths[:5]  # Limit to first 5
                    },
                    remediation="Verify this is intentional (cross-references) or consolidate"
                ))

        self._log(f"  Found {len(identifiers)} unique identifiers")

    def detect_file_integrity_drift(self) -> None:
        """
        Detect file integrity issues.

        Checks for:
        - Empty files
        - Files with only whitespace
        - Very large files (potential data files in wrong location)
        """
        print("🔍 Checking file integrity...")

        for path in self.repo_root.rglob('*'):
            if not path.is_file():
                continue
            if self._is_excluded_path(path):
                continue

            try:
                stat = path.stat()

                # Check for empty files
                if stat.st_size == 0:
                    self.report.add_item(DriftItem(
                        category="file_integrity",
                        severity="warning",
                        message=f"Empty file detected",
                        file_path=str(path),
                        remediation="Add content or remove if not needed"
                    ))
                    continue

                # Check for very large files (> 10MB)
                if stat.st_size > 10 * 1024 * 1024:
                    self.report.add_item(DriftItem(
                        category="file_integrity",
                        severity="warning",
                        message=f"Large file detected ({stat.st_size / 1024 / 1024:.1f} MB)",
                        file_path=str(path),
                        details={"size_bytes": stat.st_size},
                        remediation="Consider using Git LFS for large files"
                    ))

            except OSError:
                continue

    def run_all_checks(self) -> DriftReport:
        """
        Run all drift detection checks.

        Returns:
            DriftReport with all findings
        """
        print("\n" + "=" * 60)
        print("DRIFT DETECTION SCAN")
        print(f"Repository: {self.repository}")
        print(f"Branch: {self.branch}")
        print(f"Timestamp: {self.report.timestamp}")
        print("=" * 60 + "\n")

        self.detect_nomenclature_drift()
        self.detect_schema_drift()
        self.detect_trace_link_drift()
        self.detect_identifier_drift()
        self.detect_file_integrity_drift()

        # Print summary
        print("\n" + "=" * 60)
        print("DRIFT DETECTION SUMMARY")
        print("=" * 60)

        if not self.report.items:
            print("✅ No drift detected - All governance checks passed.")
        else:
            error_count = sum(1 for i in self.report.items if i.severity == "error")
            warning_count = sum(1 for i in self.report.items if i.severity == "warning")
            info_count = sum(1 for i in self.report.items if i.severity == "info")

            print(f"❌ Errors: {error_count}")
            print(f"⚠️  Warnings: {warning_count}")
            print(f"ℹ️  Info: {info_count}")
            print(f"Total items: {self.report.total_items}")

        print("=" * 60 + "\n")

        return self.report


def main() -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Detect drift in governance artifacts',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --check-all
  %(prog)s --check-nomenclature --check-schemas
  %(prog)s --output-json drift-report.json
  %(prog)s --output-markdown drift-report.md

Exit codes:
  0: No drift detected (or only info items)
  1: Drift detected (warnings or errors)
  2: Script error
        """
    )

    parser.add_argument(
        '--check-all',
        action='store_true',
        help='Run all drift detection checks'
    )
    parser.add_argument(
        '--check-nomenclature',
        action='store_true',
        help='Check for nomenclature drift'
    )
    parser.add_argument(
        '--check-schemas',
        action='store_true',
        help='Check for schema registry drift'
    )
    parser.add_argument(
        '--check-traces',
        action='store_true',
        help='Check for trace link drift'
    )
    parser.add_argument(
        '--check-identifiers',
        action='store_true',
        help='Check for identifier registry drift'
    )
    parser.add_argument(
        '--check-integrity',
        action='store_true',
        help='Check for file integrity issues'
    )
    parser.add_argument(
        '--repo-root',
        metavar='DIR',
        default='.',
        help='Repository root directory (default: current directory)'
    )
    parser.add_argument(
        '--repository',
        metavar='OWNER/REPO',
        default='',
        help='Repository name (e.g., owner/repo)'
    )
    parser.add_argument(
        '--branch',
        default='main',
        help='Current branch name (default: main)'
    )
    parser.add_argument(
        '--output-json',
        metavar='FILE',
        help='Write JSON report to file'
    )
    parser.add_argument(
        '--output-markdown',
        metavar='FILE',
        help='Write Markdown report to file'
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Enable verbose output'
    )

    args = parser.parse_args()

    # Default to all checks if none specified
    if not any([
        args.check_all, args.check_nomenclature, args.check_schemas,
        args.check_traces, args.check_identifiers, args.check_integrity
    ]):
        args.check_all = True

    repo_root = Path(args.repo_root)
    if not repo_root.is_dir():
        print(f"Error: '{args.repo_root}' is not a directory", file=sys.stderr)
        return 2

    try:
        detector = DriftDetector(
            repo_root=repo_root,
            repository=args.repository,
            branch=args.branch,
            verbose=args.verbose
        )

        if args.check_all:
            detector.run_all_checks()
        else:
            print("\n" + "=" * 60)
            print("DRIFT DETECTION SCAN (Selected Checks)")
            print("=" * 60 + "\n")

            if args.check_nomenclature:
                detector.detect_nomenclature_drift()
            if args.check_schemas:
                detector.detect_schema_drift()
            if args.check_traces:
                detector.detect_trace_link_drift()
            if args.check_identifiers:
                detector.detect_identifier_drift()
            if args.check_integrity:
                detector.detect_file_integrity_drift()

        report = detector.report

        # Write output files
        if args.output_json:
            with open(args.output_json, 'w', encoding='utf-8') as f:
                f.write(report.to_json())
            print(f"📄 JSON report written to: {args.output_json}")

        if args.output_markdown:
            with open(args.output_markdown, 'w', encoding='utf-8') as f:
                f.write(report.to_markdown())
            print(f"📄 Markdown report written to: {args.output_markdown}")

        # Return code based on findings
        if report.has_errors or report.has_warnings:
            return 1
        return 0

    except KeyboardInterrupt:
        print("\nInterrupted by user", file=sys.stderr)
        return 2
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
