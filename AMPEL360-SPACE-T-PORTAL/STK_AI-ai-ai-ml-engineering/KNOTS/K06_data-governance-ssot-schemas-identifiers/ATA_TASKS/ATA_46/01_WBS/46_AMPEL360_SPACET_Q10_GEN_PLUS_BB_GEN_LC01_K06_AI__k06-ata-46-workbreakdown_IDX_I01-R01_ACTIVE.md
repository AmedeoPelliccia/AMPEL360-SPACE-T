---
title: "K06 ATA 46 Work Breakdown Structure"
type: IDX
project: AMPEL360
program: SPACET
variant: PLUS
status: ACTIVE
knot_id: K06
ata: "46"
lc_or_subbucket: "LC01"
description: "Work Breakdown Structure for K06 (Data Governance / SSOT / Schemas / Identifiers) for ATA 46 (Information Systems / Data Distribution / Data Services)"
---

# K06 ATA 46 — Work Breakdown Structure (WBS)

## Overview

This index provides the Work Breakdown Structure for closing **K06** (Data Governance / SSOT / Schemas / Identifiers) for **ATA 46** (Information Systems / Data Distribution / Data Services).

**Purpose:** Converts uncertainty into executable work packages (tasks, owners, inputs/outputs).

**Closes:** "We don't know what to do next / who owns it."

**Done when:** T001–T006 exist with owners, acceptance criteria, and artifact links.

---

## 1) Task Summary

| Task ID | Title | Owner | Status | Artifact Link |
| :--- | :--- | :--- | :--- | :--- |
| T001 | SSOT Source & Ownership | AI + DATA | Open | [T001 Details](46_AMPEL360_SPACET_Q10_GEN_PLUS_PR_GEN_LC06_K06-T001_AI__k06-t001-ssot-source-ownership_ACT_I01-R01_ACTIVE.md) |
| T002 | Identifier Grammar | AI + DATA | Open | [T002 Details](46_AMPEL360_SPACET_Q10_GEN_PLUS_PR_GEN_LC06_K06-T002_AI__k06-t002-identifier-grammar_ACT_I01-R01_ACTIVE.md) |
| T003 | Schema Definition | AI + SE | Open | [T003 Details](46_AMPEL360_SPACET_Q10_GEN_PLUS_PR_GEN_LC06_K06-T003_AI__k06-t003-schema-definition_ACT_I01-R01_ACTIVE.md) |
| T004 | Export Publication | AI + DATA | Open | [T004 Details](46_AMPEL360_SPACET_Q10_GEN_PLUS_PR_GEN_LC06_K06-T004_AI__k06-t004-export-publication_ACT_I01-R01_ACTIVE.md) |
| T005 | CI Validation Gates | AI + CM | Open | [T005 Details](46_AMPEL360_SPACET_Q10_GEN_PLUS_PR_GEN_LC06_K06-T005_AI__k06-t005-ci-validation-gates_ACT_I01-R01_ACTIVE.md) |
| T006 | Baseline Service Contract Set | AI + CERT | Open | [T006 Details](46_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_GEN_LC06_K06-T006_AI__k06-t006-baseline-service-contract-set_ACT_I01-R01_ACTIVE.md) |

---

## 2) RACI Matrix

See: [RACI Matrix (CSV)](46_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_LC06_K06_AI__k06-ata-46-raci_MAT_I01-R01_ACTIVE.csv)

### RACI Summary

| Task | AI | DATA | CM | SE | CERT | OPS | V&V |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| T001 (SSOT) | R | A | C | C | I | I | I |
| T002 (IDs) | R | A | C | C | I | I | I |
| T003 (Schema) | R | C | C | A | I | C | I |
| T004 (Export) | R | A | C | C | I | C | I |
| T005 (CI Gates) | R | C | A | C | I | I | I |
| T006 (Baseline) | R | C | C | C | A | C | R |

**Legend:**
- **R** = Responsible (does the work)
- **A** = Accountable (approves/signs-off)
- **C** = Consulted (provides input)
- **I** = Informed (notified of outcomes)

---

## 3) Dependencies & Sequencing

```
T001 (SSOT) --+--> T002 (IDs) --> T003 (Schema) --+--> T004 (Export) --> T006 (Baseline)
              |                                    |
              +------------------------------------+--> T005 (CI Gates)
```

### Dependency Table

| Task | Depends On | Enables |
| :--- | :--- | :--- |
| T001 | None | T002, T003, T004, T005 |
| T002 | T001 | T003, T004 |
| T003 | T001, T002 | T004, T005 |
| T004 | T001, T002, T003 | T006 |
| T005 | T001, T003 | T006 |
| T006 | T004, T005 | None (closure artifact) |

---

## 4) Acceptance Criteria (WBS Closure)

This WBS index is **closed** when:

- [ ] All T001–T006 task files exist and are linked
- [ ] Each task has an assigned owner (not "TBD")
- [ ] Each task has explicit acceptance criteria
- [ ] RACI matrix is approved by CM WG
- [ ] Dependencies are documented and accepted

---

## 5) Cross-Reference Links

### Parent Index
- [K06 ATA 46 Tasklist](../46_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_LC01_K06_AI__k06-ata-46-tasklist_IDX_I01-R01_ACTIVE.md)

### Related K06 WBS (Other ATAs)
- [ATA 45 WBS](../../ATA_45/)
- [ATA 91 WBS](../../ATA_91/)
- [ATA 93 WBS](../../ATA_93/)
- [ATA 99 WBS](../../ATA_99/)
- [ATA 101 WBS](../../ATA_101/)

---

## Maintenance

**Last Updated:** 2025-12-17  
**Update Frequency:** Per task status change  
**Maintained By:** AI + DATA Teams

---

## Notes

- Task IDs (T001–T006) are stable and permanent.
- New tasks (T007+) require CM WG approval and WBS update.
- Evidence of task completion must be linked before status changes to "Closed".
