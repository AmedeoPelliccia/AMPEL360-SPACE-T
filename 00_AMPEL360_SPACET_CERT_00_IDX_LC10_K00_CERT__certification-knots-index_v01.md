---
title: "Certification Knots Index"
type: IDX
variant: "CERT"
owner: "Regulatory Affairs / Certification Department"
status: Active
---

# AMPEL360 Space-T Certification Knots Index

## 1. Introduction

### 1.1 Purpose
This index documents all certification knots defined for the AMPEL360 Space-T program. Knots are cross-cutting workflow elements that represent systematic certification and compliance activities spanning multiple ATA systems.

### 1.2 What is a Knot?
A **knot** is a workflow element that:
- Addresses a specific certification or compliance objective
- Affects multiple ATA systems across the vehicle
- Contains ordered task templates with defined inputs/outputs
- Establishes traceability and accountability
- Integrates with the OPT-IN Framework lifecycle phases

Knots provide a systematic approach to managing complex, cross-system certification activities that cannot be adequately addressed within a single ATA system.

### 1.3 Knot Naming Convention
- **Knot ID**: K## (e.g., K01, K02, K03)
- **Title**: kebab-case descriptive name (e.g., certification-authority-basis)
- **Task IDs**: T### (e.g., T001, T002, T003)

## 2. Active Knots Catalog

### 2.1 K01: Certification Authority Basis

**Status:** Active  
**Slug:** authority-model-certification-basis  
**Owner:** Regulatory Affairs / Certification Department  
**Primary AoR:** STK_CERT  
**Lifecycle Phases:** LC02, LC03, LC10

**Purpose:**  
Establishes the certification basis and decision criteria for the Space-T vehicle, defining compliance objectives and mapping them to evidence and verification activities.

**Organizational Structure:**
- **Directory Path:** `KNOTS/K01_authority-model-certification-basis/`
- **Portal Effectivity:** SPACET-INT (internal), SPACET-AUTH (authority pack-ready)
- **Stakeholder Dependencies:** STK_CM, STK_PMO, STK_SE, STK_SAF, STK_DATA

**Focus Areas:**
- Certification basis establishment
- Authority model and decision rights
- Acceptance criteria definition
- Compliance mapping and traceability

**Primary Outputs:** STD, IDX, RPT, TRC

**Affected ATA Systems:** 52 systems across all OPT-IN axes
- O/P Axis: 00, 01, 02, 03, 04, 11, 13-19
- T-Technology: 21, 22, 24-28, 32-35, 38, 42-44, 47, 48, 52, 56, 58, 59, 67-69, 72-74, 76
- N-Neural: 90, 93, 96
- T-SIMTEST: 100, 105, 106, 109, 110, 112, 114, 115

**Task Templates:**
- **T001**: Define Certification Basis and Decision Criteria
  - Inputs: Program requirements, regulations, design concepts
  - Outputs: Certification Basis Document, Special Conditions, ESF justifications
  - Duration: 8-12 weeks
  - Responsible: Certification Manager, Chief Engineer, Regulatory Affairs Manager

- **T002**: Map Compliance Objectives to Evidence and Tests
  - Inputs: Certification Basis, requirements, safety assessments
  - Outputs: Compliance Matrix, Verification Cross-Reference, Evidence Plan
  - Duration: 12-16 weeks
  - Responsible: Certification Manager, System Engineer, Verification Engineer

**Documentation:**
- Detailed Plan: `00_00_PLAN_LC10_CERT_knot-k01-certification-authority-basis_v01.md`
- Data Definition: `00_90_CAT_SB00_CERT_knots-catalog_v01.json`

**Dependencies:** None (foundational knot)

**Related Documents:**
- Certification Basis Document (deliverable from T001)
- Compliance Matrix (deliverable from T002)
- Safety Management System Plan
- Configuration Management Plan

### 2.2 Future Knots (Planned)

The following knots are under development or planned:

- **K02**: System Safety Assessment Workflow (Planned)
- **K03**: Software Certification Process (Planned)
- **K04**: Hardware Certification Process (Planned)
- **K05**: Human Factors Certification (Planned)
- **K06**: Environmental Qualification (Planned)
- **K07**: Supplier Quality Assurance (Planned)
- **K08**: Flight Test Certification (Planned)

## 3. Using Knots in Your ATA System

### 3.1 Identifying Applicable Knots
Each ATA system documentation should identify which knots apply:

```markdown
## Applicable Certification Knots
- **K01**: Certification Authority Basis - Tasks T001, T002
- **K03**: Software Certification Process - Tasks T008, T009 (when K03 is defined)
```

### 3.2 Implementing Knot Tasks
For each applicable knot task:

1. **Review Task Requirements**
   - Read the detailed task description in the knot plan document
   - Understand inputs, outputs, and acceptance criteria

2. **Assign Responsibilities**
   - Identify personnel within your ATA system team
   - Coordinate with knot owner for cross-system activities

3. **Execute Task**
   - Follow the defined process
   - Use specified templates and tools
   - Document results in compliance with nomenclature standard

4. **Deliver Outputs**
   - Create required deliverables using appropriate file naming
   - Submit for review according to knot plan schedule
   - Update traceability matrices

### 3.3 File Naming for Knot Deliverables

Follow the AMPEL360 Nomenclature Standard v1.0:

**Format:**
```
[ROOT]_[BUCKET]_[TYPE]_[LC_OR_SB]_[VARIANT]_[DESCRIPTION]_[VERSION].[EXT]
```

