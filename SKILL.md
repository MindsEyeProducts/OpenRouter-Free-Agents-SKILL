---
name: openrouter-free-agents
description: "Search OpenRouter for current free AI models, update the Free OpenRouter group in the VS Code Copilot Chat Models selector, and optionally preview or save a coding capability and health report. Does not populate Custom Agents in Set Agents."
---

# Free OpenRouter Models Sync

Use the bundled `scripts/sync_openrouter_agents.py` for model synchronization and evaluation. It queries OpenRouter, configures **Other Models -> Free OpenRouter**, pins active free models, unpins expired models, and cleans legacy `openrouter-*.agent.md` files.

## Select the requested workflow

Honor flags and natural-language choices supplied with `/openrouter-free-agents`. An upfront request to evaluate and save a report authorizes that complete workflow; do not ask the evaluation or Markdown Y/N questions again.

| Request | Script arguments | Result |
| --- | --- | --- |
| Sync and save the evaluation | `--eval-md` | Sync once, fetch health once, save the report. |
| Sync models | No arguments | Sync and print the active model list and changes. |
| Preview evaluation / health only | `--evaluate` | Print the complete Markdown report; no VS Code updates, cleanup, or report file writes. |
| List models only | `--list` | Print the model list; no changes. |
| Preview synchronization changes | `--dry-run` | Show the planned sync without applying it. |

`--tools-only` can be added to any workflow and must be retained in later evaluation requests for that run. `--eval-md`, `--evaluate`, and `--list` are mutually exclusive. `--dry-run --eval-md` previews synchronization and the destination without fetching health or writing a report.

## Run one bundled command

Resolve `scripts/sync_openrouter_agents.py` relative to **the SKILL.md being used**. Use that resolved path in one terminal invocation. This works for a repository checkout, `.agents/skills`, `.github/skills`, and personal skill installations without maintaining separate path-selection snippets.

For example, with the personal Copilot installation:

```powershell
python -B "$HOME/.copilot/skills/openrouter-free-agents/scripts/sync_openrouter_agents.py" --eval-md
```

Use the current project as the working directory. If the terminal is elsewhere, pass `--workspace-dir "<absolute project path>"`; relative report filenames resolve against that project. `--eval-md "report.md"` selects a different filename.

- Use the command's model list and sync summary. A successful sync does not need a follow-up `--list` or duplicate verification run.
- Use `--evaluate` for an evaluation-only request. The CLI provides all endpoint queries and report formatting; do not reconstruct them with Python snippets, Pylance, or per-model terminal calls.
- Inspect failures before retrying. Retry for a concrete error, not merely to obtain the same output through another tool.
- Keep normal host approval controls. Do not change permission settings as part of synchronization. A skill cannot promise a fixed number of Allow prompts.

## Present results and finish

For synchronization, summarize configured, pinned, retained, and unpinned models and legacy file cleanup from the actual output. Report errors or skipped operations accurately. Custom Agents in **Set Agents** are not created.

For `--eval-md`, read the saved report with a file-reading tool, summarize its tiers, use cases, and health, and link the file. The default destination is `OpenRouter_Free_Models_Coding_Capability.md` in the current project. No further evaluation or save question is needed.

For `--evaluate`, present the Markdown returned on stdout. If the user requested only a preview, honor that choice. If they have not decided whether to save, offer to save after showing the result. On approval, write the captured Markdown using the host's file-editing tool; reuse the displayed result rather than resynchronizing or fetching health again. Explain if the complete prior output is unavailable before fetching a replacement.

For a bare invocation with no scope specified, perform the standard sync and offer the optional evaluation. If accepted, run `--evaluate`, show the result, and offer to save it. Skip these questions whenever the user's request already answers them.

After completing the requested sync and any chosen evaluation/save steps, ask the user to run **Developer: Reload Window** with `Ctrl+Shift+P` (or `F1`). Then select a model under **Other Models -> Free OpenRouter** in Copilot Chat. Preview, list, and dry-run modes do not require a reload by themselves.

The report combines live API data with maintained coding tiers and model notes. Describe it as a capability and health report, not a fresh benchmark run.

## Files affected by synchronization

- VS Code user `chatLanguageModels.json`: the Free OpenRouter provider group.
- VS Code user `globalStorage/state.vscdb`: model pinning and visibility.
- Workspace and user prompt directories: legacy `openrouter-*.agent.md` cleanup.
- Current project report: written only when `--eval-md` or a later save is requested.

`--no-db-sync` skips only database updates; provider configuration and legacy cleanup still run.

## References

- [OpenRouter API notes](./references/openrouter-api.md)
- [VS Code provider and model pinning](./references/agent-pinning.md)
- [Bundled sync and evaluation script](./scripts/sync_openrouter_agents.py)
