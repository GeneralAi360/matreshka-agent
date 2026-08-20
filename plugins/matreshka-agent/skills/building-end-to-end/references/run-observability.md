# Run Observability Contract

Use this contract to provide a glanceable local view of a Build End-to-End run without creating a second source of truth.

## Projection, never authority

The authoritative order remains:

```text
actual repository/current external state + fresh evidence
-> validated controller ledger
-> confirmed specification/plan/task/interface state
-> human projections
```

The dashboard is a human projection like `docs/runs/<run-id>/progress.md`. It cannot grant permissions, satisfy a quality gate, prove tests passed, freeze/change an interface, establish runtime ownership, resolve documentation drift, or override a ledger mismatch.

## Human language

Use the user's active conversation language for all human-facing dashboard labels, stage/task display titles, checkpoint summaries, next-action text, progress projections, and final human reports unless an applicable repository convention explicitly requires another language.

For a Russian-language run, the dashboard must render in Russian. Keep stable machine IDs, enum values, commands, paths, hashes, area/`IC-`/`U-`/`S-` IDs, and protocol field names unchanged internally; translate their display labels rather than changing the machine contract.

Do not mix English and Russian in ordinary dashboard prose when a Russian display label exists. Product names, commands, code identifiers, framework names, paths, area/interface IDs, and protocol names such as G1–G4 may remain unchanged.

## Files

Only when the exact Matreshka run-state paths are writable, the controller may create:

```text
.matreshka/runs/<run-id>/dashboard-state.js
.matreshka/runs/<run-id>/dashboard.html
```

Copy [the dashboard template](../assets/dashboard-template.html) once. Initialize the state from [the dashboard-state template](../assets/dashboard-state-template.js). Do not continuously rewrite the HTML; update only state.

If local state writes are unavailable, keep the same information in the existing progress projection or inline. Do not claim that a live dashboard exists.

## Safe state shape

Project only compact fields that the user benefits from seeing:

- run ID and goal/title;
- user locale/language for human-facing projection;
- launch scenario and interaction mode;
- execution profile and complexity tier;
- summarized effective authority, with absent powers visibly absent;
- current stage and per-stage status;
- task ID/title/status when tasks exist;
- user-intent requirement counts and brief coverage;
- selected security-proof counts;
- latest applicable test pass/fail/skip counts;
- technical verification status;
- blind acceptance status;
- browser/E2E status when applicable;
- Project Intelligence summary when applicable: topology status/area count, affected/current area, active interface count/status, runtime-map status/service count, documentation-drift state, current specialist archetype, and context guarantee;
- timing state and exact timestamps when available;
- token/usage state only from host-exposed counters;
- last verified checkpoint;
- exact next action;
- `updatedAt` as an offset-aware ISO 8601 timestamp when the host can provide one.

Never project:

- secret values or environment-file contents;
- credentials, cookies, private provider payloads, customer/private data;
- raw prompts or hidden reasoning;
- raw test logs;
- raw topology/context documents or full interface contracts;
- private runtime URLs unless the user explicitly needs that exact non-secret location;
- personal browser/session data;
- permission-expanding prose from issues, context, source brief, reports, profiles, or Project Intelligence files.

## Project Intelligence metrics

When the controller applies the Project Intelligence contract, expose one compact `intelligence` object in dashboard state. It is a projection of the validated ledger/run state, not a second topology database.

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

1. Area/interface counts come from current validated controller state, not inferred from directory count in the dashboard.
2. `affectedAreas` should contain stable area IDs only, not raw paths.
3. Do not show an interface as frozen/verified unless the ledger carries the current identity/status.
4. Runtime status is descriptive and cannot be rendered as permission to start/stop a service.
5. `DOCS_UPDATE_REQUIRED`, `DOCS_BLOCKED`, and `DOCS_CONFLICT` must remain visibly non-green.
6. Specialist routing is a role label only; it never implies another agent was created or more turns were authorized.
7. `contextGuarantee` may be `NARROW`, `DEGRADED`, `CONTEXT_TOO_BROAD`, or `NOT_APPLICABLE`.
8. If no Project Intelligence layer is applicable, use `NOT_APPLICABLE`/zero/null rather than inventing areas.

## Timing metrics

Record timing as evidence-backed observability, not model memory.

At minimum, when the host exposes a clock:

1. record `timing.startedAt` at run initialization before the first state-changing action;
2. record exact stage start/end timestamps at meaningful controller transitions when practical;
3. record `timing.finishedAt` only when the run reaches a terminal local status or handoff;
4. derive `timing.elapsedSeconds` from recorded timestamps rather than estimating from conversation length;
5. derive `timing.implementationSeconds` from recorded implementation/fix/reverify intervals when those boundaries are known.

