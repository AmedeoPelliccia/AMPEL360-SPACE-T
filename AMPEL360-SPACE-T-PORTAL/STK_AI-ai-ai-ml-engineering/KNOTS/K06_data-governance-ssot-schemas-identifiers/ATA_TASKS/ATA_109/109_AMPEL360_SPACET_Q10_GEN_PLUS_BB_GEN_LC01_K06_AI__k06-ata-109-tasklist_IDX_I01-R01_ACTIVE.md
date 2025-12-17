---
title: "K06 ATA 109 — Partitioned Uncertainty Resolution Index"
type: IDX
variant: SPACET
status: Draft
knot_id: K06
ata: "109"
lc_or_subbucket: "LC01"
description: "GitHub-navigable hub for closing K06 (SSOT/Schemas/Identifiers) for ATA 109 (100+ Simulation & Testing domain) with NKU control and TEKNIA sharing rules."
---

# K06 — Data Governance (SSOT / Schemas / Identifiers)
## ATA 109 — Partitioned Uncertainty Resolution Index (IDX)

This file is the **single navigation hub** for all artifacts required to close **K06** for **ATA 109** (in the **100+ Simulation & Testing** domain).  
NKU progress is credited only when each partition is closed with **evidence + approval**.

> Note: ATA 109 is treated here as a Sim/Test governance node consistent with your rule “100+ = simulations and testing”. Adjust the local ATA label if your internal register assigns a more specific title.

---

## 1) Global Navigation (GitHub-navigable)

- Knot overview: [K06 overview](../../00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_LC01_K06_CM__k06-data-governance-ssot-schemas-identifiers_I01-R01.md)  
  _Comment:_ Canonical K06 scope, impacted ATAs, closure criteria, and shared definitions.

- Portal index: [AMPEL360-SPACE-T-PORTAL index](../../../../../00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_LC01_K04_CM__stakeholder-entrypoints_I01-R01.md)  
  _Comment:_ Global entry point; use it to navigate stakeholders and the full knot portfolio.

- Stakeholder entrypoint (AI): [STK_AI entrypoint](../../../../00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_LC01_K04_AI__stakeholder-ai-entrypoint_I01-R01.md)  
  _Comment:_ AI/ML execution lane; includes automation hooks and governance helpers.

- ATA 109 home (T-SIMTEST): [AMPEL360_SPACE-T/T-SIMTEST/ATA 109](../../../../../../AMPEL360_SPACE-T/T-SIMTEST/ATA_109-SIMTEST/)  
  _Comment:_ Intended authoritative location for ATA 109 sim/test governance outputs. If your folder name differs, update only this link target.

---

## 2) Partitioned Uncertainty Resolution Pathway (P1–P8)

Each partition corresponds to a dedicated folder. **Do not credit closure** unless the partition’s “Done” definition is satisfied.

### P1 — Work Breakdown & Ownership (Execution Closure)
- Folder: [01_WBS/](01_WBS/)  
  _Comment:_ Converts uncertainty into executable work packages (tasks, owners, inputs/outputs).

- WBS index: [K06 ATA 109 Work Breakdown](01_WBS/00_00_IDX_LC01_AMPEL360_SPACET_PLUS_k06-ata-109-workbreakdown_I01-R01.md)  
  _Closes:_ “We don’t know what to do next / who owns it.”  
  _Done when:_ T001–T006 exist with owners, acceptance criteria, and artifact links.

- RACI (CSV): [RACI](01_WBS/00_00_MAT_LC06_AMPEL360_SPACET_PLUS_k06-ata-109-raci_I01-R01.csv)  
  _Closes:_ Responsibility ambiguity (execution vs approval).  
  _Done when:_ CM approval path is explicit and accepted by all contributors.

**Task stubs (minimum set):**
- T001: [SSOT source & ownership](01_WBS/00_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t001-ssot-source-ownership_I01-R01.md)  
  _Comment:_ Declares authoritative SSOT for sim/test runs and datasets (source of truth, owners, change control).

- T002: [Identifier grammar](01_WBS/00_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t002-identifier-grammar_I01-R01.md)  
  _Comment:_ Defines canonical IDs for test runs, simulations, datasets, configurations, and evidence packs.

- T003: [Schema definition](01_WBS/00_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t003-schema-definition_I01-R01.md)  
  _Comment:_ Stabilizes semantics for run metadata, configuration, results, and evidence relationships.

- T004: [Export publication](01_WBS/00_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t004-export-publication_I01-R01.md)  
  _Comment:_ Defines what consumers ingest (exports/manifests) and how reproduction is ensured.

- T005: [CI validation gates](01_WBS/00_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t005-ci-validation-gates_I01-R01.md)  
  _Comment:_ Turns governance rules into automated enforcement; prevents untraceable evidence.

- T006: [Baseline evidence set](01_WBS/00_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t006-baseline-evidence-set_I01-R01.md)  
  _Comment:_ Produces a frozen baseline set of sim/test evidence for certification-grade claims.

---

### P2 — IDs & Registry (Identity Closure)
- Folder: [02_IDS_REGISTRY/](02_IDS_REGISTRY/)  
  _Comment:_ Ensures every run/dataset/evidence item has a unique ID, owner, lifecycle state, and dedup policy.

