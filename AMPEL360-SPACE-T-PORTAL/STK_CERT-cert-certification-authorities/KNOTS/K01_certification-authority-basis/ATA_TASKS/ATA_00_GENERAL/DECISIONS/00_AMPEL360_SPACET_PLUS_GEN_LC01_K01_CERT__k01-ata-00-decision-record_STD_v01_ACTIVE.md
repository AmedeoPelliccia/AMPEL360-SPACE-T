---
title: "K01 ATA 00 Decision Record"
type: STD
project: "AMPEL360"
program: "SPACET"
variant: "PLUS"
status: "TEMPLATE"
knot_id: "K01"
ata_code: "00"
lc_or_subbucket: "LC01"
generated: "2025-12-15"
---

# K01 ATA 00 Decision Record

## 1. Purpose
This document is the controlled **decision log** for **K01 / ATA 00 (General / Program Governance)**.  
It records certification-basis and authority-facing decisions, including rationale, approvals, and mandatory links to evidence artifacts.

## 2. Quick Links (mandatory)
- Evidence summary (RPT): **[00_00_RPT_LC01_AMPEL360_SPACET_PLUS_k01-ata-00-evidence-pack-summary_v01.md](../EVIDENCE/00_AMPEL360_SPACET_PLUS_00_RPT_LC01_K01_CERT__k01-ata-00-evidence-pack-summary_v01.md)**
- Evidence inventory (LST): **[00_00_LST_LC01_AMPEL360_SPACET_PLUS_k01-ata-00-evidence-inventory_v01.md](../EVIDENCE/00_AMPEL360_SPACET_PLUS_00_LST_LC01_K01_CERT__k01-ata-00-evidence-inventory_v01.md)**
- Evidence pack manifest (SCH): **[00_00_SCH_LC01_AMPEL360_SPACET_PLUS_k01-ata-00-evidence-pack-manifest_v01.json](../EVIDENCE/00_AMPEL360_SPACET_PLUS_00_SCH_LC01_K01_CERT__k01-ata-00-evidence-pack-manifest_v01.json)**
- Acceptance criteria (REQ): **[00_00_REQ_LC01_AMPEL360_SPACET_PLUS_k01-ata-00-acceptance-criteria_v01.md](../EVIDENCE/00_AMPEL360_SPACET_PLUS_00_REQ_LC01_K01_CERT__k01-ata-00-acceptance-criteria_v01.md)**
- NKU tracking (TAB/CSV): **[00_00_TAB_LC01_AMPEL360_SPACET_PLUS_k01-ata-00-nku-tracking_v01.csv](../MONITORING/00_00_TAB_LC01_AMPEL360_SPACET_PLUS_k01-ata-00-nku-tracking_v01.csv)**

## 3. Decision Governance (how to use this record)
- Each decision is **atomic** and must include:
  - **Decision statement**
  - **Scope boundary**
  - **Rationale**
  - **Impact / affected ATAs**
  - **Evidence links** (GitHub-navigable)
  - **Approvals** (CERT + CM minimum)
- A decision may be marked **Provisional** only if it includes:
  - explicit expiry/next-review date, and
  - a linked NKU item explaining the remaining uncertainty.

## 4. Decision Register (populate)

| DEC_ID | Date | Title | Decision Statement | Scope (In/Out) | Affected ATAs | Evidence Links | Approvals | Status | Notes |
|---|---|---|---|---|---|---|---|---|---|
| DEC-00-001 | TBD | Certification Basis Set (Program-Level) | TBD | TBD | 00, … | **[Inventory](../EVIDENCE/00_AMPEL360_SPACET_PLUS_00_LST_LC01_K01_CERT__k01-ata-00-evidence-inventory_v01.md)** | CERT+CM | TBD | _TBD_ |
| DEC-00-002 | TBD | Authority Engagement Model | TBD | TBD | 00, … | **[Engagement Plan](../EVIDENCE/00_00_PLAN_LC01_AMPEL360_SPACET_PLUS_k01-ata-00-authority-engagement_v01.md)** | CERT+CM | TBD | _TBD_ |
| DEC-00-003 | TBD | Means of Compliance Framework | TBD | TBD | 00, … | **[Compliance Matrix](../EVIDENCE/00_00_TAB_LC01_AMPEL360_SPACET_PLUS_k01-ata-00-compliance-matrix_v01.csv)** | CERT+CM | TBD | _TBD_ |
| DEC-00-004 | TBD | Evidence Packaging & Audit Query Contract | TBD | TBD | 00, 93, 98, 109 | **[Manifest](../EVIDENCE/00_AMPEL360_SPACET_PLUS_00_SCH_LC01_K01_CERT__k01-ata-00-evidence-pack-manifest_v01.json)** | CERT+CM | TBD | _TBD_ |

## 5. Decision Detail Template (copy for each DEC_ID)

### 5.1 Decision Header
- **DEC_ID:** DEC-00-XXX  
- **Date:** YYYY-MM-DD  
- **Owner:** CERT (or designated)  
- **Approval authority:** CM (baseline/control) + CERT (regulatory)  
- **Status:** Draft / Proposed / Approved / Rejected / Superseded  
- **Supersedes:** (optional) DEC-00-XXX  
- **Next review date:** (optional)

### 5.2 Decision Statement
- **Decision:**  
  _Write the decision in one unambiguous sentence._

### 5.3 Scope Boundary
- **In-scope:**  
- **Out-of-scope:**

### 5.4 Rationale
- **Why this decision is needed now:**  
- **Alternatives considered:**  
- **Reason for selection:**

### 5.5 Impact Assessment
- **Affected ATAs:**  
- **Affected knots (if any):**  
- **Interfaces / downstream consequences:**  
- **Risk if wrong / delayed:**

### 5.6 Evidence (mandatory hyperlinks)
Provide links to the exact artifacts that support the decision.
- **Primary evidence:**  
  - **[Evidence inventory](../EVIDENCE/00_AMPEL360_SPACET_PLUS_00_LST_LC01_K01_CERT__k01-ata-00-evidence-inventory_v01.md)**
- **Supporting evidence:**  
  - **[Evidence summary](../EVIDENCE/00_AMPEL360_SPACET_PLUS_00_RPT_LC01_K01_CERT__k01-ata-00-evidence-pack-summary_v01.md)**  
  - **[Acceptance criteria](../EVIDENCE/00_AMPEL360_SPACET_PLUS_00_REQ_LC01_K01_CERT__k01-ata-00-acceptance-criteria_v01.md)**

### 5.7 NKU Linkage (if decision is provisional)
- **NKU reference:** **[NKU tracker](../MONITORING/00_00_TAB_LC01_AMPEL360_SPACET_PLUS_k01-ata-00-nku-tracking_v01.csv)**  
- **NKU item(s):** NKU-00-XXX  
- **Closure plan:** (tasks + expected evidence + due date)

### 5.8 Approvals (mandatory)
| Role | Name | Org | Date | Decision |
|---|---|---|---|---|
| CERT (Owner) | TBD | CERT | TBD | Approve/Reject |
| CM (Baseline Authority) | TBD | CM | TBD | Approve/Reject |
| QA (optional) | TBD | QA | TBD | Review |

## 6. Change Log (optional)
| Date | Change | Author | Notes |
|---|---|---|---|
| 2025-12-15 | Created template | TBD | Initial decision-record scaffold |
