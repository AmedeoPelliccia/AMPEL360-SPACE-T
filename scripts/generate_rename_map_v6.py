#!/usr/bin/env python3
"""
AMPEL360 Space-T Nomenclature v5.0 → v6.0 R1.0 Rename Map Generator
===================================================================

Generates a rename mapping CSV for migrating from v5.0 to v6.0 R1.0 nomenclature.

Key v6.0 R1.0 changes:
1. Add FAMILY field (e.g., Q10, Q100)
2. Redefine VARIANT field (governance lane: GEN, BASELINE, CERT, etc.)
3. Add VERSION field (branding: PLUS, PLUSULTRA with optional 2-digit iteration)
4. Add MODEL field (artifact domain: BB, HW, SW, PR)
5. Add ISSUE-REVISION field (change tracking: I##-R##)
6. Enforce R1.0 FINAL LOCK rules:
   - Conditional SUBJECT prefixes for CUST/MSN variants
   - Length limits validation
   - VERSION iteration pattern (optional 2-digit)

Output: rename_map_v6.csv with columns:
  old_path, new_path, confidence, rule_applied, notes
"""

import re
import csv
import sys
import yaml
from pathlib import Path
from typing import List, Dict, Tuple, Optional


# v5.0 Pattern
V5_PATTERN = re.compile(
    r'^(?P<root>\d{2,3})_'
    r'(?P<project>AMPEL360)_'
    r'(?P<program>SPACET)_'
    r'(?P<variant>[A-Z0-9]+(?:-[A-Z0-9]+)*)_'
    r'(?P<block>[A-Z0-9]+)_'
    r'(?P<phase>(LC(?:0[1-9]|1[0-4])|SB(?:0[1-9]|[1-9]\d)))_'
    r'(?P<knot>K(?:0[1-9]|1[0-4])(?:-T[0-9]{3})?)_'
    r'(?P<aor>[A-Z]+)__'
    r'(?P<subject>[a-z0-9]+(?:-[a-z0-9]+)*)_'
    r'(?P<type>[A-Z0-9]+)_'
    r'(?P<version>v\d{2})_'
    r'(?P<status>[A-Z]+)'
    r'\.(?P<ext>[a-z0-9]{1,6})$'
)


def load_v6_config(config_path: str = "config/nomenclature/v6_0.yaml") -> Dict:
    """Load v6.0 configuration from YAML."""
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)


def infer_family(root: str, block: str, desc: str, aor: str) -> Tuple[str, float, str]:
    """
    Infer FAMILY token from context.
    
    Default to Q10 (10-passenger quantum family) unless context suggests otherwise.
    
    Returns: (family, confidence, reason)
    """
    # Default to Q10 for most files
    # Q100 would be used for high-capacity variants (not present in current repo)
    return ('Q10', 0.90, "Default family Q10 (10-passenger quantum)")


def infer_variant_v6(variant_v5: str, desc: str, aor: str, type_code: str) -> Tuple[str, float, str]:
    """
    Infer v6.0 VARIANT from v5.0 VARIANT.
    
    v6.0 VARIANT is governance lane token (GEN, BASELINE, CERT, etc.)
    v5.0 VARIANT was different semantic (PLUS, etc.)
    
    Returns: (variant_v6, confidence, reason)
    """
    desc_lower = desc.lower()
    
    # Check for certification-specific files
    if aor == 'CERT' or 'cert' in desc_lower or 'certification' in desc_lower:
        return ('CERT', 0.85, "Certification context in AoR or description")
    
    # Check for baseline indicators
    if 'baseline' in desc_lower:
        return ('BASELINE', 0.90, "Baseline keyword in description")
    
    # Check for flight test indicators
    if 'flighttest' in desc_lower or 'flight-test' in desc_lower:
        return ('FLIGHTTEST', 0.90, "Flight test keyword in description")
    
    # Check for customer-specific indicators
    if 'cust' in desc_lower or 'customer' in desc_lower:
        return ('CUST', 0.85, "Customer keyword in description")
    
    # Check for MSN indicators
    if 'msn' in desc_lower or desc_lower.startswith('msn-'):
        return ('MSN', 0.90, "MSN keyword in description")
    
    # Default to GEN (general purpose)
    return ('GEN', 0.80, "Default variant GEN (general purpose)")


