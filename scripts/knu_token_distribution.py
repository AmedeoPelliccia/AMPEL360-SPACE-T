#!/usr/bin/env python3
"""
AMPEL360 Space-T KNU Token Distribution System
===============================================
Version: 1.0
Date: 2026-01-10

Implements KNU (Known Non-Unknowns / Uncertainty Resolution Unit) token distribution
that rewards contributors based on predicted effort and measured impact (including 
spillover effects to adjacent KNOTs).

Distribution Formula:
    w_i = α·Ê_i + (1-α)·Î_i
    T_i = P_k · w_i

Where:
    - P_k = Prize pool (total KNU tokens for the KNOT)
    - E_i = Predicted effort (normalized)
    - Ê_i = Normalized effort: E_i / Σ E_i
    - I_i = Effective impact: ΔR_k,i + λ·S_i
    - Î_i = Normalized impact: I_i / Σ I_i
    - S_i = Spillover: Σ(a_k→j · ΔR_j,i) for adjacent KNOTs
    - ΔR_k,i = Direct residue reduction attributed to KNU
    - a_k→j = Adjacency weight between KNOTs

Default Parameters:
    - α = 0.30 (30% effort, 70% impact)
    - λ = 0.50 (spillover worth 50% of direct impact)

Usage:
    # Distribute tokens for a KNOT
    python scripts/knu_token_distribution.py distribute --knot K06 --pool 1000

    # Generate distribution report
    python scripts/knu_token_distribution.py report --knot K06 --output rewards.json

    # Validate KNU eligibility
    python scripts/knu_token_distribution.py validate --knot K06 --knu KNU-K06-00-001

    # Calculate with custom parameters
    python scripts/knu_token_distribution.py distribute --knot K06 --pool 1000 --alpha 0.25 --lambda 0.6
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
import yaml
from dataclasses import dataclass, field, asdict
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple

# Import KNOT_AOR_MAPPING for adjacency relationships
try:
    from knot_aor_mapping import KNOT_AOR_MAPPING
except ImportError:
    # If running from scripts directory, try relative import
    sys.path.insert(0, str(Path(__file__).parent))
    from knot_aor_mapping import KNOT_AOR_MAPPING

# CSV injection prevention (reuse pattern from nku_scoring.py)
CSV_INJECTION_CHARS = ('=', '+', '-', '@', '\t', '\r', '\n')


def sanitize_csv_field(value: Optional[str]) -> str:
    """
    Sanitize a string field to prevent CSV injection attacks.
    
    Prefixes dangerous characters with a single quote when they appear 
    at the start of the string. Also replaces embedded newlines.
    
    Args:
        value: The string value to sanitize (can be None)
        
    Returns:
        Sanitized string safe for CSV output
    """
    if value is None:
        return ""
    
    # Replace embedded newlines to prevent row injection
    result = str(value).replace('\n', ' ').replace('\r', ' ')
    
    # Prefix dangerous starting characters
    if result and result[0] in CSV_INJECTION_CHARS:
        return "'" + result
    return result


@dataclass
class KNURewardEntry:
    """Represents a single KNU reward entry with effort, impact, and token allocation."""
    knu_id: str
    knot_id: str
    owner: str
    E_pred: float  # Predicted effort
    dR_primary: float  # Direct residue reduction in primary KNOT
    dR_adj_sum: float = 0.0  # Sum of residue reductions in adjacent KNOTs
    status: str = "draft"
    artifacts: List[str] = field(default_factory=list)
    validated_by: str = ""
    validated_at: str = ""
    weight: float = 0.0  # Calculated weight for distribution
    tokens_awarded: float = 0.0  # Tokens awarded
    
    def to_row(self) -> List[str]:
        """Convert to CSV row with sanitized fields."""
        artifacts_str = ";".join(self.artifacts) if self.artifacts else ""
        return [
            sanitize_csv_field(self.knot_id),
            sanitize_csv_field(self.knu_id),
            sanitize_csv_field(self.owner),
            sanitize_csv_field(str(self.E_pred)),
            sanitize_csv_field(str(self.dR_primary)),
            sanitize_csv_field(str(self.dR_adj_sum)),
            sanitize_csv_field(self.status),
            sanitize_csv_field(artifacts_str),
            sanitize_csv_field(self.validated_by),
            sanitize_csv_field(self.validated_at),
            sanitize_csv_field(f"{self.weight:.6f}"),
            sanitize_csv_field(f"{self.tokens_awarded:.2f}")
        ]
    
    @classmethod
    def from_row(cls, row: List[str]) -> "KNURewardEntry":
        """Create from CSV row."""
        # Handle rows with missing fields
        while len(row) < 12:
            row.append("")
        
        # Parse artifacts (semicolon-separated)
        artifacts = []
        if row[7].strip():
            artifacts = [a.strip() for a in row[7].split(";") if a.strip()]
        
        return cls(
            knot_id=row[0].strip(),
            knu_id=row[1].strip(),
            owner=row[2].strip(),
            E_pred=float(row[3].strip()) if row[3].strip() else 0.0,
            dR_primary=float(row[4].strip()) if row[4].strip() else 0.0,
            dR_adj_sum=float(row[5].strip()) if row[5].strip() else 0.0,
            status=row[6].strip() if row[6].strip() else "draft",
            artifacts=artifacts,
            validated_by=row[8].strip() if len(row) > 8 else "",
            validated_at=row[9].strip() if len(row) > 9 else "",
            weight=float(row[10].strip()) if len(row) > 10 and row[10].strip() else 0.0,
            tokens_awarded=float(row[11].strip()) if len(row) > 11 and row[11].strip() else 0.0
        )


@dataclass
class KNOTPool:
    """Token pool configuration for a specific KNOT."""
    knot_id: str
    pool_amount: float
    residue_before: float = 0.0
    residue_after: float = 0.0


class TokenDistributor:
    """
    Main token distribution engine for KNU rewards.
    
    Implements the distribution algorithm:
        w_i = α·Ê_i + (1-α)·Î_i
        T_i = P_k · w_i
    
    Example:
        With P_k=1000, α=0.30, λ=0.50:
        
        KNU1: E=5, ΔR_k=30, S=10 → I=35
        KNU2: E=3, ΔR_k=15, S=5 → I=17.5
        KNU3: E=2, ΔR_k=5, S=0 → I=5
        
        Sum: E_total=10, I_total=57.5
        
        KNU1: Ê=0.50, Î=0.609 → w=0.576 → T=576
        KNU2: Ê=0.30, Î=0.304 → w=0.303 → T=303
        KNU3: Ê=0.20, Î=0.087 → w=0.121 → T=121
    """
    
    CSV_HEADER = [
        "knot_id", "knu_id", "owner", "E_pred", "dR_primary", "dR_adj_sum",
        "status", "artifacts", "validated_by", "validated_at", "weight", "tokens_awarded"
    ]
    
    def __init__(self, config_path: Optional[Path] = None):
        """
        Initialize token distributor.
        
        Args:
            config_path: Path to configuration YAML file (default: config/tokenomics/knu_distribution.yaml)
        """
        if config_path is None:
            # Assume script is in scripts/ directory, config in config/
            repo_root = Path(__file__).parent.parent
            config_path = repo_root / "config" / "tokenomics" / "knu_distribution.yaml"
        
        self.config_path = config_path
        self.config = self._load_config()
        
        # Extract parameters
        self.alpha = self.config.get("parameters", {}).get("alpha", 0.30)
        self.lambda_spillover = self.config.get("parameters", {}).get("lambda_spillover", 0.50)
        self.eligibility = self.config.get("eligibility", {})
        self.knot_pools = self.config.get("knot_pools", {})
        self.adjacency_graph = self.config.get("adjacency_graph", {})
    
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from YAML file."""
        if not self.config_path.exists():
            print(f"Warning: Config file not found at {self.config_path}, using defaults", 
                  file=sys.stderr)
            return {}
        
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        except Exception as e:
            print(f"Error loading config: {e}", file=sys.stderr)
            return {}
    
    def calculate_spillover(self, knu: KNURewardEntry, 
                           adjacency_graph: Optional[Dict[str, Dict[str, float]]] = None) -> float:
        """
        Calculate spillover impact S_i for a KNU entry.
        
        Conceptual formula:
            S_i = Σ(a_k→j · ΔR_j,i) for adjacent KNOTs
        
        In this implementation, the spillover term is expected to be
        pre-computed externally (including adjacency weights a_k→j) and
        provided via ``knu.dR_adj_sum``:
        
            knu.dR_adj_sum ≡ Σ(a_k→j · ΔR_j,i)
        
        The ``adjacency_graph`` parameter is accepted for backwards and
        forwards compatibility but is not currently used inside this
        method. It allows future versions to derive ``dR_adj_sum`` from
        the graph if needed without changing the public API.
        
        Args:
            knu: KNU reward entry, with ``dR_adj_sum`` already including
                adjacency weights (Σ(a_k→j · ΔR_j,i)).
            adjacency_graph: Optional adjacency graph (currently unused in
                this calculation; kept for API compatibility).
        
        Returns:
            Spillover impact value (pre-weighted sum from ``knu.dR_adj_sum``).
        """
        # Mark adjacency_graph as intentionally unused for now while keeping
        # the parameter for API compatibility and potential future use.
        _ = adjacency_graph
        
        # If no dR_adj_sum provided, spillover is 0
        if knu.dR_adj_sum == 0.0:
            return 0.0
        
        # Spillover is provided as the pre-weighted sum of adjacent residue
        # reductions: knu.dR_adj_sum ≡ Σ(a_k→j · ΔR_j,i)
        return knu.dR_adj_sum
    
    def validate_eligibility(self, knu: KNURewardEntry) -> Tuple[bool, str]:
        """
        Check if KNU entry qualifies for rewards.
        
        Args:
            knu: KNU reward entry to validate
        
        Returns:
            Tuple of (is_eligible, reason)
        """
        # Check status
        required_statuses = self.eligibility.get("required_status", ["accepted", "merged"])
        if knu.status not in required_statuses:
            return (False, f"Status '{knu.status}' not in required statuses: {required_statuses}")
        
        # Check artifacts
        if self.eligibility.get("require_artifacts", True):
            if not knu.artifacts or len(knu.artifacts) == 0:
                return (False, "No artifacts provided")
        
        # Check validation
        if self.eligibility.get("require_validation", True):
            if not knu.validated_by or not knu.validated_at:
                return (False, "Not validated by authorized reviewer")
        
        return (True, "Eligible")
    
    def distribute_tokens(self, knot_pool: KNOTPool, knus: List[KNURewardEntry],
                         alpha: Optional[float] = None,
                         lambda_spill: Optional[float] = None) -> List[KNURewardEntry]:
        """
        Distribute tokens across KNU entries using the distribution formula.
        
        Formula:
            w_i = α·Ê_i + (1-α)·Î_i
            T_i = P_k · w_i
        
        Where:
            Ê_i = E_i / Σ E_i  (normalized effort)
            Î_i = I_i / Σ I_i  (normalized impact)
            I_i = ΔR_k,i + λ·S_i  (effective impact)
        
        Args:
            knot_pool: Pool configuration for the KNOT
            knus: List of KNU entries to distribute tokens to
            alpha: Override alpha parameter (effort weight)
            lambda_spill: Override lambda spillover parameter
        
        Returns:
            List of KNU entries with updated weights and token awards
        """
        # Use provided parameters or defaults
        alpha = alpha if alpha is not None else self.alpha
        lambda_spill = lambda_spill if lambda_spill is not None else self.lambda_spillover
        
        # Filter eligible entries
        eligible_knus = []
        for knu in knus:
            is_eligible, reason = self.validate_eligibility(knu)
            if is_eligible:
                eligible_knus.append(knu)
            else:
                print(f"  Skipping {knu.knu_id}: {reason}", file=sys.stderr)
        
        if not eligible_knus:
            print(f"Warning: No eligible KNU entries for {knot_pool.knot_id}", file=sys.stderr)
            return knus
        
        # Calculate spillover for each entry
        for knu in eligible_knus:
            # Spillover S_i is already in dR_adj_sum or calculate it
            # For this implementation, we assume dR_adj_sum contains the spillover
            pass
        
        # Calculate normalized effort Ê_i
        total_effort = sum(knu.E_pred for knu in eligible_knus)
        if total_effort == 0:
            # Equal effort if all are 0
            for knu in eligible_knus:
                knu.E_pred = 1.0
            total_effort = len(eligible_knus)
        
        normalized_efforts = {}
        for knu in eligible_knus:
            normalized_efforts[knu.knu_id] = knu.E_pred / total_effort
        
        # Calculate effective impact I_i = ΔR_k,i + λ·S_i
        effective_impacts = {}
        for knu in eligible_knus:
            spillover = self.calculate_spillover(knu)
            effective_impacts[knu.knu_id] = knu.dR_primary + lambda_spill * spillover
        
        # Calculate normalized impact Î_i
        total_impact = sum(effective_impacts.values())
        if total_impact == 0:
            # Equal impact if all are 0
            for knu_id in effective_impacts:
                effective_impacts[knu_id] = 1.0
            total_impact = len(eligible_knus)
        
        normalized_impacts = {}
        for knu_id, impact in effective_impacts.items():
            normalized_impacts[knu_id] = impact / total_impact
        
        # Calculate weights w_i = α·Ê_i + (1-α)·Î_i
        weights = {}
        for knu in eligible_knus:
            e_norm = normalized_efforts[knu.knu_id]
            i_norm = normalized_impacts[knu.knu_id]
            weights[knu.knu_id] = alpha * e_norm + (1 - alpha) * i_norm
        
        # Distribute tokens T_i = P_k · w_i
        for knu in eligible_knus:
            knu.weight = weights[knu.knu_id]
            knu.tokens_awarded = knot_pool.pool_amount * knu.weight
        
        return knus
    
    def load_knus_from_csv(self, csv_path: Path) -> List[KNURewardEntry]:
        """Load KNU entries from CSV file."""
        knus = []
        
        if not csv_path.exists():
            print(f"Warning: CSV file not found: {csv_path}", file=sys.stderr)
            return knus
        
        try:
            with open(csv_path, 'r', newline='', encoding='utf-8') as f:
                lines = f.readlines()
        except Exception as e:
            print(f"Error reading CSV file: {e}", file=sys.stderr)
            return knus
        
        # Filter out comment lines
        data_lines = [line for line in lines if not line.strip().startswith('#')]
        
        if not data_lines:
            return knus
        
        reader = csv.reader(data_lines)
        rows = list(reader)
        
        if not rows:
            return knus
        
        # Skip header row
        start_idx = 0
        if rows[0][0].lower().strip() in ['knot_id', 'knot']:
            start_idx = 1
        
        for row in rows[start_idx:]:
            if row and len(row) >= 3 and row[0].strip():
                try:
                    knu = KNURewardEntry.from_row(row)
                    knus.append(knu)
                except Exception as e:
                    print(f"Warning: Could not parse row {row}: {e}", file=sys.stderr)
        
        return knus
    
    def save_knus_to_csv(self, knus: List[KNURewardEntry], csv_path: Path) -> None:
        """Save KNU entries to CSV file."""
        try:
            csv_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(csv_path, 'w', newline='', encoding='utf-8') as f:
                # Write header comment
                f.write("# KNU Token Distribution Results\n")
                f.write(f"# Generated: {datetime.now().isoformat()}\n")
                f.write("#\n")
                
                writer = csv.writer(f)
                writer.writerow(self.CSV_HEADER)
                
                for knu in knus:
                    writer.writerow(knu.to_row())
        except Exception as e:
            print(f"Error writing CSV file: {e}", file=sys.stderr)
            raise
    
    def generate_report(self, knot_id: str, knus: List[KNURewardEntry],
                       pool: KNOTPool, alpha: float, lambda_spill: float) -> Dict[str, Any]:
        """
        Generate distribution report.
        
        Args:
            knot_id: KNOT identifier
            knus: List of KNU entries
            pool: Pool configuration
            alpha: Alpha parameter used
            lambda_spill: Lambda spillover parameter used
        
        Returns:
            Dictionary containing distribution report
        """
        eligible_knus = [knu for knu in knus if self.validate_eligibility(knu)[0]]
        total_tokens = sum(knu.tokens_awarded for knu in eligible_knus)
        
        report = {
            "generated_at": datetime.now().isoformat(),
            "knot_id": knot_id,
            "pool": asdict(pool),
            "parameters": {
                "alpha": alpha,
                "lambda_spillover": lambda_spill
            },
            "entries": [asdict(knu) for knu in knus],
            "total_tokens_distributed": total_tokens,
            "eligible_entries": len(eligible_knus)
        }
        
        return report


