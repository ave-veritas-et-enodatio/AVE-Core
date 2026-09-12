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
the heuristic with an author-declared PER-CITE marker.

THE TOKEN IS NOT COINED HERE. It was written on 2026-08-06 and already lives in
canon at `manuscript/ave-kb/CONVENTIONS.md` (search "Author-declared pin
marker"):

    per `some-leaf.md:42` pin:`c4a546dc` -- *"the sentence that line carried then"*

i.e. `` pin:`<7-40 hex>` `` placed immediately after the location cite it pins,
binding the nearest cite to its LEFT. This module READS that convention; it does
not get a vote on the spelling. An earlier round of this lane invented a second
token (`path:NN@<sha>`) for the same concept without checking whether one
existed -- a homonym, which `ave-vocab-discipline`'s COINAGE rule answers
directly: an existing meaning is REUSED, not silently overloaded.

This module answers the question the migration needs answered first: of the
cites the heuristic exempts today, which ones did the author actually MEAN
historically?  Three classes:

  TRUE-PIN  the cite does not resolve at HEAD, AND it RESOLVES at a SHA named
            on its own line.  Resolution at the SHA is NECESSARY: prose may
            corroborate a pin but can never establish one (see THE PROSE ARM
            IS NOT SUFFICIENT, below).
  LIVE      the cite resolves at HEAD.  It is a normal live cite that merely
            shares a row with somebody else's provenance SHA.  These are the
            false negatives R2 was ruled to eliminate: the gate is not checking
            them today, and it should be.
  DEAD      the cite resolves at neither HEAD nor any SHA on its line, though
            its path does resolve at HEAD.  Real rot, hidden by the exemption --
            and STILL DEAD when the line claims a pin in prose.

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

THE PROSE ARM IS NOT SUFFICIENT
-------------------------------
An earlier revision classified `resolving or prose` as TRUE-PIN, so PROSE ALONE
carried a cite into the migratable class.  That is a laundering machine: a row
reading ``| run at the time of `b649f9f2` | rot `target.md:99` |`` -- where line
99 exists neither at HEAD nor at `b649f9f2` -- came out TRUE-PIN and would have
been REWRITTEN to carry a pin marker, converting undiscovered rot into a signed
author declaration that the rot is deliberate.  A pin marker must never be
applied to a cite that resolves at NEITHER end.  So resolution at the SHA is the
necessary condition, and `prose_marker` is recorded, reported, and never
sufficient.  A DEAD row whose line claims a pin in prose is the loudest thing
this census can find, and `pin-census.py` prints that sub-count separately.

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

# ---------------------------------------------------------------------------
# The marker, as CONVENTIONS.md defines it.  One definition, shared by the
# census, the migrator and any future consumer, so nobody retypes it wrong.
# ---------------------------------------------------------------------------

#: `` pin:`c4a546dc` `` -- the author-declared marker itself, anywhere in a text.
PIN_MARKER_RE = re.compile(r"pin:`(?P<sha>[0-9a-f]{7,40})`")

#: The same marker where it must sit to BIND a cite: immediately to the cite's
#: right, separated by nothing but inline whitespace.  Used as a lookahead after
#: a cite occurrence, which is what makes both the census's `already_marked` and
#: the migrator's idempotence positional rather than line-scoped.
TRAILING_MARKER_RE = re.compile(r"[ \t]*pin:`[0-9a-f]{7,40}`")


def count_markers(text: str) -> int:
    """Occurrences of the author-declared pin marker in `text`."""
    return len(PIN_MARKER_RE.findall(text))


def cite_occurrence_re(form: str, path: str, start: int | None, end: int | None) -> re.Pattern:
    """A regex matching this cite WHERE IT IS WRITTEN, in its own form.

    Needed because the marker attaches to the cite's right-hand edge, and that
    edge is in a different place in each of the three forms:

        backticked   `path:12`                -> after the closing backtick
        link-in      [text](path:12)          -> after the closing paren
        link-ext     [text](path):12          -> after the line suffix

    ★ RANGE SEPARATOR. `LineCite.as_written` NORMALISES `:133--147` to
    `:133-147`, so a migrator that searched for `as_written` literally would
    silently skip every double-dash range in the corpus. This builds the line
    suffix from the parsed numbers with `-{1,2}`, so both spellings match.
    """
    body = re.escape(path)
    if start is not None:
        body += rf":{start}"
        if end is not None and end != start:
            body += rf"-{{1,2}}{end}"
        body += r"(?!\d)"
    if form == "link-in":
        return re.compile(r"\[[^\]]*\]\(\s*" + body + r"\s*\)")
    if form == "link-ext":
        head = re.escape(path)
        suffix = body[len(re.escape(path)):]
        return re.compile(r"\[[^\]]*\]\(\s*" + head + r"\s*\)" + suffix)
    return re.compile(r"`\s*" + body + r"\s*`")


def marked_occurrences(line: str, form: str, path: str,
                       start: int | None, end: int | None) -> tuple[int, int]:
    """`(occurrences, of which already carry a trailing marker)` on `line`."""
    total = marked = 0
    for m in cite_occurrence_re(form, path, start, end).finditer(line):
        total += 1
        if TRAILING_MARKER_RE.match(line, m.end()):
            marked += 1
    return total, marked


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
    as_written: str        # the cite text, NORMALISED (`:133--147` -> `:133-147`)
    path: str              # the cited path, exactly as written
    start: int | None      # cited line
    end: int | None        # range end (== start for a single line)
    line_shas: tuple[str, ...]
    line_len: int
    cites_on_line: int
    resolves_at_head: bool | None      # None => no candidate at HEAD
    resolving_shas: tuple[str, ...]    # SHAs on the line at which it DOES resolve
    prose_marker: bool
    klass: str
    #: True when at least one occurrence of this cite on its line already
    #: carries a trailing `` pin:`sha` ``. A line that writes the same cite
    #: twice, once marked and once not, reports True and is left to a human --
    #: the migrator's per-occurrence lookahead still marks only the bare one.
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
            _total, _marked = marked_occurrences(line, cite.form, cite.path, cite.start, cite.end)
            already = _marked > 0
            cited_last = max(cite.start, cite.end or cite.start)

            if vml.cite_target_uncheckable(cite.path):
                rows.append(CensusRow(rel_source, cite.lineno, cite.form, cite.as_written,
                                      cite.path, cite.start, cite.end,
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

            # ★ RESOLUTION AT THE SHA IS NECESSARY. `prose` is deliberately
            # absent from this ladder: see THE PROSE ARM IS NOT SUFFICIENT in
            # the module docstring. A cite that resolves at neither end is rot,
            # and rot with a confident sentence beside it is still rot.
            if at_head:
                klass = "LIVE"
            elif resolving:
                klass = "TRUE-PIN"
            elif not cands:
                klass = "UNRESOLVED-PATH"
            else:
                klass = "DEAD"

            rows.append(CensusRow(rel_source, cite.lineno, cite.form, cite.as_written,
                                  cite.path, cite.start, cite.end,
                                  shas, len(line), per_line[cite.lineno],
                                  at_head if cands else None,
                                  tuple(dict.fromkeys(resolving)), prose, klass, already,
                                  cand_rel))
    return rows
