# Tested Output: AI Reporting Assistant Governance Intake Review

## Input Summary

Use Case Name: AI Reporting Assistant  
Requested By: Reporting Services Team  

Business Purpose:  
The team wants to use an AI assistant to summarize reporting trends, explain dashboard anomalies, and generate draft leadership updates from internal reporting data.

AI Tool Type:  
Third-party SaaS AI assistant with natural language query and summarization features.

Data Involved:
- Internal reporting data
- Employee user IDs
- Department-level performance metrics
- Operational dashboards
- Exported CSV files from the Reporting Service

Users:
- 25 internal users from Reporting Services, Business Operations, and IT leadership.

Integration:
- The tool may connect to the Reporting Service API.
- The tool may allow users to upload CSV exports.

Vendor Status:
- Vendor security review has not been completed.
- SOC 2 report has not been provided.
- DPA has not been reviewed.
- No AI-specific terms have been reviewed.

Known Context:
- The Reporting Service recently had a production outage after a database configuration change.
- A high residual risk entry remains open for weak validation, rollback, monitoring, and evidence controls.
- Governance has identified concerns around CSV export, data retention, and third-party access.

Requested Decision:
Approve the AI assistant for a pilot within two weeks.

## AI Governance Intake Review Summary

Status: Not Ready for Approval  
Recommended Decision: Hold  
Risk Rating: High  
Pilot Recommendation: Consider non-production pilot only with synthetic or anonymized data.  
Production Approval: Not approved as submitted.

## Executive Finding

The AI Reporting Assistant intake should be held.

The business need is legitimate, but the request is not ready for approval because it combines third-party AI, internal reporting data, employee identifiers, possible API access, CSV upload/export functionality, incomplete vendor due diligence, and an existing high residual risk tied to the Reporting Service.

This request also introduces AI-specific risks that go beyond a standard SaaS vendor review, including prompt retention, model training use, AI-generated leadership content, transparency, human review, and output reliability.

## Key Findings

- Vendor security review has not been completed.
- SOC 2 report has not been provided.
- DPA has not been reviewed.
- AI-specific contractual terms have not been reviewed.
- Data retention and prompt retention practices are unknown.
- It is unclear whether customer prompts, uploaded files, or outputs may be used for model training.
- The tool may connect to the Reporting Service API, which introduces integration risk.
- CSV upload/export functionality creates data transfer, retention, and deletion concerns.
- The Reporting Service already has an open high residual risk entry.
- AI-generated leadership updates require transparency, human review, and approval controls.
- The requested two-week approval timeline is not realistic for production use under current conditions.

## Decision Rationale

The recommended decision is **Hold**, not reject.

The request should be held because the use case may be valuable, but the governance, security, privacy, legal, AI, and operational reviews are incomplete. A path to approval exists, but production use or live internal data use should not be approved until required due diligence is completed.

## AI-Specific Risk Review

| Risk Area | Rating | Assessment |
|---|---|---|
| Data Privacy Risk | High | Employee user IDs, internal reporting data, operational dashboards, and CSV files may be processed by a third-party AI vendor without a reviewed DPA. |
| Prompt Retention Risk | High | Vendor terms have not confirmed whether prompts, uploads, or outputs are retained or used for model training. |
| Model Training Risk | High | If customer inputs can be used for model training, internal data could be incorporated into a shared model. |
| Security Risk | High | Vendor security review is incomplete and SOC 2 has not been provided. |
| Integration Risk | High | API connection to the Reporting Service could increase exposure for a system with open residual risk. |
| Data Export Risk | High | CSV upload/export creates data egress, retention, access, deletion, and audit visibility concerns. |
| Output Reliability Risk | Medium to High | AI-generated summaries may contain errors, omissions, or unsupported interpretations. |
| Transparency Risk | Medium to High | Leadership updates drafted by AI may be used without clear disclosure or human validation. |
| Compliance Risk | High | Missing DPA, AI terms, security review, and data handling review create audit and governance exposure. |
| Operational Risk | High | The Reporting Service has recent outage history and unresolved governance control gaps. |

## Approval Readiness

The request is not ready for approval.

Production approval should be blocked until the following are completed:

1. Vendor security review.
2. SOC 2 or equivalent security evidence review.
3. DPA review and approval.
4. AI-specific terms review.
5. Confirmation of prompt retention and training-use restrictions.
6. Data classification review.
7. Data flow documentation.
8. API integration review.
9. CSV upload/export control review.
10. Human review process for AI-generated outputs.
11. Transparency requirements for AI-assisted leadership communications.
12. Access control and logging plan.
13. Pilot scope and exit criteria.
14. Business owner, data owner, system owner, Security, Privacy, Legal, and Governance approval.

## Required Owner Questions

### Business Owner Questions

1. What decisions will leadership make using AI-generated summaries?
2. Will AI-generated content be distributed externally or only internally?
3. Will users be required to disclose when content is AI-assisted?
4. Who is responsible for reviewing and approving AI-generated leadership updates?
5. What dashboard anomalies will the AI assistant be allowed to interpret?
6. What is the success criteria for the pilot?
7. Can the pilot be performed using synthetic or anonymized data?
8. Why is production Reporting Service API access needed for the pilot?

