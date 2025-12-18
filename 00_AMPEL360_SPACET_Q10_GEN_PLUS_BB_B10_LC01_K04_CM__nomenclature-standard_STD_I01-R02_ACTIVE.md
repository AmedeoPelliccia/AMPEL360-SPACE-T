---
title: "Nomenclature Standard v3.0"
lifecycle_phase: "All"
generated: "2025-12-15"
standard: "OPT-IN Framework v1.1 / AMPEL360 Space-T"
status: "Normative"
owner: "Configuration Management WG"
breaking_change: "v3.0 introduces mandatory PROJECT and PROGRAM fields (10-field format)"
---

# Nomenclature Standard v3.0 (Normative)

## 1. Purpose

This standard defines the **mandatory** file naming convention for all artifacts within AMPEL360 Space-T. It ensures:

1. **Unambiguous identification** of file content and context.
2. **Machine-readability** for automated sorting, filtering, indexing, and traceability.
3. **CI/CD enforceability** using deterministic regular expressions and validation rules.
4. **Explicit lifecycle and sub-bucket encoding** through dedicated field.

## 2. Filename Format

All files must strictly adhere to the **10-field format**:

`[ROOT]_[BUCKET]_[TYPE]_[SUBJECT]_[PROJECT]_[PROGRAM]_[VARIANT]_[DESCRIPTION]_[VERSION].[EXT]`

**Breaking changes**:
- **v2.0**: Introduced mandatory `SUBJECT` field (renamed from `LC_OR_SUBBUCKET`)
- **v3.0**: Introduced mandatory `PROJECT` and `PROGRAM` fields between `SUBJECT` and `VARIANT`

## 3. Field Definitions and Constraints

### 3.1 Field Definitions

| Field           | Meaning                               | Constraint                             | Regex                        |
| :-------------- | :------------------------------------ | :------------------------------------- | :--------------------------- |
| **ROOT**        | ATA Chapter or Project Code           | 2-3 digits                             | `^\d{2,3}$`                  |
| **BUCKET**      | Domain Classification (OPT-IN + LC)   | 2 digits (enum)                        | `^(00\|10\|20\|30\|40\|50\|60\|70\|80\|90)$` |
| **TYPE**        | Artifact Type                         | 2–8 uppercase alphanumeric             | `^[A-Z0-9]{2,8}$`            |
| **SUBJECT**     | Lifecycle Stage or Sub-bucket         | LC01-LC14 or SB15-SB99                 | `^(LC(0[1-9]\|1[0-4])\|SB(1[5-9]\|[2-9]\d))$` |
| **PROJECT**     | Project Identity                      | Fixed: AMPEL360                        | `^AMPEL360$`                 |
| **PROGRAM**     | Program Identity                      | Allowlist: SPACET (extensible)         | `^(SPACET)$`                 |
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

### 4.4 `[SUBJECT]` (Lifecycle Stage or Sub-bucket)

This mandatory field encodes either:
- **Lifecycle stage** (LC01-LC14) for `BUCKET=00` files
- **Sub-bucket** identifier (SB15-SB99) for all other buckets

**Conditional rules (mandatory):**

1. **If `BUCKET = 00`** → `SUBJECT` **must** match:
   ```regex
   ^LC(0[1-9]|1[0-4])$
   ```
   * Valid: `LC01`, `LC02`, ..., `LC14`
   * Invalid: `SB15`, `LC00`, `LC15`

2. **If `BUCKET ≠ 00`** → `SUBJECT` **must** match bucket-specific ranges:
   ```regex
   ^SB(1[5-9]|[2-9]\d)$
   ```
   
   **Bucket-specific subbucket ranges:**
   
   | BUCKET | Domain | Allowed Subbuckets |
   |--------|--------|-------------------|
   | `10` | Operations | SB15-SB19, SB80-SB85 |
   | `20` | Primary Subsystem | SB20-SB29 |
   | `30` | Circularity | SB30-SB39 |
   | `40` | Software | SB40-SB49 |
   | `50` | Structures | SB50-SB59 |
   | `60` | Storages | SB60-SB69 |
   | `70` | Propulsion | SB70-SB79 |
   | `80` | Energy | SB86-SB89 |
   | `90` | Tables/Schemas/Diagrams | SB90-SB99 |
   
   * Invalid: `LC01`, `SB00`, `SB01`, ..., `SB14`, `SB`, `SBXX`
   * Invalid: Subbuckets outside the allowed range for the specific BUCKET
   * **Convention**: SB00-SB14 are reserved; each bucket has designated ranges

**Sub-bucket mapping:**
* Each BUCKET uses designated subbucket ranges aligned with the domain
* Ranges are enforced to maintain clear separation between buckets
* Note: SB00-SB14 are reserved and not available for use

### 4.5 `[PROJECT]` (Project Identity) **[NEW in v3.0]**

The `PROJECT` field identifies the portfolio-level project identity.

**Hard constraint:**
* `PROJECT` **must** be `AMPEL360` for all files in this repository
* This ensures filenames are self-describing at portfolio scale
* Future projects in the AMPEL360 portfolio would use the same PROJECT value

**Rationale:**
* Prevents ambiguity when files are shared across organizational boundaries
* Enables portfolio-level aggregation and reporting
* Maintains consistent identity across all AMPEL360 programs

### 4.6 `[PROGRAM]` (Program Identity) **[NEW in v3.0]**

The `PROGRAM` field identifies the specific program within the AMPEL360 project.

**Allowlist (extensible):**
* `SPACET`: Space-T program (AMPEL360-SPACE-T)
* Future programs may be added through Configuration Management WG approval

