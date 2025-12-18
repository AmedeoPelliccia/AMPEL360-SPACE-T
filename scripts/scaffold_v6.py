#!/usr/bin/env python3
"""
AMPEL360 Space-T File Scaffolding Tool
=======================================
Version: 6.0 R1.0
Date: 2025-12-17

Automates creation of files from templates with proper nomenclature v5.0 or v6.0 (R1.0 FINAL LOCK).

Usage (v5.0):
    python scripts/scaffold.py --standard v5.0 <ATA_ROOT> <PROJECT> <PROGRAM> <VARIANT> <BLOCK> <PHASE> <KNOT_TASK> <AOR> <SUBJECT> <TYPE> <VERSION> <STATUS>

Usage (v6.0):
    python scripts/scaffold.py --standard v6.0 <ATA_ROOT> <PROJECT> <PROGRAM> <FAMILY> <VARIANT> <VERSION> <MODEL> <BLOCK> <PHASE> <KNOT_TASK> <AOR> <SUBJECT> <TYPE> <ISSUE-REVISION> <STATUS>

Example (v5.0):
    python scripts/scaffold.py --standard v5.0 27 AMPEL360 SPACET PLUS OPS LC03 K06 SE thermal-loop-overview STD v01 ACTIVE
    Creates: 27_AMPEL360_SPACET_PLUS_OPS_LC03_K06_SE__thermal-loop-overview_STD_v01_ACTIVE.md

Example (v6.0):
    python scripts/scaffold.py --standard v6.0 27 AMPEL360 SPACET Q10 GEN PLUS BB OPS LC03 K06 SE thermal-loop STD I01-R01 ACTIVE
    Creates: 27_AMPEL360_SPACET_Q10_GEN_PLUS_BB_OPS_LC03_K06_SE__thermal-loop_STD_I01-R01_ACTIVE.md
"""

import sys
import re
import yaml
from pathlib import Path
from typing import Dict, Any


# Template directory
TEMPLATE_DIR = "templates"

# Default config paths
DEFAULT_CONFIG_V5 = "config/nomenclature/v5_0.yaml"
DEFAULT_CONFIG_V6 = "config/nomenclature/v6_0.yaml"


def load_config(config_path: str) -> Dict[str, Any]:
    """Load configuration from YAML file."""
    try:
        path = Path(config_path)
        if not path.exists():
            # Try relative to script directory
            script_dir = Path(__file__).parent.parent
            path = script_dir / config_path
        
        if not path.exists():
            print(f"Warning: Config file not found at {config_path}, using defaults")
            return get_default_config()
        
        with open(path, 'r') as f:
            config = yaml.safe_load(f)
            return config or {}
    except Exception as e:
        print(f"Warning: Failed to load config from {config_path}: {e}, using defaults")
        return get_default_config()


def load_ata_partition_matrix(matrix_path: str) -> Dict[str, Any]:
    """Load ATA_PARTITION_MATRIX from YAML file."""
    try:
        path = Path(matrix_path)
        if not path.exists():
            # Try relative to script directory
            script_dir = Path(__file__).parent.parent
            path = script_dir / matrix_path
        
        if not path.exists():
            print(f"Warning: ATA_PARTITION_MATRIX not found at {matrix_path}")
            return {}
        
        with open(path, 'r') as f:
            matrix = yaml.safe_load(f)
            return matrix or {}
    except Exception as e:
        print(f"Warning: Failed to load ATA_PARTITION_MATRIX from {matrix_path}: {e}")
        return {}