### Vendor Questions

1. Are customer prompts retained?
2. Are uploaded CSV files retained?
3. Are customer prompts, uploads, or outputs used to train models?
4. Can customer data be excluded from model training?
5. Where is customer data stored?
6. How long is customer data retained?
7. Can customer data be deleted upon request?
8. Are logs available for customer review?
9. What subprocessors are used?
10. What security certifications or audit reports are available?
11. Can CSV upload/export be disabled or restricted?
12. Are role-based access controls supported?

### Security, Privacy, and Legal Questions

1. Has the vendor completed security review?
2. Has the SOC 2 report or equivalent evidence been reviewed?
3. Has the DPA been reviewed and approved?
4. Have AI-specific terms been reviewed separately from standard SaaS terms?
5. Does the vendor contract prohibit customer data use for model training?
6. Are employee identifiers allowed in the tool?
7. Are there restrictions on uploading internal reporting data?
8. Are audit logs available and retained?
9. Is there an approved incident notification process?
10. Is there an approved data deletion process?

## Non-Production Pilot Option

A limited non-production pilot may be considered if the team needs to evaluate the AI assistant quickly.

Recommended pilot guardrails:

- Use synthetic, anonymized, or non-sensitive data only.
- Do not connect the tool to the production Reporting Service API.
- Do not upload production CSV files.
- Do not include employee user IDs.
- Limit access to named pilot users.
- Disable export and sharing features where possible.
- Require human review of all AI outputs.
- Do not distribute AI-generated leadership updates as official communications.
- Document pilot success criteria.
- Continue vendor, security, privacy, legal, and AI governance review in parallel.
- Require separate approval before production data or production integration is allowed.

## AI Transparency and Human Review Requirements

Because the use case includes draft leadership updates, the governance process should require:

- Human review before any AI-generated content is shared.
- Clear ownership for final content approval.
- Disclosure when content is AI-assisted, where appropriate.
- Validation of AI-generated summaries against source data.
- Prohibition on using AI output as the sole basis for leadership decisions.
- Documentation of known limitations, such as hallucinations, omissions, or misinterpretation of trends.
- Review process for correcting inaccurate outputs.

## Pattern and Sequencing Concern

This intake should also be reviewed in the context of broader Reporting Service governance activity.

The Reporting Services Team has multiple related requests involving the same system, similar data, third-party tools, CSV exports, and production integration. The Reporting Service also has an open high residual risk entry.

Governance should consider sequencing the work as follows:

1. Resolve or actively remediate the open Reporting Service risk.
2. Complete third-party risk review for related analytics tooling.
3. Establish baseline vendor and AI governance requirements.
4. Approve only non-production pilots until production controls are validated.
5. Require production approval through normal security, privacy, legal, and governance gates.

## Required Evidence Before Production Approval

Before production approval, the intake should include:

- Completed AI intake form.
- Business owner approval.
- System owner approval.
- Data owner approval.
- Security review approval.
- Privacy or Legal approval.
- Governance approval.
- SOC 2 report or equivalent security evidence.
- Reviewed DPA.
- Reviewed AI-specific terms.
- Confirmation that customer data is not used for model training.
- Data flow diagram.
- Data classification review.
- API integration design.
- CSV upload/export control decision.
- Access control plan.
- Audit logging plan.
- Human review and transparency process.
- Pilot success and exit criteria.
- Production implementation plan.
- Rollback or removal plan.

## Governance Note

**AI Governance Intake Review**

- **Use Case**: AI Reporting Assistant for reporting trends, dashboard anomalies, and draft leadership updates.
- **Requested Decision**: Approve pilot within two weeks.
- **Decision**: Hold. Not approved for production use or live internal data use as submitted.
- **Risk Summary**: High risk due to third-party AI processing, internal reporting data, employee identifiers, CSV upload/export, possible production API integration, missing SOC 2, missing DPA, incomplete security review, unreviewed AI terms, and open high residual risk for the Reporting Service.
- **AI-Specific Concerns**: Prompt retention, model training use, AI-generated leadership content, transparency, human review, output accuracy, and data retention are unresolved.
- **Pilot Option**: A limited non-production pilot may be considered using synthetic or anonymized data only.
- **Required Actions**: Complete security review, obtain SOC 2 or equivalent evidence, review DPA, review AI-specific terms, confirm model training restrictions, document data flows, define human review controls, and establish pilot guardrails.

Governance review completed. The AI intake request should remain on hold until security, privacy, legal, AI governance, data protection, and operational risk requirements are satisfied.

## Recommended Next Action

Hold production approval and offer a limited non-production pilot using synthetic or anonymized data. Begin due diligence immediately by requesting SOC 2 or equivalent evidence, completing the security questionnaire, initiating DPA and AI terms review, documenting data flows, and confirming whether customer prompts, uploads, or outputs are retained or used for model training.
