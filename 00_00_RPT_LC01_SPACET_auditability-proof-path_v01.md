---
title: "Auditability Proof Path: Chain Reproduction Methodology"
type: RPT
variant: "SPACET"
report_date: "2025-12-14"
author: "Configuration Management WG"
status: Normative
---

# Report: Auditability Proof Path

## Executive Summary

This report defines the **minimal audit query path** that enables auditors to reproduce the complete chain from requirement identification through schema validation, design, implementation, to verification and evidence. It establishes:

1. **Standardized audit procedures** for trace chain reconstruction
2. **Tool-based query methods** for automated path traversal
3. **Evidence retrieval protocols** for baseline verification
4. **Compliance validation steps** for governance enforcement

The proof path ensures **independent reproducibility** of any artifact's lineage and verification status, supporting certification, regulatory compliance, and quality audits.

## 1. Introduction

### 1.1 Purpose

The purpose of this report is to:

- Define a **step-by-step audit query path** for reproducing artifact lineage
- Establish **tool commands and queries** for each audit step
- Document **expected outputs** and **validation criteria** at each step
- Provide **worked examples** of complete audit chains
- Enable **independent auditor verification** without CM WG assistance

### 1.2 Scope

This report covers:

- **Requirement-to-verification chains** (REQ → Design → Implementation → Test → Evidence)
- **Hazard-to-mitigation chains** (Hazard → Control → Verification → Evidence)
- **Schema-to-instance validation** (Schema registration → Artifact compliance)
- **Baseline-to-artifact tracing** (Baseline tag → Included artifacts → Evidence packs)
- **Governance compliance verification** (Standards → CI gates → Approval logs)

Out of scope:
- Internal tool implementation details (black box approach)
- Non-governance artifacts (e.g., informal documentation)
- External dependencies (third-party tools, commercial off-the-shelf)

### 1.3 Applicable Documents

| Reference | Title | Version |
| :--- | :--- | :--- |
| **00_00_STD_LC01_SPACET_identifier-grammar_v01.md** | Identifier Grammar | v01 |
| **00_00_STD_LC01_SPACET_ssot-decision-matrix_v01.md** | SSOT Decision Matrix | v01 |
| **00_00_STD_LC01_SPACET_governance-reference-policy_v01.md** | Governance Reference Policy | v01 |
| **00_00_IDX_LC01_SPACET_ci-governance-gates_v01.md** | CI Governance Gates Index | v01 |
| **ATA 91** | Schema Registry & Versioning | TBD |
| **ATA 93** | Trace Semantics & Evidence Links | TBD |
| **ATA 99** | Namespace Registry | TBD |

## 2. Methodology

### 2.1 Audit Path Principles

The audit query path follows these principles:

1. **Deterministic**: Same inputs always produce same outputs
2. **Reproducible**: Independent auditors get identical results
3. **Tool-based**: Automated queries preferred over manual inspection
4. **Evidence-backed**: Every step references verifiable artifacts
5. **Git-traceable**: All artifacts version-controlled in Git repository

### 2.2 Data Sources

| Source Type | Location | Access Method |
| :--- | :--- | :--- |
| **Git Repository** | GitHub: `AmedeoPelliccia/AMPEL360-SPACE-T` | `git clone`, `git log`, `git show` |
| **File Artifacts** | Repository files (`.md`, `.json`, etc.) | File system access, `grep`, `view` |
| **ATA 91 Schema Registry** | `ATA91/` directory (planned) | Registry query scripts |
| **ATA 93 Trace Registry** | `ATA93/` directory (planned) | Trace link query scripts |
| **ATA 99 Namespace Registry** | `ATA99/` directory (planned) | Namespace query scripts |
| **CI/CD Logs** | GitHub Actions artifacts | GitHub API, workflow logs |
| **Baseline Tags** | Git tags | `git tag`, `git describe` |

### 2.3 Analysis Methods

