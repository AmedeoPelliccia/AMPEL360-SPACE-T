#!/usr/bin/env python3
"""
KNOT and AoR Mapping Configuration
===================================
Version: 4.0
Date: 2025-12-16

Canonical mapping of KNOT IDs to their owning AoRs and directory paths.
Used by the v4.0 retrofit tooling to determine TRIGGER_KNOT and AoR values.
"""

from typing import Dict, List, Tuple

# Canonical KNOT to AoR mapping (source of truth)
KNOT_AOR_MAPPING = {
    'K01': {
        'knot_id': 'K01',
        'knot_slug': 'K01_certification-authority-basis',
        'aor': 'CERT',
        'aor_dir': 'STK_CERT-cert-certification-authorities',
        'knot_dir_path': 'AMPEL360-SPACE-T-PORTAL/STK_CERT-cert-certification-authorities/KNOTS/K01_certification-authority-basis/',
        'uncertainty_focus': 'Authority model, certification basis, means of compliance, evidence packaging',
        'keywords': ['certification', 'authority', 'compliance', 'cert', 'basis', 'easa', 'faa']
    },
    'K02': {
        'knot_id': 'K02',
        'knot_slug': 'K02_conops-command-authority-readiness',
        'aor': 'OPS',
        'aor_dir': 'STK_OPS-ops-operations',
        'knot_dir_path': 'AMPEL360-SPACE-T-PORTAL/STK_OPS-ops-operations/KNOTS/K02_conops-command-authority-readiness/',
        'uncertainty_focus': 'ConOps/mission phases, command authority, readiness gates, jurisdiction',
        'keywords': ['conops', 'command', 'authority', 'readiness', 'mission', 'operations', 'ops']
    },
    'K03': {
        'knot_id': 'K03',
        'knot_slug': 'K03_hazard-management-cryogenic-fire-containment',
        'aor': 'SAF',
        'aor_dir': 'STK_SAF-saf-safety',
        'knot_dir_path': 'AMPEL360-SPACE-T-PORTAL/STK_SAF-saf-safety/KNOTS/K03_hazard-management-cryogenic-fire-containment/',
        'uncertainty_focus': 'Hazard zoning, cryogenic/fire containment, emergency response constraints',
        'keywords': ['hazard', 'cryogenic', 'cryo', 'fire', 'containment', 'emergency', 'safety', 'propellant']
    },
    'K04': {
        'knot_id': 'K04',
        'knot_slug': 'K04_interfaces-geometry-icds-datums',
        'aor': 'SE',
        'aor_dir': 'STK_SE-se-systems-engineering',
        'knot_dir_path': 'AMPEL360-SPACE-T-PORTAL/STK_SE-se-systems-engineering/KNOTS/K04_interfaces-geometry-icds-datums/',
        'uncertainty_focus': 'Geometry/datums/interfaces, ICD portfolio, configuration of interfaces',
        'keywords': ['interface', 'geometry', 'icd', 'datum', 'configuration', 'system']
    },
    'K05': {
        'knot_id': 'K05',
        'knot_slug': 'K05_model-fidelity-uncertainty-budgets-substantiation',
        'aor': 'SE',
        'aor_dir': 'STK_SE-se-systems-engineering',
        'knot_dir_path': 'AMPEL360-SPACE-T-PORTAL/STK_SE-se-systems-engineering/KNOTS/K05_model-fidelity-uncertainty-budgets-substantiation/',
        'uncertainty_focus': 'Model fidelity & substantiation, uncertainty budgets, acceptance thresholds',
        'keywords': ['model', 'fidelity', 'uncertainty', 'budget', 'substantiation', 'threshold']
    },
    'K06': {
        'knot_id': 'K06',
        'knot_slug': 'K06_data-governance-ssot-schemas-identifiers',
        'aor': 'DATA',
        'aor_dir': 'STK_DATA-data-data-governance',
        'knot_dir_path': 'AMPEL360-SPACE-T-PORTAL/STK_DATA-data-data-governance/KNOTS/K06_data-governance-ssot-schemas-identifiers/',
        'uncertainty_focus': 'Identifiers, registries, schema governance, SSOT decision matrix',
        'keywords': ['data', 'governance', 'ssot', 'schema', 'identifier', 'registry', 'decision']
    },
    'K07': {
        'knot_id': 'K07',
        'knot_slug': 'K07_ai-autonomy-assurance-monitoring',
        'aor': 'AI',
        'aor_dir': 'STK_AI-ai-ai-ml-engineering',
        'knot_dir_path': 'AMPEL360-SPACE-T-PORTAL/STK_AI-ai-ai-ml-engineering/KNOTS/K07_ai-autonomy-assurance-monitoring/',
        'uncertainty_focus': 'Autonomy assurance, monitors, drift/bias, fail-safe actions, DAL allocation',
        'keywords': ['ai', 'autonomy', 'assurance', 'monitoring', 'ml', 'drift', 'bias']
    },
    'K08': {
        'knot_id': 'K08',
        'knot_slug': 'K08_dpp-provenance-sbom-circularity',
        'aor': 'DATA',
        'aor_dir': 'STK_DATA-data-data-governance',
        'knot_dir_path': 'AMPEL360-SPACE-T-PORTAL/STK_DATA-data-data-governance/KNOTS/K08_dpp-provenance-sbom-circularity/',
        'uncertainty_focus': 'DPP scope & provenance, SBOM linkage, circularity & signed exports',
        'keywords': ['dpp', 'provenance', 'sbom', 'circularity', 'export', 'supply']
    },
    'K09': {
        'knot_id': 'K09',
        'knot_slug': 'K09_spaceport-infrastructure-interfaces-permits',
        'aor': 'SPACEPORT',
        'aor_dir': 'STK_SPACEPORT-spaceport-spaceport-airport-ops',
        'knot_dir_path': 'AMPEL360-SPACE-T-PORTAL/STK_SPACEPORT-spaceport-spaceport-airport-ops/KNOTS/K09_spaceport-infrastructure-interfaces-permits/',
        'uncertainty_focus': 'Spaceport ecosystem interfaces, energy/cryogenic services, permitting',
        'keywords': ['spaceport', 'airport', 'infrastructure', 'permit', 'ground', 'fueling']
    },
    'K10': {
        'knot_id': 'K10',
        'knot_slug': 'K10_industrial-readiness-supply-chain-tool-qualification',
        'aor': 'PMO',
        'aor_dir': 'STK_PMO-pmo-program-management-office',
        'knot_dir_path': 'AMPEL360-SPACE-T-PORTAL/STK_PMO-pmo-program-management-office/KNOTS/K10_industrial-readiness-supply-chain-tool-qualification/',
        'uncertainty_focus': 'Industrial readiness, supplier/tool qualification, production evidence',
        'keywords': ['industrial', 'readiness', 'supply', 'chain', 'supplier', 'tool', 'qualification']
    },
    'K11': {
        'knot_id': 'K11',
        'knot_slug': 'K11_human-factors-training-readiness-gates',
        'aor': 'OPS',
        'aor_dir': 'STK_OPS-ops-operations',
        'knot_dir_path': 'AMPEL360-SPACE-T-PORTAL/STK_OPS-ops-operations/KNOTS/K11_human-factors-training-readiness-gates/',
        'uncertainty_focus': 'Human factors, training, procedures, ORR/FRR and operational discipline',
        'keywords': ['human', 'factors', 'training', 'readiness', 'orr', 'frr', 'procedures']
    },
    'K12': {
        'knot_id': 'K12',
        'knot_slug': 'K12_noise-vibration-plume-environment',
        'aor': 'OPS',
        'aor_dir': 'STK_OPS-ops-operations',
        'knot_dir_path': 'AMPEL360-SPACE-T-PORTAL/STK_OPS-ops-operations/KNOTS/K12_noise-vibration-plume-environment/',
        'uncertainty_focus': 'Noise/vibration/plume environment, corridors, measurement vs model gaps',
        'keywords': ['noise', 'vibration', 'plume', 'environment', 'corridor', 'acoustic']
    },
    'K13': {
        'knot_id': 'K13',
        'knot_slug': 'K13_cybersecurity-zones-key-management',
        'aor': 'CY',
        'aor_dir': 'STK_CY-cy-cybersecurity',
        'knot_dir_path': 'AMPEL360-SPACE-T-PORTAL/STK_CY-cy-cybersecurity/KNOTS/K13_cybersecurity-zones-key-management/',
        'uncertainty_focus': 'Cyber zones, key mgmt, secure comms, signing and tamper evidence',
        'keywords': ['cyber', 'cybersecurity', 'security', 'key', 'crypto', 'zone', 'tamper']
    },
    'K14': {
        'knot_id': 'K14',
        'knot_slug': 'K14_reliability-maintenance-intervals-health-monitoring',
        'aor': 'MRO',
        'aor_dir': 'STK_MRO-mro-mro-maintenance',
        'knot_dir_path': 'AMPEL360-SPACE-T-PORTAL/STK_MRO-mro-mro-maintenance/KNOTS/K14_reliability-maintenance-intervals-health-monitoring/',
        'uncertainty_focus': 'Reliability growth, maintenance intervals, health monitoring, sustainment loops',
        'keywords': ['reliability', 'maintenance', 'mro', 'health', 'monitoring', 'interval', 'sustainment']
    }
}

