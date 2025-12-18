---
title: "Catalog: ATA Master Relations Table"
type: CAT
project: "AMPEL360"
program: "SPACET"
family: "Q10"
variant: "GEN"
version: "PLUS"
model: "BB"
block: "B30"
phase: "LC01"
knot_task: "K06"
aor: "CM"
catalog_type: "Master Relations"
status: Active
date: "2025-12-18"
owner: "Configuration Management WG"
---

# Catalog: ATA Master Relations Table

## 1. Catalog Overview

### 1.1 Purpose

This catalog documents the **ATA Master Relations Table**, which serves as the Single Source of Truth (SSOT) for:

- **ATA chapter relationships** across all 117 chapters (ATA 00-116)
- **Domain mappings** to OPTINS Framework axes (P, O, I, T, N, S)
- **Area of Responsibility (AoR)** assignments for each ATA chapter
- **Stakeholder cross-dependencies** (STK interfaces)
- **Agency/context mappings** for regulatory and operational contexts
- **Knot applicability** (K01-K14) for each ATA chapter

This master table is essential for:
- Configuration management and governance
- Stakeholder coordination and interface management
- Traceability and change impact analysis
- Compliance and certification planning
- Data governance and schema validation

### 1.2 Scope

The catalog covers all 117 ATA chapters organized across the OPTINS Framework axes:

- **P-PROGRAM (O Axis):** General governance and reserved chapters (00-19)
- **O-OPS/ORG:** Operational organization and procedures
- **I-INFRASTRUCTURES:** Infrastructure and support systems (80-89)
- **T-TECHNOLOGY:** Onboard technology systems (20-79)
- **N-NEURAL_NETWORKS:** Registries, SSOT, and ledgers (90-99)
- **T-SIMTEST (S Axis):** Simulation and testing systems (100-116)

### 1.3 Organization

The catalog is organized by:
1. **ATA chapter number** (00-116)
2. **Domain axis** (P/O/I/T/N/S)
3. **Primary AoR** (Area of Responsibility)
4. **Cross-dependencies** with other stakeholders

The complete structured data is maintained in:
`config/database/ata_master_relations_table.yaml`

## 2. Master Table Structure

### 2.1 Data Schema

Each ATA chapter entry contains:

| Field | Description | Example |
| :--- | :--- | :--- |
| **ata** | ATA chapter number | "27" |
| **description** | Human-readable chapter name | "FLIGHT CONTROLS" |
| **domain** | OPTINS axis classification | "T-TECHNOLOGY" |
| **aor** | Primary Area of Responsibility | "PHM" |
| **stks** | Cross-dependent stakeholders | ["SE", "SPE", "SAF"] |
| **agencies** | Context/regulatory tags | ["ACTUATION", "REDUNDANCY"] |
| **knots** | Applicable knot numbers | ["K01", "K05", "K07"] |
| **notes** | Additional guidance | "Actuation/servos/surfaces..." |

### 2.2 Stakeholder Abbreviations

| Code | Full Name | Portal Directory |
| :--- | :--- | :--- |
| CM | Configuration Management | STK_CM-cm-configuration-management |
| PMO | Program Management Office | STK_PMO-pmo-program-management-office |
| SE | Systems Engineering | STK_SE-se-systems-engineering |
| SAF | Safety | STK_SAF-saf-safety |
| CERT | Certification & Authorities | STK_CERT-cert-certification-authorities |
| OPS | Operations | STK_OPS-ops-operations |
| SPACEPORT | Spaceport/Airport Operations | STK_SPACEPORT-spaceport-spaceport-airport-ops |
| MRO | MRO / Maintenance | STK_MRO-mro-mro-maintenance |
| DAB | Digital Applications and Blockchains | STK_DAB-dab-digital-applications-blockchains |
| AI | AI/ML Engineering | STK_AI-ai-ai-ml-engineering |
| CY | Cybersecurity | STK_CY-cy-cybersecurity |
| TEST | IVVQ / Testing | STK_TEST-test-ivvq-testing |
| PHM | Physical Hardware & Materials | STK_PHM-phm-physical-hardware |


