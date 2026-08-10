#!/usr/bin/env python3
"""

Known false-positive classes (do NOT promote to gating without an FP-triage pass):
- range citations `:NN-MM` (window anchors to NN; content at MM flags falsely)
- table cross-row quote/cite mis-association
- TeX/ASCII notation paraphrase
- generic short strings (def/return/origin-main class)
Anchor-content drift checker for AVE-Core — WARN-CLASS, NON-GATING.

Motivation
----------
Across research/, _orchestration/, and manuscript/ave-kb/ the corpus cites
locations as `path.ext:NN` and frequently pins a verbatim excerpt next to the
cite in `backticks`. When the target file drifts (lines inserted/removed above
the cited spot), the `:NN` goes stale while the quoted excerpt still names the
real content — a "line-anchor drift" the review lane kept catching by hand.

This tool automates that catch: for every `path.ext:NN` cite that carries a
NEARBY backtick-quoted excerpt, it verifies the excerpt actually occurs within
±10 lines of the cited line in the target file. If the excerpt appears MOVED (a candidate — still FP-contaminated: range cites :NN-MM anchor only to range start, cross-row table associations, TeX/ASCII paraphrase; spot-check base rate ~1-in-5 real), (it is
elsewhere in the file) the `:NN` is stale; if it is ABSENT the quote/target may
be reworded or the FP classes below apply.

WARN-CLASS ONLY. This tool prints a summary + the worst offenders and ALWAYS
exits 0. It is wired into `make verify` as an advisory step. Gating is a
deliberate later promotion, not a default — the false-positive classes below
must be driven down first.

Scope
-----
  * Citing files: `.md` under research/ + _orchestration/ + manuscript/ave-kb/
    (SKIP_DIRS pruned — .git, build, session/, _archive, .index, ...).
  * Cite pattern: `path.ext:NN` where ext ∈ TARGET_EXTS (md, py, tex, json, ...),
    optionally wrapped in backticks. TWO written forms are recognized, and both
    are scanned (see CITE_RE):
      - BARE form ...... `path.ext:NN`, including the in-parens link variant
                         `[text](path.ext:NN)` where the line rides inside the
                         link target;
      - LINK form ...... `[text](path.ext):NN` where the line number is written
                         AFTER the closing paren. This is the house style for
                         KB-leaf-to-KB-leaf anchors.
  * Target files: resolved relative to the citing file's directory first, then
    the repo root. Unresolvable targets are counted UNRESOLVED and skipped
    (broken-link territory — that is `verify-md-links`'s job, not ours).
  * Association: a cite is paired with the nearest CHECKABLE excerpt span on
    the same line or ±QUOTE_ADJACENCY lines. THREE written excerpt styles are
    recognized, because the corpus uses all three:
      - `backticks` .... preferred for symbols, identifiers, code;
      - *"emphasised quotes"* (also `**"…"**` / `_"…"_`) .... used for running
        prose, INCLUDING when the excerpt straddles a hard line-wrap;
      - "bare double quotes" .... the plain-prose form (see BARE_QUOTE_RE),
        admitted as a LAST RESORT so it can never displace a house-style span.
    A span is checkable when it is not itself a path-cite / bare-path reference
    and is not trivially short (see MIN_QUOTE_LEN). Cites with no checkable
    adjacent excerpt are counted NOT-CHECKED (no-quote) and are NOT failures.

Matching is whitespace-normalized (`\\s+` → single space) and case-sensitive;
the ±10-line target window is joined before matching so a target-side line wrap
does not cause a spurious miss.

Known false-positive / false-negative classes (why this is WARN-CLASS)
----------------------------------------------------------------------
  * TeX escaping. A quote carrying LaTeX (`$\\alpha$`, `\\text{sat}`, `$1/r^2$`)
    may differ character-for-character from the target source (one side escapes,
    the other renders), yielding a spurious ABSENT.
  * Multi-line / structural quotes. Inline backtick spans are single-line; the
    ±10 window is whitespace-joined to absorb target-side wrapping, but a quote
    meant to span a table row or block may still fragment.
  * Markdown decoration. Bold/italic markers (`**`, `_`) and differing internal
    whitespace inside the quoted excerpt can defeat the substring test.
  * Paraphrase quotes. Some backtick spans paraphrase rather than transcribe;
    an ABSENT verdict there is not a line-anchor problem.
  * Short / symbol-only quotes. Excerpts shorter than MIN_QUOTE_LEN are skipped
    (counted trivial) because they match almost any window (false OK), so they
    carry no anchor signal.
  * Multi-cite lines. A line with several cites and one quote may associate that
    quote with more than one cite (double-count). Warn-class tolerates this.

Self-test
---------
`--self-test` builds a throwaway tree exercising OK / drift-moved / drift-absent
/ no-quote / trivial cases and asserts the classifier buckets them correctly.
Returns nonzero on self-test failure (a dev-time signal); the normal scan run
always returns 0.
"""

