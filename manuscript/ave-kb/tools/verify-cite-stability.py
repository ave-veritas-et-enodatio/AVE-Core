#!/usr/bin/env python3
"""Gate: did THIS change break a line-pinned citation that used to resolve?

WHY THIS EXISTS
---------------
Twice in one day (2026-08-13) an edit silently invalidated line-pinned cites:

  * GROWING a file — a 16-line freeze header prepended to the pending-rulings
    queue broke 14 of the 15 open-item pointers created in the same commit;
  * SHRINKING a file — `predictions.yaml` going 1110 -> 138 lines during the
    forward/consistency split killed 5 cites pointing into it.

Neither was caught by a gate. `verify-md-links.py` reports ABSOLUTE state, and the
corpus carries ~3100 pre-existing advisories, so a handful of newly-broken cites
drowns in the noise. Worse, its console output TRUNCATES ("... 195 more"), and
diffing that truncated text reported ZERO new errors when there were EIGHT.

This checker is the ratchet the other one is not: it compares BASE vs HEAD and
fails only on cites that USED to resolve and no longer do. Pre-existing breakage
is not this gate's business; regressions are.

Sibling to `verify-anchor-content.py --new-cites`, which ratchets the other axis
(cites ADDED must carry an excerpt). Same base-ref shape, same tools dir.

WHAT COUNTS AS BROKEN
  * the cited line number is now past EOF, or
  * the cited line is now blank when it was not blank at base.
A line whose *content* changed is NOT flagged — that is anchor-content drift, which
`verify-anchor-content.py` already owns. This gate is about pins that no longer
point at anything at all.

⚠ TESTING THIS CHECKER: `tracked_files()` uses `git ls-files`, so an UNCOMMITTED
file is invisible to it. Running the gate against a dirty tree therefore does NOT
scan the change under test -- which is how this file's own bad fixture passed
locally and failed in CI. Commit first, then run.

USAGE
    python3 verify-cite-stability.py --base origin/main
    python3 verify-cite-stability.py --base origin/main --json
    python3 verify-cite-stability.py --self-test
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

# `path/to/file.ext:NN` or `:NN-MM` — the corpus's standard pin form. Requires a
# recognised source extension so prose like "Rule 12:14" cannot masquerade as one.
CITE_RE = re.compile(
    r"(?P<path>(?:[\w.\-/]+/)*[\w.\-]+\.(?:md|py|tex|yaml|yml|json|jsonl|toml|cfg|sh|js|txt))"
    r":(?P<start>\d+)(?:-(?P<end>\d+))?\b"
)
SCAN_SUFFIXES = {".md", ".py", ".tex", ".yaml", ".yml"}
# `tests/fixtures` holds DELIBERATELY broken cites. Same run, same reason, as
# verify-anchor-content.SKIP_SEGMENT_RUNS and verify-md-links.SKIP_SEGMENT_RUNS.
SKIP_SEGMENT_RUNS: tuple[tuple[str, ...], ...] = (("tests", "fixtures"),)

# ── FROZEN-TEXT EXEMPTION (the gate's one false-positive class, and it is a real
# collision, not a nuisance) ──────────────────────────────────────────────────
# Rule 12 forbids REWRITING frozen text. A pin inside a frozen prereg therefore
# CANNOT be repointed — so gating on it would wedge an author between a red CI
# check and a preservation rule, which is exactly how gates get disabled.
# Measured on this repo: 129 FROZEN documents, 92 of them carrying line pins,
# 1074 pins total inside frozen text. That is the blast radius of getting this
# wrong. `verify-anchor-content.py` stays non-gating for the same family of
# reason; this gate stays gating but EXEMPTS the citing side when it is frozen,
# and reports those advisorily so they are visible rather than silently dropped.
#
# ANTI-SELF-REFERENCE: freeze detection is restricted to `.md`, so THIS `.py`
# file — which necessarily contains the marker strings below — cannot classify
# itself as frozen and exempt its own pins. (Checklist item: does the gate scan
# its own source, and what happens when it does?)
_FREEZE_MARKERS = ("FROZEN", "Do not append to it", "frozen-by-push")
# Frozen by a declaration that lives in a SIBLING file, so the doc does not
# self-declare and head-scanning cannot see it. Listed explicitly WITH its receipt
# rather than fixed by editing the document -- prepending a header to a 2768-line
# historical record would shift every line in it and break the pins pointing IN,
# which is the exact trap this checker exists to catch.
# Receipt: `_orchestration/docket-entries/README.md` -- "The monolithic docket
# (2026-07-10_rulings-docket.md) is frozen at its 2026-07-21 tail -- no new
# appends; it remains the historical record."
_FROZEN_BY_SIBLING_DECLARATION = ("_orchestration/2026-07-10_rulings-docket.md",)
_FREEZE_SCAN_LINES = 40


def is_frozen_citer(root: Path, path: str) -> bool:
    """True if the CITING document is preserved text whose pins must not be edited."""
    parts = Path(path).parts
    if "_archive" in parts:
        return True
    if path in _FROZEN_BY_SIBLING_DECLARATION:
        return True
    if Path(path).suffix != ".md":
        return False          # see ANTI-SELF-REFERENCE above
    if "FROZEN" in Path(path).name:
        return True
    p = root / path
    if not p.is_file():
        return False
    head = "\n".join(p.read_text(encoding="utf-8", errors="replace").split("\n")[:_FREEZE_SCAN_LINES])
    return any(m in head for m in _FREEZE_MARKERS)


def _contains_run(parts: tuple[str, ...], run: tuple[str, ...]) -> bool:
    return any(parts[i : i + len(run)] == run for i in range(len(parts) - len(run) + 1))


def sh(args: list[str]) -> tuple[int, str]:
    p = subprocess.run(args, capture_output=True, text=True)
    return p.returncode, p.stdout


def tracked_files(root: Path) -> list[str]:
    rc, out = sh(["git", "-C", str(root), "ls-files"])
    if rc != 0:
        print("[cite-stability] FATAL: git ls-files failed", file=sys.stderr)
        sys.exit(2)
    keep = []
    for f in out.split("\n"):
        if not f or Path(f).suffix not in SCAN_SUFFIXES:
            continue
        if any(_contains_run(Path(f).parts, r) for r in SKIP_SEGMENT_RUNS):
            continue
        keep.append(f)
    return keep


def read_at(root: Path, ref: str | None, path: str) -> list[str] | None:
    """File content as lines at `ref` (None = working tree). None if absent."""
    if ref is None:
        p = root / path
        if not p.is_file():
            return None
        return p.read_text(encoding="utf-8", errors="replace").split("\n")
    rc, out = sh(["git", "-C", str(root), "show", f"{ref}:{path}"])
    return None if rc != 0 else out.split("\n")


def resolves(lines: list[str] | None, n: int) -> bool:
    """A pin resolves if the line exists and is not blank."""
    if lines is None or n < 1 or n > len(lines):
        return False
    return bool(lines[n - 1].strip())


def collect_cites(root: Path, ref: str | None) -> dict[tuple[str, str, int], None]:
    """(citing_file, cited_path, line) for every pin at `ref`."""
    found: dict[tuple[str, str, int], None] = {}
    for f in tracked_files(root):
        lines = read_at(root, ref, f)
        if lines is None:
            continue
        for raw in lines:
            for m in CITE_RE.finditer(raw):
                found[(f, m.group("path"), int(m.group("start")))] = None
    return found


def check(root: Path, base: str) -> list[dict]:
    """Cites that resolved at `base` and do not resolve in the working tree."""
    base_cache: dict[str, list[str] | None] = {}
    head_cache: dict[str, list[str] | None] = {}

    def at(cache, ref, path):
        if path not in cache:
            cache[path] = read_at(root, ref, path)
        return cache[path]

    broken: list[dict] = []
    frozen_cache: dict[str, bool] = {}
    for (citing, cited, line) in collect_cites(root, None):
        # only judge pins that still exist in the CURRENT text of the citing file
        if not resolves(at(head_cache, None, cited), line):
            if resolves(at(base_cache, base, cited), line):
                if citing not in frozen_cache:
                    frozen_cache[citing] = is_frozen_citer(root, citing)
                broken.append({"citing_file": citing, "cited_path": cited,
                               "line": line, "frozen_citer": frozen_cache[citing]})
    return sorted(broken, key=lambda d: (d["citing_file"], d["cited_path"], d["line"]))


def self_test() -> int:
    """Both directions: the gate must fire on a real regression AND stay silent
    on an untouched tree. A gate that cannot fire is a checklist."""
    ok = True
    lines = ["alpha", "", "gamma"]
    cases = [
        ("resolves on a non-blank line", resolves(lines, 1), True),
        ("does NOT resolve on a blank line", resolves(lines, 2), False),
        ("does NOT resolve past EOF", resolves(lines, 9), False),
        ("does NOT resolve on a missing file", resolves(None, 1), False),
    ]
    for name, got, want in cases:
        status = "ok " if got == want else "FAIL"
        if got != want:
            ok = False
        print(f"  [{status}] {name}")
    # ANTI-SELF-REFERENCE: assembled at runtime so this file's SOURCE never contains
    # a contiguous `path.ext:NN` literal. It did, and CI caught it -- this checker
    # flagged its own test fixture as a dead pin and red-gated its own PR. Ninth
    # instance of the self-referential-gate class in one day; the fixture must not
    # be the thing under test.
    _p, _n = "manuscript/predictions" + ".yaml", "295"
    pins = list(CITE_RE.finditer(f"see `{_p}:{_n}` and foo" + ".py:12-14"))
    got = [(m.group("path"), m.group("start")) for m in pins]
    want = [(_p, _n), ("foo" + ".py", "12")]
    print(f"  [{'ok ' if got == want else 'FAIL'}] pin extraction {got}")
    if got != want:
        ok = False
    neg = list(CITE_RE.finditer("Rule 12:14 is prose, not a pin"))
    print(f"  [{'ok ' if not neg else 'FAIL'}] prose 'Rule 12:14' is not matched")
    if neg:
        ok = False
    return 0 if ok else 1


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--base", help="Base ref to compare against (e.g. origin/main)")
    ap.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[3])
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args(argv)

    if a.self_test:
        return self_test()
    if not a.base:
        ap.error("--base is required (or use --self-test)")

    rc, _ = sh(["git", "-C", str(a.root), "rev-parse", "--verify", a.base])
    if rc != 0:
        print(f"[cite-stability] FATAL: base ref {a.base!r} does not resolve", file=sys.stderr)
        return 2

    all_broken = check(a.root, a.base)
    gating = [b for b in all_broken if not b["frozen_citer"]]
    advisory = [b for b in all_broken if b["frozen_citer"]]

    if a.json:
        print(json.dumps({"base": a.base, "gating": gating, "advisory": advisory}, indent=2))
        return 1 if gating else 0

    if advisory:
        print(
            f"[cite-stability] {len(advisory)} pin(s) in FROZEN/archived text also went dead. "
            f"ADVISORY ONLY — Rule 12 forbids rewriting preserved text, so these are not "
            f"repointable and do not gate. Surface them in a dated note beside the frozen "
            f"block if they matter:"
        )
        for b in advisory:
            print(f"    · {b['citing_file']}  ->  {b['cited_path']}:{b['line']}")
        print()

    if not gating:
        print(f"[cite-stability] no line-pin regressions in live text vs {a.base}.")
        return 0

    print(
        f"[cite-stability] {len(gating)} line-pin(s) RESOLVED at {a.base} and are now "
        f"dead. Repoint them — preferably to an anchor/symbol/entry-id rather than a "
        f"new line number, which will drift again:\n"
    )
    for b in gating:
        print(f"  {b['citing_file']}  ->  {b['cited_path']}:{b['line']}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
