# Skill to Framework Matrix

This matrix maps each Governance Systems Skills Library skill to common governance, risk, compliance, audit, and operational control themes.

This mapping is intended for portfolio demonstration, training, internal governance design, control conversation support, and audit-readiness planning. It is not a substitute for legal, regulatory, audit, or certification advice.

## Matrix Overview

| Skill | ISO 27001 Theme | SOC 2 Theme | NIST CSF Theme | COBIT Theme | Primary Governance Use Case |
|---|---|---|---|---|---|
| `change-governance-review` | Change control, operational control, secure change practices | Change management, logical access, system operations | Govern, Protect, Detect | BAI06, DSS01, MEA01 | Review production changes for readiness, risk, approvals, rollback, validation, and monitoring. |
| `cab-readiness-check` | Change authorization and operational readiness | Change approval and change evidence | Govern, Protect | BAI06, APO12 | Determine whether a change is ready for CAB review or needs conditions before approval. |
| `rca-governance-analysis` | Incident learning, corrective action, continual improvement | Incident response, corrective action, monitoring | Detect, Respond, Recover | DSS02, DSS03, MEA01 | Review RCA quality, ownership, monitoring gaps, corrective actions, and leadership readiness. |
| `audit-evidence-request` | Evidence quality, control documentation, audit support | Control evidence, review evidence, audit request support | Govern, Identify | MEA03, APO12 | Convert audit requests into clear evidence checklists and owner questions. |
| `risk-register-builder` | Risk identification, treatment, ownership | Risk assessment and monitoring | Govern, Identify | APO12, EDM03 | Convert issues, findings, and incidents into structured risk register entries. |
| `executive-grc-summary` | Governance reporting and accountability | Management reporting and oversight | Govern | EDM01, EDM03, MEA01 | Turn complex governance activity into leadership-ready status and decision summaries. |
| `policy-exception-review` | Exception management, risk acceptance, compensating controls | Risk acceptance, exception documentation | Govern, Identify, Protect | APO12, MEA02 | Review exceptions for risk impact, approvals, duration, compensating controls, and evidence. |
| `third-party-risk-review` | Supplier security, access, data protection | Vendor management, confidentiality, privacy | Govern, Identify, Protect | APO10, APO12 | Review SaaS vendors, integrations, data sharing, security evidence, and approval readiness. |
| `control-evidence-quality-check` | Evidence reliability, control operation, audit readiness | Evidence sufficiency, completeness, and traceability | Govern, Identify | MEA03, MEA01 | Assess whether evidence demonstrates control operation and is ready for audit submission. |
| `governance-metrics-summary` | Performance monitoring, governance reporting | Control monitoring and management review | Govern, Identify, Respond | MEA01, EDM05 | Summarize governance metrics, exceptions, trends, risks, and leadership actions. |
| `ai-governance-intake-review` | AI use governance, supplier risk, data protection | Security, confidentiality, privacy, change and vendor risk | Govern, Identify, Protect | APO12, APO14, BAI03 | Review AI use cases for data use, model risk, vendor risk, transparency, and approval readiness. |

## Practical Interpretation

The library is designed around operational workflows rather than framework memorization. Each skill supports a repeatable governance activity that can generate evidence, decisions, risk records, or leadership summaries.

Framework alignment helps demonstrate that the workflows are not isolated templates. They support broader control objectives across change management, incident governance, risk management, vendor review, audit evidence, and AI governance.

## Common Control Themes

| Theme | Related Skills |
|---|---|
| Change governance | `change-governance-review`, `cab-readiness-check`, `audit-evidence-request`, `control-evidence-quality-check` |
| RCA and incident governance | `rca-governance-analysis`, `risk-register-builder`, `executive-grc-summary` |
| Audit readiness | `audit-evidence-request`, `control-evidence-quality-check`, `executive-grc-summary` |
| Risk management | `risk-register-builder`, `policy-exception-review`, `third-party-risk-review`, `ai-governance-intake-review` |
| Vendor and third-party risk | `third-party-risk-review`, `ai-governance-intake-review`, `control-evidence-quality-check` |
| Executive governance reporting | `governance-metrics-summary`, `executive-grc-summary`, `risk-register-builder` |
| AI governance | `ai-governance-intake-review`, `third-party-risk-review`, `policy-exception-review` |

## How to Use This Matrix

Use this matrix to:

1. Explain how each skill connects to recognized governance domains.
2. Demonstrate portfolio alignment to GRC frameworks.
3. Support training conversations with new GRC practitioners.
4. Show how workflow-based governance can produce audit-ready evidence.
5. Identify which skills apply to a control gap, audit request, incident, vendor intake, policy exception, or leadership report.
