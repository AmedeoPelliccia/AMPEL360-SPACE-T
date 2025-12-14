---
title: "Schema: {{DESCRIPTION}}"
type: SCH
variant: "{{VARIANT}}"
schema_type: "JSON Schema"
version: "{{VERSION}}"
status: Draft
---

# Schema: {{TITLE}}

## 1. Schema Overview

### 1.1 Purpose
Description of what this schema defines and validates.

### 1.2 Schema Type
- Format: [JSON Schema / XML Schema / Database Schema]
- Version: [Draft-07 / v1.0 / etc.]
- Compliance: [Standard]

### 1.3 Scope
Define what data structures this schema covers.

## 2. Schema Definition

### 2.1 JSON Schema Example

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "https://ampel360.space/schemas/{{DESCRIPTION}}.json",
  "title": "{{TITLE}}",
  "description": "Schema for {{DESCRIPTION}}",
  "type": "object",
  "properties": {
    "id": {
      "type": "string",
      "description": "Unique identifier",
      "pattern": "^[A-Z]{3}-[0-9]{3}$"
    },
    "name": {
      "type": "string",
      "description": "Name of the item",
      "minLength": 1,
      "maxLength": 100
    },
    "status": {
      "type": "string",
      "enum": ["active", "inactive", "archived"],
      "description": "Current status"
    },
    "created": {
      "type": "string",
      "format": "date-time",
      "description": "Creation timestamp"
    },
    "metadata": {
      "type": "object",
      "description": "Additional metadata",
      "properties": {
        "owner": {"type": "string"},
        "tags": {
          "type": "array",
          "items": {"type": "string"}
        }
      }
    }
  },
  "required": ["id", "name", "status"],
  "additionalProperties": false
}
```

### 2.2 Data Structure Documentation

#### Root Object

| Field | Type | Required | Description | Constraints |
| :--- | :--- | :--- | :--- | :--- |
| `id` | string | Yes | Unique identifier | Pattern: `^[A-Z]{3}-[0-9]{3}$` |
| `name` | string | Yes | Item name | Length: 1-100 chars |
| `status` | string | Yes | Current status | Enum: active, inactive, archived |
| `created` | string | No | Creation timestamp | Format: ISO 8601 date-time |
| `metadata` | object | No | Additional metadata | See Metadata Object |

#### Metadata Object

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `owner` | string | No | Owner name |
| `tags` | array[string] | No | List of tags |

## 3. Validation Rules

### 3.1 Field Validations

**ID Field:**
- Must match pattern: `[A-Z]{3}-[0-9]{3}`
- Must be unique within dataset
- Example: `ABC-001`

**Name Field:**
- Minimum length: 1 character
- Maximum length: 100 characters
- No special characters except hyphen and underscore

**Status Field:**
- Must be one of: `active`, `inactive`, `archived`
- Default: `active`

### 3.2 Business Rules

1. Once status is `archived`, it cannot be changed back
2. Owner must be specified for `active` items
3. Creation timestamp must not be in the future

## 4. Example Instances

### 4.1 Valid Example

```json
{
  "id": "ABC-001",
  "name": "Example Item",
  "status": "active",
  "created": "2025-12-14T15:00:00Z",
  "metadata": {
    "owner": "Engineering Team",
    "tags": ["critical", "review-pending"]
  }
}
```

### 4.2 Invalid Example (with errors)

```json
{
  "id": "123",  // Invalid: doesn't match pattern
  "name": "",   // Invalid: empty string
  "status": "pending",  // Invalid: not in enum
  "extra": "field"  // Invalid: additional property not allowed
}
```

## 5. Schema Versioning

### 5.1 Version History

| Version | Date | Changes | Author |
| :--- | :--- | :--- | :--- |
| {{VERSION}} | {{DATE}} | Initial schema | {{OWNER}} |

### 5.2 Backward Compatibility

Description of compatibility with previous versions.

## 6. Implementation Notes

### 6.1 Validation Libraries

**Python:**
```python
import jsonschema

schema = {...}
data = {...}
jsonschema.validate(instance=data, schema=schema)
```

**JavaScript:**
```javascript
const Ajv = require('ajv');
const ajv = new Ajv();
const validate = ajv.compile(schema);
const valid = validate(data);
```

### 6.2 Integration Points

Where and how this schema is used in the system.

## 7. Testing

### 7.1 Test Cases

| Test ID | Description | Input | Expected Result |
| :--- | :--- | :--- | :--- |
| TEST-001 | Valid data | [Example] | Pass |
| TEST-002 | Invalid ID format | [Example] | Fail with error |

## 8. References

- JSON Schema specification: https://json-schema.org/
- Related schemas: [List]
- API documentation: [Reference]
