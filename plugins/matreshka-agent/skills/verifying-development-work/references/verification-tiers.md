# Verification tiers and evidence rules

## Convert acceptance into a matrix

Use one row per independently observable claim:

| Claim | Risk | Current-state check | Required evidence | Result |
| --- | --- | --- | --- | --- |
| `<criterion>` | `<low/medium/high>` | `<command or inspection>` | `<exit/counts/observable state>` | `<pending>` |

Do not merge unrelated claims into a vague row such as “all tests pass.” Include negative behavior and failure semantics when the acceptance contract requires them.

## Focused tier

Use after a narrow implementation or fixer-wave:

- the exact covering test;
- one nearest regression when relevant;
- a targeted static check only when it can invalidate the claim.

Use this tier to prove the local behavior, not completion of an entire phase.

## Task-gate tier

Use before marking an independently reviewable task complete:

- focused task suite;
- one to three nearest regression suites;
- targeted typecheck, lint, schema validation, or compile check;
- diff/whitespace validation when Git tooling or repository policy provides it;
- a build only when the changed path participates in build behavior;
- targeted security or secret checks for affected boundaries.

Select commands from repository instructions, package scripts, CI configuration, and existing patterns. Do not invent a command and report success without confirming it exists.

## Phase/final tier

Use once at a meaningful integration boundary:

- affected integration or end-to-end suites;
- the project build or packaging check;
- broader typecheck/lint/test suites required by policy;
- migration compatibility, rollback preparation, or provider contract checks when relevant;
- release-specific scans or validation.

Avoid repeating this tier after every small task. A full suite can still miss the exact acceptance behavior, so retain the targeted rows.

## Judge freshness

Evidence is current only when it identifies the exact state being claimed. Record a commit/ref when available or scoped file hashes/current-state identity in uncommitted or no-Git mode.

Accept remote CI evidence only when:

1. the job ran on the exact claimed state;
2. the workflow and relevant configuration match;
3. the result is recent enough for the run;
4. the job actually covers the criterion;
5. no later local change invalidates it.

## Interpret exit status and counts

Exit code zero is necessary but not always sufficient. Confirm that expected tests or checks actually ran. A filtered command that selects zero tests does not prove behavior. Record skipped tests when their scope matters.

When tooling does not provide counts, state `counts unavailable` and record the specific success signal. Do not fabricate counts.

## Verify non-test claims

Use the strongest permitted observable method:

- static schema or config validation;
- build or parser output;
- rendered UI inspection or accessibility check;
- local emulator interaction;
- deterministic artifact comparison;
- prepared external operator procedure.

If the final proof requires remote production or staging access outside the permission envelope, mark the criterion pending and return `HANDOFF_REQUIRED` with the exact target, operator, safe command or interaction, expected result, and rollback/stop condition.

## Handle pre-existing failures safely

Prefer an existing isolated baseline, prior immutable CI run, or controller-provided clean artifact. Never reset the active checkout or discard user work for comparison.

Record both outcomes with the same command and comparable environment. If comparison is impossible, mark attribution unresolved and keep the affected criterion unverified.
