# AMPEL360-SPACE-T

## Overview

AMPEL360 SPACE-T is a comprehensive directory structure management system for aerospace and space technology projects. It implements a standardized OPT-IN topology with ATA chapter organization and P-CAD-CAE-CAM-CAOS engineering cycle support.

## Features

- **OPT-IN Topology**: Organized container axes for different technology domains
- **ATA Chapter Mapping**: Standard ATA (Air Transport Association) chapter organization
- **Lifecycle Management**: 14 standard lifecycle folders for each system
- **Engineering Cycles**: Complete P-CAD-CAE-CAM-CAOS workflow support
- **Subsystem Organization**: Hierarchical structure for subsystems and components

## Usage

### Generate the Directory Structure

To generate the complete AMPEL360 SPACE-T directory structure:

```bash
python generate_structure.py
```

This will create the `AMPEL360_SPACE-T` directory with the complete structure including:

- OPT-IN topology spine
- All configured ATA systems (21, 22, 23, 24, 25, 27, 28, 31, 53, 57, 85, 95)
- Lifecycle folders (XX-00_GENERAL)
- Root buckets (XX-10 through XX-90)
- Example subsystems with complete engineering cycles

### Structure Overview

The generated structure follows this hierarchy:

```
AMPEL360_SPACE-T/
├── O-ORGANIZATION/
├── P-PROGRAM/
├── T-TECHNOLOGY_ONBOARD_SYSTEMS/
│   ├── A-AIRFRAME_STRUCTURE/
│   │   ├── ATA_53-STRUCTURE_FUSELAGE/
│   │   │   ├── 53-00_GENERAL/
│   │   │   │   ├── 53-00-01_Overview/
│   │   │   │   ├── 53-00-02_Safety/
│   │   │   │   └── ... (14 lifecycle folders)
│   │   │   ├── 53-10_Operations/
│   │   │   ├── 53-20_Subsystems/
│   │   │   │   ├── 53-20-01_Pressure_Vessel/
│   │   │   │   │   ├── 00_PRE-CAD_Prompt_Engineering/
│   │   │   │   │   ├── 10_CAD/
│   │   │   │   │   ├── 20_CAE/
│   │   │   │   │   ├── 30_CAM/
│   │   │   │   │   ├── 40_CAOS/
│   │   │   │   │   └── META/
│   │   │   │   └── 53-20-02_Heat_Shield_TPS/
│   │   │   ├── 53-30_Circularity/
│   │   │   └── ... (through 53-90)
│   │   └── ATA_57-WINGS_LIFTING_BODY/
│   ├── E1-ENVIRONMENT_ECLSS/
│   │   └── ATA_21-ECLSS/
│   ├── L1-LOGICS_GNC/
│   └── ... (other technology domains)
├── I-INFRASTRUCTURES/
└── N-NEURAL_NETWORKS_DPP_TRACEABILITY/
    └── ATA_95-NEURAL_OPS_AI/
```

## Configuration

The structure can be customized by modifying the following sections in `generate_structure.py`:

- **OPT_IN_STRUCTURE**: Define the top-level axes
- **SYSTEMS_MAP**: Map ATA chapters to specific axes
- **LIFECYCLE_FOLDERS**: Configure the 14 standard lifecycle folders
- **BUCKETS**: Define root buckets (XX-10 to XX-90)
- **CYCLE_STRUCTURE**: Configure the engineering cycle phases

## Example Subsystems

The script includes example subsystems for demonstration:

- **ATA 21 (ECLSS)**:
  - 21-20-01_Cabin_Atmosphere
  - 21-20-02_Thermal_Control

- **ATA 53 (Structure/Fuselage)**:
  - 53-20-01_Pressure_Vessel
  - 53-20-02_Heat_Shield_TPS

- **ATA 95 (Neural Ops/AI)**:
  - 95-20-01_Mission_Planner_NN

## Specification

Based on AMPEL360 SPACE-T Specification v1.0 (2025-12-09)

## License

See LICENSE file for details.