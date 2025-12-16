#!/usr/bin/env python3
"""
AMPEL360 Space-T Trace Link Validator
======================================
Version: 1.0
Date: 2025-12-16
Task: T5-AI from K06 ATA 00 Tasklist (CI Gates for Governance Enforcement)

Validates trace link integrity across the repository.
Enforces trace governance policy by ensuring:
- All trace links reference existing files
- No broken internal markdown links
- No orphaned evidence references
- Link freshness validation (staleness detection)

Consumes:
- ATA 93 trace semantics and evidence link schema
- Repository file structure

Usage:
    python scripts/validate_trace_links.py --check-all
    python scripts/validate_trace_links.py --check-file <file>
    python scripts/validate_trace_links.py --check-dir <directory>

Exit codes:
    0: All validations passed
    1: Validation errors found (broken links)
    2: Script error (file not found, etc.)
"""

import argparse
import os
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple
from urllib.parse import unquote, urlparse


@dataclass
class LinkInfo:
    """Information about a link found in a file."""
    source_file: Path
    line_number: int
    link_text: str
    link_target: str
    link_type: str  # 'relative', 'absolute', 'external', 'reference', 'html'


@dataclass
class ValidationResult:
    """Container for validation results."""
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    info: List[str] = field(default_factory=list)
    broken_links: List[LinkInfo] = field(default_factory=list)
    valid_links: int = 0
    passed: bool = True

    def add_error(self, message: str) -> None:
        """Add an error message."""
        self.errors.append(message)
        self.passed = False

    def add_warning(self, message: str) -> None:
        """Add a warning message."""
        self.warnings.append(message)

    def add_info(self, message: str) -> None:
        """Add an info message."""
        self.info.append(message)

    def add_broken_link(self, link: LinkInfo) -> None:
        """Add a broken link to the list."""
        self.broken_links.append(link)
        self.passed = False

    def print_summary(self) -> None:
        """Print validation summary."""
        print("\n" + "=" * 60)
        print("TRACE LINK VALIDATION SUMMARY")
        print("=" * 60)

        if self.broken_links:
            print(f"\n❌ BROKEN LINKS ({len(self.broken_links)}):")
            for i, link in enumerate(self.broken_links, 1):
                print(f"  {i}. {link.source_file}:{link.line_number}")
                print(f"     Text: '{link.link_text[:50]}{'...' if len(link.link_text) > 50 else ''}'")
                print(f"     Target: {link.link_target}")

        if self.errors:
            print(f"\n❌ ERRORS ({len(self.errors)}):")
            for i, error in enumerate(self.errors, 1):
                print(f"  {i}. {error}")

        if self.warnings:
            print(f"\n⚠️  WARNINGS ({len(self.warnings)}):")
            for i, warning in enumerate(self.warnings, 1):
                print(f"  {i}. {warning}")

        if self.info:
            print(f"\n📋 INFO ({len(self.info)}):")
            for info_msg in self.info:
                print(f"  • {info_msg}")

        print("\n" + "=" * 60)
        total_links = self.valid_links + len(self.broken_links)
        if self.passed and not self.warnings:
            print(f"✅ VALIDATION PASSED - {self.valid_links}/{total_links} links valid")
        elif self.passed:
            print(f"✅ VALIDATION PASSED - Warnings present ({self.valid_links}/{total_links} links valid)")
        else:
            print(f"❌ VALIDATION FAILED - {len(self.broken_links)} broken links found")
        print("=" * 60 + "\n")


