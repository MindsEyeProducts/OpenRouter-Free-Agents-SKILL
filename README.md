# OpenRouter Free Agents Skill

Keeps the currently free OpenRouter models available in VS Code Copilot Chat under **Other Models → Free OpenRouter**. The skill updates the custom model provider, pins active free models, unpins expired ones, and removes legacy generated agent files so the **Set Agents** menu stays clean.

## Install

Clone this repository into a supported personal skill directory. For Codex:

```powershell
git clone https://github.com/MindsEyeProducts/OpenRouter-Free-Agents-SKILL.git "$HOME/.codex/skills/openrouter-free-agents"
```

For GitHub Copilot:

```powershell
git clone https://github.com/MindsEyeProducts/OpenRouter-Free-Agents-SKILL.git "$HOME/.copilot/skills/openrouter-free-agents"
```

## Run

From the cloned repository:

```powershell
# Preview changes
python -B scripts/sync_openrouter_agents.py --dry-run

# Sync every currently free model
python -B scripts/sync_openrouter_agents.py

# Sync only models that advertise tool calling
python -B scripts/sync_openrouter_agents.py --tools-only
```

After syncing, reload VS Code with **Developer: Reload Window**, then choose a model from **Other Models → Free OpenRouter** in the Copilot Chat model selector.

## Contents

- [`SKILL.md`](./SKILL.md) — agent instructions and workflow
- [`scripts/sync_openrouter_agents.py`](./scripts/sync_openrouter_agents.py) — deterministic sync utility
- [`references/openrouter-api.md`](./references/openrouter-api.md) — OpenRouter API notes
- [`references/agent-pinning.md`](./references/agent-pinning.md) — VS Code provider and pinning details
- [`OpenRouter_Free_Models_Coding_Capability.md`](./OpenRouter_Free_Models_Coding_Capability.md) — latest generated coding-capability evaluation

## License

MIT
