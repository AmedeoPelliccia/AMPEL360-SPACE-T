# K06 ATA 91 Work Breakdown — 01_WBS

**Portal:** AMPEL360-SPACE-T-PORTAL  
**AoR (entry point):** STK_AI  
**KNOT:** K06 — Data governance / SSOT / schemas / identifiers  
**ATA_TASKS:** ATA_91  
**Objective:** Convert uncertainty into executable work packages (tasks, owners, inputs/outputs).

## Closes
"We don't know what to do next / who owns it."

## Done when
- T001–T008 exist with: owner, acceptance criteria, artifact links
- RACI.csv exists and CM approval path is explicit and accepted

## Task list
| Task | Title | Owner (AoR) | Approver (AoR) | Primary artifact(s) |
|---|---|---|---|---|
| T001 | SSOT source & ownership | STK_AI | STK_CM | SSOT Authority + Change Control |
| T002 | Identifier grammar | STK_AI | STK_CM | ID Grammar Spec |
| T003 | Schema registry definition | STK_AI | STK_CM | Registry Schema + Workflow |
| T004 | Versioning & compatibility policy | STK_AI | STK_CM | Compatibility Policy |
| T005 | CI validation gates | STK_AI | STK_CM | CI Gate Specs + Checks |
| T006 | Schema pack export | STK_AI | STK_CM | Export/Packaging Spec |
| T007 | Canonical model alignment | STK_SE | STK_CM | Canonical Model Alignment Rules |
| T008 | Schema consumer onboarding | STK_AI | STK_PMO | Onboarding Process + Guardrails |

## Artifact link map (targets)
These are *targets* to be created/linked by tasks. Keep paths stable once created.

- Schema registry root (target): `.../SCHEMAS/REGISTRY/`
- Canonical models root (target): `.../CANONICAL_MODELS/`
- Identifier grammar (target): `.../IDENTIFIERS/grammar.md` (or `.yaml/.json` as decided)
- CI gate definitions (target): `.../CI/GATES/`
- Export packs (target): `.../EXPORTS/SCHEMA_PACKS/`

## Governance
- Change control authority: **STK_CM**
- Implementing authority: **STK_AI**
- System-wide alignment stakeholder: **STK_SE**
- Rollout / adoption tracking: **STK_PMO**