**Rationale:**
* Previously, `SPACET` was overloaded into the `VARIANT` field
* Dedicated `PROGRAM` field enables clear program identity
* Frees `VARIANT` for its intended purpose (configuration/baseline variants)

### 4.7 `[VARIANT]` (Configuration / Baseline)

`VARIANT` encodes the configuration context, now decoupled from program identity.

**Recommended baseline tokens:**

* `PLUS`: AMPEL360+ variant (the enhanced AMPEL360-SPACE-T configuration)
* `CERT`: Certification-related artifacts
* `DRAFT`: Work in progress (non-baseline)
* `PROTO`: Prototyping artifacts
* `SYS`, `SW`, `HW`: System / Software / Hardware scoped artifacts
* `GEN`: General-purpose artifacts

Hyphenated variants are allowed: `SYS-01`, `SW-PLAT-A`, `CERT-EASA`.

**Breaking change from v2.0:** `SPACET` is no longer a valid VARIANT; it is now the PROGRAM field.

### 4.8 `[DESCRIPTION]`

* Must be lowercase kebab-case.
* Must not duplicate semantic content already encoded in `TYPE` or `BUCKET`.
  * Example: avoid `..._FHA_SB70_AMPEL360_SPACET_PLUS_propulsion-fha_...` → use `..._FHA_SB70_AMPEL360_SPACET_PLUS_propulsion_...`

### 4.9 `[VERSION]`

* Exactly `vNN` where `NN` is two digits (`v01`, `v02`, …).
* Increment `vNN` only per the versioning rules in Section 7.

---

## 5. Enforcement

### 5.1 Primary Regex (PCRE) — 10-Field Format

This regex validates the general filename structure for v3.0:

```regex
^(?<root>\d{2,3})_(?<bucket>00|10|20|30|40|50|60|70|80|90)_(?<type>[A-Z0-9]{2,8})_(?<subject>(LC(0[1-9]|1[0-4])|SB(1[5-9]|[2-9]\d)))_(?<project>AMPEL360)_(?<program>SPACET)_(?<variant>[A-Z0-9]+(?:-[A-Z0-9]+)*)_(?<desc>[a-z0-9]+(?:-[a-z0-9]+)*)_(?<ver>v\d{2})\.(?<ext>[a-z0-9]{1,6})$
```

### 5.2 Conditional Rules (Mandatory)

CI shall additionally enforce:

* **`project` field** must be exactly `AMPEL360` (hard constraint)

* **`program` field** must be in allowlist: `SPACET` (extensible via CM WG)

* **If `bucket == "00"`** then `subject` matches:
  ```regex
  ^LC(0[1-9]|1[0-4])$
  ```

* **If `bucket != "00"`** then `subject` matches bucket-specific ranges:
  ```regex
  ^SB(1[5-9]|[2-9]\d)$
  ```
  And falls within the bucket's designated range (see section 4.4)

---

## 6. Examples

### 6.1 Valid examples (v3.0 format)

* Lifecycle (LC) plan for AMPEL360+ Space-T:
  * `00_00_PLAN_LC02_AMPEL360_SPACET_PLUS_safety-program_I01-R01.md`
* Propulsion FHA (domain bucket with sub-bucket):
  * `00_70_FHA_SB70_AMPEL360_SPACET_PLUS_propulsion_I01-R01.md`
* Software safety requirements:
  * `00_40_REQ_SB40_AMPEL360_SPACET_PLUS_software-safety-reqs_I01-R01.md`
* Traceability matrix workbook:
  * `00_20_TRC_SB20_AMPEL360_SPACET_PLUS_traceability-matrix_I01-R01.xlsx`
* Reference schema:
  * `00_90_SCH_SB90_AMPEL360_SPACET_GEN_hazard-log-schema_I01-R01.json`
* Operations plan:
  * `00_10_PLAN_SB15_AMPEL360_SPACET_GEN_operations-plan_I01-R01.md`
* Energy system FHA:
  * `00_80_FHA_SB86_AMPEL360_SPACET_SYS_energy-system_I01-R01.md`
* Certification artifacts:
  * `00_00_PLAN_LC10_AMPEL360_SPACET_CERT_certification-authority-basis_I01-R01.md`
* Extended ATA code (3-digit ROOT):
  * `115_00_PLAN_LC01_AMPEL360_SPACET_PLUS_supply-chain-plan_I01-R01.md`
  * `116_70_FHA_SB70_AMPEL360_SPACET_SYS_facility-systems_I01-R01.md`

### 6.2 Invalid examples

* Missing PROJECT and PROGRAM fields (v2.0 format):
  * `00_00_PLAN_LC02_SPACET_safety-program_I01-R01.md` *(non-compliant: missing PROJECT/PROGRAM)*
* Wrong PROJECT value:
  * `00_70_FHA_SB70_PROJECT2_SPACET_PLUS_propulsion_I01-R01.md` *(non-compliant: PROJECT must be AMPEL360)*
* Wrong PROGRAM value:
  * `00_70_FHA_SB70_AMPEL360_OTHER_PLUS_propulsion_I01-R01.md` *(non-compliant: PROGRAM must be SPACET)*
* Wrong delimiter:
  * `00-70-FHA-SB70-AMPEL360-SPACET-PLUS-propulsion-v01.md` *(non-compliant: must use `_` between fields)*
* Wrong version format:
  * `00_70_FHA_SB70_AMPEL360_SPACET_PLUS_propulsion_v1.md` *(non-compliant: version must be `vNN`)*
* Invalid bucket:
  * `00_99_LST_SB90_AMPEL360_SPACET_GEN_glossary_I01-R01.md` *(non-compliant: bucket must be in allowlist)*

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
