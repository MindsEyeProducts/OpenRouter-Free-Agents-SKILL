---
name: openrouter-free-agents
description: "Search OpenRouter for current free AI models and update the Free OpenRouter group in the VS Code Copilot Chat Models selector. Does not populate Custom Agents in Set Agents."
---

# Free OpenRouter Models Sync

Queries the live OpenRouter API for currently available free models, updates the VS Code Copilot Chat Models selector under **Other Models -> Free OpenRouter**, and un-pins/removes any models that are no longer free. Does not create or populate Custom Agents in GitHub Copilot Set Agents.

## When to Use
- User wants to find or use free OpenRouter models in VS Code Copilot Chat.
- User wants to update or refresh the **Other Models -> Free OpenRouter** group in the Models selector.
- User wants to remove expired free models.
- User invokes `/openrouter-free-agents` in Copilot Chat.

## Architecture

This skill configures and maintains the Models selector for free OpenRouter models without cluttering GitHub Copilot Set Agents:
1. **Language Model Provider Configuration (`chatLanguageModels.json`)**: Configures the dedicated `Free OpenRouter` custom endpoint provider group, placing active free models under **Other Models -> Free OpenRouter** in the Models selector.
2. **Model Selector Quick Access (`chatModelPinned` in `state.vscdb`)**: Pins active free models under `customendpoint/Free OpenRouter/<model_id>` for instant access and automatically unpins expired models.
3. **Agent Selector Cleanliness**: Deliberately does NOT create Custom Agent files (`.agent.md`), keeping GitHub Copilot's Set Agents menu (Agent / Ask / Plan) clean and unpolluted. Automatically detects and purges any legacy `openrouter-*.agent.md` files from workspace and user profile directories.

## Availability & Scope

This skill is installed for both **local workspace** and **global cross-workspace** use:

| Scope | Type | Location | Purpose |
| :--- | :--- | :--- | :--- |
| **Global (Personal)** | Skill Definition | `~/.copilot/skills/openrouter-free-agents/`<br>`~/.agents/skills/openrouter-free-agents/`<br>`~/.claude/skills/openrouter-free-agents/` | Invokable via `/openrouter-free-agents` in any project across VS Code. |
| **Global (Personal)** | Model Provider Group | `chatLanguageModels.json` (`Free OpenRouter` group) | Populates active free models under **Other Models -> Free OpenRouter** in the Chat Model Picker across all workspaces. |
| **Global (Personal)** | Pinned Models | `state.vscdb` (`chatModelPinned`) | Quick access to active free models in the Models selector. |
| **Local (Workspace)** | Skill Definition | `.agents/skills/openrouter-free-agents/` | Team/project-shared skill repository. |

## Quick Execution

Execute the sync script to update free models (works from any directory or workspace):

### 1. Standard Sync (Local & Global)
```powershell
python -B "$HOME/.copilot/skills/openrouter-free-agents/scripts/sync_openrouter_agents.py"
```
*(If working inside this project workspace, `python -B .agents/skills/openrouter-free-agents/scripts/sync_openrouter_agents.py` also works).*

### 2. Preview changes (Dry Run)
```powershell
python -B "$HOME/.copilot/skills/openrouter-free-agents/scripts/sync_openrouter_agents.py" --dry-run
```

### 3. Tool-Enabled Models Only (Recommended for coding models)
```powershell
python -B "$HOME/.copilot/skills/openrouter-free-agents/scripts/sync_openrouter_agents.py" --tools-only
```

### 4. Inspect Free Models Only
```powershell
python -B "$HOME/.copilot/skills/openrouter-free-agents/scripts/sync_openrouter_agents.py" --list
```

### 5. Generate Coding Capabilities Evaluation Document
```powershell
python -B "$HOME/.copilot/skills/openrouter-free-agents/scripts/sync_openrouter_agents.py" --eval-md
```

## Procedure for Agents

When requested to run this skill or sync free OpenRouter models:

1. **Run the sync script**:
   Invoke `run_in_terminal` with:
   ```powershell
   if (Test-Path ".agents/skills/openrouter-free-agents/scripts/sync_openrouter_agents.py") {
       python -B .agents/skills/openrouter-free-agents/scripts/sync_openrouter_agents.py
   } else {
       python -B "$HOME/.copilot/skills/openrouter-free-agents/scripts/sync_openrouter_agents.py"
   }
   ```
2. **Inspect script output**:
   Review the list of models updated in the `Free OpenRouter` group, newly pinned models, retained models, unpinned models, and legacy agent files purged.
3. **Report to User**:
   Summarize:
   - Free models configured in **Other Models -> Free OpenRouter**.
   - Models pinned/retained in the Models selector.
   - Unpinned models (models that expired or are no longer free).
   - Confirmation that Custom Agents are NOT populated in Set Agents (and any legacy `.agent.md` files were cleaned up).
   - How to select them in Copilot Chat: open the Models selector at the bottom of the chat panel and choose from the **Other Models -> Free OpenRouter** group.
   - Prompt the user to reload the window to apply changes:
     Press `Ctrl+Shift+P` (or `F1`) and run:
     **`Developer: Reload Window`**
   - Ask the user:
     "Would you like a coding capability evaluation of the identified free models? (Y/N)"
   *(Do NOT ask to create the markdown document yet; that prompt occurs only after the evaluation results are displayed).*
4. **Evaluation & Health Check (When user responds Y)**:
   - Perform the coding capability evaluation AND live health check across the active free models by querying OpenRouter endpoint telemetry (`/api/v1/models/{author}/{slug}/endpoints`).
   - Present the evaluation findings to the user:
     - Tier breakdown (S, A, B, C, N/A) with **Health status icons** (🟢 Healthy, 🟡 Degraded, 🔴 Offline) and technical specifications (Params, Context, Tools, Reasoning).
     - Recommended models by use case (Daily Coding, Deep Architecture, Low-Latency Iteration, Multimodal UI).
     - How to select models in VS Code Copilot Chat.
     - Real-Time Model Health & Operational Status table placed at the bottom (Upstream Provider, Status, 5m Uptime, 24h Uptime, Latency, Demand).
   - **Immediately following these evaluation and health check results**, prompt the user:
     "Create MD document with this OpenRouter Free Models coding capabilities evaluation? (Y/N)"
5. **Markdown Document Generation (When user responds Y to MD creation)**:
   - Generate or update `OpenRouter_Free_Models_Coding_Capability.md` in the workspace root directory (with the Health column in the Tier Summary and the Real-Time Model Health table at the bottom), or execute:
     ```powershell
     python -B .agents/skills/openrouter-free-agents/scripts/sync_openrouter_agents.py --eval-md
     ```
   - Confirm to the user that `OpenRouter_Free_Models_Coding_Capability.md` has been created or updated in the workspace root.

## References
- [OpenRouter API Specification](./references/openrouter-api.md)
- [VS Code Model Selector & Free OpenRouter Configuration Guide](./references/agent-pinning.md)
- [OpenRouter Free Models Coding Capability Document](./OpenRouter_Free_Models_Coding_Capability.md)
- [Sync Script Source](./scripts/sync_openrouter_agents.py)

---

### Reload & Follow-Up Prompts
Follow this sequential prompt flow across conversation turns:

#### Phase 1: Immediately after Initial Sync
1. Window Reload:
   > Press `Ctrl+Shift+P` (or `F1`) and run:
   > **`Developer: Reload Window`**
2. Evaluation Prompt:
   > Would you like a coding capability evaluation of the identified free models? (Y/N)

#### Phase 2: Only AFTER Presenting Evaluation & Health Check Results
3. Evaluation Markdown Document Generation Prompt:
   > Create MD document with this OpenRouter Free Models coding capabilities evaluation? (Y/N)
