# VS Code Copilot Chat Model Selector & Free OpenRouter Configuration Guide

## How Copilot Chat Models & Providers Work

GitHub Copilot Chat in VS Code allows users to switch language models via the **Models selector** located at the bottom of the chat interface.

### 1. Language Model Provider (`chatLanguageModels.json`)
Custom model providers are defined globally in:
- **Location (Windows)**: `%APPDATA%\Code\User\chatLanguageModels.json`
- **Location (macOS)**: `~/Library/Application Support/Code/User/chatLanguageModels.json`
- **Location (Linux)**: `~/.config/Code/User/chatLanguageModels.json`

The `openrouter-free-agents` skill configures a dedicated provider group:
```json
{
  "name": "Free OpenRouter",
  "vendor": "customendpoint",
  "apiKey": "${input:chat.lm.secret.-4190c49f}",
  "models": [ ... ]
}
```
In the VS Code Chat Models selector, this populates the **Other Models -> Free OpenRouter** section with all currently active free models.

### 2. Pinned Models (`chatModelPinned`)
VS Code tracks pinned models in its profile state database:
- **Location (Windows)**: `%APPDATA%\Code\User\globalStorage\state.vscdb`
- **Location (macOS)**: `~/Library/Application Support/Code/User/globalStorage/state.vscdb`
- **Location (Linux)**: `~/.config/Code/User/globalStorage/state.vscdb`
- **Database Table**: `ItemTable`
- **Key**: `chatModelPinned`
- **Format**: JSON array of model ID strings, e.g.:
  ```json
  [
    "copilot/gpt-5.6-luna",
    "customendpoint/Free OpenRouter/cohere/north-mini-code:free",
    "customendpoint/Free OpenRouter/nvidia/nemotron-3.5-lightning:free"
  ]
  ```

#### Pinning & Un-Pinning
- **Pinning**: Models with ID `"customendpoint/Free OpenRouter/<model_id>"` are pinned for immediate access.
- **Un-pinning**: When a model is no longer free, it is automatically removed from `chatModelPinned`. Non-OpenRouter models (Copilot, OpenAI, Anthropic, Gemini) are strictly preserved.

### 3. Separation from Set Agents (No Custom Agents)
- **Models belong in the Models selector**: Language models provide completion/chat backends and belong under **Other Models -> Free OpenRouter** in the model picker.
- **Set Agents stays clean**: GitHub Copilot Set Agents (Agent / Ask / Plan) should NOT be cluttered with dozens of model personas. The skill deliberately avoids generating `.agent.md` files and purges any legacy agent files so that Set Agents remains clean and organized.
