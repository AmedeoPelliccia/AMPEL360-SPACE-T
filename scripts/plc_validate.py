#!/usr/bin/env python3
"""
AMPEL360 Space-T PLC Process Control Logic Validator
=====================================================
Version: 1.0
Date: 2025-12-17
Standard: Nomenclature Standard v6.0 R1.0 (Normative)

Implements PLC (Process Logic Control) validation for chained consistency
between nomenclature fields and overall file naming validity.

PLC validates:
1. Field-to-field consistency (chained constraints)
2. ATA_ROOT ↔ BLOCK coherence
3. PHASE ↔ STATUS lifecycle alignment
4. AoR ↔ KNOT governance mapping
5. VARIANT ↔ SUBJECT prefix requirements
6. MODEL ↔ TYPE alignment
7. Cross-field semantic validation

Usage:
    python scripts/plc_validate.py <filename>
    python scripts/plc_validate.py --check-all
    python scripts/plc_validate.py --check-dir <directory>

Exit codes:
    0: All files valid
    1: One or more files invalid
    2: Script error
"""

import argparse
import re
import sys
import yaml
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass, field


@dataclass
class PLCValidationResult:
    """Result of PLC validation."""
    filename: str
    valid: bool
    parsed_fields: Dict[str, str]
    consistency_errors: List[str] = field(default_factory=list)
    consistency_warnings: List[str] = field(default_factory=list)
    chain_violations: List[Tuple[str, str, str]] = field(default_factory=list)  # (field1, field2, reason)


