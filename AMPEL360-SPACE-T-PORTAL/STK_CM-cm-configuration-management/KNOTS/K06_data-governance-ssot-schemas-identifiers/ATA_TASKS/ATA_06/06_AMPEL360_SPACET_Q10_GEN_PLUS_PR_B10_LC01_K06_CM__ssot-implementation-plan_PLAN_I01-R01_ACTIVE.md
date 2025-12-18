---
title: "ATA-06 SSOT Implementation Plan"
type: PLAN
variant: "SPACET"
lifecycle_phase: "LC01"
owner: "Configuration Management WG"
status: Draft
ata_chapter: "06"
related_docs: ["06_00_IDX_LC01_SPACET_k06-ata-06-tasklist_I01-R01.md"]
---

# ATA-06 SSOT Implementation Plan

## 1. Introduction

### 1.1 Purpose

This plan defines the approach for establishing a Single Source of Truth (SSOT) for ATA-06 dimensional data, including datums, zones, and envelopes. The plan addresses Task T1 from the ATA-06 tasklist: "Define authoritative source (CAD vs derived tables) and ownership."

**Lifecycle Phase**: LC01 - Concept and Requirements Definition

### 1.2 Scope

**IN SCOPE:**
- Definition of authoritative data source for ATA-06 dimensional data
- Ownership and maintenance model
- Export process from CAD to consumable formats (CSV/JSON)
- Governance and approval workflow
- Change control procedures
- Version management strategy

**OUT OF SCOPE:**
- Detailed CAD modeling procedures (covered by Design Engineering)
- Specific dimension values (data, not process)
- Non-dimensional ATA-06 data
- Integration with external systems (covered separately)

### 1.3 Applicable Documents

| Doc ID | Title | Reference |
| :--- | :--- | :--- |
| 06_00_IDX_LC01_SPACET_k06-ata-06-tasklist_I01-R01.md | ATA-06 SSOT Task List | Parent document |
| 00_00_STD_LC01_SPACET_nomenclature-standard_I01-R02.md | Nomenclature Standard | File naming |
| 06_00_CAT_LC01_SPACET_identifier-registry_I01-R01.md | Identifier Registry | Related artifact (T2) |
| 06_90_SCH_SB00_GEN_dimensional-data-schema_I01-R01.json | Data Schema | Related artifact (T3) |

### 1.4 Definitions

- **SSOT (Single Source of Truth)**: The one authoritative, canonical source for a given data element
- **CAD**: Computer-Aided Design system (e.g., CATIA, NX, SolidWorks)
- **Datum**: Reference point or surface for dimensional measurement
- **Zone**: Spatial region with defined boundaries
- **Envelope**: Maximum dimensional boundary for component or system

## 2. SSOT Decision: CAD as Authoritative Source

### 2.1 Authoritative Source Selection

**DECISION: CAD models are designated as the SSOT for ATA-06 dimensional data.**

**Rationale:**
1. **Primary Design Authority**: CAD is where dimensions are originally defined during design
2. **Engineering Integration**: CAD integrates with CAE (analysis) and CAM (manufacturing)
3. **Version Control**: CAD systems have built-in version management
4. **Geometry Accuracy**: CAD maintains precise geometric relationships
5. **Change Traceability**: CAD changes are tracked through ECO/ECR process

### 2.2 Derived Data Sources

The following are **NOT** authoritative sources, but derived from CAD:

| Source Type | Status | Usage | Update Trigger |
| :--- | :--- | :--- | :--- |
| Spreadsheets | Derived | Analysis, quick reference | When CAD changes |
| Diagrams | Derived | Communication, documentation | When CAD changes |
| Presentations | Derived | Reviews, approvals | When CAD changes |
| Simulation Models | Derived | Analysis input | When CAD changes |
| Manufacturing Drawings | Derived | Fabrication | When CAD changes |

**Rule**: If spreadsheet/diagram/document conflicts with CAD, **CAD is correct**.

### 2.3 Migration Strategy

For existing projects with legacy dimensional data:

1. **Phase 1: Audit** - Identify all sources claiming authority
2. **Phase 2: Reconcile** - Compare sources, resolve conflicts using engineering judgment
3. **Phase 3: Update CAD** - Ensure CAD reflects approved dimensions
4. **Phase 4: Deprecate** - Mark legacy sources as "Superseded by CAD export"
5. **Phase 5: Export** - Generate canonical exports from CAD

