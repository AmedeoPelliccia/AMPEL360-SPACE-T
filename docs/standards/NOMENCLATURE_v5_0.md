---
title: "Nomenclature Standard v5.0"
lifecycle_phase: "All"
generated: "2025-12-17"
standard: "OPT-IN Framework v1.1 / AMPEL360 Space-T"
status: "Normative"
owner: "Configuration Management WG"
breaking_change: "v5.0 introduces strict KNOT governance (K01-K14 only), mandatory AoR, TEKNIA credential policy, and new canonical format"
supersedes: "v4.0"
---

# Nomenclature Standard v5.0 (Normative)

## 1. Purpose

This standard defines the **mandatory** file naming convention for all artifacts within AMPEL360 Space-T. It ensures:

1. **Unambiguous identification** of file content, context, accountability, and governance
2. **Machine-readability** for automated sorting, filtering, indexing, and traceability
3. **CI/CD enforceability** using deterministic validation rules
4. **Strict KNOT governance** through controlled expansion (K01-K14 only)
5. **AoR accountability** aligned with portal entry points
6. **TEKNIA credential governance** with CM/CERT-controlled issuance

## 2. Filename Format (Canonical v5.0)

All files must strictly adhere to the **canonical format**:

```
[ATA_ROOT]_[PROJECT]_[PROGRAM]_[VARIANT]_[BLOCK]_[PHASE]_[KNOT_TASK]_[AoR]__[SUBJECT]_[TYPE]_[VERSION]_[STATUS].[EXT]
```

### Breaking changes from v4.0:

* **KNOT governance**: Only `K01..K14` allowed (no K15-K99); optional `-T###` task suffix
* **AoR mandatory**: Portal entry points only (no `STK_` prefix)
* **New fields**: BLOCK (replaces BUCKET concept), STATUS added
* **PHASE field**: Replaces LC|SB with stricter governance
* **TEKNIA policy**: Separate credential artifacts with schema validation
* **Config-driven**: All allowlists in versioned YAML files

## 3. Field Definitions and Constraints

### 3.1 Field Definitions

| Field            | Meaning                                   | Constraint                                    | Example              |
|:-----------------|:------------------------------------------|:----------------------------------------------|:---------------------|
| **ATA_ROOT**     | ATA Chapter or Project Code               | 2 digits for <100, 3 digits for ≥100         | `00`, `27`, `115`    |
| **PROJECT**      | Project Identity                          | Fixed: AMPEL360                               | `AMPEL360`           |
| **PROGRAM**      | Program Identity                          | Fixed: SPACET                                 | `SPACET`             |
| **VARIANT**      | Configuration / Baseline                  | Allowlist (config-driven)                     | `PLUS`, `CERT`       |
| **BLOCK**        | Domain Classification / Module            | Controlled vocabulary (config)                | `OPS`, `STR`, `AI`   |
| **PHASE**        | Lifecycle Stage or Sub-bucket             | LC01-LC14 or SB01-SB99                        | `LC03`, `SB04`       |
| **KNOT_TASK**    | Uncertainty Resolution Trigger            | K01-K14 optionally with -T001 to -T999        | `K06`, `K06-T001`    |
| **AoR**          | Area of Responsibility                    | Allowlist (portal entry points)               | `CM`, `CERT`, `SAF`  |
| **SUBJECT**      | Human-readable content label              | lowercase kebab-case                          | `thermal-loop`       |
| **TYPE**         | Artifact Type                             | Controlled vocabulary (config)                | `STD`, `RPT`, `FHA`  |
| **VERSION**      | Revision Control                          | `v` + 2 digits                                | `v01`, `v02`         |
| **STATUS**       | Document Status                           | Allowlist (config)                            | `ACTIVE`, `DRAFT`    |
| **EXT**          | File Extension                            | Allowlist (GitHub-first)                      | `md`, `json`, `pdf`  |

### 3.2 General Naming Rules (Mandatory)

* **Delimiters**
  * Use underscore `_` **only** between fields
  * Use double underscore `__` **only** between AoR and SUBJECT
  * Use hyphen `-` **only** inside VARIANT, KNOT_TASK (for task suffix), and SUBJECT
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

### 4.4 `[VARIANT]` (Allowlist - Config-Driven)

**Baseline variants (initial allowlist):**

* `PLUS`: AMPEL360+ enhanced configuration (default)

**Extension rule:** Additional variants require CM change control and config update.

**Rationale:** Controlled variants prevent proliferation and ensure governance.

### 4.5 `[BLOCK]` (Controlled Vocabulary - Config-Driven)

`BLOCK` replaces the previous BUCKET concept with more flexible domain classification.

**Initial allowlist:** Defined in `config/nomenclature/v5_0.yaml`

Example blocks: `OPS`, `STR`, `PROP`, `AI`, `DATA`, `CERT`, `SAF`

