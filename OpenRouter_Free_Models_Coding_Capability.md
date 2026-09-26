# OpenRouter Free Models: Coding Capability & Health Evaluation

**Generated**: September 26, 2026
**Scope**: Models in VS Code Copilot Chat (`Other Models -> Free OpenRouter`)
**Total Evaluated Models**: 21

---

## 1. Overview & Evaluation Criteria

This document provides a technical evaluation of the active free models available on OpenRouter, assessed for real-world software engineering, code generation, refactoring, agentic tool use (reading/editing files, executing commands, running tests), and **real-time operational health**.

### Evaluation Dimensions
- **Coding Benchmarks & Training**: Dedicated code fine-tuning vs. general-purpose instruct.
- **Operational Health**: Real-time provider availability, 5m and 24h uptime %, and response latency.
- **Tool Calling (`tools`)**: Critical for GitHub Copilot Chat tool use (search, read, edit, terminal execution).
- **Reasoning Architecture**: MoE parameter efficiency, dedicated reasoning tokens, chain-of-thought support.
- **Context Window**: Ability to ingest entire multi-file codebases, logs, and documentation.
- **Latency & Throughput**: Suitability for fast iterative programming vs. deep architectural design.

---

## 2. Tier Summary & Technical Specifications

> **Health Legend**: 🟢 Healthy / High Availability (≥95% uptime) &nbsp;|&nbsp; 🟡 Degraded / Reduced Availability (<95% uptime) &nbsp;|&nbsp; 🔴 Offline / Outage

| Tier | Model | Health | Context | Params (Active / Total) | Tools | Reasoning | Best Use Case |
| :--- | :--- | :---: | :--- | :--- | :---: | :---: | :--- |
| **S** | **Cohere: North Mini Code (free)** | 🟢 | 256K | 3B / 30B (MoE) | Yes | Yes | **Code Generation**: Cohere’s dedicated agentic coding model; high syntactic precision. |
| **S** | **Poolside: Laguna S 2.1 (free)** | 🟢 | 262K | 8B / 118B (MoE) | Yes | Yes | **Primary Coding Agent**: 70.2% on Terminal-Bench 2.1; terminal & refactoring workflows. |
| **S** | **Thinking Machines: Inkling (free)** | 🟢 | 1.05M | 41B / 975B (MoE) | Yes | Configurable | **Frontier Reasoning**: Massive 1M context, system design, and complex algorithmic debugging. |
| **A** | **Google: Gemma 4 31B (free)** | 🟢 | 262K | 30.7B (Dense) | Yes | Yes | **General Engineering**: Dense parameter quality; consistent across Python, TS/JS, Rust, C++. |
| **A** | **NVIDIA: Nemotron 3 Ultra (free)** | 🟢 | 1.00M | 55B / 550B (Hybrid MoE) | Yes | Configurable | **Large-Scale Architecture**: Hybrid Transformer-Mamba; multi-file codebase reasoning. |
| **A** | **Poolside: Laguna XS 2.1 (free)** | 🟢 | 262K | 3B / 33B (MoE) | Yes | Yes | **Low-Latency Coding**: Fast, interactive inline editing and terminal commands. |
| **B** | Dots Studio: Dots3-Note Preview (free) | 🟢 | 512K | 16B / 280B (MoE) | Yes | Yes | **Architecture Notes & Specs**: Technical design documents, API specs, and schemas. |
| **B** | Google: Gemma 4 26B A4B  (free) | 🟢 | 262K | 3.8B / 25.2B (MoE) | Yes | Yes | **Fast Assistant**: Lightweight MoE delivering near-31B quality at higher token throughput. |
| **B** | NVIDIA: Nemotron 3 Super (free) | 🟢 | 262K | 12B / 120B (Hybrid MoE) | Yes | Configurable | **Backend & Scripting**: Hybrid Mamba architecture for structured outputs. |
| **B** | Qwen: Qwen3.8 27B (free) | 🟢 | 262K | N/A | Yes | Yes | Qwen3.8 27B is an open-weight dense vision-language model from Qwen. It is suite |
| **B** | Space Bunny Alpha | 🟢 | 1.00M | N/A | Yes | Yes | Space Bunny Alpha is an anonymous large model with blazing-fast inference, stron |
| **B** | Thinking Machines: Inkling Small (free) | 🟢 | 1.05M | 12B / 276B (MoE) | Yes | Configurable | **Fast Code Review**: High context window for repository audits and PR reviews. |
| **C** | Free Models Router | 🟢 | 200K | Dynamic Router | Yes | Yes | **Fallback**: Automatically balances across available free endpoints when rate-limited. |
| **C** | NVIDIA: Nemotron 3 Nano Omni (free) | 🟡 | 256K | 3B / 30B (MoE) | Yes | Yes | **Visual UI Inspection**: Multimodal input (inspecting mockups, UI bugs, diagrams). |
| **C** | NVIDIA: Nemotron 3.5 Lightning (free) | 🟡 | 1.00M | 3B / 30B (MoE) | Yes | Yes | **High-Throughput Utility**: Lint fixes, boilerplate expansion, and quick file parsing. |
| **N/A** | Google: Lyria 3 Clip Preview | 🟢 | 1.05M | Audio/Music Model | No | No | *Audio synthesis*: Music generation API preview models. |
| **N/A** | Google: Lyria 3 Pro Preview | 🟢 | 1.05M | Audio/Music Model | No | No | *Audio synthesis*: Music generation API preview models. |
| **N/A** | inclusionAI: Ling 3.0 Flash Fin (free) | 🟢 | 262K | 5.1B / 124B (MoE) | Yes | Yes | *Domain specific*: Tuned for financial data/models rather than general programming. |
| **N/A** | inclusionAI: Ling 3.0 Flash Sante (free) | 🟢 | 262K | 5.1B / 124B (MoE) | Yes | Yes | *Domain specific*: Tuned for healthcare/medical terminology. |
| **N/A** | LiquidAI: LFM2.5-2.6B (free) | 🟢 | 65K | 2.6B | Yes | Yes | *Not recommended*: Provider explicitly advises against agentic coding. |
| **N/A** | NVIDIA: Nemotron 3.5 Content Safety (free) | 🟢 | 128K | 4B | No | No | *Guardrail only*: Safety and moderation filter. |

