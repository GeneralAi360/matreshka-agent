# Matreshka Agent 0.5 — 15 Vibecoding Security Failure Classes

- Date: `2026-08-21`
- Branch: `dev/0.5-brief-traceability-observability`
- Status: `IMPLEMENTED_PENDING_NATIVE_VALIDATION`
- Scope: security-design protection against the 15 common failure classes supplied by the project owner
- Release policy: this audit does not authorize a `0.5.0` release claim

## Result

The existing Security-by-Design baseline already covered most of the 15 classes through `S-xx` requirements + negative proofs. This hardening pass made the five previously implicit/partial boundaries explicit and automatic.

| # | Failure class | Matreshka 0.5 protection after hardening |
| --- | --- | --- |
| 1 | brute-force login | `S-AUTH-HARDENING`: authoritative source+account abuse throttling + negative proof |
| 2 | credential stuffing / weak password / privileged auth | `S-AUTH-HARDENING`: app-owned password baseline, non-enumeration, privileged MFA/step-up where applicable |
| 3 | secrets exposed in client/Git | baseline Secrets/configuration + server-side secret boundary + negative proof |
| 4 | IDOR/object ownership | baseline Authentication/authorization + wrong-user/wrong-tenant negative tests |
| 5 | admin UI hidden but API unprotected | server-side role/action authorization; client hiding is never access control |
| 6 | SQL injection | boundary validation + parameterized data access + injection negative proof |
| 7 | forged/replayed payment webhook | authenticated/replay-protected webhook + server-side provider verification/idempotency |
| 8 | unsafe/vulnerable dependency | dependency source/maintainer/license/lockfile/vulnerability evidence |
| 9 | stored/reflected XSS | output-context encoding + unsafe-rendering negative proof |
| 10 | permissive CORS | origin allowlist + cookie/CSRF policy + operations/config review |
| 11 | executable upload | `S-FILE-EXECUTION`: content/type/size, generated key, non-executable storage/serving boundary |
| 12 | race/double effect | `S-ATOMIC-EFFECT`: transaction/lock/CAS/unique/idempotency equivalent + concurrent/replay proof |
| 13 | Supabase/Firebase/BaaS without provider-side policy | `S-BAAS-AUTHZ`: RLS/rules/equivalent policy inventory + cross-user/tenant read/write proof |
| 14 | paid API cost abuse | `S-PAID-API-BUDGET`: per-caller quota + global fail-closed ceiling/circuit breaker + concurrency-safe accounting |
| 15 | prompt injection / tool injection | AI/tool trust-boundary baseline + least capability + adversarial indirect-injection/exfiltration/tool-use tests |

## Automatic selection contract

Every specification now records:

```text
S-AUTH-HARDENING: REQUIRED | N/A(reason) | HANDOFF
S-FILE-EXECUTION: REQUIRED | N/A(reason) | HANDOFF
S-ATOMIC-EFFECT: REQUIRED | N/A(reason) | HANDOFF
S-BAAS-AUTHZ: REQUIRED | N/A(reason) | HANDOFF
S-PAID-API-BUDGET: REQUIRED | N/A(reason) | HANDOFF
```

`REQUIRED` does not itself satisfy security. It must materialize as one or more ordinary `S-xx` rows with:

```text
requirement/control
+ implementation owner
+ negative proof
+ review ownership
+ fresh verification result
```

The five family names are routing labels only. The existing Matreshka `S-xx` machinery remains the evidence contract.

## Important design choices

### Auth thresholds are explicit policy, not copied folklore

The baseline requires source/network + account/identity throttling but does not pretend `5 attempts / 15 minutes` is universally correct. The specification records the actual repository/provider/product policy and its evidence.

### Public BaaS keys are not automatically called secrets

For architectures such as Supabase/Firebase, a public client/anon key can be expected. The security boundary is provider-side authorization policy. Matreshka therefore checks RLS/rules/ownership rather than giving a false sense of safety by merely hiding a public key.

### Atomicity is invariant-based, not database-brand based

`S-ATOMIC-EFFECT` does not always demand a row lock. Transaction+lock, optimistic CAS, unique operation constraints, idempotency keys or equivalent mechanisms are valid when they prove the product invariant.

### Paid API budgets separate usage from fabricated money

When exact provider currency cost cannot be known synchronously, Matreshka may enforce tokens/images/SMS/provider units. It must not fabricate exact cost. A configured app-side global circuit breaker plus provider-side budget/alerts is stronger than either alone.

### Upload scanning is not silently installed

High-risk files may require scanner/quarantine/re-encoding, but a security requirement cannot silently grant dependency/network/tool authority. Missing approved capability becomes an explicit handoff/blocker.

## Cross-skill path

```text
security-by-design.md
↓ automatic family selection
specification-template.md
↓ REQUIRED family → S-xx rows
planning-software-work
↓ S-xx → task + negative proof owner
implementing-with-tests
↓ implement authoritative control + focused negative evidence
reviewing-agent-work
↓ independent security review + five-family checklist
verifying-development-work
↓ fresh required negative-proof rows
COMPLETE only if selected security evidence is current
```

Functional green does not override a failed/missing security proof.

## Eval and CI guard

Added:

```text
plugins/matreshka-agent/evals/security-hardening-evals.json
plugins/matreshka-agent/scripts/check_security_hardening.py
```

The eval matrix contains ten scenarios across specification, implementation, review and verification, including auth enumeration/MFA, executable upload, concurrent promo/balance effects, Supabase RLS/cross-tenant access and concurrent paid-API quota bypass.

The deterministic checker requires:

- all five family definitions;
- the specification selection table;
- explicit reviewer checks;
- existing `S-xx` implementation/review/verification wiring;
- all required security eval IDs;
- a live CI step for `check_security_hardening.py`.

## Evidence boundary

This pass establishes `PRESENT + WIRED + COVERED` for the five new hardening families. It does **not** claim every future application is secure and does not replace application-specific threat modeling.

Before `0.5.0`, native full-stack acceptance should deliberately exercise at least representative triggered families (for example password/admin auth, a Supabase-style protected data boundary, race-sensitive effect, and metered provider request) and preserve exact negative evidence.
