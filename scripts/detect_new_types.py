#!/usr/bin/env python3
"""
AMPEL360 Space-T TYPE Detection and Extension System
====================================================
Version: 1.0
Date: 2025-12-14

Automatically detects new TYPE codes in use and provides guidance
for extending the nomenclature standard and template library.

Usage:
    python scripts/detect_new_types.py [--auto-suggest]
"""

import argparse
import re
import sys
from pathlib import Path
from typing import Set, List, Dict
from collections import defaultdict


# Import the approved types from validation script
sys.path.insert(0, str(Path(__file__).parent.parent))
from validate_nomenclature import NomenclatureValidator


def detect_types_in_files(directory: Path = Path('.')) -> Dict[str, List[str]]:
    """
    Scan repository for files following nomenclature pattern and extract TYPEs.
    
    Returns:
        Dictionary mapping TYPE codes to list of example filenames
    """
    # Pattern to match nomenclature
    pattern = re.compile(
        r'^(?P<root>\d{2})_(?P<bucket>\d{2})_(?P<type>[A-Z0-9]{2,8})_'
        r'(?P<variant>[A-Z0-9]+(?:-[A-Z0-9]+)*)_(?P<desc>[a-z0-9]+(?:-[a-z0-9]+)*)_'
        r'(?P<ver>v\d{2})\.(?P<ext>[a-z0-9]{1,6})$'
    )
    
    found_types = defaultdict(list)
    validator = NomenclatureValidator()
    
    for path in directory.rglob('*'):
        if not path.is_file():
            continue
        
        # Skip excluded directories
        if validator._is_excluded_path(path):
            continue
        
        match = pattern.match(path.name)
        if match:
            type_code = match.group('type')
            found_types[type_code].append(path.name)
    
    return dict(found_types)


def identify_new_types(found_types: Dict[str, List[str]]) -> Set[str]:
    """Identify TYPE codes that are not in approved vocabulary."""
    validator = NomenclatureValidator()
    approved = validator.APPROVED_TYPES
    
    new_types = set()
    for type_code in found_types.keys():
        if type_code not in approved:
            new_types.add(type_code)
    
    return new_types


def generate_template_stub(type_code: str) -> str:
    """Generate a template stub for a new TYPE."""
    return f"""---
title: "{{{{DESCRIPTION}}}}"
type: {type_code}
variant: "{{{{VARIANT}}}}"
status: Draft
owner: "{{{{OWNER}}}}"
---

# {type_code}: {{{{TITLE}}}}

## 1. Overview

### 1.1 Purpose
[Describe the purpose of this {type_code} document]

### 1.2 Scope
[Define the scope and boundaries]

## 2. Content Structure

### 2.1 Section 1
[Content guidance]

### 2.2 Section 2
[Content guidance]

## 3. References

- Related documents
- Standards and specifications

## Revision History

| Version | Date | Changes | Author |
| :--- | :--- | :--- | :--- |
| {{{{VERSION}}}} | {{{{DATE}}}} | Initial version | {{{{OWNER}}}} |
"""


