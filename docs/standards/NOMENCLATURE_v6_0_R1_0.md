---
title: "Nomenclature Standard v6.0 (R1.0)"
lifecycle_phase: "All"
generated: "2025-12-17"
standard: "OPT-IN Framework v1.1 / AMPEL360 Space-T"
status: "Normative"
owner: "Configuration Management WG"
revision: "R1.0"
breaking_change: "v6.0 introduces FAMILY/VARIANT/VERSION/MODEL tokens, ISSUE-REVISION format, and updated canonical structure"
supersedes: "v5.0"
---

# Nomenclature Standard v6.0 (R1.0) - Normative

## 1. Purpose

This standard defines the **mandatory** file naming convention for all artifacts within AMPEL360 Space-T. It ensures:

1. **Unambiguous identification** of file content, context, accountability, and governance
2. **Machine-readability** for automated sorting, filtering, indexing, and traceability
3. **CI/CD enforceability** using deterministic validation rules
4. **Strict KNOT governance** through controlled expansion (K01-K14 only)
5. **AoR accountability** aligned with portal entry points
6. **TEKNIA credential governance** with CM/CERT-controlled issuance
7. **Family/variant/version/model classification** for quantum-inspired pax configurations
8. **Issue-revision tracking** for change control

## 2. Filename Format (Canonical v6.0)

All files must strictly adhere to the **canonical format**:

```
[ATA_ROOT]_[PROJECT]_[PROGRAM]_[FAMILY]_[VARIANT]_[VERSION]_[MODEL]_[BLOCK]_[PHASE]_[KNOT_TASK]_[AoR]__[SUBJECT]_[TYPE]_[ISSUE-REVISION]_[STATUS].[EXT]
```

### Breaking changes from v5.0:

* **FAMILY added**: Quantum-inspired + pax payload numbering (e.g., `Q10`, `Q100`)
* **VARIANT redefined**: Now governance lane token (e.g., `GEN`, `BASELINE`, `CERT`)
* **VERSION added**: Branding reinforcer (e.g., `PLUS`, `PLUSULTRA`)
* **MODEL added**: Artifact domain (e.g., `BB`, `HW`, `SW`, `PR`)
* **ISSUE-REVISION added**: Change tracking format `I##-R##` (e.g., `I01-R01`)
* **Position changes**: BLOCK, PHASE, KNOT_TASK, AoR positions shifted
* **Config-driven**: All allowlists in versioned YAML files (`v6_0.yaml`)

## 3. Field Definitions and Constraints

### 3.1 Field Definitions

| Field              | Meaning                                    | Constraint                                    | Example                  |
|:-------------------|:-------------------------------------------|:----------------------------------------------|:-------------------------|
| **ATA_ROOT**       | ATA Chapter or Project Code                | 2 digits for <100, 3 digits for ≥100         | `00`, `27`, `115`        |
| **PROJECT**        | Project Identity                           | Fixed: AMPEL360                               | `AMPEL360`               |
| **PROGRAM**        | Program Identity                           | Fixed: SPACET                                 | `SPACET`                 |
| **FAMILY**         | Quantum Family / Pax Payload               | Allowlist (Q10, Q100, etc.)                   | `Q10`, `Q100`            |
| **VARIANT**        | Governance Lane Token                      | Allowlist (GEN, BASELINE, etc.)               | `GEN`, `CERT`            |
| **VERSION**        | Branding Reinforcer                        | Allowlist (PLUS, PLUSULTRA)                   | `PLUS`, `PLUSULTRA`      |
| **MODEL**          | Artifact Domain                            | Allowlist (BB, HW, SW, PR)                    | `BB`, `HW`, `SW`         |
| **BLOCK**          | Domain Classification / Module             | Controlled vocabulary (config)                | `OPS`, `STR`, `AI`       |
| **PHASE**          | Lifecycle Stage or Sub-bucket              | LC01-LC14 or SB01-SB99                        | `LC03`, `SB04`           |
| **KNOT_TASK**      | Uncertainty Resolution Trigger             | K01-K14 optionally with -T001 to -T999        | `K06`, `K06-T001`        |
| **AoR**            | Area of Responsibility                     | Allowlist (portal entry points)               | `CM`, `CERT`, `SAF`      |
| **SUBJECT**        | Human-readable content label               | lowercase kebab-case                          | `thermal-loop`           |
| **TYPE**           | Artifact Type                              | Controlled vocabulary (config)                | `STD`, `RPT`, `FHA`      |
| **ISSUE-REVISION** | Issue and Revision Numbers                 | I##-R## format                                | `I01-R01`, `I12-R03`     |
| **STATUS**         | Document Status                            | Allowlist (config)                            | `ACTIVE`, `DRAFT`        |
| **EXT**            | File Extension                             | Allowlist (GitHub-first)                      | `md`, `json`, `pdf`      |

