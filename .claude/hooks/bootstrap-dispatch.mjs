#!/usr/bin/env node
// @gate name=bootstrap-dispatch plane=harness event=PreToolUse guard and PostToolUse stamp doc=docs/GATE-DOCUMENTATION-AND-ERROR-CODES.md#bootstrap-dispatch-codes
// @gate-code bootstrap-dispatch-denied: a target guard returned status 2 | remedy: read the guard line above this one and satisfy that guard in the named repo
// @gate-code bootstrap-dispatch-undecided: the guard exists and returned neither 0 nor 2 | remedy: repair the named guard so it returns 0 or 2 | override: HOUSEHOLD_BOOTSTRAP_GUARD_BLOCK=0 (operator)
// @gate-code bootstrap-dispatch-unreadable: guard mode could not read or dispatch the request | remedy: send one JSON object on stdin. A fault in this file is repaired here | override: HOUSEHOLD_BOOTSTRAP_GUARD_BLOCK=0 (operator)
// @gate-exit 0: allowed. Unknown mode fails open. Stamp mode never blocks. A missing hook, a status-0 guard, an unrelated worktree that could not load, a restore-only repair, and HOUSEHOLD_BOOTSTRAP_GUARD_BLOCK=0 return and print no denial code. An internal error outside blocking guard mode returns.
// @gate-exit 2: denied. The line prints code=bootstrap-dispatch-denied, code=bootstrap-dispatch-undecided, or code=bootstrap-dispatch-unreadable, and names docs/GATE-REGISTRY.md.
// bootstrap-dispatch.mjs — multi-root workspace dispatcher for the loud-bootstrap hooks.
// Spec: docs/HOUSEHOLD-LOUD-BOOTSTRAP-REQUIREMENT.md v1.2.0 §5.1 (A4 — multi-root deployment).
// HLS: p0-read-order-enforcement-bootstrap-hook-edit-guard-preflight-wi.
//
// WHY: per-repo `.claude/settings.json` hooks only load when Claude Code's project dir IS the
// repo. In multi-root workspaces (remote/web sessions with a parent workspace dir like
// /home/user containing several repos) they never load, so bootstrap-guard, the stamp hook,
// and the dangerous-command guard are silently inert — observed live 2026-07-19: a session
// committed to this repo repeatedly with no stamp root even existing. This dispatcher is
// registered at the USER level (~/.claude/settings.json, via admin/install-bootstrap-dispatch.mjs)
// and delegates each tool event to the canonical hooks of whichever onboarded repo the event
// targets. Delegation, not reimplementation: the per-repo hooks stay the single source of truth.
//
// Modes (argv[2]):
//   guard  — PreToolUse (Edit|Write|NotebookEdit|Bash): delegate to the target repo's
//            bootstrap-guard.mjs; exit 2 propagates (deny).
//   stamp  — PostToolUse (Read|Bash): delegate to the target repo's bootstrap-stamp-hook.mjs;
//            always exits 0 (observation must never block).
//
// Repo resolution:
//   Edit/Write/NotebookEdit/Read → walk up from tool_input.file_path/notebook_path.
//   Bash → absolute paths in the command + event cwd, each walked up. A memory-recall
//   command (repo-agnostic) additionally stamps every onboarded repo found in the
//   workspace (own repo root's parent, one level deep) — recall is session-global.
//   "Onboarded" = the directory contains .claude/hooks/bootstrap-guard.mjs.
//
// NAMED LIMITS (do not paper over — spec §4.1 grade: friction, not proof):
//   - Repos without the bootstrap hooks pass silently (un-onboarded ≠ enforced).
//   - User-level registration is enforced at latest from the next session start; some
//     harnesses load it immediately (observed live 2026-07-20 — plan for the floor).
//   - Fail-open on internal dispatcher error, loudly — a dispatch bug must not brick
//     every session (household precedent: bootstrap-guard, dangerous-command-guard).
import fs from "node:fs";
import path from "node:path";
import { spawnSync } from "node:child_process";
import { fileURLToPath } from "node:url";

