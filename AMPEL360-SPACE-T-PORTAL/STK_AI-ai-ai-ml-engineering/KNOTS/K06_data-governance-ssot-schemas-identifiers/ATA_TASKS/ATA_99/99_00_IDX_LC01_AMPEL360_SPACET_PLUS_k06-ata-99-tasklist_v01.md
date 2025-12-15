---
title: "K06 ATA 99 — Partitioned Uncertainty Resolution Index"
type: IDX
variant: SPACET
status: Draft
knot_id: K06
ata: "99"
lc_or_subbucket: "LC01"
description: "GitHub-navigable hub for closing K06 (SSOT/Schemas/Identifiers) for ATA 99 (Master Registers, Anti-Duplication, SSOT Consolidation) with NKU control and TEKNIA sharing rules."
---

# K06 — Data Governance (SSOT / Schemas / Identifiers)
## ATA 99 — Partitioned Uncertainty Resolution Index (IDX)

This file is the **single navigation hub** for all artifacts required to close **K06** for **ATA 99** (your domain for **Master Registers and SSOT consolidation**).  
NKU progress is credited only when each partition is closed with **evidence + approval**.

> ATA 99 is the K06 “anti-fragmentation governor”: if master registers are weak, every other ATA will drift into duplicated IDs, conflicting schemas, and non-auditable exports.

---

## 1) Global Navigation (GitHub-navigable)

- Knot overview: [K06 overview](../../00_00_IDX_LC01_AMPEL360_SPACET_PLUS_k06-data-governance-ssot-schemas-identifiers_v01.md)  
  _Comment:_ Canonical K06 scope, impacted ATAs, closure criteria, and shared definitions.

- Portal index: [AMPEL360-SPACE-T-PORTAL index](../../../../../00_00_IDX_LC01_AMPEL360_SPACET_PLUS_stakeholder-entrypoints_v01.md)  
  _Comment:_ Global entry point; use it to navigate stakeholders and the knot portfolio.

- Stakeholder entrypoint (AI): [STK_AI entrypoint](../../../../00_00_IDX_LC01_AMPEL360_SPACET_PLUS_stakeholder-ai-entrypoint_v01.md)  
  _Comment:_ AI/ML execution lane; automation hooks and governance helpers.

- ATA 99 home (Master Registers): [AMPEL360_SPACE-T/N-NEURAL_NETWORKS/ATA 99](../../../../../../AMPEL360_SPACE-T/N-NEURAL_NETWORKS/ATA_99-MASTER-REGISTERS/)  
  _Comment:_ Intended authoritative location for ATA 99 outputs. If your folder name differs, update only this link target.

---

## 2) ATA 99 K06 Focus (what uncertainty we are closing)

### Uncertainty to Resolve (ATA-specific)
K06 within ATA 99 is the absence of a single governed SSOT for:
- **Master registers inventory:** what registers exist, where they live, who owns them, and what they govern.
- **Deduplication policy:** how duplicates are detected, resolved, and prevented (global uniqueness rules).
- **Namespace boundaries:** which ATA owns which identifiers/schemas/registries, and how delegation works.
- **Canonical cross-links:** consistent references between registries (schemas ↔ trace graph ↔ DPP ↔ BOM).
- **Drift monitoring:** detection of registry divergence, stale references, and broken links.
- **Enforcement:** CI checks that ensure new artifacts register correctly and do not introduce duplicates.

### Primary consumers (typical)
- Configuration management, all ATA owners, CI automation, DPP and traceability pipelines, agents, auditors.

---

## 3) Partitioned Uncertainty Resolution Pathway (P1–P8)

Each partition corresponds to a dedicated folder. **Do not credit closure** unless the partition’s “Done” definition is satisfied.

### P1 — Work Breakdown & Ownership (Execution Closure)
- Folder: [01_WBS/](01_WBS/)  
  _Comment:_ Converts uncertainty into executable work packages (tasks, owners, inputs/outputs).

- WBS index: [K06 ATA 99 Work Breakdown](01_WBS/99_00_IDX_LC01_AMPEL360_SPACET_PLUS_k06-ata-99-workbreakdown_v01.md)  
  _Closes:_ “We don’t know what to do next / who owns it.”  
  _Done when:_ T001–T010 exist with owners, acceptance criteria, and artifact links.

- RACI (CSV): [RACI](01_WBS/99_00_MAT_LC06_AMPEL360_SPACET_PLUS_k06-ata-99-raci_v01.csv)  
  _Closes:_ Responsibility ambiguity (execution vs approval).  
  _Done when:_ CM approval path is explicit and accepted.

