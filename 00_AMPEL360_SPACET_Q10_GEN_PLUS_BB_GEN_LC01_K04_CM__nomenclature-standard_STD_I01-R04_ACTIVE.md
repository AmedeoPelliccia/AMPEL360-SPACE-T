---
title: "Nomenclature Standard v4.0"
lifecycle_phase: "All"
generated: "2025-12-16"
standard: "OPT-IN Framework v1.1 / AMPEL360 Space-T"
status: "Normative"
owner: "Configuration Management WG"
breaking_change: "v4.0 introduces TRIGGER_KNOT and AoR fields with program-scoped prefix (12-field format)"
---

# Nomenclature Standard v4.0 (Normative)

## 1. Purpose

This standard defines the **mandatory** file naming convention for all artifacts within AMPEL360 Space-T. It ensures:

1. **Unambiguous identification** of file content, context, accountability, and uncertainty triggers.
2. **Machine-readability** for automated sorting, filtering, indexing, and traceability.
3. **CI/CD enforceability** using deterministic regular expressions and validation rules.
4. **Knot-triggered accountability** through explicit TRIGGER_KNOT and AoR (Area of Responsibility) encoding.
5. **Program-scoped prefix** enabling portfolio-scale queryability and cross-program disambiguation.

## 2. Filename Format

All files must strictly adhere to the **12-field format**:

```
[ROOT]_[PROJECT]_[PROGRAM]_[VARIANT]_[BUCKET]_[TYPE]_[LC|SB]_[TRIGGER_KNOT]_[AoR]__[DESCRIPTION]_[VERSION].[EXT]
```

**Breaking changes from v3.0:**
- **Field order changed**: PROJECT, PROGRAM, and VARIANT moved before BUCKET
- **Two new fields**: TRIGGER_KNOT and AoR added after LC|SB
- **Double underscore**: `__` (two underscores) between AoR and DESCRIPTION is mandatory
- **Total fields**: 12 (up from 10 in v3.0)

## 3. Field Definitions and Constraints

### 3.1 Field Definitions

| Field             | Meaning                                   | Constraint                             | Regex                        |
| :---------------- | :---------------------------------------- | :------------------------------------- | :--------------------------- |
| **ROOT**          | ATA Chapter or Project Code               | 2-3 digits                             | `^\d{2,3}$`                  |
| **PROJECT**       | Project Identity                          | Fixed: AMPEL360                        | `^AMPEL360$`                 |
| **PROGRAM**       | Program Identity                          | Fixed: SPACET                          | `^SPACET$`                   |
| **VARIANT**       | Configuration / Baseline                  | uppercase alphanumeric; hyphen allowed | `^[A-Z0-9]+(?:-[A-Z0-9]+)*$` |
| **BUCKET**        | Domain Classification (OPT-IN + LC)       | 2 digits (enum)                        | `^(00\|10\|20\|30\|40\|50\|60\|70\|80\|90)$` |
| **TYPE**          | Artifact Type                             | 2–8 uppercase alphanumeric             | `^[A-Z0-9]{2,8}$`            |
| **LC\|SB**        | Lifecycle Stage or Sub-bucket             | LC01-LC14 or SB15-SB99                 | `^(LC(0[1-9]\|1[0-4])\|SB(1[5-9]\|[2-9]\d))$` |
| **TRIGGER_KNOT**  | Uncertainty Resolution Trigger            | K00 or K01-K99                         | `^K(00\|[0-9]{2})$`          |
| **AoR**           | Area of Responsibility (Portal entry)     | Allowlist (see 4.9)                    | `^(CM\|CERT\|AI\|DATA\|OPS\|SE\|SAF\|PMO\|CY\|TEST\|MRO\|SPACEPORT)$` |
| **DESCRIPTION**   | Human-readable content label              | lowercase kebab-case                   | `^[a-z0-9]+(?:-[a-z0-9]+)*$` |
| **VERSION**       | Revision Control                          | `v` + 2 digits                         | `^v\d{2}$`                   |
| **EXT**           | File Extension                            | lowercase alphanumeric                 | `^[a-z0-9]{1,6}$`            |

### 3.2 General Naming Rules (Mandatory)

* **Delimiters**
  * Use underscore `_` **only** between fields.
  * Use double underscore `__` **only** between AoR and DESCRIPTION.
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

### 4.2 `[PROJECT]` (Project Identity) — Hard Constraint

The `PROJECT` field identifies the portfolio-level project identity.

**Hard constraint:**
* `PROJECT` **must** be `AMPEL360` for all files in this repository
* This ensures filenames are self-describing at portfolio scale
* Future projects in the AMPEL360 portfolio would use the same PROJECT value

