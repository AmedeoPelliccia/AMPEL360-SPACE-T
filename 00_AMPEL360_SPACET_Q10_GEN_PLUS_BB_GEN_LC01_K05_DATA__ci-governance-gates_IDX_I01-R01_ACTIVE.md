---
title: "CI/CD Governance Gates Index"
type: IDX
variant: "SPACET"
indexed_content: "CI/CD gates, validation scripts, governance workflows"
status: Normative
owner: "Configuration Management WG (Tooling Authority)"
---

# Index: CI/CD Governance Gates

## Overview

This index catalogs all **CI/CD governance gates** implemented to enforce nomenclature standards, schema registration, trace integrity, and approval requirements for governance-impacting changes. It serves as the authoritative reference for:

1. **Automated validation gates** (pre-commit, PR checks)
2. **Manual review gates** (CM approval, governance review)
3. **Validation scripts** and their locations
4. **Workflow configurations** and trigger conditions
5. **Failure remediation procedures**

## Index Structure

### Category A: Pre-Commit Automated Gates

| Gate ID | Gate Name | Script/Tool | Enforcement Level | Status | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GATE-001** | Nomenclature Validation | `validate_nomenclature.py` | BLOCKING | Active | Validates all files against v3.0 standard |
| **GATE-002** | Schema Registration Check | `scripts/validate_schema_registry.py` | BLOCKING | Active | Verifies schema refs exist in ATA 91 |
| **GATE-003** | Trace Link Integrity | `scripts/validate_trace_links.py --skip-templates` | BLOCKING | Active | Validates trace link targets exist, skips template placeholders and planned structure |
| **GATE-004** | Namespace Deduplication | `scripts/check_ata99_registry.py` | BLOCKING | Planned | Prevents duplicate IDs across namespaces |
| **GATE-005** | Identifier Grammar Check | `scripts/validate_identifiers.py` | BLOCKING | Planned | Validates canonical ID format |

### Category B: Pull Request Review Gates

| Gate ID | Gate Name | Script/Tool | Enforcement Level | Status | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GATE-006** | Governance Change Detection | Built into governance-gates.yml | LABELING | Active | Auto-labels PRs requiring CM review |
| **GATE-007** | Breaking Schema Change Detection | `scripts/detect_schema_breaking_changes.py` | BLOCKING | Planned | Requires migration plan for breaking changes |
| **GATE-008** | Evidence Link Validation | `scripts/validate_evidence_links.py` | WARNING | Planned | Checks evidence pack integrity |
| **GATE-009** | TYPE Code Detection | `scripts/detect_new_types.py` | WARNING | Active | Alerts on unapproved TYPE codes |

### Category C: Manual Approval Gates

| Gate ID | Gate Name | Approver(s) | Trigger Condition | Status | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GATE-010** | CM WG Approval | CM WG consensus | Governance-impacting changes | Active | Changes to STD, SCH, TRC, NS files |
| **GATE-011** | ATA 91 Schema Approval | ATA 91 Lead | New or modified schemas | Planned | Schema registry changes |
| **GATE-012** | ATA 93 Trace Approval | ATA 93 Lead | Trace semantics changes | Planned | Trace link type/rule changes |
| **GATE-013** | ATA 99 Namespace Approval | ATA 99 Lead | Namespace add/remove | Planned | Namespace registry changes |
| **GATE-014** | Baseline Approval | Baseline Manager + CM WG | Baseline creation/update | Planned | Before tagging baseline |

### Category D: Periodic Audit Gates

| Gate ID | Gate Name | Script/Tool | Frequency | Status | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GATE-015** | SSOT Ownership Audit | `scripts/audit_ssot_ownership.py` | Quarterly | Planned | Verifies SSOT matrix compliance |
| **GATE-016** | Staleness Detection | `scripts/check_staleness.py` | Weekly | Planned | Detects stale derived artifacts |
| **GATE-017** | Shadow Registry Detection | `scripts/detect_shadow_registries.py` | Weekly | Planned | Finds uncoordinated ID lists |
| **GATE-018** | Trace Coverage Report | `scripts/generate_trace_coverage.py` | On-baseline | Planned | Ensures min coverage thresholds |

