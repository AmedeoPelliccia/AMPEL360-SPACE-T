# Post-Retrofit Issue Tracking

## Overview

This document tracks GitHub issues created for post-v5.0 retrofit cleanup across all STK portals.

**Status:** Issue templates generated  
**Date:** 2025-12-17  
**Related PR:** Nomenclature v5.0 Retrofit

## Issue Templates Generated

12 issue templates have been created in `.github/ISSUE_TEMPLATES/portal-retrofit/`:

| # | AoR | Portal | Files | Template |
|---|-----|--------|-------|----------|
| 1 | AI | STK_AI-ai-ai-ml-engineering | ~100 | post-retrofit-cleanup-ai.md |
| 2 | CERT | STK_CERT-cert-certification-authorities | ~180 | post-retrofit-cleanup-cert.md |
| 3 | CM | STK_CM-cm-configuration-management | 87 | post-retrofit-cleanup-cm.md |
| 4 | CY | STK_CY-cy-cybersecurity | ~80 | post-retrofit-cleanup-cy.md |
| 5 | DATA | STK_DATA-data-data-governance | ~90 | post-retrofit-cleanup-data.md |
| 6 | MRO | STK_MRO-mro-mro-maintenance | ~70 | post-retrofit-cleanup-mro.md |
| 7 | OPS | STK_OPS-ops-operations | ~85 | post-retrofit-cleanup-ops.md |
| 8 | PMO | STK_PMO-pmo-program-management-office | ~75 | post-retrofit-cleanup-pmo.md |
| 9 | SAF | STK_SAF-saf-safety | ~150 | post-retrofit-cleanup-saf.md |
| 10 | SE | STK_SE-se-systems-engineering | ~140 | post-retrofit-cleanup-se.md |
| 11 | SPACEPORT | STK_SPACEPORT-spaceport-spaceport-airport-ops | ~60 | post-retrofit-cleanup-spaceport.md |
| 12 | TEST | STK_TEST-test-ivvq-testing | ~90 | post-retrofit-cleanup-test.md |

**Total:** 12 portals tracked

## Creating Issues

### Option 1: GitHub UI (Manual)

For each portal:
1. Go to: https://github.com/AmedeoPelliccia/AMPEL360-SPACE-T/issues/new
2. Copy content from: `.github/ISSUE_TEMPLATES/portal-retrofit/post-retrofit-cleanup-<aor>.md`
3. Paste into issue description
4. Create issue
5. Link to this PR in the issue

### Option 2: GitHub CLI (Batch)

```bash
# Install GitHub CLI: https://cli.github.com/

# Create all issues at once
cd .github/ISSUE_TEMPLATES/portal-retrofit
for template in post-retrofit-cleanup-*.md; do
  echo "Creating issue from $template..."
  gh issue create \
    --body-file "$template" \
    --repo AmedeoPelliccia/AMPEL360-SPACE-T
done
```

### Option 3: Use Script

```bash
# Create issues via API (requires token)
python scripts/create_portal_issues.py --token $GITHUB_TOKEN
```

## Issue Status Tracking

Once issues are created, track them here:

| Portal | Issue # | Status | Assignee | Notes |
|--------|---------|--------|----------|-------|
| AI | TBD | Not Created | - | - |
| CERT | TBD | Not Created | - | - |
| CM | TBD | Not Created | - | - |
| CY | TBD | Not Created | - | - |
| DATA | TBD | Not Created | - | - |
| MRO | TBD | Not Created | - | - |
| OPS | TBD | Not Created | - | - |
| PMO | TBD | Not Created | - | - |
| SAF | TBD | Not Created | - | - |
| SE | TBD | Not Created | - | - |
| SPACEPORT | TBD | Not Created | - | - |
| TEST | TBD | Not Created | - | - |

**Update this table after creating issues!**

## Common Cleanup Tasks

Each issue tracks these common tasks:

1. **Review Broken Links**
   - Run link checker for the portal
   - Fix or document broken links
   - Update cross-references

2. **Update Portal Documentation**
   - Review README and index files
   - Update hardcoded references
   - Verify navigation

3. **Verify Cross-References**
   - Check inter-portal links
   - Verify ATA task references
   - Update knot cross-references

4. **Update External Documentation**
   - External docs and bookmarks
   - Stakeholder communication

## Priority & Effort

- **Priority:** Low (non-blocking)
- **Effort per portal:** 1-2 hours
- **Total effort:** 12-24 hours (can be distributed)

All cleanup is **non-blocking** - v5.0 retrofit is complete and all portals are operational.

## Resources

- **Issue Templates:** `.github/ISSUE_TEMPLATES/portal-retrofit/`
- **Link Checker:** `scripts/check_and_update_links.py`
- **Portal Reports:** `AMPEL360-SPACE-T-PORTAL/STK_*/00_AMPEL360_SPACET_Q10_GEN_PLUS_PR_GEN_LC01_K04_*__v5-retrofit-report_RPT_I01-R01_ACTIVE.md`
- **v5.0 Standard:** `docs/standards/NOMENCLATURE_v5_0.md`

## Progress Milestones

- [x] Issue templates generated (2025-12-17)
- [ ] All 12 issues created
- [ ] Issues assigned to teams
- [ ] 25% of issues completed
- [ ] 50% of issues completed
- [ ] 75% of issues completed
- [ ] 100% of issues completed and closed

---

**Last Updated:** 2025-12-17  
**Maintained by:** Configuration Management WG
