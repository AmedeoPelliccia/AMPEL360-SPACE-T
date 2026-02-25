---
title: "K01 ATA 01 Tasklist — PHM Operations, Organization & Policy"
type: IDX
project: "AMPEL360"
program: "SPACET"
family: "Q10"
variant: "GEN"
version: "PLUS"
model: "BB"
block: "GEN"
phase: "LC01"
knot_task: "K01"
ata_code: "01"
aor: "PHM"
status: Draft
date: "2026-02-25"
owner: "Physical Hardware & Mechanical Engineering"
---

# K01 — Certification Authority Basis
## ATA 01 — Operations, Organization & Policy (PHM Scope)

## Uncertainty to Resolve (ATA-specific)

- Which organizational policies govern PHM engineering authority and delegation?
- How is the PHM AoR structured within the AMPEL360 Design Organization Approval (DOA)?
- What are the PHM-specific maintenance philosophy and design philosophy documents required for type certification?
- How does PHM coordinate with CERT for means of compliance (MoC) agreements?
- What competency requirements apply to PHM signatories (DER, CVE, stress engineers)?

## Tasks (minimum set)

| Task ID | Description | Owner | Evidence Type | Target Phase | Status |
|---------|-------------|-------|---------------|-------------|--------|
| K01-T001 | Define PHM organizational chart within DOA/POA structure | PHM Lead | ORG chart + delegation matrix | LC01 | 🟡 In Progress — see [EVIDENCE/](./EVIDENCE/) |
| K01-T002 | Establish PHM engineering authority delegation (stress, materials, systems) | PHM Lead + CERT | Delegation of Authority document | LC01 | |
| K01-T003 | Define PHM maintenance philosophy (MSG-3/RCM approach for hardware) | PHM + MRO | Maintenance philosophy document | LC02 | |
| K01-T004 | Map PHM-owned ATA chapters to applicable certification specifications (CS-25, ECSS, 14 CFR) | PHM + CERT | Compliance matrix | LC01 | |
| K01-T005 | Define competency and training requirements for PHM signatories | PHM + QA | Competency register | LC01 | |
| K01-T006 | Establish PHM interface control with SE, SAF, CERT, TEST stakeholders | PHM + SE | ICD register | LC02 | |
| K01-T007 | Record decisions; update baseline and trace links | PHM + CM | Decision record + CM baseline | LC02 | |

## Task Structure

See subdirectories for:
- **TASKS/**: Detailed scope, acceptance criteria, evidence links, and closure records per task
- **DECISIONS/**: Certification and engineering authority decisions
- **EVIDENCE/**: Evidence inventory and packages (org charts, delegation matrices)
- **MONITORING/**: NKU tracking and action register
- **LINKS/**: Related PRs, issues, and cross-stakeholder references

## Cross-Dependencies

| Stakeholder | Dependency | Direction |
|-------------|-----------|-----------|
| **CERT** | Regulatory framework; DOA/POA approval basis | CERT → PHM |
| **SE** | Systems architecture; ICD structure | SE ↔ PHM |
| **SAF** | Safety policy integration; design safety philosophy | SAF → PHM |
| **QA** | Quality system; competency framework | QA → PHM |
| **MRO** | Maintenance philosophy; inspection requirements | PHM → MRO |
| **CM** | Baseline management; configuration control | PHM → CM |

## Acceptance Criteria

- [ ] PHM organizational structure documented and approved by CERT
- [ ] Engineering authority delegation matrix signed off
- [ ] Maintenance philosophy document drafted (MSG-3/RCM basis)
- [ ] All PHM ATA chapters mapped to applicable certification specs
- [ ] Competency register established for PHM signatories
- [ ] Interface agreements recorded with SE, SAF, CERT, TEST
- [ ] Decision record filed; CM baseline updated

## Parent References

- **K01 Overview:** `../../00_AMPEL360_SPACET_Q10_CERT_PLUS_BB_GEN_LC01_K01_PHM__k01-certification-authority-basis_IDX_I01-R01_ACTIVE.md`
- **PHM Entry Point:** `../../../../00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_LC01_K01_PHM__stakeholder-phm-entrypoint_IDX_I01-R01_ACTIVE.md`
- **All ATA Tasks:** `../`

## Status

Draft — Populate tasks as K01 activities are executed for ATA 01 within PHM scope.