## 3. Catalog Entries by Domain Axis

### 3.1 P-PROGRAM / O-OPS/ORG (ATA 00-19)

#### ATA 00: GENERAL
- **Domain:** P-PROGRAM
- **AoR:** CM
- **STKs:** PMO, SE, SAF, CERT, DATA
- **Agencies:** PROG_GOV, CM, PMO, DATA_GOV, AUDIT
- **Knots:** K01, K04, K06, K10
- **Notes:** Program governance baseline (nomenclature, CC, registers). Foundation for all other ATAs.

#### ATA 01-04: OPERATIONS/ORGANIZATION (RESERVED)
- **Domain:** O-OPS/ORG
- **AoR:** OPS
- **STKs:** SAF, CERT, CM, SPACEPORT
- **Notes:** Reserved for operational policy, organization, support information, and operational limits.

#### ATA 05: TIME LIMITS / MAINTENANCE CHECKS
- **Domain:** O-OPS/ORG
- **AoR:** MRO
- **STKs:** CM, OPS, SAF, CERT, DATA
- **Agencies:** MRO_PLANS, MSG3_LIKE
- **Knots:** K01, K04, K05, K11
- **Notes:** Time limits, checks, intervals, escalations. Critical for safety and availability.

#### ATA 06: DIMENSIONS AND AREAS
- **Domain:** T-TECHNOLOGY
- **AoR:** PHM
- **STKs:** SE, CERT, TEST, DATA
- **Agencies:** GEOMETRY, AREAS, MASS_PROP
- **Knots:** K01, K05, K06
- **Notes:** Reference geometry, areas, envelopes for downstream validation.

#### ATA 07-12: INFRASTRUCTURE SUPPORT
- **Domain:** I-INFRASTRUCTURES
- **AoRs:** MRO, OPS, PHM
- **Notes:** Ground support equipment, servicing, storage, and operational procedures.

#### ATA 18: NOISE & VIBRATION MANAGEMENT
- **Domain:** O-OPS/ORG
- **AoR:** SAF
- **STKs:** OPS, CERT, TEST, SE, PHM, SPACEPORT
- **Agencies:** NVH, ENV, MONITORING
- **Knots:** K01, K05, K12
- **Notes:** NVH constraints/monitoring/mitigation.

### 3.2 T-TECHNOLOGY (ATA 20-79)

**Onboard technology systems including:**

#### Environmental & Life Support (ATA 20-21, 30, 35-38)
- **ATA 21:** AIR CONDITIONING / ENVIRONMENTAL CONTROL
  - **AoR:** PHM | **STKs:** SE, SAF, CERT, TEST, DATA, SPE
  - **Agencies:** ECLSS, ECS, THERMAL | **Knots:** K01, K03, K05, K06

#### Guidance, Navigation & Control (ATA 22, 27, 34)
- **ATA 22:** AUTO FLIGHT / GNC
  - **AoR:** SPE | **STKs:** SE, AI, SAF, CERT, TEST, OPS, CY, DATA, PHM
  - **Agencies:** GNC, AUTONOMY, FDIR | **Knots:** K01, K05, K07, K13

- **ATA 27:** FLIGHT CONTROLS
  - **AoR:** PHM | **STKs:** SE, SPE, SAF, CERT, TEST, DATA, CY
  - **Agencies:** ACTUATION, REDUNDANCY | **Knots:** K01, K05, K07

#### Communications & Data (ATA 23, 31, 45-46)
- **ATA 23:** COMMUNICATIONS
  - **AoR:** SPE | **STKs:** SE, CY, OPS, CERT, TEST, DATA, SPACEPORT
  - **Agencies:** COMMS, TT&C, LINK_BUDGET | **Knots:** K01, K05, K09, K13

