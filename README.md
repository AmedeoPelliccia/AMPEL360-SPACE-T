# AMPEL360-SPACE-T

**Aircraft Models by Proactive Engineering Leaders – Space Transport**

Complete OPT-IN Framework Directory Structure Generator Suite

---

## Overview

This repository contains the official directory structure generators for AMPEL360 Space-T projects, implementing:

- **OPT-IN Framework Standard v1.1** (5 axes: Organization, Program, Technology, Infrastructures, Neural)
- **Nomenclature Standard v3.0** (Mandatory 10-field file naming with PROJECT/PROGRAM identity)
- **ATA-SpaceT numbering system** (70+ aerospace systems across all axes)
- **14-folder lifecycle structure** (XX-00_GENERAL canonical pattern)
- **9 Cross-ATA root buckets** (XX-10 through XX-90)
- **P→CAD→CAE→CAM→CAOS engineering cycle** (AI-assisted workflow)
- **ML Lifecycle** for neural systems (Architecture→Training→Validation→Deployment→Monitoring)

---

## File Naming Convention (Nomenclature Standard v3.0)

**All artifacts in this repository MUST follow the mandatory nomenclature standard.**

### Format

```
[ROOT]_[BUCKET]_[TYPE]_[SUBJECT]_[PROJECT]_[PROGRAM]_[VARIANT]_[DESCRIPTION]_[VERSION].[EXT]
```

### Field Definitions

- **ROOT**: ATA code (2-3 digits, e.g., `00`, `24`, `115`)
- **BUCKET**: Domain classification (`00|10|20|30|40|50|60|70|80|90`)
- **TYPE**: Artifact type (2-8 uppercase, e.g., `PLAN`, `FHA`, `REQ`)
- **SUBJECT**: Lifecycle stage (`LC01-LC14`) or Sub-bucket (`SB15-SB99`)
- **PROJECT**: Fixed value `AMPEL360` (hard constraint)
- **PROGRAM**: Program identity `SPACET` (allowlist, extensible)
- **VARIANT**: Configuration variant (e.g., `PLUS`, `CERT`, `SYS`, `SW`)
- **DESCRIPTION**: lowercase-kebab-case description
- **VERSION**: `vNN` (e.g., `v01`, `v02`)
- **EXT**: File extension (lowercase)

### Examples

- `00_00_PLAN_LC02_AMPEL360_SPACET_PLUS_safety-program_v01.md` (Lifecycle plan)
- `00_70_FHA_SB70_AMPEL360_SPACET_PLUS_propulsion_v01.md` (Propulsion FHA)
- `00_40_REQ_SB40_AMPEL360_SPACET_PLUS_software-safety-reqs_v01.md` (Software requirements)
- `00_90_SCH_SB90_AMPEL360_SPACET_GEN_hazard-log-schema_v01.json` (Reference schema)
- `00_00_PLAN_LC10_AMPEL360_SPACET_CERT_certification-authority-basis_v01.md` (Certification plan)

### Validation

```bash
# Validate a single file
python validate_nomenclature.py <filename>

# Validate all files in repository
python validate_nomenclature.py --check-all

# Get help
python validate_nomenclature.py --help
```

### Installation of Pre-commit Hook

```bash
# Install the pre-commit hook to validate files before committing
cp scripts/pre-commit .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

📖 **Full standard**: [`00_00_STD_LC01-SPACET_nomenclature-standard_v01.md`](00_00_STD_LC01-SPACET_nomenclature-standard_v01.md)

### Document Templates

Use standardized templates to create compliant documentation:

```bash
# Create a new document from template
python scripts/scaffold.py <ROOT> <BUCKET> <TYPE> <VARIANT> <DESC> <VER>

# Examples:
python scripts/scaffold.py 00 00 PLAN LC02-SPACET safety-program v01
python scripts/scaffold.py 00 70 FHA SYS propulsion v01
python scripts/scaffold.py 00 40 REQ SW software-requirements v01
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
📖 **Guide**: [`00_00_IDX_LC01-SPACET_automatic-type-detection_v01.md`](00_00_IDX_LC01-SPACET_automatic-type-detection_v01.md)