**Extension rule:** New blocks require CM approval and config update.

### 4.6 `[PHASE]` (Lifecycle or Subbucket)

This mandatory field encodes either:
- **Lifecycle stage** (LC01-LC14) for lifecycle artifacts
- **Sub-bucket** identifier (SB01-SB99) for domain artifacts

**Format patterns:**

* **Lifecycle:** `LC01` through `LC14`
  * Regex: `^LC(0[1-9]|1[0-4])$`
  * Valid: `LC01`, `LC02`, ..., `LC14`

* **Subbucket:** `SB01` through `SB99`
  * Regex: `^SB(0[1-9]|[1-9][0-9])$`
  * Valid: `SB01`, `SB02`, ..., `SB99`

**Conditional rules:**

1. Lifecycle artifacts (e.g., BLOCK=OPS with lifecycle scope) should use `LC01-LC14`
2. Domain artifacts within a block should use `SB01-SB99`
3. Bucket-to-subbucket mapping is defined in config (allows controlled ranges per block)

### 4.7 `[KNOT_TASK]` (Strict Governance - K01..K14 Only)

**CRITICAL GOVERNANCE RULE:**

* **No KNOT IDs outside `K01..K14`** are allowed in filenames
* Any **new Knot** requires a **Nomenclature Standard upgrade** and **CM approval**
* Optional task suffix: `-T###` where `###` is `001..999`

**Valid formats:**

* `K01` through `K14` (knot identifier)
* `K01-T001` through `K14-T999` (knot with task suffix)

**Regex pattern:** `^K(0[1-9]|1[0-4])(?:-T[0-9]{3})?$`

**Invalid examples:**

* `K00` (reserved for v4.0 compatibility but not allowed in v5.0)
* `K15`, `K99` (outside allowed range)
* `K01-001` (must use `-T` prefix)

**Rationale:**

* Prevents uncontrolled knot proliferation
* Enforces governance through CM change control
* Maintains manageable knot catalog

### 4.8 `[AoR]` (Mandatory - Portal Entry Points)

The `AoR` field explicitly encodes the portal entry point responsible for this artifact.

**Mandatory allowlist (initial set):**

`CM`, `CERT`, `SAF`, `SE`, `OPS`, `DATA`, `AI`, `CY`, `TEST`, `MRO`, `SPACEPORT`, `PMO`, `QA`, `SEC`, `LEG`, `FIN`, `PROC`

**Format constraints:**

* Portal entry-point code only (no `STK_` prefix)
* Must match one value from allowlist exactly
* Case-sensitive (uppercase only)

**Extension rule:** New AoR values require CM approval and config update.

**Rationale:**

* Encodes ownership and accountability directly in filename
* Aligns with portal directory structure
* Supports RBAC and access control policies

### 4.9 `[SUBJECT]` (Double Underscore Separator)

* Must be lowercase kebab-case: `^[a-z0-9]+(?:-[a-z0-9]+)*$`
* Must be preceded by `__` (double underscore separator)
* Must not duplicate semantic content already encoded in TYPE or BLOCK

**Examples:**

* `__thermal-loop-overview` ✅
* `__propulsion-fha` ❌ (redundant with TYPE=FHA)
* `__propulsion` ✅ (use instead)

### 4.10 `[TYPE]` (Controlled Vocabulary - Config-Driven)

**Baseline TYPE allowlist:**

`IDX`, `STD`, `REQ`, `RPT`, `LST`, `TAB`, `SCH`, `DIA`, `SPEC`, `PLN`, `PROC`, `MAN`, `API`, `CFG`, `JSON`, `YAML`, `FHA`, `PSSA`, `SSA`, `FTA`, `ANA`, `DAL`, `TRC`, `CAT`, `GLO`, `MAT`, `MIN`, `ACT`, `LOG`

**Extension rule:** New TYPE values require CM approval and config update.

### 4.11 `[VERSION]`

* Exactly `vNN` where `NN` is two digits (`v01`, `v02`, ..., `v99`)
* Increment version when artifact reaches a new controlled state

### 4.12 `[STATUS]` (New in v5.0)

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

### 4.13 `[EXT]` (Extension Allowlist - GitHub-First)

**Baseline allowlist:**

`md`, `yml`, `yaml`, `json`, `csv`, `svg`, `png`, `jpg`, `jpeg`, `pdf`, `drawio`

**Extension rule:** New extensions require CM approval and alignment with portal renderers.

---

## 5. TEKNIA Credential Policy (v5.0)

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

### 6.1 Primary Regex (Structural Validation)

