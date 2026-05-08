# Claude Skill Testing Guide

This guide explains how to test each skill before publishing or packaging it.

## Testing goals

A skill should be tested for:

- Trigger clarity: the description should make it obvious when Claude should use the skill.
- Output consistency: the response should follow the required output format.
- Governance quality: findings should be practical, defensible, and audit-aware.
- Non-invention: the skill should not make up approvals, owners, dates, evidence, or facts.
- Reusability: output should be usable in Jira, Confluence, audit workpapers, or leadership updates.

## Suggested test process

1. Open the skill folder.
2. Copy the contents of `examples/sample-input.md`.
3. Ask Claude to apply the corresponding skill.
4. Compare the output to `examples/sample-output.md`.
5. Confirm the answer identifies blockers, required actions, risk level, and owner questions.

## Minimum pass criteria

A skill passes testing if it produces a clear decision or recommendation, separates blockers from minor improvements, identifies missing evidence or approvals, provides next actions, and avoids unsupported assumptions.