def get_valid_blocks_for_ata(ata_root: str, matrix: Dict[str, Any]) -> list:
    """
    Get valid BLOCK values for the given ATA_ROOT from ATA_PARTITION_MATRIX.
    
    Business Rule: B00 (GENERAL) is universally valid for all ATA roots as it
    represents the universal baseline that applies to all systems. This is
    explicitly defined in the ATA_PARTITION_MATRIX as implicit/universal.
    
    Args:
        ata_root: ATA chapter code (e.g., "00", "27", "115")
        matrix: ATA_PARTITION_MATRIX dictionary
        
    Returns:
        List of valid BLOCK codes (e.g., ["B00", "B10", "B20", "B30"]).
        B00 is always included as it is universally valid per OPTINS Framework.
        Returns empty list if ATA not found in matrix.
    """
    if not matrix:
        return []
    
    # Construct ATA key (e.g., "ATA_00", "ATA_27", "ATA_115")
    ata_key = f"ATA_{ata_root}"
    
    # Search across all axes (o_axis, i_axis, t_axis, n_axis, s_axis)
    for axis_name in ['o_axis', 'i_axis', 't_axis', 'n_axis', 's_axis']:
        axis = matrix.get(axis_name, {})
        if ata_key in axis:
            ata_config = axis[ata_key]
            blocks = ata_config.get('blocks', [])
            # Work on a copy to avoid mutating or exposing the underlying config list
            merged_blocks = list(blocks)
            # B00 is always implicit/valid per OPTINS Framework (universal baseline)
            if 'B00' not in merged_blocks:
                merged_blocks.insert(0, 'B00')
            return merged_blocks
    
    # If ATA not found in matrix, return empty list
    return []


def get_default_config() -> Dict[str, Any]:
    """Return default configuration."""
    return {
        'allowlists': {
            'families': ['Q10', 'Q100'],
            'variants': ['PLUS', 'GEN', 'BASELINE', 'CERT'],
            'version_brand': ['PLUS', 'PLUSULTRA'],
            'models': ['BB', 'HW', 'SW', 'PR'],
            'blocks': ['OPS', 'STR', 'PROP', 'AI', 'DATA', 'CERT', 'SAF', 'SW', 'HW', 'SYS', 'TEST', 'MRO', 'CIRC', 'ENRG', 'STOR', 'GEN'],
            'aors': ['CM', 'CERT', 'SAF', 'SE', 'OPS', 'DATA', 'AI', 'CY', 'TEST', 'MRO', 'SPACEPORT', 'PMO', 'QA', 'SEC', 'LEG', 'FIN', 'PROC'],
            'types': ['IDX', 'STD', 'PLAN', 'MIN', 'RPT', 'LOG', 'ACT', 'FHA', 'PSSA', 'SSA', 'FTA', 'ANA', 'REQ', 'DAL', 'TRC', 'CAT', 'LST', 'GLO', 'MAT', 'SCH', 'DIA', 'TAB', 'SPEC', 'PLN', 'PROC', 'MAN', 'API', 'CFG'],
            'statuses': ['TEMPLATE', 'DRAFT', 'ACTIVE', 'APPROVED', 'RELEASED', 'SUPERSEDED', 'ARCHIVED'],
            'extensions': ['md', 'yml', 'yaml', 'json', 'csv', 'svg', 'png', 'jpg', 'jpeg', 'pdf', 'drawio']
        }
    }


def print_usage_v5():
    """Print v5.0 usage instructions."""
    print("Usage (v5.0): python scripts/scaffold.py --standard v5.0 <ATA_ROOT> <PROJECT> <PROGRAM> <VARIANT> <BLOCK> <PHASE> <KNOT_TASK> <AOR> <SUBJECT> <TYPE> <VERSION> <STATUS>")
    print("\nExample (Thermal System Overview):")
    print("  python scripts/scaffold.py --standard v5.0 27 AMPEL360 SPACET PLUS OPS LC03 K06 SE thermal-loop-overview STD v01 ACTIVE")
    print("\nField requirements:")
    print("  ATA_ROOT: 2-3 digits (00-116, e.g., 00, 27, 115)")
    print("  PROJECT: AMPEL360 (hard constraint)")
    print("  PROGRAM: SPACET (fixed)")
    print("  VARIANT: PLUS (or other approved variants - see config)")
    print("  BLOCK: OPS, STR, PROP, AI, DATA, etc. (see config)")
    print("  PHASE: LC01-LC14 (lifecycle) or SB01-SB99 (subbucket)")
    print("  KNOT_TASK: K01-K14 (optionally with -T001 to -T999)")
    print("  AOR: CM, CERT, SAF, SE, etc. (see config)")
    print("  SUBJECT: lowercase-kebab-case")
    print("  TYPE: IDX, STD, REQ, RPT, etc. (see config)")
    print("  VERSION: vNN (e.g., v01, v02)")
    print("  STATUS: TEMPLATE, DRAFT, ACTIVE, etc. (see config)")