const MODE = process.argv[2];
// UL-175: must accept every recall spelling the Sophos skill documents — including
// `memory_evidence.py recall`, the K1 evidence-envelope path, which this regex omitted
// while bootstrap-lib.mjs included it, so multi-root sessions running the DOCUMENTED
// command left memory-recall unstamped (measured live 2026-08-08 and again 2026-08-19).
// Deliberately a local literal, not an import from ./bootstrap-lib.mjs: this dispatcher
// must fail OPEN on its own internal errors and never gain a load-time dependency that
// can brick every tool call. Parity with the lib is pinned by a test instead
// (tests/bootstrap-dispatch.test.mjs "UL-175" cases).
// `['"]?` after `.py` tolerates the quoted script path the SessionStart injection actually prints
// (python3 "/abs/memory_evidence.py" recall ...); without it the canonical printed recall never stamps.
// Kept byte-identical to bootstrap-lib.mjs RECALL_CMD_RE (pinned by bootstrap-dispatch.test.mjs).
const RECALL_CMD_RE = /(memory_ops\.py['"]?\s+recall|recall-memory\.mjs|memory_evidence\.py['"]?\s+recall)/;
const OWN_REPO_ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..", "..");

// TOOL-NAME ALIASES. Kept LOCAL rather than imported, for the same reason RECALL_CMD_RE above is
// (header: this dispatcher must fail OPEN on its own internal errors, and must never gain a
// load-time dependency that can brick every tool call). Parity with bootstrap-lib.mjs TOOL_ALIASES
// is pinned by a test instead (tests/bootstrap-dispatch.test.mjs), so the two cannot drift silently
// — which is exactly how the gap below opened.
//
// MEASURED 2026-10-03: without this, the branch in targetsFor() compared the RAW tool name against
// Claude names only. Hermes sends read_file / write_file / patch / terminal, so no branch matched,
// targetsFor() returned [], and the dispatcher **stamped nothing in stamp mode and exited 0 (ALLOW)
// in guard mode** — a registered, allowlisted, `hermes hooks doctor`-clean gate that permitted every
// mutation it was installed to deny. bootstrap-lib.mjs had the alias table all along; the delegator
// understood Hermes and the delegate did not.
export const TOOL_ALIASES = {
  read: "Read",
  read_file: "Read",
  bash: "Bash",
  run_terminal_command: "Bash",
  shell: "Bash",
  edit: "Edit",
  write: "Write",
  multiedit: "Edit",
  search_replace: "Edit",
  notebookedit: "NotebookEdit",
  notebook_edit: "NotebookEdit",
  // Hermes (skynet2) tool names.
  terminal: "Bash",
  write_file: "Write",
  patch: "Edit",
  edit_file: "Edit",
  skill_view: "SkillView",
};

/** Canonical tool name for the branches below; an unknown name passes through unchanged. */
export function canonTool(name) {
  const raw = String(name ?? "");
  return TOOL_ALIASES[raw.toLowerCase()] || raw;
}

// Home-relative for readability in denial messages. Deliberately local rather than imported: this
// dispatcher must fail OPEN on its own errors and never gain a load-time dependency (see header).
function shortPath(p) {
  const home = process.env.HOME || "";
  return home && String(p).startsWith(home + path.sep) ? "~" + String(p).slice(home.length) : String(p);
}

function isOnboarded(dir) {
  try { return fs.existsSync(path.join(dir, ".claude", "hooks", "bootstrap-guard.mjs")); }
  catch { return false; }
}

// Walk up from p to the nearest onboarded repo root (bounded by filesystem root).
function repoRootFor(p) {
  let dir = path.resolve(String(p || ""));
  try { if (fs.statSync(dir).isFile()) dir = path.dirname(dir); } catch { dir = path.dirname(dir); }
  for (let i = 0; i < 40; i++) {
    if (isOnboarded(dir)) return dir;
    const parent = path.dirname(dir);
    if (parent === dir) return null;
    dir = parent;
  }
  return null;
}

// Onboarded repos that are siblings of (or are) this clone — the workspace set for
// repo-agnostic events like memory recall. Bounded: one directory level.
function workspaceRepos() {
  const found = new Set();
  if (isOnboarded(OWN_REPO_ROOT)) found.add(OWN_REPO_ROOT);
  const wsRoot = path.dirname(OWN_REPO_ROOT);
  let entries = [];
  try { entries = fs.readdirSync(wsRoot, { withFileTypes: true }); } catch { /* bounded scan only */ }
  for (const e of entries) {
    if (!e.isDirectory()) continue;
    const d = path.join(wsRoot, e.name);
    if (isOnboarded(d)) found.add(d);
  }
  return [...found];
}

// SHELL-VARIABLE TARGETS (HLS bootstrap-dispatch-blind-to-shell-variable-targets, measured
// 2026-09-08). Targets were read from LITERAL paths only, so a loop such as
//     for r in ken Romans; do git -C /home/user/$r commit ...; done
// named no repository: the path regex stopped at `$` and matched only the parent directory. Only
// the cwd repo's guard ran, and fourteen leaf commits went through unexamined while the same commit
// with a literal path was denied. This expands, conservatively and from the command text alone:
//   - `for VAR in w1 w2 ...;` loop lists (the measured shape), each word literal
//   - literal assignments in the same command: `VAR=/x`, `export VAR=/x`, `VAR="/x"`
//   - $HOME, ${HOME} and a leading `~` from the environment
// A token whose variables cannot all be resolved is left alone. NAMED LIMIT: it is not denied,
// because this household's own scripted commands use run-time variables (`git -C $S/x push`) and a
// deny on every one would refuse ordinary work; whether to fail closed there is an operator call.
// Words that contain `$`, a backtick, a glob or a command substitution are never used as values.
const unquoteWord = (w) => String(w || "").replace(/^(['"])(.*)\1$/, "$2");
const literalWord = (w) => !!w && !/[$`*?[\]{}()<>|;&\s]/.test(w);

/** Variables the command text itself defines: loop lists, literal assignments, and HOME. */
export function shellVars(cmd, env = process.env) {
  const text = String(cmd || "");
  const vars = new Map();                     // name -> [values]
  const add = (k, vs) => vars.set(k, [...(vars.get(k) || []), ...vs]);
  for (const m of text.matchAll(/\bfor\s+([A-Za-z_]\w*)\s+in\s+([^;\n]+?)\s*;\s*do\b/g)) {
    const words = m[2].trim().split(/\s+/).map(unquoteWord).filter(literalWord);
    if (words.length) add(m[1], words);
  }
  for (const m of text.matchAll(/(?:^|[;&|\n]\s*|\bexport\s+)([A-Za-z_]\w*)=("[^"$`]*"|'[^']*'|[^\s;&|$`'"()<>]+)/g)) {
    add(m[1], [unquoteWord(m[2])]);
  }
  if (env.HOME && !vars.has("HOME")) vars.set("HOME", [env.HOME]);
  return vars;
}

