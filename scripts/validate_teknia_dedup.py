#!/usr/bin/env python3
"""
AMPEL360 Space-T TEKNIA Deduplication Validator
================================================
Version: 1.0
Date: 2025-12-16
Task: T7-AI from K06 ATA 00 Tasklist

Validates hash uniqueness and namespace separation to support TEKNIA
evidence-first packaging rules. Ensures no duplicate content exists
and that identifiers are properly segregated across namespaces.

Performs:
1. Content Hash Validation - Detects duplicate files by SHA-256 hash
2. Namespace Separation Checks - Detects duplicate identifiers across namespaces

Usage:
    python scripts/validate_teknia_dedup.py --check-all
    python scripts/validate_teknia_dedup.py --check-hash
    python scripts/validate_teknia_dedup.py --check-namespace

Exit codes:
    0: All validations passed
    1: Validation errors found (duplicates detected)
    2: Script error (file not found, etc.)
"""

import argparse
import csv
import hashlib
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple


@dataclass
class DuplicateEntry:
    """Represents a group of duplicate files or identifiers."""
    hash_or_id: str
    items: List[str]
    category: str  # 'file' or 'identifier'


@dataclass
class ValidationResult:
    """Container for validation results."""
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    info: List[str] = field(default_factory=list)
    duplicates: List[DuplicateEntry] = field(default_factory=list)
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

    def add_duplicate(self, hash_or_id: str, items: List[str], category: str) -> None:
        """Record a duplicate group."""
        self.duplicates.append(DuplicateEntry(hash_or_id, items, category))
        self.passed = False

    def print_summary(self) -> None:
        """Print validation summary."""
        print("\n" + "=" * 60)
        print("TEKNIA DEDUPLICATION VALIDATION SUMMARY")
        print("=" * 60)

        if self.errors:
            print(f"\n❌ ERRORS ({len(self.errors)}):")
            for i, error in enumerate(self.errors, 1):
                print(f"  {i}. {error}")

        if self.duplicates:
            print(f"\n🔁 DUPLICATES DETECTED ({len(self.duplicates)}):")
            for dup in self.duplicates:
                print(f"\n  [{dup.category.upper()}] {dup.hash_or_id[:16]}...")
                for item in dup.items:
                    print(f"    • {item}")

        if self.warnings:
            print(f"\n⚠️  WARNINGS ({len(self.warnings)}):")
            for i, warning in enumerate(self.warnings, 1):
                print(f"  {i}. {warning}")

        if self.info:
            print(f"\n📋 INFO ({len(self.info)}):")
            for info_msg in self.info:
                print(f"  • {info_msg}")

        print("\n" + "=" * 60)
        if self.passed and not self.warnings:
            print("✅ TEKNIA DEDUP VALIDATION PASSED - No duplicates or conflicts")
        elif self.passed:
            print("✅ TEKNIA DEDUP VALIDATION PASSED - Warnings present but no errors")
        else:
            print("❌ TEKNIA DEDUP VALIDATION FAILED - Duplicates detected")
        print("=" * 60 + "\n")