```regex
^(?P<ata_root>(?:0[0-9]|[1-9][0-9]|1[0-1][0-6]))_
(?P<project>AMPEL360)_
(?P<program>SPACET)_
(?P<variant>[A-Z0-9]+(?:-[A-Z0-9]+)*)_
(?P<block>[A-Z0-9]+)_
(?P<phase>(?:LC(?:0[1-9]|1[0-4])|SB(?:0[1-9]|[1-9][0-9])))_
(?P<knot_task>K(?:0[1-9]|1[0-4])(?:-T[0-9]{3})?)_
(?P<aor>[A-Z]+)__
(?P<subject>[a-z0-9]+(?:-[a-z0-9]+)*)_
(?P<type>[A-Z0-9]+)_
(?P<version>v[0-9]{2})_
(?P<status>[A-Z]+)
\.(?P<ext>[a-z0-9]{1,6})$
```

### 6.2 Semantic Validation (Config-Driven)

CI must additionally enforce:

1. **ATA_ROOT padding policy**
   * 2 digits for <100
   * 3 digits for ≥100

2. **VARIANT allowlist** (from config)

3. **BLOCK allowlist** (from config)

4. **KNOT_TASK governance**
   * Must be K01-K14 (no other values)
   * Optional -T### suffix

5. **AoR allowlist** (from config)

6. **TYPE allowlist** (from config)

7. **STATUS allowlist** (from config)

8. **EXT allowlist** (from config)

9. **Phase-vs-Block mapping** (from config)
   * Certain blocks may restrict phase ranges

### 6.3 Exemptions (Explicit)

**Exempted files (explicit list):**

* `README.md`, `LICENSE`, `EXAMPLES.md`, `STRUCTURE_SUMMARY.md`
* `.gitignore`, `.gitattributes`
* `.gitkeep`, `.editorconfig`

**Exempted directories (implicit):**

* `.git/`, `.github/`, `node_modules/`, `__pycache__/`
* `.pytest_cache/`, `.venv/`, `venv/`, `dist/`, `build/`
* `tools/` (utility scripts and tooling)

**Exempted patterns:**

* `generate_*.py` (generator scripts)
* `validate_*.py` (validation scripts)
* `*_Agent_Config.(yaml|json|yml)` (agent configs)

---

## 7. Examples

### 7.1 Valid v5.0 Examples

**Lifecycle artifact (thermal overview):**
```
27_AMPEL360_SPACET_PLUS_OPS_LC03_K06-T001_SE__thermal-loop-overview_STD_v01_ACTIVE.md
```

**Domain artifact (pressure bulkhead trade study):**
```
53_AMPEL360_SPACET_PLUS_STR_LC07_K02_CERT__pressure-bulkhead-trade_RPT_v02_DRAFT.pdf
```

**AI model card template:**
```
95_AMPEL360_SPACET_PLUS_AI_SB04_K11_CM__model-card-template_STD_v01_TEMPLATE.md
```

**Certification authority basis:**
```
00_AMPEL360_SPACET_PLUS_CERT_LC10_K01_CERT__certification-authority-basis_PLAN_v01_ACTIVE.md
```

**Software safety requirements:**
```
00_AMPEL360_SPACET_PLUS_SW_SB40_K02_SAF__software-safety-reqs_REQ_v01_APPROVED.md
```

### 7.2 Invalid Examples

**Missing STATUS field (v4.0 format):**
```
27_AMPEL360_SPACET_PLUS_OPS_LC03_K06_SE__thermal-loop_STD_v01.md
```
❌ Non-compliant: Missing STATUS field

**Invalid KNOT (outside K01-K14 range):**
```
27_AMPEL360_SPACET_PLUS_OPS_LC03_K99_SE__thermal-loop_STD_v01_ACTIVE.md
```
❌ Non-compliant: K99 not allowed (only K01-K14)

**Invalid AoR (STK_ prefix):**
```
27_AMPEL360_SPACET_PLUS_OPS_LC03_K06_STK_SE__thermal-loop_STD_v01_ACTIVE.md
```
❌ Non-compliant: No STK_ prefix allowed

**Single underscore before SUBJECT:**
```
27_AMPEL360_SPACET_PLUS_OPS_LC03_K06_SE_thermal-loop_STD_v01_ACTIVE.md
```
❌ Non-compliant: Must use `__` (double underscore)

**Invalid KNOT task format:**
```
27_AMPEL360_SPACET_PLUS_OPS_LC03_K06-001_SE__thermal-loop_STD_v01_ACTIVE.md
```
❌ Non-compliant: Task suffix must be `-T001` not `-001`

---

## 8. Controlled Lists Configuration

All controlled lists (allowlists) are published as versioned config files:

**Primary config:** `config/nomenclature/v5_0.yaml`

**Config schema:**

