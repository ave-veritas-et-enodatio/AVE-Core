#!/usr/bin/env python3
"""iomega_law_number_check.py — standing verify gate for the I_omega(A)-law lane.

Checks, on every `make verify` (all gating; exit nonzero on any failure):
  1. NUMERALS   — the result doc's load-bearing numeric tokens reconcile against the two
                  shipped JSONs (hit counts, class totals, digests, p values).
  2. LAW-RERUN  — iomega_law_check.py re-runs live and reproduces its shipped digest
                  (fast, pure-sympy; the scan driver is NOT re-run here — its G-DET
                  two-run receipt is banked in the result doc; its JSON is instead
                  integrity-checked by the numerals + completeness passes).
  3. COMPLETE   — the result doc's Appendix classification covers EVERY hit in the scan
                  JSON (per the frozen prereg section 3.2 rule), and the class totals
                  printed in the doc match a recount.
  4. QUOTES     — the load-bearing cite registry below re-verifies at HEAD: each excerpt
                  occurs within +/-2 lines of its registered line (G-CITE).
  5. MUTATION   — receipts that the instrument can fail: an in-memory perturbation of a
                  shipped digest, a perturbed quote-registry entry (FT-CITE), and a
                  perturbed classification row must each be caught.
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

DRIVERS = Path(__file__).resolve().parent
REPO = DRIVERS.parents[1]
RESULT_DOC = REPO / "research/2026-08-06_iomega-law_result.md"
SCAN_JSON = DRIVERS / "iomega_law_scan_results.json"
CHECK_JSON = DRIVERS / "iomega_law_check_results.json"

FAIL: list[str] = []


def check(cond: bool, msg: str) -> None:
    if not cond:
        FAIL.append(msg)


# --- the load-bearing cite registry (G-CITE): (path, line, excerpt) -------------------
QUOTE_REGISTRY = [
    ("manuscript/ave-kb/common/universal-saturation-kernel-catalog.md", 145,
     "All 26 catalog instances are SWING-typed."),
    ("manuscript/ave-kb/common/universal-saturation-kernel-catalog.md", 171, "pending A4"),
    ("manuscript/ave-kb/common/operators.md", 139,
     "the canonical μ-kernel is slew-KEYED"),
    ("manuscript/common_equations/eq_calibration_constants.tex", 47,
     "per-node inductance (rotational inertia)"),
    ("manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/relativistic-inductor.md",
     15, "I_{max} = \\xi_{topo}\\, c \\approx 124.4"),
    ("manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/pvlas-static-b-verdict.md",
     29, "ideal relativistic inductor keyed on the"),
    ("manuscript/ave-kb/vol3/claim-quality.md", 451,
     "longitudinal inertia in 3D spherical collapse"),
    ("manuscript/vol_3_macroscopic/chapters/15_black_hole_orbital_resonance.tex", 445,
     "longitudinal inertia scales with the Lorentz factor"),
    ("manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/interior-singularity-resolution.md",
     16, "Topo-Relativistic Impedance Divergence"),
    ("research/2026-07-31_qlaw-framing-challenge_walk.md", 1201,
     "two different substances, and canon must say so"),
    ("manuscript/ave-kb/common/wall-taxonomy.md", 433, "the fork is still OPEN"),
    ("research/2026-08-05_last-bond-kernel-collapse_result.md", 151,
     "carries no micro-rotation at all"),
    ("_orchestration/docket-entries/2026-08-05-srs-twist-coefficient.md", 22,
     "zero free positional parameters"),
    ("manuscript/ave-kb/common/axiom-register.md", 190, "underdetermined at $O(\\alpha)$"),
    ("research/_archive/L5/axiom_derivation_status.md", 313,
     "cleanliness only, NOT load-bearing for closure"),
    ("research/2026-08-05_a008-factor-propagation_note.md", 175,
     "G_c/I_\\omega = \\omega_C^2 = 1"),
    ("src/ave/topological/cosserat_field_3d.py", 761, "S_eps_sq = jnp.clip"),
    ("src/ave/topological/cosserat_field_3d.py", 954, "phase-I placeholder"),
    ("src/ave/topological/cosserat_field_3d.py", 967, "self.I_omega = float(I_omega)"),
    ("src/scripts/vol_1_foundations/r8_diag_a_cosserat_wave_speed.py", 257,
     "add S factor to T_kinetic via ρ → ρ·S, I_ω → I_ω·S."),
]

WINDOW = 2  # +/- lines


def quote_ok(path: str, line: int, excerpt: str) -> bool:
    try:
        lines = (REPO / path).read_text(encoding="utf-8").splitlines()
    except FileNotFoundError:
        return False
    lo = max(0, line - 1 - WINDOW)
    hi = min(len(lines), line + WINDOW)
    return excerpt in "\n".join(lines[lo:hi])


def main() -> int:
    doc = RESULT_DOC.read_text(encoding="utf-8")
    scan = json.loads(SCAN_JSON.read_text(encoding="utf-8"))
    law = json.loads(CHECK_JSON.read_text(encoding="utf-8"))

    # 1. NUMERALS ----------------------------------------------------------------------
    check(scan["digest_excluding_runtime"] in doc,
          "scan digest missing from result doc")
    check(law["digest_excluding_runtime"] in doc,
          "law-check digest missing from result doc")
    census = {"P-NC3": 6, "P-NC4": 0, "P-I3a": 14, "P-I3b": 19, "P-I3c": 34,
              "P-I4": 0, "P-I5": 67, "P-I6": 0, "P-CAT": 0}
    for pid, expected in census.items():
        got = len(scan["patterns"][pid]["hits_union"])
        check(got == expected,
              f"{pid}: shipped JSON has {got} union hits, doc census says {expected}")
    check(scan["meta"]["tracked_blob_count"] == 5075 and "5075" in doc,
          "tracked-blob count 5075 mismatch (JSON vs doc)")
    # p-values per branch in the shipped law JSON reconcile with the doc's section-3 table
    want = {("ARM-0", "1"): "1/2", ("ARM-0", "2"): "1",
            ("ARM-1", "1"): "0", ("ARM-1", "2"): "1/2"}
    for br in law["branches"]:
        arm = br["name"].split(" ")[0]
        for row in br["knife_rows"]:
            check(want.get((arm, row["a"])) == row["p"],
                  f"{arm} a={row['a']}: shipped p={row['p']} != doc table")
            check(row["engines_agree"], f"{arm} a={row['a']}: engine pair disagrees")
    check(all(g.get("pass", g.get("fires", False)) for g in law["gates"].values()),
          "a law-stage gate is not green in the shipped JSON")
    check(all(scan["gates"][g].get("pass", scan["gates"][g].get("fires", False))
              for g in scan["gates"]),
          "a scan-stage gate is not green in the shipped JSON")

    # 2. LAW-RERUN ---------------------------------------------------------------------
    r = subprocess.run([sys.executable, str(DRIVERS / "iomega_law_check.py")],
                       capture_output=True, text=True, cwd=REPO)
    check(r.returncode == 0, f"iomega_law_check.py re-run failed: {r.stdout[-300:]}")
    law2 = json.loads(CHECK_JSON.read_text(encoding="utf-8"))
    check(law2["digest_excluding_runtime"] == law["digest_excluding_runtime"],
          "law-check re-run digest drifted")

    # 3. COMPLETE ----------------------------------------------------------------------
    doc_sites = set(re.findall(r"\| \d+ \| `([^`]+):(\d+)` \|", doc))
    missing = []
    for pid, p in scan["patterns"].items():
        for path, line, _text in p["hits_union"]:
            if (path, str(line)) not in doc_sites:
                missing.append(f"{pid} {path}:{line}")
    check(not missing,
          f"classification appendix missing {len(missing)} hits: {missing[:5]}")
    for token in ("'ARCHIVE-STAGED': 36", "'NON-LAW': 63", "'DISCOURSE': 41",
                  "CANON-LAW count: 0"):
        check(token in doc, f"class-total token missing from doc: {token}")

    # 4. QUOTES (G-CITE) ---------------------------------------------------------------
    for path, line, excerpt in QUOTE_REGISTRY:
        check(quote_ok(path, line, excerpt),
              f"G-CITE: excerpt not within ±{WINDOW} lines of {path}:{line}: {excerpt[:50]!r}")

    # 5. MUTATION receipts -------------------------------------------------------------
    mutated_digest = scan["digest_excluding_runtime"][:-1] + (
        "0" if scan["digest_excluding_runtime"][-1] != "0" else "1")
    check(mutated_digest not in doc, "mutation receipt: perturbed scan digest found in doc")
    p0, l0, e0 = QUOTE_REGISTRY[0]
    check(not quote_ok(p0, l0 + 7, e0 + "X"),
          "FT-CITE mutation receipt: perturbed registry entry did not fail")
    check(("NOT-A-REAL-PATH.md", "1") not in doc_sites,
          "mutation receipt: phantom classification row matched")

    if FAIL:
        print("[iomega_law_number_check] FAIL")
        for f in FAIL:
            print("  ✗", f)
        return 1
    print(f"[iomega_law_number_check] PASS — numerals + law-rerun + completeness "
          f"({sum(len(p['hits_union']) for p in scan['patterns'].values())} hits) + "
          f"{len(QUOTE_REGISTRY)} registry quotes + mutation receipts")
    return 0


if __name__ == "__main__":
    sys.exit(main())
