# Matreshka Agent 0.5 — Component Hardening Audit

- Audit date: 2026-08-20
- Branch: `dev/0.5-brief-traceability-observability`
- Audited implementation snapshot before this audit commit: `2fa828f093302d3195503514ac21098e78dab246`
- Baseline `main`: `7249a56e9afb5f5b70e56ddd0dc272e6bdab9ea0`
- Release status: `DEVELOPMENT_PREVIEW`
- Versioned manifests during audit: `0.4.0` by deliberate release policy

## Verdict model

This audit separates three claims that must not be conflated:

- `PRESENT` — required files/contracts/assets exist in the branch;
- `WIRED` — the feature is connected through the relevant controller/planner/task/review/verification/finish/recovery/observability seams;
- `NATIVE_PROVEN` — the behavior has been exercised on a real supported host against the current implementation snapshot.

Static presence/wiring cannot by itself prove native host behavior.

## Overall result

- Component inventory: `STATIC_PASS`
- Cross-component wiring review: `STATIC_PASS`
- Development hardening defects found and corrected: `YES`
- Existing native core evidence: `PARTIAL / older snapshot`
- Latest Browser + Project Intelligence native evidence: `PENDING`
- Observable GitHub Actions result for final development HEAD from the current connector: `UNAVAILABLE`
- `0.5.0` release claim: `NOT_ALLOWED_YET`

No implementation component from the confirmed 0.5 scope is intentionally left in `PENDING_IMPLEMENTATION`. Remaining items are execution/release evidence gates.

## Component matrix

