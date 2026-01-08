# Nomenclature Standard Enforcement for Agents

## Mandatory Instruction for All Agent Tasks

When creating, renaming, or managing any files in the AMPEL360 Space-T repository, you **MUST** strictly adhere to the **Nomenclature Standard v1.0**.

### Filename Format (Mandatory)

All files must follow this exact pattern:

```
[ROOT]_[BUCKET]_[TYPE]_[VARIANT]_[DESCRIPTION]_[VERSION].[EXT]
```

### Field Requirements

1. **ROOT** (2 digits): ATA chapter code or `00` for general/cross-domain
   - Pattern: `\d{2}`
   - Example: `00`, `24`, `72`

2. **BUCKET** (2 digits): Domain classification
   - Allowed values: `00`,`01`, `10`, `20`, `30`, `40`, `50`, `60`, `70`, `80`, `90`
    
| BLOCK   | Domain–Subsystem                         | Environment                      |
| ------- | ---------------------------------------- | -------------------------------- |
| **B00** | GENERAL (universal, implicit)            | **all**                          |
| **B01** | POLICIES (governance, standards, rules)  | **all**                          |
| **B10** | INFRASTRUCTURES AND SPACEPORTS           | **onboard + offboard + simtest** |
| **B20** | ROBOTICS                                 | **onboard + offboard**           |
| **B30** | CYBERSECURITY, DATA, COMMS               | **digital + onboard**            |
| **B40** | PHYSICS (pressure/thermal/cryo)          | **onboard + simtest**            |
| **B50** | PHYSICAL (aerostructures + HW, materials) | **onboard + offboard**           |
| **B60** | DYNAMICS (thrust/attitude/inerting)      | **onboard + simtest**            |
| **B70** | LAUNCHERS AND ENGINES                    | **onboard + simtest**            |
| **B80** | RENEWABLE ENERGY & CIRCULARITY           | **onboard + offboard**           |
| **B90** | OPTICS, SENSING AND OBSERVATION          | **onboard + offboard + simtest** |


3. **TYPE** (2-8 uppercase alphanumeric): Artifact type
   - Approved types: `PLAN`, `MIN`, `RPT`, `LOG`, `ACT`, `IDX`, `FHA`, `PSSA`, `SSA`, `FTA`, `ANA`, `REQ`, `DAL`, `TRC`, `CAT`, `LST`, `GLO`, `MAT`, `SCH`, `DIA`, `TAB`, `STD`
   - Pattern: `[A-Z0-9]{2,8}`

4. **VARIANT** (uppercase alphanumeric with hyphens): Configuration/baseline identifier
   - Pattern: `[A-Z0-9]+(?:-[A-Z0-9]+)*`
   - Common values: `Q100BL`, `DRAFT`, `PROTO`, `SYS`, `SW`, `HW`
   - **SPECIAL RULE**: If `BUCKET=00`, VARIANT **MUST** start with `LC01` through `LC14`
   - Example: `LC02-Q100BL`, `LC04-GEN`, `LC11-DRAFT`

5. **DESCRIPTION** (lowercase kebab-case): Human-readable label
   - Pattern: `[a-z0-9]+(?:-[a-z0-9]+)*`
   - Example: `safety-program`, `propulsion`, `hazard-log-schema`
   - Do NOT duplicate TYPE in description

6. **VERSION** (v + 2 digits): Revision control
   - Pattern: `v\d{2}`
   - Example: `v01`, `v02`, `v10`

7. **EXT** (lowercase): File extension
   - Pattern: `[a-z0-9]{1,6}`
   - Example: `md`, `xlsx`, `json`, `pdf`

### Critical Rules

1. **Delimiters**:
   - Use underscore `_` ONLY between fields
   - Use hyphen `-` ONLY inside VARIANT and DESCRIPTION fields

2. **Character Set**:
   - ASCII only (no spaces, no special characters beyond `_` and `-`)

3. **LC Constraint**:
   - If `BUCKET=00`, then `VARIANT` MUST match: `^LC(0[1-9]|1[0-4])(?:-[A-Z0-9]+(?:-[A-Z0-9]+)*)?$`

### Valid Examples

✅ `00_00_PLAN_LC02-Q100BL_safety-program_v01.md`
✅ `00_70_FHA_SYS_propulsion_v01.md`
✅ `00_40_REQ_SW_software-safety-reqs_v01.md`
✅ `00_20_TRC_Q100BL_traceability-matrix_v01.xlsx`
✅ `00_90_SCH_GEN_hazard-log-schema_v01.json`

### Invalid Examples

❌ `00_00_PLAN_Q100BL_safety-program_v01.md` (Missing LC prefix for BUCKET=00)
❌ `00-70-FHA-SYS-propulsion-v01.md` (Wrong delimiter)
❌ `00_70_FHA_SYS_propulsion_v1.md` (Wrong version format)
❌ `00_99_LST_GEN_glossary_v01.md` (Invalid bucket)

### Validation

Before completing any task that creates or renames files:

1. Run validation: `python validate_nomenclature.py <filename>`
2. Fix any errors reported
3. Only proceed when validation passes

### Reference

See `00_00_STD_LC01-Q100BL_nomenclature-standard_v01.md` for complete standard details.

---

**This instruction is MANDATORY for all agent tasks involving file creation or modification.**
