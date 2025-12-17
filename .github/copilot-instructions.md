# GitHub Copilot Instructions for AMPEL360 Space-T

## File Naming Convention (MANDATORY)

**CRITICAL**: All files created or renamed in this repository MUST follow the Nomenclature Standard.

### Current Standards

This repository is transitioning from **v5.0 (12 fields)** to **R1.0/v6.0 (14 fields)** via PR^3 process.

**Active Standard:** v5.0 (PR-blocking in CI)  
**Upcoming Standard:** R1.0 (warn mode in CI, not yet enforced)

---

## v5.0 Pattern (Current - PR-Blocking)

```
[ATA_ROOT]_[PROJECT]_[PROGRAM]_[VARIANT]_[BLOCK]_[PHASE]_[KNOT_TASK]_[AoR]__[SUBJECT]_[TYPE]_[VERSION]_[STATUS].[EXT]
```

### Quick Reference (v5.0)

- **ATA_ROOT**: 2-3 digits (e.g., `00`, `27`, `115`)
- **PROJECT**: `AMPEL360` (hard constraint)
- **PROGRAM**: `SPACET` (fixed)
- **VARIANT**: `PLUS`, `CERT`, `GEN` (config-driven)
- **BLOCK**: `OPS`, `STR`, `AI`, etc. (config-driven)
- **PHASE**: `LC01-LC14` or `SB01-SB99`
- **KNOT_TASK**: `K01-K14` (opt. `-T###`) — **strict governance**
- **AoR**: `CM`, `CERT`, `SAF`, etc. (no `STK_` prefix!)
- **__**: Double underscore separator
- **SUBJECT**: lowercase-kebab-case
- **TYPE**: `STD`, `RPT`, `FHA`, etc.
- **VERSION**: `v01`, `v02`, etc.
- **STATUS**: `DRAFT`, `ACTIVE`, `APPROVED`, etc.
- **EXT**: `md`, `json`, `pdf`, etc.

---

## R1.0 (v6.0) Pattern (Upcoming - Warn Mode)

```
[ATA_ROOT]_[PROJECT]_[PROGRAM]_[MODEL]_[VARIANT]_[VERSION]_[BLOCK]_[PHASE]_[KNOT_TASK]_[AoR]__[SUBJECT]_[TYPE]_[ISSUE-REVISION]_[STATUS].[EXT]
```

### Key Changes in R1.0

1. **MODEL field added** (NEW)
   - Quantum-inspired, passenger-payload-numbered
   - `Q10`: SPACE-T (10 passengers, current dev)
   - `Q100`: AIR-T (100 passengers)
   - Also: `PROTO`, `SIM`, `TEST`, `GEN`

2. **VERSION field changed** (BREAKING)
   - Was: `vNN` (e.g., `v01`, `v02`)
   - Now: `(BL|TS|GN)NN`
   - `BL01`, `BL02`: Baseline versions
   - `TS01`, `TS02`: Testing versions
   - `GN01`, `GN02`: Generated versions

3. **ISSUE-REVISION field added** (NEW)
   - Format: `I##-R##`
   - Examples: `I00-R00`, `I01-R01`, `I05-R03`
   - Use `I00-R00` for non-issue artifacts

### Quick Reference (R1.0)

All v5.0 rules apply, plus:
- **MODEL**: `Q10`, `Q100`, `PROTO`, `SIM`, `TEST`, `GEN`
- **VERSION**: `BL##`, `TS##`, or `GN##` (not `v##`)
- **ISSUE-REVISION**: `I##-R##` (e.g., `I00-R00`)

---

## Critical Rules (Both Standards)

1. **KNOT GOVERNANCE (Breaking Change!)**
   - **Only K01 through K14 are allowed**
   - K15-K99 are **NOT valid** in v5.0
   - Optional task suffix: `-T001` through `-T999`
   - New knots require **CM approval** and **standard upgrade**
   - Example: `K06`, `K06-T001` ✅ | `K00`, `K99` ❌

2. **AoR is MANDATORY**
   - Must match portal entry points exactly
   - **No `STK_` prefix** in filenames
   - Valid: `CM`, `CERT`, `SAF`, `SE` ✅
   - Invalid: `STK_CM`, `STK_CERT` ❌

3. **Double Underscore**
   - Use `__` (double underscore) before SUBJECT
   - Valid: `..._CM__thermal-loop_...` ✅
   - Invalid: `..._CM_thermal-loop_...` ❌

4. **STATUS Field**
   - New mandatory field in v5.0
   - Allowlist: `TEMPLATE`, `DRAFT`, `ACTIVE`, `APPROVED`, `RELEASED`, `SUPERSEDED`, `ARCHIVED`

5. **Config-Driven**
   - All allowlists defined in `config/nomenclature/v5_0.yaml`
   - Changes require CM approval

### Examples