| Component | Present | Wired | Native evidence | Audit verdict |
| --- | --- | --- | --- | --- |
| Build End-to-End entry | yes | entry → namespaced controller | older Codex core run; latest launch UX not rerun | `STATIC_PASS / NATIVE_PARTIAL` |
| `INTERVIEW / ASSISTED / FULL_AUTO` | yes | entry, controller, ledger, dashboard/docs | older run exercised Assisted only | `STATIC_PASS / NATIVE_PARTIAL` |
| `NEW_PROJECT / CONTINUE_PROJECT / EXISTING_PROJECT` | yes | launch-scenario contract + controller state/recovery | latest three-way scenario matrix not yet native-rerun | `STATIC_PASS / NATIVE_PENDING` |
| `SOURCE_BRIEF` | yes | source state → controller → G2/G4 | TaskLedger older snapshot exercised source brief | `STATIC_PASS / NATIVE_PARTIAL` |
| `U-` user requirements / `S-` security | yes | spec/plan/task/review/verify/G4 | TaskLedger exercised U rows; security framework pre-existed | `STATIC_PASS / NATIVE_PARTIAL` |
| G1 | yes | before spec completion | older TaskLedger PASS | `STATIC_PASS / NATIVE_PARTIAL` |
| G2 | yes | fresh brief→spec gate | older TaskLedger PASS | `STATIC_PASS / NATIVE_PARTIAL` |
| G3 | yes | planner bidirectional task/proof gate | older TaskLedger PASS | `STATIC_PASS / NATIVE_PARTIAL` |
| G4 blind acceptance | yes | fresh restricted verifier → controller reconciliation | older TaskLedger PARTIAL, correctly blocking COMPLETE | `STATIC_PASS / NATIVE_PARTIAL` |
| Complexity T0–T3 | yes | planner/task budget/merge pass | latest tier behavior not independently benchmarked | `STATIC_PASS / NATIVE_PENDING` |
| P1 Project Topology | yes | preflight → profile/ledger/plan/dashboard/recovery | full-stack native run pending | `STATIC_PASS / NATIVE_PENDING` |
| P2 Area Context Router | yes | plan → task brief → dispatch → report/review | native context isolation pending | `STATIC_PASS / NATIVE_PENDING` |
| P3 `IC-xx` contracts | yes | controller freeze → plan/task/review/verify/docs | native producer/consumer run pending | `STATIC_PASS / NATIVE_PENDING` |
| `INTERFACE_CHANGED` status | yes | formal controller status + task stop/reconciliation | native drift case pending | `STATIC_PASS / NATIVE_PENDING` |
| P4 Runtime Map | yes | preflight/ledger/task/permission/recovery | native ownership/port case pending | `STATIC_PASS / NATIVE_PENDING` |
| P5 Documentation Drift Gate | yes | after verified behavior → finish/handoff | native public-contract drift case pending | `STATIC_PASS / NATIVE_PENDING` |
| P6 Specialist Role Routing | yes | planner/task/dispatch/review; same 10 package skills | native role-routing/budget case pending | `STATIC_PASS / NATIVE_PENDING` |
| Browser capability discovery | yes | controller/platform adapters/ledger | native current-host discovery pending | `STATIC_PASS / NATIVE_PENDING` |
| Existing E2E first | yes | verifier/browser contract | native Playwright/Cypress reuse pending | `STATIC_PASS / NATIVE_PENDING` |
| Technical Browser E2E | yes | VERIFY axis | native web fixture pending | `STATIC_PASS / NATIVE_PENDING` |
| Browser G4 | yes | ACCEPTANCE axis, separate from E2E | native browser G4 pending | `STATIC_PASS / NATIVE_PENDING` |
| Browser isolation/destructive firewall | yes | permission/controller/verifier contracts | adversarial native test pending | `STATIC_PASS / NATIVE_PENDING` |
| Russian dashboard | yes | state ↔ HTML keys reconciled | older native dashboard was pre-redesign and exposed UX defect | `STATIC_PASS / NATIVE_PENDING` |
| Timing telemetry | yes | ledger/state/dashboard/handoff | latest exact timing capture pending | `STATIC_PASS / NATIVE_PENDING` |
| Token telemetry | yes | EXACT/PARTIAL/UNAVAILABLE semantics through ledger/dashboard | older Codex run had no authoritative token counter | `STATIC_PASS / NATIVE_PARTIAL` |
| Permission envelope | yes | controller + browser/runtime/docs/Git/remote boundaries | older TaskLedger respected forbidden Git/network/etc. | `STATIC_PASS / NATIVE_PARTIAL` |
| Security by Design | yes | spec/plan/review/verify | inherited from 0.4 + still wired | `STATIC_PASS / NATIVE_PARTIAL` |
| One-writer / one-fixer-wave | yes | budgets/dispatch/review/recovery | TaskLedger exercised one fix/re-review wave | `STATIC_PASS / NATIVE_PARTIAL` |
| Recovery | yes | actual state → ledger → source/PI/interface/runtime → projections | latest PI-aware recovery pending | `STATIC_PASS / NATIVE_PENDING` |
| Planner integration | yes | U/S + topology/context/IC/runtime/docs/specialist | static complete | `STATIC_PASS / NATIVE_PENDING` |
| Reviewer integration | yes | source narrowing + frozen IC + specialist boundary + security | older review native; latest IC checks pending | `STATIC_PASS / NATIVE_PARTIAL` |
| Verifier integration | yes | technical/security + Browser E2E + G4 separation | older technical/G4 partial; browser pending | `STATIC_PASS / NATIVE_PARTIAL` |
| Finish/handoff | yes | docs gate + PI + Git/remote + Russian handoff + metrics | latest full finish pending | `STATIC_PASS / NATIVE_PENDING` |
| Platform adapters | yes | Codex/Claude/Cursor/Antigravity capability fallbacks + browser | only Codex older snapshot has native evidence | `STATIC_PASS / NATIVE_PARTIAL` |
| 10 bundled skills only | yes | package identity routing preserved | installed older dev snapshot on Codex | `STATIC_PASS / NATIVE_PARTIAL` |
| Package validator/self-tests | existing | CI + local documented command | final-head execution result not observable here | `CONFIGURED / EXECUTION_PENDING` |
| `check_dev_05.py` | yes | CI + README/local command | final-head execution result not observable here | `CONFIGURED / EXECUTION_PENDING` |
| `doctor.py` | existing | CI + local command | final-head execution result not observable here | `CONFIGURED / EXECUTION_PENDING` |
| GitHub Actions workflow | yes | validator → 0.5 integrity → doctor | current connector exposes no final-head Actions check result | `CONFIGURED / RESULT_UNAVAILABLE` |

