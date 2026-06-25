#!/usr/bin/env python3
"""FORK-A α-flip driver: does the self-biased quiescent-point pressure-equilibrium
FORCE R·r = 1/4 on the (2,3) winding torus WITHOUT α?

Run:  PYTHONPATH=/tmp/forka/src .venv/bin/python \
        src/scripts/forka_alpha_flip/qpoint_pressure_equilibrium.py

Discipline:
  - substrate-native-first (pressure = energy-density = reactive store / volume)
  - no-α-hiding GUARD: trace EVERY dimensionful constant; flag any α (or √α, or
    a ratio that reduces to α) that enters the closing equation.
  - the route-2 trap: a kinematic phasor↔real-space area unit-bridge forces
    R·r → 4π²α (NOT 1/4). We re-state that closed form to show the trap is
    structural, then ask whether the *pressure* route escapes it.

This is a SYMBOLIC/numeric AUDIT, not a fit. It does not "discover" 1/4; it
tests whether the equilibrium *forces* it α-free, or whether 1/4 (or √α)
re-enters. Pure-stdlib + numpy (no sympy dependency).
"""

import math
from fractions import Fraction

# physical α from the corpus closed form (4π³+π²+π); value-level only, for the
# route-2 numeric check — the AUDIT conclusion does not depend on its precision.
ALPHA = 1.0 / (4 * math.pi**3 + math.pi**2 + math.pi)
PHI = (1 + math.sqrt(5)) / 2


def banner(s):
    print("\n" + "=" * 72)
    print(s)
    print("=" * 72)


def step1_geometric_closure():
    """The two α-FREE geometric regimes (a)+(b) from the Golden-Torus leaf.

    regime (a) Nyquist:   d = 1 ell_node              (α-free, Ax-1 cutoff)
    regime (b) crossings: 2(R - r) = d  =>  R - r = 1/2 (α-free, self-avoidance)
    Two unknowns (R,r), ONE equation. The SECOND equation (regime c) is the one
    under audit: is it R·r = 1/4 (α-free) or does α re-enter?
    """
    banner("STEP 1 — the α-FREE geometric regimes (a)+(b)")
    print("regime (a) Nyquist     :  d = 1 ell_node            (α-free: Ax-1 sampling cutoff)")
    print("regime (b) crossing    :  2(R - r) = d => R - r = 1/2 (α-free: self-avoidance)")
    print("\n  => ONE equation in (R,r): R - r = 1/2.  A SECOND equation is required.")
    return Fraction(1, 2)  # R - r


def step2_closing_with_quarter(R_minus_r):
    """IF the second equation is R·r = 1/4, the Golden Torus drops out α-free.
    Solve { R - r = 1/2, R·r = 1/4 } exactly: 2R² - R - 1/2 = 0 => R = (1+√5)/4."""
    banner("STEP 2 — closing with R·r = 1/4 (the INPUT under audit)")
    # R(R - 1/2) = 1/4  ->  2R^2 - R - 1/2 = 0  ->  R = (1 + sqrt5)/4 = phi/2
    R = (1 + math.sqrt(5)) / 4
    r = R - 0.5
    print(f"R = (1+√5)/4 = φ/2 ≈ {R:.6f}")
    print(f"r = R - 1/2  = (φ-1)/2 ≈ {r:.6f}")
    print(f"R/r ≈ {R / r:.6f}   (golden φ = {PHI:.6f})")
    print(f"R·r ≈ {R * r:.6f}   (= 1/4 by construction)")
    print("\n  => Golden Torus. NOTE: this STEP ASSUMES R·r=1/4; it does not")
    print("     derive it. The whole fork is whether the PRESSURE balance forces it.")
    return R, r