# AoR to directory prefix mapping
AOR_DIR_MAPPING = {
    'CM': 'STK_CM-cm-configuration-management',
    'CERT': 'STK_CERT-cert-certification-authorities',
    'AI': 'STK_AI-ai-ai-ml-engineering',
    'DATA': 'STK_DATA-data-data-governance',
    'OPS': 'STK_OPS-ops-operations',
    'SE': 'STK_SE-se-systems-engineering',
    'SAF': 'STK_SAF-saf-safety',
    'PMO': 'STK_PMO-pmo-program-management-office',
    'CY': 'STK_CY-cy-cybersecurity',
    'TEST': 'STK_TEST-test-ivvq-testing',
    'MRO': 'STK_MRO-mro-mro-maintenance',
    'SPACEPORT': 'STK_SPACEPORT-spaceport-spaceport-airport-ops'
}


def get_knot_from_path(path: str) -> Tuple[str, float]:
    """
    Determine KNOT ID from file path.
    
    Returns:
        Tuple of (knot_id, confidence) where confidence is 0.0-1.0
    """
    path_lower = path.lower()
    
    # Check if path contains KNOTS/ directory with knot ID
    for knot_id, info in KNOT_AOR_MAPPING.items():
        if info['knot_slug'].lower() in path_lower:
            return (knot_id, 1.0)  # High confidence
        
        # Check for knot ID pattern in path (e.g., "K01_", "/K01/")
        if f"/{knot_id.lower()}_" in path_lower or f"/{knot_id.lower()}/" in path_lower:
            return (knot_id, 0.9)  # High confidence
    
    # Check description patterns (e.g., "k01-", "-k01-")
    for knot_id in KNOT_AOR_MAPPING.keys():
        if f"{knot_id.lower()}-" in path_lower or f"-{knot_id.lower()}-" in path_lower:
            return (knot_id, 0.8)  # Medium-high confidence
    
    # Default to K00 (global)
    return ('K00', 0.5)  # Low confidence


