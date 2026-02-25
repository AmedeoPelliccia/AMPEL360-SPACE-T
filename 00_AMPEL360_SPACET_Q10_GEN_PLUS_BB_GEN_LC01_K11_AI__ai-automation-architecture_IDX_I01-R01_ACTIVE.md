---
title: "Index: AI Automation Architecture and Integration Points"
type: IDX
project: "AMPEL360"
program: "SPACET"
variant: "PLUS"
indexed_content: "AI/ML automation tooling, CI/CD integration points, validation scripts, governance workflows"
status: Draft
owner: "STK_AI — AI/ML Engineering (contributor); STK_CM (authority)"
knot_id: K06
ata: "00"
lc_or_subbucket: "LC01"
bucket: "00"
description: "Documents the AI automation architecture, integration points, validation tooling, and CI/CD infrastructure supporting K06 governance enforcement."
---

# Index: AI Automation Architecture and Integration Points

## 1. Overview

This index documents the **AI automation architecture** and **integration points** for the AMPEL360 Space-T project. It provides a comprehensive reference to:

1. **Validation tooling** (nomenclature, schema, trace, evidence validators)
2. **CI/CD integration points** (GitHub Actions workflows, pre-commit hooks)
3. **Governance enforcement mechanisms** (blocking gates, labeling, alerts)
4. **Evidence automation** (pack generation, link validation, staleness detection)
5. **Agent integration** (GitHub Copilot instructions, scaffolding tools)

This document fulfills **Task T10-AI** from the K06 ATA 00 Tasklist and serves as the authoritative index for all AI-developed automation supporting governance enforcement.

## 2. Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                        AI AUTOMATION ARCHITECTURE                               │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│  ┌─────────────────┐    ┌──────────────────┐    ┌─────────────────────┐        │
│  │  DEVELOPMENT    │───▶│  LOCAL GATES     │───▶│  CI/CD PIPELINES    │        │
│  │  WORKFLOW       │    │  (Pre-commit)    │    │  (GitHub Actions)   │        │
│  └─────────────────┘    └──────────────────┘    └─────────────────────┘        │
│          │                      │                        │                      │
│          │                      ▼                        ▼                      │
│          │         ┌──────────────────────────────────────────────┐             │
│          │         │           VALIDATION LAYER                   │             │
│          │         ├──────────────────────────────────────────────┤             │
│          │         │  ┌───────────────┐  ┌───────────────────┐    │             │
│          │         │  │ Nomenclature  │  │ Schema Registry   │    │             │
│          │         │  │ Validator     │  │ Validator         │    │             │
│          │         │  │ (GATE-001)    │  │ (GATE-002)        │    │             │
│          │         │  └───────────────┘  └───────────────────┘    │             │
│          │         │  ┌───────────────┐  ┌───────────────────┐    │             │
│          │         │  │ Trace Link    │  │ Namespace Dedup   │    │             │
│          │         │  │ Validator     │  │ Checker           │    │             │
│          │         │  │ (GATE-003)    │  │ (GATE-004)        │    │             │
│          │         │  └───────────────┘  └───────────────────┘    │             │
│          │         │  ┌───────────────┐  ┌───────────────────┐    │             │
│          │         │  │ Identifier    │  │ Evidence Link     │    │             │
│          │         │  │ Grammar       │  │ Validator         │    │             │
│          │         │  │ (GATE-005)    │  │ (GATE-008)        │    │             │
│          │         │  └───────────────┘  └───────────────────┘    │             │
│          │         └──────────────────────────────────────────────┘             │
│          │                      │                                               │
│          │                      ▼                                               │
│          │         ┌──────────────────────────────────────────────┐             │
│          │         │           ENFORCEMENT LAYER                  │             │
│          │         ├──────────────────────────────────────────────┤             │
│          │         │  • BLOCKING: Prevents merge on failure       │             │
│          │         │  • LABELING: Auto-labels PRs for review      │             │
│          │         │  • WARNING: Non-blocking alerts              │             │
│          │         │  • MANUAL: CM WG approval required           │             │
│          │         └──────────────────────────────────────────────┘             │
│          │                      │                                               │
│          ▼                      ▼                                               │
│  ┌─────────────────────────────────────────────────────────────────────┐        │
│  │                    GOVERNANCE ARTIFACTS                             │        │
│  ├─────────────────────────────────────────────────────────────────────┤        │
│  │  ┌────────────────────┐  ┌────────────────┐  ┌───────────────────┐  │        │
│  │  │ CM Standards       │  │ ATA 91 Schema  │  │ ATA 93 Trace      │  │        │
│  │  │ (STD files)        │  │ Registry       │  │ Registry          │  │        │
│  │  └────────────────────┘  └────────────────┘  └───────────────────┘  │        │
│  │  ┌────────────────────┐  ┌────────────────┐  ┌───────────────────┐  │        │
│  │  │ ATA 99 Namespace   │  │ Evidence Packs │  │ Baselines         │  │        │
│  │  │ Registry           │  │ (EVD indexes)  │  │ (BL tags)         │  │        │
│  │  └────────────────────┘  └────────────────┘  └───────────────────┘  │        │
│  └─────────────────────────────────────────────────────────────────────┘        │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

