---
title: "K06 ATA 90 — Partitioned Uncertainty Resolution Index"
type: IDX
variant: SPACET
status: Draft
knot_id: K06
ata: "90"
lc_or_subbucket: "LC01"
description: "GitHub-navigable hub for closing K06 (SSOT/Schemas/Identifiers) for ATA 90 (Neural Networks, Schemas, Wiring, Traceability, DPP) with NKU control and TEKNIA sharing rules."
---

# K06 — Data Governance (SSOT / Schemas / Identifiers)
## ATA 90 — Partitioned Uncertainty Resolution Index (IDX)

This file is the **single navigation hub** for all artifacts required to close **K06** for **ATA 90** (your domain for **Neural Networks, Schemas, Wiring, Traceability, and DPP**).  
NKU progress is credited only when each partition is closed with **evidence + approval**.

> ATA 90 is a governance-heavy “meta-domain” in Space-T: this index is intentionally stricter on schema identity, trace graph integrity, and export provenance.

---

## 1) Global Navigation (GitHub-navigable)

- Knot overview: [K06 overview](../../00_00_IDX_LC01_AMPEL360_SPACET_PLUS_k06-data-governance-ssot-schemas-identifiers_v01.md)  
  _Comment:_ Canonical K06 scope, impacted ATAs, closure criteria, and shared definitions.

- Portal index: [AMPEL360-SPACE-T-PORTAL index](../../../../../00_00_IDX_LC01_AMPEL360_SPACET_PLUS_stakeholder-entrypoints_v01.md)  
  _Comment:_ Global entry point; use it to navigate stakeholders and the knot portfolio.

- Stakeholder entrypoint (AI): [STK_AI entrypoint](../../../../00_00_IDX_LC01_AMPEL360_SPACET_PLUS_stakeholder-ai-entrypoint_v01.md)  
  _Comment:_ AI/ML execution lane; automation hooks and governance helpers.

- ATA 90 home (N/Meta): [AMPEL360_SPACE-T/N-NEURAL_NETWORKS/ATA 90](../../../../../../AMPEL360_SPACE-T/N-NEURAL_NETWORKS/ATA_90-NN-SCHEMAS-TRACEABILITY-DPP/)  
  _Comment:_ Intended authoritative location for ATA 90 outputs. If your folder name differs, update only this link target.

---

## 2) ATA 90 K06 Focus (what uncertainty we are closing)

### Uncertainty to Resolve (ATA-specific)
K06 within ATA 90 is the absence of a single governed SSOT for:
- **Schema registry:** canonical IDs for schemas, versions, and compatibility rules across the program.
- **Trace graph primitives:** identifiers for nodes/edges, link semantics, and evidence reference rules.
- **Wiring/dataflow documentation IDs:** stable identity for signals/wires/messages/topics and their authoritative definitions.
- **Model & dataset identity:** canonical IDs for ML models, training datasets, feature definitions, evaluation suites.
- **DPP/exports identity:** canonical IDs for DPP artifacts, export packs, signatures, and provenance metadata.
- **Enforcement:** CI gates ensuring no “untraceable” or “unnamed” artifacts enter baseline, and preventing schema drift.

### Primary consumers (typical)
- All ATAs (as a common governance substrate), Copilot/agents, CI validation, traceability auditors, DPP export and verification tooling, sim/test governance nodes (100+).

---

## 3) Partitioned Uncertainty Resolution Pathway (P1–P8)

Each partition corresponds to a dedicated folder. **Do not credit closure** unless the partition’s “Done” definition is satisfied.

### P1 — Work Breakdown & Ownership (Execution Closure)
- Folder: [01_WBS/](01_WBS/)  
  _Comment:_ Converts uncertainty into executable work packages (tasks, owners, inputs/outputs).

- WBS index: [K06 ATA 90 Work Breakdown](01_WBS/90_00_IDX_LC01_AMPEL360_SPACET_PLUS_k06-ata-90-workbreakdown_v01.md)  
  _Closes:_ “We don’t know what to do next / who owns it.”  
  _Done when:_ T001–T008 exist with owners, acceptance criteria, and artifact links.

- RACI (CSV): [RACI](01_WBS/90_00_MAT_LC06_AMPEL360_SPACET_PLUS_k06-ata-90-raci_v01.csv)  
  _Closes:_ Responsibility ambiguity (execution vs approval).  
  _Done when:_ CM approval path is explicit and accepted.

