---
title: "Portal Card UI & Data Model: AI Generator Tab"
type: STD
project: "AMPEL360"
program: "SPACET"
variant: "GEN"
owner: "AI / Configuration Management WG"
status: Active
schema_refs:
  - schema_id: "SCH-CARD-001-V01"
    registry: "ATA 91"
    status: "active"
  - schema_id: "SCH-PROMPT-001-V01"
    registry: "ATA 91"
    status: "active"
trace_links:
  - type: "satisfies"
    target: "REQ-PORTAL-001"
    status: "implemented"
  - type: "satisfies"
    target: "REQ-PORTAL-002"
    status: "implemented"
---

# Standard: Portal Card UI & Data Model

## 1. Purpose

This standard defines the **card-based user interface** and **data model** for the AMPEL360-SPACE-T Portal. The portal surfaces each Area of Responsibility (AoR) as an individual card and provides an **AI Generator tab** on every card for producing audience-targeted, schema-conformant content.

### 1.1 Scope

This standard applies to:

- The portal card UI layout and card-to-AoR mapping
- The AI Generator tab component embedded in each card
- The tokenized prompt data model (prompt composition, audience binding, template binding, metadata schema binding)
- The generator output specification (content body, metadata values, schema conformance, traceability, write-back)

### 1.2 Applicability

**Mandatory compliance** for:

- Portal UI developers and designers
- AI/ML engineering teams implementing the generator
- Configuration Management WG (prompt governance)
- All stakeholder teams consuming generator output

## 2. Normative References

| Reference | Title | Authority |
| :--- | :--- | :--- |
| `portal-card-data-model_SCH` | Portal Card Data Model JSON Schema | AMPEL360 Space-T |
| `ai-generator-prompt-token-schema_SCH` | AI Generator Prompt Token Schema | AMPEL360 Space-T |
| `knots-data-structure_SCH` | Knots Data Structure Schema | AMPEL360 Space-T |
| Nomenclature Standard v6.0 R1.0 | Naming conventions | AMPEL360 Space-T |
| ATA 91 | Schema Registry & Versioning | AMPEL360 Space-T |
| ATA 93 | Trace Semantics & Evidence Links | AMPEL360 Space-T |
| `governance-reference-policy_STD` | Schema & Trace Coupling Policy | AMPEL360 Space-T |

## 3. Terms and Definitions

- **AoR (Area of Responsibility)**: A stakeholder domain in the portal (e.g., CM, CERT, SAF, AI). Maps 1:1 to a `STK_*` directory.
- **Portal Card**: A UI element representing exactly one AoR entry. Contains tabs for navigation, knot status, and AI generation.
- **AI Generator Tab**: A tab within a portal card that stores and activates tokenized prompts.
- **Tokenized Prompt**: A reusable, composable prompt definition assembled from ordered token units. Each prompt is bound to an audience/role, a template ID, and a metadata schema.
- **Prompt Token**: An atomic, reusable prompt unit (e.g., an instruction, context block, constraint, or format directive). Tokens can be shared across prompts.
- **Audience Binding**: The association of a prompt with a target role/audience that determines content tone, depth, and vocabulary.
- **Template Binding**: The association of a prompt with a document TYPE template (e.g., STD, RPT, FHA) whose structure the generated content must fill.
- **Metadata Schema Binding**: The association of a prompt with a schema (registered in ATA 91) whose required fields the generated metadata must satisfy.
- **Write-back**: The process of persisting generator output to the AoR record from which the generation was triggered.

## 4. Card-Based UI Architecture

### 4.1 Card Layout

The portal presents a **card grid** where each card represents exactly one AoR entry. The set of cards corresponds 1:1 with the `STK_*` directories in `AMPEL360-SPACE-T-PORTAL/`.

```
┌─────────────────────────────────────────────────────┐
│                AMPEL360 SPACE-T PORTAL               │
├─────────┬─────────┬─────────┬─────────┬─────────────┤
│  CM     │  CERT   │  SAF    │  SE     │  OPS        │
│  Card   │  Card   │  Card   │  Card   │  Card       │
├─────────┼─────────┼─────────┼─────────┼─────────────┤
│  DATA   │  AI     │  CY     │  TEST   │  MRO        │
│  Card   │  Card   │  Card   │  Card   │  Card       │
├─────────┼─────────┼─────────┼─────────┼─────────────┤
│  PMO    │ SPACEPORT│  PHM   │         │             │
│  Card   │  Card   │  Card   │         │             │
└─────────┴─────────┴─────────┴─────────┴─────────────┘
```