**Step-by-step query execution**:
1. **Identify target artifact** (e.g., requirement ID)
2. **Retrieve artifact file** from Git repository
3. **Extract trace links** from artifact metadata (frontmatter)
4. **Follow each trace link** to target artifacts
5. **Validate schema compliance** against ATA 91 registry
6. **Retrieve evidence** from evidence packs
7. **Verify baseline inclusion** via Git tags
8. **Confirm approval** via decision logs and CI history

## 3. Audit Query Path Definition

### 3.1 Path Overview

The complete audit query path consists of **8 steps**:

```
Step 1: Requirement Identification
   ↓
Step 2: Schema Validation
   ↓
Step 3: Trace to Design
   ↓
Step 4: Trace to Implementation
   ↓
Step 5: Trace to Test
   ↓
Step 6: Evidence Retrieval
   ↓
Step 7: Baseline Verification
   ↓
Step 8: Approval Confirmation
```

### 3.2 Step-by-Step Query Procedure

#### Step 1: Requirement Identification

**Objective**: Locate the authoritative requirement artifact

**Input**: Requirement ID (e.g., `REQ-SYS-042`)

**Query**:
```bash
# Search repository for requirement file
grep -r "REQ-SYS-042" --include="*.md" .

# Expected output: File path containing requirement
# Example: ./ATA24/00_24_REQ_LC02_SYS_electrical-requirements_v01.md
```

**Validation**:
- File exists in repository
- File name conforms to nomenclature standard v2.0
- File metadata (frontmatter) contains requirement ID

**Output**: Requirement file path

---

#### Step 2: Schema Validation

**Objective**: Confirm requirement validates against registered schema

**Input**: Requirement file path from Step 1

**Query**:
```bash
# Extract schema reference from frontmatter
grep "schema_refs:" -A5 ./ATA24/00_24_REQ_LC02_SYS_electrical-requirements_v01.md

# Expected output:
# schema_refs:
#   - schema_id: "SCH-REQ-001-V02"
#     registry: "ATA 91"
#     status: "approved"
```

**Validation**:
```bash
# Verify schema exists in ATA 91 registry
python scripts/check_schema_registration.py --schema SCH-REQ-001-V02 --registry ATA91

# Expected output:
# ✅ Schema SCH-REQ-001-V02 found in ATA 91 registry
# Status: approved
# Owner: Requirements Team
```

**Output**: Schema ID and validation status

---

#### Step 3: Trace to Design

**Objective**: Follow trace link from requirement to design artifact

**Input**: Requirement file from Step 1

**Query**:
```bash
# Extract trace links from requirement
grep "trace_links:" -A10 ./ATA24/00_24_REQ_LC02_SYS_electrical-requirements_v01.md

# Expected output:
# trace_links:
#   - type: "satisfies"
#     target: "ATA24-DESIGN-042"
#     status: "verified"
#     evidence: "REVIEW-DESIGN-001"
```

**Validation**:
```bash
# Verify design artifact exists
grep -r "ATA24-DESIGN-042" --include="*.md" .

# Check trace link integrity
python scripts/check_trace_integrity.py --link-id REQ-SYS-042 --target ATA24-DESIGN-042
```

**Output**: Design artifact reference

---

#### Step 4: Trace to Implementation

**Objective**: Follow trace link from design to implementation

**Input**: Design artifact from Step 3

**Query**:
```bash
# Extract implementation trace link from design
grep "trace_links:" -A10 ./ATA24/00_24_DESIGN_LC03_SYS_power-distribution-design_v01.md

# Expected output:
# trace_links:
#   - type: "implements"
#     target: "ATA24-IMPL-042"
#     status: "verified"
```

**Validation**:
```bash
# Verify implementation artifact exists
grep -r "ATA24-IMPL-042" --include="*.md" .

# For software: Check code repository references
# For hardware: Check manufacturing specs
```

**Output**: Implementation artifact reference

---

#### Step 5: Trace to Test

**Objective**: Follow trace link from requirement/implementation to test case

**Input**: Requirement file from Step 1 OR Implementation from Step 4

**Query**:
```bash
# Extract test trace link
grep "trace_links:" -A10 ./ATA24/00_24_REQ_LC02_SYS_electrical-requirements_v01.md | grep "verifies"

# Expected output:
# - type: "verifies"
#   target: "TC-SYS-0042"
#   status: "verified"
#   evidence: "TEST-RESULTS-042"
```

