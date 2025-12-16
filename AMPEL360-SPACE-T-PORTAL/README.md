# AMPEL360-SPACE-T-PORTAL

**CAXS — Computer-Aided Cross Sustainment Environment**

---

## Overview

The **AMPEL360-SPACE-T-PORTAL** is the first **CAXS (Computer-Aided Cross Sustainment)** environment: a GitHub-based, all-in-one digital workspace for cross-ATA program follow-up and controlled publications (Knots, tasklists, evidence, releases) across the Space-T lifecycle.

It provides a single, navigable workspace integrating stakeholder collaboration, uncertainty resolution, governed outputs, and controlled publication channels into one comprehensive GitHub-based structure.

### Terminology

**CAXS — Computer-Aided Cross Sustainment**  
Technical term for this integrated digital environment combining:
- **Cross-ATA coordination** — Multi-discipline program follow-up
- **Traceability** — Evidence chains and provenance tracking
- **Evidence packaging** — Structured compliance artifacts
- **Controlled publications** — RBAC-governed output channels
- **Lifecycle sustainment** — From requirements through operations

*Also known as:* **CA360º** (Computer-Aided Everything) — equivalent branding term emphasizing the comprehensive, 360-degree coverage across all program activities.

### Key Features

1. **Stakeholder Entry Points (AoR)** — Role-based navigation and cross-stakeholder collaboration
2. **Backlog Knots** — Structured uncertainty resolution pathways linked to ATA tasklists
3. **Governed Outputs** — Standards, plans, requirements, evidence packs, and releases under CM control
4. **Controlled Publication Channels** — Multi-tier access control (RBAC) for internal, operations, authority, and supplier audiences

---

## Portal Structure

```
AMPEL360-SPACE-T-PORTAL/
├── README.md                                          # This file
├── 00_00_IDX_LC01_SPACET_stakeholder-entrypoints_v01.md  # Master stakeholder index
├── 00_00_TAB_LC01_SPACET_knot-register_v01.csv       # Active knot registry
│
├── STK_AI-ai-ai-ml-engineering/                      # AI/ML Engineering stakeholder
│   ├── 00_00_IDX_LC01_SPACET_stakeholder-ai-entrypoint_v01.md
│   └── KNOTS/
│       ├── K06_data-governance-ssot-schemas-identifiers/
│       ├── K07_ai-autonomy-assurance-monitoring/
│       └── K13_cybersecurity-zones-key-management/
│
├── STK_CERT-cert-certification-authorities/          # Certification & Authorities
├── STK_CM-cm-configuration-management/               # Configuration Management
├── STK_CY-cy-cybersecurity/                          # Cybersecurity
├── STK_DATA-data-data-governance/                    # Data Governance
├── STK_MRO-mro-mro-maintenance/                      # MRO / Maintenance
├── STK_OPS-ops-operations/                           # Operations
├── STK_PMO-pmo-program-management-office/            # Program Management Office
├── STK_SAF-saf-safety/                               # Safety
├── STK_SE-se-systems-engineering/                    # Systems Engineering
├── STK_SPACEPORT-spaceport-spaceport-airport-ops/    # Spaceport/Airport Ops
└── STK_TEST-test-ivvq-testing/                       # IVVQ / Testing
```

