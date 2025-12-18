---
title: "K06 ATA 45 — Partitioned Uncertainty Resolution Index"
type: IDX
variant: SPACET
status: Draft
knot_id: K06
ata: "45"
lc_or_subbucket: "LC01"
description: "GitHub-navigable hub for closing K06 (SSOT/Schemas/Identifiers) for ATA 45 (Technology domain) with NKU control and TEKNIA sharing rules."
---

# K06 — Data Governance (SSOT / Schemas / Identifiers)
## ATA 45 — Partitioned Uncertainty Resolution Index (IDX)

This file is the **single navigation hub** for all artifacts required to close **K06** for **ATA 45** (Technology domain).  
NKU progress is credited only when each partition is closed with **evidence + approval**.

> Note: ATA 45 label/title may differ in your Space-T internal register. This index treats ATA 45 as a technology node where **information exchange, sensing/telemetry, and/or communications data definitions** require SSOT, stable schemas, and identifier governance. Update the ATA 45 title in your master register if needed—this index remains valid.

---

## 1) Global Navigation (GitHub-navigable)

- Knot overview: [K06 overview](../../../../../STK_DATA-data-data-governance/KNOTS/K06_data-governance-ssot-schemas-identifiers/00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_LC01_K06_DATA__k06-data-governance-ssot-schemas-identifiers_IDX_I01-R01_ACTIVE.md)  
  _Comment:_ Canonical K06 scope, impacted ATAs, closure criteria, shared definitions.

- Portal index: [AMPEL360-SPACE-T-PORTAL index](../../../../../00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_LC01_K04_CM__stakeholder-entrypoints_IDX_I01-R01_ACTIVE.md)  
  _Comment:_ Global entry point; use it to navigate stakeholders and the knot portfolio.

- Stakeholder entrypoint (AI): [STK_AI entrypoint](../../../../00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_LC01_K11_AI__stakeholder-ai-entrypoint_IDX_I01-R01_ACTIVE.md)  
  _Comment:_ AI/ML execution lane; automation hooks and governance helpers.

- ATA 45 home (T-TECHNOLOGY): [AMPEL360_SPACE-T/T-TECHNOLOGY/ATA 45](../../../../../../AMPEL360_SPACE-T/T-TECHNOLOGY/ATA_45-INFORMATION_EXCHANGE/)  
  _Comment:_ Intended authoritative location for ATA 45 outputs. If your folder name differs, update only this link target.

---

## 2) ATA 45 K06 Focus (what uncertainty we are closing)

### Uncertainty to Resolve (ATA-specific)
K06 within ATA 45 is the absence of a single governed SSOT for:
- **Message identity:** canonical IDs for messages, topics, channels, interfaces, ports, endpoints.
- **Semantic correctness:** stable schemas for payloads, fields, units, frames, enums, validity flags.
- **Interface governance:** interface contracts (producer/consumer ownership), compatibility rules, breaking-change controls.
- **Publication and consumption:** machine-consumable exports for downstream ATAs/tools (integration, sim/test, ops).
- **Enforcement:** CI gates preventing drift (duplicate IDs, unversioned schemas, undocumented changes).

### Primary consumers (typical)
- Avionics integration and networks, onboard/offboard telemetry routing, ops monitoring, sim/test harnesses, traceability/DPP export packs.

---

## 3) Partitioned Uncertainty Resolution Pathway (P1–P8)

Each partition corresponds to a dedicated folder. **Do not credit closure** unless the partition’s “Done” definition is satisfied.

### P1 — Work Breakdown & Ownership (Execution Closure)
- Folder: [01_WBS/](01_WBS/)  
  _Comment:_ Converts uncertainty into executable work packages (tasks, owners, inputs/outputs).

- WBS index: [K06 ATA 45 Work Breakdown](01_WBS/45_00_IDX_LC01_AMPEL360_SPACET_PLUS_k06-ata-45-workbreakdown_I01-R01.md)  
  _Closes:_ “We don’t know what to do next / who owns it.”  
  _Done when:_ T001–T006 exist with owners, acceptance criteria, and artifact links.

- RACI (CSV): [RACI](01_WBS/45_00_MAT_LC06_AMPEL360_SPACET_PLUS_k06-ata-45-raci_I01-R01.csv)  
  _Closes:_ Responsibility ambiguity (execution vs approval).  
  _Done when:_ CM approval path is explicit and accepted.

**Task stubs (minimum set):**
- T001: [SSOT source & ownership](01_WBS/45_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t001-ssot-source-ownership_I01-R01.md)  
  _Comment:_ Declares authoritative SSOT for message catalogs and interface contracts and defines change control.

- T002: [Identifier grammar](01_WBS/45_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t002-identifier-grammar_I01-R01.md)  
  _Comment:_ Defines canonical IDs for messages/topics/channels and constraints on naming/versioning.

- T003: [Schema definition](01_WBS/45_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t003-schema-definition_I01-R01.md)  
  _Comment:_ Stabilizes payload semantics (fields, units, frames, enums, validity, timestamps).

