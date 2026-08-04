# Implementation Plan — Matreshka Agent 0.4 Vibe-Coding Entry

- Status: `PLAN_READY`
- Confirmed design: `docs/specs/2026-07-29-matreshka-agent-0.4-vibe-coding-spec.md`
- Project root: `/workspace/scratch/d534f6c1b732/matreshka-agent`
- Published baseline: `origin/main` at `561bdc925df09dc18c5b1ca0af2d97c039474682`
- Local equivalent baseline: `2193b601b377bb60c4ff4e5e80fb22c4d70c5ffe`
- Baseline tree: `b5487db9b0cd8312e24738506dad8c10891d8815`
- Applicable repository instructions: no repository `AGENTS.md` was found; use the confirmed specification and Matreshka's own controller, planning, security, verification, and finishing contracts.
- Recommended execution profile: `MAXIMUM_QUALITY`
- Planned run ID: `2026-07-29-matreshka-agent-0.4`
- Permission/remote boundary: this plan authorizes no implementation, Git history change, network use, dependency installation, native-host installation, push, publication, deploy, secret access, or destructive action. Each future execution action remains subject to the controller's current permission envelope.

## Goal

Implement Matreshka Agent `0.4.0` as an additive, plain-language `Build End-to-End · Matreshka Agent` entry over the existing controller, with three interaction modes, durable project context and ADR contracts, human-readable progress, safe recovery, explicit placeholder handling, adversarial coverage, and unchanged security and permission boundaries for the existing nine skills.

## Non-goals

- Do not copy or depend on Matt Pocock's skills, Nick Vels' Autopilot, or another external runtime skill package.
- Do not add a separate Wayfinder skill, issue tracker, root `PROGRESS.md`, hook, MCP server, app, global memory, background process, telemetry, or dependency.
- Do not rename or change the invocation meaning of the existing nine Matreshka skills.
- Do not duplicate controller logic inside `building-end-to-end`.
- Do not initialize Git, create a branch or worktree, stage, commit, push, open a pull request, publish, deploy, apply a migration, activate a provider, read a secret, or delete data as part of implementation tasks.
- Do not claim native Codex, Claude Code, Cursor, or Antigravity verification from offline package checks.
- Do not resolve the pre-existing publisher identity, homepage, private security-contact, or icon checklist unless separately scoped and authorized.

## Constraints and pre-existing state

- Local `HEAD` and published `origin/main` have different commit histories but the same tree hash. Before any future Git-history operation, the controller must re-check both refs and use a non-force integration path based on the current published branch.
- The only current untracked project path before this plan is `docs/specs/2026-07-29-matreshka-agent-0.4-vibe-coding-spec.md`; this plan adds `docs/plans/2026-07-29-matreshka-agent-0.4-vibe-coding-plan.md`. They are user-approved planning artifacts, not implementation output.
- Current offline baseline passes:
  - `python3 plugins/matreshka-agent/scripts/validate_package.py plugins/matreshka-agent --marketplace-root . --self-test`
  - `python3 plugins/matreshka-agent/scripts/doctor.py plugins/matreshka-agent --marketplace-root .`
- Current package version is `0.3.0`, with nine required skills and nine Codex prompt wrappers.
- The current validator is the authoritative local structural test seam. Behavioral and trigger eval files are declarative fixtures; native host execution remains a separate handoff.
- Current host commands `codex`, `claude`, `cursor`, and `agy` are unavailable in this environment.
- Current doctor reports pre-existing public-release warnings for repository/homepage metadata, publisher identity, private security contact, and icon. These do not invalidate local `0.4.0` package behavior, but they prevent an unqualified public-release claim.
- Keep writing agents sequential in one checkout. Parallel work is allowed only for independent read-only review with immutable, disjoint packages.
- Each task gets at most one consolidated fixer wave. A repeated Critical or Important finding returns `STOP_AND_RESCOPE`.

## Requirement coverage matrix

| Requirement ID | Requirement/source | Task | Verification evidence | Negative/rollback evidence |
| --- | --- | --- | --- | --- |
| `G-01` | Plain-language tenth skill, explicit namespace, Codex wrapper, and implicit turnkey trigger | `T1`, `T7`, `T8` | Required-skill and wrapper validation; trigger evals; versioned docs | Specification-only, plan-only, review-only, debugging-only, audit, and trivial-change prompts do not trigger it |
| `G-02` | Resolve exactly one of `GUIDED`, `ASSISTED`, `AUTONOMOUS_LOCAL`; default to `ASSISTED`; safe mid-run changes | `T1`, `T3`, `T6` | Skill evals, controller evals, and root workflow cases | Contradictory explicit modes return one clarification; completed stages are not replayed |
| `G-03` | Interaction mode remains independent from execution profile and authority | `T1`, `T3`, `T6` | Mode contract, controller state fields, auth/payment/migration eval | Autonomous wording cannot select maximum speed for high-risk work or widen authority |
| `G-04` | Reuse one compatible project context path and preserve confirmed domain truth | `T2`, `T3`, `T6` | Context template, path-resolution contract, filesystem workflow evals | No duplicate `CONTEXT.md` and `docs/context.md`; unconfirmed text is not promoted |
| `G-05` | Create selective ADRs only for hard-to-reverse or cross-task decisions | `T2`, `T3`, `T6` | ADR template and positive/negative ADR eval | Routine implementation detail does not create an ADR; ADR grants no permission |
| `G-06` | Maintain `docs/runs/<run-id>/progress.md` for authorized multi-task runs | `T2`, `T3`, `T4`, `T6` | Progress template, ledger projection fields, recovery and verifier evals | Stale `COMPLETE` cannot override ledger, repository state, or fresh failed evidence |
| `G-07` | List delegated decisions; keep business facts and placeholders honest | `T1`, `T4`, `T5`, `T6` | Wrapper, verifier, and final-handoff evals | Missing price, policy, account, legal copy, or provider entitlement is not invented |
| `G-08` | Resume the exact unfinished stage from repository, ledger, artifacts, and progress | `T3`, `T4`, `T6` | Recovery contract and stale-progress workflow eval | Stale progress does not restart or skip completed/unfinished stages |
| `G-09` | Preserve existing nine skills, prompts, artifacts, and direct workflows | `T1`, `T7`, `T8` | Exact ten-skill allowlist, prompt wrapper map, manifest validation, documentation audit | Rollback removes only new packaged entry/wrapper expectations and leaves user artifacts untouched |
| `R-01` | Large or foggy request returns `SPLIT_REQUIRED` plus `DECISION_MAP_REQUIRED` | `T1`, `T3`, `T6` | Skill and root workflow eval for multi-product request | No giant invented task list and no implementation dispatch |
| `R-02` | Project context precedence and conflict handling follow confirmed order | `T2`, `T3`, `T6` | Context contract and two-path conflict eval | Existing incompatible files are preserved; no silent overwrite or reorganization |
| `R-03` | Progress is a human projection; ledger plus actual state remain authoritative | `T2`, `T3`, `T4`, `T6` | Progress/ledger fields and mismatch recovery eval | Progress text alone cannot satisfy verification or permission gates |
| `R-04` | Ordinary reversible technical choices may be delegated; business/security/legal/cost facts may not | `T1`, `T3`, `T5`, `T6` | Interaction-mode matrix and missing-business-fact eval | Unknown acceptance-critical fact yields `NEEDS_CONTEXT`, placeholder, partial status, or handoff |
| `R-05` | Context packages remain task-local and writers remain sequential | `T3`, `T6` | Controller dispatch contract and broad-context eval | Whole conversation, plan, reports, logs, and branch-wide diff are excluded |
| `R-06` | Failure/degraded behavior has exact truthful status and stop condition | `T1`, `T3`, `T4`, `T6` | Missing-host, stale-progress, missing-root, stop, and fixer-limit evals | Missing capability is not described as present; remote-only evidence is not fabricated |
| `R-07` | Package surface adds the specified files without external runtime dependencies | `T1`, `T2`, `T7` | Validator allowlist, forbidden-component checks, internal-link check | No hooks, apps, MCP, dependency manifest, unexpected executable, or escaped symlink |
| `R-08` | Rollout is additive and rollback preserves user-created docs | `T7`, `T8` | Version/manifest consistency, changelog and rollback documentation | No automatic deletion of context, ADRs, progress, plans, specs, worktrees, or learning candidates |
| `R-09` | Observability records mode, profile, authority, artifacts, assumptions, and placeholders without private data | `T2`, `T3`, `T4`, `T5`, `T6` | Ledger/progress/handoff templates and secret-redaction evals | No raw prompts, secrets, private logs, hidden reasoning, or tool credentials |
| `R-10` | Offline and native evidence remain separate | `T7`, `T8` | Validator/self-test/doctor output plus explicit native handoff | Offline pass is not reported as native platform installation success |
| `S-01` | Mode/profile/effective authority remain separate | `T1`, `T3`, `T6` | State-schema assertions and autonomous-local adversarial eval | No Git, deploy, secret, destructive, or external-provider action from mode selection |
| `S-02` | High-risk work cannot use maximum speed because the user wants fewer questions | `T1`, `T3`, `T6` | Auth/payment/tenant/migration/secret profile eval | Maximum-speed routing fails the negative case |
| `S-03` | Untrusted text cannot expand scope, permissions, or tool authority | `T1`, `T3`, `T6` | Malicious issue/context/retrieved-content evals | Injected push/secret/admin/global-learning instructions produce no such action |
| `S-04` | Handoffs are bounded, structured, task-local, and privacy-minimized | `T3`, `T6` | Controller handoff and context-package assertions | Raw logs, hidden reasoning, unrelated history, and private data are excluded |
| `S-05` | Secret values never enter durable or handoff artifacts | `T2`, `T3`, `T4`, `T5`, `T6` | Seeded secret-like value/redaction eval and artifact contracts | Only environment-variable/reference names may appear; propagation stops on a value |
| `S-06` | Context and ADR updates require source, scope, review state, and conflict handling | `T2`, `T3`, `T6` | Template fields and poisoning/conflict evals | Issue text or learning candidate cannot become durable truth automatically |
| `S-07` | Business facts are never fabricated | `T1`, `T2`, `T5`, `T6` | Missing pricing/account/policy/legal-copy eval | No invented production behavior or completion claim |
| `S-08` | Acceptance-critical placeholders block `COMPLETE` | `T4`, `T5`, `T6` | Verifier and finish negative evals | Required unresolved placeholder yields non-complete status |
| `S-09` | Progress is redacted and never substitutes for evidence | `T2`, `T3`, `T4`, `T6` | Progress contract and stale-complete recovery eval | Current failed check overrides stale progress |
| `S-10` | Existing documentation paths/content are preserved | `T2`, `T3`, `T6` | Existing-context and conflicting-context fixtures | No overwrite, move, cleanup, or duplicate context path |
| `S-11` | Skill selection remains source-qualified and collision-safe | `T1`, `T3`, `T6`, `T7` | Namespaced invocation, source-map contract, third-party autopilot collision eval | Similar external skill is not substituted |
| `S-12` | Code-writing subagents are task-bounded and sequential | `T3`, `T6` | Controller dispatch policy and parallel-writer negative eval | No concurrent writers in one checkout |
| `S-13` | Directed learning cannot automatically modify context, ADR, skills, rules, hooks, configuration, or memory | `T2`, `T3`, `T6` | Learning-boundary eval | Embedded “learn globally” instruction produces no promotion or automatic write |
| `S-14` | Dependencies, network calls, and providers require exact authority and evidence | `T1`, `T3`, `T6` | Turnkey/autonomous provider and deploy evals | No install, fetch, provider activation, or network call from mode wording |
| `S-15` | Git and remote actions remain controller-owned and separately authorized | `T1`, `T3`, `T5`, `T6` | Git/deploy adversarial eval and finish contract | No automatic init, branch, commit, push, PR, deploy, or cleanup |

