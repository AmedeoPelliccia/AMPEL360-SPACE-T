---
title: "Governance Reference Policy: Schema and Trace Coupling"
type: STD
variant: "SPACET"
owner: "Configuration Management WG"
status: Normative
coordinated_with: "ATA 91 (Schemas), ATA 93 (Trace)"
---

# Standard: Governance Reference Policy

## 1. Purpose

This standard defines the **governance reference policy** for how ATA chapters and artifacts must reference schemas (managed by ATA 91) and establish traceability (managed by ATA 93). It ensures:

1. **Consistent schema referencing** across all ATAs
2. **Mandatory trace link establishment** for requirements, hazards, and verification
3. **Version-controlled schema coupling** preventing stale references
4. **Auditability** of evidence chains from requirement to verification
5. **Governance enforcement** through CI/CD gates and manual reviews

### 1.1 Scope

This policy applies to:
- All ATA chapters creating or using data schemas
- All artifacts requiring traceability (requirements, hazards, tests, evidence)
- Schema definitions in ATA 91 (Schema Registry)
- Trace link definitions in ATA 93 (Trace Semantics)
- CI/CD pipeline governance checks

### 1.2 Applicability

**Mandatory compliance** for:
- All ATA leads and technical teams
- Schema designers and data architects (ATA 91)
- Requirements, safety, and verification teams
- Configuration Management team
- Tool developers implementing schema validation and trace checking

## 2. Normative References

| Reference | Title | Authority |
| :--- | :--- | :--- |
| **00_00_STD_LC01_SPACET_nomenclature-standard_I01-R02.md** | Nomenclature Standard v2.0 | AMPEL360 Space-T |
| **00_00_STD_LC01_SPACET_identifier-grammar_I01-R01.md** | Identifier Grammar | AMPEL360 Space-T |
| **00_00_STD_LC01_SPACET_ssot-decision-matrix_I01-R01.md** | SSOT Decision Matrix | AMPEL360 Space-T |
| **ATA 91** | Schema Registry & Versioning | AMPEL360 Space-T |
| **ATA 93** | Trace Semantics & Evidence Links | AMPEL360 Space-T |
| **ATA 99** | Namespace Registry | AMPEL360 Space-T |
| **ECSS-E-ST-10C** | System engineering general requirements | ECSS |
| **ECSS-Q-ST-80C** | Software product assurance | ECSS |
| **ISO/IEC 15288** | Systems and software engineering | ISO/IEC |

## 3. Terms and Definitions

- **Schema Reference**: A pointer from an artifact to a canonical schema definition in ATA 91.
- **Schema Coupling**: The dependency relationship between an artifact and a schema version.
- **Trace Link**: A directed relationship between artifacts (e.g., REQ → TEST) managed by ATA 93.
- **Trace Integrity**: The property that all required trace links exist and are current.
- **Evidence Chain**: The complete path from requirement through design, implementation, to verification.
- **Governance-Impacting Change**: A modification to governance standards, schemas, or trace semantics requiring CM approval.
- **Stale Reference**: A schema or trace reference pointing to a deprecated or non-existent target.

## 4. Schema Referencing Policy (ATA 91 Coupling)

### 4.1 Schema Registration Requirement

**Rule 1: All Schemas Must Be Registered**
- Any data schema (JSON, XML, YAML, database table) **SHALL** be registered in ATA 91 before use.
- Unregistered schemas **SHALL** be rejected by CI/CD pipeline.

**Rule 2: Schema Versioning**
- Schemas **SHALL** follow semantic versioning: `SCH-[TYPE]-[NNN]-V[NN]`
- Example: `SCH-DATA-005-V02`

**Rule 3: Schema Metadata**
- Each schema **SHALL** include metadata:
  - `schema_id`: Unique identifier (per Identifier Grammar)
  - `version`: Semantic version
  - `owner`: Responsible team
  - `status`: `draft`, `approved`, `deprecated`
  - `registered_date`: ISO 8601 timestamp
  - `approval_authority`: Who approved this schema

### 4.2 How ATAs Must Reference Schemas

**Rule 1: Explicit Schema Reference in Artifact Frontmatter**

All artifacts using a schema **SHALL** declare it in frontmatter:

```yaml
---
title: "Propulsion System Hazard Analysis"
type: FHA
variant: "SYS"
schema_refs:
  - schema_id: "SCH-FHA-001-V02"
    registry: "ATA 91"
    status: "approved"
---
```

