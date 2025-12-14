---
title: "K06 ATA 00 Tasklist"
type: IDX
variant: SPACET
status: Draft
knot_id: K06
ata: "00"
lc_or_subbucket: "LC01"
---

# K06 — data-governance-ssot-schemas-identifiers
## ATA 00 — Tasklist

## Links (GitHub-navigable)
- Knot overview: [K06 overview](../../00_00_IDX_LC01_SPACET_k06-data-governance-ssot-schemas-identifiers_v01.md)
- Portal index: [AMPEL360-SPACE-T-PORTAL index](../../../../../00_00_IDX_LC01_SPACET_stakeholder-entrypoints_v01.md)
- Stakeholder entrypoint (AI): [STK_AI entrypoint](../../../../00_00_IDX_LC01_SPACET_stakeholder-ai-entrypoint_v01.md)
- ATA 00 home (program governance): [AMPEL360_SPACE-T/P-PROGRAM/ATA 00](../../../../../../AMPEL360_SPACE-T/P-PROGRAM/ATA_00-GENERAL/)
  - If your folder name differs, update only this link target.

## Related ATA tasklists (same Knot)
- [ATA 91 (Schemas)](../ATA_91/)
- [ATA 93 (Traceability Graph)](../ATA_93/)
- [ATA 94 (DPP)](../ATA_94/)
- [ATA 95 (SBOM/ModelBOM)](../ATA_95/)
- [ATA 98 (Signed Export Packs)](../ATA_98/)
- [ATA 99 (Master Registers)](../ATA_99/)

---

## 1) Uncertainty to Resolve (ATA-specific)
ATA 00 must define the **authoritative governance** for:
- Canonical identifiers (parts, docs, baselines, hazards, requirements, datasets, models).
- SSOT rules (what is authoritative, where it lives, how it is versioned).
- Schema/versioning policy used by the whole Space-T repository.

### Decision required
One CM-approved decision covering:
- Identifier grammar + registry authority.
- Schema governance + compatibility rules.
- CI gates for validation and auditability.

## 2) Scope Boundary
### In-scope
- Nomenclature + metadata rules for program-level artifacts (ATA 00).
- Registries and schema publication mechanism (policy + “where it lives”).
- CI enforcement rules + auditability hooks.

### Out-of-scope
- Subsystem-specific schema definitions (owned in ATA 91 and downstream ATAs).
- Tool implementation details beyond “minimum viable enforcement” (owned by tooling backlog unless pulled in).

## 3) Owners & Stakeholders
- **Primary owner:** AI + DATA (joint) with **CM** as approval authority
- **Contributors:** SE, CERT, CY, OPS, TEST
- **Approvers:** CM WG (final), CERT (if compliance impact)

## 4) Interfaces / Affected Areas
### Impacted ATAs (dependency view)
- Direct: ATA 00 (governance), ATA 91 (schemas), ATA 93 (trace graph), ATA 94/95/98 (DPP/SBOM/export packs), ATA 101/109 (sim/test evidence linkage)
- Indirect: any ATA emitting IDs or consuming registries/schemas

### Authoritative targets (SSOT candidates)
- `AMPEL360_SPACE-T/P-PROGRAM/ATA_00-GENERAL/` (program governance)
- `AMPEL360_SPACE-T/N-NEURAL_NETWORKS/ATA_91-*` (schemas)
- `AMPEL360_SPACE-T/N-NEURAL_NETWORKS/ATA_93-*` (traceability)
- `AMPEL360_SPACE-T/N-NEURAL_NETWORKS/ATA_94-*` (DPP)
- `AMPEL360_SPACE-T/N-NEURAL_NETWORKS/ATA_95-*` (SBOM/ModelBOM)
- `AMPEL360_SPACE-T/N-NEURAL_NETWORKS/ATA_98-*` (signed exports)

## 5) Closure Criteria
This tasklist is **closed only if** all conditions are true:
1. Identifier standard approved (CM WG) and published (ATA 00).
2. Schema governance/versioning policy published (DATA owner) and referenced from ATA 00.
3. CI enforcement exists (PR gate) and is documented (how to comply + how it fails).
4. At least one reproducible audit query exists proving: `IDs → Schema → Trace → Signed export`.
5. Baseline update recorded (change record/changelog) and links updated for affected ATAs.

## 6) Tasks (minimum set)
### 6.1 Governance and SSOT definition
- [ ] **T1** Define canonical identifier grammar + registry ownership (CM+DATA+AI).
- [ ] **T2** Define SSOT decision matrix (authoritative vs derived artifacts).
- [ ] **T3** Define schema versioning policy (compatibility + breaking-change rules).

### 6.2 Enforcement implementation
- [ ] **T4** Confirm CI gates: naming + metadata + schema validation + trace link checks.
- [ ] **T5** Provide a minimal “audit query” script or documented query path (K06→K08 linkage).

### 6.3 Evidence + baseline freeze
- [ ] **T6** Produce minimal evidence pack: `IDs → Schema → Trace → Signed export`.
- [ ] **T7** Record decision, link approvals, update baseline references (CM).

## 7) Outputs / Artifacts
- Identifier standard (ATA 00, TYPE=STD)
- Schema governance policy (ATA 91, TYPE=SCH/STD)
- CI workflow updates + validation logs (evidence)
- Traceability proof artifact (ATA 93)
- Signed export pack reference (ATA 98)

## 8) Dependencies / Risks
- Dependency on **K13** for signing/key management and secure artifact handling.
- Dependency on **K01** if authorities impose specific trace/evidence formats.
- Risk: uncontrolled proliferation of “new IDs/schemas” if CI is not enforced early.

