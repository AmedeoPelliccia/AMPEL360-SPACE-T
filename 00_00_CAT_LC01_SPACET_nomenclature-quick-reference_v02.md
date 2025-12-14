# Nomenclature Standard Quick Reference

## Pattern

```
[ROOT]_[BUCKET]_[TYPE]_[VARIANT]_[DESCRIPTION]_[VERSION].[EXT]
```

## Field Rules

| Field | Format | Examples |
|-------|--------|----------|
| ROOT | 2 digits | `00`, `24`, `72` |
| BUCKET | 2 digits | `00`, `10`, `20`, `30`, `40`, `50`, `60`, `70`, `80`, `90` |
| TYPE | 2-8 uppercase | `PLAN`, `FHA`, `REQ`, `STD`, `IDX` |
| VARIANT | Uppercase + hyphens | `SPACET`, `DRAFT`, `SYS`, `LC02-SPACET` |
| DESCRIPTION | lowercase-kebab-case | `safety-program`, `propulsion`, `hazard-log` |
| VERSION | v + 2 digits | `v01`, `v02`, `v10` |
| EXT | lowercase | `md`, `json`, `xlsx`, `pdf` |

## Special Rules

### ⚠️ CRITICAL: BUCKET=00 requires LC prefix

If `BUCKET=00`, then `VARIANT` **MUST** start with `LC01` through `LC14`

✅ `00_00_PLAN_LC02-SPACET_safety-program_v01.md`  
❌ `00_00_PLAN_SPACET_safety-program_v01.md`

### Delimiters

- Use `_` **only** between fields
- Use `-` **only** inside VARIANT and DESCRIPTION

## BUCKET Values

| Code | Domain |
|------|--------|
| `00` | Lifecycle (requires LC prefix in VARIANT) |
| `10` | Operations |
| `20` | Primary Subsystem |
| `30` | Circularity |
| `40` | Software |
| `50` | Structures |
| `60` | Storages |
| `70` | Propulsion |
| `80` | Energy |
| `90` | Tables/Schemas/Diagrams/Reference |

## Approved TYPE Codes

### Planning / Control
`PLAN`, `MIN`, `RPT`, `LOG`, `ACT`, `IDX`

### Safety Analyses
`FHA`, `PSSA`, `SSA`, `FTA`, `ANA`

### Requirements / Allocation
`REQ`, `DAL`, `TRC`

### Data / Reference
`CAT`, `LST`, `GLO`, `MAT`, `SCH`, `DIA`, `TAB`, `STD`

## Validation

```bash
# Single file
python validate_nomenclature.py <filename>

# All files
python validate_nomenclature.py --check-all
```

## Examples

### ✅ Valid

```
00_00_PLAN_LC02-SPACET_safety-program_v01.md
00_70_FHA_SYS_propulsion_v01.md
00_40_REQ_SW_software-safety-reqs_v01.md
00_20_TRC_SPACET_traceability-matrix_v01.xlsx
00_90_SCH_GEN_hazard-log-schema_v01.json
24_40_REQ_SW-01_electrical-power-software_v01.md
```

### ❌ Invalid

```
00_00_PLAN_SPACET_safety-program_v01.md       # Missing LC prefix
00-70-FHA-SYS-propulsion-v01.md              # Wrong delimiter
00_70_FHA_SYS_propulsion_v1.md               # VERSION must be vNN
00_99_LST_GEN_glossary_v01.md                # Invalid BUCKET
00_70_FHA_SYS_PropulsionFHA_v01.md           # Uppercase in DESCRIPTION
00_70_fha_SYS_propulsion_v01.md              # Lowercase TYPE
```

## Common Mistakes

1. **Missing LC prefix for BUCKET=00**
   - Fix: Add `LC01` through `LC14` to start of VARIANT
   - Example: `SPACET` → `LC02-SPACET`

2. **Wrong delimiters**
   - Fix: Use `_` between fields, `-` inside fields only
   - Example: `00-70-FHA` → `00_70_FHA`

3. **Wrong version format**
   - Fix: Always use 2 digits after `v`
   - Example: `v1` → `v01`

4. **Uppercase in DESCRIPTION**
   - Fix: Use lowercase-kebab-case only
   - Example: `SafetyProgram` → `safety-program`

5. **Lowercase TYPE**
   - Fix: Use uppercase only
   - Example: `fha` → `FHA`

## Reference Documents

- **Full Standard**: `00_00_STD_LC01-SPACET_nomenclature-standard_v01.md`
- **Automation Guide**: `00_00_IDX_LC01-SPACET_nomenclature-automation-guide_v01.md`
- **Agent Instructions**: `.github/NOMENCLATURE_AGENT_INSTRUCTIONS.md`

---

**Last Updated**: 2025-12-14  
**Version**: 1.0