### 4.2 Card Structure

Each portal card exposes the following tabs:

| Tab | Purpose |
| :--- | :--- |
| **Overview** | AoR name, description, owner, status |
| **Knots** | Active backlog knots with affected ATAs |
| **AI Generator** | Tokenized prompt library and generation controls |
| **Audit Trail** | Generation log and write-back history |

### 4.3 Card-to-AoR Mapping

| Card ID Pattern | AoR Code | STK Directory |
| :--- | :--- | :--- |
| `CARD-CM-001` | CM | `STK_CM-cm-configuration-management/` |
| `CARD-CERT-001` | CERT | `STK_CERT-cert-certification-authorities/` |
| `CARD-SAF-001` | SAF | `STK_SAF-saf-safety/` |
| `CARD-SE-001` | SE | `STK_SE-se-systems-engineering/` |
| `CARD-OPS-001` | OPS | `STK_OPS-ops-operations/` |
| `CARD-DATA-001` | DATA | `STK_DATA-data-data-governance/` |
| `CARD-AI-001` | AI | `STK_AI-ai-ai-ml-engineering/` |
| `CARD-CY-001` | CY | `STK_CY-cy-cybersecurity/` |
| `CARD-TEST-001` | TEST | `STK_TEST-test-ivvq-testing/` |
| `CARD-MRO-001` | MRO | `STK_MRO-mro-mro-maintenance/` |
| `CARD-SPACEPORT-001` | SPACEPORT | `STK_SPACEPORT-spaceport-spaceport-ops/` |
| `CARD-PMO-001` | PMO | `STK_PMO-pmo-program-management-office/` |
| `CARD-PHM-001` | PHM | `STK_PHM-phm-physical-hardware-mechanical-engineering/` |

## 5. AI Generator Tab

### 5.1 Overview

The AI Generator tab is a component of every portal card. It provides:

1. **Prompt Library** — a collection of tokenized prompts available for the card's AoR
2. **Generation Controls** — UI to select a prompt, configure parameters, and activate generation
3. **Output Preview** — rendered preview of generated content before write-back
4. **Validation Status** — real-time schema conformance check of generated output

### 5.2 Tokenized Prompt Model

Each tokenized prompt is a reusable prompt definition composed of ordered **prompt tokens**. A tokenized prompt is bound to three axes:

```
                    ┌──────────────┐
                    │  Tokenized   │
                    │   Prompt     │
                    │  PROMPT-*    │
                    └──────┬───────┘
                           │
              ┌────────────┼────────────┐
              │            │            │
     ┌────────▼───┐  ┌─────▼──────┐  ┌──▼──────────────┐
     │  Audience  │  │  Template  │  │ Metadata Schema  │
     │  Binding   │  │  Binding   │  │ Binding          │
     │ role_code  │  │ template_id│  │ schema_ref       │
     │ role_name  │  │ template   │  │ required_fields  │
     │ clearance  │  │ path       │  │ schema_version   │
     └────────────┘  └────────────┘  └──────────────────┘
```

#### 5.2.1 Audience/Role Binding

Every tokenized prompt targets a specific audience:

| Field | Type | Description |
| :--- | :--- | :--- |
| `role_code` | string | AoR code from v6.0 allowlist (e.g., `CM`, `SAF`, `CERT`) |
| `role_name` | string | Human-readable name (e.g., "Safety Engineers") |
| `clearance_level` | enum | `public`, `internal`, `restricted`, `confidential` |

The audience binding determines the tone, vocabulary, depth, and access level of the generated content.

#### 5.2.2 Template ID Binding

Every tokenized prompt targets a specific document TYPE template:

| Field | Type | Description |
| :--- | :--- | :--- |
| `template_id` | enum | TYPE code from v6.0 allowlist (e.g., `STD`, `RPT`, `FHA`) |
| `template_path` | string | Path to the template file (e.g., `templates/FHA.md`) |
| `required_sections` | array | Template sections the generator must populate |

The template binding defines the structural contract that the generated content must fulfill.

#### 5.2.3 Metadata Schema Binding

Every tokenized prompt specifies a metadata schema that its output must satisfy:

| Field | Type | Description |
| :--- | :--- | :--- |
| `schema_ref` | string | Schema ID in ATA 91 format (e.g., `SCH-FHA-001-V02`) |
| `required_metadata_fields` | array | Field definitions the generator must emit |
| `schema_version` | string | Schema version (e.g., `V02`) |

