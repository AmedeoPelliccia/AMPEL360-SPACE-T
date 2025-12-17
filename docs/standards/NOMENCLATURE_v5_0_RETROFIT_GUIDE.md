# Nomenclature v5.0 Repository Retrofit Guide

## Overview

This guide documents the controlled execution plan for retrofitting the AMPEL360-SPACE-T repository from Nomenclature v4.0 to v5.0.

**Status:** Phase A (Spec) and Phase B (Tooling) are complete. Phase C (Retrofit) is ready for execution.

## Prerequisites (Completed)

- ✅ Nomenclature v5.0 standard published (`docs/standards/NOMENCLATURE_v5_0.md`)
- ✅ Config-driven validator implemented (`validate_nomenclature.py`)
- ✅ Scaffold script updated (`scripts/scaffold.py`)
- ✅ CI workflow updated
- ✅ Rename map generated (`rename_map_v5.csv`)

## Retrofit Scope

**Files to rename:** 1,395 files  
**All files require review** due to:
- K00 → K01-K14 mapping (requires domain knowledge)
- STATUS field assignment (requires context)
- BUCKET → BLOCK semantic mapping

## Phased Execution Plan

### Phase C.1: Manual Review (Required)

**Goal:** Review and refine rename map entries

**Actions:**
1. Open `rename_map_v5.csv`
2. For each entry with `requires_review=YES`:
   - Verify KNOT mapping (K00 → K##)
   - Verify STATUS assignment
   - Verify BLOCK mapping
   - Adjust `new_path` if needed
   - Update `confidence` score
3. Mark entries ready for automated processing

**High-priority review categories:**
- Certification artifacts (K00 → K01)
- Safety artifacts (K00 → K02) 
- CM/configuration artifacts (K00 → K04)
- Lifecycle control artifacts (decide on KNOT)

**Estimated time:** 2-4 hours (can be distributed across team)

### Phase C.2: Incremental Execution (Controlled)

**Goal:** Execute renames in controlled batches

**Batch strategy:**
1. **Batch 1: High confidence (≥0.80)** - K01-K14 files with clear mappings
2. **Batch 2: Documentation** - Standards, guides, references
3. **Batch 3: Portal/Knot indexes** - Structural files
4. **Batch 4: Domain artifacts** - Technical artifacts by AoR
5. **Batch 5: Remaining files** - Final cleanup

**Safety controls per batch:**
- Run on feature branch
- Generate Git commit per batch
- Run validator after each batch
- Checkpoint before next batch

**Execution script:** `scripts/execute_rename_v5.py` (to be created)

### Phase C.3: Cross-Reference Update

**Goal:** Update all internal links and references

**Files to update:**
- Markdown links (`[text](path)`)
- Portal indexes (`*.md` with file lists)
- Knot indexes (`K##_*_index_*.md`)
- JSON/YAML manifests (`*.json`, `*.yaml` with path references)

**Script:** `scripts/update_cross_references_v5.py` (to be created)

**Process:**
1. Parse rename_map_v5.csv
2. Build old → new path lookup
3. Search/replace in all affected files
4. Validate links after update

### Phase C.4: Verification & Reporting

**Goal:** Verify complete compliance and document results

**Verification steps:**
1. Run validator: `python validate_nomenclature.py --check-all`
   - Target: 0 violations
2. Run link checker (if available)
   - Target: 0 broken internal links
3. Run CI pipeline
   - Target: All checks pass
4. Generate retrofit report

**Report contents:**
- Total files renamed
- Breakdown by batch
- K00 → K## mapping distribution
- STATUS field distribution
- Exceptions (if any)
- Broken links fixed
- Validator results

## Execution Commands

### Generate Rename Map (Completed)
```bash
python scripts/generate_rename_map_v5.py
```

### Review Rename Map
```bash
# Open in spreadsheet editor for review
open rename_map_v5.csv  # macOS
xdg-open rename_map_v5.csv  # Linux
start rename_map_v5.csv  # Windows
```

### Execute Rename (Batch)
```bash
# Create execution script first
# Then run per batch:
python scripts/execute_rename_v5.py --batch 1 --dry-run
python scripts/execute_rename_v5.py --batch 1  # Execute after dry-run review
```

### Update Cross-References
```bash
python scripts/update_cross_references_v5.py --dry-run
python scripts/update_cross_references_v5.py  # Execute after dry-run review
```

### Verify Compliance
```bash
python validate_nomenclature.py --check-all --strict
```

## Risk Mitigation

### Rollback Plan
1. **Branch-based execution** - All work on feature branch
2. **Batch commits** - Each batch is a separate commit
3. **Rename map preservation** - `rename_map_v5.csv` is source of truth
4. **Revert capability** - Can revert individual batch commits
5. **Backup recommendation** - Tag repo state before starting

### High-Impact Areas
- **Portal indexes** - Many cross-references
- **Knot catalogs** - Structural dependencies
- **CI configuration** - May reference specific files
- **Documentation** - External links may exist

### Manual Verification Required
- External documentation referencing old filenames
- External tools/scripts referencing old paths
- Bookmarks and saved links
- Git history and commits (old paths will still work in history)

## Timeline Estimate

- **Phase C.1 (Review):** 2-4 hours (distributed)
- **Phase C.2 (Execution):** 1-2 hours (incremental)
- **Phase C.3 (Cross-refs):** 1-2 hours (automated + verification)
- **Phase C.4 (Verification):** 1 hour
- **Total:** 5-9 hours (can span multiple sessions)

## Decision Points

### Immediate Execution vs. Scheduled

**Option A: Execute now (recommended for development)**
- Minimal disruption (single repo, controlled)
- Allows immediate v5.0 compliance
- Clean slate for new development

**Option B: Schedule for milestone**
- Coordinate with release cycle
- Bundle with other breaking changes
- Communicate to all stakeholders

### Incremental vs. Big Bang

**Recommended: Incremental (batched)**
- Lower risk per batch
- Easier to verify
- Can pause/adjust between batches
- Better Git history

**Not recommended: Big Bang**
- High risk
- Difficult to verify
- Single large commit
- Harder to rollback partially

## Post-Retrofit Actions

1. **Announce completion** to all stakeholders
2. **Update CI/CD** to enforce v5.0 only
3. **Update documentation** to reference v5.0 standard
4. **Archive v4.0 artifacts** (standard, old scripts)
5. **Update training materials** for new nomenclature

## Support & Escalation

For issues during retrofit:
1. **Stop current batch** if errors occur
2. **Review error** in rename map or scripts
3. **Fix and rerun** current batch
4. **Document exception** if manual intervention needed
5. **Escalate to CM WG** for governance decisions (new knots, ambiguous mappings)

## Status Tracking

Track progress in this document or a separate tracking sheet:

- [ ] Phase C.1: Manual review completed
- [ ] Phase C.2: Batch 1 executed
- [ ] Phase C.2: Batch 2 executed
- [ ] Phase C.2: Batch 3 executed
- [ ] Phase C.2: Batch 4 executed
- [ ] Phase C.2: Batch 5 executed
- [ ] Phase C.3: Cross-references updated
- [ ] Phase C.4: Verification passed
- [ ] Phase C.4: Report generated

---

**Last Updated:** 2025-12-17  
**Version:** 1.0  
**Author:** CM WG (via Copilot)
