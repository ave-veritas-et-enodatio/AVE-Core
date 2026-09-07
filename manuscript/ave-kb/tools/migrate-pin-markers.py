#!/usr/bin/env python3
"""Rewrite TRUE-PIN line-cites to carry the per-cite `@<sha>` marker (ruling R2).

TOKEN (fixed by the ruling's dispatch, not by this script):

    <path>:<line>@<sha>          <path>:<start>-<end>@<sha>

meaning "this cite is DELIBERATELY pinned to the repo state at <sha>"; the SHA
is 7-40 lowercase hex and the marker exempts EXACTLY the cite it is attached to.

WHAT IT TOUCHES
---------------
Only cites `pin_census_lib.classify` returns as TRUE-PIN, and by default only
those ALSO named in a hand-verified allow-list (`--verified`).  The allow-list
is not belt-and-braces: the classifier's TRUE-PIN precision was MEASURED by hand
on its whole corpus population and came out 2/5.  The failure mode is specific
and unfixable by regex — a line-cite can EXIST at a SHA that happens to sit on
its row for an unrelated reason (a session stamp, a ruling id), which is a
line-existence coincidence, not an author's pin.  So the classifier proposes and
a human disposes.  `--allow-unverified` exists for the case where the census has
been re-read end to end; it prints the measured precision before it runs.

LIVE and DEAD cites are never touched, and neither are UNRESOLVED-PATH /
SKIPPED-SHAPE rows.

FROZEN DOCUMENTS ARE REFUSED, NOT REWRITTEN
-------------------------------------------
Byte-frozen documents are gated by `verify-frozen-provenance.py`, whose whole
premise is that a criterion labeled *Frozen* is byte-identical to its prereg.
Editing one from a migration script would break exactly the property that gate
exists to hold. So any candidate in

  * a file whose name contains `prereg-FROZEN`,
  * any `research/**/*prereg*.md` (the guard's comparison targets), or
  * any `research/**/*[-_]result.md` / `_RESULT.md` (the guard's gating docs),

is LISTED FOR A HUMAN and skipped, and the run exits 2 so a caller cannot
mistake "refused" for "nothing to do".

DRY RUN IS THE DEFAULT.  `--apply` writes.

    python3 manuscript/ave-kb/tools/migrate-pin-markers.py --dir _orchestration \
        --verified _orchestration/docket-entries/2026-09-07-r2-pin-verified.txt
    ... same, plus --apply

EXIT CODES
    0  nothing refused (whether or not anything was rewritten)
    2  at least one TRUE-PIN candidate sits in a frozen-guarded file
"""

from __future__ import annotations

import argparse
import difflib
import importlib.util
import re
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent

# Measured by hand over the FULL corpus TRUE-PIN population (2026-09-07); see
# the docket fragment named in --help output. Printed by --allow-unverified so
# nobody bulk-migrates without seeing it.
MEASURED_TRUE_PIN_PRECISION = "2/5 (40%) hand-confirmed, whole population"


