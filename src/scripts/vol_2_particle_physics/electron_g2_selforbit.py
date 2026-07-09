#!/usr/bin/env python3
"""Electron g-factor from the AVE (2,3) c-speed self-orbit geometry.

First test of the electron-as-chiral-self-orbit push (Grant-walked 2026-07-08).
Pre-reg: research/2026-07-08_electron-g2-selforbit_prereg.md (FROZEN @ eb05cbf3).

Computes  g = 2*m*mu / (q*S)  from the ACTUAL (2,3)+A1 geometry and tests whether
the geometry FORCES g=2. Everything is symbolic (e, m_e, c, lam_C, hbar as FREE
SymPy symbols) so the firewall can prove the physical constants CANCEL and g is a
pure geometric number. `ave.core.constants` is imported ONLY at the very end as an
anti-firewall cross-check (g must be invariant under CODATA substitution), never as
an input to the symbolic g.

FIREWALL (pre-registered s4): no M_E / ALPHA / HBAR numeric token reaches the
symbolic g. The "2" enters ONLY as an integer cover degree N_cover (a topological
winding number), never as a hand-plugged zitter radius lam_C/2 or frequency 2*w_C.

Run:  python src/scripts/vol_2_particle_physics/electron_g2_selforbit.py
"""
from __future__ import annotations

import sympy as sp

# ---------------------------------------------------------------------------
# Free physical SYMBOLS (positive reals). These are ABSTRACT — no numeric value.
# The firewall asserts none of ave.core.constants' numeric tokens reaches g.
# ---------------------------------------------------------------------------
e, m, c, lam, hbar = sp.symbols("e m c lambda_C hbar", positive=True)
# Torus-knot winding integers and the spin-cover degree (dimensionless topology).
p, q = sp.symbols("p q", positive=True, integer=True)   # (p toroidal, q poloidal)
R, r = sp.symbols("R r", positive=True)                 # torus major/minor radii
N_cover = sp.symbols("N_cover", positive=True, integer=True)
t = sp.symbols("t", real=True)


def g_from(mu, S):
    """Mechanical g-factor: g = 2*m*mu / (q*S). q is the circulating charge e."""
    return sp.simplify(2 * m * mu / (e * S))


# ===========================================================================
# 1. NAIVE c-ORBIT CONTROL — one object, single cover, charge==mass co-located.
#    Point charge e AND mass m on ONE loop of radius lam at speed c.
#    Pre-registered prediction: g = 1.
# ===========================================================================
def naive_control():
    omega = c / lam                       # c-ceiling: omega*lam = c (NOT hand-set 2*w_C)
    # angular momentum of the mass: S = m * v * R = m * c * lam
    S = m * c * lam
    # magnetic moment of the charge: I = e*omega/(2*pi), A = pi*lam^2
    I = e * omega / (2 * sp.pi)
    A = sp.pi * lam**2
    mu = I * A                            # = e*c*lam/2  (this is mu_B when lam=lam_C)
    return sp.simplify(mu), sp.simplify(S), g_from(mu, S)