## 3. Automation Components Index

### 3.1 Validation Scripts

| Script ID | Script Name | Location | Purpose | Gate | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **VAL-001** | Nomenclature Validator | `validate_nomenclature.py` | Validates filenames against v3.0 standard | GATE-001 | **Active** |
| **VAL-002** | Schema Registry Validator | `scripts/validate_schema_registry.py` | Verifies schema refs exist in ATA 91 | GATE-002 | **Active** |
| **VAL-003** | ATA 06 Dimensions Validator | `scripts/validate_ata06_dimensions.py` | Validates dimensional data | Custom | **Active** |
| **VAL-004** | Trace Link Integrity Checker | `scripts/check_trace_integrity.py` | Validates trace link targets exist | GATE-003 | Planned |
| **VAL-005** | Namespace Deduplication Checker | `scripts/check_ata99_registry.py` | Prevents duplicate IDs across namespaces | GATE-004 | Planned |
| **VAL-006** | Identifier Grammar Validator | `scripts/validate_identifiers.py` | Validates canonical ID format | GATE-005 | Planned |
| **VAL-007** | Evidence Link Validator | `scripts/validate_evidence_links.py` | Checks evidence pack integrity | GATE-008 | Planned |
| **VAL-008** | Staleness Detector | `scripts/check_staleness.py` | Detects stale derived artifacts | GATE-016 | Planned |
| **VAL-009** | Shadow Registry Detector | `scripts/detect_shadow_registries.py` | Finds uncoordinated ID lists | GATE-017 | Planned |
| **VAL-010** | Type Code Detector | `scripts/detect_new_types.py` | Detects unapproved TYPE codes | GATE-009 | **Active** |

### 3.2 Scaffolding and Generation Tools

| Tool ID | Tool Name | Location | Purpose | Status |
| :--- | :--- | :--- | :--- | :--- |
| **GEN-001** | File Scaffold Generator | `scripts/scaffold.py` | Generates files from templates with nomenclature compliance | **Active** |
| **GEN-002** | Stakeholder/Knot Structure Generator | `scripts/generate_stakeholder_knot_structure.py` | Generates portal folder structure | **Active** |
| **GEN-003** | Evidence Pack Generator | `scripts/generate_evidence_pack.py` | Automated evidence pack creation | Planned |
| **GEN-004** | Trace Coverage Report Generator | `scripts/generate_trace_coverage.py` | Generates trace coverage metrics | Planned |

### 3.3 GitHub Actions Workflows

