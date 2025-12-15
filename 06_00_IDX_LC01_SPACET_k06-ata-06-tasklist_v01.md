---
title: "ATA-06 SSOT and Identifiers - Task List"
type: IDX
variant: "SPACET"
indexed_content: "ATA-06 dimensions, datums, zones, envelopes"
status: Active
owner: "Configuration Management WG"
ata_chapter: "06"
related_ata: "00, 91, 93"
---

# ATA-06 SSOT and Identifiers - Task List

## 1. Overview

This tasklist defines the implementation plan for establishing a Single Source of Truth (SSOT) for ATA-06 dimensions, datums, zones, and envelopes. The goal is to eliminate conflicting sources and establish authoritative identifiers with proper governance.

**Objective**: Define and enforce a single, authoritative source for spacecraft dimensional data (datums, zones, envelopes) with stable identifiers, schemas, and CI validation.

**Scope**: ATA-06 dimensional data including:
- Reference datums and coordinate systems
- Zone definitions and boundaries
- Envelope specifications (launch, thermal, structural)
- Integration interfaces and tolerances

## 2. Context

**Problem**: Multiple competing sources (CAD files, spreadsheets, diagrams) create inconsistency and integration errors.

**Solution**: Establish CAD as SSOT, define export schemas, implement CI validation, and ensure downstream adoption.

## 3. Stakeholders

| Role | Team/Person | Responsibility |
| :--- | :--- | :--- |
| Owner | Configuration Management WG | Overall governance and approval |
| Technical Lead | Systems Engineering | Schema definition and validation |
| CAD Authority | Design Engineering | CAD model maintenance |
| Consumers | Ops/Infra/Sim Teams | Adopt and validate against SSOT |

## 4. Related Documents

| Document ID | Title | Type | Status |
| :--- | :--- | :--- | :--- |
| 06_00_PLAN_LC01_SPACET_ssot-implementation-plan_v01 | SSOT Implementation Plan | PLAN | Planned |
| 06_00_CAT_LC01_SPACET_identifier-registry_v01 | Identifier Registry | CAT | Planned |
| 06_90_SCH_SB00_GEN_dimensional-data-schema_v01 | Dimensional Data Schema | SCH | Planned |
| 06_00_TRC_LC01_SPACET_ssot-traceability_v01 | SSOT Traceability Matrix | TRC | Planned |

## 5. Prerequisites

- [ ] CAD model baseline established
- [ ] CM governance framework in place
- [ ] CI/CD pipeline available
- [ ] Schema validation tools identified

## 6. Tasks (Minimum Set)

### 6.1 Define SSOT and Identifiers

| Task ID | Description | Owner | Status | Artifacts |
| :--- | :--- | :--- | :--- | :--- |
| **T1** | Define authoritative source (CAD vs derived tables) and ownership | Config Mgmt WG | Planned | 06_00_PLAN_LC01_SPACET_ssot-implementation-plan_v01.md |
| **T2** | Define identifier grammar for datums/zones/envelopes (stable, unique) | Systems Eng | Planned | 06_00_CAT_LC01_SPACET_identifier-registry_v01.md |
| **T3** | Define schema: units, coordinate frame, tolerances, metadata | Systems Eng | Planned | 06_90_SCH_SB00_GEN_dimensional-data-schema_v01.json |

**T1 Details**: Define authoritative source (CAD vs derived tables) and ownership
- Establish CAD as primary SSOT
- Define ownership model (who maintains, who approves)
- Document decision rationale
- Define export process from CAD to consumable formats

**T2 Details**: Define identifier grammar for datums/zones/envelopes (stable, unique)
- Create identifier patterns (e.g., `DATUM-{system}-{number}`, `ZONE-{area}-{id}`)
- Ensure stability across versions
- Define uniqueness constraints
- Document identifier allocation process

