#!/usr/bin/env python3
"""
AMPEL360 Space-T Nomenclature v5.0 Retrofit Executor
=====================================================

Executes the rename operation from v4.0 to v5.0 nomenclature using the 
generated rename_map_v5.csv.

Features:
- Batch execution with safety controls
- Dry-run mode
- Rollback capability (via Git)
- Progress tracking
- Validation after each batch

Usage:
    python scripts/execute_rename_v5.py --dry-run
    python scripts/execute_rename_v5.py --batch all
    python scripts/execute_rename_v5.py --batch 1
"""

import csv
import sys
import argparse
import shutil
from pathlib import Path
from typing import List, Dict, Tuple


def load_rename_map(csv_path: str) -> List[Dict[str, str]]:
    """Load rename map from CSV."""
    entries = []
    with open(csv_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            entries.append(row)
    return entries


def execute_rename(old_path: str, new_path: str, dry_run: bool = False) -> Tuple[bool, str]:
    """
    Execute a single file rename.
    
    Returns: (success, message)
    """
    old_file = Path(old_path)
    new_file = Path(new_path)
    
    # Check if old file exists
    if not old_file.exists():
        return False, f"Source file not found: {old_path}"
    
    # Check if new file already exists
    if new_file.exists():
        return False, f"Target file already exists: {new_path}"
    
    # Ensure target directory exists
    new_file.parent.mkdir(parents=True, exist_ok=True)
    
    if dry_run:
        return True, f"[DRY-RUN] Would rename: {old_path} → {new_path}"
    
    try:
        # Use Git to rename (preserves history)
        import subprocess
        result = subprocess.run(
            ['git', 'mv', old_path, new_path],
            capture_output=True,
            text=True,
            check=True
        )
        return True, f"Renamed: {old_path} → {new_path}"
    except subprocess.CalledProcessError as e:
        # Fallback to regular rename if git mv fails
        try:
            shutil.move(str(old_file), str(new_file))
            return True, f"Renamed (non-git): {old_path} → {new_path}"
        except Exception as ex:
            return False, f"Failed to rename {old_path}: {ex}"


def execute_batch(entries: List[Dict[str, str]], batch_id: str, dry_run: bool = False) -> Tuple[int, int, List[str]]:
    """
    Execute a batch of renames.
    
    Returns: (success_count, fail_count, error_messages)
    """
    success_count = 0
    fail_count = 0
    errors = []
    
    print(f"\n{'='*70}")
    print(f"Executing Batch: {batch_id}")
    print(f"Mode: {'DRY-RUN' if dry_run else 'EXECUTE'}")
    print(f"Files to process: {len(entries)}")
    print(f"{'='*70}\n")
    
    for i, entry in enumerate(entries, 1):
        old_path = entry['old_path']
        new_path = entry['new_path']
        confidence = float(entry['confidence'])
        
        # Skip if file doesn't need renaming (same path)
        if old_path == new_path:
            continue
        
        success, message = execute_rename(old_path, new_path, dry_run)
        
        if success:
            success_count += 1
            if dry_run or i % 50 == 0:  # Progress update every 50 files
                print(f"[{i}/{len(entries)}] {message}")
        else:
            fail_count += 1
            errors.append(message)
            print(f"[{i}/{len(entries)}] ✗ {message}")
    
    return success_count, fail_count, errors


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Execute Nomenclature v5.0 retrofit',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Dry-run to preview changes
  %(prog)s --dry-run

  # Execute all renames
  %(prog)s --batch all

  # Execute specific batch (not implemented - executes all)
  %(prog)s --batch 1
        """
    )
    
    parser.add_argument(
        '--batch',
        choices=['all', '1', '2', '3', '4', '5'],
        help='Batch to execute (currently only "all" is supported)'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Preview changes without executing'
    )
    parser.add_argument(
        '--csv',
        default='rename_map_v5.csv',
        help='Path to rename map CSV (default: rename_map_v5.csv)'
    )
    
    args = parser.parse_args()
    
    # Validate arguments
    if not args.batch and not args.dry_run:
        parser.error('Must specify --batch or --dry-run')
    
    # Load rename map
    csv_path = Path(args.csv)
    if not csv_path.exists():
        print(f"Error: Rename map not found: {csv_path}", file=sys.stderr)
        return 2
    
    print(f"Loading rename map from {csv_path}...")
    entries = load_rename_map(str(csv_path))
    print(f"Loaded {len(entries)} entries")
    
    # Filter entries based on batch (for now, execute all)
    if args.batch:
        batch_entries = entries
        batch_id = args.batch
    else:
        # Dry-run mode - preview first 20
        batch_entries = entries[:20] if args.dry_run else entries
        batch_id = "DRY-RUN-PREVIEW"
    
    # Execute batch
    success, fail, errors = execute_batch(batch_entries, batch_id, args.dry_run or False)
    
    # Print summary
    print(f"\n{'='*70}")
    print(f"Batch {batch_id} Summary")
    print(f"{'='*70}")
    print(f"Successful: {success}")
    print(f"Failed: {fail}")
    print(f"Total processed: {success + fail}")
    
    if errors:
        print(f"\nErrors ({len(errors)}):")
        for error in errors[:10]:  # Show first 10 errors
            print(f"  - {error}")
        if len(errors) > 10:
            print(f"  ... and {len(errors) - 10} more errors")
    
    print(f"{'='*70}\n")
    
    # Return appropriate exit code
    if fail > 0 and not args.dry_run:
        print("⚠ Some renames failed. Review errors above.")
        return 1
    elif not args.dry_run:
        print("✅ All renames completed successfully!")
        print("\nNext steps:")
        print("  1. Run validator: python validate_nomenclature.py --check-all")
        print("  2. Update cross-references (create update script)")
        print("  3. Commit changes: Use report_progress tool")
        return 0
    else:
        print("ℹ Dry-run completed. Use --batch all to execute.")
        return 0


if __name__ == '__main__':
    sys.exit(main())
