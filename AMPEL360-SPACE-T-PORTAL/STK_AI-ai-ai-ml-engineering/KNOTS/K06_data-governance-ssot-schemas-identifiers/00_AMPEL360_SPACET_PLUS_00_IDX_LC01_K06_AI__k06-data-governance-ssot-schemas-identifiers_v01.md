---
title: "Backlog Knot K06: data-governance-ssot-schemas-identifiers"
type: IDX
variant: "SPACET"
status: Draft
knot_id: "K06"
stakeholder_id: "AI"
affected_atas: ["00", "06", "31", "45", "46", "90", "91", "93", "94", "95", "99", "101", "107", "109"]
bucket: "00"
lc_or_subbucket: "LC01"
---

# Backlog Knot K06 — data-governance-ssot-schemas-identifiers

This is the **K06 master index** for **Partitioned Uncertainty Resolution (NKU progress)** across impacted ATAs.
It is the authoritative navigation hub for **SSOT**, **schema governance**, and **identifier discipline** in AMPEL360 Space-T.

---

## 1) Problem Statement

K06 exists because the program currently lacks a single, governed, machine-enforceable definition of:

- **SSOT boundaries** (what is authoritative, where it lives, who owns it, how it changes)
- **Schema governance** (registries, canonical models, versioning, compatibility, deprecation, packaging)
- **Identifiers** (global uniqueness, namespaces, anti-duplication, cross-registry link semantics)
- **Trace semantics** (node/edge types, evidence link rules, audit-ready snapshots)
- **Export governance** (DPP packs, BOM packs, signed releases, provenance metadata)

**Decision required:** establish the governance baseline (standards + registries + CI gates + approvals) so that **every ATA can produce auditable, reproducible artifacts** without drift, duplication, or broken trace links.

---

## 2) Scope Boundary

### In-scope
- Naming/identifier grammar and namespace control
- Schema registry + canonical data model governance
- Traceability graph semantics and evidence link discipline
- DPP, SBOM/ModelBOM, signed export pack governance (structure + provenance + verification)
- CI/CD enforcement rules (pre-commit + PR gates + weekly drift scans)
- Adoption controls: consumer onboarding and anti-shadow-artifact prevention

### Out-of-scope
- Designing the underlying subsystem behavior (ATA engineering content itself)
- Generating the full operational datasets (only schemas/registries/pack structures)
- Vendor selection and procurement decisions (unless required as evidence artifacts)
- Non-governed exploratory drafts without intent to converge into SSOT

---

## 3) Impacted ATAs (GitHub-navigable)

Each link below is the **ATA-specific K06 tasklist index**. Treat them as **execution partitions**: K06 is not closed unless each critical ATA reaches closure thresholds.

### P-Program / Governance
- [ATA 00 — General (program SSOT, nomenclature, CM, finance, trade studies)](./ATA_TASKS/ATA_00/00_AMPEL360_SPACET_PLUS_00_IDX_LC01_K06_CM__k06-ata-00-tasklist_v01.md)  
  _Comment:_ Defines the **program-wide governance spine** and decision rights. K06 cannot close without ATA 00 baseline rules.

- [ATA 06 — Dimensions & Areas (zone/area conventions as identifiers)](./ATA_TASKS/ATA_06/06_AMPEL360_SPACET_PLUS_00_IDX_LC01_K06_CM__k06-ata-06-tasklist_v01.md)  
  _Comment:_ Prevents ambiguity in **geometric/zone identifiers** used across ops, maintenance, and digital twins.

### Technology consumers (schema-adopters)
- [ATA 31](./ATA_TASKS/ATA_31/31_AMPEL360_SPACET_PLUS_00_IDX_LC01_K06_CM__k06-ata-31-tasklist_v01.md)  
  _Comment:_ Primary consumer of governed schemas (interfaces/telemetry). Ensure no “shadow schemas”.

- [ATA 45](./ATA_TASKS/ATA_45/45_AMPEL360_SPACET_PLUS_00_IDX_LC01_K06_CM__k06-ata-45-tasklist_v01.md)  
  _Comment:_ High-coupling integration domain; schema governance must be enforced at interface level.

- [ATA 46](./ATA_TASKS/ATA_46/46_AMPEL360_SPACET_PLUS_00_IDX_LC01_K06_CM__k06-ata-46-tasklist_v01.md)  
  _Comment:_ Data exchange + configuration integration; requires strict ID and trace alignment.