## Quick Reference

### By Enforcement Level

- **BLOCKING (merge prevention):** GATE-001, GATE-002, GATE-003, GATE-004, GATE-005, GATE-007
- **LABELING (PR labels):** GATE-006
- **WARNING (non-blocking alerts):** GATE-008, GATE-009
- **MANUAL (human approval):** GATE-010, GATE-011, GATE-012, GATE-013, GATE-014
- **AUDIT (periodic reports):** GATE-015, GATE-016, GATE-017, GATE-018

### By Status

- **Active (implemented):** GATE-001, GATE-002, GATE-003, GATE-006, GATE-009, GATE-010
- **Planned (to be implemented):** GATE-004, GATE-005, GATE-007, GATE-008, GATE-011, GATE-012, GATE-013, GATE-014, GATE-015, GATE-016, GATE-017, GATE-018

### By Responsible Team

- **CI Automation:** GATE-001 through GATE-009, GATE-015 through GATE-018
- **CM WG:** GATE-010
- **ATA 91 (Schemas):** GATE-011
- **ATA 93 (Trace):** GATE-012
- **ATA 99 (Namespaces):** GATE-013
- **Baseline Manager:** GATE-014

## Cross-Reference Matrix

| Gate | Related Policy | Related Workflow | Dependencies |
| :--- | :--- | :--- | :--- |
| GATE-001 | Nomenclature Standard v3.0 | `.github/workflows/nomenclature-validation.yml` | `validate_nomenclature.py` |
| GATE-002 | Governance Reference Policy §4.2 | `.github/workflows/governance-gates.yml` | ATA 91 schema registry |
| GATE-003 | Governance Reference Policy §5.3 | `.github/workflows/governance-gates.yml` | `scripts/validate_trace_links.py`, `docs/GATE-003-TRACE-LINK-VALIDATION.md` |
| GATE-004 | Identifier Grammar §4.5.2 | Planned: `.github/workflows/governance-gates.yml` | ATA 99 namespace registry |
| GATE-005 | Identifier Grammar §4.1 | Planned: `.github/workflows/governance-gates.yml` | None |
| GATE-006 | Governance Reference Policy §6.3 | `.github/workflows/governance-gates.yml` | CM WG approval list |
| GATE-007 | Governance Reference Policy §4.3 | Planned: `.github/workflows/governance-gates.yml` | ATA 91 schema versioning |
| GATE-008 | Governance Reference Policy §7.1 | Planned: `.github/workflows/governance-gates.yml` | Evidence pack index |
| GATE-009 | Nomenclature Standard v3.0 §4.3 | `.github/workflows/detect-new-types.yml` | TYPE vocabulary list |
| GATE-010 | SSOT Decision Matrix §5.1 | Manual PR review process | CM WG roster |

## Workflow Configurations

### Active Workflows

#### 1. Nomenclature Validation Workflow

**File:** `.github/workflows/nomenclature-validation.yml`  
**Gates:** GATE-001  
**Trigger:** Push/PR to any branch  
**Enforcement:** BLOCKING

**Configuration:**
```yaml
name: Nomenclature Standard Validation
on:
  push:
    branches: ['**']
  pull_request:
    branches: ['**']
jobs:
  validate-nomenclature:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.x'
      - name: Validate all files
        run: python validate_nomenclature.py --check-all --strict --verbose
```

#### 2. New TYPE Detection Workflow

**File:** `.github/workflows/detect-new-types.yml`  
**Gates:** GATE-009  
**Trigger:** Push/PR, weekly schedule, manual dispatch  
**Enforcement:** WARNING (issues created for new TYPEs)