- Standard (STD): [Identifier grammar](02_IDS_REGISTRY/00_00_STD_LC03_AMPEL360_SPACET_PLUS_simtest-identifier-grammar_I01-R01.md)  
  _Done when:_ Grammar is approved and referenced by schema + CI gates.

- Registry (TAB/CSV): [Sim/Test registry](02_IDS_REGISTRY/00_00_TAB_LC03_AMPEL360_SPACET_PLUS_simtest-registry_I01-R01.csv)  
  _Done when:_ Registry is SSOT (no duplicates), with owners/status and required metadata.

- Change log (LOG): [Registry change log](02_IDS_REGISTRY/00_00_LOG_LC03_AMPEL360_SPACET_PLUS_registry-change-log_I01-R01.md)  
  _Done when:_ Every change references a decision/change record (P7).

---

### P3 — Schema & Versioning (Semantic Closure)
- Folder: [03_SCHEMA/](03_SCHEMA/)  
  _Comment:_ Defines stable machine-readable meaning and compatibility rules for sim/test metadata and evidence graphs.

- Schema (SCH/JSON): [Sim/Test run schema](03_SCHEMA/00_00_SCH_LC03_AMPEL360_SPACET_PLUS_simtest-run-schema_I01-R01.json)  
  _Done when:_ Schema validates exports and is referenced by CI.

- Standard (STD): [Schema versioning policy](03_SCHEMA/00_00_STD_LC03_AMPEL360_SPACET_PLUS_schema-versioning-policy_I01-R01.md)  
  _Done when:_ Compatibility/breaking-change rules exist and are enforced.

- Units/Frames map (TAB/CSV): [Units/frames mapping](03_SCHEMA/00_00_TAB_LC03_AMPEL360_SPACET_PLUS_units-frames-mapping_I01-R01.csv)  
  _Done when:_ Every result field declares unit/frame/tolerance rule to prevent misinterpretation.

---

### P4 — Exports (Consumable Data Closure)
- Folder: [04_EXPORTS/](04_EXPORTS/)  
  _Comment:_ Provides reproducible exports/manifests for sim/test runs and evidence packs (consumable by downstream tooling and reviews).

- Baseline dataset (TAB/CSV): [Baseline run/evidence set](04_EXPORTS/00_00_TAB_LC04_AMPEL360_SPACET_PLUS_baseline-simtest-evidence-set_I01-R01.csv)  
  _Done when:_ Export is reproducible, validated, and release-referenced.

- Manifest (RPT): [Export manifest](04_EXPORTS/00_00_RPT_LC04_AMPEL360_SPACET_PLUS_export-manifest_I01-R01.md)  
  _Done when:_ Inputs/tools/versions are recorded; rebuild is deterministic.

- Diagram (DIA): [Evidence relationship map](04_EXPORTS/00_00_DIA_LC04_AMPEL360_SPACET_PLUS_evidence-graph-map_I01-R01.md)  
  _Done when:_ Diagram references match registry IDs and baseline export.

---

### P5 — CI Gates (Enforcement Closure)
- Folder: [05_CI_GATES/](05_CI_GATES/)  
  _Comment:_ Makes governance non-optional; blocks “evidence without provenance”.

- Requirements (STD): [CI validation requirements](05_CI_GATES/00_00_STD_LC05_AMPEL360_SPACET_PLUS_ci-validation-requirements_I01-R01.md)  
  _Done when:_ Rules map to checks; failures are actionable.

- Checklist (LOG): [CI checklist](05_CI_GATES/00_00_LOG_LC05_AMPEL360_SPACET_PLUS_ci-checklist_I01-R01.md)  
  _Done when:_ Checklist matches CI outputs and reviewer expectations.

- Sample run (RPT): [CI validation sample run](05_CI_GATES/00_00_RPT_LC05_AMPEL360_SPACET_PLUS_ci-validation-sample-run_I01-R01.md)  
  _Done when:_ Demonstrates representative pass/fail cases.

---

### P6 — Evidence Pack (Proof Closure)
- Folder: [06_EVIDENCE/](06_EVIDENCE/)  
  _Comment:_ NKU credit requires reproducible evidence and stable links, not narrative.

- Evidence pack index (IDX): [Evidence pack](06_EVIDENCE/00_00_IDX_LC06_AMPEL360_SPACET_PLUS_k06-ata-109-evidence-pack_I01-R01.md)  
  _Done when:_ All required evidence is linked and current.

- Evidence links (TRC/CSV): [Evidence links register](06_EVIDENCE/00_00_TRC_LC06_AMPEL360_SPACET_PLUS_k06-ata-109-evidence-links_I01-R01.csv)  
  _Done when:_ Each claim has an evidence link and status (OK/STALE/MISSING).

- NKU ledger (TAB/CSV): [NKU ledger](06_EVIDENCE/00_00_TAB_LC06_AMPEL360_SPACET_PLUS_k06-ata-109-nku-ledger_I01-R01.csv)  
  _Done when:_ Partition scores are updated and backed by evidence + decision.