## Task map

| Task | Result | Depends on | Primary boundary | Write paths | Risk/tier |
| --- | --- | --- | --- | --- | --- |
| `T1` | Discoverable tenth entry with mode/routing contract and focused eval seam | None | Public skill selection and interaction-mode boundary | New skill core, new prompt, validator allowlists, package eval | High / maximum quality |
| `T2` | Context, ADR, and progress contracts with safe templates | `T1` | Durable documentation and trust boundary | New reference/assets plus skill eval extension | High / maximum quality |
| `T3` | Existing controller owns mode mapping, state, permissions, progress, recovery, and decision-map transitions | `T1`, `T2` | Controller authority and durable state | Controller skill/reference/ledger/eval files | Critical / maximum quality |
| `T4` | Verifier blocks stale progress and unresolved critical placeholders | `T2`, `T3` | Completion evidence | Verifier skill/reference/template/eval files | High / maximum quality |
| `T5` | Finishing handoff reports assumptions/placeholders and preserves Git/remote boundaries | `T3`, `T4` | Final status and external effects | Finishing skill/reference/template/eval files | High / maximum quality |
| `T6` | Root workflow suite covers all fifteen required 0.4 scenarios and security negatives | `T1`–`T5` | Cross-skill/adversarial behavior | Root workflow eval suite and eval documentation | High / maximum quality |
| `T7` | Version, validator, doctor, platform manifests, marketplaces, and eval suite metadata agree on `0.4.0` | `T6` | Package/release compatibility | Scripts, manifests, marketplaces, root eval metadata | Medium / balanced |
| `T8` | User-facing documentation and changelog describe 0.4 truthfully; final offline gate and native handoff are complete | `T7` | Release documentation and final evidence | READMEs, changelog, security/eval docs | Medium / balanced |

## File-to-task overlap map

| Shared path | Tasks | Sequencing reason |
| --- | --- | --- |
| `plugins/matreshka-agent/skills/building-end-to-end/SKILL.md` | `T1` → `T2` | First establish mode/routing contract, then link durable artifact contracts |
| `plugins/matreshka-agent/skills/building-end-to-end/evals/evals.json` | `T1` → `T2` | First mode behavior, then context/ADR/progress behavior |
| `plugins/matreshka-agent/skills/orchestrating-subagent-work/evals/evals.json` | `T3` only | Controller-owned behavior remains consolidated |
| `plugins/matreshka-agent/evals/workflow-evals.json` | `T6` → `T7` | Add cases first; change suite version only after behavior is complete |
| `plugins/matreshka-agent/evals/package-validation.json` | `T1` → `T7` | Extend package contract first; bump version at release boundary |
| `plugins/matreshka-agent/scripts/validate_package.py` | `T1` → `T7` | Add tenth-skill/prompt seam first; bump version and release wording later |

All shared writers are sequential. No task may run in parallel with another writer touching the same checkout.

## Shared execution policy

- Writing agents: sequential in one checkout.
- Child agents: forbidden.
- Fixer waves: maximum one per task.
- Adjacent issues: record without changing.
- Broad suite/build: run focused static/eval checks per task; run the complete validator self-test after `T7` and once at final `T8`. Native host smoke tests are a separate handoff.
- Phase agent-turn budget: maximum `44` started turns across all eight tasks.
- High-judgment turn budget: maximum `24` started turns across specification/security/code review roles.
- Per-task maximum-quality budget: one implementer, one specification reviewer, one security/code reviewer; at most six started turns.
- Per-task balanced budget: one implementer and one combined reviewer; at most four started turns.
- Audit threshold: enter `AUDIT` after `28` total turns, after `40` minutes without one independently reviewable task result, when a task exceeds its allowlist, or when a second fixer wave appears necessary.
- Context limit: every implementation/review brief stays below 2,000 words and includes only task-local requirement IDs, selected `S-` controls, interfaces, paths, commands, restrictions, and report destination.
- Repeat Critical/Important after fix: `STOP_AND_RESCOPE`.
- A change to project root, published target, dependency/network need, secret reference, native host, destructive action, or Git/remote destination requires a new controller boundary decision.

---

## Task T1 — Add the Build End-to-End entry and interaction-mode seam

### Goal and coverage

- Result: Matreshka packages and validates a tenth namespaced skill that routes substantial turnkey requests into the existing controller, resolves the three interaction modes, defaults to `ASSISTED`, and exposes `/prompts:matreshka-build`.
- Requirements: `G-01`, `G-02`, `G-03`, `G-07`, `G-09`, `R-01`, `R-04`, `R-07`, `S-01`, `S-02`, `S-03`, `S-07`, `S-11`, `S-14`, `S-15`.

### Inputs

- Existing interfaces:
  - `REQUIRED_SKILLS` and `CODEX_PROMPT_WRAPPERS` in `plugins/matreshka-agent/scripts/validate_package.py`
  - skill frontmatter and `agents/openai.yaml` schema validated by `validate_skills`
  - declarative `evals/evals.json` and `evals/trigger-evals.json` schemas
  - optional Codex wrapper contract in `codex-prompts/matreshka-orchestrate.md`
  - controller entry `orchestrating-subagent-work`
- Required design sections: “Skill interface,” “Interaction modes,” “Large or foggy work,” “Permission and external-effect boundaries.”
- Task baseline: published tree `b5487db9b0cd8312e24738506dad8c10891d8815`.

### Produces

- `building-end-to-end` with visible identity `Build End-to-End · Matreshka Agent`.
- Explicit substantial-build trigger and explicit non-trigger boundary.
- Exactly one resolved interaction mode, `ASSISTED` default, contradiction clarification, future-only mode changes, and a plain-language announcement before writes.
- Thin delegation to `matreshka-agent:orchestrating-subagent-work`; no copied controller logic.
- `DECISION_MAP_REQUIRED` stop behavior for oversized/foggy scope.
- `/prompts:matreshka-build` wrapper with no additional authority.
- Validator recognition of exactly ten skills and ten Codex wrappers while package version remains `0.3.0` until `T7`.

