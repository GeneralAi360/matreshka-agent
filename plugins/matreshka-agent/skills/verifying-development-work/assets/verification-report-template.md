# Verification report — <task, phase, or branch>

## Verdict

- Status: `<VERIFIED | PARTIALLY_VERIFIED | FAILED | BLOCKED | HANDOFF_REQUIRED>`
- Verified state: `<project root and exact ref/hashes>`
- Verification tier: `<focused | task gate | phase/final>`
- Permission envelope used: `<scope and expiry>`
- Review blockers: `<none or unresolved IDs>`
- Completed verification scope: `<criteria proved>`
- Incomplete verification scope: `<criteria not proved or none>`
- Product/test files changed: `none`
- Paths or diff range verified: `<exact scope>`
- Progress reconciliation: `<MATCH | MISMATCH | NOT_APPLICABLE; progress / ledger / repository / fresh evidence summary>`
- Unresolved acceptance-critical placeholders: `<items and affected criteria, or none>`
- Assumption status: `<confirmed / optional documented / acceptance-critical unresolved>`
- Required security negative proofs: `<proved / failed / not run rows>`
- Exact non-complete verdict reason: `<required when status is not VERIFIED, or none>`

## Acceptance matrix

| Claim | Verification | Exit code/counts | Result | Relevant note |
| --- | --- | --- | --- | --- |
| `<criterion>` | `<command or interaction>` | `<code; pass/fail/skip>` | `<proved/failed/unverified>` | `<note>` |

## State integrity

- State before checks: `<status/hashes>`
- State after checks: `<status/hashes>`
- Unexpected generated changes: `<paths or none>`
- Pre-existing dirty files preserved: `<paths or none>`

## Progress and placeholder truth

| Item | Source | Acceptance impact | Current evidence | Resolution owner/status |
| --- | --- | --- | --- | --- |
| `<progress mismatch, assumption, placeholder, or provider fact>` | `<progress / ledger / repository / specification>` | `<critical / optional>` | `<observable evidence>` | `<controller / user / external operator; status>` |

## Failure attribution

| Failure | Current evidence | Baseline evidence | Attribution |
| --- | --- | --- | --- |
| `<failure>` | `<result>` | `<result or unavailable>` | `<task-owned/pre-existing/unresolved/environment>` |

## Gaps and handoff

- Skipped or unavailable checks: `<list and reason>`
- Unverified claims: `<list or none>`
- External verification: `<operator / target / action / expected result / stop policy>`
- Assumptions: `<list or none>`
- Concerns and evidence limitations: `<list or none>`
- Permissions still required: `<list or none>`
- Exact next action: `<single controller action>`