**T3 Details**: Define schema: units, coordinate frame, tolerances, metadata
- Define coordinate reference frame (origin, axes, handedness)
- Specify units (SI standard)
- Define tolerance notation and limits
- Include metadata fields (version, timestamp, approval status)

### 6.2 Publish and Enforce

| Task ID | Description | Owner | Status | Artifacts |
| :--- | :--- | :--- | :--- | :--- |
| **T4** | Publish canonical exports (CSV/JSON) + minimal diagram references | Design Eng | Planned | 06_90_TAB_SB00_GEN_dimensional-exports_v01.csv |
| **T5** | Implement CI validation: schema checks + unit checks + required fields | DevOps | Planned | scripts/validate_ata06_dimensions.py |

**T4 Details**: Publish canonical exports (CSV/JSON) + minimal diagram references
- Create export scripts from CAD
- Generate CSV/JSON in standardized format
- Include references to source diagrams (but data is canonical)
- Publish to accessible location

**T5 Details**: Implement CI validation: schema checks + unit checks + required fields
- JSON schema validation
- Unit consistency checks
- Required field validation
- Integration with existing CI pipeline

### 6.3 Evidence and Adoption

| Task ID | Description | Owner | Status | Artifacts |
| :--- | :--- | :--- | :--- | :--- |
| **T6** | Produce a frozen "baseline envelope set" with release manifest | Config Mgmt WG | Planned | 06_00_RPT_LC01_SPACET_baseline-release-manifest_v01.md |
| **T7** | Link downstream consumers (Ops/Infra/Sim) and record adoption evidence | Systems Eng | Planned | 06_00_TRC_LC01_SPACET_ssot-traceability_v01.md |

**T6 Details**: Produce a frozen "baseline envelope set" with release manifest
- Create versioned release package
- Include all exports (CSV/JSON)
- Document baseline in manifest
- Formal CM approval

**T7 Details**: Link downstream consumers (Ops/Infra/Sim) and record adoption evidence
- Identify all consumers of dimensional data
- Update consumer systems to use SSOT
- Document adoption in traceability matrix
- Verify consumer compliance

## 7. Outputs / Artifacts

The following artifacts will be produced:

### 7.1 Planning and Control

| Artifact | File Name | Type | Description |
| :--- | :--- | :--- | :--- |
| SSOT Implementation Plan | 06_00_PLAN_LC01_SPACET_ssot-implementation-plan_v01.md | PLAN | Detailed implementation approach |
| Baseline Release Manifest | 06_00_RPT_LC01_SPACET_baseline-release-manifest_v01.md | RPT | Frozen baseline documentation |

### 7.2 Identifier Set and Registry

| Artifact | File Name | Type | Description |
| :--- | :--- | :--- | :--- |
| Identifier Registry (ATA 00) | 00_00_CAT_LC01_SPACET_ata06-identifier-registry_v01.md | CAT | Cross-project identifier catalog |
| Identifier Registry (ATA 06) | 06_00_CAT_LC01_SPACET_identifier-registry_v01.md | CAT | ATA-06 specific identifiers |

### 7.3 Schema Definition (ATA 91)

| Artifact | File Name | Type | Description |
| :--- | :--- | :--- | :--- |
| Dimensional Data Schema | 06_90_SCH_SB00_GEN_dimensional-data-schema_v01.json | SCH | JSON schema for validation |
| Schema Documentation | 06_90_STD_SB00_GEN_schema-specification_v01.md | STD | Human-readable schema docs |

### 7.4 Frozen Baseline Export Pack

| Artifact | File Name | Type | Description |
| :--- | :--- | :--- | :--- |
| Dimensional Exports (CSV) | 06_90_TAB_SB00_GEN_dimensional-exports_v01.csv | TAB | Canonical dimensional data |
| Dimensional Exports (JSON) | 06_90_TAB_SB00_GEN_dimensional-exports_v01.json | TAB | Canonical dimensional data |

### 7.5 CI Validation

