# Nomenclature Standard Automation Guide

## Overview

This guide explains the automated nomenclature enforcement system for AMPEL360 Space-T. All files created in this repository must follow the **Nomenclature Standard v1.0**.

## Automation Components

### 1. Validation Script (`validate_nomenclature.py`)

**Purpose**: Validates filenames against the nomenclature standard.

**Usage**:
```bash
# Validate a single file
python validate_nomenclature.py <filename>

# Validate all files in repository
python validate_nomenclature.py --check-all

# Validate specific directory
python validate_nomenclature.py --check-dir <path>

# Verbose output (show all results)
python validate_nomenclature.py --check-all --verbose
```

**Exit Codes**:
- `0`: All files valid
- `1`: One or more files invalid
- `2`: Script error

### 2. GitHub Actions Workflow (`.github/workflows/nomenclature-validation.yml`)

**Purpose**: Automatically validates all files on push and pull request.

**Trigger Events**:
- Push to any branch
- Pull request to any branch

**Actions**:
1. Checks out repository
2. Sets up Python environment
3. Runs validation script
4. Reports results in workflow logs
5. Fails CI if validation errors found

**Viewing Results**:
- Go to repository → Actions tab
- Select workflow run
- View validation output in job logs

### 3. Pre-commit Hook (`scripts/pre-commit`)

**Purpose**: Validates files locally before committing.

**Installation**:
```bash
# Copy hook to .git/hooks/
cp scripts/pre-commit .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

**Behavior**:
- Runs automatically on `git commit`
- Validates only staged files
- Blocks commit if validation fails
- Shows which files are non-compliant

**Bypass** (not recommended):
```bash
git commit --no-verify
```

### 4. GitHub Copilot Instructions (`.github/copilot-instructions.md`)

**Purpose**: Automatically instructs GitHub Copilot about nomenclature requirements.

**Integration**:
- GitHub Copilot automatically reads this file
- Provides context for all AI-assisted coding
- Ensures AI suggestions follow nomenclature

### 5. Agent Instructions (`.github/NOMENCLATURE_AGENT_INSTRUCTIONS.md`)

**Purpose**: Comprehensive reference for all agents (human and AI).

**Content**:
- Complete field requirements
- Valid/invalid examples
- Critical rules and constraints
- Validation procedures

## File Naming Pattern

```
[ROOT]_[BUCKET]_[TYPE]_[VARIANT]_[DESCRIPTION]_[VERSION].[EXT]
```

### Field Constraints

1. **ROOT**: 2 digits (`\d{2}`)
2. **BUCKET**: `00|10|20|30|40|50|60|70|80|90`
3. **TYPE**: 2-8 uppercase alphanumeric (`[A-Z0-9]{2,8}`)
4. **VARIANT**: Uppercase with hyphens (`[A-Z0-9]+(?:-[A-Z0-9]+)*`)
5. **DESCRIPTION**: lowercase-kebab-case (`[a-z0-9]+(?:-[a-z0-9]+)*`)
6. **VERSION**: `v` + 2 digits (`v\d{2}`)
7. **EXT**: lowercase alphanumeric (`[a-z0-9]{1,6}`)

### Special Rules

- **BUCKET=00** requires **VARIANT** to start with `LC01` through `LC14`
- Use `_` only between fields
- Use `-` only inside VARIANT and DESCRIPTION

## Excluded Files

The following files are automatically excluded from validation:

### By Name
- `README.md`, `LICENSE`, `EXAMPLES.md`
- `STRUCTURE_SUMMARY.md`
- `.gitignore`, `.gitattributes`
- `00_INDEX_README.md`
- `Dependencies.yaml`
- `Traceability_Matrix.csv`
- `Prompt_to_Artifact_Map.csv`
- Agent config files

### By Pattern
- `.*-xx_.*` (template files)
- `generate_.*\.py` (generator scripts)
- `validate_.*\.py` (validation scripts)
- `pre-commit` (git hooks)
- `.*_Agent_Config\.(yaml|json|yml)` (agent configs)
- `.*_Config\.(yaml|json|yml)` (config files)

### By Directory
- `.git/`, `.github/`
- `node_modules/`, `__pycache__/`
- `.pytest_cache/`, `.venv/`, `venv/`
- `dist/`, `build/`

## Workflow for New Files

### For Developers

1. **Create file** with compliant name:
   ```
   00_70_FHA_SYS_propulsion_v01.md
   ```

2. **Validate locally**:
   ```bash
   python validate_nomenclature.py 00_70_FHA_SYS_propulsion_v01.md
   ```

3. **Stage and commit**:
   ```bash
   git add 00_70_FHA_SYS_propulsion_v01.md
   git commit -m "Add propulsion FHA"
   ```
   
   Pre-commit hook validates automatically.

4. **Push**:
   ```bash
   git push
   ```
   
   GitHub Actions validates in CI.

### For AI Agents

1. **Read instructions** from `.github/copilot-instructions.md`

2. **Generate compliant filename**:
   - Follow pattern exactly
   - Validate fields individually
   - Check special rules (LC prefix for BUCKET=00)

3. **Validate before completing task**:
   ```python
   import subprocess
   result = subprocess.run(['python', 'validate_nomenclature.py', filename])
   if result.returncode != 0:
       # Fix filename and retry
   ```

4. **Include validation in task completion**:
   - Report validation status
   - Fix any errors
   - Confirm compliance

## Troubleshooting

### Common Errors

**Error**: `Filename does not match required pattern`
- **Solution**: Check field count (6 fields + extension)
- **Solution**: Check delimiters (use `_` between fields)

**Error**: `BUCKET=00 requires VARIANT to start with LC prefix`
- **Solution**: Add `LC01` through `LC14` prefix to VARIANT
- **Example**: Change `SPACET` to `LC02-SPACET`

**Error**: `Invalid BUCKET`
- **Solution**: Use only allowed buckets: `00, 10, 20, 30, 40, 50, 60, 70, 80, 90`

**Error**: `TYPE not in approved vocabulary`
- **Solution**: Use approved types or request extension via Configuration Management WG

**Error**: `VERSION must be 'vNN' with exactly 2 digits`
- **Solution**: Change `v1` to `v01`, `v2` to `v02`, etc.

### CI Failure

1. **Check workflow logs**:
   - Go to Actions tab
   - Select failed run
   - View job output

2. **Fix locally**:
   ```bash
   python validate_nomenclature.py --check-all
   ```

3. **Rename files**:
   ```bash
   git mv old_name.md 00_70_FHA_SYS_propulsion_v01.md
   git commit -m "Fix nomenclature compliance"
   git push
   ```

## References

- **Full Standard**: `00_00_STD_LC01-SPACET_nomenclature-standard_v01.md`
- **Agent Instructions**: `.github/NOMENCLATURE_AGENT_INSTRUCTIONS.md`
- **Copilot Instructions**: `.github/copilot-instructions.md`
- **Validation Script**: `validate_nomenclature.py`
- **Pre-commit Hook**: `scripts/pre-commit`
- **GitHub Workflow**: `.github/workflows/nomenclature-validation.yml`

## Support

For questions or change requests:
1. Review the full standard document
2. Check existing issues in repository
3. Contact Configuration Management WG
4. Submit change request following CM process

---

**Last Updated**: 2025-12-14  
**Version**: 1.0  
**Status**: Active
