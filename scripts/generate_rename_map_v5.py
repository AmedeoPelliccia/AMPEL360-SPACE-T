#!/usr/bin/env python3
"""
AMPEL360 Space-T Nomenclature v4.0 → v5.0 Rename Map Generator
================================================================

Generates a rename mapping CSV for migrating from v4.0 to v5.0 nomenclature.

Key v5.0 changes:
1. Add STATUS field (new mandatory field)
2. Map BUCKET to BLOCK (semantic change)
3. Handle K00 → K01-K14 mapping (strict governance)
4. Validate all field constraints

Output: rename_map_v5.csv with columns:
  old_path, new_path, confidence, rule_applied, notes, requires_review
"""

import re
import csv
import sys
from pathlib import Path
from typing import List, Dict, Tuple, Optional


# v4.0 Pattern
V4_PATTERN = re.compile(
    r'^(?P<root>\d{2,3})_'
    r'(?P<project>AMPEL360)_'
    r'(?P<program>SPACET)_'
    r'(?P<variant>[A-Z0-9]+(?:-[A-Z0-9]+)*)_'
    r'(?P<bucket>00|10|20|30|40|50|60|70|80|90)_'
    r'(?P<type>[A-Z0-9]{2,8})_'
    r'(?P<lcsb>(LC(0[1-9]|1[0-4])|SB(1[5-9]|[2-9]\d)))_'
    r'(?P<knot>K(00|[0-9]{2}))_'
    r'(?P<aor>[A-Z]+)__'
    r'(?P<desc>[a-z0-9]+(?:-[a-z0-9]+)*)_'
    r'(?P<ver>v\d{2})'
    r'\.(?P<ext>[a-z0-9]{1,6})$'
)

# BUCKET → BLOCK mapping
BUCKET_TO_BLOCK_MAP = {
    '00': 'GEN',     # General/Lifecycle → GEN
    '10': 'OPS',     # Operations
    '20': 'SYS',     # Primary Subsystem → Systems
    '30': 'CIRC',    # Circularity
    '40': 'SW',      # Software
    '50': 'STR',     # Structures
    '60': 'STOR',    # Storages
    '70': 'PROP',    # Propulsion
    '80': 'ENRG',    # Energy
    '90': 'GEN',     # Tables/Schemas/Diagrams → General
}

# K00 → K01-K14 mapping heuristics
# Based on file content/path analysis
K00_MAPPING_RULES = {
    'certification': 'K01',
    'cert': 'K01',
    'safety': 'K02',
    'saf': 'K02',
    'hazard': 'K02',
    'propulsion': 'K03',
    'prop': 'K03',
    'configuration': 'K04',
    'cm': 'K04',
    'nomenclature': 'K04',
    'data': 'K05',
    'governance': 'K05',
    'evidence': 'K06',
    'k06': 'K06',
    'ai': 'K11',
    'automation': 'K11',
}

# Default STATUS mapping
STATUS_MAP = {
    'draft': 'DRAFT',
    'active': 'ACTIVE',
    'template': 'TEMPLATE',
    'approved': 'APPROVED',
}


def map_k00_to_knot(desc: str, aor: str, type_code: str) -> Tuple[str, float, str]:
    """
    Map K00 to appropriate K01-K14 based on context.
    
    Returns: (knot_id, confidence, reason)
    """
    desc_lower = desc.lower()
    aor_lower = aor.lower()
    
    # Check description for keywords
    for keyword, knot in K00_MAPPING_RULES.items():
        if keyword in desc_lower:
            return (knot, 0.85, f"Keyword '{keyword}' in description")
    
    # Check AoR mapping
    aor_to_knot = {
        'CERT': 'K01',
        'SAF': 'K02',
        'CM': 'K04',
        'DATA': 'K05',
        'AI': 'K11',
    }
    if aor in aor_to_knot:
        return (aor_to_knot[aor], 0.80, f"AoR '{aor}' suggests {aor_to_knot[aor]}")
    
    # Default to K04 (Configuration Management) for global artifacts
    return ('K04', 0.60, "Default to K04 for global artifacts (requires manual review)")


def determine_status(desc: str, ver: str, variant: str) -> Tuple[str, float, str]:
    """
    Determine STATUS for v5.0 file.
    
    Returns: (status, confidence, reason)
    """
    desc_lower = desc.lower()
    
    # Check for template indicators
    if 'template' in desc_lower or variant == 'TEMPLATE':
        return ('TEMPLATE', 0.95, "Template keyword in description or variant")
    
    # Check for draft indicators
    if 'draft' in desc_lower or variant == 'DRAFT':
        return ('DRAFT', 0.95, "Draft keyword in description or variant")
    
    # Check version for v01 → likely active or draft
    if ver == 'v01':
        return ('ACTIVE', 0.75, "Version v01 suggests initial active release")
    
    # Higher versions → likely active
    return ('ACTIVE', 0.80, "Higher version suggests active document")


