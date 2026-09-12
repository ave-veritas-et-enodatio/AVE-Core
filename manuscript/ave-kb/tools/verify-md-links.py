#!/usr/bin/env python3
"""Repo-wide Markdown link-integrity checker for AVE-Core.

Crawls every tracked `.md` file in the repo, extracts Markdown links
`[text](target)`, and reports broken file targets. Also folds in a
consumer-side id-validity check: hashed claim/experiment/support/definition ids
(`clm-`/`exp-`/`sup-`/`def-` + 6 [a-z0-9]) cited in prose must resolve to a node
in `manuscript/ave-kb/.index/claims.jsonl`.

Pure standard library. See `make verify-md-links` / `make verify-inter-repo-links`.

Link classification:
  - external schemes (http, https, mailto, absolute URLs) are skipped.
  - intra-repo  = resolved path stays inside AVE-Core.
  - inter-repo  = resolved path escapes into a sibling repo (../AVE-*). These
    are legitimately stale/in-flux; handling is controlled by --inter-repo.

Source-based gating:
  A broken intra-repo link or an unknown-id citation is a HARD ERROR (flips the
  exit code) only when its SOURCE file is in the error-source set; otherwise it
  is WARN-only (printed, tagged `· warn`, but does not flip the exit code). The
  error-source set is the canonical-authority surface:
    - files under `manuscript/ave-kb/` but NOT under `manuscript/ave-kb/session/`, OR
    - the repo-root user-facing docs README.md, LIVING_REFERENCE.md, AGENTS.md.
  Everything else (research/, _orchestration/, src/, docs/, ...) is WARN-only.
  Note: a KB leaf linking to a missing `src/...` file IS a hard error, because
  its source is the canonical KB tree — broken KB→src derivation refs must gate.

Skipped targets (never classified broken):
  - targets ending in `.tex` (the LaTeX manuscript is a derived build artifact,
    not a navigation target),
  - targets beginning with `~` (home-dir paths like `~/.claude/...`), and
  - targets resolving INTO an `IGNORED_PATHS` dir (e.g. `assets/sim_outputs/`) —
    gitignored generated artifacts that are absent on a fresh checkout.

False-positive avoidance:
  - links and ids inside ``` fenced code blocks and `inline code` spans are
    NOT extracted (doc/example links live in fences).
  - a trailing `#anchor` fragment and a trailing `:linenum` suffix are stripped
    before resolving (the codebase cites locations as `path/file.md:42`).

Line-cite (`path.ext:NN`) pass — added 2026-08-05, cite-rot options (2)+(3):
  The corpus's load-bearing provenance form is a LOCATION cite, and until this
  pass NONE of the line numbers were validated (`strip_target` deletes the
  `:NN` by construction) and the MOST COMMON written form — backticked-bare
  `` `path.md:NN` `` — was invisible end-to-end, because `strip_code` blanks
  inline spans before the link regex runs. A cite could name a file that does
  not exist, at a line that does not exist, and gating stayed green.

  `iter_line_cites` reads the fences-blanked / inline-spans-KEPT view and
  parses all three written forms (backticked-bare, `[t](path:NN)`,
  `[t](path):NN`). Findings:

    - `dead line cite` — GATING per `is_error_source`, same as broken-intra.
      No resolvable candidate file HAS the cited line. Zero-false-positive by
      construction: candidates are the UNION of direct resolution and
      suffix-index resolution, and the verdict fires only when EVERY candidate
      is too short. It asserts existence ONLY — content drift stays with the
      advisory `verify-anchor-content.py`, and the two do not overlap
      (that tool skips unresolvable targets as "verify-md-links territory";
      this one never inspects excerpt text).
    - `blank line cite` — ADVISORY, never gating. The line exists but is empty
      or pure decoration.
    - `broken backtick path` — ADVISORY, never gating. A backticked-bare cite
      whose path resolves nowhere.
    - `stale line-cite waiver` — GATING, like its kbleaf twin.

  POSTURE (measured, not assumed). `dead line cite` gates from day one
  because its error-source population measured ZERO — and that zero does not
  go stale, because the gate itself re-asserts it on every `make verify`. The
  two advisory kinds do NOT gate because their error-source populations are a
  real pre-existing backlog, and a gate that red-lights merge on day one gets
  bypassed rather than obeyed.

  NO CENSUS IS BAKED INTO THIS DOCSTRING. The single source of truth for every
  count — populations, flip conditions, measurement basis — is the docket
  fragment `_orchestration/docket-entries/2026-08-05-cite-rot-line-existence.md`.
  The live numbers are printed by every run (`make verify-md-links`, and
  `--advisory-cites report` for the itemised queue). Three separate stale
  figures shipped in this file's first draft; a comment that carries a census
  is a comment that lies within the month, so it now carries a pointer.
  N.B. the counts are CHECKOUT-SENSITIVE (this pass walks the filesystem, so
  untracked local files resolve paths a fresh clone cannot) — measure in a
  pristine `git worktree`, per the docket fragment's §2 measurement basis.

  Deliberately-historical cites are exempt, in one of TWO ways (R2, checker
  landed 2026-09-07 — the convention an author reads is
  `manuscript/ave-kb/CONVENTIONS.md`, "Author-declared pin marker", written
  2026-08-06):

    MARKER-EXEMPT    the cite is directly followed by the corpus's own
                     author-declared pin marker, `` pin:`<sha>` `` (7-40
                     lowercase hex), in any of the three written forms:

                         per `some-leaf.md:42` pin:`c4a546dc`

                     It exempts exactly the cite it follows and nothing else on
                     the line, and the exemption is granted only when the pin's
                     CLAIM IS TRUE: `<path>` exists at `<sha>` and has at least
                     `<line>` lines. A marker that is unreadable
                     (`malformed pin marker`), names no commit
                     (`unknown pin sha`), is false at its own commit
                     (`pin does not resolve at its own sha`), or binds to no
                     cite (`orphan pin marker`) exempts NOTHING and gates from
                     a KB source. Otherwise the marker would be an opt-out by
                     assertion.
    HERITAGE-EXEMPT  no marker, but the citing LINE carries a backticked SHA.
                     The pre-R2 line-scoped heuristic, GRANDFATHERED and still
                     honoured, but counted apart so the migration is
                     measurable. `HERITAGE_PIN_EXEMPTION` is the re-key switch
                     (`--no-heritage-pin-exemption` previews the flip); it
                     ships ON and flipping it is not this change. Every
                     ordinary run PRINTS what the flip would cost, measured.

  Every run prints the three-way split, the marker-keyed ratio and the flip
  preview. The measurement that motivated the marker, and its 2026-09-07
  re-measurement, are at
  `_HISTORICAL_PIN_RE`. Byte-frozen documents (`research/*_prereg-FROZEN.md`,
  dated result docs, `_orchestration/docket-entries/*`) are never forced to
  change: they are all outside the error-source set, so their findings are
  warn-only by the pre-existing source-gating rule; `WAIVED_LINE_CITE` is the
  escape hatch if a frozen document ever lands inside the KB tree.

kbleaf (.tex) citation pass:
  The rendered manuscript cites canonical KB leaves / repo files inline via
  `\\kbleaf{<path>}` (defined in manuscript/structure/commands.tex). This pass
  crawls `manuscript/**/*.tex` and verifies every path-shaped argument resolves
  to a real file, so a dead KB path in the manuscript gates `make verify`
  instead of passing silently. Resolution is PATH-SUFFIX matching: every
  directory segment the cite names must lie on the tail of a real repo path,
  so tail-of-path shorthand (`ch01-gravity-yield/leaf.md`) resolves while a
  cite naming a WRONG directory fails even when a same-named leaf exists
  elsewhere. Bare filenames resolve by basename, and only when they carry a
  known file extension; `...` ellipses and `[..]` ranges resolve as globs;
  targets starting `AVE-<Repo>/` resolve against the sibling-repo umbrella
  dir and are classified `broken inter` (sibling checkouts are legitimately
  absent on a fresh CI checkout). Non-path arguments (identifiers, skill
  names, shell snippets — \\kbleaf is also used as a generic monospace
  typesetter) are skipped and counted. A `\\texttt{prefix-} \\kbleaf{tail}`
  split cite is flagged as `split kbleaf`: the tail alone resolves against
  the wrong leaf or nothing, defeating the check — cite the full name in one
  \\kbleaf{} (its seqsplit already provides the line breaking). Findings gate
  the exit code except (source, argument) pairs in WAIVED_KBLEAF
  (adjudicated report-don't-fix), and a waiver that no longer matches a live
  dead cite is itself a gating `stale kbleaf waiver` failure.
"""

import argparse
import json
import logging
import posixpath
import re
import subprocess
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

# Share the canonical spine-id grammar with the rest of the tools tree rather
# than re-encoding it here (kb_index_lib is the single source of truth for the
# clm-/exp-/sup- id shape). kb_index_lib lives alongside this script and
# resolves via PYTHONPATH (set by the make target that runs this tool).
import kb_index_lib

logger = logging.getLogger("verify-md-links")

# Directories never crawled, matched as a single path segment at any depth.
#   - `.index` holds generated jsonl + format-spec docs.
#   - `.agents` is gitignored ephemeral scratch — must never be linted.
#   - `_archive` (at any depth) is a frozen archive — content is intentionally
#     stale and must not gate or warn (e.g. research/_archive/,
#     _orchestration/_archive/).
SKIP_DIRS = {".venv", "venv", ".git", "build", "node_modules", ".index", ".agents", "_archive"}

# Consecutive path-segment sequences that exclude a file from the crawl,
# matched anywhere in the file's relative path.
#   - `tests/fixtures`: test fixtures (this checker's and the KB tooling's)
#     contain deliberately broken links and placeholder ids; scanning them as
#     real content would fail a repo-wide run on intentional test data.
#   - `.claude/worktrees`: nested git worktrees (gitignored) — scanning them
#     would double-count the repo against itself.
SKIP_SEGMENT_RUNS: tuple[tuple[str, ...], ...] = (
    ("tests", "fixtures"),
    (".claude", "worktrees"),
)


def _contains_run(parts: tuple[str, ...], run: tuple[str, ...]) -> bool:
    """True if `run` appears as a consecutive subsequence of `parts`."""
    return any(parts[i : i + len(run)] == run for i in range(len(parts) - len(run) + 1))


# Top-level entries that constitute "inside AVE-Core" for intra/inter split.
# A resolved path that is not under the repo root is inter-repo by definition;
# this set is informational and not used as a gate (the gate is repo-root
# containment), but documents the intra surface.
INTRA_ROOTS = {
    "manuscript",
    "research",
    "_orchestration",
    "src",
    "tools",
    "docs",
    "future_work",
    "assets",
}

# Pragmatic carveout (deliberately NOT a .gitignore parser — that is well beyond
# this tool's scope). A broken link whose resolved target points INTO one of
# these repo-relative directories is never reported. These hold gitignored
# generated artifacts (e.g. simulation figure outputs) that are absent on a
# fresh checkout, so a link into them must not gate — even from an error source.
IGNORED_PATHS: tuple[Path, ...] = (
    Path("assets/sim_outputs"),
)


