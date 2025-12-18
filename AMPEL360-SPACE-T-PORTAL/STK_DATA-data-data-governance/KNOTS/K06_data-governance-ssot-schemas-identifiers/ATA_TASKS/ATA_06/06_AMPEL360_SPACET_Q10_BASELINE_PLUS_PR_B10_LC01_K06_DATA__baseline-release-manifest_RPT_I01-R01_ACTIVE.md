---
title: "ATA-06 Baseline Release Manifest - BL-0001"
type: RPT
variant: "SPACET"
report_date: "2025-12-15"
author: "Configuration Management WG"
status: Draft
baseline_id: "BL-0001"
ata_chapter: "06"
---

# ATA-06 Baseline Release Manifest - BL-0001

## Executive Summary

This manifest documents the first frozen baseline release of ATA-06 dimensional data exports. Baseline BL-0001 contains 8 identifiers (3 datums, 2 zones, 3 envelopes) exported from CAD and validated against the dimensional data schema. This release establishes the Single Source of Truth (SSOT) for spacecraft dimensional references.

**Baseline ID**: BL-0001  
**Release Date**: 2025-12-15  
**Approval Status**: Candidate (pending CM approval)  
**CAD Source**: SpaceT_Main_Assembly_v1.0.CATPart  

## 1. Introduction

### 1.1 Purpose

This baseline release manifest addresses Task T6 from the ATA-06 tasklist: "Produce a frozen baseline envelope set with release manifest."

The purpose of this manifest is to:
1. Document all artifacts included in baseline BL-0001
2. Provide checksums and validation results for each artifact
3. Record approval status and change history
4. Enable traceability to CAD source (SSOT)
5. Support downstream consumer adoption

### 1.2 Scope

**IN SCOPE:**
- All dimensional data exports in JSON format
- Identifier registry entries for BL-0001
- Schema definition and validation scripts
- Supporting documentation (plans, catalogs)

**OUT OF SCOPE:**
- CAD model files (maintained separately by Design Engineering)
- CSV exports (to be added in future baseline)
- Downstream consumer systems (documented separately)

### 1.3 Applicable Documents

| Doc ID | Title | Version |
| :--- | :--- | :--- |
| 06_00_IDX_LC01_SPACET_k06-ata-06-tasklist_I01-R01.md | ATA-06 SSOT Task List | v01 |
| 06_00_PLAN_LC01_SPACET_ssot-implementation-plan_I01-R01.md | SSOT Implementation Plan | v01 |
| 06_00_CAT_LC01_SPACET_identifier-registry_I01-R01.md | Identifier Registry | v01 |
| 06_90_SCH_SB00_GEN_dimensional-data-schema_I01-R01.json | Dimensional Data Schema | v01 |
| 06_90_SCH_SB00_GEN_dimensional-data-schema_I01-R01.md | Schema Documentation | v01 |

## 2. Baseline Contents

### 2.1 Export Files

#### Primary Export

| Artifact | File Name | Type | Size | Checksum (SHA256) |
| :--- | :--- | :--- | :--- | :--- |
| Dimensional Data Export | 06_90_TAB_SB00_GEN_dimensional-exports_I01-R01.json | JSON | 8.7 KB | TBD (computed on approval) |

**Contents Summary:**
- **Metadata**: Export timestamp, CAD source, baseline ID, schema version
- **Coordinate Frame**: Spacecraft body frame definition (origin, axes, units)
- **Datums**: 3 identifiers (DATUM-GLOBAL-001, DATUM-GLOBAL-002, DATUM-FUS-001)
- **Zones**: 2 identifiers (ZONE-PROP-001, ZONE-INTEG-001)
- **Envelopes**: 3 identifiers (ENVELOPE-GLOBAL-001, ENVELOPE-PROP-001, ENVELOPE-STRUCT-001)

**Total Identifiers**: 8

### 2.2 Supporting Documentation

| Artifact | File Name | Purpose | Version |
| :--- | :--- | :--- | :--- |
| Task List | 06_00_IDX_LC01_SPACET_k06-ata-06-tasklist_I01-R01.md | Task tracking | v01 |
| SSOT Plan | 06_00_PLAN_LC01_SPACET_ssot-implementation-plan_I01-R01.md | Implementation approach | v01 |
| Identifier Registry | 06_00_CAT_LC01_SPACET_identifier-registry_I01-R01.md | Identifier definitions | v01 |
| Schema (JSON) | 06_90_SCH_SB00_GEN_dimensional-data-schema_I01-R01.json | Validation schema | v01 |
| Schema (Docs) | 06_90_SCH_SB00_GEN_dimensional-data-schema_I01-R01.md | Schema documentation | v01 |
| This Manifest | 06_00_RPT_LC01_SPACET_baseline-release-manifest_I01-R01.md | Release documentation | v01 |

