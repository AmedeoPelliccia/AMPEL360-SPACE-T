---
title: "CI Gate Failures and Remediation Runbook"
type: RPT
project: "AMPEL360"
program: "SPACET"
variant: "PLUS"
report_date: "2025-12-16"
author: "Configuration Management WG (Tooling Authority)"
status: Draft
---

# Report: CI Gate Failures and Remediation Runbook

## Executive Summary

This runbook provides **step-by-step remediation procedures** for all CI/CD governance gate failures in the AMPEL360 Space-T project. It serves as the authoritative guide for developers, ATA leads, and CM WG members to:

1. **Diagnose CI gate failures** rapidly and accurately
2. **Execute standardized remediation steps** to resolve issues
3. **Escalate appropriately** when automated resolution is not possible
4. **Maintain compliance** with nomenclature, schema, and trace governance policies

Each runbook entry includes failure symptoms, root cause analysis, remediation steps, verification procedures, and escalation paths.

## 1. Introduction

### 1.1 Purpose

This report defines **operational runbooks** for resolving CI gate failures in the AMPEL360 Space-T repository. It provides:

- **Standardized troubleshooting procedures** for each governance gate
- **Command-line instructions** for local diagnosis and resolution
- **Escalation criteria** for issues requiring manual intervention
- **Prevention guidelines** to avoid future failures

### 1.2 Scope

This runbook covers:

- **Active gates (implemented)**: GATE-001, GATE-002, GATE-006, GATE-009, GATE-010
- **Planned gates (documented for future)**: GATE-003 through GATE-005, GATE-007, GATE-008, GATE-011 through GATE-018

### 1.3 Applicable Documents

| Reference | Title | Version |
| :--- | :--- | :--- |
| **00_00_IDX_LC01_AMPEL360_SPACET_PLUS_ci-governance-gates_v01.md** | CI Governance Gates Index | v01 |
| **00_00_STD_LC01_AMPEL360_SPACET_PLUS_nomenclature-standard_v02.md** | Nomenclature Standard | v02 |
| **00_00_STD_LC01_AMPEL360_SPACET_PLUS_governance-reference-policy_v01.md** | Governance Reference Policy | v01 |
| **00_00_STD_LC01_AMPEL360_SPACET_PLUS_identifier-grammar_v01.md** | Identifier Grammar | v01 |

## 2. Quick Reference: Gate Failure Summary

### 2.1 Gate Status Overview

| Gate ID | Name | Enforcement | Status | Workflow File |
| :--- | :--- | :--- | :--- | :--- |
| GATE-001 | Nomenclature Validation | BLOCKING | Active | `nomenclature-validation.yml` |
| GATE-002 | Schema Registration Check | BLOCKING | Active | `governance-gates.yml` |
| GATE-003 | Trace Link Integrity | BLOCKING | Planned | `governance-gates.yml` |
| GATE-004 | Namespace Deduplication | BLOCKING | Planned | `governance-gates.yml` |
| GATE-005 | Identifier Grammar Check | BLOCKING | Planned | `governance-gates.yml` |
| GATE-006 | Governance Change Detection | LABELING | Active | `governance-gates.yml` |
| GATE-007 | Breaking Schema Change | BLOCKING | Planned | `governance-gates.yml` |
| GATE-008 | Evidence Link Validation | WARNING | Planned | `governance-gates.yml` |
| GATE-009 | TYPE Code Detection | WARNING | Active | `detect-new-types.yml` |
| GATE-010 | CM WG Approval | MANUAL | Active | PR review process |

### 2.2 Quick Remediation Commands

```bash
# GATE-001: Nomenclature validation
python validate_nomenclature.py --check-all --strict --verbose

# GATE-002: Schema registration check
python scripts/validate_schema_registry.py --check-all --verbose

# GATE-009: TYPE code detection
python scripts/detect_new_types.py --directory .
```

## 3. Gate Runbooks

---

### 3.1 GATE-001: Nomenclature Validation Failure

**Gate ID:** GATE-001  
**Name:** Nomenclature Standard Validation  
**Enforcement:** BLOCKING (merge prevented)  
**Workflow:** `.github/workflows/nomenclature-validation.yml`  
**Script:** `validate_nomenclature.py`

#### 3.1.1 Failure Symptoms

- CI workflow `Nomenclature Standard Validation` fails
- Error message: "❌ Nomenclature validation failed!"
- Files listed with "✗" prefix in workflow logs

