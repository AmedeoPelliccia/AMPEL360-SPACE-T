---
title: "Backlog Knot K10: industrialization-supplychain-quality"
type: IDX
variant: "SPACET"
status: Draft
knot_id: "K10"
stakeholder_id: "PHM"
affected_atas: ["00", "05", "10", "20", "51", "70", "80", "82", "89", "100", "115"]
---

# Backlog Knot K10 — Industrialization, Supply Chain & Quality (PHM Scope)

## Problem Statement

Define the industrialization strategy, supply chain architecture, and quality requirements for PHM hardware manufacturing and assembly. Establish make-or-buy decisions, supplier qualification criteria, and manufacturing readiness levels for structural, mechanical, and propulsion hardware.

## Scope Boundary
- In-scope: Hardware manufacturing processes, supplier qualification for structural/mechanical parts, material procurement strategy, manufacturing readiness levels, quality inspection criteria
- Out-of-scope: Software supply chain (SW AoR), MRO logistics (MRO AoR)

## PHM ATA Impact Breakdown

| ATA | Chapter Title | K10 Relevance |
|-----|--------------|---------------|
| 00 | General | Cross-cutting industrialization framework |
| 05 | Time Limits / Maintenance Checks | Manufacturing-driven maintenance |
| 10 | Parking, Mooring, Storage | Storage/handling of hardware |
| 20 | Standard Practices - Airframe | Airframe manufacturing standards |
| 51 | Standard Practices & Structures | Structural manufacturing processes |
| 70 | Engine / Propulsion (General) | Propulsion hardware manufacturing |
| 80 | Starting | Starter system supply chain |
| 82 | Water Injection | Injection system manufacturing |
| 89 | SpaceT Propulsion Integration | Propulsion integration manufacturing |
| 100 | SpaceT-specific | Novel configuration manufacturing |
| 115 | SpaceT Structural | Structural assembly processes |

## Tasks (minimum set)

1. Define make-or-buy strategy for PHM hardware domains
2. Establish supplier qualification criteria for structural/mechanical parts
3. Define manufacturing readiness level targets per ATA domain
4. Establish quality inspection and acceptance criteria
5. Record decisions; update baseline and trace links

## Cross-Dependencies

- **PMO** — Program schedule and budget
- **CM** — Configuration control of manufacturing data
- **MRO** — Maintenance-driven manufacturing requirements
- **TEST** — Production test requirements

## Decision & Closure Criteria
- Decision owner: PHM + PMO leads
- Evidence required: Make-or-buy matrix, supplier qualification plan, MRL assessment
- Acceptance criteria:
  - [ ] Make-or-buy decisions recorded for all critical hardware
  - [ ] Supplier qualification criteria defined
  - [ ] Manufacturing readiness levels assessed
  - [ ] Baseline updated (CM)

## Pathways
1) Requirements/ConOps
2) Architecture/ICDs
3) Implementation/Industrialization
4) Verification/Qualification
5) Baseline & Release
