# Framework Mapping Coverage Model

This document explains the coverage logic used in the framework mapping files.

## Coverage Approach

The Governance Systems Skills Library uses a workflow-first mapping model.

Instead of trying to map every skill to every possible framework control, the project maps each skill to practical governance themes that commonly appear across frameworks.

## Coverage Layers

| Layer | Description |
|---|---|
| Workflow | The practical GRC activity the skill performs. |
| Control Theme | The type of control or governance objective the workflow supports. |
| Framework Theme | The broader framework area that relates to the control theme. |
| Evidence Output | The artifact or decision record the skill helps generate. |

## Example

Skill: `change-governance-review`

| Layer | Example |
|---|---|
| Workflow | Review a production change request. |
| Control Theme | Change approval, validation, rollback, monitoring, evidence retention. |
| Framework Theme | Change management, system operations, governance, audit evidence. |
| Evidence Output | Governance review note, CAB decision support, missing evidence checklist. |

## Why This Model Works

This model works because GRC practitioners often need to bridge the gap between framework expectations and operational execution.

A framework may state that changes should be controlled, but a practitioner still needs to know:

- Was the change reviewed?
- Was it approved before deployment?
- Was testing performed?
- Was validation documented?
- Was rollback planned?
- Was monitoring performed?
- Is evidence audit-ready?

The skills help turn those expectations into repeatable review outputs.

## Mapping Confidence Levels

The project uses three informal confidence levels:

| Confidence | Meaning |
|---|---|
| Strong | The skill directly supports the governance workflow or evidence type. |
| Moderate | The skill supports the theme indirectly or as part of a broader process. |
| Contextual | The skill may apply depending on the organization's process, scope, or risk profile. |

## Use Caution

Framework mappings should always be validated against:

- Internal policies.
- Control descriptions.
- Audit scope.
- Regulatory commitments.
- System boundaries.
- Risk acceptance decisions.
- Management expectations.

## Recommended Future Enhancement

A future release can add control-by-control mapping tables with fields such as:

| Framework | Domain | Control Theme | Skill | Evidence Output | Confidence | Notes |
|---|---|---|---|---|---|---|
