---
title: "K06 ATA 46 — Partitioned Uncertainty Resolution Index"
type: IDX
variant: SPACET
status: Draft
knot_id: K06
ata: "46"
lc_or_subbucket: "LC01"
description: "GitHub-navigable hub for closing K06 (SSOT/Schemas/Identifiers) for ATA 46 (Technology domain) with NKU control and TEKNIA sharing rules."
---

# K06 — Data Governance (SSOT / Schemas / Identifiers)
## ATA 46 — Partitioned Uncertainty Resolution Index (IDX)

This file is the **single navigation hub** for all artifacts required to close **K06** for **ATA 46** (Technology domain).  
NKU progress is credited only when each partition is closed with **evidence + approval**.

> Note: ATA 46 label/title may differ in your Space-T internal register. This index treats ATA 46 as a technology node focused on **information systems / data distribution / data services**, where SSOT, stable schemas, and identifier governance are critical. Update the ATA title in your master register if needed—this index remains valid.

---

## 1) Global Navigation (GitHub-navigable)

- Knot overview: [K06 overview](../../00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_LC01_K06_CM__k06-data-governance-ssot-schemas-identifiers_I01-R01.md)  
  _Comment:_ Canonical K06 scope, impacted ATAs, closure criteria, shared definitions.

- Portal index: [AMPEL360-SPACE-T-PORTAL index](../../../../../00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_LC01_K04_CM__stakeholder-entrypoints_I01-R01.md)  
  _Comment:_ Global entry point; use it to navigate stakeholders and the knot portfolio.

- Stakeholder entrypoint (AI): [STK_AI entrypoint](../../../../00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_LC01_K04_AI__stakeholder-ai-entrypoint_I01-R01.md)  
  _Comment:_ AI/ML execution lane; automation hooks and governance helpers.

- ATA 46 home (T-TECHNOLOGY): [AMPEL360_SPACE-T/T-TECHNOLOGY/ATA 46](../../../../../../AMPEL360_SPACE-T/T-TECHNOLOGY/ATA_46-INFORMATION_SYSTEMS/)  
  _Comment:_ Intended authoritative location for ATA 46 outputs. If your folder name differs, update only this link target.

---

## 2) ATA 46 K06 Focus (what uncertainty we are closing)

### Uncertainty to Resolve (ATA-specific)
K06 within ATA 46 is the absence of a single governed SSOT for:
- **Service identity:** canonical IDs for data services, APIs, endpoints, contracts, datasets, and routing rules.
- **Semantic correctness:** stable schemas for service payloads, metadata, units, frames, validity, timing, QoS.
- **Distribution rules:** canonical topic/routing/labeling rules, data retention policies, and access controls (as metadata).
- **Publication and consumption:** machine-consumable exports for downstream ATAs/tools (integration, ops monitoring, sim/test).
- **Enforcement:** CI gates preventing drift (duplicate IDs, unversioned schemas, undocumented breaking changes).

### Primary consumers (typical)
- Avionics/IMA runtime, communications/telemetry routing, ops dashboards, health monitoring, sim/test harnesses, traceability/DPP exports.

---

## 3) Partitioned Uncertainty Resolution Pathway (P1–P8)

Each partition corresponds to a dedicated folder. **Do not credit closure** unless the partition’s “Done” definition is satisfied.

### P1 — Work Breakdown & Ownership (Execution Closure)
- Folder: [01_WBS/](01_WBS/)  
  _Comment:_ Converts uncertainty into executable work packages (tasks, owners, inputs/outputs).

- WBS index: [K06 ATA 46 Work Breakdown](01_WBS/46_00_IDX_LC01_AMPEL360_SPACET_PLUS_k06-ata-46-workbreakdown_I01-R01.md)  
  _Closes:_ “We don’t know what to do next / who owns it.”  
  _Done when:_ T001–T006 exist with owners, acceptance criteria, and artifact links.

- RACI (CSV): [RACI](01_WBS/46_00_MAT_LC06_AMPEL360_SPACET_PLUS_k06-ata-46-raci_I01-R01.csv)  
  _Closes:_ Responsibility ambiguity (execution vs approval).  
  _Done when:_ CM approval path is explicit and accepted.

**Task stubs (minimum set):**
- T001: [SSOT source & ownership](01_WBS/46_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t001-ssot-source-ownership_I01-R01.md)  
  _Comment:_ Declares authoritative SSOT for service catalogs/contracts/datasets and defines change control.

- T002: [Identifier grammar](01_WBS/46_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t002-identifier-grammar_I01-R01.md)  
  _Comment:_ Defines canonical IDs for services/endpoints/contracts/datasets and naming/version constraints.

- T003: [Schema definition](01_WBS/46_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t003-schema-definition_I01-R01.md)  
  _Comment:_ Stabilizes semantics for payloads/metadata (units, frames, QoS, timing, validity).

- T004: [Export publication](01_WBS/46_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t004-export-publication_I01-R01.md)  
  _Comment:_ Defines deterministic export packs (service catalog + contract schemas + manifests).

