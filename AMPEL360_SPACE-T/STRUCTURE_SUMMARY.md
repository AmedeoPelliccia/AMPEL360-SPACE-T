# AMPEL360 Space-T Directory Structure Summary

**Generated:** 2025-12-11  
**Generator Version:** 1.0  
**Standard:** OPT-IN Framework v1.1 / ATA-SpaceT

---

## Overview

This directory contains the complete AMPEL360 Space-T structure with:

- **5 OPT-IN Axes** (O, P, T, I, N)
- **43 ATA-SpaceT Chapters** (Complete aerospace system catalog)
- **~3,400 Directories**
- **~3,300 Template Files**
- **~27 MB Total Size**

---

## Structure Statistics

### OPT-IN Axes (Top Level)

1. **O-ORGANIZATION** - Governance, standards, program office, stakeholders
2. **P-PROGRAM** - Lifecycle phases, milestones, reviews, deliverables
3. **T-TECHNOLOGY_ONBOARD_SYSTEMS** - All 43 ATA chapters
4. **I-INFRASTRUCTURES** - Ground systems, launch, H₂ value chains, facilities
5. **N-NEURAL_NETWORKS_DPP_TRACEABILITY** - AI ops, Digital Product Passport

### ATA Systems (43 Chapters)

Each chapter includes:
- **14 Lifecycle Folders** under XX-00_GENERAL
- **9 Cross-ATA Buckets** (Operations, Subsystems, Circularity, Software, Structures, Storages, Propulsion, Energy, Tables/Schemas)
- **Subsystem Engineering Cycles** (P→CAD→CAE→CAM→CAOS) for applicable systems
- **META Folder** with system registry and traceability matrix

### Key ATA Chapters

| Code | System | Subsystems |
|------|--------|------------|
| 00 | GENERAL_PROGRAM | Program governance |
| 21 | ECLSS | 3 subsystems (Cabin Atmosphere, Thermal Control, Humidity) |
| 22 | GNC_AUTOFLIGHT | 3 subsystems (AOCS, Autopilot, Flight Management) |
| 23 | COMMS | 3 subsystems (Space-Ground Link, Inter-Vehicle, Crew Comms) |
| 24 | EPS_POWER | 3 subsystems (Energy Storage, Power Distribution, Solar Arrays) |
| 25 | HABITAT_INTERIORS | 3 subsystems (Seats/Restraints, Interior Modules, Cargo) |
| 28 | PROPULSION_FUEL | 3 subsystems (Main Tanks, Feed System, Engine Interface) |
| 31 | AVIONICS_CORE | 3 subsystems (Flight Computers, Displays, Data Acquisition) |
| 53 | STRUCTURE_FUSELAGE | 3 subsystems (Pressure Vessel, Primary Structure, TPS) |
| 57 | WINGS_LIFTING_BODY | 3 subsystems (Main Wing, Control Surfaces, Winglets) |
| 72 | MAIN_ENGINES | 3 subsystems (Engine Core, Turbomachinery, Combustion Chamber) |
| 95 | NEURAL_OPS_AI | 3 subsystems (Mission AI, Predictive Maintenance, Autonomous Ops) |
| 96 | DPP_TRACEABILITY | Digital Product Passport |
| 97 | WIRING_DATA | Wiring diagrams, harness data |

---

## Engineering Cycle Structure

Each subsystem follows the **P→CAD→CAE→CAM→CAOS** cycle:

```
XX-20-YY_Subsystem_Name/
├── 00_PRE-CAD_Prompt_Engineering/
│   ├── PROMPTS/          # Design prompts
│   ├── CONTEXT/          # Contextual information
│   ├── AGENTS/           # AI agent configurations (CAD, CAE, CAOS)
│   ├── SPECS/            # Specifications
│   └── TRACE/            # Traceability maps
├── 10_CAD/               # Computer-Aided Design
│   ├── WORKSPACE/
│   ├── MASTERS/
│   ├── COMPONENTS/
│   ├── EXPORTS/
│   ├── DRAWINGS/
│   └── META/
├── 20_CAE/               # Computer-Aided Engineering
│   ├── MESHES/
│   ├── SCENARIOS/
│   ├── RESULTS/
│   ├── REPORTS/
│   └── META/
├── 30_CAM/               # Computer-Aided Manufacturing
│   ├── PROCESS_PLANS/
│   ├── G-CODE/
│   ├── 3D_PRINT/
│   ├── BOM/
│   ├── TOOLING/
│   └── META/
├── 40_CAOS/              # Computer-Aided Operations & Support
│   ├── MANUALS/
│   ├── PROCEDURES/
│   ├── DIGITAL_TWINS/
│   ├── AI_AGENTS/
│   ├── SPARES/
│   └── META/
└── META/                 # Subsystem metadata
```

