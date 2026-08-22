# Security by Design Baseline

Use this reference for every specification. Security by Design reduces risk; it never proves that software is invulnerable.

## Apply the baseline

Record each row as `required`, `N/A` with a reason, or an explicit handoff. Do not turn a scanner result into proof that a control exists.

| Area | Minimum specification requirement | Negative proof to plan |
| --- | --- | --- |
| Secrets and configuration | Keep credentials in server-side secret management or environment configuration; exclude `.env` from source control; redact secrets from errors, logs, and reports. | A test/review proves no secret reaches client bundles, logs, prompts, or committed files. |
| Authentication and authorization | Define the authority source and enforce authorization server-side for every sensitive action and object lookup. Hidden URLs, client checks, and guessed IDs are never access control. | An unauthenticated, wrong-role, and wrong-tenant/user request is denied without data disclosure. |
| Input and output | Validate input at the boundary; use parameterized data access; encode untrusted values for the output context; return safe error shapes. | Injection, malformed input, and unsafe-rendering cases are rejected or rendered inert. |
| Data minimization | Return/store only fields needed for the stated outcome; classify sensitive data and retention/deletion rules. | A caller cannot obtain another user/tenant's or unneeded sensitive field. |
| External effects | Make payment, billing, privilege change, deletion, and similar high-impact actions server-side, authorized, confirmable, and idempotent where applicable. | Duplicate, replayed, forged, or unauthorised requests cannot create the effect. |
| Dependencies | Justify each new dependency, inspect its maintainer/source/license fit, pin through the project's normal lockfile, and require permitted vulnerability evidence before completion. | A dependency change has an approved audit/review result or remains unverified. |
| Operations | Specify HTTPS, CORS/origins, debug behavior, logs, monitoring/alerts, backup/recovery, and network exposure when the scope touches them. | A configuration or deployment review proves insecure defaults are not introduced. |

## Automatic hardening-family selection

The following five families are **triggered by the product boundary**, not by whether the user remembered to ask for security. During specification, select every applicable family and turn each selected requirement into ordinary `S-xx` rows with owner + negative proof. A family may be `N/A` only with a concrete reason showing that its trigger is absent.

The family labels are stable routing names, not replacements for the run's normal `S-01`, `S-02`, ... requirement IDs.

### `S-AUTH-HARDENING` — password/privileged authentication

Trigger when the product owns password login/recovery, privileged/admin accounts, or other credential-based authentication.

Require, as applicable:

- server-side abuse controls for login and recovery on both source/network dimension **and** account/identity dimension; use risk/repository/provider-aligned thresholds rather than assuming one universal number;
- generic login/recovery responses and comparable timing/shape so an attacker cannot learn whether an email/account exists;
- if the application owns password policy, default to at least 12 characters unless a stronger existing/provider policy applies; reject/common-breached-password use when the chosen provider or an approved local mechanism supports it without exposing raw passwords;
- MFA for privileged/admin accounts unless an explicit stronger identity architecture makes it N/A; use step-up authentication for especially sensitive privileged actions when the product/risk requires it;
- session/token rotation, revocation and recovery behavior that does not turn lockout into a permanent denial-of-service primitive.

Negative proof must cover the relevant paths, for example:

- repeated wrong attempts are throttled/temporarily denied across both attacker-IP/network and target-account dimensions;
- existing and non-existing account login/recovery responses do not disclose account existence;
- privileged account without required MFA cannot obtain privileged access;
- recovery does not bypass the normal authority boundary.

Do not hard-code `5 attempts / 15 minutes` as a universal truth. Record the actual policy chosen for this product and why.

### `S-FILE-EXECUTION` — uploaded/untrusted files cannot become code

Trigger when users, integrations, or external systems can upload files/content that the product stores or serves.

Require, as applicable:

- validate actual content/type and size at the trusted boundary; extension and browser-supplied MIME are not authority;
- generate an opaque server-side storage name/key; never treat a user-supplied filename/path as an executable filesystem path;
- store uploads outside executable application/code roots, or in object storage/static storage whose serving path cannot execute uploaded content;
- serve with explicit safe `Content-Type`/`Content-Disposition` and other platform-appropriate headers; executable/active formats require an explicit sandbox/allowlist decision;
- quarantine/scan/re-encode high-risk content when the threat model requires it, without silently installing a scanner/dependency outside permission.