### Neural / Data Spine (90+)
- [ATA 90 — Neural Networks / wiring / schema spine](./ATA_TASKS/ATA_90/90_AMPEL360_SPACET_PLUS_00_IDX_LC01_K06_CM__k06-ata-90-tasklist_v01.md)  
  _Comment:_ Meta-registry, provenance expectations, and TEKNIA gating anchors.

- [ATA 91 — Schemas & Canonical Data Models](./ATA_TASKS/ATA_91/91_AMPEL360_SPACET_PLUS_00_IDX_LC01_K06_CM__k06-ata-91-tasklist_v01.md)  
  _Comment:_ The schema “engine room”: registry, versioning, compatibility, canonical primitives.

- [ATA 93 — Traceability Graph & Evidence Links](./ATA_TASKS/ATA_93/93_AMPEL360_SPACET_PLUS_00_IDX_LC01_K06_CM__k06-ata-93-tasklist_v01.md)  
  _Comment:_ Enforces graph integrity and evidence-link semantics. K06 is non-auditable without this closure.

- [ATA 94 — Digital Product Passport (DPP) & Provenance Exports](./ATA_TASKS/ATA_94/94_AMPEL360_SPACET_PLUS_00_IDX_LC01_K06_CM__k06-ata-94-tasklist_v01.md)  
  _Comment:_ External-facing consequence: reproducible packs, redaction rules, signing/provenance metadata.

- [ATA 95 — SBOM / ModelBOM / ML Asset Traceability](./ATA_TASKS/ATA_95/95_AMPEL360_SPACET_PLUS_00_IDX_LC01_K06_CM__k06-ata-95-tasklist_v01.md)  
  _Comment:_ Supply-chain integrity for software/ML; policy gates and trace alignment are mandatory.

- [ATA 99 — Master Registers & Anti-Duplication](./ATA_TASKS/ATA_99/99_AMPEL360_SPACET_PLUS_00_IDX_LC01_K06_CM__k06-ata-99-tasklist_v01.md)  
  _Comment:_ Prevents fragmentation: master inventory of registries, namespace boundaries, dedup governance, drift monitoring.

### Simulations & Testing (100+)
- [ATA 101 — Simulation evidence node](./ATA_TASKS/ATA_101/101_AMPEL360_SPACET_PLUS_00_IDX_LC01_K06_AI__k06-ata-101-tasklist_v01.md)  
  _Comment:_ Must consume governed schemas and output verifiable evidence packs (no local formats).

- [ATA 107 — Test evidence node](./ATA_TASKS/ATA_107/00_AMPEL360_SPACET_PLUS_00_IDX_LC01_K06_CM__k06-ata-107-tasklist_v01.md)  
  _Comment:_ Must publish test evidence using ATA 93 semantics and ATA 98-style signed pack expectations (if applicable).

- [ATA 109 — Qualification/validation evidence node](./ATA_TASKS/ATA_109/00_AMPEL360_SPACET_PLUS_00_IDX_LC01_K06_CM__k06-ata-109-tasklist_v01.md)  
  _Comment:_ Must produce audit-ready V&V trace links; staleness detection is essential.

---

## 4) Decision & Closure Criteria

### Decision Owner
- **Primary:** Configuration Management WG (CM WG)  
- **Delegated Authorities:**  
  - Schemas: ATA 91 authority  
  - Trace: ATA 93 authority  
  - DPP: ATA 94 authority  
  - BOM: ATA 95 authority  
  - Master registers/dedup: ATA 99 authority  
  - Program governance: ATA 00 authority

### Evidence Required (minimum)
1. Approved **identifier grammar** and **namespace boundary** rules
2. Approved **schema registry** + canonical model registry (SSOT)
3. Approved **trace node/edge semantics** + evidence link schema
4. Reproducible **exports** (registry exports, trace snapshot exports, DPP/BOM manifests)
5. **CI enforcement** (PR gate + pre-commit) proving invalid artifacts cannot merge
6. **Decision records** (minutes + approvals) for any breaking or governance-impacting changes
7. **Adoption tracking** showing consumers are onboarded and not forking shadow schemas

