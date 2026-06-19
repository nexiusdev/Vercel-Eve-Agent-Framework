# Vercel Eve Agent Framework

This repository stores an Eve-inspired Codex skill for creating project agent folder structures.

[Vercel Eve](https://github.com/vercel/eve) is a filesystem-first framework for durable AI agents. Its central idea is that the filesystem is the authoring interface: an agent's behavior, knowledge, tools, channels, and schedules live in predictable folders so the agent is easy to inspect, extend, and operate.

This repository does not install or depend on the Eve runtime. It mirrors the folder concept so Codex projects can use an inspectable agent contract.

## Eve Folder Concept

A typical Eve agent uses this shape:

```text
my-agent/
`-- agent/
    |-- agent.ts
    |-- instructions.md
    |-- tools/
    |   `-- get_weather.ts
    |-- skills/
    |   `-- plan_a_trip.md
    |-- channels/
    |   `-- slack.ts
    `-- schedules/
        `-- weekly_recap.ts
```

## Folder Purposes

| Path | Purpose |
| --- | --- |
| `agent/` | The dedicated agent directory. This is the visible control plane for the agent. |
| `agent/agent.ts` | Optional Eve runtime/model configuration. In this repo's Codex adaptation, this is represented as `agent/agent.yaml`. |
| `agent/instructions.md` | The always-on system prompt: who the agent is, how it should behave, and what rules it must follow. |
| `agent/tools/` | Callable functions the model can use to act on the world, such as API calls, local commands, or typed helper functions. |
| `agent/skills/` | Reusable procedures or knowledge that can be loaded when relevant to a task. |
| `agent/channels/` | Message surfaces where the agent can live, such as HTTP, Slack, Discord, or other integrations. |
| `agent/schedules/` | Recurring jobs and cron-like tasks that let the agent act on a cadence. |

## Codex Folder-Only Adaptation

For Codex projects, this repository uses a documentation/control-plane version of the Eve pattern:

```text
project/
|-- AGENTS.md
|-- .codex/
|   `-- instructions.md
|-- agent/
|   |-- agent.yaml
|   |-- instructions.md
|   |-- learning.md
|   |-- tools/
|   |   `-- README.md
|   |-- skills/
|   |   `-- README.md
|   |-- schedules/
|   |   `-- README.md
|   |-- approvals/
|   |   `-- human-gates.yaml
|   |-- evidence/
|   |   `-- README.md
|   |-- runs/
|   |   `-- README.md
|   |-- subagents/
|   |   `-- README.md
|   `-- workspaces/
|       `-- shared/
|           |-- README.md
|           |-- handoffs/
|           `-- artifacts/
`-- src/
```

## Codex Adaptation Folder Purposes

| Path | Purpose |
| --- | --- |
| `AGENTS.md` | Repository-level instructions for AI coding agents. It points agents to the local contract before they work. |
| `.codex/instructions.md` | Codex-specific startup instructions for this project. |
| `agent/agent.yaml` | Inspectable project agent metadata: name, purpose, owner, autonomy level, allowed surfaces, evidence policy, and workspace policy. |
| `agent/instructions.md` | Operating instructions for the project agent: mission, boundaries, working loop, verification, evidence, and escalation rules. |
| `agent/tools/README.md` | Documents project-local commands and tools, such as package manager, test, build, lint, typecheck, and git commands. |
| `agent/skills/README.md` | Documents reusable project knowledge: architecture, conventions, testing practices, deployment practices, and known pitfalls. |
| `agent/schedules/README.md` | Documents recurring jobs, cron tasks, CI workflows, or automations. |
| `agent/approvals/human-gates.yaml` | Defines actions that require human approval, such as deploys, external publishing, credential changes, destructive operations, customer-impacting changes, and risky dependency upgrades. |
| `agent/evidence/README.md` | Defines how to record proof of meaningful changes, including files changed, commands run, verification results, artifacts, and unresolved risks. |
| `agent/runs/README.md` | Defines how to record operational run notes after completing tasks. |
| `agent/subagents/README.md` | Documents specialist agent roles and the expected per-subagent workspace pattern. |
| `agent/workspaces/shared/` | Shared handoff and artifact area for intentional cross-agent collaboration. |
| `agent/learning.md` | Living project memory for reusable lessons, recurring issues, stable conventions, useful commands, and open questions. |
| `src/` | Application or product source code. The agent contract should stay separate from product code unless explicitly integrated. |

## Subagent Workspace Pattern

Each named subagent can have its own documented workspace and sandbox boundary:

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

| Path | Purpose |
| --- | --- |
| `agent/subagents/<name>/agent.yaml` | Metadata for the specialist agent. |
| `agent/subagents/<name>/instructions.md` | Role-specific instructions for that subagent. |
| `agent/subagents/<name>/sandbox.yaml` | Documents what the subagent may read/write and what requires approval. |
| `workspace/inbox/` | Assigned tasks, prompts, and handoff notes. |
| `workspace/working/` | Scratch work, drafts, analysis, and temporary files. |
| `workspace/outputs/` | Final deliverables from the subagent. |
| `workspace/evidence/` | Verification notes, command summaries, logs, screenshots, and artifacts. |

A folder-only sandbox is inspectable but not self-enforcing. Hard enforcement requires a runner, filesystem permissions, containers, or an approved runtime.

## Included Skill

The reusable Codex skill lives here:

```text
skills/eve-project-agent-structure/
|-- SKILL.md
|-- metadata.json
|-- agents/
|   `-- openai.yaml
|-- references/
|   `-- eve-filesystem-layout.md
`-- scripts/
    `-- create_eve_agent_structure.py
```

Use it to scaffold the Codex adaptation of the Eve folder pattern in a new project.
