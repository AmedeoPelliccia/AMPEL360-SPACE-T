# KNU Token Distribution System

## Overview

The **KNU Token Distribution System** distributes token rewards to contributors based on a weighted combination of **predicted effort** and **measured impact** (including spillover effects to adjacent KNOTs).

This system implements the distribution formula:

```
w_i = α·Ê_i + (1-α)·Î_i
T_i = P_k · w_i
```

Where:
- `P_k` = Prize pool (total KNU tokens for the KNOT)
- `E_i` = Predicted effort (normalized)
- `Ê_i` = Normalized effort: `E_i / Σ E_i`
- `I_i` = Effective impact: `ΔR_k,i + λ·S_i`
- `Î_i` = Normalized impact: `I_i / Σ I_i`
- `S_i` = Spillover: `Σ(a_k→j · ΔR_j,i)` for adjacent KNOTs
- `ΔR_k,i` = Direct residue reduction attributed to KNU
- `a_k→j` = Adjacency weight between KNOTs

**Default Parameters:**
- `α = 0.30` (30% effort, 70% impact)
- `λ = 0.50` (spillover worth 50% of direct impact)

## Files

### Configuration
- **`config/tokenomics/knu_distribution.yaml`** - Central configuration for distribution parameters, eligibility criteria, KNOT pools, and adjacency graph

### Schema
- **`schemas/knu_reward_record.schema.json`** - JSON Schema for reward record validation

### Templates
- **`templates/knu-reward-ledger.csv`** - CSV template for tracking KNU rewards

### Scripts
- **`scripts/knu_token_distribution.py`** - Main distribution calculator with CLI commands

## Usage

### 1. Prepare KNU Entries

Create a CSV file with your KNU entries following the template in `templates/knu-reward-ledger.csv`:

```csv
knot_id,knu_id,owner,E_pred,dR_primary,dR_adj_sum,status,artifacts,validated_by,validated_at,weight,tokens_awarded
K06,KNU-K06-00-001,CM WG,5.0,30.0,10.0,merged,schema_v2.json;migration_guide.md,Lead Architect,2026-01-10T12:00:00Z,,
K06,KNU-K06-00-002,AI/ML Engineering,3.0,15.0,5.0,accepted,trace_validator.py,QA Team,2026-01-10T14:00:00Z,,
```

**Field Descriptions:**
- `knot_id` - KNOT identifier (K01-K14)
- `knu_id` - Unique KNU identifier (format: `KNU-{KNOT}-{PARTITION}-{SEQUENCE}`)
- `owner` - Person or team responsible for resolution
- `E_pred` - Predicted effort score (arbitrary units, normalized during calculation)
- `dR_primary` - Direct residue reduction in primary KNOT (0-100%)
- `dR_adj_sum` - Sum of residue reductions in adjacent KNOTs (0-100%)
- `status` - Current status (`draft`, `submitted`, `in_review`, `accepted`, `merged`, `rejected`)
- `artifacts` - Semicolon-separated list of artifact references
- `validated_by` - Name of validator who confirmed impact
- `validated_at` - Validation timestamp (ISO 8601 format)
- `weight` - Calculated distribution weight (filled by script)
- `tokens_awarded` - Number of tokens awarded (filled by script)

### 2. Distribute Tokens

Run the distribution command:

```bash
python scripts/knu_token_distribution.py distribute \
  --knot K06 \
  --pool 1000 \
  --input knu_entries.csv \
  --output knu_rewards.csv
```

**Options:**
- `--knot` (required) - KNOT ID (e.g., K06)
- `--pool` (optional) - Pool amount (overrides config default)
- `--input` (required) - Input CSV file with KNU entries
- `--output` (optional) - Output CSV file (defaults to overwriting input)
- `--alpha` (optional) - Effort weight (0.0-1.0, default: 0.30)
- `--lambda` (optional) - Spillover multiplier (0.0-1.0, default: 0.50)

**Example with custom parameters:**
```bash
python scripts/knu_token_distribution.py distribute \
  --knot K06 \
  --pool 1000 \
  --input knu_entries.csv \
  --alpha 0.25 \
  --lambda 0.60
```

### 3. Generate Distribution Report

Generate a JSON report with detailed distribution information:

```bash
python scripts/knu_token_distribution.py report \
  --knot K06 \
  --input knu_rewards.csv \
  --output distribution_report.json
```

**Report Contents:**
- Distribution timestamp
- KNOT ID and pool configuration
- Distribution parameters (α, λ)
- All KNU entries with calculated weights and token awards
- Total tokens distributed
- Number of eligible entries

### 4. Validate KNU Eligibility

Check if a specific KNU entry qualifies for rewards:

```bash
python scripts/knu_token_distribution.py validate \
  --knot K06 \
  --knu KNU-K06-00-001 \
  --input knu_entries.csv
```

