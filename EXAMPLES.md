# AMPEL360 Space-T Generator - Usage Examples

## Example 1: Quick Start - Single System

Generate structure for Environmental Control & Life Support System (ECLSS):

```bash
python generate_space_t_structure.py --systems 21
```

**Generated Structure:**
```
AMPEL360_SPACE-T/
├── O-ORGANIZATION/
├── P-PROGRAM/
├── T-TECHNOLOGY_ONBOARD_SYSTEMS/
│   └── ATA_21-ECLSS/
│       ├── 21-00_GENERAL/           # 14 lifecycle folders
│       ├── 21-10_Operations/
│       ├── 21-20_Subsystems/
│       │   ├── 21-20-10_Cabin_Atmosphere/
│       │   │   ├── 00_PRE-CAD_Prompt_Engineering/
│       │   │   ├── 10_CAD/
│       │   │   ├── 20_CAE/
│       │   │   ├── 30_CAM/
│       │   │   ├── 40_CAOS/
│       │   │   └── META/
│       │   ├── 21-20-20_Thermal_Control/
│       │   └── 21-20-30_Humidity_Contamination/
│       ├── 21-30_Circularity/
│       ├── 21-40_Software/
│       ├── 21-50_Structures/
│       ├── 21-60_Storages/
│       ├── 21-70_Propulsion/
│       ├── 21-80_Energy/
│       ├── 21-90_Tables_Schemas_Diagrams/
│       └── META/
├── I-INFRASTRUCTURES/
└── N-NEURAL_NETWORKS_DPP_TRACEABILITY/
```

---

## Example 2: Multi-System Project

Generate structure for a complete spacecraft:

```bash
python generate_space_t_structure.py \
  --root ./SpacecraftProject \
  --systems 21,22,23,24,28,31,53,72,95
```

**Systems Generated:**
- ATA 21: ECLSS (Life Support)
- ATA 22: GNC/Autoflight (Guidance, Navigation, Control)
- ATA 23: Communications
- ATA 24: Electrical Power System
- ATA 28: Propulsion/Fuel
- ATA 31: Avionics Core
- ATA 53: Structure/Fuselage
- ATA 72: Main Engines
- ATA 95: Neural Ops/AI

---

## Example 3: Preview Before Generation

Check what will be created:

```bash
python generate_space_t_structure.py --dry-run --systems 53,57
```

**Output:**
```
============================================================
AMPEL360 Space-T Directory Structure Generator
============================================================
Root: /path/to/AMPEL360_SPACE-T
Systems: 2 chapters
============================================================

DRY RUN - No files will be created

Would generate:
  - OPT-IN axis structure (5 axes)
  - 2 ATA chapters
  - 14 lifecycle folders per chapter
  - 9 cross-ATA buckets per chapter
  - Engineering cycle (P→CAD→CAE→CAM→CAOS) per subsystem
```

---

## Example 4: Full Enterprise Project

Generate complete structure with all 43 systems:

```bash
python generate_space_t_structure.py --root ./AMPEL360_Enterprise
```

**Result:**
- 5 OPT-IN axes
- 43 ATA chapters (complete aerospace system catalog)
- ~600 lifecycle folders (14 per chapter)
- ~400 cross-ATA buckets (9 per chapter)
- ~150 subsystem engineering cycles (for systems with defaults)
- Thousands of template files (READMEs, configs, matrices)

---

## Example 5: Custom Integration

For integration with existing projects:

```bash
# Navigate to existing project
cd /path/to/existing/project

# Generate AMPEL360 structure in subdirectory
python /path/to/generate_space_t_structure.py \
  --root ./documentation/AMPEL360 \
  --systems 21,22,24,31,53
```

---

## Understanding Generated Files

### 1. System Registry (`META/XX-xx_System_Registry.yaml`)

```yaml
system:
  code: "21"
  name: "ECLSS"
  description: "Environmental Control & Life Support System"
  created: 2025-12-11
  status: ACTIVE

subsystems: []
interfaces: []
compliance:
  standards:
    - DO-178C
    - DO-254
    - ECSS-E-ST-40C
  dal_level: TBD
```

