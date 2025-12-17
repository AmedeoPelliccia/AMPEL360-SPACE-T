# PR^3-1 — PRE-RELEASE (Nomenclature v6.0 R1.0 FINAL LOCK — Spec + Config + Automation in WARN mode)

## Summary
- Purpose: Publish Nomenclature v6.0 (R1.0 FINAL LOCK) normative spec + config + tooling updates.
- Enforcement: CI runs validator in **WARN/REPORT** (not PR-blocking yet).
- Governance owner (AoR): CM

## v6.0 Canonical Filename Format (Reference)
`[ATA_ROOT]_[PROJECT]_[PROGRAM]_[FAMILY]_[VARIANT]_[VERSION]_[MODEL]_[BLOCK]_[PHASE]_[KNOT_TASK]_[AoR]__[SUBJECT]_[TYPE]_[ISSUE-REVISION]_[STATUS].[EXT]`

---

## Scope (what this PR changes)
- [ ] Normative spec document(s) for v6.0 R1.0
- [ ] Versioned nomenclature config (v6_0.yaml with R1.0 FINAL LOCK)
- [ ] Validator implementation updates (parse + semantics)
- [ ] CI workflow updates (warn/report)
- [ ] Pre-commit hook updates
- [ ] Scaffold generator updates (v6.0)
- [ ] Agent instructions updates
- [ ] Inventory report generation (violations snapshot)

---

## Change Checklist (must be fully satisfied)

### A) Spec & Governance (v6.0 tokens explicitly defined + R1.0 FINAL LOCK)
- [ ] `FAMILY` defined as quantum-inspired + pax payload numbering (e.g., `Q10`, `Q100`) with pattern + allowlist rules.
- [ ] `VARIANT` defined as governance lane token with controlled list (e.g., `GEN`, `BASELINE`, `FLIGHTTEST`, `CERT`, `MSN`, `HOV`, `CUST`) and normalization rules (no spaces).
- [ ] `VERSION` defined as branding reinforcer with controlled list (e.g., `PLUS`, `PLUSULTRA`) **plus optional 2-digit iteration** (e.g., `PLUS01`, `PLUSULTRA02`).
- [ ] `MODEL` defined as artifact domain with controlled list (`BB`, `HW`, `SW`, `PR`).
- [ ] **R1.0 FINAL LOCK**: Conditional `SUBJECT` prefix rules documented:
  - [ ] `VARIANT=CUST` requires `SUBJECT` to start with `cust-<custcode>-` (custcode: 2-12 alphanumeric)
  - [ ] `VARIANT=MSN` requires `SUBJECT` to start with `msn-<serial>-` (serial: 3-6 digits)
- [ ] **R1.0 FINAL LOCK**: Normative length limits documented:
  - [ ] Max filename length: 180 characters
  - [ ] Max BLOCK: 12 chars
  - [ ] Max SUBJECT: 60 chars
  - [ ] Max TYPE: 8 chars
  - [ ] Max AoR: 10 chars
- [ ] AoR allowlist published (portal entry points) and referenced by spec.
- [ ] KNOT governance published (K01..K14 only; optional `-T###` only).
- [ ] `__` double underscore rule published.
- [ ] `ISSUE-REVISION` rule published (e.g., `I##-R##`).
- [ ] Extension allowlist published (GitHub-first).
- [ ] Exemptions policy is explicit and versioned (no implicit exemptions).

### B) Config Packaging (versioned, CI-consumed, R1.0 FINAL LOCK)
- [ ] `config/nomenclature/v6_0.yaml` committed with status "FINAL LOCK".
- [ ] Allowlist entries present for: `FAMILY`, `VARIANT`, `VERSION` (brand roots), `MODEL`, `AoR`, `TYPE`, `STATUS`, `EXT`.
- [ ] `patterns` section includes:
  - [ ] `version`: `^(PLUS|PLUSULTRA)([0-9]{2})?$`
  - [ ] `subject_prefix_for_variant.CUST`: `^cust-[a-z0-9]{2,12}-`
  - [ ] `subject_prefix_for_variant.MSN`: `^msn-[0-9]{3,6}-`
- [ ] `limits` section includes:
  - [ ] `filename_max_len`: 180
  - [ ] `token_max_len`: block (12), subject (60), type (8), aor (10)
- [ ] Bucket/phase mapping rules included (LC01..LC14 vs SBxx ranges).
- [ ] Explicit exemptions list included (empty is acceptable, implicit is not).

