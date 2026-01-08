# T006 — Schema pack export

**Owner (AoR):** STK_AI  
**Approver (AoR):** STK_CM  
**Status:** NOT-STARTED  
**Closes:** No deterministic packaging/publication of schema packs.

## Objective
Define deterministic packaging and publication:
- pack contents rules
- naming rules (pack id/version)
- manifests (hashes, dependencies)
- export destinations (consumption + evidence)

## Outputs (artifacts)
- Export spec (target): `.../EXPORTS/SCHEMA_PACKS/export_spec.md`
- Pack manifest schema (target): `.../EXPORTS/SCHEMA_PACKS/pack.manifest.schema.json`
- Example pack manifest (target): `.../EXPORTS/SCHEMA_PACKS/examples/pack.manifest.json`

## Acceptance criteria
- Export is reproducible from repo state (same inputs => same hashes)
- Manifest includes sha256 per file + overall pack digest
- Registry links to pack artifacts (bidirectional trace)
- Evidence path is defined (where packs are published/anchored)

## Definition of Done
- Export spec + schemas exist
- One example pack can be produced locally and validated by CI

## Links
- Depends on: T003, T004, T005
- Feeds: T008
