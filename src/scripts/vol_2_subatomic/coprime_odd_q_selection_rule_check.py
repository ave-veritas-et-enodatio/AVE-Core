"""
Lane D-gate — Coprime-Odd-q Stability Selection Rule: validate-on-known check.

Companion to: research/2026-06-23_coprime-odd-q-selection-rule_derivation.md

This is NOT the full enumeration (that is Lane D-full, gated on this gate). It is a
VALIDATE-ON-KNOWN check: the selection rule, stated as three substrate constraints,
MUST recover the known stable assignments before any forward prediction counts.

The rule is the conjunction of three constraints (derivation §3):
  C-α  gcd(p, q) == 1         single-loop closure (integer charge, not a link)
  C-β  p >= 2 and q >= 2      non-trivial winding (a knot, not the unknot)
  C-γ  p == 2                 the Z2 spinor double-cover (FM kink → spin-1/2)

C-γ ∩ C-α  ⟹  q odd  (gcd(2,q)=1 ⟺ q odd). The odd-q rule is a COROLLARY, not a
4th primitive.

Honest scope (per the derivation §6): C-α and C-β are standard knot theory on the
substrate's integer-charge + protection primitives (DERIVED). C-γ's real-space half
(FM double cover) is DERIVED + engine-corroborated; its phase-space↔real-space bridge
(minor winding p = Hopf-fibre wrap ⟹ spinor ⟹ p=2) is plausibility-strong, NOT
theorem-rigorous. This check does NOT re-derive C-γ — it ENCODES the rule and tests
that the encoded rule (a) recovers the knowns and (b) has nontrivial exclusion content.

No CODATA value, no mass, no alpha is read: this is a pure topological selection test
(value-echo immunity). The only import from constants is the canonical crossing-number
ladder, used as the known-stable reference set.
"""

import sys
from math import gcd
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))

from ave.core.constants import TORUS_KNOT_CROSSING_NUMBERS  # canonical odd-q ladder [5,7,9,11,13]


def crossing_number(p: int, q: int) -> int:
    """Torus-knot crossing number c(p,q) = min(p(q-1), q(p-1)); 0 ⟹ unknot."""
    return min(p * (q - 1), q * (p - 1))


# ---- The three substrate constraints (the selection RULE) ----

def c_alpha_single_loop(p: int, q: int) -> bool:
    """C-α: gcd(p,q)=1 — single-component knot, not a d-component link."""
    return gcd(p, q) == 1


def c_beta_nontrivial(p: int, q: int) -> bool:
    """C-β: both windings ≥ 2 — a real knot, not the unknot (c=0)."""
    return p >= 2 and q >= 2


def c_gamma_spinor_doublecover(p: int) -> bool:
    """C-γ: p == 2 — the minimal even minor winding closing the Z2 spinor cover."""
    return p == 2


def is_stable_loop(p: int, q: int) -> bool:
    """A (p,q) phase-space portrait is a STABLE charged-matter loop iff all three hold."""
    return (
        c_alpha_single_loop(p, q)
        and c_beta_nontrivial(p, q)
        and c_gamma_spinor_doublecover(p)
    )


def reason_excluded(p: int, q: int) -> str:
    """First failing constraint, for the audit trail."""
    if not c_gamma_spinor_doublecover(p):
        return f"C-γ FAIL: p={p}≠2 (not the minimal Z2 spinor double-cover)"
    if not c_beta_nontrivial(p, q):
        return f"C-β FAIL: unknot (c={crossing_number(p, q)}=0, a winding is 1)"
    if not c_alpha_single_loop(p, q):
        return f"C-α FAIL: gcd(2,{q})={gcd(p, q)} → {gcd(p, q)}-component LINK, not one loop"
    return "ALLOWED"