| Artifact | File Name | Type | Description |
| :--- | :--- | :--- | :--- |
| Validation Script | scripts/validate_ata06_dimensions.py | - | CI validation implementation |
| Validation Log Template | 06_00_LOG_LC01_SPACET_ci-validation-log_v01.md | LOG | Evidence of validation runs |

### 7.6 Traceability Links (ATA 93)

| Artifact | File Name | Type | Description |
| :--- | :--- | :--- | :--- |
| SSOT Traceability Matrix | 06_00_TRC_LC01_SPACET_ssot-traceability_v01.md | TRC | Links to consumers and evidence |

## 8. Dependencies / Risks

### 8.1 Dependencies

| Dependency | Description | Impact | Mitigation |
| :--- | :--- | :--- | :--- |
| CM Approval | Requires Configuration Management WG approval | Blocks baseline release | Early engagement with CM WG |
| CAD Model Baseline | Requires stable CAD model | Blocks SSOT definition | Coordinate with Design Engineering |
| CI Infrastructure | Requires functioning CI/CD pipeline | Blocks validation automation | Use existing CI framework |
| Registry Governance | Requires identifier allocation process (ATA 00) | Blocks identifier definition | Align with existing registry process |

### 8.2 Risks

| Risk ID | Risk Description | Impact | Probability | Mitigation Strategy |
| :--- | :--- | :--- | :--- | :--- |
| **R1** | Multiple competing "truths" (CAD vs spreadsheets vs diagrams) without SSOT | High | High | Establish CAD as authoritative, deprecate other sources |
| **R2** | Unit/frame mismatches causing downstream integration errors (K04 coupling) | High | Medium | Strict schema validation, unit testing in CI |
| **R3** | Resistance to adoption from downstream consumers | Medium | Medium | Early stakeholder engagement, clear benefits |
| **R4** | Schema changes breaking existing consumers | Medium | Low | Versioning strategy, backward compatibility |
| **R5** | CAD export process failure or data corruption | High | Low | Automated validation, checksums, manual review |

### 8.3 Risk Mitigation Actions

- **For R1**: Document and communicate SSOT decision, provide migration path from legacy sources
- **For R2**: Implement comprehensive CI validation including unit and coordinate frame checks
- **For R3**: Demonstrate value through pilot projects, provide tooling support
- **For R4**: Use semantic versioning, maintain changelog, notify consumers of breaking changes
- **For R5**: Implement export validation pipeline, maintain audit trail

## 9. Success Criteria

- [ ] Single authoritative source (CAD) formally designated and approved
- [ ] All identifiers allocated and documented in registry
- [ ] Schema published and validated
- [ ] CI validation pipeline operational and passing
- [ ] Baseline release package published with CM approval
- [ ] All downstream consumers migrated and documented
- [ ] Zero dimensional data conflicts in integration

## 10. Timeline

| Phase | Tasks | Duration | Dependencies |
| :--- | :--- | :--- | :--- |
| Phase 1: Define | T1, T2, T3 | 2 weeks | CAD baseline |
| Phase 2: Implement | T4, T5 | 3 weeks | Phase 1 complete |
| Phase 3: Baseline | T6 | 1 week | Phase 2 complete, CM approval |
| Phase 4: Adoption | T7 | 2 weeks | Phase 3 complete |

**Total Estimated Duration**: 8 weeks

## 11. Maintenance

**Last Updated:** 2025-12-15  
**Update Frequency:** As tasks are completed  
**Maintained By:** Configuration Management WG

## 12. Approval

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| CM WG Lead | TBD | Pending | - |
| Systems Engineering Lead | TBD | Pending | - |
| Design Engineering Lead | TBD | Pending | - |

## 13. Revision History

| Version | Date | Author | Changes |
| :--- | :--- | :--- | :--- |
| v01 | 2025-12-15 | System | Initial tasklist creation |

---

**Document ID**: 06_00_IDX_LC01_SPACET_k06-ata-06-tasklist_v01.md  
**Status**: Active  
**Owner**: Configuration Management WG
