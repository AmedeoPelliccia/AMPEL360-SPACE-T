#!/usr/bin/env python3
"""
AMPEL360 Space-T File Scaffolding Tool
=======================================
Version: 5.0
Date: 2025-12-17

Automates creation of files from templates with proper nomenclature v5.0.

Usage:
    python scripts/scaffold.py <ATA_ROOT> <PROJECT> <PROGRAM> <VARIANT> <BLOCK> <PHASE> <KNOT_TASK> <AOR> <SUBJECT> <TYPE> <VERSION> <STATUS>

Example:
    python scripts/scaffold.py 27 AMPEL360 SPACET PLUS OPS LC03 K06 SE thermal-loop-overview STD v01 ACTIVE
    Creates: 27_AMPEL360_SPACET_PLUS_OPS_LC03_K06_SE__thermal-loop-overview_STD_v01_ACTIVE.md
"""

import sys
import os
import yaml
from pathlib import Path
from datetime import date
from typing import Dict, Any, Optional


# Template directory
TEMPLATE_DIR = "templates"

# Default config path
DEFAULT_CONFIG_PATH = "config/nomenclature/v5_0.yaml"


def load_config(config_path: str = DEFAULT_CONFIG_PATH) -> Dict[str, Any]:
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


def get_default_config() -> Dict[str, Any]:
    """Return default configuration."""
    return {
        'allowlists': {
            'variants': ['PLUS'],
            'blocks': ['OPS', 'STR', 'PROP', 'AI', 'DATA', 'CERT', 'SAF', 'SW', 'HW', 'SYS', 'TEST', 'MRO', 'CIRC', 'ENRG', 'STOR', 'GEN'],
            'aors': ['CM', 'CERT', 'SAF', 'SE', 'OPS', 'DATA', 'AI', 'CY', 'TEST', 'MRO', 'SPACEPORT', 'PMO', 'QA', 'SEC', 'LEG', 'FIN', 'PROC'],
            'types': ['IDX', 'STD', 'PLAN', 'MIN', 'RPT', 'LOG', 'ACT', 'FHA', 'PSSA', 'SSA', 'FTA', 'ANA', 'REQ', 'DAL', 'TRC', 'CAT', 'LST', 'GLO', 'MAT', 'SCH', 'DIA', 'TAB', 'SPEC', 'PLN', 'PROC', 'MAN', 'API', 'CFG'],
            'statuses': ['TEMPLATE', 'DRAFT', 'ACTIVE', 'APPROVED', 'RELEASED', 'SUPERSEDED', 'ARCHIVED'],
            'extensions': ['md', 'yml', 'yaml', 'json', 'csv', 'svg', 'png', 'jpg', 'jpeg', 'pdf', 'drawio']
        }
    }


