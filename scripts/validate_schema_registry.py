#!/usr/bin/env python3
"""
AMPEL360 Space-T Schema Registry Validator
===========================================
Version: 1.0
Date: 2025-12-16
Task: T2-AI from K06 ATA 00 Tasklist

Validates schema registry completeness and version conflicts.
Enforces schema governance policy by ensuring:
- All JSON schema files are registered in the registry
- No duplicate schema IDs exist
- No version conflicts (same schema ID with different content)
- Schema files follow proper naming conventions

Consumes:
- ATA 91 schema registry (schema-registry.csv)
- CM's schema governance policy

Usage:
    python scripts/validate_schema_registry.py --check-all
    python scripts/validate_schema_registry.py --registry <registry_file>
    python scripts/validate_schema_registry.py --schema <schema_file>

Exit codes:
    0: All validations passed
    1: Validation errors found
    2: Script error (file not found, etc.)
"""

import argparse
import csv
import hashlib
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple


@dataclass
class SchemaEntry:
    """Represents a schema entry in the registry."""
    schema_id: str
    version: str
    namespace: str
    owner: str
    status: str
    file_path: str
    description: str = ""
    content_hash: str = ""


@dataclass
class ValidationResult:
    """Container for validation results."""
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    info: List[str] = field(default_factory=list)
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

    def print_summary(self) -> None:
        """Print validation summary."""
        print("\n" + "=" * 60)
        print("SCHEMA REGISTRY VALIDATION SUMMARY")
        print("=" * 60)

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
        if self.passed and not self.warnings:
            print("✅ VALIDATION PASSED - No errors or warnings")
        elif self.passed:
            print("✅ VALIDATION PASSED - Warnings present but no errors")
        else:
            print("❌ VALIDATION FAILED - Errors must be fixed")
        print("=" * 60 + "\n")