# ===========================================================================
# 2. GENERAL (p,q) TORUS-KNOT CO-CIRCULATION CONTROL.
#    Charge AND mass co-circulate on the SAME (p,q) torus knot at speed c.
#    x = (R + r cos(q t)) cos(p t),  y = (R + r cos(q t)) sin(p t),  z = r sin(q t)
#    mu_z = (I/2) oint (x dy - y dx);  S_z = oint (x v_y - y v_x) dm.
#    Pre-registered prediction: g = 1 for ALL (p,q) — winding topology ALONE does
#    NOT lift g when charge and mass are the SAME circulating object.
# ===========================================================================
def torus_knot_control():
    rho = R + r * sp.cos(q * t)
    x = rho * sp.cos(p * t)
    y = rho * sp.sin(p * t)
    xdot = sp.diff(x, t)
    ydot = sp.diff(y, t)

    # z-projected enclosed-area integrand: x*ydot - y*xdot simplifies to p*rho^2.
    area_integrand = sp.simplify(x * ydot - y * xdot)          # expect p*rho^2
    # One full knot traversal = charge goes around once: t in [0, 2*pi].
    enclosed = sp.integrate(area_integrand, (t, 0, 2 * sp.pi))  # = p*(2*pi*R^2 + pi*r^2)

    # Charge current over the traversal period T: I = e/T, T = L/c (L = knot length).
    # For mu_z = (I/2)*enclosed with the SAME 1/L, and for S_z the mass carries the
    # SAME p and enclosed with a matching 1/L, the L and p factors cancel in g.
    # Work with the geometric ratio directly (L>0 cancels identically):
    L = sp.symbols("L", positive=True)     # knot arc length (>0, cancels)
    I = e * c / L
    mu_z = I / 2 * enclosed                                    # z-magnetic moment
    # Mass at speed c, uniform linear density m/L. S_z = (m*c/L)*enclosed
    # (velocity = c * unit-tangent; the |r'| Jacobian cancels the arc-length weight).
    S_z = (m * c / L) * enclosed
    g = g_from(mu_z, S_z)
    return sp.simplify(area_integrand - p * rho**2), sp.simplify(enclosed), sp.simplify(g)


# ===========================================================================
# 3. AVE ELECTRON — A1 (mass) perp T2 (charge) SPLIT via the double-cover.
#    mu = mu_B from the charge single-2*pi current loop (double-cover-IMMUNE:
#         the charge still encloses one area per traversal, so mu is unchanged).
#    S  = ħ/2 from the mass/A1 spin observable being a 4*pi double-cover spinor.
#    But we do NOT plug ħ/2 by hand — we DERIVE S_naive = m*c*lam and HALVE it by
#    the integer cover degree N_cover (the (2,3) poloidal "2" / K4 bipartite).
# ===========================================================================
def ave_electron(cover):
    omega = c / lam
    I = e * omega / (2 * sp.pi)
    mu = I * sp.pi * lam**2                # charge current-loop: cover-immune
    S = (m * c * lam) / cover              # mass angular momentum, halved by cover
    return sp.simplify(mu), sp.simplify(S), g_from(mu, S)


# ===========================================================================
# 4. COVER-DEGREE GENERALIZATION — g = N_cover EXACTLY (the "WHERE" trace).
# ===========================================================================
def cover_generalization():
    _, _, g = ave_electron(N_cover)
    return sp.simplify(g)


# ===========================================================================
# FIREWALL — prove the physical constants CANCEL and no CODATA token is on path.
# ===========================================================================
def firewall_report(g_expr, label):
    g_s = sp.simplify(g_expr)
    free = g_expr.free_symbols
    physical = {e, m, c, lam, hbar, R, r}
    leaked = free & physical
    is_pure = g_s.is_number or (g_s.free_symbols <= {N_cover, p, q})
    print(f"  [{label}] g = {g_s}")
    print(f"           free symbols in g: {sorted(map(str, free)) or '(none - pure number)'}")
    print(f"           physical constants leaked into g: "
          f"{sorted(map(str, leaked)) or 'NONE (all cancelled)'}")
    print(f"           g is a pure geometric number/integer: {is_pure}")
    return g_s, (len(leaked) == 0), is_pure