def get_aor_from_path(path: str) -> Tuple[str, float]:
    """
    Determine AoR from file path.
    
    Returns:
        Tuple of (aor, confidence) where confidence is 0.0-1.0
    """
    path_lower = path.lower()
    
    # Check if path contains STK_ directory
    for aor, dir_prefix in AOR_DIR_MAPPING.items():
        if dir_prefix.lower() in path_lower:
            return (aor, 1.0)  # High confidence
    
    # Check for AoR in path components
    for aor in AOR_DIR_MAPPING.keys():
        if f"/stk_{aor.lower()}" in path_lower or f"stk_{aor.lower()}" in path_lower:
            return (aor, 0.9)  # High confidence
    
    # Default to CM (configuration management)
    return ('CM', 0.3)  # Low confidence


def get_aor_from_knot(knot_id: str) -> str:
    """
    Get the owning AoR for a given KNOT ID.
    
    Args:
        knot_id: KNOT ID (e.g., 'K01', 'K02')
    
    Returns:
        AoR code (e.g., 'CERT', 'OPS')
    """
    if knot_id in KNOT_AOR_MAPPING:
        return KNOT_AOR_MAPPING[knot_id]['aor']
    return 'CM'  # Default to CM for K00 and unknown knots


def get_aor_from_variant(variant: str) -> Tuple[str, float]:
    """
    Determine AoR from VARIANT field.
    
    Args:
        variant: VARIANT field value
    
    Returns:
        Tuple of (aor, confidence)
    """
    variant_upper = variant.upper()
    
    if variant_upper == 'CERT':
        return ('CERT', 0.9)
    elif variant_upper == 'BB':
        return ('AI', 0.8)  # Body-Brain protorobotics → AI/ML Engineering
    elif variant_upper == 'PLUS':
        return ('CM', 0.4)  # Low confidence, PLUS is general
    elif variant_upper in ['DRAFT', 'PROTO']:
        return ('CM', 0.3)  # Low confidence
    elif variant_upper in ['SYS', 'SW', 'HW']:
        return ('SE', 0.5)  # Medium confidence
    elif variant_upper == 'GEN':
        return ('CM', 0.4)  # Low confidence
    
    return ('CM', 0.3)  # Default


