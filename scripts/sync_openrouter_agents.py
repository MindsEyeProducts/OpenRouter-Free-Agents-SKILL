#!/usr/bin/env python3
"""Compatibility entry point for commands using the old repository script path."""

from pathlib import Path
import runpy


if __name__ == "__main__":
    script = (
        Path(__file__).resolve().parents[1]
        / "skills" / "openrouter-free-agents" / "scripts" / "sync_openrouter_agents.py"
    )
    runpy.run_path(str(script), run_name="__main__")