def _under_ignored_path(resolved: Path, repo_root: Path) -> bool:
    """True if `resolved` is one of, or lives under, an `IGNORED_PATHS` dir."""
    try:
        rel = resolved.relative_to(repo_root)
    except ValueError:
        return False
    return any(rel == p or p in rel.parents for p in IGNORED_PATHS)


# External / non-file schemes to skip outright.
_SCHEME_RE = re.compile(r"^(?:[a-z][a-z0-9+.\-]*:)?//|^(?:https?|mailto):", re.IGNORECASE)

# Markdown inline link: [text](target). Target captured up to first ) or space.
# We deliberately do not try to handle titles `(url "title")`; targets here
# are file paths without titles.
_LINK_RE = re.compile(r"\[[^\]]*\]\(\s*([^)\s]+)\s*\)")

# Hashed id citation. `xxxxxx` literal placeholders are excluded downstream.
# Pattern is single-sourced from kb_index_lib (see import above) and now spans
# clm- / exp- / sup- / def- (INVARIANT-S12 extended ANY_NODE_ID_RE to include
# the def- prefix so the vocabulary register's def- ids are id-validity checked).
_ID_RE = kb_index_lib.ANY_NODE_ID_RE
_ID_PLACEHOLDERS = {"clm-xxxxxx", "exp-xxxxxx", "sup-xxxxxx", "def-xxxxxx"}


@dataclass(frozen=True)
class Finding:
    file: Path  # absolute path of the markdown file
    line: int
    kind: str  # "broken intra" | "broken inter" | "unknown id" | ...
    target: str
    detail: str = ""  # optional diagnostic appended to the printed line


def find_repo_root(start: Path) -> Path:
    """Walk up from `start` to the AVE-Core repo root.

    Identified by the repo-root Makefile + manuscript/ pair. Falls back to the
    git toplevel sentinel (`.git` file or dir) and finally to `start`.
    """
    for parent in (start, *start.parents):
        if (parent / "Makefile").is_file() and (parent / "manuscript").is_dir():
            return parent
    for parent in (start, *start.parents):
        if (parent / ".git").exists():
            return parent
    return start


def iter_markdown_files(root: Path):
    """Yield every `.md` file under `root`, skipping SKIP_DIRS at any depth."""
    for path in sorted(root.rglob("*.md")):
        parts = path.relative_to(root).parts
        if any(part in SKIP_DIRS for part in parts):
            continue
        if any(_contains_run(parts, run) for run in SKIP_SEGMENT_RUNS):
            continue
        yield path


def strip_code(text: str) -> str:
    """Blank out fenced code blocks and inline code spans, preserving line count.

    Lines inside ``` / ~~~ fences become empty; inline `code` spans are replaced
    by spaces. Newlines are preserved so reported line numbers stay accurate.
    """
    out_lines: list[str] = []
    fence: str | None = None  # active fence marker, "```" or "~~~"
    for raw in text.splitlines():
        stripped = raw.lstrip()
        if fence is None:
            if stripped.startswith("```") or stripped.startswith("~~~"):
                fence = stripped[:3]
                out_lines.append("")
                continue
            # Drop inline code spans on this line.
            out_lines.append(re.sub(r"`[^`]*`", lambda m: " " * len(m.group(0)), raw))
        else:
            # Inside a fence: blank everything until the closing fence.
            out_lines.append("")
            if stripped.startswith(fence):
                fence = None
    return "\n".join(out_lines)


def strip_fences(text: str) -> str:
    """Blank fenced code blocks ONLY; inline code spans are PRESERVED.

    The complement of `strip_code`, and the view the line-cite pass reads.
    `strip_code` blanks inline spans because the *link* regex must not see
    doc/example links; but the corpus's most common location-cite form IS an
    inline span (`` `path.md:42` ``), so blanking those made ~11k cites
    invisible end-to-end. Fences stay blanked: cites inside a fenced snippet
    are illustrative.

    Newlines are preserved so reported line numbers stay accurate.

    (Coverage split, deliberate: `verify-anchor-content.py` carries its own
    `strip_fenced` with the same semantics. The two tools stay independent —
    they run from different make targets and coupling them would make an
    advisory tool's failure able to take down a gating one.)
    """
    out_lines: list[str] = []
    fence: str | None = None
    for raw in text.splitlines():
        stripped = raw.lstrip()
        if fence is None:
            if stripped.startswith("```") or stripped.startswith("~~~"):
                fence = stripped[:3]
                out_lines.append("")
                continue
            out_lines.append(raw)
        else:
            out_lines.append("")
            if stripped.startswith(fence):
                fence = None
    return "\n".join(out_lines)


def strip_target(target: str) -> str:
    """Strip a trailing #anchor and :linenum suffix from a link target.

    NO PIN ARM, deliberately. The R2 pin marker is written OUTSIDE the link
    (`` [t](leaf.md:42) pin:`c4a546dc` ``), so a marker can never reach this
    function and the two passes cannot contradict each other on one token —
    the link pass resolves exactly the text it always did. A glued in-target
    form would have needed a strip arm here; that is one of the reasons the
    corpus's own token is the better one.
    """
    target = target.split("#", 1)[0]
    # Strip a trailing :NNN line-number suffix (path/file.md:42).
    target = re.sub(r":\d+$", "", target)
    return target


# Repo-root user-facing docs whose broken links/ids gate, alongside the KB tree.
_ERROR_SOURCE_ROOT_DOCS = {"README.md", "LIVING_REFERENCE.md", "AGENTS.md"}


def is_error_source(md_file: Path, repo_root: Path) -> bool:
    """True if broken links/ids from `md_file` should gate the exit code.

    Error sources are the canonical-authority surface: the KB tree
    (`manuscript/ave-kb/`, excluding its `session/` subtree) plus the
    repo-root user-facing docs. Everything else is warn-only.
    """
    try:
        rel = md_file.resolve().relative_to(repo_root)
    except ValueError:
        return False
    parts = rel.parts
    if parts[:2] == ("manuscript", "ave-kb"):
        return parts[2:3] != ("session",)
    return len(parts) == 1 and parts[0] in _ERROR_SOURCE_ROOT_DOCS


def load_known_ids(repo_root: Path) -> set[str] | None:
    """Load the set of node ids from `.index/claims.jsonl`, or None if absent.

    None signals the id-validity check should be skipped (e.g. the generated
    index is not present on this branch/worktree).
    """
    index_path = repo_root / "manuscript" / "ave-kb" / ".index" / "claims.jsonl"
    if not index_path.is_file():
        logger.info("id-validity check skipped: %s not present", index_path)
        return None
    ids: set[str] = set()
    with index_path.open(encoding="utf-8") as handle:
        for lineno, raw in enumerate(handle, 1):
            raw = raw.strip()
            if not raw:
                continue
            try:
                node = json.loads(raw)
            except json.JSONDecodeError:
                logger.warning("%s:%d unparseable JSON line, skipping", index_path, lineno)
                continue
            node_id = node.get("id")
            if isinstance(node_id, str):
                ids.add(node_id)
    logger.info("loaded %d node ids from %s", len(ids), index_path)
    return ids


def check_links(md_file: Path, body: str, repo_root: Path) -> list[Finding]:
    """Extract links from a code-stripped body and classify broken ones."""
    findings: list[Finding] = []
    for lineno, line in enumerate(body.splitlines(), 1):
        for match in _LINK_RE.finditer(line):
            raw_target = match.group(1)
            if _SCHEME_RE.search(raw_target):
                continue
            if raw_target.startswith("~"):
                continue  # home-dir path (~/.claude/...), not a repo link
            target = strip_target(raw_target)
            if not target:
                continue  # pure anchor link like (#section)
            if target.endswith(".tex"):
                continue  # derived LaTeX build artifact, not a nav target
            resolved = (md_file.parent / target).resolve()
            if _under_ignored_path(resolved, repo_root):
                continue  # gitignored generated-artifact dir — never gate
            try:
                resolved.relative_to(repo_root)
                is_intra = True
            except ValueError:
                is_intra = False
            if resolved.exists():
                continue
            kind = "broken intra" if is_intra else "broken inter"
            findings.append(Finding(md_file, lineno, kind, raw_target))
    return findings


def check_ids(md_file: Path, body: str, known_ids: set[str]) -> list[Finding]:
    """Flag cited hashed ids that do not resolve to a known node."""
    findings: list[Finding] = []
    for lineno, line in enumerate(body.splitlines(), 1):
        for match in _ID_RE.finditer(line):
            cited = match.group(1)
            if cited in _ID_PLACEHOLDERS:
                continue
            if cited not in known_ids:
                findings.append(Finding(md_file, lineno, "unknown id", cited))
    return findings


# --- line-cite parsing (`path.ext:NN`) --------------------------------------
#
# The corpus's load-bearing provenance form is a LOCATION cite `path.ext:NN`,
# written in three shapes. Before this pass the checker saw none of the line
# numbers and only one of the three paths:
#
#   form         written as                     path checked before / now
#   backticked   `path.ext:NN`                  NO  / yes (advisory)
#   link-in      [text](path.ext:NN)            yes / yes   (`strip_target`)
#   link-ext     [text](path.ext):NN            yes / yes   (KB house style)
#
# `strip_code` blanks inline spans before `_LINK_RE` runs, which is why the
# backticked form — the most common one — was invisible end-to-end.

# Extensions a `path.EXT:NN` location cite may name. Same family
# verify-anchor-content.py recognises, plus the typesetting/build extensions
# that appear in KB provenance cites.
_CITE_EXTS = (
    "md", "py", "tex", "sty", "cls", "json", "jsonl", "csv", "txt",
    "yaml", "yml", "toml", "cfg", "ini", "sh", "bib", "mk", "stl",
)
_CITE_PATH = r"(?:[\w.+@-]+/)*[\w.+@-]+\.(?:" + "|".join(_CITE_EXTS) + r")"
# `:42`, `:8-24`, `:133--147`. The trailing (?!\d) stops `:12` swallowing the
# leading digit of a following range half.
_CITE_LINE = r":(?P<start>\d+)(?:-{1,2}(?P<end>\d+))?(?!\d)"

