# Implementation report — `<task ID and title>`

## Status

- Result: `<COMPLETE | PARTIALLY_VERIFIED | BLOCKED | SPLIT_REQUIRED | STOP_AND_RESCOPE | HANDOFF_REQUIRED>`
- Project root: `<resolved root or NO_GIT_MODE>`
- Baseline/current state: `<refs or hashes>`
- Permission envelope used: `<scope and expiry>`

## Scope

- Completed: `<acceptance results>`
- Not completed: `<remaining results>`
- Changed files: `<exact paths>`
- Pre-existing dirty files left untouched: `<paths or none>`

## Focused cycle

### RED

- Command: `<command>`
- State: `<baseline or current ref/hash>`
- Exit code: `<code>`
- Counts: `<passed / failed / skipped>`
- Expected failure reason: `<reason>`

### GREEN

- Command: `<same focused command>`
- State: `<current ref/hash>`
- Exit code: `<code>`
- Counts: `<passed / failed / skipped>`
- Relevant note: `<what now works>`

### Exception, if any

- Reason: `<why executable RED was unavailable>`
- Alternate check: `<check and result>`
- Remaining verifier: `<operator or none>`

## Task gate

| Command | State | Exit code | Counts | Relevant note |
| --- | --- | ---: | --- | --- |
| `<focused suite>` | `<ref/hash>` | `<code>` | `<counts>` | `<note>` |
| `<nearby regression>` | `<ref/hash>` | `<code>` | `<counts>` | `<note>` |
| `<targeted static/diff check>` | `<ref/hash>` | `<code>` | `<counts>` | `<note>` |

## Handoff

- Assumptions: `<list or none>`
- Pre-existing failures: `<evidence or none>`
- Adjacent findings: `<RECORD_FOR_FUTURE_TASK items or none>`
- Permissions still required: `<actions or none>`
- Concerns: `<list or none>`
- Exact next action: `<controller action>`
