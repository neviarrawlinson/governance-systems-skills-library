# Governance Workflow Model

## Overview

The Governance Systems Skills Library is built around a simple operating model:

1. Intake the request, issue, incident, or evidence need.
2. Apply a repeatable governance review pattern.
3. Identify gaps, blockers, risks, and required corrections.
4. Produce a usable artifact for the system of record.
5. Track follow-up actions and report outcomes.

## Core Workflow Types

| Workflow | Skill Pack |
|---|---|
| Change review | `change-governance-review` |
| CAB decision support | `cab-readiness-check` |
| Incident and RCA review | `rca-governance-analysis` |
| Audit evidence collection | `audit-evidence-request` |
| Risk documentation | `risk-register-builder` |
| Leadership reporting | `executive-grc-summary` |

## Design Principles

- Controls should be embedded in work, not only documented in policies.
- Governance decisions should be repeatable and explainable.
- Audit evidence should be generated as a byproduct of normal workflows.
- Risk and remediation should be tracked with ownership.
- Executive reporting should focus on decisions, patterns, and blockers.

## Example End-to-End Flow

1. A production change is submitted.
2. `change-governance-review` checks completeness.
3. `cab-readiness-check` decides whether the change can move to CAB.
4. If a gap is repeated, `risk-register-builder` creates a risk entry.
5. If the change causes an incident, `rca-governance-analysis` reviews the RCA.
6. `executive-grc-summary` prepares weekly reporting for leadership.