# --- R2 author-declared pin marker: `` pin:`<sha>` `` ----------------------
#
# THE TOKEN IS THE CORPUS'S OWN. It was written on 2026-08-06 by the lane R2
# routed the question to, and it is canon at `manuscript/ave-kb/CONVENTIONS.md`,
# "Author-declared pin marker". This checker reads THAT token. It does not mint
# a second spelling for a concept the corpus already names — a homonym is
# exactly what ave-vocab-discipline's COINAGE rule forbids.
#
#     per `some-leaf.md:42` pin:`c4a546dc` — *"the sentence that line carried"*
#
# BINDING IS BY ADJACENCY, NOT PROXIMITY. The marker binds to the cite it
# directly follows — nothing but spaces or tabs may sit between the end of the
# cite token and the `pin:`. That is deliberately STRICTER than the convention's
# looser gloss ("the nearest location cite to its left on the same line"):
# adjacency is decidable by reading two adjacent tokens, so it cannot mis-bind
# across a row, which is the whole failure R2 named. A well-formed marker that
# is adjacent to NO cite is not silently dropped — it is reported
# (`orphan pin marker`), so the stricter rule fails loudly rather than quietly.
#
# WHY THE BACKTICKS EARN THEIR KEEP. The SHA is delimited by its own backticks,
# so ordinary sentence punctuation after a marker (`.` `,` `;` `)` `*` `**`, a
# table cell's `|`, end of line) cannot be swallowed into the SHA. A glued
# `@<sha>` form has no closing delimiter and does swallow it, turning a
# legitimate pin at the end of a sentence into a red light inside `make verify`.
# `test_pin_marker_survives_trailing_punctuation` pins that property open.
#
# CAPTURE IS PERMISSIVE, VALIDATION IS STRICT, DELIBERATELY. If the regex only
# matched well-formed hex, a typo (`` pin:`zzz` ``) would not be seen at all and
# an author who meant "exempt this" would get neither the exemption nor an
# error. So the capture takes any backticked body — and also an UNBACKTICKED
# `pin:<something>`, which is the other way to write the token wrong — and
# `_PIN_SHA_RE` decides. A marker that fails is reported
# (`malformed pin marker`) and its cite is checked as if unmarked.
_PIN_SHA_RE = re.compile(r"^[0-9a-f]{7,40}$")
# Anchored at the character just past a cite token. Group `pin` is the
# canonical backticked body; `badpin` is the unbackticked mis-spelling.
_PIN_AFTER_CITE_RE = re.compile(r"[ \t]*pin:(?:`(?P<pin>[^`\n]*)`|(?P<badpin>[^\s`]+))")
# Every marker-shaped token on a line, used ONLY to find well-formed markers
# that bound to no cite at all (`orphan pin marker`). The lookbehind is not
# decoration: unguarded, this matches inside `` spin:`...` `` — and "spin" is
# one of the most common words in this corpus.
_PIN_ANYWHERE_RE = re.compile(r"(?<![A-Za-z0-9_])pin:`(?P<pin>[^`\n]*)`")

# One inline code span (no nested backticks).
_INLINE_SPAN_RE = re.compile(r"`([^`\n]+)`")
# A span is a cite only when its ENTIRE stripped body is a path (+ optional
# line suffix). Anything else in the backticks — prose, a formula, a shell
# snippet — is not a location cite, and requiring a whole-body match is what
# keeps the backticked form's false-positive rate at zero-by-construction.
# The cite grammar is UNCHANGED by R2. The pin marker is a separate token that
# follows a cite (`` `leaf.md:42` pin:`c4a546dc` ``), so it is matched by
# adjacency in `iter_line_cites` rather than being folded in here — which is
# also why the LINK pass never sees it and `strip_target` needs no pin arm.
_BARE_CITE_RE = re.compile(r"^(?P<path>" + _CITE_PATH + r")(?:" + _CITE_LINE + r")?$")
_LINK_IN_CITE_RE = re.compile(
    r"\[[^\]]*\]\(\s*(?P<path>" + _CITE_PATH + r")" + _CITE_LINE + r"\s*\)"
)
_LINK_EXT_CITE_RE = re.compile(
    r"\[[^\]]*\]\(\s*(?P<path>" + _CITE_PATH + r")\s*\)" + _CITE_LINE
)

# A cite deliberately pinned to a PAST repo state is correct as written even
# when it does not resolve at HEAD (e.g. a frozen prereg's
# "§9 (as shipped on `c4a546dc`)", where the SHA predates a renumber).
#
# ── RESOLVED 2026-09-07 (R2 pin marker) ────────────────────────────────────
# The finding recorded below — "the corpus has NO machine-readable marker for a
# historical cite" — was already false when it was written down: the doc lane
# R2 routed the question to had defined `` pin:`<sha>` `` on 2026-08-06, at
# manuscript/ave-kb/CONVENTIONS.md, and only the CHECKER was missing. What
# landed here is the checker for THAT token — not a new one. (A first pass at
# this work minted a second spelling, `path:NN@<sha>`, because its coinage grep
# asked whether its own candidates collided and never asked whether a token
# already existed. Two spellings for one concept is a homonym; the corpus's own
# is the one that survives.)
#
# The pass now sorts every historical pin into THREE dispositions:
#
#   MARKER-EXEMPT    the cite is directly followed by `` pin:`<sha>` ``.
#                    Per-cite. Decided before HEAD path resolution, and granted
#                    only when the pin's claim is TRUE at its own commit.
#   HERITAGE-EXEMPT  no marker, but the LINE carries a backticked SHA — the
#                    line-scoped heuristic described below. GRANDFATHERED per
#                    R2, still honoured, counted separately.
#   CHECKED          everything else.
#
# The migration's progress is exactly the ratio of the first to the second, and
# it is printed on every run. The re-key ("exemption becomes marker-only once
# migrated") is a SWITCH, `HERITAGE_PIN_EXEMPTION` — built, DEFAULT-OFF-READY,
# left ON, with its cost printed on every ordinary run.
#
# The paragraph and the measurement below are PRESERVED as the record of the
# defect that motivated the marker. They describe the HERITAGE arm, which is
# still live for every unmarked cite. ────────────────────────────────────────
#
# FINDING, recorded rather than papered over: the corpus has NO machine-readable
# marker for a historical cite. The convention is free prose — "as shipped on",
# "at commit", "frozen at", "was correct at" — always adjacent to a BACKTICKED
# short hex SHA. That backticked SHA is therefore the only reliable signal, and
# this pass uses it: any line carrying one has its line-cites skipped.
#
# PRECISION DISCLOSURE — the exemption is LINE-SCOPED, and the KB's lines are
# not sentences. It skips EVERY line-cite on any line carrying a SHA anywhere,
# and the KB's ledger rows run hundreds to thousands of characters, routinely
# mixing one provenance SHA with several LIVE derivation cites. So the SHA is a
# row-level token, not a per-cite marker, and the rule's coverage is coarse.
#
# Measured 2026-08-05 on a pristine checkout of `d5a1b06b` (a dated snapshot,
# not a live census — see the NO CENSUS note in the module docstring; the
# itemisation lives in §5 of the docket fragment):
#   - 96 KB line-cites sit on a SHA-bearing line (3.6% of the KB's 2,681),
#     of which 85 are actually exempted here (the other 11 are skipped anyway,
#     by shape or unresolvable path);
#   - those 96 sit on just 55 distinct lines — 89 of them on lines of 500+
#     characters (median 1,655, max 6,112), and 66 share their line with at
#     least one other line-cite;
#   - only 7 of the 96 (7%) sit on a line that also carries one of the four
#     free-prose phrases this rule is modelled on; widening to every
#     historical-ish phrasing found by reading all 55 lines reaches 65 (68%).
#     Either way most exempted cites have no marker tying the SHA to the cite.
#   - it hides ZERO dead cites today: re-running the line check over the 85
#     with the exemption disabled yields 0 dead (9 blank-line advisory).
# Worked instances, each a live cite riding a SHA's exemption:
# `claim-quality-closure-roadmap.md:76` (a `57b36e5` provenance link plus THREE
# live derivation cites on one 625-char row), `manuscript/ave-kb/CLAUDE.md:75`
# (3,941 chars; a genuine historical pin on `:439` exempts the live
# `operators.md:54` beside it), `claim-quality-closure-roadmap.md:32`
# (2,731 chars, five SHAs, live `q_g47_path_b_k4_eigenmode.py:54`).
#
# FORWARD RISK, stated plainly: a dead cite that lands on a ledger row which
# happens to mention a commit passes this gate silently — and ledger rows are
# exactly where cite-rot concentrates. This is a precision disclosure, not a
# defect report (today's hidden-dead count is zero); the fix, if the residue
# ever bites, is an explicit per-cite historical marker, not a wider SHA regex.
#
# RE-MEASURED 2026-09-07 on a pristine `git worktree` of `5a36cea5`. ADDITIVE —
# the 2026-08-05 / `d5a1b06b` figures above are the historical record and stay
# as written. R2's ruling text quotes the "96" from that snapshot; it has since
# drifted, so cite THIS block for a current number and that one for the ruling.
#
#   OPERATIVE COUNTS — what the pass actually exempts (a cite reaches this
#   verdict only if it parses, resolves, and carries a `:NN`), read straight off
#   the printed `pin dispositions` line:
#     - corpus-wide : 480 HERITAGE-EXEMPT, 0 MARKER-EXEMPT, 13,644 CHECKED
#                     → migration 0/480 marker-keyed (0.0%) at landing
#     - KB tree only:  141 HERITAGE-EXEMPT, 0 MARKER-EXEMPT,  2,837 CHECKED
#
#   PARSED COUNTS — every `:NN` cite this file's grammar sees on a SHA-bearing
#   line, resolvable or not (the population a migration sweep must walk):
#     - KB only     : 156 line-cites on  74 SHA-bearing lines
#     - corpus-wide : 525 line-cites on 271 SHA-bearing lines,
#                     182 of those lines longer than 500 characters
#
#   SECOND METHOD, per the grep-completeness rule — an independent scan that
#   does NOT import this module (git ls-files + its own fence stripper + a
#   contiguous `path.ext:NN` regex): KB 115 cites / 56 lines, corpus 585 / 298,
#   168 long lines. The two disagree BY CONSTRUCTION and the gap is the
#   definition, not an error: method 1 counts the `[t](path):NN` link-ext form
#   (KB house style) that a contiguous regex cannot see, and method 2 counts
#   non-backticked cites in plain prose that method 1's whole-span rule
#   rejects. Method 1 is the operative one — the gate exempts only what it
#   parses. Neither is quotable without its inclusion rule.
#
#   HIDDEN-DEAD, re-run: still ZERO. Re-running the whole corpus with
#   `--no-heritage-pin-exemption` demotes all 480 to CHECKED and the dead count
#   is unchanged at 11 (gating 0); only the blank-line advisory moves,
#   1,112 → 1,144. So the heritage arm is still hiding no dead cite today.
_HISTORICAL_PIN_RE = re.compile(r"`[0-9a-f]{7,40}`")

# Sibling-repo cite target (`AVE-Foo/...`, `Applied-Vacuum-Engineering/...`).
# Sibling checkouts are legitimately absent on a fresh CI checkout, so their
# lines can never be resolved — skipped, exactly as md inter-repo links are.
_CITE_SIBLING_RE = re.compile(r"(?:^|/)(?:AVE-[A-Za-z0-9-]+|Applied-Vacuum-Engineering)/")

# Target shapes that are PATTERNS, not paths: `vol3/.../leaf.md` elision,
# `chiral_lattice_v9..v17.py` ranges, globs. The kbleaf pass resolves these as
# globs; a location cite into one has no single line to check, so it is skipped.
#
# A bare `..` SEGMENT is NOT a pattern — it is an ordinary parent-dir hop, and
# `../vol1/.../leaf.md`-style relative cites are the KB house style: 639 of the
# KB's 2,650 line-cites (24%) carry one. An earlier `\.{2,}` form of this regex
# swallowed all of them; the mutation test in
# tools/tests/test_verify_md_links.py is what surfaced it (the planted
# link-ext cite silently never fired). Hence: 3+ dots anywhere, or 2 dots
# inside a segment that is not exactly `..`.
_CITE_GLOB_RE = re.compile(r"\.{3,}|[*\[\]]")


