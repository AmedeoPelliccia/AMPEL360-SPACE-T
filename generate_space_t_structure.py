#!/usr/bin/env python3
"""
AMPEL360 Space-T Directory Structure Generator
==============================================
Version: 1.0
Date: 2025-12-09
Author: AMPEL360 Documentation WG / IDEALEeu Enterprise

Generates the complete directory structure following:
- OPT-IN Framework Standard v1.1
- ATA-SpaceT numbering
- 14-folder lifecycle structure
- Cross-ATA root buckets
- P→CAD→CAE→CAM→CAOS engineering cycle

Usage:
    python generate_space_t_structure.py [--root PATH] [--systems CODES]
    
Examples:
    python generate_space_t_structure.py
    python generate_space_t_structure.py --root ./my_project
    python generate_space_t_structure.py --systems 21,22,53,57,95
"""

import argparse
from pathlib import Path
from datetime import datetime

# ============================================================================
# CONFIGURATION: ATA-SpaceT Systems Master Table
# ============================================================================

SYSTEMS = {
    "00": ("GENERAL_PROGRAM", "Program governance, standards, config mgmt"),
    "05": ("TIME_LIMITS", "Inspection intervals, maintenance schedules"),
    "06": ("DIMENSIONS_AREAS", "Vehicle dimensions, zones, access areas"),
    "07": ("LIFTING_SHORING", "Ground handling, jacking, transportation"),
    "10": ("PARKING_MOORING", "Pad operations, docking, tie-down"),
    "21": ("ECLSS", "Environmental Control & Life Support System"),
    "22": ("GNC_AUTOFLIGHT", "Guidance, Navigation, Control (AOCS)"),
    "23": ("COMMS", "Communications (Ground-Space, Inter-vehicle)"),
    "24": ("EPS_POWER", "Electrical Power System"),
    "25": ("HABITAT_INTERIORS", "Cabin modules, seats, restraints, cargo"),
    "26": ("FIRE_PROTECTION", "Fire detection, suppression, smoke mgmt"),
    "27": ("FLIGHT_CONTROLS", "RCS, aero surfaces, TVC actuators"),
    "28": ("PROPULSION_FUEL", "Tanks, feed lines, engines, propellants"),
    "29": ("HYDRAULICS", "Hydraulic/pneumatic actuation systems"),
    "30": ("ICE_RAIN_PROTECT", "Thermal protection, de-icing"),
    "31": ("AVIONICS_CORE", "Flight computers, displays, data acquisition"),
    "32": ("LANDING_GEAR", "Landing systems, gear, recovery"),
    "34": ("NAVIGATION", "Inertial nav, star trackers, GPS"),
    "35": ("OXYGEN", "Crew oxygen, emergency supply"),
    "36": ("PNEUMATICS", "Pneumatic systems, pressurization"),
    "42": ("IMA_SYSTEMS", "Integrated Modular Avionics"),
    "44": ("CABIN_SYSTEMS", "Lighting, entertainment, crew facilities"),
    "45": ("CENTRAL_MAINT", "Central maintenance, diagnostics"),
    "46": ("INFO_SYSTEMS", "Information systems, connectivity"),
    "47": ("NITROGEN", "Nitrogen systems, cryogenic interfaces"),
    "49": ("APU", "Auxiliary Power Unit"),
    "53": ("STRUCTURE_FUSELAGE", "Pressure vessel, primary structure, TPS"),
    "55": ("STABILIZERS", "Vertical/horizontal stabilizers, fins"),
    "57": ("WINGS_LIFTING_BODY", "Wings, lifting surfaces, flaperons"),
    "72": ("MAIN_ENGINES", "Primary propulsion engines"),
    "73": ("ENGINE_FUEL_CTRL", "Engine fuel control, regulators"),
    "74": ("IGNITION", "Engine ignition systems"),
    "75": ("BLEED_AIR", "Bleed air systems"),
    "76": ("ENGINE_CONTROLS", "Engine electronic controls, FADEC"),
    "77": ("ENGINE_INDICATING", "Engine parameters, health monitoring"),
    "78": ("EXHAUST", "Exhaust systems, nozzles"),
    "79": ("OIL", "Lubrication systems"),
    "80": ("STARTING", "Engine starting systems"),
    "85": ("CIRCULARITY_SYSTEMS", "Recycling, LCA, bio-regeneration"),
    "90": ("GROUND_SUPPORT", "Ground support equipment, interfaces"),
    "95": ("NEURAL_OPS_AI", "Neural networks, AI mission ops"),
    "96": ("DPP_TRACEABILITY", "Digital Product Passport"),
    "97": ("WIRING_DATA", "Wiring diagrams, harness data"),
}

