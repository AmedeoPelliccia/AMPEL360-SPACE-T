---
title: "ATA-06 Dimensional Data Schema Documentation"
type: SCH
variant: "GEN"
schema_type: "JSON Schema Draft-07"
version: "v01"
status: Draft
ata_chapter: "06"
owner: "Systems Engineering"
related_docs: ["06_00_IDX_LC01_SPACET_k06-ata-06-tasklist_I01-R01.md", "06_90_SCH_SB00_GEN_dimensional-data-schema_I01-R01.json"]
---

# ATA-06 Dimensional Data Schema Documentation

## 1. Schema Overview

### 1.1 Purpose

This schema defines and validates the structure of ATA-06 dimensional data exports from the CAD SSOT. It addresses Task T3 from the ATA-06 tasklist: "Define schema: units, coordinate frame, tolerances, metadata."

**What this schema validates:**
- Metadata about the export (timestamp, CAD source, baseline ID, approval status)
- Coordinate frame definition (origin, axes, handedness, units)
- Dimensional data (datums, zones, envelopes) with required fields
- Identifier format compliance
- Unit consistency
- Tolerance specifications

### 1.2 Schema Type

- **Format**: JSON Schema
- **Version**: Draft-07 (http://json-schema.org/draft-07/schema#)
- **Compliance**: JSON Schema specification
- **Schema File**: `06_90_SCH_SB00_GEN_dimensional-data-schema_I01-R01.json`

### 1.3 Scope

**IN SCOPE:**
- JSON exports from CAD containing dimensional data
- Datums (reference points, lines, planes, coordinate systems)
- Zones (spatial regions for integration and analysis)
- Envelopes (maximum dimensional boundaries and keep-out zones)
- Metadata, coordinate frames, tolerances

**OUT OF SCOPE:**
- CAD model files themselves (CAD is the SSOT, this validates exports)
- CSV format (separate but similar structure)
- Non-dimensional data (mass properties, materials)

## 2. Schema Structure

### 2.1 Top-Level Structure

The JSON export must contain three top-level objects:

```json
{
  "metadata": { /* Export metadata */ },
  "coordinate_frame": { /* Coordinate system definition */ },
  "data": { /* Dimensional data arrays */ }
}
```

All three are **required**.

### 2.2 Data Structure Documentation

#### 2.2.1 Metadata Object

Contains information about the export itself.

| Field | Type | Required | Description | Constraints |
| :--- | :--- | :--- | :--- | :--- |
| `export_timestamp` | string | **Yes** | ISO 8601 timestamp when export was generated | Format: date-time |
| `cad_source` | object | **Yes** | CAD source information | See CAD Source Object |
| `baseline_id` | string | **Yes** | CM baseline identifier | Pattern: `^BL-[0-9]{4}$` (e.g., BL-0001) |
| `schema_version` | string | **Yes** | Version of this schema | Pattern: `^[0-9]+\.[0-9]+$` (e.g., 1.0) |
| `approval_status` | string | No | CM approval status | Enum: draft, candidate, approved, superseded |
| `approved_by` | string | No | Name of approver (if approved) | - |
| `approval_date` | string | No | Date of approval (if approved) | Format: date (YYYY-MM-DD) |
| `notes` | string | No | Additional notes | - |

#### CAD Source Object (nested in metadata)

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `tool` | string | **Yes** | CAD tool name (e.g., "CATIA V6") |
| `version` | string | **Yes** | CAD tool version (e.g., "R2021x") |
| `model_file` | string | **Yes** | CAD model file name |
| `export_script` | string | No | Script used to generate export |

#### 2.2.2 Coordinate Frame Object

Defines the coordinate reference frame for all dimensional data.

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `name` | string | **Yes** | Coordinate frame name |
| `origin` | object | **Yes** | Origin definition (see below) |
| `axes` | object | **Yes** | Axes definition (x, y, z) |
| `handedness` | string | **Yes** | Enum: right-handed, left-handed |
| `units` | object | **Yes** | Units definition (length, angle) |
| `convention` | string | No | Reference standard (e.g., ISO 1151) |

**Origin Object:**
- `identifier` (string, required): Datum ID for origin (e.g., DATUM-GLOBAL-001)
- `description` (string, required): Human-readable description
- `physical_reference` (string, optional): Physical reference point

**Axes Object:**
- `x`, `y`, `z` (each required): Objects with `direction` and `description` fields

**Units Object:**
- `length` (string, required): Enum: mm, m, in, ft (SI preferred)
- `angle` (string, required): Enum: deg, rad

#### 2.2.3 Data Object

Contains arrays of dimensional data.

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `datums` | array | **Yes** | Array of datum objects |
| `zones` | array | **Yes** | Array of zone objects |
| `envelopes` | array | **Yes** | Array of envelope objects |

Each array can be empty but must be present.

#### 2.2.4 Datum Object (in data.datums array)

| Field | Type | Required | Description | Constraints |
| :--- | :--- | :--- | :--- | :--- |
| `identifier` | string | **Yes** | Unique datum identifier | Pattern: `^DATUM-[A-Z0-9]+-[0-9]{3}(-[A-Z0-9]+)?$` |
| `name` | string | **Yes** | Human-readable name | - |
| `category` | string | **Yes** | Always "DATUM" | Const: DATUM |
| `system` | string | **Yes** | System code (e.g., FUS, PROP) | Pattern: `^[A-Z]{2,6}$` |
| `type` | string | **Yes** | Datum type | Enum: point, line, plane, coordinate_system |
| `status` | string | **Yes** | Datum status | Enum: active, deprecated, superseded |
| `description` | string | No | Detailed description | - |
| `geometry` | object | No | Geometric definition | See Geometry Objects |
| `tolerance` | object | No | Tolerance specification | positional, angular fields |
| `cad_reference` | string | No | CAD feature reference | - |
| `related_identifiers` | array[string] | No | Related IDs | - |
| `superseded_by` | string | No | Replacement ID (if superseded) | - |

#### 2.2.5 Zone Object (in data.zones array)

| Field | Type | Required | Description | Constraints |
| :--- | :--- | :--- | :--- | :--- |
| `identifier` | string | **Yes** | Unique zone identifier | Pattern: `^ZONE-[A-Z0-9]+-[0-9]{3}(-[A-Z0-9]+)?$` |
| `name` | string | **Yes** | Human-readable name | - |
| `category` | string | **Yes** | Always "ZONE" | Const: ZONE |
| `system` | string | **Yes** | System code | Pattern: `^[A-Z]{2,6}$` |
| `type` | string | **Yes** | Zone type | Enum: cuboid, cylinder, sphere, annular, complex |
| `status` | string | **Yes** | Zone status | Enum: active, deprecated, superseded |
| `description` | string | No | Detailed description | - |
| `bounds` | object | **Yes** | Boundary definition | See Bounds Objects |
| `purpose` | string | No | Purpose of zone | - |
| `clearance` | object | No | Clearance requirements | minimum, preferred fields (numbers) |
| `volume` | number | No | Zone volume (cubic length units) | - |
| `cad_reference` | string | No | CAD feature reference | - |
| `related_identifiers` | array[string] | No | Related IDs | - |

#### 2.2.6 Envelope Object (in data.envelopes array)

| Field | Type | Required | Description | Constraints |
| :--- | :--- | :--- | :--- | :--- |
| `identifier` | string | **Yes** | Unique envelope identifier | Pattern: `^ENVELOPE-[A-Z0-9]+-[0-9]{3}(-[A-Z0-9]+)?$` |
| `name` | string | **Yes** | Human-readable name | - |
| `category` | string | **Yes** | Always "ENVELOPE" | Const: ENVELOPE |
| `system` | string | **Yes** | System code | Pattern: `^[A-Z]{2,6}$` |
| `type` | string | **Yes** | Envelope type | Enum: cuboid, cylinder, sphere, cone, complex, keep_out |
| `status` | string | **Yes** | Envelope status | Enum: active, deprecated, superseded |
| `description` | string | No | Detailed description | - |
| `bounds` | object | **Yes** | Boundary definition | See Bounds Objects |
| `purpose` | string | No | Purpose of envelope | - |
| `mass_limit` | number | No | Maximum mass (kg) | - |
| `cg_limits` | object | No | Center of gravity limits | x, y, z objects with min/max |
| `cad_reference` | string | No | CAD feature reference | - |
| `related_identifiers` | array[string] | No | Related IDs | - |

### 2.3 Geometry and Bounds Objects

#### Point Geometry
```json
{
  "type": "point",
  "coordinates": [x, y, z]
}
```

#### Line Geometry
```json
{
  "type": "line",
  "point": [x, y, z],
  "direction": [dx, dy, dz]
}
```

#### Plane Geometry
```json
{
  "type": "plane",
  "point": [x, y, z],
  "normal": [nx, ny, nz]
}
```

#### Cuboid Bounds
```json
{
  "type": "cuboid",
  "x_min": number,
  "x_max": number,
  "y_min": number,
  "y_max": number,
  "z_min": number,
  "z_max": number
}
```

#### Cylindrical Bounds
```json
{
  "type": "cylinder",
  "axis": "x" | "y" | "z",
  "center": [x, y, z],
  "radius": number,
  "length": number
}
```

#### Spherical Bounds
```json
{
  "type": "sphere",
  "center": [x, y, z],
  "radius": number
}
```

#### Complex Bounds (CAD-defined)
```json
{
  "type": "complex",
  "cad_reference": "CAD feature reference",
  "description": "Description",
  "approximate_volume": number
}
```

## 3. Validation Rules

### 3.1 Identifier Format Validation

All identifiers must follow the ATA-06 identifier grammar:

- **DATUM**: `^DATUM-[A-Z0-9]+-[0-9]{3}(-[A-Z0-9]+)?$`
  - Examples: `DATUM-GLOBAL-001`, `DATUM-FUS-042-A`
- **ZONE**: `^ZONE-[A-Z0-9]+-[0-9]{3}(-[A-Z0-9]+)?$`
  - Examples: `ZONE-PROP-001`, `ZONE-STRUCT-015-X`
- **ENVELOPE**: `^ENVELOPE-[A-Z0-9]+-[0-9]{3}(-[A-Z0-9]+)?$`
  - Examples: `ENVELOPE-GLOBAL-001`, `ENVELOPE-THERM-008`

### 3.2 Unit Consistency

- All linear dimensions must use the same unit (specified in coordinate_frame.units.length)
- All angular dimensions must use the same unit (specified in coordinate_frame.units.angle)
- **Preferred**: mm for length, deg for angles (SI compatible)

### 3.3 Required Field Validation

The schema enforces required fields at compile-time. Missing required fields will cause validation failure.

### 3.4 Status Validation

- Status must be one of: `active`, `deprecated`, `superseded`
- Only `active` items should be used in new designs
- `deprecated` items remain for historical reference
- `superseded` items must have `superseded_by` field pointing to replacement

### 3.5 Baseline ID Validation

- Baseline ID must match pattern: `BL-NNNN` where N is a digit
- Examples: `BL-0001`, `BL-0042`, `BL-1234`

## 4. Example Instances

### 4.1 Minimal Valid Example

```json
{
  "metadata": {
    "export_timestamp": "2025-12-15T10:30:00Z",
    "cad_source": {
      "tool": "CATIA V6",
      "version": "R2021x",
      "model_file": "SpaceT_Main_v1.0.CATPart"
    },
    "baseline_id": "BL-0001",
    "schema_version": "1.0"
  },
  "coordinate_frame": {
    "name": "Spacecraft Body Frame",
    "origin": {
      "identifier": "DATUM-GLOBAL-001",
      "description": "Launch vehicle interface center"
    },
    "axes": {
      "x": {
        "direction": "Forward",
        "description": "Longitudinal axis, positive forward"
      },
      "y": {
        "direction": "Right",
        "description": "Lateral axis, positive starboard"
      },
      "z": {
        "direction": "Down",
        "description": "Vertical axis, positive nadir"
      }
    },
    "handedness": "right-handed",
    "units": {
      "length": "mm",
      "angle": "deg"
    }
  },
  "data": {
    "datums": [
      {
        "identifier": "DATUM-GLOBAL-001",
        "name": "Primary Datum Origin",
        "category": "DATUM",
        "system": "GLOBAL",
        "type": "point",
        "status": "active",
        "geometry": {
          "type": "point",
          "coordinates": [0, 0, 0]
        }
      }
    ],
    "zones": [],
    "envelopes": []
  }
}
```

### 4.2 Complete Example with All Features

See the JSON schema file for comprehensive examples.

### 4.3 Invalid Example (with errors)

```json
{
  "metadata": {
    "export_timestamp": "not-a-valid-timestamp",  // Invalid: not ISO 8601
    "cad_source": {
      "tool": "CATIA V6",
      // Missing required fields: version, model_file
      "placeholder": "to make valid JSON"
    },
    "baseline_id": "BASELINE-1",  // Invalid: doesn't match pattern BL-NNNN
    "schema_version": "1.0"
  },
  "coordinate_frame": {
    // Missing required field: origin
    "name": "Test Frame",
    "handedness": "left",  // Invalid: should be "left-handed"
    "units": {
      "length": "meters"  // Invalid: should be "m", not "meters"
    }
  }
  // Missing required field: data
}
```

## 5. Schema Versioning

### 5.1 Version History

| Version | Date | Changes | Author |
| :--- | :--- | :--- | :--- |
| v01 (1.0) | 2025-12-15 | Initial schema for ATA-06 dimensional data | Systems Engineering |

### 5.2 Backward Compatibility

This is version 1.0, the initial release. No backward compatibility concerns.

**Future versioning:**
- **Minor version** (1.x): Adding optional fields - backward compatible
- **Major version** (2.0): Changing required fields, removing fields - breaking change
- All versions will be maintained and documented

### 5.3 Schema Evolution Process

1. Propose schema change via ECR (Engineering Change Request)
2. Review by Systems Engineering and CM WG
3. Update schema file and documentation
4. Update version number per semantic versioning
5. Notify all consumers of change
6. Maintain old version for transition period (if breaking change)

## 6. Implementation Notes

### 6.1 Validation Libraries

#### Python

```python
import json
import jsonschema

# Load schema
with open('06_90_SCH_SB00_GEN_dimensional-data-schema_I01-R01.json') as f:
    schema = json.load(f)

# Load data to validate
with open('dimensional_export.json') as f:
    data = json.load(f)

# Validate
try:
    jsonschema.validate(instance=data, schema=schema)
    print("✅ Validation passed")
except jsonschema.ValidationError as e:
    print(f"❌ Validation failed: {e.message}")
    print(f"   Path: {'.'.join(str(p) for p in e.absolute_path)}")
```

#### JavaScript/Node.js

```javascript
const Ajv = require('ajv');
const addFormats = require('ajv-formats');
const fs = require('fs');

// Load schema
const schema = JSON.parse(fs.readFileSync(
  '06_90_SCH_SB00_GEN_dimensional-data-schema_I01-R01.json', 'utf8'
));

// Load data
const data = JSON.parse(fs.readFileSync(
  'dimensional_export.json', 'utf8'
));

// Validate
const ajv = new Ajv({allErrors: true});
addFormats(ajv);
const validate = ajv.compile(schema);
const valid = validate(data);

if (valid) {
  console.log('✅ Validation passed');
} else {
  console.log('❌ Validation failed:');
  validate.errors.forEach(err => {
    console.log(`  ${err.instancePath}: ${err.message}`);
  });
}
```

### 6.2 Integration Points

This schema is used in:

1. **CAD Export Script**: Validates generated JSON before saving
2. **CI Pipeline**: Validates all committed dimensional data files
3. **Analysis Tools**: Validates input data before processing
4. **Documentation Tools**: Validates data for report generation
5. **Integration Tools**: Validates data before system integration

### 6.3 CI Validation Script

A validation script is provided at `scripts/validate_ata06_dimensions.py` that:
- Validates JSON against this schema
- Checks unit consistency
- Verifies identifier uniqueness
- Reports validation errors with context

## 7. Testing

### 7.1 Test Cases

| Test ID | Description | Input | Expected Result |
| :--- | :--- | :--- | :--- |
| **TEST-001** | Valid minimal export | Minimal valid JSON | Pass |
| **TEST-002** | Valid complete export | Complete JSON with all fields | Pass |
| **TEST-003** | Missing required field (metadata) | JSON without metadata | Fail: "metadata is required" |
| **TEST-004** | Invalid identifier format | `identifier: "DATUM-001"` (missing system) | Fail: pattern mismatch |
| **TEST-005** | Invalid baseline ID | `baseline_id: "BL-1"` (not 4 digits) | Fail: pattern mismatch |
| **TEST-006** | Invalid unit | `length: "meters"` | Fail: not in enum |
| **TEST-007** | Invalid timestamp | `export_timestamp: "12/15/2025"` | Fail: not ISO 8601 |
| **TEST-008** | Deprecated datum | `status: "deprecated"` | Pass (valid status) |
| **TEST-009** | Extra unexpected field | `extra_field: "value"` | Pass (additionalProperties allowed in most objects) |
| **TEST-010** | Invalid handedness | `handedness: "right"` | Fail: must be "right-handed" |

### 7.2 Test Data

Test JSON files should be created covering:
- Minimal valid case
- Complete valid case with all optional fields
- Each invalid case from test table
- Edge cases (empty arrays, maximum lengths, etc.)

## 8. References

### 8.1 Related Documents

| Doc ID | Title |
| :--- | :--- |
| 06_00_IDX_LC01_SPACET_k06-ata-06-tasklist_I01-R01.md | ATA-06 SSOT Task List |
| 06_00_PLAN_LC01_SPACET_ssot-implementation-plan_I01-R01.md | SSOT Implementation Plan (T1) |
| 06_00_CAT_LC01_SPACET_identifier-registry_I01-R01.md | Identifier Registry (T2) |
| 06_90_SCH_SB00_GEN_dimensional-data-schema_I01-R01.json | JSON Schema File (this schema) |

### 8.2 Standards

- **JSON Schema**: http://json-schema.org/draft-07/schema
- **ISO 8601**: Date and time format standard
- **ISO 1151**: Coordinate system conventions for aerospace
- **ATA-SpaceT**: Numbering system for space transport
- **Nomenclature Standard v2.0**: File naming convention

### 8.3 Tools

- **JSON Schema Validators**: 
  - Python: `jsonschema` library
  - JavaScript: `ajv` library
  - Online: https://www.jsonschemavalidator.net/
- **JSON Schema Generators**: 
  - https://json-schema.org/implementations.html

---

**Document ID**: 06_90_SCH_SB00_GEN_dimensional-data-schema_I01-R01.md  
**Schema File**: 06_90_SCH_SB00_GEN_dimensional-data-schema_I01-R01.json  
**Status**: Draft  
**Version**: v01  
**Date**: 2025-12-15
