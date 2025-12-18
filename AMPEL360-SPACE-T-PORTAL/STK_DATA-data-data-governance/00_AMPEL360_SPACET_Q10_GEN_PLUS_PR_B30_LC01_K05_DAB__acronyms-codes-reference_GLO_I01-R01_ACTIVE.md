---
title: "Glossary: Acronyms and Codes (CAXS / AMPEL360 Space-T)"
type: GLO
project: "AMPEL360"
program: "SPACET"
variant: "GEN"
domain: "N-NEURAL_NETWORKS"
stakeholder_id: "DATA"
status: ACTIVE
---

# Glossary — Acronyms and Codes (CAXS / AMPEL360 Space-T)

## Introduction

This glossary defines acronyms, codes, and terminology used throughout the AMPEL360 Space-T project. It serves as the single source of truth for understanding governance structures, repository organization, engineering terms, and process controls.

## Usage Guidelines

- Terms are organized by category (Governance, Repository Structure, Engineering, Process, Program Tokens)
- Cross-references use → symbol
- Standard definitions reference source standards where applicable
- All governance tokens (STK codes, AoR designations) are defined here

---

## A) Governance / Ownership (AoR / STK codes)

| Acronym | Meaning | Used for |
|---|---|---|
| **AoR** | Area of Responsibility | Portal entry point + accountable owner for an ATA root / solution pack |
| **STK_CM** | Configuration Management | Naming standard, change control, baselines, registers, release governance |
| **STK_PMO** | Program Management Office | Planning, schedule, cost, risk, gates, stakeholder/program governance |
| **STK_SE** | Systems Engineering (Architecture & MBSE Governance) | Architecture, SysML/MBSE, ICD governance, requirements structure, integration governance |
| **STK_SPE** | Software & Prompting Engineering | Software engineering, agent prompting/specs, automation pipelines, toolchains, CLIs, scripts |
| **STK_PHM** | Physical & Mechanical Engineering | Aerostructures, mechanisms, hydraulics, pneumatics, actuation, landing gear, physical integration |
| **STK_SAF** | Safety | FHA/PSSA/SSA logic, hazard controls, safety constraints, operational limits safety evidence |
| **STK_CERT** | Certification / Compliance | Compliance evidence, certification packs, authority-facing deliverables |
| **STK_TEST** | Test / Verification & Validation | Test planning/execution, benches, results, anomalies, VV evidence generation |
| **STK_OPS** | Operations | ConOps, procedures, readiness, operational baselines and operational evidence |
| **STK_MRO** | Maintenance, Repair & Overhaul | Maintenance plans, servicing, facilities/tooling, maintainability evidence |
| **STK_DATA** | Data / Digital / Traceability | Data governance, schemas, SSOT, traceability graph, DPP, SBOM/BOM exports |
| **STK_AI** | AI / ML Engineering & Assurance | Model registry, AI validation, monitoring, AI governance and assurance |
| **STK_CY** | Cybersecurity | IAM, ZTA, secure networks, hardening, cyber evidence and security controls |
| **STK_SPACEPORT** | Spaceport / Ground Segment | Spaceport interfaces, off-board infrastructure, range constraints, emergency response |

> **Note:**  
> *"AoR owner" in the table is the primary accountable STK. The "STKs cross dependencies" are collaborating AoRs.*

---

## B) Repository Structure / Domains

| Acronym | Meaning | Used for |
|---|---|---|
| **O-OPS/ORG** | Operations / Organization domain | Policy, ops governance, readiness, operational limits documentation |
| **P-PROGRAM** | Program domain | Governance, planning, registers, baselines, audits |
| **T-TECHNOLOGY** | On-board / vehicle technology domain | Vehicle systems and product subsystems |
| **I-INFRASTRUCTURES** | Off-board / infrastructure domain | Spaceport/ground systems, facilities, energy/cryo services |
| **N-NEURAL_NETWORKS** | AI/Data/DPP/Traceability domain | Model lifecycle, schemas, trace graph, DPP, registers |
| **T-SIMTEST** | Simulation & Test domain (OPT-INS S-axis in practice) | SIL/HIL/PIL, campaigns, VV evidence, archives |

---

## C) Engineering / Evidence Terms