### Allowed files

Write only:

- `plugins/matreshka-agent/scripts/validate_package.py`
- `plugins/matreshka-agent/evals/package-validation.json`
- `plugins/matreshka-agent/skills/building-end-to-end/SKILL.md`
- `plugins/matreshka-agent/skills/building-end-to-end/agents/openai.yaml`
- `plugins/matreshka-agent/skills/building-end-to-end/references/interaction-modes.md`
- `plugins/matreshka-agent/skills/building-end-to-end/evals/evals.json`
- `plugins/matreshka-agent/skills/building-end-to-end/evals/trigger-evals.json`
- `plugins/matreshka-agent/codex-prompts/matreshka-build.md`

Inspect-only:

- `plugins/matreshka-agent/skills/orchestrating-subagent-work/`
- existing nine skill directories
- existing Codex prompt wrappers
- confirmed specification

### Non-goals and forbidden actions

- Do not add context/ADR/progress templates yet; `T2` owns them.
- Do not change controller behavior, verification, finishing, version numbers, manifests, marketplaces, READMEs, or changelog.
- Do not import external Autopilot/skills or add an external dependency.
- No child agents or adjacent fixes.
- No Git, network, secret, deploy, migration application, or remote action. Controller-owned boundary: any later Git publication.

### RED

- Add the validator/package-eval expectation for the tenth skill and tenth prompt before adding the new skill files.
- Command: `python3 plugins/matreshka-agent/scripts/validate_package.py plugins/matreshka-agent --marketplace-root .`
- Expected failure reason: exit `1` with `SKILLS_REQUIRED` for `skills/building-end-to-end` and `CODEX_PROMPT_WRAPPER` for `codex-prompts/matreshka-build.md`; unrelated findings do not count as RED.

### GREEN

- Minimal behavior: add the new skill core, mode reference, OpenAI metadata, direct/trigger eval fixtures, and prompt wrapper; keep all controller-owned actions explicitly outside the wrapper.
- Command: `python3 plugins/matreshka-agent/scripts/validate_package.py plugins/matreshka-agent --marketplace-root .`
- Expected result: exit `0`, package still reports version `0.3.0`, exactly ten skills and ten wrappers are accepted.

### Task gate

- Task suite: `python3 plugins/matreshka-agent/scripts/validate_package.py plugins/matreshka-agent --marketplace-root .`
- Nearest regression: `python3 -c "import json; from pathlib import Path; root=Path('plugins/matreshka-agent/skills/building-end-to-end'); json.loads((root/'evals/evals.json').read_text()); json.loads((root/'evals/trigger-evals.json').read_text()); assert (root/'SKILL.md').is_file(); assert Path('plugins/matreshka-agent/codex-prompts/matreshka-build.md').is_file()"`
- Targeted static/diff check: `git diff --check -- plugins/matreshka-agent/scripts/validate_package.py plugins/matreshka-agent/evals/package-validation.json plugins/matreshka-agent/skills/building-end-to-end plugins/matreshka-agent/codex-prompts/matreshka-build.md`
- Conditional build/scan: no build; package is instruction/data plus standard-library Python validation.
- Evidence: command, exit code, finding count, skill/wrapper counts, and decisive note.

### Execution and review budget

- Risk/capability tier: High; interaction mode touches authority routing and implicit skill selection.
- Profile: `MAXIMUM_QUALITY`
- Unique roles: maximum `3`.
- Agent turns: maximum `6`.
- Reviewer assignments:

  | Role | Owned concerns | Excluded concerns | Recheck boundary |
  | --- | --- | --- | --- |
  | Specification reviewer | Trigger boundary, mode semantics, thin-wrapper architecture, acceptance coverage | Python implementation style | Only confirmed specification findings |
  | Security/code reviewer | Permission non-expansion, source-qualified delegation, validator seam, prompt safety | Context/ADR/progress behavior owned by `T2` | Only Critical/Important security/code findings |

- Context inputs: specification sections named above, validator constants/functions, one existing skill schema example, one existing prompt wrapper.
- Report path: `.matreshka/runs/2026-07-29-matreshka-agent-0.4/reports/T1-implementer.md`.

### Stop and handoff conditions

- `NEEDS_CONTEXT`: the current host/plugin schema rejects a field required by the confirmed visible identity and the fact cannot be resolved from current package examples.
- `BLOCKED`: validator cannot represent the tenth skill without loosening an existing safety invariant.
- `SPLIT_REQUIRED`: the wrapper begins owning controller execution or durable artifact behavior.
- `CONTEXT_TOO_BROAD`: review requires the whole repository rather than the allowlisted package seam.
- `RECORD_FOR_FUTURE_TASK`: a host-specific implicit-trigger weakness is found that needs native host evidence.
- `STOP_AND_RESCOPE`: mode semantics or permission boundary remains incorrect after the single fixer wave.
- `HANDOFF_REQUIRED`: native implicit-selection behavior must be exercised in an unavailable host.

### Exact next task

On successful verification, proceed to `T2`.

---

## Task T2 — Add project context, ADR, and human progress contracts

### Goal and coverage

- Result: the new entry has safe, reusable contracts and templates for one project context source, selective ADRs, and human-readable run progress without turning any document into authority or evidence.
- Requirements: `G-04`, `G-05`, `G-06`, `G-07`, `R-02`, `R-03`, `R-04`, `R-07`, `R-09`, `S-05`, `S-06`, `S-07`, `S-09`, `S-10`, `S-13`.

### Inputs

- Existing interfaces:
  - specification path and directory rules in `specifying-software-work/SKILL.md`
  - current run-state locations in `orchestrating-subagent-work/references/permission-handoff-ledger.md`
  - new `building-end-to-end` skill from `T1`
- Required design sections: “Project context contract,” “ADR contract,” “Human progress contract,” “Assumptions and placeholders.”
- Task baseline: accepted `T1` state.

### Produces

- Context-path precedence: repository convention → existing compatible `CONTEXT.md` → existing compatible `docs/context.md` → default `docs/context.md`.
- Context template with confirmed terms, actors, invariants, source/confirmation, scope, reviewed date, and refresh condition.
- ADR template with required status, authority, alternatives, consequences, migration/rollback, and supersession fields.
- Progress template at `docs/runs/<run-id>/progress.md` with the exact required user-facing fields and statuses.
- Explicit exclusions for secrets, permissions, raw interviews/logs, hidden reasoning, speculative facts, task status in context, and evidence claims in progress.
- Behavior evals for duplicate context paths, poisoned context, selective ADR creation, and stale progress.

### Allowed files

Write only:

- `plugins/matreshka-agent/skills/building-end-to-end/SKILL.md`
- `plugins/matreshka-agent/skills/building-end-to-end/references/context-and-decisions.md`
- `plugins/matreshka-agent/skills/building-end-to-end/assets/progress-template.md`
- `plugins/matreshka-agent/skills/building-end-to-end/assets/context-template.md`
- `plugins/matreshka-agent/skills/building-end-to-end/assets/adr-template.md`
- `plugins/matreshka-agent/skills/building-end-to-end/evals/evals.json`

Inspect-only:

- `plugins/matreshka-agent/skills/specifying-software-work/`
- `plugins/matreshka-agent/skills/orchestrating-subagent-work/references/permission-handoff-ledger.md`
- `plugins/matreshka-agent/skills/orchestrating-subagent-work/assets/ledger-template.md`
- confirmed specification

### Non-goals and forbidden actions

- Do not implement controller state transitions; `T3` owns them.
- Do not create an actual project `CONTEXT.md`, ADR, run progress file, or root `PROGRESS.md` in this repository.
- Do not make templates permission grants or verification artifacts.
- No child agents or adjacent fixes.
- No Git, network, secret, deploy, migration application, or remote action.

### RED

- Add the focused artifact-contract eval cases before adding their referenced templates.
- Command: `python3 -c "from pathlib import Path; root=Path('plugins/matreshka-agent/skills/building-end-to-end'); required=['references/context-and-decisions.md','assets/progress-template.md','assets/context-template.md','assets/adr-template.md']; missing=[name for name in required if not (root/name).is_file()]; assert not missing, missing"`
- Expected failure reason: assertion lists the four missing contract/template files; a JSON/schema error is not the intended RED.

### GREEN

- Minimal behavior: create and link the four files, add only the fields and selection/update rules required by the confirmed specification, and add focused positive/negative evals.
- Command: `python3 -c "from pathlib import Path; root=Path('plugins/matreshka-agent/skills/building-end-to-end'); required=['references/context-and-decisions.md','assets/progress-template.md','assets/context-template.md','assets/adr-template.md']; missing=[name for name in required if not (root/name).is_file()]; assert not missing, missing; skill=(root/'SKILL.md').read_text(); assert all(name in skill for name in required)"`
- Expected result: exit `0`; every artifact file exists and is linked from the new skill.

