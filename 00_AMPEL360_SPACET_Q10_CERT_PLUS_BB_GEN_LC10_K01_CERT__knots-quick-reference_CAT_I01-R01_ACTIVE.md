---
title: "Knots Quick Reference"
type: CAT
variant: "CERT"
status: Active
---

# AMPEL360 Space-T Knots Quick Reference

## KNOTS — Knowledge Nets and Ontology as Tasking Strategy

**KNOTS (Knowledge Nets and Ontology as Tasking Strategy)** is the AMPEL360 **Computer-Aided Cross Sustainment (CAXS)** method for turning **design thinking** into **certifiable, repeatable agentic work**, expressed as **SysML-consumable task structures** and enforced by **governance gates**.

A **KNOT** is a **controlled process node** that:

1. defines **what knowledge must exist** (*ontology commitments*),
2. defines **how it must connect** (*knowledge net interfaces*),
3. defines **what tasks agents may execute** (*tasking strategy*),
4. defines **what evidence must be produced** (*compliance-ready outputs*).

KNOTS is the bridge between:

* **MBSE/SysML architecture** (requirements, behavior, structure, interfaces),
* **agentic execution** (task decomposition, automation, prompting/tooling),
* **configuration control** (traceability, naming standard, release packs),
* **certification evidence** (VV packs, audit queries, signed manifests).

---

### 1) Core Concepts

#### Knowledge Net

A directed graph where nodes are controlled artifacts (models, specs, data, test results) and edges are typed relations (e.g., *satisfies*, *verifies*, *allocatesTo*, *dependsOn*, *evidencedBy*).

#### Ontology Commitments

A governed vocabulary and schema set that makes artifacts machine-checkable:

* controlled terms (**AoR**, TYPE, STATUS, IDENTIFIER grammars),
* schemas (SSOT) for registers, evidence, interfaces, and manifests,
* constraints (allowed ranges, required fields, invariants, effectivity rules).

#### Tasking Strategy

A rule set that converts “what we need” into “what agents do”:

* permitted actions per **AoR** (role-based authorizations),
* sequencing rules and dependencies,
* minimum evidence required to close a KNOT,
* exception handling and escalation paths (CM/CERT approval).

#### SysML Expression

KNOTS can be represented as:

* **Activity** flows (task decomposition and sequencing),
* **State** constraints (status transitions, guard conditions),
* **Requirements** relations (satisfy/verify/trace),
* **Interfaces/ports** (ICDs and knowledge edges),
* **Allocation** to **AoR owners** and toolchains (CI/CD + validators).

---

### 2) Governance: Controlled KNOT IDs

KNOT IDs are **configuration-controlled tokens** used in filenames, indexes, dashboards, and CI gates.

* Allowed IDs: **K01..K14 only**
* Optional task suffix: **`-T###`** (e.g., `K06-T001`)
* Any new KNOT requires:

  * a **nomenclature standard upgrade**, and
  * **CM approval** (with change record and allowlist update).

This ensures:

* stable automation rules,
* predictable portal navigation,
* auditable process boundaries and closure.

---

### 3) KNOT Execution Model for Agentic Systems

Each KNOT is defined by a controlled contract:

* **Inputs**: required artifacts + schemas + effectivity context
* **Transformations**: allowed agent actions (generate/validate/link/package)
* **Outputs**: NKUs (Non-Known Unknowns—explicit, cataloged uncertainty items) + evidence bundles + trace edges  
  NKUs are partitioned uncertainty units tracked via NKU ledgers and gated by evidence.
* **Guards**: CI/PLC gates that must pass (PR-blocking)
* **Trace edges**: relations recorded into the traceability graph / ontology DB

A KNOT is **closed** only when:

* naming + identifier validators pass,
* evidence links resolve (no dangling references),
* exceptions (if any) are registered and approved,
* a release/checkpoint artifact exists (when applicable),
* trace graph queries reproduce the closure story.

---

