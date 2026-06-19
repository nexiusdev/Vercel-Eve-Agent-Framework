# Eve Filesystem Layout Reference

Use this as a lightweight reference for folder-only scaffolds inspired by
`vercel/eve`.

The Vercel Eve repository describes Eve as a filesystem-first framework for
durable AI agents. Its README says core agent capabilities live in conventional
locations so projects are easier to inspect, extend, and operate.

Canonical Eve-style locations include:

- `agent/agent.ts`: optional model and runtime config.
- `agent/instructions.md`: required always-on system prompt.
- `agent/tools/`: optional typed functions the model can call.
- `agent/skills/`: optional procedures or knowledge loaded on demand.
- `agent/channels/`: optional message channels such as HTTP, Slack, or Discord.
- `agent/schedules/`: optional recurring cron jobs.

For Codex folder-only projects, mirror the idea without installing Eve:

- Use `agent/agent.yaml` instead of `agent.ts` for inspectable metadata.
- Use Markdown READMEs for `tools/`, `skills/`, `schedules/`, `evidence/`,
  `runs/`, and `subagents/`.
- Add `approvals/` for human gates.
- Add `learning.md` for project memory.
- Add per-subagent `workspace/` folders and `sandbox.yaml` files for documented
  sandbox boundaries.

Do not claim hard sandbox enforcement unless a real runtime, permissions model,
or container boundary is configured.