| Workflow ID | Workflow Name | File | Trigger | Gates Implemented (Active) | Gates Planned | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **WF-001** | Nomenclature Validation | `.github/workflows/nomenclature-validation.yml` | Push/PR to any branch | GATE-001 | — | **Active** |
| **WF-002** | Governance Gates (Comprehensive) | `.github/workflows/governance-gates.yml` | PR to main/develop, manual | GATE-001, GATE-002, GATE-006 | GATE-003, GATE-004, GATE-005, GATE-007, GATE-008 | **Active** (partial) |
| **WF-003** | Detect New TYPE Codes | `.github/workflows/detect-new-types.yml` | Push/PR, weekly, manual | GATE-009 | — | **Active** |
| **WF-004** | Baseline Readiness Check | `.github/workflows/baseline-readiness.yml` | Manual dispatch | — | GATE-014, GATE-018 | Planned |
| **WF-005** | Weekly Governance Audit | `.github/workflows/weekly-audit.yml` | Weekly schedule | — | GATE-015, GATE-016, GATE-017 | Planned |

> **Note**: WF-002 is marked as **Active (partial)** because the workflow file exists and executes, but some gates have placeholder implementations that check for script existence and skip if not found.

### 3.4 Agent Integration

| Agent ID | Agent Name | Configuration | Purpose | Status |
| :--- | :--- | :--- | :--- | :--- |
| **AGENT-001** | GitHub Copilot Instructions | `.github/copilot-instructions.md` | Guides AI suggestions for nomenclature compliance | **Active** |
| **AGENT-002** | Nomenclature Agent Instructions | `.github/NOMENCLATURE_AGENT_INSTRUCTIONS.md` | Comprehensive agent reference for nomenclature | **Active** |
| **AGENT-003** | Stakeholder/Knot Config | `scripts/stakeholder_knot_config.json` | Configuration for portal structure generation | **Active** |

## 4. Integration Points

### 4.1 CI/CD Pipeline Integration

