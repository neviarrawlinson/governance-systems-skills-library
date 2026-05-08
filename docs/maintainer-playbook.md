# Maintainer Playbook

This playbook defines how to maintain the skills library as it grows.

## Add a new skill

1. Create a folder under `skills/` using lowercase letters and hyphens.
2. Add `SKILL.md` with YAML frontmatter.
3. Add `README.md`.
4. Add `examples/sample-input.md`.
5. Add `examples/sample-output.md`.
6. Add `references/checklist.md` if the skill needs a supporting checklist.
7. Update `skills/README.md`.
8. Update `skill-catalog.json`.
9. Run validation.
10. Package the skill.

## Skill naming rules

- Use lowercase letters, numbers, and hyphens.
- Keep names action-oriented and specific.
- Avoid broad framework-only names unless the skill performs a practical workflow.

## Quality standard

Each skill should help a practitioner make a better governance decision, not just generate generic content.
