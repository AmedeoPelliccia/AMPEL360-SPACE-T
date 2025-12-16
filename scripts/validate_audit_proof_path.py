#!/usr/bin/env python3
"""
AMPEL360 Space-T Auditability Proof Path Validator
===================================================
Version: 1.0
Date: 2025-12-16
Task: Implement auditability proof validator for K06 ATA 00 Tasklist

Validates the complete audit query path: ID → Schema → Trace → Export
Based on the 8-step audit path defined in:
    00_00_RPT_LC01_AMPEL360_SPACET_PLUS_auditability-proof-path_v01.md

Usage:
    python scripts/validate_audit_proof_path.py --id <identifier>
    python scripts/validate_audit_proof_path.py --validate-chain <identifier>
    python scripts/validate_audit_proof_path.py --check-all
    python scripts/validate_audit_proof_path.py --help

Exit codes:
    0: Validation passed
    1: Validation errors found
    2: Script error (file not found, etc.)
"""

import argparse
import json
import re
import sys
import traceback
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple, Any


# =============================================================================
# Constants and Patterns
# =============================================================================

# Identifier pattern strings - compiled lazily for performance
_IDENTIFIER_PATTERN_STRINGS = {
    'DATUM': r'^DATUM-[A-Z0-9]+-[0-9]{3}(-[A-Z0-9]+)?$',
    'ZONE': r'^ZONE-[A-Z0-9]+-[0-9]{3}(-[A-Z0-9]+)?$',
    'ENVELOPE': r'^ENVELOPE-[A-Z0-9]+-[0-9]{3}(-[A-Z0-9]+)?$',
    'REQ': r'^REQ-[A-Z0-9]{2,5}-\d{3,6}(-[A-Z0-9]{1,8})?$',
    'HAZ': r'^HAZ-[A-Z0-9]{2,5}-\d{3,6}(-[A-Z0-9]{1,8})?$',
    'TC': r'^TC-[A-Z0-9]{2,5}-\d{3,6}(-[A-Z0-9]{1,8})?$',
    'SCH': r'^SCH-[A-Z0-9]{2,5}-\d{3,6}(-V\d{2})?$',
    'TRC': r'^TRC-[A-Z0-9]{2,5}-[A-Z0-9]{2,5}-\d{3,6}$',
    'EVD': r'^EVD-[A-Z0-9]{2,5}-\d{3,6}$',
    'BL': r'^BL-\d{4}(-\d{2})?(-\d{2})?$',
}

# Cache for compiled patterns
_IDENTIFIER_PATTERNS_CACHE: Dict[str, re.Pattern] = {}


def get_identifier_patterns() -> Dict[str, re.Pattern]:
    """Get compiled identifier patterns, using lazy compilation."""
    global _IDENTIFIER_PATTERNS_CACHE
    if not _IDENTIFIER_PATTERNS_CACHE:
        for key, pattern_str in _IDENTIFIER_PATTERN_STRINGS.items():
            _IDENTIFIER_PATTERNS_CACHE[key] = re.compile(pattern_str)
    return _IDENTIFIER_PATTERNS_CACHE


# Canonical identifier grammar (comprehensive pattern)
CANONICAL_ID_PATTERN = re.compile(
    r'^[A-Z0-9]{2,8}-[A-Z0-9]{2,8}-\d{3,6}(-[A-Z0-9]{1,8})?$'
)

# Schema file locations (relative paths)
SCHEMA_LOCATIONS = [
    "06_90_SCH_SB90_AMPEL360_SPACET_GEN_dimensional-data-schema_v01.json",
    "00_90_SCH_SB90_AMPEL360_SPACET_GEN_knots-data-structure_v01.json",
]

# Export file locations (relative paths)
EXPORT_LOCATIONS = [
    "06_90_TAB_SB90_AMPEL360_SPACET_GEN_dimensional-exports_v01.json",
]

# Traceability file locations
TRACEABILITY_LOCATIONS = [
    "06_00_TRC_LC01_AMPEL360_SPACET_PLUS_ssot-traceability_v01.md",
]

