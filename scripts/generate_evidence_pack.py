#!/usr/bin/env python3
"""
AMPEL360 Space-T Evidence Pack Generator
=========================================
Version: 1.0
Date: 2025-12-16

Generates automated, reproducible evidence packs for certification and audit purposes.
Scans repository for evidence artifacts, computes integrity hashes, and produces
manifest JSON + summary report following nomenclature standard v3.0.

Usage:
    python scripts/generate_evidence_pack.py --knot K06 --ata 00 [OPTIONS]

Options:
    --knot KNOT_ID        Knot identifier (e.g., K01, K06)
    --ata ATA_CODE        ATA code (e.g., 00, 72, 110)
    --output-dir DIR      Output directory for generated files (default: current dir)
    --repo-root DIR       Repository root path (default: .)
    --scan-patterns FILE  JSON file with scan patterns (optional)
    --dry-run             Show what would be generated without writing files
    --verbose             Verbose output
    --force               Overwrite existing files

Consumes:
    - Evidence pack schema (AMPEL360-SPACE-T-PORTAL/.../00_00_SCH_LC01_AMPEL360_SPACET_PLUS_k01-ata-00-evidence-pack-manifest_v01.json)
    - CM's evidence requirements (nomenclature standard, file patterns)

Produces:
    - Evidence pack manifest (JSON)
    - Evidence pack summary report (Markdown)
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from dataclasses import dataclass, field, asdict
from datetime import date, datetime
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple

# Nomenclature pattern for 10-field format
NOMENCLATURE_PATTERN = re.compile(
    r'^(?P<root>\d{2,3})_'
    r'(?P<bucket>00|10|20|30|40|50|60|70|80|90)_'
    r'(?P<type>[A-Z0-9]{2,8})_'
    r'(?P<subject>(LC(0[1-9]|1[0-4])|SB(1[5-9]|[2-9]\d)))_'
    r'(?P<project>AMPEL360)_'
    r'(?P<program>SPACET)_'
    r'(?P<variant>[A-Z0-9]+(?:-[A-Z0-9]+)*)_'
    r'(?P<desc>[a-z0-9]+(?:-[a-z0-9]+)*)_'
    r'(?P<ver>v\d{2})'
    r'\.(?P<ext>[a-z0-9]{1,6})$'
)

# Artifact type to role mapping
ARTIFACT_ROLE_MAP = {
    'REQ': 'requirement',
    'ACT': 'acceptance_criteria',
    'MIN': 'decision',
    'RPT': 'report',
    'IDX': 'evidence',
    'TRC': 'traceability',
    'SCH': 'schema',
    'TAB': 'table',
    'DIA': 'diagram',
    'STD': 'evidence',
    'LOG': 'evidence',
    'PLAN': 'evidence',
    'FHA': 'evidence',
    'PSSA': 'evidence',
    'SSA': 'evidence',
    'FTA': 'evidence',
    'ANA': 'evidence',
    'DAL': 'evidence',
    'CAT': 'evidence',
    'LST': 'evidence',
    'GLO': 'evidence',
    'MAT': 'evidence',
}

# Default scan patterns for evidence discovery
DEFAULT_SCAN_PATTERNS = [
    # Root level governance and standards
    "00_00_*_LC*_AMPEL360_SPACET_*_v*.md",
    "00_00_*_LC*_AMPEL360_SPACET_*_v*.json",
    # ATA-specific evidence in portal
    "AMPEL360-SPACE-T-PORTAL/**/EVIDENCE/*.md",
    "AMPEL360-SPACE-T-PORTAL/**/EVIDENCE/*.json",
    "AMPEL360-SPACE-T-PORTAL/**/TASKS/*.md",
    # Schemas
    "*_90_SCH_*_v*.json",
    # CI workflows
    ".github/workflows/*.yml",
]

# Files and directories to exclude
EXCLUDE_PATTERNS = [
    r'\.git/',
    r'node_modules/',
    r'__pycache__/',
    r'\.pytest_cache/',
    r'templates/',  # Template files
    r'scripts/',    # Script files (except for evidence)
]


@dataclass
class NomenclatureComponents:
    """Parsed nomenclature components from filename."""
    root: str
    bucket: str
    type: str
    subject: str
    project: str
    program: str
    variant: str
    description: str
    version: str
    ext: str


@dataclass
class EvidenceItem:
    """Single evidence item in a pack."""
    path: str
    artifact_role: str
    nomenclature: Dict[str, str]
    hashes: Dict[str, str]
    linked_criteria: List[str] = field(default_factory=list)
    linked_tasks: List[str] = field(default_factory=list)
    source_refs: Dict[str, List[str]] = field(default_factory=dict)


def compute_sha256(filepath: Path) -> Optional[str]:
    """Compute SHA256 hash of a file. Returns None if file cannot be read."""
    sha256_hash = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256_hash.update(chunk)
        return sha256_hash.hexdigest()
    except (FileNotFoundError, PermissionError, OSError) as e:
        print(f"Warning: Could not compute SHA256 for {filepath}: {e}", file=sys.stderr)
        return None


def parse_nomenclature(filename: str) -> Optional[NomenclatureComponents]:
    """Parse filename into nomenclature components."""
    match = NOMENCLATURE_PATTERN.match(filename)
    if not match:
        return None
    return NomenclatureComponents(
        root=match.group('root'),
        bucket=match.group('bucket'),
        type=match.group('type'),
        subject=match.group('subject'),
        project=match.group('project'),
        program=match.group('program'),
        variant=match.group('variant'),
        description=match.group('desc'),
        version=match.group('ver'),
        ext=match.group('ext'),
    )


def is_excluded(path: Path) -> bool:
    """Check if path should be excluded from scanning."""
    path_str = path.as_posix()
    for pattern in EXCLUDE_PATTERNS:
        if re.search(pattern, path_str):
            return True
    return False


def scan_for_evidence(
    repo_root: Path,
    knot_id: str,
    ata_code: str,
    patterns: Optional[List[str]] = None,
    verbose: bool = False
) -> List[Tuple[Path, NomenclatureComponents]]:
    """
    Scan repository for evidence artifacts matching the given knot and ATA.
    
    Returns list of (path, nomenclature_components) tuples.
    """
    if patterns is None:
        patterns = DEFAULT_SCAN_PATTERNS
    
    evidence_files: List[Tuple[Path, NomenclatureComponents]] = []
    seen_paths = set()
    
    for pattern in patterns:
        if verbose:
            print(f"Scanning pattern: {pattern}")
        
        # Use glob to find matching files
        for filepath in repo_root.glob(pattern):
            if not filepath.is_file():
                continue
            if is_excluded(filepath):
                continue
            
            rel_path = filepath.relative_to(repo_root)
            if rel_path in seen_paths:
                continue
            seen_paths.add(rel_path)
            
            # Check if filename matches nomenclature
            components = parse_nomenclature(filepath.name)
            
            # Filter by knot_id in filename - use word boundary matching to avoid false positives
            filename_no_ext = filepath.stem
            # Match knot_id as a discrete identifier (delimited by _ or - or start/end)
            knot_pattern = re.compile(r'(?i)(?:^|[_\-])' + re.escape(knot_id) + r'(?:[_\-]|$)')
            if knot_pattern.search(filename_no_ext):
                # Add to evidence list - components may be None for non-nomenclature files
                evidence_files.append((filepath, components))
                if verbose:
                    if components:
                        print(f"  Found: {rel_path}")
                    else:
                        print(f"  Found (non-nomenclature): {rel_path}")
    
    # Also scan for K-specific files anywhere in the repo
    knot_pattern = f"**/*{knot_id.lower()}*"
    for filepath in repo_root.glob(knot_pattern):
        if not filepath.is_file():
            continue
        if is_excluded(filepath):
            continue
        
        rel_path = filepath.relative_to(repo_root)
        if rel_path in seen_paths:
            continue
        seen_paths.add(rel_path)
        
        components = parse_nomenclature(filepath.name)
        if components:
            evidence_files.append((filepath, components))
            if verbose:
                print(f"  Found (knot match): {rel_path}")
    
    # Sort for reproducibility
    evidence_files.sort(key=lambda x: x[0].as_posix())
    
    return evidence_files


def create_evidence_item(
    repo_root: Path,
    filepath: Path,
    components: Optional[NomenclatureComponents]
) -> Optional[EvidenceItem]:
    """Create an EvidenceItem from a file path. Returns None if hash computation fails."""
    rel_path = filepath.relative_to(repo_root).as_posix()
    sha256 = compute_sha256(filepath)
    
    # Skip items where hash computation failed
    if sha256 is None:
        return None
    
    if components:
        artifact_role = ARTIFACT_ROLE_MAP.get(components.type, 'evidence')
        nomenclature = {
            'root': components.root,
            'bucket': components.bucket,
            'type': components.type,
            'lc_or_subbucket': components.subject,
            'project': components.project,
            'program': components.program,
            'variant': components.variant,
            'description': components.description,
            'version': components.version,
            'ext': components.ext,
        }
    else:
        # For non-nomenclature files (e.g., .yml workflows)
        artifact_role = 'evidence'
        nomenclature = {
            'root': '00',
            'bucket': '00',
            'type': 'UNKNOWN',
            'lc_or_subbucket': 'LC01',
            'project': 'AMPEL360',
            'program': 'SPACET',
            'variant': 'PLUS',
            'description': filepath.stem.lower().replace('_', '-'),
            'version': 'v01',
            'ext': filepath.suffix.lstrip('.'),
        }
    
    return EvidenceItem(
        path=rel_path,
        artifact_role=artifact_role,
        nomenclature=nomenclature,
        hashes={'sha256': sha256},
        source_refs={'prs': [], 'issues': [], 'commits': []},
    )


def generate_manifest(
    knot_id: str,
    ata_code: str,
    ata_title: str,
    items: List[EvidenceItem],
    owner: str = "CM",
    variant: str = "PLUS",
) -> Dict[str, Any]:
    """Generate the evidence pack manifest JSON structure."""
    today = date.today().isoformat()
    
    manifest = {
        "manifest": {
            "schema_version": "v01",
            "project": "AMPEL360",
            "program": "SPACET",
            "variant": variant,
            "knot_id": knot_id,
            "ata_code": ata_code,
            "ata_title": ata_title,
            "lc_or_subbucket": "LC01",
            "status": "DRAFT",
            "aor_owner": owner,
            "contributors": ["CM", "QA"],
            "created_date": today,
            "updated_date": today,
            "description": f"Evidence pack for {knot_id} ATA {ata_code} - {ata_title}",
            "purpose": f"Collect and validate evidence artifacts for {knot_id} closure",
            "related_acceptance_criteria": [],
            "related_tasks": [],
            "effectivity": {
                "portal_scopes": ["SPACET-INT"],
                "workspace_access_grants": [
                    {
                        "principal": f"STK_{owner}",
                        "role": "Owner",
                        "access": "admin",
                        "paths": [f"AMPEL360-SPACE-T-PORTAL/STK_{owner}-*/KNOTS/{knot_id}_*/"]
                    }
                ]
            },
            "rbac": {
                "classification": "INTERNAL",
                "minimum_reviewers": ["CM", "QA"],
                "required_approvals": [owner]
            },
            "teknia_sharing": {
                "share_policy": "EVIDENCE_FIRST",
                "nku_reporting": {
                    "nku_tracker_path": f"AMPEL360-SPACE-T-PORTAL/MONITORING/{ata_code}_00_TAB_LC01_AMPEL360_SPACET_{variant}_{knot_id.lower()}-ata-{ata_code}-nku-tracking_v01.csv",
                    "reporting_frequency": "per_pr"
                }
            },
            "signing": {
                "signing_required": True,
                "signature_algorithm": "program-defined",
                "key_id": "",
                "signed_at": "",
                "signature": ""
            }
        },
        "contents": [asdict(item) for item in items],
        "audit": {
            "audit_queries": [
                {
                    "name": f"{knot_id} ATA{ata_code} pack completeness",
                    "path": f"KNOTS/{knot_id}_*/ASSETS/SCHEMAS/*_audit-query-contract_v01.yaml",
                    "expected_output": "All mandatory artifacts present, hashed, and linked to criteria."
                }
            ]
        }
    }
    
    return manifest


def generate_summary_report(
    knot_id: str,
    ata_code: str,
    ata_title: str,
    items: List[EvidenceItem],
    manifest_path: str,
    variant: str = "PLUS",
) -> str:
    """Generate the evidence pack summary report in Markdown."""
    today = date.today().isoformat()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Group items by artifact role
    by_role: Dict[str, List[EvidenceItem]] = {}
    for item in items:
        role = item.artifact_role
        if role not in by_role:
            by_role[role] = []
        by_role[role].append(item)
    
    lines = [
        "---",
        f'title: "{knot_id} ATA {ata_code} Evidence Pack Summary"',
        "type: RPT",
        "project: AMPEL360",
        "program: SPACET",
        f"variant: {variant}",
        f"report_date: {today}",
        "author: Evidence Pack Generator (Automated)",
        "status: Draft",
        f"knot_id: {knot_id}",
        f"ata_code: {ata_code}",
        "---",
        "",
        f"# Evidence Pack Summary: {knot_id} ATA {ata_code}",
        "",
        "## Executive Summary",
        "",
        f"This report summarizes the evidence pack for **{knot_id}** covering **ATA {ata_code} ({ata_title})**.",
        f"Generated automatically on {timestamp} for audit and certification purposes.",
        "",
        f"**Total Evidence Items:** {len(items)}",
        f"**Manifest File:** `{manifest_path}`",
        "",
        "## Evidence Summary by Category",
        "",
    ]
    
    # Add summary table
    lines.append("| Category | Count | Status |")
    lines.append("| :--- | :---: | :--- |")
    for role, role_items in sorted(by_role.items()):
        lines.append(f"| {role.replace('_', ' ').title()} | {len(role_items)} | ✓ Collected |")
    lines.append("")
    
    # Detailed listing
    lines.append("## Detailed Evidence Inventory")
    lines.append("")
    
    for role, role_items in sorted(by_role.items()):
        lines.append(f"### {role.replace('_', ' ').title()}")
        lines.append("")
        lines.append("| # | Path | Type | Version | SHA256 (first 16 chars) |")
        lines.append("| :---: | :--- | :--- | :---: | :--- |")
        for idx, item in enumerate(role_items, 1):
            path = item.path
            item_type = item.nomenclature.get('type', 'N/A')
            version = item.nomenclature.get('version', 'N/A')
            sha_short = item.hashes.get('sha256', '')[:16] + '...'
            lines.append(f"| {idx} | `{path}` | {item_type} | {version} | `{sha_short}` |")
        lines.append("")
    
    # Verification section
    lines.append("## Verification Status")
    lines.append("")
    lines.append("| Check | Status | Notes |")
    lines.append("| :--- | :---: | :--- |")
    lines.append(f"| Evidence items collected | ✅ | {len(items)} items |")
    lines.append("| SHA256 hashes computed | ✅ | All items hashed |")
    lines.append("| Manifest generated | ✅ | JSON format |")
    lines.append("| Nomenclature compliance | ⏳ | Run `validate_nomenclature.py` |")
    lines.append("| Signature | ⏳ | Pending review and approval |")
    lines.append("")
    
    # Reproducibility section
    lines.append("## Reproducibility")
    lines.append("")
    lines.append("This evidence pack was generated using the automated generator script.")
    lines.append("To reproduce:")
    lines.append("")
    lines.append("```bash")
    cmd = f"python scripts/generate_evidence_pack.py --knot {knot_id} --ata {ata_code}"
    if ata_title and ata_title != "GENERAL":
        cmd += f' --ata-title "{ata_title}"'
    lines.append(cmd)
    lines.append("```")
    lines.append("")
    
    # Next steps
    lines.append("## Next Steps")
    lines.append("")
    lines.append("1. Review evidence inventory for completeness")
    lines.append("2. Validate nomenclature compliance: `python validate_nomenclature.py --check-all`")
    lines.append("3. Obtain CM/QA review and approval")
    lines.append("4. Sign manifest with appropriate key")
    lines.append("5. Tag baseline in version control")
    lines.append("")
    
    # Footer
    lines.append("---")
    lines.append("")
    lines.append("**Document Control**")
    lines.append("")
    lines.append("| Field | Value |")
    lines.append("| :--- | :--- |")
    lines.append(f"| Generated | {timestamp} |")
    lines.append("| Generator | `scripts/generate_evidence_pack.py` v1.0 |")
    lines.append(f"| Knot | {knot_id} |")
    lines.append(f"| ATA | {ata_code} - {ata_title} |")
    lines.append(f"| Items | {len(items)} |")
    lines.append("")
    
    return "\n".join(lines)


def main() -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Generate automated, reproducible evidence packs for AMPEL360 Space-T",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    # Generate evidence pack for K06 ATA 00
    python scripts/generate_evidence_pack.py --knot K06 --ata 00

    # Generate with custom output directory
    python scripts/generate_evidence_pack.py --knot K01 --ata 00 --output-dir ./evidence-packs

    # Dry run to preview what would be generated
    python scripts/generate_evidence_pack.py --knot K06 --ata 00 --dry-run --verbose
        """
    )
    
    parser.add_argument(
        '--knot',
        required=True,
        help='Knot identifier (e.g., K01, K06)'
    )
    parser.add_argument(
        '--ata',
        required=True,
        help='ATA code (e.g., 00, 72)'
    )
    parser.add_argument(
        '--ata-title',
        default='GENERAL',
        help='ATA title for display (default: GENERAL)'
    )
    parser.add_argument(
        '--output-dir',
        default='.',
        help='Output directory for generated files'
    )
    parser.add_argument(
        '--repo-root',
        default='.',
        help='Repository root path'
    )
    parser.add_argument(
        '--owner',
        default='CM',
        help='Area of responsibility owner (default: CM)'
    )
    parser.add_argument(
        '--variant',
        default='PLUS',
        help='Variant code (default: PLUS)'
    )
    parser.add_argument(
        '--scan-patterns',
        help='JSON file with custom scan patterns'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be generated without writing files'
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Verbose output'
    )
    parser.add_argument(
        '--force',
        action='store_true',
        help='Overwrite existing files'
    )
    
    args = parser.parse_args()
    
    # Validate inputs
    knot_id = args.knot.upper()
    if not re.match(r'^K\d{2}$', knot_id):
        print(f"Error: Invalid knot ID '{knot_id}'. Must be K followed by 2 digits (e.g., K01, K06).")
        return 1
    
    # Handle ATA codes: 2-3 digits, zero-pad only if needed for 2-digit codes
    ata_code = args.ata
    if len(ata_code) == 1:
        ata_code = ata_code.zfill(2)
    if not re.match(r'^\d{2,3}$', ata_code):
        print(f"Error: Invalid ATA code '{args.ata}'. Must be 2-3 digits (e.g., 00, 72, 110).")
        return 1
    
    repo_root = Path(args.repo_root).resolve()
    if not repo_root.is_dir():
        print(f"Error: Repository root not found: {repo_root}")
        return 1
    
    output_dir = Path(args.output_dir).resolve()
    
    # Load custom scan patterns if provided
    patterns = None
    if args.scan_patterns:
        patterns_file = Path(args.scan_patterns)
        if patterns_file.exists():
            try:
                patterns = json.loads(patterns_file.read_text())
                if args.verbose:
                    print(f"Loaded {len(patterns)} custom scan patterns")
            except json.JSONDecodeError as e:
                print(f"Error: Invalid JSON in scan patterns file '{patterns_file}': {e}")
                return 1
    
    print(f"🔍 Scanning for evidence: {knot_id} ATA {ata_code}")
    if args.verbose:
        print(f"   Repository root: {repo_root}")
        print(f"   Output directory: {output_dir}")
    
    # Scan for evidence
    evidence_files = scan_for_evidence(
        repo_root, knot_id, ata_code,
        patterns=patterns,
        verbose=args.verbose
    )
    
    if not evidence_files:
        print(f"⚠️  No evidence files found for {knot_id} ATA {ata_code}")
        print("   Try running with --verbose to see scan details")
        return 0
    
    print(f"📦 Found {len(evidence_files)} evidence items")
    
    # Create evidence items
    items: List[EvidenceItem] = []
    for filepath, components in evidence_files:
        item = create_evidence_item(repo_root, filepath, components)
        if item is not None:
            items.append(item)
    
    # Generate filenames following nomenclature
    ata_root = ata_code[:2] if len(ata_code) >= 2 else '00'
    manifest_filename = f"{ata_root}_00_SCH_LC01_AMPEL360_SPACET_{args.variant}_{knot_id.lower()}-ata-{ata_code}-evidence-pack-manifest_v01.json"
    summary_filename = f"{ata_root}_00_RPT_LC01_AMPEL360_SPACET_{args.variant}_{knot_id.lower()}-ata-{ata_code}-evidence-pack-summary_v01.md"
    
    manifest_path = output_dir / manifest_filename
    summary_path = output_dir / summary_filename
    
    # Generate manifest
    manifest = generate_manifest(
        knot_id, ata_code, args.ata_title,
        items, owner=args.owner, variant=args.variant
    )
    
    # Generate summary report
    summary = generate_summary_report(
        knot_id, ata_code, args.ata_title,
        items, manifest_filename, variant=args.variant
    )
    
    if args.dry_run:
        print(f"\n[DRY RUN] Would create:")
        print(f"   📄 {manifest_path}")
        print(f"   📄 {summary_path}")
        print(f"\nManifest preview (first 50 lines):")
        manifest_json = json.dumps(manifest, indent=2)
        for line in manifest_json.split('\n')[:50]:
            print(f"   {line}")
        print("   ...")
        return 0
    
    # Check if files exist
    if manifest_path.exists() and not args.force:
        print(f"⚠️  Manifest already exists: {manifest_path}")
        print("   Use --force to overwrite")
        return 1
    if summary_path.exists() and not args.force:
        print(f"⚠️  Summary already exists: {summary_path}")
        print("   Use --force to overwrite")
        return 1
    
    # Write files
    output_dir.mkdir(parents=True, exist_ok=True)
    
    manifest_path.write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8')
    print(f"✅ Created manifest: {manifest_path}")
    
    summary_path.write_text(summary, encoding='utf-8')
    print(f"✅ Created summary: {summary_path}")
    
    print(f"\n🎉 Evidence pack generated successfully!")
    print(f"   Items: {len(items)}")
    print(f"   Manifest: {manifest_path.name}")
    print(f"   Summary: {summary_path.name}")
    print(f"\nNext steps:")
    print(f"   1. Review the generated files")
    print(f"   2. Validate: python validate_nomenclature.py {manifest_path.name}")
    print(f"   3. Commit and push for review")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
