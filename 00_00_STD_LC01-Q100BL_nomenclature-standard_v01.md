---
title: "Nomenclature Standard v1.0"
lifecycle_phase: "All"
generated: "2025-12-14"
standard: "OPT-IN Framework v1.1 / AMPEL360 Space-T"
status: "Normative"
owner: "Configuration Management WG"
---

# Nomenclature Standard v1.0 (Normative)

## 1. Purpose

This standard defines the **mandatory** file naming convention for all artifacts within AMPEL360 Space-T. It ensures:

1. **Unambiguous identification** of file content and context.
2. **Machine-readability** for automated sorting, filtering, indexing, and traceability.
3. **CI/CD enforceability** using deterministic regular expressions and validation rules.

## 2. Filename Format

All files must strictly adhere to:

`[ROOT]_[BUCKET]_[TYPE]_[VARIANT]_[DESCRIPTION]_[VERSION].[EXT]`

## 3. Field Definitions and Constraints

### 3.1 Field Definitions

| Field           | Meaning                               | Constraint                             | Regex                        |
| :-------------- | :------------------------------------ | :------------------------------------- | :--------------------------- |
| **ROOT**        | ATA Chapter or Project Code           | 2 digits                               | `^\d{2}$`                    |
| **BUCKET**      | Domain Classification (OPT-IN + LC)   | 2 digits (enum)                        | `^(00\|10\|20\|30\|40\|50\|60\|70\|80\|90)$` |
| **TYPE**        | Artifact Type                         | 2–8 uppercase alphanumeric             | `^[A-Z0-9]{2,8}$`            |
| **VARIANT**     | Configuration / Baseline / Item Class | uppercase alphanumeric; hyphen allowed | `^[A-Z0-9]+(?:-[A-Z0-9]+)*$` |
| **DESCRIPTION** | Human-readable content label          | lowercase kebab-case                   | `^[a-z0-9]+(?:-[a-z0-9]+)*$` |
| **VERSION**     | Revision Control                      | `v` + 2 digits                         | `^v\d{2}$`                   |
| **EXT**         | File Extension                        | lowercase alphanumeric                 | `^[a-z0-9]{1,6}$`            |

### 3.2 General Naming Rules (Mandatory)

* **Delimiters**
  * Use underscore `_` **only** between fields.
  * Use hyphen `-` **only** inside `VARIANT` (if needed) and inside `DESCRIPTION`.
* **Character set**
  * ASCII only (no accents/diacritics). No spaces.
* **Field count and order**
  * Do not add fields; do not remove fields; do not reorder fields.
* **Folder sub-buckets**
  * Directory sub-bucket identifiers (e.g., `00-20-01_*`) remain **directory-level semantics** and must not be encoded by changing the 2-digit `BUCKET` field.

---

## 4. Allowed Values and Semantics

### 4.1 `[ROOT]` (2 digits)

* `00`: General / Project-Level / Cross-Domain
* `01`–`99`: ATA chapter codes (e.g., `24` Electrical, `27` Flight Controls, `72` Engine) or programme-approved codes.

### 4.2 `[BUCKET]` (2 digits) — Authoritative Allowlist

`BUCKET` indicates the **domain classification** used for filtering and portfolio grouping.

* `00`: **Lifecycle (LC) artifacts only** (LC01–LC14 deliverables, gates, lifecycle governance, lifecycle control packs)
* `10`: Operations
* `20`: Primary Subsystem
* `30`: Circularity
* `40`: Software
* `50`: Structures
* `60`: Storages
* `70`: Propulsion
* `80`: Energy
* `90`: Tables / Schemas / Diagrams / Reference

**Normative rule:** `BUCKET=00` is **reserved**. Non-LC artifacts shall not use `00`.

### 4.3 `[TYPE]` (Controlled Vocabulary)

The following set is **approved** for v1.0. Extensions require Configuration Management WG change control.

* **Planning / Control:** `PLAN`, `MIN`, `RPT`, `LOG`, `ACT`, `IDX`
* **Safety Analyses:** `FHA`, `PSSA`, `SSA`, `FTA`, `ANA`
* **Requirements / Allocation:** `REQ`, `DAL`, `TRC`
* **Data / Reference:** `CAT`, `LST`, `GLO`, `MAT`, `SCH`, `DIA`, `TAB`, `STD`

### 4.4 `[VARIANT]` (Configuration / Baseline)

`VARIANT` encodes the configuration context.

**Reserved tokens (recommended baseline):**

