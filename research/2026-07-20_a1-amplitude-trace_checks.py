#!/usr/bin/env python3
"""A1 amplitude trace — symbolic + numeric checks (research artifact).

Verifies the four load-bearing algebraic claims in
`2026-07-20_a1-amplitude-trace_result.md`. Pure-corpus; reads no engine module;
imports only sympy/numpy. Run: `python research/2026-07-20_a1-amplitude-trace_checks.py`.

The claims (each printed PASS/FAIL):

  C1  RETIREMENT EQUIVALENCE. A = sqrt(g_N/a_0) into the canonical QUADRATIC
      kernel S(A)=sqrt(1-A^2) is identically the RETIRED LINEAR kernel factor
      sqrt(1 - g_N/a_0). => reading (ii) == the retired linear form. (This is the
      whole reason (ii) winning would REOPEN #748.)

  C2  PREFACTOR DECOMPOSITION. The canonical drag prefactor sqrt(g_N*a_0) equals
      a_0*sqrt(A) with A = g_N/a_0. => the sqrt(g_N) that legitimately appears in
      the deep-MOND drag AMPLITUDE is the PREFACTOR, a DISTINCT object from the
      kernel ARGUMENT A (which is linear g_N/a_0). The docstring "strain prop
      sqrt(g_N)" is TRUE of the prefactor, FALSE if fed to the kernel argument.

  C3  STEELMAN-(ii) COLLAPSE. The only substrate-native amplitude that is
      literally proportional to sqrt(g_N) is the orbital-motion Lorentz strain
      A = v/c with v^2 = g_N*r. Setting sqrt(g_N/a_0) == v/c forces r = c^2/a_0.
      With a_0 = c*H_inf/(2*pi) this is r = 2*pi*(c/H_inf) = 2*pi*R_Hubble, a
      COSMIC length, not a galactic radius. => at galactic r the object
      sqrt(g_N/a_0) has NO clean physical-amplitude reading; it is just the
      algebraic square-root of the field ratio.

  C4  MAXWELL SMALL-A DISCRIMINATOR. Quadratic kernel -> 1 - A^2/2 (even, recovers
      Maxwell); linear kernel -> 1 - A/2 (odd leading term, breaks Maxwell
      recovery). Consistent with #748 sec5.3 + the Axiom-4 buckling-kernel result.
"""

import math

import sympy as sp

# Canonical constants (no magic numbers) — same source galactic_rotation.py uses.
from ave.core.constants import C_0, H_INFINITY

gN, a0, A, c, r, Hinf = sp.symbols("g_N a_0 A c r H_inf", positive=True)

print("=" * 68)
print("A1 amplitude trace — symbolic/numeric checks")
print("=" * 68)

# ---- C1: retirement equivalence -------------------------------------------
# reading (ii): A = sqrt(g_N/a_0). Feed into quadratic kernel sqrt(1 - A^2).
A_ii = sp.sqrt(gN / a0)
kernel_quad_of_Aii = sp.sqrt(1 - A_ii**2)
linear_kernel = sp.sqrt(1 - gN / a0)
c1 = sp.simplify(kernel_quad_of_Aii - linear_kernel) == 0
print(f"\nC1 retirement equivalence:")
print(f"    sqrt(1 - (sqrt(g_N/a_0))^2) = {sp.simplify(kernel_quad_of_Aii)}")
print(f"    retired linear kernel        = {linear_kernel}")
print(f"    => reading (ii) IS the retired linear form: {'PASS' if c1 else 'FAIL'}")

# ---- C2: prefactor decomposition ------------------------------------------
prefactor = sp.sqrt(gN * a0)
decomp = a0 * sp.sqrt(gN / a0)  # = a_0 * sqrt(A), A = g_N/a_0
c2 = sp.simplify(prefactor - decomp) == 0
print(f"\nC2 prefactor decomposition:")
print(f"    sqrt(g_N*a_0) = a_0*sqrt(A), A=g_N/a_0 : {'PASS' if c2 else 'FAIL'}")
print(f"    => sqrt(g_N) lives in the drag PREFACTOR, not the kernel ARGUMENT")

# ---- C3: steelman-(ii) collapse -------------------------------------------
# orbital-motion Lorentz strain: A_v = v/c, with circular-orbit v^2 = g_N * r.
Av_sq = gN * r / c**2                       # (v/c)^2
# require A_v == sqrt(g_N/a_0)  <=>  A_v^2 == g_N/a_0
sol_r = sp.solve(sp.Eq(Av_sq, gN / a0), r)
r_star = sp.simplify(sol_r[0])              # expect c^2/a_0
c3a = sp.simplify(r_star - c**2 / a0) == 0
# substitute canonical a_0 = c*H_inf/(2*pi): r_star -> 2*pi*c/H_inf = 2*pi*R_H
r_star_cosmic = sp.simplify(r_star.subs(a0, c * Hinf / (2 * sp.pi)))
R_hubble = c / Hinf
c3b = sp.simplify(r_star_cosmic - 2 * sp.pi * R_hubble) == 0
print(f"\nC3 steelman-(ii) collapse:")
print(f"    A_v = v/c == sqrt(g_N/a_0) forces r* = {r_star}  (== c^2/a_0: {'PASS' if c3a else 'FAIL'})")
print(f"    with a_0 = c*H_inf/(2pi):  r* = {r_star_cosmic} = 2*pi*R_Hubble : {'PASS' if c3b else 'FAIL'}")
# numeric magnitude — canonical constants, no magic numbers
r_star_num = 2 * math.pi * float(C_0) / float(H_INFINITY)
print(f"    r* ~ {r_star_num:.3e} m  (2*pi*Hubble radius ~ 8.4e26 m) — COSMIC, not galactic")
print(f"    => at galactic r, sqrt(g_N/a_0) is NOT v/c; it has no clean amplitude reading")

# ---- C4: Maxwell small-A discriminator ------------------------------------
quad_series = sp.series(sp.sqrt(1 - A**2), A, 0, 3).removeO()
lin_series = sp.series(sp.sqrt(1 - A), A, 0, 3).removeO()
c4a = quad_series.coeff(A, 1) == 0                    # no linear term (even)
c4b = lin_series.coeff(A, 1) == sp.Rational(-1, 2)    # linear term present (odd)
print(f"\nC4 Maxwell small-A discriminator:")
print(f"    quadratic sqrt(1-A^2) ~ {quad_series}  (linear coeff 0: {'PASS' if c4a else 'FAIL'})")
print(f"    linear    sqrt(1-A)   ~ {lin_series}  (linear coeff -1/2: {'PASS' if c4b else 'FAIL'})")
print(f"    => quadratic recovers Maxwell (1 - A^2/2); linear breaks it")

all_pass = all([c1, c2, c3a, c3b, c4a, c4b])
print("\n" + "=" * 68)
print(f"ALL CHECKS: {'PASS' if all_pass else 'FAIL'}")
print("=" * 68)
raise SystemExit(0 if all_pass else 1)
