#!/usr/bin/env python3
"""
AMPEL360 Space-T Staleness Detection Script
============================================
Version: 1.0
Date: 2026-01-07
Task: GATE-016 implementation for Weekly Governance Audit

Detects stale artifacts in the repository based on:
- File modification time vs. repository activity
- Derived artifacts that may be out of sync with their sources
- Artifacts marked as DRAFT or OBSOLETE that haven't been updated
- Evidence packs with old timestamps

Usage:
    python scripts/check_staleness.py --all
    python scripts/check_staleness.py --threshold-days 90
    python scripts/check_staleness.py --check-derived-only

Exit codes:
    0: No stale artifacts found
    1: Stale artifacts detected
    2: Script error
"""

import argparse
import os
import sys
import re
from datetime import datetime
from pathlib import Path
from typing import List, Tuple

# Staleness thresholds (in days)
DEFAULT_THRESHOLD_DAYS = 90
DRAFT_THRESHOLD_DAYS = 60
OBSOLETE_WARNING_DAYS = 30

# File patterns that indicate derived artifacts
DERIVED_PATTERNS = {
    'RPT': 'Report (may be derived from requirements, test results)',
    'TRC': 'Traceability matrix (derived from REQ, TST)',
    'IDX': 'Index (derived from catalog of artifacts)',
    'CAT': 'Catalog (derived from collection of items)',
    'LOG': 'Log (should be regularly updated)',
}

# Status patterns in filename
STATUS_PATTERNS = {
    'DRAFT': r'_DRAFT\.',
    'OBSOLETE': r'_OBSOLETE\.',
    'ACTIVE': r'_ACTIVE\.',
    'RELEASED': r'_RELEASED\.',
    'APPROVED': r'_APPROVED\.',
}


class StaleArtifact:
    """Represents a potentially stale artifact."""
    
    def __init__(self, path: Path, reason: str, days_old: int, severity: str = "WARNING"):
        self.path = path
        self.reason = reason
        self.days_old = days_old
        self.severity = severity
    
    def __str__(self) -> str:
        return f"[{self.severity}] {self.path} ({self.days_old} days old) - {self.reason}"


