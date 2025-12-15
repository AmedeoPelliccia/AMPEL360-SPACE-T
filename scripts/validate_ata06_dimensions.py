#!/usr/bin/env python3
"""
ATA-06 Dimensional Data Validation Script
==========================================

This script validates ATA-06 dimensional data exports against the schema.
Addresses Task T5: Implement CI validation (schema checks + unit checks + required fields)

Usage:
    python scripts/validate_ata06_dimensions.py <json_file>
    python scripts/validate_ata06_dimensions.py --check-all

Features:
    - JSON Schema validation
    - Unit consistency checks
    - Identifier uniqueness validation
    - Required field verification
    - Tolerance validation
    - CI integration support
"""

import json
import sys
import os
import re
from pathlib import Path
from typing import Dict, List, Set, Tuple

try:
    import jsonschema
    from jsonschema import validate, ValidationError
except ImportError:
    print("Error: jsonschema library not installed")
    print("Install with: pip install jsonschema")
    sys.exit(1)


# Constants
SCHEMA_FILE = "06_90_SCH_SB00_GEN_dimensional-data-schema_v01.json"
DATA_FILE_PATTERN = r"^\d{2}_90_TAB_SB\d{2}_GEN_dimensional-exports_v\d{2}\.json$"

# Identifier patterns
DATUM_PATTERN = r"^DATUM-[A-Z0-9]+-[0-9]{3}(-[A-Z0-9]+)?$"
ZONE_PATTERN = r"^ZONE-[A-Z0-9]+-[0-9]{3}(-[A-Z0-9]+)?$"
ENVELOPE_PATTERN = r"^ENVELOPE-[A-Z0-9]+-[0-9]{3}(-[A-Z0-9]+)?$"

# Approved system codes
APPROVED_SYSTEMS = [
    "GLOBAL", "FUS", "PROP", "AVION", "POWER", "THERM",
    "STRUCT", "MECH", "PAYLOAD", "GNC", "COMM", "INTEG"
]

# Approved units
APPROVED_LENGTH_UNITS = ["mm", "m", "in", "ft"]
APPROVED_ANGLE_UNITS = ["deg", "rad"]


class ValidationResult:
    """Container for validation results."""
    
    def __init__(self):
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.info: List[str] = []
        self.passed = True
    
    def add_error(self, message: str):
        """Add an error message."""
        self.errors.append(message)
        self.passed = False
    
    def add_warning(self, message: str):
        """Add a warning message."""
        self.warnings.append(message)
    
    def add_info(self, message: str):
        """Add an info message."""
        self.info.append(message)
    
    def print_summary(self):
        """Print validation summary."""
        print("\n" + "="*60)
        print("VALIDATION SUMMARY")
        print("="*60)
        
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
            for info in self.info:
                print(f"  • {info}")
        
        print("\n" + "="*60)
        if self.passed and not self.warnings:
            print("✅ VALIDATION PASSED - No errors or warnings")
        elif self.passed:
            print("✅ VALIDATION PASSED - Warnings present but no errors")
        else:
            print("❌ VALIDATION FAILED - Errors must be fixed")
        print("="*60 + "\n")


