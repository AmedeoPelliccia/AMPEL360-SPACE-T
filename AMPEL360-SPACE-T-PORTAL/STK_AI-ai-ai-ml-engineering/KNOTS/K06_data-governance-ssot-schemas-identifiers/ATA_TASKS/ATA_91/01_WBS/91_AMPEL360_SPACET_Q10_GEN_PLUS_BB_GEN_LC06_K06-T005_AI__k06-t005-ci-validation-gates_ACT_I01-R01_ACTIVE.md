# T005 — CI validation gates

**Owner (AoR):** STK_AI  
**Approver (AoR):** STK_CM  
**Status:** NOT-STARTED  
**Closes:** Schemas can drift without enforcement.

## Objective
Define CI gates that enforce:
- schema validity (JSON Schema/YAML schema lint)
- registry completeness and correctness
- versioning compliance (T004)
- identifier grammar compliance (T002)
- canonical model alignment checks (T007)

## Outputs (artifacts)
- Gate spec (target): `.../CI/GATES/schema_gates.md`
- Gate config (target): `.../CI/GATES/schema_gates.yml`
- Validator tool stub (target): `.../tools/ci/schema_registry_validator.py`

## Acceptance criteria
- Gates fail PRs on: invalid schema, missing registry entry, wrong version bump, invalid ID format
- Gates produce actionable output (file + reason + fix hint)
- STK_CM approval required for policy exceptions (documented mechanism)

## Definition of Done
- CI gate definitions exist in repo
- One minimal validator runs in CI on sample registry
- Documentation explains local execution

## Links
- Depends on: T002, T003, T004, T007
- Feeds: T006, T008