### 3.2 General Naming Rules (Mandatory)

* **Delimiters**
  * Use underscore `_` **only** between fields
  * Use double underscore `__` **only** between AoR and SUBJECT
  * Use hyphen `-` **only** inside FAMILY (not applicable in current allowlist), KNOT_TASK (for task suffix), SUBJECT, and ISSUE-REVISION
* **Character set**
  * ASCII only (no accents/diacritics). No spaces
* **Field count and order**
  * Do not add fields; do not remove fields; do not reorder fields
* **Case sensitivity**
  * Fields are case-sensitive as specified in constraints

---

## 4. Allowed Values and Semantics

### 4.1 `[ATA_ROOT]` (Padding Policy)

* `00`-`99`: 2-digit format (e.g., `00`, `24`, `72`)
* `100`-`116`: 3-digit format (e.g., `100`, `115`, `116`)

**Normative rule:** No mixed padding. Always use 2 digits for values <100 and 3 digits for values ≥100.

### 4.2 `[PROJECT]` (Hard Constraint)

**Hard constraint:** `PROJECT` **must** be `AMPEL360` for all files in this repository.

### 4.3 `[PROGRAM]` (Fixed Value)

**Fixed value:** `PROGRAM` **must** be `SPACET` for AMPEL360-SPACE-T.

### 4.4 `[FAMILY]` (Allowlist - Config-Driven) **NEW in v6.0**

**Definition:** Quantum-inspired + pax payload numbering identifier for vehicle family classification.

**Pattern:** `Q[0-9]{2,3}` (e.g., Q10, Q100)

**Initial allowlist:**

* `Q10`: 10-passenger quantum family
* `Q100`: 100-passenger quantum family

**Extension rule:** New FAMILY values require CM change control, config update, and standard revision.

**Governance:** FAMILY expansion requires CM approval and nomenclature standard upgrade.

### 4.5 `[VARIANT]` (Allowlist - Config-Driven) **REDEFINED in v6.0**

**Definition:** Governance lane token indicating configuration variant or mission profile.

**Initial allowlist:**

* `GEN`: General purpose
* `BASELINE`: Baseline configuration
* `FLIGHTTEST`: Flight test variant
* `CERT`: Certification variant
* `MSN`: Mission-specific (with mission number context)
* `HOV`: High-occupancy vehicle
* `CUST`: Customer-specific

**Normalization rule:** No spaces allowed in VARIANT field. Use single token only.

**Extension rule:** New VARIANT values require CM change control and config update.

**v5.0 migration:** v5.0 `PLUS` → v6.0 `GEN` (or context-appropriate mapping)

### 4.6 `[VERSION]` (Allowlist - Config-Driven) **NEW in v6.0**

**Definition:** Branding reinforcer indicating product version line.

**Initial allowlist:**

* `PLUS`: AMPEL360+ standard branding
* `PLUSULTRA`: AMPEL360+ Ultra enhanced branding

**Extension rule:** New VERSION values require CM change control and config update.

**Governance:** VERSION changes require stakeholder communication and brand alignment.

### 4.7 `[MODEL]` (Allowlist - Config-Driven) **NEW in v6.0**

**Definition:** Artifact domain indicating the primary model or discipline focus.

**Initial allowlist:**

* `BB`: Body Brain / PR-O-RO model (integrated vehicle intelligence)
* `HW`: Hardware artifacts
* `SW`: Software artifacts
* `PR`: Process/Procedure artifacts

**Extension rule:** New MODEL values require CM change control and config update.

**Usage guidance:** Select MODEL based on primary artifact domain (may be multi-disciplinary in practice).

### 4.8 `[BLOCK]` (Allowlist - Config-Driven)

**Definition:** Domain classification or subsystem module.

**Allowlist (from v6_0.yaml):**

`OPS`, `STR`, `PROP`, `AI`, `DATA`, `CERT`, `SAF`, `SW`, `HW`, `SYS`, `TEST`, `MRO`, `CIRC`, `ENRG`, `STOR`, `GEN`

**Extension rule:** New BLOCK values require CM change control and config update.

