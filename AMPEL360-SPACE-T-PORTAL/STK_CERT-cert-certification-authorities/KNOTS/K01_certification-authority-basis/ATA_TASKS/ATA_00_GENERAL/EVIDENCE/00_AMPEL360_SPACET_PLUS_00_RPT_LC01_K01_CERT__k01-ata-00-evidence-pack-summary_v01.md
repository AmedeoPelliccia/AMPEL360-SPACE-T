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
This report summarizes the **K01 Certification Authority Basis** evidence pack for **ATA 00 (General / Program Governance)** and provides **mandatory GitHub-navigable hyperlinks** to all pack components.

## 2. Quick Links (mandatory)
- Evidence inventory (human index): **[00_00_LST_LC01_AMPEL360_SPACET_PLUS_k01-ata-00-evidence-inventory_v01.md](./00_AMPEL360_SPACET_PLUS_00_LST_LC01_K01_CERT__k01-ata-00-evidence-inventory_v01.md)**
- Evidence pack manifest (contract): **[00_00_SCH_LC01_AMPEL360_SPACET_PLUS_k01-ata-00-evidence-pack-manifest_v01.json](./00_AMPEL360_SPACET_PLUS_00_SCH_LC01_K01_CERT__k01-ata-00-evidence-pack-manifest_v01.json)**
- NKU tracking (monitoring): **[00_00_TAB_LC01_AMPEL360_SPACET_PLUS_k01-ata-00-nku-tracking_v01.csv](../MONITORING/00_00_TAB_LC01_AMPEL360_SPACET_PLUS_k01-ata-00-nku-tracking_v01.csv)**
- Action register (monitoring): **[00_00_TAB_LC01_AMPEL360_SPACET_PLUS_k01-ata-00-action-register_v01.csv](../MONITORING/00_00_TAB_LC01_AMPEL360_SPACET_PLUS_k01-ata-00-action-register_v01.csv)**

## 3. Pack Status Snapshot (populate)
| Area | Status | Owner | Notes |
|---|---|---|---|
| Certification basis definition | TBD | CERT | _TBD_ |
| Authority engagement | TBD | CERT | _TBD_ |
| Compliance mapping | TBD | CERT/SE | _TBD_ |
| Evidence packaging | TBD | CERT/CM | _TBD_ |
| Baseline + change control readiness | TBD | CM | _TBD_ |

## 4. Evidence Items (hyperlinked register)
> Rule: every row must contain a working link. If the file does not exist yet, keep the row but set **Status=TBD**.

| ID | Evidence Item | Status | Link | Reviewer Comment |
|---|---:|---:|---|---|
| EV-00-001 | Acceptance criteria | TBD | **[Open](./00_AMPEL360_SPACET_PLUS_00_REQ_LC01_K01_CERT__k01-ata-00-acceptance-criteria_v01.md)** | _TBD_ |
| EV-00-002 | Applicable standards list | TBD | **[Open](./00_00_LST_LC01_AMPEL360_SPACET_PLUS_k01-ata-00-applicable-standards_v01.md)** | _TBD_ |
| EV-00-003 | Special conditions list | TBD | **[Open](./00_00_LST_LC01_AMPEL360_SPACET_PLUS_k01-ata-00-special-conditions_v01.md)** | _TBD_ |
| EV-00-004 | Authority engagement plan | TBD | **[Open](./00_00_PLAN_LC01_AMPEL360_SPACET_PLUS_k01-ata-00-authority-engagement_v01.md)** | _TBD_ |
| EV-00-005 | Certification strategy | TBD | **[Open](./00_00_PLAN_LC01_AMPEL360_SPACET_PLUS_k01-ata-00-certification-strategy_v01.md)** | _TBD_ |
| EV-00-006 | Evidence plan | TBD | **[Open](./00_00_PLAN_LC01_AMPEL360_SPACET_PLUS_k01-ata-00-evidence-plan_v01.md)** | _TBD_ |
| EV-00-007 | Compliance matrix | TBD | **[Open](./00_00_TAB_LC01_AMPEL360_SPACET_PLUS_k01-ata-00-compliance-matrix_v01.csv)** | _TBD_ |
| EV-00-008 | Requirements mapping | TBD | **[Open](./00_00_TRC_LC01_AMPEL360_SPACET_PLUS_k01-ata-00-requirements-mapping_v01.md)** | _TBD_ |
| EV-00-009 | Cross-ATA traceability | TBD | **[Open](./00_00_TRC_LC01_AMPEL360_SPACET_PLUS_k01-ata-00-ata-traceability_v01.md)** | _TBD_ |
| EV-00-010 | Config management standard | TBD | **[Open](./00_00_STD_LC01_AMPEL360_SPACET_PLUS_k01-ata-00-config-management_v01.md)** | _TBD_ |
| EV-00-011 | Change control standard | TBD | **[Open](./00_00_STD_LC01_AMPEL360_SPACET_PLUS_k01-ata-00-change-control_v01.md)** | _TBD_ |
| EV-00-012 | Authority comms protocol | TBD | **[Open](./00_00_STD_LC01_AMPEL360_SPACET_PLUS_k01-ata-00-authority-comms-protocol_v01.md)** | _TBD_ |
| EV-00-013 | Nomenclature audit report | TBD | **[Open](./00_00_RPT_LC01_AMPEL360_SPACET_PLUS_k01-ata-00-nomenclature-audit_v01.md)** | _TBD_ |

## 5. Cross-ATA Dependencies (K01 propagation)
| Dependent ATA | Reason | Link |
|---|---|---|
| ATA 91 | Schema governance + identifier policy consumption | _TBD_ |
| ATA 93 | Evidence ledger + audit query contract | _TBD_ |
| ATA 99 | Master registers (golden records) alignment | _TBD_ |
| ATA 109 | VV evidence packs linkage to trace graph | _TBD_ |

## 6. NKU Control and Monitoring (NKU → closure gating)
- **NKU tracker:** **[Open](../MONITORING/00_00_TAB_LC01_AMPEL360_SPACET_PLUS_k01-ata-00-nku-tracking_v01.csv)**
- **Gating rule (release block):** any **CRITICAL** NKU **OPEN** blocks K01 ATA 00 closure.
- **Weekly reporting:** % NKU closed, newly opened, aging > 30 days, and top 5 blockers.

## 7. TEKNIA Sharing Rule (evidence-first)
- **Sharing policy:** `EVIDENCE_FIRST`
- External sharing allowed only when:
  1) this report links all mandatory items,  
  2) the manifest is complete,  
  3) CM approvals are recorded, and  
  4) a signed/snapshotted release pack exists (if applicable).

## 8. Review & Approval Record (populate)
| Reviewer | Role | Date | Outcome | Notes |
|---|---|---|---|---|
| TBD | CERT | TBD | TBD | _TBD_ |
| TBD | CM | TBD | TBD | _TBD_ |
| TBD | QA (optional) | TBD | TBD | _TBD_ |

## 9. Closure Statement (when complete)
- [ ] All evidence items present and linked
- [ ] Reviews complete (CERT + CM minimum)
- [ ] NKU gating satisfied
- [ ] Closure decision recorded and baselined

**Closure decision:** TBD  
**Closure date:** TBD  
**Signed by (CERT):** TBD  
**Approved by (CM):** TBD
