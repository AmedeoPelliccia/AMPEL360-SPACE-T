---
title: "K06 ATA 91 — Partitioned Uncertainty Resolution Index"
type: IDX
variant: SPACET
status: Draft
knot_id: K06
ata: "91"
lc_or_subbucket: "LC01"
description: "GitHub-navigable hub for closing K06 (SSOT/Schemas/Identifiers) for ATA 91 (Schemas & Canonical Data Models) with NKU control and TEKNIA sharing rules."
---

# K06 — Data Governance (SSOT / Schemas / Identifiers)
## ATA 91 — Partitioned Uncertainty Resolution Index (IDX)

This file is the **single navigation hub** for all artifacts required to close **K06** for **ATA 91** (your domain for **Schemas and Canonical Data Models**).  
NKU progress is credited only when each partition is closed with **evidence + approval**.

> ATA 91 is the canonical “schema engine room” for Space-T. This index is intentionally strict on schema identity, versioning, compatibility, and CI validation.

---

## 1) Global Navigation (GitHub-navigable)

- Knot overview: [K06 overview](../../../../../STK_DATA-data-data-governance/KNOTS/K06_data-governance-ssot-schemas-identifiers/00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_LC01_K06_DATA__k06-data-governance-ssot-schemas-identifiers_IDX_I01-R01_ACTIVE.md)  
  _Comment:_ Canonical K06 scope, impacted ATAs, closure criteria, and shared definitions.

- Portal index: [AMPEL360-SPACE-T-PORTAL index](../../../../../00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_LC01_K04_CM__stakeholder-entrypoints_IDX_I01-R01_ACTIVE.md)  
  _Comment:_ Global entry point; use it to navigate stakeholders and the knot portfolio.

- Stakeholder entrypoint (AI): [STK_AI entrypoint](../../../../00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_LC01_K11_AI__stakeholder-ai-entrypoint_IDX_I01-R01_ACTIVE.md)  
  _Comment:_ AI/ML execution lane; automation hooks and governance helpers.

- ATA 91 home (Schemas): [AMPEL360_SPACE-T/N-NEURAL_NETWORKS/ATA 91](../../../../../../AMPEL360_SPACE-T/N-NEURAL_NETWORKS/ATA_91-SCHEMAS/)  
  _Comment:_ Intended authoritative location for ATA 91 schema governance outputs. If your folder name differs, update only this link target.

---

## 2) ATA 91 K06 Focus (what uncertainty we are closing)

### Uncertainty to Resolve (ATA-specific)
K06 within ATA 91 is the absence of a single governed SSOT for:
- **Schema registry:** canonical IDs, owners, lifecycle status, and discovery metadata for all schemas.
- **Canonical data models:** shared definitions for entities/fields/enums used cross-ATA.
- **Versioning and compatibility:** strict rules for breaking changes, deprecations, and migration guidance.
- **Validation and tooling:** schema validation, linting, and packaging (CI gates).
- **Publication and consumption:** deterministic export packs and references that downstream ATAs can rely on.
- **Trace semantics alignment:** schemas must integrate with traceability primitives (ATA 93) and DPP packs (ATA 94).

### Primary consumers (typical)
- All ATAs (as schema consumers), traceability tooling, DPP export tooling, sim/test governance nodes (100+), and agent automation.

---

## 3) Partitioned Uncertainty Resolution Pathway (P1–P8)

Each partition corresponds to a dedicated folder. **Do not credit closure** unless the partition’s “Done” definition is satisfied.

### P1 — Work Breakdown & Ownership (Execution Closure)
- Folder: [01_WBS/](01_WBS/)  
  _Comment:_ Converts uncertainty into executable work packages (tasks, owners, inputs/outputs).

- WBS index: [K06 ATA 91 Work Breakdown](01_WBS/91_00_IDX_LC01_AMPEL360_SPACET_PLUS_k06-ata-91-workbreakdown_I01-R01.md)  
  _Closes:_ “We don’t know what to do next / who owns it.”  
  _Done when:_ T001–T008 exist with owners, acceptance criteria, and artifact links.

