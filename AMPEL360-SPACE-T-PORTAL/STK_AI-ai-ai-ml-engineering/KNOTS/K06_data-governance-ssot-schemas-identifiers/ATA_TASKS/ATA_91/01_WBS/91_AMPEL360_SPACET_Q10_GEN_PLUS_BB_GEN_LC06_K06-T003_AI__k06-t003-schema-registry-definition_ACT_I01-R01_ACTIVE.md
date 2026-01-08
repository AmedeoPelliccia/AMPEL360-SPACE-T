# T003 — Schema registry definition

**Owner (AoR):** STK_AI  
**Approver (AoR):** STK_CM  
**Status:** NOT-STARTED  
**Closes:** No consistent discovery metadata or workflows for schemas.

## Objective
Define the schema registry:
- required fields (metadata)
- discovery and indexing rules
- workflows (add/update/deprecate)
- validation responsibilities

## Outputs (artifacts)
- Registry schema (target): `.../SCHEMAS/REGISTRY/registry.schema.json`
- Registry index format (target): `.../SCHEMAS/REGISTRY/index.yaml`
- Workflow doc (target): `.../SCHEMAS/REGISTRY/workflow.md`

## Acceptance criteria
- Registry entry includes: schema_id, version, namespace, owner_aor, status, sha256, dependencies, applicable_ata, date, change_ref
- Index is machine-readable and supports deterministic resolution
- Workflow defines required approvals and review checks (STK_CM approval gate)

## Definition of Done
- registry.schema.json exists and validates index.yaml
- Example entries exist for ≥ 3 schema packs (real or placeholders)
- CI gate references registry checks (link to T005)

## Links
- Depends on: T001, T002
- Feeds: T005, T006, T008
