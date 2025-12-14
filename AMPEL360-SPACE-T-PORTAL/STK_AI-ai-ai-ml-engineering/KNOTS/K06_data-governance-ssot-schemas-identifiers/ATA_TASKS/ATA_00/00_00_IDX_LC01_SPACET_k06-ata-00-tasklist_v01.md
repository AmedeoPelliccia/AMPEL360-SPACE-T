---
title: "K06 ATA 00 Tasklist"
type: IDX
variant: SPACET
status: Draft
knot_id: K06
ata: "00"
lc_or_subbucket: "LC01"
bucket: "00"
description: "CM-owned tasklist for K06 governance spine: SSOT boundaries, identifier/nomenclature authority, schema governance references, CI enforcement, and auditability proof chain."
owner: "STK_CM — Configuration Management"
---

# K06 — data-governance-ssot-schemas-identifiers
## ATA 00 — Tasklist (OWNER: STK_CM)

This tasklist is the **authoritative execution lane** for K06 items that are **program-governance** in nature.
ATA 00 is managed by **CM**. Other stakeholders contribute, but **CM owns decisions and baselines**.

---

## Links (GitHub-navigable)

- Knot overview (within STK_CM):  
  [K06 overview](../../00_00_IDX_LC01_SPACET_k06-data-governance-ssot-schemas-identifiers_v01.md)  
  _Comment:_ Canonical K06 scope, impacted ATAs, closure criteria, and shared definitions.

- Portal index:  
  [AMPEL360-SPACE-T-PORTAL index](../../../../00_00_IDX_LC01_SPACET_stakeholder-entrypoints_v01.md)  
  _Comment:_ Single portal navigation for all stakeholders.

- Stakeholder entrypoint (CM):  
  [STK_CM entrypoint](../../../00_00_IDX_LC01_SPACET_stakeholder-cm-entrypoint_v01.md)  
  _Comment:_ CM authority for ATA 00 governance, baselines, and enforcement.

- ATA 00 home (program governance, CM-owned):  
  [STK_CM/P-PROGRAM/ATA_00-GENERAL](../../../P-PROGRAM/ATA_00-GENERAL/)  
  _Comment:_ Canonical location for program structures: nomenclature, SSOT rules, registers, change control, baselines.

> Note: ATA homes for engineering domains may exist outside STK_CM, but **ATA 00 program governance** is anchored here.

---

## Related ATA tasklists (same Knot)

> These are cross-links to the same knot in other ATA partitions (where they exist).
> Use these to verify K06 closure end-to-end.

- [ATA 91 (Schemas)](../ATA_91/)  
  _Comment:_ Canonical schema registry, versioning, compatibility, and controlled publication.

- [ATA 93 (Traceability Graph)](../ATA_93/)  
  _Comment:_ Node/edge semantics, evidence link rules, and trace snapshots.

- [ATA 94 (DPP)](../ATA_94/)  
  _Comment:_ DPP export packs and provenance references that rely on K06 governance.

- [ATA 95 (SBOM/ModelBOM)](../ATA_95/)  
  _Comment:_ Supply chain identity and BOM export governance driven by K06 primitives.

- [ATA 98 (Signed Export Packs)](../ATA_98/)  
  _Comment:_ Signing/hashing verification requirements coupling to K13.

- [ATA 99 (Master Registers)](../ATA_99/)  
  _Comment:_ Namespace boundaries, dedup policy, drift monitoring, master inventory.

---

## 1) Uncertainty to Resolve (ATA-specific)

ATA 00 must define the **authoritative CM governance spine** for:

- **Identifier authority:** canonical identifier grammar, namespace boundaries, uniqueness rules.
- **SSOT boundaries:** which artifacts are authoritative vs derived, where they live, how they change.
- **Schema governance references:** the mandatory program-level referencing rules to ATA 91 (schemas) and ATA 93 (trace semantics).
- **Enforcement:** CI gates and review rules that prevent uncontrolled proliferation of IDs/schemas and broken trace links.
- **Auditability chain:** minimum proof that `IDs → Schema → Trace → Export (signed when required)` is reproducible.

### Decision required (CM-owned)
One CM-approved decision (with recorded minutes) establishing:
- Identifier grammar + namespace registry authority (in coordination with ATA 99).
- SSOT decision matrix and publication locations (paths).
- Mandatory references to schema governance (ATA 91) and trace governance (ATA 93).
- CI gates (lint/validation) and escalation path on failure.

---

## 2) Scope Boundary

### In-scope
- Program-level nomenclature and metadata rules (ATA 00).
- SSOT decision matrix (authoritative vs derived) and publication location rules.
- Cross-ATA governance references (how ATAs must reference ATA 91/93/99 registries).
- CI enforcement rules + reviewer workflow for governance-impacting changes.
- Minimum auditability proof chain definition and demonstration approach.

### Out-of-scope
- Subsystem-specific schema definitions (owned by ATA 91 + downstream ATAs).
- Implementation details beyond minimum viable enforcement (tracked as tooling tasks unless pulled into K06).
- Cryptographic key management design (owned by K13), except defining governance requirements and interfaces.

---

## 3) Owners & Stakeholders

### Primary owner
- **STK_CM — Configuration Management** (authority, decision owner, baseline owner)

