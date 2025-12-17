---
title: "Stakeholder Entry Point: AI/ML Engineering (AI)"
type: IDX
variant: "SPACET"
status: Draft
stakeholder_id: "AI"
bucket: "00"
lc_or_subbucket: "LC01"
description: "Primary entry point for AI/ML Engineering in AMPEL360 Space-T. Navigate knots, ATA partitions, NKU control, and TEKNIA sharing gates."
owner: "STK_AI Lead"
---

# Stakeholder Entry Point — AI/ML Engineering (AI)

This page is the **stakeholder-centric entry point** for the AI/ML Engineering lane within **AMPEL360-SPACE-T-PORTAL/**.  
Work is organized by **Backlog Knots** (partitioned uncertainty knots). Each knot is resolved through **ATA-partitioned tasklists** and credited via **NKU progress**.

---

## 1) Scope

AI/ML Engineering (STK_AI) owns and/or contributes to:
- ML lifecycle governance (datasets, models, evaluation, drift monitoring)
- Schema alignment for AI-related data (canonical models, feature schemas, telemetry schemas)
- Traceability instrumentation for evidence (training, evaluation, verification, and deployment)
- TEKNIA packaging gates for shareable knowledge and certifiable hybrid artifacts
- Automation (CI checks, validators, scaffolding, and agent instruction enforcement)

---

## 2) Navigation Rules

- **KNOTS/** is the top-level backlog structure (one folder per knot).
- Each knot contains:
  - **one overview index** (IDX) describing scope and closure criteria,
  - **ATA_TASKS/** with one ATA-specific IDX per impacted ATA,
  - evidence/decisions/exports subtrees (as defined by the ATA tasklist index structure).
- Closure requires **Decision + Evidence** and a baseline/trace update routed through **CM**.

---

## 3) Active Backlog Knots (GitHub-navigable)

### K06 — Data Governance (SSOT / Schemas / Identifiers)
- Knot folder: [K06_data-governance-ssot-schemas-identifiers/](KNOTS/K06_data-governance-ssot-schemas-identifiers/)  
  _Comment:_ Program-wide SSOT, schema governance, identifier discipline, trace semantics, DPP/BOM export integrity.

- Master index: [K06 master index](KNOTS/K06_data-governance-ssot-schemas-identifiers/00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_LC01_K06_AI__k06-data-governance-ssot-schemas-identifiers_IDX_I01-R01_ACTIVE.md)  
  _Comment:_ Authoritative K06 navigation hub across impacted ATAs with closure criteria and NKU controls.

- ATA partitions (high-priority subset):
  - [ATA 91 — Schemas & Canonical Models](KNOTS/K06_data-governance-ssot-schemas-identifiers/ATA_TASKS/ATA_91/91_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_LC01_K06_AI__k06-ata-91-tasklist_IDX_I01-R01_ACTIVE.md)  
    _Comment:_ Schema registry, versioning, compatibility, canonical primitives.
  - [ATA 93 — Traceability Graph & Evidence Links](KNOTS/K06_data-governance-ssot-schemas-identifiers/ATA_TASKS/ATA_93/93_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_LC01_K06_AI__k06-ata-93-tasklist_IDX_I01-R01_ACTIVE.md)  
    _Comment:_ Node/edge semantics, evidence freshness, audit-ready snapshots.
  - [ATA 94 — DPP](KNOTS/K06_data-governance-ssot-schemas-identifiers/ATA_TASKS/ATA_94/94_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_LC01_K06_AI__k06-ata-94-tasklist_IDX_I01-R01_ACTIVE.md)  
    _Comment:_ Export packs, provenance, signing coupling, redaction rules.
  - [ATA 95 — SBOM / ModelBOM](KNOTS/K06_data-governance-ssot-schemas-identifiers/ATA_TASKS/ATA_95/95_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_LC01_K06_AI__k06-ata-95-tasklist_IDX_I01-R01_ACTIVE.md)  
    _Comment:_ Software/ML supply chain identity, policy gates, trace alignment.
  - [ATA 99 — Master Registers](KNOTS/K06_data-governance-ssot-schemas-identifiers/ATA_TASKS/ATA_99/99_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_LC01_K06_AI__k06-ata-99-tasklist_IDX_I01-R01_ACTIVE.md)  
    _Comment:_ Namespace boundaries, dedup governance, drift monitoring.

---

### K07 — AI Autonomy Assurance & Monitoring
- Knot folder: [K07_ai-autonomy-assurance-monitoring/](KNOTS/K07_ai-autonomy-assurance-monitoring/)  
  _Comment:_ Assurance cases, runtime monitoring, autonomy constraints, safe operation envelopes (structure to be populated).
- Entry index (to create/confirm): [K07 index](KNOTS/K07_ai-autonomy-assurance-monitoring/00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_LC01_K07_AI__k07-ai-autonomy-assurance-monitoring_IDX_I01-R01_ACTIVE.md)  
  _Comment:_ Defines the uncertainty, closure criteria, and ATA partitions.

---

### K13 — Cybersecurity Zones & Key Management
- Knot folder: [K13_cybersecurity-zones-key-management/](KNOTS/K13_cybersecurity-zones-key-management/)  
  _Comment:_ Key management, zone boundaries, cryptographic identity, and CI enforcement coupling with SBOM/DPP.
- Entry index (to create/confirm): [K13 index](KNOTS/K13_cybersecurity-zones-key-management/00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_LC01_K13_AI__k13-cybersecurity-zones-key-management_IDX_I01-R01_ACTIVE.md)  
  _Comment:_ Defines the uncertainty, closure criteria, and ATA partitions.

---

## 4) Operating Model (Decision + Evidence + Baseline)

### 4.1 Partitioned Uncertainty Resolution (NKU)
- NKU credit is granted only when a partition is closed with:
  - **Evidence links** (reproducible, stable targets; staleness controlled), and
  - **Decision record** (minutes + approvals when required).
- Each knot/ATA tasklist includes a **Control & Monitoring** section describing NKU scoring and thresholds.

### 4.2 TEKNIA Sharing Gate (for publishable increments)
A TEKTOK or shareable knowledge increment must include:
- knot_id, ata, partitions_closed
- referenced schema IDs / registry IDs / trace snapshot IDs
- evidence links + decision reference
- dedup proof (hash + namespace checks)
- NV and sharing classification (internal/external)

### 4.3 Coordination Interfaces
- **CM (Configuration Management):** approves baseline changes, nomenclature compliance, and closure discipline.
- **DATA (Data Governance):** owns SSOT boundaries and stewardship assignments.
- **CY (Cybersecurity):** owns key management, threat-driven constraints, and security evidence packaging.
- **TEST (IVVQ):** owns test evidence nodes, qualification pathways, and trace-verified evidence chains.

---

## 5) Execution Checklist (minimum)

1. Choose the target knot (K06/K07/K13).
2. Open the knot **master index** and select the impacted ATA tasklist.
3. Execute tasks by partitions (IDs/Schema/Exports/CI/Evidence/Decisions/Adoption).
4. Update NKU ledgers and evidence links.
5. Route governance-impacting changes through CM for approval and baseline tagging.

---
