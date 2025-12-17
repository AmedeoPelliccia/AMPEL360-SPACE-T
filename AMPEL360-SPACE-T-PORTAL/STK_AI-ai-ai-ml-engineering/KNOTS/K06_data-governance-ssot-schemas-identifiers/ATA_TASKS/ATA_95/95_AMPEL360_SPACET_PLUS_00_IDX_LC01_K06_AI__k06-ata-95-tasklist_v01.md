---
title: "K06 ATA 95 — Partitioned Uncertainty Resolution Index"
type: IDX
variant: SPACET
status: Draft
knot_id: K06
ata: "95"
lc_or_subbucket: "LC01"
description: "GitHub-navigable hub for closing K06 (SSOT/Schemas/Identifiers) for ATA 95 (SBOM / ModelBOM / ML Asset Traceability) with NKU control and TEKNIA sharing rules."
---

# K06 — Data Governance (SSOT / Schemas / Identifiers)
## ATA 95 — Partitioned Uncertainty Resolution Index (IDX)

This file is the **single navigation hub** for all artifacts required to close **K06** for **ATA 95** (your domain for **SBOM, ModelBOM, and ML asset traceability**).  
NKU progress is credited only when each partition is closed with **evidence + approval**.

> ATA 95 operationalizes K06 for software and ML supply chain: if identifiers and schemas are inconsistent here, provenance claims become unverifiable and risk propagates into DPP exports.

---

## 1) Global Navigation (GitHub-navigable)

- Knot overview: [K06 overview](../../00_AMPEL360_SPACET_PLUS_00_IDX_LC01_K06_CM__k06-data-governance-ssot-schemas-identifiers_v01.md)  
  _Comment:_ Canonical K06 scope, impacted ATAs, closure criteria, and shared definitions.

- Portal index: [AMPEL360-SPACE-T-PORTAL index](../../../../../00_AMPEL360_SPACET_PLUS_00_IDX_LC01_K00_CM__stakeholder-entrypoints_v01.md)  
  _Comment:_ Global entry point; use it to navigate stakeholders and the knot portfolio.

- Stakeholder entrypoint (AI): [STK_AI entrypoint](../../../../00_AMPEL360_SPACET_PLUS_00_IDX_LC01_K00_AI__stakeholder-ai-entrypoint_v01.md)  
  _Comment:_ AI/ML execution lane; automation hooks and governance helpers.

- ATA 95 home (SBOM/ModelBOM): [AMPEL360_SPACE-T/N-NEURAL_NETWORKS/ATA 95](../../../../../../AMPEL360_SPACE-T/N-NEURAL_NETWORKS/ATA_95-SBOM-MODELBOM/)  
  _Comment:_ Intended authoritative location for ATA 95 outputs. If your folder name differs, update only this link target.

---

## 2) ATA 95 K06 Focus (what uncertainty we are closing)

### Uncertainty to Resolve (ATA-specific)
K06 within ATA 95 is the absence of a single governed SSOT for:
- **Software/ML identity:** canonical IDs for software components, packages, containers, libraries, toolchains, models, datasets.
- **BOM schemas:** stable schemas for SBOM and ModelBOM (including ML metadata: training data provenance, feature schema, evaluation suite).
- **Link semantics:** standardized links from SBOM/ModelBOM entries to source, build, test, evidence, and approvals.
- **Release provenance:** deterministic generation, hashing, signing, and verification of SBOM/ModelBOM packs.
- **Policy gates:** license policy, vulnerability policy, model risk policy (as metadata and CI checks).
- **Enforcement:** CI gates preventing uncontrolled changes and ensuring BOM-to-trace alignment (ATA 93) and DPP readiness (ATA 94).

### Primary consumers (typical)
- Software engineering, cybersecurity, certification evidence, release management, DPP export pipeline, sim/test governance nodes (100+), ops.

---

## 3) Partitioned Uncertainty Resolution Pathway (P1–P8)

Each partition corresponds to a dedicated folder. **Do not credit closure** unless the partition’s “Done” definition is satisfied.

### P1 — Work Breakdown & Ownership (Execution Closure)
- Folder: [01_WBS/](01_WBS/)  
  _Comment:_ Converts uncertainty into executable work packages (tasks, owners, inputs/outputs).

- WBS index: [K06 ATA 95 Work Breakdown](01_WBS/95_00_IDX_LC01_AMPEL360_SPACET_PLUS_k06-ata-95-workbreakdown_v01.md)  
  _Closes:_ “We don’t know what to do next / who owns it.”  
  _Done when:_ T001–T010 exist with owners, acceptance criteria, and artifact links.