- RACI (CSV): [RACI](01_WBS/91_00_MAT_LC06_AMPEL360_SPACET_PLUS_k06-ata-91-raci_I01-R01.csv)  
  _Closes:_ Responsibility ambiguity (execution vs approval).  
  _Done when:_ CM approval path is explicit and accepted.

**Task stubs (minimum set — expanded for schema domain):**
- T001: [SSOT source & ownership](01_WBS/91_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t001-ssot-source-ownership_I01-R01.md)  
  _Comment:_ Declares SSOT locations for schema registry and canonical models; sets change control authority.

- T002: [Identifier grammar](01_WBS/91_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t002-identifier-grammar_I01-R01.md)  
  _Comment:_ Canonical ID grammar for schema IDs, versions, namespaces, and packages.

- T003: [Schema registry definition](01_WBS/91_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t003-schema-registry-definition_I01-R01.md)  
  _Comment:_ Defines required fields, discovery metadata, and registry workflows.

- T004: [Versioning & compatibility policy](01_WBS/91_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t004-versioning-compatibility-policy_I01-R01.md)  
  _Comment:_ Defines breaking/nonbreaking rules, deprecation windows, and migration obligations.

- T005: [CI validation gates](01_WBS/91_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t005-ci-validation-gates_I01-R01.md)  
  _Comment:_ Enforces schema validity, registry completeness, and versioning compliance.

- T006: [Schema pack export](01_WBS/91_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t006-schema-pack-export_I01-R01.md)  
  _Comment:_ Defines deterministic packaging and publication of schema packs (for consumption and evidence).

- T007: [Canonical model alignment](01_WBS/91_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t007-canonical-model-alignment_I01-R01.md)  
  _Comment:_ Ensures shared entity definitions remain consistent across ATAs.

- T008: [Schema consumer onboarding](01_WBS/91_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t008-schema-consumer-onboarding_I01-R01.md)  
  _Comment:_ Defines adoption pathway for ATAs; blocks “shadow schemas”.

---

### P2 — IDs & Registry (Identity Closure)
- Folder: [02_IDS_REGISTRY/](02_IDS_REGISTRY/)  
  _Comment:_ Ensures every schema/canonical model/package has a unique ID, owner, lifecycle state, and dedup policy.

- Standard (STD): [Identifier grammar](02_IDS_REGISTRY/91_00_STD_LC03_AMPEL360_SPACET_PLUS_schema-identifier-grammar_I01-R01.md)  
  _Done when:_ Grammar is approved and referenced by CI and all schema documents.

- Registry (TAB/CSV): [Schema registry](02_IDS_REGISTRY/91_00_TAB_LC03_AMPEL360_SPACET_PLUS_schema-registry_I01-R01.csv)  
  _Done when:_ Registry is SSOT (no duplicates), with owners/status and required metadata.

- Registry (TAB/CSV): [Canonical model registry](02_IDS_REGISTRY/91_00_TAB_LC03_AMPEL360_SPACET_PLUS_canonical-model-registry_I01-R01.csv)  
  _Done when:_ All canonical entities are registered and referenced by schemas.

- Change log (LOG): [Registry change log](02_IDS_REGISTRY/91_00_LOG_LC03_AMPEL360_SPACET_PLUS_registry-change-log_I01-R01.md)  
  _Done when:_ Every change references a decision/change record (P7).

---

### P3 — Schema & Versioning (Semantic Closure)
- Folder: [03_SCHEMA/](03_SCHEMA/)  
  _Comment:_ Defines the authoritative schemas and the rules for their evolution.

- Schema (SCH/JSON): [Schema registry schema](03_SCHEMA/91_00_SCH_LC03_AMPEL360_SPACET_PLUS_schema-registry-schema_I01-R01.json)  
  _Done when:_ Validates registry format and is used by CI.

- Standard (STD): [Schema versioning policy](03_SCHEMA/91_00_STD_LC03_AMPEL360_SPACET_PLUS_schema-versioning-policy_I01-R01.md)  
  _Done when:_ Compatibility/breaking-change rules exist and are enforced.