### C) Automation & CI (WARN mode + R1.0 FINAL LOCK enforcement)
- [ ] `validate_nomenclature.py` updated to v6.0 R1.0:
  - [ ] Parses all tokens including `FAMILY/VARIANT/VERSION/MODEL`
  - [ ] Enforces allowlists for `FAMILY/VARIANT/MODEL`
  - [ ] **R1.0**: Validates `VERSION` pattern (brand + optional 2-digit iteration)
  - [ ] **R1.0**: Validates conditional `SUBJECT` prefixes for `CUST` and `MSN` variants
  - [ ] **R1.0**: Enforces normative length limits (filename, BLOCK, SUBJECT, TYPE, AoR)
  - [ ] Enforces K01..K14 only (+ optional `-T###`)
  - [ ] Enforces AoR allowlist
  - [ ] Enforces mandatory `__`
  - [ ] Enforces `ISSUE-REVISION` format
  - [ ] Enforces extension allowlist
  - [ ] Enforces phase/bucket compatibility rules
- [ ] CI workflow runs validator in **WARN/REPORT** mode and publishes summary.
- [ ] `scripts/scaffold.py` generates v6.0 filenames with required tokens and allowlist validation.
- [ ] Pre-commit hook updated to run validator on changed files.

### D) Repository Inventory (Required)
- [ ] Inventory report generated and committed: counts of violations by category, including:
  - [ ] invalid_family
  - [ ] invalid_variant
  - [ ] invalid_version (including iteration pattern)
  - [ ] invalid_model
  - [ ] invalid_knot
  - [ ] invalid_aor
  - [ ] missing_double_underscore
  - [ ] invalid_issue_revision
  - [ ] invalid_subject (including prefix violations)
  - [ ] invalid_type
  - [ ] invalid_status
  - [ ] invalid_ext
  - [ ] phase_bucket_mismatch
  - [ ] **R1.0**: length_limit_exceeded (filename, tokens)
  - [ ] **R1.0**: conditional_prefix_missing (CUST/MSN)

---

## Required Evidence (paste outputs below)

### 1) Validator Output (WARN/REPORT)
```text
COMMAND:
  python validate_nomenclature.py --standard v6.0 --mode warn --check-all

SUMMARY:
  Total files scanned:
  Violations (by category):
    invalid_family:
    invalid_variant:
    invalid_version:
    invalid_model:
    invalid_knot:
    invalid_aor:
    missing_double_underscore:
    invalid_issue_revision:
    invalid_subject:
    conditional_prefix_missing:
    length_limit_exceeded:
    invalid_type:
    invalid_status:
    invalid_ext:
    phase_bucket_mismatch:
  Exemptions applied:
  Exit code:
```

### 2) Inventory Report Reference

```text
Inventory report:
  Path:
  Generated at (UTC):
  Top offending directories:
  Estimated rename volume:
```

### 3) Exception Register Diff (if present)

```diff
COMMAND:
  git diff -- path/to/exception_register.*

DIFF (excerpt):
  (paste excerpt here, or state "No changes")
```

### 4) R1.0 FINAL LOCK Validation Examples

```text
# Test VERSION with iteration
python validate_nomenclature.py --standard v6.0 \
  "27_AMPEL360_SPACET_Q10_GEN_PLUS01_BB_OPS_LC03_K06_SE__thermal-loop_STD_I01-R01_ACTIVE.md"
Result: [PASS/FAIL]

# Test CUST variant with required prefix
python validate_nomenclature.py --standard v6.0 \
  "27_AMPEL360_SPACET_Q10_CUST_PLUS_SW_OPS_LC03_K06_SE__cust-airbus-thermal_STD_I01-R01_DRAFT.md"
Result: [PASS/FAIL]

# Test CUST variant WITHOUT required prefix (should fail)
python validate_nomenclature.py --standard v6.0 \
  "27_AMPEL360_SPACET_Q10_CUST_PLUS_SW_OPS_LC03_K06_SE__thermal-loop_STD_I01-R01_DRAFT.md"
Result: [PASS/FAIL]
Error: VARIANT 'CUST' requires SUBJECT to start with 'cust-<custcode>-'

# Test MSN variant with required prefix
python validate_nomenclature.py --standard v6.0 \
  "27_AMPEL360_SPACET_Q100_MSN_PLUSULTRA02_HW_OPS_LC03_K06_SE__msn-000123-thermal_STD_I01-R01_ACTIVE.md"
Result: [PASS/FAIL]

# Test length limit enforcement
python validate_nomenclature.py --standard v6.0 \
  "<filename exceeding 180 chars>"
Result: [PASS/FAIL]
Error: Filename length exceeds maximum (180 chars)
```

---

## Risk / Rollback

* [ ] No mass-renames performed in PR^3-1.
* [ ] Tooling/config changes are revertible and isolated.
* [ ] R1.0 FINAL LOCK semantics are immutable and documented.

## Approvals

* [ ] CM review completed (mandatory)
* [ ] CERT review completed (only if TEKNIA credential schema/policy changes)

## Notes / Follow-ups

* Next: PR^3-2 Retrofit (rename_map.csv + mass rename + cross-ref rewrite, CI becomes PR-blocking).
* R1.0 FINAL LOCK ensures future evolution is strictly additive (allowlist expansion only).