def get_aor_from_type(type_code: str) -> Tuple[str, float]:
    """
    Determine AoR from TYPE field.
    
    Args:
        type_code: TYPE field value
    
    Returns:
        Tuple of (aor, confidence)
    """
    type_upper = type_code.upper()
    
    # Safety artifacts
    if type_upper in ['FHA', 'PSSA', 'SSA', 'FTA']:
        return ('SAF', 0.8)
    
    # Compliance/certification artifacts
    if type_upper in ['TRC', 'DAL']:
        return ('CERT', 0.7)
    
    # Configuration management artifacts
    if type_upper in ['STD', 'IDX', 'CAT']:
        return ('CM', 0.6)
    
    # Systems engineering artifacts
    if type_upper in ['REQ', 'ANA']:
        return ('SE', 0.5)
    
    # Data governance artifacts
    if type_upper in ['SCH', 'DIA', 'TAB']:
        return ('DATA', 0.6)
    
    # Planning artifacts
    if type_upper in ['PLAN', 'RPT']:
        return ('CM', 0.4)
    
    return ('CM', 0.3)  # Default


def get_aor_from_description(description: str) -> Tuple[str, float]:
    """
    Determine AoR from DESCRIPTION field.
    
    Args:
        description: DESCRIPTION field value
    
    Returns:
        Tuple of (aor, confidence)
    """
    desc_lower = description.lower()
    
    # Check keywords for each AoR
    for knot_id, info in KNOT_AOR_MAPPING.items():
        for keyword in info['keywords']:
            if keyword.lower() in desc_lower:
                return (info['aor'], 0.7)
    
    # Specific patterns
    if any(word in desc_lower for word in ['cert', 'compliance', 'authority', 'easa', 'faa']):
        return ('CERT', 0.7)
    
    if any(word in desc_lower for word in ['safety', 'hazard', 'risk', 'fha', 'ssa']):
        return ('SAF', 0.7)
    
    if any(word in desc_lower for word in ['test', 'verification', 'ivvq', 'qual']):
        return ('TEST', 0.7)
    
    if any(word in desc_lower for word in ['operation', 'mission', 'flight', 'conops']):
        return ('OPS', 0.7)
    
    if any(word in desc_lower for word in ['cyber', 'security', 'threat', 'crypto']):
        return ('CY', 0.7)
    
    if any(word in desc_lower for word in ['data', 'schema', 'governance', 'ssot']):
        return ('DATA', 0.7)
    
    if any(word in desc_lower for word in ['system', 'interface', 'icd', 'requirement']):
        return ('SE', 0.6)
    
    if any(word in desc_lower for word in ['ai', 'ml', 'autonomy', 'model', 'body-brain', 'protorobotics', 'robotics']):
        return ('AI', 0.7)
    
    if any(word in desc_lower for word in ['maintenance', 'mro', 'reliability', 'health']):
        return ('MRO', 0.7)
    
    if any(word in desc_lower for word in ['spaceport', 'airport', 'ground', 'infrastructure']):
        return ('SPACEPORT', 0.7)
    
    if any(word in desc_lower for word in ['program', 'schedule', 'milestone', 'resource']):
        return ('PMO', 0.6)
    
    if any(word in desc_lower for word in ['configuration', 'baseline', 'nomenclature', 'governance']):
        return ('CM', 0.6)
    
    return ('CM', 0.3)  # Default


