---
title: "Stakeholder Entry Point: Physical Hardware & Mechanical Engineering (PHM)"
type: IDX
project: "AMPEL360"
program: "SPACET"
family: "Q10"
variant: "GEN"
version: "PLUS"
model: "BB"
block: "GEN"
phase: "LC01"
knot_task: "K04"
aor: "PHM"
status: Active
date: "2025-12-18"
owner: "Physical Hardware & Mechanical Engineering"
---

# Stakeholder Entry Point — Physical Hardware & Mechanical Engineering (PHM)

## Scope

This directory is the stakeholder-centric entry point for **Physical Hardware & Mechanical Engineering (PHM)**. 

PHM is responsible for all physical hardware domains including:
- **Aerostructures** — Fuselage, wings, stabilizers, doors, hatches, nacelles, pylons
- **Landing gear** — Gear systems, brakes, steering, deployment mechanisms
- **Pneumatics** — Gas distribution, valves, sensors, alarms
- **Flight and attitude control** — Actuation, servos, control surfaces
- **Hydraulics** — Generation, distribution, health monitoring
- **Materials** — Material specifications, structural practices, allowables

Work is organized by **Backlog Knots** (uncertainty knots).

## Active Backlog Knots

- **K01** — certification-authority-basis → `KNOTS/K01_certification-authority-basis/`
- **K03** — hazmat-cryo-propellants-safety-case → `KNOTS/K03_hazmat-cryo-propellants-safety-case/`
- **K05** — model-fidelity-verification-credit → `KNOTS/K05_model-fidelity-verification-credit/`
- **K10** — industrialization-supplychain-quality → `KNOTS/K10_industrialization-supplychain-quality/`
- **K11** — human-factors-training-readiness → `KNOTS/K11_human-factors-training-readiness/`

## Operating Model

- Each Knot has an **overview**, **ATA impact breakdown**, and **tasks** to close uncertainties.
- Tasks close with **Decision + Evidence**, then a baseline update (CM).

## ATA Chapters Owned by PHM

PHM is the primary Area of Responsibility (AoR) for the following ATA chapters:

| ATA | Description | Domain |
| :--- | :--- | :--- |
| 06 | DIMENSIONS AND AREAS | T-TECHNOLOGY |
| 08 | LEVELING AND WEIGHING | T-TECHNOLOGY |
| 20 | STANDARD PRACTICES - AIRFRAME | T-TECHNOLOGY |
| 21 | AIR CONDITIONING / ENVIRONMENTAL CONTROL | T-TECHNOLOGY |
| 24 | ELECTRICAL POWER | T-TECHNOLOGY |
| 25 | EQUIPMENT / FURNISHINGS | T-TECHNOLOGY |
| 27 | FLIGHT CONTROLS | T-TECHNOLOGY |
| 28 | FUEL / PROPELLANT SYSTEMS | T-TECHNOLOGY |
| 29 | HYDRAULIC POWER | T-TECHNOLOGY |
| 30 | ICE AND RAIN PROTECTION | T-TECHNOLOGY |
| 32 | LANDING GEAR | T-TECHNOLOGY |
| 35 | OXYGEN / LIFE SUPPORT GAS | T-TECHNOLOGY |
| 36 | PNEUMATIC / GAS DISTRIBUTION | T-TECHNOLOGY |
| 37 | VACUUM (IF APPLICABLE) | T-TECHNOLOGY |
| 38 | WATER / WASTE (LIFE SUPPORT) | T-TECHNOLOGY |
| 39 | ELECTRICAL / ELECTRONIC PANELS | T-TECHNOLOGY |
| 41 | WATER BALLAST / MASS TRIM | T-TECHNOLOGY |
| 49 | AIRBORNE AUXILIARY POWER | T-TECHNOLOGY |
| 50 | CARGO AND ACCESSORY COMPARTMENTS | T-TECHNOLOGY |
| 51 | STANDARD PRACTICES & STRUCTURES | T-TECHNOLOGY |
| 52 | DOORS / HATCHES | T-TECHNOLOGY |
| 53 | FUSELAGE / PRESSURE VESSEL | T-TECHNOLOGY |
| 54 | NACELLES / PYLONS | T-TECHNOLOGY |
| 55 | STABILIZERS / CONTROL SURFACES | T-TECHNOLOGY |
| 56 | WINDOWS / VIEWPORTS | T-TECHNOLOGY |
| 57 | WINGS / LIFTING SURFACES | T-TECHNOLOGY |
| 60-67 | PROPELLER / ROTOR SYSTEMS | T-TECHNOLOGY |
| 70-79 | ENGINE / PROPULSION SYSTEMS | T-TECHNOLOGY |

## Cross-Dependencies

PHM collaborates with the following stakeholders:
- **SE** — Systems Engineering (architecture, ICDs, integration)
- **SAF** — Safety (hazard analysis, safety cases)
- **CERT** — Certification (compliance evidence)
- **TEST** — Testing (verification, qualification)
- **MRO** — Maintenance (servicing, inspection)
- **DAB** — Digital Applications (control software, health monitoring)

## Related Documents

- **Nomenclature Standard:** `docs/standards/NOMENCLATURE_v6_0_R1_0.md`
- **ATA Master Relations:** `config/database/ata_master_relations_table.yaml`
- **Stakeholder Entrypoints Index:** `AMPEL360-SPACE-T-PORTAL/00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_LC01_K04_CM__stakeholder-entrypoints_IDX_I01-R01_ACTIVE.md`

---

**Document Control:**
- **Status:** Active
- **Created:** 2025-12-18
- **Owner:** Physical Hardware & Mechanical Engineering
