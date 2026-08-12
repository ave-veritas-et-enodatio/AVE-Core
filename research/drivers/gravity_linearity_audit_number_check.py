#!/usr/bin/env python3
"""Number checks for the 2026-08-11 gravity-sector linearity audit (records-class).

Every numeral asserted in `research/2026-08-11_gravity-linearity-audit_result.md` is
recomputed here on TWO independent engines (three where the number is load-bearing):

  ENGINE A  python `math` floats
  ENGINE B  sympy exact / series
  ENGINE C  `decimal.Decimal` at 40 digits (headline delta only)

The lane is READ-ONLY adjudication: nothing here derives new physics. It exists so the
audit's arithmetic can be re-run against the corpus quotes it classifies.

Run:   python3 research/drivers/gravity_linearity_audit_number_check.py
Exit:  0 = all checks green.

Mutation receipt (proves the kernel-dependent legs can actually FAIL):
       python3 research/drivers/gravity_linearity_audit_number_check.py --mutation-receipt
mutates the Axiom-4 kernel exponent (`1-A**2` -> `1-A**3`) and requires every detector in
`MUTATION_DETECTORS` to trip. Exit 0 = all tripped (receipt satisfied); non-zero names the
detectors that stayed green under a mutated kernel, i.e. are NOT actually coupled to it.
This driver writes no tracked artifact, so a mutated run cannot dirty the tree.

⚑ Added 2026-08-11 after the independent §1-§8 review found R8a hard-coded the kernel: a
hand-run kernel mutation did NOT trip it. R8's C0 is now derived from `S_KERNEL`.
"""

from __future__ import annotations

import math
import sys
from decimal import Decimal, getcontext

import sympy as sp

getcontext().prec = 40

FAILURES: list[str] = []

MUTATE = "--mutation-receipt" in sys.argv
# Detectors that MUST trip when the Ax4 kernel is mutated. Any that stays green is not
# genuinely coupled to the kernel and is therefore not a receipt for a kernel claim.
MUTATION_DETECTORS = (
    "R1a kernel  sqrt(S(A)) series",
    "R6a n = 1/sqrt(S) series",
    "R8a kernel omega*sqrt(S)",
)


def check(tag: str, got: float, want: float, rtol: float, note: str = "") -> None:
    ok = abs(got - want) <= rtol * abs(want) if want else abs(got) <= rtol
    status = "PASS" if ok else "FAIL"
    print(f"  [{status}] {tag:<44s} got={got!r:>26s} want={want!r:>14s}  {note}")
    if not ok:
        FAILURES.append(tag)


def check_expr(tag: str, got, want, note: str = "") -> None:
    ok = sp.simplify(got - want) == 0
    status = "PASS" if ok else "FAIL"
    print(f"  [{status}] {tag:<44s} {got}  ==  {want}   {note}")
    if not ok:
        FAILURES.append(tag)


# --------------------------------------------------------------------------------------
A = sp.symbols("A", positive=True)
e11 = sp.symbols("varepsilon_11", positive=True)
NU_VAC = sp.Rational(2, 7)
NU_SCALAR = sp.Rational(1, 7)  # site 15: the 1/7 Lagrangian isotropic projection
# eq_axiom_4.tex:7. Every kernel-dependent leg below MUST read this symbol, never a
# re-typed literal — that is what makes the mutation receipt meaningful.
S_KERNEL = sp.sqrt(1 - A**3) if MUTATE else sp.sqrt(1 - A**2)
if MUTATE:
    print("\n⚑ MUTATION RECEIPT RUN — Ax4 kernel mutated to sqrt(1 - A**3).")
    print(f"   Detectors required to trip: {len(MUTATION_DETECTORS)}")

