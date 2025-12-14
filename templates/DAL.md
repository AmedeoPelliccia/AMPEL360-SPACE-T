---
title: "Development Assurance Level Assignment: {{DESCRIPTION}}"
type: DAL
variant: "{{VARIANT}}"
system: "{{SYSTEM_NAME}}"
status: Draft
---

# Development Assurance Level (DAL) Assignment

## 1. Overview

### 1.1 Purpose
This document assigns Development Assurance Levels to system items based on safety criticality.

### 1.2 Applicable Standards
- DO-178C (Software)
- DO-254 (Hardware)
- DO-297 (Integration)

### 1.3 System Description
Brief description of the system being assessed.

## 2. DAL Assignment Methodology

### 2.1 Failure Condition Classification

| Classification | Effect | Acceptable Probability |
| :--- | :--- | :--- |
| Catastrophic | Loss of life, loss of vehicle | Extremely Improbable (< 1E-9) |
| Hazardous | Serious injury, major damage | Extremely Remote (< 1E-7) |
| Major | Minor injury, significant damage | Remote (< 1E-5) |
| Minor | Inconvenience | Probable (< 1E-3) |
| No Safety Effect | No impact | No probability requirement |

### 2.2 DAL Determination

| DAL | Failure Condition | Objectives |
| :--- | :--- | :--- |
| A | Catastrophic | Most rigorous (DO-178C Table A-1) |
| B | Hazardous | Rigorous (DO-178C Table A-2) |
| C | Major | Moderate (DO-178C Table A-3) |
| D | Minor | Basic (DO-178C Table A-4) |
| E | No Safety Effect | Minimal |

## 3. System Item DAL Assignments

### 3.1 Software Items

| Item ID | Item Name | Function | Failure Effect | DAL | Rationale |
| :--- | :--- | :--- | :--- | :--- | :--- |
| SW-001 | Flight Control Software | Primary flight control | Catastrophic | A | Loss of control |
| SW-002 | Navigation Software | Position calculation | Hazardous | B | Navigation error |

### 3.2 Hardware Items

| Item ID | Item Name | Function | Failure Effect | DAL | Rationale |
| :--- | :--- | :--- | :--- | :--- | :--- |
| HW-001 | Flight Computer | Data processing | Catastrophic | A | System failure |

### 3.3 Integration Items

| Item ID | Item Name | Integrated Items | Failure Effect | DAL | Rationale |
| :--- | :--- | :--- | :--- | :--- | :--- |
| INT-001 | Flight Control System | SW-001, HW-001 | Catastrophic | A | Combined failure |

## 4. DAL Justification

### 4.1 Item: [Item Name]

**Assigned DAL:** [A/B/C/D/E]

**Justification:**
Detailed rationale for the DAL assignment including:
- Failure condition analysis
- Safety assessment results (FHA, PSSA)
- Mitigation strategies
- Architectural considerations

**Supporting Evidence:**
- Reference to FHA: [DOC-ID]
- Reference to PSSA: [DOC-ID]
- Reference to SSA: [DOC-ID]

## 5. DAL Impact Analysis

### 5.1 Development Processes

| Process | DAL A | DAL B | DAL C | DAL D |
| :--- | :--- | :--- | :--- | :--- |
| Requirements Review | Full | Full | Moderate | Basic |
| Design Review | Full | Full | Moderate | Basic |
| Code Review | 100% | 100% | Sample | Sample |
| Testing | MC/DC | DC | Statement | Statement |

### 5.2 Verification Requirements

Summary of verification activities required for each DAL level.

## 6. Traceability

### 6.1 Requirements Traceability

| Item | System Req | Safety Req | FHA Hazard | DAL |
| :--- | :--- | :--- | :--- | :--- |
| SW-001 | REQ-001 | SR-001 | HAZ-001 | A |

## 7. Change Impact

### 7.1 Upgrade/Downgrade Considerations
Process for changing DAL assignments.

### 7.2 Configuration Management
How DAL assignments are controlled and baselined.

## 8. Approval

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| System Safety Engineer | TBD | | |
| Chief Engineer | TBD | | |
| Certification Authority | TBD | | |