**Task stubs (minimum set — expanded for ATA 90):**
- T001: [SSOT source & ownership](01_WBS/90_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t001-ssot-source-ownership_v01.md)  
  _Comment:_ Declares SSOT locations for schemas/trace graph/model registry/DPP exports and change control authority.

- T002: [Identifier grammar](01_WBS/90_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t002-identifier-grammar_v01.md)  
  _Comment:_ Canonical ID grammar for schema IDs, trace IDs, wiring/signal IDs, model/dataset IDs, DPP pack IDs.

- T003: [Schema definition](01_WBS/90_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t003-schema-definition_v01.md)  
  _Comment:_ Defines the “meta-schemas”: registry schema, trace edge schema, provenance schema.

- T004: [Export publication](01_WBS/90_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t004-export-publication_v01.md)  
  _Comment:_ Defines deterministic generation of schema packs, trace packs, and DPP export packs.

- T005: [CI validation gates](01_WBS/90_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t005-ci-validation-gates_v01.md)  
  _Comment:_ Enforces ID uniqueness, schema versioning rules, trace-link integrity, provenance completeness.

- T006: [Baseline registry set](01_WBS/90_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t006-baseline-registry-set_v01.md)  
  _Comment:_ Frozen baseline of the schema registry + trace primitives for release milestones.

- T007: [Trace graph integrity checks](01_WBS/90_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t007-trace-graph-integrity-checks_v01.md)  
  _Comment:_ Prevents broken edges, orphan nodes, stale evidence references.

- T008: [Model/dataset governance alignment](01_WBS/90_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t008-model-dataset-governance-alignment_v01.md)  
  _Comment:_ Aligns model IDs, dataset IDs, feature schemas, and evaluation artifacts under K06 rules.

---

### P2 — IDs & Registry (Identity Closure)
- Folder: [02_IDS_REGISTRY/](02_IDS_REGISTRY/)  
  _Comment:_ Ensures every schema/trace primitive/wiring definition/model/dataset/export pack has a unique ID, owner, lifecycle state, and dedup policy.

- Standard (STD): [Identifier grammar](02_IDS_REGISTRY/90_00_STD_LC03_AMPEL360_SPACET_PLUS_meta-identifier-grammar_v01.md)  
  _Done when:_ Grammar is approved and referenced by schema + CI.

- Registry (TAB/CSV): [Schema registry](02_IDS_REGISTRY/90_00_TAB_LC03_AMPEL360_SPACET_PLUS_schema-registry_v01.csv)  
  _Done when:_ Central registry is SSOT; every schema/version is registered and referenced.

- Registry (TAB/CSV): [Trace primitives registry](02_IDS_REGISTRY/90_00_TAB_LC03_AMPEL360_SPACET_PLUS_trace-primitives-registry_v01.csv)  
  _Done when:_ Node/edge types and link semantics are registered and stable.

- Registry (TAB/CSV): [Model & dataset registry](02_IDS_REGISTRY/90_00_TAB_LC03_AMPEL360_SPACET_PLUS_model-dataset-registry_v01.csv)  
  _Done when:_ Models/datasets/feature sets/eval suites have canonical IDs and owners.

- Change log (LOG): [Registry change log](02_IDS_REGISTRY/90_00_LOG_LC03_AMPEL360_SPACET_PLUS_registry-change-log_v01.md)  
  _Done when:_ Every registry change references a decision (P7).

---

### P3 — Schema & Versioning (Semantic Closure)
- Folder: [03_SCHEMA/](03_SCHEMA/)  
  _Comment:_ Defines stable machine-readable meaning and compatibility rules for meta-schemas.

- Schema (SCH/JSON): [Schema registry schema](03_SCHEMA/90_00_SCH_LC03_AMPEL360_SPACET_PLUS_schema-registry-schema_v01.json)  
  _Done when:_ Validates the schema registry (P2) and is used by CI.

- Schema (SCH/JSON): [Trace edge schema](03_SCHEMA/90_00_SCH_LC03_AMPEL360_SPACET_PLUS_trace-edge-schema_v01.json)  
  _Done when:_ Validates trace links and edge semantics.

- Schema (SCH/JSON): [Provenance schema](03_SCHEMA/90_00_SCH_LC03_AMPEL360_SPACET_PLUS_provenance-schema_v01.json)  
  _Done when:_ Ensures all exports (including DPP packs) contain required provenance.

- Standard (STD): [Schema versioning policy](03_SCHEMA/90_00_STD_LC03_AMPEL360_SPACET_PLUS_schema-versioning-policy_v01.md)  
  _Done when:_ Compatibility and breaking-change rules exist and are enforced.