### Acceptance Criteria (K06 Closure)
- NKU ≥ **0.80** across critical partitions (see §6) and no hard blockers open
- All critical ATA tasklists show **P2/P3/P5/P7** closed (IDs/Schema/CI/Decisions)
- Evidence links are **OK (non-stale)** for all closed items
- DPP and BOM baseline exports are **verifiable** and trace-linked
- Master registers inventory is complete and dedup policy is enforced

---

## 5) Pathways (Program-wide execution lanes)

K06 resolves via five pathways. Each pathway has outputs that must be referenced by the ATA tasklists.

### 1) Requirements / ConOps
**Goal:** Define what “SSOT + schema + identifiers” means operationally, and what must be true at each release.  
**Outputs:** governance requirements, scope boundaries, and owner assignments.

### 2) Architecture / ICDs
**Goal:** Define interface contracts as governed schemas and registries; standardize link semantics.  
**Outputs:** schema registries, canonical models, edge semantics, evidence link rules.

### 3) Implementation / Industrialization
**Goal:** Implement the automation that makes governance real (linting, validation, export packs, dedup checks).  
**Outputs:** CI gates, validation scripts, export pack generation tooling, drift monitoring jobs.

### 4) Verification / Qualification
**Goal:** Prove the governance works end-to-end using real PRs and evidence packs; demonstrate audit readiness.  
**Outputs:** validation runs, sample pass/fail demonstrations, evidence pack indexes, trace snapshots.

### 5) Baseline & Release
**Goal:** Freeze released states with reproducible exports and decision logs; ensure consumers can verify authenticity.  
**Outputs:** signed/exportable packs (where applicable), baseline registries, approvals, adoption status.

---

## 6) Control & Monitoring (NKU + TEKNIA Sharing Rules)

### 6.1 NKU Model (Partitioned Uncertainty Resolution)
**NKU is credited only when closure is backed by evidence + decisions.**

- **Scoring:** `score ∈ {0, 0.5, 1.0}` per partition, per ATA
- **Program NKU:** weighted aggregation across ATAs and partitions (authority-defined weights)
- **No-false-closure rule:** a “1.0” requires:
  - evidence links (stable, non-stale), and
  - decision reference (minutes + approvals where required)

**Hard blockers (non-negotiable):**
- Missing schema registry SSOT (ATA 91)
- Missing trace semantics SSOT (ATA 93)
- Missing master registers + dedup governance (ATA 99)
- Missing CI enforcement for naming/registry/link integrity

### 6.2 Monitoring Cadence
| Control Item | Owner | Frequency | Evidence Source | Comment |
|---|---|---:|---|---|
| NKU ledger updates | AI + CM | Per PR touching K06 | ATA evidence packs + ledgers | No uplift without links |
| Duplicate detection | ATA 99 + Tooling | Weekly + on PR | drift reports | Must produce actionable diffs |
| Schema governance compliance | ATA 91 + Tooling | Per PR | CI reports | Prevent shadow schemas |
| Trace integrity & link freshness | ATA 93 + Tooling | Per PR + weekly sweep | CI + staleness checks | Broken links are blockers |
| DPP pack verifiability | ATA 94 + CM | Per release | manifest + verification logs | External-facing integrity |
| BOM policy compliance | ATA 95 + Security/Model Gov | Per PR + release | policy outputs | Exceptions require P7 decisions |

### 6.3 TEKNIA Rules for Sharing (Minimum Gate)
A TEKTOK derived from K06 work may be shared only when:
- Evidence is reproducible and referenced in evidence packs
- Dedup passes (hash + namespace checks)
- Decision record exists for governance-impacting claims
- NV threshold meets program policy (internal ≥ 0.50; external target ≥ 0.65)

Required TEKNIA metadata for K06 outputs:
- `knot_id`, `ata`, `partitions_closed`
- referenced registry IDs / schema IDs / trace snapshot IDs
- evidence links + decision reference
- hash/signature metadata (when baseline/release-grade)
- classification + redaction notes (especially DPP-related)

---

## 7) Immediate Next Actions (Minimum Set)

1. Ensure every impacted ATA index exists and is linked (this file is the hub).
2. Converge on **one** identifier grammar and namespace map (ATA 00 + ATA 99).
3. Converge on **one** schema registry SSOT (ATA 91).
4. Converge on **one** trace semantics SSOT (ATA 93).
5. Enforce via CI so drift cannot reappear (ATA 99 + Tooling).
6. Validate export reproducibility for DPP and BOM packs (ATA 94 + ATA 95).

