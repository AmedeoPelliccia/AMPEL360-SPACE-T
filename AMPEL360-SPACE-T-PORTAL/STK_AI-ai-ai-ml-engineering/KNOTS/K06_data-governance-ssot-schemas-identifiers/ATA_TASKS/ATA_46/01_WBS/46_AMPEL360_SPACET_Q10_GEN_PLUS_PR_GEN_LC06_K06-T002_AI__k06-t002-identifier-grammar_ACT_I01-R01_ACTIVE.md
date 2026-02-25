---
title: "Action Item: T002 Identifier Grammar"
type: ACT
project: AMPEL360
program: SPACET
variant: PLUS
status: ACTIVE
owner: "AI + DATA"
knot_id: K06
task_id: T002
ata: "46"
lc_or_subbucket: "LC06"
---

# T002: Identifier Grammar

## Action Items Register

| ID | Action | Owner | Due Date | Priority | Status | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| T002-01 | Survey existing identifier schemes | DATA | TBD | High | Open | Document current patterns |
| T002-02 | Define canonical ID grammar for services and contracts | AI + SE | TBD | High | Open | Formal specification |
| T002-03 | Define deduplication rules | DATA | TBD | Medium | Open | Prevent duplicate IDs |
| T002-04 | Create identifier allocation process | CM | TBD | Medium | Open | Change control integration |
| T002-05 | Publish identifier grammar standard | DATA | TBD | High | Open | STD artifact |

---

## Action Item Details

### T002-01: Survey Existing Identifier Schemes

**Created:** 2025-12-17  
**Owner:** DATA  
**Due Date:** TBD  
**Priority:** High  
**Status:** Open

**Description:**
Survey and document all existing identifier schemes used for data services, API endpoints, service contracts, datasets, and routing rules.

**Context:**
Understanding existing schemes is necessary to design a compatible canonical grammar that doesn't break existing references.

**Acceptance Criteria:**
- [ ] Inventory of existing ID schemes documented
- [ ] Each scheme: format, scope, usage context, issuing authority
- [ ] Compatibility constraints identified
- [ ] Gap analysis completed

**Dependencies:**
- T001 (SSOT must be identified to know where IDs are used)

**Progress Updates:**
- 2025-12-17 - Task created

**Completion Evidence:**
TBD - Link to identifier survey report

---

### T002-02: Define Canonical ID Grammar

**Created:** 2025-12-17  
**Owner:** AI + SE  
**Due Date:** TBD  
**Priority:** High  
**Status:** Open

**Description:**
Define the canonical identifier grammar for all information-systems entities including data services, API endpoints, service contracts, datasets, and routing configurations.

**Context:**
A stable, unique ID grammar prevents duplicates and enables traceability across the service lifecycle.

**Acceptance Criteria:**
- [ ] Grammar specification document created
- [ ] Covers: services, endpoints, contracts, datasets, routing configs
- [ ] Format rules: components, separators, length, allowed characters
- [ ] Uniqueness guarantees documented
- [ ] Examples provided for each entity type

**Dependencies:**
- T002-01 (survey must be complete first)

**Progress Updates:**
- 2025-12-17 - Task created

**Completion Evidence:**
TBD - Link to identifier grammar specification

---

### T002-03: Define Deduplication Rules

**Created:** 2025-12-17  
**Owner:** DATA  
**Due Date:** TBD  
**Priority:** Medium  
**Status:** Open

**Description:**
Define rules and mechanisms to prevent duplicate identifiers from being issued across service registries and contract databases.

**Context:**
Duplicate IDs cause routing failures, contract conflicts, and traceability breakdowns.

**Acceptance Criteria:**
- [ ] Deduplication rules documented
- [ ] Collision detection mechanism specified
- [ ] Remediation process for discovered duplicates
- [ ] CI integration requirements defined

**Dependencies:**
- T002-02 (grammar must be defined to define dedup rules)

**Progress Updates:**
- 2025-12-17 - Task created

**Completion Evidence:**
TBD - Link to deduplication rules document

---

### T002-04: Create Identifier Allocation Process

**Created:** 2025-12-17  
**Owner:** CM  
**Due Date:** TBD  
**Priority:** Medium  
**Status:** Open

**Description:**
Create the process for allocating new identifiers, including request workflow, approval, and registry update.

**Context:**
Controlled allocation ensures ID uniqueness and maintains registry integrity for services and contracts.

**Acceptance Criteria:**
- [ ] Allocation process documented
- [ ] Request/approval workflow defined
- [ ] Registry update procedure defined
- [ ] Automation opportunities identified

**Dependencies:**
- T002-02, T002-03 (grammar and dedup rules)

**Progress Updates:**
- 2025-12-17 - Task created

**Completion Evidence:**
TBD - Link to allocation process document

---

### T002-05: Publish Identifier Grammar Standard

**Created:** 2025-12-17  
**Owner:** DATA  
**Due Date:** TBD  
**Priority:** High  
**Status:** Open

**Description:**
Publish the identifier grammar as a formal standard (STD artifact) for use across ATA 46.

**Context:**
A published standard enables consistent implementation and provides certification evidence.

**Acceptance Criteria:**
- [ ] STD artifact created with full grammar specification
- [ ] Approved by CM WG
- [ ] Referenced from P2 (IDs & Registry) partition
- [ ] Linked in evidence pack

**Dependencies:**
- T002-01 through T002-04 (all prior tasks)

**Progress Updates:**
- 2025-12-17 - Task created

**Completion Evidence:**
TBD - Link to published identifier grammar STD

---

## Task Closure Criteria

**T002 is closed when:**

- [ ] Canonical IDs defined for services/endpoints/contracts/datasets/routing configs
- [ ] Deduplication rules prevent duplicate identifiers
- [ ] Identifier grammar standard is published and approved
- [ ] All sub-actions (T002-01 through T002-05) are completed
- [ ] Evidence links are recorded in P6 Evidence Pack

---

## Statistics

| Metric | Count |
| :--- | :--- |
| Total Actions | 5 |
| Open | 5 |
| In Progress | 0 |
| Overdue | 0 |
| Completed | 0 |
