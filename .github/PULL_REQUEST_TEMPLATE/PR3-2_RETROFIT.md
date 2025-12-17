# PR^3-2 — RETROFIT (Mass Rename + Cross-Reference Rewrite + PR-Blocking CI)

## Summary
- Purpose: Execute deterministic retrofit to Nomenclature R1.0 (v6.0) across the repository.
- Mode: CI validation becomes **PR-blocking**.
- AoR Owner: CM

## Retrofit Scope
- [ ] Batch renames (git mv)
- [ ] Markdown link rewrites
- [ ] Portal index updates
- [ ] Knot/task index updates
- [ ] Manifest updates (YAML/JSON/CSV references)
- [ ] Exception register updates (explicit)

---

## Mandatory Retrofit Artifacts
- [ ] `rename_map_v6.csv` generated (dry-run first; includes confidence scoring).
- [ ] `retrofit_report_v6.md` produced (totals, broken links fixed, exceptions list, validator evidence).
- [ ] Exception register updated where needed (explicit approvals).

---

## Change Checklist (must be fully satisfied)

### A) Deterministic Mapping & Safety Controls
- [ ] Dry-run mapping generated and reviewed.
- [ ] Low-confidence mappings are flagged for manual review (threshold documented).
- [ ] Renames executed via `git mv` (no delete/recreate).
- [ ] Renames are grouped into atomic commits by subsystem/bucket (no giant monolith unless unavoidable).
- [ ] Rollback strategy documented (revert commits + rename_map retained).

### B) Cross-Reference Rewrite
- [ ] Markdown links updated to new paths.
- [ ] Portal indexes updated and validated.
- [ ] Knot indexes updated and validated.
- [ ] Manifests updated (YAML/JSON/CSV references).

### C) Enforcement (PR-Blocking)
- [ ] Validator runs in **BLOCK** mode in CI (PR fails on violations).
- [ ] Pre-commit hook updated (if needed) to match block semantics locally.

---

## Required Evidence (paste outputs below)

### 1) rename_map_v6.csv Evidence
Provide a short summary and the location of the file in-repo.

```text
rename_map_v6.csv:
  Path:
  Total entries:
  Confidence threshold:
  Low-confidence entries:
  Manual overrides count:
```

### 2) Validator Output (BLOCK)

Paste validator summary (must be zero violations).

```text
COMMAND:
  python validate_nomenclature.py --standard R1.0 --mode block

SUMMARY:
  Total files scanned:
  Violations: 0
  Exemptions applied:
  Exit code: 0
```

### 3) Link Check Output (BLOCK)

Paste link-checker summary (must be zero broken internal links).

```text
COMMAND:
  python tools/link_check.py --scope repo --format summary --mode block

SUMMARY:
  Markdown files scanned:
  Broken internal links: 0
  Exit code: 0
```

### 4) Exception Register Diff (Required if any exceptions exist)

Paste a concise diff excerpt.

```diff
COMMAND:
  git diff -- path/to/exception_register.*

DIFF (excerpt):
  (paste excerpt here)
```

### 5) Retrofit Report Reference

Confirm the report path and key totals.

```text
retrofit_report_v6.md:
  Path:
  Files renamed:
  Links rewritten:
  Manifests updated:
  Exceptions:
```

---

## Risk Controls

* [ ] CI gating proven on this PR (block mode).
* [ ] No residual "known broken" links are left behind.
* [ ] Exceptions are explicit, justified, and CM-approved.

## Approvals

* [ ] CM approval (mandatory)
* [ ] CERT approval (mandatory if TEKNIA credentials/schemas affected)
* [ ] Maintainer approval for large-scale repo changes

## Notes / Follow-ups

* Next PR: **PR^3-3 Predicted Release** (freeze lists/rules + final verification + release notes).
