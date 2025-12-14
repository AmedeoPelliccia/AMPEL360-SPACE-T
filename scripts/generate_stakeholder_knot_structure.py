#!/usr/bin/env python3
"""
AMPEL360 SPACE-T Portal Generator
==================================
Version: 1.0
Date: 2025-12-14

Generates the AMPEL360-SPACE-T-PORTAL stakeholder-centric navigation structure.
This portal organizes work by Stakeholder → Knots → ATAs → Tasks.

Usage:
    python scripts/generate_stakeholder_knot_structure.py [OPTIONS]

Options:
    --repo-root DIR       Repository root path (default: .)
    --config FILE         Config JSON path (default: scripts/stakeholder_knot_config.json)
    --dry-run            Show what would be created without writing files
    --force              Overwrite existing stub files
    --full               Generate per-ATA task stubs (not only tasklists)
"""
from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Any, Tuple

DESC_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")

def slugify(s: str) -> str:
    """Convert string to lowercase kebab-case."""
    s = s.strip().lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-{2,}", "-", s).strip("-")
    return s or "tbd"

def mk_name(root: str, bucket: str, typ: str, lc: str, variant: str, desc: str, ver: str, ext: str) -> str:
    """
    Create filename following nomenclature v2.0 (8-field format).
    
    Format: [ROOT]_[BUCKET]_[TYPE]_[LC_OR_SUBBUCKET]_[VARIANT]_[DESCRIPTION]_[VERSION].[EXT]
    """
    desc = slugify(desc)
    if not DESC_RE.match(desc):
        raise ValueError(f"Bad DESCRIPTION after slugify: {desc}")
    return f"{root}_{bucket}_{typ}_{lc}_{variant}_{desc}_{ver}.{ext}"

def ensure_dir(path: Path, dry: bool) -> None:
    """Create directory if it doesn't exist."""
    if dry:
        print(f"[DRY] mkdir -p {path.as_posix()}")
        return
    path.mkdir(parents=True, exist_ok=True)

def write_file(path: Path, content: str, dry: bool, force: bool) -> None:
    """Write file to path, respecting dry-run and force flags."""
    if path.exists() and not force:
        return
    if dry:
        print(f"[DRY] write {path.as_posix()}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")

def stakeholder_index_md(stk_id: str, stk_name: str, knots: List[Tuple[str, str, Path]]) -> str:
    """Generate stakeholder entry point index markdown."""
    lines = [
        "---",
        f"title: \"Stakeholder Entry Point: {stk_name} ({stk_id})\"",
        "type: IDX",
        "variant: \"SPACET\"",
        "status: Draft",
        f"stakeholder_id: \"{stk_id}\"",
        "---",
        "",
        f"# Stakeholder Entry Point — {stk_name} ({stk_id})",
        "",
        "## Scope",
        "This directory is the stakeholder-centric entry point. Work is organized by **Backlog Knots** (uncertainty knots).",
        "",
        "## Active Backlog Knots",
        ""
    ]
    for kid, title, kpath in knots:
        lines.append(f"- **{kid}** — {title} → `{kpath.name}/`")
    lines += [
        "",
        "## Operating Model",
        "- Each Knot has an **overview**, **ATA impact breakdown**, and **tasks** to close uncertainties.",
        "- Tasks close with **Decision + Evidence**, then a baseline update (CM).",
        ""
    ]
    return "\n".join(lines)

def knot_overview_md(kid: str, title: str, stakeholder_id: str, affected_atas: List[str]) -> str:
    """Generate knot overview markdown."""
    atas = ", ".join([f"ATA {a}" for a in affected_atas])
    return "\n".join([
        "---",
        f"title: \"Backlog Knot {kid}: {title}\"",
        "type: IDX",
        "variant: \"SPACET\"",
        "status: Draft",
        f"knot_id: \"{kid}\"",
        f"stakeholder_id: \"{stakeholder_id}\"",
        f"affected_atas: [{', '.join([f'\"{a}\"' for a in affected_atas])}]",
        "---",
        "",
        f"# Backlog Knot {kid} — {title}",
        "",
        "## Problem Statement",
        "_Define the uncertainty precisely; specify the decision required._",
        "",
        "## Scope Boundary",
        "- In-scope: ...",
        "- Out-of-scope: ...",
        "",
        "## Impacted ATAs",
        f"- {atas}",
        "",
        "## Decision & Closure Criteria",
        "- Decision owner: ...",
        "- Evidence required: ...",
        "- Acceptance criteria: ...",
        "",
        "## Pathways",
        "1) Requirements/ConOps",
        "2) Architecture/ICDs",
        "3) Implementation/Industrialization",
        "4) Verification/Qualification",
        "5) Baseline & Release",
        ""
    ])