def infer_version(variant_v5: str, desc: str) -> Tuple[str, float, str]:
    """
    Infer VERSION token for v6.0.
    
    VERSION = branding reinforcer (PLUS, PLUSULTRA) + optional 2-digit iteration
    
    Returns: (version, confidence, reason)
    """
    desc_lower = desc.lower()
    
    # Check for PLUSULTRA indicators
    if 'plusultra' in desc_lower or 'plus-ultra' in desc_lower or 'ultra' in desc_lower:
        return ('PLUSULTRA', 0.85, "PLUSULTRA indicator in description")
    
    # Default to PLUS (standard branding)
    # Note: No iteration by default (PLUS, not PLUS01)
    return ('PLUS', 0.80, "Default version PLUS (standard branding)")


def infer_model(block: str, type_code: str, desc: str, aor: str) -> Tuple[str, float, str]:
    """
    Infer MODEL token from context.
    
    MODEL = artifact domain (BB, HW, SW, PR)
    
    Returns: (model, confidence, reason)
    """
    desc_lower = desc.lower()
    
    # Software indicators
    if block == 'SW' or 'software' in desc_lower or 'sw-' in desc_lower or aor == 'SW':
        return ('SW', 0.90, "Software context from block/description/AoR")
    
    # Hardware indicators
    if block == 'HW' or 'hardware' in desc_lower or 'hw-' in desc_lower or aor == 'HW':
        return ('HW', 0.90, "Hardware context from block/description/AoR")
    
    # Process/Procedure indicators
    if type_code in ['PROC', 'PLAN', 'MIN', 'RPT', 'LOG', 'ACT']:
        return ('PR', 0.85, f"Process artifact type {type_code}")
    
    # Default to BB (Body Brain / PR-O-RO model)
    return ('BB', 0.75, "Default model BB (Body Brain)")


def generate_issue_revision(version_v5: str, desc: str) -> Tuple[str, float, str]:
    """
    Generate ISSUE-REVISION for v6.0.
    
    Format: I##-R##
    Default: I01-R01 (initial issue, first revision)
    
    Returns: (issue_revision, confidence, reason)
    """
    # Extract version number from v5.0 version (e.g., v01 → 01)
    ver_match = re.match(r'v(\d{2})', version_v5)
    if ver_match:
        ver_num = int(ver_match.group(1))
        if ver_num == 1:
            return ('I01-R01', 0.95, "Initial version maps to I01-R01")
        else:
            # Higher versions could be revisions
            return (f'I01-R{ver_num:02d}', 0.80, f"Version {version_v5} maps to revision R{ver_num:02d}")
    
    # Default
    return ('I01-R01', 0.90, "Default issue-revision I01-R01")


def apply_r1_0_rules(variant: str, subject: str) -> Tuple[str, float, List[str]]:
    """
    Apply R1.0 FINAL LOCK rules:
    - Conditional SUBJECT prefixes for CUST/MSN variants
    - Length validation
    
    Returns: (modified_subject, confidence, warnings)
    """
    warnings = []
    modified_subject = subject
    confidence = 1.0
    
    # R1.0: VARIANT=CUST requires SUBJECT to start with cust-<custcode>-
    if variant == 'CUST':
        if not subject.startswith('cust-'):
            # Need to add prefix, but we don't have customer code
            # Flag for manual review
            warnings.append("CUST variant requires 'cust-<custcode>-' prefix in SUBJECT (manual review needed)")
            confidence = 0.60
    
    # R1.0: VARIANT=MSN requires SUBJECT to start with msn-<serial>-
    if variant == 'MSN':
        if not subject.startswith('msn-'):
            # Need to add prefix, but we don't have MSN serial
            # Flag for manual review
            warnings.append("MSN variant requires 'msn-<serial>-' prefix in SUBJECT (manual review needed)")
            confidence = 0.60
    
    # R1.0: SUBJECT length limit ≤60 chars
    if len(subject) > 60:
        warnings.append(f"SUBJECT length {len(subject)} exceeds limit of 60 chars")
        confidence = min(confidence, 0.70)
    
    return (modified_subject, confidence, warnings)


