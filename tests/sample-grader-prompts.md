# Sample Grader Prompts

Use these prompts to manually evaluate generated skill outputs.

## General Grader Prompt

```text
You are evaluating a GRC skill output against an expected governance outcome. Score the response using the 100-point Governance Skill Evaluation Scorecard.

Evaluate the output for:
- Correct decision or recommendation
- Governance gap identification
- Risk and impact analysis
- Evidence and traceability requirements
- Ownership and accountability
- Output usability
- Tone and professional judgment

Return:
1. Total score
2. Score by category
3. Missed issues
4. Strong points
5. Recommended improvements
```

## Change Governance Grader Prompt

```text
Evaluate whether this change governance output correctly identifies CAB readiness, implementation gaps, validation gaps, rollback weaknesses, monitoring requirements, approval gaps, risk level, and next actions.
```

## Audit Evidence Grader Prompt

```text
Evaluate whether this audit evidence review correctly determines audit readiness, identifies evidence gaps, distinguishes primary evidence from supporting context, identifies traceability issues, and recommends remediation before submission.
```

## AI Governance Grader Prompt

```text
Evaluate whether this AI governance intake review correctly identifies third-party AI risk, prompt retention risk, model training concerns, data usage concerns, DPA and AI terms review needs, human review requirements, transparency needs, and approval gates.
```
