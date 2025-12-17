# PR^3-1 — PRE-RELEASE (Nomenclature R1.0 / v6.0 Spec + Automation in Warn Mode)

## Summary
- Purpose: Publish Nomenclature R1.0 (v6.0) specification + config + tooling updates.
- Mode: CI validation runs in **WARN/REPORT** (not PR-blocking yet).
- AoR Owner: CM

## Scope (what this PR changes)
- [ ] Normative spec document(s)
- [ ] Versioned config allowlists/rules
- [ ] Validator implementation updates
- [ ] CI workflow updates (warn/report)
- [ ] Pre-commit hook updates
- [ ] Scaffold generator updates
- [ ] Agent instructions updates
- [ ] Inventory report generation (violations snapshot)

---

## Change Checklist (must be fully satisfied)

### A) Spec & Governance
- [ ] `Nomenclature R1.0 (v6.0)` normative document published (fields + rules + semantics).
- [ ] Quick reference published (examples + do/don't).
- [ ] Controlled lists are versioned and committed (AoR/TYPE/STATUS/MODEL/VARIANT/EXT).
- [ ] Bucket/phase mapping rules are defined (LC vs SB ranges) and committed.
- [ ] Exemptions policy is explicit and committed (no implicit exemptions).

### B) Automation & CI (Warn Mode)
- [ ] `validate_nomenclature.py` supports v6.0 parsing + semantic checks (K01..K14, AoR allowlist, `__`, MODEL, VERSION pattern, ISSUE-REVISION).
- [ ] CI workflow updated to run validator in **WARN/REPORT** mode.
- [ ] Pre-commit hook updated to run validator on changed files.
- [ ] `scripts/scaffold.py` generates v6.0 compliant filenames.

### C) Repository Inventory (Required)
- [ ] Inventory report is generated and committed (current naming violations, by category).
- [ ] Inventory report includes estimated rename volume and top-offenders list.

---

## Required Evidence (paste outputs below)

### 1) Validator Output (Warn/Report)
Paste the validator summary output (include command and totals).

```text
COMMAND:
  python validate_nomenclature.py --standard R1.0 --mode warn --report out/nomenclature_report.txt

SUMMARY:
  Total files scanned:
  Violations:
    - missing_model_field:
    - invalid_version_pattern:
    - missing_issue_revision:
    - invalid_knot:
    - invalid_aor:
    - missing_double_underscore:
    - invalid_subject:
    - invalid_type:
    - invalid_status:
    - invalid_ext:
    - phase_bucket_mismatch:
  Exemptions applied:
  Exit code:
```

### 2) Link Check Output (if link checker is introduced here)

If link checker is added in PR^3-1, paste summary output.

```text
COMMAND:
  python tools/link_check.py --scope repo --format summary

SUMMARY:
  Markdown files scanned:
  Broken internal links:
  Exit code:
```

### 3) Exception Register Diff (if present)

If an exception register exists/changes in this PR, paste a concise `git diff` excerpt.

```diff
COMMAND:
  git diff -- path/to/exception_register.*

DIFF (excerpt):
  (paste excerpt here)
```

---

## Risk / Rollback

* [ ] No mass-renames performed in PR^3-1.
* [ ] Tooling changes are isolated and revertible (single PR rollback).

## Approvals

* [ ] CM review completed
* [ ] CERT review completed (only if credential policy/schema changed)
* [ ] Maintainer sign-off for CI changes

## Notes / Follow-ups

* Next PR: **PR^3-2 Retrofit** (rename_map.csv + mass rename + cross-ref rewrite, CI becomes PR-blocking).
