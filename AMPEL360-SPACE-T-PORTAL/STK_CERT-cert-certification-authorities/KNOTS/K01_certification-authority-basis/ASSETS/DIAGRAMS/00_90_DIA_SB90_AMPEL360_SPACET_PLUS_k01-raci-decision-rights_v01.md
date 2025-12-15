---
knot_id: K01
type: DIA
format: table
---

# K01 RACI - Decision Rights Matrix

## Certification Authority Basis Activities

| Activity | STK_CERT | STK_CM | STK_PMO | STK_SE | STK_SAF | STK_DATA | Authority |
|:---------|:--------:|:------:|:-------:|:------:|:-------:|:--------:|:---------:|
| Define Certification Basis | **R** | A | C | C | C | C | **A** |
| Map Compliance Requirements | **R** | A | I | C | C | I | I |
| Collect Evidence | A | C | I | **R** | **R** | C | I |
| Package Evidence | **R** | A | I | C | C | C | I |
| Submit to Authority | **R** | C | I | I | I | I | **A** |
| Manage Decision Records | **R** | **A** | I | C | C | I | C |
| Baseline Control | C | **R/A** | C | I | I | I | I |

**Legend:**
- **R**: Responsible (does the work)
- **A**: Accountable (final approval)
- **C**: Consulted (provides input)
- **I**: Informed (kept updated)

## Decision Authority Levels

1. **Program Level**: STK_CM (with STK_CERT input)
2. **Technical Level**: STK_CERT (with stakeholder consultation)
3. **Authority Level**: Certification Authority (external)
