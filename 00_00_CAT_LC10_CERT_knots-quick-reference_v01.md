---
title: "Knots Quick Reference"
type: CAT
variant: "CERT"
status: Active
---

# AMPEL360 Space-T Knots Quick Reference

## What is a Knot?

A **knot** is a cross-cutting workflow element that represents certification/compliance activities spanning multiple ATA systems.

## Active Knots

### K01: Certification Authority Basis
**Status:** Active | **Owner:** Regulatory Affairs

**Affected Systems:** 52 ATAs across all axes (O/P, T, N, SIMTEST)
- Full list: 00, 01, 02, 03, 04, 11, 13-19, 21, 22, 24-28, 32-35, 38, 42-44, 47, 48, 52, 56, 58, 59, 67-69, 72-74, 76, 90, 93, 96, 100, 105, 106, 109, 110, 112, 114, 115

**Tasks:**
- **T001**: Define Certification Basis and Decision Criteria (8-12 weeks)
- **T002**: Map Compliance Objectives to Evidence and Tests (12-16 weeks)

**Key Deliverables:**
- `00_00_PLAN_LC10_CERT_certification-basis_v01.md`
- `00_00_TRC_LC10_CERT_compliance-matrix_v01.md`

**Documentation:** `00_00_PLAN_LC10_CERT_knot-k01-certification-authority-basis_v01.md`

---

## Quick Commands

### Validate Knot Data
```bash
# Validate schema
python3 -c "
import json, jsonschema
schema = json.load(open('00_90_SCH_SB00_GEN_knots-data-structure_v01.json'))
data = json.load(open('00_90_CAT_SB00_CERT_knots-catalog_v01.json'))
jsonschema.validate(instance=data, schema=schema)
print('✓ Valid')
"
```

### View Knot Details
```bash
# Extract K01 details
python3 -c "
import json
catalog = json.load(open('00_90_CAT_SB00_CERT_knots-catalog_v01.json'))
k01 = catalog['knots']['K01']
print(f'Title: {k01[\"title\"]}')
print(f'ATAs: {len(k01[\"affected_atas\"])} systems')
print(f'Tasks: {len(k01[\"task_templates\"])}')
for task in k01['task_templates']:
    print(f'  - {task[\"id\"]}: {task[\"title\"]}')
"
```

---

## File Naming Pattern

**Knot Documentation:**
```
00_00_PLAN_LC10_CERT_knot-k##-[name]_v##.md
```

**Knot Deliverables (per ATA):**
```
[ATA]_00_[TYPE]_LC10_CERT_[description]_v##.md
```

**Examples:**
- `00_00_PLAN_LC10_CERT_knot-k01-certification-authority-basis_v01.md`
- `21_00_PLAN_LC10_CERT_certification-basis_v01.md`
- `22_00_TRC_LC10_CERT_compliance-matrix_v01.md`

---

## Key Files

| File | Purpose |
| :--- | :--- |
| `00_90_SCH_SB00_GEN_knots-data-structure_v01.json` | JSON Schema definition |
| `00_90_CAT_SB00_CERT_knots-catalog_v01.json` | Machine-readable knot data |
| `00_00_IDX_LC10_CERT_certification-knots-index_v01.md` | Complete knots index |
| `00_00_PLAN_LC10_CERT_knot-k01-*_v01.md` | K01 detailed documentation |

---

## Integration Checklist

For each ATA system affected by K01:

- [ ] Review K01 documentation
- [ ] Identify system-specific requirements
- [ ] Assign task responsibilities
- [ ] Execute T001: Define certification basis
- [ ] Execute T002: Create compliance matrix
- [ ] Update traceability links
- [ ] Submit deliverables for review
- [ ] Coordinate with Regulatory Affairs

---

## Support

**Contacts:**
- Certification Manager: [Contact]
- Regulatory Affairs: [Contact]
- Configuration Management: [Contact]

**Resources:**
- Full Index: `00_00_IDX_LC10_CERT_certification-knots-index_v01.md`
- OPT-IN Framework: `README.md`
- Nomenclature Standard: `00_00_STD_LC01_SPACET_nomenclature-standard_v02.md`

---

**Version:** v01 | **Date:** 2025-12-15 | **Status:** Active
