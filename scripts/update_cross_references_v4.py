#!/usr/bin/env python3
"""
Update Cross-References for v3.0 → v4.0 Migration
==================================================
Version: 4.0
Date: 2025-12-16

Updates all cross-references (links, imports, manifests) after rename.

Usage:
    python scripts/update_cross_references_v4.py --map rename_map.csv --dry-run
    python scripts/update_cross_references_v4.py --map rename_map.csv --execute
"""

import argparse
import csv
import re
import sys
from pathlib import Path
from typing import List, Dict, Set, Tuple


def load_rename_map(map_file: Path) -> Dict[str, str]:
    """
    Load rename map from CSV into a lookup dictionary.
    
    Returns:
        Dict mapping old_filename → new_filename
    """
    filename_map = {}
    path_map = {}
    
    with open(map_file, 'r') as f:
        reader = csv.DictReader(f)
        for entry in reader:
            # Map both full paths and just filenames
            filename_map[entry['old_filename']] = entry['new_filename']
            path_map[entry['old_path']] = entry['new_path']
    
    return {'filenames': filename_map, 'paths': path_map}


def find_files_to_update(root_dir: Path) -> List[Path]:
    """
    Find all files that may contain cross-references.
    
    Returns:
        List of file paths to check
    """
    extensions = {'.md', '.json', '.yaml', '.yml', '.csv', '.txt', '.html'}
    files_to_check = []
    
    excluded_dirs = {'.git', 'node_modules', '__pycache__', '.venv', 'venv', 'dist', 'build'}
    
    for path in root_dir.rglob('*'):
        if not path.is_file():
            continue
        
        # Skip excluded directories
        if any(excluded in path.parts for excluded in excluded_dirs):
            continue
        
        # Check extension
        if path.suffix in extensions:
            files_to_check.append(path)
    
    return files_to_check


def update_file_references(file_path: Path, rename_maps: Dict, dry_run: bool = False) -> Tuple[int, List[str]]:
    """
    Update cross-references in a single file.
    
    Returns:
        Tuple of (replacement_count, changed_lines)
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        # Skip binary files
        return 0, []
    
    original_content = content
    replacement_count = 0
    changed_lines = []
    
    filename_map = rename_maps['filenames']
    path_map = rename_maps['paths']
    
    # Replace full paths first (more specific)
    for old_path, new_path in path_map.items():
        if old_path in content:
            content = content.replace(old_path, new_path)
            replacement_count += content.count(new_path) - original_content.count(new_path)
            changed_lines.append(f"  Path: {old_path} → {new_path}")
    
    # Replace filenames (in links, imports, references)
    for old_filename, new_filename in filename_map.items():
        # Skip if already replaced via path
        if old_filename not in content:
            continue
        
        # Pattern 1: Markdown links [text](filename)
        pattern1 = re.compile(rf'\[([^\]]+)\]\(([^\)]*){re.escape(old_filename)}([^\)]*)\)')
        if pattern1.search(content):
            content = pattern1.sub(rf'[\1](\g<2>{new_filename}\g<3>)', content)
            replacement_count += 1
            changed_lines.append(f"  Markdown link: {old_filename} → {new_filename}")
        
        # Pattern 2: Direct filename references (with surrounding whitespace/quotes)
        pattern2 = re.compile(rf'([\s"\'\`])({re.escape(old_filename)})([\s"\'\`])')
        if pattern2.search(content):
            content = pattern2.sub(rf'\1{new_filename}\3', content)
            replacement_count += 1
            changed_lines.append(f"  Direct reference: {old_filename} → {new_filename}")
        
        # Pattern 3: In JSON/YAML values
        pattern3 = re.compile(rf'(:\s*["\'])({re.escape(old_filename)})(["\'])')
        if pattern3.search(content):
            content = pattern3.sub(rf'\1{new_filename}\3', content)
            replacement_count += 1
            changed_lines.append(f"  JSON/YAML value: {old_filename} → {new_filename}")
    
    # Write updated content if changes were made
    if content != original_content:
        if not dry_run:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
        return replacement_count, changed_lines
    
    return 0, []


def update_cross_references(root_dir: Path, rename_maps: Dict, dry_run: bool = False) -> Tuple[int, int]:
    """
    Update all cross-references in the repository.
    
    Returns:
        Tuple of (files_updated, total_replacements)
    """
    files_to_check = find_files_to_update(root_dir)
    print(f"Found {len(files_to_check)} files to check for cross-references")
    
    files_updated = 0
    total_replacements = 0
    
    for i, file_path in enumerate(files_to_check, 1):
        rel_path = file_path.relative_to(root_dir)
        
        replacement_count, changed_lines = update_file_references(file_path, rename_maps, dry_run)
        
        if replacement_count > 0:
            files_updated += 1
            total_replacements += replacement_count
            
            if dry_run:
                print(f"\n[{i}/{len(files_to_check)}] {rel_path}")
                print(f"  {replacement_count} replacements:")
                for line in changed_lines[:5]:
                    print(line)
                if len(changed_lines) > 5:
                    print(f"  ... and {len(changed_lines) - 5} more")
            else:
                if files_updated <= 20 or files_updated % 50 == 0:
                    print(f"[{i}/{len(files_to_check)}] Updated: {rel_path} ({replacement_count} replacements)")
    
    return files_updated, total_replacements


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Update cross-references after v3.0 → v4.0 rename',
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
        help='Preview updates without modifying files'
    )
    parser.add_argument(
        '--execute',
        action='store_true',
        help='Execute the updates (WARNING: modifies files!)'
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
        rename_maps = load_rename_map(map_file)
        print(f"Loaded {len(rename_maps['filenames'])} filename mappings")
        print(f"Loaded {len(rename_maps['paths'])} path mappings")
        
        # Update cross-references
        if args.dry_run:
            print("\n=== DRY RUN: Preview of cross-reference updates ===\n")
            files_updated, total_replacements = update_cross_references(root_dir, rename_maps, dry_run=True)
            
            print(f"\n{'='*60}")
            print(f"Summary (DRY RUN):")
            print(f"  Files with references: {files_updated}")
            print(f"  Total replacements:    {total_replacements}")
            print(f"{'='*60}")
            
            if files_updated > 0:
                print("\nRun with --execute to apply these changes.")
        else:
            print("\n=== EXECUTING CROSS-REFERENCE UPDATES ===")
            print("⚠️  WARNING: This will modify files in the repository!")
            print()
            
            files_updated, total_replacements = update_cross_references(root_dir, rename_maps, dry_run=False)
            
            print(f"\n{'='*60}")
            print(f"Cross-reference update complete:")
            print(f"  Files updated:       {files_updated}")
            print(f"  Total replacements:  {total_replacements}")
            print(f"{'='*60}")
            
            print("\n✅ Cross-reference updates completed!")
            print("\nNext steps:")
            print("  1. Run: git status")
            print("  2. Run: python validate_nomenclature.py --check-all")
            print("  3. Review changes and commit")
        
        return 0
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return 2


if __name__ == '__main__':
    sys.exit(main())