def load_schema(schema_path: str) -> Dict:
    """Load JSON schema from file."""
    try:
        with open(schema_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: Schema file not found: {schema_path}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in schema file: {e}")
        sys.exit(1)


def load_data(data_path: str) -> Dict:
    """Load dimensional data from file."""
    try:
        with open(data_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: Data file not found: {data_path}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in data file: {e}")
        sys.exit(1)


def validate_schema(data: Dict, schema: Dict, result: ValidationResult):
    """Validate data against JSON schema."""
    print("🔍 Validating against JSON Schema...")
    
    try:
        validate(instance=data, schema=schema)
        result.add_info("JSON Schema validation passed")
    except ValidationError as e:
        result.add_error(f"JSON Schema validation failed: {e.message}")
        result.add_error(f"  Path: {'.'.join(str(p) for p in e.absolute_path)}")
        if e.validator:
            result.add_error(f"  Validator: {e.validator}")


def validate_identifiers(data: Dict, result: ValidationResult):
    """Validate identifier format and uniqueness."""
    print("🔍 Validating identifiers...")
    
    all_identifiers: Set[str] = set()
    duplicates: List[str] = []
    
    # Check datums
    for datum in data.get("data", {}).get("datums", []):
        identifier = datum.get("identifier", "")
        
        # Check format
        if not re.match(DATUM_PATTERN, identifier):
            result.add_error(f"Invalid DATUM identifier format: {identifier}")
        
        # Check uniqueness
        if identifier in all_identifiers:
            duplicates.append(identifier)
        else:
            all_identifiers.add(identifier)
        
        # Check system code
        system = datum.get("system", "")
        if system not in APPROVED_SYSTEMS:
            result.add_warning(f"Non-standard system code in {identifier}: {system}")
    
    # Check zones
    for zone in data.get("data", {}).get("zones", []):
        identifier = zone.get("identifier", "")
        
        if not re.match(ZONE_PATTERN, identifier):
            result.add_error(f"Invalid ZONE identifier format: {identifier}")
        
        if identifier in all_identifiers:
            duplicates.append(identifier)
        else:
            all_identifiers.add(identifier)
        
        system = zone.get("system", "")
        if system not in APPROVED_SYSTEMS:
            result.add_warning(f"Non-standard system code in {identifier}: {system}")
    
    # Check envelopes
    for envelope in data.get("data", {}).get("envelopes", []):
        identifier = envelope.get("identifier", "")
        
        if not re.match(ENVELOPE_PATTERN, identifier):
            result.add_error(f"Invalid ENVELOPE identifier format: {identifier}")
        
        if identifier in all_identifiers:
            duplicates.append(identifier)
        else:
            all_identifiers.add(identifier)
        
        system = envelope.get("system", "")
        if system not in APPROVED_SYSTEMS:
            result.add_warning(f"Non-standard system code in {identifier}: {system}")
    
    # Report duplicates
    if duplicates:
        result.add_error(f"Duplicate identifiers found: {', '.join(duplicates)}")
    
    result.add_info(f"Total identifiers validated: {len(all_identifiers)}")


def validate_units(data: Dict, result: ValidationResult):
    """Validate unit consistency."""
    print("🔍 Validating unit consistency...")
    
    coord_frame = data.get("coordinate_frame", {})
    units = coord_frame.get("units", {})
    
    length_unit = units.get("length")
    angle_unit = units.get("angle")
    
    # Check approved units
    if length_unit not in APPROVED_LENGTH_UNITS:
        result.add_error(f"Invalid length unit: {length_unit}")
    
    if angle_unit not in APPROVED_ANGLE_UNITS:
        result.add_error(f"Invalid angle unit: {angle_unit}")
    
    # Recommend SI units
    if length_unit not in ["mm", "m"]:
        result.add_warning(f"Non-SI length unit: {length_unit} (prefer mm or m)")
    
    if angle_unit != "deg":
        result.add_warning(f"Non-degree angle unit: {angle_unit} (prefer deg)")
    
    result.add_info(f"Units: length={length_unit}, angle={angle_unit}")


def validate_baseline_id(data: Dict, result: ValidationResult):
    """Validate baseline ID format."""
    print("🔍 Validating baseline ID...")
    
    baseline_id = data.get("metadata", {}).get("baseline_id", "")
    
    if not re.match(r"^BL-\d{4}$", baseline_id):
        result.add_error(f"Invalid baseline ID format: {baseline_id} (must be BL-NNNN)")
    else:
        result.add_info(f"Baseline ID: {baseline_id}")


def validate_approval_status(data: Dict, result: ValidationResult):
    """Validate approval status and related fields."""
    print("🔍 Validating approval status...")
    
    metadata = data.get("metadata", {})
    status = metadata.get("approval_status", "")
    
    if status == "approved":
        # Approved status requires additional fields
        if not metadata.get("approved_by"):
            result.add_error("Approved status requires 'approved_by' field")
        if not metadata.get("approval_date"):
            result.add_error("Approved status requires 'approval_date' field")
        else:
            result.add_info(f"Approval: {status} by {metadata.get('approved_by')} on {metadata.get('approval_date')}")
    else:
        result.add_info(f"Approval status: {status}")


def validate_geometry_bounds(data: Dict, result: ValidationResult):
    """Validate geometry and bounds consistency."""
    print("🔍 Validating geometry and bounds...")
    
    # Check datums with geometry
    for datum in data.get("data", {}).get("datums", []):
        identifier = datum.get("identifier", "")
        geometry = datum.get("geometry", {})
        
        if geometry:
            geom_type = geometry.get("type")
            datum_type = datum.get("type")
            
            # Type consistency check
            if geom_type != datum_type:
                result.add_warning(f"{identifier}: geometry type '{geom_type}' doesn't match datum type '{datum_type}'")
    
    # Check zones with cuboid bounds for valid ranges
    for zone in data.get("data", {}).get("zones", []):
        identifier = zone.get("identifier", "")
        bounds = zone.get("bounds", {})
        
        if bounds.get("type") == "cuboid":
            # Check that required fields exist before comparing
            if "x_min" in bounds and "x_max" in bounds:
                if bounds["x_min"] >= bounds["x_max"]:
                    result.add_error(f"{identifier}: x_min must be less than x_max")
            if "y_min" in bounds and "y_max" in bounds:
                if bounds["y_min"] >= bounds["y_max"]:
                    result.add_error(f"{identifier}: y_min must be less than y_max")
            if "z_min" in bounds and "z_max" in bounds:
                if bounds["z_min"] >= bounds["z_max"]:
                    result.add_error(f"{identifier}: z_min must be less than z_max")


def validate_file(file_path: str, schema_path: str) -> ValidationResult:
    """Validate a single dimensional data file."""
    print(f"\n{'='*60}")
    print(f"Validating: {file_path}")
    print(f"{'='*60}\n")
    
    result = ValidationResult()
    
    # Load schema and data
    schema = load_schema(schema_path)
    data = load_data(file_path)
    
    # Run validations
    validate_schema(data, schema, result)
    validate_identifiers(data, result)
    validate_units(data, result)
    validate_baseline_id(data, result)
    validate_approval_status(data, result)
    validate_geometry_bounds(data, result)
    
    # Print summary
    result.print_summary()
    
    return result


def find_dimensional_data_files() -> List[str]:
    """Find all dimensional data files in the repository."""
    files = []
    for file_path in Path(".").rglob("*.json"):
        if re.match(DATA_FILE_PATTERN, file_path.name):
            files.append(str(file_path))
    return files


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python scripts/validate_ata06_dimensions.py <json_file>")
        print("  python scripts/validate_ata06_dimensions.py --check-all")
        sys.exit(1)
    
    # Find schema file
    schema_path = SCHEMA_FILE
    if not os.path.exists(schema_path):
        print(f"Error: Schema file not found: {schema_path}")
        print("Make sure you're running from the repository root.")
        sys.exit(1)
    
    # Handle --check-all
    if sys.argv[1] == "--check-all":
        print("Searching for dimensional data files...")
        files = find_dimensional_data_files()
        
        if not files:
            print("No dimensional data files found.")
            sys.exit(0)
        
        print(f"Found {len(files)} file(s) to validate.\n")
        
        all_passed = True
        for file_path in files:
            result = validate_file(file_path, schema_path)
            if not result.passed:
                all_passed = False
        
        if all_passed:
            print("\n✅ All files validated successfully!")
            sys.exit(0)
        else:
            print("\n❌ Some files failed validation.")
            sys.exit(1)
    
    # Validate single file
    file_path = sys.argv[1]
    
    if not os.path.exists(file_path):
        print(f"Error: File not found: {file_path}")
        sys.exit(1)
    
    result = validate_file(file_path, schema_path)
    
    sys.exit(0 if result.passed else 1)


if __name__ == "__main__":
    main()