import argparse
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path

# Directories pruned at any depth (mirrors verify-md-links SKIP_DIRS + session/).
SKIP_DIRS = {
    ".venv",
    "venv",
    ".git",
    "build",
    "node_modules",
    ".index",
    ".agents",
    "_archive",
    "session",
    "__pycache__",
}

# Consecutive path-segment runs pruned anywhere in a file's relative path.
# `tests/fixtures` holds DELIBERATELY broken cites (this tool's and
# verify-md-links'); scanning them as real content pollutes the corpus counts
# and, for --new-cites, would fail a branch on its own test data.
# verify-md-links.SKIP_SEGMENT_RUNS carries the same run for the same reason.
SKIP_SEGMENT_RUNS: tuple[tuple[str, ...], ...] = (("tests", "fixtures"),)

# Roots whose .md files we scan for cites (repo-root-relative).
CITING_ROOTS = ("research", "_orchestration", "manuscript/ave-kb")


def _contains_run(parts: tuple[str, ...], run: tuple[str, ...]) -> bool:
    """True if `run` appears as a consecutive subsequence of `parts`."""
    return any(parts[i : i + len(run)] == run for i in range(len(parts) - len(run) + 1))

# Target extensions a `path.EXT:NN` cite may point at.
TARGET_EXTS = (
    "md",
    "py",
    "tex",
    "json",
    "jsonl",
    "csv",
    "txt",
    "yaml",
    "yml",
    "toml",
    "cfg",
    "ini",
    "sh",
)

# A `path.ext:NN` cite. Path may carry directory segments; ext is a known target
# extension; line is a positive integer. Word boundary after the digits keeps
# `foo.md:12` from swallowing a trailing `:34` range half.
_PATH_RE = r"(?:[\w.+-]+/)*[\w.+-]+\.(?:" + "|".join(TARGET_EXTS) + r")"

# TWO branches, sharing the `:NN` tail:
#   LINK branch (`lpath`) — `[text](path.ext):NN`. The `](` opener is asserted by
#     a fixed-width lookbehind rather than consumed, so `m.start()` still lands on
#     the path (the column `associate_quote` ranks quote-proximity against) and the
#     trailing `)` is only allowed when a link actually opened it. A bare
#     `(prose parenthetical foo.md):12` is therefore NOT matched — the lookbehind
#     is what keeps an unrelated `):` sequence out.
#   BARE branch (`path`) — `path.ext:NN`, incl. the `[text](path.ext:NN)` variant
#     where the line rides inside the link target (unchanged, pre-existing).
# The branches are mutually exclusive at any given start position (the LINK
# branch needs `](` behind AND `)` ahead; the BARE branch needs `:` where the
# LINK branch needs `)`), so alternation order does not change the match set —
# it is written LINK-first only to read in the order of the docstring.
# Use cite_path(m) to read the path — the two branches need distinct group names.
CITE_RE = re.compile(
    r"(?:(?<=\]\()(?P<lpath>" + _PATH_RE + r")\)|(?P<path>" + _PATH_RE + r"))"
    r":(?P<line>\d+)(?!\d)"
)


def cite_path(m: "re.Match[str]") -> str:
    """The cited path from either CITE_RE branch (markdown-link form or bare)."""
    return m.group("lpath") or m.group("path")


# One inline backtick span (no nested backticks).
BACKTICK_RE = re.compile(r"`([^`\n]+)`")

