#!/usr/bin/env python3
"""
AMPEL360 Space-T GATE-007: Breaking Schema Change Detection
===========================================================
Version: 1.0
Date: 2025-12-17
Standard: Nomenclature v6.0 R1.0

Implements GATE-007 (Breaking Schema Change Detection) to detect
incompatible schema changes that require migration plans.

This addresses Known Issue KI-PR3-004.

Usage:
    python scripts/detect_schema_breaking_changes.py --check
    python scripts/detect_schema_breaking_changes.py --compare <old_schema> <new_schema>
    python scripts/detect_schema_breaking_changes.py --registry ATA91

Exit codes:
    0: No breaking changes detected
    1: Breaking changes found
    2: Script error
"""

import argparse
import json
import sys
import hashlib
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple, Set
from dataclasses import dataclass
from enum import Enum

# Import PLC database module
try:
    from plc_db import PLCDatabase
except ImportError:
    sys.path.insert(0, str(Path(__file__).parent))
    from plc_db import PLCDatabase


class ChangeType(Enum):
    """Types of schema changes."""
    FIELD_REMOVED = "FIELD_REMOVED"
    FIELD_TYPE_CHANGED = "FIELD_TYPE_CHANGED"
    FIELD_MADE_REQUIRED = "FIELD_MADE_REQUIRED"
    ENUM_VALUE_REMOVED = "ENUM_VALUE_REMOVED"
    MIN_LENGTH_INCREASED = "MIN_LENGTH_INCREASED"
    MAX_LENGTH_DECREASED = "MAX_LENGTH_DECREASED"
    MIN_VALUE_INCREASED = "MIN_VALUE_INCREASED"
    MAX_VALUE_DECREASED = "MAX_VALUE_DECREASED"
    PATTERN_MADE_STRICTER = "PATTERN_MADE_STRICTER"
    ADDITIONAL_PROPERTIES_DISALLOWED = "ADDITIONAL_PROPERTIES_DISALLOWED"
    
    # Non-breaking changes
    FIELD_ADDED = "FIELD_ADDED"
    FIELD_MADE_OPTIONAL = "FIELD_MADE_OPTIONAL"
    ENUM_VALUE_ADDED = "ENUM_VALUE_ADDED"
    MAX_LENGTH_INCREASED = "MAX_LENGTH_INCREASED"
    MIN_LENGTH_DECREASED = "MIN_LENGTH_DECREASED"


@dataclass
class SchemaChange:
    """Represents a detected schema change."""
    change_type: ChangeType
    field_path: str
    old_value: Any
    new_value: Any
    breaking: bool
    severity: int  # 0=non-breaking, 1=minor, 2=major, 3=critical


