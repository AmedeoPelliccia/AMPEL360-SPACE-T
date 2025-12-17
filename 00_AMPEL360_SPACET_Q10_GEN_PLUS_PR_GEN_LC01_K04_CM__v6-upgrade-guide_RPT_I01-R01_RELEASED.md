# AMPEL360 Space-T v6.0 R1.0 Upgrade Guide
# Migration from v5.0 to v6.0 R1.0

**Version:** I01-R01  
**Status:** RELEASED  
**Date:** 2025-12-17  
**Owner:** Configuration Management Working Group

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Breaking Changes](#breaking-changes)
3. [Migration Strategy](#migration-strategy)
4. [Step-by-Step Migration](#step-by-step-migration)
5. [Validation](#validation)
6. [Troubleshooting](#troubleshooting)
7. [Support](#support)

---

## Executive Summary

This guide provides comprehensive instructions for migrating from Nomenclature Standard v5.0 to v6.0 R1.0 (FINAL LOCK).

### Migration Overview

- **Complexity**: Moderate (4 new mandatory tokens)
- **Time Required**: 2-4 hours (automated tooling available)
- **Risk Level**: Low (automated validation)
- **Rollback**: Supported via git

### What's Changing

v6.0 R1.0 introduces a **15-token canonical format** with 4 new mandatory fields:

1. **FAMILY** - Quantum-inspired pax payload numbering (Q10, Q100)
2. **VERSION** - Branding reinforcer (PLUS, PLUSULTRA) with optional 2-digit iteration
3. **MODEL** - Artifact domain (BB, HW, SW, PR)
4. **ISSUE-REVISION** - Change tracking (I##-R##)

Additionally:
- **VARIANT** semantics redefined (governance lane vs. configuration)
- **Conditional subject prefixes** required for CUST and MSN variants
- **Normative length limits** enforced

---

## Breaking Changes

### 1. Canonical Format Changed

**v5.0 Format (11 tokens):**
```
[ATA_ROOT]_[PROJECT]_[PROGRAM]_[VARIANT]_[BLOCK]_[PHASE]_[KNOT_TASK]_[AoR]__[SUBJECT]_[TYPE]_[VERSION]_[STATUS].[EXT]
```

**v6.0 Format (15 tokens):**
```
[ATA_ROOT]_[PROJECT]_[PROGRAM]_[FAMILY]_[VARIANT]_[VERSION]_[MODEL]_[BLOCK]_[PHASE]_[KNOT_TASK]_[AoR]__[SUBJECT]_[TYPE]_[ISSUE-REVISION]_[STATUS].[EXT]
```

### 2. Token Position Changes

| Token | v5.0 Position | v6.0 Position | Change |
|-------|--------------|--------------|--------|
| ATA_ROOT | 1 | 1 | No change |
| PROJECT | 2 | 2 | No change |
| PROGRAM | 3 | 3 | No change |
| **FAMILY** | N/A | **4** | **NEW** |
| VARIANT | 4 | **5** | Moved |
| **VERSION** | 11 | **6** | **Moved + Redefined** |
| **MODEL** | N/A | **7** | **NEW** |
| BLOCK | 5 | **8** | Moved |
| PHASE | 6 | **9** | Moved |
| KNOT_TASK | 7 | **10** | Moved |
| AoR | 8 | **11** | Moved |
| __ | 9 | **12** | Moved |
| SUBJECT | 10 | **13** | Moved |
| TYPE | 11 | **14** | Moved |
| **ISSUE-REVISION** | N/A | **15** | **NEW** |
| STATUS | 12 | **16** | Moved |
| EXT | 13 | **17** | No change |

### 3. Semantic Changes

#### VARIANT (Redefined)

**v5.0:** Configuration variant (PLUS, CERT, SYS, SW, etc.)

**v6.0:** Governance lane / variant context
- Allowlist: `GEN`, `BASELINE`, `FLIGHTTEST`, `CERT`, `MSN`, `HOV`, `CUST`
- Old `PLUS` → New `GEN` (general purpose)
- Old `CERT` → New `CERT` (certification - unchanged in name, redefined semantics)

#### VERSION (Redefined)

**v5.0:** Version counter (`v01`, `v02`, etc.)

**v6.0:** Branding reinforcer with optional iteration
- Pattern: `(PLUS|PLUSULTRA)[0-9]{2}?`
- Examples: `PLUS`, `PLUS01`, `PLUSULTRA02`
- No longer a simple version counter

#### ISSUE-REVISION (New)

**v6.0:** Replaces the old version counter concept
- Pattern: `I##-R##`
- Examples: `I01-R01`, `I12-R03`
- Zero-padded to 2 digits
- Mandatory in all files

### 4. New Governance Rules

#### Conditional Subject Prefixes

- **VARIANT=CUST** requires `SUBJECT` to start with `cust-<custcode>-`
  - Example: `cust-airbus-thermal-loop`
  
- **VARIANT=MSN** requires `SUBJECT` to start with `msn-<serial>-`
  - Example: `msn-000123-thermal-loop`

#### Length Limits (Normative)

- Max filename length: 180 characters
- Max BLOCK length: 12 characters
- Max SUBJECT length: 60 characters
- Max TYPE length: 8 characters
- Max AoR length: 10 characters

---

## Migration Strategy

### Automated Migration (Recommended)

Use the provided migration tools for bulk conversion:

```bash
# Step 1: Generate v6 rename map
python scripts/generate_rename_map_v6.py

# Step 2: Review rename_map_v6.csv
# Check proposed changes, verify defaults

# Step 3: Execute rename
python scripts/execute_rename_v6.py --dry-run   # Preview first
python scripts/execute_rename_v6.py             # Execute rename
```

### Manual Migration (Single Files)

For individual files or custom scenarios:

```bash
# Use scaffolding tool
python scripts/scaffold_v6.py --standard v6.0 \
  <ATA_ROOT> <PROJECT> <PROGRAM> <FAMILY> <VARIANT> \
  <VERSION> <MODEL> <BLOCK> <PHASE> <KNOT_TASK> <AOR> \
  <SUBJECT> <TYPE> <ISSUE-REVISION> <STATUS>
```

### Default Values

The migration tools apply these defaults for new fields:

| Field | Default Value | Rationale |
|-------|--------------|-----------|
| FAMILY | `Q10` | 10-passenger quantum family |
| VARIANT | `GEN` | General purpose (for v5.0 PLUS files) |
| VERSION | `PLUS` | Standard branding |
| MODEL | `BB` | Body Brain / PR-O-RO model |
| ISSUE-REVISION | `I01-R01` | Initial issue and revision |

---

## Step-by-Step Migration

### Phase 1: Preparation

#### 1.1. Backup Current State

```bash
# Create a backup branch
git checkout -b backup-pre-v6-migration
git push origin backup-pre-v6-migration

# Return to working branch
git checkout main  # or your working branch
```

#### 1.2. Review Documentation

Read the following documents:

- `docs/standards/NOMENCLATURE_v6_0_R1_0.md` (full standard)
- `docs/standards/NOMENCLATURE_v6_0_R1_0_QUICKREF.md` (quick reference)
- `00_AMPEL360_SPACET_Q10_GEN_PLUS_PR_GEN_LC01_K04_CM__retrofit-report-v6_RPT_I01-R01_ACTIVE.md` (retrofit report)

#### 1.3. Validate Current State

```bash
# Validate v5.0 compliance before migration
python validate_nomenclature.py --standard v5.0 --check-all --verbose
```

### Phase 2: Migration Execution

#### 2.1. Generate Rename Map

```bash
# Generate v6 rename map with default values
python scripts/generate_rename_map_v6.py

# Output: rename_map_v6.csv
```

#### 2.2. Review Rename Map

Open `rename_map_v6.csv` and review proposed changes:

- Check that FAMILY defaults are appropriate (Q10 vs Q100)
- Verify VARIANT mappings (PLUS → GEN, CERT → CERT)
- Confirm MODEL assignments (BB, HW, SW, PR)
- Review ISSUE-REVISION assignments

**Adjust if needed:**
- Edit CSV manually for special cases
- Set custom FAMILY for specific files
- Override default VARIANT mappings
- Specify different MODEL values

#### 2.3. Dry-Run Migration

```bash
# Preview changes without executing
python scripts/execute_rename_v6.py --dry-run

# Review output carefully
```

#### 2.4. Execute Migration

```bash
# Execute the rename
python scripts/execute_rename_v6.py

# Monitor output for errors
```

#### 2.5. Update Cross-References

```bash
# Update internal links and cross-references
python scripts/update_cross_references_v6.py
```

### Phase 3: Validation

#### 3.1. Validate Nomenclature

```bash
# Validate all files against v6.0 standard
python validate_nomenclature.py --standard v6.0 --check-all --verbose

# Expected output: 0 violations
```

#### 3.2. Check Links

```bash
# Check for broken internal links
python scripts/check_and_update_links.py --check-only

# Fix broken links if any
python scripts/check_and_update_links.py --update
```

#### 3.3. Validate Schemas

```bash
# Validate schema registries
python scripts/validate_schema_registry.py --check-all
```

#### 3.4. Run CI Checks Locally

```bash
# Simulate CI governance gates
python validate_nomenclature.py --standard v6.0 --mode block --check-all --strict --verbose
python scripts/validate_trace_links.py --check-all
```

### Phase 4: Finalization

#### 4.1. Commit Changes

```bash
# Stage all changes
git add .

# Commit with descriptive message
git commit -m "Migrate to v6.0 R1.0 nomenclature standard

- Generate v6 rename map
- Execute automated rename (1,416 files)
- Update cross-references and links
- Validate against v6.0 standard
- Apply default values: FAMILY=Q10, VARIANT=GEN, VERSION=PLUS, MODEL=BB
- All files pass v6.0 validation (0 violations)"

# Push changes
git push origin <your-branch>
```

#### 4.2. Create Pull Request

Create a PR with the following information:

**Title:** `Migrate to Nomenclature Standard v6.0 R1.0`

**Description:**
```markdown
## Migration to v6.0 R1.0

This PR migrates all files from v5.0 to v6.0 R1.0 nomenclature standard.

### Changes
- 1,416 files renamed to v6.0 format
- 4 new mandatory tokens added (FAMILY, VERSION, MODEL, ISSUE-REVISION)
- Cross-references updated
- Internal links validated

### Validation Results
- ✅ Nomenclature: 1,416 valid, 0 invalid
- ✅ CI Gates: All passing
- ✅ Schema validation: Pass
- ✅ Trace links: Pass

### Default Values Applied
- FAMILY: Q10 (10-passenger)
- VARIANT: GEN (general) for v5.0 PLUS files
- VERSION: PLUS (standard branding)
- MODEL: BB (Body Brain)
- ISSUE-REVISION: I01-R01 (initial)

### References
- Migration guide: 00_AMPEL360_SPACET_Q10_GEN_PLUS_PR_GEN_LC01_K04_CM__v6-upgrade-guide_RPT_I01-R01_RELEASED.md
- Retrofit report: 00_AMPEL360_SPACET_Q10_GEN_PLUS_PR_GEN_LC01_K04_CM__retrofit-report-v6_RPT_I01-R01_ACTIVE.md
```

#### 4.3. Review and Merge

1. Wait for CI checks to pass
2. Request reviews from CM WG members
3. Address any feedback
4. Merge when approved

---

## Validation

### Validation Commands

```bash
# Full v6.0 validation
python validate_nomenclature.py --standard v6.0 --check-all --mode block --strict --verbose

# Check specific file
python validate_nomenclature.py --standard v6.0 <filename>

# Link checking
python scripts/check_and_update_links.py --check-only

# Schema validation
python scripts/validate_schema_registry.py --check-all

# Trace link validation
python scripts/validate_trace_links.py --check-all
```

### Expected Results

✅ **Nomenclature Validation**
- All files pass v6.0 standard
- 0 violations reported
- Mode: block (zero tolerance)

✅ **Link Checking**
- 0 broken internal links
- All cross-references updated

✅ **CI Gates**
- GATE-001 (Nomenclature): PASS
- GATE-002 (Schema Registry): PASS
- GATE-003 (Trace Links): PASS

---

## Troubleshooting

### Common Issues

#### Issue: Validation Fails with "Invalid FAMILY"

**Symptom:** File fails validation with message about invalid FAMILY token.

**Solution:**
```bash
# FAMILY must be Q10 or Q100
# Check your rename map or manual filename

# Valid examples:
# - 27_AMPEL360_SPACET_Q10_GEN_PLUS_BB_OPS_LC03_K06_SE__thermal-loop_STD_I01-R01_ACTIVE.md
# - 27_AMPEL360_SPACET_Q100_GEN_PLUS_BB_OPS_LC03_K06_SE__thermal-loop_STD_I01-R01_ACTIVE.md
```

#### Issue: "CUST variant requires cust- prefix"

**Symptom:** Validation error for CUST variant files without proper prefix.

**Solution:**
```bash
# CUST variant requires SUBJECT to start with cust-<custcode>-
# Example: cust-airbus-thermal-loop

# Before (invalid):
# 27_AMPEL360_SPACET_Q10_CUST_PLUS_SW_OPS_LC03_K06_SE__thermal-loop_STD_I01-R01_DRAFT.md

# After (valid):
# 27_AMPEL360_SPACET_Q10_CUST_PLUS_SW_OPS_LC03_K06_SE__cust-airbus-thermal_STD_I01-R01_DRAFT.md
```

#### Issue: "MSN variant requires msn- prefix"

**Symptom:** Validation error for MSN variant files without proper prefix.

**Solution:**
```bash
# MSN variant requires SUBJECT to start with msn-<serial>-
# Example: msn-000123-thermal-loop

# Valid:
# 27_AMPEL360_SPACET_Q10_MSN_PLUSULTRA02_HW_OPS_LC03_K06_SE__msn-000123-thermal_STD_I01-R01_ACTIVE.md
```

#### Issue: "VERSION pattern mismatch"

**Symptom:** VERSION token doesn't match required pattern.

**Solution:**
```bash
# VERSION must be: (PLUS|PLUSULTRA) with optional 2-digit iteration

# Valid:
# - PLUS
# - PLUS01
# - PLUS99
# - PLUSULTRA
# - PLUSULTRA01
# - PLUSULTRA99

# Invalid:
# - PLUS1 (must be 2 digits)
# - PLUSULTRA001 (must be 2 digits, not 3)
# - plus (must be uppercase)
```

#### Issue: "ISSUE-REVISION format invalid"

**Symptom:** ISSUE-REVISION doesn't match I##-R## pattern.

**Solution:**
```bash
# Must be I##-R## with zero-padding

# Valid:
# - I01-R01
# - I12-R03
# - I99-R99

# Invalid:
# - I1-R1 (must be zero-padded)
# - I001-R01 (must be 2 digits, not 3)
# - i01-r01 (must be uppercase)
```

#### Issue: "Filename too long"

**Symptom:** Filename exceeds 180 character limit.

**Solution:**
```bash
# Check token lengths:
# - BLOCK: max 12 chars
# - SUBJECT: max 60 chars
# - TYPE: max 8 chars
# - AoR: max 10 chars

# Shorten SUBJECT if needed
# Use abbreviations where appropriate
```

### Getting Help

If you encounter issues not covered here:

1. **Check documentation:**
   - `docs/standards/NOMENCLATURE_v6_0_R1_0.md`
   - `docs/standards/NOMENCLATURE_v6_0_R1_0_QUICKREF.md`

2. **Run validation in verbose mode:**
   ```bash
   python validate_nomenclature.py --standard v6.0 --verbose <filename>
   ```

3. **Check config file:**
   - `config/nomenclature/v6_0.yaml`

4. **Contact CM WG:**
   - Open GitHub issue with label `nomenclature`
   - Tag: @configuration-management

---

## Support

### Resources

- **Full Standard**: `docs/standards/NOMENCLATURE_v6_0_R1_0.md`
- **Quick Reference**: `docs/standards/NOMENCLATURE_v6_0_R1_0_QUICKREF.md`
- **Config File**: `config/nomenclature/v6_0.yaml`
- **Retrofit Report**: `00_AMPEL360_SPACET_Q10_GEN_PLUS_PR_GEN_LC01_K04_CM__retrofit-report-v6_RPT_I01-R01_ACTIVE.md`

### Tools

- **Validator**: `validate_nomenclature.py`
- **Scaffolding**: `scripts/scaffold_v6.py`
- **Migration**: `scripts/generate_rename_map_v6.py`, `scripts/execute_rename_v6.py`
- **Link Checker**: `scripts/check_and_update_links.py`

### Contact

- **GitHub Issues**: https://github.com/AmedeoPelliccia/AMPEL360-SPACE-T/issues
- **CM WG**: Configuration Management Working Group
- **Documentation**: README.md and docs/ directory

---

## Appendix

### A. Migration Checklist

- [ ] Backup current state (branch + git tag)
- [ ] Review v6.0 documentation
- [ ] Validate v5.0 compliance
- [ ] Generate v6 rename map
- [ ] Review rename map for accuracy
- [ ] Dry-run migration
- [ ] Execute migration
- [ ] Update cross-references
- [ ] Validate v6.0 compliance
- [ ] Check internal links
- [ ] Run CI checks locally
- [ ] Commit changes
- [ ] Create pull request
- [ ] Request CM WG review
- [ ] Merge when approved

### B. Example Migrations

#### Example 1: Simple File

**v5.0:**
```
27_AMPEL360_SPACET_PLUS_OPS_LC03_K06_SE__thermal-loop_STD_v01_ACTIVE.md
```

**v6.0:**
```
27_AMPEL360_SPACET_Q10_GEN_PLUS_BB_OPS_LC03_K06_SE__thermal-loop_STD_I01-R01_ACTIVE.md
```

**Changes:**
- Added FAMILY: `Q10`
- Changed VARIANT: `PLUS` → `GEN`
- Moved VERSION to position 6: `PLUS`
- Added MODEL: `BB`
- Changed ISSUE-REVISION: `v01` → `I01-R01`

#### Example 2: CUST Variant

**v5.0:**
```
27_AMPEL360_SPACET_CERT_SW_LC03_K06_SE__airbus-requirements_REQ_v02_DRAFT.md
```

**v6.0:**
```
27_AMPEL360_SPACET_Q10_CUST_PLUS_SW_OPS_LC03_K06_SE__cust-airbus-requirements_REQ_I02-R01_DRAFT.md
```

**Changes:**
- Added FAMILY: `Q10`
- Changed VARIANT: `CERT` → `CUST`
- Added VERSION: `PLUS`
- Kept MODEL: `SW`
- Added conditional prefix: `cust-airbus-`
- Changed ISSUE-REVISION: `v02` → `I02-R01`

#### Example 3: MSN Variant

**v5.0:**
```
27_AMPEL360_SPACET_PLUS_HW_LC05_K08_TEST__msn123-test-procedure_PROC_v01_ACTIVE.md
```

**v6.0:**
```
27_AMPEL360_SPACET_Q10_MSN_PLUS_HW_TEST_LC05_K08_TEST__msn-000123-test-procedure_PROC_I01-R01_ACTIVE.md
```

**Changes:**
- Added FAMILY: `Q10`
- Changed VARIANT: `PLUS` → `MSN`
- Moved VERSION: `PLUS`
- Kept MODEL: `HW`
- Standardized MSN prefix: `msn123` → `msn-000123-`
- Changed ISSUE-REVISION: `v01` → `I01-R01`

---

**Document Control**

- **Owner**: Configuration Management WG
- **Status**: RELEASED
- **Version**: I01-R01
- **Last Updated**: 2025-12-17
- **Next Review**: Post-migration feedback cycle
