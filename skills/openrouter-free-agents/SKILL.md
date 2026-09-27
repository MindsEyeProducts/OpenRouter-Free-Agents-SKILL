---
name: openrouter-free-agents
description: "Search OpenRouter for current free AI models, update the Free OpenRouter group in the VS Code Copilot Chat Models selector, and optionally preview or save a coding capability and health report. Does not populate Custom Agents in Set Agents."
---

# Free OpenRouter Models Sync

This plugin uses the same skill as the standalone repository install. Read the full instructions in [`../../SKILL.md`](../../SKILL.md) before acting, and honor its flags, workflow choices, permission guidance, and reporting requirements.

The bundled command is [`../../scripts/sync_openrouter_agents.py`](../../scripts/sync_openrouter_agents.py), relative to this file. The repository root `SKILL.md` describes the script as relative to itself; for this plugin installation, use this explicit plugin-root path. Supporting notes are in [`../../references/openrouter-api.md`](../../references/openrouter-api.md) and [`../../references/agent-pinning.md`](../../references/agent-pinning.md).

Run the script once for the requested workflow from the user's project directory. For example, on Windows, `python -B <resolved path to ../../scripts/sync_openrouter_agents.py> --eval-md` synchronizes and saves the coding capability and health report. Keep the normal host approval controls and follow the root skill's instructions to present results.
