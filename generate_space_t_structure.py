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
# Complete ATA 00-116 mapping following OPT-IN Framework Standard v1.1
# Updated: 2025-12-15
# Source: AMPEL360 Space-T Master Table with stakeholder mapping

# T-TECHNOLOGY axis systems (ATA 20-79: main onboard systems)
SYSTEMS = {
    "20": ("STANDARD_PRACTICES_AIRFRAME", "Standard Practices - Airframe"),
    "21": ("AIR_CONDITIONING_ENVIRONMENTAL_CONTROL", "Air Conditioning / Environmental Control"),
    "22": ("AUTO_FLIGHT_GUIDANCE_NAVIGATION_CONTROL", "Auto Flight / Guidance-Navigation-Control"),
    "23": ("COMMUNICATIONS", "Communications"),
    "24": ("ELECTRICAL_POWER", "Electrical Power"),
    "25": ("EQUIPMENT_FURNISHINGS", "Equipment / Furnishings"),
    "26": ("FIRE_PROTECTION", "Fire Protection"),
    "27": ("FLIGHT_CONTROLS", "Flight Controls"),
    "28": ("FUEL_PROPELLANT_SYSTEMS", "Fuel / Propellant Systems"),
    "29": ("HYDRAULIC_POWER", "Hydraulic Power"),
    "30": ("ICE_AND_RAIN_PROTECTION_ATMOSPHERIC_PROTECTION", "Ice and Rain Protection / Atmospheric Protection"),
    "31": ("INDICATING_RECORDING_SYSTEMS", "Indicating / Recording Systems"),
    "32": ("LANDING_GEAR", "Landing Gear"),
    "33": ("LIGHTS", "Lights"),
    "34": ("NAVIGATION", "Navigation"),
    "35": ("OXYGEN_LIFE_SUPPORT_GAS", "Oxygen / Life Support Gas"),
    "36": ("PNEUMATIC_GAS_DISTRIBUTION", "Pneumatic / Gas Distribution"),
    "37": ("VACUUM_IF_APPLICABLE", "Vacuum (if applicable)"),
    "38": ("WATER_WASTE_LIFE_SUPPORT", "Water / Waste (Life Support)"),
    "39": ("ELECTRICAL_ELECTRONIC_PANELS_AND_MULTIPURPOSE_COMPONENTS", "Electrical / Electronic Panels & Multipurpose Components"),
    "40": ("MULTI_SYSTEM_INTEGRATION_SERVICES", "Multi-System / Integration Services"),
    "41": ("WATER_BALLAST_MASS_TRIM_IF_APPLICABLE", "Water Ballast / Mass Trim (if applicable)"),
    "42": ("INTEGRATED_MODULAR_AVIONICS_COMPUTE_PLATFORM", "Integrated Modular Avionics / Compute Platform"),
    "43": ("RESERVED_PLATFORM_INTEGRATION", "Reserved / Platform Integration"),
    "44": ("CABIN_SYSTEMS", "Cabin Systems"),
    "45": ("CENTRAL_MAINTENANCE_SYSTEM_HEALTH_MONITORING", "Central Maintenance System / Health Monitoring"),
    "46": ("INFORMATION_SYSTEMS_DATA_NETWORKS", "Information Systems / Data Networks"),
    "47": ("INERT_GAS_SYSTEM_TANK_INERTING", "Inert Gas System / Tank Inerting"),
    "48": ("IN_FLIGHT_FUEL_DISPENSING_RESERVED", "In-Flight Fuel Dispensing (Reserved)"),
    "49": ("AIRBORNE_AUXILIARY_POWER_APU_AUX_POWER_MODULES", "Airborne Auxiliary Power / APU / Aux Power Modules"),
    "50": ("CARGO_AND_ACCESSORY_COMPARTMENTS", "Cargo and Accessory Compartments"),
    "51": ("STANDARD_PRACTICES_AND_STRUCTURES_GENERAL", "Standard Practices & Structures - General"),
    "52": ("DOORS_HATCHES", "Doors / Hatches"),
    "53": ("FUSELAGE_PRESSURE_VESSEL", "Fuselage / Pressure Vessel"),
    "54": ("NACELLES_PYLONS_IF_APPLICABLE", "Nacelles / Pylons (if applicable)"),
    "55": ("STABILIZERS_CONTROL_SURFACES", "Stabilizers / Control Surfaces"),
    "56": ("WINDOWS_VIEWPORTS", "Windows / Viewports"),
    "57": ("WINGS_LIFTING_SURFACES", "Wings / Lifting Surfaces"),
    "58": ("RESERVED_EXTENSION", "Reserved / Extension"),
    "59": ("RESERVED_EXTENSION", "Reserved / Extension"),
    "60": ("STANDARD_PRACTICES_PROPELLER_ROTOR", "Standard Practices - Propeller / Rotor"),
    "61": ("PROPELLERS_PROPULSORS_IF_APPLICABLE", "Propellers / Propulsors (if applicable)"),
    "62": ("ROTORS_IF_APPLICABLE", "Rotors (if applicable)"),
    "63": ("ROTOR_DRIVES_IF_APPLICABLE", "Rotor Drives (if applicable)"),
    "64": ("TAIL_ROTOR_IF_APPLICABLE", "Tail Rotor (if applicable)"),
    "65": ("TAIL_ROTOR_DRIVE_IF_APPLICABLE", "Tail Rotor Drive (if applicable)"),
    "66": ("FOLDING_BLADES_TAIL_PYLON_IF_APPLICABLE", "Folding Blades / Tail Pylon (if applicable)"),
    "67": ("ROTORS_FLIGHT_CONTROL_IF_APPLICABLE", "Rotors Flight Control (if applicable)"),
    "68": ("RESERVED_EXTENSION", "Reserved / Extension"),
    "69": ("RESERVED_EXTENSION", "Reserved / Extension"),
    "70": ("STANDARD_PRACTICES_ENGINE", "Standard Practices - Engine"),
    "71": ("POWER_PLANT_PROPULSION_INTEGRATION", "Power Plant / Propulsion Integration"),
    "72": ("ENGINE_TURBINE_ROCKET_HYBRID_AS_APPLICABLE", "Engine (Turbine/Rocket/Hybrid as applicable)"),
    "73": ("ENGINE_FUEL_AND_CONTROL", "Engine Fuel and Control"),
    "74": ("IGNITION", "Ignition"),
    "75": ("AIR_BLEED_INLET_APU_AIR_INTAKE", "Air (Bleed / Inlet / APU Air) / Intake"),
    "76": ("ENGINE_CONTROLS", "Engine Controls"),
    "77": ("ENGINE_INDICATING", "Engine Indicating"),
    "78": ("EXHAUST_PLUME_MANAGEMENT", "Exhaust / Plume Management"),
    "79": ("OIL_LUBRICATION", "Oil / Lubrication"),
}

