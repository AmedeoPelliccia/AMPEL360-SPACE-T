---
title: "Backlog Knot K01: certification-authority-basis"
type: IDX
variant: "SPACET"
status: Draft
knot_id: "K01"
stakeholder_id: "PHM"
affected_atas: ["00", "01", "04", "05", "18", "20", "21", "22", "24", "26", "27", "28", "42", "100", "109", "115"]
---

# Backlog Knot K01 — Certification Authority Basis (PHM Scope)

## Problem Statement

Define the regulatory framework, compliance basis, and certification authority relationships for all PHM-owned ATA chapters. Establish means of compliance (MoC) for structural, mechanical, and hardware domains covering airframe, flight controls, fuel/propellant, and hydraulic systems.

## Scope Boundary
- In-scope: Certification specifications mapping (CS/FAR/ECSS), means of compliance matrices, equivalent safety findings for novel materials/configurations, DER/CVE/ODA delegation structure for PHM disciplines
- Out-of-scope: Software certification (SW AoR), avionics qualification (CY AoR)

## PHM ATA Impact Breakdown

| ATA | Chapter Title | K01 Relevance |
|-----|--------------|---------------|
| 00 | General | Cross-cutting certification framework |
| 01 | Operations | Operational certification requirements |
| 04 | Airworthiness Limitations | Structural airworthiness limits |
| 05 | Time Limits / Maintenance Checks | Maintenance-driven certification |
| 18 | Vibration & Noise Analysis | Vibration certification basis |
| 20 | Standard Practices - Airframe | Structural certification basis |
| 21 | Air Conditioning / ECS | ECS airworthiness |
| 22 | Auto Flight | Auto-flight hardware certification |
| 24 | Electrical Power | Power system certification |
| 26 | Fire Protection | Fire protection compliance |
| 27 | Flight Controls | Control surface airworthiness |
| 28 | Fuel / Propellant Systems | Propellant containment certification |
| 42 | Integrated Modular Avionics | Hardware integration certification |
| 100 | SpaceT-specific | Novel configuration certification |
| 109 | SpaceT Thermal | Thermal protection certification |
| 115 | SpaceT Structural | Structural substantiation |

## Tasks (minimum set)

1. Map applicable certification specifications (CS/FAR/ECSS) to PHM ATA chapters
2. Define means of compliance matrix for structural substantiation
3. Identify equivalent safety findings needed for novel materials/configurations
4. Establish DER/CVE/ODA delegation structure for PHM disciplines
5. Record decisions; update baseline and trace links

## Cross-Dependencies

- **CERT** — Regulatory framework owner
- **SAF** — Safety case integration
- **SE** — Architecture-level ICD compliance
- **TEST** — Test plan alignment with MoC

## Decision & Closure Criteria
- Decision owner: CERT + PHM leads
- Evidence required: Certification basis document, MoC matrix, equivalent safety findings
- Acceptance criteria:
  - [ ] Certification basis document approved by CERT AoR
  - [ ] MoC matrix complete for all PHM ATA chapters
  - [ ] Equivalent safety findings identified and documented
  - [ ] Baseline updated (CM)

## Pathways
1) Requirements/ConOps
2) Architecture/ICDs
3) Implementation/Industrialization
4) Verification/Qualification
5) Baseline & Release
