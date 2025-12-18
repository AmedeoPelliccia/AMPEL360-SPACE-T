---
title: "AMPEL360-SPACE-T-PORTAL — Stakeholder Entry Points"
type: IDX
variant: "SPACET"
status: Draft
bucket: "00"
lc_or_subbucket: "LC01"
description: "Primary navigation index for stakeholder workspaces (entrypoints + execution lanes) in AMPEL360 Space-T."
owner: "Configuration Management WG"
---

# AMPEL360-SPACE-T-PORTAL — Stakeholder Entry Points

This index provides the **single, GitHub-navigable entry point** to each stakeholder workspace under **AMPEL360-SPACE-T-PORTAL/**.

Conventions:
- Each stakeholder has a dedicated folder: `STK_<ID>-<slug>/`
- Each folder contains one canonical entrypoint file: `00_00_IDX_LC01_SPACET_stakeholder-<id>-entrypoint_I01-R01.md`
- Stakeholder work is organized by **KNOTS/** → **ATA_TASKS/** → ATA-specific IDXs.

---

## Stakeholders

### CM — Configuration Management
- Entry point: [CM — Configuration Management](STK_CM-cm-configuration-management/00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_LC01_K04_CM__stakeholder-cm-entrypoint_IDX_I01-R01_ACTIVE.md)  
  _Comment:_ Governance spine (nomenclature, baselines, change control, approvals, CI enforcement). Owns closure discipline.
- Workspace: [STK_CM-cm-configuration-management/](STK_CM-cm-configuration-management/)  
  _Comment:_ CM execution lanes, decisions, registers, and PR gatekeeping.

### PMO — Program Management Office
- Entry point: [PMO — Program Management Office](STK_PMO-pmo-program-management-office/00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_LC01_K04_PMO__stakeholder-pmo-entrypoint_IDX_I01-R01_ACTIVE.md)  
  _Comment:_ Program cadence, milestones, resourcing, and portfolio prioritization of knots.
- Workspace: [STK_PMO-pmo-program-management-office/](STK_PMO-pmo-program-management-office/)  
  _Comment:_ Delivery pathways, schedules, and program-level reporting.

### SE — Systems Engineering
- Entry point: [SE — Systems Engineering](STK_SE-se-systems-engineering/00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_LC01_K04_SE__stakeholder-se-entrypoint_IDX_I01-R01_ACTIVE.md)  
  _Comment:_ System architecture, ICDs, requirements decomposition, and cross-ATA interfaces.
- Workspace: [STK_SE-se-systems-engineering/](STK_SE-se-systems-engineering/)  
  _Comment:_ Interface governance and system-level assurance artifacts.

### SAF — Safety
- Entry point: [SAF — Safety](STK_SAF-saf-safety/00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_LC01_K02_SAF__stakeholder-saf-entrypoint_IDX_I01-R01_ACTIVE.md)  
  _Comment:_ Safety processes, hazard logs, safety cases, and evidence expectations (air/space worthiness).
- Workspace: [STK_SAF-saf-safety/](STK_SAF-saf-safety/)  
  _Comment:_ Safety knots, ATA linkages, and closure verification.

### CERT — Certification & Authorities
- Entry point: [CERT — Certification & Authorities](STK_CERT-cert-certification-authorities/00_AMPEL360_SPACET_Q10_CERT_PLUS_BB_GEN_LC01_K01_CERT__stakeholder-cert-entrypoint_IDX_I01-R01_ACTIVE.md)  
  _Comment:_ Authority engagement, compliance mapping, evidence packaging rules, audit readiness.
- Workspace: [STK_CERT-cert-certification-authorities/](STK_CERT-cert-certification-authorities/)  
  _Comment:_ Compliance pathways and evidence acceptance criteria.

### OPS — Operations
- Entry point: [OPS — Operations](STK_OPS-ops-operations/00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_LC01_K04_OPS__stakeholder-ops-entrypoint_IDX_I01-R01_ACTIVE.md)  
  _Comment:_ Operational concepts, procedures, mission profiles, operational constraints and feedback loops.
- Workspace: [STK_OPS-ops-operations/](STK_OPS-ops-operations/)  
  _Comment:_ Ops-driven knots and operational readiness evidence.

### SPACEPORT — Spaceport/Airport Ops
- Entry point: [SPACEPORT — Spaceport/Airport Ops](STK_SPACEPORT-spaceport-spaceport-airport-ops/00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_LC01_K04_SPACEPORT__stakeholder-spaceport-entrypoint_IDX_I01-R01_ACTIVE.md)  
  _Comment:_ Off-board infrastructure coupling (ground ops, turnaround, fueling/servicing interfaces, constraints).
- Workspace: [STK_SPACEPORT-spaceport-spaceport-airport-ops/](STK_SPACEPORT-spaceport-spaceport-airport-ops/)  
  _Comment:_ Infrastructure-driven uncertainties and adoption pathways.

### MRO — MRO / Maintenance
- Entry point: [MRO — MRO / Maintenance](STK_MRO-mro-mro-maintenance/00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_LC01_K04_MRO__stakeholder-mro-entrypoint_IDX_I01-R01_ACTIVE.md)  
  _Comment:_ Maintainability, servicing, inspection, and evidence trails for continued air/space worthiness.
- Workspace: [STK_MRO-mro-mro-maintenance/](STK_MRO-mro-mro-maintenance/)  
  _Comment:_ Maintenance knots, tasking, and artifact readiness.

### DATA — Data Governance
- Entry point: [DATA — Data Governance](STK_DATA-data-data-governance/00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_LC01_K05_DATA__stakeholder-data-entrypoint_IDX_I01-R01_ACTIVE.md)  
  _Comment:_ SSOT definitions, schema governance, identifier discipline, data quality and stewardship.
- Workspace: [STK_DATA-data-data-governance/](STK_DATA-data-data-governance/)  
  _Comment:_ Registry ownership, dedup policies, and cross-ATA adoption controls.

### AI — AI/ML Engineering
- Entry point: [AI — AI/ML Engineering](STK_AI-ai-ai-ml-engineering/00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_LC01_K11_AI__stakeholder-ai-entrypoint_IDX_I01-R01_ACTIVE.md)  
  _Comment:_ ML lifecycle, dataset/model governance, automated validation, TEKNIA/NKU instrumentation.
- Workspace: [STK_AI-ai-ai-ml-engineering/](STK_AI-ai-ai-ml-engineering/)  
  _Comment:_ AI execution lane (KNOTS/ → ATA partitioning → evidence packs).

### CY — Cybersecurity
- Entry point: [CY — Cybersecurity](STK_CY-cy-cybersecurity/00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_LC01_K04_CY__stakeholder-cy-entrypoint_IDX_I01-R01_ACTIVE.md)  
  _Comment:_ Threat models, security requirements, secure-by-design controls, vulnerability governance (incl. SBOM coupling).
- Workspace: [STK_CY-cy-cybersecurity/](STK_CY-cy-cybersecurity/)  
  _Comment:_ Security knots and policy gates linked to CI enforcement.

### TEST — IVVQ / Testing
- Entry point: [TEST — IVVQ / Testing](STK_TEST-test-ivvq-testing/00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_LC01_K04_TEST__stakeholder-test-entrypoint_IDX_I01-R01_ACTIVE.md)  
  _Comment:_ Verification strategy, test evidence nodes (100+), qualification readiness, reproducible evidence chains.
- Workspace: [STK_TEST-test-ivvq-testing/](STK_TEST-test-ivvq-testing/)  
  _Comment:_ Test campaigns, evidence packs, and trace closure routines.

### PHM — Physical Hardware & Mechanical Engineering
- Entry point: [PHM — Physical Hardware & Mechanical Engineering](STK_PHM-phm-physical-hardware-mechanical-engineering/00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_LC01_K01_PHM__stakeholder-phm-entrypoint_IDX_I01-R01_ACTIVE.md)  
  _Comment:_ Physical hardware domains including aerostructures, landing gear, pneumatics, flight control, hydraulics, and materials.
- Workspace: [STK_PHM-phm-physical-hardware-mechanical-engineering/](STK_PHM-phm-physical-hardware-mechanical-engineering/)  
  _Comment:_ Hardware-centric knots, structural integrity, actuation, and maintainability evidence.

---

## How to use this portal (minimum workflow)

1. Start from your stakeholder entrypoint.
2. Navigate to `KNOTS/` and select the active Knot (e.g., K06).
3. Inside the Knot, use `ATA_TASKS/` and open the relevant ATA tasklist (IDX).
4. Close uncertainty by partitions (IDs/Schema/Exports/CI/Evidence/Decisions/Adoption), then update NKU ledgers.

---

## Active knots (optional curated shortcuts)

- K06 — Data Governance (SSOT / Schemas / Identifiers)  
  - AI lane: [STK_AI K06](STK_AI-ai-ai-ml-engineering/KNOTS/K06_data-governance-ssot-schemas-identifiers/)  
  - Master K06 index: [K06 master index](STK_DATA-data-data-governance/KNOTS/K06_data-governance-ssot-schemas-identifiers/00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_LC01_K06_DATA__k06-data-governance-ssot-schemas-identifiers_IDX_I01-R01_ACTIVE.md)