```
┌─────────────────────────────────────────────────────────────────────────┐
│                     CI/CD INTEGRATION FLOW                              │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│   DEVELOPER                  GITHUB                      MERGE         │
│   ─────────                  ──────                      ─────         │
│                                                                         │
│   ┌─────────┐               ┌─────────────────────────────────┐        │
│   │  Code   │               │  WORKFLOW: nomenclature-        │        │
│   │  Change │──push────────▶│  validation.yml                 │        │
│   └─────────┘               │                                 │        │
│       │                     │  ┌───────────────────────────┐  │        │
│       │                     │  │ GATE-001: Nomenclature    │  │        │
│       │                     │  │ python validate_          │  │        │
│       │                     │  │ nomenclature.py --check-  │  │        │
│       │                     │  │ all --strict --verbose    │  │        │
│       │                     │  └───────────────────────────┘  │        │
│       │                     └─────────────────────────────────┘        │
│       │                                   │                             │
│       │                                   ▼                             │
│       │                     ┌─────────────────────────────────┐        │
│   ┌───▼─────┐               │  WORKFLOW: governance-gates.yml │        │
│   │  Pull   │──PR──────────▶│  (on PR to main/develop)       │        │
│   │ Request │               │                                 │        │
│   └─────────┘               │  ┌───────────────────────────┐  │        │
│       │                     │  │ GATE-001 (blocking)       │  │        │
│       │                     │  │ GATE-002 (blocking)       │  │        │
│       │                     │  │ GATE-005 (planned)        │  │        │
│       │                     │  │ GATE-006 (labeling)       │  │        │
│       │                     │  │ GATE-007 (planned)        │  │        │
│       │                     │  │ GATE-008 (warning)        │  │        │
│       │                     │  └───────────────────────────┘  │        │
│       │                     │                                 │        │
│       │                     │  If governance change detected: │        │
│       │                     │  → Add label: governance-review-│        │
│       │                     │    required                     │        │
│       │                     │  → Create comment with guidance │        │
│       │                     └─────────────────────────────────┘        │
│       │                                   │                             │
│       │                                   ▼                             │
│       │                     ┌─────────────────────────────────┐        │
│       │                     │  MANUAL REVIEW (if required)    │        │
│       │                     │  CM WG approves governance      │        │
│       │                     │  changes (GATE-010)             │        │
│       │                     └─────────────────────────────────┘        │
│       │                                   │                             │
│       │                                   ▼                             │
│   ┌───▼─────┐               ┌─────────────────────────────────┐        │
│   │  Merge  │◀───pass/approve──│  All gates pass OR approved   │        │
│   └─────────┘               └─────────────────────────────────┘        │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### 4.2 Local Development Integration

```
┌─────────────────────────────────────────────────────────────────────────┐
│                   LOCAL DEVELOPMENT FLOW                                │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│   ┌─────────────────────────────────────────────────────────────┐      │
│   │  1. CREATE FILE                                             │      │
│   │     ─────────────                                           │      │
│   │     Use scaffolding: python scripts/scaffold.py 00 70 FHA  │      │
│   │       SB70 AMPEL360 SPACET PLUS propulsion v01             │      │
│   │                                                             │      │
│   │     Or use Copilot with .github/copilot-instructions.md    │      │
│   └─────────────────────────────────────────────────────────────┘      │
│                           │                                             │
│                           ▼                                             │
│   ┌─────────────────────────────────────────────────────────────┐      │
│   │  2. VALIDATE LOCALLY                                        │      │
│   │     ─────────────────                                       │      │
│   │     python validate_nomenclature.py <filename>              │      │
│   │     python validate_nomenclature.py --check-all             │      │
│   └─────────────────────────────────────────────────────────────┘      │
│                           │                                             │
│                           ▼                                             │
│   ┌─────────────────────────────────────────────────────────────┐      │
│   │  3. PRE-COMMIT HOOK (optional)                              │      │
│   │     ─────────────────────────                               │      │
│   │     Install: cp scripts/pre-commit .git/hooks/pre-commit   │      │
│   │              chmod +x .git/hooks/pre-commit                 │      │
│   │                                                             │      │
│   │     On git commit:                                          │      │
│   │     → Validates staged files                                │      │
│   │     → Blocks commit if validation fails                     │      │
│   │     → Shows which files are non-compliant                   │      │
│   └─────────────────────────────────────────────────────────────┘      │
│                           │                                             │
│                           ▼                                             │
│   ┌─────────────────────────────────────────────────────────────┐      │
│   │  4. COMMIT AND PUSH                                         │      │
│   │     ───────────────                                         │      │
│   │     git add <file>                                          │      │
│   │     git commit -m "Add <description>"                       │      │
│   │     git push                                                │      │
│   │                                                             │      │
│   │     → CI validation runs automatically                      │      │
│   └─────────────────────────────────────────────────────────────┘      │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### 4.3 Governance Artifact Dependencies

| Automation Component | Consumes | Produces | Updates When |
| :--- | :--- | :--- | :--- |
| **Nomenclature Validator** | Nomenclature Standard v3.0 | Validation reports | Standard updated |
| **Schema Registry Validator** | ATA 91 schema registry, Schema governance policy | Validation reports, Missing registry issues | Schema changes |
| **Trace Link Validator** | ATA 93 trace registry, Evidence link schema | Validation reports | Trace changes |
| **Namespace Dedup Checker** | ATA 99 namespace registry | Conflict reports | Registry changes |
| **Governance Change Detector** | STD/SCH/TRC/NS files | PR labels, Comments | PR created |
| **Evidence Pack Generator** | Evidence schema, Linked artifacts | Evidence packs (EVD) | On-baseline |
| **TYPE Detector** | Approved TYPE vocabulary | Issues, Extension guides | New TYPEs detected |

## 5. Gate Implementation Status

### 5.1 Active Gates (Implemented)

