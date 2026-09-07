#!/usr/bin/env python3
"""Census + classification library for SHA-pinned line-cites (ruling R2).

WHY THIS EXISTS
---------------
`verify-md-links.py` exempts a line-cite from its `dead line cite` check when
the CITING LINE carries a backticked short SHA anywhere on it
(`_HISTORICAL_PIN_RE`). That exemption is LINE-SCOPED, and the corpus's ledger
rows are hundreds to thousands of characters wide, so one provenance SHA
silently exempts every other cite that shares its row. Ruling R2
(`_orchestration/docket-entries/2026-08-06-rulings-decision-batch.md`) replaces
the heuristic with an author-declared PER-CITE marker:

    <path>:<line>@<sha>          <path>:<start>-<end>@<sha>

This module answers the question the migration needs answered first: of the
cites the heuristic exempts today, which ones did the author actually MEAN
historically?  Three classes:

  TRUE-PIN  the cite does not resolve at HEAD, AND the pin is corroborated --
            either it RESOLVES at a SHA named on its own line (the objective
            arm), or the line carries historical-pin prose (the prose arm).
  LIVE      the cite resolves at HEAD.  It is a normal live cite that merely
            shares a row with somebody else's provenance SHA.  These are the
            false negatives R2 was ruled to eliminate: the gate is not checking
            them today, and it should be.
  DEAD      the cite resolves at neither HEAD nor any SHA on its line, and no
            prose claims it is pinned.  Real rot, hidden by the exemption.

plus two bookkeeping classes that are NOT defects and NOT migration subjects:

  UNRESOLVED-PATH  no candidate file anywhere in the repo (the gate reports
                   these separately as advisory `broken backtick path`).
  SKIPPED-SHAPE    glob / sibling-repo / home-dir / ephemeral target; the gate
                   never checks these either.

DEFINITION OF "LINE-CITE" IS BORROWED, NOT RE-INVENTED
------------------------------------------------------
Every extraction and resolution primitive here is imported from
`verify-md-links.py` itself (`iter_line_cites`, `cite_target_uncheckable`,
`resolve_cite_candidates`, `build_kbleaf_target_index`, `iter_markdown_files`,
`_HISTORICAL_PIN_RE`).  A census that used its own regex would be measuring a
different population than the gate acts on, and the counts would not be an
argument about the gate.

THE OBJECTIVE ARM
-----------------
`resolves_at_sha` is the arm that does not depend on reading prose: for each
backticked SHA on the citing line, the cited path is resolved AGAINST THAT
COMMIT'S TREE (same direct + path-suffix union as HEAD resolution) and the
cited line number is compared against the blob's length at that commit.  A cite
that is too long for HEAD but in range at the SHA beside it is a pin by
construction, whatever the prose says.
"""

from __future__ import annotations

import importlib.util
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

_HERE = Path(__file__).resolve().parent


def load_vml(path: Path | None = None):
    """Import `verify-md-links.py` (hyphenated, so not a normal import)."""
    target = path or (_HERE / "verify-md-links.py")
    spec = importlib.util.spec_from_file_location("_vml_for_census", target)
    if spec is None or spec.loader is None:  # pragma: no cover - defensive
        raise RuntimeError(f"cannot load {target}")
    if str(target.parent) not in sys.path:
        sys.path.insert(0, str(target.parent))  # verify-md-links imports kb_index_lib
    module = importlib.util.module_from_spec(spec)
    # Registered BEFORE exec: verify-md-links defines @dataclass classes, and
    # dataclasses resolves `cls.__module__` through sys.modules.
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


