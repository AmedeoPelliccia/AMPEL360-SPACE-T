# T008 — Schema consumer onboarding

**Owner (AoR):** STK_AI  
**Approver (AoR):** STK_PMO  
**Status:** NOT-STARTED  
**Closes:** "Shadow schemas" and inconsistent adoption across ATAs.

## Objective
Define an onboarding pathway for ATAs/teams:
- how to discover approved schemas
- how to request changes
- how to adopt packs and validate locally
- how to prevent shadow schema creation

## Outputs (artifacts)
- Onboarding guide (target): `.../SCHEMAS/ONBOARDING.md`
- Intake template (target): `.../SCHEMAS/INTAKE_TEMPLATE.md`
- Shadow-schema blocking rules (target): `.../SCHEMAS/POLICY/no_shadow_schemas.md`

## Acceptance criteria
- Clear adoption steps for a new ATA team
- Mandatory registry usage and CI checks are described
- Exceptions require explicit approval path (STK_CM referenced)
- PMO tracking mechanism is defined (rollout metrics)

## Definition of Done
- Onboarding doc exists and links to registry + CI instructions
- Intake template exists and is usable in PRs/issues

## Links
- Depends on: T003, T005, T006, T007
