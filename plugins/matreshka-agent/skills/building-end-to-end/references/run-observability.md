# Run Observability Contract

Use this contract to provide a glanceable local view of a Build End-to-End run without creating a second source of truth.

## Projection, never authority

Authoritative order:

```text
actual repository/current external/rendered state + fresh evidence
-> validated controller ledger
-> confirmed specification/plan/task/interface/design-contract state
-> human projections
```

Dashboard/progress state cannot grant permissions, prove tests/design, freeze/change an interface or design identity, establish runtime ownership, resolve drift, or advance completion by itself.

## Human language

Use the user's active conversation language for dashboard labels, stage/task titles, checkpoint summaries, next action and final human reports unless repository convention requires another language. Stable machine IDs/enums/commands/paths/hashes/U-/S-/IC-/design identities stay unchanged internally.

For a Russian run, ordinary dashboard prose is Russian. Product/framework names, protocol IDs, `DESIGN.md` and G1-G4 may remain literal.

## Files

Only when exact run-state paths are writable may controller create:

```text
.matreshka/runs/<run-id>/dashboard-state.js
.matreshka/runs/<run-id>/dashboard.html
```

Copy the packaged HTML and initialize state from the packaged state template. The HTML body/layout is immutable after copy **except** the machine-owned snapshot block delimited by:

```text
/*MATRESHKA_SNAPSHOT_START*/
/*MATRESHKA_SNAPSHOT_END*/
```

Do not hand-edit that block. It is maintained only by the packaged run-state synchronizer or an equivalent controller-owned atomic operation.

If run-state writes are unavailable, keep the same information inline/progress and state that the dashboard is unavailable.

## A1 — embedded last-known-good snapshot

The dashboard must remain useful when sibling `dashboard-state.js` cannot be loaded by the host viewer (`data:`/preview/file restrictions, missing sibling resource, temporary read error).

Therefore:

1. `dashboard-state.js` remains the fresh projection when reachable;
2. `dashboard.html` carries the last-known-good synchronized snapshot inside the marked block;
3. the page renders the embedded snapshot immediately, then overlays live state when the sibling script loads;
4. when live loading fails, the page visibly labels the data as a snapshot/stale-capable projection rather than going blank;
5. a render exception must not permanently kill future polling;
6. a broken new state must never overwrite the last valid embedded snapshot.

Snapshot state is still projection only. It cannot supersede ledger/current evidence.

## A2 — atomic run-state synchronizer

When the current host exposes the active Matreshka package path and local command execution for authorized run-state writes, prefer:

```text
python3 -B <plugin-root>/scripts/sync_run_state.py \
  .matreshka/runs/<run-id>
```

Run it after a meaningful dashboard-state update and before relying on the projection for handoff/recovery.

The helper is intentionally narrow:

- parses/validates `dashboard-state.js`;
- checks deterministic stage/projection invariants;
- derives only non-semantic exact timestamps that are mechanically provable;
- atomically rewrites normalized dashboard state;
- atomically refreshes the embedded HTML snapshot;
- leaves the previous last-known-good dashboard untouched on validation failure.

It **does not** start a server, bind a port, open a browser, install anything, kill processes, modify product code/tests/ledger/`DESIGN.md`, use Git/network/secrets/remotes, or grant authority.

The command itself requires the same run-state write + local-command authority already needed for those changes. If executing the helper is unavailable, use an equivalent host-native atomic write/validation path and record the weaker guarantee; never pretend synchronization ran.

## A3 — stage transition invariants

`stageOrder` is explicit state, not model memory. Default development order:

```text
source -> g1 -> spec -> g2 -> plan -> implementation -> review -> technical -> g4 -> finish
```

Rules:

1. duplicate stage IDs are invalid;
2. a stage with `ACTIVE`/`IN_PROGRESS` needs an exact `startedAt`;
3. two active stages are invalid unless the exact pair appears in `stateIntegrity.allowedConcurrentStagePairs`;
4. an earlier stage may not remain active after a later sequential stage has started;
5. the synchronizer may fill a missing `finishedAt` **only** when the stage is already semantically terminal and an exact later `startedAt` (or exact run `finishedAt`) proves the timestamp;
6. the synchronizer must never convert `ACTIVE`, `PARTIAL`, `BLOCKED`, `FAILED`, etc. into `PASS` merely because work moved forward;
7. contradictions block snapshot refresh and return to controller reconciliation.

This distinction is intentional: mechanical time/state consistency may be derived; semantic success may not.

## State integrity metadata

Project compact integrity state:

```text
stateIntegrity.status                  PASS | PARTIAL | PENDING
stateIntegrity.findingsCount
stateIntegrity.lastSyncedAt
stateIntegrity.snapshotUpdatedAt
stateIntegrity.normalizations[]
stateIntegrity.allowedConcurrentStagePairs[]
stateIntegrity.source
```

`PARTIAL` means safe mechanical normalization occurred or a non-blocking warning remains. A hard contradiction causes synchronizer failure and preserves the previous snapshot.

## Safe state shape

Project only compact user-benefit fields:

- run ID/title/locale/scenario/mode/profile/tier;
- summarized effective authority;
- `stageOrder`, stage/task status and timing;
- U requirement counts / brief coverage;
- security proof counts;
- latest authoritative test counts;
- technical verification and blind acceptance;
- browser/E2E status when applicable;
- Project Intelligence summary;
- Design Intelligence summary;
- timing/timestamps when evidenced;
- token usage only from host counters;
- state-integrity metadata;
- last verified checkpoint and exact next action;
- offset-aware `updatedAt` when available.