| Gate ID | Gate Name | Enforcement | Implementation | Test Coverage |
| :--- | :--- | :--- | :--- | :--- |
| **GATE-001** | Nomenclature Validation | BLOCKING | `validate_nomenclature.py` + WF-001, WF-002 | ✅ Comprehensive |
| **GATE-002** | Schema Registration Check | BLOCKING | `scripts/validate_schema_registry.py` + WF-002 | ✅ Basic |
| **GATE-006** | Governance Change Detection | LABELING | WF-002 (inline bash) | ✅ Pattern matching |
| **GATE-009** | TYPE Code Detection | WARNING | `scripts/detect_new_types.py` + WF-003 | ✅ Comprehensive |

### 5.2 Planned Gates (Not Yet Implemented)

| Gate ID | Gate Name | Target | Dependencies | Priority |
| :--- | :--- | :--- | :--- | :--- |
| **GATE-003** | Trace Link Integrity | Q1 2026 | ATA 93 trace registry | High |
| **GATE-004** | Namespace Deduplication | Q1 2026 | ATA 99 namespace registry | High |
| **GATE-005** | Identifier Grammar Check | Q1 2026 | Identifier Grammar Standard | High |
| **GATE-007** | Breaking Schema Change Detection | Q2 2026 | ATA 91 schema versioning | Medium |
| **GATE-008** | Evidence Link Validation | Q2 2026 | Evidence pack index | Medium |
| **GATE-014** | Baseline Approval | Q3 2026 | Baseline Manager setup | Low |
| **GATE-015** | SSOT Ownership Audit | Q2 2026 | SSOT Decision Matrix | Medium |
| **GATE-016** | Staleness Detection | Q2 2026 | Derivation metadata | Medium |
| **GATE-017** | Shadow Registry Detection | Q2 2026 | ATA 99 namespace registry | Medium |
| **GATE-018** | Trace Coverage Report | Q3 2026 | ATA 93 trace registry | Low |

## 6. Script Technical Specifications

### 6.1 Nomenclature Validator (`validate_nomenclature.py`)

**Purpose**: Validates filenames against AMPEL360 Space-T nomenclature standard v3.0.

**Pattern Validated**:
```
[ROOT]_[BUCKET]_[TYPE]_[SUBJECT]_[PROJECT]_[PROGRAM]_[VARIANT]_[DESCRIPTION]_[VERSION].[EXT]
```

**Field Constraints**:
- **ROOT**: 2-3 digits (`\d{2,3}`)
- **BUCKET**: `00|10|20|30|40|50|60|70|80|90`
- **TYPE**: 2-8 uppercase alphanumeric (`[A-Z0-9]{2,8}`)
- **SUBJECT**: LC01-LC14 (for BUCKET=00) or SB15-SB99 (for BUCKET≠00)
- **PROJECT**: `AMPEL360` (hard constraint)
- **PROGRAM**: `SPACET` (allowlist)
- **VARIANT**: Uppercase with hyphens
- **DESCRIPTION**: lowercase-kebab-case
- **VERSION**: `v` + 2 digits (`v\d{2}`)
- **EXT**: lowercase alphanumeric

**Usage**:
```bash
# Validate single file
python validate_nomenclature.py 00_70_FHA_SB70_AMPEL360_SPACET_PLUS_propulsion_I01-R01.md

# Validate all files
python validate_nomenclature.py --check-all

# Validate directory
python validate_nomenclature.py --check-dir ./AMPEL360-SPACE-T-PORTAL

# Strict mode (default)
python validate_nomenclature.py --check-all --strict

# Verbose output
python validate_nomenclature.py --check-all --verbose
```

**Exit Codes**:
- `0`: All files valid
- `1`: One or more files invalid
- `2`: Script error

### 6.2 Schema Registry Validator (`scripts/validate_schema_registry.py`)

**Purpose**: Verifies schema references exist in ATA 91 schema registry.

**Expected Registry Locations**:
- `**/schema-registry*.csv`
- `**/91_*_TAB_*_schema-registry_*.csv`
- `**/schema_registry*.csv`

