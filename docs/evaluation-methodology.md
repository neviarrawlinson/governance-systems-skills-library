# Evaluation Methodology

## Overview

The Governance Systems Skills Library evaluation methodology is designed to test whether each skill produces practical, governance-ready outputs.

The evaluation process focuses on decision quality, governance gap detection, risk analysis, evidence requirements, ownership, usability, and professional tone.

## Evaluation Principles

1. **Scenario-based testing**: Skills are tested against realistic GRC scenarios.
2. **Expected outcome comparison**: Outputs are compared to predefined expected findings.
3. **Rubric scoring**: Each output is scored using a consistent 100-point scorecard.
4. **Traceable review notes**: Each evaluation should include the prompt, output, score, and reviewer comments.
5. **Continuous improvement**: Missed findings should be converted into skill improvements.

## Scoring Categories

| Category | Points |
|---|---:|
| Correct decision or recommendation | 20 |
| Governance gap identification | 20 |
| Risk and impact analysis | 15 |
| Evidence and traceability requirements | 15 |
| Ownership and accountability | 10 |
| Output usability | 10 |
| Tone and professional judgment | 10 |

## Evaluation Process

1. Select a test case from the `tests/` folder.
2. Run the prompt with the applicable skill.
3. Save the generated output.
4. Score the output using the evaluation scorecard.
5. Record results in the evaluation log.
6. Identify missed findings or improvement opportunities.
7. Update the skill if necessary.
8. Re-test after changes.

## Success Criteria

A skill output is considered portfolio-ready if it scores 85 or higher and does not miss any critical governance blockers.

Critical blockers include:

- Unsafe production approval.
- Missing security or compliance approval.
- Missing audit evidence gap.
- Failure to identify high residual risk.
- Failure to identify missing ownership or due dates.
- Failure to distinguish draft/supporting context from primary evidence.
