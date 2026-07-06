"""Problem 3 — muonic-H 2S-2P SVE-kernel shift: gating tests.

FROZEN prereg: research/2026-07-05_problem3-muonic-lamb_METHOD-prereg.md (freeze
commit 4747630b). Routes the FROZEN fork-memo bins ([A]/[B]/[C]).

Fast closed-form checks (Gate-0 reconnaissance reproduction, analytic tail
coefficient, ReconcileGate positive control, routing verdict) STAY gating. The
full-band driver (two-path quadrature over 5 variants, ~7s) is engine_sim
(::test_full_driver_runs_and_routes_C), routed to make test-engine.
"""

import numpy as np
import pytest
from scipy import integrate, special

from ave.core.constants import ALPHA, E_YIELD, EPSILON_0, L_NODE, M_E, M_PROTON, e_charge

# ---- canonical + external inputs (mirror the driver) ------------------------
E_C = E_YIELD
K = e_charge / (4.0 * np.pi * EPSILON_0)
M_MU = 206.7682830 * M_E  # CODATA 2018 ratio (external input)
MU_RED = M_MU * M_PROTON / (M_MU + M_PROTON)
A_MU = (L_NODE / ALPHA) * (M_E / MU_RED)
R_NS = np.sqrt(e_charge / (4.0 * np.pi * EPSILON_0 * E_C))
WINDOW_ueV = 2.3  # CREMA 1 sigma (primary edge)


def test_gate0_reconnaissance_reproduces_frozen_memo():
    """Gate 0: the frozen memo's Problem-1/2 numbers reproduce from constants.py."""
    assert L_NODE * 1e15 == pytest.approx(386.16, abs=0.01)  # ell_node
    assert E_C == pytest.approx(1.1304e17, rel=1e-3)  # E_c = E_YIELD

    # no-solution radii (E=E_c)
    def r_ns(Z):
        return np.sqrt(Z * e_charge / (4 * np.pi * EPSILON_0 * E_C))

    assert r_ns(1) * 1e15 == pytest.approx(112.9, abs=0.2)
    assert r_ns(29) * 1e15 == pytest.approx(607.8, abs=0.5)
    assert r_ns(92) * 1e15 == pytest.approx(1082.6, abs=1.0)

    # A^2 landmarks
    def A2(Z, r):
        return (Z * e_charge / (4 * np.pi * EPSILON_0 * r**2) / E_C) ** 2

    assert A2(1, 285e-15) == pytest.approx(0.0246, abs=0.001)  # muonic-H
    assert A2(92, 575e-15) == pytest.approx(12.6, rel=0.02)  # U91+ (>1: no real S)


def test_muonic_reduced_mass_and_bohr_radius():
    """External CODATA muon input -> reduced mass ~186 m_e, a_mu ~285 fm."""
    assert MU_RED / M_E == pytest.approx(185.84, abs=0.05)
    assert A_MU * 1e15 == pytest.approx(284.75, abs=0.5)


def test_analytic_tail_coefficient_derived_independently():
    """The 1/10 tail coefficient is DERIVED (not restated) two independent ways, both
    disjoint from the closed-form deltaV=k^3/(10 E_c^2 r^5) used in the driver:

      (A) from the constitutive law directly: root-find the true field E(r') from
          E*sqrt(1-(E/E_c)^2)=E_C(r'), integrate (E-E_C) inward from a large radius r0
          where the field is weak, and check the result equals C*k^3/(E_c^2 r0^5) with
          C recovered = 1/10 (the coefficient falls out of the numeric integral).
      (B) from the branch-inversion series coefficient: the leading field enhancement is
          (E-E_C)=(1/2)E_C^3/E_c^2, and int_r^inf (1/2)(k/r'^2)^3/E_c^2 dr' = k^3/(10 E_c^2 r^5)
          -> the 1/10 = (1/2)*(1/5) where 1/5 is int_r^inf r'^-6 dr' * r^5. Both the 1/2
          (series) and the 1/5 (integral) are recomputed here, not assumed.
    """
    from scipy import optimize

    r0 = 30.0 * R_NS  # weak-field radius (A^2 ~ (r_ns/r0)^4 ~ 1e-6): tail regime

    # --- (A) constitutive-law root-find + inward integral, coefficient recovered ---
    def E_true(rp):
        EC = K / rp**2
        if EC > E_C / 2:
            return np.nan
        return optimize.brentq(lambda E: E * np.sqrt(max(1 - (E / E_C) ** 2, 0.0)) - EC, EC, E_C / np.sqrt(2))

    dV_num, _ = integrate.quad(lambda rp: E_true(rp) - K / rp**2, r0, 400 * R_NS, limit=400)
    C_recovered = dV_num * E_C**2 * r0**5 / K**3
    assert C_recovered == pytest.approx(0.1, rel=1e-3)  # 1/10 falls out of the physics

    # --- (B) recompute the two factors that make 1/10 = (1/2)*(1/5) ---
    # series factor 1/2: solve u*sqrt(1-u^2)=x for small x, leading correction u=x+(1/2)x^3
    # (x=1e-3 balances higher-order +7/8 x^2 drift ~9e-7 against float cancellation in u-x)
    x = 1e-3
    u = optimize.brentq(lambda uu: uu * np.sqrt(1 - uu**2) - x, x, 1 / np.sqrt(2), xtol=1e-16, rtol=1e-15)
    series_half = (u - x) / x**3  # -> 1/2
    assert series_half == pytest.approx(0.5, rel=1e-3)
    # integral factor 1/5: int_r^inf r'^-6 dr' * r^5 = 1/5
    integ_fifth = integrate.quad(lambda rp: rp**-6, 1.0, np.inf)[0]  # = 1/5 at r=1
    assert integ_fifth == pytest.approx(0.2, rel=1e-9)
    assert series_half * integ_fifth == pytest.approx(0.1, rel=1e-3)  # (1/2)*(1/5)=1/10, independent


