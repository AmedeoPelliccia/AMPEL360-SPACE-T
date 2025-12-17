# Portal Post-Retrofit Cleanup Issues

This directory contains GitHub issue templates for tracking post-retrofit cleanup tasks
for each STK portal after the Nomenclature v5.0 migration.

## Generated Templates

1. **AI** - `post-retrofit-cleanup-ai.md`
2. **CERT** - `post-retrofit-cleanup-cert.md`
3. **CM** - `post-retrofit-cleanup-cm.md`
4. **CY** - `post-retrofit-cleanup-cy.md`
5. **DATA** - `post-retrofit-cleanup-data.md`
6. **MRO** - `post-retrofit-cleanup-mro.md`
7. **OPS** - `post-retrofit-cleanup-ops.md`
8. **PMO** - `post-retrofit-cleanup-pmo.md`
9. **SAF** - `post-retrofit-cleanup-saf.md`
10. **SE** - `post-retrofit-cleanup-se.md`
11. **SPACEPORT** - `post-retrofit-cleanup-spaceport.md`
12. **TEST** - `post-retrofit-cleanup-test.md`

## Total Templates: 12

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
