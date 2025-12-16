---
title: "ATA-06 Identifier Registry - Datums, Zones, and Envelopes"
type: CAT
variant: "SPACET"
catalog_type: "Identifier Registry"
status: Draft
ata_chapter: "06"
owner: "Configuration Management WG"
related_docs: ["06_00_IDX_LC01_SPACET_k06-ata-06-tasklist_v01.md", "06_00_PLAN_LC01_SPACET_ssot-implementation-plan_v01.md"]
---

# ATA-06 Identifier Registry - Datums, Zones, and Envelopes

## 1. Catalog Overview

### 1.1 Purpose

This registry defines and catalogs all unique identifiers for ATA-06 dimensional data elements, including:
- **Datums**: Reference points and surfaces for dimensional measurement
- **Zones**: Spatial regions with defined boundaries
- **Envelopes**: Maximum dimensional boundaries for components or systems

The registry addresses Task T2 from the ATA-06 tasklist: "Define identifier grammar for datums/zones/envelopes (stable, unique)."

### 1.2 Scope

**IN SCOPE:**
- All spacecraft dimensional reference identifiers
- Datum definitions (point, line, plane, coordinate systems)
- Zone boundaries (spatial regions for integration, thermal, structural)
- Envelope limits (keep-out zones, maximum dimensions)
- Identifier grammar and allocation rules

**OUT OF SCOPE:**
- Actual dimensional values (maintained in SSOT/CAD)
- Non-dimensional identifiers (part numbers, assembly codes)
- External reference systems (launch vehicle interfaces handled separately)

### 1.3 Organization

Identifiers are organized into three primary categories with consistent grammar:
1. **DATUM**: Reference points, lines, planes, and coordinate systems
2. **ZONE**: Spatial regions for integration and analysis
3. **ENVELOPE**: Maximum dimensional boundaries

## 2. Identifier Grammar

### 2.1 General Rules

All ATA-06 identifiers follow this grammar:

```
{CATEGORY}-{SYSTEM}-{SEQUENCE}[-{VARIANT}]
```

**Field Definitions:**
- **CATEGORY**: `DATUM` | `ZONE` | `ENVELOPE`
- **SYSTEM**: 2-3 character system code (e.g., `FUS` for fuselage, `PROP` for propulsion)
- **SEQUENCE**: 3-digit zero-padded sequence number within category and system
- **VARIANT** (optional): Variant or sub-identifier (e.g., `A`, `B`, `X`, `Y`, `Z` for axes)

**Examples:**
- `DATUM-FUS-001`: Primary fuselage datum
- `ZONE-PROP-042-A`: Propulsion zone 42, variant A
- `ENVELOPE-STRUCT-010`: Structural envelope 10

### 2.2 Stability and Uniqueness Rules

**Stability:**
- Identifiers are **permanent** once allocated
- Deprecated identifiers are **never reused**
- Superseded identifiers maintain historical record with pointer to replacement

**Uniqueness:**
- Each identifier is unique across all categories and systems
- Sequence numbers are unique within {CATEGORY}-{SYSTEM} scope
- Variants extend, not replace, base identifier

**Versioning:**
- Identifiers themselves do not version (they are stable references)
- Dimensional values may change, but identifier remains constant
- Changes tracked in CAD version control and change history

### 2.3 System Codes

| System Code | System Name | Description |
| :--- | :--- | :--- |
| **FUS** | Fuselage | Main body structure |
| **PROP** | Propulsion | Engines, tanks, propellant systems |
| **AVION** | Avionics | Electronics, computers, sensors |
| **POWER** | Power | Electrical power generation and distribution |
| **THERM** | Thermal | Thermal control systems |
| **STRUCT** | Structure | Primary and secondary structure |
| **MECH** | Mechanisms | Deployables, actuators, mechanisms |
| **PAYLOAD** | Payload | Mission-specific payload equipment |
| **GNC** | Guidance/Nav/Control | GNC sensors and actuators |
| **COMM** | Communications | Antennas, transceivers |
| **INTEG** | Integration | Cross-system integration interfaces |
| **GLOBAL** | Global | Spacecraft-level references |

## 3. Catalog Entries