**Rationale:**
* Prevents ambiguity when files are shared across organizational boundaries
* Enables portfolio-level aggregation and reporting
* Maintains consistent identity across all AMPEL360 programs

### 4.3 `[PROGRAM]` (Program Identity) — Fixed Value

The `PROGRAM` field identifies the specific program within the AMPEL360 project.

**Fixed value:**
* `PROGRAM` **must** be `SPACET` for AMPEL360-SPACE-T
* Future programs may be added through Configuration Management WG approval

**Rationale:**
* Dedicated `PROGRAM` field enables clear program identity
* Enables multi-program repositories and cross-program queries
* Maintains backward compatibility with portfolio tooling

### 4.4 `[VARIANT]` (Configuration / Baseline)

`VARIANT` encodes the configuration context.

**Recommended baseline tokens:**

* `PLUS`: AMPEL360+ variant (the enhanced AMPEL360-SPACE-T configuration)
* `CERT`: Certification-related artifacts
* `BB`: Body-Brain protorobotics models (protorobotics integration artifacts)
* `DRAFT`: Work in progress (non-baseline)
* `PROTO`: Prototyping artifacts
* `SYS`, `SW`, `HW`: System / Software / Hardware scoped artifacts
* `GEN`: General-purpose artifacts

Hyphenated variants are allowed: `SYS-01`, `SW-PLAT-A`, `CERT-EASA`, `BB-PROTO`.

### 4.5 `[BUCKET]` (2 digits) — Authoritative Allowlist

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

### 4.6 `[TYPE]` (Controlled Vocabulary)

The following set is **approved** for v4.0. Extensions require Configuration Management WG change control.

* **Planning / Control:** `PLAN`, `MIN`, `RPT`, `LOG`, `ACT`, `IDX`
* **Safety Analyses:** `FHA`, `PSSA`, `SSA`, `FTA`, `ANA`
* **Requirements / Allocation:** `REQ`, `DAL`, `TRC`
* **Data / Reference:** `CAT`, `LST`, `GLO`, `MAT`, `SCH`, `DIA`, `TAB`, `STD`

### 4.7 `[LC|SB]` (Lifecycle Stage or Sub-bucket)

This mandatory field encodes either:
- **Lifecycle stage** (LC01-LC14) for `BUCKET=00` files
- **Sub-bucket** identifier (SB15-SB99) for all other buckets

**Conditional rules (mandatory):**

1. **If `BUCKET = 00`** → `LC|SB` **must** match:
   ```regex
   ^LC(0[1-9]|1[0-4])$
   ```
   * Valid: `LC01`, `LC02`, ..., `LC14`
   * Invalid: `SB15`, `LC00`, `LC15`

2. **If `BUCKET ≠ 00`** → `LC|SB` **must** match bucket-specific ranges:
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

### 4.8 `[TRIGGER_KNOT]` (Uncertainty Resolution Trigger) — **NEW in v4.0**

The `TRIGGER_KNOT` field explicitly encodes which uncertainty knot triggered or owns this artifact.

**Mandatory constraint:**
* Must be `K00` (reserved for global/non-knot artifacts) or `K01` through `K99`
* Regex: `^K(00|[0-9]{2})$`

**Semantic rules:**
* `K00`: Global artifacts not tied to a specific knot (e.g., nomenclature standard, program-level plans)
* `K01`-`K99`: Artifacts triggered by or owned by a specific knot

**Examples:**
* `K00`: Nomenclature standard, program baselines, CI configuration
* `K01`: Certification authority basis knot
* `K02`: Hazard analysis and safety case knot
* `K03`: Hazmat and cryo propellants safety knot

**Rationale:**
* Makes uncertainty resolution queryable at scale
* Enables knot-based filtering and aggregation
* Provides accountability chain from knot to artifact
* Supports automated knot closure verification

### 4.9 `[AoR]` (Area of Responsibility / Portal Entry Point) — **NEW in v4.0**

The `AoR` field explicitly encodes the portal entry point responsible for this artifact.

**Mandatory allowlist:**
* `CM`: Configuration Management
* `CERT`: Certification & Authorities
* `AI`: AI/ML Engineering
* `DATA`: Data Governance
* `OPS`: Operations
* `SE`: Systems Engineering
* `SAF`: Safety
* `PMO`: Program Management Office
* `CY`: Cybersecurity
* `TEST`: IVVQ / Testing
* `MRO`: MRO / Maintenance
* `SPACEPORT`: Spaceport/Airport Ops

**Format constraint:**
* Portal entry-point code only (no `STK_` prefix)
* Must match one value from allowlist exactly
* Case-sensitive (uppercase only)

