# PR^3-3 — PREDICTED RELEASE (R1.0 Freeze + Final Verification + Release Notes)

## Summary
- Purpose: Freeze R1.0 governance surface area; publish release notes; prove end-to-end verification.
- Mode: Stable enforcement on PR + main; changes require CM-controlled standard upgrade.

## Freeze Scope
- [ ] Controlled lists frozen (AoR/TYPE/STATUS/MODEL/VARIANT/EXT)
- [ ] Bucket/phase rules frozen (LC vs SB ranges)
- [ ] Exemptions list frozen (explicit only)
- [ ] TEKNIA credential schemas frozen (if in scope)

---

## Change Checklist (must be fully satisfied)

### A) Governance Freeze (R1.0 Locked)
- [ ] Controlled lists are locked and version-tagged as R1.0 baseline.
- [ ] Any future changes require CM-approved standard upgrade (documented in spec).
- [ ] Agent instructions explicitly prohibit new KNOT IDs outside K01..K14.

### B) Verification Gates (Hard Requirements)
- [ ] Validator passes repo-wide with **0 violations**.
- [ ] Link checker passes with **0 broken internal links**.
- [ ] CI passes on PR and main-equivalent checks.

### C) Release Notes / Upgrade Guide
- [ ] Release notes published (what changed, why, how to comply).
- [ ] Upgrade guide published (v5→v6 deltas, examples, common pitfalls).
- [ ] "How to request an exception / new knot" process documented.

---

## Required Evidence (paste outputs below)

### 1) Validator Output (Repo-Wide, 0 violations)
```text
COMMAND:
  python validate_nomenclature.py --standard R1.0 --mode block --scope repo

SUMMARY:
  Total files scanned:
  Violations: 0
  Exemptions applied:
  Exit code: 0
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

If no changes, paste a diff showing no modifications or state explicitly.

```diff
COMMAND:
  git diff -- path/to/exception_register.*

DIFF (excerpt):
  (paste excerpt here, or state "No diff")
```

### 4) Release Notes Reference

```text
Release notes:
  Path:
Upgrade guide:
  Path:
Spec reference:
  Path:
Config baseline:
  Path:
```

---

## Risk Controls

* [ ] No new rename operations introduced in PR^3-3 (freeze/verification only).
* [ ] CI gates are proven stable (no flaky checks introduced).
* [ ] Exceptions process is documented and CM-owned.

## Approvals

* [ ] CM approval (mandatory)
* [ ] CERT approval (mandatory if TEKNIA policy/schema is frozen/updated here)
* [ ] Maintainer approval (release documentation + governance freeze)

## Notes

* Post-release: all nomenclature changes must be via CM-controlled standard upgrade PR (no ad-hoc list edits).
