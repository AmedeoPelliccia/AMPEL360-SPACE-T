#!/usr/bin/env python3
"""
AMPEL360 Space-T NKU Scoring Automation
========================================
Version: 1.0
Date: 2025-12-16

Implements NKU (Non-Known Unknowns / Partitioned Uncertainty Resolution) scoring:
- NKU ledger updater: Add/update entries in NKU tracking CSV files
- Partition score calculator: Compute scores based on evidence + decisions

Usage:
    # Add/update NKU entry
    python scripts/nku_scoring.py add-entry --knot K06 --ata 00 --category OPEN \\
        --description "Missing schema registry" --owner "CM WG" --notes "Priority: High"
    
    # Update entry status
    python scripts/nku_scoring.py update-entry --knot K01 --ata 22 --id NKU-K01-22-001 \\
        --status RESOLVED --resolution-date 2025-12-16
    
    # Calculate partition scores
    python scripts/nku_scoring.py calc-scores --knot K06
    
    # Calculate all scores across repository
    python scripts/nku_scoring.py calc-scores --all
    
    # Generate score report
    python scripts/nku_scoring.py report --knot K06 --output report.json
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
from dataclasses import dataclass, field, asdict
from datetime import date, datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any


# NKU Status values
NKU_STATUS_OPEN = "OPEN"
NKU_STATUS_IN_PROGRESS = "IN_PROGRESS"
NKU_STATUS_RESOLVED = "RESOLVED"
NKU_STATUS_BLOCKED = "BLOCKED"
NKU_STATUSES = {NKU_STATUS_OPEN, NKU_STATUS_IN_PROGRESS, NKU_STATUS_RESOLVED, NKU_STATUS_BLOCKED}

# NKU Category values
NKU_CATEGORY_TECHNICAL = "TECHNICAL"
NKU_CATEGORY_PROCESS = "PROCESS"
NKU_CATEGORY_RESOURCE = "RESOURCE"
NKU_CATEGORY_DEPENDENCY = "DEPENDENCY"
NKU_CATEGORY_GOVERNANCE = "GOVERNANCE"
NKU_CATEGORIES = {
    NKU_CATEGORY_TECHNICAL, NKU_CATEGORY_PROCESS, NKU_CATEGORY_RESOURCE,
    NKU_CATEGORY_DEPENDENCY, NKU_CATEGORY_GOVERNANCE
}

# Score values per NKU model
SCORE_NOT_STARTED = 0.0
SCORE_IN_PROGRESS = 0.5
SCORE_COMPLETE = 1.0

# CSV header for NKU tracking files
NKU_CSV_HEADER = ["ID", "Date", "Category", "Description", "Status", "Owner", "Resolution_Date", "Notes"]


@dataclass
class NKUEntry:
    """Represents a single NKU entry in the ledger."""
    id: str
    date: str
    category: str
    description: str
    status: str
    owner: str
    resolution_date: str = ""
    notes: str = ""
    
    def to_row(self) -> List[str]:
        """Convert to CSV row."""
        return [
            self.id, self.date, self.category, self.description,
            self.status, self.owner, self.resolution_date, self.notes
        ]
    
    @classmethod
    def from_row(cls, row: List[str]) -> "NKUEntry":
        """Create from CSV row."""
        # Handle rows with missing fields
        while len(row) < 8:
            row.append("")
        return cls(
            id=row[0].strip(),
            date=row[1].strip(),
            category=row[2].strip(),
            description=row[3].strip(),
            status=row[4].strip(),
            owner=row[5].strip(),
            resolution_date=row[6].strip() if len(row) > 6 else "",
            notes=row[7].strip() if len(row) > 7 else ""
        )


@dataclass
class PartitionScore:
    """Score for a single partition (Knot + ATA combination)."""
    knot_id: str
    ata: str
    total_entries: int = 0
    resolved_entries: int = 0
    in_progress_entries: int = 0
    open_entries: int = 0
    blocked_entries: int = 0
    score: float = 0.0
    
    def calculate_score(self) -> float:
        """
        Calculate partition score based on NKU model.
        
        Scoring approach:
        - No entries: score = 1.0 (no uncertainty to resolve)
        - All resolved: score = 1.0
        - Mix of resolved/in-progress/open: weighted average
        - Blocked entries reduce score
        """
        if self.total_entries == 0:
            self.score = SCORE_COMPLETE
            return self.score
        
        # Calculate weighted score
        resolved_weight = self.resolved_entries * SCORE_COMPLETE
        in_progress_weight = self.in_progress_entries * SCORE_IN_PROGRESS
        open_weight = self.open_entries * SCORE_NOT_STARTED
        blocked_weight = self.blocked_entries * SCORE_NOT_STARTED
        
        total_weight = resolved_weight + in_progress_weight + open_weight + blocked_weight
        self.score = round(total_weight / self.total_entries, 2)
        return self.score


@dataclass
class KnotScore:
    """Aggregated score for a knot across all ATAs."""
    knot_id: str
    partition_scores: List[PartitionScore] = field(default_factory=list)
    aggregated_score: float = 0.0
    total_entries: int = 0
    
    def calculate_aggregated_score(self) -> float:
        """
        Calculate aggregated score across all partitions.
        Uses weighted average by number of entries per partition.
        """
        if not self.partition_scores:
            self.aggregated_score = SCORE_COMPLETE
            return self.aggregated_score
        
        total_weight = 0.0
        total_count = 0
        
        for ps in self.partition_scores:
            # Weight by number of entries (minimum 1 to include empty partitions)
            weight = max(ps.total_entries, 1)
            total_weight += ps.score * weight
            total_count += weight
        
        if total_count == 0:
            self.aggregated_score = SCORE_COMPLETE
        else:
            self.aggregated_score = round(total_weight / total_count, 2)
        
        self.total_entries = sum(ps.total_entries for ps in self.partition_scores)
        return self.aggregated_score


class NKULedger:
    """Manages NKU ledger entries for a specific knot and ATA."""
    
    def __init__(self, csv_path: Path):
        """
        Initialize ledger from CSV file.
        
        Args:
            csv_path: Path to the NKU tracking CSV file
        """
        self.csv_path = csv_path
        self.entries: List[NKUEntry] = []
        self.header_comment: str = ""
        self._load()
    
    def _load(self) -> None:
        """Load entries from CSV file."""
        if not self.csv_path.exists():
            return
        
        with open(self.csv_path, 'r', newline='', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Parse header comment and data
        data_lines = []
        for line in lines:
            stripped = line.strip()
            if stripped.startswith('#'):
                self.header_comment += line
            elif stripped:
                data_lines.append(stripped)
        
        if not data_lines:
            return
        
        # Parse CSV data
        reader = csv.reader(data_lines)
        rows = list(reader)
        
        if not rows:
            return
        
        # Skip header row if present
        start_idx = 0
        if rows[0][0].upper() == "ID":
            start_idx = 1
        
        for row in rows[start_idx:]:
            if row and row[0].strip():  # Skip empty rows
                try:
                    entry = NKUEntry.from_row(row)
                    if entry.id:  # Only add entries with valid IDs
                        self.entries.append(entry)
                except (IndexError, ValueError):
                    continue
    
    def save(self) -> None:
        """Save entries to CSV file."""
        self.csv_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(self.csv_path, 'w', newline='', encoding='utf-8') as f:
            # Write header comment if present
            if self.header_comment:
                f.write(self.header_comment)
            
            writer = csv.writer(f)
            writer.writerow(NKU_CSV_HEADER)
            
            for entry in self.entries:
                writer.writerow(entry.to_row())
    
    def generate_id(self, knot_id: str, ata: str) -> str:
        """Generate next NKU ID for the ledger."""
        # Find max existing sequence number
        pattern = re.compile(rf"NKU-{knot_id}-{ata}-(\d+)")
        max_seq = 0
        
        for entry in self.entries:
            match = pattern.match(entry.id)
            if match:
                seq = int(match.group(1))
                max_seq = max(max_seq, seq)
        
        next_seq = max_seq + 1
        return f"NKU-{knot_id}-{ata}-{next_seq:03d}"
    
    def add_entry(self, knot_id: str, ata: str, category: str, description: str,
                  owner: str, notes: str = "", status: str = NKU_STATUS_OPEN) -> NKUEntry:
        """
        Add a new NKU entry to the ledger.
        
        Args:
            knot_id: Knot identifier (e.g., K06)
            ata: ATA chapter code (e.g., 00, 22)
            category: Category (TECHNICAL, PROCESS, etc.)
            description: Description of the uncertainty
            owner: Owner responsible for resolution
            notes: Optional notes
            status: Initial status (default: OPEN)
        
        Returns:
            The newly created NKUEntry
        """
        entry_id = self.generate_id(knot_id, ata)
        entry = NKUEntry(
            id=entry_id,
            date=date.today().isoformat(),
            category=category.upper(),
            description=description,
            status=status.upper(),
            owner=owner,
            notes=notes
        )
        self.entries.append(entry)
        return entry
    
    def update_entry(self, entry_id: str, status: Optional[str] = None,
                     resolution_date: Optional[str] = None,
                     notes: Optional[str] = None) -> Optional[NKUEntry]:
        """
        Update an existing NKU entry.
        
        Args:
            entry_id: ID of the entry to update
            status: New status (optional)
            resolution_date: Resolution date (optional, required if status=RESOLVED)
            notes: Additional notes (optional)
        
        Returns:
            Updated entry or None if not found
        """
        for entry in self.entries:
            if entry.id == entry_id:
                if status:
                    entry.status = status.upper()
                if resolution_date:
                    entry.resolution_date = resolution_date
                elif status == NKU_STATUS_RESOLVED and not entry.resolution_date:
                    entry.resolution_date = date.today().isoformat()
                if notes:
                    entry.notes = notes
                return entry
        return None
    
    def get_entry(self, entry_id: str) -> Optional[NKUEntry]:
        """Get entry by ID."""
        for entry in self.entries:
            if entry.id == entry_id:
                return entry
        return None
    
    def calculate_partition_score(self, knot_id: str, ata: str) -> PartitionScore:
        """Calculate score for this partition."""
        ps = PartitionScore(knot_id=knot_id, ata=ata)
        
        for entry in self.entries:
            ps.total_entries += 1
            status = entry.status.upper()
            if status == NKU_STATUS_RESOLVED:
                ps.resolved_entries += 1
            elif status == NKU_STATUS_IN_PROGRESS:
                ps.in_progress_entries += 1
            elif status == NKU_STATUS_BLOCKED:
                ps.blocked_entries += 1
            else:  # OPEN or unknown
                ps.open_entries += 1
        
        ps.calculate_score()
        return ps


class NKUScoringEngine:
    """
    NKU Scoring Engine for the AMPEL360 Space-T project.
    
    Discovers NKU tracking files across the repository and calculates scores.
    """
    
    # Pattern to find NKU tracking CSV files
    NKU_FILE_PATTERN = re.compile(r".*nku-tracking.*\.csv$", re.IGNORECASE)
    
    # Pattern to extract knot and ATA from filename
    # Example: 22_00_LOG_LC01_AMPEL360_SPACET_PLUS_k01-ata-22-nku-tracking_v01.csv
    KNOT_ATA_PATTERN = re.compile(r"k(\d{2})-ata-(\d+)-nku-tracking", re.IGNORECASE)
    
    # Pattern to extract knot from knot-level NKU file
    # Example: 00_00_LOG_LC01_AMPEL360_SPACET_PLUS_k01-nku-tracking_v01.csv
    KNOT_PATTERN = re.compile(r"k(\d{2})-nku-tracking", re.IGNORECASE)
    
    def __init__(self, repo_root: Path):
        """
        Initialize scoring engine.
        
        Args:
            repo_root: Root directory of the repository
        """
        self.repo_root = repo_root
        self.nku_files: Dict[str, Dict[str, Path]] = {}  # {knot_id: {ata: path}}
        self._discover_nku_files()
    
    def _discover_nku_files(self) -> None:
        """Discover all NKU tracking files in the repository."""
        portal_path = self.repo_root / "AMPEL360-SPACE-T-PORTAL"
        
        if not portal_path.exists():
            return
        
        for csv_file in portal_path.rglob("*.csv"):
            if not self.NKU_FILE_PATTERN.match(csv_file.name):
                continue
            
            # Try to extract knot and ATA from filename
            match = self.KNOT_ATA_PATTERN.search(csv_file.name)
            if match:
                knot_id = f"K{match.group(1)}"
                ata = match.group(2)
                
                if knot_id not in self.nku_files:
                    self.nku_files[knot_id] = {}
                self.nku_files[knot_id][ata] = csv_file
            else:
                # Try knot-level pattern
                match = self.KNOT_PATTERN.search(csv_file.name)
                if match:
                    knot_id = f"K{match.group(1)}"
                    if knot_id not in self.nku_files:
                        self.nku_files[knot_id] = {}
                    self.nku_files[knot_id]["_knot"] = csv_file
    
    def get_nku_file_path(self, knot_id: str, ata: str) -> Optional[Path]:
        """Get path to NKU tracking file for a specific knot and ATA."""
        if knot_id in self.nku_files:
            return self.nku_files[knot_id].get(ata)
        return None
    
    def get_all_knots(self) -> List[str]:
        """Get all discovered knot IDs."""
        return sorted(self.nku_files.keys())
    
    def get_atas_for_knot(self, knot_id: str) -> List[str]:
        """Get all ATAs with NKU tracking files for a knot."""
        if knot_id in self.nku_files:
            return sorted(ata for ata in self.nku_files[knot_id].keys() if ata != "_knot")
        return []
    
    def calculate_partition_score(self, knot_id: str, ata: str) -> Optional[PartitionScore]:
        """Calculate score for a specific partition."""
        csv_path = self.get_nku_file_path(knot_id, ata)
        if not csv_path or not csv_path.exists():
            return None
        
        ledger = NKULedger(csv_path)
        return ledger.calculate_partition_score(knot_id, ata)
    
    def calculate_knot_score(self, knot_id: str) -> KnotScore:
        """Calculate aggregated score for a knot across all ATAs."""
        ks = KnotScore(knot_id=knot_id)
        
        for ata in self.get_atas_for_knot(knot_id):
            ps = self.calculate_partition_score(knot_id, ata)
            if ps:
                ks.partition_scores.append(ps)
        
        ks.calculate_aggregated_score()
        return ks
    
    def calculate_all_scores(self) -> Dict[str, KnotScore]:
        """Calculate scores for all discovered knots."""
        scores = {}
        for knot_id in self.get_all_knots():
            scores[knot_id] = self.calculate_knot_score(knot_id)
        return scores
    
    def generate_report(self, knot_id: Optional[str] = None) -> Dict[str, Any]:
        """
        Generate a comprehensive score report.
        
        Args:
            knot_id: Optional knot ID to filter report
        
        Returns:
            Dictionary containing score report
        """
        report = {
            "generated_at": datetime.now().isoformat(),
            "repository": str(self.repo_root),
            "knots": {}
        }
        
        if knot_id:
            knots_to_process = [knot_id] if knot_id in self.nku_files else []
        else:
            knots_to_process = self.get_all_knots()
        
        total_score = 0.0
        total_knots = 0
        
        for kid in knots_to_process:
            ks = self.calculate_knot_score(kid)
            
            knot_report = {
                "knot_id": kid,
                "aggregated_score": ks.aggregated_score,
                "total_entries": ks.total_entries,
                "partitions": []
            }
            
            for ps in ks.partition_scores:
                knot_report["partitions"].append({
                    "ata": ps.ata,
                    "score": ps.score,
                    "total_entries": ps.total_entries,
                    "resolved": ps.resolved_entries,
                    "in_progress": ps.in_progress_entries,
                    "open": ps.open_entries,
                    "blocked": ps.blocked_entries
                })
            
            report["knots"][kid] = knot_report
            total_score += ks.aggregated_score
            total_knots += 1
        
        # Calculate program-wide score
        if total_knots > 0:
            report["program_score"] = round(total_score / total_knots, 2)
        else:
            report["program_score"] = 1.0
        
        report["total_knots"] = total_knots
        return report


def cmd_add_entry(args: argparse.Namespace, engine: NKUScoringEngine) -> int:
    """Handle add-entry command."""
    knot_id = args.knot.upper()
    ata = args.ata
    
    # Find the NKU file
    csv_path = engine.get_nku_file_path(knot_id, ata)
    
    if not csv_path:
        # Create a new NKU file path if none exists
        # Use a default location in the portal
        portal_path = engine.repo_root / "AMPEL360-SPACE-T-PORTAL"
        
        # Find an appropriate location based on knot
        knot_dirs = list(portal_path.rglob(f"*/{knot_id}_*"))
        if knot_dirs:
            # Use first matching knot directory
            knot_dir = knot_dirs[0]
            ata_dir = knot_dir / "ATA_TASKS" / f"ATA_{ata}" / "MONITORING"
        else:
            print(f"Error: Could not find knot directory for {knot_id}", file=sys.stderr)
            return 1
        
        # Generate filename following nomenclature
        ata_root = ata.zfill(2) if int(ata) < 100 else "00"
        csv_filename = f"{ata_root}_00_LOG_LC01_AMPEL360_SPACET_PLUS_{knot_id.lower()}-ata-{ata}-nku-tracking_v01.csv"
        csv_path = ata_dir / csv_filename
        
        # Create header comment
        header = f"# {knot_id} ATA {ata} NKU Tracking\n"
    else:
        header = ""
    
    ledger = NKULedger(csv_path)
    if header:
        ledger.header_comment = header
    
    # Validate category
    category = args.category.upper()
    if category not in NKU_CATEGORIES:
        print(f"Warning: Category '{category}' not in standard categories: {sorted(NKU_CATEGORIES)}")
    
    entry = ledger.add_entry(
        knot_id=knot_id,
        ata=ata,
        category=category,
        description=args.description,
        owner=args.owner,
        notes=args.notes or "",
        status=args.status or NKU_STATUS_OPEN
    )
    
    ledger.save()
    print(f"✅ Added NKU entry: {entry.id}")
    print(f"   File: {csv_path}")
    return 0


def cmd_update_entry(args: argparse.Namespace, engine: NKUScoringEngine) -> int:
    """Handle update-entry command."""
    knot_id = args.knot.upper()
    ata = args.ata
    
    csv_path = engine.get_nku_file_path(knot_id, ata)
    if not csv_path or not csv_path.exists():
        print(f"Error: NKU file not found for {knot_id} ATA {ata}", file=sys.stderr)
        return 1
    
    ledger = NKULedger(csv_path)
    
    entry = ledger.update_entry(
        entry_id=args.id,
        status=args.status,
        resolution_date=args.resolution_date,
        notes=args.notes
    )
    
    if not entry:
        print(f"Error: Entry '{args.id}' not found", file=sys.stderr)
        return 1
    
    ledger.save()
    print(f"✅ Updated NKU entry: {entry.id}")
    print(f"   Status: {entry.status}")
    if entry.resolution_date:
        print(f"   Resolution Date: {entry.resolution_date}")
    return 0


def cmd_calc_scores(args: argparse.Namespace, engine: NKUScoringEngine) -> int:
    """Handle calc-scores command."""
    if args.all:
        scores = engine.calculate_all_scores()
        
        print("=" * 60)
        print("NKU Partition Scores")
        print("=" * 60)
        
        total_score = 0.0
        total_knots = 0
        
        for knot_id in sorted(scores.keys()):
            ks = scores[knot_id]
            print(f"\n{knot_id}: {ks.aggregated_score:.2f} ({ks.total_entries} entries)")
            
            for ps in sorted(ks.partition_scores, key=lambda x: x.ata):
                status = "✓" if ps.score >= 0.8 else ("⚠" if ps.score >= 0.5 else "✗")
                print(f"  {status} ATA {ps.ata}: {ps.score:.2f} "
                      f"(R:{ps.resolved_entries} P:{ps.in_progress_entries} "
                      f"O:{ps.open_entries} B:{ps.blocked_entries})")
            
            total_score += ks.aggregated_score
            total_knots += 1
        
        if total_knots > 0:
            program_score = total_score / total_knots
            print("\n" + "=" * 60)
            print(f"Program NKU Score: {program_score:.2f}")
            print("=" * 60)
    else:
        knot_id = args.knot.upper()
        ks = engine.calculate_knot_score(knot_id)
        
        print(f"\nKnot {knot_id} NKU Score: {ks.aggregated_score:.2f}")
        print(f"Total entries: {ks.total_entries}")
        print("\nPartition Breakdown:")
        
        for ps in sorted(ks.partition_scores, key=lambda x: x.ata):
            status = "✓" if ps.score >= 0.8 else ("⚠" if ps.score >= 0.5 else "✗")
            print(f"  {status} ATA {ps.ata}: {ps.score:.2f} "
                  f"(R:{ps.resolved_entries} P:{ps.in_progress_entries} "
                  f"O:{ps.open_entries} B:{ps.blocked_entries})")
    
    return 0


def cmd_report(args: argparse.Namespace, engine: NKUScoringEngine) -> int:
    """Handle report command."""
    report = engine.generate_report(knot_id=args.knot.upper() if args.knot else None)
    
    if args.output:
        output_path = Path(args.output)
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2)
        print(f"✅ Report saved to: {output_path}")
    else:
        print(json.dumps(report, indent=2))
    
    return 0


def main() -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="AMPEL360 Space-T NKU Scoring Automation",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        "--repo-root",
        default=".",
        help="Repository root path (default: current directory)"
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # add-entry command
    add_parser = subparsers.add_parser("add-entry", help="Add a new NKU entry")
    add_parser.add_argument("--knot", required=True, help="Knot ID (e.g., K06)")
    add_parser.add_argument("--ata", required=True, help="ATA chapter code (e.g., 00, 22)")
    add_parser.add_argument("--category", required=True,
                           help=f"Category: {', '.join(sorted(NKU_CATEGORIES))}")
    add_parser.add_argument("--description", required=True, help="Description of uncertainty")
    add_parser.add_argument("--owner", required=True, help="Owner responsible for resolution")
    add_parser.add_argument("--notes", help="Additional notes")
    add_parser.add_argument("--status", default=NKU_STATUS_OPEN,
                           help=f"Initial status: {', '.join(sorted(NKU_STATUSES))}")
    
    # update-entry command
    update_parser = subparsers.add_parser("update-entry", help="Update an existing NKU entry")
    update_parser.add_argument("--knot", required=True, help="Knot ID (e.g., K06)")
    update_parser.add_argument("--ata", required=True, help="ATA chapter code")
    update_parser.add_argument("--id", required=True, help="NKU entry ID to update")
    update_parser.add_argument("--status", help=f"New status: {', '.join(sorted(NKU_STATUSES))}")
    update_parser.add_argument("--resolution-date", help="Resolution date (YYYY-MM-DD)")
    update_parser.add_argument("--notes", help="Additional notes")
    
    # calc-scores command
    calc_parser = subparsers.add_parser("calc-scores", help="Calculate NKU partition scores")
    calc_group = calc_parser.add_mutually_exclusive_group(required=True)
    calc_group.add_argument("--knot", help="Calculate scores for specific knot")
    calc_group.add_argument("--all", action="store_true", help="Calculate all scores")
    
    # report command
    report_parser = subparsers.add_parser("report", help="Generate score report")
    report_parser.add_argument("--knot", help="Filter report to specific knot")
    report_parser.add_argument("--output", "-o", help="Output file path (JSON)")
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return 1
    
    repo_root = Path(args.repo_root).resolve()
    engine = NKUScoringEngine(repo_root)
    
    if args.command == "add-entry":
        return cmd_add_entry(args, engine)
    elif args.command == "update-entry":
        return cmd_update_entry(args, engine)
    elif args.command == "calc-scores":
        return cmd_calc_scores(args, engine)
    elif args.command == "report":
        return cmd_report(args, engine)
    else:
        parser.print_help()
        return 1


if __name__ == "__main__":
    sys.exit(main())
