---
title: "{{KNOT_ID}} ATA {{ATA_CODE}} Evidence Pack Summary"
type: RPT
project: AMPEL360
program: SPACET
variant: "{{VARIANT}}"
report_date: "{{DATE}}"
author: "{{OWNER}}"
status: Draft
knot_id: "{{KNOT_ID}}"
ata_code: "{{ATA_CODE}}"
---

# Evidence Pack Summary: {{KNOT_ID}} ATA {{ATA_CODE}}

## Executive Summary

This report summarizes the evidence pack for **{{KNOT_ID}}** covering **ATA {{ATA_CODE}} ({{ATA_TITLE}})**.

**Purpose:** {{PURPOSE}}

**Total Evidence Items:** {{ITEM_COUNT}}

**Manifest File:** `{{MANIFEST_FILENAME}}`

**Pack Status:** {{STATUS}}

---

## Evidence Summary by Category

| Category | Count | Status |
| :--- | :---: | :--- |
| Requirements | {{REQ_COUNT}} | {{REQ_STATUS}} |
| Acceptance Criteria | {{AC_COUNT}} | {{AC_STATUS}} |
| Decisions | {{DEC_COUNT}} | {{DEC_STATUS}} |
| Evidence | {{EVD_COUNT}} | {{EVD_STATUS}} |
| Traceability | {{TRC_COUNT}} | {{TRC_STATUS}} |
| Reports | {{RPT_COUNT}} | {{RPT_STATUS}} |
| Schemas | {{SCH_COUNT}} | {{SCH_STATUS}} |
| Tables | {{TAB_COUNT}} | {{TAB_STATUS}} |
| Diagrams | {{DIA_COUNT}} | {{DIA_STATUS}} |

---

## Detailed Evidence Inventory

### Requirements

| # | Path | Type | Version | SHA256 (first 16 chars) |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `{{PATH}}` | {{TYPE}} | {{VERSION}} | `{{SHA256_SHORT}}...` |

### Acceptance Criteria

| # | Path | Type | Version | SHA256 (first 16 chars) |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `{{PATH}}` | {{TYPE}} | {{VERSION}} | `{{SHA256_SHORT}}...` |

### Evidence Artifacts

| # | Path | Type | Version | SHA256 (first 16 chars) |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `{{PATH}}` | {{TYPE}} | {{VERSION}} | `{{SHA256_SHORT}}...` |

### Traceability Links

| # | Path | Type | Version | SHA256 (first 16 chars) |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `{{PATH}}` | {{TYPE}} | {{VERSION}} | `{{SHA256_SHORT}}...` |

---

## Verification Status

| Check | Status | Notes |
| :--- | :---: | :--- |
| Evidence items collected | {{COLLECTED_STATUS}} | {{ITEM_COUNT}} items |
| SHA256 hashes computed | {{HASH_STATUS}} | All items hashed |
| Manifest generated | {{MANIFEST_STATUS}} | JSON format |
| Nomenclature compliance | {{NOMENCLATURE_STATUS}} | Run `validate_nomenclature.py` |
| Signature | {{SIGNATURE_STATUS}} | Pending review and approval |

---

## Cross-Reference Matrix

| Evidence ID | Depends On | Referenced By | Verification Status |
| :--- | :--- | :--- | :--- |
| EVD-{{KNOT_ID}}-001 | {{DEPENDS_ON}} | {{REFERENCED_BY}} | {{VERIFICATION_STATUS}} |

---

## Reproducibility

This evidence pack was generated using the automated generator script.

To reproduce:

```bash
python scripts/generate_evidence_pack.py --knot {{KNOT_ID}} --ata {{ATA_CODE}}
```

### Generator Parameters

| Parameter | Value |
| :--- | :--- |
| Knot ID | {{KNOT_ID}} |
| ATA Code | {{ATA_CODE}} |
| ATA Title | {{ATA_TITLE}} |
| Variant | {{VARIANT}} |
| Owner | {{OWNER}} |
| Repository Root | {{REPO_ROOT}} |
| Generated At | {{TIMESTAMP}} |

---

## Next Steps

1. [ ] Review evidence inventory for completeness
2. [ ] Validate nomenclature compliance: `python validate_nomenclature.py --check-all`
3. [ ] Link acceptance criteria to evidence items
4. [ ] Obtain CM/QA review and approval
5. [ ] Sign manifest with appropriate key
6. [ ] Tag baseline in version control

---

## Baseline Information

**Target Baseline:** {{KNOT_ID}}-{{ATA_TITLE}}-{{ATA_CODE}}-v01

**Baseline Date:** {{BASELINE_DATE}}

**Baseline Manager:** Configuration Management WG

**Baseline Status:** {{BASELINE_STATUS}}

### Baseline Approval Process

1. {{BASELINE_STEP_1_STATUS}} All deliverables created
2. {{BASELINE_STEP_2_STATUS}} Nomenclature validation passed
3. {{BASELINE_STEP_3_STATUS}} Evidence hashes computed
4. {{BASELINE_STEP_4_STATUS}} CM WG approval obtained
5. {{BASELINE_STEP_5_STATUS}} Baseline tag created
6. {{BASELINE_STEP_6_STATUS}} Evidence pack frozen

---

## Signed Export Requirements

**Digital Signature:** Required for baseline approval

**Signing Authority:** CM WG Lead

**Signing Tool:** GPG (GNU Privacy Guard)

**Signature Process** (when baseline ready):

```bash
# Create baseline tag (signed)
git tag -s {{KNOT_ID}}-{{ATA_TITLE}}-{{ATA_CODE}}-v01 -m "{{KNOT_ID}} {{ATA_TITLE}} baseline"

# Verify signature
git tag -v {{KNOT_ID}}-{{ATA_TITLE}}-{{ATA_CODE}}-v01

# Export evidence pack
git archive --format=tar.gz --prefix={{KNOT_ID}}-evidence/ {{KNOT_ID}}-{{ATA_TITLE}}-{{ATA_CODE}}-v01 > {{KNOT_ID}}-evidence-pack-signed.tar.gz

# Sign archive
gpg --detach-sign --armor {{KNOT_ID}}-evidence-pack-signed.tar.gz
```

---

## Document Control

| Field | Value |
| :--- | :--- |
| **Generated** | {{TIMESTAMP}} |
| **Generator** | `scripts/generate_evidence_pack.py` v1.0 |
| **Knot** | {{KNOT_ID}} |
| **ATA** | {{ATA_CODE}} - {{ATA_TITLE}} |
| **Items** | {{ITEM_COUNT}} |
| **Manifest** | `{{MANIFEST_FILENAME}}` |
| **Version** | {{VERSION}} |
| **Status** | {{STATUS}} |

---

**Maintained By:** Configuration Management WG

**Last Updated:** {{DATE}}