Each stakeholder workspace contains:
- **One canonical entry point** (IDX file) describing their Area of Responsibility (AoR)
- **KNOTS/** directory with Backlog Knots for uncertainty resolution
- **ATA_TASKS/** subdirectories within each knot, linking to ATA-specific tasklists

---

## 1. Stakeholder Entry Points (AoR)

### What Are Stakeholder Entry Points?

Each stakeholder has a dedicated workspace with a single, navigable **entry point** that defines:
- **Area of Responsibility (AoR)** — What the stakeholder owns and contributes to
- **Active Knots** — Which uncertainty resolution pathways they participate in
- **Navigation Rules** — How to find and execute work within their workspace
- **Coordination Interfaces** — How they collaborate with other stakeholders

### Complete Stakeholder List

| Stakeholder | ID | Entry Point | Primary AoR |
|:------------|:---|:------------|:------------|
| **AI/ML Engineering** | AI | [stakeholder-ai-entrypoint](STK_AI-ai-ai-ml-engineering/00_AMPEL360_SPACET_PLUS_00_IDX_LC01_K00_AI__stakeholder-ai-entrypoint_v01.md) | ML lifecycle, datasets, models, TEKNIA packaging |
| **Certification & Authorities** | CERT | [stakeholder-cert-entrypoint](STK_CERT-cert-certification-authorities/00_AMPEL360_SPACET_PLUS_00_IDX_LC01_K00_CERT__stakeholder-cert-entrypoint_v01.md) | Authority engagement, compliance mapping, evidence packaging |
| **Configuration Management** | CM | [stakeholder-cm-entrypoint](STK_CM-cm-configuration-management/00_AMPEL360_SPACET_PLUS_00_IDX_LC01_K00_CM__stakeholder-cm-entrypoint_v01.md) | Governance spine, baselines, change control, CI enforcement |
| **Cybersecurity** | CY | [stakeholder-cy-entrypoint](STK_CY-cy-cybersecurity/00_AMPEL360_SPACET_PLUS_00_IDX_LC01_K00_CY__stakeholder-cy-entrypoint_v01.md) | Threat models, security requirements, SBOM coupling |
| **Data Governance** | DATA | [stakeholder-data-entrypoint](STK_DATA-data-data-governance/00_AMPEL360_SPACET_PLUS_00_IDX_LC01_K00_DATA__stakeholder-data-entrypoint_v01.md) | SSOT definitions, schema governance, identifier discipline |
| **MRO / Maintenance** | MRO | [stakeholder-mro-entrypoint](STK_MRO-mro-mro-maintenance/00_AMPEL360_SPACET_PLUS_00_IDX_LC01_K00_MRO__stakeholder-mro-entrypoint_v01.md) | Maintainability, servicing, continued airworthiness |
| **Operations** | OPS | [stakeholder-ops-entrypoint](STK_OPS-ops-operations/00_AMPEL360_SPACET_PLUS_00_IDX_LC01_K00_OPS__stakeholder-ops-entrypoint_v01.md) | Operational concepts, procedures, mission profiles |
| **Program Management Office** | PMO | [stakeholder-pmo-entrypoint](STK_PMO-pmo-program-management-office/00_AMPEL360_SPACET_PLUS_00_IDX_LC01_K00_PMO__stakeholder-pmo-entrypoint_v01.md) | Program cadence, milestones, resourcing, prioritization |
| **Safety** | SAF | [stakeholder-saf-entrypoint](STK_SAF-saf-safety/00_AMPEL360_SPACET_PLUS_00_IDX_LC01_K00_SAF__stakeholder-saf-entrypoint_v01.md) | Safety processes, hazard logs, safety cases |
| **Systems Engineering** | SE | [stakeholder-se-entrypoint](STK_SE-se-systems-engineering/00_AMPEL360_SPACET_PLUS_00_IDX_LC01_K00_SE__stakeholder-se-entrypoint_v01.md) | System architecture, ICDs, requirements decomposition |
| **Spaceport/Airport Ops** | SPACEPORT | [stakeholder-spaceport-entrypoint](STK_SPACEPORT-spaceport-spaceport-airport-ops/00_AMPEL360_SPACET_PLUS_00_IDX_LC01_K00_SPACEPORT__stakeholder-spaceport-entrypoint_v01.md) | Ground operations, turnaround, fueling/servicing interfaces |
| **IVVQ / Testing** | TEST | [stakeholder-test-entrypoint](STK_TEST-test-ivvq-testing/00_AMPEL360_SPACET_PLUS_00_IDX_LC01_K00_TEST__stakeholder-test-entrypoint_v01.md) | Verification strategy, test evidence nodes, qualification |

📋 **Master Index**: [`00_00_IDX_LC01_SPACET_stakeholder-entrypoints_v01.md`](00_AMPEL360_SPACET_PLUS_00_IDX_LC01_K00_CM__stakeholder-entrypoints_v01.md)

### Cross-Stakeholder Collaboration

Stakeholders collaborate through **shared Backlog Knots**. Each knot addresses a cross-cutting uncertainty (e.g., data governance, certification basis) that requires input from multiple disciplines. The knot structure ensures:

- **Partitioned Uncertainty Resolution** — Each stakeholder tackles their portion using ATA-specific tasklists
- **Coordinated Decision-Making** — Decisions require cross-stakeholder input and CM approval
- **Unified Evidence Chains** — All contributions link to the same traceability graph
- **NKU Progress Tracking** — Net Knowledge Unit (NKU) metrics track resolution progress

---

## 2. Backlog Knots — Uncertainty Resolution Pathways

### What Are Backlog Knots?

A **Backlog Knot** is a structured pathway for resolving program-wide uncertainty. Each knot represents a critical cross-cutting concern that impacts multiple ATA chapters and requires coordinated resolution.

### Active Knots Registry

📊 **Knot Register**: [`00_00_TAB_LC01_SPACET_knot-register_v01.csv`](00_AMPEL360_SPACET_PLUS_00_TAB_LC01_K00_DATA__knot-register_v01.csv)

| Knot ID | Title | Stakeholders | Affected ATAs |
|:--------|:------|:-------------|:--------------|
| **K01** | Certification Authority Basis | CM, PMO, SAF, CERT | 00, 01, 04, 05, 18, 20-28, 42, 100, 109, 115 |
| **K02** | CONOPS & Mission Phases | PMO, SE, OPS | 01, 02, 09, 10, 18, 21, 22, 27, 34, 100, 102, 112 |
| **K03** | Hazmat, Cryo, Propellants Safety Case | SAF, SPACEPORT | 12, 18, 26, 28, 47, 78, 81, 84, 110 |
| **K04** | Integration Boundaries & ICDs | CM, SE | 00, 06, 22-24, 27, 40, 42, 46, 71, 73, 76, 83, 111 |
| **K05** | Model Fidelity & Verification Credit | SE, SAF, CERT, TEST | 05-08, 18, 21, 22, 24, 27, 32, 53, 57, 100, 101, 109, 110, 113 |
| **K06** | Data Governance, SSOT, Schemas, Identifiers | CM, SE, DATA, AI, CY | 00, 06, 31, 45, 46, 90-95, 99, 101, 107, 109 |
| **K07** | AI Autonomy Assurance & Monitoring | AI | 22, 27, 42, 90, 96, 114 |
| **K08** | DPP, SBOM, Provenance Scope | CM, DATA | 00, 85, 93-95, 98, 99 |
| **K09** | Infrastructure Permitting & Jurisdiction | OPS, SPACEPORT, CY | 09, 12, 80, 81, 83, 84, 87, 89, 110 |
| **K10** | Industrialization, Supply Chain, Quality | CM, PMO, CERT, SPACEPORT, MRO, TEST | 00, 05, 10, 20, 51, 70, 80, 82, 89, 100, 115 |
| **K11** | Human Factors & Training Readiness | SAF, OPS, SPACEPORT, MRO | 01, 09-12, 18, 25, 44, 84, 112 |
| **K12** | NVH Metrics, Corridors, Exposure | SAF, OPS, TEST | 18, 61, 78, 110, 112 |
| **K13** | Cybersecurity Zones & Key Management | AI, CY, DATA | 23, 46, 83, 87, 90, 94, 98, 103, 111 |
| **K14** | Reliability Growth, Maintenance Intervals, Health | PMO, SE, OPS, MRO, TEST | 05, 08, 45, 77, 79, 88, 108, 113 |

### Knot Structure

Each knot follows a standard structure within stakeholder workspaces:

```
STK_<ID>/
└── KNOTS/
    └── K##_<knot-title>/
        ├── 00_00_IDX_LC01_SPACET_k##-<knot-title>_v01.md   # Knot master index
        └── ATA_TASKS/
            ├── ATA_00/
            │   └── 00_00_IDX_LC01_SPACET_k##-ata-00-tasklist_v01.md
            ├── ATA_06/
            │   └── 06_00_IDX_LC01_SPACET_k##-ata-06-tasklist_v01.md
            └── ATA_##/
                └── ##_00_IDX_LC01_SPACET_k##-ata-##-tasklist_v01.md
```

### ATA-Linked Tasklists

Each knot is partitioned by **ATA chapter**, with dedicated tasklists that define:

- **Partition Scope** — What uncertainties exist for this ATA within this knot
- **Closure Criteria** — Required deliverables (IDs, Schema, Exports, CI, Evidence, Decisions)
- **Evidence Links** — Traceability to authoritative artifacts
- **NKU Control** — Progress metrics and thresholds
- **Coordination Points** — Dependencies on other ATAs or stakeholders

### Uncertainty Resolution Process

1. **Select Knot** — Navigate to your stakeholder workspace, choose active knot
2. **Pick ATA Tasklist** — Open the relevant ATA partition within the knot
3. **Execute by Partitions** — Complete work in structured partitions (IDs → Schema → Exports → CI → Evidence → Decisions → Adoption)
4. **Update NKU Ledgers** — Track progress and closure status
5. **Route to CM** — Submit governance-impacting changes for approval and baseline tagging

---

## 3. Governed Outputs

### Output Categories

The portal produces four categories of governed outputs, all under Configuration Management control:

#### 3.1 Standards (STD)

Normative documents defining how work is done:
- **Nomenclature Standard** — File naming convention and validation rules
- **Governance Reference Policy** — Schema and trace coupling requirements
- **SSOT Decision Matrix** — Authority assignments for artifacts
- **Identifier Grammar** — Canonical ID format and namespace boundaries

📂 **Location**: Root repository (`00_00_STD_LC01_SPACET_*`)

#### 3.2 Plans (PLAN)

Implementation strategies and execution roadmaps:
- **SSOT Implementation Plan** — Data governance rollout
- **Safety Program Plans** — Safety management approach
- **Verification Plans** — Test and validation strategies

📂 **Location**: Root repository and stakeholder workspaces (`##_00_PLAN_*`)

#### 3.3 Requirements (REQ)

Functional, performance, and safety requirements:
- **System Requirements** — Top-level spacecraft requirements
- **Subsystem Requirements** — ATA-specific requirements
- **Software Safety Requirements** — DO-178C compliant specifications
- **Interface Requirements** — ICD specifications

📂 **Location**: ATA chapter directories (`##_40_REQ_*`)

#### 3.4 Evidence Packs (IDX + multiple types)

Structured collections proving task completion and compliance:
- **Task Evidence Pack** — All deliverables for a specific task
- **Approval Logs** — Decision records and sign-offs
- **Traceability Matrices** — Requirement-to-verification links
- **Validation Results** — Test reports and analysis

📂 **Location**: Root repository and stakeholder KNOTS (`00_00_IDX_*_evidence-pack_*`)

#### 3.5 Releases (RPT)

Frozen baseline manifests and release documentation:
- **Baseline Release Manifest** — Complete artifact inventory with checksums
- **Change History** — Version control and approval trail
- **Validation Results** — Schema compliance and business rule checks

📂 **Location**: ATA chapter directories (`##_00_RPT_*_baseline-release-manifest_*`)

### Governance Process

All governed outputs follow a standard approval workflow:

1. **Draft Creation** — Author creates artifact following templates and nomenclature
2. **Validation** — CI/CD gates check nomenclature, schema compliance, trace integrity
3. **Review** — Stakeholders review and provide feedback
4. **CM Approval** — Configuration Management WG approves baseline inclusion
5. **Baseline Tagging** — Artifact tagged with baseline ID (e.g., BL-0001)
6. **Publication** — Artifact published to appropriate channel(s)

---

## 4. Controlled Publication Channels (RBAC)

### Multi-Tier Access Control

The portal implements **Role-Based Access Control (RBAC)** to ensure appropriate audience access to different artifact types. Publication channels are structured by intended audience and sensitivity level.

### Publication Channels

#### 4.1 Internal Workspace (All Stakeholders)

**Audience**: All program team members with repository access

**Content Types**:
- Working drafts and in-progress artifacts
- Stakeholder entry points and navigation indexes
- Active knot tasklists and work-in-progress evidence
- Internal decision minutes and approvals
- Development schemas and data exports (draft status)

**Access Control**: GitHub repository access (private repository)

**Publication Method**: Direct commit to PORTAL workspace

**Example Artifacts**:
- `STK_*/KNOTS/K##_*/ATA_TASKS/**/*.md`
- `00_00_MIN_LC01_SPACET_*_decisions_v01.md` (draft)
- `##_90_SCH_*_v01.json` (status: draft)

