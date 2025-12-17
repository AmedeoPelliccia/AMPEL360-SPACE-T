---
title: "K06 ATA 00 Tasklist"
type: "IDX"
variant: "SPACET"
status: "Active"
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
- `00_AMPEL360_SPACET_PLUS_00_RPT_LC01_K00_CM__auditability-proof-path_v01.md`
- `00_AMPEL360_SPACET_PLUS_00_STD_LC01_K00_DATA__identifier-grammar_v01.md`
- F_AMPEL360_SPACET_GEN_90_SCH_SB90_K06_CM__dimensional-data-schema_v01.json`
