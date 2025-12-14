---
title: "00-00-02 Safety"
lifecycle_phase: "02: Safety"
generated: "2025-12-11 11:03:48"
standard: "OPT-IN Framework v1.1 / AMPEL360 Space-T"
status: "Draft – In Progress"
owner: "Safety & Certification WG (Space-T)"
primary_artefacts:
  - "Safety Plan"
  - "Hazard Log"
  - "Safety Case"
  - "FHA/PSSA/SSA Pack"
---

# 00-00-02 Safety

## 1. Purpose and Scope

This section defines the **Safety Management and Safety Assurance approach** for AMPEL360 Space-T, covering **flight**, **ground**, **launch/landing operations**, and **support segments** (GSE, facilities, software services) as applicable. The intent is to establish a **single safety framework** capable of supporting both:

* **Airworthiness-style** system safety assessments (civil aviation methods), and
* **Space system safety assurance** (ECSS-based safety programme and tailoring).

Safety assurance applies to **hardware, software, human procedures, and operational constraints**, and produces a structured evidence set suitable for certification/approval pathways and internal gate reviews.

---

## 2. Standards Baseline and Tailoring

### 2.1 Space safety and product assurance (ECSS)

* **System Safety Programme:** ECSS **Q-ST-40** (Safety) defines the safety programme and technical requirements for European space projects.
* **Space Software Engineering:** ECSS **E-ST-40** (Software) covers the space software engineering lifecycle, including requirements, design, V&V, transfer, operations, and maintenance.
* **Software Product Assurance:** ECSS **Q-ST-80** defines software product assurance requirements and includes tailoring/applicability concepts based on software criticality.

> **Project Rule:** ECSS tailoring decisions (per mission profile, criticality, and segment scope) shall be recorded in a **Tailoring Matrix** and controlled under configuration management.

### 2.2 Airworthiness-style system safety (methods baseline)

* FHA/PSSA/SSA (and related analyses such as FMEA/FTA/CCA) are used as the **core workflow** for functional safety assessment; FAA guidance explicitly references SAE ARP4761-family techniques for these analyses.

### 2.3 Avionics assurance (as adopted by project)

* **Software Safety:** DO-178C (software lifecycle data, verification, traceability).
* **Hardware Safety:** DO-254 (complex electronic hardware assurance).
* **Documentation Structure:** ATA iSpec 2200 (Space-T adaptation) for safety messaging consistency (Warnings/Cautions/Notes).

---

## 3. Safety Governance and Responsibilities

### 3.1 Roles (minimum set)

| Role | Accountability (A) / Responsibility (R) |
| :--- | :--- |
| Safety Manager (Program) | A: Safety policy, acceptance criteria, programme-level risk acceptance |
| Chief / Lead System Safety Engineer | R: Safety process execution, safety case structure, cross-segment safety consistency |
| Segment Safety Owners (Vehicle / Ground / Ops / SW Platform) | R: Hazard identification, mitigation closure, evidence delivery |
| SW Assurance Lead | R: DAL/criticality allocation (software), partitioning strategy, verification evidence |
| HW Assurance Lead | R: DAL/criticality allocation (hardware), independence, design assurance evidence |
| Verification & Validation Lead | R: Verification planning, coverage and independence, anomaly disposition linkage |
| Configuration Management Lead | R: Baseline control of safety artefacts, change impact workflow |
| Technical Publications Lead | R: Mapping hazards → Warnings/Cautions/Notes and procedural mitigations |

### 3.2 Decision rights

* **Risk acceptance** thresholds and residual-risk approvals are controlled via the **Safety Review Board (SRB)**.
* Any change impacting safety objectives triggers a **Safety Impact Assessment (SIA)** and SRB disposition.

---

## 4. Safety Assurance Outputs (Evidence Set)

Minimum deliverables for lifecycle phase 02 (Safety):

1. **Safety Plan** (process, tailoring, responsibilities, schedule, acceptance criteria).
2. **Hazard Log** (single source of truth; unique hazard IDs; traceable to requirements and mitigations).
3. **FHA Pack** (aircraft/vehicle-level and system/segment-level, as applicable).
4. **PSSA Pack** (architecture-driven; allocation of safety requirements and independence).
5. **SSA Pack** (implementation verification; closure of safety objectives; residual risk statement).
6. **Safety Requirements Specification (SRS-SAFE)** with verification methods and evidence links.
7. **Safety Case** (structured argument + evidence index + traceability matrix).
8. **Safety Traceability Matrix (STM)**: Hazard ↔ Safety Req ↔ Design ↔ Verification ↔ Ops/Docs.

> **Evidence Control:** All safety artefacts shall be configuration-controlled; evidence packages may be hash-anchored (CDTL/UTCS) where the programme requires immutable auditability.

---

## 5. Criticality and Design Assurance Allocation

### 5.1 Aviation-style DAL table (project baseline)