def step3_route2_trap():
    """Route-2 kinematic unit-bridge: phasor enclosed area = per-cycle reactive
    energy, identified with a REAL-SPACE area via a kinematic bridge.

    ch8 line 11 reports this closes Class B and forces  R·r -> 4π²α  (NOT 1/4):
    the kinematic bridge ABSORBS α, cannot predict it. Reproduce numerically.
    """
    banner("STEP 3 — the ROUTE-2 TRAP (kinematic unit-bridge ⇒ R·r → 4π²α)")
    rr_route2 = 4 * math.pi**2 * ALPHA
    rr_needed_alpha = 1.0 / (16 * math.pi**2)
    print("phasor enclosed area        A_phasor = π R r")
    print("leaf-reported closed form   R·r      = 4 π² α   (ch8 line 11, route-2)")
    print(f"  4 π² α  at physical α      = {rr_route2:.6f}   vs  1/4 = 0.250000")
    print(f"  => the unit-bridge gives {rr_route2:.4f}, NOT 1/4.")
    print(f"     to FORCE R·r=1/4 you must SET α = 1/(16π²) ≈ {rr_needed_alpha:.6f}")
    print(f"     — but physical α ≈ {ALPHA:.6f}.  The bridge cannot predict α.")
    print("  VERDICT(step3): a kinematic area-bridge is an α-ABSORBER, not an")
    print("                  α-predictor. Confirms ch8 route-2 closed-NEGATIVE.")
    return rr_route2


def step4_pressure_equilibrium():
    """THE FORK ATTEMPT — the longitudinal pressure balance on the winding torus.

    Substrate-native pressure = energy-density (Pa = J/m³). Two-sided balance at
    the self-biased Q-point:
      INSIDE  P_in : confined reactive store (breather virial C<->L energy
                     density) pushing the cage OUTWARD.
      OUTSIDE P_out: cold-vacuum bulk stiffness (K) pushing IN + the tube
                     curvature (Laplace-like) surface term.

    Question: does P_in = P_out close on a SECOND (R,r) relation, and is it
    R·r=1/4 α-free — OR does the energy-density SCALE carry V_yield = √α V_snap
    (the α-echo) into the balance, and does it fix only a SCALE not the PRODUCT?
    """
    banner("STEP 4 — THE PRESSURE-EQUILIBRIUM ATTEMPT (the fork)")

    # The bias ladder (constants.py:451,:460):  V_yield = √α · V_snap.
    # Energy density ~ (1/2) ε0 (V/ell)^2. The winding/CHARGE port self-saturates
    # to V_yield; the MASS port to V_snap. Trace the SCALE ratio of their
    # inside pressures (ε0, ell cancel):
    u_wind_over_u_mass = (math.sqrt(ALPHA)) ** 2  # (V_yield/V_snap)^2 = (√α)^2 = α
    print("inside-pressure SCALE comes from the per-port self-bias:")
    print("   mass-port  field  E_mass = V_snap / ell")
    print("   wind-port  field  E_wind = V_yield/ ell ,  V_yield = √α V_snap")
    print(f"   => u_wind / u_mass = (V_yield/V_snap)^2 = (√α)^2 = α ≈ {u_wind_over_u_mass:.6e}")
    print("   <-- α RE-ENTERS: the winding-port inside pressure is α × mass-port.")

    print("\nthin-tube Laplace balance:  u_wind = γ_surf / r")
    print("   => r = γ_surf / u_wind   — solves for r ALONE (a SCALE).")

    # STRONGEST-VERSION TEST: the FULL torus mean-curvature DOES carry an
    # R-dependent term. Does the full Laplace balance close on the PRODUCT R·r?
    import numpy as np
    R_gt, r_gt = (1 + math.sqrt(5)) / 4, (math.sqrt(5) - 1) / 4
    # <2H> = (1/r)(2 - R/sqrt(R^2 - r^2))  (exact poloidal average of the torus
    # mean curvature; the cos/(R+r cosθ) term does NOT vanish, it gives the
    # second term). Verified numerically against the quadrature below.
    avg2H_analytic = (1 / r_gt) * (2 - R_gt / math.sqrt(R_gt**2 - r_gt**2))
    th = np.linspace(0, 2 * np.pi, 2_000_001)
    twoH = 1.0 / r_gt + np.cos(th) / (R_gt + r_gt * np.cos(th))
    avg2H_numeric = float(np.trapezoid(twoH, th) / (2 * np.pi))
    print("\nFULL torus mean-curvature Laplace balance (strongest version):")
    print("   <2H> = (1/r)(2 - R/√(R²-r²))   [exact poloidal average]")
    print(f"     analytic <2H> at golden torus = {avg2H_analytic:.9f}")
    print(f"     numeric  <2H> (quadrature)    = {avg2H_numeric:.9f}  (match)")
    print("   This is a genuine (R,r) RELATION, but it is NOT R·r = 1/4 and")
    print("   NOT proportional to R·r — it does NOT reproduce the area-product.")
    print("   So even the FULL torus Laplace balance fails to force R·r=1/4.")
    print("   A genuine R·r product needs an AREA identification (πRr = π(d/2)²),")
    print("   which is exactly the route-(c)/route-2 INPUT — NOT a pressure output.")

    banner("STEP 4 — NO-α-HIDING TRACE (every dimensionful constant)")
    rows = [
        ("ε0", "sets pressure UNITS; cancels in the ratio", "α-free"),
        ("ell_node", "Nyquist pitch (Ax-1)", "α-free"),
        ("V_snap = m_e c²/e", "MASS scale (value-level)", "α-free"),
        ("V_yield = √α·V_snap", "CHARGE/winding bias (INVARIANT-C1, constants.py:460)", "CARRIES α"),
        ("K_bulk = √2 ρ c0", "outside stiffness at K=2G (ν=2/7 GR-import)", "α-free (separate echo)"),
        ("γ_surf", "line/surface tension; SCALE rides V_yield", "α-laden if winding-port"),
    ]
    for name, role, tag in rows:
        print(f"  {name:22s} {role:48s} -> {tag}")
    print("\n RESULT: the winding-port pressure scale is α × (mass-port pressure),")
    print("         so any equilibrium using the winding-port bias INHERITS α.")
    print("         The balance fixes a SCALE (r or R), not the PRODUCT R·r;")
    print("         the product still needs the area-identification INPUT.")
    return u_wind_over_u_mass


