---
title: "Table: ATA Master Relations Quick Reference"
type: TAB
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
table_type: "Quick Reference"
status: Active
date: "2025-12-18"
owner: "Configuration Management WG"
---

# Table: ATA Master Relations Quick Reference

## 1. Table Information

| Field | Details |
| :--- | :--- |
| **Table Name:** | ATA Master Relations Quick Reference |
| **Type:** | Master Reference Table |
| **Purpose:** | Quick reference for ATA chapter relations, domains, stakeholders, and knots |
| **Owner:** | Configuration Management WG |
| **Last Updated:** | 2025-12-18 |
| **Status:** | Active |
| **Data Source:** | config/database/ata_master_relations_table.yaml |

## 2. Table Description

### 2.1 Purpose

This table provides a quick reference view of all ATA chapters with their:
- Domain/axis classification
- Primary Area of Responsibility (AoR) - the main owner/portal entry point
- Cross-dependent stakeholders (STKs) - AoR cross-dependencies
- Agency/context classifications
- Applicable knots (K01-K14)
- Descriptive notes

This format matches the original master table specification and provides an at-a-glance view for:
- Configuration management planning
- Stakeholder coordination
- Work assignment and responsibility mapping
- Interface identification
- Knot applicability assessment

### 2.2 Scope

Complete coverage of all 117 ATA chapters (00-116) across the OPTINS Framework axes.

### 2.3 Update Frequency

On change basis, managed through Configuration Management WG approval process.

## 3. Master Table

### 3.1 Column Definitions

| Column | Description | Values/Format |
| :--- | :--- | :--- |
| **ATA** | ATA chapter number | 00-116 (numeric, zero-padded) |
| **DESCR** | Chapter description | Short descriptive name |
| **DOMAIN** | OPTINS axis classification | P-PROGRAM, O-OPS/ORG, I-INFRASTRUCTURES, T-TECHNOLOGY, N-NEURAL_NETWORKS, T-SIMTEST |
| **AoR** | Primary Area of Responsibility (portal entry point, main owner) | CM, DAB, AI, CY, TEST, CERT, SAF, OPS, MRO, SPACEPORT, SE, PHM, DAB, PMO |
| **STKs** | Cross-dependent stakeholders (AoR cross-dependencies) | Comma-separated stakeholder codes |
| **AGENCY/CONTEXT** | Regulatory/operational context tags | Comma-separated agency/context identifiers |
| **Note** | Additional guidance and knot applicability | Free text with Knots: K##,K##,... |

### 3.2 Quick Reference Table