## 3. Organization and Responsibilities

### 3.1 Roles and Responsibilities

| Role | Responsibility | Authority | Contact |
| :--- | :--- | :--- | :--- |
| **Configuration Management WG** | Overall SSOT governance, approval of baselines | Approve baselines, control changes | TBD |
| **Design Engineering Lead** | CAD model maintenance, export generation | Update CAD, generate exports | TBD |
| **Systems Engineering Lead** | Schema definition, validation rules | Define data requirements | TBD |
| **CAD Administrator** | CAD tool configuration, access control | Manage CAD system | TBD |
| **DevOps Engineer** | CI pipeline implementation, automation | Implement validation | TBD |
| **Downstream Consumers** | Adopt SSOT exports, report issues | Use canonical data only | Various |

### 3.2 Ownership Model

**Primary Owner**: Design Engineering (CAD model maintenance)  
**Data Custodian**: Configuration Management WG (baseline approval)  
**Consumers**: All teams requiring dimensional data (read-only access to exports)

### 3.3 Decision Authority

| Decision Type | Authority | Process |
| :--- | :--- | :--- |
| Dimensional changes | Design Engineering + Chief Engineer | ECR/ECO process |
| Baseline release | Configuration Management WG | CM review and approval |
| Schema changes | Systems Engineering + CM WG | Change control board |
| Export format | Systems Engineering | Technical review |

## 4. Process Description

### 4.1 SSOT Workflow

```
┌─────────────┐
│  CAD Model  │ ◄── Primary authority, version controlled
│   (SSOT)    │
└──────┬──────┘
       │
       │ Export Process (automated)
       │
       ▼
┌─────────────────────────────┐
│  Canonical Exports          │
│  - CSV (tables)             │
│  - JSON (structured data)   │
│  - Metadata                 │
└──────┬──────────────────────┘
       │
       │ Validation (CI)
       │
       ▼
┌─────────────────────────────┐
│  Published Baseline         │
│  (CM approved, frozen)      │
└──────┬──────────────────────┘
       │
       │ Consumption
       │
       ▼
┌─────────────────────────────┐
│  Downstream Systems         │
│  - Ops    - Sim             │
│  - Infra  - Analysis        │
└─────────────────────────────┘
```

### 4.2 CAD Export Process

**Step 1: Prepare CAD Model**
- Ensure model is at approved baseline
- Verify all datums/zones/envelopes are properly annotated
- Check coordinate frame definitions

**Step 2: Execute Export Script**
- Run automated export script (CAD API or macro)
- Generate CSV and JSON files
- Include metadata (timestamp, CAD version, baseline ID)

**Step 3: Validate Export**
- Run schema validation (JSON Schema)
- Check unit consistency (all values in SI)
- Verify required fields present
- Check identifier format

**Step 4: Review and Approve**
- Engineering review (spot check dimensions)
- CM review (baseline compliance)
- Approval signature

**Step 5: Publish**
- Commit to repository with proper nomenclature
- Tag release version
- Update manifest
- Notify consumers

### 4.3 Lifecycle Model

**Model**: Incremental baseline releases with continuous validation

**Stages**:
1. **Development**: CAD model under active design, frequent changes
2. **Candidate**: CAD model stable, ready for export and validation
3. **Baseline**: Exports validated and CM approved, frozen
4. **Maintenance**: Baseline in use, changes via ECO only

### 4.4 Tools and Environment

| Tool Category | Tool Name | Purpose |
| :--- | :--- | :--- |
| CAD System | CATIA V5/V6, NX, SolidWorks | Primary design tool, SSOT |
| Export Automation | CAD API/Macro | Automated export generation |
| Validation | Python + JSON Schema | Schema and unit validation |
| Version Control | Git | Export file version control |
| CI/CD | GitHub Actions | Automated validation pipeline |
| Documentation | Markdown | Human-readable documentation |

### 4.5 Change Control

All changes to CAD dimensional data must follow the ECO (Engineering Change Order) process:

1. **Initiate**: Submit ECR (Engineering Change Request) with justification
2. **Review**: Technical review by Design Engineering and Systems Engineering
3. **Approve**: Chief Engineer approval required for dimensional changes
4. **Implement**: Update CAD model per approved ECR
5. **Export**: Generate new exports from updated CAD
6. **Validate**: Run CI validation pipeline
7. **Baseline**: CM approval for new baseline release
8. **Notify**: Inform all downstream consumers of change