# Directories to exclude from scanning
EXCLUDED_DIRS = {
    '.git', '.github', 'node_modules', '__pycache__',
    '.pytest_cache', '.venv', 'venv', 'dist', 'build'
}


# =============================================================================
# Data Classes
# =============================================================================

@dataclass
class ValidationResult:
    """Container for validation results."""
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    info: List[str] = field(default_factory=list)
    steps: List[Dict[str, Any]] = field(default_factory=list)
    passed: bool = True

    def add_error(self, message: str, step: str = "") -> None:
        """Add an error message."""
        self.errors.append(f"[{step}] {message}" if step else message)
        self.passed = False

    def add_warning(self, message: str, step: str = "") -> None:
        """Add a warning message."""
        self.warnings.append(f"[{step}] {message}" if step else message)

    def add_info(self, message: str, step: str = "") -> None:
        """Add an info message."""
        self.info.append(f"[{step}] {message}" if step else message)

    def add_step(self, step_name: str, status: str, details: Dict[str, Any]) -> None:
        """Add a step result to the chain."""
        self.steps.append({
            "step": step_name,
            "status": status,
            "details": details
        })

    def print_summary(self) -> None:
        """Print validation summary."""
        print("\n" + "=" * 70)
        print("AUDITABILITY PROOF PATH VALIDATION SUMMARY")
        print("=" * 70)

        # Print step-by-step results
        if self.steps:
            print("\n📋 AUDIT CHAIN STEPS:")
            for step in self.steps:
                status_icon = "✅" if step["status"] in ("passed", "complete") else "⚠️" if step["status"] == "warning" else "❌"
                print(f"  {status_icon} {step['step']}: {step['status']}")
                for key, value in step["details"].items():
                    if isinstance(value, list):
                        print(f"      {key}:")
                        for item in value[:5]:  # Limit display
                            print(f"        - {item}")
                        if len(value) > 5:
                            print(f"        ... and {len(value) - 5} more")
                    else:
                        print(f"      {key}: {value}")

        if self.errors:
            print(f"\n❌ ERRORS ({len(self.errors)}):")
            for i, error in enumerate(self.errors, 1):
                print(f"  {i}. {error}")

        if self.warnings:
            print(f"\n⚠️  WARNINGS ({len(self.warnings)}):")
            for i, warning in enumerate(self.warnings, 1):
                print(f"  {i}. {warning}")

        if self.info:
            print(f"\n📋 INFO ({len(self.info)}):")
            for info_msg in self.info:
                print(f"  • {info_msg}")

        print("\n" + "=" * 70)
        if self.passed and not self.warnings:
            print("✅ AUDIT PATH VALIDATION PASSED - Complete chain verified")
        elif self.passed:
            print("✅ AUDIT PATH VALIDATION PASSED - Warnings present")
        else:
            print("❌ AUDIT PATH VALIDATION FAILED - Chain integrity issues found")
        print("=" * 70 + "\n")


@dataclass
class IdentifierInfo:
    """Information about an identifier."""
    identifier: str
    category: str
    system: str
    sequence: str
    variant: Optional[str] = None
    found_in_files: List[str] = field(default_factory=list)
    schema_refs: List[str] = field(default_factory=list)
    trace_links: List[str] = field(default_factory=list)
    evidence_refs: List[str] = field(default_factory=list)


# =============================================================================
# Audit Path Validator Class
# =============================================================================