/** Every concrete string a token can stand for; [] when any variable in it is unresolvable. */
export function expandToken(token, vars, env = process.env) {
  let tok = unquoteWord(String(token || "").replace(/^["']|["']$/g, ""));
  if (tok.startsWith("~/") && env.HOME) tok = env.HOME + tok.slice(1);
  if (!tok.includes("$")) return [tok];
  let expansions = [tok];
  for (const vm of tok.matchAll(/\$\{([A-Za-z_]\w*)\}|\$([A-Za-z_]\w*)/g)) {
    const values = vars.get(vm[1] || vm[2]);
    if (!values) return [];
    const next = [];
    for (const e of expansions) for (const v of values) next.push(e.split(vm[0]).join(v));
    expansions = next.slice(0, 64);           // bounded: a pathological list cannot fan out forever
  }
  return expansions.filter((e) => !e.includes("$"));
}

/** Absolute paths the command reaches through a variable or `~` (the literal scan misses these). */
export function expandShellTokens(cmd, env = process.env) {
  const vars = shellVars(cmd, env);
  const out = new Set();
  for (const raw of String(cmd || "").split(/[\s;&|()<>]+/)) {
    if (!raw.includes("$") && !raw.replace(/^["']/, "").startsWith("~")) continue;
    for (const e of expandToken(raw, vars, env)) if (e.startsWith("/")) out.add(e);
  }
  return [...out];
}

function targetsFor(input) {
  const tool = canonTool(input.tool_name);
  const targets = new Set();
  if (tool === "Edit" || tool === "Write" || tool === "NotebookEdit" || tool === "Read") {
    // Hermes sends the target as `path` (write_file/patch/read_file), not `file_path`.
    // Without this the dispatcher cannot resolve the repo root for a Hermes mutation
    // and silently allows it — the exact "registered but inert" gap HERMES.md warns about.
    const fp = input.tool_input?.file_path || input.tool_input?.notebook_path || input.tool_input?.path || "";
    const root = fp ? repoRootFor(fp) : null;
    if (root) targets.add(root);
  } else if (tool === "Bash") {
    const cmd = String(input.tool_input?.command || "");
    for (const m of cmd.match(/\/[A-Za-z0-9_@%+=:,.~/-]+/g) || []) {
      const root = repoRootFor(m);
      if (root) targets.add(root);
    }
    // Paths reached through a loop variable, a same-command assignment, $HOME or `~`.
    for (const p of expandShellTokens(cmd, process.env)) {
      const root = repoRootFor(p);
      if (root) targets.add(root);
    }
    const shellVarMap = shellVars(cmd, process.env);
    // Relative `cd x`/`git -C x` targets resolve against the event cwd — without this,
    // `cd open-claw-stuff && git commit` from the workspace root evades attribution
    // (cwd walks UP, never down; landed self-attack probe, closed before ship).
    // UL-1018 (B): repoRoot must not come ONLY from input.cwd — a well-formed payload lacking cwd
    // resolved nothing and the gate guarded NOTHING, exiting 0 silently. Fall back to the process cwd
    // (where the dispatcher was invoked), so a mutation run from inside an onboarded repo is caught
    // even when the harness omits cwd. Silence is the defect: "measured nothing" != "nothing to guard".
    const cwd = input.cwd || process.cwd();
    if (cwd) {
      for (const m of cmd.matchAll(/(?:\bcd|\s-C)\s+([^\s;&|)]+)/g)) {
        const raw = m[1].replace(/^['"]|['"]$/g, "");
        // A variable here (`cd $r`, `git -C $base/$r`) expands through the same map; a relative
        // result resolves against cwd exactly like a literal one.
        for (const tok of raw.includes("$") ? expandToken(raw, shellVarMap, process.env) : [raw]) {
          if (tok.startsWith("/") || tok.startsWith("-")) continue;
          const root = repoRootFor(path.resolve(String(cwd), tok));
          if (root) targets.add(root);
        }
      }
      const root = repoRootFor(cwd);
      if (root) targets.add(root);
    }
    if (MODE === "stamp" && RECALL_CMD_RE.test(cmd)) {
      for (const r of workspaceRepos()) targets.add(r);
    }
  }
  return [...targets];
}

// #3373: the worktree a command actually RUNS IN (Bash: its cwd; Edit/Write: the file's repo).
// The load-failure denial is scoped to THIS tree so one conflicted bootstrap-lib.mjs in an
// unrelated worktree cannot deny work in every other worktree (measured 2026-09-06: it denied
// a bare echo in an unrelated tree, and blocked its own repair).
function primaryWorktreeFor(input) {
  const tool = canonTool(input.tool_name);
  if (tool === "Edit" || tool === "Write" || tool === "NotebookEdit") {
    const fp = input.tool_input?.file_path || input.tool_input?.notebook_path || "";
    return fp ? repoRootFor(fp) : null;
  }
  if (tool === "Bash") return repoRootFor(input.cwd || process.cwd());
  return null;
}

// #3373(b): the ONLY commands permitted through a load-wedged guard — they revert a worktree
// to a committed state and so cannot introduce an unstamped change. Deliberately tight: a bare
// repair command with NO shell chaining/redirection/substitution, so a repair prefix cannot
// smuggle a mutation (e.g. `git merge --abort && <anything>` is refused).
const REPAIR_RESTORE_RE = /^\s*git\s+(?:merge|rebase)\s+--abort\s*$|^\s*git\s+checkout\s+--\s+\S|^\s*git\s+restore\s+\S/;
function isRepairRestoreCommand(cmd) {
  const c = String(cmd || "");
  if (/[;&|`\n]|\$\(|<\(|>\s|>>/.test(c)) return false; // no chaining, redirection, or substitution
  return REPAIR_RESTORE_RE.test(c);
}

try {
  if (MODE !== "guard" && MODE !== "stamp") {
    // bootstrap-dispatch-unknown-mode-fails-open: a misconfigured settings.json hook line (one
    // wrong or dropped mode word) must NOT turn the P0 mutation gate into a printed warning with
    // exit 0. Fails CLOSED (exit 2, deny, loud) so a wedged dispatch is caught, not silently
    // allowed. Same present-is-not-runnable class as UL-888/UL-1016; candidate fix from the task.
    console.error(`bootstrap-dispatch: unknown mode '${MODE ?? ""}' (want guard|stamp), failing CLOSED`);
    process.exit(2);
  }
  const raw = fs.readFileSync(0, "utf8");
  const input = JSON.parse(raw);
  const hookFile = MODE === "guard" ? "bootstrap-guard.mjs" : "bootstrap-stamp-hook.mjs";

  const targets = targetsFor(input);

  for (const repoRoot of targets) {
    const hook = path.join(repoRoot, ".claude", "hooks", hookFile);
    if (!fs.existsSync(hook)) continue;
    const r = spawnSync("node", [hook], { input: raw, encoding: "utf8" });
    // Finding 5 (2026-09-18): this used to write every target's stderr RAW, so a warning from one
    // repo and the denial from another arrived as one undifferentiated block with no way to tell
    // them apart. Measured cost: an evening spent re-reading posture layers because the surfaced
    // message was a read-order complaint from one repo while the real blocker was a liveness
    // failure in a different one. Tag each line with the repo that said it.
    if (r.stderr) process.stderr.write(r.stderr.replace(/^(?!$)/gm, `[${path.basename(repoRoot)}] `));
    if (MODE !== "guard") continue;      // stamp mode: observation must never block
    if (r.status === 2) {
      // Attribute the denial. The verdict is unchanged (first denial still wins and still denies);
      // what changes is that the operator can now tell WHICH repo denied, and what else was in play
      // but never consulted. A denial nobody can attribute sends people to fix the wrong repo.
      console.error(
        `⛔ BOOTSTRAP DISPATCH: the denial above came from ${repoRoot} code=bootstrap-dispatch-denied Key: docs/GATE-REGISTRY.md\n` +
        `  guard:    ${hook}\n` +
        `  targets:  ${targets.map(shortPath).join(", ") || "(none)"}\n` +
        `  note:     first denial wins, so any target after this one was NOT consulted. If the\n` +
        `            message above names a remedy, run it in THAT repo, not in your cwd.`,
      );
      process.exit(2);
    }
    if (r.status === 0) continue;        // explicit allow

    // UL-1016: the guard EXISTS but could not RENDER A DECISION — uncaught throw, syntax
    // error, spawn failure, killing signal, any exit outside {0,2}. bootstrap-guard.mjs
    // exits only 0 or 2 by construction, so anything else means it did not get to decide.
    // Before this, only `status === 2` denied, so every such outcome fell through to the
    // loop's exit(0) and the mutation was ALLOWED — while isOnboarded() (a file-existence
    // test) still reported the repo as enforced. That is the household's "present is not
    // runnable" class (UL-888) sitting on the P0 mutation gate: onboarding measured
    // EXISTENCE where enforcement needs a DECISION. Measured 2026-08-23 with an inert
    // differential probe: guard exits 2 -> DENY (control); guard throws -> ALLOW; guard is
    // a syntax error -> ALLOW. (A guard writing 2MB to stdout then exiting 2 still DENIED,
    // so this is deliberately NOT a maxBuffer/ENOBUFS fix — that hypothesis was tested and
    // failed, and no maxBuffer is added here.)
    //
    // "Could not look" is UNAVAILABLE, never CLEAN. Deny, loudly and attributably.
    // The operator keeps the key at THIS level on purpose: a guard that has crashed cannot
    // honour its own HOUSEHOLD_BOOTSTRAP_GUARD_BLOCK, so the dispatcher honours it instead
    // — otherwise this fix would be a brick with no way out.
    const why = r.error
      ? `spawn failed: ${r.error.message}`
      : r.signal
        ? `killed by signal ${r.signal}`
        : `exit ${r.status}`;
    // #3373(a): a guard that could not LOAD in an UNRELATED worktree must not deny a command
    // whose own worktree is healthy. Scope the load-failure denial to the invoking worktree;
    // a broken tree's guard being down is that tree's problem, not this command's. (A guard
    // that LOADED and DECIDED deny — status 2 above — still wins for any target, unchanged.)
    const primary = primaryWorktreeFor(input);
    if (primary && path.resolve(repoRoot) !== path.resolve(primary)) {
      console.error(`bootstrap-dispatch: guard for ${repoRoot} could not load (${why}); it is not the invoking worktree (${primary}), so not denying this command on account of an unrelated broken tree (#3373).`);
      continue;
    }
    // #3373(b): when the INVOKING worktree's own guard cannot LOAD, permit ONLY a restore-only
    // repair command so the guard cannot block its own repair. Anything else stays denied below.
    if (canonTool(input.tool_name) === "Bash" && isRepairRestoreCommand(input.tool_input?.command)) {
      console.error(`bootstrap-dispatch: guard for ${repoRoot} could not load (${why}); permitting the restore-only repair command so the wedge can be undone (#3373). This cannot introduce an unstamped change.`);
      process.exit(0);
    }
    if (process.env.HOUSEHOLD_BOOTSTRAP_GUARD_BLOCK === "0") {
      console.error(`bootstrap-dispatch: guard for ${repoRoot} could not render a decision (${why}) — WARN-ONLY per HOUSEHOLD_BOOTSTRAP_GUARD_BLOCK=0; ALLOWING.`);
      continue;
    }
    console.error(
      `⛔ BOOTSTRAP DISPATCH: the guard for ${repoRoot} could not render a decision (${why}). code=bootstrap-dispatch-undecided Key: docs/GATE-REGISTRY.md\n` +
      `A guard that cannot RUN is UNAVAILABLE, not CLEAN — denying rather than silently allowing this mutation.\n` +
      `  guard: ${hook}\n` +
      `Repair the guard, or set HOUSEHOLD_BOOTSTRAP_GUARD_BLOCK=0 for warn-only (operator switch, not an agent's).`
    );
    process.exit(2);
  }
  process.exit(0);
} catch (e) {
  const why = e?.message || e;
  if (MODE === "guard" && process.env.HOUSEHOLD_BOOTSTRAP_GUARD_BLOCK !== "0") {
    console.error(
      `⛔ BOOTSTRAP DISPATCH: internal error in GUARD mode (${why}) — the mutation gate cannot read or ` +
      `dispatch this request, so it cannot confirm the mutation is safe. DENYING (fail-closed, UL-1018). code=bootstrap-dispatch-unreadable Key: docs/GATE-REGISTRY.md\n` +
      `  Malformed stdin or a dispatcher fault must not become permission to proceed.\n` +
      `  Set HOUSEHOLD_BOOTSTRAP_GUARD_BLOCK=0 for warn-only (operator switch, not an agent's).`,
    );
    process.exit(2);
  }
  console.error(
    `bootstrap-dispatch: internal error (${why}) — ` +
    (MODE === "guard" ? "WARN-ONLY per HOUSEHOLD_BOOTSTRAP_GUARD_BLOCK=0, ALLOWING" : "stamp observation lost, exit 0") + ".",
  );
  process.exit(0);
}
