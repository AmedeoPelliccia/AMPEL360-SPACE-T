# AMPEL360 Space-T Document Templates

This directory contains standardized templates for creating compliant documentation artifacts.

## Available Templates

### 1. PLAN.md - Project Plans & Safety Plans
**Usage**: Project management plans, safety plans, quality plans, configuration management plans

**Based on**: ECSS-M-ST-10C and DO-178C PSAC structure

**Example**:
```bash
python scripts/scaffold.py 00 00 PLAN LC02-Q100BL safety-program v01
```

### 2. STD.md - Standards & Specifications
**Usage**: Internal standards, specifications, guidelines, procedures

**Based on**: ISO/IEC Directives and ECSS standards structure

**Example**:
```bash
python scripts/scaffold.py 00 00 STD LC01-Q100BL coding-standard v01
```

### 3. FHA.md - Functional Hazard Assessment
**Usage**: Safety analysis documents following SAE ARP4761 methodology

**Based on**: SAE ARP4761 and DO-178C safety assessment

**Example**:
```bash
python scripts/scaffold.py 00 70 FHA SYS propulsion v01
```

### 4. REQ.md - Requirements Specification
**Usage**: Requirements documents for systems, software, hardware

**Based on**: IEEE 29148 requirements engineering standard

**Example**:
```bash
python scripts/scaffold.py 00 40 REQ SW software-requirements v01
```

## Template Placeholders

All templates support the following placeholders:

| Placeholder | Description | Example |
|-------------|-------------|---------|
| `{{DESCRIPTION}}` | File description field | `safety-program` |
| `{{TITLE}}` | Human-readable title | `Safety Program` |
| `{{VARIANT}}` | Configuration variant | `LC02-Q100BL` |
| `{{BUCKET}}` | Domain bucket code | `70` |
| `{{ROOT}}` | ATA chapter code | `00` |
| `{{LC_PHASE}}` | Lifecycle phase (for BUCKET=00) | `02` |
| `{{OWNER}}` | Responsible owner/team | `Safety WG` |
| `{{SYSTEM_NAME}}` | System name (for FHA) | `Propulsion System` |
| `{{DATE}}` | Current date | `2025-12-14` |

## Using Templates

### Method 1: Scaffolding Script (Recommended)

```bash
python scripts/scaffold.py <ROOT> <BUCKET> <TYPE> <VARIANT> <DESC> <VER>
```

The script will:
1. Load the appropriate template
2. Replace all placeholders
3. Create the file with correct nomenclature
4. Validate the filename

### Method 2: Manual (Copy & Edit)

1. Copy the template file: `cp templates/PLAN.md ./my-new-file.md`
2. Rename to follow nomenclature: `00_00_PLAN_LC02-Q100BL_my-plan_v01.md`
3. Edit and replace all `{{...}}` placeholders
4. Validate: `python validate_nomenclature.py <filename>`

### Method 3: GitHub Copilot (AI-Assisted)

GitHub Copilot is configured to automatically use these templates when you ask it to create a new document. Simply request:

> "Create a new FHA for the propulsion system"

Copilot will:
1. Load the FHA template
2. Generate proper filename
3. Fill placeholders with context
4. Create the file

## Adding New Templates

To add a new template type:

1. **Create template file**: `templates/<TYPE>.md`
2. **Use placeholders**: `{{DESCRIPTION}}`, `{{TITLE}}`, etc.
3. **Update Copilot instructions**: Add mapping in `.github/copilot-instructions.md`
4. **Test with scaffold**: `python scripts/scaffold.py ...`
5. **Document**: Update this README

## Template Development Guidelines

### Structure
- Use YAML front matter for metadata
- Include clear section headings
- Provide examples and guidance text
- Use tables for structured data

### Placeholders
- Use `{{UPPERCASE_WITH_UNDERSCORES}}` format
- Document all placeholders in template comments
- Provide sensible defaults where possible

### Compliance
- Follow aerospace documentation standards (ECSS, DO-178C, SAE)
- Include traceability elements
- Provide verification/validation sections
- Support lifecycle management

## Validation

Template files themselves are excluded from nomenclature validation (they're in the `templates/` directory). However, files created FROM templates must follow the nomenclature standard.

## References

- **Nomenclature Standard**: `00_00_STD_LC01-Q100BL_nomenclature-standard_v01.md`
- **Scaffolding Tool**: `scripts/scaffold.py`
- **Copilot Instructions**: `.github/copilot-instructions.md`
- **Automation Guide**: `00_00_IDX_LC01-Q100BL_nomenclature-automation-guide_v01.md`

---

**Last Updated**: 2025-12-14  
**Version**: 1.0  
**Maintained by**: Configuration Management WG
