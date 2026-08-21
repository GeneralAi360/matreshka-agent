# Software Specification — {{TITLE}}

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

## Design Intelligence reference

Use this section only when UI/UX is material. It references the durable design contract; it does not duplicate it.

- Design status: `{{DESIGN_NOT_APPLICABLE_DESIGN_CURRENT_DESIGN_READY_TO_SAVE_OTHER}}`
- Root design contract: `{{DESIGN_MD_PATH_OR_READY_TO_SAVE_OR_NONE}}`
- Design identity/hash: `{{DESIGN_IDENTITY_OR_NONE}}`
- Accepted direction/personality: {{DIRECTION_OR_EXISTING_CURRENT_DESIGN_OR_NONE}}
- Design source/decision authority: {{DESIGN_DECISION_RECORD_OR_NONE}}

### User-experience outcomes

- {{OBSERVABLE_UX_FLOW_OR_STATE_OR_NA}}

### Design-critical constraints that affect software behavior

- {{RESPONSIVE_ACCESSIBILITY_STATE_NAVIGATION_OR_INTERFACE_CONSTRAINT_OR_NA}}

Do not copy the full typography/color/spacing/component/motion catalog here. Planning derives task-local `DESIGN_CONTEXT_SET` from root `DESIGN.md`.

## Approaches considered

### Approach A — {{NAME}}

- Shape: {{SUMMARY}}
- Advantages: {{ADVANTAGES}}
- Costs/risks: {{COSTS}}
- Migration/rollback: {{IMPLICATIONS}}
- Fit with frozen interfaces/design identity: {{FIT}}

### Approach B — {{NAME}}

- Shape: {{SUMMARY}}
- Advantages: {{ADVANTAGES}}
- Costs/risks: {{COSTS}}
- Migration/rollback: {{IMPLICATIONS}}
- Fit with frozen interfaces/design identity: {{FIT}}

### Approach C — {{NAME_OR_NA}}

- Shape: {{SUMMARY_OR_NA}}
- Advantages: {{ADVANTAGES_OR_NA}}
- Costs/risks: {{COSTS_OR_NA}}
- Migration/rollback: {{IMPLICATIONS}}
- Fit with frozen interfaces/design identity: {{FIT_OR_NA}}

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

## Security by Design

### Threat model

| Asset/data class | Actor and authority | Trust boundary | Abuse case | Mitigation |
| --- | --- | --- | --- | --- |
| {{ASSET_OR_NA}} | {{ACTOR}} | {{BOUNDARY}} | {{ABUSE_CASE}} | {{CONTROL}} |

### Automatic hardening-family selection

Every specification records all five families. Use `N/A` only with a concrete reason that the trigger is absent. A `REQUIRED` family must map to one or more normal `S-xx` rows below.

| Family | Selection | Trigger/evidence | Planned negative proof |
| --- | --- | --- | --- |
| `S-AUTH-HARDENING` | `{{REQUIRED_NA_HANDOFF}}` | {{PASSWORD_PRIVILEGED_AUTH_TRIGGER_OR_REASON}} | {{RATE_ENUMERATION_MFA_NEGATIVE_PROOF_OR_NA}} |
| `S-FILE-EXECUTION` | `{{REQUIRED_NA_HANDOFF}}` | {{UPLOAD_STORAGE_TRIGGER_OR_REASON}} | {{TYPE_PATH_NONEXECUTION_NEGATIVE_PROOF_OR_NA}} |
| `S-ATOMIC-EFFECT` | `{{REQUIRED_NA_HANDOFF}}` | {{RACE_SENSITIVE_EFFECT_TRIGGER_OR_REASON}} | {{CONCURRENT_DUPLICATE_NEGATIVE_PROOF_OR_NA}} |
| `S-BAAS-AUTHZ` | `{{REQUIRED_NA_HANDOFF}}` | {{CLIENT_ADDRESSABLE_BAAS_TRIGGER_OR_REASON}} | {{ANON_WRONG_USER_TENANT_READ_WRITE_PROOF_OR_NA}} |
| `S-PAID-API-BUDGET` | `{{REQUIRED_NA_HANDOFF}}` | {{METERED_PROVIDER_TRIGGER_OR_REASON}} | {{PER_USER_GLOBAL_CONCURRENT_BUDGET_PROOF_OR_NA}} |

### Security requirements

| ID | Requirement/control | Family/source | Owner | Negative proof |
| --- | --- | --- | --- | --- |
| `S-01` | {{SECURITY_REQUIREMENT}} | {{BASELINE_OR_HARDENING_FAMILY}} | {{OWNER}} | {{NEGATIVE_TEST_OR_REVIEW}} |

- Secret handling: {{SECRET_POLICY_OR_NA}}
- Data exposure/redaction: {{EXPOSURE_POLICY_OR_NA}}
- Dependency/supply-chain evidence: {{DEPENDENCY_EVIDENCE_OR_NA}}
- AI-input/tool-use boundary: {{AI_BOUNDARY_OR_NA}}
- BaaS policy inventory/RLS/rules evidence: {{BAAS_POLICY_EVIDENCE_OR_NA}}
- Paid-provider quota/circuit-breaker model: {{PAID_API_BUDGET_MODEL_OR_NA}}

## Migration, rollout, and rollback

- Existing compatibility: {{COMPATIBILITY}}
- Migration stages: {{STAGES_OR_NA}}
- Rollout guardrails: {{GUARDRAILS}}
- Rollback trigger/action: {{ROLLBACK}}
- Cleanup: {{CLEANUP_OR_NA}}

## Observability and operations

- Metrics/logs/traces: {{SIGNALS}}
- Sensitive-data exclusions: {{REDACTION}}
- Security/abuse/budget alerts: {{SECURITY_AND_BUDGET_ALERTS_OR_NA}}
- Owner/response: {{OWNER}}

## Testing and verification strategy

| Claim | Evidence category | Critical negative / visual state |
| --- | --- | --- |
| {{CLAIM}} | {{TEST_TYPE}} | {{NEGATIVE_OR_VISUAL_CASE}} |

- Browser E2E required: {{YES_NO_NA_WITH_REASON}}
- Design Review required: {{YES_NO_NA_WITH_REASON}}
- Visual Design Check required/capability: {{YES_NO_UNCHECKABLE_NA_WITH_REASON}}
- G4 source-intent acceptance: {{REQUIRED_NOT_APPLICABLE}}

## Open decisions

- {{OPEN_DECISION_OR_NONE}}

## Self-review

- [ ] No unresolved acceptance-critical placeholder remains.
- [ ] Requirements and interfaces do not contradict each other.
- [ ] Frozen design identity is referenced, not silently redefined, when UI is material.
- [ ] `DESIGN.md` detail is not duplicated into this software specification.
- [ ] Remote actions and permissions are explicit.
- [ ] Failure and rollback behavior are defined.
- [ ] All five automatic security hardening families are `REQUIRED`, `N/A(reason)`, or `HANDOFF`.
- [ ] Every `REQUIRED` hardening family materializes as one or more `S-xx` rows.
- [ ] Security requirements have owner and negative proof.
- [ ] Race-sensitive effects include concurrent/replay proof, not sequential-only evidence.
- [ ] Client-addressable BaaS includes policy/RLS/rules inventory and cross-user/tenant negative proof when applicable.
- [ ] Metered APIs include quota/circuit-breaker/accounting evidence when applicable.
- [ ] Each acceptance outcome has verification path.
- [ ] Design-critical outcomes have a review/visual evidence path or explicit capability gap.
- [ ] Scope can be decomposed into independently reviewable tasks.