# The corpus writes verbatim excerpts in TWO house styles, and a recognizer that
# sees only one trains lanes to work around the gate rather than obey it. The
# second style is an EMPHASISED QUOTE — *"..."*, **"..."**, _"..."_ — used
# wherever the excerpt is running prose rather than a symbol or an identifier
# (backticks are preferred for the latter because they suppress markdown).
# Measured over the back-test window when this was added: 6 of 21 blocked cites
# (29%) carried an excerpt in this style and were flagged anyway. Details in
# §6 of _orchestration/docket-entries/2026-08-05-cite-rot-line-existence.md.
EMPHASIS_QUOTE_RE = re.compile(r"[*_]{1,3}[\"“]([^\"“”\n]+)[\"”][*_]{1,3}")

# The THIRD house form: a BARE double-quoted excerpt, with no emphasis markers
# and no back-ticks. Added 2026-08-07 under ruling R27
# (_orchestration/docket-entries/2026-08-07-rulings-r23-r27.md). It was the
# escape route around the #915 primer-misquote blocker: a lane could write its
# excerpt as "…", satisfy no recognizer, and the drift check above would never
# compare that excerpt against its target — a misquote written this way was
# unreachable by any gate in the repo.
#
# ADMITTED AS A LAST RESORT, never as a peer (see `associate_quote`). Bare
# double quotes are ubiquitous in ordinary prose, so giving them equal standing
# would let a passing quoted phrase DISPLACE a deliberate house-style excerpt
# that a lane put beside its cite. Measured over the whole corpus at the commit
# this landed on, the three orderings buy IDENTICAL coverage (+700 newly-checked
# cites in every one) and differ only in displacement:
#
#   ordering                              newly-checked   OK->not-OK flips
#   bare as a peer, nearest span wins          +700              43
#   bare as a same-line fallback               +700               4
#   bare as a whole-pass last resort (SHIPPED) +700               0
#
# The peer ordering therefore costs 43 displaced anchors and buys nothing. That
# is a measurement, not a preference.
#
# ⚑ RESIDUAL FALSE-NEGATIVE, disclosed (PR #926 Tier-2 audit). Admitting bare
# quotes AT ALL — in any pass order — opens one narrow hole: if a lane's real
# house-style excerpt is MALFORMED so that it yields no span in any form (an
# unclosed back-tick, say), and some unrelated bare-quoted phrase sits in the
# window and happens to occur in the target file, the cite flips BLOCKED -> ok
# on an excerpt nobody meant as one. The shipped last-resort order does not
# cause this and is the safest of the three measured; the hole is inherent to
# the form. ACCEPTED as the R27 trade: it costs a rare false-negative on
# malformed excerpts, and it buys the closing of a blind spot that hid every
# bare-quoted MISQUOTE from every gate in the repo.
BARE_QUOTE_RE = re.compile(r"[\"“]([^\"“”\n]+)[\"”]")

# A span whose whole (stripped) body is a bare path or path-cite — NOT content.
PATHISH_RE = re.compile(r"^[\w./+-]+\.[A-Za-z0-9]+(:\d+)?$")

# Reference fragments that are decoration, not target-line content: a bare
# `:NN` line-number fragment or a bare `.ext` extension. These appear all over
# the corpus and match everywhere, so treating them as anchors is pure noise.
FRAGMENT_RE = re.compile(r"^(:\d+|\.[A-Za-z0-9]+)$")

WINDOW = 10  # ±N lines around the cited line in the TARGET file
QUOTE_ADJACENCY = 1  # ±N lines around the cite in the CITING file to find a quote
MIN_QUOTE_LEN = 4  # min stripped length of a backtick span to count as an anchor
DEFAULT_TOP = 25  # worst-offenders printed


@dataclass
class Finding:
    citing_file: Path
    citing_line: int
    target: str  # cite path as written
    target_line: int
    quote: str
    kind: str  # "moved" | "moved-wrapped" | "absent"
    found_at: list[int] = field(default_factory=list)


@dataclass
class Counts:
    cites: int = 0
    checked_ok: int = 0
    drift_moved: int = 0
    drift_absent: int = 0
    not_checked_noquote: int = 0
    not_checked_trivial: int = 0
    unresolved: int = 0