**Rule 2: Version-Locked References**
- Schema references **SHALL** specify exact version (not `latest` or `current`).
- Example: `SCH-FHA-001-V02` (correct), not `SCH-FHA-001` (incorrect).

**Rule 3: Schema Validation on Commit**
- CI **SHALL** validate artifact data against referenced schema.
- Invalid data **SHALL** block merge.

### 4.3 Schema Evolution and Migration

**Rule 1: Breaking Changes Require New Version**
- Incompatible schema changes **SHALL** increment major version: `V01 → V02`.
- Compatible changes **MAY** use minor version if ATA 91 supports sub-versioning.

**Rule 2: Deprecation Process**
1. ATA 91 marks schema as `deprecated` with sunset date.
2. Artifacts using deprecated schema receive CI warning.
3. After sunset date, CI **SHALL** fail for deprecated schema references.
4. Teams must migrate to new schema version.

**Rule 3: Migration Assistance**
- ATA 91 **SHALL** provide migration guide for breaking changes.
- CM WG **MAY** provide migration scripts or tools.

### 4.4 Schema Change Approval

**Governance-Impacting Changes** (require CM WG approval):
- New schema affecting multiple ATAs
- Breaking changes to existing schema
- Schema deprecation with < 90 days notice

**Non-Governance Changes** (ATA 91 approval sufficient):
- Compatible schema extensions
- Bug fixes in schema definitions
- Documentation updates

## 5. Trace Link Policy (ATA 93 Coupling)

### 5.1 Mandatory Trace Links

**Rule 1: Requirements Traceability**

All requirements **SHALL** have bidirectional trace links:
- **Downstream**: Requirement → Design → Implementation → Test
- **Upstream**: Test → Implementation → Design → Requirement

**Rule 2: Hazard Traceability**

All hazards (FHA/PSSA/SSA) **SHALL** trace to:
- **Causal requirements**: What requirement introduced this hazard?
- **Mitigations**: What controls mitigate this hazard?
- **Verification**: How is mitigation effectiveness verified?

**Rule 3: Evidence Traceability**

All evidence packs **SHALL** trace to:
- **Lifecycle phase**: Which LC gate does this support?
- **Requirements/Hazards**: What is being evidenced?
- **Verification results**: What test results are included?

### 5.2 Trace Link Syntax

**Rule 1: Canonical Trace Link Format**

Trace links **SHALL** use this format:

```yaml
trace_links:
  - type: "satisfies"
    target: "REQ-SYS-042"
    status: "verified"
    evidence: "TC-SYS-0042"
  - type: "mitigates"
    target: "HAZ-PROP-007"
    status: "implemented"
    evidence: "ATA70-DESIGN-042"
```

**Rule 2: Trace Link Types (ATA 93 Registry)**

| Link Type | Source → Target | Meaning |
| :--- | :--- | :--- |
| `satisfies` | Implementation → Requirement | "This implementation satisfies this requirement" |
| `verifies` | Test → Requirement | "This test verifies this requirement" |
| `mitigates` | Control → Hazard | "This control mitigates this hazard" |
| `derives_from` | Derived Req → Parent Req | "This requirement derives from parent" |
| `traces_to` | Generic | Generic trace link |

**Rule 3: Link Status Values**

| Status | Meaning |
| :--- | :--- |
| `proposed` | Link identified but not verified |
| `implemented` | Link exists in implementation |
| `verified` | Link verified by test/review |
| `broken` | Link target no longer exists |
| `deprecated` | Link being phased out |

### 5.3 Trace Link Validation

**Rule 1: Link Integrity Check**
- CI **SHALL** verify all trace link targets exist.
- Broken links **SHALL** block merge or generate high-priority issue.

**Rule 2: Bidirectional Consistency**
- If `A traces_to B`, then `B` **SHOULD** acknowledge reverse link.
- ATA 93 tools **SHALL** check bidirectional consistency.

**Rule 3: Evidence Validation**
- Trace links claiming `verified` status **SHALL** reference evidence artifact.
- Missing evidence **SHALL** downgrade status to `implemented`.

### 5.4 Trace Coverage Metrics

**Rule 1: Minimum Coverage Thresholds**

