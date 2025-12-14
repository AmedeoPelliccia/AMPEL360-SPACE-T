---
title: "K06 ATA 06 — Partitioned Uncertainty Resolution Index"
type: IDX
variant: SPACET
status: Draft
knot_id: K06
ata: "06"
lc_or_subbucket: "LC01"
description: "GitHub-navigable hub for closing K06 (SSOT/Schemas/Identifiers) for ATA 06 (Dimensions and Areas) with NKU control and TEKNIA sharing rules."
---

# K06 — Data Governance (SSOT / Schemas / Identifiers)
## ATA 06 — Partitioned Uncertainty Resolution Index (IDX)

This file is the **single navigation hub** for all artifacts required to close **K06** for **ATA 06 (Dimensions and Areas)**.  
Progress is credited as **NKU** only when the relevant partition is closed with **evidence + approval**.

---

## 1) Global Navigation (GitHub-navigable)

- Knot overview: [K06 overview](../../00_00_IDX_LC01_SPACET_k06-data-governance-ssot-schemas-identifiers_v01.md)  
  _Comment:_ Canonical K06 scope, impacted ATAs, closure criteria, and shared definitions.

- Portal index: [AMPEL360-SPACE-T-PORTAL index](../../../../../00_00_IDX_LC01_SPACET_stakeholder-entrypoints_v01.md)  
  _Comment:_ Global entry point; use it to navigate stakeholders and the full knot portfolio.

- Stakeholder entrypoint (AI): [STK_AI entrypoint](../../../../00_00_IDX_LC01_SPACET_stakeholder-ai-entrypoint_v01.md)  
  _Comment:_ AI/ML execution lane; contains automation hooks, model/schema governance tasks, and compliance helpers.

- ATA 06 home (P-PROGRAM): [AMPEL360_SPACE-T/P-PROGRAM/ATA 06](../../../../../../AMPEL360_SPACE-T/P-PROGRAM/ATA_06-DIMENSIONS_AND_AREAS/)  
  _Comment:_ Authoritative program location for ATA 06 governance outputs. If the folder name differs in your repo, update only this link target.

---

## 2) Partitioned Uncertainty Resolution Pathway (P1–P8)

Each partition corresponds to a dedicated folder. **Do not credit closure** unless the partition’s “Done” definition is satisfied.

### P1 — Work Breakdown & Ownership (Execution Closure)
- Folder: [01_WBS/](01_WBS/)  
  _Comment:_ Converts uncertainty into executable work packages (tasks, owners, inputs/outputs).

- WBS index: [K06 ATA 06 Work Breakdown](01_WBS/06_00_IDX_LC01_SPACET_k06-ata-06-workbreakdown_v01.md)  
  _Closes:_ “We don’t know what to do next / who owns it.”  
  _Done when:_ T001–T006 exist with owners, acceptance criteria, and artifact links.

- RACI (CSV): [RACI](01_WBS/06_00_MAT_LC06_SPACET_k06-ata-06-raci_v01.csv)  
  _Closes:_ Responsibility ambiguity (execution vs approval).  
  _Done when:_ CM approval path is explicit and accepted by all contributors.

**Task stubs (minimum set):**
- T001: [SSOT source & ownership](01_WBS/06_00_ACT_LC06_SPACET_k06-t001-ssot-source-ownership_v01.md)  
  _Comment:_ Declares which source is authoritative (CAD/exports/tables) and who controls change.

- T002: [Identifier grammar](01_WBS/06_00_ACT_LC06_SPACET_k06-t002-identifier-grammar_v01.md)  
  _Comment:_ Prevents uncontrolled proliferation of labels/IDs for zones/envelopes/datums.

- T003: [Schema definition](01_WBS/06_00_ACT_LC06_SPACET_k06-t003-schema-definition_v01.md)  
  _Comment:_ Stabilizes the meaning of geometry-related data (fields, units, frames, tolerances).

- T004: [Export publication](01_WBS/06_00_ACT_LC06_SPACET_k06-t004-export-publication_v01.md)  
  _Comment:_ Defines what downstream consumers can ingest and how it is generated reproducibly.

- T005: [CI validation gates](01_WBS/06_00_ACT_LC06_SPACET_k06-t005-ci-validation-gates_v01.md)  
  _Comment:_ Turns policy into enforcement (fail fast on noncompliance).

