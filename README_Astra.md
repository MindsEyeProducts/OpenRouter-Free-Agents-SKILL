# OpenRouter Free Agents Skill

## Prerequisites

Before installing and running this skill, make sure you have:

- **VS Code with Copilot Chat available.** Use a desktop installation with support for agent skills, terminal commands, and custom model providers. The setup instructions in this README use Windows and PowerShell.
- **Python 3 available in your terminal.** Confirm that `python --version` reports a Python 3 installation. The bundled script uses the Python standard library; no additional Python packages are required.
- **An OpenRouter account and API key configured in VS Code.** Create a key in your [OpenRouter account settings](https://openrouter.ai/settings/keys), then add OpenRouter through **Chat: Manage Language Models**. Follow the [OpenRouter setup guide for Copilot](https://openrouter.ai/works-with-openrouter/github-copilot).
- **Internet access to OpenRouter.** The skill retrieves the model catalog and health data from `https://openrouter.ai/api/v1`.
- **A local project folder open in VS Code.** Run the skill from that project so any requested Markdown report is saved in the intended location. The synchronization script also needs permission to update your VS Code user configuration and model pinning data.

### Configure OpenRouter before the first sync

Open the Command Palette with `Ctrl+Shift+P`, run **Chat: Manage Language Models**, and add the OpenRouter provider with your API key. Confirm that an OpenRouter model is available in the model selector before running this skill. See [VS Code's model configuration documentation](https://code.visualstudio.com/docs/agent-customization/language-models).

The current script expects an existing `chatLanguageModels.json` configuration and reuses a configured provider's API-key reference. It does not create your OpenRouter account or register a new API key. On Windows, it looks for the standard VS Code user configuration under `%APPDATA%\Code\User\`.

### Optional: Git

Install Git if you plan to use the **Clone with Git** installation method. The **Download ZIP** method does not require Git.

## Support

If you find this skill useful, consider [buying me a ☕](https://buymeacoffee.com/mindseyeproducts).
