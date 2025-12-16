---
title: "K06 ATA 00 Tasklist"
type: IDX
variant: "SPACET"
status: Active
knot_id: "K06"
ata: "00"
last_updated: "2025-12-16"
---

# K06 — data-governance-ssot-schemas-identifiers
## ATA 00 — Tasklist

## Uncertainty to Resolve (ATA-specific)
- Auditability proof path validation for governance compliance
- Query path validation: ID → Schema → Trace → Export

## Tasks (minimum set)
1. Define ATA-specific scope, interfaces, owners.
2. Define decision criteria and evidence package.
3. Execute validation/verification activities.
4. Record decision; update baseline and trace links.

## Completed Deliverables

### Auditability Proof Validator

**Deliverable**: Query path validator for ID → Schema → Trace → Export
---

## 5) Closure Criteria (AI validation deliverables)

This tasklist is **closed** when AI has delivered and validated:

1. **Nomenclature validator** operational in CI (blocks invalid identifier grammar and namespace violations)
2. **Schema registry validator** operational in CI (blocks unregistered schema IDs and version conflicts)
3. **Trace link validator** operational in CI (blocks broken trace links and missing evidence pointers)
4. **Evidence pack generator** operational (produces reproducible evidence packs with link validation)
5. **TEKNIA dedup checker** operational (validates hash uniqueness and namespace separation)
6. **NKU scoring automation** operational (computes partition scores based on evidence + decisions)
7. **Auditability proof validator** operational (validates query paths: `ID → Schema → Trace → Export`)
8. **CI gate integration** complete (all validators run on PR and block merge on failure)

### CM-owned closure dependencies
AI deliverables support CM's closure criteria:
- AI validators enforce CM-approved identifier grammar
- AI CI gates enforce CM-approved SSOT decision matrix
- AI evidence generators consume CM-approved schema governance policy
- AI proof validators verify CM-approved auditability chain definition

---

## 6) Tasks (minimum set, AI perspective)

### 6.1 Automation development
- [ ] **T1-AI (AI-owned)** Develop nomenclature validator (identifier grammar, namespace boundaries)
  - _Deliverable:_ `validate_nomenclature.py` + CI workflow integration
  - _Consumes:_ CM's `00_00_STD_LC01_SPACET_identifier-grammar_v01.md`

- [ ] **T2-AI (AI-owned)** Develop schema registry validator (completeness, version conflicts)
  - _Deliverable:_ Schema validator script + CI workflow integration
  - _Consumes:_ ATA 91 schema registry + CM's schema governance policy

- [ ] **T3-AI (AI-owned)** Develop trace link integrity validator (broken links, staleness)
  - _Deliverable:_ Trace validator script + CI workflow integration
  - _Consumes:_ ATA 93 trace semantics + evidence link schema

- [ ] **T4-AI (AI-owned)** Develop evidence pack generator (automated, reproducible)
  - _Deliverable:_ Evidence pack generation script + templates
  - _Consumes:_ Evidence pack schema + CM's evidence requirements

### 6.2 CI/CD instrumentation
- [ ] **T5-AI (AI-owned)** Implement CI gates for governance enforcement
  - nomenclature validation (pre-commit + PR gate)
  - schema registry validation (PR gate)
  - trace link validation (PR gate + weekly scan)
  - governance-impact detection (PR gate requiring CM approval)
  - _Deliverable:_ GitHub Actions workflows + gate specifications

- [x] **T6-AI (AI-owned)** Implement drift detection and monitoring
  - _Deliverable:_ Weekly drift scan workflow + alerting integration

### 6.3 TEKNIA/NKU tooling
- [ ] **T7-AI (AI-owned)** Implement TEKNIA dedup checker
  - _Deliverable:_ Dedup validation script (hash + namespace checks)

- [x] **T8-AI (AI-owned)** Implement NKU scoring automation
  - _Deliverable:_ NKU ledger updater + partition score calculator
  - _Implementation:_ `scripts/nku_scoring.py` + `00_90_SCH_SB90_AMPEL360_SPACET_GEN_nku-ledger-schema_v01.json`
  - _Status:_ Complete (2025-12-16)

- [ ] **T9-AI (AI-owned)** Implement auditability proof validator
  - _Deliverable:_ Query path validator for `ID → Schema → Trace → Export`

### 6.4 Documentation and integration
- [ ] **T10-AI (AI-owned)** Document automation architecture and integration points
  - _Deliverable:_ `00_00_IDX_LC01_SPACET_ai-automation-architecture_v01.md`

- [ ] **T11-AI (AI-owned)** Create runbooks for CI gate failures and remediation
  - _Deliverable:_ `00_00_RPT_LC01_SPACET_ci-gate-runbook_v01.md`

---

## 7) Outputs / Artifacts (AI-specific)

### Validation tooling (TYPE=executable scripts)
- Nomenclature validator (`validate_nomenclature.py`)
- Schema registry validator
- Trace link integrity validator
- Evidence pack generator
- TEKNIA dedup checker
- NKU scoring calculator
- Auditability proof validator

### CI/CD integration (TYPE=workflows)
- Pre-commit hook configurations
- PR gate workflow definitions
- Weekly drift scan workflows
- Governance-impact detection workflow

### Documentation (TYPE=IDX/RPT/STD)
- Automation architecture index
- CI gate runbook
- Validator usage guides
- Integration specifications

### Evidence outputs (TYPE=RPT/TAB)
- Validation reports (per-PR)
- Drift detection reports (weekly)
- NKU ledger updates (per-partition)
- Auditability proof chains (on-demand)

---

## 8) Dependencies / Risks (AI perspective)

### Dependencies
- **CM standards** (identifier grammar, SSOT matrix, governance policy) must be published before AI can implement validators
- **ATA 91 schema registry** must be operational before schema validation can be enforced
- **ATA 93 trace semantics** must be defined before trace link validation can be implemented
- **ATA 99 namespace registry** must exist before dedup enforcement can be automated

**Location**: `scripts/validate_audit_proof_path.py`

**Description**: Python script implementing the 8-step audit query path from the Auditability Proof Path Report. Validates the complete chain from identifier through schema, trace links, to export/evidence.

**Usage**:
```bash
# Validate complete audit chain for an identifier
python scripts/validate_audit_proof_path.py --validate-chain DATUM-GLOBAL-001

# Validate identifier format only
python scripts/validate_audit_proof_path.py --id ZONE-PROP-001

# Discover and validate all identifiers in repository
python scripts/validate_audit_proof_path.py --check-all
```

**Validation Steps**:
1. **Step 1 - Identifier Validation**: Validates identifier format against grammar standard
2. **Step 2 - Schema Validation**: Locates and verifies schema registration
3. **Steps 3-5 - Trace Link Validation**: Finds related trace links (design, implementation, test)
4. **Step 6 - Export Validation**: Verifies identifier presence in export files
5. **Step 7 - Baseline Verification**: Confirms baseline inclusion
6. **Step 8 - Approval Verification**: Checks approval status

**Exit Codes**:
- `0`: Validation passed
- `1`: Validation errors found
- `2`: Script error

**References**:
- `00_00_RPT_LC01_AMPEL360_SPACET_PLUS_auditability-proof-path_v01.md`
- `00_00_STD_LC01_AMPEL360_SPACET_PLUS_identifier-grammar_v01.md`
- `06_90_SCH_SB90_AMPEL360_SPACET_GEN_dimensional-data-schema_v01.json`
