#!/usr/bin/env python3
"""
AMPEL360 Space-T Shadow Registry Detection Script
==================================================
Version: 1.0
Date: 2026-01-07
Task: GATE-017 implementation for Weekly Governance Audit

Detects "shadow registries" - uncoordinated lists of IDs or schemas that
should be centrally managed in official registries (ATA 91, ATA 93, ATA 99).

Shadow registries are problematic because they:
- Create duplicate/conflicting identifier definitions
- Bypass governance approval processes
- Cause synchronization and maintenance issues
- Lead to namespace collisions

This script detects:
- CSV files that look like registries but aren't the official ones
- JSON files with lists of schema IDs
- Markdown files with ID allocation tables
- YAML files with namespace definitions

Usage:
    python scripts/detect_shadow_registries.py --namespaces ATA99
    python scripts/detect_shadow_registries.py --all
    python scripts/detect_shadow_registries.py --check-schemas

Exit codes:
    0: No shadow registries found
    1: Shadow registries detected
    2: Script error
"""

import argparse
import csv
import json
import os
import re
import sys
import yaml  # Requires PyYAML>=6.0 (declared in scripts/requirements.txt)
from pathlib import Path
from typing import List

# Known official registries (whitelist)
OFFICIAL_REGISTRIES = {
    # ATA 91 - Schema Registry
    '91_AMPEL360_SPACET_Q10_GEN_PLUS_BB_B30_SB91_K06_DATA__schema-registry_TAB_I01-R01_ACTIVE.csv',
    
    # ATA 93 - Trace Link Registry (when created)
    # '93_AMPEL360_SPACET_Q10_GEN_PLUS_BB_B30_SB93_K06_DATA__trace-registry_TAB_I01-R01_ACTIVE.csv',
    
    # ATA 99 - Namespace Registry (when created)
    # '99_AMPEL360_SPACET_Q10_GEN_PLUS_BB_B30_SB99_K06_DATA__namespace-registry_TAB_I01-R01_ACTIVE.csv',
    
    # Knot Register (official)
    '00_AMPEL360_SPACET_Q10_GEN_PLUS_BB_GEN_LC01_K05_DATA__knot-register_TAB_I01-R01_ACTIVE.csv',
}

# Suspicious patterns that indicate shadow registries
SHADOW_PATTERNS = {
    'schema_list': r'schema[_-]?(id|list|inventory|catalog)',
    'namespace_list': r'namespace[_-]?(id|list|registry|allocation)',
    'id_list': r'(id|identifier)[_-]?(list|registry|allocation|catalog)',
    'registry': r'registry(?!\.py)',  # registry but not Python scripts
}

# Suspicious CSV column patterns
REGISTRY_COLUMN_PATTERNS = {
    'schema': ['schema_id', 'schema_name', '$id', 'schema_uri'],
    'namespace': ['namespace', 'namespace_id', 'ns_id'],
    'trace': ['trace_id', 'trace_type', 'source_id', 'target_id'],
    'id_allocation': ['id', 'identifier', 'canonical_id', 'uuid'],
}


class ShadowRegistry:
    """Represents a detected shadow registry."""
    
    def __init__(self, path: Path, reason: str, severity: str = "WARNING", evidence: str = ""):
        self.path = path
        self.reason = reason
        self.severity = severity
        self.evidence = evidence
    
    def __str__(self) -> str:
        result = f"[{self.severity}] {self.path}\n  Reason: {self.reason}"
        if self.evidence:
            result += f"\n  Evidence: {self.evidence}"
        return result