### 4.9 `[PHASE]` (Lifecycle or Subbucket)

**Definition:** Lifecycle stage or subbucket identifier.

**Lifecycle format:** `LC01` to `LC14` (14 lifecycle phases)

**Subbucket format:** `SB01` to `SB99` (99 subbuckets)

**Validation rules:**

* Lifecycle: Available for all blocks
* Subbuckets: Some blocks have restricted ranges (see `phase_block_mapping` in config)

**Examples:**

* `LC03`: Lifecycle phase 3
* `SB04`: Subbucket 4

### 4.10 `[KNOT_TASK]` (Strict Governance)

**Definition:** Uncertainty resolution trigger knot (K01-K14) with optional task suffix.

**Format:** `K{01-14}` or `K{01-14}-T{001-999}`

**Normative rule:** Only `K01` through `K14` are allowed. No other KNOT IDs are valid.

**Task suffix:** Optional `-T###` format (e.g., `-T001`, `-T042`)

**Governance policy:**

* New KNOTs (beyond K14) require **Nomenclature Standard upgrade** and **CM approval**
* Prevents uncontrolled knot proliferation

**Examples:**

* `K06`: Knot 6
* `K06-T001`: Knot 6, Task 1
* `K02`: Knot 2

### 4.11 `[AoR]` (Mandatory - Portal Entry Points)

**Definition:** Area of Responsibility - must match portal entry points exactly.

**Normative rule:** AoR is **mandatory** and must be from approved list.

**Allowlist (from v6_0.yaml):**

`CM`, `CERT`, `SAF`, `SE`, `OPS`, `DATA`, `AI`, `CY`, `TEST`, `MRO`, `SPACEPORT`, `PMO`, `QA`, `SEC`, `LEG`, `FIN`, `PROC`

**Important:** No `STK_` prefix allowed (portal entry points are short form only).

**Extension rule:** New AoR values require CM approval and portal alignment.

### 4.12 `[SUBJECT]` (Human-Readable Label)

**Format:** lowercase kebab-case (e.g., `thermal-loop`, `pressure-bulkhead-trade`)

**Rules:**

* Use lowercase letters and digits only
* Use hyphens to separate words
* Be descriptive but concise
* Avoid redundancy with TYPE

**Examples:**

* `thermal-loop-overview`
* `pressure-bulkhead-trade`
* `certification-authority-basis`
* `model-card-template`

### 4.13 `[TYPE]` (Allowlist - Config-Driven)

**Definition:** Artifact type indicator.

**Baseline allowlist (from v6_0.yaml):**

`IDX`, `STD`, `REQ`, `RPT`, `LST`, `TAB`, `SCH`, `DIA`, `SPEC`, `PLN`, `PROC`, `MAN`, `API`, `CFG`, `JSON`, `YAML`, `FHA`, `PSSA`, `SSA`, `FTA`, `ANA`, `DAL`, `TRC`, `CAT`, `GLO`, `MAT`, `MIN`, `ACT`, `LOG`, `PLAN`

**Extension rule:** New TYPE values require CM approval and config update.

### 4.14 `[ISSUE-REVISION]` (Format I##-R##) **NEW in v6.0**

**Definition:** Issue number and revision number for change tracking.

**Format:** `I{01-99}-R{01-99}`

**Pattern:** `I[0-9]{2}-R[0-9]{2}`

**Rules:**

* Issue number: 01-99 (zero-padded)
* Revision number: 01-99 (zero-padded)
* Use hyphen separator between I## and R##

**Examples:**

* `I01-R01`: Issue 1, Revision 1
* `I12-R03`: Issue 12, Revision 3
* `I05-R10`: Issue 5, Revision 10

**Governance:** CM tracks issue-revision mappings in change control system.

**Default for migration:** `I01-R01` for existing files without issue tracking.

### 4.15 `[STATUS]` (Allowlist - Config-Driven)

**Allowlist:**

`TEMPLATE`, `DRAFT`, `ACTIVE`, `APPROVED`, `RELEASED`, `SUPERSEDED`, `ARCHIVED`

**Semantic rules:**

* `TEMPLATE`: Template file for scaffolding
* `DRAFT`: Work in progress
* `ACTIVE`: Current working version
* `APPROVED`: Reviewed and approved
* `RELEASED`: Formally released baseline
* `SUPERSEDED`: Replaced by newer version
* `ARCHIVED`: Retained for historical record

### 4.16 `[EXT]` (Extension Allowlist - GitHub-First)