def ata_tasklist_md(kid: str, title: str, ata: str) -> str:
    """Generate ATA tasklist markdown."""
    return "\n".join([
        "---",
        f"title: \"{kid} ATA {ata} Tasklist\"",
        "type: IDX",
        "variant: \"SPACET\"",
        "status: Draft",
        f"knot_id: \"{kid}\"",
        f"ata: \"{ata}\"",
        "---",
        "",
        f"# {kid} — {title}",
        f"## ATA {ata} — Tasklist",
        "",
        "## Uncertainty to Resolve (ATA-specific)",
        "- ...",
        "",
        "## Tasks (minimum set)",
        "1. Define ATA-specific scope, interfaces, owners.",
        "2. Define decision criteria and evidence package.",
        "3. Execute validation/verification activities.",
        "4. Record decision; update baseline and trace links.",
        ""
    ])

def task_md(kid: str, ata: str, tid: str, task_title: str, affected_paths: List[str]) -> str:
    """Generate task action item markdown."""
    return "\n".join([
        "---",
        f"title: \"{kid} {tid} — {task_title}\"",
        "type: ACT",
        "variant: \"SPACET\"",
        "status: Draft",
        f"knot_id: \"{kid}\"",
        f"ata: \"{ata}\"",
        f"task_id: \"{tid}\"",
        f"affected_ata_paths: {json.dumps(affected_paths)}",
        "---",
        "",
        f"# {kid} {tid} — {task_title}",
        "",
        "## Objective",
        "_What decision or evidence gap does this task close?_",
        "",
        "## Inputs",
        "- ...",
        "",
        "## Work Steps",
        "- ...",
        "",
        "## Outputs (Evidence)",
        "- ...",
        "",
        "## Closure",
        "- Decision recorded: Yes/No",
        "- Evidence attached/linked: Yes/No",
        "- Baseline updated: Yes/No",
        ""
    ])

@dataclass
class GenParams:
    """Generation parameters."""
    repo_root: Path
    portal_path: Path
    variant: str
    root_code: str
    bucket_code: str
    version: str
    dry_run: bool
    force: bool
    full: bool

