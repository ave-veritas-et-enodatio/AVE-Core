#!/usr/bin/env python3
"""Repo-wide Markdown link-integrity checker for AVE-Core.

Crawls every tracked `.md` file in the repo, extracts Markdown links
`[text](target)`, and reports broken file targets. Also folds in a
consumer-side id-validity check: hashed claim/experiment/support ids
(`clm-`/`exp-`/`sup-` + 6 [a-z0-9]) cited in prose must resolve to a node
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
# Pattern is single-sourced from kb_index_lib (see import above).
_ID_RE = kb_index_lib.ANY_NODE_ID_RE
_ID_PLACEHOLDERS = {"clm-xxxxxx", "exp-xxxxxx", "sup-xxxxxx"}


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


def is_gating(finding: Finding, repo_root: Path) -> bool:
    """True if `finding` flips the exit code.

    Broken-inter findings are handled separately by --inter-repo and are never
    gating here. Broken-intra and unknown-id findings gate iff their source is
    an error source (see `is_error_source`).
    """
    if finding.kind == "broken inter":
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
    parser.add_argument("-v", "--verbose", action="store_true", help="enable info-level logging")
    args = parser.parse_args(argv)

    logging.basicConfig(
        level=logging.INFO if args.verbose else logging.WARNING,
        format="%(levelname)s: %(message)s",
    )

    repo_root = (args.root or find_repo_root(Path(__file__).resolve())).resolve()
    logger.info("scanning repo root: %s", repo_root)

    findings = scan(repo_root, check_ids_enabled=not args.no_id_check)

    if args.inter_repo == "dont-check":
        findings = [f for f in findings if f.kind != "broken inter"]

    report(findings, repo_root)

    broken_inter = sum(1 for f in findings if f.kind == "broken inter")

    # Split intra/id findings by source: gating (error source) vs warn-only.
    intra_id = [f for f in findings if f.kind in ("broken intra", "unknown id")]
    gating_errors = sum(1 for f in intra_id if is_gating(f, repo_root))
    warn_only = len(intra_id) - gating_errors

    print(
        f"\n[verify-md-links] gating errors: {gating_errors}  "
        f"warn-only: {warn_only}  broken inter: {broken_inter}  "
        f"(inter-repo mode: {args.inter_repo})",
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