def find_repo_root(start: Path) -> Path:
    """Walk up from `start` to the AVE-Core repo root (Makefile + manuscript/)."""
    for parent in (start, *start.parents):
        if (parent / "Makefile").is_file() and (parent / "manuscript").is_dir():
            return parent
    for parent in (start, *start.parents):
        if (parent / ".git").exists():
            return parent
    return start


def strip_fenced(text: str) -> str:
    """Blank ``` / ~~~ fenced blocks (line-count preserved); KEEP inline spans.

    Unlike verify-md-links.strip_code, inline `code` spans are preserved — they
    ARE the quoted content this tool inspects. Only multi-line fences (example
    snippets) are dropped, since cites inside them are illustrative.
    """
    out: list[str] = []
    fence: str | None = None
    for raw in text.splitlines():
        stripped = raw.lstrip()
        if fence is None:
            if stripped.startswith("```") or stripped.startswith("~~~"):
                fence = stripped[:3]
                out.append("")
                continue
            out.append(raw)
        else:
            out.append("")
            if stripped.startswith(fence):
                fence = None
    return "\n".join(out)


def iter_citing_files(repo_root: Path):
    """Yield .md files under the citing roots, pruning SKIP_DIRS at any depth."""
    for root_name in CITING_ROOTS:
        root = repo_root / root_name
        if not root.is_dir():
            continue
        for path in sorted(root.rglob("*.md")):
            parts = path.relative_to(repo_root).parts
            if any(part in SKIP_DIRS for part in parts):
                continue
            if any(_contains_run(parts, run) for run in SKIP_SEGMENT_RUNS):
                continue
            yield path


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def is_checkable_quote(body: str) -> bool:
    """True if a backtick span is a substantive anchor (not a path / trivial)."""
    s = body.strip()
    if len(s) < MIN_QUOTE_LEN:
        return False
    if FRAGMENT_RE.match(s):  # bare `:NN` or `.ext` reference fragment
        return False
    if PATHISH_RE.match(s):  # bare path or path-cite reference
        return False
    if CITE_RE.search(s):  # contains a path:line cite — it IS a cite, not content
        return False
    if not any(c.isalnum() for c in s):  # pure punctuation / symbols
        return False
    return True


def _straddling_emphasis_spans(lines: list[str], idx: int) -> list[tuple[int, str]]:
    """Emphasised-quote spans that cross a hard line-wrap at line `idx`.

    The KB hard-wraps prose, so a running-prose excerpt routinely opens on one
    line and closes on the next: `*"the arrow comes from` / `mode-count or a
    click, never a valve"*`. A per-line regex sees neither half. Rejoining the
    line with each neighbour and keeping only matches that CROSS the seam
    recovers exactly those, with no risk of re-reporting a same-line span.
    """
    out: list[tuple[int, str]] = []
    if idx > 0:
        prev = lines[idx - 1]
        seam = len(prev) + 1
        for m in EMPHASIS_QUOTE_RE.finditer(prev + " " + lines[idx]):
            if m.start() < seam <= m.end() and is_checkable_quote(m.group(1)):
                out.append((0, m.group(1)))  # continues from the left margin
    if idx + 1 < len(lines):
        seam = len(lines[idx]) + 1
        for m in EMPHASIS_QUOTE_RE.finditer(lines[idx] + " " + lines[idx + 1]):
            if m.start() < seam <= m.end() and is_checkable_quote(m.group(1)):
                out.append((m.start(), m.group(1)))
    return out


def _quote_spans(lines: list[str], idx: int, bare: bool = False) -> list[tuple[int, str]]:
    """Checkable excerpt spans visible from line `idx`, as (start_col, body).

    The house styles (backticks and emphasised quotes), plus emphasised quotes
    that straddle a single hard line-wrap into the neighbouring line. With
    `bare=True` the plain `"…"` form is admitted as well — only the second pass
    of `associate_quote` passes that, never the first.
    """
    line = lines[idx]
    regexes = (BACKTICK_RE, EMPHASIS_QUOTE_RE) + ((BARE_QUOTE_RE,) if bare else ())
    spans = [
        (m.start(), m.group(1))
        for regex in regexes
        for m in regex.finditer(line)
        if is_checkable_quote(m.group(1))
    ]
    spans.extend(_straddling_emphasis_spans(lines, idx))
    return spans