### 5.3 Prompt Token Units

Prompts are composed from an ordered sequence of **prompt tokens**. Each token is a reusable unit with a specific function:

| Token Type | Purpose | Example |
| :--- | :--- | :--- |
| `instruction` | Core generation directive | "Generate an FHA for the propulsion subsystem" |
| `context` | Background information | "The propulsion system uses cryogenic hydrogen fuel" |
| `constraint` | Boundary or rule | "Do not reference classified material" |
| `example` | Sample output pattern | "See Appendix A for expected hazard table format" |
| `format` | Output structure directive | "Use markdown tables with columns: ID, Hazard, Severity, Likelihood" |
| `audience_directive` | Audience-specific tuning | "Write for safety certification reviewers; use formal technical language" |
| `schema_directive` | Metadata generation rule | "Populate title, type, variant, system, and schema_refs fields in YAML frontmatter" |

Tokens are identified by `TKN-{CATEGORY}-{NNNN}` (e.g., `TKN-INSTR-0001`) and can be shared across prompts via the shared token library.

### 5.4 Prompt Composition Example

```yaml
prompt_id: "PROMPT-SAF-0001"
version: "1.0.0"
title: "Generate FHA for Propulsion Subsystem"
audience_binding:
  role_code: "SAF"
  role_name: "Safety Engineers"
  clearance_level: "internal"
template_binding:
  template_id: "FHA"
  template_path: "templates/FHA.md"
  required_sections:
    - "Functional Hazard Identification"
    - "Hazard Classification"
    - "Safety Objectives"
metadata_schema_binding:
  schema_ref: "SCH-FHA-001-V02"
  required_metadata_fields:
    - field_name: "title"
      field_type: "string"
    - field_name: "type"
      field_type: "enum"
      enum_values: ["FHA"]
    - field_name: "system"
      field_type: "string"
    - field_name: "schema_refs"
      field_type: "array"
token_sequence:
  - token_ref: "TKN-AUDIR-0001"   # audience directive for SAF
  - token_ref: "TKN-INSTR-0010"   # FHA generation instruction
  - token_ref: "TKN-CNTXT-0005"   # propulsion system context
    parameter_overrides:
      subsystem: "propulsion"
  - token_ref: "TKN-FRMAT-0003"   # FHA table format directive
  - token_ref: "TKN-SCHDR-0001"   # metadata schema directive
output_spec:
  content_format: "markdown"
  must_fill_placeholders:
    - "{{TITLE}}"
    - "{{SYSTEM_NAME}}"
    - "{{DATE}}"
  writeback_target: "aor_record"
status: "active"
```

## 6. Generator Output Specification

### 6.1 Output Structure

When the AI Generator is activated, it **must** produce a structured output containing:

| Output Component | Description | Required |
| :--- | :--- | :--- |
| `content_body` | Audience-targeted content that fills the template body | ✅ |
| `metadata_values` | Key-value pairs satisfying the template metadata schema | ✅ |
| `schema_validation` | Result of validating output against the metadata schema | ✅ |
| `trace` | Traceability record linking output to prompt ID and version | ✅ |

### 6.2 Content Body Requirements

The `content_body` must:

1. **Fill the template structure** defined by `template_id` — all `required_sections` must be populated.
2. **Target the bound audience** — language, depth, and terminology must match the `audience_binding`.
3. **Resolve all placeholders** listed in `must_fill_placeholders`.
4. **Conform to AMPEL360 document conventions** — YAML frontmatter, section numbering, table formatting.

### 6.3 Metadata Value Requirements

The `metadata_values` must:

1. **Satisfy every field** in `required_metadata_fields` from the `metadata_schema_binding`.
2. **Pass type validation** — each field must match its declared `field_type`.
3. **Pass pattern validation** — fields with `validation_pattern` must match the regex.
4. **Include `schema_refs`** pointing to the bound schema in ATA 91.

### 6.4 Schema Conformance

Before write-back, the generator output must pass schema validation:

```
Output ──► Schema Validator ──► { is_conformant: true/false, validation_errors: [...] }
                │
                ▼
        schema_ref from metadata_schema_binding
```

- **Conformant output**: proceeds to write-back.
- **Non-conformant output**: blocked from write-back; validation errors are surfaced in the UI.

### 6.5 Traceability

