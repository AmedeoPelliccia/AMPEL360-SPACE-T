---
title: "K06 ATA 31 — Partitioned Uncertainty Resolution Index"
type: IDX
variant: SPACET
status: Draft
knot_id: K06
ata: "31"
lc_or_subbucket: "LC01"
description: "GitHub-navigable hub for closing K06 (SSOT/Schemas/Identifiers) for ATA 31 (Technology domain) with NKU control and TEKNIA sharing rules."
---

# K06 — Data Governance (SSOT / Schemas / Identifiers)
## ATA 31 — Partitioned Uncertainty Resolution Index (IDX)

This file is the **single navigation hub** for all artifacts required to close **K06** for **ATA 31** (Technology domain).  
NKU progress is credited only when each partition is closed with **evidence + approval**.

> Note: ATA 31 label/title may differ in your Space-T internal register. This index treats ATA 31 as a technology node where **instrumentation / indication / sensing data definitions** require SSOT, stable schemas, and identifier governance. Update the ATA 31 title in your master register if needed—this index remains valid.

---

## 1) Global Navigation (GitHub-navigable)

- Knot overview: [K06 overview](../../00_00_IDX_LC01_SPACET_k06-data-governance-ssot-schemas-identifiers_v01.md)  
  _Comment:_ Canonical K06 scope, impacted ATAs, closure criteria, shared definitions.

- Portal index: [AMPEL360-SPACE-T-PORTAL index](../../../../../00_00_IDX_LC01_SPACET_stakeholder-entrypoints_v01.md)  
  _Comment:_ Global entry point; use it to navigate stakeholders and the knot portfolio.

- Stakeholder entrypoint (AI): [STK_AI entrypoint](../../../../00_00_IDX_LC01_SPACET_stakeholder-ai-entrypoint_v01.md)  
  _Comment:_ AI/ML execution lane; automation hooks and governance helpers.

- ATA 31 home (T-TECHNOLOGY): [AMPEL360_SPACE-T/T-TECHNOLOGY/ATA 31](../../../../../../AMPEL360_SPACE-T/T-TECHNOLOGY/ATA_31-INSTRUMENTS/)  
  _Comment:_ Intended authoritative location for ATA 31 technology outputs. If your folder name differs, update only this link target.

---

## 2) ATA 31 K06 Focus (what uncertainty we are closing)

### Uncertainty to Resolve (ATA-specific)
K06 within ATA 31 is the lack of a single, governed SSOT for:
- **Sensor/parameter identity:** canonical IDs for parameters, sensors, channels, derived values, display labels.
- **Semantics and units:** stable schema for value meaning, units, scaling, frames, tolerances, validity flags.
- **Calibration/provenance:** calibration tables, validity ranges, source lineage, and version governance.
- **Publication and consumption:** machine-consumable exports that downstream ATAs/tools can ingest without ambiguity.
- **Enforcement:** CI gates to prevent uncontrolled divergence (duplicate IDs, unit mismatches, undocumented schema changes).

### Primary consumers (typical)
- Avionics integration / IMA / data buses, health monitoring, operations tooling, simulation/test evidence, DPP/traceability export packs.

---

## 3) Partitioned Uncertainty Resolution Pathway (P1–P8)

Each partition corresponds to a dedicated folder. **Do not credit closure** unless the partition’s “Done” definition is satisfied.

### P1 — Work Breakdown & Ownership (Execution Closure)
- Folder: [01_WBS/](01_WBS/)  
  _Comment:_ Converts uncertainty into executable work packages (tasks, owners, inputs/outputs).

- WBS index: [K06 ATA 31 Work Breakdown](01_WBS/31_00_IDX_LC01_SPACET_k06-ata-31-workbreakdown_v01.md)  
  _Closes:_ “We don’t know what to do next / who owns it.”  
  _Done when:_ T001–T006 exist with owners, acceptance criteria, and artifact links.

- RACI (CSV): [RACI](01_WBS/31_00_MAT_LC06_SPACET_k06-ata-31-raci_v01.csv)  
  _Closes:_ Responsibility ambiguity (execution vs approval).  
  _Done when:_ CM approval path is explicit and accepted.

**Task stubs (minimum set):**
- T001: [SSOT source & ownership](01_WBS/31_00_ACT_LC06_SPACET_k06-t001-ssot-source-ownership_v01.md)  
  _Comment:_ Declares authoritative SSOT (e.g., parameter registry + calibration source) and change control.

- T002: [Identifier grammar](01_WBS/31_00_ACT_LC06_SPACET_k06-t002-identifier-grammar_v01.md)  
  _Comment:_ Defines canonical IDs for parameters/sensors/channels/derived values and naming constraints.