**Task stubs (minimum set — expanded for master register governance):**
- T001: [Register inventory SSOT](01_WBS/99_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t001-register-inventory-ssot_v01.md)  
  _Comment:_ Defines the master inventory of registers and their authoritative paths.

- T002: [Namespace & ownership boundaries](01_WBS/99_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t002-namespace-ownership-boundaries_v01.md)  
  _Comment:_ Defines who owns which ID spaces and how delegation works.

- T003: [Deduplication policy](01_WBS/99_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t003-deduplication-policy_v01.md)  
  _Comment:_ Detection + resolution workflow; canonical tie-breakers; required decision records.

- T004: [Global identifier coordination](01_WBS/99_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t004-global-identifier-coordination_v01.md)  
  _Comment:_ Ensures schema IDs, trace IDs, DPP IDs, BOM IDs do not conflict.

- T005: [Cross-registry link semantics](01_WBS/99_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t005-cross-registry-link-semantics_v01.md)  
  _Comment:_ How registries reference each other (fields, formats, required metadata).

- T006: [Drift monitoring design](01_WBS/99_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t006-drift-monitoring-design_v01.md)  
  _Comment:_ Defines checks for divergence, stale references, and missing registry entries.

- T007: [CI validation gates](01_WBS/99_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t007-ci-validation-gates_v01.md)  
  _Comment:_ Blocks new duplicates and missing registry entries; enforces link integrity.

- T008: [Registry consolidation procedure](01_WBS/99_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t008-registry-consolidation-procedure_v01.md)  
  _Comment:_ How to merge parallel registries into the master without breaking consumers.

- T009: [Baseline master registers set](01_WBS/99_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t009-baseline-master-registers-set_v01.md)  
  _Comment:_ Frozen master register baseline for a milestone release.

- T010: [Verification procedure](01_WBS/99_00_ACT_LC06_AMPEL360_SPACET_PLUS_k06-t010-verification-procedure_v01.md)  
  _Comment:_ How to verify master registers integrity, dedup, and drift controls.

---

### P2 — IDs & Registry (Identity Closure)
- Folder: [02_IDS_REGISTRY/](02_IDS_REGISTRY/)  
  _Comment:_ Establishes the authoritative master register set and the rules that bind them.

- Standard (STD): [Master register governance](02_IDS_REGISTRY/99_00_STD_LC03_AMPEL360_SPACET_PLUS_master-register-governance_v01.md)  
  _Done when:_ Governance is approved and referenced by CI and all register owners.

- Registry (TAB/CSV): [Master register inventory](02_IDS_REGISTRY/99_00_TAB_LC03_AMPEL360_SPACET_PLUS_master-register-inventory_v01.csv)  
  _Done when:_ Inventory is complete, authoritative, and includes owner + scope + SSOT path for each register.

- Registry (TAB/CSV): [Global namespace registry](02_IDS_REGISTRY/99_00_TAB_LC03_AMPEL360_SPACET_PLUS_global-namespace-registry_v01.csv)  
  _Done when:_ All namespaces are declared and ownership boundaries are explicit.

- Change log (LOG): [Registry change log](02_IDS_REGISTRY/99_00_LOG_LC03_AMPEL360_SPACET_PLUS_registry-change-log_v01.md)  
  _Done when:_ Every change references a decision (P7).

---

### P3 — Schema & Versioning (Semantic Closure)
- Folder: [03_SCHEMA/](03_SCHEMA/)  
  _Comment:_ Defines machine-readable structures for the master registers and link semantics.

- Schema (SCH/JSON): [Master register inventory schema](03_SCHEMA/99_00_SCH_LC03_AMPEL360_SPACET_PLUS_master-register-inventory-schema_v01.json)  
  _Done when:_ Validates inventory structure and is used by CI.

- Schema (SCH/JSON): [Cross-registry link schema](03_SCHEMA/99_00_SCH_LC03_AMPEL360_SPACET_PLUS_cross-registry-link-schema_v01.json)  
  _Done when:_ Validates how registries reference each other.

- Standard (STD): [Schema versioning policy](03_SCHEMA/99_00_STD_LC03_AMPEL360_SPACET_PLUS_schema-versioning-policy_v01.md)  
  _Done when:_ Compatibility/breaking-change rules exist and are enforced.

---

