#!/usr/bin/env python3
"""Number checks for the 2026-08-11 gravity-sector linearity audit (records-class).

Every numeral asserted in `research/2026-08-11_gravity-linearity-audit_result.md` is
recomputed here on TWO independent engines (three where the number is load-bearing):

  ENGINE A  python `math` floats
  ENGINE B  sympy exact / series
  ENGINE C  `decimal.Decimal` at 40 digits (headline delta only)

The lane is READ-ONLY adjudication: nothing here derives new physics. It exists so the
audit's arithmetic can be re-run against the corpus quotes it classifies.

Run:  python3 research/drivers/gravity_linearity_audit_number_check.py
Exit: 0 = all checks green.
"""

from __future__ import annotations

import math
from decimal import Decimal, getcontext

import sympy as sp

getcontext().prec = 40

FAILURES: list[str] = []


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
S_KERNEL = sp.sqrt(1 - A**2)  # eq_axiom_4.tex:7

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

print("\nR8 — the THREE candidate local clocks (result §7)")
C0 = 1 - (1 - e11**2) ** sp.Rational(1, 4)          # kernel  : backreaction.md:128
C1 = 1 - sp.sqrt(1 - NU_VAC * e11)                   # lapse   : temporal-spatial:24 / W2
C2 = 1 - 1 / (1 + NU_VAC * e11)                      # index   : Op19 route, op14 leaf:11
for tag, ex, want_lead in (("R8a kernel omega*sqrt(S)", C0, 2),
                           ("R8b lapse  sqrt(1-r_s/r)", C1, 1),
                           ("R8c index  omega/n", C2, 1)):
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

print("\n" + "=" * 90)
if FAILURES:
    print(f"RESULT: {len(FAILURES)} FAILED -> {FAILURES}")
    raise SystemExit(1)
print("RESULT: all number checks GREEN (engines: math floats / sympy / Decimal p=40)")
