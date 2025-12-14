# AMPEL360-SPACE-T-PORTAL Usage Examples

## Quick Start

### 1. Generate Basic Portal (Tasklists Only)

```bash
cd /home/runner/work/AMPEL360-SPACE-T/AMPEL360-SPACE-T
python scripts/generate_stakeholder_knot_structure.py
```

This creates:
- 12 stakeholder directories
- 14 knot categories
- 580+ markdown files with tasklists for each ATA
- 1 CSV knot register
- All files validated against nomenclature v2.0

### 2. Preview Changes (Dry-Run)

```bash
python scripts/generate_stakeholder_knot_structure.py --dry-run
```

Shows what would be created without actually creating files.

### 3. Generate Full Portal (With Individual Tasks)

```bash
python scripts/generate_stakeholder_knot_structure.py --full
```

This additionally creates ACT (Action) files for each task template within each ATA directory.

### 4. Force Regeneration

```bash
python scripts/generate_stakeholder_knot_structure.py --force
```

Overwrites existing files. Useful when updating the configuration.

## Navigation Examples

### Example 1: Configuration Manager Workflow

1. Start at the global index:
   ```
   AMPEL360-SPACE-T-PORTAL/00_00_IDX_LC01_SPACET_stakeholder-entrypoints_v01.md
   ```

2. Navigate to CM entry point:
   ```
   AMPEL360-SPACE-T-PORTAL/STK_CM-cm-configuration-management/
     00_00_IDX_LC01_SPACET_stakeholder-cm-entrypoint_v01.md
   ```

3. Select a knot (e.g., K06 - Data Governance):
   ```
   AMPEL360-SPACE-T-PORTAL/STK_CM-cm-configuration-management/KNOTS/
     K06_data-governance-ssot-schemas-identifiers/
       00_00_IDX_LC01_SPACET_k06-data-governance-ssot-schemas-identifiers_v01.md
   ```

4. View ATA-specific tasklist:
   ```
   AMPEL360-SPACE-T-PORTAL/STK_CM-cm-configuration-management/KNOTS/
     K06_data-governance-ssot-schemas-identifiers/ATA_TASKS/ATA_91/
       00_00_IDX_LC01_SPACET_k06-ata-91-tasklist_v01.md
   ```

### Example 2: Safety Engineer Workflow

1. Navigate to SAF entry point:
   ```
   AMPEL360-SPACE-T-PORTAL/STK_SAF-saf-safety/
     00_00_IDX_LC01_SPACET_stakeholder-saf-entrypoint_v01.md
   ```

2. Active knots for Safety:
   - K01 — certification-authority-basis
   - K03 — hazmat-cryo-propellants-safety-case
   - K05 — model-fidelity-verification-credit
   - K11 — human-factors-training-readiness
   - K12 — nvh-metrics-corridors-exposure

3. Select K03 (Hazmat/Cryo):
   ```
   AMPEL360-SPACE-T-PORTAL/STK_SAF-saf-safety/KNOTS/
     K03_hazmat-cryo-propellants-safety-case/
   ```

4. Review impacted ATAs: 12, 18, 26, 28, 47, 78, 81, 84, 110

## Configuration Examples

### Custom Configuration

Create a custom config file:

```json
{
  "portal_path": "MY-CUSTOM-PORTAL",
  "variant": "DRAFT",
  "root_code": "00",
  "bucket_code": "00",
  "version": "v02",
  "stakeholders": [
    {"id": "DEV", "name": "Development Team", "knots": ["K04","K05"]}
  ],
  "knots": {
    "K04": {
      "title": "integration-boundaries",
      "affected_atas": ["00","06","22"],
      "task_templates": [
        {"id": "T001", "title": "define-icds"}
      ]
    },
    "K05": {
      "title": "model-verification",
      "affected_atas": ["05","06"],
      "task_templates": [
        {"id": "T001", "title": "plan-correlations"}
      ]
    }
  }
}
```

Generate:
```bash
python scripts/generate_stakeholder_knot_structure.py --config my-config.json
```

## Validation Examples

### Validate All Portal Files

```bash
python validate_nomenclature.py --check-dir AMPEL360-SPACE-T-PORTAL
```

Expected output:
```
============================================================
Summary: 580 valid, 0 invalid (total: 580)
============================================================
```

### Validate Specific File

```bash
python validate_nomenclature.py \
  AMPEL360-SPACE-T-PORTAL/00_00_IDX_LC01_SPACET_stakeholder-entrypoints_v01.md
```

### Verbose Validation

