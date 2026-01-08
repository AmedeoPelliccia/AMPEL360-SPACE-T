# T004 — Versioning & compatibility policy

**Owner (AoR):** STK_AI  
**Approver (AoR):** STK_CM  
**Status:** NOT-STARTED  
**Closes:** Breaking changes without controls; unclear deprecation.

## Objective
Define:
- breaking vs non-breaking change rules
- deprecation windows
- migration obligations
- compatibility checks (schema evolution)

## Outputs (artifacts)
- Policy doc (target): `.../SCHEMAS/POLICY/versioning_compatibility.md`
- Compatibility matrix template (target): `.../SCHEMAS/POLICY/compatibility_matrix.csv`

## Acceptance criteria
- Clear rule set for MAJOR/MINOR/PATCH (or equivalent)
- Deprecation process includes timelines and required communications
- Migration plan requirement for breaking changes
- Compatibility enforcement strategy is specified (ties to T005)

## Definition of Done
- Policy doc exists, reviewed, and approved by STK_CM
- CI rules reference policy (link to T005)

## Links
- Depends on: T002, T003
- Feeds: T005, T006, T008