**Configuration:**
```yaml
name: Detect New TYPE Codes
on:
  push:
  pull_request:
  schedule:
    - cron: '0 9 * * 1'  # Weekly on Monday 9:00 UTC
  workflow_dispatch:
jobs:
  detect-new-types:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
      - name: Detect new TYPE codes
        run: python scripts/detect_new_types.py --directory .
      - name: Generate extension guide
        run: python scripts/detect_new_types.py --auto-suggest
      - name: Create issue for new TYPEs
        uses: actions/github-script@v7
        # [Creates/updates issue with detected TYPEs]
```

### Planned Workflows

#### 3. Governance Gates Workflow (Comprehensive)

**File:** `.github/workflows/governance-gates.yml` (PLANNED)  
**Gates:** GATE-002, GATE-003, GATE-004, GATE-005, GATE-006, GATE-007, GATE-008  
**Trigger:** Pull request to main/develop  
**Enforcement:** BLOCKING + LABELING

**Proposed Configuration:**
```yaml
name: Governance Gates

on:
  pull_request:
    branches: ['main', 'develop']

jobs:
  governance-checks:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      
      - uses: actions/setup-python@v5
        with:
          python-version: '3.x'
      
      - name: Nomenclature Validation (GATE-001)
        run: python validate_nomenclature.py --check-all --strict
      
      - name: Identifier Grammar Check (GATE-005)
        run: python scripts/validate_identifiers.py --all
      
      - name: Schema Registration Check (GATE-002)
        run: python scripts/check_schema_registration.py --registry ATA91
      
      - name: Trace Integrity Check (GATE-003)
        run: python scripts/check_trace_integrity.py --registry ATA93
      
      - name: Namespace Dedup Check (GATE-004)
        run: python scripts/check_ata99_registry.py --deduplicate
      
      - name: Detect Governance Changes (GATE-006)
        id: governance
        run: |
          CHANGED_FILES=$(git diff --name-only origin/${{ github.base_ref }}...${{ github.sha }})
          python scripts/detect_governance_changes.py --files $CHANGED_FILES
          if [ $? -eq 1 ]; then
            echo "governance_change=true" >> $GITHUB_OUTPUT
          fi
      
      - name: Label PR for Governance Review
        if: steps.governance.outputs.governance_change == 'true'
        uses: actions/github-script@v7
        with:
          script: |
            github.rest.issues.addLabels({
              owner: context.repo.owner,
              repo: context.repo.repo,
              issue_number: context.issue.number,
              labels: ['governance-review-required']
            });
            github.rest.issues.createComment({
              owner: context.repo.owner,
              repo: context.repo.repo,
              issue_number: context.issue.number,
              body: '⚠️ **Governance change detected**\n\nThis PR modifies governance-impacting files and requires CM WG approval before merge.'
            });
      
      - name: Detect Breaking Schema Changes (GATE-007)
        run: python scripts/detect_schema_breaking_changes.py --registry ATA91
      
      - name: Validate Evidence Links (GATE-008)
        run: python scripts/validate_evidence_links.py --all
        continue-on-error: true  # WARNING level
```

#### 4. Baseline Readiness Workflow

**File:** `.github/workflows/baseline-readiness.yml` (PLANNED)  
**Gates:** GATE-014, GATE-018  
**Trigger:** Manual dispatch (on baseline request)  
**Enforcement:** BLOCKING (prevents baseline tag if failed)

**Proposed Configuration:**
```yaml
name: Baseline Readiness Check

on:
  workflow_dispatch:
    inputs:
      baseline_id:
        description: 'Baseline identifier (e.g., BL-2025-12-01)'
        required: true

jobs:
  baseline-readiness:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Generate Trace Coverage Report (GATE-018)
        run: |
          python scripts/generate_trace_coverage.py --baseline ${{ github.event.inputs.baseline_id }} --output coverage_report.md
      
      - name: Check Coverage Thresholds
        run: |
          python scripts/check_coverage_thresholds.py --report coverage_report.md
      
      - name: Validate Evidence Completeness
        run: |
          python scripts/validate_evidence_completeness.py --baseline ${{ github.event.inputs.baseline_id }}
      
      - name: Upload Readiness Report
        uses: actions/upload-artifact@v4
        with:
          name: baseline-readiness-report
          path: coverage_report.md
```