def _is_pattern_segment(segment: str) -> bool:
    """True if a path segment is a glob / elision rather than a real name."""
    return bool(_CITE_GLOB_RE.search(segment)) or (".." in segment and segment != "..")

# Repo-relative dirs whose contents are gitignored ephemera — a cite into one
# can never resolve on a fresh checkout. Kept SEPARATE from `IGNORED_PATHS`
# (used by the link pass) so this pass's carveout cannot silently widen the
# existing link check's blind spot.
_CITE_EPHEMERAL_DIRS = (".agents", ".claude/worktrees", "build")


@dataclass(frozen=True)
class LineCite:
    """One `path.ext:NN` location cite, as written."""

    lineno: int  # line in the CITING file
    form: str  # "backticked" | "link-in" | "link-ext"
    path: str  # target path as written
    start: int | None  # cited line, or None when the cite carries no :NN
    end: int | None  # range end for `:NN-MM`, else == start
    pinned: bool  # HERITAGE: the citing LINE carries a backticked SHA
    pin: str | None = None  # MARKER: the ``pin:`...` `` body directly after it
    pin_backticked: bool = True  # False for the unbackticked mis-spelling

    @property
    def as_written(self) -> str:
        if self.start is None:
            base = self.path
        elif self.end is not None and self.end != self.start:
            base = f"{self.path}:{self.start}-{self.end}"
        else:
            base = f"{self.path}:{self.start}"
        if self.pin is None:
            return base
        return f"{base} pin:`{self.pin}`" if self.pin_backticked else f"{base} pin:{self.pin}"

    @property
    def pin_wellformed(self) -> bool:
        """True iff the marker is BACKTICKED and its body is a short SHA.

        The backticks are load-bearing, not decoration: they are what delimits
        the SHA from the sentence around it. `` pin:c4a546dc. `` has no closing
        delimiter, so accepting it would re-open exactly the punctuation-eating
        defect the token was chosen to avoid. It is reported, not accepted.
        """
        return (
            self.pin is not None
            and self.pin_backticked
            and bool(_PIN_SHA_RE.match(self.pin))
        )


def _pin_after(line: str, pos: int) -> tuple[str | None, bool, int]:
    """The marker bound to a cite ending at `pos`, and where it ends.

    Adjacency, not proximity: only spaces/tabs may separate the cite's last
    character from the `pin:`. Returns (body as written, was-backticked, end
    offset), or (None, True, pos) when nothing is bound.
    """
    match = _PIN_AFTER_CITE_RE.match(line, pos)
    if not match:
        return None, True, pos
    if match.group("pin") is not None:
        return match.group("pin"), True, match.end()
    return match.group("badpin"), False, match.end()


def iter_line_cites(text: str):
    """Yield every `LineCite` in `text` (fences blanked, inline spans kept).

    A cite carries `pin` when a ``pin:`<sha>` `` token sits DIRECTLY after it.
    """
    for lineno, line in enumerate(strip_fences(text).splitlines(), 1):
        # ★ A MARKER IS NOT PROSE. The corpus's marker spells its SHA inside
        # backticks, so a marked row would otherwise trip the row-scoped
        # HERITAGE rule on its own marker and re-exempt the whole row — handing
        # back exactly the coarseness R2 named. The heritage rule keys on a
        # backticked SHA written as PROVENANCE PROSE, so markers are masked out
        # before it is asked. A row that also carries a real prose SHA still
        # reads as heritage, which is what keeps the migration flag-day-free.
        pinned = bool(_HISTORICAL_PIN_RE.search(_PIN_ANYWHERE_RE.sub("", line)))
        for regex, form in ((_LINK_EXT_CITE_RE, "link-ext"), (_LINK_IN_CITE_RE, "link-in")):
            for match in regex.finditer(line):
                start = int(match.group("start"))
                end = int(match.group("end")) if match.group("end") else start
                pin, ticked, _ = _pin_after(line, match.end())
                yield LineCite(lineno, form, match.group("path"), start, end, pinned, pin, ticked)
        for span in _INLINE_SPAN_RE.finditer(line):
            match = _BARE_CITE_RE.match(span.group(1).strip())
            if not match:
                continue
            start = int(match.group("start")) if match.group("start") else None
            end = int(match.group("end")) if match.group("end") else start
            pin, ticked, _ = _pin_after(line, span.end())
            yield LineCite(
                lineno, "backticked", match.group("path"), start, end, pinned, pin, ticked
            )


def iter_orphan_pins(text: str):
    """Yield (lineno, sha) for every WELL-FORMED marker that failed to bind.

    The adjacency rule cannot mis-bind, but it CAN decline to bind — a marker
    written a few words away from the cite it was meant for. That must not be
    silent, or the stricter rule would just be the quieter one.

    TWO NARROWINGS, both there to keep this from firing on writing ABOUT the
    token rather than writing WITH it, and both testable in either direction:

      - the body must be a well-formed short SHA. `` pin:`<sha>` `` in running
        prose is a description, not a marker anyone meant literally.
      - the LINE must also carry at least one location cite. A marker that
        misses its cite misses it on a line that has one; a `pin:` on a line
        with no cite at all is documentation (this repo's own CONVENTIONS.md
        spells the token out in a table), and the convention is same-line
        anyway, so there is nothing on that line it could have been aimed at.
    """
    for lineno, line in enumerate(strip_fences(text).splitlines(), 1):
        bound: set[int] = set()
        cites = 0
        for regex in (_LINK_EXT_CITE_RE, _LINK_IN_CITE_RE):
            for match in regex.finditer(line):
                cites += 1
                pin, _, end = _pin_after(line, match.end())
                if pin is not None:
                    bound.add(end)
        for span in _INLINE_SPAN_RE.finditer(line):
            if not _BARE_CITE_RE.match(span.group(1).strip()):
                continue
            cites += 1
            pin, _, end = _pin_after(line, span.end())
            if pin is not None:
                bound.add(end)
        if not cites:
            continue
        for match in _PIN_ANYWHERE_RE.finditer(line):
            if match.end() in bound:
                continue
            if _PIN_SHA_RE.match(match.group("pin")):
                yield lineno, match.group("pin")


def cite_target_uncheckable(target: str) -> bool:
    """True if a cite target cannot be resolved to one repo file, by shape.

    Home-dir paths, sibling-repo paths, glob/elision patterns, and gitignored
    ephemeral trees. These are skipped by BOTH new passes — they are not
    findings, they are out of scope.
    """
    if target.startswith(("~", "/")):
        return True
    if _CITE_SIBLING_RE.search(target):
        return True
    parts = tuple(p for p in target.split("/") if p and p != ".")
    if any(_is_pattern_segment(p) for p in parts):
        return True
    if any(p in _CITE_EPHEMERAL_DIRS for p in parts):
        return True
    if any(
        parts[i : i + len(ignored.parts)] == ignored.parts
        for ignored in IGNORED_PATHS
        for i in range(len(parts))
    ):
        return True
    return False


def resolve_cite_candidates(
    target: str,
    md_file: Path,
    repo_root: Path,
    file_index: dict[str, list[tuple[str, ...]]],
) -> list[Path]:
    """Every repo file a cite target could name — UNION of two resolutions.

    (a) DIRECT: relative to the citing file's directory, then to the repo root.
    (b) SUFFIX-INDEX: any indexed file whose path TAIL matches the cited
        segments — the same resolution the kbleaf pass uses (Rule 14: one
        resolution model for the repo, not two), and what makes the corpus's
        bare-basename shorthand (`` `master-equation.md:78` ``) resolvable.

    The union is deliberate and is what makes the line check zero-FP: a bare
    `CLAUDE.md:182` names SOME `CLAUDE.md`, and it is only a real dead cite if
    NO candidate is that long. Direct-only resolution would pick the repo-root
    one (125 lines) and fire falsely against the KB one (353).
    """
    found: set[Path] = set()
    for base in (md_file.parent, repo_root):
        candidate = (base / target).resolve()
        if candidate.is_file():
            found.add(candidate)
    parts = tuple(p for p in target.split("/") if p and p != ".")
    if parts:
        for indexed in file_index.get(parts[-1], ()):
            if indexed[-len(parts):] == parts:
                found.add(repo_root / Path(*indexed))
    return sorted(found)


class TargetLineCache:
    """Split cite-target files into lines once each."""

    def __init__(self) -> None:
        self._lines: dict[Path, list[str]] = {}

    def lines(self, path: Path) -> list[str]:
        if path not in self._lines:
            try:
                text = path.read_text(encoding="utf-8", errors="replace")
            except OSError:
                self._lines[path] = []
            else:
                self._lines[path] = text.splitlines()
        return self._lines[path]

    def count(self, path: Path) -> int:
        return len(self.lines(path))


# A cited line that exists but carries nothing to cite: empty, or pure
# structural decoration (blockquote marker, list bullet, table rule, hr).
_CONTENTLESS_LINE_RE = re.compile(r"^[\s>*+\-|#=_~`]*$")

# --- pin-marker validation: does the pin RESOLVE AT ITS OWN SHA? ------------
#
# ★ THE MARKER MUST NOT BE AN OPT-OUT BY ASSERTION. Checking only that the SHA
# names *some* commit makes the gate opt-out-able: append any real short SHA to
# any dead cite and it goes quiet, whether or not the file existed at that
# commit or ever had that many lines. So a marker is honoured only when the
# claim it makes is TRUE — `<path>` exists in the tree at `<sha>` AND has at
# least `<line>` lines. That is exactly the hand-verification the migration
# lane's allow-list encodes ("read it at HEAD, then read it at the SHA"),
# mechanised.
#
# Path resolution at the pinned SHA mirrors `resolve_cite_candidates` at HEAD:
# direct (relative to the citing file, then to the repo root) UNION suffix
# match over the pinned tree. The corpus's bare-basename shorthand
# (`` `master-equation.md:78` ``) has to resolve the same way in both eras or
# the gate would contradict itself across time.
#
# ── THE FAIL-OPEN BOUNDARY, drawn deliberately ─────────────────────────────
# This check reads the object store, and this tool ships inside `make verify`,
# where a false FAIL red-lights the repo. "I cannot look" must never read as
# "the pin is bad". So:
#
#   no git on PATH / not a checkout    -> validation DISABLED wholesale, every
#                                         marker exempt, printed loudly.
#   SHA absent, checkout INCOMPLETE    -> UNVERIFIED (exempt, counted).
#     (shallow clone, or a partial /     A truncated history legitimately does
#      promisor clone)                   not have the commit; that is a fact
#                                        about the checkout, not the cite.
#   SHA absent, checkout COMPLETE      -> GATING `unknown pin sha`.
#                                         Full history and the commit is not in
#                                         it: the SHA is wrong, or it names a
#                                         state nobody can read — either way the
#                                         pin cannot be honoured. CI checks out
#                                         with `fetch-depth: 0`
#                                         (.github/workflows/verify.yml), so the
#                                         gating arm is the live one where it
#                                         matters.
#   SHA present, tree unreadable       -> UNVERIFIED (a tree-filtered clone).
#   SHA present, path/line absent      -> GATING
#                                         `pin does not resolve at its own sha`.
#   SHA present, path present, blob
#     unreadable (blobless clone)      -> UNVERIFIED.
#
# An AMBIGUOUS short SHA fails as absent, deliberately: a prefix matching two
# objects names no single state. Git's own message is carried into the finding
# so the author reads "ambiguous", not "nonexistent" — the fix is to lengthen
# the marker, not to delete it.

