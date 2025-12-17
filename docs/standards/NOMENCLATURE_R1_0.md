---
title: "Nomenclature Standard R1.0 (v6.0)"
lifecycle_phase: "All"
generated: "2025-12-17"
standard: "OPT-IN Framework v1.1 / AMPEL360 Space-T"
status: "Normative"
owner: "Configuration Management WG"
breaking_change: "R1.0 introduces MODEL, VERSION (BL/TS/GN), and ISSUE-REVISION fields (14-field format)"
---

# Nomenclature Standard R1.0 (v6.0) — Normative

## 1. Purpose

This standard defines the **mandatory** file naming convention for all artifacts within AMPEL360 Space-T. It ensures:

1. **Unambiguous identification** of file content, model variant, version type, and issue tracking.
2. **Machine-readability** for automated sorting, filtering, indexing, and traceability.
3. **CI/CD enforceability** using deterministic regular expressions and validation rules.
4. **Knot-triggered accountability** through explicit KNOT_TASK and AoR (Area of Responsibility) encoding.
5. **Deterministic versioning** with typed versions (baseline/testing/generated) for release control.
6. **Issue tracking integration** via embedded ISSUE-REVISION field.

## 2. Filename Format

All files must strictly adhere to the **15-field format**:

```
[ATA_ROOT]_[PROJECT]_[PROGRAM]_[FAMILY]_[VARIANT]_[VERSION]_[MODEL]_[BLOCK]_[PHASE]_[KNOT_TASK]_[AoR]__[SUBJECT]_[TYPE]_[ISSUE-REVISION]_[STATUS].[EXT]
```

**Breaking changes from v5.0:**
- **FAMILY field added**: Quantum aircraft families (Qx/Qxx pattern only)
- **VARIANT field restructured**: MSN/HOV/CUST added; SYS/HW/SW removed (use MODEL instead)
- **VERSION field replaced**: Simple `vNN` replaced with typed `BLnn`, `TSnn`, or `GNnn`
- **MODEL field added**: System/artifact type classification (BB/HW/SW/PR)
- **ISSUE-REVISION field added**: New `I##-R##` format for issue tracking
- **Total fields**: 15 (up from 12 in v5.0)

**Field Order Logic:**
- High-level identifiers: FAMILY, VARIANT, VERSION
- Implementation detail: MODEL
- Domain classification: BLOCK, PHASE, KNOT_TASK, AoR
- Content description: SUBJECT, TYPE
- Tracking: ISSUE-REVISION, STATUS

## 3. Field Definitions and Constraints

### 3.1 Field Definitions

