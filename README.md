# Governance Systems Skills Library

Practical AI skill packs for governance, risk, compliance, audit readiness, change management, RCA, and executive reporting.

This project is designed for GRC practitioners, IT governance analysts, compliance teams, auditors, risk owners, and technology leaders who need repeatable, audit-ready workflows.

Unlike generic framework reference libraries, this repository focuses on operational governance workflows: reviewing change requests, preparing CAB summaries, analyzing RCAs, building risk register entries, responding to audit evidence requests, and creating executive-ready GRC summaries.

## Live Demo

View the project landing page:

https://neviarrawlinson.github.io/governance-systems-skills-library/

## Why This Exists

Many governance programs fail because controls live in documents but not in daily workflows.

Governance Systems Engineering focuses on turning governance expectations into repeatable systems, checklists, decision logic, templates, and AI-assisted workflows that support real operational decisions.

## Initial Skill Packs

| Skill | Purpose |
|---|---|
| `change-governance-review` | Reviews change requests for governance completeness, risk, rollback, validation, monitoring, approvals, and audit readiness. |
| `cab-readiness-check` | Determines whether a change is ready for CAB review and identifies blockers before approval. |
| `rca-governance-analysis` | Reviews incident and RCA details for root cause quality, monitoring gaps, ownership gaps, and corrective actions. |
| `audit-evidence-request` | Converts vague audit requests into clear evidence checklists and response plans. |
| `risk-register-builder` | Converts risks, issues, incidents, or audit findings into structured risk register entries. |
| `executive-grc-summary` | Creates concise leadership-ready summaries for governance, risk, audit, compliance, and change updates. |

## Repository Structure

```text
governance-systems-skills-library/
├── README.md
├── docs/
├── skills/
│   ├── change-governance-review/
│   ├── cab-readiness-check/
│   ├── rca-governance-analysis/
│   ├── audit-evidence-request/
│   ├── risk-register-builder/
│   └── executive-grc-summary/
├── templates/
├── examples/
├── framework-mapping/
├── dist/
└── site/
```

Each skill folder contains a `SKILL.md` file with Claude-compatible skill instructions, a human-readable `README.md`, references, and examples.

## How to Use

1. Open a skill folder under `skills/`.
2. Review the `SKILL.md` instructions.
3. Upload or install the skill using the Claude Skills workflow available in your Claude environment.
4. Test the skill with realistic governance inputs, such as a change request, RCA draft, audit request, risk statement, or executive update.
5. Refine the skill based on your organization, control framework, risk methodology, and governance process.

## Suggested First Test

Use the `change-governance-review` skill with a sample change request that includes:

- Summary
- Environment
- Implementation plan
- Validation plan
- Rollback plan
- Risk and impact
- Monitoring plan
- Approvals

Then ask Claude:

```text
Review this change request for governance completeness and CAB readiness.
```

## Practical Workflow Examples

This project includes examples for:

- Jira change governance review.
- CAB packet preparation.
- Confluence RCA documentation.
- Audit evidence response planning.
- Risk register entry creation.
- Executive GRC update summarization.

## Framework Mapping

The `framework-mapping/` folder connects the skill packs to common governance and assurance themes across:

- ISO 27001
- SOC 2
- NIST CSF
- COBIT

These mappings are practical references and do not reproduce proprietary framework text.

## Packaging Skills

Run the packaging script from the repo root:

```bash
bash package-skills.sh
```

This creates downloadable zip files under:

```text
dist/
```

## Intended Use

These skills are designed to help practitioners produce clearer, more consistent governance outputs. They support professional judgment, but they do not replace legal advice, audit advice, regulatory interpretation, or organization-specific policy decisions.

## Roadmap

- Add more Jira and Confluence workflow examples.
- Add downloadable release assets through GitHub Releases.
- Add screenshots and project preview images.
- Add additional framework mappings.
- Add governance automation examples.
- Add tests for skill folder validation.

## License

This project is released under the MIT License. See `LICENSE` for details.