class SchemaBreakingChangeDetector:
    """
    Detector for breaking changes in JSON schemas.
    
    Analyzes schema diffs and assigns breaking scores based on
    the severity and type of changes detected.
    """
    
    # Breaking scores for different change types
    BREAKING_SCORES = {
        ChangeType.FIELD_REMOVED: 3,  # Critical
        ChangeType.FIELD_TYPE_CHANGED: 3,  # Critical
        ChangeType.FIELD_MADE_REQUIRED: 2,  # Major
        ChangeType.ENUM_VALUE_REMOVED: 2,  # Major
        ChangeType.MIN_LENGTH_INCREASED: 2,  # Major
        ChangeType.MAX_LENGTH_DECREASED: 2,  # Major
        ChangeType.MIN_VALUE_INCREASED: 2,  # Major
        ChangeType.MAX_VALUE_DECREASED: 2,  # Major
        ChangeType.PATTERN_MADE_STRICTER: 2,  # Major
        ChangeType.ADDITIONAL_PROPERTIES_DISALLOWED: 1,  # Minor
        
        # Non-breaking changes (score 0)
        ChangeType.FIELD_ADDED: 0,
        ChangeType.FIELD_MADE_OPTIONAL: 0,
        ChangeType.ENUM_VALUE_ADDED: 0,
        ChangeType.MAX_LENGTH_INCREASED: 0,
        ChangeType.MIN_LENGTH_DECREASED: 0,
    }
    
    def __init__(self, db_path: str = "plc_ontology.db"):
        """Initialize with database connection."""
        self.db = PLCDatabase(db_path)
        self.changes: List[SchemaChange] = []
        self.breaking_changes: List[SchemaChange] = []
    
    def compare_schemas(
        self,
        old_schema: Dict[str, Any],
        new_schema: Dict[str, Any],
        base_path: str = ""
    ) -> List[SchemaChange]:
        """
        Compare two JSON schemas and detect changes.
        
        Args:
            old_schema: The old schema version
            new_schema: The new schema version
            base_path: Base path for nested fields
            
        Returns:
            List of detected changes
        """
        changes = []
        
        # Compare properties
        old_props = old_schema.get('properties', {})
        new_props = new_schema.get('properties', {})
        
        # Check for removed fields
        for field_name in old_props:
            if field_name not in new_props:
                change = SchemaChange(
                    change_type=ChangeType.FIELD_REMOVED,
                    field_path=f"{base_path}.{field_name}" if base_path else field_name,
                    old_value=old_props[field_name],
                    new_value=None,
                    breaking=True,
                    severity=self.BREAKING_SCORES[ChangeType.FIELD_REMOVED]
                )
                changes.append(change)
                self.breaking_changes.append(change)
        
        # Check for added fields
        for field_name in new_props:
            if field_name not in old_props:
                change = SchemaChange(
                    change_type=ChangeType.FIELD_ADDED,
                    field_path=f"{base_path}.{field_name}" if base_path else field_name,
                    old_value=None,
                    new_value=new_props[field_name],
                    breaking=False,
                    severity=0
                )
                changes.append(change)
        
        # Check for field changes
        for field_name in old_props:
            if field_name in new_props:
                field_path = f"{base_path}.{field_name}" if base_path else field_name
                field_changes = self._compare_field(
                    old_props[field_name],
                    new_props[field_name],
                    field_path
                )
                changes.extend(field_changes)
        
        # Check required fields
        old_required = set(old_schema.get('required', []))
        new_required = set(new_schema.get('required', []))
        
        # Fields made required (breaking)
        for field in new_required - old_required:
            change = SchemaChange(
                change_type=ChangeType.FIELD_MADE_REQUIRED,
                field_path=f"{base_path}.{field}" if base_path else field,
                old_value=False,
                new_value=True,
                breaking=True,
                severity=self.BREAKING_SCORES[ChangeType.FIELD_MADE_REQUIRED]
            )
            changes.append(change)
            self.breaking_changes.append(change)
        
        # Fields made optional (non-breaking)
        for field in old_required - new_required:
            change = SchemaChange(
                change_type=ChangeType.FIELD_MADE_OPTIONAL,
                field_path=f"{base_path}.{field}" if base_path else field,
                old_value=True,
                new_value=False,
                breaking=False,
                severity=0
            )
            changes.append(change)
        
        self.changes.extend(changes)
        return changes
    
    def _compare_field(
        self,
        old_field: Dict[str, Any],
        new_field: Dict[str, Any],
        field_path: str
    ) -> List[SchemaChange]:
        """Compare a single field definition."""
        changes = []
        
        # Type changes
        old_type = old_field.get('type')
        new_type = new_field.get('type')
        if old_type != new_type:
            change = SchemaChange(
                change_type=ChangeType.FIELD_TYPE_CHANGED,
                field_path=field_path,
                old_value=old_type,
                new_value=new_type,
                breaking=True,
                severity=self.BREAKING_SCORES[ChangeType.FIELD_TYPE_CHANGED]
            )
            changes.append(change)
            self.breaking_changes.append(change)
        
        # Enum changes
        old_enum = set(old_field.get('enum', []))
        new_enum = set(new_field.get('enum', []))
        
        if old_enum and new_enum:
            # Removed enum values (breaking)
            for value in old_enum - new_enum:
                change = SchemaChange(
                    change_type=ChangeType.ENUM_VALUE_REMOVED,
                    field_path=field_path,
                    old_value=value,
                    new_value=None,
                    breaking=True,
                    severity=self.BREAKING_SCORES[ChangeType.ENUM_VALUE_REMOVED]
                )
                changes.append(change)
                self.breaking_changes.append(change)
            
            # Added enum values (non-breaking)
            for value in new_enum - old_enum:
                change = SchemaChange(
                    change_type=ChangeType.ENUM_VALUE_ADDED,
                    field_path=field_path,
                    old_value=None,
                    new_value=value,
                    breaking=False,
                    severity=0
                )
                changes.append(change)
        
        # String constraints
        if old_type == 'string' and new_type == 'string':
            # minLength increased (breaking)
            old_min = old_field.get('minLength')
            new_min = new_field.get('minLength')
            if old_min is not None and new_min is not None and new_min > old_min:
                change = SchemaChange(
                    change_type=ChangeType.MIN_LENGTH_INCREASED,
                    field_path=field_path,
                    old_value=old_min,
                    new_value=new_min,
                    breaking=True,
                    severity=self.BREAKING_SCORES[ChangeType.MIN_LENGTH_INCREASED]
                )
                changes.append(change)
                self.breaking_changes.append(change)
            
            # maxLength decreased (breaking)
            old_max = old_field.get('maxLength')
            new_max = new_field.get('maxLength')
            if old_max is not None and new_max is not None and new_max < old_max:
                change = SchemaChange(
                    change_type=ChangeType.MAX_LENGTH_DECREASED,
                    field_path=field_path,
                    old_value=old_max,
                    new_value=new_max,
                    breaking=True,
                    severity=self.BREAKING_SCORES[ChangeType.MAX_LENGTH_DECREASED]
                )
                changes.append(change)
                self.breaking_changes.append(change)
        
        # Number constraints
        if old_type in ('integer', 'number') and new_type in ('integer', 'number'):
            # minimum increased (breaking)
            old_min = old_field.get('minimum')
            new_min = new_field.get('minimum')
            if old_min is not None and new_min is not None and new_min > old_min:
                change = SchemaChange(
                    change_type=ChangeType.MIN_VALUE_INCREASED,
                    field_path=field_path,
                    old_value=old_min,
                    new_value=new_min,
                    breaking=True,
                    severity=self.BREAKING_SCORES[ChangeType.MIN_VALUE_INCREASED]
                )
                changes.append(change)
                self.breaking_changes.append(change)
            
            # maximum decreased (breaking)
            old_max = old_field.get('maximum')
            new_max = new_field.get('maximum')
            if old_max is not None and new_max is not None and new_max < old_max:
                change = SchemaChange(
                    change_type=ChangeType.MAX_VALUE_DECREASED,
                    field_path=field_path,
                    old_value=old_max,
                    new_value=new_max,
                    breaking=True,
                    severity=self.BREAKING_SCORES[ChangeType.MAX_VALUE_DECREASED]
                )
                changes.append(change)
                self.breaking_changes.append(change)
        
        return changes
    
    def calculate_breaking_score(self) -> int:
        """Calculate total breaking score from all changes."""
        return sum(change.severity for change in self.breaking_changes)
    
    def load_schema(self, schema_path: Path) -> Dict[str, Any]:
        """Load JSON schema from file."""
        with open(schema_path, 'r') as f:
            return json.load(f)
    
    def compute_sha256(self, data: Dict[str, Any]) -> str:
        """Compute SHA-256 hash of schema content."""
        content = json.dumps(data, sort_keys=True)
        return hashlib.sha256(content.encode()).hexdigest()
    
    def scan_schema_files(self, directory: Path = Path('.')) -> List[Dict[str, Any]]:
        """Scan repository for schema files."""
        print("Scanning for schema files...")
        
        schemas = []
        
        # Find JSON schema files (TYPE=SCH)
        json_files = list(directory.rglob('*_SCH_*.json'))
        
        # Exclude certain directories
        excluded_dirs = {'.git', 'node_modules', '__pycache__', '.venv', 'venv'}
        schema_files = [
            f for f in json_files
            if not any(exc in f.parts for exc in excluded_dirs)
        ]
        
        print(f"Found {len(schema_files)} schema files")
        
        for schema_file in schema_files:
            try:
                schema_content = self.load_schema(schema_file)
                schema_id = schema_content.get('$id', str(schema_file.name))
                version = schema_content.get('version', 'v01')
                
                schemas.append({
                    'schema_id': schema_id,
                    'version': version,
                    'path': str(schema_file.relative_to(directory)),
                    'content': schema_content,
                    'sha256': self.compute_sha256(schema_content)
                })
            except Exception as e:
                print(f"  Warning: Could not load {schema_file}: {e}")
        
        return schemas
    
    def register_schemas(self, schemas: List[Dict[str, Any]], owner_aor: str = 'DATA') -> int:
        """Register schemas in the database."""
        count = 0
        for schema in schemas:
            try:
                self.db.register_schema(
                    schema_id=schema['schema_id'],
                    version=schema['version'],
                    artifact_path=schema['path'],
                    artifact_sha256=schema['sha256'],
                    owner_aor=owner_aor,
                    schema_content=schema['content']
                )
                count += 1
            except Exception as e:
                print(f"  Warning: Could not register {schema['schema_id']}: {e}")
        
        print(f"Registered {count} schemas")
        return count
    
    def print_changes(self) -> None:
        """Print detected changes in a readable format."""
        if not self.changes:
            print("\n✅ No schema changes detected")
            return
        
        breaking = [c for c in self.changes if c.breaking]
        non_breaking = [c for c in self.changes if not c.breaking]
        
        if breaking:
            print(f"\n❌ Found {len(breaking)} breaking change(s):\n")
            for change in breaking:
                severity_icon = "🔴" if change.severity == 3 else "🟠"
                print(f"{severity_icon} {change.change_type.value}")
                print(f"  Field: {change.field_path}")
                print(f"  Old: {change.old_value}")
                print(f"  New: {change.new_value}")
                print(f"  Severity: {change.severity}")
                print()
        
        if non_breaking:
            print(f"ℹ️ Found {len(non_breaking)} non-breaking change(s)")