#### 5. Weekly Audit Workflow

**File:** `.github/workflows/weekly-audit.yml` (PLANNED)  
**Gates:** GATE-015, GATE-016, GATE-017  
**Trigger:** Weekly schedule (Sunday night)  
**Enforcement:** REPORTING (creates issues for violations)

**Configuration (Active):**

**File:** `.github/workflows/weekly-governance-audit.yml`

```yaml
name: Weekly Governance Audit

on:
  schedule:
    - cron: '0 0 * * 0'  # Sunday at midnight UTC
  workflow_dispatch:

jobs:
  audit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: GATE-003 - Trace Link Validation (Weekly Scan)
        run: python scripts/validate_trace_links.py --check-all --verbose
        continue-on-error: true
      
      - name: GATE-016 - Staleness Detection
        run: python scripts/check_staleness.py --all  # Planned
        continue-on-error: true
      
      - name: GATE-017 - Shadow Registry Detection
        run: python scripts/detect_shadow_registries.py --namespaces ATA99  # Planned
        continue-on-error: true
      
      - name: GATE-002 - Schema Registry Audit
        run: python scripts/validate_schema_registry.py --check-all --verbose
        continue-on-error: true
      
      - name: GATE-001 - Nomenclature Audit
        run: python validate_nomenclature.py --check-all --strict --verbose
        continue-on-error: true
      
      - name: Create Audit Issues
        if: failure()
        uses: actions/github-script@v7
        # Creates issues for audit failures
```

## Script Inventory

### Existing Scripts

| Script | Location | Purpose | Used By |
| :--- | :--- | :--- | :--- |
| `validate_nomenclature.py` | Repository root | Validates nomenclature v3.0 compliance | GATE-001 |
| `scripts/detect_new_types.py` | `scripts/` | Detects unapproved TYPE codes | GATE-009 |
| `scripts/scaffold.py` | `scripts/` | Generates files from templates | Development |
| `scripts/validate_schema_registry.py` | `scripts/` | Verifies schema refs in ATA 91 | GATE-002 |
| `scripts/validate_trace_links.py` | `scripts/` | Validates trace link targets | GATE-003 |

### Planned Scripts

| Script | Location | Purpose | Used By |
| :--- | :--- | :--- | :--- |
| `scripts/validate_identifiers.py` | `scripts/` | Validates canonical ID grammar | GATE-005 |
| `scripts/check_ata99_registry.py` | `scripts/` | Deduplicates namespace IDs | GATE-004 |
| `scripts/detect_governance_changes.py` | `scripts/` | Identifies governance-impacting diffs | GATE-006 |
| `scripts/detect_schema_breaking_changes.py` | `scripts/` | Flags incompatible schema changes | GATE-007 |
| `scripts/validate_evidence_links.py` | `scripts/` | Checks evidence pack integrity | GATE-008 |
| `scripts/audit_ssot_ownership.py` | `scripts/` | Audits SSOT matrix compliance | GATE-015 |
| `scripts/check_staleness.py` | `scripts/` | Detects stale derived artifacts | GATE-016 |
| `scripts/detect_shadow_registries.py` | `scripts/` | Finds uncoordinated ID lists | GATE-017 |
| `scripts/generate_trace_coverage.py` | `scripts/` | Generates trace coverage metrics | GATE-018 |
| `scripts/check_coverage_thresholds.py` | `scripts/` | Validates min coverage requirements | GATE-018 |
| `scripts/validate_evidence_completeness.py` | `scripts/` | Checks baseline evidence completeness | GATE-014 |

## Failure Remediation Procedures

### GATE-001: Nomenclature Validation Failure

