#!/usr/bin/env python3
"""
AMPEL360 Space-T File Scaffolding Tool
=======================================
Version: 4.0
Date: 2025-12-16

Automates creation of files from templates with proper nomenclature v4.0.

Usage:
    python scripts/scaffold.py <ROOT> <PROJECT> <PROGRAM> <VARIANT> <BUCKET> <TYPE> <LC|SB> <KNOT> <AOR> <DESC> <VER>

Example:
    python scripts/scaffold.py 00 AMPEL360 SPACET PLUS 00 PLAN LC01 K00 CM safety-program v01
    Creates: 00_AMPEL360_SPACET_PLUS_00_PLAN_LC01_K00_CM__safety-program_v01.md
"""

import sys
import os
from pathlib import Path
from datetime import date


# Template directory
TEMPLATE_DIR = "templates"

# Allowed AoR values (v4.0)
ALLOWED_AORS = [
    'CM', 'CERT', 'AI', 'DATA', 'OPS', 'SE', 'SAF', 
    'PMO', 'CY', 'TEST', 'MRO', 'SPACEPORT'
]

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
    if len(sys.argv) < 12:
        print("Usage: python scripts/scaffold.py ROOT PROJECT PROGRAM VARIANT BUCKET TYPE LC|SB KNOT AOR DESC VER")
        print("\nExample (Global Program Plan):")
        print("  python scripts/scaffold.py 00 AMPEL360 SPACET PLUS 00 PLAN LC01 K00 CM safety-program v01")
        print("\nExample (Certification Authority Basis):")
        print("  python scripts/scaffold.py 00 AMPEL360 SPACET CERT 00 PLAN LC10 K01 CERT certification-authority-basis v01")
        print("\nExample (Propulsion FHA):")
        print("  python scripts/scaffold.py 00 AMPEL360 SPACET PLUS 70 FHA SB70 K02 SAF propulsion v01")
        print("\nExample (ATA Tasklist):")
        print("  python scripts/scaffold.py 78 AMPEL360 SPACET PLUS 00 IDX LC01 K03 SPACEPORT k03-ata-78-tasklist v01")
        print("\nField requirements:")
        print("  ROOT: 2-3 digits (ATA chapter)")
        print("  PROJECT: AMPEL360 (hard constraint)")
        print("  PROGRAM: SPACET (fixed)")
        print("  VARIANT: PLUS, CERT, BB, DRAFT, PROTO, SYS, SW, HW, GEN")
        print("  BUCKET: 00, 10, 20, 30, 40, 50, 60, 70, 80, 90")
        print("  TYPE: PLAN, FHA, REQ, etc.")
        print("  LC|SB: LC01-LC14 (for BUCKET=00) or SB15-SB99 (for others)")
        print("  KNOT: K00 (global) or K01-K99 (specific knot)")
        print("  AOR: CM, CERT, SAF, etc. (see allowlist)")
        print("  DESC: lowercase-kebab-case")
        print("  VER: vNN (e.g., v01)")
        print("\nAoR Allowlist:")
        print("  " + ", ".join(ALLOWED_AORS))
        print("\nAvailable templates:")
        print("  Planning/Control: PLAN, MIN, RPT, LOG, ACT, IDX")
        print("  Safety Analysis: FHA, PSSA, SSA, FTA, ANA")
        print("  Requirements: REQ, DAL, TRC")
        print("  Data/Reference: CAT, LST, GLO, MAT, SCH, DIA, TAB, STD")
        sys.exit(1)

    root, project, program, variant, bucket, ftype, lcsb, knot, aor, desc, ver = sys.argv[1:12]
    
    # Validate inputs
    if not root.isdigit() or len(root) < 2 or len(root) > 3:
        print(f"Error: ROOT must be 2-3 digits, got '{root}'")
        sys.exit(1)
    
    # Validate PROJECT (hard constraint)
    if project != "AMPEL360":
        print(f"Error: PROJECT must be AMPEL360 (hard constraint), got '{project}'")
        sys.exit(1)
    
    # Validate PROGRAM (allowlist)
    if program not in ["SPACET"]:
        print(f"Error: PROGRAM must be SPACET (allowlist), got '{program}'")
        sys.exit(1)
    
    if not variant.replace('-', '').replace('_', '').isalnum():
        print(f"Error: VARIANT must be alphanumeric with hyphens, got '{variant}'")
        sys.exit(1)
    
    if bucket not in BUCKET_DIRS:
        print(f"Error: BUCKET must be one of {list(BUCKET_DIRS.keys())}, got '{bucket}'")
        sys.exit(1)
    
    if not ftype.isupper():
        print(f"Error: TYPE must be uppercase, got '{ftype}'")
        sys.exit(1)
    
    # Validate LC|SB
    if bucket == "00":
        if not lcsb.startswith("LC") or len(lcsb) != 4 or not lcsb[2:].isdigit():
            print(f"Error: BUCKET=00 requires LC|SB to be LC01-LC14, got '{lcsb}'")
            sys.exit(1)
        lc_num = int(lcsb[2:])
        if lc_num < 1 or lc_num > 14:
            print(f"Error: LC must be 01-14, got LC{lc_num:02d}")
            sys.exit(1)
    else:
        if not lcsb.startswith("SB") or len(lcsb) != 4 or not lcsb[2:].isdigit():
            print(f"Error: BUCKET≠00 requires LC|SB to be SB15-SB99, got '{lcsb}'")
            sys.exit(1)
    
    # Validate TRIGGER_KNOT (NEW in v4.0)
    if not knot.startswith("K") or len(knot) != 3 or not knot[1:].isdigit():
        print(f"Error: TRIGGER_KNOT must be K00 or K01-K99, got '{knot}'")
        sys.exit(1)
    
    # Validate AoR (NEW in v4.0)
    if aor not in ALLOWED_AORS:
        print(f"Error: AoR must be one of {ALLOWED_AORS}, got '{aor}'")
        sys.exit(1)
    
    if not ver.startswith('v') or len(ver) != 3 or not ver[1:].isdigit():
        print(f"Error: VERSION must be vNN (e.g., v01), got '{ver}'")
        sys.exit(1)
    
    # Construct filename (12-field format, v4.0)
    filename = f"{root}_{project}_{program}_{variant}_{bucket}_{ftype}_{lcsb}_{knot}_{aor}__{desc}_{ver}.md"
    
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
        "{{PROJECT}}": project,
        "{{PROGRAM}}": program,
        "{{VARIANT}}": variant,
        "{{BUCKET}}": bucket,
        "{{ROOT}}": root,
        "{{LC_OR_SUBBUCKET}}": lcsb,  # Backward compatibility
        "{{LCSB}}": lcsb,
        "{{LC_PHASE}}": lcsb if lcsb.startswith("LC") else "N/A",
        "{{SUBBUCKET}}": lcsb if lcsb.startswith("SB") else "N/A",
        "{{TRIGGER_KNOT}}": knot,  # NEW in v4.0
        "{{AOR}}": aor,  # NEW in v4.0
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