### 4) Practical Mapping to Stakeholder Domains and AoR

To remove ambiguity:

* **AoR** is the **enforced ownership code** (used in filenames, portals, and Role-Based Access Control (RBAC)). Examples: `CM`, `CERT`, `SAF`, `SE`, `OPS`, `AI`, `CY`, `TEST`, `MRO`, `SPACEPORT`, `PMO`, `STK_DAB` (Digital Applications & Blockchains — unified DATA/SPE).
  These codes are the allowlisted tokens for naming and gate enforcement (e.g., `CERT` for certification/authority ownership, `STK_DAB` for digital/prompting/data/traceability).
* “STK” (stakeholder domain) can remain as a **directory navigation concept**, but **does not add value in filenames** and may be omitted there. Existing `STK_*` folders remain for portal navigation; filenames/CI gates should use AoR tokens. New artifacts should prefer AoR tokens in filenames while legacy STK-prefixed names are migrated.

#### Stakeholder split (SE vs STK_DAB)

* **SE (Architecture & Governance)**: SysML structure, ontology commitments, interface/ICD rules, allocation logic, process constraints, closure criteria definitions.
* **STK_DAB (Digital Applications & Blockchains)**: software + prompting engineering, data/traceability registries, evidence ledgers/signing, portal automation, and related agentic tooling.

KNOTS is the contract between them:

* SE defines **“what must be true”**,
* STK_DAB implements **“how it is enforced and executed”**,
* CM/CERT decide **“what is releasable / acceptable”**.

---

### 5) Minimal KNOT Metadata

All metadata keys are expressed in `snake_case` to align with the machine-validated schema.

Each KNOT definition shall include (schema-ready):

* `knot_id`: K01..K14
* `purpose`: why this knot exists
* `inputs_required`: artifact types + schemas + effectivity context
* `outputs_required`: artifact types + evidence expectations
* `relations_required`: required trace edges (satisfy/verify/allocatesTo/dependsOn/evidencedBy)
* `aor_owner`: primary AoR
* `cross_aor_dependencies`: other AoRs and handoffs
* `gates`: validators and PR-blocking checks
* `close_criteria`: measurable completion criteria
* `exceptions_policy`: what can be waived, by whom, and how recorded
* `release_policy`: what constitutes a checkpoint/release pack, and signing requirements

---

### 6) One-sentence definition for README / Portal

**KNOTS operationalizes design thinking as SysML (Systems Modeling Language)–governed, agent-executable task networks. These networks are validated by ontology-backed rules (single-source-of-truth schemas/constraints) and closed through CM-controlled evidence and traceability.**

---

## Operational shortcut: K01 snapshot

**Status:** Active | **Slug:** authority-model-certification-basis  
**Owner:** Regulatory Affairs | **AoR:** CERT (AoR token; directory path may still include `STK_CERT` for navigation)

**Directory:** `KNOTS/K01_authority-model-certification-basis/`  
**Portal:** SPACET-INT | SPACET-AUTH

**Affected Systems:** 52 ATAs across all axes (O/P, T, N, SIMTEST)
- Full list: 00, 01, 02, 03, 04, 11, 13-19, 21, 22, 24-28, 32-35, 38, 42-44, 47, 48, 52, 56, 58, 59, 67-69, 72-74, 76, 90, 93, 96, 100, 105, 106, 109, 110, 112, 114, 115

**Tasks:**
- **T001**: Define Certification Basis and Decision Criteria (8-12 weeks)
- **T002**: Map Compliance Objectives to Evidence and Tests (12-16 weeks)

**Key Deliverables:**
- `00_00_PLAN_LC10_CERT_certification-basis_I01-R01.md`
- `00_00_TRC_LC10_CERT_compliance-matrix_I01-R01.md`

**Documentation:** `00_00_PLAN_LC10_CERT_knot-k01-certification-authority-basis_I01-R01.md`

---

**Version:** v01 | **Date:** 2025-12-15 | **Status:** Active