### Task gate

- Task suite: `python3 plugins/matreshka-agent/scripts/validate_package.py plugins/matreshka-agent --marketplace-root .`
- Nearest regression: `python3 -c "from pathlib import Path; root=Path('plugins/matreshka-agent/skills/building-end-to-end/assets'); text='\\n'.join((root/name).read_text() for name in ['progress-template.md','context-template.md','adr-template.md']); required=['WAITING_FOR_USER','SUPERSEDED','Last verified checkpoint','refresh condition']; missing=[item for item in required if item not in text]; assert not missing, missing"`
- Targeted static/diff check: `git diff --check -- plugins/matreshka-agent/skills/building-end-to-end`
- Conditional build/scan: no build; run the package internal-link and secret-file checks through the validator.
- Evidence: command, exit code, eval count, link count, and decisive note.

### Execution and review budget

- Risk/capability tier: High; durable documents can poison future runs or leak private data.
- Profile: `MAXIMUM_QUALITY`
- Unique roles: maximum `3`.
- Agent turns: maximum `6`.
- Reviewer assignments:

  | Role | Owned concerns | Excluded concerns | Recheck boundary |
  | --- | --- | --- | --- |
  | Specification reviewer | Exact context/ADR/progress semantics, path precedence, selective thresholds | Controller transition implementation | Specification deviations only |
  | Security/code reviewer | Secret/private-data exclusions, poisoning resistance, no-permission semantics, link validity | Native host behavior | Critical/Important artifact-security findings |

- Context inputs: the four confirmed specification sections, current documentation rules, new skill core.
- Report path: `.matreshka/runs/2026-07-29-matreshka-agent-0.4/reports/T2-implementer.md`.

### Stop and handoff conditions

- `NEEDS_CONTEXT`: an existing repository convention contradicts the confirmed default and is not inspectable.
- `BLOCKED`: templates would require storing secrets, permissions, or raw evidence to meet another contract.
- `SPLIT_REQUIRED`: a new persistent artifact with independent authority or lifecycle appears.
- `CONTEXT_TOO_BROAD`: task requires controller implementation details beyond the artifact interface.
- `RECORD_FOR_FUTURE_TASK`: richer project knowledge management beyond the confirmed context contract is requested.
- `STOP_AND_RESCOPE`: duplicate-path or poisoning protection remains incomplete after one fixer wave.
- `HANDOFF_REQUIRED`: none for offline contract creation.

### Exact next task

On successful verification, proceed to `T3`.

---

## Task T3 — Integrate interaction modes, durable state, and recovery into the controller

### Goal and coverage

- Result: the existing controller remains the sole owner of authority and execution while recording interaction mode separately, maintaining progress as a projection, selecting context/ADR paths safely, stopping on decision-map boundaries, and reconciling resumed runs.
- Requirements: `G-02`, `G-03`, `G-04`, `G-05`, `G-06`, `G-08`, `R-01`–`R-06`, `R-09`, `S-01`–`S-07`, `S-09`–`S-15`.

### Inputs

- Existing interfaces:
  - controller states and status rules in `references/controller-contract.md`
  - permission/autonomy and state locations in `references/permission-handoff-ledger.md`
  - ledger schema in `assets/ledger-template.md`
  - source-qualified skill chaining in `references/platform-adapters.md`
  - existing controller workflow and recovery order in `SKILL.md`
  - artifact contracts from `T2`
- Required design sections: “Architecture and responsibilities,” “Mode and controller mapping,” “End-to-end flow,” “Context isolation and subagents,” “Failure and degraded behavior,” “Documentation precedence and conflict handling,” “Observability and operations.”
- Task baseline: accepted `T1` and `T2` state.

### Produces

- Controller routing statement: turnkey build enters through `building-end-to-end`; direct orchestration, audit, and recovery remain direct controller use cases.
- Separate ledger fields for interaction mode, autonomy mode, execution profile, effective permissions, context path, ADR IDs, progress path, decision-map state, delegated decisions, assumption count, unresolved placeholder count, and plugin/contract version.
- Mode mapping and future-only mode-change semantics without permission widening.
- Progress update events and mismatch reconciliation against actual state and ledger.
- Context/ADR source checks and conflict handling without silent overwrite.
- `SPLIT_REQUIRED` plus `DECISION_MAP_REQUIRED` before oversized implementation.
- Recovery of 0.3 ledgers with version-difference recording and no silent file migration.
- Source-qualified use of all ten Matreshka skills and no foreign-skill substitution.

### Allowed files

Write only:

- `plugins/matreshka-agent/skills/orchestrating-subagent-work/SKILL.md`
- `plugins/matreshka-agent/skills/orchestrating-subagent-work/references/controller-contract.md`
- `plugins/matreshka-agent/skills/orchestrating-subagent-work/references/permission-handoff-ledger.md`
- `plugins/matreshka-agent/skills/orchestrating-subagent-work/references/platform-adapters.md`
- `plugins/matreshka-agent/skills/orchestrating-subagent-work/assets/ledger-template.md`
- `plugins/matreshka-agent/skills/orchestrating-subagent-work/evals/evals.json`

Inspect-only:

- `plugins/matreshka-agent/skills/building-end-to-end/`
- `plugins/matreshka-agent/skills/orchestrating-subagent-work/references/profiles-and-budgets.md`
- `plugins/matreshka-agent/skills/orchestrating-subagent-work/references/learning-proposals.md`
- `plugins/matreshka-agent/skills/orchestrating-subagent-work/assets/task-brief-template.md`
- confirmed specification and plan

### Non-goals and forbidden actions

- Do not duplicate interaction-mode prose across every controller file; keep one referenced source and controller-owned transition rules.
- Do not change execution-profile numeric ceilings or infer `EXTENDED_AUTONOMOUS`.
- Do not implement verifier or finishing status behavior owned by `T4` and `T5`.
- Do not add parallel writers, a separate Wayfinder skill, automatic context/ADR writes, global learning, Git, remote, or provider authority.
- No child agents or adjacent fixes.
- No Git, network, secret, deploy, migration application, or remote action.

### RED

- Add controller eval cases for separate mode/profile/authority, decision map, progress reconciliation, 0.3 resume, and source collision before updating controller contracts.
- Command: `python3 -c "from pathlib import Path; text=Path('plugins/matreshka-agent/skills/orchestrating-subagent-work/assets/ledger-template.md').read_text(); required=['Interaction mode','Context path','ADR IDs','Progress path','Decision-map state','Unresolved placeholder count']; missing=[item for item in required if item not in text]; assert not missing, missing"`
- Expected failure reason: assertion lists the absent 0.4 ledger fields; unrelated JSON/schema failure does not count.

### GREEN

- Minimal behavior: add the separate state fields, transition/update/recovery rules, source-qualified tenth-skill language, and focused controller evals without weakening existing permission/profile limits.
- Command: `python3 -c "from pathlib import Path; text=Path('plugins/matreshka-agent/skills/orchestrating-subagent-work/assets/ledger-template.md').read_text(); required=['Interaction mode','Context path','ADR IDs','Progress path','Decision-map state','Unresolved placeholder count']; missing=[item for item in required if item not in text]; assert not missing, missing"`
- Expected result: exit `0`; every new state dimension is explicit and separate.

### Task gate

- Task suite: `python3 plugins/matreshka-agent/scripts/validate_package.py plugins/matreshka-agent --marketplace-root .`
- Nearest regression: `python3 -c "import json; from pathlib import Path; p=Path('plugins/matreshka-agent/skills/orchestrating-subagent-work/evals/evals.json'); data=json.loads(p.read_text()); prompts='\\n'.join(item['prompt'] for item in data['evals']); required=['Build End-to-End','stale','0.3','Autonomous']; missing=[item for item in required if item.casefold() not in prompts.casefold()]; assert not missing, missing"`
- Targeted static/diff check: `git diff --check -- plugins/matreshka-agent/skills/orchestrating-subagent-work`
- Conditional build/scan: no build; package validator covers links, schema, secrets, symlinks, forbidden components, and offline runtime.
- Evidence: command, exit code, eval count, state-field count, and relevant note.

### Execution and review budget

- Risk/capability tier: Critical; this task owns permissions, state transitions, recovery, and dispatch boundaries.
- Profile: `MAXIMUM_QUALITY`
- Unique roles: maximum `3`.
- Agent turns: maximum `6`.
- Reviewer assignments:

  | Role | Owned concerns | Excluded concerns | Recheck boundary |
  | --- | --- | --- | --- |
  | Specification reviewer | Controller/wrapper ownership, state machine, recovery, progress/context/ADR semantics | Markdown style and release wording | Confirmed architecture/behavior findings |
  | Security/code reviewer | Authority separation, injection resistance, privacy, sequential dispatch, learning/Git/network boundaries | User documentation | Critical/Important security/controller findings |