def cmd_distribute(args: argparse.Namespace, distributor: TokenDistributor) -> int:
    """Handle distribute command."""
    knot_id = args.knot.upper()
    
    # Get pool configuration
    pool_config = distributor.knot_pools.get(knot_id)
    if not pool_config:
        print(f"Error: No pool configuration found for {knot_id}", file=sys.stderr)
        return 1
    
    pool = KNOTPool(
        knot_id=knot_id,
        pool_amount=args.pool if args.pool else pool_config.get("base_pool", 1000)
    )
    
    # Load KNU entries
    if args.input:
        input_path = Path(args.input).resolve()
        knus = distributor.load_knus_from_csv(input_path)
    else:
        # Try to find default input file
        print(f"Error: --input required to specify KNU entries CSV", file=sys.stderr)
        return 1
    
    if not knus:
        print(f"Error: No KNU entries found", file=sys.stderr)
        return 1
    
    print(f"Distributing {pool.pool_amount} tokens for {knot_id}")
    print(f"Found {len(knus)} KNU entries")
    
    # Override parameters if provided
    alpha = args.alpha if args.alpha is not None else distributor.alpha
    lambda_spill = args.lambda_val if args.lambda_val is not None else distributor.lambda_spillover
    
    print(f"Using α={alpha:.2f} (effort weight), λ={lambda_spill:.2f} (spillover)")
    
    # Distribute tokens
    knus = distributor.distribute_tokens(pool, knus, alpha=alpha, lambda_spill=lambda_spill)
    
    # Save results
    output_path = Path(args.output).resolve() if args.output else input_path
    distributor.save_knus_to_csv(knus, output_path)
    
    # Print summary
    eligible_knus = [knu for knu in knus if distributor.validate_eligibility(knu)[0]]
    total_tokens = sum(knu.tokens_awarded for knu in eligible_knus)
    
    print(f"\n✅ Distribution complete!")
    print(f"   Eligible entries: {len(eligible_knus)}")
    print(f"   Total tokens distributed: {total_tokens:.2f}")
    print(f"   Results saved to: {output_path}")
    
    # Print top recipients
    eligible_knus.sort(key=lambda k: k.tokens_awarded, reverse=True)
    print(f"\n   Top recipients:")
    for knu in eligible_knus[:5]:
        print(f"     {knu.knu_id}: {knu.tokens_awarded:.2f} tokens (w={knu.weight:.4f})")
    
    return 0


