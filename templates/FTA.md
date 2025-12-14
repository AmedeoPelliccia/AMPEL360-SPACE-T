---
title: "Fault Tree Analysis: {{SYSTEM_NAME}}"
type: FTA
variant: "{{VARIANT}}"
bucket: "{{BUCKET}}"
top_event: "TBD"
status: Draft
---

# Fault Tree Analysis (FTA): {{TITLE}}

## 1. Analysis Overview

### 1.1 Top Event Definition
**Top Event:** [Clear statement of the undesired event]

**Classification:** [Catastrophic/Hazardous/Major/Minor]

**Target Probability:** [e.g., < 1E-9 per flight hour]

### 1.2 Analysis Scope
Define system boundaries and operating conditions.

### 1.3 Assumptions
List all assumptions made in the analysis.

## 2. Fault Tree Diagram

```
[Insert fault tree diagram or reference to diagram file]

TOP EVENT: [Event Description]
    |
    AND Gate
    /    \
Event A   Event B
  |         |
  OR       ...
 / \
...
```

## 3. Event Definitions

### 3.1 Basic Events

| Event ID | Event Description | Failure Rate | Source | Notes |
| :--- | :--- | :--- | :--- | :--- |
| BE-001 | Component X fails | 1E-6/hr | [Data source] | [Notes] |

### 3.2 Intermediate Events

| Event ID | Event Description | Gate Type | Input Events |
| :--- | :--- | :--- | :--- |
| IE-001 | Subsystem failure | OR | BE-001, BE-002 |

## 4. Quantitative Analysis

### 4.1 Minimal Cut Sets

| Cut Set | Events | Probability | Contribution |
| :--- | :--- | :--- | :--- |
| CS-001 | BE-001 AND BE-002 | 1E-12 | 60% |
| CS-002 | BE-003 AND BE-004 | 6E-13 | 30% |

### 4.2 Top Event Probability

**Calculated Probability:** [Value]

**Target Probability:** [Value]

**Compliance:** [Met/Not Met]

## 5. Sensitivity Analysis

Analysis of how changes in input parameters affect the top event probability.

| Parameter | Baseline | +50% | -50% | Impact |
| :--- | :--- | :--- | :--- | :--- |
| BE-001 failure rate | 1E-6 | [Result] | [Result] | High/Med/Low |

## 6. Qualitative Analysis

### 6.1 Single Point Failures
Identification of events that alone cause the top event.

### 6.2 Common Cause Failures
Identification of common cause vulnerabilities.

## 7. Mitigation Recommendations

| Issue | Recommendation | Priority | Owner |
| :--- | :--- | :--- | :--- |
| [Issue description] | [Recommendation] | High/Med/Low | [Name] |

## 8. References

- Failure rate data sources
- Related FHA/PSSA documents
- System specifications
