#!/usr/bin/env python3
"""
Quick Link Updater for v5.0 Retrofit
=====================================

Quickly updates the most common broken links in key files.
"""

import csv
import re
from pathlib import Path


def load_rename_map():
    """Load rename map."""
    old_to_new = {}
    with open('rename_map_v5.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            old_to_new[row['old_path']] = row['new_path']
    return old_to_new


def update_file(filepath, old_to_new):
    """Update a single file."""
    try:
        content = Path(filepath).read_text(encoding='utf-8', errors='ignore')
        original = content
        
        # Update direct filename references
        for old_path, new_path in old_to_new.items():
            old_name = Path(old_path).name
            new_name = Path(new_path).name
            
            # Update Markdown links
            content = re.sub(
                rf'\[([^\]]+)\]\({re.escape(old_name)}\)',
                rf'[\1]({new_name})',
                content
            )
            content = re.sub(
                rf'\[([^\]]+)\]\({re.escape(old_path)}\)',
                rf'[\1]({new_path})',
                content
            )
        
        if content != original:
            Path(filepath).write_text(content, encoding='utf-8')
            return True
    except Exception as e:
        print(f"Error updating {filepath}: {e}")
    return False


def main():
    """Update key files."""
    print("Loading rename map...")
    old_to_new = load_rename_map()
    
    # Key files to update
    key_files = [
        'README.md',
        '00_AMPEL360_SPACET_PLUS_GEN_LC01_K04_CM__nomenclature-automation-guide_IDX_v04_ACTIVE.md',
        '00_AMPEL360_SPACET_PLUS_GEN_LC01_K04_CM__nomenclature-quick-reference_CAT_v04_ACTIVE.md',
        'AMPEL360-SPACE-T-PORTAL/README.md',
        'AMPEL360-SPACE-T-PORTAL/00_AMPEL360_SPACET_PLUS_GEN_LC01_K04_CM__stakeholder-entrypoints_IDX_v01_ACTIVE.md',
    ]
    
    updated = 0
    for filepath in key_files:
        if Path(filepath).exists():
            if update_file(filepath, old_to_new):
                print(f"✓ Updated: {filepath}")
                updated += 1
        else:
            print(f"✗ Not found: {filepath}")
    
    print(f"\nUpdated {updated} file(s)")


if __name__ == '__main__':
    main()