# O-ORGANIZATION axis systems
O_SYSTEMS = {
    "00": ("GENERAL_INFO", "Program-wide general information, glossary, units"),
    "01": ("POLICY_PROCEDURES", "Corporate policies, procedures, directives"),
    "04": ("AIRWORTHINESS_LIMITS", "Certification basis, airworthiness limitations"),
    "05": ("TIME_LIMITS_CHECKS", "Scheduled maintenance, life limits, inspections"),
    "06": ("CONFIG_MANAGEMENT", "Configuration control, baselines, change management"),
    "07": ("QUALITY_MANAGEMENT", "QMS, audits, non-conformance, supplier quality"),
    "08": ("SAFETY_MANAGEMENT", "SMS, hazard analysis, risk management"),
    "09": ("REGULATORY_AFFAIRS", "Certification plans, authority liaison, compliance"),
}

# P-PROGRAM axis systems
P_SYSTEMS = {
    "06": ("PROGRAM_PLANNING", "Master plans, WBS, IMS, resource planning"),
    "07": ("COST_MANAGEMENT", "Budget, EVM, financial controls, forecasting"),
    "08": ("RISK_MANAGEMENT", "Program risks, opportunities, mitigation"),
    "09": ("REVIEWS_GATES", "Design reviews, gate reviews, audits"),
    "10": ("STAKEHOLDER_MGMT", "Communication, reporting, decisions"),
    "11": ("CONTRACT_MGMT", "Contracts, procurement, supplier management"),
    "12": ("INTEGRATION_MGMT", "Cross-axis integration, dependencies"),
}

# I-INFRASTRUCTURES axis systems
I_SYSTEMS = {
    "02": ("OPERATIONS_INFO", "Ground operations information systems"),
    "03": ("GROUND_EQUIPMENT", "Support equipment, tooling, GSE"),
    "10": ("PARKING_MOORING", "Pad operations, docking, tie-down"),
    "13": ("LOGISTICS", "Spare parts, consumables, supply chain"),
    "85": ("H2_VALUE_CHAIN", "Hydrogen production, storage, distribution"),
    "86": ("LAUNCH_FACILITIES", "Launch pads, towers, umbilicals"),
    "87": ("LANDING_RECOVERY", "Landing zones, recovery systems"),
    "88": ("PASSENGER_TERMINAL", "Check-in, training, boarding facilities"),
    "89": ("MISSION_CONTROL", "MCC, telemetry, flight dynamics"),
    "90": ("GROUND_SUPPORT", "GSE, transportation, handling"),
    "115": ("SUPPLY_CHAIN", "Supplier network, procurement, QA"),
    "116": ("FACILITIES_MGMT", "Buildings, utilities, security"),
}

# N-NEURAL_NETWORKS_DPP_TRACEABILITY axis systems
N_SYSTEMS = {
    "95": ("NEURAL_OPS_AI", "Neural networks, ML models, AI mission operations"),
    "96": ("DPP_TRACEABILITY", "Digital Product Passport, blockchain anchoring, provenance"),
    "97": ("DATA_ANALYTICS", "Big data processing, telemetry analytics, insights"),
    "98": ("HUMAN_AI_INTERFACE", "XAI, crew decision support, autonomy levels"),
}

