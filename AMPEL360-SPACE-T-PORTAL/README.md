# AMPEL360 SPACE-T Portal

## Overview

The **AMPEL360-SPACE-T-PORTAL** is a stakeholder-centric navigation hub that organizes work by uncertainty "knots" (critical decision points) rather than by traditional technical hierarchies. This portal complements the main engineering tree (`AMPEL360_SPACE-T/`) by providing entry points tailored to each stakeholder's role and responsibilities.

## Structure

```
AMPEL360-SPACE-T-PORTAL/
├── 00_00_IDX_LC01_SPACET_stakeholder-entrypoints_v01.md  # Global index
├── 00_00_TAB_LC01_SPACET_knot-register_v01.csv          # Knot registry
└── STK_{ID}-{name}/                                      # Stakeholder directories
    ├── 00_00_IDX_LC01_SPACET_stakeholder-{id}-entrypoint_v01.md
    └── KNOTS/
        └── {KID}_{knot-title}/
            ├── 00_00_IDX_LC01_SPACET_{kid}-{title}_v01.md
            └── ATA_TASKS/
                └── ATA_{XX}/
                    ├── 00_00_IDX_LC01_SPACET_{kid}-ata-{xx}-tasklist_v01.md
                    └── 00_00_ACT_LC06_SPACET_{kid}-{tid}-{task-title}_v01.md  (with --full)
```

## Stakeholders

The portal is organized around 12 key stakeholders:

- **CM** — Configuration Management
- **PMO** — Program Management Office
- **SE** — Systems Engineering
- **SAF** — Safety
- **CERT** — Certification & Authorities
- **OPS** — Operations
- **SPACEPORT** — Spaceport/Airport Ops
- **MRO** — MRO / Maintenance
- **DATA** — Data Governance
- **AI** — AI/ML Engineering
- **CY** — Cybersecurity
- **TEST** — IVVQ / Testing

Each stakeholder has a dedicated entry point that lists their active backlog knots.

## Backlog Knots (K01-K14)

Knots represent critical uncertainty points that require decisions to unblock progress:

- **K01** — certification-authority-basis
- **K02** — conops-mission-phases
- **K03** — hazmat-cryo-propellants-safety-case
- **K04** — integration-boundaries-and-icds
- **K05** — model-fidelity-verification-credit
- **K06** — data-governance-ssot-schemas-identifiers
- **K07** — ai-autonomy-assurance-monitoring
- **K08** — dpp-sbom-provenance-scope
- **K09** — infrastructure-permitting-jurisdiction
- **K10** — industrialization-supplychain-quality
- **K11** — human-factors-training-readiness
- **K12** — nvh-metrics-corridors-exposure
- **K13** — cybersecurity-zones-key-management
- **K14** — reliability-growth-maintenance-intervals-health

Each knot:
- Has a clear problem statement and decision criteria
- Impacts multiple ATA chapters
- Contains ATA-specific tasklists
- Links to the relevant paths in the main engineering tree

## Relationship to Engineering Tree

The portal is a **navigation layer** only. The actual engineering artifacts remain in:

```
AMPEL360_SPACE-T/
├── P-PROGRAM/           # Program management & requirements
├── O-OPS_ORG/          # Operations & organization
├── T-TECHNOLOGY/       # Onboard systems & technology
├── I-INFRASTRUCTURES/  # Ground infrastructure
├── N-NEURAL_NETWORKS/  # AI/ML systems
└── T-SIMTEST/          # Simulation & testing
```

Each task in the portal includes `affected_ata_paths` that point to the relevant directories in the engineering tree.

## Generation

The portal is generated using:

```bash
# Basic generation (tasklists only)
python scripts/generate_stakeholder_knot_structure.py

# Full generation (includes individual task ACT files)
python scripts/generate_stakeholder_knot_structure.py --full

# Dry-run (preview without creating files)
python scripts/generate_stakeholder_knot_structure.py --dry-run

# Force overwrite existing files
python scripts/generate_stakeholder_knot_structure.py --force
```

## Configuration

The portal structure is defined in `scripts/stakeholder_knot_config.json`:

- **stakeholders**: List of stakeholder IDs, names, and assigned knots
- **knots**: Knot definitions with affected ATAs and task templates
- **portal_path**: Output directory for the portal
- **variant**: Configuration baseline (default: SPACET)
- **root_code**, **bucket_code**, **version**: Nomenclature fields

## Nomenclature Compliance

All generated files follow the **Nomenclature Standard v2.0** (8-field format):

```
[ROOT]_[BUCKET]_[TYPE]_[LC_OR_SUBBUCKET]_[VARIANT]_[DESCRIPTION]_[VERSION].[EXT]
```

For BUCKET=00 (lifecycle artifacts), LC_OR_SUBBUCKET uses LC01-LC14.

Validation:
```bash
python validate_nomenclature.py --check-dir AMPEL360-SPACE-T-PORTAL
```

## Workflow

1. **Stakeholder** navigates to their entry point
2. **Selects** an active knot from their list
3. **Reviews** the knot overview and decision criteria
4. **Navigates** to affected ATA tasklists
5. **Executes** tasks and records decisions
6. **Updates** baseline via Configuration Management

## Maintenance

To update the portal:

1. Edit `scripts/stakeholder_knot_config.json`
2. Regenerate: `python scripts/generate_stakeholder_knot_structure.py --force`
3. Validate: `python validate_nomenclature.py --check-dir AMPEL360-SPACE-T-PORTAL`
4. Commit changes

## Design Principles

- **Stakeholder-centric**: Organized by role, not by technical discipline
- **Decision-focused**: Knots represent uncertainty that blocks progress
- **ATA-mapped**: Clear mapping to ATA chapters for traceability
- **Navigation layer**: Complements rather than replaces the engineering tree
- **Automated**: Generated from configuration for consistency
- **Standards-compliant**: Follows nomenclature v2.0 and OPT-IN framework
