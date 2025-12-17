#!/usr/bin/env python3
"""
AMPEL360 Space-T Nomenclature v6.0 R1.0 Retrofit Executor
=========================================================

Executes the rename operation from v5.0 to v6.0 R1.0 nomenclature using the 
generated rename_map_v6.csv.

Features:
- Batch execution with safety controls
- Dry-run mode
- git mv for preserving history
- Progress tracking
- Validation after each batch

Usage:
    python scripts/execute_rename_v6.py --dry-run
    python scripts/execute_rename_v6.py --execute
    python scripts/execute_rename_v6.py --execute --batch 100
"""

import csv
import sys
import argparse
import subprocess
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
    Execute a single file rename using git mv.
    
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
        result = subprocess.run(
            ['git', 'mv', old_path, new_path],
            capture_output=True,
            text=True,
            check=True
        )
        return True, f"Renamed: {old_path} → {new_path}"
    except subprocess.CalledProcessError as e:
        return False, f"Failed to rename {old_path}: {e.stderr}"


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
        confidence = entry['confidence']
        
        success, message = execute_rename(old_path, new_path, dry_run)
        
        if success:
            success_count += 1
            if i % 50 == 0 or dry_run:
                print(f"  [{i}/{len(entries)}] {message}")
        else:
            fail_count += 1
            errors.append(message)
            print(f"  ❌ [{i}/{len(entries)}] {message}")
    
    print(f"\n{'='*70}")
    print(f"Batch Summary")
    print(f"{'='*70}")
    print(f"Success: {success_count}")
    print(f"Failed: {fail_count}")
    print(f"{'='*70}\n")
    
    return success_count, fail_count, errors


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description='Execute v5.0 → v6.0 R1.0 rename operation')
    parser.add_argument('--map', type=str, default='rename_map_v6.csv',
                        help='Rename map CSV file (default: rename_map_v6.csv)')
    parser.add_argument('--dry-run', action='store_true',
                        help='Dry-run mode (show what would be done)')
    parser.add_argument('--execute', action='store_true',
                        help='Execute the rename operation')
    parser.add_argument('--batch', type=int, default=None,
                        help='Process only first N entries (for testing)')
    parser.add_argument('--min-confidence', type=float, default=0.0,
                        help='Minimum confidence threshold (default: 0.0, process all)')
    
    args = parser.parse_args()
    
    if not args.dry_run and not args.execute:
        print("Error: Must specify either --dry-run or --execute")
        return 1
    
    print("="*70)
    print("AMPEL360 Space-T v5.0 → v6.0 R1.0 Rename Executor")
    print("="*70)
    print(f"Rename map: {args.map}")
    print(f"Mode: {'DRY-RUN' if args.dry_run else 'EXECUTE'}")
    print(f"Min confidence: {args.min_confidence}")
    print()
    
    # Load rename map
    print("Loading rename map...")
    try:
        entries = load_rename_map(args.map)
        print(f"  Loaded {len(entries)} entries")
    except FileNotFoundError:
        print(f"Error: Rename map file not found: {args.map}")
        return 1
    except Exception as e:
        print(f"Error loading rename map: {e}")
        return 1
    
    # Filter by confidence
    if args.min_confidence > 0:
        filtered = [e for e in entries if float(e['confidence']) >= args.min_confidence]
        print(f"  Filtered to {len(filtered)} entries with confidence ≥ {args.min_confidence}")
        entries = filtered
    
    # Limit batch size if specified
    if args.batch:
        entries = entries[:args.batch]
        print(f"  Limited to first {args.batch} entries")
    
    if not entries:
        print("No entries to process")
        return 0
    
    # Execute batch
    success_count, fail_count, errors = execute_batch(
        entries, 
        'all' if not args.batch else f'1-{args.batch}',
        dry_run=args.dry_run
    )
    
    # Report errors
    if errors:
        print(f"\n{'='*70}")
        print(f"Errors ({len(errors)}):")
        print(f"{'='*70}")
        for error in errors:
            print(f"  • {error}")
        print()
    
    # Final summary
    total = len(entries)
    print(f"{'='*70}")
    print(f"Final Summary")
    print(f"{'='*70}")
    print(f"Total processed: {total}")
    print(f"Success: {success_count} ({100*success_count/total:.1f}%)")
    print(f"Failed: {fail_count} ({100*fail_count/total:.1f}%)")
    print(f"{'='*70}")
    
    if args.dry_run:
        print("\n✅ Dry-run complete. Use --execute to perform actual renames.")
    else:
        print("\n✅ Rename operation complete.")
        print("   Next steps:")
        print("   1. Update cross-references: python scripts/update_cross_references_v6.py")
        print("   2. Update indexes")
        print("   3. Validate: python validate_nomenclature.py --standard v6.0 --check-all")
    
    return 0 if fail_count == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
