# GATE-003: Trace Link Validation Guide

**Version**: 1.1  
**Date**: 2026-01-07  
**Status**: Active  
**Owner**: Configuration Management WG

## Overview

GATE-003 validates trace link integrity across the repository to ensure all markdown links reference existing files or known placeholder structures.

## Validator Usage

### Basic Usage

```bash
# Validate all markdown files (strict mode)
python scripts/validate_trace_links.py --check-all

# Validate with template/placeholder skipping (recommended for CI)
python scripts/validate_trace_links.py --check-all --skip-templates

# Validate a single file
python scripts/validate_trace_links.py --check-file path/to/file.md

# Validate a directory
python scripts/validate_trace_links.py --check-dir path/to/directory
```

### Skip-Templates Mode

The `--skip-templates` flag enables lenient validation suitable for repositories with:
- Template files containing placeholders (e.g., `{{DESCRIPTION}}`)
- Structural directories under active build-out
- Planned content referenced before creation

**What is skipped:**
1. **Template placeholders**: Links containing `{{...}}` or `{%...%}` patterns
2. **Placeholder directories**: TASKS/, DECISIONS/, EVIDENCE/, MONITORING/, diagrams/, figures/
3. **Structural directories without index files**:
   - ATA chapter directories (ATA_00, ATA_91, ATA_93, etc.)
   - Numbered subdirectories (01_WBS/, 02_IDS_REGISTRY/, etc.)
   - Stakeholder directories (STK_CM-, STK_AI-, etc.)

## Current Status (as of 2026-01-07)

### Validation Results

| Mode | Broken Links | Status |
|------|--------------|--------|
| Strict (no flags) | 1,000+ | ❌ Failing (expected during build-out) |
| Skip-templates | 490 | ⚠️ Acceptable (planned content) |

### Broken Link Breakdown (Skip-Templates Mode)

| Category | Count | Description |
|----------|-------|-------------|
| Missing files | 420 | Planned evidence, decisions, traceability files |
| Parent directories | 52 | Navigation links to `../` without index files |
| Sibling structural directories | 10 | MONITORING/, SCHEMAS/, ASSETS/ |
| Other | 8 | Miscellaneous |

**Total**: 490 broken links

### Remediation Progress

- ✅ **Phase 1 Complete**: Template placeholder detection (reduced 1,000+ → 784)
- ✅ **Phase 2 Complete**: Structural directory patterns (reduced 784 → 490)
- 📋 **Phase 3 Planned**: PORTAL structure build-out (target: <100 broken links)
- 📋 **Phase 4 Planned**: Baseline readiness (target: 0 critical broken links)

## Expected Link Patterns

### Valid Patterns (Always Pass)

1. **External URLs**: `https://example.com`, `mailto:user@example.com`
2. **Anchor links**: `#section-name`
3. **Existing files**: Links to files that exist in the repository
4. **Directories with index files**: Links to directories containing README.md or index.md

### Skipped Patterns (Pass with --skip-templates)

1. **Template placeholders**: `diagrams/{{DESCRIPTION}}.svg`
2. **Placeholder directories**: `./TASKS/`, `./EVIDENCE/`
3. **Structural directories**: `../ATA_00/`, `01_WBS/`, `STK_CM-*/`

### Invalid Patterns (Always Fail)

1. **Non-existent files**: Links to files that don't exist
2. **Typos**: Misspelled filenames or paths
3. **Outdated references**: Links to renamed or moved files

## CI Configuration

### GitHub Actions Workflow

```yaml
- name: GATE-003 - Trace Link Integrity Check
  run: |
    python scripts/validate_trace_links.py --check-all --skip-templates
  continue-on-error: false
```

### Exit Codes

- `0`: All validations passed
- `1`: Validation errors found (broken links)
- `2`: Script error (file not found, etc.)

## Remediation Procedures

### For Template Files

**Symptom**: Broken link to `{{PLACEHOLDER}}` pattern

**Remediation**: None required - these are skipped with `--skip-templates`

### For Structural Directories

**Symptom**: Link to ATA_XX/ or numbered subdirectory fails

**Remediation Options**:
1. **Option A (Recommended)**: Use `--skip-templates` flag
2. **Option B**: Create README.md or index.md in the directory
3. **Option C**: Wait for PORTAL structure build-out

### For Missing Files

**Symptom**: Link to specific file that doesn't exist

**Remediation Options**:
1. **Option A (Immediate)**: Create the referenced file
2. **Option B (Short-term)**: Remove or comment out the link
3. **Option C (Long-term)**: Track in PORTAL build-out plan

### For Parent Directory Links

**Symptom**: Link to `../` fails validation

**Remediation Options**:
1. **Option A (Recommended)**: Create index file in parent directory
2. **Option B**: Use `--skip-templates` flag temporarily
3. **Option C**: Replace with explicit link to parent's index file