**Validation**:
```bash
# Verify test case exists
grep -r "TC-SYS-0042" --include="*.md" .

# Check bidirectional trace
python scripts/check_trace_integrity.py --bidirectional REQ-SYS-042 TC-SYS-0042
```

**Output**: Test case ID and verification status

---

#### Step 6: Evidence Retrieval

**Objective**: Retrieve test results and verification evidence

**Input**: Evidence reference from Step 5 trace link

**Query**:
```bash
# Locate evidence pack
grep -r "TEST-RESULTS-042" --include="*_IDX_*evidence*.md" .

# Expected output: Evidence pack index file
# Example: ./00_00_IDX_LC03_SPACET_lc03-evidence-pack_v01.md
```

**Evidence Pack Query**:
```bash
# Extract evidence details from pack
grep "TEST-RESULTS-042" -A10 ./00_00_IDX_LC03_SPACET_lc03-evidence-pack_v01.md

# Expected output:
# | TEST-RESULTS-042 | Test Execution Log | ./evidence/test_results_042.pdf | PDF | Verified | Pass |
```

**Validation**:
```bash
# Verify evidence file exists
ls -la ./evidence/test_results_042.pdf

# Check evidence metadata
python scripts/validate_evidence_links.py --evidence-id TEST-RESULTS-042
```

**Output**: Evidence artifact location and validation status

---

#### Step 7: Baseline Verification

**Objective**: Confirm all artifacts are in same approved baseline

**Input**: Requirement ID, Design ID, Implementation ID, Test ID from previous steps

**Query**:
```bash
# List all baselines
git tag -l "BL-*"

# Check artifact inclusion in specific baseline
git show BL-2025-12-01:./ATA24/00_24_REQ_LC02_SYS_electrical-requirements_v01.md
git show BL-2025-12-01:./ATA24/00_24_DESIGN_LC03_SYS_power-distribution-design_v01.md
git show BL-2025-12-01:./evidence/test_results_042.pdf
```

**Validation**:
```bash
# Verify baseline includes all artifacts in chain
python scripts/validate_baseline_completeness.py --baseline BL-2025-12-01 --chain REQ-SYS-042

# Expected output:
# ✅ All artifacts in chain REQ-SYS-042 present in baseline BL-2025-12-01
# - REQ-SYS-042: ✅ included
# - ATA24-DESIGN-042: ✅ included
# - ATA24-IMPL-042: ✅ included
# - TC-SYS-0042: ✅ included
# - TEST-RESULTS-042: ✅ included
```

**Output**: Baseline tag and completeness confirmation

---

#### Step 8: Approval Confirmation

**Objective**: Verify governance approvals for all changes

**Input**: Baseline tag from Step 7

**Query**:
```bash
# Check CI workflow execution for baseline
gh run list --workflow="governance-gates.yml" --branch=main --limit=20

# Retrieve approval log
cat ./00_00_LOG_LC01_SPACET_k06-approvals_v01.md | grep "BL-2025-12-01"

# Expected output:
# | APPR-042 | 2025-12-01 | Baseline BL-2025-12-01 | CM WG Consensus | Approved | J. Smith |
```

**Validation**:
```bash
# Verify CM WG approval signature
git log --all --grep="BL-2025-12-01" --show-signature

# Check CI gate success
gh run view <run-id> --log
```

**Output**: Approval log entry and CI gate confirmation

---

## 4. Worked Example

### 4.1 Complete Audit Chain: REQ-SYS-042

**Scenario**: External auditor verifies requirement REQ-SYS-042 has been fully implemented and verified.

**Step 1 - Requirement Identification**:
```bash
$ grep -r "REQ-SYS-042" --include="*.md" .
./ATA24/00_24_REQ_LC02_SYS_electrical-requirements_v01.md:### REQ-SYS-042: Emergency Power Distribution
```