### 3.1 Category: DATUM - Reference Datums and Coordinate Systems

Datums define reference points, lines, planes, and coordinate systems for dimensional measurement.

---

#### DATUM-GLOBAL-001: Spacecraft Primary Datum Origin

| Field | Value |
| :--- | :--- |
| **ID:** | DATUM-GLOBAL-001 |
| **Name:** | Spacecraft Primary Datum Origin |
| **Category:** | DATUM |
| **System:** | GLOBAL |
| **Type:** | Point (Coordinate System Origin) |
| **Status:** | Active |
| **Version:** | CAD Baseline v1.0 |
| **Owner:** | Design Engineering |
| **CAD Location:** | Main Assembly → Datum Features → Primary Origin |

**Description:**
The primary datum origin for the entire spacecraft. All dimensional measurements reference this origin. Defined at the geometric center of the launch vehicle adapter interface.

**Specifications:**
- **Coordinate Frame**: Right-handed Cartesian (X forward, Y right, Z down per aerospace convention)
- **Units**: Millimeters (mm)
- **Tolerance**: ±0.1 mm positional accuracy
- **Reference Standard**: Per ATA-06 SSOT Implementation Plan

**Related Items:**
- DATUM-GLOBAL-002 (X-axis reference)
- DATUM-GLOBAL-003 (XY reference plane)
- All zone and envelope identifiers

**References:**
- 06_00_PLAN_LC01_SPACET_ssot-implementation-plan_v01.md
- CAD Model: SpaceT_Main_Assembly_v1.0

---

#### DATUM-GLOBAL-002: Spacecraft X-Axis Reference Line

| Field | Value |
| :--- | :--- |
| **ID:** | DATUM-GLOBAL-002 |
| **Name:** | Spacecraft X-Axis Reference Line |
| **Category:** | DATUM |
| **System:** | GLOBAL |
| **Type:** | Line (Axis) |
| **Status:** | Active |
| **Version:** | CAD Baseline v1.0 |
| **Owner:** | Design Engineering |
| **CAD Location:** | Main Assembly → Datum Features → X-Axis |

**Description:**
Primary X-axis defining the forward direction of the spacecraft. Aligned with the longitudinal axis through the center of mass and launch vehicle interface.

**Specifications:**
- **Direction**: Forward (nose direction)
- **Origin**: DATUM-GLOBAL-001
- **Tolerance**: ±0.05° angular tolerance
- **Unit Vector**: [1, 0, 0]

**Related Items:**
- DATUM-GLOBAL-001 (origin)
- DATUM-GLOBAL-003 (defines XY plane)

**References:**
- Coordinate Frame Definition Document

---

#### DATUM-FUS-001: Fuselage Station 0 (FS0)

| Field | Value |
| :--- | :--- |
| **ID:** | DATUM-FUS-001 |
| **Name:** | Fuselage Station 0 (FS0) |
| **Category:** | DATUM |
| **System:** | FUS |
| **Type:** | Plane (YZ plane) |
| **Status:** | Active |
| **Version:** | CAD Baseline v1.0 |
| **Owner:** | Design Engineering |
| **CAD Location:** | Fuselage Assembly → Reference Planes → FS0 |

**Description:**
Fuselage Station 0 defines the forward-most reference plane for fuselage measurements. Perpendicular to DATUM-GLOBAL-002 (X-axis).

**Specifications:**
- **Plane Normal**: X-axis (forward)
- **Position**: X = 0 mm at DATUM-GLOBAL-001
- **Tolerance**: ±0.5 mm
- **Usage**: All fuselage station measurements (FS) reference this plane

**Related Items:**
- DATUM-FUS-002 through DATUM-FUS-050 (subsequent fuselage stations)
- ZONE-FUS-* (fuselage zones reference FS datums)

**References:**
- Fuselage Layout Drawing

---

### 3.2 Category: ZONE - Spatial Regions

Zones define spatial regions for integration, thermal analysis, structural analysis, and operational clearances.

---

#### ZONE-PROP-001: Main Propulsion Module Zone

