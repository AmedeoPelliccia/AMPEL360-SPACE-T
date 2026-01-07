## T001 — SSOT source & ownership (Must Have)

**Intent**
Declare the authoritative **Single Source of Truth (SSOT)** for (1) **message catalogs** and (2) **interface contracts**, and define the **change-control** mechanism that governs updates, approvals, versioning, and downstream propagation.

---

## 1) Scope

### In scope

* **SSOT declaration** for:

  * Message catalogs (UI/system messages, notifications, error codes, event labels, i18n keys, etc.)
  * Interface contracts (API schemas, event schemas, ICDs, data-model contracts)
* **Ownership model** (who owns what, who approves what; minimally CM as governance owner).
* **Change control**:

  * Propose → validate → approve → merge → release → notify/propagate
  * Versioning rules and compatibility gates
* **Traceability**:

  * Each message entry / contract element must be linkable to: change request, commit, review, and release tag.

### Out of scope (explicitly)

* Implementing the actual runtime messaging service or API gateway
* Rewriting existing services (unless needed to comply with the contract governance)

---

## 2) Definitions (operational)

* **SSOT**: The single authoritative repository location and schema for a given artifact type. Any other copies are **derived artifacts** and must be reproducible from SSOT.
* **Message Catalog**: A structured registry of message keys and metadata (severity, domain, code, localization, remediation hints, etc.).
* **Interface Contract**: A canonical contract definition (e.g., OpenAPI/AsyncAPI/JSON Schema/Protobuf/IDL) plus rules for compatibility and deprecation.

---

## 3) SSOT decision table (minimum required output)

Create a table (Markdown + machine-readable format) that maps **artifact type → SSOT → owner → validation → release policy**.

**Template**

| Artifact Type      | Canonical Format            | SSOT Location         | Owner (AoR)                                        | Required Approver(s)       | Validation Gate                                             | Release / Versioning          |
| ------------------ | --------------------------- | --------------------- | -------------------------------------------------- | -------------------------- | ----------------------------------------------------------- | ----------------------------- |
| Message catalog    | YAML/JSON                   | `.../SSOT/messages/`  | **STK_CM** (governance) + product owner for domain | CM + relevant domain owner | schema lint + uniqueness + backward-compat checks           | catalog version + changelog   |
| Interface contract | OpenAPI/AsyncAPI/Schema/IDL | `.../SSOT/contracts/` | **STK_CM** (governance) + interface owner          | CM + interface owner(s)    | contract lint + breaking-change detector + examples compile | SemVer + compatibility policy |

Notes:

* Keep non-CM owners **parametric** if you do not want stakeholder codes invented. Only bind **STK_CM** where you already use it.

---

## 4) Ownership and decision rights (RACI)

**Minimum governance model**

* **Accountable (A):** STK_CM (configuration governance of SSOT locations, schema rules, release tagging)
* **Responsible (R):** Artifact maintainers (message catalog maintainer; interface contract maintainer)
* **Consulted (C):** Downstream consumers (UI, services, documentation, safety/cert stakeholders as applicable)
* **Informed (I):** All impacted portal users / AoRs via release notes + portal changelog

**Decision rights**

* SSOT structure, schema evolution, and release/tag policy: **CM-controlled**
* Domain content changes (new message keys, new endpoints/events): **domain maintainer proposes**, CM ensures compliance gates

---

## 5) Change control workflow (normative)

### 5.1 Change request lifecycle

1. **Propose**: PR includes:

   * Diff to SSOT artifact(s)
   * Rationale
   * Compatibility declaration (non-breaking / breaking)
   * Updated changelog entry
2. **Validate (CI gates)**:

   * Schema validation
   * Duplicate detection (keys, codes, ids)
   * Breaking-change detection (contracts)
   * Reference integrity (no orphaned keys; no undocumented fields)
3. **Approve**:

   * CM approval mandatory
   * Interface owner approval mandatory for contracts
4. **Merge**
5. **Release**:

   * Tag SSOT release (SemVer for contracts; catalog versioning for messages)
   * Publish derived artifacts (generated bundles, docs, stubs)
6. **Notify/Propagate**:

   * Portal changelog entry
   * Consumer update instructions (dependency bump / regeneration)

### 5.2 Compatibility rules (baseline)

* **Contracts**: SemVer + explicit breaking-change detection.

  * Breaking changes require: migration notes + deprecation window (where feasible) + major version bump.
* **Message catalogs**:

  * Message key removals treated as breaking unless a deprecation alias exists.
  * Codes/IDs must be immutable once released (unless emergency with documented rationale + release note).

---

## 6) Required deliverables (Definition of Done)

1. **SSOT policy document** (human-readable):

   * SSOT locations, formats, ownership, gates, versioning, release/tagging rules
2. **SSOT registry file** (machine-readable):

   * The decision table in YAML/JSON for automation
3. **CI validation checklist**:

   * Minimum gates listed above, with pass/fail criteria
4. **Evidence**:

   * Example PR showing the end-to-end process (proposal → CI → approvals → release)
   * Release notes artifact for one sample change

---

## 7) Acceptance criteria (testable)

* A developer can identify **exactly one** canonical location for:

  * message catalogs
  * interface contracts
* Any modification to SSOT artifacts:

  * cannot merge without CM approval
  * fails CI if schema invalid or if duplicates exist
  * flags breaking changes for contracts
* A release tag/version is produced and recorded for SSOT updates.
* Derived artifacts (if any) are reproducible from SSOT with documented command(s) and match the release tag.

---

## 8) Suggested minimal file set (names/paths kept generic)

* `SSOT/messages/` (catalog sources)
* `SSOT/contracts/` (contract sources)
* `SSOT/registry/ssot_map.yaml` (decision table)
* `SSOT/policy/SSOT_POLICY.md` (governance + workflow)
