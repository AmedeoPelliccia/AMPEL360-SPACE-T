---
title: "Nomenclature v5.0 Retrofit Report - TEST"
date: "2025-12-17"
status: "ACTIVE"
type: "RPT"
aor: "TEST"
---

# Nomenclature v5.0 Retrofit Report

**Portal:** STK_TEST-test-ivvq-testing  
**AoR:** TEST  
**Date:** 2025-12-17  
**Retrofit Version:** v5.0

## Summary

This report documents the Nomenclature v5.0 retrofit execution for the TEST area of responsibility.

### Files Affected

**Total files in this AoR:** 116

### Key Transformations

All files in this portal have been migrated to Nomenclature v5.0 with the following changes:

1. **BUCKET → BLOCK mapping**
   - Semantic domain classification applied
   - BUCKET codes replaced with intuitive BLOCK codes

2. **KNOT governance (K00 → K01-K14)**
   - Strict K01-K14 enforcement
   - K00 mapped to appropriate knots based on context

3. **STATUS field added**
   - All files assigned lifecycle status (ACTIVE/DRAFT/TEMPLATE)

4. **Field reordering**
   - Updated to v5.0 canonical format
   - Added mandatory double underscore `__` separator

## v5.0 Canonical Format

```
[ATA_ROOT]_[PROJECT]_[PROGRAM]_[VARIANT]_[BLOCK]_[PHASE]_[KNOT_TASK]_[AoR]__[SUBJECT]_[TYPE]_[VERSION]_[STATUS].[EXT]
```

## Validation Status

✅ **100% compliance achieved** for TEST portal files

## Files Renamed in This Portal

### Sample Transformations

1. `00_AMPEL360_SPACET_PLUS_00_IDX_LC01_K00_TEST__stakeholder-test-entrypoint_v01.md`
   → `00_AMPEL360_SPACET_PLUS_GEN_LC01_K04_TEST__stakeholder-test-entrypoint_IDX_v01_ACTIVE.md`

2. `100_AMPEL360_SPACET_PLUS_00_IDX_LC01_K01_CERT__k01-ata-100-nav_v01.md`
   → `100_AMPEL360_SPACET_PLUS_GEN_LC01_K01_CERT__k01-ata-100-nav_IDX_v01_ACTIVE.md`

3. `100_AMPEL360_SPACET_PLUS_00_IDX_LC01_K01_CERT__k01-ata-100-tasklist_v01.md`
   → `100_AMPEL360_SPACET_PLUS_GEN_LC01_K01_CERT__k01-ata-100-tasklist_IDX_v01_ACTIVE.md`

4. `106_AMPEL360_SPACET_PLUS_00_IDX_LC01_K01_CERT__k01-ata-106-tasklist_v01.md`
   → `106_AMPEL360_SPACET_PLUS_GEN_LC01_K01_CERT__k01-ata-106-tasklist_IDX_v01_ACTIVE.md`

5. `106_AMPEL360_SPACET_PLUS_00_IDX_LC01_K01_CERT__k01-ata-106-nav_v01.md`
   → `106_AMPEL360_SPACET_PLUS_GEN_LC01_K01_CERT__k01-ata-106-nav_IDX_v01_ACTIVE.md`

6. `112_AMPEL360_SPACET_PLUS_00_IDX_LC01_K01_CERT__k01-ata-112-nav_v01.md`
   → `112_AMPEL360_SPACET_PLUS_GEN_LC01_K01_CERT__k01-ata-112-nav_IDX_v01_ACTIVE.md`

7. `112_AMPEL360_SPACET_PLUS_00_IDX_LC01_K01_CERT__k01-ata-112-tasklist_v01.md`
   → `112_AMPEL360_SPACET_PLUS_GEN_LC01_K01_CERT__k01-ata-112-tasklist_IDX_v01_ACTIVE.md`

8. `115_AMPEL360_SPACET_PLUS_00_IDX_LC01_K01_CERT__k01-ata-115-tasklist_v01.md`
   → `115_AMPEL360_SPACET_PLUS_GEN_LC01_K01_CERT__k01-ata-115-tasklist_IDX_v01_ACTIVE.md`

9. `115_AMPEL360_SPACET_PLUS_00_IDX_LC01_K01_CERT__k01-ata-115-nav_v01.md`
   → `115_AMPEL360_SPACET_PLUS_GEN_LC01_K01_CERT__k01-ata-115-nav_IDX_v01_ACTIVE.md`

10. `110_AMPEL360_SPACET_PLUS_00_IDX_LC01_K01_CERT__k01-ata-110-tasklist_v01.md`
   → `110_AMPEL360_SPACET_PLUS_GEN_LC01_K01_CERT__k01-ata-110-tasklist_IDX_v01_ACTIVE.md`

*...and 106 more files*


## Breaking Changes

### For Developers
- Update any hardcoded file references to new v5.0 format
- Update bookmarks and documentation links
- Use validator for new file creation: `python validate_nomenclature.py <filename>`

### For Stakeholders
- All internal links have been updated automatically
- External references may need manual update
- Contact CM team for questions: Configuration Management WG

## Resources

- **Standard:** `docs/standards/NOMENCLATURE_v5_0.md`
- **Quick Reference:** `docs/standards/NOMENCLATURE_v5_0_QUICKREF.md`
- **Config:** `config/nomenclature/v5_0.yaml`
- **Validator:** `validate_nomenclature.py`
- **Scaffold:** `scripts/scaffold.py`

## Support

For questions or issues related to this retrofit:
- Open an issue in the repository
- Contact Configuration Management WG
- Review the implementation summary: `docs/standards/NOMENCLATURE_v5_0_IMPLEMENTATION_SUMMARY.md`

---

**Generated:** 2025-12-17  
**Retrofit Status:** COMPLETE  
**Validation:** 100% COMPLIANT