#### 3.1.2 Common Root Causes

| Cause | Example | Frequency |
| :--- | :--- | :--- |
| **Incorrect field separator** | Using `-` instead of `_` between fields | High |
| **Missing field** | `00_00_REQ_LC01_description_v01.md` (missing PROJECT/PROGRAM/VARIANT) | High |
| **Invalid BUCKET** | Using `05` instead of `00`, `10`, `20`, etc. | Medium |
| **Invalid TYPE code** | Using `DOC` instead of approved TYPE like `RPT` | Medium |
| **Wrong SUBJECT for BUCKET** | BUCKET=70 with LC02 instead of SB70-SB79 | Medium |
| **Invalid version format** | `v1` instead of `v01` | Low |
| **Case sensitivity** | `Plan` instead of `PLAN` | Low |

#### 3.1.3 Remediation Steps

**Step 1: Identify failing files**

```bash
# Run validation locally to see which files fail
python validate_nomenclature.py --check-all --strict --verbose 2>&1 | grep "✗"
```

**Step 2: Analyze error message**

Error messages specify which field is invalid. Common patterns:

```
✗ Error: Filename does not match required pattern
✗ Error: BUCKET=00 requires SUBJECT to be LC01-LC14, got 'SB70'
✗ Error: TYPE 'DOC' not in approved vocabulary
✗ Error: Invalid PROJECT 'AMPEL': must be AMPEL360
```

**Step 3: Rename file to correct format**

```bash
# Use git mv to preserve history
git mv "old_filename.md" "00_00_RPT_LC01_AMPEL360_SPACET_PLUS_description_v01.md"
```

**Step 4: Verify fix**

```bash
# Validate the renamed file
python validate_nomenclature.py "00_00_RPT_LC01_AMPEL360_SPACET_PLUS_description_v01.md"

# Expected output:
# ✓ 00_00_RPT_LC01_AMPEL360_SPACET_PLUS_description_v01.md
```

**Step 5: Commit and push**

```bash
git add .
git commit -m "fix: rename file to comply with nomenclature standard v3.0"
git push
```

#### 3.1.4 Nomenclature Quick Reference

**Pattern:**
```
[ROOT]_[BUCKET]_[TYPE]_[SUBJECT]_[PROJECT]_[PROGRAM]_[VARIANT]_[DESCRIPTION]_[VERSION].[EXT]
```

**Field Rules:**

| Field | Format | Examples |
| :--- | :--- | :--- |
| ROOT | 2-3 digits | `00`, `06`, `24`, `100` |
| BUCKET | `00\|10\|20\|30\|40\|50\|60\|70\|80\|90` | `00`, `70`, `90` |
| TYPE | 2-8 uppercase letters | `RPT`, `FHA`, `REQ`, `STD` |
| SUBJECT | `LC01-LC14` (BUCKET=00) or `SB15-SB99` (BUCKET≠00) | `LC01`, `SB70` |
| PROJECT | Fixed: `AMPEL360` | `AMPEL360` |
| PROGRAM | Fixed: `SPACET` | `SPACET` |
| VARIANT | Uppercase with hyphens | `PLUS`, `GEN`, `SYS` |
| DESCRIPTION | lowercase-kebab-case | `ci-gate-runbook`, `propulsion` |
| VERSION | `vNN` (2 digits) | `v01`, `v02` |
| EXT | lowercase | `md`, `json`, `csv` |

**Approved TYPE Codes:**

- Planning/Control: `PLAN`, `MIN`, `RPT`, `LOG`, `ACT`, `IDX`
- Safety Analyses: `FHA`, `PSSA`, `SSA`, `FTA`, `ANA`
- Requirements/Allocation: `REQ`, `DAL`, `TRC`
- Data/Reference: `CAT`, `LST`, `GLO`, `MAT`, `SCH`, `DIA`, `TAB`, `STD`

#### 3.1.5 Escalation

**When to escalate:**

- Need for new TYPE code not in approved vocabulary
- Conflict between nomenclature rule and existing file structure
- Pattern edge case not covered by validator

**Escalation path:**

1. Create issue with label `nomenclature`
2. Tag @CM-WG-members in issue
3. For new TYPE codes: run `python scripts/detect_new_types.py --auto-suggest`

---

### 3.2 GATE-002: Schema Registration Check Failure