### 2. Agent Configuration (`AGENTS/CAD_Agent_Config.yaml`)

```yaml
agent_type: CAD
version: "1.0"
profile:
  name: "CAD_Agent"
  role: "Generative engineering assistant"
  capabilities:
    - geometry_generation
    - requirements_analysis
    - compliance_checking
```

### 3. Traceability Matrix (`TRACE/Prompt_to_Artifact_Map.csv`)

```csv
artifact_id,system_id,subsystem_id,cycle,source_prompt_ids,status,version,created,compliance_refs
# AMPEL360 Space-T Traceability Matrix
# Format: ST-XX-YY-C-NNNN
# Cycles: P=Prompting, D=CAD, E=CAE, M=CAM, O=CAOS
```

---

## Next Steps After Generation

### 1. Initialize Version Control

```bash
cd AMPEL360_SPACE-T
git init
git add .
git commit -m "Initial AMPEL360 Space-T structure"
```

### 2. Customize READMEs

Edit system-specific README files with your project details:
- `T-TECHNOLOGY_ONBOARD_SYSTEMS/ATA_21-ECLSS/README.md`
- `T-TECHNOLOGY_ONBOARD_SYSTEMS/ATA_21-ECLSS/21-00-01_Overview/README.md`

### 3. Populate Engineering Artifacts

Add your design files following the engineering cycle:
```
21-20-10_Cabin_Atmosphere/
  00_PRE-CAD_Prompt_Engineering/PROMPTS/  ← Add design prompts
  10_CAD/WORKSPACE/                        ← Add CAD models
  20_CAE/SCENARIOS/                        ← Add analysis scenarios
  30_CAM/PROCESS_PLANS/                    ← Add manufacturing plans
  40_CAOS/MANUALS/                         ← Add operational manuals
```

### 4. Configure Continuous Integration

Create `.github/workflows/structure-validation.yml` to verify structure integrity.

---

## Common Use Cases

### Use Case 1: Aerospace Startup

```bash
# Small team, focused systems
python generate_space_t_structure.py \
  --root ./NewSpaceStartup \
  --systems 00,21,22,24,28,31,53,72,95
```

### Use Case 2: Research Project

```bash
# Academic research on specific subsystem
python generate_space_t_structure.py \
  --root ./PhD_ECLSS_Research \
  --systems 21
```

### Use Case 3: Digital Twin Development

```bash
# Generate structure for digital twin project
python generate_space_t_structure.py \
  --root ./DigitalTwin_Project \
  --systems 21,22,28,53,72,95
```

### Use Case 4: Compliance Documentation

```bash
# Full structure for certification
python generate_space_t_structure.py \
  --root ./Certification_Package
# Generates all 43 systems for complete compliance documentation
```

---

## Tips & Best Practices

1. **Start Small**: Begin with essential systems, expand as needed
2. **Use Dry Run**: Always preview with `--dry-run` first
3. **Version Control**: Initialize git immediately after generation
4. **Customize Templates**: Edit generated templates to match your project
5. **Maintain Structure**: Don't delete folders, mark as N/A if not applicable
6. **Follow Naming**: Use ST-XX-YY-C-NNNN format for artifacts
7. **Document Decisions**: Use META folders for project-specific documentation

---

## Troubleshooting

### Issue: Too many folders

**Solution**: Use `--systems` flag to generate only needed chapters

### Issue: Structure too complex for small project

**Solution**: Start with minimal systems (21,22,24,31,53) and expand later

### Issue: Need different root location

**Solution**: Use `--root` flag to specify custom path

### Issue: Want to preview changes

**Solution**: Use `--dry-run` flag before actual generation

---

## Version History

- **v1.0** (2025-12-09): Initial release
  - 43 ATA-SpaceT systems
  - 14-folder lifecycle structure
  - P→CAD→CAE→CAM→CAOS engineering cycle
  - OPT-IN Framework v1.1 compliance