**Required CSV Fields**:
- `schema_id`: Unique identifier for the schema
- `version`: Schema version
- `namespace`: Schema namespace
- `owner`: Responsible owner/team
- `status`: Current status (active, deprecated, draft, superseded)
- `file_path`: Path to the schema file
- `description`: Brief description of the schema
- `content_hash`: SHA-256 hash of schema content (optional)

**Usage**:
```bash
python scripts/validate_schema_registry.py --check-all --verbose
```

### 6.3 TYPE Code Detector (`scripts/detect_new_types.py`)

**Purpose**: Detects unapproved TYPE codes in filenames and generates extension requests.

**Approved TYPE Vocabulary**:
```
PLAN, MIN, RPT, LOG, ACT, IDX,
FHA, PSSA, SSA, FTA, ANA,
REQ, DAL, TRC,
CAT, LST, GLO, MAT, SCH, DIA, TAB, STD
```

**Usage**:
```bash
# Detect new TYPEs
python scripts/detect_new_types.py --directory .

# Auto-generate extension guide
python scripts/detect_new_types.py --auto-suggest
```

### 6.4 File Scaffold Generator (`scripts/scaffold.py`)

**Purpose**: Generates new files from templates with nomenclature compliance.

**Usage**:
```bash
python scripts/scaffold.py <ROOT> <BUCKET> <TYPE> <SUBJECT> <PROJECT> <PROGRAM> <VARIANT> <DESC> <VER>

# Example
python scripts/scaffold.py 00 70 FHA SB70 AMPEL360 SPACET PLUS propulsion v01
```

**Behavior**:
1. Validates all field values against nomenclature rules
2. Looks up template in `templates/[TYPE].md`
3. Fills placeholders with provided values
4. Creates file with compliant filename

## 7. Workflow Technical Specifications

### 7.1 Nomenclature Validation Workflow (`nomenclature-validation.yml`)

**Trigger**: Push/PR to any branch

**Steps**:
1. Checkout repository
2. Set up Python environment
3. Run `python validate_nomenclature.py --check-all --strict --verbose`
4. Fail workflow if validation errors found

**Permissions**: `contents: read`

### 7.2 Governance Gates Workflow (`governance-gates.yml`)

**Trigger**: PR to main/develop, manual dispatch

**Gates Executed**:
1. GATE-001: Nomenclature Validation (BLOCKING)
2. GATE-002: Schema Registration Check (BLOCKING)
3. GATE-005: Identifier Grammar Check (PLANNED)
4. GATE-003: Trace Link Integrity (PLANNED)
5. GATE-004: Namespace Deduplication (PLANNED)
6. GATE-006: Governance Change Detection (LABELING)
7. GATE-007: Breaking Schema Detection (PLANNED)
8. GATE-008: Evidence Link Validation (PLANNED)

**Permissions**: `contents: read`, `issues: write`, `pull-requests: write`

**Outputs**:
- Gate summary table
- PR labels (if governance change detected)
- PR comments (if governance change detected)
- Issues created (if schema registry missing)

### 7.3 Detect New TYPE Codes Workflow (`detect-new-types.yml`)

**Trigger**: Push/PR, weekly schedule (Monday 9:00 UTC), manual dispatch

**Steps**:
1. Checkout repository
2. Set up Python environment
3. Run TYPE detection script
4. Generate extension guide if new TYPEs found
5. Create/update GitHub issue for new TYPEs

## 8. Cross-Reference Matrix

### 8.1 Script to Gate Mapping