| Field | Value |
| :--- | :--- |
| **ID:** | ZONE-PROP-001 |
| **Name:** | Main Propulsion Module Zone |
| **Category:** | ZONE |
| **System:** | PROP |
| **Type:** | Volumetric Zone (Cuboid) |
| **Status:** | Active |
| **Version:** | CAD Baseline v1.0 |
| **Owner:** | Propulsion Engineering |
| **CAD Location:** | Main Assembly → Zones → Propulsion → Zone_001 |

**Description:**
Primary integration zone for the main propulsion module, including engines, tanks, and feed systems.

**Specifications:**
- **Bounds**: 
  - X: 2000 mm to 4500 mm (FS200 to FS450)
  - Y: -1200 mm to +1200 mm
  - Z: -1500 mm to +500 mm
- **Volume**: ~13.2 m³
- **Purpose**: Integration envelope, thermal analysis, mass properties
- **Clearance**: 50 mm minimum to adjacent zones

**Related Items:**
- ENVELOPE-PROP-001 (propulsion envelope limits)
- ZONE-STRUCT-005 (adjacent structural zone)
- DATUM-FUS-020 (reference station)

**References:**
- Propulsion Integration Plan
- Thermal Analysis Model Zone Definitions

---

#### ZONE-INTEG-001: Launch Vehicle Interface Zone

| Field | Value |
| :--- | :--- |
| **ID:** | ZONE-INTEG-001 |
| **Name:** | Launch Vehicle Interface Zone |
| **Category:** | ZONE |
| **System:** | INTEG |
| **Type:** | Annular Zone |
| **Status:** | Active |
| **Version:** | CAD Baseline v1.0 |
| **Owner:** | Integration Engineering |
| **CAD Location:** | Main Assembly → Zones → Integration → LV_Interface |

**Description:**
Integration zone at the launch vehicle adapter interface. Defines the region where spacecraft interfaces with launch vehicle.

**Specifications:**
- **Bounds**: 
  - X: -200 mm to 0 mm (aft of FS0)
  - Radial: 800 mm to 1500 mm (annular region)
- **Interface Standard**: Launch Vehicle ICD Rev C
- **Bolt Pattern**: 24 × M12 bolts on 1200 mm bolt circle
- **Clearance**: No spacecraft hardware within 100 mm of bolt holes

**Related Items:**
- DATUM-GLOBAL-001 (interface origin)
- ENVELOPE-GLOBAL-001 (launch configuration envelope)

**References:**
- Launch Vehicle Interface Control Document (ICD)
- Adapter Design Specification

---

### 3.3 Category: ENVELOPE - Dimensional Limits

Envelopes define maximum dimensional boundaries that components or systems must not exceed.

---

#### ENVELOPE-GLOBAL-001: Launch Configuration Envelope

| Field | Value |
| :--- | :--- |
| **ID:** | ENVELOPE-GLOBAL-001 |
| **Name:** | Launch Configuration Envelope |
| **Category:** | ENVELOPE |
| **System:** | GLOBAL |
| **Type:** | Cylindrical Envelope with Truncated Cone |
| **Status:** | Active |
| **Version:** | CAD Baseline v1.0 |
| **Owner:** | Systems Engineering |
| **CAD Location:** | Main Assembly → Envelopes → Launch_Config |

**Description:**
Maximum allowable envelope for the spacecraft in launch configuration (stowed). Must fit within launch vehicle fairing.

**Specifications:**
- **Cylindrical Section**: 
  - Diameter: 4800 mm max (4700 mm allocation, 100 mm margin)
  - Length (X): 6000 mm max
- **Cone Section** (forward):
  - Half-angle: 30°
  - Height: 1500 mm
- **Mass**: ≤ 5000 kg (launch mass limit)
- **CG Limits**: X = 3000 ± 200 mm

**Related Items:**
- ENVELOPE-GLOBAL-002 (on-orbit deployed envelope)
- All zone identifiers (must fit within launch envelope)

**References:**
- Launch Vehicle Fairing Envelope Drawing
- Mission Requirements Document

---

#### ENVELOPE-PROP-001: Propulsion Module Envelope