# Historical-pin PROSE markers.  This is the corroborating arm, deliberately
# secondary to `resolves_at_sha`.  The four phrases named in verify-md-links'
# own `_HISTORICAL_PIN_RE` comment are the seed; the rest were read off the
# corpus lines this census reports.  Matched case-insensitively against the
# WHOLE citing line.
PIN_PROSE_PATTERNS: tuple[str, ...] = (
    r"as shipped (?:on|at|in)",
    r"as (?:it )?(?:stood|shipped|was) at",
    r"at commit",
    r"frozen at",
    r"frozen[- ]snapshot",
    r"was correct at",
    r"correct as (?:written )?at",
    r"against main @",
    r"as of commit",
    r"line numbers? (?:are )?(?:as )?(?:of|at)",
    r"pinned to",
    r"pre-?renumber",
    r"at the time of",
    r"snapshot(?:ted)? at",
    r"historical(?:ly)? pinned",
)
_PIN_PROSE_RE = re.compile("|".join(PIN_PROSE_PATTERNS), re.IGNORECASE)

# The per-cite marker this migration installs.  Kept here so the census, the
# migrator and any future consumer share ONE definition.
MARKER_RE = re.compile(r"@(?P<sha>[0-9a-f]{7,40})")
# A fully-marked cite, as written: `path.md:12@abcdef1` / `path.md:8-24@abcdef1`.
MARKED_CITE_TAIL_RE = re.compile(r":(?P<start>\d+)(?:-{1,2}(?P<end>\d+))?@(?P<sha>[0-9a-f]{7,40})")


class ShaTree:
    """Cached view of one commit: its file list and its blobs' line counts."""

    def __init__(self, repo_root: Path, sha: str) -> None:
        self.repo_root = repo_root
        self.sha = sha
        self._files: dict[str, list[tuple[str, ...]]] | None = None
        self._counts: dict[str, int | None] = {}
        self._paths: set[str] | None = None
        self.exists = self._commit_exists()

    def _git(self, *args: str) -> tuple[int, str]:
        proc = subprocess.run(
            ["git", "-C", str(self.repo_root), *args],
            capture_output=True,
            text=True,
        )
        return proc.returncode, proc.stdout

    def _commit_exists(self) -> bool:
        code, _ = self._git("cat-file", "-e", f"{self.sha}^{{commit}}")
        return code == 0

    @property
    def files(self) -> dict[str, list[tuple[str, ...]]]:
        if self._files is None:
            index: dict[str, list[tuple[str, ...]]] = {}
            if self.exists:
                code, out = self._git("ls-tree", "-r", "--name-only", self.sha)
                if code == 0:
                    for rel in out.splitlines():
                        parts = tuple(rel.split("/"))
                        index.setdefault(parts[-1], []).append(parts)
            self._files = index
        return self._files

    def line_count(self, rel: str) -> int | None:
        """Lines in `rel` at this commit, or None when the blob is absent."""
        if rel not in self._counts:
            code, out = self._git("show", f"{self.sha}:{rel}")
            self._counts[rel] = len(out.splitlines()) if code == 0 else None
        return self._counts[rel]

    def _all_paths(self) -> set[str]:
        if self._paths is None:
            self._paths = {"/".join(p) for p in _flat(self.files)}
        return self._paths

    def candidates(self, target: str, citing_rel: str) -> list[str]:
        """Same union resolution as HEAD, against this commit's tree."""
        found: set[str] = set()
        citing_dir = str(Path(citing_rel).parent)
        for base in (citing_dir, "."):
            joined = target if base == "." else f"{citing_dir}/{target}"
            norm = _normalise(joined)
            if norm in self._all_paths():
                found.add(norm)
        parts = tuple(p for p in target.split("/") if p and p != ".")
        if parts:
            for indexed in self.files.get(parts[-1], ()):
                if indexed[-len(parts):] == parts:
                    found.add("/".join(indexed))
        return sorted(found)


def _flat(index: dict[str, list[tuple[str, ...]]]):
    for entries in index.values():
        yield from entries


def _normalise(path: str) -> str:
    out: list[str] = []
    for seg in path.split("/"):
        if seg in ("", "."):
            continue
        if seg == "..":
            if out:
                out.pop()
            continue
        out.append(seg)
    return "/".join(out)