def print_usage_v6():
    """Print v6.0 usage instructions."""
    print("Usage (v6.0): python scripts/scaffold.py --standard v6.0 <ATA_ROOT> <PROJECT> <PROGRAM> <FAMILY> <VARIANT> <VERSION> <MODEL> <BLOCK> <PHASE> <KNOT_TASK> <AOR> <SUBJECT> <TYPE> <ISSUE-REVISION> <STATUS>")
    print("\nExample (Thermal System Overview):")
    print("  python scripts/scaffold.py --standard v6.0 27 AMPEL360 SPACET Q10 GEN PLUS BB B10 LC03 K06 SE thermal-loop STD I01-R01 ACTIVE")
    print("\nExample (Customer-specific):")
    print("  python scripts/scaffold.py --standard v6.0 27 AMPEL360 SPACET Q10 CUST PLUS01 SW B20 LC03 K06 SE cust-airbus-thermal STD I01-R01 DRAFT")
    print("\nField requirements:")
    print("  ATA_ROOT: 2-3 digits (00-116, e.g., 00, 27, 115)")
    print("  PROJECT: AMPEL360 (hard constraint)")
    print("  PROGRAM: SPACET (fixed)")
    print("  FAMILY: Q10, Q100, etc. (quantum-inspired pax family)")
    print("  VARIANT: GEN, BASELINE, CERT, CUST, MSN, etc. (governance lane)")
    print("  VERSION: PLUS, PLUS01, PLUSULTRA, PLUSULTRA02 (branding + optional iteration)")
    print("  MODEL: BB, HW, SW, PR (artifact domain)")
    print("  BLOCK: B## format (B00, B10, B20, ..., B90) - domain partition system")
    print("    NOTE: Valid BLOCK values depend on ATA_ROOT (see ATA_PARTITION_MATRIX)")
    print("  PHASE: LC01-LC14 (lifecycle) or SB01-SB99 (subbucket)")
    print("  KNOT_TASK: K01-K14 (optionally with -T001 to -T999)")
    print("  AOR: CM, CERT, SAF, SE, etc. (see config)")
    print("  SUBJECT: lowercase-kebab-case")
    print("    - CUST variant requires: cust-<custcode>- prefix")
    print("    - MSN variant requires: msn-<serial>- prefix")
    print("  TYPE: IDX, STD, REQ, RPT, etc. (see config)")
    print("  ISSUE-REVISION: I##-R## (e.g., I01-R01, I12-R03)")
    print("  STATUS: TEMPLATE, DRAFT, ACTIVE, etc. (see config)")
    print("\nNOTE: Only K01-K14 are allowed for KNOT (strict governance)!")
    print("NOTE: B## format required - valid blocks depend on ATA_ROOT per ATA_PARTITION_MATRIX")


def scaffold_v5(args):
    """Scaffold v5.0 file (deprecated - use original scaffold.py for v5.0)."""
    print("❌ Error: v5.0 scaffolding not supported in scaffold_v6.py")
    print("   Use the original scripts/scaffold.py for v5.0 file generation")
    sys.exit(1)