| Field | Value |
| :--- | :--- |
| **ID:** | ENVELOPE-PROP-001 |
| **Name:** | Propulsion Module Envelope |
| **Category:** | ENVELOPE |
| **System:** | PROP |
| **Type:** | Cuboid Keep-Out Zone |
| **Status:** | Active |
| **Version:** | CAD Baseline v1.0 |
| **Owner:** | Propulsion Engineering |
| **CAD Location:** | Propulsion Assembly → Envelope_Max |

**Description:**
Maximum envelope allocated to propulsion module. No propulsion hardware may extend beyond this envelope.

**Specifications:**
- **Bounds**:
  - X: 2000 mm to 4500 mm
  - Y: -1200 mm to +1200 mm  
  - Z: -1500 mm to +500 mm
- **Volume**: 13.2 m³
- **Mass Allocation**: ≤ 800 kg (propulsion dry mass)
- **Thermal**: Must accommodate propellant tanks at -10°C to +50°C

**Related Items:**
- ZONE-PROP-001 (associated integration zone)
- ENVELOPE-GLOBAL-001 (must fit within global envelope)

**References:**
- Propulsion Subsystem Specification

---

#### ENVELOPE-STRUCT-001: Primary Structure Keep-Out

| Field | Value |
| :--- | :--- |
| **ID:** | ENVELOPE-STRUCT-001 |
| **Name:** | Primary Structure Keep-Out Envelope |
| **Category:** | ENVELOPE |
| **System:** | STRUCT |
| **Type:** | Complex 3D Surface (CAD-defined) |
| **Status:** | Active |
| **Version:** | CAD Baseline v1.0 |
| **Owner:** | Structural Engineering |
| **CAD Location:** | Structure Assembly → Keep_Out_Surface |

**Description:**
Keep-out envelope defining the space occupied by primary structure. No other subsystems may intrude into this envelope without structural coordination.

**Specifications:**
- **Definition**: Complex 3D surface defined in CAD
- **Clearance**: 20 mm minimum between structure and adjacent subsystems
- **Load Paths**: Primary load paths protected within envelope
- **Access**: Maintenance access ports excluded from keep-out

**Related Items:**
- Multiple ZONE-* identifiers (zones must not conflict)
- ENVELOPE-GLOBAL-001 (structural envelope within global)

**References:**
- Structural Layout Drawing
- Structural Design Specification

---

## 4. Indexes

### 4.1 Alphabetical Index

- **C**
  - Communications → see System Code: COMM
  - Coordinate Frame → DATUM-GLOBAL-001, DATUM-GLOBAL-002
- **D**
  - Datum Origin → DATUM-GLOBAL-001
- **E**
  - Envelope (Launch) → ENVELOPE-GLOBAL-001
  - Envelope (Propulsion) → ENVELOPE-PROP-001
  - Envelope (Structure) → ENVELOPE-STRUCT-001
- **F**
  - Fuselage Station 0 → DATUM-FUS-001
- **I**
  - Integration Zone → ZONE-INTEG-001
  - Interface (Launch Vehicle) → ZONE-INTEG-001
- **L**
  - Launch Configuration → ENVELOPE-GLOBAL-001
  - Launch Vehicle Interface → ZONE-INTEG-001
- **P**
  - Primary Datum → DATUM-GLOBAL-001
  - Propulsion Module → ZONE-PROP-001, ENVELOPE-PROP-001
- **S**
  - Spacecraft Origin → DATUM-GLOBAL-001
  - Structure Keep-Out → ENVELOPE-STRUCT-001
- **X**
  - X-Axis → DATUM-GLOBAL-002
- **Z**
  - Zone (Propulsion) → ZONE-PROP-001
  - Zone (Integration) → ZONE-INTEG-001

### 4.2 By Category

- **DATUM:** DATUM-GLOBAL-001, DATUM-GLOBAL-002, DATUM-FUS-001
- **ZONE:** ZONE-PROP-001, ZONE-INTEG-001
- **ENVELOPE:** ENVELOPE-GLOBAL-001, ENVELOPE-PROP-001, ENVELOPE-STRUCT-001

### 4.3 By System

- **GLOBAL:** DATUM-GLOBAL-001, DATUM-GLOBAL-002, ENVELOPE-GLOBAL-001
- **FUS:** DATUM-FUS-001
- **PROP:** ZONE-PROP-001, ENVELOPE-PROP-001
- **STRUCT:** ENVELOPE-STRUCT-001
- **INTEG:** ZONE-INTEG-001

