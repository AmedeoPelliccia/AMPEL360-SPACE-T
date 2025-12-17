# GitHub Copilot Instructions for AMPEL360 Space-T

## File Naming Convention (MANDATORY)

**CRITICAL**: All files created or renamed in this repository MUST follow the Nomenclature Standard v6.0 (R1.0 FINAL LOCK).

### Required Pattern (v6.0 R1.0)

```
[ATA_ROOT]_[PROJECT]_[PROGRAM]_[FAMILY]_[VARIANT]_[VERSION]_[MODEL]_[BLOCK]_[PHASE]_[KNOT_TASK]_[AoR]__[SUBJECT]_[TYPE]_[ISSUE-REVISION]_[STATUS].[EXT]
```

### Quick Reference

- **ATA_ROOT**: 2-3 digits (e.g., `00`, `27`, `115`) - 2 digits for <100, 3 for ≥100
- **PROJECT**: `AMPEL360` (hard constraint)
- **PROGRAM**: `SPACET` (fixed)
- **FAMILY**: `Q10`, `Q100` (quantum-inspired pax payload, allowlist)
- **VARIANT**: `GEN`, `BASELINE`, `FLIGHTTEST`, `CERT`, `MSN`, `HOV`, `CUST` (governance lane, allowlist)
- **VERSION**: `PLUS`, `PLUS01`, `PLUSULTRA`, `PLUSULTRA02` (branding + optional 2-digit iteration)
- **MODEL**: `BB`, `HW`, `SW`, `PR` (artifact domain, allowlist)
- **BLOCK**: `OPS`, `STR`, `AI`, etc. (config-driven allowlist)
- **PHASE**: `LC01-LC14` (lifecycle) or `SB01-SB99` (subbucket)
- **KNOT_TASK**: `K01-K14` optionally with `-T001` to `-T999` (**strict governance**)
- **AoR**: `CM`, `CERT`, `SAF`, etc. (**no STK_ prefix!**)
- **__**: **Double underscore separator required!**
- **SUBJECT**: lowercase-kebab-case (e.g., `thermal-loop`, `propulsion`)
- **TYPE**: `STD`, `RPT`, `FHA`, etc. (config-driven allowlist)
- **ISSUE-REVISION**: `I##-R##` (e.g., `I01-R01`, `I12-R03`)
- **STATUS**: `DRAFT`, `ACTIVE`, `APPROVED`, etc. (config-driven allowlist)
- **EXT**: lowercase (e.g., `md`, `json`, `pdf`)

### Critical Rules (v6.0 R1.0 FINAL LOCK)

1. **KNOT GOVERNANCE**
   - **Only K01 through K14 are allowed**
   - K15-K99 are **NOT valid** in v6.0
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

4. **VERSION Iteration (R1.0 FINAL LOCK)**
   - Brand root: `PLUS` or `PLUSULTRA`
   - Optional 2-digit iteration: `01` to `99`
   - Pattern: `^(PLUS|PLUSULTRA)([0-9]{2})?$`
   - Examples: `PLUS`, `PLUS01`, `PLUSULTRA02` ✅
   - Invalid: `PLUS1`, `PLUSULTRA001` ❌

5. **Conditional SUBJECT Prefixes (R1.0 FINAL LOCK)**
   - **VARIANT=CUST** requires `SUBJECT` to start with `cust-<custcode>-`
     - custcode: 2-12 alphanumeric characters
     - Example: `cust-airbus-thermal-loop` ✅
   - **VARIANT=MSN** requires `SUBJECT` to start with `msn-<serial>-`
     - serial: 3-6 digits
     - Example: `msn-000123-thermal-loop` ✅

6. **Length Limits (R1.0 FINAL LOCK)**
   - Filename: ≤180 characters
   - BLOCK: ≤12 chars
   - SUBJECT: ≤60 chars
   - TYPE: ≤8 chars
   - AoR: ≤10 chars

7. **ISSUE-REVISION Format**
   - Pattern: `I##-R##` with zero-padding
   - Examples: `I01-R01`, `I12-R03` ✅
   - Invalid: `I1-R1`, `I001-R01` ❌

8. **Config-Driven**
   - All allowlists defined in `config/nomenclature/v6_0.yaml`
   - Changes require CM approval

### Examples

