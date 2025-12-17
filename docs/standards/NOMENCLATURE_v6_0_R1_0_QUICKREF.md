# Nomenclature Standard v6.0 (R1.0) - Quick Reference

**Date**: 2025-12-17 | **Status**: Normative | **Owner**: CM WG

---

## Canonical Format

```
[ATA_ROOT]_[PROJECT]_[PROGRAM]_[FAMILY]_[VARIANT]_[VERSION]_[MODEL]_[BLOCK]_[PHASE]_[KNOT_TASK]_[AoR]__[SUBJECT]_[TYPE]_[ISSUE-REVISION]_[STATUS].[EXT]
```

---

## Field Quick Reference

| Field           | Format/Constraint                    | Examples                     |
|:----------------|:-------------------------------------|:-----------------------------|
| ATA_ROOT        | 2 digits (<100), 3 digits (≥100)    | `00`, `27`, `115`            |
| PROJECT         | `AMPEL360` (fixed)                   | `AMPEL360`                   |
| PROGRAM         | `SPACET` (fixed)                     | `SPACET`                     |
| FAMILY          | `Q##` or `Q###` (allowlist)          | `Q10`, `Q100`                |
| VARIANT         | Allowlist (GEN, BASELINE, etc.)      | `GEN`, `CERT`, `FLIGHTTEST`  |
| VERSION         | Allowlist (PLUS, PLUSULTRA)          | `PLUS`, `PLUSULTRA`          |
| MODEL           | Allowlist (BB, HW, SW, PR)           | `BB`, `HW`, `SW`, `PR`       |
| BLOCK           | B## format (B00-B90)                 | `B10`, `B50`, `B60`, `B20`   |
| PHASE           | LC01-LC14 or SB01-SB99               | `LC03`, `SB04`, `LC10`       |
| KNOT_TASK       | K01-K14, optional -T001 to -T999     | `K06`, `K06-T001`, `K02`     |
| AoR             | Allowlist (portal entry points)      | `CM`, `CERT`, `SAF`, `SE`    |
| SUBJECT         | lowercase-kebab-case                 | `thermal-loop`, `model-card` |
| TYPE            | Allowlist (STD, RPT, FHA, etc.)      | `STD`, `RPT`, `FHA`, `PLAN`  |
| ISSUE-REVISION  | I##-R## (e.g., I01-R01)              | `I01-R01`, `I12-R03`         |
| STATUS          | Allowlist (DRAFT, ACTIVE, etc.)      | `DRAFT`, `ACTIVE`, `APPROVED`|
| EXT             | Allowlist (md, json, pdf, etc.)      | `md`, `json`, `pdf`, `yaml`  |

---

## Critical Rules

### 🔴 **BREAKING CHANGES from v5.0**