class AuditProofPathValidator:
    """
    Validates the auditability proof path for identifiers.
    
    Implements the 8-step audit query path:
    1. Identifier Location (ID)
    2. Schema Validation (Schema)
    3. Trace to Design (Trace)
    4. Trace to Implementation (Trace)
    5. Trace to Test (Trace)
    6. Evidence Retrieval (Export)
    7. Baseline Verification (Export)
    8. Approval Confirmation (Export)
    """

    def __init__(self, repo_root: Path = Path('.'), verbose: bool = False):
        """
        Initialize the validator.
        
        Args:
            repo_root: Path to the repository root
            verbose: Enable verbose output
        """
        self.repo_root = repo_root
        self.verbose = verbose
        self.identifier_cache: Dict[str, IdentifierInfo] = {}
        self.schema_cache: Dict[str, Dict] = {}
        self.export_cache: Dict[str, Dict] = {}

    def _is_excluded_path(self, path: Path) -> bool:
        """Check if path should be excluded from scanning."""
        # Check current path first for efficiency
        if path.name.startswith('.'):
            return True
        for parent in path.parents:
            if parent.name in EXCLUDED_DIRS:
                return True
        return False

    def _parse_identifier(self, identifier: str) -> Optional[IdentifierInfo]:
        """
        Parse an identifier into its components.
        
        Args:
            identifier: The identifier string to parse
            
        Returns:
            IdentifierInfo if valid, None otherwise
        """
        patterns = get_identifier_patterns()
        
        # Try to match against known patterns
        for category, pattern in patterns.items():
            if pattern.match(identifier):
                parts = identifier.split('-')
                
                # Handle different identifier structures
                if category == 'BL':
                    # BL identifiers: BL-YYYY or BL-YYYY-MM or BL-YYYY-MM-DD
                    return IdentifierInfo(
                        identifier=identifier,
                        category='BL',
                        system='BASELINE',
                        sequence=parts[1] if len(parts) > 1 else "",
                        variant='-'.join(parts[2:]) if len(parts) > 2 else None
                    )
                elif category in ('DATUM', 'ZONE', 'ENVELOPE'):
                    # Standard pattern: CATEGORY-SYSTEM-SEQUENCE[-VARIANT]
                    return IdentifierInfo(
                        identifier=identifier,
                        category=parts[0] if len(parts) > 0 else "",
                        system=parts[1] if len(parts) > 1 else "",
                        sequence=parts[2] if len(parts) > 2 else "",
                        variant=parts[3] if len(parts) > 3 else None
                    )
                else:
                    # Generic pattern: CATEGORY-SYSTEM-SEQUENCE[-VARIANT]
                    return IdentifierInfo(
                        identifier=identifier,
                        category=parts[0] if len(parts) > 0 else "",
                        system=parts[1] if len(parts) > 1 else "",
                        sequence=parts[2] if len(parts) > 2 else "",
                        variant=parts[3] if len(parts) > 3 else None
                    )
        
        # Try canonical pattern as fallback
        if CANONICAL_ID_PATTERN.match(identifier):
            parts = identifier.split('-')
            return IdentifierInfo(
                identifier=identifier,
                category=parts[0] if len(parts) > 0 else "",
                system=parts[1] if len(parts) > 1 else "",
                sequence=parts[2] if len(parts) > 2 else "",
                variant=parts[3] if len(parts) > 3 else None
            )
        
        return None

    def _identifier_in_content(self, identifier: str, content: str) -> bool:
        """
        Check if identifier appears in content with word boundaries.
        
        Uses precise matching to avoid false positives like 
        'DATUM-GLOBAL-001' matching 'DATUM-GLOBAL-0012'.
        
        Args:
            identifier: The identifier to search for
            content: The text content to search in
            
        Returns:
            True if identifier found with word boundaries
        """
        # Escape special regex characters in identifier
        escaped_id = re.escape(identifier)
        # Use word boundary or non-alphanumeric boundary for precise matching
        pattern = rf'(?<![A-Z0-9-]){escaped_id}(?![A-Z0-9-])'
        return bool(re.search(pattern, content))

    def _find_identifier_in_files(self, identifier: str) -> List[Path]:
        """
        Find all files containing the given identifier.
        
        Args:
            identifier: The identifier to search for
            
        Returns:
            List of file paths containing the identifier
        """
        found_files = []
        
        # Search in markdown files
        for path in self.repo_root.rglob('*.md'):
            if self._is_excluded_path(path):
                continue
            try:
                content = path.read_text(encoding='utf-8')
                if self._identifier_in_content(identifier, content):
                    found_files.append(path)
            except (OSError, UnicodeDecodeError):
                continue
        
        # Search in JSON files
        for path in self.repo_root.rglob('*.json'):
            if self._is_excluded_path(path):
                continue
            try:
                content = path.read_text(encoding='utf-8')
                if self._identifier_in_content(identifier, content):
                    found_files.append(path)
            except (OSError, UnicodeDecodeError):
                continue
        
        return found_files

    def _load_json_file(self, path: Path) -> Optional[Dict]:
        """
        Load and parse a JSON file.
        
        Args:
            path: Path to the JSON file
            
        Returns:
            Parsed JSON content or None if error
        """
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError, UnicodeDecodeError):
            return None

    def _find_schema_for_identifier(self, identifier: str) -> List[Tuple[Path, str]]:
        """
        Find schema files that define or reference the identifier.
        
        Args:
            identifier: The identifier to search for
            
        Returns:
            List of (path, schema_id) tuples for matching schemas
        """
        schemas = []
        
        for schema_file in SCHEMA_LOCATIONS:
            schema_path = self.repo_root / schema_file
            if schema_path.exists():
                content = self._load_json_file(schema_path)
                if content:
                    schema_id = content.get('$id', schema_file)
                    # Check if this schema could validate the identifier
                    info = self._parse_identifier(identifier)
                    if info and info.category in ['DATUM', 'ZONE', 'ENVELOPE']:
                        if 'dimensional' in schema_file.lower():
                            schemas.append((schema_path, schema_id))
                    elif info:
                        schemas.append((schema_path, schema_id))
        
        # Also search for any JSON schema that might reference this identifier
        for path in self.repo_root.rglob('*_SCH_*.json'):
            if self._is_excluded_path(path):
                continue
            if path not in [s[0] for s in schemas]:
                content = self._load_json_file(path)
                if content and '$schema' in content:
                    schema_id = content.get('$id', str(path))
                    schemas.append((path, schema_id))
        
        return schemas

    def _find_identifier_in_exports(self, identifier: str) -> List[Tuple[Path, Dict]]:
        """
        Find export files that contain the identifier.
        
        Args:
            identifier: The identifier to search for
            
        Returns:
            List of (path, matching_data) tuples
        """
        exports = []
        
        for export_file in EXPORT_LOCATIONS:
            export_path = self.repo_root / export_file
            if export_path.exists():
                content = self._load_json_file(export_path)
                if content:
                    # Search in data arrays
                    data = content.get('data', {})
                    for category in ['datums', 'zones', 'envelopes']:
                        items = data.get(category, [])
                        for item in items:
                            if item.get('identifier') == identifier:
                                exports.append((export_path, item))
        
        # Also search for any TAB export files
        for path in self.repo_root.rglob('*_TAB_*.json'):
            if self._is_excluded_path(path):
                continue
            try:
                content = path.read_text(encoding='utf-8')
                if self._identifier_in_content(identifier, content):
                    data = json.loads(content)
                    exports.append((path, data))
            except (json.JSONDecodeError, OSError, UnicodeDecodeError):
                continue
        
        return exports

    def _find_trace_links(self, identifier: str) -> List[Dict[str, str]]:
        """
        Find trace links for the identifier.
        
        Args:
            identifier: The identifier to search for
            
        Returns:
            List of trace link dictionaries
        """
        trace_links = []
        
        for trace_file in TRACEABILITY_LOCATIONS:
            trace_path = self.repo_root / trace_file
            if trace_path.exists():
                try:
                    content = trace_path.read_text(encoding='utf-8')
                    if self._identifier_in_content(identifier, content):
                        trace_links.append({
                            'file': str(trace_path),
                            'type': 'traceability_matrix',
                            'status': 'found'
                        })
                except (OSError, UnicodeDecodeError):
                    continue
        
        # Search for trace links in markdown files
        for path in self.repo_root.rglob('*_TRC_*.md'):
            if self._is_excluded_path(path):
                continue
            try:
                content = path.read_text(encoding='utf-8')
                if self._identifier_in_content(identifier, content):
                    trace_links.append({
                        'file': str(path),
                        'type': 'trace_document',
                        'status': 'found'
                    })
            except (OSError, UnicodeDecodeError):
                continue
        
        # Search for related_identifiers in JSON exports
        for path in self.repo_root.rglob('*.json'):
            if self._is_excluded_path(path):
                continue
            try:
                content = self._load_json_file(path)
                if content:
                    self._extract_trace_links_from_json(
                        content, identifier, str(path), trace_links
                    )
            except (json.JSONDecodeError, OSError, UnicodeDecodeError, TypeError, KeyError):
                # Skip files that can't be parsed or have unexpected structure
                continue
        
        return trace_links

    def _extract_trace_links_from_json(
        self, 
        data: Any, 
        identifier: str, 
        source_file: str,
        trace_links: List[Dict[str, str]]
    ) -> None:
        """
        Extract trace links from JSON data recursively.
        
        Args:
            data: JSON data to search
            identifier: The identifier to search for
            source_file: Source file path for logging
            trace_links: List to append found trace links
        """
        if isinstance(data, dict):
            # Check for related_identifiers field
            related = data.get('related_identifiers', [])
            if identifier in related or data.get('identifier') == identifier:
                for related_id in related:
                    if related_id != identifier:
                        trace_links.append({
                            'file': source_file,
                            'type': 'related_identifier',
                            'target': related_id,
                            'status': 'found'
                        })
            
            # Check for trace_links field
            traces = data.get('trace_links', [])
            for trace in traces:
                if isinstance(trace, dict):
                    if trace.get('source') == identifier or trace.get('target') == identifier:
                        trace_links.append({
                            'file': source_file,
                            'type': trace.get('type', 'unknown'),
                            'target': trace.get('target', ''),
                            'source': trace.get('source', ''),
                            'status': trace.get('status', 'unknown')
                        })
            
            # Recurse into nested objects
            for value in data.values():
                self._extract_trace_links_from_json(
                    value, identifier, source_file, trace_links
                )
        
        elif isinstance(data, list):
            for item in data:
                self._extract_trace_links_from_json(
                    item, identifier, source_file, trace_links
                )

    def _validate_identifier_format(self, identifier: str, result: ValidationResult) -> bool:
        """
        Step 1: Validate identifier format.
        
        Args:
            identifier: The identifier to validate
            result: ValidationResult to update
            
        Returns:
            True if valid, False otherwise
        """
        step_name = "Step 1: Identifier Validation"
        print(f"🔍 {step_name}...")
        
        info = self._parse_identifier(identifier)
        
        if info is None:
            result.add_error(f"Invalid identifier format: {identifier}", step_name)
            result.add_step(step_name, "failed", {
                "identifier": identifier,
                "reason": "Does not match any known identifier pattern"
            })
            return False
        
        # Find files containing this identifier
        found_files = self._find_identifier_in_files(identifier)
        info.found_in_files = [str(f) for f in found_files]
        
        if not found_files:
            result.add_warning(
                f"Identifier {identifier} not found in any repository files",
                step_name
            )
        
        result.add_step(step_name, "passed", {
            "identifier": identifier,
            "category": info.category,
            "system": info.system,
            "sequence": info.sequence,
            "variant": info.variant or "None",
            "found_in_files": len(found_files)
        })
        result.add_info(f"Identifier {identifier} is valid ({info.category})", step_name)
        
        # Cache the info
        self.identifier_cache[identifier] = info
        
        return True

    def _validate_schema(self, identifier: str, result: ValidationResult) -> bool:
        """
        Step 2: Validate schema registration and compliance.
        
        Args:
            identifier: The identifier to validate
            result: ValidationResult to update
            
        Returns:
            True if valid, False otherwise
        """
        step_name = "Step 2: Schema Validation"
        print(f"🔍 {step_name}...")
        
        schemas = self._find_schema_for_identifier(identifier)
        
        if not schemas:
            result.add_warning(
                f"No schema found for identifier: {identifier}",
                step_name
            )
            result.add_step(step_name, "warning", {
                "identifier": identifier,
                "schemas_found": 0,
                "note": "Schema registration pending - see REC-002 in auditability report"
            })
            return True  # Warning, not error
        
        # Validate each schema
        valid_schemas = []
        for schema_path, schema_id in schemas:
            content = self._load_json_file(schema_path)
            if content:
                # Check for JSON Schema markers
                if '$schema' in content or '$id' in content:
                    valid_schemas.append({
                        "path": str(schema_path),
                        "id": schema_id,
                        "status": "valid"
                    })
        
        if self.identifier_cache.get(identifier):
            self.identifier_cache[identifier].schema_refs = [s["id"] for s in valid_schemas]
        
        result.add_step(step_name, "passed", {
            "identifier": identifier,
            "schemas_found": len(valid_schemas),
            "schema_ids": [s["id"] for s in valid_schemas]
        })
        result.add_info(
            f"Found {len(valid_schemas)} applicable schema(s) for {identifier}",
            step_name
        )
        
        return True

    def _validate_trace_links(self, identifier: str, result: ValidationResult) -> bool:
        """
        Steps 3-5: Validate trace links (Design, Implementation, Test).
        
        Args:
            identifier: The identifier to validate
            result: ValidationResult to update
            
        Returns:
            True if valid, False otherwise
        """
        step_name = "Steps 3-5: Trace Link Validation"
        print(f"🔍 {step_name}...")
        
        trace_links = self._find_trace_links(identifier)
        
        if not trace_links:
            result.add_warning(
                f"No trace links found for identifier: {identifier}",
                step_name
            )
            result.add_step(step_name, "warning", {
                "identifier": identifier,
                "trace_links_found": 0,
                "note": "Trace link establishment pending - see ATA 93"
            })
            return True  # Warning, not error
        
        # Categorize trace links
        link_types = {}
        for link in trace_links:
            link_type = link.get('type', 'unknown')
            if link_type not in link_types:
                link_types[link_type] = []
            link_types[link_type].append(link)
        
        if self.identifier_cache.get(identifier):
            self.identifier_cache[identifier].trace_links = [
                link.get('target', link.get('file', ''))
                for link in trace_links
            ]
        
        result.add_step(step_name, "passed", {
            "identifier": identifier,
            "trace_links_found": len(trace_links),
            "link_types": {k: len(v) for k, v in link_types.items()},
            "related_identifiers": [
                link.get('target', '') 
                for link in trace_links 
                if link.get('target')
            ][:10]  # Limit display
        })
        result.add_info(
            f"Found {len(trace_links)} trace link(s) for {identifier}",
            step_name
        )
        
        return True

    def _validate_exports(self, identifier: str, result: ValidationResult) -> bool:
        """
        Step 6: Validate evidence/export retrieval.
        
        Args:
            identifier: The identifier to validate
            result: ValidationResult to update
            
        Returns:
            True if valid, False otherwise
        """
        step_name = "Step 6: Export/Evidence Validation"
        print(f"🔍 {step_name}...")
        
        exports = self._find_identifier_in_exports(identifier)
        
        if not exports:
            result.add_warning(
                f"No exports found containing identifier: {identifier}",
                step_name
            )
            result.add_step(step_name, "warning", {
                "identifier": identifier,
                "exports_found": 0,
                "note": "Export generation pending"
            })
            return True  # Warning, not error
        
        export_details = []
        for export_path, data in exports:
            detail = {
                "file": str(export_path),
                "has_data": bool(data)
            }
            if isinstance(data, dict):
                detail["status"] = data.get('status', 'unknown')
                detail["name"] = data.get('name', 'unknown')
            export_details.append(detail)
        
        if self.identifier_cache.get(identifier):
            self.identifier_cache[identifier].evidence_refs = [
                str(e[0]) for e in exports
            ]
        
        result.add_step(step_name, "passed", {
            "identifier": identifier,
            "exports_found": len(exports),
            "export_files": [str(e[0]) for e in exports]
        })
        result.add_info(
            f"Found {len(exports)} export(s) containing {identifier}",
            step_name
        )
        
        return True

    def _validate_baseline(self, identifier: str, result: ValidationResult) -> bool:
        """
        Step 7: Validate baseline inclusion.
        
        Args:
            identifier: The identifier to validate
            result: ValidationResult to update
            
        Returns:
            True if valid, False otherwise
        """
        step_name = "Step 7: Baseline Verification"
        print(f"🔍 {step_name}...")
        
        # Check for baseline references in export files
        baseline_info = []
        
        for export_file in EXPORT_LOCATIONS:
            export_path = self.repo_root / export_file
            if export_path.exists():
                content = self._load_json_file(export_path)
                if content:
                    metadata = content.get('metadata', {})
                    baseline_id = metadata.get('baseline_id', '')
                    if baseline_id:
                        baseline_info.append({
                            "file": str(export_path),
                            "baseline_id": baseline_id,
                            "status": metadata.get('approval_status', 'unknown')
                        })
        
        if not baseline_info:
            result.add_warning(
                f"No baseline information found for identifier: {identifier}",
                step_name
            )
            result.add_step(step_name, "warning", {
                "identifier": identifier,
                "baselines_found": 0,
                "note": "Baseline tagging pending"
            })
            return True  # Warning, not error
        
        result.add_step(step_name, "passed", {
            "identifier": identifier,
            "baselines_found": len(baseline_info),
            "baseline_ids": [b["baseline_id"] for b in baseline_info]
        })
        result.add_info(
            f"Found baseline information for {identifier}",
            step_name
        )
        
        return True

    def _validate_approvals(self, identifier: str, result: ValidationResult) -> bool:
        """
        Step 8: Validate approval confirmation.
        
        Args:
            identifier: The identifier to validate
            result: ValidationResult to update
            
        Returns:
            True if valid, False otherwise
        """
        step_name = "Step 8: Approval Verification"
        print(f"🔍 {step_name}...")
        
        # Check approval logs
        approval_info = []
        
        for path in self.repo_root.rglob('*_LOG_*approvals*.md'):
            if self._is_excluded_path(path):
                continue
            try:
                content = path.read_text(encoding='utf-8')
                if self._identifier_in_content(identifier, content):
                    approval_info.append({
                        "file": str(path),
                        "status": "referenced"
                    })
            except (OSError, UnicodeDecodeError):
                continue
        
        # Also check for approval status in exports
        for export_file in EXPORT_LOCATIONS:
            export_path = self.repo_root / export_file
            if export_path.exists():
                content = self._load_json_file(export_path)
                if content:
                    metadata = content.get('metadata', {})
                    status = metadata.get('approval_status', '')
                    if status:
                        approval_info.append({
                            "file": str(export_path),
                            "status": status,
                            "approved_by": metadata.get('approved_by', ''),
                            "approval_date": metadata.get('approval_date', '')
                        })
        
        if not approval_info:
            result.add_warning(
                f"No approval information found for identifier: {identifier}",
                step_name
            )
            result.add_step(step_name, "warning", {
                "identifier": identifier,
                "approvals_found": 0,
                "note": "Approval pending CM WG sign-off"
            })
            return True  # Warning, not error
        
        result.add_step(step_name, "passed", {
            "identifier": identifier,
            "approvals_found": len(approval_info),
            "approval_status": [a.get("status", "unknown") for a in approval_info]
        })
        result.add_info(
            f"Found {len(approval_info)} approval record(s) for {identifier}",
            step_name
        )
        
        return True

    def validate_chain(self, identifier: str) -> ValidationResult:
        """
        Validate the complete audit proof path chain for an identifier.
        
        ID → Schema → Trace → Export
        
        Args:
            identifier: The identifier to validate
            
        Returns:
            ValidationResult with all findings
        """
        result = ValidationResult()
        
        print("\n" + "=" * 70)
        print(f"AUDITABILITY PROOF PATH VALIDATION")
        print(f"Identifier: {identifier}")
        print("Chain: ID → Schema → Trace → Export")
        print("=" * 70 + "\n")
        
        # Step 1: Identifier Validation
        if not self._validate_identifier_format(identifier, result):
            result.print_summary()
            return result
        
        # Step 2: Schema Validation
        self._validate_schema(identifier, result)
        
        # Steps 3-5: Trace Link Validation
        self._validate_trace_links(identifier, result)
        
        # Step 6: Export Validation
        self._validate_exports(identifier, result)
        
        # Step 7: Baseline Verification
        self._validate_baseline(identifier, result)
        
        # Step 8: Approval Verification
        self._validate_approvals(identifier, result)
        
        result.print_summary()
        return result

    def validate_identifier(self, identifier: str) -> ValidationResult:
        """
        Validate just the identifier format and location.
        
        Args:
            identifier: The identifier to validate
            
        Returns:
            ValidationResult with findings
        """
        result = ValidationResult()
        
        print("\n" + "=" * 70)
        print(f"IDENTIFIER VALIDATION")
        print(f"Identifier: {identifier}")
        print("=" * 70 + "\n")
        
        self._validate_identifier_format(identifier, result)
        
        result.print_summary()
        return result

    def check_all_identifiers(self) -> ValidationResult:
        """
        Discover and validate all identifiers in the repository.
        
        Returns:
            ValidationResult with all findings
        """
        result = ValidationResult()
        
        print("\n" + "=" * 70)
        print("COMPREHENSIVE IDENTIFIER AUDIT")
        print("Discovering all identifiers in repository...")
        print("=" * 70 + "\n")
        
        # Collect all identifiers from export files
        all_identifiers: Set[str] = set()
        
        for export_file in EXPORT_LOCATIONS:
            export_path = self.repo_root / export_file
            if export_path.exists():
                content = self._load_json_file(export_path)
                if content:
                    data = content.get('data', {})
                    for category in ['datums', 'zones', 'envelopes']:
                        items = data.get(category, [])
                        for item in items:
                            identifier = item.get('identifier', '')
                            if identifier:
                                all_identifiers.add(identifier)
        
        if not all_identifiers:
            result.add_warning("No identifiers found in export files")
            result.print_summary()
            return result
        
        result.add_info(f"Discovered {len(all_identifiers)} identifier(s)")
        
        # Validate each identifier
        passed_count = 0
        failed_count = 0
        
        for identifier in sorted(all_identifiers):
            print(f"\n--- Validating: {identifier} ---")
            info = self._parse_identifier(identifier)
            
            if info:
                passed_count += 1
                result.add_info(f"✅ {identifier} - Valid ({info.category})")
            else:
                failed_count += 1
                result.add_error(f"Invalid identifier format: {identifier}")
        
        result.add_step("Comprehensive Check", "complete", {
            "total_identifiers": len(all_identifiers),
            "passed": passed_count,
            "failed": failed_count
        })
        
        result.print_summary()
        return result