**Gate ID:** GATE-002  
**Name:** Schema Registration Check  
**Enforcement:** BLOCKING (merge prevented)  
**Workflow:** `.github/workflows/governance-gates.yml`  
**Script:** `scripts/validate_schema_registry.py`

#### 3.2.1 Failure Symptoms

- CI workflow `Governance Gates` fails at "GATE-002 - Schema Registration Check"
- Error message: "REGISTRY_MISSING" or "SCHEMA_NOT_FOUND"
- GitHub issue may be auto-created with label `schema-registry-missing`

#### 3.2.2 Common Root Causes

| Cause | Description | Resolution |
| :--- | :--- | :--- |
| **Registry missing** | No ATA 91 schema registry CSV exists | Create registry file |
| **Schema not registered** | Schema referenced but not in registry | Add to registry |
| **Invalid schema ID** | Schema ID format incorrect | Correct ID format |
| **Version mismatch** | Referencing deprecated version | Update reference |

#### 3.2.3 Remediation Steps

**Scenario A: Registry missing**

```bash
# Check if registry exists
find . -name "*schema-registry*.csv" -o -name "*schema_registry*.csv"

# If no registry exists, create one at expected location:
# Create: 91_00_TAB_SB90_AMPEL360_SPACET_GEN_schema-registry_v01.csv
```

**Registry CSV Format:**

```csv
schema_id,version,namespace,owner,status,file_path,description,content_hash
SCH-FHA-001,V02,ATA-70,Safety Team,approved,./schemas/fha_schema.json,FHA data schema,sha256:abc123...
SCH-REQ-001,V02,ATA-00,Requirements Team,approved,./schemas/req_schema.json,Requirement data schema,sha256:def456...
```

**Scenario B: Schema not registered**

```bash
# Step 1: Identify which schema is missing
python scripts/validate_schema_registry.py --check-all --verbose

# Step 2: Add missing schema to registry CSV
echo "SCH-NEW-001,V01,ATA-XX,Your Team,draft,./path/to/schema.json,Description,TBD" >> schema-registry.csv

# Step 3: Re-run validation
python scripts/validate_schema_registry.py --check-all --verbose
```

**Scenario C: Version mismatch**

```bash
# Update artifact frontmatter to reference correct version:
# OLD: schema_id: "SCH-FHA-001-V01"
# NEW: schema_id: "SCH-FHA-001-V02"
```

#### 3.2.4 Verification

```bash
# Run schema validation locally
python scripts/validate_schema_registry.py --check-all --verbose

# Expected output:
# ✅ Schema registry found: 91_00_TAB_SB90_AMPEL360_SPACET_GEN_schema-registry_v01.csv
# ✅ All referenced schemas are registered
```

#### 3.2.5 Escalation

**When to escalate:**

- Need to register new schema type
- Breaking change to existing schema
- Multiple teams affected by schema change

**Escalation path:**

1. Contact ATA 91 lead for schema governance questions
2. For breaking changes: Follow migration process in Governance Reference Policy §4.3
3. For new schemas: Request CM WG approval

---

### 3.3 GATE-006: Governance Change Detection

**Gate ID:** GATE-006  
**Name:** Governance Change Detection  
**Enforcement:** LABELING (PR labeled, not blocked)  
**Workflow:** `.github/workflows/governance-gates.yml`

#### 3.3.1 Trigger Symptoms

- PR automatically receives label `governance-review-required`
- Bot comment: "⚠️ **Governance Change Detected (GATE-006)**"
- PR cannot merge without CM WG approval

#### 3.3.2 What Triggers GATE-006

| File Pattern | Reason |
| :--- | :--- |
| `00_00_STD_*.md` | Governance standard modification |
| `.github/workflows/*.yml` | CI/CD workflow modification |
| `validate_*.py` | Validation script modification |
| `scripts/(check\|validate\|detect)*.py` | Governance script modification |

#### 3.3.3 Remediation Steps

**This is NOT a failure—it's a governance control.**

**Step 1: Acknowledge the label**

The label indicates your PR modifies governance-impacting files and requires additional review.

**Step 2: Request CM WG review**

```markdown
@CM-WG-members Please review this governance-impacting change.

**Changes:**
- [List what files were modified and why]

**Impact:**
- [Describe impact on other teams/artifacts]
```

**Step 3: Address CM WG feedback**

