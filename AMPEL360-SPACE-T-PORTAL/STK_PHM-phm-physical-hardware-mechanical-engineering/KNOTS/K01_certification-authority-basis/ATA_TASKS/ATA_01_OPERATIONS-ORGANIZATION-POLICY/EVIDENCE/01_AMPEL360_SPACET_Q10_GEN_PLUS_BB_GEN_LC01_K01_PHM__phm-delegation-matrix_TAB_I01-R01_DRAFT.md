---
title: "PHM Delegation Matrix — Authority & Responsibility within DOA/POA"
type: TAB
project: "AMPEL360"
program: "SPACET"
family: "Q10"
variant: "GEN"
version: "PLUS"
model: "BB"
block: "GEN"
phase: "LC01"
knot_task: "K01"
task_id: "T001"
ata_code: "01"
aor: "PHM"
status: Draft
date: "2026-02-25"
owner: "Physical Hardware & Mechanical Engineering"
table_type: "RACI Delegation Matrix"
schema_refs:
  - schema_id: "SCH-RACI-001-V01"
    registry: "ATA 91"
    status: "draft"
trace_links:
  - type: "satisfies"
    target: "K01-T001"
    status: "proposed"
  - type: "derives_from"
    target: "EASA-Part21-SubpartJ"
    status: "proposed"
  - type: "derives_from"
    target: "EASA-Part21-SubpartG"
    status: "proposed"
---

# PHM Delegation Matrix — Authority & Responsibility within DOA/POA

## 1. Table Information

| Field | Details |
| :--- | :--- |
| **Table Name:** | PHM Delegation Matrix |
| **Type:** | RACI Delegation Matrix |
| **Purpose:** | Define authority levels and RACI responsibilities for PHM decision areas within the AMPEL360 DOA/POA framework |
| **Owner:** | PHM Lead |
| **Last Updated:** | 2026-02-25 |
| **Status:** | Draft |
| **Task Reference:** | K01-T001 |

## 2. Table Description

### 2.1 Purpose

This delegation matrix defines **who can decide what** within the PHM (Physical Hardware & Mechanical Engineering) domain. It maps decision areas to authority levels and assigns RACI responsibilities across PHM roles and external stakeholders, ensuring clear accountability for certification, design, production, and operational decisions.

### 2.2 Scope

- All PHM-owned ATA chapters (structural, mechanical, propulsion, systems)
- Decision areas spanning DOA (design authority) and POA (production authority)
- Authority levels aligned with the K01 RBAC model (§2.3 of the K01 Plan)

### 2.3 Authority Levels

| Level | Name | Description |
| :--- | :--- | :--- |
| **L1** | Authority | Final decision authority; requires senior management sign-off |
| **L2** | Approve | Decision authority delegated to domain lead; binding within scope |
| **L3** | Certify/Recommend | Technical recommendation; decision escalated to L1/L2 authority |

### 2.4 RACI Legend

| Code | Role | Description |
| :--- | :--- | :--- |
| **A** | Accountable | Ultimately answerable; one per decision area |
| **R** | Responsible | Does the work; may be multiple |
| **C** | Consulted | Provides input before decision; two-way communication |
| **I** | Informed | Notified after decision; one-way communication |

## 3. Delegation Matrix — Design Authority (DOA, Part 21J)

### 3.1 Design Decision Areas

| Decision Area | Auth. Level | PHM Lead | PHM Sys Eng | PHM Struct Eng | PHM Prop Eng | PHM V&V Eng | PHM Int Eng | Head of Design | Quality Mgr |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| PHM Architecture Changes | L2 | **A** | R | R | R | C | I | I | I |
| Structural Design Data Approval (ATA 20, 51, 53, 57, 115) | L2 | **A** | I | R | I | C | I | I | C |
| Systems Design Data Approval (ATA 21, 22, 24, 26, 27, 42) | L2 | **A** | R | I | I | C | I | I | C |
| Propulsion Design Data Approval (ATA 28, 70-84, 110) | L2 | **A** | I | I | R | C | I | I | C |
| Means of Compliance Agreement (MoC) | L1 | R | C | C | C | R | I | **A** | C |
| Design Change Classification (Minor/Major) | L2 | **A** | C | C | C | I | R | I | C |
| Equivalent Safety Finding Proposals | L1 | R | C | R | C | R | I | **A** | C |
| Certification Submission Evidence (ATA 109, 115) | L2 | **A** | I | C | C | R | I | I | C |
| Material & Process Qualification | L2 | **A** | I | R | R | C | I | I | C |
| Vibration & Noise Analysis (ATA 18) | L2 | **A** | C | R | C | R | R | I | I |

