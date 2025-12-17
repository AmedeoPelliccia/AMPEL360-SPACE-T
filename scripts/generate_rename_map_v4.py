#!/usr/bin/env python3
"""
Generate Rename Map for v3.0 → v4.0 Migration
==============================================
Version: 4.0
Date: 2025-12-16

Analyzes all v3.0 filenames and generates a rename map to v4.0 format.

Usage:
    python scripts/generate_rename_map_v4.py --output rename_map.csv [--dry-run]
"""

import argparse
import csv
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Optional

# Import the knot_aor_mapping module
sys.path.insert(0, str(Path(__file__).parent))
from knot_aor_mapping import determine_knot_and_aor


# v3.0 regex pattern
V3_PATTERN = re.compile(
    r'^(?P<root>\d{2,3})_'
    r'(?P<bucket>00|10|20|30|40|50|60|70|80|90)_'
    r'(?P<type>[A-Z0-9]{2,8})_'
    r'(?P<subject>(LC(0[1-9]|1[0-4])|SB(1[5-9]|[2-9]\d)))_'
    r'(?P<project>AMPEL360)_'
    r'(?P<program>SPACET)_'
    r'(?P<variant>[A-Z0-9]+(?:-[A-Z0-9]+)*)_'
    r'(?P<desc>[a-z0-9]+(?:-[a-z0-9]+)*)_'
    r'(?P<ver>v\d{2})'
    r'\.(?P<ext>[a-z0-9]{1,6})$'
)

# Files to exclude from renaming
EXCLUDED_FILES = {
    'README.md', 'LICENSE', 'EXAMPLES.md', 'STRUCTURE_SUMMARY.md',
    'IMPLEMENTATION_SUMMARY.md', 'REVIEW_NOTES.md',
    'NOMENCLATURE_V3_AUDIT_REPORT.md',
    '.gitignore', '.gitattributes', '.gitkeep'
}

# Directories to exclude
EXCLUDED_DIRS = {
    '.git', '.github', 'node_modules', '__pycache__',
    '.pytest_cache', '.venv', 'venv', 'dist', 'build',
    'templates', 'scripts'
}


def parse_v3_filename(filename: str) -> Optional[Dict[str, str]]:
    """
    Parse a v3.0 filename into components.
    
    Returns:
        Dict of components or None if not v3.0 format
    """
    match = V3_PATTERN.match(filename)
    if match:
        return match.groupdict()
    return None


def generate_v4_filename(v3_components: Dict[str, str], knot: str, aor: str) -> str:
    """
    Generate v4.0 filename from v3.0 components and determined KNOT/AoR.
    
    Args:
        v3_components: Parsed v3.0 components
        knot: Determined KNOT ID
        aor: Determined AoR code
    
    Returns:
        v4.0 filename
    """
    # v4.0 field order: ROOT_PROJECT_PROGRAM_VARIANT_BUCKET_TYPE_LCSB_KNOT_AOR__DESC_VER.EXT
    return (
        f"{v3_components['root']}_"
        f"{v3_components['project']}_"
        f"{v3_components['program']}_"
        f"{v3_components['variant']}_"
        f"{v3_components['bucket']}_"
        f"{v3_components['type']}_"
        f"{v3_components['subject']}_"
        f"{knot}_"
        f"{aor}__"
        f"{v3_components['desc']}_"
        f"{v3_components['ver']}"
        f".{v3_components['ext']}"
    )


def scan_repository(root_dir: Path) -> List[Tuple[Path, str]]:
    """
    Scan repository for v3.0 files to rename.
    
    Returns:
        List of (full_path, relative_path) tuples
    """
    files_to_rename = []
    
    for path in root_dir.rglob('*'):
        # Skip non-files
        if not path.is_file():
            continue
        
        # Skip excluded files
        if path.name in EXCLUDED_FILES:
            continue
        
        # Skip excluded directories
        if any(excluded in path.parts for excluded in EXCLUDED_DIRS):
            continue
        
        # Skip already v4.0 files (contain double underscore before description)
        if '__' in path.name:
            continue
        
        # Try to parse as v3.0
        v3_components = parse_v3_filename(path.name)
        if v3_components:
            rel_path = path.relative_to(root_dir)
            files_to_rename.append((path, str(rel_path)))
    
    return files_to_rename


