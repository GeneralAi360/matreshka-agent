# Onboarding and session lifecycle change review

Date: 2026-10-21. Repository: https://github.com/GeneralAi360/matreshka-agent

Base: `974b7cf1cbbed5dfe8f1280b1c4756b6c3388498`.
Working copy: `D:\МПИК ТЕст\tooling\matreshka-agent`.
Status: local source changes implemented; native host acceptance and release pending.
At this validation checkpoint, no commit, push, plugin installation, host settings change or dependency installation had been performed. Subsequent source publication does not constitute plugin installation or release acceptance. Versioned manifests remain unchanged at 0.4.0, consistent with the development track.

## Problem and result

Previously, a goal-bearing invocation could skip the menu, the dashboard was optional, and no common bootstrap/Feedback/session lifecycle contract existed. The new [project lifecycle contract](../../plugins/matreshka-agent/skills/building-end-to-end/references/project-lifecycle.md) makes those outcomes explicit and connects the entry skill, controller, design and finishing routes.

| User requirement | Implementation |
| --- | --- |
| Immediate interview / assisted / full-auto hints and Russian Интервью | Mandatory first-response menu, Russian alias mapping, updated Codex default_prompt; already selected mode does not trigger another question |
| Appropriate folders and AGENTS.md | Stack-specific bootstrap matrix, existing-first merge rules and AGENTS template with source-qualified conditional skill routes |
| Dashboard always | Created with authorized run-state during onboarding, refreshed at stage/session transitions; explicit pending projection if read-only |
| Check Context7, shadcn/ui, 21st.dev, Impeccable, frontend-design | Five-row audit distinguishing skill, tool, project config and connectivity; no inferred installation or provider authority |
| Ask about existing design and create missing design | Evidence-aware design decision, available Impeccable offer and disclosed fallbacks, one root DESIGN.md and existing design gates |
| Remember project feedback | Feedback folder, scoped source-attributed confirmed/proposed/superseded entries, use before relevant future work |
| Start/end session | Checkpoint/feedback/context/current-state reconciliation, honest progress/dashboard, saved unfinished state without false completion |
| Frontend/backend/tests | Proportional static, React+Supabase, custom full-stack and backend-only structures; risk-based test plan and negative authorization checks |

Native host dropdown registration is not implemented or claimed: the package supplies hints and mandatory text menu, and uses selectable answers only when the host supports them. These are procedural agent instructions and templates, not an installed host hook or a separate scaffolding CLI.

## Behavioral evidence

RED baseline: independent read-only review of the unmodified installed instructions found menu required only without a goal, optional dashboard, no explicit Russian alias table, no mandatory bootstrap/AGENTS/Feedback/checkpoint lifecycle, and no special five-capability audit contract.

GREEN: a separate read-only reviewer simulated all nine new [behavioral eval scenarios](../../plugins/matreshka-agent/skills/building-end-to-end/evals/evals.json). All nine passed the text-based instruction review:

1. Russian interview with supplied goal and React + Supabase.
2. Static HTML/CSS/JS with no runtime installs.
3. Session start with stale COMPLETE dashboard and an actual failed test.
4. Session end with unfinished work, explicit compact-interface preference and user-owned server.
5. Skill/tool/config/connectivity distinctions and Impeccable prerequisites.
6. Read-only onboarding without false artifact claims.
7. Existing architecture, AGENTS/context preservation and superseding feedback.
8. Partial checkpoint write/dashboard sync failure and external-text injection.
9. Menu in a host without a dropdown API.

The reviewer found one minor language inconsistency: session close required Russian even for an English session. Corrected to the active conversation language. No permission regressions were identified. This is scenario simulation, not proof of real file generation or host UI behavior. Four trigger examples also cover Russian interview/session commands and a translation non-trigger.

## Executed local checks

Used the already available bundled Python runtime; nothing was installed.
Commands below are relative to the repository and use `python` as a placeholder for that verified executable, not a statement that system Python is installed.

| Command | Result |
| --- | --- |
| `python -B plugins/matreshka-agent/scripts/validate_dev_05.py plugins/matreshka-agent --marketplace-root .` | PASS, including current manifests, eval schemas and internal links |
| Same validator with `--self-test` | PARTIAL: executable-policy negative fixture FAIL; symlink fixture SKIP (WinError 1314); other listed negative fixtures PASS |
| `python -B plugins/matreshka-agent/scripts/check_dev_05.py` | PASS |
| `python -B plugins/matreshka-agent/scripts/check_dev_05_behavioral_contracts.py` | PASS, including required presence of nine lifecycle cases |
| `python -B plugins/matreshka-agent/scripts/check_context_budget.py` | PASS; lifecycle increment 40,120 / 45,000 UTF-8 bytes; existing surface budgets unchanged |
| `python -B plugins/matreshka-agent/scripts/check_autopilot_regressions.py` | PASS |
| `python -B plugins/matreshka-agent/scripts/sync_run_state.py --self-test` | PASS, 7 existing state/snapshot checks |
| `git diff --check` | PASS |

The full validator self-test was also run against the unchanged marketplace source checkout. It reproduced the same executable-policy failure (`expected EXECUTABLE_UNEXPECTED; observed []`) and symlink skip. These results do not establish a completely passing release gate; the validator was not weakened or changed to hide them.

## Remaining acceptance

- Run package negative fixtures on the supported Linux/Python CI environment, including executable-bit and symlink cases.
- Run native disposable-project acceptance for actual scaffold creation, AGENTS mapping, design output, dashboard refresh and cross-session Feedback recovery. Test idempotent adoption of an existing project and read-only behavior.
- Verify selection hints in each target host; do not claim native autocomplete based on default_prompt alone.
- Installation/publication is a separate next step. The currently installed plugin still follows its previous source until updated through the repository's release/install workflow.