### P4 — Exports (Consumable Data Closure)
- Folder: [04_EXPORTS/](04_EXPORTS/)  
  _Comment:_ Deterministic exports of the master inventory and drift reports for consumers and audits.

- Baseline export (TAB/CSV): [Baseline master register inventory export](04_EXPORTS/99_00_TAB_LC04_AMPEL360_SPACET_PLUS_baseline-master-register-inventory-export_v01.csv)  
  _Done when:_ Export is reproducible, validated, and milestone-referenced.

- Drift report (RPT): [Drift report](04_EXPORTS/99_00_RPT_LC04_AMPEL360_SPACET_PLUS_drift-report_v01.md)  
  _Done when:_ Drift signals are generated deterministically and linked to remediation actions.

- Manifest (RPT): [Export manifest](04_EXPORTS/99_00_RPT_LC04_AMPEL360_SPACET_PLUS_export-manifest_v01.md)  
  _Done when:_ Inputs/tools/versions are recorded; rebuild is deterministic.

- Diagram (DIA): [Register topology map](04_EXPORTS/99_00_DIA_LC04_AMPEL360_SPACET_PLUS_register-topology-map_v01.md)  
  _Done when:_ Diagram references match the inventory and namespaces.

---

### P5 — CI Gates (Enforcement Closure)
- Folder: [05_CI_GATES/](05_CI_GATES/)  
  _Comment:_ Blocks merges that introduce duplicates, missing registrations, or broken cross-links.

- Requirements (STD): [CI validation requirements](05_CI_GATES/99_00_STD_LC05_AMPEL360_SPACET_PLUS_ci-validation-requirements_v01.md)  
  _Done when:_ Rules map to checks; failures are actionable.

- Checklist (LOG): [CI checklist](05_CI_GATES/99_00_LOG_LC05_AMPEL360_SPACET_PLUS_ci-checklist_v01.md)  
  _Done when:_ Checklist matches CI outputs and reviewer expectations.

- Sample run (RPT): [CI validation sample run](05_CI_GATES/99_00_RPT_LC05_AMPEL360_SPACET_PLUS_ci-validation-sample-run_v01.md)  
  _Done when:_ Demonstrates pass/fail cases (duplicate ID, missing inventory entry, broken cross-link).

---

### P6 — Evidence Pack (Proof Closure)
- Folder: [06_EVIDENCE/](06_EVIDENCE/)  
  _Comment:_ NKU credit requires reproducible evidence and stable links for dedup decisions and drift resolution.

- Evidence pack index (IDX): [Evidence pack](06_EVIDENCE/99_00_IDX_LC06_AMPEL360_SPACET_PLUS_k06-ata-99-evidence-pack_v01.md)  
  _Done when:_ All required evidence is linked and current.

- Evidence links (TRC/CSV): [Evidence links register](06_EVIDENCE/99_00_TRC_LC06_AMPEL360_SPACET_PLUS_k06-ata-99-evidence-links_v01.csv)  
  _Done when:_ Each claim has evidence links and status (OK/STALE/MISSING).

- NKU ledger (TAB/CSV): [NKU ledger](06_EVIDENCE/99_00_TAB_LC06_AMPEL360_SPACET_PLUS_k06-ata-99-nku-ledger_v01.csv)  
  _Done when:_ Partition scores are updated and backed by evidence + decision.

---

### P7 — Decisions & Approvals (Authority Closure)
- Folder: [07_DECISIONS/](07_DECISIONS/)  
  _Comment:_ Converts evidence into approved baseline outcomes for master register governance, dedup outcomes, and namespace boundaries.

- Decision minutes (MIN): [Decision minutes](07_DECISIONS/99_00_MIN_LC07_AMPEL360_SPACET_PLUS_k06-ata-99-decision-minutes_v01.md)  
  _Done when:_ Decision, rationale, dissent/risks are recorded (including dedup tie-breakers).

- Approvals log (LOG): [Approvals log](07_DECISIONS/99_00_LOG_LC07_AMPEL360_SPACET_PLUS_k06-ata-99-approvals_v01.md)  
  _Done when:_ CM approval + register authority sign-offs are referenced.

---

### P8 — Traceability & Adoption (Impact Closure)
- Folder: [08_TRACEABILITY/](08_TRACEABILITY/)  
  _Comment:_ Ensures register owners and consumers adopt the master inventory and comply with dedup/link rules.