- RACI (CSV): [RACI](01_WBS/95_00_MAT_LC06_AMPEL360_SPACET_PLUS_k06-ata-95-raci_v01.csv)  
  _Closes:_ Responsibility ambiguity (execution vs approval).  
  _Done when:_ CM approval path is explicit and accepted.

**Task stubs (minimum set — expanded for BOM domain):**
- T001: [SSOT source & ownership](01_WBS/95_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t001-ssot-source-ownership_v01.md)  
  _Comment:_ Declares authoritative sources for SBOM/ModelBOM content and ownership boundaries.

- T002: [Identifier grammar](01_WBS/95_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t002-identifier-grammar_v01.md)  
  _Comment:_ Canonical IDs for software components, build artifacts, models, datasets, and toolchains.

- T003: [SBOM schema definition](01_WBS/95_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t003-sbom-schema-definition_v01.md)  
  _Comment:_ Stabilizes SBOM semantics and required fields; aligns with ATA 91 schema rules.

- T004: [ModelBOM schema definition](01_WBS/95_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t004-modelbom-schema-definition_v01.md)  
  _Comment:_ Stabilizes ML asset semantics (model lineage, dataset provenance, evaluation suite, feature schema).

- T005: [Link semantics to trace graph](01_WBS/95_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t005-link-semantics-to-trace-graph_v01.md)  
  _Comment:_ Defines how BOM entries map to ATA 93 nodes/edges and evidence links.

- T006: [Policy gates](01_WBS/95_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t006-policy-gates_v01.md)  
  _Comment:_ License, vulnerability, and model-risk policy gating rules and evidence expectations.

- T007: [Export publication](01_WBS/95_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t007-export-publication_v01.md)  
  _Comment:_ Deterministic generation of SBOM/ModelBOM packs with manifests and checksums.

- T008: [CI validation gates](01_WBS/95_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t008-ci-validation-gates_v01.md)  
  _Comment:_ Enforces schema validity, registry completeness, policy checks, and trace alignment.

- T009: [Baseline BOM set](01_WBS/95_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t009-baseline-bom-set_v01.md)  
  _Comment:_ Frozen baseline SBOM/ModelBOM for a milestone release (referenced by DPP packs).

- T010: [Verification procedure](01_WBS/95_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t010-verification-procedure_v01.md)  
  _Comment:_ How consumers verify BOM authenticity, completeness, and policy status.

---

### P2 — IDs & Registry (Identity Closure)
- Folder: [02_IDS_REGISTRY/](02_IDS_REGISTRY/)  
  _Comment:_ Ensures every software component/model/dataset/toolchain artifact has a unique ID, owner, lifecycle state, and dedup policy.

- Standard (STD): [Identifier grammar](02_IDS_REGISTRY/95_00_STD_LC03_AMPEL360_SPACET_PLUS_bom-identifier-grammar_v01.md)  
  _Done when:_ Grammar is approved and referenced by export tooling + CI.

- Registry (TAB/CSV): [Software component registry](02_IDS_REGISTRY/95_00_TAB_LC03_AMPEL360_SPACET_PLUS_software-component-registry_v01.csv)  
  _Done when:_ Components have canonical IDs, owners, versions, and source references.

- Registry (TAB/CSV): [Model & dataset registry](02_IDS_REGISTRY/95_00_TAB_LC03_AMPEL360_SPACET_PLUS_model-dataset-registry_v01.csv)  
  _Done when:_ ML assets have canonical IDs, provenance pointers, and evaluation references.

- Registry (TAB/CSV): [Toolchain registry](02_IDS_REGISTRY/95_00_TAB_LC03_AMPEL360_SPACET_PLUS_toolchain-registry_v01.csv)  
  _Done when:_ Build and training toolchains are identified and versioned.

- Change log (LOG): [Registry change log](02_IDS_REGISTRY/95_00_LOG_LC03_AMPEL360_SPACET_PLUS_registry-change-log_v01.md)  
  _Done when:_ Every change references a decision (P7).

---

### P3 — Schema & Versioning (Semantic Closure)
- Folder: [03_SCHEMA/](03_SCHEMA/)  
  _Comment:_ Defines machine-readable schemas for SBOM/ModelBOM and compatibility rules.

- Schema (SCH/JSON): [SBOM schema](03_SCHEMA/95_00_SCH_LC03_AMPEL360_SPACET_PLUS_sbom-schema_v01.json)  
  _Done when:_ Validates SBOM exports and is used by CI.

- Schema (SCH/JSON): [ModelBOM schema](03_SCHEMA/95_00_SCH_LC03_AMPEL360_SPACET_PLUS_modelbom-schema_v01.json)  
  _Done when:_ Validates ModelBOM exports and is used by CI.

- Schema (SCH/JSON): [BOM manifest schema](03_SCHEMA/95_00_SCH_LC03_AMPEL360_SPACET_PLUS_bom-manifest-schema_v01.json)  
  _Done when:_ Validates provenance metadata, checksums, and policy results.

