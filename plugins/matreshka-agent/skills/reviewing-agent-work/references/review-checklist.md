# Review checklist and severity guide

## Validate the package

Confirm before substantive review:

- task goal and acceptance criteria are explicit;
- allowed and non-goal scope are known;
- baseline and current state identify the exact diff;
- all task-owned untracked files are included;
- implementer evidence identifies commands, exit codes, counts, and state;
- pre-existing dirty files and failures are separated;
- the review environment is technically read-only or protected by immutable artifacts and integrity checks.

Return `REVIEW_BLOCKED` when missing information could materially change the decision.

## Review by risk, not by checklist volume

### Specification and behavior

- Map each acceptance criterion to code and evidence.
- Check boundary inputs, outputs, error states, defaults, and compatibility.
- Look for behavior that passes the focused example but violates the broader contract.
- Confirm non-goals remain untouched.

### Security and isolation

- Verify authentication and authorization at the authoritative boundary.
- Verify tenant or organization identity cannot be selected by untrusted input when a trusted source should control it.
- Trace sensitive values through logs, errors, reports, caches, and provider payloads.
- Check validation before side effects.
- Check least privilege, deny-by-default behavior, and failure paths.
- Inspect secret references without requesting or reproducing secret values.

### State and distributed behavior

- Check transaction boundaries and partial failures.
- Check retry safety, idempotency keys, duplicate execution, timeout behavior, and concurrency.
- Check migration ordering, compatibility window, rollback assumptions, and existing data.
- Check persistence ownership and cross-tenant uniqueness.

### Tests and evidence

- Confirm RED failed for the intended missing behavior.
- Confirm GREEN and nearby regressions match the current state.
- Check that tests would fail for plausible broken implementations.
- Reject assertions tied only to private implementation details unless required.
- Identify skipped acceptance criteria and contradictory evidence.

### Maintainability and user impact

- Check repository patterns, public naming, error messages, accessibility, and observability only where relevant.
- Raise complexity only when it creates a concrete correctness, security, or support risk.

## Assign severity consistently

### Critical

Use when progression could cause unauthorized access, cross-tenant exposure, secret disclosure, destructive data loss, payment or production harm, or a readily exploitable security failure. State the exploit or failure path and affected asset.

### Important

Use when the task fails an acceptance criterion, introduces a likely regression, violates a public contract, lacks necessary error handling, or leaves a material test gap. State the user-visible or operational consequence.

### Minor

Use for a concrete improvement that is safe to defer and does not violate acceptance criteria. Do not block approval for Minor-only findings; list them separately.

## Require finding quality

Reject a proposed finding when it lacks a demonstrable location, impact, or relation to the task. Before keeping a finding, ask:

1. What exact behavior or invariant is wrong?
2. What evidence proves it in the reviewed state?
3. What realistic impact follows?
4. Does existing code or evidence contradict the claim?
5. Is the issue task-owned or adjacent?
6. What minimum condition would resolve it without prescribing unnecessary implementation?

## Re-review narrowly

For each confirmed finding, inspect the original location, fix diff, covering test, and one nearest regression when relevant. Preserve the original severity unless new evidence changes the impact. Do not turn re-review into a fresh whole-diff review.
