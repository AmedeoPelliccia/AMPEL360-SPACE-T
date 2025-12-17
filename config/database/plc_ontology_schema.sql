-- AMPEL360 Space-T PLC Ontology Database Schema
-- Version: 1.0
-- Date: 2025-12-17
-- Standard: Nomenclature v6.0 R1.0
-- Purpose: Relational ontology database for PLC gate control logic
--
-- This schema implements the PLC gate tracking and ontology database
-- as specified in KI-PR3-001 through KI-PR3-005 implementation plan.

-- ============================================================================
-- SECTION A: Gate Registry (PLC Ladder Diagram in Tables)
-- ============================================================================

-- Gate definitions (the PLC ladder diagram)
CREATE TABLE IF NOT EXISTS gate (
    gate_code VARCHAR(20) PRIMARY KEY,
    gate_name VARCHAR(255) NOT NULL,
    description TEXT,
    owner_aor VARCHAR(20) NOT NULL,
    default_severity VARCHAR(20) NOT NULL CHECK (default_severity IN ('BLOCK', 'WARN', 'INFO')),
    mode_pr3 VARCHAR(20) NOT NULL DEFAULT 'WARN' CHECK (mode_pr3 IN ('WARN', 'BLOCK', 'FREEZE')),
    script_entrypoint VARCHAR(255),
    rung_id INTEGER,
    implementation_status VARCHAR(20) DEFAULT 'PLANNED' CHECK (implementation_status IN ('ACTIVE', 'PLANNED', 'DEPRECATED')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Gate execution runs (tracks each validation run)
CREATE TABLE IF NOT EXISTS gate_run (
    run_id INTEGER PRIMARY KEY AUTOINCREMENT,
    gate_code VARCHAR(20) NOT NULL,
    run_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    git_ref VARCHAR(255),
    git_sha VARCHAR(40),
    pr_number INTEGER,
    branch_name VARCHAR(255),
    passed BOOLEAN NOT NULL,
    error_count INTEGER DEFAULT 0,
    warning_count INTEGER DEFAULT 0,
    info_count INTEGER DEFAULT 0,
    execution_time_ms INTEGER,
    metadata JSON,
    FOREIGN KEY (gate_code) REFERENCES gate(gate_code)
);

-- Individual gate findings (normalized finding rows)
CREATE TABLE IF NOT EXISTS gate_finding (
    finding_id INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id INTEGER NOT NULL,
    gate_code VARCHAR(20) NOT NULL,
    severity VARCHAR(20) NOT NULL CHECK (severity IN ('ERROR', 'WARN', 'INFO')),
    artifact_path VARCHAR(512),
    artifact_id VARCHAR(255),
    finding_code VARCHAR(50),
    message TEXT NOT NULL,
    details JSON,
    line_number INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (run_id) REFERENCES gate_run(run_id),
    FOREIGN KEY (gate_code) REFERENCES gate(gate_code)
);

CREATE INDEX idx_gate_run_timestamp ON gate_run(run_timestamp);
CREATE INDEX idx_gate_run_gate_code ON gate_run(gate_code);
CREATE INDEX idx_gate_finding_run_id ON gate_finding(run_id);
CREATE INDEX idx_gate_finding_artifact_path ON gate_finding(artifact_path);

-- ============================================================================
-- SECTION B: Namespace Registry (for GATE-004)
-- ============================================================================

-- Namespace registry for ATA 99 deduplication
CREATE TABLE IF NOT EXISTS namespace_registry (
    namespace_id VARCHAR(255) PRIMARY KEY,
    namespace_type VARCHAR(50) NOT NULL,
    scope VARCHAR(100),
    owner_aor VARCHAR(20) NOT NULL,
    artifact_path VARCHAR(512) NOT NULL,
    artifact_sha256 VARCHAR(64),
    description TEXT,
    status VARCHAR(20) DEFAULT 'ACTIVE' CHECK (status IN ('ACTIVE', 'DEPRECATED', 'SUPERSEDED')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Namespace conflicts (detected duplicates)
CREATE TABLE IF NOT EXISTS namespace_conflict (
    conflict_id INTEGER PRIMARY KEY AUTOINCREMENT,
    namespace_id VARCHAR(255) NOT NULL,
    artifact_path_1 VARCHAR(512) NOT NULL,
    artifact_path_2 VARCHAR(512) NOT NULL,
    conflict_type VARCHAR(50) NOT NULL,
    detected_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    resolved BOOLEAN DEFAULT FALSE,
    resolution_notes TEXT,
    resolved_at TIMESTAMP
);

CREATE INDEX idx_namespace_type ON namespace_registry(namespace_type);
CREATE INDEX idx_namespace_owner ON namespace_registry(owner_aor);
CREATE INDEX idx_namespace_conflict_unresolved ON namespace_conflict(resolved) WHERE resolved = FALSE;

-- ============================================================================
-- SECTION C: Identifier Grammar Registry (for GATE-005)
-- ============================================================================

-- Identifier grammar definitions
CREATE TABLE IF NOT EXISTS identifier_grammar (
    identifier_kind VARCHAR(50) PRIMARY KEY,
    description TEXT,
    regex_pattern TEXT,
    jsonschema_fragment JSON,
    owner_aor VARCHAR(20) NOT NULL,
    examples JSON,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Identifier instances extracted from artifacts
CREATE TABLE IF NOT EXISTS identifier_instance (
    instance_id INTEGER PRIMARY KEY AUTOINCREMENT,
    identifier_kind VARCHAR(50) NOT NULL,
    identifier_value VARCHAR(255) NOT NULL,
    artifact_path VARCHAR(512) NOT NULL,
    artifact_line INTEGER,
    context JSON,
    valid BOOLEAN,
    validation_errors JSON,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (identifier_kind) REFERENCES identifier_grammar(identifier_kind)
);

CREATE INDEX idx_identifier_instance_kind ON identifier_instance(identifier_kind);
CREATE INDEX idx_identifier_instance_artifact ON identifier_instance(artifact_path);
CREATE INDEX idx_identifier_instance_invalid ON identifier_instance(valid) WHERE valid = FALSE;

-- ============================================================================
-- SECTION D: Schema Registry + Diff Ledger (for GATE-007)
-- ============================================================================

-- Schema registry
CREATE TABLE IF NOT EXISTS schema_registry (
    schema_id VARCHAR(255) NOT NULL,
    version VARCHAR(50) NOT NULL,
    artifact_path VARCHAR(512) NOT NULL,
    artifact_sha256 VARCHAR(64) NOT NULL,
    owner_aor VARCHAR(20) NOT NULL,
    schema_content JSON,
    status VARCHAR(20) DEFAULT 'ACTIVE' CHECK (status IN ('ACTIVE', 'DEPRECATED', 'SUPERSEDED')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (schema_id, version)
);

-- Schema change events (breaking change detection)
CREATE TABLE IF NOT EXISTS schema_change_event (
    event_id INTEGER PRIMARY KEY AUTOINCREMENT,
    schema_id VARCHAR(255) NOT NULL,
    from_version VARCHAR(50) NOT NULL,
    to_version VARCHAR(50) NOT NULL,
    from_sha256 VARCHAR(64) NOT NULL,
    to_sha256 VARCHAR(64) NOT NULL,
    breaking_score INTEGER DEFAULT 0,
    breaking_reasons JSON,
    change_type VARCHAR(50),
    detected_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    reviewed BOOLEAN DEFAULT FALSE,
    review_notes TEXT,
    reviewed_by VARCHAR(100),
    reviewed_at TIMESTAMP
);

CREATE INDEX idx_schema_registry_id ON schema_registry(schema_id);
CREATE INDEX idx_schema_change_breaking ON schema_change_event(breaking_score) WHERE breaking_score > 0;

-- ============================================================================
-- SECTION E: Evidence Graph (for GATE-008)
-- ============================================================================

-- Evidence references
CREATE TABLE IF NOT EXISTS evidence_ref (
    evidence_id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_artifact_id VARCHAR(255) NOT NULL,
    source_artifact_path VARCHAR(512) NOT NULL,
    target_path VARCHAR(512),
    target_artifact_id VARCHAR(255),
    evidence_kind VARCHAR(50) NOT NULL CHECK (evidence_kind IN ('HASH', 'REPORT', 'DATASET', 'TEST_LOG', 'CERTIFICATE', 'TRACE', 'OTHER')),
    required BOOLEAN DEFAULT FALSE,
    resolved BOOLEAN DEFAULT FALSE,
    resolution_status VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Evidence resolution tracking
CREATE TABLE IF NOT EXISTS evidence_resolution (
    resolution_id INTEGER PRIMARY KEY AUTOINCREMENT,
    evidence_id INTEGER NOT NULL,
    resolved_path VARCHAR(512),
    hash_match BOOLEAN,
    commit_ref_match BOOLEAN,
    validation_errors JSON,
    checked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (evidence_id) REFERENCES evidence_ref(evidence_id)
);

CREATE INDEX idx_evidence_source ON evidence_ref(source_artifact_path);
CREATE INDEX idx_evidence_target ON evidence_ref(target_path);
CREATE INDEX idx_evidence_unresolved ON evidence_ref(resolved) WHERE resolved = FALSE;
CREATE INDEX idx_evidence_required_unresolved ON evidence_ref(required, resolved) WHERE required = TRUE AND resolved = FALSE;

-- ============================================================================
-- SECTION F: Clustering & Governance Profiles
-- ============================================================================

-- Cluster definitions
CREATE TABLE IF NOT EXISTS cluster (
    cluster_id VARCHAR(50) PRIMARY KEY,
    cluster_name VARCHAR(255) NOT NULL,
    description TEXT,
    owner_aor VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Cluster membership rules (token-based constraints)
CREATE TABLE IF NOT EXISTS cluster_membership_rule (
    rule_id INTEGER PRIMARY KEY AUTOINCREMENT,
    cluster_id VARCHAR(50) NOT NULL,
    rule_type VARCHAR(50) NOT NULL CHECK (rule_type IN ('AOR', 'MODEL', 'TYPE', 'BLOCK', 'ATA_RANGE', 'VARIANT', 'PHASE', 'KNOT', 'CUSTOM')),
    rule_operator VARCHAR(20) DEFAULT 'IN' CHECK (rule_operator IN ('IN', 'NOT_IN', 'EQUALS', 'RANGE', 'REGEX')),
    rule_values JSON NOT NULL,
    priority INTEGER DEFAULT 0,
    FOREIGN KEY (cluster_id) REFERENCES cluster(cluster_id)
);

-- Cluster-specific constraints
CREATE TABLE IF NOT EXISTS cluster_constraint (
    constraint_id INTEGER PRIMARY KEY AUTOINCREMENT,
    cluster_id VARCHAR(50) NOT NULL,
    constraint_type VARCHAR(50) NOT NULL,
    constraint_condition JSON NOT NULL,
    severity VARCHAR(20) DEFAULT 'WARN' CHECK (severity IN ('BLOCK', 'WARN', 'INFO')),
    error_message TEXT,
    FOREIGN KEY (cluster_id) REFERENCES cluster(cluster_id)
);

CREATE INDEX idx_cluster_membership_cluster ON cluster_membership_rule(cluster_id);

-- ============================================================================
-- SECTION G: Artifact Metadata (cached parse results)
-- ============================================================================

-- Parsed artifact metadata
CREATE TABLE IF NOT EXISTS artifact_metadata (
    artifact_id INTEGER PRIMARY KEY AUTOINCREMENT,
    artifact_path VARCHAR(512) UNIQUE NOT NULL,
    filename VARCHAR(255) NOT NULL,
    ata_root VARCHAR(10),
    project VARCHAR(50),
    program VARCHAR(50),
    family VARCHAR(50),
    variant VARCHAR(50),
    version VARCHAR(50),
    model VARCHAR(10),
    block VARCHAR(50),
    phase VARCHAR(20),
    knot_task VARCHAR(20),
    aor VARCHAR(20),
    subject VARCHAR(255),
    type VARCHAR(50),
    issue_revision VARCHAR(20),
    status VARCHAR(50),
    extension VARCHAR(20),
    file_sha256 VARCHAR(64),
    last_parsed TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    parse_valid BOOLEAN DEFAULT TRUE,
    parse_errors JSON
);

CREATE INDEX idx_artifact_path ON artifact_metadata(artifact_path);
CREATE INDEX idx_artifact_ata_root ON artifact_metadata(ata_root);
CREATE INDEX idx_artifact_aor ON artifact_metadata(aor);
CREATE INDEX idx_artifact_type ON artifact_metadata(type);
CREATE INDEX idx_artifact_status ON artifact_metadata(status);

-- ============================================================================
-- SECTION H: Link Integrity Tracking (for GATE-LINK-001 / KI-PR3-001)
-- ============================================================================

-- Link integrity records
CREATE TABLE IF NOT EXISTS link_integrity (
    link_id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_path VARCHAR(512) NOT NULL,
    target_link VARCHAR(512) NOT NULL,
    target_resolved_path VARCHAR(512),
    link_type VARCHAR(50) DEFAULT 'INTERNAL' CHECK (link_type IN ('INTERNAL', 'EXTERNAL', 'ANCHOR', 'RELATIVE')),
    broken BOOLEAN DEFAULT FALSE,
    fixable BOOLEAN DEFAULT FALSE,
    suggested_fix VARCHAR(512),
    last_checked TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fix_applied BOOLEAN DEFAULT FALSE,
    fix_applied_at TIMESTAMP
);

CREATE INDEX idx_link_source ON link_integrity(source_path);
CREATE INDEX idx_link_broken ON link_integrity(broken) WHERE broken = TRUE;
CREATE INDEX idx_link_fixable ON link_integrity(fixable) WHERE fixable = TRUE AND fix_applied = FALSE;

-- ============================================================================
-- INITIAL SEED DATA
-- ============================================================================

-- Seed gate definitions
INSERT OR IGNORE INTO gate (gate_code, gate_name, description, owner_aor, default_severity, mode_pr3, script_entrypoint, rung_id, implementation_status) VALUES
('GATE-001', 'Nomenclature Validation', 'Validates all files against v6.0 standard', 'CM', 'BLOCK', 'BLOCK', 'validate_nomenclature.py', 1, 'ACTIVE'),
('GATE-002', 'Schema Registration Check', 'Verifies schema refs exist in ATA 91', 'DATA', 'BLOCK', 'BLOCK', 'scripts/validate_schema_registry.py', 1, 'ACTIVE'),
('GATE-003', 'Trace Link Integrity', 'Validates trace link targets exist', 'DATA', 'BLOCK', 'BLOCK', 'scripts/validate_trace_links.py', 4, 'ACTIVE'),
('GATE-004', 'Namespace Deduplication', 'Prevents duplicate IDs across namespaces', 'DATA', 'BLOCK', 'BLOCK', 'scripts/check_ata99_registry.py', 1, 'PLANNED'),
('GATE-005', 'Identifier Grammar Check', 'Validates canonical ID format', 'SE', 'BLOCK', 'BLOCK', 'scripts/validate_identifiers.py', 2, 'PLANNED'),
('GATE-006', 'Governance Change Detection', 'Auto-labels PRs requiring CM review', 'CM', 'WARN', 'WARN', 'Built into governance-gates.yml', NULL, 'ACTIVE'),
('GATE-007', 'Breaking Schema Detection', 'Requires migration plan for breaking changes', 'DATA', 'BLOCK', 'BLOCK', 'scripts/detect_schema_breaking_changes.py', 3, 'PLANNED'),
('GATE-008', 'Evidence Link Validation', 'Checks evidence pack integrity', 'CERT', 'WARN', 'WARN', 'scripts/validate_evidence_links.py', 4, 'PLANNED'),
('GATE-LINK-001', 'Link Integrity Check', 'Validates internal links in Markdown files', 'CM', 'BLOCK', 'BLOCK', 'scripts/check_and_update_links.py', 4, 'PLANNED');

-- Seed identifier grammar definitions
INSERT OR IGNORE INTO identifier_grammar (identifier_kind, description, regex_pattern, owner_aor) VALUES
('am_id', 'AMPEL360 Master Identifier', '^AM-[A-Z]{2,4}-[0-9]{4,6}$', 'CM'),
('teknia_id', 'TEKNIA Credential Identifier', '^TEK-[A-Z]{3,5}-[0-9]{6}$', 'CERT'),
('schema_id', 'Schema Registry Identifier', '^SCH-ATA[0-9]{2,3}-[A-Z0-9-]+$', 'DATA'),
('trace_id', 'Trace Link Identifier', '^TR-[A-Z]{2,4}-[0-9]{4}$', 'SE'),
('namespace_id', 'Namespace Identifier', '^NS-ATA[0-9]{2,3}-[A-Z0-9-]+$', 'DATA');

-- Seed clusters
INSERT OR IGNORE INTO cluster (cluster_id, cluster_name, description, owner_aor) VALUES
('CERT_EVIDENCE', 'Certification Evidence', 'Artifacts requiring certification evidence', 'CERT'),
('TEST_SIM', 'Test & Simulation', 'Test and simulation artifacts', 'TEST'),
('DATA_AI', 'Data & AI Systems', 'Data governance and AI/ML artifacts', 'AI'),
('CM_BASELINES', 'Configuration Baselines', 'Baseline-controlled artifacts', 'CM');

-- Seed cluster membership rules
INSERT OR IGNORE INTO cluster_membership_rule (cluster_id, rule_type, rule_operator, rule_values) VALUES
('CERT_EVIDENCE', 'AOR', 'IN', '["CERT", "SAF"]'),
('CERT_EVIDENCE', 'TYPE', 'IN', '["FHA", "PSSA", "SSA", "FTA", "PLAN"]'),
('TEST_SIM', 'BLOCK', 'IN', '["TEST", "SYS"]'),
('TEST_SIM', 'ATA_RANGE', 'RANGE', '{"min": 100, "max": 114}'),
('DATA_AI', 'BLOCK', 'IN', '["AI", "DATA"]'),
('DATA_AI', 'ATA_RANGE', 'RANGE', '{"min": 95, "max": 98}'),
('CM_BASELINES', 'STATUS', 'IN', '["APPROVED", "RELEASED"]'),
('CM_BASELINES', 'VARIANT', 'IN', '["BASELINE", "CERT"]');

-- ============================================================================
-- VIEWS FOR REPORTING
-- ============================================================================

-- Gate execution summary view
CREATE VIEW IF NOT EXISTS v_gate_execution_summary AS
SELECT 
    g.gate_code,
    g.gate_name,
    g.implementation_status,
    COUNT(gr.run_id) as total_runs,
    SUM(CASE WHEN gr.passed THEN 1 ELSE 0 END) as passed_runs,
    SUM(CASE WHEN NOT gr.passed THEN 1 ELSE 0 END) as failed_runs,
    MAX(gr.run_timestamp) as last_run_timestamp,
    AVG(gr.execution_time_ms) as avg_execution_time_ms
FROM gate g
LEFT JOIN gate_run gr ON g.gate_code = gr.gate_code
GROUP BY g.gate_code, g.gate_name, g.implementation_status;

-- Unresolved findings view
CREATE VIEW IF NOT EXISTS v_unresolved_findings AS
SELECT 
    gf.gate_code,
    g.gate_name,
    gf.severity,
    gf.artifact_path,
    gf.message,
    gf.created_at,
    gr.git_sha,
    gr.pr_number
FROM gate_finding gf
JOIN gate_run gr ON gf.run_id = gr.run_id
JOIN gate g ON gf.gate_code = g.gate_code
WHERE gr.run_id = (
    SELECT MAX(run_id) FROM gate_run WHERE gate_code = gf.gate_code
)
AND NOT gr.passed
ORDER BY gf.severity, gf.created_at DESC;

-- Broken links view
CREATE VIEW IF NOT EXISTS v_broken_links AS
SELECT 
    source_path,
    target_link,
    target_resolved_path,
    fixable,
    suggested_fix,
    last_checked
FROM link_integrity
WHERE broken = TRUE AND fix_applied = FALSE
ORDER BY fixable DESC, source_path;

-- Schema breaking changes view
CREATE VIEW IF NOT EXISTS v_schema_breaking_changes AS
SELECT 
    sce.schema_id,
    sce.from_version,
    sce.to_version,
    sce.breaking_score,
    sce.breaking_reasons,
    sce.detected_at,
    sce.reviewed
FROM schema_change_event sce
WHERE sce.breaking_score > 0 AND NOT sce.reviewed
ORDER BY sce.breaking_score DESC, sce.detected_at DESC;
