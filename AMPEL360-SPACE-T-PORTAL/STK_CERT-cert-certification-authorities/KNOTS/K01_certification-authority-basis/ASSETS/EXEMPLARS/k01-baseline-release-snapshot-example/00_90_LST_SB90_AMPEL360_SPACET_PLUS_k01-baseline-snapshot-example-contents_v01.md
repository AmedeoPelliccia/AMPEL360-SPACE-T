---
title: "K01 Baseline Release Snapshot Example — Contents"
type: LST
project: "AMPEL360"
program: "SPACET"
variant: "PLUS"
status: "EXAMPLE"
knot_id: "K01"
bucket: "90"
lc_or_subbucket: "SB90"
exemplar: "baseline-release-snapshot"
snapshot_id: "K01-BASELINE-SNAPSHOT-EXAMPLE-001"
baseline_name: "Certification Basis Baseline v1.0"
date: "2025-12-15"
git_commit: "example_commit_hash"
---

# K01 Baseline Release Snapshot Example — Contents

## Links (GitHub-navigable)
- Snapshot index: **[00_90_IDX_SB90_AMPEL360_SPACET_PLUS_k01-baseline-snapshot-example-index_v01.md](./00_90_IDX_SB90_AMPEL360_SPACET_PLUS_k01-baseline-snapshot-example-index_v01.md)**
- Snapshot manifest (example): **[00_90_SCH_SB90_AMPEL360_SPACET_PLUS_k01-baseline-snapshot-manifest-example_v01.json](./00_90_SCH_SB90_AMPEL360_SPACET_PLUS_k01-baseline-snapshot-manifest-example_v01.json)**
- K01 Assets index: **[00_00_IDX_LC01_AMPEL360_SPACET_PLUS_k01-assets-index_v01.md](../../00_00_IDX_LC01_AMPEL360_SPACET_PLUS_k01-assets-index_v01.md)**

---

## Snapshot Information
- **Snapshot ID**: `K01-BASELINE-SNAPSHOT-EXAMPLE-001`
- **Baseline Name**: `Certification Basis Baseline v1.0`
- **Date**: `2025-12-15`
- **Git Commit**: `example_commit_hash`
- **Status**: Example (non-authoritative)

---

## Included Artifacts (Clickable Inventory)

> Rule: every entry must include a **GitHub-navigable link**.  
> If filenames change, update only the link target.

| # | Artifact ID | Type | File (GitHub link) | CM Status | Comment |
|---:|---|---|---|---|---|
| 1 | `K01-CERT-BASIS-PLAN` | `PLAN` | **[00_00_PLAN_LC01_AMPEL360_SPACET_PLUS_k01-certification-authority-basis-plan_v01.md](../../../../ATA_TASKS/ATA_00_GENERAL/EVIDENCE/00_00_PLAN_LC01_AMPEL360_SPACET_PLUS_k01-ata-00-certification-strategy_v01.md)** | Approved (Example) | Points to the program-level certification strategy/plan artefact used as the “plan anchor” for this snapshot. |
| 2 | `K01-ASSETS-INDEX` | `IDX` | **[00_00_IDX_LC01_AMPEL360_SPACET_PLUS_k01-assets-index_v01.md](../../00_00_IDX_LC01_AMPEL360_SPACET_PLUS_k01-assets-index_v01.md)** | Approved (Example) | Canonical inventory entry point for K01 assets. |
| 3 | `K01-AUTH-PACK-EXAMPLE` | `SCH` | **[00_90_SCH_SB90_AMPEL360_SPACET_PLUS_k01-authority-pack-example-manifest_v01.json](../k01-authority-pack-example/00_90_SCH_SB90_AMPEL360_SPACET_PLUS_k01-authority-pack-example-manifest_v01.json)** | Approved (Example) | Links the authority pack manifest used as the evidence bundle example. |
| 4 | `K01-COMPLIANCE-WORKFLOW` | `DIA` | **[00_90_DIA_SB90_AMPEL360_SPACET_PLUS_k01-compliance-workflow_v01.md](../../DIAGRAMS/00_90_DIA_SB90_AMPEL360_SPACET_PLUS_k01-compliance-workflow_v01.md)** | Approved (Example) | Reviewer-facing compliance workflow (renderable in GitHub). |

---

## Release Notes
This baseline snapshot freezes the **K01 certification authority basis** context for formal CM control.

For a real release (non-example), the snapshot must additionally:
- reference the **CM decision record** and **CERT approval** (links),
- provide an **effectivity statement** (portal + workspace + RBAC),
- provide a **reproducible audit query** path with expected outputs,
- reference the **signed release pack** when applicable.




