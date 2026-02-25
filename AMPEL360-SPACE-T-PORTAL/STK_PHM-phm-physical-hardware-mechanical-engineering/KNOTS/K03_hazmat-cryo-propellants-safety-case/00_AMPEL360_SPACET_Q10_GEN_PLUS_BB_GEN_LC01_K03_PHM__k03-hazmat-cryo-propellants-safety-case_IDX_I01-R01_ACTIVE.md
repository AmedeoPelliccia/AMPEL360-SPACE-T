---
title: "Backlog Knot K03: hazmat-cryo-propellants-safety-case"
type: IDX
variant: "SPACET"
status: Draft
knot_id: "K03"
stakeholder_id: "PHM"
affected_atas: ["12", "18", "26", "28", "47", "78", "81", "84", "110"]
---

# Backlog Knot K03 — Hazmat / Cryo Propellants Safety Case (PHM Scope)

## Problem Statement

Establish the safety case for handling, storage, and containment of hazardous materials and cryogenic propellants across PHM-owned hardware. Define material compatibility, leak detection, and containment integrity requirements for novel propellant configurations.

## Scope Boundary
- In-scope: Propellant containment design, cryo-material compatibility, leak detection hardware, hazmat handling procedures for PHM hardware, fire/explosion protection
- Out-of-scope: Operational procedures (OPS AoR), spaceport ground handling (SPACEPORT AoR)

## PHM ATA Impact Breakdown

| ATA | Chapter Title | K03 Relevance |
|-----|--------------|---------------|
| 12 | Servicing | Propellant servicing hardware |
| 18 | Vibration & Noise Analysis | Cryo-induced vibration effects |
| 26 | Fire Protection | Propellant fire/explosion protection |
| 28 | Fuel / Propellant Systems | Primary propellant containment |
| 47 | Inerting Systems | Tank inerting for propellant safety |
| 78 | Exhaust / Thrust Reverser | Propulsion exhaust safety |
| 81 | Turbine / Turbopump | Cryo turbopump material compatibility |
| 84 | Propellant Systems | Cryo propellant distribution hardware |
| 110 | SpaceT Propulsion | Novel propulsion containment |

## Tasks (minimum set)

1. Define cryo-material compatibility matrix for PHM hardware
2. Establish containment integrity requirements and leak rate criteria
3. Map hazmat classification to PHM hardware components
4. Define fire/explosion protection design requirements
5. Record decisions; update baseline and trace links

## Cross-Dependencies

- **SAF** — Safety case owner, hazard analysis
- **CERT** — Regulatory compliance for hazmat
- **SPACEPORT** — Ground handling interfaces
- **TEST** — Cryo test campaign planning

## Decision & Closure Criteria
- Decision owner: SAF + PHM leads
- Evidence required: Material compatibility matrix, containment integrity analysis, hazmat classification
- Acceptance criteria:
  - [ ] Cryo-material compatibility verified for all propellant-wetted hardware
  - [ ] Containment integrity criteria defined and accepted
  - [ ] Hazmat handling procedures aligned with PHM hardware design
  - [ ] Baseline updated (CM)

## Pathways
1) Requirements/ConOps
2) Architecture/ICDs
3) Implementation/Industrialization
4) Verification/Qualification
5) Baseline & Release