- T006: [Baseline envelope set](01_WBS/06_00_ACT_LC06_SPACET_k06-t006-baseline-envelope-set_v01.md)  
  _Comment:_ Produces a frozen “golden set” of envelopes for consumers and verification.

---

### P2 — IDs & Registry (Identity Closure)
- Folder: [02_IDS_REGISTRY/](02_IDS_REGISTRY/)  
  _Comment:_ Ensures every datum/zone/envelope has a unique ID, owner, and lifecycle state.

- Standard (STD): [Identifier grammar](02_IDS_REGISTRY/06_00_STD_LC03_SPACET_geometry-envelope-identifier-grammar_v01.md)  
  _Done when:_ Grammar is approved and referenced by schema + CI gates.

- Registry (TAB/CSV): [Geometry/Envelope registry](02_IDS_REGISTRY/06_00_TAB_LC03_SPACET_geometry-envelope-registry_v01.csv)  
  _Done when:_ Registry is SSOT (no duplicates), with owners/status and required metadata.

- Change log (LOG): [Registry change log](02_IDS_REGISTRY/06_00_LOG_LC03_SPACET_registry-change-log_v01.md)  
  _Done when:_ Every change references a decision/change record (P7).

---

### P3 — Schema & Versioning (Semantic Closure)
- Folder: [03_SCHEMA/](03_SCHEMA/)  
  _Comment:_ Defines stable machine-readable meaning and compatibility rules.

- Schema (SCH/JSON): [Dimensions & Areas schema](03_SCHEMA/06_00_SCH_LC03_SPACET_dimensions-areas-schema_v01.json)  
  _Done when:_ Schema validates exports and is referenced by CI.

- Standard (STD): [Schema versioning policy](03_SCHEMA/06_00_STD_LC03_SPACET_schema-versioning-policy_v01.md)  
  _Done when:_ Compatibility/breaking-change rules exist and are enforced.

- Units/Frames map (TAB/CSV): [Units and frames mapping](03_SCHEMA/06_00_TAB_LC03_SPACET_units-and-frames-mapping_v01.csv)  
  _Done when:_ Every schema field declares unit/frame/tolerance rule to prevent integration defects.

---

### P4 — Exports (Consumable Data Closure)
- Folder: [04_EXPORTS/](04_EXPORTS/)  
  _Comment:_ Provides the reproducible, consumable dataset for downstream ATAs/tools.

- Baseline dataset (TAB/CSV): [Baseline envelope set](04_EXPORTS/06_00_TAB_LC04_SPACET_baseline-envelope-set_v01.csv)  
  _Done when:_ Export is reproducible, validated, and release-referenced.

- Manifest (RPT): [Export manifest](04_EXPORTS/06_00_RPT_LC04_SPACET_export-manifest_v01.md)  
  _Done when:_ Inputs/tools/versions are recorded; rebuild is deterministic.

- Diagram (DIA): [Envelope map](04_EXPORTS/06_00_DIA_LC04_SPACET_envelope-map_v01.md)  
  _Done when:_ Diagram references match registry IDs and the baseline export.

---

### P5 — CI Gates (Enforcement Closure)
- Folder: [05_CI_GATES/](05_CI_GATES/)  
  _Comment:_ Makes governance non-optional; prevents “paper compliance”.

- Requirements (STD): [CI validation requirements](05_CI_GATES/06_00_STD_LC05_SPACET_ci-validation-requirements_v01.md)  
  _Done when:_ Rules map to checks; failures are actionable.

- Checklist (LOG): [CI checklist](05_CI_GATES/06_00_LOG_LC05_SPACET_ci-checklist_v01.md)  
  _Done when:_ Checklist matches CI outputs and reviewer expectations.

- Sample run (RPT): [CI validation sample run](05_CI_GATES/06_00_RPT_LC05_SPACET_ci-validation-sample-run_v01.md)  
  _Done when:_ Demonstrates representative pass/fail cases.

---

### P6 — Evidence Pack (Proof Closure)
- Folder: [06_EVIDENCE/](06_EVIDENCE/)  
  _Comment:_ NKU credit requires reproducible evidence and stable links.

- Evidence pack index (IDX): [Evidence pack](06_EVIDENCE/06_00_IDX_LC06_SPACET_k06-ata-06-evidence-pack_v01.md)  
  _Done when:_ All required evidence is linked and current.

