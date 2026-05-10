# NIST CSF Skill Mapping

This page maps the Governance Systems Skills Library to NIST Cybersecurity Framework themes. The mapping is intended to show how workflow-based governance skills can support cybersecurity governance, risk management, control execution, and reporting.

## NIST CSF Theme Mapping

| Skill | Govern | Identify | Protect | Detect | Respond | Recover |
|---|---:|---:|---:|---:|---:|---:|
| `change-governance-review` | Yes | Yes | Yes | Yes |  |  |
| `cab-readiness-check` | Yes | Yes | Yes |  |  |  |
| `rca-governance-analysis` | Yes | Yes |  | Yes | Yes | Yes |
| `audit-evidence-request` | Yes | Yes |  |  |  |  |
| `risk-register-builder` | Yes | Yes |  |  | Yes |  |
| `executive-grc-summary` | Yes |  |  |  | Yes |  |
| `policy-exception-review` | Yes | Yes | Yes |  |  |  |
| `third-party-risk-review` | Yes | Yes | Yes |  |  |  |
| `control-evidence-quality-check` | Yes | Yes |  |  |  |  |
| `governance-metrics-summary` | Yes | Yes |  | Yes | Yes |  |
| `ai-governance-intake-review` | Yes | Yes | Yes |  |  |  |

## Skill-Level NIST CSF Alignment

### `change-governance-review`

Primary CSF themes:

- Govern
- Identify
- Protect
- Detect

Governance value:

This skill supports change governance by checking whether a technology change includes risk, approvals, implementation planning, validation, rollback, and monitoring.

### `cab-readiness-check`

Primary CSF themes:

- Govern
- Identify
- Protect

Governance value:

This skill supports governance decision-making before a change moves forward by identifying approval gaps, readiness blockers, and required pre-deployment conditions.

### `rca-governance-analysis`

Primary CSF themes:

- Govern
- Identify
- Detect
- Respond
- Recover

Governance value:

This skill supports incident governance by evaluating root cause completeness, detection failure, timeline quality, corrective actions, and recovery lessons.

### `audit-evidence-request`

Primary CSF themes:

- Govern
- Identify

Governance value:

This skill helps turn control requests into clear evidence expectations and owner questions.

### `risk-register-builder`

Primary CSF themes:

- Govern
- Identify
- Respond

Governance value:

This skill converts observed issues into structured risk entries with owners, treatment plans, residual risk, and evidence requirements.

### `executive-grc-summary`

Primary CSF themes:

- Govern
- Respond

Governance value:

This skill supports leadership communication and decision-making when governance gaps, risks, or incidents require visibility.

### `policy-exception-review`

Primary CSF themes:

- Govern
- Identify
- Protect

Governance value:

This skill reviews whether exceptions are justified, time-bound, approved, and supported by compensating controls.

### `third-party-risk-review`

Primary CSF themes:

- Govern
- Identify
- Protect

Governance value:

This skill supports vendor and supplier risk management by reviewing data use, integrations, security evidence, privacy documentation, and approval readiness.

### `control-evidence-quality-check`

Primary CSF themes:

- Govern
- Identify

Governance value:

This skill evaluates whether control evidence is complete, traceable, relevant, and ready for audit submission.

### `governance-metrics-summary`

Primary CSF themes:

- Govern
- Identify
- Detect
- Respond

Governance value:

This skill turns governance metrics into trends, exceptions, leadership actions, and improvement priorities.

### `ai-governance-intake-review`

Primary CSF themes:

- Govern
- Identify
- Protect

Governance value:

This skill supports AI governance by reviewing data use, AI vendor risk, prompt retention, model training risk, transparency, access, and approval readiness.

## NIST CSF Use Cases

| Use Case | Recommended Skills |
|---|---|
| Evaluate production change risk | `change-governance-review`, `cab-readiness-check` |
| Investigate incident governance gaps | `rca-governance-analysis`, `risk-register-builder` |
| Prepare for audit evidence review | `audit-evidence-request`, `control-evidence-quality-check` |
| Summarize program health | `governance-metrics-summary`, `executive-grc-summary` |
| Review a SaaS tool | `third-party-risk-review` |
| Review an AI tool | `ai-governance-intake-review` |
| Review a control exception | `policy-exception-review` |

## Usage Note

This mapping is designed to support NIST CSF-aligned thinking. It is not a formal control assessment or certification claim.
