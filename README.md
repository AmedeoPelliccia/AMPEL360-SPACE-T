# AMPEL360-SPACE-T

AMPEL360 Space-T Directory Structure Generator

## Overview

This repository contains the official directory structure generator for AMPEL360 Space-T projects, implementing:

- **OPT-IN Framework Standard v1.1**
- **ATA-SpaceT numbering system** (43 aerospace systems)
- **14-folder lifecycle structure**
- **Cross-ATA root buckets** (9 functional buckets)
- **P→CAD→CAE→CAM→CAOS engineering cycle**

## Quick Start

### Generate Complete Structure (All 43 Systems)

```bash
python generate_space_t_structure.py
```

This creates the `AMPEL360_SPACE-T/` directory with all OPT-IN axes and 43 ATA chapters.

### Generate Specific Systems

```bash
python generate_space_t_structure.py --systems 21,22,53,57,95
```

Only generates specified ATA chapters (ECLSS, GNC, Structure, Wings, Neural Ops).

### Custom Root Directory

```bash
python generate_space_t_structure.py --root ./my_project
```

### Dry Run (Preview Only)

```bash
python generate_space_t_structure.py --dry-run
```

## Generated Structure

### OPT-IN Axes (Top Level)

```
AMPEL360_SPACE-T/
├── O-ORGANIZATION/           # Governance, standards, program office
├── P-PROGRAM/                # Lifecycle phases, milestones, reviews
├── T-TECHNOLOGY_ONBOARD_SYSTEMS/  # All ATA chapters reside here
├── I-INFRASTRUCTURES/        # Ground systems, launch facilities
└── N-NEURAL_NETWORKS_DPP_TRACEABILITY/  # AI ops, Digital Product Passport
```

### ATA System Structure

Each ATA chapter follows this structure:

```
ATA_XX-SYSTEM_NAME/
├── XX-00_GENERAL/            # 14 lifecycle folders
│   ├── XX-00-01_Overview/
│   ├── XX-00-02_Safety/
│   ├── XX-00-03_Requirements/
│   ├── XX-00-04_Design/
│   ├── XX-00-05_Interfaces/
│   ├── XX-00-06_Engineering/
│   ├── XX-00-07_V_AND_V/
│   ├── XX-00-08_Prototyping/
│   ├── XX-00-09_Production_Planning/
│   ├── XX-00-10_Certification/
│   ├── XX-00-11_EIS_Versions_Tags/
│   ├── XX-00-12_Services/
│   ├── XX-00-13_Subsystems_Components/
│   └── XX-00-14_Ops_Std_Sustain/
├── XX-10_Operations/         # Operational procedures
├── XX-20_Subsystems/         # Functional subsystems with engineering cycle
├── XX-30_Circularity/        # Sustainability, LCA, recycling
├── XX-40_Software/           # SW, control logic, ML/NN
├── XX-50_Structures/         # Frames, housings, mounts
├── XX-60_Storages/           # Tanks, reservoirs
├── XX-70_Propulsion/         # Propulsive interfaces
├── XX-80_Energy/             # Electrical/thermal interactions
├── XX-90_Tables_Schemas_Diagrams/  # Data catalogs, training
└── META/                     # System registry, traceability
```

### Engineering Cycle (Per Subsystem)

```
XX-20-YY_Subsystem_Name/
├── 00_PRE-CAD_Prompt_Engineering/
│   ├── PROMPTS/
│   ├── CONTEXT/
│   ├── AGENTS/               # AI agent configs
│   ├── SPECS/
│   └── TRACE/                # Traceability maps
├── 10_CAD/
│   ├── WORKSPACE/
│   ├── MASTERS/
│   ├── COMPONENTS/
│   ├── EXPORTS/
│   ├── DRAWINGS/
│   └── META/
├── 20_CAE/
│   ├── MESHES/
│   ├── SCENARIOS/
│   ├── RESULTS/
│   ├── REPORTS/
│   └── META/
├── 30_CAM/
│   ├── PROCESS_PLANS/
│   ├── G-CODE/
│   ├── 3D_PRINT/
│   ├── BOM/
│   ├── TOOLING/
│   └── META/
├── 40_CAOS/
│   ├── MANUALS/
│   ├── PROCEDURES/
│   ├── DIGITAL_TWINS/
│   ├── AI_AGENTS/
│   ├── SPARES/
│   └── META/
└── META/                     # Subsystem traceability
```

## ATA-SpaceT Systems

The generator includes all 43 ATA chapters:

| Code | System | Description |
|------|--------|-------------|
| 00 | GENERAL_PROGRAM | Program governance, standards |
| 21 | ECLSS | Environmental Control & Life Support |
| 22 | GNC_AUTOFLIGHT | Guidance, Navigation, Control |
| 23 | COMMS | Communications |
| 24 | EPS_POWER | Electrical Power System |
| 25 | HABITAT_INTERIORS | Cabin modules, seats |
| 28 | PROPULSION_FUEL | Tanks, engines, propellants |
| 31 | AVIONICS_CORE | Flight computers, displays |
| 53 | STRUCTURE_FUSELAGE | Pressure vessel, TPS |
| 57 | WINGS_LIFTING_BODY | Wings, lifting surfaces |
| 72 | MAIN_ENGINES | Primary propulsion |
| 95 | NEURAL_OPS_AI | Neural networks, AI mission ops |
| 96 | DPP_TRACEABILITY | Digital Product Passport |
| ... | ... | _(see generate_space_t_structure.py for complete list)_ |

## Features

### Template Generation

The generator creates standardized templates for:

- **README.md files** - Documentation stubs with proper headers
- **Traceability matrices** - CSV format with ST-XX-YY-C-NNNN convention
- **Agent configurations** - AI agent configs (CAD, CAE, CAOS)
- **System registries** - YAML metadata files
- **Artifact templates** - Compliance-ready artifact headers

### Compliance & Standards

Generated structure follows:

- **OPT-IN Framework v1.1**
- **ATA iSpec 2200** (Space-T Adaptation)
- **DO-178C** (Software considerations)
- **DO-254** (Hardware considerations)
- **ECSS-E-ST-40C** (European Space Standards)

## Usage Examples

### Example 1: Full Project Initialization

```bash
# Initialize complete AMPEL360 Space-T structure
python generate_space_t_structure.py --root ./AMPEL360_Project

# Navigate to generated structure
cd AMPEL360_Project
```

### Example 2: Specific Systems for Small Projects

```bash
# Generate only essential systems
python generate_space_t_structure.py \
  --root ./SmallSat_Project \
  --systems 21,22,24,31,53
```

### Example 3: Preview Before Generation

```bash
# Check what will be created
python generate_space_t_structure.py --dry-run --systems 21,22

# If satisfied, run without --dry-run
python generate_space_t_structure.py --systems 21,22
```

## Requirements

- Python 3.6 or higher
- No external dependencies (uses standard library only)

## License

See [LICENSE](LICENSE) file for details.

## Contributing

This generator follows strict aerospace documentation standards. Any modifications must maintain:

- OPT-IN Framework compatibility
- ATA-SpaceT numbering consistency
- 14-folder lifecycle structure
- Complete traceability chains

## Version

- **Version:** 1.0
- **Date:** 2025-12-09
- **Author:** AMPEL360 Documentation WG / IDEALEeu Enterprise

## Next Steps After Generation

1. **Review generated structure** - Verify all required folders exist
2. **Populate README.md files** - Add system-specific content
3. **Add engineering artifacts** - Follow ST-XX-YY-C-NNNN naming convention
4. **Configure CI validation** - Set up automated structure checks
5. **Initialize version control** - Commit baseline structure