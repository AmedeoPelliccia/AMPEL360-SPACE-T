---
title: "K06 ATA 94 — Partitioned Uncertainty Resolution Index"
type: IDX
variant: SPACET
status: Draft
knot_id: K06
ata: "94"
lc_or_subbucket: "LC01"
description: "GitHub-navigable hub for closing K06 (SSOT/Schemas/Identifiers) for ATA 94 (Digital Product Passport & Provenance Exports) with NKU control and TEKNIA sharing rules."
---

# K06 — Data Governance (SSOT / Schemas / Identifiers)
## ATA 94 — Partitioned Uncertainty Resolution Index (IDX)

This file is the **single navigation hub** for all artifacts required to close **K06** for **ATA 94** (your domain for **Digital Product Passport (DPP) and provenance exports**).  
NKU progress is credited only when each partition is closed with **evidence + approval**.

> ATA 94 is the “external-facing consequence” of K06: if SSOT/schema/identifier governance is weak, DPP exports become non-auditable and non-reproducible.

---

## 1) Global Navigation (GitHub-navigable)

- Knot overview: [K06 overview](../../00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_LC01_K06_CM__k06-data-governance-ssot-schemas-identifiers_I01-R01.md)  
  _Comment:_ Canonical K06 scope, impacted ATAs, closure criteria, and shared definitions.

- Portal index: [AMPEL360-SPACE-T-PORTAL index](../../../../../00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_LC01_K04_CM__stakeholder-entrypoints_I01-R01.md)  
  _Comment:_ Global entry point; use it to navigate stakeholders and the knot portfolio.

- Stakeholder entrypoint (AI): [STK_AI entrypoint](../../../../00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_LC01_K04_AI__stakeholder-ai-entrypoint_I01-R01.md)  
  _Comment:_ AI/ML execution lane; automation hooks and governance helpers.

- ATA 94 home (DPP): [AMPEL360_SPACE-T/N-NEURAL_NETWORKS/ATA 94](../../../../../../AMPEL360_SPACE-T/N-NEURAL_NETWORKS/ATA_94-DPP/)  
  _Comment:_ Intended authoritative location for ATA 94 DPP outputs. If your folder name differs, update only this link target.

---

## 2) ATA 94 K06 Focus (what uncertainty we are closing)

### Uncertainty to Resolve (ATA-specific)
K06 within ATA 94 is the absence of a single governed SSOT for:
- **DPP identity:** canonical IDs for passports, views, packages, and release states.
- **DPP schema:** stable schemas for DPP payloads (materials, configurations, evidence, sustainability, compliance, models).
- **Provenance & signatures:** deterministic hashing, signing, and provenance metadata (what was exported, from where, when, using which tools/versions).
- **Trace references:** unambiguous links to trace graph snapshots and evidence packs (ATA 93/90/98).
- **Publication lifecycle:** draft vs baseline release, redaction rules, and sharing classification.
- **Enforcement:** CI gates preventing uncontrolled DPP changes and ensuring export reproducibility.

### Primary consumers (typical)
- Configuration management, compliance and audit stakeholders, sustainability reporting, customer/authority evidence packs, internal release pipelines, toolchains consuming DPP packs.

---

## 3) Partitioned Uncertainty Resolution Pathway (P1–P8)

Each partition corresponds to a dedicated folder. **Do not credit closure** unless the partition’s “Done” definition is satisfied.

### P1 — Work Breakdown & Ownership (Execution Closure)
- Folder: [01_WBS/](01_WBS/)  
  _Comment:_ Converts uncertainty into executable work packages (tasks, owners, inputs/outputs).

- WBS index: [K06 ATA 94 Work Breakdown](01_WBS/94_00_IDX_LC01_AMPEL360_SPACET_PLUS_k06-ata-94-workbreakdown_I01-R01.md)  
  _Closes:_ “We don’t know what to do next / who owns it.”  
  _Done when:_ T001–T009 exist with owners, acceptance criteria, and artifact links.

- RACI (CSV): [RACI](01_WBS/94_00_MAT_LC06_AMPEL360_SPACET_PLUS_k06-ata-94-raci_I01-R01.csv)  
  _Closes:_ Responsibility ambiguity (execution vs approval).  
  _Done when:_ CM approval path is explicit and accepted.

**Task stubs (minimum set — expanded for DPP domain):**
- T001: [SSOT source & ownership](01_WBS/94_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t001-ssot-source-ownership_I01-R01.md)  
  _Comment:_ Declares authoritative sources for DPP content (registries, schemas, trace snapshots) and sets change control.

