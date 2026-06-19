#!/usr/bin/env python3
"""Create an Eve-inspired Codex agent folder contract."""

from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path


def write(path: Path, content: str, force: bool) -> bool:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and not force:
        return False
    path.write_text(content.strip() + "\n", encoding="utf-8")
    return True


def touch(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.touch(exist_ok=True)


def slug(value: str) -> str:
    return "".join(ch.lower() if ch.isalnum() else "-" for ch in value).strip("-")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", required=True, help="Project directory to scaffold.")
    parser.add_argument("--project-name", default=None)
    parser.add_argument("--owner", default="TODO")
    parser.add_argument("--subagents", default="")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    root = Path(args.target).expanduser().resolve()
    root.mkdir(parents=True, exist_ok=True)
    project_name = args.project_name or root.name
    project_slug = slug(project_name) or "project"
    today = datetime.now().strftime("%Y-%m-%d")
    subagents = [item.strip() for item in args.subagents.split(",") if item.strip()]

    created: list[str] = []
    skipped: list[str] = []

    def record(path: Path, content: str) -> None:
        if write(path, content, args.force):
            created.append(str(path.relative_to(root)))
        else:
            skipped.append(str(path.relative_to(root)))

    record(
        root / "AGENTS.md",
        f"""
# Project Agent Contract

This repository uses an Eve-inspired "agent as a directory" contract. The
agent operating model lives in `agent/` so it is explicit, inspectable, and
maintainable by Codex.

Any AI coding agent must read `agent/instructions.md` before work, check
`agent/approvals/human-gates.yaml` before risky actions, record evidence under
`agent/evidence/` after meaningful changes, record run notes under
`agent/runs/`, and update `agent/learning.md` with reusable lessons.

Human approval is required for production deploys, external publishing,
credential changes, destructive file or data operations, customer-impacting
changes, financial/trading/payment actions, and risky dependency upgrades.
""",
    )
    record(root / ".codex" / "instructions.md", "Read `AGENTS.md` and `agent/instructions.md` before work.")
    record(
        root / "agent" / "agent.yaml",
        f"""
name: {project_slug}-agent
purpose: Maintain an Eve-inspired agent-as-directory contract for this project.
owner: {args.owner}
primary_agent: Codex
project_type: TODO
repository_path: "{root}"
autonomy_level: supervised
default_model_policy:
  prefer: capable coding model
  allow_model_switching: true
allowed_surfaces:
  - filesystem
  - local_shell
  - git
workspace_policy:
  subagent_workspace_pattern: agent/subagents/<name>/workspace
  shared_workspace: agent/workspaces/shared
  default_rule: Subagents write only inside their own workspace unless approved.
  enforcement: documented_boundary_only
evidence_required: true
approval_policy:
  source: agent/approvals/human-gates.yaml
  default: ask_before_risky_or_external_actions
created_at: {today}
""",
    )
    record(
        root / "agent" / "instructions.md",
        """
# Agent Instructions

## Mission

Maintain this project safely using the Eve-inspired agent folder contract.

## Responsibilities

- Inspect the repository before editing.
- Preserve user work and existing project-specific instructions.
- Keep changes scoped to the request.
- Prefer real project commands over guesses.
- Record evidence and run notes after meaningful work.
- Update `agent/learning.md` with reusable lessons.

## Boundaries

- Do not install the real Eve runtime unless explicitly approved.
- Do not modify source code unless required by the task.
- Treat each subagent `workspace/` as its default sandbox.
- Ask before deploys, external publishing, credential changes, destructive
  operations, customer-impacting changes, financial actions, or risky upgrades.

## Default Working Loop

1. Read the relevant agent contract files.
2. Inspect repository structure and current state.
3. Identify commands, conventions, and risks.
4. Make the smallest useful change.
5. Verify with available project commands.
6. Record evidence and run notes.
7. Summarize changes, verification, TODOs, and risks.
""",
    )
    record(
        root / "agent" / "tools" / "README.md",
        """
# Project-Local Tools

## Package Manager

TODO

## Test Command

TODO

## Build Command

TODO

## Lint or Typecheck Command

TODO

## Git Commands

```text
git status --short
git diff --stat
git diff
```
""",
    )
    record(
        root / "agent" / "skills" / "README.md",
        """
# Reusable Project Knowledge

## Project Architecture

TODO

## Coding Conventions

TODO

## Testing Conventions

TODO

## Deployment Conventions

TODO

## Known Pitfalls

- Do not install or depend on the real Eve runtime without explicit approval.
""",
    )
    record(root / "agent" / "schedules" / "README.md", "# Schedules\n\nNo schedules are currently registered.")
    record(
        root / "agent" / "approvals" / "human-gates.yaml",
        """
approval_gates:
  production_deployment:
    requires_human_approval: true
  external_publishing_or_messaging:
    requires_human_approval: true
  credential_or_secret_changes:
    requires_human_approval: true
  destructive_file_or_data_operations:
    requires_human_approval: true
  customer_facing_behavior_changes:
    requires_human_approval: true
  financial_trading_or_payment_actions:
    requires_human_approval: true
  dependency_upgrades_with_security_or_breaking_change_risk:
    requires_human_approval: true
default_policy:
  when_uncertain: ask_for_human_approval
  record_decisions_in: agent/runs/
""",
    )
    record(
        root / "agent" / "evidence" / "README.md",
        """
# Evidence

Use `YYYY-MM-DD-short-task-name.md`.

Template:

- task
- summary
- files changed
- commands run
- verification result
- screenshots/artifacts if applicable
- unresolved risks
""",
    )
    record(
        root / "agent" / "runs" / "README.md",
        """
# Run Notes

Use `YYYY-MM-DD-HHMM-run.md`.

Template:

- trigger
- objective
- actions taken
- result
- next action
- blocked status
""",
    )
    record(
        root / "agent" / "subagents" / "README.md",
        """
# Subagents

Each subagent should be a directory with `agent.yaml`, `instructions.md`,
`sandbox.yaml`, and `workspace/`.

The workspace should contain:

- `inbox/`
- `working/`
- `outputs/`
- `evidence/`

This is a documented sandbox boundary only. Hard enforcement requires a runner,
filesystem permissions, containers, or an approved runtime.
""",
    )
    record(
        root / "agent" / "workspaces" / "shared" / "README.md",
        """
# Shared Agent Workspace

Use this folder only for intentional cross-agent handoffs and shared artifacts.
""",
    )
    record(
        root / "agent" / "learning.md",
        """
# Learning Log

## Recurring Issues

- TODO

## Stable Project Conventions

- This project uses an Eve-inspired agent folder contract under `agent/`.

## Useful Commands

- TODO

## Things Not To Repeat

- Do not invent commands before inspecting the project.

## Open Questions

- TODO
""",
    )

    for folder in [
        root / "src",
        root / "agent" / "workspaces" / "shared" / "handoffs",
        root / "agent" / "workspaces" / "shared" / "artifacts",
    ]:
        touch(folder / ".gitkeep")

    for name in subagents:
        base = root / "agent" / "subagents" / slug(name)
        record(
            base / "agent.yaml",
            f"""
name: {slug(name)}
role: TODO
status: placeholder
workspace_root: agent/subagents/{slug(name)}/workspace
sandbox_policy: agent/subagents/{slug(name)}/sandbox.yaml
""",
        )
        record(base / "instructions.md", f"# {name} Instructions\n\nWrite only inside your workspace unless approved.")
        record(
            base / "sandbox.yaml",
            f"""
sandbox:
  type: documented_filesystem_boundary
  workspace_root: agent/subagents/{slug(name)}/workspace
  can_write:
    - agent/subagents/{slug(name)}/workspace/**
  requires_approval_for:
    - writing_outside_workspace
    - destructive_operations
    - external_publishing_or_messaging
    - credential_or_secret_changes
  enforcement_note: This documents intent but does not enforce permissions by itself.
""",
        )
        record(
            base / "workspace" / "README.md",
            f"# {name} Workspace\n\nDefault rule: write only inside this workspace unless explicitly approved.",
        )
        for folder_name in ["inbox", "working", "outputs", "evidence"]:
            touch(base / "workspace" / folder_name / ".gitkeep")

    print("Created or updated:")
    for item in created:
        print(f"  + {item}")
    if skipped:
        print("Skipped existing files:")
        for item in skipped:
            print(f"  = {item}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