---

## 3. Recommended Models by Use Case

### 1. Daily Coding, Bug Fixing & Refactoring
- **Primary Pick**: `poolside/laguna-s-2.1:free` (**Poolside: Laguna S 2.1**)
  - Built specifically for coding agents, diff generation, and terminal tool calls.
  - Strong benchmark results on Terminal-Bench 2.1 (70.2%).
- **Secondary Pick**: `cohere/north-mini-code:free` (**Cohere: North Mini Code**)
  - Cohere’s specialized agentic coding model with strict syntactic precision and clean documentation generation.

### 2. Complex Architecture, System Design & Large Repositories
- **Primary Pick**: `thinkingmachines/inkling:free` (**Thinking Machines: Inkling**)
  - 41B active parameters / 975B total with a 1,048,576-token context window.
  - Excels at tracing complicated bugs across large workspaces and designing modular architectures.
- **Alternative**: `nvidia/nemotron-3-ultra-550b-a55b:free` (**NVIDIA: Nemotron 3 Ultra**)
  - 55B active parameters; hybrid Transformer-Mamba architecture capable of high-throughput reasoning.

### 3. Fast Interactive Iteration (Low Latency)
- **Primary Pick**: `poolside/laguna-xs-2.1:free` (**Poolside: Laguna XS 2.1**)
  - Activates only 3B parameters per token for near-instant responses on unit test generation and single-function refactoring.
- **Alternative**: `google/gemma-4-26b-a4b-it:free` (**Google: Gemma 4 26B A4B**)
  - 3.8B active parameters; balanced speed and reasoning for quick shell scripts and boilerplate.

### 4. Multimodal UI & Visual Design Work
- **Primary Pick**: `google/gemma-4-31b-it:free` (**Google: Gemma 4 31B**) or `minimax/minimax-m3:free` (**MiniMax M3**)
  - Native image understanding enables inspecting screenshots, wireframes, and design specs to produce matching front-end code (HTML/Tailwind, React, Vue, Flutter).

