---
title: "K06 ATA 06 Tasklist"
type: IDX
variant: SPACET
status: Draft
knot_id: K06
ata: "06"
lc_or_subbucket: "LC01"
---

# K06 — data-governance-ssot-schemas-identifiers
## ATA 06 — Tasklist (Dimensions and Areas)

## Links (GitHub-navigable)
- Knot overview: [K06 overview](../../00_00_IDX_LC01_AMPEL360_SPACET_PLUS_k06-data-governance-ssot-schemas-identifiers_v01.md)
- Portal index: [AMPEL360-SPACE-T-PORTAL index](../../../../../00_00_IDX_LC01_AMPEL360_SPACET_PLUS_stakeholder-entrypoints_v01.md)
- Stakeholder entrypoint (AI): [STK_AI entrypoint](../../../../00_00_IDX_LC01_AMPEL360_SPACET_PLUS_stakeholder-ai-entrypoint_v01.md)
- ATA 06 home (P-PROGRAM): [AMPEL360_SPACE-T/P-PROGRAM/ATA 06](../../../../../../AMPEL360_SPACE-T/P-PROGRAM/ATA_06-DIMENSIONS_AND_AREAS/)
  - If your folder name differs, update only this link target.

## Related K06 tasklists
- [ATA 00 (Program Governance)](../ATA_00/)
- [ATA 91 (Schemas)](../ATA_91/)
- [ATA 93 (Traceability Graph)](../ATA_93/)
- [ATA 99 (Master Registers)](../ATA_99/)

---

## 1) Uncertainty to Resolve (ATA-specific)
For ATA 06 (Dimensions and Areas), the K06 uncertainty is to define a **single authoritative geometry/envelope SSOT** that is:
- **Identified** via canonical IDs (datums, zones, keep-outs, service envelopes, access volumes).
- **Versioned** with stable schema rules so tooling and downstream ATAs can consume it.
- **Traceable** to requirements, safety constraints, and infrastructure compatibility assumptions.

### Decision required
A CM-approved decision covering:
- Which dataset is authoritative (CAD SSOT / derived exports / published tables).
- Identifier grammar for datums/zones/envelopes.
- Publication format(s) and schema versioning policy.
- CI validation rules for geometry/envelope artifacts.

## 2) Scope Boundary
### In-scope
- Geometry/envelope **identifier set** (datums, zones, areas, envelopes).
- Canonical “areas & dimensions” schema (fields, units, tolerances, coordinate frames).
- Publication routes (e.g., CSV/JSON + diagrams + extracted metadata) and versioning.
- CI checks: naming + metadata + schema validation + unit consistency checks.

### Out-of-scope
- Full CAD modeling methodology (owned by design tooling unless pulled into this knot).
- Spaceport facility design (handled in ATA 80–89; linked only via interface constraints).

## 3) Owners & Stakeholders
- **Primary owner:** SE + DATA (with AI supporting extraction/validation automation)
- **Approvers:** CM WG
- **Contributors:** STR, OPS, SPACEPORT, CERT, TEST

## 4) Interfaces / Affected Areas
### Key dependencies
- Datum policy and coordinate frames used across ATAs (K04 integration boundary risk).
- Spaceport compatibility envelopes (ATA 80–89) consume ATA 06 data.
- Sim/test correlation may require “frozen envelope sets” (ATA 101/113/116).

### Authoritative targets (SSOT candidates)
- `AMPEL360_SPACE-T/P-PROGRAM/ATA_06-DIMENSIONS_AND_AREAS/`
- `AMPEL360_SPACE-T/N-NEURAL_NETWORKS/ATA_91-*` (schema definitions)
- `AMPEL360_SPACE-T/N-NEURAL_NETWORKS/ATA_93-*` (traceability evidence)

## 5) Closure Criteria
This tasklist is **closed only if** all conditions are true:
1. Canonical IDs for areas/dimensions/envelopes are defined and published.
2. A schema (fields, units, coordinate frames, tolerances) is published and versioned.
3. CI validations exist (schema + units + basic consistency) and are documented.
4. A “golden export” baseline exists (frozen set) and is referenced by downstream ATAs (80–89, 101+ as applicable).
5. Baseline change record is created and trace links updated.

## 6) Tasks (minimum set)
### 6.1 Define SSOT and identifiers
- [ ] **T1** Define authoritative source (CAD vs derived tables) and ownership.
- [ ] **T2** Define identifier grammar for datums/zones/envelopes (stable, unique).
- [ ] **T3** Define schema: units, coordinate frame, tolerances, metadata.

### 6.2 Publish and enforce
- [ ] **T4** Publish canonical exports (CSV/JSON) + minimal diagram references.
- [ ] **T5** Implement CI validation: schema checks + unit checks + required fields.

### 6.3 Evidence and adoption
- [ ] **T6** Produce a frozen “baseline envelope set” with release manifest.
- [ ] **T7** Link downstream consumers (Ops/Infra/Sim) and record adoption evidence.

## 7) Outputs / Artifacts
- Identifier set and registry entries (ATA 00 + ATA 06)
- Schema definition (ATA 91)
- Frozen baseline export pack (linked to release)
- CI validation logs (evidence)
- Traceability links (ATA 93)

## 8) Dependencies / Risks
- Risk: multiple competing “truths” (CAD vs spreadsheets vs diagrams) without SSOT.
- Risk: unit/frame mismatches causing downstream integration errors (K04 coupling).
- Dependency: CM approval and registry governance (ATA 00).
