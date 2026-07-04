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
import re
import sys
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
    kind: str  # "broken intra" | "broken inter" | "unknown id"
    target: str


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


def strip_target(target: str) -> str:
    """Strip a trailing #anchor and a trailing :linenum suffix from a target."""
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
) -> tuple[list[Finding], int, int]:
    """Run the kbleaf pass over manuscript/**/*.tex.

    Returns (findings, checked_count, skipped_count). Stale waivers (entries
    in `waived` that matched no live dead cite) are appended as gating
    `stale kbleaf waiver` findings.
    """
    file_index, dir_index = build_kbleaf_target_index(repo_root)
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


def scan(repo_root: Path, check_ids_enabled: bool) -> list[Finding]:
    known_ids = load_known_ids(repo_root) if check_ids_enabled else None
    findings: list[Finding] = []
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
    return findings


# kbleaf finding kinds that always gate: every manuscript/**/*.tex source is
# the rendered manuscript — canonical-authority surface, like the KB tree.
_KBLEAF_GATING_KINDS = {"dead kbleaf", "split kbleaf", "stale kbleaf waiver"}


def is_gating(finding: Finding, repo_root: Path) -> bool:
    """True if `finding` flips the exit code.

    Broken-inter findings are handled separately by --inter-repo and are never
    gating here. Broken-intra and unknown-id findings gate iff their source is
    an error source (see `is_error_source`). kbleaf findings gate
    unconditionally (their source is always the rendered manuscript), except
    `waived kbleaf` (adjudicated report-don't-fix, warn-only).
    """
    if finding.kind == "broken inter":
        return False
    if finding.kind in _KBLEAF_GATING_KINDS:
        return True
    if finding.kind == "waived kbleaf":
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
        print(f"{rel}:{finding.line}  [{tag}]  ->  {finding.target}")


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
    parser.add_argument("-v", "--verbose", action="store_true", help="enable info-level logging")
    args = parser.parse_args(argv)

    logging.basicConfig(
        level=logging.INFO if args.verbose else logging.WARNING,
        format="%(levelname)s: %(message)s",
    )

    repo_root = (args.root or find_repo_root(Path(__file__).resolve())).resolve()
    logger.info("scanning repo root: %s", repo_root)

    findings = scan(repo_root, check_ids_enabled=not args.no_id_check)

    kbleaf_checked = kbleaf_skipped = 0
    if not args.no_kbleaf_check:
        kbleaf_findings, kbleaf_checked, kbleaf_skipped = scan_kbleaf(repo_root)
        findings.extend(kbleaf_findings)

    if args.inter_repo == "dont-check":
        findings = [f for f in findings if f.kind != "broken inter"]

    report(findings, repo_root)

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

    # Exit 1 iff there is >=1 gating error (error-source broken-intra or
    # unknown-id), plus broken-inter under --inter-repo error. Warn-only
    # findings and inter-repo links under warn/dont-check do not flip the code.
    failing = gating_errors
    if args.inter_repo == "error":
        failing += broken_inter

    return 1 if failing else 0


if __name__ == "__main__":
    raise SystemExit(main())