def _associate(lines: list[str], cite_line_idx: int, cite_col: int, bare: bool) -> str | None:
    """One association pass (same line, then ±ADJACENCY).

    Same-line spans are ranked by |column distance| to the cite; adjacent lines
    are considered only if the cite line has none AND the adjacent line carries
    no cite of its own (so a sibling cite's quote is never stolen — this is what
    keeps dense cite-lists from cross-contaminating). Returns the body or None.
    """
    same = _quote_spans(lines, cite_line_idx, bare)
    if same:
        same.sort(key=lambda cb: abs(cb[0] - cite_col))
        return same[0][1]
    for delta in range(1, QUOTE_ADJACENCY + 1):
        for idx in (cite_line_idx - delta, cite_line_idx + delta):
            if 0 <= idx < len(lines):
                if CITE_RE.search(lines[idx]):  # that quote belongs to its own cite
                    continue
                spans = _quote_spans(lines, idx, bare)
                if spans:
                    return spans[0][1]
    return None


def associate_quote(lines: list[str], cite_line_idx: int, cite_col: int) -> str | None:
    """Nearest checkable excerpt span to a cite — house styles first, bare last.

    TWO passes of the SAME search. The first admits only the house styles, so
    every association that existed before BARE_QUOTE_RE was added is returned
    unchanged, by construction. Only when that pass comes up EMPTY is the search
    re-run with bare `"…"` spans admitted. The widening is therefore purely
    additive: it can turn a None into a quote and can never change or remove one.

    That is what makes it safe in BOTH consumers. In the gating `--new-cites`
    ratchet a None is the violation, so no cite that passed can start failing.
    In the advisory drift scan the selected excerpt drives the verdict, so a
    displaced selection could have flipped an anchored cite to drift; measured
    corpus-wide at the landing commit, this ordering flips ZERO (the peer
    ordering flips 43 — see BARE_QUOTE_RE).
    """
    quote = _associate(lines, cite_line_idx, cite_col, bare=False)
    if quote is None:
        quote = _associate(lines, cite_line_idx, cite_col, bare=True)
    return quote


class TargetCache:
    """Lazily read + normalize target files once."""

    def __init__(self) -> None:
        self._norm_lines: dict[Path, list[str]] = {}
        self._whole: dict[Path, str] = {}

    def load(self, path: Path) -> tuple[list[str], str]:
        if path not in self._norm_lines:
            try:
                raw = path.read_text(encoding="utf-8", errors="replace")
            except OSError:
                self._norm_lines[path] = []
                self._whole[path] = ""
                return [], ""
            lines = raw.splitlines()
            self._norm_lines[path] = [normalize(ln) for ln in lines]
            self._whole[path] = normalize(" ".join(lines))
        return self._norm_lines[path], self._whole[path]


def resolve_target(target_path: str, citing_file: Path, repo_root: Path) -> Path | None:
    """Resolve a cite path relative to the citing file, then the repo root.

    The parameter is `target_path`, NOT `cite_path` — `cite_path` is the
    module-level helper that reads the path out of either CITE_RE branch, and a
    same-named parameter would shadow it inside this function body.
    """
    for base in (citing_file.parent, repo_root):
        cand = (base / target_path).resolve()
        if cand.is_file():
            return cand
    return None


def classify(
    norm_lines: list[str], whole: str, cited_line: int, quote: str
) -> tuple[str, list[int]]:
    """Classify a (cited_line, quote) against a target file.

    Returns ("ok"|"moved"|"moved-wrapped"|"absent", found_line_numbers).
    """
    q = normalize(quote)
    if not q or not norm_lines:
        return "absent", []
    lo = max(0, cited_line - 1 - WINDOW)
    hi = min(len(norm_lines), cited_line - 1 + WINDOW + 1)
    window = " ".join(norm_lines[lo:hi])
    if q in window:
        return "ok", []
    hits = [i + 1 for i, ln in enumerate(norm_lines) if q in ln]
    if hits:
        return "moved", hits
    if q in whole:  # wrapped across lines somewhere outside the window
        return "moved-wrapped", []
    return "absent", []


