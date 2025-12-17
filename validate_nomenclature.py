#!/usr/bin/env python3
"""
AMPEL360 Space-T Nomenclature Validator
========================================
Version: 5.0
Date: 2025-12-17
Standard: Nomenclature Standard v5.0 (Normative)

Validates filenames against the AMPEL360 Space-T nomenclature standard.
Config-driven validation using config/nomenclature/v5_0.yaml

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
import yaml
from pathlib import Path
from typing import List, Dict, Any, Optional
from dataclasses import dataclass


@dataclass
class ValidationResult:
    """Result of filename validation."""
    filename: str
    valid: bool
    errors: List[str]
    warnings: List[str]


class NomenclatureValidator:
    """Validates filenames against AMPEL360 Space-T nomenclature standard v5.0."""
    
    # Default config path
    DEFAULT_CONFIG_PATH = "config/nomenclature/v5_0.yaml"
    
    # Primary regex pattern (v5.0 format)
    PRIMARY_PATTERN = re.compile(
        r'^(?P<ata_root>(?:0[0-9]|[1-9][0-9]|10[0-9]|11[0-6]))_'
        r'(?P<project>AMPEL360)_'
        r'(?P<program>SPACET)_'
        r'(?P<variant>[A-Z0-9]+(?:-[A-Z0-9]+)*)_'
        r'(?P<block>[A-Z0-9]+)_'
        r'(?P<phase>(?:LC(?:0[1-9]|1[0-4])|SB(?:0[1-9]|[1-9][0-9])))_'
        r'(?P<knot_task>K(?:0[1-9]|1[0-4])(?:-T[0-9]{3})?)_'
        r'(?P<aor>[A-Z]+)__'
        r'(?P<subject>[a-z0-9]+(?:-[a-z0-9]+)*)_'
        r'(?P<type>[A-Z0-9]+)_'
        r'(?P<version>v[0-9]{2})_'
        r'(?P<status>[A-Z]+)'
        r'\.(?P<ext>[a-z0-9]{1,6})$'
    )
    
    # LC stage pattern (LC01-LC14)
    LC_PATTERN = re.compile(r'^LC(0[1-9]|1[0-4])$')
    
    # SB stage pattern (SB01-SB99)
    SB_PATTERN = re.compile(r'^SB(0[1-9]|[1-9][0-9])$')
    
    # KNOT_TASK pattern (K01-K14 with optional -T###)
    KNOT_TASK_PATTERN = re.compile(r'^K(0[1-9]|1[0-4])(?:-T[0-9]{3})?$')
    
    # VERSION format pattern
    VERSION_PATTERN = re.compile(r'^v\d{2}$')
    
    # Allowed PROJECT values (hard constraint)
    ALLOWED_PROJECTS = {'AMPEL360'}
    
    # Allowed PROGRAM values (fixed)
    ALLOWED_PROGRAMS = {'SPACET'}
    
    def __init__(self, config_path: Optional[str] = None, strict: bool = True):
        """
        Initialize validator.
        
        Args:
            config_path: Path to config YAML file (default: config/nomenclature/v5_0.yaml)
            strict: If True, enforce all vocabulary; if False, only warn
        """
        self.strict = strict
        self.config = self._load_config(config_path or self.DEFAULT_CONFIG_PATH)
        
        # Extract allowlists from config
        allowlists = self.config.get('allowlists', {})
        self.allowed_variants = set(allowlists.get('variants', []))
        self.allowed_blocks = set(allowlists.get('blocks', []))
        self.allowed_aors = set(allowlists.get('aors', []))
        self.allowed_types = set(allowlists.get('types', []))
        self.allowed_statuses = set(allowlists.get('statuses', []))
        self.allowed_extensions = set(allowlists.get('extensions', []))
        
        # Extract exemptions from config
        exemptions = self.config.get('exemptions', {})
        self.excluded_files = set(exemptions.get('files', []))
        self.excluded_dirs = set(exemptions.get('directories', []))
        self.excluded_patterns = exemptions.get('patterns', [])
        
        # Extract phase-block mapping
        self.phase_block_mapping = self.config.get('phase_block_mapping', {})
        
        # Extract KNOT governance
        knot_config = self.config.get('knots', {})
        allowed_range = knot_config.get('allowed_range', {})
        self.knot_min = allowed_range.get('min', 1)
        self.knot_max = allowed_range.get('max', 14)
    
    def _load_config(self, config_path: str) -> Dict[str, Any]:
        """Load configuration from YAML file."""
        try:
            path = Path(config_path)
            if not path.exists():
                # Try relative to script directory
                script_dir = Path(__file__).parent
                path = script_dir / config_path
            
            if not path.exists():
                print(f"Warning: Config file not found at {config_path}, using defaults", file=sys.stderr)
                return self._get_default_config()
            
            with open(path, 'r') as f:
                config = yaml.safe_load(f)
                return config or {}
        except Exception as e:
            print(f"Warning: Failed to load config from {config_path}: {e}, using defaults", file=sys.stderr)
            return self._get_default_config()
    
    def _get_default_config(self) -> Dict[str, Any]:
        """Return default configuration if config file is not available."""
        return {
            'allowlists': {
                'variants': ['PLUS'],
                'blocks': ['OPS', 'STR', 'PROP', 'AI', 'DATA', 'CERT', 'SAF', 'SW', 'HW', 'SYS', 'TEST', 'MRO', 'CIRC', 'ENRG', 'STOR', 'GEN'],
                'aors': ['CM', 'CERT', 'SAF', 'SE', 'OPS', 'DATA', 'AI', 'CY', 'TEST', 'MRO', 'SPACEPORT', 'PMO', 'QA', 'SEC', 'LEG', 'FIN', 'PROC'],
                'types': ['IDX', 'STD', 'PLAN', 'MIN', 'RPT', 'LOG', 'ACT', 'FHA', 'PSSA', 'SSA', 'FTA', 'ANA', 'REQ', 'DAL', 'TRC', 'CAT', 'LST', 'GLO', 'MAT', 'SCH', 'DIA', 'TAB', 'SPEC', 'PLN', 'PROC', 'MAN', 'API', 'CFG', 'JSON', 'YAML'],
                'statuses': ['TEMPLATE', 'DRAFT', 'ACTIVE', 'APPROVED', 'RELEASED', 'SUPERSEDED', 'ARCHIVED'],
                'extensions': ['md', 'yml', 'yaml', 'json', 'csv', 'svg', 'png', 'jpg', 'jpeg', 'pdf', 'drawio']
            },
            'exemptions': {
                'files': ['README.md', 'LICENSE', 'EXAMPLES.md', '.gitignore', '.gitattributes'],
                'directories': ['.git', '.github', 'node_modules', '__pycache__', 'templates', 'scripts', 'tools'],
                'patterns': ['generate_.*\\.py', 'validate_.*\\.py', '.*_Agent_Config\\.(yaml|json|yml)']
            },
            'knots': {
                'allowed_range': {'min': 1, 'max': 14}
            }
        }
    
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
        if filename in self.excluded_files:
            return ValidationResult(filename, True, [], [])
        
        # Check if filename matches any excluded pattern
        for pattern in self.excluded_patterns:
            if re.match(pattern, filename):
                return ValidationResult(filename, True, [], [])
        
        # Match against primary pattern
        match = self.PRIMARY_PATTERN.match(filename)
        
        if not match:
            errors.append(
                "Filename does not match required pattern (v5.0): "
                "[ATA_ROOT]_[PROJECT]_[PROGRAM]_[VARIANT]_[BLOCK]_[PHASE]_[KNOT_TASK]_[AoR]__[SUBJECT]_[TYPE]_[VERSION]_[STATUS].[EXT]"
            )
            return ValidationResult(filename, False, errors, warnings)
        
        # Extract components
        components = match.groupdict()
        ata_root = components['ata_root']
        project = components['project']
        program = components['program']
        variant = components['variant']
        block = components['block']
        phase = components['phase']
        knot_task = components['knot_task']
        aor = components['aor']
        subject = components['subject']
        type_code = components['type']
        version = components['version']
        status = components['status']
        ext = components['ext']
        
        # Validate ATA_ROOT padding
        ata_num = int(ata_root)
        if ata_num < 100 and len(ata_root) != 2:
            errors.append(f"ATA_ROOT '{ata_root}' must be 2 digits for values <100")
        elif ata_num >= 100 and len(ata_root) != 3:
            errors.append(f"ATA_ROOT '{ata_root}' must be 3 digits for values ≥100")
        
        # Validate PROJECT (hard constraint)
        if project not in self.ALLOWED_PROJECTS:
            errors.append(
                f"Invalid PROJECT '{project}': must be AMPEL360 (hard constraint)"
            )
        
        # Validate PROGRAM (fixed value)
        if program not in self.ALLOWED_PROGRAMS:
            errors.append(
                f"Invalid PROGRAM '{program}': must be SPACET"
            )
        
        # Validate VARIANT allowlist
        if variant not in self.allowed_variants:
            msg = f"Invalid VARIANT '{variant}': must be one of {sorted(self.allowed_variants)}"
            if self.strict:
                errors.append(msg)
            else:
                warnings.append(msg)
        
        # Validate BLOCK allowlist
        if block not in self.allowed_blocks:
            msg = f"Invalid BLOCK '{block}': must be one of {sorted(self.allowed_blocks)}"
            if self.strict:
                errors.append(msg)
            else:
                warnings.append(msg)
        
        # Validate PHASE format
        if not (self.LC_PATTERN.match(phase) or self.SB_PATTERN.match(phase)):
            errors.append(
                f"Invalid PHASE '{phase}': must be LC01-LC14 or SB01-SB99"
            )
        
        # Validate KNOT_TASK (strict K01-K14 governance)
        if not self.KNOT_TASK_PATTERN.match(knot_task):
            errors.append(
                f"Invalid KNOT_TASK '{knot_task}': must be K01-K14 (optionally with -T001 to -T999)"
            )
        else:
            # Extract knot number and validate range
            knot_match = re.match(r'^K(\d{2})', knot_task)
            if knot_match:
                knot_num = int(knot_match.group(1))
                if knot_num < self.knot_min or knot_num > self.knot_max:
                    errors.append(
                        f"Invalid KNOT number in '{knot_task}': must be K{self.knot_min:02d}-K{self.knot_max:02d} (strict governance)"
                    )
        
        # Validate AoR allowlist
        if aor not in self.allowed_aors:
            errors.append(
                f"Invalid AoR '{aor}': must be one of {sorted(self.allowed_aors)}"
            )
        
        # Validate TYPE allowlist
        if type_code not in self.allowed_types:
            msg = f"Invalid TYPE '{type_code}': must be one of {sorted(self.allowed_types)}"
            if self.strict:
                errors.append(msg)
            else:
                warnings.append(msg)
        
        # Validate STATUS allowlist
        if status not in self.allowed_statuses:
            errors.append(
                f"Invalid STATUS '{status}': must be one of {sorted(self.allowed_statuses)}"
            )
        
        # Validate EXT allowlist
        if ext not in self.allowed_extensions:
            msg = f"Invalid EXT '{ext}': must be one of {sorted(self.allowed_extensions)}"
            if self.strict:
                errors.append(msg)
            else:
                warnings.append(msg)
        
        # Check for redundancy in SUBJECT
        subject_lower = subject.lower()
        type_lower = type_code.lower()
        if type_lower in subject_lower and type_lower != subject_lower:
            warnings.append(
                f"SUBJECT '{subject}' may redundantly include TYPE '{type_code}'"
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
                if path.is_file() and path.name not in self.excluded_files:
                    results.append(self.validate_file_path(path))
        
        return results
    
    def _is_excluded_path(self, path: Path) -> bool:
        """Check if path should be excluded from validation."""
        # Check if any parent directory is excluded
        for parent in path.parents:
            if parent.name in self.excluded_dirs:
                return True
        
        # Check if filename is excluded
        if path.name in self.excluded_files:
            return True
        
        # Check if filename matches any excluded pattern
        for pattern in self.excluded_patterns:
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
        description='Validate filenames against AMPEL360 Space-T nomenclature standard v5.0',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s 27_AMPEL360_SPACET_PLUS_OPS_LC03_K06_SE__thermal-loop_STD_v01_ACTIVE.md
  %(prog)s --check-all
  %(prog)s --check-dir ./docs
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
        '--config',
        metavar='CONFIG',
        help='Path to config YAML file (default: config/nomenclature/v5_0.yaml)'
    )
    parser.add_argument(
        '--strict',
        action='store_true',
        default=True,
        help='Enforce all vocabularies strictly (default: True)'
    )
    parser.add_argument(
        '--no-strict',
        dest='strict',
        action='store_false',
        help='Do not enforce vocabularies strictly (only warn)'
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
    
    validator = NomenclatureValidator(config_path=args.config, strict=args.strict)
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
        import traceback
        traceback.print_exc()
        return 2


if __name__ == '__main__':
    sys.exit(main())