Every generator output must include a `trace` object with:

| Trace Field | Description |
| :--- | :--- |
| `prompt_id` | ID of the tokenized prompt used |
| `prompt_version` | Version of the prompt at time of generation |
| `generation_id` | Unique ID for this generation event (`GEN-YYYYMMDD-HHMMSS-XXXX`) |
| `template_id` | TYPE code of the template filled |
| `audience_role_code` | AoR code of the target audience |

This trace information enables full auditability: any generated artifact can be traced back to the exact prompt version, audience, and template that produced it.

### 6.6 Write-Back

Conformant, validated output is **written back** to the AoR record:

1. **Target**: The `writeback_target` field determines where the output is persisted:
   - `aor_record` — written to the stakeholder entrypoint or card-level record
   - `knot_task` — written to the specific KNOT/ATA task directory
   - `ata_evidence` — written to the EVIDENCE/ subdirectory
   - `stakeholder_entrypoint` — updates the stakeholder IDX

2. **File naming**: Output files follow v6.0 nomenclature, with the TYPE matching the `template_id`.

3. **Generation log**: Each write-back creates a `generation_record` in the card's `generation_log` with status `written_back`.

## 7. Data Model Summary

### 7.1 Entity Relationship

```
┌──────────────┐ 1    1 ┌──────────────┐
│  Portal Card │────────│  AoR Entry   │
│  (CARD-*)    │        │  (STK_*)     │
└──────┬───────┘        └──────────────┘
       │ 1
       │
       │ 1
┌──────▼───────┐
│ AI Generator │
│     Tab      │
└──────┬───────┘
       │ 1
       │
       │ *
┌──────▼───────┐       ┌──────────────┐
│  Tokenized   │ * ──► │ Prompt Token │
│  Prompt      │       │ (TKN-*)      │
│ (PROMPT-*)   │       └──────────────┘
└──────┬───────┘
       │
  ┌────┼────────────┐
  │    │             │
  ▼    ▼             ▼
┌────┐┌──────┐┌──────────┐
│Aud.││Templ.││ Metadata │
│Bind││Bind. ││ Schema   │
│    ││      ││ Binding  │
└────┘└──────┘└──────────┘
       │
       │ activates
       ▼
┌──────────────┐
│  Generator   │
│  Output      │
├──────────────┤
│ content_body │
│ metadata_val │
│ schema_valid │
│ trace        │
└──────┬───────┘
       │ writes back to
       ▼
┌──────────────┐
│  AoR Record  │
│  (STK_*)     │
└──────────────┘
```

### 7.2 JSON Schema References

| Schema | File | Purpose |
| :--- | :--- | :--- |
| Portal Card Data Model | `portal-card-data-model_SCH_I01-R01_ACTIVE.json` | Card structure, AI generator tab, output format |
| Prompt Token Schema | `ai-generator-prompt-token-schema_SCH_I01-R01_ACTIVE.json` | Shared tokens, prompt definitions, bindings |

## 8. Enforcement

### 8.1 Validation Rules

| Rule | Check | Gate |
| :--- | :--- | :--- |
| Every card maps to exactly one AoR | Card ID matches AoR code | CI: card-aor-mapping |
| Every prompt has audience binding | `audience_binding.role_code` is present | CI: prompt-validation |
| Every prompt has template binding | `template_binding.template_id` is present | CI: prompt-validation |
| Every prompt has metadata schema binding | `metadata_schema_binding.schema_ref` is present | CI: prompt-validation |
| Generator output is schema-conformant | `schema_validation.is_conformant == true` | Runtime: pre-writeback |
| Generator output includes trace | `trace.prompt_id` and `trace.prompt_version` are present | Runtime: pre-writeback |
| Write-back follows v6.0 nomenclature | Output filename validates against v6.0 | CI: nomenclature-check |

### 8.2 Change Control

Changes to the portal card data model or prompt token schema require:

1. **CM WG approval** for schema changes
2. **AI WG review** for prompt library changes
3. **Impact analysis** on existing generated artifacts
4. **Schema version increment** following ATA 91 versioning policy

---

**Document Control**

| Field | Value |
| :--- | :--- |
| **Version** | I01-R01 |
| **Status** | Active |
| **Owner** | AI / Configuration Management WG |
| **Last Updated** | 2026-02-25 |
| **Coordinated With** | ATA 91 (Schemas), ATA 93 (Trace), AI WG, CM WG |
