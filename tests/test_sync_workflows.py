"""Exercise the CLI against temporary VS Code files, with API responses mocked."""

import contextlib
import importlib.util
import io
import json
from pathlib import Path
import sqlite3
import sys
import tempfile
import unittest
from unittest.mock import patch


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "sync_openrouter_agents.py"
spec = importlib.util.spec_from_file_location("sync_openrouter_agents", SCRIPT)
sync = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sync)

MODELS = [{
    "id": "example/coder:free", "name": "Example Coder", "description": "Coding model",
    "context_length": 32000, "supports_tools": True, "supports_reasoning": False,
    "architecture": {},
}]
HEALTH = {"example/coder:free": {
    "provider": "Example", "status": "Online", "uptime_5m": "99.0%",
    "uptime_1d": "99.0%", "latency": "Fast", "demand": "10",
}}


class WorkflowTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.config = self.root / "chatLanguageModels.json"
        self.config.write_text('[{"name":"OpenRouter","vendor":"openrouter"}]', encoding="utf-8")
        self.db = self.root / "state.vscdb"
        with contextlib.closing(sqlite3.connect(self.db)) as conn:
            conn.execute("CREATE TABLE ItemTable (key TEXT PRIMARY KEY, value TEXT)")
            conn.commit()
        self.legacy = self.root / ".github" / "agents" / "openrouter-old.agent.md"
        self.legacy.parent.mkdir(parents=True)
        self.legacy.write_text("legacy", encoding="utf-8")
        self.stack = contextlib.ExitStack()
        self.addCleanup(self.stack.close)
        self.stack.enter_context(patch.object(sync.Path, "home", return_value=self.root / "home"))
        self.fetch = self.stack.enter_context(patch.object(sync, "fetch_openrouter_models", return_value=MODELS))
        self.health = self.stack.enter_context(patch.object(sync, "fetch_all_health", return_value=HEALTH))
        self.stack.enter_context(patch.object(sync, "get_default_chat_language_models_path", return_value=self.config))
        self.stack.enter_context(patch.object(sync, "get_default_vscode_state_db", return_value=self.db))
        self.stack.enter_context(patch.object(sync, "get_default_user_prompts_dir", return_value=self.root / "prompts"))

    def run_cli(self, *args):
        output = io.StringIO()
        with patch.object(sys, "argv", [str(SCRIPT), "--workspace-dir", str(self.root), *args]):
            with contextlib.redirect_stdout(output):
                sync.main()
        return output.getvalue()

    def snapshot(self):
        return {str(p.relative_to(self.root)): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}

    def test_combined_sync_and_report_fetch_each_dataset_once(self):
        output = self.run_cli("--tools-only", "--eval-md", "chosen.md")
        self.fetch.assert_called_once_with(tools_only=True)
        self.health.assert_called_once_with(MODELS)
        report = self.root / "chosen.md"
        self.assertIn("Example Coder", report.read_text(encoding="utf-8"))
        self.assertIn("Example Coder", output)
        groups = json.loads(self.config.read_text(encoding="utf-8"))
        self.assertEqual(groups[0]["name"], "Free OpenRouter")
        with contextlib.closing(sqlite3.connect(self.db)) as conn:
            pinned = json.loads(conn.execute("SELECT value FROM ItemTable WHERE key='chatModelPinned'").fetchone()[0])
        self.assertIn("customendpoint/Free OpenRouter/example/coder:free", pinned)
        self.assertFalse(self.legacy.exists())
        self.assertNotIn("(Y/N)", output)
        self.assertLess(output.index("Saved evaluation"), output.index("Developer: Reload Window"))

    def test_evaluate_prints_markdown_without_touching_vscode_or_files(self):
        before = self.snapshot()
        with patch.object(sync, "get_default_chat_language_models_path", side_effect=AssertionError("sync attempted")):
            with patch.object(sync, "cleanup_legacy_agent_files", side_effect=AssertionError("cleanup attempted")):
                output = self.run_cli("--evaluate", "--tools-only")
        self.assertTrue(output.startswith("# OpenRouter Free Models:"))
        self.assertIn("Example Coder", output)
        self.assertNotIn("Developer: Reload Window", output)
        self.assertEqual(before, self.snapshot())
        self.fetch.assert_called_once_with(tools_only=True)
        self.health.assert_called_once_with(MODELS)
        saved = self.root / "saved-preview.md"
        saved.write_text(output, encoding="utf-8")
        self.assertEqual(saved.read_text(encoding="utf-8"), output)
        self.health.assert_called_once()

    def test_dry_run_with_report_changes_no_files_and_skips_health(self):
        before = self.snapshot()
        output = self.run_cli("--dry-run", "--eval-md")
        self.assertEqual(before, self.snapshot())
        self.health.assert_not_called()
        self.assertNotIn("Developer: Reload Window", output)

    def test_sync_includes_model_list_without_health_or_report(self):
        output = self.run_cli()
        self.fetch.assert_called_once()
        self.health.assert_not_called()
        self.assertIn("Example Coder", output)
        self.assertFalse((self.root / "OpenRouter_Free_Models_Coding_Capability.md").exists())

    def test_list_is_read_only(self):
        before = self.snapshot()
        output = self.run_cli("--list")
        self.assertEqual(before, self.snapshot())
        self.assertIn("Example Coder", output)
        self.health.assert_not_called()

    def test_conflicting_modes_fail_before_fetching(self):
        with contextlib.redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit) as raised:
                self.run_cli("--evaluate", "--eval-md")
        self.assertEqual(raised.exception.code, 2)
        self.fetch.assert_not_called()


if __name__ == "__main__":
    unittest.main()