# Default subsystems for key chapters (expandable)
DEFAULT_SUBSYSTEMS = {
    "21": [("10", "Cabin_Atmosphere"), ("20", "Thermal_Control"), ("30", "Humidity_Contamination")],
    "22": [("10", "AOCS"), ("20", "Autopilot"), ("30", "Flight_Management")],
    "23": [("10", "Space_Ground_Link"), ("20", "Inter_Vehicle_Comms"), ("30", "Crew_Comms")],
    "24": [("10", "Energy_Storage"), ("20", "Power_Distribution"), ("30", "Solar_Arrays")],
    "25": [("10", "Seats_Restraints"), ("20", "Interior_Modules"), ("30", "Cargo_Lockers")],
    "28": [("10", "Main_Propellant_Tanks"), ("20", "Feed_System"), ("30", "Engine_Interface")],
    "31": [("10", "Flight_Computers"), ("20", "Displays_Controls"), ("30", "Data_Acquisition")],
    "53": [("10", "Pressure_Vessel"), ("20", "Primary_Structure"), ("30", "Thermal_Protection")],
    "57": [("10", "Main_Wing_Structure"), ("20", "Control_Surfaces"), ("30", "Winglets")],
    "72": [("10", "Engine_Core"), ("20", "Turbomachinery"), ("30", "Combustion_Chamber")],
    "95": [("10", "Mission_AI"), ("20", "Predictive_Maintenance"), ("30", "Autonomous_Ops")],
}

# 14-folder lifecycle structure
LIFECYCLE_FOLDERS = [
    ("01", "Overview"),
    ("02", "Safety"),
    ("03", "Requirements"),
    ("04", "Design"),
    ("05", "Interfaces"),
    ("06", "Engineering"),
    ("07", "V_AND_V"),
    ("08", "Prototyping"),
    ("09", "Production_Planning"),
    ("10", "Certification"),
    ("11", "EIS_Versions_Tags"),
    ("12", "Services"),
    ("13", "Subsystems_Components"),
    ("14", "Ops_Std_Sustain"),
]

# Cross-ATA buckets
CROSS_ATA_BUCKETS = [
    ("10", "Operations", "Operational use, turnarounds, procedures"),
    ("20", "Subsystems", "Functional subsystems (design-driven)"),
    ("30", "Circularity", "Sustainability, LCA, reuse/recycle, DPP links"),
    ("40", "Software", "SW, control logic, diagnostics, ML/NN"),
    ("50", "Structures", "Frames, housings, mounts, structural routes"),
    ("60", "Storages", "Tanks, reservoirs, accumulators, cryo vessels"),
    ("70", "Propulsion", "Propulsive interfaces/couplings"),
    ("80", "Energy", "Electrical/thermal energy interactions"),
    ("90", "Tables_Schemas_Diagrams", "Tables, data dicts, catalogs, SDS/training"),
]

# Engineering cycle folders
ENGINEERING_CYCLE = [
    ("00_PRE-CAD_Prompt_Engineering", [
        "PROMPTS",
        "CONTEXT",
        "AGENTS",
        "SPECS",
        "TRACE",
    ]),
    ("10_CAD", [
        "WORKSPACE",
        "MASTERS",
        "COMPONENTS",
        "EXPORTS",
        "DRAWINGS",
        "META",
    ]),
    ("20_CAE", [
        "MESHES",
        "SCENARIOS",
        "RESULTS",
        "REPORTS",
        "META",
    ]),
    ("30_CAM", [
        "PROCESS_PLANS",
        "G-CODE",
        "3D_PRINT",
        "BOM",
        "TOOLING",
        "META",
    ]),
    ("40_CAOS", [
        "MANUALS",
        "PROCEDURES",
        "DIGITAL_TWINS",
        "AI_AGENTS",
        "SPARES",
        "META",
    ]),
]


# ============================================================================
# TEMPLATE FILES
# ============================================================================

def get_readme_content(path_context: str, description: str) -> str:
    """Generate README.md content for a folder."""
    return f"""# {path_context}

{description}

---

**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
**Standard:** OPT-IN Framework v1.1 / AMPEL360 Space-T  
**Status:** Placeholder - To Be Populated

## Contents

_This folder is part of the AMPEL360 Space-T documentation structure._

## References

- OPT-IN Framework Standard v1.1
- ATA iSpec 2200 (Space-T Adaptation)
- DO-178C / DO-254 / ECSS-E-ST-40C
"""


def get_na_readme(system_code: str, bucket_name: str) -> str:
    """Generate README for N/A buckets."""
    return f"""# {system_code}-{bucket_name}

## Status: Not Applicable

This bucket is not applicable for ATA {system_code} system.

### Rationale

_[Document specific reason why this bucket doesn't apply to this system]_

---

**Note:** Per OPT-IN Framework v1.1, all buckets must exist even if N/A.
Do not remove this folder.
"""


