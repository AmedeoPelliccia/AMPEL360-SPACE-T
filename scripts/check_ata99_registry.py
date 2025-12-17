#!/usr/bin/env python3
"""
AMPEL360 Space-T GATE-004: Namespace Deduplication Check
========================================================
Version: 1.0
Date: 2025-12-17
Standard: Nomenclature v6.0 R1.0

Implements GATE-004 (Namespace Deduplication Check) to prevent
duplicate namespace IDs in the ATA 99 registry.

This addresses Known Issue KI-PR3-002.

Usage:
    python scripts/check_ata99_registry.py --check
    python scripts/check_ata99_registry.py --register <namespace_id> <type> <aor> <path>
    python scripts/check_ata99_registry.py --deduplicate

Exit codes:
    0: No duplicates found or operation successful
    1: Duplicates found or validation errors
    2: Script error
"""

import argparse
import json
import re
import sys
import hashlib
from pathlib import Path
from typing import List, Dict, Any, Optional, Set, Tuple
from dataclasses import dataclass

# Import PLC database module
try:
    from plc_db import PLCDatabase
except ImportError:
    sys.path.insert(0, str(Path(__file__).parent))
    from plc_db import PLCDatabase


@dataclass
class NamespaceEntry:
    """Represents a namespace registry entry."""
    namespace_id: str
    namespace_type: str
    scope: Optional[str]
    owner_aor: str
    artifact_path: str
    artifact_sha256: Optional[str]
    description: Optional[str]


