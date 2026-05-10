# Quickstart Guide

Use this guide to quickly understand, download, and test the Governance Systems Skills Library.

## 1. Download the latest skill package

Go to the latest GitHub release and download:

```text
governance-systems-skill-packages.zip
```

## 2. Unzip the package

After downloading, extract the package on your computer.

You should see individual skill folders such as:

```text
change-governance-review/
cab-readiness-check/
rca-governance-analysis/
audit-evidence-request/
risk-register-builder/
executive-grc-summary/
policy-exception-review/
third-party-risk-review/
control-evidence-quality-check/
governance-metrics-summary/
ai-governance-intake-review/
```

Each skill folder contains a `SKILL.md` file and supporting examples or references.

## 3. Choose a skill to test

Start with one of the core workflow skills:

```text
change-governance-review
cab-readiness-check
audit-evidence-request
```

## 4. Use a tested prompt

Each skill folder contains a tested output example under:

```text
skills/<skill-name>/examples/tested-output.md
```

Use the tested example to understand the expected output style and quality.

## 5. Validate the repository

If you are working from the source repository, run:

```bash
python scripts/validate-skills.py
```

## 6. Package the skills

If you want to package the skill folders locally, run:

```bash
bash package-skills.sh
```

The output is generated in the `dist/` folder.

## Recommended first test

Use the `change-governance-review` skill with a weak production change request. The skill should identify missing implementation details, weak validation, weak rollback planning, missing monitoring, incomplete approvals, and audit readiness gaps.
