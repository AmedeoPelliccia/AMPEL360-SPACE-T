---
title: "K01 ATA 00 Evidence Pack Summary"
type: RPT
project: "AMPEL360"
program: "SPACET"
variant: "PLUS"
status: "TEMPLATE"
knot_id: "K01"
ata_code: "00"
lc_or_subbucket: "LC01"
generated: "2025-12-15"
---

# K01 ATA 00 Evidence Pack Summary

## 1. Purpose
This report provides a single, review-friendly summary of the **K01 Certification Authority Basis** evidence pack for **ATA 00 (General / Program Governance)**. It is intended to support **CERT and CM review**, audit readiness, and controlled release of program-level certification artifacts.

## 2. Pack Scope
- **Knot:** K01 — certification-authority-basis  
- **ATA:** 00 — General / Program Governance  
- **Project / Program / Variant:** AMPEL360 / SPACET / PLUS  
- **Lifecycle:** LC01 (Lifecycle artifacts; BUCKET=00)

## 3. Status Snapshot (to be completed)
| Item | Status | Owner | Last Update | Notes |
|---|---|---|---|---|
| Certification basis identified | TBD | CERT | TBD | Regulations + standards identified |
| Authority engagement plan | TBD | CERT | TBD | Schedule + comms protocol |
| Compliance mapping (program level) | TBD | CERT/SE | TBD | Verification methods defined |
| Evidence plan | TBD | CERT | TBD | Evidence pack composition agreed |
| CM processes operational | TBD | CM | TBD | Change control + baselines |

## 4. Evidence Inventory (links)
Populate the table with **repo-relative links**. Use the manifest as the SSOT for “what must exist”.

| Artifact Role | Expected File | Status | Link | Review Comment |
|---|---|---:|---|---|
| Manifest (schema/contract) | Evidence pack manifest schema | TBD | `00_00_SCH_LC01_AMPEL360_SPACET_PLUS_k01-ata-00-evidence-pack-manifest_v01.json` | _TBD_ |
| Acceptance criteria | ATA 00 acceptance criteria | TBD | `00_00_REQ_LC01_AMPEL360_SPACET_PLUS_k01-ata-00-acceptance-criteria_v01.md` | _TBD_ |
| Compliance matrix | Program compliance matrix | TBD | `00_00_TAB_LC01_AMPEL360_SPACET_PLUS_k01-ata-00-compliance-matrix_v01.csv` | _TBD_ |
| Standards list | Applicable standards list | TBD | `00_00_LST_LC01_AMPEL360_SPACET_PLUS_k01-ata-00-applicable-standards_v01.md` | _TBD_ |
| Authority engagement plan | Authority engagement | TBD | `00_00_PLAN_LC01_AMPEL360_SPACET_PLUS_k01-ata-00-authority-engagement_v01.md` | _TBD_ |
| Config mgmt standard | CM rules for certification artifacts | TBD | `00_00_STD_LC01_AMPEL360_SPACET_PLUS_k01-ata-00-config-management_v01.md` | _TBD_ |
| Traceability links | ATA linkage proof | TBD | `00_00_TRC_LC01_AMPEL360_SPACET_PLUS_k01-ata-00-ata-traceability_v01.md` | _TBD_ |

## 5. Cross-ATA Linkage (K01 propagation)
List the ATA tasklists whose K01 closure depends on ATA 00 governance outputs.

| Dependent ATA | Why it depends on ATA 00 | Link |
|---|---|---|
| ATA 91 | Schema governance + identifier policy | _TBD_ |
| ATA 93 | Evidence ledger + audit query contract | _TBD_ |
| ATA 99 | Master registers policy | _TBD_ |
| ATA 109 | VV evidence packs linkage | _TBD_ |

## 6. Review & Approval
### 6.1 Required reviewers (minimum)
- CERT (Owner)
- CM (Approval authority for baselines and governance artifacts)
- QA (process/audit readiness), if applicable

### 6.2 Review record (populate)
| Reviewer | Organization | Date | Outcome | Notes |
|---|---|---|---|---|
| _TBD_ | CERT | _TBD_ | _TBD_ | _TBD_ |
| _TBD_ | CM | _TBD_ | _TBD_ | _TBD_ |

## 7. NKU and TEKNIA Control (Monitoring)
### 7.1 NKU tracker
- NKU tracking CSV (ATA 00):  
  `../MONITORING/00_00_TAB_LC01_AMPEL360_SPACET_PLUS_k01-ata-00-nku-tracking_v01.csv`

### 7.2 NKU gating rules (declare for this pack)
- **Release block if:** any **OPEN** NKU of category **Authority / Compliance / Evidence-Chain** remains unresolved.
- **Release block if:** any NKU is tagged **CRITICAL** (or equivalent severity) and not closed with evidence.
- **Progress metric:** % NKU closed per week (rolling 4-week window), reported per PR and per release.

### 7.3 TEKNIA sharing rule (evidence-first)
- **Share policy:** EVIDENCE_FIRST  
- External sharing is allowed only when:
  1) required artifacts exist and are linked in this report,  
  2) manifest completeness is met, and  
  3) CM-approved snapshot (signed/released) is produced.

## 8. Closure Statement (when complete)
When all referenced artifacts exist, are reviewed, and approvals recorded:

- [ ] Pack complete per manifest
- [ ] All required reviews completed
- [ ] NKU gating satisfied
- [ ] CM sign-off recorded

**Closure decision:** _TBD_  
**Date:** _TBD_  
**Signed by (CERT):** _TBD_  
**Approved by (CM):** _TBD_