#### Power & Propulsion (ATA 24, 28-29, 70-79)
- **ATA 24:** ELECTRICAL POWER
  - **AoR:** PHM | **STKs:** SE, SAF, CERT, TEST, MRO, DATA, SPE
  - **Agencies:** EPOWER, HVDC, EMC | **Knots:** K01, K03, K05

- **ATA 28:** FUEL / PROPELLANT SYSTEMS
  - **AoR:** PHM | **STKs:** SE, SAF, CERT, OPS, SPACEPORT, TEST, DATA, SPE
  - **Agencies:** TECH_PROP, HAZARDS | **Knots:** K01, K03, K05, K09

- **ATA 71-79:** PROPULSION INTEGRATION & ENGINE SYSTEMS
  - **AoRs:** SE (Integration), PHM (Hardware), SPE (Control)
  - **Notes:** Complete propulsion integration, control, and indication systems.

#### Structures (ATA 51-57)
- **ATA 51:** STANDARD PRACTICES & STRUCTURES - GENERAL
- **ATA 52:** DOORS / HATCHES
- **ATA 53:** FUSELAGE / PRESSURE VESSEL
- **ATA 54:** NACELLES / PYLONS
- **ATA 55:** STABILIZERS / CONTROL SURFACES
- **ATA 56:** WINDOWS / VIEWPORTS
- **ATA 57:** WINGS / LIFTING SURFACES
- **Common:** AoR: PHM | Agencies: Structural practices, loads, materials

#### Safety Systems (ATA 26, 47)
- **ATA 26:** FIRE PROTECTION
  - **AoR:** SAF | **STKs:** PHM, SE, SPE, CERT, OPS, TEST
  - **Agencies:** FIRE_SAFETY, HAZARDS | **Knots:** K01, K03, K05

### 3.3 I-INFRASTRUCTURES (ATA 80-89)

#### Off-Board Infrastructure Master (ATA 80)
- **AoR:** SPACEPORT
- **STKs:** OPS, SAF, CERT, CM, DATA
- **Agencies:** SPACEPORT_MASTER
- **Knots:** K01, K02, K09, K10
- **Notes:** Master off-board infra baseline (Spaceport/Airport).

#### Energy & Services (ATA 81)
- **AoR:** SPACEPORT
- **STKs:** SAF, OPS, CERT, PHM, MRO
- **Agencies:** CRYO, ENERGY_SERVICES
- **Knots:** K02, K03, K09

#### MRO Facilities (ATA 82)
- **AoR:** MRO
- **STKs:** OPS, SAF, CM, DATA
- **Agencies:** MRO_FACILITIES, TOOLING
- **Knots:** K02, K04, K11

#### Digital & Cyber Infrastructure (ATA 83, 86-87)
- **ATA 83:** GROUND COMMS / DATA EXCHANGE
- **ATA 86:** OFF-BOARD DIGITAL SERVICES PLATFORM
- **ATA 87:** IDENTITY / ACCESS / CYBERSECURITY INFRA
- **AoRs:** DATA (83, 86), CY (87)
- **Common:** Cyber-required, data governance integration

#### Safety & Emergency (ATA 84)
- **AoR:** SAF
- **STKs:** SPACEPORT, OPS, CERT, TEST
- **Agencies:** EMERGENCY_RESPONSE
- **Knots:** K02, K03, K09, K10

#### Circularity & Sustainability (ATA 85)
- **AoR:** DATA
- **STKs:** PMO, CM, OPS, SPACEPORT
- **Agencies:** CIRCULARITY, LEDGERS
- **Knots:** K01, K06, K14

#### Asset Management & Test Infrastructure (ATA 88-89)
- **ATA 88:** GSE CONFIGURATION / ASSET MANAGEMENT
  - **AoR:** CM
- **ATA 89:** TEST RIGS / INSTRUMENTATION INFRA
  - **AoR:** TEST

### 3.4 N-NEURAL_NETWORKS (ATA 90-99)

**Registries, SSOT, and Ledgers**

