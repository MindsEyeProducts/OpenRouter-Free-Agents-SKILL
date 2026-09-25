# OpenRouter API & Free Model Reference

## Overview
OpenRouter (https://openrouter.ai) exposes an OpenAI-compatible interface with a unified model catalog. It provides a variety of community and provider-sponsored free models.

## Free Model Identification
Models on OpenRouter are free when:
1. **Identifier suffix**: The model ID ends with `:free` (e.g. `nvidia/nemotron-3.5-lightning:free`, `cohere/north-mini-code:free`, `openrouter/free`).
2. **Pricing fields**: In the model schema, `pricing.prompt == "0"` and `pricing.completion == "0"`.

## API Endpoint
- **URL**: `GET https://openrouter.ai/api/v1/models`
- **Filtered by tool support**: `GET https://openrouter.ai/api/v1/models?supported_parameters=tools`

### Sample Response Entry
```json
{
  "id": "minimax/minimax-m3:free",
  "name": "MiniMax: MiniMax M3 (free)",
  "description": "MiniMax M3 is a high-capability mixture-of-experts model...",
  "context_length": 1048576,
  "pricing": {
    "prompt": "0",
    "completion": "0"
  },
  "supported_parameters": [
    "tools",
    "reasoning",
    "temperature",
    "top_p"
  ]
}
```

## Free Tier Best Practices
- **Rate Limits**: Free models on OpenRouter typically share rate limits (e.g. 20 requests/minute or 200 requests/day per key, or free IP quota).
- **Fallback / Router**: `openrouter/free` is OpenRouter's dynamic free model router that automatically selects an available free model.
- **Tool Calling**: For GitHub Copilot Chat agents that read/write files or execute commands, prioritize models where `"tools"` is in `supported_parameters`.
