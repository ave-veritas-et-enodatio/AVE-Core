#!/usr/bin/env python3
"""
ξ Namespace Collision Guard — a focused regression gate for the two ξ-glyph
mis-uses corrected by the xi-symbol-cleanup PR.

Two distinct ξ-objects share the Greek letter ξ and were corrupted:

  (i)  The Machian hierarchy coupling formula ξ = 4π(R_H/ℓ_node)α⁻² (≈ 8.15e43)
       was repeatedly printed with the MAGNITUDE of its internal FACTOR
       R_H/ℓ_node (≈ 3.46e38) — a 5.4-OOM mis-pairing. This gate FAILS if the
       Machian formula co-occurs (within N lines) with a 1e38-family magnitude.

  (ii) ξ_topo (= e/ℓ_node, a C/m constant) is shorthand-equated to √α (the
       dimensionless native value of the charge e) across the corpus. Strictly
       √α is the native value of e (e = ξ_topo·ℓ_node = √α in natural units),
       NOT of the C/m constant ξ_topo. This is the FIX-9 conflation — currently
       a PENDING Grant-call (the "ξ_topo = √α in native units" phrasing is a
       widespread CLEAVE-01-echo convention, ~18 sites, not an isolated bug),
       so check (ii) is ADVISORY (reports sites, does NOT fail the gate) until
       Grant adjudicates the convention. Re-promote to hard-fail once resolved.

Canonical disambiguation: manuscript/ave-kb/common/xi-topo-traceability.md and
the ξ def-node in manuscript/ave-kb/common/vocabulary-register.md.

Exit codes:
  0 — clean (no magnitude mis-pairing; check (ii) advisory only)
  1 — at least one check-(i) magnitude collision found (printed to stderr)

Scope: skips audit-trail-preserved trees per audit-trail-in-git discipline
(_archive, *_FROZEN preregs, SESSION_STATE, result/walk-back docs, .git, and
THIS file plus the traceability/register/cheatsheet leaves that legitimately
quote both magnitudes side-by-side to document the watch-list).
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]

# Window (lines) within which the Machian formula and a 1e38-magnitude
# co-occurring is treated as the mis-pairing.
WINDOW = 3

# --- Check (i): the Machian formula near a 1e38-family magnitude --------------
# Match the formula in either Unicode/markdown or LaTeX spacing variants.
FORMULA = re.compile(
    r"4\\?pi\s*\\?left?\(?\s*\\?frac?\{?\s*R[_{]?H\}?\s*/?\}?\{?\s*"
    r"(?:\\ell_\{?node\}?|ℓ_?\{?node\}?|l_node)"
    r"\}?\s*\\?right?\)?\s*\\?alpha\s*\^?\{?-?2\}?|"
    r"4π\s*\(?\s*R_?H\s*/\s*(?:ℓ_?node|\\ell_\{node\})\s*\)?\s*α[⁻^]?\{?-?2\}?",
    re.IGNORECASE,
)
# 1e38-family magnitudes that are the FACTOR, not ξ_M.
BAD_MAG = re.compile(
    r"(?:3\.4(?:55)?|3\.46)?\s*[×x*]?\s*10\s*[\^{]?\s*\{?38\}?|"
    r"10³⁸|1e38|3\.455e38|3\.46e38|≈\s*10\^?38",
)

# --- Check (ii): ξ_topo = √α conflation --------------------------------------
XI_TOPO_SQRT_ALPHA = re.compile(
    r"(?:\\?xi_\{?topo\}?|ξ_?\{?topo\}?)\s*=\s*"
    r"(?:\\?sqrt\s*\{?\s*\\?alpha\}?|√\s*α|√\\?alpha)",
    re.IGNORECASE,
)

# Files/trees that legitimately document BOTH magnitudes side-by-side (the
# watch-list leaves) or preserve audit history — excluded from check (i)
# co-occurrence (they intentionally print the factor next to ξ_M to teach the
# distinction). They are NOT excluded from check (ii).
WATCHLIST_LEAVES = {
    "manuscript/ave-kb/common/xi-topo-traceability.md",
    "manuscript/ave-kb/common/natural-units-cheatsheet.md",
    "manuscript/ave-kb/common/divergence-test-substrate-map.md",
    "manuscript/ave-kb/common/q-g47-substrate-scale-cosserat-closure.md",
    "manuscript/ave-kb/common/claim-quality.md",
    "manuscript/ave-kb/common/interlock-register.md",
    "manuscript/ave-kb/common/vocabulary-register.md",
    "src/scripts/verify_xi_namespace.py",
}

SKIP_DIR_TOKENS = ("/_archive/", "/.git/", "/SESSION_STATE")
SKIP_NAME_TOKENS = ("_FROZEN", "session_state", "_result", "_walk-back", "_walkback")
SCAN_SUFFIXES = (".md", ".tex", ".py")


def _skip(path: Path) -> bool:
    s = str(path)
    if any(tok in s for tok in SKIP_DIR_TOKENS):
        return True
    name = path.name.lower()
    return any(tok in name for tok in SKIP_NAME_TOKENS)


def main() -> int:
    hard_violations: list[str] = []  # check (i) — fails the gate
    advisories: list[str] = []  # check (ii) — reported, does NOT fail
    rel_watchlist = {(REPO / p) for p in WATCHLIST_LEAVES}

    for path in REPO.rglob("*"):
        if not path.is_file() or path.suffix not in SCAN_SUFFIXES or _skip(path):
            continue
        # The guard's own source quotes both patterns to document them.
        if path == Path(__file__).resolve():
            continue
        try:
            lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
        except OSError:
            continue

        # Check (ii) ADVISORY: ξ_topo = √α conflation (FIX-9, pending Grant).
        for i, line in enumerate(lines, 1):
            if XI_TOPO_SQRT_ALPHA.search(line):
                advisories.append(
                    f"{path.relative_to(REPO)}:{i}: ξ_topo shorthand-equated to √α "
                    f"(√α is the native value of e, NOT of the C/m ξ_topo): {line.strip()[:110]}"
                )

        # Check (i) HARD: Machian formula near a 1e38 magnitude — exempt watch-list.
        if path in rel_watchlist:
            continue
        formula_lines = [i for i, ln in enumerate(lines) if FORMULA.search(ln)]
        for fi in formula_lines:
            lo, hi = max(0, fi - WINDOW), min(len(lines), fi + WINDOW + 1)
            for j in range(lo, hi):
                if BAD_MAG.search(lines[j]):
                    hard_violations.append(
                        f"{path.relative_to(REPO)}:{fi + 1}: Machian formula "
                        f"4π(R_H/ℓ_node)α⁻² co-occurs with a 1e38-family magnitude "
                        f"at line {j + 1} (ξ_M ≈ 8.15e43; 1e38 is the cell-count "
                        f"FACTOR, not ξ): {lines[j].strip()[:90]}"
                    )
                    break

    if advisories:
        print(
            f"ξ namespace ADVISORY (check ii, non-gating): {len(advisories)} "
            f"'ξ_topo = √α' site(s) — FIX-9 convention, pending Grant adjudication:"
        )
        for v in advisories:
            print(f"  {v}")
        print()

    if hard_violations:
        print("ξ NAMESPACE COLLISION GUARD: FAIL (check i — magnitude mis-pairing)", file=sys.stderr)
        for v in hard_violations:
            print(f"  {v}", file=sys.stderr)
        print(
            "\nCanonical disambiguation: "
            "manuscript/ave-kb/common/xi-topo-traceability.md + the ξ def-node "
            "in manuscript/ave-kb/common/vocabulary-register.md.",
            file=sys.stderr,
        )
        return 1

    print("ξ namespace collision guard: PASS (check i — no Machian/factor magnitude mis-pairing).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