| Acronym | Meaning | Used for |
|---|---|---|
| **MBSE** | Model-Based Systems Engineering | SysML architecture/governance, ICD structure |
| **SysML** | Systems Modeling Language | Architecture models, interfaces, behavior/state models |
| **ICD** | Interface Control Document | Interface definitions and control between subsystems |
| **V&V / VV** | Verification & Validation | Demonstrating requirements met + system fit-for-use |
| **FHA** | Functional Hazard Assessment | Safety hazard identification at functional level |
| **PSSA** | Preliminary System Safety Assessment | Early allocation of safety requirements/mitigations |
| **SSA** | System Safety Assessment | Final safety case evidence and compliance demonstration |
| **PHM** | (In industry) Prognostics & Health Management | Here **STK_PHM** means **Physical & Mechanical**; CMS/health monitoring is handled under **STK_DATA** with ops/MRO deps |
| **DPP** | Digital Product Passport | Provenance, materials, compliance, lifecycle identity |
| **SBOM** | Software Bill of Materials | Export of SW components/dependencies for assurance |
| **BOM** | Bill of Materials | HW/SW/Model BOM export for configuration & certification |
| **SSOT** | Single Source of Truth | Canonical data model / ontologies / registries |

---

## D) Process / Controls (as used in your governance language)

| Acronym | Meaning | Used for |
|---|---|---|
| **CM** | Configuration Management | Change control, baselines, naming/ID governance |
| **CI** | Continuous Integration | Automated validation gates (PR-blocking) |
| **Gate** | Governance validation step | PLC/validator gates, pass/fail evidence |
| **PLC** | Process Logic Controller | Logical validators enforcing nomenclature/ontology constraints |
| **KNOT (K01..K14)** | Controlled process knot | Governed workflow nodes; IDs must remain within K01..K14 |
| **NKU** | New Knowledge Unit | Every artifact is implicitly an NKU; not encoded in filename |

---

## E) Program Tokens (per your convention)

| Token | Meaning | Used for |
|---|---|---|
| **AIRT** | Advanced (Manned) Air Transport | Program token for aircraft environment |
| **SPACET** | Advanced Space Transport | Program token for spacecraft environment |
| **FAMILY** | Family identifier | Quantum-inspired + pax payload numbering (e.g., Q10, Q100) |
| **VARIANT** | Operating / certification context | GEN, BASELINE, FLIGHT_TEST, CERT, MSN, CUST, etc. |
| **VERSION** | Branding / product line | PLUS, PLUSULTRA (branding reinforcer) |
| **MODEL** | Artifact model class | BB (Body-Brain PR-O-RO), HW, SW, PR (Process) |

---

## Quick Reference: Common Acronyms

| Acronym | Full Form |
| :--- | :--- |
| ANA | Analysis |
| AoR | Area of Responsibility |
| ATA | Air Transport Association |
| BOM | Bill of Materials |
| CAT | Catalog |
| CI | Continuous Integration |
| CM | Configuration Management |
| DAL | Development Assurance Level |
| DPP | Digital Product Passport |
| FHA | Functional Hazard Assessment |
| FTA | Fault Tree Analysis |
| GLO | Glossary |
| ICD | Interface Control Document |
| IDX | Index |
| LOG | Log |
| LST | List |
| MAT | Material |
| MBSE | Model-Based Systems Engineering |
| MIN | Minutes |
| NKU | New Knowledge Unit |
| PHM | Physical & Mechanical (also: Prognostics & Health Management in industry) |
| PLC | Process Logic Controller |
| PLAN | Plan |
| PSSA | Preliminary System Safety Assessment |
| REQ | Requirements |
| RPT | Report |
| SBOM | Software Bill of Materials |
| SCH | Schema |
| SSA | System Safety Assessment |
| SSOT | Single Source of Truth |
| STD | Standard |
| STK | Stakeholder |
| SysML | Systems Modeling Language |
| TRC | Traceability |
| V&V / VV | Verification & Validation |

---

## References

- DO-178C: Software Considerations in Airborne Systems and Equipment Certification
- DO-254: Design Assurance Guidance for Airborne Electronic Hardware
- SAE ARP4761: Guidelines and Methods for Conducting the Safety Assessment Process
- ECSS-M-ST-10C: Project Planning and Implementation
- AMPEL360 Nomenclature Standard v6.0 R1.0
- OPT-INS Framework Standard v1.1

---

## Maintenance

**Maintained By:** STK_DATA (Data Governance)  
**Last Updated:** 2025-12-18  
**Review Cycle:** Quarterly or upon major standard updates

### Change History

| Date | Term/Section | Action | Changed By |
| :--- | :--- | :--- | :--- |
| 2025-12-18 | All sections | Initial version with 5 main categories (A-E) | STK_DATA |

---

## Notes

This glossary is maintained under Data Governance and aligned with:
- Nomenclature Standard v6.0 R1.0 (FINAL LOCK)
- OPT-INS Framework v1.1
- K05 Data Governance knot
- ATA 00 (GENERAL) program governance baseline

> If you want, I can append this glossary directly under the table as a single consolidated Markdown section (table + glossary in one file-ready block).
