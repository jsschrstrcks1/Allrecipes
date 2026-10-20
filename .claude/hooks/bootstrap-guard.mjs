// @gate name=bootstrap-guard plane=harness event=PreToolUse Edit/Write/Bash via bootstrap-dispatch, every repo mutation until the seven Layer 0/1 files are read this session (reads expire after 24h) doc=docs/HOUSEHOLD-LOUD-BOOTSTRAP-REQUIREMENT.md#refusal-codes
// @gate-code hooks_path_unarmed: core.hooksPath is not .githooks, so git-plane liveness is not armed | remedy: set core.hooksPath=.githooks and run `node admin/gate-liveness.mjs --probe` in the guard's own repo | override: HOUSEHOLD_BOOTSTRAP_GUARD_BLOCK=0 (operator)
// @gate-code pre_commit_unavailable: the pre-commit hook could not be read | remedy: restore .githooks/pre-commit, then run `node admin/gate-liveness.mjs --probe`
// @gate-code receipt_missing_or_corrupt: no readable git-hook dispatch receipt | remedy: run `node admin/gate-liveness.mjs --probe` so Git's dispatcher writes the receipt
// @gate-code receipt_invalid: the receipt is not a valid dispatch record | remedy: run `node admin/gate-liveness.mjs --probe` to write a fresh receipt
// @gate-code receipt_unbound: the receipt belongs to a different checkout | remedy: run `node admin/gate-liveness.mjs --probe` in this checkout
// @gate-code receipt_stale: the dispatch receipt is outside its freshness window | remedy: run `node admin/gate-liveness.mjs --probe` to refresh it
// @gate-code BOOTSTRAP_STAMP_FORGED: the session stamp failed HMAC verification | remedy: discard the hand-written stamp and re-read the layers so the stamp hook writes the record
// @gate-code BOOTSTRAP_SESSION_ID: this session has no stable session_id | remedy: the runtime must supply session_id; do not invent a shared id
// @gate-code BOOTSTRAP_READS_EXPIRED: a layer was read, then aged past 24h | remedy: re-read the named layers with the Read tool; reading is never blocked
// @gate-code BOOTSTRAP_READS_FUTURE: a layer or step is dated more than 5 minutes ahead of this clock, so it is not credited (a future date would otherwise never age out) | remedy: re-read the named layers or re-run the named steps, and check the container clock
// @gate-code BOOTSTRAP_LAYERS_MISSING: a required layer has not been read this session | remedy: read the layers in the pointer file's read order, front door skills/sophos first
// @gate-code BOOTSTRAP_STEPS_MISSING: a required observed step has not been run | remedy: run the missing step the denial names (pointer, directives inject, claim-patron, or preflight)
// @gate-code BOOTSTRAP_READ_ORDER: a section 5-6 layer was read before section 0-4 | remedy: re-read in the pointer's read order
// @gate-code BOOTSTRAP_ALLOWANCE_MODULE_ABSENT: admin/operator-allowance.mjs is not in this repo | remedy: complete the read order, or ask the operator to vendor admin/operator-allowance.mjs and admin/gate-liveness.mjs
// @gate-code BOOTSTRAP_ALLOWANCE_UNRECORDABLE: an allowance is in force but its use could not be recorded | remedy: fix the uses file the denial names; the allowance is not honored until the use can be recorded
// @gate-exit 0: allowed. Also: not a household repo, not a mutation, an operator allowance whose use was recorded, warn-only when HOUSEHOLD_BOOTSTRAP_GUARD_BLOCK=0, or an internal error failing open
// @gate-exit 2: denied. stderr and the JSON decision print code=<slug> and name docs/GATE-REGISTRY.md
// bootstrap-guard.mjs — PreToolUse: loud half of household bootstrap (R2).
// Denies repo mutations when the session lacks a complete, HMAC-valid stamp.
// Dual-runtime: Claude Code + Grok (via normalizeHookInput).
// Escape hatch: HOUSEHOLD_BOOTSTRAP_GUARD_BLOCK=0 → warn-only.
// Spec: docs/HOUSEHOLD-LOUD-BOOTSTRAP-REQUIREMENT.md
// HLS: loud-bootstrap-impl-claude-code · loud-bootstrap-impl-grok
//
// SUPERSET NOTE (2026-09-25): open-claw-stuff canonical and Project-Sophos had each carried a
// real, independent fix the other lacked. Union-merged here, by content, not by which side is
// newer or bigger:
//   - from Project-Sophos (Finding 7, 2026-09-18): the gate-liveness check now assesses THIS
//     FILE'S OWN repository (OWN_REPO_ROOT), never the mutation's target repo. bootstrap-dispatch
//     can invoke a repo's guard to judge a DIFFERENT repo's mutation, and a guard can only
//     honestly attest to the git plane it lives on. Kept open-claw-stuff's SAFE dynamic-import
//     pattern for the recorder (fs.existsSync + await import + try/catch) rather than Project-
//     Sophos's static top-level import, which throws at load time in any leaf repo that has no
//     admin/gate-liveness.mjs — most of them — and would have made this file unusable there.
//   - from Project-Sophos (Finding 3): a liveness denial is now reachable from the SAME operator-
//     allowance escape hatch as a read-order denial. open-claw-stuff's liveness path denied
//     unconditionally, with the allowance check reachable only from the read-order path — a
//     denial whose own advertised remedy (arm the hooks) was itself blocked by the same denial,
//     the broken-escape-hatch shape.
//   - from open-claw-stuff (A8, 2026-09-12): FILE_MUTATION_TOOLS / MUTATION_VERB_RE census, so a
//     write from a runtime whose file tool isn't literally named Edit/Write/NotebookEdit is still
//     caught. Project-Sophos's isRepoMutation only recognized those three names plus Bash.
//   - from open-claw-stuff: SHELL_TOOLS recognizes Hermes's "terminal" and other shell aliases,
//     not just "Bash". Project-Sophos's version matched "Bash" only.
//   - from open-claw-stuff (#3431): the read-order denial names STALE (read, then expired)
//     separately from NEVER read, so a session isn't sent hunting for a layer it already read.
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";
// Imported defensively: leaf repos receive this file by copy (admin/onboard-loud-bootstrap.mjs
// HOOK_FILES), and a copy that arrives without its lib must not crash, because a PreToolUse hook
// that dies on MODULE_NOT_FOUND is treated as ALLOW (postmortem 2026-09-18, finding 6). Without the
// lib this guard keeps its own write patterns below, which is exactly its behaviour before the lib.
let bashWriteTargets = () => [];
let leadingCd = () => null;
try {
  ({ bashWriteTargets, leadingCd } = await import("./lib/bash-write-targets.mjs"));
} catch { /* leaf copy without lib/bash-write-targets.mjs: own patterns only */ }
import {
  getRepoRoot,
  isHouseholdRepo,
  verifyStamp,
  loadStamp,
  newStamp,
  saveStamp,
  missingLayers,
  missingFrontDoorSkill,
  missingActions,
  readOrderViolation,
  layerReadStatus,
  LAYER_READ_TTL_MS,
  appendEvent,
  readStdinJson,
  normalizeHookInput,
  sessionIdValid,
  resolveSessionId,
  effectiveStamp,
  judgeBootstrapSession,
  resolveGuardedSessionId,
  getRuntime,
  isGenuineRecall,
} from "./bootstrap-lib.mjs";