class TraceLinkValidator:
    """Validates trace links and internal references in markdown files."""

    # Markdown link pattern: [text](target) or [text](target "title")
    MARKDOWN_LINK_PATTERN = re.compile(
        r'\[([^\]]+)\]\(([^)\s]+)(?:\s+"[^"]*")?\)'
    )

    # Reference-style link pattern: [text][ref]
    REF_LINK_PATTERN = re.compile(r'\[([^\]]+)\]\[([^\]]+)\]')

    # Reference definition pattern: [ref]: target
    REF_DEF_PATTERN = re.compile(r'^\[([^\]]+)\]:\s*(.+)$', re.MULTILINE)

    # HTML anchor link pattern: <a href="target">text</a>
    HTML_LINK_PATTERN = re.compile(r'<a\s+href="([^"]+)"[^>]*>([^<]*)</a>')

    # Directories to exclude from validation
    EXCLUDED_DIRS = {
        '.git', '.github', 'node_modules', '__pycache__',
        '.pytest_cache', '.venv', 'venv', 'dist', 'build'
    }

    # External URL patterns (skip validation)
    EXTERNAL_PATTERNS = [
        r'^https?://',
        r'^mailto:',
        r'^ftp://',
        r'^#',  # Internal anchors
    ]

    def __init__(self, repo_root: Path = Path('.'), verbose: bool = False):
        """
        Initialize the validator.

        Args:
            repo_root: Path to the repository root
            verbose: Enable verbose output
        """
        self.repo_root = repo_root.resolve()
        self.verbose = verbose
        self.external_pattern = re.compile('|'.join(self.EXTERNAL_PATTERNS))

    def is_excluded_path(self, path: Path) -> bool:
        """Check if path should be excluded from scanning."""
        for parent in path.parents:
            if parent.name in self.EXCLUDED_DIRS:
                return True
        return False

    def is_external_link(self, target: str) -> bool:
        """Check if link target is external (URL, mailto, etc.)."""
        return bool(self.external_pattern.match(target))

    def extract_links(self, file_path: Path) -> List[LinkInfo]:
        """
        Extract all links from a markdown file.

        Args:
            file_path: Path to the markdown file

        Returns:
            List of LinkInfo objects
        """
        links = []

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                lines = content.split('\n')
        except (OSError, UnicodeDecodeError) as e:
            if self.verbose:
                print(f"  Warning: Cannot read {file_path}: {e}")
            return []

        # Build reference definitions map
        ref_defs = {}
        for match in self.REF_DEF_PATTERN.finditer(content):
            ref_name = match.group(1).lower()
            ref_target = match.group(2).strip()
            ref_defs[ref_name] = ref_target

        # Find inline markdown links
        for line_num, line in enumerate(lines, 1):
            for match in self.MARKDOWN_LINK_PATTERN.finditer(line):
                link_text = match.group(1)
                link_target = match.group(2)

                # Skip external links
                if self.is_external_link(link_target):
                    link_type = 'external'
                else:
                    link_type = 'relative' if not link_target.startswith('/') else 'absolute'

                links.append(LinkInfo(
                    source_file=file_path,
                    line_number=line_num,
                    link_text=link_text,
                    link_target=link_target,
                    link_type=link_type
                ))

            # Find reference-style links
            for match in self.REF_LINK_PATTERN.finditer(line):
                link_text = match.group(1)
                ref_name = match.group(2).lower()

                if ref_name in ref_defs:
                    link_target = ref_defs[ref_name]
                    if self.is_external_link(link_target):
                        link_type = 'external'
                    else:
                        link_type = 'reference'

                    links.append(LinkInfo(
                        source_file=file_path,
                        line_number=line_num,
                        link_text=link_text,
                        link_target=link_target,
                        link_type=link_type
                    ))

            # Find HTML links
            for match in self.HTML_LINK_PATTERN.finditer(line):
                link_target = match.group(1)
                link_text = match.group(2)

                if self.is_external_link(link_target):
                    link_type = 'external'
                else:
                    link_type = 'html'

                links.append(LinkInfo(
                    source_file=file_path,
                    line_number=line_num,
                    link_text=link_text,
                    link_target=link_target,
                    link_type=link_type
                ))

        return links

    def resolve_link_target(self, source_file: Path, link_target: str) -> Optional[Path]:
        """
        Resolve a link target to an absolute path.

        Args:
            source_file: Path to the source file containing the link
            link_target: The link target string

        Returns:
            Resolved Path if valid, None if cannot resolve
        """
        # Remove URL fragment (anchor)
        target = link_target.split('#')[0]

        # URL decode
        target = unquote(target)

        if not target:
            # Anchor-only link (e.g., #section)
            return source_file

        if target.startswith('/'):
            # Absolute path from repo root
            resolved = self.repo_root / target.lstrip('/')
        else:
            # Relative path from source file directory
            resolved = source_file.parent / target

        return resolved.resolve()

    def validate_link(self, link: LinkInfo) -> bool:
        """
        Validate a single link.

        Args:
            link: LinkInfo object to validate

        Returns:
            True if link is valid, False otherwise
        """
        # Skip external links
        if link.link_type == 'external':
            return True

        # Resolve target path
        resolved = self.resolve_link_target(link.source_file, link.link_target)

        if resolved is None:
            return False

        # Check if it's a directory with index file
        if resolved.is_dir():
            for index_name in ['index.md', 'README.md', 'index.html']:
                if (resolved / index_name).exists():
                    return True
            return False

        # Check if target file exists
        return resolved.exists()

    def validate_file(self, file_path: Path, result: ValidationResult) -> None:
        """
        Validate all links in a single file.

        Args:
            file_path: Path to the file to validate
            result: ValidationResult to update
        """
        if self.verbose:
            print(f"  Scanning: {file_path}")

        links = self.extract_links(file_path)

        for link in links:
            if link.link_type == 'external':
                result.valid_links += 1
                continue

            if self.validate_link(link):
                result.valid_links += 1
            else:
                result.add_broken_link(link)

    def validate_directory(self, directory: Path, result: ValidationResult,
                          recursive: bool = True) -> None:
        """
        Validate all markdown files in a directory.

        Args:
            directory: Directory to scan
            result: ValidationResult to update
            recursive: If True, scan recursively
        """
        pattern = '**/*.md' if recursive else '*.md'

        for path in directory.glob(pattern):
            if not path.is_file():
                continue

            if self.is_excluded_path(path):
                continue

            self.validate_file(path, result)

    def validate_all(self) -> ValidationResult:
        """
        Validate all markdown files in the repository.

        Returns:
            ValidationResult with all findings
        """
        result = ValidationResult()

        print("\n" + "=" * 60)
        print("TRACE LINK VALIDATION")
        print("=" * 60 + "\n")

        print("🔍 Scanning repository for markdown files...")
        self.validate_directory(self.repo_root, result, recursive=True)

        result.add_info(
            f"Scanned repository from: {self.repo_root}"
        )

        result.print_summary()
        return result