class PLCValidator:
    """
    PLC (Process Logic Control) Validator for nomenclature chained consistency.
    
    Implements cross-field validation rules to ensure semantic coherence
    between related nomenclature fields.
    """
    
    # v6.0 pattern for parsing filenames
    PATTERN_V6 = re.compile(
        r'^(?P<ata_root>(?:0[0-9]|[1-9][0-9]|10[0-9]|11[0-6]))_'
        r'(?P<project>AMPEL360)_'
        r'(?P<program>SPACET)_'
        r'(?P<family>Q[0-9]{2,3})_'
        r'(?P<variant>[A-Z0-9]+)_'
        r'(?P<version>(?:PLUS|PLUSULTRA)(?:[0-9]{2})?)_'
        r'(?P<model>[A-Z]{2})_'
        r'(?P<block>[A-Z0-9]+)_'
        r'(?P<phase>(?:LC(?:0[1-9]|1[0-4])|SB(?:0[1-9]|[1-9][0-9])))_'
        r'(?P<knot_task>K(?:0[1-9]|1[0-4])(?:-T[0-9]{3})?)_'
        r'(?P<aor>[A-Z]+)__'
        r'(?P<subject>[a-z0-9]+(?:-[a-z0-9]+)*)_'
        r'(?P<type>[A-Z0-9]+)_'
        r'(?P<issue_revision>I[0-9]{2}-R[0-9]{2})_'
        r'(?P<status>[A-Z]+)'
        r'\.(?P<ext>[a-z0-9]{1,6})$'
    )
    
    # ATA chapter to primary BLOCK mapping (semantic coherence)
    ATA_BLOCK_MAP = {
        # O-ORGANIZATION (ATA 00-09)
        (0, 9): ['GEN', 'OPS', 'CERT', 'SAF', 'DATA'],
        # T-TECHNOLOGY / Vehicle Systems (ATA 21-79)
        (21, 27): ['OPS', 'STR', 'SYS', 'HW'],
        (28, 29): ['PROP', 'HW', 'SYS'],
        (30, 39): ['HW', 'SYS', 'OPS'],
        (40, 49): ['SW', 'SYS', 'HW'],
        (50, 59): ['STR', 'HW'],
        (70, 79): ['PROP', 'HW', 'ENRG'],
        # I-INFRASTRUCTURES (ATA 80-90, 115-116)
        (80, 90): ['OPS', 'MRO', 'STOR', 'ENRG'],
        (115, 116): ['OPS', 'MRO', 'DATA'],
        # N-NEURAL (ATA 95-98)
        (95, 98): ['AI', 'DATA', 'SW'],
        # S-SIM_TEST (ATA 100-114)
        (100, 114): ['TEST', 'SW', 'DATA', 'SYS'],
    }
    
    # PHASE ↔ STATUS lifecycle alignment
    PHASE_STATUS_RULES = {
        # Early lifecycle phases (LC01-LC03) typically have DRAFT/ACTIVE
        'LC01': ['DRAFT', 'ACTIVE', 'TEMPLATE'],
        'LC02': ['DRAFT', 'ACTIVE', 'TEMPLATE'],
        'LC03': ['DRAFT', 'ACTIVE', 'APPROVED'],
        # Design phases (LC04-LC06) progress to APPROVED
        'LC04': ['DRAFT', 'ACTIVE', 'APPROVED'],
        'LC05': ['DRAFT', 'ACTIVE', 'APPROVED'],
        'LC06': ['DRAFT', 'ACTIVE', 'APPROVED'],
        # V&V phases (LC07-LC08) require APPROVED or RELEASED
        'LC07': ['ACTIVE', 'APPROVED', 'RELEASED'],
        'LC08': ['ACTIVE', 'APPROVED', 'RELEASED'],
        # Production/Certification (LC09-LC10) require APPROVED/RELEASED
        'LC09': ['APPROVED', 'RELEASED'],
        'LC10': ['APPROVED', 'RELEASED'],
        # Operations/Sustainment (LC11-LC14) allow all mature statuses
        'LC11': ['ACTIVE', 'APPROVED', 'RELEASED', 'SUPERSEDED'],
        'LC12': ['ACTIVE', 'APPROVED', 'RELEASED', 'SUPERSEDED'],
        'LC13': ['ACTIVE', 'APPROVED', 'RELEASED', 'SUPERSEDED', 'ARCHIVED'],
        'LC14': ['ACTIVE', 'APPROVED', 'RELEASED', 'SUPERSEDED', 'ARCHIVED'],
    }
    
    # AoR ↔ KNOT governance mapping (which KNOTs each AoR primarily owns/participates in)
    AOR_KNOT_MAP = {
        'CM': ['K01', 'K04', 'K06', 'K08', 'K10'],
        'CERT': ['K01', 'K05', 'K10'],
        'SAF': ['K01', 'K03', 'K05', 'K11', 'K12'],
        'SE': ['K02', 'K04', 'K05', 'K06', 'K14'],
        'OPS': ['K02', 'K09', 'K11', 'K12', 'K14'],
        'DATA': ['K06', 'K08', 'K13'],
        'AI': ['K06', 'K07', 'K13'],
        'CY': ['K09', 'K13'],
        'TEST': ['K05', 'K10', 'K12', 'K14'],
        'MRO': ['K10', 'K11', 'K14'],
        'SPACEPORT': ['K03', 'K09', 'K10', 'K11'],
        'PMO': ['K01', 'K02', 'K10', 'K14'],
    }
    
    # MODEL ↔ TYPE alignment (which TYPEs are appropriate for each MODEL)
    MODEL_TYPE_MAP = {
        'BB': ['IDX', 'STD', 'PLAN', 'CAT', 'SCH', 'DIA', 'TAB', 'GLO', 'TRC'],  # Body Brain - schemas, indexes
        'HW': ['SPEC', 'REQ', 'ANA', 'DIA', 'MAT', 'RPT', 'FHA', 'PSSA', 'SSA', 'FTA'],  # Hardware
        'SW': ['SPEC', 'REQ', 'ANA', 'API', 'CFG', 'RPT', 'DAL'],  # Software
        'PR': ['PLAN', 'PROC', 'MAN', 'LOG', 'MIN', 'RPT', 'ACT'],  # Process/Procedure
    }
    
    # VARIANT ↔ SUBJECT prefix requirements (already in v6.0, but validated here for PLC)
    VARIANT_SUBJECT_PREFIX = {
        'CUST': r'^cust-[a-z0-9]{2,12}-',
        'MSN': r'^msn-[0-9]{3,6}-',
    }
    
    # BLOCK ↔ AoR coherence (which AoRs typically work in which BLOCKs)
    BLOCK_AOR_MAP = {
        'OPS': ['OPS', 'SPACEPORT', 'MRO', 'PMO'],
        'STR': ['SE', 'CERT', 'SAF'],
        'PROP': ['SE', 'SAF', 'CERT'],
        'AI': ['AI', 'DATA', 'CY'],
        'DATA': ['DATA', 'CM', 'AI', 'CY'],
        'CERT': ['CERT', 'SAF', 'CM'],
        'SAF': ['SAF', 'CERT', 'SE', 'OPS'],
        'SW': ['SE', 'AI', 'TEST', 'CERT'],
        'HW': ['SE', 'TEST', 'CERT', 'MRO'],
        'SYS': ['SE', 'CERT', 'SAF', 'TEST'],
        'TEST': ['TEST', 'SE', 'CERT', 'SAF'],
        'MRO': ['MRO', 'OPS', 'SPACEPORT'],
        'CIRC': ['SE', 'OPS', 'DATA', 'PMO'],
        'ENRG': ['SE', 'OPS', 'SAF'],
        'STOR': ['SE', 'OPS', 'SAF'],
        'GEN': ['CM', 'PMO', 'DATA', 'SE', 'OPS', 'CERT', 'SAF', 'AI', 'CY', 'TEST', 'MRO', 'SPACEPORT'],
    }
    
    def __init__(self, config_path: Optional[str] = None, strict: bool = True, 
                 mode: str = "warn"):
        """
        Initialize PLC validator.
        
        Args:
            config_path: Path to v6.0 config YAML file
            strict: If True, treat consistency warnings as errors
            mode: Validation mode ("warn", "report", "block")
        """
        self.strict = strict
        self.mode = mode
        self.config = self._load_config(config_path or "config/nomenclature/v6_0.yaml")
        
        # Extract exemptions
        exemptions = self.config.get('exemptions', {})
        self.excluded_files = set(exemptions.get('files', []))
        self.excluded_dirs = set(exemptions.get('directories', []))
        self.excluded_patterns = exemptions.get('patterns', [])
    
    def _load_config(self, config_path: str) -> Dict[str, Any]:
        """Load configuration from YAML file."""
        try:
            path = Path(config_path)
            if not path.exists():
                script_dir = Path(__file__).parent.parent
                path = script_dir / config_path
            
            if path.exists():
                with open(path, 'r') as f:
                    return yaml.safe_load(f) or {}
        except Exception as e:
            print(f"Warning: Failed to load config: {e}", file=sys.stderr)
        return {}
    
    def parse_filename(self, filename: str) -> Optional[Dict[str, str]]:
        """
        Parse filename into component fields.
        
        Returns:
            Dictionary of parsed fields, or None if parsing fails
        """
        match = self.PATTERN_V6.match(filename)
        if match:
            return match.groupdict()
        return None
    
    def validate_chained_consistency(self, filename: str) -> PLCValidationResult:
        """
        Validate chained consistency between nomenclature fields.
        
        This is the core PLC validation that checks semantic coherence
        between related fields in the nomenclature.
        
        Args:
            filename: The filename to validate
            
        Returns:
            PLCValidationResult with consistency validation results
        """
        # Check if file should be excluded
        if filename in self.excluded_files:
            return PLCValidationResult(filename, True, {})
        
        for pattern in self.excluded_patterns:
            if re.match(pattern, filename):
                return PLCValidationResult(filename, True, {})
        
        # Parse the filename
        fields = self.parse_filename(filename)
        if fields is None:
            return PLCValidationResult(
                filename, False, {},
                consistency_errors=["Failed to parse filename - does not match v6.0 pattern"]
            )
        
        errors = []
        warnings = []
        chain_violations = []
        
        # Extract key fields
        ata_root = int(fields['ata_root'])
        block = fields['block']
        phase = fields['phase']
        status = fields['status']
        aor = fields['aor']
        knot_task = fields['knot_task']
        variant = fields['variant']
        subject = fields['subject']
        model = fields['model']
        type_code = fields['type']
        
        # Extract knot ID (without task suffix)
        knot_id = knot_task.split('-')[0]  # K01, K02, etc.
        
        # ═══════════════════════════════════════════════════════════════════
        # CHAIN 1: ATA_ROOT ↔ BLOCK coherence
        # ═══════════════════════════════════════════════════════════════════
        ata_mapped = False
        for (ata_min, ata_max), valid_blocks in self.ATA_BLOCK_MAP.items():
            if ata_min <= ata_root <= ata_max:
                ata_mapped = True
                if block not in valid_blocks and block != 'GEN':
                    # GEN block is always acceptable as a fallback
                    chain_violations.append((
                        'ATA_ROOT', 'BLOCK',
                        f"ATA {ata_root} typically uses BLOCK in {valid_blocks}, not '{block}'"
                    ))
                    warnings.append(
                        f"ATA_ROOT↔BLOCK: ATA {ata_root} is typically in {valid_blocks}, not '{block}'"
                    )
                break
        
        # If ATA chapter is not in any mapped range, GEN is always acceptable
        # For unmapped ATAs, only warn if BLOCK is not GEN (permissive for gaps)
        if not ata_mapped and block != 'GEN':
            warnings.append(
                f"ATA_ROOT↔BLOCK: ATA {ata_root} has no explicit mapping; using BLOCK '{block}' (GEN is preferred for unmapped)"
            )
        
        # ═══════════════════════════════════════════════════════════════════
        # CHAIN 2: PHASE ↔ STATUS lifecycle alignment
        # ═══════════════════════════════════════════════════════════════════
        if phase.startswith('LC'):
            if phase in self.PHASE_STATUS_RULES:
                valid_statuses = self.PHASE_STATUS_RULES[phase]
                if status not in valid_statuses:
                    chain_violations.append((
                        'PHASE', 'STATUS',
                        f"{phase} typically has STATUS in {valid_statuses}, not '{status}'"
                    ))
                    warnings.append(
                        f"PHASE↔STATUS: {phase} lifecycle phase typically uses STATUS in {valid_statuses}, not '{status}'"
                    )
        
        # ═══════════════════════════════════════════════════════════════════
        # CHAIN 3: AoR ↔ KNOT governance mapping
        # ═══════════════════════════════════════════════════════════════════
        if aor in self.AOR_KNOT_MAP:
            expected_knots = self.AOR_KNOT_MAP[aor]
            if knot_id not in expected_knots:
                chain_violations.append((
                    'AoR', 'KNOT_TASK',
                    f"AoR '{aor}' typically works on KNOTs {expected_knots}, not '{knot_id}'"
                ))
                warnings.append(
                    f"AoR↔KNOT: AoR '{aor}' typically participates in {expected_knots}, not '{knot_id}'"
                )
        
        # ═══════════════════════════════════════════════════════════════════
        # CHAIN 4: VARIANT ↔ SUBJECT prefix requirements (MANDATORY)
        # ═══════════════════════════════════════════════════════════════════
        if variant in self.VARIANT_SUBJECT_PREFIX:
            required_pattern = self.VARIANT_SUBJECT_PREFIX[variant]
            if not re.match(required_pattern, subject):
                chain_violations.append((
                    'VARIANT', 'SUBJECT',
                    f"VARIANT '{variant}' REQUIRES SUBJECT prefix matching '{required_pattern}'"
                ))
                errors.append(
                    f"VARIANT↔SUBJECT: VARIANT '{variant}' requires SUBJECT to match prefix '{required_pattern}'"
                )
        
        # ═══════════════════════════════════════════════════════════════════
        # CHAIN 5: MODEL ↔ TYPE alignment
        # ═══════════════════════════════════════════════════════════════════
        if model in self.MODEL_TYPE_MAP:
            valid_types = self.MODEL_TYPE_MAP[model]
            if type_code not in valid_types:
                chain_violations.append((
                    'MODEL', 'TYPE',
                    f"MODEL '{model}' typically uses TYPE in {valid_types}, not '{type_code}'"
                ))
                warnings.append(
                    f"MODEL↔TYPE: MODEL '{model}' typically uses TYPE in {valid_types}, not '{type_code}'"
                )
        
        # ═══════════════════════════════════════════════════════════════════
        # CHAIN 6: BLOCK ↔ AoR coherence
        # ═══════════════════════════════════════════════════════════════════
        if block in self.BLOCK_AOR_MAP:
            expected_aors = self.BLOCK_AOR_MAP[block]
            if aor not in expected_aors:
                chain_violations.append((
                    'BLOCK', 'AoR',
                    f"BLOCK '{block}' typically has AoR in {expected_aors}, not '{aor}'"
                ))
                warnings.append(
                    f"BLOCK↔AoR: BLOCK '{block}' typically works with AoR in {expected_aors}, not '{aor}'"
                )
        
        # ═══════════════════════════════════════════════════════════════════
        # CHAIN 7: Cross-field semantic validation
        # ═══════════════════════════════════════════════════════════════════
        
        # 7a: CERT variant should typically have CERT-related BLOCK/AoR
        if variant == 'CERT' and block not in ['CERT', 'SAF', 'GEN'] and aor not in ['CERT', 'SAF']:
            chain_violations.append((
                'VARIANT', 'BLOCK/AoR',
                f"CERT variant typically has CERT-related BLOCK/AoR"
            ))
            warnings.append(
                f"VARIANT↔BLOCK/AoR: CERT variant should typically have CERT/SAF BLOCK or AoR"
            )
        
        # 7b: FLIGHTTEST variant should typically be in TEST-related areas
        if variant == 'FLIGHTTEST' and block not in ['TEST', 'OPS', 'SYS'] and aor not in ['TEST', 'OPS']:
            chain_violations.append((
                'VARIANT', 'BLOCK/AoR',
                f"FLIGHTTEST variant typically has TEST/OPS-related BLOCK/AoR"
            ))
            warnings.append(
                f"VARIANT↔BLOCK/AoR: FLIGHTTEST variant should typically have TEST/OPS BLOCK or AoR"
            )
        
        # 7c: S-axis (ATA 100-114) should have TEST-related content
        if 100 <= ata_root <= 114:
            if block not in ['TEST', 'SW', 'DATA', 'SYS', 'GEN']:
                chain_violations.append((
                    'ATA_ROOT', 'BLOCK',
                    f"S-axis ATA {ata_root} should have TEST/SW/DATA/SYS block"
                ))
                warnings.append(
                    f"ATA_ROOT↔BLOCK: S-axis ATA {ata_root} should typically use TEST/SW/DATA/SYS BLOCK"
                )
        
        # 7d: Neural chapters (95-98) should have AI/DATA content
        if 95 <= ata_root <= 98:
            if block not in ['AI', 'DATA', 'SW', 'GEN'] and aor not in ['AI', 'DATA']:
                chain_violations.append((
                    'ATA_ROOT', 'BLOCK/AoR',
                    f"Neural ATA {ata_root} should have AI/DATA-related content"
                ))
                warnings.append(
                    f"ATA_ROOT↔BLOCK/AoR: Neural ATA {ata_root} should typically have AI/DATA BLOCK or AoR"
                )
        
        # Determine overall validity based on mode
        if self.mode == "warn" or self.mode == "report":
            # In warn/report mode, treat errors as warnings (no failure)
            valid = True
            warnings_to_add = errors.copy()  # Don't mutate original list
            consistency_warnings = warnings + warnings_to_add
            consistency_errors = []
        else:
            # In block mode, only MANDATORY errors cause failure
            valid = len(errors) == 0
            consistency_errors = errors
            consistency_warnings = warnings
        
        return PLCValidationResult(
            filename=filename,
            valid=valid,
            parsed_fields=fields,
            consistency_errors=consistency_errors,
            consistency_warnings=consistency_warnings,
            chain_violations=chain_violations
        )
    
    def validate_directory(self, directory: Path, recursive: bool = True) -> List[PLCValidationResult]:
        """Validate all files in a directory."""
        results = []
        
        if recursive:
            for path in directory.rglob('*'):
                if path.is_file() and not self._is_excluded_path(path):
                    results.append(self.validate_chained_consistency(path.name))
        else:
            for path in directory.iterdir():
                if path.is_file() and path.name not in self.excluded_files:
                    results.append(self.validate_chained_consistency(path.name))
        
        return results
    
    def _is_excluded_path(self, path: Path) -> bool:
        """Check if path should be excluded from validation."""
        for parent in path.parents:
            if parent.name in self.excluded_dirs:
                return True
        
        if path.name in self.excluded_files:
            return True
        
        for pattern in self.excluded_patterns:
            if re.match(pattern, path.name):
                return True
        
        return False


