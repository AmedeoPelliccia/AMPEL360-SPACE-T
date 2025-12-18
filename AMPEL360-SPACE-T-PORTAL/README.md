# AMPEL360-SPACE-T — Spacecraft CAXS Portal (CA360º)

**AMPEL360 Spacecraft CAXS (CA360º)** is a **Computer-Aided Cross Sustainment** platform: **product-grade spacecraft deliverable automation** with configuration control, cross-ATA traceability, and compliance evidence across the **sustainable-lifecycle agentic process (XS)**.

This portal is the **first concrete manifestation of the CAOS pillar**: it operationalizes **KNOT governance (K01–K14)** for indeterminacy control and enables **predictive development** via **NKU pathways** for agentic task execution.

---

## Release Status

**Status:** R1.0 LOCK (No major breaking changes planned)  
**Nomenclature:** v6.0 R1.0 (FINAL LOCK)  
**Governance:** CM change control for all allowlists and exceptions

> Note: Nomenclature compliance and link integrity are validated via separate CI gates.  
> Nomenclature can be 0-violation while link remediation is handled as a controlled follow-up.

---

## What This Portal Is

The CAXS Portal (CA360º) provides **a navigable, enforceable and automatable entry layer** for:

- **AoR entry points** (CM/CERT/SAF/SE/OPS/DATA/AI/CY/TEST/MRO/SPACEPORT/PMO/…)
- **Cross-ATA sustainment traceability** (Spacecraft adaptation)
- **KNOT execution lanes** (K01..K14, optional `-T###`)
- **NKU pathways** (task-to-evidence chains for agentic workflows)
- **CAOS integration surfaces** (automation, predictive pipelines, evidence packaging)

---

## OPT-INS Framework (OPT-IN + S Axis)

This repository implements **OPT-INS** (extended OPT-IN) to support spacecraft-scale sustainment and test:

- **O — Organization**
- **P — Program**
- **T — Technology (Onboard systems)**
- **I — Infrastructures (Ground / launch / mission control)**
- **N — Neural / Data / DPP / Traceability**
- **S — SIM/TEST (new axis)**

### S Axis (SIM/TEST) — ATA 100..114 (OPT-INS reserved range)

For spacecraft adaptation, **ATA 100–114 are reserved for the S axis** (simulation, test, verification, qualification, and validation), and are treated as **first-class OPT-INS chapters** integrated into the same portal patterns (indexes, knots, AoR entry points, evidence packaging).

> The exact ATA_100..ATA_114 chapter naming is **CM-controlled**. The range is immutable; names may evolve additively under change control without changing the reserved numeric allocation.

Recommended initial mapping (CM-controlled):
- **ATA 100** — Simulation Baselines (SIM)
- **ATA 101** — Digital Twin Configurations (DT)
- **ATA 102** — Model-Based Test Design (MBT)
- **ATA 103** — SIL Environments (SIL)
- **ATA 104** — HIL Benches (HIL)
- **ATA 105** — Qualification & Acceptance (QUAL)
- **ATA 106** — Integration Test Campaigns (ITC)
- **ATA 107** — Environmental Test (ENV)
- **ATA 108** — Flight / Mission Test (FLTTEST)
- **ATA 109** — Ops Readiness Tests (ORT)
- **ATA 110** — Safety Validation (SAFVAL)
- **ATA 111** — Certification Evidence Packs (EVD)
- **ATA 112** — Ground Test & Checkout (GTC)
- **ATA 113** — Range / Corridor / Constraints (RANGE)
- **ATA 114** — Post-Test Analytics (PTA)

---

## Portal Navigation

### 1) Entry by AoR (Portal Entry Points)
Use AoR codes as your primary navigation key (governance-first):
- **CM** configuration management and baselines
- **CERT** certification, compliance mapping, evidence
- **SAF** hazard analysis, safety cases, risk controls
- **SE** systems engineering, architecture, SysML, ICDs, governance
- **OPS** operations, procedures, sustainment planning
- **DAB** digital applications and blockchains, data networks, control software
- **AI** AI/ML engineering, model governance
- **CY** cybersecurity
- **PHM** physical hardware & mechanical engineering (aerostructures, landing gear, pneumatics, flight control, hydraulics, materials)
- **TEST** verification, validation, simulation and test campaigns
- **MRO / SPACEPORT / PMO** sustainment operations, ground/launch sites, programme governance

### 2) Entry by KNOT (Execution Governance)
KNOTs define cross-cutting governance and execution sequences (K01..K14 only).  
Optional task suffix: `K##-T###` (e.g., `K06-T001`).

### 3) Entry by ATA Chapter (Spacecraft adaptation)
ATA chapters are used to structure technical and sustainment content consistently across OPT-INS.

---

## Nomenclature (v6.0 R1.0 FINAL LOCK)

All portal artifacts MUST follow the canonical filename format:

`[ATA_ROOT]_[PROJECT]_[PROGRAM]_[FAMILY]_[VARIANT]_[VERSION]_[MODEL]_[BLOCK]_[PHASE]_[KNOT_TASK]_[AoR]__[SUBJECT]_[TYPE]_[ISSUE-REVISION]_[STATUS].[EXT]`

### Spacecraft program constants
- `PROJECT = AMPEL360`
- `PROGRAM = SPACET`

### v6.0 tokens (normative)
- `FAMILY`: pax payload family (e.g., `Q10`, `Q100`, …; CM allowlist)
- `VARIANT`: governance lane (GEN/BASELINE/FLIGHTTEST/CERT/MSN/HOV/CUST; CM allowlist)
- `VERSION`: branding reinforcer with optional 2-digit iteration  
  `PLUS`, `PLUS01`..`PLUS99`, `PLUSULTRA`, `PLUSULTRA01`..`PLUSULTRA99` (CM allowlist roots)
- `MODEL`: domain classifier (`BB`, `HW`, `SW`, `PR`; CM allowlist)

### Conditional SUBJECT prefixes (normative)
To avoid adding tokens while preserving uniqueness:
- If `VARIANT=CUST` → `SUBJECT` MUST start with `cust-<custcode>-`
- If `VARIANT=MSN` → `SUBJECT` MUST start with `msn-<serial>-`

---

## CAOS Pillar Enablement (How this becomes "Computer-Aided")

### KNOTs (indeterminacy control)
KNOTs provide a controlled mechanism to handle uncertainty and evolving requirements while keeping the repository auditable and navigable.

### NKU Pathways (agentic task execution)
Every artifact is an NKU implicitly; the portal structures NKUs into **pathways**:
- task intent → inputs → transformations → outputs → verification → evidence
- predictable "what changed, why, and which evidence supports it" chains
- CI-enforceable, PR-reviewable, CM-governed

### Cross-Sustainment (XS)
"XS" is the portal's operative lens: cross-domain sustainment across vehicle, ground, mission control, software, data, and test.

---

## Quick Start (Portal Usage)

1. Start from an **AoR entry point** (e.g., CM/CERT/TEST).
2. Use the **KNOT index** to identify the governance sequence.
3. Navigate to the relevant **ATA chapter** (including SIM/TEST chapters 100–114 when applicable).
4. Create new artifacts using the scaffold tooling (v6.0) and validate before commit.
5. Attach evidence outputs (validator, link-check, exception diffs) in PR^3 templates.

---

## Topics

spacecraft aerospace configuration-management certification traceability do-178c systems-engineering safety-critical evidence ecss compliance-automation digital-product-passport amedeo-pelliccia-methodology caxs ca360 arp4754a nomenclature-automation sustainable-lifecycle circular-systems