---

#### 4.2 Ops-Facing Documentation

**Audience**: Operations teams, flight crews, mission control, ground operations

**Content Types**:
- Operational procedures and checklists
- Mission profiles and CONOPS
- Operational constraints and flight envelopes
- Crew training materials
- Ground operations manuals
- Maintenance procedures (MRO)

**Access Control**: Operations teams (internal + authorized external personnel)

**Publication Method**: Export to controlled ops documentation system

**Approval Required**: OPS stakeholder + CM approval

**Example Artifacts**:
- Operational procedures from `STK_OPS/` and `STK_SPACEPORT/`
- Flight manuals and crew checklists
- Ground turnaround procedures
- MRO servicing instructions

**Export Format**: PDF with version watermarks, controlled distribution

---

#### 4.3 Authority Packs (Certification Evidence)

**Audience**: Certification authorities (FAA, EASA, ESA), auditors, compliance officers

**Content Types**:
- Evidence packs proving compliance with certification basis
- Safety cases and hazard analysis reports
- Verification and validation results
- Requirements traceability matrices
- Approval logs and decision records
- Test reports and qualification evidence
- Standards and governance policies (normative)

**Access Control**: Restricted to certification authorities and authorized audit personnel

**Publication Method**: Formal evidence package submission with provenance chain

