# Matreshka Agent 0.5 — Autopilot v1.0.1+ Regression Hardening

- Date: 2026-08-21
- Branch: `dev/0.5-brief-traceability-observability`
- Source audit: `nick-vels/skills` v1.0.1 plus post-v1.0.1 fixes on `main`
- Scope: regression classes that could plausibly affect Matreshka 0.5
- Release policy: no `0.5.0` claim from this audit alone

## Why this pass exists

Autopilot's own v1.0.1 audit fixed major execution-quality gaps (real RED before code, root-cause repair, reviewer inputs, state survival through compaction). Subsequent real runs then exposed additional failures in dashboard/state plumbing and transition bookkeeping.

Matreshka had already avoided most Autopilot-specific server/PID/path architecture, but this pass found five transferable risk classes worth closing before native full-stack acceptance.

## Result

| ID | Risk | Matreshka result |
| --- | --- | --- |
| A1 | dashboard blank/stale when sibling state cannot load | `IMPLEMENTED` — embedded last-known-good snapshot + visible stale mode + render recovery |
| A2 | repeated manual state-update ritual drifts | `IMPLEMENTED` — `sync_run_state.py`, validation + atomic projection writes, no server/PID/port logic |
| A3 | previous stage remains active after later stage begins | `IMPLEMENTED` — explicit `stageOrder`, concurrency allowlist, mechanical invariant rejection |
| A4 | instruction hot-path grows until context cost explodes | `IMPLEMENTED` — exact byte budgets + CI regression gate |
| A5 | one successful native run mistaken for stable behavior | `IMPLEMENTED_AS_RELEASE_CONTRACT` — 6 blocking properties × 5 repetitions; native results still required |

`IMPLEMENTED` here means package contract/tooling is present and wired. It does not mean native repeatability evidence already exists.

## A1 — embedded dashboard snapshot

### Failure class

A host preview may inline/open `dashboard.html` in a context where sibling `dashboard-state.js` is inaccessible. A dashboard that depends only on the sibling file becomes blank or permanently stale even while run state exists on disk.

### Matreshka fix

`dashboard-template.html` now contains:

```text
/*MATRESHKA_SNAPSHOT_START*/
window.MATRESHKA_RUN_STATE_SNAPSHOT=...
/*MATRESHKA_SNAPSHOT_END*/
```

Behavior:

1. render embedded snapshot immediately when present;
2. poll sibling live state when the host permits it;
3. live state replaces snapshot when available;
4. failed live load falls back to the last known state and visibly labels it as a snapshot;
5. render exceptions do not permanently stop future polling;
6. invalid new state cannot overwrite the previous embedded snapshot because synchronization validates before writing.

The snapshot is projection only; ledger/current evidence still outrank it.

## A2 — atomic run-state synchronizer

Added:

```text
plugins/matreshka-agent/scripts/sync_run_state.py
```

It performs only run-projection maintenance:

```text
parse state
→ validate deterministic invariants
→ derive only mechanically provable terminal timestamps
→ atomic dashboard-state.js replace
→ atomic marked-snapshot refresh
```

Explicit non-capabilities:

```text
NO HTTP server
NO PID ownership
NO port binding
NO process kill/start
NO browser launch
NO network
NO Git
NO product/test/DESIGN.md/ledger mutation
```

This deliberately takes the useful lesson from Autopilot's `sync.py` without adopting its host/process lifecycle complexity.

The script includes `--self-test` covering successful normalization, parseability, embedded snapshot update, conflicting active-stage rejection, and preservation of the previous dashboard on invalid state.

## A3 — stage transition invariants

Dashboard state now declares a canonical `stageOrder`:

```text
source
→ g1
→ spec
→ g2
→ plan
→ implementation
→ review
→ technical
→ g4
→ finish
```

`stateIntegrity.allowedConcurrentStagePairs` is explicit and empty by default.

Mechanical rules:

- duplicate stage IDs fail;
- active stage requires exact `startedAt`;
- multiple active stages fail unless exact pair is allowlisted;
- an earlier sequential stage cannot remain active once a later stage has started;
- missing `finishedAt` can be derived only for a stage whose semantic status is already terminal and only from an exact later timestamp;
- chronology never upgrades a stage to PASS/VERIFIED/APPROVED.

This is intentionally stricter than simply auto-closing stages: state consistency can be inferred; success cannot.

## A4 — context-cost guardrail

Added:

```text
plugins/matreshka-agent/evals/context-budget.json
plugins/matreshka-agent/scripts/check_context_budget.py
```

The metric is exact UTF-8 bytes, not fake token estimation.

Initial protected surfaces:

```text
build-entry-core          max 50,000 bytes
controller-preflight-core max 110,000 bytes
ui-design-increment       max 65,000 bytes
single file               max 32,000 bytes
```

The current declared surfaces fit inside those ceilings by repository-size inspection. A future growth regression fails CI unless the budget/config change is explicit and reviewed.

Runtime dashboard token telemetry is unchanged: only host-reported `EXACT | PARTIAL | UNAVAILABLE` counts may be shown.

## A5 — repeated native behavior evidence

Added:

```text
plugins/matreshka-agent/evals/native-repeatability.json
plugins/matreshka-agent/scripts/evaluate_native_repeatability.py
```

Release-blocking scenarios:

1. real RED before production code;
2. frozen `IC-xx` is not silently redefined;
3. frozen `DESIGN.md` identity is not silently rewritten;
4. `FULL_AUTO` does not widen permissions;
5. G4 refuses/flags contaminated inputs;
6. Design Review/Visual Design Check catches material design drift even when E2E passes.

Each scenario requires 5 repetitions per host claimed for release. Native result evaluation requires every required repetition to be present and `PASS`.

CI uses `--validate-plan` only. That proves the matrix is intact, **not** that a host already passed 30 native runs.

## CI integration

The development workflow now runs:

```text
validate_dev_05.py --self-test
→ check_dev_05.py
→ check_dev_05_behavioral_contracts.py
→ sync_run_state.py --self-test
→ check_context_budget.py
→ evaluate_native_repeatability.py --validate-plan
→ check_autopilot_regressions.py
→ doctor_dev_05.py
```

`check_autopilot_regressions.py` specifically fails if A1–A5 files/markers lose their wiring to controller observability or CI.

## What was deliberately NOT copied from Autopilot

- no global or run-owned HTTP dashboard server requirement;
- no PID-file lifecycle;
- no port reuse/kill heuristics;
- no broad process cleanup;
- no `git mv` run-directory lifecycle;
- no idle-gap heuristic presented as exact active development time;
- no runtime token estimates from package text size;
- no auto-Git authority.

## Current evidence boundary

Package implementation/wiring for A1–A5 is complete.

Still required before a release claim:

```text
final-head deterministic CI result
+ disposable full-stack native acceptance
+ native repeatability result set for each release-claimed host
```

Until those execute successfully, the accurate label remains `0.5 development preview`.
