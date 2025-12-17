# AMPEL360 Space-T Nomenclature Inventory Report

**Generated:** 2025-12-17
**Repository:** /home/runner/work/AMPEL360-SPACE-T/AMPEL360-SPACE-T

---

## Executive Summary

- **Total files scanned:** 1415
- **v5.0 compliant:** 1415 (100.0%)
- **v5.0 violations:** 0 (0.0%)
- **R1.0 compliant:** 0 (0.0%)
- **R1.0 violations:** 1415 (100.0%)
- **Estimated renames for R1.0:** ~1415 files

## v5.0 Violations by Category

✅ No v5.0 violations detected!

## R1.0 Violations by Category

| Category | Count | Files |
|----------|-------|-------|
| Pattern Mismatch | 1405 | 45_AMPEL360_SPACET_PLUS_GEN_LC01_K14_OPS__k14-ata-45-tasklist_IDX_v01_ACTIVE.md, 82_AMPEL360_SPACET_PLUS_GEN_LC01_K10_MRO__k10-ata-82-tasklist_IDX_v01_ACTIVE.md, 51_AMPEL360_SPACET_PLUS_GEN_LC01_K10_TEST__k10-ata-51-tasklist_IDX_v01_ACTIVE.md ... (+1402 more) |

## Top Offenders

Files with the most violations:

✅ No violations!

## v5.0 → R1.0 Migration Strategy

### Required Changes

1. **Add MODEL field** (after PROGRAM)
   - Default: `GEN` for generic artifacts
   - Use `Q10` for SPACE-T specific (10 passengers)
   - Use `Q100` for AIR-T specific (100 passengers)

2. **Update VERSION format**
   - `v01` → `BL01` (baseline)
   - `v02` → `BL02` (baseline)
   - Use `TS##` for testing versions
   - Use `GN##` for generated versions

3. **Add ISSUE-REVISION field** (before STATUS)
   - Default: `I00-R00` for non-issue artifacts
   - Use actual issue numbers where applicable

### Example Mappings

```
v5.0:
  00_AMPEL360_SPACET_PLUS_GEN_LC01_K04_CM__nomenclature-standard_STD_v01_ACTIVE.md

R1.0:
  00_AMPEL360_SPACET_GEN_PLUS_BL01_GEN_LC01_K04_CM__nomenclature-standard_STD_I00-R00_ACTIVE.md
  └─ Added: MODEL=GEN, VERSION=BL01 (was v01), ISSUE-REVISION=I00-R00
```

## Recommendations

1. **Fix v5.0 violations first** before migrating to R1.0
2. **Use automated rename tools** (`generate_rename_map_v6.py` + `execute_rename_v6.py`)
3. **Review low-confidence mappings manually**
4. **Update cross-references** after renaming
5. **Validate with R1.0 validator** after migration

---

**Next Steps:**

- [ ] Review this inventory report
- [ ] Fix v5.0 violations (if any)
- [ ] Generate rename map for R1.0 migration
- [ ] Execute PR^3-2 (Retrofit)
