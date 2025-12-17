---
title: "Single Source of Truth (SSOT) Decision Matrix"
type: STD
variant: "SPACET"
owner: "Configuration Management WG"
status: Normative
---

# Standard: Single Source of Truth (SSOT) Decision Matrix

## 1. Purpose

This standard defines the **SSOT decision matrix** for determining which artifacts are **authoritative** (source of truth) versus **derived** (generated or computed) within the AMPEL360 Space-T project. It establishes:

1. **Ownership assignment** for each artifact type
2. **Canonical location** for authoritative artifacts
3. **Derivation rules** for computed/generated artifacts
4. **Conflict resolution** when multiple sources claim authority
5. **Update propagation** requirements for derived artifacts

### 1.1 Scope

This standard applies to:
- All document types (standards, plans, reports, analyses)
- Data artifacts (schemas, tables, catalogs, indexes)
- Requirements, hazards, and test artifacts
- Configuration items and baselines
- Evidence packs and audit trails

### 1.2 Applicability

**Mandatory compliance** for:
- Configuration Management team (SSOT stewards)
- All artifact creators and maintainers
- Tool developers implementing data pipelines
- Auditors verifying data integrity

## 2. Normative References

| Reference | Title | Authority |
| :--- | :--- | :--- |
| **00_00_STD_LC01_SPACET_nomenclature-standard_v02.md** | Nomenclature Standard v2.0 | AMPEL360 Space-T |
| **00_00_STD_LC01_SPACET_identifier-grammar_v01.md** | Identifier Grammar | AMPEL360 Space-T |
| **ATA 91** | Schema Registry & Versioning | AMPEL360 Space-T |
| **ATA 93** | Trace Semantics & Evidence Links | AMPEL360 Space-T |
| **ATA 99** | Namespace Registry | AMPEL360 Space-T |
| **ECSS-M-ST-40C** | Configuration and information management | ECSS |
| **ISO/IEC 19770** | IT asset management | ISO/IEC |

## 3. Terms and Definitions

- **Authoritative Artifact**: The single, definitive source of truth for a data element or document.
- **Derived Artifact**: An artifact generated, computed, or extracted from one or more authoritative sources.
- **SSOT Owner**: The individual or team responsible for maintaining an authoritative artifact.
- **SSOT Location**: The canonical file path or registry location of an authoritative artifact.
- **Stale Derived Artifact**: A derived artifact that no longer reflects its authoritative source(s).
- **Bidirectional Sync**: A prohibited pattern where two artifacts claim mutual authority.
- **Derivation Chain**: The traceable path from derived artifact back to authoritative source(s).

## 4. SSOT Decision Matrix

### 4.1 Matrix Structure

The matrix categorizes all artifact types using these attributes:

| Attribute | Values | Meaning |
| :--- | :--- | :--- |
| **Authority** | `Authoritative`, `Derived`, `Hybrid` | Source of truth status |
| **Owner** | `CM WG`, `ATA Lead`, `Team`, `Tool` | Responsible party |
| **Location** | File path or registry | Canonical storage |
| **Update Frequency** | `On-demand`, `Daily`, `Weekly`, `On-baseline` | Refresh cadence |
| **Derivation Source** | File/registry references | Source artifacts (if derived) |

### 4.2 Authoritative Artifacts Matrix

| Artifact Type | Authority | Owner | SSOT Location | Update Control |
| :--- | :--- | :--- | :--- | :--- |
| **Nomenclature Standard** | Authoritative | CM WG | `00_00_STD_LC01_SPACET_nomenclature-standard_v*.md` | Baseline-controlled |
| **Identifier Grammar** | Authoritative | CM WG | `00_00_STD_LC01_SPACET_identifier-grammar_v*.md` | Baseline-controlled |
| **SSOT Matrix** | Authoritative | CM WG | `00_00_STD_LC01_SPACET_ssot-decision-matrix_v*.md` | Baseline-controlled |
| **Governance Policy** | Authoritative | CM WG | `00_00_STD_LC01_SPACET_governance-reference-policy_v*.md` | Baseline-controlled |
| **ATA 99 Namespace Registry** | Authoritative | ATA 99 Lead | ATA 99 registry files | Merge-controlled |
| **ATA 91 Schema Registry** | Authoritative | ATA 91 Lead | ATA 91 schema files | Version-controlled |
| **ATA 93 Trace Links** | Authoritative | ATA 93 Lead | ATA 93 trace files | Tool-enforced |
| **Requirements (REQ)** | Authoritative | Requirements Team | `*_REQ_*` files per ATA | Review-approved |
| **Hazards (FHA/PSSA/SSA)** | Authoritative | Safety Team | `*_FHA_*`, `*_PSSA_*`, `*_SSA_*` | Safety-approved |
| **Test Cases** | Authoritative | Verification Team | `*_TC_*` files or test DB | Test-approved |
| **Meeting Minutes (MIN)** | Authoritative | Meeting Secretary | `*_MIN_*` files | Attendee-approved |
| **Decision Logs (LOG)** | Authoritative | CM WG | `*_LOG_*` files | CM-approved |
| **Evidence Packs (EVD)** | Authoritative | Evidence Manager | `*_EVD_*` indexes + linked files | Baseline-controlled |
| **Baselines (BL)** | Authoritative | Baseline Manager | Baseline registry + tags | CM-approved |