print("\nR1 — the two functions written '√S' (result §3.2, §7)")
kern = sp.series(sp.sqrt(S_KERNEL), A, 0, 3).removeO()
laps = sp.series(sp.sqrt(1 - A), A, 0, 3).removeO()
check_expr("R1a kernel  sqrt(S(A)) series", kern, 1 - A**2 / 4)
check_expr("R1b lapse   sqrt(1-A) series", laps, 1 - A / 2 - A**2 / 8)
check("R1c d/dA sqrt(S) at 0", float(sp.diff(sp.sqrt(S_KERNEL), A).subs(A, 0)), 0.0, 0,
      "kernel is FLAT at the origin")
check("R1d d/dA sqrt(1-A) at 0", float(sp.diff(sp.sqrt(1 - A), A).subs(A, 0)), -0.5, 1e-15,
      "lapse has slope -1/2")

print("\nR2 — #951 lemma, widened: any C1 f(S) has zero A-slope at the origin")
f = sp.Function("f")
check("R2  d/dA f(S(A)) at A=0", float(sp.diff(f(S_KERNEL), A).subs(A, 0)), 0.0, 0,
      "independent re-derivation of the merged #951 lemma")

print("\nR3 — the nu_vac = 2/7 gap between the two strain measures (result §3.3)")
check("R3a (r_s/r) / eps11", float(NU_VAC), 2 / 7, 1e-15, "r_s/r = nu_vac * eps11")
check("R3b r_sat / r_s", float(1 / NU_VAC), 3.5, 1e-15, "eps11=1 at 3.5 r_s, NOT at r_s")
check("R3c eps11 at r = r_s", float(1 / NU_VAC), 3.5, 1e-15,
      "so eq_axiom_4.tex:24's 'eps11=1 at r_s' is off by 3.5x")

print("\nR4 — Sirius B, white-dwarf leaf :27/:44/:51/:56/:66/:67/:70 (result §5)")
# Canonical source: never hard-code. `ave.core.constants` is the single source of truth.
from ave.core.constants import C_0 as c, G, M_SUN as MSUN  # noqa: E402

# Sirius B M/R and the solar radius are the LEAF's own inputs, not substrate constants:
# M/M_sun = 1.018 and R = 5800 km are quoted from white-dwarf-gravitational-predictions.md:32;
# R_SUN is an astronomical datum with no canonical entry -> declared ENG-CHOICE at use site.
R_SUN = 6.957e8  # m — IAU nominal solar radius (ENG-CHOICE; used only by R7's limb amplitude)
M, R = 1.018 * MSUN, 5800e3
phi = G * M / (c**2 * R)
eps = 7 * phi
rs_r = 2 * phi
z_gr = 1 / math.sqrt(1 - 2 * phi) - 1


def delta_v(a: float) -> float:
    """delta-v [km/s] for kernel argument `a`, exact (no series truncation)."""
    return c * (1 / (math.sqrt(1 - 2 * phi) * math.sqrt(1 - a**2)) - 1 / math.sqrt(1 - 2 * phi)) / 1e3


check("R4a eps11(Sirius B)  [leaf :32]", round(eps, 6), 0.001815, 3e-3, "leaf prints 1.81e-3")
check("R4b v_GR km/s        [leaf :66]", round(c * z_gr / 1e3, 2), 77.75, 1e-3, "leaf prints 77.75")
dv_eps = delta_v(eps)
dv_rsr = delta_v(rs_r)
dv_leaf_formula = c * z_gr * (1 / math.sqrt(1 - eps**2) - 1) / 1e3
check("R4c delta_v at A=eps11 (leaf's own :27)", round(dv_eps, 6), 0.493785, 1e-6)
check("R4d delta_v at A=r_s/r (eq_axiom_4:10)", round(dv_rsr, 6), 0.040309, 1e-6)
check("R4e delta_v from :56 as written", round(dv_leaf_formula, 9), 0.000128, 5e-3)
check("R4f F-2 dropped factor (1+z)/z", round((1 + z_gr) / z_gr, 1), 3856.8, 1e-4)
check("R4g F-4 table 0.05 vs r_s/r reading", round(0.05 / dv_rsr, 3), 1.240, 1e-3,
      "~24% apart")