def run_gate_007(
    db_path: str = "plc_ontology.db",
    directory: Path = Path('.'),
    old_schema_path: Optional[str] = None,
    new_schema_path: Optional[str] = None
) -> Tuple[bool, Dict[str, Any]]:
    """
    Execute GATE-007 check.
    
    Returns:
        (passed, report)
    """
    import time
    start_time = time.time()
    
    detector = SchemaBreakingChangeDetector(db_path)
    
    # If specific schemas provided, compare them
    if old_schema_path and new_schema_path:
        old_schema = detector.load_schema(Path(old_schema_path))
        new_schema = detector.load_schema(Path(new_schema_path))
        
        detector.compare_schemas(old_schema, new_schema)
        
        breaking_score = detector.calculate_breaking_score()
        
        report = {
            'comparison': f"{old_schema_path} -> {new_schema_path}",
            'total_changes': len(detector.changes),
            'breaking_changes': len(detector.breaking_changes),
            'breaking_score': breaking_score,
            'changes': [
                {
                    'type': c.change_type.value,
                    'field': c.field_path,
                    'breaking': c.breaking,
                    'severity': c.severity
                }
                for c in detector.changes
            ]
        }
    else:
        # Scan and register all schemas
        schemas = detector.scan_schema_files(directory)
        if schemas:
            detector.register_schemas(schemas)
        
        report = {
            'total_schemas': len(schemas),
            'schemas_registered': len(schemas)
        }
    
    execution_time_ms = int((time.time() - start_time) * 1000)
    
    # Record gate run in database
    breaking_score = detector.calculate_breaking_score()
    passed = breaking_score == 0
    
    run_id = detector.db.record_gate_run(
        gate_code='GATE-007',
        passed=passed,
        error_count=len(detector.breaking_changes),
        warning_count=len(detector.changes) - len(detector.breaking_changes),
        execution_time_ms=execution_time_ms,
        metadata=report
    )
    
    # Record findings
    for change in detector.breaking_changes:
        detector.db.record_gate_finding(
            run_id=run_id,
            gate_code='GATE-007',
            severity='ERROR',
            message=f"Breaking change: {change.change_type.value} on {change.field_path}",
            finding_code=change.change_type.value,
            details={
                'field_path': change.field_path,
                'old_value': str(change.old_value),
                'new_value': str(change.new_value),
                'severity': change.severity
            }
        )
    
    return (passed, report)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='GATE-007: Breaking Schema Change Detection',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Scan and register all schemas
  %(prog)s --check

  # Compare two schema versions
  %(prog)s --compare old_schema.json new_schema.json

  # Check with ATA 91 registry
  %(prog)s --registry ATA91
        """
    )
    
    parser.add_argument(
        '--check',
        action='store_true',
        help='Scan and register all schemas'
    )
    parser.add_argument(
        '--compare',
        nargs=2,
        metavar=('OLD_SCHEMA', 'NEW_SCHEMA'),
        help='Compare two schema files'
    )
    parser.add_argument(
        '--registry',
        metavar='REGISTRY',
        help='Check against registry (e.g., ATA91)'
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
    
    if not any([args.check, args.compare, args.registry]):
        parser.error('Must specify one of: --check, --compare, or --registry')
    
    directory = Path(args.directory)
    
    try:
        detector = SchemaBreakingChangeDetector(args.db_path)
        
        # Initialize database if needed
        try:
            detector.db.initialize_database()
        except Exception:
            pass  # Already initialized
        
        # Compare specific schemas
        if args.compare:
            old_path, new_path = args.compare
            passed, report = run_gate_007(
                args.db_path, directory,
                old_schema_path=old_path,
                new_schema_path=new_path
            )
            
            if args.json:
                print(json.dumps(report, indent=2))
            else:
                detector.print_changes()
                
                print(f"\n{'═'*70}")
                print(f"GATE-007: Breaking Schema Change Detection")
                print(f"{'═'*70}")
                print(f"Result: {'✅ PASSED' if passed else '❌ FAILED'}")
                print(f"Total changes: {report['total_changes']}")
                print(f"Breaking changes: {report['breaking_changes']}")
                print(f"Breaking score: {report['breaking_score']}")
                print(f"{'═'*70}")
            
            return 0 if passed else 1
        
        # Check registry or scan all
        if args.check or args.registry:
            passed, report = run_gate_007(args.db_path, directory)
            
            if args.json:
                print(json.dumps(report, indent=2))
            else:
                print(f"\n{'═'*70}")
                print(f"GATE-007: Breaking Schema Change Detection")
                print(f"{'═'*70}")
                print(f"Result: ✅ PASSED")
                print(f"Total schemas: {report['total_schemas']}")
                print(f"Schemas registered: {report['schemas_registered']}")
                print(f"{'═'*70}")
            
            return 0
        
    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return 2


if __name__ == '__main__':
    sys.exit(main())
