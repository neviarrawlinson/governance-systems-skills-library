# Installation and Usage Guide

This guide explains how to use the Governance Systems Skills Library as a practical Claude-compatible GRC workflow library.

## Purpose

The library is designed to help practitioners apply repeatable governance logic to common GRC workflows, including:

- Change request review
- CAB readiness checks
- RCA quality review
- Audit evidence preparation
- Risk register documentation
- Executive GRC reporting
- Policy exception review
- Third-party risk review
- Control evidence quality review
- Governance metrics reporting
- AI governance intake review

## Skill package structure

Each skill is organized as a folder. The core instruction file is:

```text
SKILL.md
```

A typical skill folder may include:

```text
SKILL.md
README.md
examples/
references/
```

## Using the skills

Use the skill that best matches the workflow you are trying to complete.

| Workflow | Recommended Skill |
|---|---|
| Review a production change request | `change-governance-review` |
| Decide if a change is ready for CAB | `cab-readiness-check` |
| Review an incident RCA | `rca-governance-analysis` |
| Prepare audit evidence response guidance | `audit-evidence-request` |
| Convert a finding into a risk register entry | `risk-register-builder` |
| Summarize governance issues for leadership | `executive-grc-summary` |
| Review a policy exception | `policy-exception-review` |
| Review a SaaS vendor intake | `third-party-risk-review` |
| Check evidence before audit submission | `control-evidence-quality-check` |
| Summarize governance metrics | `governance-metrics-summary` |
| Review an AI use case intake | `ai-governance-intake-review` |

## Recommended usage pattern

1. Select the skill that matches the task.
2. Provide the relevant source material.
3. Ask for a structured output.
4. Review the output for accuracy.
5. Apply professional judgment before using the output in a real governance process.

## Example prompt pattern

```text
Use the [skill-name] skill to review the following [ticket, RCA, evidence request, vendor intake, policy exception, or AI use case].

Evaluate it for governance completeness, risk, approval readiness, audit readiness, ownership, evidence quality, and next actions.

[Paste source material here.]
```

## Important notes

These skills do not replace professional judgment, legal advice, audit advice, regulatory interpretation, management approval, security review, privacy review, or compliance signoff.

They are designed to improve consistency, structure, and completeness in GRC workflows.