- Standard (STD): [Deprecation & migration policy](03_SCHEMA/91_00_STD_LC03_AMPEL360_SPACET_PLUS_schema-migration-policy_I01-R01.md)  
  _Done when:_ Deprecation windows and migration artifacts are mandatory and defined.

- Units/Frames/Enums map (TAB/CSV): [Common primitives mapping](03_SCHEMA/91_00_TAB_LC03_AMPEL360_SPACET_PLUS_common-primitives-mapping_I01-R01.csv)  
  _Done when:_ Common units/frames/enums are standardized (prevents schema divergence).

---

### P4 — Exports (Consumable Data Closure)
- Folder: [04_EXPORTS/](04_EXPORTS/)  
  _Comment:_ Reproducible schema packs for downstream consumption and evidence.

- Baseline export (TAB/CSV): [Baseline schema registry export](04_EXPORTS/91_00_TAB_LC04_AMPEL360_SPACET_PLUS_baseline-schema-registry-export_I01-R01.csv)  
  _Done when:_ Export is reproducible and validated.

- Schema pack manifest (RPT): [Schema pack manifest](04_EXPORTS/91_00_RPT_LC04_AMPEL360_SPACET_PLUS_schema-pack-manifest_I01-R01.md)  
  _Done when:_ Tools/versions, included schemas, and checksums are listed.

- Diagram (DIA): [Schema dependency map](04_EXPORTS/91_00_DIA_LC04_AMPEL360_SPACET_PLUS_schema-dependency-map_I01-R01.md)  
  _Done when:_ Dependencies are explicit and reference registry IDs.

---

### P5 — CI Gates (Enforcement Closure)
- Folder: [05_CI_GATES/](05_CI_GATES/)  
  _Comment:_ Governance enforcement: validity, uniqueness, version rules, and registry completeness.

- Requirements (STD): [CI validation requirements](05_CI_GATES/91_00_STD_LC05_AMPEL360_SPACET_PLUS_ci-validation-requirements_I01-R01.md)  
  _Done when:_ Rules map to checks; failures are actionable.

- Checklist (LOG): [CI checklist](05_CI_GATES/91_00_LOG_LC05_AMPEL360_SPACET_PLUS_ci-checklist_I01-R01.md)  
  _Done when:_ Checklist matches CI outputs and reviewer expectations.

- Sample run (RPT): [CI validation sample run](05_CI_GATES/91_00_RPT_LC05_AMPEL360_SPACET_PLUS_ci-validation-sample-run_I01-R01.md)  
  _Done when:_ Demonstrates pass/fail cases (missing registry entry, duplicate schema ID, breaking change without bump).

---

### P6 — Evidence Pack (Proof Closure)
- Folder: [06_EVIDENCE/](06_EVIDENCE/)  
  _Comment:_ NKU credit requires reproducible evidence and stable links.

- Evidence pack index (IDX): [Evidence pack](06_EVIDENCE/91_00_IDX_LC06_AMPEL360_SPACET_PLUS_k06-ata-91-evidence-pack_I01-R01.md)  
  _Done when:_ All required evidence is linked and current.

- Evidence links (TRC/CSV): [Evidence links register](06_EVIDENCE/91_00_TRC_LC06_AMPEL360_SPACET_PLUS_k06-ata-91-evidence-links_I01-R01.csv)  
  _Done when:_ Each claim has an evidence link and status (OK/STALE/MISSING).

- NKU ledger (TAB/CSV): [NKU ledger](06_EVIDENCE/91_00_TAB_LC06_AMPEL360_SPACET_PLUS_k06-ata-91-nku-ledger_I01-R01.csv)  
  _Done when:_ Partition scores are updated and backed by evidence + decision.

---

### P7 — Decisions & Approvals (Authority Closure)
- Folder: [07_DECISIONS/](07_DECISIONS/)  
  _Comment:_ Converts evidence into approved baseline outcomes for schema governance.

