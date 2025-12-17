---
title: "K06 ATA 93 — Partitioned Uncertainty Resolution Index"
type: IDX
variant: SPACET
status: Draft
knot_id: K06
ata: "93"
lc_or_subbucket: "LC01"
description: "GitHub-navigable hub for closing K06 (SSOT/Schemas/Identifiers) for ATA 93 (Traceability Graph & Evidence Link Semantics) with NKU control and TEKNIA sharing rules."
---

# K06 — Data Governance (SSOT / Schemas / Identifiers)
## ATA 93 — Partitioned Uncertainty Resolution Index (IDX)

This file is the **single navigation hub** for all artifacts required to close **K06** for **ATA 93** (your domain for **Traceability Graph and Evidence Link Semantics**).  
NKU progress is credited only when each partition is closed with **evidence + approval**.

> ATA 93 is where K06 becomes operational: if trace edges are ambiguous or broken, K06 cannot be closed program-wide.

---

## 1) Global Navigation (GitHub-navigable)

- Knot overview: [K06 overview](../../../../../STK_DATA-data-data-governance/KNOTS/K06_data-governance-ssot-schemas-identifiers/00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_LC01_K06_DATA__k06-data-governance-ssot-schemas-identifiers_IDX_I01-R01_ACTIVE.md)  
  _Comment:_ Canonical K06 scope, impacted ATAs, closure criteria, shared definitions.

- Portal index: [AMPEL360-SPACE-T-PORTAL index](../../../../../00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_LC01_K04_CM__stakeholder-entrypoints_IDX_I01-R01_ACTIVE.md)  
  _Comment:_ Global entry point; use it to navigate stakeholders and the knot portfolio.

- Stakeholder entrypoint (AI): [STK_AI entrypoint](../../../../00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_LC01_K11_AI__stakeholder-ai-entrypoint_IDX_I01-R01_ACTIVE.md)  
  _Comment:_ AI/ML execution lane; automation hooks and governance helpers.

- ATA 93 home (Traceability): [AMPEL360_SPACE-T/N-NEURAL_NETWORKS/ATA 93](../../../../../../AMPEL360_SPACE-T/N-NEURAL_NETWORKS/ATA_93-TRACEABILITY-GRAPH/)  
  _Comment:_ Intended authoritative location for ATA 93 outputs. If your folder name differs, update only this link target.

---

## 2) ATA 93 K06 Focus (what uncertainty we are closing)

### Uncertainty to Resolve (ATA-specific)
K06 within ATA 93 is the absence of a single governed SSOT for:
- **Trace node identity:** canonical IDs for artifacts, requirements, hazards, tests, datasets, models, decisions.
- **Trace edge semantics:** standardized edge types (e.g., *derives*, *verifies*, *mitigates*, *implements*, *depends-on*, *evidenced-by*).
- **Evidence link rules:** how links point to files, commits, releases, signed packs; staleness detection rules.
- **Graph integrity:** prevention of orphan nodes, broken edges, cycles (where prohibited), and duplicate identities.
- **Publication:** deterministic export of trace graphs for audits, reviews, and DPP packs.
- **Enforcement:** CI gates that block merges when trace integrity breaks.

### Primary consumers (typical)
- Configuration management, safety/certification evidence, DPP exports, CI validation, sim/test evidence nodes (100+), agent automation.

---

## 3) Partitioned Uncertainty Resolution Pathway (P1–P8)

Each partition corresponds to a dedicated folder. **Do not credit closure** unless the partition’s “Done” definition is satisfied.

### P1 — Work Breakdown & Ownership (Execution Closure)
- Folder: [01_WBS/](01_WBS/)  
  _Comment:_ Converts uncertainty into executable work packages (tasks, owners, inputs/outputs).

- WBS index: [K06 ATA 93 Work Breakdown](01_WBS/93_00_IDX_LC01_AMPEL360_SPACET_PLUS_k06-ata-93-workbreakdown_I01-R01.md)  
  _Closes:_ “We don’t know what to do next / who owns it.”  
  _Done when:_ T001–T009 exist with owners, acceptance criteria, and artifact links.