| ATA | DESCR | DOMAIN | AoR (portal entry points and main owner) | STKs (AoR cross dependencies) | AGENCY/CONTEXT (EG TECH_PROP, ESG, QA...) | Note |
|---:|---|---|---|---|---|---|
| 00 | GENERAL | P-PROGRAM | CM | PMO,SE,SAF,CERT,DAB | PROG_GOV,CM,PMO,DATA_GOV,AUDIT | Program governance baseline (nomenclature, CC, registers). Knots: K01,K04,K06,K10. |
| 01 | OPERATIONS/ORGANIZATION POLICY (RESERVED) | O-OPS/ORG | OPS | SAF,CERT,CM,SPACEPORT | OPS_GOV,CONOPS,TRAINING,READINESS | Ops policy/governance. Knots: K01,K02,K11. |
| 02 | OPERATIONS/ORGANIZATION (RESERVED) | O-OPS/ORG | OPS | SAF,CERT,CM,SPACEPORT | OPS_GOV,CONOPS,READINESS | Ops organization + readiness. Knots: K01,K02,K11. |
| 03 | SUPPORT INFORMATION (RESERVED) | O-OPS/ORG | OPS | SAF,CERT,CM,SPACEPORT | TECHPUBS,OPS_SUPPORT | Support info (procedures/reporting). Knots: K01,K02,K11. |
| 04 | AIRWORTHINESS LIMITATIONS / OPERATIONAL LIMITS (RESERVED) | O-OPS/ORG | OPS | SAF,CERT,CM,SPACEPORT | OPS_LIMITS,SAFETY_LIMITS | Operational limits baseline. Knots: K01,K02,K11. |
| 05 | TIME LIMITS / MAINTENANCE CHECKS | O-OPS/ORG | MRO | CM,OPS,SAF,CERT,DAB | MRO_PLANS,MSG3_LIKE | Time limits, checks, intervals, escalations. Knots: K01,K04,K05,K11. |
| 06 | DIMENSIONS AND AREAS | T-TECHNOLOGY | PHM | SE,CERT,TEST,DAB | GEOMETRY,AREAS,MASS_PROP | Reference geometry, areas, envelopes for downstream validation. Knots: K01,K05,K06. |
| 07 | LIFTING AND SHORING | I-INFRASTRUCTURES | MRO | PHM,SAF,OPS,CERT | GSE,LIFTING,SAFETY | Ground lifting/jacking/shoring requirements & procedures. Knots: K02,K03,K05,K11. |
| 08 | LEVELING AND WEIGHING | T-TECHNOLOGY | PHM | OPS,MRO,TEST,DAB | WEIGHING,CENTER_OF_GRAVITY | Mass properties measurement + leveling methods. Knots: K01,K05,K06,K11. |
| 09 | TOWING AND TAXIING | I-INFRASTRUCTURES | OPS | MRO,SAF,SPACEPORT | GROUND_OPS,TOWING | Tow/taxi ground ops constraints + procedures. Knots: K02,K03,K11. |
| 10 | PARKING / MOORING / STORAGE / RETURN TO SERVICE | I-INFRASTRUCTURES | OPS | MRO,SAF,SPACEPORT,CM | STORAGE,RTS_PROCEDURES | Parking/mooring/storage + RTS checks. Knots: K02,K04,K11. |
| 11 | PLACARDS AND MARKINGS | P-PROGRAM | OPS | MRO,SAF,CERT,CM | OPS_LABELS,HFE,TECHPUBS | Labels/markings governance. Knots: K01,K11. |
| 12 | SERVICING | I-INFRASTRUCTURES | MRO | OPS,SAF,SPACEPORT,CERT | SERVICING,FLUIDS,CRYO | Servicing procedures (fluids/consumables/cryo/prop). Knots: K02,K03,K09,K11. |
| 13 | NOT ASSIGNED / RESERVED | Not Assigned | CM | SE,CERT | TAXONOMY,CM | Reserved (Space-T tailoring). Knots: K01,K04. |
| 14 | NOT ASSIGNED / RESERVED | Not Assigned | CM | SE,CERT | TAXONOMY,CM | Reserved (Space-T tailoring). Knots: K01,K04. |
| 15 | NOT ASSIGNED / RESERVED | Not Assigned | CM | SE,CERT | TAXONOMY,CM | Reserved (Space-T tailoring). Knots: K01,K04. |
| 16 | NOT ASSIGNED / RESERVED | Not Assigned | CM | SE,CERT | TAXONOMY,CM | Reserved (Space-T tailoring). Knots: K01,K04. |
| 17 | NOT ASSIGNED / RESERVED | Not Assigned | CM | SE,CERT | TAXONOMY,CM | Reserved (Space-T tailoring). Knots: K01,K04. |
| 18 | NOISE & VIBRATION MANAGEMENT | O-OPS/ORG | SAF | OPS,CERT,TEST,SE,PHM,SPACEPORT | NVH,ENV,MONITORING | NVH constraints/monitoring/mitigation. Knots: K01,K05,K12. |
| 19 | NOT ASSIGNED / RESERVED | Not Assigned | CM | SE,CERT | TAXONOMY,CM | Reserved (Space-T tailoring). Knots: K01,K04. |
| 20 | STANDARD PRACTICES - AIRFRAME | T-TECHNOLOGY | PHM | SE,SAF,CERT,TEST,DAB | PRACTICES,FASTENERS,REPAIRS | Airframe standard practices, materials, repair methods. Knots: K01,K05,K10. |
| 21 | AIR CONDITIONING / ENVIRONMENTAL CONTROL | T-TECHNOLOGY | PHM | SE,SAF,CERT,TEST,DAB | ECLSS,ECS,THERMAL | ECLSS/ECS physical plant + controls. Knots: K01,K03,K05,K06. |
| 22 | AUTO FLIGHT / GUIDANCE-NAVIGATION-CONTROL | T-TECHNOLOGY | DAB | SE,AI,SAF,CERT,TEST,OPS,CY,DAB,PHM | GNC,AUTONOMY,FDIR | GNC SW/control-law implementation; SE governs architecture. Knots: K01,K05,K07,K13. |
| 23 | COMMUNICATIONS | T-TECHNOLOGY | DAB | SE,CY,OPS,CERT,TEST,DAB,SPACEPORT | COMMS,TT&C,LINK_BUDGET | Comms/TT&C stacks + ICDs + link security. Knots: K01,K05,K09,K13. |
| 24 | ELECTRICAL POWER | T-TECHNOLOGY | PHM | SE,SAF,CERT,TEST,MRO,DAB | EPOWER,HVDC,EMC | Power generation/distribution/protection + monitoring SW. Knots: K01,K03,K05. |
| 25 | EQUIPMENT / FURNISHINGS | T-TECHNOLOGY | PHM | OPS,SAF,CERT,MRO,SE | HFE,CABIN,SAFETY_EQUIP | Interiors/equipment/ergonomics + maintainability. Knots: K01,K10,K11. |
| 26 | FIRE PROTECTION | T-TECHNOLOGY | SAF | PHM,SE,DAB,CERT,OPS,TEST | FIRE_SAFETY,HAZARDS | Detection/suppression, hazard zoning, flammability. Knots: K01,K03,K05. |
| 27 | FLIGHT CONTROLS | T-TECHNOLOGY | PHM | SE,DAB,SAF,CERT,TEST,CY | ACTUATION,REDUNDANCY | Actuation/servos/surfaces; SW control under DAB. Knots: K01,K05,K07. |
| 28 | FUEL / PROPELLANT SYSTEMS | T-TECHNOLOGY | PHM | SE,SAF,CERT,OPS,SPACEPORT,TEST,DAB | TECH_PROP,HAZARDS | Tanks/feeds/venting/leak; spaceport servicing ICDs. Knots: K01,K03,K05,K09. |
| 29 | HYDRAULIC POWER | T-TECHNOLOGY | PHM | SE,SAF,CERT,TEST,MRO,DAB | HYDRAULICS,ACTUATION | Hydraulic generation/distribution/health monitoring. Knots: K01,K05,K11. |
| 30 | ICE AND RAIN PROTECTION / ATMOSPHERIC PROTECTION | T-TECHNOLOGY | PHM | SE,SAF,CERT,TEST,DAB | ENV_PROTECTION,THERMAL | Atmospheric protection (air) or env protection features (space). Knots: K01,K03,K05. |
| 31 | INDICATING / RECORDING SYSTEMS | T-TECHNOLOGY | DAB | SE,CY,CERT,TEST,DAB,OPS | DISPLAYS,LOGGING,RECORDERS | Indication/recording SW + data logging governance. Knots: K01,K06,K13. |
| 32 | LANDING GEAR | T-TECHNOLOGY | PHM | SE,SAF,CERT,TEST,OPS,MRO,DAB | GEAR,LOADS,KINEMATICS | Gear/brakes/steering + deployment logic interfaces. Knots: K01,K05,K11. |
| 33 | LIGHTS | T-TECHNOLOGY | DAB | PHM,SE,OPS,SAF,CERT,SPACEPORT,DAB | LIGHTS,SIGNALING | Lighting control SW + HW integration. Knots: K01,K05. |
| 34 | NAVIGATION | T-TECHNOLOGY | DAB | SE,CY,OPS,CERT,TEST,DAB,AI | NAV,SENSOR_FUSION | Nav sensors fusion + integrity + cyber resilience. Knots: K01,K05,K13. |
| 35 | OXYGEN / LIFE SUPPORT GAS | T-TECHNOLOGY | PHM | OPS,SAF,SE,CERT,MRO,DAB | LS_GAS,EMERGENCY | Breathing gas storage/distribution + emergency procedures. Knots: K01,K03,K11. |
| 36 | PNEUMATIC / GAS DISTRIBUTION | T-TECHNOLOGY | PHM | SE,SAF,CERT,TEST,MRO,DAB | PNEUMATICS,GAS_NETS | Pneumatics/gas distribution, valves, sensors, alarms. Knots: K01,K03,K05. |
| 37 | VACUUM (IF APPLICABLE) | T-TECHNOLOGY | PHM | SE,SAF,CERT,TEST,MRO | VACUUM_SYSTEMS | Vacuum systems where applicable. Knots: K01,K03,K05. |
| 38 | WATER / WASTE (LIFE SUPPORT) | T-TECHNOLOGY | PHM | OPS,SAF,SE,CERT,TEST,DAB | WATER_WASTE,CONTAMINATION | Water/waste loops + hygiene + contamination controls. Knots: K01,K03,K11. |
| 39 | ELECTRICAL / ELECTRONIC PANELS & MULTIPURPOSE COMPONENTS | T-TECHNOLOGY | PHM | SE,CY,CERT,TEST,MRO,DAB | PANELS,LRU_RACKS | Panels/racks/enclosures, harness interfaces, maintainability. Knots: K01,K05,K13. |
| 40 | MULTI-SYSTEM / INTEGRATION SERVICES | T-TECHNOLOGY | SE | CM,CERT,TEST,DAB,CY,PHM | INTEGRATION,ICDS,MBSE | Cross-system integration services + ICD governance. Knots: K01,K04,K06,K10. |
| 41 | WATER BALLAST / MASS TRIM (IF APPLICABLE) | T-TECHNOLOGY | PHM | SE,SAF,TEST,DAB | MASS_TRIM,BALLAST | Ballast/mass trim where applicable. Knots: K01,K05,K06. |
| 42 | INTEGRATED MODULAR AVIONICS / COMPUTE PLATFORM | T-TECHNOLOGY | DAB | CY,SE,SAF,CERT,DAB,TEST,AI | IMA,COMPUTE,PLATFORM | Compute platform SW/toolchains; cyber & partitioning. Knots: K01,K05,K13. |
| 43 | RESERVED / PLATFORM INTEGRATION | T-TECHNOLOGY | CM | SE,CERT,DAB | PLATFORM_POLICY | Reserved platform integration governance. Knots: K01,K04. |
| 44 | CABIN / HABITAT SYSTEMS | T-TECHNOLOGY | OPS | SAF,CERT,SE,PHM,DAB | HABITAT,SERVICES,HFE | Passenger/crew services + ops training integration. Knots: K01,K02,K11. |
| 45 | CENTRAL MAINTENANCE SYSTEM / HEALTH MONITORING | T-TECHNOLOGY | DAB | DAB,MRO,SE,CY,CERT,TEST | PHM_HEALTH,LOGS,DIAG | Health monitoring, diagnostics, maintenance data pipelines. Knots: K01,K06,K11,K13. |
| 46 | INFORMATION SYSTEMS / DAB NETWORKS | T-TECHNOLOGY | DAB | CY,DAB,SE,CERT,TEST,OPS | DATA_NETWORKS,AVIONICS_NETS | Onboard networks + data services; cyber-required. Knots: K01,K06,K13. |
| 47 | INERT GAS SYSTEM / TANK INERTING | T-TECHNOLOGY | SAF | PHM,SE,OPS,CERT,TEST,DAB | INERTING,HAZARDS | Inerting safety system + procedures + validation. Knots: K01,K03,K05. |
| 48 | IN-FLIGHT FUEL DISPENSING (RESERVED) | T-TECHNOLOGY | CM | SE,SAF,CERT,DAB,PHM | APPLICABILITY | Reserved; activate only if applicable. Knots: K01,K04. |
| 49 | AIRBORNE AUXILIARY POWER / APU / AUX POWER MODULES | T-TECHNOLOGY | PHM | SE,SAF,CERT,TEST,MRO,DAB | AUX_POWER,START,SAFETY | Auxiliary power modules (as applicable). Knots: K01,K03,K05. |
| 50 | CARGO AND ACCESSORY COMPARTMENTS | T-TECHNOLOGY | PHM | SE,SAF,CERT,TEST,MRO | CARGO,COMPARTMENTS | Compartments/structure/access/inspection. Knots: K01,K05,K11. |
| 51 | STANDARD PRACTICES & STRUCTURES - GENERAL | T-TECHNOLOGY | PHM | SE,SAF,CERT,TEST,DAB | STRUCT_PRACTICES,MATERIALS | Structural practices, allowables, methods. Knots: K01,K05,K10. |
| 52 | DOORS / HATCHES | T-TECHNOLOGY | PHM | SE,SAF,CERT,OPS,TEST,MRO,DAB | DOORS,EGRESS | Doors/hatches/seals/actuation; egress compliance. Knots: K01,K05,K11. |
| 53 | FUSELAGE / PRESSURE VESSEL | T-TECHNOLOGY | PHM | SE,SAF,CERT,TEST,DAB | PRESSURE_VESSEL,LOADS | Primary structure / pressure vessel (Space-T). Knots: K01,K05,K10. |
| 54 | NACELLES / PYLONS (IF APPLICABLE) | T-TECHNOLOGY | PHM | SE,SAF,CERT,TEST | NACELLES,PYLONS | Nacelles/pylons and integration structures. Knots: K01,K05,K10. |
| 55 | STABILIZERS / CONTROL SURFACES | T-TECHNOLOGY | PHM | SE,SAF,CERT,TEST,DAB | CONTROL_SURFACES | Control surfaces mechanisms, loads, actuation interfaces. Knots: K01,K05,K07. |
| 56 | WINDOWS / VIEWPORTS | T-TECHNOLOGY | PHM | SE,SAF,CERT,OPS,MRO,TEST | VIEWPORTS,DEBRIS | Viewports/windows, debris protection, inspection. Knots: K01,K05,K11. |
| 57 | WINGS / LIFTING SURFACES | T-TECHNOLOGY | PHM | SE,SAF,CERT,TEST,DAB | LIFT_SURFACES,AEROELASTIC | Lifting surfaces / lifting body structures. Knots: K01,K05,K10. |
| 58 | RESERVED / EXTENSION | T-TECHNOLOGY | CM | SE,CERT | TAXONOMY | Reserved extension. Knots: K01,K04. |
| 59 | RESERVED / EXTENSION | T-TECHNOLOGY | CM | SE,CERT | TAXONOMY | Reserved extension. Knots: K01,K04. |
| 60 | STANDARD PRACTICES - PROPELLER / ROTOR | T-TECHNOLOGY | PHM | SE,CERT,TEST | PROP_ROTOR_PRACTICES | Prop/rotor practices (if applicable). Knots: K01,K05,K10. |
| 61 | PROPELLERS / PROPULSORS (IF APPLICABLE) | T-TECHNOLOGY | PHM | SE,SAF,CERT,TEST | PROPULSORS | Propulsors hardware (if applicable). Knots: K01,K05,K10. |
| 62 | ROTORS (IF APPLICABLE) | T-TECHNOLOGY | PHM | SE,CERT,TEST | ROTORS | Rotors (if applicable). Knots: K01,K05. |
| 63 | ROTOR DRIVES (IF APPLICABLE) | T-TECHNOLOGY | PHM | SE,CERT,TEST | ROTOR_DRIVES | Rotor drive trains (if applicable). Knots: K01,K05. |
| 64 | TAIL ROTOR (IF APPLICABLE) | T-TECHNOLOGY | PHM | SE,CERT,TEST | TAIL_ROTOR | Tail rotor (if applicable). Knots: K01,K05. |
| 65 | TAIL ROTOR DRIVE (IF APPLICABLE) | T-TECHNOLOGY | PHM | SE,CERT,TEST | TAIL_ROTOR_DRIVE | Tail rotor drive (if applicable). Knots: K01,K05. |
| 66 | FOLDING BLADES / TAIL PYLON (IF APPLICABLE) | T-TECHNOLOGY | PHM | SE,CERT,TEST | FOLDING_MECH | Folding mechanisms (if applicable). Knots: K01,K05. |
| 67 | ROTORS FLIGHT CONTROL (IF APPLICABLE) | T-TECHNOLOGY | PHM | SE,DAB,CERT,TEST | ROTOR_CONTROL | Rotor control interfaces and VV (if applicable). Knots: K01,K05,K07. |
| 68 | RESERVED / EXTENSION | T-TECHNOLOGY | CM | SE,CERT | TAXONOMY | Reserved extension. Knots: K01,K04. |
| 69 | RESERVED / EXTENSION | T-TECHNOLOGY | CM | SE,CERT | TAXONOMY | Reserved extension. Knots: K01,K04. |
| 70 | STANDARD PRACTICES - ENGINE | T-TECHNOLOGY | PHM | SE,SAF,CERT,TEST | ENGINE_PRACTICES | Engine/propulsion practices, methods, inspections. Knots: K01,K05,K10. |
| 71 | POWER PLANT / PROPULSION INTEGRATION | T-TECHNOLOGY | SE | PHM,DAB,SAF,CERT,TEST,SPACEPORT | PROP_INTEGRATION,ICDS | Propulsion integration architecture + ICD governance. Knots: K01,K04,K05,K09. |
| 72 | ENGINE (TURBINE/ROCKET/HYBRID AS APPLICABLE) | T-TECHNOLOGY | PHM | SE,SAF,CERT,TEST,SPACEPORT,DAB | TECH_PROP,QUAL_TESTS | Propulsion unit hardware + integration constraints. Knots: K01,K03,K05,K09. |
| 73 | ENGINE FUEL AND CONTROL | T-TECHNOLOGY | DAB | PHM,SE,CY,SAF,CERT,TEST,DAB | FADEC_LIKE,CYSEC | Propulsion control SW + safety/cyber evidence. Knots: K01,K05,K13. |
| 74 | IGNITION | T-TECHNOLOGY | PHM | SE,SAF,CERT,TEST,DAB | IGNITION,INTERLOCKS | Ignition hardware + interlocks + validation. Knots: K01,K03,K05. |
| 75 | AIR (BLEED / INLET / APU AIR) / INTAKE | T-TECHNOLOGY | PHM | SE,SAF,CERT,TEST | INTAKES,FLOW_PATHS | Intake/bleed/flow paths (as applicable). Knots: K01,K03,K05. |
| 76 | ENGINE CONTROLS | T-TECHNOLOGY | DAB | PHM,SE,CY,CERT,TEST,DAB | CONTROL_INTEGRATION | Integrated propulsion control SW (ICDs + VV). Knots: K01,K05,K13. |
| 77 | ENGINE INDICATING | T-TECHNOLOGY | DAB | PHM,SE,CERT,TEST,DAB | ENGINE_INDICATION | Indication/recording for propulsion. Knots: K01,K05,K06. |
| 78 | EXHAUST / PLUME MANAGEMENT | T-TECHNOLOGY | PHM | SE,SAF,CERT,TEST,SPACEPORT | PLUME,THERMAL,SAFETY | Exhaust/plume/thermal interactions + constraints. Knots: K01,K03,K05,K09. |
| 79 | OIL / LUBRICATION | T-TECHNOLOGY | PHM | SE,SAF,CERT,TEST,MRO | LUBE,OIL_SYSTEMS | Lubrication systems + servicing/inspection. Knots: K01,K03,K11. |
| 80 | OFF-BOARD / AIRPORT / SPACEPORT INFRASTRUCTURES (MASTER) | I-INFRASTRUCTURES | SPACEPORT | OPS,SAF,CERT,CM,DAB | SPACEPORT_MASTER | Master off-board infra baseline (Spaceport/Airport). Knots: K01,K02,K09,K10. |
| 81 | OFF-BOARD ENERGY / CRYO SERVICES | I-INFRASTRUCTURES | SPACEPORT | SAF,OPS,CERT,PHM,MRO | CRYO,ENERGY_SERVICES | Energy/cryo services & interfaces. Knots: K02,K03,K09. |
| 82 | OFF-BOARD MRO FACILITIES / TOOLING / LOGISTICS | I-INFRASTRUCTURES | MRO | OPS,SAF,CM,DAB | MRO_FACILITIES,TOOLING | MRO facilities/tooling/logistics baselines. Knots: K02,K04,K11. |
| 83 | GROUND COMMS / DAB EXCHANGE INFRA (GATEWAYS, EDGE) | I-INFRASTRUCTURES | DAB | CY,OPS,SPACEPORT,CERT,TEST | GATEWAYS,EDGE,DATA_EXCHANGE | Ground gateways/edge data exchange; cyber-required. Knots: K02,K06,K09,K13. |
| 84 | SPACEPORT SAFETY / EMERGENCY RESPONSE INFRA | I-INFRASTRUCTURES | SAF | SPACEPORT,OPS,CERT,TEST | EMERGENCY_RESPONSE | Safety infra & emergency response baselines. Knots: K02,K03,K09,K10. |
| 85 | CIRCULARITY INFRA (RETURN FLOWS, RECYCLING, CO2/H2 LOOPS) | I-INFRASTRUCTURES | DAB | PMO,CM,OPS,SPACEPORT | CIRCULARITY,LEDGERS | Circularity infra + trace/ledger hooks. Knots: K01,K06,K14. |
| 86 | OFF-BOARD DIGITAL SERVICES PLATFORM (PORTALS, ORCHESTRATION) | I-INFRASTRUCTURES | DAB | CY,OPS,CM,TEST,DAB | PORTALS,ORCHESTRATION | CAXS portals/orchestration services. Knots: K01,K06,K13. |
| 87 | IDENTITY / ACCESS / CYBERSECURITY INFRA (PHYSICAL+DIGITAL) | I-INFRASTRUCTURES | CY | DAB,CM,CERT,OPS | IAM,ZTA,SECOPS | Identity/access/cyber infra. Knots: K01,K06,K13. |
| 88 | GSE CONFIGURATION / ASSET MANAGEMENT | I-INFRASTRUCTURES | CM | MRO,DAB,OPS,CERT | ASSET_MGMT,CONFIG | GSE asset mgmt + configuration baselines. Knots: K01,K04,K06. |
| 89 | TEST RIGS / INSTRUMENTATION INFRA (GROUND) | I-INFRASTRUCTURES | TEST | SPACEPORT,PHM,DAB,CERT | TEST_RIGS,INSTRUMENTATION | Ground rigs/instrumentation infra. Knots: K01,K05,K09. |
| 90 | AI/ML MODEL REGISTRY & MODEL LIFECYCLE | N-NEURAL_NETWORKS | AI | DAB,CM,CERT,OPS,CY,TEST | MODEL_REGISTRY,GOV | Model registry + lifecycle governance. Knots: K01,K06,K07. |
| 91 | DAB SCHEMAS / ONTOLOGIES / SEMANTIC MODEL (SSOT) | N-NEURAL_NETWORKS | DAB | CM,SE,CY,CERT,TEST | ONTOLOGIES,SSOT | Ontologies/SSOT for validation and trace. Knots: K01,K06,K13. |
| 92 | WIRING / CONNECTIVITY GRAPHS & HARNESS DAB PACKAGES | N-NEURAL_NETWORKS | DAB | PHM,SE,CM,CERT,TEST | CONNECTIVITY,GRAPH | Connectivity graphs/harness datasets. Knots: K01,K06,K05. |
| 93 | TRACEABILITY GRAPH (REQ↔DESIGN↔VV↔OPS) & EVIDENCE LEDGERS | N-NEURAL_NETWORKS | CM | DAB,SE,CERT,TEST,AI | TRACEABILITY,EVIDENCE_LEDGER | Trace graph + evidence ledgers for audits/releases. Knots: K01,K06,K08. |
| 94 | DPP CORE (DIGITAL PRODUCT PASSPORT) & PROVENANCE | N-NEURAL_NETWORKS | DAB | CM,CERT,CY,OPS | DPP,PROVENANCE | DPP core + provenance/export views. Knots: K01,K06,K13,K14. |
| 95 | SBOM / SWHW BOM / MODEL BOM EXPORTS | N-NEURAL_NETWORKS | DAB | CY,CM,CERT,DAB | SBOM,BOM_EXPORTS | SBOM/SW/HW BOM exports + signing hooks. Knots: K01,K06,K13. |
| 96 | AI GOVERNANCE (RISK, ASSURANCE, MONITORING, DRIFT/BIAS) | N-NEURAL_NETWORKS | AI | SAF,CERT,OPS,CY,DAB,CM | AI_RISK,ASSURANCE | AI governance, monitors, approvals, rollback. Knots: K01,K07,K13. |
| 97 | CHANGE IMPACT ANALYTICS (WIRING/CONFIG/TRACE) | N-NEURAL_NETWORKS | DAB | CM,SE,CERT,TEST | IMPACT_ANALYTICS | Change impact analytics across config/trace/connectivity. Knots: K01,K04,K06. |
| 98 | SIGNED RELEASE PACKS / MANIFESTS / EXPORTS | N-NEURAL_NETWORKS | CM | CERT,DAB,CY,OPS | SIGNING,MANIFESTS,EXPORTS | Signed releases/manifests/exports (PR-blocking). Knots: K01,K04,K08,K13. |
| 99 | MASTER REGISTERS (GOLDEN RECORDS) & REFERENCE DATASETS | N-NEURAL_NETWORKS | DAB | CM,SE,CERT,TEST | MASTER_DATA,REGISTERS | Golden registers + reference datasets. Knots: K01,K06. |
| 100 | SIM/TEST GOVERNANCE (PLANS, ENVIRONMENTS, QUALITY) | T-SIMTEST | TEST | CERT,CM,DAB,SE | SIMTEST_GOV,TOOL_QUAL | Test governance, environments, tool qualification. Knots: K01,K05. |
| 101 | DIGITAL TWIN CONFIGURATION & SIM MODEL CATALOG | T-SIMTEST | DAB | TEST,SE,CM,CERT | DIGITAL_TWIN,CATALOG | Digital twin config + model catalog. Knots: K01,K06,K05. |
| 102 | SCENARIO LIBRARIES (MISSION, OFF-NOMINAL, EMERGENCY) | T-SIMTEST | OPS | TEST,SAF,SE,DAB | SCENARIOS,CONOPS | Scenario libraries for mission/off-nominal/emergency. Knots: K01,K02,K05. |
| 103 | SIL (SOFTWARE-IN-THE-LOOP) AUTOMATION | T-SIMTEST | DAB | TEST,CY,DAB,SE | SIL,AUTOMATION | SIL harnesses, runners, automation, logs. Knots: K01,K05,K13. |
| 104 | HIL (HARDWARE-IN-THE-LOOP) BENCHES | T-SIMTEST | TEST | PHM,DAB,SE,CERT | HIL,BENCHES | HIL benches + instrumentation + procedures. Knots: K01,K05. |
| 105 | PIL / TARGET EXECUTION (PROCESSOR/PLATFORM-IN-THE-LOOP) | T-SIMTEST | TEST | SE,CM,CERT,CY,DAB,PHM | PIL,TARGET,PERF_TIMING | Target execution evidence (timing/mem constraints). Knots: K01,K05,K13. |
| 106 | TEST PROCEDURES / TEST CASES / ACCEPTANCE CRITERIA | T-SIMTEST | TEST | SE,SAF,CERT,CM,DAB | TEST_CASES,ACCEPTANCE | Procedures/cases/criteria + trace links. Knots: K01,K06. |
| 107 | TEST DAB / INPUT DECKS / STIMULI | T-SIMTEST | DAB | TEST,SE,CM | TEST_DATA,STIMULI | Controlled test datasets/input decks/stimuli. Knots: K01,K06. |
| 108 | TEST RESULTS / REPORTING / ANOMALY MANAGEMENT | T-SIMTEST | TEST | DAB,OPS,SAF,CERT,CM | RESULTS,NCR,ANOMALIES | Results reporting + anomaly/NCR management. Knots: K01,K05,K08. |
| 109 | VV EVIDENCE PACKS (LINKED TO TRACEABILITY) | T-SIMTEST | CERT | CM,TEST,DAB,SE | VV_EVIDENCE,PACKAGING | Evidence bundling linked to trace graph. Knots: K01,K06,K08. |
| 110 | QUALIFICATION / ENVIRONMENTAL TESTING (SPACE-T) | T-SIMTEST | TEST | SAF,CERT,SPACEPORT,CM,SE,PHM,DAB | THERMAL_VAC,VIB,EMC | Space-T qual tests + facility constraints. Knots: K01,K05,K09. |
| 111 | SYSTEM INTEGRATION TESTING (END-TO-END) | T-SIMTEST | TEST | SE,SAF,CERT,DAB,CY | E2E_INTEGRATION | End-to-end integration testing across subsystems. Knots: K01,K05,K13. |
| 112 | MISSION/FLIGHT TESTING (OPERATIONAL DEMOS) | T-SIMTEST | OPS | TEST,SAF,CERT,CM,SPACEPORT,SE,DAB,PHM | OPS_DEMOS,READINESS | Operational demos + readiness + limits confirmation. Knots: K01,K02,K11,K12. |
| 113 | UNCERTAINTY QUANTIFICATION (UQ) / MONTE CARLO / SENSITIVITY | T-SIMTEST | DAB | TEST,SE,AI | UQ,MONTE_CARLO | UQ/Monte Carlo/sensitivity suites. Knots: K01,K05,K06. |
| 114 | AI/ML VALIDATION SUITES & MONITORING TESTS | T-SIMTEST | AI | TEST,SAF,CERT,OPS,CY,DAB | AI_VALIDATION,DRIFT | AI validation/robustness/drift suites. Knots: K01,K05,K07,K13. |
| 115 | CERTIFICATION TESTS (SW/HW/ECSS-DO) & COMPLIANCE REPORTS | T-SIMTEST | CERT | TEST,CM,SE,DAB,SAF,CY,PHM | COMPLIANCE,AUDIT | Compliance tests + reports + authority packs. Knots: K01,K05,K10,K13. |
| 116 | SIM/TEST ARCHIVES & BASELINES (FROZEN CAMPAIGNS) | T-SIMTEST | CM | TEST,DAB,CERT | ARCHIVES,BASELINES | Frozen campaigns, baselines, retention policy. Knots: K01,K04,K08. |