```yaml
version: "5.0"
date: "2025-12-17"

allowlists:
  variants:
    - PLUS
    # Extend via CM change control
  
  blocks:
    - OPS
    - STR
    - PROP
    - AI
    - DATA
    - CERT
    - SAF
    # Extend via CM change control
  
  aors:
    - CM
    - CERT
    - SAF
    - SE
    - OPS
    - DATA
    - AI
    - CY
    - TEST
    - MRO
    - SPACEPORT
    - PMO
    - QA
    - SEC
    - LEG
    - FIN
    - PROC
  
  types:
    - IDX
    - STD
    - REQ
    - RPT
    - LST
    - TAB
    - SCH
    - DIA
    - SPEC
    - PLN
    - PROC
    - MAN
    - API
    - CFG
    - JSON
    - YAML
    - FHA
    - PSSA
    - SSA
    - FTA
    - ANA
    - DAL
    - TRC
    - CAT
    - GLO
    - MAT
    - MIN
    - ACT
    - LOG
  
  statuses:
    - TEMPLATE
    - DRAFT
    - ACTIVE
    - APPROVED
    - RELEASED
    - SUPERSEDED
    - ARCHIVED
  
  extensions:
    - md
    - yml
    - yaml
    - json
    - csv
    - svg
    - png
    - jpg
    - jpeg
    - pdf
    - drawio

exemptions:
  files:
    - README.md
    - LICENSE
    - EXAMPLES.md
    - STRUCTURE_SUMMARY.md
    - .gitignore
    - .gitattributes
    - .gitkeep
    - .editorconfig
  
  directories:
    - .git
    - .github
    - node_modules
    - __pycache__
    - .pytest_cache
    - .venv
    - venv
    - dist
    - build
    - tools
  
  patterns:
    - "generate_*.py"
    - "validate_*.py"
    - "*_Agent_Config.(yaml|json|yml)"
```

---

## 9. Migration from v4.0

### 9.1 Breaking Changes

v5.0 introduces breaking changes requiring **full repository retrofit**:

1. **KNOT governance**: K01-K14 only (K15-K99 no longer allowed)
2. **STATUS field**: New mandatory field
3. **BLOCK field**: Replaces BUCKET concept
4. **AoR enforcement**: Mandatory, no STK_ prefix
5. **Config-driven**: All allowlists moved to YAML config

### 9.2 Migration Process

1. **Update standard** → Publish v5.0 docs and config
2. **Update tooling** → Validators, scaffolding, CI
3. **Generate rename map** → Automated mapping with confidence scoring
4. **Execute batch rename** → Controlled, incremental execution
5. **Update cross-references** → Links, indexes, manifests
6. **Verify compliance** → Validator + link checker
7. **Document results** → Retrofit report with statistics

### 9.3 Determining Field Values for Migration

**For existing v4.0 files:**

* **BLOCK:** Map from v4.0 BUCKET using conversion table (in config)
* **STATUS:** Default to `ACTIVE` for current files, `SUPERSEDED` for old versions
* **KNOT_TASK:** 
  * Files with K00 → manual review required
  * Files with K01-K14 → keep as-is
  * Files with K15+ → manual review + knot consolidation required

---

## 10. Automation

### 10.1 Validation Script

```bash
python validate_nomenclature.py <filename>
python validate_nomenclature.py --check-all
```

### 10.2 Scaffolding Script

```bash
python scripts/scaffold.py <ATA_ROOT> <PROJECT> <PROGRAM> <VARIANT> <BLOCK> <PHASE> <KNOT_TASK> <AOR> <SUBJECT> <TYPE> <VERSION> <STATUS>
```

Example:
```bash
python scripts/scaffold.py 27 AMPEL360 SPACET PLUS OPS LC03 K06 SE thermal-loop-overview STD v01 ACTIVE
```

### 10.3 CI/CD Integration

GitHub Actions workflow validates all committed files against v5.0 standard (PR-blocking).

### 10.4 Pre-commit Hook

```bash
cp scripts/pre-commit .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

---

## 11. References

* OPT-IN Framework v1.1
* ATA-SpaceT numbering system
* AMPEL360 Configuration Management Plan
* KNOTS Catalog v01
* Portal Stakeholder Index v01
* TEKNIA Credential Schema v1.0

---

## 12. Revision History

| Version | Date       | Changes                                                                           | Author |
|---------|------------|-----------------------------------------------------------------------------------|--------|
| v05     | 2025-12-17 | Breaking change: Strict KNOT governance (K01-K14), mandatory AoR, STATUS field, TEKNIA policy, config-driven allowlists | CM WG  |
| v04     | 2025-12-16 | Added TRIGGER_KNOT and AoR fields, reordered fields, double underscore           | CM WG  |
| v03     | 2025-12-15 | Added PROJECT and PROGRAM fields                                                  | CM WG  |
| v02     | 2025-12-14 | Introduced SUBJECT field (LC|SB)                                                  | CM WG  |
| v01     | 2025-12-13 | Initial normative standard                                                        | CM WG  |

---

**END OF NORMATIVE STANDARD v5.0**
