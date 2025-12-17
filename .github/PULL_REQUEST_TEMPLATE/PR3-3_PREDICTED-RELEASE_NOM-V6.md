# PR^3-3 — PREDICTED RELEASE (Nomenclature v6.0 R1.0 FINAL LOCK — Freeze + Final Verification + Release Notes)

## Summary
- Purpose: Freeze R1.0 FINAL LOCK governance surface area (including v6.0 token allowlists) and prove end-to-end verification.
- Enforcement: Stable PR-blocking CI on PR + main-equivalent checks.
- Governance owner (AoR): CM

## v6.0 Canonical Filename Format (Reference)
`[ATA_ROOT]_[PROJECT]_[PROGRAM]_[FAMILY]_[VARIANT]_[VERSION]_[MODEL]_[BLOCK]_[PHASE]_[KNOT_TASK]_[AoR]__[SUBJECT]_[TYPE]_[ISSUE-REVISION]_[STATUS].[EXT]`

---

## Freeze Scope (R1.0 FINAL LOCK)
- [ ] `FAMILY` allowlist frozen (e.g., Q10/Q100 etc. via CM change control only)
- [ ] `VARIANT` allowlist frozen (GEN/BASELINE/FLIGHTTEST/CERT/MSN/HOV/CUST)
- [ ] `VERSION` allowlist frozen (PLUS/PLUSULTRA brand roots, with optional iteration)
- [ ] `MODEL` allowlist frozen (BB/HW/SW/PR)
- [ ] **R1.0 FINAL LOCK**: VERSION iteration pattern frozen (`^(PLUS|PLUSULTRA)([0-9]{2})?$`)
- [ ] **R1.0 FINAL LOCK**: Conditional SUBJECT prefix rules frozen (CUST, MSN)
- [ ] **R1.0 FINAL LOCK**: Normative length limits frozen (filename: 180, tokens: 12/60/8/10)
- [ ] AoR/TYPE/STATUS/EXT allowlists frozen
- [ ] Bucket/phase rules frozen (LC vs SB ranges)
- [ ] Exemptions list frozen (explicit only)
- [ ] (If in scope) TEKNIA credential schema frozen and enforced (issuance AoR CM/CERT only)

---

## Change Checklist (must be fully satisfied)

### A) Governance Freeze (R1.0 FINAL LOCK locked and documented)
- [ ] Spec explicitly states: changes to `FAMILY/VARIANT/VERSION/MODEL` require CM-approved standard upgrade.
- [ ] Spec explicitly states R1.0 FINAL LOCK immutable semantics:
  - [ ] VARIANT is lane/governance context
  - [ ] VERSION is branding reinforcer with optional iteration
  - [ ] CUST variant requires `cust-<custcode>-` prefix in SUBJECT
  - [ ] MSN variant requires `msn-<serial>-` prefix in SUBJECT
  - [ ] Length limits are normative and enforced
- [ ] Agent instructions explicitly prohibit non-allowlisted values for:
  - [ ] `FAMILY`
  - [ ] `VARIANT`
  - [ ] `VERSION` (brand roots)
  - [ ] `MODEL`
  - [ ] KNOT outside K01..K14
- [ ] Agent instructions explicitly enforce R1.0 FINAL LOCK rules:
  - [ ] VERSION iteration pattern
  - [ ] Conditional SUBJECT prefixes
  - [ ] Length limits
- [ ] Config baseline version tagged/identified as R1.0 FINAL LOCK.

### B) Verification Gates (Hard Requirements)
- [ ] Validator passes repo-wide with **0 violations** (including v6.0 R1.0 token semantics).
- [ ] Link checker passes with **0 broken internal links**.
- [ ] CI passes reliably (no flaky checks introduced).
- [ ] **R1.0 FINAL LOCK specific checks pass**:
  - [ ] All VERSION fields match pattern (brand + optional iteration)
  - [ ] All CUST variants have valid SUBJECT prefixes
  - [ ] All MSN variants have valid SUBJECT prefixes
  - [ ] No length limit violations

### C) Release Notes / Upgrade Guide
- [ ] Release notes published (what changed, why, compliance impact).
- [ ] Upgrade guide published (v5→v6 token mapping guidance: FAMILY/VARIANT/VERSION/MODEL).
- [ ] **R1.0 FINAL LOCK guide** published:
  - [ ] VERSION iteration usage examples
  - [ ] Conditional SUBJECT prefix requirements
  - [ ] Length limit policy
- [ ] Exception/new-knot process documented (CM-owned).