- RACI (CSV): [RACI](01_WBS/93_00_MAT_LC06_AMPEL360_SPACET_PLUS_k06-ata-93-raci_I01-R01.csv)  
  _Closes:_ Responsibility ambiguity (execution vs approval).  
  _Done when:_ CM approval path is explicit and accepted.

**Task stubs (minimum set — expanded for trace graph domain):**
- T001: [SSOT source & ownership](01_WBS/93_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t001-ssot-source-ownership_I01-R01.md)  
  _Comment:_ Declares SSOT for trace graph store, link conventions, and authority for edge semantics.

- T002: [Identifier grammar](01_WBS/93_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t002-identifier-grammar_I01-R01.md)  
  _Comment:_ Canonical IDs for nodes/edges, including stable URI-like references to repo artifacts.

- T003: [Edge semantics standard](01_WBS/93_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t003-edge-semantics-standard_I01-R01.md)  
  _Comment:_ Defines allowed edge types, directionality, and constraints (what can link to what).

- T004: [Evidence link standard](01_WBS/93_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t004-evidence-link-standard_I01-R01.md)  
  _Comment:_ Defines link targets (path/commit/tag/signed pack), and how staleness is detected.

- T005: [Graph integrity rules](01_WBS/93_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t005-graph-integrity-rules_I01-R01.md)  
  _Comment:_ Orphans, duplicates, prohibited cycles, minimum required edges for closure.

- T006: [Export publication](01_WBS/93_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t006-export-publication_I01-R01.md)  
  _Comment:_ Deterministic trace graph export (CSV/JSON) for audits and downstream consumption.

- T007: [CI validation gates](01_WBS/93_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t007-ci-validation-gates_I01-R01.md)  
  _Comment:_ Enforces trace integrity and evidence link rules in PRs.

- T008: [Cross-ATA adoption plan](01_WBS/93_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t008-cross-ata-adoption-plan_I01-R01.md)  
  _Comment:_ Onboarding checklist for ATAs to conform to trace rules.

- T009: [Baseline trace snapshot](01_WBS/93_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t009-baseline-trace-snapshot_I01-R01.md)  
  _Comment:_ Frozen snapshot for a milestone; referenced by DPP packs and certification evidence.

---

### P2 — IDs & Registry (Identity Closure)
- Folder: [02_IDS_REGISTRY/](02_IDS_REGISTRY/)  
  _Comment:_ Ensures trace node and edge identifiers are unique, owned, and discoverable.

- Standard (STD): [Identifier grammar](02_IDS_REGISTRY/93_00_STD_LC03_AMPEL360_SPACET_PLUS_trace-identifier-grammar_I01-R01.md)  
  _Done when:_ Grammar is approved and referenced by schema + CI.

- Registry (TAB/CSV): [Trace node registry](02_IDS_REGISTRY/93_00_TAB_LC03_AMPEL360_SPACET_PLUS_trace-node-registry_I01-R01.csv)  
  _Done when:_ Nodes are uniquely identified and mapped to repo artifacts.

- Registry (TAB/CSV): [Trace edge registry](02_IDS_REGISTRY/93_00_TAB_LC03_AMPEL360_SPACET_PLUS_trace-edge-registry_I01-R01.csv)  
  _Done when:_ Edge types are enumerated with constraints and owners.

- Change log (LOG): [Registry change log](02_IDS_REGISTRY/93_00_LOG_LC03_AMPEL360_SPACET_PLUS_registry-change-log_I01-R01.md)  
  _Done when:_ Every change references a decision (P7).

---

### P3 — Schema & Versioning (Semantic Closure)
- Folder: [03_SCHEMA/](03_SCHEMA/)  
  _Comment:_ Defines machine-readable schemas for trace graphs and evidence links.

- Schema (SCH/JSON): [Trace graph schema](03_SCHEMA/93_00_SCH_LC03_AMPEL360_SPACET_PLUS_trace-graph-schema_I01-R01.json)  
  _Done when:_ Validates exported graphs and is used by CI.