def get_artifact_template(artifact_id: str, system_id: str, subsystem_id: str, cycle: str) -> str:
    """Generate artifact header template."""
    return f"""---
artifact_id: {artifact_id}
system_id: {system_id}
subsystem_id: {subsystem_id}
cycle: {cycle}
source_prompt_ids: []
status: DRAFT
version: v0.1
created: {datetime.now().strftime('%Y-%m-%d')}
compliance_refs:
  - DO-178C
  - ECSS-E-ST-40C
---

# {artifact_id}

## Purpose

_[Describe the purpose of this artifact]_

## Content

_[Main content goes here]_

## Traceability

| Source   | Reference                      |
|:---------|:-------------------------------|
| Prompt   | _[Link to source prompt]_      |
| Upstream | _[Link to upstream artifact]_ |

---

**End of Document**
"""


def get_traceability_csv_header() -> str:
    """Generate traceability matrix CSV header."""
    return """artifact_id,system_id,subsystem_id,cycle,source_prompt_ids,status,version,created,compliance_refs
# AMPEL360 Space-T Traceability Matrix
# Format: ST-XX-YY-C-NNNN format
# Cycles: P=Prompting, D=CAD, E=CAE, M=CAM, O=CAOS
"""


def get_agent_config_template(agent_type: str) -> str:
    """Generate AI agent configuration template."""
    return f"""# {agent_type} Agent Configuration
# AMPEL360 Space-T / CAOS Integration

agent_type: {agent_type}
version: "1.0"
created: {datetime.now().strftime('%Y-%m-%d')}

# Agent Profile
profile:
  name: "{agent_type}_Agent"
  role: "Generative engineering assistant"
  capabilities:
    - geometry_generation
    - requirements_analysis
    - compliance_checking
  
# Input Sources
inputs:
  prompts_dir: "../PROMPTS/"
  context_dir: "../CONTEXT/"
  specs_dir: "../SPECS/"

# Output Configuration
outputs:
  format: "native"
  validation: true
  trace_links: true

# Quality Gates
quality:
  min_confidence: 0.85
  compliance_check: true
  review_required: true
"""


# ============================================================================
# STRUCTURE GENERATION
# ============================================================================

def create_dir(path: Path) -> None:
    """Create directory if it doesn't exist."""
    path.mkdir(parents=True, exist_ok=True)


def write_file(path: Path, content: str) -> None:
    """Write content to file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding='utf-8')


def generate_lifecycle_folders(base_path: Path, system_code: str) -> None:
    """Generate the 14-folder lifecycle structure under XX-00_GENERAL."""
    general_path = base_path / f"{system_code}-00_GENERAL"
    
    for num, name in LIFECYCLE_FOLDERS:
        folder_path = general_path / f"{system_code}-00-{num}_{name}"
        create_dir(folder_path)
        write_file(
            folder_path / "README.md",
            get_readme_content(
                f"{system_code}-00-{num} {name}",
                f"Lifecycle phase {num}: {name.replace('_', ' ')}"
            )
        )


def generate_engineering_cycle(base_path: Path, system_code: str, subsystem_code: str, subsystem_name: str) -> None:
    """Generate P→CAD→CAE→CAM→CAOS cycle structure for a subsystem."""
    subsystem_path = base_path / f"{system_code}-20-{subsystem_code}_{subsystem_name}"
    
    # Create index
    write_file(
        subsystem_path / "00_INDEX_README.md",
        get_readme_content(
            f"Subsystem {system_code}-20-{subsystem_code}: {subsystem_name}",
            f"Engineering cycle workspace for {subsystem_name.replace('_', ' ')}"
        )
    )
    
    # Create engineering cycle folders
    for cycle_folder, subfolders in ENGINEERING_CYCLE:
        cycle_path = subsystem_path / cycle_folder
        create_dir(cycle_path)
        
        for subfolder in subfolders:
            subfolder_path = cycle_path / subfolder
            create_dir(subfolder_path)
            write_file(
                subfolder_path / "README.md",
                get_readme_content(
                    f"{cycle_folder}/{subfolder}",
                    f"Workspace for {subfolder.replace('_', ' ').lower()}"
                )
            )
        
        # Add specific templates
        if cycle_folder == "00_PRE-CAD_Prompt_Engineering":
            # Agent configs
            for agent in ["CAD", "CAE", "CAOS"]:
                write_file(
                    cycle_path / "AGENTS" / f"{agent}_Agent_Config.yaml",
                    get_agent_config_template(agent)
                )
            # Trace template
            write_file(
                cycle_path / "TRACE" / "Prompt_to_Artifact_Map.csv",
                get_traceability_csv_header()
            )
    
    # Create META folder with traceability
    meta_path = subsystem_path / "META"
    create_dir(meta_path)
    write_file(
        meta_path / "Traceability_Matrix.csv",
        get_traceability_csv_header()
    )
    write_file(
        meta_path / "Dependencies.yaml",
        f"""# Dependencies for {system_code}-20-{subsystem_code}_{subsystem_name}