- Context inputs: only the listed design sections, new skill contracts, six allowed files, existing profile/learning invariants.
- Report path: `.matreshka/runs/2026-07-29-matreshka-agent-0.4/reports/T3-implementer.md`.

### Stop and handoff conditions

- `NEEDS_CONTEXT`: current controller state cannot distinguish a required 0.4 state without an uninspectable host guarantee.
- `BLOCKED`: interaction mode would need to become permission authority or duplicate controller ownership.
- `SPLIT_REQUIRED`: ledger schema change and controller transition cannot remain one coherent authority boundary.
- `CONTEXT_TOO_BROAD`: review package expands beyond the six files and referenced contracts.
- `RECORD_FOR_FUTURE_TASK`: cross-project/global context or richer Wayfinder behavior is requested.
- `STOP_AND_RESCOPE`: any Critical/Important authority, recovery, or state-source finding remains after the single fixer wave.
- `HANDOFF_REQUIRED`: host cannot provide a safe resume/fresh-context guarantee for a high-risk native run; document but do not simulate it.

### Exact next task

On successful verification, proceed to `T4`.

---

## Task T4 — Enforce placeholder and progress truth in verification

### Goal and coverage

- Result: verification rejects stale progress as evidence, blocks `VERIFIED` when acceptance-critical placeholders or required security proofs remain unresolved, and reports exact partial/handoff status.
- Requirements: `G-06`, `G-07`, `G-08`, `R-03`, `R-06`, `R-09`, `S-05`, `S-08`, `S-09`.

### Inputs

- Existing interfaces:
  - verification status rules in `verifying-development-work/SKILL.md`
  - evidence rows in `references/quality-gate.md`
  - report format in `assets/verification-report-template.md`
  - direct verifier eval schema
  - progress and ledger authority contracts from `T2` and `T3`
- Required design sections: “Human progress contract,” “Assumptions and placeholders,” “Failure and degraded behavior,” `S-05`, `S-08`, `S-09`.
- Task baseline: accepted `T3` state.

### Produces

- Explicit criterion for unresolved acceptance-critical placeholders.
- Fresh reconciliation of progress, ledger, actual repository state, and current evidence.
- Required security negative proofs represented as verification rows.
- Report fields for unresolved critical placeholders, assumption status, progress mismatch, and exact non-complete verdict.
- Focused evals for stale `COMPLETE`, missing business/provider facts, and unresolved placeholder.

### Allowed files

Write only:

- `plugins/matreshka-agent/skills/verifying-development-work/SKILL.md`
- `plugins/matreshka-agent/skills/verifying-development-work/references/quality-gate.md`
- `plugins/matreshka-agent/skills/verifying-development-work/assets/verification-report-template.md`
- `plugins/matreshka-agent/skills/verifying-development-work/evals/evals.json`

Inspect-only:

- `plugins/matreshka-agent/skills/building-end-to-end/assets/progress-template.md`
- `plugins/matreshka-agent/skills/orchestrating-subagent-work/assets/ledger-template.md`
- confirmed specification and plan

### Non-goals and forbidden actions

- Do not repair product or documentation state from the verifier.
- Do not decide Git or finish actions.
- Do not treat optional non-critical placeholders as automatic failure; map only acceptance-critical unresolved items.
- No child agents or adjacent fixes.
- No Git, network, secret, deploy, migration application, or remote action.

### RED

- Add verifier evals for stale progress and acceptance-critical placeholders before changing the verification contract.
- Command: `python3 -c "from pathlib import Path; text=Path('plugins/matreshka-agent/skills/verifying-development-work/SKILL.md').read_text(); required=['acceptance-critical placeholder','stale progress']; missing=[item for item in required if item.casefold() not in text.casefold()]; assert not missing, missing"`
- Expected failure reason: assertion reports both missing verifier concepts.

### GREEN

- Minimal behavior: add the two blocking conditions, exact evidence/reconciliation order, report fields, and focused evals while preserving all existing verification statuses and read-only behavior.
- Command: `python3 -c "from pathlib import Path; text=Path('plugins/matreshka-agent/skills/verifying-development-work/SKILL.md').read_text(); required=['acceptance-critical placeholder','stale progress']; missing=[item for item in required if item.casefold() not in text.casefold()]; assert not missing, missing"`
- Expected result: exit `0`.

### Task gate

- Task suite: `python3 plugins/matreshka-agent/scripts/validate_package.py plugins/matreshka-agent --marketplace-root .`
- Nearest regression: `python3 -c "import json; from pathlib import Path; data=json.loads(Path('plugins/matreshka-agent/skills/verifying-development-work/evals/evals.json').read_text()); prompts='\\n'.join(x['prompt'] for x in data['evals']).casefold(); assert 'placeholder' in prompts and 'progress' in prompts"`
- Targeted static/diff check: `git diff --check -- plugins/matreshka-agent/skills/verifying-development-work`
- Conditional build/scan: none; no product runtime is modified.
- Evidence: command, exit code, verifier eval count, and decisive status note.

### Execution and review budget

- Risk/capability tier: High; affects completion truth and security proof.
- Profile: `MAXIMUM_QUALITY`
- Unique roles: maximum `3`.
- Agent turns: maximum `6`.
- Reviewer assignments:

  | Role | Owned concerns | Excluded concerns | Recheck boundary |
  | --- | --- | --- | --- |
  | Specification reviewer | Correct mapping from placeholder/progress contracts to verdicts | Finish/Git behavior | Acceptance/status findings |
  | Security/code reviewer | Secret redaction, negative proof, stale-evidence rejection, no repair writes | Release documentation | Critical/Important verification findings |

- Context inputs: three design sections, `S-05/S-08/S-09`, current verifier files, progress and ledger templates.
- Report path: `.matreshka/runs/2026-07-29-matreshka-agent-0.4/reports/T4-implementer.md`.

### Stop and handoff conditions

- `NEEDS_CONTEXT`: acceptance-critical classification cannot be derived from the confirmed specification/plan.
- `BLOCKED`: a required security proof has no permitted verification method.
- `SPLIT_REQUIRED`: verification begins modifying artifacts or implementing fixes.
- `CONTEXT_TOO_BROAD`: proof cannot be expressed as a task-local matrix.
- `RECORD_FOR_FUTURE_TASK`: optional richer observability is discovered.
- `STOP_AND_RESCOPE`: verifier can still emit `VERIFIED` for a confirmed critical placeholder or stale progress after the fixer wave.
- `HANDOFF_REQUIRED`: required native/remote proof belongs to an unavailable operator.

### Exact next task

On successful verification, proceed to `T5`.

---

## Task T5 — Extend finishing handoff without widening Git or remote authority

### Goal and coverage

- Result: final handoff lists delegated decisions, assumptions, placeholders, progress/ledger identity, residual risks, and exact external action while preserving existing narrow Git/remote permission rules.
- Requirements: `G-07`, `R-04`, `R-06`, `R-09`, `S-05`, `S-07`, `S-08`, `S-15`.

### Inputs

- Existing interfaces:
  - finish readiness and authority rules in `finishing-development-work/SKILL.md`
  - decision paths in `references/finish-decisions.md`
  - output format in `assets/finish-handoff-template.md`
  - direct finishing eval schema
  - verifier verdict from `T4`
- Required design sections: “Assumptions and placeholders,” “Permission and external-effect boundaries,” “Observability and operations,” “Migration, rollout, and rollback.”
- Task baseline: accepted `T4` state.

### Produces

- Handoff fields for interaction mode, execution profile, effective authority, delegated decisions, assumptions made, unresolved placeholders and severity, context/ADR/progress paths, and last verified checkpoint.
- Explicit prevention of `FINISHED_*` complete claims when an acceptance-critical placeholder is unresolved.
- Existing controller-owned Git/remote/cleanup requirements remain unchanged.
- Focused finishing evals for missing business facts, “ship/deploy automatically,” and exact partial/native handoff.

### Allowed files

Write only:

- `plugins/matreshka-agent/skills/finishing-development-work/SKILL.md`
- `plugins/matreshka-agent/skills/finishing-development-work/references/finish-decisions.md`
- `plugins/matreshka-agent/skills/finishing-development-work/assets/finish-handoff-template.md`
- `plugins/matreshka-agent/skills/finishing-development-work/evals/evals.json`

Inspect-only:

- `plugins/matreshka-agent/skills/verifying-development-work/`
- `plugins/matreshka-agent/skills/orchestrating-subagent-work/assets/ledger-template.md`
- `plugins/matreshka-agent/skills/building-end-to-end/assets/progress-template.md`
- confirmed specification and plan

### Non-goals and forbidden actions