PIN_OK = "ok"  # the pin's claim is true
PIN_NO_SHA = "no-sha"  # complete checkout, no such commit
PIN_NO_RESOLVE = "no-resolve"  # commit is here; path/line is not, at that commit
PIN_UNVERIFIED = "unverified"  # cannot answer -> exempt, never a manufactured fail


class PinStore:
    """Answers 'does `<path>` have line `<n>` at `<sha>`?' from the object store.

    `enabled` is False when there is no store to ask at all; every verdict is
    then PIN_UNVERIFIED. `incomplete` is True for a shallow or partial clone,
    which is the ONLY condition under which a missing commit fails open.
    """

    def __init__(self, repo_root: Path, enabled: bool = True) -> None:
        self.repo_root = repo_root
        self.enabled = enabled and self._probe()
        self.incomplete = self._probe_incomplete() if self.enabled else False
        self._commits: dict[str, bool] = {}
        self._trees: dict[str, dict[str, list[tuple[str, ...]]] | None] = {}
        self._blob_lines: dict[tuple[str, str], int | None] = {}

    # -- plumbing ----------------------------------------------------------
    def _git(self, *args: str) -> tuple[int, str]:
        try:
            done = subprocess.run(
                ["git", "-C", str(self.repo_root), *args],
                capture_output=True,
                text=True,
                timeout=60,
            )
        except (OSError, subprocess.SubprocessError) as exc:
            logger.warning("git %s failed: %s", " ".join(args), exc)
            return 1, ""
        return done.returncode, done.stdout

    def _probe(self) -> bool:
        rc, _ = self._git("rev-parse", "--git-dir")
        if rc != 0:
            logger.info("pin validation disabled (%s is not a git checkout)", self.repo_root)
        return rc == 0

    def _probe_incomplete(self) -> bool:
        rc, out = self._git("rev-parse", "--is-shallow-repository")
        if rc == 0 and out.strip() == "true":
            logger.info("shallow checkout: a missing pin sha will fail OPEN")
            return True
        rc, out = self._git("config", "--get-regexp", r"^remote\..*\.(promisor|partialclonefilter)$")
        if rc == 0 and out.strip():
            logger.info("partial clone: a missing pin sha will fail OPEN")
            return True
        return False

    def commit_exists(self, sha: str) -> bool:
        if sha not in self._commits:
            rc, out = self._git("cat-file", "-t", f"{sha}^{{commit}}")
            self._commits[sha] = rc == 0 and out.strip() == "commit"
        return self._commits[sha]

    def _tree_index(self, sha: str) -> dict[str, list[tuple[str, ...]]] | None:
        """basename -> [path segment tuples] for the whole tree at `sha`."""
        if sha not in self._trees:
            rc, out = self._git("ls-tree", "-r", "--name-only", sha)
            if rc != 0 or not out.strip():
                self._trees[sha] = None
            else:
                index: dict[str, list[tuple[str, ...]]] = {}
                for raw in out.splitlines():
                    parts = tuple(raw.split("/"))
                    index.setdefault(parts[-1], []).append(parts)
                self._trees[sha] = index
        return self._trees[sha]

    def _lines_at(self, sha: str, path: str) -> int | None:
        key = (sha, path)
        if key not in self._blob_lines:
            rc, out = self._git("cat-file", "blob", f"{sha}:{path}")
            self._blob_lines[key] = None if rc != 0 else len(out.splitlines())
        return self._blob_lines[key]

    # -- the verdict -------------------------------------------------------
    def verdict(
        self, sha: str, target: str, cited_last: int, citing_dir: str
    ) -> tuple[str, str]:
        """Is the pin's claim true? Returns (one of PIN_*, human detail)."""
        if not self.enabled:
            return PIN_UNVERIFIED, "no object store to ask"
        if not self.commit_exists(sha):
            if self.incomplete:
                return PIN_UNVERIFIED, "commit absent, and this checkout is shallow/partial"
            return PIN_NO_SHA, f"`{sha}` resolves to no commit in this repo"

        # Fast path: the two direct resolutions, without listing the whole tree.
        direct: list[str] = []
        for base in (citing_dir, ""):
            joined = posixpath.normpath(posixpath.join(base, target))
            if joined not in direct and not joined.startswith("..") and joined not in (".", ""):
                direct.append(joined)
        for candidate in direct:
            count = self._lines_at(sha, candidate)
            if count is not None and count >= cited_last:
                return PIN_OK, candidate

        index = self._tree_index(sha)
        if index is None:
            return PIN_UNVERIFIED, "tree at that commit is not readable here"

        parts = tuple(part for part in target.split("/") if part and part != ".")
        candidates = {
            candidate
            for candidate in direct
            if tuple(candidate.split("/")) in index.get(candidate.split("/")[-1], ())
        }
        for indexed in index.get(parts[-1], ()) if parts else ():
            if indexed[-len(parts):] == parts:
                candidates.add("/".join(indexed))
        if not candidates:
            return PIN_NO_RESOLVE, f"no file matching `{target}` exists at `{sha}`"

        longest = -1
        for candidate in sorted(candidates):
            count = self._lines_at(sha, candidate)
            if count is None:
                return PIN_UNVERIFIED, f"blob for `{candidate}` is not readable here"
            longest = max(longest, count)
            if count >= cited_last:
                return PIN_OK, candidate
        return (
            PIN_NO_RESOLVE,
            f"`{target}` exists at `{sha}` but is only {longest} lines "
            f"({len(candidates)} candidate(s))",
        )


class _DisabledPinStore:
    """The no-store stand-in: every pin is UNVERIFIED, so every pin is honoured.

    Used when the caller passes no store at all (library callers, tests that are
    not about the object store). Never manufactures a failure.
    """

    enabled = False
    incomplete = False

    def verdict(self, *_args, **_kwargs) -> tuple[str, str]:
        return PIN_UNVERIFIED, "pin validation not enabled for this run"


_NULL_PIN_STORE = _DisabledPinStore()


# ── HERITAGE EXEMPTION SWITCH — FLIPPED OFF 2026-09-12 ─────────────────────
# R2: "the gate's exemption re-keys to marker-only once migrated". The corpus
# half landed (the four TRUE-PIN cites are marked), so the terminal step ran.
#
# HISTORICAL RECORD OF THE PRE-FLIP STATE, kept because it is the record:
# from 2026-08-05 to 2026-09-12 a cite was exempt when the LINE IT SAT ON
# carried a backticked SHA anywhere — line-scoped, not cite-scoped. On rows
# thousands of characters long that exempted cites having nothing to do with
# the SHA. That coarseness is the defect R2 exists to end. It is now gone: the
# per-cite `` pin:`<sha>` `` marker is the ONLY route to an exemption, and a
# marker is honoured only when its claim resolves at its own SHA.
#
# WHAT THE FLIP COST, measured on the live corpus at 42dd7b40 rather than
# argued — the same `_cite_verdict` the CHECKED arm uses, run over all 485:
#   CHECKED 13,644 -> 14,129 (+485)   HERITAGE-EXEMPT 485 -> 0
#   dead line cite 11 -> 11 (+0), and the SAME ELEVEN cites byte for byte
#   GATING dead 0 -> 0                exit 0 -> 0
#   blank line cite 1,112 -> 1,144 (+32, advisory, never gating)
# Zero cites newly gate. The heritage arm was hiding no dead cite on flip day.
#
# ⚠ THE FLIP WAS NEVER THE ONE LINE THIS COMMENT PROMISED. `main()` bound
# `heritage_exemption=not args.no_heritage_pin_exemption`, reading the CLI flag
# and NOT this constant, so setting it False alone would have changed nothing
# that `make verify` runs. The constant is now the default and the flag an
# override, which is what makes the line below load-bearing.
HERITAGE_PIN_EXEMPTION = False  # ← flipped 2026-09-12 (R2 terminal step)


# (source repo-relative path, cite as written) pairs adjudicated
# report-don't-fix — a `dead line cite` that is KNOWN and deliberately left, e.g.
# inside a byte-frozen document. Mirrors WAIVED_KBLEAF, including its
# anti-rot property: a waiver matching no live dead cite is itself a GATING
# `stale line-cite waiver` failure, so the list can only shrink truthfully.
#
# EMPTY at landing: the gating (error-source) dead-line-cite set measured ZERO
# at this HEAD, so no waiver is needed yet. See the posture note in the docket
# fragment 2026-08-05-cite-rot-line-existence.md.
WAIVED_LINE_CITE: frozenset[tuple[str, str]] = frozenset()


def _cite_verdict(cite: LineCite, candidates: list[Path], line_cache: TargetLineCache) -> str:
    """The line-existence verdict for one resolved cite: dead / blank / ok.

    ONE function, two callers: the CHECKED arm reports it, and the
    HERITAGE-EXEMPT arm computes it silently to measure what turning the
    exemption off would cost. Sharing the function is what makes the printed
    flip preview the same arithmetic as the flip.
    """
    cited_last = max(cite.start, cite.end or cite.start)
    if max(line_cache.count(c) for c in candidates) < cited_last:
        return "dead"
    if len(candidates) == 1:
        lines = line_cache.lines(candidates[0])
        if cite.start <= len(lines) and _CONTENTLESS_LINE_RE.match(lines[cite.start - 1]):
            return "blank"
    return "ok"