check("R4h F-4 table 0.05 vs eps11 reading", round(dv_eps / 0.05, 2), 9.88, 1e-3,
      "~10x apart")
check("R4i kernel term as %% of (obs-GR) residual", round(100 * dv_eps / 2.90, 1), 17.0, 2e-2,
      "leaf :68 residual = +2.90 km/s")

# ENGINE C — Decimal cross-check on the headline delta
D = Decimal
phiD = D(G) * D(M) / (D(c) ** 2 * D(R))
epsD = 7 * phiD
one = D(1)
zC = one / (one - 2 * phiD).sqrt() - one
zAC = one / ((one - 2 * phiD).sqrt() * (one - epsD**2).sqrt()) - one
check("R4j ENGINE C (Decimal p=40) delta_v", round(float(D(c) * (zAC - zC) / D(1000)), 6),
      0.493785, 1e-6, "3rd engine agrees with R4c")

print("\nR5 — white-dwarf :44 (slope 2) vs :51 (slope 1) (result §5, F-1)")
p = sp.symbols("p", positive=True)  # p = GM/c^2 R
check_expr("R5a :44  1/(1+2p) - 1", sp.series(1 / (1 + 2 * p) - 1, p, 0, 2).removeO(), -2 * p)
check_expr("R5b :51  1/sqrt(1-2p) - 1", sp.series(1 / sp.sqrt(1 - 2 * p) - 1, p, 0, 2).removeO(), p)

print("\nR6 — site 9: n = 1/sqrt(S) is quadratic at EVERY normalization (result §3.2)")
check_expr("R6a n = 1/sqrt(S) series", sp.series(1 / sp.sqrt(S_KERNEL), A, 0, 3).removeO(),
           1 + A**2 / 4)
for name, sub in (("A=eps11", e11), ("A=(2/7)eps11", NU_VAC * e11)):
    lead = sp.series((1 / sp.sqrt(S_KERNEL)).subs(A, sub) - 1, e11, 0, 3).removeO()
    deg = sp.Poly(sp.expand(lead), e11).monoms()[-1][0]
    ok = deg == 2
    print(f"  [{'PASS' if ok else 'FAIL'}] R6 {name:<40s} leading power of eps11 = {deg}  ({lead})")
    if not ok:
        FAILURES.append(f"R6 {name}")

print("\nR7 — anisotropy-scoping :893 fixes A == eps11 numerically (result §1)")
A_limb = 7 * G * MSUN / (c**2 * R_SUN)
check("R7a 7GM/c^2 R_sun", round(A_limb, 9), 1.486e-5, 4e-4, "scoping :893 prints 1.486e-5")
check("R7b A^2 at the limb", round(A_limb**2, 13), 2.21e-10, 5e-3, "scoping :893 prints 2.21e-10")

print("\nR8 — the FOUR candidate local clocks (result §7; 4th row added 2026-08-11, B-1c)")
# ⚑ C0 is DERIVED FROM S_KERNEL (was hard-coded until 2026-08-11 — see module docstring).
C0 = 1 - sp.sqrt(S_KERNEL).subs(A, e11)              # kernel  : backreaction.md:128
C1 = 1 - sp.sqrt(1 - NU_VAC * e11)                   # lapse   : temporal-spatial:24 / W2
C2 = 1 - 1 / (1 + NU_VAC * e11)                      # index   : Op19 route, op14 leaf:11
C3 = 1 - 1 / (1 + NU_SCALAR * e11)                   # substrate-side matter : site 15 :14,:19
for tag, ex, want_lead in (("R8a kernel omega*sqrt(S)", C0, 2),
                           ("R8b lapse  sqrt(1-r_s/r)", C1, 1),
                           ("R8c index  omega/n", C2, 1),
                           ("R8g substrate-side omega/n_scalar", C3, 1)):
    lead = sp.series(ex, e11, 0, 3).removeO()
    deg = sp.Poly(sp.expand(lead), e11).monoms()[-1][0]
    ok = deg == want_lead
    print(f"  [{'PASS' if ok else 'FAIL'}] {tag:<44s} leading power = {deg}  ({sp.nsimplify(lead)})")
    if not ok:
        FAILURES.append(tag)
