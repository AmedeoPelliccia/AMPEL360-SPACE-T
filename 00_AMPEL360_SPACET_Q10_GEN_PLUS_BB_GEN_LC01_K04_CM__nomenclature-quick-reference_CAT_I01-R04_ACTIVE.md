---
title: "Nomenclature Quick Reference v4.0"
type: CAT
variant: "PLUS"
status: "Normative"
owner: "Configuration Management WG"
---

# Nomenclature Quick Reference v4.0

**Quick lookup** for the AMPEL360 Space-T nomenclature standard v4.0.

---

## Format (12 fields)

```
[ROOT]_[PROJECT]_[PROGRAM]_[VARIANT]_[BUCKET]_[TYPE]_[LC|SB]_[TRIGGER_KNOT]_[AoR]__[DESCRIPTION]_[VERSION].[EXT]
```

**Note:** Double underscore `__` between AoR and DESCRIPTION is mandatory.

---

## Field Constraints

| Field | Format | Example | Notes |
|-------|--------|---------|-------|
| ROOT | 2-3 digits | `00`, `24`, `115` | ATA chapter or project code |
| PROJECT | `AMPEL360` | `AMPEL360` | Hard constraint (fixed) |
| PROGRAM | `SPACET` | `SPACET` | Fixed for AMPEL360-SPACE-T |
| VARIANT | Uppercase + hyphens | `PLUS`, `CERT`, `DRAFT` | Configuration context |
| BUCKET | 2 digits | `00`, `70`, `90` | Domain (00=LC only) |
| TYPE | 2-8 uppercase | `PLAN`, `FHA`, `REQ` | Artifact type |
| LC\|SB | LC01-LC14 or SB15-SB99 | `LC01`, `SB70` | Lifecycle or sub-bucket |
| TRIGGER_KNOT | K00 or K01-K99 | `K00`, `K01`, `K02` | Uncertainty trigger |
| AoR | Portal entry-point | `CM`, `CERT`, `SAF` | Area of Responsibility |
| DESCRIPTION | lowercase-kebab-case | `safety-program` | Human-readable label |
| VERSION | vNN (2 digits) | `v01`, `v02` | Revision number |
| EXT | lowercase | `md`, `json`, `csv` | File extension |

---

## Bucket Allowlist

| Code | Domain | LC/SB Rule |
|------|--------|------------|
| `00` | Lifecycle / Governance | **LC01-LC14 only** |
| `10` | Operations | SB15-SB19, SB80-SB85 |
| `20` | Primary Subsystem | SB20-SB29 |
| `30` | Circularity | SB30-SB39 |
| `40` | Software | SB40-SB49 |
| `50` | Structures | SB50-SB59 |
| `60` | Storages | SB60-SB69 |
| `70` | Propulsion | SB70-SB79 |
| `80` | Energy | SB86-SB89 |
| `90` | Tables/Schemas/Diagrams | SB90-SB99 |

---

## TYPE Vocabulary (Approved)

### Planning / Control
`PLAN`, `MIN`, `RPT`, `LOG`, `ACT`, `IDX`

### Safety Analyses
`FHA`, `PSSA`, `SSA`, `FTA`, `ANA`

### Requirements / Allocation
`REQ`, `DAL`, `TRC`

### Data / Reference
`CAT`, `LST`, `GLO`, `MAT`, `SCH`, `DIA`, `TAB`, `STD`

---

## TRIGGER_KNOT Codes

* **K00**: Global / non-knot artifacts (nomenclature, baselines, program-level)
* **K01-K99**: Specific uncertainty knots (see KNOTS catalog for details)

**Common knots:**
* `K01` = Certification authority basis
* `K02` = Hazard analysis and safety case
* `K03` = Hazmat and cryo propellants safety
* `K04` = Flight control authority and redundancy
* `K05` = Thermal protection system qualification
* `K06` = Decision governance and approvals
* `K10` = Industrialization, supply chain, quality

---

## AoR Allowlist (Portal Entry Points)

