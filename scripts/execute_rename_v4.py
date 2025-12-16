#!/usr/bin/env python3
"""
Execute Batch Rename for v3.0 → v4.0 Migration
==============================================
Version: 4.0
Date: 2025-12-16

Executes the batch rename based on the generated rename map CSV.

Usage:
    python scripts/execute_rename_v4.py --map rename_map.csv --dry-run
    python scripts/execute_rename_v4.py --map rename_map.csv --execute
"""

import argparse
import csv
import shutil
import sys
from pathlib import Path
from typing import List, Tuple


def load_rename_map(map_file: Path) -> List[dict]:
    """
    Load rename map from CSV file.
    
    Returns:
        List of rename entries
    """
    with open(map_file, 'r') as f:
        reader = csv.DictReader(f)
        return list(reader)


def validate_rename_map(root_dir: Path, rename_map: List[dict]) -> Tuple[List[dict], List[str]]:
    """
    Validate rename map entries.
    
    Returns:
        Tuple of (valid_entries, errors)
    """
    valid_entries = []
    errors = []
    
    for i, entry in enumerate(rename_map, 1):
        old_path = root_dir / entry['old_path']
        new_path = root_dir / entry['new_path']
        
        # Check if old file exists
        if not old_path.exists():
            errors.append(f"Entry {i}: Old file does not exist: {entry['old_path']}")
            continue
        
        # Check if old file is a file (not directory)
        if not old_path.is_file():
            errors.append(f"Entry {i}: Old path is not a file: {entry['old_path']}")
            continue
        
        # Check if new file already exists
        if new_path.exists():
            errors.append(f"Entry {i}: New file already exists: {entry['new_path']}")
            continue
        
        # Check if parent directory exists for new file
        if not new_path.parent.exists():
            errors.append(f"Entry {i}: Parent directory does not exist: {new_path.parent}")
            continue
        
        valid_entries.append(entry)
    
    return valid_entries, errors


def execute_renames(root_dir: Path, rename_map: List[dict], dry_run: bool = False) -> Tuple[int, int]:
    """
    Execute the renames.
    
    Returns:
        Tuple of (success_count, failure_count)
    """
    success_count = 0
    failure_count = 0
    
    for i, entry in enumerate(rename_map, 1):
        old_path = root_dir / entry['old_path']
        new_path = root_dir / entry['new_path']
        
        if dry_run:
            print(f"[{i}/{len(rename_map)}] Would rename:")
            print(f"  From: {entry['old_path']}")
            print(f"  To:   {entry['new_path']}")
            print(f"  KNOT: {entry['trigger_knot']}, AoR: {entry['aor']}, Confidence: {entry['confidence']}")
            success_count += 1
        else:
            try:
                # Perform the rename
                old_path.rename(new_path)
                
                if i % 100 == 0 or i <= 10:
                    print(f"[{i}/{len(rename_map)}] Renamed: {entry['old_filename']} → {entry['new_filename']}")
                
                success_count += 1
            except Exception as e:
                print(f"[{i}/{len(rename_map)}] ERROR: Failed to rename {entry['old_path']}: {e}")
                failure_count += 1
    
    return success_count, failure_count


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Execute batch rename for v3.0 → v4.0 migration',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --map rename_map.csv --dry-run
  %(prog)s --map rename_map.csv --execute
  %(prog)s --map /tmp/rename_map.csv --root /path/to/repo --execute
        """
    )
    
    parser.add_argument(
        '--map',
        required=True,
        help='Rename map CSV file'
    )
    parser.add_argument(
        '--root',
        default='.',
        help='Repository root directory (default: current directory)'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Preview renames without executing'
    )
    parser.add_argument(
        '--execute',
        action='store_true',
        help='Execute the renames (WARNING: modifies files!)'
    )
    
    args = parser.parse_args()
    
    # Validate arguments
    if not args.dry_run and not args.execute:
        parser.error('Must specify --dry-run or --execute')
    
    if args.dry_run and args.execute:
        parser.error('Cannot specify both --dry-run and --execute')
    
    root_dir = Path(args.root).resolve()
    map_file = Path(args.map)
    
    if not root_dir.is_dir():
        print(f"Error: Repository root not found: {root_dir}", file=sys.stderr)
        return 2
    
    if not map_file.exists():
        print(f"Error: Rename map file not found: {map_file}", file=sys.stderr)
        return 2
    
    try:
        # Load rename map
        print(f"Loading rename map from: {map_file}")
        rename_map = load_rename_map(map_file)
        print(f"Loaded {len(rename_map)} entries")
        
        # Validate rename map
        print("\nValidating rename map...")
        valid_entries, errors = validate_rename_map(root_dir, rename_map)
        
        if errors:
            print(f"\n❌ Validation errors found ({len(errors)}):")
            for error in errors[:10]:
                print(f"  {error}")
            if len(errors) > 10:
                print(f"  ... and {len(errors) - 10} more errors")
            
            if len(valid_entries) == 0:
                print("\nNo valid entries to process. Aborting.")
                return 1
            
            print(f"\n⚠️  Proceeding with {len(valid_entries)} valid entries (skipping {len(errors)} invalid)")
        else:
            print(f"✅ All {len(valid_entries)} entries are valid")
        
        # Execute renames
        if args.dry_run:
            print("\n=== DRY RUN: Preview of renames ===\n")
            success, failure = execute_renames(root_dir, valid_entries[:10], dry_run=True)
            if len(valid_entries) > 10:
                print(f"\n... and {len(valid_entries) - 10} more renames")
            print(f"\nTotal renames to perform: {len(valid_entries)}")
        else:
            print("\n=== EXECUTING RENAMES ===")
            print("⚠️  WARNING: This will modify files in the repository!")
            print(f"Renaming {len(valid_entries)} files...\n")
            
            success, failure = execute_renames(root_dir, valid_entries, dry_run=False)
            
            print(f"\n{'='*60}")
            print(f"Rename complete:")
            print(f"  Success: {success}")
            print(f"  Failure: {failure}")
            print(f"{'='*60}")
            
            if failure > 0:
                print("\n⚠️  Some renames failed. Review errors above.")
                return 1
            else:
                print("\n✅ All renames completed successfully!")
                print("\nNext steps:")
                print("  1. Run: git status")
                print("  2. Run: python scripts/update_cross_references_v4.py --map rename_map.csv --execute")
                print("  3. Run: python validate_nomenclature.py --check-all")
                print("  4. Commit changes")
        
        return 0
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return 2


if __name__ == '__main__':
    sys.exit(main())
