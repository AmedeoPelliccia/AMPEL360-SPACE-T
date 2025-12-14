---
title: "Nomenclature Standard v2.0"
lifecycle_phase: "All"
generated: "2025-12-14"
standard: "OPT-IN Framework v1.1 / AMPEL360 Space-T"
status: "Normative"
owner: "Configuration Management WG"
breaking_change: "v2.0 introduces mandatory LC_OR_SUBBUCKET field (8-field format)"
---

# Nomenclature Standard v2.0 (Normative)

## 1. Purpose

This standard defines the **mandatory** file naming convention for all artifacts within AMPEL360 Space-T. It ensures:

1. **Unambiguous identification** of file content and context.
2. **Machine-readability** for automated sorting, filtering, indexing, and traceability.
3. **CI/CD enforceability** using deterministic regular expressions and validation rules.
4. **Explicit lifecycle and sub-bucket encoding** through dedicated field.

## 2. Filename Format

All files must strictly adhere to the **8-field format**:

`[ROOT]_[BUCKET]_[TYPE]_[LC_OR_SUBBUCKET]_[VARIANT]_[DESCRIPTION]_[VERSION].[EXT]`

**Breaking change from v1.0**: A new mandatory `LC_OR_SUBBUCKET` field has been added between `TYPE` and `VARIANT`.

## 3. Field Definitions and Constraints

### 3.1 Field Definitions

| Field                | Meaning                               | Constraint                             | Regex                        |
| :------------------- | :------------------------------------ | :------------------------------------- | :--------------------------- |
| **ROOT**             | ATA Chapter or Project Code           | 2-3 digits                             | `^\d{2,3}$`                  |
| **BUCKET**           | Domain Classification (OPT-IN + LC)   | 2 digits (enum)                        | `^(00\|10\|20\|30\|40\|50\|60\|70\|80\|90)$` |
| **TYPE**             | Artifact Type                         | 2–8 uppercase alphanumeric             | `^[A-Z0-9]{2,8}$`            |
| **LC_OR_SUBBUCKET**  | Lifecycle Stage or Sub-bucket         | LC01-LC14 or SB00-SB99                 | `^(LC(0[1-9]\|1[0-4])\|SB\d{2})$` |
| **VARIANT**          | Configuration / Baseline / Item Class | uppercase alphanumeric; hyphen allowed | `^[A-Z0-9]+(?:-[A-Z0-9]+)*$` |
| **DESCRIPTION**      | Human-readable content label          | lowercase kebab-case                   | `^[a-z0-9]+(?:-[a-z0-9]+)*$` |
| **VERSION**          | Revision Control                      | `v` + 2 digits                         | `^v\d{2}$`                   |
| **EXT**              | File Extension                        | lowercase alphanumeric                 | `^[a-z0-9]{1,6}$`            |

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

### 4.1 `[ROOT]` (2-3 digits)

* `00`: General / Project-Level / Cross-Domain
* `01`–`99`: ATA chapter codes (e.g., `24` Electrical, `27` Flight Controls, `72` Engine) or programme-approved codes.
* `100`–`999`: Extended ATA chapter codes (e.g., `115` Supply Chain, `116` Facilities Management).

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

### 4.4 `[LC_OR_SUBBUCKET]` (Lifecycle Stage or Sub-bucket) **[NEW in v2.0]**

This mandatory field encodes either:
- **Lifecycle stage** (LC01-LC14) for `BUCKET=00` files
- **Sub-bucket** identifier (SB00-SB99) for all other buckets

**Conditional rules (mandatory):**

1. **If `BUCKET = 00`** → `LC_OR_SUBBUCKET` **must** match:
   ```regex
   ^LC(0[1-9]|1[0-4])$
   ```
   * Valid: `LC01`, `LC02`, ..., `LC14`
   * Invalid: `SB00`, `LC00`, `LC15`