✅ Valid v5.0:
```
27_AMPEL360_SPACET_PLUS_OPS_LC03_K06-T001_SE__thermal-loop-overview_STD_v01_ACTIVE.md
53_AMPEL360_SPACET_PLUS_STR_LC07_K02_CERT__pressure-bulkhead-trade_RPT_v02_DRAFT.pdf
95_AMPEL360_SPACET_PLUS_AI_SB04_K11_CM__model-card-template_STD_v01_TEMPLATE.md
00_AMPEL360_SPACET_PLUS_CERT_LC10_K01_CERT__certification-authority-basis_PLAN_v01_ACTIVE.md
```

✅ Valid R1.0:
```
00_AMPEL360_SPACET_Q10_PLUS_BL01_GEN_LC01_K04_CM__nomenclature-standard_STD_I00-R00_ACTIVE.md
27_AMPEL360_SPACET_Q10_PLUS_BL01_OPS_LC03_K06-T001_SE__thermal-loop-overview_STD_I01-R01_ACTIVE.md
53_AMPEL360_SPACET_Q100_CERT_BL02_STR_LC07_K02_CERT__pressure-bulkhead-trade_RPT_I03-R02_DRAFT.pdf
95_AMPEL360_SPACET_GEN_PLUS_TS01_AI_SB04_K11_CM__model-card-template_STD_I00-R00_TEMPLATE.md
```

❌ Invalid (v5.0):
```
# Missing STATUS field
27_AMPEL360_SPACET_PLUS_OPS_LC03_K06_SE__thermal-loop_STD_v01.md

# Invalid KNOT (K99 not allowed)
27_AMPEL360_SPACET_PLUS_OPS_LC03_K99_SE__thermal-loop_STD_v01_ACTIVE.md

# STK_ prefix not allowed
27_AMPEL360_SPACET_PLUS_OPS_LC03_K06_STK_SE__thermal-loop_STD_v01_ACTIVE.md

# Single underscore (must be __)
27_AMPEL360_SPACET_PLUS_OPS_LC03_K06_SE_thermal-loop_STD_v01_ACTIVE.md
```

❌ Invalid (R1.0):
```
# Missing MODEL field (v5.0 format, not R1.0)
00_AMPEL360_SPACET_PLUS_GEN_LC01_K04_CM__nomenclature-standard_STD_v01_ACTIVE.md

# Wrong VERSION format (should be BL/TS/GN)
00_AMPEL360_SPACET_Q10_PLUS_v01_GEN_LC01_K04_CM__nomenclature-standard_STD_I00-R00_ACTIVE.md

# Missing ISSUE-REVISION field
00_AMPEL360_SPACET_Q10_PLUS_BL01_GEN_LC01_K04_CM__nomenclature-standard_STD_ACTIVE.md
```

# STK_ prefix not allowed
27_AMPEL360_SPACET_PLUS_OPS_LC03_K06_STK_SE__thermal-loop_STD_v01_ACTIVE.md

# Single underscore (must be __)
27_AMPEL360_SPACET_PLUS_OPS_LC03_K06_SE_thermal-loop_STD_v01_ACTIVE.md
```

### Excluded Files

These files are exempt from the nomenclature standard:
- `README.md`, `LICENSE`, `EXAMPLES.md`, `STRUCTURE_SUMMARY.md`
- `.gitignore`, `.gitattributes`
- Files in `.git/`, `.github/`, `node_modules/`, `__pycache__/`, etc.

### Validation

Always validate your files before committing:
```bash
# v5.0 validation (current standard)
python validate_nomenclature.py --standard v5.0 <filename>
python validate_nomenclature.py --standard v5.0 --check-all

