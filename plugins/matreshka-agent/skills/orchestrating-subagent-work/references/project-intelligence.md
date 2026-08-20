# Project Intelligence Layer

Use this contract during controller preflight, planning, task dispatch, verification, recovery, and finish when repository structure or cross-area coordination materially affects correctness, context size, runtime ownership, or durable documentation.

Project Intelligence is descriptive state. It never grants filesystem writes, commands, Git, network, browser, process, port, secret, provider, database, deploy, migration, destructive, or remote authority.

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
- `PARTIAL` — enough for the current task, but some non-blocking areas remain unknown;
- `STALE` — a reusable profile/doc disagrees with current repository evidence;
- `UNAVAILABLE` — required structure cannot be inspected.

An existing architecture document, context index, project profile, or area guide is only a candidate. Validate its claimed paths, commands, interfaces, and current area ownership before reuse. Current code/config plus applicable repository instructions outrank stale prose.

### Topology merge/split rules

Keep two paths in one area when they share one owner, lifecycle, interface surface, and review boundary. Split areas when they have materially independent public contracts, runtime lifecycles, data/security boundaries, or task ownership.

Do not split only to reduce file count. Do not merge auth/data boundaries merely to make the map smaller.

## P2 — AREA_CONTEXT_SET

Before each task dispatch, derive a minimal context set from topology, source-intent requirements, interfaces, and the task plan.

Required context classes:

1. task brief and relevant `U-` / `S-` rows;
2. primary area facts and applicable path instructions;
3. exact cross-area interface contracts/invariants the task produces or consumes;
4. focused commands and exact allowlisted paths;
5. required data/security/runtime constraints;
6. the smallest surrounding code/docs needed to judge the change.

Default exclusions:

- full source brief after task-local `U-` rows exist;
- unrelated area documents;
- entire project history;
- old implementation/review reports;
- raw logs;
- full branch diff;
- unrelated runtime/deployment material;
- broad file inventories.

Record a compact context manifest in the task brief:

```text
Primary area: AREA-...
Adjacent areas: ...
Interface contracts: IC-... or none
Included sources: ...
Explicitly excluded areas: ...
Context guarantee: NARROW | DEGRADED | CONTEXT_TOO_BROAD
```

Context minimization must never remove an invariant required for correctness. If the task needs several independent areas and contracts in order to remain correct, split it or return `CONTEXT_TOO_BROAD`; do not solve context pressure by hiding dependencies.

## P3 — CROSS_AREA_INTERFACE_CONTRACT

Create an interface contract when one user-visible or system outcome crosses two or more independently owned areas and producer/consumer assumptions can drift.

Examples:

- frontend -> backend HTTP/API;
- API -> data/persistence;
- worker -> queue/event producer;
- service -> external-provider adapter;
- CLI -> storage boundary;
- mobile/web -> shared backend;
- build/runtime component -> another process with a defined protocol.

Do not create a contract for an internal helper call inside one cohesive area unless that seam itself is independently versioned/reviewed.

### Identity and path

Assign `IC-01`, `IC-02`, ... within a run. When run-state writes are authorized, use:

```text
.matreshka/runs/<run-id>/interfaces/IC-xx-<safe-slug>.md
```

Use [the interface contract template](../assets/interface-contract-template.md). The contract is run coordination state and is not committed by default.

Promote/update a durable repository interface document only when:

- the repository already has a compatible interface-doc convention; or
- the interface is intentionally durable/public and documentation writes are authorized.

### Required fields

Every contract records:

- source `U-` / `S-` / enabling requirement IDs;
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

Before dispatching a dependent consumer writer, freeze the relevant contract identity in the ledger and both task briefs. A material interface change after producer or consumer work starts requires controller reconciliation:

1. stop the dependent dispatch or current task at the next safe boundary;
2. update/confirm the contract from valid design authority;
3. identify affected tasks/tests/docs;
4. update task briefs/context sets;
5. rerun the smallest required RED/GREEN/review/verification chain.

Never let frontend and backend writers independently redefine the same contract. Parallel writers remain disabled in one checkout.

## P4 — RUNTIME_MAP

Map relevant development/test services before the controller relies on them.

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

A runtime map may exist even when no process actions are authorized.

### Ownership safety

Observing status/logs is not authority to start, stop, restart, kill, bind, or mutate anything. Prefer project-owned PID/service identities or host-native service ownership. Never clear a port by broad process name/port killing simply because the intended service cannot start.

If an expected port is occupied and ownership is not proven, return `BLOCKED` or `NEEDS_CONTEXT` with the exact ownership fact required. Do not guess that an unknown process belongs to the current run.

Process/runtime authority stays in the permission envelope already defined by Matreshka. `FULL_AUTO` does not widen it.

### Runtime reuse

On `CONTINUE_PROJECT` or recovery, revalidate commands, service ownership, and environment classification before reuse. A PID file or old log proves historical activity, not current health.

## P5 — DOCUMENTATION_DRIFT_GATE

After implementation is reviewed and fresh technical/security verification is sufficient, but before a clean final handoff/completion, classify documentation impact:

- `DOCS_NOT_REQUIRED` — no durable documented truth changed;
- `DOCS_CURRENT` — affected durable docs already match verified behavior;
- `DOCS_UPDATE_REQUIRED` — affected authoritative project docs are stale;
- `DOCS_BLOCKED` — required update cannot be performed inside current authority;
- `DOCS_CONFLICT` — multiple candidate docs disagree and authority cannot resolve the canonical source.

### Durable-change triggers

Check documentation impact when verified work changes any repository-documented truth such as:

- public/API/interface contract;
- project topology or area ownership;
- runtime command, service relationship, required port, or status/log procedure;
- persistence model/migration behavior;
- auth/security/trust boundary;
- required environment variable name or semantics;
- documented deployment/test procedure;
- durable user workflow that project docs promise.

