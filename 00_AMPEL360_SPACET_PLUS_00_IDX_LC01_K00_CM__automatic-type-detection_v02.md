---
title: "Automatic TYPE Detection and Extension System"
type: IDX
variant: "LC01-SPACET"
status: Active
owner: "Configuration Management WG"
---

# Automatic TYPE Detection and Extension System

## Overview

This system automatically detects when new TYPE codes are being used in the repository that are not in the approved nomenclature vocabulary, and provides automated guidance for extending the standard.

## Purpose

1. **Early Detection**: Identify new TYPEs before they proliferate
2. **Guided Extension**: Provide step-by-step process for adding new TYPEs
3. **Template Generation**: Auto-create template stubs for new TYPEs
4. **Documentation**: Maintain consistency across all documentation
5. **Governance**: Ensure Configuration Management WG review

## Components

### 1. Detection Script (`scripts/detect_new_types.py`)

**Purpose**: Scan repository and identify unapproved TYPE codes

**Usage**:
```bash
# Basic detection
python scripts/detect_new_types.py

# Generate extension guide and template stubs
python scripts/detect_new_types.py --auto-suggest

# Generate template stub for specific TYPE
python scripts/detect_new_types.py --generate-template MAINT > templates/MAINT.md
```

**Features**:
- Scans all files following nomenclature pattern
- Compares against approved TYPE vocabulary
- Reports usage statistics for each detected TYPE
- Generates extension guide with examples
- Creates template stubs automatically

### 2. GitHub Actions Workflow (`.github/workflows/detect-new-types.yml`)

**Triggers**:
- On every push (any branch)
- On pull requests
- Weekly schedule (Monday 9:00 UTC)
- Manual workflow dispatch

**Actions**:
- **Detection**: Scans repository for new TYPEs
- **Issue Creation**: Creates/updates GitHub issue with findings
- **PR Comments**: Adds warning comments to PRs with new TYPEs
- **Artifacts**: Uploads extension guide for download

**Permissions**:
- Read repository contents
- Write issues
- Write PR comments

### 3. Extension Guide Generation

Automatically generates `NOMENCLATURE_EXTENSION_GUIDE.md` containing:

- List of detected new TYPE codes
- Example files using each TYPE
- Step-by-step extension process
- Checklist for standard updates
- Template creation guidance
- Testing procedures
- Approval process documentation

### 4. Template Stub Generation

Creates basic template structure for new TYPEs:

```markdown
---
title: "{{DESCRIPTION}}"
type: NEWTYPE
variant: "{{VARIANT}}"
status: Draft
---

# NEWTYPE: {{TITLE}}

## 1. Overview
[Content structure]
```

## Workflow

### Automatic Detection Flow

```
┌─────────────────┐
│  Push/PR/Schedule│
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Run Detection   │
│ Script          │
└────────┬────────┘
         │
         ├─── No New TYPEs ──► ✅ Success
         │
         └─── New TYPEs Found
                     │
                     ▼
         ┌─────────────────────┐
         │ Generate Extension  │
         │ Guide               │
         └──────────┬──────────┘
                    │
                    ├──► Create/Update GitHub Issue
                    │
                    ├──► Comment on PR (if applicable)
                    │
                    └──► Upload Artifacts
```

### Manual Extension Process

1. **Detection**
   ```bash
   python scripts/detect_new_types.py --auto-suggest
   ```

2. **Review Output**
   - Check `NOMENCLATURE_EXTENSION_GUIDE.md`
   - Review detected TYPEs and examples
   - Verify new TYPEs are justified

3. **Decision**
   - **Use Existing**: Refactor to use approved TYPEs
   - **Add New**: Follow extension process