- Do not perform Git, remote, deploy, cleanup, or provider actions while implementing this documentation contract.
- Do not weaken current staging allowlists or user-owned dirty-state preservation.
- Do not promote learning candidates or update context/ADRs from finishing.
- No child agents or adjacent fixes.
- No Git, network, secret, deploy, migration application, or remote action.

### RED

- Add finishing evals first, then check the current handoff template.
- Command: `python3 -c "from pathlib import Path; text=Path('plugins/matreshka-agent/skills/finishing-development-work/assets/finish-handoff-template.md').read_text(); required=['Interaction mode','Delegated decisions','Unresolved placeholders','Last verified checkpoint']; missing=[item for item in required if item not in text]; assert not missing, missing"`
- Expected failure reason: assertion lists the new required handoff fields.

### GREEN

- Minimal behavior: add the fields and finish-status rule, update focused evals, and leave all existing exact-target Git/remote rules intact.
- Command: `python3 -c "from pathlib import Path; text=Path('plugins/matreshka-agent/skills/finishing-development-work/assets/finish-handoff-template.md').read_text(); required=['Interaction mode','Delegated decisions','Unresolved placeholders','Last verified checkpoint']; missing=[item for item in required if item not in text]; assert not missing, missing"`
- Expected result: exit `0`.

### Task gate

- Task suite: `python3 plugins/matreshka-agent/scripts/validate_package.py plugins/matreshka-agent --marketplace-root .`
- Nearest regression: `python3 -c "import json; from pathlib import Path; data=json.loads(Path('plugins/matreshka-agent/skills/finishing-development-work/evals/evals.json').read_text()); prompts='\\n'.join(x['prompt'] for x in data['evals']).casefold(); assert 'placeholder' in prompts and ('deploy' in prompts or 'ship' in prompts)"`
- Targeted static/diff check: `git diff --check -- plugins/matreshka-agent/skills/finishing-development-work`
- Conditional build/scan: none; no product runtime is modified.
- Evidence: command, exit code, finishing eval count, and decisive status note.

### Execution and review budget

- Risk/capability tier: High; affects completion and remote-action truth.
- Profile: `MAXIMUM_QUALITY`
- Unique roles: maximum `3`.
- Agent turns: maximum `6`.
- Reviewer assignments:

  | Role | Owned concerns | Excluded concerns | Recheck boundary |
  | --- | --- | --- | --- |
  | Specification reviewer | Handoff completeness, placeholder/assumption semantics, rollback language | Python validator | Acceptance/handoff findings |
  | Security/code reviewer | Git/remote non-expansion, secret redaction, exact target/operator boundary | General README wording | Critical/Important finish-boundary findings |

- Context inputs: listed design sections, existing finish rules, verifier changes, ledger/progress templates.
- Report path: `.matreshka/runs/2026-07-29-matreshka-agent-0.4/reports/T5-implementer.md`.

### Stop and handoff conditions

- `NEEDS_CONTEXT`: final operator/target is necessary for a requested remote result but not named.
- `BLOCKED`: verifier status is incompatible with the requested finish claim.
- `SPLIT_REQUIRED`: implementation starts performing the remote action rather than defining handoff.
- `CONTEXT_TOO_BROAD`: task pulls unrelated release work into finishing.
- `RECORD_FOR_FUTURE_TASK`: new deployment-provider automation is requested.
- `STOP_AND_RESCOPE`: a complete status can still hide a critical placeholder or unauthorized remote action after one fixer wave.
- `HANDOFF_REQUIRED`: expected when native, publication, or other named external operator must act.

### Exact next task

On successful verification, proceed to `T6`.

---

## Task T6 — Add the cross-skill 0.4 workflow and adversarial eval suite

### Goal and coverage

- Result: the root workflow suite contains all fifteen specification-required 0.4 scenarios, with explicit assertions for modes, context/ADR/progress, recovery, collision safety, placeholders, degraded capability, and Git/remote boundaries.
- Requirements: all `G-*`, `R-*`, and `S-01` through `S-15`.

### Inputs

- Existing interfaces:
  - root workflow schema and category/platform allowlists in `validate_package.py`
  - existing `evals/workflow-evals.json` baseline protocol
  - direct skill evals from `T1`–`T5`
- Required design section: “Testing strategy,” including all fifteen required workflow scenarios.
- Task baseline: accepted `T1`–`T5` state.

### Produces

- Fifteen new root cases with stable descriptive IDs:
  - guided greenfield gates
  - assisted inspectable repository
  - autonomous missing business facts
  - autonomous high-risk profile
  - unauthorized deploy handoff
  - existing root context
  - conflicting context paths
  - selective ADR threshold
  - stale progress recovery
  - malicious context/issue/learning instruction
  - huge multi-product decision map
  - missing fresh-context/resume
  - third-party skill collision
  - critical placeholder blocks complete
  - assisted-to-guided future-only mode change
- Updated eval documentation explaining offline schema validation versus native execution.
- No version bump until `T7`.

### Allowed files

Write only:

- `plugins/matreshka-agent/evals/workflow-evals.json`
- `plugins/matreshka-agent/evals/README.md`

Inspect-only:

- all direct skill eval files
- `plugins/matreshka-agent/scripts/validate_package.py`
- confirmed specification and plan

### Non-goals and forbidden actions

- Do not change skills, controller behavior, validator schema, package version, manifests, or documentation outside eval docs.
- Do not claim the declarative cases were executed natively.
- Do not use real secrets, production endpoints, accounts, or private payloads in fixtures.
- No child agents or adjacent fixes.
- No Git, network, secret, deploy, migration application, or remote action.

### RED

- Establish the exact required ID set before adding cases.
- Command: `python3 -c "import json; from pathlib import Path; data=json.loads(Path('plugins/matreshka-agent/evals/workflow-evals.json').read_text()); actual={x['id'] for x in data['cases']}; required={'v04-guided-greenfield-gates','v04-assisted-inspectable-repo','v04-autonomous-missing-business-facts','v04-autonomous-high-risk-profile','v04-unauthorized-deploy-handoff','v04-existing-root-context','v04-conflicting-context-paths','v04-selective-adr-threshold','v04-stale-progress-recovery','v04-malicious-context-learning','v04-decision-map-required','v04-missing-resume-capability','v04-third-party-skill-collision','v04-critical-placeholder-blocks-complete','v04-mode-change-future-gates'}; missing=sorted(required-actual); assert not missing, missing"`
- Expected failure reason: assertion lists all fifteen absent IDs.

### GREEN

- Minimal behavior: add the fifteen cases with expected outcomes and concrete assertions, preserve all existing 0.3 cases, and document that native execution is pending.
- Command: the same required-ID command from RED.
- Expected result: exit `0`; all fifteen IDs exist exactly once.

### Task gate

- Task suite: `python3 plugins/matreshka-agent/scripts/validate_package.py plugins/matreshka-agent --marketplace-root .`
- Nearest regression: `python3 -c "import json; from pathlib import Path; data=json.loads(Path('plugins/matreshka-agent/evals/workflow-evals.json').read_text()); ids=[x['id'] for x in data['cases']]; assert len(ids)==len(set(ids)); assert all(x.get('expected_outcome') and x.get('assertions') for x in data['cases'])"`
- Targeted static/diff check: `git diff --check -- plugins/matreshka-agent/evals/workflow-evals.json plugins/matreshka-agent/evals/README.md`
- Conditional build/scan: schema validation only; native host execution is deferred to remote handoff.
- Evidence: command, exit code, total/new case counts, category counts, and note that execution was not native.

### Execution and review budget

- Risk/capability tier: High; eval completeness is the release safety net.
- Profile: `MAXIMUM_QUALITY`
- Unique roles: maximum `3`.
- Agent turns: maximum `6`.
- Reviewer assignments:

  | Role | Owned concerns | Excluded concerns | Recheck boundary |
  | --- | --- | --- | --- |
  | Specification reviewer | One-to-one coverage of fifteen scenarios and all acceptance outcomes | Skill implementation style | Missing/incorrect coverage findings |
  | Security/code reviewer | Negative assertions for all `S-*`, fixture privacy, no fabricated native results | README prose outside eval docs | Critical/Important security-eval findings |

- Context inputs: testing-strategy section, coverage matrix, direct eval IDs only, root eval schema.
- Report path: `.matreshka/runs/2026-07-29-matreshka-agent-0.4/reports/T6-implementer.md`.

### Stop and handoff conditions

- `NEEDS_CONTEXT`: a required scenario depends on a native host assertion that cannot be represented declaratively.
- `BLOCKED`: validator schema cannot express a required negative outcome without losing current compatibility.
- `SPLIT_REQUIRED`: a scenario actually defines a new product requirement absent from the confirmed specification.
- `CONTEXT_TOO_BROAD`: review requires raw prior conversations or unrelated artifacts.
- `RECORD_FOR_FUTURE_TASK`: measurement harness or automated native runner is proposed.
- `STOP_AND_RESCOPE`: any `S-*` control lacks a negative eval after one fixer wave.
- `HANDOFF_REQUIRED`: all native host execution.