- Consumers (TRC/CSV): [Register owners & consumers list](08_TRACEABILITY/99_00_TRC_LC08_AMPEL360_SPACET_PLUS_k06-ata-99-consumers_v01.csv)  
  _Done when:_ Owners/consumers are listed with responsibilities and verification expectations.

- Adoption status (RPT): [Adoption status](08_TRACEABILITY/99_00_RPT_LC08_AMPEL360_SPACET_PLUS_k06-ata-99-adoption-status_v01.md)  
  _Done when:_ Each register owner has compliance status + remediation plan if blocked.

---

## 4) Cross-ATA Links (same Knot, coupled closures)

ATA 99 coordinates the K06 “spine.” These couplings are mandatory.

- [ATA 90 — Meta spine (NN / Schemas / Trace / DPP)](../ATA_90/)  
  _Comment:_ ATA 99 must prevent parallel registries and define ownership boundaries.

- [ATA 91 — Schemas](../ATA_91/)  
  _Comment:_ Schema registry is a governed register; must appear in master inventory and namespace mapping.

- [ATA 93 — Traceability Graph](../ATA_93/)  
  _Comment:_ Trace node/edge registries must appear in master inventory and cross-link schema rules.

- [ATA 94 — DPP](../ATA_94/)  
  _Comment:_ DPP registry and view registries must be inventoried and governed.

- [ATA 95 — SBOM / ModelBOM](../ATA_95/)  
  _Comment:_ BOM registries and policy outputs must be inventoried and governed.

- [ATA 98 — Signed Export Packs](../ATA_98/)  
  _Comment:_ Signed export packs should be a governed register or governed reference class.

**Sim/Test Coupling (100+):**
- [ATA 101](../ATA_101/) / [ATA 107](../ATA_107/) / [ATA 109](../ATA_109/)  
  _Comment:_ Evidence nodes must register their export packs and trace references according to ATA 99 rules.

---

## 5) Control & Monitoring (NKU Values + TEKNIA Sharing Rules)

### 5.1 NKU Control Model
**Primary metric:** NKU Progress Score for K06/ATA99  
**Source of truth:** [NKU ledger](06_EVIDENCE/99_00_TAB_LC06_AMPEL360_SPACET_PLUS_k06-ata-99-nku-ledger_v01.csv)

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
| NKU ledger updates | AI + DATA + CM | Per PR affecting K06/ATA99 | NKU ledger + evidence links | No score uplift without links |
| CI gate compliance | CM + Tooling | Per PR | CI gates + logs | Enforcement mechanism |
| Duplicate detection | CM + Tooling | Per PR + weekly sweep | CI outputs + drift report | Must produce actionable diff |
| Register inventory completeness | CM WG | Monthly / per gate | Inventory export | Missing register is a blocker |
| Evidence freshness | SE + V&V | Weekly / per gate | Evidence links register | Detect staleness |
| Decision capture | CM WG | At dedup/namespace changes | Decisions + approvals | Required for closure |
| Adoption tracking | Register owners | Biweekly | Adoption status | Prevent shadow registers |

### 5.3 Thresholds
- Green ≥ 0.80; Amber 0.50–0.79; Red < 0.50  
Hard blockers: missing master inventory, missing namespace mapping, missing dedup policy, missing P7 decisions for dedup outcomes, stale evidence for any closed item.

### 5.4 TEKNIA Sharing Rules
TEKTOKs may be created only when:
- Evidence is reproducible (P6 complete)
- Decision exists (P7 complete, CM-approved)
- Dedup passes (SHA-256) and no namespace conflict exists
- NV threshold met (≥ 0.50 internal, ≥ 0.65 external recommended)

### 5.5 TEKNIA Packaging Requirements (mandatory metadata)
Any TEKTOK that claims SSOT or introduces IDs/schemas must include:
- knot_id, ata, partitions_closed
- namespace_id + owner + registry references
- dedup evidence (hash + conflict resolution)
- trace snapshot/evidence links
- decision reference
- nv + rationale + sharing classification

### 5.6 Enforcement
CI should validate:
- new registers must be declared in master inventory
- cross-registry links must validate against link schema
- duplicate IDs across namespaces are blocked
- TEKNIA gate for “approved” TEKTOK status (NV + dedup)

---

## 6) Practical Notes (common failure modes)
- “Multiple inventories” is an immediate K06 failure mode—ATA 99 must declare the single inventory SSOT.
- Dedup without a decision record creates governance debt; require P7 always.
- Namespace boundaries must be explicit, otherwise consumers will fork registries and K06 will never converge.
