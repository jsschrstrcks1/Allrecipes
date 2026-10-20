// bash-write-targets.mjs — which files does this shell command WRITE?
//
// The HLS claim guard used to look only at Edit|Write|NotebookEdit, so a `printf > file`, a
// heredoc, `tee`, `cp`, `sed -i` or `rm` walked straight past a claim another live actor held
// (#3585, measured 2026-09-14: the same path denied to the Write tool and allowed to printf in
// the same minute). This extractor names the targets of the write shapes a shell command can
// carry on its face. It is deliberately a whitelist of shapes, and it names its own limit: a
// path built from a shell variable or command substitution is NOT seen. A shape it cannot see is
// reported as nothing, never as "safe".
//
// Interpreter bodies ARE read now (HLS script-writers-bypass-write-guards-20260930, P0): a python
// or node program handed over as a heredoc (`python3 - <<'EOF'`), `-c`, `-e`/`-p`/`--eval` writes
// files the Write/Edit guards never see. Measured 2026-09-30: a python3 heredoc rewrote a git hook
// in the same batch where a Write to that worktree was being refused, and two PRs' code was written
// that way unseen. Only the BODY handed to the interpreter is read, so a commit message or a grep
// pattern that merely quotes `open('x','w')` is not a write (mention is not use). A target is a
// string literal, or a name the same body assigned string literals to (every such literal counts,
// erring toward seeing). Still unseen: paths computed at run time (joins, f-strings, arguments),
// and interpreters other than python and node.
//
// Returns [{ target, verb }] with the raw (unquoted) token; the caller resolves paths.

/** Strip one layer of shell quoting from a token. */
export function unquoteToken(tok) {
  const s = String(tok || "").trim();
  if (s.length >= 2 && ((s[0] === '"' && s.endsWith('"')) || (s[0] === "'" && s.endsWith("'")))) {
    return s.slice(1, -1);
  }
  return s;
}

const TOKEN = String.raw`("[^"]+"|'[^']+'|[^\s;&|<>()]+)`;
const FLAG = /^-/;