- Schema (SCH/JSON): [Evidence link schema](03_SCHEMA/93_00_SCH_LC03_AMPEL360_SPACET_PLUS_evidence-link-schema_I01-R01.json)  
  _Done when:_ Validates link targets and metadata (commit/tag/hash/classification).

- Standard (STD): [Schema versioning policy](03_SCHEMA/93_00_STD_LC03_AMPEL360_SPACET_PLUS_schema-versioning-policy_I01-R01.md)  
  _Done when:_ Compatibility and breaking-change rules exist and are enforced.

---

### P4 — Exports (Consumable Data Closure)
- Folder: [04_EXPORTS/](04_EXPORTS/)  
  _Comment:_ Deterministic graph exports and audit-ready snapshots.

- Baseline export (TAB/CSV): [Baseline trace graph export](04_EXPORTS/93_00_TAB_LC04_AMPEL360_SPACET_PLUS_baseline-trace-graph-export_I01-R01.csv)  
  _Done when:_ Export is reproducible, validated, and milestone-referenced.

- Manifest (RPT): [Export manifest](04_EXPORTS/93_00_RPT_LC04_AMPEL360_SPACET_PLUS_export-manifest_I01-R01.md)  
  _Done when:_ Inputs/tools/versions are recorded; rebuild is deterministic.

- Diagram (DIA): [Trace graph map](04_EXPORTS/93_00_DIA_LC04_AMPEL360_SPACET_PLUS_trace-graph-map_I01-R01.md)  
  _Done when:_ Diagram references match registries and exports.

---

### P5 — CI Gates (Enforcement Closure)
- Folder: [05_CI_GATES/](05_CI_GATES/)  
  _Comment:_ Blocks merges that break trace integrity or evidence rules.

- Requirements (STD): [CI validation requirements](05_CI_GATES/93_00_STD_LC05_AMPEL360_SPACET_PLUS_ci-validation-requirements_I01-R01.md)  
  _Done when:_ Rules map to checks; failures are actionable.

- Checklist (LOG): [CI checklist](05_CI_GATES/93_00_LOG_LC05_AMPEL360_SPACET_PLUS_ci-checklist_I01-R01.md)  
  _Done when:_ Checklist matches CI outputs and reviewer expectations.

- Sample run (RPT): [CI validation sample run](05_CI_GATES/93_00_RPT_LC05_AMPEL360_SPACET_PLUS_ci-validation-sample-run_I01-R01.md)  
  _Done when:_ Demonstrates representative pass/fail cases (broken link, orphan node, invalid edge type).

---

### P6 — Evidence Pack (Proof Closure)
- Folder: [06_EVIDENCE/](06_EVIDENCE/)  
  _Comment:_ NKU credit requires reproducible evidence and stable links.

- Evidence pack index (IDX): [Evidence pack](06_EVIDENCE/93_00_IDX_LC06_AMPEL360_SPACET_PLUS_k06-ata-93-evidence-pack_I01-R01.md)  
  _Done when:_ All required evidence is linked and current.

- Evidence links (TRC/CSV): [Evidence links register](06_EVIDENCE/93_00_TRC_LC06_AMPEL360_SPACET_PLUS_k06-ata-93-evidence-links_I01-R01.csv)  
  _Done when:_ Each claim has evidence links and status (OK/STALE/MISSING).

- NKU ledger (TAB/CSV): [NKU ledger](06_EVIDENCE/93_00_TAB_LC06_AMPEL360_SPACET_PLUS_k06-ata-93-nku-ledger_I01-R01.csv)  
  _Done when:_ Partition scores are updated and backed by evidence + decision.

---

### P7 — Decisions & Approvals (Authority Closure)
- Folder: [07_DECISIONS/](07_DECISIONS/)  
  _Comment:_ Converts evidence into approved baseline outcomes for trace semantics.

- Decision minutes (MIN): [Decision minutes](07_DECISIONS/93_00_MIN_LC07_AMPEL360_SPACET_PLUS_k06-ata-93-decision-minutes_I01-R01.md)  
  _Done when:_ Decision, rationale, dissent/risks are recorded.

