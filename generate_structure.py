import os
from pathlib import Path

# ==============================================================================
# CONFIGURATION: AMPEL360 SPACE-T MASTER STRUCTURE
# Based on Spec v1.0 (2025-12-09)
# ==============================================================================

ROOT_DIR = "AMPEL360_SPACE-T"

# 1. OPT-IN TOPOLOGY (The Container Axes)
OPT_IN_STRUCTURE = [
    "O-ORGANIZATION",
    "P-PROGRAM",
    "T-TECHNOLOGY_ONBOARD_SYSTEMS/A-AIRFRAME_STRUCTURE",
    "T-TECHNOLOGY_ONBOARD_SYSTEMS/M-MECHANICS_ACTUATION",
    "T-TECHNOLOGY_ONBOARD_SYSTEMS/E1-ENVIRONMENT_ECLSS",
    "T-TECHNOLOGY_ONBOARD_SYSTEMS/D-DATA_RECORDING",
    "T-TECHNOLOGY_ONBOARD_SYSTEMS/E2-ENERGY_POWER",
    "T-TECHNOLOGY_ONBOARD_SYSTEMS/O-OPERATING_SYSTEMS_IMA",
    "T-TECHNOLOGY_ONBOARD_SYSTEMS/P-PROPULSION",
    "T-TECHNOLOGY_ONBOARD_SYSTEMS/E3-ELECTRONICS_AVIONICS",
    "T-TECHNOLOGY_ONBOARD_SYSTEMS/L1-LOGICS_GNC",
    "T-TECHNOLOGY_ONBOARD_SYSTEMS/L2-LINKS_COMMS",
    "T-TECHNOLOGY_ONBOARD_SYSTEMS/I-INFORMATION_INTERFACES",
    "T-TECHNOLOGY_ONBOARD_SYSTEMS/C1-COCKPIT_CABIN_CARGO",
    "T-TECHNOLOGY_ONBOARD_SYSTEMS/C2-CIRCULAR_CRYOGENICS",
    "T-TECHNOLOGY_ONBOARD_SYSTEMS/I2-R_AND_D",
    "T-TECHNOLOGY_ONBOARD_SYSTEMS/A2-AERODYNAMICS_AERO",
    "I-INFRASTRUCTURES",
    "N-NEURAL_NETWORKS_DPP_TRACEABILITY"
]

# 2. MASTER SYSTEMS TABLE (Mapping ATA to OPT-IN Axis)
# Format: "ATA_CODE": ("FOLDER_NAME", "OPT_IN_PARENT_PATH")
SYSTEMS_MAP = {
    "21": ("ATA_21-ECLSS", "T-TECHNOLOGY_ONBOARD_SYSTEMS/E1-ENVIRONMENT_ECLSS"),
    "22": ("ATA_22-GNC_AUTOFLIGHT", "T-TECHNOLOGY_ONBOARD_SYSTEMS/L1-LOGICS_GNC"),
    "23": ("ATA_23-COMMS", "T-TECHNOLOGY_ONBOARD_SYSTEMS/L2-LINKS_COMMS"),
    "24": ("ATA_24-EPS_POWER", "T-TECHNOLOGY_ONBOARD_SYSTEMS/E2-ENERGY_POWER"),
    "25": ("ATA_25-HABITAT_INTERIORS", "T-TECHNOLOGY_ONBOARD_SYSTEMS/C1-COCKPIT_CABIN_CARGO"),
    "27": ("ATA_27-FLIGHT_CONTROLS", "T-TECHNOLOGY_ONBOARD_SYSTEMS/M-MECHANICS_ACTUATION"),
    "28": ("ATA_28-PROPULSION_FUEL", "T-TECHNOLOGY_ONBOARD_SYSTEMS/P-PROPULSION"),
    "31": ("ATA_31-AVIONICS_CORE", "T-TECHNOLOGY_ONBOARD_SYSTEMS/E3-ELECTRONICS_AVIONICS"),
    "53": ("ATA_53-STRUCTURE_FUSELAGE", "T-TECHNOLOGY_ONBOARD_SYSTEMS/A-AIRFRAME_STRUCTURE"),
    "57": ("ATA_57-WINGS_LIFTING_BODY", "T-TECHNOLOGY_ONBOARD_SYSTEMS/A-AIRFRAME_STRUCTURE"),
    "85": ("ATA_85-CIRCULARITY_SYSTEMS", "T-TECHNOLOGY_ONBOARD_SYSTEMS/C2-CIRCULAR_CRYOGENICS"),
    "95": ("ATA_95-NEURAL_OPS_AI", "N-NEURAL_NETWORKS_DPP_TRACEABILITY"),
    # Add other ATA chapters here as needed...
}

# 3. LIFECYCLE FOLDERS (XX-00_GENERAL) - The 14 Standard Folders
LIFECYCLE_FOLDERS = [
    "01_Overview", "02_Safety", "03_Requirements", "04_Design", 
    "05_Interfaces", "06_Engineering", "07_V_AND_V", "08_Prototyping",
    "09_Production_Planning", "10_Certification", "11_EIS_Versions_Tags",
    "12_Services", "13_Subsystems_Components", "14_Ops_Std_Sustain"
]

# 4. ROOT BUCKETS (XX-10 to XX-90)
BUCKETS = [
    ("10", "Operations"),
    ("20", "Subsystems"),
    ("30", "Circularity"),
    ("40", "Software"),
    ("50", "Structures"),
    ("60", "Storages"),
    ("70", "Propulsion"),
    ("80", "Energy"),
    ("90", "Tables_Schemas_Diagrams")
]

