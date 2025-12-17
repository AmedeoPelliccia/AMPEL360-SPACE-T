#!/usr/bin/env python3
"""
AMPEL360 Space-T Repository Inventory Generator
================================================
Generates an inventory report of current nomenclature compliance status.

This tool:
1. Scans all files in the repository
2. Validates against both v5.0 and R1.0 standards
3. Categorizes violations by type
4. Estimates rename volume for v5.0 → R1.0 migration
5. Identifies top offenders

Usage:
    python scripts/generate_inventory_report.py
    python scripts/generate_inventory_report.py --output reports/inventory.md
"""

import sys
import argparse
from pathlib import Path
from datetime import date
from collections import defaultdict, Counter

# Add parent directory to path to import validator
sys.path.insert(0, str(Path(__file__).parent.parent))
from validate_nomenclature import NomenclatureValidator


def generate_inventory_report(output_file: str = None):
    """Generate comprehensive inventory report."""
    
    print("Generating nomenclature inventory report...")
    print("="*60)
    
    # Initialize validators
    validator_v5 = NomenclatureValidator(standard="v5.0", strict=True)
    validator_r1 = NomenclatureValidator(standard="R1.0", strict=True)
    
    # Scan repository
    repo_root = Path.cwd()
    print(f"Scanning repository: {repo_root}")
    
    results_v5 = validator_v5.validate_directory(repo_root, recursive=True)
    results_r1 = validator_r1.validate_directory(repo_root, recursive=True)
    
    # Categorize results
    v5_violations = defaultdict(list)
    r1_violations = defaultdict(list)
    
    for result in results_v5:
        if not result.valid:
            for error in result.errors:
                # Categorize error
                if "does not match required pattern" in error:
                    v5_violations["pattern_mismatch"].append(result.filename)
                elif "Invalid KNOT" in error:
                    v5_violations["invalid_knot"].append(result.filename)
                elif "Invalid AoR" in error:
                    v5_violations["invalid_aor"].append(result.filename)
                elif "ATA_ROOT" in error:
                    v5_violations["ata_root_padding"].append(result.filename)
                elif "Invalid VARIANT" in error:
                    v5_violations["invalid_variant"].append(result.filename)
                elif "Invalid BLOCK" in error:
                    v5_violations["invalid_block"].append(result.filename)
                elif "Invalid PHASE" in error:
                    v5_violations["invalid_phase"].append(result.filename)
                elif "Invalid TYPE" in error:
                    v5_violations["invalid_type"].append(result.filename)
                elif "Invalid STATUS" in error:
                    v5_violations["invalid_status"].append(result.filename)
                elif "VERSION" in error:
                    v5_violations["invalid_version"].append(result.filename)
                else:
                    v5_violations["other"].append(result.filename)
    
    for result in results_r1:
        if not result.valid:
            for error in result.errors:
                # Categorize error
                if "does not match required pattern" in error:
                    r1_violations["pattern_mismatch"].append(result.filename)
                elif "Invalid MODEL" in error:
                    r1_violations["missing_model"].append(result.filename)
                elif "VERSION" in error and "BL|TS|GN" in error:
                    r1_violations["invalid_version_format"].append(result.filename)
                elif "ISSUE-REVISION" in error:
                    r1_violations["missing_issue_revision"].append(result.filename)
                elif "Invalid KNOT" in error:
                    r1_violations["invalid_knot"].append(result.filename)
                elif "Invalid AoR" in error:
                    r1_violations["invalid_aor"].append(result.filename)
                else:
                    r1_violations["other"].append(result.filename)
    
    # Count totals
    v5_valid = sum(1 for r in results_v5 if r.valid)
    v5_invalid = sum(1 for r in results_v5 if not r.valid)
    r1_valid = sum(1 for r in results_r1 if r.valid)
    r1_invalid = sum(1 for r in results_r1 if not r.valid)
    total_scanned = len(results_v5)
    
    # Estimate rename volume (files that are v5 compliant but need R1.0 update)
    rename_candidates = v5_valid
    
    # Generate report content
    report_lines = []
    report_lines.append("# AMPEL360 Space-T Nomenclature Inventory Report")
    report_lines.append("")
    report_lines.append(f"**Generated:** {date.today()}")
    report_lines.append(f"**Repository:** {repo_root}")
    report_lines.append("")
    report_lines.append("---")
    report_lines.append("")
    
    # Executive Summary
    report_lines.append("## Executive Summary")
    report_lines.append("")
    report_lines.append(f"- **Total files scanned:** {total_scanned}")
    report_lines.append(f"- **v5.0 compliant:** {v5_valid} ({v5_valid/total_scanned*100:.1f}%)")
    report_lines.append(f"- **v5.0 violations:** {v5_invalid} ({v5_invalid/total_scanned*100:.1f}%)")
    report_lines.append(f"- **R1.0 compliant:** {r1_valid} ({r1_valid/total_scanned*100:.1f}%)")
    report_lines.append(f"- **R1.0 violations:** {r1_invalid} ({r1_invalid/total_scanned*100:.1f}%)")
    report_lines.append(f"- **Estimated renames for R1.0:** ~{rename_candidates} files")
    report_lines.append("")
    
    # v5.0 Violations Breakdown
    report_lines.append("## v5.0 Violations by Category")
    report_lines.append("")
    if v5_violations:
        report_lines.append("| Category | Count | Files |")
        report_lines.append("|----------|-------|-------|")
        for category, files in sorted(v5_violations.items(), key=lambda x: len(x[1]), reverse=True):
            unique_files = list(set(files))
            count = len(unique_files)
            files_preview = ", ".join(unique_files[:3])
            if count > 3:
                files_preview += f" ... (+{count-3} more)"
            report_lines.append(f"| {category.replace('_', ' ').title()} | {count} | {files_preview} |")
        report_lines.append("")
    else:
        report_lines.append("✅ No v5.0 violations detected!")
        report_lines.append("")
    
    # R1.0 Violations Breakdown
    report_lines.append("## R1.0 Violations by Category")
    report_lines.append("")
    if r1_violations:
        report_lines.append("| Category | Count | Files |")
        report_lines.append("|----------|-------|-------|")
        for category, files in sorted(r1_violations.items(), key=lambda x: len(x[1]), reverse=True):
            unique_files = list(set(files))
            count = len(unique_files)
            files_preview = ", ".join(unique_files[:3])
            if count > 3:
                files_preview += f" ... (+{count-3} more)"
            report_lines.append(f"| {category.replace('_', ' ').title()} | {count} | {files_preview} |")
        report_lines.append("")
    else:
        report_lines.append("✅ No R1.0 violations detected!")
        report_lines.append("")
    
    # Top Offenders (most violations)
    report_lines.append("## Top Offenders")
    report_lines.append("")
    report_lines.append("Files with the most violations:")
    report_lines.append("")
    
    # Count violations per file
    file_violation_counts = Counter()
    for result in results_v5:
        if not result.valid:
            file_violation_counts[result.filename] += len(result.errors)
    
    if file_violation_counts:
        report_lines.append("| File | Violation Count |")
        report_lines.append("|------|-----------------|")
        for filename, count in file_violation_counts.most_common(20):
            report_lines.append(f"| `{filename}` | {count} |")
        report_lines.append("")
    else:
        report_lines.append("✅ No violations!")
        report_lines.append("")
    
    # Migration Strategy
    report_lines.append("## v5.0 → R1.0 Migration Strategy")
    report_lines.append("")
    report_lines.append("### Required Changes")
    report_lines.append("")
    report_lines.append("1. **Add MODEL field** (after PROGRAM)")
    report_lines.append("   - Default: `GEN` for generic artifacts")
    report_lines.append("   - Use `Q10` for SPACE-T specific (10 passengers)")
    report_lines.append("   - Use `Q100` for AIR-T specific (100 passengers)")
    report_lines.append("")
    report_lines.append("2. **Update VERSION format**")
    report_lines.append("   - `v01` → `BL01` (baseline)")
    report_lines.append("   - `v02` → `BL02` (baseline)")
    report_lines.append("   - Use `TS##` for testing versions")
    report_lines.append("   - Use `GN##` for generated versions")
    report_lines.append("")
    report_lines.append("3. **Add ISSUE-REVISION field** (before STATUS)")
    report_lines.append("   - Default: `I00-R00` for non-issue artifacts")
    report_lines.append("   - Use actual issue numbers where applicable")
    report_lines.append("")
    report_lines.append("### Example Mappings")
    report_lines.append("")
    report_lines.append("```")
    report_lines.append("v5.0:")
    report_lines.append("  00_AMPEL360_SPACET_PLUS_GEN_LC01_K04_CM__nomenclature-standard_STD_v01_ACTIVE.md")
    report_lines.append("")
    report_lines.append("R1.0:")
    report_lines.append("  00_AMPEL360_SPACET_GEN_PLUS_BL01_GEN_LC01_K04_CM__nomenclature-standard_STD_I00-R00_ACTIVE.md")
    report_lines.append("  └─ Added: MODEL=GEN, VERSION=BL01 (was v01), ISSUE-REVISION=I00-R00")
    report_lines.append("```")
    report_lines.append("")
    
    # Recommendations
    report_lines.append("## Recommendations")
    report_lines.append("")
    report_lines.append("1. **Fix v5.0 violations first** before migrating to R1.0")
    report_lines.append("2. **Use automated rename tools** (`generate_rename_map_v6.py` + `execute_rename_v6.py`)")
    report_lines.append("3. **Review low-confidence mappings manually**")
    report_lines.append("4. **Update cross-references** after renaming")
    report_lines.append("5. **Validate with R1.0 validator** after migration")
    report_lines.append("")
    report_lines.append("---")
    report_lines.append("")
    report_lines.append("**Next Steps:**")
    report_lines.append("")
    report_lines.append("- [ ] Review this inventory report")
    report_lines.append("- [ ] Fix v5.0 violations (if any)")
    report_lines.append("- [ ] Generate rename map for R1.0 migration")
    report_lines.append("- [ ] Execute PR^3-2 (Retrofit)")
    report_lines.append("")
    
    # Write report
    report_content = "\n".join(report_lines)
    
    if output_file:
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w') as f:
            f.write(report_content)
        print(f"\n✅ Report written to: {output_path}")
    else:
        print("\n" + report_content)
    
    print("\n" + "="*60)
    print("Inventory report generation complete!")
    
    return report_content


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Generate nomenclature inventory report for AMPEL360 Space-T'
    )
    parser.add_argument(
        '--output',
        '-o',
        metavar='FILE',
        help='Output file path (default: print to stdout)'
    )
    
    args = parser.parse_args()
    
    try:
        generate_inventory_report(output_file=args.output)
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return 2


if __name__ == '__main__':
    sys.exit(main())
