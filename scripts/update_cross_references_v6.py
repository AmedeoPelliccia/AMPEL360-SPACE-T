#!/usr/bin/env python3
"""
AMPEL360 Space-T Cross-Reference Updater v6.0
==============================================

Updates cross-references after batch rename operation.

Handles:
- Markdown links: [text](path), [text](file.md)
- Relative file references
- JSON/YAML manifest paths
- Portal index files
- Knot index files

Usage:
    python scripts/update_cross_references_v6.py --map rename_map_v6.csv --dry-run
    python scripts/update_cross_references_v6.py --map rename_map_v6.csv --execute
"""

import argparse
import csv
import re
import sys
import json
from pathlib import Path
from typing import Dict, List, Tuple, Set


def load_rename_map(csv_path: Path) -> Dict[str, str]:
    """
    Load rename map from CSV into lookup dictionaries.
    
    Returns:
        Dict with 'paths' and 'filenames' mappings
    """
    path_map = {}
    filename_map = {}
    
    with open(csv_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            old_path = row['old_path']
            new_path = row['new_path']
            
            # Full path mapping
            path_map[old_path] = new_path
            
            # Filename-only mapping
            old_filename = Path(old_path).name
            new_filename = Path(new_path).name
            filename_map[old_filename] = new_filename
    
    return {'paths': path_map, 'filenames': filename_map}


def find_files_to_update(root_dir: Path) -> List[Path]:
    """
    Find all files that may contain cross-references.
    
    Returns:
        List of file paths to check
    """
    extensions = {'.md', '.json', '.yaml', '.yml', '.csv', '.txt'}
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


def update_markdown_content(
    content: str,
    path_map: Dict[str, str],
    filename_map: Dict[str, str],
    file_path: Path
) -> Tuple[str, int, List[str]]:
    """
    Update markdown links and references.
    
    Returns: (updated_content, replacement_count, changes_list)
    """
    updated_content = content
    replacement_count = 0
    changes = []
    
    # Pattern for markdown links: [text](path)
    link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
    
    def replace_link(match):
        nonlocal replacement_count, changes
        link_text = match.group(1)
        link_path = match.group(2)
        
        # Skip external links
        if link_path.startswith(('http://', 'https://', '#', 'mailto:')):
            return match.group(0)
        
        # Try full path match first
        if link_path in path_map:
            new_link_path = path_map[link_path]
            replacement_count += 1
            changes.append(f"  Link: [{link_text}]({link_path}) → [{link_text}]({new_link_path})")
            return f"[{link_text}]({new_link_path})"
        
        # Try filename-only match
        link_filename = Path(link_path).name
        if link_filename in filename_map:
            new_filename = filename_map[link_filename]
            # Preserve directory structure
            new_link_path = str(Path(link_path).parent / new_filename)
            if new_link_path == '.':
                new_link_path = new_filename
            replacement_count += 1
            changes.append(f"  Link: [{link_text}]({link_path}) → [{link_text}]({new_link_path})")
            return f"[{link_text}]({new_link_path})"
        
        return match.group(0)
    
    updated_content = link_pattern.sub(replace_link, updated_content)
    
    # Also handle plain file references (not in links)
    # Be careful to avoid false positives
    for old_path, new_path in path_map.items():
        # Only replace if it's a standalone reference (surrounded by whitespace or quotes)
        pattern = re.compile(r'(["\s`])(' + re.escape(old_path) + r')(["\s`])')
        
        def replace_plain(match):
            nonlocal replacement_count, changes
            replacement_count += 1
            changes.append(f"  Plain ref: {old_path} → {new_path}")
            return f"{match.group(1)}{new_path}{match.group(3)}"
        
        updated_content = pattern.sub(replace_plain, updated_content)
    
    return updated_content, replacement_count, changes


def update_json_content(
    content: str,
    path_map: Dict[str, str],
    filename_map: Dict[str, str]
) -> Tuple[str, int, List[str]]:
    """
    Update JSON/YAML path references.
    
    Returns: (updated_content, replacement_count, changes_list)
    """
    updated_content = content
    replacement_count = 0
    changes = []
    
    # Replace full paths in JSON strings
    for old_path, new_path in path_map.items():
        if old_path in updated_content:
            count_before = updated_content.count(old_path)
            updated_content = updated_content.replace(old_path, new_path)
            count_after = updated_content.count(new_path)
            if count_after > 0:
                replacement_count += count_before
                changes.append(f"  JSON path: {old_path} → {new_path} ({count_before} occurrences)")
    
    # Replace filenames in JSON strings
    for old_filename, new_filename in filename_map.items():
        # Use word boundaries to avoid partial matches
        pattern = re.compile(r'(["\s])' + re.escape(old_filename) + r'(["\s,}])')
        
        def replace_json_filename(match):
            nonlocal replacement_count, changes
            replacement_count += 1
            changes.append(f"  JSON filename: {old_filename} → {new_filename}")
            return f"{match.group(1)}{new_filename}{match.group(2)}"
        
        updated_content = pattern.sub(replace_json_filename, updated_content)
    
    return updated_content, replacement_count, changes


def update_file(
    file_path: Path,
    rename_maps: Dict[str, Dict[str, str]],
    dry_run: bool = False
) -> Tuple[bool, int, List[str]]:
    """
    Update cross-references in a single file.
    
    Returns: (was_modified, replacement_count, changes_list)
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            original_content = f.read()
    except UnicodeDecodeError:
        # Skip binary files
        return False, 0, []
    except Exception as e:
        print(f"  ⚠ Error reading {file_path}: {e}")
        return False, 0, []
    
    path_map = rename_maps['paths']
    filename_map = rename_maps['filenames']
    
    # Update based on file type
    if file_path.suffix == '.md':
        updated_content, replacement_count, changes = update_markdown_content(
            original_content, path_map, filename_map, file_path
        )
    elif file_path.suffix in {'.json', '.yaml', '.yml'}:
        updated_content, replacement_count, changes = update_json_content(
            original_content, path_map, filename_map
        )
    else:
        # Generic text replacement
        updated_content, replacement_count, changes = update_json_content(
            original_content, path_map, filename_map
        )
    
    # Check if content changed
    if updated_content == original_content:
        return False, 0, []
    
    if not dry_run:
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
        except Exception as e:
            print(f"  ⚠ Error writing {file_path}: {e}")
            return False, 0, []
    
    return True, replacement_count, changes


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Update cross-references after nomenclature rename',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Dry-run (preview changes)
  %(prog)s --map rename_map_v6.csv --dry-run

  # Execute updates
  %(prog)s --map rename_map_v6.csv --execute
  
  # Verbose output
  %(prog)s --map rename_map_v6.csv --execute --verbose
        """
    )
    
    parser.add_argument(
        '--map',
        default='rename_map_v6.csv',
        help='Path to rename map CSV (default: rename_map_v6.csv)'
    )
    parser.add_argument(
        '--execute',
        action='store_true',
        help='Execute updates (default is dry-run)'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Preview changes without executing (default)'
    )
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Show detailed changes'
    )
    
    args = parser.parse_args()
    
    # Determine mode
    dry_run = not args.execute or args.dry_run
    
    # Load rename map
    map_path = Path(args.map)
    if not map_path.exists():
        print(f"Error: Rename map not found: {map_path}", file=sys.stderr)
        print(f"Run: python scripts/generate_rename_map_v6.py", file=sys.stderr)
        return 2
    
    print("=" * 70)
    print("Cross-Reference Updater v6.0")
    print("=" * 70)
    print(f"Rename map: {map_path}")
    print(f"Mode: {'DRY-RUN' if dry_run else 'EXECUTE'}")
    print("=" * 70)
    print()
    
    print(f"Loading rename map from {map_path}...")
    rename_maps = load_rename_map(map_path)
    print(f"Loaded {len(rename_maps['paths'])} path mappings")
    print(f"Loaded {len(rename_maps['filenames'])} filename mappings")
    print()
    
    # Find files to update
    print("Scanning for files with potential cross-references...")
    files_to_check = find_files_to_update(Path('.'))
    print(f"Found {len(files_to_check)} files to check")
    print()
    
    # Update files
    print("Updating cross-references...")
    files_modified = 0
    total_replacements = 0
    
    for file_path in files_to_check:
        was_modified, replacement_count, changes = update_file(
            file_path, rename_maps, dry_run
        )
        
        if was_modified:
            files_modified += 1
            total_replacements += replacement_count
            print(f"  {'[DRY-RUN] ' if dry_run else ''}✓ Updated {file_path} ({replacement_count} replacements)")
            
            if args.verbose and changes:
                for change in changes:
                    print(change)
    
    # Print summary
    print()
    print("=" * 70)
    print("Update Summary")
    print("=" * 70)
    print(f"Files checked: {len(files_to_check)}")
    print(f"Files modified: {files_modified}")
    print(f"Total replacements: {total_replacements}")
    print("=" * 70)
    print()
    
    if dry_run:
        print("ℹ  Dry-run completed. Use --execute to apply changes.")
    elif files_modified > 0:
        print("✅ Cross-references updated successfully!")
        print()
        print("Next steps:")
        print("  1. Review changes: git diff")
        print("  2. Run validator: python validate_nomenclature.py --check-all")
        print("  3. Commit changes if satisfied")
    else:
        print("ℹ  No cross-references needed updating.")
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
