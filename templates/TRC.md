---
title: "Traceability Matrix: {{DESCRIPTION}}"
type: TRC
variant: "{{VARIANT}}"
trace_from: "TBD"
trace_to: "TBD"
status: Draft
---

# Traceability Matrix: {{TITLE}}

## 1. Traceability Overview

### 1.1 Purpose
This matrix establishes traceability between [source] and [target] artifacts.

### 1.2 Scope
Define what is being traced (e.g., requirements to design, design to tests).

### 1.3 Traceability Relationships

**Forward Traceability:** [Source] → [Target]  
**Backward Traceability:** [Target] → [Source]

## 2. Traceability Matrix

### 2.1 Requirements to Design

| Req ID | Requirement | Design Element | Status | Verification Method | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| REQ-001 | [Requirement text] | [Design ID] | Traced | Test | [Notes] |
| REQ-002 | [Requirement text] | [Design ID] | Traced | Analysis | [Notes] |

### 2.2 Design to Verification

| Design ID | Design Element | Test Case | Analysis | Inspection | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| DSN-001 | [Design element] | TC-001, TC-002 | ANA-001 | - | Verified |

### 2.3 Requirements to Verification

| Req ID | Requirement | Test Cases | Analysis | Status | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- |
| REQ-001 | [Requirement] | TC-001 | ANA-001 | Verified | [Report ID] |

## 3. Coverage Analysis

### 3.1 Forward Coverage

| Artifact Type | Total Items | Traced Items | Coverage % | Untraced Items |
| :--- | :--- | :--- | :--- | :--- |
| Requirements | 100 | 98 | 98% | REQ-045, REQ-078 |
| Design Elements | 150 | 150 | 100% | None |

### 3.2 Backward Coverage

| Artifact Type | Total Items | Traced Items | Coverage % | Orphaned Items |
| :--- | :--- | :--- | :--- | :--- |
| Design Elements | 150 | 148 | 99% | DSN-099 |
| Test Cases | 200 | 195 | 98% | TC-101, TC-155 |

## 4. Untraced Items

### 4.1 Forward Untraced (Missing Implementation)

| Source ID | Description | Reason | Action | Owner |
| :--- | :--- | :--- | :--- | :--- |
| REQ-045 | [Requirement] | Deferred to Phase 2 | [Action] | [Name] |

### 4.2 Backward Untraced (Orphaned Artifacts)

| Target ID | Description | Reason | Action | Owner |
| :--- | :--- | :--- | :--- | :--- |
| DSN-099 | [Design element] | Legacy item | Remove or trace | [Name] |

## 5. Many-to-Many Relationships

### 5.1 Requirements with Multiple Implementations

| Req ID | Mapped Design Elements | Reason |
| :--- | :--- | :--- |
| REQ-001 | DSN-001, DSN-002, DSN-003 | Distributed implementation |

### 5.2 Design Elements Satisfying Multiple Requirements

| Design ID | Mapped Requirements | Reason |
| :--- | :--- | :--- |
| DSN-001 | REQ-001, REQ-002, REQ-010 | Common component |

## 6. Traceability Gaps and Issues

| Gap ID | Description | Impact | Resolution Plan | Owner | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| GAP-001 | [Description] | [Impact] | [Plan] | [Name] | Open |

## 7. Change Impact Analysis

How changes to source artifacts affect traced target artifacts.

### 7.1 Recent Changes

| Change ID | Affected Source | Affected Targets | Impact Assessment |
| :--- | :--- | :--- | :--- |
| CHG-001 | REQ-001 | DSN-001, TC-001 | Re-verification required |

## 8. Verification Status Summary

| Status | Count | Percentage |
| :--- | :--- | :--- |
| Fully Verified | 95 | 95% |
| Partially Verified | 3 | 3% |
| Not Verified | 2 | 2% |

## 9. Traceability Maintenance

**Update Frequency:** [Weekly/Monthly]  
**Maintained By:** {{OWNER}}  
**Last Update:** {{DATE}}  
**Next Review:** TBD

## 10. References

- Source documents
- Target documents
- Traceability tool information