---

## 14-Folder Lifecycle Structure

Each system includes these lifecycle phases under XX-00_GENERAL:

1. **01_Overview** - System overview and introduction
2. **02_Safety** - Safety analysis and requirements
3. **03_Requirements** - Functional and performance requirements
4. **04_Design** - Design specifications and documentation
5. **05_Interfaces** - Interface definitions and protocols
6. **06_Engineering** - Engineering analysis and calculations
7. **07_V_AND_V** - Verification and validation
8. **08_Prototyping** - Prototype development and testing
9. **09_Production_Planning** - Manufacturing planning
10. **10_Certification** - Certification documentation
11. **11_EIS_Versions_Tags** - Entry into service, versions, tags
12. **12_Services** - Service and support documentation
13. **13_Subsystems_Components** - Subsystem and component details
14. **14_Ops_Std_Sustain** - Operations, standards, sustainability

---

## Template Files Included

Every folder contains:

### 1. README.md Files
- Standardized structure with generation timestamp
- OPT-IN Framework v1.1 compliance
- Reference to aerospace standards (DO-178C, DO-254, ECSS-E-ST-40C)

### 2. System Registries (YAML)
- System metadata
- Subsystem listings
- Interface definitions
- Compliance standards tracking

### 3. Traceability Matrices (CSV)
- Artifact tracking (ST-XX-YY-C-NNNN format)
- Source prompt linkage
- Status and version control

### 4. Agent Configurations (YAML)
- CAD Agent config
- CAE Agent config
- CAOS Agent config
- AI-assisted engineering setup

---

## Compliance & Standards

This structure follows:

- ✅ **OPT-IN Framework Standard v1.1**
- ✅ **ATA iSpec 2200** (Space-T Adaptation)
- ✅ **DO-178C** - Software Considerations in Airborne Systems
- ✅ **DO-254** - Design Assurance for Airborne Electronic Hardware
- ✅ **ECSS-E-ST-40C** - European Cooperation for Space Standardization

---

## Usage

### Navigate the Structure

```bash
# Browse OPT-IN axes
cd O-ORGANIZATION/
cd P-PROGRAM/
cd T-TECHNOLOGY_ONBOARD_SYSTEMS/
cd I-INFRASTRUCTURES/
cd N-NEURAL_NETWORKS_DPP_TRACEABILITY/

# Access specific ATA system
cd T-TECHNOLOGY_ONBOARD_SYSTEMS/ATA_21-ECLSS/

# Access lifecycle phase
cd T-TECHNOLOGY_ONBOARD_SYSTEMS/ATA_21-ECLSS/21-00_GENERAL/21-00-03_Requirements/

# Access subsystem engineering cycle
cd T-TECHNOLOGY_ONBOARD_SYSTEMS/ATA_21-ECLSS/21-20-10_Cabin_Atmosphere/10_CAD/
```

### Next Steps

1. **Customize README Files** - Add system-specific content
2. **Populate Templates** - Fill in project details
3. **Add Engineering Artifacts** - Follow naming conventions
4. **Initialize Git** - Version control baseline
5. **Configure CI/CD** - Automated validation

---

## Regeneration

To regenerate or update this structure:

```bash
# Full regeneration (all 43 systems)
python generate_space_t_structure.py --root ./AMPEL360_SPACE-T

# Partial regeneration (specific systems)
python generate_space_t_structure.py --root ./AMPEL360_SPACE-T --systems 21,22,53

# Preview changes
python generate_space_t_structure.py --dry-run
```

---

## Maintenance

- **DO NOT DELETE** folders marked as N/A (per OPT-IN Framework v1.1)
- **MAINTAIN** naming conventions (XX-YY-ZZ format)
- **UPDATE** META/System_Registry.yaml as subsystems are added
- **TRACK** artifacts using ST-XX-YY-C-NNNN format
- **VERSION** changes in Git with meaningful commits

---

## Contact & Support

For questions about this structure:
- Refer to OPT-IN Framework Standard v1.1
- Consult ATA iSpec 2200 (Space-T Adaptation)
- Review EXAMPLES.md for usage patterns

---

**End of Summary**
