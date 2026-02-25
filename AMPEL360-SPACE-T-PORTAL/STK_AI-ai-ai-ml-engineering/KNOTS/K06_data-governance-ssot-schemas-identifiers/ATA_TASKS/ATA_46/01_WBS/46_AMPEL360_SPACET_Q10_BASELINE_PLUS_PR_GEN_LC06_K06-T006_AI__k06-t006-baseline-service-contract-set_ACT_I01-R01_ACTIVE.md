---
title: "Action Item: T006 Baseline Service Contract Set"
type: ACT
project: AMPEL360
program: SPACET
variant: PLUS
status: ACTIVE
owner: "AI + CERT"
knot_id: K06
task_id: T006
ata: "46"
lc_or_subbucket: "LC06"
---

# T006: Baseline Service Contract Set

## Action Items Register

| ID | Action | Owner | Due Date | Priority | Status | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| T006-01 | Define baseline freeze criteria | CERT + CM | TBD | High | Open | What qualifies for baseline |
| T006-02 | Select candidate services and contracts | OPS + DATA | TBD | High | Open | Initial baseline set |
| T006-03 | Validate candidates against schema | AI | TBD | High | Open | Schema compliance |
| T006-04 | Validate candidates against CI gates | AI | TBD | High | Open | ID uniqueness/versioning |
| T006-05 | Create frozen baseline manifest | DATA | TBD | High | Open | Immutable reference |
| T006-06 | Publish baseline service contract set | CERT | TBD | High | Open | Integration-grade artifact |

---

## Action Item Details

### T006-01: Define Baseline Freeze Criteria

**Created:** 2025-12-17  
**Owner:** CERT + CM  
**Due Date:** TBD  
**Priority:** High  
**Status:** Open

**Description:**
Define the criteria that services, contracts, and routing configurations must meet to qualify for inclusion in the frozen baseline.

**Context:**
Clear criteria ensure the baseline contains only integration-grade and ops-ready service contracts.

**Acceptance Criteria:**
- [ ] Freeze criteria documented
- [ ] Required attributes: schema compliance, CI pass, contract completeness
- [ ] Exclusion criteria defined
- [ ] Approval authority specified

**Dependencies:**
- T003 (Schema), T005 (CI Gates)

**Progress Updates:**
- 2025-12-17 - Task created

**Completion Evidence:**
TBD - Link to baseline freeze criteria document

---

### T006-02: Select Candidate Services and Contracts

**Created:** 2025-12-17  
**Owner:** OPS + DATA  
**Due Date:** TBD  
**Priority:** High  
**Status:** Open

**Description:**
Identify and select candidate services, contracts, and routing configurations for inclusion in the baseline.

**Context:**
Initial selection based on operational readiness, contract completeness, and integration coverage.

**Acceptance Criteria:**
- [ ] Candidate list created
- [ ] Each candidate: service ID, contract ID, description, owner, consumer list
- [ ] Selection rationale documented
- [ ] Gaps identified (missing services/contracts)

**Dependencies:**
- T006-01 (freeze criteria must be defined)

**Progress Updates:**
- 2025-12-17 - Task created

**Completion Evidence:**
TBD - Link to candidate selection report

---

### T006-03: Validate Candidates Against Schema

**Created:** 2025-12-17  
**Owner:** AI  
**Due Date:** TBD  
**Priority:** High  
**Status:** Open

**Description:**
Validate each candidate service/contract against the published schema (T003).

**Context:**
Schema validation ensures data integrity and semantic consistency for integration use.

**Acceptance Criteria:**
- [ ] Each candidate validated against schema
- [ ] Validation results documented
- [ ] Non-compliant candidates flagged for remediation
- [ ] Remediation tracked to completion or exclusion

**Dependencies:**
- T003 (Schema), T006-02 (candidates)

**Progress Updates:**
- 2025-12-17 - Task created

**Completion Evidence:**
TBD - Link to schema validation report

---

### T006-04: Validate Candidates Against CI Gates

**Created:** 2025-12-17  
**Owner:** AI  
**Due Date:** TBD  
**Priority:** High  
**Status:** Open

**Description:**
Validate each candidate service/contract against CI gate requirements (T005).

**Context:**
CI gate validation ensures ID uniqueness, versioning compliance, and absence of breaking changes.

**Acceptance Criteria:**
- [ ] Each candidate validated against CI gates
- [ ] ID uniqueness verified
- [ ] Versioning compliance verified
- [ ] Non-compliant candidates flagged for remediation

**Dependencies:**
- T005 (CI Gates), T006-02 (candidates)

**Progress Updates:**
- 2025-12-17 - Task created

**Completion Evidence:**
TBD - Link to CI gate validation report

---

### T006-05: Create Frozen Baseline Manifest

**Created:** 2025-12-17  
**Owner:** DATA  
**Due Date:** TBD  
**Priority:** High  
**Status:** Open

**Description:**
Create the frozen baseline manifest containing all validated services and contracts with immutable references.

**Context:**
The frozen manifest is the integration reference that cannot be changed without versioning.

**Acceptance Criteria:**
- [ ] Manifest created with all validated items
- [ ] SHA-256 checksums for all items
- [ ] Immutability mechanism documented
- [ ] Version and timestamp recorded

**Dependencies:**
- T006-03, T006-04 (validation must pass)

**Progress Updates:**
- 2025-12-17 - Task created

**Completion Evidence:**
TBD - Link to frozen baseline manifest

---

### T006-06: Publish Baseline Service Contract Set

**Created:** 2025-12-17  
**Owner:** CERT  
**Due Date:** TBD  
**Priority:** High  
**Status:** Open

**Description:**
Publish the baseline service contract set as the official integration-grade artifact for K06 ATA 46 closure.

**Context:**
Publication makes the baseline official and enables integration and operations teams to rely on a stable contract set.

**Acceptance Criteria:**
- [ ] Baseline service contract set published
- [ ] References frozen manifest
- [ ] Approved by CM WG and CERT
- [ ] Linked in P6 Evidence Pack
- [ ] Release record created

**Dependencies:**
- T006-05 (manifest must be created)

**Progress Updates:**
- 2025-12-17 - Task created

**Completion Evidence:**
TBD - Link to published baseline service contract set

---

## Task Closure Criteria

**T006 is closed when:**

- [ ] Frozen baseline set of services/contracts is produced
- [ ] All items are integration-grade (schema + CI validated)
- [ ] Baseline manifest is published and immutable
- [ ] All sub-actions (T006-01 through T006-06) are completed
- [ ] Evidence links are recorded in P6 Evidence Pack

---

## Statistics

| Metric | Count |
| :--- | :--- |
| Total Actions | 6 |
| Open | 6 |
| In Progress | 0 |
| Overdue | 0 |
| Completed | 0 |
