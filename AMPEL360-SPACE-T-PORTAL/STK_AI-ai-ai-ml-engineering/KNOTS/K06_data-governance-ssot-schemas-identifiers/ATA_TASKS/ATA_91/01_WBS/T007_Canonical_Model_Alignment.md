# T007 — Canonical model alignment

**Owner (AoR):** STK_SE  
**Approver (AoR):** STK_CM  
**Status:** NOT-STARTED  
**Closes:** Divergent entity definitions across ATAs ("same thing, different schema").

## Objective
Ensure shared entity definitions remain consistent across ATAs:
- canonical entity set
- ownership and change control
- mapping rules (ATA-local extensions)
- alignment checks consumed by CI

## Outputs (artifacts)
- Canonical entity catalog (target): `.../CANONICAL_MODELS/entities.yaml`
- Alignment rules (target): `.../CANONICAL_MODELS/alignment_rules.md`
- Extension policy (target): `.../CANONICAL_MODELS/extension_policy.md`

## Acceptance criteria
- Canonical entities are versioned and governed (STK_CM approval)
- Extension rules prevent breaking divergence
- CI-checkable alignment rules exist (ties into T005)

## Definition of Done
- Canonical artifacts exist and are referenced by registry entries
- At least one example of ATA-local extension is documented

## Links
- Depends on: T001
- Feeds: T005, T008