**Rationale:**
* Encodes ownership and accountability directly in filename
* Enables stakeholder-based filtering and queries
* Supports RBAC and access control policies
* Aligns with portal directory structure (`STK_<AoR>-*`)

**Note:** The `STK_` prefix is used in directory names (e.g., `STK_CM-cm-configuration-management/`) but **NOT** in the AoR field of filenames.

### 4.10 `[DESCRIPTION]`

* Must be lowercase kebab-case.
* Must not duplicate semantic content already encoded in `TYPE` or `BUCKET`.
  * Example: avoid `..._FHA_SB70_K02_SAF__propulsion-fha_...` → use `..._FHA_SB70_K02_SAF__propulsion_...`

### 4.11 `[VERSION]`

* Exactly `vNN` where `NN` is two digits (`v01`, `v02`, …).
* Increment `vNN` only per the versioning rules in Section 7.

---

## 5. Enforcement

### 5.1 Primary Regex (PCRE) — 12-Field Format

This regex validates the general filename structure for v4.0:

```regex
^(?<root>\d{2,3})_(?<project>AMPEL360)_(?<program>SPACET)_(?<variant>[A-Z0-9]+(?:-[A-Z0-9]+)*)_(?<bucket>00|10|20|30|40|50|60|70|80|90)_(?<type>[A-Z0-9]{2,8})_(?<lcsb>(LC(0[1-9]|1[0-4])|SB(1[5-9]|[2-9]\d)))_(?<knot>K(00|[0-9]{2}))_(?<aor>CM|CERT|AI|DATA|OPS|SE|SAF|PMO|CY|TEST|MRO|SPACEPORT)__(?<desc>[a-z0-9]+(?:-[a-z0-9]+)*)_(?<ver>v\d{2})\.(?<ext>[a-z0-9]{1,6})$
```

**Key changes from v3.0:**
* Field order: PROJECT, PROGRAM, VARIANT come before BUCKET
* Two new fields: TRIGGER_KNOT and AoR
* Double underscore `__` before DESCRIPTION

### 5.2 Conditional Rules (Mandatory)

CI shall additionally enforce:

* **`project` field** must be exactly `AMPEL360` (hard constraint)

* **`program` field** must be exactly `SPACET` (fixed value)

* **`knot` field** must match `K00` or `K01`-`K99` pattern

* **`aor` field** must be in allowlist (see 4.9)

* **If `bucket == "00"`** then `lcsb` matches:
  ```regex
  ^LC(0[1-9]|1[0-4])$
  ```

* **If `bucket != "00"`** then `lcsb` matches bucket-specific ranges:
  ```regex
  ^SB(1[5-9]|[2-9]\d)$
  ```
  And falls within the bucket's designated range (see section 4.7)

---

## 6. Examples

### 6.1 Valid examples (v4.0 format)

* Lifecycle (LC) plan for AMPEL360+ Space-T (global, CM-owned):
  * `00_AMPEL360_SPACET_PLUS_00_PLAN_LC02_K00_CM__safety-program_v01.md`

* Propulsion FHA (domain bucket with sub-bucket, K02 knot, SAF-owned):
  * `00_AMPEL360_SPACET_PLUS_70_FHA_SB70_K02_SAF__propulsion_v01.md`

* Software safety requirements (K02 knot, SAF-owned):
  * `00_AMPEL360_SPACET_PLUS_40_REQ_SB40_K02_SAF__software-safety-reqs_v01.md`

* Certification authority basis (K01 knot, CERT-owned):
  * `00_AMPEL360_SPACET_CERT_00_PLAN_LC10_K01_CERT__certification-authority-basis_v01.md`

* Reference schema (K00 global, DATA-owned):
  * `00_AMPEL360_SPACET_GEN_90_SCH_SB90_K00_DATA__hazard-log-schema_v01.json`

* Nomenclature standard (K00 global, CM-owned):
  * `00_AMPEL360_SPACET_PLUS_00_STD_LC01_K00_CM__nomenclature-standard_v04.md`

* Compliance workflow diagram (K01 knot, CERT-owned):
  * `00_AMPEL360_SPACET_PLUS_90_DIA_SB90_K01_CERT__compliance-workflow_v01.svg`

* ATA-specific tasklist index (K03 knot, SPACEPORT-owned):
  * `78_AMPEL360_SPACET_PLUS_00_IDX_LC01_K03_SPACEPORT__k03-ata-78-tasklist_v01.md`

* Extended ATA code (3-digit ROOT, K10 knot, OPS-owned):
  * `115_AMPEL360_SPACET_PLUS_00_PLAN_LC01_K10_OPS__supply-chain-plan_v01.md`

### 6.2 Invalid examples