```bash
python validate_nomenclature.py --check-dir AMPEL360-SPACE-T-PORTAL --verbose
```

Shows all validated files, not just errors.

## Integration with Engineering Tree

The portal references the main engineering tree:

```
Portal (Navigation)                     Engineering Tree (Content)
====================                    ===========================
STK_SE-se-systems-engineering/    →     AMPEL360_SPACE-T/
  KNOTS/                                  P-PROGRAM/
    K04_integration.../                     ATA_22-*/
      ATA_TASKS/                           O-OPS_ORG/
        ATA_22/                              ATA_22-*/
          tasklist.md  ─────────────────→   T-TECHNOLOGY/
            (references)                       ATA_22-*/
```

Each task file includes `affected_ata_paths` pointing to relevant directories in:
- `AMPEL360_SPACE-T/P-PROGRAM/ATA_{XX}-*/`
- `AMPEL360_SPACE-T/O-OPS_ORG/ATA_{XX}-*/`
- `AMPEL360_SPACE-T/T-TECHNOLOGY/ATA_{XX}-*/`
- `AMPEL360_SPACE-T/I-INFRASTRUCTURES/ATA_{XX}-*/`
- `AMPEL360_SPACE-T/N-NEURAL_NETWORKS/ATA_{XX}-*/`
- `AMPEL360_SPACE-T/T-SIMTEST/ATA_{XX}-*/`

## Statistics

Default generation (without --full):
- **12 stakeholders**
- **14 knots** (K01-K14)
- **580 markdown files** (IDX type)
- **1 CSV register**
- **100% nomenclature compliant**

With --full flag:
- Additional ACT files for each task × ATA combination
- Typically 3 tasks per knot × multiple ATAs = 1000+ additional files

## Maintenance

### Adding a New Stakeholder

Edit `scripts/stakeholder_knot_config.json`:

```json
{
  "stakeholders": [
    ...,
    {"id": "NEW", "name": "New Team", "knots": ["K01","K02"]}
  ]
}
```

Regenerate:
```bash
python scripts/generate_stakeholder_knot_structure.py --force
```

### Adding a New Knot

Edit `scripts/stakeholder_knot_config.json`:

```json
{
  "knots": {
    ...,
    "K15": {
      "title": "new-uncertainty-knot",
      "affected_atas": ["00","01"],
      "task_templates": [
        {"id": "T001", "title": "first-task"}
      ]
    }
  }
}
```

Update stakeholder assignments and regenerate.

### Updating Task Templates

Modify task templates in the knot definition:

```json
{
  "knots": {
    "K01": {
      "task_templates": [
        {"id": "T001", "title": "updated-task-name"},
        {"id": "T004", "title": "new-additional-task"}
      ]
    }
  }
}
```

Regenerate with `--force` flag.

## Troubleshooting

### Issue: "Config file not found"

**Solution**: Check path and filename:
```bash
ls -l scripts/stakeholder_knot_config.json
```

### Issue: "Bad DESCRIPTION after slugify"

**Solution**: Ensure description contains only lowercase letters, numbers, and hyphens.
Invalid: `My_Task!`, `TASK#1`
Valid: `my-task`, `task-1`

### Issue: "File already exists"

**Solution**: Use `--force` flag to overwrite:
```bash
python scripts/generate_stakeholder_knot_structure.py --force
```

## Advanced Usage

### Generate to Different Location

```bash
python scripts/generate_stakeholder_knot_structure.py \
  --repo-root /path/to/repo \
  --config custom-config.json
```

### Chain with Validation

```bash
python scripts/generate_stakeholder_knot_structure.py --force && \
  python validate_nomenclature.py --check-dir AMPEL360-SPACE-T-PORTAL
```

### Extract Statistics

```bash
# Count stakeholders
ls -d AMPEL360-SPACE-T-PORTAL/STK_* | wc -l

# Count total files
find AMPEL360-SPACE-T-PORTAL -type f | wc -l

# Find all tasklists
find AMPEL360-SPACE-T-PORTAL -name "*tasklist*.md" | wc -l

# List all knots for a stakeholder
ls AMPEL360-SPACE-T-PORTAL/STK_CM-*/KNOTS/
```

## See Also

- [Portal README](AMPEL360-SPACE-T-PORTAL/README.md)
- [Nomenclature Standard v2.0](00_00_STD_LC01_SPACET_nomenclature-standard_v02.md)
- [Generator Script](scripts/generate_stakeholder_knot_structure.py)
- [Configuration File](scripts/stakeholder_knot_config.json)
