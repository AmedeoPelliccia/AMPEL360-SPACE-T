#!/usr/bin/env python3
"""
Generate GitHub Issue Templates for Portal Retrofit Follow-up
==============================================================

Creates issue template files for each STK portal documenting remaining
problems after v5.0 retrofit.

Usage:
    python scripts/generate_portal_issues.py
"""

import csv
import json
from pathlib import Path
from collections import defaultdict


def load_rename_map():
    """Load rename map."""
    entries = []
    with open('rename_map_v5.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            entries.append(row)
    return entries


def get_portal_data():
    """Get portal directories and their AoRs."""
    portal_base = Path("AMPEL360-SPACE-T-PORTAL")
    portals = []
    
    if portal_base.exists():
        for stk_dir in sorted(portal_base.iterdir()):
            if stk_dir.is_dir() and stk_dir.name.startswith('STK_'):
                # Extract AoR from directory name
                dir_parts = stk_dir.name.split('-')
                if len(dir_parts) >= 2:
                    aor = dir_parts[0].replace('STK_', '')
                    portals.append({
                        'aor': aor,
                        'dir': stk_dir.name,
                        'path': stk_dir
                    })
    
    return portals


def generate_issue_template(portal, rename_map):
    """Generate issue template for a portal."""
    aor = portal['aor']
    dir_name = portal['dir']
    
    # Count files in this portal
    files_in_portal = [
        entry for entry in rename_map
        if aor in entry['new_path'] or aor.lower() in entry['new_path'].lower()
    ]
    
    issue_content = f"""---
name: Post-Retrofit Cleanup for {aor}
about: Track remaining issues after v5.0 nomenclature retrofit in {dir_name}
title: "[{aor}] Post-v5.0 Retrofit Cleanup"
labels: nomenclature-v5.0, cleanup, {aor.lower()}
assignees: ''
---

## Portal Information

**AoR:** {aor}  
**Portal Directory:** `{dir_name}`  
**Report:** `{portal['path'].name}/00_AMPEL360_SPACET_PLUS_GEN_LC01_K04_{aor}__v5-retrofit-report_RPT_v01_ACTIVE.md`

## Context

This issue tracks remaining cleanup tasks after the Nomenclature v5.0 retrofit for the **{aor}** area of responsibility. All files in this portal have been successfully migrated to v5.0 format with 100% validation compliance, but some cross-references and links require manual review.

## Retrofit Summary

- **Files migrated:** {len(files_in_portal)} files in this AoR
- **Validation status:** ✅ 100% compliant
- **Retrofit date:** 2025-12-17

## Remaining Tasks

### 1. Review Broken Links

**Action Required:**
- Review broken internal links in files within this portal
- Fix or remove links to non-existent files
- Update links to external resources if needed

**How to Check:**
```bash
cd AMPEL360-SPACE-T-PORTAL/{dir_name}
python ../../scripts/check_and_update_links.py --check-only
```

### 2. Update Portal-Specific Documentation

**Action Required:**
- Review portal README and index files
- Update any hardcoded file references
- Verify all internal navigation works correctly

**Files to Check:**
- Portal README files
- Index files (TYPE: IDX)
- Navigation manifests

### 3. Verify Cross-References

**Action Required:**
- Check links between this portal and other portals
- Verify ATA task references are correct
- Update knot cross-references if needed

### 4. Update External Documentation

**Action Required:**
- Update any external documentation referencing this portal
- Update bookmarks and saved links
- Communicate changes to stakeholders

## Link Checker Results

From automated link checking:
- **Fixable links:** Automatically updated where possible
- **Unfixable links:** Require manual review (see link checker output)

**To generate detailed report:**
```bash
cd AMPEL360-SPACE-T-PORTAL/{dir_name}
python ../../scripts/check_and_update_links.py --check-only > link-check-report.txt
```

## Resources

- **v5.0 Standard:** `docs/standards/NOMENCLATURE_v5_0.md`
- **Quick Reference:** `docs/standards/NOMENCLATURE_v5_0_QUICKREF.md`
- **Retrofit Guide:** `docs/standards/NOMENCLATURE_v5_0_RETROFIT_GUIDE.md`
- **Portal Report:** See report file listed above
- **Validator:** `python validate_nomenclature.py <filename>`

## Acceptance Criteria

- [ ] All broken links reviewed and fixed or documented
- [ ] Portal documentation updated with v5.0 references
- [ ] Cross-references to other portals verified
- [ ] External documentation updated
- [ ] Link checker reports 0 critical broken links in this portal
- [ ] Portal navigation fully functional

## Notes

This cleanup is **non-blocking** for v5.0 adoption. All files are already compliant and the portal is fully operational. This issue tracks quality improvements and cross-reference cleanup.

**Priority:** Low (Quality of Life improvement)  
**Estimated Effort:** 1-2 hours

---

**Related Issues:**
- Main retrofit PR: #{'{'}PR_NUMBER{'}'}
- Other portal cleanup issues: See issues labeled `nomenclature-v5.0, cleanup`

**Assigned Workspace:** `{dir_name}`
"""
    
    return issue_content


def main():
    """Generate issue templates for all portals."""
    print("Generating GitHub issue templates for portal retrofits...")
    
    # Load data
    rename_map = load_rename_map()
    portals = get_portal_data()
    
    if not portals:
        print("Error: No portal directories found")
        return 1
    
    # Create issues directory
    issues_dir = Path(".github/ISSUE_TEMPLATES/portal-retrofit")
    issues_dir.mkdir(parents=True, exist_ok=True)
    
    # Generate templates
    generated = []
    for portal in portals:
        aor = portal['aor']
        template_file = issues_dir / f"post-retrofit-cleanup-{aor.lower()}.md"
        
        content = generate_issue_template(portal, rename_map)
        template_file.write_text(content, encoding='utf-8')
        
        generated.append(template_file)
        print(f"  ✓ Generated: {template_file}")
    
    # Create index file
    index_content = f"""# Portal Post-Retrofit Cleanup Issues

This directory contains GitHub issue templates for tracking post-retrofit cleanup tasks
for each STK portal after the Nomenclature v5.0 migration.

## Generated Templates

"""
    for i, portal in enumerate(portals, 1):
        aor = portal['aor']
        index_content += f"{i}. **{aor}** - `post-retrofit-cleanup-{aor.lower()}.md`\n"
    
    index_content += f"""
## Total Templates: {len(portals)}

## How to Use These Templates

### Option 1: Create Issues via GitHub UI
1. Go to repository Issues → New Issue
2. Copy content from template file
3. Create issue

### Option 2: Create Issues via Script (requires gh CLI)
```bash
# Install GitHub CLI if needed
# https://cli.github.com/

# Create all issues at once
for template in .github/ISSUE_TEMPLATES/portal-retrofit/*.md; do
  gh issue create --body-file "$template" --repo AmedeoPelliccia/AMPEL360-SPACE-T
done
```

### Option 3: Manual Creation
Copy the template content and create issues manually for each portal.

## Issue Organization

All issues are labeled with:
- `nomenclature-v5.0` - Links to v5.0 retrofit effort
- `cleanup` - Post-migration cleanup work
- `<aor>` - Specific AoR (e.g., `cm`, `cert`, `saf`)

## Priority

All post-retrofit cleanup issues are **Low Priority** and **non-blocking**. The v5.0
retrofit is complete and all portals are fully operational. These issues track quality
improvements and cross-reference cleanup only.

---

**Generated:** 2025-12-17  
**Related PR:** Nomenclature v5.0 Retrofit
"""
    
    index_file = issues_dir / "README.md"
    index_file.write_text(index_content, encoding='utf-8')
    print(f"  ✓ Generated index: {index_file}")
    
    # Generate summary
    print(f"\n{'='*70}")
    print(f"Generated {len(generated)} issue templates")
    print(f"{'='*70}\n")
    
    print("Issue templates created in:")
    print(f"  {issues_dir}/")
    print()
    print("Next steps:")
    print("  1. Review templates in .github/ISSUE_TEMPLATES/portal-retrofit/")
    print("  2. Create issues via GitHub UI or gh CLI")
    print("  3. Assign to appropriate team members")
    print("  4. Track cleanup progress per portal")
    print()
    
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main())
