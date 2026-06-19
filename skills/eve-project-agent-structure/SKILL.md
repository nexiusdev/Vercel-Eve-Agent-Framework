---
name: eve-project-agent-structure
description: Create Eve-inspired filesystem-first agent folder contracts for new Codex projects. Use when the user wants a new project scaffold, agent-as-directory structure, project agent contract, subagent workspaces, sandbox folders, approvals, evidence, runs, schedules, tools, skills, or AGENTS.md based on Vercel Eve concepts without installing the Eve runtime.
---

# Eve Project Agent Structure

## Purpose

Create a folder-only, Codex-friendly project control plane inspired by Vercel
Eve's filesystem-first agent layout. Do not install or depend on the real Eve
runtime unless the user explicitly asks.

## Reference

When the user asks for details or fidelity to Eve, read
`references/eve-filesystem-layout.md`. It summarizes the relevant Vercel Eve
repo concepts: agent capabilities live in conventional filesystem locations
such as `agent.ts`, `instructions.md`, `tools/`, `skills/`, `channels/`, and
`schedules/`.

## Default Workflow

1. Inspect the target project before writing:
   - Existing `AGENTS.md`
   - Existing `agent/`
   - Package/build/test metadata
   - CI or schedule metadata
2. Create or update the folder contract without touching product source code.
3. Preserve existing project-specific instructions. If `AGENTS.md` exists,
   append a clean agent-contract section instead of replacing it blindly.
4. Include subagent workspaces and documented sandbox policies when useful.
5. Mark unknown commands and owners as `TODO`; do not invent commands.
6. Record evidence and run notes when the target project uses those folders.
7. Do not commit unless the user explicitly asks.

## Recommended Structure

Use this structure for a new project unless the user asks for a smaller one:

```text
AGENTS.md
.codex/
`-- instructions.md
agent/
|-- agent.yaml
|-- instructions.md
|-- learning.md
|-- tools/
|   `-- README.md
|-- skills/
|   `-- README.md
|-- schedules/
|   `-- README.md
|-- approvals/
|   `-- human-gates.yaml
|-- evidence/
|   `-- README.md
|-- runs/
|   `-- README.md
|-- subagents/
|   `-- README.md
`-- workspaces/
    `-- shared/
        |-- README.md
        |-- handoffs/
        `-- artifacts/
src/
```

For named subagents, create:

```text
agent/subagents/<name>/
|-- agent.yaml
|-- instructions.md
|-- sandbox.yaml
`-- workspace/
    |-- README.md
    |-- inbox/
    |-- working/
    |-- outputs/
    `-- evidence/
```

Use `.gitkeep` files inside empty workspace folders when the project is or may
become version-controlled.

## Scripted Creation

For a fresh scaffold, prefer the bundled script:

```powershell
python <skill>/scripts/create_eve_agent_structure.py --target <project-path>
```

Useful options:

```powershell
python <skill>/scripts/create_eve_agent_structure.py --target <project-path> --subagents andrej,enrico,troas
python <skill>/scripts/create_eve_agent_structure.py --target <project-path> --project-name "My Project"
python <skill>/scripts/create_eve_agent_structure.py --target <project-path> --force
```

The script creates missing files and preserves existing files unless `--force`
is passed.

## Required Content

Ensure the scaffold includes:

- `AGENTS.md`: tells agents to read `agent/instructions.md`, check
  `agent/approvals/human-gates.yaml`, record evidence/runs, and require human
  approval for deploys, external publishing, credential changes, destructive
  operations, customer-impacting changes, financial/payment actions, and risky
  dependency upgrades.
- `agent/agent.yaml`: project metadata, owner placeholders, autonomy level,
  allowed surfaces, evidence requirement, approval policy, and workspace policy.
- `agent/instructions.md`: mission, responsibilities, boundaries, working loop,
  verification, evidence, and escalation rules.
- `agent/tools/README.md`: real package/test/build/lint commands when
  inferable; otherwise `TODO`.
- `agent/skills/README.md`: architecture, coding/testing/deployment
  conventions, known pitfalls.
- `agent/schedules/README.md`: recurring jobs or "none registered."
- `agent/approvals/human-gates.yaml`: approval gates.
- `agent/evidence/README.md`: evidence filename convention and template.
- `agent/runs/README.md`: run-note filename convention and template.
- `agent/subagents/README.md`: specialist roles and workspace/sandbox pattern.
- `agent/learning.md`: reusable project memory.

## Sandbox Rule

Represent sandbox boundaries in folders and YAML, but state clearly that this is
a documented boundary only. Hard enforcement requires a runner, filesystem
permissions, containers, or an approved runtime.
