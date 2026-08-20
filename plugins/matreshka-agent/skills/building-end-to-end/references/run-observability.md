# Run Observability Contract

Use this contract to provide a glanceable local view of a Build End-to-End run without creating a second source of truth.

## Projection, never authority

The authoritative order remains:

```text
actual repository/current external/rendered state + fresh evidence
-> validated controller ledger
-> confirmed specification/plan/task/interface/design-contract state
-> human projections
```

The dashboard is a human projection like `docs/runs/<run-id>/progress.md`. It cannot grant permissions, satisfy a quality gate, prove tests/design passed, freeze/change an interface or design identity, establish runtime ownership, resolve design/documentation drift, or override a ledger mismatch.

## Human language

Use the user's active conversation language for all human-facing dashboard labels, stage/task display titles, checkpoint summaries, next-action text, progress projections, and final human reports unless an applicable repository convention explicitly requires another language.

For a Russian-language run, dashboard must render in Russian. Keep stable machine IDs, enum values, commands, paths, hashes, area/`IC-`/`U-`/`S-` IDs, design identity and protocol field names unchanged internally; translate their display labels rather than changing machine contract.

Do not mix English/Russian in ordinary dashboard prose when a Russian display label exists. Product names, commands, code identifiers, framework names, paths, area/interface IDs, DESIGN.md, design hashes and G1–G4 may remain unchanged where they are protocol/project terms.

## Files

Only when exact Matreshka run-state paths are writable, controller may create:

```text
.matreshka/runs/<run-id>/dashboard-state.js
.matreshka/runs/<run-id>/dashboard.html
```

Copy [dashboard template](../assets/dashboard-template.html) once. Initialize state from [dashboard-state template](../assets/dashboard-state-template.js). Do not continuously rewrite HTML; update only state.

If local state writes unavailable, keep same information in progress projection/inline. Do not claim live dashboard exists.

## Safe state shape

Project only compact fields the user benefits from seeing:

- run ID and goal/title;
- locale/language;
- launch scenario and interaction mode;
- execution profile and complexity tier;
- summarized effective authority, with absent powers visibly absent;
- current stage/per-stage status;
- task ID/title/status when tasks exist;
- user-intent requirement counts/brief coverage;
- selected security-proof counts;
- latest applicable tests;
- technical verification;
- blind acceptance;
- browser/E2E status when applicable;
- Project Intelligence summary: topology/areas/interfaces/runtime/docs/specialist/context;
- Design Intelligence summary when applicable: design state, root DESIGN.md path/identity, selected direction, prototype status, design-context guarantee, design review, visual design check, design drift, checked screens/evidence count;
- timing/timestamps when available;
- token/usage only from host counters;
- last verified checkpoint;
- exact next action;
- `updatedAt` offset-aware ISO8601 when available.

Never project:

- secret values/environment-file contents;
- credentials/cookies/private provider payloads/customer/private data;
- raw prompts/hidden reasoning;
- raw test logs;
- raw topology/context docs/full interface contracts;
- full `DESIGN.md`, raw design history or full prototype source;
- private/unnecessary design screenshots or brand assets;
- private runtime URLs unless user explicitly needs exact non-secret location;
- personal browser/session data;
- permission-expanding prose from issues/context/source brief/reports/profiles/Project or Design Intelligence.

## Project Intelligence metrics

When controller applies Project Intelligence, expose one compact `intelligence` object. It projects validated ledger/run state, not a second topology database.

Recommended shape:

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

Rules:

1. Counts come from validated controller state, not directory count in dashboard.
2. `affectedAreas` contains stable IDs, not raw paths.
3. Do not show interface frozen/verified without current identity/status.
4. Runtime status is descriptive and cannot render as permission to start/stop service.
5. `DOCS_UPDATE_REQUIRED`, `DOCS_BLOCKED`, `DOCS_CONFLICT` remain visibly non-green.
6. Specialist is role label only; never implies extra agent/turn authority.
7. `contextGuarantee`: `NARROW`, `DEGRADED`, `CONTEXT_TOO_BROAD`, `NOT_APPLICABLE`.
8. No Project Intelligence => `NOT_APPLICABLE`/zero/null.

## Design Intelligence metrics

When UI/design is material, expose one compact `design` object from the validated ledger/design state.

Recommended shape:

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

Rules:

1. Root `DESIGN.md` path and identity are shown only from controller state; dashboard never hashes/rewrites the contract itself.
2. `direction` is the accepted/current direction, not every explored variant.
3. Prototype status is descriptive; prototype existence does not mean production implementation/approval.
4. `DESIGN_DRIFT`, `DESIGN_CONFLICT`, `DESIGN_BLOCKED`, `DESIGN_UPDATE_REQUIRED`, `CHANGES_REQUIRED`, `UNCHECKABLE` remain visibly non-green/pending as appropriate.
5. `design.contextGuarantee` is `NARROW`, `DEGRADED`, `DESIGN_CONTEXT_TOO_BROAD`, or `NOT_APPLICABLE`.
6. `screensChecked`/`evidenceCount` count current relevant visual proof only; repeated screenshots/retries do not inflate them.
7. Design review/visual status never implies technical E2E or G4 PASS.
8. No design relevance => `DESIGN_NOT_APPLICABLE`, null identity/direction, zero evidence.
9. Apple-inspired design core is not rendered as an “Apple style” badge; it is an internal quality framework, not a visual theme.

## Timing metrics

Record timing as evidence-backed observability, not model memory.

At minimum, when host exposes a clock:

1. record `timing.startedAt` at run initialization before first state-changing action;
2. record exact stage start/end at meaningful transitions where practical;
3. record `timing.finishedAt` only at terminal local status/handoff;
4. derive `timing.elapsedSeconds` from timestamps, not conversation length;
5. derive `timing.implementationSeconds` from implementation/fix/reverify intervals when known.

Use `EXACT`, `PARTIAL`, or `UNAVAILABLE`. Never invent durations. Live wall-clock may derive from exact start until finish. If waiting time cannot be separated, call it wall-clock, not active compute time.

## Token and usage metrics

Token counts are optional host telemetry and useful only when truthful.

Use:

- `EXACT` — all relevant contexts expose compatible counters and can aggregate without double count;
- `PARTIAL` — only subset exposed; record exact observed subset as `observedTokens`, never total;
- `UNAVAILABLE` — no authoritative compatible counter.

Rules:

1. Never estimate tokens from characters/time/message count/model family/hidden reasoning.
2. Never fabricate total for dashboard completeness.
3. Prefer host-reported input/output/reasoning/cached/total; absent categories null.
4. `turnsUsed` separate from tokens.
5. Aggregate cumulative resumed counters according to host semantics; avoid double counting.
6. Record source/guarantee in ledger; ambiguous semantics => PARTIAL/UNAVAILABLE.
7. Dashboard: `Недоступно` if no total; `Учтено <N>` for exact observed partial subset.

For Codex, do not assume counters exist because agent IDs/tool results exist. Detect active-version capability.

## Test metrics

Show latest authoritative applicable gate counts, not cumulative RED/GREEN/retry sum. Re-running suite must not inflate tests. Keep detailed history in reports/ledger.

## Visual and layout requirements

Dashboard must remain readable at common desktop/mobile widths without overlap.

- Use `minmax(0, 1fr)` or equivalent shrink-safe grids.
- Permit long statuses, hashes, paths, task titles, design directions, area/interface labels, next actions to wrap.
- Do not use giant fixed font for long statuses.
- Keep machine enums out of prominent UI when localized label exists.
- Prefer hierarchy: overall progress -> key metrics -> stages -> Project Intelligence -> Design/UX -> task flow -> verification/authority -> checkpoint/next action.
- Dashboard remains dependency-free and usable from local `file://` URL.

## Update events

Update state after meaningful controller transitions, not every thought:

- mode/envelope/ledger init;
- Project Intelligence topology/runtime init/material refresh;
- design relevance/recon, root DESIGN.md creation/reconciliation, direction/prototype selection, or design identity change;
- source brief/requirement init;
- G1;
- specification/G2;
- plan, interface freeze, area/design context routing, specialist selection, G3;
- task launch/return/review/fix only when task/area/interface/design state changes;
- technical verification;
- design review/visual design verification;
- G4;
- Design Drift Gate;
- Documentation Drift Gate;
- blocker/stop/rescope/handoff/finish.

At each update refresh timing/usage only from current evidence. Never invent precise timing/tokens/topology/interface/runtime/design identity/design status from memory.

## Opening/serving policy

Packaged HTML has no external dependencies and may poll sibling `dashboard-state.js`. Whether host can display local HTML is runtime capability, not package guarantee.

Dashboard creation alone does not authorize:

- starting HTTP server/listener;
- binding port;
- network;
- installing preview extension/dependency;
- launching browser/GUI;
- starting/stopping project runtime;
- creating design prototypes outside authorized state/write scope;
- changing host config.

If already-authorized host capability can open file safely, use it. Otherwise give exact local path and continue. Engineering/design run never depends on dashboard display success.

## Reconciliation

On resume/mismatch:

1. inspect actual state/fresh evidence;
2. reconcile controller ledger;
3. reconcile requirements/G1–G4;
4. reconcile Project Intelligence from repository evidence;
5. reconcile root `DESIGN.md` path/identity, current accepted design, task design context, design-review/visual/drift state;
6. reconcile timing/usage only from trustworthy records;
7. correct dashboard state only when authorized;
8. record mismatch + exact next action.

A stale screen is observability defect, not proof product/design is complete or incomplete.