## 4. Table Statistics

| Metric | Value |
| :--- | :--- |
| Total Rows | 117 |
| Active ATAs | 97 |
| Reserved ATAs | 20 |
| Unique AoRs | 14 |
| Unique Domains | 6 |
| Average STKs per ATA | 4.5 |
| Last Updated | 2025-12-18 |

## 5. Usage Examples

### 5.1 Query by AoR

To find all ATAs owned by DATA:
```
Filter: AoR = "DATA"
Result: ATAs 45, 46, 83, 85, 86, 91, 92, 94, 95, 97, 99, 101, 107, 113
```

### 5.2 Query by Domain

To find all T-TECHNOLOGY ATAs:
```
Filter: DOMAIN = "T-TECHNOLOGY"
Result: ATAs 06, 08, 20-79
```

### 5.3 Query by Stakeholder Involvement

To find all ATAs where CY is involved:
```
Filter: AoR = "CY" OR "CY" IN STKs
Result: ATAs 22, 23, 27, 31, 34, 39, 42, 46, 73, 76, 83, 86, 87, 90-91, 94-96, 98, 103, 105, 111, 114-115
```

### 5.4 Query by Knot

To find all ATAs applicable to K13 (Cybersecurity):
```
Filter: "K13" IN Knots
Result: ATAs 22, 23, 31, 34, 39, 42, 45-46, 73, 76, 83, 86-87, 90-91, 94-96, 98, 103, 105, 111, 114-115
```