## End-to-end wiring audit

### Entry and source intent

Verified statically:

```text
building-end-to-end
→ public mode/scenario normalization
→ SOURCE_BRIEF + SOURCE_DECISIONS
→ namespaced matreshka-agent:orchestrating-subagent-work
→ ledger/source-brief/U-manifest
→ G1
→ specification
→ G2
```

The Build wrapper/card remains namespaced for the real Matreshka invocation while preserving the canonical `$building-end-to-end` token and `[TASK]` wrapper shape expected by the current 0.4 package validator.

### Project Intelligence and planning

Verified statically:

```text
read-only repository evidence
→ PROJECT_TOPOLOGY
→ affected areas
→ required IC-xx seams
→ RUNTIME_MAP
→ planning
→ AREA_CONTEXT_SET per task
→ specialist archetype
→ G3
```

The planner cannot treat topology/context/interface/runtime state as permission. A frozen interface change has a formal controller status: `INTERFACE_CHANGED`.

### Dispatch and implementation

Verified statically:

```text
task brief
  + primary area
  + adjacent areas only when required
  + IC IDs/hashes
  + context guarantee/exclusions
  + specialist boundary
  + runtime observation
  + docs-impact candidate
→ scoped implementer dispatch
→ RED → GREEN
→ agent report with area/interface/runtime/docs observations
```

Multiple areas do not add writer budget. Remote/file-transfer operator dispatches are execution-only.

### Review and correction

Verified statically:

```text
scoped diff + task-local source intent + frozen IC
→ independent review
→ source-intent narrowing / interface drift / specialist-boundary / security findings
→ controller adjudication
→ one consolidated fixer wave on original thread
→ targeted re-review on original reviewer thread
```

### Verification / Browser / G4

Verified statically:

```text
review accepted
→ technical/security verification
→ repository-native Browser E2E when required and authorized
→ separate fresh G4
→ Browser G4 for browser-only user outcomes when trustworthy capability exists
```

`E2E PASS` does not imply G4 PASS. Browser install/start/port/test-data authority remains separate.

### Documentation and finish

Verified statically:

```text
verified current behavior
→ DOCUMENTATION_DRIFT_GATE
→ DOCS_NOT_REQUIRED / DOCS_CURRENT / authorized docs-only update / honest block-handoff
→ finishing-development-work
→ only authorized Git/remote action or local handoff
```

Human-facing handoff is Russian-first and carries Project Intelligence, Browser/E2E, G4, docs drift, timing/token limitations and exact next action.

### Recovery

Verified statically:

```text
actual repository/current evidence
→ ledger
→ source brief/U state
→ topology/area roots
→ active IC contracts
→ runtime ownership/environment
→ task/report/diff
→ context/specialist routing
→ docs drift
→ dashboard/progress projections
→ exact next action
```

Stale topology/profile/runtime/docs/dashboard state cannot override current repository evidence.

## Hardening defects found and fixed

### H-01 — Codex Build UX vs package validator

**Problem:** richer 0.5 Build wrapper/card had diverged from current 0.4 static validator expectations (`[TASK]` wrapper hint and canonical `$building-end-to-end` token).

**Fix:** restore validator-compatible shape while keeping Russian public mode/scenario hints and namespaced `$matreshka-agent:building-end-to-end` routing.

**Status:** `FIXED`.

### H-02 — Dashboard integrity checker key mismatch

**Problem:** initial `check_dev_05.py` looked for working-name `projectIntelligence`, while the real dashboard state/HTML consistently use `intelligence` / `s.intelligence`.