**Step 2 - Schema Validation**:
```bash
$ grep "schema_refs:" -A5 ./ATA24/00_24_REQ_LC02_SYS_electrical-requirements_v01.md
schema_refs:
  - schema_id: "SCH-REQ-001-V02"
    registry: "ATA 91"
    status: "approved"

$ python scripts/check_schema_registration.py --schema SCH-REQ-001-V02
✅ Schema SCH-REQ-001-V02 found in ATA 91 registry
```

**Step 3 - Trace to Design**:
```bash
$ grep "trace_links:" -A5 ./ATA24/00_24_REQ_LC02_SYS_electrical-requirements_v01.md
trace_links:
  - type: "satisfies"
    target: "ATA24-DESIGN-042"
    status: "verified"
    evidence: "REVIEW-DESIGN-001"

$ grep -r "ATA24-DESIGN-042" --include="*.md" .
./ATA24/00_24_DESIGN_LC03_SYS_power-distribution-design_v01.md:## ATA24-DESIGN-042: Emergency Bus Topology
```

**Step 4 - Trace to Implementation**:
```bash
$ grep "trace_links:" -A5 ./ATA24/00_24_DESIGN_LC03_SYS_power-distribution-design_v01.md
trace_links:
  - type: "implements"
    target: "ATA24-IMPL-042"
    status: "verified"

$ ls -la ./ATA24/implementation/emergency_bus_042.cfg
-rw-r--r-- 1 user user 4096 2025-11-15 14:32 emergency_bus_042.cfg
```

**Step 5 - Trace to Test**:
```bash
$ grep "verifies" ./ATA24/00_24_REQ_LC02_SYS_electrical-requirements_v01.md
  - type: "verifies"
    target: "TC-SYS-0042"
    status: "verified"
    evidence: "TEST-RESULTS-042"

$ grep -r "TC-SYS-0042" --include="*.md" .
./00_40_TC_LC04_SYS_system-test-cases_v01.md:### TC-SYS-0042: Emergency Power Failover Test
```

**Step 6 - Evidence Retrieval**:
```bash
$ grep "TEST-RESULTS-042" -r --include="*evidence*.md" .
./00_00_IDX_LC04_SPACET_lc04-evidence-pack_v01.md:| TEST-RESULTS-042 | Emergency Power Test Log | ./evidence/test_042.pdf | PDF | Verified | PASS |

$ ls -la ./evidence/test_042.pdf
-rw-r--r-- 1 user user 245760 2025-11-20 09:15 test_042.pdf
```

**Step 7 - Baseline Verification**:
```bash
$ git tag -l "BL-*"
BL-2025-12-01

$ git show BL-2025-12-01:./ATA24/00_24_REQ_LC02_SYS_electrical-requirements_v01.md | head -5
---
title: "Electrical System Requirements"
type: REQ
[...file content confirmed...]

$ python scripts/validate_baseline_completeness.py --baseline BL-2025-12-01 --chain REQ-SYS-042
✅ All artifacts in chain REQ-SYS-042 present in baseline BL-2025-12-01
```

**Step 8 - Approval Confirmation**:
```bash
$ cat ./00_00_LOG_LC01_SPACET_k06-approvals_v01.md | grep "BL-2025-12-01"
| APPR-042 | 2025-12-01 | Baseline BL-2025-12-01 approval | CM WG | Approved | J. Smith |

$ git log --grep="BL-2025-12-01" --show-signature
commit abc123def456... (tag: BL-2025-12-01)
gpg: Signature made Mon Dec  1 10:00:00 2025
gpg: Good signature from "CM WG <cm@ampel360.space>"
```

**Audit Result**: ✅ **COMPLETE CHAIN VERIFIED**

All artifacts from requirement to evidence are present, traced, baselined, and approved.

---

## 5. Tool Reference

### 5.1 Query Tools