#### AI/ML Governance (ATA 90, 96)
- **ATA 90:** AI/ML MODEL REGISTRY & MODEL LIFECYCLE
  - **AoR:** AI | **STKs:** DATA, CM, CERT, OPS, CY, TEST, SPE
  - **Agencies:** MODEL_REGISTRY, GOV | **Knots:** K01, K06, K07

- **ATA 96:** AI GOVERNANCE
  - **AoR:** AI | **STKs:** SAF, CERT, OPS, CY, DATA, CM, SPE
  - **Agencies:** AI_RISK, ASSURANCE | **Knots:** K01, K07, K13

#### Data Schemas & Ontologies (ATA 91)
- **AoR:** DATA
- **STKs:** CM, SE, CY, CERT, TEST
- **Agencies:** ONTOLOGIES, SSOT
- **Knots:** K01, K06, K13
- **Notes:** Ontologies/SSOT for validation and trace.

#### Connectivity & Traceability (ATA 92-93)
- **ATA 92:** WIRING / CONNECTIVITY GRAPHS
- **ATA 93:** TRACEABILITY GRAPH & EVIDENCE LEDGERS
- **AoRs:** DATA (92), CM (93)
- **Notes:** Graph-based traceability and connectivity management.

#### Product Passport & BOM (ATA 94-95)
- **ATA 94:** DPP CORE & PROVENANCE
- **ATA 95:** SBOM / SWHW BOM / MODEL BOM EXPORTS
- **AoR:** DATA
- **STKs:** CM, CERT, CY, OPS, SPE
- **Knots:** K01, K06, K13, K14

#### Change & Release Management (ATA 97-98)
- **ATA 97:** CHANGE IMPACT ANALYTICS
  - **AoR:** DATA | **Knots:** K01, K04, K06

- **ATA 98:** SIGNED RELEASE PACKS / MANIFESTS
  - **AoR:** CM | **Knots:** K01, K04, K08, K13

#### Master Registers (ATA 99)
- **AoR:** DATA
- **STKs:** CM, SE, CERT, TEST
- **Agencies:** MASTER_DATA, REGISTERS
- **Knots:** K01, K06
- **Notes:** Golden registers + reference datasets.

### 3.5 T-SIMTEST (ATA 100-116)

**Simulation and Testing Systems**

#### Test Governance & Configuration (ATA 100-101)
- **ATA 100:** SIM/TEST GOVERNANCE
  - **AoR:** TEST | **Knots:** K01, K05

- **ATA 101:** DIGITAL TWIN CONFIGURATION
  - **AoR:** DATA | **Knots:** K01, K06, K05

#### Test Scenarios & Automation (ATA 102-105)
- **ATA 102:** SCENARIO LIBRARIES
  - **AoR:** OPS | **Knots:** K01, K02, K05

- **ATA 103:** SIL AUTOMATION
  - **AoR:** SPE | **Knots:** K01, K05, K13

- **ATA 104:** HIL BENCHES
  - **AoR:** TEST | **Knots:** K01, K05

- **ATA 105:** PIL / TARGET EXECUTION
  - **AoR:** TEST | **Knots:** K01, K05, K13

#### Test Data & Results (ATA 106-109)
- **ATA 106:** TEST PROCEDURES / CASES
- **ATA 107:** TEST DATA / STIMULI
- **ATA 108:** TEST RESULTS / ANOMALY MANAGEMENT
- **ATA 109:** VV EVIDENCE PACKS
- **AoRs:** TEST (106, 108), DATA (107), CERT (109)

#### Qualification & Compliance Testing (ATA 110-116)
- **ATA 110:** QUALIFICATION / ENVIRONMENTAL TESTING
- **ATA 111:** SYSTEM INTEGRATION TESTING
- **ATA 112:** MISSION/FLIGHT TESTING
- **ATA 113:** UNCERTAINTY QUANTIFICATION
- **ATA 114:** AI/ML VALIDATION SUITES
- **ATA 115:** CERTIFICATION TESTS & COMPLIANCE
- **ATA 116:** SIM/TEST ARCHIVES & BASELINES

## 4. Indexes

### 4.1 By Primary AoR