## PORTAL Structure Build-Out Plan

### Phase 3: Missing Stakeholder Directories

**Status**: Planned  
**Timeline**: Q1 2026  
**Broken Links**: ~200

Create missing stakeholder portal directories:
- STK_PMO-pmo-program-management-office/
- STK_SAF-saf-safety/
- STK_OPS-ops-operations/
- STK_SPACEPORT-spaceport-spaceport-airport-ops/
- STK_MRO-mro-mro-maintenance/
- STK_TEST-test-ivvq-testing/
- STK_PHM-phm-physical-hardware-mechanical-engineering/

### Phase 4: Numbered Subdirectory Content

**Status**: Planned  
**Timeline**: Q1-Q2 2026  
**Broken Links**: ~420

Create content in numbered subdirectories:
- 01_WBS/ (work breakdown structures)
- 02_IDS_REGISTRY/ (identifier registries)
- 03_SCHEMA/ (schema definitions)
- 04_EXPORTS/ (export artifacts)
- 05_CI_GATES/ (CI gate documentation)
- 06_EVIDENCE/ (evidence packages)
- 07_DECISIONS/ (decision logs)
- 08_TRACEABILITY/ (traceability matrices)

### Phase 5: Index File Generation

**Status**: Planned  
**Timeline**: Q2 2026  
**Broken Links**: ~52

Auto-generate index files for parent directories:
```bash
# Planned script
python scripts/generate_directory_indexes.py --all
```

## Whitelist Management

### Adding New Structural Patterns

If you need to add a new structural directory pattern to skip validation:

1. Edit `scripts/validate_trace_links.py`
2. Update `STRUCTURAL_DIRECTORY_PATTERNS` list:
   ```python
   STRUCTURAL_DIRECTORY_PATTERNS = [
       r'ATA_\d+',           # ATA chapter directories
       r'ATA_\d+_',          # ATA chapter directories with names
       r'^\d+_[A-Z_]+',      # Numbered subdirectories
       r'STK_[A-Z]+-',       # Stakeholder directories
       r'YOUR_NEW_PATTERN',  # Add new pattern here
   ]
   ```
3. Test locally before committing
4. Request CM WG approval for pattern additions

### Adding New Placeholder Directories

If you need to add a new placeholder directory type:

1. Edit `scripts/validate_trace_links.py`
2. Update `PLACEHOLDER_DIRECTORIES` set:
   ```python
   PLACEHOLDER_DIRECTORIES = {
       'TASKS', 'DECISIONS', 'EVIDENCE', 'MONITORING',
       'diagrams', 'figures', 'attachments',
       'your_new_placeholder'  # Add here
   }
   ```

## Best Practices

### For Authors

1. **Use relative links**: Prefer `./file.md` or `../dir/file.md` over absolute paths
2. **Verify links locally**: Run validator before committing
3. **Use descriptive link text**: Avoid "click here" or bare URLs
4. **Check for typos**: Most broken links are due to typos

### For Reviewers

1. **Run validation**: Always run `--skip-templates` mode in CI
2. **Categorize failures**: Distinguish template placeholders from real errors
3. **Track planned content**: Document expected future links
4. **Request fixes**: Ask authors to fix broken links in active documentation

### For Repository Maintainers

1. **Monitor weekly**: Check gate status in weekly governance audit
2. **Plan build-out**: Prioritize creating most-referenced missing files
3. **Update patterns**: Add new structural patterns as repository evolves
4. **Document exceptions**: Track known acceptable broken links

## Troubleshooting

### Issue: Too many false positives

**Solution**: Use `--skip-templates` flag

### Issue: Validator too slow

**Solution**: 
- Use `--check-dir` for specific directories
- Exclude large directories (already configured for node_modules, .git, etc.)

### Issue: Pattern not recognized

**Solution**: 
- Check regex pattern syntax
- Test pattern locally with Python regex
- Add debug output with `--verbose` flag

### Issue: Links valid locally but fail in CI

**Solution**: 
- Check for case-sensitivity (Linux vs. Windows)
- Check for spaces or special characters in filenames
- Verify files are committed and pushed

## References

- **Validator Script**: `scripts/validate_trace_links.py`
- **Workflow**: `.github/workflows/governance-gates.yml`
- **Gate Index**: `00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_LC01_K05_DATA__ci-governance-gates_IDX_I01-R01_ACTIVE.md`
- **Issue Tracker**: GitHub Issues with label `gate-003`

## Change Log

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-12-16 | CM WG | Initial validator implementation |
| 1.1 | 2026-01-07 | CM WG | Added --skip-templates flag, structural patterns, documentation |

---

**Document Control**

| Field | Value |
|-------|-------|
| **Type** | IDX |
| **Status** | Active |
| **Owner** | Configuration Management WG |
| **Last Updated** | 2026-01-07 |
| **Next Review** | 2026-02-07 (monthly) |