**Approval Required**: CERT stakeholder + SAF (if safety) + CM approval

**Package Structure**:
```
AUTHORITY_PACK_<ID>/
├── COVER_LETTER.pdf                    # Submission letter
├── EVIDENCE_INDEX.pdf                  # Master evidence index
├── STANDARDS/                          # Normative standards
│   ├── 00_00_STD_*.pdf
│   └── ...
├── REQUIREMENTS/                       # Requirements specifications
│   ├── ##_##_REQ_*.pdf
│   └── ...
├── SAFETY/                             # Safety evidence
│   ├── FHA reports
│   ├── PSSA reports
│   ├── Hazard logs
│   └── Safety cases
├── VERIFICATION/                       # V&V evidence
│   ├── Test reports
│   ├── Traceability matrices
│   └── Validation results
├── TRACEABILITY/                       # Trace graphs
│   └── Complete REQ→DESIGN→TEST→EVIDENCE chains
├── APPROVALS/                          # Approval records
│   ├── Decision minutes
│   └── Approval logs
└── MANIFEST.json                       # Digital signature, checksums
```

**Digital Signing**: All authority packs signed with organizational key, includes checksum manifest

**Example Artifacts**:
- `00_00_IDX_LC01_SPACET_k06-evidence-pack_v01.md` → Evidence_Pack_K06.pdf
- `00_00_STD_LC01_SPACET_governance-reference-policy_v01.md` → Policy_Document.pdf
- Complete safety case for specific systems
- Full traceability from requirement to qualification

