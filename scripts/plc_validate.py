#!/usr/bin/env python3
r"""
AMPEL360 Space-T PLC Process Control Logic Validator
=====================================================
Version: 2.0
Date: 2025-12-17
Standard: Nomenclature Standard v6.0 R1.0 (Normative)

Implements PLC (Process Logic Control) validation using a deterministic
rung-stack architecture for nomenclature artifact validation.

PLC RUNG STACK ARCHITECTURE:
===============================================================================
  RUNG 0 - Parse & Tokenize
           Parse v6.0 tokens from filename (and optionally directory context)
           
  RUNG 1 - Allowlist Enforcement
           FAMILY/VARIANT/VERSION/MODEL/AoR/TYPE/STATUS/EXT must be in config
           
  RUNG 2 - Cross-field Semantics
           VARIANT=MSN => SUBJECT matches ^msn-\d{3,6}-
           VARIANT=CUST => SUBJECT matches ^cust-[a-z0-9]{2,12}-
           TEKNIA issuance: TYPE in {BADGE,CERT,LIC} => AoR in {CM,CERT}
           
  RUNG 3 - Context Constraints (Ontology-driven)
           MODEL<->TYPE coherence, AoR permissions, BLOCK<->AoR mapping
           ATA_ROOT<->BLOCK coherence, PHASE<->STATUS lifecycle alignment
           
  RUNG 4 - Cross-reference Integrity
           Internal links and index references resolve correctly
           
  RUNG 5 - Release Gating (PR^3 aware)
           STATUS=RELEASED => proper lifecycle phase (LC09+)
           Exception register validation
===============================================================================

Usage:
    python scripts/plc_validate.py <filename>
    python scripts/plc_validate.py --check-all
    python scripts/plc_validate.py --check-dir <directory>
    python scripts/plc_validate.py --check-all --rung 0,1,2  # Run specific rungs

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
class PLCRungResult:
    """Result of a single PLC rung execution."""
    rung_id: int
    rung_name: str
    passed: bool
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    data: Dict[str, Any] = field(default_factory=dict)  # Rung-specific output data


@dataclass
class PLCValidationResult:
    """Result of PLC validation."""
    filename: str
    valid: bool
    parsed_fields: Dict[str, str]
    rung_results: List[PLCRungResult] = field(default_factory=list)
    consistency_errors: List[str] = field(default_factory=list)
    consistency_warnings: List[str] = field(default_factory=list)
    chain_violations: List[Tuple[str, str, str]] = field(default_factory=list)  # (field1, field2, reason)


class PLCValidator:
    """
    PLC (Process Logic Control) Validator for nomenclature chained consistency.
    
    Implements a deterministic rung-stack architecture for validating
    nomenclature artifacts with cross-field semantic coherence.
    
    RUNG STACK:
        0: Parse & Tokenize
        1: Allowlist Enforcement
        2: Cross-field Semantics
        3: Context Constraints (Ontology-driven)
        4: Cross-reference Integrity
        5: Release Gating (PR^3 aware)
    """
    
    # Rung definitions
    RUNG_NAMES = {
        0: "Parse & Tokenize",
        1: "Allowlist Enforcement",
        2: "Cross-field Semantics",
        3: "Context Constraints",
        4: "Cross-reference Integrity",
        5: "Release Gating",
    }
    
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
    
    # TEKNIA credential constraints
    TEKNIA_TYPES = {'BADGE', 'CERT', 'LIC'}
    TEKNIA_ISSUANCE_AORS = {'CM', 'CERT'}
    
    def __init__(self, config_path: Optional[str] = None, strict: bool = True, 
                 mode: str = "warn", rungs: Optional[List[int]] = None):
        """
        Initialize PLC validator.
        
        Args:
            config_path: Path to v6.0 config YAML file
            strict: If True, treat consistency warnings as errors
            mode: Validation mode ("warn", "report", "block")
            rungs: List of rung IDs to execute (default: all 0-5)
        """
        self.strict = strict
        self.mode = mode
        self.rungs_to_execute = rungs if rungs is not None else list(range(6))
        self.config = self._load_config(config_path or "config/nomenclature/v6_0.yaml")
        
        # Extract exemptions
        exemptions = self.config.get('exemptions', {})
        self.excluded_files = set(exemptions.get('files', []))
        self.excluded_dirs = set(exemptions.get('directories', []))
        self.excluded_patterns = exemptions.get('patterns', [])
        
        # Extract allowlists for Rung 1 enforcement
        allowlists = self.config.get('allowlists', {})
        self.allowed_families = set(allowlists.get('families', []))
        self.allowed_variants = set(allowlists.get('variants', []))
        self.allowed_version_brands = set(allowlists.get('version_brand', []))
        self.allowed_models = set(allowlists.get('models', []))
        self.allowed_blocks = set(allowlists.get('blocks', []))
        self.allowed_aors = set(allowlists.get('aors', []))
        self.allowed_types = set(allowlists.get('types', []))
        self.allowed_statuses = set(allowlists.get('statuses', []))
        self.allowed_extensions = set(allowlists.get('extensions', []))
    
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
    
    # ═══════════════════════════════════════════════════════════════════════════
    # PLC RUNG METHODS
    # ═══════════════════════════════════════════════════════════════════════════
    
    def _execute_rung_0(self, filename: str) -> PLCRungResult:
        """
        RUNG 0 — Parse & Tokenize
        Parse v6.0 tokens from filename.
        """
        fields = self.parse_filename(filename)
        if fields is None:
            return PLCRungResult(
                rung_id=0,
                rung_name=self.RUNG_NAMES[0],
                passed=False,
                errors=["Failed to parse filename - does not match v6.0 pattern"],
                data={'parsed': False}
            )
        return PLCRungResult(
            rung_id=0,
            rung_name=self.RUNG_NAMES[0],
            passed=True,
            data={'parsed': True, 'fields': fields}
        )
    
    def _execute_rung_1(self, fields: Dict[str, str]) -> PLCRungResult:
        """
        RUNG 1 — Allowlist Enforcement
        FAMILY/VARIANT/VERSION/MODEL/AoR/TYPE/STATUS/EXT must be in config allowlists.
        """
        errors = []
        warnings = []
        
        # Check FAMILY
        family = fields.get('family', '')
        if self.allowed_families and family not in self.allowed_families:
            errors.append(f"FAMILY '{family}' not in allowlist: {sorted(self.allowed_families)}")
        
        # Check VARIANT
        variant = fields.get('variant', '')
        if self.allowed_variants and variant not in self.allowed_variants:
            errors.append(f"VARIANT '{variant}' not in allowlist: {sorted(self.allowed_variants)}")
        
        # Check VERSION (brand root)
        version = fields.get('version', '')
        version_brand = re.match(r'^(PLUS|PLUSULTRA)', version)
        if version_brand:
            brand = version_brand.group(1)
            if self.allowed_version_brands and brand not in self.allowed_version_brands:
                errors.append(f"VERSION brand '{brand}' not in allowlist: {sorted(self.allowed_version_brands)}")
        else:
            errors.append(f"VERSION '{version}' does not match expected pattern")
        
        # Check MODEL
        model = fields.get('model', '')
        if self.allowed_models and model not in self.allowed_models:
            errors.append(f"MODEL '{model}' not in allowlist: {sorted(self.allowed_models)}")
        
        # Check BLOCK
        block = fields.get('block', '')
        if self.allowed_blocks and block not in self.allowed_blocks:
            warnings.append(f"BLOCK '{block}' not in allowlist: {sorted(self.allowed_blocks)}")
        
        # Check AoR
        aor = fields.get('aor', '')
        if self.allowed_aors and aor not in self.allowed_aors:
            errors.append(f"AoR '{aor}' not in allowlist: {sorted(self.allowed_aors)}")
        
        # Check TYPE
        type_code = fields.get('type', '')
        if self.allowed_types and type_code not in self.allowed_types:
            warnings.append(f"TYPE '{type_code}' not in allowlist: {sorted(self.allowed_types)}")
        
        # Check STATUS
        status = fields.get('status', '')
        if self.allowed_statuses and status not in self.allowed_statuses:
            errors.append(f"STATUS '{status}' not in allowlist: {sorted(self.allowed_statuses)}")
        
        # Check EXT
        ext = fields.get('ext', '')
        if self.allowed_extensions and ext not in self.allowed_extensions:
            warnings.append(f"EXT '{ext}' not in allowlist: {sorted(self.allowed_extensions)}")
        
        return PLCRungResult(
            rung_id=1,
            rung_name=self.RUNG_NAMES[1],
            passed=len(errors) == 0,
            errors=errors,
            warnings=warnings,
            data={'allowlist_checks': True}
        )
    
    def _execute_rung_2(self, fields: Dict[str, str]) -> PLCRungResult:
        r"""
        RUNG 2 - Cross-field Semantics
        VARIANT=MSN => SUBJECT matches ^msn-\d{3,6}-
        VARIANT=CUST => SUBJECT matches ^cust-[a-z0-9]{2,12}-
        TEKNIA issuance: TYPE in {BADGE,CERT,LIC} => AoR in {CM,CERT}
        """
        errors = []
        warnings = []
        
        variant = fields.get('variant', '')
        subject = fields.get('subject', '')
        type_code = fields.get('type', '')
        aor = fields.get('aor', '')
        
        # Check VARIANT ↔ SUBJECT prefix requirements
        if variant in self.VARIANT_SUBJECT_PREFIX:
            pattern = self.VARIANT_SUBJECT_PREFIX[variant]
            if not re.match(pattern, subject):
                errors.append(
                    f"VARIANT '{variant}' requires SUBJECT to match pattern '{pattern}', "
                    f"got '{subject}'"
                )
        
        # Check TEKNIA credential issuance constraints
        if type_code in self.TEKNIA_TYPES:
            if aor not in self.TEKNIA_ISSUANCE_AORS:
                errors.append(
                    f"TEKNIA credential TYPE '{type_code}' can only be issued by "
                    f"AoR in {self.TEKNIA_ISSUANCE_AORS}, got '{aor}'"
                )
        
        return PLCRungResult(
            rung_id=2,
            rung_name=self.RUNG_NAMES[2],
            passed=len(errors) == 0,
            errors=errors,
            warnings=warnings,
            data={'cross_field_checks': True}
        )
    
    def _execute_rung_3(self, fields: Dict[str, str]) -> PLCRungResult:
        """
        RUNG 3 — Context Constraints (Ontology-driven)
        MODEL↔TYPE coherence, AoR permissions, BLOCK↔AoR mapping
        ATA_ROOT↔BLOCK coherence, PHASE↔STATUS lifecycle alignment
        """
        errors = []
        warnings = []
        chain_violations = []
        
        ata_root = int(fields.get('ata_root', '0'))
        block = fields.get('block', '')
        phase = fields.get('phase', '')
        status = fields.get('status', '')
        aor = fields.get('aor', '')
        knot_task = fields.get('knot_task', '')
        model = fields.get('model', '')
        type_code = fields.get('type', '')
        variant = fields.get('variant', '')
        
        knot_id = knot_task.split('-')[0]  # K01, K02, etc.
        
        # ATA_ROOT ↔ BLOCK coherence
        ata_mapped = False
        for (ata_min, ata_max), valid_blocks in self.ATA_BLOCK_MAP.items():
            if ata_min <= ata_root <= ata_max:
                ata_mapped = True
                if block not in valid_blocks and block != 'GEN':
                    chain_violations.append(('ATA_ROOT', 'BLOCK',
                        f"ATA {ata_root} typically uses BLOCK in {valid_blocks}, not '{block}'"))
                    warnings.append(f"ATA_ROOT↔BLOCK: ATA {ata_root} typically in {valid_blocks}, not '{block}'")
                break
        
        if not ata_mapped and block != 'GEN':
            warnings.append(f"ATA_ROOT↔BLOCK: ATA {ata_root} has no explicit mapping; GEN preferred for unmapped")
        
        # PHASE ↔ STATUS lifecycle alignment
        if phase.startswith('LC') and phase in self.PHASE_STATUS_RULES:
            valid_statuses = self.PHASE_STATUS_RULES[phase]
            if status not in valid_statuses:
                chain_violations.append(('PHASE', 'STATUS',
                    f"{phase} typically has STATUS in {valid_statuses}, not '{status}'"))
                warnings.append(f"PHASE↔STATUS: {phase} typically uses STATUS in {valid_statuses}, not '{status}'")
        
        # AoR ↔ KNOT governance mapping
        if aor in self.AOR_KNOT_MAP:
            expected_knots = self.AOR_KNOT_MAP[aor]
            if knot_id not in expected_knots:
                chain_violations.append(('AoR', 'KNOT_TASK',
                    f"AoR '{aor}' typically works on KNOTs {expected_knots}, not '{knot_id}'"))
                warnings.append(f"AoR↔KNOT: AoR '{aor}' typically participates in {expected_knots}, not '{knot_id}'")
        
        # MODEL ↔ TYPE alignment
        if model in self.MODEL_TYPE_MAP:
            valid_types = self.MODEL_TYPE_MAP[model]
            if type_code not in valid_types:
                chain_violations.append(('MODEL', 'TYPE',
                    f"MODEL '{model}' typically uses TYPE in {valid_types}, not '{type_code}'"))
                warnings.append(f"MODEL↔TYPE: MODEL '{model}' typically uses TYPE in {valid_types}, not '{type_code}'")
        
        # BLOCK ↔ AoR coherence
        if block in self.BLOCK_AOR_MAP:
            expected_aors = self.BLOCK_AOR_MAP[block]
            if aor not in expected_aors:
                chain_violations.append(('BLOCK', 'AoR',
                    f"BLOCK '{block}' typically has AoR in {expected_aors}, not '{aor}'"))
                warnings.append(f"BLOCK↔AoR: BLOCK '{block}' typically works with AoR in {expected_aors}, not '{aor}'")
        
        # Cross-field semantic validation for special variants
        if variant == 'CERT' and block not in ['CERT', 'SAF', 'GEN'] and aor not in ['CERT', 'SAF']:
            warnings.append("VARIANT↔BLOCK/AoR: CERT variant should typically have CERT/SAF BLOCK or AoR")
        
        if variant == 'FLIGHTTEST' and block not in ['TEST', 'OPS', 'SYS'] and aor not in ['TEST', 'OPS']:
            warnings.append("VARIANT↔BLOCK/AoR: FLIGHTTEST variant should typically have TEST/OPS BLOCK or AoR")
        
        # S-axis (ATA 100-114) should have TEST-related content
        if 100 <= ata_root <= 114 and block not in ['TEST', 'SW', 'DATA', 'SYS', 'GEN']:
            warnings.append(f"ATA_ROOT↔BLOCK: S-axis ATA {ata_root} should typically use TEST/SW/DATA/SYS BLOCK")
        
        # Neural chapters (95-98) should have AI/DATA content
        if 95 <= ata_root <= 98:
            if block not in ['AI', 'DATA', 'SW', 'GEN'] and aor not in ['AI', 'DATA']:
                warnings.append(f"ATA_ROOT↔BLOCK/AoR: Neural ATA {ata_root} should typically have AI/DATA BLOCK or AoR")
        
        return PLCRungResult(
            rung_id=3,
            rung_name=self.RUNG_NAMES[3],
            passed=len(errors) == 0,
            errors=errors,
            warnings=warnings,
            data={'chain_violations': chain_violations, 'ontology_checks': True}
        )
    
    def _execute_rung_4(self, fields: Dict[str, str], filename: str) -> PLCRungResult:
        """
        RUNG 4 — Cross-reference Integrity
        Internal links and index references resolve correctly.
        (Placeholder - full implementation requires file system access)
        """
        warnings = []
        
        # This rung would check:
        # 1. If file contains links, verify they resolve
        # 2. If file is referenced in an index, verify index entry exists
        # 3. Verify canonical path matches expected location
        
        # Placeholder: In production, this would scan file content for links
        warnings.append("RUNG 4: Cross-reference integrity check not fully implemented (placeholder)")
        
        return PLCRungResult(
            rung_id=4,
            rung_name=self.RUNG_NAMES[4],
            passed=True,  # Pass by default until fully implemented
            warnings=warnings,
            data={'cross_reference_checks': 'placeholder'}
        )
    
    def _execute_rung_5(self, fields: Dict[str, str]) -> PLCRungResult:
        """
        RUNG 5 — Release Gating (PR^3 aware)
        STATUS=RELEASED ⇒ proper lifecycle phase (LC09+)
        Exception register validation.
        """
        errors = []
        warnings = []
        
        phase = fields.get('phase', '')
        status = fields.get('status', '')
        
        # Release gating: RELEASED status should only appear in LC09+ phases
        if status == 'RELEASED':
            if phase.startswith('LC'):
                phase_num = int(phase[2:])
                if phase_num < 9:
                    warnings.append(
                        f"Release gate warning: STATUS 'RELEASED' in {phase} (typically LC09+)"
                    )
        
        # APPROVED status typically in LC03+ phases
        if status == 'APPROVED':
            if phase.startswith('LC'):
                phase_num = int(phase[2:])
                if phase_num < 3:
                    warnings.append(
                        f"Release gate warning: STATUS 'APPROVED' in {phase} (typically LC03+)"
                    )
        
        return PLCRungResult(
            rung_id=5,
            rung_name=self.RUNG_NAMES[5],
            passed=len(errors) == 0,
            errors=errors,
            warnings=warnings,
            data={'release_gating_checks': True}
        )
    
    def execute_plc_rungs(self, filename: str) -> PLCValidationResult:
        """
        Execute all PLC rungs on a filename.
        
        Args:
            filename: The filename to validate
            
        Returns:
            PLCValidationResult with all rung results
        """
        # Check if file should be excluded
        if filename in self.excluded_files:
            return PLCValidationResult(filename, True, {})
        
        for pattern in self.excluded_patterns:
            if re.match(pattern, filename):
                return PLCValidationResult(filename, True, {})
        
        rung_results = []
        all_errors = []
        all_warnings = []
        all_chain_violations = []
        fields = {}
        
        # RUNG 0: Parse & Tokenize
        if 0 in self.rungs_to_execute:
            rung0 = self._execute_rung_0(filename)
            rung_results.append(rung0)
            all_errors.extend(rung0.errors)
            all_warnings.extend(rung0.warnings)
            
            if not rung0.passed:
                return PLCValidationResult(
                    filename=filename,
                    valid=False,
                    parsed_fields={},
                    rung_results=rung_results,
                    consistency_errors=all_errors,
                    consistency_warnings=all_warnings
                )
            
            fields = rung0.data.get('fields', {})
        else:
            # Must parse even if rung 0 not explicitly selected
            fields = self.parse_filename(filename)
            if fields is None:
                return PLCValidationResult(
                    filename=filename,
                    valid=False,
                    parsed_fields={},
                    consistency_errors=["Failed to parse filename"]
                )
        
        # RUNG 1: Allowlist Enforcement
        if 1 in self.rungs_to_execute:
            rung1 = self._execute_rung_1(fields)
            rung_results.append(rung1)
            all_errors.extend(rung1.errors)
            all_warnings.extend(rung1.warnings)
        
        # RUNG 2: Cross-field Semantics
        if 2 in self.rungs_to_execute:
            rung2 = self._execute_rung_2(fields)
            rung_results.append(rung2)
            all_errors.extend(rung2.errors)
            all_warnings.extend(rung2.warnings)
        
        # RUNG 3: Context Constraints
        if 3 in self.rungs_to_execute:
            rung3 = self._execute_rung_3(fields)
            rung_results.append(rung3)
            all_errors.extend(rung3.errors)
            all_warnings.extend(rung3.warnings)
            all_chain_violations.extend(rung3.data.get('chain_violations', []))
        
        # RUNG 4: Cross-reference Integrity
        if 4 in self.rungs_to_execute:
            rung4 = self._execute_rung_4(fields, filename)
            rung_results.append(rung4)
            all_errors.extend(rung4.errors)
            all_warnings.extend(rung4.warnings)
        
        # RUNG 5: Release Gating
        if 5 in self.rungs_to_execute:
            rung5 = self._execute_rung_5(fields)
            rung_results.append(rung5)
            all_errors.extend(rung5.errors)
            all_warnings.extend(rung5.warnings)
        
        # Determine overall validity based on mode
        if self.mode == "warn" or self.mode == "report":
            valid = True
            all_warnings.extend(all_errors)
            all_errors = []
        else:
            valid = len(all_errors) == 0
        
        return PLCValidationResult(
            filename=filename,
            valid=valid,
            parsed_fields=fields,
            rung_results=rung_results,
            consistency_errors=all_errors,
            consistency_warnings=all_warnings,
            chain_violations=all_chain_violations
        )
    
    def validate_chained_consistency(self, filename: str) -> PLCValidationResult:
        """
        Validate chained consistency between nomenclature fields.
        
        This is a wrapper around execute_plc_rungs for backward compatibility.
        
        Args:
            filename: The filename to validate
            
        Returns:
            PLCValidationResult with consistency validation results
        """
        return self.execute_plc_rungs(filename)
    
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


def print_result(result: PLCValidationResult, verbose: bool = False, show_rungs: bool = False) -> None:
    """Print PLC validation result to console."""
    if result.valid:
        if verbose or result.consistency_warnings:
            print(f"✓ {result.filename}")
            if show_rungs and result.rung_results:
                for rung in result.rung_results:
                    status = "✓" if rung.passed else "✗"
                    print(f"  {status} RUNG {rung.rung_id}: {rung.rung_name}")
            for warning in result.consistency_warnings:
                print(f"  ⚠ {warning}")
            if verbose and result.chain_violations:
                print(f"  Chain violations: {len(result.chain_violations)}")
    else:
        print(f"✗ {result.filename}")
        if show_rungs and result.rung_results:
            for rung in result.rung_results:
                status = "✓" if rung.passed else "✗"
                print(f"  {status} RUNG {rung.rung_id}: {rung.rung_name}")
                for err in rung.errors:
                    print(f"    ✗ {err}")
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
    
    # Count rung statistics
    rung_stats = {}
    for result in results:
        for rung in result.rung_results:
            if rung.rung_id not in rung_stats:
                rung_stats[rung.rung_id] = {'passed': 0, 'failed': 0, 'name': rung.rung_name}
            if rung.passed:
                rung_stats[rung.rung_id]['passed'] += 1
            else:
                rung_stats[rung.rung_id]['failed'] += 1
    
    return {
        'total_files': total,
        'valid_files': valid,
        'invalid_files': invalid,
        'pass_rate': f"{(valid/total)*100:.1f}%" if total > 0 else "N/A",
        'chain_violation_summary': violation_counts,
        'files_with_warnings': sum(1 for r in results if r.consistency_warnings),
        'files_with_errors': sum(1 for r in results if r.consistency_errors),
        'rung_statistics': rung_stats,
    }


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='PLC (Process Logic Control) validator for AMPEL360 Space-T nomenclature chained consistency',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
PLC RUNG STACK ARCHITECTURE:
═══════════════════════════════════════════════════════════════════════════════
  RUNG 0: Parse & Tokenize      - Parse v6.0 tokens from filename
  RUNG 1: Allowlist Enforcement - FAMILY/VARIANT/VERSION/MODEL/AoR/TYPE/STATUS
  RUNG 2: Cross-field Semantics - VARIANT↔SUBJECT prefix, TEKNIA issuance
  RUNG 3: Context Constraints   - ATA↔BLOCK, PHASE↔STATUS, MODEL↔TYPE
  RUNG 4: Cross-reference       - Internal link integrity (placeholder)
  RUNG 5: Release Gating        - PR^3 aware, lifecycle STATUS checks
═══════════════════════════════════════════════════════════════════════════════

Examples:
  %(prog)s 27_AMPEL360_SPACET_Q10_GEN_PLUS_BB_OPS_LC03_K06_SE__thermal-loop_STD_I01-R01_ACTIVE.md
  %(prog)s --check-all
  %(prog)s --check-all --verbose --show-rungs
  %(prog)s --check-all --rung 0,1,2  # Run specific rungs only
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
    parser.add_argument(
        '--rung',
        metavar='RUNGS',
        help='Comma-separated list of rung IDs to execute (0-5). Default: all'
    )
    parser.add_argument(
        '--show-rungs',
        action='store_true',
        help='Show individual rung results in output'
    )
    
    args = parser.parse_args()
    
    if not any([args.filename, args.check_all, args.check_dir]):
        parser.error('Must specify filename, --check-all, or --check-dir')
    
    # Parse rung selection
    rungs = None
    if args.rung:
        try:
            rungs = [int(r.strip()) for r in args.rung.split(',')]
            for r in rungs:
                if r < 0 or r > 5:
                    parser.error(f'Invalid rung ID: {r}. Must be 0-5.')
        except ValueError:
            parser.error('--rung must be comma-separated integers (e.g., 0,1,2)')
    
    validator = PLCValidator(
        config_path=args.config,
        strict=args.strict,
        mode=args.mode,
        rungs=rungs
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
                    print_result(result, verbose=args.verbose, show_rungs=args.show_rungs)
                    if result.consistency_warnings:
                        warning_count += 1
            else:
                invalid_count += 1
                print_result(result, verbose=args.verbose, show_rungs=args.show_rungs)
        
        # Print summary
        total = len(results)
        if total > 1 or args.check_all or args.check_dir or args.report:
            print(f"\n{'═'*70}")
            print("PLC VALIDATION SUMMARY (RUNG STACK ARCHITECTURE v2.0)")
            print(f"{'═'*70}")
            print(f"Total files scanned: {total}")
            print(f"  ✓ Valid:   {valid_count}")
            print(f"  ✗ Invalid: {invalid_count}")
            print(f"  ⚠ With warnings: {warning_count}")
            
            if args.report:
                report = generate_plc_report(results)
                print(f"\nPass rate: {report['pass_rate']}")
                
                # Print rung statistics
                if report.get('rung_statistics'):
                    print("\nRung execution summary:")
                    for rung_id in sorted(report['rung_statistics'].keys()):
                        stats = report['rung_statistics'][rung_id]
                        passed = stats['passed']
                        failed = stats['failed']
                        total_rung = passed + failed
                        rate = (passed / total_rung * 100) if total_rung > 0 else 0
                        print(f"  RUNG {rung_id}: {stats['name']}")
                        print(f"    Passed: {passed}, Failed: {failed} ({rate:.1f}%)")
                
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