**Examples:**
```
# Certification Basis for ATA 21 (ECLSS)
21_00_PLAN_LC10_CERT_certification-basis_v01.md

# Compliance Matrix for ATA 22 (GNC)
22_00_TRC_LC10_CERT_compliance-matrix_v01.md

# Safety Assessment for ATA 28 (Propulsion)
28_70_FHA_SB00_SYS_propulsion-fha_v01.md
```

### 3.4 Traceability and Reporting

**Maintain Traceability:**
- Link knot tasks to system requirements
- Reference knot IDs and task IDs in deliverables
- Update compliance matrices with knot task completion status

**Reporting:**
- Report knot task status in program reviews
- Flag issues or deviations to knot owner
- Participate in cross-system coordination meetings

## 4. Knot Data Structure

### 4.1 Schema Definition
The complete JSON schema for knots is defined in:
- `00_90_SCH_SB00_GEN_knots-data-structure_v01.json`

### 4.2 Knots Catalog Data
All active knots are documented in machine-readable format:
- `00_90_CAT_SB00_CERT_knots-catalog_v01.json`

This catalog can be used for:
- Automated workflow generation
- Project management tool integration
- Compliance tracking dashboards
- Requirement traceability tools

### 4.3 Schema Validation
Validate knot data files using JSON Schema validators:

```bash
# Python example
python -c "
import json
import jsonschema

with open('00_90_SCH_SB00_GEN_knots-data-structure_v01.json') as f:
    schema = json.load(f)
with open('00_90_CAT_SB00_CERT_knots-catalog_v01.json') as f:
    data = json.load(f)
    
jsonschema.validate(instance=data, schema=schema)
print('Validation successful!')
"
```

## 5. Governance and Change Control

### 5.1 Knot Definition Process
1. **Proposal**: Submit knot proposal to Certification WG
2. **Review**: Technical review and impact assessment
3. **Approval**: Configuration Control Board approval
4. **Implementation**: Create documentation and update catalog
5. **Communication**: Notify all affected ATA system owners

### 5.2 Knot Modification
Changes to existing knots follow change control process:
- Minor changes (clarifications): Document review only
- Major changes (scope, tasks): CCB approval required
- Version control: Increment version numbers appropriately

### 5.3 Knot Status Lifecycle
- **Draft**: Under development, not for operational use
- **Active**: Approved and in use
- **Deprecated**: Being phased out, use discouraged
- **Archived**: Historical record, no longer applicable

## 6. Integration with OPT-IN Framework

### 6.1 Lifecycle Phase Mapping
Knots are mapped to OPT-IN Framework lifecycle phases (LC01-LC14):

| Lifecycle Phase | Typical Knot Activities |
| :--- | :--- |
| LC01: Overview | Knot planning and scoping |
| LC02: Safety | Safety-related knots (K01, K02) |
| LC03: Requirements | Requirements and compliance knots (K01) |
| LC04-LC09: Design/V&V/Production | System-specific knot execution |
| LC10: Certification | Active certification knots (K01, K03, K04) |
| LC11-LC14: Operations | Operational certification maintenance |

### 6.2 Cross-Axis Integration
Knots integrate across OPT-IN axes:
- **O (Organization)**: Policies, procedures, quality systems
- **P (Program)**: Program management and coordination
- **T (Technology)**: Technical systems certification
- **I (Infrastructure)**: Ground support and facilities
- **N (Neural)**: AI/ML certification considerations

## 7. Tools and Automation

### 7.1 Recommended Tools
- **Requirements Management**: DOORS, Jama Connect, Polarion
- **Traceability**: Custom database, IBM Rational DOORS Next
- **Project Management**: Jira, MS Project with certification tracking
- **Document Control**: Git, PLM systems with CM capabilities
- **Compliance Dashboards**: Custom web applications, PowerBI

### 7.2 Automation Opportunities
- Automated compliance matrix generation from requirements
- Traceability link validation
- Evidence package completeness checking
- Status reporting and dashboards
- Alert notifications for task deadlines

## 8. Training and Resources

### 8.1 Required Training
- Certification process overview
- Knot workflow training
- Tool-specific training
- Regulatory standards familiarization

### 8.2 Support Resources
- Certification Working Group meetings (bi-weekly)
- Knot owner office hours
- Documentation repository
- Internal knowledge base

### 8.3 Points of Contact
- **Certification Manager**: [Contact info]
- **Regulatory Affairs Manager**: [Contact info]
- **Configuration Management**: [Contact info]
- **Quality Assurance**: [Contact info]

## 9. References

### 9.1 Internal Documents
- OPT-IN Framework Standard v1.1
- AMPEL360 Nomenclature Standard v1.0
- Configuration Management Plan
- Safety Management System Plan
- Quality Assurance Program Plan

### 9.2 Regulatory Standards
- FAA Part 460 - Human Space Flight Requirements
- EASA CS-SC - Certification Specifications for Space Vehicles
- ECSS-E-ST-10C - System engineering general requirements
- ECSS-Q-ST-40C - Safety
- DO-178C - Software Considerations in Airborne Systems
- DO-254 - Design Assurance Guidance for Airborne Electronic Hardware

### 9.3 Templates
- Planning documents: `templates/PLAN.md`
- Traceability matrices: `templates/TRC.md`
- Safety assessments: `templates/FHA.md`, `templates/PSSA.md`, `templates/SSA.md`

## 10. Revision History

| Version | Date | Author | Changes |
| :--- | :--- | :--- | :--- |
| v01 | 2025-12-15 | AMPEL360 Certification Team | Initial release with K01 |

---

**End of Document**