// Finding 7 (Project-Sophos, 2026-09-18). THIS GUARD MUST ONLY ATTEST TO ITS OWN REPOSITORY'S
// GIT PLANE. bootstrap-dispatch.mjs spawns the guard of every repo an event targets, but a guard
// that derives repoRoot from the PAYLOAD can end up assessing whatever repo a session's cwd
// happens to be, not the repo it actually lives in. Measured live (Project-Sophos): a session
// whose cwd was a different repo entirely had every mutation denied by Project-Sophos's own
// guard, reporting a receipt that repo had no way to produce. A guard can only honestly attest to
// the plane it lives on. Its own location is unambiguous; the payload's repo is not this guard's
// business for THIS check.
const OWN_REPO_ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..", "..");

// Verbs that are a repository mutation WHEREVER they point stay here: git history, in-place sed,
// library custody verbs, and the REMOVAL family (`rm`, `mv`, `truncate`, `chmod`, `chown`), which the
// suite pins as verb-blind by design (a named limit: a removal is judged by its verb, not its target).
// The COPY family (`tee`, `cp`, `install`, `dd of=`) is judged by writeTargetsInside() below, which
// resolves the target against the repo: `tee /tmp/x.log` and `cp a.md /tmp/` are not repo mutations,
// and were denied as such until 2026-10-11 (adversarial analysis L1.13: a test run piped into the
// scratchpad was refused). `release\b` used to match `release-name` too, which turned the documented
// remedy for self_quorum_friction into a denied command and closed the deadlock the lead met (L1.11).
const MUTATING_BASH_RE = new RegExp(
  [
    String.raw`\bgit\b[^|&;]*?\b(commit|push|merge|rebase|reset)\b`,
    // red-team finding 12: a path prefix, `command`, `sudo`, `env`, or `xargs` must not hide the verb.
    String.raw`(^|[;&|]\s*)(?:(?:command|sudo|nice|xargs)\s+|env\s+\S+\s+)*(?:\S*/)?(rm|mv|truncate|chmod|chown)\s`,
    String.raw`\bsed\s+-i\b`,
    String.raw`library\.mjs['"]?\s+(register|checkout|release(?!-name)|complete|verify|reassign)\b`,
  ].join("|"),
);

