#!/usr/bin/env python3
"""
AMPEL360 Space-T GATE-005: Identifier Grammar Check
===================================================
Version: 1.0
Date: 2025-12-17
Standard: Nomenclature v6.0 R1.0

Implements GATE-005 (Identifier Grammar Check) to validate
identifier syntax beyond nomenclature.

This addresses Known Issue KI-PR3-003.

Usage:
    python scripts/validate_identifiers.py --all
    python scripts/validate_identifiers.py --file <path>
    python scripts/validate_identifiers.py --kind <identifier_kind>

Exit codes:
    0: All identifiers valid
    1: Invalid identifiers found
    2: Script error
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass

# Import PLC database module
try:
    from plc_db import PLCDatabase
except ImportError:
    sys.path.insert(0, str(Path(__file__).parent))
    from plc_db import PLCDatabase


@dataclass
class IdentifierInstance:
    """Represents an identifier instance found in a file."""
    identifier_kind: str
    identifier_value: str
    artifact_path: str
    line_number: Optional[int]
    context: Optional[str]
    valid: bool
    errors: List[str]


class IdentifierValidator:
    """
    Validator for identifier grammar across the repository.
    
    Validates identifiers against defined grammar rules beyond
    the basic nomenclature validation.
    """
    
    def __init__(self, db_path: str = "plc_ontology.db"):
        """Initialize with database connection."""
        self.db = PLCDatabase(db_path)
        self.grammars = self._load_grammars()
        self.invalid_instances: List[IdentifierInstance] = []
    
    def _load_grammars(self) -> Dict[str, Dict[str, Any]]:
        """Load identifier grammars from database."""
        grammars = {}
        
        # Try to get from database
        try:
            with self.db.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM identifier_grammar")
                for row in cursor.fetchall():
                    row_dict = dict(row)
                    grammars[row_dict['identifier_kind']] = {
                        'description': row_dict['description'],
                        'regex': row_dict['regex_pattern'],
                        'owner_aor': row_dict['owner_aor']
                    }
        except Exception:
            pass  # Database not initialized yet
        
        # Add default grammars if database empty
        if not grammars:
            grammars = {
                'am_id': {
                    'description': 'AMPEL360 Master Identifier',
                    'regex': r'^AM-[A-Z]{2,4}-[0-9]{4,6}$',
                    'owner_aor': 'CM'
                },
                'teknia_id': {
                    'description': 'TEKNIA Credential Identifier',
                    'regex': r'^TEK-[A-Z]{3,5}-[0-9]{6}$',
                    'owner_aor': 'CERT'
                },
                'schema_id': {
                    'description': 'Schema Registry Identifier',
                    'regex': r'^SCH-ATA[0-9]{2,3}-[A-Z0-9-]+$',
                    'owner_aor': 'DATA'
                },
                'trace_id': {
                    'description': 'Trace Link Identifier',
                    'regex': r'^TR-[A-Z]{2,4}-[0-9]{4}$',
                    'owner_aor': 'SE'
                },
                'namespace_id': {
                    'description': 'Namespace Identifier',
                    'regex': r'^NS-ATA[0-9]{2,3}-[A-Z0-9-]+$',
                    'owner_aor': 'DATA'
                },
                'requirement_id': {
                    'description': 'Requirement Identifier',
                    'regex': r'^REQ-[A-Z]{2,4}-[0-9]{4}$',
                    'owner_aor': 'SE'
                },
                'test_id': {
                    'description': 'Test Case Identifier',
                    'regex': r'^TC-[A-Z]{2,4}-[0-9]{4}$',
                    'owner_aor': 'TEST'
                },
                'hazard_id': {
                    'description': 'Hazard Identifier',
                    'regex': r'^HAZ-[A-Z]{2,4}-[0-9]{4}$',
                    'owner_aor': 'SAF'
                }
            }
        
        return grammars
    
    def scan_file(self, file_path: Path, base_dir: Path = Path('.')) -> List[IdentifierInstance]:
        """
        Scan a single file for identifiers.
        
        Returns:
            List of identifier instances found
        """
        instances = []
        
        try:
            content = file_path.read_text(encoding='utf-8', errors='ignore')
            lines = content.split('\n')
            
            relative_path = str(file_path.relative_to(base_dir))
            
            for line_num, line in enumerate(lines, 1):
                # Check each identifier pattern
                for id_kind, grammar in self.grammars.items():
                    pattern = grammar['regex']
                    
                    # Find all matches in the line
                    matches = re.finditer(pattern, line)
                    
                    for match in matches:
                        id_value = match.group(0)
                        
                        # Validate the identifier
                        is_valid, errors = self.validate_identifier(id_kind, id_value)
                        
                        instance = IdentifierInstance(
                            identifier_kind=id_kind,
                            identifier_value=id_value,
                            artifact_path=relative_path,
                            line_number=line_num,
                            context=line.strip()[:100],  # First 100 chars of line
                            valid=is_valid,
                            errors=errors
                        )
                        
                        instances.append(instance)
                        
                        if not is_valid:
                            self.invalid_instances.append(instance)
                        
                        # Record in database
                        try:
                            self.db.record_identifier_instance(
                                identifier_kind=id_kind,
                                identifier_value=id_value,
                                artifact_path=relative_path,
                                valid=is_valid,
                                artifact_line=line_num,
                                context={'line': line.strip()[:100]},
                                validation_errors=errors if errors else None
                            )
                        except Exception:
                            pass  # Database may not be initialized
            
        except Exception as e:
            print(f"  Warning: Could not scan {file_path}: {e}")
        
        return instances
    
    def scan_repository(self, directory: Path = Path('.')) -> List[IdentifierInstance]:
        """
        Scan entire repository for identifiers.
        
        Returns:
            List of all identifier instances found
        """
        print("Scanning repository for identifiers...")
        
        all_instances = []
        
        # Find Markdown, JSON, and YAML files
        md_files = list(directory.rglob('*.md'))
        json_files = list(directory.rglob('*.json'))
        yaml_files = list(directory.rglob('*.yaml')) + list(directory.rglob('*.yml'))
        
        # Exclude certain directories
        excluded_dirs = {'.git', 'node_modules', '__pycache__', '.venv', 'venv'}
        files_to_scan = [
            f for f in (md_files + json_files + yaml_files)
            if not any(exc in f.parts for exc in excluded_dirs)
        ]
        
        print(f"Found {len(files_to_scan)} files to scan")
        
        for file_path in files_to_scan:
            instances = self.scan_file(file_path, directory)
            all_instances.extend(instances)
        
        print(f"Found {len(all_instances)} identifier instances")
        print(f"Invalid identifiers: {len(self.invalid_instances)}")
        
        return all_instances
    
    def validate_identifier(self, id_kind: str, id_value: str) -> Tuple[bool, List[str]]:
        """
        Validate a single identifier against its grammar.
        
        Returns:
            (is_valid, error_messages)
        """
        errors = []
        
        if id_kind not in self.grammars:
            errors.append(f"Unknown identifier kind: {id_kind}")
            return (False, errors)
        
        grammar = self.grammars[id_kind]
        pattern = grammar['regex']
        
        # Check basic pattern match
        if not re.match(pattern, id_value):
            errors.append(f"Does not match pattern: {pattern}")
            return (False, errors)
        
        # Additional validation rules can be added here
        # For example:
        # - Check if ID is registered in appropriate registry
        # - Check if ID follows organizational numbering scheme
        # - Check if ID is properly scoped
        
        return (True, [])
    
    def print_invalid_identifiers(self) -> None:
        """Print invalid identifiers in a readable format."""
        if not self.invalid_instances:
            print("\n✅ All identifiers valid")
            return
        
        print(f"\n❌ Found {len(self.invalid_instances)} invalid identifier(s):\n")
        
        # Group by identifier kind
        by_kind: Dict[str, List[IdentifierInstance]] = {}
        for instance in self.invalid_instances:
            if instance.identifier_kind not in by_kind:
                by_kind[instance.identifier_kind] = []
            by_kind[instance.identifier_kind].append(instance)
        
        for id_kind, instances in sorted(by_kind.items()):
            print(f"Identifier Kind: {id_kind}")
            grammar = self.grammars.get(id_kind, {})
            print(f"  Expected pattern: {grammar.get('regex', 'N/A')}")
            print(f"  Invalid instances: {len(instances)}")
            print()
            
            for instance in instances[:5]:  # Show first 5
                print(f"    File: {instance.artifact_path}:{instance.line_number}")
                print(f"    Value: {instance.identifier_value}")
                print(f"    Errors: {', '.join(instance.errors)}")
                print()
            
            if len(instances) > 5:
                print(f"    ...and {len(instances) - 5} more\n")


def run_gate_005(db_path: str = "plc_ontology.db", directory: Path = Path('.')) -> Tuple[bool, Dict[str, Any]]:
    """
    Execute GATE-005 check.
    
    Returns:
        (passed, report)
    """
    import time
    start_time = time.time()
    
    validator = IdentifierValidator(db_path)
    
    # Scan repository
    all_instances = validator.scan_repository(directory)
    
    # Generate report
    report = {
        'total_identifiers': len(all_instances),
        'invalid_identifiers': len(validator.invalid_instances),
        'by_kind': {}
    }
    
    # Count by kind
    for instance in all_instances:
        kind = instance.identifier_kind
        if kind not in report['by_kind']:
            report['by_kind'][kind] = {'total': 0, 'invalid': 0}
        report['by_kind'][kind]['total'] += 1
        if not instance.valid:
            report['by_kind'][kind]['invalid'] += 1
    
    execution_time_ms = int((time.time() - start_time) * 1000)
    
    # Record gate run in database
    passed = len(validator.invalid_instances) == 0
    run_id = validator.db.record_gate_run(
        gate_code='GATE-005',
        passed=passed,
        error_count=len(validator.invalid_instances),
        warning_count=0,
        execution_time_ms=execution_time_ms,
        metadata=report
    )
    
    # Record findings
    for instance in validator.invalid_instances:
        validator.db.record_gate_finding(
            run_id=run_id,
            gate_code='GATE-005',
            severity='ERROR',
            message=f"Invalid {instance.identifier_kind}: {instance.identifier_value}",
            artifact_path=instance.artifact_path,
            line_number=instance.line_number,
            finding_code='INVALID_IDENTIFIER',
            details={
                'identifier_kind': instance.identifier_kind,
                'identifier_value': instance.identifier_value,
                'errors': instance.errors,
                'context': instance.context
            }
        )
    
    return (passed, report)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='GATE-005: Identifier Grammar Check',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Validate all identifiers in repository
  %(prog)s --all

  # Validate identifiers in a specific file
  %(prog)s --file path/to/file.md

  # Show specific identifier kind
  %(prog)s --all --kind am_id
        """
    )
    
    parser.add_argument(
        '--all',
        action='store_true',
        help='Scan entire repository'
    )
    parser.add_argument(
        '--file',
        metavar='PATH',
        help='Scan a specific file'
    )
    parser.add_argument(
        '--kind',
        metavar='IDENTIFIER_KIND',
        help='Filter by identifier kind'
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
    
    if not any([args.all, args.file]):
        parser.error('Must specify either --all or --file')
    
    directory = Path(args.directory)
    
    try:
        validator = IdentifierValidator(args.db_path)
        
        # Initialize database if needed
        try:
            validator.db.initialize_database()
        except Exception:
            pass  # Already initialized
        
        # Scan file
        if args.file:
            file_path = directory / args.file
            if not file_path.exists():
                print(f"❌ File not found: {file_path}", file=sys.stderr)
                return 1
            
            instances = validator.scan_file(file_path, directory)
            
            # Filter by kind if specified
            if args.kind:
                instances = [i for i in instances if i.identifier_kind == args.kind]
            
            if args.json:
                print(json.dumps([{
                    'kind': i.identifier_kind,
                    'value': i.identifier_value,
                    'path': i.artifact_path,
                    'line': i.line_number,
                    'valid': i.valid,
                    'errors': i.errors
                } for i in instances], indent=2))
            else:
                print(f"Found {len(instances)} identifier(s) in {args.file}")
                validator.print_invalid_identifiers()
            
            return 0 if all(i.valid for i in instances) else 1
        
        # Scan all
        if args.all:
            passed, report = run_gate_005(args.db_path, directory)
            
            # Filter by kind if specified
            if args.kind and not args.json:
                validator.invalid_instances = [
                    i for i in validator.invalid_instances
                    if i.identifier_kind == args.kind
                ]
            
            if args.json:
                print(json.dumps(report, indent=2))
            else:
                validator.print_invalid_identifiers()
                
                print(f"\n{'═'*70}")
                print(f"GATE-005: Identifier Grammar Check")
                print(f"{'═'*70}")
                print(f"Result: {'✅ PASSED' if passed else '❌ FAILED'}")
                print(f"Total identifiers: {report['total_identifiers']}")
                print(f"Invalid identifiers: {report['invalid_identifiers']}")
                print(f"{'═'*70}")
            
            return 0 if passed else 1
        
    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return 2


if __name__ == '__main__':
    sys.exit(main())
