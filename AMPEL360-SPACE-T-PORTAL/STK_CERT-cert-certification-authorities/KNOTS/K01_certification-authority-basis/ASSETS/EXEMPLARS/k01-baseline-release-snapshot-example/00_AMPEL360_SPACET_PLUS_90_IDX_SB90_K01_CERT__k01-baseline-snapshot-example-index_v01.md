---
title: "K01 Baseline Release Snapshot Example — Index"
type: IDX
project: "AMPEL360"
program: "SPACET"
variant: "PLUS"
status: "EXAMPLE"
knot_id: "K01"
bucket: "90"
lc_or_subbucket: "SB90"
exemplar: "baseline-release-snapshot"
generated: "2025-12-15"
---

# K01 Baseline Release Snapshot Example — Index

This exemplar demonstrates the **minimum baseline snapshot** structure expected when K01 activities result in a **controlled release** (CM-governed) and an **authority-facing evidence snapshot**.

## Links (GitHub-navigable)
- K01 Assets index: **[00_00_IDX_LC01_AMPEL360_SPACET_PLUS_k01-assets-index_v01.md](../../00_00_IDX_LC01_AMPEL360_SPACET_PLUS_k01-assets-index_v01.md)**
- K01 Compliance workflow: **[00_90_DIA_SB90_AMPEL360_SPACET_PLUS_k01-compliance-workflow_v01.md](../../DIAGRAMS/00_AMPEL360_SPACET_PLUS_90_DIA_SB90_K01_CERT__k01-compliance-workflow_v01.md)**
- K01 Evidence Pack Manifest schema (contract): **[00_00_SCH_LC01_AMPEL360_SPACET_PLUS_k01-evidence-pack-manifest_v01.json](../../SCHEMAS/00_00_SCH_LC01_AMPEL360_SPACET_PLUS_k01-evidence-pack-manifest_v01.json)**

---

## 1) What this snapshot represents
A baseline snapshot is a **frozen, reviewable** representation of:
- the **decision state** (what was approved),
- the **baseline scope/effectivity** (what is included),
- the **evidence inventory** (what supports compliance),
- and the **audit path** (how a reviewer reproduces traceability checks).

This is not the full payload of all evidence; it is the **release “front-door”** for auditors and reviewers.

---

## 2) Snapshot contents (expected in this exemplar folder)

| # | Artifact | Filename (GitHub link) | Comment |
|---:|---|---|---|
| 1 | Snapshot Manifest (machine-readable) | **[00_90_SCH_SB90_AMPEL360_SPACET_PLUS_k01-baseline-snapshot-manifest-example_v01.json](./00_90_SCH_SB90_AMPEL360_SPACET_PLUS_k01-baseline-snapshot-manifest-example_v01.json)** | Canonical inventory of the snapshot, versions, and included references. |
| 2 | Snapshot Contents List (human-readable) | **[00_90_LST_SB90_AMPEL360_SPACET_PLUS_k01-baseline-snapshot-contents-example_v01.md](./00_90_LST_SB90_AMPEL360_SPACET_PLUS_k01-baseline-snapshot-contents-example_v01.md)** | Reviewer-oriented “what/why” list with links. |
| 3 | Release Notes (what changed) | **[00_90_RPT_SB90_AMPEL360_SPACET_PLUS_k01-baseline-snapshot-release-notes-example_v01.md](./00_90_RPT_SB90_AMPEL360_SPACET_PLUS_k01-baseline-snapshot-release-notes-example_v01.md)** | Delta summary and impact highlights. |
| 4 | Effectivity / Scope Statement | **[00_90_LST_SB90_AMPEL360_SPACET_PLUS_k01-baseline-snapshot-effectivity-example_v01.md](./00_90_LST_SB90_AMPEL360_SPACET_PLUS_k01-baseline-snapshot-effectivity-example_v01.md)** | What is in/out, and which portal workspaces it applies to. |
| 5 | Evidence Links (click-through) | **[00_90_TRC_SB90_AMPEL360_SPACET_PLUS_k01-baseline-snapshot-evidence-links-example_v01.md](./00_90_TRC_SB90_AMPEL360_SPACET_PLUS_k01-baseline-snapshot-evidence-links-example_v01.md)** | Links to the authoritative evidence locations (ATA taskspaces). |
| 6 | Decision Record Pointer | **[00_90_STD_SB90_AMPEL360_SPACET_PLUS_k01-baseline-snapshot-decision-pointer-example_v01.md](./00_90_STD_SB90_AMPEL360_SPACET_PLUS_k01-baseline-snapshot-decision-pointer-example_v01.md)** | Links to CM/CERT approval records. |
| 7 | Audit Query Path | **[00_90_IDX_SB90_AMPEL360_SPACET_PLUS_k01-baseline-snapshot-audit-query-example_v01.md](./00_90_IDX_SB90_AMPEL360_SPACET_PLUS_k01-baseline-snapshot-audit-query-example_v01.md)** | Repro steps + expected results (trace → evidence → snapshot). |

> If any file is missing, create a stub and keep the link targets stable.

---

## 3) Canonical directory skeleton (reference)

```text
k01-baseline-release-snapshot-example/
├── 00_90_SCH_SB90_AMPEL360_SPACET_PLUS_k01-baseline-snapshot-manifest-example_v01.json
├── 00_90_LST_SB90_AMPEL360_SPACET_PLUS_k01-baseline-snapshot-contents-example_v01.md
├── 00_90_RPT_SB90_AMPEL360_SPACET_PLUS_k01-baseline-snapshot-release-notes-example_v01.md
├── 00_90_LST_SB90_AMPEL360_SPACET_PLUS_k01-baseline-snapshot-effectivity-example_v01.md
├── 00_90_TRC_SB90_AMPEL360_SPACET_PLUS_k01-baseline-snapshot-evidence-links-example_v01.md
├── 00_90_STD_SB90_AMPEL360_SPACET_PLUS_k01-baseline-snapshot-decision-pointer-example_v01.md
└── 00_90_IDX_SB90_AMPEL360_SPACET_PLUS_k01-baseline-snapshot-audit-query-example_v01.md
````

---

## 4) Effectivity expectations (portal + workspace)

A baseline snapshot must declare:

* **Portal effectivity**: which stakeholder entry points (STK_*) are in-scope,
* **Workspace effectivity**: which ATA taskspaces are included/excluded,
* **Access grants**: minimum RBAC roles required to view each referenced item (e.g., PUBLIC / INTERNAL / CONFIDENTIAL / RESTRICTED).

The effectivity statement is provided in:

* **[00_90_LST_SB90_AMPEL360_SPACET_PLUS_k01-baseline-snapshot-effectivity-example_v01.md](./00_90_LST_SB90_AMPEL360_SPACET_PLUS_k01-baseline-snapshot-effectivity-example_v01.md)**

---

## 5) NKU / TEKNIA monitoring note

This snapshot is considered “release-grade” only if:

* NKU for K01 is above the release threshold (per K01 monitoring rules),
* the evidence inventory is complete and link-valid,
* decision approvals are present (CM + CERT),
* audit query path reproduces expected outputs.

For exemplars, approvals may be marked as `N/A`, but structure must be complete.

::contentReference[oaicite:0]{index=0}
```