---

#### 4.4 Supplier-Facing Specifications

**Audience**: External suppliers, subcontractors, manufacturing partners

**Content Types**:
- Interface Control Documents (ICDs)
- Component specifications and requirements
- Manufacturing requirements and quality standards
- Test acceptance criteria
- Dimensional data and CAD references (as needed)
- DPP requirements and SBOM expectations
- Supply chain quality procedures

**Access Control**: Supplier portal access (controlled by procurement/contracts)

**Publication Method**: Export to supplier collaboration platform with NDA enforcement

**Approval Required**: SE (technical) + CM (baseline) + Procurement (contractual)

**Example Artifacts**:
- ICDs for subsystem interfaces
- Component requirements specifications
- Quality acceptance criteria
- Manufacturing process requirements
- Test procedures and acceptance criteria
- DPP and SBOM formatting requirements

**Export Format**: Controlled PDF release with revision control and watermarking

**Supplier Feedback Loop**: 
- Suppliers can request clarifications → routed to SE/CM
- Change requests tracked in CM system
- Formal interface change process for ICD updates

---

### RBAC Implementation

#### Access Matrix

| Artifact Type | Internal | Ops | Authority | Supplier |
|:--------------|:---------|:----|:----------|:---------|
| Draft working documents | ✅ | ❌ | ❌ | ❌ |
| Knot tasklists | ✅ | ❌ | ❌ | ❌ |
| Approved standards (STD) | ✅ | ✅ | ✅ | Subset |
| Operational procedures | ✅ | ✅ | Review only | ❌ |
| Evidence packs | ✅ | ❌ | ✅ | ❌ |
| Safety cases | ✅ | Review only | ✅ | ❌ |
| ICDs | ✅ | Review only | Review only | ✅ |
| Component specs | ✅ | ❌ | Review only | ✅ |
| Baseline releases | ✅ | As needed | ✅ | As contracted |