- Evidence links (TRC/CSV): [Evidence links register](06_EVIDENCE/06_00_TRC_LC06_SPACET_k06-ata-06-evidence-links_v01.csv)  
  _Done when:_ Each claim has an evidence link and status (OK/STALE/MISSING).

- NKU ledger (TAB/CSV): [NKU ledger](06_EVIDENCE/06_00_TAB_LC06_SPACET_k06-ata-06-nku-ledger_v01.csv)  
  _Done when:_ Partition scores are updated and backed by evidence + decision.

---

### P7 — Decisions & Approvals (Authority Closure)
- Folder: [07_DECISIONS/](07_DECISIONS/)  
  _Comment:_ Turns evidence into an approved baseline outcome.

- Decision minutes (MIN): [Decision minutes](07_DECISIONS/06_00_MIN_LC07_SPACET_k06-ata-06-decision-minutes_v01.md)  
  _Done when:_ Decision, rationale, dissent/risks are recorded.

- Approvals log (LOG): [Approvals log](07_DECISIONS/06_00_LOG_LC07_SPACET_k06-ata-06-approvals_v01.md)  
  _Done when:_ CM approval + any required sign-offs are referenced.

---

### P8 — Traceability & Adoption (Impact Closure)
- Folder: [08_TRACEABILITY/](08_TRACEABILITY/)  
  _Comment:_ Ensures consumers adopt the SSOT; prevents “closed on paper”.

- Consumers (TRC/CSV): [Consumers list](08_TRACEABILITY/06_00_TRC_LC08_SPACET_k06-ata-06-consumers_v01.csv)  
  _Done when:_ Consumers are listed with interface/version and owner.

- Adoption status (RPT): [Adoption status](08_TRACEABILITY/06_00_RPT_LC08_SPACET_k06-ata-06-adoption-status_v01.md)  
  _Done when:_ Each consumer has status + remediation plan if blocked.

---

## 3) Cross-ATA Links (same Knot, different ATA folders)

These are the primary K06 “coupled closures” that must stay aligned.

- [ATA 00 — Program Governance](../ATA_00/)  
  _Comment:_ Defines naming/metadata/registry authority; blocks false closure if missing.

- [ATA 91 — Schemas](../ATA_91/)  
  _Comment:_ Provides canonical schema governance and validation primitives.

- [ATA 93 — Traceability Graph](../ATA_93/)  
  _Comment:_ Enables evidence trace from IDs → schema → export → decision.

- [ATA 94 — DPP](../ATA_94/)  
  _Comment:_ Ensures data governance supports DPP provenance/exports.

- [ATA 95 — SBOM / ModelBOM](../ATA_95/)  
  _Comment:_ Ensures data governance supports software/model supply chain trace.

- [ATA 98 — Signed Export Packs](../ATA_98/)  
  _Comment:_ Provides signed, auditable export packaging and provenance enforcement.

- [ATA 99 — Master Registers](../ATA_99/)  
  _Comment:_ Provides consolidated registers and anti-duplication mechanisms.

---

## 4) Control & Monitoring (NKU Values + TEKNIA Sharing Rules)

This section defines how progress is **measured, controlled, and credited** (NKU), and how K06 outputs are **packaged and shared** under TEKNIA rules (evidence-first, anti-noise, deduplicated, authority-approved).

### 4.1 NKU Control Model
**Primary metric:** NKU Progress Score for K06/ATA06  
**Source of truth:** [NKU ledger](06_EVIDENCE/06_00_TAB_LC06_SPACET_k06-ata-06-nku-ledger_v01.csv)

**Scoring rule (per partition):**
- `score ∈ {0, 0.5, 1.0}`
  - `0` = missing / not usable
  - `0.5` = draft exists, but missing enforcement/evidence/decision
  - `1.0` = closed with evidence + decision (per criteria below)
- **NKU Progress Score** = `Σ(weight × score)` across partitions P1..P8

**No-false-closure rule (mandatory):**
- Any item with `score = 1.0` must have:
  - at least one evidence link in `06_EVIDENCE/...evidence-links...csv`, and
  - a decision reference in `07_DECISIONS/...decision-minutes...md` (and approvals if applicable).

