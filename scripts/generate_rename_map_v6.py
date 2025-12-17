#!/usr/bin/env python3
"""
AMPEL360 Space-T Nomenclature v6.0 Rename Map Generator
========================================================

Enhanced rename map generator with improved confidence scoring and
support for advanced features like KNOT-TASK patterns.

Key improvements over v5:
1. Multi-signal confidence scoring (path, AoR, content, type)
2. Support for K##-T### (KNOT-TASK) patterns
3. Better STATUS field inference with context analysis
4. Enhanced K00 → K01-K14 mapping with domain rules
5. Detailed reasoning and notes for all mappings

Output: rename_map_v6.csv with columns:
  old_path, new_path, confidence, rule_applied, notes, requires_review, knot_reason, status_reason
"""

import re
import csv
import sys
from pathlib import Path
from typing import List, Dict, Tuple, Optional


# v5.0 Pattern (current standard)
V5_PATTERN = re.compile(
    r'^(?P<root>\d{2,3})_'
    r'(?P<project>AMPEL360)_'
    r'(?P<program>SPACET)_'
    r'(?P<variant>[A-Z0-9]+(?:-[A-Z0-9]+)*)_'
    r'(?P<block>GEN|OPS|SYS|CIRC|SW|STR|STOR|PROP|ENRG)_'
    r'(?P<phase>(LC(0[1-9]|1[0-4])|SB(0[1-9]|[1-9]\d)))_'
    r'(?P<knot>K(0[0-9]|1[0-4])(?:-T\d{3})?)_'
    r'(?P<aor>[A-Z]+)__'
    r'(?P<subject>[a-z0-9]+(?:-[a-z0-9]+)*)_'
    r'(?P<type>[A-Z0-9]{2,8})_'
    r'(?P<version>v\d{2})_'
    r'(?P<status>TEMPLATE|DRAFT|ACTIVE|APPROVED|RELEASED|SUPERSEDED|ARCHIVED)'
    r'\.(?P<ext>[a-z0-9]{1,6})$'
)

# v4.0 Pattern (migration source if needed)
V4_PATTERN = re.compile(
    r'^(?P<root>\d{2,3})_'
    r'(?P<project>AMPEL360)_'
    r'(?P<program>SPACET)_'
    r'(?P<variant>[A-Z0-9]+(?:-[A-Z0-9]+)*)_'
    r'(?P<bucket>00|10|20|30|40|50|60|70|80|90)_'
    r'(?P<lcsb>(LC(0[1-9]|1[0-4])|SB(1[5-9]|[2-9]\d)))_'
    r'(?P<knot>K(00|[0-9]{2}))_'
    r'(?P<aor>[A-Z]+)__'
    r'(?P<desc>[a-z0-9]+(?:-[a-z0-9]+)*)_'
    r'(?P<type>[A-Z0-9]{2,8})_'
    r'(?P<ver>v\d{2})'
    r'\.(?P<ext>[a-z0-9]{1,6})$'
)

# BUCKET → BLOCK mapping (for v4 → v6 if needed)
BUCKET_TO_BLOCK_MAP = {
    '00': 'GEN',
    '10': 'OPS',
    '20': 'SYS',
    '30': 'CIRC',
    '40': 'SW',
    '50': 'STR',
    '60': 'STOR',
    '70': 'PROP',
    '80': 'ENRG',
    '90': 'GEN',
}

# Enhanced K00 → K01-K14 mapping with domain rules
K00_MAPPING_RULES = {
    # K01: Certification Authority Basis
    'certification': ('K01', 0.90),
    'cert': ('K01', 0.90),
    'authority': ('K01', 0.85),
    'basis': ('K01', 0.80),
    
    # K02: Safety Case & Hazard Analysis
    'safety': ('K02', 0.90),
    'hazard': ('K02', 0.90),
    'risk': ('K02', 0.85),
    'fha': ('K02', 0.95),
    'pssa': ('K02', 0.95),
    'ssa': ('K02', 0.95),
    'fta': ('K02', 0.95),
    
    # K03: Propulsion & Hazmat
    'propulsion': ('K03', 0.90),
    'propellant': ('K03', 0.90),
    'hazmat': ('K03', 0.90),
    'cryo': ('K03', 0.85),
    
    # K04: Configuration Management
    'configuration': ('K04', 0.90),
    'nomenclature': ('K04', 0.90),
    'cm': ('K04', 0.85),
    'versioning': ('K04', 0.80),
    
    # K05: Data Governance
    'data': ('K05', 0.85),
    'governance': ('K05', 0.85),
    'schema': ('K05', 0.90),
    'registry': ('K05', 0.85),
    
    # K06: Evidence & Audit
    'evidence': ('K06', 0.90),
    'audit': ('K06', 0.90),
    'proof': ('K06', 0.85),
    'traceability': ('K06', 0.85),
    
    # K11: AI/ML Engineering
    'ai': ('K11', 0.90),
    'ml': ('K11', 0.90),
    'automation': ('K11', 0.80),
    'model': ('K11', 0.75),
}

