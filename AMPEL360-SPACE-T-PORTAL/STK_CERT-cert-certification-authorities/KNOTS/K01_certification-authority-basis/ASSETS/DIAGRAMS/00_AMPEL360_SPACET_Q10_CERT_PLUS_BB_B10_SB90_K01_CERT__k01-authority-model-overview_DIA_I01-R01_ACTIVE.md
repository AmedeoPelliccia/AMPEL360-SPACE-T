---
knot_id: K01
type: DIA
format: mermaid
---

# K01 Authority Model Overview

```mermaid
flowchart TD

%% =========================
%% K01 Authority Model Overview (AMPEL360 / SPACET / PLUS)
%% =========================

A["AMPEL360-SPACE-T-PORTAL<br/>All-in-one digital environment<br/>for spacecraft activities follow-up & publications"]
A --> B["STK_CERT (AoR)<br/>Certification & Authorities"]
A --> C["STK_CM (AoR)<br/>Configuration Management"]
A --> D["STK_SE<br/>Systems Engineering"]
A --> E["STK_DATA<br/>Data Governance"]
A --> F["STK_CY<br/>Cybersecurity"]
A --> G["STK_TEST<br/>IVVQ / Testing"]
A --> H["STK_OPS<br/>Operations"]
A --> I["STK_SAF<br/>Safety"]
A --> J["STK_PMO<br/>Program Management Office"]

B --> K["KNOT K01<br/>certification-authority-basis<br/>PROGRAM=SPACET / VARIANT=PLUS"]

%% -------------------------
%% K01 structure
%% -------------------------
subgraph K01["K01 Directory Skeleton (canonical)"]
direction TB
K --> K_ASSETS["ASSETS/<br/>DIAGRAMS • TABLES • SCHEMAS • EXEMPLARS • LINKS"]
K --> K_ATA["ATA_TASKS/<br/>per affected ATA (ATA_XX_TITLE)"]
K --> K_LINKS["LINKS/<br/>public context • normative references"]
end

%% -------------------------
%% ASSETS detail
%% -------------------------
subgraph ASSETS["ASSETS (BUCKET=90 / SB90)"]
direction TB
K_ASSETS --> DGM["DIAGRAMS/<br/>Authority model • RACI • Compliance workflow"]
K_ASSETS --> TBL["TABLES/<br/>Authority matrix • RBAC role matrix • gates checklist"]
K_ASSETS --> SCH["SCHEMAS/<br/>Compliance object • Evidence pack manifest • Audit query contract"]
K_ASSETS --> EXM["EXEMPLARS/<br/>Authority pack example • baseline snapshot example"]
K_ASSETS --> LNK["LINKS/<br/>Normative references • public context"]
end

%% -------------------------
%% Per-ATA task skeleton
%% -------------------------
subgraph ATA00["ATA_00_GENERAL (example ATA task workspace)"]
direction TB
K_ATA --> ATA00_HOME["ATA_00_GENERAL/"]
ATA00_HOME --> ATA00_TASKS["TASKS/<br/>Scope & Interfaces • Acceptance Criteria"]
ATA00_HOME --> ATA00_EVID["EVIDENCE/<br/>Inventory (LST) • Manifest (SCH) • Summary (RPT)"]
ATA00_HOME --> ATA00_DEC["DECISIONS/<br/>Decision Record (STD)"]
ATA00_HOME --> ATA00_MON["MONITORING/<br/>NKU tracking • Action register"]
ATA00_HOME --> ATA00_LNK["LINKS/<br/>Related PRs • Related issues"]
end

%% -------------------------
%% Cross-ATA propagation
%% -------------------------
K_ATA --> XATA["Cross-ATA propagation (minimum set)"]
XATA --> ATA91["ATA 91<br/>Schemas / Ontologies / SSOT"]
XATA --> ATA93["ATA 93<br/>Traceability graph & evidence ledgers"]
XATA --> ATA98["ATA 98<br/>Signed release packs / manifests / exports"]
XATA --> ATA109["ATA 109<br/>VV evidence packs linked to traceability"]

%% -------------------------
%% Workflow (decision → evidence → baseline)
%% -------------------------
subgraph WF["K01 Workflow (decision + evidence + baseline)"]
direction LR
S1["T001: Certification Basis Definition<br/>(scope, authorities, regulations, special conditions)"]
S2["T002: Compliance Mapping<br/>(MoC, verification, trace links)"]
S3["Evidence Pack Build<br/>(manifest + inventory + summary)"]
S4["Decision Record<br/>(approval + rationale + impacts)"]
S5["Baseline / Release Snapshot<br/>(CM-controlled + signed if required)"]
S1 --> S2 --> S3 --> S4 --> S5
end

ATA00_TASKS --> S1
ATA00_EVID --> S3
ATA00_DEC --> S4
C --> S5

%% -------------------------
%% Controls (CI + RBAC + NKU + TEKNIA)
%% -------------------------
subgraph CTRL["Controls & Monitoring"]
direction TB
CI["CI Gates (repo-wide)<br/>nomenclature • metadata • schema validation • link checks"]
RBAC["RBAC & Effectivity (portal access)<br/>STK-level grants + LC/SB constraints"]
NKU["NKU Monitoring<br/>open/closed • severity • aging • gating to closure"]
TEK["TEKNIA sharing rules<br/>EVIDENCE_FIRST • reproducible audit path"]
end

CI --> S3
RBAC --> ATA00_HOME
NKU --> S4
TEK --> S5

%% -------------------------
%% Stakeholder decision rights (high-level)
%% -------------------------
subgraph RACI["Decision Rights (AoR + cross-dependencies)"]
direction LR
CERT["CERT (AoR)<br/>regulatory strategy + acceptance"]
CM["CM (AoR)<br/>baseline + change control + releases"]
SE["SE<br/>system scope + interfaces"]
QA["QA<br/>process audit + readiness"]
DATA2["DATA<br/>schemas + SSOT + evidence structure"]
CY2["CY<br/>security + signing pre-reqs"]
CERT --- CM --- SE --- QA --- DATA2 --- CY2
end

CERT --> S4
CM --> S5
SE --> S2
QA --> CI
DATA2 --> ATA91
CY2 --> ATA98

```

**Description**: Overview of the certification authority model showing relationships between stakeholders and the certification authority.
