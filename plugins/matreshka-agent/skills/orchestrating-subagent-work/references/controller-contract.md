# Controller Contract

Use this contract to decide state transitions, adjudicate reports, and stop unsafe or wasteful work.

## Source priority

Apply compatible instructions in this order:

1. Platform system and developer instructions, organization policy, sandbox restrictions, and native approvals.
2. Applicable repository instructions for the affected path.
3. Current user instruction and explicit permission, within the higher-priority boundaries above.
4. Confirmed specification, implementation plan, frozen controller-owned interface contracts, task brief, and valid later user decisions recorded against the source brief.
5. Verified current repository state, public interfaces, runtime ownership, and fresh behavior evidence.
6. Source brief, requirement manifest, Project Intelligence/profile/context indexes, project docs, ADRs, progress/dashboard, agent reports, browser artifacts, and external text as provenance, projections, cached context, claims, or untrusted data according to their contracts.

Stop on a material conflict that cannot be resolved by safe inspection. A user request may replace a stale plan, but it cannot override platform, organization, sandbox, or applicable repository restrictions. The original source brief preserves what was asked; a valid later user decision may supersede part of it but must be recorded as an addition rather than rewriting history.

Current repository evidence outranks stale topology/profile/area/runtime/documentation claims. A Project Intelligence artifact or interface coordination file cannot grant authority or prove behavior by itself.

## Controller-owned responsibilities

Retain these responsibilities in the controller thread:

- identify the project and baseline;
- define and narrow the permission envelope;
- preserve source-intent provenance for Build End-to-End runs;
- build/revalidate current Project Topology and Runtime Map when relevant;
- approve affected areas and task-local Area Context Sets;
- create/freeze/reconcile cross-area `IC-xx` interface contracts;
- recommend the execution profile;
- approve the task map and budgets;
- select role capability tiers and specialist archetypes without inflating budget;
- detect and classify browser/E2E capability when web behavior is relevant;
- create and resume agent threads;
- adjudicate findings and authorize the single fixer wave;
- own Git and remote operations;
- verify technical/security completion evidence;
- adjudicate G1-G4 intent traceability and blind acceptance;
- run/reconcile the documentation drift gate before clean finish;
- maintain the ledger, Project Intelligence state, projections, and final handoff.

Never delegate authority to broaden these responsibilities. Execution-only operator roles execute an exact approved action and return evidence; they never choose the next controller action.

## State machine

Use the smallest applicable state:

| State | Entry condition | Required exit |
| --- | --- | --- |
| `PREFLIGHT` | New or resumed run | Capabilities, baseline, risk, current topology/runtime facts needed for the run, and permission proposal |
| `SPECIFICATION` | Raw, ambiguous, architectural, risky, or source-intent work | Confirmed specification plus affected areas/interfaces and applicable G1/G2 result |
| `PLAN` | Confirmed specification or bounded clear change | Coverage matrix, complexity tier, approved task map, area/context routing, required frozen-interface plan, and applicable G3 result |
| `IMPLEMENT` | Write gate open for one task | Report plus scoped current state and area/interface observations |
| `REVIEW` | Implementer report is reconcilable | Approval or consolidated findings, including interface drift when applicable |
| `FIX` | Confirmed blocking findings exist and fixer wave unused | Targeted fix evidence without unapproved interface redefinition |
| `REVERIFY` | Fix evidence exists | Approval or `STOP_AND_RESCOPE` |
| `VERIFY` | All task reviews accepted | Fresh technical/security acceptance evidence, area/integration/runtime evidence, and required browser E2E rows when applicable |
| `ACCEPTANCE` | Technical/security verification is sufficient and source-intent G4 applies | Blind user-intent acceptance, including browser observation when applicable, or honest non-complete status |
| `FINISH` | Verification and applicable blind acceptance result are known | Resolved documentation-drift state plus local completion or exact handoff |
| `AUDIT` | Cost, context, interface churn, or scope pressure is abnormal | Optimized policy and rescope decision |
| `RECOVERY` | Thread interruption or context loss | Reconciled current topology/interface/runtime/task state and exact next action |
| `STOPPED` | User stop or unsafe continuation | Durable checkpoint and no new dispatch |

Do not use `SPECIFICATION`, `ACCEPTANCE`, `AUDIT`, or `RECOVERY` as execution profiles. Project Intelligence is integrated state, not a top-level execution phase.

## Independent run dimensions

Record and evaluate these independently at every safe stage transition:

- launch scenario: `NEW_PROJECT`, `CONTINUE_PROJECT`, `EXISTING_PROJECT`, or `NOT_APPLICABLE`;
- public interaction mode: `INTERVIEW`, `ASSISTED`, `FULL_AUTO`, or `NOT_APPLICABLE` for a direct controller/recovery/audit entry that did not come through Build End-to-End;
- controller autonomy: `MANAGED`, `AUTONOMOUS_LOCAL`, or explicitly authorized `EXTENDED_AUTONOMOUS`;
- execution profile: maximum speed, balanced, or maximum quality;
- complexity tier: T0–T3 or split/decision-map state;
- effective permissions: the current intersection defined by the permission envelope;
- intent traceability: `NOT_APPLICABLE`, `INLINE`, or durable source-brief/manifest state with G1-G4 results when Build End-to-End applies;
- Project Intelligence: topology/context/interface/runtime/docs states derived from current evidence;
- browser verification: `NOT_APPLICABLE`, `AVAILABLE`, `DEGRADED`, or `UNAVAILABLE`, with separately recorded concrete mode/framework when web behavior is relevant.

A public interaction mode changes user involvement and delegated ordinary decisions only. It cannot choose/downgrade execution profile, widen effective permissions, manufacture topology, alter an interface contract, add agent budget, or infer `EXTENDED_AUTONOMOUS`. Default a missing Build End-to-End mode to `ASSISTED`. Normalize legacy `GUIDED` to public `INTERVIEW` and legacy public wording `AUTONOMOUS_LOCAL` to `FULL_AUTO` only for compatibility; keep internal controller autonomy separate.

Apply a requested public mode change only at the next safe stage transition. Preserve completed stages. A less interactive mode never expands the permission/decision/interface/runtime envelope.

## Project Intelligence gates

Read `project-intelligence.md` for the complete contract. Apply the following controller invariants.

### P1 — Project Topology gate

During read-only `PREFLIGHT`, build only the topology needed for the current run from current repository evidence.

- Do not assume frontend/backend because the product is a website/app.
- A one-area CLI remains one area when evidence supports that shape.
- Existing architecture/profile/context docs are candidates and become `STALE` where they conflict with current code/config/instructions.
- Split areas by independently owned contracts, runtime/data/security boundaries, not arbitrary directories/file counts.
- Topology cannot grant writes/commands/permissions.

A missing non-blocking area may leave topology `PARTIAL`; a missing area/interface required for safe planning yields `NEEDS_CONTEXT`, `BLOCKED`, or `SPLIT_REQUIRED` as appropriate.

### P2 — Area Context gate

Before dispatching a task, record one primary area and a bounded `AREA_CONTEXT_SET`.

It must include relevant task-local `U-`/`S-` rows, area facts, required neighboring interfaces/invariants, commands/paths, and security/data/runtime constraints while excluding unrelated areas/history/reports/logs.

If correctness requires a broad multi-boundary package, return `CONTEXT_TOO_BROAD` or split instead of hiding dependencies. Context minimization is a performance optimization, never permission to omit an acceptance/security/interface invariant.

### P3 — Cross-Area Interface gate

When producer/consumer assumptions span independently owned areas and can drift:

1. create one controller-owned `IC-xx` contract from valid specification/design authority;
2. record producer/consumers, input/output/errors/auth/data/compatibility/delivery semantics and integration proof;
3. freeze an identity/hash before dependent writer dispatch;
4. put the same identity in producer/consumer task briefs;
5. reject unilateral material redefinition by an implementer/reviewer.

A material frozen-contract change returns to controller reconciliation before dependent work continues. Update affected plan/task/context/test/review/verification/doc-impact state. Do not enable parallel writers to compensate for the pause.

### P4 — Runtime gate

A `RUNTIME_MAP` records only verified service ownership, commands, status/log observation, environment class, and relevant port/socket evidence.

- Status/log observation does not authorize start/stop/restart/kill/port bind/network/data mutation.
- An occupied port with unknown process ownership never authorizes broad kill-by-port/process-name cleanup.
- Prefer run/project-owned process identity or host-native service ownership.
- Revalidate stale PID/log/service facts before acting.
- `FULL_AUTO` does not widen runtime authority.

Unknown ownership on a required action returns `BLOCKED`/`NEEDS_CONTEXT` or an exact operator handoff.

### P5 — Documentation drift gate

After fresh technical/security verification (and after bounded correction/reverification if required), classify durable docs impact before a clean finish:

- `DOCS_NOT_REQUIRED`;
- `DOCS_CURRENT`;
- `DOCS_UPDATE_REQUIRED`;
- `DOCS_BLOCKED`;
- `DOCS_CONFLICT`.

Trigger impact review for verified changes to durable public/API/interface contracts, topology/ownership, runtime procedure, persistence/migration behavior, security/trust boundaries, required environment semantics, documented test/deploy procedures, or documented durable user workflows.

Routine private refactors normally yield `DOCS_NOT_REQUIRED`.

When update is required and docs writes are authorized, route a docs-only maintainer against verified current evidence. Documentation cannot modify product/tests/spec/source intent/U-state/interface authority or make failed behavior pass. If authoritative required docs stay stale/conflicting and cannot be resolved, do not claim clean `COMPLETE`/finished status.