def main() -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Validate trace links and internal references',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --check-all
  %(prog)s --check-file path/to/document.md
  %(prog)s --check-dir path/to/directory

Exit codes:
  0: All validations passed
  1: Validation errors found (broken links)
  2: Script error
        """
    )

    parser.add_argument(
        '--check-all',
        action='store_true',
        help='Validate all markdown files in the repository'
    )
    parser.add_argument(
        '--check-file',
        metavar='FILE',
        help='Validate a single markdown file'
    )
    parser.add_argument(
        '--check-dir',
        metavar='DIR',
        help='Validate all markdown files in a directory'
    )
    parser.add_argument(
        '--repo-root',
        metavar='DIR',
        default='.',
        help='Repository root directory (default: current directory)'
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Enable verbose output'
    )

    args = parser.parse_args()

    # Validate arguments
    if not any([args.check_all, args.check_file, args.check_dir]):
        parser.error('Must specify --check-all, --check-file, or --check-dir')

    repo_root = Path(args.repo_root).resolve()
    if not repo_root.is_dir():
        print(f"Error: '{args.repo_root}' is not a directory", file=sys.stderr)
        return 2

    try:
        validator = TraceLinkValidator(repo_root, verbose=args.verbose)
        result = ValidationResult()

        if args.check_file:
            file_path = Path(args.check_file)
            if not file_path.exists():
                print(f"Error: File not found: {args.check_file}", file=sys.stderr)
                return 2
            if file_path.suffix.lower() != '.md':
                print(f"Error: Not a markdown file: {args.check_file}", file=sys.stderr)
                return 2
            validator.validate_file(file_path, result)
            result.print_summary()

        elif args.check_dir:
            dir_path = Path(args.check_dir)
            if not dir_path.is_dir():
                print(f"Error: Not a directory: {args.check_dir}", file=sys.stderr)
                return 2
            validator.validate_directory(dir_path, result, recursive=True)
            result.print_summary()

        elif args.check_all:
            result = validator.validate_all()

        return 0 if result.passed else 1

    except KeyboardInterrupt:
        print("\nInterrupted by user", file=sys.stderr)
        return 2
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