## 6. Data Quality

### 6.1 Data Sources
- **Primary Source:** config/database/ata_master_relations_table.yaml
- **Authority:** Configuration Management WG
- **Validation:** Automated schema validation + manual review

### 6.2 Data Validation
- **Schema validation:** YAML schema compliance
- **Referential integrity:** All STK codes must exist in stakeholder_map
- **Knot validation:** All knot references must be K01-K14
- **Domain validation:** All domains must match OPTINS Framework axes
- **Last validation:** 2025-12-18

### 6.3 Known Issues

None currently identified.

## 7. Related Tables

- **ATA Partition Matrix:** config/nomenclature/ATA_PARTITION_MATRIX.yaml
- **Stakeholder Knot Config:** scripts/stakeholder_knot_config.json
- **Knots Catalog:** 00_AMPEL360_SPACET_Q10_CERT_PLUS_BB_GEN_SB90_K01_CERT__knots-catalog_CAT_I01-R02_ACTIVE.json
- **Master Relations Catalog:** 00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_B30_LC01_K06_CM__ata-master-relations-table_CAT_I01-R02_ACTIVE.md

## 8. Change History

| Version | Date | Changes | Changed By | Rows Affected |
| :--- | :--- | :--- | :--- | :--- |
| I01-R02 | 2025-12-18 | Initial table creation | CM WG | All (117) |

## 9. Export Formats

This table is available in multiple formats:

- **Markdown:** This document
- **YAML:** `config/database/ata_master_relations_table.yaml` (structured master)
- **CSV:** Can be exported from YAML using conversion tools
- **JSON:** Can be exported from YAML using conversion tools

## 10. Maintenance

**Update Process:** Changes require CM WG approval and must update both YAML master and this quick reference.  
**Review Cycle:** Quarterly or on-demand for major changes  
**Data Owner:** Configuration Management WG  
**Technical Contact:** CM Lead

## 11. References

- **Nomenclature Standard:** NOMENCLATURE_v6_0_R1_0
- **OPTINS Framework:** v1.1
- **ATA iSpec 2200:** Industry standard ATA chapter structure
- **Portal Structure:** AMPEL360-SPACE-T-PORTAL/ stakeholder directories

---

**Document Control:**
- **Filename:** 00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_B30_LC01_K06_CM__ata-master-relations-quick-ref_TAB_I01-R02_ACTIVE.md
- **Location:** Repository root
- **Format:** Markdown (TAB template)
- **Status:** Active
- **Classification:** Internal reference
- **Distribution:** All stakeholders