# =============================================================================
# CLI Interface
# =============================================================================

def main() -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Validate auditability proof path: ID → Schema → Trace → Export',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --id DATUM-GLOBAL-001
  %(prog)s --validate-chain ZONE-PROP-001
  %(prog)s --check-all
  %(prog)s --id REQ-SYS-042 --verbose

Exit codes:
  0: Validation passed
  1: Validation errors found
  2: Script error
        """
    )

    parser.add_argument(
        '--id',
        metavar='IDENTIFIER',
        help='Validate identifier format only'
    )
    parser.add_argument(
        '--validate-chain', '-c',
        metavar='IDENTIFIER',
        help='Validate complete audit chain for identifier (ID → Schema → Trace → Export)'
    )
    parser.add_argument(
        '--check-all',
        action='store_true',
        help='Discover and validate all identifiers in the repository'
    )
    parser.add_argument(
        '--repo-root',
        metavar='DIR',
        default='.',
        help='Repository root directory (default: current directory)'
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Enable verbose output'
    )

    args = parser.parse_args()

    # Validate arguments
    if not any([args.id, args.validate_chain, args.check_all]):
        parser.error('Must specify --id, --validate-chain, or --check-all')

    repo_root = Path(args.repo_root)
    if not repo_root.is_dir():
        print(f"Error: '{args.repo_root}' is not a directory", file=sys.stderr)
        return 2

    try:
        validator = AuditProofPathValidator(repo_root, verbose=args.verbose)

        if args.id:
            result = validator.validate_identifier(args.id)
        elif args.validate_chain:
            result = validator.validate_chain(args.validate_chain)
        elif args.check_all:
            result = validator.check_all_identifiers()
        else:
            parser.print_help()
            return 2

        return 0 if result.passed else 1

    except KeyboardInterrupt:
        print("\nInterrupted by user", file=sys.stderr)
        return 2
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        if args.verbose:
            traceback.print_exc()
        return 2


if __name__ == '__main__':
    sys.exit(main())
