---
title: "Canonical Identifier Grammar and Namespace Boundaries"
type: STD
variant: "SPACET"
owner: "Configuration Management WG"
status: Normative
coordinated_with: "ATA 99 (Namespace Registry)"
---

# Standard: Canonical Identifier Grammar and Namespace Boundaries

## 1. Purpose

This standard defines the **canonical identifier grammar** and **namespace boundaries** for all identifiable artifacts, entities, and data elements within the AMPEL360 Space-T project. It ensures:

1. **Global uniqueness** across all ATAs and lifecycle phases
2. **Namespace collision prevention** through structured prefixing
3. **Machine-readable traceability** for automated tooling
4. **ATA 99 registry integration** for deduplication enforcement

### 1.1 Scope

This standard applies to:
- All file identifiers (governed by Nomenclature Standard v2.0)
- Internal artifact identifiers (requirements, hazards, test cases, etc.)
- Cross-ATA references and trace links
- Schema identifiers and version tags
- Evidence and baseline identifiers

### 1.2 Applicable Personnel

**Mandatory compliance** for:
- All engineering staff creating identifiable artifacts
- Configuration Management team managing registries
- Tool developers implementing ID generation/validation
- Auditors verifying trace integrity

## 2. Normative References

| Reference | Title | Authority |
| :--- | :--- | :--- |
| **00_00_STD_LC01_SPACET_nomenclature-standard_v02.md** | Nomenclature Standard v2.0 | AMPEL360 Space-T |
| **ATA 99** | Namespace Registry & Deduplication | AMPEL360 Space-T |
| **ATA 91** | Schema Registry & Versioning | AMPEL360 Space-T |
| **ATA 93** | Trace Semantics & Evidence Links | AMPEL360 Space-T |
| **ISO/IEC 11179** | Metadata registries | ISO/IEC |
| **ECSS-M-ST-40C** | Configuration and information management | ECSS |

## 3. Terms and Definitions

- **Canonical Identifier**: A globally unique, immutable identifier conforming to this grammar.
- **Namespace**: A logical grouping prefix preventing collisions (e.g., `ATA24`, `REQ`, `HAZ`).
- **Namespace Boundary**: The organizational or technical limit of an identifier authority's jurisdiction, defining the scope within which an identifier authority has exclusive control over ID assignment.
- **Identifier Authority**: The ATA, system, or team responsible for issuing IDs within a namespace.
- **Shadow Registry**: An unauthorized or uncoordinated identifier registry (forbidden).
- **Deduplication Enforcement**: ATA 99 mechanism preventing duplicate IDs across namespaces.

## 4. Rules and Requirements

### 4.1 Canonical Identifier Grammar

All canonical identifiers **SHALL** conform to this grammar:

```
[NAMESPACE]-[CATEGORY]-[SEQUENCE][-VARIANT]
```

#### 4.1.1 Grammar Components

| Component | Description | Format | Example |
| :--- | :--- | :--- | :--- |
| **NAMESPACE** | Root authority (ATA or domain) | 2-5 uppercase alphanumeric | `ATA24`, `SYS`, `SW`, `REQ` |
| **CATEGORY** | Artifact type within namespace | 2-4 uppercase alphanumeric | `REQ`, `HAZ`, `TC`, `FHA` |
| **SEQUENCE** | Monotonic numeric sequence | 3-6 zero-padded digits | `001`, `0042`, `123456` |
| **VARIANT** | Optional sub-variant or version | 1-8 uppercase alphanumeric | `A`, `V01`, `DRAFT` |

**Separators**: Hyphen (`-`) only. No underscores, dots, or other delimiters.

#### 4.1.2 Grammar Examples

| Valid | Invalid | Reason |
| :--- | :--- | :--- |
| `REQ-SYS-001` | `REQ_SYS_001` | Wrong separator (underscore) |
| `ATA24-HAZ-042` | `ATA24.HAZ.042` | Wrong separator (dot) |
| `SW-TC-0001-A` | `SW-TC-1-A` | Sequence not zero-padded |
| `FHA-PROP-123` | `fha-prop-123` | Lowercase not allowed |
| `ATA99-NS-00001` | `ATA99-NS-1` | Insufficient zero-padding |

### 4.2 Namespace Definitions and Boundaries

#### 4.2.1 Primary Namespaces