def scan(citing_files, repo_root: Path) -> tuple[Counts, list[Finding]]:
    counts = Counts()
    findings: list[Finding] = []
    cache = TargetCache()
    for cf in citing_files:
        try:
            text = strip_fenced(cf.read_text(encoding="utf-8", errors="replace"))
        except OSError:
            continue
        lines = text.splitlines()
        for i, line in enumerate(lines):
            for m in CITE_RE.finditer(line):
                counts.cites += 1
                target_path = cite_path(m)
                cited_line = int(m.group("line"))
                quote = associate_quote(lines, i, m.start())
                if quote is None:
                    # Distinguish "there was a nearby span but it was trivial"
                    # from "no span at all" for an honest not-checked breakdown.
                    raw_spans = [
                        b for _, b in ((mm.start(), mm.group(1)) for mm in BACKTICK_RE.finditer(line))
                    ]
                    if any(len(b.strip()) < MIN_QUOTE_LEN for b in raw_spans):
                        counts.not_checked_trivial += 1
                    else:
                        counts.not_checked_noquote += 1
                    continue
                target = resolve_target(target_path, cf, repo_root)
                if target is None:
                    counts.unresolved += 1
                    continue
                norm_lines, whole = cache.load(target)
                kind, found = classify(norm_lines, whole, cited_line, quote)
                if kind == "ok":
                    counts.checked_ok += 1
                elif kind in ("moved", "moved-wrapped"):
                    counts.drift_moved += 1
                    findings.append(
                        Finding(cf, i + 1, target_path, cited_line, quote, kind, found)
                    )
                else:
                    counts.drift_absent += 1
                    findings.append(
                        Finding(cf, i + 1, target_path, cited_line, quote, kind, found)
                    )
    return counts, findings


def _fmt_quote(q: str, width: int = 60) -> str:
    q = normalize(q)
    return q if len(q) <= width else q[: width - 1] + "…"


def report(counts: Counts, findings: list[Finding], repo_root: Path, top: int) -> None:
    print("[anchor-content] WARN-CLASS advisory — quoted-excerpt vs cited line drift")
    print(f"  cites scanned .............. {counts.cites}")
    print(f"  checked & anchored (OK) .... {counts.checked_ok}")
    print(f"  DRIFT — excerpt moved ...... {counts.drift_moved}  (stale :NN, excerpt found elsewhere)")
    print(f"  DRIFT — excerpt absent ..... {counts.drift_absent}  (not in target; see FP classes)")
    print(f"  not-checked (no quote) ..... {counts.not_checked_noquote}")
    print(f"  not-checked (trivial quote)  {counts.not_checked_trivial}")
    print(f"  unresolved target .......... {counts.unresolved}  (verify-md-links territory)")
    checked = counts.checked_ok + counts.drift_moved + counts.drift_absent
    drift = counts.drift_moved + counts.drift_absent
    rate = (drift / checked * 100.0) if checked else 0.0
    print(f"  → checked cites: {checked}; drift: {drift} ({rate:.1f}% of checked)")

    if not findings:
        print("  No drift among checkable cites.")
        return
    # Moved (stale-line, strongest signal) first, then absent.
    order = {"moved": 0, "moved-wrapped": 1, "absent": 2}
    findings.sort(key=lambda f: (order.get(f.kind, 3), str(f.citing_file), f.citing_line))
    print(f"\n  worst offenders (up to {top}; moved-line drift first):")
    for f in findings[:top]:
        try:
            rel = f.citing_file.relative_to(repo_root)
        except ValueError:
            rel = f.citing_file
        loc = ""
        if f.kind == "moved" and f.found_at:
            near = ", ".join(str(n) for n in f.found_at[:5])
            loc = f" [found at {target_line_summary(f.target, near)}]"
        elif f.kind == "moved-wrapped":
            loc = " [found wrapped elsewhere]"
        print(f"   · {rel}:{f.citing_line}  →  {f.target}:{f.target_line}  {f.kind}{loc}")
        print(f"       excerpt: `{_fmt_quote(f.quote)}`")