- T003: [Schema definition](01_WBS/31_00_ACT_LC06_SPACET_k06-t003-schema-definition_v01.md)  
  _Comment:_ Stabilizes semantics: units, scaling, frames, validity states, uncertainty, tolerances.

- T004: [Export publication](01_WBS/31_00_ACT_LC06_SPACET_k06-t004-export-publication_v01.md)  
  _Comment:_ Defines published machine-consumable exports and deterministic build procedure.

- T005: [CI validation gates](01_WBS/31_00_ACT_LC06_SPACET_k06-t005-ci-validation-gates_v01.md)  
  _Comment:_ Enforces identifier/schema rules and blocks noncompliant changes at PR time.

- T006: [Baseline parameter set](01_WBS/31_00_ACT_LC06_SPACET_k06-t006-baseline-parameter-set_v01.md)  
  _Comment:_ Produces a frozen baseline of parameters/calibration metadata for downstream consumption.

---

### P2 — IDs & Registry (Identity Closure)
- Folder: [02_IDS_REGISTRY/](02_IDS_REGISTRY/)  
  _Comment:_ Ensures every parameter/sensor/channel has a unique ID, owner, and lifecycle state.

- Standard (STD): [Identifier grammar](02_IDS_REGISTRY/31_00_STD_LC03_SPACET_parameter-identifier-grammar_v01.md)  
  _Done when:_ Grammar is approved and referenced by schema + CI gates.

- Registry (TAB/CSV): [Parameter registry](02_IDS_REGISTRY/31_00_TAB_LC03_SPACET_parameter-registry_v01.csv)  
  _Done when:_ Registry is SSOT (no duplicates), with owners/status and required metadata.

- Change log (LOG): [Registry change log](02_IDS_REGISTRY/31_00_LOG_LC03_SPACET_registry-change-log_v01.md)  
  _Done when:_ Every change references a decision/change record (P7).

---

### P3 — Schema & Versioning (Semantic Closure)
- Folder: [03_SCHEMA/](03_SCHEMA/)  
  _Comment:_ Defines stable machine-readable meaning and compatibility rules.

- Schema (SCH/JSON): [Parameter schema](03_SCHEMA/31_00_SCH_LC03_SPACET_parameter-schema_v01.json)  
  _Done when:_ Schema validates exports and is referenced by CI.

- Standard (STD): [Schema versioning policy](03_SCHEMA/31_00_STD_LC03_SPACET_schema-versioning-policy_v01.md)  
  _Done when:_ Compatibility/breaking-change rules exist and are enforced.

- Units/Frames map (TAB/CSV): [Units and frames mapping](03_SCHEMA/31_00_TAB_LC03_SPACET_units-frames-mapping_v01.csv)  
  _Done when:_ Every field declares unit/frame/scaling/tolerance rule to prevent integration defects.

---

### P4 — Exports (Consumable Data Closure)
- Folder: [04_EXPORTS/](04_EXPORTS/)  
  _Comment:_ Provides reproducible, consumable datasets for downstream ATAs and tooling.

- Baseline dataset (TAB/CSV): [Baseline parameter set](04_EXPORTS/31_00_TAB_LC04_SPACET_baseline-parameter-set_v01.csv)  
  _Done when:_ Export is reproducible, validated, and release-referenced.

- Manifest (RPT): [Export manifest](04_EXPORTS/31_00_RPT_LC04_SPACET_export-manifest_v01.md)  
  _Done when:_ Inputs/tools/versions are recorded; rebuild is deterministic.

- Diagram (DIA): [Parameter map](04_EXPORTS/31_00_DIA_LC04_SPACET_parameter-map_v01.md)  
  _Done when:_ Diagram references match registry IDs and baseline export.

---

### P5 — CI Gates (Enforcement Closure)
- Folder: [05_CI_GATES/](05_CI_GATES/)  
  _Comment:_ Makes governance non-optional; prevents silent drift (IDs, units, schema).

- Requirements (STD): [CI validation requirements](05_CI_GATES/31_00_STD_LC05_SPACET_ci-validation-requirements_v01.md)  
  _Done when:_ Rules map to checks; failures are actionable.

- Checklist (LOG): [CI checklist](05_CI_GATES/31_00_LOG_LC05_SPACET_ci-checklist_v01.md)  
  _Done when:_ Checklist matches CI outputs and reviewer expectations.

- Sample run (RPT): [CI validation sample run](05_CI_GATES/31_00_RPT_LC05_SPACET_ci-validation-sample-run_v01.md)  
  _Done when:_ Demonstrates representative pass/fail cases.

---

