---
title: "Nomenclature v5.0 Retrofit Report - DATA"
date: "2025-12-17"
status: "ACTIVE"
type: "RPT"
aor: "DATA"
---

# Nomenclature v5.0 Retrofit Report

**Portal:** STK_DATA-data-data-governance  
**AoR:** DATA  
**Date:** 2025-12-17  
**Retrofit Version:** v5.0

## Summary

This report documents the Nomenclature v5.0 retrofit execution for the DATA area of responsibility.

### Files Affected

**Total files in this AoR:** 139

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

✅ **100% compliance achieved** for DATA portal files

## Files Renamed in This Portal

### Sample Transformations

1. `00_AMPEL360_SPACET_PLUS_00_IDX_LC01_K06_DATA__k06-evidence-pack_v01.md`
   → `00_AMPEL360_SPACET_PLUS_GEN_LC01_K06_DATA__k06-evidence-pack_IDX_v01_ACTIVE.md`

2. `00_AMPEL360_SPACET_PLUS_00_STD_LC01_K00_DATA__governance-reference-policy_v01.md`
   → `00_AMPEL360_SPACET_PLUS_GEN_LC01_K05_DATA__governance-reference-policy_STD_v01_ACTIVE.md`

3. `00_AMPEL360_SPACET_PLUS_00_MIN_LC01_K06_DATA__k06-governance-decisions_v01.md`
   → `00_AMPEL360_SPACET_PLUS_GEN_LC01_K06_DATA__k06-governance-decisions_MIN_v01_ACTIVE.md`

4. `00_AMPEL360_SPACET_GEN_90_SCH_SB90_K00_DATA__nku-ledger-schema_v01.json`
   → `00_AMPEL360_SPACET_GEN_GEN_SB90_K05_DATA__nku-ledger-schema_SCH_v01_ACTIVE.json`

5. `00_AMPEL360_SPACET_GEN_90_SCH_SB90_K00_DATA__knots-data-structure_v01.json`
   → `00_AMPEL360_SPACET_GEN_GEN_SB90_K05_DATA__knots-data-structure_SCH_v01_ACTIVE.json`

6. `00_AMPEL360_SPACET_PLUS_00_STD_LC01_K00_DATA__identifier-grammar_v01.md`
   → `00_AMPEL360_SPACET_PLUS_GEN_LC01_K05_DATA__identifier-grammar_STD_v01_ACTIVE.md`

7. `00_AMPEL360_SPACET_PLUS_00_IDX_LC01_K00_DATA__ci-governance-gates_v01.md`
   → `00_AMPEL360_SPACET_PLUS_GEN_LC01_K05_DATA__ci-governance-gates_IDX_v01_ACTIVE.md`

8. `00_AMPEL360_SPACET_PLUS_00_LOG_LC01_K06_DATA__k06-approvals_v01.md`
   → `00_AMPEL360_SPACET_PLUS_GEN_LC01_K06_DATA__k06-approvals_LOG_v01_ACTIVE.md`

9. `00_AMPEL360_SPACET_PLUS_00_STD_LC01_K00_DATA__ssot-decision-matrix_v01.md`
   → `00_AMPEL360_SPACET_PLUS_GEN_LC01_K05_DATA__ssot-decision-matrix_STD_v01_ACTIVE.md`

10. `00_AMPEL360_SPACET_PLUS_00_TAB_LC01_K00_DATA__knot-register_v01.csv`
   → `00_AMPEL360_SPACET_PLUS_GEN_LC01_K05_DATA__knot-register_TAB_v01_ACTIVE.csv`

*...and 129 more files*


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
