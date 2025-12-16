---
title: "Nomenclature Automation Guide v4.0"
type: IDX
variant: "PLUS"
status: "Normative"
owner: "Configuration Management WG"
---

# Nomenclature Automation Guide v4.0

This guide documents the automation tooling for nomenclature standard v4.0 enforcement, validation, and scaffolding.

---

## 1. Overview

The nomenclature v4.0 automation suite consists of:

1. **Validator** (`validate_nomenclature.py`) - Filename compliance checking
2. **Scaffolder** (`scripts/scaffold.py`) - Template-based file generation
3. **CI Workflow** (`.github/workflows/nomenclature-validation.yml`) - Automated PR checks
4. **Pre-commit Hook** (`scripts/pre-commit`) - Local validation before commit

---

## 2. Validation Tool

### 2.1 Usage

```bash
# Validate single filename
python validate_nomenclature.py <filename>

# Validate all files in repository
python validate_nomenclature.py --check-all

# Validate specific directory
python validate_nomenclature.py --check-dir <directory>

# Strict mode (enforce TYPE vocabulary)
python validate_nomenclature.py --check-all --strict

# Verbose output (show all files including valid ones)
python validate_nomenclature.py --check-all --verbose
```

### 2.2 Validation Rules

The validator enforces:

1. **Primary regex pattern** (12-field format)
2. **Field constraints** (format, character sets, case)
3. **PROJECT constraint** (must be `AMPEL360`)
4. **PROGRAM constraint** (must be `SPACET`)
5. **TRIGGER_KNOT format** (K00 or K01-K99)
6. **AoR allowlist** (CM, CERT, AI, DATA, OPS, SE, SAF, PMO, CY, TEST, MRO, SPACEPORT)
7. **BUCKET-SUBJECT rules** (LC01-LC14 for BUCKET=00, SB ranges for others)
8. **TYPE vocabulary** (approved artifact types)
9. **Double underscore** before DESCRIPTION

### 2.3 Exit Codes

* `0`: All files valid
* `1`: One or more files invalid
* `2`: Script error

### 2.4 Excluded Files and Directories

The validator automatically excludes:

**Files:**
* `README.md`, `LICENSE`, `EXAMPLES.md`
* `IMPLEMENTATION_SUMMARY.md`, `REVIEW_NOTES.md`
* `.gitignore`, `.gitattributes`, `.gitkeep`
* Agent config files (`*_Agent_Config.*`)
* Python bytecode (`*.pyc`, `*.pyo`, `*.pyd`)

**Directories:**
* `.git`, `.github`, `node_modules`, `__pycache__`
* `.pytest_cache`, `.venv`, `venv`, `dist`, `build`
* `templates` (template source files)
* `scripts` (utility scripts)

---

## 3. Scaffolding Tool

### 3.1 Usage

```bash
python scripts/scaffold.py <ROOT> <PROJECT> <PROGRAM> <VARIANT> <BUCKET> <TYPE> <LC|SB> <KNOT> <AOR> <DESC> <VER>
```

### 3.2 Examples

```bash
# Global program plan (K00, CM-owned)
python scripts/scaffold.py 00 AMPEL360 SPACET PLUS 00 PLAN LC02 K00 CM safety-program v01

# Certification authority basis (K01, CERT-owned)
python scripts/scaffold.py 00 AMPEL360 SPACET CERT 00 PLAN LC10 K01 CERT certification-authority-basis v01

# Propulsion FHA (K02, SAF-owned)
python scripts/scaffold.py 00 AMPEL360 SPACET PLUS 70 FHA SB70 K02 SAF propulsion v01

# ATA tasklist (K03, SPACEPORT-owned)
python scripts/scaffold.py 78 AMPEL360 SPACET PLUS 00 IDX LC01 K03 SPACEPORT k03-ata-78-tasklist v01

# Data schema (K00, DATA-owned)
python scripts/scaffold.py 00 AMPEL360 SPACET GEN 90 SCH SB90 K00 DATA knots-data-structure v01
```

### 3.3 Template System

The scaffolder uses templates from `templates/<TYPE>.md`. If no template exists, it creates a minimal file.