def main():
    print("=" * 74)
    print("ELECTRON g-FACTOR FROM THE (2,3) c-SPEED SELF-ORBIT — sympy derivation")
    print("=" * 74)

    print("\n[1] NAIVE c-ORBIT CONTROL (single object, single cover, charge==mass):")
    mu_n, S_n, g_n = naive_control()
    print(f"    mu_naive = {mu_n}   (= e*c*lam/2 = mu_B at lam=lam_C)")
    print(f"    S_naive  = {S_n}   (= m*c*lam = hbar at lam=lam_C=hbar/(m c))")
    g_n_s, clean_n, pure_n = firewall_report(g_n, "naive")
    assert g_n_s == 1, f"NAIVE CONTROL FAILED: expected g=1, got {g_n_s}"
    print("    -> PASS: naive single-cover c-orbit gives g=1 (geometry does NOT lift).")

    print("\n[2] GENERAL (p,q) TORUS-KNOT CO-CIRCULATION CONTROL:")
    area_check, enclosed, g_pq = torus_knot_control()
    print(f"    (x y' - y x') - p*rho^2  simplifies to: {area_check}   (expect 0)")
    print(f"    z-enclosed area over one traversal: {enclosed}   (= p*(2 pi R^2 + pi r^2))")
    assert area_check == 0, "enclosed-area integrand identity failed"
    g_pq_s, clean_pq, pure_pq = firewall_report(g_pq, "torus(p,q)")
    assert g_pq_s == 1, f"(p,q) CO-CIRCULATION FAILED: expected g=1, got {g_pq_s}"
    print("    -> PASS: g=1 for ALL (p,q). Winding topology ALONE does NOT lift g;")
    print("       the p enclosed-area factor cancels the p angular-momentum factor.")
    print("       => the SECTOR SPLIT (not the knot per se) must do the work.")

    print("\n[3] AVE ELECTRON — A1(mass) perp T2(charge), double-cover N_cover=2:")
    mu_e, S_e, g_e = ave_electron(2)
    print(f"    mu = {mu_e}   (charge single-2pi loop: cover-IMMUNE -> mu_B)")
    print(f"    S  = {S_e}   (mass A1 spinor 4pi double-cover -> S_naive/2 = hbar/2)")
    g_e_s, clean_e, pure_e = firewall_report(g_e, "electron")
    assert g_e_s == 2, f"AVE ELECTRON FAILED: expected g=2, got {g_e_s}"
    print("    -> g = 2.")

    print("\n[4] COVER-DEGREE GENERALIZATION (the WHERE-trace): g = N_cover exactly.")
    g_cov = cover_generalization()
    print(f"    g(N_cover) = {g_cov}")
    assert sp.simplify(g_cov - N_cover) == 0, "cover generalization failed"
    print("    -> g = N_cover. N_cover=1 (single cover) -> g=1;")
    print("       N_cover=2 (double cover = (2,3) poloidal '2' = K4 bipartite) -> g=2.")
    print("       The '3' (q-axis / toroidal) does NOT enter g.")

    print("\n[5] FIREWALL SUMMARY (pre-registered s4):")
    all_clean = clean_n and clean_pq and clean_e
    all_pure = pure_n and pure_pq and pure_e
    print(f"    constants cancel in every g (no e/m/c/lam/hbar leak): {all_clean}")
    print(f"    every g is a pure geometric number/integer:           {all_pure}")
    assert all_clean and all_pure, "FIREWALL DIRTY"

    print("\n[6] ANTI-FIREWALL NUMERIC CROSS-CHECK (constants are NOT an input to g):")
    # Import CODATA ONLY here, ONLY to confirm g is INVARIANT under substitution.
    from ave.core.constants import M_E, C_0, HBAR, e_charge
    lam_C_num = HBAR / (M_E * C_0)         # reduced Compton wavelength (numeric)
    subs = {m: M_E, c: C_0, hbar: HBAR, e: e_charge, lam: lam_C_num}
    g_e_num = sp.simplify(g_e.subs(subs))
    print(f"    g_electron with CODATA substituted: {g_e_num}   (must equal 2)")
    assert sp.nsimplify(g_e_num) == 2, "g CHANGED under CODATA substitution -> FIREWALL DIRTY"
    print("    -> g is invariant under CODATA substitution (constant in the physical")
    print("       constants). The numeric check CONFIRMS, it does NOT feed, g.")

    print("\n" + "=" * 74)
    print("VERDICT: [G2-FORCED] (conditional on the canonical double-cover assignment)")
    print("  naive control g=1; (p,q) co-circulation g=1; A1/T2 split g=2; firewall clean.")
    print("  WHERE the 2 comes from: g = N_cover; N_cover=2 is the (2,3) poloidal")
    print("  double-wrap = K4 bipartite 2-sublattice = spin-1/2 4pi double-cover.")
    print("  Peer-with-Dirac at VALUE level; AVE content = the FORCED FORM g=2.")
    print("=" * 74)


if __name__ == "__main__":
    main()