CM WG may request:
- Impact analysis documentation
- Notification to affected ATA leads
- Phased rollout plan for breaking changes
- Migration guide for deprecated items

**Step 4: Obtain approval**

- At least one CM WG member must approve
- For breaking changes: May require consensus

#### 3.3.4 Bypassing GATE-006 (Not Recommended)

GATE-006 cannot be bypassed—it is a mandatory control. If you believe your change was incorrectly flagged:

1. Comment on PR explaining why this is not a governance change
2. CM WG can remove label if assessment agrees
3. Merge proceeds with normal approval

---

### 3.4 GATE-009: TYPE Code Detection Warning

**Gate ID:** GATE-009  
**Name:** New TYPE Code Detection  
**Enforcement:** WARNING (non-blocking, creates issue/comment)  
**Workflow:** `.github/workflows/detect-new-types.yml`  
**Script:** `scripts/detect_new_types.py`

#### 3.4.1 Failure Symptoms

- Workflow creates/updates issue titled "🔍 New TYPE Codes Detected"
- PR receives comment listing unknown TYPE codes
- Files with unapproved TYPE codes are flagged

#### 3.4.2 Common Root Causes

| Cause | Example | Resolution |
| :--- | :--- | :--- |
| **Typo in TYPE** | `PLN` instead of `PLAN` | Correct typo |
| **Unofficial TYPE** | `DOC`, `NOTE`, `INFO` | Use approved TYPE or request extension |
| **New TYPE needed** | Novel document category | Follow TYPE extension process |

#### 3.4.3 Remediation Steps

**Scenario A: Typo or using wrong TYPE**

```bash
# Check approved TYPE codes
python scripts/detect_new_types.py --directory . --show-vocabulary

# Approved TYPEs:
# PLAN, MIN, RPT, LOG, ACT, IDX, FHA, PSSA, SSA, FTA, ANA, 
# REQ, DAL, TRC, CAT, LST, GLO, MAT, SCH, DIA, TAB, STD

# Rename file with correct TYPE
git mv "00_00_DOC_LC01_AMPEL360_SPACET_PLUS_readme_v01.md" \
       "00_00_RPT_LC01_AMPEL360_SPACET_PLUS_readme_v01.md"
```

**Scenario B: Need new TYPE code**

```bash
# Step 1: Generate extension guide
python scripts/detect_new_types.py --auto-suggest

# Step 2: Review NOMENCLATURE_EXTENSION_GUIDE.md

# Step 3: Create issue requesting TYPE extension
# Include:
# - Proposed TYPE code (2-8 uppercase letters)
# - Definition and purpose
# - Example filenames
# - Justification for why existing TYPEs don't work
```

**TYPE Extension Request Template:**

```markdown
## TYPE Extension Request

**Proposed TYPE:** `SPEC`

**Definition:** Technical specification document

**Purpose:** Captures detailed technical specifications that don't fit REQ (requirements) or STD (standards)

**Example filenames:**
- `00_00_SPEC_LC01_AMPEL360_SPACET_SYS_power-specification_v01.md`
- `24_00_SPEC_SB24_AMPEL360_SPACET_HW_electrical-specification_v01.md`

**Why existing TYPEs don't work:**
- REQ: For requirements, not specifications
- STD: For standards, not project-specific specs
- RPT: For reports, not normative specifications
```

#### 3.4.4 Verification

```bash
# Re-run TYPE detection
python scripts/detect_new_types.py --directory .

# Expected output:
# ✅ All TYPE codes are approved
```

#### 3.4.5 Escalation

**When to escalate:**

- Legitimate need for new TYPE code
- Disagreement on TYPE categorization
- Multiple teams need same new TYPE

**Escalation path:**

1. Create issue with label `nomenclature`
2. Include TYPE Extension Request (template above)
3. CM WG reviews and votes on addition

---

### 3.5 GATE-010: CM WG Manual Approval Required

**Gate ID:** GATE-010  
**Name:** CM WG Approval  
**Enforcement:** MANUAL (human approval required)  
**Workflow:** PR review process (CODEOWNERS)

#### 3.5.1 When GATE-010 Applies

GATE-010 requires CM WG approval for:

| Change Type | Files Affected |
| :--- | :--- |
| Nomenclature standard update | `00_00_STD_*nomenclature*` |
| Identifier grammar change | `00_00_STD_*identifier*` |
| SSOT matrix update | `00_00_STD_*ssot*` |
| New governance policy | `00_00_STD_*` |
| CI workflow modification | `.github/workflows/*.yml` |
| Validation script changes | `validate_*.py`, `scripts/*.py` |