class ShadowRegistryDetector:
    """Detects shadow registries in the repository."""
    
    def __init__(self, repo_root: Path):
        self.repo_root = repo_root
        self.shadow_registries: List[ShadowRegistry] = []
        self.checked_files = 0
        self.excluded_dirs = {'.git', 'node_modules', '__pycache__', '.github', '.vscode', 'templates'}
    
    def is_official_registry(self, file_path: Path) -> bool:
        """Check if file is an official registry."""
        return file_path.name in OFFICIAL_REGISTRIES
    
    def check_csv_file(self, file_path: Path) -> None:
        """Check if a CSV file is a shadow registry."""
        if self.is_official_registry(file_path):
            return
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                headers = reader.fieldnames or []
                
                # Check for suspicious column patterns
                for registry_type, suspicious_cols in REGISTRY_COLUMN_PATTERNS.items():
                    matches = [col for col in headers if col.lower() in [s.lower() for s in suspicious_cols]]
                    
                    if len(matches) >= 2:  # At least 2 matching columns
                        # Read a few rows to confirm
                        sample_rows = []
                        try:
                            f.seek(0)
                            reader = csv.DictReader(f)
                            sample_rows = list(row for _, row in zip(range(3), reader))
                        except:
                            pass
                        
                        if len(sample_rows) > 0:
                            self.shadow_registries.append(
                                ShadowRegistry(
                                    path=file_path.relative_to(self.repo_root),
                                    reason=f"CSV file appears to be a {registry_type} registry",
                                    severity="WARNING",
                                    evidence=f"Contains columns: {', '.join(matches)}"
                                )
                            )
                            break
        
        except (csv.Error, UnicodeDecodeError, OSError):
            pass
    
    def check_json_file(self, file_path: Path) -> None:
        """Check if a JSON file contains a shadow registry."""
        if self.is_official_registry(file_path):
            return
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Check for arrays of schemas or namespaces
            if isinstance(data, dict):
                for key in data.keys():
                    key_lower = key.lower()
                    
                    # Check for suspicious keys
                    if any(pattern in key_lower for pattern in ['schemas', 'namespaces', 'registr']):
                        value = data[key]
                        
                        if isinstance(value, list) and len(value) > 2:
                            # Check if list items look like registry entries
                            if all(isinstance(item, dict) for item in value[:3]):
                                self.shadow_registries.append(
                                    ShadowRegistry(
                                        path=file_path.relative_to(self.repo_root),
                                        reason=f"JSON file contains list that looks like a registry",
                                        severity="INFO",
                                        evidence=f"Key '{key}' contains {len(value)} entries"
                                    )
                                )
                                break
        
        except (json.JSONDecodeError, UnicodeDecodeError, OSError):
            pass
    
    def check_yaml_file(self, file_path: Path) -> None:
        """Check if a YAML file contains a shadow registry."""
        if self.is_official_registry(file_path):
            return
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
            
            if isinstance(data, dict):
                for key in data.keys():
                    key_lower = str(key).lower()
                    
                    # Check for suspicious keys
                    if any(pattern in key_lower for pattern in ['schemas', 'namespaces', 'registr', 'identifiers']):
                        value = data[key]
                        
                        if isinstance(value, (list, dict)) and len(value) > 2:
                            self.shadow_registries.append(
                                ShadowRegistry(
                                    path=file_path.relative_to(self.repo_root),
                                    reason=f"YAML file contains configuration that looks like a registry",
                                    severity="INFO",
                                    evidence=f"Key '{key}' contains {len(value)} entries"
                                )
                            )
                            break
        
        except (yaml.YAMLError, UnicodeDecodeError, OSError):
            pass
    
    def check_markdown_table(self, file_path: Path) -> None:
        """Check if a Markdown file contains ID allocation tables."""
        if self.is_official_registry(file_path):
            return
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Look for tables with suspicious headers
            table_pattern = r'\|[^\n]*(?:schema|namespace|identifier|registry)[^\n]*\|'
            matches = re.findall(table_pattern, content, re.IGNORECASE)
            
            if len(matches) >= 3:  # At least a header and 2 rows
                # Check if it's not just a reference to official registries
                if not any(reg_name in content for reg_name in OFFICIAL_REGISTRIES):
                    self.shadow_registries.append(
                        ShadowRegistry(
                            path=file_path.relative_to(self.repo_root),
                            reason="Markdown file contains table that may be a shadow registry",
                            severity="INFO",
                            evidence=f"Found {len(matches)} table rows with registry-like headers"
                        )
                    )
        
        except (UnicodeDecodeError, OSError):
            pass
    
    def check_filename_patterns(self, file_path: Path) -> None:
        """Check if filename suggests shadow registry."""
        if self.is_official_registry(file_path):
            return
        
        filename_lower = file_path.name.lower()
        
        for pattern_name, pattern in SHADOW_PATTERNS.items():
            if re.search(pattern, filename_lower):
                # Reduce false positives: check file extension and size
                if file_path.suffix in ['.csv', '.json', '.yaml', '.yml']:
                    try:
                        size = os.path.getsize(file_path)
                        if size > 100:  # Only flag non-trivial files
                            self.shadow_registries.append(
                                ShadowRegistry(
                                    path=file_path.relative_to(self.repo_root),
                                    reason=f"Filename suggests a {pattern_name} shadow registry",
                                    severity="INFO",
                                    evidence=f"Pattern '{pattern}' matched in filename"
                                )
                            )
                    except OSError:
                        pass
    
    def scan_repository(self) -> None:
        """Scan repository for shadow registries."""
        print(f"🔍 Scanning repository for shadow registries...")
        print(f"   Root: {self.repo_root}")
        print(f"   Official registries: {len(OFFICIAL_REGISTRIES)}")
        
        for root, dirs, files in os.walk(self.repo_root):
            # Remove excluded directories from search
            dirs[:] = [d for d in dirs if d not in self.excluded_dirs]
            
            for file in files:
                file_path = Path(root) / file
                self.checked_files += 1
                
                # Check based on file type
                if file_path.suffix == '.csv':
                    self.check_csv_file(file_path)
                elif file_path.suffix == '.json':
                    self.check_json_file(file_path)
                elif file_path.suffix in ['.yaml', '.yml']:
                    self.check_yaml_file(file_path)
                elif file_path.suffix == '.md':
                    self.check_markdown_table(file_path)
                
                # Check filename patterns
                self.check_filename_patterns(file_path)
    
    def print_summary(self) -> None:
        """Print shadow registry detection summary."""
        print("\n" + "=" * 60)
        print("SHADOW REGISTRY DETECTION SUMMARY")
        print("=" * 60)
        
        print(f"\n📋 Checked {self.checked_files} files")
        print(f"   Official registries: {len(OFFICIAL_REGISTRIES)}")
        
        if not self.shadow_registries:
            print("\n✅ No shadow registries detected")
            return
        
        # Remove duplicates (same file flagged multiple times)
        unique_paths = {}
        for shadow in self.shadow_registries:
            path_str = str(shadow.path)
            if path_str not in unique_paths or unique_paths[path_str].severity == "INFO":
                unique_paths[path_str] = shadow
        
        shadow_list = list(unique_paths.values())
        
        # Group by severity
        warnings = [s for s in shadow_list if s.severity == "WARNING"]
        infos = [s for s in shadow_list if s.severity == "INFO"]
        
        if warnings:
            print(f"\n⚠️  WARNINGS ({len(warnings)}):")
            for shadow in warnings:
                print(f"\n{shadow}")
        
        if infos:
            print(f"\n📋 INFO ({len(infos)}):")
            for shadow in infos[:10]:  # Limit to first 10
                print(f"\n{shadow}")
            if len(infos) > 10:
                print(f"\n  ... and {len(infos) - 10} more informational findings")
        
        print("\n" + "=" * 60)
        if warnings:
            print(f"⚠️  SHADOW REGISTRIES DETECTED - {len(warnings)} warnings, {len(infos)} info")
        else:
            print(f"✅ VALIDATION PASSED - Only informational messages ({len(infos)})")
        print("=" * 60)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Detect shadow registries in AMPEL360 Space-T repository"
    )
    parser.add_argument(
        '--all',
        action='store_true',
        help='Check for all types of shadow registries'
    )
    parser.add_argument(
        '--namespaces',
        type=str,
        help='Specific namespace to check (e.g., ATA99)'
    )
    parser.add_argument(
        '--check-schemas',
        action='store_true',
        help='Focus on schema registry shadows'
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
    
    detector = ShadowRegistryDetector(repo_root)
    
    try:
        detector.scan_repository()
        detector.print_summary()
        
        # Return exit code based on warnings
        warnings = [s for s in detector.shadow_registries if s.severity == "WARNING"]
        return 1 if warnings else 0
        
    except Exception as e:
        print(f"❌ Error during shadow registry detection: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return 2


if __name__ == "__main__":
    sys.exit(main())