### 4.3 Derived Artifacts Matrix

| Artifact Type | Authority | Derived From | Owner | Location | Refresh Frequency |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Traceability Matrix (TRC)** | Derived | Requirements + Tests + Hazards | CM Tool | `*_TRC_*` files | Daily (automated) |
| **Evidence Pack Index** | Derived | All linked evidence files | CM Tool | `*_IDX_*` files | On-baseline |
| **Nomenclature Quick Reference** | Derived | Nomenclature Standard | CM WG | `*_CAT_*` files | On standard update |
| **Type Detection Reports** | Derived | All files in repo | CI Tool | CI artifacts | On commit |
| **Audit Reports** | Derived | Baselines + Evidence + Trace | Auditor | `*_RPT_*` files | On-demand |
| **Dashboard Metrics** | Derived | All artifacts | Metrics Tool | Dashboard DB | Hourly |
| **Schema Catalogs** | Derived | ATA 91 Schema Registry | ATA 91 Tool | `*_CAT_*` files | On schema update |
| **Namespace Catalogs** | Derived | ATA 99 Registry | ATA 99 Tool | `*_CAT_*` files | On registry update |
| **Cross-ATA Indexes** | Derived | All ATA artifacts | CM Tool | `*_IDX_*` files | Weekly |

### 4.4 Hybrid Artifacts (Special Cases)

| Artifact Type | Authority | Notes | Owner | Resolution |
| :--- | :--- | :--- | :--- | :--- |
| **Test Results** | Hybrid | Authoritative for execution; derived for pass/fail analysis | Test Team | Results are authoritative; summaries are derived |
| **Code + Documentation** | Hybrid | Code is authoritative; auto-docs are derived | Dev Team | Code SSOT; docs regenerated |
| **Schema + Instances** | Hybrid | Schema is authoritative; instance validation is derived | ATA 91 (Schema Registry) | Schema SSOT; validation reports derived |

### 4.5 Forbidden Patterns

| Pattern | Description | Why Forbidden | Remediation |
| :--- | :--- | :--- | :--- |
| **Bidirectional Sync** | Two artifacts claim to sync from each other | Circular dependency; no SSOT | Designate one as authoritative |
| **Shadow Registry** | Parallel ID/schema list outside master | Deduplication fails | Migrate to ATA 99/91 |
| **Manual Copy** | Human-copied data from authoritative to derived | Staleness risk; no automation | Implement automated pipeline |
| **Untraced Derivation** | Derived artifact with unknown source | Audit failure | Document derivation chain |
| **Stale Derivation** | Derived artifact not updated after source change | Data integrity failure | Enforce refresh frequency |

## 5. SSOT Ownership and Location Rules

### 5.1 Ownership Assignment

**Rule 1: Single Owner**
- Each authoritative artifact **SHALL** have exactly one owner (team or individual).
- Owner is responsible for correctness, updates, and access control.

**Rule 2: Derived Artifacts Inherit Ownership Responsibility**
- Owner of derived artifact **SHALL** ensure automated refresh or manual update per matrix.
- Failure to refresh derived artifacts is a compliance violation.

**Rule 3: Ownership Transitions**
- Ownership changes **SHALL** be recorded in decision log.
- Transitioning ownership **SHALL** include knowledge transfer and tool handoff.

### 5.2 Canonical Location

**Rule 1: File-Based SSOT**
- Authoritative file-based artifacts **SHALL** reside in location per nomenclature standard.
- No copies in multiple locations unless explicitly derived (e.g., cache, export).

**Rule 2: Registry-Based SSOT**
- Registry-based artifacts (ATA 91/93/99) **SHALL** have single master registry file.
- Replicas or exports **SHALL** be clearly marked as derived.

**Rule 3: Git as Version Control SSOT**
- Git repository (`main` branch) is authoritative for file versions.
- Local clones, forks, and branches are derived.

### 5.3 Update Propagation

**Rule 1: Automated Derivation Preferred**
- Derived artifacts **SHOULD** be auto-generated via CI/CD pipeline.
- Manual derivation **SHALL** be documented and minimized.