def print_result(result: PLCValidationResult, verbose: bool = False) -> None:
    """Print PLC validation result to console."""
    if result.valid:
        if verbose or result.consistency_warnings:
            print(f"✓ {result.filename}")
            for warning in result.consistency_warnings:
                print(f"  ⚠ {warning}")
            if verbose and result.chain_violations:
                print(f"  Chain violations: {len(result.chain_violations)}")
    else:
        print(f"✗ {result.filename}")
        for error in result.consistency_errors:
            print(f"  ✗ Error: {error}")
        for warning in result.consistency_warnings:
            print(f"  ⚠ Warning: {warning}")
        if result.chain_violations:
            print(f"  Chain violations ({len(result.chain_violations)}):")
            for field1, field2, reason in result.chain_violations:
                print(f"    • {field1}↔{field2}: {reason}")


def generate_plc_report(results: List[PLCValidationResult]) -> Dict[str, Any]:
    """Generate a summary report of PLC validation results."""
    total = len(results)
    valid = sum(1 for r in results if r.valid)
    invalid = total - valid
    
    # Count chain violations by type
    violation_counts = {}
    for result in results:
        for field1, field2, _ in result.chain_violations:
            key = f"{field1}↔{field2}"
            violation_counts[key] = violation_counts.get(key, 0) + 1
    
    return {
        'total_files': total,
        'valid_files': valid,
        'invalid_files': invalid,
        'pass_rate': f"{(valid/total)*100:.1f}%" if total > 0 else "N/A",
        'chain_violation_summary': violation_counts,
        'files_with_warnings': sum(1 for r in results if r.consistency_warnings),
        'files_with_errors': sum(1 for r in results if r.consistency_errors),
    }


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='PLC (Process Logic Control) validator for AMPEL360 Space-T nomenclature chained consistency',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
PLC validates chained consistency between nomenclature fields:

  CHAIN 1: ATA_ROOT ↔ BLOCK coherence
  CHAIN 2: PHASE ↔ STATUS lifecycle alignment  
  CHAIN 3: AoR ↔ KNOT governance mapping
  CHAIN 4: VARIANT ↔ SUBJECT prefix (MANDATORY)
  CHAIN 5: MODEL ↔ TYPE alignment
  CHAIN 6: BLOCK ↔ AoR coherence
  CHAIN 7: Cross-field semantic validation