**Eligibility Criteria (default):**
- Status must be `accepted` or `merged`
- Must have at least one artifact
- Must be validated by an authorized reviewer

## Example Calculation

Given the reference example from the requirements:

**Input:**
- Pool: 1000 tokens
- α = 0.30, λ = 0.50
- KNU1: E=5, ΔR_k=30, S=10
- KNU2: E=3, ΔR_k=15, S=5
- KNU3: E=2, ΔR_k=5, S=0

**Calculation:**

1. **Effective Impact:** `I_i = ΔR_k,i + λ·S_i`
   - KNU1: 30 + 0.50×10 = 35
   - KNU2: 15 + 0.50×5 = 17.5
   - KNU3: 5 + 0.50×0 = 5

2. **Normalized Effort:** `Ê_i = E_i / ΣE_i`
   - E_total = 10
   - KNU1: 5/10 = 0.50
   - KNU2: 3/10 = 0.30
   - KNU3: 2/10 = 0.20

3. **Normalized Impact:** `Î_i = I_i / ΣI_i`
   - I_total = 57.5
   - KNU1: 35/57.5 = 0.6087
   - KNU2: 17.5/57.5 = 0.3043
   - KNU3: 5/57.5 = 0.0870

4. **Weights:** `w_i = α·Ê_i + (1-α)·Î_i`
   - KNU1: 0.30×0.50 + 0.70×0.6087 = 0.5761
   - KNU2: 0.30×0.30 + 0.70×0.3043 = 0.3030
   - KNU3: 0.30×0.20 + 0.70×0.0870 = 0.1209

5. **Token Awards:** `T_i = P_k · w_i`
   - KNU1: 1000 × 0.5761 = **576 tokens**
   - KNU2: 1000 × 0.3030 = **303 tokens**
   - KNU3: 1000 × 0.1209 = **121 tokens**

## Configuration

### Adjusting Distribution Parameters

Edit `config/tokenomics/knu_distribution.yaml`:

```yaml
parameters:
  alpha: 0.30           # Effort weight (0.0-1.0)
  lambda_spillover: 0.50 # Spillover multiplier (0.0-1.0)
```

### Modifying Eligibility Criteria

```yaml
eligibility:
  required_status:
    - "accepted"
    - "merged"
  require_artifacts: true
  require_validation: true
```

### Updating KNOT Pools

```yaml
knot_pools:
  K06:
    base_pool: 1000
    description: "Data governance SSOT schemas identifiers"
```

### Defining Adjacency Relationships

The adjacency graph defines how impact in one KNOT spills over to adjacent KNOTs:

```yaml
adjacency_graph:
  K06:
    K01: 0.3  # Data governance → Certification
    K05: 0.3  # Data governance → Model fidelity
    K07: 0.4  # Data governance → AI/ML
    K08: 0.5  # Data governance → DPP
```

## Integration with Existing Code

The token distribution system integrates with existing AMPEL360 Space-T components:

### KNOT-AoR Mapping
- Imports `KNOT_AOR_MAPPING` from `scripts/knot_aor_mapping.py`
- Uses KNOT definitions to derive adjacency relationships

### NKU Scoring Patterns
- Follows CSV handling patterns from `scripts/nku_scoring.py`
- Implements CSV injection prevention
- Uses similar dataclass patterns and CLI structure

## Security Considerations

### CSV Injection Prevention
All CSV fields are sanitized to prevent injection attacks:
- Dangerous characters (`=`, `+`, `-`, `@`, tabs, newlines) are prefixed with a single quote
- Embedded newlines are replaced with spaces

### Input Validation
- KNOT IDs validated against pattern `^K(0[1-9]|1[0-4])$`
- KNU IDs validated against pattern `^KNU-K(0[1-9]|1[0-4])-[A-Z0-9]{2,6}-\d{3}$`
- Numeric values constrained (effort ≥ 0, residue 0-100%)
- Required fields enforced by JSON Schema

## Troubleshooting

### Error: "No eligible KNU entries"
- Check that KNU entries have status `accepted` or `merged`
- Verify artifacts are provided
- Ensure entries are validated by an authorized reviewer

### Error: "No pool configuration found"
- Check that the KNOT ID exists in `config/tokenomics/knu_distribution.yaml`
- Verify KNOT ID format (K01-K14)

### Calculation discrepancies
- Verify input data is correct (E_pred, dR_primary, dR_adj_sum)
- Check that spillover values (dR_adj_sum) are pre-calculated correctly
- Ensure normalization is working (weights should sum to 1.0)

## References

- **Problem Statement**: See issue requirements for full specification
- **KNOT Governance**: K01-K14 definitions with uncertainty focus
- **NKU Scoring**: `scripts/nku_scoring.py` for related uncertainty tracking
- **KNOT-AoR Mapping**: `scripts/knot_aor_mapping.py` for KNOT relationships