check_expr("R8d lapse leading term", sp.series(C1, e11, 0, 2).removeO(), e11 / 7)
check_expr("R8e index leading term", sp.series(C2, e11, 0, 2).removeO(), 2 * e11 / 7)
check("R8f kernel/lapse ratio at Sirius B", round(float(C0.subs(e11, eps) / C1.subs(e11, eps)), 6),
      0.003175, 1e-3, "kernel clock is 0.3% of the lapse clock — it cannot be the leading law")

print("\nR9 — operating-offset slope is nonzero for A0 != 0 (result §4.3; STRUCTURE ONLY)")
A0 = sp.symbols("A_0", positive=True)
W = (1 - A**2) ** sp.Rational(1, 4)
dlnW = sp.simplify(sp.diff(W, A) / W).subs(A, A0)
check_expr("R9a dlnW/dA at A0", sp.simplify(dlnW), A0 / (2 * (A0**2 - 1)))
check_expr("R9b small-A0 limit", sp.series(dlnW, A0, 0, 2).removeO(), -A0 / 2)
print("       (no A0 VALUE is proposed — that is the pre-tension lane's charter)")

# ======================================================================================
# §9 ADDENDUM LEGS (⚑ UN-AUDITED candidate — see result doc §9). These recompute the
# chat-walk algebra so it can be attacked; they assert nothing about which reading is
# correct. R11's `f(S)` exponent is the pre-existing VACATED Op16 question, NOT settled
# here — `sqrt(S)` below is the "clock rides c_shear" reading, written to be refutable.
# ======================================================================================
Lsym, Csym, msym, Ssym = sp.symbols("L C m S", positive=True)
w_base = 1 / sp.sqrt(Lsym * Csym)
Z_base = sp.sqrt(Lsym / Csym)

print("\nR10 — §9.1 co-scaling: hold the RATIO, pump the PRODUCT")
w_co = 1 / sp.sqrt(msym * Lsym * msym * Csym)
Z_co = sp.sqrt(msym * Lsym / (msym * Csym))
check_expr("R10a co-scaled omega ratio", sp.simplify(w_co / w_base), 1 / msym)
check_expr("R10b co-scaled Z ratio", sp.simplify(Z_co / Z_base), sp.Integer(1))
check_expr("R10c m that gives the OBSERVED slope-1 z",
           sp.series((1 - NU_VAC * e11) ** sp.Rational(-1, 2), e11, 0, 2).removeO(), 1 + e11 / 7)
check_expr("R10d m^2 == n_temporal (slope 2)",
           sp.expand(sp.series((1 + e11 / 7) ** 2, e11, 0, 2).removeO()), 1 + 2 * e11 / 7)
print("       => W2's bridge z = (n_t - 1)/2 falls out of m vs m^2, not stipulated")

print("\nR11 — §9.2 bond-break: runaway compliance at fixed fabric (C -> C/S)")
w_bb = 1 / sp.sqrt(Lsym * Csym / Ssym)
Z_bb = sp.sqrt(Lsym * Ssym / Csym)
check_expr("R11a bond-break omega ratio", sp.simplify(w_bb / w_base), sp.sqrt(Ssym))
check_expr("R11b bond-break Z ratio", sp.simplify(Z_bb / Z_base), sp.sqrt(Ssym))
check("R11c Gamma as S->0", float(sp.limit((Z_bb - Z_base) / (Z_bb + Z_base), Ssym, 0)), -1.0,
      1e-12, "inverting wall (SHORT), two-element tank")
# ORTHOGONALITY — the load-bearing claim. Z must be blind to m and sensitive to S.
check("R11d dlnZ/dm  (co-scaling)", float(sp.diff(sp.log(Z_co), msym).subs(msym, 1)), 0.0, 0,
      "Z is BLIND to co-scaling")