✅ Valid v6.0 R1.0:
```
27_AMPEL360_SPACET_Q10_GEN_PLUS_BB_OPS_LC03_K06-T001_SE__thermal-loop-overview_STD_I01-R01_ACTIVE.md
27_AMPEL360_SPACET_Q10_GEN_PLUS01_BB_OPS_LC03_K06_SE__thermal-loop_STD_I01-R01_ACTIVE.md
27_AMPEL360_SPACET_Q10_CUST_PLUS_SW_OPS_LC03_K06_SE__cust-airbus-thermal_STD_I01-R01_DRAFT.md
27_AMPEL360_SPACET_Q100_MSN_PLUSULTRA02_HW_OPS_LC03_K06_SE__msn-000123-thermal_STD_I01-R01_ACTIVE.md
95_AMPEL360_SPACET_Q10_BASELINE_PLUS_SW_AI_SB04_K11_CM__model-card-template_STD_I01-R01_TEMPLATE.md
00_AMPEL360_SPACET_Q10_CERT_PLUS_PR_CERT_LC10_K01_CERT__certification-authority-basis_PLAN_I01-R01_ACTIVE.md
```

❌ Invalid:
```
# Missing new v6.0 tokens (FAMILY, VERSION redefined, MODEL, ISSUE-REVISION)
27_AMPEL360_SPACET_Q10_GEN_PLUS_BB_OPS_LC03_K06_SE__thermal-loop_STD_I01-R01_ACTIVE.md

# Invalid KNOT (K99 not allowed)
27_AMPEL360_SPACET_Q10_GEN_PLUS_BB_OPS_LC03_K99_SE__thermal-loop_STD_I01-R01_ACTIVE.md

# STK_ prefix not allowed
27_AMPEL360_SPACET_Q10_GEN_PLUS_BB_OPS_LC03_K06_STK_SE__thermal-loop_STD_I01-R01_ACTIVE.md

# Single underscore (must be __)
27_AMPEL360_SPACET_Q10_GEN_PLUS_BB_OPS_LC03_K06_SE_thermal-loop_STD_I01-R01_ACTIVE.md

# CUST variant without required prefix
27_AMPEL360_SPACET_Q10_CUST_PLUS_SW_OPS_LC03_K06_SE__thermal-loop_STD_I01-R01_DRAFT.md

# Invalid VERSION iteration (must be 2 digits)
27_AMPEL360_SPACET_Q10_GEN_PLUS1_BB_OPS_LC03_K06_SE__thermal-loop_STD_I01-R01_ACTIVE.md

# Invalid ISSUE-REVISION (must be zero-padded)
27_AMPEL360_SPACET_Q10_GEN_PLUS_BB_OPS_LC03_K06_SE__thermal-loop_STD_I1-R1_ACTIVE.md
```

### Excluded Files

These files are exempt from the nomenclature standard:
- `README.md`, `LICENSE`, `EXAMPLES.md`, `STRUCTURE_SUMMARY.md`
- `.gitignore`, `.gitattributes`
- Files in `.git/`, `.github/`, `node_modules/`, `__pycache__/`, etc.

### Validation

Always validate your files before committing:
```bash
python validate_nomenclature.py --standard v6.0 <filename>
python validate_nomenclature.py --standard v6.0 --check-all
```

### Scaffolding

Create new files with proper v6.0 nomenclature:
```bash
python scripts/scaffold_v6.py --standard v6.0 <ATA_ROOT> <PROJECT> <PROGRAM> <FAMILY> <VARIANT> <VERSION> <MODEL> <BLOCK> <PHASE> <KNOT_TASK> <AOR> <SUBJECT> <TYPE> <ISSUE-REVISION> <STATUS>
```

Example:
```bash
python scripts/scaffold_v6.py --standard v6.0 27 AMPEL360 SPACET Q10 GEN PLUS BB OPS LC03 K06 SE thermal-loop STD I01-R01 ACTIVE
```

### Documentation

- **Full standard**: `docs/standards/NOMENCLATURE_v6_0_R1_0.md`
- **Quick reference**: `docs/standards/NOMENCLATURE_v6_0_R1_0_QUICKREF.md`
- **Config file**: `config/nomenclature/v6_0.yaml`

---

## Template Usage (MANDATORY)
```bash
python scripts/scaffold.py <ATA_ROOT> <PROJECT> <PROGRAM> <VARIANT> <BLOCK> <PHASE> <KNOT_TASK> <AOR> <SUBJECT> <TYPE> <VERSION> <STATUS>
```

Example:
```bash
python scripts/scaffold.py 27 AMPEL360 SPACET PLUS OPS LC03 K06 SE thermal-loop STD v01 ACTIVE
```

### Documentation

- **Full standard**: `docs/standards/NOMENCLATURE_v5_0.md`
- **Quick reference**: `docs/standards/NOMENCLATURE_v5_0_QUICKREF.md`
- **Config file**: `config/nomenclature/v5_0.yaml`

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
