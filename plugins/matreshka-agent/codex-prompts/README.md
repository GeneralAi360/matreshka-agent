# Optional Codex slash-prompt wrappers

Codex skills are normally invoked with `$skill-name` or from `/skills`. Codex does not register a plugin `commands/` directory as slash commands.

For people who prefer a slash command, these optional wrappers use Codex custom prompts. Copy the Markdown files into the **top level** of `~/.codex/prompts/`, reload the IDE extension or start a new Codex session, then run the listed `/prompts:...` command.

macOS/Linux:

```bash
mkdir -p ~/.codex/prompts
cp /absolute/path/to/matreshka-agent/plugins/matreshka-agent/codex-prompts/*.md ~/.codex/prompts/
```

Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force "$HOME/.codex/prompts"
Copy-Item "C:\path\to\matreshka-agent\plugins\matreshka-agent\codex-prompts\*.md" "$HOME\.codex\prompts\"
```

| Slash command | Starts skill |
| --- | --- |
| `/prompts:matreshka-orchestrate` | `orchestrating-subagent-work` |
| `/prompts:matreshka-design` | `designing-software-work` |
| `/prompts:matreshka-plan` | `planning-software-work` |
| `/prompts:matreshka-prompt` | `writing-portable-agent-prompt` |
| `/prompts:matreshka-implement` | `implementing-with-tests` |
| `/prompts:matreshka-debug` | `debugging-systematically` |
| `/prompts:matreshka-review` | `reviewing-agent-work` |
| `/prompts:matreshka-verify` | `verifying-development-work` |
| `/prompts:matreshka-finish` | `finishing-development-work` |

The wrappers do not add permissions, hooks, network access, or automation. They only expand an explicit skill invocation and pass your text as the task. Codex marks custom prompts as deprecated, so skills remain the preferred mechanism; these files are an optional compatibility layer for people who specifically need a slash command.
