# Nomenclature Standard Quick Reference

## Pattern (v2.0 - 8 Fields)

```
[ROOT]_[BUCKET]_[TYPE]_[LC_OR_SUBBUCKET]_[VARIANT]_[DESCRIPTION]_[VERSION].[EXT]
```

## Field Rules

| Field | Format | Examples |
|-------|--------|----------|
| ROOT | 2-3 digits | `00`, `24`, `72`, `115`, `116` |
| BUCKET | 2 digits | `00`, `10`, `20`, `30`, `40`, `50`, `60`, `70`, `80`, `90` |
| TYPE | 2-8 uppercase | `PLAN`, `FHA`, `REQ`, `STD`, `IDX` |
| LC_OR_SUBBUCKET | LC01-LC14 or SB15-SB99 | `LC01`, `LC14`, `SB15`, `SB99` |
| VARIANT | Uppercase + hyphens | `SPACET`, `DRAFT`, `SYS`, `HW-01` |
| DESCRIPTION | lowercase-kebab-case | `safety-program`, `propulsion`, `hazard-log` |
| VERSION | v + 2 digits | `v01`, `v02`, `v10` |
| EXT | lowercase | `md`, `json`, `xlsx`, `pdf` |

## Special Rules

### ⚠️ CRITICAL: Subject Category Rules

**If `BUCKET=00`** → Use **LC** (Lifecycle) category:
- `LC_OR_SUBBUCKET` **MUST** be `LC01` through `LC14`
- Example: ✅ `00_00_PLAN_LC02_SPACET_safety-program_v01.md`
- Invalid: ❌ `00_00_PLAN_SB15_SPACET_safety-program_v01.md`

**If `BUCKET≠00`** → Use **SB** (Sub-bucket) category:
- `LC_OR_SUBBUCKET` **MUST** be `SB15` through `SB99`
- Example: ✅ `00_70_FHA_SB15_SYS_propulsion_v01.md`
- Invalid: ❌ `00_70_FHA_SB00_SYS_propulsion_v01.md`
- Invalid: ❌ `00_70_FHA_LC01_SYS_propulsion_v01.md`

### Delimiters

- Use `_` **only** between fields
- Use `-` **only** inside VARIANT and DESCRIPTION

## BUCKET Values

| Code | Domain | Allowed Subbuckets |
|------|--------|-------------------|
| `00` | Lifecycle | LC01-LC14 |
| `10` | Operations | SB15-SB19, SB80-SB85 |
| `20` | Primary Subsystem | SB20-SB29 |
| `30` | Circularity | SB30-SB39 |
| `40` | Software | SB40-SB49 |
| `50` | Structures | SB50-SB59 |
| `60` | Storages | SB60-SB69 |
| `70` | Propulsion | SB70-SB79 |
| `80` | Energy | SB86-SB89 |
| `90` | Tables/Schemas/Diagrams/Reference | SB90-SB99 |

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
00_00_PLAN_LC02_SPACET_safety-program_v01.md
00_70_FHA_SB70_SYS_propulsion_v01.md
00_40_REQ_SB40_SW_software-safety-reqs_v01.md
00_20_TRC_SB20_SPACET_traceability-matrix_v01.xlsx
00_90_SCH_SB90_GEN_hazard-log-schema_v01.json
24_40_REQ_SB40_SW_electrical-power-software_v01.md
00_10_PLAN_SB15_GEN_operations-plan_v01.md
00_80_FHA_SB86_SYS_energy-system_v01.md
```

### ❌ Invalid

```
00_00_PLAN_SB15_SPACET_safety-program_v01.md  # BUCKET=00 requires LC, not SB
00_70_FHA_SB00_SYS_propulsion_v01.md          # SB00 not allowed (reserved)
00_70_FHA_SB40_SYS_propulsion_v01.md          # BUCKET=70 requires SB70-SB79
00_70_FHA_LC01_SYS_propulsion_v01.md          # BUCKET≠00 requires SB, not LC
00_40_REQ_SB70_SW_software_v01.md             # BUCKET=40 requires SB40-SB49
00-70-FHA-SB70-SYS-propulsion-v01.md          # Wrong delimiter
00_70_FHA_SB70_SYS_propulsion_v1.md           # VERSION must be vNN
00_99_LST_SB90_GEN_glossary_v01.md            # Invalid BUCKET
00_70_FHA_SB70_SYS_PropulsionFHA_v01.md       # Uppercase in DESCRIPTION
00_70_fha_SB70_SYS_propulsion_v01.md          # Lowercase TYPE
```

## Common Mistakes

1. **Wrong subject category for BUCKET=00**: Must use LC01-LC14, not SB
   - Fix: Use LC_OR_SUBBUCKET field with LC01-LC14
   - Example: `00_00_PLAN_SB15_SPACET_...` → `00_00_PLAN_LC02_SPACET_...`

2. **Using wrong subbucket range for bucket**: Each bucket has specific ranges
   - Fix: Use the correct subbucket range for your bucket
   - Example: `00_70_FHA_SB40_SYS_...` → `00_70_FHA_SB70_SYS_...`
   - Example: `00_40_REQ_SB20_SW_...` → `00_40_REQ_SB40_SW_...`

3. **Using SB00-SB14**: These are reserved and not allowed
   - Fix: Use bucket-specific ranges starting from SB15
   - Example: `00_70_FHA_SB00_SYS_...` → `00_70_FHA_SB70_SYS_...`

4. **Wrong delimiters**
   - Fix: Use `_` between fields, `-` inside fields only
   - Example: `00-70-FHA` → `00_70_FHA`

5. **Wrong version format**
   - Fix: Always use 2 digits after `v`
   - Example: `v1` → `v01`

6. **Uppercase in DESCRIPTION**
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