### Certification Knots System

Cross-cutting workflow elements for systematic certification and compliance activities:

```bash
# View active knots
cat 00_90_CAT_SB00_CERT_knots-catalog_v01.json

# Validate knot data structure
python3 -c "
import json, jsonschema
schema = json.load(open('00_90_SCH_SB00_GEN_knots-data-structure_v01.json'))
data = json.load(open('00_90_CAT_SB00_CERT_knots-catalog_v01.json'))
jsonschema.validate(instance=data, schema=schema)
print('✓ Knot data validated successfully')
"
```

**Active Knots:**
- **K01**: Certification Authority Basis - Establishes certification basis and compliance mapping (52 ATA systems across all axes)

📋 **Quick Reference**: [`00_00_CAT_LC10_CERT_knots-quick-reference_v01.md`](00_AMPEL360_SPACET_Q10_CERT_PLUS_BB_GEN_LC10_K01_CERT__knots-quick-reference_CAT_I01-R01_ACTIVE.md)  
📖 **Complete Index**: [`00_00_IDX_LC10_CERT_certification-knots-index_v01.md`](00_AMPEL360_SPACET_Q10_CERT_PLUS_BB_GEN_LC10_K01_CERT__certification-knots-index_IDX_I01-R01_ACTIVE.md)  
📘 **K01 Documentation**: [`00_00_PLAN_LC10_CERT_knot-k01-certification-authority-basis_v01.md`](00_AMPEL360_SPACET_Q10_CERT_PLUS_PR_GEN_LC10_K01_CERT__knot-k01-certification-authority-basis_PLAN_I01-R01_ACTIVE.md)

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

## OPT-IN Framework Architecture

### Five Axes (Top Level)

```
AMPEL360_SPACE-T/
├── O-ORGANIZATION/                        # Governance, CM, QMS, SMS, Regulatory
│   ├── ATA_00-GENERAL_INFO/
│   ├── ATA_01-POLICY_PROCEDURES/
│   ├── ATA_04-AIRWORTHINESS_LIMITS/
│   ├── ATA_05-TIME_LIMITS_CHECKS/
│   ├── ATA_06-CONFIG_MANAGEMENT/
│   ├── ATA_07-QUALITY_MANAGEMENT/
│   ├── ATA_08-SAFETY_MANAGEMENT/
│   └── ATA_09-REGULATORY_AFFAIRS/
│
├── P-PROGRAM/                             # Planning, Cost, Risk, Reviews
│   ├── ATA_06-PROGRAM_PLANNING/
│   ├── ATA_07-COST_MANAGEMENT/
│   ├── ATA_08-RISK_MANAGEMENT/
│   ├── ATA_09-REVIEWS_GATES/
│   ├── ATA_10-STAKEHOLDER_MGMT/
│   ├── ATA_11-CONTRACT_MGMT/
│   └── ATA_12-INTEGRATION_MGMT/
│
├── T-TECHNOLOGY_ONBOARD_SYSTEMS/          # Vehicle systems (41 chapters)
│   ├── ATA_21-ECLSS/
│   ├── ATA_22-GNC_AUTOFLIGHT/
│   ├── ATA_23-COMMS/
│   ├── ATA_24-EPS_POWER/
│   ├── ATA_25-HABITAT_INTERIORS/
│   ├── ATA_28-PROPULSION_FUEL/
│   ├── ATA_31-AVIONICS_CORE/
│   ├── ATA_53-STRUCTURE_FUSELAGE/
│   ├── ATA_57-WINGS_LIFTING_BODY/
│   ├── ATA_72-MAIN_ENGINES/
│   └── ... (41 systems total)
│
├── I-INFRASTRUCTURES/                     # Ground systems, H₂, Launch
│   ├── ATA_02-OPERATIONS_INFO/
│   ├── ATA_03-GROUND_EQUIPMENT/
│   ├── ATA_10-PARKING_MOORING/
│   ├── ATA_13-LOGISTICS/
│   ├── ATA_85-H2_VALUE_CHAIN/
│   ├── ATA_86-LAUNCH_FACILITIES/
│   ├── ATA_87-LANDING_RECOVERY/
│   ├── ATA_88-PASSENGER_TERMINAL/
│   ├── ATA_89-MISSION_CONTROL/
│   ├── ATA_90-GROUND_SUPPORT/
│   ├── ATA_115-SUPPLY_CHAIN/
│   └── ATA_116-FACILITIES_MGMT/
│
└── N-NEURAL_NETWORKS_DPP_TRACEABILITY/    # AI/ML, DPP, Analytics
    ├── ATA_95-NEURAL_OPS_AI/
    ├── ATA_96-DPP_TRACEABILITY/
    ├── ATA_97-DATA_ANALYTICS/
    └── ATA_98-HUMAN_AI_INTERFACE/
```

