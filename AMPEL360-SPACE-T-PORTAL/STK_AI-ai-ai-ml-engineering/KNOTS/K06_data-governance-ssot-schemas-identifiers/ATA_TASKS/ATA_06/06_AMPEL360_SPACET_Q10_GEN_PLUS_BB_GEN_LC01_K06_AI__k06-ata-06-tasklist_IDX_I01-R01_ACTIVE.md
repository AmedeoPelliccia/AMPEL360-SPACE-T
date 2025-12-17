---
title: "K06 ATA 06 Tasklist"
type: IDX
variant: SPACET
status: Draft
knot_id: K06
ata: "06"
lc_or_subbucket: "LC01"
---

# K06 — data-governance-ssot-schemas-identifiers
## ATA 06 — Tasklist (Dimensions and Areas)

## Links (GitHub-navigable)
- Knot overview: [K06 overview](../../../../../STK_DATA-data-data-governance/KNOTS/K06_data-governance-ssot-schemas-identifiers/00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_LC01_K06_DATA__k06-data-governance-ssot-schemas-identifiers_IDX_I01-R01_ACTIVE.md)
- Portal index: [AMPEL360-SPACE-T-PORTAL index](../../../../../00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_LC01_K04_CM__stakeholder-entrypoints_IDX_I01-R01_ACTIVE.md)
- Stakeholder entrypoint (AI): [STK_AI entrypoint](../../../../00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_LC01_K11_AI__stakeholder-ai-entrypoint_IDX_I01-R01_ACTIVE.md)
- ATA 06 home (P-PROGRAM): [AMPEL360_SPACE-T/P-PROGRAM/ATA 06](../../../../../../AMPEL360_SPACE-T/P-PROGRAM/ATA_06-DIMENSIONS_AND_AREAS/)
  - If your folder name differs, update only this link target.

## Related K06 tasklists
- [ATA 00 (Program Governance)](../ATA_00/)
- [ATA 91 (Schemas)](../ATA_91/)
- [ATA 93 (Traceability Graph)](../ATA_93/)
- [ATA 99 (Master Registers)](../ATA_99/)

---

## 1) Uncertainty to Resolve (ATA-specific)
For ATA 06 (Dimensions and Areas), the K06 uncertainty is to define a **single authoritative geometry/envelope SSOT** that is:
- **Identified** via canonical IDs (datums, zones, keep-outs, service envelopes, access volumes).
- **Versioned** with stable schema rules so tooling and downstream ATAs can consume it.
- **Traceable** to requirements, safety constraints, and infrastructure compatibility assumptions.

### Decision required
A CM-approved decision covering:
- Which dataset is authoritative (CAD SSOT / derived exports / published tables).
- Identifier grammar for datums/zones/envelopes.
- Publication format(s) and schema versioning policy.
- CI validation rules for geometry/envelope artifacts.

## 2) Scope Boundary
### In-scope
- Geometry/envelope **identifier set** (datums, zones, areas, envelopes).
- Canonical “areas & dimensions” schema (fields, units, tolerances, coordinate frames).
- Publication routes (e.g., CSV/JSON + diagrams + extracted metadata) and versioning.
- CI checks: naming + metadata + schema validation + unit consistency checks.

### Out-of-scope
- Full CAD modeling methodology (owned by design tooling unless pulled into this knot).
- Spaceport facility design (handled in ATA 80–89; linked only via interface constraints).

## 3) Owners & Stakeholders
- **Primary owner:** SE + DATA (with AI supporting extraction/validation automation)
- **Approvers:** CM WG
- **Contributors:** STR, OPS, SPACEPORT, CERT, TEST

## 4) Interfaces / Affected Areas
### Key dependencies
- Datum policy and coordinate frames used across ATAs (K04 integration boundary risk).
- Spaceport compatibility envelopes (ATA 80–89) consume ATA 06 data.
- Sim/test correlation may require “frozen envelope sets” (ATA 101/113/116).