**Symptom:** File does not match `[ROOT]_[BUCKET]_[TYPE]_[LC_OR_SUBBUCKET]_[VARIANT]_[DESCRIPTION]_[VERSION].[EXT]`

**Remediation:**
1. Run locally: `python validate_nomenclature.py <filename>`
2. Rename file per error message guidance
3. Re-commit and push

### GATE-002: Schema Registration Failure

**Symptom:** Schema file is not registered or has version conflicts

**Remediation:**
1. Run locally: `python scripts/validate_schema_registry.py --check-all`
2. **Option A (register):** Register the missing schema in ATA 91 schema registry
3. **Option B (fix reference):** Correct the schema file to use existing registered ID
4. Re-run check locally before pushing

### GATE-003: Trace Link Integrity Failure

**Symptom:** Markdown file contains broken internal links

**Remediation:**
1. Run locally: `python scripts/validate_trace_links.py --check-all --skip-templates`
2. Review broken links in the output
3. **Option A (fix target):** Update link to point to correct existing file
4. **Option B (create target):** Create the missing target file
5. **Option C (remove link):** Remove the broken link if target is no longer needed
6. **Option D (acceptable):** If link references planned content in PORTAL structure, it will be skipped with `--skip-templates` flag
7. Re-commit and push

**Status Update (2026-01-07):**
- Validator enhanced with `--skip-templates` flag
- Broken links reduced from 1,000+ to 490 (51% improvement)
- Remaining 490 links are planned content (expected during PORTAL build-out)
- See `docs/GATE-003-TRACE-LINK-VALIDATION.md` for detailed guide

### GATE-004: Namespace Deduplication Failure

**Symptom:** Duplicate identifier IDs found across namespaces

**Remediation:**
1. **Option A (register):** Register the missing item in ATA 99
2. **Option B (fix reference):** Correct the reference to existing item
3. Re-run check locally before pushing

### GATE-006: Governance Change Detected

**Symptom:** PR auto-labeled `governance-review-required`

**Remediation:**
1. Request review from CM WG member (listed in CODEOWNERS)
2. Address CM WG feedback
3. Await approval before merge

### GATE-007: Breaking Schema Change

**Symptom:** Incompatible schema modification detected

**Remediation:**
1. Create schema migration plan
2. Increment schema major version (e.g., V01 → V02)
3. Update all dependent artifacts
4. Request ATA 91 + CM WG approval

## Maintenance

**Last Updated:** 2025-12-16  
**Update Frequency:** As gates are added/modified  
**Maintained By:** Configuration Management WG (Tooling Authority)

**Change Process:**
1. Propose gate addition/modification via PR
2. Update this index and relevant workflow YAML
3. Implement/update validation script
4. Test in feature branch
5. Request CM WG approval
6. Merge and deploy

## Notes

### Implementation Priority

**Phase 1 (Immediate - Complete):** GATE-001, GATE-002, GATE-003, GATE-006, GATE-009, GATE-010 (active)

**Phase 2 (Q1 2026):** GATE-004, GATE-005 (critical for governance enforcement)

**Phase 3 (Q2 2026):** GATE-007, GATE-008, GATE-015, GATE-016, GATE-017 (audit and staleness detection)

**Phase 4 (Q3 2026):** GATE-011, GATE-012, GATE-013, GATE-014, GATE-018 (full baseline readiness)

### Dependencies

- **ATA 91 Schema Registry:** Must be established for GATE-002, GATE-007, GATE-011
- **ATA 93 Trace Registry:** Must be established for GATE-003, GATE-012, GATE-018
- **ATA 99 Namespace Registry:** Must be established for GATE-004, GATE-013, GATE-017
- **CODEOWNERS file:** Must define CM WG members for GATE-010 approval routing

---

**Document Control**

| Field | Value |
| :--- | :--- |
| **Version** | v01 |
| **Status** | Normative |
| **Owner** | Configuration Management WG (Tooling Authority) |
| **Last Updated** | 2025-12-16 |
| **Next Review** | 2026-03-14 (quarterly) |
