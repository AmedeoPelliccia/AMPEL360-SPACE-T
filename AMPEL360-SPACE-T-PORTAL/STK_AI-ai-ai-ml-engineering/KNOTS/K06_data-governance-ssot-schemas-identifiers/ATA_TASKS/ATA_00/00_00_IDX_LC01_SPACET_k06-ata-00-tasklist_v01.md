---
title: "K06 ATA 00 Tasklist"
type: IDX
variant: SPACET
status: Draft
knot_id: K06
ata: "00"
lc_or_subucket: "LC01"
---

# K06 — data-governance-ssot-schemas-identifiers
## ATA 00 — Tasklist

## 1. Uncertainty to Resolve (ATA-specific)
Define the **authoritative governance** for:
- Canonical identifiers (parts, docs, baselines, hazards, requirements, datasets, models).
- SSOT rules (what is authoritative, where it lives, how it is versioned).
- Schema/versioning policy used by the whole Space-T repo.

### Decision required
A single CM-approved decision covering:
- Identifier format + registry authority.
- Schema governance + compatibility rules.
- CI gates for validation and auditability.

## 2. Scope Boundary
### In-scope
- File naming + metadata normalization rules for “program-level” artifacts (ATA 00).
- Registries and schema publication mechanism.
- CI validation rules + audit queries.

### Out-of-scope
- Detailed subsystem schemas (handled in ATA 91/93/94+).
- Implementation details of specific tooling (owned by Tooling/Automation backlog unless explicitly pulled in).

## 3. Owners & Stakeholders
- **Primary Owner:** DATA + CM (joint ownership)
- **Contributors:** SE, CERT, CY, OPS, TEST
- **Approvers:** CM WG (final), CERT (if compliance impact)

## 4. Interfaces / Affected Areas
### Affected ATAs (by dependency)
- Direct: ATA 00 (governance), ATA 91 (schemas), ATA 93 (trace graph), ATA 94/95/98 (DPP/SBOM/export packs), ATA 101/109 (sim/test evidence linkage)
- Indirect: Any ATA that emits registries or references IDs

### Authoritative paths (targets)
- `AMPEL360_SPACE-T/P-PROGRAM/ATA_00-GENERAL/`
- `AMPEL360_SPACE-T/N-NEURAL_NETWORKS/ATA_91-*` (schemas)
- `AMPEL360_SPACE-T/N-NEURAL_NETWORKS/ATA_93-*` (traceability graph)
- `AMPEL360_SPACE-T/N-NEURAL_NETWORKS/ATA_94-*` (DPP)
- `AMPEL360_SPACE-T/N-NEURAL_NETWORKS/ATA_95-*` (SBOM/ModelBOM)

## 5. Closure Criteria (Must be explicit)
✅ **Closed when ALL are true:**
1) Identifier standard approved (CM WG) and published.
2) Schema publication/versioning rules published (DATA owner).
3) CI enforcement exists (PR gate) and is documented.
4) At least one “audit query” is reproducible (evidence pack) proving traceability to release artifacts.
5) Baseline update recorded (release note / change record) and linked to affected ATAs.

## 6. Tasks (minimum set)
### 6.1 Define governance and SSOT
- [ ] **T1** Define canonical identifier grammar + registry ownership (CM+DATA).
- [ ] **T2** Define “SSOT decision matrix” (what is authoritative vs derived).
- [ ] **T3** Define schema versioning policy (semver rules, breaking change rules).

### 6.2 Implement enforcement
- [ ] **T4** Add/confirm CI rules: schema validation + naming + metadata lint.
- [ ] **T5** Add “audit query” CLI (or script) for traceability checks (K06→K08 linkage).

### 6.3 Prove and freeze evidence
- [ ] **T6** Create one minimal evidence pack: `IDs → Schema → Trace → Signed export`.
- [ ] **T7** Record decision + baseline: changelog entry + CM approval reference.

## 7. Outputs / Artifacts
- `00_00_STD_LC01_SPACET_identifier-standard_v01.md` (or equivalent)
- `00_00_SCH_LC01_SPACET_schema-governance_v01.md`
- CI workflow updates + validation logs
- Evidence pack link (ATA 93/98)

## 8. Risks / Dependencies
- Dependency on K13 (cyber/key management) for signed exports.
- Dependency on K01 for compliance framing if authorities require specific trace forms.