## 5. Activities and Schedule

### 5.1 Implementation Milestones

| Milestone | Description | Target Date | Dependencies |
| :--- | :--- | :--- | :--- |
| **M1: SSOT Decision** | CAD designated as SSOT (this document) | Week 1 | None |
| **M2: CAD Baseline** | Establish initial CAD baseline | Week 2 | M1 complete |
| **M3: Export Script** | Develop automated export script | Week 3 | M2 complete, schema defined (T3) |
| **M4: CI Integration** | Integrate validation into CI pipeline | Week 4 | M3 complete, validation script (T5) |
| **M5: First Baseline** | First CM-approved baseline release | Week 6 | M4 complete, CM approval |
| **M6: Consumer Adoption** | All consumers migrated to SSOT | Week 8 | M5 complete, consumer readiness |

### 5.2 Detailed Schedule

**Week 1-2: Foundation**
- Approve SSOT Implementation Plan
- Audit existing dimensional data sources
- Reconcile conflicts between sources
- Establish CAD baseline

**Week 3-4: Automation**
- Develop CAD export script (CSV/JSON generation)
- Implement validation pipeline
- Test export and validation process
- Document export procedure

**Week 5-6: Baseline**
- Generate first canonical exports
- Execute CM review and approval
- Publish baseline release package
- Create release manifest

**Week 7-8: Adoption**
- Update downstream consumers
- Verify consumer compliance
- Document adoption evidence
- Close migration

## 6. Quality and Assurance

### 6.1 Verification Methods

| Verification Item | Method | Frequency | Owner |
| :--- | :--- | :--- | :--- |
| CAD model accuracy | Design review | Per baseline | Design Engineering |
| Export correctness | Automated validation + spot check | Per export | Systems Engineering |
| Schema compliance | CI validation (JSON Schema) | Every commit | CI pipeline |
| Unit consistency | CI validation (unit checks) | Every commit | CI pipeline |
| Baseline integrity | CM audit | Per release | CM WG |
| Consumer adoption | Traceability review | Monthly | Systems Engineering |

### 6.2 Compliance Criteria

**Plan compliance verified through:**
1. **Audits**: CM WG quarterly audit of SSOT process adherence
2. **Reviews**: Baseline release reviews verify export quality
3. **CI Results**: Green CI pipeline indicates validation passing
4. **Traceability**: All consumers documented in traceability matrix
5. **Metrics**: Track:
   - Number of exports generated
   - Validation pass rate
   - Consumer adoption rate
   - Conflict reports (should decrease to zero)

### 6.3 Success Metrics

| Metric | Target | Measurement |
| :--- | :--- | :--- |
| SSOT conflicts | Zero | Monthly audit |
| Export validation pass rate | 100% | CI logs |
| Consumer adoption | 100% | Traceability matrix |
| Baseline release cycle | ≤ 2 weeks | CM logs |
| Dimensional integration errors | Zero | Issue tracker |

## 7. Risk Management

### 7.1 Key Risks

| Risk | Impact | Mitigation |
| :--- | :--- | :--- |
| CAD export failure | High | Automated validation, manual backup |
| Legacy data conflicts | High | Migration plan (Section 2.3) |
| Consumer resistance | Medium | Stakeholder engagement, pilot program |
| CAD tool changes | Medium | Tool-agnostic export format |

### 7.2 Contingency Plans

- **If CAD export fails**: Use previous validated baseline, manual export, escalate to CAD vendor
- **If validation fails**: Do not publish, investigate root cause, fix CAD or validation script
- **If CM approval delayed**: Continue development on next version, hold publication

## 8. Maintenance and Updates

**Plan Maintenance:**
- Review quarterly or when process changes
- Update upon major CAD tool upgrades
- Revise based on lessons learned

**Plan Owner:** Configuration Management WG  
**Next Review:** Q2 2026

## 9. Approval

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| CM WG Lead | TBD | _________________ | __/__/____ |
| Design Engineering Lead | TBD | _________________ | __/__/____ |
| Systems Engineering Lead | TBD | _________________ | __/__/____ |
| Chief Engineer | TBD | _________________ | __/__/____ |

---

**Document ID**: 06_00_PLAN_LC01_SPACET_ssot-implementation-plan_I01-R01.md  
**Status**: Draft  
**Version**: v01  
**Date**: 2025-12-15
