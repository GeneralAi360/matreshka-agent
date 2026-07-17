# Review report — `<task ID and title>`

## Decision

`<APPROVED | CHANGES_REQUIRED | REVIEW_BLOCKED | STOP_AND_RESCOPE>`

- Reviewed baseline/current state: `<refs or hashes>`
- Reviewed files/diff range: `<exact scope>`
- Review integrity: `<technical read-only | immutable package | DEGRADED_MODE reason>`
- Evidence relied on: `<commands/state>`
- Checks rerun: `<focused checks and reason, or none>`
- Completed review scope: `<criteria and owned concerns checked>`
- Incomplete review scope: `<unreviewed required concern or none>`
- Product/test files changed: `none`
- Pre-existing failures or dirty files: `<list or none>`

## Blocking findings

### `<ID>` — `<Critical | Important>` — `<short title>`

- Location: `<file:line or contract boundary>`
- Evidence: `<observable fact>`
- Impact: `<security, user, data, or acceptance consequence>`
- Acceptance/invariant: `<violated requirement>`
- Required condition: `<minimum outcome needed>`
- Confidence/counterevidence: `<assessment>`

## Minor findings

- `<ID / location / evidence / improvement>`

## Adjacent findings

- `RECORD_FOR_FUTURE_TASK: <issue and evidence>`

## Coverage summary

| Acceptance or risk | Diff/evidence checked | Result |
| --- | --- | --- |
| `<criterion>` | `<location or command>` | `<pass/fail/unknown>` |

## Review dimensions

| Dimension | Result | Evidence or N/A reason |
| --- | --- | --- |
| Specification/correctness | `<checked/N/A>` | `<evidence or reason>` |
| Public contract/compatibility | `<checked/N/A>` | `<evidence or reason>` |
| Input validation/error/side effects | `<checked/N/A>` | `<evidence or reason>` |
| Authorization/isolation/leakage/secrets | `<checked/N/A>` | `<evidence or reason>` |
| Concurrency/retry/idempotency | `<checked/N/A>` | `<evidence or reason>` |
| Persistence/migration/rollback | `<checked/N/A>` | `<evidence or reason>` |
| Test sufficiency | `<checked/N/A>` | `<evidence or reason>` |
| Maintainability | `<checked/N/A>` | `<evidence or reason>` |
| UX/accessibility | `<checked/N/A>` | `<evidence or reason>` |

## Controller handoff

- Confirmed findings for consolidated fix: `<IDs or none>`
- Disputed findings needing adjudication: `<IDs or none>`
- Assumptions: `<list or none>`
- Concerns and evidence limitations: `<list or none>`
- Permissions or evidence still needed: `<list or none>`
- Exact next action: `<single controller action>`