def main() -> int:
    print("=" * 74)
    print("Lane D-gate — Coprime-Odd-q Selection Rule: VALIDATE-ON-KNOWN")
    print("=" * 74)

    # ---- P1: recover the known stable set ----
    # Known stable assignments (PHASE-SPACE winding portraits; def-kn0t01):
    #   electron  (2,3)  trefoil   c=3
    #   proton    (2,5)  cinquefoil c=5  (per-loop winding on Borromean N=3 body)
    #   ladder    (2,q)  for q in canonical TORUS_KNOT_CROSSING_NUMBERS
    known_stable = [(2, 3), (2, 5)] + [(2, q) for q in TORUS_KNOT_CROSSING_NUMBERS]
    known_stable = sorted(set(known_stable))

    print("\n[P1] Rule must SELECT every known stable (2,q) portrait:")
    p1_ok = True
    for (p, q) in known_stable:
        ok = is_stable_loop(p, q)
        p1_ok &= ok
        tag = "electron" if (p, q) == (2, 3) else ("proton" if (p, q) == (2, 5) else "baryon ladder")
        print(f"   ({p},{q})  c={crossing_number(p, q):2d}  selected={ok!s:5}  [{tag}]")
    print(f"   => P1 recover-knowns: {'PASS' if p1_ok else 'FAIL'}")

    # ---- P1 (negative): must FORBID the canonical anti-cases ----
    print("\n[P1-neg] Rule must FORBID the known-unstable / non-knot cases:")
    anti = [
        (1, 1, "unknot"),
        (1, 3, "unknot (one winding=1)"),
        (2, 2, "2-component link"),
        (2, 4, "2-component link (no (2,4) knot)"),
        (2, 6, "2-component link"),
        (3, 3, "3-component link"),
    ]
    p1neg_ok = True
    for (p, q, label) in anti:
        forbidden = not is_stable_loop(p, q)
        p1neg_ok &= forbidden
        print(f"   ({p},{q})  forbidden={forbidden!s:5}  [{label}] -> {reason_excluded(p, q)}")
    print(f"   => P1-neg forbid-anti-cases: {'PASS' if p1neg_ok else 'FAIL'}")

    # ---- P4: nontrivial exclusion content beyond 'any coprime knot' ----
    # A naive 'any coprime non-trivial knot is stable' rule would ALSO admit p>=3
    # knots: (3,4),(3,5),(3,7),(4,5),... The C-γ spinor constraint EXCLUDES all of
    # these. Show the rule's predictive teeth: list p>=3 coprime knots it forbids.
    print("\n[P4] Exclusion content — coprime non-trivial knots the rule FORBIDS")
    print("     (these pass a naive 'any coprime knot' rule but FAIL C-γ p=2):")
    forbidden_pge3 = []
    for p in range(3, 7):
        for q in range(p + 1, 12):  # q>p to avoid mirror double-count; both>=2 auto
            if c_alpha_single_loop(p, q) and c_beta_nontrivial(p, q):
                forbidden_pge3.append((p, q, crossing_number(p, q)))
    for (p, q, c) in forbidden_pge3:
        assert not is_stable_loop(p, q), "C-γ must forbid all p>=3 knots"
        print(f"   ({p},{q})  c={c:2d}  FORBIDDEN by C-γ (would-be stable under naive rule)")
    naive_allowed = len(known_stable) + len(forbidden_pge3)
    p4_ok = len(forbidden_pge3) > 0
    print(f"   => naive 'any coprime knot' would admit {naive_allowed} portraits;")
    print(f"      the C-γ spinor rule admits only the {len(known_stable)} p=2 portraits,")
    print(f"      FORBIDDING {len(forbidden_pge3)} coprime knots. P4 has-teeth: "
          f"{'PASS' if p4_ok else 'FAIL'}")

    # ---- Forward continuation (NOT the full enumeration — that is D-full) ----
    print("\n[forward] c>=21 ladder continuation the rule FORCES stable (gate-only):")
    for q in (21, 23, 25):
        ok = is_stable_loop(2, q)
        print(f"   (2,{q})  c={crossing_number(2, q):2d}  selected={ok}  [forced odd-q continuation]")

    verdict = p1_ok and p1neg_ok and p4_ok
    print("\n" + "=" * 74)
    print(f"VALIDATE-ON-KNOWN VERDICT: {'PASS' if verdict else 'FAIL'}")
    print("  P1 recover-knowns      :", "PASS" if p1_ok else "FAIL")
    print("  P1-neg forbid-anti     :", "PASS" if p1neg_ok else "FAIL")
    print("  P4 exclusion-has-teeth :", "PASS" if p4_ok else "FAIL")
    print("=" * 74)
    print("\nScope: this checks the ENCODED rule recovers the knowns + has exclusion")
    print("content. It does NOT re-derive C-γ (the p=2 spinor constraint) — that is the")
    print("derivation doc §3.C-γ + §6 (FORCED-vs-FITTED). The full a-priori enumeration")
    print("of all stable (p,q,N,chirality) is Lane D-full, gated on this gate.")
    return 0 if verdict else 1


if __name__ == "__main__":
    raise SystemExit(main())