Never project secrets/env contents, credentials/cookies/private payloads/customer data, raw prompts/hidden reasoning, raw logs, full topology/interface/design history, private screenshots, personal browser data, or permission-expanding prose.

## Project Intelligence metrics

Recommended compact object:

```text
intelligence.topologyStatus
intelligence.areaCount
intelligence.affectedAreas
intelligence.currentArea
intelligence.interfacesTotal
intelligence.interfacesFrozen
intelligence.interfaceStatus
intelligence.runtimeStatus
intelligence.runtimeServices
intelligence.docsStatus
intelligence.specialist
intelligence.contextGuarantee
```

Counts come from validated controller state. Runtime status is descriptive. Specialist labels add no authority/budget. Drift/conflict statuses stay visibly non-green.

## Design Intelligence metrics

Recommended compact object:

```text
design.relevant
design.status
design.contractPath
design.identity
design.direction
design.prototypeStatus
design.contextGuarantee
design.reviewStatus
design.visualStatus
design.driftStatus
design.screensChecked
design.evidenceCount
design.blockedReason
```

Root `DESIGN.md` path/identity come only from controller state. Prototype existence is not production approval. Design review/visual state never implies E2E or G4 PASS. Apple-inspired design core is never shown as an Apple visual-style badge.

## Timing metrics

Timing is evidence-backed observability, not model memory.

When host exposes a trustworthy clock:

1. record run start before first state-changing action;
2. record meaningful stage/task transition timestamps when they actually occur;
3. record finish only at terminal local status/handoff;
4. derive wall-clock from exact timestamps;
5. derive implementation/fix/reverify time only from known intervals.

Use `EXACT`, `PARTIAL`, `UNAVAILABLE`. Never call wall-clock active compute time. Do not use an arbitrary idle-gap heuristic as exact development time; if active intervals are not known, report wall-clock and the limitation.

## Token/usage metrics

Runtime token counts remain host telemetry only:

- `EXACT` — all relevant compatible counters are available and aggregate without double count;
- `PARTIAL` — exact observed subset only;
- `UNAVAILABLE` — no authoritative compatible counter.

Never estimate runtime tokens from characters, byte budgets, time, message count or model family. Static context-budget tooling measures package bytes only and must not be displayed as runtime token usage.

## A4 — context-cost guardrail

Package instruction growth is a separate engineering metric from runtime usage.

Use:

```text
python3 -B <plugin-root>/scripts/check_context_budget.py <plugin-root>
```

against `evals/context-budget.json`.

This gate measures exact UTF-8 bytes for declared hot-path surfaces (`build-entry-core`, `controller-preflight-core`, `ui-design-increment`) plus a single-file ceiling. It intentionally does **not** estimate model tokens.

Budget changes require an explicit reviewed config change. Do not solve a budget failure by deleting safety/acceptance requirements; prefer deduplication, progressive disclosure, moving human rationale out of hot-path instructions, or narrowing mandatory reads.

## Test metrics

Show latest authoritative applicable gate counts, not cumulative RED/GREEN/retry sums. Re-running a suite must not inflate counts.

## Visual/layout requirements

Dashboard must remain readable at desktop/mobile widths without overlap:

- shrink-safe `minmax(0,1fr)` grids;
- long statuses/hashes/paths/task titles/design directions may wrap;
- no giant fixed text for long states;
- localized prominent labels when available;
- hierarchy: progress -> metrics -> stages -> Project Intelligence -> Design/UX -> task flow -> verification/authority -> checkpoint/next action.

Dashboard remains dependency-free.

## Update events

Update projection after meaningful controller transitions, not every thought:

- mode/envelope/ledger init;
- Project Intelligence init/material refresh;
- design relevance/recon/`DESIGN.md`/direction/identity changes;
- source brief/requirements/G1;
- spec/G2;
- plan/interface freeze/context routing/G3;
- task launch/return/review/fix when state materially changes;
- technical verification;
- Design Review/Visual Design Check;
- G4;
- Design Drift Gate;
- Documentation Drift Gate;
- blocker/stop/rescope/handoff/finish.

After writing `dashboard-state.js`, perform the atomic synchronization step when that mechanism is available/authorized. A synchronization failure is an observability blocker to reconcile, not proof that product work failed.

## Opening/serving policy

Dashboard display is runtime capability, not package guarantee.

Dashboard creation never authorizes HTTP server/listener, port bind, network, preview dependency, browser launch, runtime start/stop or host configuration. If an already-authorized host viewer can open the local file safely, use it. Otherwise give the exact path and continue. Engineering/design success never depends on dashboard display.

## Reconciliation

On resume/mismatch:

1. inspect actual state/fresh evidence;
2. reconcile controller ledger;
3. reconcile source requirements/G1-G4;
4. reconcile Project Intelligence;
5. reconcile current `DESIGN.md` identity/design evidence/drift;
6. reconcile timing/usage only from trustworthy records;
7. validate stage/projection invariants;
8. refresh dashboard state/snapshot only when authorized;
9. record mismatch + exact next action.

A stale or broken screen is an observability defect, never proof that product/design is complete or incomplete.