# AoR to KNOT mapping (high confidence)
AOR_TO_KNOT_MAP = {
    'CERT': ('K01', 0.85),
    'SAF': ('K02', 0.85),
    'CM': ('K04', 0.85),
    'DATA': ('K05', 0.85),
    'AI': ('K11', 0.85),
}

# TYPE to KNOT hints (lower confidence)
TYPE_TO_KNOT_HINTS = {
    'FHA': ('K02', 0.70),
    'PSSA': ('K02', 0.70),
    'SSA': ('K02', 0.70),
    'FTA': ('K02', 0.70),
    'PLAN': ('K04', 0.60),
    'SCH': ('K05', 0.65),
}

# STATUS inference rules
STATUS_INFERENCE_RULES = {
    'template': ('TEMPLATE', 0.95),
    'draft': ('DRAFT', 0.95),
    'wip': ('DRAFT', 0.90),
    'approved': ('APPROVED', 0.95),
    'released': ('RELEASED', 0.95),
    'active': ('ACTIVE', 0.85),
    'superseded': ('SUPERSEDED', 0.95),
    'archived': ('ARCHIVED', 0.95),
    'deprecated': ('SUPERSEDED', 0.85),
}


def analyze_confidence_signals(
    path: Path,
    subject: str,
    aor: str,
    type_code: str,
    knot: str,
    version: str
) -> Dict[str, Tuple[Optional[str], float, str]]:
    """
    Analyze multiple signals for KNOT mapping confidence.
    
    Returns dict with:
        'path_signal': (knot, confidence, reason)
        'subject_signal': (knot, confidence, reason)
        'aor_signal': (knot, confidence, reason)
        'type_signal': (knot, confidence, reason)
    """
    signals = {}
    
    # Path signal (directory structure)
    path_str = str(path).lower()
    path_knot = None
    path_conf = 0.0
    path_reason = "No path signal"
    
    if '/knots/k' in path_str:
        match = re.search(r'/knots/k(\d{2})', path_str)
        if match:
            path_knot = f"K{match.group(1)}"
            path_conf = 0.95
            path_reason = f"Path contains /KNOTS/{path_knot}/"
    
    signals['path_signal'] = (path_knot, path_conf, path_reason)
    
    # Subject signal (keywords in description)
    subject_lower = subject.lower()
    best_subject_knot = None
    best_subject_conf = 0.0
    best_subject_reason = "No subject keywords matched"
    
    for keyword, (mapped_knot, conf) in K00_MAPPING_RULES.items():
        if keyword in subject_lower:
            if conf > best_subject_conf:
                best_subject_knot = mapped_knot
                best_subject_conf = conf
                best_subject_reason = f"Keyword '{keyword}' in subject"
    
    signals['subject_signal'] = (best_subject_knot, best_subject_conf, best_subject_reason)
    
    # AoR signal
    aor_knot, aor_conf = AOR_TO_KNOT_MAP.get(aor, (None, 0.0))
    aor_reason = f"AoR '{aor}' suggests {aor_knot}" if aor_knot else "No AoR mapping"
    signals['aor_signal'] = (aor_knot, aor_conf, aor_reason)
    
    # Type signal
    type_knot, type_conf = TYPE_TO_KNOT_HINTS.get(type_code, (None, 0.0))
    type_reason = f"TYPE '{type_code}' suggests {type_knot}" if type_knot else "No TYPE hint"
    signals['type_signal'] = (type_knot, type_conf, type_reason)
    
    return signals


