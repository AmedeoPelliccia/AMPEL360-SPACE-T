#!/usr/bin/env python3
"""
AMPEL360 Space-T Nomenclature Validator
========================================
Version: 4.0
Date: 2025-12-16
Standard: Nomenclature Standard v4.0 (Normative)

Validates filenames against the AMPEL360 Space-T nomenclature standard.

Usage:
    python validate_nomenclature.py <filename>
    python validate_nomenclature.py --check-all
    python validate_nomenclature.py --check-dir <directory>

Exit codes:
    0: All files valid
    1: One or more files invalid
    2: Script error
"""

import argparse
import re
import sys
from pathlib import Path
from typing import List
from dataclasses import dataclass


@dataclass
class ValidationResult:
    """Result of filename validation."""
    filename: str
    valid: bool
    errors: List[str]
    warnings: List[str]


class NomenclatureValidator:
    """Validates filenames against AMPEL360 Space-T nomenclature standard v4.0."""
    
    # Primary regex pattern (12 fields) - v4.0 format
    PRIMARY_PATTERN = re.compile(
        r'^(?P<root>\d{2,3})_'
        r'(?P<project>AMPEL360)_'
        r'(?P<program>SPACET)_'
        r'(?P<variant>[A-Z0-9]+(?:-[A-Z0-9]+)*)_'
        r'(?P<bucket>00|10|20|30|40|50|60|70|80|90)_'
        r'(?P<type>[A-Z0-9]{2,8})_'
        r'(?P<lcsb>(LC(0[1-9]|1[0-4])|SB(1[5-9]|[2-9]\d)))_'
        r'(?P<knot>K(00|[0-9]{2}))_'
        r'(?P<aor>CM|CERT|AI|DATA|OPS|SE|SAF|PMO|CY|TEST|MRO|SPACEPORT)__'
        r'(?P<desc>[a-z0-9]+(?:-[a-z0-9]+)*)_'
        r'(?P<ver>v\d{2})'
        r'\.(?P<ext>[a-z0-9]{1,6})$'
    )
    
    # LC stage pattern (LC01-LC14)
    LC_PATTERN = re.compile(r'^LC(0[1-9]|1[0-4])$')
    
    # SB stage pattern (SB15-SB99)
    SB_PATTERN = re.compile(r'^SB(1[5-9]|[2-9]\d)$')
    
    # VERSION format pattern
    VERSION_PATTERN = re.compile(r'^v\d{2}$')
    
    # Allowed buckets
    ALLOWED_BUCKETS = {'00', '10', '20', '30', '40', '50', '60', '70', '80', '90'}
    
    # Allowed PROJECT values (hard constraint)
    ALLOWED_PROJECTS = {'AMPEL360'}
    
    # Allowed PROGRAM values (extensible allowlist)
    ALLOWED_PROGRAMS = {'SPACET'}
    
    # Allowed AoR values (portal entry points) - NEW in v4.0
    ALLOWED_AORS = {
        'CM', 'CERT', 'AI', 'DATA', 'OPS', 'SE', 'SAF', 
        'PMO', 'CY', 'TEST', 'MRO', 'SPACEPORT'
    }
    
    # TRIGGER_KNOT pattern - NEW in v4.0
    KNOT_PATTERN = re.compile(r'^K(00|[0-9]{2})$')
    
    # Bucket-specific subbucket ranges
    BUCKET_SUBBUCKET_RANGES = {
        '10': [(15, 19), (80, 85)],  # Operations: SB15-SB19 + SB80-SB85
        '20': [(20, 29)],             # Primary Subsystem: SB20-SB29
        '30': [(30, 39)],             # Circularity: SB30-SB39
        '40': [(40, 49)],             # Software: SB40-SB49
        '50': [(50, 59)],             # Structures: SB50-SB59
        '60': [(60, 69)],             # Storages: SB60-SB69
        '70': [(70, 79)],             # Propulsion: SB70-SB79
        '80': [(86, 89)],             # Energy: SB86-SB89
        '90': [(90, 99)],             # Tables/Schemas/Diagrams/Reference: SB90-SB99
    }
    
    # Approved TYPE vocabulary
    APPROVED_TYPES = {
        # Planning / Control
        'PLAN', 'MIN', 'RPT', 'LOG', 'ACT', 'IDX',
        # Safety Analyses
        'FHA', 'PSSA', 'SSA', 'FTA', 'ANA',
        # Requirements / Allocation
        'REQ', 'DAL', 'TRC',
        # Data / Reference
        'CAT', 'LST', 'GLO', 'MAT', 'SCH', 'DIA', 'TAB', 'STD'
    }
    
    # Files to exclude from validation
    EXCLUDED_FILES = {
        'README.md', 'USAGE.md', 'LICENSE', 'EXAMPLES.md', 
        'STRUCTURE_SUMMARY.md', '.gitignore', '.gitattributes',
        '00_INDEX_README.md', 'Dependencies.yaml', 
        'Traceability_Matrix.csv', 'Prompt_to_Artifact_Map.csv',
        'CAOS_Agent_Config.yaml', 'CAE_Agent_Config.yaml', 
        'CAD_Agent_Config.yaml', 'CAM_Agent_Config.yaml',
        'IMPLEMENTATION_SUMMARY.md', 'REVIEW_NOTES.md',
        'NOMENCLATURE_V3_AUDIT_REPORT.md',
        '.gitkeep'
    }
    
    # File patterns to exclude from validation
    EXCLUDED_PATTERNS = [
        r'.*-xx_.*',  # Template files with -xx pattern
        r'generate_.*\.py',  # Generator scripts
        r'validate_.*\.py',  # Validation scripts
        r'scaffold\.py',  # Scaffolding script
        r'pre-commit',  # Git hooks
        r'.*\.py[cod]$',  # Python bytecode
        r'.*_Agent_Config\.(yaml|json|yml)$',  # Agent config files
        r'.*_Config\.(yaml|json|yml)$',  # Config files
    ]
    
    # Directories to exclude from validation
    EXCLUDED_DIRS = {
        '.git', '.github', 'node_modules', '__pycache__',
        '.pytest_cache', '.venv', 'venv', 'dist', 'build',
        'templates',  # Template source files for scaffolding
        'scripts'  # Utility scripts
    }
    
    def __init__(self, strict: bool = True):
        """
        Initialize validator.
        
        Args:
            strict: If True, enforce TYPE vocabulary; if False, only warn
        """
        self.strict = strict
    
    def validate_filename(self, filename: str) -> ValidationResult:
        """
        Validate a single filename.
        
        Args:
            filename: The filename (not path) to validate
            
        Returns:
            ValidationResult with validation status and messages
        """
        errors = []
        warnings = []
        
        # Check if file should be excluded
        if filename in self.EXCLUDED_FILES:
            return ValidationResult(filename, True, [], [])
        
        # Check if filename matches any excluded pattern
        for pattern in self.EXCLUDED_PATTERNS:
            if re.match(pattern, filename):
                return ValidationResult(filename, True, [], [])
        
        # Match against primary pattern
        match = self.PRIMARY_PATTERN.match(filename)
        
        if not match:
            errors.append(
                "Filename does not match required pattern (v4.0): "
                "[ROOT]_[PROJECT]_[PROGRAM]_[VARIANT]_[BUCKET]_[TYPE]_[LC|SB]_[TRIGGER_KNOT]_[AoR]__[DESCRIPTION]_[VERSION].[EXT]"
            )
            return ValidationResult(filename, False, errors, warnings)
        
        # Extract components
        components = match.groupdict()
        root = components['root']
        project = components['project']
        program = components['program']
        variant = components['variant']
        bucket = components['bucket']
        type_code = components['type']
        lcsb = components['lcsb']
        knot = components['knot']
        aor = components['aor']
        desc = components['desc']
        version = components['ver']
        
        # Validate BUCKET
        if bucket not in self.ALLOWED_BUCKETS:
            errors.append(f"Invalid BUCKET '{bucket}': must be one of {sorted(self.ALLOWED_BUCKETS)}")
        
        # Validate PROJECT (hard constraint)
        if project not in self.ALLOWED_PROJECTS:
            errors.append(
                f"Invalid PROJECT '{project}': must be AMPEL360 (hard constraint)"
            )
        
        # Validate PROGRAM (allowlist)
        if program not in self.ALLOWED_PROGRAMS:
            errors.append(
                f"Invalid PROGRAM '{program}': must be one of {sorted(self.ALLOWED_PROGRAMS)}"
            )
        
        # Validate TRIGGER_KNOT format (NEW in v4.0)
        if not self.KNOT_PATTERN.match(knot):
            errors.append(
                f"Invalid TRIGGER_KNOT '{knot}': must be K00 or K01-K99"
            )
        
        # Validate AoR allowlist (NEW in v4.0)
        if aor not in self.ALLOWED_AORS:
            errors.append(
                f"Invalid AoR '{aor}': must be one of {sorted(self.ALLOWED_AORS)}"
            )
        
        # Validate TYPE vocabulary
        if type_code not in self.APPROVED_TYPES:
            msg = f"TYPE '{type_code}' not in approved vocabulary: {sorted(self.APPROVED_TYPES)}"
            if self.strict:
                errors.append(msg)
            else:
                warnings.append(msg)
        
        # Validate LC|SB conditional rules
        if bucket == '00':
            # BUCKET=00 requires LC stage
            if not self.LC_PATTERN.match(lcsb):
                errors.append(
                    f"BUCKET=00 requires LC|SB to be LC01-LC14, got '{lcsb}'"
                )
        else:
            # BUCKET≠00 requires SB stage
            if not self.SB_PATTERN.match(lcsb):
                errors.append(
                    f"BUCKET={bucket} requires LC|SB to be SB format, got '{lcsb}'"
                )
            else:
                # Validate bucket-specific subbucket range
                if bucket in self.BUCKET_SUBBUCKET_RANGES:
                    try:
                        # Extract numeric part from lcsb (e.g., "SB15" -> 15)
                        sb_num = int(lcsb[2:])
                        ranges = self.BUCKET_SUBBUCKET_RANGES[bucket]
                        
                        # Check if subbucket number is in any of the allowed ranges for this bucket
                        in_range = any(start <= sb_num <= end for start, end in ranges)
                        
                        if not in_range:
                            # Format ranges for error message
                            range_strs = [f"SB{start:02d}-SB{end:02d}" for start, end in ranges]
                            allowed = " or ".join(range_strs)
                            errors.append(
                                f"BUCKET={bucket} requires LC|SB to be {allowed}, got '{lcsb}'"
                            )
                    except (ValueError, IndexError):
                        # This should not happen if SB_PATTERN matched, but handle defensively
                        errors.append(
                            f"Invalid subbucket format '{lcsb}' for BUCKET={bucket}"
                        )
        
        # Check for redundancy in DESCRIPTION
        desc_lower = desc.lower()
        type_lower = type_code.lower()
        if type_lower in desc_lower and type_lower != desc_lower:
            warnings.append(
                f"DESCRIPTION '{desc}' may redundantly include TYPE '{type_code}'"
            )
        
        # Validate VERSION format
        if not self.VERSION_PATTERN.match(version):
            errors.append(f"VERSION '{version}' must be 'vNN' with exactly 2 digits")
        
        valid = len(errors) == 0
        return ValidationResult(filename, valid, errors, warnings)
    
    def validate_file_path(self, filepath: Path) -> ValidationResult:
        """
        Validate a file by its path.
        
        Args:
            filepath: Path object to validate
            
        Returns:
            ValidationResult for the filename
        """
        return self.validate_filename(filepath.name)
    
    def validate_directory(self, directory: Path, recursive: bool = True) -> List[ValidationResult]:
        """
        Validate all files in a directory.
        
        Args:
            directory: Directory path to scan
            recursive: If True, scan recursively
            
        Returns:
            List of ValidationResult objects
        """
        results = []
        
        if recursive:
            for path in directory.rglob('*'):
                if path.is_file() and not self._is_excluded_path(path):
                    results.append(self.validate_file_path(path))
        else:
            for path in directory.iterdir():
                if path.is_file() and path.name not in self.EXCLUDED_FILES:
                    results.append(self.validate_file_path(path))
        
        return results
    
    def _is_excluded_path(self, path: Path) -> bool:
        """Check if path should be excluded from validation."""
        # Check if any parent directory is excluded
        for parent in path.parents:
            if parent.name in self.EXCLUDED_DIRS:
                return True
        
        # Check if filename is excluded
        if path.name in self.EXCLUDED_FILES:
            return True
        
        # Check if filename matches any excluded pattern
        for pattern in self.EXCLUDED_PATTERNS:
            if re.match(pattern, path.name):
                return True
        
        return False