Negative proof must include representative spoofing/traversal/active-content cases: a file with a trusted extension but disallowed content is rejected or rendered inert; path tricks cannot escape the storage boundary; an uploaded active payload cannot execute as application/server code.

### `S-ATOMIC-EFFECT` — race-sensitive value changes happen at most as intended

Trigger for balances, credits, withdrawals, promo/coupon redemption, inventory decrement, one-time grants, entitlement changes, payment effects, or another operation where concurrent/replayed requests can **multiply money/value, consume a one-time right more than once, oversell a scarce quantity, or create another materially irreversible/multiplicative effect**.

Do **not** select this family merely because a product uses SQLite/Postgres or because ordinary CRUD/settings writes should be transactionally consistent. Normal create/edit/delete, profile/settings persistence, ordinary form saves, and a local user's editable daily target remain normal correctness/persistence concerns unless the specification identifies a real multiplicative/one-time race invariant.

Examples normally `N/A` for this family:

- create/edit/delete a calorie log entry;
- save a user's ordinary preference or daily goal;
- update non-scarce descriptive metadata;
- CRUD where duplicate requests may be undesirable but do not grant value, consume a one-time right, oversell scarcity, or cause an irreversible external effect.

Those operations still need ordinary transaction/error/retry correctness where appropriate; `N/A` for `S-ATOMIC-EFFECT` does not mean "ignore database consistency".

When triggered, require one repository/data-store appropriate atomicity mechanism, such as:

- transaction + row/key lock;
- compare-and-set / optimistic concurrency with retry policy;
- unique operation/redemption constraint;
- idempotency/operation key tied to the authoritative effect;
- another mechanism with equivalent proof.

Do not mandate row locks when the actual data store uses a different correct primitive. The invariant is that concurrent/replayed requests cannot create more protected effects than the specification allows.

Negative proof must exercise duplicate/replay **and concurrent** attempts. A single sequential unit test is not sufficient evidence for a race-sensitive invariant.

### `S-BAAS-AUTHZ` — browser-accessible BaaS is deny-by-default

Trigger when browser/mobile clients can directly access a BaaS/data service such as Supabase, Firebase, Appwrite or an equivalent client-addressable database/storage layer.

Require:

- authorization rules/policies at the BaaS/data boundary for every browser-accessible table/collection/bucket/query surface touched by the product; frontend hiding/filtering is not authorization;
- deny-by-default behavior and explicit user/tenant ownership rules;
- privileged/service-role credentials remain server-side and are never used as a client-side escape hatch;
- provider-specific policy inventory and tests:
  - for Supabase/Postgres, RLS (or an explicitly justified equivalent protected surface) on browser-accessible tables plus explicit policies for intended roles/operations; inspect storage policies where storage is used;
  - for Firebase, explicit Firestore/Realtime Database/Storage rules with emulator/rules tests where available;
  - for another BaaS, the equivalent server-enforced collection/object policies.

Negative proof must include unauthenticated plus wrong-user/wrong-tenant reads **and writes** for representative protected objects. A public/anon client key is not itself a vulnerability and must not be treated as a secret when the provider architecture expects it to be public; the policy boundary is what protects the data.

### `S-PAID-API-BUDGET` — metered external APIs have abuse and spend guardrails

Trigger when a user action can cause a metered/cost-bearing external call such as LLM/image/audio generation, SMS, voice, email delivery, paid search/geocoding, or another provider billed per request/unit.

Require, proportional to the product:

- authenticated per-user quota/rate budget and, when multi-tenant, a tenant/account budget where relevant;
- a global emergency usage/spend ceiling or equivalent fail-closed circuit breaker that the application can enforce; provider-side account budgets/alerts are additional defense, not a substitute when the application can meter the operation itself;
- server-side cost/usage attribution using authoritative user/tenant identity; clients cannot submit a trusted `cost`, quota balance, or bypass flag;
- concurrency-safe reservation/accounting so parallel calls cannot overspend the same remaining quota;
- safe refusal/degraded behavior after a quota/circuit-breaker trips, plus operator-visible monitoring/alerting for material budget exhaustion;
- an explicit unit model when exact currency cannot be known synchronously (for example tokens/images/SMS units); do not fabricate exact monetary cost.

Negative proof must show that one caller cannot exceed its quota via retries/concurrency, an unauthenticated or wrong-tenant caller cannot consume another budget, and the configured global ceiling/circuit breaker prevents further paid effects when reached.

