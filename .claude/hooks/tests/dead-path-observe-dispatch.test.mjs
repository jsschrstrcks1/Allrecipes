// dead-path-observe-dispatch.test.mjs — slice of hls-dead-path-hooks-in-9-repos.
// Project-Sophos's PostToolUse('*') hook ran a machine-absolute path
// (/home/user/ken/.claude/hooks/observe-tool-use.sh) that is DEAD on the operator's
// Mac (/home/user does not exist) and silently so. This locks the fix: no hook
// command may carry a machine-absolute path, and the observe hook must route through
// the portable household-hook-dispatch.sh to the ocs-resident observe-tool-use-dispatch.sh
// (which resolves ken fail-loud-not-fatal). Text-invariant on the served config — the
// dispatch's own resolve/exec behavior is covered by open-claw-stuff's
// household-hook-dispatch.test.mjs (#3315).
import { test } from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const SETTINGS = path.resolve(
  path.dirname(fileURLToPath(import.meta.url)), "..", "..", "settings.json",
);

function allCommands() {
  const cfg = JSON.parse(fs.readFileSync(SETTINGS, "utf8"));
  const cmds = [];
  for (const event of Object.values(cfg.hooks || {})) {
    for (const group of event) {
      for (const h of group.hooks || []) {
        if (typeof h.command === "string") cmds.push({ matcher: group.matcher, command: h.command });
      }
    }
  }
  return cmds;
}

test("no hook command carries a machine-absolute path (dead off the authoring machine)", () => {
  const bad = allCommands().filter((c) => /\/(home|Users)\//.test(c.command));
  assert.deepEqual(
    bad, [],
    "machine-absolute paths in hook commands are dead on other machines (UL-173/UL-337): " +
      JSON.stringify(bad),
  );
});

test("the PostToolUse('*') observe hook routes through the dispatch to observe-tool-use-dispatch.sh", () => {
  const observe = allCommands().find((c) => c.matcher === "*");
  assert.ok(observe, "the PostToolUse('*') observation hook must still be wired");
  assert.match(
    observe.command,
    /household-hook-dispatch\.sh observe-tool-use-dispatch\.sh$/,
    "must dispatch the ocs-resident observe-tool-use-dispatch.sh via the portable dispatch",
  );
  assert.match(observe.command, /\$CLAUDE_PROJECT_DIR/, "dispatch path must be project-relative");
});

test("the portable dispatch was actually vendored into this repo and is executable", () => {
  const dispatch = path.resolve(path.dirname(SETTINGS), "hooks", "household-hook-dispatch.sh");
  assert.ok(fs.existsSync(dispatch), "household-hook-dispatch.sh must exist in this repo");
  // #3315 fix present: the resolver must know the operator's ~/ocs-work clone name.
  const body = fs.readFileSync(dispatch, "utf8");
  assert.match(body, /ocs-work/, "the vendored dispatch must be the #3315 version that resolves ~/ocs-work");
});
