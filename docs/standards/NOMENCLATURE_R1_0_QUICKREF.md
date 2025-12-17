# Nomenclature R1.0 (v6.0) — Quick Reference

## Pattern (14 Fields)

```
[ATA_ROOT]_[PROJECT]_[PROGRAM]_[FAMILY]_[VARIANT]_[VERSION]_[BLOCK]_[PHASE]_[KNOT_TASK]_[AoR]__[SUBJECT]_[TYPE]_[ISSUE-REVISION]_[STATUS].[EXT]
```

## Field Constraints

| Field | Constraint | Example |
|-------|------------|---------|
| **ATA_ROOT** | 2-3 digits (00-116) | `00`, `27`, `115` |
| **PROJECT** | Fixed: `AMPEL360` | `AMPEL360` |
| **PROGRAM** | Fixed: `SPACET` | `SPACET` |
| **FAMILY** | Qx or Qxx pattern only | `Q10`, `Q100` |
| **VARIANT** | Allowlist: `PLUS`, `CERT`, `PROTO`, `SIM`, `TEST`, `GEN`, etc. | `PLUS`, `PROTO` |
| **VERSION** | `(BL\|TS\|GN)[0-9]{2}` | `BL01`, `TS02`, `GN03` |
| **BLOCK** | Allowlist: `OPS`, `STR`, `AI`, etc. | `OPS`, `AI` |
| **PHASE** | `LC01-LC14` or `SB01-SB99` | `LC03`, `SB90` |
| **KNOT_TASK** | `K01-K14` (opt. `-T###`) | `K06`, `K06-T001` |
| **AoR** | Allowlist: `CM`, `CERT`, `SE`, etc. | `CM`, `SE` |
| **__** | **Double underscore** | `__` |
| **SUBJECT** | lowercase-kebab-case | `thermal-loop`, `fha-report` |
| **TYPE** | Allowlist: `STD`, `RPT`, `FHA`, etc. | `STD`, `RPT` |
| **ISSUE-REVISION** | `I[0-9]{2}-R[0-9]{2}` | `I00-R00`, `I05-R03` |
| **STATUS** | Allowlist: `DRAFT`, `ACTIVE`, etc. | `ACTIVE`, `DRAFT` |
| **EXT** | Allowlist: `md`, `json`, `pdf`, etc. | `md`, `json` |

## Key Rules (R1.0)

### 1. **FAMILY Field (NEW)**
- Required field after PROGRAM
- Quantum-inspired, passenger-payload-numbered: Qx or Qxx pattern ONLY
- Examples: `Q10` (SPACE-T, 10 pax), `Q100` (AIR-T, 100 pax)
- **Restriction:** Only quantum families allowed; PROTO, SIM, TEST, GEN belong in VARIANT
- Extensions require CM approval

### 2. **VERSION Pattern (CHANGED)**
- **BL##**: Baseline versions (e.g., `BL01`, `BL02`)
- **TS##**: Testing versions (e.g., `TS01`, `TS02`)
- **GN##**: Generated versions (e.g., `GN01`, `GN02`)
- Pattern: `^(BL|TS|GN)[0-9]{2}$` (CI-enforced)

### 3. **ISSUE-REVISION Field (NEW)**
- Format: `I##-R##` (e.g., `I00-R00`, `I05-R03`)
- Pattern: `^I[0-9]{2}-R[0-9]{2}$` (CI-enforced)
- Use `I00-R00` for non-issue-specific artifacts

### 4. **KNOT Governance (STRICT)**
- **Only K01-K14 allowed** (K00, K15-K99 invalid)
- Optional task suffix: `-T001` to `-T999`
- New knots require CM approval + standard upgrade

### 5. **AoR Mandatory**
- Must match portal entry points exactly
- **No `STK_` prefix** (e.g., use `CM`, not `STK_CM`)

### 6. **Double Underscore**
- Use `__` before SUBJECT (e.g., `..._CM__thermal-loop_...`)

## Examples

### ✅ Valid R1.0

```
00_AMPEL360_SPACET_Q10_PLUS_BL01_GEN_LC01_K04_CM__nomenclature-standard_STD_I00-R00_ACTIVE.md
27_AMPEL360_SPACET_Q10_PLUS_BL01_OPS_LC03_K06-T001_SE__thermal-loop-overview_STD_I01-R01_ACTIVE.md
53_AMPEL360_SPACET_Q100_CERT_BL02_STR_LC07_K02_CERT__pressure-bulkhead-trade_RPT_I03-R02_DRAFT.pdf
95_AMPEL360_SPACET_Q10_PROTO_TS01_AI_SB04_K11_CM__model-card-template_STD_I00-R00_TEMPLATE.md
115_AMPEL360_SPACET_Q10_GEN_GN01_DATA_SB90_K05_DATA__supply-chain-schema_SCH_I02-R01_ACTIVE.json
```

### ❌ Invalid

