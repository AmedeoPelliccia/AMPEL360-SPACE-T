# AMPEL360-SPACE-T

**Spacecraft CAXS (CA360º) — Computer-Aided Cross Sustainment Platform**

Complete OPT-INS Framework Directory Structure Generator Suite

---

## 🎉 Release Announcement: PR^3-3 (v6.0 R1.0 FINAL LOCK)

**Status:** Code Freeze Active | Predicted Release Ready  
**Date:** 2025-12-17  
**Standard:** Nomenclature v6.0 R1.0 (FINAL LOCK)

### Key Highlights
- ✅ **1,423 files** validated with **0 violations**
- ✅ **v6.0 R1.0** nomenclature standard **finalized and frozen**
- ✅ **8 CI governance gates** operational (3 blocking, 1 review, 4 planned)
- ✅ All allowlists **locked under CM change control**
- ⚠️ 802 broken links identified (post-release hotfix planned)

📖 **[Release Notes](00_AMPEL360_SPACET_Q10_GEN_PLUS_PR_GEN_LC01_K04_CM__pr3-3-release-notes_RPT_I01-R01_RELEASED.md)** | **[Upgrade Guide](00_AMPEL360_SPACET_Q10_GEN_PLUS_PR_GEN_LC01_K04_CM__v6-upgrade-guide_RPT_I01-R01_RELEASED.md)** | **[Known Issues](00_AMPEL360_SPACET_Q10_GEN_PLUS_PR_GEN_LC01_K04_CM__known-issues-pr3-3_LOG_I01-R01_ACTIVE.md)**

---

## Overview

This repository contains the official directory structure generators for AMPEL360 Space-T projects, implementing:

- **OPT-INS Framework Standard v1.1** (6 axes: Organization, Program, Technology, Infrastructures, Neural, SIM/TEST)
- **Nomenclature Standard v6.0 R1.0** (15-token canonical format with frozen allowlists)
- **ATA-SpaceT numbering system** (116 ATA chapters covering aerospace systems, ATA 100–114 reserved for S-axis)
- **14-folder lifecycle structure** (LC01-LC14 with subbuckets SB01-SB99)
- **Knot-based governance** (K01-K14 with strict change control)
- **8 CI governance gates** (3 blocking, 1 review, 4 planned)
- **TEKNIA credential framework** (v1.0 with schema validation)
- **P→CAD→CAE→CAM→CAOS engineering cycle** (AI-assisted workflow)
- **ML Lifecycle** for neural systems (Architecture→Training→Validation→Deployment→Monitoring)
- **CAOS Pillar Enablement** (indeterminacy control via KNOTs, NKU pathways for agentic execution)

### Key Features (v6.0 R1.0)