---

### P7 — Decisions & Approvals (Authority Closure)
- Folder: [07_DECISIONS/](07_DECISIONS/)  
  _Comment:_ Converts evidence into an approved baseline outcome.

- Decision minutes (MIN): [Decision minutes](07_DECISIONS/00_00_MIN_LC07_AMPEL360_SPACET_PLUS_k06-ata-109-decision-minutes_I01-R01.md)  
  _Done when:_ Decision, rationale, dissent/risks are recorded.

- Approvals log (LOG): [Approvals log](07_DECISIONS/00_00_LOG_LC07_AMPEL360_SPACET_PLUS_k06-ata-109-approvals_I01-R01.md)  
  _Done when:_ CM approval + any required sign-offs are referenced.

---

### P8 — Traceability & Adoption (Impact Closure)
- Folder: [08_TRACEABILITY/](08_TRACEABILITY/)  
  _Comment:_ Ensures consumers adopt the SSOT; prevents “closed on paper”.

- Consumers (TRC/CSV): [Consumers list](08_TRACEABILITY/00_00_TRC_LC08_AMPEL360_SPACET_PLUS_k06-ata-109-consumers_I01-R01.csv)  
  _Done when:_ Consumers are listed with interface/version and owner.

- Adoption status (RPT): [Adoption status](08_TRACEABILITY/00_00_RPT_LC08_AMPEL360_SPACET_PLUS_k06-ata-109-adoption-status_I01-R01.md)  
  _Done when:_ Each consumer has status + remediation plan if blocked.

---

## 3) Cross-ATA Links (same Knot, different ATA folders)

- [ATA 00 — Program Governance](../ATA_00/)  
  _Comment:_ Defines naming/metadata/registry authority; blocks false closure if missing.

- [ATA 06 — Dimensions & Areas](../ATA_06/)  
  _Comment:_ Geometry/envelope SSOT; feeds infrastructure and integration boundaries.

- [ATA 91 — Schemas](../ATA_91/)  
  _Comment:_ Provides canonical schema governance and validation primitives.

- [ATA 93 — Traceability Graph](../ATA_93/)  
  _Comment:_ Enables evidence trace from IDs → schema → export → decision.

- [ATA 94 — DPP](../ATA_94/)  
  _Comment:_ Ensures governance supports DPP provenance/exports.

- [ATA 95 — SBOM / ModelBOM](../ATA_95/)  
  _Comment:_ Ensures governance supports software/model supply chain trace.

- [ATA 98 — Signed Export Packs](../ATA_98/)  
  _Comment:_ Provides signed, auditable export packaging and provenance enforcement.

- [ATA 99 — Master Registers](../ATA_99/)  
  _Comment:_ Provides consolidated registers and anti-duplication mechanisms.

---

## 4) Control & Monitoring (NKU Values + TEKNIA Sharing Rules)

### 4.1 NKU Control Model
**Primary metric:** NKU Progress Score for K06/ATA109  
**Source of truth:** [NKU ledger](06_EVIDENCE/00_00_TAB_LC06_AMPEL360_SPACET_PLUS_k06-ata-109-nku-ledger_I01-R01.csv)

**Scoring:**
- `score ∈ {0, 0.5, 1.0}`
- **NKU Score** = `Σ(weight × score)` across partitions P1..P8

**No-false-closure (mandatory):**
- `score = 1.0` requires:
  - evidence link(s) in `06_EVIDENCE/...evidence-links...csv`, and
  - decision reference in `07_DECISIONS/...decision-minutes...md`

### 4.2 Monitoring Cadence
| Control Item | Owner | Frequency | Source | Comment |
|---|---|---:|---|---|
| NKU ledger updates | AI + DATA | Per PR | NKU ledger + evidence links | No score uplift without links |
| CI gate compliance | CM + Tooling | Per PR | CI gates + logs | Enforcement |
| Evidence completeness | SE + TEST | Weekly / per gate | Evidence pack index | Detect staleness |
| Decision capture | CM WG | At gate closure | Decisions + approvals | Required for closure |
| Adoption tracking | TEST + SIM owners | Biweekly | Consumers + adoption status | Avoid “paper closure” |

### 4.3 Thresholds
- Green ≥ 0.80; Amber 0.50–0.79; Red < 0.50  
Hard blockers: missing P2/P3/P5 closure, missing P7 decision, stale evidence for any closed item.

### 4.4 TEKNIA Sharing Rules
TEKTOKs may be created only when:
- Evidence is reproducible (P6 complete)
- Decision exists (P7 complete, CM-approved)
- Dedup passes (SHA-256)
- NV threshold met (≥ 0.50 internal, ≥ 0.65 external recommended)

### 4.5 Enforcement
CI should validate NKU ledger integrity and block false closure and “approved” TEKTOKs without NV+dedup compliance.

---

## 5) Practical Notes
- Do not accept “released sim/test evidence” without schema validation (P3) and CI enforcement (P5).
- Do not credit NKU closure without decision minutes (P7) and an evidence pack (P6).
- Treat run configuration and environment capture as first-class governance objects; irreproducibility starts here.
```
