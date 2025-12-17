#!/usr/bin/env python3
"""
Update Cross-References for v5.0 → v6.0 R1.0 Migration
======================================================
Version: 6.0
Date: 2025-12-17

Updates all cross-references (links, imports, manifests) after rename.

Usage:
    python scripts/update_cross_references_v6.py --map rename_map_v6.csv --dry-run
    python scripts/update_cross_references_v6.py --map rename_map_v6.csv --execute
"""

import argparse
import csv
import re
import sys
from pathlib import Path
from typing import List, Dict, Set, Tuple


def load_rename_map(map_file: Path) -> Tuple[Dict[str, str], Dict[str, str]]:
    """
    Load rename map from CSV into lookup dictionaries.
    
    Returns:
        Tuple of (filename_map, path_map)
        - filename_map: Dict mapping old_filename → new_filename
        - path_map: Dict mapping old_path → new_path
    """
    filename_map = {}
    path_map = {}
    
    with open(map_file, 'r') as f:
        reader = csv.DictReader(f)
        for entry in reader:
            old_path = entry['old_path']
            new_path = entry['new_path']
            
            # Map full paths
            path_map[old_path] = new_path
            
            # Map just filenames
            old_filename = Path(old_path).name
            new_filename = Path(new_path).name
            filename_map[old_filename] = new_filename
    
    return filename_map, path_map


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


def update_file_references(file_path: Path, filename_map: Dict[str, str], path_map: Dict[str, str], dry_run: bool = False) -> Tuple[int, List[str]]:
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
    
    # Replace full paths first (more specific)
    for old_path, new_path in path_map.items():
        if old_path in content:
            count_before = content.count(old_path)
            content = content.replace(old_path, new_path)
            count_after = content.count(new_path) - original_content.count(new_path)
            if count_after > 0:
                replacement_count += count_after
                changed_lines.append(f"  Path: {old_path} → {new_path} ({count_after} occurrences)")
    
    # Replace filenames (in links, imports, references)
    for old_filename, new_filename in filename_map.items():
        # Skip if already replaced via path
        if old_filename not in content:
            continue
        
        # Be careful to only replace actual references, not substrings
        # Match markdown links: [text](filename)
        pattern_md_link = r'\[([^\]]+)\]\(' + re.escape(old_filename) + r'(#[^\)]*?)?\)'
        replacement_md = r'[\1](' + new_filename + r'\2)'
        new_content, count = re.subn(pattern_md_link, replacement_md, content)
        if count > 0:
            content = new_content
            replacement_count += count
            changed_lines.append(f"  MD link: {old_filename} → {new_filename} ({count} occurrences)")
        
        # Match file references in various contexts
        # Pattern: filename at word boundary or after specific chars (/, ", ', space)
        pattern_ref = r'([\s"\'/])' + re.escape(old_filename) + r'(?=[\s"\',\)\]]|$)'
        replacement_ref = r'\1' + new_filename
        new_content, count = re.subn(pattern_ref, replacement_ref, content)
        if count > 0:
            content = new_content
            replacement_count += count
            changed_lines.append(f"  Reference: {old_filename} → {new_filename} ({count} occurrences)")
    
    # Write changes if any
    if content != original_content and not dry_run:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
    
    return replacement_count, changed_lines


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description='Update cross-references for v5.0 → v6.0 R1.0 migration')
    parser.add_argument('--map', type=str, required=True,
                        help='Rename map CSV file')
    parser.add_argument('--directory', type=str, default='.',
                        help='Root directory to scan (default: current directory)')
    parser.add_argument('--dry-run', action='store_true',
                        help='Dry-run mode (show what would be changed)')
    parser.add_argument('--execute', action='store_true',
                        help='Execute the updates')
    
    args = parser.parse_args()
    
    if not args.dry_run and not args.execute:
        print("Error: Must specify either --dry-run or --execute")
        return 1
    
    print("="*70)
    print("AMPEL360 Space-T Cross-Reference Updater (v5.0 → v6.0 R1.0)")
    print("="*70)
    print(f"Rename map: {args.map}")
    print(f"Directory: {args.directory}")
    print(f"Mode: {'DRY-RUN' if args.dry_run else 'EXECUTE'}")
    print()
    
    # Load rename map
    print("Loading rename map...")
    try:
        map_file = Path(args.map)
        filename_map, path_map = load_rename_map(map_file)
        print(f"  Loaded {len(filename_map)} filename mappings")
        print(f"  Loaded {len(path_map)} path mappings")
    except FileNotFoundError:
        print(f"Error: Rename map file not found: {args.map}")
        return 1
    except Exception as e:
        print(f"Error loading rename map: {e}")
        return 1
    
    # Find files to update
    print("\nScanning for files to update...")
    root_dir = Path(args.directory).resolve()
    files_to_check = find_files_to_update(root_dir)
    print(f"  Found {len(files_to_check)} files to check")
    
    # Process files
    print(f"\n{'='*70}")
    print("Processing files...")
    print(f"{'='*70}\n")
    
    total_files_changed = 0
    total_replacements = 0
    
    for file_path in files_to_check:
        replacement_count, changed_lines = update_file_references(
            file_path, filename_map, path_map, dry_run=args.dry_run
        )
        
        if replacement_count > 0:
            total_files_changed += 1
            total_replacements += replacement_count
            rel_path = file_path.relative_to(root_dir)
            print(f"✏️  {rel_path} ({replacement_count} replacements)")
            for line in changed_lines:
                print(line)
            print()
    
    # Final summary
    print(f"{'='*70}")
    print(f"Summary")
    print(f"{'='*70}")
    print(f"Files checked: {len(files_to_check)}")
    print(f"Files modified: {total_files_changed}")
    print(f"Total replacements: {total_replacements}")
    print(f"{'='*70}")
    
    if args.dry_run:
        print("\n✅ Dry-run complete. Use --execute to perform actual updates.")
    else:
        print("\n✅ Cross-reference update complete.")
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