**CM (Configuration Management):**
- ATA 00, 13-17, 19, 43, 48, 88, 93, 98, 116

**DAB (Digital Applications and Blockchains):**
- ATA 45, 46, 83, 85, 86, 91, 92, 94, 95, 97, 99, 101, 107, 113

**AI (AI/ML Engineering):**
- ATA 90, 96, 114

**CY (Cybersecurity):**
- ATA 87

**TEST (IVVQ / Testing):**
- ATA 89, 100, 104, 105, 106, 108, 110, 111

**CERT (Certification & Authorities):**
- ATA 109, 115

**SAF (Safety):**
- ATA 18, 26, 47, 84

**OPS (Operations):**
- ATA 01-04, 09, 10, 44, 102, 112

**MRO (MRO / Maintenance):**
- ATA 05, 07, 82

**SPACEPORT (Spaceport/Airport Ops):**
- ATA 80, 81

**SE (Systems Engineering):**
- ATA 40, 71

**PHM (Physical Hardware & Materials):**
- ATA 06, 08, 20, 21, 24, 25, 27-38, 49-57, 60-79

**DAB (Digital Applications and Blockchains):**
- ATA 22, 23, 31, 33, 34, 42, 73, 76, 77, 103

### 4.2 By Domain Axis

**P-PROGRAM:**
- ATA 00, 11

**O-OPS/ORG:**
- ATA 01-05, 18

**I-INFRASTRUCTURES:**
- ATA 07, 09, 10, 12, 80-89

**T-TECHNOLOGY:**
- ATA 06, 08, 20-79

**N-NEURAL_NETWORKS:**
- ATA 90-99

**T-SIMTEST:**
- ATA 100-116

### 4.3 By Knot Applicability

**K01 (Certification Authority Basis):**
- All active ATAs (baseline requirement)

**K02 (CONOPS/Mission Phases):**
- ATA 01-04, 07, 09-12, 18, 44, 80-82, 84, 102, 112

**K03 (Hazmat/Cryo/Propellants Safety):**
- ATA 12, 18, 21, 24, 26, 28, 30, 35-36, 47, 49, 72, 74-75, 78-79, 81, 84

**K04 (Integration Boundaries/ICDs):**
- ATA 00, 05, 10, 13-17, 19, 40, 43, 48, 71, 82, 88, 97-98, 116

**K05 (Model Fidelity/Verification Credit):**
- ATA 05-08, 18, 20-24, 26-38, 41-42, 47, 49-57, 60-79, 89, 100-106, 108, 110-111, 114-115

**K06 (Data Governance/SSOT/Schemas):**
- ATA 00, 06, 08, 21, 31, 40, 45-46, 77, 83, 85-88, 90-95, 97, 99, 101, 106-107, 109, 113

**K07 (AI/Autonomy Assurance):**
- ATA 22, 27, 42, 55, 67, 90, 96, 114

**K08 (DPP/SBOM/Provenance):**
- ATA 93-94, 98, 108-109, 116

**K09 (Infrastructure Permitting/Jurisdiction):**
- ATA 12, 23, 28, 71-72, 78, 80-81, 83-84, 89, 110

**K10 (Industrialization/Supply Chain/Quality):**
- ATA 00, 05, 10, 20, 25, 40, 51, 53-54, 57, 60-61, 70, 84, 115

**K11 (Human Factors/Training/Readiness):**
- ATA 01-05, 07-08, 10-12, 18, 25, 29, 32, 35, 38, 44-45, 50, 52, 56, 79, 82, 112

**K12 (NVH Metrics/Corridors/Exposure):**
- ATA 18, 112

**K13 (Cybersecurity Zones/Key Management):**
- ATA 22-23, 31, 34, 39, 42, 45-46, 73, 76, 83, 86-87, 90-91, 94-96, 98, 103, 105, 111, 114-115

**K14 (Reliability Growth/Maintenance Intervals/Health):**
- ATA 85, 94

## 5. Statistics