- T002: [DPP identifier grammar](01_WBS/94_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t002-dpp-identifier-grammar_I01-R01.md)  
  _Comment:_ Canonical IDs for DPP passports, views, export packs, and releases.

- T003: [DPP schema definition](01_WBS/94_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t003-dpp-schema-definition_I01-R01.md)  
  _Comment:_ Stabilizes DPP payload semantics (fields, required evidence pointers, compatibility rules).

- T004: [Provenance & signing rules](01_WBS/94_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t004-provenance-signing-rules_I01-R01.md)  
  _Comment:_ Defines hashing/signing, metadata requirements, and verification procedure.

- T005: [Export publication](01_WBS/94_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t005-export-publication_I01-R01.md)  
  _Comment:_ Deterministic generation of DPP packs (manifest + payload + trace snapshot pointers).

- T006: [CI validation gates](01_WBS/94_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t006-ci-validation-gates_I01-R01.md)  
  _Comment:_ Enforces DPP schema validity, provenance completeness, and trace link integrity.

- T007: [Redaction & classification policy](01_WBS/94_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t007-redaction-classification-policy_I01-R01.md)  
  _Comment:_ Controls what can be shared externally and how to redact sensitive fields.

- T008: [Baseline DPP view definition](01_WBS/94_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t008-baseline-dpp-view-definition_I01-R01.md)  
  _Comment:_ Defines which DPP views are mandatory for releases and what evidence is required.

- T009: [Verification procedure](01_WBS/94_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t009-dpp-verification-procedure_I01-R01.md)  
  _Comment:_ Defines how consumers verify authenticity, completeness, and trace links.

---

### P2 — IDs & Registry (Identity Closure)
- Folder: [02_IDS_REGISTRY/](02_IDS_REGISTRY/)  
  _Comment:_ Ensures every DPP view/export pack has a unique ID, owner, lifecycle state, and dedup policy.

- Standard (STD): [DPP identifier grammar](02_IDS_REGISTRY/94_00_STD_LC03_AMPEL360_SPACET_PLUS_dpp-identifier-grammar_I01-R01.md)  
  _Done when:_ Grammar is approved and referenced by export tooling + CI.

- Registry (TAB/CSV): [DPP registry](02_IDS_REGISTRY/94_00_TAB_LC03_AMPEL360_SPACET_PLUS_dpp-registry_I01-R01.csv)  
  _Done when:_ Registry is SSOT (no duplicates), with owners/status and required metadata.

- Registry (TAB/CSV): [DPP view registry](02_IDS_REGISTRY/94_00_TAB_LC03_AMPEL360_SPACET_PLUS_dpp-view-registry_I01-R01.csv)  
  _Done when:_ Views are enumerated with scope, required evidence, and release applicability.

- Change log (LOG): [Registry change log](02_IDS_REGISTRY/94_00_LOG_LC03_AMPEL360_SPACET_PLUS_registry-change-log_I01-R01.md)  
  _Done when:_ Every change references a decision (P7).

---

### P3 — Schema & Versioning (Semantic Closure)
- Folder: [03_SCHEMA/](03_SCHEMA/)  
  _Comment:_ Defines authoritative DPP schemas and compatibility rules.

- Schema (SCH/JSON): [DPP payload schema](03_SCHEMA/94_00_SCH_LC03_AMPEL360_SPACET_PLUS_dpp-payload-schema_I01-R01.json)  
  _Done when:_ Validates DPP payloads and is used by CI.

- Schema (SCH/JSON): [DPP manifest schema](03_SCHEMA/94_00_SCH_LC03_AMPEL360_SPACET_PLUS_dpp-manifest-schema_I01-R01.json)  
  _Done when:_ Validates manifest metadata (tool versions, hashes, trace pointers, classification).

- Standard (STD): [Schema versioning policy](03_SCHEMA/94_00_STD_LC03_AMPEL360_SPACET_PLUS_schema-versioning-policy_I01-R01.md)  
  _Done when:_ Compatibility/breaking-change rules exist and are enforced.

- Standard (STD): [Redaction rules](03_SCHEMA/94_00_STD_LC03_AMPEL360_SPACET_PLUS_redaction-rules_I01-R01.md)  
  _Done when:_ Redaction is standardized and verifiable.

---

### P4 — Exports (Consumable Data Closure)
- Folder: [04_EXPORTS/](04_EXPORTS/)  
  _Comment:_ Deterministic DPP export packs with manifests, payloads, and verifiable pointers.