def determine_knot_and_aor(path: str, variant: str = '', type_code: str = '', description: str = '') -> Tuple[str, str, float]:
    """
    Determine KNOT and AoR using multiple heuristics.
    
    Args:
        path: File path
        variant: VARIANT field (optional)
        type_code: TYPE field (optional)
        description: DESCRIPTION field (optional)
    
    Returns:
        Tuple of (knot_id, aor, confidence) where confidence is 0.0-1.0
    """
    # Determine KNOT from path
    knot, knot_confidence = get_knot_from_path(path)
    
    # Determine AoR using multiple signals
    signals = []
    
    # Path-based signal (highest priority)
    aor_path, conf_path = get_aor_from_path(path)
    signals.append((aor_path, conf_path))
    
    # KNOT-based signal (if knot is not K00)
    if knot != 'K00' and knot_confidence > 0.5:
        aor_knot = get_aor_from_knot(knot)
        signals.append((aor_knot, 0.95))
    
    # VARIANT-based signal
    if variant:
        aor_variant, conf_variant = get_aor_from_variant(variant)
        signals.append((aor_variant, conf_variant))
    
    # TYPE-based signal
    if type_code:
        aor_type, conf_type = get_aor_from_type(type_code)
        signals.append((aor_type, conf_type))
    
    # DESCRIPTION-based signal
    if description:
        aor_desc, conf_desc = get_aor_from_description(description)
        signals.append((aor_desc, conf_desc))
    
    # Weight signals by confidence and pick highest
    signals.sort(key=lambda x: x[1], reverse=True)
    aor = signals[0][0] if signals else 'CM'
    confidence = max(knot_confidence, signals[0][1] if signals else 0.3)
    
    return (knot, aor, confidence)


if __name__ == '__main__':
    # Test cases
    test_cases = [
        ('AMPEL360-SPACE-T-PORTAL/STK_CERT-cert-certification-authorities/KNOTS/K01_certification-authority-basis/file.md', 'CERT', 'FHA', 'certification-basis'),
        ('AMPEL360-SPACE-T-PORTAL/STK_SAF-saf-safety/KNOTS/K03_hazard-management/file.md', 'PLUS', 'FHA', 'propulsion-hazards'),
        ('00_00_STD_LC01_AMPEL360_SPACET_PLUS_nomenclature-standard_v02.md', 'PLUS', 'STD', 'nomenclature-standard'),
    ]
    
    print("Testing KNOT and AoR determination:")
    for path, variant, type_code, desc in test_cases:
        knot, aor, conf = determine_knot_and_aor(path, variant, type_code, desc)
        print(f"\nPath: {path}")
        print(f"  KNOT: {knot}, AoR: {aor}, Confidence: {conf:.2f}")
