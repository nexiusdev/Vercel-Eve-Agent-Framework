# nexiuslabs-skill-library

A monorepo for NexiusLabs agent skills and optional role→skill mappings.

## Layout

```
nexiuslabs-skill-library/
  skills/
    <skill_id>/
      SKILL.md
      metadata.json
      bin/
      assets/
      templates/
  roles/
    role_sales.json
    role_support.json
  README.md
```

## Conventions

- `skills/<skill_id>/` folder name must match the skill id.
- Every skill includes a `SKILL.md` and (recommended) `metadata.json`.
- `roles/` contains repo-side mapping files for reference.

## Adding a new skill

1. Create `skills/<skill_id>/`
2. Add `SKILL.md`, `metadata.json`
3. Implement entry script in `bin/`

## Git Author

Commits in this repo are authored as `henry@nexiuslabs.com`.
