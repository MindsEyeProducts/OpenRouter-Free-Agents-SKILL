import assert from "node:assert/strict";
import { cpSync, mkdtempSync, readFileSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import { dirname, join, relative } from "node:path";
import { fileURLToPath } from "node:url";
import test from "node:test";
import { runLint } from "@microsoft/vally";

const root = dirname(dirname(fileURLToPath(import.meta.url)));
const ignored = new Set([
  ".git", "node_modules", ".venv", ".work", ".cleanup-backups",
  ".implementation-staging", ".agents", "__pycache__",
]);

async function assertValidSkill(rootPath) {
  // Match awesome-copilot's default runLint call; an empty discovery is not a pass.
  const result = await runLint({ rootPath });
  assert.equal(result.passed, true, JSON.stringify(result, null, 2));
  assert.equal(result.skillResults.length, 1, "Expected exactly one discoverable skill");
  assert.equal(result.skillResults[0].skill.name, "openrouter-free-agents");
}

test("intake discovers the packaged skill from a checkout named submission", async (t) => {
  const temp = mkdtempSync(join(tmpdir(), "openrouter-intake-"));
  t.after(() => rmSync(temp, { recursive: true, force: true }));
  const submission = join(temp, "submission");
  cpSync(root, submission, {
    recursive: true,
    filter: (source) => !relative(root, source).split(/[/\\]/).some((part) => ignored.has(part)),
  });
  await assertValidSkill(submission);
});

test("the standalone skill validates without files from the repository root", async (t) => {
  const temp = mkdtempSync(join(tmpdir(), "openrouter-standalone-"));
  t.after(() => rmSync(temp, { recursive: true, force: true }));
  const standalone = join(temp, "openrouter-free-agents");
  cpSync(join(root, "skills", "openrouter-free-agents"), standalone, { recursive: true });
  await assertValidSkill(standalone);
});

test("marketplace metadata matches the installable plugin", () => {
  const plugin = JSON.parse(readFileSync(join(root, "plugin.json"), "utf8"));
  const marketplace = JSON.parse(readFileSync(join(root, ".github", "plugin", "marketplace.json"), "utf8"));
  assert.equal(marketplace.plugins.length, 1);
  assert.equal(marketplace.plugins[0].name, plugin.name);
  assert.equal(marketplace.plugins[0].version, plugin.version);
  assert.equal(marketplace.metadata.version, plugin.version);
  assert.equal(marketplace.plugins[0].source, "./");
});