**Fix:** checker now validates the actual state contract and explicitly cross-checks `intelligence`, `timing`, `usage`, `tests`, `browser`, and `authority` between state and HTML.

**Status:** `FIXED`.

### H-03 — Integrity markers too coupled to draft wording

**Problem:** early static markers expected draft phrases such as `PROJECT_TOPOLOGY` in locations that intentionally used human wording such as `Project Topology`.

**Fix:** align markers to stable semantic contract phrases and expand the checker to real downstream templates instead of brittle wording-only checks.

**Status:** `FIXED`.

### H-04 — stale implementation-plan statuses

**Problem:** main 0.5, Browser and Project Intelligence plans still showed `IN_PROGRESS/PARTIAL` although implementation had moved further.

**Fix:** plans now distinguish `IMPLEMENTED`/`STATIC_HARDENING_IMPLEMENTED` from remaining native/release evidence gates. The old T5 interface-map deferral is resolved by evidence-scoped `IC-xx`, not a global decorative interface map.

**Status:** `FIXED`.

### H-05 — stale 0.4 user-facing repository docs

**Problem:** root/package README and finish handoff still presented old `GUIDED/AUTONOMOUS_LOCAL` UX or English-first output.

**Fix:** development-branch README/handoff now reflect current `INTERVIEW/ASSISTED/FULL_AUTO`, scenarios, G1–G4, Browser, Project Intelligence, Russian dashboard and metrics. Versioned manifests remain 0.4 intentionally.

**Status:** `FIXED`.

## Deterministic validation configuration

The branch configures this order in `.github/workflows/package-validation.yml` on Python 3.11:

```text
validate_package.py --self-test
→ check_dev_05.py
→ doctor.py
```

`check_dev_05.py` is read-only/offline and checks:

- required 0.5 source-intent/Browser/Project-Intelligence files;
- cross-skill wiring through controller/planner/task/review/verifier/finish;
- task/dispatch/report/handoff templates;
- dashboard state↔HTML key agreement;
- Russian launch/dashboard markers;
- the 14 required Project Intelligence adversarial cases;
- JSON syntax for major eval suites;
- plans/root README/CI development-track markers.

## What this audit still cannot claim

The current ChatGPT GitHub connector can inspect files, commits, tree state and legacy combined statuses, but it does not expose a successful push-triggered GitHub Actions check for the final development snapshot here. The final-head combined status endpoint returned no legacy statuses; this is not evidence of CI success or failure.

The current environment also does not provide a local checkout of this GitHub branch on which these Python validators can be executed directly. Therefore this audit does **not** fabricate:

- `validate_package.py --self-test PASS` on final HEAD;
- `check_dev_05.py PASS` on final HEAD;
- `doctor.py PASS` on final HEAD;
- GitHub Actions PASS;
- native Browser/Project-Intelligence PASS.

Those are the remaining evidence gates.

## Required next native acceptance

Use the final development snapshot in a fresh Codex thread and a disposable full-stack project. The acceptance must prove, in one audited run:

1. real frontend/backend/data/E2E topology without fake areas;
2. one shared frozen `IC-xx` between producer and consumer;
3. narrow backend/frontend task contexts;
4. specialist routing without profile-budget inflation;
5. Runtime Map observation and permission boundaries;
6. existing/repository-approved Playwright/E2E path;
7. Browser G4 independent from E2E;
8. Documentation Drift Gate;
9. Russian dashboard with Project Intelligence, timing and truthful token state;
10. recovery artifacts sufficient to resume without reconstructing work from conversation.

Before the native project test, execute the three deterministic commands on the same checkout and preserve their exact exit/result output.

## Release gate

`0.5.0` may be proposed only when:

```text
final-head package validation PASS
+ final-head 0.5 integrity PASS
+ doctor result reviewed
+ disposable full-stack native acceptance PASS (or consciously resolved findings)
+ native evidence for each release-claimed host
+ version/publisher/security release metadata completed
```

Until then the correct label is `0.5 development preview`, not released `0.5.0`.