---

## 4. How to Select Models in VS Code Copilot Chat

1. Open **GitHub Copilot Chat** in VS Code (`Ctrl+Alt+I` or click the Chat icon in the Activity Bar).
2. Click the **Model Selector** dropdown at the bottom of the chat panel.
3. Select your model under **Other Models -> Free OpenRouter** (or under **Pinned Models**).
4. Recommended starting model: **Poolside: Laguna S 2.1 (free)** or **Cohere: North Mini Code (free)**.

---

## 5. Real-Time Model Health & Operational Status

Telemetry pulled directly from OpenRouter endpoint monitoring:

| Model | Upstream Provider | Status | 5m Uptime | 24h Uptime | Latency (TTFT) | 30m Demand |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **Cohere: North Mini Code (free)** | Cohere | 🟢 **Online** | 97.6% | 97.84% | Fast | Dynamic |
| **Poolside: Laguna S 2.1 (free)** | Poolside | 🟢 **Online** | 99.8% | 99.88% | Fast | Dynamic |
| **Thinking Machines: Inkling (free)** | Thinking Machines | 🟢 **Online** | 99.8% | 99.49% | Fast | Dynamic |
| **Google: Gemma 4 31B (free)** | Google AI Studio | 🟢 **Online** | 100.0% | 99.59% | Fast | Dynamic |
| **NVIDIA: Nemotron 3 Ultra (free)** | Nvidia | 🟢 **Online** | 99.0% | 98.40% | Fast | Dynamic |
| **Poolside: Laguna XS 2.1 (free)** | Poolside | 🟢 **Online** | 99.7% | 99.75% | Fast | Dynamic |
| **Dots Studio: Dots3-Note Preview (free)** | AtlasCloud | 🟢 **Online** | 99.8% | 99.91% | Fast | Dynamic |
| **Google: Gemma 4 26B A4B  (free)** | Google AI Studio | 🟢 **Online** | 100.0% | 99.69% | Fast | Dynamic |
| **NVIDIA: Nemotron 3 Super (free)** | Nvidia | 🟢 **Online** | 98.6% | 95.86% | Fast | Dynamic |
| **Qwen: Qwen3.8 27B (free)** | ModelRun | 🟢 **Online** | 100.0% | 97.63% | Fast | Dynamic |
| **Space Bunny Alpha** | Stealth | 🟢 **Online** | 100.0% | 99.91% | Fast | Dynamic |
| **Thinking Machines: Inkling Small (free)** | Thinking Machines | 🟢 **Online** | 100.0% | 99.96% | Fast | Dynamic |
| **Free Models Router** | OpenRouter Gateway | 🟢 **Online** | 100% | 100% | Dynamic | High |
| **NVIDIA: Nemotron 3 Nano Omni (free)** | Nvidia | 🟡 Degraded (-5) | 76.1% | 80.81% | Fast | Dynamic |
| **NVIDIA: Nemotron 3.5 Lightning (free)** | Nvidia | 🟡 Degraded (-2) | 90.6% | 87.10% | Fast | Dynamic |
| **Google: Lyria 3 Clip Preview** | Google AI Studio | 🟢 **Online** | 100% | 100.00% | Fast | Dynamic |
| **Google: Lyria 3 Pro Preview** | Google AI Studio | 🟢 **Online** | 100% | 99.94% | Fast | Dynamic |
| **inclusionAI: Ling 3.0 Flash Fin (free)** | Novita | 🟢 **Online** | 100.0% | 99.99% | Fast | Dynamic |
| **inclusionAI: Ling 3.0 Flash Sante (free)** | Novita | 🟢 **Online** | 100.0% | 100.00% | Fast | Dynamic |
| **LiquidAI: LFM2.5-2.6B (free)** | Liquid | 🟢 **Online** | 100.0% | 99.39% | Fast | Dynamic |
| **NVIDIA: Nemotron 3.5 Content Safety (free)** | Nvidia | 🟢 **Online** | 99.1% | 97.34% | Fast | Dynamic |

