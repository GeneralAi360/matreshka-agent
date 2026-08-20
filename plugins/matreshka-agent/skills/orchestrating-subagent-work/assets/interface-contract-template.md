# Interface Contract {{IC_ID}} — {{TITLE}}

- Status: `{{DRAFT_FROZEN_CHANGED_VERIFIED}}`
- Run ID: `{{RUN_ID}}`
- Source requirements: {{U_AND_S_IDS}}
- Producer area: `{{PRODUCER_AREA}}`
- Consumer areas: {{CONSUMER_AREAS}}
- Contract identity/hash: `{{IDENTITY_HASH}}`
- Frozen for dependent dispatch at: `{{TIMESTAMP_OR_PENDING}}`

## Purpose

{{ONE_SENTENCE_SEAM_PURPOSE}}

## Input / request / event

```text
{{INPUT_SHAPE}}
```

- Validation: {{VALIDATION}}
- Auth/authorization: {{AUTH_BOUNDARY_OR_NA}}
- Data classification/minimization: {{DATA_BOUNDARY_OR_NA}}

## Output / response / event

```text
{{OUTPUT_SHAPE}}
```

## Failure semantics

| Condition | Observable result | Consumer behavior |
| --- | --- | --- |
| {{FAILURE}} | {{ERROR_STATUS_EVENT}} | {{EXPECTED_CONSUMER_BEHAVIOR}} |

## Delivery semantics

- Ordering: {{ORDERING_OR_NA}}
- Idempotency: {{IDEMPOTENCY_OR_NA}}
- Retry/timeout: {{RETRY_TIMEOUT_OR_NA}}
- Transaction/atomicity boundary: {{ATOMICITY_OR_NA}}

## Compatibility

- Current version/shape: {{VERSION_OR_UNVERSIONED}}
- Backward compatibility: {{RULE}}
- Deprecation/migration: {{RULE_OR_NA}}

## Producer obligations

- {{OBLIGATION}}

## Consumer obligations

- {{OBLIGATION}}

## Proof

- Producer-focused check: `{{COMMAND_OR_CHECK}}`
- Consumer-focused check: `{{COMMAND_OR_CHECK}}`
- Integration/contract proof: `{{COMMAND_OR_CHECK}}`
- Negative/security proof: {{CHECK_OR_NA}}

## Change rule

After this contract is frozen for a dependent task, a material change requires controller reconciliation of affected tasks, context sets, tests, review, verification, and documentation impact before dependent implementation continues.

This contract is coordination state. It does not grant product writes, commands, Git, network, secrets, provider, browser, process, database, migration, deploy, destructive, or remote authority.
