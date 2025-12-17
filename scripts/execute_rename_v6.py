#!/usr/bin/env python3
"""
AMPEL360 Space-T Nomenclature v6.0 Rename Executor
==================================================

Executes batch file renames using git mv to preserve history.

Features:
- Git mv for history preservation
- Batch processing with validation
- Confidence-based filtering
- Dry-run mode
- Progress tracking and reporting
- Rollback support (via Git)

Usage:
    python scripts/execute_rename_v6.py --dry-run
    python scripts/execute_rename_v6.py --execute --min-confidence 0.85
    python scripts/execute_rename_v6.py --execute --all
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


def validate_entry(entry: Dict[str, str], min_confidence: float) -> Tuple[bool, str]:
    """
    Validate a rename entry.
    
    Returns: (is_valid, error_message)
    """
    old_path = entry['old_path']
    new_path = entry['new_path']
    confidence = float(entry['confidence'])
    
    # Check confidence threshold
    if confidence < min_confidence:
        return False, f"Confidence {confidence:.2f} below threshold {min_confidence:.2f}"
    
    # Check if source exists
    old_file = Path(old_path)
    if not old_file.exists():
        return False, f"Source file not found: {old_path}"
    
    # Check if target already exists
    new_file = Path(new_path)
    if new_file.exists():
        return False, f"Target file already exists: {new_path}"
    
    return True, ""


def execute_git_mv(old_path: str, new_path: str, dry_run: bool = False) -> Tuple[bool, str]:
    """
    Execute git mv to rename file with history preservation.
    
    Returns: (success, message)
    """
    old_file = Path(old_path)
    new_file = Path(new_path)
    
    # Ensure target directory exists
    new_file.parent.mkdir(parents=True, exist_ok=True)
    
    if dry_run:
        return True, f"[DRY-RUN] Would execute: git mv {old_path} {new_path}"
    
    try:
        # Execute git mv
        result = subprocess.run(
            ['git', 'mv', old_path, new_path],
            capture_output=True,
            text=True,
            check=True
        )
        return True, f"✓ Renamed: {old_path} → {new_path}"
    except subprocess.CalledProcessError as e:
        error_msg = e.stderr.strip() if e.stderr else str(e)
        return False, f"✗ Failed to rename {old_path}: {error_msg}"
    except Exception as e:
        return False, f"✗ Unexpected error renaming {old_path}: {e}"


def execute_batch(
    entries: List[Dict[str, str]],
    min_confidence: float,
    dry_run: bool = False,
    skip_review: bool = False
) -> Tuple[int, int, List[str]]:
    """
    Execute batch of renames.
    
    Returns: (success_count, fail_count, error_messages)
    """
    success_count = 0
    fail_count = 0
    skip_count = 0
    errors = []
    
    print()
    print("=" * 70)
    print(f"Executing Rename Batch")
    print("=" * 70)
    print(f"Mode: {'DRY-RUN' if dry_run else 'EXECUTE'}")
    print(f"Minimum confidence: {min_confidence:.2f}")
    print(f"Skip review entries: {skip_review}")
    print(f"Total entries: {len(entries)}")
    print("=" * 70)
    print()
    
    for i, entry in enumerate(entries, 1):
        old_path = entry['old_path']
        new_path = entry['new_path']
        confidence = float(entry['confidence'])
        requires_review = entry.get('requires_review', 'NO')
        
        # Skip if requires review (unless --all flag)
        if requires_review == 'YES' and not skip_review:
            skip_count += 1
            if i % 50 == 0 or i <= 5:
                print(f"[{i}/{len(entries)}] ⊘ Skipped (requires review): {old_path}")
            continue
        
        # Validate entry
        is_valid, error_msg = validate_entry(entry, min_confidence)
        if not is_valid:
            fail_count += 1
            errors.append(f"{old_path}: {error_msg}")
            print(f"[{i}/{len(entries)}] ✗ Validation failed: {error_msg}")
            continue
        
        # Execute rename
        success, message = execute_git_mv(old_path, new_path, dry_run)
        
        if success:
            success_count += 1
            # Show progress every 50 files or first 10
            if dry_run or i % 50 == 0 or i <= 10:
                print(f"[{i}/{len(entries)}] {message}")
        else:
            fail_count += 1
            errors.append(message)
            print(f"[{i}/{len(entries)}] {message}")
    
    return success_count, fail_count, skip_count, errors


def print_summary(
    total: int,
    success: int,
    fail: int,
    skip: int,
    errors: List[str],
    dry_run: bool
):
    """Print execution summary."""
    print()
    print("=" * 70)
    print("Execution Summary")
    print("=" * 70)
    print(f"Total entries: {total}")
    print(f"Successful: {success}")
    print(f"Failed: {fail}")
    print(f"Skipped (requires review): {skip}")
    print(f"Processed: {success + fail}")
    print("=" * 70)
    
    if errors:
        print()
        print(f"Errors ({len(errors)}):")
        for error in errors[:20]:  # Show first 20 errors
            print(f"  - {error}")
        if len(errors) > 20:
            print(f"  ... and {len(errors) - 20} more errors")
    
    print()
    
    if dry_run:
        print("ℹ  Dry-run completed. Use --execute to apply changes.")
    elif fail > 0:
        print("⚠  Some renames failed. Review errors above.")
        print("   Consider running git status to see changes.")
    elif success > 0:
        print("✅ All renames completed successfully!")
        print()
        print("Next steps:")
        print("  1. Run validator: python validate_nomenclature.py --check-all")
        print("  2. Update cross-references: python scripts/update_cross_references_v6.py")
        print("  3. Review changes: git status")
        print("  4. Commit changes if satisfied")
    else:
        print("ℹ  No files were renamed.")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Execute Nomenclature v6.0 batch rename',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Dry-run (preview changes)
  %(prog)s --dry-run

  # Execute high-confidence renames only
  %(prog)s --execute --min-confidence 0.85

  # Execute all renames including those requiring review
  %(prog)s --execute --all
  
  # Execute with custom CSV
  %(prog)s --execute --csv custom_rename_map.csv
        """
    )
    
    parser.add_argument(
        '--execute',
        action='store_true',
        help='Execute renames (default is dry-run)'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Preview changes without executing (default)'
    )
    parser.add_argument(
        '--all',
        action='store_true',
        help='Process all entries including those requiring manual review'
    )
    parser.add_argument(
        '--min-confidence',
        type=float,
        default=0.80,
        help='Minimum confidence threshold (default: 0.80)'
    )
    parser.add_argument(
        '--csv',
        default='rename_map_v6.csv',
        help='Path to rename map CSV (default: rename_map_v6.csv)'
    )
    
    args = parser.parse_args()
    
    # Determine mode
    dry_run = not args.execute or args.dry_run
    
    # Load rename map
    csv_path = Path(args.csv)
    if not csv_path.exists():
        print(f"Error: Rename map not found: {csv_path}", file=sys.stderr)
        print(f"Run: python scripts/generate_rename_map_v6.py", file=sys.stderr)
        return 2
    
    print(f"Loading rename map from {csv_path}...")
    entries = load_rename_map(str(csv_path))
    print(f"Loaded {len(entries)} entries")
    
    # Execute batch
    success, fail, skip, errors = execute_batch(
        entries,
        args.min_confidence,
        dry_run,
        args.all
    )
    
    # Print summary
    print_summary(len(entries), success, fail, skip, errors, dry_run)
    
    # Return appropriate exit code
    if fail > 0 and not dry_run:
        return 1
    else:
        return 0


if __name__ == '__main__':
    sys.exit(main())
