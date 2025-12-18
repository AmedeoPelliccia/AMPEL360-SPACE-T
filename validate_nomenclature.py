#!/usr/bin/env python3
"""
AMPEL360 Space-T Nomenclature Validator
========================================
Version: 6.0
Date: 2025-12-17
Standard: Nomenclature Standard v5.0 and v6.0 (R1.0) (Normative)

Validates filenames against the AMPEL360 Space-T nomenclature standard.
Config-driven validation using config/nomenclature/v5_0.yaml or v6_0.yaml

Usage:
    python validate_nomenclature.py <filename>
    python validate_nomenclature.py --standard v6.0 --check-all
    python validate_nomenclature.py --standard v6.0 --mode warn --check-all
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
    """Validates filenames against AMPEL360 Space-T nomenclature standard v5.0 or v6.0."""
    
    # Default config path
    DEFAULT_CONFIG_PATH = "config/nomenclature/v5_0.yaml"
    
    # Primary regex pattern (v5.0 format)
    PRIMARY_PATTERN_V5 = re.compile(
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
    
    # Primary regex pattern (v6.0 format)
    # VERSION supports optional 2-digit iteration: (PLUS|PLUSULTRA)[0-9]{2}?
    PRIMARY_PATTERN_V6 = re.compile(
        r'^(?P<ata_root>(?:0[0-9]|[1-9][0-9]|10[0-9]|11[0-6]))_'
        r'(?P<project>AMPEL360)_'
        r'(?P<program>SPACET)_'
        r'(?P<family>Q[0-9]{2,3})_'
        r'(?P<variant>[A-Z0-9]+)_'
        r'(?P<version>(?:PLUS|PLUSULTRA)(?:[0-9]{2})?)_'  # R1.0: optional 2-digit iteration
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
    
    # LC stage pattern (LC01-LC14)
    LC_PATTERN = re.compile(r'^LC(0[1-9]|1[0-4])$')
    
    # SB stage pattern (SB01-SB99)
    SB_PATTERN = re.compile(r'^SB(0[1-9]|[1-9][0-9])$')
    
    # KNOT_TASK pattern (K01-K14 with optional -T###)
    KNOT_TASK_PATTERN = re.compile(r'^K(0[1-9]|1[0-4])(?:-T[0-9]{3})?$')
    
    # VERSION format pattern (v5.0)
    VERSION_PATTERN_V5 = re.compile(r'^v\d{2}$')
    
    # ISSUE-REVISION pattern (v6.0)
    ISSUE_REVISION_PATTERN = re.compile(r'^I[0-9]{2}-R[0-9]{2}$')
    
    # FAMILY pattern (v6.0)
    FAMILY_PATTERN = re.compile(r'^Q[0-9]{2,3}$')
    
    # MODEL pattern (v6.0)
    MODEL_PATTERN = re.compile(r'^[A-Z]{2}$')
    
    # BLOCK pattern (v6.0 - B## format: B00, B10, B20, ..., B90)
    BLOCK_PATTERN = re.compile(r'^B[0-9]0$')
    
    # Allowed PROJECT values (hard constraint)
    ALLOWED_PROJECTS = {'AMPEL360'}
    
    # Allowed PROGRAM values (fixed)
    ALLOWED_PROGRAMS = {'SPACET'}
    
    def __init__(self, config_path: Optional[str] = None, strict: bool = True, 
                 standard: str = "v5.0", mode: str = "block"):
        """
        Initialize validator.
        
        Args:
            config_path: Path to config YAML file (default: config/nomenclature/v5_0.yaml or v6_0.yaml)
            strict: If True, enforce all vocabulary; if False, only warn
            standard: Standard version to validate against ("v5.0" or "v6.0")
            mode: Validation mode ("warn", "report", "block")
        """
        self.strict = strict
        self.standard = standard
        self.mode = mode
        
        # Determine config path based on standard
        if config_path is None:
            if standard == "v6.0":
                config_path = "config/nomenclature/v6_0.yaml"
            else:
                config_path = self.DEFAULT_CONFIG_PATH
        
        self.config = self._load_config(config_path)
        
        # Extract allowlists from config
        allowlists = self.config.get('allowlists', {})
        self.allowed_variants = set(allowlists.get('variants', []))
        self.allowed_blocks = set(allowlists.get('blocks', []))
        self.allowed_aors = set(allowlists.get('aors', []))
        self.allowed_types = set(allowlists.get('types', []))
        self.allowed_statuses = set(allowlists.get('statuses', []))
        self.allowed_extensions = set(allowlists.get('extensions', []))
        
        # v6.0 specific allowlists
        if standard == "v6.0":
            self.allowed_families = set(allowlists.get('families', []))
            self.allowed_version_brands = set(allowlists.get('version_brand', []))
            self.allowed_models = set(allowlists.get('models', []))
            
            # Load patterns and limits from config (R1.0 FINAL LOCK)
            patterns = self.config.get('patterns', {})
            self.version_pattern_str = patterns.get('version', r'^(PLUS|PLUSULTRA)([0-9]{2})?$')
            self.subject_prefix_for_variant = patterns.get('subject_prefix_for_variant', {})
            
            limits = self.config.get('limits', {})
            self.filename_max_len = limits.get('filename_max_len', 180)
            token_limits = limits.get('token_max_len', {})
            self.block_max_len = token_limits.get('block', 3)
            self.subject_max_len = token_limits.get('subject', 60)
            self.type_max_len = token_limits.get('type', 8)
            self.aor_max_len = token_limits.get('aor', 10)
            
            # Load ATA_PARTITION_MATRIX for v6.0 (Phase 2)
            optins_config = self.config.get('optins_framework', {})
            matrix_path = optins_config.get('ata_partition_matrix', 'config/nomenclature/ATA_PARTITION_MATRIX.yaml')
            self.ata_partition_matrix = self._load_ata_partition_matrix(matrix_path)
            self.enforce_ata_block_mapping = optins_config.get('enforcement', {}).get('validate_ata_block_mapping', True)
        
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
    
    def _load_ata_partition_matrix(self, matrix_path: str) -> Dict[str, Any]:
        """Load ATA_PARTITION_MATRIX from YAML file."""
        try:
            path = Path(matrix_path)
            if not path.exists():
                # Try relative to script directory
                script_dir = Path(__file__).parent
                path = script_dir / matrix_path
            
            if not path.exists():
                print(f"Warning: ATA_PARTITION_MATRIX not found at {matrix_path}, ATA+BLOCK validation disabled", file=sys.stderr)
                return {}
            
            with open(path, 'r') as f:
                matrix = yaml.safe_load(f)
                return matrix or {}
        except Exception as e:
            print(f"Warning: Failed to load ATA_PARTITION_MATRIX from {matrix_path}: {e}, ATA+BLOCK validation disabled", file=sys.stderr)
            return {}
    
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
        
        # Match against primary pattern based on standard version
        if self.standard == "v6.0":
            match = self.PRIMARY_PATTERN_V6.match(filename)
            pattern_desc = "[ATA_ROOT]_[PROJECT]_[PROGRAM]_[FAMILY]_[VARIANT]_[VERSION]_[MODEL]_[BLOCK]_[PHASE]_[KNOT_TASK]_[AoR]__[SUBJECT]_[TYPE]_[ISSUE-REVISION]_[STATUS].[EXT]"
        else:
            match = self.PRIMARY_PATTERN_V5.match(filename)
            pattern_desc = "[ATA_ROOT]_[PROJECT]_[PROGRAM]_[VARIANT]_[BLOCK]_[PHASE]_[KNOT_TASK]_[AoR]__[SUBJECT]_[TYPE]_[VERSION]_[STATUS].[EXT]"
        
        if not match:
            errors.append(
                f"Filename does not match required pattern ({self.standard}): {pattern_desc}"
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
        status = components['status']
        ext = components['ext']
        
        # v6.0 specific fields
        if self.standard == "v6.0":
            family = components.get('family')
            version = components.get('version')
            model = components.get('model')
            issue_revision = components.get('issue_revision')
        else:
            version = components.get('version')  # vNN format in v5.0
        
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
        
        # v6.0 specific validations
        if self.standard == "v6.0":
            # Validate FAMILY
            if family not in self.allowed_families:
                msg = f"Invalid FAMILY '{family}': must be one of {sorted(self.allowed_families)}"
                if self.strict:
                    errors.append(msg)
                else:
                    warnings.append(msg)
            
            # Validate VERSION (R1.0 FINAL LOCK: brand + optional 2-digit iteration)
            # The regex pattern already enforces the brand roots (PLUS|PLUSULTRA) and optional 2-digit iteration
            version_pattern = re.compile(self.version_pattern_str)
            if not version_pattern.match(version):
                # Extract brand roots for error message
                brand_list = ', '.join(sorted(self.allowed_version_brands))
                errors.append(
                    f"Invalid VERSION '{version}': must be a brand root ({brand_list}) "
                    f"optionally followed by 2 digits (e.g., PLUS, PLUS01, PLUSULTRA02)"
                )
            
            # Validate MODEL
            if model not in self.allowed_models:
                msg = f"Invalid MODEL '{model}': must be one of {sorted(self.allowed_models)}"
                if self.strict:
                    errors.append(msg)
                else:
                    warnings.append(msg)
            
            # Validate ISSUE-REVISION format
            if not self.ISSUE_REVISION_PATTERN.match(issue_revision):
                errors.append(
                    f"Invalid ISSUE-REVISION '{issue_revision}': must be I##-R## format (e.g., I01-R01)"
                )
            
            # R1.0 FINAL LOCK: Conditional SUBJECT prefix validation
            if variant in self.subject_prefix_for_variant:
                required_prefix_pattern = self.subject_prefix_for_variant[variant]
                if not re.match(required_prefix_pattern, subject):
                    if variant == "CUST":
                        errors.append(
                            f"VARIANT '{variant}' requires SUBJECT to start with 'cust-<custcode>-' "
                            f"where custcode is 2-12 alphanumeric chars (e.g., cust-airbus-...)"
                        )
                    elif variant == "MSN":
                        errors.append(
                            f"VARIANT '{variant}' requires SUBJECT to start with 'msn-<serial>-' "
                            f"where serial is 3-6 digits (e.g., msn-000123-...)"
                        )
                    else:
                        errors.append(
                            f"VARIANT '{variant}' requires SUBJECT to match prefix pattern: {required_prefix_pattern}"
                        )
            
            # R1.0 FINAL LOCK: Length limits validation
            filename_len = len(filename)
            if filename_len > self.filename_max_len:
                errors.append(
                    f"Filename length ({filename_len}) exceeds maximum ({self.filename_max_len} chars)"
                )
            
            if len(block) > self.block_max_len:
                errors.append(
                    f"BLOCK '{block}' length ({len(block)}) exceeds maximum ({self.block_max_len} chars)"
                )
            
            if len(subject) > self.subject_max_len:
                errors.append(
                    f"SUBJECT '{subject}' length ({len(subject)}) exceeds maximum ({self.subject_max_len} chars)"
                )
            
            if len(type_code) > self.type_max_len:
                errors.append(
                    f"TYPE '{type_code}' length ({len(type_code)}) exceeds maximum ({self.type_max_len} chars)"
                )
            
            if len(aor) > self.aor_max_len:
                errors.append(
                    f"AoR '{aor}' length ({len(aor)}) exceeds maximum ({self.aor_max_len} chars)"
                )
        else:
            # v5.0 VERSION validation (vNN format)
            if not self.VERSION_PATTERN_V5.match(version):
                errors.append(f"VERSION '{version}' must be 'vNN' with exactly 2 digits")
        
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
        
        # v6.0: Validate B## pattern format (Phase 2)
        if self.standard == "v6.0":
            if not self.BLOCK_PATTERN.match(block):
                errors.append(
                    f"Invalid BLOCK format '{block}': must be B## format (B00, B10, B20, ..., B90)"
                )
            
            # Validate ATA_ROOT + BLOCK combination against ATA_PARTITION_MATRIX (Phase 2)
            if self.enforce_ata_block_mapping and self.ata_partition_matrix:
                ata_blocks = self._get_valid_blocks_for_ata(ata_root)
                if ata_blocks is not None and block not in ata_blocks:
                    errors.append(
                        f"Invalid BLOCK '{block}' for ATA_ROOT '{ata_root}': "
                        f"must be one of {sorted(ata_blocks)} (per ATA_PARTITION_MATRIX)"
                    )
        
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
        
        # Determine validity based on mode
        if self.mode == "warn" or self.mode == "report":
            # In warn/report mode, always return valid=True but include errors as warnings
            valid = True
            if errors:
                warnings.extend(errors)
                errors = []
        else:
            # In block mode, fail on errors
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
    
    def _get_valid_blocks_for_ata(self, ata_root: str) -> Optional[List[str]]:
        """
        Get valid BLOCK values for the given ATA_ROOT from ATA_PARTITION_MATRIX.
        
        Business Rule: B00 (GENERAL) is universally valid for all ATA roots as it
        represents the universal baseline that applies to all systems. This is
        explicitly defined in the ATA_PARTITION_MATRIX as implicit/universal.
        
        Args:
            ata_root: ATA chapter code (e.g., "00", "27", "115")
            
        Returns:
            List of valid BLOCK codes (e.g., ["B00", "B10", "B20", "B30"]) or None if not found.
            B00 is always included as it is universally valid per OPTINS Framework.
        """
        if not self.ata_partition_matrix:
            return None
        
        # Construct ATA key (e.g., "ATA_00", "ATA_27", "ATA_115")
        ata_key = f"ATA_{ata_root}"
        
        # Search across all axes (o_axis, i_axis, t_axis, n_axis, s_axis)
        for axis_name in ['o_axis', 'i_axis', 't_axis', 'n_axis', 's_axis']:
            axis = self.ata_partition_matrix.get(axis_name, {})
            if ata_key in axis:
                ata_config = axis[ata_key]
                blocks = ata_config.get('blocks', [])
                # Work on a copy to avoid mutating or exposing the underlying config list
                merged_blocks = list(blocks)
                # B00 is always implicit/valid per OPTINS Framework (universal baseline)
                if 'B00' not in merged_blocks:
                    merged_blocks.insert(0, 'B00')
                return merged_blocks
        
        # If ATA not found in matrix, return None (no validation)
        return None


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
        description='Validate filenames against AMPEL360 Space-T nomenclature standard v5.0 or v6.0 (R1.0)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # v5.0 validation
  %(prog)s 27_AMPEL360_SPACET_PLUS_OPS_LC03_K06_SE__thermal-loop_STD_v01_ACTIVE.md
  %(prog)s --check-all
  
  # v6.0 validation (R1.0 FINAL LOCK)
  %(prog)s --standard v6.0 --check-all
  %(prog)s --standard v6.0 --mode warn --check-all
  %(prog)s --standard v6.0 --mode block --check-all
  
  # v6.0 examples
  %(prog)s --standard v6.0 27_AMPEL360_SPACET_Q10_GEN_PLUS_BB_OPS_LC03_K06_SE__thermal-loop_STD_I01-R01_ACTIVE.md
  %(prog)s --standard v6.0 27_AMPEL360_SPACET_Q10_CUST_PLUS01_SW_OPS_LC03_K06_SE__cust-airbus-thermal_STD_I01-R01_DRAFT.md
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
        '--standard',
        choices=['v5.0', 'v6.0'],
        default='v5.0',
        help='Nomenclature standard version to validate against (default: v5.0)'
    )
    parser.add_argument(
        '--mode',
        choices=['warn', 'report', 'block'],
        default='block',
        help='Validation mode: warn (no fail), report (detailed), block (fail on error) (default: block)'
    )
    parser.add_argument(
        '--config',
        metavar='CONFIG',
        help='Path to config YAML file (default: auto-detected based on --standard)'
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
    
    validator = NomenclatureValidator(
        config_path=args.config, 
        strict=args.strict,
        standard=args.standard,
        mode=args.mode
    )
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
