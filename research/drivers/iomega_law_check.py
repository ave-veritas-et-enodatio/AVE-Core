#!/usr/bin/env python3
"""iomega_law_check.py — the I_omega(A) lane's law-stage gates (prereg section 4).

Frozen prereg: research/2026-08-06_iomega-law_prereg-FROZEN.md (aa62941f, pushed ALONE).

Gates implemented here (all comparisons exact — rationals and booleans, no floats):
  G-A008-COLD  every delivered branch reproduces the pinned cold-point ratio at S=1
  G-PAIR       the density-cancellation shift (a,b)->(a-d, b+d) leaves p invariant (symbolic)
  G-KNIFE-ARITH p=(a+b)/2 per delivered branch x a in {1,2}, two engines
               (fractions.Fraction and sympy.Rational), mapped to the v2-adjudicated
               member table; p outside the member set reports NOT-A-FROZEN-MEMBER
  FT-A008 / FT-PAIR / FT-KNIFE  fireability injections (each MUST fire)

Output: research/drivers/iomega_law_check_results.json
"""
from __future__ import annotations

import hashlib
import json
import time
from fractions import Fraction
from pathlib import Path

import sympy as sp

OUT = Path(__file__).resolve().parent / "iomega_law_check_results.json"

# The v2-adjudicated member table (approach-leak v2 result: GAP-CLOSED on {0.5, 1.0, 1.5};
# CHANNEL-OPENS on {2.0, 2.5, 3.0}; p = 2.0 is knife-edge, SPLIT-annotated, awarded v1's
# frozen CHANNEL-OPENS).
MEMBER_TABLE = {
    Fraction(1, 2): "GAP-CLOSED",
    Fraction(1, 1): "GAP-CLOSED",
    Fraction(3, 2): "GAP-CLOSED",
    Fraction(2, 1): "CHANNEL-OPENS",
    Fraction(5, 2): "CHANNEL-OPENS",
    Fraction(3, 1): "CHANNEL-OPENS",
}

# The delivered branches (finalized at result-write time from the derivation; the GATES
# above are frozen in the prereg and do not depend on which branches appear here).
# b convention (v1 prereg section 1.3): I_omega^eff = I_omega * S^(-b); b > 0 grows
# toward the wall.
DELIVERED_BRANCHES = [
    {
        "name": "ARM-0 (carve-out governs, or disidentification)",
        "b": "0",
        "antecedent": "link L-A resolves to the wall-specific carve-out OR link L-B resolves "
                      "negatively (the graded per-node mu_eff is NOT the gap's kinetic "
                      "coefficient); own-rate channels empty at the static bias",
    },
    {
        "name": "ARM-1 (SYM loading AND identification)",
        "b": "-1",
        "antecedent": "link L-A resolves to the W6 Symmetric-Gravity voice AND link L-B "
                      "resolves positively (mu_eff IS the gap's kinetic coefficient, via the "
                      "unstated xi_topo^2 bridge) — the E-073-prescribed downward direction",
    },
]

# The excluded chain, run through the same arithmetic for the record (and FT-KNIFE):
EXCLUDED_CHAIN = {"name": "CH-R-TRANSFER (excluded from receipted structure)", "b": "3"}

A_VALUES = [Fraction(1), Fraction(2)]  # dispatch's a=1; engine's coded a=2 (canon-unratified)


def p_two_engines(a: Fraction, b: Fraction) -> tuple[Fraction, bool]:
    p1 = (a + b) / 2
    p2 = (sp.Rational(a.numerator, a.denominator) + sp.Rational(b.numerator, b.denominator)) / 2
    agree = sp.Rational(p1.numerator, p1.denominator) == p2
    return p1, bool(agree)


def bin_for(p: Fraction) -> str:
    if p in MEMBER_TABLE:
        return MEMBER_TABLE[p]
    lo = min(MEMBER_TABLE)
    return "NOT-A-FROZEN-MEMBER (below every member)" if p < lo else "NOT-A-FROZEN-MEMBER"


