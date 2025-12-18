# BLOCK Field Migration Guide: Legacy to Domain Partitions (B## Format)

**Date**: 2025-12-17  
**Status**: Normative  
**Owner**: Configuration Management WG  
**Related**: OPTINS Framework v1.1, Nomenclature Standard v6.0 R1.0

---

## 1. Overview

This document provides guidance for migrating from legacy BLOCK abbreviations (OPS, STR, AI, etc.) to the new domain partition system (B00-B90) aligned with the OPTINS Framework v1.1.

### Why This Change?

1. **Alignment with OPTINS Framework**: The B## format directly maps to OPTINS domain partitions
2. **Semantic Clarity**: Domain partitions have clear, defined meanings across programs
3. **Solution Pack Support**: Enables versioned solution packs (COM, AIRT, SPACET)
4. **ATA_ROOT Validation**: Clear matrix defining valid BLOCK values per ATA_ROOT

### Key Changes

- **Old**: BLOCK used abbreviations (OPS, STR, PROP, AI, DATA, etc.)
- **New**: BLOCK uses B## format (B00, B10, B20, ..., B90)
- **Validation**: BLOCK values must be valid for the given ATA_ROOT per ATA_PARTITION_MATRIX

---

## 2. Domain Partition Table

The new BLOCK field represents domain partitions defined by the OPTINS Framework:

| BLOCK | Domain-Subsystem                                        | Environment Typical          | Legacy Mapping Hint       |
|------:|:--------------------------------------------------------|:-----------------------------|:--------------------------|
|   B00 | GENERAL (universal, implicit)                           | all                          | GEN (partially)           |
|   B10 | OPERATIONAL SYSTEMS                                     | onboard/offboard/simtest     | OPS, CERT, SAF, SYS, TEST, MRO |
|   B20 | CYBERSECURITY                                           | digital + onboard            | AI (partially), SW (partially) |
|   B30 | DATA, COMMS AND REGISTRY                                | digital + onboard            | DATA                      |
|   B40 | PHYSICS (pressure/thermal/cryo/…)                       | onboard + simtest            | (new semantic)            |
|   B50 | PHYSICAL (aerostructures + info HW)                     | onboard/offboard             | STR, HW, STOR             |
|   B60 | DYNAMICS (thrust/drag-lift/balancing/attitude/inerting) | onboard + simtest            | PROP                      |
|   B70 | RECIPROCITY & ALTERNATIVE ENGINES                       | onboard + simtest            | (new semantic)            |
|   B80 | RENEWABLE ENERGY & CIRCULARITY                          | onboard + offboard           | CIRC, ENRG                |
|   B90 | CONNECTIONS & MAPPING                                   | digital + onboard            | (new semantic)            |

**Note**: B00 is universal and implicit - always valid for all ATA_ROOT values.

---

## 3. Legacy BLOCK Mapping

The following table provides **suggested** mappings from legacy BLOCK abbreviations to new B## format. **These are guidelines only** - actual migration requires manual review based on ATA_ROOT and semantic context.

### General Mapping Table

| Legacy BLOCK | Suggested B## | Rationale                                    | Notes                          |
|:-------------|:--------------|:---------------------------------------------|:-------------------------------|
| **OPS**      | B10           | Operational systems and procedures           | Most common mapping            |
| **STR**      | B50           | Structures are physical artifacts            | Physical domain                |
| **PROP**     | B60           | Propulsion involves dynamics                 | Dynamics domain                |
| **AI**       | B20           | AI/ML systems fall under cybersecurity       | Digital security focus         |
| **DATA**     | B30           | Data management and communications           | Direct mapping                 |
| **CERT**     | B10           | Certification is operational governance      | Operational systems            |
| **SAF**      | B10           | Safety is operational governance             | Operational systems            |
| **SW**       | B20           | Software systems involve cybersecurity       | Digital security focus         |
| **HW**       | B50           | Hardware is physical                         | Physical domain                |
| **SYS**      | B10           | Systems engineering is operational           | Operational systems            |
| **TEST**     | B10           | Testing/IVVQ is operational                  | Operational systems            |
| **MRO**      | B10           | MRO/maintenance is operational               | Operational systems            |
| **CIRC**     | B80           | Circularity maps to renewable energy         | Direct mapping                 |
| **ENRG**     | B80           | Energy systems                               | Direct mapping                 |
| **STOR**     | B50           | Storage is physical infrastructure           | Physical domain                |
| **GEN**      | B10           | General/cross-cutting is operational         | Operational systems            |

