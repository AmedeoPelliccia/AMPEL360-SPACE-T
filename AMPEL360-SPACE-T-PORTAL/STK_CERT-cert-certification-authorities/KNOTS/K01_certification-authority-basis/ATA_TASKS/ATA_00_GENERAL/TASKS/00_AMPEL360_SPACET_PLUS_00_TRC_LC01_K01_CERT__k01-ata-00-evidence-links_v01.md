---
title: "K01 ATA 00 Evidence Links"
type: TRC
project: "AMPEL360"
program: "SPACET"
variant: "PLUS"
status: "TEMPLATE"
knot_id: "K01"
ata: "00"
lc_or_subbucket: "LC01"
effectivity: ["SPACET-INT"]
aor: "CM"
mandatory_reviewers: ["CERT"]
stakeholders: ["PMO", "SE", "SAF", "DATA", "CY", "TEST", "QA"]
last_updated: "2025-12-15"
---

# K01 ATA 00 Evidence Links

## 1. Purpose
Provide the **traceability register** that links **K01 / ATA 00** requirements and acceptance criteria to:
- evidence artifacts (documents, tables, schemas, manifests),
- decisions/approvals,
- trace graph anchors (if used),
- signed release packs (if applicable).

This document is the **single navigable map** used during reviews and audits.

---

## 2. Source Requirements / Criteria
Primary source for acceptance criteria:
- `../REQ/00_00_REQ_LC01_AMPEL360_SPACET_PLUS_k01-ata-00-acceptance-criteria_v01.md` (or update path if stored elsewhere)

---

## 3. Traceability Matrix (Template)

| Item ID (AC/REQ) | Item statement / intent | Evidence artifact (primary) | Supporting evidence | Review / approval record | Trace graph link (optional) | Release pack link (optional) | Status |
|---|---|---|---|---|---|---|---|
| AC-00-001 | Applicable regulations identified and documented | `../EVIDENCE/00_00_LST_LC01_AMPEL360_SPACET_PLUS_k01-ata-00-applicable-standards_v01.md` | `../ASSETS/LINKS/...` | `../DECISIONS/...` | `../TRACE/...` | `../RELEASE/...` | TEMPLATE |
| AC-00-002 | Certification strategy approved | `../EVIDENCE/00_00_PLAN_LC01_AMPEL360_SPACET_PLUS_k01-ata-00-certification-strategy_v01.md` | `../EVIDENCE/...` | `../DECISIONS/...` | `../TRACE/...` | `../RELEASE/...` | TEMPLATE |
| AC-00-003 | Special conditions + MoC defined | `../EVIDENCE/00_00_LST_LC01_AMPEL360_SPACET_PLUS_k01-ata-00-special-conditions_v01.md` | `../EVIDENCE/...` | `../DECISIONS/...` | `../TRACE/...` | `../RELEASE/...` | TEMPLATE |
| AC-00-004 | Authority engagement plan established | `../EVIDENCE/00_00_PLAN_LC01_AMPEL360_SPACET_PLUS_k01-ata-00-authority-engagement_v01.md` | `../EVIDENCE/...` | `../DECISIONS/...` | `../TRACE/...` | `../RELEASE/...` | TEMPLATE |
| AC-00-005 | Certification plan outline approved | `../EVIDENCE/00_00_PLAN_LC01_AMPEL360_SPACET_PLUS_k01-ata-00-certification-plan_v01.md` | `../EVIDENCE/...` | `../DECISIONS/...` | `../TRACE/...` | `../RELEASE/...` | TEMPLATE |
| AC-00-006 | 100% mapping to verification methods | `../EVIDENCE/00_00_TRC_LC01_AMPEL360_SPACET_PLUS_k01-ata-00-requirements-mapping_v01.md` | `../EVIDENCE/...` | `../DECISIONS/...` | `../TRACE/...` | `../RELEASE/...` | TEMPLATE |
| AC-00-007 | Compliance matrix complete/approved | `../EVIDENCE/00_00_TAB_LC01_AMPEL360_SPACET_PLUS_k01-ata-00-compliance-matrix_v01.csv` | `../EVIDENCE/...` | `../DECISIONS/...` | `../TRACE/...` | `../RELEASE/...` | TEMPLATE |
| AC-00-008 | Evidence plan documented/submitted | `../EVIDENCE/00_00_PLAN_LC01_AMPEL360_SPACET_PLUS_k01-ata-00-evidence-plan_v01.md` | `../EVIDENCE/...` | `../DECISIONS/...` | `../TRACE/...` | `../RELEASE/...` | TEMPLATE |
| AC-00-009 | CM system established for cert artifacts | `../EVIDENCE/00_00_STD_LC01_AMPEL360_SPACET_PLUS_k01-ata-00-config-management_v01.md` | `../EVIDENCE/...` | `../DECISIONS/...` | `../TRACE/...` | `../RELEASE/...` | TEMPLATE |
| AC-00-010 | Cross-ATA traceability documented | `../EVIDENCE/00_00_TRC_LC01_AMPEL360_SPACET_PLUS_k01-ata-00-ata-traceability_v01.md` | `../EVIDENCE/...` | `../DECISIONS/...` | `../TRACE/...` | `../RELEASE/...` | TEMPLATE |
| AC-00-011 | Nomenclature standard applied | `../EVIDENCE/00_00_RPT_LC01_AMPEL360_SPACET_PLUS_k01-ata-00-nomenclature-audit_v01.md` | `../EVIDENCE/...` | `../DECISIONS/...` | `../TRACE/...` | `../RELEASE/...` | TEMPLATE |
| AC-00-012 | Change control operational | `../EVIDENCE/00_00_STD_LC01_AMPEL360_SPACET_PLUS_k01-ata-00-change-control_v01.md` | `../EVIDENCE/...` | `../DECISIONS/...` | `../TRACE/...` | `../RELEASE/...` | TEMPLATE |
| AC-00-013 | Roles/responsibilities defined | `../EVIDENCE/00_00_LST_LC01_AMPEL360_SPACET_PLUS_k01-ata-00-roles-responsibilities_v01.md` | `../EVIDENCE/...` | `../DECISIONS/...` | `../TRACE/...` | `../RELEASE/...` | TEMPLATE |
| AC-00-014 | Authority comms protocol established | `../EVIDENCE/00_00_STD_LC01_AMPEL360_SPACET_PLUS_k01-ata-00-authority-comms-protocol_v01.md` | `../EVIDENCE/...` | `../DECISIONS/...` | `../TRACE/...` | `../RELEASE/...` | TEMPLATE |

---

## 4. Audit Query Pointer (Required at closure)
At closure, link at least one reproducible path proving:
`K01 decision → ATA 00 criteria → evidence → (optional) trace graph → (optional) signed release pack`

- Audit query/report artifact: `../EVIDENCE/...`
- How-to-run / click-path notes: `../EVIDENCE/...`

---

## 5. TEKNIA Sharing Controls (Checkpoint)
Before setting effectivity to `SPACET-AUTH`, confirm:

- [ ] Every row has a **primary evidence artifact** committed and linked
- [ ] Review records are linked (CERT mandatory)
- [ ] RBAC is enforced (CODEOWNERS/required approvals) for K01 scope
- [ ] A reproducible audit query exists and is linked

