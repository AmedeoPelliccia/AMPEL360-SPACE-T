# AMPEL360 Space-T PR^3-3 Known Issues

**Release:** PR^3-3 Predicted Release  
**Status:** ACTIVE  
**Date:** 2025-12-17  
**Owner:** Configuration Management Working Group

---

## Overview

This document tracks known issues, limitations, and deferred items for the PR^3-3 Predicted Release. All items have been reviewed and accepted by the Configuration Management Working Group.

---

## Critical Issues

### None

No critical issues identified at release time.

---

## High Priority Issues

### 1. Broken Internal Links (803 identified)

**Issue ID:** KI-PR3-001  
**Priority:** High  
**Category:** Documentation  
**Status:** Known, Deferred to Post-Release  
**Target Resolution:** Within 1 week post-release

**Description:**
Link checker identified 803 broken internal links in Markdown files after v6.0 migration.

**Impact:**
- Documentation navigation impaired
- Cross-references may not work correctly
- Portal navigation affected

**Root Cause:**
- v6.0 filename migration changed file paths
- Cross-references not fully updated
- Some links reference deprecated v5.0 filenames

**Mitigation:**
- Validation tooling still functional (links to config files unaffected)
- Core functionality not impacted
- Documentation still readable (only links broken)

**Resolution Plan:**
1. Use `scripts/check_and_update_links.py --update` to fix automatically
2. Manual review of unfixable links
3. Update cross-references using v6 rename map
4. Re-validate all links
5. Deploy hotfix within 1 week

**Owner:** Documentation Team / CM WG  
**Estimated Effort:** 8-16 hours

---

## Medium Priority Issues

### 2. GATE-004 Not Implemented (Namespace Deduplication)

**Issue ID:** KI-PR3-002  
**Priority:** Medium  
**Category:** CI/CD Governance  
**Status:** Planned, Not Implemented  
**Target Resolution:** Next minor release

**Description:**
GATE-004 (Namespace Deduplication Check) is defined but not yet implemented.

**Impact:**
- No automated check for duplicate namespace IDs in ATA 99 registry
- Manual review required for namespace conflicts
- Risk of duplicate identifiers

**Mitigation:**
- Manual review process in place
- Low risk (limited namespace changes expected)
- Schema validation catches some issues

**Resolution Plan:**
1. Implement `scripts/check_ata99_registry.py`
2. Integrate with CI workflow
3. Add to blocking gates
4. Document in governance gates index

**Owner:** Data Governance / CM WG  
**Target Release:** Next minor (Q1 2026)

---

### 3. GATE-005 Not Implemented (Identifier Grammar Check)

**Issue ID:** KI-PR3-003  
**Priority:** Medium  
**Category:** CI/CD Governance  
**Status:** Planned, Not Implemented  
**Target Resolution:** Next minor release

**Description:**
GATE-005 (Identifier Grammar Check) is defined but not yet implemented.

**Impact:**
- No automated validation of identifier syntax beyond nomenclature
- Manual review required for complex identifiers
- Risk of inconsistent identifier formats

**Mitigation:**
- Nomenclature validation catches most issues
- Identifier governance policy documented
- Manual review in PR process

**Resolution Plan:**
1. Implement `scripts/validate_identifiers.py`
2. Define identifier grammar rules
3. Integrate with CI workflow
4. Add to blocking gates

**Owner:** Systems Engineering / CM WG  
**Target Release:** Next minor (Q1 2026)

---

### 4. GATE-007 Not Implemented (Breaking Schema Detection)

**Issue ID:** KI-PR3-004  
**Priority:** Medium  
**Category:** CI/CD Governance  
**Status:** Planned, Not Implemented  
**Target Resolution:** Next minor release

**Description:**
GATE-007 (Breaking Schema Change Detection) is defined but not yet implemented.

**Impact:**
- No automated detection of breaking schema changes
- Manual review required for schema modifications
- Risk of unintended breaking changes

**Mitigation:**
- Schema validation catches structural issues
- Change control process requires CM review
- Schema registry tracks versions

**Resolution Plan:**
1. Implement `scripts/detect_schema_breaking_changes.py`
2. Define breaking change rules
3. Integrate with CI workflow
4. Add to blocking gates

**Owner:** Data Governance / CM WG  
**Target Release:** Next minor (Q1 2026)

---

### 5. GATE-008 Not Implemented (Evidence Link Validation)

**Issue ID:** KI-PR3-005  
**Priority:** Medium  
**Category:** CI/CD Governance  
**Status:** Planned, Not Implemented  
**Target Resolution:** Next minor release

**Description:**
GATE-008 (Evidence Link Validation) is defined but not yet implemented.

**Impact:**
- No automated validation of evidence links
- Manual review required for compliance evidence
- Risk of broken evidence trails

**Mitigation:**
- Trace link validation covers some evidence
- Audit proof path validation operational
- Manual review in certification process

**Resolution Plan:**
1. Implement `scripts/validate_evidence_links.py`
2. Define evidence link requirements
3. Integrate with CI workflow
4. Add to warning or blocking gates

**Owner:** Certification / CM WG  
**Target Release:** Next minor (Q1 2026)

---

## Low Priority Issues

### 6. Limited Ecosystem Integration

**Issue ID:** KI-PR3-006  
**Priority:** Low  
**Category:** Tooling  
**Status:** Enhancement Request  
**Target Resolution:** Future release

**Description:**
Current tooling is Python-based. Integration with other ecosystems (JavaScript, Java, etc.) not available.

**Impact:**
- Limited use in non-Python projects
- Manual validation required for other languages
- Reduced automation potential

