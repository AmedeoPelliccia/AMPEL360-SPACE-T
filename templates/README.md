# AMPEL360 Space-T Document Templates

This directory contains standardized templates for creating compliant documentation artifacts. All 22 approved TYPE codes have corresponding templates.

## Available Templates (22 Total)

### Planning / Control (6 templates)

1. **PLAN.md** - Project Plans & Safety Plans
   - Based on: ECSS-M-ST-10C and DO-178C PSAC
   - Use for: Project management plans, safety plans, quality plans

2. **MIN.md** - Meeting Minutes
   - Based on: Standard meeting documentation practices
   - Use for: Technical meetings, reviews, working group meetings

3. **RPT.md** - Reports
   - Based on: Technical reporting standards
   - Use for: Analysis reports, status reports, assessment reports

4. **LOG.md** - Logs
   - Based on: Issue tracking and event logging practices
   - Use for: Issue logs, event logs, change logs, hazard logs

5. **ACT.md** - Action Items
   - Based on: Action item tracking standards
   - Use for: Action registers, task tracking

6. **IDX.md** - Indexes
   - Based on: Documentation indexing standards
   - Use for: Document indexes, artifact catalogs

### Safety Analyses (5 templates)

7. **FHA.md** - Functional Hazard Assessment
   - Based on: SAE ARP4761 and DO-178C
   - Use for: System-level hazard analysis

8. **PSSA.md** - Preliminary System Safety Assessment
   - Based on: SAE ARP4761 and DO-178C
   - Use for: Preliminary safety analysis during development

9. **SSA.md** - System Safety Assessment
   - Based on: SAE ARP4761 and DO-178C
   - Use for: Final safety compliance demonstration

10. **FTA.md** - Fault Tree Analysis
    - Based on: SAE ARP4761 and IEC 61025
    - Use for: Quantitative failure probability analysis

11. **ANA.md** - Analysis
    - Based on: Engineering analysis standards
    - Use for: Trade studies, performance analysis, stress analysis

### Requirements / Allocation (3 templates)

12. **REQ.md** - Requirements Specification
    - Based on: IEEE 29148 requirements engineering
    - Use for: System, software, hardware requirements

13. **DAL.md** - Development Assurance Level Assignment
    - Based on: DO-178C and DO-254
    - Use for: Safety criticality level assignments

14. **TRC.md** - Traceability Matrix
    - Based on: DO-178C and DO-254 traceability
    - Use for: Requirements traceability, verification coverage

### Data / Reference (8 templates)

15. **CAT.md** - Catalog
    - Based on: Cataloging and classification standards
    - Use for: Component catalogs, document catalogs

16. **LST.md** - List
    - Based on: Structured data listing practices
    - Use for: Item lists, inventories, rosters

17. **GLO.md** - Glossary
    - Based on: Terminology management standards
    - Use for: Term definitions, acronyms, abbreviations

18. **MAT.md** - Material Specification
    - Based on: Material specification standards (ASTM, ISO)
    - Use for: Material properties, specifications, certifications

19. **SCH.md** - Schema
    - Based on: JSON Schema, XML Schema standards
    - Use for: Data structure definitions, validation schemas

20. **DIA.md** - Diagram
    - Based on: Technical drawing and diagramming standards
    - Use for: Architecture diagrams, flow diagrams, state diagrams

21. **TAB.md** - Table
    - Based on: Data table documentation standards
    - Use for: Data tables, lookup tables, mapping tables

22. **STD.md** - Standard
    - Based on: ISO/IEC Directives and ECSS standards
    - Use for: Internal standards, specifications, guidelines

## Template Placeholders

All templates support the following placeholders:

| Placeholder | Description | Example |
|-------------|-------------|---------|
| `{{DESCRIPTION}}` | File description field | `safety-program` |
| `{{TITLE}}` | Human-readable title | `Safety Program` |
| `{{VARIANT}}` | Configuration variant | `LC02-SPACET` |
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
2. Rename to follow nomenclature: `00_00_PLAN_LC02-SPACET_my-plan_I01-R01.md`
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

- **Nomenclature Standard**: `00_00_STD_LC01-SPACET_nomenclature-standard_I01-R01.md`
- **Scaffolding Tool**: `scripts/scaffold.py`
- **Copilot Instructions**: `.github/copilot-instructions.md`
- **Automation Guide**: `00_00_IDX_LC01-SPACET_nomenclature-automation-guide_I01-R01.md`

---

**Last Updated**: 2025-12-14  
**Version**: 1.0  
**Maintained by**: Configuration Management WG