def check_line_cites(
    md_file: Path,
    text: str,
    repo_root: Path,
    file_index: dict[str, list[tuple[str, ...]]],
    line_cache: TargetLineCache,
    waived: frozenset[tuple[str, str]] = WAIVED_LINE_CITE,
    heritage_exemption: bool = HERITAGE_PIN_EXEMPTION,
    pin_store: "PinStore | None" = None,
) -> tuple[list[Finding], Counter, set[tuple[str, str]]]:
    """Check every `path.ext:NN` location cite in one markdown file.

    Emits three finding kinds:

    `dead line cite` — GATING (per `is_error_source`, like broken-intra).
      NO resolvable candidate file has the cited line. Zero-false-positive by
      construction: the check is "does line N exist", the candidate set is the
      UNION of every resolution the cite could mean, and the verdict fires only
      when EVERY candidate is too short. It does not attempt content drift —
      that stays with the advisory `verify-anchor-content.py`.

    `blank line cite` — ADVISORY, never gating. The cited line exists but is
      empty or pure decoration, so the cite anchors nothing. Almost always
      one-line drift (the content sits at N+1). Advisory because its
      error-source population is a real pre-existing backlog and a gate that
      red-lights merge on day one gets bypassed, not obeyed.

    `broken backtick path` — ADVISORY, never gating. A backticked-bare cite
      whose path resolves nowhere. This form was never path-checked before, so
      turning it on surfaces a pre-existing backlog, heavy with
      pattern/placeholder strings like `volN/claim-quality.md`. Reported and
      counted; not gated. Link-form cites are NOT re-reported here — the
      existing link pass already owns their paths.

    Counts for both advisory kinds live in the docket fragment named in the
    module docstring, not here — see the NO CENSUS IS BAKED note there. Every
    run prints the live populations.

    Returns (findings, stats, matched_waiver_keys).
    """
    findings: list[Finding] = []
    stats: Counter = Counter()
    matched: set[tuple[str, str]] = set()
    try:
        rel_source = str(md_file.resolve().relative_to(repo_root))
    except ValueError:
        rel_source = str(md_file)

    try:
        citing_dir = str(md_file.resolve().parent.relative_to(repo_root))
    except ValueError:
        citing_dir = ""
    if citing_dir == ".":
        citing_dir = ""

    for lineno, sha in iter_orphan_pins(text):
        stats["pin_orphan"] += 1
        findings.append(
            Finding(
                md_file,
                lineno,
                "orphan pin marker",
                f"pin:`{sha}`",
                "a marker binds to the cite DIRECTLY before it; this one binds to none",
            )
        )

    for cite in iter_line_cites(text):
        if cite_target_uncheckable(cite.path):
            stats["skipped_shape"] += 1
            continue

        # DISPOSITION 1 — MARKER-EXEMPT. Decided BEFORE path resolution at HEAD:
        # a cite pinned to a past state is expected not to resolve at HEAD, so
        # running it through the HEAD resolver would only manufacture a `broken
        # backtick path` advisory for a cite that is correct as written. The
        # claim is instead checked where it is made — at its own SHA.
        if cite.pin is not None:
            if not cite.pin_wellformed:
                stats["pin_malformed"] += 1
                findings.append(
                    Finding(
                        md_file,
                        cite.lineno,
                        "malformed pin marker",
                        cite.as_written,
                        "marker must be pin:`<7-40 lowercase hex>` "
                        "(backticks included); cite is NOT exempt",
                    )
                )
                # Fall through. An unreadable marker buys nothing — the cite is
                # checked exactly as if it had never carried one.
            elif cite.start is None:
                stats["pin_malformed"] += 1
                findings.append(
                    Finding(
                        md_file,
                        cite.lineno,
                        "malformed pin marker",
                        cite.as_written,
                        "a pin needs a `:NN` to pin; cite is NOT exempt",
                    )
                )
            else:
                # ★ THE PIN MUST BE TRUE, NOT MERELY WELL FORMED. Without this
                # the marker is an opt-out by assertion: any dead cite goes
                # quiet the moment any real SHA is appended.
                cited_last = max(cite.start, cite.end or cite.start)
                store = pin_store if pin_store is not None else _NULL_PIN_STORE
                verdict, detail = store.verdict(cite.pin, cite.path, cited_last, citing_dir)
                if verdict == PIN_NO_SHA:
                    stats["pin_unknown_sha"] += 1
                    findings.append(
                        Finding(md_file, cite.lineno, "unknown pin sha", cite.as_written, detail)
                    )
                    continue
                if verdict == PIN_NO_RESOLVE:
                    stats["pin_unresolved"] += 1
                    findings.append(
                        Finding(
                            md_file,
                            cite.lineno,
                            "pin does not resolve at its own sha",
                            cite.as_written,
                            detail,
                        )
                    )
                    continue
                if verdict == PIN_UNVERIFIED:
                    stats["pin_unverified"] += 1
                stats["exempt_marker"] += 1
                continue
        candidates = resolve_cite_candidates(cite.path, md_file, repo_root, file_index)
        if not candidates:
            if cite.form == "backticked":
                stats["unresolved_backtick_path"] += 1
                findings.append(
                    Finding(md_file, cite.lineno, "broken backtick path", cite.as_written)
                )
            else:
                stats["unresolved_link_path"] += 1  # the link pass owns this one
            continue
        if cite.start is None:
            stats["path_only"] += 1  # `path.md` with no :NN — path checked, no line
            continue
        # DISPOSITION 2 — HERITAGE-EXEMPT. The pre-R2 line-scoped heuristic:
        # no marker on this cite, but the LINE carries a backticked SHA
        # somewhere. Grandfathered per R2 and still honoured, but counted on
        # its own so the migration's remaining distance is a printed number.
        #
        # While the exemption is ON the would-be verdict is computed anyway and
        # counted, never reported: that is what turns "what does the flip cost?"
        # from an argument into a measurement on the live corpus. The verdict
        # comes from `_cite_verdict`, the SAME function the CHECKED arm below
        # uses, so the preview cannot drift from the thing it previews.
        if cite.pinned:
            if heritage_exemption:
                stats["exempt_heritage"] += 1
                kind = _cite_verdict(cite, candidates, line_cache)
                if kind == "dead":
                    stats["heritage_flip_dead"] += 1
                    if is_error_source(md_file, repo_root):
                        stats["heritage_flip_dead_gating"] += 1
                elif kind == "blank":
                    stats["heritage_flip_blank"] += 1
                continue
            stats["heritage_demoted"] += 1

        # DISPOSITION 3 — CHECKED.
        stats["checked"] += 1
        kind = _cite_verdict(cite, candidates, line_cache)
        if kind == "dead":
            key = (rel_source, cite.as_written)
            longest = max(line_cache.count(c) for c in candidates)
            detail = f"longest of {len(candidates)} candidate(s): {longest} lines"
            if key in waived:
                matched.add(key)
                findings.append(
                    Finding(md_file, cite.lineno, "waived line cite", cite.as_written, detail)
                )
                stats["dead_waived"] += 1
            else:
                findings.append(
                    Finding(md_file, cite.lineno, "dead line cite", cite.as_written, detail)
                )
                stats["dead"] += 1
        elif kind == "blank":
            # Advisory. Only meaningful when the cite resolves to exactly one
            # file — with several candidates there is no single line to inspect.
            stats["blank"] += 1
            findings.append(
                Finding(
                    md_file,
                    cite.lineno,
                    "blank line cite",
                    cite.as_written,
                    "cited line is empty / decoration-only",
                )
            )
    return findings, stats, matched


# --- \kbleaf{...} citation checking (manuscript .tex) -----------------------

_KBLEAF_RE = re.compile(r"\\kbleaf\{([^}]*)\}")

# LaTeX line comment (an unescaped %). \% is literal percent, not a comment.
_TEX_COMMENT_RE = re.compile(r"(?<!\\)%.*")

# A leaf name split across a literal \texttt{...-} prefix and a \kbleaf tail.
# The tail alone resolves against the WRONG leaf (or nothing), so the pattern
# defeats path checking — cite the full name in one \kbleaf{} (seqsplit
# already provides the any-character line breaking the split was doing by hand).
_SPLIT_KBLEAF_RE = re.compile(r"\\texttt\{[^{}]*-\}\s*\\kbleaf\{[^}]*\}")

# Trailing location suffixes stripped before resolution:
#   :42  :8-24  :133--147          (line / line-range cites)
#   ::member  :member()  ::member() (python symbol cites on a path)
_TEX_LINE_SUFFIX_RE = re.compile(r":\d+(?:-{1,2}\d+)?$")
_TEX_MEMBER_SUFFIX_RE = re.compile(r"(?:::|:)[A-Za-z_][\w.]*(?:\(\))?$")

# LaTeX escapes that appear inside path arguments.
_TEX_ESCAPES = ((r"\_", "_"), (r"\&", "&"), (r"\%", "%"), (r"\#", "#"), (r"\$", "$"))

# An argument containing any of these (after suffix stripping) is not a path:
# whitespace / parens / assignment (shell snippets, formulae), $ (math), or a
# residual :: (unstripped symbol form).
_TEX_UNCHECKABLE_RE = re.compile(r"[\s()=$`]|::")

# A bare (single-segment) argument is only checkable when it names a file by a
# known extension; extensionless bare tokens (skill names, identifiers, leaf
# STEMS like `theorem-3-1-q-factor`) are typography, not checkable paths.
_BARE_CHECKABLE_EXTS = {
    ".md", ".py", ".tex", ".sty", ".json", ".jsonl",
    ".yaml", ".yml", ".csv", ".txt", ".stl",
}

_SIBLING_REPO_RE = re.compile(r"^AVE-[A-Za-z0-9-]+/")

# Ephemeral / generated dirs excluded from the kbleaf TARGET index. Narrower
# than SKIP_DIRS: `_archive` and `.index` ARE valid citation targets (tracked,
# present on a fresh checkout); gitignored or generated trees are not.
_TARGET_INDEX_SKIP = {".venv", "venv", ".git", "build", "node_modules", ".agents", "__pycache__"}

# (source repo-relative path, verbatim \kbleaf argument) pairs adjudicated
# report-don't-fix: the dead cite is KNOWN and tracked here, and the correct
# canonical target is an open judgment call. A waived pair that no longer
# matches a live dead cite is a STALE WAIVER and fails the run, so this list
# can only shrink truthfully — it cannot silently outlive its subject.
WAIVED_KBLEAF: frozenset[tuple[str, str]] = frozenset({
    # p2.9b_goldstone_proof.md never existed in tracked history (it named a
    # gitignored session-handoff-era artifact); the four-lemma Goldstone
    # derivation needs a canonical tracked anchor before this cite can be
    # repointed. See the PR that introduced this pass for the adjudication.
    (
        "manuscript/vol_2_subatomic/chapters/06_electroweak_and_higgs.tex",
        r"p2.9b\_goldstone\_proof.md",
    ),
})


def iter_tex_files(root: Path):
    """Yield every `manuscript/**/*.tex`, with the same skips as the md crawl."""
    manuscript = root / "manuscript"
    if not manuscript.is_dir():
        return
    for path in sorted(manuscript.rglob("*.tex")):
        parts = path.relative_to(root).parts
        if any(part in SKIP_DIRS for part in parts):
            continue
        if any(_contains_run(parts, run) for run in SKIP_SEGMENT_RUNS):
            continue
        yield path


def normalize_kbleaf_target(raw: str) -> str:
    r"""LaTeX-unescape a \kbleaf argument and strip :line / :symbol suffixes."""
    target = raw.strip()
    for esc, char in _TEX_ESCAPES:
        target = target.replace(esc, char)
    target = _TEX_LINE_SUFFIX_RE.sub("", target)
    target = _TEX_MEMBER_SUFFIX_RE.sub("", target)
    return target