# Cross-subsystem and cross-system dependencies

dependencies:
  upstream: []
  downstream: []
  interfaces: []
"""
    )


def generate_cross_ata_buckets(base_path: Path, system_code: str, system_name: str) -> None:
    """Generate cross-ATA root buckets (10-90)."""
    for bucket_code, bucket_name, description in CROSS_ATA_BUCKETS:
        bucket_path = base_path / f"{system_code}-{bucket_code}_{bucket_name}"
        create_dir(bucket_path)
        
        if bucket_code == "20":  # Subsystems - add engineering cycle
            # Check if we have default subsystems for this system
            if system_code in DEFAULT_SUBSYSTEMS:
                for sub_code, sub_name in DEFAULT_SUBSYSTEMS[system_code]:
                    generate_engineering_cycle(base_path, system_code, sub_code, sub_name)
            else:
                # Create placeholder subsystem
                generate_engineering_cycle(base_path, system_code, "01", "Primary_Subsystem")
        else:
            # Standard bucket with README
            write_file(
                bucket_path / "README.md",
                get_readme_content(
                    f"{system_code}-{bucket_code} {bucket_name}",
                    description
                )
            )


def generate_system(root_path: Path, system_code: str, system_name: str, system_desc: str) -> None:
    """Generate complete ATA system structure."""
    system_path = root_path / f"ATA_{system_code}-{system_name}"
    create_dir(system_path)
    
    # 1. Generate XX-00_GENERAL with 14 lifecycle folders
    generate_lifecycle_folders(system_path, system_code)
    
    # 2. Generate cross-ATA buckets
    generate_cross_ata_buckets(system_path, system_code, system_name)
    
    # 3. Create system META folder
    meta_path = system_path / "META"
    create_dir(meta_path)
    write_file(
        meta_path / f"{system_code}-xx_System_Registry.yaml",
        f"""# System Registry: ATA {system_code} - {system_name}
# {system_desc}

system:
  code: "{system_code}"
  name: "{system_name}"
  description: "{system_desc}"
  created: {datetime.now().strftime('%Y-%m-%d')}
  status: ACTIVE

subsystems: []
# Add subsystem entries as they are populated

interfaces: []
# Add interface definitions

compliance:
  standards:
    - DO-178C
    - DO-254
    - ECSS-E-ST-40C
  dal_level: TBD
