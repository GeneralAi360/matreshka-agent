# Testing — adapt to the actual project

Architecture/spec references: <canonical paths>. Current project identity: <baseline>. Tests planned here are not results.

| Requirement/check ID | App owner / layer | Scenario and expected result | Cwd / command / declaration source | Prerequisites and safe target | Status / reason | Evidence / baseline |
| --- | --- | --- | --- | --- | --- | --- |
| <ID> | <actual frontend/backend/data boundary> | <observable positive/negative behavior> | <real command or unresolved> | <runtime, permitted setup, synthetic data> | <PLANNED/NOT_RUN/BLOCKED/PASSED/FAILED/NOT_APPLICABLE> | <actual report or none> |

## Commands

Separate frontend, backend, database/access and browser commands. Name the actual manifest/config that defines each command and its cwd. Note targeted file/filter syntax and when to run the full suite/build. State unavailable tools explicitly. A package script's presence does not prove it runs.

## Fixtures and runtime

- Exact safe test-environment identity (no secrets), setup/mutation scope and cleanup strategy.
- Synthetic account/data creation, isolation between cases, fixture owner.
- Server/browser process ownership, addresses/ports and safe termination of owned processes.
- Missing permission/runtime and its effect on applicable tests.

## Evidence and completion

- Per executed check: baseline, command/cwd, target, exit/signal, passed/failed/skipped counts, safe report references.
- Distinguish API tests, browser tests with mocks, browser tests with actual backend/data, and visual/manual observations.
- Reasoned NOT_APPLICABLE is different from unavailable execution. Zero tests/all skipped cannot establish PASS.
- Independent G4 uses the original source brief and product, not this document. Completion remains with the controller's existing gates.