def build_kbleaf_target_index(
    repo_root: Path,
) -> tuple[dict[str, list[tuple[str, ...]]], dict[str, list[tuple[str, ...]]]]:
    """Index repo files and dirs by basename -> [relative path parts].

    Backs bare-name and path-suffix resolution. Includes `_archive` and
    `.index` (tracked, legitimately citable); excludes gitignored/generated
    trees, nested worktrees, and test fixtures (placeholder files must not
    satisfy citations).
    """
    files: dict[str, list[tuple[str, ...]]] = {}
    dirs: dict[str, list[tuple[str, ...]]] = {}
    for path in repo_root.rglob("*"):
        parts = path.relative_to(repo_root).parts
        if any(part in _TARGET_INDEX_SKIP for part in parts):
            continue
        if any(_contains_run(parts, run) for run in SKIP_SEGMENT_RUNS):
            continue
        if path.is_file():
            files.setdefault(parts[-1], []).append(parts)
        elif path.is_dir():
            dirs.setdefault(parts[-1], []).append(parts)
    return files, dirs


def _suffix_hit(target_parts: tuple[str, ...], index: dict[str, list[tuple[str, ...]]]) -> bool:
    """True if some indexed path ENDS WITH target_parts (segment-wise)."""
    candidates = index.get(target_parts[-1], ())
    return any(cand[-len(target_parts):] == target_parts for cand in candidates)


def _any_glob(base: Path, pattern: str) -> bool:
    try:
        return next(iter(base.glob(pattern)), None) is not None
    except (ValueError, NotImplementedError):
        return False


def check_kbleaf(
    tex_file: Path,
    text: str,
    repo_root: Path,
    file_index: dict[str, list[tuple[str, ...]]],
    dir_index: dict[str, list[tuple[str, ...]]],
    waived: frozenset[tuple[str, str]] = WAIVED_KBLEAF,
) -> tuple[list[Finding], int, int, set[tuple[str, str]]]:
    r"""Check every \kbleaf{...} in one .tex file.

    Returns (findings, checked_count, skipped_count, matched_waiver_keys).
    """
    findings: list[Finding] = []
    checked = 0
    skipped = 0
    matched_waivers: set[tuple[str, str]] = set()
    try:
        rel_source = str(tex_file.resolve().relative_to(repo_root))
    except ValueError:
        rel_source = str(tex_file)

    for lineno, line in enumerate(text.splitlines(), 1):
        line = _TEX_COMMENT_RE.sub("", line)
        for split in _SPLIT_KBLEAF_RE.finditer(line):
            findings.append(Finding(tex_file, lineno, "split kbleaf", split.group(0)))
        for match in _KBLEAF_RE.finditer(line):
            raw = match.group(1)
            target = normalize_kbleaf_target(raw)
            if (
                not target
                or target.startswith(("~", "/"))
                or _TEX_UNCHECKABLE_RE.search(target)
            ):
                skipped += 1
                continue
            checked += 1

            def dead() -> None:
                key = (rel_source, raw)
                if key in waived:
                    matched_waivers.add(key)
                    findings.append(Finding(tex_file, lineno, "waived kbleaf", raw))
                else:
                    findings.append(Finding(tex_file, lineno, "dead kbleaf", raw))

            # Sibling-repo target: resolved against the umbrella dir that holds
            # the sibling checkouts. Absent siblings are `broken inter`, which
            # participates in --inter-repo (warn by default) — same semantics
            # as md inter-repo links.
            if _SIBLING_REPO_RE.match(target):
                pattern = target.replace("...", "**")
                umbrella = repo_root.parent
                if "*" in pattern or "[" in pattern:
                    hit = _any_glob(umbrella, pattern.rstrip("/"))
                else:
                    hit = (umbrella / target).exists()
                if not hit:
                    findings.append(Finding(tex_file, lineno, "broken inter", raw))
                continue

            # Glob-shaped target (`...` ellipsis, `[..]` range, `*`): must
            # match under repo root, manuscript/, or manuscript/ave-kb/.
            if "..." in target or "*" in target or "[" in target:
                pattern = target.replace("...", "**").rstrip("/")
                bases = (repo_root, repo_root / "manuscript", repo_root / "manuscript" / "ave-kb")
                if not any(_any_glob(base, pattern) for base in bases):
                    dead()
                continue

            parts = tuple(p for p in target.split("/") if p and p != ".")
            if not parts:
                skipped += 1
                checked -= 1
                continue
            # Gitignored generated-artifact carveout (mirrors IGNORED_PATHS).
            if any(
                parts[i : i + len(ignored.parts)] == ignored.parts
                for ignored in IGNORED_PATHS
                for i in range(len(parts))
            ):
                continue
            if len(parts) == 1 and not target.endswith("/"):
                # Bare filename: basename resolution, extension-gated.
                if Path(parts[0]).suffix not in _BARE_CHECKABLE_EXTS:
                    skipped += 1
                    checked -= 1
                    continue
                if not _suffix_hit(parts, file_index):
                    dead()
                continue
            # Multi-segment (or explicit directory) path: suffix resolution —
            # every named directory segment must lie on a real path's tail.
            if not (_suffix_hit(parts, file_index) or _suffix_hit(parts, dir_index)):
                dead()
    return findings, checked, skipped, matched_waivers


def scan_kbleaf(
    repo_root: Path,
    waived: frozenset[tuple[str, str]] = WAIVED_KBLEAF,
    indexes: tuple[dict[str, list[tuple[str, ...]]], dict[str, list[tuple[str, ...]]]] | None = None,
) -> tuple[list[Finding], int, int]:
    """Run the kbleaf pass over manuscript/**/*.tex.

    Returns (findings, checked_count, skipped_count). Stale waivers (entries
    in `waived` that matched no live dead cite) are appended as gating
    `stale kbleaf waiver` findings. `indexes` lets a caller share the
    (file, dir) target index with the line-cite pass instead of rebuilding it.
    """
    file_index, dir_index = indexes if indexes is not None else build_kbleaf_target_index(repo_root)
    findings: list[Finding] = []
    checked = 0
    skipped = 0
    matched: set[tuple[str, str]] = set()
    for tex_file in iter_tex_files(repo_root):
        try:
            text = tex_file.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as exc:
            logger.warning("could not read %s: %s", tex_file, exc)
            continue
        f, c, s, m = check_kbleaf(tex_file, text, repo_root, file_index, dir_index, waived)
        findings.extend(f)
        checked += c
        skipped += s
        matched |= m
    for rel_source, raw in sorted(waived - matched):
        findings.append(Finding(repo_root / rel_source, 0, "stale kbleaf waiver", raw))
    logger.info("kbleaf pass: %d cites checked, %d non-path args skipped", checked, skipped)
    return findings, checked, skipped


def scan(
    repo_root: Path,
    check_ids_enabled: bool,
    file_index: dict[str, list[tuple[str, ...]]] | None = None,
    waived_line_cites: frozenset[tuple[str, str]] = WAIVED_LINE_CITE,
    heritage_exemption: bool = HERITAGE_PIN_EXEMPTION,
    pin_store: "PinStore | None" = None,
) -> tuple[list[Finding], Counter]:
    """Crawl every markdown file once, running all md-side passes on it.

    `file_index` enables the line-cite pass (None disables it). Returns
    (findings, line-cite stats).
    """
    known_ids = load_known_ids(repo_root) if check_ids_enabled else None
    findings: list[Finding] = []
    stats: Counter = Counter()
    matched_waivers: set[tuple[str, str]] = set()
    line_cache = TargetLineCache()
    for md_file in iter_markdown_files(repo_root):
        try:
            text = md_file.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as exc:
            logger.warning("could not read %s: %s", md_file, exc)
            continue
        body = strip_code(text)
        findings.extend(check_links(md_file, body, repo_root))
        if known_ids is not None:
            findings.extend(check_ids(md_file, body, known_ids))
        if file_index is not None:
            cite_findings, cite_stats, matched = check_line_cites(
                md_file,
                text,
                repo_root,
                file_index,
                line_cache,
                waived_line_cites,
                heritage_exemption,
                pin_store,
            )
            findings.extend(cite_findings)
            stats.update(cite_stats)
            matched_waivers |= matched
    if file_index is not None:
        for rel_source, as_written in sorted(waived_line_cites - matched_waivers):
            findings.append(
                Finding(repo_root / rel_source, 0, "stale line-cite waiver", as_written)
            )
    return findings, stats


# kbleaf finding kinds that always gate: every manuscript/**/*.tex source is
# the rendered manuscript — canonical-authority surface, like the KB tree.
_KBLEAF_GATING_KINDS = {"dead kbleaf", "split kbleaf", "stale kbleaf waiver"}

# Line-cite kinds that NEVER gate, whatever their source. Each names a
# pre-existing corpus backlog that a day-one gate would only teach lanes to
# bypass; the flip conditions are named in the docket fragment
# 2026-08-05-cite-rot-line-existence.md.
_ADVISORY_CITE_KINDS = {"broken backtick path", "blank line cite", "waived line cite"}

# Line-cite kinds that ALWAYS gate (a waiver outliving its subject is a lie in
# the tool's own bookkeeping, exactly as for `stale kbleaf waiver`).
_LINE_CITE_GATING_KINDS = {"stale line-cite waiver"}

# Pin-marker kinds. All gate through `is_error_source`, exactly like `dead line
# cite` — they are not a new gating CLASS, they are the same class applied to a
# cite whose author declared an exemption the tool could not honour:
#   `malformed pin marker`  — `` pin:`zzz` ``, `pin:c4a546dc` (unbackticked), or
#                             a marker on a cite with no `:NN`. Unreadable, so
#                             it exempts nothing and the cite is still checked.
#   `unknown pin sha`       — well formed, names no commit in a COMPLETE
#                             checkout.
#   `pin does not resolve at its own sha` — ★ the anti-silencer. Well formed,
#                             the commit is here, and the cite's own claim is
#                             FALSE there: no such path, or not that many lines.
#                             Without this arm the marker is an opt-out by
#                             assertion.
#   `orphan pin marker`     — a well-formed marker bound to no cite at all.
# All measured ZERO corpus-wide at the landing commit (`` pin:` `` had hits only
# in CONVENTIONS.md's own prose, two methods), so none can red-light a live tree
# on day one; each fires the moment someone writes a marker that is not true.
_PIN_MARKER_KINDS = {
    "malformed pin marker",
    "unknown pin sha",
    "pin does not resolve at its own sha",
    "orphan pin marker",
}


def is_gating(finding: Finding, repo_root: Path) -> bool:
    """True if `finding` flips the exit code.

    Broken-inter findings are handled separately by --inter-repo and are never
    gating here. Broken-intra, unknown-id, and `dead line cite` findings gate
    iff their source is an error source (see `is_error_source`). kbleaf
    findings gate unconditionally (their source is always the rendered
    manuscript), except `waived kbleaf` (adjudicated report-don't-fix,
    warn-only). Advisory cite kinds never gate.
    """
    if finding.kind == "broken inter":
        return False
    if finding.kind in _KBLEAF_GATING_KINDS or finding.kind in _LINE_CITE_GATING_KINDS:
        return True
    if finding.kind == "waived kbleaf" or finding.kind in _ADVISORY_CITE_KINDS:
        return False
    return is_error_source(finding.file, repo_root)


