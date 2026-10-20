// bootstrap-lib.mjs — shared loud-bootstrap stamp + guard logic.
// Spec: docs/HOUSEHOLD-LOUD-BOOTSTRAP-REQUIREMENT.md v1.2.0 (R1–R3).
// HLS: loud-bootstrap-impl-claude-code · loud-bootstrap-impl-grok
//
// Dual-runtime: Claude Code (snake_case tools) + Grok (camelCase tools).
// Tamper-evidence grade: FRICTION, not proof (named limit, spec §4.1).
//
// SUPERSET NOTE (2026-09-25): union-merged from open-claw-stuff canonical (this file's base — it had
// grown a staleness/TTL layer, a quoted-path-tolerant RECALL_CMD_RE, and a latest-wins merge fix that
// Project-Sophos's copy lacked) plus two real, non-conflicting Project-Sophos additions this base
// lacked: `skillPathForThisRepo` (a leaf repo's `.claude/skills` layout resolves layer paths that a
// bare `skills/` prefix cannot see there) and a per-repository Codex stamp root (`~/.codex/household-
// bootstrap/<repo>`, matching Codex's own writer). Every other export was identical on both sides.
import fs from "node:fs";
import path from "node:path";
import os from "node:os";
import crypto from "node:crypto";
import { fileURLToPath } from "node:url";

/** Repo that contains this hooks tree (open-claw-stuff / ocs-work clone). */
export const HOOK_FILE_REPO_ROOT = path.resolve(
  path.dirname(fileURLToPath(import.meta.url)),
  "..",
  "..",
);
/** @deprecated Prefer getRepoRoot(input) — kept for Claude test compatibility. */
export const REPO_ROOT = HOOK_FILE_REPO_ROOT;
export const REPO_NAME = path.basename(HOOK_FILE_REPO_ROOT);

