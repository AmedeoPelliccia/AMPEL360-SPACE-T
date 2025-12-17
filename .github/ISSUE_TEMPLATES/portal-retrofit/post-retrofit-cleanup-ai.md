---
name: Post-Retrofit Cleanup for AI
about: Track remaining issues after v5.0 nomenclature retrofit in STK_AI-ai-ai-ml-engineering
title: "[AI] Post-v5.0 Retrofit Cleanup"
labels: nomenclature-v5.0, cleanup, ai
assignees: ''
---

## Portal Information

**AoR:** AI  
**Portal Directory:** `STK_AI-ai-ai-ml-engineering`  
**Report:** `STK_AI-ai-ai-ml-engineering/00_AMPEL360_SPACET_Q10_GEN_PLUS_PR_GEN_LC01_K04_AI__v5-retrofit-report_RPT_I01-R01_ACTIVE.md`

## Context

This issue tracks remaining cleanup tasks after the Nomenclature v5.0 retrofit for the **AI** area of responsibility. All files in this portal have been successfully migrated to v5.0 format with 100% validation compliance, but some cross-references and links require manual review.

## Retrofit Summary

- **Files migrated:** 294 files in this AoR
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
cd AMPEL360-SPACE-T-PORTAL/STK_AI-ai-ai-ml-engineering
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
cd AMPEL360-SPACE-T-PORTAL/STK_AI-ai-ai-ml-engineering
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
- Main retrofit PR: #{PR_NUMBER}
- Other portal cleanup issues: See issues labeled `nomenclature-v5.0, cleanup`

**Assigned Workspace:** `STK_AI-ai-ai-ml-engineering`
