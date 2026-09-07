#!/usr/bin/env python3
"""Census of SHA-pinned line-cites — the measurement half of ruling R2.

Read-only.  Prints, for every markdown line-cite that sits on a line carrying a
backticked SHA (i.e. every cite `verify-md-links.py` silently exempts today),
which of TRUE-PIN / LIVE / DEAD it actually is.  See `pin_census_lib` for the
class definitions and for why the objective arm (does the cite resolve at the
SHA on its own line?) leads the prose arm.

    python3 manuscript/ave-kb/tools/pin-census.py                # corpus-wide
    python3 manuscript/ave-kb/tools/pin-census.py --scope kb     # KB tree only
    python3 manuscript/ave-kb/tools/pin-census.py --dir _orchestration/docket-entries
    python3 manuscript/ave-kb/tools/pin-census.py --list DEAD    # itemise a class
    python3 manuscript/ave-kb/tools/pin-census.py --json out.json

Exit code is 0 whatever the census finds: this is a measuring instrument, not a
gate.  The gate is `verify-md-links.py`, which a parallel lane owns.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from collections import Counter
from pathlib import Path

_HERE = Path(__file__).resolve().parent


def _load_lib():
    spec = importlib.util.spec_from_file_location("pin_census_lib", _HERE / "pin_census_lib.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


CLASSES = ("TRUE-PIN", "LIVE", "DEAD", "UNRESOLVED-PATH", "SKIPPED-SHAPE")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--repo-root", type=Path, default=None)
    parser.add_argument("--scope", choices=("corpus", "kb"), default="corpus")
    parser.add_argument("--dir", dest="subdir", default=None,
                        help="restrict to markdown under this repo-relative dir")
    parser.add_argument("--list", dest="listing", choices=CLASSES, action="append", default=None)
    parser.add_argument("--json", dest="json_out", type=Path, default=None)
    args = parser.parse_args(argv)

    lib = _load_lib()
    vml = lib.load_vml()
    repo_root = (args.repo_root or Path(__file__).resolve().parents[3]).resolve()

    md_files = list(vml.iter_markdown_files(repo_root))
    if args.scope == "kb":
        kb = repo_root / "manuscript" / "ave-kb"
        md_files = [f for f in md_files if kb in f.parents]
    if args.subdir:
        base = (repo_root / args.subdir).resolve()
        md_files = [f for f in md_files if base == f or base in f.parents]

    file_index, _ = vml.build_kbleaf_target_index(repo_root)
    rows = lib.classify(repo_root, vml, file_index, md_files)

    # Counted by READING the files, not off `rows`. A `` pin:`sha` `` marker
    # sits OUTSIDE the cite token, so -- unlike the `@sha` spelling an earlier
    # revision used -- a marked cite REMAINS a well-formed cite and keeps being
    # classified. This count is therefore markers-in-text, and `already marked`
    # below is the per-cite view of the same thing.
    marked = 0
    for f in md_files:
        try:
            # Fence-stripped, so this counts markers in PROSE and matches the
            # population `iter_line_cites` walks. Unstripped it would also count
            # CONVENTIONS.md's own fenced example of the token, which is
            # documentation of the grammar, not a pin on a real cite.
            marked += lib.count_markers(vml.strip_fences(f.read_text(encoding="utf-8")))
        except (OSError, UnicodeDecodeError):
            continue

    counts = Counter(r.klass for r in rows)
    sha_lines = {(r.source, r.lineno) for r in rows}
    wide = {(r.source, r.lineno) for r in rows if r.line_len > 500}

    scope = args.subdir or args.scope
    print(f"=== SHA-pinned line-cite census — scope: {scope} ===")
    print(f"markdown files scanned          : {len(md_files)}")
    print(f"line-cites on SHA-bearing lines : {len(rows)}")
    print(f"  ... on distinct lines         : {len(sha_lines)}")
    print(f"  ... of those, lines >500 chars: {len(wide)}")
    print(f"pin:`sha` markers in prose      : {marked}")
    print(f"  ... cites bound by one        : {sum(1 for r in rows if r.already_marked)}")
    print()
    for klass in CLASSES:
        print(f"  {klass:<16} {counts.get(klass, 0):>5}")
    print()
    checkable = counts.get("TRUE-PIN", 0) + counts.get("LIVE", 0) + counts.get("DEAD", 0)
    print(f"  checkable (TRUE-PIN+LIVE+DEAD) {checkable:>5}")
    if checkable:
        print(f"  LIVE share of checkable        {counts.get('LIVE', 0) / checkable:>5.1%}"
              "   <- exempted today for no reason (R2's false negatives)")
        print(f"  DEAD share of checkable        {counts.get('DEAD', 0) / checkable:>5.1%}"
              "   <- rot the exemption hides")
    tp = [r for r in rows if r.klass == "TRUE-PIN"]
    if tp:
        print()
        print(f"  TRUE-PIN resolving at a row SHA (all, by construction) : {sum(1 for r in tp if r.resolving_shas)}")
        print(f"  TRUE-PIN also corroborated by prose                    : {sum(1 for r in tp if r.prose_marker)}")
        print(f"  TRUE-PIN already carrying a marker                     : {sum(1 for r in tp if r.already_marked)}")

    # The loudest thing this census can find: a cite that resolves at NEITHER
    # end, on a line whose prose asserts it is deliberately pinned. Before the
    # D2 repair these were classified TRUE-PIN on the prose alone and were
    # migratable -- i.e. the tool would have signed rot as an author's intent.
    laundering = [r for r in rows if r.prose_marker and r.klass in ("DEAD", "UNRESOLVED-PATH")]
    if laundering:
        print()
        print(f"  ⚠ prose claims a pin but the cite resolves at NEITHER end : {len(laundering)}")
        for r in laundering:
            print(f"      {r.source}:{r.lineno}  {r.as_written}  [{r.klass}]")

    for klass in args.listing or ():
        print()
        print(f"--- {klass} ---")
        for r in sorted(rows, key=lambda r: (r.klass, r.source, r.lineno)):
            if r.klass != klass:
                continue
            extra = ""
            if r.resolving_shas:
                extra = f"  resolves@{','.join(r.resolving_shas)}"
            elif r.prose_marker:
                extra = "  prose-marker"
            print(f"{r.source}:{r.lineno}  {r.as_written}  "
                  f"[shas={','.join(r.line_shas) or '-'} len={r.line_len} "
                  f"cites_on_line={r.cites_on_line}]{extra}")

    if args.json_out:
        args.json_out.write_text(
            json.dumps([r.__dict__ for r in rows], indent=1, default=list) + "\n",
            encoding="utf-8",
        )
        print(f"\nwrote {args.json_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