def cmd_report(args: argparse.Namespace, distributor: TokenDistributor) -> int:
    """Handle report command."""
    knot_id = args.knot.upper()
    
    # Load KNU entries
    if args.input:
        input_path = Path(args.input).resolve()
        knus = distributor.load_knus_from_csv(input_path)
    else:
        print(f"Error: --input required to specify KNU entries CSV", file=sys.stderr)
        return 1
    
    # Get pool configuration
    pool_config = distributor.knot_pools.get(knot_id)
    if not pool_config:
        print(f"Error: No pool configuration found for {knot_id}", file=sys.stderr)
        return 1
    
    pool = KNOTPool(
        knot_id=knot_id,
        pool_amount=pool_config.get("base_pool", 1000)
    )
    
    # Generate report
    report = distributor.generate_report(
        knot_id, knus, pool,
        alpha=distributor.alpha,
        lambda_spill=distributor.lambda_spillover
    )
    
    # Output report
    if args.output:
        output_path = Path(args.output).resolve()
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(report, f, indent=2)
            print(f"✅ Report saved to: {output_path}")
        except Exception as e:
            print(f"Error writing report: {e}", file=sys.stderr)
            return 1
    else:
        print(json.dumps(report, indent=2))
    
    return 0


def cmd_validate(args: argparse.Namespace, distributor: TokenDistributor) -> int:
    """Handle validate command."""
    knot_id = args.knot.upper()
    knu_id = args.knu
    
    # Load KNU entries
    if args.input:
        input_path = Path(args.input).resolve()
        knus = distributor.load_knus_from_csv(input_path)
    else:
        print(f"Error: --input required to specify KNU entries CSV", file=sys.stderr)
        return 1
    
    # Find the specific KNU
    target_knu = None
    for knu in knus:
        if knu.knu_id == knu_id and knu.knot_id == knot_id:
            target_knu = knu
            break
    
    if not target_knu:
        print(f"Error: KNU {knu_id} not found in {knot_id}", file=sys.stderr)
        return 1
    
    # Validate eligibility
    is_eligible, reason = distributor.validate_eligibility(target_knu)
    
    print(f"\nKNU Entry: {knu_id}")
    print(f"  KNOT: {target_knu.knot_id}")
    print(f"  Owner: {target_knu.owner}")
    print(f"  Status: {target_knu.status}")
    print(f"  Effort: {target_knu.E_pred}")
    print(f"  Primary Impact: {target_knu.dR_primary}")
    print(f"  Adjacent Impact: {target_knu.dR_adj_sum}")
    print(f"  Artifacts: {len(target_knu.artifacts)}")
    print(f"  Validated: {'Yes' if target_knu.validated_by else 'No'}")
    
    if is_eligible:
        print(f"\n✅ ELIGIBLE for token rewards")
    else:
        print(f"\n❌ NOT ELIGIBLE: {reason}")
        return 1
    
    return 0