def target_line_summary(target: str, near: str) -> str:
    name = target.rsplit("/", 1)[-1]
    return f"{name}:{near}"


# --- NEW-cite excerpt requirement (cite-rot option 3) -----------------------
#
# The corpus-wide backlog is ~13k cites and roughly half carry no excerpt at
# all, so a repo-wide excerpt requirement is not on the table. This RATCHET
# requires an excerpt only on cites a branch ADDS, so the backlog stops growing
# and every new cite is self-verifying (the advisory drift check above can
# actually see it) without touching one byte of history.
#
# Scope is the same canonical-authority surface verify-md-links gates on — the
# KB tree plus the repo-root user-facing docs — so research/ and
# _orchestration/ lanes are never blocked. "Load-bearing" is that surface.

_ERROR_SOURCE_ROOT_DOCS = {"README.md", "LIVING_REFERENCE.md", "AGENTS.md"}

_DIFF_FILE_RE = re.compile(r"^\+\+\+ b/(.+)$")
_DIFF_HUNK_RE = re.compile(r"^@@ -\d+(?:,\d+)? \+(\d+)(?:,(\d+))? @@")


def is_load_bearing_source(rel: Path) -> bool:
    """True if a repo-relative markdown path is on the canonical-authority surface."""
    parts = rel.parts
    if any(p in SKIP_DIRS for p in parts):
        return False
    if any(_contains_run(parts, run) for run in SKIP_SEGMENT_RUNS):
        return False
    if parts[:2] == ("manuscript", "ave-kb"):
        return parts[2:3] != ("session",)
    return len(parts) == 1 and parts[0] in _ERROR_SOURCE_ROOT_DOCS


def added_lines_by_file(base_ref: str, repo_root: Path) -> dict[Path, set[int]]:
    """Map repo-relative .md path -> set of line numbers ADDED vs `base_ref`.

    Uses `git diff --unified=0 <base>...HEAD`, i.e. the merge-base three-dot
    form, so a branch is measured against what it actually introduced rather
    than against unrelated drift on the base.
    """
    proc = subprocess.run(
        ["git", "diff", "--unified=0", "--diff-filter=d", f"{base_ref}...HEAD", "--", "*.md"],
        cwd=repo_root,
        capture_output=True,
        text=True,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"git diff against {base_ref!r} failed: {proc.stderr.strip()}")
    added: dict[Path, set[int]] = {}
    current: Path | None = None
    lineno = 0
    for raw in proc.stdout.splitlines():
        file_match = _DIFF_FILE_RE.match(raw)
        if file_match:
            current = Path(file_match.group(1))
            continue
        hunk = _DIFF_HUNK_RE.match(raw)
        if hunk:
            lineno = int(hunk.group(1))
            continue
        if current is not None and raw.startswith("+") and not raw.startswith("+++"):
            added.setdefault(current, set()).add(lineno)
            lineno += 1
    return added


def check_new_cites(base_ref: str, repo_root: Path) -> list[tuple[Path, int, str]]:
    """Every ADDED load-bearing line-cite that carries no adjacent excerpt.

    Returns (repo-relative path, line, cite-as-written) triples.
    """
    violations: list[tuple[Path, int, str]] = []
    for rel, added in sorted(added_lines_by_file(base_ref, repo_root).items()):
        if not is_load_bearing_source(rel):
            continue
        path = repo_root / rel
        if not path.is_file():
            continue
        lines = strip_fenced(path.read_text(encoding="utf-8", errors="replace")).splitlines()
        for lineno in sorted(added):
            if lineno > len(lines):
                continue
            line = lines[lineno - 1]
            for match in CITE_RE.finditer(line):
                if associate_quote(lines, lineno - 1, match.start()) is None:
                    cited = f"{cite_path(match)}:{match.group('line')}"
                    violations.append((rel, lineno, cited))
    return violations


