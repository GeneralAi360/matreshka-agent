# Project Intelligence Layer

Use this contract during controller preflight, planning, task dispatch, verification, recovery, and finish when repository structure or cross-area coordination materially affects correctness, context size, runtime ownership, or durable documentation.

Project Intelligence is descriptive state. It never grants filesystem writes, commands, Git, network, browser, process, port, secret, provider, database, deploy, migration, destructive, or remote authority.

When UI/UX is material, Project Intelligence interoperates with the separate [Design Intelligence controller bridge](design-intelligence.md). Project areas answer **where/what owns the code**; Design Intelligence answers **how the product experience should remain coherent**. Neither layer grants authority.

## Apply the smallest useful layer

Do not manufacture architecture for a simple project. For a small one-area change, topology may contain one area, no interface contract, no runtime service, `DOCS_NOT_REQUIRED`, and `GENERAL_IMPLEMENTER`.

For multi-area work, use the six capabilities below.

## P1 — PROJECT_TOPOLOGY

During read-only preflight, identify current architectural areas from repository evidence. Never assume that an app has separate frontend/backend components merely because it is a web project.

Record each area as:

```text
AREA_ID
kind
purpose
real roots
entry points
applicable repository instructions
stack/framework facts needed for execution
verified commands and their source
produced interfaces
consumed interfaces
owned state/data
security or trust boundary
freshness/source identity
```

Useful kinds include `FRONTEND`, `BACKEND`, `DATA`, `E2E`, `CLI`, `WORKER`, `QUEUE`, `MOBILE`, `SHARED_LIBRARY`, `INFRA`, and repository-specific kinds. Names are descriptive, not permissions or skill names.

Topology status is one of:

- `CURRENT` — material facts were validated against current repository state;
- `PARTIAL` — enough for current task, but some non-blocking areas remain unknown;
- `STALE` — reusable profile/doc disagrees with current repository evidence;
- `UNAVAILABLE` — required structure cannot be inspected.

An existing architecture document, context index, project profile, or area guide is only a candidate. Validate claimed paths, commands, interfaces, and current area ownership before reuse. Current code/config plus applicable repository instructions outrank stale prose.

### Topology merge/split rules

Keep paths in one area when they share owner, lifecycle, interface surface, and review boundary. Split areas when they have materially independent public contracts, runtime lifecycles, data/security boundaries, or task ownership.

Do not split only to reduce file count. Do not merge auth/data boundaries merely to make the map smaller.

## P2 — AREA_CONTEXT_SET

Before each task dispatch, derive a minimal context set from topology, source-intent requirements, interfaces, and task plan.

Required context classes:

1. task brief and relevant `U-` / `S-` rows;
2. primary area facts and applicable path instructions;
3. exact cross-area interface contracts/invariants the task produces/consumes;
4. focused commands and exact allowlisted paths;
5. required data/security/runtime constraints;
6. smallest surrounding code/docs needed to judge the change.

Default exclusions:

- full source brief after task-local U rows exist;
- unrelated area documents;
- entire project history;
- old implementation/review reports;
- raw logs;
- full branch diff;
- unrelated runtime/deployment material;
- broad file inventories.

Record in task brief:

```text
Primary area: AREA-...
Adjacent areas: ...
Interface contracts: IC-... or none
Included sources: ...
Explicitly excluded areas: ...
Context guarantee: NARROW | DEGRADED | CONTEXT_TOO_BROAD
```

Context minimization must never remove a correctness invariant. If task needs several independent areas/contracts to stay correct, split or return `CONTEXT_TOO_BROAD`; do not hide dependencies.

For UI tasks, `AREA_CONTEXT_SET` may be paired with a separate `DESIGN_CONTEXT_SET`; do not stuff the full design history into area context.

## P3 — CROSS_AREA_INTERFACE_CONTRACT

Create an interface contract when one user-visible/system outcome crosses independently owned areas and producer/consumer assumptions can drift.

Examples:

- frontend -> backend HTTP/API;
- API -> data/persistence;
- worker -> queue/event producer;
- service -> external-provider adapter;
- CLI -> storage boundary;
- mobile/web -> shared backend;
- build/runtime component -> another process with a defined protocol.

Do not create a contract for a cohesive internal helper seam unless independently versioned/reviewed.

### Identity and path

Assign `IC-01`, `IC-02`, ... within a run. When run-state writes are authorized:

```text
.matreshka/runs/<run-id>/interfaces/IC-xx-<safe-slug>.md
```

Use [the interface contract template](../assets/interface-contract-template.md). It is run coordination state, not committed by default.

