# Software Specification — Matreshka Agent 0.5 Project Intelligence Layer

- Status: `CONFIRMED_BY_USER`
- Date: `2026-08-20`
- Branch: `dev/0.5-brief-traceability-observability`
- Scope: project understanding and task-context intelligence for Matreshka Agent; no merge to `main` in this specification.

## Outcome

Matreshka must understand a software repository as a set of current architectural areas rather than as one undifferentiated codebase. For multi-area work it must route only the relevant context, freeze shared cross-area interfaces before dependent implementation, understand local runtime ownership, keep durable documentation aligned with verified behavior, and choose useful specialist role archetypes without multiplying agents or widening permissions.

The layer is portable across Codex, Claude Code, Cursor, and Antigravity. It does not require Pi, MCP, a particular framework, a frontend/backend split, or a monorepo.

## Design principles

1. Repository evidence is authoritative over remembered or generated project documentation.
2. Frontend/backend is one possible topology, not a universal template.
3. Project intelligence describes structure and context; it never grants write, Git, network, process, browser, secret, provider, deploy, migration, or destructive authority.
4. New durable artifacts are optional and evidence-gated. Run-local state is preferred for coordination-only information.
5. Context routing must reduce irrelevant context without hiding the interfaces and invariants necessary for correctness.
6. Cross-area producer/consumer work must share one explicit interface contract rather than independently reinventing the seam.
7. Runtime discovery must describe process ownership before any start/stop action.
8. Documentation follows verified behavior. Documentation must never be used to retroactively redefine acceptance.
9. Specialist routing changes role focus, not permissions, execution profile, or the one-writer rule.
10. The controller remains the decision maker. Execution-only operators return evidence and do not choose the next action.

## P1 — Project Topology

During read-only preflight, build a compact `PROJECT_TOPOLOGY` from current repository evidence.

Each area has:

- stable run-local area ID, for example `AREA-FRONTEND`, `AREA-BACKEND`, `AREA-DATA`, `AREA-E2E`, `AREA-WORKER`, `AREA-CLI`, `AREA-INFRA`, or repository-specific IDs;
- kind and purpose;
- real roots and important entry points;
- stack/framework facts that affect execution;
- existing build/test/type/lint/runtime commands with their source;
- owned state/data boundary;
- public or cross-area interfaces it produces/consumes;
- relevant security/trust boundary;
- repository instructions that apply to that area.

Do not create artificial areas merely to match a desired architecture. A small CLI may have one area. A full-stack product may have frontend, backend, data, E2E, workers, and infrastructure.

Topology is `CURRENT`, `STALE`, `PARTIAL`, or `UNAVAILABLE`. Existing topology/context documents are candidates only; they must be revalidated against the repository before reuse.

## P2 — Area Context Router

For every task, derive a minimal `AREA_CONTEXT_SET` from the topology and current task requirements.

The context set contains only:

- task brief and relevant `U-` / `S-` rows;
- primary area facts;
- required neighboring interface contracts and invariants;
- exact relevant repository instructions;
- focused commands and allowlisted paths;
- required security/data/runtime boundary facts;
- the smallest surrounding source/doc references required to judge the change.

Exclude unrelated area documentation, old reports, whole-project history, raw logs, full source brief, and broad branch diffs.

A task that cannot be made correct with a narrow context package returns `CONTEXT_TOO_BROAD` or requires a split. Context reduction may never omit a contract that a producer or consumer depends on.

## P3 — Cross-Area Interface Contract

When one user outcome crosses two or more independently owned areas, planning must create a single controller-owned interface contract before dispatching dependent writers.

Examples include:

- frontend -> HTTP/API backend;
- API -> persistence schema;
- worker -> queue/event producer;
- service -> provider adapter;
- CLI -> storage layer;
- mobile/web -> shared backend contract.

A contract records:

- `IC-xx` identity and source requirement IDs;
- producer and consumer areas;
- request/input shape;
- response/output shape;
- errors/failure semantics;
- auth/authorization/data boundary;
- compatibility/versioning rule;
- idempotency/ordering where relevant;
- contract proof/integration evidence;
- current contract hash/identity.

Default run-local path when state writes are authorized:

```text
.matreshka/runs/<run-id>/interfaces/IC-xx-<slug>.md
```

A durable repository interface document may be updated only when the project already has a compatible convention or the interface is intentionally durable/public and documentation writes are authorized.

Producer and consumer task briefs must reference the same contract identity. A material contract change after either side starts blocks dependent dispatch until the controller reconciles the contract, affected tasks, tests, and evidence. Parallel writers remain disabled in one checkout.

## P4 — Runtime Map

Build a read-only `RUNTIME_MAP` for services/processes relevant to development or verification.

For each service record:

- area/owner;
- verified start command;
- verified stop command or safe owned-process mechanism;
- status/health observation;
- log source;
- port/socket only when repository evidence provides it;
- environment classification: local test/dev/staging/production/unknown;
- process ownership evidence;
- mutation/destructive implications;
- whether start, stop, port bind, network, or test-data authority is required.

Runtime discovery does not authorize starting or stopping anything. Never kill by broad process name or occupied port merely to clear a conflict. Prefer project-owned PID/process identity or host-native ownership. Unknown ownership returns `BLOCKED`/`NEEDS_CONTEXT` rather than destructive cleanup.

## P5 — Documentation Drift Gate

After implementation review and fresh technical verification, but before final completion/handoff, classify documentation impact as:

- `DOCS_NOT_REQUIRED` — no durable project truth changed;
- `DOCS_CURRENT` — affected durable docs already match verified behavior;
- `DOCS_UPDATE_REQUIRED` — one or more authoritative project docs are stale;
- `DOCS_BLOCKED` — required docs cannot be updated inside current authority;
- `DOCS_CONFLICT` — current docs disagree and valid authority cannot resolve the source.

A documentation update is required when verified work changes a durable public or operational truth such as:

- public/API/interface contract;
- project topology or area ownership;
- runtime command/port/service relationship;
- persistence model or migration behavior;
- auth/security/trust boundary;
- required environment variable name/meaning;
- supported user workflow whose project docs intentionally document behavior;
- testing/deployment procedure that is part of the repository contract.

Do not update documentation for routine private refactors, local helper names, temporary task status, or implementation details with no durable consumer.

Only affected docs are eligible. Revalidate their claims against current code/config before editing. Documentation updates occur after behavior is verified and must not change the specification or acceptance result. Missing documentation-write permission cannot be converted into `COMPLETE` when the repository requires the stale doc to remain authoritative; return a truthful handoff or partial status.

## P6 — Specialist Role Routing

The controller may assign a role archetype to a normal Matreshka implementation/review/verification dispatch when the topology/task shows a material benefit.

Supported archetypes are capabilities, not new global skills:

- `GENERAL_IMPLEMENTER`;
- `FRONTEND_IMPLEMENTER`;
- `BACKEND_IMPLEMENTER`;
- `DATA_MIGRATION_IMPLEMENTER`;
- `UI_SPECIALIST`;
- `TEST_E2E_SPECIALIST`;
- `DOCUMENTATION_MAINTAINER`;
- `BROWSER_CHECKER`;
- `REMOTE_OPERATOR` / `FILE_TRANSFER_OPERATOR` only for separately authorized remote workflows.

Routing rules:

- use the smallest useful role set;
- a T0/simple task stays with a general implementer unless a special boundary materially matters;
- specialization does not add agent turns by itself or bypass profile budgets;
- a specialist receives only its area context set and interface contracts;
- specialists cannot create child agents;
- a UI specialist may not silently change business/API behavior;
- a documentation maintainer may edit only affected authorized docs after verified behavior;
- execution-only operators return command/transfer evidence and do not decide follow-up actions;
- Git, network, provider, secret, deploy, migration, destructive, browser, process, and filesystem authority remain controller-owned permission decisions.

## Controller integration

The controller applies Project Intelligence inside existing states rather than adding a new top-level state:

```text
PREFLIGHT
  -> topology + runtime + context candidates
SPECIFICATION
  -> affected areas and cross-area seams
PLAN
  -> interface contracts + area context sets + specialist routing
IMPLEMENT/REVIEW
  -> task-local area/contract packages
VERIFY
  -> area/integration/runtime evidence
ACCEPTANCE
  -> unchanged G4 source-brief acceptance
FINISH
  -> documentation drift gate + exact handoff
```

G1-G4, Security by Design, execution profiles, complexity tiers, one-writer rule, single fixer wave, browser/E2E rules, Git boundaries, and existing permission semantics remain unchanged in strength.

## Project intelligence artifacts

When run-state writes are authorized, coordination state may live under:

```text
.matreshka/runs/<run-id>/project-intelligence.md
.matreshka/runs/<run-id>/interfaces/
```

Durable project docs are reused first. Matreshka must not create a parallel documentation tree simply because the layer exists.

If a reusable project profile is authorized, it may cache validated topology/runtime/context-index facts with an input identity and refresh condition. Cached data is never more authoritative than current repository evidence.

## Dashboard and ledger

Ledger/project projection should expose only compact intelligence:

- topology status and area count;
- affected/current area IDs;
- active cross-area interface IDs/status;
- runtime map status/service count;
- documentation drift state;
- selected specialist role;
- context package size/source summary when available.

Do not project raw docs, private URLs, secrets, environment contents, browser/session data, raw logs, or hidden reasoning.

## Acceptance criteria

The layer is implemented when all of the following contracts exist and are wired into the current 0.5 workflow:

1. A multi-area web project yields topology areas instead of one undifferentiated task context.
2. A one-area CLI does not get artificial frontend/backend decomposition.
3. Frontend/backend work that shares an API uses one interface contract before dependent implementation.
4. Backend task context excludes unrelated frontend history while retaining the interface contract.
5. A runtime map distinguishes inspect/status/log operations from start/stop/port authority.
6. Unknown process ownership cannot lead to broad kill-by-port/process cleanup.
7. Verified public interface/runtime/security changes trigger a documentation impact decision.
8. Routine private refactors can truthfully produce `DOCS_NOT_REQUIRED`.
9. Specialist role routing stays inside the selected profile/turn budget and permission envelope.
10. Documentation/operator specialists cannot broaden scope or self-authorize follow-up actions.
11. Recovery revalidates cached topology/interface/runtime facts before reuse.
12. Dashboard/ledger intelligence remains projection/state and cannot satisfy verification or grant authority.

## Non-goals

- Force every project into `frontend/backend` directories.
- Add a new framework/runtime dependency.
- Install Pi or an MCP server.
- Introduce parallel writers in one checkout.
- Automatically rewrite AGENTS.md or repository rules.
- Automatically start/stop services, open ports, install packages, read secrets, mutate databases, deploy, or use remote systems.
- Replace the existing specification, planning, review, verification, G4, or finishing skills.