### Authoritative targets (SSOT candidates)
- `AMPEL360_SPACE-T/P-PROGRAM/ATA_06-DIMENSIONS_AND_AREAS/`
- `AMPEL360_SPACE-T/N-NEURAL_NETWORKS/ATA_91-*` (schema definitions)
- `AMPEL360_SPACE-T/N-NEURAL_NETWORKS/ATA_93-*` (traceability evidence)

## 5) Closure Criteria
This tasklist is **closed only if** all conditions are true:
1. Canonical IDs for areas/dimensions/envelopes are defined and published.
2. A schema (fields, units, coordinate frames, tolerances) is published and versioned.
3. CI validations exist (schema + units + basic consistency) and are documented.
4. A “golden export” baseline exists (frozen set) and is referenced by downstream ATAs (80–89, 101+ as applicable).
5. Baseline change record is created and trace links updated.

## 6) Tasks (minimum set)
### 6.1 Define SSOT and identifiers
- [x] **T1** Define authoritative source (CAD vs derived tables) and ownership. ✅ **COMPLETE**
- [x] **T2** Define identifier grammar for datums/zones/envelopes (stable, unique). ✅ **COMPLETE**
- [x] **T3** Define schema: units, coordinate frame, tolerances, metadata. ✅ **COMPLETE**

### 6.2 Publish and enforce
- [ ] **T4** Publish canonical exports (CSV/JSON) + minimal diagram references.
- [ ] **T5** Implement CI validation: schema checks + unit checks + required fields.

### 6.3 Evidence and adoption
- [ ] **T6** Produce a frozen “baseline envelope set” with release manifest.
- [ ] **T7** Link downstream consumers (Ops/Infra/Sim) and record adoption evidence.

## 7) Outputs / Artifacts
- Identifier set and registry entries (ATA 00 + ATA 06)
- Schema definition (ATA 91)
- Frozen baseline export pack (linked to release)
- CI validation logs (evidence)
- Traceability links (ATA 93)

## 8) Dependencies / Risks
- Risk: multiple competing “truths” (CAD vs spreadsheets vs diagrams) without SSOT.
- Risk: unit/frame mismatches causing downstream integration errors (K04 coupling).
- Dependency: CM approval and registry governance (ATA 00).

---

## T1 Resolution: Authoritative Source and Ownership

### Decision

**CAD models are designated as the Single Source of Truth (SSOT) for ATA-06 dimensional data.**

### Authoritative Source Definition

| Attribute | Value |
| :--- | :--- |
| **SSOT Type** | CAD Models (CATIA V6 / NX / SolidWorks) |
| **Authority** | Authoritative |
| **Location** | Design Engineering CAD Repository |
| **Rationale** | Primary design authority; engineering integration; version control; geometry accuracy; change traceability |

### Derived Sources (NOT authoritative)

| Source Type | Status | Usage | Update Trigger |
| :--- | :--- | :--- | :--- |
| Spreadsheets | Derived | Analysis, quick reference | When CAD changes |
| Diagrams | Derived | Communication, documentation | When CAD changes |
| Presentations | Derived | Reviews, approvals | When CAD changes |
| Simulation Models | Derived | Analysis input | When CAD changes |
| Manufacturing Drawings | Derived | Fabrication | When CAD changes |
| JSON/CSV Exports | Derived | Machine-readable distribution | When CAD changes |

**Conflict Resolution Rule**: If spreadsheet, diagram, or document conflicts with CAD, **CAD is correct**.

### Ownership Model

| Role | Team | Responsibility | Authority Level |
| :--- | :--- | :--- | :--- |
| **Primary Owner** | Design Engineering | CAD model maintenance, export generation | Update CAD |
| **Data Custodian** | Configuration Management WG | Baseline approval, governance | Approve baselines |
| **Technical Authority** | Systems Engineering | Schema definition, validation rules | Define requirements |
| **Tooling Owner** | DevOps | CI pipeline, automation | Implement validation |
| **Consumers** | Ops/Infra/Sim Teams | Use canonical exports, report issues | Read-only access |

