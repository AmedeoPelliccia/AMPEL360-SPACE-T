# Nomenclature v5.0 Quick Reference

## Canonical Format

```
[ATA_ROOT]_[PROJECT]_[PROGRAM]_[VARIANT]_[BLOCK]_[PHASE]_[KNOT_TASK]_[AoR]__[SUBJECT]_[TYPE]_[VERSION]_[STATUS].[EXT]
```

## Field Quick Guide

| Field | Format | Example | Notes |
|-------|--------|---------|-------|
| **ATA_ROOT** | 2-3 digits | `00`, `27`, `115` | 2 digits for <100, 3 for ≥100 |
| **PROJECT** | Fixed | `AMPEL360` | Hard constraint |
| **PROGRAM** | Fixed | `SPACET` | Fixed for this repo |
| **VARIANT** | Allowlist | `PLUS`, `CERT` | Config-driven |
| **BLOCK** | Allowlist | `OPS`, `STR`, `AI` | Config-driven |
| **PHASE** | LC or SB | `LC03`, `SB04` | LC01-LC14 or SB01-SB99 |
| **KNOT_TASK** | K01-K14 | `K06`, `K06-T001` | **Only K01-K14!** Optional -T### |
| **AoR** | Allowlist | `CM`, `CERT`, `SAF` | **No STK_ prefix!** |
| **__** | Separator | `__` | **Double underscore required!** |
| **SUBJECT** | kebab-case | `thermal-loop` | Lowercase, hyphens only |
| **TYPE** | Allowlist | `STD`, `RPT`, `FHA` | Config-driven |
| **VERSION** | vNN | `v01`, `v02` | Exactly 2 digits |
| **STATUS** | Allowlist | `ACTIVE`, `DRAFT` | New in v5.0! |
| **EXT** | Allowlist | `md`, `json`, `pdf` | Config-driven |

## Critical Rules

### 🔴 KNOT Governance (Breaking Change!)

* **Only K01 through K14 are allowed**
* K15-K99 are **NOT valid** in v5.0
* Optional task suffix: `-T001` through `-T999`
* New knots require **CM approval** and **standard upgrade**

### 🔴 AoR is Mandatory

* Must match portal entry points exactly
* **No `STK_` prefix** in filenames
* Valid: `CM`, `CERT`, `SAF`, `SE`, etc.
* Invalid: `STK_CM`, `STK_CERT`

### 🔴 Double Underscore

* Use `__` (double underscore) before SUBJECT
* Valid: `..._CM__thermal-loop_...`
* Invalid: `..._CM_thermal-loop_...`

### 🔴 STATUS Field

* New mandatory field in v5.0
* Allowlist: `TEMPLATE`, `DRAFT`, `ACTIVE`, `APPROVED`, `RELEASED`, `SUPERSEDED`, `ARCHIVED`

## Examples

### ✅ Valid v5.0 Files

```
27_AMPEL360_SPACET_PLUS_OPS_LC03_K06-T001_SE__thermal-loop-overview_STD_v01_ACTIVE.md
53_AMPEL360_SPACET_PLUS_STR_LC07_K02_CERT__pressure-bulkhead-trade_RPT_v02_DRAFT.pdf
95_AMPEL360_SPACET_PLUS_AI_SB04_K11_CM__model-card-template_STD_v01_TEMPLATE.md
00_AMPEL360_SPACET_PLUS_CERT_LC10_K01_CERT__certification-authority-basis_PLAN_v01_ACTIVE.md
```

### ❌ Invalid Examples

```
27_AMPEL360_SPACET_PLUS_OPS_LC03_K99_SE__thermal-loop_STD_v01_ACTIVE.md
❌ K99 not allowed (only K01-K14)

27_AMPEL360_SPACET_PLUS_OPS_LC03_K06_STK_SE__thermal-loop_STD_v01_ACTIVE.md
❌ No STK_ prefix allowed in AoR

27_AMPEL360_SPACET_PLUS_OPS_LC03_K06_SE_thermal-loop_STD_v01_ACTIVE.md
❌ Must use __ (double underscore) not single _

27_AMPEL360_SPACET_PLUS_OPS_LC03_K06_SE__thermal-loop_STD_v01.md
❌ Missing STATUS field
```

## Allowlists (Config-Driven)

All allowlists are defined in `config/nomenclature/v5_0.yaml`

### VARIANT Allowlist (Initial)
`PLUS` (default)

### AoR Allowlist (Initial)
`CM`, `CERT`, `SAF`, `SE`, `OPS`, `DATA`, `AI`, `CY`, `TEST`, `MRO`, `SPACEPORT`, `PMO`, `QA`, `SEC`, `LEG`, `FIN`, `PROC`

### TYPE Allowlist (Baseline)
`IDX`, `STD`, `REQ`, `RPT`, `LST`, `TAB`, `SCH`, `DIA`, `SPEC`, `PLN`, `PROC`, `MAN`, `API`, `CFG`, `JSON`, `YAML`, `FHA`, `PSSA`, `SSA`, `FTA`, `ANA`, `DAL`, `TRC`, `CAT`, `GLO`, `MAT`, `MIN`, `ACT`, `LOG`

### STATUS Allowlist
`TEMPLATE`, `DRAFT`, `ACTIVE`, `APPROVED`, `RELEASED`, `SUPERSEDED`, `ARCHIVED`

### EXT Allowlist (GitHub-First)
`md`, `yml`, `yaml`, `json`, `csv`, `svg`, `png`, `jpg`, `jpeg`, `pdf`, `drawio`

## TEKNIA Credentials

TEKNIA credentials are **separate artifacts** with specific governance:

* **Credential TYPEs:** `BADGE`, `CERT`, `LIC`
* **Issuance AoR:** Only `CM` or `CERT` can issue
* **Schema:** Must follow `config/teknia/credential_schema_v1.yaml`
* **Binding:** Credentials bind to subject NKUs via path, SHA-256, and commit

## Validation

```bash
# Validate single file
python validate_nomenclature.py <filename>

# Validate all files
python validate_nomenclature.py --check-all

# Scaffold new file
python scripts/scaffold.py <ATA_ROOT> <PROJECT> <PROGRAM> <VARIANT> <BLOCK> <PHASE> <KNOT_TASK> <AOR> <SUBJECT> <TYPE> <VERSION> <STATUS>
```

## Migration from v4.0

Key changes:
1. **KNOT restriction:** K01-K14 only (no K15+)
2. **STATUS field:** New mandatory field
3. **BLOCK field:** Replaces BUCKET concept
4. **AoR mandatory:** No STK_ prefix
5. **Config-driven:** All allowlists in YAML

## Exemptions

**Exempt files:**
* `README.md`, `LICENSE`, `.gitignore`, etc.
* Files in `.git/`, `.github/`, `node_modules/`, etc.
* Generator/validation scripts (`generate_*.py`, `validate_*.py`)

## Extension Process

To add new values to allowlists:
1. Propose change to Configuration Management WG
2. Update `config/nomenclature/v5_0.yaml`
3. Update tooling (validators, scaffolding)
4. Document in change control record

**For new KNOT IDs (K15+):**
* Requires **Nomenclature Standard upgrade** (new version)
* Cannot be added via config alone
* Requires formal CM approval

## Full Documentation

See `docs/standards/NOMENCLATURE_v5_0.md` for complete normative standard.