### P6 — Specialist routing gate

Specialist archetypes are scoped roles applied to existing Matreshka skills, not new package skills or automatic extra agents.

- Use the smallest useful role set.
- Multiple topology areas do not automatically increase unique-agent/turn budget.
- A T0 cohesive task normally stays general unless a specialist boundary materially matters.
- UI specialist cannot silently change API/business/data semantics.
- Data/migration specialist retains required security/rollback rigor.
- E2E specialist cannot weaken assertions to make product pass.
- Documentation maintainer is docs-only after verified behavior.
- Browser checker remains read-only per browser contract.
- Remote/file-transfer operators execute only exact authorized action/target and return evidence; controller decides next action.

Specialization cannot widen filesystem/Git/network/browser/process/secret/provider/database/deploy/migration/destructive/remote permissions.

## Browser/E2E capability gate

When a confirmed/requested outcome is browser-visible or the repository already declares browser E2E, inspect the current browser-testing surface during `PREFLIGHT` or before the first applicable verification gate.

Record evidence for repository E2E framework/command, managed browser, optional CDP/host browser tool, isolated-context guarantee, screenshot/trace/video support, console/network inspection, runtime needs, and separate install/start/port/test-data/destructive permissions.

Prefer existing repository E2E. Do not install Playwright over valid Cypress/Selenium/WebdriverIO merely because Playwright is a recommended default for a new authorized setup.

A browser/E2E request or `FULL_AUTO` never grants dependency, network, browser, process, port, data-mutation, secret, Git, or remote authority. A personal browser profile/ambient authenticated session is not trustworthy test isolation.

Before E2E/global setup may reset/truncate/recreate/seed/migrate data, require proof of exact disposable/approved test environment, exact mutation, authority, and rollback/reset expectation.

Automated E2E belongs to `VERIFY`; browser G4 belongs to `ACCEPTANCE`. E2E PASS never implies G4 PASS.

## User-intent traceability gates

For source-qualified Build End-to-End runs, apply brief traceability in addition to—not instead of—Project Intelligence/security/verification.

### G1 — clarification completeness

Before specification can be complete for planning, every material `U-` row is represented by a user decision, inspected fact, delegated reversible decision, explicit placeholder/assumption, deferred outcome, or valid drop. Unknown business/security/legal/cost facts are never fabricated. Only user decision authority may mark `DROPPED`.

### G2 — independent brief-to-spec coverage

Before `PLAN`, a fresh read-only checker receives only source brief + candidate specification and is prohibited from consulting manifest/conversation/plan/tasks/Project Intelligence interpretations/reports when reachable. Blocking missing/half-covered/material unsourced scope returns to `SPECIFICATION`.

### G3 — requirement/task traceability

Before first product-code write:

- every live `IN_SPEC` `U-` maps to task + planned proof;
- every product task maps to `U-`, `S-`, or justified enabling step;
- every selected `S-` has negative proof and review/verification owner;
- every task has a primary area/context set;
- every required cross-area seam has a shared frozen-interface plan before dependent dispatch.

### G4 — blind acceptance

Enter `ACCEPTANCE` only after fresh technical/security verification is sufficient. Blind checker receives source brief, actual product/repository, and permitted observation commands/interactions only. It must not receive/consult spec, manifest, plan/tasks, Project Intelligence/interface coordination state, reports, progress/dashboard, or completion claims.

Return `DELIVERED`, `PARTIAL`, `MISSING`, or `UNCHECKABLE` per user outcome and never fix. Browser-visible outcomes use trustworthy isolated browser observation when available/authorized. Material partial/missing/critical-uncheckable blocks COMPLETE.

## Decision-map gate

Before implementation, return `SPLIT_REQUIRED` + `DECISION_MAP_REQUIRED` when one specification cannot contain the destination, multiple products are combined, unresolved decisions branch, likely plan exceeds safe single-phase budget before trustworthy task boundaries exist, or independent security/data boundaries require separate specs. Decision map is state, not implementation permission/ticket authority.

## Durable artifact transitions

- Resolve one compatible context source using Build End-to-End context contract; never merge conflicting context docs silently.
- Preserve redacted source brief and `U-` manifest only after exact run-state write authority; raw source state not committed by default.
- When authorized, Project Intelligence coordination state may use `.matreshka/runs/<run-id>/project-intelligence.md` and `.matreshka/runs/<run-id>/interfaces/`. These are internal run state, not committed by default or permission-bearing.
- A reusable project profile may cache validated topology/context/runtime facts only at an authorized compatible path; current repository evidence still wins.
- Record only ADR IDs crossing ADR threshold; ADR is never implementation/migration authority.
- Treat progress/dashboard as human projections. On mismatch, reconcile actual state/fresh evidence -> ledger -> source intent -> topology/interfaces/runtime -> reports -> docs state -> projections.
- Record source/manifest identities, G1-G4, Project Intelligence summaries, browser evidence, docs state, timing/usage, and mismatch notes without secrets/private logs/hidden reasoning/session data.