def determine_knot_mapping(
    knot: str,
    path: Path,
    subject: str,
    aor: str,
    type_code: str,
    version: str
) -> Tuple[str, float, str]:
    """
    Determine KNOT mapping with multi-signal analysis.
    
    Returns: (knot_id, confidence, reason)
    """
    # If knot is already K01-K14, validate it
    if knot != 'K00':
        knot_num = int(knot[1:4]) if '-' in knot else int(knot[1:])
        if 1 <= knot_num <= 14:
            return (knot, 1.0, f"Valid {knot} (already compliant)")
        else:
            # K15+ not allowed in v5.0+
            # Need manual mapping - use signals
            pass
    
    # Analyze all signals for K00 or invalid knots
    signals = analyze_confidence_signals(path, subject, aor, type_code, knot, version)
    
    # Vote-based approach: pick signal with highest confidence
    best_knot = None
    best_confidence = 0.0
    best_reason = ""
    
    for signal_name, (signal_knot, signal_conf, signal_reason) in signals.items():
        if signal_knot and signal_conf > best_confidence:
            best_knot = signal_knot
            best_confidence = signal_conf
            best_reason = signal_reason
    
    # If no signal found, default to K04 (CM) for global artifacts
    if not best_knot:
        return ('K04', 0.60, "Default to K04 for global artifacts (requires manual review)")
    
    return (best_knot, best_confidence, best_reason)


def determine_status(
    subject: str,
    version: str,
    variant: str,
    path: Path
) -> Tuple[str, float, str]:
    """
    Determine STATUS field with context analysis.
    
    Returns: (status, confidence, reason)
    """
    subject_lower = subject.lower()
    
    # Check for explicit status keywords
    for keyword, (status, conf) in STATUS_INFERENCE_RULES.items():
        if keyword in subject_lower:
            return (status, conf, f"Keyword '{keyword}' in subject")
    
    # Check variant
    if variant == 'TEMPLATE':
        return ('TEMPLATE', 0.95, "Variant is TEMPLATE")
    
    # Check version patterns
    if version == 'v01':
        # v01 could be draft or active - check path for clues
        if 'template' in str(path).lower():
            return ('TEMPLATE', 0.85, "Version v01 in templates path")
        else:
            return ('ACTIVE', 0.75, "Version v01 suggests initial active release")
    
    # Higher versions likely active
    return ('ACTIVE', 0.80, f"Version {version} suggests active document")