def print_result(result: ValidationResult, verbose: bool = False) -> None:
    """Print validation result to console."""
    if result.valid:
        if verbose or result.warnings:
            print(f"✓ {result.filename}")
            for warning in result.warnings:
                print(f"  ⚠ Warning: {warning}")
    else:
        print(f"✗ {result.filename}")
        for error in result.errors:
            print(f"  ✗ Error: {error}")
        for warning in result.warnings:
            print(f"  ⚠ Warning: {warning}")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Validate filenames against AMPEL360 Space-T nomenclature standard',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s 00_AMPEL360_SPACET_PLUS_70_FHA_SB70_K02_SAF__propulsion_v01.md
  %(prog)s --check-all
  %(prog)s --check-dir ./AMPEL360-SPACE-T-PORTAL
  %(prog)s --check-all --strict
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
        '--strict',
        action='store_true',
        default=True,
        help='Enforce TYPE vocabulary (default: True)'
    )
    parser.add_argument(
        '--no-strict',
        dest='strict',
        action='store_false',
        help='Do not enforce TYPE vocabulary strictly'
    )
    parser.add_argument(
        '--verbose',
        '-v',
        action='store_true',
        help='Show all results including valid files'
    )
    
    args = parser.parse_args()
    
    # Validate arguments
    if not any([args.filename, args.check_all, args.check_dir]):
        parser.error('Must specify filename, --check-all, or --check-dir')
    
    validator = NomenclatureValidator(strict=args.strict)
    results = []
    
    try:
        if args.filename:
            # Validate single filename
            result = validator.validate_filename(args.filename)
            results = [result]
        elif args.check_dir:
            # Validate directory
            dir_path = Path(args.check_dir)
            if not dir_path.is_dir():
                print(f"Error: '{args.check_dir}' is not a directory", file=sys.stderr)
                return 2
            results = validator.validate_directory(dir_path, recursive=True)
        elif args.check_all:
            # Validate current directory
            results = validator.validate_directory(Path('.'), recursive=True)
        
        # Print results
        valid_count = 0
        invalid_count = 0
        
        for result in results:
            if result.valid:
                valid_count += 1
                if args.verbose:
                    print_result(result, verbose=True)
            else:
                invalid_count += 1
                print_result(result, verbose=args.verbose)
        
        # Print summary
        total = len(results)
        if total > 1 or args.check_all or args.check_dir:
            print(f"\n{'='*60}")
            print(f"Summary: {valid_count} valid, {invalid_count} invalid (total: {total})")
            print(f"{'='*60}")
        
        # Return appropriate exit code
        return 0 if invalid_count == 0 else 1
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