| Code | Stakeholder | Typical Artifacts |
|------|-------------|-------------------|
| `CM` | Configuration Management | Baselines, standards, governance |
| `CERT` | Certification & Authorities | Compliance, certification plans, authority engagement |
| `AI` | AI/ML Engineering | ML models, datasets, TEKNIA |
| `DATA` | Data Governance | Schemas, SSOT, identifiers |
| `OPS` | Operations | Operational concepts, procedures |
| `SE` | Systems Engineering | Architecture, ICDs, requirements |
| `SAF` | Safety | Hazard logs, safety cases, FHA/PSSA/SSA |
| `PMO` | Program Management Office | Schedules, milestones, resourcing |
| `CY` | Cybersecurity | Threat models, security requirements |
| `TEST` | IVVQ / Testing | Test plans, verification evidence |
| `MRO` | MRO / Maintenance | Maintainability, servicing, inspection |
| `SPACEPORT` | Spaceport/Airport Ops | Ground ops, fueling, turnaround |

**Note:** Use the code only (no `STK_` prefix in filenames).

---

## Variant Recommendations

* **PLUS**: AMPEL360+ baseline (enhanced configuration)
* **CERT**: Certification-controlled artifacts
* **BB**: Body-Brain protorobotics models (protorobotics integration)
* **DRAFT**: Work in progress (non-baseline)
* **PROTO**: Prototyping artifacts
* **SYS**: System-level scope
* **SW**: Software-specific scope
* **HW**: Hardware-specific scope
* **GEN**: General-purpose artifacts

---

## Examples

### Global program-level plan (K00, CM-owned)
```
00_AMPEL360_SPACET_PLUS_00_PLAN_LC02_K00_CM__safety-program_v01.md
```

### Certification authority basis (K01, CERT-owned)
```
00_AMPEL360_SPACET_CERT_00_PLAN_LC10_K01_CERT__certification-authority-basis_v01.md
```

### Propulsion FHA (K02, SAF-owned)
```
00_AMPEL360_SPACET_PLUS_70_FHA_SB70_K02_SAF__propulsion_v01.md
```

### ATA tasklist index (K03, SPACEPORT-owned)
```
78_AMPEL360_SPACET_PLUS_00_IDX_LC01_K03_SPACEPORT__k03-ata-78-tasklist_v01.md
```

### Knots data schema (K00, DATA-owned)
```
00_AMPEL360_SPACET_GEN_90_SCH_SB90_K00_DATA__knots-data-structure_v01.json
```

---

## Common Mistakes

❌ **Wrong:** `00_00_PLAN_LC02_AMPEL360_SPACET_PLUS_safety-program_v01.md`
* Missing TRIGGER_KNOT and AoR fields (v3.0 format)

❌ **Wrong:** `00_00_AMPEL360_SPACET_PLUS_PLAN_LC02_K00_CM__safety-program_v01.md`
* Wrong field order (BUCKET before PROJECT)

❌ **Wrong:** `00_AMPEL360_SPACET_PLUS_00_PLAN_LC02_K00_CM_safety-program_v01.md`
* Single underscore before DESCRIPTION (must use `__`)

❌ **Wrong:** `00_AMPEL360_SPACET_PLUS_00_PLAN_LC02_KNOT01_CM__safety-program_v01.md`
* Invalid TRIGGER_KNOT format (must be K00-K99)

❌ **Wrong:** `00_AMPEL360_SPACET_PLUS_00_PLAN_LC02_K00_STK_CM__safety-program_v01.md`
* AoR has STK_ prefix (not allowed in filename)

✅ **Correct:** `00_AMPEL360_SPACET_PLUS_00_PLAN_LC02_K00_CM__safety-program_v01.md`

---

## Validation

```bash
# Validate single file
python validate_nomenclature.py <filename>

# Validate all files
python validate_nomenclature.py --check-all

# Scaffold new file
python scripts/scaffold.py 00 AMPEL360 SPACET PLUS 00 PLAN LC01 K00 CM my-new-file v01
```

---

## See Also

* [Nomenclature Standard v4.0](00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_LC01_K04_CM__nomenclature-standard_STD_I01-R04_ACTIVE.md) - Full normative specification
* [Nomenclature Automation Guide v4.0](00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_LC01_K04_CM__nomenclature-automation-guide_IDX_I01-R04_ACTIVE.md) - Tooling documentation
* [KNOTS Catalog](00_AMPEL360_SPACET_Q10_CERT_PLUS_BB_GEN_SB90_K01_CERT__knots-catalog_CAT_I01-R01_ACTIVE.json) - Knot definitions

---

**Version:** v4.0  
**Date:** 2025-12-16  
**Owner:** Configuration Management WG
