#!/usr/bin/env python3
"""Rewrite TRUE-PIN line-cites to carry the author-declared pin marker (R2).

TOKEN -- READ FROM CANON, NOT COINED HERE.  `manuscript/ave-kb/CONVENTIONS.md`
("Author-declared pin marker", written 2026-08-06) already fixes the form:

    per `some-leaf.md:42` pin:`c4a546dc` -- *"the sentence that line carried then"*

`` pin:`<7-40 lowercase hex>` `` sits immediately to the RIGHT of the cite it
pins and binds that cite alone -- which is the whole content of R2, because the
heuristic it replaces is row-scoped.  This script writes exactly that token in
exactly that position, in each of the three cite forms:

    backticked   `path:12` pin:`sha`
    link-in      [text](path:12) pin:`sha`
    link-ext     [text](path):12 pin:`sha`

A marked cite carries a backticked SHA on its line, so it stays exempt under the
OLD heuristic too: the migration needs no flag day, exactly as CONVENTIONS says.

WHAT IT TOUCHES
---------------
Only cites `pin_census_lib.classify` returns as TRUE-PIN -- which since the D2
repair requires the cite to RESOLVE AT A SHA ON ITS OWN ROW, so a confident
sentence can no longer carry rot into this script -- and by default only those
ALSO named in a hand-verified allow-list (`--verified`).  The allow-list is not
belt-and-braces: the classifier's TRUE-PIN precision was MEASURED by hand on its
whole corpus population three times, and the three passes returned 5/5, then
2/5, then -- byte-level, 2026-09-12 -- 4/5.  The 2/5 pass was wrong, and HOW it
was wrong is the reason this allow-list exists at all: it characterised a
3,964-BYTE table row by its first 100 bytes and never searched the rest of the
line for the content the citing sentence claimed, which sat at character offset
1,173.  Two independent readers agreed, and agreed because they made the same
read of the same head of the same line.  The residual failure mode is specific
and unfixable by regex — a line-cite can EXIST at a SHA that happens to sit on
its row for an unrelated reason (a session stamp, a ruling id), which is a
line-existence coincidence, not an author's pin.  So the classifier proposes and
a human disposes -- and the human searches the WHOLE line, with an offset.  `--allow-unverified` exists for the case where the census has
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

    python3 manuscript/ave-kb/tools/migrate-pin-markers.py \
        --verified _orchestration/docket-entries/2026-09-07-r2-pin-verified.tsv
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

# Measured by hand over the FULL corpus TRUE-PIN population, THREE times:
# 5/5 (2026-09-07, line-scoped SHA heuristic), 2/5 (2026-09-07, two independent
# hand passes), 4/5 (2026-09-12, byte-level with character offsets quoted). The
# 4/5 supersedes: the 2/5 pass read two 3,964-byte rows by their opening ~100
# bytes and called them "contradicted" while the claimed content sat at offset
# 1,173 of the same line. See `_orchestration/docket-entries/2026-09-07-r2-pin-
# marker-census.md` §4 for the per-cite both-ways receipts and §4d for how
# 5 -> 2 -> 4 happened. Printed by --allow-unverified so nobody bulk-migrates
# without seeing it.
MEASURED_TRUE_PIN_PRECISION = (
    "4/5 (80%) hand-confirmed byte-level 2026-09-12, whole population, three passes "
    "(5/5 heuristic -> 2/5 head-of-row -> 4/5 byte-level); the 4/5 supersedes"
)


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


def rewrite_line(line: str, row, sha: str, lib) -> tuple[str, int]:
    """Insert `` pin:`sha` `` after every UNMARKED occurrence of this cite.

    Placement, not substitution: the marker goes immediately to the right of the
    cite as written, in whichever of the three forms it was written -- which is
    why this takes the row (form + path + line numbers) rather than a string.

    IDEMPOTENT by inspection, not by hope: each occurrence is skipped when
    `TRAILING_MARKER_RE` already matches at its right edge, so a second pass
    finds nothing to do even though the cite -- unlike under the `@sha`
    spelling -- REMAINS a well-formed cite that the census still classifies.

    Right-to-left so an earlier insertion cannot shift a later match's offsets.
    """
    occurrences = list(
        lib.cite_occurrence_re(row.form, row.path, row.start, row.end).finditer(line)
    )
    out, hits = line, 0
    for m in reversed(occurrences):
        if lib.TRAILING_MARKER_RE.match(out, m.end()):
            continue
        out = out[: m.end()] + f" pin:`{sha}`" + out[m.end():]
        hits += 1
    return out, hits


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
    # `already_marked` rows are the migration's own output on a re-run; a
    # marked cite is still a well-formed cite, so it is still classified.
    candidates = [r for r in rows if r.klass == "TRUE-PIN" and not r.already_marked]

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
            new, n = rewrite_line(lines[idx], row, marker_for(row), lib)
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
    all_true_pin = [r for r in rows if r.klass == "TRUE-PIN"]
    print(f"TRUE-PIN candidates in scope : {len(all_true_pin)}")
    print(f"  already marked             : {sum(1 for r in all_true_pin if r.already_marked)}")
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