def report_new_cites(violations: list[tuple[Path, int, str]], base_ref: str) -> None:
    print(f"[anchor-content] NEW-cite excerpt requirement (vs {base_ref})")
    if not violations:
        print("  OK — every added load-bearing line-cite carries an adjacent excerpt.")
        return
    print(f"  {len(violations)} added cite(s) with no adjacent verbatim excerpt:\n")
    for rel, lineno, cited in violations:
        print(f"   · {rel}:{lineno}  ->  {cited}")
    print(
        "\n  Fix: put a verbatim excerpt of the cited content beside the cite (same\n"
        "  line, or the line above/below), in any of the three house styles —\n"
        "  `backticks` for symbols and identifiers, *\"emphasised quotes\"* for\n"
        '  running prose, or plain "double quotes".\n'
        "  That makes the cite self-verifying — the advisory drift check can then\n"
        "  re-anchor it when the target file moves, instead of the `:NN` rotting\n"
        "  silently."
    )


def run_self_test() -> int:
    print("[anchor-content] self-test ...")
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        (root / "Makefile").write_text("# sentinel\n")
        (root / "manuscript").mkdir()
        # Target file: known content at known lines.
        target_lines = ["\n"] * 40
        target_lines[9] = "the quick brown fox anchor phrase\n"  # line 10
        target_lines[29] = "a drifted excerpt that moved down here\n"  # line 30
        target = root / "target.md"
        target.write_text("".join(target_lines))
        # Citing file exercising each bucket.
        citing = root / "research"
        citing.mkdir()
        cite_md = citing / "cites.md"
        cite_md.write_text(
            "\n".join(
                [
                    "GOOD:   see `target.md:10` for `the quick brown fox anchor phrase` here.",
                    "MOVED:  per `target.md:10` the `a drifted excerpt that moved down here` note.",
                    "ABSENT: `target.md:10` claims `a phrase that exists nowhere at all`.",
                    "NOQUOTE: `target.md:10` with no adjacent quoted excerpt whatsoever.",
                    "TRIVIAL: `target.md:10` near `S` only.",
                ]
            )
            + "\n"
        )
        counts, findings = scan([cite_md], root)
        expect = {
            "cites": 5,
            "checked_ok": 1,
            "drift_moved": 1,
            "drift_absent": 1,
            "not_checked_noquote": 1,
            "not_checked_trivial": 1,
            "unresolved": 0,
        }
        ok = True
        for k, v in expect.items():
            got = getattr(counts, k)
            status = "ok" if got == v else "FAIL"
            if got != v:
                ok = False
            print(f"   {status}: {k} = {got} (expected {v})")
        moved = [f for f in findings if f.kind == "moved"]
        if not (len(moved) == 1 and 30 in moved[0].found_at):
            ok = False
            print(f"   FAIL: expected 1 moved finding located at line 30; got {[ (f.kind,f.found_at) for f in findings]}")
        else:
            print("   ok: moved finding correctly located at target line 30")
        print("[anchor-content] self-test", "PASSED" if ok else "FAILED")
        return 0 if ok else 1


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--self-test", action="store_true", help="run the built-in self-test and exit")
    parser.add_argument("--top", type=int, default=DEFAULT_TOP, help="max worst-offenders to print")
    parser.add_argument("--root", type=Path, default=None, help="repo root (default: auto-detect)")
    parser.add_argument(
        "--new-cites",
        metavar="BASE_REF",
        default=None,
        help=(
            "GATING ratchet: require a verbatim excerpt beside every line-cite this "
            "branch ADDS to the canonical-authority surface (KB tree + root docs), "
            "measured as `git diff BASE_REF...HEAD`. Exits nonzero on a violation. "
            "The repo-wide scan below stays warn-class."
        ),
    )
    args = parser.parse_args(argv)

    if args.self_test:
        return run_self_test()

    repo_root = args.root.resolve() if args.root else find_repo_root(Path(__file__).resolve().parent)

    if args.new_cites:
        violations = check_new_cites(args.new_cites, repo_root)
        report_new_cites(violations, args.new_cites)
        return 1 if violations else 0
    counts, findings = scan(list(iter_citing_files(repo_root)), repo_root)
    report(counts, findings, repo_root, args.top)
    # WARN-CLASS: never gate. Gating is a later, deliberate promotion.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