class TekniaDedupValidator:
    """Validates hash uniqueness and namespace separation for TEKNIA compliance."""

    # Directories to exclude from hash scanning
    EXCLUDED_DIRS = {
        '.git', '.github', 'node_modules', '__pycache__',
        '.pytest_cache', '.venv', 'venv', 'dist', 'build'
    }

    # Files to exclude from hash scanning
    EXCLUDED_FILES = {
        '.gitignore', '.gitattributes', '.DS_Store', 'Thumbs.db',
        'package-lock.json', '.eslintcache'
    }

    # File extensions to include in hash validation
    INCLUDE_EXTENSIONS = {
        '.md', '.json', '.yaml', '.yml', '.csv', '.xml', '.xlsx',
        '.py', '.js', '.ts', '.txt'
    }

    # Patterns for files that are expected to have duplicates across stakeholders
    # These are allowlisted from being flagged as errors
    ALLOWLISTED_DUPLICATE_PATTERNS = [
        # Tasklist files are intentionally duplicated across stakeholder folders
        # Match patterns like: k10-ata-10-tasklist_v01.md
        r'-tasklist_v\d+\.md$',
        # README files may have similar content
        r'README\.md$',
        # Template placeholders: Only allowlist files in the templates/ directory
        r'templates/[A-Z]+\.md$',
    ]

    # Patterns for extracting identifiers from files
    IDENTIFIER_PATTERNS = {
        # DATUM-SYSTEM-NNN, ZONE-SYSTEM-NNN, ENVELOPE-SYSTEM-NNN patterns
        'dimensional': re.compile(
            r'\b(DATUM|ZONE|ENVELOPE)-([A-Z]+)-(\d{3})(?:-([A-Z0-9]+))?\b'
        ),
        # URN-style identifiers with proper segment structure
        'urn': re.compile(
            r'urn:ampel360:spacet:(?:[a-z0-9]+(?:-[a-z0-9]+)*:)*[a-z0-9]+(?:-[a-z0-9]+)*'
        ),
        # Schema $id fields
        'schema_id': re.compile(
            r'"\$id"\s*:\s*"([^"]+)"'
        ),
        # Requirement IDs (REQ-XXX-NNN pattern)
        'requirement': re.compile(
            r'\bREQ-([A-Z]+)-(\d{3,4})\b'
        ),
        # Knot IDs (K01-K14)
        'knot': re.compile(
            r'\bK(0[1-9]|1[0-4])\b'
        )
    }

    # Registry file patterns following nomenclature standard
    REGISTRY_PATTERNS = [
        '**/identifier-registry*.md',
        '**/identifier-registry*.csv',
        '**/schema-registry*.csv',
        '**/[0-9][0-9]_[0-9][0-9]_CAT_*_*_identifier-registry_v[0-9][0-9].md'
    ]

    def __init__(self, repo_root: Path = Path('.'), verbose: bool = False,
                 strict: bool = False):
        """
        Initialize the validator.

        Args:
            repo_root: Path to the repository root
            verbose: Enable verbose output
            strict: If True, flag all duplicates as errors; if False, allowlist expected patterns
        """
        self.repo_root = repo_root
        self.verbose = verbose
        self.strict = strict
        self._compiled_allowlist = [
            re.compile(pattern) for pattern in self.ALLOWLISTED_DUPLICATE_PATTERNS
        ]

    def _is_allowlisted_duplicate(self, path: Path) -> bool:
        """Check if a file path matches any allowlisted duplicate pattern."""
        # Use relative path from repo root for matching (allows path-based patterns)
        try:
            rel_path = str(path.relative_to(self.repo_root))
        except ValueError:
            rel_path = path.name
        
        for pattern in self._compiled_allowlist:
            # Try matching against relative path first, then filename
            if pattern.search(rel_path):
                return True
        return False

    def _is_excluded_path(self, path: Path) -> bool:
        """Check if path should be excluded from scanning."""
        for parent in path.parents:
            if parent.name in self.EXCLUDED_DIRS:
                return True
        return path.name in self.EXCLUDED_FILES

    def _should_include_file(self, path: Path) -> bool:
        """Check if file should be included in hash validation."""
        if self._is_excluded_path(path):
            return False
        return path.suffix.lower() in self.INCLUDE_EXTENSIONS

    def _compute_file_hash(self, path: Path) -> Optional[str]:
        """
        Compute SHA-256 hash of file content.

        Args:
            path: Path to the file

        Returns:
            SHA-256 hex digest or None if file cannot be read
        """
        try:
            with open(path, 'rb') as f:
                return hashlib.sha256(f.read()).hexdigest()
        except OSError:
            return None

    def validate_hash_uniqueness(self, result: ValidationResult) -> Dict[str, List[Path]]:
        """
        Validate that all files have unique content hashes.

        Args:
            result: ValidationResult to update

        Returns:
            Dictionary mapping hashes to list of file paths
        """
        print("🔍 Scanning files for content hash uniqueness...")

        hash_to_files: Dict[str, List[Path]] = {}
        file_count = 0

        for path in self.repo_root.rglob('*'):
            if not path.is_file():
                continue

            if not self._should_include_file(path):
                continue

            file_hash = self._compute_file_hash(path)
            if file_hash:
                if file_hash not in hash_to_files:
                    hash_to_files[file_hash] = []
                hash_to_files[file_hash].append(path)
                file_count += 1

                if self.verbose:
                    print(f"  Hashed: {path}")

        # Find duplicates
        duplicates = {
            h: paths for h, paths in hash_to_files.items()
            if len(paths) > 1
        }

        # Separate allowlisted from problematic duplicates
        allowlisted_count = 0
        problematic_duplicates = {}

        for file_hash, paths in duplicates.items():
            # Check if all paths match allowlisted patterns
            all_allowlisted = all(
                self._is_allowlisted_duplicate(p) for p in paths
            )

            if all_allowlisted and not self.strict:
                allowlisted_count += 1
                if self.verbose:
                    print(f"  ℹ️  Allowlisted duplicate group: {file_hash[:16]}...")
            else:
                problematic_duplicates[file_hash] = paths

        if problematic_duplicates:
            for file_hash, paths in problematic_duplicates.items():
                # Get relative paths for cleaner output
                rel_paths = [str(p.relative_to(self.repo_root)) for p in paths]
                result.add_duplicate(file_hash, rel_paths, 'file')
                result.add_error(
                    f"Duplicate content detected: {len(paths)} files share hash {file_hash[:16]}..."
                )
        else:
            result.add_info("No problematic duplicate file content detected")

        if allowlisted_count > 0:
            result.add_info(
                f"{allowlisted_count} allowlisted duplicate groups (expected tasklist copies, etc.)"
            )

        result.add_info(
            f"Scanned {file_count} files, found {len(duplicates)} total duplicate groups "
            f"({len(problematic_duplicates)} problematic, {allowlisted_count} allowlisted)"
        )

        return hash_to_files

    def _extract_identifiers_from_file(self, path: Path) -> Dict[str, Set[str]]:
        """
        Extract identifiers from a file based on patterns.

        Args:
            path: Path to the file

        Returns:
            Dictionary mapping identifier type to set of identifiers found
        """
        identifiers: Dict[str, Set[str]] = {}

        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()

            for id_type, pattern in self.IDENTIFIER_PATTERNS.items():
                matches = pattern.findall(content)
                if matches:
                    if id_type not in identifiers:
                        identifiers[id_type] = set()
                    # Handle different match structures based on pattern type
                    for match in matches:
                        if id_type == 'dimensional':
                            # match is a tuple: (DATUM|ZONE|ENVELOPE, SYSTEM, NNN, optional variant)
                            full_id = f"{match[0]}-{match[1]}-{match[2]}"
                            if match[3]:  # Has variant
                                full_id += f"-{match[3]}"
                            identifiers[id_type].add(full_id)
                        elif id_type == 'requirement':
                            # match is a tuple: (SYSTEM, NNN)
                            # Ensure the numeric portion is zero-padded to at least 3 digits
                            num = match[1].zfill(3)
                            identifiers[id_type].add(f"REQ-{match[0]}-{num}")
                        elif id_type == 'knot':
                            # match is a string like '05' - prepend 'K' to the matched digits
                            identifiers[id_type].add(f"K{match}")
                        elif id_type == 'schema_id':
                            # match is a string: the captured $id value
                            identifiers[id_type].add(match)
                        else:
                            # fallback: add as string (handles 'urn' which returns strings)
                            if isinstance(match, tuple):
                                identifiers[id_type].add(str(match))
                            else:
                                identifiers[id_type].add(match)

        except (OSError, UnicodeDecodeError):
            # Silently skip files that cannot be read (binary files, encoding issues)
            pass

        return identifiers

    def _find_registry_files(self) -> List[Path]:
        """
        Find all identifier registry files in the repository.

        Returns:
            List of paths to registry files
        """
        registries = []
        for pattern in self.REGISTRY_PATTERNS:
            registries.extend(self.repo_root.glob(pattern))
        return list(set(registries))

    def _parse_registry_identifiers(self, path: Path) -> Dict[str, Tuple[str, str]]:
        """
        Parse identifiers from a registry file.

        Args:
            path: Path to the registry file

        Returns:
            Dictionary mapping identifier to (namespace, source_file) tuple
        """
        identifiers: Dict[str, Tuple[str, str]] = {}
        source = str(path.relative_to(self.repo_root))

        # Determine namespace from file path
        namespace = self._extract_namespace_from_path(path)

        try:
            if path.suffix == '.csv':
                # Parse CSV registry
                with open(path, 'r', encoding='utf-8') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        # Look for common identifier column names
                        for col in ['id', 'identifier', 'schema_id', 'ID', 'Identifier']:
                            if col in row and row[col]:
                                identifiers[row[col]] = (namespace, source)
                                break

            elif path.suffix == '.md':
                # Parse markdown registry - look for identifier patterns
                extracted = self._extract_identifiers_from_file(path)
                for id_type, ids in extracted.items():
                    for identifier in ids:
                        identifiers[identifier] = (namespace, source)

        except (OSError, UnicodeDecodeError, csv.Error):
            # Silently skip files that cannot be read or parsed
            pass

        return identifiers

    def _extract_namespace_from_path(self, path: Path) -> str:
        """
        Extract namespace from file path based on folder structure.

        Namespace precedence order (first match wins):
        1. STK_* (stakeholder namespaces) - highest priority
        2. K01-K14_* (Knot folders) - domain-specific namespaces
        3. ATA_* (ATA chapter folders)
        4. Top-level folder under repo root - fallback

        This precedence ensures that stakeholder-scoped files are properly
        attributed to their stakeholder namespace even if they are nested
        within Knot or ATA subfolders.

        Args:
            path: Path to the file

        Returns:
            Namespace string
        """
        # Priority 1: Look for STK_* folder names (stakeholder namespaces)
        for parent in path.parents:
            if parent.name.startswith('STK_'):
                return parent.name

        # Priority 2: Look for KNOT folder names (K01-K14 with underscore suffix)
        for parent in path.parents:
            if re.match(r'^K(0[1-9]|1[0-4])_', parent.name):
                return parent.name

        # Priority 3: Look for ATA folder names
        for parent in path.parents:
            if parent.name.startswith('ATA_'):
                return parent.name

        # Priority 4: Default to top-level folder under repo root
        try:
            relative = path.relative_to(self.repo_root)
            return str(relative.parts[0]) if relative.parts else 'root'
        except ValueError:
            return 'unknown'

    def validate_namespace_separation(self, result: ValidationResult) -> None:
        """
        Validate that identifiers are properly separated across namespaces.

        Checks for:
        1. Duplicate identifiers within the same namespace
        2. Identifier conflicts across different namespaces (same ID, different sources)

        Args:
            result: ValidationResult to update
        """
        print("🔍 Checking namespace separation and identifier uniqueness...")

        # Collect all identifiers with their namespaces
        all_identifiers: Dict[str, List[Tuple[str, str]]] = {}  # id -> [(namespace, source), ...]

        # Scan registry files
        registries = self._find_registry_files()
        result.add_info(f"Found {len(registries)} registry files")

        for registry in registries:
            if self.verbose:
                print(f"  Parsing registry: {registry}")

            registry_ids = self._parse_registry_identifiers(registry)
            for identifier, (namespace, source) in registry_ids.items():
                if identifier not in all_identifiers:
                    all_identifiers[identifier] = []
                all_identifiers[identifier].append((namespace, source))

        # Scan markdown files for identifiers (beyond registries)
        for path in self.repo_root.rglob('*.md'):
            if self._is_excluded_path(path):
                continue
            if path in registries:  # Already processed
                continue

            extracted = self._extract_identifiers_from_file(path)
            namespace = self._extract_namespace_from_path(path)
            source = str(path.relative_to(self.repo_root))

            for id_type, ids in extracted.items():
                for identifier in ids:
                    if identifier not in all_identifiers:
                        all_identifiers[identifier] = []
                    all_identifiers[identifier].append((namespace, source))

        # Check for duplicate identifiers
        duplicates_found = 0
        namespace_conflicts = 0

        for identifier, locations in all_identifiers.items():
            if len(locations) > 1:
                # Check if duplicates are in the same namespace or different
                namespaces = set(loc[0] for loc in locations)

                if len(namespaces) == 1:
                    # Same namespace - might be intentional references
                    # Only flag if it appears in multiple distinct files
                    sources = set(loc[1] for loc in locations)
                    if len(sources) > 1:
                        # Multiple definitions in same namespace
                        duplicates_found += 1
                        result.add_warning(
                            f"Identifier '{identifier}' appears in multiple files "
                            f"within namespace '{list(namespaces)[0]}': "
                            f"{', '.join(sources)}"
                        )
                else:
                    # Different namespaces - potential conflict
                    # This is a warning, not error, as some identifiers may be
                    # legitimately referenced across namespaces
                    namespace_conflicts += 1
                    if self.verbose:
                        result.add_info(
                            f"Identifier '{identifier}' found in namespaces: "
                            f"{', '.join(namespaces)}"
                        )

        result.add_info(
            f"Analyzed {len(all_identifiers)} unique identifiers, "
            f"{namespace_conflicts} cross-namespace references"
        )

        if duplicates_found == 0:
            result.add_info("No problematic identifier duplicates detected")

    def validate_all(self) -> ValidationResult:
        """
        Run all deduplication validations.

        Returns:
            ValidationResult with all findings
        """
        result = ValidationResult()

        print("\n" + "=" * 60)
        print("TEKNIA DEDUPLICATION VALIDATION")
        print("=" * 60 + "\n")

        # Run hash uniqueness validation
        self.validate_hash_uniqueness(result)

        # Run namespace separation validation
        self.validate_namespace_separation(result)

        result.print_summary()
        return result

    def validate_hash_only(self) -> ValidationResult:
        """
        Run only hash uniqueness validation.

        Returns:
            ValidationResult with findings
        """
        result = ValidationResult()

        print("\n" + "=" * 60)
        print("TEKNIA HASH UNIQUENESS VALIDATION")
        print("=" * 60 + "\n")

        self.validate_hash_uniqueness(result)

        result.print_summary()
        return result

    def validate_namespace_only(self) -> ValidationResult:
        """
        Run only namespace separation validation.

        Returns:
            ValidationResult with findings
        """
        result = ValidationResult()

        print("\n" + "=" * 60)
        print("TEKNIA NAMESPACE SEPARATION VALIDATION")
        print("=" * 60 + "\n")

        self.validate_namespace_separation(result)

        result.print_summary()
        return result