- T005: [CI validation gates](01_WBS/46_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t005-ci-validation-gates_I01-R01.md)  
  _Comment:_ Enforces rules; blocks noncompliant PRs (duplicate IDs, breaking changes without versioning).

- T006: [Baseline service contract set](01_WBS/46_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t006-baseline-service-contract-set_I01-R01.md)  
  _Comment:_ Produces a frozen baseline of services/contracts for integration and ops usage.

---

### P2 — IDs & Registry (Identity Closure)
- Folder: [02_IDS_REGISTRY/](02_IDS_REGISTRY/)  
  _Comment:_ Ensures every service/endpoint/contract/dataset has a unique ID, owner, lifecycle state, and dedup policy.

- Standard (STD): [Identifier grammar](02_IDS_REGISTRY/46_00_STD_LC03_AMPEL360_SPACET_PLUS_service-identifier-grammar_I01-R01.md)  
  _Done when:_ Grammar is approved and referenced by schema + CI gates.

- Registry (TAB/CSV): [Service registry](02_IDS_REGISTRY/46_00_TAB_LC03_AMPEL360_SPACET_PLUS_service-registry_I01-R01.csv)  
  _Done when:_ Registry is SSOT (no duplicates), with owners/status and required metadata.

- Change log (LOG): [Registry change log](02_IDS_REGISTRY/46_00_LOG_LC03_AMPEL360_SPACET_PLUS_registry-change-log_I01-R01.md)  
  _Done when:_ Every change references a decision/change record (P7).

---

### P3 — Schema & Versioning (Semantic Closure)
- Folder: [03_SCHEMA/](03_SCHEMA/)  
  _Comment:_ Defines stable machine-readable meaning and compatibility rules for service payloads and metadata.

- Schema (SCH/JSON): [Service payload schema](03_SCHEMA/46_00_SCH_LC03_AMPEL360_SPACET_PLUS_service-payload-schema_I01-R01.json)  
  _Done when:_ Schema validates exports and is referenced by CI.

- Standard (STD): [Schema versioning policy](03_SCHEMA/46_00_STD_LC03_AMPEL360_SPACET_PLUS_schema-versioning-policy_I01-R01.md)  
  _Done when:_ Compatibility/breaking-change rules exist and are enforced.

- Units/Frames map (TAB/CSV): [Units and frames mapping](03_SCHEMA/46_00_TAB_LC03_AMPEL360_SPACET_PLUS_units-frames-mapping_I01-R01.csv)  
  _Done when:_ Every field declares unit/frame/tolerance rule to prevent integration defects.

---

### P4 — Exports (Consumable Data Closure)
- Folder: [04_EXPORTS/](04_EXPORTS/)  
  _Comment:_ Provides reproducible, consumable service catalogs and contract packs for integration and tooling.

- Baseline dataset (TAB/CSV): [Baseline service contract set](04_EXPORTS/46_00_TAB_LC04_AMPEL360_SPACET_PLUS_baseline-service-contract-set_I01-R01.csv)  
  _Done when:_ Export is reproducible, validated, and release-referenced.

- Manifest (RPT): [Export manifest](04_EXPORTS/46_00_RPT_LC04_AMPEL360_SPACET_PLUS_export-manifest_I01-R01.md)  
  _Done when:_ Inputs/tools/versions are recorded; rebuild is deterministic.

- Diagram (DIA): [Service map](04_EXPORTS/46_00_DIA_LC04_AMPEL360_SPACET_PLUS_service-map_I01-R01.md)  
  _Done when:_ Diagram references match registry IDs and baseline export.

---

### P5 — CI Gates (Enforcement Closure)
- Folder: [05_CI_GATES/](05_CI_GATES/)  
  _Comment:_ Makes governance non-optional; prevents silent drift in services/contracts/schemas.

- Requirements (STD): [CI validation requirements](05_CI_GATES/46_00_STD_LC05_AMPEL360_SPACET_PLUS_ci-validation-requirements_I01-R01.md)  
  _Done when:_ Rules map to checks; failures are actionable.

- Checklist (LOG): [CI checklist](05_CI_GATES/46_00_LOG_LC05_AMPEL360_SPACET_PLUS_ci-checklist_I01-R01.md)  
  _Done when:_ Checklist matches CI outputs and reviewer expectations.

- Sample run (RPT): [CI validation sample run](05_CI_GATES/46_00_RPT_LC05_AMPEL360_SPACET_PLUS_ci-validation-sample-run_I01-R01.md)  
  _Done when:_ Demonstrates representative pass/fail cases.

---

### P6 — Evidence Pack (Proof Closure)
- Folder: [06_EVIDENCE/](06_EVIDENCE/)  
  _Comment:_ NKU credit requires reproducible evidence and stable links.

- Evidence pack index (IDX): [Evidence pack](06_EVIDENCE/46_00_IDX_LC06_AMPEL360_SPACET_PLUS_k06-ata-46-evidence-pack_I01-R01.md)  
  _Done when:_ All required evidence is linked and current.

- Evidence links (TRC/CSV): [Evidence links register](06_EVIDENCE/46_00_TRC_LC06_AMPEL360_SPACET_PLUS_k06-ata-46-evidence-links_I01-R01.csv)  
  _Done when:_ Each claim has an evidence link and status (OK/STALE/MISSING).

