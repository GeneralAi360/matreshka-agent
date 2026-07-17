# Debugging report — `<symptom>`

## Status

- Result: `<ROOT_CAUSE_PROVED | LEADING_HYPOTHESIS | NEEDS_CONTEXT | BLOCKED | STOP_AND_RESCOPE | HANDOFF_REQUIRED>`
- Investigation mode: `<read-only; report/run-owned diagnostic artifact only>`
- Project root and current state: `<root / ref / hashes>`
- Confidence: `<level and reason>`

## Scope handoff

- Completed investigation scope: `<boundaries inspected and questions answered>`
- Incomplete investigation scope: `<remaining question or none>`
- Product/test files changed: `none`
- Report or diagnostic artifacts written: `<exact authorized paths or none>`
- Pre-existing failures: `<list or none>`

## Symptom and reproduction

- Expected: `<behavior>`
- Observed: `<behavior>`
- Focused command or interaction: `<exact safe reproduction>`
- Exit code/counts: `<evidence>`
- Frequency: `<deterministic or N failures in M bounded runs>`
- Baseline comparison: `<result or unavailable>`

## Causal analysis

- Trigger: `<condition>`
- Earliest incorrect state: `<boundary and value>`
- Root defect: `<code/configuration/data/environment condition>`
- Propagation: `<short causal chain>`
- Counterfactual evidence: `<experiment and result>`

## Hypotheses

| Hypothesis | Prediction | Evidence | Decision |
| --- | --- | --- | --- |
| `<candidate>` | `<observable result>` | `<support/counterevidence>` | `<accepted/rejected/open>` |

## Fix handoff

- Smallest fix boundary: `<files/interfaces for a separate implementation task; no implementation in DEBUG mode>`
- Focused regression test: `<behavior and command>`
- Risks and adjacent findings: `<list>`
- Assumptions and concerns: `<list or none>`
- Permissions still required: `<list or none>`
- Exact next action: `<single next step>`
