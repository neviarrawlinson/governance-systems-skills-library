---
name: risk-register-builder
description: Converts issues, incidents, audit findings, control gaps, vendor concerns, process failures, or governance observations into structured risk register entries. Use when creating, improving, or normalizing risk statements and risk register records.
---

# Risk Register Builder

## Purpose

Use this skill to turn informal risk information into structured risk register entries.

The skill should produce clear, business-readable risk statements that include cause, event, impact, likelihood, severity, owner, mitigation, controls, and next steps.

## Risk Statement Pattern

Use this structure when possible:

Because of [cause], there is a risk that [event] may occur, resulting in [impact].

Example:

Because change requests are submitted without complete validation plans, there is a risk that production changes may be implemented without sufficient post-deployment confirmation, resulting in service disruption, delayed incident detection, or audit evidence gaps.

## Risk Register Fields

Create or improve the following fields:

- Risk ID
- Risk Title
- Risk Category
- Risk Statement
- Cause
- Event
- Impact
- Likelihood
- Impact Rating
- Inherent Risk
- Existing Controls
- Control Gaps
- Mitigation Plan
- Risk Owner
- Due Date
- Residual Risk
- Status
- Evidence Needed

## Rating Guidance

Use qualitative ratings unless the user provides a scoring model:

Likelihood: Low / Medium / High  
Impact: Low / Medium / High  
Risk Level: Low / Medium / High / Critical

Base the rating on business impact, customer impact, operational disruption, compliance exposure, security exposure, recurrence risk, and control maturity.

## Output Format

### Risk Register Entry

| Field | Entry |
|---|---|
| Risk ID |  |
| Risk Title |  |
| Risk Category |  |
| Risk Statement |  |
| Cause |  |
| Event |  |
| Impact |  |
| Likelihood |  |
| Impact Rating |  |
| Inherent Risk |  |
| Existing Controls |  |
| Control Gaps |  |
| Mitigation Plan |  |
| Risk Owner |  |
| Due Date Recommendation |  |
| Residual Risk |  |
| Status |  |
| Evidence Needed |  |

### Plain-English Summary

Explain the risk in 2 to 4 sentences for a non-technical audience.

### Recommended Next Action

Provide one clear next step for the risk owner or governance team.