### 4.2 Monitoring Cadence
| Control Item | Owner | Frequency | Source | Comment |
|---|---|---:|---|---|
| NKU ledger updates (scores + links) | AI + DATA | Per PR affecting K06/ATA06 | NKU ledger + evidence links | Scores must not increase without links |
| CI gate compliance | CM + Tooling | Per PR | CI gates + workflow logs | Enforcement mechanism |
| Evidence pack completeness | SE + TEST | Weekly / per gate | Evidence pack index | Detect stale/missing links |
| Decision/approval capture | CM WG | At closure gates | Decision + approvals | Required for “Closed = 1.0” |
| Consumer adoption tracking | OPS + SPACEPORT + SIM/TEST | Biweekly | Consumers + adoption status | Prevent “paper closure” |

### 4.3 NKU Thresholds (for readiness and escalation)
- **Green:** NKU ≥ 0.80 (release-ready discussion)
- **Amber:** 0.50 ≤ NKU < 0.80 (progress exists, closure incomplete)
- **Red:** NKU < 0.50 (high integration risk; governance immature)

**Hard blockers for release claims:**
- P2 (IDs), P3 (schema), or P5 (CI) not fully closed while claiming a released export (P4).
- P7 decision minutes missing.
- Evidence links stale/missing for any “closed” item.

### 4.4 TEKNIA Rules for Sharing (evidence-first, anti-noise)
**Shareable unit:** TEKTOK (minimal verified technical value note) derived from a closed outcome.

A TEKTOK may be created only if:
1) **Evidence exists and is reproducible** (P6 complete).  
2) **Authority decision exists** (P7 complete, CM-approved).  
3) **Deduplication passes** (payload hash not already present).  
4) **Net Value (NV) threshold met** (below).

**Default sharing classification:**
- **Internal share:** allowed for drafts and partial closures, clearly marked as Draft/Amber.
- **External share:** allowed only after CM approval + redaction review + explicit release tag.

### 4.5 NV (Net Value) and Anti-Noise Gate
- NV range: `0..1`
- **Minimum NV for internal sharing:** `NV ≥ 0.50`
- **Recommended NV for external sharing:** `NV ≥ 0.65`
- **Dedup by SHA-256:** required
- **Synergy credit:** optional, capped, and must be justified (avoid inflated value claims)

**Interpretation for K06/ATA06:**
- ID registry + schema + CI enforcement TEKTOKs often deliver the earliest high NV (high leverage).
- Baseline exports should not be shared as “baseline” unless schema + CI + decision are closed.

### 4.6 TEKNIA Packaging Requirements (minimum metadata)
Any TEKTOK created from this pathway must include:
- Knot ID, ATA, and partition(s) closed
- Claim (which uncertainty is closed)
- Evidence links (artifacts + CI evidence)
- Decision link (minutes + approvals)
- Hash (SHA-256 of payload)
- NV score + rationale
- Sharing classification (internal/external) + redaction notes

Recommended TEKTOK header (example):
```yaml
tektok_id: "TEKTOK-K06-ATA06-0001"
knot_id: "K06"
ata: "06"
partitions_closed: ["P2","P3","P5"]
status: "approved"
hash_sha256: "<sha256>"
nv: 0.68
dedup_by_sha256: true
evidence:
  - "06_EVIDENCE/06_00_TRC_LC06_SPACET_k06-ata-06-evidence-links_v01.csv"
decision:
  - "07_DECISIONS/06_00_MIN_LC07_SPACET_k06-ata-06-decision-minutes_v01.md"
sharing:
  classification: "internal"
  external_allowed: false
````

### 4.7 Enforcement (how rules become non-optional)

CI should enforce at minimum:

* NKU ledger validity (columns, weights sum, allowed score values)
* No-false-closure rule (score=1.0 requires evidence + decision references)
* TEKNIA gate for “approved” TEKTOK status (NV threshold + dedup)

Operational rule: if CI fails, **do not** increase NKU scores and **do not** mark TEKTOKs as approved.

---

## 5) Practical Notes (common failure modes)

* Do not accept a “released baseline export” (P4) without **schema validation** (P3) and **CI enforcement** (P5).
* Do not credit NKU closure without **Decision Minutes** (P7) and an **Evidence Pack** (P6).
* Treat **units/frames/tolerances** as first-class governance objects; most downstream integration defects originate here.

::contentReference[oaicite:0]{index=0}
```
