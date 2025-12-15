---
title: "K01 RACI & Decision Rights Diagram"
type: DIA
project: "AMPEL360"
program: "SPACET"
variant: "PLUS"
status: "DRAFT"
knot_id: "K01"
lc_or_subbucket: "SB90"
bucket: "90"
generated: "2025-12-15"
---

# K01 — RACI & Decision Rights (Diagram)

## Links (GitHub-navigable)
- K01 Assets index: **[00_00_IDX_LC01_AMPEL360_SPACET_PLUS_k01-assets-index_v01.md](../00_00_IDX_LC01_AMPEL360_SPACET_PLUS_k01-assets-index_v01.md)**
- Compliance workflow (MD): **[00_90_DIA_SB90_AMPEL360_SPACET_PLUS_k01-compliance-workflow_v01.md](./00_90_DIA_SB90_AMPEL360_SPACET_PLUS_k01-compliance-workflow_v01.md)**
- Authority model overview (SVG): **[00_90_DIA_SB90_AMPEL360_SPACET_PLUS_k01-authority-model-overview_v01.svg](./00_90_DIA_SB90_AMPEL360_SPACET_PLUS_k01-authority-model-overview_v01.svg)**

## 1) Purpose
This diagram defines **decision rights and RACI** for **K01 (certification-authority-basis)** across portal stakeholders, ensuring:
- unambiguous ownership (AoR) at portal entry points,
- controlled baseline authority and release governance,
- clear cross-dependencies (consulted/informed),
- explicit gating for **CI**, **NKU**, and **TEKNIA evidence-first sharing**.

## 2) Decision Types (K01)
- **D1 — Certification Basis & Tailoring** (regulations, standards tailoring, special conditions)
- **D2 — Means of Compliance & Verification Strategy** (MoC mapping, V&V scope)
- **D3 — Evidence Pack Definition & Audit Query Contract** (schemas, trace links, evidence structure)
- **D4 — Baseline Release / Signed Export Packs** (release approvals, signatures, publication)
- **D5 — RBAC & Portal Effectivity** (workspace access grants, STK permissions, visibility)

## 3) RACI Matrix (Decision Rights)

> R = Responsible (executes)  
> A = Accountable (final decision)  
> C = Consulted (must be consulted)  
> I = Informed (notified)

| Decision | CERT | CM | PMO | SE | SAF | DATA | CY | TEST | OPS | SPACEPORT | QA/Process |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **D1 Certification Basis & Tailoring** | **A/R** | C | I | C | C | C | C | I | I | I | C |
| **D2 MoC & Verification Strategy** | **A** | C | I | **R** | C | C | C | **R** | I | I | C |
| **D3 Evidence Pack & Audit Contract** | **A** | **A** | I | C | C | **R** | C | C | I | I | **R** |
| **D4 Baseline Release / Signed Exports** | **A** | **A/R** | I | C | C | C | **R** (signing) | C | I | I | C |
| **D5 RBAC & Portal Effectivity** | C | **A/R** | I | C | C | **R** (data access) | **R** (security) | I | I | I | C |

### Notes on split-accountability
- **D3 / D4** deliberately use **shared accountability** between **CERT** (regulatory acceptability) and **CM** (baseline authority, release control).  
- If your governance requires single-A only, set **CM=A** for D4 and **CERT=A** for D1–D2, keeping the other as mandatory **C**.

## 4) RACI by Artifact Family (where decisions land)

| Artifact / Location | Primary AoR | Approval Authority | Minimum consulted |
|---|---|---|---|
| `.../K01.../ATA_TASKS/*/DECISIONS/*decision-record*` | CERT | CERT + CM | SE, QA, DATA |
| `.../K01.../ATA_TASKS/*/EVIDENCE/*manifest*` | DATA | CERT + CM | TEST, QA, CY |
| `.../K01.../ASSETS/SCHEMAS/*` | DATA | CM + CERT | SE, QA |
| `.../K01.../ASSETS/TABLES/*rbac-role-matrix*` | CM | CM | CY, DATA |
| `.../K01.../ASSETS/DIAGRAMS/*` | CERT | CERT | CM, SE |

## 5) Mermaid (GitHub-renderable)

### 5.1 Stakeholder authority map (AoR + approvals)
```mermaid
flowchart LR
  CERT["STK_CERT (AoR)<br/>Certification Authority Basis"] -->|A for D1/D2, joint A for D3/D4| DEC["K01 Decisions"]
  CM["STK_CM (AoR)<br/>Baseline + Change Control"] -->|joint A for D3/D4, A for D5| DEC

  SE["STK_SE<br/>System scope & interfaces"] -->|C| DEC
  SAF["STK_SAF<br/>Hazard/Safety case"] -->|C| DEC
  DATA["STK_DATA<br/>Schemas/SSOT/Evidence structure"] -->|R for D3| DEC
  CY["STK_CY<br/>Signing/Key mgmt/Security"] -->|R for D4 signing + D5 security| DEC
  TEST["STK_TEST<br/>IVVQ & test evidence"] -->|R for D2 execution + evidence| DEC
  QA["QA/Process"] -->|R for process audits| DEC
  OPS["STK_OPS"] -->|I| DEC
  SPACEPORT["STK_SPACEPORT"] -->|I| DEC
  PMO["STK_PMO"] -->|I| DEC
````

### 5.2 Decision gating (CI → NKU → TEKNIA → Release)

```mermaid
flowchart TD
  P["PR / Change submitted"] --> CI["CI Gates<br/>nomenclature • metadata • schema • links • trace"]
  CI -->|fail| F["Fix + iterate"]
  CI -->|pass| NKU["NKU Gate<br/>critical open blocks closure"]
  NKU -->|blocked| A["Open actions + mitigation plan"]
  NKU -->|clear| DR["Decision Record approvals<br/>CERT + CM"]
  DR --> TEK["TEKNIA evidence-first check<br/>reproducible audit path"]
  TEK -->|hold| H["Internal-only until evidence complete"]
  TEK -->|ok| R["Baseline/Release update<br/>CM-controlled + signed if needed"]
```

## 6) Implementation comment (why this matters)

* This RACI model prevents “silent ownership drift” when K01 touches multiple ATAs and axes.
* It aligns portal entry points (AoR) with **release authority** and **evidence accountability**, which is essential for certification-grade audits.