**Template placeholders:**
* `{{DESCRIPTION}}` - Replaced with DESC field
* `{{TITLE}}` - Human-readable title (capitalized DESC)
* `{{PROJECT}}` - PROJECT field value
* `{{PROGRAM}}` - PROGRAM field value
* `{{VARIANT}}` - VARIANT field value
* `{{BUCKET}}` - BUCKET field value
* `{{ROOT}}` - ROOT field value
* `{{LC_OR_SUBBUCKET}}` - LC|SB field value
* `{{TRIGGER_KNOT}}` - TRIGGER_KNOT field value (NEW in v4.0)
* `{{AOR}}` - AoR field value (NEW in v4.0)
* `{{OWNER}}` - Default owner (typically "TBD")
* `{{SYSTEM_NAME}}` - System name (from DESC)
* `{{DATE}}` - Current ISO date

### 3.4 Validation

The scaffolder performs basic input validation:
* ROOT must be 2-3 digits
* PROJECT must be `AMPEL360`
* PROGRAM must be `SPACET`
* BUCKET must be in allowlist
* TYPE must be uppercase
* LC|SB format and BUCKET compatibility
* TRIGGER_KNOT format (K00-K99)
* AoR must be in allowlist
* VERSION format (vNN)

---

## 4. CI/CD Integration

### 4.1 GitHub Actions Workflow

File: `.github/workflows/nomenclature-validation.yml`

**Triggers:**
* Push to any branch
* Pull request to any branch

**Steps:**
1. Checkout repository
2. Set up Python 3.x
3. Run `validate_nomenclature.py --check-all --strict --verbose`
4. Report results (fail PR if violations found)

### 4.2 Customization

To modify CI behavior, edit the workflow file:

```yaml
- name: Validate all files
  run: |
    python validate_nomenclature.py --check-all --strict --verbose
```

Options:
* Remove `--strict` to only warn on TYPE vocabulary violations
* Remove `--verbose` to only show invalid files
* Add `--check-dir <directory>` to validate specific directories

---

## 5. Pre-commit Hook

### 5.1 Installation

```bash
cp scripts/pre-commit .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

### 5.2 Behavior

The pre-commit hook:
1. Validates all staged files against nomenclature standard
2. Blocks commit if violations found
3. Prints actionable error messages
4. Allows commit if all files valid

### 5.3 Bypass (Emergency Only)

To bypass pre-commit validation (not recommended):
```bash
git commit --no-verify
```

**Warning:** Bypassing pre-commit will cause CI to fail. Only use for emergencies.

---

## 6. Migration Tools

### 6.1 Rename Map Generator

For v3.0 → v4.0 migration, use the rename mapping script:

```bash
python scripts/generate_rename_map_v4.py --output rename_map.csv
```

This generates a CSV with columns:
* `old_path` - Current v3.0 filename
* `new_path` - Target v4.0 filename
* `trigger_knot` - Determined KNOT value
* `aor` - Determined AoR value
* `confidence` - Heuristic confidence level

### 6.2 Batch Rename

Execute batch rename with the generated map:

```bash
python scripts/execute_rename_v4.py --map rename_map.csv --dry-run

# After verifying dry-run output:
python scripts/execute_rename_v4.py --map rename_map.csv --execute
```

### 6.3 Cross-Reference Updater

Update all internal links and references:

```bash
python scripts/update_cross_references_v4.py --map rename_map.csv --dry-run