def scaffold():
    """Main scaffolding function."""
    if len(sys.argv) < 13:
        print("Usage: python scripts/scaffold.py <ATA_ROOT> <PROJECT> <PROGRAM> <VARIANT> <BLOCK> <PHASE> <KNOT_TASK> <AOR> <SUBJECT> <TYPE> <VERSION> <STATUS>")
        print("\nExample (Thermal System Overview):")
        print("  python scripts/scaffold.py 27 AMPEL360 SPACET PLUS OPS LC03 K06 SE thermal-loop-overview STD v01 ACTIVE")
        print("\nExample (Certification Authority Basis):")
        print("  python scripts/scaffold.py 00 AMPEL360 SPACET PLUS CERT LC10 K01 CERT certification-authority-basis PLAN v01 ACTIVE")
        print("\nExample (Propulsion FHA):")
        print("  python scripts/scaffold.py 53 AMPEL360 SPACET PLUS STR LC07 K02 CERT pressure-bulkhead-trade RPT v02 DRAFT")
        print("\nExample (AI Model Card):")
        print("  python scripts/scaffold.py 95 AMPEL360 SPACET PLUS AI SB04 K11 CM model-card-template STD v01 TEMPLATE")
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
        print("\nNOTE: Only K01-K14 are allowed for KNOT (strict governance)!")
        sys.exit(1)

    ata_root, project, program, variant, block, phase, knot_task, aor, subject, ftype, version, status = sys.argv[1:13]
    
    # Load config
    config = load_config()
    allowlists = config.get('allowlists', {})
    
    # Validate inputs
    if not ata_root.isdigit() or len(ata_root) < 2 or len(ata_root) > 3:
        print(f"Error: ATA_ROOT must be 2-3 digits, got '{ata_root}'")
        sys.exit(1)
    
    # Validate ATA_ROOT padding
    ata_num = int(ata_root)
    if ata_num < 100 and len(ata_root) != 2:
        print(f"Error: ATA_ROOT must be 2 digits for values <100, got '{ata_root}'")
        sys.exit(1)
    elif ata_num >= 100 and len(ata_root) != 3:
        print(f"Error: ATA_ROOT must be 3 digits for values ≥100, got '{ata_root}'")
        sys.exit(1)
    
    # Validate PROJECT (hard constraint)
    if project != "AMPEL360":
        print(f"Error: PROJECT must be AMPEL360 (hard constraint), got '{project}'")
        sys.exit(1)
    
    # Validate PROGRAM (fixed)
    if program != "SPACET":
        print(f"Error: PROGRAM must be SPACET (fixed), got '{program}'")
        sys.exit(1)
    
    # Validate VARIANT
    allowed_variants = allowlists.get('variants', ['PLUS'])
    if variant not in allowed_variants:
        print(f"Error: VARIANT must be one of {allowed_variants}, got '{variant}'")
        sys.exit(1)
    
    # Validate BLOCK
    allowed_blocks = allowlists.get('blocks', [])
    if block not in allowed_blocks:
        print(f"Error: BLOCK must be one of {allowed_blocks}, got '{block}'")
        sys.exit(1)
    
    # Validate PHASE
    if not (phase.startswith('LC') or phase.startswith('SB')):
        print(f"Error: PHASE must start with LC or SB, got '{phase}'")
        sys.exit(1)
    
    if phase.startswith('LC'):
        if len(phase) != 4 or not phase[2:].isdigit():
            print(f"Error: LC phase must be LC01-LC14, got '{phase}'")
            sys.exit(1)
        lc_num = int(phase[2:])
        if lc_num < 1 or lc_num > 14:
            print(f"Error: LC must be 01-14, got LC{lc_num:02d}")
            sys.exit(1)
    else:  # SB
        if len(phase) != 4 or not phase[2:].isdigit():
            print(f"Error: SB phase must be SB01-SB99, got '{phase}'")
            sys.exit(1)
        sb_num = int(phase[2:])
        if sb_num < 1 or sb_num > 99:
            print(f"Error: SB must be 01-99, got SB{sb_num:02d}")
            sys.exit(1)
    
    # Validate KNOT_TASK (strict K01-K14 governance)
    if not knot_task.startswith('K'):
        print(f"Error: KNOT_TASK must start with K, got '{knot_task}'")
        sys.exit(1)
    
    # Check for task suffix
    if '-T' in knot_task:
        parts = knot_task.split('-T')
        if len(parts) != 2:
            print(f"Error: Invalid KNOT_TASK format '{knot_task}', expected K##-T### or K##")
            sys.exit(1)
        knot_base = parts[0]
        task_suffix = parts[1]
        if len(knot_base) != 3 or not knot_base[1:].isdigit():
            print(f"Error: KNOT must be K01-K14, got '{knot_base}'")
            sys.exit(1)
        if len(task_suffix) != 3 or not task_suffix.isdigit():
            print(f"Error: Task suffix must be T001-T999, got 'T{task_suffix}'")
            sys.exit(1)
    else:
        knot_base = knot_task
        if len(knot_base) != 3 or not knot_base[1:].isdigit():
            print(f"Error: KNOT must be K01-K14, got '{knot_base}'")
            sys.exit(1)
    
    knot_num = int(knot_base[1:])
    if knot_num < 1 or knot_num > 14:
        print(f"Error: KNOT must be K01-K14 (strict governance), got '{knot_base}'")
        print("Note: K15+ are not allowed in v5.0. New knots require CM approval and standard upgrade.")
        sys.exit(1)
    
    # Validate AoR
    allowed_aors = allowlists.get('aors', [])
    if aor not in allowed_aors:
        print(f"Error: AoR must be one of {allowed_aors}, got '{aor}'")
        sys.exit(1)
    
    # Validate SUBJECT format
    if not subject.replace('-', '').isalnum() or not subject.islower() and not subject.isdigit():
        print(f"Error: SUBJECT must be lowercase kebab-case, got '{subject}'")
        sys.exit(1)
    
    # Validate TYPE
    allowed_types = allowlists.get('types', [])
    if ftype not in allowed_types:
        print(f"Error: TYPE must be one of {allowed_types}, got '{ftype}'")
        sys.exit(1)
    
    # Validate VERSION
    if not version.startswith('v') or len(version) != 3 or not version[1:].isdigit():
        print(f"Error: VERSION must be vNN (e.g., v01), got '{version}'")
        sys.exit(1)
    
    # Validate STATUS
    allowed_statuses = allowlists.get('statuses', [])
    if status not in allowed_statuses:
        print(f"Error: STATUS must be one of {allowed_statuses}, got '{status}'")
        sys.exit(1)
    
    # Construct filename (v5.0 format with STATUS field)
    filename = f"{ata_root}_{project}_{program}_{variant}_{block}_{phase}_{knot_task}_{aor}__{subject}_{ftype}_{version}_{status}.md"
    
    # Determine target directory (current directory by default)
    target_dir = "."
    full_path = os.path.join(target_dir, filename)
    
    # Check if file already exists
    if os.path.exists(full_path):
        print(f"Error: File already exists: {full_path}")
        sys.exit(1)
    
    # Find template
    template_path = os.path.join(TEMPLATE_DIR, f"{ftype}.md")
    
    if not os.path.exists(template_path):
        print(f"Warning: No template found for {ftype}. Creating minimal file.")
        content = f"---\ntitle: \"{subject}\"\ntype: {ftype}\nvariant: {variant}\nblock: {block}\nphase: {phase}\nknot_task: {knot_task}\naor: {aor}\nstatus: {status}\nversion: {version}\ndate: {date.today().isoformat()}\n---\n\n# {subject.replace('-', ' ').title()}\n\n"
    else:
        print(f"Using template: {template_path}")
        with open(template_path, 'r') as t:
            content = t.read()
    
    # Replace placeholders
    replacements = {
        "{{ATA_ROOT}}": ata_root,
        "{{PROJECT}}": project,
        "{{PROGRAM}}": program,
        "{{VARIANT}}": variant,
        "{{BLOCK}}": block,
        "{{PHASE}}": phase,
        "{{KNOT_TASK}}": knot_task,
        "{{AOR}}": aor,
        "{{SUBJECT}}": subject,
        "{{TYPE}}": ftype,
        "{{VERSION}}": version,
        "{{STATUS}}": status,
        "{{TITLE}}": subject.replace("-", " ").title(),
        "{{DESCRIPTION}}": subject,
        "{{OWNER}}": "TBD",
        "{{SYSTEM_NAME}}": subject.replace("-", " ").title(),
        "{{DATE}}": date.today().isoformat(),
        # Backward compatibility placeholders
        "{{BUCKET}}": block,  # Map BLOCK to old BUCKET
        "{{LCSB}}": phase,    # Map PHASE to old LCSB
        "{{LC_PHASE}}": phase if phase.startswith("LC") else "N/A",
        "{{SUBBUCKET}}": phase if phase.startswith("SB") else "N/A",
        "{{TRIGGER_KNOT}}": knot_task,  # Old v4.0 name
    }
    
    for placeholder, value in replacements.items():
        content = content.replace(placeholder, value)
    
    # Write file
    with open(full_path, 'w') as f:
        f.write(content)
    
    print(f"✅ Created: {full_path}")
    print(f"\nNext steps:")
    print(f"  1. Edit the file to add content")
    print(f"  2. Validate: python validate_nomenclature.py {filename}")
    print(f"  3. Commit: git add {full_path} && git commit -m 'Add {subject}'")
    print(f"\nv5.0 Format:")
    print(f"  [ATA_ROOT]_[PROJECT]_[PROGRAM]_[VARIANT]_[BLOCK]_[PHASE]_[KNOT_TASK]_[AoR]__[SUBJECT]_[TYPE]_[VERSION]_[STATUS].[EXT]")


if __name__ == "__main__":
    scaffold()