### Context-Dependent Mapping

Some legacy BLOCK values may map to different B## values depending on ATA_ROOT and context:

#### AI/ML Systems
- **ATA 95-96** (AI governance, registries): **B20** (Cybersecurity) or **B30** (Data/Registry)
- **ATA 22** (Autoflight/GNC with AI): **B60** (Dynamics) if dynamics-focused
- **ATA 42** (IMA/Compute with AI): **B20** (Cybersecurity)

#### Software Systems
- **General software artifacts**: **B20** (Cybersecurity)
- **Software in specific physical systems**: May be **B50** (Physical) or **B60** (Dynamics)

#### Hardware Systems
- **Physical structures**: **B50** (Physical)
- **Hardware with dynamics focus**: **B60** (Dynamics)
- **Hardware with energy focus**: **B80** (Renewable Energy)

---

## 4. Migration Process

### Step 1: Identify Current Files

```bash
# Find all files with legacy BLOCK format
find . -type f -name "*_OPS_*" -o -name "*_STR_*" -o -name "*_AI_*" | grep -v ".git"
```

### Step 2: Review ATA_PARTITION_MATRIX

Before migrating, consult `config/nomenclature/ATA_PARTITION_MATRIX.yaml` to determine:
1. Which BLOCK values are valid for the ATA_ROOT
2. Whether a Solution Pack (COM, AIRT, SPACET) designation applies
3. The semantic intent of the artifact

### Step 3: Determine Correct B## Value

**Process:**

1. **Extract ATA_ROOT** from filename
2. **Consult ATA_PARTITION_MATRIX** for valid BLOCK values for that ATA_ROOT
3. **Review artifact content** to understand semantic intent
4. **Select appropriate B##** value based on:
   - Domain partition semantics
   - ATA_ROOT applicability
   - Artifact content and purpose

### Step 4: Update Filename

**Manual rename** or use migration script:

```bash
# Example: Rename with new BLOCK format
mv "27_AMPEL360_SPACET_Q10_GEN_PLUS_BB_OPS_LC03_K06_SE__thermal-loop_STD_I01-R01_ACTIVE.md" \
   "27_AMPEL360_SPACET_Q10_GEN_PLUS_BB_B10_LC03_K06_SE__thermal-loop_STD_I01-R01_ACTIVE.md"
```

### Step 5: Update Internal References

After renaming, update any internal references, links, or documentation:

```bash
# Update internal links (use with caution)
grep -r "27_AMPEL360_SPACET_Q10_GEN_PLUS_BB_OPS_" . --exclude-dir=.git
```

### Step 6: Validate

```bash
# Validate with new nomenclature standard
python validate_nomenclature.py --standard v6.0 <filename>
```

---

## 5. Migration Examples

### Example 1: Operational Systems (OPS → B10)

**Before:**
```
27_AMPEL360_SPACET_Q10_GEN_PLUS_BB_OPS_LC03_K06_SE__thermal-loop_STD_I01-R01_ACTIVE.md
```

**After:**
```
27_AMPEL360_SPACET_Q10_GEN_PLUS_BB_B10_LC03_K06_SE__thermal-loop_STD_I01-R01_ACTIVE.md
```

**Rationale**: ATA 27 (Flight Controls) allows B10 (Operational Systems) per ATA_PARTITION_MATRIX.

### Example 2: Structures (STR → B50)

**Before:**
```
53_AMPEL360_SPACET_Q100_CERT_PLUS_HW_STR_LC07_K02_CERT__pressure-bulkhead-trade_RPT_I02-R01_DRAFT.pdf
```

**After:**
```
53_AMPEL360_SPACET_Q100_CERT_PLUS_HW_B50_LC07_K02_CERT__pressure-bulkhead-trade_RPT_I02-R01_DRAFT.pdf
```