#### 3.5.2 Obtaining CM WG Approval

**Step 1: Prepare PR description**

Include:
- **Summary** of changes
- **Impact analysis** on other teams/artifacts
- **Migration plan** if breaking changes
- **Testing performed** (local validation results)

**Step 2: Request review**

```markdown
@CM-WG-members Requesting approval for governance change.

**Change summary:**
- [What was changed]

**Impact:**
- [Who is affected]

**Testing:**
- [Local validation results]
```

**Step 3: Address feedback**

CM WG may request:
- Additional documentation
- Coordination with affected teams
- Phased rollout plan

**Step 4: Approval and merge**

- CM WG member approves PR
- Merge proceeds after approval

#### 3.5.3 CM WG Approval Criteria

| Criteria | Description |
| :--- | :--- |
| **Completeness** | All required documentation present |
| **Consistency** | Changes align with existing governance |
| **Communication** | Affected parties notified |
| **Reversibility** | Rollback plan if issues arise |
| **Testing** | Local validation successful |

---

## 4. Planned Gate Runbooks (Future Implementation)

### 4.1 GATE-003: Trace Link Integrity (Planned)

**Status:** Planned for Q1 2026  
**Script:** `scripts/check_trace_integrity.py` (not yet implemented)

**Expected Failure Symptoms:**
- Trace link target does not exist
- Broken bidirectional trace links
- Missing required trace relationships

**Planned Remediation:**
1. Run: `python scripts/check_trace_integrity.py --all`
2. Identify broken links in output
3. Update artifact to fix/remove broken links
4. For missing trace targets: Create target artifact or update reference

---

### 4.2 GATE-004: Namespace Deduplication (Planned)

**Status:** Planned for Q1 2026  
**Script:** `scripts/check_ata99_registry.py` (not yet implemented)

**Expected Failure Symptoms:**
- Duplicate identifier across namespaces
- Conflicting ID assignments
- Namespace collision detected

**Planned Remediation:**
1. Run: `python scripts/check_ata99_registry.py --check-duplicates`
2. Identify colliding IDs
3. Reassign IDs to resolve collision
4. Update ATA 99 namespace registry

---

### 4.3 GATE-005: Identifier Grammar (Planned)

**Status:** Planned for Q1 2026  
**Script:** `scripts/validate_identifiers.py` (not yet implemented)

**Expected Failure Symptoms:**
- Identifier format does not match grammar
- Invalid prefix, suffix, or structure
- Missing required identifier components

**Planned Remediation:**
1. Run: `python scripts/validate_identifiers.py --all`
2. Review error messages for format requirements
3. Update identifiers to match grammar specification
4. See: `00_00_STD_LC01_AMPEL360_SPACET_PLUS_identifier-grammar_v01.md`

---

### 4.4 GATE-007: Breaking Schema Change (Planned)

**Status:** Planned for Q2 2026  
**Script:** `scripts/detect_schema_breaking_changes.py` (not yet implemented)

**Expected Failure Symptoms:**
- Incompatible schema modification detected
- Required field removed
- Field type changed incompatibly

**Planned Remediation:**
1. Create migration plan document
2. Increment schema major version (V01 → V02)
3. Update all dependent artifacts
4. Request ATA 91 + CM WG approval
5. Execute migration according to plan

---

### 4.5 GATE-008: Evidence Link Validation (Planned)

**Status:** Planned for Q2 2026  
**Script:** `scripts/validate_evidence_links.py` (not yet implemented)

**Expected Failure Symptoms:**
- Evidence pack missing required links
- Broken evidence file references
- Evidence not associated with requirement/hazard

**Planned Remediation:**
1. Run: `python scripts/validate_evidence_links.py --all`
2. Add missing evidence links to artifacts
3. Fix broken file references
4. Ensure evidence index is complete

---

## 5. General Troubleshooting

### 5.1 CI Workflow Debugging

**Viewing workflow logs:**

1. Navigate to PR → "Checks" tab
2. Click on failed workflow
3. Expand failed step to see detailed logs
4. Look for `✗` or `❌` markers indicating specific failures

**Re-running workflows:**

1. Navigate to Actions tab
2. Select the failed workflow run
3. Click "Re-run failed jobs" (if issue was transient)
4. Or push a fix commit to trigger new run

