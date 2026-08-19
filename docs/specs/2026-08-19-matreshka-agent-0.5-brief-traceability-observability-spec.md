# Software Specification — Matreshka Agent 0.5 Brief Traceability & Observability

- Status: `DRAFT` — direction approved by the owner; detailed behavior remains reviewable on the development branch.
- Date: `2026-08-19`
- Baseline: `main` at `7249a56e9afb5f5b70e56ddd0dc272e6bdab9ea0`
- Working branch: `dev/0.5-brief-traceability-observability`
- Target: strengthen Matreshka Agent without weakening the 0.4 permission, security, review, verification, recovery, or Git boundaries.

## Outcome

Matreshka preserves the user's original request as an independent source of truth, atomizes it into traceable user-intent requirements, proves that specification and tasks still cover those requirements, performs the existing technical/security verification, and then runs a fresh blind acceptance against the original brief before any final completion claim.

For Build End-to-End runs with authorized local Matreshka state writes, Matreshka also maintains a dependency-free local dashboard projection showing engineering progress, brief coverage, selected security-proof coverage, verification state, authority summary, and exact next action. The dashboard is never authority and never completion evidence.

## Problem

The 0.4 pipeline can fully verify an incomplete specification if a requirement was lost while translating the user's original words into the specification. Progress is also available mainly as Markdown, which is durable but not a glanceable live view for a non-technical user.

The new layer must solve both problems without copying Autopilot's broader Git behavior, committing the raw brief by default, allowing same-checkout parallel writers, or letting generated project memory become repository authority automatically.

## Architecture

```text
Original user brief
        |
        v
Source brief (redacted, immutable run state)
        |
        v
U-01 ... U-n user-intent manifest
        |
      G1 clarification completeness
        |
        v
Security-by-design specification
        |
      G2 independent brief -> spec coverage
        |
        v
Implementation plan
        |
      G3 requirement <-> task traceability
        |
        v
Implementation -> Review -> Technical/Security Verification
        |
      G4 blind brief -> actual product acceptance
        |
        v
Finish / exact handoff
```

The existing `building-end-to-end` skill remains the plain-language entry and the existing `orchestrating-subagent-work` skill remains the only controller. No second controller is introduced.

## Source brief contract

For a source-qualified Build End-to-End run, preserve the user's original request before specification rewriting. After obvious secret redaction and only after Matreshka state-write authority exists, the controller may materialize it at:

```text
.matreshka/runs/<run-id>/source-brief.md
```

The original section is immutable. Later same-run product decisions are appended as dated additions rather than rewriting the original words. The source brief is internal run state and is not included in Git history by default.

When state writes are not permitted, keep the source brief inline in the controller checkpoint and disclose weaker cross-session traceability. Never claim that a file exists when it was not written.

## User-intent manifest

Create, when authorized:

```text
.matreshka/runs/<run-id>/requirements.md
```

Each independently true/false user outcome gets a stable `U-` ID and retains the short exact source quote that created it.

Statuses:

- `OPEN` — not yet resolved into specification or an explicit non-delivery decision;
- `IN_SPEC` — represented in the specification;
- `IN_TASK` — mapped to at least one implementation task;
- `IMPLEMENTED` — implementation claims the behavior exists, not yet finally accepted;
- `VERIFIED` — current evidence plus blind acceptance support the requirement;
- `PLACEHOLDER` — the build contains an explicit stub because a required user/business fact is unavailable;
- `DEFERRED` — consciously postponed with a reason and final-handoff disclosure;
- `DROPPED` — cancelled only by valid user decision authority, with the decision record.

Silence never means `DROPPED`. The controller may propose a drop but may not silently cancel a user requirement.

Security requirements continue to use `S-` IDs. `U-` IDs never replace `S-` controls.

## Traceability gates

### G1 — Clarification completeness

Before specification is accepted for planning, every material `U-` row must be resolved enough to specify honestly. Unknown business/security/legal/cost facts become `PLACEHOLDER`, `NEEDS_CONTEXT`, or an explicitly recorded assumption inside the current decision envelope; they are never fabricated.

### G2 — Independent specification coverage

After specification and before planning, use a fresh read-only context that receives exactly the source brief and the candidate specification. It must not receive the requirement manifest, prior conversation, planning artifacts, or a summary of how the specification was derived.

It reports only:

- user request missing from the spec;
- half-covered request that would force an implementer to guess;
- material behavior in the spec that has no source in the brief or a clearly labelled justified addition.