ok_S = sp.simplify(sp.diff(sp.log(Z_bb), Ssym)) != 0
print(f"  [{'PASS' if ok_S else 'FAIL'}] R11e dlnZ/dS  (bond-break)"
      f"{'':<20s} = {sp.simplify(sp.diff(sp.log(Z_bb), Ssym))}  -> Z is SENSITIVE to bond-break")
if not ok_S:
    FAILURES.append("R11e")

print("\nR12 — §9.2 the two failures arrive at DIFFERENT radii in DIFFERENT quantities")
for label, r_over_rs in (("r_sat = 3.5 r_s", 3.5), ("r_s", 1.0)):
    rs_r = 1.0 / r_over_rs
    e_here = 3.5 * rs_r
    m_here = 1 / math.sqrt(1 - rs_r) if rs_r < 1 else float("inf")
    s_here = math.sqrt(1 - e_here**2) if e_here <= 1 else float("nan")
    print(f"       {label:<16s} eps11={e_here:<6.3f} m={m_here:<8.3f} S={s_here:.3f}")
check("R12a m at the shear wall r_sat", round(1 / math.sqrt(1 - 1 / 3.5), 3), 1.183, 1e-3,
      "tank detuned only 18% where the springs are already gone")
check("R12b S at the shear wall r_sat", round(math.sqrt(max(0.0, 1 - 1.0**2)), 6), 0.0, 0,
      "bond-break arrives FIRST, and from OUTSIDE (r_sat = 3.5 r_s)")

print("\nR13 — §2 site 15: the substrate-side clock AGREES with the lapse at leading order")
print("      but is a DISTINCT FUNCTION (they part at O(eps11^2)) — result §7 fourth row")
check_expr("R13a site-15 leading term == eps11/7",
           sp.series(C3, e11, 0, 2).removeO(), e11 / 7)
check_expr("R13b lapse leading term == eps11/7",
           sp.series(C1, e11, 0, 2).removeO(), e11 / 7)
d2 = sp.simplify(sp.series(C3 - C1, e11, 0, 3).removeO())
ok13 = d2 != 0
print(f"  [{'PASS' if ok13 else 'FAIL'}] R13c they DIFFER at second order"
      f"{'':<14s} C3 - C1 = {d2}  -> distinct clocks, not one clock twice")
if not ok13:
    FAILURES.append("R13c")
check_expr("R13d site-15 U_wave = m c^2 - GMm/r  (leaf :19)",
           sp.series(1 / (1 + NU_SCALAR * e11), e11, 0, 2).removeO(), 1 - e11 / 7)

print("\n" + "=" * 90)
if MUTATE:
    # An EMPTY detector tuple would pass vacuously ("all 0 detectors tripped", exit 0) —
    # exactly the shape the repo's own verify-lane-number-checks refuses. Gate it.
    if not MUTATION_DETECTORS:
        print("MUTATION RECEIPT INVALID: MUTATION_DETECTORS is empty — a vacuous pass.")
        raise SystemExit(1)
    # Receipt inverted: under a mutated kernel the named detectors MUST have failed.
    missed = [d for d in MUTATION_DETECTORS if d not in FAILURES]
    for d in MUTATION_DETECTORS:
        print(f"  [{'TRIPPED' if d not in missed else 'MISSED '}] {d}")
    if missed:
        print(f"\nMUTATION RECEIPT FAILED: {len(missed)} detector(s) NOT coupled to the kernel "
              f"-> {missed}")
        raise SystemExit(1)
    print(f"\nMUTATION RECEIPT SATISFIED: all {len(MUTATION_DETECTORS)} kernel detectors tripped.")
    raise SystemExit(0)
if FAILURES:
    print(f"RESULT: {len(FAILURES)} FAILED -> {FAILURES}")
    raise SystemExit(1)
print("RESULT: all number checks GREEN (engines: math floats / sympy / Decimal p=40)")