# O-ORGANIZATION axis systems (Operations/Organization)
O_SYSTEMS = {
    "01": ("OPERATIONS_ORGANIZATION_POLICY_RESERVED", "Operations/Organization Policy (Reserved)"),
    "02": ("OPERATIONS_ORGANIZATION_RESERVED", "Operations/Organization (Reserved)"),
    "03": ("SUPPORT_INFORMATION_RESERVED", "Support Information (Reserved)"),
    "04": ("AIRWORTHINESS_LIMITATIONS_OPERATIONAL_LIMITS_RESERVED", "Airworthiness Limitations / Operational Limits (Reserved)"),
    "12": ("SERVICING", "Servicing"),
    "18": ("NOISE_AND_VIBRATION_MANAGEMENT", "Noise & Vibration Management"),
}

# P-PROGRAM axis systems
P_SYSTEMS = {
    "00": ("GENERAL", "General"),
    "05": ("TIME_LIMITS_MAINTENANCE_CHECKS", "Time Limits / Maintenance Checks"),
    "06": ("DIMENSIONS_AND_AREAS", "Dimensions and Areas"),
    "07": ("LIFTING_AND_SHORING", "Lifting and Shoring"),
    "08": ("LEVELING_AND_WEIGHING", "Leveling and Weighing"),
    "09": ("TOWING_AND_TAXIING", "Towing and Taxiing"),
    "10": ("PARKING_MOORING_STORAGE_RETURN_TO_SERVICE", "Parking / Mooring / Storage / Return to Service"),
    "11": ("PLACARDS_AND_MARKINGS", "Placards and Markings"),
}