| Artifact Type | Trace Coverage Requirement |
| :--- | :--- |
| System Requirements | 100% traced to verification |
| Safety Requirements | 100% traced to mitigation + verification |
| Software Requirements (DAL A/B) | 100% traced to test cases |
| Software Requirements (DAL C/D) | ≥95% traced to test cases |
| Hazards (Catastrophic/Hazardous) | 100% traced to controls + verification |
| Hazards (Major/Minor) | ≥90% traced to controls |

**Rule 2: Coverage Reporting**
- ATA 93 **SHALL** generate coverage report on each baseline.
- Below-threshold coverage **SHALL** block baseline approval.

## 6. CI/CD Governance Gates

### 6.1 Pre-Commit Checks (Automated)

**Gate 1: Nomenclature Validation**
```bash
python validate_nomenclature.py --check-all --strict
```
- **Purpose**: Ensure all files conform to nomenclature standard.
- **Fail action**: Block commit; require filename correction.

**Gate 2: Schema Registration Check**
```bash
python scripts/check_schema_registration.py --registry ATA91
```
- **Purpose**: Verify all referenced schemas exist in ATA 91.
- **Fail action**: Block merge; require schema registration or reference correction.

**Gate 3: Trace Link Integrity Check**
```bash
python scripts/check_trace_integrity.py --registry ATA93
```
- **Purpose**: Verify all trace link targets exist.
- **Fail action**: Block merge; require link correction or target restoration.

**Gate 4: Namespace Deduplication Check**
```bash
python scripts/check_ata99_registry.py --deduplicate
```
- **Purpose**: Prevent duplicate IDs across namespaces.
- **Fail action**: Block merge; require ID reassignment.

### 6.2 Pull Request Review Gates (Manual + Automated)

**Gate 5: Governance Change Detection**
```bash
python scripts/detect_governance_changes.py --files <changed_files>
```
- **Purpose**: Detect changes to governance standards, schemas, or trace semantics.
- **Automated action**: Label PR as `governance-review-required`.
- **Manual action**: CM WG member must approve before merge.

**Gate 6: Breaking Schema Change Detection**
```bash
python scripts/detect_schema_breaking_changes.py --registry ATA91
```
- **Purpose**: Detect incompatible schema changes.
- **Automated action**: Require migration plan and impact analysis.
- **Manual action**: ATA 91 lead + CM WG approval required.

**Gate 7: Evidence Link Validation**
```bash
python scripts/validate_evidence_links.py --baseline <baseline_id>
```
- **Purpose**: Verify evidence packs have valid trace links.
- **Automated action**: Generate evidence validation report.
- **Manual action**: Evidence manager reviews before baseline approval.

### 6.3 Approval Requirements for Governance-Impacting Diffs

**Governance-Impacting Changes** require:

| Change Type | Required Approvals |
| :--- | :--- |
| Nomenclature standard update | CM WG consensus |
| Identifier grammar change | CM WG + ATA 99 lead |
| SSOT matrix update | CM WG majority vote |
| New schema in ATA 91 | ATA 91 lead + affected ATA leads |
| Breaking schema change | ATA 91 lead + CM WG + affected ATAs |
| Trace semantics change | ATA 93 lead + CM WG |
| Namespace addition/removal | ATA 99 lead + CM WG |
| Baseline approval | Baseline manager + CM WG |

**Approval Process**:
1. PR author labels PR as `governance-review`.
2. CI detects governance changes and comments on PR.
3. Required approvers are automatically requested.
4. Approvers review and approve/request changes.
5. After all approvals, CM WG member merges.

### 6.4 CI Workflow Configuration