class ATA99RegistryChecker:
    """
    Checker for ATA 99 namespace registry deduplication.
    
    Validates that namespace IDs are unique across the registry
    and identifies conflicts.
    """
    
    # Namespace ID patterns for validation
    NAMESPACE_PATTERNS = {
        'ata99_namespace': r'^NS-ATA99-[A-Z0-9-]+$',
        'schema_namespace': r'^NS-SCH-[A-Z0-9-]+$',
        'trace_namespace': r'^NS-TR-[A-Z0-9-]+$',
        'identifier_namespace': r'^NS-ID-[A-Z0-9-]+$',
    }
    
    def __init__(self, db_path: str = "plc_ontology.db"):
        """Initialize with database connection."""
        self.db = PLCDatabase(db_path)
        self.conflicts: List[Dict[str, Any]] = []
    
    def scan_repository(self, directory: Path = Path('.')) -> List[NamespaceEntry]:
        """
        Scan repository for namespace declarations in JSON/YAML files.
        
        Returns:
            List of discovered namespace entries
        """
        print("Scanning repository for namespace declarations...")
        
        entries = []
        
        # Find JSON and YAML files that might contain namespace declarations
        json_files = list(directory.rglob('*.json'))
        yaml_files = list(directory.rglob('*.yaml')) + list(directory.rglob('*.yml'))
        
        # Exclude certain directories
        excluded_dirs = {'.git', 'node_modules', '__pycache__', '.venv', 'venv'}
        manifest_files = [
            f for f in (json_files + yaml_files)
            if not any(exc in f.parts for exc in excluded_dirs)
        ]
        
        print(f"Found {len(manifest_files)} potential manifest files")
        
        for manifest_file in manifest_files:
            try:
                content = manifest_file.read_text(encoding='utf-8', errors='ignore')
                
                # Look for namespace ID patterns in content
                for ns_type, pattern in self.NAMESPACE_PATTERNS.items():
                    matches = re.finditer(pattern, content)
                    for match in matches:
                        namespace_id = match.group(0)
                        
                        # Try to extract additional context from JSON/YAML
                        # This is a simple implementation; could be enhanced
                        entries.append(NamespaceEntry(
                            namespace_id=namespace_id,
                            namespace_type=ns_type,
                            scope='ATA99',
                            owner_aor='DATA',  # Default, should be extracted from context
                            artifact_path=str(manifest_file.relative_to(directory)),
                            artifact_sha256=self._compute_file_hash(manifest_file),
                            description=None
                        ))
                
            except Exception as e:
                print(f"  Warning: Could not process {manifest_file}: {e}")
        
        print(f"Discovered {len(entries)} namespace declarations")
        return entries
    
    def register_namespaces(self, entries: List[NamespaceEntry]) -> int:
        """
        Register namespace entries in the database.
        
        Returns:
            Number of entries registered
        """
        print("Registering namespaces in database...")
        count = 0
        
        for entry in entries:
            try:
                self.db.register_namespace(
                    namespace_id=entry.namespace_id,
                    namespace_type=entry.namespace_type,
                    owner_aor=entry.owner_aor,
                    artifact_path=entry.artifact_path,
                    scope=entry.scope,
                    artifact_sha256=entry.artifact_sha256,
                    description=entry.description
                )
                count += 1
            except Exception as e:
                print(f"  Warning: Failed to register {entry.namespace_id}: {e}")
        
        print(f"Registered {count} namespace entries")
        return count
    
    def check_duplicates(self) -> List[Dict[str, Any]]:
        """
        Check for duplicate namespace IDs in the registry.
        
        Returns:
            List of conflicts
        """
        print("Checking for duplicate namespace IDs...")
        
        duplicates = self.db.check_namespace_duplicates()
        
        if duplicates:
            print(f"Found {len(duplicates)} duplicate namespace ID(s)")
            
            # Record conflicts in database
            for dup in duplicates:
                paths = dup['paths'].split(', ')
                if len(paths) >= 2:
                    conflict_id = self.db.record_namespace_conflict(
                        namespace_id=dup['namespace_id'],
                        artifact_path_1=paths[0],
                        artifact_path_2=paths[1],
                        conflict_type='DUPLICATE_ID'
                    )
                    self.conflicts.append({
                        'conflict_id': conflict_id,
                        'namespace_id': dup['namespace_id'],
                        'count': dup['count'],
                        'paths': paths
                    })
        else:
            print("✓ No duplicate namespace IDs found")
        
        return self.conflicts
    
    def validate_namespace_id_format(self, namespace_id: str) -> Tuple[bool, Optional[str]]:
        """
        Validate namespace ID against known patterns.
        
        Returns:
            (is_valid, error_message)
        """
        for ns_type, pattern in self.NAMESPACE_PATTERNS.items():
            if re.match(pattern, namespace_id):
                return (True, None)
        
        return (False, f"Namespace ID '{namespace_id}' does not match any known pattern")
    
    def _compute_file_hash(self, file_path: Path) -> str:
        """Compute SHA-256 hash of file."""
        sha256_hash = hashlib.sha256()
        try:
            with open(file_path, "rb") as f:
                for byte_block in iter(lambda: f.read(4096), b""):
                    sha256_hash.update(byte_block)
            return sha256_hash.hexdigest()
        except Exception:
            return ""
    
    def generate_report(self) -> Dict[str, Any]:
        """Generate deduplication report."""
        duplicates = self.db.check_namespace_duplicates()
        
        report = {
            'total_duplicates': len(duplicates),
            'conflicts': self.conflicts,
            'duplicates_detail': duplicates
        }
        
        return report
    
    def print_conflicts(self) -> None:
        """Print conflicts in a readable format."""
        if not self.conflicts:
            print("\n✅ No namespace conflicts detected")
            return
        
        print(f"\n❌ Found {len(self.conflicts)} namespace conflict(s):\n")
        
        for conflict in self.conflicts:
            print(f"Namespace ID: {conflict['namespace_id']}")
            print(f"  Occurrences: {conflict['count']}")
            print(f"  Conflicting files:")
            for path in conflict['paths']:
                print(f"    - {path}")
            print()