**Rule 2: Staleness Detection**
- Tools **SHALL** detect when derived artifact is older than source(s).
- CI **SHALL** fail if critical derived artifacts are stale.

**Rule 3: Derivation Chain Traceability**
- Derived artifacts **SHALL** include metadata pointing to source(s).
- Example: `derived_from: ["00_00_STD_LC01_SPACET_nomenclature-standard_v02.md"]`

## 6. Conflict Resolution

### 6.1 Conflict Types

| Conflict Type | Description | Resolution Authority |
| :--- | :--- | :--- |
| **Multiple Claims to Authority** | Two teams claim same artifact as authoritative | CM WG arbitration |
| **Source-Derived Mismatch** | Derived artifact contradicts source | Re-derive from authoritative source |
| **Outdated SSOT Location** | SSOT moved but matrix not updated | Update matrix via change control |
| **Bidirectional Sync Detected** | Two artifacts syncing bidirectionally | Designate one as authoritative; other as derived |

### 6.2 Resolution Process

1. **Detect Conflict**: CI tool or manual audit identifies conflict.
2. **Escalate to CM WG**: Owner logs issue with Configuration Management.
3. **CM WG Decision**: CM WG designates authoritative source and owner.
4. **Matrix Update**: Update this SSOT matrix to reflect decision.
5. **Remediation**: Align artifacts per updated matrix.
6. **Evidence**: Log decision in `00_00_LOG_LC01_SPACET_*` decision log.

## 7. Enforcement

### 7.1 Validation Mechanisms

| Mechanism | Frequency | Responsibility |
| :--- | :--- | :--- |
| **CI staleness check** | Every commit | Automated |
| **Derivation chain validation** | Pull request | Automated |
| **SSOT ownership audit** | Quarterly | CM WG |
| **Conflict detection scan** | Weekly | Automated |

### 7.2 CI/CD Pipeline Integration

**Pre-commit checks**:
```bash
# Check for stale derived artifacts
python scripts/check_staleness.py --matrix ssot-decision-matrix_v01.md

# Validate derivation chains
python scripts/validate_derivation_chains.py --all

# Detect SSOT conflicts
python scripts/detect_ssot_conflicts.py --matrix ssot-decision-matrix_v01.md
```

### 7.3 Non-Compliance Remediation

| Severity | Issue | Action |
| :--- | :--- | :--- |
| **Critical** | Bidirectional sync or shadow registry | Immediate halt; CM WG intervention |
| **High** | Stale critical derived artifact | Block merge; require refresh |
| **Medium** | Missing derivation metadata | Request addition; allow merge |
| **Low** | Ownership ambiguity | Clarify in next CM WG meeting |

### 7.4 Change Control

Changes to this matrix **SHALL** require:
1. **CM WG approval** (consensus or majority vote)
2. **Impact analysis** on dependent artifacts
3. **Baseline update entry**
4. **Communication** to affected teams

## 8. Appendices

### Appendix A: SSOT Decision Flowchart

```
Is artifact created/maintained manually?
  ├─ YES → Is it the definitive source?
  │   ├─ YES → **Authoritative** (assign owner + location)
  │   └─ NO → **Derived** (identify source + refresh rule)
  └─ NO → Is it auto-generated from another artifact?
      ├─ YES → **Derived** (document derivation chain)
      └─ NO → **Authoritative** (likely a registry or baseline)
```

### Appendix B: Example Derivation Metadata

**In derived artifact frontmatter**:
```yaml
---
title: "Traceability Matrix: Requirements to Tests"
type: TRC
variant: "SPACET"
authority: Derived
derived_from:
  - "00_40_REQ_LC02_SW_software-requirements_v01.md"
  - "00_40_TC_LC03_SW_test-cases_v01.md"
last_derived: "2025-12-14T10:30:00Z"
derivation_script: "scripts/generate_trc_matrix.py"
---
```

### Appendix C: Quick Reference by Artifact TYPE

| TYPE | Authority | Typical Owner |
| :--- | :--- | :--- |
| STD | Authoritative | CM WG |
| PLAN | Authoritative | Project/Program Manager |
| MIN | Authoritative | Meeting Secretary |
| RPT | Hybrid (depends on content) | Report Author |
| LOG | Authoritative | CM WG or designated team |
| ACT | Authoritative | Action Item Owner |
| IDX | Derived (typically) | CM Tool |
| FHA/PSSA/SSA | Authoritative | Safety Team |
| REQ | Authoritative | Requirements Team |
| TRC | Derived | CM Tool |
| CAT | Derived | CM Tool or ATA Lead |
| SCH | Authoritative | Data Architecture (ATA 91) |

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