- Baseline export (TAB/CSV): [Baseline DPP registry export](04_EXPORTS/94_00_TAB_LC04_AMPEL360_SPACET_PLUS_baseline-dpp-registry-export_I01-R01.csv)  
  _Done when:_ Export is reproducible and validated.

- Manifest (RPT): [Export manifest](04_EXPORTS/94_00_RPT_LC04_AMPEL360_SPACET_PLUS_export-manifest_I01-R01.md)  
  _Done when:_ Inputs/tools/versions are recorded; rebuild is deterministic.

- Diagram (DIA): [DPP pack structure map](04_EXPORTS/94_00_DIA_LC04_AMPEL360_SPACET_PLUS_dpp-pack-structure-map_I01-R01.md)  
  _Done when:_ Diagram references match schemas/registries and exported packs.

---

### P5 — CI Gates (Enforcement Closure)
- Folder: [05_CI_GATES/](05_CI_GATES/)  
  _Comment:_ Prevents uncontrolled DPP changes and enforces provenance and trace integrity.

- Requirements (STD): [CI validation requirements](05_CI_GATES/94_00_STD_LC05_AMPEL360_SPACET_PLUS_ci-validation-requirements_I01-R01.md)  
  _Done when:_ Rules map to checks; failures are actionable.

- Checklist (LOG): [CI checklist](05_CI_GATES/94_00_LOG_LC05_AMPEL360_SPACET_PLUS_ci-checklist_I01-R01.md)  
  _Done when:_ Checklist matches CI outputs and reviewer expectations.

- Sample run (RPT): [CI validation sample run](05_CI_GATES/94_00_RPT_LC05_AMPEL360_SPACET_PLUS_ci-validation-sample-run_I01-R01.md)  
  _Done when:_ Demonstrates pass/fail cases (missing provenance, invalid trace pointer, unregistered view).

---

### P6 — Evidence Pack (Proof Closure)
- Folder: [06_EVIDENCE/](06_EVIDENCE/)  
  _Comment:_ NKU credit requires reproducible evidence and stable links, including signed pack verification.

- Evidence pack index (IDX): [Evidence pack](06_EVIDENCE/94_00_IDX_LC06_AMPEL360_SPACET_PLUS_k06-ata-94-evidence-pack_I01-R01.md)  
  _Done when:_ All required evidence is linked and current.

- Evidence links (TRC/CSV): [Evidence links register](06_EVIDENCE/94_00_TRC_LC06_AMPEL360_SPACET_PLUS_k06-ata-94-evidence-links_I01-R01.csv)  
  _Done when:_ Each claim has evidence links and status (OK/STALE/MISSING).

- NKU ledger (TAB/CSV): [NKU ledger](06_EVIDENCE/94_00_TAB_LC06_AMPEL360_SPACET_PLUS_k06-ata-94-nku-ledger_I01-R01.csv)  
  _Done when:_ Partition scores are updated and backed by evidence + decision.

---

### P7 — Decisions & Approvals (Authority Closure)
- Folder: [07_DECISIONS/](07_DECISIONS/)  
  _Comment:_ Converts evidence into approved baseline outcomes for DPP governance.

- Decision minutes (MIN): [Decision minutes](07_DECISIONS/94_00_MIN_LC07_AMPEL360_SPACET_PLUS_k06-ata-94-decision-minutes_I01-R01.md)  
  _Done when:_ Decision, rationale, dissent/risks are recorded.

- Approvals log (LOG): [Approvals log](07_DECISIONS/94_00_LOG_LC07_AMPEL360_SPACET_PLUS_k06-ata-94-approvals_I01-R01.md)  
  _Done when:_ CM approval + DPP authority sign-offs are referenced.

---

### P8 — Traceability & Adoption (Impact Closure)
- Folder: [08_TRACEABILITY/](08_TRACEABILITY/)  
  _Comment:_ Ensures DPP consumers adopt the SSOT (schemas/registries/trace pointers) and can verify authenticity.

- Consumers (TRC/CSV): [Consumers list](08_TRACEABILITY/94_00_TRC_LC08_AMPEL360_SPACET_PLUS_k06-ata-94-consumers_I01-R01.csv)  
  _Done when:_ Consumers are listed with pack version, verification method, and owner.

- Adoption status (RPT): [Adoption status](08_TRACEABILITY/94_00_RPT_LC08_AMPEL360_SPACET_PLUS_k06-ata-94-adoption-status_I01-R01.md)  
  _Done when:_ Each consumer has status + remediation plan if blocked.

