---
title: "K01 Authority Pack Example — Contents List"
type: LST
project: "AMPEL360"
program: "SPACET"
variant: "PLUS"
status: "EXAMPLE"
knot_id: "K01"
lc_or_subbucket: "SB90"
bucket: "90"
exemplar: "authority-pack"
pack_id: "K01-AUTH-PACK-EXAMPLE-001"
version: "v01"
atas_covered: ["00", "21", "22"]
generated: "2025-12-15"
---

# K01 Authority Pack Example — Contents List

## Links (GitHub-navigable)
- Exemplar index: **[00_90_IDX_SB90_AMPEL360_SPACET_PLUS_k01-authority-pack-example-index_I01-R01.md](./00_AMPEL360_SPACET_PLUS_90_IDX_SB90_K01_CERT__k01-authority-pack-example-index_I01-R01.md)**
- K01 Assets index: **[00_00_IDX_LC01_AMPEL360_SPACET_PLUS_k01-assets-index_I01-R01.md](../../00_00_IDX_LC01_AMPEL360_SPACET_PLUS_k01-assets-index_I01-R01.md)**
- K01 Evidence Pack Manifest schema: **[00_00_SCH_LC01_AMPEL360_SPACET_PLUS_k01-evidence-pack-manifest_I01-R01.json](../../SCHEMAS/00_00_SCH_LC01_AMPEL360_SPACET_PLUS_k01-evidence-pack-manifest_I01-R01.json)**

## Package Information
- **Pack ID**: `K01-AUTH-PACK-EXAMPLE-001`
- **Pack Version**: `v01`
- **Status**: Example (non-authoritative)
- **ATAs Covered**: ATA 00, ATA 21, ATA 22
- **Submission intent**: Demonstration of K01 packaging (structure + trace), not a formal submission

---

## Evidence Items (Linked Inventory)

> Convention: every “File” entry is a **clickable GitHub link**.  
> If you later relocate files, update only the link targets (do not remove the item row).

| # | Evidence ID | Type | ATA | File (GitHub link) | Status | Comment |
|---:|---|---|---|---|---|---|
| 1 | `CERT-BASIS-001` | `STD` | 00 | **[00_00_STD_LC01_AMPEL360_SPACET_PLUS_k01-ata-00-certification-basis_I01-R01.md](../../ATA_TASKS/ATA_00_GENERAL/EVIDENCE/00_00_STD_LC01_AMPEL360_SPACET_PLUS_k01-ata-00-certification-basis_I01-R01.md)** | Complete | Program-level basis and tailoring statement for K01. |
| 2 | `COMPLIANCE-MATRIX-001` | `TRC` | 00 | **[00_00_TRC_LC01_AMPEL360_SPACET_PLUS_k01-ata-00-compliance-matrix_I01-R01.md](../../ATA_TASKS/ATA_00_GENERAL/EVIDENCE/00_00_TRC_LC01_AMPEL360_SPACET_PLUS_k01-ata-00-compliance-matrix_I01-R01.md)** | Complete | MoC mapping and verification ownership references. |
| 3 | `ATA21-SCOPE-IF-001` | `REQ` | 21 | **[21_00_REQ_LC01_AMPEL360_SPACET_PLUS_k01-ata-21-scope-interfaces_I01-R01.md](../../ATA_TASKS/ATA_21_AIR-CONDITIONING-ENVIRONMENTAL-CONTROL/REQ/21_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_LC01_K01_CERT__k01-ata-21-scope-interfaces_I01-R01.md)** | Draft | ATA 21 scope boundary + interface obligations under K01. |
| 4 | `ATA22-SCOPE-IF-001` | `REQ` | 22 | **[22_00_REQ_LC01_AMPEL360_SPACET_PLUS_k01-ata-22-scope-interfaces_I01-R01.md](../../ATA_TASKS/ATA_22_AUTO-FLIGHT-GNC/REQ/22_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_LC01_K01_CERT__k01-ata-22-scope-interfaces_I01-R01.md)** | Draft | ATA 22 scope boundary + certification-critical interfaces. |

### Mandatory pack files (in this exemplar folder)
| Item | File (GitHub link) | Comment |
|---|---|---|
| Manifest example | **[00_90_SCH_SB90_AMPEL360_SPACET_PLUS_k01-authority-pack-manifest-example_I01-R01.json](./00_90_SCH_SB90_AMPEL360_SPACET_PLUS_k01-authority-pack-manifest-example_I01-R01.json)** | Machine-readable list of included items (and hashes if used). |
| Evidence links example | **[00_90_TRC_SB90_AMPEL360_SPACET_PLUS_k01-authority-pack-evidence-links-example_I01-R01.md](./00_90_TRC_SB90_AMPEL360_SPACET_PLUS_k01-authority-pack-evidence-links-example_I01-R01.md)** | Single “click-through” page to all evidence sources. |
| Decision context example | **[00_90_STD_SB90_AMPEL360_SPACET_PLUS_k01-authority-pack-decision-context-example_I01-R01.md](./00_90_STD_SB90_AMPEL360_SPACET_PLUS_k01-authority-pack-decision-context-example_I01-R01.md)** | What was decided + who approved + constraints. |
| Audit query example | **[00_90_IDX_SB90_AMPEL360_SPACET_PLUS_k01-authority-pack-audit-query-example_I01-R01.md](./00_90_IDX_SB90_AMPEL360_SPACET_PLUS_k01-authority-pack-audit-query-example_I01-R01.md)** | Reproducible audit path for reviewers. |

---

## Submission Notes
This example pack demonstrates the **minimum viable content** for a K01 authority submission:
- certification basis + tailoring posture,
- compliance/MoC mapping,
- ATA scope and interface declarations (per affected ATA),
- deterministic inventory and reproducible trace path.

Actual submission packs must:
- extend coverage to all affected ATAs,
- include or reference signed release packs where required,
- ensure CERT + CM approvals are recorded and linked.