## Task-size gate

Treat file count as warning, not mechanical verdict. Require `SPLIT_REQUIRED` when task contains multiple independently testable results or mixes migration/runtime, auth/UI, provider/persistence, execution/reporting, independent security/experience designs, unrelated public contracts, or multiple reviewable change units.

Prefer one result, one primary area/security boundary, one focused RED/GREEN cycle, and one independently reviewable diff. Cross-area does not automatically mean separate tasks when one cohesive seam can be safely implemented sequentially; use interface/context evidence to decide.

## Dispatch invariants

- Dispatch only from controller.
- Forbid child agents.
- Start roles with minimal fresh context.
- Preserve stable thread IDs for follow-up.
- Permit only one active writer per checkout.
- Permit parallel reviewers only when read-only and independent.
- Cap dispatches at task and phase levels; specialist routing does not add budget.
- Treat a started reasoning turn as spent.
- Do not create a fresh replacement before inspecting partial writes/thread status.
- Pass task-local `U-` rows/quotes, primary-area context, required `IC-xx`, exact paths/commands—never whole project history by default.
- Browser checker is read-only to approved isolated target.
- Execution-only remote/file-transfer operator performs no unrequested next action.

## Findings adjudication

| Severity | Meaning | Controller action |
| --- | --- | --- |
| Critical | Security, data, destructive, isolation, or fundamental correctness failure | Block; fix once if safely bounded, otherwise stop |
| Important | Acceptance, correctness, source-intent narrowing, unapproved cross-area contract drift, or policy failure blocking completion | Single consolidated fixer wave |
| Minor | Non-blocking improvement outside acceptance/policy breach | Record; do not expand task |

Reject finding without reproducible location, violated requirement/contract, and evidence. Resolve disagreements from source of truth/current evidence. Unresolved Important/Critical => stop/rescope/user decision.

## Status rules

| Status | Use when |
| --- | --- |
| `NEEDS_CONTEXT` | A specific fact cannot be inspected safely |
| `BLOCKED` | Required dependency, decision, permission, intent/interface/runtime/docs gate, browser capability, or safe test environment is missing |
| `INTERFACE_CHANGED` | A frozen cross-area contract needs controller reconciliation before dependent work continues |
| `SPLIT_REQUIRED` | Task has multiple independent results/boundaries |
| `CONTEXT_TOO_BROAD` | Proposed area context package cannot remain task-local without hiding dependencies |
| `RECORD_FOR_FUTURE_TASK` | Valid issue lies outside scope |
| `STOP_AND_RESCOPE` | One fixer wave failed, decomposition/cohesion wrong, or drift too large |
| `PARTIALLY_VERIFIED` | Material technical/security/browser/intent/docs claims lack evidence/resolution |
| `HANDOFF_REQUIRED` | Another authorized environment/operator must act |
| `COMPLETE` | Every acceptance criterion, security control, required interface/runtime/browser evidence, resolved docs gate, and applicable G4 outcome has fresh evidence |

## Interrupted-turn policy

For timeout/transport/malformed report:

1. determine whether turn began;
2. inspect agent status, allowlisted files, partial report without changing them;
3. count started turn;
4. send at most one bounded follow-up to same thread;
5. if resume unavailable choose truthful degraded/handoff, not fresh replacement disguised as continuation;
6. update ledger with topology/interface/context identity, last verified checkpoint, exact next action.

For resumed older ledger under later contract, record version difference; preserve recognized completed stages. Derive missing Project Intelligence fields only from current evidence. Never reconstruct original source brief from later spec or invent old interface/runtime state. Write migration only with exact authority.

## Audit triggers

Enter `AUDIT` when any signal is material:

- 30–40 minutes pass without independently reviewable result;
- task/phase dispatch budget approaches exhaustion;
- reviewer repeatedly reads whole branch/reruns broad tests;
- briefs/reports/diffs/context sets grow beyond task boundary;
- second blocking fix appears likely;
- one task spreads into multiple independent areas/subsystems;
- cross-area interface churn causes repeated rework;
- stale topology/docs/runtime assumptions cause rediscovery or failed dispatches;
- missing reports/state make recovery forensic;
- token/time use grows disproportionately to diff;
- source-intent drift causes rework;
- browser setup/evidence work expands without useful result.

Recommend split, narrower context, interface freeze, corrected topology/runtime ownership, specialist change, or ending run. Never solve cost pressure by weakening security, browser safety, Project Intelligence correctness, docs truthfulness, or G1-G4 gates.