# R1.0 validation (upcoming standard - informational)
python validate_nomenclature.py --standard R1.0 <filename>
python validate_nomenclature.py --standard R1.0 --check-all --mode warn
```

### Scaffolding

**v5.0 (current):**
```bash
python scripts/scaffold.py <ATA_ROOT> <PROJECT> <PROGRAM> <VARIANT> <BLOCK> <PHASE> <KNOT_TASK> <AOR> <SUBJECT> <TYPE> <VERSION> <STATUS>
```

Example:
```bash
python scripts/scaffold.py 27 AMPEL360 SPACET PLUS OPS LC03 K06 SE thermal-loop STD v01 ACTIVE
```

**R1.0 (upcoming - not yet in scaffold.py):**
```bash
# Will be: python scripts/scaffold.py <ATA_ROOT> <PROJECT> <PROGRAM> <MODEL> <VARIANT> <VERSION> <BLOCK> <PHASE> <KNOT_TASK> <AOR> <SUBJECT> <TYPE> <ISSUE-REVISION> <STATUS>
```

Example (future):
```bash
# python scripts/scaffold.py 27 AMPEL360 SPACET Q10 PLUS BL01 OPS LC03 K06 SE thermal-loop STD I00-R00 ACTIVE
```

### Documentation

**v5.0 (current):**
- **Full standard**: `docs/standards/NOMENCLATURE_v5_0.md`
- **Quick reference**: `docs/standards/NOMENCLATURE_v5_0_QUICKREF.md`
- **Config file**: `config/nomenclature/v5_0.yaml`

**R1.0 (upcoming):**
- **Full standard**: `docs/standards/NOMENCLATURE_R1_0.md`
- **Quick reference**: `docs/standards/NOMENCLATURE_R1_0_QUICKREF.md`
- **Config file**: `config/nomenclature/r1_0.yaml`

---

## PR^3 Transition Process

The repository is undergoing a phased transition to R1.0:

- **PR^3-1 (PRE-RELEASE)**: Spec + tooling + warn mode (current phase)
- **PR^3-2 (RETROFIT)**: Mass rename + cross-ref rewrite + block mode
- **PR^3-3 (PREDICTED RELEASE)**: Freeze + final verification

**Current status**: PR^3-1 in progress  
**Action required**: Use v5.0 for new files; R1.0 validation is informational only

---

## Template Usage (MANDATORY)

When creating a new file of a specific `TYPE`, you MUST use the appropriate template:

1. **Look up** the template in `templates/[TYPE].md`
2. **Read** the template content
3. **Use the scaffold script** to generate properly named files
4. **Fill** the placeholders (`{{...}}`) with context from the user's prompt

### Scaffolding Workflow

**Always use the scaffold script:**
```bash
python scripts/scaffold.py <ATA_ROOT> <PROJECT> <PROGRAM> <VARIANT> <BLOCK> <PHASE> <KNOT_TASK> <AOR> <SUBJECT> <TYPE> <VERSION> <STATUS>
```

This ensures:
- Correct v5.0 nomenclature
- Proper template usage
- All required fields present
- Validation passes

### Available Templates

| TYPE | Template | Purpose |
|------|----------|---------|
| `PLAN` | `templates/PLAN.md` | Project plans, safety plans, management plans |
| `MIN` | `templates/MIN.md` | Meeting minutes |
| `RPT` | `templates/RPT.md` | Reports and assessments |
| `LOG` | `templates/LOG.md` | Issue logs, event logs, hazard logs |
| `ACT` | `templates/ACT.md` | Action item registers |
| `IDX` | `templates/IDX.md` | Indexes and catalogs |
| `FHA` | `templates/FHA.md` | Functional Hazard Assessments |
| `PSSA` | `templates/PSSA.md` | Preliminary System Safety Assessments |
| `SSA` | `templates/SSA.md` | System Safety Assessments |
| `FTA` | `templates/FTA.md` | Fault Tree Analysis |
| `ANA` | `templates/ANA.md` | Engineering analysis and trade studies |
| `REQ` | `templates/REQ.md` | Requirements specifications |
| `DAL` | `templates/DAL.md` | Development Assurance Level assignments |
| `TRC` | `templates/TRC.md` | Traceability matrices |
| `CAT` | `templates/CAT.md` | Catalogs |
| `LST` | `templates/LST.md` | Lists and inventories |
| `GLO` | `templates/GLO.md` | Glossaries and terminology |
| `MAT` | `templates/MAT.md` | Material specifications |
| `SCH` | `templates/SCH.md` | Data schemas (JSON, XML) |
| `DIA` | `templates/DIA.md` | Diagrams and flowcharts |
| `TAB` | `templates/TAB.md` | Data tables |
| `STD` | `templates/STD.md` | Standards and specifications |

### Template Placeholders

**v5.0 Placeholders:**
- `{{ATA_ROOT}}` - ATA chapter code
- `{{PROJECT}}` - Project identifier (AMPEL360)
- `{{PROGRAM}}` - Program identifier (SPACET)
- `{{VARIANT}}` - Configuration variant
- `{{BLOCK}}` - Domain classification
- `{{PHASE}}` - Lifecycle or subbucket phase
- `{{KNOT_TASK}}` - Knot and optional task
- `{{AOR}}` - Area of responsibility
- `{{SUBJECT}}` - Human-readable subject
- `{{TYPE}}` - Artifact type
- `{{VERSION}}` - Version number
- `{{STATUS}}` - Document status
- `{{TITLE}}` - Replace with human-readable title
- `{{OWNER}}` - Replace with responsible owner/team
- `{{DATE}}` - Current date

**Backward compatibility placeholders (deprecated):**
- `{{BUCKET}}` - Maps to BLOCK
- `{{LCSB}}` - Maps to PHASE
- `{{DESCRIPTION}}` - Maps to SUBJECT

### New TYPE Detection

If you encounter a need for a new TYPE code not in the approved list:

1. **Check existing TYPEs first**: Ensure no approved TYPE fits the use case
2. **Use temporary generic TYPE**: Use the closest existing TYPE temporarily
3. **Run detection tool**:
   ```bash
   python scripts/detect_new_types.py --auto-suggest
   ```
4. **Follow extension process**: See generated `NOMENCLATURE_EXTENSION_GUIDE.md`
5. **Notify team**: New TYPEs require Configuration Management WG approval

**Automated Detection**: GitHub Actions automatically detects new TYPEs and creates issues

---

## Project Context

This is the AMPEL360 Space-T project implementing:
- OPT-IN Framework v1.1 (5 axes: O, P, T, I, N)
- ATA-SpaceT numbering system
- 14-folder lifecycle structure
- Cross-ATA root buckets

## Code Style

- Follow existing code patterns in the repository
- Use clear, descriptive variable names
- Add comments only when necessary for complex logic
- Maintain consistency with existing documentation style
