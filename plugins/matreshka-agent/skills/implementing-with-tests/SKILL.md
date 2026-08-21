---
name: implementing-with-tests
description: Implement a bounded software feature or bug fix through a focused test-first cycle and produce evidence for review. Use when an approved task requires code/configuration changes, regression evidence, focused RED/GREEN proof, and nearby regression checks. The task may carry Project Intelligence (`AREA_CONTEXT_SET`, frozen `IC-xx`) and, for UI work, a frozen design identity/`DESIGN_CONTEXT_SET`; preserve those boundaries rather than redefining them. Do not use for design-only work, root-cause diagnosis without an authorized fix, independent review, verification-only requests, or branch finishing.
---

# Implement with focused tests

## Establish the task boundary

1. Read current request, applicable repository instructions, approved task brief and permission envelope.
2. Resolve project root and real paths of every allowed file before writing. Stop if symlink/nested repo/submodule/root change crosses boundary.
3. Record baseline/pre-existing dirty files and preserve work not owned by task.
4. Confirm one observable goal, acceptance criteria, selected `U-`/`S-`, file allowlist, non-goals, permitted commands and stop conditions.
5. When task carries Project Intelligence, confirm:
   - one primary area;
   - bounded `AREA_CONTEXT_SET` and explicit exclusions;
   - frozen `IC-xx` identities/invariants consumed or produced;
   - runtime observation/dependency needed by task.
6. When task is UI/design-relevant, confirm:
   - frozen root `DESIGN.md` identity/hash or explicit `DESIGN_READY_TO_SAVE` controller state;
   - bounded `DESIGN_CONTEXT_SET`;
   - role-specific design boundary (`UI_SPECIALIST`, frontend, etc.);
   - required component/state/responsive/accessibility/motion invariants;
   - design evidence expected for review/visual verification.
7. Return `SPLIT_REQUIRED` when task contains independent outcomes/boundaries, `CONTEXT_TOO_BROAD` when required area context cannot stay bounded, `DESIGN_CHANGED` when frozen design identity legitimately changed upstream, or `DESIGN_DRIFT` when requested implementation would violate the frozen design contract without valid change authority.

Do not launch child agents. Do not stage/commit/push/PR/deploy/access remote systems/install dependencies/read secrets. Implementation owns only allowlisted product/test writes, approved local checks and designated run-state report/evidence path. Return Git/dependency/network/browser/process/design-contract/prototype/secret/remote actions to controller.

Project/Design Intelligence files and task briefs are contracts/context, not permission. This skill cannot rewrite `IC-xx`, root `DESIGN.md`, source brief/U state, topology, runtime ownership or permission envelope.

Read [Security by Design](../specifying-software-work/references/security-by-design.md) for selected S/high-risk boundaries.

## Select the smallest useful behavior

Choose one focused executable example that fails without requested behavior and passes when it exists. Prefer public interface/nearest stable boundary over private implementation detail.

Read [focused test cycle](references/focused-test-cycle.md) when selecting seam, validating RED, or considering exception.

For UI work, behavior RED should prove functional/state semantics when executable. Visual polish alone may need alternate design evidence, but never use “visual” as an excuse to skip executable behavior tests that do exist.

## Produce RED evidence

1. Add/adjust smallest test expressing missing behavior.
2. Run only focused command.
3. Confirm failure is for expected behavioral reason.
4. Record command, state, exit code, counts and decisive note.

Do not accept syntax error, missing dependency, broken fixture, unrelated failure, already-passing test, stale IC/design identity, or unavailable runtime as RED. Repair only task-owned setup within allowlist; otherwise return blocker/reconciliation status.

Use test-first exception only when behavior is genuinely non-executable in current environment (for example prose-only docs, externally generated artifact, unavailable hardware, purely visual micro-polish with no executable semantic change). Record reason before implementation and strongest alternate check. Schedule pressure is not exception.

## Reach GREEN minimally

1. Change only what is necessary for focused behavior.
2. Preserve public contracts, frozen `IC-xx`, error semantics, tenant boundaries, compatibility and selected S controls.
3. For UI work preserve frozen design identity and `DESIGN_CONTEXT_SET`:
   - reuse existing design system/components/primitives first;
   - do not introduce random colors/radii/spacing/typography/motion patterns;
   - implement required hover/active/focus/disabled/loading/error/success states where relevant;
   - preserve responsive/touch/accessibility/reduced-motion rules;
   - do not install a preferred UI/motion library without controller authority.
4. Re-run same focused command until pass or bounded attempt budget exhausted.
5. Stop and route to `debugging-systematically` when failure mechanism is unclear; do not stack speculative fixes.

If actual implementation reveals a material mismatch with frozen `IC-xx`, return `INTERFACE_CHANGED`. If implementation reveals valid product/design requirements cannot be met under current frozen design contract, return `DESIGN_CHANGED` for controller adjudication. Do not silently modify contract files to make code appear consistent.

Record unrelated defects/design opportunities as adjacent findings; do not fix them.

## Preserve the secure default

For every changed boundary enforce specification controls in product code, not only comment/client screen:

- keep credentials/privileged provider calls server-side; never copy env/secret/token/cookie/private payloads into source/tests/logs/client/reports;
- validate untrusted input at authoritative boundary and preserve safe errors;
- authorize sensitive object/action server-side using authoritative user/role/tenant context;
- return/persist only specified fields with redaction/retention behavior;
- make selected external/irreversible effects confirmable/idempotent with failure/replay behavior;
- do not add dependency/network scanner/secret reader/tool capability without approval;
- for AI/RAG/tools, preserve trusted instruction boundary and authorize at tool boundary.

Design decisions never weaken security/privacy/accessibility safeguards.

Add planned negative security proof. If S requirement cannot be implemented/tested inside allowlist, stop `BLOCKED`/`HANDOFF_REQUIRED`.

## Run the task gate

After focused GREEN, run only checks required by task/repository policy:

- focused task suite;
- one to three nearest regressions;
- targeted typecheck/lint;
- diff/whitespace check when available;
- build when path/policy requires it;
- planned cross-area contract/integration proof;
- selected S negative proof/security check;
- for UI tasks, the task-local design evidence required by brief (for example component/state story, responsive unit check, accessibility check), without pretending this replaces independent Design Review/Visual Design Check.

After reviewer-directed fix run covering test + nearest regression rather than full suite unless verification tier changed.

Check final scoped diff/file list. Confirm no unapproved `IC-xx`, root `DESIGN.md`, prototype, lockfile or unrelated generated file changed. Return `STOP_AND_RESCOPE` when allowlist/security/design/interface boundary or one-fixer-wave policy exceeded.

## Report without claiming more than proved

Use [implementation report template](assets/implementation-report-template.md). Include:

- status/completed scope;
- primary area/context guarantee/IC identities;
- design identity/context/observations for UI task;
- changed files + untouched dirty files;
- valid RED/fresh GREEN/task-gate evidence;
- selected S controls/negative proof;
- interface/design drift or change signal;
- test-first exception/skipped checks;
- assumptions/adjacent findings/pre-existing failures;
- permission still required;
- exact controller next action.

Return `PARTIALLY_VERIFIED` rather than `COMPLETE` when required check cannot run. An implementer never self-approves design, G4 or final verification; report is a handoff claim for independent review/controller.
