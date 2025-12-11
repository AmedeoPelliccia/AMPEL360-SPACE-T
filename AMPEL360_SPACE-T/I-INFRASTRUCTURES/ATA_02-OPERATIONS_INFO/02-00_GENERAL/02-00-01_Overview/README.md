# 02-00-01 — Operations Information Overview

**Programme:** AMPEL360 Space-T  
**Axis:** I-INFRASTRUCTURES — Operations & Ground Infrastructures  
**ATA-SpaceT:** [ATA_02-OPERATIONS_INFO](../..)  
**Document ID:** ST-02-00-01-OVW  
**Version:** 1.0  
**Date:** 2025-12-09  
**Status:** DRAFT  
**Owner:** AMPEL360 Documentation WG / IDEALEeu Enterprise  

---

## 1. Purpose

ATA 02-OPERATIONS_INFO defines the **information layer that enables Space-T operations** across:

- Ground segment (launch sites, mission control, logistics hubs).  
- Flight/mission operations (planning, execution, monitoring, debrief).  
- Post-flight analysis, circularity loops and Digital Product Passport (DPP) updates.

This document provides a **high-level overview** of:

- What is in scope for Operations Information within the I-INFRASTRUCTURES axis.  
- How the `02-00_GENERAL` lifecycle folders are structured and used.  
- How ATA 02 connects to other Space-T systems ([ATA_03-SUPPORT_INFORMATION_GSE](../../../ATA_03-SUPPORT_INFORMATION_GSE/), [ATA_21-ECLSS](../../../../T-TECHNOLOGY_ONBOARD_SYSTEMS/ATA_21-ECLSS/), [ATA_22-GNC_AUTOFLIGHT](../../../../T-TECHNOLOGY_ONBOARD_SYSTEMS/ATA_22-GNC_AUTOFLIGHT/), [ATA_24-EPS_POWER](../../../../T-TECHNOLOGY_ONBOARD_SYSTEMS/ATA_24-EPS_POWER/), [ATA_31-AVIONICS_CORE](../../../../T-TECHNOLOGY_ONBOARD_SYSTEMS/ATA_31-AVIONICS_CORE/), [ATA_72-MAIN_ENGINES](../../../../T-TECHNOLOGY_ONBOARD_SYSTEMS/ATA_72-MAIN_ENGINES/), [ATA_95-NEURAL_OPS_AI](../../../../N-NEURAL_NETWORKS_DPP_TRACEABILITY/ATA_95-NEURAL_OPS_AI/), [ATA_96-DPP_TRACEABILITY](../../../../N-NEURAL_NETWORKS_DPP_TRACEABILITY/ATA_96-DPP_TRACEABILITY/)).

---

## 2. Scope

### 2.1 In Scope

ATA 02 covers the **data, tools and documentation** required to operate AMPEL360 Space-T safely and efficiently, including:

- Mission planning data and products (launch windows, trajectories, constraints).  
- Ground operations procedures and timelines (pad turn-around, fueling, loading).  
- Control room configurations, checklists, and runbooks.  
- Telemetry definitions, logging policies, and replay tools.  
- Incident / anomaly reporting workflows and repositories.  
- Operational dashboards, KPIs, and performance monitoring frameworks.  
- Interfaces to DPP / traceability systems for operational events and cycles.  

### 2.2 Out of Scope

The following are **not** owned by ATA 02, but are referenced:

- Detailed design of on-board systems (e.g. [ATA_21-ECLSS](../../../../T-TECHNOLOGY_ONBOARD_SYSTEMS/ATA_21-ECLSS/), [ATA_22-GNC_AUTOFLIGHT](../../../../T-TECHNOLOGY_ONBOARD_SYSTEMS/ATA_22-GNC_AUTOFLIGHT/), [ATA_24-EPS_POWER](../../../../T-TECHNOLOGY_ONBOARD_SYSTEMS/ATA_24-EPS_POWER/), [ATA_31-AVIONICS_CORE](../../../../T-TECHNOLOGY_ONBOARD_SYSTEMS/ATA_31-AVIONICS_CORE/), [ATA_53-STRUCTURE_FUSELAGE](../../../../T-TECHNOLOGY_ONBOARD_SYSTEMS/ATA_53-STRUCTURE_FUSELAGE/), [ATA_57-WINGS_LIFTING_BODY](../../../../T-TECHNOLOGY_ONBOARD_SYSTEMS/ATA_57-WINGS_LIFTING_BODY/), [ATA_72-MAIN_ENGINES](../../../../T-TECHNOLOGY_ONBOARD_SYSTEMS/ATA_72-MAIN_ENGINES/)).  
- Ground Support Equipment hardware design ([ATA_03-SUPPORT_INFORMATION_GSE](../../../ATA_03-SUPPORT_INFORMATION_GSE/)).  
- Neural network models and training artefacts ([ATA_95-NEURAL_OPS_AI](../../../../N-NEURAL_NETWORKS_DPP_TRACEABILITY/ATA_95-NEURAL_OPS_AI/)).  
- DPP core specifications and schemas ([ATA_96-DPP_TRACEABILITY](../../../../N-NEURAL_NETWORKS_DPP_TRACEABILITY/ATA_96-DPP_TRACEABILITY/)).  

These are documented in their respective ATA chapters and linked from ATA 02.

---

## 3. Position in OPT-IN & Space-T Architecture

- **OPT-IN Axis:** `I-INFRASTRUCTURES` – focuses on fixed/ground systems and the digital backbone that supports operations.  
- **Role of ATA 02:** acts as the **operations “nervous system”**: connecting procedures, data flows, mission tooling and traceability.  
- **Relation to other axes:**
  - `O-ORGANIZATION`: governance, policies, operational roles and responsibilities.
  - `P-PROGRAM`: lifecycle phases (Qualification, EIS, Incremental Upgrades) and their operational baselines.
  - `T-TECHNOLOGY_ONBOARD_SYSTEMS`: consumers and producers of telemetry and commands (see ATA 21/22/24/31/53/57/72).  
  - `N-NEURAL_NETWORKS_DPP_TRACEABILITY`: AI-assisted ops, anomaly detection, carbon/circularity accounting (see [ATA_95-NEURAL_OPS_AI](../../../../N-NEURAL_NETWORKS_DPP_TRACEABILITY/ATA_95-NEURAL_OPS_AI/), [ATA_96-DPP_TRACEABILITY](../../../../N-NEURAL_NETWORKS_DPP_TRACEABILITY/ATA_96-DPP_TRACEABILITY/)).

---

## 4. 02-00_GENERAL Structure

The `02-00_GENERAL` folder provides the **14-folder lifecycle skeleton** for Operations Information. Subfolders are:

1. **02-00-01_Overview**  
   – This document; mission, scope, stakeholders, and structure.

2. **02-00-02_Safety**  
   – Operational safety concepts, hazard logs interfaces, operating limitations, links to safety assessments (FHA/PSSA/FTA/FMEA) with operational impact.

3. **02-00-03_Requirements**  
   – Operational information requirements, including:
   - Minimum data sets for each mission phase.  
   - Latency, integrity and availability requirements.  
   - Regulatory and standard-driven constraints (e.g., ECSS, range safety).

4. **02-00-04_Design**  
   – Logical and physical design of the operations information architecture:
   - Data models, schemas, master data.  
   - Tooling landscape (planning systems, telemetry servers, archives).  
   - Human–machine interfaces (HMI/HCI) for mission controllers.