def step5_forkguard():
    banner("STEP 5 — FORK-2 GUARD vs S3 H_couple")
    print("S3 H_couple (device-circuit-models.md:201,:203,:207, PR #321) is the")
    print("conservative bulk<->shear skew-Hermitian circulator coupling:")
    print("  - norm-conserved to 1.1e-12 / 40k steps (NO pump)")
    print("  - transfers 100% bulk->shear (it SLOSHES), NOT isolation, NOT inert")
    print("  - non-reciprocity MAGNITUDE is IMPOSED (echo); only the FORM is α-free")
    print()
    print("What is PHYSICALLY DIFFERENT in the pressure-equilibrium fork?")
    print("  The pressure balance is ALSO a conservative reactive store (Ax-3")
    print("  lossless): inside push = outside push at the parked Q-point — NO net")
    print("  work, NO pump. Same energetic character as H_couple's slosh. It moves")
    print("  energy C<->L (virial) and in<->out (cage), but originates NO new")
    print("  dimensionless number: its only SCALE is the bias ladder, whose ratio")
    print("  IS √α.")
    print()
    print("  => Nothing PHYSICAL differs from H_couple's conservative slosh. The")
    print("     'pressure-equilibrium sets R·r=1/4' framing is a RELABEL of the")
    print("     same conservative virial balance + the SAME area-identification")
    print("     INPUT. It adds no force that selects the PRODUCT R·r. Chord BARRED.")


if __name__ == "__main__":
    rmr = step1_geometric_closure()
    step2_closing_with_quarter(rmr)
    step3_route2_trap()
    step4_pressure_equilibrium()
    step5_forkguard()
    banner("OVERALL")
    print("R·r=1/4 is NOT forced α-free by the Q-point pressure-equilibrium.")
    print(" - regimes (a)+(b) give R-r=1/2 α-free (ONE equation).")
    print(" - the SECOND equation (the PRODUCT R·r) still needs the phasor-area")
    print("   = Nyquist-cell-area IDENTIFICATION (Class-B INPUT), unchanged.")
    print(" - the pressure route fixes a SCALE (r or R), not the product; and")
    print("   where it uses the winding-port bias it INHERITS √α (route-2-class).")
    print(" - FORK-2: physically identical to H_couple's conservative slosh =>")
    print("   RELABEL, chord BARRED.")
    print("\nVERDICT: ECHO (α re-enters via the √α bias ladder; the product needs")
    print("         the area-INPUT). The charge stays the 4th echo.")