| Script | Gates | Workflows | Script Status |
| :--- | :--- | :--- | :--- |
| `validate_nomenclature.py` | GATE-001 | WF-001, WF-002 | **Active** |
| `scripts/validate_schema_registry.py` | GATE-002 | WF-002 | **Active** |
| `scripts/validate_identifiers.py` | GATE-005 | WF-002 (planned) | Planned |
| `scripts/check_trace_integrity.py` | GATE-003 | WF-002 (planned) | Planned |
| `scripts/check_ata99_registry.py` | GATE-004 | WF-002 (planned) | Planned |
| `scripts/detect_new_types.py` | GATE-009 | WF-003 | **Active** |
| `scripts/validate_evidence_links.py` | GATE-008 | WF-002 (planned) | Planned |
| `scripts/check_staleness.py` | GATE-016 | WF-005 (planned) | Planned |
| `scripts/detect_shadow_registries.py` | GATE-017 | WF-005 (planned) | Planned |
| `scripts/generate_trace_coverage.py` | GATE-018 | WF-004 (planned) | Planned |

> **Note**: Scripts marked "Planned" are referenced in workflows but do not yet exist. Workflows handle missing scripts gracefully by skipping those gates.

### 8.2 Gate to Policy Mapping

| Gate | Policy Reference | Governance Authority |
| :--- | :--- | :--- |
| GATE-001 | Nomenclature Standard v3.0 | CM WG |
| GATE-002 | Governance Reference Policy §4.2 | ATA 91 Lead + CM WG |
| GATE-003 | Governance Reference Policy §5.3 | ATA 93 Lead + CM WG |
| GATE-004 | Identifier Grammar §4.5.2 | ATA 99 Lead + CM WG |
| GATE-005 | Identifier Grammar §4.1 | CM WG |
| GATE-006 | Governance Reference Policy §6.3 | CM WG |
| GATE-007 | Governance Reference Policy §4.3 | ATA 91 Lead + CM WG |
| GATE-008 | Governance Reference Policy §7.1 | Evidence Manager + CM WG |
| GATE-009 | Nomenclature Standard v3.0 §4.3 | CM WG |
| GATE-010 | SSOT Decision Matrix §5.1 | CM WG |

### 8.3 Component to ATA Mapping

| Component | Primary ATA | Related ATAs |
| :--- | :--- | :--- |
| Nomenclature Validator | ATA 00 | All ATAs |
| Schema Registry Validator | ATA 91 | ATA 94, 95, 98 |
| Trace Link Validator | ATA 93 | ATA 101, 107, 109 |
| Namespace Dedup Checker | ATA 99 | All ATAs |
| Evidence Pack Generator | ATA 109 | ATA 93, 94, 95 |
| TYPE Detector | ATA 00 | All ATAs |

## 9. Dependencies and Prerequisites

### 9.1 External Dependencies

| Dependency | Type | Version | Purpose |
| :--- | :--- | :--- | :--- |
| Python | Runtime | 3.x | Script execution |
| Git | Tool | 2.x+ | Version control, diff operations |
| GitHub Actions | Platform | N/A | CI/CD execution |

### 9.2 Internal Dependencies

| Automation Component | Depends On | Required Before |
| :--- | :--- | :--- |
| Schema Registry Validator | ATA 91 Schema Registry | Schema validation can be enforced |
| Trace Link Validator | ATA 93 Trace Registry | Trace validation can be enforced |
| Namespace Dedup Checker | ATA 99 Namespace Registry | Dedup enforcement can be activated |
| Evidence Pack Generator | Evidence Schema + Linked Artifacts | Evidence packs can be generated |
| Staleness Detector | Derivation Metadata in Artifacts | Staleness detection can work |

### 9.3 Registry Dependencies

| Registry | Owner | Location | Status |
| :--- | :--- | :--- | :--- |
| ATA 91 Schema Registry | ATA 91 Lead | `**/schema-registry*.csv` | Required for GATE-002 |
| ATA 93 Trace Registry | ATA 93 Lead | `**/trace-registry*.csv` | Required for GATE-003 |
| ATA 99 Namespace Registry | ATA 99 Lead | `**/namespace-registry*.csv` | Required for GATE-004 |
| Evidence Pack Index | Evidence Manager | `**/evidence-pack*.csv` | Required for GATE-008 |

## 10. Maintenance and Support

### 10.1 Update Procedures