class SchemaRegistryValidator:
    """Validates schema registry for completeness and version conflicts."""

    # URN prefix for schema IDs generated from filenames
    SCHEMA_URN_PREFIX = "urn:ampel360:spacet:schema"

    # Required fields for registry entries
    REGISTRY_REQUIRED_FIELDS = ['schema_id', 'version', 'status', 'file_path']

    # Valid status values for schemas
    VALID_SCHEMA_STATUSES = ['active', 'deprecated', 'draft', 'superseded']

    # Pattern for schema files following nomenclature standard v3.0
    # Example: 06_90_SCH_SB90_AMPEL360_SPACET_GEN_dimensional-data-schema_v01.json
    SCHEMA_FILE_PATTERN = re.compile(
        r'^(?P<root>\d{2,3})_'
        r'(?P<bucket>\d{2})_'
        r'SCH_'  # TYPE must be SCH
        r'(?P<subject>(LC(0[1-9]|1[0-4])|SB(1[5-9]|[2-9]\d)))_'
        r'(?P<project>AMPEL360)_'
        r'(?P<program>SPACET)_'
        r'(?P<variant>[A-Z0-9]+(?:-[A-Z0-9]+)*)_'
        r'(?P<desc>[a-z0-9]+(?:-[a-z0-9]+)*)_'
        r'(?P<ver>v\d{2})'
        r'\.json$'
    )

    # Directories to exclude from scanning
    EXCLUDED_DIRS = {
        '.git', '.github', 'node_modules', '__pycache__',
        '.pytest_cache', '.venv', 'venv', 'dist', 'build',
        'templates', 'scripts'
    }

    # Files to exclude from scanning
    EXCLUDED_FILES = {
        'package.json', 'package-lock.json', 'tsconfig.json',
        '.eslintrc.json', '.prettierrc.json'
    }

    def __init__(self, repo_root: Path = Path('.'), verbose: bool = False):
        """
        Initialize the validator.

        Args:
            repo_root: Path to the repository root
            verbose: Enable verbose output
        """
        self.repo_root = repo_root
        self.verbose = verbose
        self.registry: Dict[str, SchemaEntry] = {}
        self.discovered_schemas: Dict[str, List[Path]] = {}

    def discover_schema_files(self) -> Dict[str, List[Path]]:
        """
        Discover all JSON schema files in the repository.

        Returns:
            Dictionary mapping schema IDs to list of file paths (to detect duplicates)
        """
        schemas: Dict[str, List[Path]] = {}

        for path in self.repo_root.rglob('*.json'):
            # Skip excluded directories
            if self._is_excluded_path(path):
                continue

            # Skip excluded files
            if path.name in self.EXCLUDED_FILES:
                continue

            # Try to identify as a JSON schema file
            schema_info = self._extract_schema_info(path)
            if schema_info:
                schema_id, _ = schema_info
                if schema_id:
                    if schema_id not in schemas:
                        schemas[schema_id] = []
                    schemas[schema_id].append(path)
                    if self.verbose:
                        print(f"  Found schema: {schema_id} -> {path}")

        return schemas

    def _is_excluded_path(self, path: Path) -> bool:
        """Check if path should be excluded from scanning."""
        for parent in path.parents:
            if parent.name in self.EXCLUDED_DIRS:
                return True
        return False

    def _extract_schema_info(self, path: Path) -> Optional[Tuple[str, str]]:
        """
        Extract schema ID and version from a JSON schema file.

        Args:
            path: Path to the JSON file

        Returns:
            Tuple of (schema_id, version) if valid schema, None otherwise
        """
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
                data = json.loads(content)

            # Check if this is a JSON Schema file
            if not isinstance(data, dict):
                return None

            # Look for $schema or $id fields (JSON Schema indicators)
            if '$schema' in data or '$id' in data:
                schema_id = data.get('$id', '')
                version = data.get('version', '1.0')

                # If no $id, try to derive from filename
                if not schema_id:
                    match = self.SCHEMA_FILE_PATTERN.match(path.name)
                    if match:
                        # Create schema ID from filename
                        desc = match.group('desc')
                        ver = match.group('ver')
                        schema_id = f"{self.SCHEMA_URN_PREFIX}:{desc}:{ver}"

                return (schema_id, str(version)) if schema_id else None

            return None

        except (json.JSONDecodeError, OSError, UnicodeDecodeError):
            return None

    def _compute_content_hash(self, path: Path) -> str:
        """
        Compute SHA-256 hash of file content.

        Args:
            path: Path to the file

        Returns:
            SHA-256 hex digest
        """
        try:
            with open(path, 'rb') as f:
                return hashlib.sha256(f.read()).hexdigest()
        except OSError:
            return ""

    def load_registry(self, registry_path: Path) -> bool:
        """
        Load schema registry from CSV file.

        Args:
            registry_path: Path to the registry CSV file

        Returns:
            True if loaded successfully, False otherwise
        """
        if not registry_path.exists():
            return False

        try:
            with open(registry_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)

                for row in reader:
                    entry = SchemaEntry(
                        schema_id=row.get('schema_id', ''),
                        version=row.get('version', ''),
                        namespace=row.get('namespace', ''),
                        owner=row.get('owner', ''),
                        status=row.get('status', ''),
                        file_path=row.get('file_path', ''),
                        description=row.get('description', ''),
                        content_hash=row.get('content_hash', '')
                    )
                    if entry.schema_id:
                        self.registry[entry.schema_id] = entry

            return True

        except (OSError, csv.Error, UnicodeDecodeError):
            return False

    def validate_completeness(self, result: ValidationResult) -> None:
        """
        Validate that all discovered schemas are registered.

        Args:
            result: ValidationResult to update
        """
        print("🔍 Checking schema registry completeness...")

        unregistered = []
        for schema_id, paths in self.discovered_schemas.items():
            if schema_id not in self.registry:
                unregistered.append((schema_id, paths[0]))  # Use first path for error message

        if unregistered:
            for schema_id, path in unregistered:
                result.add_error(
                    f"Unregistered schema: {schema_id} (file: {path})"
                )
        else:
            total_files = sum(len(paths) for paths in self.discovered_schemas.values())
            result.add_info(
                f"All {total_files} discovered schema files are registered"
            )

    def validate_duplicate_ids(self, result: ValidationResult) -> None:
        """
        Validate that there are no duplicate schema IDs.

        Args:
            result: ValidationResult to update
        """
        print("🔍 Checking for duplicate schema IDs...")

        # discovered_schemas already maps schema_id to List[Path]
        duplicates = {
            sid: paths for sid, paths in self.discovered_schemas.items()
            if len(paths) > 1
        }

        if duplicates:
            for schema_id, paths in duplicates.items():
                result.add_error(
                    f"Duplicate schema ID '{schema_id}' found in: "
                    f"{', '.join(str(p) for p in paths)}"
                )
        else:
            result.add_info("No duplicate schema IDs found")

    def validate_version_conflicts(self, result: ValidationResult) -> None:
        """
        Validate that there are no version conflicts.

        A version conflict occurs when:
        - Same schema ID has different content but same version
        - Same schema has breaking changes without version bump

        Args:
            result: ValidationResult to update
        """
        print("🔍 Checking for version conflicts...")

        # Group schemas by base ID (without version)
        base_id_to_versions: Dict[str, List[Tuple[str, Path, str]]] = {}

        for schema_id, paths in self.discovered_schemas.items():
            # Extract base ID and version
            # Pattern: ends with -vNN.json or :vNN or -vNN
            base_id = re.sub(r'[-:]v\d+(\.json)?$', '', schema_id)

            for path in paths:
                # Get version from schema or filename
                version = "unknown"
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        version = str(data.get('version', 'unknown'))
                except (json.JSONDecodeError, OSError):
                    # Silently continue if unable to read version from file
                    pass

                content_hash = self._compute_content_hash(path)

                if base_id not in base_id_to_versions:
                    base_id_to_versions[base_id] = []
                base_id_to_versions[base_id].append((version, path, content_hash))

        # Check for conflicts
        conflicts = []
        for base_id, versions in base_id_to_versions.items():
            if len(versions) > 1:
                # Check if same version has different content
                version_hashes: Dict[str, Set[str]] = {}
                for version, path, content_hash in versions:
                    if version not in version_hashes:
                        version_hashes[version] = set()
                    version_hashes[version].add(content_hash)

                for version, hashes in version_hashes.items():
                    if len(hashes) > 1:
                        conflicts.append(
                            f"Version conflict: {base_id} version {version} "
                            f"has {len(hashes)} different contents"
                        )

        if conflicts:
            for conflict in conflicts:
                result.add_error(conflict)
        else:
            result.add_info("No version conflicts detected")

    def validate_registry_entries(self, result: ValidationResult) -> None:
        """
        Validate registry entries for completeness and correctness.

        Args:
            result: ValidationResult to update
        """
        print("🔍 Validating registry entries...")

        for schema_id, entry in self.registry.items():
            # Check required fields
            for field_name in self.REGISTRY_REQUIRED_FIELDS:
                value = getattr(entry, field_name, '')
                if not value:
                    result.add_warning(
                        f"Registry entry '{schema_id}' missing field: {field_name}"
                    )

            # Check if referenced file exists
            if entry.file_path:
                file_path = self.repo_root / entry.file_path
                if not file_path.exists():
                    result.add_error(
                        f"Registry entry '{schema_id}' references "
                        f"non-existent file: {entry.file_path}"
                    )

            # Check status validity
            if entry.status and entry.status.lower() not in self.VALID_SCHEMA_STATUSES:
                result.add_warning(
                    f"Registry entry '{schema_id}' has invalid status: "
                    f"{entry.status} (expected: {self.VALID_SCHEMA_STATUSES})"
                )

        result.add_info(f"Validated {len(self.registry)} registry entries")

    def validate_schema_syntax(self, path: Path, result: ValidationResult) -> None:
        """
        Validate JSON schema syntax and structure.

        Args:
            path: Path to the schema file
            result: ValidationResult to update
        """
        try:
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # Check for required JSON Schema fields
            if '$schema' not in data:
                result.add_warning(
                    f"Schema {path} missing '$schema' field"
                )

            if '$id' not in data:
                result.add_warning(
                    f"Schema {path} missing '$id' field"
                )

            if 'title' not in data and 'description' not in data:
                result.add_warning(
                    f"Schema {path} missing 'title' or 'description'"
                )

        except json.JSONDecodeError as e:
            result.add_error(f"Invalid JSON in {path}: {e}")
        except OSError as e:
            result.add_error(f"Cannot read {path}: {e}")

    def validate_all(self, registry_path: Optional[Path] = None) -> ValidationResult:
        """
        Run all validations.

        Args:
            registry_path: Optional path to registry file

        Returns:
            ValidationResult with all findings
        """
        result = ValidationResult()

        print("\n" + "=" * 60)
        print("SCHEMA REGISTRY VALIDATION")
        print("=" * 60 + "\n")

        # Discover schemas
        print("🔍 Discovering schema files...")
        self.discovered_schemas = self.discover_schema_files()
        total_files = sum(len(paths) for paths in self.discovered_schemas.values())
        result.add_info(
            f"Discovered {total_files} schema files ({len(self.discovered_schemas)} unique IDs)"
        )

        # Load registry if provided
        if registry_path:
            print(f"📄 Loading registry from: {registry_path}")
            if self.load_registry(registry_path):
                result.add_info(
                    f"Loaded {len(self.registry)} entries from registry"
                )
                # Run registry-based validations
                self.validate_completeness(result)
                self.validate_registry_entries(result)
            else:
                result.add_warning(
                    f"Could not load registry from: {registry_path}"
                )

        # Run schema-based validations (no registry needed)
        self.validate_duplicate_ids(result)
        self.validate_version_conflicts(result)

        # Validate individual schema files
        print("🔍 Validating schema file syntax...")
        for schema_id, paths in self.discovered_schemas.items():
            for path in paths:
                self.validate_schema_syntax(path, result)

        result.print_summary()
        return result


