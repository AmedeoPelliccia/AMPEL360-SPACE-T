#!/usr/bin/env python3
"""
AMPEL360 Space-T File Scaffolding Tool
=======================================
Version: 2.0
Date: 2025-12-14

Automates creation of files from templates with proper nomenclature v2.0.

Usage:
    python scripts/scaffold.py <ROOT> <BUCKET> <TYPE> <LC_OR_SB> <VARIANT> <DESC> <VER>

Example:
    python scripts/scaffold.py 00 00 PLAN LC01 Q100BL safety-program v01
    Creates: 00_00_PLAN_LC01_Q100BL_safety-program_v01.md
"""

import sys
import os
from pathlib import Path
from datetime import date


# Template directory
TEMPLATE_DIR = "templates"

# Bucket to directory mapping (simplified)
BUCKET_DIRS = {
    "00": ".",  # Root level for lifecycle artifacts
    "10": ".",  # Operations - user specifies or moves later
    "20": ".",  # Primary Subsystem
    "30": ".",  # Circularity
    "40": ".",  # Software
    "50": ".",  # Structures
    "60": ".",  # Storages
    "70": ".",  # Propulsion
    "80": ".",  # Energy
    "90": ".",  # Tables/Schemas
}


def scaffold():
    """Main scaffolding function."""
    if len(sys.argv) < 8:
        print("Usage: python scripts/scaffold.py ROOT BUCKET TYPE LC_OR_SB VARIANT DESC VER")
        print("\nExample (Lifecycle):")
        print("  python scripts/scaffold.py 00 00 PLAN LC01 SPACET safety-program v02")
        print("\nExample (Non-Lifecycle):")
        print("  python scripts/scaffold.py 00 70 FHA SB00 SYS propulsion v02")
        print("\nLC_OR_SB field:")
        print("  - For BUCKET=00: LC01-LC14 (lifecycle stage)")
        print("  - For BUCKET≠00: SB00-SB99 (sub-bucket, use SB00 if none)")
        print("\nAvailable templates:")
        print("  Planning/Control: PLAN, MIN, RPT, LOG, ACT, IDX")
        print("  Safety Analysis: FHA, PSSA, SSA, FTA, ANA")
        print("  Requirements: REQ, DAL, TRC")
        print("  Data/Reference: CAT, LST, GLO, MAT, SCH, DIA, TAB, STD")
        sys.exit(1)

    root, bucket, ftype, stage, variant, desc, ver = sys.argv[1:8]
    
    # Validate inputs
    if not root.isdigit() or len(root) < 2 or len(root) > 3:
        print(f"Error: ROOT must be 2-3 digits, got '{root}'")
        sys.exit(1)
    
    if bucket not in BUCKET_DIRS:
        print(f"Error: BUCKET must be one of {list(BUCKET_DIRS.keys())}, got '{bucket}'")
        sys.exit(1)
    
    if not ftype.isupper():
        print(f"Error: TYPE must be uppercase, got '{ftype}'")
        sys.exit(1)
    
    # Validate LC_OR_SUBBUCKET
    if bucket == "00":
        if not stage.startswith("LC") or len(stage) != 4 or not stage[2:].isdigit():
            print(f"Error: BUCKET=00 requires LC_OR_SUBBUCKET to be LC01-LC14, got '{stage}'")
            sys.exit(1)
        lc_num = int(stage[2:])
        if lc_num < 1 or lc_num > 14:
            print(f"Error: LC must be 01-14, got LC{lc_num:02d}")
            sys.exit(1)
    else:
        if not stage.startswith("SB") or len(stage) != 4 or not stage[2:].isdigit():
            print(f"Error: BUCKET≠00 requires LC_OR_SUBBUCKET to be SB00-SB99, got '{stage}'")
            sys.exit(1)
    
    if not variant.replace('-', '').replace('_', '').isalnum():
        print(f"Error: VARIANT must be alphanumeric with hyphens, got '{variant}'")
        sys.exit(1)
    
    if not ver.startswith('v') or len(ver) != 3 or not ver[1:].isdigit():
        print(f"Error: VERSION must be vNN (e.g., v01), got '{ver}'")
        sys.exit(1)
    
    # Construct filename (8-field format)
    filename = f"{root}_{bucket}_{ftype}_{stage}_{variant}_{desc}_{ver}.md"
    
    # Determine target directory
    target_dir = BUCKET_DIRS.get(bucket, ".")
    full_path = os.path.join(target_dir, filename)
    
    # Check if file already exists
    if os.path.exists(full_path):
        print(f"Error: File already exists: {full_path}")
        sys.exit(1)
    
    # Find template
    template_path = os.path.join(TEMPLATE_DIR, f"{ftype}.md")
    
    if not os.path.exists(template_path):
        print(f"Warning: No template found for {ftype}. Creating minimal file.")
        content = f"---\ntitle: \"{desc}\"\ntype: {ftype}\nvariant: {variant}\nstatus: Draft\n---\n\n# {desc.replace('-', ' ').title()}\n\n"
    else:
        print(f"Using template: {template_path}")
        with open(template_path, 'r') as t:
            content = t.read()
    
    # Replace placeholders
    replacements = {
        "{{DESCRIPTION}}": desc,
        "{{TITLE}}": desc.replace("-", " ").title(),
        "{{VARIANT}}": variant,
        "{{BUCKET}}": bucket,
        "{{ROOT}}": root,
        "{{LC_OR_SUBBUCKET}}": stage,
        "{{LC_PHASE}}": stage if stage.startswith("LC") else "N/A",
        "{{SUBBUCKET}}": stage if stage.startswith("SB") else "N/A",
        "{{OWNER}}": "TBD",
        "{{SYSTEM_NAME}}": desc.replace("-", " ").title(),
        "{{DATE}}": date.today().isoformat(),
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
    print(f"  3. Commit: git add {full_path} && git commit -m 'Add {desc}'")


def get_lc_phase(bucket, variant):
    """Extract lifecycle phase (deprecated - kept for compatibility)."""
    return "N/A"


if __name__ == "__main__":
    scaffold()