def main() -> int:
    """Main entry point."""
    ap = argparse.ArgumentParser(
        description="Generate AMPEL360-SPACE-T-PORTAL stakeholder-centric structure"
    )
    ap.add_argument("--repo-root", default=".", help="Repository root path")
    ap.add_argument("--config", default="scripts/stakeholder_knot_config.json", help="Config JSON path")
    ap.add_argument("--dry-run", action="store_true", help="Show what would be created without writing")
    ap.add_argument("--force", action="store_true", help="Overwrite existing stub files")
    ap.add_argument("--full", action="store_true", help="Generate per-ATA task stubs (not only tasklists)")
    ns = ap.parse_args()

    repo_root = Path(ns.repo_root).resolve()
    cfg_path = (repo_root / ns.config).resolve()
    
    if not cfg_path.exists():
        print(f"Error: Config file not found: {cfg_path}")
        return 1
    
    cfg = json.loads(cfg_path.read_text(encoding="utf-8"))

    params = GenParams(
        repo_root=repo_root,
        portal_path=repo_root / cfg.get("portal_path", "AMPEL360-SPACE-T-PORTAL"),
        variant=cfg.get("variant", "SPACET"),
        root_code=cfg.get("root_code", "00"),
        bucket_code=cfg.get("bucket_code", "00"),
        version=cfg.get("version", "v01"),
        dry_run=ns.dry_run,
        force=ns.force,
        full=ns.full
    )

    ensure_dir(params.portal_path, params.dry_run)

    # Generate global index
    global_index = params.portal_path / mk_name(
        params.root_code, params.bucket_code, "IDX", "LC01", params.variant,
        "stakeholder-entrypoints", params.version, "md"
    )

    # Generate knot register CSV
    knot_register_csv = params.portal_path / mk_name(
        params.root_code, params.bucket_code, "TAB", "LC01", params.variant,
        "knot-register", params.version, "csv"
    )

    stakeholders: List[Dict[str, Any]] = cfg["stakeholders"]
    knots: Dict[str, Any] = cfg["knots"]

    register_rows = ["knot_id,title,stakeholder_id,affected_atas"]
    global_lines = [
        "---",
        "title: \"AMPEL360 SPACE-T Portal — Stakeholder Entry Points\"",
        "type: IDX",
        f"variant: \"{params.variant}\"",
        "status: Draft",
        "---",
        "",
        "# AMPEL360 SPACE-T Portal",
        "",
        "## Stakeholders",
        ""
    ]

    for stk in stakeholders:
        stk_id = stk["id"]
        stk_name = stk["name"]
        stk_slug = slugify(f"{stk_id}-{stk_name}")

        stk_dir = params.portal_path / f"STK_{stk_id}-{stk_slug}"
        ensure_dir(stk_dir, params.dry_run)

        stakeholder_knots = []
        for kid in stk.get("knots", []):
            k = knots[kid]
            k_title = k["title"]
            k_dir = stk_dir / "KNOTS" / f"{kid}_{slugify(k_title)}"
            ensure_dir(k_dir, params.dry_run)

            # Generate knot overview
            knot_overview = k_dir / mk_name(
                params.root_code, params.bucket_code, "IDX", "LC01", params.variant,
                f"{kid}-{k_title}", params.version, "md"
            )
            write_file(
                knot_overview,
                knot_overview_md(kid, k_title, stk_id, k.get("affected_atas", [])),
                params.dry_run, params.force
            )

            # Create ATA_TASKS directory
            ata_tasks_root = k_dir / "ATA_TASKS"
            ensure_dir(ata_tasks_root, params.dry_run)

            # Generate per-ATA directories and tasklists
            affected_atas = k.get("affected_atas", [])
            for ata in affected_atas:
                ata_dir = ata_tasks_root / f"ATA_{ata}"
                ensure_dir(ata_dir, params.dry_run)

                # Generate tasklist
                tasklist = ata_dir / mk_name(
                    params.root_code, params.bucket_code, "IDX", "LC01", params.variant,
                    f"{kid}-ata-{ata}-tasklist", params.version, "md"
                )
                write_file(tasklist, ata_tasklist_md(kid, k_title, ata), params.dry_run, params.force)

                # Generate individual tasks if --full flag is set
                if params.full:
                    for t in k.get("task_templates", []):
                        tid = t["id"]
                        ttitle = t["title"]

                        # These are routing hints to the real engineering tree
                        affected_paths = [
                            f"AMPEL360_SPACE-T/P-PROGRAM/ATA_{ata}-*/{ata}-00_GENERAL/",
                            f"AMPEL360_SPACE-T/O-OPS_ORG/ATA_{ata}-*/",
                            f"AMPEL360_SPACE-T/T-TECHNOLOGY/ATA_{ata}-*/",
                            f"AMPEL360_SPACE-T/I-INFRASTRUCTURES/ATA_{ata}-*/",
                            f"AMPEL360_SPACE-T/N-NEURAL_NETWORKS/ATA_{ata}-*/",
                            f"AMPEL360_SPACE-T/T-SIMTEST/ATA_{ata}-*/"
                        ]

                        task_file = ata_dir / mk_name(
                            params.root_code, params.bucket_code, "ACT", "LC06", params.variant,
                            f"{kid}-{tid}-{ttitle}", params.version, "md"
                        )
                        write_file(task_file, task_md(kid, ata, tid, ttitle, affected_paths), params.dry_run, params.force)

            stakeholder_knots.append((kid, k_title, k_dir))
            register_rows.append(f"{kid},{k_title},{stk_id},\"{';'.join(affected_atas)}\"")

        # Generate stakeholder index
        stk_index = stk_dir / mk_name(
            params.root_code, params.bucket_code, "IDX", "LC01", params.variant,
            f"stakeholder-{stk_id}-entrypoint", params.version, "md"
        )
        write_file(stk_index, stakeholder_index_md(stk_id, stk_name, stakeholder_knots), params.dry_run, params.force)

        rel = stk_index.relative_to(params.portal_path).as_posix()
        global_lines.append(f"- **{stk_id}** — {stk_name} → `{rel}`")

    # Write global index and register
    write_file(global_index, "\n".join(global_lines) + "\n", params.dry_run, params.force)
    write_file(knot_register_csv, "\n".join(register_rows) + "\n", params.dry_run, params.force)

    print("✅ OK: AMPEL360-SPACE-T-PORTAL generated.")
    if params.dry_run:
        print("(Dry-run mode: no files were actually created)")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