**Rationale**: ATA 53 (Structures) allows B50 (Physical) per ATA_PARTITION_MATRIX.

### Example 3: AI/ML (AI → B20)

**Before:**
```
95_AMPEL360_SPACET_Q10_BASELINE_PLUS_SW_AI_SB04_K11_CM__model-card-template_STD_I01-R01_TEMPLATE.md
```

**After:**
```
95_AMPEL360_SPACET_Q10_BASELINE_PLUS_SW_B20_SB04_K11_CM__model-card-template_STD_I01-R01_TEMPLATE.md
```

**Rationale**: ATA 95 (SBOM/BOM exports) allows B20 (Cybersecurity) per ATA_PARTITION_MATRIX. AI governance falls under cybersecurity domain.

### Example 4: Data Governance (DATA → B30)

**Before:**
```
00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_DATA_LC01_K05_DATA__governance-reference-policy_STD_I01-R01_ACTIVE.md
```

**After:**
```
00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_B30_LC01_K05_DATA__governance-reference-policy_STD_I01-R01_ACTIVE.md
```

**Rationale**: ATA 00 (General) allows B30 (Data, Comms and Registry) per ATA_PARTITION_MATRIX.

### Example 5: Propulsion (PROP → B60)

**Before:**
```
71_AMPEL360_SPACET_Q10_GEN_PLUS_HW_PROP_LC05_K03_SE__engine-performance-analysis_ANA_I01-R01_ACTIVE.md
```

**After:**
```
71_AMPEL360_SPACET_Q10_GEN_PLUS_HW_B60_LC05_K03_SE__engine-performance-analysis_ANA_I01-R01_ACTIVE.md
```

**Rationale**: ATA 71 (Propulsion family) allows B60 (Dynamics) per ATA_PARTITION_MATRIX.

---

## 6. Edge Cases and Special Considerations

### 6.1 Multi-Domain Artifacts

Some artifacts span multiple domains. Choose the **primary** domain based on:
1. **Subject matter emphasis** in the artifact
2. **ATA_ROOT semantic focus**
3. **Stakeholder intent**

**Example**: A thermal management system for propulsion
- Could be **B40** (Physics) if thermal analysis is primary
- Could be **B60** (Dynamics) if propulsion integration is primary
- **Decision**: Review artifact content and consult with domain experts

### 6.2 Invalid BLOCK for ATA_ROOT

If your current BLOCK maps to a B## value that is **not valid** for the ATA_ROOT:

1. **Re-evaluate ATA_ROOT**: Is the file in the correct ATA chapter?
2. **Re-evaluate semantic intent**: Does the artifact's purpose align with available BLOCK values?
3. **Escalate to CM WG**: If no valid mapping exists, this may indicate a gap in the ATA_PARTITION_MATRIX

### 6.3 Solution Pack Designation

Some ATA_ROOT + BLOCK combinations have distinct Solution Packs:
- **COM**: Common baseline (AIRT + SPACET)
- **AIRT**: AIRT-only addendum
- **SPACET**: SPACET-only addendum

**Example**: ATA 18 (Noise & Vibration), B60 (Dynamics)
- **COM**: Common dynamics baseline
- **AIRT-only**: Airport/community noise focus
- **SPACET-only**: Launch/reentry vibro-acoustics focus

**Action**: Determine if your artifact should reference a specific Solution Pack in documentation or metadata.

---

## 7. Validation and Compliance

### 7.1 Nomenclature Validation

After migration, all files **must** pass v6.0 nomenclature validation:

```bash
python validate_nomenclature.py --standard v6.0 --check-all
```

### 7.2 ATA_PARTITION_MATRIX Compliance

CI must validate that BLOCK values are valid for the given ATA_ROOT:

```python
# Example validation logic
def validate_block_for_ata_root(ata_root, block):
    matrix = load_ata_partition_matrix()
    valid_blocks = matrix.get(ata_root, {}).get('blocks', [])
    
    if block not in valid_blocks:
        raise ValueError(f"BLOCK {block} not valid for ATA_ROOT {ata_root}")
```