### 5.2 Local Pre-Push Validation

**Before pushing, run all validations locally:**

```bash
#!/bin/bash
# Save as: pre-push-check.sh

echo "=== Running Local CI Gate Checks ==="

# GATE-001: Nomenclature
echo "GATE-001: Nomenclature Validation..."
python validate_nomenclature.py --check-all --strict
if [ $? -ne 0 ]; then
    echo "❌ GATE-001 FAILED - Fix nomenclature issues before push"
    exit 1
fi

# GATE-002: Schema Registration
echo "GATE-002: Schema Registration..."
if [ -f "scripts/validate_schema_registry.py" ]; then
    python scripts/validate_schema_registry.py --check-all
fi

# GATE-009: TYPE Detection
echo "GATE-009: TYPE Code Detection..."
if [ -f "scripts/detect_new_types.py" ]; then
    python scripts/detect_new_types.py --directory .
fi

echo "=== All Checks Passed ✅ ==="
```

### 5.3 Common Python Environment Issues

```bash
# Ensure Python 3.x is available
python3 --version

# If scripts fail with import errors, check working directory
cd /path/to/AMPEL360-SPACE-T

# Run with explicit Python 3
python3 validate_nomenclature.py --check-all
```

## 6. Conclusions

### 6.1 Key Takeaways

1. **GATE-001 (Nomenclature)** is the most common failure—use the quick reference table in §3.1.4
2. **GATE-006 (Governance Change)** is not a failure—it's a mandatory review trigger
3. **Always run local validation** before pushing to catch issues early
4. **Escalate appropriately** when automated remediation is not possible

### 6.2 Prevention Best Practices

| Practice | Benefit |
| :--- | :--- |
| Use scaffolding script for new files | Ensures correct naming from start |
| Run pre-push validation script | Catches issues before CI |
| Review nomenclature quick reference | Reduces naming errors |
| Request TYPE extensions proactively | Avoids blocking on new document types |

## 7. Appendices

### Appendix A: Error Message Quick Reference

| Error Pattern | Gate | Likely Cause | Quick Fix |
| :--- | :--- | :--- | :--- |
| "does not match required pattern" | GATE-001 | Incorrect file naming | Rename file |
| "BUCKET=00 requires SUBJECT to be LC01-LC14" | GATE-001 | Wrong SUBJECT for bucket | Use LC## for BUCKET=00 |
| "TYPE 'X' not in approved vocabulary" | GATE-001/009 | Unapproved TYPE code | Use approved TYPE or request extension |
| "REGISTRY_MISSING" | GATE-002 | No schema registry file | Create registry CSV |
| "governance-review-required" | GATE-006 | Governance file modified | Request CM WG review |

### Appendix B: Useful Commands

```bash
# Validate single file
python validate_nomenclature.py "filename.md"

# Validate all files
python validate_nomenclature.py --check-all --strict --verbose

# Check schema registry
python scripts/validate_schema_registry.py --check-all --verbose

# Detect new TYPE codes
python scripts/detect_new_types.py --directory .

# Generate TYPE extension guide
python scripts/detect_new_types.py --auto-suggest

# Scaffold new file from template
python scripts/scaffold.py 00 00 RPT LC01 PLUS description v01
```

### Appendix C: Contact and Escalation

| Issue Type | Contact | Channel |
| :--- | :--- | :--- |
| Nomenclature questions | CM WG | GitHub issue with `nomenclature` label |
| Schema registration | ATA 91 Lead | GitHub issue with `schema-registry` label |
| Trace link issues | ATA 93 Lead | GitHub issue with `traceability` label |
| Namespace conflicts | ATA 99 Lead | GitHub issue with `namespace` label |
| Governance approval | CM WG | PR review request |
| Tooling bugs | Tooling Team | GitHub issue with `ci-tooling` label |

---

**Document Control**

| Field | Value |
| :--- | :--- |
| **Version** | v01 |
| **Status** | Draft |
| **Owner** | Configuration Management WG (Tooling Authority) |
| **Author** | Configuration Management WG |
| **Last Updated** | 2025-12-16 |
| **Next Review** | 2026-03-16 (quarterly) |
| **Approvals** | Pending CM WG sign-off |
| **Cross-Reference** | 00_00_IDX_LC01_AMPEL360_SPACET_PLUS_ci-governance-gates_v01.md |