| Event | Action Required | Responsible |
| :--- | :--- | :--- |
| Nomenclature Standard Update | Update `validate_nomenclature.py` patterns | AI Team |
| New TYPE Added to Vocabulary | Update `APPROVED_TYPES` in validator | AI Team + CM WG |
| New Registry Created | Add validation script + CI integration | AI Team |
| Gate Status Changes | Update CI governance gates index | AI Team + CM WG |
| New Workflow Added | Update this architecture document | AI Team |

### 10.2 Monitoring and Metrics

| Metric | Source | Frequency | Purpose |
| :--- | :--- | :--- | :--- |
| Validation Pass Rate | CI workflow logs | Per-PR | Gate effectiveness |
| False Positive Rate | Manual review of overrides | Monthly | Validator tuning |
| Gate Block Rate | CI workflow logs | Weekly | Enforcement effectiveness |
| Governance Change Detection Rate | PR labels | Weekly | Detection coverage |
| Issue Creation Rate | GitHub Issues | Weekly | Problem discovery |

### 10.3 Escalation Paths

| Issue Type | First Responder | Escalation |
| :--- | :--- | :--- |
| Validator False Positive | AI Team | CM WG (for override approval) |
| CI Gate Failure | Developer | AI Team (for diagnosis) |
| Registry Missing | AI Team (creates issue) | ATA Lead (creates registry) |
| Governance Change Detected | Developer | CM WG (for approval) |
| Standards Update Needed | AI Team | CM WG (for approval) |

## 11. Related Documents

| Document | Location | Relationship |
| :--- | :--- | :--- |
| K06 ATA 00 Tasklist | `AMPEL360-SPACE-T-PORTAL/.../00_00_IDX_LC01_AMPEL360_SPACET_PLUS_k06-ata-00-tasklist_I01-R01.md` | Source task (T10-AI) |
| CI Governance Gates Index | `00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_LC01_K04_DATA__ci-governance-gates_I01-R01.md` | Gate catalog |
| Nomenclature Automation Guide | `00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_LC01_K04_CM__nomenclature-automation-guide_I01-R02.md` | Usage guide |
| Nomenclature Standard v3.0 | `00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_LC01_K04_CM__nomenclature-standard_I01-R02.md` | Normative standard |
| Identifier Grammar | `00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_LC01_K04_DATA__identifier-grammar_I01-R01.md` | ID format rules |
| SSOT Decision Matrix | `00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_LC01_K04_DATA__ssot-decision-matrix_I01-R01.md` | Ownership rules |
| Governance Reference Policy | `00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_LC01_K04_DATA__governance-reference-policy_I01-R01.md` | Policy framework |
| Portal Card Data Model | `00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_SB90_K11_AI__portal-card-data-model_SCH_I01-R01_ACTIVE.json` | Card/AI Generator schema |
| AI Generator Prompt Token Schema | `00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_SB90_K11_AI__ai-generator-prompt-token-schema_SCH_I01-R01_ACTIVE.json` | Tokenized prompt schema |
| Portal Card UI & Data Model STD | `AMPEL360-SPACE-T-PORTAL/00_AMPEL360_SPACET_Q10_GEN_PLUS_PR_GEN_LC01_K11_AI__portal-card-ui-data-model_STD_I01-R01_ACTIVE.md` | Product documentation |
| GitHub Copilot Instructions | `.github/copilot-instructions.md` | Agent integration |

---

## Document Control

| Field | Value |
| :--- | :--- |
| **Version** | v01 |
| **Status** | Draft |
| **Owner** | STK_AI — AI/ML Engineering |
| **Authority** | STK_CM — Configuration Management |
| **Last Updated** | 2025-12-16 |
| **Next Review** | 2026-03-16 (quarterly) |
| **Related Task** | T10-AI from K06 ATA 00 Tasklist |

---

## Notes

- This document serves as the **authoritative index** for AI automation architecture
- Updates to automation components should be reflected in this document
- Gate implementation status should be kept current with CI governance gates index
- Script specifications should be updated when implementations change