| Tool | Purpose | Example Usage |
| :--- | :--- | :--- |
| `grep` | Text search in files | `grep -r "REQ-SYS-042" --include="*.md" .` |
| `git` | Version control queries | `git show BL-2025-12-01:./file.md` |
| `python scripts/check_schema_registration.py` | Schema validation | `--schema SCH-REQ-001-V02` |
| `python scripts/check_trace_integrity.py` | Trace link validation | `--link-id REQ-SYS-042` |
| `python scripts/validate_baseline_completeness.py` | Baseline checking | `--baseline BL-2025-12-01 --chain REQ-SYS-042` |
| `python scripts/validate_evidence_links.py` | Evidence validation | `--evidence-id TEST-RESULTS-042` |
| `gh` (GitHub CLI) | CI/CD logs | `gh run list --workflow governance-gates.yml` |

### 5.2 Expected Tool Outputs

All validation tools follow this output format:

**Success**:
```
✅ [Check name] passed
[Details]
```

**Failure**:
```
❌ [Check name] failed
[Error details]
[Remediation steps]
```

**Warning**:
```
⚠️  [Check name] warning
[Warning details]
```

---

## 6. Conclusions

### 6.1 Auditability Assurance

The defined audit query path ensures:

1. **Independent Reproducibility**: Any auditor can execute queries and get identical results
2. **Tool-Based Automation**: Reduces human error and bias
3. **Evidence-Backed Verification**: Every step references verifiable artifacts
4. **Git Traceability**: Full version history and approval signatures
5. **Governance Compliance**: All changes pass CI gates and CM WG approval

### 6.2 Minimal Query Path

The **minimal 8-step path** is sufficient to verify:
- Requirement → Design → Implementation → Test → Evidence chain
- Schema compliance
- Baseline inclusion
- Governance approvals

No additional steps are required for basic auditability.

### 6.3 Compliance with Standards

This audit path complies with:
- **ECSS-M-ST-40C**: Configuration and information management
- **ISO/IEC 15288**: Systems and software engineering lifecycle
- **DO-178C** (aerospace software): Traceability requirements
- **ISO 9001**: Quality management audit trails

---

## 7. Recommendations

| ID | Recommendation | Priority | Owner | Target Date |
| :--- | :--- | :--- | :--- | :--- |
| **REC-001** | Implement planned validation scripts (GATE-002 through GATE-008) | High | Tooling Team | Q1 2026 |
| **REC-002** | Establish ATA 91/93/99 registries with query interfaces | High | CM WG | Q1 2026 |
| **REC-003** | Automate baseline completeness checking | Medium | Tooling Team | Q2 2026 |
| **REC-004** | Provide auditor training on query path execution | Medium | CM WG | Q2 2026 |
| **REC-005** | Integrate audit path into quarterly compliance reviews | Low | CM WG | Q3 2026 |

---

## 8. Appendices

### Appendix A: Query Script Templates

**Template: Requirement Chain Query**
```bash
#!/bin/bash
REQ_ID=$1

echo "=== Auditing Requirement Chain: $REQ_ID ==="

# Step 1: Find requirement file
REQ_FILE=$(grep -rl "$REQ_ID" --include="*.md" .)
echo "✓ Requirement file: $REQ_FILE"

# Step 2: Extract trace links
DESIGN_ID=$(grep -A10 "trace_links:" "$REQ_FILE" | grep "target:" | head -1 | awk '{print $2}' | tr -d '"')
echo "✓ Design: $DESIGN_ID"

# Step 3-5: Continue chain traversal...
# [Additional steps]

echo "=== Audit Complete ==="
```

### Appendix B: Validation Checklist

**Auditor Validation Checklist** (for manual verification):

- [ ] Requirement file exists and conforms to nomenclature
- [ ] Schema reference is valid and approved
- [ ] Trace links are complete and bidirectional
- [ ] Design artifact exists
- [ ] Implementation artifact exists
- [ ] Test case exists with verified status
- [ ] Evidence file exists and is accessible
- [ ] All artifacts present in same baseline
- [ ] Baseline has CM WG approval
- [ ] CI gates passed for all changes

---

**Document Control**

| Field | Value |
| :--- | :--- |
| **Version** | v01 |
| **Status** | Normative |
| **Owner** | Configuration Management WG |
| **Author** | Configuration Management WG |
| **Last Updated** | 2025-12-14 |
| **Next Review** | 2026-06-14 (6 months) |
| **Approvals** | Pending CM WG sign-off |