### Decision Authority Matrix

| Decision Type | Authority | Process |
| :--- | :--- | :--- |
| Dimensional changes | Design Engineering + Chief Engineer | ECR/ECO process |
| Baseline release | Configuration Management WG | CM review and approval |
| Schema changes | Systems Engineering + CM WG | Change control board |
| Export format | Systems Engineering | Technical review |

### Evidence and References

| Evidence | Document ID | Status |
| :--- | :--- | :--- |
| SSOT Implementation Plan | F_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_LC01_K06_CM__ssot-implementation-plan_I01-R01.md` | Published |
| SSOT Decision Matrix | `00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_LC01_K04_DATA__ssot-decision-matrix_I01-R01.md` | Published |
| Identifier Registry | F_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_LC01_K06_CM__identifier-registry_I01-R01.md` | Published |

### Approval

| Role | Status | Date |
| :--- | :--- | :--- |
| CM WG Lead | Documented | 2025-12-16 |

---

## T2 Resolution: Identifier Grammar for Datums/Zones/Envelopes

### Decision

**A canonical identifier grammar has been defined for all ATA-06 dimensional data elements (datums, zones, envelopes).**

### Identifier Grammar

All ATA-06 identifiers follow this grammar:

```
{CATEGORY}-{SYSTEM}-{SEQUENCE}[-{VARIANT}]
```

### Grammar Components

| Component | Description | Format | Required |
| :--- | :--- | :--- | :--- |
| **CATEGORY** | Artifact type | `DATUM` \| `ZONE` \| `ENVELOPE` | Yes |
| **SYSTEM** | System code | 2-5 uppercase alphanumeric | Yes |
| **SEQUENCE** | Sequence number | 3-digit zero-padded | Yes |
| **VARIANT** | Sub-variant | 1-8 uppercase alphanumeric | Optional |

### System Codes

| Code | System Name | Description |
| :--- | :--- | :--- |
| **GLOBAL** | Global | Spacecraft-level references |
| **FUS** | Fuselage | Main body structure |
| **PROP** | Propulsion | Engines, tanks, propellant systems |
| **AVION** | Avionics | Electronics, computers, sensors |
| **POWER** | Power | Electrical power generation |
| **THERM** | Thermal | Thermal control systems |
| **STRUCT** | Structure | Primary and secondary structure |
| **MECH** | Mechanisms | Deployables, actuators |
| **PAYLOAD** | Payload | Mission-specific equipment |
| **GNC** | Guidance/Nav/Control | GNC sensors and actuators |
| **COMM** | Communications | Antennas, transceivers |
| **INTEG** | Integration | Cross-system interfaces |

### Identifier Examples

| Identifier | Description |
| :--- | :--- |
| `DATUM-GLOBAL-001` | Spacecraft Primary Datum Origin |
| `DATUM-GLOBAL-002` | Spacecraft X-Axis Reference Line |
| `DATUM-FUS-001` | Fuselage Station 0 (FS0) |
| `ZONE-PROP-001` | Main Propulsion Module Zone |
| `ZONE-INTEG-001` | Launch Vehicle Interface Zone |
| `ENVELOPE-GLOBAL-001` | Launch Configuration Envelope |
| `ENVELOPE-PROP-001` | Propulsion Module Envelope |
| `ENVELOPE-STRUCT-001` | Primary Structure Keep-Out |

### Stability and Uniqueness Rules

| Rule | Description |
| :--- | :--- |
| **Permanence** | Identifiers are permanent once allocated |
| **No Reuse** | Deprecated identifiers are never reused |
| **Historical Record** | Superseded identifiers maintain pointer to replacement |
| **Full ID Unique** | Each full identifier (e.g., `DATUM-GLOBAL-001`) is globally unique |
| **Sequence Scope** | Sequence numbers are allocated within {CATEGORY}-{SYSTEM} scope (e.g., `DATUM-GLOBAL-001` and `ZONE-GLOBAL-001` both valid) |
| **Immutable Base** | Identifiers themselves do not version; values may change |

