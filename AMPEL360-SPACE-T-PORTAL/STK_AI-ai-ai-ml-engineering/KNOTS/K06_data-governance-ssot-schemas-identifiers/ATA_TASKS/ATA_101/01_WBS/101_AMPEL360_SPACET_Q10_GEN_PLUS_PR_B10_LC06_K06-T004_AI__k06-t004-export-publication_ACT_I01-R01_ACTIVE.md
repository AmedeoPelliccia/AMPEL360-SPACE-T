---
title: "Action Item: T004 Export Publication"
type: ACT
project: AMPEL360
program: SPACET
variant: PLUS
status: ACTIVE
owner: "AI + DATA"
knot_id: K06
task_id: T004
ata: "101"
lc_or_subbucket: "LC06"
---

# T004: Export Publication

## Action Items Register

| ID | Action | Owner | Due Date | Priority | Status | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| T004-01 | Define export pack structure | DATA | TBD | High | Open | Manifest + data + evidence |
| T004-02 | Define manifest format | AI | TBD | High | Open | Deterministic generation |
| T004-03 | Define evidence pointer format | SE + CERT | TBD | High | Open | Link to evidence pack |
| T004-04 | Create export generation tooling | AI | TBD | Medium | Open | Automation |
| T004-05 | Publish export publication standard | DATA | TBD | High | Open | STD artifact |

---

## Action Item Details

### T004-01: Define Export Pack Structure

**Created:** 2025-12-17  
**Owner:** DATA  
**Due Date:** TBD  
**Priority:** High  
**Status:** Open

**Description:**
Define the structure of deterministic export packs including manifests, datasets, and evidence pointers.

**Context:**
Export packs enable downstream consumers (reviews, certification, analytics) to consume sim/test data consistently.

**Acceptance Criteria:**
- [ ] Directory/file structure defined
- [ ] Manifest location and naming specified
- [ ] Dataset packaging rules defined
- [ ] Evidence pointer requirements specified
- [ ] Determinism requirements documented

**Dependencies:**
- T001 (SSOT), T002 (IDs), T003 (Schema)

**Progress Updates:**
- 2025-12-17 - Task created

**Completion Evidence:**
TBD - Link to export pack structure specification

---

### T004-02: Define Manifest Format

**Created:** 2025-12-17  
**Owner:** AI  
**Due Date:** TBD  
**Priority:** High  
**Status:** Open

**Description:**
Define the manifest format for export packs including required fields, generation rules, and integrity verification.

**Context:**
Manifests enable consumers to verify export completeness and provenance.

**Acceptance Criteria:**
- [ ] Manifest schema defined (JSON/YAML)
- [ ] Required fields: version, timestamp, sources, checksums
- [ ] Deterministic generation rules documented
- [ ] SHA-256 integrity verification specified

**Dependencies:**
- T004-01 (structure must be defined first)

**Progress Updates:**
- 2025-12-17 - Task created

**Completion Evidence:**
TBD - Link to manifest format specification

---

### T004-03: Define Evidence Pointer Format

**Created:** 2025-12-17  
**Owner:** SE + CERT  
**Due Date:** TBD  
**Priority:** High  
**Status:** Open

**Description:**
Define the format for evidence pointers that link export packs to the evidence pack (P6).

**Context:**
Evidence pointers enable certification reviewers to trace from exports to underlying evidence.

**Acceptance Criteria:**
- [ ] Pointer format defined (URI, path, ID reference)
- [ ] Pointer types: run evidence, requirement trace, certification claim
- [ ] Validity checking rules specified
- [ ] Integration with evidence pack documented

**Dependencies:**
- T004-01, T004-02 (structure and manifest)

**Progress Updates:**
- 2025-12-17 - Task created

**Completion Evidence:**
TBD - Link to evidence pointer format specification

---

### T004-04: Create Export Generation Tooling

**Created:** 2025-12-17  
**Owner:** AI  
**Due Date:** TBD  
**Priority:** Medium  
**Status:** Open

**Description:**
Create tooling (scripts, CI jobs) to generate export packs deterministically.

**Context:**
Automation ensures consistent export generation and reduces human error.

**Acceptance Criteria:**
- [ ] Export generation script created
- [ ] CI integration defined
- [ ] Determinism verification (same inputs → same outputs)
- [ ] Documentation for tooling usage

**Dependencies:**
- T004-01, T004-02, T004-03 (all format specs)

**Progress Updates:**
- 2025-12-17 - Task created

**Completion Evidence:**
TBD - Link to tooling and documentation

---

### T004-05: Publish Export Publication Standard

**Created:** 2025-12-17  
**Owner:** DATA  
**Due Date:** TBD  
**Priority:** High  
**Status:** Open

**Description:**
Publish the export publication rules as a formal standard (STD artifact).

**Context:**
A published standard enables consistent implementation and provides certification evidence.

**Acceptance Criteria:**
- [ ] STD artifact created
- [ ] References T004-01 through T004-04 outputs
- [ ] Approved by CM WG
- [ ] Linked in evidence pack

**Dependencies:**
- T004-01 through T004-04 (all prior tasks)

**Progress Updates:**
- 2025-12-17 - Task created

**Completion Evidence:**
TBD - Link to published export publication STD

---

## Task Closure Criteria

**T004 is closed when:**

- [ ] Deterministic export packs are defined (manifests + datasets + evidence pointers)
- [ ] Export generation tooling is available
- [ ] Export publication standard is published and approved
- [ ] All sub-actions (T004-01 through T004-05) are completed
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