def _load_lib():
    spec = importlib.util.spec_from_file_location("pin_census_lib", _HERE / "pin_census_lib.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


_FROZEN_NAME_RE = re.compile(r"prereg-FROZEN", re.IGNORECASE)
_RESEARCH_PREREG_RE = re.compile(r"^research/.*prereg.*\.md$", re.IGNORECASE)
_RESEARCH_RESULT_RE = re.compile(r"^research/.*[-_]result\.md$", re.IGNORECASE)


def frozen_guarded(rel_source: str) -> str | None:
    """Reason `rel_source` must not be machine-edited, or None."""
    if _FROZEN_NAME_RE.search(Path(rel_source).name):
        return "name contains prereg-FROZEN"
    if _RESEARCH_PREREG_RE.match(rel_source):
        return "research prereg (verify-frozen-provenance comparison target)"
    if _RESEARCH_RESULT_RE.match(rel_source):
        return "research result doc (verify-frozen-provenance gating doc)"
    return None


def load_allowlist(path: Path) -> set[tuple[str, int, str]]:
    """`<source>\\t<lineno>\\t<as_written>` per line; `#` comments and blanks ok."""
    out: set[tuple[str, int, str]] = set()
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        parts = [p.strip() for p in line.split("\t") if p.strip()]
        if len(parts) != 3:
            raise SystemExit(f"{path}: malformed allow-list row (want 3 tab-separated fields): {raw!r}")
        out.add((parts[0], int(parts[1]), parts[2]))
    return out


def marker_for(row) -> str | None:
    """The SHA this cite should be pinned to, or None when it is ambiguous.

    Preference order: a SHA the cite actually RESOLVES at (the objective arm);
    else the line's SOLE SHA. A prose-only pin on a multi-SHA line has no
    determinable target and is left for a human — guessing which of five
    provenance SHAs an author meant is exactly the row-level ambiguity R2 was
    ruled to end.
    """
    if row.resolving_shas:
        return row.resolving_shas[0]
    if len(row.line_shas) == 1:
        return row.line_shas[0]
    return None


def rewrite_line(line: str, as_written: str, sha: str) -> tuple[str, int]:
    """Append `@sha` to every un-marked occurrence of `as_written` on `line`.

    IDEMPOTENT by construction: the negative lookahead `(?!@[0-9a-f])` means an
    already-marked cite is not a match, so a second pass finds nothing to do.
    The `(?![0-9])` guard stops `foo.md:8` matching the head of `foo.md:80`.
    """
    pattern = re.compile(re.escape(as_written) + r"(?![0-9])(?!@[0-9a-f])")
    return pattern.subn(f"{as_written}@{sha}", line)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--repo-root", type=Path, default=None)
    parser.add_argument("--dir", dest="subdir", default=None,
                        help="restrict to markdown under this repo-relative dir")
    parser.add_argument("--verified", type=Path, default=None,
                        help="hand-verified allow-list (source<TAB>lineno<TAB>cite)")
    parser.add_argument("--allow-unverified", action="store_true",
                        help="migrate every classifier TRUE-PIN (prints measured precision first)")
    parser.add_argument("--apply", action="store_true", help="write the changes (default: dry run)")
    args = parser.parse_args(argv)

    if not args.verified and not args.allow_unverified:
        parser.error("pass --verified <allow-list> (recommended) or --allow-unverified")

    lib = _load_lib()
    vml = lib.load_vml()
    repo_root = (args.repo_root or Path(__file__).resolve().parents[3]).resolve()

    md_files = list(vml.iter_markdown_files(repo_root))
    if args.subdir:
        base = (repo_root / args.subdir).resolve()
        md_files = [f for f in md_files if base == f or base in f.parents]

    file_index, _ = vml.build_kbleaf_target_index(repo_root)
    rows = lib.classify(repo_root, vml, file_index, md_files)
    candidates = [r for r in rows if r.klass == "TRUE-PIN"]

    allow = load_allowlist(args.verified) if args.verified else None
    if allow is not None:
        skipped_unverified = [r for r in candidates if r.key() not in allow]
        candidates = [r for r in candidates if r.key() in allow]
    else:
        skipped_unverified = []
        print(f"!! --allow-unverified: classifier TRUE-PIN precision is {MEASURED_TRUE_PIN_PRECISION}")

    refused: list[tuple[str, str, str]] = []
    ambiguous: list = []
    by_file: dict[str, list] = {}
    for row in candidates:
        reason = frozen_guarded(row.source)
        if reason:
            refused.append((row.source, row.as_written, reason))
            continue
        if marker_for(row) is None:
            ambiguous.append(row)
            continue
        by_file.setdefault(row.source, []).append(row)

    changed_files = 0
    changed_cites = 0
    for rel, rws in sorted(by_file.items()):
        path = repo_root / rel
        original = path.read_text(encoding="utf-8")
        lines = original.splitlines(keepends=True)
        file_hits = 0
        for row in sorted(rws, key=lambda r: r.lineno):
            idx = row.lineno - 1
            if idx >= len(lines):
                continue
            new, n = rewrite_line(lines[idx], row.as_written, marker_for(row))
            lines[idx] = new
            file_hits += n
        updated = "".join(lines)
        if updated == original:
            continue
        changed_files += 1
        changed_cites += file_hits
        diff = difflib.unified_diff(
            original.splitlines(True), updated.splitlines(True),
            fromfile=f"a/{rel}", tofile=f"b/{rel}", n=0,
        )
        for chunk in diff:
            sys.stdout.write(chunk if chunk.endswith("\n") else chunk + "\n")
        if args.apply:
            path.write_text(updated, encoding="utf-8")

    scope = args.subdir or "corpus"
    print()
    print(f"=== migrate-pin-markers — scope: {scope} — {'APPLIED' if args.apply else 'DRY RUN'} ===")
    print(f"TRUE-PIN candidates in scope : {len(rows and [r for r in rows if r.klass == 'TRUE-PIN'])}")
    if allow is not None:
        print(f"  not on the allow-list      : {len(skipped_unverified)} (left alone)")
    print(f"files rewritten              : {changed_files}")
    print(f"cites marked                 : {changed_cites}")
    if ambiguous:
        print(f"ambiguous (multi-SHA, prose-only) — LEFT FOR A HUMAN: {len(ambiguous)}")
        for row in ambiguous:
            print(f"  {row.source}:{row.lineno}  {row.as_written}  shas={','.join(row.line_shas)}")
    if refused:
        print(f"REFUSED — frozen-guarded, migrate by hand or not at all: {len(refused)}")
        for source, cite, reason in refused:
            print(f"  {source}  {cite}  [{reason}]")
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
