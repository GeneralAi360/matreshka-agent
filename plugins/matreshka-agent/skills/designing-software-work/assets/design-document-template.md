# Design — {{TITLE}}

- Status: `{{DRAFT_OR_CONFIRMED}}`
- Date: `{{DATE}}`
- Owner/decision authority: {{OWNER}}
- Related request: {{REQUEST_REFERENCE}}

## Outcome

{{PLAIN_LANGUAGE_USER_OR_SYSTEM_OUTCOME}}

## Confirmed facts

- {{INSPECTED_FACT}}

## Assumptions

- {{ASSUMPTION_AND_VALIDATION_PLAN}}

## Constraints

- {{CONSTRAINT}}

## Goals and acceptance outcomes

- {{MEASURABLE_OUTCOME}}

## Non-goals

- {{EXCLUDED_OUTCOME}}

## Approaches considered

### Approach A — {{NAME}}

- Shape: {{SUMMARY}}
- Advantages: {{ADVANTAGES}}
- Costs/risks: {{COSTS}}
- Migration/rollback: {{IMPLICATIONS}}

### Approach B — {{NAME}}

- Shape: {{SUMMARY}}
- Advantages: {{ADVANTAGES}}
- Costs/risks: {{COSTS}}
- Migration/rollback: {{IMPLICATIONS}}

### Approach C — {{NAME_OR_NA}}

- Shape: {{SUMMARY_OR_NA}}
- Advantages: {{ADVANTAGES_OR_NA}}
- Costs/risks: {{COSTS_OR_NA}}
- Migration/rollback: {{IMPLICATIONS_OR_NA}}

## Decision

- Recommended approach: {{APPROACH}}
- Rationale: {{WHY_IT_FITS}}
- Confirmation or delegated authority: {{DECISION_RECORD}}

## Architecture and responsibilities

| Component | Responsibility | Owns | Must not own |
| --- | --- | --- | --- |
| {{COMPONENT}} | {{RESPONSIBILITY}} | {{OWNERSHIP}} | {{NON_RESPONSIBILITY}} |

## Interfaces

| Interface | Caller/owner | Input/output | Validation/errors | Compatibility |
| --- | --- | --- | --- | --- |
| {{INTERFACE}} | {{OWNER}} | {{CONTRACT}} | {{BEHAVIOR}} | {{RULE}} |

## Data and state flow

1. {{FLOW_STEP}}
2. {{FLOW_STEP}}

- Source of truth: {{SOURCE}}
- State transitions: {{TRANSITIONS}}
- Atomicity/idempotency: {{RULES}}
- Tenant/organization boundary: {{BOUNDARY_OR_NA}}

## Failure and degraded behavior

| Failure | Expected behavior | Evidence/observability |
| --- | --- | --- |
| {{FAILURE}} | {{SAFE_BEHAVIOR}} | {{SIGNAL}} |

## Security and privacy

- Authority source: {{AUTHORITY_OR_NA}}
- Trust boundaries: {{BOUNDARIES_OR_NA}}
- Secret handling: {{SECRET_POLICY_OR_NA}}
- Data exposure/redaction: {{EXPOSURE_POLICY_OR_NA}}
- Abuse and isolation negatives: {{NEGATIVE_CASES_OR_NA}}

## Migration, rollout, and rollback

- Existing compatibility: {{COMPATIBILITY}}
- Migration stages: {{STAGES_OR_NA}}
- Rollout guardrails: {{GUARDRAILS}}
- Rollback trigger and action: {{ROLLBACK}}
- Cleanup: {{CLEANUP_OR_NA}}

## Observability and operations

- Metrics/logs/traces: {{SIGNALS}}
- Sensitive-data exclusions: {{REDACTION}}
- Owner and response: {{OWNER}}

## Testing strategy

| Design claim | Evidence category | Critical negative |
| --- | --- | --- |
| {{CLAIM}} | {{TEST_TYPE}} | {{NEGATIVE_CASE}} |

## Open decisions

- {{OPEN_DECISION_OR_NONE}}

## Self-review

- [ ] No unresolved placeholder remains.
- [ ] Requirements and interfaces do not contradict each other.
- [ ] Remote actions and permissions are explicit.
- [ ] Failure and rollback behavior are defined.
- [ ] Each acceptance outcome has a verification path.
- [ ] Scope can be decomposed into independently reviewable tasks.
