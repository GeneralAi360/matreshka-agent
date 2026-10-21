# Specification-driven project bootstrap

Use with [project-lifecycle.md](project-lifecycle.md). The controller owns writes/gates; directories do not prove runtime behavior.

## Resolve independent decisions

Inspect accepted specification, repository and decisions before asking questions. Resolve these axes separately; record provenance in canonical context and `docs/architecture.md` (or existing equivalents):

| Axis | Required decision | Do not infer |
| --- | --- | --- |
| Frontend | UI needed, stack, separate or integrated app | React does not choose backend language |
| Backend | Own API/business logic, fullstack server modules, managed backend, or combination | A hosted database does not replace an agreed own API |
| Data | Database needed, engine, schema/migration owner, access boundary | PostgreSQL does not mean Supabase; not every app needs RLS |
| Hosting | App, API and data placement separately; existing resources | Database hosting does not select Auth, Storage or application hosting |
| Verification | Required layers, actual tools, safe targets, permitted setup | Test directory names do not prove executable checks |

Unresolved hosting does not block confirmed local boundaries. An unresolved backend shape blocks dependent scaffolding, not the menu/dashboard or independent docs. Ask material unanswered questions in Interview/Assisted; Full Auto may choose reversible local decisions within scope and record assumptions. Never infer a provider from an example.

## Select a shape, then map actual paths

| Profile | New-project example | Backend/data/test ownership |
| --- | --- | --- |
| `split` | `apps/frontend/`, `apps/backend/` | Each app owns its unit/component or unit/API/integration tests; backend owns migrations if it owns the schema |
| `fullstack` | `apps/web/` | Name actual client and server modules and their tests using framework conventions; a single app still has server responsibilities |
| `managed` | `apps/frontend/` plus selected service contract/configuration | Document external backend boundary and verify its integration/access contract; own API may coexist and must be mapped |
| `backend` | `apps/backend/` or existing root application | Server rules, API, storage, integrations and access tests; no browser or DESIGN.md requirement without UI |
| `static` | `index.html`, `assets/` | Applicable browser/manual checks; no runtime, database, package.json or Docker just for scaffolding |

Map adopted projects to existing paths without migration. Profiles do not choose languages: a Python backend keeps Python commands beside an npm frontend. Workspaces, `packages/` and `infra/` require an actual tooling/shared-code/infrastructure need.

One schema has one canonical migration owner/path. A split app may use `apps/backend/db/{migrations,seeds}`; an ORM/framework/provider may require another path. Do not duplicate migrations in a second location. Seeds contain synthetic test/demo data. Provider-specific folders, Auth, Storage, functions and RLS appear only for selected capabilities. Supabase used only for PostgreSQL does not remove `apps/backend/`.

Example for an agreed split app with a database:

```text
apps/frontend/{src,public,tests/unit,tests/components}
apps/backend/{src,db/migrations,db/seeds,tests/unit,tests/integration}
tests/integration/       # cross-service contracts only, not duplicate API tests
tests/e2e/               # browser journeys
tests/fixtures/          # synthetic data with an explicit lifecycle
docs/{architecture,local-development,testing}.md
```

Create applicable directories and genuine stack configurations, never success-only dummy scripts. Preserve user files, nested repos and instructions; reconcile conflicts. Repeat bootstrap fills missing artifacts/owned sections without resetting code or history.

## Materialize a reviewable bootstrap

1. Show selected shape, actual paths, unresolved decisions and write scope. Use the current scope; do not ask for approval again for already authorized local scaffolding.
2. Create applicable lifecycle outputs and adapt [project-documentation-template.md](../assets/project-documentation-template.md). Keep AGENTS short and link details. `docs/api.md` is conditional on an API; `docs/data-access.md` is conditional on data/access boundaries. Existing equivalent documents win over new duplicates.
3. Follow [testing-bootstrap.md](testing-bootstrap.md) to materialize appropriate runner configurations, real command declarations, safe fixtures and first meaningful checks. Install/start permissions remain separate from file creation. Configuration may be prepared while execution is `NOT_RUN`.
4. After profile resolution, adapt [bootstrap-map-example.json](../assets/bootstrap-map-example.json) into `docs/bootstrap.json`: actual paths and decisions, explained NONE/UNRESOLVED values, no secrets or private data. This structural projection is not a second ledger.
5. Inspect files, doc links, commands and boundaries. With existing Python, optionally run packaged `scripts/check_project_bootstrap.py --project <root>`; otherwise use the checklist manually. Do not install Python for a site. The checker never executes project commands.
6. Report files, structural result, pending checks, actual evidence and unresolved decisions separately. Pass relevant rows to planning/task briefs; reconcile existing ledger/dashboard/checkpoint without new state enums or false completion.

## Bootstrap map contract

`schema_version: 1`; `profile` from the table. Required `documents` maps architecture/testing/local_development roles to existing documents, including adopted equivalents; `source` equals its architecture path. `decisions` describes frontend/backend/database/hosting independently. `areas` maps frontend/backend/data to actual paths; a managed backend may reference its contract document. `migration_roots` lists each canonical root once. `files` lists outputs including README, AGENTS and applicable lifecycle artifacts. Paths are relative, without traversal, symlinks or secrets; never list real env files.

`checks` rows have unique ID, area owner, layer, scenario, cwd, command argument array, command-source path, prerequisites, safe target label, status and reason. Empty command + reason represents an unresolved runner; never executable success. Layers: unit/component/api/integration/access/browser/visual/build. Statuses: PLANNED/NOT_RUN/BLOCKED/PASSED/FAILED/NOT_APPLICABLE. These are map row labels; translate to existing ledger enums without changing its schema. A frontend has a browser row; a backend has unit and integration rows, using reasoned NOT_APPLICABLE where legitimately unnecessary. For backend-only API E2E, use the integration/API layer, never pretend a browser exists.

Automated PASSED requires command/source, exit, positive passed count, failed/skipped counts, baseline and safe evidence path. Keep manual/build/visual observations in their normal reports without fake test counts. Unexecuted automation remains NOT_RUN or reasoned NOT_APPLICABLE. The checker validates declarations, not report authenticity, design correctness, exhaustive links or runtime safety. `STRUCTURE_VALID` always has `runtime: NOT_VERIFIED`; it cannot replace verification or G1–G4.