class StalenessDetector:
    """Detects stale artifacts in the repository."""
    
    def __init__(self, repo_root: Path, threshold_days: int = DEFAULT_THRESHOLD_DAYS):
        self.repo_root = repo_root
        self.threshold_days = threshold_days
        self.stale_artifacts: List[StaleArtifact] = []
        self.checked_files = 0
        self.excluded_dirs = {'.git', 'node_modules', '__pycache__', '.github', '.vscode'}
    
    def get_file_age_days(self, file_path: Path) -> int:
        """Get the age of a file in days."""
        try:
            mtime = os.path.getmtime(file_path)
            file_time = datetime.fromtimestamp(mtime)
            age = datetime.now() - file_time
            return age.days
        except OSError:
            return 0
    
    def extract_status_from_filename(self, filename: str) -> str:
        """Extract status from filename using v6.0 nomenclature."""
        for status, pattern in STATUS_PATTERNS.items():
            if re.search(pattern, filename):
                return status
        return "UNKNOWN"
    
    def extract_type_from_filename(self, filename: str) -> str:
        """Extract TYPE code from v6.0 nomenclature filename."""
        # Pattern: ..._{TYPE}_I##-R##_{STATUS}.ext
        match = re.search(r'_([A-Z]{2,8})_I\d{2}-R\d{2}_', filename)
        if match:
            return match.group(1)
        return "UNKNOWN"
    
    def is_derived_artifact(self, file_path: Path) -> Tuple[bool, str]:
        """Check if a file is a derived artifact."""
        type_code = self.extract_type_from_filename(file_path.name)
        
        if type_code in DERIVED_PATTERNS:
            return True, DERIVED_PATTERNS[type_code]
        
        return False, ""
    
    def check_draft_staleness(self, file_path: Path) -> None:
        """Check if DRAFT artifacts are stale."""
        status = self.extract_status_from_filename(file_path.name)
        
        if status == "DRAFT":
            age_days = self.get_file_age_days(file_path)
            
            if age_days > DRAFT_THRESHOLD_DAYS:
                self.stale_artifacts.append(
                    StaleArtifact(
                        path=file_path.relative_to(self.repo_root),
                        reason=f"DRAFT artifact not updated in {age_days} days (threshold: {DRAFT_THRESHOLD_DAYS})",
                        days_old=age_days,
                        severity="WARNING"
                    )
                )
    
    def check_obsolete_staleness(self, file_path: Path) -> None:
        """Check if OBSOLETE artifacts should be cleaned up."""
        status = self.extract_status_from_filename(file_path.name)
        
        if status == "OBSOLETE":
            age_days = self.get_file_age_days(file_path)
            
            if age_days > OBSOLETE_WARNING_DAYS:
                self.stale_artifacts.append(
                    StaleArtifact(
                        path=file_path.relative_to(self.repo_root),
                        reason=f"OBSOLETE artifact still present after {age_days} days (consider removing)",
                        days_old=age_days,
                        severity="INFO"
                    )
                )
    
    def check_derived_artifact_staleness(self, file_path: Path) -> None:
        """Check if derived artifacts are stale."""
        is_derived, reason = self.is_derived_artifact(file_path)
        
        if is_derived:
            age_days = self.get_file_age_days(file_path)
            
            if age_days > self.threshold_days:
                self.stale_artifacts.append(
                    StaleArtifact(
                        path=file_path.relative_to(self.repo_root),
                        reason=f"Derived artifact ({reason}) not updated in {age_days} days",
                        days_old=age_days,
                        severity="WARNING"
                    )
                )
    
    def check_general_staleness(self, file_path: Path) -> None:
        """Check general file staleness."""
        age_days = self.get_file_age_days(file_path)
        
        # Only report if significantly stale
        if age_days > self.threshold_days * 2:
            status = self.extract_status_from_filename(file_path.name)
            
            # Don't flag RELEASED or APPROVED artifacts
            if status not in ['RELEASED', 'APPROVED']:
                self.stale_artifacts.append(
                    StaleArtifact(
                        path=file_path.relative_to(self.repo_root),
                        reason=f"Artifact not modified in {age_days} days (threshold: {self.threshold_days * 2})",
                        days_old=age_days,
                        severity="INFO"
                    )
                )
    
    def scan_repository(self, check_derived_only: bool = False) -> None:
        """Scan repository for stale artifacts."""
        print(f"🔍 Scanning repository for stale artifacts...")
        print(f"   Threshold: {self.threshold_days} days")
        print(f"   Root: {self.repo_root}")
        
        for root, dirs, files in os.walk(self.repo_root):
            # Remove excluded directories from search
            dirs[:] = [d for d in dirs if d not in self.excluded_dirs]
            
            for file in files:
                file_path = Path(root) / file
                
                # Skip non-text files
                if file_path.suffix not in ['.md', '.json', '.yaml', '.yml', '.csv', '.txt']:
                    continue
                
                # Skip templates
                if '/templates/' in str(file_path):
                    continue
                
                self.checked_files += 1
                
                if check_derived_only:
                    self.check_derived_artifact_staleness(file_path)
                else:
                    self.check_draft_staleness(file_path)
                    self.check_obsolete_staleness(file_path)
                    self.check_derived_artifact_staleness(file_path)
                    # Uncomment to check general staleness (can be noisy)
                    # self.check_general_staleness(file_path)
    
    def print_summary(self) -> None:
        """Print staleness detection summary."""
        print("\n" + "=" * 60)
        print("STALENESS DETECTION SUMMARY")
        print("=" * 60)
        
        print(f"\n📋 Checked {self.checked_files} files")
        
        if not self.stale_artifacts:
            print("\n✅ No stale artifacts detected")
            return
        
        # Group by severity
        warnings = [a for a in self.stale_artifacts if a.severity == "WARNING"]
        infos = [a for a in self.stale_artifacts if a.severity == "INFO"]
        
        if warnings:
            print(f"\n⚠️  WARNINGS ({len(warnings)}):")
            for artifact in sorted(warnings, key=lambda x: x.days_old, reverse=True)[:20]:
                print(f"  • {artifact}")
            if len(warnings) > 20:
                print(f"  ... and {len(warnings) - 20} more")
        
        if infos:
            print(f"\n📋 INFO ({len(infos)}):")
            for artifact in sorted(infos, key=lambda x: x.days_old, reverse=True)[:10]:
                print(f"  • {artifact}")
            if len(infos) > 10:
                print(f"  ... and {len(infos) - 10} more")
        
        print("\n" + "=" * 60)
        if warnings:
            print(f"⚠️  STALENESS DETECTED - {len(warnings)} warnings, {len(infos)} info messages")
        else:
            print(f"✅ VALIDATION PASSED - Only informational messages")
        print("=" * 60)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Detect stale artifacts in AMPEL360 Space-T repository"
    )
    parser.add_argument(
        '--all',
        action='store_true',
        help='Check all staleness conditions'
    )
    parser.add_argument(
        '--check-derived-only',
        action='store_true',
        help='Only check derived artifacts (RPT, TRC, IDX, CAT, LOG)'
    )
    parser.add_argument(
        '--threshold-days',
        type=int,
        default=DEFAULT_THRESHOLD_DAYS,
        help=f'Staleness threshold in days (default: {DEFAULT_THRESHOLD_DAYS})'
    )
    parser.add_argument(
        '--repo-root',
        type=str,
        default='.',
        help='Repository root path (default: current directory)'
    )
    
    args = parser.parse_args()
    
    repo_root = Path(args.repo_root).resolve()
    
    if not repo_root.exists():
        print(f"❌ Error: Repository root not found: {repo_root}", file=sys.stderr)
        return 2
    
    detector = StalenessDetector(repo_root, args.threshold_days)
    
    try:
        detector.scan_repository(check_derived_only=args.check_derived_only)
        detector.print_summary()
        
        # Return exit code based on warnings
        warnings = [a for a in detector.stale_artifacts if a.severity == "WARNING"]
        return 1 if warnings else 0
        
    except Exception as e:
        print(f"❌ Error during staleness detection: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
