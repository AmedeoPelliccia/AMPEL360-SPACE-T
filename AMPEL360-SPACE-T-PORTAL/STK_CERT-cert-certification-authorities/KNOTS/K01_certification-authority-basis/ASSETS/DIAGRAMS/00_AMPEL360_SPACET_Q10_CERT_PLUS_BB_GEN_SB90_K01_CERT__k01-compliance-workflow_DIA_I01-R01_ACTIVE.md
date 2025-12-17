---
title: "K01 Compliance Workflow Diagram"
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

# K01 — Compliance Workflow (Diagram)

## Links (GitHub-navigable)
- K01 Assets index: **[00_00_IDX_LC01_AMPEL360_SPACET_PLUS_k01-assets-index_I01-R01.md](../00_AMPEL360_SPACET_Q10_CERT_PLUS_BB_GEN_SB90_K01_CERT__k01-assets-index_IDX_I01-R01_ACTIVE.md)**
- Authority model overview (SVG): **[00_90_DIA_SB90_AMPEL360_SPACET_PLUS_k01-authority-model-overview_I01-R01.svg](./00_AMPEL360_SPACET_PLUS_90_DIA_SB90_K01_CERT__k01-authority-model-overview_I01-R01.svg)**
- RACI / decision rights (SVG/PDF if present):  
  - **[00_90_DIA_SB90_AMPEL360_SPACET_PLUS_k01-raci-decision-rights_I01-R01.svg](./00_90_DIA_SB90_AMPEL360_SPACET_PLUS_k01-raci-decision-rights_I01-R01.svg)**  
  - **[00_90_DIA_SB90_AMPEL360_SPACET_PLUS_k01-raci-decision-rights_I01-R01.pdf](./00_90_DIA_SB90_AMPEL360_SPACET_PLUS_k01-raci-decision-rights_I01-R01.pdf)**

## Diagram (Mermaid)
> This is the GitHub-renderable compliance workflow for **K01** across ATAs, with NKU gating, CI enforcement, RBAC effectivity, and TEKNIA sharing rules.

```mermaid
flowchart TD

%% ==========================================================
%% K01 Certification Authority Basis — Compliance Workflow
%% AMPEL360 / SPACET / PLUS
%% ==========================================================

START(["Trigger: New/Changed requirement, design change, or authority request"])

%% --- Inputs ---
START --> IN1["Input A: Certification Basis update<br/>Regulations • ECSS/DO/CS tailoring • Special conditions"]
START --> IN2["Input B: System change request<br/>Design delta • SW/HW change • Ops/Infra change"]
START --> IN3["Input C: Evidence gap / audit finding<br/>Missing trace • weak MoC • NKU opened"]

%% --- Governance / Effectivity ---
IN1 --> GOV["K01 Governance (ATA 00)<br/>Decision owner: CERT<br/>Baseline authority: CM"]
IN2 --> GOV
IN3 --> GOV

GOV --> RBAC["RBAC & Effectivity Check<br/>Portal workspace access grants by STK<br/>LC/SB constraints enforced"]
RBAC -->|Denied| STOP1(["STOP: Access not granted<br/>Request RBAC update"])
RBAC -->|Granted| SCOPE["Define scope & affected ATAs<br/>ATA impact map + interfaces"]

%% --- Plan & Requirements ---
SCOPE --> T001["T001: Certification Basis Definition<br/>Scope • authorities • tailoring • engagement plan"]
SCOPE --> T002["T002: Compliance Mapping<br/>MoC • verification • trace targets"]
T001 --> AC["Acceptance Criteria (REQ)<br/>Per ATA: AC-XX-YYY"]
T002 --> AC

%% --- Implementation + Evidence ---
AC --> WORK["Execute work in affected ATA taskspaces<br/>TASKS → EVIDENCE → DECISIONS → MONITORING"]
WORK --> EVID["Assemble Evidence Pack (EVIDENCE/)"]
EVID --> MAN["Evidence Pack Manifest (SCH/JSON)<br/>Deterministic inventory + hashes (if used)"]
EVID --> INV["Evidence Inventory (LST/MD)<br/>Human-readable, fully linked"]
EVID --> SUM["Evidence Summary (RPT/MD)<br/>What was done, what proves it"]

%% --- CI Enforcement ---
MAN --> CI["CI Gates (PR level)<br/>Naming • metadata • schema validation • link checks • trace checks"]
INV --> CI
SUM --> CI

CI -->|Fail| FIX["Fix issues (iterate)<br/>Update artifacts + links"]
FIX --> EVID

CI -->|Pass| NKU["NKU Gate (MONITORING)<br/>Any CRITICAL NKU OPEN blocks closure"]

NKU -->|Blocked| MIT["Mitigation plan + owner + due date<br/>Open actions, update NKU tracker"]
MIT --> WORK

NKU -->|Clear| DEC["Decision Record (DECISIONS/)<br/>Decision statement + rationale + approvals"]

%% --- Approvals ---
DEC --> APPR{"Approvals obtained?<br/>CERT + CM mandatory"}
APPR -->|No| REWORK["Rework decision/evidence<br/>Address reviewer comments"]
REWORK --> WORK
APPR -->|Yes| BASE["Baseline & Release Update (CM)<br/>Changelog • tags • release snapshot"]

%% --- TEKNIA Sharing Rule ---
BASE --> TEK{"TEKNIA Sharing Rule<br/>EVIDENCE_FIRST satisfied?"}
TEK -->|No| HOLD(["HOLD: Internal only<br/>Missing reproducible audit path"])
TEK -->|Yes| EXPORT["Release / Export Pack (if applicable)<br/>Signed manifest • audit query path"]

%% --- Audit & Continuous Improvement ---
EXPORT --> AUDIT["Audit Query Execution (ATA 93)<br/>IDs → Schema → Trace → Evidence → Release"]
AUDIT --> CI2["Post-release CI/Monitoring<br/>Metrics • drift • nonconformities"]
CI2 --> END(["Closed: K01 work accepted<br/>Baseline updated • evidence traceable"])

%% --- Cross-ATA Anchors ---
SCOPE --> ATA91["ATA 91: Schemas/SSOT governance"]
SCOPE --> ATA93["ATA 93: Traceability graph + audit queries"]
SCOPE --> ATA98["ATA 98: Signed packs/exports"]
SCOPE --> ATA109["ATA 109: VV evidence packs"]

ATA91 --> MAN
ATA93 --> AUDIT
ATA98 --> EXPORT
ATA109 --> EVID
````

## Notes (reviewer guidance)

* This file is a **DIA** artifact stored as Markdown for **native GitHub rendering**.
* If you later produce a Draw.io source, keep it adjacent and cross-link both:

  * `..._k01-compliance-workflow_I01-R01.drawio` (editable source)
  * `..._k01-compliance-workflow_I01-R01.svg` (rendered export)
  * keep this `.md` as the **portable narrative + mermaid** reference.



