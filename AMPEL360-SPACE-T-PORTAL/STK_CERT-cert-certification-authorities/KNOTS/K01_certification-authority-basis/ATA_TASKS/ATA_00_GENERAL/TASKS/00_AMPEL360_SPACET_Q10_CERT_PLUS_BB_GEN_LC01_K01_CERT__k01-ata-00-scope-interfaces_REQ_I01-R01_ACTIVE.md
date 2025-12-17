---
title: "K01 ATA 00 Scope & Interfaces"
type: REQ
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
stakeholders: ["PMO", "SE", "SAF", "DATA", "CY", "TEST"]
last_updated: "2025-12-15"
---

# K01 ATA 00 Scope & Interfaces

## 1. Purpose
Define and control the **certification scope** and the **interfaces** for **ATA 00 (General Program / Program Governance)** under **K01 Authority Model & Certification Basis**.

This artifact exists to prevent scope drift, clarify ownership (AoR), and establish cross-ATA dependency handling for certification-basis activities.

---

## 2. Scope

### 2.1 In scope (ATA 00 under K01)
- **Authority model governance** (decision rights, approval chain, escalation, publication rules).
- **Certification basis strategy** at program level (how compliance is structured across ATAs and lifecycle gates).
- **Compliance governance**: compliance matrix ownership, MoC/MoE conventions, submission packaging rules.
- **Configuration & change control** for certification artifacts:
  - baseline IDs and release snapshot rules,
  - change request workflow, impact assessment and approvals,
  - audit readiness criteria and retention policy.
- **Portal governance alignment**:
  - effectivity labels (e.g., `SPACET-INT`, `SPACET-AUTH`),
  - RBAC rules for access grants and reviewer enforcement.

### 2.2 Out of scope (owned elsewhere)
- Technical compliance implementation inside individual systems ATAs (e.g., ATA 22, 24, 27, 72).
- Cybersecurity architecture and key management details (unless referenced as a K01 dependency; see §4).
- Detailed schema/ontology design (ATA 91) and trace graph implementation (ATA 93) beyond governance requirements.

---

## 3. Interfaces

### 3.1 Cross-ATA interfaces (minimum set)
| Interface ID | With ATA | Interface topic | What ATA 00 provides | What the other ATA provides | Primary owner | Reviewers |
|---|---:|---|---|---|---|---|
| IF-00-91 | 91 | Schema/identifier governance | Policy, approval chain, publication rules | Schema versions, compatibility statements, validators | CM/DATA | CERT |
| IF-00-93 | 93 | Traceability + audit queries | Governance rules, minimum trace obligations | Trace graph, audit query outputs, evidence linkage | CM/SE | CERT/QA |
| IF-00-98 | 98 | Release packs / signed exports | Release acceptance criteria, baseline snapshot policy | Signed pack mechanics, manifests, storage, retrieval | CM | CY/CERT |
| IF-00-100 | 100 | Sim/Test governance | Governance rules for evidence quality gates | Test plan governance, tool qualification paths | CERT/TEST | CM |
| IF-00-109 | 109 | VV evidence packs | Evidence packaging rules, submission policy | Evidence pack contents, closure evidence | CERT | CM/QA |

> Populate additional ATAs as they become in-scope for K01 execution.

### 3.2 Cross-knot interfaces (minimum set)
| Interface ID | With Knot | Dependency type | Description | Impact on ATA 00 | Status |
|---|---|---|---|---|---|
| IF-K01-K06 | K06 | Governance dependency | ID/SSOT/schema rules must align with certification basis | Affects identifiers, registries, auditability | TEMPLATE |
| IF-K01-K13 | K13 | Security dependency | Key management and secure sharing conditions | Affects RBAC, signing, external sharing | TEMPLATE |
| IF-K01-K08 | K08 | Evidence/provenance dependency | DPP/provenance expectations for auditability | Affects evidence pack semantics | TEMPLATE |

---

## 4. Constraints & Assumptions (template)
- **Assumption A1:** Authority engagement cadence and submission routes are defined by CERT and accepted by CM.
- **Assumption A2:** Portal effectivity classes are stable (`SPACET-INT`, `SPACET-AUTH`, optional supplier view).
- **Constraint C1:** All K01 artifacts must be GitHub-native and reviewable (Markdown/CSV/JSON/YAML preferred).
- **Constraint C2:** RBAC must be enforceable with GitHub primitives (CODEOWNERS, branch protection, reviews).

---

## 5. Deliverables (outputs)
Populate with the minimum set expected from this scope definition:

- [ ] Scope statement approved (CM AoR, CERT review).
- [ ] Cross-ATA interface register completed and linked to affected ATA tasklists.
- [ ] Cross-knot dependency register completed and linked to knot overviews.
- [ ] Publication/effectivity and RBAC rules referenced (or linked) for K01/ATA00.

---

## 6. Template notes (how to use)
- Replace `TEMPLATE` items with concrete decisions, links, and owners as execution proceeds.
- Any change to **scope** must trigger a change-control entry and update K01 overview links.

