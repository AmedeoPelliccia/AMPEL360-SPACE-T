---
title: "Stakeholder Entry Point: Configuration Management (CM)"
type: IDX
variant: "SPACET"
status: Draft
stakeholder_id: "CM"
---

# Stakeholder Entry Point — Configuration Management (CM)

## Scope
This directory is the stakeholder-centric entry point. Work is organized by **Backlog Knots** (uncertainty knots).

## Active Backlog Knots

- **K01** — certification-authority-basis → `K01_certification-authority-basis/`
- **K04** — integration-boundaries-and-icds → `K04_integration-boundaries-and-icds/`
- **K06** — data-governance-ssot-schemas-identifiers → `K06_data-governance-ssot-schemas-identifiers/`
- **K08** — dpp-sbom-provenance-scope → `K08_dpp-sbom-provenance-scope/`
- **K10** — industrialization-supplychain-quality → `K10_industrialization-supplychain-quality/`

## Operating Model
- Each Knot has an **overview**, **ATA impact breakdown**, and **tasks** to close uncertainties.
- Tasks close with **Decision + Evidence**, then a baseline update (CM).

## Key References

### Master Tables and Relations

- **ATA Master Relations Table (YAML):** `../../config/database/ata_master_relations_table.yaml`
  - Complete structured data for all 117 ATA chapters
  - Domain mappings, AoR assignments, STK dependencies
  - Knot applicability and agency/context mappings

- **ATA Master Relations Catalog:** `../../00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_B30_LC01_K06_CM__ata-master-relations-table_CAT_I01-R01_ACTIVE.md`
  - Comprehensive documentation and usage guidelines
  - Indexes by AoR, domain, knot, and stakeholder

- **ATA Master Relations Quick Reference:** `../../00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_B30_LC01_K06_CM__ata-master-relations-quick-ref_TAB_I01-R01_ACTIVE.md`
  - Tabular format matching original specification
  - Quick lookup for ATA relations and interfaces

### Configuration Management Resources

- **ATA Partition Matrix:** `../../config/nomenclature/ATA_PARTITION_MATRIX.yaml`
- **Stakeholder Knot Config:** `../../scripts/stakeholder_knot_config.json`
- **Nomenclature Standard v6.0:** `../../docs/standards/NOMENCLATURE_v6_0_R1_0.md`
