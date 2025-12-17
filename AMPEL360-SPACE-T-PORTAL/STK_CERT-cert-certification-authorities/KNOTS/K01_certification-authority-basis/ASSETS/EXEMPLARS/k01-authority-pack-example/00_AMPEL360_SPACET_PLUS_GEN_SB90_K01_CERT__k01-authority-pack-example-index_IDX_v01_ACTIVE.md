---
title: "K01 Authority Pack Example — Index"
type: IDX
project: "AMPEL360"
program: "SPACET"
variant: "PLUS"
status: "DRAFT"
knot_id: "K01"
lc_or_subbucket: "SB90"
bucket: "90"
exemplar: "authority-pack"
generated: "2025-12-15"
---

# K01 Authority Pack Example — Index

This exemplar demonstrates a **minimum viable, audit-ready** certification authority submission pack aligned with **K01** (certification-authority-basis).  
It is designed to be **GitHub-navigable** and to illustrate **evidence-first** packaging (TEKNIA rule: reproducible trace + inventory + decision context).

## Links (GitHub-navigable)
- K01 Assets index: **[00_00_IDX_LC01_AMPEL360_SPACET_PLUS_k01-assets-index_v01.md](../../00_00_IDX_LC01_AMPEL360_SPACET_PLUS_k01-assets-index_v01.md)**
- K01 Compliance workflow: **[00_90_DIA_SB90_AMPEL360_SPACET_PLUS_k01-compliance-workflow_v01.md](../../DIAGRAMS/00_AMPEL360_SPACET_PLUS_90_DIA_SB90_K01_CERT__k01-compliance-workflow_v01.md)**
- K01 RACI / decision rights: **[00_90_DIA_SB90_AMPEL360_SPACET_PLUS_k01-raci-decision-rights_v01.md](../../DIAGRAMS/00_AMPEL360_SPACET_PLUS_90_DIA_SB90_K01_CERT__k01-raci-decision-rights_v01.md)**
- K01 Evidence Pack Manifest schema (contract): **[00_00_SCH_LC01_AMPEL360_SPACET_PLUS_k01-evidence-pack-manifest_v01.json](../../SCHEMAS/00_00_SCH_LC01_AMPEL360_SPACET_PLUS_k01-evidence-pack-manifest_v01.json)**

## Purpose
This exemplar shows how to organize a complete authority submission pack for K01 tasks (especially **T002 Compliance Mapping**):
- deterministic, machine-readable inventory (manifest),
- human-readable contents list with links,
- trace hooks into the portal (ATA taskspaces, decisions, and evidence),
- a minimal **audit query path** (IDs → schema → trace → evidence → release).

## Contents (this folder)
> Replace filenames below with the actual files present in this exemplar folder.

### 1) Manifest (machine-readable)
- **[00_90_SCH_SB90_AMPEL360_SPACET_PLUS_k01-authority-pack-manifest-example_v01.json](./00_90_SCH_SB90_AMPEL360_SPACET_PLUS_k01-authority-pack-manifest-example_v01.json)**  
  _Comment:_ Canonical inventory: package ID, version, included artifacts, hashes (if used), and linkage to K01 decisions.

### 2) Contents List (human-readable)
- **[00_90_LST_SB90_AMPEL360_SPACET_PLUS_k01-authority-pack-contents-example_v01.md](./00_90_LST_SB90_AMPEL360_SPACET_PLUS_k01-authority-pack-contents-example_v01.md)**  
  _Comment:_ Reviewer-friendly list: what each item is, why it exists, and where it originates in the portal.

### 3) Evidence pointers (referenced, not copied)
- **[00_90_TRC_SB90_AMPEL360_SPACET_PLUS_k01-authority-pack-evidence-links-example_v01.md](./00_90_TRC_SB90_AMPEL360_SPACET_PLUS_k01-authority-pack-evidence-links-example_v01.md)**  
  _Comment:_ Links to authoritative evidence locations (per ATA taskspaces), avoiding duplication while ensuring trace.

### 4) Decision context (what was approved)
- **[00_90_STD_SB90_AMPEL360_SPACET_PLUS_k01-authority-pack-decision-context-example_v01.md](./00_90_STD_SB90_AMPEL360_SPACET_PLUS_k01-authority-pack-decision-context-example_v01.md)**  
  _Comment:_ Extract of decision statements and approvals (CERT + CM), plus scope boundary and assumptions.

### 5) Audit query path (reproducible)
- **[00_90_IDX_SB90_AMPEL360_SPACET_PLUS_k01-authority-pack-audit-query-example_v01.md](./00_90_IDX_SB90_AMPEL360_SPACET_PLUS_k01-authority-pack-audit-query-example_v01.md)**  
  _Comment:_ A “how to reproduce” path that demonstrates auditability (what to click/run, expected outputs).

## Canonical pack structure (reference)
Use this structure when building a real submission pack (do not copy evidence files; link them):

```text
k01-authority-pack-example/
├── 00_90_SCH_SB90_AMPEL360_SPACET_PLUS_k01-authority-pack-manifest-example_v01.json
├── 00_90_LST_SB90_AMPEL360_SPACET_PLUS_k01-authority-pack-contents-example_v01.md
├── 00_90_TRC_SB90_AMPEL360_SPACET_PLUS_k01-authority-pack-evidence-links-example_v01.md
├── 00_90_STD_SB90_AMPEL360_SPACET_PLUS_k01-authority-pack-decision-context-example_v01.md
└── 00_90_IDX_SB90_AMPEL360_SPACET_PLUS_k01-authority-pack-audit-query-example_v01.md
````

## TEKNIA control note (evidence-first sharing)

This exemplar is **shareable outside the core team only if**:

1. The manifest is complete and consistent with the K01 manifest schema.
2. Every listed item has a valid GitHub link (no dead paths).
3. The audit query page is reproducible (a reviewer can follow it end-to-end).
4. CERT + CM approvals exist (or the pack is explicitly marked “pre-decision draft”).

## Reviewer checklist (quick)

* [ ] Links render in GitHub (no 404s)
* [ ] Scope and assumptions are explicit
* [ ] MoC mapping references acceptance criteria
* [ ] Trace links exist to affected ATA workspaces
* [ ] Release/baseline reference is present (if applicable)