---

## Generator Scripts

| Generator | Axis | Systems | Key Content |
|:----------|:-----|:--------|:------------|
| `generate_space_t_structure.py` | T-TECHNOLOGY | 41 ATA chapters | Vehicle HW/SW, engineering cycle |
| `generate_organization.py` | O-ORGANIZATION | 8 ATA chapters | CM, QMS, SMS, Regulatory |
| `generate_program.py` | P-PROGRAM | 7 ATA chapters | WBS, EVM, Risk, Reviews |
| `generate_infrastructures.py` | I-INFRASTRUCTURES | 12 ATA chapters | H₂, Launch, MCC, Terminals |

### Common Options

```bash
--root PATH      # Output directory (default: ./AMPEL360_SPACE-T)
--systems LIST   # Comma-separated ATA codes (e.g., "21,22,53")
--dry-run        # Preview without creating files
```

---

## Canonical Structure

### XX-00_GENERAL (14 Lifecycle Folders)

Every ATA chapter includes:

```
ATA_XX-DESCRIPTION/
└── XX-00_GENERAL/
    ├── XX-00-01_Overview/           # System description, scope
    ├── XX-00-02_Safety/             # Safety requirements, hazards
    ├── XX-00-03_Requirements/       # Functional/performance reqs
    ├── XX-00-04_Design/             # Design philosophy, trade studies
    ├── XX-00-05_Interfaces/         # ICDs, interface definitions
    ├── XX-00-06_Engineering/        # Engineering standards, methods
    ├── XX-00-07_V_AND_V/            # Verification & validation plans
    ├── XX-00-08_Prototyping/        # Prototype specs, test articles
    ├── XX-00-09_Production_Planning/# Manufacturing planning
    ├── XX-00-10_Certification/      # Certification plans, evidence
    ├── XX-00-11_EIS_Versions_Tags/  # Entry-into-service, baselines
    ├── XX-00-12_Services/           # Support services, logistics
    ├── XX-00-13_Subsystems_Components/ # Component breakdown
    └── XX-00-14_Ops_Std_Sustain/    # Operations, standards, sustainability
```

### Cross-ATA Buckets (9 Mandatory)

```
ATA_XX-DESCRIPTION/
├── XX-10_Operations/              # Operational procedures
├── XX-20_Subsystems/              # Engineering subsystems (P→CAD→CAE→CAM→CAOS)
├── XX-30_Circularity/             # Sustainability, LCA, DPP links
├── XX-40_Software/                # SW, controllers, ML/NN
├── XX-50_Structures/              # Physical structures, mounts
├── XX-60_Storages/                # Tanks, reservoirs, archives
├── XX-70_Propulsion/              # Propulsive interfaces
├── XX-80_Energy/                  # Power, thermal interfaces
└── XX-90_Tables_Schemas_Diagrams/ # Data catalogs, drawings
```

---

## Engineering Cycle

### Standard P→CAD→CAE→CAM→CAOS (XX-20_Subsystems)

