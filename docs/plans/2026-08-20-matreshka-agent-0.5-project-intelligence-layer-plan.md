# Implementation Plan — Matreshka Agent 0.5 Project Intelligence Layer

- Status: `IN_PROGRESS`
- Specification: `docs/specs/2026-08-20-matreshka-agent-0.5-project-intelligence-layer-spec.md`
- Branch: `dev/0.5-brief-traceability-observability`
- Delivery policy: development branch only; no merge to `main` or `0.5.0` release claim from this plan.

## Goal

Implement a portable Project Intelligence Layer for the existing Matreshka controller: current project topology, area-scoped context routing, shared cross-area interface contracts, safe runtime mapping, documentation-drift control, and bounded specialist role routing.

## Task map

| Task | Result | Main files | Gate |
| --- | --- | --- | --- |
| `P1` | `PROJECT_TOPOLOGY` and reusable profile shape | project-intelligence reference, project-profile reference/template | topology cases |
| `P2` | `AREA_CONTEXT_SET` routing into task briefs | project-intelligence reference, task brief/report templates | context cases |
| `P3` | Controller-owned `IC-xx` contracts for cross-area seams | interface contract template, planning template | producer/consumer cases |
| `P4` | Safe `RUNTIME_MAP` with ownership/permission separation | project-intelligence reference, profile/ledger templates | runtime cases |
| `P5` | Documentation impact/drift gate after verification | project-intelligence reference, ledger/final handoff | stale-doc cases |
| `P6` | Specialist role archetypes without authority inflation | project-intelligence reference, task/dispatch/report templates | routing/budget cases |
| `P7` | Project Intelligence observable and recoverable | ledger/dashboard projection | projection/recovery cases |
| `P8` | Package/native hardening | existing 0.5 release phase | validator/doctor/native tests |

## P1 — Project Topology

Read-only discovery must identify real architectural areas instead of assuming a frontend/backend template. Record area ID, kind, purpose, roots, entry points, verified commands and source, produced/consumed interfaces, state/data ownership, security/trust boundary, applicable instructions, and freshness identity.

Examples may include `FRONTEND`, `BACKEND`, `DATA`, `E2E`, `CLI`, `WORKER`, `QUEUE`, `MOBILE`, or repository-specific areas. A single-area project stays single-area.

## P2 — Area Context Router

Derive one minimal context package per dispatched task. Preserve relevant `U-`/`S-` rows, primary area facts, necessary adjacent interface contracts, focused commands, security/data/runtime invariants, and exact scoped paths. Exclude unrelated area history, reports, raw logs, full source brief, and broad diffs.

Return `CONTEXT_TOO_BROAD` when correctness cannot be preserved with a bounded task package.

## P3 — Cross-Area Interface Contract

For one user outcome crossing multiple area owners, create one `IC-xx` contract before dependent writers begin. Default run-local path when state writes are authorized:

```text
.matreshka/runs/<run-id>/interfaces/IC-xx-<slug>.md
```

Producer and consumer tasks reference the same contract identity/hash. A material contract change blocks dependent dispatch until controller reconciliation. Do not create an interface artifact for a single-area task with no shared seam.

## P4 — Runtime Map

Map verified service/process ownership, start/stop/status/log commands, ports when evidenced, environment class, and mutation implications. Status/log observation remains separate from process start/stop, port bind, network, and destructive authority. Unknown process ownership must never cause broad kill-by-port/process cleanup.

## P5 — Documentation Drift Gate

After fresh technical verification and before final handoff, classify:

```text
DOCS_NOT_REQUIRED
DOCS_CURRENT
DOCS_UPDATE_REQUIRED
DOCS_BLOCKED
DOCS_CONFLICT
```

Only affected authorized durable docs may be updated, and only from verified current behavior. Public interfaces, topology, runtime commands, persistence, security boundaries, environment contracts, and documented user workflows are eligible durable changes. Private refactors are not.

## P6 — Specialist Role Routing

Reuse existing Matreshka skills with narrower role archetypes instead of adding package skills solely for labels:

- `GENERAL_IMPLEMENTER`
- `FRONTEND_IMPLEMENTER`
- `BACKEND_IMPLEMENTER`
- `DATA_MIGRATION_IMPLEMENTER`
- `UI_SPECIALIST`
- `TEST_E2E_SPECIALIST`
- `DOCUMENTATION_MAINTAINER`
- `BROWSER_CHECKER`
- `REMOTE_OPERATOR` / `FILE_TRANSFER_OPERATOR` only for separately authorized remote workflows

Specialization stays inside execution-profile role/turn budgets and never grants additional permissions.

## P7 — State and observability

Extend run state/ledger with compact topology, affected/current areas, active interface IDs, runtime status/service count, documentation drift state, selected specialist, and context-package summary. Dashboard may display these values but remains a projection.

## Required adversarial cases

1. Multi-area web repository -> real frontend/backend/E2E areas detected.
2. Small CLI -> no fabricated frontend/backend areas.
3. Frontend depends on backend API -> shared interface contract before dependent dispatch.
4. Existing area docs disagree with current code -> repository wins; docs/cache marked stale.
5. Backend task context keeps required API seam but excludes unrelated UI history.
6. Unknown process owns expected port -> no broad kill; blocker/ownership resolution.
7. Status/log command exists but start permission does not -> observation only.
8. Public API changed and authoritative docs are stale -> docs gate blocks clean finish until update or handoff.
9. Private helper refactor -> `DOCS_NOT_REQUIRED`.
10. UI-only specialist cannot change API/business logic.
11. High-risk migration specialization does not downgrade security/profile rigor.
12. Multiple areas do not automatically increase agent-turn budget.
13. Execution-only remote operator returns evidence and does not choose follow-up actions.
14. Recovery revalidates stale topology/interface/runtime data before reuse.

## Current checkpoint

Implementation starts on this branch. P1-P7 must be wired into controller/planning/task/state contracts before this plan can move to `IMPLEMENTED`. Native proof remains part of the wider 0.5 release gate.