# 5. THE ENGINEERING CYCLE (P-CAD-CAE-CAM-CAOS)
# Dictionary defining the deep structure of a subsystem
CYCLE_STRUCTURE = {
    "00_PRE-CAD_Prompt_Engineering": ["PROMPTS", "CONTEXT", "AGENTS", "SPECS", "TRACE"],
    "10_CAD": ["WORKSPACE", "MASTERS", "COMPONENTS", "EXPORTS", "DRAWINGS", "META"],
    "20_CAE": ["MESHES", "SCENARIOS", "RESULTS", "REPORTS", "META"],
    "30_CAM": ["PROCESS_PLANS", "G-CODE", "3D_PRINT", "BOM", "TOOLING", "META"],
    "40_CAOS": ["MANUALS", "PROCEDURES", "DIGITAL_TWINS", "AI_AGENTS", "SPARES", "META"],
    "META": [] # Root meta for the subsystem
}

# ==============================================================================
# GENERATOR FUNCTIONS
# ==============================================================================

def create_folder(path: Path, readme_content=None):
    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)
        # print(f"Created: {path}") # Uncomment for verbose output
    
    if readme_content:
        readme = path / "README.md"
        if not readme.exists():
            with open(readme, "w", encoding="utf-8") as f:
                f.write(readme_content)

def generate_opt_in_skeleton():
    print(">>> Building OPT-IN Skeleton...")
    root = Path(ROOT_DIR)
    for axis in OPT_IN_STRUCTURE:
        create_folder(root / axis)

def generate_ata_system(ata_code, folder_name, parent_path):
    print(f"  > Generating System: {folder_name}...")
    base_path = Path(ROOT_DIR) / parent_path / folder_name
    create_folder(base_path)

    # 1. Generate XX-00_GENERAL (Lifecycle)
    general_path = base_path / f"{ata_code}-00_GENERAL"
    create_folder(general_path)
    for folder in LIFECYCLE_FOLDERS:
        sub_path = general_path / f"{ata_code}-00-{folder}"
        create_folder(sub_path, readme_content=f"# {folder.replace('_', ' ')}\nLifecycle artifact storage.")

    # 2. Generate Root Buckets (XX-10 to XX-90)
    for bucket_num, bucket_name in BUCKETS:
        bucket_path = base_path / f"{ata_code}-{bucket_num}_{bucket_name}"
        
        # If it's the Subsystems bucket, we prepare it for deep structures
        if bucket_num == "20":
            create_folder(bucket_path, readme_content="# Functional Subsystems\nContains P-CAD-CAE-CAM-CAOS cycles.")
        else:
            create_folder(bucket_path, readme_content=f"# {bucket_name}\nArtifact container. If N/A, please document why.")
        
    # 3. Generate Metadata
    meta_path = base_path / "META"
    create_folder(meta_path)
    (meta_path / f"{ata_code}-xx_System_Registry.yaml").touch()
    (meta_path / f"{ata_code}-xx_Traceability_Map.csv").touch()

    return base_path

def generate_subsystem_cycle(system_base_path, ata_code, subsystem_num, subsystem_name):
    """
    Generates the P-CAD-CAE-CAM-CAOS cycle for a specific subsystem.
    Target: ATA_XX... / XX-20_Subsystems / XX-20-YY_Name / ...
    """
    subsystems_bucket = system_base_path / f"{ata_code}-20_Subsystems"
    sub_folder_name = f"{ata_code}-{subsystem_num}_{subsystem_name}"
    sub_path = subsystems_bucket / sub_folder_name
    
    print(f"    -> Injecting Cycle into: {sub_folder_name}")
    
    create_folder(sub_path, readme_content=f"# {subsystem_name} Index\nEngineering Cycle Root.")
    (sub_path / "00_INDEX_README.md").touch()

    for phase, subfolders in CYCLE_STRUCTURE.items():
        phase_path = sub_path / phase
        create_folder(phase_path)
        for sub in subfolders:
            create_folder(phase_path / sub)

# ==============================================================================
# EXECUTION
# ==============================================================================

def main():
    print(f"Initializing AMPEL360 Space-T Repository at: ./{ROOT_DIR}")
    
    # 1. Build the OPT-IN Spine
    generate_opt_in_skeleton()

    # 2. Build ATA Chapters defined in the map
    for ata_code, (name, axis) in SYSTEMS_MAP.items():
        sys_path = generate_ata_system(ata_code, name, axis)

        # 3. EXAMPLE SUBSYSTEMS INSTANTIATION
        # Here we manually trigger the cycle generation for known examples from the spec.
        # In the future, you can add more lines here or automate this list.
        
        if ata_code == "21": # ECLSS Examples
            generate_subsystem_cycle(sys_path, "21", "20-01", "Cabin_Atmosphere")
            generate_subsystem_cycle(sys_path, "21", "20-02", "Thermal_Control")
        
        elif ata_code == "53": # Fuselage Examples
            generate_subsystem_cycle(sys_path, "53", "20-01", "Pressure_Vessel")
            generate_subsystem_cycle(sys_path, "53", "20-02", "Heat_Shield_TPS")

        elif ata_code == "95": # AI Ops Examples
            generate_subsystem_cycle(sys_path, "95", "20-01", "Mission_Planner_NN")

    print("\n✅ Initialization Complete. Space-T Directory Structure is ready.")
    print("Run validation scripts (as defined in Spec Sec 10) to verify compliance.")

if __name__ == "__main__":
    main()