/** A quote-stripped token that looks like a filesystem target rather than a flag. */
function unquote(t) {
  const s = String(t || "");
  const m = s.match(/^(['"])(.*)\1$/);
  return m ? m[2] : s;
}

/**
 * red-team finding 12 (closed 2026-09-12): a redirect or a copy target writes into the repo without
 * ever naming `rm`/`mv`. The checklist requirement must bind that writer too, so any `>`/`>>`,
 * `tee`, or `cp`/`install`/`dd of=` target that resolves inside the repo is a repository mutation.
 */
function writeTargetsInside(command, repoRoot) {
  if (!repoRoot) return false;
  const s = String(command || "");
  const targets = [];
  for (const m of s.matchAll(/>>?\s*("[^"]+"|'[^']+'|[^\s;&|]+)/g)) targets.push(m[1]);
  for (const m of s.matchAll(/\btee\s+(?:-\S+\s+)*("[^"]+"|'[^']+'|[^\s;&|]+)/g)) targets.push(m[1]);
  for (const m of s.matchAll(/\b(?:cp|install)\s+(?:-\S+\s+)*(?:\S+\s+)+("[^"]+"|'[^']+'|[^\s;&|]+)/g)) targets.push(m[1]);
  for (const m of s.matchAll(/\bdd\s+[^;&|]*\bof=("[^"]+"|'[^']+'|[^\s;&|]+)/g)) targets.push(m[1]);
  // The shared extractor also reads python/node bodies (heredoc, -c, -e), which the patterns above
  // cannot see (HLS script-writers-bypass-write-guards-20260930: a python3 heredoc rewrote a hook in
  // the same batch where a Write to that worktree was refused). Unioned, so this guard and
  // hls-claim-guard cannot disagree about what one command writes.
  const base = leadingCd(s);
  for (const { target } of bashWriteTargets(s)) {
    targets.push(base && !path.isAbsolute(target) ? path.join(base, target) : target);
  }
  return targets
    .map((t) => unquote(t))
    .filter((t) => t && !/^[-&>]/.test(t) && !/^\/dev\//.test(t))
    .some((t) => insideRepo(path.isAbsolute(t) ? t : path.resolve(repoRoot, t), repoRoot));
}

function realOr(p) {
  const resolved = path.resolve(p);
  let ancestor = resolved;
  const suffix = [];
  for (;;) {
    try { return path.join(fs.realpathSync(ancestor), ...suffix); }
    catch (error) {
      if (error.code !== "ENOENT" && error.code !== "ENOTDIR") return resolved;
      const parent = path.dirname(ancestor);
      if (parent === ancestor) return resolved;
      suffix.unshift(path.basename(ancestor));
      ancestor = parent;
    }
  }
}

// Is `fp` inside `root`? Literal prefix first; then by REAL identity. #3077 landed this on
// its own probe: a repo reached through a symlinked prefix (macOS /var → /private/var,
// /tmp → /private/tmp) has its guard's module path resolved by Node to the REAL location,
// so the fallback repo root is the realpath while the tool input carries the alias — the
// literal comparison then reads an in-repo edit as out-of-repo and ALLOWS it. Same rule
// hls-claim-guard.mjs already applies (self-attack 2026-07-28). A not-yet-existing Write
// target resolves its nearest existing ancestor, preserving the missing suffix.
function insideRepo(fp, root) {
  const a = path.resolve(fp);
  const r = path.resolve(root);
  if (a.startsWith(r + path.sep)) return true;
  const ra = realOr(a);
  const rr = realOr(r);
  return ra === rr || ra.startsWith(rr + path.sep);
}

/** Every tool that can write into the tree, by every runtime's name for it. A8 (2026-09-12): the guard
 *  watched Bash and Claude's three file tools, and let every other writer walk. Measured live: while the
 *  guard denied `git commit`, `write_file` and `patch` wrote household files inside the repo in the same
 *  minutes. The rule was real for the shell and absent for the hand. A mutation is not a tool name; it is
 *  a write, and one boundary must judge them all. */
const FILE_MUTATION_TOOLS = new Set([
  "edit", "write", "notebookedit", "multiedit", "apply_patch", "applypatch",
  "write_file", "patch", "edit_file", "create_file", "delete_file", "move_file",
  "str_replace_editor", "str_replace", "insert_text", "append_file",
  "save_file", "rename_file", "remove_file", "copy_file", "upload_file",
]);

/** A name we have not met, judged by the verb it carries. The known set above is documentation; the
 *  mutation battery (2026-09-14) showed every name in it already matched the verb fallback, so the
 *  fallback is the teeth and the set is the census. `save`, `put`, `upload`, `store`, `rename`,
 *  `remove`, `copy`, `truncate`, `touch`, `mkdir`, `unlink`, `persist` were missing from the first cut:
 *  a `save_file` with a repo path walked past the guard. A name-based judgment can never be complete;
 *  the honest limit stays what it was, and the census grows every time a new runtime's writer is met. */
const MUTATION_VERB_RE = /(write|edit|create|delete|remove|move|rename|copy|patch|replace|append|insert|save|put|upload|store|truncate|touch|mkdir|unlink|persist)/i;

/** Reading is never a mutation, whatever the rest of the name says: `get_edit_history` with a repo path
 *  is a read, and this guard must never block a read (it would push the agent to the hatch). */
const READ_PREFIX_RE = /^(read|get|list|view|cat|show|search|find|grep|glob|open|stat|describe|inspect|preview|fetch|query|lookup)(_|$)/i;

function isFileMutationTool(tool) {
  const lower = String(tool || "").toLowerCase();
  if (!lower) return false;
  if (READ_PREFIX_RE.test(lower)) return false;
  return FILE_MUTATION_TOOLS.has(lower) || MUTATION_VERB_RE.test(lower);
}

/** The shell, by every runtime's name for it. `terminal` included: it is what Hermes calls its shell,
 *  and it was unguarded until now. */
const SHELL_TOOLS = new Set(["bash", "shell", "shell_command", "exec", "exec_command", "run_terminal_cmd", "terminal"]);

function fileTargetOf(input) {
  const t = input.tool_input || {};
  return String(
    t.file_path || t.filePath || t.path || t.notebook_path || t.notebookPath || t.target_file || t.filename || "",
  );
}

// Finding 7 scopes the git-plane refusal to mutations of THIS repository, but judged that by the
// session's tree (getRepoRoot reads cwd). The mutation's own target is the better evidence: a Bash
// command that cds into this repository from another tree mutates THIS plane whatever the session's
// cwd. Mirrored from Project-Sophos #843 (bootstrap-guard-self-root S3, red there from #738 until the
// fix). It only ADDS cases where liveness is assessed; a truly foreign target stays unjudged (S6).
// Named limits: `git -C <dir>` and a cd later in the chain are not read; and an edit tool whose path
// is inside this repository while the session sits elsewhere never reaches here, because
// isRepoMutation() judges it against the session's tree and exits first (a design decision, not a repair).
function mutationTargetsOwnPlane(input, repoRoot) {
  if (!SHELL_TOOLS.has(String(input.tool_name || "").toLowerCase())) return false;
  const cd = leadingCd(String(input.tool_input?.command || input.tool_input?.cmd || ""));
  const base = repoRoot || OWN_REPO_ROOT;
  return Boolean(cd) && insideRepo(path.isAbsolute(cd) ? cd : path.resolve(base, cd), OWN_REPO_ROOT);
}

function isRepoMutation(input, repoRoot) {
  const tool = String(input.tool_name || "");
  const lower = tool.toLowerCase();

  if (SHELL_TOOLS.has(lower)) {
    const cmd = String(input.tool_input?.command || input.tool_input?.cmd || "");
    if (MUTATING_BASH_RE.test(cmd)) return true;
    return writeTargetsInside(cmd, repoRoot);
  }

  const fp = fileTargetOf(input);

  // Claude's original three, kept explicit so their behavior never depends on the census or the verbs.
  if (tool === "Edit" || tool === "Write" || tool === "NotebookEdit") {
    if (!fp || !repoRoot) return false;
    return insideRepo(fp, repoRoot);
  }

  // Every other writer, by census or by verb, judged by its payload: a runtime we have never seen
  // should not need us to have heard of it first.
  if (isFileMutationTool(tool)) {
    if (!fp || !repoRoot) return false;
    return insideRepo(fp, repoRoot);
  }
  return false;
}

function codeSuffix(codes) {
  const list = [...new Set((codes || []).filter(Boolean))];
  const token = list.length ? `code=${list.join(" code=")}\n` : "";
  return `${token}Key: docs/GATE-REGISTRY.md`;
}

function deny(blocking, msg) {
  console.error(msg);
  // Grok: JSON decision; Claude: exit 2. Both runtimes honor exit 2 on PreToolUse.
  if (blocking) {
    try {
      process.stdout.write(JSON.stringify({ decision: "deny", reason: msg }) + "\n");
    } catch {
      /* ignore */
    }
    process.exit(2);
  }
  process.exit(0);
}

function denyCoded(blocking, msg, codes) {
  deny(blocking, `${msg}\n${codeSuffix(codes)}`);
}

// The ONE release valve, read by EVERY runtime's guard adapter (A7, 2026-09-12), reachable from
// EVERY deny path in this file (Project-Sophos Finding 3, 2026-09-18: open-claw-stuff's liveness
// denial used to call deny() directly, with no allowance check reachable from that path at all —
// so a liveness denial whose own advertised remedy is "arm the hooks", itself a mutation, could
// never be worked around even with a genuine, signed operator allowance in force). Consulted only
// AFTER a verdict is already deny, so it can only ever be a named, signed, expiring, scope-narrow
// operator record, never a bypass chosen ahead of the check.
//
// A REMEDY THE AGENT CAN PERFORM (HLS bootstrap-guard-names-an-impossible-remedy-when-a-layer-is-
// unreachable; probed INERT by syl 2026-09-08). In a guarded leaf cloned alone, six of the seven
// layer files exist nowhere on disk, and the denial still said "Read the layers in CLAUDE.md read
// order": an instruction that cannot be carried out, whose only exit is the switch agents may not
// touch. The VERDICT does not change here: an unreachable layer is still unread, and passing it
// would be a bypass wearing a fix's clothes. Only what the denial SAYS changes.
//
// It asks admin/layer-reachability.mjs, the household's one answer to "could this repo reach
// Layer 0 at all?", and looks for it without assuming it is local: a leaf repo carries this guard
// but no admin/. Three outcomes, never two: every missing layer reachable (the old remedy is real,
// and the lines say where each copy is); some UNREACHABLE (say so, and name the remedy that works);
// the tool itself not found (say reachability was NOT checked, never imply it was).
async function layerRemedyLines(repoRoot, missing, pointer, env = process.env) {
  const standard = `Read the layers in ${pointer} §Read order (front door skills/sophos first); the stamp hook records reads automatically.`;
  const fileBacked = missing.filter((m) => m !== "memory-recall");
  if (!fileBacked.length) return [standard];
  const candidates = [
    path.join(repoRoot, "admin", "layer-reachability.mjs"),
    path.join(OWN_REPO_ROOT, "admin", "layer-reachability.mjs"),
    ...["HOUSEHOLD_OCS_ROOT", "HOUSEHOLD_RUNTIME_ROOT"].filter((k) => env[k]).map((k) => path.join(env[k], "admin", "layer-reachability.mjs")),
    path.join(repoRoot, "..", "open-claw-stuff", "admin", "layer-reachability.mjs"),
  ];
  let lib = null;
  for (const c of candidates) {
    try {
      if (!fs.existsSync(c)) continue;
      lib = await import(pathToFileURL(c).href);
      if (typeof lib.reachability === "function") break;
      lib = null;
    } catch { lib = null; }
  }
  const setEnv = "clone open-claw-stuff (and Project-Sophos, for sophos-os) beside this repo, or point HOUSEHOLD_OCS_ROOT / HOUSEHOLD_SOPHOS_ROOT at existing clones";
  if (!lib) {
    return [
      standard,
      `Layer reachability was NOT checked: admin/layer-reachability.mjs is not reachable from ${repoRoot}. If a missing layer has no copy on this machine, reading cannot satisfy it: ${setEnv}, then read. If that is not possible here, ask the operator.`,
    ];
  }
  let r;
  try { r = lib.reachability(repoRoot, { env }); }
  catch (e) { return [standard, `Layer reachability could not be computed (${e?.message || e}); not checked is not reachable.`]; }
  const unreachable = fileBacked.filter((m) => r.layers?.[m]?.state === "UNREACHABLE");
  const reachable = fileBacked.filter((m) => r.layers?.[m]?.state === "reachable");
  const lines = [];
  if (reachable.length) {
    lines.push(`Read the layers in ${pointer} §Read order (front door skills/sophos first); these have a copy you can read: ` +
      reachable.map((m) => `${m} at ${r.layers[m].at}`).join("; ") + ".");
  }
  if (unreachable.length) {
    const searched = unreachable.reduce((n, m) => n + (r.layers[m].searched?.length || 0), 0);
    lines.push(`UNREACHABLE from here: ${unreachable.join(", ")}. No copy exists anywhere this guard can see (${searched} places searched), so reading cannot satisfy them, and the denial stands because passing an unread layer would be a bypass.`);
    lines.push(`Remedy that works: make Layer 0 reachable: ${setEnv}; then read them. If that is not possible here, ask the operator.`);
  }
  return lines.length ? lines : [standard];
}

// THE USE IS RECORDED BEFORE IT IS HONORED (2026-09-14). The first cut wrote a ledger row after the
// fact and never read it back, so a one-use allowance stayed open for its whole window; and it said a
// failed record was "not a failure to allow", which turns a key into a door the moment the record
// cannot be written. Now: recordUse() beside the grant first; if THAT fails, the denial stands and
// says why. The HLS ledger row is the second tie, best-effort and reported, never the permission.
async function denyUnlessAllowed(blocking, msg, ctx) {
  // WHICH REPO'S LEDGER, named explicitly by the caller (independent review of open-claw-stuff PR
  // #3860, 2026-09-26): this used to hardcode OWN_REPO_ROOT for both call sites. Finding 7's own
  // rationale for OWN_REPO_ROOT was specific to LIVENESS -- a guard can only honestly attest to the
  // git plane it lives on -- and says nothing about which repo's allowance ledger should satisfy a
  // READ-ORDER override, a SESSION-level fact (the stamp lives in a household-shared location, not
  // per-repo) about the mutation's actual TARGET repo, repoRoot. Silently unifying both onto
  // OWN_REPO_ROOT during the Finding-7/Finding-3 merge was an untested generalization neither
  // finding asked for: in the ordinary single-repo case OWN_REPO_ROOT === repoRoot so it never
  // showed, but in the multi-root dispatch case this file's own comments already name as real (one
  // repo's guard judging another's mutation), it silently widened what a single grant covers or
  // silently orphaned a grant filed against the mutation's real target. Falls back to OWN_REPO_ROOT
  // only if a caller omits ctx.root, so no existing call site can regress by accident.
  const allowanceRoot = ctx.root || OWN_REPO_ROOT;
  let allowance = { allowed: false, why: "not consulted" };
  let mod = null;
  let moduleAbsent = false;
  try {
    mod = await import("../../admin/operator-allowance.mjs");
    allowance = mod.allowanceFor({ scope: "bootstrap-guard", root: allowanceRoot });
  } catch (e) {
    // Named by an independent reviewer of manateecreeksheep PR #90 (2026-09-26): a leaf repo that
    // carries this guard but never received admin/operator-allowance.mjs got told, in every single
    // denial, to run a command guaranteed to fail with the identical "Cannot find module" error —
    // the escape hatch this message exists to advertise was itself a dead end there. The guard's
    // own DECISION was never wrong (deny stands either way, correctly fail-closed), but a remedy
    // that cannot be taken is not a remedy, the same class of defect the read-order denial message
    // was already fixed for (bootstrap-guard-names-an-impossible-remedy-when-a-layer-is-unreachable).
    // Distinguish "the module genuinely is not here" from any other allowance-check failure, and
    // stop advertising a command specific to the absent case.
    moduleAbsent = e?.code === "ERR_MODULE_NOT_FOUND";
    allowance = { allowed: false, why: `allowance check unavailable: ${e?.message || e}` };
  }
  if (!(allowance.allowed && allowance.record && mod)) {
    const codes = Array.isArray(ctx.codes) ? ctx.codes : [];
    denyCoded(
      blocking,
      moduleAbsent
        ? `${msg}\nThis repository has no admin/operator-allowance.mjs, so no operator allowance can be granted or read here at all — the module genuinely is not present, not merely empty. ` +
          "Running the grant command below would fail with the same \"Cannot find module\" error this denial hit; it is not offered as a remedy. " +
          "Complete the read order this denial names instead, or ask whoever holds admin/ tooling access on this repo to vendor admin/operator-allowance.mjs and admin/gate-liveness.mjs from the canonical."
        : `${msg}\nNo operator allowance is in force for this scope (${allowance.why}).\n` +
          "Operator consent, read by EVERY runtime (no per-runtime hatch):\n" +
          `  node admin/operator-allowance.mjs grant --scope bootstrap-guard --by <you> --reason "<20+ chars>" --expires-in 60${allowanceRoot !== OWN_REPO_ROOT ? ` (run in ${allowanceRoot})` : ""}\n` +
          "  Signed, scope-narrow, single-use by default; every use is recorded beside the grant and, where a ledger exists, on it. A chat allowance is not one: this guard reads a record, not a conversation.",
      moduleAbsent ? [...codes, "BOOTSTRAP_ALLOWANCE_MODULE_ABSENT"] : codes,
    );
  }
  const use = mod.recordUse(allowanceRoot, allowance.record, ctx.context || {});
  if (!use.ok) {
    // No `return` after this: deny() always calls process.exit() and never returns, so a trailing
    // return here was unreachable dead code (independent review of open-claw-stuff PR #3860,
    // 2026-09-26) -- harmless, but it read like a fall-through guard against a case that cannot occur.
    denyCoded(
      blocking,
      `${msg}\nAn operator allowance (${allowance.record.id}, by ${allowance.record.by}) is in force but its use could not be recorded (${use.why}). An allowance that cannot be marked spent is a door left open, so it is not honored.`,
      [...(Array.isArray(ctx.codes) ? ctx.codes : []), "BOOTSTRAP_ALLOWANCE_UNRECORDABLE"],
    );
  }
  let ledgered = null;
  try {
    ledgered = appendEvent(
      {
        type: "bootstrap_guard_allowance_used",
        session_id: ctx.context?.session_id,
        denied_tool: ctx.context?.denied_tool,
        allowance_id: allowance.record.id,
        allowed_by: allowance.record.by,
        allowed_reason: allowance.record.reason,
        use_number: (allowance.spent || 0) + 1,
        uses: allowance.uses,
        gate: ctx.gate,
        ...(ctx.context?.missing_layers ? { missing_layers: ctx.context.missing_layers } : {}),
      },
      ctx.raw,
    );
  } catch {
    ledgered = false;
  }
  deny(
    false,
    `BOOTSTRAP GUARD: allowed by operator allowance ${allowance.record.id}, by ${allowance.record.by}: ` +
      `${allowance.record.reason} (gate: ${ctx.gate}, use ${(allowance.spent || 0) + 1} of ${allowance.uses}, ` +
      `recorded in ${use.file}${ledgered ? "" : "; no HLS ledger here, so no ledger row"}).`,
  );
}

try {
  const raw = readStdinJson();
  const input = normalizeHookInput(raw);
  if (!input) process.exit(0);

  const repoRoot = getRepoRoot(input.raw || input);
  // Outside household repos: no belt (Grok may be in ~/ unrelated work).
  if (!isHouseholdRepo(repoRoot)) process.exit(0);

  if (!isRepoMutation(input, repoRoot)) process.exit(0);

  // A GUARD NEVER GATES ITS OWN REMEDY (p1-guard-never-gates-its-own-remedy, 2026-10-01, 4th
  // occurrence). The expired-posture denial names memory-recall as the remedy, but this guard never
  // consulted RECALL_CMD_RE (only the stamp hook did), so the recall itself was denied and the
  // posture could never be refreshed. Genuine recall commands and Reads of the seven layer paths are
  // the remedy for EVERY first-read/expiry denial, so they are exempt BEFORE the denial, regardless
  // of cwd or stamp state. Reading is never blocked by this gate; only the denial verdict changes.
  if (input.tool_name === "Bash") {
    if (isGenuineRecall(String(input.tool_input?.command || ""))) process.exit(0);
  }
  if (input.tool_name === "Read" || input.tool_name === "read_file") {
    const fp = String(input.tool_input?.file_path || "");
    const base = fp.split("/").pop() || "";
    // The six file-backed layer paths (LAYER_SUFFIXES in bootstrap-lib.mjs) plus any pointer file.
    const isLayerRead = /^skills\/soli-deo-gloria\/SKILL\.md$/i.test(fp) ||
      /^skills\/careful-not-clever\/SKILL\.md$/i.test(fp) ||
      /^skills\/sophos\/SKILL\.md$/i.test(fp) ||
      /^docs\/SOPHOS-OPERATING-SYSTEM\.md$/i.test(fp) ||
      /^docs\/HOUSEHOLD-AGENT-RULEBOOK\.md$/i.test(fp) ||
      /^skills\/household-library\/SKILL\.md$/i.test(fp) ||
      /^(?:HERMES|CLAUDE|GROK|AGENT)\.md$/i.test(base);
    if (isLayerRead) process.exit(0);
  }

  const blocking = process.env.HOUSEHOLD_BOOTSTRAP_GUARD_BLOCK !== "0";

  // P1 gate liveness (Project-Sophos #114, ported 2026-09-15; assessed against OWN_REPO_ROOT per
  // Finding 7, 2026-09-18 — see the note at the top of this file): configuration alone is not
  // evidence that Git dispatches the tracked hooks. A corrupt, foreign, absent, or stale RECEIPT
  // denies just like a missing bootstrap layer; the remedy (an inert probe through git's
  // dispatcher) is reachable through the SAME allowance escape hatch as every other denial in this
  // file. The receipt is written by .githooks/pre-commit on Git dispatch, not by this guard, so
  // this gate does not certify its own plane. The recorder is loaded from THIS guard's own repo,
  // dynamically and defensively (open-claw-stuff's pattern, kept over Project-Sophos's static
  // top-level import): a static import of admin/gate-liveness.mjs throws at module-load time in
  // any leaf repo that carries this guard but not that recorder — most of them — which would make
  // the whole guard unusable there rather than reporting the honest, narrow "not assessed" limit.
  // Two cases are NAMED on stderr and skipped rather than denied, because denying them would block
  // the only remedy (an edit) and make the gate unsatisfiable (UL-349): a leaf that carries this
  // guard but no admin/gate-liveness.mjs, and a recorder that does not load (measured 2026-09-15:
  // a half-edited recorder denied the edit that would have finished it).
  {
    // Finding 7: this guard may only attest to OWN_REPO_ROOT's git plane. A mutation that
    // targets a different checkout must not be refused because THIS plane is unarmed.
    const sessionOnOwnPlane = realOr(repoRoot) === OWN_REPO_ROOT;
    const mutationOnOwnPlane = sessionOnOwnPlane || mutationTargetsOwnPlane(input, repoRoot);
    const recorder = path.join(OWN_REPO_ROOT, "admin", "gate-liveness.mjs");
    if (!mutationOnOwnPlane) {
      // named limit, not a pass: foreign mutation is not judged by this plane's dispatch receipt
    } else if (!fs.existsSync(recorder)) {
      console.error(`bootstrap-guard: no admin/gate-liveness.mjs under ${OWN_REPO_ROOT}; git-plane liveness NOT assessed here (named limit, not a pass).`);
    } else {
      let liveness = null;
      try {
        const mod = await import(recorder);
        liveness = mod.assessGateLiveness(OWN_REPO_ROOT);
      } catch (e) {
        console.error(`bootstrap-guard: admin/gate-liveness.mjs under ${OWN_REPO_ROOT} does not load (${String(e?.message || e).slice(0, 100)}); git-plane liveness NOT assessed here (named limit, not a pass). Fix the recorder; that edit is not blocked.`);
      }
      if (liveness && !liveness.live) {
        await denyUnlessAllowed(
          blocking,
          [
            `BOOTSTRAP GUARD: git-plane liveness is ${liveness.reason} for ${OWN_REPO_ROOT}; a configured hook is not proof it fired.`,
            `Denied: ${input.tool_name}: ${input.tool_input?.file_path || input.tool_input?.command || ""}`,
            // Say which repo to repair. Naming "this repository" while assessing a different one
            // (the pre-Finding-7 shape) sends whoever reads it to probe a repo that was never the
            // subject. Compared through realOr() (independent review of open-claw-stuff PR #3860,
            // 2026-09-26), not a bare path.resolve(): this exact file already carries realOr()/
            // insideRepo() for the identical reason (#3077, macOS /tmp -> /private/tmp) a few dozen
            // lines above, and the bare comparison reproduced that same false mismatch here --
            // Node's ESM loader resolves OWN_REPO_ROOT through the symlink while a payload's raw
            // cwd string never is, so an entirely ordinary single-repo /tmp checkout printed a false
            // "targets a different plane" NOTE on every denial. Message-only, never the verdict, but
            // exactly the "claims more than it can back up" class this file's own doctrine refuses.
            // Since the cd read above this NOTE can actually fire (before it, a session outside this
            // repo never reached here). The session's tree is not the mutation's target; say so.
            ...(sessionOnOwnPlane
              ? []
              : [`NOTE: the session's working tree is ${repoRoot}; the mutation targets this guard's own plane (${OWN_REPO_ROOT}), and this guard attests only to its own plane.`]),
            ...(liveness.remedy ? [liveness.remedy] : []),
            `Run \`node admin/gate-liveness.mjs --probe\` in ${OWN_REPO_ROOT}. It uses Git's hook dispatcher with an inert probe and requires core.hooksPath=.githooks. Reading is never blocked by this gate.`,
          ].join("\n"),
          {
            gate: "git_plane_liveness",
            root: OWN_REPO_ROOT,
            raw: input.raw || input,
            codes: [liveness.reason],
            context: {
              session_id: resolveSessionId(input),
              denied_tool: input.tool_name,
              liveness_reason: liveness.reason,
            },
          },
        );
      }
    }
  }

  const idValid = sessionIdValid(input.session_id);
  // Prefer payload session id; after compact/model-swap follow stamp-hook's last-credited
  // pointer when that stamp is complete+fresh (bootstrap-dispatch-guard-blocks-all-session-writes).
  const guarded = resolveGuardedSessionId(input.raw || input, { repoRoot });
  const sessionId = guarded.sessionId;
  if (guarded.remapped) {
    console.error(
      `bootstrap-guard: session id remapped ${guarded.from} → ${sessionId} via last-credited ` +
      `(at ${guarded.last_at}) — payload stamp incomplete after compact/model-swap; stamp-writer kept the prior id.`,
    );
  }
  // ONE verifier signature with bootstrap-status (judgeBootstrapSession). Sub-agent keys still
  // inherit parent reads READ-ONLY via effectiveStamp inside the judge; denial bookkeeping
  // below still writes to the child's own stamp.
  const verdict = judgeBootstrapSession(sessionId, input.raw || input, { repoRoot });
  const stamp = verdict.stamp;
  // missingLayers / missingActions / readOrderViolation already treat null|"forged" as
  // fully-missing (loud). Do NOT short-circuit to [] — that prints "missing: none" while
  // still denying (false-incomplete land ternary; measured red on allowance + unreachable suites).
  const missing = missingLayers(stamp);
  // Belt 2: the Hermes front-door skill (sophos-household) must be loaded before any
  // mutation. Scoped to the Hermes runtime only. This is the enforcement half of the
  // belt-and-suspenders pair — the Hermes plugin injects "load sophos-household first"
  // (belt 1); this guard refuses a Hermes mutation until the skill was actually loaded.
  const missingFrontDoor = missingFrontDoorSkill(stamp, getRuntime());
  const missingSteps = missingActions(stamp, repoRoot);
  const orderProblem = stamp && stamp !== "forged" ? readOrderViolation(stamp) : null;
  const readStatus = layerReadStatus(stamp);

  if (idValid && verdict.complete && !missingFrontDoor) {
    // Bootstrapped — allow (Grok optional explicit allow).
    if (getRuntime() === "grok") {
      try {
        process.stdout.write(JSON.stringify({ decision: "allow" }) + "\n");
      } catch {
        /* ignore */
      }
    }
    process.exit(0);
  }

  const forged = stamp === "forged";
  const toolDesc =
    input.tool_name === "Bash"
      ? `Bash: ${String(input.tool_input?.command || "").slice(0, 120)}`
      : `${input.tool_name}: ${input.tool_input?.file_path || ""}`;

  // The verdict is already settled above: this is a guarded mutation whose stamp
  // was not affirmatively verified, so it WILL be denied. Everything from here to
  // saveStamp is BOOKKEEPING, and bookkeeping must never be able to turn that
  // denial into permission. Without this boundary an I/O failure here escapes to
  // the outer catch, which exits 0 (allow) — and because stampRoot() lives outside
  // repoRoot while isRepoMutation() only guards Write/Edit paths INSIDE repoRoot,
  // the guard's own state is unguarded, so a single `chmod` on the stamp dir
  // disarmed the guard for the rest of the session (measured DENIED -> ALLOWED,
  // persisting across further Writes and a `git commit`).
  // A failure to RECORD a denial is not consent to proceed.
  // HLS p1-guard-found-validating-p0-read-order-enforcement… / open-claw-stuff#2727;
  // same class as guard-hook-fail-open-on-error and hls-p0-the-c5-guard-fails-open.
  let ledgered = null; // null = not attempted (cap reached); false = skipped/failed; true = written
  try {
    let counter = loadStamp(sessionId, input.raw || input);
    if (!counter || typeof counter !== "object") {
      counter = newStamp(sessionId, input.raw || input);
    }
    if (forged) {
      counter = newStamp(sessionId, input.raw || input);
      counter.forge_detected = true;
    }
    counter.denials = (counter.denials || 0) + 1;
    // red-team finding 17 (closed 2026-09-12): the order violation lived only in the guard's message and
    // in the stamp, and the stamp is deletable. Record it on the append-only ledger and in the counter,
    // so erasing the stamp cannot erase the evidence.
    if (orderProblem) {
      counter.order_violation = orderProblem;
      counter.order_violation_at = new Date().toISOString();
    }
    if (counter.denials <= 3) {
      ledgered = appendEvent(
        {
          type: "bootstrap_guard_denial",
          patron: counter.patron,
          session_id: sessionId,
          denied_tool: input.tool_name,
          missing_layers: missing,
          forged,
          blocked: blocking,
          sessionid_invalid: !idValid,
          ...(orderProblem ? { order_violation: orderProblem } : {}),
        },
        input.raw || input,
      );
    }
    saveStamp(counter, input.raw || input);
  } catch (bookkeepingError) {
    // Loud, but never fatal to the verdict — fall through to deny().
    console.error(
      `bootstrap-guard: denial bookkeeping failed (${bookkeepingError?.message || bookkeepingError}) — denying anyway. A failure to record a denial must never become permission to proceed.`,
    );
  }

  const pointer = getRuntime() === "grok" ? "GROK.md" : "CLAUDE.md";
  const expiredOnly = readStatus.stale.length && !readStatus.never.length && missingSteps.length === 0 && !orderProblem && !missingFrontDoor;
  const readOrderDenial = !forged && idValid && !expiredOnly;
  const refusalCodes = forged
    ? ["BOOTSTRAP_STAMP_FORGED"]
    : !idValid
      ? ["BOOTSTRAP_SESSION_ID"]
      : expiredOnly
        ? ["BOOTSTRAP_READS_EXPIRED"]
        : [
            readStatus.never.length ? "BOOTSTRAP_LAYERS_MISSING" : null,
            readStatus.stale.length ? "BOOTSTRAP_READS_EXPIRED" : null,
            (readStatus.future || []).length ? "BOOTSTRAP_READS_FUTURE" : null,
            missingSteps.length ? "BOOTSTRAP_STEPS_MISSING" : null,
            orderProblem ? "BOOTSTRAP_READ_ORDER" : null,
            missingFrontDoor ? "BOOTSTRAP_FRONT_DOOR_SKILL_MISSING" : null,
          ].filter(Boolean);
  const standardRemedy = `Read the layers in ${pointer} §Read order (front door skills/sophos first); the stamp hook records reads automatically.`;
  let remedy = [standardRemedy];
  // Its own try: the outer catch of this file FAILS OPEN, so a throw from wording code would turn a
  // denial into an allow. A remedy that cannot be computed falls back to the old line, never to a pass.
  if (readOrderDenial) {
    try { remedy = await layerRemedyLines(repoRoot, missing, pointer); }
    catch (e) { remedy = [standardRemedy, `(layer reachability not checked: ${e?.message || e})`]; }
  }
  // EVERY CODE CARRIES ITS OWN KEY (adversarial analysis 2026-10-11, L1.8 / lane A A15): the denial
  // used to print the LAYERS remedy for a STEPS_MISSING or READ_ORDER refusal, so an agent whose
  // layers were all read was told to read them again. Each code now names its own next action.
  const stepRemedy = {
    pointer: `Read ${pointer} at the repo root with the Read tool (or cat it).`,
    directives_inject: "Run: bash .claude/hooks/memory-directives-inject.sh   (or: python3 admin/memory_evidence.py directives)",
    claim_patron: "Run, as its own command, not after an echo: node admin/library.mjs claim-patron   (a refusal still counts as run; see release-name if a name is held)",
    preflight: 'Run: node admin/library.mjs preflight --query "<task>" --patron <you> --merge --repo <repo>',
  };
  if (readOrderDenial && !readStatus.never.length && !readStatus.stale.length && !(readStatus.future || []).length) {
    remedy = []; // the layers are not the problem; do not send the agent to re-read them
  }
  if (missingSteps.length) {
    remedy.push(`Missing steps are satisfied by RUNNING them (code=BOOTSTRAP_STEPS_MISSING):`);
    for (const s of missingSteps) if (stepRemedy[s]) remedy.push(`  - ${s}: ${stepRemedy[s]}`);
  }
  if ((readStatus.future || []).length) {
    remedy.push(`Future-dated reads are not credited (${readStatus.future.join(", ")} are dated more than 5 minutes ahead of this clock): re-read them, and check the container clock.`);
  }
  if (orderProblem) {
    remedy.push("Read order (code=BOOTSTRAP_READ_ORDER): re-read ALL layers in the pointer's order, Soli Deo Gloria first, library last; the violation clears only after a full in-order re-read.");
  }
  if (missingFrontDoor) {
    remedy.push("Front-door skill (code=BOOTSTRAP_FRONT_DOOR_SKILL_MISSING): load the `sophos-household` skill with skill_view before any mutation. It is the procedure that prevents improvise-and-stall; the Hermes plugin injects this reminder, and this guard enforces it.");
  }
  const msg = [
    forged
      ? "BOOTSTRAP GUARD: stamp failed HMAC verification — a hand-written stamp is testimony, not evidence (spec R1/R5). Forgery is itself a governance finding."
      : !idValid
        ? "BOOTSTRAP GUARD: this session has no stable session_id, so its bootstrap cannot be attributed — a shared `unknown` stamp would let any un-read session inherit another's reads. Refusing (loud-bootstrap-sessionid-contract). The runtime must supply session_id, or use the escape hatch."
        : expiredOnly
          // #3431: telling an agent to read what it demonstrably DID read sends it hunting for a
          // file it already has. Name the decay instead: these were read, and then aged out.
          ? `BOOTSTRAP GUARD: this session's posture reads have EXPIRED (stale: ${readStatus.stale.join(", ")}). They were read, but more than ${Math.round(LAYER_READ_TTL_MS / 3600000)}h ago, so they no longer govern this session. Re-read them; reading is never blocked by this guard.`
          : `BOOTSTRAP GUARD: this session has not completed the Layer 0/1 read order (missing: ${missing.join(", ") || "none"}${readStatus.stale.length ? `; of those, EXPIRED rather than unread: ${readStatus.stale.join(", ")}` : ""}${(readStatus.future || []).length ? `; of those, FUTURE-dated rather than unread: ${readStatus.future.join(", ")}` : ""}; missing steps: ${missingSteps.join(", ") || "none"}${orderProblem ? `; ${orderProblem}` : ""}${missingFrontDoor ? `; front-door skill (sophos-household) not loaded` : ""}).`,
    `Denied: ${toolDesc}`,
    // #3077: a leaf repo (Project-Sophos, the recipe repos) carries the guard but no library, so
    // there is no ledger to append to — say so rather than let a missing row read as "no denial".
    ...(ledgered === false
      ? [`Denial NOT ledgered: the ledger for ${repoRoot} is absent or could not be written — this message is the record.`]
      : []),
    ...remedy,
    "Operator warn-only switch, where the harness passes env: HOUSEHOLD_BOOTSTRAP_GUARD_BLOCK=0. Spec: docs/HOUSEHOLD-LOUD-BOOTSTRAP-REQUIREMENT.md",
  ].join("\n");

  await denyUnlessAllowed(blocking, msg, {
    gate: "read_order",
    root: repoRoot,
    raw: input.raw || input,
    codes: refusalCodes.length ? refusalCodes : ["BOOTSTRAP_LAYERS_MISSING"],
    context: { session_id: sessionId, denied_tool: input.tool_name, missing_layers: missing },
  });
} catch (e) {
  console.error(
    `bootstrap-guard: internal error, failing OPEN (named limit — guard bugs must not brick sessions): ${e?.message || e}`,
  );
  process.exit(0);
}