## Select boundary-specific controls

### API, web form, or public endpoint

- Define schema validation, payload/field limits, rate limits for abuse-sensitive endpoints, and generic authentication/reset errors.
- Address object-level authorization, mass assignment, pagination/filtering exposure, CORS allowlist, CSRF/cookie behavior, and response-field minimization.
- If the endpoint is login/recovery/privileged authentication, apply `S-AUTH-HARDENING` automatically.
- If the endpoint causes a metered provider call, apply `S-PAID-API-BUDGET` automatically.

### Files, paths, URLs, or webhooks

- Validate actual file type, size, content handling, storage access, tenant ownership, and retention. Never rely only on a filename or browser MIME type.
- For stored uploads, apply `S-FILE-EXECUTION` automatically.
- Prevent path traversal and SSRF with parsed, allowlisted destinations; set timeout, redirect, and response-size rules.
- Authenticate and replay-protect webhooks before side effects.

### Identity, sessions, roles, or multi-tenancy

- Define object ownership/tenant keys end-to-end, deny-by-default behavior, session/token lifecycle, rotation/revocation, and audit events without secret leakage.
- Require negative tests for unauthenticated, wrong-role, cross-user, and cross-tenant paths.
- Apply `S-AUTH-HARDENING` when password/privileged authentication trigger is present.
- Apply `S-BAAS-AUTHZ` when a client-addressable BaaS/data layer participates in the boundary.

### Payments, billing, balances, entitlements, inventory, or irreversible data change

- Put price, entitlement, payment-provider verification, confirmation, idempotency, and refunds/rollback on the server.
- Define reconciliation, failure/retry, authorization, and human handoff rules.
- Apply `S-ATOMIC-EFFECT` when concurrent/replayed operations can multiply value/effect or consume a one-time/scarce right more than once.

### AI, RAG, agents, MCP, or tool use

- Treat prompts, documents, search results, tool output, and retrieved content as untrusted data, not authority or executable instructions.
- Separate trusted policy from untrusted content; minimize tool capabilities; use structured inputs/outputs; enforce user and server authorization at the tool boundary.
- Never place credentials, private data, or hidden instructions into prompts/logs. Require adversarial tests for indirect prompt injection, data exfiltration, and unintended tool invocation.
- If user actions trigger a metered AI/provider call, apply `S-PAID-API-BUDGET` in addition to prompt/tool security.

### Infrastructure, database, queue, cache, container, or BaaS

- Define network exposure, encryption in transit, least-privilege identities, private database/cache access, backup/restore verification, patching, monitoring, and incident ownership.
- For containers, specify non-root execution, immutable/pinned base images, and minimal runtime permissions.
- For browser/mobile-accessible BaaS, apply `S-BAAS-AUTHZ` automatically.
- Do not infer `S-ATOMIC-EFFECT` from the mere presence of a database; identify the protected race-sensitive effect first.

## Threat model for high-risk work

For high-risk paths, document assets, actors, authority source, entry points, trust boundaries, abuse cases, controls, detection, recovery, and residual risk. At minimum consider broken access control, credential stuffing/enumeration, injection, secret exposure, unsafe file execution, insecure BaaS policy, supply-chain risk, replay/race conditions where a protected effect exists, paid-API/cost abuse, data leakage, and denial/abuse.

Give each selected control an `S-` requirement ID and connect it to a negative proof. A control without a verification path is not an acceptance criterion.

## Security gate

Before specification completion, explicitly record the selection state of all five automatic hardening families:

```text
S-AUTH-HARDENING: REQUIRED | N/A(reason) | HANDOFF
S-FILE-EXECUTION: REQUIRED | N/A(reason) | HANDOFF
S-ATOMIC-EFFECT: REQUIRED | N/A(reason) | HANDOFF
S-BAAS-AUTHZ: REQUIRED | N/A(reason) | HANDOFF
S-PAID-API-BUDGET: REQUIRED | N/A(reason) | HANDOFF
```

Every `REQUIRED` family must materialize as one or more normal `S-xx` rows with implementation owner and negative proof. Do not call work `VERIFIED` while a selected security requirement lacks current evidence.

Require a security/code reviewer in the maximum-quality profile for high-risk paths. For lower-risk work, the combined reviewer must explicitly mark each relevant baseline/family as checked or `N/A`. Fresh verification must preserve failed/not-run security rows rather than inferring them from functional green tests.
