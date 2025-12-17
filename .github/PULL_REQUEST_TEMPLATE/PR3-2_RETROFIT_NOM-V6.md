# PR^3-2 — RETROFIT (Nomenclature v6.0 R1.0 FINAL LOCK — Mass Rename + Cross-Refs + PR-blocking CI)

## Summary
- Purpose: Retrofit repo to v6.0 R1.0 by deterministic mapping (filenames + references).
- Enforcement: CI validator in **BLOCK** mode; PR fails on violations.
- Governance owner (AoR): CM

## v6.0 Canonical Filename Format (Reference)
`[ATA_ROOT]_[PROJECT]_[PROGRAM]_[FAMILY]_[VARIANT]_[VERSION]_[MODEL]_[BLOCK]_[PHASE]_[KNOT_TASK]_[AoR]__[SUBJECT]_[TYPE]_[ISSUE-REVISION]_[STATUS].[EXT]`

---

## Retrofit Scope
- [ ] Batch renames (git mv) to include required v6.0 tokens: `FAMILY/VARIANT/VERSION/MODEL/ISSUE-REVISION`
- [ ] Apply R1.0 FINAL LOCK rules (VERSION iteration, conditional SUBJECT prefixes)
- [ ] Markdown link rewrites
- [ ] Portal index updates
- [ ] Knot/task index updates
- [ ] Manifest updates (YAML/JSON/CSV references)
- [ ] Exception register updates (explicit, CM-approved)

---

## Mandatory Retrofit Artifacts
- [ ] `rename_map_v6.csv` generated (dry-run first) and committed.
- [ ] `retrofit_report_v6.md` produced and committed.
- [ ] Exception register updated where needed (explicit approvals recorded).

---

## Change Checklist (must be fully satisfied)

### A) rename_map_v6.csv (Deterministic mapping includes v6.0 R1.0 tokens)
- [ ] `rename_map_v6.csv` has columns:
  - [ ] `old_path`
  - [ ] `new_path`
  - [ ] `confidence`
  - [ ] `rule_applied`
  - [ ] `notes`
- [ ] Mapping rules explicitly handle:
  - [ ] inference/assignment of `FAMILY` (e.g., Q10/Q100 allowlist)
  - [ ] inference/assignment of `VARIANT` (GEN/BASELINE/FLIGHTTEST/CERT/MSN/HOV/CUST)
  - [ ] inference/assignment of `VERSION` (PLUS/PLUSULTRA, no iteration by default)
  - [ ] inference/assignment of `MODEL` (BB/HW/SW/PR)
  - [ ] inference/assignment of `ISSUE-REVISION` (default: I01-R01)
  - [ ] **R1.0**: Apply conditional `SUBJECT` prefixes for CUST/MSN variants (manual review if needed)
  - [ ] **R1.0**: Validate length limits before rename (flag violations)
- [ ] Low-confidence rows are flagged and manually reviewed (threshold documented).
- [ ] `new_path` conforms to v6.0 R1.0 structure (including mandatory `__`).

### B) Rename Execution Safety Controls
- [ ] Renames executed via `git mv` (no delete/recreate).
- [ ] Atomic commits by subsystem/bucket (unless justified).
- [ ] Rollback strategy documented (revert commits + preserve rename_map).

### C) Cross-Reference Rewrite
- [ ] Markdown links updated to new filenames.
- [ ] Portal indexes updated and validated.
- [ ] Knot indexes updated and validated.
- [ ] Manifests updated (YAML/JSON/CSV references).

### D) Enforcement (BLOCK mode with R1.0 FINAL LOCK)
- [ ] CI runs nomenclature validator in **BLOCK** mode for v6.0 R1.0.
- [ ] Pre-commit hook matches v6.0 R1.0 rules (optional but recommended).

---

## Required Evidence (paste outputs below)

### 1) rename_map_v6.csv Evidence
```text
rename_map_v6.csv:
  Path:
  Total entries:
  Confidence threshold:
  Low-confidence entries:
  Manual overrides count:

v6.0 token coverage:
  FAMILY assigned (%):
  VARIANT assigned (%):
  VERSION assigned (%):
  MODEL assigned (%):
  ISSUE-REVISION assigned (%):

R1.0 FINAL LOCK compliance:
  Conditional SUBJECT prefixes applied:
  Length limit violations flagged:
```

### 2) Validator Output (BLOCK; MUST be 0 violations)

```text
COMMAND:
  python validate_nomenclature.py --standard v6.0 --mode block --check-all

SUMMARY:
  Total files scanned:
  Violations: 0
  Exemptions applied:
  Exit code: 0
```

### 3) Link Check Output (BLOCK; MUST be 0 broken internal links)

```text
COMMAND:
  python tools/link_check.py --scope repo --format summary --mode block

SUMMARY:
  Markdown files scanned:
  Broken internal links: 0
  Exit code: 0
```

### 4) Exception Register Diff (Required if any exceptions exist)

```diff
COMMAND:
  git diff -- path/to/exception_register.*

DIFF (excerpt):
  (paste excerpt here, or state "No changes")
```

### 5) Retrofit Report Reference (Required)

```text
retrofit_report_v6.md:
  Path:
  Files renamed:
  Links rewritten:
  Manifests updated:
  Exceptions (count):
  R1.0 FINAL LOCK issues resolved:
  Notes:
```

### 6) R1.0 FINAL LOCK Retrofit Examples

```text
# Example v5.0 → v6.0 R1.0 rename
OLD: 27_AMPEL360_SPACET_PLUS_OPS_LC03_K06_SE__thermal-loop_STD_v01_ACTIVE.md
NEW: 27_AMPEL360_SPACET_Q10_GEN_PLUS_BB_OPS_LC03_K06_SE__thermal-loop_STD_I01-R01_ACTIVE.md

# Example CUST variant rename (manual review required)
OLD: 27_AMPEL360_SPACET_PLUS_OPS_LC03_K06_SE__airbus-thermal_STD_v01_ACTIVE.md
NEW: 27_AMPEL360_SPACET_Q10_CUST_PLUS_SW_OPS_LC03_K06_SE__cust-airbus-thermal_STD_I01-R01_ACTIVE.md
     ^ Applied conditional SUBJECT prefix for CUST variant

# Example with VERSION iteration (if applicable)
NEW: 27_AMPEL360_SPACET_Q10_GEN_PLUS01_BB_OPS_LC03_K06_SE__thermal-loop_STD_I01-R01_ACTIVE.md
     ^ Optional iteration applied
```

---

## Risk Controls

* [ ] CI gating proven on this PR (block mode).
* [ ] No residual broken links remain.
* [ ] Exceptions are explicit, justified, and CM-approved.
* [ ] R1.0 FINAL LOCK rules enforced: length limits, conditional prefixes validated.

## Approvals

* [ ] CM approval (mandatory)
* [ ] CERT approval (mandatory if TEKNIA schemas/credentials are in scope)
* [ ] Maintainer approval for large-scale repo change

## Notes / Follow-ups

* Next: PR^3-3 Predicted Release (freeze lists/rules + final verification + release notes).
* R1.0 FINAL LOCK ensures no future token-level redesign needed.