Examples:
  %(prog)s 27_AMPEL360_SPACET_Q10_GEN_PLUS_BB_OPS_LC03_K06_SE__thermal-loop_STD_I01-R01_ACTIVE.md
  %(prog)s --check-all
  %(prog)s --check-all --verbose
  %(prog)s --report
        """
    )
    
    parser.add_argument(
        'filename',
        nargs='?',
        help='Filename to validate'
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
        '--mode',
        choices=['warn', 'report', 'block'],
        default='warn',
        help='Validation mode: warn (default), report (detailed), block (fail on error)'
    )
    parser.add_argument(
        '--config',
        metavar='CONFIG',
        help='Path to config YAML file'
    )
    parser.add_argument(
        '--strict',
        action='store_true',
        default=False,
        help='Treat warnings as errors'
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Show all results including valid files'
    )
    parser.add_argument(
        '--report',
        action='store_true',
        help='Generate summary report'
    )
    
    args = parser.parse_args()
    
    if not any([args.filename, args.check_all, args.check_dir]):
        parser.error('Must specify filename, --check-all, or --check-dir')
    
    validator = PLCValidator(
        config_path=args.config,
        strict=args.strict,
        mode=args.mode
    )
    results = []
    
    try:
        if args.filename:
            result = validator.validate_chained_consistency(args.filename)
            results = [result]
        elif args.check_dir:
            dir_path = Path(args.check_dir)
            if not dir_path.is_dir():
                print(f"Error: '{args.check_dir}' is not a directory", file=sys.stderr)
                return 2
            results = validator.validate_directory(dir_path, recursive=True)
        elif args.check_all:
            results = validator.validate_directory(Path('.'), recursive=True)
        
        # Print results
        valid_count = 0
        invalid_count = 0
        warning_count = 0
        
        for result in results:
            if result.valid:
                valid_count += 1
                if args.verbose or result.consistency_warnings:
                    print_result(result, verbose=args.verbose)
                    if result.consistency_warnings:
                        warning_count += 1
            else:
                invalid_count += 1
                print_result(result, verbose=args.verbose)
        
        # Print summary
        total = len(results)
        if total > 1 or args.check_all or args.check_dir or args.report:
            print(f"\n{'═'*70}")
            print("PLC VALIDATION SUMMARY")
            print(f"{'═'*70}")
            print(f"Total files scanned: {total}")
            print(f"  ✓ Valid:   {valid_count}")
            print(f"  ✗ Invalid: {invalid_count}")
            print(f"  ⚠ With warnings: {warning_count}")
            
            if args.report:
                report = generate_plc_report(results)
                print(f"\nPass rate: {report['pass_rate']}")
                if report['chain_violation_summary']:
                    print("\nChain violation breakdown:")
                    for chain, count in sorted(report['chain_violation_summary'].items(), 
                                               key=lambda x: -x[1]):
                        print(f"  {chain}: {count}")
            
            print(f"{'═'*70}")
        
        return 0 if invalid_count == 0 else 1
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return 2


if __name__ == '__main__':
    sys.exit(main())