def find_registry_files(repo_root: Path) -> List[Path]:
    """
    Find schema registry files in the repository.

    Args:
        repo_root: Path to repository root

    Returns:
        List of paths to registry files
    """
    registries = []

    # Common registry locations and patterns
    patterns = [
        '**/schema-registry*.csv',
        '**/91_*_TAB_*_schema-registry_*.csv',
        '**/schema_registry*.csv'
    ]

    for pattern in patterns:
        registries.extend(repo_root.glob(pattern))

    return list(set(registries))


def main() -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Validate schema registry completeness and version conflicts',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --check-all
  %(prog)s --registry path/to/schema-registry.csv
  %(prog)s --schema path/to/schema.json

Exit codes:
  0: All validations passed
  1: Validation errors found
  2: Script error
        """
    )

    parser.add_argument(
        '--check-all',
        action='store_true',
        help='Validate all schemas in the repository'
    )
    parser.add_argument(
        '--registry',
        metavar='FILE',
        help='Path to schema registry CSV file'
    )
    parser.add_argument(
        '--schema',
        metavar='FILE',
        help='Validate a single schema file'
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
    if not any([args.check_all, args.registry, args.schema]):
        parser.error('Must specify --check-all, --registry, or --schema')

    repo_root = Path(args.repo_root)
    if not repo_root.is_dir():
        print(f"Error: '{args.repo_root}' is not a directory", file=sys.stderr)
        return 2

    try:
        validator = SchemaRegistryValidator(repo_root, verbose=args.verbose)

        if args.schema:
            # Validate single schema file
            schema_path = Path(args.schema)
            if not schema_path.exists():
                print(f"Error: Schema file not found: {args.schema}",
                      file=sys.stderr)
                return 2

            result = ValidationResult()
            validator.validate_schema_syntax(schema_path, result)
            result.print_summary()
            return 0 if result.passed else 1

        # Find registry files
        registry_path = None
        if args.registry:
            registry_path = Path(args.registry)
            if not registry_path.exists():
                print(f"Warning: Registry file not found: {args.registry}",
                      file=sys.stderr)
                registry_path = None
        elif args.check_all:
            # Try to auto-discover registry
            registries = find_registry_files(repo_root)
            if registries:
                registry_path = registries[0]
                print(f"📄 Auto-discovered registry: {registry_path}")
            else:
                # Output marker for CI workflow to detect missing registry
                print("⚠️  REGISTRY_MISSING: No ATA 91 schema registry found in repository")

        # Run validation
        result = validator.validate_all(registry_path)
        return 0 if result.passed else 1

    except KeyboardInterrupt:
        print("\nInterrupted by user", file=sys.stderr)
        return 2
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