#### Publication Workflow

```
┌─────────────────┐
│  Draft Created  │
│  (Internal)     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   CI Validation │
│   (Automated)   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Stakeholder     │
│ Review          │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  CM Approval    │
│  (Governance)   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Baseline Tag   │
│  (BL-####)      │
└────────┬────────┘
         │
         ├───────────► Internal (Always)
         │
         ├───────────► Ops-Facing (if operational)
         │
         ├───────────► Authority Pack (if evidence/compliance)
         │
         └───────────► Supplier-Facing (if contractual/ICD)
```

#### Channel-Specific Gates

**Ops-Facing Gate**:
- OPS stakeholder approval ✅
- Operational impact assessment ✅
- Safety review (if safety-critical) ✅
- CM baseline approval ✅

**Authority Pack Gate**:
- Evidence completeness check ✅
- Traceability validation ✅
- CERT stakeholder approval ✅
- Digital signature generation ✅
- CM baseline approval ✅

**Supplier-Facing Gate**:
- Technical correctness (SE) ✅
- Contractual alignment (Procurement) ✅
- IP/ITAR review (Legal) ✅
- CM baseline approval ✅
- NDA confirmation ✅

---

## 5. Minimum Workflow (Getting Started)

### For Stakeholders

1. **Navigate to Your Entry Point**
   - Go to `STK_<YOUR-ID>/`
   - Open `00_00_IDX_LC01_SPACET_stakeholder-<id>-entrypoint_v01.md`

2. **Select Active Knot**
   - Review your assigned knots
   - Choose the knot with highest priority or active work

3. **Open ATA Tasklist**
   - Navigate to `KNOTS/K##_<title>/ATA_TASKS/ATA_##/`
   - Open the ATA-specific tasklist IDX

4. **Execute by Partitions**
   - Work through: IDs → Schema → Exports → CI → Evidence → Decisions → Adoption
   - Update progress in tasklist

5. **Submit for Approval**
   - Create evidence links
   - Route governance-impacting changes to CM
   - Update NKU ledgers

### For Program Management

1. **Monitor Knot Progress**
   - Review [`00_00_TAB_LC01_SPACET_knot-register_v01.csv`](00_AMPEL360_SPACET_PLUS_00_TAB_LC01_K00_DATA__knot-register_v01.csv)
   - Track NKU reduction across knots

2. **Prioritize Backlog**
   - Identify blocking knots
   - Allocate resources to high-priority uncertainties

3. **Coordinate Cross-Stakeholder Work**
   - Facilitate decision-making for shared knots
   - Resolve resource conflicts

### For Configuration Management

1. **Enforce Governance**
   - Review all PR submissions for nomenclature compliance
   - Validate trace integrity and schema coupling