5. **02-00-05_Interfaces**  
   – Interfaces between ATA 02 and:
   - On-board systems ([ATA_21-ECLSS](../../../../T-TECHNOLOGY_ONBOARD_SYSTEMS/ATA_21-ECLSS/), [ATA_22-GNC_AUTOFLIGHT](../../../../T-TECHNOLOGY_ONBOARD_SYSTEMS/ATA_22-GNC_AUTOFLIGHT/), [ATA_24-EPS_POWER](../../../../T-TECHNOLOGY_ONBOARD_SYSTEMS/ATA_24-EPS_POWER/), [ATA_31-AVIONICS_CORE](../../../../T-TECHNOLOGY_ONBOARD_SYSTEMS/ATA_31-AVIONICS_CORE/), [ATA_72-MAIN_ENGINES](../../../../T-TECHNOLOGY_ONBOARD_SYSTEMS/ATA_72-MAIN_ENGINES/)).  
   - GSE / launch infrastructure ([ATA_03-SUPPORT_INFORMATION_GSE](../../../ATA_03-SUPPORT_INFORMATION_GSE/)).  
   - DPP/UTCS, NN Ops, external stakeholders ([ATA_95-NEURAL_OPS_AI](../../../../N-NEURAL_NETWORKS_DPP_TRACEABILITY/ATA_95-NEURAL_OPS_AI/), [ATA_96-DPP_TRACEABILITY](../../../../N-NEURAL_NETWORKS_DPP_TRACEABILITY/ATA_96-DPP_TRACEABILITY/)).

6. **02-00-06_Engineering**  
   – Engineering artefacts supporting operations information:
   - Trade studies on architectures and tools.  
   - Performance analyses (throughput, reliability).  
   - Non-functional characteristics (security, resilience, scalability).

7. **02-00-07_V_AND_V**  
   – Verification & Validation of operations information systems:
   - Test plans, test cases, test procedures.  
   - Simulators, digital twins and rehearsal environments.  
   - V&V evidence for compliance with programme and regulatory requirements.

8. **02-00-08_Prototyping**  
   – Experimental tooling, sandboxes and trial configurations:
   - Early demonstrations of new dashboards or planning tools.  
   - Trial integrations with NN/AI agents for mission ops support.  

9. **02-00-09_Production_Planning**  
   – Planning the deployment and evolution of Ops Info systems:
   - Roll-out plans, migration strategies, cut-over procedures.  
   - Capacity plans for storage, networks and compute.

10. **02-00-10_Certification**  
    – Evidence supporting regulatory and internal certification:
    - Compliance mapping to ECSS, EASA/FAA where applicable.  
    - Audit trails, procedures and findings closure for operations information.

11. **02-00-11_EIS_Versions_Tags**  
    – In-service (EIS) baselines and evolution:
    - Versioned configurations of operations tools and data flows.  
    - Tagging rules for mission series, campaigns and major upgrades.

12. **02-00-12_Services**  
    – Operational services catalogue:
    - Monitoring, alerting, 24/7 mission support services.  
    - SLAs, OLAs and service contact points.

13. **02-00-13_Subsystems_Components**  
    – Breakdown of the operations information architecture into subsystems:
    - Planning, telemetry, logging, analytics, archiving, reporting, etc.  
    - Each with pointers into `02-20_Subsystems`.

14. **02-00-14_Ops_Std_Sustain**  
    – Standard operating procedures (SOPs) and sustainability aspects:
    - Standardisation of mission timelines, checklists, handovers.  
    - Circularity and sustainability metrics as seen from operations (energy, consumables, CO₂, water reuse).

---

## 5. Key Interfaces and Cross-ATA Links

