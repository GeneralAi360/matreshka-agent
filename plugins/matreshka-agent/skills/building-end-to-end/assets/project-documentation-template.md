# Project documentation sections

Create separate documents only where no canonical equivalents exist. Replace drafting fields with confirmed facts or explicit pending decisions. No invented commands, credentials or duplicated specifications.

## docs/README.md

Index: purpose/spec, architecture, local development, testing, conditional API/data docs, DESIGN.md for UI, capabilities, feedback, checkpoint and current dashboard. Link actual files; keep instructions in their owning document.

## docs/architecture.md

- Source requirement/decision references and current status.
- Shape and why it fits: split / integrated fullstack / managed / backend-only / static.
- Frontend, backend, data engine and hosting decisions separately; unresolved choices and their effect.
- Each area's actual paths, runtime, inputs/outputs and responsibility.
- API/contract boundaries; authentication/authorization ownership where relevant.
- One owner/path per database schema's migrations; synthetic seeds and compatibility expectations.
- Existing conventions retained; what is deliberately absent and why.
- Structural projection: docs/bootstrap.json; it is not runtime evidence or the task ledger.

## docs/local-development.md

| Component | Required version/source | Check command | Setup/start command + cwd | Preconditions/status | Process/port owner |
| --- | --- | --- | --- | --- | --- |
| <actual app/runtime> | <manifest/lockfile or unresolved> | <safe version check> | <declared command or pending> | <actual evidence> | <owner or not started> |

List frontend, backend and data separately where applicable. Explain safe stop/restart of owned processes, configuration variable names and scope (client versus server), test environment selection and common failures. Real secrets never belong here. No tool installation or service execution merely because a command is documented.

## docs/api.md — only for applicable API contracts

Operation, request/response, validation/error shapes, actor/permissions and contract-test reference. Link source schemas where authoritative; do not maintain competing copies.

## docs/data-access.md — only for data/access boundaries

Entities/ownership, selected engine, schema/migration locations, actual authorization boundary, constraints and applicable denied-access scenarios. Record placement/provider independently of engine. Describe safe test setup/cleanup and prerequisites; omit credentials, real account identifiers and personal records.

## Maintenance

After verification, use the existing docs-maintainer for affected sections only. AGENTS owns routing, testing/runtime docs own commands, Feedback owns preferences, checkpoint owns continuation, ledger owns progress.
