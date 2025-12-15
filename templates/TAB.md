---
title: "Table: {{DESCRIPTION}}"
type: TAB
project: "{{PROJECT}}"
program: "{{PROGRAM}}"
variant: "{{VARIANT}}"
table_type: "TBD"
status: Draft
---

# Table: {{TITLE}}

## 1. Table Information

| Field | Details |
| :--- | :--- |
| **Table Name:** | {{TITLE}} |
| **Type:** | [Data Table/Lookup Table/Mapping Table/etc.] |
| **Purpose:** | {{DESCRIPTION}} |
| **Owner:** | {{OWNER}} |
| **Last Updated:** | {{DATE}} |
| **Status:** | {{STATUS}} |

## 2. Table Description

### 2.1 Purpose
Description of what this table contains and its intended use.

### 2.2 Scope
Define the domain and boundaries of data in this table.

### 2.3 Update Frequency
[Real-time / Daily / Weekly / Monthly / On Change]

## 3. Table Structure

### 3.1 Column Definitions

| Column Name | Data Type | Unit | Range/Values | Required | Description |
| :--- | :--- | :--- | :--- | :--- | :--- |
| ID | Integer | - | 1-999 | Yes | Unique identifier |
| Name | String | - | 1-100 chars | Yes | Item name |
| Value | Float | [Unit] | 0.0-100.0 | Yes | Measured value |
| Status | Enum | - | Active/Inactive | Yes | Current status |
| Date | DateTime | - | ISO 8601 | No | Last update date |

### 3.2 Primary Key
- **Column(s):** ID
- **Type:** Auto-increment / Manual
- **Uniqueness:** Enforced

### 3.3 Constraints and Validations

**Constraints:**
- ID must be unique
- Name must not be empty
- Value must be within specified range
- Status must be one of allowed values

**Relationships:**
- Foreign key to [Table Name]: [Column]
- Referenced by [Table Name]: [Column]

## 4. Table Data

### 4.1 Main Table

| ID | Name | Value | Status | Date | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Item A | 25.5 | Active | 2025-12-14 | [Note] |
| 2 | Item B | 42.3 | Active | 2025-12-14 | [Note] |
| 3 | Item C | 18.7 | Inactive | 2025-12-13 | [Note] |
| 4 | Item D | 91.2 | Active | 2025-12-14 | [Note] |

### 4.2 Additional Rows

*Continue adding rows as needed...*

| ID | Name | Value | Status | Date | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 5 | Item E | 33.8 | Active | 2025-12-14 | [Note] |

## 5. Table Statistics

| Metric | Value |
| :--- | :--- |
| Total Rows | 5 |
| Active Rows | 4 |
| Inactive Rows | 1 |
| Last Updated | {{DATE}} |
| Average Value | 42.3 |
| Min Value | 18.7 |
| Max Value | 91.2 |

## 6. Usage Examples

### 6.1 Query Examples

**SQL:**
```sql
SELECT * FROM table_name WHERE Status = 'Active';
SELECT AVG(Value) FROM table_name WHERE Status = 'Active';
SELECT * FROM table_name WHERE Value > 50.0 ORDER BY Value DESC;
```

**Python/Pandas:**
```python
import pandas as pd
df = pd.read_csv('table_data.csv')
active_items = df[df['Status'] == 'Active']
avg_value = df['Value'].mean()
```

### 6.2 Common Operations

**Filter by Status:**
```
Active items: Rows 1, 2, 4, 5
Inactive items: Row 3
```

**Sort by Value (descending):**
```
Row 4 (91.2) > Row 2 (42.3) > Row 5 (33.8) > Row 1 (25.5) > Row 3 (18.7)
```

## 7. Data Dictionary

### 7.1 Value Codes

If the table uses coded values, define them here:

| Code | Meaning | Description |
| :--- | :--- | :--- |
| A | Active | Item is currently in use |
| I | Inactive | Item is not currently in use |
| D | Deprecated | Item will be removed |

### 7.2 Status Definitions

**Active:**
- Item is operational and in current use
- Should be included in calculations

**Inactive:**
- Item is not currently operational
- Excluded from standard calculations
- May be reactivated

## 8. Data Quality

### 8.1 Data Sources
- Source 1: [Description and authority]
- Source 2: [Description and authority]

### 8.2 Data Validation
- Automated validation: [Description]
- Manual review: [Process]
- Last validation: {{DATE}}

### 8.3 Known Issues

| Issue ID | Description | Impact | Resolution Plan | Status |
| :--- | :--- | :--- | :--- | :--- |
| ISS-001 | [Issue] | [Impact] | [Plan] | Open |

## 9. Related Tables

- **Parent Table:** [Name] - [Relationship]
- **Child Tables:** [Name] - [Relationship]
- **Reference Tables:** [Name] - [Purpose]

## 10. Change History

| Version | Date | Changes | Changed By | Rows Affected |
| :--- | :--- | :--- | :--- | :--- |
| {{VERSION}} | {{DATE}} | Initial table | {{OWNER}} | All |
| [Version] | [Date] | [Changes] | [Name] | [Count] |

## 11. Export Formats

This table is available in multiple formats:

- **Markdown:** This document
- **CSV:** `data/{{DESCRIPTION}}.csv`
- **Excel:** `data/{{DESCRIPTION}}.xlsx`
- **JSON:** `data/{{DESCRIPTION}}.json`
- **SQL:** `data/{{DESCRIPTION}}.sql`

## 12. Maintenance

**Update Process:** [Description of how to update this table]  
**Review Cycle:** [Frequency]  
**Data Owner:** {{OWNER}}  
**Technical Contact:** [Name/Email]

## 13. References

- Data specification document: [DOC-ID]
- Related requirements: [REQ-ID]
- Source systems: [List]