| ATA / Domain                                                                                               | Type of Link                           | Examples                                                        |
|------------------------------------------------------------------------------------------------------------|----------------------------------------|-----------------------------------------------------------------|
| [ATA_03-SUPPORT_INFORMATION_GSE](../../../ATA_03-SUPPORT_INFORMATION_GSE/)                                 | Ground infrastructure information      | Pad configuration, fueling sequences, vehicle–GSE connections   |
| [ATA_21-ECLSS](../../../../T-TECHNOLOGY_ONBOARD_SYSTEMS/ATA_21-ECLSS/)                                     | Mission & cabin ops data               | Life support consumables tracking, alarms, contingency modes    |
| [ATA_22-GNC_AUTOFLIGHT](../../../../T-TECHNOLOGY_ONBOARD_SYSTEMS/ATA_22-GNC_AUTOFLIGHT/)                   | Guidance & control data flows          | TM/TC link structures, navigation solutions, auto-flight modes  |
| [ATA_24-EPS_POWER](../../../../T-TECHNOLOGY_ONBOARD_SYSTEMS/ATA_24-EPS_POWER/)                             | Power budgets & status                 | Power allocation timelines, constraints for mission phases      |
| [ATA_31-AVIONICS_CORE](../../../../T-TECHNOLOGY_ONBOARD_SYSTEMS/ATA_31-AVIONICS_CORE/)                     | Core avionics data definitions         | TM packets, event logs, time synchronisation                    |
| [ATA_72-MAIN_ENGINES](../../../../T-TECHNOLOGY_ONBOARD_SYSTEMS/ATA_72-MAIN_ENGINES/)                       | Propulsion operations                  | Engine start sequences, throttle profiles, health monitoring    |
| [ATA_95-NEURAL_OPS_AI](../../../../N-NEURAL_NETWORKS_DPP_TRACEABILITY/ATA_95-NEURAL_OPS_AI/)               | AI support for operations              | Anomaly detection, trajectory optimisation, decision support    |
| [ATA_96-DPP_TRACEABILITY](../../../../N-NEURAL_NETWORKS_DPP_TRACEABILITY/ATA_96-DPP_TRACEABILITY/)         | Traceability and audit trails          | Mission events in DPP, carbon and circularity accounting        |

---

## 6. Intended Users and Roles

Typical users of ATA 02 documentation and artefacts include:

- Mission Directors and Flight Operations Managers.  
- Ground Segment and Control Room Engineers.  
- GSE and Launch Operations Teams (interface perspective).  
- Safety & Certification Engineers (ops-related evidence).  
- Data / AI Engineers working on operational analytics and NN support tools.  
- Regulatory / Audit stakeholders reviewing operations information flows.

---

## 7. Usage & Contribution Guidelines

- Use ATA 02 as the **single reference** for describing how operations information is structured, stored, exchanged and governed.  
- When creating new documents:
  - Place them under the appropriate `02-00-XX` lifecycle folder.  
  - Use the `ST-02-XX-YY-<NNNN>` naming convention (to be detailed in `02-00-03_Requirements` and `02-00-05_Interfaces`).  
  - Maintain cross-links to relevant ATA chapters, especially [ATA_03-SUPPORT_INFORMATION_GSE](../../../ATA_03-SUPPORT_INFORMATION_GSE/), [ATA_21-ECLSS](../../../../T-TECHNOLOGY_ONBOARD_SYSTEMS/ATA_21-ECLSS/), [ATA_22-GNC_AUTOFLIGHT](../../../../T-TECHNOLOGY_ONBOARD_SYSTEMS/ATA_22-GNC_AUTOFLIGHT/), [ATA_24-EPS_POWER](../../../../T-TECHNOLOGY_ONBOARD_SYSTEMS/ATA_24-EPS_POWER/), [ATA_31-AVIONICS_CORE](../../../../T-TECHNOLOGY_ONBOARD_SYSTEMS/ATA_31-AVIONICS_CORE/), [ATA_72-MAIN_ENGINES](../../../../T-TECHNOLOGY_ONBOARD_SYSTEMS/ATA_72-MAIN_ENGINES/), [ATA_95-NEURAL_OPS_AI](../../../../N-NEURAL_NETWORKS_DPP_TRACEABILITY/ATA_95-NEURAL_OPS_AI/), [ATA_96-DPP_TRACEABILITY](../../../../N-NEURAL_NETWORKS_DPP_TRACEABILITY/ATA_96-DPP_TRACEABILITY/).  
- Keep this overview updated when:
  - New subsystems are added in `02-20_Subsystems`.  
  - Major changes occur in the operations information architecture or tooling.  

---

## 8. References

- OPT-IN Framework Standard v1.1 – I-INFRASTRUCTURES Axis.  
- AMPEL360 Space-T – Global Architecture Overview.  
- ECSS-E-ST-40C – Space engineering – Software.  
- ECSS-E-ST-70 series – Ground systems and operations (as applicable).  
- Internal AMPEL360 LC/UTCS and DPP standards.
