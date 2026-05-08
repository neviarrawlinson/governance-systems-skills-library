# Getting Started

This repository contains practical AI skill packs for Governance Systems Engineering.

The goal is to help GRC practitioners turn governance expectations into repeatable work products, including change reviews, CAB readiness checks, RCA analysis, audit evidence requests, risk register entries, and executive summaries.

## What to Build First

Start with the `change-governance-review` skill because it demonstrates a complete governance workflow:

1. Review a change request.
2. Identify missing or weak control evidence.
3. Determine readiness for CAB.
4. Produce a governance note that can be pasted into a ticket.
5. Recommend the next action.

## Minimum Skill Package

Each skill should include:

- `SKILL.md`
- Optional `references/` folder
- Optional `examples/` folder
- Optional templates or checklists

## Testing Method

Use realistic examples. A good test input should include both strong and weak information so the skill can demonstrate practical judgment.

Suggested test prompt:

```text
Use the change governance review skill to evaluate the change request below. Identify gaps, rate CAB readiness, and write a governance note.
```

## Quality Standard

A good skill should be:

- Specific enough to trigger at the right time
- Clear enough to produce repeatable output
- Practical enough for a real GRC practitioner
- Structured enough to support audit readiness
- Flexible enough to adapt to different organizations