- Standard (STD): [Schema versioning policy](03_SCHEMA/95_00_STD_LC03_AMPEL360_SPACET_PLUS_schema-versioning-policy_v01.md)  
  _Done when:_ Compatibility/breaking-change rules exist and are enforced.

---

### P4 — Exports (Consumable Data Closure)
- Folder: [04_EXPORTS/](04_EXPORTS/)  
  _Comment:_ Deterministic BOM exports and audit-ready baselines.

- Baseline export (TAB/CSV): [Baseline SBOM export](04_EXPORTS/95_00_TAB_LC04_AMPEL360_SPACET_PLUS_baseline-sbom-export_v01.csv)  
  _Done when:_ Export is reproducible, validated, and milestone-referenced.

- Baseline export (TAB/CSV): [Baseline ModelBOM export](04_EXPORTS/95_00_TAB_LC04_AMPEL360_SPACET_PLUS_baseline-modelbom-export_v01.csv)  
  _Done when:_ Export is reproducible, validated, and milestone-referenced.

- Manifest (RPT): [Export manifest](04_EXPORTS/95_00_RPT_LC04_AMPEL360_SPACET_PLUS_export-manifest_v01.md)  
  _Done when:_ Inputs/tools/versions are recorded; rebuild is deterministic.

- Diagram (DIA): [BOM-to-trace map](04_EXPORTS/95_00_DIA_LC04_AMPEL360_SPACET_PLUS_bom-to-trace-map_v01.md)  
  _Done when:_ Diagram references match registry IDs and trace semantics (ATA 93).

---

### P5 — CI Gates (Enforcement Closure)
- Folder: [05_CI_GATES/](05_CI_GATES/)  
  _Comment:_ Blocks merges that break BOM validity, policy gates, or trace alignment.

- Requirements (STD): [CI validation requirements](05_CI_GATES/95_00_STD_LC05_AMPEL360_SPACET_PLUS_ci-validation-requirements_v01.md)  
  _Done when:_ Rules map to checks; failures are actionable.

- Checklist (LOG): [CI checklist](05_CI_GATES/95_00_LOG_LC05_AMPEL360_SPACET_PLUS_ci-checklist_v01.md)  
  _Done when:_ Checklist matches CI outputs and reviewer expectations.

- Sample run (RPT): [CI validation sample run](05_CI_GATES/95_00_RPT_LC05_AMPEL360_SPACET_PLUS_ci-validation-sample-run_v01.md)  
  _Done when:_ Demonstrates pass/fail cases (missing registry entry, license violation, vulnerability threshold breach, trace mismatch).

---

### P6 — Evidence Pack (Proof Closure)
- Folder: [06_EVIDENCE/](06_EVIDENCE/)  
  _Comment:_ NKU credit requires reproducible evidence and stable links (including policy results and signed packs).

- Evidence pack index (IDX): [Evidence pack](06_EVIDENCE/95_00_IDX_LC06_AMPEL360_SPACET_PLUS_k06-ata-95-evidence-pack_v01.md)  
  _Done when:_ All required evidence is linked and current.

- Evidence links (TRC/CSV): [Evidence links register](06_EVIDENCE/95_00_TRC_LC06_AMPEL360_SPACET_PLUS_k06-ata-95-evidence-links_v01.csv)  
  _Done when:_ Each claim has evidence links and status (OK/STALE/MISSING).

- NKU ledger (TAB/CSV): [NKU ledger](06_EVIDENCE/95_00_TAB_LC06_AMPEL360_SPACET_PLUS_k06-ata-95-nku-ledger_v01.csv)  
  _Done when:_ Partition scores are updated and backed by evidence + decision.

---

### P7 — Decisions & Approvals (Authority Closure)
- Folder: [07_DECISIONS/](07_DECISIONS/)  
  _Comment:_ Converts evidence into approved baseline outcomes for BOM governance and policy thresholds.

- Decision minutes (MIN): [Decision minutes](07_DECISIONS/95_00_MIN_LC07_AMPEL360_SPACET_PLUS_k06-ata-95-decision-minutes_v01.md)  
  _Done when:_ Decision, rationale, dissent/risks are recorded (including policy exceptions).

- Approvals log (LOG): [Approvals log](07_DECISIONS/95_00_LOG_LC07_AMPEL360_SPACET_PLUS_k06-ata-95-approvals_v01.md)  
  _Done when:_ CM approval + security/model governance sign-offs are referenced.

---

### P8 — Traceability & Adoption (Impact Closure)
- Folder: [08_TRACEABILITY/](08_TRACEABILITY/)  
  _Comment:_ Ensures BOM consumers adopt the SSOT and can verify authenticity and policy status.