- Approvals log (LOG): [Approvals log](07_DECISIONS/93_00_LOG_LC07_AMPEL360_SPACET_PLUS_k06-ata-93-approvals_I01-R01.md)  
  _Done when:_ CM approval + trace authority sign-offs are referenced.

---

### P8 — Traceability & Adoption (Impact Closure)
- Folder: [08_TRACEABILITY/](08_TRACEABILITY/)  
  _Comment:_ Ensures every consumer adopts the trace rules; prevents “shadow traces”.

- Consumers (TRC/CSV): [Consumers list](08_TRACEABILITY/93_00_TRC_LC08_AMPEL360_SPACET_PLUS_k06-ata-93-consumers_I01-R01.csv)  
  _Done when:_ Consumers are listed with interface/version and owner.

- Adoption status (RPT): [Adoption status](08_TRACEABILITY/93_00_RPT_LC08_AMPEL360_SPACET_PLUS_k06-ata-93-adoption-status_I01-R01.md)  
  _Done when:_ Each consumer has status + remediation plan if blocked.

---

## 4) Cross-ATA Links (same Knot, coupled closures)

ATA 93 is a cross-ATA dependency. These couplings are mandatory.

- [ATA 90 — NN / Schemas / DPP spine](../ATA_90/)  
  _Comment:_ Meta-registry, provenance expectations, TEKNIA packaging gates.

- [ATA 91 — Schemas](../ATA_91/)  
  _Comment:_ Edge and evidence schemas must be defined and versioned consistently.

- [ATA 94 — DPP](../ATA_94/)  
  _Comment:_ DPP export packs must reference trace graph snapshots and evidence links.

- [ATA 95 — SBOM / ModelBOM](../ATA_95/)  
  _Comment:_ Supply-chain trace links must conform to edge semantics and evidence rules.

- [ATA 98 — Signed Export Packs](../../../../../STK_DATA-data-data-governance/KNOTS/K08_dpp-sbom-provenance-scope/ATA_TASKS/ATA_98)  
  _Comment:_ Signed packs are the preferred evidence-link target for “released” states.

- [ATA 99 — Master Registers](../ATA_99/)  
  _Comment:_ Consolidated registers and anti-duplication controls.

**Sim/Test Coupling (100+):**
- [ATA 101](../ATA_101/), [ATA 107](../ATA_107/), [ATA 109](../ATA_109/)  
  _Comment:_ Sim/test evidence nodes must export trace edges and evidence links that validate under ATA 93 schemas.

---

## 5) Control & Monitoring (NKU Values + TEKNIA Sharing Rules)

### 5.1 NKU Control Model
**Primary metric:** NKU Progress Score for K06/ATA93  
**Source of truth:** [NKU ledger](06_EVIDENCE/93_00_TAB_LC06_AMPEL360_SPACET_PLUS_k06-ata-93-nku-ledger_I01-R01.csv)

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
| NKU ledger updates | AI + DATA | Per PR affecting K06/ATA93 | NKU ledger + evidence links | No score uplift without links |
| CI gate compliance | CM + Tooling | Per PR | CI gates + logs | Enforcement mechanism |
| Graph integrity | Trace Authority + Tooling | Per PR + weekly sweep | CI outputs + integrity reports | Orphans/broken edges are blockers |
| Evidence freshness | SE + V&V | Weekly / per gate | Evidence links register | Detect staleness |
| Decision capture | CM WG + Trace Authority | At gate closure | Decisions + approvals | Required for closure |
| Adoption tracking | Consumer owners | Biweekly | Consumers + adoption status | Prevent shadow traces |

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
CI should validate:
- trace graph schema compliance
- link target validity (path/commit/tag/signed pack) and required metadata
- graph integrity constraints (no broken edges/orphans)
- TEKNIA gate for “approved” TEKTOK status (NV + dedup)

---

## 6) Practical Notes (common failure modes)
- If a consumer cannot ingest the trace export deterministically, K06 cannot be considered closed.
- Prefer signed export packs as evidence targets for released states; raw file paths drift.
- Avoid ambiguous edge types; if a new edge type is needed, register it (P2) and define semantics (P3) before use.
```