# I-INFRASTRUCTURES axis systems
I_SYSTEMS = {
    "80": ("OFF_BOARD_AIRPORT_SPACEPORT_INFRASTRUCTURES_MASTER", "Off-Board / Airport / Spaceport Infrastructures (Master)"),
    "81": ("OFF_BOARD_ENERGY_CRYO_SERVICES", "Off-Board Energy / Cryo Services"),
    "82": ("OFF_BOARD_MRO_FACILITIES_TOOLING_LOGISTICS", "Off-Board MRO Facilities / Tooling / Logistics"),
    "83": ("GROUND_COMMS_DATA_EXCHANGE_INFRA_GATEWAYS_EDGE", "Ground Comms / Data Exchange Infra (Gateways, Edge)"),
    "84": ("SPACEPORT_SAFETY_EMERGENCY_RESPONSE_INFRA", "Spaceport Safety / Emergency Response Infra"),
    "85": ("CIRCULARITY_INFRA_RETURN_FLOWS_RECYCLING_CO2_H2_LOOPS", "Circularity Infra (Return Flows, Recycling, CO2/H2 Loops)"),
    "86": ("OFF_BOARD_DIGITAL_SERVICES_PLATFORM_PORTALS_ORCHESTRATION", "Off-Board Digital Services Platform (Portals, Orchestration)"),
    "87": ("IDENTITY_ACCESS_CYBERSECURITY_INFRA_PHYSICAL_DIGITAL", "Identity / Access / Cybersecurity Infra (Physical+Digital)"),
    "88": ("GSE_CONFIGURATION_ASSET_MANAGEMENT", "GSE Configuration / Asset Management"),
    "89": ("TEST_RIGS_INSTRUMENTATION_INFRA_GROUND", "Test Rigs / Instrumentation Infra (Ground)"),
}

# N-NEURAL_NETWORKS_DPP_TRACEABILITY axis systems
N_SYSTEMS = {
    "90": ("AI_ML_MODEL_REGISTRY_AND_MODEL_LIFECYCLE", "AI/ML Model Registry & Model Lifecycle"),
    "91": ("DATA_SCHEMAS_ONTOLOGIES_SEMANTIC_MODEL_SSOT", "Data Schemas / Ontologies / Semantic Model (SSOT)"),
    "92": ("WIRING_CONNECTIVITY_GRAPHS_AND_HARNESS_DATA_PACKAGES", "Wiring / Connectivity Graphs & Harness Data Packages"),
    "93": ("TRACEABILITY_GRAPH_REQ_DESIGN_VV_OPS_AND_EVIDENCE_LEDGERS", "Traceability Graph (REQ↔DESIGN↔VV↔OPS) & Evidence Ledgers"),
    "94": ("DPP_CORE_DIGITAL_PRODUCT_PASSPORT_AND_PROVENANCE", "DPP Core (Digital Product Passport) & Provenance"),
    "95": ("SBOM_SWHW_BOM_MODEL_BOM_EXPORTS", "SBOM / SWHW BOM / Model BOM Exports"),
    "96": ("AI_GOVERNANCE_RISK_ASSURANCE_MONITORING_DRIFT_BIAS", "AI Governance (Risk, Assurance, Monitoring, Drift/Bias)"),
    "97": ("CHANGE_IMPACT_ANALYTICS_WIRING_CONFIG_TRACE", "Change Impact Analytics (Wiring/Config/Trace)"),
    "98": ("SIGNED_RELEASE_PACKS_MANIFESTS_EXPORTS", "Signed Release Packs / Manifests / Exports"),
    "99": ("MASTER_REGISTERS_GOLDEN_RECORDS_AND_REFERENCE_DATASETS", "Master Registers (Golden Records) & Reference Datasets"),
}