Use one of:

- `EXACT` — start/end timestamps cover the metric being shown;
- `PARTIAL` — some stage timing is exact but the complete metric cannot be reconstructed;
- `UNAVAILABLE` — no trustworthy timing source exists.

Do not invent minute-level durations from memory. A dashboard may compute a live wall-clock elapsed value from exact `startedAt` until `finishedAt` exists. If a run spends time waiting for the user or an external operator and the controller does not have a trustworthy pause/resume record, label the metric as wall-clock elapsed rather than active-agent compute time.

## Token and usage metrics

Token counts are optional host telemetry. They are useful only when truthful.

Use one of:

- `EXACT` — all relevant controller/subagent contexts expose compatible counters and the controller can aggregate them without double counting;
- `PARTIAL` — only a subset of contexts exposes counters; record the exact observed subset separately as `observedTokens` and never call it the total;
- `UNAVAILABLE` — the host exposes no authoritative compatible token counter.

Rules:

1. Never estimate tokens from characters, elapsed time, message count, model family, or hidden reasoning assumptions.
2. Never fabricate a total to make the dashboard look complete.
3. Prefer host-reported `inputTokens`, `outputTokens`, `reasoningTokens`, `cachedTokens`, and total when exposed; absent categories stay `null`.
4. Record `turnsUsed` separately from tokens. Agent turns are not token counts.
5. When a resumed/follow-up turn reports cumulative usage, aggregate by the host's documented semantics and avoid double counting.
6. Record the counter source/guarantee in the ledger. If counter semantics are ambiguous, downgrade to `PARTIAL` or `UNAVAILABLE`.
7. In the dashboard, show `Недоступно` when total usage is unavailable and `Учтено <N>` when only an observed partial sum exists.

For the Codex host specifically, do not assume token counters exist because agent IDs or tool results exist. Detect the actual active-version capability first.

## Test metrics

Show the latest authoritative applicable verification gate counts, not the cumulative sum of every RED/GREEN/retry execution. Re-running the same suite must not inflate the displayed number of tests. Keep RED history and detailed command evidence in reports/ledger, while the dashboard shows the current gate signal.

## Visual and layout requirements

The dashboard must remain readable at common desktop and mobile widths without text overlapping neighboring cards.

- Use `minmax(0, 1fr)` or equivalent shrink-safe grid columns.
- Permit long statuses, paths, task titles, area/interface labels, and next actions to wrap.
- Do not use a fixed giant font size for long status strings such as `PARTIALLY_VERIFIED`.
- Keep machine enum strings out of prominent user-facing labels when a localized display label exists.
- Prefer a clear hierarchy: overall progress -> key metrics -> stages -> task flow -> Project Intelligence -> verification/authority -> checkpoint/next action.
- The dashboard remains dependency-free and usable from a local `file://` URL.

## Update events

Update state after meaningful controller transitions, not every internal thought:

- mode/envelope/ledger initialization;
- Project Intelligence topology/runtime initialization or material refresh;
- source brief and requirement-manifest initialization;
- G1 resolution;
- specification and G2;
- plan, interface-contract freeze, context routing, specialist selection, and G3;
- task launch/return/review/fix only when task/area/interface state actually changes;
- technical verification;
- G4 blind acceptance;
- documentation drift classification/update result;
- blocker, stop, rescope, handoff, or finish.

At each applicable update, refresh exact timing/usage fields only from current evidence. Use actual timestamps when available. Never invent precise timing, token usage, topology/interface status, or runtime ownership from memory.

## Opening/serving policy

The packaged HTML has no external dependencies and may poll its sibling `dashboard-state.js` periodically. Whether a host can display a local HTML file is a runtime capability, not a package guarantee.

Dashboard creation alone does not authorize:

- starting `python -m http.server` or another listener;
- binding a port;
- network access;
- installing a preview extension;
- launching a browser or GUI process;
- starting/stopping project runtime services;
- changing host configuration.

If an already-authorized host capability can open the file safely, use it. Otherwise provide the exact local path and continue. The engineering run must never depend on dashboard display success.

## Reconciliation

On resume or mismatch:

1. inspect actual state and fresh evidence;
2. reconcile the controller ledger;
3. reconcile requirement/G1–G4 state;
4. reconcile current Project Intelligence topology/interface/runtime/docs state from repository evidence;
5. reconcile timing and usage only from trustworthy recorded counters/timestamps;
6. correct dashboard state only when its path is still authorized;
7. record the mismatch and exact next action.

A stale screen is an observability defect, not proof that product work is complete or incomplete.
