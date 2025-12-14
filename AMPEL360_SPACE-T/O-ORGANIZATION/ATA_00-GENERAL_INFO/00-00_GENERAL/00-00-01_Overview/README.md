---
document_id: ATA_00-00-01_Overview
program: AMPEL360_SPACE-T
axis: O-ORGANIZATION
ata_chapter: ATA_00-GENERAL_INFO
lifecycle_node: 00-00_GENERAL/00-00-01_Overview
title: "AMPEL360 Space-T — Program Overview"
version: "0.2.1"
status: DRAFT
classification: INTERNAL
owner: AMPEL360 Space-T Program Board (O-Axis)
author: IDEALEeu / AMPEL360 Documentation WG
date: 2025-12-14
language: EN
---


# 1. PURPOSE

Define the **program-level overview** for AMPEL360 Space-T, including mission, vision, scope, lifecycle model (BRAVOS), governance logic, and market-driven baseline intent.

---

# 2. MISSION

Provide a **certifiable, service-ready Space-T transport capability** enabling human and payload transport across defined near-space and orbital missions, supported by evidence-based engineering and lifecycle traceability.

---

# 3. VISION

Establish AMPEL360 Space-T as a **reference space transport program** in which:

* Market demand drives baseline definition
* Verification enables operations
* Fleet feedback governs evolution
* Governance ensures safety and sustainability

---

# 4. SCOPE

## 4.1 In Scope

* Program governance and lifecycle control (O-Axis)
* Market and mission trade studies
* Baseline and variant selection logic
* Operations, sustainment, and fleet feedback integration
* High-level execution planning and phase gating

## 4.2 Out of Scope

* Detailed system architectures (T-Axis)
* Certification compliance matrices
* Cost, funding, and investor documentation

---

# 5. PROGRAM OPERATING MODEL (BRAVOS)

## 5.1 BRAVOS Definition

The AMPEL360 Space-T program follows the **BRAVOS lifecycle**:

* **B** — Baselines
* **R** — Requirements
* **A** — Architecture
* **V** — Verification & Validation
* **O** — Operations (OPS)
* **S** — Sustainment

## 5.2 BRAVOS Lifecycle Flow

```mermaid
flowchart LR
    OX[O-Axis Governance] --> M[Market & Mission Trade Studies]
    M --> B[Baseline Selection - Variants]
    B --> R[Requirements Seed]
    R --> A[Architecture & Design]
    A --> V[Verification & Validation]
    V --> OPS[Operations & Service Readiness]
    OPS --> S[Sustainment]
    S --> F[Fleet Operations Feedback]
    F --> B
```

---

# 6. GOVERNANCE (O-AXIS)

## 6.1 Governance Principle

No technical baseline shall exist without explicit **market, operational, and sustainment justification**.

## 6.2 Governance Bodies

| Body                              | Responsibility                         | Controlled Outputs                       |
| --------------------------------- | -------------------------------------- | ---------------------------------------- |
| Program Board                     | Strategy, market approval, phase gates | Segment approval, baseline authorization |
| Technical Authority               | Architectural integrity                | Architecture budgets, interface rules    |
| Safety & Assurance                | Hazard and evidence integrity          | Safety cases, assurance packages         |
| OPS & Services Council            | Operational viability                  | ConOps, OPS readiness criteria           |
| Configuration Control Board (CCB) | Baseline stability                     | Change approvals, configuration tags     |

---

# 7. MARKET AND MISSION TRADE STUDIES

## 7.1 Purpose

Define **market justification** for each baseline prior to engineering commitment.

## 7.2 Initial Market Segments

* Suborbital human experience
* Near-space high-speed transport
* Commercial crew logistics
* Microgravity research operations
* High-value payload logistics
* In-space servicing support

## 7.3 Evaluation Criteria

Each segment shall be evaluated against:

* Certification tractability
* Technical feasibility
* Operational scalability
* Revenue density
* Infrastructure readiness
* Portfolio synergy
* Risk concentration

Only segments meeting **OPS and sustainment viability thresholds** may proceed.

---

# 8. BASELINE AND VARIANT PHILOSOPHY

## 8.1 Baseline Definition

A baseline represents a **service-capable configuration**, not a static design snapshot.

## 8.2 Baseline Classes

| Baseline Class     | Purpose                                 |
| ------------------ | --------------------------------------- |
| Demonstrator       | Risk retirement and evidence generation |
| Entry Baseline     | Initial operational service             |
| Expansion Baseline | Envelope and market growth              |
| Family Baseline    | Multi-mission platform reuse            |

All baselines remain subject to controlled evolution.

---

# 9. OPERATIONS (OPS)

Operations are a **mandatory lifecycle phase**, including:

* Operational procedures
* Training concepts
* Turnaround and maintainability targets
* Dispatch reliability metrics
* Customer service interfaces

Verification is incomplete until OPS readiness is achieved.

---

# 10. SUSTAINMENT AND FLEET FEEDBACK

Sustainment provides authoritative feedback through:

* Reliability trends
* Maintenance burden
* Software and AI performance behavior
* Human-factors observations
* Cost and utilization deltas

Fleet feedback shall directly inform baseline evolution under CCB control.

---

# 11. OPT-IN AXIS INTERFACES

* **P-PROGRAM:** schedules, milestones, cost control
* **T-TECHNOLOGY:** system and vehicle architectures
* **I-INFRASTRUCTURES:** ground segment and support systems
* **N-NEURAL NETWORKS:** AI lifecycle, monitoring, assurance

---

# 12. NEXT ACTIONS

1. Freeze BRAVOS lifecycle as program standard
2. Approve market segment shortlist
3. Define OPS readiness criteria per segment
4. Establish fleet-to-CCB feedback process
5. Align CI/CD ownership with BRAVOS phases

---

# 13. REVISION HISTORY

| Version | Date       | Description                            |
| ------- | ---------- | -------------------------------------- |
| 0.2.1   | 2025-12-14 | Normalized ATA-style heading structure |

```