### Required contributors (inputs)
- **STK_DATA — Data Governance** (stewardship, SSOT boundaries, registry requirements)
- **STK_AI — AI/ML Engineering** (automation/validation, TEKNIA/NKU instrumentation)
- **STK_SE — Systems Engineering** (ICD expectations, interface-driven schema consumption)
- **STK_CERT — Certification & Authorities** (evidence expectations if compliance impacts)
- **STK_CY — Cybersecurity** (K13 coupling for signing/key controls)
- **STK_TEST — IVVQ/Testing** (evidence node adoption for 100+)

### Approvers
- **CM WG** (final approval, baseline release)
- **CERT** (approval required only if compliance/evidence format is impacted)

---

## 4) Interfaces / Affected Areas

### Impacted ATAs (dependency view)
- Direct governance dependencies:
  - **ATA 99** (namespaces, dedup, master inventory)
  - **ATA 91** (schemas + versioning)
  - **ATA 93** (trace semantics + evidence links)
- Output consumers:
  - **ATA 94/95/98** (DPP/BOM/signed packs)
  - **ATA 101/107/109** (sim/test evidence nodes consuming IDs/schemas and emitting trace)

### Authoritative targets (SSOT pointers)
> ATA 00 declares “where truth lives” without duplicating the truth.

- CM governance home: `STK_CM/P-PROGRAM/ATA_00-GENERAL/`
- Master registers/dedup: `.../ATA_99/...`
- Schemas governance: `.../ATA_91/...`
- Trace semantics: `.../ATA_93/...`
- DPP packs: `.../ATA_94/...`
- SBOM/ModelBOM: `.../ATA_95/...`
- Signed packs: `.../ATA_98/...`

---

## 5) Closure Criteria

This tasklist is **closed only if** all conditions are true:

1. **Identifier standard** approved by CM WG and published under ATA 00 governance home.
2. **SSOT decision matrix** approved by CM WG and published (authoritative vs derived + ownership).
3. **Schema governance reference policy** published: ATA 00 mandates how to reference ATA 91 schemas and versioning.
4. **CI enforcement** exists and demonstrably blocks:
   - invalid nomenclature / namespace violations,
   - unregistered schema IDs,
   - broken trace links / missing evidence pointers,
   - unauthorized governance-impacting changes.
5. **Auditability proof chain** documented and demonstrated for at least one reference flow:
   `ID registry entry → schema ID → trace snapshot link → export pack reference (signed when required)`.
6. **Decision record** exists (minutes + approvals log) and baseline references are updated.

---

## 6) Tasks (minimum set)

### 6.1 Governance and SSOT definition
- [ ] **T1 (CM-owned)** Define canonical identifier grammar and namespace boundaries (coordinate with ATA 99).
  - _Deliverable:_ `00_00_STD_LC01_SPACET_identifier-grammar_v01.md` (location: ATA 00 home)

- [ ] **T2 (CM-owned)** Define SSOT decision matrix (authoritative vs derived artifacts; ownership + location).
  - _Deliverable:_ `00_00_STD_LC01_SPACET_ssot-decision-matrix_v01.md` (location: ATA 00 home)

- [ ] **T3 (CM-owned)** Publish “governance reference policy”: how ATAs must reference schemas (ATA 91) and trace (ATA 93).
  - _Deliverable:_ `00_00_STD_LC01_SPACET_governance-reference-policy_v01.md` (location: ATA 00 home)

### 6.2 Enforcement (CI + reviews)
- [ ] **T4 (Tooling with CM authority)** Confirm CI gates for:
  - nomenclature + namespace checks,
  - schema registration checks,
  - trace/evidence link integrity checks,
  - approvals required for governance-impacting diffs.
  - _Deliverable:_ `00_00_IDX_LC01_SPACET_ci-governance-gates_v01.md` + CI workflow updates (linked)

- [ ] **T5 (CM-owned)** Define the minimal audit query path (how an auditor reproduces the chain).
  - _Deliverable:_ `00_00_RPT_LC01_SPACET_auditability-proof-path_v01.md`

### 6.3 Evidence + baseline freeze
- [ ] **T6 (CM-owned)** Produce minimal evidence pack showing:
  `IDs → Schema → Trace → Export (signed when required)`
  - _Deliverable:_ Evidence pack IDX + link register under K06/ATA00 evidence folder

- [ ] **T7 (CM-owned)** Record decision minutes, approvals, and baseline update entry.
  - _Deliverable:_ minutes + approvals log + changelog/baseline record

---

## 7) Outputs / Artifacts (expected)

- ATA 00 governance standards (TYPE=STD):
  - Identifier grammar + namespace boundaries
  - SSOT decision matrix
  - Governance reference policy (schemas/trace coupling)
- CI gates documentation (TYPE=IDX/STD) + workflow artifacts (linked)
- Auditability proof path (TYPE=RPT)
- Evidence pack index + evidence links register (TYPE=IDX/TRC)
- Decision minutes + approvals log (TYPE=MIN/LOG)

---

## 8) Dependencies / Risks

### Dependencies
- **ATA 99** (namespace registry + dedup enforcement)
- **ATA 91** (schema registry + versioning)
- **ATA 93** (trace semantics + evidence links)
- **K13** (signing/key management) for any “signed export pack” requirement (ATA 98 coupling)

### Risks (principal “uncertainty knots”)
- **Shadow registries**: parallel ID/schema lists outside the master inventory.
- **Namespace collisions**: duplicate IDs across ATAs without enforcement.
- **Stale evidence links**: closure claimed but evidence has drifted or is unverifiable.
- **Governance bypass**: PRs merging governance-impacting changes without CM approvals.
- **Tooling drift**: validators and schemas diverge from normative standards if not baselined.