"""
    )
    write_file(
        meta_path / f"{system_code}-xx_Traceability_Map.csv",
        get_traceability_csv_header()
    )
    
    print(f"  ✓ Generated ATA_{system_code}-{system_name}")


def generate_opt_in_structure(root_path: Path) -> None:
    """Generate top-level OPT-IN axis structure."""
    axes = [
        ("O-ORGANIZATION", "Governance, standards, program office, stakeholders"),
        ("P-PROGRAM", "Lifecycle phases, milestones, reviews, deliverables"),
        ("T-TECHNOLOGY_ONBOARD_SYSTEMS", "All ATA chapters reside here"),
        ("I-INFRASTRUCTURES", "Ground systems, launch, H₂ value chains, facilities"),
        ("N-NEURAL_NETWORKS_DPP_TRACEABILITY", "AI ops, Digital Product Passport, neural governance"),
    ]
    
    for axis_name, axis_desc in axes:
        axis_path = root_path / axis_name
        create_dir(axis_path)
        write_file(
            axis_path / "README.md",
            get_readme_content(axis_name, axis_desc)
        )
    
    print("✓ Generated OPT-IN axis structure")


def main():
    parser = argparse.ArgumentParser(
        description="AMPEL360 Space-T Directory Structure Generator"
    )
    parser.add_argument(
        "--root",
        type=str,
        default="./AMPEL360_SPACE-T",
        help="Root directory for structure generation"
    )
    parser.add_argument(
        "--systems",
        type=str,
        default=None,
        help="Comma-separated list of system codes (e.g., '21,22,53,57,95'). Default: all systems"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be created without creating files"
    )
    
    args = parser.parse_args()
    
    root_path = Path(args.root)
    
    # Parse system codes
    if args.systems:
        system_codes = [s.strip() for s in args.systems.split(",") if s.strip()]
    else:
        system_codes = list(SYSTEMS.keys())
    
    print(f"\n{'='*60}")
    print("AMPEL360 Space-T Directory Structure Generator")
    print(f"{'='*60}")
    print(f"Root: {root_path.absolute()}")
    print(f"Systems: {len(system_codes)} chapters")
    print(f"{'='*60}\n")
    
    if args.dry_run:
        print("DRY RUN - No files will be created\n")
        print("Would generate:")
        print(f"  - OPT-IN axis structure (5 axes)")
        print(f"  - {len(system_codes)} ATA chapters")
        print(f"  - 14 lifecycle folders per chapter")
        print(f"  - 9 cross-ATA buckets per chapter")
        print(f"  - Engineering cycle (P→CAD→CAE→CAM→CAOS) per subsystem")
        return
    
    # Create root
    create_dir(root_path)
    
    # Generate OPT-IN structure
    generate_opt_in_structure(root_path)
    
    # Generate systems for all axes
    print("\nGenerating ATA chapters for all OPT-IN axes:")
    
    # T-TECHNOLOGY axis
    tech_path = root_path / "T-TECHNOLOGY_ONBOARD_SYSTEMS"
    print("\n  T-TECHNOLOGY_ONBOARD_SYSTEMS:")
    for code in system_codes:
        if code in SYSTEMS:
            name, desc = SYSTEMS[code]
            generate_system(tech_path, code, name, desc)
        else:
            print(f"    ⚠ Unknown system code: {code}")
    
    # O-ORGANIZATION axis
    org_path = root_path / "O-ORGANIZATION"
    print("\n  O-ORGANIZATION:")
    for code, (name, desc) in O_SYSTEMS.items():
        generate_system(org_path, code, name, desc)
    
    # P-PROGRAM axis
    prog_path = root_path / "P-PROGRAM"
    print("\n  P-PROGRAM:")
    for code, (name, desc) in P_SYSTEMS.items():
        generate_system(prog_path, code, name, desc)
    
    # I-INFRASTRUCTURES axis
    infra_path = root_path / "I-INFRASTRUCTURES"
    print("\n  I-INFRASTRUCTURES:")
    for code, (name, desc) in I_SYSTEMS.items():
        generate_system(infra_path, code, name, desc)
    
    # N-NEURAL_NETWORKS_DPP_TRACEABILITY axis
    neural_path = root_path / "N-NEURAL_NETWORKS_DPP_TRACEABILITY"
    print("\n  N-NEURAL_NETWORKS_DPP_TRACEABILITY:")
    for code, (name, desc) in N_SYSTEMS.items():
        generate_system(neural_path, code, name, desc)
    
    # Summary
    total_systems = len(system_codes) + len(O_SYSTEMS) + len(P_SYSTEMS) + len(I_SYSTEMS) + len(N_SYSTEMS)
    print(f"\n{'='*60}")
    print("GENERATION COMPLETE")
    print(f"{'='*60}")
    print(f"Root: {root_path.absolute()}")
    print(f"T-TECHNOLOGY chapters: {len(system_codes)}")
    print(f"O-ORGANIZATION chapters: {len(O_SYSTEMS)}")
    print(f"P-PROGRAM chapters: {len(P_SYSTEMS)}")
    print(f"I-INFRASTRUCTURES chapters: {len(I_SYSTEMS)}")
    print(f"N-NEURAL chapters: {len(N_SYSTEMS)}")
    print(f"Total chapters: {total_systems}")
    print(f"\nNext steps:")
    print("  1. Review generated structure")
    print("  2. Populate README.md files with specific content")
    print("  3. Add engineering artifacts following ST-XX-YY-C-NNNN convention")
    print("  4. Configure CI validation scripts")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