def main() -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='TEKNIA deduplication validator - hash uniqueness and namespace separation',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --check-all
  %(prog)s --check-hash
  %(prog)s --check-namespace
  %(prog)s --repo-root /path/to/repo --verbose

Exit codes:
  0: All validations passed
  1: Validation errors found (duplicates detected)
  2: Script error
        """
    )

    parser.add_argument(
        '--check-all',
        action='store_true',
        help='Run all deduplication validations (hash + namespace)'
    )
    parser.add_argument(
        '--check-hash',
        action='store_true',
        help='Run only hash uniqueness validation'
    )
    parser.add_argument(
        '--check-namespace',
        action='store_true',
        help='Run only namespace separation validation'
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
    parser.add_argument(
        '--strict',
        action='store_true',
        help='Strict mode: flag all duplicates as errors, ignore allowlist'
    )

    args = parser.parse_args()

    # Validate arguments - require exactly one check mode flag
    # Note: --check-all already provides combined functionality, so if multiple
    # flags are specified, --check-all takes priority, then --check-hash, then --check-namespace
    if not any([args.check_all, args.check_hash, args.check_namespace]):
        parser.error('Must specify --check-all, --check-hash, or --check-namespace')

    # Warn if multiple flags are specified (only one will be used)
    check_count = sum([args.check_all, args.check_hash, args.check_namespace])
    if check_count > 1:
        print("Warning: Multiple check flags specified. Using priority order: "
              "--check-all > --check-hash > --check-namespace", file=sys.stderr)

    repo_root = Path(args.repo_root)
    if not repo_root.is_dir():
        print(f"Error: '{args.repo_root}' is not a directory", file=sys.stderr)
        return 2

    try:
        validator = TekniaDedupValidator(
            repo_root, verbose=args.verbose, strict=args.strict
        )

        if args.check_all:
            result = validator.validate_all()
        elif args.check_hash:
            result = validator.validate_hash_only()
        elif args.check_namespace:
            result = validator.validate_namespace_only()
        else:
            result = ValidationResult()

        return 0 if result.passed else 1

    except KeyboardInterrupt:
        print("\nInterrupted by user", file=sys.stderr)
        return 2
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