```
XX-20-YY_Subsystem_Name/
├── 00_INDEX_README.md
├── 00_PRE-CAD_Prompt_Engineering/
│   ├── PROMPTS/          # ST-XX-YY-P-NNNN prompt files
│   ├── CONTEXT/          # Standards, references
│   ├── AGENTS/           # AI agent configurations
│   ├── SPECS/            # Hard requirements
│   └── TRACE/            # Prompt→Artifact traceability
├── 10_CAD/
│   ├── WORKSPACE/        # Work-in-progress
│   ├── MASTERS/          # Released geometry (ST-XX-YY-D-NNNN)
│   ├── COMPONENTS/       # Part models
│   ├── EXPORTS/          # STEP, IGES, STL
│   ├── DRAWINGS/         # 2D drawings
│   └── META/
├── 20_CAE/
│   ├── MESHES/           # FEA/CFD meshes
│   ├── SCENARIOS/        # Analysis cases (ST-XX-YY-E-CaseNN)
│   ├── RESULTS/          # Simulation outputs
│   ├── REPORTS/          # Analysis reports
│   └── META/
├── 30_CAM/
│   ├── PROCESS_PLANS/    # Manufacturing process
│   ├── G-CODE/           # NC programs (ST-XX-YY-M-NNNN)
│   ├── 3D_PRINT/         # AM build files
│   ├── BOM/              # Bills of material
│   ├── TOOLING/          # Tool designs
│   └── META/
├── 40_CAOS/
│   ├── MANUALS/          # User manuals
│   ├── PROCEDURES/       # Ops procedures (ST-XX-YY-O-NNNN)
│   ├── DIGITAL_TWINS/    # Twin configurations
│   ├── AI_AGENTS/        # Runtime agents
│   ├── SPARES/           # Spare parts lists
│   └── META/
└── META/
    ├── Traceability_Matrix.csv
    └── Dependencies.yaml
```

### ML Lifecycle (ATA 95 Neural Systems)

```
95-20-XX_Neural_Model/
├── 00_INDEX_README.md
├── 00_PRE-CAD_Prompt_Engineering/
├── 10_ARCHITECTURE/      # Network topology, hyperparameters
├── 20_TRAINING/          # Datasets, pipelines, checkpoints
├── 30_VALIDATION/        # Test cases, benchmarks, adversarial
├── 40_DEPLOYMENT/        # ONNX models, runtime configs
├── 50_MONITORING/        # Dashboards, drift detection
└── META/
    ├── Model_Card.yaml
    └── Certification_Evidence.yaml
```

---

## ATA-SpaceT Chapter Index

### O-ORGANIZATION (8 Chapters)

| Code | System | Description |
|:-----|:-------|:------------|
| 00 | GENERAL_INFO | Glossary, units, document numbering |
| 01 | POLICY_PROCEDURES | Policies, procedures, directives |
| 04 | AIRWORTHINESS_LIMITS | Certification basis, limitations |
| 05 | TIME_LIMITS_CHECKS | Maintenance intervals, life limits |
| 06 | CONFIG_MANAGEMENT | Baselines, change control |
| 07 | QUALITY_MANAGEMENT | QMS, audits, NCR, supplier QA |
| 08 | SAFETY_MANAGEMENT | SMS, hazard analysis, risk |
| 09 | REGULATORY_AFFAIRS | FAA/EASA/ESA certification |

### P-PROGRAM (7 Chapters)

| Code | System | Description |
|:-----|:-------|:------------|
| 06 | PROGRAM_PLANNING | WBS, IMS, resources, phases |
| 07 | COST_MANAGEMENT | Budget, EVM, cost estimation |
| 08 | RISK_MANAGEMENT | Risk register, mitigation |
| 09 | REVIEWS_GATES | SRR/PDR/CDR/TRR/FRR, gates |
| 10 | STAKEHOLDER_MGMT | Communication, reporting |
| 11 | CONTRACT_MGMT | Procurement, suppliers |
| 12 | INTEGRATION_MGMT | Cross-axis integration |

### T-TECHNOLOGY (41 Chapters)