```
# Missing FAMILY field (v5.0 format)
00_AMPEL360_SPACET_PLUS_GEN_LC01_K04_CM__nomenclature-standard_STD_v01_ACTIVE.md

# Wrong VERSION format (should be BL/TS/GN)
00_AMPEL360_SPACET_Q10_PLUS_v01_GEN_LC01_K04_CM__nomenclature-standard_STD_I00-R00_ACTIVE.md

# Missing ISSUE-REVISION field
00_AMPEL360_SPACET_Q10_PLUS_BL01_GEN_LC01_K04_CM__nomenclature-standard_STD_ACTIVE.md

# Invalid FAMILY (GEN/PROTO not allowed - use in VARIANT)
00_AMPEL360_SPACET_GEN_PLUS_BL01_GEN_LC01_K04_CM__nomenclature-standard_STD_I00-R00_ACTIVE.md

# Invalid KNOT (K99 not allowed)
27_AMPEL360_SPACET_Q10_PLUS_BL01_OPS_LC03_K99_SE__thermal-loop_STD_I00-R00_ACTIVE.md

# STK_ prefix not allowed
27_AMPEL360_SPACET_Q10_PLUS_BL01_OPS_LC03_K06_STK_SE__thermal-loop_STD_I00-R00_ACTIVE.md

# Single underscore (must be __)
27_AMPEL360_SPACET_Q10_PLUS_BL01_OPS_LC03_K06_SE_thermal-loop_STD_I00-R00_ACTIVE.md

# Wrong ISSUE-REVISION format
27_AMPEL360_SPACET_Q10_PLUS_BL01_OPS_LC03_K06_SE__thermal-loop_STD_I1-R1_ACTIVE.md
```

## Migration from v5.0

| v5.0 (12 fields) | R1.0 (14 fields) |
|------------------|------------------|
| No MODEL field | Add MODEL (default: `GEN`) |
| `vNN` | `BLNN` (assume baseline) |
| No ISSUE-REVISION | Add `I00-R00` (default) |

## Validation

```bash
# Validate single file
python validate_nomenclature.py --standard R1.0 <filename>

# Validate all files
python validate_nomenclature.py --standard R1.0 --check-all

# Modes
--mode warn    # Report violations, don't fail
--mode block   # Fail on violations (PR-blocking)
--mode report  # Generate detailed report
```

## Scaffolding

```bash
python scripts/scaffold.py <ATA_ROOT> <PROJECT> <PROGRAM> <MODEL> <VARIANT> <VERSION> <BLOCK> <PHASE> <KNOT_TASK> <AOR> <SUBJECT> <TYPE> <ISSUE-REVISION> <STATUS>
```

**Example:**
```bash
python scripts/scaffold.py 27 AMPEL360 SPACET Q10 PLUS BL01 OPS LC03 K06 SE thermal-loop-overview STD I01-R01 ACTIVE
```

## Allowlists (config-driven)

All allowlists are defined in `config/nomenclature/r1_0.yaml`:

- **FAMILY:** Q10 (SPACE-T, 10 pax), Q100 (AIR-T, 100 pax) - Qx/Qxx pattern only
- **VARIANT:** PLUS, CERT, GEN, PROTO, SIM, TEST, SYS, SW, HW
- **VARIANT:** PLUS, CERT, GEN, PROTO, SYS, SW, HW
- **BLOCK:** OPS, STR, PROP, AI, DATA, CERT, SAF, SW, HW, SYS, TEST, MRO, CIRC, ENRG, STOR, GEN
- **AoR:** CM, CERT, SAF, SE, OPS, DATA, AI, CY, TEST, MRO, SPACEPORT, PMO, QA, SEC, LEG, FIN, PROC
- **TYPE:** IDX, STD, PLAN, MIN, RPT, LOG, ACT, FHA, PSSA, SSA, FTA, ANA, REQ, DAL, TRC, CAT, LST, GLO, MAT, SCH, DIA, TAB, SPEC, PLN, PROC, MAN, API, CFG, JSON, YAML
- **STATUS:** TEMPLATE, DRAFT, ACTIVE, APPROVED, RELEASED, SUPERSEDED, ARCHIVED
- **EXT:** md, yml, yaml, json, csv, svg, png, jpg, jpeg, pdf, drawio

## Exemptions

Files/directories exempt from validation (see `config/nomenclature/r1_0.yaml`):

- **Files:** README.md, LICENSE, EXAMPLES.md, .gitignore, rename_map*.csv, etc.
- **Directories:** .git, .github, scripts, templates, docs, config, node_modules, __pycache__, etc.

## Change Control

**Authority:** Configuration Management Working Group (CM WG)

**Approval required for:**
- New MODEL, VARIANT, BLOCK, AoR, TYPE, STATUS values
- New KNOT IDs (requires standard upgrade)
- VERSION or ISSUE-REVISION pattern changes

**Process:**
1. Submit change request to CM WG
2. Review and approval
3. Update `config/nomenclature/r1_0.yaml`
4. Update tooling and documentation
5. Announce to stakeholders

## References

- **Full spec:** `docs/standards/NOMENCLATURE_R1_0.md`
- **Config:** `config/nomenclature/r1_0.yaml`
- **Validator:** `validate_nomenclature.py`
- **Scaffolder:** `scripts/scaffold.py`
- **CI workflow:** `.github/workflows/nomenclature-validation.yml`

---

**Version:** R1.0 (v6.0)  
**Date:** 2025-12-17  
**Owner:** CM WG