def validate_v6_fields(args, config, ata_matrix=None):
    """Validate v6.0 fields."""
    ata_root, project, program, family, variant, version, model, block, phase, knot_task, aor, subject, ftype, issue_revision, status = args[:15]
    
    allowlists = config.get('allowlists', {})
    patterns = config.get('patterns', {})
    limits = config.get('limits', {})
    
    errors = []
    
    # Validate ATA_ROOT
    if not ata_root.isdigit() or len(ata_root) < 2 or len(ata_root) > 3:
        errors.append(f"ATA_ROOT must be 2-3 digits, got '{ata_root}'")
    else:
        ata_num = int(ata_root)
        if ata_num < 100 and len(ata_root) != 2:
            errors.append(f"ATA_ROOT must be 2 digits for values <100, got '{ata_root}'")
        elif ata_num >= 100 and len(ata_root) != 3:
            errors.append(f"ATA_ROOT must be 3 digits for values ≥100, got '{ata_root}'")
    
    # Validate PROJECT
    if project != "AMPEL360":
        errors.append(f"PROJECT must be AMPEL360 (hard constraint), got '{project}'")
    
    # Validate PROGRAM
    if program != "SPACET":
        errors.append(f"PROGRAM must be SPACET (fixed), got '{program}'")
    
    # Validate FAMILY
    allowed_families = allowlists.get('families', ['Q10', 'Q100'])
    if family not in allowed_families:
        errors.append(f"FAMILY must be one of {allowed_families}, got '{family}'")
    
    # Validate VARIANT
    allowed_variants = allowlists.get('variants', ['GEN'])
    if variant not in allowed_variants:
        errors.append(f"VARIANT must be one of {allowed_variants}, got '{variant}'")
    
    # Validate VERSION (brand + optional iteration)
    version_pattern = patterns.get('version', r'^(PLUS|PLUSULTRA)([0-9]{2})?$')
    if not re.match(version_pattern, version):
        brand_roots = allowlists.get('version_brand', ['PLUS', 'PLUSULTRA'])
        errors.append(f"VERSION must be a brand root ({', '.join(brand_roots)}) optionally followed by 2 digits, got '{version}'")
    
    # Validate MODEL
    allowed_models = allowlists.get('models', ['BB', 'HW', 'SW', 'PR'])
    if model not in allowed_models:
        errors.append(f"MODEL must be one of {allowed_models}, got '{model}'")
    
    # Validate BLOCK allowlist
    allowed_blocks = allowlists.get('blocks', [])
    if block not in allowed_blocks:
        errors.append(f"BLOCK must be one of {allowed_blocks}, got '{block}'")
    
    # Validate B## pattern format (Phase 2)
    block_pattern = patterns.get('block', r'^B([0-9]0)$')
    if not re.match(block_pattern, block):
        errors.append(f"BLOCK must be in B## format (B00, B10, B20, ..., B90), got '{block}'")
    
    # Validate ATA_ROOT + BLOCK combination (Phase 2)
    if ata_matrix:
        valid_blocks = get_valid_blocks_for_ata(ata_root, ata_matrix)
        if valid_blocks and block not in valid_blocks:
            errors.append(
                f"Invalid BLOCK '{block}' for ATA_ROOT '{ata_root}': "
                f"must be one of {sorted(valid_blocks)} (per ATA_PARTITION_MATRIX)"
            )
    
    # Validate PHASE
    if not re.match(r'^(LC(0[1-9]|1[0-4])|SB(0[1-9]|[1-9][0-9]))$', phase):
        errors.append(f"PHASE must be LC01-LC14 or SB01-SB99, got '{phase}'")
    
    # Validate KNOT_TASK
    if not re.match(r'^K(0[1-9]|1[0-4])(-T[0-9]{3})?$', knot_task):
        errors.append(f"KNOT_TASK must be K01-K14 (optionally with -T001 to -T999), got '{knot_task}'")
    
    # Validate AoR
    allowed_aors = allowlists.get('aors', [])
    if aor not in allowed_aors:
        errors.append(f"AoR must be one of {allowed_aors}, got '{aor}'")
    
    # Validate SUBJECT
    if not re.match(r'^[a-z0-9]+(-[a-z0-9]+)*$', subject):
        errors.append(f"SUBJECT must be lowercase kebab-case, got '{subject}'")
    
    # Validate conditional SUBJECT prefixes (R1.0 FINAL LOCK)
    subject_prefix_rules = patterns.get('subject_prefix_for_variant', {})
    if variant in subject_prefix_rules:
        required_pattern = subject_prefix_rules[variant]
        if not re.match(required_pattern, subject):
            if variant == 'CUST':
                errors.append(f"VARIANT '{variant}' requires SUBJECT to start with 'cust-<custcode>-' (custcode: 2-12 alphanumeric)")
            elif variant == 'MSN':
                errors.append(f"VARIANT '{variant}' requires SUBJECT to start with 'msn-<serial>-' (serial: 3-6 digits)")
    
    # Validate TYPE
    allowed_types = allowlists.get('types', [])
    if ftype not in allowed_types:
        errors.append(f"TYPE must be one of {allowed_types}, got '{ftype}'")
    
    # Validate ISSUE-REVISION
    if not re.match(r'^I[0-9]{2}-R[0-9]{2}$', issue_revision):
        errors.append(f"ISSUE-REVISION must be I##-R## format, got '{issue_revision}'")
    
    # Validate STATUS
    allowed_statuses = allowlists.get('statuses', [])
    if status not in allowed_statuses:
        errors.append(f"STATUS must be one of {allowed_statuses}, got '{status}'")
    
    # Validate length limits (R1.0 FINAL LOCK)
    token_limits = limits.get('token_max_len', {})
    if len(block) > token_limits.get('block', 12):
        errors.append(f"BLOCK exceeds maximum length of {token_limits.get('block', 12)} chars")
    if len(subject) > token_limits.get('subject', 60):
        errors.append(f"SUBJECT exceeds maximum length of {token_limits.get('subject', 60)} chars")
    if len(ftype) > token_limits.get('type', 8):
        errors.append(f"TYPE exceeds maximum length of {token_limits.get('type', 8)} chars")
    if len(aor) > token_limits.get('aor', 10):
        errors.append(f"AoR exceeds maximum length of {token_limits.get('aor', 10)} chars")
    
    return errors


