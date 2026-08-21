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
- For every selected `S-xx`, inspect the implementation boundary **and** the planned negative proof; functional green alone cannot satisfy a security row.

### Five automatic hardening families

When the specification marks one of these families `REQUIRED`, treat the corresponding invariant as a first-class security review concern. If the trigger is visibly present but the specification marked the family `N/A` without a valid reason, raise a specification/security finding rather than silently accepting the omission.

#### `S-AUTH-HARDENING`

For password login/recovery or privileged/admin access, check:

- abuse controls cover both attacker source/network and target account/identity dimensions;
- login/recovery errors do not enumerate whether an account exists;
- application-owned password policy follows the accepted minimum/strength/provider policy;
- privileged/admin MFA or explicitly justified stronger equivalent is enforced at the authoritative identity boundary;
- lockout/backoff/recovery does not create an obvious permanent account-denial primitive.

A frontend-only disabled button/countdown is not rate limiting or MFA enforcement.

#### `S-FILE-EXECUTION`

For stored uploads, check:

- actual content/type + size validation occurs at the trusted boundary;
- storage names/keys are generated server-side rather than trusted from user path/filename;
- uploaded content cannot land in an executable application/code directory or equivalent execution surface;
- serving headers/disposition make untrusted active content inert unless an explicit sandboxed active-content design exists;
- path traversal and tenant/storage ownership are enforced.

A `.png` suffix or browser MIME value is not sufficient evidence.

#### `S-ATOMIC-EFFECT`

For balances, credits, promo redemption, inventory, withdrawals, one-time grants, entitlements and similar race-sensitive effects, check:

- an actual datastore-appropriate atomicity primitive exists (transaction/lock/CAS/unique constraint/idempotency or equivalent);
- the operation has authoritative identity/uniqueness semantics;
- duplicate/replay **and concurrent** attempts are covered;
- partial failure/retry cannot multiply the protected effect.

Sequential-only tests are insufficient for a concurrency invariant.

#### `S-BAAS-AUTHZ`

For browser/mobile-addressable Supabase/Firebase/Appwrite/equivalent data/storage:

- frontend filtering/hiding is not treated as authorization;
- every touched browser-accessible table/collection/bucket has provider-side deny-by-default ownership policy;
- privileged/service-role credentials remain server-only;
- Supabase/Postgres surfaces have appropriate RLS/policies (or explicitly justified protected equivalent); Firebase surfaces have explicit rules; equivalent providers have equivalent policies;
- unauthenticated, wrong-user and cross-tenant read **and write** negative cases exist.

A public/anon provider key may be intentionally public; the security question is whether the provider-side policies protect the data.

#### `S-PAID-API-BUDGET`

For metered external providers, check:

- per-user and relevant tenant/account quota is enforced server-side;
- a global emergency usage/spend ceiling or equivalent fail-closed circuit breaker exists where application-side metering is possible;
- cost/usage attribution uses authoritative identity, not client-submitted cost/quota state;
- budget reservation/accounting is concurrency-safe;
- exhausted quota/circuit breaker fails safely and emits appropriate operator-visible signal;
- exact money is not fabricated when only usage units are knowable.

Provider billing alerts alone are not an application abuse boundary.

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
- For selected security families, confirm the negative proof actually attacks the invariant: enumeration/abuse, active upload/path, concurrent duplicate effect, cross-tenant BaaS read/write, or quota/global-budget bypass as applicable.

### Maintainability and user impact

- Check repository patterns, public naming, error messages, accessibility, and observability only where relevant.
- Raise complexity only when it creates a concrete correctness, security, or support risk.

## Assign severity consistently

### Critical

Use when progression could cause unauthorized access, cross-tenant exposure, secret disclosure, executable untrusted upload, destructive data loss, duplicated money/value effect, payment or production harm, uncontrolled metered-provider spend, or another readily exploitable security failure. State the exploit or failure path and affected asset.

### Important

Use when the task fails an acceptance criterion, introduces a likely regression, violates a public contract, lacks necessary error handling, or leaves a material security/test gap. State the user-visible or operational consequence.

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