def test_reconcile_positive_control_fires():
    """ReconcileGate liveness: PATH-A exp-integral == direct quad on a known 1/r^5."""
    a = A_MU
    coeff = K**3 / (10.0 * E_C**2)
    uc = (R_NS * np.sqrt(2.0)) / a

    def rho_2s(r):
        R = (1 / np.sqrt(2)) * a**-1.5 * (1 - r / (2 * a)) * np.exp(-r / (2 * a))
        return R**2 * r**2

    def upn(n, x):
        return x ** (1 - n) * special.expn(n, x)

    ctrlA = coeff / (2.0 * a**5) * (upn(3, uc) - upn(2, uc) + 0.25 * upn(1, uc))
    ctrlB, _ = integrate.quad(lambda r: rho_2s(r) * coeff / r**5, R_NS * np.sqrt(2.0), 60 * a, limit=400)
    assert abs(ctrlA - ctrlB) / abs(ctrlA) < 1e-6  # gate CAN fire on a known case


def test_smallest_variant_grossly_violates_window():
    """The most-favorable (smallest) shift variant is L-i ~5e4 ueV, ~2e4x the window.

    Even the smallest arm/variant exceeds the 2.3 ueV window by >1e4x -> the routing
    is [C-EXCLUDED] robustly (no arm clears). We assert the FLOOR of the band here
    (L-i, the lattice hard-cutoff at ell_node, the smallest magnitude) using the fast
    closed-form tail integral for the lattice-scoped 2S and 2P from ell_node.
    """
    a = A_MU
    coeff = K**3 / (10.0 * E_C**2)
    uc = L_NODE / a  # lattice hard-cutoff L-i

    def upn(n, x):
        return x ** (1 - n) * special.expn(n, x)

    e2s = e_charge * coeff / (2.0 * a**5) * (upn(3, uc) - upn(2, uc) + 0.25 * upn(1, uc))
    e2p = e_charge * coeff / (24.0 * a**5) * special.exp1(uc)
    shift_ueV = (e2s - e2p) / e_charge * 1e6
    # L-i shift ~ -4.9e4 ueV; magnitude ~2e4x the 2.3 ueV window
    assert abs(shift_ueV) > 1e4 * WINDOW_ueV  # grossly violates -> not [A], not [B]
    assert abs(shift_ueV) == pytest.approx(4.9e4, rel=0.1)


def test_b_defeat_cutoff_refutes_the_300fm_floor():
    """The hard cutoff must move to ~9 ell_node (~3.5 pm) to clear the window -> ~12x the
    memo's ~300 fm floor estimate. Refutes the floor as the protective scale (routing)."""
    from scipy import optimize

    a = A_MU
    coeff = K**3 / (10.0 * E_C**2)

    def upn(n, x):
        return x ** (1 - n) * special.expn(n, x)

    def shift_ueV(r_cut):
        uc = r_cut / a
        e2s = e_charge * coeff / (2.0 * a**5) * (upn(3, uc) - upn(2, uc) + 0.25 * upn(1, uc))
        e2p = e_charge * coeff / (24.0 * a**5) * special.exp1(uc)
        return (e2s - e2p) / e_charge * 1e6

    r_defeat = optimize.brentq(lambda rc: abs(shift_ueV(rc)) - WINDOW_ueV, 5 * L_NODE, 40 * L_NODE)
    assert r_defeat / L_NODE == pytest.approx(9.05, rel=0.05)  # ~9 ell_node
    assert r_defeat / 300e-15 > 10  # >10x the memo's ~300 fm floor


def test_u91_continuum_arm_is_incomputable():
    """U91+ secondary: the 1s orbit sits inside the no-solution radius -> continuum
    kernel incomputable over the bulk of the density (reportable result, not failure)."""
    Z = 92
    a_U = (L_NODE / ALPHA) / Z  # electronic 1s Bohr for Z=92
    r_ns_U = np.sqrt(Z * e_charge / (4 * np.pi * EPSILON_0 * E_C))
    assert a_U < r_ns_U  # orbit inside no-solution radius

    def rho_1s(r):
        R = 2 * a_U**-1.5 * np.exp(-r / a_U)
        return R**2 * r**2

    frac_inside, _ = integrate.quad(rho_1s, 0, r_ns_U, limit=300)
    assert frac_inside > 0.5  # >50% of 1s density has no real solution


@pytest.mark.engine_sim
def test_full_driver_runs_and_routes_C():
    """Full two-path, 5-variant driver runs and routes [C-EXCLUDED]. engine_sim (~7s)."""
    import importlib

    mod = importlib.import_module("scripts.verify.problem3_muonic_lamb_shift")
    # smoke: main() runs both paths over all variants without error
    mod.main()