| Field             | Meaning                                   | Constraint                             | Regex                                |
| :---------------- | :---------------------------------------- | :------------------------------------- | :----------------------------------- |
| **ATA_ROOT**      | ATA Chapter or Project Code               | 2-3 digits                             | `^\d{2,3}$`                          |
| **PROJECT**       | Project Identity                          | Fixed: AMPEL360                        | `^AMPEL360$`                         |
| **PROGRAM**       | Program Identity                          | Fixed: SPACET                          | `^SPACET$`                           |
| **FAMILY**        | Quantum Aircraft Family                   | Qx or Qxx pattern only                 | `^Q[0-9]{1,2}$`                      |
| **VARIANT**       | Configuration / Context                   | Allowlist (PLUS, CERT, MSN, HOV, etc.) | `^[A-Z0-9]+(?:-[A-Z0-9]+)*$`         |
| **VERSION**       | Version Type + Number                     | BLnn, TSnn, or GNnn                    | `^(BL\|TS\|GN)[0-9]{2}$`             |
| **MODEL**         | System/Artifact Type                      | BB, HW, SW, PR                         | `^(BB\|HW\|SW\|PR)$`                 |
| **BLOCK**         | Domain Classification                     | Allowlist (e.g., OPS, STR, AI)         | `^[A-Z0-9]+$`                        |
| **PHASE**         | Lifecycle Stage or Sub-bucket             | LC01-LC14 or SB01-SB99                 | `^(LC(0[1-9]\|1[0-4])\|SB(0[1-9]\|[1-9][0-9]))$` |
| **KNOT_TASK**     | Uncertainty Resolution Trigger            | K01-K14 (optionally with -T###)        | `^K(0[1-9]\|1[0-4])(?:-T[0-9]{3})?$` |
| **AoR**           | Area of Responsibility (Portal entry)     | Allowlist (see 4.10)                   | `^(CM\|CERT\|AI\|DATA\|...)$`        |
| **SUBJECT**       | Human-readable content label              | lowercase kebab-case                   | `^[a-z0-9]+(?:-[a-z0-9]+)*$`         |
| **TYPE**          | Artifact Type                             | Allowlist (see 4.11)                   | `^[A-Z0-9]{2,8}$`                    |
| **ISSUE-REVISION**| Issue and Revision Tracking               | I##-R## format                         | `^I[0-9]{2}-R[0-9]{2}$`              |
| **STATUS**        | Document Status                           | Allowlist (see 4.12)                   | `^[A-Z]+$`                           |
| **EXT**           | File Extension                            | lowercase alphanumeric                 | `^[a-z0-9]{1,6}$`                    |

### 3.2 General Naming Rules (Mandatory)

* **Delimiters**
  * Use underscore `_` **only** between fields.
  * Use double underscore `__` **only** between AoR and SUBJECT.
  * Use hyphen `-` **only** inside `VARIANT` (if needed), inside `SUBJECT`, and in KNOT_TASK suffix.
* **Character set**
  * ASCII only (no accents/diacritics). No spaces.
* **Field count and order**
  * Do not add fields; do not remove fields; do not reorder fields.
* **Case sensitivity**
  * Fields are case-sensitive per specification.
  * SUBJECT must be lowercase kebab-case.

---

## 4. Allowed Values and Semantics

### 4.1 `[ATA_ROOT]` (2-3 digits)

* `00`: General / Project-Level / Cross-Domain
* `01`–`99`: ATA chapter codes (e.g., `24` Electrical, `27` Flight Controls, `72` Engine)
* `100`–`116`: Extended ATA chapter codes (e.g., `115` Supply Chain, `116` Facilities Management)

**Padding rule:**
* 2 digits for values < 100 (e.g., `00`, `27`, `95`)
* 3 digits for values ≥ 100 (e.g., `115`, `116`)

### 4.2 `[PROJECT]` (Project Identity) — Hard Constraint

**Hard constraint:**
* `PROJECT` **must** be `AMPEL360` for all files in this repository
* This ensures filenames are self-describing at portfolio scale

### 4.3 `[PROGRAM]` (Program Identity) — Fixed Value

**Fixed value:**
* `PROGRAM` **must** be `SPACET` for AMPEL360-SPACE-T
* Future programs may be added through Configuration Management WG approval

### 4.4 `[FAMILY]` (Quantum Aircraft Family) — NEW IN R1.0

`FAMILY` identifies the quantum aircraft family using passenger-payload-numbered naming.

**Naming Convention:**
* `Qx` or `Qxx` format: Q + passenger count (1-99)
* Pattern: `^Q[0-9]{1,2}$`
* Examples: Q10 (10 passengers), Q100 (100 passengers - future: Q200, Q300, etc.)

**Current Allowlist:**
* `Q10`: SPACE-T Quantum 10-passenger family (current dev focus)
* `Q100`: AIR-T Quantum 100-passenger family

**Future expansion:**
* Additional quantum families (Q20, Q50, Q200, etc.) via CM approval
* Passenger count directly encoded in family identifier
* **Restriction:** Only Qx/Qxx pattern allowed in FAMILY field

**Governance:**
* New FAMILY values require CM approval
* Only quantum passenger-numbered patterns (Qx/Qxx) permitted
* Extensions require update to `config/nomenclature/r1_0.yaml`

### 4.5 `[MODEL]` (System/Artifact Type) — NEW IN R1.0

`MODEL` classifies the type of system or artifact.

**Allowlist (config-driven):**
* `BB`: Body-Brain - Hybrid protorobotics/cyberphysical systems
* `HW`: Hardware - Physical components, structures, equipment
* `SW`: Software - Code, algorithms, digital systems
* `PR`: Process - Procedures, workflows, methodologies

**Usage Guidelines:**
* Use `BB` for integrated cyberphysical/protorobotics artifacts
* Use `HW` for physical components, structures, mechanical systems
* Use `SW` for software, code, algorithms, digital artifacts
* Use `PR` for procedures, processes, workflows, methodologies

**Note:** This replaces the v5.0 practice of using SYS/HW/SW in VARIANT field.

**Governance:**
* New MODEL values require CM approval
* Extensions require update to `config/nomenclature/r1_0.yaml`

### 4.6 `[VARIANT]` (Configuration / Context)

`VARIANT` encodes the configuration or deployment context.

**Allowlist (config-driven):**
* `PLUS`: AMPEL360+ enhanced configuration (default)
* `CERT`: Certification-related artifacts
* `GEN`: General-purpose artifacts
* `PROTO`: Prototyping artifacts
* `SIM`: Simulation artifacts
* `TEST`: Test artifacts
* `MSN`: Mission-specific configuration
* `HOV`: Head of Version (release management)
* `CUST`: Customer-specific configuration

**Note:** SYS/HW/SW removed from VARIANT - use MODEL field (BB/HW/SW/PR) instead.

Hyphenated variants are allowed: `CERT-EASA`, `CUST-ACME`, `MSN-DEMO`.

### 4.7 `[VERSION]` (Version Type + Number) — CHANGED IN R1.0

The VERSION field now uses **typed versioning** for release control.

**Format:** `(BL|TS|GN)[0-9]{2}`

**Types:**
* **BL** = Baseline: Official released versions (e.g., `BL01`, `BL02`)
* **TS** = Testing: Testing/validation versions (e.g., `TS01`, `TS02`)
* **GN** = Generated: Auto-generated/proposed versions (e.g., `GN01`, `GN02`)

**Examples:**
* `BL01` — First baseline release
* `BL02` — Second baseline release
* `TS01` — First testing version
* `GN01` — First generated/proposed version

**Range:** 01-99 for each type

**Normative rule:** VERSION is **CI-enforced** and must match the pattern `^(BL|TS|GN)[0-9]{2}$`

### 4.8 `[BLOCK]` (Domain Classification)

`BLOCK` indicates the **domain classification** used for filtering and portfolio grouping.

**Allowlist (config-driven):**
* `OPS`: Operations
* `STR`: Structures
* `PROP`: Propulsion
* `AI`: AI/ML Systems
* `DATA`: Data Governance
* `CERT`: Certification
* `SAF`: Safety
* `SW`: Software
* `HW`: Hardware
* `SYS`: Systems Engineering
* `TEST`: Testing/IVVQ
* `MRO`: Maintenance/MRO
* `CIRC`: Circularity
* `ENRG`: Energy
* `STOR`: Storages
* `GEN`: General/Cross-cutting

### 4.9 `[PHASE]` (Lifecycle Stage or Sub-bucket)

This mandatory field encodes either:

* **Lifecycle stages (LC01-LC14)**: For lifecycle-specific deliverables
* **Sub-buckets (SB01-SB99)**: For domain-specific categorization

**LC stages:**
* `LC01`: Concept
* `LC02`: Feasibility
* `LC03`: Preliminary Design
* `LC04`: Detailed Design
* `LC05`: Manufacturing/Build
* `LC06`: Integration
* `LC07`: Verification
* `LC08`: Validation
* `LC09`: Certification
* `LC10`: Production
* `LC11`: Operations
* `LC12`: Maintenance
* `LC13`: Modification/Upgrade
* `LC14`: Retirement/Disposal

**SB sub-buckets:**
* `SB01-SB99`: Block-specific categorization (see config for block-specific ranges)

### 4.10 `[KNOT_TASK]` (Uncertainty Resolution Trigger)

**Format:** `K01-K14` optionally with `-T###` suffix

**Governance (STRICT):**
* **Only K01 through K14 are allowed** in R1.0
* K00, K15-K99 are **NOT valid**
* Optional task suffix: `-T001` through `-T999`
* New knots require **standard upgrade + CM approval**

**Examples:**
* `K01` — Knot 1
* `K06` — Knot 6
* `K06-T001` — Knot 6, Task 1
* `K14` — Knot 14 (maximum)

**Invalid:**
* `K00` — Not allowed
* `K15` — Beyond R1.0 governance boundary
* `K99` — Not allowed

### 4.11 `[AoR]` (Area of Responsibility) — MANDATORY

`AoR` identifies the portal entry point and responsible area.

**Allowlist (config-driven):**
* `CM`: Configuration Management
* `CERT`: Certification & Authorities
* `SAF`: Safety
* `SE`: Systems Engineering
* `OPS`: Operations
* `DATA`: Data Governance
* `AI`: AI/ML Engineering
* `CY`: Cybersecurity
* `TEST`: IVVQ / Testing
* `MRO`: MRO / Maintenance
* `SPACEPORT`: Spaceport/Airport Operations
* `PMO`: Program Management Office
* `QA`: Quality Assurance
* `SEC`: Security
* `LEG`: Legal
* `FIN`: Finance
* `PROC`: Procurement

**Normative rules:**
* AoR is **mandatory** (no omission)
* **No `STK_` prefix** in filenames (e.g., use `CM`, not `STK_CM`)
* Must match portal entry points exactly

### 4.12 `[TYPE]` (Artifact Type) — Controlled Vocabulary

The following set is **approved** for R1.0. Extensions require Configuration Management WG change control.

**Planning / Control:**
* `IDX`: Indexes and catalogs
* `STD`: Standards and specifications
* `PLAN`: Plans (project, safety, management)
* `MIN`: Meeting minutes
* `RPT`: Reports and assessments
* `LOG`: Logs (issue, event, hazard)
* `ACT`: Action item registers

**Safety Analyses:**
* `FHA`: Functional Hazard Assessment
* `PSSA`: Preliminary System Safety Assessment
* `SSA`: System Safety Assessment
* `FTA`: Fault Tree Analysis
* `ANA`: Engineering analysis and trade studies

**Requirements / Allocation:**
* `REQ`: Requirements specifications
* `DAL`: Development Assurance Level assignments
* `TRC`: Traceability matrices

**Data / Reference:**
* `CAT`: Catalogs
* `LST`: Lists and inventories
* `GLO`: Glossaries and terminology
* `MAT`: Material specifications
* `SCH`: Data schemas (JSON, XML)
* `DIA`: Diagrams and flowcharts
* `TAB`: Data tables

**Technical Artifacts:**
* `SPEC`: Technical specifications
* `PLN`: Technical plans
* `PROC`: Procedures
* `MAN`: Manuals
* `API`: API documentation
* `CFG`: Configuration files

### 4.13 `[ISSUE-REVISION]` (Issue and Revision Tracking) — NEW IN R1.0

The ISSUE-REVISION field embeds issue tracking information in the filename.

**Format:** `I##-R##`

**Components:**
* `I##`: Issue number (00-99)
* `R##`: Revision number (00-99)

**Examples:**
* `I00-R00`: No issue/initial version
* `I01-R01`: Issue 1, Revision 1
* `I05-R03`: Issue 5, Revision 3
* `I12-R15`: Issue 12, Revision 15

**Normative rules:**
* Format is **CI-enforced** and must match pattern `^I[0-9]{2}-R[0-9]{2}$`
* Both issue and revision must be 2-digit zero-padded
* Use `I00-R00` for artifacts not tied to a specific issue

### 4.14 `[STATUS]` (Document Status)

`STATUS` indicates the lifecycle status of the artifact.

**Allowlist (config-driven):**
* `TEMPLATE`: Template file for scaffolding
* `DRAFT`: Work in progress
* `ACTIVE`: Current working version
* `APPROVED`: Reviewed and approved
* `RELEASED`: Formally released baseline
* `SUPERSEDED`: Replaced by newer version
* `ARCHIVED`: Retained for historical record

### 4.15 `[EXT]` (File Extension)

**GitHub-first policy:** Only extensions that render well in GitHub.

**Allowlist (config-driven):**
* `md`: Markdown
* `yml`, `yaml`: YAML
* `json`: JSON
* `csv`: CSV
* `svg`, `png`, `jpg`, `jpeg`: Graphics
* `pdf`: PDF documents
* `drawio`: Draw.io diagrams

---

## 5. Complete Examples

### 5.1 Valid R1.0 Filenames

```
00_AMPEL360_SPACET_Q10_PLUS_BL01_SW_GEN_LC01_K04_CM__nomenclature-standard_STD_I00-R00_ACTIVE.md
27_AMPEL360_SPACET_Q10_PLUS_BL01_HW_OPS_LC03_K06-T001_SE__thermal-loop-overview_STD_I01-R01_ACTIVE.md
53_AMPEL360_SPACET_Q100_CERT_BL02_HW_STR_LC07_K02_CERT__pressure-bulkhead-trade_RPT_I03-R02_DRAFT.pdf
95_AMPEL360_SPACET_Q10_PROTO_TS01_BB_AI_SB04_K11_CM__model-card-template_STD_I00-R00_TEMPLATE.md
00_AMPEL360_SPACET_Q10_CERT_BL01_PR_CERT_LC10_K01_CERT__certification-authority-basis_PLAN_I00-R00_ACTIVE.md
115_AMPEL360_SPACET_Q10_GEN_GN01_SW_DATA_SB90_K05_DATA__supply-chain-schema_SCH_I02-R01_ACTIVE.json
```

### 5.2 Invalid Filenames (with reasons)

```
# Missing FAMILY and MODEL fields (v5.0 format)
00_AMPEL360_SPACET_PLUS_GEN_LC01_K04_CM__nomenclature-standard_STD_v01_ACTIVE.md

# Wrong field order (MODEL before VARIANT)
00_AMPEL360_SPACET_Q10_SW_PLUS_BL01_GEN_LC01_K04_CM__nomenclature-standard_STD_I00-R00_ACTIVE.md

# Missing MODEL field (14-field format, not 15)
00_AMPEL360_SPACET_Q10_PLUS_BL01_GEN_LC01_K04_CM__nomenclature-standard_STD_I00-R00_ACTIVE.md

# Wrong VERSION format (should be BL/TS/GN)
00_AMPEL360_SPACET_Q10_PLUS_v01_SW_GEN_LC01_K04_CM__nomenclature-standard_STD_I00-R00_ACTIVE.md

# Missing ISSUE-REVISION field
00_AMPEL360_SPACET_Q10_PLUS_BL01_SW_GEN_LC01_K04_CM__nomenclature-standard_STD_ACTIVE.md

# Invalid FAMILY (GEN not allowed - use Qx/Qxx only)
00_AMPEL360_SPACET_GEN_PLUS_BL01_SW_GEN_LC01_K04_CM__nomenclature-standard_STD_I00-R00_ACTIVE.md

# Invalid MODEL (SYS not allowed - use BB/HW/SW/PR only)
00_AMPEL360_SPACET_Q10_PLUS_BL01_SYS_GEN_LC01_K04_CM__nomenclature-standard_STD_I00-R00_ACTIVE.md

# Invalid KNOT (K99 not allowed)
27_AMPEL360_SPACET_Q10_PLUS_BL01_OPS_LC03_K99_SE__thermal-loop_STD_I00-R00_ACTIVE.md

# STK_ prefix not allowed
27_AMPEL360_SPACET_Q10_PLUS_BL01_OPS_LC03_K06_STK_SE__thermal-loop_STD_I00-R00_ACTIVE.md

# Single underscore (must be __)
27_AMPEL360_SPACET_Q10_PLUS_BL01_OPS_LC03_K06_SE_thermal-loop_STD_I00-R00_ACTIVE.md

# Wrong ISSUE-REVISION format (should be I##-R##)
27_AMPEL360_SPACET_Q10_PLUS_BL01_OPS_LC03_K06_SE__thermal-loop_STD_I1-R1_ACTIVE.md
```

---

## 6. Normative Constraints (Non-Negotiable)

### 6.1 Knot Governance (CM-controlled)

* Filenames MUST contain **only** `K01..K14` (no other Knot IDs).
* Optional task suffix allowed only as `-T###` (e.g., `K06-T001`).
* Any new Knot requires **standard upgrade + CM approval** (change control).

### 6.2 AoR Mandatory (Portal Entry Points)

* AoR MUST be one of the **portal entry point codes** (allowlist, config-driven).
* No `STK_` prefix in filenames.

### 6.3 NKU Implicit; TEKNIA Controlled

* NKU MUST NOT appear in filename (implicit).
* TEKNIA outputs are controlled credentials (BADGE/CERT/LIC) governed by CM (and CERT for issuance).

### 6.4 VERSION Pattern (CI-Enforced)

* VERSION MUST match pattern `^(BL|TS|GN)[0-9]{2}$`
* Only BL (baseline), TS (testing), or GN (generated) prefixes allowed

### 6.5 ISSUE-REVISION Format (CI-Enforced)

* ISSUE-REVISION MUST match pattern `^I[0-9]{2}-R[0-9]{2}$`
* Both issue and revision must be 2-digit zero-padded

---

## 7. Exemptions

Certain files are **explicitly exempt** from nomenclature validation:

* **Root-level documentation:** `README.md`, `LICENSE`, `EXAMPLES.md`, etc.
* **Configuration/tooling artifacts:** `.gitignore`, `rename_map*.csv`, `generate_*.py`, etc.
* **Directories:** `.git`, `.github`, `scripts`, `templates`, `docs`, `config`, `node_modules`, `__pycache__`, etc.

See `config/nomenclature/r1_0.yaml` for the complete exemption list.

**No implicit exemptions:** All exemptions must be explicitly declared in the config file.

---

## 8. Validation and Enforcement

### 8.1 Validation Tool

* `validate_nomenclature.py --standard R1.0` validates files against R1.0
* Supports three modes:
  * `--mode warn`: Report violations but do not fail
  * `--mode block`: Fail on any violation (PR-blocking)
  * `--mode report`: Generate detailed report

### 8.2 CI/CD Integration

* GitHub Actions workflow validates all files on push/PR
* Initially runs in **warn mode** (PR^3-1 phase)
* Transitions to **block mode** after retrofit (PR^3-2 phase)
* Final enforcement in **block mode** (PR^3-3 phase)

### 8.3 Pre-commit Hooks

* Local validation before commit
* Prevents accidental non-compliant commits
* Uses same validator as CI

---

## 9. Migration from v5.0 to R1.0

### 9.1 Key Differences

| Aspect | v5.0 (12 fields) | R1.0 (14 fields) |
|--------|------------------|------------------|
| Fields | 12 | 14 |
| MODEL | N/A | Required |
| VERSION | `vNN` | `(BL\|TS\|GN)NN` |
| ISSUE-REVISION | N/A | `I##-R##` |
| Pattern | `[ATA]_[PROJ]_[PROG]_[VAR]_[BLOCK]_[PHASE]_[KNOT]_[AoR]__[SUBJ]_[TYPE]_[VER]_[STATUS]` | `[ATA]_[PROJ]_[PROG]_[MODEL]_[VAR]_[VER]_[BLOCK]_[PHASE]_[KNOT]_[AoR]__[SUBJ]_[TYPE]_[I-R]_[STATUS]` |

### 9.2 Migration Strategy

1. **Default MODEL:** `GEN` for existing files
2. **Version mapping:** `v01` → `BL01`, `v02` → `BL02` (assume baseline)
3. **Default ISSUE-REVISION:** `I00-R00` for existing files
4. **Automated tooling:** `scripts/generate_rename_map_v6.py` generates deterministic mapping
5. **Confidence scoring:** High-confidence renames automated, low-confidence reviewed manually

### 9.3 PR^3 Process

* **PR^3-1 (Pre-Release):** Spec + tooling + warn mode
* **PR^3-2 (Retrofit):** Mass rename + cross-ref rewrite + block mode
* **PR^3-3 (Predicted Release):** Freeze + final verification + release

---

## 10. Change Control

### 10.1 Governance Authority

* **Owner:** Configuration Management Working Group (CM WG)
* **Approval required for:**
  * New MODEL values
  * New VARIANT values
  * New BLOCK values
  * New AoR values
  * New TYPE values
  * New STATUS values
  * New file extensions
  * New KNOT IDs (requires standard upgrade)
  * VERSION pattern changes
  * ISSUE-REVISION format changes

### 10.2 Change Process

1. Submit change request to CM WG
2. Review and approval
3. Update `config/nomenclature/r1_0.yaml`
4. Update tooling (validators, scaffolding)
5. Update documentation
6. Announce to stakeholders

---

## 11. References

* **Config file:** `config/nomenclature/r1_0.yaml`
* **Quick reference:** `docs/standards/NOMENCLATURE_R1_0_QUICKREF.md`
* **Validator:** `validate_nomenclature.py`
* **Scaffolder:** `scripts/scaffold.py`
* **CI workflow:** `.github/workflows/nomenclature-validation.yml`
* **Agent instructions:** `.github/copilot-instructions.md`

---

## 12. Revision History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| R1.0 (v6.0) | 2025-12-17 | Initial R1.0 release with MODEL, VERSION (BL/TS/GN), ISSUE-REVISION fields | CM WG |

---

**END OF NORMATIVE DOCUMENT**