* Missing TRIGGER_KNOT and AoR fields (v3.0 format):
  * `00_00_PLAN_LC02_AMPEL360_SPACET_PLUS_safety-program_v01.md` *(non-compliant: v3.0 format)*

* Wrong field order:
  * `00_00_AMPEL360_SPACET_PLUS_PLAN_LC02_K00_CM__safety-program_v01.md` *(non-compliant: BUCKET before PROJECT)*

* Single underscore before DESCRIPTION:
  * `00_AMPEL360_SPACET_PLUS_00_PLAN_LC02_K00_CM_safety-program_v01.md` *(non-compliant: must use `__`)*

* Invalid TRIGGER_KNOT:
  * `00_AMPEL360_SPACET_PLUS_00_PLAN_LC02_KNOT01_CM__safety-program_v01.md` *(non-compliant: must be K00-K99)*

* Invalid AoR:
  * `00_AMPEL360_SPACET_PLUS_00_PLAN_LC02_K00_STK_CM__safety-program_v01.md` *(non-compliant: no STK_ prefix)*

* AoR not in allowlist:
  * `00_AMPEL360_SPACET_PLUS_00_PLAN_LC02_K00_CUSTOM__safety-program_v01.md` *(non-compliant: AoR must be in allowlist)*

---

## 7. Versioning Strategy (Normative)

* **Version increments:** When an artifact reaches a new controlled state (review gate output, released update, or materially changed content), increment `vNN`.
* **Git history:** Git commits provide authoritative line-level history. Filename version `vNN` denotes a **distinct controlled state** suitable for baselining, gate evidence packaging, and traceability snapshots.
* **Baseline restriction:** Baseline-controlled artifacts shall use `PLUS` or `CERT` variants; exploratory work shall use `DRAFT` or `PROTO`.

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

### 8.4 Scaffolding

Use the scaffolding script to generate v4.0-compliant files:

```bash
python scripts/scaffold.py <ROOT> <PROJECT> <PROGRAM> <VARIANT> <BUCKET> <TYPE> <LC|SB> <KNOT> <AOR> <DESC> <VER>
```

Example:
```bash
python scripts/scaffold.py 00 AMPEL360 SPACET PLUS 00 PLAN LC01 K00 CM safety-program v01
```

---

## 9. Migration from v3.0

### 9.1 Breaking Changes

v4.0 introduces breaking changes that require **full repository retrofit**:

1. **Field order changed**: PROJECT, PROGRAM, VARIANT moved before BUCKET
2. **New fields**: TRIGGER_KNOT and AoR added after LC|SB
3. **Double underscore**: `__` between AoR and DESCRIPTION (was single `_`)
4. **Total fields**: 12 (up from 10 in v3.0)

### 9.2 Migration Process

1. **Update tooling** (validators, scaffolding, CI) to v4.0
2. **Generate rename map** for all existing files
3. **Execute batch rename** with rename map
4. **Update cross-references** in all files (links, indices, manifests)
5. **Verify** with v4.0 validator and link checker
6. **Document** exceptions and statistics in retrofit report

### 9.3 Determining KNOT and AoR Values

**For existing files**, use these heuristics:

* **TRIGGER_KNOT:**
  * Files in `KNOTS/KXX_*/` directories → use `KXX`
  * Files with `kXX-` in description → use `KXX`
  * Global/program-level files → use `K00`
  * Lifecycle control files → use `K00`

* **AoR:**
  * Files in `STK_<AOR>-*/` directories → use `<AOR>`
  * Files owned by specific stakeholder → use that AoR
  * Certification artifacts (VARIANT=CERT) → use `CERT`
  * Safety artifacts (FHA, PSSA, SSA) → use `SAF`
  * Configuration/baseline artifacts → use `CM`
  * Test/verification artifacts → use `TEST`
  * System engineering artifacts → use `SE`
  * Default for ambiguous cases → use `CM`

---

## 10. References

* OPT-IN Framework v1.1
* ATA-SpaceT numbering system
* AMPEL360 Configuration Management Plan
* KNOTS Catalog v01
* Portal Stakeholder Index v01

---

## Revision History

| Version | Date       | Changes                                                                 | Author |
|---------|------------|-------------------------------------------------------------------------|--------|
| v04     | 2025-12-16 | Breaking change: Added TRIGGER_KNOT and AoR fields, reordered fields, double underscore before DESCRIPTION | CM WG  |
| v03     | 2025-12-15 | Added PROJECT and PROGRAM fields (10-field format)                     | CM WG  |
| v02     | 2025-12-14 | Introduced SUBJECT field (LC|SB)                                        | CM WG  |
| v01     | 2025-12-13 | Initial normative standard                                              | CM WG  |

---

**END OF NORMATIVE STANDARD v4.0**