Promote/update a durable repository interface document only when repository already has compatible convention or interface is intentionally durable/public and documentation writes are authorized.

### Required fields

Every contract records:

- source U/S/enabling requirement IDs;
- producer area and consumer area(s);
- request/input/event shape;
- response/output/event shape;
- validation and error/failure semantics;
- auth/authorization/data boundary;
- ordering/idempotency/retry semantics when relevant;
- compatibility/version rule;
- expected integration proof;
- current contract identity/hash.

### Contract freeze rule

Before dependent consumer writer dispatch, freeze contract identity in ledger and dependent task briefs. A material interface change after work starts requires controller reconciliation:

1. stop dependent dispatch/current task at safe boundary;
2. update/confirm contract from valid authority;
3. identify affected tasks/tests/docs/design context when UX depends on contract;
4. update briefs/context sets;
5. rerun smallest required RED/GREEN/review/verification chain.

Never let frontend/backend writers independently redefine same contract. Parallel writers remain disabled in one checkout.

## P4 — RUNTIME_MAP

Map relevant dev/test services before controller relies on them.

For each runtime unit record:

```text
service ID / owning area
verified start command + source
verified stop command or owned-process mechanism + source
status/health observation
log source
port/socket only when evidenced
environment class: LOCAL_TEST | LOCAL_DEV | STAGING | PRODUCTION | UNKNOWN
process ownership evidence
state/data mutation implications
required permissions for start/stop/port/network/test-data actions
```

Runtime map may exist even when no process actions are authorized.

### Ownership safety

Observing status/logs is not authority to start/stop/restart/kill/bind/mutate. Prefer project-owned PID/service identities or host-native ownership. Never clear a port by broad process name/port killing because intended service cannot start.

If expected port is occupied and ownership unproven, return `BLOCKED` or `NEEDS_CONTEXT` with exact ownership fact required. `FULL_AUTO` does not widen runtime authority.

### Runtime reuse

On `CONTINUE_PROJECT`/recovery, revalidate commands, ownership, and environment classification before reuse. Old PID/log proves history, not current health.

## P5 — DOCUMENTATION_DRIFT_GATE

After implementation is reviewed and fresh technical/security verification is sufficient, and after applicable Design Drift Gate is resolved, classify documentation impact:

- `DOCS_NOT_REQUIRED` — no durable documented truth changed;
- `DOCS_CURRENT` — affected durable docs already match verified behavior;
- `DOCS_UPDATE_REQUIRED` — affected authoritative project docs are stale;
- `DOCS_BLOCKED` — required update cannot be performed inside authority;
- `DOCS_CONFLICT` — candidate docs disagree and authority cannot resolve canonical source.

### Durable-change triggers

Check impact when verified work changes:

- public/API/interface contract;
- project topology/area ownership;
- runtime command/service relationship/port/status/log procedure;
- persistence model/migration behavior;
- auth/security/trust boundary;
- required environment variable semantics;
- documented deployment/test procedure;
- durable user workflow promised by project docs.

Routine private refactors, helper renames, temporary task status, internal detail, and local test fixtures normally produce `DOCS_NOT_REQUIRED`.

### Update policy

When `DOCS_UPDATE_REQUIRED` and docs writes authorized:

1. select only affected docs;
2. revalidate changed claims from current code/config/test evidence;
3. update minimally after behavior verified;
4. keep secrets/private payloads/raw logs out;
5. verify changed links/commands/paths where practical;
6. record paths in ledger/final handoff.

Documentation maintainer may not modify product code/tests/spec/source brief/U state/IC state/DESIGN.md/Git/remote systems. Documentation follows verified behavior and can never make failing behavior pass.

If stale authoritative docs cannot be updated, do not claim clean COMPLETE/finished result.

## P6 — SPECIALIST_ROLE_ROUTING

Use role archetypes only when specialization improves correctness, context isolation, design quality, or boundary ownership. These are task-role labels over bundled Matreshka skills, not automatic agent-count increases.

Supported archetypes:

| Archetype | Use when | Required boundary |
| --- | --- | --- |
| `GENERAL_IMPLEMENTER` | cohesive ordinary task | normal task contract |
| `FRONTEND_IMPLEMENTER` | UI/client behavior + client integration | cannot redefine backend/data contract |
| `BACKEND_IMPLEMENTER` | API/service/domain behavior | cannot redesign consumer UI contract unilaterally |
| `DATA_MIGRATION_IMPLEMENTER` | schema/migration/persistence boundary | explicit rollback/data/security proof |
| `UI_SPECIALIST` | implement visual/layout/accessibility change | must follow frozen DESIGN.md; no business/API/state semantics unless scoped |
| `DESIGN_ENGINEER` | design recon, direction/prototype, root DESIGN.md contract | design-only authority; no unapproved business/product/Git/dependency/remote expansion |
| `DESIGN_REVIEWER` | independent UX/UI consistency review | read-only; cannot fix code or rewrite DESIGN.md |
| `TEST_E2E_SPECIALIST` | test harness/scenario work | cannot weaken assertions to make product pass |
| `DOCUMENTATION_MAINTAINER` | verified durable docs drift | docs-only allowlist; not DESIGN.md unless separately authorized as design contract write |
| `BROWSER_CHECKER` | browser observation/G4 | read-only product/browser contract |
| `REMOTE_OPERATOR` | explicitly authorized remote command | execute exact command, return evidence, no follow-up decision |
| `FILE_TRANSFER_OPERATOR` | explicitly authorized file transfer | exact source/destination, no shell action |

`DESIGN_ENGINEER` routes through bundled `designing-product-experience`; `DESIGN_REVIEWER` routes through read-only review workflow. They do not create new permission classes or increase selected execution-profile budgets.

### Budget rule

Specialist routing does not create extra budget. Selected execution profile and complexity still cap unique roles/turns. A multi-area or design-heavy project may still use one general implementer/combined reviewer when task is small/cohesive.

Do not create one agent per topology area or design concern. Split only by independently reviewable outcomes/boundaries.

### Decision/execution separation

Execution-only operator archetypes return exact target/action/result/exit/evidence and stop. Controller decides next action.

### Specialist task contract

Every specialist dispatch receives:

- role archetype;
- primary/adjacent area IDs;
- `AREA_CONTEXT_SET`;
- `IC-xx` references when relevant;
- current design identity and `DESIGN_CONTEXT_SET` when UI/design relevant;
- exact write/inspect allowlists;
- unchanged permission envelope;
- task-local RED/GREEN/review/verification requirements;
- explicit forbidden neighboring responsibilities.

## Persistent/reusable project intelligence

Project Intelligence is derived from current evidence. Reuse is optional.

When project-profile writes authorized, validated profile may cache:

- topology summary;
- area context index;
- runtime map summary;
- known command sources;
- durable interface-doc locations;
- sensitive boundaries;
- root `DESIGN.md` location/identity as a pointer only when UI exists (actual Design Intelligence remains separate and must be revalidated);
- refresh identity/condition.

Do not cache secrets/env values/raw logs/private URLs/personal data/full inventories/hidden reasoning/transient task status.

A stale profile does not block work when current inspection can rebuild required facts; mark/rebuild stale subset.

## Run-state and recovery

When run-state writes authorized, controller may materialize compact snapshot using [project intelligence template](../assets/project-intelligence-template.md):

```text
.matreshka/runs/<run-id>/project-intelligence.md
```

Interface contracts live under run `interfaces/`. State not committed by default.

On recovery:

1. resolve current real root/baseline/current identity;
2. validate topology roots/entry points/commands touched by remaining work;
3. validate active interface contracts;
4. validate runtime ownership/environment before process actions;
5. revalidate root `DESIGN.md` pointer/identity through Design Intelligence when UI remains;
6. reconcile area/design context sets and specialist routing;
7. rerun documentation impact after fresh verification if code changed;
8. correct ledger/dashboard projections last.

Do not repeat completed tasks because topology/profile/design pointer refreshed.

## Planning and task requirements

A multi-area plan names:

- affected area IDs;
- primary area per task;
- cross-area interfaces/freeze order;
- required context set;
- runtime dependency when behavior/tests need it;
- specialist archetype when useful;
- applicable design identity/context for UI tasks;
- documentation impact candidates.

An interface-only enabling task is justified only when later producer/consumer tasks depend on it. Avoid decorative architecture tasks.

## Verification and finish

Technical verification proves relevant area-local checks and smallest integration seam. Browser E2E/G4 and visual design verification remain separate according to their contracts.

Before FINISH, controller records resolved Design Drift Gate when applicable, then documentation drift. Final handoff preserves Project Intelligence summary, active interfaces, runtime caveats, design identity/state, docs state, and specialist/operator handoffs.

## Dashboard projection

When dashboard authorized, project compact fields only:

```text
topology status / area count
affected/current area
active interface count/status
runtime map status/service count
documentation drift state
current specialist archetype
context guarantee
```

Design Intelligence projects its own compact `design` block. Do not duplicate full DESIGN.md/prototype/screenshots in Project Intelligence dashboard state.

Dashboard cannot update topology/interface/design authority, dispatch work, or satisfy a gate.