- T004: [Export publication](01_WBS/45_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t004-export-publication_I01-R01.md)  
  _Comment:_ Defines published interface contract exports (schemas + catalogs) and deterministic generation.

- T005: [CI validation gates](01_WBS/45_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t005-ci-validation-gates_I01-R01.md)  
  _Comment:_ Enforces contract/schema rules and blocks noncompliant PRs.

- T006: [Baseline interface contract set](01_WBS/45_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t006-baseline-interface-contract-set_I01-R01.md)  
  _Comment:_ Produces a frozen baseline catalog of interfaces/contracts for downstream integration and verification.

---

### P2 — IDs & Registry (Identity Closure)
- Folder: [02_IDS_REGISTRY/](02_IDS_REGISTRY/)  
  _Comment:_ Ensures every message/topic/interface has a unique ID, owner, lifecycle state, and dedup policy.

- Standard (STD): [Identifier grammar](02_IDS_REGISTRY/45_00_STD_LC03_AMPEL360_SPACET_PLUS_message-identifier-grammar_I01-R01.md)  
  _Done when:_ Grammar is approved and referenced by schema + CI gates.

- Registry (TAB/CSV): [Message & interface registry](02_IDS_REGISTRY/45_00_TAB_LC03_AMPEL360_SPACET_PLUS_message-interface-registry_I01-R01.csv)  
  _Done when:_ Registry is SSOT (no duplicates), with owners/status and required metadata.

- Change log (LOG): [Registry change log](02_IDS_REGISTRY/45_00_LOG_LC03_AMPEL360_SPACET_PLUS_registry-change-log_I01-R01.md)  
  _Done when:_ Every change references a decision/change record (P7).

---

### P3 — Schema & Versioning (Semantic Closure)
- Folder: [03_SCHEMA/](03_SCHEMA/)  
  _Comment:_ Defines stable machine-readable meaning and compatibility rules for payloads and contracts.

- Schema (SCH/JSON): [Interface payload schema](03_SCHEMA/45_00_SCH_LC03_AMPEL360_SPACET_PLUS_interface-payload-schema_I01-R01.json)  
  _Done when:_ Schema validates exports and is referenced by CI.

- Standard (STD): [Schema versioning policy](03_SCHEMA/45_00_STD_LC03_AMPEL360_SPACET_PLUS_schema-versioning-policy_I01-R01.md)  
  _Done when:_ Compatibility/breaking-change rules exist and are enforced.

- Units/Frames map (TAB/CSV): [Units and frames mapping](03_SCHEMA/45_00_TAB_LC03_AMPEL360_SPACET_PLUS_units-frames-mapping_I01-R01.csv)  
  _Done when:_ Every field declares unit/frame/tolerance rule to prevent integration defects.

---

### P4 — Exports (Consumable Data Closure)
- Folder: [04_EXPORTS/](04_EXPORTS/)  
  _Comment:_ Provides reproducible, consumable interface catalogs and schema packs for integration and tooling.

- Baseline dataset (TAB/CSV): [Baseline interface contract set](04_EXPORTS/45_00_TAB_LC04_AMPEL360_SPACET_PLUS_baseline-interface-contract-set_I01-R01.csv)  
  _Done when:_ Export is reproducible, validated, and release-referenced.

- Manifest (RPT): [Export manifest](04_EXPORTS/45_00_RPT_LC04_AMPEL360_SPACET_PLUS_export-manifest_I01-R01.md)  
  _Done when:_ Inputs/tools/versions are recorded; rebuild is deterministic.

- Diagram (DIA): [Interface map](04_EXPORTS/45_00_DIA_LC04_AMPEL360_SPACET_PLUS_interface-map_I01-R01.md)  
  _Done when:_ Diagram references match registry IDs and baseline export.

---

### P5 — CI Gates (Enforcement Closure)
- Folder: [05_CI_GATES/](05_CI_GATES/)  
  _Comment:_ Makes governance non-optional; prevents silent drift in contracts/schemas/IDs.

- Requirements (STD): [CI validation requirements](05_CI_GATES/45_00_STD_LC05_AMPEL360_SPACET_PLUS_ci-validation-requirements_I01-R01.md)  
  _Done when:_ Rules map to checks; failures are actionable.

- Checklist (LOG): [CI checklist](05_CI_GATES/45_00_LOG_LC05_AMPEL360_SPACET_PLUS_ci-checklist_I01-R01.md)  
  _Done when:_ Checklist matches CI outputs and reviewer expectations.

- Sample run (RPT): [CI validation sample run](05_CI_GATES/45_00_RPT_LC05_AMPEL360_SPACET_PLUS_ci-validation-sample-run_I01-R01.md)  
  _Done when:_ Demonstrates representative pass/fail cases.

---

### P6 — Evidence Pack (Proof Closure)
- Folder: [06_EVIDENCE/](06_EVIDENCE/)  
  _Comment:_ NKU credit requires reproducible evidence and stable links.

- Evidence pack index (IDX): [Evidence pack](06_EVIDENCE/45_00_IDX_LC06_AMPEL360_SPACET_PLUS_k06-ata-45-evidence-pack_I01-R01.md)  
  _Done when:_ All required evidence is linked and current.