def generate_rename_map(directory: Path, output_csv: str = "rename_map_v5.csv"):
    """Generate rename mapping for v4.0 → v5.0 migration."""
    
    rename_entries = []
    
    print("Scanning repository for v4.0 files...")
    
    # Scan all files
    for filepath in directory.rglob('*'):
        if not filepath.is_file():
            continue
        
        # Skip excluded directories
        skip_dirs = {'.git', '.github', 'node_modules', '__pycache__', 'templates', 'scripts', 'tools', 'docs', 'config'}
        if any(parent.name in skip_dirs for parent in filepath.parents):
            continue
        
        filename = filepath.name
        
        # Try to match v4.0 pattern
        match = V4_PATTERN.match(filename)
        if not match:
            continue
        
        # Extract v4.0 components
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
        ver = components['ver']
        ext = components['ext']
        
        # Map BUCKET → BLOCK
        block = BUCKET_TO_BLOCK_MAP.get(bucket, 'GEN')
        block_confidence = 1.0 if bucket in BUCKET_TO_BLOCK_MAP else 0.5
        
        # Map KNOT (handle K00)
        if knot == 'K00':
            knot_new, knot_confidence, knot_reason = map_k00_to_knot(desc, aor, type_code)
            requires_review = True
        else:
            # Check if knot is K01-K14 (valid) or K15+ (invalid)
            knot_num = int(knot[1:])
            if 1 <= knot_num <= 14:
                knot_new = knot
                knot_confidence = 1.0
                knot_reason = "Valid K01-K14 knot"
                requires_review = False
            else:
                # K15+ not allowed in v5.0 - requires manual consolidation
                knot_new = 'K04'  # Default to CM
                knot_confidence = 0.40
                knot_reason = f"K{knot_num:02d} not allowed in v5.0 - requires manual mapping"
                requires_review = True
        
        # Determine STATUS
        status, status_confidence, status_reason = determine_status(desc, ver, variant)
        
        # Calculate overall confidence
        confidence = min(block_confidence, knot_confidence, status_confidence)
        
        # Build new filename
        new_filename = f"{root}_{project}_{program}_{variant}_{block}_{lcsb}_{knot_new}_{aor}__{desc}_{type_code}_{ver}_{status}.{ext}"
        
        # Relative paths
        old_rel_path = str(filepath.relative_to(directory))
        new_rel_path = str(filepath.parent.relative_to(directory) / new_filename) if filepath.parent != directory else new_filename
        
        # Build notes
        notes = []
        if bucket != block:
            notes.append(f"BUCKET {bucket} → BLOCK {block}")
        if knot != knot_new:
            notes.append(f"KNOT {knot} → {knot_new}: {knot_reason}")
        notes.append(f"STATUS: {status} ({status_reason})")
        
        notes_str = " | ".join(notes)
        rule_applied = "v4→v5_migration"
        
        rename_entries.append({
            'old_path': old_rel_path,
            'new_path': new_rel_path,
            'confidence': f"{confidence:.2f}",
            'rule_applied': rule_applied,
            'notes': notes_str,
            'requires_review': 'YES' if requires_review or confidence < 0.85 else 'NO'
        })
        
        print(f"  Mapped: {filename}")
        if requires_review:
            print(f"    ⚠ Requires review: {notes_str}")
    
    # Write CSV
    print(f"\nWriting rename map to {output_csv}...")
    with open(output_csv, 'w', newline='') as csvfile:
        fieldnames = ['old_path', 'new_path', 'confidence', 'rule_applied', 'notes', 'requires_review']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rename_entries)
    
    # Print summary
    total = len(rename_entries)
    requires_review_count = sum(1 for e in rename_entries if e['requires_review'] == 'YES')
    auto_process_count = total - requires_review_count
    
    print(f"\n{'='*60}")
    print(f"Rename Map Summary")
    print(f"{'='*60}")
    print(f"Total files mapped: {total}")
    print(f"Auto-processable (confidence ≥0.85): {auto_process_count}")
    print(f"Requires manual review: {requires_review_count}")
    print(f"{'='*60}")
    print(f"\nNext steps:")
    print(f"  1. Review {output_csv}")
    print(f"  2. Manually verify entries with 'requires_review=YES'")
    print(f"  3. Execute rename with: python scripts/execute_rename_v5.py")
    print(f"  4. Update cross-references")
    print(f"  5. Run validator to verify compliance")


def main():
    """Main entry point."""
    if len(sys.argv) > 1:
        directory = Path(sys.argv[1])
    else:
        directory = Path('.')
    
    if not directory.is_dir():
        print(f"Error: {directory} is not a directory", file=sys.stderr)
        return 1
    
    generate_rename_map(directory)
    return 0


if __name__ == '__main__':
    sys.exit(main())