| Namespace | Authority | Scope | Registry Owner |
| :--- | :--- | :--- | :--- |
| **ATA00** - **ATA99** | ATA Chapter leads | Chapter-specific artifacts | ATA 99 (central) |
| **REQ** | Requirements team | All requirements (system, SW, HW) | ATA 93 |
| **HAZ** | Safety team | Hazards, FHA, PSSA, SSA | ATA 00 Safety |
| **TC** | Verification team | Test cases | ATA 93 |
| **SCH** | Data Architecture | Schema definitions | ATA 91 |
| **TRC** | CM team | Trace links | ATA 93 |
| **EVD** | Evidence manager | Evidence packs | ATA 00 CM |
| **BL** | Baseline manager | Baselines and releases | ATA 00 CM |

#### 4.2.2 Namespace Ownership Rules

1. **Single Authority**: Each namespace **SHALL** have exactly one identifier authority.
2. **No Overlap**: Namespace scopes **SHALL NOT** overlap (enforced by ATA 99).
3. **Registration Required**: New namespaces **SHALL** be registered with ATA 99 before first use.
4. **Immutable Assignments**: Once assigned, an ID **SHALL NOT** be reassigned to a different artifact.

#### 4.2.3 Cross-ATA Namespace Coordination

For artifacts spanning multiple ATAs (e.g., `ATA24-REQ-001` referenced by ATA 27):

1. **Origin namespace retains authority**: `ATA24` owns `ATA24-REQ-001` lifecycle.
2. **Cross-references use full ID**: `ATA27-FHA-005` references `ATA24-REQ-001` (not `REQ-001`).
3. **ATA 99 dedup check**: All cross-ATA IDs checked against master registry.

### 4.3 Sequence Number Management

#### 4.3.1 Sequence Allocation Rules

1. **Monotonic increment**: Sequences **SHALL** increment without gaps or reuse.
2. **Zero-padding**: Sequences **SHALL** be zero-padded to minimum width (3-6 digits).
3. **No semantic meaning**: Sequence numbers **SHALL NOT** encode semantic information.
4. **Auto-generation preferred**: Tooling **SHOULD** auto-generate sequences to prevent collisions.

#### 4.3.2 Sequence Ranges (Optional Partitioning)

Namespaces **MAY** partition sequence ranges for organizational purposes:

| Range | Purpose | Example |
| :--- | :--- | :--- |
| `001-099` | Reserved for governance | `REQ-SYS-001` |
| `100-999` | Normal operations | `REQ-SYS-100` |
| `1000-9999` | High-volume artifacts | `TC-SW-1000` |

**Important**: Range partitioning is **advisory only** and does not affect uniqueness.

### 4.4 Variant and Versioning

#### 4.4.1 Variant Suffix Rules

The optional `VARIANT` suffix is used for:

- **Item variants**: `REQ-SYS-001-A`, `REQ-SYS-001-B` (alternative designs)
- **Draft indicators**: `FHA-PROP-042-DRAFT` (pre-approval state)
- **Version tags**: `SCH-DATA-005-V02` (schema version)

**Constraints**:
1. Variants **SHALL NOT** change the base ID (`REQ-SYS-001` is constant).
2. Variants **SHALL** be uppercase alphanumeric (hyphens allowed within).
3. Variants **SHOULD** be coordinated with ATA 93 for trace link integrity.

#### 4.4.2 File vs. Internal ID Versioning

| Context | Version Location | Example |
| :--- | :--- | :--- |
| **File identifiers** | In filename (per Nomenclature v2.0) | `00_00_STD_LC01_SPACET_identifier-grammar_v01.md` |
| **Internal artifact IDs** | In variant suffix (optional) | `REQ-SYS-001` (immutable base) |
| **Schema definitions** | In variant suffix (required) | `SCH-DATA-005-V02` |

### 4.5 Namespace Boundaries and Shadow Registry Prevention

#### 4.5.1 Boundary Definition

A **namespace boundary** is the organizational or technical limit of an identifier authority's jurisdiction.

**Example Boundaries**:
- **ATA Chapter**: `ATA24` controls all `ATA24-*` identifiers
- **Artifact Type**: `REQ` namespace controls all `REQ-*` identifiers
- **Lifecycle Phase**: `LC02` artifacts may have distinct namespace `LC02-*`

#### 4.5.2 Shadow Registry Detection and Prevention

**Prohibited**: Parallel or uncoordinated identifier lists outside ATA 99 master registry.

