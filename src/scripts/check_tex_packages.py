#!/usr/bin/env python3
r"""Preflight the TeX toolchain against the manuscript's own \usepackage list.

WHY THIS EXISTS, MEASURED
-------------------------
The `manuscript-pdf` CI job ran twice on 2026-09-06/07 (Actions jobs
101579155504 @ 126a723b and 101585646220 @ 75e4eff8). Both reported `success`.
Neither typeset a single page: both the base build and the branch build died at
`! LaTeX Error: File 'lmodern.sty' not found.`, and both artifact uploads logged
`No files were found with the provided path: build/*.pdf`. The job's apt line
used `--no-install-recommends`, under which Debian's `lmodern` package (which
carries `lmodern.sty`) is only *Recommended* by `texlive-latex-recommended`;
`fonts-lmodern` installed, the `.sty` did not. Because the identical failure
reproduced at the merge base, the job's base-comparison logic classified an
ENVIRONMENT failure as PRE-EXISTING and exited 0.

So the job's failure was not a wrong package list alone -- it was that a missing
toolchain and a wrong manuscript looked the same to the check. This script
separates them: it asks only "can this machine resolve what the sources ask
for", answers before any typesetting is attempted, and exits non-zero with the
missing names when it cannot. A missing `.sty` is an environment defect and must
go red on its own terms, never be laundered through a base comparison.

WHAT IT CHECKS
--------------
  [1] `pdflatex` and `bibtex` are on PATH (the two binaries the Makefile's
      COMPILE_VOL macro invokes).
  [2] Every package named in a `\usepackage[...]{...}` in the scanned .tex tree
      resolves to a file via `kpsewhich <name>.sty`.

It parses the sources rather than carrying a hardcoded list, so a package added
to a preamble is covered without anyone remembering to update CI.

ANTI-TAUTOLOGY
--------------
The check can fail: `--selftest` injects a package name that cannot exist
(`ave-nonexistent-preflight-probe`) and asserts the resolver reports it missing.
If that probe resolves, the resolver is broken and the run aborts rather than
reporting a false clean. Run it in CI immediately before the real check.

Exit codes: 0 all resolve · 1 something is missing (or the binaries are absent)
· 2 the checker itself could not run (no kpsewhich, no .tex files, selftest
did not fire).
"""
import argparse
import os
import re
import shutil
import subprocess
import sys

# \usepackage, optionally with [options], then the mandatory {a,b,c} list.
USEPACKAGE_RE = re.compile(r"\\usepackage\s*(?:\[[^\]]*\])?\s*\{([^}]*)\}")
IMPOSSIBLE = "ave-nonexistent-preflight-probe"


def strip_comment(line: str) -> str:
    """Cut the line at the first unescaped % (LaTeX comment)."""
    out = []
    i = 0
    while i < len(line):
        c = line[i]
        if c == "\\" and i + 1 < len(line):
            out.append(line[i : i + 2])
            i += 2
            continue
        if c == "%":
            break
        out.append(c)
        i += 1
    return "".join(out)


def collect_packages(roots):
    """Return {package_name: sorted list of "path:line" sites}."""
    found = {}
    for root in roots:
        for dirpath, _dirs, files in os.walk(root):
            for fn in sorted(files):
                if not fn.endswith(".tex"):
                    continue
                path = os.path.join(dirpath, fn)
                try:
                    with open(path, encoding="utf-8", errors="replace") as fh:
                        lines = fh.readlines()
                except OSError:
                    continue
                for n, raw in enumerate(lines, 1):
                    for group in USEPACKAGE_RE.findall(strip_comment(raw)):
                        for name in group.split(","):
                            name = name.strip()
                            if name:
                                found.setdefault(name, []).append("%s:%d" % (path, n))
    return found


def resolve(name: str) -> str:
    """Absolute path of <name>.sty per kpsewhich, or '' if unresolvable."""
    try:
        out = subprocess.run(
            ["kpsewhich", name + ".sty"], capture_output=True, text=True
        )
    except FileNotFoundError:
        return ""
    return out.stdout.strip()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("roots", nargs="*", default=["manuscript"])
    ap.add_argument(
        "--selftest",
        action="store_true",
        help="prove the resolver can report a miss, then exit",
    )
    args = ap.parse_args()
    roots = args.roots or ["manuscript"]

    if shutil.which("kpsewhich") is None:
        print("[tex-preflight] ABORT: kpsewhich is not on PATH — no TeX installation "
              "to interrogate. This is an ENVIRONMENT failure, not a manuscript one.")
        return 2

    if args.selftest:
        hit = resolve(IMPOSSIBLE)
        if hit:
            print("[tex-preflight] ABORT: the impossible probe %r RESOLVED to %s. "
                  "The resolver is broken; a clean report would be false."
                  % (IMPOSSIBLE, hit))
            return 2
        print("[tex-preflight] selftest OK — the resolver reports a miss for %r, so a "
              "clean result below is a measurement, not a silence." % IMPOSSIBLE)
        return 0

    missing_bins = [b for b in ("pdflatex", "bibtex") if shutil.which(b) is None]
    if missing_bins:
        print("[tex-preflight] FAIL: binaries the Makefile invokes are absent: %s"
              % ", ".join(missing_bins))
        return 1

    packages = collect_packages(roots)
    if not packages:
        print("[tex-preflight] ABORT: no \\usepackage found under %s — the scan "
              "found nothing to check, which is not the same as clean."
              % ", ".join(roots))
        return 2

    missing = []
    for name in sorted(packages):
        if not resolve(name):
            missing.append(name)

    print("[tex-preflight] scanned roots: %s" % ", ".join(roots))
    print("[tex-preflight] distinct packages named in \\usepackage: %d"
          % len(packages))
    if missing:
        print("[tex-preflight] FAIL — %d of %d do not resolve via kpsewhich:"
              % (len(missing), len(packages)))
        for name in missing:
            sites = packages[name]
            print("    %-16s .sty NOT FOUND   first named at %s%s"
                  % (name, sites[0], "" if len(sites) == 1 else
                     " (+%d more sites)" % (len(sites) - 1)))
        print("[tex-preflight] This is an ENVIRONMENT defect: the sources ask for a "
              "package this machine cannot provide. Install it (Debian/Ubuntu: the "
              "package name is usually the TeX Live collection carrying it; note "
              "that `lmodern.sty` lives in the `lmodern` package, which "
              "`--no-install-recommends` will NOT pull in). Do not compare against a "
              "base build to decide whether this matters — it fails identically at "
              "every ref and tells you nothing about the manuscript.")
        return 1

    print("[tex-preflight] OK — every named package resolves.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