// A target token the shell would not treat as a file: a flag, a fd dup (`>&2`), a variable or
// substitution we cannot resolve, or a device. Skipped, and the skip is the named limit above.
function usable(tok) {
  const t = unquoteToken(tok);
  if (!t || FLAG.test(t)) return false;
  if (t.startsWith("&")) return false;
  if (/[$`]/.test(t)) return false;
  if (t.startsWith("/dev/")) return false;
  return true;
}

/** Split a command on the operators that end a simple command, keeping each piece's text. */
function simpleCommands(command) {
  return String(command || "")
    .split(/\n|;|&&|\|\||\|/)
    .map((s) => s.trim())
    .filter(Boolean);
}

/** Tokens of one simple command, quoted strings kept whole. */
function words(piece) {
  return (piece.match(new RegExp(TOKEN, "g")) || []).filter(Boolean);
}

/** Drop a leading `command`, `sudo`, `nice`, `env VAR=x`, `xargs` so the verb is visible. */
function verbIndex(ws) {
  let i = 0;
  for (;;) {
    const w = unquoteToken(ws[i] || "");
    if (["command", "sudo", "nice", "xargs"].includes(w)) { i += 1; continue; }
    if (w === "env") { i += 1; while (i < ws.length && /^[A-Za-z_][A-Za-z0-9_]*=/.test(unquoteToken(ws[i]))) i += 1; continue; }
    if (/^[A-Za-z_][A-Za-z0-9_]*=/.test(w) && i === 0) { i += 1; continue; } // VAR=x cmd
    return i;
  }
}

/**
 * @param {string} command
 * @returns {{target:string, verb:string}[]} raw targets; may contain duplicates
 */
export function bashWriteTargets(command) {
  const out = [];
  const push = (target, verb) => { if (usable(target)) out.push({ target: unquoteToken(target), verb }); };
  const src = String(command || "");

  for (const piece of simpleCommands(src)) {
    const ws = words(piece);
    if (!ws.length) continue;
    // Redirects: `> f`, `>> f`, `2> f`, `&> f`, `>f`. Judged on TOKENS, which keep quoted strings whole,
    // so a `>` INSIDE a quoted argument (`node -e 'console.log("=>")'`, a commit message with an arrow)
    // is text, not a write. The old whole-string regex saw every `>` and denied read-only commands as
    // repo mutations (adversarial analysis 2026-10-11, L1.12). A `>&2`-style fd dup is skipped by
    // usable(). A heredoc `<<EOF` is not a write; its `> f` beside it still is.
    // TOKEN deliberately excludes `<>`, so the redirect scan uses its own tokenizer that yields the
    // operator (`>`, `>>`, `2>`, `&>`) as a token of its own, quoted strings whole, everything else
    // as in TOKEN; the operand is the next token.
    const rws = piece.match(/("[^"]*"|'[^']*'|\d?>>?|&>|&[\d-]+|[^\s;&|<>()]+)/g) || [];
    for (let i = 0; i < rws.length; i += 1) {
      if (!/^(?:\d?>>?|&>)$/.test(rws[i])) continue;
      const target = rws[i + 1] || "";
      i += 1;
      push(target, "redirect");
    }
    const vi = verbIndex(ws);
    const verbTok = unquoteToken(ws[vi] || "");
    const verb = verbTok.includes("/") ? verbTok.slice(verbTok.lastIndexOf("/") + 1) : verbTok;
    const args = ws.slice(vi + 1);
    const positional = args.filter((a) => !FLAG.test(unquoteToken(a)));
    switch (verb) {
      case "tee":
        for (const a of positional) push(a, "tee");
        break;
      case "cp": case "install": case "mv": case "ln":
        if (positional.length >= 2) push(positional[positional.length - 1], verb);
        break;
      case "rm": case "unlink": case "shred":
        for (const a of positional) push(a, verb);
        break;
      case "chmod": case "chown": case "chgrp":
        // The first positional is the mode/owner; every one after it is a file operand. These verbs
        // left the bootstrap guard's target-blind regex on 2026-10-11 and are judged by target here.
        for (const a of positional.slice(1)) push(a, verb);
        break;
      case "truncate": {
        // `-s SIZE` / `-r REF` take a value; the value is not a file operand.
        const files = [];
        for (let i = 0; i < args.length; i += 1) {
          const u = unquoteToken(args[i]);
          if (/^-[sr]$/.test(u)) { i += 1; continue; }
          if (FLAG.test(u)) continue;
          files.push(args[i]);
        }
        for (const f of files) push(f, verb);
        break;
      }
      case "sed": case "perl": {
        // Only an in-place edit writes. `sed -i` / `sed -i.bak` / `perl -pi -e` / `perl -i`.
        const inPlace = args.some((a) => /^-[a-zA-Z]*i/.test(unquoteToken(a)));
        if (!inPlace) break;
        // File operands are the positionals after the script: `-e SCRIPT` consumes the next
        // token; a bare first positional is the script when no -e/-f was given.
        let skipNext = false, scriptSeen = args.some((a) => /^-[a-zA-Z]*[ef]$/.test(unquoteToken(a)) || /^-[a-zA-Z]*[ef]./.test(unquoteToken(a)));
        const files = [];
        for (const a of args) {
          const u = unquoteToken(a);
          if (skipNext) { skipNext = false; continue; }
          if (/^-[a-zA-Z]*[ef]$/.test(u)) { skipNext = true; continue; }
          if (FLAG.test(u)) continue;
          if (!scriptSeen) { scriptSeen = true; continue; } // the bare script operand
          files.push(a);
        }
        for (const f of files) push(f, `${verb} -i`);
        break;
      }
      case "dd":
        for (const a of args) { const u = unquoteToken(a); if (u.startsWith("of=")) push(u.slice(3), "dd"); }
        break;
      case "git": {
        // `git checkout -- <paths>` and `git restore <paths>` overwrite working files.
        const sub = unquoteToken(args[0] || "");
        if (sub === "checkout" || sub === "restore") {
          const dd = args.findIndex((a) => unquoteToken(a) === "--");
          const paths = dd >= 0 ? args.slice(dd + 1) : (sub === "restore" ? positional.slice(1) : []);
          for (const p of paths) push(p, `git ${sub}`);
        }
        break;
      }
      default:
        break;
    }
  }
  for (const t of interpreterWriteTargets(src)) out.push(t);
  return out;
}

// ---- interpreter bodies ------------------------------------------------------------------------

const INTERP = String.raw`(?:^|[\s;&|(])(?:[\w./-]*/)?(python3?(?:\.\d+)?|node)(?=\s)`;
const LIT = String.raw`(?:'([^'\\\n]*)'|"([^"\\\n]*)")`;
const IDENT = String.raw`([A-Za-z_$][\w$]*)`;

const lang = (exe) => (exe.startsWith("python") ? "python" : "node");

/** The program text each python/node invocation in `src` is handed: heredoc bodies and -c/-e args. */
export function interpreterBodies(src) {
  const bodies = [];
  const heredoc = new RegExp(
    INTERP + String.raw`[^\n]*?<<-?\s*(['"]?)([A-Za-z_]\w*)\2[^\n]*\n([\s\S]*?)\n[ \t]*\3[ \t]*(?=\n|$)`, "g");
  for (const m of src.matchAll(heredoc)) bodies.push({ lang: lang(m[1]), body: m[4] });
  const arg = new RegExp(
    INTERP + String.raw`(?:\s+(?!-c\b|-e\b|-p\b|--eval\b|--print\b)-[\w-]+(?:=\S+)?)*\s+(?:-c|-e|-p|--eval|--print)\s+("(?:[^"\\]|\\[\s\S])*"|'[^']*')`, "g");
  for (const m of src.matchAll(arg)) {
    const raw = m[2];
    const body = raw[0] === '"' ? raw.slice(1, -1).replace(/\\(["\\$`])/g, "$1") : raw.slice(1, -1);
    bodies.push({ lang: lang(m[1]), body });
  }
  return bodies;
}

/** name -> every string literal the body assigns to it (python `p = 'x'`, node `const p = 'x'`). */
function literalAssignments(body) {
  const map = new Map();
  const re = new RegExp(String.raw`(?:^|[\s;(,])(?:const\s+|let\s+|var\s+)?` + IDENT + String.raw`\s*=(?!=)\s*` + LIT, "g");
  for (const m of body.matchAll(re)) {
    const v = m[2] ?? m[3];
    if (!map.has(m[1])) map.set(m[1], new Set());
    map.get(m[1]).add(v);
  }
  return map;
}

// A write call's path operand: a literal, or a name resolved through literalAssignments.
const OPERAND = String.raw`(?:${LIT}|${IDENT})`;

const PY_RULES = [
  // open(path, mode) / io.open / codecs.open, mode positional or mode=, writing when it has w|a|x|+
  { re: String.raw`\bopen\(\s*${OPERAND}\s*,\s*(?:mode\s*=\s*)?${LIT}`, mode: true },
  { re: String.raw`\bPath\(\s*${OPERAND}\s*\)\s*\.\s*(?:write_text|write_bytes|touch|unlink|rmdir)\s*\(` },
  { re: String.raw`\bPath\(\s*${OPERAND}\s*\)\s*\.\s*open\(\s*(?:mode\s*=\s*)?${LIT}`, mode: true },
  { re: String.raw`\bos\.(?:remove|unlink|rmdir)\(\s*${OPERAND}` },
  { re: String.raw`\b(?:shutil\.(?:copy2?|copyfile|move)|os\.(?:rename|replace))\(\s*[^,()]+,\s*${OPERAND}` },
];
const NODE_RULES = [
  { re: String.raw`\b(?:writeFileSync|appendFileSync|writeFile|appendFile|createWriteStream|rmSync|unlinkSync|truncateSync)\(\s*${OPERAND}` },
  { re: String.raw`\b(?:copyFileSync|copyFile|renameSync|cpSync)\(\s*[^,()]+,\s*${OPERAND}` },
];

/** @returns {{target:string, verb:string}[]} literal (or literal-assigned) paths an interpreter body writes. */
export function interpreterWriteTargets(src) {
  const out = [];
  for (const { lang: l, body } of interpreterBodies(String(src || ""))) {
    const names = literalAssignments(body);
    for (const rule of l === "python" ? PY_RULES : NODE_RULES) {
      for (const m of body.matchAll(new RegExp(rule.re, "g"))) {
        // groups: 1,2 = literal path (single/double), 3 = identifier, then 4,5 = mode literal
        if (rule.mode) {
          const mode = m[4] ?? m[5] ?? "";
          if (!/[wax+]/.test(mode)) continue;
        }
        const lit = m[1] ?? m[2];
        const paths = lit !== undefined ? [lit] : [...(names.get(m[3]) || [])];
        for (const p of paths) if (p && !p.startsWith("/dev/")) out.push({ target: p, verb: `${l} write` });
      }
    }
  }
  return out;
}

/** The leading `cd <dir> &&` of a command, if any: relative targets resolve against it. */
export function leadingCd(command) {
  const m = String(command || "").match(/^\s*cd\s+("[^"]+"|'[^']+'|[^\s;&|]+)\s*(?:&&|;)/);
  return m ? unquoteToken(m[1]) : null;
}

/** For a glob target, the longest literal directory prefix; null when the target has no glob. */
export function globPrefix(target) {
  const t = String(target || "");
  if (!/[*?[]/.test(t)) return null;
  const idx = t.search(/[*?[]/);
  const cut = t.lastIndexOf("/", idx);
  return cut >= 0 ? t.slice(0, cut) : ".";
}