def run_gate_004(db_path: str = "plc_ontology.db", directory: Path = Path('.')) -> Tuple[bool, Dict[str, Any]]:
    """
    Execute GATE-004 check.
    
    Returns:
        (passed, report)
    """
    import time
    start_time = time.time()
    
    checker = ATA99RegistryChecker(db_path)
    
    # Scan and register namespaces
    entries = checker.scan_repository(directory)
    if entries:
        checker.register_namespaces(entries)
    
    # Check for duplicates
    conflicts = checker.check_duplicates()
    
    # Generate report
    report = checker.generate_report()
    
    execution_time_ms = int((time.time() - start_time) * 1000)
    
    # Record gate run in database
    passed = len(conflicts) == 0
    run_id = checker.db.record_gate_run(
        gate_code='GATE-004',
        passed=passed,
        error_count=len(conflicts),
        warning_count=0,
        execution_time_ms=execution_time_ms,
        metadata=report
    )
    
    # Record findings
    for conflict in conflicts:
        checker.db.record_gate_finding(
            run_id=run_id,
            gate_code='GATE-004',
            severity='ERROR',
            message=f"Duplicate namespace ID: {conflict['namespace_id']}",
            finding_code='NAMESPACE_DUPLICATE',
            details=conflict
        )
    
    return (passed, report)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='GATE-004: Namespace Deduplication Check (ATA 99 Registry)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Check for duplicates
  %(prog)s --check

  # Register a namespace manually
  %(prog)s --register NS-ATA99-EXAMPLE schema DATA path/to/file.json

  # Run deduplication check with reporting
  %(prog)s --deduplicate
        """
    )
    
    parser.add_argument(
        '--check',
        action='store_true',
        help='Check for duplicate namespace IDs'
    )
    parser.add_argument(
        '--register',
        nargs=4,
        metavar=('NAMESPACE_ID', 'TYPE', 'AOR', 'PATH'),
        help='Register a namespace entry'
    )
    parser.add_argument(
        '--deduplicate',
        action='store_true',
        help='Run full deduplication check with report'
    )
    parser.add_argument(
        '--db-path',
        default='plc_ontology.db',
        help='Path to PLC database (default: plc_ontology.db)'
    )
    parser.add_argument(
        '--directory',
        default='.',
        help='Repository root directory (default: current directory)'
    )
    parser.add_argument(
        '--json',
        action='store_true',
        help='Output report in JSON format'
    )
    
    args = parser.parse_args()
    
    if not any([args.check, args.register, args.deduplicate]):
        parser.error('Must specify one of: --check, --register, or --deduplicate')
    
    directory = Path(args.directory)
    
    try:
        checker = ATA99RegistryChecker(args.db_path)
        
        # Initialize database if needed
        try:
            checker.db.initialize_database()
        except Exception:
            pass  # Already initialized
        
        # Register namespace
        if args.register:
            namespace_id, ns_type, aor, path = args.register
            
            # Validate format
            valid, error = checker.validate_namespace_id_format(namespace_id)
            if not valid:
                print(f"❌ {error}", file=sys.stderr)
                return 1
            
            # Compute hash if file exists
            file_path = directory / path
            sha256 = checker._compute_file_hash(file_path) if file_path.exists() else None
            
            checker.db.register_namespace(
                namespace_id=namespace_id,
                namespace_type=ns_type,
                owner_aor=aor,
                artifact_path=path,
                artifact_sha256=sha256
            )
            
            print(f"✓ Registered namespace: {namespace_id}")
            return 0
        
        # Check for duplicates
        if args.check or args.deduplicate:
            passed, report = run_gate_004(args.db_path, directory)
            
            if args.json:
                print(json.dumps(report, indent=2))
            else:
                checker.print_conflicts()
                
                print(f"\n{'═'*70}")
                print(f"GATE-004: Namespace Deduplication Check")
                print(f"{'═'*70}")
                print(f"Result: {'✅ PASSED' if passed else '❌ FAILED'}")
                print(f"Duplicates found: {report['total_duplicates']}")
                print(f"{'═'*70}")
            
            return 0 if passed else 1
        
    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return 2


if __name__ == '__main__':
    sys.exit(main())