1. **FAMILY added**: Quantum-inspired pax family (Q10, Q100)
2. **VARIANT redefined**: Now governance lane token (GEN, BASELINE, CERT, etc.)
3. **VERSION added**: Branding reinforcer (PLUS, PLUSULTRA)
4. **MODEL added**: Artifact domain (BB, HW, SW, PR)
5. **ISSUE-REVISION added**: Change tracking format (I##-R##)
6. **Field positions changed**: Total 16 fields vs 12 in v5.0

### 🟡 **Mandatory Rules**

1. **Double underscore**: `__` (double) before SUBJECT, not single `_`
2. **KNOT governance**: Only K01-K14 allowed (no K15+)
3. **AoR mandatory**: Must be from allowlist (no `STK_` prefix)
4. **ISSUE-REVISION format**: Must be `I##-R##` with zero-padding
5. **No spaces**: All fields use hyphens or no separators

### 🟢 **Allowlist Governance**

* All allowlists defined in `config/nomenclature/v6_0.yaml`
* Changes require CM WG approval
* New KNOTs require standard upgrade (not just config change)

---

## Field Allowlists (Initial R1.0)

### FAMILY
```
Q10      # 10-passenger quantum family
Q100     # 100-passenger quantum family
```

### VARIANT
```
GEN              # General purpose
BASELINE         # Baseline configuration
FLIGHTTEST       # Flight test variant
CERT             # Certification variant
MSN              # Mission-specific
HOV              # High-occupancy vehicle
CUST             # Customer-specific
```

### VERSION
```
PLUS             # AMPEL360+ standard
PLUSULTRA        # AMPEL360+ Ultra enhanced
```

### MODEL
```
BB               # Body Brain / PR-O-RO model
HW               # Hardware
SW               # Software
PR               # Process/Procedure
```

### BLOCK (Domain Partitions - OPTINS Framework)
```
B00      # GENERAL (universal, implicit)
B10      # OPERATIONAL SYSTEMS (onboard/offboard/simtest)
B20      # CYBERSECURITY (digital + onboard)
B30      # DATA, COMMS AND REGISTRY (digital + onboard)
B40      # PHYSICS (pressure/thermal/crio) (onboard + simtest)
B50      # PHYSICAL (aerostructures + HW) (onboard/offboard)
B60      # DYNAMICS (thrust/attitude/inerting) (onboard + simtest)
B70      # RECIPROCITY & ALTERNATIVE ENGINES (onboard + simtest)
B80      # RENEWABLE ENERGY & CIRCULARITY (onboard + offboard)
B90      # CONNECTIONS & MAPPING (digital + onboard)
```

**Note:** Not all BLOCK values are valid for all ATA_ROOT values. See `config/nomenclature/ATA_PARTITION_MATRIX.yaml` for complete mapping.

### AoR (Portal Entry Points)
```
CM, CERT, SAF, SE, OPS, DATA, AI, CY, TEST, MRO,
SPACEPORT, PMO, QA, SEC, LEG, FIN, PROC
```

### TYPE
```
IDX, STD, PLAN, MIN, RPT, LOG, ACT, FHA, PSSA, SSA, FTA,
ANA, REQ, DAL, TRC, CAT, LST, GLO, MAT, SCH, DIA, TAB,
SPEC, PLN, PROC, MAN, API, CFG, JSON, YAML
```

### STATUS
```
TEMPLATE, DRAFT, ACTIVE, APPROVED, RELEASED, SUPERSEDED, ARCHIVED
```

### EXT
```
md, yml, yaml, json, csv, svg, png, jpg, jpeg, pdf, drawio
```

---

## Examples

### ✅ Valid v6.0 Examples

**Thermal loop overview (Q10, GEN, PLUS, BB, B10):**
```
27_AMPEL360_SPACET_Q10_GEN_PLUS_BB_B10_LC03_K06-T001_SE__thermal-loop-overview_STD_I01-R01_ACTIVE.md
```

**Pressure bulkhead trade (Q100, CERT, HW, B50):**
```
53_AMPEL360_SPACET_Q100_CERT_PLUS_HW_B50_LC07_K02_CERT__pressure-bulkhead-trade_RPT_I02-R01_DRAFT.pdf
```

**Model card template (Q10, BASELINE, SW, B20):**
```
95_AMPEL360_SPACET_Q10_BASELINE_PLUS_SW_B20_SB04_K11_CM__model-card-template_STD_I01-R01_TEMPLATE.md
```

**Cert authority basis (Q10, CERT, PR, B00):**
```
00_AMPEL360_SPACET_Q10_CERT_PLUS_PR_B00_LC10_K01_CERT__certification-authority-basis_PLAN_I01-R01_ACTIVE.md
```

### ❌ Common Errors

**Missing new fields (v5.0 format):**
```
27_AMPEL360_SPACET_PLUS_B10_LC03_K06_SE__thermal-loop_STD_v01_ACTIVE.md
❌ Missing: FAMILY, VARIANT (redefined), VERSION, MODEL, ISSUE-REVISION
```

**Invalid KNOT:**
```
27_AMPEL360_SPACET_Q10_GEN_PLUS_BB_B10_LC03_K99_SE__thermal-loop_STD_I01-R01_ACTIVE.md
❌ K99 not allowed (only K01-K14)
```

**Single underscore before SUBJECT:**
```
27_AMPEL360_SPACET_Q10_GEN_PLUS_BB_B10_LC03_K06_SE_thermal-loop_STD_I01-R01_ACTIVE.md
❌ Must use double underscore (__) before SUBJECT
```

**Invalid FAMILY:**
```
27_AMPEL360_SPACET_Q50_GEN_PLUS_BB_OPS_LC03_K06_SE__thermal-loop_STD_I01-R01_ACTIVE.md
❌ Q50 not in allowlist (only Q10, Q100 initially)
```

**Invalid ISSUE-REVISION format:**
```
27_AMPEL360_SPACET_Q10_GEN_PLUS_BB_OPS_LC03_K06_SE__thermal-loop_STD_I1-R1_ACTIVE.md
❌ Must be I##-R## with zero-padding (I01-R01, not I1-R1)
```

---

## Validation Modes (v6.0)

| Mode   | Behavior                                      | Use Case           |
|:-------|:----------------------------------------------|:-------------------|
| WARN   | Report violations without failing             | Pre-release testing|
| REPORT | Generate detailed violation inventory         | Pre-retrofit audit |
| BLOCK  | Fail CI on any violation (PR-blocking)        | Post-retrofit      |

---

## Migration from v5.0 to v6.0

### Default Value Assignment

| New Field       | Default Value | Notes                          |
|:----------------|:--------------|:-------------------------------|
| FAMILY          | `Q10`         | 10-passenger family default    |
| VARIANT         | `GEN`         | General purpose (v5 PLUS → GEN)|
| VERSION         | `PLUS`        | Standard branding              |
| MODEL           | `BB`          | Body Brain integrated model    |
| ISSUE-REVISION  | `I01-R01`     | Initial issue/revision         |

### Migration Strategy

1. Run `scripts/generate_rename_map_v6.py` to create mapping
2. Review confidence scores (>0.95 auto-process, <0.80 manual review)
3. Execute batch rename with `scripts/execute_rename_v6.py`
4. Update cross-references with `scripts/update_cross_references_v6.py`
5. Validate with `validate_nomenclature.py --standard v6.0 --mode block`

---

## Tooling

### Validation
```bash
# Validate single file
python validate_nomenclature.py --standard v6.0 <filename>

# Validate all files (warn mode)
python validate_nomenclature.py --standard v6.0 --mode warn --check-all

# Validate all files (block mode - PR blocking)
python validate_nomenclature.py --standard v6.0 --mode block --check-all
```

### Scaffolding
```bash
# Generate new file with v6.0 format
python scripts/scaffold.py --standard v6.0 \
  <ATA_ROOT> <PROJECT> <PROGRAM> <FAMILY> <VARIANT> <VERSION> <MODEL> \
  <BLOCK> <PHASE> <KNOT_TASK> <AOR> <SUBJECT> <TYPE> <ISSUE-REVISION> <STATUS>

# Example:
python scripts/scaffold.py --standard v6.0 \
  27 AMPEL360 SPACET Q10 GEN PLUS BB OPS LC03 K06 SE \
  thermal-loop STD I01-R01 ACTIVE
```

---

## Governance

### Change Control Authority

**Configuration Management Working Group (CM WG)**

### Approval Required For

* New FAMILY values
* New VARIANT values
* New VERSION values
* New MODEL values
* New BLOCK values
* New AoR values
* New TYPE values
* New STATUS values
* New file extensions
* **New KNOT IDs** (requires standard upgrade, not just config change)

### Change Process

1. Submit change request to CM WG
2. CM WG reviews with impact assessment
3. Approval/rejection decision
4. Update `config/nomenclature/v6_0.yaml`
5. Update tooling (validator, scaffold)
6. Update specification document
7. Announce to stakeholders

---

## TEKNIA Credential Policy

### Credential Types
* `BADGE`
* `CERT`
* `LIC`

### Issuance Restriction
**Only CM or CERT AoR can issue credentials**

### Binding Requirements
* `subject_path`: Repo-relative path
* `subject_sha256`: SHA-256 hash
* `subject_commit`: Git commit (optional)

---

## Key Differences: v5.0 → v6.0

| Aspect                | v5.0                                | v6.0                                           |
|:----------------------|:------------------------------------|:-----------------------------------------------|
| **Total Fields**      | 12                                  | 16                                             |
| **Canonical Format**  | `...VARIANT_BLOCK_PHASE...`         | `...FAMILY_VARIANT_VERSION_MODEL_BLOCK_PHASE...`|
| **VARIANT Semantics** | Config variant (PLUS, CERT)         | Governance lane (GEN, BASELINE, CERT, etc.)    |
| **VERSION Field**     | Not present (was vNN at end)        | Branding reinforcer (PLUS, PLUSULTRA)          |
| **FAMILY Field**      | Not present                         | Quantum-inspired pax (Q10, Q100)               |
| **MODEL Field**       | Not present                         | Artifact domain (BB, HW, SW, PR)               |
| **Change Tracking**   | VERSION field (vNN)                 | ISSUE-REVISION (I##-R##)                       |
| **Validation Modes**  | Single mode (strict)                | Three modes (WARN, REPORT, BLOCK)              |

---

## Resources

* **Full Specification**: `docs/standards/NOMENCLATURE_v6_0_R1_0.md`
* **Config File**: `config/nomenclature/v6_0.yaml`
* **Validator**: `validate_nomenclature.py --standard v6.0`
* **Scaffold Tool**: `scripts/scaffold.py --standard v6.0`
* **Migration Tools**: `scripts/generate_rename_map_v6.py`, `scripts/execute_rename_v6.py`

---

## Contact

* **Questions**: Configuration Management WG
* **Change Requests**: Submit to CM WG via standard process
* **Issues**: Report via GitHub Issues with label `nomenclature-v6`

---

**Document Version**: v6.0 R1.0  
**Last Updated**: 2025-12-17  
**Status**: Normative  
**Owner**: Configuration Management WG