- NKU ledger (TAB/CSV): [NKU ledger](06_EVIDENCE/46_00_TAB_LC06_AMPEL360_SPACET_PLUS_k06-ata-46-nku-ledger_I01-R01.csv)  
  _Done when:_ Partition scores are updated and backed by evidence + decision.

---

### P7 — Decisions & Approvals (Authority Closure)
- Folder: [07_DECISIONS/](07_DECISIONS/)  
  _Comment:_ Converts evidence into an approved baseline outcome.

- Decision minutes (MIN): [Decision minutes](07_DECISIONS/46_00_MIN_LC07_AMPEL360_SPACET_PLUS_k06-ata-46-decision-minutes_I01-R01.md)  
  _Done when:_ Decision, rationale, dissent/risks are recorded.

- Approvals log (LOG): [Approvals log](07_DECISIONS/46_00_LOG_LC07_AMPEL360_SPACET_PLUS_k06-ata-46-approvals_I01-R01.md)  
  _Done when:_ CM approval + any required sign-offs are referenced.

---

### P8 — Traceability & Adoption (Impact Closure)
- Folder: [08_TRACEABILITY/](08_TRACEABILITY/)  
  _Comment:_ Ensures consumers adopt the SSOT; prevents “closed on paper”.

- Consumers (TRC/CSV): [Consumers list](08_TRACEABILITY/46_00_TRC_LC08_AMPEL360_SPACET_PLUS_k06-ata-46-consumers_I01-R01.csv)  
  _Done when:_ Consumers are listed with interface/version and owner.

- Adoption status (RPT): [Adoption status](08_TRACEABILITY/46_00_RPT_LC08_AMPEL360_SPACET_PLUS_k06-ata-46-adoption-status_I01-R01.md)  
  _Done when:_ Each consumer has status + remediation plan if blocked.

---

## 4) Cross-ATA Links (same Knot, coupled closures)

- [ATA 00 — Program Governance](../ATA_00/)  
  _Comment:_ Defines naming/metadata/registry authority; blocks false closure if missing.

- [ATA 45 — Information Exchange](../ATA_45/)  
  _Comment:_ Message-level catalogs and contracts should align with service-level catalogs and routing rules.

- [ATA 91 — Schemas](../ATA_91/)  
  _Comment:_ Provides canonical schema governance and validation primitives.

- [ATA 93 — Traceability Graph](../ATA_93/)  
  _Comment:_ Enables evidence trace from IDs → schema → export → decision.

- [ATA 94 — DPP](../ATA_94/)  
  _Comment:_ Ensures service governance supports DPP provenance/exports.

- [ATA 95 — SBOM / ModelBOM](../ATA_95/)  
  _Comment:_ Ensures service governance aligns with software/model supply-chain trace.

- [ATA 98 — Signed Export Packs](../ATA_98/)  
  _Comment:_ Enables signed, auditable export packaging and provenance enforcement.

- [ATA 99 — Master Registers](../ATA_99/)  
  _Comment:_ Consolidates registers and anti-duplication controls.

---

## 5) Control & Monitoring (NKU Values + TEKNIA Sharing Rules)

### 5.1 NKU Control Model
**Primary metric:** NKU Progress Score for K06/ATA46  
**Source of truth:** [NKU ledger](06_EVIDENCE/46_00_TAB_LC06_AMPEL360_SPACET_PLUS_k06-ata-46-nku-ledger_I01-R01.csv)

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
| NKU ledger updates | AI + DATA | Per PR affecting K06/ATA46 | NKU ledger + evidence links | No score uplift without links |
| CI gate compliance | CM + Tooling | Per PR | CI gates + logs | Enforcement mechanism |
| Evidence completeness | SE + V&V | Weekly / per gate | Evidence pack index | Detect staleness |
| Decision capture | CM WG | At gate closure | Decisions + approvals | Required for closure |
| Adoption tracking | Data Platform owners + OPS + SIM/TEST | Biweekly | Consumers + adoption status | Avoid “paper closure” |

### 5.3 Thresholds
- Green ≥ 0.80; Amber 0.50–0.79; Red < 0.50  
Hard blockers: missing P2/P3/P5 closure, missing P7 decision, stale evidence for any closed item.

### 5.4 TEKNIA Sharing Rules
TEKTOKs may be created only when:
- Evidence is reproducible (P6 complete)
- Decision exists (P7 complete, CM-approved)
- Dedup passes (SHA-256)
- NV threshold met (≥ 0.50 internal, ≥ 0.65 external recommended)

### 5.5 Enforcement
CI should validate NKU ledger integrity and block false closure and “approved” TEKTOKs without NV+dedup compliance.

---

## 6) Practical Notes (common failure modes)
- Do not accept “released service catalogs” without schema validation (P3) and CI enforcement (P5).
- Do not credit NKU closure without decision minutes (P7) and an evidence pack (P6).
- Treat routing/labeling semantics and QoS/timing metadata as priority risks; they break interoperability silently.