2. **If `BUCKET ≠ 00`** → `LC_OR_SUBBUCKET` **must** match:
   ```regex
   ^SB\d{2}$
   ```
   * Valid: `SB00`, `SB01`, ..., `SB99`
   * Invalid: `LC01`, `SB`, `SBXX`
   * **Convention**: Use `SB00` if no sub-bucket applies

**Sub-bucket mapping:**
* `SB00` = No sub-bucket / Not applicable
* `SB01` = Maps to directory sub-bucket `*-01_*` (e.g., `00-20-01_*`)
* `SB02` = Maps to directory sub-bucket `*-02_*`
* etc.

### 4.5 `[VARIANT]` (Configuration / Baseline)

`VARIANT` encodes the configuration context (no longer includes lifecycle stage).

**Reserved tokens (recommended baseline):**

* `SPACET`: Formally controlled baseline (Freeze/Release)
* `DRAFT`: Work in progress (non-baseline)
* `PROTO`: Prototyping artifacts
* `SYS`, `SW`, `HW`: System / Software / Hardware scoped artifacts

Hyphenated variants are allowed: `SYS-01`, `SW-PLAT-A`.

**Breaking change from v1.0:** LC prefix is no longer embedded in VARIANT; it is now in the dedicated `LC_OR_SUBBUCKET` field.

### 4.6 `[DESCRIPTION]`

* Must be lowercase kebab-case.
* Must not duplicate semantic content already encoded in `TYPE` or `BUCKET`.
  * Example: avoid `..._FHA_SYS_propulsion-fha_...` → use `..._FHA_SB00_SYS_propulsion_...`

### 4.7 `[VERSION]`

* Exactly `vNN` where `NN` is two digits (`v01`, `v02`, …).
* Increment `vNN` only per the versioning rules in Section 7.

---

## 5. Enforcement

### 5.1 Primary Regex (PCRE) — 8-Field Format

This regex validates the general filename structure for v2.0:

```regex
^(?<root>\d{2})_(?<bucket>00|10|20|30|40|50|60|70|80|90)_(?<type>[A-Z0-9]{2,8})_(?<stage>(LC(0[1-9]|1[0-4])|SB\d{2}))_(?<variant>[A-Z0-9]+(?:-[A-Z0-9]+)*)_(?<desc>[a-z0-9]+(?:-[a-z0-9]+)*)_(?<ver>v\d{2})\.(?<ext>[a-z0-9]{1,6})$
```

### 5.2 Conditional Rules (Mandatory)

CI shall additionally enforce:

* **If `bucket == "00"`** then `stage` matches:
  ```regex
  ^LC(0[1-9]|1[0-4])$
  ```

* **If `bucket != "00"`** then `stage` matches:
  ```regex
  ^SB\d{2}$
  ```

---

## 6. Examples

### 6.1 Valid examples (v2.0 format)

* Lifecycle (LC) plan:
  * `00_00_PLAN_LC02_SPACET_safety-program_v02.md`
* Propulsion FHA (domain bucket with no sub-bucket):
  * `00_70_FHA_SB00_SYS_propulsion_v02.md`
* Software safety requirements:
  * `00_40_REQ_SB00_SW_software-safety-reqs_v02.md`
* Traceability matrix workbook:
  * `00_20_TRC_SPACET_traceability-matrix_v01.xlsx`
* Reference schema:
  * `00_90_SCH_GEN_hazard-log-schema_v01.json`
* Extended ATA code (3-digit ROOT):
  * `115_00_PLAN_LC01_SPACET_supply-chain-plan_v01.md`
  * `116_70_FHA_SB00_SYS_facility-systems_v01.md`

### 6.2 Invalid examples

* Missing LC stage while using lifecycle bucket:
  * `00_00_PLAN_SPACET_safety-program_v01.md` *(non-compliant: BUCKET=00 requires VARIANT prefix `LCxx`)*
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
* **Baseline restriction:** `SPACET` shall only be used for baseline-controlled artifacts; exploratory work shall use `DRAFT` or `PROTO`.

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