**Mitigation:**
- Python tooling sufficient for current needs
- Documentation in markdown (language-agnostic)
- APIs can be called from other languages

**Resolution Plan:**
1. Assess demand for other language support
2. Design language-agnostic APIs
3. Implement bindings for common languages
4. Package for distribution (npm, Maven, etc.)

**Owner:** Engineering Tools / Future Planning  
**Target Release:** TBD based on demand

---

### 7. Template Coverage Incomplete

**Issue ID:** KI-PR3-007  
**Priority:** Low  
**Category:** Documentation  
**Status:** Enhancement Request  
**Target Resolution:** Ongoing

**Description:**
Not all TYPE codes have corresponding templates. 22 templates available, but 29 TYPEs defined.

**Impact:**
- Some artifact types require manual template creation
- Inconsistent scaffolding experience
- Learning curve for new TYPEs

**Mitigation:**
- Most common TYPEs have templates
- Scaffolding tool generates valid filenames
- Generic templates can be adapted

**Resolution Plan:**
1. Prioritize templates based on usage
2. Create missing templates incrementally
3. Community contribution encouraged
4. Template generator tool (future enhancement)

**Owner:** Documentation Team / CM WG  
**Target Release:** Ongoing improvements

---

## Deferred Features

### 8. TEKNIA Credential Issuance Portal

**Feature ID:** DF-PR3-001  
**Priority:** Medium  
**Category:** Feature  
**Status:** Deferred  
**Target Delivery:** Future release

**Description:**
Web-based portal for TEKNIA credential issuance not yet implemented.

**Current State:**
- TEKNIA schema defined
- Validation tooling operational
- Manual credential creation supported

**Future Enhancement:**
- Web UI for credential issuance
- Workflow automation
- Digital signature integration
- Blockchain anchoring (optional)

**Owner:** TEKNIA Team / Future Planning  
**Target Release:** TBD

---

### 9. Advanced Analytics Dashboard

**Feature ID:** DF-PR3-002  
**Priority:** Low  
**Category:** Feature  
**Status:** Deferred  
**Target Delivery:** Future release

**Description:**
Analytics dashboard for nomenclature compliance metrics, validation trends, and governance insights.

**Current State:**
- Basic reports via CLI tools
- CSV exports available
- Manual analysis required

**Future Enhancement:**
- Web-based dashboard
- Real-time metrics
- Trend analysis
- Customizable reports

**Owner:** Data Analytics Team / Future Planning  
**Target Release:** TBD

---

## Workarounds

### For Broken Internal Links (KI-PR3-001)

**Temporary Workaround:**
1. Use repository search to find referenced files
2. Manually navigate to correct file paths
3. Reference `rename_map_v6.csv` for path mappings
4. Use GitHub's file finder (press `t` in repo)

**Permanent Fix:**
Scheduled for post-release hotfix (within 1 week).

---

### For Missing Gates (KI-PR3-002 through KI-PR3-005)

**Temporary Workaround:**
1. Manual review by CM WG for affected PRs
2. Use existing validation tools where applicable
3. Follow documented processes (schemas, identifiers, evidence)
4. Request CM WG review for high-risk changes

**Permanent Fix:**
Scheduled for next minor release (Q1 2026).

---

## Issue Tracking

All issues tracked in GitHub Issues with appropriate labels:

- `known-issue` - Items in this document
- `deferred` - Features deferred to future releases
- `post-release` - Items for post-release hotfix
- `next-release` - Items for next minor/major release

**GitHub Label Filter:**
```
label:known-issue milestone:PR^3-3
```

---

## Risk Assessment

### Overall Risk Level: **LOW**

**Justification:**
- No critical issues
- High-priority issues have clear mitigation and resolution plans
- Core functionality validated and operational
- Known limitations documented and understood

### Risk Matrix

| Issue | Likelihood | Impact | Risk Level | Mitigation |
|-------|-----------|--------|------------|------------|
| KI-PR3-001 | High | Medium | Medium | Post-release hotfix scheduled |
| KI-PR3-002 | Low | Low | Low | Manual review process |
| KI-PR3-003 | Low | Low | Low | Nomenclature validation sufficient |
| KI-PR3-004 | Low | Medium | Low | Change control + manual review |
| KI-PR3-005 | Low | Low | Low | Existing validation covers most cases |

---

## Communication Plan

### Stakeholder Notification

All stakeholders notified via:
- ✅ Release notes
- ✅ This known issues document
- ✅ GitHub release announcement
- ✅ Repository README update

### Support Channels

Users encountering issues should:
1. Check this document first
2. Search GitHub Issues
3. Review documentation
4. Contact CM WG if unresolved

---

## Review Schedule

This document will be reviewed and updated:

- **Post-release:** After hotfix deployment (1 week)
- **Quarterly:** Review deferred items and priorities
- **Next release:** Update for next release cycle

---

## Appendix: Issue Resolution Criteria

### High Priority
- Must be resolved within 1 week to 1 month
- Significant impact on user experience
- Clear resolution plan required
- Owner assigned

### Medium Priority
- Target resolution: Next minor release
- Moderate impact or workaround available
- Planned for upcoming sprint
- Owner identified

### Low Priority
- Target resolution: Future release (TBD)
- Minimal impact or enhancement request
- Deferred based on priority
- Owner may be unassigned

---

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| I01-R01 | 2025-12-17 | CM WG | Initial known issues document for PR^3-3 |

---

**Document Control**

- **Owner**: Configuration Management WG
- **Status**: ACTIVE
- **Version**: I01-R01
- **Created**: 2025-12-17
- **Last Updated**: 2025-12-17
- **Next Review**: Post-release + 1 week