| Level | Failure Condition | Reference Baseline | Typical Application |
| :--- | :--- | :--- | :--- |
| A | Catastrophic | DO-178C / DO-254 | Flight-critical control/command |
| B | Hazardous / Severe-Major | DO-178C / DO-254 | Mission-critical subsystems |
| C | Major | DO-178C / DO-254 | Standard operational systems |
| D | Minor | DO-178C / DO-254 | Non-essential interfaces |
| E | No Effect | DO-178C / DO-254 | Administrative / non-safety functions |

### 5.2 Space criticality (ECSS tailoring)

Space-segment software/hardware criticality shall be defined and tailored per ECSS programme rules, using:

* ECSS-E-ST-40 for engineering lifecycle obligations, and
* ECSS-Q-ST-80 for product assurance requirements and applicability by criticality.

> **Project Rule:** Where dual compliance applies (aviation DAL + ECSS criticality), the governing obligations are the **more stringent** of the two, unless explicitly tailored and approved by SRB.

---

## 6. Hazard Analysis Workflow (FHA → PSSA → SSA)

### 6.1 Workflow steps (with required outputs)

1. **Functional Hazard Assessment (FHA)**
   * Input: Functional architecture, concept of operations, operational scenarios
   * Output: Failure conditions, severity classification, candidate safety objectives

2. **Preliminary System Safety Assessment (PSSA)**
   * Input: Proposed system/segment architecture, redundancy concept, partitioning concept
   * Output: Allocated safety requirements, independence/segregation requirements, candidate safety monitors

3. **System Safety Assessment (SSA)**
   * Input: Implemented design, test results, analyses, operational procedures
   * Output: Demonstrated compliance with safety objectives; residual risk statement; closure evidence

FAA guidance references these analysis techniques (FHA/PSSA/FMEA/CMA/PRA/ZSA, etc.) as typical elements of system safety compliance demonstrations.

### 6.2 Mandatory analysis set (tailored by segment)

* **FMEA/FMECA** (component failure effects)
* **FTA** (top-event probability/logic)
* **CCA** (common cause/common mode, zonal/particular risks)
* **Human factors & procedure hazards** (crew/ground/maintenance actions)
* **Operational risk controls** (constraints, dispatch rules, go/no-go criteria)

---

## 7. Safety Requirements (Initial Set)

All safety requirements shall be uniquely identified, traceable to hazards, and include verification method(s).

| ID | Requirement | Verification |
| :--- | :--- | :--- |
| SR-001 | All safety-critical commands shall implement **dual independent verification** (e.g., cross-channel agreement, reasonableness checks, and authority gating). | Test + Analysis |
| SR-002 | **Partitioning/segregation** shall enforce isolation between DAL A (or highest criticality) functions and lower-criticality functions, including fault containment and resource control. | Analysis + Review + Test |
| SR-003 | **Hardware watchdog(s)** shall be independent of the primary processing path and capable of forcing the system to a defined safe state upon detected runaway/fault. | Test + Inspection |
| SR-004 | All safety monitors shall have a defined **safe-state** and **time-to-detect/time-to-react** objective appropriate to the hazard severity. | Analysis + Test |
| SR-005 | Any single failure (or single erroneous command) shall not cause loss of safety-critical function where redundancy is claimed; common-cause vulnerabilities shall be explicitly addressed. | Analysis (CCA/FTA) |
| SR-006 | Safety-related crew/ground procedures shall include clear **Warnings/Cautions/Notes** mapped to hazard IDs and validated in operational trials or simulations. | Review + Operational Validation |

---

## 8. Technical Documentation Integration (ATA iSpec 2200)

Safety messaging in procedures and operational documentation shall follow a consistent hierarchy:

* **Warnings** — risk of injury/fatality (personnel / public).
* **Cautions** — risk of equipment damage or mission degradation.
* **Notes** — operational emphasis and clarity.

**Traceability Rule:** every Warning/Caution must reference at least one **Hazard ID** and the associated **mitigation control** (design control and/or procedural control).

---

## 9. Reviews, Gates, and Auditability

Minimum safety gates (tailored to programme milestones):

* **Safety Kick-off / Tailoring Review**
* **FHA Review** (functional baseline freeze)
* **PSSA Review** (architecture baseline readiness)
* **SSA Readiness Review** (verification sufficiency, anomaly status)
* **Safety Case Review** (release / certification package)

All safety artefacts are subject to:
* configuration control,
* independent review (commensurate with criticality),
* anomaly linkage (problem reports ↔ hazard impacts).

---

## 10. References

* OPT-IN Framework Standard v1.1
* ECSS-Q-ST-40 (Safety)
* ECSS-E-ST-40 (Software)
* ECSS-Q-ST-80 (Software product assurance)
* FAA AC 25.1309-1B (system safety guidance referencing FHA/PSSA/SSA techniques)
* DO-178C / DO-254 / ATA iSpec 2200 (Space-T adaptation)