### P6 — Evidence Pack (Proof Closure)
- Folder: [06_EVIDENCE/](06_EVIDENCE/)  
  _Comment:_ NKU credit requires reproducible evidence and stable links.

- Evidence pack index (IDX): [Evidence pack](06_EVIDENCE/31_00_IDX_LC06_SPACET_k06-ata-31-evidence-pack_v01.md)  
  _Done when:_ All required evidence is linked and current.

- Evidence links (TRC/CSV): [Evidence links register](06_EVIDENCE/31_00_TRC_LC06_SPACET_k06-ata-31-evidence-links_v01.csv)  
  _Done when:_ Each claim has an evidence link and status (OK/STALE/MISSING).

- NKU ledger (TAB/CSV): [NKU ledger](06_EVIDENCE/31_00_TAB_LC06_SPACET_k06-ata-31-nku-ledger_v01.csv)  
  _Done when:_ Partition scores are updated and backed by evidence + decision.

---

### P7 — Decisions & Approvals (Authority Closure)
- Folder: [07_DECISIONS/](07_DECISIONS/)  
  _Comment:_ Converts evidence into an approved baseline outcome.

- Decision minutes (MIN): [Decision minutes](07_DECISIONS/31_00_MIN_LC07_SPACET_k06-ata-31-decision-minutes_v01.md)  
  _Done when:_ Decision, rationale, dissent/risks are recorded.

- Approvals log (LOG): [Approvals log](07_DECISIONS/31_00_LOG_LC07_SPACET_k06-ata-31-approvals_v01.md)  
  _Done when:_ CM approval + any required sign-offs are referenced.

---

### P8 — Traceability & Adoption (Impact Closure)
- Folder: [08_TRACEABILITY/](08_TRACEABILITY/)  
  _Comment:_ Ensures consumers adopt the SSOT; prevents “closed on paper”.

- Consumers (TRC/CSV): [Consumers list](08_TRACEABILITY/31_00_TRC_LC08_SPACET_k06-ata-31-consumers_v01.csv)  
  _Done when:_ Consumers are listed with interface/version and owner.

- Adoption status (RPT): [Adoption status](08_TRACEABILITY/31_00_RPT_LC08_SPACET_k06-ata-31-adoption-status_v01.md)  
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
  _Comment:_ Ensures parameter governance supports DPP provenance/exports.

- [ATA 95 — SBOM / ModelBOM](../ATA_95/)  
  _Comment:_ Ensures parameter governance aligns with software/model supply-chain trace.

- [ATA 98 — Signed Export Packs](../ATA_98/)  
  _Comment:_ Enables signed, auditable export packaging and provenance enforcement.

- [ATA 99 — Master Registers](../ATA_99/)  
  _Comment:_ Consolidates registers and anti-duplication controls.

**Technology coupling (recommended to track if applicable):**
- [ATA 42 — Integrated Modular Avionics / Data Platform](../ATA_42/)  
  _Comment:_ Data buses/IMA often consume parameter registries and schemas.
- [ATA 46 — Information Systems / Data Distribution](../ATA_46/)  
  _Comment:_ Distribution and labeling rules are frequent integration failure points.
- [ATA 100+ — Sim/Test Evidence Nodes](../ATA_107/) and [ATA_109](../ATA_109/)  
  _Comment:_ Simulation/test evidence must reference the same parameter IDs and schema.

---

## 5) Control & Monitoring (NKU Values + TEKNIA Sharing Rules)

This section defines how progress is measured, controlled, and credited (NKU), and how outputs are packaged and shared under TEKNIA rules (evidence-first, anti-noise, deduplicated, authority-approved).

### 5.1 NKU Control Model
**Primary metric:** NKU Progress Score for K06/ATA31  
**Source of truth:** [NKU ledger](06_EVIDENCE/31_00_TAB_LC06_SPACET_k06-ata-31-nku-ledger_v01.csv)

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
| NKU ledger updates | AI + DATA | Per PR affecting K06/ATA31 | NKU ledger + evidence links | No score uplift without links |
| CI gate compliance | CM + Tooling | Per PR | CI gates + logs | Enforcement mechanism |
| Evidence completeness | SE + V&V | Weekly / per gate | Evidence pack index | Detect staleness |
| Decision capture | CM WG | At gate closure | Decisions + approvals | Required for closure |
| Adoption tracking | Avionics/IMA owners + OPS + SIM/TEST | Biweekly | Consumers + adoption status | Avoid “paper closure” |

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
- Do not accept “released parameter exports” without schema validation (P3) and CI enforcement (P5).
- Do not credit NKU closure without decision minutes (P7) and an evidence pack (P6).
- Treat unit/scaling/frame mismatches as priority risks; they propagate silently into sim/test and ops analytics.
```