# After verifying dry-run output:
python scripts/update_cross_references_v4.py --map rename_map.csv --execute
```

---

## 7. Heuristics for KNOT and AoR Assignment

### 7.1 TRIGGER_KNOT Heuristics

**From directory structure:**
* Files in `KNOTS/K01_*/` → `K01`
* Files in `KNOTS/K02_*/` → `K02`
* Files in `KNOTS/KXX_*/` → `KXX`

**From description:**
* Description contains `k01-` → `K01`
* Description contains `k02-` → `K02`
* Description contains `kXX-` → `KXX`

**From content type:**
* Nomenclature, baselines, CI config → `K00`
* Program-level plans → `K00`
* Lifecycle control files → `K00`

**Default:** `K00` (global)

### 7.2 AoR Heuristics

**From directory structure:**
* Files in `STK_CM-*/` → `CM`
* Files in `STK_CERT-*/` → `CERT`
* Files in `STK_SAF-*/` → `SAF`
* Files in `STK_<AOR>-*/` → `<AOR>`

**From variant:**
* VARIANT=CERT → `CERT`

**From artifact type:**
* TYPE=FHA, PSSA, SSA, FTA → `SAF`
* TYPE=TRC, DAL (compliance) → `CERT`
* TYPE=STD, IDX (governance) → `CM`
* TYPE=REQ (test-related) → `TEST`
* TYPE=REQ (system-level) → `SE`

**From description:**
* Contains "certification", "compliance", "authority" → `CERT`
* Contains "safety", "hazard", "risk" → `SAF`
* Contains "test", "verification", "ivvq" → `TEST`
* Contains "operation", "mission", "flight" → `OPS`
* Contains "cyber", "security", "threat" → `CY`
* Contains "data", "schema", "governance" → `DATA`

**Default:** `CM` (configuration management)

---

## 8. Troubleshooting

### 8.1 Common Errors

**Error:** "Filename does not match required pattern"
* **Solution:** Ensure 12 fields separated by single `_`, with `__` before DESCRIPTION

**Error:** "Invalid PROJECT 'XXX': must be AMPEL360"
* **Solution:** Use `AMPEL360` (case-sensitive, no variations)

**Error:** "Invalid PROGRAM 'XXX': must be SPACET"
* **Solution:** Use `SPACET` (case-sensitive, no variations)

**Error:** "BUCKET=00 requires SUBJECT to be LC01-LC14"
* **Solution:** Use lifecycle codes (LC01-LC14) for BUCKET=00

**Error:** "BUCKET=70 requires SUBJECT to be SB70-SB79"
* **Solution:** Use appropriate sub-bucket range for the bucket

**Error:** "Invalid TRIGGER_KNOT 'KNOT01'"
* **Solution:** Use format K00 or K01-K99 (uppercase K + 2 digits)

**Error:** "Invalid AoR 'STK_CM'"
* **Solution:** Use portal code only (CM, not STK_CM)

**Error:** "AoR 'CUSTOM' not in allowlist"
* **Solution:** Use one of the approved AoR codes (see quick reference)

**Error:** "Single underscore before DESCRIPTION"
* **Solution:** Use double underscore `__` between AoR and DESCRIPTION

### 8.2 Debug Mode

Enable debug output for troubleshooting:

```bash
python validate_nomenclature.py --check-all --verbose --strict
```

---

## 9. Best Practices

### 9.1 Before Creating New Files

1. **Check if template exists** for the TYPE
2. **Use scaffolder** instead of manual creation
3. **Validate immediately** after creation
4. **Run pre-commit hook** before committing

### 9.2 During Migration

1. **Generate rename map first** (with `--dry-run`)
2. **Review heuristic assignments** manually
3. **Execute rename in test branch first**
4. **Validate all files** after rename
5. **Update cross-references** before merging
6. **Run link checker** to verify navigation

### 9.3 Ongoing Maintenance

1. **Always use scaffolder** for new files
2. **Enable pre-commit hook** for all contributors
3. **Monitor CI results** on all PRs
4. **Update templates** when new patterns emerge
5. **Document exceptions** in retrofit report

---

## 10. Reference

### 10.1 Related Documents

* [Nomenclature Standard v4.0](00_AMPEL360_SPACET_PLUS_00_STD_LC01_K00_CM__nomenclature-standard_v04.md)
* [Nomenclature Quick Reference v4.0](00_AMPEL360_SPACET_PLUS_00_CAT_LC01_K00_CM__nomenclature-quick-reference_v04.md)
* [KNOTS Catalog](00_AMPEL360_SPACET_CERT_90_CAT_SB90_K00_CERT__knots-catalog_v01.json)

### 10.2 Tool Locations

* Validator: `validate_nomenclature.py`
* Scaffolder: `scripts/scaffold.py`
* CI Workflow: `.github/workflows/nomenclature-validation.yml`
* Pre-commit: `scripts/pre-commit`
* Migration scripts: `scripts/generate_rename_map_v4.py`, `scripts/execute_rename_v4.py`, `scripts/update_cross_references_v4.py`

---

**Version:** v4.0  
**Date:** 2025-12-16  
**Owner:** Configuration Management WG