2. **Approve Baselines**
   - Review evidence packs
   - Tag approved baselines (BL-####)

3. **Manage Publications**
   - Route artifacts to appropriate channels
   - Maintain access control and distribution records

---

## 6. Key Concepts

### NKU (Net Knowledge Unit / Next Knowledge Aggregation)

A metric tracking knowledge aggregation and uncertainty resolution in the program. Each knot has NKU credit assigned; closure requires:
- **Evidence links** (reproducible, stable targets)
- **Decision record** (minutes + approvals)
- **Baseline update** (CM-approved incorporation)

### TEKNIA Sharing

A knowledge increment packaging format for publishable artifacts. Requirements:
- knot_id, ata, partitions_closed
- referenced schema/registry/trace IDs
- evidence links + decision reference
- dedup proof (hash + namespace checks)
- NV and sharing classification

### Evidence Chain

The complete path from requirement through design, implementation, to verification. Managed by ATA 93 (Traceability) with:
- **Forward trace**: REQ → DESIGN → IMPLEMENTATION → TEST
- **Backward trace**: TEST → IMPLEMENTATION → DESIGN → REQ
- **Bidirectional validation**: All links current and non-stale

### Baseline

A frozen configuration of artifacts approved by CM. Baselines are:
- **Immutable** — Once tagged, contents do not change
- **Versioned** — Sequential baseline IDs (BL-0001, BL-0002, ...)
- **Traceable** — Complete manifest with checksums
- **Approved** — CM WG sign-off required

---

## 7. Compliance and Standards

### Applicable Standards

| Domain | Standards |
|:-------|:----------|
| Configuration | ANSI/EIA-649B, MIL-HDBK-61A |
| Quality | AS9100D, ISO 9001:2015 |
| Safety | SAE ARP4754A, ARP4761, MIL-STD-882E |
| Software | DO-178C, DO-330 |
| Hardware | DO-254 |
| AI/ML | EASA AI Roadmap, DO-178C/ML Supplement |
| Publications | S1000D, ATA iSpec 2200 |
| Space Ops | ECSS-E-ST-40C, NASA-STD-3001 |
| Systems Engineering | ECSS-E-ST-10C, ISO/IEC 15288 |

### Nomenclature Compliance

All artifacts in the portal **MUST** follow the Nomenclature Standard v1.0:

```
[ROOT]_[BUCKET]_[TYPE]_[VARIANT]_[DESCRIPTION]_[VERSION].[EXT]
```

**Validation**: `python validate_nomenclature.py <filename>`

📖 **Full Standard**: [`00_00_STD_LC01_SPACET_nomenclature-standard_v02.md`](../00_AMPEL360_SPACET_PLUS_00_STD_LC01_K00_CM__nomenclature-standard_v02.md)

### CI/CD Enforcement

GitHub Actions automatically validate:
- ✅ Nomenclature compliance
- ✅ Schema validation (JSON/YAML against registered schemas)
- ✅ Trace link integrity
- ✅ Duplicate detection
- ✅ Type detection (new TYPE codes trigger review)

📋 **CI Gates**: [`00_00_IDX_LC01_SPACET_ci-governance-gates_v01.md`](../00_AMPEL360_SPACET_PLUS_00_IDX_LC01_K00_DATA__ci-governance-gates_v01.md)

---

## 8. Support and Contact

### Stakeholder Leads

Contact your stakeholder lead for workspace-specific questions. See individual entry points for current lead assignments.

### Configuration Management

For governance questions, baseline approvals, and publication requests:
- **CM WG** — Configuration Management Working Group
- **Contact**: Via repository issues tagged with `governance` label

### Technical Support

For repository structure, CI/CD, or tooling issues:
- **Repository Issues**: Create issue with appropriate labels
- **Documentation**: See root [`README.md`](../README.md)

---

## 9. Quick Reference

### Essential Links

| Resource | Link |
|:---------|:-----|
| Master Stakeholder Index | [`00_00_IDX_LC01_SPACET_stakeholder-entrypoints_v01.md`](00_AMPEL360_SPACET_PLUS_00_IDX_LC01_K00_CM__stakeholder-entrypoints_v01.md) |
| Knot Register | [`00_00_TAB_LC01_SPACET_knot-register_v01.csv`](00_AMPEL360_SPACET_PLUS_00_TAB_LC01_K00_DATA__knot-register_v01.csv) |
| Nomenclature Standard | [`../00_00_STD_LC01_SPACET_nomenclature-standard_v02.md`](../00_AMPEL360_SPACET_PLUS_00_STD_LC01_K00_CM__nomenclature-standard_v02.md) |
| Governance Policy | [`../00_00_STD_LC01_SPACET_governance-reference-policy_v01.md`](../00_AMPEL360_SPACET_PLUS_00_STD_LC01_K00_DATA__governance-reference-policy_v01.md) |
| CI Gates | [`../00_00_IDX_LC01_SPACET_ci-governance-gates_v01.md`](../00_AMPEL360_SPACET_PLUS_00_IDX_LC01_K00_DATA__ci-governance-gates_v01.md) |
| Main Repository README | [`../README.md`](../README.md) |

### Command Reference

```bash
# Validate file naming
python validate_nomenclature.py <filename>

# Check all files in repository
python validate_nomenclature.py --check-all

# Create new artifact from template
python scripts/scaffold.py <ROOT> <BUCKET> <TYPE> <VARIANT> <DESC> <VER>

# Detect new TYPE codes
python scripts/detect_new_types.py --auto-suggest
```

---

## 10. Version History

| Version | Date | Changes | Author |
|:--------|:-----|:--------|:-------|
| 1.0 | 2025-12-15 | Initial PORTAL README creation | GitHub Copilot Agent |

---

**AMPEL360-SPACE-T-PORTAL** — Single Source of Truth for Space-T Program Collaboration

*Maintained by Configuration Management WG*
