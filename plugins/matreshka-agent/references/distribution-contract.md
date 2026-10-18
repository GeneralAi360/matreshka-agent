# Matreshka distribution and identity

The eleven canonical skills are one plugin with shared root resources and cross-skill
dependencies. Copying a canonical `skills/<name>` directory alone is not a supported
installation. Missing package identity/resources returns HANDOFF_REQUIRED before
development; it must not silently use an older, same-named skill or a plugin cache.
Source presence, package byte integrity, native workflow behavior, technical evidence,
visual inspection and user approval are separate claims.

## Full plugin and portable skill adapters

Native plugin entry names remain `matreshka-agent:<skill>`; UI default prompts must
use that qualified form. Existing generic separately imported skills are not modified
or treated as this plugin. A direct bounded task does not require an end-to-end run.

`scripts/package_distribution.py build --output <new-directory-outside-package>`
validates the source and produces a complete plugin ZIP plus eleven standalone skill
ZIPs named `matreshka-agent-<skill>`. These are generated distribution adapters, not
new manually maintained controllers. Each adapter includes the full dependency set
from the same source snapshot, so copying only that adapter directory is sufficient.
Canonical SKILL.md documents become WORKFLOW.md inside the adapter's bundled package;
their Markdown links and package-owned JSON resource paths are rewritten mechanically.
External peer SKILL.md discovery remains unchanged. Only the outer adapter is
discoverable as SKILL.md, preventing nested generic skills from being registered.
Runtime/template/source-contract files remain bundled. Internal project reports,
test workspaces, result artifacts, Python caches and unit tests are excluded.

The builder does not install, publish, merge, release, update external skills or alter
host settings. Choose a new output directory for each build; an existing successful
build is never overwritten. Archive entries use deterministic ordering/timestamps.
The manifest version remains the existing development-track version until separately
authorized release gates pass. `distribution.json` also records source ref/SHA, dirty
snapshot status, source tree digest, entrypoint map and exact payload file hashes.
A hash detects changed bytes; this unsigned record does not authenticate an author
or prove that the recorded commit alone includes uncommitted changes.
Exported full-plugin entries use mandatory `probe` rather than checkout-only `source`.
An installation marker also prevents missing-stamp fallback in the `source` helper.
Removing metadata from an installed export must never weaken its entry preflight.

## Preflight and acceptance

In a full source checkout, `source --root <plugin-root> --entry <skill>` checks the
plugin identity and required shared resources without writes. Its SOURCE_PRESENT
result is not an installed-package comparison or native behavior verdict.

In a generated installation, `probe --root <installed-root> --entry <skill>` validates
the inventory, hashes, entry mapping, manifests and contained resource links. Portable
adapters supply their expected source digest explicitly. Reject missing, changed or
unexpected payload, wrong selected adapters, unsafe paths and symlinks. Do not copy
missing files from ambient installations. No lock or report is created by preflight.

`verify --archive <built.zip>` unpacks into a temporary directory, copies only the
selected install root to an unrelated host layout and removes the download. It runs
the installed report CLI with an empty PYTHONPATH and no site packages: initialize,
update, reread, check the same homepage, retained revision and external docs root.
It also runs the bundled context-budget command against actual installed paths.
No product source is changed. The smoke test does not mark project criteria PASS or
claim a browser view. Visual inspection and native host skill selection still need
their actual host-specific evidence. CI runs these archive scenarios on Windows and
Ubuntu and runs negative corruption/incomplete-install cases separately.

Matreshka Project Start, find-skills and other external peers keep their own source,
identity and update lifecycle. This package does not rewrite or install them.