| Code | System | Code | System |
|:-----|:-------|:-----|:-------|
| 21 | ECLSS | 50 | CARGO_ACCESS |
| 22 | GNC_AUTOFLIGHT | 51 | STANDARD_PRACTICES |
| 23 | COMMS | 52 | DOORS |
| 24 | EPS_POWER | 53 | STRUCTURE_FUSELAGE |
| 25 | HABITAT_INTERIORS | 55 | STABILIZERS |
| 26 | FIRE_PROTECTION | 56 | WINDOWS |
| 27 | FLIGHT_CONTROLS | 57 | WINGS_LIFTING_BODY |
| 28 | PROPULSION_FUEL | 70 | STANDARD_PRACTICES_PROP |
| 29 | HYDRAULICS | 71 | POWERPLANT |
| 30 | ICE_RAIN_PROTECT | 72 | MAIN_ENGINES |
| 31 | AVIONICS_CORE | 73 | ENGINE_FUEL_CONTROL |
| 32 | LANDING_GEAR | 74 | IGNITION |
| 33 | LIGHTS | 75 | ENGINE_AIR |
| 34 | NAVIGATION | 76 | ENGINE_CONTROLS |
| 35 | OXYGEN | 77 | ENGINE_INDICATING |
| 36 | PNEUMATICS | 78 | ENGINE_EXHAUST |
| 38 | WATER_WASTE | 79 | ENGINE_OIL |
| 39 | ELECTRICAL_PANELS | 95 | NEURAL_OPS_AI |
| 42 | INTEGRATED_MODULAR | 96 | DPP_TRACEABILITY |
| 44 | CABIN_SYSTEMS | 97 | DATA_ANALYTICS |
| 45 | CENTRAL_MAINTENANCE | | |
| 46 | INFO_SYSTEMS | | |
| 49 | APU | | |

### I-INFRASTRUCTURES (12 Chapters)

| Code | System | Description |
|:-----|:-------|:------------|
| 02 | OPERATIONS_INFO | Ground operations manuals |
| 03 | GROUND_EQUIPMENT | GSE, tooling, support |
| 10 | PARKING_MOORING | Pad ops, umbilicals |
| 13 | LOGISTICS | Spares, consumables |
| 85 | H2_VALUE_CHAIN | Hydrogen production, storage |
| 86 | LAUNCH_FACILITIES | Pads, towers, loading |
| 87 | LANDING_RECOVERY | Landing zones, recovery |
| 88 | PASSENGER_TERMINAL | Check-in, training, boarding |
| 89 | MISSION_CONTROL | MCC, telemetry, flight dynamics |
| 90 | GROUND_SUPPORT | Transport, erector, checkout |
| 115 | SUPPLY_CHAIN | Suppliers, procurement |
| 116 | FACILITIES_MGMT | Buildings, utilities |

### N-NEURAL (4 Chapters)

| Code | System | Description |
|:-----|:-------|:------------|
| 95 | NEURAL_OPS_AI | Flight control NN, anomaly detection, predictive maintenance |
| 96 | DPP_TRACEABILITY | Digital Product Passport, blockchain anchoring |
| 97 | DATA_ANALYTICS | Telemetry analytics, BI |
| 98 | HUMAN_AI_INTERFACE | XAI, crew decision support, autonomy |

---

## Artifact ID Convention

### Standard Pattern

```
ST-XX-YY-C-NNNN_Name.ext
```

| Component | Description | Values |
|:----------|:------------|:-------|
| ST | Space-T prefix | Fixed |
| XX | ATA chapter | 00-98, 115-116 |
| YY | Subsystem code | 10, 20, 30... |
| C | Cycle phase | P, D, E, M, O |
| NNNN | Sequence | 0001-9999 |
| Name | Descriptive | Alphanumeric |
| ext | Extension | .md, .yaml, .prt... |

### Cycle Phase Codes

| Code | Phase | Description |
|:-----|:------|:------------|
| P | Prompting | PRE-CAD prompt engineering |
| D | Design | CAD geometry/models |
| E | Engineering | CAE analysis/simulation |
| M | Manufacturing | CAM production data |
| O | Operations | CAOS procedures/manuals |

### Special Types

| Pattern | Type | Example |
|:--------|:-----|:--------|
| `DPP-ST-XX-NNNNNNNN` | Digital Product Passport | DPP-ST-53-A1B2C3D4 |
| `ST-95-XX-M-NNNN` | ML Model | ST-95-10-M-0001.onnx |
| `DS-XX-YY-NNN` | Dataset | DS-95-10-001 |
| `EVD-ST-XX-NNNN` | Evidence package | EVD-ST-53-0001 |

---

## Compliance Standards