**Baseline allowlist:**

`md`, `yml`, `yaml`, `json`, `csv`, `svg`, `png`, `jpg`, `jpeg`, `pdf`, `drawio`

**Extension rule:** New extensions require CM approval and alignment with portal renderers.

---

## 5. TEKNIA Credential Policy (v6.0)

TEKNIA outputs are **separate controlled artifacts** (credentials), not embedded into ordinary filenames beyond TYPE.

### 5.1 Allowed TEKNIA Credential TYPE

* `BADGE`
* `CERT`
* `LIC`

### 5.2 Issuance AoR Restriction

**Normative rule:** Issuance AoR must be **`CM` or `CERT` only**

* Other AoRs may propose credentials, but cannot issue
* Issuance requires review and CM/CERT approval

### 5.3 Binding Requirements (Credential → Subject NKU)

Credentials must bind to target NKUs using:

* `subject_path`: Repo-relative path to target artifact
* `subject_sha256`: SHA-256 hash of target content
* `subject_commit`: Optional Git commit reference

### 5.4 Credential Schema Requirements

* Schemas must be versioned and validated (CI-enforced)
* Credentials must be reviewable and diff-friendly (`.yml` or `.json`)

**Minimum credential fields (normative):**

```yaml
schema_version: "1.0"
issued_by_aor: "CM"  # or "CERT"
issued_by_actor: "string"
issued_at: "2025-12-17T00:00:00Z"  # ISO8601
credential_type: "BADGE"  # or "CERT" or "LIC"
subject_path: "path/to/artifact"
subject_sha256: "sha256_hash_of_content"
subject_commit: "git_commit_sha"  # optional
scope: {}  # structured claims
claims: {}  # structured claims
```

**Schema location:** `config/teknia/credential_schema_v1.yaml`

---

## 6. Enforcement

### 6.1 Primary Regex (Structural Validation v6.0)

```regex
^(?P<ata_root>(?:0[0-9]|[1-9][0-9]|1[0-1][0-6]))_
(?P<project>AMPEL360)_
(?P<program>SPACET)_
(?P<family>Q[0-9]{2,3})_
(?P<variant>[A-Z0-9]+)_
(?P<version>[A-Z]+)_
(?P<model>[A-Z]{2})_
(?P<block>[A-Z0-9]+)_
(?P<phase>(?:LC(?:0[1-9]|1[0-4])|SB(?:0[1-9]|[1-9][0-9])))_
(?P<knot_task>K(?:0[1-9]|1[0-4])(?:-T[0-9]{3})?)_
(?P<aor>[A-Z]+)__
(?P<subject>[a-z0-9]+(?:-[a-z0-9]+)*)_
(?P<type>[A-Z0-9]+)_
(?P<issue_revision>I[0-9]{2}-R[0-9]{2})_
(?P<status>[A-Z]+)
\.(?P<ext>[a-z0-9]{1,6})$
```

### 6.2 Semantic Validation (Config-Driven)

CI must additionally enforce:

1. **ATA_ROOT padding policy**
   * 2 digits for <100
   * 3 digits for ≥100

2. **FAMILY allowlist** (from v6_0.yaml)

3. **VARIANT allowlist** (from v6_0.yaml)

4. **VERSION allowlist** (from v6_0.yaml)

5. **MODEL allowlist** (from v6_0.yaml)

6. **BLOCK allowlist** (from v6_0.yaml)

7. **KNOT_TASK governance**
   * Must be K01-K14 (no other values)
   * Optional -T### suffix

8. **AoR allowlist** (from v6_0.yaml)

9. **TYPE allowlist** (from v6_0.yaml)

10. **ISSUE-REVISION format**
    * Must match `I[0-9]{2}-R[0-9]{2}` pattern

11. **STATUS allowlist** (from v6_0.yaml)

12. **EXT allowlist** (from v6_0.yaml)

13. **Phase-vs-Block mapping** (from v6_0.yaml)
    * Certain blocks may restrict phase ranges

### 6.3 Validation Modes

**v6.0 introduces three validation modes:**

1. **WARN mode**: Report violations without failing (used in pre-release)
2. **REPORT mode**: Generate detailed violation reports for inventory
3. **BLOCK mode**: Fail on any violation (PR-blocking enforcement)

### 6.4 Exemptions (Explicit)

**Exempted files (explicit list):**

* `README.md`, `LICENSE`, `EXAMPLES.md`, `STRUCTURE_SUMMARY.md`
* `.gitignore`, `.gitattributes`, `.gitkeep`, `.editorconfig`
* Validation/generation scripts (see config for full list)