---

## Required Evidence (paste outputs below)

### 1) Validator Output (Repo-Wide, 0 violations; v6.0 R1.0 tokens validated)
```text
COMMAND:
  python validate_nomenclature.py --standard v6.0 --mode block --check-all

SUMMARY:
  Total files scanned:
  Violations: 0
  Exemptions applied:
  Exit code: 0

Token compliance (spot-check summary):
  FAMILY allowlist violations: 0
  VARIANT allowlist violations: 0
  VERSION pattern violations: 0
  MODEL allowlist violations: 0
  
R1.0 FINAL LOCK compliance:
  Conditional prefix violations: 0
  Length limit violations: 0
```

### 2) Link Check Output (Repo-Wide, 0 broken links)

```text
COMMAND:
  python tools/link_check.py --scope repo --mode block --format summary

SUMMARY:
  Markdown files scanned:
  Broken internal links: 0
  Exit code: 0
```

### 3) Exception Register Diff (Required even if "no changes")

```diff
COMMAND:
  git diff -- path/to/exception_register.*

DIFF (excerpt):
  (paste excerpt here, or state "No diff")
```

### 4) Release Notes References (Required)

```text
Release notes:
  Path:
Upgrade guide:
  Path:
R1.0 FINAL LOCK guide:
  Path:
Spec reference:
  Path:
Config baseline:
  Path:
```

### 5) R1.0 FINAL LOCK Verification Examples

```text
# Verify VERSION with iteration
COMMAND: python validate_nomenclature.py --standard v6.0 --check-all | grep -i "version"
Result: 0 violations

# Verify conditional SUBJECT prefixes
COMMAND: python validate_nomenclature.py --standard v6.0 --check-all | grep -i "cust\|msn"
Result: 0 violations

# Verify length limits
COMMAND: python validate_nomenclature.py --standard v6.0 --check-all | grep -i "length"
Result: 0 violations

# Sample valid R1.0 files (spot check):
- 27_AMPEL360_SPACET_Q10_GEN_PLUS_BB_OPS_LC03_K06_SE__thermal-loop_STD_I01-R01_ACTIVE.md
- 27_AMPEL360_SPACET_Q10_GEN_PLUS01_BB_OPS_LC03_K06_SE__thermal-loop_STD_I01-R01_ACTIVE.md
- 27_AMPEL360_SPACET_Q10_CUST_PLUS_SW_OPS_LC03_K06_SE__cust-airbus-thermal_STD_I01-R01_DRAFT.md
- 27_AMPEL360_SPACET_Q100_MSN_PLUSULTRA02_HW_OPS_LC03_K06_SE__msn-000123-thermal_STD_I01-R01_ACTIVE.md

All: VALID ✓
```

---

## Risk Controls

* [ ] No new mass-renames introduced in PR^3-3 (freeze/verification only).
* [ ] CI gates proven stable on at least one re-run.
* [ ] R1.0 FINAL LOCK semantics are immutable and cannot be changed without major version bump.

## Approvals

* [ ] CM approval (mandatory)
* [ ] CERT approval (mandatory if TEKNIA policy/schema is frozen/updated here)
* [ ] Maintainer approval (governance freeze + documentation)

## R1.0 FINAL LOCK Commitments

By approving this PR, the following are **IMMUTABLE** without a major standard revision:

1. **VARIANT** semantics: Governance lane context (cannot change meaning)
2. **VERSION** semantics: Branding reinforcer with optional 2-digit iteration
3. **Conditional SUBJECT prefixes**: CUST and MSN requirements
4. **Length limits**: filename ≤180, BLOCK ≤12, SUBJECT ≤60, TYPE ≤8, AoR ≤10
5. **Canonical format**: 16-field structure is frozen

Future evolution is **strictly additive**: new allowlist values only, via CM approval.

## Notes / Follow-ups

* Post-release: Monitor for any unforeseen edge cases in first 30 days.
* Future extensions: New FAMILY/VARIANT/VERSION/MODEL values via CM change control.
* KNOT expansion: Requires major standard revision (v7.0).

---

**Document Control**

* **Version**: 6.0
* **Revision**: R1.0
* **Status**: FINAL LOCK
* **Date**: 2025-12-17
* **Owner**: Configuration Management WG
* **Approvers**: CM WG, CERT (for TEKNIA policy)
* **Distribution**: All AMPEL360 Space-T stakeholders
* **Next Review**: Upon request for allowlist extension or KNOT expansion

---

**END OF PR^3 SEQUENCE**