* `Q100BL`: Formally controlled baseline (Freeze/Release)
* `DRAFT`: Work in progress (non-baseline)
* `PROTO`: Prototyping artifacts
* `SYS`, `SW`, `HW`: System / Software / Hardware scoped artifacts

Hyphenated variants are allowed: `SYS-01`, `SW-PLAT-A`.

#### 4.4.1 Mandatory LC encoding when `BUCKET=00`

When `BUCKET=00`, the lifecycle stage identifier **shall** be encoded at the beginning of `VARIANT`:

* Required prefix: `LC01` … `LC14`
* Recommended pattern: `LCxx-<context>` (e.g., `LC02-Q100BL`, `LC04-GEN`, `LC11-DRAFT`)

**LC prefix regex:** `^LC(0[1-9]|1[0-4])(?:-[A-Z0-9]+(?:-[A-Z0-9]+)*)?$`

**Normative rule:** If `BUCKET=00` and `VARIANT` does not start with `LCxx`, the filename is **non-compliant**.

### 4.5 `[DESCRIPTION]`

* Must be lowercase kebab-case.
* Must not duplicate semantic content already encoded in `TYPE` or `BUCKET`.
  * Example: avoid `..._FHA_SYS_propulsion-fha_...` → use `..._FHA_SYS_propulsion_...`

### 4.6 `[VERSION]`

* Exactly `vNN` where `NN` is two digits (`v01`, `v02`, …).
* Increment `vNN` only per the versioning rules in Section 6.

---

## 5. Enforcement

### 5.1 Primary Regex (PCRE)

This regex validates the general filename structure:

```regex
^(?<root>\d{2})_(?<bucket>00|10|20|30|40|50|60|70|80|90)_(?<type>[A-Z0-9]{2,8})_(?<variant>[A-Z0-9]+(?:-[A-Z0-9]+)*)_(?<desc>[a-z0-9]+(?:-[a-z0-9]+)*)_(?<ver>v\d{2})\.(?<ext>[a-z0-9]{1,6})$
```

### 5.2 Conditional Rule (Mandatory) — LC Constraint for `BUCKET=00`

CI shall additionally enforce:

* If `bucket == "00"` then `variant` matches:

```regex
^LC(0[1-9]|1[0-4])(?:-[A-Z0-9]+(?:-[A-Z0-9]+)*)?$
```

---

## 6. Examples

### 6.1 Valid examples

* Lifecycle (LC) plan:
  * `00_00_PLAN_LC02-Q100BL_safety-program_v01.md`
* Propulsion FHA (domain bucket):
  * `00_70_FHA_SYS_propulsion_v01.md`
* Software safety requirements:
  * `00_40_REQ_SW_software-safety-reqs_v01.md`
* Traceability matrix workbook:
  * `00_20_TRC_Q100BL_traceability-matrix_v01.xlsx`
* Reference schema:
  * `00_90_SCH_GEN_hazard-log-schema_v01.json`

### 6.2 Invalid examples

* Missing LC stage while using lifecycle bucket:
  * `00_00_PLAN_Q100BL_safety-program_v01.md` *(non-compliant: BUCKET=00 requires VARIANT prefix `LCxx`)*
* Wrong delimiter:
  * `00-70-FHA-SYS-propulsion-v01.md` *(non-compliant: must use `_` between fields)*
* Wrong version format:
  * `00_70_FHA_SYS_propulsion_v1.md` *(non-compliant: version must be `vNN`)*
* Invalid bucket:
  * `00_99_LST_GEN_glossary_v01.md` *(non-compliant: bucket must be in allowlist)*

---

## 7. Versioning Strategy (Normative)

* **Version increments:** When an artifact reaches a new controlled state (review gate output, released update, or materially changed content), increment `vNN`.
* **Git history:** Git commits provide authoritative line-level history. Filename version `vNN` denotes a **distinct controlled state** suitable for baselining, gate evidence packaging, and traceability snapshots.
* **Baseline restriction:** `Q100BL` shall only be used for baseline-controlled artifacts; exploratory work shall use `DRAFT` or `PROTO`.

---

## 8. Automation

### 8.1 Validation Script

Use `validate_nomenclature.py` to check files:

```bash
python validate_nomenclature.py <filename>
python validate_nomenclature.py --check-all
```

### 8.2 CI/CD Integration

GitHub Actions workflow automatically validates all committed files against this standard.

### 8.3 Pre-commit Hook

Install the pre-commit hook to validate files before committing:

```bash
cp scripts/pre-commit .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

---