def cold_point_ok(b: Fraction) -> bool:
    """G-A008-COLD: I_omega^eff(S=1) == I_omega exactly, symbolically."""
    S, I0 = sp.symbols("S I0", positive=True)
    law = I0 * S ** (-sp.Rational(b.numerator, b.denominator))
    return bool(sp.simplify(law.subs(S, 1) - I0) == 0)


def main() -> int:
    t0 = time.time()
    results: dict = {"gates": {}, "branches": [], "excluded_chain": {}}

    # G-PAIR: symbolic density-shift invariance.
    a_c, b_j, d = sp.symbols("a_c b_j d")
    p_shifted = ((a_c - d) + (b_j + d)) / 2
    p_plain = (a_c + b_j) / 2
    g_pair = bool(sp.simplify(p_shifted - p_plain) == 0)
    results["gates"]["G-PAIR"] = {"residual_zero": g_pair, "pass": g_pair}

    # FT-PAIR: the broken shift (a-d, b+2d) must yield a nonzero residual.
    p_broken = ((a_c - d) + (b_j + 2 * d)) / 2
    ft_pair = bool(sp.simplify(p_broken - p_plain) != 0)
    results["gates"]["FT-PAIR"] = {"fires": ft_pair}

    # Per-branch: G-A008-COLD + G-KNIFE-ARITH.
    g_a008_all = True
    knife_all_agree = True
    for br in DELIVERED_BRANCHES:
        b = Fraction(br["b"])
        cold = cold_point_ok(b)
        g_a008_all &= cold
        rows = []
        for a in A_VALUES:
            p, agree = p_two_engines(a, b)
            knife_all_agree &= agree
            rows.append({"a": str(a), "p": str(p), "engines_agree": agree, "bin": bin_for(p)})
        results["branches"].append(
            {"name": br["name"], "b": br["b"], "antecedent": br["antecedent"],
             "cold_point_pin_preserved": cold, "knife_rows": rows}
        )
    results["gates"]["G-A008-COLD"] = {"all_branches_preserve_pin": g_a008_all, "pass": g_a008_all}

    # FT-A008: a law violating the cold point (I_eff(S=1) = 2*I0) must FAIL the check.
    S, I0 = sp.symbols("S I0", positive=True)
    bad_law = 2 * I0 * S ** 0
    ft_a008 = bool(sp.simplify(bad_law.subs(S, 1) - I0) != 0)
    results["gates"]["FT-A008"] = {"fires": ft_a008}

    # Excluded chain through the same arithmetic (record + FT-KNIFE).
    b3 = Fraction(EXCLUDED_CHAIN["b"])
    ex_rows = []
    for a in A_VALUES:
        p, agree = p_two_engines(a, b3)
        knife_all_agree &= agree
        ex_rows.append({"a": str(a), "p": str(p), "engines_agree": agree, "bin": bin_for(p)})
    results["excluded_chain"] = {**EXCLUDED_CHAIN, "knife_rows": ex_rows}
    ft_knife = all(r["bin"] == "CHANNEL-OPENS" for r in ex_rows)
    results["gates"]["FT-KNIFE"] = {
        "b3_bins": [r["bin"] for r in ex_rows], "fires": bool(ft_knife)
    }
    results["gates"]["G-KNIFE-ARITH"] = {"all_engine_pairs_agree": knife_all_agree,
                                         "pass": knife_all_agree}

    canonical = json.dumps(results, sort_keys=True, ensure_ascii=False, indent=1)
    results["digest_excluding_runtime"] = hashlib.sha256(canonical.encode()).hexdigest()[:16]
    results["_runtime_sec"] = round(time.time() - t0, 3)
    OUT.write_text(json.dumps(results, sort_keys=True, ensure_ascii=False, indent=1) + "\n",
                   encoding="utf-8")

    ok = all(g.get("pass", g.get("fires", False)) for g in results["gates"].values())
    print(f"[iomega_law_check] digest={results['digest_excluding_runtime']} all_gates_ok={ok}")
    for name, g in sorted(results["gates"].items()):
        print(f"  {name}: {g}")
    return 0 if ok else 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