### 3.2 Certification Coordination Areas

| Decision Area | Auth. Level | PHM Lead | STK_CERT | STK_SE | STK_SAF | STK_TEST | STK_CM |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Certification Basis Definition | L1 | C | **A** | C | C | I | I |
| PHM Compliance Matrix Approval | L2 | **A** | R | C | C | I | I |
| Test Plan Alignment with MoC | L2 | R | C | I | I | **A** | I |
| Safety Assessment Integration | L2 | C | I | C | **A** | I | I |
| Configuration Baseline Updates | L2 | R | I | I | I | I | **A** |
| ICD Change Management | L2 | R | I | **A** | C | I | R |

## 4. Delegation Matrix — Production Authority (POA, Part 21G)

### 4.1 Production Decision Areas

| Decision Area | Auth. Level | PHM Lead | PHM Struct Eng | PHM Prop Eng | PHM V&V Eng | PHM Int Eng | Head of Production | Quality Mgr |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Production Conformity — Structural Parts | L2 | **A** | R | I | C | I | C | C |
| Production Conformity — Propulsion Parts | L2 | **A** | I | R | C | I | C | C |
| Manufacturing Process Approval | L2 | C | R | R | I | I | **A** | C |
| Inspection Criteria Definition | L2 | **A** | C | C | R | I | I | C |
| Non-Conformance Disposition (Structural) | L2 | **A** | R | I | C | I | C | R |
| Non-Conformance Disposition (Propulsion) | L2 | **A** | I | R | C | I | C | R |
| Supplier Qualification — PHM Hardware | L3 | R | C | C | I | R | **A** | C |
| First Article Inspection Criteria | L2 | **A** | R | R | C | I | C | C |

## 5. Delegation Matrix — Operational & Maintenance Authority

| Decision Area | Auth. Level | PHM Lead | PHM V&V Eng | PHM Int Eng | STK_MRO | STK_OPS | Quality Mgr |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Maintenance Philosophy (MSG-3/RCM) | L2 | **A** | C | R | R | C | I |
| Time Limits & Maintenance Checks (ATA 05) | L2 | **A** | R | C | C | I | I |
| Airworthiness Limitations (ATA 04) | L1 | R | R | C | I | I | **A** |
| PHM Anomaly Resolution | L3 | **A** | R | R | C | I | C |
| Fleet-wide PHM Data Analysis | L2 | **A** | R | C | R | I | I |

## 6. Escalation Matrix

| Situation | First Escalation | Second Escalation | Decision Authority |
| :--- | :--- | :--- | :--- |
| Disagreement on design data approval | PHM Lead | Head of Design | Head of Design |
| Cross-stakeholder ICD conflict | PHM Lead + SE Lead | Head of Design | Head of Design + QM |
| Safety-critical non-conformance | PHM Lead + QM | Head of Airworthiness | Accountable Manager |
| Certification submission dispute | PHM Lead + CERT Lead | Head of Design | Accountable Manager |
| Production conformity rejection | PHM Lead + Head of Production | Quality Manager | Quality Manager |

## 7. Constraints and Validations

- Each decision area must have exactly **one Accountable (A)** role
- Authority level L1 decisions require Head of Design or Accountable Manager sign-off
- Safety-critical decisions (ATA 26, 27, 28) require concurrent SAF stakeholder consultation
- All delegation changes must be recorded in DECISIONS/ and approved by CM

## 8. Trace Links

| Link Type | Target | Status |
| :--- | :--- | :--- |
| satisfies | K01-T001 | Proposed |
| derives_from | EASA Part 21 Subpart J (DOA) | Proposed |
| derives_from | EASA Part 21 Subpart G (POA) | Proposed |
| inputs_to | K01-T002 (Engineering authority delegation) | Proposed |
| related_to | K01 RBAC Model (§2.3) | Proposed |
| related_to | PHM ORG Chart (phm-org-chart-doa-poa_DIA) | Proposed |

## 9. Change History

| Version | Date | Changes | Changed By | Rows Affected |
| :--- | :--- | :--- | :--- | :--- |
| I01-R01 | 2026-02-25 | Initial draft — PHM delegation matrix | PHM Lead | All |

## 10. Approval

| Role | Name | Date | Signature |
| :--- | :--- | :--- | :--- |
| PHM Lead | ___________________ | __________ | __________ |
| Head of Design (DOA) | ___________________ | __________ | __________ |
| Head of Production (POA) | ___________________ | __________ | __________ |
| Quality Manager | ___________________ | __________ | __________ |
| STK_CERT Representative | ___________________ | __________ | __________ |