@dataclass
class CensusRow:
    source: str            # repo-relative citing file
    lineno: int            # line in the citing file
    form: str              # backticked | link-in | link-ext
    as_written: str        # the cite text
    line_shas: tuple[str, ...]
    line_len: int
    cites_on_line: int
    resolves_at_head: bool | None      # None => no candidate at HEAD
    resolving_shas: tuple[str, ...]    # SHAs on the line at which it DOES resolve
    prose_marker: bool
    klass: str
    already_marked: bool = False
    head_candidates: tuple[str, ...] = field(default_factory=tuple)

    def key(self) -> tuple[str, int, str]:
        return (self.source, self.lineno, self.as_written)


def classify(
    repo_root: Path,
    vml,
    file_index,
    md_files,
    sha_cache: dict[str, ShaTree] | None = None,
) -> list[CensusRow]:
    """Classify every line-cite that sits on a SHA-bearing line."""
    sha_cache = {} if sha_cache is None else sha_cache
    line_cache = vml.TargetLineCache()
    rows: list[CensusRow] = []

    for md_file in md_files:
        try:
            text = md_file.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        rel_source = str(md_file.resolve().relative_to(repo_root))
        raw_lines = vml.strip_fences(text).splitlines()
        cites = [c for c in vml.iter_line_cites(text) if c.pinned and c.start is not None]
        per_line: dict[int, int] = {}
        for c in cites:
            per_line[c.lineno] = per_line.get(c.lineno, 0) + 1

        for cite in cites:
            line = raw_lines[cite.lineno - 1] if cite.lineno <= len(raw_lines) else ""
            # `_HISTORICAL_PIN_RE` has no groups, so finditer yields the whole
            # match INCLUDING its backticks; strip them to get the bare SHA.
            shas = tuple(
                dict.fromkeys(m.group(0).strip("`") for m in vml._HISTORICAL_PIN_RE.finditer(line))
            )
            prose = bool(_PIN_PROSE_RE.search(line))
            already = bool(MARKED_CITE_TAIL_RE.search(cite.as_written))
            cited_last = max(cite.start, cite.end or cite.start)

            if vml.cite_target_uncheckable(cite.path):
                rows.append(CensusRow(rel_source, cite.lineno, cite.form, cite.as_written,
                                      shas, len(line), per_line[cite.lineno], None, (), prose,
                                      "SKIPPED-SHAPE", already))
                continue

            cands = vml.resolve_cite_candidates(cite.path, md_file, repo_root, file_index)
            cand_rel = tuple(str(Path(c).resolve().relative_to(repo_root)) for c in cands)
            if cands:
                at_head = max(line_cache.count(c) for c in cands) >= cited_last
            else:
                # No candidate file at HEAD at all. This is NOT automatically a
                # bookkeeping skip: a genuine pin cites a path that was later
                # RENAMED OR DELETED, so it must still be offered to the SHA arm
                # before it is written off. Only if no SHA on the line has the
                # path either does it fall through to UNRESOLVED-PATH.
                at_head = False

            resolving: list[str] = []
            if not at_head:
                for sha in shas:
                    tree = sha_cache.get(sha)
                    if tree is None:
                        tree = sha_cache[sha] = ShaTree(repo_root, sha)
                    if not tree.exists:
                        continue
                    for rel in tree.candidates(cite.path, rel_source):
                        n = tree.line_count(rel)
                        if n is not None and n >= cited_last:
                            resolving.append(sha)
                            break

            if at_head:
                klass = "LIVE"
            elif resolving or prose:
                klass = "TRUE-PIN"
            elif not cands:
                klass = "UNRESOLVED-PATH"
            else:
                klass = "DEAD"

            rows.append(CensusRow(rel_source, cite.lineno, cite.form, cite.as_written,
                                  shas, len(line), per_line[cite.lineno],
                                  at_head if cands else None,
                                  tuple(dict.fromkeys(resolving)), prose, klass, already,
                                  cand_rel))
    return rows