---

## 4) Cross-ATA Links (same Knot, coupled closures)

ATA 94 is downstream of the K06 spine; these couplings are mandatory.

- [ATA 90 — Meta spine (NN / Schemas / Trace / DPP)](../ATA_90/)  
  _Comment:_ Provenance expectations and TEKNIA packaging gates.

- [ATA 91 — Schemas](../ATA_91/)  
  _Comment:_ DPP payload/manifest must reference canonical schema IDs.

- [ATA 93 — Traceability Graph](../ATA_93/)  
  _Comment:_ DPP exports must point to trace graph snapshots and evidence links.

- [ATA 95 — SBOM / ModelBOM](../ATA_95/)  
  _Comment:_ DPP packs should reference software/model supply chain artifacts when applicable.

- [ATA 98 — Signed Export Packs](../ATA_98/)  
  _Comment:_ Signing/hashing and verification primitives for released DPP packs.

- [ATA 99 — Master Registers](../ATA_99/)  
  _Comment:_ Consolidated registers; prevents duplicated registries and drift.

**Sim/Test Coupling (100+):**
- [ATA 101](../ATA_101/) / [ATA 107](../ATA_107/) / [ATA 109](../ATA_109/)  
  _Comment:_ Evidence packs feeding DPP must be trace-linked and verifiable.

---

## 5) Control & Monitoring (NKU Values + TEKNIA Sharing Rules)

### 5.1 NKU Control Model
**Primary metric:** NKU Progress Score for K06/ATA94  
**Source of truth:** [NKU ledger](06_EVIDENCE/94_00_TAB_LC06_AMPEL360_SPACET_PLUS_k06-ata-94-nku-ledger_I01-R01.csv)

**Scoring:**
- `score ∈ {0, 0.5, 1.0}`
- **NKU Score** = `Σ(weight × score)` across partitions P1..P8

**No-false-closure (mandatory):**
- `score = 1.0` requires:
  - evidence link(s) in `06_EVIDENCE/...evidence-links...csv`, and
  - decision reference in `07_DECISIONS/...decision-minutes...md` (and approvals if applicable).

### 5.2 Monitoring Cadence
| Control Item | Owner | Frequency | Source | Comment |
|---|---|---:|---|---|
| NKU ledger updates | AI + DATA | Per PR affecting K06/ATA94 | NKU ledger + evidence links | No score uplift without links |
| CI gate compliance | CM + Tooling | Per PR | CI gates + logs | Enforcement mechanism |
| Provenance/signing checks | CM + Security + Tooling | Per PR + release | CI outputs + signed pack logs | “Unsigned release” is a blocker |
| Evidence freshness | SE + V&V | Weekly / per gate | Evidence links register | Detect staleness |
| Decision capture | CM WG + DPP Authority | At gate closure | Decisions + approvals | Required for closure |
| Consumer verification | DPP consumers | Per release | Adoption status | Verify pack authenticity |

### 5.3 Thresholds
- Green ≥ 0.80; Amber 0.50–0.79; Red < 0.50  
Hard blockers: missing P2/P3/P5 closure, missing P7 decision, missing signing/provenance for baseline exports, stale evidence for any closed item.

### 5.4 TEKNIA Sharing Rules
TEKTOKs may be created only when:
- Evidence is reproducible (P6 complete)
- Decision exists (P7 complete, CM-approved)
- Dedup passes (SHA-256)
- NV threshold met (≥ 0.50 internal, ≥ 0.65 external recommended)

### 5.5 TEKNIA Packaging Requirements (mandatory metadata)
Any TEKTOK that triggers or references a DPP export must include:
- knot_id, ata, partitions_closed
- dpp_view_id + dpp_pack_id + release_state
- schema_ids referenced (payload + manifest)
- trace_snapshot_id + evidence_links
- hash_sha256 + signature metadata
- classification + redaction notes
- nv + rationale

### 5.6 Enforcement
CI should validate:
- DPP schema compliance (payload + manifest)
- DPP view registry membership and required evidence completeness
- trace snapshot pointer validity (ATA 93)
- signature/provenance completeness for baseline exports (ATA 98 coupling)
- TEKNIA gate for “approved” TEKTOK status (NV + dedup)

---

## 6) Practical Notes (common failure modes)
- A DPP pack without deterministic provenance metadata is not auditable: treat as invalid.
- Do not embed “live” repo paths without a release reference for baseline states; prefer signed export packs.
- Redaction must be standardized; ad-hoc removal breaks verifiability and comparability.