Routine private refactors, helper renames, temporary task status, internal implementation detail, and local test fixtures normally produce `DOCS_NOT_REQUIRED`.

### Update policy

When `DOCS_UPDATE_REQUIRED` and documentation writes are authorized:

1. select only docs whose scope is affected;
2. revalidate each changed claim from current code/config/test evidence;
3. update minimally after behavior is verified;
4. keep secrets/private payloads/raw logs out;
5. verify links/commands/paths referenced by the changed documentation where practical;
6. record the updated doc paths in the ledger/final handoff.

A documentation maintainer may not modify product code, tests, specification, source brief, requirement status, Git state, or remote systems. Documentation follows verified behavior and can never make failing behavior pass.

If the repository treats stale docs as an authoritative contract and they cannot be updated, do not claim a clean `COMPLETE`/finished result; return the appropriate handoff/partial/blocker state.

## P6 — SPECIALIST_ROLE_ROUTING

Use role archetypes only when specialization improves correctness, context isolation, or boundary ownership. These are task-role labels applied to existing Matreshka skills, not extra package skills or automatic agent-count increases.

Supported initial archetypes:

| Archetype | Use when | Required boundary |
| --- | --- | --- |
| `GENERAL_IMPLEMENTER` | cohesive ordinary task | normal task contract |
| `FRONTEND_IMPLEMENTER` | UI/client behavior plus client-side integration | cannot redefine backend/data contract |
| `BACKEND_IMPLEMENTER` | API/service/domain behavior | cannot redesign consumer UI contract unilaterally |
| `DATA_MIGRATION_IMPLEMENTER` | schema/migration/persistence boundary | explicit rollback/data/security proof |
| `UI_SPECIALIST` | visual/layout/accessibility-only change | no business/API/state semantics unless separately scoped |
| `TEST_E2E_SPECIALIST` | test harness/scenario work | cannot weaken assertions to make product pass |
| `DOCUMENTATION_MAINTAINER` | verified durable docs drift | docs-only allowlist |
| `BROWSER_CHECKER` | browser observation/G4 | read-only product/browser contract |
| `REMOTE_OPERATOR` | explicitly authorized remote command execution | execute exact command, return evidence, no follow-up decision |
| `FILE_TRANSFER_OPERATOR` | explicitly authorized file transfer | transfer exact source/destination, no shell action |

### Budget rule

Specialist routing does not create extra budget. The selected execution profile and task complexity still cap unique roles/turns. A multi-area project may still use one general implementer when the task is small and cohesive.

Do not create one agent per topology area. Split only by independently reviewable outcomes/boundaries.

### Decision/execution separation

Execution-only operator archetypes do not interpret output into additional actions. They return exact target, action, result/exit signal, concise evidence, and stop. The controller remains responsible for deciding what happens next.

### Specialist task contract

Every specialist dispatch receives:

- role archetype;
- primary/adjacent area IDs;
- `AREA_CONTEXT_SET`;
- `IC-xx` references when relevant;
- exact write/inspect allowlists;
- unchanged permission envelope;
- task-local RED/GREEN/review/verification requirements;
- explicit forbidden neighboring responsibilities.

## Persistent/reusable project intelligence

Project Intelligence is primarily derived from current evidence. Reuse is optional.

When project-profile writes are authorized, a validated project profile may cache:

- topology summary;
- area context index;
- runtime map summary;
- known command sources;
- durable interface-doc locations;
- sensitive boundaries;
- refresh identity/condition.

Do not cache secrets, environment values, raw logs, private URLs, personal data, whole source inventories, hidden reasoning, or transient task status.

A reusable profile becoming stale does not block work when current repository inspection can rebuild the required facts. Mark/rebuild the stale subset rather than trusting it.

## Run-state and recovery

When run-state writes are authorized, the controller may materialize a compact snapshot using [the project intelligence template](../assets/project-intelligence-template.md):

```text
.matreshka/runs/<run-id>/project-intelligence.md
```

Interface contracts live under the run `interfaces/` directory. This state is not committed by default.

On recovery:

1. resolve current real project root and baseline/current identity;
2. validate topology roots/entry points and commands touched by the remaining work;
3. validate every active interface contract against current producer/consumer state;
4. validate runtime ownership/environment before process actions;
5. reconcile context sets and specialist routing for the next task;
6. re-run documentation impact after fresh verification if code changed;
7. correct ledger/dashboard projections last.

Do not repeat completed tasks merely because topology/profile state was refreshed.

## Planning and task requirements

A multi-area plan must name:

- affected area IDs;
- primary area per task;
- cross-area interfaces and freeze order;
- required context set per task;
- runtime dependency only when behavior/tests need it;
- specialist archetype only when useful;
- documentation impact candidates.

An interface-only enabling task is justified only when later producer/consumer tasks depend on that contract. Avoid decorative architecture tasks.

## Verification and finish

Technical verification should prove relevant area-local checks and the smallest integration seam that demonstrates the contract. Browser E2E/G4 remains separate according to the browser contract.

Before FINISH, the controller records documentation drift state. Finishing work must preserve the project-intelligence summary, active interface identities, runtime caveats, docs state, and specialist/operator handoffs in the final record when relevant.

## Dashboard projection

When dashboard state is authorized, project only compact fields:

```text
topology status / area count
affected/current area
active interface count/status
runtime map status/service count
documentation drift state
current specialist archetype
context guarantee
```

Do not display raw code/docs/logs, private runtime URLs, secret values, environment values, personal browser/session data, or permission-expanding prose.

Dashboard state cannot update topology/interface authority, dispatch work, or satisfy a gate.