- ✅ **Zero-tolerance validation** (1,423 files, 0 violations)
- ✅ **Immutable allowlists** (frozen under CM change control)
- ✅ **Quantum-inspired families** (Q10, Q100 pax payload numbering)
- ✅ **Governance lane variants** (GEN, BASELINE, CERT, MSN, CUST, etc.)
- ✅ **Branding version system** (PLUS, PLUSULTRA with optional iteration)
- ✅ **Conditional subject prefixes** (CUST/MSN variants)
- ✅ **Change tracking** (I##-R## issue-revision format)
- ✅ **Automated CI gates** (nomenclature, schemas, trace links)

---

## File Naming Convention (Nomenclature Standard v6.0 R1.0 FINAL LOCK)

**All artifacts in this repository MUST follow the mandatory nomenclature standard.**

### Canonical Format (15 tokens)

```
[ATA_ROOT]_[PROJECT]_[PROGRAM]_[FAMILY]_[VARIANT]_[VERSION]_[MODEL]_[BLOCK]_[PHASE]_[KNOT_TASK]_[AoR]__[SUBJECT]_[TYPE]_[ISSUE-REVISION]_[STATUS].[EXT]
```

### Field Definitions

- **ATA_ROOT**: ATA code (2-3 digits, e.g., `00`, `27`, `115`)
- **PROJECT**: Fixed value `AMPEL360` (immutable)
- **PROGRAM**: Fixed value `SPACET` (immutable)
- **FAMILY**: Quantum-inspired pax payload (e.g., `Q10`, `Q100`)
- **VARIANT**: Governance lane (e.g., `GEN`, `CERT`, `CUST`, `MSN`)
- **VERSION**: Branding reinforcer (e.g., `PLUS`, `PLUS01`, `PLUSULTRA02`)
- **MODEL**: Artifact domain (e.g., `BB`, `HW`, `SW`, `PR`)
- **BLOCK**: Domain partition B## format (e.g., `B10`, `B50`, `B60`) - OPTINS Framework aligned
- **PHASE**: Lifecycle (`LC01-LC14`) or Subbucket (`SB01-SB99`)
- **KNOT_TASK**: Knot ID with optional task (e.g., `K06`, `K06-T001`)
- **AoR**: Area of Responsibility (e.g., `CM`, `CERT`, `SAF`, `SE`)
- **__**: Double underscore separator (mandatory)
- **SUBJECT**: lowercase-kebab-case description
- **TYPE**: Artifact type (e.g., `STD`, `PLAN`, `RPT`, `FHA`)
- **ISSUE-REVISION**: Change tracking (e.g., `I01-R02`, `I12-R03`)
- **STATUS**: Document status (e.g., `ACTIVE`, `APPROVED`, `RELEASED`)
- **EXT**: File extension (lowercase, e.g., `md`, `json`, `yaml`)

### Examples (v6.0 R1.0)

- `27_AMPEL360_SPACET_Q10_GEN_PLUS_BB_B10_LC03_K06_SE__thermal-loop_STD_I01-R02_ACTIVE.md`
- `00_AMPEL360_SPACET_Q10_CERT_PLUS_PR_B00_LC10_K01_CERT__certification-basis_PLAN_I01-R02_ACTIVE.md`
- `95_AMPEL360_SPACET_Q10_GEN_PLUS_SW_B20_SB04_K11_CM__model-card-template_STD_I01-R02_TEMPLATE.md`

### BLOCK Field: Domain Partitions (OPTINS Framework)

The **BLOCK** field uses domain partition identifiers (B00-B90) aligned with the OPTINS Framework v1.1:

| BLOCK   | Domain–Subsystem                         | Environment                      |
| ------- | ---------------------------------------- | -------------------------------- |
| **B00** | GENERAL (universal, implicit)            | **all**                          |
| **B01** | POLICIES (governance, standards, rules)  | **all**                          |
| **B10** | INFRASTRUCTURES AND SPACEPORTS           | **onboard + offboard + simtest** |
| **B20** | ROBOTICS                                 | **onboard + offboard**           |
| **B30** | CYBERSECURITY, DATA, COMMS               | **digital + onboard**            |
| **B40** | PHYSICS (pressure/thermal/cryo)          | **onboard + simtest**            |
| **B50** | PHYSICAL (aerostructures + HW, material) | **onboard + offboard**           |
| **B60** | DYNAMICS (thrust/attitude/inerting)      | **onboard + simtest**            |
| **B70** | LAUNCHERS AND ENGINES                    | **onboard + simtest**            |
| **B80** | RENEWABLE ENERGY & CIRCULARITY           | **onboard + offboard**           |
| **B90** | OPTICS, SENSORING AND OBSERVATION        | **onboard + offboard + simtest** |

**Rationale for B90 environment:** sensors/optics typically have **onboard** operation, **simtest** validation (SIL/HIL, lab scenes), and **offboard** calibration/test assets (benches, metrology, ground stations).

#### Controlled Vocabulary

To keep CI validation deterministic, Environment is constrained to these tokens:

* `onboard` — Onboard systems and components
* `offboard` — Ground-based/external infrastructure
* `simtest` — Simulation and testing environments
* `digital` — Digital/software-only domains
* `all` — Universal applicability (exclusive, cannot combine with others)

**Combination Rules:**
* `all` **cannot** be combined with any other environment token
* Combinations use ` + ` (space-plus-space) as separator
* Combinations should follow canonical order: `digital + onboard + offboard + simtest`

**Note:** Not all BLOCK values are valid for all ATA_ROOT values. See `config/nomenclature/ATA_PARTITION_MATRIX.yaml` for the complete ATA_ROOT to BLOCK mapping.

### Validation

```bash
# Validate a single file (v6.0 R1.0)
python validate_nomenclature.py --standard v6.0 <filename>

# Validate all files in repository (v6.0 R1.0)
python validate_nomenclature.py --standard v6.0 --check-all

# Run comprehensive PR^3-3 verification suite
python scripts/pr3_3_verification.py --all

# Get help
python validate_nomenclature.py --help
```

### Installation of Pre-commit Hook

```bash
# Install the pre-commit hook to validate files before committing
cp scripts/pre-commit .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

📖 **Full standard**: 
- **v6.0 R1.0 (Current)**: `docs/standards/NOMENCLATURE_v6_0_R1_0.md`
- **Quick Reference**: `docs/standards/NOMENCLATURE_v6_0_R1_0_QUICKREF.md`
- **Config**: `config/nomenclature/v6_0.yaml`
- **Glossary**: [`00_AMPEL360_SPACET_Q10_GEN_PLUS_PR_B00_LC01_K04_CM__glossary-acronyms-codes_GLO_I01-R01_ACTIVE.md`](00_AMPEL360_SPACET_Q10_GEN_PLUS_PR_B00_LC01_K04_CM__glossary-acronyms-codes_GLO_I01-R01_ACTIVE.md)

### Document Templates

Use standardized templates to create compliant documentation:

```bash
# Create a new document from template (v6.0 R1.0)
python scripts/scaffold_v6.py --standard v6.0 \
  <ATA_ROOT> <PROJECT> <PROGRAM> <FAMILY> <VARIANT> <VERSION> \
  <MODEL> <BLOCK> <PHASE> <KNOT_TASK> <AOR> <SUBJECT> <TYPE> \
  <ISSUE-REVISION> <STATUS>

# Examples:
python scripts/scaffold_v6.py --standard v6.0 \
  27 AMPEL360 SPACET Q10 GEN PLUS BB OPS LC03 K06 SE \
  thermal-loop STD I01-R02 ACTIVE

python scripts/scaffold_v6.py --standard v6.0 \
  00 AMPEL360 SPACET Q10 CERT PLUS PR GEN LC10 K01 CERT \
  certification-plan PLAN I01-R02 DRAFT
```

📚 **Templates**: [`templates/`](templates/) | **Available**: 22 approved TYPEs

### Automatic TYPE Detection

System automatically detects new TYPE codes and provides extension guidance:

```bash
# Detect new TYPEs in repository
python scripts/detect_new_types.py

# Generate extension guide and template stubs
python scripts/detect_new_types.py --auto-suggest
```

🤖 **Automated**: GitHub Actions runs weekly and on every PR to detect new TYPEs  
📖 **Guide**: [`00_00_IDX_LC01-SPACET_automatic-type-detection_I01-R02.md`](00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_LC01_K04_CM__automatic-type-detection_IDX_I01-R02_ACTIVE.md)

### Certification Knots System

Cross-cutting workflow elements for systematic certification and compliance activities:

```bash
# View active knots
cat 00_90_CAT_SB00_CERT_knots-catalog_I01-R02.json

# Validate knot data structure
python3 -c "
import json, jsonschema
schema = json.load(open('00_90_SCH_SB00_GEN_knots-data-structure_I01-R02.json'))
data = json.load(open('00_90_CAT_SB00_CERT_knots-catalog_I01-R02.json'))
jsonschema.validate(instance=data, schema=schema)
print('✓ Knot data validated successfully')
"
```

**Active Knots:**
- **K01**: Certification Authority Basis - Establishes certification basis and compliance mapping (52 ATA systems across all axes)

📋 **Quick Reference**: [`00_00_CAT_LC10_CERT_knots-quick-reference_I01-R02.md`](00_AMPEL360_SPACET_Q10_CERT_PLUS_BB_GEN_LC10_K01_CERT__knots-quick-reference_CAT_I01-R01_ACTIVE.md)  
📖 **Complete Index**: [`00_00_IDX_LC10_CERT_certification-knots-index_I01-R02.md`](00_AMPEL360_SPACET_Q10_CERT_PLUS_BB_GEN_LC10_K01_CERT__certification-knots-index_IDX_I01-R01_ACTIVE.md)  
📘 **K01 Documentation**: [`00_00_PLAN_LC10_CERT_knot-k01-certification-authority-basis_I01-R02.md`](00_AMPEL360_SPACET_Q10_CERT_PLUS_PR_GEN_LC10_K01_CERT__knot-k01-certification-authority-basis_PLAN_I01-R01_ACTIVE.md)

### ATA Master Relations Table

Complete mapping of all 117 ATA chapters with domain assignments, stakeholder interfaces, and knot applicability:

```bash
# View structured YAML data
cat config/database/ata_master_relations_table.yaml

# View comprehensive catalog documentation
cat 00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_B30_LC01_K06_CM__ata-master-relations-table_CAT_I01-R02_ACTIVE.md

# View quick reference table
cat 00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_B30_LC01_K06_CM__ata-master-relations-quick-ref_TAB_I01-R02_ACTIVE.md
```

**Key Features:**
- **117 ATA chapters** (00-116) with complete relations
- **Domain mappings** to OPTINS Framework axes (P/O/I/T/N/S)
- **AoR assignments** (primary Area of Responsibility for each ATA)
- **STK cross-dependencies** (stakeholder interfaces)
- **Agency/context mappings** (regulatory and operational contexts)
- **Knot applicability** (K01-K14 for each ATA chapter)

📊 **Master Data**: [`config/database/ata_master_relations_table.yaml`](config/database/ata_master_relations_table.yaml)  
📖 **Catalog Documentation**: [`00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_B30_LC01_K06_CM__ata-master-relations-table_CAT_I01-R02_ACTIVE.md`](00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_B30_LC01_K06_CM__ata-master-relations-table_CAT_I01-R02_ACTIVE.md)  
📋 **Quick Reference Table**: [`00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_B30_LC01_K06_CM__ata-master-relations-quick-ref_TAB_I01-R02_ACTIVE.md`](00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_B30_LC01_K06_CM__ata-master-relations-quick-ref_TAB_I01-R02_ACTIVE.md)

---

## Quick Start

### Generate Complete Structure (All Axes)

```bash
# Generate T-TECHNOLOGY (Vehicle Systems)
python generate_space_t_structure.py

# Generate O-ORGANIZATION (Governance)
python generate_organization.py

# Generate P-PROGRAM (Program Management)
python generate_program.py

# Generate I-INFRASTRUCTURES (Ground Systems)
python generate_infrastructures.py
```

### Generate Specific Systems

```bash
# T-TECHNOLOGY: ECLSS, GNC, Structure, Neural
python generate_space_t_structure.py --systems 21,22,53,95

# O-ORGANIZATION: General, CM, QMS, SMS
python generate_organization.py --systems 00,06,07,08

# P-PROGRAM: Planning, Cost, Risk, Reviews
python generate_program.py --systems 06,07,08,09

# I-INFRASTRUCTURES: H2, Launch, MCC
python generate_infrastructures.py --systems 85,86,89
```

### Custom Root Directory

```bash
python generate_space_t_structure.py --root ./my_project
python generate_organization.py --root ./my_project
python generate_program.py --root ./my_project
python generate_infrastructures.py --root ./my_project
```

---


| ATA | DESCR | DOMAIN | AoR (portal entry points and main owner) | STKs (AoR cross dependancies) | AGENCY/CONTEXT (EG TECH_PROP, ESG, QA...) | Note |
|---:|---|---|---|---|---|---|
| 00 | GENERAL | P-PROGRAM | STK_CM | STK_PMO,STK_SE,STK_SAF,STK_CERT,STK_DAB | PROG_GOV,CM,PMO,DATA_GOV,AUDIT | Program governance baseline (nomenclature, CC, registers). Knots: K01,K04,K06,K10. |
| 01 | OPERATIONS/ORGANIZATION POLICY (RESERVED) | O-OPS/ORG | STK_OPS | STK_SAF,STK_CERT,STK_CM,STK_SPACEPORT | OPS_GOV,CONOPS,TRAINING,READINESS | Ops policy/governance. Knots: K01,K02,K11. |
| 02 | OPERATIONS/ORGANIZATION (RESERVED) | O-OPS/ORG | STK_OPS | STK_SAF,STK_CERT,STK_CM,STK_SPACEPORT | OPS_GOV,CONOPS,READINESS | Ops organization + readiness. Knots: K01,K02,K11. |
| 03 | SUPPORT INFORMATION (RESERVED) | O-OPS/ORG | STK_OPS | STK_SAF,STK_CERT,STK_CM,STK_SPACEPORT | TECHPUBS,OPS_SUPPORT | Support info (procedures/reporting). Knots: K01,K02,K11. |
| 04 | AIRWORTHINESS LIMITATIONS / OPERATIONAL LIMITS (RESERVED) | O-OPS/ORG | STK_OPS | STK_SAF,STK_CERT,STK_CM,STK_SPACEPORT | OPS_LIMITS,SAFETY_LIMITS | Operational limits baseline. Knots: K01,K02,K11. |
| 05 | TIME LIMITS / MAINTENANCE CHECKS | O-OPS/ORG | STK_MRO | STK_CM,STK_OPS,STK_SAF,STK_CERT,STK_DAB | MRO_PLANS,MSG3_LIKE | Time limits, checks, intervals, escalations. Knots: K01,K04,K05,K11. |
| 06 | DIMENSIONS AND AREAS | T-TECHNOLOGY | STK_PHM | STK_SE,STK_CERT,STK_TEST,STK_DAB | GEOMETRY,AREAS,MASS_PROP | Reference geometry, areas, envelopes for downstream validation. Knots: K01,K05,K06. |
| 07 | LIFTING AND SHORING | I-INFRASTRUCTURES | STK_MRO | STK_PHM,STK_SAF,STK_OPS,STK_CERT | GSE,LIFTING,SAFETY | Ground lifting/jacking/shoring requirements & procedures. Knots: K02,K03,K05,K11. |
| 08 | LEVELING AND WEIGHING | T-TECHNOLOGY | STK_PHM | STK_OPS,STK_MRO,STK_TEST,STK_DAB | WEIGHING,CENTER_OF_GRAVITY | Mass properties measurement + leveling methods. Knots: K01,K05,K06,K11. |
| 09 | TOWING AND TAXIING | I-INFRASTRUCTURES | STK_OPS | STK_MRO,STK_SAF,STK_SPACEPORT | GROUND_OPS,TOWING | Tow/taxi ground ops constraints + procedures. Knots: K02,K03,K11. |
| 10 | PARKING / MOORING / STORAGE / RETURN TO SERVICE | I-INFRASTRUCTURES | STK_OPS | STK_MRO,STK_SAF,STK_SPACEPORT,STK_CM | STORAGE,RTS_PROCEDURES | Parking/mooring/storage + RTS checks. Knots: K02,K04,K11. |
| 11 | PLACARDS AND MARKINGS | P-PROGRAM | STK_OPS | STK_MRO,STK_SAF,STK_CERT,STK_CM | OPS_LABELS,HFE,TECHPUBS | Labels/markings governance. Knots: K01,K11. |
| 12 | SERVICING | I-INFRASTRUCTURES | STK_MRO | STK_OPS,STK_SAF,STK_SPACEPORT,STK_CERT | SERVICING,FLUIDS,CRYO | Servicing procedures (fluids/consumables/cryo/prop). Knots: K02,K03,K09,K11. |
| 13 | NOT ASSIGNED / RESERVED | Not Assigned | STK_CM | STK_SE,STK_CERT | TAXONOMY,CM | Reserved (Space-T tailoring). Knots: K01,K04. |
| 14 | NOT ASSIGNED / RESERVED | Not Assigned | STK_CM | STK_SE,STK_CERT | TAXONOMY,CM | Reserved (Space-T tailoring). Knots: K01,K04. |
| 15 | NOT ASSIGNED / RESERVED | Not Assigned | STK_CM | STK_SE,STK_CERT | TAXONOMY,CM | Reserved (Space-T tailoring). Knots: K01,K04. |
| 16 | NOT ASSIGNED / RESERVED | Not Assigned | STK_CM | STK_SE,STK_CERT | TAXONOMY,CM | Reserved (Space-T tailoring). Knots: K01,K04. |
| 17 | NOT ASSIGNED / RESERVED | Not Assigned | STK_CM | STK_SE,STK_CERT | TAXONOMY,CM | Reserved (Space-T tailoring). Knots: K01,K04. |
| 18 | NOISE & VIBRATION MANAGEMENT | O-OPS/ORG | STK_SAF | STK_OPS,STK_CERT,STK_TEST,STK_SE,STK_PHM,STK_SPACEPORT | NVH,ENV,MONITORING | NVH constraints/monitoring/mitigation. Knots: K01,K05,K12. |
| 19 | NOT ASSIGNED / RESERVED | Not Assigned | STK_CM | STK_SE,STK_CERT | TAXONOMY,CM | Reserved (Space-T tailoring). Knots: K01,K04. |
| 20 | STANDARD PRACTICES - AIRFRAME | T-TECHNOLOGY | STK_PHM | STK_SE,STK_SAF,STK_CERT,STK_TEST,STK_DAB | PRACTICES,FASTENERS,REPAIRS | Airframe standard practices, materials, repair methods. Knots: K01,K05,K10. |
| 21 | AIR CONDITIONING / ENVIRONMENTAL CONTROL | T-TECHNOLOGY | STK_PHM | STK_SE,STK_SAF,STK_CERT,STK_TEST,STK_DAB | ECLSS,ECS,THERMAL | ECLSS/ECS physical plant + controls. Knots: K01,K03,K05,K06. |
| 22 | AUTO FLIGHT / GUIDANCE-NAVIGATION-CONTROL | T-TECHNOLOGY | STK_DAB | STK_SE,STK_AI,STK_SAF,STK_CERT,STK_TEST,STK_OPS,STK_CY,STK_PHM | GNC,AUTONOMY,FDIR | GNC SW/control-law implementation; SE governs architecture. Knots: K01,K05,K07,K13. |
| 23 | COMMUNICATIONS | T-TECHNOLOGY | STK_DAB | STK_SE,STK_CY,STK_OPS,STK_CERT,STK_TEST,STK_SPACEPORT | COMMS,TT&C,LINK_BUDGET | Comms/TT&C stacks + ICDs + link security. Knots: K01,K05,K09,K13. |
| 24 | ELECTRICAL POWER | T-TECHNOLOGY | STK_PHM | STK_SE,STK_SAF,STK_CERT,STK_TEST,STK_MRO,STK_DAB | EPOWER,HVDC,EMC | Power generation/distribution/protection + monitoring SW. Knots: K01,K03,K05. |
| 25 | EQUIPMENT / FURNISHINGS | T-TECHNOLOGY | STK_PHM | STK_OPS,STK_SAF,STK_CERT,STK_MRO,STK_SE | HFE,CABIN,SAFETY_EQUIP | Interiors/equipment/ergonomics + maintainability. Knots: K01,K10,K11. |
| 26 | FIRE PROTECTION | T-TECHNOLOGY | STK_SAF | STK_PHM,STK_SE,STK_DAB,STK_CERT,STK_OPS,STK_TEST | FIRE_SAFETY,HAZARDS | Detection/suppression, hazard zoning, flammability. Knots: K01,K03,K05. |
| 27 | FLIGHT CONTROLS | T-TECHNOLOGY | STK_PHM | STK_SE,STK_DAB,STK_SAF,STK_CERT,STK_TEST,STK_CY | ACTUATION,REDUNDANCY | Actuation/servos/surfaces; SW control under DAB. Knots: K01,K05,K07. |
| 28 | FUEL / PROPELLANT SYSTEMS | T-TECHNOLOGY | STK_PHM | STK_SE,STK_SAF,STK_CERT,STK_OPS,STK_SPACEPORT,STK_TEST,STK_DAB | TECH_PROP,HAZARDS | Tanks/feeds/venting/leak; spaceport servicing ICDs. Knots: K01,K03,K05,K09. |
| 29 | HYDRAULIC POWER | T-TECHNOLOGY | STK_PHM | STK_SE,STK_SAF,STK_CERT,STK_TEST,STK_MRO,STK_DAB | HYDRAULICS,ACTUATION | Hydraulic generation/distribution/health monitoring. Knots: K01,K05,K11. |
| 30 | ICE AND RAIN PROTECTION / ATMOSPHERIC PROTECTION | T-TECHNOLOGY | STK_PHM | STK_SE,STK_SAF,STK_CERT,STK_TEST,STK_DAB | ENV_PROTECTION,THERMAL | Atmospheric protection (air) or env protection features (space). Knots: K01,K03,K05. |
| 31 | INDICATING / RECORDING SYSTEMS | T-TECHNOLOGY | STK_DAB | STK_SE,STK_CY,STK_CERT,STK_TEST,STK_OPS | DISPLAYS,LOGGING,RECORDERS | Indication/recording SW + data logging governance. Knots: K01,K06,K13. |
| 32 | LANDING GEAR | T-TECHNOLOGY | STK_PHM | STK_SE,STK_SAF,STK_CERT,STK_TEST,STK_OPS,STK_MRO,STK_DAB | GEAR,LOADS,KINEMATICS | Gear/brakes/steering + deployment logic interfaces. Knots: K01,K05,K11. |
| 33 | LIGHTS | T-TECHNOLOGY | STK_DAB | STK_PHM,STK_SE,STK_OPS,STK_SAF,STK_CERT,STK_SPACEPORT,STK_DAB | LIGHTS,SIGNALING | Lighting control SW + HW integration. Knots: K01,K05. |
| 34 | NAVIGATION | T-TECHNOLOGY | STK_DAB | STK_SE,STK_CY,STK_OPS,STK_CERT,STK_TEST,STK_DAB,STK_AI | NAV,SENSOR_FUSION | Nav sensors fusion + integrity + cyber resilience. Knots: K01,K05,K13. |
| 35 | OXYGEN / LIFE SUPPORT GAS | T-TECHNOLOGY | STK_PHM | STK_OPS,STK_SAF,STK_SE,STK_CERT,STK_MRO,STK_DAB | LS_GAS,EMERGENCY | Breathing gas storage/distribution + emergency procedures. Knots: K01,K03,K11. |
| 36 | PNEUMATIC / GAS DISTRIBUTION | T-TECHNOLOGY | STK_PHM | STK_SE,STK_SAF,STK_CERT,STK_TEST,STK_MRO,STK_DAB | PNEUMATICS,GAS_NETS | Pneumatics/gas distribution, valves, sensors, alarms. Knots: K01,K03,K05. |
| 37 | VACUUM (IF APPLICABLE) | T-TECHNOLOGY | STK_PHM | STK_SE,STK_SAF,STK_CERT,STK_TEST,STK_MRO | VACUUM_SYSTEMS | Vacuum systems where applicable. Knots: K01,K03,K05. |
| 38 | WATER / WASTE (LIFE SUPPORT) | T-TECHNOLOGY | STK_PHM | STK_OPS,STK_SAF,STK_SE,STK_CERT,STK_TEST,STK_DAB | WATER_WASTE,CONTAMINATION | Water/waste loops + hygiene + contamination controls. Knots: K01,K03,K11. |
| 39 | ELECTRICAL / ELECTRONIC PANELS & MULTIPURPOSE COMPONENTS | T-TECHNOLOGY | STK_PHM | STK_SE,STK_CY,STK_CERT,STK_TEST,STK_MRO,STK_DAB | PANELS,LRU_RACKS | Panels/racks/enclosures, harness interfaces, maintainability. Knots: K01,K05,K13. |
| 40 | MULTI-SYSTEM / INTEGRATION SERVICES | T-TECHNOLOGY | STK_SE | STK_CM,STK_CERT,STK_TEST,STK_DAB,STK_CY,STK_PHM | INTEGRATION,ICDS,MBSE | Cross-system integration services + ICD governance. Knots: K01,K04,K06,K10. |
| 41 | WATER BALLAST / MASS TRIM (IF APPLICABLE) | T-TECHNOLOGY | STK_PHM | STK_SE,STK_SAF,STK_TEST,STK_DAB | MASS_TRIM,BALLAST | Ballast/mass trim where applicable. Knots: K01,K05,K06. |
| 42 | INTEGRATED MODULAR AVIONICS / COMPUTE PLATFORM | T-TECHNOLOGY | STK_DAB | STK_CY,STK_SE,STK_SAF,STK_CERT,STK_DAB,STK_TEST,STK_AI | IMA,COMPUTE,PLATFORM | Compute platform SW/toolchains; cyber & partitioning. Knots: K01,K05,K13. |
| 43 | RESERVED / PLATFORM INTEGRATION | T-TECHNOLOGY | STK_CM | STK_SE,STK_CERT,STK_DAB | PLATFORM_POLICY | Reserved platform integration governance. Knots: K01,K04. |
| 44 | CABIN / HABITAT SYSTEMS | T-TECHNOLOGY | STK_OPS | STK_SAF,STK_CERT,STK_SE,STK_PHM,STK_DAB | HABITAT,SERVICES,HFE | Passenger/crew services + ops training integration. Knots: K01,K02,K11. |
| 45 | CENTRAL MAINTENANCE SYSTEM / HEALTH MONITORING | T-TECHNOLOGY | STK_DAB | STK_DAB,STK_MRO,STK_SE,STK_CY,STK_CERT,STK_TEST | PHM_HEALTH,LOGS,DIAG | Health monitoring, diagnostics, maintenance data pipelines. Knots: K01,K06,K11,K13. |
| 46 | INFORMATION SYSTEMS / DATA NETWORKS | T-TECHNOLOGY | STK_DAB | STK_CY,STK_DAB,STK_SE,STK_CERT,STK_TEST,STK_OPS | DATA_NETWORKS,AVIONICS_NETS | Onboard networks + data services; cyber-required. Knots: K01,K06,K13. |
| 47 | INERT GAS SYSTEM / TANK INERTING | T-TECHNOLOGY | STK_SAF | STK_PHM,STK_SE,STK_OPS,STK_CERT,STK_TEST,STK_DAB | INERTING,HAZARDS | Inerting safety system + procedures + validation. Knots: K01,K03,K05. |
| 48 | IN-FLIGHT FUEL DISPENSING (RESERVED) | T-TECHNOLOGY | STK_CM | STK_SE,STK_SAF,STK_CERT,STK_DAB,STK_PHM | APPLICABILITY | Reserved; activate only if applicable. Knots: K01,K04. |
| 49 | AIRBORNE AUXILIARY POWER / APU / AUX POWER MODULES | T-TECHNOLOGY | STK_PHM | STK_SE,STK_SAF,STK_CERT,STK_TEST,STK_MRO,STK_DAB | AUX_POWER,START,SAFETY | Auxiliary power modules (as applicable). Knots: K01,K03,K05. |
| 50 | CARGO AND ACCESSORY COMPARTMENTS | T-TECHNOLOGY | STK_PHM | STK_SE,STK_SAF,STK_CERT,STK_TEST,STK_MRO | CARGO,COMPARTMENTS | Compartments/structure/access/inspection. Knots: K01,K05,K11. |
| 51 | STANDARD PRACTICES & STRUCTURES - GENERAL | T-TECHNOLOGY | STK_PHM | STK_SE,STK_SAF,STK_CERT,STK_TEST,STK_DAB | STRUCT_PRACTICES,MATERIALS | Structural practices, allowables, methods. Knots: K01,K05,K10. |
| 52 | DOORS / HATCHES | T-TECHNOLOGY | STK_PHM | STK_SE,STK_SAF,STK_CERT,STK_OPS,STK_TEST,STK_MRO,STK_DAB | DOORS,EGRESS | Doors/hatches/seals/actuation; egress compliance. Knots: K01,K05,K11. |
| 53 | FUSELAGE / PRESSURE VESSEL | T-TECHNOLOGY | STK_PHM | STK_SE,STK_SAF,STK_CERT,STK_TEST,STK_DAB | PRESSURE_VESSEL,LOADS | Primary structure / pressure vessel (Space-T). Knots: K01,K05,K10. |
| 54 | NACELLES / PYLONS (IF APPLICABLE) | T-TECHNOLOGY | STK_PHM | STK_SE,STK_SAF,STK_CERT,STK_TEST | NACELLES,PYLONS | Nacelles/pylons and integration structures. Knots: K01,K05,K10. |
| 55 | STABILIZERS / CONTROL SURFACES | T-TECHNOLOGY | STK_PHM | STK_SE,STK_SAF,STK_CERT,STK_TEST,STK_DAB | CONTROL_SURFACES | Control surfaces mechanisms, loads, actuation interfaces. Knots: K01,K05,K07. |
| 56 | WINDOWS / VIEWPORTS | T-TECHNOLOGY | STK_PHM | STK_SE,STK_SAF,STK_CERT,STK_OPS,STK_MRO,STK_TEST | VIEWPORTS,DEBRIS | Viewports/windows, debris protection, inspection. Knots: K01,K05,K11. |
| 57 | WINGS / LIFTING SURFACES | T-TECHNOLOGY | STK_PHM | STK_SE,STK_SAF,STK_CERT,STK_TEST,STK_DAB | LIFT_SURFACES,AEROELASTIC | Lifting surfaces / lifting body structures. Knots: K01,K05,K10. |
| 58 | RESERVED / EXTENSION | T-TECHNOLOGY | STK_CM | STK_SE,STK_CERT | TAXONOMY | Reserved extension. Knots: K01,K04. |
| 59 | RESERVED / EXTENSION | T-TECHNOLOGY | STK_CM | STK_SE,STK_CERT | TAXONOMY | Reserved extension. Knots: K01,K04. |
| 60 | STANDARD PRACTICES - PROPELLER / ROTOR | T-TECHNOLOGY | STK_PHM | STK_SE,STK_CERT,STK_TEST | PROP_ROTOR_PRACTICES | Prop/rotor practices (if applicable). Knots: K01,K05,K10. |
| 61 | PROPELLERS / PROPULSORS (IF APPLICABLE) | T-TECHNOLOGY | STK_PHM | STK_SE,STK_SAF,STK_CERT,STK_TEST | PROPULSORS | Propulsors hardware (if applicable). Knots: K01,K05,K10. |
| 62 | ROTORS (IF APPLICABLE) | T-TECHNOLOGY | STK_PHM | STK_SE,STK_CERT,STK_TEST | ROTORS | Rotors (if applicable). Knots: K01,K05. |
| 63 | ROTOR DRIVES (IF APPLICABLE) | T-TECHNOLOGY | STK_PHM | STK_SE,STK_CERT,STK_TEST | ROTOR_DRIVES | Rotor drive trains (if applicable). Knots: K01,K05. |
| 64 | TAIL ROTOR (IF APPLICABLE) | T-TECHNOLOGY | STK_PHM | STK_SE,STK_CERT,STK_TEST | TAIL_ROTOR | Tail rotor (if applicable). Knots: K01,K05. |
| 65 | TAIL ROTOR DRIVE (IF APPLICABLE) | T-TECHNOLOGY | STK_PHM | STK_SE,STK_CERT,STK_TEST | TAIL_ROTOR_DRIVE | Tail rotor drive (if applicable). Knots: K01,K05. |
| 66 | FOLDING BLADES / TAIL PYLON (IF APPLICABLE) | T-TECHNOLOGY | STK_PHM | STK_SE,STK_CERT,STK_TEST | FOLDING_MECH | Folding mechanisms (if applicable). Knots: K01,K05. |
| 67 | ROTORS FLIGHT CONTROL (IF APPLICABLE) | T-TECHNOLOGY | STK_PHM | STK_SE,STK_DAB,STK_CERT,STK_TEST | ROTOR_CONTROL | Rotor control interfaces and VV (if applicable). Knots: K01,K05,K07. |
| 68 | RESERVED / EXTENSION | T-TECHNOLOGY | STK_CM | STK_SE,STK_CERT | TAXONOMY | Reserved extension. Knots: K01,K04. |
| 69 | RESERVED / EXTENSION | T-TECHNOLOGY | STK_CM | STK_SE,STK_CERT | TAXONOMY | Reserved extension. Knots: K01,K04. |
| 70 | STANDARD PRACTICES - ENGINE | T-TECHNOLOGY | STK_PHM | STK_SE,STK_SAF,STK_CERT,STK_TEST | ENGINE_PRACTICES | Engine/propulsion practices, methods, inspections. Knots: K01,K05,K10. |
| 71 | POWER PLANT / PROPULSION INTEGRATION | T-TECHNOLOGY | STK_SE | STK_PHM,STK_DAB,STK_SAF,STK_CERT,STK_TEST,STK_SPACEPORT | PROP_INTEGRATION,ICDS | Propulsion integration architecture + ICD governance. Knots: K01,K04,K05,K09. |
| 72 | ENGINE (TURBINE/ROCKET/HYBRID AS APPLICABLE) | T-TECHNOLOGY | STK_PHM | STK_SE,STK_SAF,STK_CERT,STK_TEST,STK_SPACEPORT,STK_DAB | TECH_PROP,QUAL_TESTS | Propulsion unit hardware + integration constraints. Knots: K01,K03,K05,K09. |
| 73 | ENGINE FUEL AND CONTROL | T-TECHNOLOGY | STK_DAB | STK_PHM,STK_SE,STK_CY,STK_SAF,STK_CERT,STK_TEST,STK_DAB | FADEC_LIKE,CYSEC | Propulsion control SW + safety/cyber evidence. Knots: K01,K05,K13. |
| 74 | IGNITION | T-TECHNOLOGY | STK_PHM | STK_SE,STK_SAF,STK_CERT,STK_TEST,STK_DAB | IGNITION,INTERLOCKS | Ignition hardware + interlocks + validation. Knots: K01,K03,K05. |
| 75 | AIR (BLEED / INLET / APU AIR) / INTAKE | T-TECHNOLOGY | STK_PHM | STK_SE,STK_SAF,STK_CERT,STK_TEST | INTAKES,FLOW_PATHS | Intake/bleed/flow paths (as applicable). Knots: K01,K03,K05. |
| 76 | ENGINE CONTROLS | T-TECHNOLOGY | STK_DAB | STK_PHM,STK_SE,STK_CY,STK_CERT,STK_TEST,STK_DAB | CONTROL_INTEGRATION | Integrated propulsion control SW (ICDs + VV). Knots: K01,K05,K13. |
| 77 | ENGINE INDICATING | T-TECHNOLOGY | STK_DAB | STK_PHM,STK_SE,STK_CERT,STK_TEST,STK_DAB | ENGINE_INDICATION | Indication/recording for propulsion. Knots: K01,K05,K06. |
| 78 | EXHAUST / PLUME MANAGEMENT | T-TECHNOLOGY | STK_PHM | STK_SE,STK_SAF,STK_CERT,STK_TEST,STK_SPACEPORT | PLUME,THERMAL,SAFETY | Exhaust/plume/thermal interactions + constraints. Knots: K01,K03,K05,K09. |
| 79 | OIL / LUBRICATION | T-TECHNOLOGY | STK_PHM | STK_SE,STK_SAF,STK_CERT,STK_TEST,STK_MRO | LUBE,OIL_SYSTEMS | Lubrication systems + servicing/inspection. Knots: K01,K03,K11. |
| 80 | OFF-BOARD / AIRPORT / SPACEPORT INFRASTRUCTURES (MASTER) | I-INFRASTRUCTURES | STK_SPACEPORT | STK_OPS,STK_SAF,STK_CERT,STK_CM,STK_DAB | SPACEPORT_MASTER | Master off-board infra baseline (Spaceport/Airport). Knots: K01,K02,K09,K10. |
| 81 | OFF-BOARD ENERGY / CRYO SERVICES | I-INFRASTRUCTURES | STK_SPACEPORT | STK_SAF,STK_OPS,STK_CERT,STK_PHM,STK_MRO | CRYO,ENERGY_SERVICES | Energy/cryo services & interfaces. Knots: K02,K03,K09. |
| 82 | OFF-BOARD MRO FACILITIES / TOOLING / LOGISTICS | I-INFRASTRUCTURES | STK_MRO | STK_OPS,STK_SAF,STK_CM,STK_DAB | MRO_FACILITIES,TOOLING | MRO facilities/tooling/logistics baselines. Knots: K02,K04,K11. |
| 83 | GROUND COMMS / DATA EXCHANGE INFRA (GATEWAYS, EDGE) | I-INFRASTRUCTURES | STK_DAB | STK_CY,STK_OPS,STK_SPACEPORT,STK_CERT,STK_TEST | GATEWAYS,EDGE,DATA_EXCHANGE | Ground gateways/edge data exchange; cyber-required. Knots: K02,K06,K09,K13. |
| 84 | SPACEPORT SAFETY / EMERGENCY RESPONSE INFRA | I-INFRASTRUCTURES | STK_SAF | STK_SPACEPORT,STK_OPS,STK_CERT,STK_TEST | EMERGENCY_RESPONSE | Safety infra & emergency response baselines. Knots: K02,K03,K09,K10. |
| 85 | CIRCULARITY INFRA (RETURN FLOWS, RECYCLING, CO2/H2 LOOPS) | I-INFRASTRUCTURES | STK_DAB | STK_PMO,STK_CM,STK_OPS,STK_SPACEPORT | CIRCULARITY,LEDGERS | Circularity infra + trace/ledger hooks. Knots: K01,K06,K14. |
| 86 | OFF-BOARD DIGITAL SERVICES PLATFORM (PORTALS, ORCHESTRATION) | I-INFRASTRUCTURES | STK_DAB | STK_CY,STK_OPS,STK_CM,STK_TEST,STK_DAB | PORTALS,ORCHESTRATION | CAXS portals/orchestration services. Knots: K01,K06,K13. |
| 87 | IDENTITY / ACCESS / CYBERSECURITY INFRA (PHYSICAL+DIGITAL) | I-INFRASTRUCTURES | STK_CY | STK_DAB,STK_CM,STK_CERT,STK_OPS | IAM,ZTA,SECOPS | Identity/access/cyber infra. Knots: K01,K06,K13. |
| 88 | GSE CONFIGURATION / ASSET MANAGEMENT | I-INFRASTRUCTURES | STK_CM | STK_MRO,STK_DAB,STK_OPS,STK_CERT | ASSET_MGMT,CONFIG | GSE asset mgmt + configuration baselines. Knots: K01,K04,K06. |
| 89 | TEST RIGS / INSTRUMENTATION INFRA (GROUND) | I-INFRASTRUCTURES | STK_TEST | STK_SPACEPORT,STK_PHM,STK_DAB,STK_CERT | TEST_RIGS,INSTRUMENTATION | Ground rigs/instrumentation infra. Knots: K01,K05,K09. |
| 90 | AI/ML MODEL REGISTRY & MODEL LIFECYCLE | N-NEURAL_NETWORKS | STK_AI | STK_DAB,STK_CM,STK_CERT,STK_OPS,STK_CY,STK_TEST | MODEL_REGISTRY,GOV | Model registry + lifecycle governance. Knots: K01,K06,K07. |
| 91 | DATA SCHEMAS / ONTOLOGIES / SEMANTIC MODEL (SSOT) | N-NEURAL_NETWORKS | STK_DAB | STK_CM,STK_SE,STK_CY,STK_CERT,STK_TEST | ONTOLOGIES,SSOT | Ontologies/SSOT for validation and trace. Knots: K01,K06,K13. |
| 92 | WIRING / CONNECTIVITY GRAPHS & HARNESS DATA PACKAGES | N-NEURAL_NETWORKS | STK_DAB | STK_PHM,STK_SE,STK_CM,STK_CERT,STK_TEST | CONNECTIVITY,GRAPH | Connectivity graphs/harness datasets. Knots: K01,K06,K05. |
| 93 | TRACEABILITY GRAPH (REQ↔DESIGN↔VV↔OPS) & EVIDENCE LEDGERS | N-NEURAL_NETWORKS | STK_CM | STK_DAB,STK_SE,STK_CERT,STK_TEST,STK_AI | TRACEABILITY,EVIDENCE_LEDGER | Trace graph + evidence ledgers for audits/releases. Knots: K01,K06,K08. |
| 94 | DPP CORE (DIGITAL PRODUCT PASSPORT) & PROVENANCE | N-NEURAL_NETWORKS | STK_DAB | STK_CM,STK_CERT,STK_CY,STK_OPS | DPP,PROVENANCE | DPP core + provenance/export views. Knots: K01,K06,K13,K14. |
| 95 | SBOM / SWHW BOM / MODEL BOM EXPORTS | N-NEURAL_NETWORKS | STK_DAB | STK_CY,STK_CM,STK_CERT,STK_DAB | SBOM,BOM_EXPORTS | SBOM/SW/HW BOM exports + signing hooks. Knots: K01,K06,K13. |
| 96 | AI GOVERNANCE (RISK, ASSURANCE, MONITORING, DRIFT/BIAS) | N-NEURAL_NETWORKS | STK_AI | STK_SAF,STK_CERT,STK_OPS,STK_CY,STK_DAB,STK_CM | AI_RISK,ASSURANCE | AI governance, monitors, approvals, rollback. Knots: K01,K07,K13. |
| 97 | CHANGE IMPACT ANALYTICS (WIRING/CONFIG/TRACE) | N-NEURAL_NETWORKS | STK_DAB | STK_CM,STK_SE,STK_CERT,STK_TEST | IMPACT_ANALYTICS | Change impact analytics across config/trace/connectivity. Knots: K01,K04,K06. |
| 98 | SIGNED RELEASE PACKS / MANIFESTS / EXPORTS | N-NEURAL_NETWORKS | STK_CM | STK_CERT,STK_DAB,STK_CY,STK_OPS | SIGNING,MANIFESTS,EXPORTS | Signed releases/manifests/exports (PR-blocking). Knots: K01,K04,K08,K13. |
| 99 | MASTER REGISTERS (GOLDEN RECORDS) & REFERENCE DATASETS | N-NEURAL_NETWORKS | STK_DAB | STK_CM,STK_SE,STK_CERT,STK_TEST | MASTER_DATA,REGISTERS | Golden registers + reference datasets. Knots: K01,K06. |
| 100 | SIM/TEST GOVERNANCE (PLANS, ENVIRONMENTS, QUALITY) | T-SIMTEST | STK_TEST | STK_CERT,STK_CM,STK_DAB,STK_SE | SIMTEST_GOV,TOOL_QUAL | Test governance, environments, tool qualification. Knots: K01,K05. |
| 101 | DIGITAL TWIN CONFIGURATION & SIM MODEL CATALOG | T-SIMTEST | STK_DAB | STK_TEST,STK_SE,STK_CM,STK_CERT | DIGITAL_TWIN,CATALOG | Digital twin config + model catalog. Knots: K01,K06,K05. |
| 102 | SCENARIO LIBRARIES (MISSION, OFF-NOMINAL, EMERGENCY) | T-SIMTEST | STK_OPS | STK_TEST,STK_SAF,STK_SE,STK_DAB | SCENARIOS,CONOPS | Scenario libraries for mission/off-nominal/emergency. Knots: K01,K02,K05. |
| 103 | SIL (SOFTWARE-IN-THE-LOOP) AUTOMATION | T-SIMTEST | STK_DAB | STK_TEST,STK_CY,STK_DAB,STK_SE | SIL,AUTOMATION | SIL harnesses, runners, automation, logs. Knots: K01,K05,K13. |
| 104 | HIL (HARDWARE-IN-THE-LOOP) BENCHES | T-SIMTEST | STK_TEST | STK_PHM,STK_DAB,STK_SE,STK_CERT | HIL,BENCHES | HIL benches + instrumentation + procedures. Knots: K01,K05. |
| 105 | PIL / TARGET EXECUTION (PROCESSOR/PLATFORM-IN-THE-LOOP) | T-SIMTEST | STK_TEST | STK_SE,STK_CM,STK_CERT,STK_CY,STK_DAB,STK_PHM | PIL,TARGET,PERF_TIMING | Target execution evidence (timing/mem constraints). Knots: K01,K05,K13. |
| 106 | TEST PROCEDURES / TEST CASES / ACCEPTANCE CRITERIA | T-SIMTEST | STK_TEST | STK_SE,STK_SAF,STK_CERT,STK_CM,STK_DAB | TEST_CASES,ACCEPTANCE | Procedures/cases/criteria + trace links. Knots: K01,K06. |
| 107 | TEST DATA / INPUT DECKS / STIMULI | T-SIMTEST | STK_DAB | STK_TEST,STK_SE,STK_CM | TEST_DATA,STIMULI | Controlled test datasets/input decks/stimuli. Knots: K01,K06. |
| 108 | TEST RESULTS / REPORTING / ANOMALY MANAGEMENT | T-SIMTEST | STK_TEST | STK_DAB,STK_OPS,STK_SAF,STK_CERT,STK_CM | RESULTS,NCR,ANOMALIES | Results reporting + anomaly/NCR management. Knots: K01,K05,K08. |
| 109 | VV EVIDENCE PACKS (LINKED TO TRACEABILITY) | T-SIMTEST | STK_CERT | STK_CM,STK_TEST,STK_DAB,STK_SE | VV_EVIDENCE,PACKAGING | Evidence bundling linked to trace graph. Knots: K01,K06,K08. |
| 110 | QUALIFICATION / ENVIRONMENTAL TESTING (SPACE-T) | T-SIMTEST | STK_TEST | STK_SAF,STK_CERT,STK_SPACEPORT,STK_CM,STK_SE,STK_PHM,STK_DAB | THERMAL_VAC,VIB,EMC | Space-T qual tests + facility constraints. Knots: K01,K05,K09. |
| 111 | SYSTEM INTEGRATION TESTING (END-TO-END) | T-SIMTEST | STK_TEST | STK_SE,STK_SAF,STK_CERT,STK_DAB,STK_CY | E2E_INTEGRATION | End-to-end integration testing across subsystems. Knots: K01,K05,K13. |
| 112 | MISSION/FLIGHT TESTING (OPERATIONAL DEMOS) | T-SIMTEST | STK_OPS | STK_TEST,STK_SAF,STK_CERT,STK_CM,STK_SPACEPORT,STK_SE,STK_DAB,STK_PHM | OPS_DEMOS,READINESS | Operational demos + readiness + limits confirmation. Knots: K01,K02,K11,K12. |
| 113 | UNCERTAINTY QUANTIFICATION (UQ) / MONTE CARLO / SENSITIVITY | T-SIMTEST | STK_DAB | STK_TEST,STK_SE,STK_AI | UQ,MONTE_CARLO | UQ/Monte Carlo/sensitivity suites. Knots: K01,K05,K06. |
| 114 | AI/ML VALIDATION SUITES & MONITORING TESTS | T-SIMTEST | STK_AI | STK_TEST,STK_SAF,STK_CERT,STK_OPS,STK_CY,STK_DAB | AI_VALIDATION,DRIFT | AI validation/robustness/drift suites. Knots: K01,K05,K07,K13. |
| 115 | CERTIFICATION TESTS (SW/HW/ECSS-DO) & COMPLIANCE REPORTS | T-SIMTEST | STK_CERT | STK_TEST,STK_CM,STK_SE,STK_DAB,STK_SAF,STK_CY,STK_PHM | COMPLIANCE,AUDIT | Compliance tests + reports + authority packs. Knots: K01,K05,K10,K13. |
| 116 | SIM/TEST ARCHIVES & BASELINES (FROZEN CAMPAIGNS) | T-SIMTEST | STK_CM | STK_TEST,STK_DAB,STK_CERT | ARCHIVES,BASELINES | Frozen campaigns, baselines, retention policy. Knots: K01,K04,K08. |



**Author:** AMPEL360 Documentation WG / IDEALEeu Enterprise

---

## License

See [LICENSE](LICENSE) file for details.