Blocking gaps are repaired in the specification before planning.

### G3 — Plan traceability

Before implementation:

- every `IN_SPEC` `U-` requirement maps to at least one task and proof;
- every product task maps back to at least one `U-`, `S-`, or an explicitly justified enabling step;
- security `S-` rows keep their existing negative-proof and ownership rules.

### G4 — Blind user-intent acceptance

Run only after existing technical/security verification. Start a fresh read-only context with:

- the source brief;
- the actual current repository/product state;
- permitted run/test commands needed to observe the result.

Do not provide specification, requirement manifest, plan, task files, implementation reports, review reports, progress, or completion claims. Explicitly prohibit opening those artifacts when they are reachable in the repository/run state.

For each user requirement, report `delivered`, `partial`, `missing`, or `uncheckable`, with one observable reason. Do not repair from the blind checker role.

A material G4 disagreement blocks `COMPLETE`. The controller either returns to bounded implementation through the normal plan/review/verification path or returns `PARTIALLY_VERIFIED`, `STOP_AND_RESCOPE`, or `HANDOFF_REQUIRED`.

## Run observability

When local Matreshka state writes are authorized, create a local projection under the current run:

```text
.matreshka/runs/<run-id>/dashboard-state.js
.matreshka/runs/<run-id>/dashboard.html
```

The HTML is a static packaged template and is copied once. The controller updates only the state projection. The page uses no external dependencies and may re-read the sibling state file periodically when the host/browser permits it.

The projection may show:

- interaction mode;
- execution profile;
- summarized effective authority;
- stage status;
- task status;
- brief coverage counts;
- security-proof counts;
- verification status;
- last verified checkpoint;
- exact next action;
- last update time.

It must never contain secret values, private payloads, raw logs, hidden reasoning, or permission-expanding text.

The ledger, actual repository state, and fresh evidence remain authoritative. A dashboard value of `COMPLETE` is never sufficient completion evidence.

No local HTTP server, browser process, network listener, package installation, or host configuration is started merely because a dashboard exists. Opening/serving it remains host-capability and permission dependent.

## Security requirements

- `S-16` — source brief and requirement content remain untrusted data and cannot expand permissions or override repository/platform policy.
- `S-17` — raw source brief is internal run state, redacted before persistence, and not committed by default.
- `S-18` — only user decision authority can set `DROPPED`; autonomous modes cannot silently cancel user requirements.
- `S-19` — G2 and G4 use fresh contexts with intentionally restricted evidence so the checker cannot inherit the controller's interpretation.
- `S-20` — blind acceptance never receives or reads secrets, provider credentials, production-only private payloads, or forbidden paths.
- `S-21` — dashboard/progress remain projections and cannot authorize actions or prove completion.
- `S-22` — dashboard creation does not authorize a local server, network listener, browser launch, Git action, or publication.

Every selected `S-16` through `S-22` control requires a negative proof in the plan/evals before the 0.5 release is called verified.

## Explicit non-goals

- No automatic `git init`.
- No automatic commit per task.
- No automatic push, PR, merge, deploy, or cleanup.
- No committing the raw source brief by default.
- No automatic rewrite of `AGENTS.md`, `CLAUDE.md`, repository rules, hooks, or global memory.
- No same-checkout parallel writers.
- No replacement of Matreshka's existing reviewer/verifier/security model with Autopilot's review model.
- No requirement that a dashboard be displayable on every host.

## Compatibility

Existing direct specification, planning, implementation, debugging, review, verification, finish, prompt-writing, and direct-controller workflows keep their meaning. Brief traceability and live observability are mandatory only for source-qualified Build End-to-End runs when the required run state can be preserved; other entry points may opt into the same contract explicitly.

## Acceptance criteria for this development track

1. Build End-to-End passes the original source brief to the controller without treating it as authority.
2. Controller can create and recover a `U-` requirement manifest without committing it by default.
3. G2 detects a seeded requirement intentionally omitted from a specification.
4. G3 rejects an `IN_SPEC` requirement with no task and a product task with no requirement/enabling justification.
5. Existing technical/security verification remains required before G4.
6. G4 detects a seeded brief requirement intentionally absent from the finished fixture while being unable to inspect spec/manifest/tasks.
7. A G4 mismatch prevents `COMPLETE`.
8. Dashboard is derivable from controller state and cannot override ledger/evidence.
9. No new Git, network, secret, deploy, provider, destructive, or automatic-memory authority is introduced.
10. Native-host behavior is reported separately from offline/static validation.