**Detection mechanisms** (enforced by CI):
1. **Duplicate ID scan**: All IDs checked against ATA 99 registry on commit.
2. **Unregistered namespace detection**: New namespaces flagged if not in registry.
3. **Cross-file ID uniqueness**: No two files may declare same canonical ID.

**Remediation**:
- **Detected shadow registry**: CM team resolves conflicts and migrates to ATA 99.
- **Duplicate ID**: Offending ID reassigned; trace links updated.

## 5. Enforcement

### 5.1 Validation Mechanisms

| Mechanism | Frequency | Responsibility |
| :--- | :--- | :--- |
| **CI/CD pre-commit hook** | Every commit | Automated |
| **ATA 99 registry check** | Pull request | Automated |
| **Manual CM review** | Governance-impacting changes | CM WG |
| **Quarterly audit** | Every quarter | CM WG + Auditors |

### 5.2 CI/CD Pipeline Integration

**Pre-commit checks**:
```bash
# Validate identifier grammar
python scripts/validate_identifiers.py --file <file>

# Check against ATA 99 registry
python scripts/check_ata99_registry.py --namespace <NS>

# Detect shadow registries
python scripts/detect_shadow_registries.py --all
```

### 5.3 Non-Compliance Remediation

| Severity | Issue | Action |
| :--- | :--- | :--- |
| **Critical** | Duplicate ID across artifacts | Immediate halt; CM reassignment |
| **High** | Unregistered namespace in use | Register with ATA 99 or refactor |
| **Medium** | Grammar non-conformance | Reject PR; request correction |
| **Low** | Missing zero-padding | Auto-fix in CI or manual correction |

### 5.4 Governance Change Control

Changes to this standard **SHALL** require:
1. **CM WG approval** (consensus or majority vote)
2. **ATA 99 coordination** (namespace impacts)
3. **Baseline update entry** (version increment)
4. **Evidence pack update** (auditability)

## 6. Appendices

### Appendix A: Identifier Grammar Regex

```regex
^[A-Z0-9]{2,5}-[A-Z0-9]{2,4}-\d{3,6}(-[A-Z0-9]{1,8})?$
```

**Breakdown**:
- `[A-Z0-9]{2,5}`: NAMESPACE (2-5 uppercase alphanumeric)
- `-`: Separator
- `[A-Z0-9]{2,4}`: CATEGORY (2-4 uppercase alphanumeric)
- `-`: Separator
- `\d{3,6}`: SEQUENCE (3-6 digits)
- `(-[A-Z0-9]{1,8})?`: Optional VARIANT (1-8 uppercase alphanumeric)

### Appendix B: Integration with ATA 99

**Workflow**:
1. **Namespace registration**: Submit request to ATA 99 with justification
2. **ATA 99 review**: Check for conflicts and approve/reject
3. **Registry update**: ATA 99 adds namespace to master registry
4. **Tooling update**: CI scripts fetch updated registry
5. **Issue authority**: Namespace owner may now issue IDs

**ATA 99 Registry Schema** (reference):
```json
{
  "namespace": "REQ",
  "authority": "Requirements Team",
  "scope": "All system, SW, HW requirements",
  "contact": "req-team@ampel360.space",
  "registered_date": "2025-12-14",
  "status": "active"
}
```

### Appendix C: Quick Reference Table

| Use Case | Identifier Pattern | Example |
| :--- | :--- | :--- |
| System requirement | `REQ-SYS-[NNN]` | `REQ-SYS-042` |
| Software requirement | `REQ-SW-[NNN]` | `REQ-SW-123` |
| Hazard (FHA) | `HAZ-[ATA]-[NNN]` | `HAZ-PROP-007` |
| Test case | `TC-[DOMAIN]-[NNNN]` | `TC-SW-1042` |
| Schema definition | `SCH-[TYPE]-[NNN]-V[NN]` | `SCH-DATA-005-V02` |
| Trace link | `TRC-[SRC]-[DST]-[NNN]` | `TRC-REQ-TC-001` |
| Evidence pack | `EVD-[LC]-[NNN]` | `EVD-LC02-003` |
| Baseline | `BL-[YYYY]-[MM]-[VV]` | `BL-2025-12-01` |

---

**Document Control**

| Field | Value |
| :--- | :--- |
| **Version** | v01 |
| **Status** | Normative |
| **Owner** | Configuration Management WG |
| **Last Updated** | 2025-12-14 |
| **Next Review** | 2026-06-14 (6 months) |
| **Approvals** | Pending CM WG sign-off |