def generate_extension_guide(new_types: Set[str], examples: Dict[str, List[str]]) -> str:
    """Generate a guide for extending the nomenclature standard."""
    guide = """# Nomenclature Standard Extension Guide

## Detected New TYPE Codes

The following TYPE codes are in use but not in the approved vocabulary:

"""
    
    for type_code in sorted(new_types):
        guide += f"\n### {type_code}\n\n"
        guide += f"**Found in files:**\n"
        for filename in examples[type_code][:5]:  # Show up to 5 examples
            guide += f"- `{filename}`\n"
        if len(examples[type_code]) > 5:
            guide += f"- *(and {len(examples[type_code]) - 5} more)*\n"
        guide += "\n"
    
    guide += """
## Extension Process

To officially add a new TYPE to the nomenclature standard:

### 1. Update Validation Script

Edit `validate_nomenclature.py`:

```python
APPROVED_TYPES = {
    # Planning / Control
    'PLAN', 'MIN', 'RPT', 'LOG', 'ACT', 'IDX',
    # Safety Analyses
    'FHA', 'PSSA', 'SSA', 'FTA', 'ANA',
    # Requirements / Allocation
    'REQ', 'DAL', 'TRC',
    # Data / Reference
    'CAT', 'LST', 'GLO', 'MAT', 'SCH', 'DIA', 'TAB', 'STD',
    # NEW TYPES (add here)
    'NEWTYPE',  # Description
}
```

### 2. Create Template

Create `templates/NEWTYPE.md` with appropriate structure:

```bash
# Generate stub template
python scripts/detect_new_types.py --generate-template NEWTYPE > templates/NEWTYPE.md
```

### 3. Update Documentation

Add to the following documents:

**`00_00_STD_LC01-Q100BL_nomenclature-standard_v01.md`:**
- Section 4.3: Add to TYPE vocabulary list

**`.github/copilot-instructions.md`:**
- Update "Available Templates" table

**`templates/README.md`:**
- Add to appropriate category

**`scripts/scaffold.py`:**
- Template will be automatically available

### 4. Update Copilot Instructions

Edit `.github/copilot-instructions.md`:

```markdown
| `NEWTYPE` | `templates/NEWTYPE.md` | Description of when to use |
```

### 5. Test

```bash
# Validate files with new TYPE
python validate_nomenclature.py --check-all

# Test template scaffolding
python scripts/scaffold.py 00 90 NEWTYPE GEN test-document v01

# Verify created file validates
python validate_nomenclature.py 00_90_NEWTYPE_GEN_test-document_v01.md
```

### 6. Submit Change Request

- Create PR with changes
- Update PR description with rationale for new TYPE
- Link to examples showing need for new TYPE
- Document intended use cases

## Approval Process

New TYPEs require:
1. **Technical Review**: Configuration Management WG
2. **Documentation**: Complete template and usage guidance
3. **Testing**: Validation and scaffolding tests pass
4. **Rationale**: Clear justification for new TYPE vs existing ones

"""
    
    return guide


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Detect new TYPE codes and provide extension guidance'
    )
    parser.add_argument(
        '--auto-suggest',
        action='store_true',
        help='Automatically generate extension suggestions'
    )
    parser.add_argument(
        '--generate-template',
        metavar='TYPE',
        help='Generate template stub for specified TYPE'
    )
    parser.add_argument(
        '--directory',
        default='.',
        help='Directory to scan (default: current directory)'
    )
    
    args = parser.parse_args()
    
    if args.generate_template:
        # Generate template stub
        print(generate_template_stub(args.generate_template))
        return 0
    
    # Detect types in use
    print("🔍 Scanning repository for TYPE codes...")
    found_types = detect_types_in_files(Path(args.directory))
    
    print(f"Found {len(found_types)} unique TYPE codes in use")
    
    # Identify new types
    new_types = identify_new_types(found_types)
    
    if not new_types:
        print("✅ All TYPE codes are in approved vocabulary")
        return 0
    
    print(f"\n⚠️  Detected {len(new_types)} new TYPE codes not in approved vocabulary:")
    for type_code in sorted(new_types):
        count = len(found_types[type_code])
        print(f"  - {type_code} ({count} file{'s' if count != 1 else ''})")
    
    if args.auto_suggest:
        print("\n📝 Generating extension guide...")
        guide = generate_extension_guide(new_types, found_types)
        
        # Write to file
        guide_path = Path('NOMENCLATURE_EXTENSION_GUIDE.md')
        guide_path.write_text(guide)
        print(f"✅ Extension guide written to: {guide_path}")
        
        # Generate template stubs
        templates_dir = Path('templates')
        if templates_dir.exists():
            for type_code in new_types:
                template_path = templates_dir / f"{type_code}.md"
                if not template_path.exists():
                    template_path.write_text(generate_template_stub(type_code))
                    print(f"✅ Template stub created: {template_path}")
                else:
                    print(f"ℹ️  Template already exists: {template_path}")
    else:
        print("\n💡 Run with --auto-suggest to generate extension guide and template stubs")
    
    return 1 if new_types else 0


if __name__ == '__main__':
    sys.exit(main())
