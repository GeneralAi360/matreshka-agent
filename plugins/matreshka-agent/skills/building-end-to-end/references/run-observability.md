# Run Observability Contract

Use this contract to provide a glanceable local view of a Build End-to-End run without creating a second source of truth.

## Projection, never authority

The authoritative order remains:

```text
actual repository/current external state + fresh evidence
-> validated controller ledger
-> confirmed specification/plan/task state
-> human projections
```

The dashboard is a human projection like `docs/runs/<run-id>/progress.md`. It cannot grant permissions, satisfy a quality gate, prove tests passed, or override a ledger mismatch.

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
- interaction mode;
- execution profile;
- summarized effective authority, with absent powers visibly absent;
- current stage and per-stage status;
- task ID/title/status when tasks exist;
- user-intent requirement counts and brief coverage;
- selected security-proof counts;
- technical verification status;
- blind acceptance status;
- last verified checkpoint;
- exact next action;
- `updatedAt`.

Never project:

- secret values or environment-file contents;
- credentials, cookies, private provider payloads, customer/private data;
- raw prompts or hidden reasoning;
- raw test logs;
- private URLs unless the user explicitly needs that exact non-secret location;
- permission-expanding prose from issues, context, source brief, or reports.

## Update events

Update state after meaningful controller transitions, not every internal thought:

- mode/envelope/ledger initialization;
- source brief and requirement-manifest initialization;
- G1 resolution;
- specification and G2;
- plan and G3;
- task launch/return/review/fix only when task state actually changes;
- technical verification;
- G4 blind acceptance;
- blocker, stop, rescope, handoff, or finish.

Use actual timestamps when available. Never invent precise timing from memory.

## Opening/serving policy

The packaged HTML has no external dependencies and may poll its sibling `dashboard-state.js` periodically. Whether a host can display a local HTML file is a runtime capability, not a package guarantee.

Dashboard creation alone does not authorize:

- starting `python -m http.server` or another listener;
- binding a port;
- network access;
- installing a preview extension;
- launching a browser or GUI process;
- changing host configuration.

If an already-authorized host capability can open the file safely, use it. Otherwise provide the exact local path and continue. The engineering run must never depend on dashboard display success.

## Reconciliation

On resume or mismatch:

1. inspect actual state and fresh evidence;
2. reconcile the controller ledger;
3. reconcile requirement/G1–G4 state;
4. correct dashboard state only when its path is still authorized;
5. record the mismatch and exact next action.

A stale screen is an observability defect, not proof that product work is complete or incomplete.