---

### P4 — Exports (Consumable Data Closure)
- Folder: [04_EXPORTS/](04_EXPORTS/)  
  _Comment:_ Reproducible schema packs, trace packs, wiring maps, and DPP-ready bundles.

- Baseline export (TAB/CSV): [Baseline schema registry export](04_EXPORTS/90_00_TAB_LC04_AMPEL360_SPACET_PLUS_baseline-schema-registry-export_v01.csv)  
  _Done when:_ Export is reproducible and validated.

- Baseline export (TAB/CSV): [Baseline trace pack export](04_EXPORTS/90_00_TAB_LC04_AMPEL360_SPACET_PLUS_baseline-trace-pack-export_v01.csv)  
  _Done when:_ Trace pack is reproducible and validated; references resolve.

- Manifest (RPT): [Export manifest](04_EXPORTS/90_00_RPT_LC04_AMPEL360_SPACET_PLUS_export-manifest_v01.md)  
  _Done when:_ Inputs/tools/versions are recorded; rebuild is deterministic.

- Diagram (DIA): [Trace graph map](04_EXPORTS/90_00_DIA_LC04_AMPEL360_SPACET_PLUS_trace-graph-map_v01.md)  
  _Done when:_ Diagram references match registries and exports.

---

### P5 — CI Gates (Enforcement Closure)
- Folder: [05_CI_GATES/](05_CI_GATES/)  
  _Comment:_ Governance enforcement for the entire program’s schemas/trace/DPP identity layer.

- Requirements (STD): [CI validation requirements](05_CI_GATES/90_00_STD_LC05_AMPEL360_SPACET_PLUS_ci-validation-requirements_v01.md)  
  _Done when:_ Rules map to checks; failures are actionable.

- Checklist (LOG): [CI checklist](05_CI_GATES/90_00_LOG_LC05_AMPEL360_SPACET_PLUS_ci-checklist_v01.md)  
  _Done when:_ Checklist matches CI outputs and reviewer expectations.

- Sample run (RPT): [CI validation sample run](05_CI_GATES/90_00_RPT_LC05_AMPEL360_SPACET_PLUS_ci-validation-sample-run_v01.md)  
  _Done when:_ Demonstrates representative pass/fail cases (broken trace edges, duplicate schema IDs, missing provenance).

---

### P6 — Evidence Pack (Proof Closure)
- Folder: [06_EVIDENCE/](06_EVIDENCE/)  
  _Comment:_ NKU credit requires reproducible evidence and stable links.

- Evidence pack index (IDX): [Evidence pack](06_EVIDENCE/90_00_IDX_LC06_AMPEL360_SPACET_PLUS_k06-ata-90-evidence-pack_v01.md)  
  _Done when:_ All required evidence is linked and current.

- Evidence links (TRC/CSV): [Evidence links register](06_EVIDENCE/90_00_TRC_LC06_AMPEL360_SPACET_PLUS_k06-ata-90-evidence-links_v01.csv)  
  _Done when:_ Each claim has an evidence link and status (OK/STALE/MISSING).

- NKU ledger (TAB/CSV): [NKU ledger](06_EVIDENCE/90_00_TAB_LC06_AMPEL360_SPACET_PLUS_k06-ata-90-nku-ledger_v01.csv)  
  _Done when:_ Partition scores are updated and backed by evidence + decision.

---

### P7 — Decisions & Approvals (Authority Closure)
- Folder: [07_DECISIONS/](07_DECISIONS/)  
  _Comment:_ Converts evidence into approved baseline outcomes for schema/trace/provenance rules.

- Decision minutes (MIN): [Decision minutes](07_DECISIONS/90_00_MIN_LC07_AMPEL360_SPACET_PLUS_k06-ata-90-decision-minutes_v01.md)  
  _Done when:_ Decision, rationale, dissent/risks are recorded.

- Approvals log (LOG): [Approvals log](07_DECISIONS/90_00_LOG_LC07_AMPEL360_SPACET_PLUS_k06-ata-90-approvals_v01.md)  
  _Done when:_ CM approval + any required sign-offs are referenced.

---

### P8 — Traceability & Adoption (Impact Closure)
- Folder: [08_TRACEABILITY/](08_TRACEABILITY/)  
  _Comment:_ Ensures all consumers adopt ATA 90 governance primitives (schemas/trace/provenance).

