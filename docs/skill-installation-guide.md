# Skill Installation Guide

This project is designed around Claude-compatible skills. Each skill is organized as a folder that contains a `SKILL.md` file.

## Basic Skill Structure

```text
skill-name/
└── SKILL.md
```

The `SKILL.md` file begins with YAML frontmatter:

```markdown
---
name: change-governance-review
description: Reviews change requests for governance completeness, CAB readiness, risk, rollback, validation, monitoring, approvals, and audit readiness.
---
```

## Packaging a Skill

To package one skill:

1. Open the `skills/` folder.
2. Choose the skill folder you want to use.
3. Zip the individual skill folder.
4. Upload or install the zip using the available Claude Skills workflow in your Claude environment.
5. Enable the skill and test it with realistic governance examples.

## Example

```text
skills/change-governance-review/
├── SKILL.md
├── references/
└── examples/
```

Zip the `change-governance-review` folder itself, not the full repository, when uploading a single skill.

## Testing Checklist

Before publishing a skill, confirm that:

- The folder name is lowercase and uses hyphens.
- The `SKILL.md` file exists at the root of the skill folder.
- The YAML frontmatter includes `name` and `description`.
- The description clearly explains when the skill should be used.
- The output format is specific and repeatable.
- The skill does not include confidential company data.
