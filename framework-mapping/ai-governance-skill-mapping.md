# AI Governance Skill Mapping

This page maps the Governance Systems Skills Library to AI governance themes. It focuses on practical intake, risk review, vendor due diligence, data protection, model use, transparency, and approval readiness.

## AI Governance Themes

| Theme | Related Skills | Governance Value |
|---|---|---|
| AI intake review | `ai-governance-intake-review` | Reviews the proposed AI use case before approval. |
| Vendor due diligence | `third-party-risk-review`, `ai-governance-intake-review` | Checks SOC 2, DPA, AI terms, vendor evidence, subprocessors, and security posture. |
| Data protection | `ai-governance-intake-review`, `third-party-risk-review`, `control-evidence-quality-check` | Reviews data types, CSV uploads, API integration, retention, deletion, and privacy concerns. |
| Prompt and model risk | `ai-governance-intake-review` | Checks prompt retention, customer data use, model training restrictions, and output risk. |
| Policy exceptions | `policy-exception-review` | Reviews exceptions to AI, vendor, privacy, security, or production usage requirements. |
| Risk tracking | `risk-register-builder` | Converts AI or vendor concerns into risk register entries. |
| Executive reporting | `executive-grc-summary`, `governance-metrics-summary` | Summarizes AI risk posture, approvals, exceptions, and remediation for leadership. |
| Evidence readiness | `audit-evidence-request`, `control-evidence-quality-check` | Helps prepare audit-ready evidence for AI approvals, vendor due diligence, and data controls. |

## AI Governance Intake Lifecycle

| Lifecycle Step | Recommended Skill | Output |
|---|---|---|
| Submit AI use case | `ai-governance-intake-review` | Intake review, risk summary, approval readiness decision. |
| Review vendor and contract evidence | `third-party-risk-review` | Vendor risk decision and required evidence. |
| Review AI-specific terms | `ai-governance-intake-review` | Prompt retention and model training review questions. |
| Identify policy exceptions | `policy-exception-review` | Exception decision, compensating controls, risk acceptance requirements. |
| Convert concerns into risk | `risk-register-builder` | Risk register entry with owner, treatment, and residual risk. |
| Prepare leadership summary | `executive-grc-summary` | Executive decision brief. |
| Track program metrics | `governance-metrics-summary` | AI governance metrics and trend summary. |
| Review evidence before audit | `control-evidence-quality-check` | Evidence quality review and submission guidance. |

## AI Governance Risk Questions

The `ai-governance-intake-review` skill is designed to ask questions such as:

1. What data will be entered, uploaded, queried, or processed?
2. Will employee, customer, internal, confidential, regulated, or proprietary data be used?
3. Does the vendor retain prompts, uploads, outputs, or logs?
4. Can customer data be used for model training?
5. Is customer data isolated from other customers?
6. Has the DPA been reviewed?
7. Have AI-specific terms been reviewed separately from standard SaaS terms?
8. Is there a human review process for outputs?
9. Will AI-generated content be disclosed or labeled?
10. What access controls and audit logs are available?
11. Can users export, download, or share outputs?
12. What is the pilot scope and exit criteria?

## AI Governance Approval Gates

Before approval, an AI use case should generally answer the following:

| Gate | Required Evidence |
|---|---|
| Business purpose | Use case, business owner, expected value, scope. |
| Data review | Data types, classification, data flow, retention, deletion. |
| Security review | Security questionnaire, SOC 2 or equivalent evidence, access controls. |
| Privacy/legal review | DPA, AI-specific terms, subprocessors, data processing commitments. |
| Model risk review | Prompt retention, model training, output limitations, reliability concerns. |
| Human oversight | Human review, approval owner, escalation process. |
| Transparency | Disclosure rules, labeling expectations, leadership communication controls. |
| Pilot controls | Non-production data, synthetic data, user limits, success criteria. |
| Production approval | Final approvals, implementation plan, rollback/removal plan, monitoring. |

## Recommended AI Governance Outputs

| Output | Supporting Skill |
|---|---|
| AI intake review memo | `ai-governance-intake-review` |
| Vendor risk decision | `third-party-risk-review` |
| AI exception review | `policy-exception-review` |
| AI risk register entry | `risk-register-builder` |
| AI governance summary | `executive-grc-summary` |
| AI governance metrics | `governance-metrics-summary` |
| Evidence quality check | `control-evidence-quality-check` |

## Usage Note

This mapping supports practical AI governance workflow design. It does not replace legal review, privacy review, security review, procurement review, or enterprise AI policy approval.