- Consumers (TRC/CSV): [Consumers list](08_TRACEABILITY/90_00_TRC_LC08_AMPEL360_SPACET_PLUS_k06-ata-90-consumers_v01.csv)  
  _Done when:_ Consumers are listed with interface/version and owner.

- Adoption status (RPT): [Adoption status](08_TRACEABILITY/90_00_RPT_LC08_AMPEL360_SPACET_PLUS_k06-ata-90-adoption-status_v01.md)  
  _Done when:_ Each consumer has status + remediation plan if blocked.

---

## 4) Cross-ATA Links (same Knot, coupled closures)

ATA 90 is the K06 “spine”; these couplings are mandatory.

- [ATA 00 — Program Governance](../ATA_00/)  
  _Comment:_ CM authority, naming/metadata standards, release gates.

- [ATA 91 — Schemas](../ATA_91/)  
  _Comment:_ Dedicated schema domain; must not diverge from ATA 90 meta-schema registry.

- [ATA 93 — Traceability Graph](../ATA_93/)  
  _Comment:_ Trace graph implementation; must align with trace edge schema and registries.

- [ATA 94 — DPP](../ATA_94/)  
  _Comment:_ DPP export packs; must comply with provenance schema and signed pack rules.

- [ATA 95 — SBOM / ModelBOM](../ATA_95/)  
  _Comment:_ Software/model supply chain; must reference schema IDs and registry entries.

- [ATA 98 — Signed Export Packs](../ATA_98/)  
  _Comment:_ Signing, hashing, and provenance enforcement.

- [ATA 99 — Master Registers](../ATA_99/)  
  _Comment:_ Consolidated registers and anti-duplication across the program.

**Sim/Test Coupling (100+):**
- [ATA 101](../ATA_101/), [ATA 107](../ATA_107/), [ATA 109](../ATA_109/)  
  _Comment:_ Sim/test evidence nodes must use the same IDs/schemas/trace semantics and TEKNIA packaging gates.

**Technology Coupling (20–79 where relevant):**
- [ATA 45](../ATA_45/) and [ATA 46](../ATA_46/)  
  _Comment:_ Interface/service catalogs should reference the same schema registry and trace primitives.

---

## 5) Control & Monitoring (NKU Values + TEKNIA Sharing Rules)

### 5.1 NKU Control Model
**Primary metric:** NKU Progress Score for K06/ATA90  
**Source of truth:** [NKU ledger](06_EVIDENCE/90_00_TAB_LC06_AMPEL360_SPACET_PLUS_k06-ata-90-nku-ledger_v01.csv)

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
| NKU ledger updates | AI + DATA | Per PR affecting K06/ATA90 | NKU ledger + evidence links | No score uplift without links |
| CI gate compliance | CM + Tooling | Per PR | CI gates + logs | Enforcement mechanism |
| Evidence completeness | SE + V&V | Weekly / per gate | Evidence pack index | Detect staleness |
| Decision capture | CM WG | At gate closure | Decisions + approvals | Required for closure |
| Adoption tracking | All consumer owners | Biweekly | Consumers + adoption status | Prevent “paper closure” |

### 5.3 Thresholds
- Green ≥ 0.80; Amber 0.50–0.79; Red < 0.50  
Hard blockers: missing P2/P3/P5 closure, missing P7 decision, stale evidence for any closed item.

### 5.4 TEKNIA Sharing Rules
TEKTOKs may be created only when:
- Evidence is reproducible (P6 complete)
- Decision exists (P7 complete, CM-approved)
- Dedup passes (SHA-256)
- NV threshold met (≥ 0.50 internal, ≥ 0.65 external recommended)

### 5.5 TEKNIA Packaging Requirements (mandatory metadata)
Any TEKTOK derived from ATA 90 closure must include:
- knot_id, ata, partitions_closed
- claim + scope
- evidence links + decision link
- hash_sha256 + dedup status
- nv + rationale
- sharing classification + redaction notes

### 5.6 Enforcement
CI should validate:
- NKU ledger integrity
- no-false-closure rule
- schema registry correctness (unique IDs, required fields)
- trace graph integrity (no broken edges/orphans)
- TEKNIA gate for “approved” TEKTOK status (NV + dedup)

---

## 6) Practical Notes (common failure modes)
- Do not accept “approved” schema/trace changes without a decision record (P7) and evidence links (P6).
- Ensure registries are not duplicated across folders; ATA 90 registries are authoritative unless explicitly delegated.
- Broken trace edges and missing provenance are immediate blockers for DPP and sim/test evidence claims.