**Exempted directories (implicit):**

* `.git/`, `.github/`, `node_modules/`, `__pycache__/`
* `.pytest_cache/`, `.venv/`, `venv/`, `dist/`, `build/`
* `tools/`, `templates/`, `scripts/`, `docs/`, `config/`

**Exempted patterns:**

* `generate_*.py` (generator scripts)
* `validate_*.py` (validation scripts)
* `*_Agent_Config.(yaml|json|yml)` (agent configs)

---

## 7. Examples

### 7.1 Valid v6.0 Examples

**Lifecycle artifact (thermal overview, Q10 family, general variant, PLUS version, Body Brain model):**
```
27_AMPEL360_SPACET_Q10_GEN_PLUS_BB_OPS_LC03_K06-T001_SE__thermal-loop-overview_STD_I01-R01_ACTIVE.md
```

**Domain artifact (pressure bulkhead trade study, Q100 family, cert variant):**
```
53_AMPEL360_SPACET_Q100_CERT_PLUS_HW_STR_LC07_K02_CERT__pressure-bulkhead-trade_RPT_I02-R01_DRAFT.pdf
```

**AI model card template (Q10, baseline variant, software model):**
```
95_AMPEL360_SPACET_Q10_BASELINE_PLUS_SW_AI_SB04_K11_CM__model-card-template_STD_I01-R01_TEMPLATE.md
```

**Certification authority basis (Q10, certification variant, process model):**
```
00_AMPEL360_SPACET_Q10_CERT_PLUS_PR_CERT_LC10_K01_CERT__certification-authority-basis_PLAN_I01-R01_ACTIVE.md
```

**Software safety requirements (Q100, flight test variant):**
```
00_AMPEL360_SPACET_Q100_FLIGHTTEST_PLUS_SW_SW_SB40_K02_SAF__software-safety-reqs_REQ_I03-R02_APPROVED.md
```

### 7.2 Invalid Examples

**Missing ISSUE-REVISION field (v5.0 format):**
```
27_AMPEL360_SPACET_PLUS_OPS_LC03_K06_SE__thermal-loop_STD_v01_ACTIVE.md
```
❌ Non-compliant: v5.0 format, missing FAMILY/VARIANT/VERSION/MODEL/ISSUE-REVISION

**Invalid KNOT (outside K01-K14 range):**
```
27_AMPEL360_SPACET_Q10_GEN_PLUS_BB_OPS_LC03_K99_SE__thermal-loop_STD_I01-R01_ACTIVE.md
```
❌ Non-compliant: K99 not allowed (only K01-K14)

**Invalid AoR (STK_ prefix):**
```
27_AMPEL360_SPACET_Q10_GEN_PLUS_BB_OPS_LC03_K06_STK_SE__thermal-loop_STD_I01-R01_ACTIVE.md
```
❌ Non-compliant: AoR must not have STK_ prefix

**Single underscore instead of double:**
```
27_AMPEL360_SPACET_Q10_GEN_PLUS_BB_OPS_LC03_K06_SE_thermal-loop_STD_I01-R01_ACTIVE.md
```
❌ Non-compliant: Must use double underscore (__) before SUBJECT

**Invalid FAMILY (not in allowlist):**
```
27_AMPEL360_SPACET_Q50_GEN_PLUS_BB_OPS_LC03_K06_SE__thermal-loop_STD_I01-R01_ACTIVE.md
```
❌ Non-compliant: Q50 not in FAMILY allowlist (only Q10, Q100 initially)

**Invalid ISSUE-REVISION format:**
```
27_AMPEL360_SPACET_Q10_GEN_PLUS_BB_OPS_LC03_K06_SE__thermal-loop_STD_I1-R1_ACTIVE.md
```
❌ Non-compliant: ISSUE-REVISION must be I##-R## with zero-padding (I01-R01, not I1-R1)

---

## 8. Migration from v5.0 to v6.0

### 8.1 Automated Migration Strategy

**High-level approach:**

1. Generate `rename_map_v6.csv` with deterministic mapping rules
2. Apply default values for new fields (FAMILY, VARIANT, VERSION, MODEL, ISSUE-REVISION)
3. Execute batch rename using `git mv`
4. Update cross-references in all documents
5. Validate 100% compliance

### 8.2 Default Value Assignment

**For v5.0 → v6.0 migration:**