| Domain | Standards |
|:-------|:----------|
| Configuration | ANSI/EIA-649B, MIL-HDBK-61A |
| Quality | AS9100D, ISO 9001:2015 |
| Safety | SAE ARP4754A, ARP4761, MIL-STD-882E |
| Software | DO-178C, DO-330 |
| Hardware | DO-254 |
| AI/ML | EASA AI Roadmap, DO-178C/ML Supplement |
| Publications | S1000D, ATA iSpec 2200 |
| H₂ Systems | NFPA 2, ISO 14687, SAE AS6858 |
| Space Ops | ECSS-E-ST-40C, NASA-STD-3001 |
| DPP | EU DPP Regulation, ISO 14067 |

---

## Generated Templates

The generators create standardized templates:

- **README.md files** - Documentation stubs with YAML frontmatter
- **Traceability matrices** - CSV with ST-XX-YY-C-NNNN convention
- **Agent configurations** - AI agent YAML configs
- **System registries** - YAML metadata files
- **Risk registers** - Program risk CSV templates
- **Review criteria** - SRR/PDR/CDR checklists
- **Model cards** - ML model documentation templates
- **DPP schemas** - Digital passport JSON schemas

---

## Usage Examples

### Example 1: Initialize Complete Project

```bash
# Create all axes
mkdir AMPEL360_Project && cd AMPEL360_Project

python generate_organization.py --root .
python generate_program.py --root .
python generate_space_t_structure.py --root .
python generate_infrastructures.py --root .
```

### Example 2: Small Satellite Project

```bash
# Minimal systems for small sat
python generate_space_t_structure.py \
  --root ./SmallSat \
  --systems 21,22,24,31,53

python generate_organization.py \
  --root ./SmallSat \
  --systems 06,07,08
```

### Example 3: H₂ Infrastructure Focus

```bash
# H2 value chain development
python generate_infrastructures.py \
  --root ./H2_Project \
  --systems 85,86,90
```

### Example 4: AI/ML Development

```bash
# Neural systems only
python generate_space_t_structure.py \
  --root ./AI_Dev \
  --systems 95,96,97,98
```

---

## Requirements

- Python 3.6 or higher
- No external dependencies (uses standard library only)

---

## Repository Contents

```
AMPEL360-SPACE-T/
├── README.md                           # This file
├── generate_space_t_structure.py       # T-TECHNOLOGY generator
├── generate_organization.py            # O-ORGANIZATION generator
├── generate_program.py                 # P-PROGRAM generator
├── generate_infrastructures.py         # I-INFRASTRUCTURES generator
├── OPT-IN_FRAMEWORK_COMPLETE_v1.1.md   # Master specification
├── O-ORGANIZATION_SPEC.md              # O-axis specification
├── P-PROGRAM_SPEC.md                   # P-axis specification
├── I-INFRASTRUCTURES_SPEC.md           # I-axis specification
├── N-NEURAL_SPEC.md                    # N-axis specification
└── AMPEL360_SPACE-T_DIR_SPEC_v1.0.md   # T-axis specification
```

---

## Next Steps After Generation

1. **Review structure** - Verify all required folders exist
2. **Populate README files** - Add system-specific content
3. **Add engineering artifacts** - Follow ST-XX-YY-C-NNNN convention
4. **Configure CI validation** - Set up automated structure checks
5. **Initialize version control** - Commit baseline structure
6. **Create traceability links** - Populate META/Traceability_Matrix.csv
7. **Define baselines** - Establish FBL → ABL → DBL → PBL

---

## Contributing

Modifications must maintain:

- OPT-IN Framework v1.1 compatibility
- ATA-SpaceT numbering consistency
- 14-folder lifecycle structure
- 9 cross-ATA bucket presence
- Complete traceability chains

---

## Version

| Version | Date | Changes |
|:--------|:-----|:--------|
| 1.0 | 2025-12-09 | Initial T-TECHNOLOGY generator |
| 1.1 | 2025-12-09 | Added O, P, I, N axis generators |

**Author:** AMPEL360 Documentation WG / IDEALEeu Enterprise

---

## License

See [LICENSE](LICENSE) file for details.
