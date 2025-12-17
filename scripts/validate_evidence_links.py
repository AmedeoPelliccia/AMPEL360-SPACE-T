#!/usr/bin/env python3
"""
AMPEL360 Space-T GATE-008: Evidence Link Validation
===================================================
Version: 1.0
Date: 2025-12-17
Standard: Nomenclature v6.0 R1.0

Implements GATE-008 (Evidence Link Validation) to check
evidence pack integrity and ensure broken evidence trails.

This addresses Known Issue KI-PR3-005.

Usage:
    python scripts/validate_evidence_links.py --all
    python scripts/validate_evidence_links.py --file <path>
    python scripts/validate_evidence_links.py --required-only

Exit codes:
    0: All evidence links valid
    1: Invalid evidence links found
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
class EvidenceLink:
    """Represents an evidence link."""
    source_path: str
    source_artifact_id: str
    target_path: Optional[str]
    target_artifact_id: Optional[str]
    evidence_kind: str
    required: bool
    resolved: bool
    errors: List[str]


class EvidenceValidator:
    """
    Validator for evidence links and trails.
    
    Ensures that evidence references resolve correctly and that
    required evidence is present for certification and compliance.
    """
    
    # Evidence kinds
    EVIDENCE_KINDS = {
        'HASH': r'(sha256|sha512|md5):\s*[a-f0-9]{32,128}',
        'REPORT': r'(report|analysis|assessment):\s*[\w\-/\.]+',
        'DATASET': r'(dataset|data):\s*[\w\-/\.]+',
        'TEST_LOG': r'(test|log):\s*[\w\-/\.]+',
        'CERTIFICATE': r'(cert|certificate):\s*[\w\-/\.]+',
        'TRACE': r'(trace|link):\s*[\w\-\.]+',
    }
    
    # TYPEs that require evidence
    EVIDENCE_REQUIRED_TYPES = {'FHA', 'PSSA', 'SSA', 'FTA', 'CERT', 'PLAN'}
    
    def __init__(self, db_path: str = "plc_ontology.db"):
        """Initialize with database connection."""
        self.db = PLCDatabase(db_path)
        self.evidence_links: List[EvidenceLink] = []
        self.unresolved_links: List[EvidenceLink] = []
    
    def scan_file(self, file_path: Path, base_dir: Path = Path('.')) -> List[EvidenceLink]:
        """
        Scan a file for evidence references.
        
        Returns:
            List of evidence links found
        """
        links = []
        
        try:
            content = file_path.read_text(encoding='utf-8', errors='ignore')
            relative_path = str(file_path.relative_to(base_dir))
            
            # Extract artifact ID from filename if possible
            artifact_id = file_path.stem
            
            # Determine if evidence is required based on file TYPE
            required = any(typ in file_path.name for typ in self.EVIDENCE_REQUIRED_TYPES)
            
            # Search for evidence patterns
            for kind, pattern in self.EVIDENCE_KINDS.items():
                matches = re.finditer(pattern, content, re.IGNORECASE)
                
                for match in matches:
                    full_match = match.group(0)
                    # Extract target path/ID from match
                    parts = full_match.split(':', 1)
                    target = parts[1].strip() if len(parts) > 1 else None
                    
                    # Check if target resolves
                    resolved, errors = self._resolve_evidence(target, base_dir)
                    
                    link = EvidenceLink(
                        source_path=relative_path,
                        source_artifact_id=artifact_id,
                        target_path=target,
                        target_artifact_id=None,
                        evidence_kind=kind,
                        required=required,
                        resolved=resolved,
                        errors=errors
                    )
                    
                    links.append(link)
                    self.evidence_links.append(link)
                    
                    if not resolved:
                        self.unresolved_links.append(link)
                    
                    # Record in database
                    try:
                        evidence_id = self.db.record_evidence_ref(
                            source_artifact_id=artifact_id,
                            source_artifact_path=relative_path,
                            evidence_kind=kind,
                            target_path=target,
                            required=required
                        )
                        
                        self.db.update_evidence_resolution(
                            evidence_id=evidence_id,
                            resolved=resolved,
                            resolved_path=target if resolved else None,
                            validation_errors=errors if errors else None
                        )
                    except Exception:
                        pass  # Database may not be initialized
            
        except Exception as e:
            print(f"  Warning: Could not scan {file_path}: {e}")
        
        return links
    
    def _resolve_evidence(
        self,
        target: Optional[str],
        base_dir: Path
    ) -> Tuple[bool, List[str]]:
        """
        Attempt to resolve an evidence reference.
        
        Returns:
            (resolved, errors)
        """
        errors = []
        
        if not target:
            errors.append("Empty target")
            return (False, errors)
        
        # Try to resolve as file path
        target_path = base_dir / target
        if target_path.exists():
            return (True, [])
        
        # Try relative paths
        for parent in ['.', 'EVIDENCE', '../EVIDENCE', '../../EVIDENCE']:
            candidate = base_dir / parent / target
            if candidate.exists():
                return (True, [])
        
        errors.append(f"Target not found: {target}")
        return (False, errors)
    
    def scan_repository(self, directory: Path = Path('.')) -> List[EvidenceLink]:
        """
        Scan entire repository for evidence links.
        
        Returns:
            List of all evidence links found
        """
        print("Scanning repository for evidence links...")
        
        all_links = []
        
        # Find files that typically contain evidence references
        md_files = list(directory.rglob('*.md'))
        json_files = list(directory.rglob('*.json'))
        
        # Exclude certain directories
        excluded_dirs = {'.git', 'node_modules', '__pycache__', '.venv', 'venv'}
        files_to_scan = [
            f for f in (md_files + json_files)
            if not any(exc in f.parts for exc in excluded_dirs)
        ]
        
        print(f"Found {len(files_to_scan)} files to scan")
        
        for file_path in files_to_scan:
            links = self.scan_file(file_path, directory)
            all_links.extend(links)
        
        print(f"Found {len(all_links)} evidence links")
        print(f"Unresolved links: {len(self.unresolved_links)}")
        
        return all_links
    
    def print_unresolved_links(self) -> None:
        """Print unresolved evidence links."""
        if not self.unresolved_links:
            print("\n✅ All evidence links resolved")
            return
        
        print(f"\n⚠️ Found {len(self.unresolved_links)} unresolved evidence link(s):\n")
        
        # Group by required/optional
        required = [link for link in self.unresolved_links if link.required]
        optional = [link for link in self.unresolved_links if not link.required]
        
        if required:
            print(f"❌ Required evidence missing ({len(required)}):")
            for link in required[:10]:
                print(f"  Source: {link.source_path}")
                print(f"  Kind: {link.evidence_kind}")
                print(f"  Target: {link.target_path}")
                print(f"  Errors: {', '.join(link.errors)}")
                print()
            if len(required) > 10:
                print(f"  ...and {len(required) - 10} more\n")
        
        if optional:
            print(f"⚠️ Optional evidence missing ({len(optional)})")


def run_gate_008(
    db_path: str = "plc_ontology.db",
    directory: Path = Path('.'),
    required_only: bool = False
) -> Tuple[bool, Dict[str, Any]]:
    """
    Execute GATE-008 check.
    
    Returns:
        (passed, report)
    """
    import time
    start_time = time.time()
    
    validator = EvidenceValidator(db_path)
    
    # Scan repository
    all_links = validator.scan_repository(directory)
    
    # Filter for required only if requested
    unresolved = validator.unresolved_links
    if required_only:
        unresolved = [link for link in unresolved if link.required]
    
    # Generate report
    report = {
        'total_evidence_links': len(all_links),
        'unresolved_links': len(unresolved),
        'required_unresolved': len([l for l in unresolved if l.required]),
        'optional_unresolved': len([l for l in unresolved if not l.required]),
    }
    
    execution_time_ms = int((time.time() - start_time) * 1000)
    
    # For GATE-008, we use WARN level by default per Known Issues document
    # Only FAIL if required evidence is missing
    required_unresolved = [l for l in unresolved if l.required]
    passed = len(required_unresolved) == 0
    
    run_id = validator.db.record_gate_run(
        gate_code='GATE-008',
        passed=passed,
        error_count=len(required_unresolved),
        warning_count=len(unresolved) - len(required_unresolved),
        execution_time_ms=execution_time_ms,
        metadata=report
    )
    
    # Record findings
    for link in unresolved:
        severity = 'ERROR' if link.required else 'WARN'
        validator.db.record_gate_finding(
            run_id=run_id,
            gate_code='GATE-008',
            severity=severity,
            message=f"Unresolved {link.evidence_kind} evidence: {link.target_path}",
            artifact_path=link.source_path,
            finding_code='UNRESOLVED_EVIDENCE',
            details={
                'evidence_kind': link.evidence_kind,
                'target_path': link.target_path,
                'required': link.required,
                'errors': link.errors
            }
        )
    
    return (passed, report)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='GATE-008: Evidence Link Validation',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Validate all evidence links
  %(prog)s --all

  # Check required evidence only
  %(prog)s --all --required-only

  # Validate specific file
  %(prog)s --file path/to/file.md
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
        '--required-only',
        action='store_true',
        help='Only check required evidence'
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
        validator = EvidenceValidator(args.db_path)
        
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
            
            links = validator.scan_file(file_path, directory)
            
            if args.json:
                print(json.dumps([{
                    'source': l.source_path,
                    'kind': l.evidence_kind,
                    'target': l.target_path,
                    'required': l.required,
                    'resolved': l.resolved,
                    'errors': l.errors
                } for l in links], indent=2))
            else:
                print(f"Found {len(links)} evidence link(s) in {args.file}")
                validator.print_unresolved_links()
            
            return 0 if all(l.resolved for l in links) else 1
        
        # Scan all
        if args.all:
            passed, report = run_gate_008(args.db_path, directory, args.required_only)
            
            if args.json:
                print(json.dumps(report, indent=2))
            else:
                validator.print_unresolved_links()
                
                print(f"\n{'═'*70}")
                print(f"GATE-008: Evidence Link Validation")
                print(f"{'═'*70}")
                result_text = '✅ PASSED' if passed else '⚠️ WARNING'
                if not passed:
                    result_text += ' (required evidence missing)'
                print(f"Result: {result_text}")
                print(f"Total evidence links: {report['total_evidence_links']}")
                print(f"Unresolved links: {report['unresolved_links']}")
                print(f"  Required: {report['required_unresolved']}")
                print(f"  Optional: {report['optional_unresolved']}")
                print(f"{'═'*70}")
            
            return 0 if passed else 1
        
    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return 2


if __name__ == '__main__':
    sys.exit(main())