| Metric | Count |
| :--- | :--- |
| Total ATA Chapters | 117 |
| Active Chapters | 97 |
| Reserved Chapters | 20 |
| Primary Stakeholders | 14 |
| Domain Axes | 6 |
| Knots Defined | 14 |
| Last Updated | 2025-12-18 |

## 6. Usage Guidelines

### 6.1 For Configuration Management

This catalog serves as the master reference for:
- Assigning responsibility for ATA chapters
- Understanding cross-stakeholder dependencies
- Planning configuration control boards
- Managing change impact across domains

### 6.2 For Systems Engineering

Use this catalog to:
- Identify integration boundaries and ICDs
- Map requirements to ATA chapters
- Plan verification and validation activities
- Understand system-of-systems relationships

### 6.3 For Project Management

Reference this catalog for:
- Work breakdown structure alignment
- Stakeholder coordination planning
- Risk identification and mitigation
- Schedule and resource planning

### 6.4 For Data Governance

This catalog enables:
- Schema design aligned with ATA chapters
- Traceability matrix construction
- Data ownership and stewardship
- SSOT validation and quality gates

## 7. Related Artifacts

### 7.1 Configuration Files

- **Master YAML:** `config/database/ata_master_relations_table.yaml`
- **ATA Partition Matrix:** `config/nomenclature/ATA_PARTITION_MATRIX.yaml`
- **Stakeholder Knot Config:** `scripts/stakeholder_knot_config.json`

### 7.2 Documentation

- **Nomenclature Standard:** `docs/standards/NOMENCLATURE_v6_0_R1_0.md`
- **OPTINS Framework:** OPTINS Framework v1.1
- **Knots Catalog:** `00_AMPEL360_SPACET_Q10_CERT_PLUS_BB_GEN_SB90_K01_CERT__knots-catalog_CAT_I01-R02_ACTIVE.json`

### 7.3 Portal Entry Points

Each stakeholder has a dedicated portal directory in `AMPEL360-SPACE-T-PORTAL/`:

- STK_CM-cm-configuration-management
- STK_DATA-data-data-governance
- STK_AI-ai-ai-ml-engineering
- STK_CY-cy-cybersecurity
- STK_TEST-test-ivvq-testing
- [Full list in stakeholder_map section above]

## 8. Maintenance

### 8.1 Update Process

1. **Change Request:** Submit to CM WG with justification
2. **Impact Analysis:** Assess cross-stakeholder impacts
3. **Review:** CM WG + affected stakeholders review
4. **Approval:** CM WG formal approval required
5. **Update:** Update YAML and documentation
6. **Communication:** Notify all stakeholders
7. **Validation:** Verify consistency across related artifacts

### 8.2 Review Cycle

- **Frequency:** Quarterly or on-demand for major changes
- **Owner:** Configuration Management WG
- **Participants:** All stakeholder representatives

### 8.3 Technical Contact

- **Data Owner:** Configuration Management WG
- **Technical Contact:** CM Lead
- **Portal Location:** STK_CM-cm-configuration-management

## 9. References

### 9.1 Standards

- NOMENCLATURE_v6_0_R1_0
- OPTINS Framework v1.1
- ATA iSpec 2200

### 9.2 Related Documents

- ATA Partition Matrix (config/nomenclature/ATA_PARTITION_MATRIX.yaml)
- Stakeholder Knot Configuration (scripts/stakeholder_knot_config.json)
- Knots Catalog (various)
- SSOT Implementation Plans

## 10. Change History

| Version | Date | Changes | Changed By | ATAs Affected |
| :--- | :--- | :--- | :--- | :--- |
| I01-R02 | 2025-12-18 | Initial catalog creation | CM WG | All (00-116) |

---

**Document Control:**
- **Filename:** 00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_B30_LC01_K06_CM__ata-master-relations-table_CAT_I01-R02_ACTIVE.md
- **Location:** Repository root
- **Format:** Markdown (CAT template)
- **Status:** Active
- **Classification:** Internal reference
- **Distribution:** All stakeholders
