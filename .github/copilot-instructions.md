# GitHub Copilot Instructions for AMPEL360 Space-T

## File Naming Convention (MANDATORY)

**CRITICAL**: All files created or renamed in this repository MUST follow the Nomenclature Standard v1.0.

### Required Pattern

```
[ROOT]_[BUCKET]_[TYPE]_[VARIANT]_[DESCRIPTION]_[VERSION].[EXT]
```

### Quick Reference

- **ROOT**: 2 digits (e.g., `00`, `24`, `72`)
- **BUCKET**: `00|10|20|30|40|50|60|70|80|90`
- **TYPE**: 2-8 uppercase (e.g., `PLAN`, `FHA`, `REQ`, `STD`)
- **VARIANT**: Uppercase with hyphens (e.g., `Q100BL`, `DRAFT`, `LC02-Q100BL`)
- **DESCRIPTION**: lowercase-kebab-case (e.g., `safety-program`, `propulsion`)
- **VERSION**: `v` + 2 digits (e.g., `v01`, `v02`)
- **EXT**: lowercase (e.g., `md`, `json`, `xlsx`)

### Special Rules

1. **BUCKET=00** requires **VARIANT** to start with `LC01` through `LC14`
   - Valid: `00_00_PLAN_LC02-Q100BL_safety-program_v01.md`
   - Invalid: `00_00_PLAN_Q100BL_safety-program_v01.md`

2. Use `_` only between fields; use `-` only inside VARIANT and DESCRIPTION

3. Validate all files: `python validate_nomenclature.py <filename>`

### Examples

✅ `00_00_PLAN_LC02-Q100BL_safety-program_v01.md`
✅ `00_70_FHA_SYS_propulsion_v01.md`
✅ `00_40_REQ_SW_software-safety-reqs_v01.md`
✅ `00_90_SCH_GEN_hazard-log-schema_v01.json`

### Excluded Files

These files are exempt from the nomenclature standard:
- `README.md`, `LICENSE`, `EXAMPLES.md`, `STRUCTURE_SUMMARY.md`
- `.gitignore`, `.gitattributes`
- Files in `.git/`, `.github/`, `node_modules/`, `__pycache__/`, etc.

### Validation

Always validate your files before committing:
```bash
python validate_nomenclature.py <filename>
python validate_nomenclature.py --check-all
```

### Documentation

Full standard: `00_00_STD_LC01-Q100BL_nomenclature-standard_v01.md`

---

## Template Usage (MANDATORY)

When creating a new file of a specific `TYPE`, you MUST use the appropriate template:

1. **Look up** the template in `templates/[TYPE].md`
2. **Read** the template content
3. **Generate** the new file using the requested `BUCKET`, `VARIANT`, and `DESCRIPTION`
4. **Fill** the placeholders (`{{...}}`) with context from the user's prompt

### Available Templates

| TYPE | Template | Purpose |
|------|----------|---------|
| `PLAN` | `templates/PLAN.md` | Project plans, safety plans, management plans |
| `STD` | `templates/STD.md` | Standards and specifications |
| `FHA` | `templates/FHA.md` | Functional Hazard Assessments |
| `REQ` | `templates/REQ.md` | Requirements specifications |

### Template Placeholders

- `{{DESCRIPTION}}` - Replace with the file's description field
- `{{TITLE}}` - Replace with human-readable title (capitalize description)
- `{{VARIANT}}` - Replace with the variant code
- `{{BUCKET}}` - Replace with the bucket code
- `{{LC_PHASE}}` - Replace with lifecycle phase (for BUCKET=00)
- `{{OWNER}}` - Replace with responsible owner/team
- `{{SYSTEM_NAME}}` - Replace with system name (for FHA)

### Scaffolding Script

Use the scaffolding script to automate file creation:
```bash
python scripts/scaffold.py <ROOT> <BUCKET> <TYPE> <VARIANT> <DESC> <VER>
```

Example:
```bash
python scripts/scaffold.py 00 70 FHA SYS propulsion v01
```

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