4. **Extension Steps** (if adding new TYPE)
   
   **A. Update Validation**
   ```python
   # validate_nomenclature.py
   APPROVED_TYPES = {
       # ... existing types
       'MAINT',  # Maintenance procedures
       'OPER',   # Operation manuals
   }
   ```
   
   **B. Create Template**
   ```bash
   # Use generated stub or create custom
   vi templates/MAINT.md
   ```
   
   **C. Update Documentation**
   - Standard document: Add to Section 4.3
   - Copilot instructions: Add to template table
   - Templates README: Add to appropriate category
   
   **D. Test**
   ```bash
   # Validate
   python validate_nomenclature.py --check-all
   
   # Test scaffolding
   python scripts/scaffold.py 00 90 MAINT GEN test-doc v01
   ```
   
   **E. Submit**
   - Create PR with all changes
   - Include rationale and examples
   - Tag Configuration Management WG

5. **Approval**
   - CM WG review
   - Technical review
   - Merge and deploy

## Examples

### Example 1: Detecting New TYPEs

```bash
$ python scripts/detect_new_types.py

🔍 Scanning repository for TYPE codes...
Found 25 unique TYPE codes in use

⚠️  Detected 3 new TYPE codes not in approved vocabulary:
  - MAINT (5 files)
  - OPER (3 files)
  - RECYC (2 files)

💡 Run with --auto-suggest to generate extension guide and template stubs
```

### Example 2: Generating Extension Guide

```bash
$ python scripts/detect_new_types.py --auto-suggest

🔍 Scanning repository for TYPE codes...
Found 25 unique TYPE codes in use

⚠️  Detected 3 new TYPE codes not in approved vocabulary:
  - MAINT (5 files)
  - OPER (3 files)
  - RECYC (2 files)

📝 Generating extension guide...
✅ Extension guide written to: NOMENCLATURE_EXTENSION_GUIDE.md
✅ Template stub created: templates/MAINT.md
✅ Template stub created: templates/OPER.md
✅ Template stub created: templates/RECYC.md
```

### Example 3: GitHub Actions Detection

**Scenario**: PR introduces files with TYPE "MAINT"

**Action**: GitHub Actions automatically:
1. Detects "MAINT" is not approved
2. Generates extension guide
3. Comments on PR:
   ```
   ⚠️ New TYPE Codes Detected
   
   This PR introduces files with TYPE codes that are not in the 
   approved nomenclature vocabulary.
   
   Detected: MAINT (in 3 files)
   
   Action Required:
   - Review if existing TYPEs can be used
   - If new TYPE needed, follow extension process
   ```
4. Creates GitHub issue for tracking

## Configuration

### Detection Script Settings

**Excluded Paths** (inherited from validation script):
- `.git/`, `.github/`
- `templates/`
- `node_modules/`, `__pycache__/`
- Infrastructure files

**Scan Pattern**:
```regex
^(?P<root>\d{2})_(?P<bucket>\d{2})_(?P<type>[A-Z0-9]{2,8})_...
```

### GitHub Actions Schedule

Default: Weekly on Mondays at 9:00 UTC

Modify in `.github/workflows/detect-new-types.yml`:
```yaml
schedule:
  - cron: '0 9 * * 1'  # Change as needed
```

## Benefits

1. **Proactive Management**: Detect issues early
2. **Guided Process**: Clear steps for extension
3. **Automated Templates**: Reduce manual work
4. **Consistent Updates**: All docs updated together
5. **Governance**: CM WG visibility and control
6. **Historical Tracking**: GitHub issues provide audit trail

## Maintenance

**Maintained By**: Configuration Management WG  
**Last Updated**: 2025-12-14  
**Review Cycle**: Quarterly

### Update Triggers

- New TYPE detection logic changes
- Template stub format updates
- Extension process modifications
- GitHub Actions workflow changes

## References

- Nomenclature Standard: `00_00_STD_LC01-SPACET_nomenclature-standard_v01.md`
- Validation Script: `validate_nomenclature.py`
- Detection Script: `scripts/detect_new_types.py`
- GitHub Workflow: `.github/workflows/detect-new-types.yml`
- Copilot Instructions: `.github/copilot-instructions.md`

---

**Document ID**: 00_00_IDX_LC01-SPACET_automatic-type-detection_v01.md  
**Version**: 1.0  
**Status**: Active