def generate_rename_map_v6(directory: Path, output_csv: str = "rename_map_v6.csv"):
    """Generate enhanced rename mapping for v6.0."""
    
    rename_entries = []
    
    print("=" * 70)
    print("AMPEL360 Space-T Rename Map Generator v6.0")
    print("=" * 70)
    print(f"Scanning directory: {directory}")
    print(f"Output file: {output_csv}")
    print("=" * 70)
    print()
    
    # Scan all files
    for filepath in directory.rglob('*'):
        if not filepath.is_file():
            continue
        
        # Skip excluded directories
        skip_dirs = {'.git', '.github', 'node_modules', '__pycache__', 'templates', 'scripts', 'tools', 'docs', 'config'}
        if any(parent.name in skip_dirs for parent in filepath.parents):
            continue
        
        filename = filepath.name
        
        # Try v5 pattern first
        match = V5_PATTERN.match(filename)
        source_version = 'v5.0'
        
        # Fall back to v4 pattern if v5 doesn't match
        if not match:
            match = V4_PATTERN.match(filename)
            source_version = 'v4.0'
        
        if not match:
            continue
        
        components = match.groupdict()
        
        # Extract common fields
        root = components['root']
        project = components['project']
        program = components['program']
        variant = components['variant']
        aor = components['aor']
        ext = components['ext']
        
        # Handle v4 vs v5 field differences
        if source_version == 'v4.0':
            # v4 → v6 migration
            bucket = components.get('bucket', '00')
            block = BUCKET_TO_BLOCK_MAP.get(bucket, 'GEN')
            phase = components.get('lcsb')
            knot = components.get('knot')
            subject = components.get('desc')
            type_code = components.get('type')
            version = components.get('ver')
            status = None  # Need to infer
        else:
            # v5 → v6 (potential improvements)
            block = components.get('block')
            phase = components.get('phase')
            knot = components.get('knot')
            subject = components.get('subject')
            type_code = components.get('type')
            version = components.get('version')
            status = components.get('status')
        
        # Determine KNOT mapping (if needed)
        needs_knot_mapping = False
        if source_version == 'v4.0' or knot == 'K00':
            needs_knot_mapping = True
        elif knot:
            # Extract knot number (handle K## and K##-T### formats)
            knot_match = re.match(r'K(\d{2})', knot)
            if knot_match:
                knot_num = int(knot_match.group(1))
                if knot_num > 14:
                    needs_knot_mapping = True
        
        if needs_knot_mapping:
            knot_new, knot_confidence, knot_reason = determine_knot_mapping(
                knot, filepath, subject, aor, type_code, version
            )
            requires_review = knot_confidence < 0.85
        else:
            knot_new = knot
            knot_confidence = 1.0
            knot_reason = f"Valid {knot} (already compliant)"
            requires_review = False
        
        # Determine STATUS (if needed)
        if not status:
            status_new, status_confidence, status_reason = determine_status(
                subject, version, variant, filepath
            )
            if status_confidence < 0.85:
                requires_review = True
        else:
            status_new = status
            status_confidence = 1.0
            status_reason = f"STATUS '{status}' (already specified)"
        
        # Calculate overall confidence
        confidence = min(knot_confidence, status_confidence)
        
        # Build new filename
        new_filename = f"{root}_{project}_{program}_{variant}_{block}_{phase}_{knot_new}_{aor}__{subject}_{type_code}_{version}_{status_new}.{ext}"
        
        # Build relative paths
        old_rel_path = str(filepath.relative_to(directory))
        new_rel_path = str(filepath.parent.relative_to(directory) / new_filename) if filepath.parent != directory else new_filename
        
        # Skip if no change
        if old_rel_path == new_rel_path:
            continue
        
        # Build notes
        notes = []
        if source_version == 'v4.0':
            notes.append(f"Migrating from v4.0 to v6.0")
        if knot != knot_new:
            notes.append(f"KNOT {knot} → {knot_new}")
        if not status:
            notes.append(f"STATUS inferred: {status_new}")
        
        notes_str = " | ".join(notes) if notes else "No changes required"
        rule_applied = f"{source_version}→v6.0_migration"
        
        rename_entries.append({
            'old_path': old_rel_path,
            'new_path': new_rel_path,
            'confidence': f"{confidence:.2f}",
            'rule_applied': rule_applied,
            'notes': notes_str,
            'requires_review': 'YES' if requires_review or confidence < 0.85 else 'NO',
            'knot_reason': knot_reason,
            'status_reason': status_reason,
        })
        
        print(f"  Mapped: {filename}")
        if requires_review:
            print(f"    ⚠ Requires review (confidence: {confidence:.2f})")
    
    # Write CSV
    print(f"\nWriting rename map to {output_csv}...")
    with open(output_csv, 'w', newline='') as csvfile:
        fieldnames = ['old_path', 'new_path', 'confidence', 'rule_applied', 'notes', 'requires_review', 'knot_reason', 'status_reason']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rename_entries)
    
    # Print summary
    total = len(rename_entries)
    requires_review_count = sum(1 for e in rename_entries if e['requires_review'] == 'YES')
    auto_process_count = total - requires_review_count
    
    print()
    print("=" * 70)
    print("Rename Map Summary")
    print("=" * 70)
    print(f"Total files to rename: {total}")
    print(f"Auto-processable (confidence ≥0.85): {auto_process_count} ({100*auto_process_count/total if total > 0 else 0:.1f}%)")
    print(f"Requires manual review: {requires_review_count} ({100*requires_review_count/total if total > 0 else 0:.1f}%)")
    print("=" * 70)
    
    if total > 0:
        print("\nNext steps:")
        print(f"  1. Review {output_csv}")
        print(f"  2. Manually verify entries with 'requires_review=YES'")
        print(f"  3. Execute rename: python scripts/execute_rename_v6.py")
        print(f"  4. Update cross-references: python scripts/update_cross_references_v6.py")
        print(f"  5. Run validator: python validate_nomenclature.py --check-all")
    else:
        print("\n✅ No files need renaming - repository is already compliant!")
    
    return 0 if total == 0 else 0


def main():
    """Main entry point."""
    if len(sys.argv) > 1:
        directory = Path(sys.argv[1])
    else:
        directory = Path('.')
    
    if not directory.is_dir():
        print(f"Error: {directory} is not a directory", file=sys.stderr)
        return 1
    
    return generate_rename_map_v6(directory)


if __name__ == '__main__':
    sys.exit(main())