# SIMTEST axis systems (ATA 100-116: simulation/test governance)
SIMTEST_SYSTEMS = {
    "100": ("SIM_TEST_GOVERNANCE_PLANS_ENVIRONMENTS_QUALITY", "Simulation/Test Governance (Plans, Environments, Quality)"),
    "101": ("DIGITAL_TWIN_CONFIGURATION_AND_SIM_MODEL_CATALOG", "Digital Twin Configuration & Sim Model Catalog"),
    "102": ("SCENARIO_LIBRARIES_MISSION_OFF_NOMINAL_EMERGENCY", "Scenario Libraries (Mission, Off-Nominal, Emergency)"),
    "103": ("SIL_SOFTWARE_IN_THE_LOOP_AUTOMATION", "SIL (Software-in-the-Loop) Automation"),
    "104": ("HIL_HARDWARE_IN_THE_LOOP_BENCHES", "HIL (Hardware-in-the-Loop) Benches"),
    "105": ("PIL_TARGET_EXECUTION_PROCESSOR_PLATFORM_IN_THE_LOOP", "PIL / Target Execution (Processor/Platform-in-the-Loop)"),
    "106": ("TEST_PROCEDURES_TEST_CASES_ACCEPTANCE_CRITERIA", "Test Procedures / Test Cases / Acceptance Criteria"),
    "107": ("TEST_DATA_INPUT_DECKS_STIMULI", "Test Data / Input Decks / Stimuli"),
    "108": ("TEST_RESULTS_REPORTING_ANOMALY_MANAGEMENT", "Test Results / Reporting / Anomaly Management"),
    "109": ("VV_EVIDENCE_PACKS_LINKED_TO_TRACEABILITY", "V&V (Verification and Validation) Evidence Packs (Linked to Traceability)"),
    "110": ("QUALIFICATION_ENVIRONMENTAL_TESTING_SPACE_T", "Qualification / Environmental Testing (Space-T)"),
    "111": ("SYSTEM_INTEGRATION_TESTING_END_TO_END", "System Integration Testing (End-to-End)"),
    "112": ("MISSION_FLIGHT_TESTING_OPERATIONAL_DEMOS", "Mission/Flight Testing (Operational Demos)"),
    "113": ("UNCERTAINTY_QUANTIFICATION_UQ_MONTE_CARLO_SENSITIVITY", "Uncertainty Quantification (UQ) / Monte Carlo / Sensitivity"),
    "114": ("AI_ML_VALIDATION_SUITES_AND_MONITORING_TESTS", "AI/ML Validation Suites & Monitoring Tests"),
    "115": ("CERTIFICATION_TESTS_SW_HW_ECSS_DO_AND_COMPLIANCE_REPORTS", "Certification Tests (SW/HW/ECSS-DO) & Compliance Reports"),
    "116": ("SIM_TEST_ARCHIVES_AND_BASELINES_FROZEN_CAMPAIGNS", "Simulation/Test Archives & Baselines (Frozen Campaigns)"),
}

# NOT ASSIGNED / RESERVED systems (ATA 13-17, 19: for future Space-T tailoring and allocation)
RESERVED_SYSTEMS = {
    "13": ("NOT_ASSIGNED_RESERVED", "Not Assigned / Reserved"),
    "14": ("NOT_ASSIGNED_RESERVED", "Not Assigned / Reserved"),
    "15": ("NOT_ASSIGNED_RESERVED", "Not Assigned / Reserved"),
    "16": ("NOT_ASSIGNED_RESERVED", "Not Assigned / Reserved"),
    "17": ("NOT_ASSIGNED_RESERVED", "Not Assigned / Reserved"),
    "19": ("NOT_ASSIGNED_RESERVED", "Not Assigned / Reserved"),
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
        ("S-SIMTEST", "Simulation and test governance, V&V evidence, qualification"),
        ("R-RESERVED", "Reserved ATA codes for future Space-T tailoring and allocation"),
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
        print(f"  - OPT-IN axis structure (7 axes)")
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
    
    # S-SIMTEST axis
    simtest_path = root_path / "S-SIMTEST"
    print("\n  S-SIMTEST:")
    for code, (name, desc) in SIMTEST_SYSTEMS.items():
        generate_system(simtest_path, code, name, desc)
    
    # R-RESERVED axis (not assigned / reserved for future allocation)
    reserved_path = root_path / "R-RESERVED"
    print("\n  R-RESERVED:")
    for code, (name, desc) in RESERVED_SYSTEMS.items():
        generate_system(reserved_path, code, name, desc)
    
    # Summary
    total_systems = len(system_codes) + len(O_SYSTEMS) + len(P_SYSTEMS) + len(I_SYSTEMS) + len(N_SYSTEMS) + len(SIMTEST_SYSTEMS) + len(RESERVED_SYSTEMS)
    print(f"\n{'='*60}")
    print("GENERATION COMPLETE")
    print(f"{'='*60}")
    print(f"Root: {root_path.absolute()}")
    print(f"T-TECHNOLOGY chapters: {len(system_codes)}")
    print(f"O-ORGANIZATION chapters: {len(O_SYSTEMS)}")
    print(f"P-PROGRAM chapters: {len(P_SYSTEMS)}")
    print(f"I-INFRASTRUCTURES chapters: {len(I_SYSTEMS)}")
    print(f"N-NEURAL chapters: {len(N_SYSTEMS)}")
    print(f"S-SIMTEST chapters: {len(SIMTEST_SYSTEMS)}")
    print(f"R-RESERVED chapters: {len(RESERVED_SYSTEMS)}")
    print(f"Total chapters: {total_systems}")
    print(f"\nNext steps:")
    print("  1. Review generated structure")
    print("  2. Populate README.md files with specific content")
    print("  3. Add engineering artifacts following ST-XX-YY-C-NNNN convention")
    print("  4. Configure CI validation scripts")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
