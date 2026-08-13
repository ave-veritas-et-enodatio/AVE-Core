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


def sh(args: list[str]) -> tuple[int, str]:
    p = subprocess.run(args, capture_output=True, text=True)
    return p.returncode, p.stdout


def tracked_files(root: Path) -> list[str]:
    rc, out = sh(["git", "-C", str(root), "ls-files"])
    if rc != 0:
        print("[cite-stability] FATAL: git ls-files failed", file=sys.stderr)
        sys.exit(2)
    return [f for f in out.split("\n") if f and Path(f).suffix in SCAN_SUFFIXES]


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
    for (citing, cited, line) in collect_cites(root, None):
        # only judge pins that still exist in the CURRENT text of the citing file
        if not resolves(at(head_cache, None, cited), line):
            if resolves(at(base_cache, base, cited), line):
                broken.append({"citing_file": citing, "cited_path": cited, "line": line})
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
    pins = list(CITE_RE.finditer("see `manuscript/predictions.yaml:295` and foo.py:12-14"))
    got = [(m.group("path"), m.group("start")) for m in pins]
    want = [("manuscript/predictions.yaml", "295"), ("foo.py", "12")]
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

    broken = check(a.root, a.base)
    if a.json:
        print(json.dumps({"base": a.base, "broken": broken}, indent=2))
    elif not broken:
        print(f"[cite-stability] no line-pin regressions vs {a.base}.")
    else:
        print(
            f"[cite-stability] {len(broken)} line-pin(s) RESOLVED at {a.base} and are "
            f"now dead. Repoint them — preferably to an anchor/symbol/entry-id rather "
            f"than a new line number, which will drift again:\n"
        )
        for b in broken:
            print(f"  {b['citing_file']}  ->  {b['cited_path']}:{b['line']}")
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