// Layer keys → canonical file suffix (read-observed). memory-recall is
// command-observed (spec §4.1 per-layer observation table).
export const LAYER_SUFFIXES = {
  "soli-deo-gloria": "skills/soli-deo-gloria/SKILL.md",
  "careful-not-clever": "skills/careful-not-clever/SKILL.md",
  "sophos": "skills/sophos/SKILL.md",
  "sophos-os": "docs/SOPHOS-OPERATING-SYSTEM.md",
  "household-rulebook": "docs/HOUSEHOLD-AGENT-RULEBOOK.md",
  "household-library": "skills/household-library/SKILL.md",
};
// The `['"]?` after `.py` is load-bearing: the household's OWN SessionStart injection prints the
// recall command with the script path in DOUBLE QUOTES (python3 "/abs/memory_evidence.py" recall ...),
// so the closing quote sits between `.py` and the whitespace. Without tolerating it, the canonical
// printed command never stamps, an agent runs recall verbatim and is still denied every mutation for
// the whole session (measured 2026-09-05, cost ~15 turns; the same class as the cat/sed read-credit
// gap). Optional, and single- or double-quote, so both the quoted and the bare forms credit; `encode`
// still cannot match, because `recall` must follow.
export const RECALL_CMD_RE =
  /(memory_ops\.py['"]?\s+recall|recall-memory\.mjs|memory_evidence\.py['"]?\s+recall)/;

// A recall that CREDITS layer 5 must be a GENUINE recall, not a ritual: the command has to invoke a
// recall tool AND carry a non-empty task query. An empty `recall ""` or a bare `recall-memory.mjs` with
// no task is a checkbox, not the continuity layer, and it must not earn credit. This closes the shortcut
// where an agent runs the recall command for the sake of the stamp without recalling anything for the
// actual task. Same posture as the ledger: watch the behavior, not the shape of the command.
// The same optional quote after `.py` as RECALL_CMD_RE (#3476): a quoted script path is still a genuine recall.
export function isGenuineRecall(command) {
  const s = String(command || "");
  if (!RECALL_CMD_RE.test(s)) return false;
  // EXECUTION, not text (adversarial analysis 2026-10-11, lane A S19): `cat CLAUDE.md | grep
  // 'memory_evidence.py recall foo'` used to credit the continuity layer. The recall must be the
  // program a segment starts: `python3 <…>memory_evidence.py recall <query>` (or memory_ops.py), or
  // `node <…>recall-memory.mjs` fed a {"task": …} by the segment before it.
  let pyQuery = false;
  let mjsRun = false;
  for (const seg of commandSegments(s)) {
    const { head, args } = segmentHead(seg);
    const a0 = args[0] || "";
    if ((head === "python3" || head === "python") && /(?:memory_ops|memory_evidence)\.py$/.test(a0) && args[1] === "recall") {
      const q = (args[2] || "").replace(/^["']/, "");
      if (/^[A-Za-z0-9]/.test(q)) pyQuery = true;
    }
    if ((head === "node" || head === "nodejs") && a0.endsWith("recall-memory.mjs")) mjsRun = true;
    if (/(?:memory_ops|memory_evidence)\.py$/.test(head) && a0 === "recall" && /^[A-Za-z0-9]/.test((args[1] || "").replace(/^["']/, ""))) pyQuery = true;
    if (head === "recall-memory.mjs") mjsRun = true;
  }
  const mjsTask = mjsRun && /"task"\s*:\s*"[A-Za-z0-9][^"]*"/.test(s);
  return pyQuery || mjsTask;
}
export const ALL_LAYERS = [...Object.keys(LAYER_SUFFIXES), "memory-recall"];

// The Hermes front-door skill. A Hermes session in a household repo MUST load this
// skill (via skill_view) before any mutation — it is the procedure that prevents the
// improvise-and-stall failure (measured 2026-10-17: a Hermes session misread its own
// system prompt as an injection and refused to bootstrap, never loading the skill).
// Belt 2 of the belt-and-suspenders pair: the Hermes plugin (belt 1) injects "load
// sophos-household first" and forwards the skill_view observation; this guard (belt 2)
// ENFORCES that the skill was actually loaded before allowing a Hermes mutation.
// Scoped to the Hermes runtime only — Claude/Grok/Codex load layers via file paths
// and are unaffected.
export const FRONT_DOOR_SKILL = "sophos-household";

// ── One house, one manifest, per-runtime read surface (measured 2026-09-12) ─────────────────────
// The house had TWO definitions of "the bootstrap is complete": this canonical set, and a second,
// longer list living inside the codex adapter. Two lanes disagreeing on what complete means is a
// governance defect, not a style difference: a session can satisfy one definition and fail the other
// while both report a completed bootstrap.
//
// The fix is not to pick a winner. The canonical seven ARE the layer set — what complete means in
// every runtime. A runtime may require MORE reads for its own read surface (codex has no trustworthy
// Read event and must read through Bash, so it names more components). Those extras are declared HERE,
// in data, with their paths, so the difference is visible and shared rather than accidental and buried
// in an adapter. Codex's extras stay exactly as strict as they were.
export const RUNTIME_EXTRA_LAYERS = {
  codex: {
    "sophos-kernel": "atlas/server/sophos.mjs",
    "hard-safety": "skills/destructive-command-safety/SKILL.md",
    "faithful-stewardship": "skills/faithful-stewardship/SKILL.md",
    "ken-voice": "skills/ken-voice/SKILL.md",
    "skynet-voice": "skills/skynet-voice/SKILL.md",
  },
};

// SUPERSET NOTE (2026-09-25, from Project-Sophos): a leaf repo vendors its synced skills beneath
// `.claude/skills` (the leaf-repo layout HOUSEHOLD_MARKERS itself names below), while the
// open-claw-stuff source tree keeps them beneath `skills`. The layer KEYS are household-wide, but a
// path is evidence only when it names a file that actually exists in the repo whose runtime is being
// governed. A fixed `skills/` prefix made Project-Sophos's own Codex contract mechanically impossible
// to satisfy (#114) — every extra layer read was credited against a path that could never exist there.
function skillPathForThisRepo(suffix) {
  const projectCopy = path.join(HOOK_FILE_REPO_ROOT, ".claude", suffix);
  if (suffix.startsWith("skills/") && fs.existsSync(projectCopy)) {
    return `.claude/${suffix}`;
  }
  return suffix;
}

/** Everything a runtime must read before a mutation: canonical layers, then its declared extras. */
export function requiredLayerPaths(runtime) {
  const extras = RUNTIME_EXTRA_LAYERS[String(runtime || "").toLowerCase()] || {};
  return Object.fromEntries(
    Object.entries({ ...LAYER_SUFFIXES, ...extras }).map(([key, suffix]) => [key, skillPathForThisRepo(suffix)]),
  );
}

/** Every layer NAME a runtime must carry, canonical set first. */
export function requiredLayers(runtime) {
  const extras = Object.keys(RUNTIME_EXTRA_LAYERS[String(runtime || "").toLowerCase()] || {});
  return [...ALL_LAYERS, ...extras];
}

// A Bash READ of one or more Layer 0/1 files credits each of them, mirroring RECALL_CMD_RE
// for recall. Closes the gap where an agent reading the layers via `cat`/`sed`/`head` — which
// "auto mode" actively instructs — got NO credit and was falsely denied every mutation for the
// whole session (measured live 2026-09-05, cost ~15 turns; HLS #3317). A read VERB is REQUIRED,
// so a mere mention (`echo path`), a delete (`rm path`), or a move (`mv path`) of a layer path
// is never miscredited as a read. The credit is no weaker than the Read tool's: both mean "the
// layer content was accessed", and neither can prove the agent absorbed it.
export const LAYER_READ_VERB_RE =
  /(?:^|[;&|]\s*|\s|\()(?:cat|bat|less|more|view|nl|od|xxd|sed|head|tail)\b/;
// ── Red-team findings 6-8, 11 (closed 2026-09-12) ───────────────────────────────
// The first cut of R1/R2 credited TEXT, not EXECUTION: `echo cat <layer path>` credited the layer,
// `/tmp/.../fake/skills/sophos/SKILL.md` credited it from outside the repo, and `echo "node
// admin/library.mjs claim-patron"` credited the checklist step. Every one was a substring match.
// Two rules close that family: a credit path must resolve INSIDE the household (or a named install
// home), and a printed/echoed string is never an execution.
function pathWithinAllowed(p, repoRoot) {
  if (!repoRoot) return true; // containment is enforced only when the caller names the root
  const home = os.homedir();
  const roots = [repoRoot, path.join(home, ".hermes", "skills"), path.join(home, ".grok", "skills")];
  const raw = String(p || "");
  // A relative path in a hook payload is relative to the session's repo (the runtime's cwd); an
  // absolute path must still resolve inside an allowed root. Both are contained; a decoy on disk is not.
  const a = raw
    ? path.isAbsolute(raw)
      ? path.resolve(raw)
      : path.resolve(repoRoot, raw)
    : "";
  if (!a) return false;
  // A leaf session may legitimately read the CANONICAL layer from the hub (spec §4.1: the canonical
  // file or its registered repo-local sync copy), so a path inside another household repo counts.
  //
  // BUT THE MARKER TEST IS CIRCULAR AND CANNOT STAND ALONE (measured 2026-09-18). HOUSEHOLD_MARKERS
  // includes `skills/sophos/SKILL.md` and `docs/SOPHOS-OPERATING-SYSTEM.md` — the very files a credit
  // path points at. So `mkdir -p /tmp/decoy/skills/sophos && echo x > .../SKILL.md` makes /tmp/decoy
  // a "household repo" BY THE ACT OF PLANTING THE DECOY, containment passes, and `cat` of that file
  // credits the sophos layer to a session that never opened the real doctrine. Six such files mint a
  // whole posture on any writable path. This hits the Read tool too, not only Bash.
  //
  // A real household repo is a CHECKOUT. Requiring .git does not make forgery impossible (an agent
  // that can mkdir can also `git init`), and that residual is named here rather than hidden: the
  // durable fix is an allowlist of known roots the candidate path cannot contribute to. What this
  // does buy is that the cheap attack — an ordinary directory — no longer authenticates itself.
  // Walk for an ancestor that is BOTH a household repo AND a checkout. walkHouseholdRoot alone
  // returns the FIRST marker-bearing ancestor, which in the leaf layout is the `.claude` directory
  // itself (it holds skills/sophos/SKILL.md), and that is not where .git lives. Checking only that
  // first hit rejected an honest cross-repo read of Project-Sophos, so this checks each level.
  // THE ALLOWLIST THE NOTE ABOVE PROMISED (adversarial analysis 2026-10-11, lane A S2/S8/S17): a
  // scratch directory with seven planted files and `git init` passed the marker-plus-checkout test
  // and credited sophos, the pointer and the OS doc to a session that never opened the real doctrine.
  // A household checkout is not anywhere a `.git` can be made; it lives BESIDE the other household
  // checkouts. So a candidate root must also sit under a known household PARENT: the parent of the
  // repo being governed, the parent of this hook's own repo, the parent of $HOUSEHOLD_OCS_ROOT, or
  // the home directory (where ~/Project-Sophos and the leaf installs live). /tmp is none of these.
  // Residual, named: an agent that can write a sibling directory under one of those parents can still
  // plant a decoy there; that requires write access beside the real repos, not merely to /tmp.
  const parents = householdParents(repoRoot);
  let cur = path.dirname(a);
  for (let i = 0; i < 10; i++) {
    if (isHouseholdRepo(cur) && fs.existsSync(path.join(cur, ".git")) && parents.has(path.dirname(path.resolve(cur)))) return true;
    const parent = path.dirname(cur);
    if (parent === cur) break;
    cur = parent;
  }
  return roots.some((r) => {
    const rr = path.resolve(r);
    return a === rr || a.startsWith(rr + path.sep);
  });
}

/** Directories a household checkout may be a child of. Explicit roots count; scratch parents do not. */
export function householdParents(repoRoot) {
  const set = new Set();
  const add = (p) => { if (p) { try { set.add(path.dirname(fs.realpathSync(path.resolve(p)))); } catch { set.add(path.dirname(path.resolve(p))); } } };
  add(repoRoot);
  add(HOOK_FILE_REPO_ROOT);
  add(process.env.HOUSEHOLD_OCS_ROOT);
  set.add(os.homedir());
  // The documented household locations (the pointers' `<OCS>` fallback hints and the cluster's
  // checkout root). A leaf whose hook copy runs far from the hub (a scratch leaf reading the real
  // canonical layers, #3077) must still be allowed to credit a read of the real hub. Declared, not
  // discovered: a parent earns a place here by being written in the pointers, never by existing.
  for (const hint of ["/workspace", "/home/user", "/agent/repos"]) {
    try { if (fs.statSync(hint).isDirectory()) set.add(fs.realpathSync(hint)); } catch { /* not this machine */ }
  }
  return set;
}

// ── Credit means EXECUTION, judged per shell segment (adversarial analysis 2026-10-11, finding 2) ──
// Every credit path below used to be a regex over the WHOLE command text. Lane A minted three of the
// four checklist steps and the continuity layer with `printf '%s' 'node admin/library.mjs
// claim-patron'`, `grep 'library.mjs claim-patron' CLAUDE.md`, `ls .claude/hooks/memory-directives-
// inject.sh` and `cat CLAUDE.md | grep 'memory_evidence.py recall'`, and a leading `echo "== claim"`
// in a compound command DROPPED a real run (the deadlock the lead met at 13:13). The whole-text
// matcher could not tell which program the shell would actually start. So the command is now split
// into segments (`;`, `&&`, `||`, `|`, `&`, newline, braces, parentheses), heredoc BODIES are removed
// first (they are data), and each segment is reduced to the program the shell starts: leading
// `NAME=value` assignments and wrappers (`command`, `sudo`, `env`, `nice`, `time`, `timeout N`, …) are
// skipped, a path prefix is dropped. A credit is granted only by a segment whose HEAD is the crediting
// program: a read verb for a layer, `node … library.mjs <verb>` for a step, `bash … inject.sh`,
// `python3 … memory_evidence.py directives|recall`. `grep`, `ls`, `printf`, `echo` and heredoc text
// can no longer mint anything, whatever they contain.
//
// Named limit: `bash -c 'cat <layer>'` and `eval` hand their string to a child shell this parser does
// not descend into, so they earn NO credit. That is the conservative direction (an honest agent runs
// the plain command and is credited); the test battery pins both the attacks and this control.
export const READ_VERBS = ["cat", "bat", "less", "more", "view", "nl", "od", "xxd", "sed", "head", "tail"];
const MENTION_HEADS = new Set(["echo", "printf", "print", "true", ":", ""]);
const WRAPPER_HEADS = new Set(["command", "sudo", "env", "nice", "time", "timeout", "exec", "builtin", "nohup", "stdbuf", "ionice", "doas"]);

function unquoteWord(t) {
  const s = String(t || "");
  const m = s.match(/^(['"])(.*)\1$/s);
  return m ? m[2] : s;
}

/** Remove heredoc bodies (`<<EOF … EOF`, `<<-'X' … X`): what a heredoc carries is input, never a command. */
function stripHeredocBodies(s) {
  return String(s).replace(/<<-?\s*(['"]?)([A-Za-z_][A-Za-z0-9_]*)\1[^\n]*\n[\s\S]*?\n[ \t]*\2(?=\s*$|\n)/g, " ");
}

function stripComments(s) {
  return String(s).replace(/(^|\s)#[^\n]*/g, " ");
}

/** The simple commands a shell would run, in order, as trimmed strings. Heredoc bodies and comments removed. */
export function commandSegments(command) {
  const s = stripComments(stripHeredocBodies(command));
  return s
    .split(/\|\||&&|[;|&\n]|[(){}]/)
    .map((x) => x.trim())
    .filter(Boolean);
}

/** { head, args } of one segment: the program the shell starts (basename, unquoted) and its arguments. */
export function segmentHead(seg) {
  const words = String(seg).trim().split(/\s+/).filter(Boolean);
  let i = 0;
  while (i < words.length) {
    const raw = unquoteWord(words[i]);
    if (/^[A-Za-z_][A-Za-z0-9_]*=/.test(raw)) { i += 1; continue; } // FOO=bar prefix
    const base = raw.split("/").pop();
    if (WRAPPER_HEADS.has(base)) {
      i += 1;
      if (base === "timeout") {
        while (i < words.length && /^(-|\d)/.test(unquoteWord(words[i]))) i += 1; // `timeout -k 5 60 cmd`
      } else if (base === "nice" || base === "ionice" || base === "stdbuf") {
        while (i < words.length && /^-/.test(unquoteWord(words[i]))) i += 1;
      }
      continue;
    }
    return { head: base, args: words.slice(i + 1).map(unquoteWord) };
  }
  return { head: "", args: [] };
}

/** True when every segment only PRINTS (echo/printf/true/:) — a mention, never an execution. */
function isMentionOnly(s) {
  const segs = commandSegments(s);
  if (!segs.length) return true;
  return segs.every((seg) => MENTION_HEADS.has(segmentHead(seg).head));
}

export function layersFromBashRead(command, repoRoot = null) {
  const hits = [];
  for (const seg of commandSegments(command)) {
    const { head, args } = segmentHead(seg);
    if (!READ_VERBS.includes(head)) continue; // only a READ program's own arguments are candidate paths
    // The credit is per-TOKEN (CONTAINMENT, closed 2026-09-18): the thing resolved is the thing the
    // shell would have opened, and a decoy outside the household does not count.
    const tokens = args.flatMap((a) => a.split(/[<>'"]+/)).filter(Boolean);
    for (const [key, suffix] of Object.entries(LAYER_SUFFIXES)) {
      if (hits.includes(key)) continue;
      const token = tokens.find((t) => t.includes(suffix));
      if (token && pathWithinAllowed(token, repoRoot)) hits.push(key);
    }
  }
  return hits;
}

/**
 * Rung 1 (2026-09-12). A READ that returned no content is not a read: the meter must not move on a
 * dedup/no-op re-read. Measured live this session: a second read of soli-deo-gloria returned
 * "unchanged since last read" with `content_returned:false`, and the stamp credited the layer anyway.
 * An agent could then walk the read order by re-reading each layer once with no content returned.
 *
 * Returns true (content observed), false (the runtime SAID there was no content), or null (the
 * runtime supplied no result at all — see the named limit: we cannot tell a read from a re-run there,
 * so backward compatibility credits it rather than bricking runtimes that send no tool_response).
 */
// ONE LIST, USED TWICE. The stamp hook tested channel PRESENCE against a wider list than this
// function read CONTENT from, and the drift was not cosmetic: a runtime naming its channel `result`
// satisfied the presence check while the content check returned null — "cannot tell" — which ALLOWS.
// Measured 2026-10-01: the same deduped observation ("File unchanged since last read.") credited the
// layer under `result` and credited nothing under `tool_response`. The list is now one exported
// constant so the two call sites cannot disagree again, and a control walks EVERY key in it.
export const RESULT_CHANNEL_KEYS = [
  "tool_response",
  "tool_result",
  "toolResponse",
  "toolResult",
  "result",
  "output",
];

// WHERE the channel is, is part of the contract. Hermes nests every non-top-level kwarg under
// `extra` (agent/shell_hooks.py `_payload_fields` — top level is only hook_event_name, tool_name,
// tool_input, session_id, cwd, profile, extra), so a top-level-only lookup reports a channel the
// runtime demonstrably SENT as absent. Measured 2026-10-03: with HOUSEHOLD_RUNTIME=hermes a Read
// carrying tool_response credited NOTHING, while the identical payload with the variable unset
// credited the layer — i.e. naming the runtime honestly was what bricked the read order, the exact
// inversion `RUNTIME_RESULT_CHANNELS` exists to avoid. Presence and content both read through this
// one function now, so the two call sites cannot disagree again (the drift the note above names).
export function resultChannelOf(raw) {
  if (!raw || typeof raw !== "object") return undefined;
  const extra = raw.extra && typeof raw.extra === "object" ? raw.extra : {};
  for (const k of RESULT_CHANNEL_KEYS) {
    if (raw[k] !== undefined && raw[k] !== null) return raw[k];
    if (extra[k] !== undefined && extra[k] !== null) return extra[k];
  }
  return undefined;
}

/** Did the payload carry a result channel at all — top level, or nested under `extra`? */
export function hasResultChannel(raw) {
  return resultChannelOf(raw) !== undefined;
}

// A result that SAYS the thing was not there is not content (adversarial analysis 2026-10-11, lane A
// S5 / lane E §3): "File does not exist." from the Read tool, and a Bash `cat` whose stdout is empty
// with "No such file" on stderr or a non-zero exit, both credited the layer. The text the runtime
// returns when it could not open the file is evidence of ABSENCE, which must never move the meter.
const NOT_FOUND_RE = /\b(?:file does not exist|no such file|not found|ENOENT|EISDIR|is a directory|permission denied|EACCES)\b/i;

export function readReturnedContent(raw) {
  const r = resultChannelOf(raw);
  if (r === undefined || r === null) return null; // no result channel — cannot tell
  if (typeof r === "object") {
    if (r.content_returned === false) return false;
    if (r.dedup === true) return false;
    // A Bash result shape: empty stdout with a not-found stderr, or a non-zero exit, is not a read.
    if (typeof r.stdout === "string" || typeof r.stderr === "string" || r.exitCode !== undefined || r.exit_code !== undefined) {
      const out = String(r.stdout ?? "");
      const err = String(r.stderr ?? "");
      const code = r.exitCode ?? r.exit_code;
      if (out.trim() === "" && (NOT_FOUND_RE.test(err) || (code !== undefined && code !== 0 && code !== null))) return false;
    }
    // Claude Code's own Read response, measured live 2026-09-22 (p1-rung-1-...): a real read is
    // { type: "text", file: { filePath, content, numLines, startLine, totalLines } }. An EMPTY file
    // returns the SAME populated wrapper — numLines:1, totalLines:1, a real filePath — with only
    // content:"" distinguishing it. Nothing here sets content_returned:false or dedup:true, and the
    // stringify-length fallback below reads the wrapper's own bytes as content, crediting an empty
    // file every time it was probed before this line existed. content is the one field this shape
    // can lie about only by being wrong outright, so it is read on its own, ahead of the fallback.
    if (r.type === "text" && r.file && typeof r.file.content === "string") {
      return r.file.content === "" ? false : true;
    }
    let s = "";
    try {
      s = JSON.stringify(r);
    } catch {
      return null;
    }
    if (/unchanged since last read/i.test(s)) return false;
    return s.length > 2 ? true : null; // "{}" / "[]" is an empty observation, not content
  }
  const s = String(r);
  if (s.trim() === "") return null; // an empty string is not affirmative evidence either way
  if (/unchanged since last read/i.test(s)) return false;
  // A short result that is only an error sentence ("File does not exist.") is absence, not content.
  if (s.length < 240 && NOT_FOUND_RE.test(s)) return false;
  return true;
}

/**
 * Rung 1's result channel, runtime-agnostic by construction (operator directive 2026-09-12: "everything
 * you build should be agnostic of hermes; if it works for hermes, it works for grok, and codex").
 *
 * ONE table, ONE rule, a CLOSED enumeration of every runtime `getRuntime()` can return, and the
 * evidence for each row. The rule is not "hermes requires a result"; it is "a read must return
 * evidence, and a runtime is exempt only where that is a measured fact about the runtime". A row that
 * is `null` is UNMEASURED, and unmeasured must not be bricked on a guess, so it is not yet enforced;
 * `bootstrap-result-channel-coverage.test.mjs` refuses a runtime with no row at all, so a new runtime
 * cannot be silently skipped, and the follow-up is to measure each row rather than to special-case one.
 */
export const RUNTIME_RESULT_CHANNELS = {
  "claude-code": { sendsResult: true, evidence: "measured 2026-09-22 (p1-rung-1-...): captured five real PostToolUse Read payloads live (a normal file, an empty file, a limit-truncated read, a repeat read, a real household file); every one carries tool_response.file.content as a string, so a Read with none, or an empty one, is now read directly rather than by the wrapper's own byte length" },
  grok: { sendsResult: null, evidence: "UNMEASURED — camelCase payload; toolResponse handled if present" },
  codex: { sendsResult: null, evidence: "UNMEASURED — Stop payload observed; no result channel seen" },
  hermes: { sendsResult: true, evidence: "measured 2026-09-12: post_tool_call carries tool_response; a Read with none is not a read" },
};

// The fallback for a runtime with NO row at all — a future runtime `getRuntime()` cannot yet return.
// Deliberately its own object, not a reuse of any named row (found 2026-09-22, p1-rung-1-...):
// riding on RUNTIME_RESULT_CHANNELS["claude-code"] meant measuring claude-code's real channel silently
// changed enforcement for every unrecognized runtime too, coupling two unrelated decisions. An unknown
// runtime is UNMEASURED by construction, so it fails toward NOT enforcing, the same as any other
// unmeasured row, never toward inheriting whatever the best-measured row happens to say.
const UNKNOWN_RUNTIME_ROW = Object.freeze({ sendsResult: null, evidence: "UNMEASURED — no row for this runtime name; the fallback row, never another runtime's" });

/** Does this runtime send an observed result, per the table? Unmeasured rows (`null`) return false. */
export function runtimeSendsResult(runtime) {
  const k = String(runtime || "").toLowerCase();
  const row = RUNTIME_RESULT_CHANNELS[k] || UNKNOWN_RUNTIME_ROW;
  return row.sendsResult === true;
}

// ── Rung 2 (2026-09-12): "fully" is the pointer's checklist, not just seven file reads ──────────
// HERMES.md / CLAUDE.md carry session steps beyond the read order: load the pointer, inject operator
// law, claim a patron, run the preflight. None were observed, so an agent could call a bootstrap
// "full" with the stamp green while skipping every one. These are observed as ACTIONS and credited on
// OBSERVED EXECUTION, never on success — `claim-patron` legitimately refuses on a shared machine, and
// the step is DONE when it has been run (the same posture as memory-recall being command-observed).
export const ACTION_KEYS = ["pointer", "directives_inject", "claim_patron", "preflight"];

const POINTER_BASENAMES = ["HERMES.md", "CLAUDE.md", "GROK.md", "AGENT.md", "AGENTS.md"];

/**
 * Which checklist step a shell command satisfies, or null. Judged PER SEGMENT on the program the shell
 * starts (see the credit-means-execution note above): `node <…>library.mjs claim-patron`, a direct
 * `<…>library.mjs claim-patron`, `bash <…>memory-directives-inject.sh`, `python3 <…>memory_evidence.py
 * directives`. A mention inside grep/printf/echo/ls/heredoc text credits nothing; a leading `echo` in a
 * compound command no longer hides the real run that follows it (G-159, L1.9).
 */
export function actionFromBashCommand(command) {
  for (const seg of commandSegments(command)) {
    const { head, args } = segmentHead(seg);
    if (!head || MENTION_HEADS.has(head)) continue;
    const a0 = args[0] || "";
    const a1 = args[1] || "";
    const isNode = head === "node" || head === "nodejs";
    const isSh = head === "bash" || head === "sh" || head === "zsh" || head === "source" || head === ".";
    const isPy = head === "python3" || head === "python";
    if ((isSh && a0.endsWith("memory-directives-inject.sh")) || head === "memory-directives-inject.sh") return "directives_inject";
    if (isPy && a0.endsWith("memory_evidence.py") && a1 === "directives") return "directives_inject";
    if (isNode && a0.endsWith("library.mjs")) {
      if (a1 === "claim-patron") return "claim_patron";
      if (a1 === "preflight") return "preflight";
    }
    if (head === "library.mjs") {
      if (a0 === "claim-patron") return "claim_patron";
      if (a0 === "preflight") return "preflight";
    }
  }
  return null;
}

/** Which checklist step a Read satisfies (the runtime pointer file), or null. */
export function pointerFromFilePath(fp, repoRoot = null) {
  const base = String(fp || "").split("/").pop();
  if (!POINTER_BASENAMES.includes(base)) return null;
  if (!pathWithinAllowed(fp, repoRoot)) return null; // a decoy elsewhere on disk is not the pointer
  return "pointer";
}

/**
 * The checklist steps not yet observed. An unreadable/forged stamp is missing ALL of them (loud).
 * Steps share the layers' clock (adversarial analysis 2026-10-11, lane A finding 5 / D13): a step
 * observed 25 h ago, or one dated in the future beyond clock skew, is missing, exactly as a layer is.
 */
export function missingActions(stamp, repoRoot = null, now = Date.now(), ttlMs = LAYER_READ_TTL_MS) {
  if (!stamp || stamp === "forged") return ACTION_KEYS.filter((k) => actionApplicable(k, repoRoot));
  return ACTION_KEYS.filter((k) => actionApplicable(k, repoRoot) && timestampStatus(stamp.actions_read?.[k], now, ttlMs) !== "fresh");
}

/**
 * Rung 2 applicability (careful-not-clever, #3077): a step may only be REQUIRED where it is
 * POSSIBLE. A leaf repo carries the guard but no `admin/library.mjs`, so requiring claim-patron or
 * preflight there would deny every mutation forever — the exact bricking #3077 exists to prevent.
 * UNAVAILABLE is not UNREAD (axiom 21): an inapplicable step is dropped from the requirement, not
 * silently credited.
 */
export function actionApplicable(step, repoRoot) {
  if (!repoRoot) return true;
  const has = (rel) => {
    try {
      return fs.existsSync(path.join(repoRoot, ...rel.split("/")));
    } catch {
      return false;
    }
  };
  switch (step) {
    case "pointer":
      return POINTER_BASENAMES.some((b) => has(b));
    case "directives_inject":
      return has(".claude/hooks/memory-directives-inject.sh") || has("admin/memory_evidence.py");
    case "claim_patron":
    case "preflight":
      return has("admin/library.mjs");
    default:
      return true;
  }
}

// ── Rung 3 (2026-09-12): the read order is enforced, narrowly ───────────────────────────────────
// The pointer says "do not skip to §5-6 without §0-4". A strict total order is NOT enforced here,
// deliberately: a genuine recall legitimately happens before any layer read, and parallel reads with
// near-equal timestamps would make a pairwise-inversion rule deny honest sessions. The enforced rule
// is the pointer's own boundary — a §5-6 read may not be credited before the first of §0-4.
// The order is DERIVED from the recorded layer timestamps, so no extra bookkeeping can drift from it.
export const READ_ORDER_HEAD = ["soli-deo-gloria", "careful-not-clever", "sophos", "sophos-os"];
export const READ_ORDER_TAIL = ["household-rulebook", "household-library"];

/** A description of the order violation, or null. Missing layers are a different finding (loud). */
export function readOrderViolation(stamp) {
  if (!stamp || stamp === "forged") return null;
  const lr = stamp.layers_read || {};
  const tsOf = (k) => {
    const v = lr[k];
    if (!v) return null;
    const t = Date.parse(v);
    return Number.isFinite(t) ? t : null;
  };
  const headTimes = READ_ORDER_HEAD.map(tsOf).filter((t) => t !== null);
  // Finding 18 (closed 2026-09-12): a recorded violation STANDS until a full in-order re-read happens.
  // Without this the only cure was deleting the stamp, which is the unrecorded path; the honest remedy
  // must be re-reading, and that remedy must actually clear it.
  const floor = stamp.order_violation_at ? Date.parse(stamp.order_violation_at) : NaN;
  if (Number.isFinite(floor)) {
    const required = [...READ_ORDER_HEAD, ...READ_ORDER_TAIL];
    const reread = required.every((k) => {
      const t = tsOf(k);
      return t !== null && t > floor;
    });
    if (!reread) {
      return `read order violated at ${stamp.order_violation_at} (§5-6 before §0-4); re-read the layers in order to clear it`;
    }
  }
  if (!headTimes.length) return null;
  const earliestHead = Math.min(...headTimes);
  const offenders = READ_ORDER_TAIL.filter((k) => {
    const t = tsOf(k);
    return t !== null && t < earliestHead;
  });
  if (!offenders.length) return null;
  return `§5-6 read before §0-4: ${offenders.join(", ")} credited before the first of [${READ_ORDER_HEAD.join(", ")}]`;
}

/** Grok / Claude / Hermes tool names → canonical names used by stamp + guard.
 *  Keys are lower-case; lookup is case-insensitive (adv: `bash` / `RUN_TERMINAL_COMMAND`).
 *
 *  The Hermes entries are not cosmetic: without them a Hermes `write_file`/`patch`
 *  normalises to itself, isRepoMutation() matches nothing, and the bootstrap guard
 *  ALLOWS the edit while reporting wired. Measured 2026-09-11 while wiring the
 *  Hermes native hooks (pre_tool_call/post_tool_call) — the alias table was the
 *  whole difference between a belt and a decoration. */
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

export function getRuntime() {
  const r = String(process.env.HOUSEHOLD_RUNTIME || "").trim().toLowerCase();
  if (r === "grok" || r === "claude-code" || r === "codex" || r === "hermes") return r; // runtime-agnostic-lint: allowed the runtime registry itself, the one place the names are canonicalised
  return "claude-code";
}

// Session patron binding (G-16 in docs/BLOCK-LOG.md; operator directive Ken 2026-09-23).
//
// HOUSEHOLD_PATRON is read from the HARNESS process environment. A remote or web session has no
// way to set that from inside the session: `export` in a tool shell never reaches a hook. So an
// agent could claim a name, check out a task under it, and still be refused by the claim guard as
// the generic id, with nothing it could legitimately do about it. Measured live 2026-09-23.
//
// The binding is a per-SESSION file the agent writes from its shell (admin/bind-patron.mjs, keyed
// by CLAUDE_CODE_SESSION_ID) and a hook reads (keyed by the session_id on its stdin). It carries
// exactly the trust of `export HOUSEHOLD_PATRON`: self-declared either way, never stronger.
// Order: HOUSEHOLD_PATRON (the operator's explicit choice) > this session's binding > default.
//
// Keyed on the exact session id, never on a name, because name-matched binding is the hijack
// class already registered as hls-session-binding-survives-release-and-name-match-hijack.
// sessionIdValid() rejects only empty and "unknown"; it allows any characters, so the id is held
// to a stricter file-safe shape before it becomes a path. A generic id in the file is ignored.
const BINDING_SAFE_ID = /^[A-Za-z0-9_-]{8,128}$/;
const BINDING_SAFE_NAME = /^[A-Za-z0-9_.-]{1,64}$/;
const GENERIC_PATRON_IDS = new Set(["claude", "claude-code"]);

export function patronBindingDir() {
  return process.env.HOUSEHOLD_PATRON_BINDING_DIR || path.join(os.homedir(), ".claude", "household-patron");
}

export function patronBindingPath(sessionId) {
  const s = String(sessionId ?? "").trim();
  if (!sessionIdValid(s) || !BINDING_SAFE_ID.test(s)) return null;
  return path.join(patronBindingDir(), s);
}

export function patronNameBindable(name) {
  const n = String(name ?? "").trim();
  return BINDING_SAFE_NAME.test(n) && !GENERIC_PATRON_IDS.has(n.toLowerCase());
}

export function readSessionPatron(sessionId) {
  const p = patronBindingPath(sessionId);
  if (!p) return null;
  let name;
  try { name = fs.readFileSync(p, "utf8").trim(); } catch { return null; }
  return patronNameBindable(name) ? name : null;
}

export function getPatron(sessionId) {
  if (process.env.HOUSEHOLD_PATRON) return process.env.HOUSEHOLD_PATRON;
  const bound = sessionId ? readSessionPatron(sessionId) : null;
  if (bound) return bound;
  return getRuntime() === "grok" ? "grok1" : "claude-code"; // runtime-agnostic-lint: allowed the lane's own display name, named not hidden
}

// Household-repo markers — what makes the loud-bootstrap belt apply to a tree.
// #3077 (yumi, 2026-09-03): the original three markers are things only a FULL open-claw-stuff
// clone carries. Leaf repos onboarded per spec §5.2 (Project-Sophos, the recipe repos) carry
// the hook trio and the synced front door under .claude/ and NONE of the three — so the guard
// they carried answered "not a household repo", exited 0 on every unstamped mutation, and
// bootstrap-dispatch (which keys "onboarded" on the guard FILE existing) reported them as
// enforced. Measured live through the user-level dispatcher with inert probes: unstamped
// Write, Edit and `git commit` into Project-Sophos ALLOWED; the same probes into ocs-work
// DENIED. Four of 22 onboarded repos on the operator Mac had that shape. "Present is not
// runnable" (UL-888 / UL-1016 class) sitting on the P0 mutation gate.
// Rule: a marker must be something that STAYS (a moved document is UL-266 again), and the
// onboarding itself is a marker — carrying this guard IS being a household repo, which is
// the same definition bootstrap-dispatch.mjs uses for "onboarded". Named limit: a guard copy
// dropped into any tree makes that tree guarded; that is the belt doing its job, not a false
// positive — the dispatcher would already have spawned it.
export const HOUSEHOLD_MARKERS = [
  ".claude/hooks/bootstrap-guard.mjs", // the onboarding itself (spec §5.2) — dispatcher parity
  ".claude/skills/sophos/SKILL.md",    // synced front door (leaf-repo layout)
  "skills/sophos/SKILL.md",            // canonical front door (open-claw-stuff layout)
  ".household-root",                   // machine-neutral discovery file (household-root-resolver step 3)
  ".household-library",
  "docs/SOPHOS-OPERATING-SYSTEM.md",
];

export function isHouseholdRepo(root) {
  if (!root) return false;
  try {
    return HOUSEHOLD_MARKERS.some((m) => fs.existsSync(path.join(root, ...m.split("/"))));
  } catch {
    return false;
  }
}

function walkHouseholdRoot(start) {
  let cur = path.resolve(start);
  for (let i = 0; i < 8; i++) {
    if (isHouseholdRepo(cur)) return cur;
    const parent = path.dirname(cur);
    if (parent === cur) break;
    cur = parent;
  }
  return null;
}

/**
 * Resolve household repo root for this hook invocation.
 * Prefer env, then workspace/cwd markers, else the hooks tree's clone.
 */
export function getRepoRoot(input = null) {
  if (process.env.HOUSEHOLD_REPO_ROOT) {
    return path.resolve(process.env.HOUSEHOLD_REPO_ROOT);
  }
  if (input) {
    for (const key of ["workspaceRoot", "workspace_root", "cwd"]) {
      const v = input[key];
      if (v) {
        const found = walkHouseholdRoot(String(v));
        if (found) return found;
      }
    }
  }
  return HOOK_FILE_REPO_ROOT;
}

export function getRepoName(input = null) {
  return path.basename(getRepoRoot(input));
}

/**
 * Normalize Claude (snake_case) and Grok (camelCase) hook stdin into one shape.
 * tool_name is canonical (Read|Bash|Edit|Write|NotebookEdit|…).
 */
export function normalizeHookInput(raw) {
  if (!raw || typeof raw !== "object") return null;
  // Session id comes from the hook PAYLOAD only — deliberately never from the
  // environment. 2026-08-08: an agent proposed a CLAUDE_CODE_SESSION_ID fallback after
  // seeing an id-less denial, then found it broke three sessionid-contract tests and
  // was solving a bug that did not exist. Two reasons it must stay payload-only:
  //   1. The premise was wrong. This runtime DOES supply session_id — the denial came
  //      from a hand-made probe JSON that omitted it, not from a real invocation. The
  //      real failure was that the hooks were never registered at all (multi-root/remote;
  //      SOPHOS-OPERATING-SYSTEM §0 case 2, memory 6857086c, 2026-07-20). Fix the
  //      registration (admin/install-bootstrap-dispatch.mjs), not the attribution.
  //   2. Even if it were needed, env is AMBIENT, not per-invocation: an exported value
  //      lets an id-less call inherit an identity the runtime never assigned it, which
  //      is exactly the hole sessionIdValid() closes. The tests encode that contract.
  const session_id = raw.session_id ?? raw.sessionId ?? raw.sessionID ?? "";
  const rawTool = String(raw.tool_name ?? raw.toolName ?? "");
  const tool_name = TOOL_ALIASES[rawTool.toLowerCase()] || rawTool;
  const tool_input = raw.tool_input ?? raw.toolInput ?? {};
  // Unify path fields: Claude file_path, Grok target_file / path
  const file_path =
    tool_input.file_path
    ?? tool_input.target_file
    ?? tool_input.path
    ?? tool_input.notebook_path
    ?? "";
  // Shell command: string, or rare array form (join with spaces for scan only).
  let command = tool_input.command ?? tool_input.cmd ?? "";
  if (Array.isArray(command)) command = command.map(String).join(" ");
  else command = String(command ?? "");
  const normalized_input = {
    ...tool_input,
    file_path: file_path || tool_input.file_path,
    command,
  };
  return {
    session_id: String(session_id),
    agent_id: String(raw.agent_id ?? raw.agentId ?? ""),
    agent_type: String(raw.agent_type ?? raw.agentType ?? ""),
    tool_name,
    tool_input: normalized_input,
    workspaceRoot: raw.workspaceRoot ?? raw.workspace_root ?? raw.cwd ?? "",
    raw,
  };
}

// Stamp root is HOUSEHOLD-SHARED, not per-repo (spec §5.2 A5, operator directive
// 2026-07-20): the six-layer read order is household-global and a session is one
// session across every repo it touches — per-repo buckets demand the same canonical
// reads once per repo, and a multi-repo session bootstrapped in one repo is denied
// in the next. Measured live 2026-08-19: Project-Sophos's guard (A5-lineage hooks,
// shared bucket) was mechanically unsatisfiable because the canonical stamp hook
// filed reads in a per-repo bucket its checker never consulted. The A5
// implementation (5ba8fced) never merged to main; the per-repo variant arrived in a
// bulk hook import (66b53970) with no counter-rationale — this restores the spec'd
// design, keeping main's dual-runtime split and the env override. `input` stays in
// the signature for caller compatibility; the location no longer depends on it.
// Migration cost, named: stamps in the old per-repo buckets are not read from the
// new location, so each live session re-earns its stamp once via the read order.
// Operator applied 2026-08-19 (HLS p1-loud-bootstrap-spec-vs-lib-stamp-root).
export function stampRoot(input = null) {
  if (process.env.HOUSEHOLD_BOOTSTRAP_ROOT) {
    return process.env.HOUSEHOLD_BOOTSTRAP_ROOT;
  }
  const runtime = getRuntime();
  if (runtime === "grok") { // runtime-agnostic-lint: allowed grok's own stamp path, named not hidden
    return path.join(os.homedir(), ".grok", "household-bootstrap", "household-v2");
  }
  // SUPERSET NOTE (2026-09-25, from Project-Sophos, pinned by bootstrap-declaration.test.mjs there):
  // Codex owns a distinct host hook and receives its session identity from the runtime event. Its
  // writer already uses this per-repository root (Project-Sophos 31df4c3); the shared reader must
  // use the identical path or a valid Codex stamp becomes invisible to the terminal declaration gate.
  if (runtime === "codex") { // runtime-agnostic-lint: allowed codex's own stamp path, named not hidden
    return path.join(os.homedir(), ".codex", "household-bootstrap", getRepoName(input));
  }
  return path.join(os.homedir(), ".claude", "household-bootstrap", "household-v2");
}

export function eventsPath(input = null) {
  if (process.env.HOUSEHOLD_BOOTSTRAP_EVENTS) {
    return process.env.HOUSEHOLD_BOOTSTRAP_EVENTS;
  }
  return path.join(getRepoRoot(input), ".household-library", "events.jsonl");
}

function secretPath(input = null) {
  return path.join(stampRoot(input), ".secret");
}

// The HMAC key for stamp sealing/verification. A failed READ must never become a WRITE
// (p1-guard-residual / #2752): distinguish a genuine first run (no secret yet -> create) from
// an existing-but-UNREADABLE secret. Overwriting the latter would ROTATE the key and ERASE the
// on-disk tamper signal, and THROWING would escape bootstrap-guard's outer catch, which fails
// OPEN (exit 0). On any non-ENOENT read error — or a read-only caller (verify) that reached a
// missing secret — do neither: return an EPHEMERAL, unpersisted key so every HMAC check fails
// CLOSED ("forged") while the on-disk secret is left untouched. `allowCreate` is the asymmetry:
// only sealing (first run) may mint; verification is strictly read-only.
/**
 * The signing key AND whether it was actually ESTABLISHED (#2753 residual, measured 2026-09-06).
 *
 * getSecret returns an ephemeral key when the anchor cannot be read, so verification fails
 * CLOSED. That is right for VERIFYING and wrong for SEALING: saveStamp is bookkeeping and the
 * guard calls it on a denial, so an unreadable anchor caused the good on-disk seal to be
 * OVERWRITTEN with an ephemeral one. Restoring the file permissions then recovered nothing,
 * because the stamp no longer matched the real secret. A transient permission problem became a
 * PERMANENT disarm, which is precisely what bootstrap-guard's own comment says bookkeeping must
 * never do. Callers that WRITE must ask for the status and refuse to seal when it is false.
 */
export function secretStatus(input = null, { allowCreate = true } = {}) {
  const p = secretPath(input);
  try {
    return { key: fs.readFileSync(p, "utf8").trim(), established: true };
  } catch (e) {
    const code = e && e.code;
    if (code === "ENOENT" && allowCreate) {
      try {
        fs.mkdirSync(stampRoot(input), { recursive: true });
        const s = crypto.randomBytes(32).toString("hex");
        fs.writeFileSync(p, s, { mode: 0o600 });
        return { key: s, established: true };
      } catch {
        // Could not mint either. Fall through to the ephemeral key rather than throwing: an
        // uncaught throw here escaped to the guard's outer catch, which used to exit 0 (allow).
      }
    }
    console.error(
      `bootstrap-lib.getSecret: secret at ${p} could not be read (${code || "unknown"})${allowCreate ? "" : " under a read-only check"} — using an ephemeral key so verification fails CLOSED; the on-disk secret was NOT overwritten. Restore its permissions to re-enable bootstrap.`,
    );
    return { key: crypto.randomBytes(32).toString("hex"), established: false };
  }
}

export function getSecret(input = null, opts = {}) {
  return secretStatus(input, opts).key;
}

export function hmacOf(stamp, secret) {
  const { hmac, ...body } = stamp;
  // Recursively bind the read evidence too. A replacer array drops nested keys.
  // Legacy seals must be re-earned through observed reads; never accept both formats.
  const canon = JSON.stringify(canonicalEventBody(body));
  return crypto.createHmac("sha256", secret).update(canon).digest("hex");
}

// Invalid ids must never satisfy the gate (loud-bootstrap-sessionid-contract).
export function sessionIdValid(raw) {
  const s = String(raw ?? "").trim();
  return s !== "" && s.toLowerCase() !== "unknown";
}

/**
 * The ONE session-id resolution both the guard and the stamp writer use. They
 * MUST agree: if the stamp hook records reads under one key and the guard checks
 * another, a fully-bootstrapped session is denied and pushed to the escape hatch
 * (p2-bootstrap-guard-stamp-writer-session-id-split, measured 2026-08-09). An id
 * sessionIdValid rejects (empty, "unknown" in any case, whitespace-only) resolves
 * to the literal "unknown" — the same key the guard denies under — so the two can
 * never key a different stamp file for the same payload.
 */
export function parentSessionId(input) {
  const id = input && typeof input === "object" ? input.session_id : input;
  return sessionIdValid(id) ? String(id) : "unknown";
}

/**
 * SUB-AGENT IDENTITY (adversarial analysis 2026-10-11, plan 2.6; findings D3, F-Q4, A).
 * A sub-agent's hook input carries the PARENT's session_id plus `agent_id` / `agent_type`
 * (Claude Code hooks reference, common input fields). Before this, every read a sub-agent made
 * landed in the parent's stamp: this session's mutation plane was restored by a sub-agent's grep.
 * A sub-agent now keys its OWN stamp, `<session>__agent-<id>`; its reads credit only that stamp,
 * and effectiveStamp() lets it INHERIT the parent's reads read-only, never the reverse.
 * Named limit: a runtime that omits agent_id is indistinguishable from the parent; the env carries
 * nothing (measured 2026-10-11: a sub-agent's environment differs from its parent's only by
 * JAVA_TOOL_OPTIONS, MCP_TOOL_TIMEOUT and TRACEPARENT).
 */
export function agentIdOf(input) {
  if (!input || typeof input !== "object") return "";
  const raw = input.raw && typeof input.raw === "object" ? input.raw : input;
  const id = input.agent_id ?? raw.agent_id ?? raw.agentId ?? "";
  const s = String(id ?? "").trim();
  return s ? s.replace(/[^A-Za-z0-9_.-]/g, "_").slice(0, 64) : "";
}

export const AGENT_KEY_RE = /^(.+)__agent-([A-Za-z0-9_.-]+)$/;

export function resolveSessionId(input) {
  const sid = parentSessionId(input);
  const agent = agentIdOf(input);
  if (!agent || sid === "unknown") return sid;
  return `${sid}__agent-${agent}`;
}

/** How long a stamp-writer "I last credited THIS id" pointer stays eligible for the guard. */
export const LAST_CREDITED_TTL_MS = 4 * 60 * 60 * 1000;

export function lastCreditedPath(input = null) {
  return path.join(stampRoot(input), ".last-credited-session.json");
}

/** Stamp-hook writes this after crediting a session so the guard can follow after compact/model-swap. */
export function recordLastCreditedSession(sessionId, input = null, nowMs = Date.now()) {
  if (!sessionIdValid(sessionId)) return null;
  const body = {
    session_id: String(sessionId),
    at: new Date(nowMs).toISOString(),
    runtime: getRuntime(),
  };
  try {
    fs.mkdirSync(stampRoot(input), { recursive: true });
    const target = lastCreditedPath(input);
    const tmp = `${target}.${process.pid}.tmp`;
    fs.writeFileSync(tmp, JSON.stringify(body) + "\n");
    fs.renameSync(tmp, target);
    return body;
  } catch {
    return null;
  }
}

export function readLastCreditedSession(input = null) {
  try {
    const j = JSON.parse(fs.readFileSync(lastCreditedPath(input), "utf8"));
    if (!j || typeof j.session_id !== "string") return null;
    return j;
  } catch {
    return null;
  }
}

/**
 * The stamp the GUARD judges: the session's own stamp, and for a sub-agent key the parent's
 * verified reads unioned in (latest timestamp per layer, parent's steps under the child's).
 * Read-only: nothing here is written back, so a child can never credit its parent.
 */
export function effectiveStamp(sessionId, input = null) {
  const own = verifyStamp(sessionId, input);
  const m = AGENT_KEY_RE.exec(String(sessionId || ""));
  if (!m || own === "forged") return own;
  const parent = verifyStamp(m[1], input);
  if (!parent || parent === "forged") return own;
  const merged = own ? JSON.parse(JSON.stringify(own)) : newStamp(sessionId, input);
  merged.layers_read = merged.layers_read || {};
  for (const [layer, ts] of Object.entries(parent.layers_read || {})) {
    if (!ts) continue;
    const mine = merged.layers_read[layer];
    if (!mine || (Date.parse(ts) || 0) > (Date.parse(mine) || 0)) merged.layers_read[layer] = ts;
  }
  merged.actions_read = { ...(parent.actions_read || {}), ...(merged.actions_read || {}) };
  merged.inherited_from = m[1];
  return merged;
}

export function stampPath(sessionId, input = null) {
  const safe = String(sessionId || "unknown").replace(/[^A-Za-z0-9_.-]/g, "_");
  return path.join(stampRoot(input), `${safe}.json`);
}

export function loadStamp(sessionId, input = null) {
  try {
    return JSON.parse(fs.readFileSync(stampPath(sessionId, input), "utf8"));
  } catch {
    return null;
  }
}

export function newStamp(sessionId, input = null) {
  const layers = {};
  for (const k of ALL_LAYERS) layers[k] = null;
  const runtime = getRuntime();
  const agentKey = AGENT_KEY_RE.exec(String(sessionId || ""));
  return {
    session_id: String(sessionId || "unknown"),
    ...(agentKey ? { parent_session_id: agentKey[1], agent_id: agentKey[2] } : {}),
    runtime,
    repo: getRepoName(input),
    patron: getPatron(),
    started_at: new Date().toISOString(),
    layers_read: layers,
    front_door_skill: null, // Hermes-only: timestamp of skill_view(FRONT_DOOR_SKILL)
    grade: "friction",
    written_by:
      runtime === "grok" ? "bootstrap-stamp-hook.mjs(grok)" : "bootstrap-stamp-hook.mjs", // runtime-agnostic-lint: allowed grok's stamp writer label, named not hidden
    ledgered: false,
    denials: 0,
  };
}

export function saveStamp(stamp, input = null, { mergeFromDisk = false } = {}) {
  // Never seal with a key that was not ESTABLISHED. Writing an ephemeral-key seal over a good
  // one turns a transient unreadable anchor into a permanent disarm: verification keeps failing
  // even after the permissions are restored, because the stamp no longer matches the real
  // secret. Losing this write is strictly better than corrupting the anchor, so we refuse it
  // LOUDLY and leave whatever is on disk intact.
  const { key, established } = secretStatus(input);
  if (!established) {
    // THROW rather than return quietly. Both callers already treat a failed write as a
    // bookkeeping failure and report it loudly (the guard prints "denial bookkeeping failed"
    // and still denies; the stamp hook logs and exits 0), and #2727 pins that report. A silent
    // return would suppress it, which is how a guard stops saying what it could not do.
    throw new Error(
      "refusing to re-seal the stamp with an ephemeral key: the trust anchor is not readable, " +
      "so sealing now would overwrite a good seal and make the disarm permanent. The existing " +
      "stamp is left untouched so bootstrap recovers once the anchor is restored.",
    );
  }
  const root = stampRoot(input);
  // A stamp root on a pseudo-filesystem made Node's recursive mkdir spin (116k calls in 8 s, lane E
  // 2026-10-11): refuse such a root outright rather than hang the hook the wrapper then has to kill.
  if (/^\/(proc|sys|dev)(\/|$)/.test(path.resolve(root))) {
    throw new Error(`refusing a stamp root on a pseudo-filesystem: ${root}`);
  }
  fs.mkdirSync(root, { recursive: true });
  // SERIALISED AND ATOMIC (adversarial analysis 2026-10-11, lane E §3): two stamp writes in the same
  // session lost a credit in 2 of 5 trials, because read-merge-write raced and the loser's union was
  // taken from a stale read. A lock file (O_EXCL, bounded wait) serialises writers; the merge is
  // re-done UNDER the lock so it sees the winner's write; the file lands by rename so a reader never
  // sees a half-written stamp (which verifyStamp would otherwise report as forged).
  const target = stampPath(stamp.session_id, input);
  const lockPath = `${target}.lock`;
  let fd = null;
  const deadline = Date.now() + 2000;
  while (fd === null) {
    try {
      fd = fs.openSync(lockPath, "wx");
    } catch (e) {
      if (e?.code !== "EEXIST") throw e;
      // A lock older than 10 s belongs to a writer that died; take it over rather than wedge.
      try { if (Date.now() - fs.statSync(lockPath).mtimeMs > 10_000) fs.unlinkSync(lockPath); } catch { /* raced away */ }
      if (Date.now() > deadline) throw new Error(`stamp lock held too long: ${lockPath}`);
      const until = Date.now() + 15;
      while (Date.now() < until) { /* short spin; hooks are sub-second */ }
    }
  }
  try {
    // The stamp HOOK asks for the union (two concurrent observers must not clobber each other); the
    // guard's denial bookkeeping and the freshness tests write exactly what they hold (a sealed
    // backdate must land, or the expiry tests prove nothing).
    if (mergeFromDisk) mergeLayersFromDisk(stamp, input);
    stamp.hmac = hmacOf(stamp, key);
    const tmp = `${target}.${process.pid}.tmp`;
    fs.writeFileSync(tmp, JSON.stringify(stamp, null, 2) + "\n");
    fs.renameSync(tmp, target);
  } finally {
    try { fs.closeSync(fd); } catch { /* already closed */ }
    try { fs.unlinkSync(lockPath); } catch { /* already gone */ }
  }
}

/**
 * Merge-on-write for parallel Reads (UL-078). The stamp hook is read-modify-write: two Read events
 * in one session both load the SAME stamp, each set their own layer, and the last saveStamp()
 * clobbers the layer the other added. A fully-read session then looks incomplete and is denied.
 * Before writing, union this stamp layers_read with whatever is on disk NOW (a concurrent hook may
 * have written a layer since we loaded), keeping the LATER timestamp per layer (#3431), and adopt an
 * on-disk ledgered:true so the bootstrap event is not appended twice. Not a lock: it converts a
 * last-writer CLOBBER into a last-writer UNION, the standard mitigation for this class.
 */
export function mergeLayersFromDisk(stamp, input = null) {
  const onDisk = verifyStamp(stamp.session_id, input);
  if (!onDisk || typeof onDisk !== "object") return stamp;
  stamp.layers_read = stamp.layers_read || {};
  for (const [layer, ts] of Object.entries(onDisk.layers_read || {})) {
    if (!ts) continue;
    const mine = stamp.layers_read[layer];
    // #3431: LATEST read wins, not earliest.
    //
    // Earliest-wins was correct for what UL-078 solved (a concurrent Read must not be
    // clobbered, and the bootstrap event must not double-append) and WRONG for freshness: it
    // silently restored the OLD timestamp over a fresh one, so the stamp hook's refresh was
    // undone on the very next union and a posture read stayed write-once no matter what the
    // writer did. Write-once was enforced in TWO places, not one. UL-078's actual concern was
    // losing a layer's PRESENCE, which latest-wins preserves identically; double-append is
    // prevented by the separate `ledgered` flag below, never by the timestamp.
    // Finding 18 (a re-read that lands after a recorded order violation must supersede the old
    // stamp) is the same rule with no special case: the later read wins.
    stamp.layers_read[layer] = mine ? (mine > ts ? mine : ts) : ts;
  }
  // Rung 2: union the observed checklist steps too (same last-writer-clobber rationale).
  stamp.actions_read = stamp.actions_read || {};
  for (const [step, ts] of Object.entries(onDisk.actions_read || {})) {
    if (!ts) continue;
    const mine = stamp.actions_read[step];
    // Latest wins, as for layers (#3431): steps now expire, so earliest-wins would restore a
    // stale time over a fresh re-run and lock the session out for good.
    stamp.actions_read[step] = mine ? (mine > ts ? mine : ts) : ts;
  }
  if (onDisk.ledgered) stamp.ledgered = true;
  return stamp;
}

// null = missing; "forged" = HMAC mismatch; otherwise the verified stamp object.
export function verifyStamp(sessionId, input = null) {
  const stamp = loadStamp(sessionId, input);
  if (!stamp) return null;
  // Verification is READ-ONLY: never mint/write a secret while checking one (a failed read must
  // not become a write — p1-guard-residual/#2752).
  //
  // Ask whether the anchor was ESTABLISHED and refuse on the answer. #3135 made the same call
  // explicit on its own shape (`if (secret === null) return "forged"`), and that is the half of
  // it worth keeping: the old line inferred the refusal from an ephemeral key not matching,
  // which is arithmetic that happens to be true rather than a stated rule.
  const { key, established } = secretStatus(input, { allowCreate: false });
  if (!established) return "forged";
  if (!stamp.hmac || stamp.hmac !== hmacOf(stamp, key)) return "forged";
  return stamp;
}

// How long a posture read stays good (#3431). The stamp always RECORDED when each layer was read
// and never COMPARED it: this function tested that the KEY EXISTED and never looked at the VALUE.
// Measured 2026-09-07: a session still running that day showed 7 of 7 layers complete on reads
// timestamped 2026-08-13. By then the files had long left its working context, and it proposed
// rebuilding a field the code already wrote, having measured a ledger twice without reading the
// write path. The guard reported a governed session; the posture was a summary of a summary.
//
// 24h is deliberate, not a placeholder: long enough that a normal working session is never
// interrupted, short enough that "stale by weeks" cannot recur. There is deliberately NO env
// override, because HOUSEHOLD_BOOTSTRAP_GUARD_BLOCK is already the operator's escape and a second
// knob here would be one more protective flag that fails unsafe when unset.
export const LAYER_READ_TTL_MS = 24 * 60 * 60 * 1000;

/**
 * Classify each required layer as never-read or read-too-long-ago.
 *
 * An absent or unparseable timestamp is STALE, never fresh: absence is not a measurement and the
 * safe direction is to ask again. A timestamp slightly in the FUTURE counts as fresh, because
 * small clock skew must not brick a session that just read the file; a maliciously future-dated
 * stamp is out of scope here and in scope for the hmac seal, which a caller cannot forge without
 * the anchor.
 */
// Clock skew a stamp may run AHEAD of this process without being disbelieved. Five minutes covers a
// container whose clock drifted; it does not cover a stamp dated an hour or a day ahead, which lane E
// (2026-10-11, §2) showed a sealed stamp could carry and this guard would allow FOREVER — a timestamp
// in the future never ages out. Beyond the skew window a read is "future": not fresh, not credited.
export const CLOCK_SKEW_MS = 5 * 60 * 1000;

/** "never" | "unparseable" | "future" | "stale" | "fresh" for one recorded timestamp. */
export function timestampStatus(raw, now = Date.now(), ttlMs = LAYER_READ_TTL_MS, skewMs = CLOCK_SKEW_MS) {
  if (!raw) return "never";
  const t = Date.parse(raw);
  if (!Number.isFinite(t)) return "unparseable";
  if (t - now > skewMs) return "future";
  if (now - t > ttlMs) return "stale";
  return "fresh";
}

export function layerReadStatus(stamp, now = Date.now(), ttlMs = LAYER_READ_TTL_MS) {
  if (!stamp || stamp === "forged") return { never: [...ALL_LAYERS], stale: [], future: [] };
  const never = [], stale = [], future = [];
  for (const k of ALL_LAYERS) {
    const st = timestampStatus(stamp.layers_read?.[k], now, ttlMs);
    if (st === "never") never.push(k);
    else if (st === "future") future.push(k);
    else if (st !== "fresh") stale.push(k); // unparseable counts as stale: absence is not a measurement
  }
  return { never, stale, future };
}

// ONE definition of "missing", so the guard, the stamp hook and bootstrap-status cannot disagree.
// A status that reports complete while the guard denies is the false-CALM this household keeps
// paying for, so a stale layer is missing everywhere or nowhere.
export function missingLayers(stamp, now = Date.now(), ttlMs = LAYER_READ_TTL_MS) {
  const { never, stale, future } = layerReadStatus(stamp, now, ttlMs);
  return [...never, ...stale, ...future];
}

// Hermes front-door-skill credit. A Hermes session must have loaded FRONT_DOOR_SKILL
// (via skill_view) before any mutation; this is belt 2 of the belt-and-suspenders pair
// (the Hermes plugin is belt 1). Returns true when the skill was loaded fresh (within
// TTL), false when missing/stale/forged.
export function frontDoorSkillRead(stamp, now = Date.now(), ttlMs = LAYER_READ_TTL_MS) {
  if (!stamp || stamp === "forged") return false;
  const ts = stamp.front_door_skill;
  if (!ts) return false;
  return timestampStatus(ts, now, ttlMs) === "fresh";
}

// Which runtimes are held to the front-door-skill requirement. A data table, not a
// branch: the runtime name is the KEY, never a decision. Only the Hermes runtime is
// held to it today — it is the runtime that loads layers through skill_view and the
// one that produced the improvise-and-stall failure. Other runtimes load layers via
// file paths and are unaffected. Add a row here to hold a future runtime to it.
export const FRONT_DOOR_SKILL_RUNTIMES = {
  hermes: { requires: true, evidence: "measured 2026-10-17: a Hermes session never loaded sophos-household, misread its own system prompt as an injection, and refused to bootstrap" },
};

// ONE definition of "front-door skill missing", shared by the guard and the stamp hook.
// A runtime with no row (or a row with requires:false) is never missing it.
export function missingFrontDoorSkill(stamp, runtime, now = Date.now(), ttlMs = LAYER_READ_TTL_MS) {
  const k = String(runtime || "").toLowerCase();
  const row = FRONT_DOOR_SKILL_RUNTIMES[k];
  if (!row || row.requires !== true) return false;
  return !frontDoorSkillRead(stamp, now, ttlMs);
}

/**
 * ONE verifier signature for "is this session bootstrapped?" — shared by bootstrap-status
 * and bootstrap-guard (board-mirror-status-false-incomplete, measured 2026-09-05).
 *
 * Status used to call `verifyStamp(sid)` with no hook input while the guard called
 * `effectiveStamp(sessionId, input)`. When those diverge, status reports complete:0 for a
 * stamp the guard just accepted — a false alarm that trains agents to ignore the real one.
 *
 * Always pass a hook-shaped `input` (at least `{ session_id }`). Status synthesizes one from
 * the stamp filename; the guard passes the real PreToolUse payload. Both then walk the same
 * effectiveStamp → missingLayers / missingActions / readOrderViolation / sessionIdValid path.
 *
 * @returns {{ complete: boolean, reasons: string[], stamp: object|null|"forged", sessionId: string }}
 */
export function judgeBootstrapSession(sessionId, input = null, { repoRoot = null } = {}) {
  const sid = String(sessionId ?? "");
  // Synthesize the same shape the guard receives so secretStatus/loadStamp see a session_id.
  // Shallow-copy so a caller’s PreToolUse payload is never mutated.
  const hookInput = input && typeof input === "object"
    ? { ...input, session_id: input.session_id || sid }
    : { session_id: sid };

  const reasons = [];
  if (!sessionIdValid(hookInput.session_id) && !sessionIdValid(sid)) {
    reasons.push("session-id");
  }

  const stamp = effectiveStamp(sid || resolveSessionId(hookInput), hookInput.raw || hookInput);
  if (!stamp) reasons.push("unreadable");
  else if (stamp === "forged") reasons.push("forged");
  else {
    const layers = missingLayers(stamp);
    const steps = missingActions(stamp, repoRoot);
    const order = readOrderViolation(stamp);
    if (layers.length) reasons.push(`layers: ${layers.join(",")}`);
    if (steps.length) reasons.push(`steps: ${steps.join(",")}`);
    if (order) reasons.push("read-order");
  }
  // Filename / resolved id must also be attributables (matches status's prior check).
  if (!sessionIdValid(sid) && !reasons.includes("session-id")) reasons.push("session-id");

  return {
    complete: reasons.length === 0,
    reasons,
    stamp,
    sessionId: sid || resolveSessionId(hookInput),
  };
}

/**
 * Session id the GUARD should judge (bootstrap-dispatch-guard-blocks-all-session-writes…).
 * Prefer the hook payload. After compact/model-swap the payload id can be new/empty while the
 * stamp-writer kept crediting the prior id — follow `.last-credited-session.json` when that
 * stamp is complete and fresh. Never falls back to an arbitrary complete stamp in the root
 * (status's complete:N counts stale sessions; inheriting one would be false-CALM).
 */
export function resolveGuardedSessionId(input, { repoRoot = null, nowMs = Date.now() } = {}) {
  const hookInput = input && typeof input === "object" ? input : { session_id: String(input ?? "") };
  // Resolve from the NORMALIZED payload: the guard passes input.raw, and a raw Grok payload says
  // `sessionId` (camelCase), which resolveSessionId never reads. Measured 2026-10-15: every Grok
  // session resolved to "unknown", so its own stamp (forged or real) was never consulted and the
  // remap below judged it by another session's stamp. normalizeHookInput reads every spelling.
  const primary = resolveSessionId(normalizeHookInput(hookInput) || hookInput);
  const primaryVerdict = judgeBootstrapSession(primary, hookInput, { repoRoot });
  if (primaryVerdict.complete) {
    return { sessionId: primary, via: "payload", remapped: false };
  }
  // Never remap away from a forged stamp (forgery is a finding to report, not a state to route
  // around), nor from an unattributable id: "unknown" names no session, so it can prove no
  // continuity with the last-credited one. The compact case this remap exists for (#3372) is a
  // NEW, valid id (admin/tests/bootstrap-dispatch-session-key.test.mjs S3), which still remaps.
  if (primaryVerdict.reasons.includes("forged") || !sessionIdValid(primary)) {
    return { sessionId: primary, via: "payload", remapped: false, refused_remap: primaryVerdict.reasons.includes("forged") ? "forged" : "unattributable" };
  }

  const last = readLastCreditedSession(hookInput);
  if (!last || !sessionIdValid(last.session_id) || last.session_id === primary) {
    return { sessionId: primary, via: "payload", remapped: false };
  }
  const age = nowMs - Date.parse(last.at);
  if (!Number.isFinite(age) || age < 0 || age > LAST_CREDITED_TTL_MS) {
    return { sessionId: primary, via: "payload", remapped: false, stale_last: true };
  }
  const altVerdict = judgeBootstrapSession(last.session_id, { ...hookInput, session_id: last.session_id }, { repoRoot });
  if (!altVerdict.complete) {
    return { sessionId: primary, via: "payload", remapped: false };
  }
  return {
    sessionId: last.session_id,
    via: "last-credited",
    remapped: true,
    from: primary,
    last_at: last.at,
  };
}

/** Canonicalize like admin/event-chain.mjs so sealed hashes match library.mjs. */
function canonicalEventBody(value) {
  if (Array.isArray(value)) return value.map(canonicalEventBody);
  if (value && typeof value === "object") {
    return Object.fromEntries(
      Object.keys(value)
        .sort()
        .map((key) => [key, canonicalEventBody(value[key])]),
    );
  }
  return value;
}

/**
 * When the household events ledger has started a hash chain, seal appends so
 * hook denials cannot brick library.mjs with `unchained_event_after_chain`.
 * Test ledgers (HOUSEHOLD_BOOTSTRAP_EVENTS) and pre-chain ledgers stay plain.
 */
function sealIfChainStarted(payload, file) {
  if (process.env.HOUSEHOLD_BOOTSTRAP_EVENTS) return payload;
  let prior = [];
  try {
    const text = fs.readFileSync(file, "utf8");
    prior = text.trim()
      ? text.trim().split("\n").filter(Boolean).map((l) => JSON.parse(l))
      : [];
  } catch {
    return payload;
  }
  let parent = null;
  for (let i = prior.length - 1; i >= 0; i--) {
    if (typeof prior[i]?.event_hash === "string") {
      parent = prior[i].event_hash;
      break;
    }
  }
  if (!parent) return payload; // chain not started (or empty)
  const sealed = { ...payload, prev_hash: parent };
  const body = { ...sealed };
  delete body.event_hash;
  const digest = crypto
    .createHash("sha256")
    .update(JSON.stringify(canonicalEventBody(body)), "utf8")
    .digest("hex");
  return { ...sealed, event_hash: `sha256:${digest}` };
}

function pidAlive(pid) {
  if (!Number.isInteger(pid) || pid <= 0) return false;
  try {
    process.kill(pid, 0);
    return true;
  } catch (error) {
    return error?.code === "EPERM";
  }
}

// Hook side-channels share the library CLI's .catalog.lock. The CLI may repair
// events.jsonl from a full snapshot before appending; an unlocked hook append in
// that interval would otherwise be erased by the atomic rename.
function withLibraryLock(file, fn) {
  const root = path.dirname(file);
  fs.mkdirSync(root, { recursive: true });
  const lockPath = path.join(root, ".catalog.lock");
  const deadline = Date.now() + 5000;
  let fd = null;
  for (;;) {
    try {
      fd = fs.openSync(lockPath, "wx");
      fs.writeSync(fd, String(process.pid));
      break;
    } catch (error) {
      if (error?.code !== "EEXIST") throw error;
      try {
        const pid = Number.parseInt(fs.readFileSync(lockPath, "utf8").trim(), 10);
        const ageMs = Date.now() - fs.statSync(lockPath).mtimeMs;
        const reclaim = Number.isInteger(pid)
          ? (!pidAlive(pid) || ageMs > 300_000)
          : ageMs > 30_000;
        if (reclaim) fs.unlinkSync(lockPath);
      } catch {
        /* raced away or already gone */
      }
      if (Date.now() > deadline) throw new Error("catalog locked by another live writer");
      Atomics.wait(new Int32Array(new SharedArrayBuffer(4)), 0, 0, 50);
    }
  }
  try {
    return fn();
  } finally {
    try { fs.closeSync(fd); } catch { /* already closed */ }
    try {
      if (Number.parseInt(fs.readFileSync(lockPath, "utf8").trim(), 10) === process.pid) {
        fs.unlinkSync(lockPath);
      }
    } catch { /* gone */ }
  }
}

export function appendEvent(ev, input = null) {
  try {
    const file = eventsPath(input);
    // #3077: a repo with no library has no ledger to append to. Creating one on the first
    // denial would plant an orphan .household-library/ (plus its .catalog.lock) in a leaf
    // repo that no union-merge ever reaches. The denial itself stays loud on stderr; only
    // the ledger row is skipped, and the caller is told (returns false) so it can say so.
    // Env-overridden paths (tests, operator redirection) are always written.
    if (!process.env.HOUSEHOLD_BOOTSTRAP_EVENTS && !fs.existsSync(path.dirname(file))) return false;
    withLibraryLock(file, () => {
      const payload = sealIfChainStarted(
        {
          at: new Date().toISOString(),
          runtime: getRuntime(),
          repo: getRepoName(input),
          ...ev,
        },
        file,
      );
      fs.appendFileSync(file, JSON.stringify(payload) + "\n");
    });
    return true;
  } catch {
    /* ledger append is best-effort */
    return false;
  }
}

export function readStdinJson() {
  try {
    return JSON.parse(fs.readFileSync(0, "utf8"));
  } catch {
    return null;
  }
}

/** Layer path hit from a file path string. */
export function layerFromFilePath(fp, repoRoot = null) {
  const s = String(fp || "");
  if (!pathWithinAllowed(s, repoRoot)) return null; // a decoy suffix elsewhere on disk is not the layer
  for (const [key, suffix] of Object.entries(LAYER_SUFFIXES)) {
    if (s.endsWith(suffix)) return key;
  }
  // The Hermes home install (~/.hermes/skills/<name>/SKILL.md) is a genuine read of the
  // layer's canonical content, and the four layer skills match the generic suffixes above.
  // Kept as an explicit branch so the accepted homes are named, not inferred.
  if (s.includes(`${path.sep}.hermes${path.sep}skills${path.sep}sophos${path.sep}SKILL.md`)) {
    return "sophos";
  }
  if (s.includes(`${path.sep}.hermes${path.sep}skills${path.sep}soli-deo-gloria${path.sep}`)) {
    return "soli-deo-gloria";
  }
  if (s.includes(`${path.sep}.hermes${path.sep}skills${path.sep}careful-not-clever${path.sep}`)) {
    return "careful-not-clever";
  }
  if (s.includes(`${path.sep}.hermes${path.sep}skills${path.sep}household-library${path.sep}`)) {
    return "household-library";
  }
  // Also accept Grok home install copies of the front door.
  if (s.includes(`${path.sep}.grok${path.sep}skills${path.sep}sophos${path.sep}SKILL.md`)) {
    return "sophos";
  }
  if (s.includes(`${path.sep}.grok${path.sep}skills${path.sep}soli-deo-gloria${path.sep}`)) {
    return "soli-deo-gloria";
  }
  if (s.includes(`${path.sep}.grok${path.sep}skills${path.sep}careful-not-clever${path.sep}`)) {
    return "careful-not-clever";
  }
  if (s.includes(`${path.sep}.grok${path.sep}skills${path.sep}household-library${path.sep}`)) {
    return "household-library";
  }
  return null;
}

/**
 * A SKILL INVOCATION is a read of that skill's content — the Hermes runtime loads
 * layers through `skill_view(name)` rather than by file path, so without this the
 * agent can read every layer and still be denied. Only the four LAYER skills count;
 * an unrelated skill load credits nothing.
 *
 * Honest limit, same as every other credit here: this records that the content was
 * served into the session, not that the agent absorbed it. The Read-tool credit is
 * no stronger.
 */
export function layerFromSkillName(name) {
  const n = String(name || "").trim().toLowerCase();
  // Accept both the bare name and the qualified plugin form ("plugin:skill").
  const bare = n.includes(":") ? n.slice(n.lastIndexOf(":") + 1) : n;
  return Object.prototype.hasOwnProperty.call(LAYER_SUFFIXES, bare) ? bare : null;
}