- Decision minutes (MIN): [Decision minutes](07_DECISIONS/91_00_MIN_LC07_AMPEL360_SPACET_PLUS_k06-ata-91-decision-minutes_I01-R01.md)  
  _Done when:_ Decision, rationale, dissent/risks are recorded.

- Approvals log (LOG): [Approvals log](07_DECISIONS/91_00_LOG_LC07_AMPEL360_SPACET_PLUS_k06-ata-91-approvals_I01-R01.md)  
  _Done when:_ CM approval + schema authority sign-offs are referenced.

---

### P8 — Traceability & Adoption (Impact Closure)
- Folder: [08_TRACEABILITY/](08_TRACEABILITY/)  
  _Comment:_ Ensures all consumers adopt ATA 91 schema governance; prevents “shadow schema” proliferation.

- Consumers (TRC/CSV): [Consumers list](08_TRACEABILITY/91_00_TRC_LC08_AMPEL360_SPACET_PLUS_k06-ata-91-consumers_I01-R01.csv)  
  _Done when:_ Consumers are listed with schema/version and owner.

- Adoption status (RPT): [Adoption status](08_TRACEABILITY/91_00_RPT_LC08_AMPEL360_SPACET_PLUS_k06-ata-91-adoption-status_I01-R01.md)  
  _Done when:_ Each consumer has status + remediation plan if blocked.

---

## 4) Cross-ATA Links (same Knot, coupled closures)

- [ATA 90 — NN / Trace / DPP spine](../ATA_90/)  
  _Comment:_ ATA 91 schemas must align with the ATA 90 meta-registry and provenance expectations.

- [ATA 93 — Traceability Graph](../ATA_93/)  
  _Comment:_ Trace edge semantics must be schema-defined and validated.

- [ATA 94 — DPP](../ATA_94/)  
  _Comment:_ DPP export packs must use schema registry IDs and provenance schema rules.

- [ATA 95 — SBOM / ModelBOM](../ATA_95/)  
  _Comment:_ Supply-chain artifacts must reference schemas and registry entries.

- [ATA 98 — Signed Export Packs](../../../../../STK_DATA-data-data-governance/KNOTS/K08_dpp-sbom-provenance-scope/ATA_TASKS/ATA_98)  
  _Comment:_ Signing/hashing/provenance mechanisms for schema packs and DPP packs.

- [ATA 99 — Master Registers](../ATA_99/)  
  _Comment:_ Consolidated registers and anti-duplication controls.

- [ATA 101/107/109 — Sim/Test nodes](../ATA_101/) / [ATA_107](../ATA_107/) / [ATA_109](../ATA_109/)  
  _Comment:_ Sim/test evidence nodes must consume schemas from ATA 91 (no local forks).

---

## 5) Control & Monitoring (NKU Values + TEKNIA Sharing Rules)

### 5.1 NKU Control Model
**Primary metric:** NKU Progress Score for K06/ATA91  
**Source of truth:** [NKU ledger](06_EVIDENCE/91_00_TAB_LC06_AMPEL360_SPACET_PLUS_k06-ata-91-nku-ledger_I01-R01.csv)

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
| NKU ledger updates | AI + DATA | Per PR affecting K06/ATA91 | NKU ledger + evidence links | No score uplift without links |
| CI gate compliance | CM + Tooling | Per PR | CI gates + logs | Enforcement mechanism |
| Evidence completeness | SE + V&V | Weekly / per gate | Evidence pack index | Detect staleness |
| Decision capture | CM WG + Schema Authority | At gate closure | Decisions + approvals | Required for closure |
| Adoption tracking | Consumer owners | Biweekly | Consumers + adoption status | Prevent shadow schemas |

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
- schema validity + registry completeness
- uniqueness of schema IDs and versions
- versioning/breaking-change compliance
- TEKNIA gate for “approved” TEKTOK status (NV + dedup)

---

## 6) Practical Notes (common failure modes)
- Do not accept “approved” schema changes without a decision record (P7) and evidence links (P6).
- Schema registry completeness is non-negotiable; missing entries are immediate CI failures.
- Breaking schema changes must ship with migration guidance and deprecation policy adherence.