| Field           | Default Value | Rationale                                |
|:----------------|:--------------|:-----------------------------------------|
| FAMILY          | `Q10`         | Default to 10-passenger family           |
| VARIANT         | `GEN`         | General purpose unless context indicates |
| VERSION         | `PLUS`        | Default branding                         |
| MODEL           | `BB`          | Body Brain as default integrated model   |
| ISSUE-REVISION  | `I01-R01`     | Initial issue and revision               |

**Special cases:**

* v5.0 `VARIANT=CERT` → v6.0 `VARIANT=CERT` (preserved)
* Context-specific FAMILY/MODEL inference based on ATA_ROOT and BLOCK

### 8.3 Migration Tools

**Required tooling updates:**

1. `validate_nomenclature.py` → v6.0 parsing and validation
2. `scripts/scaffold.py` → v6.0 filename generation
3. `scripts/generate_rename_map_v6.py` → deterministic v5.0 → v6.0 mapping
4. `scripts/execute_rename_v6.py` → safe batch rename with rollback
5. `scripts/update_cross_references_v6.py` → link rewriting

### 8.4 Confidence Scoring

**Mapping confidence thresholds:**

* **High (≥0.95)**: Auto-process
* **Medium (0.80-0.94)**: Manual review recommended
* **Low (<0.80)**: Mandatory manual review

---

## 9. Governance and Change Control

### 9.1 Allowlist Extensions

**Process for extending allowlists:**

1. Submit change request to CM WG
2. Justify new value with use case
3. CM WG reviews and approves/rejects
4. Update `config/nomenclature/v6_0.yaml`
5. Update validator and scaffold tooling
6. Update this specification document
7. Communicate to stakeholders

### 9.2 KNOT Expansion Policy

**Adding new KNOTs beyond K14:**

1. **Requires Nomenclature Standard upgrade** (major change)
2. CM approval mandatory
3. Justification and impact assessment required
4. Update config, tooling, and specification
5. Version bump of standard (e.g., v6.0 → v7.0)

**Rationale:** Prevents uncontrolled knot proliferation and maintains governance.

### 9.3 Version Control

**This specification:**

* Version: **6.0**
* Revision: **R1.0**
* Status: **Normative**
* Supersedes: v5.0
* Change control: CM WG

---

## 10. References

* OPT-IN Framework v1.1
* AMPEL360 Space-T Program Documentation
* ATA Chapter Mapping Specification
* TEKNIA Credential Schema v1.0
* Configuration file: `config/nomenclature/v6_0.yaml`

---

## Appendix A: Field Order Mnemonic

**v6.0 canonical format memory aid:**

```
ATA_ROOT PROJECT PROGRAM | FAMILY VARIANT VERSION MODEL | BLOCK PHASE KNOT_TASK AoR | SUBJECT | TYPE ISSUE-REVISION STATUS
```

**Grouping logic:**

1. **Identity tokens** (3): ATA_ROOT, PROJECT, PROGRAM
2. **Classification tokens** (4): FAMILY, VARIANT, VERSION, MODEL
3. **Governance tokens** (4): BLOCK, PHASE, KNOT_TASK, AoR
4. **Content descriptor** (1): SUBJECT
5. **Metadata tokens** (3): TYPE, ISSUE-REVISION, STATUS

---

## Appendix B: Regex Visualization

**v6.0 pattern breakdown:**

```
[ATA_ROOT:00-116]_
[PROJECT:AMPEL360]_
[PROGRAM:SPACET]_
[FAMILY:Q##|Q###]_
[VARIANT:ALLOWLIST]_
[VERSION:ALLOWLIST]_
[MODEL:BB|HW|SW|PR]_
[BLOCK:ALLOWLIST]_
[PHASE:LC##|SB##]_
[KNOT_TASK:K##(-T###)?]_
[AoR:ALLOWLIST]__
[SUBJECT:kebab-case]_
[TYPE:ALLOWLIST]_
[ISSUE-REVISION:I##-R##]_
[STATUS:ALLOWLIST].
[EXT:ALLOWLIST]
```

---

## Document Control

* **Version**: 6.0
* **Revision**: R1.0
* **Date**: 2025-12-17
* **Status**: Normative
* **Owner**: Configuration Management WG
* **Approvers**: CM WG, CERT (for TEKNIA policy)
* **Distribution**: All AMPEL360 Space-T stakeholders
* **Next Review**: Upon request for allowlist extension or KNOT expansion

---

**END OF SPECIFICATION**