### 7.3 Traceability Updates

Update traceability matrices and cross-references to reflect new filenames:

```bash
# Example: Update traceability matrix
python scripts/update_cross_references_v6.py
```

---

## 8. Rollout Plan

### Phase 1: Documentation and Config (COMPLETE)
- [x] Create ATA_PARTITION_MATRIX.yaml
- [x] Update config/nomenclature/v6_0.yaml
- [x] Update documentation (NOMENCLATURE_v6_0_R1_0.md, QUICKREF)
- [x] Create this migration guide

### Phase 2: Tooling Updates (IN PROGRESS)
- [ ] Update validate_nomenclature.py for B## validation
- [ ] Update scaffold_v6.py for B## support
- [ ] Add ATA_PARTITION_MATRIX validation to PLC gates
- [ ] Update CI/CD workflows

### Phase 3: Pilot Migration (PLANNED)
- [ ] Select pilot artifacts (e.g., 10-20 files per ATA family)
- [ ] Perform manual migration with CM WG oversight
- [ ] Validate and document lessons learned
- [ ] Update migration guide based on findings

### Phase 4: Bulk Migration (PLANNED)
- [ ] Develop automated migration script (with manual review)
- [ ] Migrate artifacts by ATA family (O, I, T, N, S axes)
- [ ] Update internal links and references
- [ ] Validate all migrated files

### Phase 5: Validation and Release (PLANNED)
- [ ] Full repository validation
- [ ] Update all traceability matrices
- [ ] Communicate to stakeholders
- [ ] Release updated repository baseline

---

## 9. Tools and Scripts

### Migration Script (Planned)

A semi-automated migration script will be developed:

```bash
# Usage (planned)
python scripts/migrate_block_to_b##.py --file <filename> --review
python scripts/migrate_block_to_b##.py --ata-root 27 --batch --review
```

**Features**:
- ATA_PARTITION_MATRIX lookup
- Suggested B## value based on legacy BLOCK
- Manual review and confirmation
- Batch processing with logging
- Rollback support

### Validation Script (Enhanced)

Enhanced validation to check ATA_PARTITION_MATRIX compliance:

```bash
python validate_nomenclature.py --standard v6.0 --check-matrix <filename>
```

---

## 10. FAQ

### Q1: Can I continue using legacy BLOCK abbreviations?

**A**: No. Legacy BLOCK abbreviations (OPS, STR, AI, etc.) are **deprecated** and not valid in v6.0 R1.0. All new files and migrated files must use B## format.

### Q2: What if multiple B## values seem applicable?

**A**: 
1. Consult ATA_PARTITION_MATRIX for valid BLOCK values for the ATA_ROOT
2. Review artifact content to determine primary domain
3. Escalate to CM WG if uncertain

### Q3: Do I need to update existing files immediately?

**A**: Migration will be phased. Critical path artifacts and new files must use B## format. Bulk migration will be scheduled and communicated.

### Q4: What happens if I use an invalid BLOCK for an ATA_ROOT?

**A**: CI validation will fail. The file will not pass nomenclature validation and cannot be merged.

### Q5: Where can I get help with migration?

**A**: Contact the Configuration Management WG via CM portal entry point or open an issue with the `nomenclature-migration` label.

---

## 11. References

- **OPTINS Framework v1.1**: OPT-IN Framework specification
- **Nomenclature Standard v6.0 R1.0**: `docs/standards/NOMENCLATURE_v6_0_R1_0.md`
- **Quick Reference**: `docs/standards/NOMENCLATURE_v6_0_R1_0_QUICKREF.md`
- **ATA_PARTITION_MATRIX**: `config/nomenclature/ATA_PARTITION_MATRIX.yaml`
- **Config**: `config/nomenclature/v6_0.yaml`

---

## 12. Contact

**Configuration Management WG**
- **Entry Point**: STK_CM portal
- **Issues**: GitHub Issues with `nomenclature-migration` label
- **Urgent**: Contact @AmedeoPelliccia or CM WG leads

---

**Document Status**: ACTIVE  
**Next Review**: After Phase 3 (Pilot Migration)  
**Change Control**: CM WG approval required for updates