### 2.3 Validation Scripts

| Script | File Name | Purpose | Language |
| :--- | :--- | :--- | :--- |
| Dimensional Data Validator | scripts/validate_ata06_dimensions.py | JSON schema and business rule validation | Python 3 |

## 3. Validation Results

### 3.1 Schema Validation

**Status**: ✅ PASSED

```
============================================================
VALIDATION SUMMARY
============================================================

📋 INFO (5):
  • JSON Schema validation passed
  • Total identifiers validated: 8
  • Units: length=mm, angle=deg
  • Baseline ID: BL-0001
  • Approval status: candidate

============================================================
✅ VALIDATION PASSED - No errors or warnings
============================================================
```

**Validator**: scripts/validate_ata06_dimensions.py  
**Validation Date**: 2025-12-15  
**Exit Code**: 0 (success)

### 3.2 Identifier Validation

All 8 identifiers validated successfully:

| Identifier | Category | System | Format | Status |
| :--- | :--- | :--- | :--- | :--- |
| DATUM-GLOBAL-001 | DATUM | GLOBAL | ✅ Valid | Active |
| DATUM-GLOBAL-002 | DATUM | GLOBAL | ✅ Valid | Active |
| DATUM-FUS-001 | DATUM | FUS | ✅ Valid | Active |
| ZONE-PROP-001 | ZONE | PROP | ✅ Valid | Active |
| ZONE-INTEG-001 | ZONE | INTEG | ✅ Valid | Active |
| ENVELOPE-GLOBAL-001 | ENVELOPE | GLOBAL | ✅ Valid | Active |
| ENVELOPE-PROP-001 | ENVELOPE | PROP | ✅ Valid | Active |
| ENVELOPE-STRUCT-001 | ENVELOPE | STRUCT | ✅ Valid | Active |

**Uniqueness**: All identifiers are unique (no duplicates detected)  
**Format Compliance**: 100% (8/8 identifiers match required patterns)

### 3.3 Unit Consistency

**Length Unit**: mm (millimeters) - SI compliant ✅  
**Angle Unit**: deg (degrees) - Standard ✅  
**Consistency**: All dimensional values use declared units ✅

### 3.4 Nomenclature Validation

**Status**: ✅ PASSED

All files validated against Nomenclature Standard v2.0:
- 11 files checked
- 11 valid
- 0 invalid

## 4. CAD Source Traceability

### 4.1 CAD Model Information

| Field | Value |
| :--- | :--- |
| **CAD Tool** | CATIA V6 |
| **Version** | R2021x |
| **Model File** | SpaceT_Main_Assembly_v1.0.CATPart |
| **Export Script** | export_dimensions_v1.0.py |
| **Export Timestamp** | 2025-12-15T10:30:00Z |

### 4.2 CAD Baseline

| Field | Value |
| :--- | :--- |
| **CAD Baseline** | CAD-BL-2025-001 |
| **Design Review** | PDR (Preliminary Design Review) |
| **Approval Date** | 2025-12-10 |
| **Approved By** | Chief Engineer |

### 4.3 Change Traceability

This baseline reflects the following approved design changes:

| ECO Number | Description | Impact |
| :--- | :--- | :--- |
| ECO-001 | Establish initial datum set | New (8 identifiers) |
| - | No changes from previous baseline | First baseline (no predecessors) |

## 5. Downstream Consumer Impact

### 5.1 Affected Systems

The following downstream systems will consume this baseline:

| Consumer System | Impact | Action Required |
| :--- | :--- | :--- |
| Operations Planning | New | Adopt dimensional data for mission planning |
| Infrastructure Sim | New | Integrate envelope data into simulation models |
| Thermal Analysis | New | Use zone boundaries for thermal modeling |
| Structural Analysis | New | Use envelope data for structural verification |
| Integration Tools | New | Import dimensional data for integration planning |

### 5.2 Migration Path

**For new consumers:**
1. Download baseline package
2. Validate against schema
3. Import into consumer system
4. Verify integration
5. Report adoption evidence

**No migration needed**: This is the first baseline (no legacy data)

## 6. Approval Status

### 6.1 Current Status

**Status**: Candidate  
**Submitted Date**: 2025-12-15  
**Target Approval Date**: 2025-12-20

### 6.2 Approval Workflow

| Stage | Status | Approver | Date |
| :--- | :--- | :--- | :--- |
| **Technical Review** | Pending | Systems Engineering Lead | TBD |
| **Engineering Review** | Pending | Design Engineering Lead | TBD |
| **CM Review** | Pending | CM WG Chair | TBD |
| **Final Approval** | Pending | Chief Engineer | TBD |