def generate_rename_map(root_dir: Path, output_file: Path, dry_run: bool = False) -> int:
    """
    Generate rename map CSV file.
    
    Args:
        root_dir: Repository root directory
        output_file: Output CSV file path
        dry_run: If True, print but don't write file
    
    Returns:
        Number of files to rename
    """
    print(f"Scanning repository: {root_dir}")
    files_to_rename = scan_repository(root_dir)
    print(f"Found {len(files_to_rename)} v3.0 files to rename")
    
    if not files_to_rename:
        print("No files need renaming.")
        return 0
    
    # Generate rename mappings
    rename_map = []
    
    for full_path, rel_path in files_to_rename:
        # Parse v3.0 filename
        v3_components = parse_v3_filename(full_path.name)
        if not v3_components:
            print(f"Warning: Could not parse {full_path.name}")
            continue
        
        # Determine KNOT and AoR
        knot, aor, confidence = determine_knot_and_aor(
            str(rel_path),
            variant=v3_components['variant'],
            type_code=v3_components['type'],
            description=v3_components['desc']
        )
        
        # Generate v4.0 filename
        v4_filename = generate_v4_filename(v3_components, knot, aor)
        v4_rel_path = str(Path(rel_path).parent / v4_filename)
        
        # Add to rename map
        rename_map.append({
            'old_path': str(rel_path),
            'new_path': v4_rel_path,
            'old_filename': full_path.name,
            'new_filename': v4_filename,
            'trigger_knot': knot,
            'aor': aor,
            'confidence': f"{confidence:.2f}",
            'variant': v3_components['variant'],
            'type': v3_components['type'],
            'bucket': v3_components['bucket']
        })
    
    # Sort by confidence (lowest first) for manual review priority
    rename_map.sort(key=lambda x: float(x['confidence']))
    
    if dry_run:
        print("\n=== DRY RUN: Rename Map Preview ===")
        for i, entry in enumerate(rename_map[:10], 1):
            print(f"\n{i}. {entry['old_filename']}")
            print(f"   → {entry['new_filename']}")
            print(f"   KNOT: {entry['trigger_knot']}, AoR: {entry['aor']}, Confidence: {entry['confidence']}")
        
        if len(rename_map) > 10:
            print(f"\n... and {len(rename_map) - 10} more files")
        
        print(f"\nTotal files to rename: {len(rename_map)}")
        print(f"\nLow confidence (<0.6): {sum(1 for e in rename_map if float(e['confidence']) < 0.6)}")
        print(f"Medium confidence (0.6-0.8): {sum(1 for e in rename_map if 0.6 <= float(e['confidence']) < 0.8)}")
        print(f"High confidence (≥0.8): {sum(1 for e in rename_map if float(e['confidence']) >= 0.8)}")
        
    else:
        # Write CSV file
        print(f"\nWriting rename map to: {output_file}")
        with open(output_file, 'w', newline='') as f:
            fieldnames = [
                'old_path', 'new_path', 'old_filename', 'new_filename',
                'trigger_knot', 'aor', 'confidence', 'variant', 'type', 'bucket'
            ]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rename_map)
        
        print(f"✅ Rename map written: {len(rename_map)} entries")
        print(f"\nConfidence distribution:")
        print(f"  Low (<0.6):      {sum(1 for e in rename_map if float(e['confidence']) < 0.6)}")
        print(f"  Medium (0.6-0.8): {sum(1 for e in rename_map if 0.6 <= float(e['confidence']) < 0.8)}")
        print(f"  High (≥0.8):     {sum(1 for e in rename_map if float(e['confidence']) >= 0.8)}")
        
        print(f"\nNext steps:")
        print(f"  1. Review rename_map.csv (especially low confidence entries)")
        print(f"  2. Edit KNOT/AoR values manually if needed")
        print(f"  3. Run: python scripts/execute_rename_v4.py --map {output_file} --dry-run")
        print(f"  4. Run: python scripts/execute_rename_v4.py --map {output_file} --execute")
    
    return len(rename_map)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Generate rename map for v3.0 → v4.0 migration',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --output rename_map.csv --dry-run
  %(prog)s --output rename_map.csv
  %(prog)s --output /tmp/rename_map.csv --root /path/to/repo
        """
    )
    
    parser.add_argument(
        '--output',
        required=True,
        help='Output CSV file path for rename map'
    )
    parser.add_argument(
        '--root',
        default='.',
        help='Repository root directory (default: current directory)'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Preview rename map without writing file'
    )
    
    args = parser.parse_args()
    
    root_dir = Path(args.root).resolve()
    output_file = Path(args.output)
    
    if not root_dir.is_dir():
        print(f"Error: Repository root not found: {root_dir}", file=sys.stderr)
        return 2
    
    try:
        count = generate_rename_map(root_dir, output_file, dry_run=args.dry_run)
        return 0 if count > 0 else 1
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return 2


if __name__ == '__main__':
    sys.exit(main())
