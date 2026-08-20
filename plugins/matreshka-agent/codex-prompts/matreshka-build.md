---
description: Build or extend software through Matreshka Agent's safe end-to-end entry
argument-hint: "[interview|assisted|full-auto] [continue-project|existing-project] <TASK>"
---

Use $$matreshka-agent:building-end-to-end for this substantial software request.

Request: $ARGUMENTS

User-facing modes:
- `interview` — ask one important product question at a time before building;
- `assisted` — ask only important questions; default;
- `full-auto` — make safe reversible local technical decisions automatically.

Project shortcuts:
- `continue-project` — continue a project already managed by Matreshka;
- `existing-project` — work on an existing project that did not previously use Matreshka.

Auto-detect the project scenario from read-only repository evidence when the user does not name one. Keep launch scenario, public interaction mode, execution profile, internal controller autonomy, and permissions separate. No mode/scenario grants Git, network, secrets, providers, deploy, destructive, or remote authority. Route the actual workflow only to Matreshka Agent's namespaced controller, preserve source-intent traceability, security, review, technical verification, and G4 blind acceptance, and stop with `DECISION_MAP_REQUIRED` when one trustworthy specification cannot bound the destination.