def scaffold_v6(args):
    """Scaffold v6.0 R1.0 file."""
    if len(args) < 15:
        print_usage_v6()
        sys.exit(1)
    
    ata_root, project, program, family, variant, version, model, block, phase, knot_task, aor, subject, ftype, issue_revision, status = args[:15]
    
    # Load config
    config = load_config(DEFAULT_CONFIG_V6)
    
    # Load ATA_PARTITION_MATRIX (Phase 2)
    optins_config = config.get('optins_framework', {})
    matrix_path = optins_config.get('ata_partition_matrix', 'config/nomenclature/ATA_PARTITION_MATRIX.yaml')
    ata_matrix = load_ata_partition_matrix(matrix_path)
    
    # Validate all fields
    errors = validate_v6_fields(args, config, ata_matrix)
    if errors:
        print("❌ Validation errors:")
        for error in errors:
            print(f"  - {error}")
        sys.exit(1)
    
    # Determine extension based on TYPE
    ext = "md"  # Default
    
    # Generate filename
    filename = f"{ata_root}_{project}_{program}_{family}_{variant}_{version}_{model}_{block}_{phase}_{knot_task}_{aor}__{subject}_{ftype}_{issue_revision}_{status}.{ext}"
    
    # Check filename length (R1.0 FINAL LOCK)
    limits = config.get('limits', {})
    max_len = limits.get('filename_max_len', 180)
    if len(filename) > max_len:
        print(f"❌ Error: Filename length ({len(filename)}) exceeds maximum ({max_len} chars)")
        print(f"   Consider shortening SUBJECT or other fields")
        sys.exit(1)
    
    print(f"✅ Generated filename: {filename}")
    print(f"   Length: {len(filename)} chars (max: {max_len})")
    
    # Check for template file
    template_file = Path(TEMPLATE_DIR) / f"{ftype}.md"
    if template_file.exists():
        print(f"   Template: {template_file}")
    else:
        print(f"   Warning: No template found for TYPE '{ftype}'")
    
    return filename


def main():
    """Main entry point."""
    if len(sys.argv) < 3:
        print("AMPEL360 Space-T File Scaffolding Tool")
        print("=" * 60)
        print("\nUsage: python scripts/scaffold.py --standard <v5.0|v6.0> <fields...>")
        print("\nFor v5.0 usage:")
        print("  python scripts/scaffold.py --standard v5.0 --help")
        print("\nFor v6.0 usage:")
        print("  python scripts/scaffold.py --standard v6.0 --help")
        sys.exit(1)
    
    if sys.argv[1] != '--standard':
        print("Error: First argument must be '--standard'")
        sys.exit(1)
    
    standard = sys.argv[2]
    args = sys.argv[3:]
    
    if args and args[0] == '--help':
        if standard == 'v5.0':
            print_usage_v5()
        elif standard == 'v6.0':
            print_usage_v6()
        else:
            print(f"Error: Unknown standard '{standard}'. Must be 'v5.0' or 'v6.0'")
        sys.exit(0)
    
    if standard == 'v5.0':
        scaffold_v5(args)
    elif standard == 'v6.0':
        scaffold_v6(args)
    else:
        print(f"Error: Unknown standard '{standard}'. Must be 'v5.0' or 'v6.0'")
        sys.exit(1)
    
    print(f"\n✅ Scaffold complete!")


if __name__ == '__main__':
    main()