def report(findings: list[Finding], repo_root: Path) -> None:
    """Print every finding, sorted by file then line. Exhaustive — no truncation.

    Warn-only (non-gating) intra/id findings are tagged with a `· warn` suffix
    so the distinction from gating findings is visible in the report.
    """
    ordered = sorted(findings, key=lambda f: (str(f.file), f.line))
    for finding in ordered:
        try:
            rel = finding.file.relative_to(repo_root)
        except ValueError:
            rel = finding.file
        warn = finding.kind != "broken inter" and not is_gating(finding, repo_root)
        tag = f"{finding.kind} · warn" if warn else finding.kind
        suffix = f"   ({finding.detail})" if finding.detail else ""
        print(f"{rel}:{finding.line}  [{tag}]  ->  {finding.target}{suffix}")


def report_advisory_cites(
    findings: list[Finding], repo_root: Path, mode: str, sample: int = 8
) -> None:
    """Print the advisory cite block: counts always, findings per `mode`.

    `report` prints every advisory finding; `summary` prints per-kind counts
    (split error-source / warn-source) plus a capped sample of the
    error-source ones. Advisory volume is in the thousands — printing it
    unconditionally would drown the gating report.
    """
    advisory = [f for f in findings if f.kind in _ADVISORY_CITE_KINDS]
    if not advisory:
        return
    print("\n[verify-md-links][advisory] cite findings (NEVER gating):")
    for kind in sorted(_ADVISORY_CITE_KINDS):
        of_kind = [f for f in advisory if f.kind == kind]
        if not of_kind:
            continue
        err = [f for f in of_kind if is_error_source(f.file, repo_root)]
        print(f"  {kind:22s} {len(of_kind):5d}  (error-source: {len(err)})")
        shown = of_kind if mode == "report" else err[:sample]
        for finding in sorted(shown, key=lambda f: (str(f.file), f.line)):
            try:
                rel = finding.file.relative_to(repo_root)
            except ValueError:
                rel = finding.file
            suffix = f"   ({finding.detail})" if finding.detail else ""
            print(f"     · {rel}:{finding.line}  ->  {finding.target}{suffix}")
        if mode != "report" and len(err) > sample:
            print(f"     … {len(err) - sample} more error-source; --advisory-cites report for all")
            # ⚠ TRUNCATION HONESTY (2026-08-13). This console list is a SAMPLE.
            # Diffing it against another run reports far fewer changes than exist:
            # measured, a before/after diff of this truncated text said "0 new
            # errors" when the full report showed EIGHT. Say so at the truncation
            # point, where someone about to diff it is looking.
            print("     ⚠ SAMPLE, NOT A COMPLETE LIST — do NOT diff this output to")
            print("       decide whether a change added errors. Use")
            print("       `--advisory-cites report`, which prints the complete list.")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        "--inter-repo",
        choices=("dont-check", "warn", "error"),
        default="warn",
        help="how to handle links that escape into sibling repos (default: warn)",
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=None,
        help="repo root to scan (default: auto-detected from this script's location)",
    )
    parser.add_argument(
        "--no-id-check",
        action="store_true",
        help="disable the consumer-side claim/experiment/support id-validity check",
    )
    parser.add_argument(
        "--no-kbleaf-check",
        action="store_true",
        help=r"disable the manuscript \kbleaf{} tex-citation existence check",
    )
    parser.add_argument(
        "--no-line-check",
        action="store_true",
        help="disable the `path.ext:NN` cited-line existence check",
    )
    parser.add_argument(
        "--no-heritage-pin-exemption",
        action="store_true",
        help=(
            "MIGRATION PREVIEW (R2). Drop the grandfathered line-scoped "
            "SHA-on-the-line exemption and check those cites; only the "
            "per-cite pin:`<sha>` marker exempts. Not the default — flipping "
            "it for real is the migration's terminal step. Every ordinary run "
            "already PRINTS what this flag would change."
        ),
    )
    parser.add_argument(
        "--no-pin-sha-check",
        action="store_true",
        help=(
            "do not resolve pin:`<sha>` markers against the repo object "
            "store (escape hatch for a checkout without the pinned history). "
            "Every marker is then honoured unchecked."
        ),
    )
    parser.add_argument(
        "--advisory-cites",
        choices=("summary", "report", "off"),
        default="summary",
        help=(
            "advisory (never-gating) cite findings: counts + a capped sample "
            "(summary, default), every finding (report), or nothing (off)"
        ),
    )
    parser.add_argument("-v", "--verbose", action="store_true", help="enable info-level logging")
    args = parser.parse_args(argv)

    logging.basicConfig(
        level=logging.INFO if args.verbose else logging.WARNING,
        format="%(levelname)s: %(message)s",
    )

    repo_root = (args.root or find_repo_root(Path(__file__).resolve())).resolve()
    logger.info("scanning repo root: %s", repo_root)

    # One target index, shared by the line-cite pass and the kbleaf pass.
    indexes = None
    if not (args.no_line_check and args.no_kbleaf_check):
        indexes = build_kbleaf_target_index(repo_root)

    pin_store = PinStore(repo_root, enabled=not args.no_pin_sha_check)
    # The constant is the default; the flag can only force it further OFF.
    heritage_on = HERITAGE_PIN_EXEMPTION and not args.no_heritage_pin_exemption
    findings, cite_stats = scan(
        repo_root,
        check_ids_enabled=not args.no_id_check,
        file_index=None if args.no_line_check or indexes is None else indexes[0],
        # The constant is the default; the flag can only force it further OFF.
        heritage_exemption=heritage_on,
        pin_store=pin_store,
    )

    kbleaf_checked = kbleaf_skipped = 0
    if not args.no_kbleaf_check:
        kbleaf_findings, kbleaf_checked, kbleaf_skipped = scan_kbleaf(repo_root, indexes=indexes)
        findings.extend(kbleaf_findings)

    if args.inter_repo == "dont-check":
        findings = [f for f in findings if f.kind != "broken inter"]

    report([f for f in findings if f.kind not in _ADVISORY_CITE_KINDS], repo_root)
    if args.advisory_cites != "off":
        report_advisory_cites(findings, repo_root, args.advisory_cites)

    broken_inter = sum(1 for f in findings if f.kind == "broken inter")

    # Split non-inter findings by gating status (error source / kbleaf kind).
    non_inter = [f for f in findings if f.kind != "broken inter"]
    gating_errors = sum(1 for f in non_inter if is_gating(f, repo_root))
    warn_only = len(non_inter) - gating_errors

    print(
        f"\n[verify-md-links] gating errors: {gating_errors}  "
        f"warn-only: {warn_only}  broken inter: {broken_inter}  "
        f"(inter-repo mode: {args.inter_repo})",
        file=sys.stderr,
    )
    if not args.no_kbleaf_check:
        kb_dead = sum(1 for f in findings if f.kind in _KBLEAF_GATING_KINDS)
        kb_waived = sum(1 for f in findings if f.kind == "waived kbleaf")
        print(
            f"[verify-md-links] kbleaf: {kbleaf_checked} cites checked  "
            f"{kbleaf_skipped} non-path args skipped  "
            f"gating: {kb_dead}  waived: {kb_waived}",
            file=sys.stderr,
        )
    if not args.no_line_check:
        dead_gating = sum(
            1 for f in findings if f.kind == "dead line cite" and is_gating(f, repo_root)
        )
        print(
            f"[verify-md-links] line-cites: {cite_stats['checked']} lines checked  "
            f"dead: {cite_stats['dead']} (gating: {dead_gating})  "
            f"waived: {cite_stats['dead_waived']}  "
            f"| advisory — blank: {cite_stats['blank']}  "
            f"broken backtick path: {cite_stats['unresolved_backtick_path']}  "
            f"| skipped — shape: {cite_stats['skipped_shape']}  "
            f"path-only: {cite_stats['path_only']}",
            file=sys.stderr,
        )
        # The three dispositions of a historical pin, printed separately
        # because the MIGRATION'S PROGRESS IS EXACTLY THE RATIO between the
        # first two (R2: the exemption re-keys to marker-only once migrated).
        marker = cite_stats["exempt_marker"]
        heritage = cite_stats["exempt_heritage"]
        exempt_total = marker + heritage
        pct = f"{100.0 * marker / exempt_total:.1f}%" if exempt_total else "n/a"
        print(
            f"[verify-md-links] pin dispositions: "
            f"MARKER-EXEMPT: {marker}  "
            f"HERITAGE-EXEMPT: {heritage}  "
            f"CHECKED: {cite_stats['checked']}  "
            f"| migration: {marker}/{exempt_total} exemptions marker-keyed ({pct})  "
            f"heritage exemption: {'ON' if heritage_on else 'OFF'}"
            + (
                f"  (demoted to CHECKED: {cite_stats['heritage_demoted']})"
                if not heritage_on
                else ""
            ),
            file=sys.stderr,
        )
        rejected = (
            cite_stats["pin_malformed"]
            + cite_stats["pin_unknown_sha"]
            + cite_stats["pin_unresolved"]
            + cite_stats["pin_orphan"]
        )
        if rejected:
            print(
                f"[verify-md-links] pin markers REJECTED: "
                f"malformed: {cite_stats['pin_malformed']}  "
                f"unknown sha: {cite_stats['pin_unknown_sha']}  "
                f"does not resolve at its own sha: {cite_stats['pin_unresolved']}  "
                f"orphan (binds to no cite): {cite_stats['pin_orphan']}",
                file=sys.stderr,
            )
        if not pin_store.enabled:
            print(
                "[verify-md-links] pin validation DISABLED "
                "(no git object store to resolve pin:`<sha>` against) — "
                "every marker is honoured unchecked",
                file=sys.stderr,
            )
        elif cite_stats["pin_unverified"]:
            print(
                f"[verify-md-links] pin validation INCOMPLETE for "
                f"{cite_stats['pin_unverified']} marker(s) "
                f"(shallow/partial checkout: {pin_store.incomplete}) — "
                "honoured unchecked; re-run with full history to decide them",
                file=sys.stderr,
            )
        # ★ WHAT THE HERITAGE FLIP WOULD COST, measured on THIS corpus by the
        # same function that would do the checking. Dormant since the flip
        # landed on 2026-09-12 — `heritage_on` is False, nothing is exempt by
        # heritage, and there is nothing left to preview. Kept live rather than
        # deleted: it is the arm that would measure the cost again if the
        # exemption were ever restored.
        if heritage_on:
            print(
                f"[verify-md-links] heritage flip preview "
                f"(--no-heritage-pin-exemption / HERITAGE_PIN_EXEMPTION = False): "
                f"{heritage} cite(s) become CHECKED  "
                f"-> newly dead: {cite_stats['heritage_flip_dead']} "
                f"(GATING: {cite_stats['heritage_flip_dead_gating']})  "
                f"newly blank-advisory: {cite_stats['heritage_flip_blank']}",
                file=sys.stderr,
            )

    # Exit 1 iff there is >=1 gating error (error-source broken-intra or
    # unknown-id), plus broken-inter under --inter-repo error. Warn-only
    # findings and inter-repo links under warn/dont-check do not flip the code.
    failing = gating_errors
    if args.inter_repo == "error":
        failing += broken_inter

    return 1 if failing else 0


if __name__ == "__main__":
    raise SystemExit(main())
