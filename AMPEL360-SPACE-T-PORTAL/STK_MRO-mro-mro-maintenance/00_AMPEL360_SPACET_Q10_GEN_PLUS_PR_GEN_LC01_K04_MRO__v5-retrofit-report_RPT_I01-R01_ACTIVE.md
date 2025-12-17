---
title: "Nomenclature v5.0 Retrofit Report - MRO"
date: "2025-12-17"
status: "ACTIVE"
type: "RPT"
aor: "MRO"
---

# Nomenclature v5.0 Retrofit Report

**Portal:** STK_MRO-mro-mro-maintenance  
**AoR:** MRO  
**Date:** 2025-12-17  
**Retrofit Version:** v5.0

## Summary

This report documents the Nomenclature v5.0 retrofit execution for the MRO area of responsibility.

### Files Affected

**Total files in this AoR:** 33

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

✅ **100% compliance achieved** for MRO portal files

## Files Renamed in This Portal

### Sample Transformations

1. `00_AMPEL360_SPACET_PLUS_00_IDX_LC01_K00_MRO__stakeholder-mro-entrypoint_v01.md`
   → `00_AMPEL360_SPACET_PLUS_GEN_LC01_K04_MRO__stakeholder-mro-entrypoint_IDX_v01_ACTIVE.md`

2. `00_AMPEL360_SPACET_PLUS_00_IDX_LC01_K10_MRO__k10-industrialization-supplychain-quality_v01.md`
   → `00_AMPEL360_SPACET_PLUS_GEN_LC01_K10_MRO__k10-industrialization-supplychain-quality_IDX_v01_ACTIVE.md`

3. `00_AMPEL360_SPACET_PLUS_00_IDX_LC01_K14_MRO__k14-reliability-growth-maintenance-intervals-health_v01.md`
   → `00_AMPEL360_SPACET_PLUS_GEN_LC01_K14_MRO__k14-reliability-growth-maintenance-intervals-health_IDX_v01_ACTIVE.md`

4. `00_AMPEL360_SPACET_PLUS_00_IDX_LC01_K11_MRO__k11-human-factors-training-readiness_v01.md`
   → `00_AMPEL360_SPACET_PLUS_GEN_LC01_K11_MRO__k11-human-factors-training-readiness_IDX_v01_ACTIVE.md`

5. `10_AMPEL360_SPACET_PLUS_00_IDX_LC01_K10_MRO__k10-ata-10-tasklist_v01.md`
   → `10_AMPEL360_SPACET_PLUS_GEN_LC01_K10_MRO__k10-ata-10-tasklist_IDX_v01_ACTIVE.md`

6. `00_AMPEL360_SPACET_PLUS_00_IDX_LC01_K10_MRO__k10-ata-00-tasklist_v01.md`
   → `00_AMPEL360_SPACET_PLUS_GEN_LC01_K10_MRO__k10-ata-00-tasklist_IDX_v01_ACTIVE.md`

7. `51_AMPEL360_SPACET_PLUS_00_IDX_LC01_K10_MRO__k10-ata-51-tasklist_v01.md`
   → `51_AMPEL360_SPACET_PLUS_GEN_LC01_K10_MRO__k10-ata-51-tasklist_IDX_v01_ACTIVE.md`

8. `82_AMPEL360_SPACET_PLUS_00_IDX_LC01_K10_MRO__k10-ata-82-tasklist_v01.md`
   → `82_AMPEL360_SPACET_PLUS_GEN_LC01_K10_MRO__k10-ata-82-tasklist_IDX_v01_ACTIVE.md`

9. `70_AMPEL360_SPACET_PLUS_00_IDX_LC01_K10_MRO__k10-ata-70-tasklist_v01.md`
   → `70_AMPEL360_SPACET_PLUS_GEN_LC01_K10_MRO__k10-ata-70-tasklist_IDX_v01_ACTIVE.md`

10. `89_AMPEL360_SPACET_PLUS_00_IDX_LC01_K10_MRO__k10-ata-89-tasklist_v01.md`
   → `89_AMPEL360_SPACET_PLUS_GEN_LC01_K10_MRO__k10-ata-89-tasklist_IDX_v01_ACTIVE.md`

*...and 23 more files*


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
