# T002 — Identifier grammar

**Owner (AoR):** STK_AI  
**Approver (AoR):** STK_CM  
**Status:** NOT-STARTED  
**Closes:** Inconsistent schema IDs, namespaces, versions, and package names.

## Objective
Define canonical identifier grammar for:
- schema IDs
- versions (semver or project-specific)
- namespaces
- packages (schema packs)
- references (cross-ATA linking)

## Outputs (artifacts)
- Identifier Grammar Spec (target): `.../IDENTIFIERS/grammar.md`
- Machine-readable grammar (target): `.../IDENTIFIERS/grammar.yaml`
- Examples + invalid cases (target): `.../IDENTIFIERS/examples.md`

## Acceptance criteria
- Grammar is unambiguous and testable (regexes / ABNF-like rules)
- Version format is defined (incl. pre-release, deprecation tags)
- Namespaces encode at least: program, ATA, subject scope, package
- Backward compatibility constraints are declared (ties into T004)

## Definition of Done
- Grammar spec + YAML exist
- At least 10 valid and 10 invalid examples included
- CI gate stub references these rules (link to T005)

## Links
- Depends on: T001
- Feeds: T003, T004, T005, T006
