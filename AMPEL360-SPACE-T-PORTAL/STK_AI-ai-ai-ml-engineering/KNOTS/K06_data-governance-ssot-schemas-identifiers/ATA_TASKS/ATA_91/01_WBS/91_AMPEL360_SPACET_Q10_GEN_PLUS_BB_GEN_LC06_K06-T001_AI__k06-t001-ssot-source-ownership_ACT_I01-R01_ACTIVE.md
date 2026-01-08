# T001 — SSOT source & ownership

**Owner (AoR):** STK_AI  
**Approver (AoR):** STK_CM  
**Status:** NOT-STARTED  
**Closes:** SSOT ambiguity for schema registry + canonical models.

## Objective
Declare authoritative SSOT locations for:
- schema registry
- canonical models
- identifier grammar packages
Define decision rights and change control.

## Inputs
- Existing portal folder taxonomy
- Current schema/code locations (if any)

## Outputs (artifacts)
- SSOT Authority Statement (target): `.../SCHEMAS/SSOT_AUTHORITY.md`
- Change Control Policy (target): `.../SCHEMAS/CHANGE_CONTROL.md`
- Ownership map (target): `.../SCHEMAS/OWNERSHIP.yaml`

## Acceptance criteria
- SSOT root paths are explicitly declared (registry + canonical models + identifiers)
- Change control flow exists (proposal → review → approval → merge)
- Approver is STK_CM and is explicitly stated
- Artifact links in this task point to stable repo paths

## Definition of Done
- Artifacts exist at target paths
- STK_CM approval recorded (link to SIGNOFF artifact or PR reference)

## Links
- Index: `00_INDEX.md`
- RACI: `RACI.csv`
