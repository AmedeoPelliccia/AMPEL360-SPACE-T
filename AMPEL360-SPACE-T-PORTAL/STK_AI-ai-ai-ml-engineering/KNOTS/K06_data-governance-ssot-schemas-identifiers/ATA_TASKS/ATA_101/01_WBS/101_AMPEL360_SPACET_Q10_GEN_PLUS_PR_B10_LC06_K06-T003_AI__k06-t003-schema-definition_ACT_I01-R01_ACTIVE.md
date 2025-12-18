---
title: "Action Item: T003 Schema Definition"
type: ACT
project: AMPEL360
program: SPACET
variant: PLUS
status: ACTIVE
owner: "AI + SE"
knot_id: K06
task_id: T003
ata: "101"
lc_or_subbucket: "LC06"
---

# T003: Schema Definition

## Action Items Register

| ID | Action | Owner | Due Date | Priority | Status | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| T003-01 | Define run metadata schema | AI + SE | TBD | High | Open | Core schema structure |
| T003-02 | Define configuration schema | SE | TBD | High | Open | Environment/toolchain metadata |
| T003-03 | Define results schema | AI + SE | TBD | High | Open | Outputs, metrics, pass/fail |
| T003-04 | Define evidence relationships schema | SE + CERT | TBD | High | Open | Evidence graph structure |
| T003-05 | Define schema versioning policy | CM | TBD | Medium | Open | Compatibility rules |
| T003-06 | Publish consolidated schema | AI | TBD | High | Open | SCH artifact |

---

## Action Item Details

### T003-01: Define Run Metadata Schema

**Created:** 2025-12-17  
**Owner:** AI + SE  
**Due Date:** TBD  
**Priority:** High  
**Status:** Open

**Description:**
Define the schema for simulation/test run metadata including identification, timestamps, ownership, and lifecycle state.

**Context:**
Run metadata is the foundation for traceability and enables downstream consumers to understand run context.

**Acceptance Criteria:**
- [ ] Schema fields defined: ID, name, owner, timestamps, status
- [ ] Field types, formats, and constraints specified
- [ ] Required vs optional fields documented
- [ ] JSON Schema draft created

**Dependencies:**
- T001 (SSOT), T002 (Identifier grammar)

**Progress Updates:**
- 2025-12-17 - Task created

**Completion Evidence:**
TBD - Link to run metadata schema draft

---

### T003-02: Define Configuration Schema

**Created:** 2025-12-17  
**Owner:** SE  
**Due Date:** TBD  
**Priority:** High  
**Status:** Open

**Description:**
Define the schema for run configuration including environment, toolchain versions, model versions, seeds, and dependencies.

**Context:**
Configuration data is essential for reproducibility and provenance tracking.

**Acceptance Criteria:**
- [ ] Schema fields: environment, toolchain, model versions, seeds
- [ ] Dependency tracking structure defined
- [ ] Reproducibility requirements encoded
- [ ] JSON Schema draft created

**Dependencies:**
- T003-01 (run metadata must be defined first)

**Progress Updates:**
- 2025-12-17 - Task created

**Completion Evidence:**
TBD - Link to configuration schema draft

---

### T003-03: Define Results Schema

**Created:** 2025-12-17  
**Owner:** AI + SE  
**Due Date:** TBD  
**Priority:** High  
**Status:** Open

**Description:**
Define the schema for run results including outputs, metrics, pass/fail criteria, and quality indicators.

**Context:**
Standardized results schema enables consistent analysis and evidence compilation.

**Acceptance Criteria:**
- [ ] Schema fields: outputs, metrics, pass/fail, quality
- [ ] Units, tolerances, and frames documented
- [ ] Pass/fail criteria encoding specified
- [ ] JSON Schema draft created

**Dependencies:**
- T003-01, T003-02 (metadata and config must be defined)

**Progress Updates:**
- 2025-12-17 - Task created

**Completion Evidence:**
TBD - Link to results schema draft

---

### T003-04: Define Evidence Relationships Schema

**Created:** 2025-12-17  
**Owner:** SE + CERT  
**Due Date:** TBD  
**Priority:** High  
**Status:** Open

**Description:**
Define the schema for evidence relationships linking runs to requirements, test cases, certification claims, and downstream artifacts.

**Context:**
Evidence relationships enable traceability from sim/test runs to certification claims.

**Acceptance Criteria:**
- [ ] Relationship types defined (verifies, validates, supports)
- [ ] Link structure: source, target, relationship type, confidence
- [ ] Certification evidence requirements encoded
- [ ] JSON Schema draft created

**Dependencies:**
- T003-01, T003-02, T003-03 (all prior schemas)

**Progress Updates:**
- 2025-12-17 - Task created

**Completion Evidence:**
TBD - Link to evidence relationships schema draft

---

### T003-05: Define Schema Versioning Policy

**Created:** 2025-12-17  
**Owner:** CM  
**Due Date:** TBD  
**Priority:** Medium  
**Status:** Open

**Description:**
Define the versioning policy for the schema including semantic versioning rules, compatibility requirements, and migration procedures.

**Context:**
Versioning policy ensures consumers can handle schema evolution without breaking.

**Acceptance Criteria:**
- [ ] Semantic versioning rules defined
- [ ] Breaking vs non-breaking change definitions
- [ ] Compatibility matrix requirements
- [ ] Migration procedure documented
- [ ] Approved by CM WG

**Dependencies:**
- T003-01 through T003-04 (schema must exist to version)

**Progress Updates:**
- 2025-12-17 - Task created

**Completion Evidence:**
TBD - Link to versioning policy document

---

### T003-06: Publish Consolidated Schema

**Created:** 2025-12-17  
**Owner:** AI  
**Due Date:** TBD  
**Priority:** High  
**Status:** Open

**Description:**
Publish the consolidated sim/test run schema as a formal SCH artifact.

**Context:**
A published schema is the normative reference for all consumers and CI validation.

**Acceptance Criteria:**
- [ ] Consolidated JSON Schema created (SCH artifact)
- [ ] Documentation artifact created
- [ ] Schema validates sample exports
- [ ] Approved by SE and CM WG
- [ ] Linked in evidence pack

**Dependencies:**
- T003-01 through T003-05 (all prior tasks)

**Progress Updates:**
- 2025-12-17 - Task created

**Completion Evidence:**
TBD - Link to published schema SCH artifact

---

## Task Closure Criteria

**T003 is closed when:**

- [ ] Semantics for run metadata, configuration, results, and evidence relationships are stabilized
- [ ] Schema versioning policy is established
- [ ] Consolidated schema is published and approved
- [ ] All sub-actions (T003-01 through T003-06) are completed
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