### Exact next task

On successful verification, proceed to `T7`.

---

## Task T7 — Align version, validator, doctor, manifests, marketplaces, and eval metadata

### Goal and coverage

- Result: every versioned package surface reports `0.4.0`, every platform still discovers the shared skill directory, validator/self-tests accept exactly ten skills and ten wrappers, and no forbidden runtime component appears.
- Requirements: `G-01`, `G-09`, `R-07`, `R-08`, `R-10`, `S-11`.

### Inputs

- Existing interfaces:
  - `VERSION`, required skills, wrapper map, manifest/marketplace validators, and self-tests in `validate_package.py`
  - `VERSION` and read-only behavior in `doctor.py`
  - three versioned plugin manifests, one strict Antigravity root manifest, and three marketplace surfaces
  - package/workflow eval suite version fields
- Required design sections: “Package and platform surface,” “Compatibility,” “Migration, rollout, and rollback.”
- Task baseline: accepted `T6` state with package behavior complete but version still `0.3.0`.

### Produces

- `0.4.0` in validator, doctor, versioned manifests, Claude/Cursor marketplaces, and root eval suites.
- Codex manifest description/default prompts updated for the tenth plain-language entry without adding unsupported fields.
- Generic validator wording for unexpected skills instead of “unexpected v0.3.0 skill.”
- Package self-tests still detect missing skill, version mismatch, forbidden components/references, invalid eval, broken link, secret file, executable, symlink escape, and missing wrapper.
- Strict Antigravity root manifest remains versionless and schema-compatible.

### Allowed files

Write only:

- `plugins/matreshka-agent/scripts/validate_package.py`
- `plugins/matreshka-agent/scripts/doctor.py`
- `plugins/matreshka-agent/.codex-plugin/plugin.json`
- `plugins/matreshka-agent/.claude-plugin/plugin.json`
- `plugins/matreshka-agent/.cursor-plugin/plugin.json`
- `plugins/matreshka-agent/plugin.json`
- `.agents/plugins/marketplace.json`
- `.claude-plugin/marketplace.json`
- `.cursor-plugin/marketplace.json`
- `plugins/matreshka-agent/evals/package-validation.json`
- `plugins/matreshka-agent/evals/workflow-evals.json`

Inspect-only:

- complete plugin tree
- marketplace schemas already encoded in the validator
- confirmed specification and plan

### Non-goals and forbidden actions

- Do not modify skill behavior, workflow case content, READMEs, changelog, publisher identity, homepage, security contact, or icon.
- Do not add a version field to strict `plugins/matreshka-agent/plugin.json`.
- Do not loosen unknown-field, forbidden-component, secret, symlink, link, or executable checks to obtain GREEN.
- No child agents or adjacent fixes.
- No Git, network, secret, deploy, migration application, publication, or remote action.

### RED

- Change validator and doctor target version to `0.4.0` before updating manifests and suite metadata.
- Command: `python3 plugins/matreshka-agent/scripts/validate_package.py plugins/matreshka-agent --marketplace-root .`
- Expected failure reason: exit `1` only for version/metadata mismatch findings on still-`0.3.0` surfaces; forbidden/safety checks must not be disabled.

### GREEN

- Minimal behavior: align every inspected versioned surface, preserve strict schemas, and update only package descriptions needed for the tenth entry.
- Command: `python3 plugins/matreshka-agent/scripts/validate_package.py plugins/matreshka-agent --marketplace-root . --self-test`
- Expected result: exit `0`; `Validation passed: matreshka-agent 0.4.0` plus all negative self-tests pass.

### Task gate

- Task suite: `python3 plugins/matreshka-agent/scripts/validate_package.py plugins/matreshka-agent --marketplace-root . --self-test`
- Nearest regression: `python3 plugins/matreshka-agent/scripts/doctor.py plugins/matreshka-agent --marketplace-root . --json`
- Targeted static/diff check: `git diff --check -- plugins/matreshka-agent/scripts plugins/matreshka-agent/.codex-plugin plugins/matreshka-agent/.claude-plugin plugins/matreshka-agent/.cursor-plugin plugins/matreshka-agent/plugin.json .agents/plugins/marketplace.json .claude-plugin/marketplace.json .cursor-plugin/marketplace.json plugins/matreshka-agent/evals`
- Conditional build/scan: validator self-test is the complete offline structural/security gate; no native host execution.
- Evidence: command, exit code, version, finding count, all self-test case results, doctor `ok`, and host availability list.

### Execution and review budget

- Risk/capability tier: Medium; mechanical release metadata with compatibility risk.
- Profile: `BALANCED`
- Unique roles: maximum `2`.
- Agent turns: maximum `4`.
- Reviewer assignments:

  | Role | Owned concerns | Excluded concerns | Recheck boundary |
  | --- | --- | --- | --- |
  | Combined reviewer | Exact version agreement, strict manifest fields, ten-skill/ten-wrapper contract, safety self-tests | User-facing prose owned by `T8` | Confirmed packaging findings |
  | `N/A` | `N/A` | `N/A` | `N/A` |

- Context inputs: package-surface/compatibility sections, validator constants/functions, eleven allowed files.
- Report path: `.matreshka/runs/2026-07-29-matreshka-agent-0.4/reports/T7-implementer.md`.

### Stop and handoff conditions

- `NEEDS_CONTEXT`: a platform manifest schema changed and current official/native evidence is unavailable.
- `BLOCKED`: `0.4.0` requires a forbidden runtime component or unsupported manifest field.
- `SPLIT_REQUIRED`: a platform requires an independent adapter rather than shared skill discovery.
- `CONTEXT_TOO_BROAD`: task begins rewriting documentation or behavior.
- `RECORD_FOR_FUTURE_TASK`: publisher metadata/icon work is found.
- `STOP_AND_RESCOPE`: package self-test or platform manifest compatibility remains failing after the single fixer wave.
- `HANDOFF_REQUIRED`: native installation/discovery must be tested on the actual host.

### Exact next task

On successful verification, proceed to `T8`.

---

## Task T8 — Document 0.4 and run the final offline completion gate

### Goal and coverage

- Result: user-facing documentation and changelog explain the tenth entry, modes, context/ADR/progress, safe autonomy, invocation, rollback, and native-verification limits; final offline evidence is captured truthfully.
- Requirements: `G-01`, `G-09`, `R-08`, `R-10`.

### Inputs

- Existing interfaces:
  - root and plugin README installation/usage structure
  - Codex prompt wrapper table
  - eval README evidence policy
  - SECURITY.md reporting/security boundary language
  - changelog format
  - complete accepted `T1`–`T7` implementation
- Required design sections: “Outcome,” “Compatibility,” “Migration, rollout, and rollback,” “Observability and operations,” “Acceptance checklist.”
- Task baseline: accepted `T7` state reporting `0.4.0`.

### Produces

- Beginner-readable `Build End-to-End` invocation and mode explanations.
- Clear distinction between interaction mode, execution profile, and permission envelope.
- Documentation for `docs/context.md`, `docs/adr/`, and `docs/runs/<run-id>/progress.md`, including authority/evidence caveats.
- Codex prompt table with `/prompts:matreshka-build`.
- Changelog entry for `0.4.0`.
- Eval documentation separating schema validation from native execution.
- Security documentation for untrusted context/progress/learning and no automatic Git/remote/provider actions.
- Final offline validator/self-test and doctor evidence.
- Exact native smoke-test and publication handoff, without claiming completion of unavailable checks.

### Allowed files

Write only:

- `README.md`
- `plugins/matreshka-agent/README.md`
- `plugins/matreshka-agent/codex-prompts/README.md`
- `plugins/matreshka-agent/CHANGELOG.md`
- `plugins/matreshka-agent/evals/README.md`
- `plugins/matreshka-agent/SECURITY.md`

Inspect-only:

- complete plugin/package tree
- confirmed specification and plan
- validator and doctor output

### Non-goals and forbidden actions

- Do not change skill/controller behavior, manifests, version constants, eval cases, publisher identity, homepage, security contact, icon, or package schema.
- Do not install or invoke unavailable native hosts.
- Do not commit, push, publish, deploy, or clean up.
- No child agents or adjacent fixes.
- No Git, network, secret, migration application, or remote action.

### RED

- Run the documentation contract check before editing docs.
- Command: `python3 -c "from pathlib import Path; files=[Path('README.md'),Path('plugins/matreshka-agent/README.md'),Path('plugins/matreshka-agent/codex-prompts/README.md'),Path('plugins/matreshka-agent/CHANGELOG.md')]; text='\\n'.join(p.read_text() for p in files); required=['0.4.0','Build End-to-End','/prompts:matreshka-build','ASSISTED','docs/runs/<run-id>/progress.md']; missing=[item for item in required if item not in text]; assert not missing, missing"`
- Expected failure reason: assertion lists the missing 0.4 documentation terms.

