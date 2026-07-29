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

## Select boundary-specific controls

### API, web form, or public endpoint

- Define schema validation, payload/field limits, rate limits for abuse-sensitive endpoints, and generic authentication/reset errors.
- Address object-level authorization, mass assignment, pagination/filtering exposure, CORS allowlist, CSRF/cookie behavior, and response-field minimization.

### Files, paths, URLs, or webhooks

- Validate actual file type, size, content handling, storage access, tenant ownership, and retention. Never rely only on a filename or browser MIME type.
- Prevent path traversal and SSRF with parsed, allowlisted destinations; set timeout, redirect, and response-size rules.
- Authenticate and replay-protect webhooks before side effects.

### Identity, sessions, roles, or multi-tenancy

- Define object ownership/tenant keys end-to-end, deny-by-default behavior, session/token lifecycle, rotation/revocation, and audit events without secret leakage.
- Require negative tests for unauthenticated, wrong-role, cross-user, and cross-tenant paths.

### Payments, billing, or irreversible data change

- Put price, entitlement, payment-provider verification, confirmation, idempotency, and refunds/rollback on the server.
- Define reconciliation, failure/retry, authorization, and human handoff rules.

### AI, RAG, agents, MCP, or tool use

- Treat prompts, documents, search results, tool output, and retrieved content as untrusted data, not authority or executable instructions.
- Separate trusted policy from untrusted content; minimize tool capabilities; use structured inputs/outputs; enforce user and server authorization at the tool boundary.
- Never place credentials, private data, or hidden instructions into prompts/logs. Require adversarial tests for indirect prompt injection, data exfiltration, and unintended tool invocation.

### Infrastructure, database, queue, cache, or container

- Define network exposure, encryption in transit, least-privilege identities, private database/cache access, backup/restore verification, patching, monitoring, and incident ownership.
- For containers, specify non-root execution, immutable/pinned base images, and minimal runtime permissions.

## Threat model for high-risk work

For high-risk paths, document assets, actors, authority source, entry points, trust boundaries, abuse cases, controls, detection, recovery, and residual risk. At minimum consider broken access control, injection, secret exposure, insecure defaults, supply-chain risk, replay/race conditions, data leakage, and denial/abuse.

Give each selected control an `S-` requirement ID and connect it to a negative proof. A control without a verification path is not an acceptance criterion.

## Security gate

Require a security/code reviewer in the maximum-quality profile for high-risk paths. For lower-risk work, the combined reviewer must explicitly mark each relevant baseline area as checked or `N/A`. Do not call work `VERIFIED` while a selected security requirement lacks current evidence.