def validate_filename_length(filename: str) -> Tuple[bool, List[str]]:
    """
    Validate filename length ≤180 chars (R1.0 FINAL LOCK).
    
    Returns: (valid, warnings)
    """
    warnings = []
    if len(filename) > 180:
        warnings.append(f"Filename length {len(filename)} exceeds limit of 180 chars")
        return (False, warnings)
    return (True, warnings)


def generate_rename_map(directory: Path, output_csv: str = "rename_map_v6.csv"):
    """Generate rename mapping for v5.0 → v6.0 R1.0 migration."""
    
    rename_entries = []
    
    print("Loading v6.0 configuration...")
    try:
        config = load_v6_config()
        print(f"  Loaded config version: {config.get('version')} {config.get('revision')}")
    except Exception as e:
        print(f"  Warning: Could not load config: {e}")
        config = {}
    
    print("\nScanning repository for v5.0 files...")
    
    # Scan all files
    for filepath in directory.rglob('*'):
        if not filepath.is_file():
            continue
        
        # Skip excluded directories
        skip_dirs = {'.git', 'node_modules', '__pycache__', 'templates', 'scripts', 'tools', 'docs', 'config'}
        if any(parent.name in skip_dirs for parent in filepath.parents):
            continue
        
        filename = filepath.name
        
        # Try to match v5.0 pattern
        match = V5_PATTERN.match(filename)
        if not match:
            continue
        
        # Extract v5.0 components
        components = match.groupdict()
        root = components['root']
        project = components['project']
        program = components['program']
        variant_v5 = components['variant']
        block = components['block']
        phase = components['phase']
        knot = components['knot']
        aor = components['aor']
        subject = components['subject']
        type_code = components['type']
        version_v5 = components['version']
        status = components['status']
        ext = components['ext']
        
        # Infer v6.0 tokens
        family, family_conf, family_reason = infer_family(root, block, subject, aor)
        variant_v6, variant_conf, variant_reason = infer_variant_v6(variant_v5, subject, aor, type_code)
        version, version_conf, version_reason = infer_version(variant_v5, subject)
        model, model_conf, model_reason = infer_model(block, type_code, subject, aor)
        issue_revision, issue_conf, issue_reason = generate_issue_revision(version_v5, subject)
        
        # Apply R1.0 FINAL LOCK rules
        subject_modified, r1_conf, r1_warnings = apply_r1_0_rules(variant_v6, subject)
        
        # Calculate overall confidence
        confidence = min(family_conf, variant_conf, version_conf, model_conf, issue_conf, r1_conf)
        
        # Build new filename (v6.0 R1.0 format)
        new_filename = f"{root}_{project}_{program}_{family}_{variant_v6}_{version}_{model}_{block}_{phase}_{knot}_{aor}__{subject_modified}_{type_code}_{issue_revision}_{status}.{ext}"
        
        # Validate filename length
        length_valid, length_warnings = validate_filename_length(new_filename)
        if not length_valid:
            confidence = min(confidence, 0.60)
        
        # Relative paths
        old_rel_path = str(filepath.relative_to(directory))
        new_rel_path = str(filepath.parent.relative_to(directory) / new_filename) if filepath.parent != directory else new_filename
        
        # Build notes
        notes = []
        notes.append(f"FAMILY: {family} ({family_reason})")
        notes.append(f"VARIANT: {variant_v5} → {variant_v6} ({variant_reason})")
        notes.append(f"VERSION: {version} ({version_reason})")
        notes.append(f"MODEL: {model} ({model_reason})")
        notes.append(f"ISSUE-REVISION: {issue_revision} ({issue_reason})")
        
        if r1_warnings:
            notes.extend([f"R1.0: {w}" for w in r1_warnings])
        if length_warnings:
            notes.extend([f"LENGTH: {w}" for w in length_warnings])
        
        notes_str = " | ".join(notes)
        rule_applied = "v5→v6_R1_0_migration"
        
        rename_entries.append({
            'old_path': old_rel_path,
            'new_path': new_rel_path,
            'confidence': f"{confidence:.2f}",
            'rule_applied': rule_applied,
            'notes': notes_str,
        })
        
        print(f"  Mapped: {filename}")
        if confidence < 0.80:
            print(f"    ⚠ Low confidence ({confidence:.2f}): Review recommended")
    
    # Write CSV
    print(f"\nWriting rename map to {output_csv}...")
    with open(output_csv, 'w', newline='') as csvfile:
        fieldnames = ['old_path', 'new_path', 'confidence', 'rule_applied', 'notes']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rename_entries)
    
    # Print summary
    total = len(rename_entries)
    low_confidence_count = sum(1 for e in rename_entries if float(e['confidence']) < 0.80)
    high_confidence_count = total - low_confidence_count
    
    print(f"\n{'='*70}")
    print(f"Rename Map Summary")
    print(f"{'='*70}")
    print(f"Total files mapped: {total}")
    print(f"High confidence (≥0.80): {high_confidence_count}")
    print(f"Low confidence (<0.80): {low_confidence_count}")
    print(f"\nv6.0 R1.0 token coverage:")
    
    # Count token assignments
    family_count = sum(1 for e in rename_entries if 'FAMILY:' in e['notes'])
    variant_count = sum(1 for e in rename_entries if 'VARIANT:' in e['notes'])
    version_count = sum(1 for e in rename_entries if 'VERSION:' in e['notes'])
    model_count = sum(1 for e in rename_entries if 'MODEL:' in e['notes'])
    issue_count = sum(1 for e in rename_entries if 'ISSUE-REVISION:' in e['notes'])
    
    print(f"  FAMILY assigned: {family_count} ({100*family_count/total:.1f}%)")
    print(f"  VARIANT assigned: {variant_count} ({100*variant_count/total:.1f}%)")
    print(f"  VERSION assigned: {version_count} ({100*version_count/total:.1f}%)")
    print(f"  MODEL assigned: {model_count} ({100*model_count/total:.1f}%)")
    print(f"  ISSUE-REVISION assigned: {issue_count} ({100*issue_count/total:.1f}%)")
    
    # Count R1.0 issues
    r1_warnings = sum(1 for e in rename_entries if 'R1.0:' in e['notes'])
    length_warnings = sum(1 for e in rename_entries if 'LENGTH:' in e['notes'])
    
    print(f"\nR1.0 FINAL LOCK compliance:")
    print(f"  Conditional SUBJECT prefix warnings: {r1_warnings}")
    print(f"  Length limit warnings: {length_warnings}")
    
    print(f"\nOutput: {output_csv}")
    print(f"{'='*70}")
    
    if low_confidence_count > 0:
        print(f"\n⚠️  {low_confidence_count} files have low confidence scores - manual review recommended")


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Generate v5.0 → v6.0 R1.0 rename map')
    parser.add_argument('--directory', type=str, default='.',
                        help='Root directory to scan (default: current directory)')
    parser.add_argument('--output', type=str, default='rename_map_v6.csv',
                        help='Output CSV filename (default: rename_map_v6.csv)')
    
    args = parser.parse_args()
    
    directory = Path(args.directory).resolve()
    
    print("="*70)
    print("AMPEL360 Space-T v5.0 → v6.0 R1.0 Rename Map Generator")
    print("="*70)
    print(f"Directory: {directory}")
    print(f"Output: {args.output}")
    print()
    
    generate_rename_map(directory, args.output)
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