- Consumers (TRC/CSV): [Consumers list](08_TRACEABILITY/95_00_TRC_LC08_AMPEL360_SPACET_PLUS_k06-ata-95-consumers_v01.csv)  
  _Done when:_ Consumers are listed with BOM version, verification method, and owner.

- Adoption status (RPT): [Adoption status](08_TRACEABILITY/95_00_RPT_LC08_AMPEL360_SPACET_PLUS_k06-ata-95-adoption-status_v01.md)  
  _Done when:_ Each consumer has status + remediation plan if blocked.

---

## 4) Cross-ATA Links (same Knot, coupled closures)

ATA 95 is a core downstream consumer of K06 primitives; these couplings are mandatory.

- [ATA 90 — Meta spine (NN / Schemas / Trace / DPP)](../ATA_90/)  
  _Comment:_ Provenance expectations and TEKNIA packaging gates.

- [ATA 91 — Schemas](../ATA_91/)  
  _Comment:_ SBOM/ModelBOM schemas and registries must align with canonical schema governance.

- [ATA 93 — Traceability Graph](../ATA_93/)  
  _Comment:_ BOM-to-trace mapping and evidence link semantics must be valid.

- [ATA 94 — DPP](../ATA_94/)  
  _Comment:_ DPP packs should reference baseline BOM exports and policy results where applicable.

- [ATA 98 — Signed Export Packs](../ATA_98/)  
  _Comment:_ Signing/hashing and verification primitives for released BOM packs.

- [ATA 99 — Master Registers](../ATA_99/)  
  _Comment:_ Consolidated registers and anti-duplication controls.

**Sim/Test Coupling (100+):**
- [ATA 101](../ATA_101/) / [ATA 107](../ATA_107/) / [ATA 109](../ATA_109/)  
  _Comment:_ Test evidence should reference BOM IDs and verify policy gates as part of the evidence chain.

---

## 5) Control & Monitoring (NKU Values + TEKNIA Sharing Rules)

### 5.1 NKU Control Model
**Primary metric:** NKU Progress Score for K06/ATA95  
**Source of truth:** [NKU ledger](06_EVIDENCE/95_00_TAB_LC06_AMPEL360_SPACET_PLUS_k06-ata-95-nku-ledger_v01.csv)

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
| NKU ledger updates | AI + DATA | Per PR affecting K06/ATA95 | NKU ledger + evidence links | No score uplift without links |
| CI gate compliance | CM + Tooling | Per PR | CI gates + logs | Enforcement mechanism |
| License & vuln policy results | Security + Tooling | Per PR + release | CI policy reports | Exceptions must be approved (P7) |
| Model risk policy results | Model Governance + Tooling | Per PR + release | CI policy reports | Exceptions must be approved (P7) |
| Evidence freshness | SE + V&V | Weekly / per gate | Evidence links register | Detect staleness |
| Decision capture | CM WG + Security/Model Gov | At gate closure | Decisions + approvals | Required for closure |
| Consumer verification | BOM consumers | Per release | Adoption status | Verify authenticity and policy status |

### 5.3 Thresholds
- Green ≥ 0.80; Amber 0.50–0.79; Red < 0.50  
Hard blockers: missing P2/P3/P5 closure, missing P7 decision, missing policy results for baseline exports, stale evidence for any closed item.

### 5.4 TEKNIA Sharing Rules
TEKTOKs may be created only when:
- Evidence is reproducible (P6 complete)
- Decision exists (P7 complete, CM-approved)
- Dedup passes (SHA-256)
- NV threshold met (≥ 0.50 internal, ≥ 0.65 external recommended)

### 5.5 TEKNIA Packaging Requirements (mandatory metadata)
Any TEKTOK derived from ATA 95 closure must include:
- knot_id, ata, partitions_closed
- sbom_id / modelbom_id + release_state
- schema_ids referenced + registry references
- trace_snapshot_id + evidence links
- hash_sha256 + signature metadata (if baseline)
- policy results summary + exceptions (if any)
- nv + rationale + sharing classification

### 5.6 Enforcement
CI should validate:
- SBOM/ModelBOM schema compliance + registry completeness
- uniqueness of component/model/dataset IDs
- policy thresholds (license/vuln/model risk) and exceptions workflow
- trace alignment (ATA 93) and DPP readiness (ATA 94)
- TEKNIA gate for “approved” TEKTOK status (NV + dedup)

---

## 6) Practical Notes (common failure modes)
- “SBOM exists” is not closure: it must be deterministic, policy-checked, trace-linked, and approved.
- Treat ModelBOM provenance as critical: dataset identity and evaluation suite links are frequent weak points.
- Prefer signed packs for baseline BOM releases; raw file paths drift and are not audit-grade.
```