### Identifier Allocation Process

1. **Check Registry**: Verify identifier doesn't already exist
2. **Determine Category**: DATUM, ZONE, or ENVELOPE
3. **Select System**: Use approved system code
4. **Assign Sequence**: Next available sequence number
5. **Document**: Create catalog entry with all required fields
6. **Submit**: Send to Configuration Management WG for approval
7. **Publish**: Add to registry and update statistics

### Evidence and References

| Evidence | Document ID | Status |
| :--- | :--- | :--- |
| Identifier Registry | F_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_LC01_K06_CM__identifier-registry_I01-R01.md` | Published |
| Identifier Grammar Standard | `00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_LC01_K04_DATA__identifier-grammar_I01-R01.md` | Published |

### Approval

| Role | Status | Date |
| :--- | :--- | :--- |
| CM WG Lead | Documented | 2025-12-16 |

---

## T3 Resolution: Schema Definition (Units, Coordinate Frame, Tolerances, Metadata)

### Decision

**A comprehensive dimensional data schema has been defined for ATA-06 data elements.**

### Schema Location

All schema artifacts have been moved to PORTAL root:
- F_AMPEL360_SPACET_GEN_90_SCH_SB90_K06_CM__dimensional-data-schema_I01-R01.json`
- F_AMPEL360_SPACET_GEN_90_SCH_SB90_K06_CM__dimensional-data-schema_I01-R01.md`
- F_AMPEL360_SPACET_GEN_90_TAB_SB90_K06_CM__dimensional-exports_I01-R01.json`

### Schema Components

| Component | Definition | Standard |
| :--- | :--- | :--- |
| **Units** | SI units (mm for length, deg for angles) | ISO 80000 |
| **Coordinate Frame** | Right-handed Cartesian (X forward, Y right, Z down) | Aerospace convention |
| **Origin** | DATUM-GLOBAL-001 (launch adapter interface center) | Project-specific |
| **Tolerances** | Positional: ±0.1mm to ±0.5mm; Angular: ±0.05° | Per feature type |

### Metadata Fields

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `identifier` | string | Yes | Unique ID per grammar |
| `name` | string | Yes | Human-readable name |
| `category` | enum | Yes | DATUM, ZONE, ENVELOPE |
| `system` | string | Yes | System code |
| `status` | enum | Yes | Active, Deprecated, Superseded |
| `version` | string | Yes | CAD baseline version |
| `owner` | string | Yes | Responsible team |
| `cad_location` | string | Yes | Path in CAD model |

### Coordinate Frame Definition

```
Origin: DATUM-GLOBAL-001 (Launch Vehicle Adapter Interface Center)
X-axis: Forward (nose direction) - DATUM-GLOBAL-002
Y-axis: Right (starboard)
Z-axis: Down (nadir in launch config)
Handedness: Right-handed
Units: Millimeters (mm)
```

### Evidence and References

| Evidence | Document ID | Status |
| :--- | :--- | :--- |
| Schema Definition (JSON) | F_AMPEL360_SPACET_GEN_90_SCH_SB90_K06_CM__dimensional-data-schema_I01-R01.json` | Published |
| Schema Documentation | F_AMPEL360_SPACET_GEN_90_SCH_SB90_K06_CM__dimensional-data-schema_I01-R01.md` | Published |
| Dimensional Exports | F_AMPEL360_SPACET_GEN_90_TAB_SB90_K06_CM__dimensional-exports_I01-R01.json` | Published |

### Approval

| Role | Status | Date |
| :--- | :--- | :--- |
| CM WG Lead | Documented | 2025-12-16 |