### 6.3 Approval Criteria

- [ ] All validation checks pass (schema, identifiers, units)
- [ ] CAD source traceability established
- [ ] Supporting documentation complete
- [ ] Technical review completed with no major findings
- [ ] CM review completed with no major findings
- [ ] All artifacts properly named per nomenclature standard

## 7. Usage Instructions

### 7.1 Accessing the Baseline

**Repository Location**: AmedeoPelliccia/AMPEL360-SPACE-T  
**Branch**: copilot/define-ssot-and-identifiers (to be merged to main)  
**Tag** (when approved): `ata06-baseline-BL-0001`

**Files to Download:**
- Primary export: `06_90_TAB_SB00_GEN_dimensional-exports_I01-R01.json`
- Schema: `06_90_SCH_SB00_GEN_dimensional-data-schema_I01-R01.json`
- Identifier registry: `06_00_CAT_LC01_SPACET_identifier-registry_I01-R01.md`

### 7.2 Validating the Baseline

```bash
# Validate the export file
python scripts/validate_ata06_dimensions.py 06_90_TAB_SB00_GEN_dimensional-exports_I01-R01.json

# Expected output: ✅ VALIDATION PASSED
```

### 7.3 Integrating into Consumer Systems

**Python Example:**
```python
import json

# Load dimensional data
with open('06_90_TAB_SB00_GEN_dimensional-exports_I01-R01.json') as f:
    dim_data = json.load(f)

# Access coordinate frame
coord_frame = dim_data['coordinate_frame']
origin = coord_frame['origin']['identifier']  # "DATUM-GLOBAL-001"

# Access datums
datums = dim_data['data']['datums']
for datum in datums:
    print(f"{datum['identifier']}: {datum['name']}")

# Access zones
zones = dim_data['data']['zones']
for zone in zones:
    print(f"{zone['identifier']}: {zone['bounds']}")
```

### 7.4 Reporting Issues

If you discover issues with this baseline:

1. Verify you're using the correct baseline version (BL-0001)
2. Re-run validation to confirm issue
3. Submit issue via GitHub issue tracker with:
   - Baseline ID
   - Affected identifier(s)
   - Description of issue
   - Impact assessment
4. Tag: @ATA06-SSOT-Team

## 8. Change History

### 8.1 Baseline History

| Baseline ID | Date | Status | Changes |
| :--- | :--- | :--- | :--- |
| **BL-0001** | 2025-12-15 | Candidate | Initial baseline with 8 identifiers |

### 8.2 Future Baselines

Planned updates for future baselines:
- **BL-0002** (planned Q1 2026): Add CSV export format, expand identifier set
- **BL-0003** (planned Q2 2026): Add deployment configuration envelopes
- **BL-0004** (planned Q3 2026): Incorporate design changes from CDR

## 9. Restrictions and Limitations

### 9.1 Current Limitations

1. **JSON only**: CSV export format not yet implemented
2. **Limited identifier set**: Only 8 identifiers (minimal baseline)
3. **No deployment config**: Only launch configuration included
4. **Complex geometries**: Some envelopes use "complex" type (CAD-defined)

### 9.2 Known Issues

None at this time.

### 9.3 Planned Enhancements

- Add CSV export format (T4 continuation)
- Expand identifier set to cover all subsystems
- Add deployment configuration data
- Provide 3D visualization tool for envelopes

## 10. Appendices

### Appendix A: File Manifest

Complete list of files in baseline BL-0001:

```
06_00_CAT_LC01_SPACET_identifier-registry_I01-R01.md
06_00_IDX_LC01_SPACET_k06-ata-06-tasklist_I01-R01.md
06_00_PLAN_LC01_SPACET_ssot-implementation-plan_I01-R01.md
06_00_RPT_LC01_SPACET_baseline-release-manifest_I01-R01.md
06_90_SCH_SB00_GEN_dimensional-data-schema_I01-R01.json
06_90_SCH_SB00_GEN_dimensional-data-schema_I01-R01.md
06_90_TAB_SB00_GEN_dimensional-exports_I01-R01.json
scripts/validate_ata06_dimensions.py
```

### Appendix B: Validation Logs

Full validation output attached in artifact package.

### Appendix C: Checksums

SHA256 checksums to be computed and added upon approval.

---

**Document ID**: 06_00_RPT_LC01_SPACET_baseline-release-manifest_I01-R01.md  
**Baseline ID**: BL-0001  
**Status**: Candidate  
**Version**: v01  
**Date**: 2025-12-15  
**Next Review**: Upon CM approval