- Evidence links (TRC/CSV): [Evidence links register](06_EVIDENCE/45_00_TRC_LC06_AMPEL360_SPACET_PLUS_k06-ata-45-evidence-links_I01-R01.csv)  
  _Done when:_ Each claim has an evidence link and status (OK/STALE/MISSING).

- NKU ledger (TAB/CSV): [NKU ledger](06_EVIDENCE/45_00_TAB_LC06_AMPEL360_SPACET_PLUS_k06-ata-45-nku-ledger_I01-R01.csv)  
  _Done when:_ Partition scores are updated and backed by evidence + decision.

---

### P7 — Decisions & Approvals (Authority Closure)
- Folder: [07_DECISIONS/](07_DECISIONS/)  
  _Comment:_ Converts evidence into an approved baseline outcome.

- Decision minutes (MIN): [Decision minutes](07_DECISIONS/45_00_MIN_LC07_AMPEL360_SPACET_PLUS_k06-ata-45-decision-minutes_I01-R01.md)  
  _Done when:_ Decision, rationale, dissent/risks are recorded.

- Approvals log (LOG): [Approvals log](07_DECISIONS/45_00_LOG_LC07_AMPEL360_SPACET_PLUS_k06-ata-45-approvals_I01-R01.md)  
  _Done when:_ CM approval + any required sign-offs are referenced.

---

### P8 — Traceability & Adoption (Impact Closure)
- Folder: [08_TRACEABILITY/](08_TRACEABILITY/)  
  _Comment:_ Ensures consumers adopt the SSOT; prevents “closed on paper”.

- Consumers (TRC/CSV): [Consumers list](08_TRACEABILITY/45_00_TRC_LC08_AMPEL360_SPACET_PLUS_k06-ata-45-consumers_I01-R01.csv)  
  _Done when:_ Consumers are listed with interface/version and owner.

- Adoption status (RPT): [Adoption status](08_TRACEABILITY/45_00_RPT_LC08_AMPEL360_SPACET_PLUS_k06-ata-45-adoption-status_I01-R01.md)  
  _Done when:_ Each consumer has status + remediation plan if blocked.

---

## 4) Cross-ATA Links (same Knot, coupled closures)

- [ATA 00 — Program Governance](../ATA_00/)  
  _Comment:_ Defines naming/metadata/registry authority; blocks false closure if missing.

- [ATA 91 — Schemas](../ATA_91/)  
  _Comment:_ Provides canonical schema governance and validation primitives.

- [ATA 93 — Traceability Graph](../ATA_93/)  
  _Comment:_ Enables evidence trace from IDs → schema → export → decision.

- [ATA 94 — DPP](../ATA_94/)  
  _Comment:_ Ensures interface governance supports DPP provenance/exports.

- [ATA 95 — SBOM / ModelBOM](../ATA_95/)  
  _Comment:_ Ensures interface governance aligns with software/model supply-chain trace.

- [ATA 98 — Signed Export Packs](../../../../../STK_DATA-data-data-governance/KNOTS/K08_dpp-sbom-provenance-scope/ATA_TASKS/ATA_98)  
  _Comment:_ Enables signed, auditable export packaging and provenance enforcement.

- [ATA 99 — Master Registers](../ATA_99/)  
  _Comment:_ Consolidates registers and anti-duplication controls.

**Technology coupling (recommended):**
- [ATA 42 — IMA / Data Platform](../../../../../STK_CERT-cert-certification-authorities/KNOTS/K01_certification-authority-basis/ATA_TASKS/ATA_42)  
  _Comment:_ Often the runtime substrate for message contracts and distribution.
- [ATA 46 — Information Systems / Data Distribution](../ATA_46/)  
  _Comment:_ Frequent integration failure point: labeling, routing, and interface compatibility.

---

## 5) Control & Monitoring (NKU Values + TEKNIA Sharing Rules)

### 5.1 NKU Control Model
**Primary metric:** NKU Progress Score for K06/ATA45  
**Source of truth:** [NKU ledger](06_EVIDENCE/45_00_TAB_LC06_AMPEL360_SPACET_PLUS_k06-ata-45-nku-ledger_I01-R01.csv)

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
| NKU ledger updates | AI + DATA | Per PR affecting K06/ATA45 | NKU ledger + evidence links | No score uplift without links |
| CI gate compliance | CM + Tooling | Per PR | CI gates + logs | Enforcement mechanism |
| Evidence completeness | SE + V&V | Weekly / per gate | Evidence pack index | Detect staleness |
| Decision capture | CM WG | At gate closure | Decisions + approvals | Required for closure |
| Adoption tracking | Avionics/Networks owners + OPS + SIM/TEST | Biweekly | Consumers + adoption status | Avoid “paper closure” |

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
- Do not accept “released interface catalogs” without schema validation (P3) and CI enforcement (P5).
- Do not credit NKU closure without decision minutes (P7) and an evidence pack (P6).
- Treat enums/units/timestamp semantics as priority risks; they break interoperability silently.
```