def main() -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="AMPEL360 Space-T KNU Token Distribution System",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        "--config",
        help="Path to configuration YAML file (default: config/tokenomics/knu_distribution.yaml)"
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # distribute command
    dist_parser = subparsers.add_parser("distribute", help="Distribute tokens for a KNOT")
    dist_parser.add_argument("--knot", required=True, help="KNOT ID (e.g., K06)")
    dist_parser.add_argument("--pool", type=float, help="Pool amount (overrides config)")
    dist_parser.add_argument("--input", required=True, help="Input CSV file with KNU entries")
    dist_parser.add_argument("--output", help="Output CSV file (default: overwrite input)")
    dist_parser.add_argument("--alpha", type=float, help="Effort weight (0.0-1.0, default: 0.30)")
    dist_parser.add_argument("--lambda", dest="lambda_val", type=float,
                            help="Spillover multiplier (0.0-1.0, default: 0.50)")
    
    # report command
    report_parser = subparsers.add_parser("report", help="Generate distribution report")
    report_parser.add_argument("--knot", required=True, help="KNOT ID (e.g., K06)")
    report_parser.add_argument("--input", required=True, help="Input CSV file with KNU entries")
    report_parser.add_argument("--output", "-o", help="Output JSON file (default: stdout)")
    
    # validate command
    validate_parser = subparsers.add_parser("validate", help="Validate KNU eligibility")
    validate_parser.add_argument("--knot", required=True, help="KNOT ID (e.g., K06)")
    validate_parser.add_argument("--knu", required=True, help="KNU ID to validate")
    validate_parser.add_argument("--input", required=True, help="Input CSV file with KNU entries")
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return 1
    
    # Initialize distributor
    config_path = Path(args.config).resolve() if args.config else None
    distributor = TokenDistributor(config_path=config_path)
    
    if args.command == "distribute":
        return cmd_distribute(args, distributor)
    elif args.command == "report":
        return cmd_report(args, distributor)
    elif args.command == "validate":
        return cmd_validate(args, distributor)
    else:
        parser.print_help()
        return 1


if __name__ == "__main__":
    sys.exit(main())