**Example GitHub Actions Workflow** (reference):

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
      
      - name: Nomenclature Validation
        run: python validate_nomenclature.py --check-all --strict
      
      - name: Schema Registration Check
        run: python scripts/check_schema_registration.py --registry ATA91
      
      - name: Trace Integrity Check
        run: python scripts/check_trace_integrity.py --registry ATA93
      
      - name: Namespace Dedup Check
        run: python scripts/check_ata99_registry.py --deduplicate
      
      - name: Detect Governance Changes
        id: governance
        run: |
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
```

## 7. Auditability and Evidence Requirements

### 7.1 Evidence Chain Completeness

**Rule 1: Every Requirement Must Have Evidence**
- For verification: Test results or review evidence
- For safety: Hazard analysis + mitigation evidence

**Rule 2: Evidence Must Be Traceable**
- Evidence files **SHALL** include trace links to requirements/hazards.
- Evidence packs **SHALL** include index referencing all evidence artifacts.

**Rule 3: Evidence Must Be Versioned**
- Evidence artifacts **SHALL** be baselined and version-controlled.
- Stale evidence (older than requirement version) **SHALL** trigger CI warning.

### 7.2 Audit Query Path

**Auditors SHALL be able to reproduce this chain**:

1. **Requirement Identification**: `REQ-SYS-042`
2. **Schema Validation**: Confirm `REQ-SYS-042` validates against `SCH-REQ-001-V02`
3. **Trace to Design**: Follow trace link to design artifact
4. **Trace to Implementation**: Follow trace link to implementation artifact
5. **Trace to Test**: Follow trace link to `TC-SYS-0042`
6. **Evidence Retrieval**: Retrieve test results from evidence pack
7. **Baseline Verification**: Confirm all artifacts are in same baseline

This path is documented in `00_00_RPT_LC01_SPACET_auditability-proof-path_I01-R01.md`.

## 8. Enforcement

### 8.1 Validation Mechanisms

| Mechanism | Frequency | Responsibility |
| :--- | :--- | :--- |
| **CI gates (automated)** | Every commit/PR | CI system |
| **Manual governance review** | On governance changes | CM WG |
| **Quarterly compliance audit** | Quarterly | CM WG + Auditors |
| **Baseline readiness review** | Before each baseline | Baseline Manager |

### 8.2 Non-Compliance Remediation

| Severity | Issue | Action |
| :--- | :--- | :--- |
| **Critical** | Broken trace links in baseline | Block baseline approval; fix immediately |
| **High** | Unregistered schema in use | Block merge; register schema or remove usage |
| **Medium** | Stale schema reference | Issue warning; schedule migration |
| **Low** | Missing optional trace link | Document in backlog; address in next sprint |

### 8.3 Change Control

Changes to this policy **SHALL** require:
1. **CM WG approval** (consensus)
2. **Coordination with ATA 91 and ATA 93**
3. **Impact analysis** on existing artifacts
4. **Communication plan** to all ATAs
5. **Baseline update entry**

## 9. Appendices

### Appendix A: Schema Reference Example (FHA)

```yaml
---
title: "Propulsion System Functional Hazard Assessment"
type: FHA
variant: "SYS"
system: "Propulsion"
schema_refs:
  - schema_id: "SCH-FHA-001-V02"
    registry: "ATA 91"
    status: "approved"
    validation_required: true
trace_links:
  - type: "mitigates"
    target: "HAZ-PROP-007"
    status: "verified"
    evidence: "TC-PROP-007"
  - type: "satisfies"
    target: "REQ-SYS-042"
    status: "verified"
    evidence: "REVIEW-SAFETY-001"
---

# Propulsion System FHA

[Content validates against SCH-FHA-001-V02]
```

### Appendix B: Governance Change Detection Script (Pseudocode)

```python
def detect_governance_changes(changed_files):
    governance_patterns = [
        "00_00_STD_*",           # Governance standards
        "ATA91/schemas/*",        # Schema definitions
        "ATA93/trace/*",          # Trace semantics
        "ATA99/namespaces/*",     # Namespace registry
        ".github/workflows/*",    # CI configuration
    ]
    
    for file in changed_files:
        if matches_any(file, governance_patterns):
            return True  # Governance change detected
    
    return False
```

### Appendix C: Quick Reference Matrix

| Task | Policy Requirement | Validation Method |
| :--- | :--- | :--- |
| Use data schema | Register in ATA 91; reference in frontmatter | CI: schema registration check |
| Update schema | Version increment; migration plan if breaking | CI: breaking change detection |
| Create requirement | Add trace links to tests | CI: trace integrity check |
| Create hazard | Add trace links to mitigations + verification | CI: trace integrity check |
| Submit governance change | Get CM WG approval | Manual: governance review gate |
| Create baseline | Validate all evidence chains | Manual: baseline readiness review |

---

**Document Control**

| Field | Value |
| :--- | :--- |
| **Version** | v01 |
| **Status** | Normative |
| **Owner** | Configuration Management WG |
| **Last Updated** | 2025-12-14 |
| **Next Review** | 2026-06-14 (6 months) |
| **Approvals** | Pending CM WG sign-off |
| **Coordinated With** | ATA 91 (Schemas), ATA 93 (Trace) |