### 4.4 By Status

- **Active:** All current identifiers (8 total in this baseline)
- **Deprecated:** None
- **Superseded:** None

## 5. Statistics

| Metric | Count |
| :--- | :--- |
| **Total Identifiers** | 8 |
| **DATUM** | 3 |
| **ZONE** | 2 |
| **ENVELOPE** | 3 |
| **Active** | 8 |
| **Deprecated** | 0 |
| **Superseded** | 0 |
| **Systems Represented** | 5 (GLOBAL, FUS, PROP, STRUCT, INTEG) |
| **Last Added** | 2025-12-15 |

## 6. Identifier Allocation Process

### 6.1 Request Procedure

To allocate a new identifier:

1. **Check Registry**: Verify identifier doesn't already exist
2. **Determine Category**: DATUM, ZONE, or ENVELOPE
3. **Select System**: Use approved system code or request new code
4. **Assign Sequence**: Next available sequence number in {CATEGORY}-{SYSTEM}
5. **Document**: Create catalog entry with all required fields
6. **Submit**: Send to Configuration Management WG for approval
7. **Approve**: CM WG reviews and approves
8. **Publish**: Add to registry and update statistics

### 6.2 Identifier Deprecation

If an identifier is no longer valid:

1. **Mark Deprecated**: Change status to "Deprecated" (do not delete entry)
2. **Document Reason**: Add note explaining why deprecated
3. **Provide Successor**: If applicable, link to replacement identifier
4. **Notify Consumers**: Inform all users of the deprecated identifier
5. **Historical Record**: Maintain entry indefinitely for traceability

### 6.3 Governance

**Owner**: Configuration Management WG  
**Approvers**: Design Engineering Lead, Systems Engineering Lead  
**Change Control**: Changes require ECR/ECO process  
**Review Cycle**: Quarterly review of registry

## 7. Catalog Maintenance

**Maintained By:** Configuration Management WG  
**Last Updated:** 2025-12-15  
**Update Frequency:** As identifiers are allocated or changed  
**Review Cycle:** Quarterly, or upon major CAD baseline updates

### 7.1 Change History

| Date | Change | Changed By | Version |
| :--- | :--- | :--- | :--- |
| 2025-12-15 | Initial registry with 8 baseline identifiers | System | v01 |

## 8. Usage Guidelines

### 8.1 Using Identifiers in Documentation

- **Always use full identifier**: `DATUM-GLOBAL-001`, not "global datum" or "D1"
- **Reference this catalog**: Include document ID when citing identifiers
- **Check current status**: Verify identifier is Active before using
- **Include description**: First use should include brief description

### 8.2 Using Identifiers in CAD

- **Annotate features**: Label datums, zones, envelopes with identifiers in CAD
- **Naming convention**: CAD feature names should include identifier
- **Metadata**: Include identifier in CAD metadata/properties
- **Export data**: Identifiers must appear in all CAD exports (CSV/JSON)

### 8.3 Using Identifiers in Analysis

- **Model setup**: Reference identifiers when defining coordinate frames
- **Results reporting**: Report results relative to identified datums/zones
- **Traceability**: Link analysis models to specific identifiers

## 9. References

### 9.1 Related Documents

| Doc ID | Title |
| :--- | :--- |
| 06_00_IDX_LC01_SPACET_k06-ata-06-tasklist_v01.md | ATA-06 SSOT Task List |
| 06_00_PLAN_LC01_SPACET_ssot-implementation-plan_v01.md | SSOT Implementation Plan |
| 06_90_SCH_SB00_GEN_dimensional-data-schema_v01.json | Dimensional Data Schema (T3) |
| 06_90_TAB_SB00_GEN_dimensional-exports_v01.csv | Dimensional Data Exports (T4) |

### 9.2 Standards

- ATA-SpaceT Numbering System
- Nomenclature Standard v2.0
- CAD Modeling Standards

---

**Document ID**: 06_00_CAT_LC01_SPACET_identifier-registry_v01.md  
**Status**: Draft  
**Version**: v01  
**Date**: 2025-12-15