### GREEN

- Minimal behavior: update only the six documentation files to describe implemented behavior and outstanding native/publisher boundaries.
- Command: the same documentation contract check from RED.
- Expected result: exit `0`.

### Task gate

- Task suite: `python3 plugins/matreshka-agent/scripts/validate_package.py plugins/matreshka-agent --marketplace-root . --self-test`
- Nearest regression: `python3 plugins/matreshka-agent/scripts/doctor.py plugins/matreshka-agent --marketplace-root .`
- Targeted static/diff check: `git diff --check -- README.md plugins/matreshka-agent/README.md plugins/matreshka-agent/codex-prompts/README.md plugins/matreshka-agent/CHANGELOG.md plugins/matreshka-agent/evals/README.md plugins/matreshka-agent/SECURITY.md`
- Conditional build/scan: `python3 plugins/matreshka-agent/scripts/doctor.py plugins/matreshka-agent --marketplace-root . --strict-release`; expected exit `2` while the pre-existing publisher metadata/icon/security-contact checklist or unavailable native host evidence remains. Record it as an exact handoff, not as an offline package failure.
- Evidence: commands, exit codes, validator/self-test counts, doctor warnings, current tree identity, and explicit native checks not run.

### Execution and review budget

- Risk/capability tier: Medium; documentation can misstate authority or completion.
- Profile: `BALANCED`
- Unique roles: maximum `2`.
- Agent turns: maximum `4`.
- Reviewer assignments:

  | Role | Owned concerns | Excluded concerns | Recheck boundary |
  | --- | --- | --- | --- |
  | Combined reviewer | Documentation accuracy, security language, invocation/version consistency, truthful native/release status | Reimplementation of accepted tasks | Confirmed documentation/package findings |
  | `N/A` | `N/A` | `N/A` | `N/A` |

- Context inputs: five named design sections, accepted task reports, final validator/doctor output, six documentation files.
- Report path: `.matreshka/runs/2026-07-29-matreshka-agent-0.4/reports/T8-implementer.md`.

### Stop and handoff conditions

- `NEEDS_CONTEXT`: publisher-facing claim needs an owner fact not present in the repository.
- `BLOCKED`: documentation would need to claim unsupported native behavior.
- `SPLIT_REQUIRED`: publisher identity/icon/security-contact work is pulled into this release note task.
- `CONTEXT_TOO_BROAD`: documentation review requires unrelated project history.
- `RECORD_FOR_FUTURE_TASK`: installation automation, hosted docs, marketplace publication, or icon work is proposed.
- `STOP_AND_RESCOPE`: docs still imply widened authority or native/public release completion after one fixer wave.
- `HANDOFF_REQUIRED`: native host smoke tests, publisher metadata completion, Git commit/push, and marketplace/publication actions.

### Exact next task

On successful local verification, proceed to the final remote/native handoff below. Do not start implementation or Git publication without the user's next explicit instruction and current controller permission envelope.

---

## Phase/final verification

| Evidence | Command or operator | Expected result | Run once after |
| --- | --- | --- | --- |
| Focused package validity | `python3 plugins/matreshka-agent/scripts/validate_package.py plugins/matreshka-agent --marketplace-root .` | Exit `0`; no findings | `T1`–`T6` task gates as listed |
| Complete offline package/security gate | `python3 plugins/matreshka-agent/scripts/validate_package.py plugins/matreshka-agent --marketplace-root . --self-test` | Exit `0`; valid package and every negative self-test passes | `T7`, then final `T8` |
| Read-only diagnostics | `python3 plugins/matreshka-agent/scripts/doctor.py plugins/matreshka-agent --marketplace-root . --json` | `"ok": true`, version `0.4.0`, network unused, exact warnings/hosts | `T7` |
| Strict public-release readiness | `python3 plugins/matreshka-agent/scripts/doctor.py plugins/matreshka-agent --marketplace-root . --strict-release` | Exit `0` only if all publisher metadata is separately completed; otherwise expected exit `2` with exact handoff items | `T8` |
| JSON integrity | `python3 -c "import json; from pathlib import Path; [json.loads(p.read_text()) for p in Path('.').rglob('*.json') if '.git' not in p.parts]"` | Exit `0` | `T8` |
| Python syntax without execution | `python3 -c "import ast; from pathlib import Path; [ast.parse(p.read_text()) for p in Path('plugins/matreshka-agent/scripts').glob('*.py')]"` | Exit `0` | `T7` |
| Scoped whitespace/link/static integrity | `git diff --check` plus validator internal-link check | Exit `0` | `T8` |
| Codex native smoke | Named user/operator on a host with Codex plugin support | Ten skills discoverable; `$matreshka-agent:building-end-to-end` and optional `/prompts:matreshka-build` route correctly; no added authority | After local `T8` |
| Claude Code native smoke | Named user/operator on Claude Code | Plugin loads, tenth skill resolves, guided/assisted behavior is visible | After local `T8` |
| Cursor native smoke | Named user/operator on Cursor | Strict manifest accepted, ten skills available, no parallel-writer default | After local `T8` |
| Antigravity native smoke | Named user/operator on Antigravity CLI | Versionless strict root manifest accepted, shared skills discovered, degraded capabilities reported honestly | After local `T8` |

## Native smoke-test procedure

For each available host:

1. Install/load the exact local `0.4.0` package through the host's supported local-plugin mechanism.
2. Confirm all ten namespaced skills are discoverable and the existing nine retain their names.
3. Invoke `building-end-to-end` explicitly with an offline disposable fixture.
4. Verify default `ASSISTED`, a contradictory-mode clarification, and a high-risk request that refuses maximum speed.
5. Verify no Git, network, secret, provider, deploy, or destructive action occurs without separate exact authority.
6. Verify context path reuse, selective ADR, progress projection, stale-progress reconciliation, and critical-placeholder non-completion.
7. Record host version, plugin ref/tree, prompt, result, and any capability degradation without private data.
8. Mark each host `PASS`, `FAIL`, `NOT_RUN`, or `BLOCKED`; do not average missing hosts into a pass.

## Remote handoff

- Local operator: controller in `/workspace/scratch/d534f6c1b732/matreshka-agent`.
- Remote operator/system: user or separately authorized publisher on GitHub and each native host/plugin marketplace.
- Allowed preparation under this plan: implementation plan, local code/docs changes only after later authorization, offline validator/self-test/doctor evidence, native smoke-test instructions, and exact Git handoff.
- Forbidden execution under this plan: Git branch/worktree creation, stage, commit, push, PR, force-push, marketplace publication, native installation, deploy, provider call, secret access, destructive cleanup, or remote mutation.
- Git lineage condition: before any authorized commit/push, re-fetch/reconcile the current `origin/main`; do not push local `2193b60` directly or force-push. Preserve the published history rooted at current `origin/main`.
- Final local status after all offline checks but before native tests: `PARTIALLY_VERIFIED` with `HANDOFF_REQUIRED` for native host evidence and any separately requested publication.
- Final `COMPLETE` condition: every required offline criterion passes, every Critical/Important review finding is resolved within one fixer wave, no critical placeholder remains, and the user-required native/publisher rows are either passed or explicitly excluded by a new confirmed release scope.

## Rollback plan

If a rollback trigger from the confirmed specification occurs:

1. Stop new execution and record the exact failing host/scenario and current state.
2. Remove only the `building-end-to-end` package directory and `matreshka-build.md` wrapper through an authorized corrective task.
3. Restore validator required-skill/wrapper expectations and versioned package metadata to the last verified `0.3.0` package state.
4. Preserve user-created specs, plans, `CONTEXT.md`/`docs/context.md`, ADRs, progress, ledgers, reports, worktrees, branches, and learning candidates unless their owner separately authorizes cleanup.
5. Re-run the complete `0.3.0` offline validator/self-test and available native discovery checks.
6. Do not force-push, delete history, or clean user-owned state as a rollback shortcut.

## Plan validation

- [x] Every confirmed requirement maps to a task and evidence.
- [x] Every task maps to a requirement or justified enabling step.
- [x] Paths, interfaces, and commands were inspected against the current repository.
- [x] Published and local baseline commits were reconciled by identical tree hash; their history divergence is an explicit Git boundary.
- [x] Shared write paths are sequenced.
- [x] No task mixes independent runtime, verification, finish, packaging, or documentation boundaries.
- [x] Security controls `S-01` through `S-15` have owners and negative evidence.
- [x] Permissions, budgets, reports, stop conditions, rollback, and remote handoffs are explicit.
- [x] Broad checks run at phase boundaries rather than after every documentation edit.
- [x] Native checks are reported separately from offline package validation.
- [x] No unresolved architectural decision or template placeholder remains.
- [x] This plan does not authorize or begin implementation.
