#!/usr/bin/env python3
"""
AMPEL360 Space-T PLC Database Module
====================================
Version: 1.0
Date: 2025-12-17
Standard: Nomenclature Standard v6.0 R1.0

Provides database operations for PLC gate tracking and ontology database.

Usage:
    from scripts.plc_db import PLCDatabase
    
    db = PLCDatabase()
    db.initialize_database()
    run_id = db.record_gate_run('GATE-001', passed=True, error_count=0)
"""

import json
import sqlite3
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple
from datetime import datetime
from contextlib import contextmanager


class PLCDatabase:
    """
    Database interface for PLC gate tracking and ontology.
    
    Uses SQLite for local-first development with option to upgrade
    to PostgreSQL for production.
    """
    
    def __init__(self, db_path: str = "plc_ontology.db"):
        """
        Initialize PLC database connection.
        
        Args:
            db_path: Path to SQLite database file
        """
        self.db_path = db_path
        self.schema_path = Path(__file__).parent.parent / "config" / "database" / "plc_ontology_schema.sql"
        
    @contextmanager
    def get_connection(self):
        """Context manager for database connections."""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        try:
            yield conn
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            conn.close()
    
    def initialize_database(self) -> None:
        """Initialize database schema from SQL file."""
        if not self.schema_path.exists():
            raise FileNotFoundError(f"Schema file not found: {self.schema_path}")
        
        with self.get_connection() as conn:
            cursor = conn.cursor()
            schema_sql = self.schema_path.read_text()
            cursor.executescript(schema_sql)
        
        print(f"✓ Database initialized: {self.db_path}")
    
    # ========================================================================
    # Gate Management
    # ========================================================================
    
    def get_gate(self, gate_code: str) -> Optional[Dict[str, Any]]:
        """Get gate definition by code."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM gate WHERE gate_code = ?", (gate_code,))
            row = cursor.fetchone()
            return dict(row) if row else None
    
    def get_all_gates(self, implementation_status: Optional[str] = None) -> List[Dict[str, Any]]:
        """Get all gate definitions, optionally filtered by status."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            if implementation_status:
                cursor.execute(
                    "SELECT * FROM gate WHERE implementation_status = ? ORDER BY gate_code",
                    (implementation_status,)
                )
            else:
                cursor.execute("SELECT * FROM gate ORDER BY gate_code")
            return [dict(row) for row in cursor.fetchall()]
    
    def record_gate_run(
        self,
        gate_code: str,
        passed: bool,
        error_count: int = 0,
        warning_count: int = 0,
        info_count: int = 0,
        git_ref: Optional[str] = None,
        git_sha: Optional[str] = None,
        pr_number: Optional[int] = None,
        branch_name: Optional[str] = None,
        execution_time_ms: Optional[int] = None,
        metadata: Optional[Dict] = None
    ) -> int:
        """
        Record a gate execution run.
        
        Returns:
            run_id of the created record
        """
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO gate_run 
                (gate_code, passed, error_count, warning_count, info_count,
                 git_ref, git_sha, pr_number, branch_name, execution_time_ms, metadata)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                gate_code, passed, error_count, warning_count, info_count,
                git_ref, git_sha, pr_number, branch_name, execution_time_ms,
                json.dumps(metadata) if metadata else None
            ))
            return cursor.lastrowid
    
    def record_gate_finding(
        self,
        run_id: int,
        gate_code: str,
        severity: str,
        message: str,
        artifact_path: Optional[str] = None,
        artifact_id: Optional[str] = None,
        finding_code: Optional[str] = None,
        details: Optional[Dict] = None,
        line_number: Optional[int] = None
    ) -> int:
        """
        Record a gate finding.
        
        Returns:
            finding_id of the created record
        """
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO gate_finding
                (run_id, gate_code, severity, message, artifact_path, artifact_id,
                 finding_code, details, line_number)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                run_id, gate_code, severity, message, artifact_path, artifact_id,
                finding_code, json.dumps(details) if details else None, line_number
            ))
            return cursor.lastrowid
    
    def get_gate_execution_summary(self) -> List[Dict[str, Any]]:
        """Get summary of all gate executions."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM v_gate_execution_summary")
            return [dict(row) for row in cursor.fetchall()]
    
    def get_unresolved_findings(self, gate_code: Optional[str] = None) -> List[Dict[str, Any]]:
        """Get unresolved findings from latest runs."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            if gate_code:
                cursor.execute(
                    "SELECT * FROM v_unresolved_findings WHERE gate_code = ?",
                    (gate_code,)
                )
            else:
                cursor.execute("SELECT * FROM v_unresolved_findings")
            return [dict(row) for row in cursor.fetchall()]
    
    # ========================================================================
    # Link Integrity (GATE-LINK-001 / KI-PR3-001)
    # ========================================================================
    
    def record_broken_link(
        self,
        source_path: str,
        target_link: str,
        target_resolved_path: Optional[str] = None,
        link_type: str = 'INTERNAL',
        fixable: bool = False,
        suggested_fix: Optional[str] = None
    ) -> int:
        """Record a broken link."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO link_integrity
                (source_path, target_link, target_resolved_path, link_type,
                 broken, fixable, suggested_fix)
                VALUES (?, ?, ?, ?, TRUE, ?, ?)
            """, (source_path, target_link, target_resolved_path, link_type,
                  fixable, suggested_fix))
            return cursor.lastrowid
    
    def get_broken_links(self, fixable_only: bool = False) -> List[Dict[str, Any]]:
        """Get all broken links."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            if fixable_only:
                cursor.execute(
                    "SELECT * FROM v_broken_links WHERE fixable = TRUE"
                )
            else:
                cursor.execute("SELECT * FROM v_broken_links")
            return [dict(row) for row in cursor.fetchall()]
    
    def mark_link_fixed(self, link_id: int) -> None:
        """Mark a broken link as fixed."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE link_integrity
                SET fix_applied = TRUE, fix_applied_at = CURRENT_TIMESTAMP
                WHERE link_id = ?
            """, (link_id,))
    
    def clear_link_integrity_records(self) -> int:
        """Clear all link integrity records. Returns number of records deleted."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM link_integrity")
            return cursor.rowcount
    
    # ========================================================================
    # Namespace Registry (GATE-004)
    # ========================================================================
    
    def register_namespace(
        self,
        namespace_id: str,
        namespace_type: str,
        owner_aor: str,
        artifact_path: str,
        scope: Optional[str] = None,
        artifact_sha256: Optional[str] = None,
        description: Optional[str] = None
    ) -> None:
        """Register a namespace identifier."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT OR REPLACE INTO namespace_registry
                (namespace_id, namespace_type, scope, owner_aor, artifact_path,
                 artifact_sha256, description)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (namespace_id, namespace_type, scope, owner_aor, artifact_path,
                  artifact_sha256, description))
    
    def check_namespace_duplicates(self) -> List[Dict[str, Any]]:
        """Check for duplicate namespace IDs."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT namespace_id, COUNT(*) as count,
                       GROUP_CONCAT(artifact_path, ', ') as paths
                FROM namespace_registry
                GROUP BY namespace_id
                HAVING count > 1
            """)
            return [dict(row) for row in cursor.fetchall()]
    
    def record_namespace_conflict(
        self,
        namespace_id: str,
        artifact_path_1: str,
        artifact_path_2: str,
        conflict_type: str
    ) -> int:
        """Record a namespace conflict."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO namespace_conflict
                (namespace_id, artifact_path_1, artifact_path_2, conflict_type)
                VALUES (?, ?, ?, ?)
            """, (namespace_id, artifact_path_1, artifact_path_2, conflict_type))
            return cursor.lastrowid
    
    # ========================================================================
    # Identifier Grammar (GATE-005)
    # ========================================================================
    
    def get_identifier_grammar(self, identifier_kind: str) -> Optional[Dict[str, Any]]:
        """Get identifier grammar definition."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM identifier_grammar WHERE identifier_kind = ?",
                (identifier_kind,)
            )
            row = cursor.fetchone()
            return dict(row) if row else None
    
    def record_identifier_instance(
        self,
        identifier_kind: str,
        identifier_value: str,
        artifact_path: str,
        valid: bool,
        artifact_line: Optional[int] = None,
        context: Optional[Dict] = None,
        validation_errors: Optional[List[str]] = None
    ) -> int:
        """Record an identifier instance."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO identifier_instance
                (identifier_kind, identifier_value, artifact_path, artifact_line,
                 context, valid, validation_errors)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                identifier_kind, identifier_value, artifact_path, artifact_line,
                json.dumps(context) if context else None, valid,
                json.dumps(validation_errors) if validation_errors else None
            ))
            return cursor.lastrowid
    
    def get_invalid_identifiers(
        self,
        identifier_kind: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """Get invalid identifier instances."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            if identifier_kind:
                cursor.execute("""
                    SELECT * FROM identifier_instance
                    WHERE valid = FALSE AND identifier_kind = ?
                    ORDER BY artifact_path, artifact_line
                """, (identifier_kind,))
            else:
                cursor.execute("""
                    SELECT * FROM identifier_instance
                    WHERE valid = FALSE
                    ORDER BY identifier_kind, artifact_path, artifact_line
                """)
            return [dict(row) for row in cursor.fetchall()]
    
    # ========================================================================
    # Schema Registry (GATE-007)
    # ========================================================================
    
    def register_schema(
        self,
        schema_id: str,
        version: str,
        artifact_path: str,
        artifact_sha256: str,
        owner_aor: str,
        schema_content: Optional[Dict] = None
    ) -> None:
        """Register a schema version."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT OR REPLACE INTO schema_registry
                (schema_id, version, artifact_path, artifact_sha256, owner_aor,
                 schema_content)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                schema_id, version, artifact_path, artifact_sha256, owner_aor,
                json.dumps(schema_content) if schema_content else None
            ))
    
    def record_schema_change(
        self,
        schema_id: str,
        from_version: str,
        to_version: str,
        from_sha256: str,
        to_sha256: str,
        breaking_score: int,
        breaking_reasons: Optional[List[str]] = None,
        change_type: Optional[str] = None
    ) -> int:
        """Record a schema change event."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO schema_change_event
                (schema_id, from_version, to_version, from_sha256, to_sha256,
                 breaking_score, breaking_reasons, change_type)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                schema_id, from_version, to_version, from_sha256, to_sha256,
                breaking_score, json.dumps(breaking_reasons) if breaking_reasons else None,
                change_type
            ))
            return cursor.lastrowid
    
    def get_breaking_schema_changes(self) -> List[Dict[str, Any]]:
        """Get unreviewed breaking schema changes."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM v_schema_breaking_changes")
            return [dict(row) for row in cursor.fetchall()]
    
    # ========================================================================
    # Evidence Graph (GATE-008)
    # ========================================================================
    
    def record_evidence_ref(
        self,
        source_artifact_id: str,
        source_artifact_path: str,
        evidence_kind: str,
        target_path: Optional[str] = None,
        target_artifact_id: Optional[str] = None,
        required: bool = False
    ) -> int:
        """Record an evidence reference."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO evidence_ref
                (source_artifact_id, source_artifact_path, target_path,
                 target_artifact_id, evidence_kind, required)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                source_artifact_id, source_artifact_path, target_path,
                target_artifact_id, evidence_kind, required
            ))
            return cursor.lastrowid
    
    def update_evidence_resolution(
        self,
        evidence_id: int,
        resolved: bool,
        resolved_path: Optional[str] = None,
        hash_match: Optional[bool] = None,
        commit_ref_match: Optional[bool] = None,
        validation_errors: Optional[List[str]] = None
    ) -> None:
        """Update evidence resolution status."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            
            # Update evidence_ref
            cursor.execute("""
                UPDATE evidence_ref
                SET resolved = ?, updated_at = CURRENT_TIMESTAMP
                WHERE evidence_id = ?
            """, (resolved, evidence_id))
            
            # Insert resolution record
            cursor.execute("""
                INSERT INTO evidence_resolution
                (evidence_id, resolved_path, hash_match, commit_ref_match,
                 validation_errors)
                VALUES (?, ?, ?, ?, ?)
            """, (
                evidence_id, resolved_path, hash_match, commit_ref_match,
                json.dumps(validation_errors) if validation_errors else None
            ))
    
    def get_unresolved_evidence(self, required_only: bool = False) -> List[Dict[str, Any]]:
        """Get unresolved evidence references."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            if required_only:
                cursor.execute("""
                    SELECT * FROM evidence_ref
                    WHERE resolved = FALSE AND required = TRUE
                    ORDER BY source_artifact_path
                """)
            else:
                cursor.execute("""
                    SELECT * FROM evidence_ref
                    WHERE resolved = FALSE
                    ORDER BY required DESC, source_artifact_path
                """)
            return [dict(row) for row in cursor.fetchall()]
    
    # ========================================================================
    # Artifact Metadata
    # ========================================================================
    
    def cache_artifact_metadata(
        self,
        artifact_path: str,
        filename: str,
        parsed_fields: Dict[str, str],
        file_sha256: Optional[str] = None,
        parse_valid: bool = True,
        parse_errors: Optional[List[str]] = None
    ) -> None:
        """Cache parsed artifact metadata."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT OR REPLACE INTO artifact_metadata
                (artifact_path, filename, ata_root, project, program, family,
                 variant, version, model, block, phase, knot_task, aor, subject,
                 type, issue_revision, status, extension, file_sha256,
                 parse_valid, parse_errors, last_parsed)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
            """, (
                artifact_path, filename,
                parsed_fields.get('ata_root'),
                parsed_fields.get('project'),
                parsed_fields.get('program'),
                parsed_fields.get('family'),
                parsed_fields.get('variant'),
                parsed_fields.get('version'),
                parsed_fields.get('model'),
                parsed_fields.get('block'),
                parsed_fields.get('phase'),
                parsed_fields.get('knot_task'),
                parsed_fields.get('aor'),
                parsed_fields.get('subject'),
                parsed_fields.get('type'),
                parsed_fields.get('issue_revision'),
                parsed_fields.get('status'),
                parsed_fields.get('ext'),
                file_sha256,
                parse_valid,
                json.dumps(parse_errors) if parse_errors else None
            ))
    
    def get_artifacts_by_criteria(
        self,
        aor: Optional[str] = None,
        block: Optional[str] = None,
        type_code: Optional[str] = None,
        status: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """Query artifacts by criteria."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            
            query = "SELECT * FROM artifact_metadata WHERE 1=1"
            params = []
            
            if aor:
                query += " AND aor = ?"
                params.append(aor)
            if block:
                query += " AND block = ?"
                params.append(block)
            if type_code:
                query += " AND type = ?"
                params.append(type_code)
            if status:
                query += " AND status = ?"
                params.append(status)
            
            query += " ORDER BY artifact_path"
            
            cursor.execute(query, params)
            return [dict(row) for row in cursor.fetchall()]


def main():
    """Test database initialization."""
    import sys
    
    db = PLCDatabase("test_plc_ontology.db")
    
    try:
        db.initialize_database()
        
        # Test gate queries
        gates = db.get_all_gates()
        print(f"\nGates defined: {len(gates)}")
        for gate in gates:
            print(f"  - {gate['gate_code']}: {gate['gate_name']} ({gate['implementation_status']})")
        
        # Test identifier grammar
        am_id_grammar = db.get_identifier_grammar('am_id')
        if am_id_grammar:
            print(f"\nAM ID Grammar: {am_id_grammar['regex_pattern']}")
        
        print("\n✅ Database test successful")
        return 0
        
    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return 1


if __name__ == '__main__':
    import sys
    sys.exit(main())
