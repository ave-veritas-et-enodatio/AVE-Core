"""Tests for the PRE-STRESSED srs elastic-tensor arc (beyond-model test 1 of 2).

Prereg (FROZEN): research/2026-07-04_prestress-tensor_prereg_FROZEN.md.
Verdict: [MAP-DEFORMED] on both channel assignments -- [SAME-TENSOR-POINT] does NOT survive
its first beyond-model test (the DC-bias pre-stress deforms the nu(rho_eff) map).

These tests lock the LOAD-BEARING physics: the derived tension form, the (T/l)(I-P) insertion,
the positive controls, the GEOMETRY-COUPLED discriminator (reading A: self-balancing), and the
anti-tune guard (read-off constants never fit).
"""
from __future__ import annotations

import numpy as np
import pytest

from scripts.vol_1_foundations.prestress_elastic_tensor import (
    A_CORE_SQRT_ALPHA,
    A_WALL_518_CROSSING,
    NU_2_7,
    RHO_STAR_IMPORTED,
    bond_tension,
    extract_prestress_Cij,
    residual_node_forces,
    run_positive_controls,
    run_sweep,
)
from scripts.vol_1_foundations.srs_elastic_tensor import (
    extract_cubic_Cij,
    moduli_from_Cij,
    simple_cubic_ref,
    srs_primitive,
)


@pytest.fixture(scope="module")
def srs():
    return srs_primitive("right")


# --------------------------------------------------------------------------
# The derived bond tension Phi'(A) (prereg §2, sympy-verified)
# --------------------------------------------------------------------------
def test_bond_tension_zero_at_zero_bias():
    """Phi'(0)=0 -- the cold reference is un-tensioned (the separating axis from #521)."""
    assert abs(float(bond_tension(0.0))) < 1e-15


def test_bond_tension_finite_pi_over_4_at_yield():
    """Phi'(1)=k0*pi/4 -- FINITE tension at the yield wall (tangent stiffness ->0, tension does not)."""
    assert abs(float(bond_tension(1.0)) - np.pi / 4.0) < 1e-12


def test_bond_tension_matches_closed_form():
    """Phi'(A)=k0(A*sqrt(1-A^2)+arcsin A)/2 at a representative point (matches the integral)."""
    A = 0.6
    expect = (A * np.sqrt(1 - A ** 2) + np.arcsin(A)) / 2.0
    assert abs(float(bond_tension(A)) - expect) < 1e-14


# --------------------------------------------------------------------------
# The (T/l)(I-P) insertion (prereg §3) reduces to the cold pipeline at T=0
# --------------------------------------------------------------------------
def test_zero_tension_reduces_to_cold_bit_exactly(srs):
    """T=0 => the pre-stress driver IS the cold/#521 driver (the identity control, PC1)."""
    pos, bonds, rho = srs
    cold = extract_cubic_Cij(pos, bonds, k_axial=RHO_STAR_IMPORTED, k_shear=1.0, rho=rho)
    pre0 = extract_prestress_Cij(pos, bonds, k_axial=RHO_STAR_IMPORTED, k_shear=1.0,
                                 T_per_bond=0.0, rho=rho)
    for k in ("C11", "C12", "C44"):
        assert abs(cold[k] - pre0[k]) / abs(cold[k]) < 1e-12


def test_nonzero_tension_moves_the_tensor(srs):
    """A live pre-stress term MUST move the tensor (else the insertion is dead)."""
    pos, bonds, rho = srs
    pre0 = extract_prestress_Cij(pos, bonds, k_axial=9.7734, k_shear=1.0, T_per_bond=0.0, rho=rho)
    preT = extract_prestress_Cij(pos, bonds, k_axial=9.7734, k_shear=1.0, T_per_bond=0.3, rho=rho)
    assert abs(preT["C44"] - pre0["C44"]) / abs(pre0["C44"]) > 1e-3


# --------------------------------------------------------------------------
# Positive controls (prereg §4) -- HALT-gated
# --------------------------------------------------------------------------
def test_positive_controls_all_pass(srs):
    pos, bonds, rho = srs
    pc = run_positive_controls(pos, bonds, rho)
    assert pc["PC1_zero_bias_recovery"]["PASS"]
    assert pc["PC2_analytic_stressed_lattice"]["PASS"]
    assert pc["PC3_homogeneity_T0"]["PASS"]
    assert pc["VS4_exact_collapse_to_shifted_shear_spring"]["PASS"]
    assert pc["ALL_PASS"]


def test_vs4_exact_collapse_to_shifted_shear_spring(srs):
    """CORRECTED MECHANISM (orchestrator 16-agent review): prestress(k_a,k_s,T) == cold(k_a,
    k_s+T/l) BIT-EXACTLY. The (T/l)(I-P) string term has the SAME projector structure as the shear
    spring, so the tensor NEVER leaves the cold one-parameter family. Homogeneity INTACT; only #521's
    dictionary breaks."""
    pos, bonds, rho = srs
    ell = float(np.mean([np.linalg.norm(d) for (_, _, d) in bonds]))
    for (ka, ks, T) in [(0.996345, 0.10194, 0.08532), (9.7734, 1.0, 0.3), (0.5, 0.9, 0.7850)]:
        pre = extract_prestress_Cij(pos, bonds, k_axial=ka, k_shear=ks, T_per_bond=T, rho=rho)
        cold = extract_cubic_Cij(pos, bonds, k_axial=ka, k_shear=ks + T / ell, rho=rho)
        err = max(abs(pre[k] - cold[k]) / (abs(cold[k]) + 1e-30) for k in ("C11", "C12", "C44"))
        assert err < 1e-9


def test_pc2_analytic_stressed_lattice_c44_shift_equals_T_over_ell():
    """PC2: uniformly-tensioned simple-cubic transverse shift C44_stressed-C44_unstressed = T/l EXACT."""
    pos, bonds, rho = simple_cubic_ref()  # ell=1
    ka, ks = 1.0, 0.4
    r_un = extract_prestress_Cij(pos, bonds, k_axial=ka, k_shear=ks, T_per_bond=0.0, rho=rho)
    for T in (0.15, 0.3):
        r_st = extract_prestress_Cij(pos, bonds, k_axial=ka, k_shear=ks, T_per_bond=T, rho=rho)
        assert abs((r_st["C44"] - r_un["C44"]) - T) < 1e-6


# --------------------------------------------------------------------------
# The GEOMETRY-COUPLED discriminator (prereg §6 branch ii, §9): reading A
# --------------------------------------------------------------------------
def test_uniform_prestress_self_balances_at_cold_geometry(srs):
    """srs z=3 site symmetry: uniform bond tensions cancel at cold geometry to machine zero =>
    reading A (self-balancing) => [GEOMETRY-COUPLED] NOT triggered => test 1 is well-posed."""
    pos, bonds, _ = srs
    T = float(bond_tension(A_WALL_518_CROSSING))
    rf = residual_node_forces(pos, bonds, T)
    assert rf["relative_residual"] < 1e-9
    assert rf["max_residual_node_force"] < 1e-12


# --------------------------------------------------------------------------
# THE VERDICT: [MAP-DEFORMED] on both assignments (prereg §6)
# --------------------------------------------------------------------------
def test_shear_loads_map_is_deformed(srs):
    """SHEAR-LOADS: the pre-stress deforms the map -- nu at the rho_eff=9.77 crossing drops far
    below 2/7. [SAME-TENSOR-POINT] does NOT survive."""
    pos, bonds, rho = srs
    sweep = run_sweep(pos, bonds, rho)
    d = sweep["SHEAR_LOADS"]
    # deformed either by the pole-free nu shift OR the pole-free shape shift
    assert d["max_abs_delta_nu_over_nu"] > 1e-4 or d["max_abs_shape_dev_vs_521"] > 1e-4
    # at the crossing, nu is pushed far off 2/7 (the SAME-TENSOR-POINT would require nu=2/7 there)
    nu_c = d["nu_Hill_at_crossing_PRESTRESS"]
    assert nu_c is not None
    assert abs(nu_c - NU_2_7) / NU_2_7 > 1e-2   # NOT 2/7 anymore


def test_axial_loads_map_is_deformed_by_shape_metric(srs):
    """AXIAL-LOADS: rho_eff<1 keeps nu in the pole region, so the POLE-FREE SHAPE metric (not the
    nu-ratio) is what gives the honest deformed verdict (guards the spurious-null failure mode)."""
    pos, bonds, rho = srs
    sweep = run_sweep(pos, bonds, rho)
    d = sweep["AXIAL_LOADS"]
    assert d["n_delta_nu_polefree_points"] == 0   # nu always in the pole region here
    assert d["max_abs_shape_dev_vs_521"] > 1e-4    # but the SHAPE is deformed


def test_crossing_amplitude_analytically_invariant(srs):
    """The crossing AMPLITUDE is analytically invariant (pre-stress does not move rho_eff, only the
    tensor at it) -- so it stays at the free-knob A_wall=0.99479 = #518's. The KNIFE is re-aimed off
    this invariant onto the MOVABLE quantities (cap, locus) -- see the knife test below."""
    pos, bonds, rho = srs
    sweep = run_sweep(pos, bonds, rho)
    cross = sweep["SHEAR_LOADS"]["crossing_A_wall"]
    assert cross is not None
    assert abs(cross - A_WALL_518_CROSSING) < 1e-3          # unchanged from #518 (invariant)


def test_true_coordinate_cap_and_corrected_locus(srs):
    """CORRECTED (item 1/4): rho' = S_ax/(S_shear+T/l) is CAPPED at S_ax*l/T = 11.6777 (yield wall
    finite, no longer -> inf); the nu=2/7 OLD-coord locus by BISECTION is 59.93 (not the 66.6 linear-
    interpolation artifact). Neither is canon-distinguished (KNIFE re-aimed, lands-on-canon False)."""
    pos, bonds, rho = srs
    sweep = run_sweep(pos, bonds, rho)
    d = sweep["SHEAR_LOADS"]
    assert abs(d["rho_prime_cap"] - 11.6777) < 1e-2          # the finite cap
    assert d["rho_prime_true_coord_at_yield_limit"] < 12.0   # capped, not diverging
    assert abs(d["new_nu_2_7_locus_rho_eff_OLD_coord_bisected"] - 59.93) < 0.2  # bisected, not 66.6


def test_knife_reaimed_lands_on_no_canon_value(srs):
    """The re-aimed knife (cap + OLD-coord locus, the MOVABLE quantities) lands on NO canon-
    distinguished value. cap ~ 1/sqrt(alpha) is the KNOWN small-A expansion (not a new coincidence)."""
    from scripts.vol_1_foundations.prestress_elastic_tensor import run_positive_controls  # noqa: F401
    pos, bonds, rho = srs
    # re-run the bin verdicts through main-equivalent path by calling run_sweep + checking knife inputs
    sweep = run_sweep(pos, bonds, rho)
    cap = sweep["SHEAR_LOADS"]["rho_prime_cap"]
    locus = sweep["SHEAR_LOADS"]["new_nu_2_7_locus_rho_eff_OLD_coord_bisected"]
    from ave.core.constants import ALPHA
    inv_sqrt_alpha = 1.0 / np.sqrt(ALPHA)
    # cap ~ 1/sqrt(alpha) is the small-A expansion (T~k0*A), documented -- NOT a new chord
    assert abs(cap - inv_sqrt_alpha) / inv_sqrt_alpha < 3e-3
    # neither cap nor locus lands on 9.7734 or 2 (the other canon values)
    for val in (cap, locus):
        assert abs(val - RHO_STAR_IMPORTED) > 1e-2
        assert abs(val - 2.0) > 1e-2


def test_sign_fork_both_arms_and_narrative_inverts(srs):
    """The SIGN FORK (item 3): T>0 (stretched) drops nu 2/7->0.089; T<0 (compressive/buckling) RAISES
    nu 2/7->0.466 toward 1/2 and UNCAPS the coordinate. Bin verdict survives either sign; the physical
    narrative inverts. Reported as an OPEN Grant-fork, not resolved."""
    pos, bonds, rho = srs
    from ave.axioms.scale_invariant import saturation_factor
    S_ax = float(saturation_factor(A_CORE_SQRT_ALPHA, yield_limit=1.0))
    S_sh = float(saturation_factor(A_WALL_518_CROSSING, yield_limit=1.0))
    T0 = float(bond_tension(A_CORE_SQRT_ALPHA))
    pos_ = extract_prestress_Cij(pos, bonds, k_axial=S_ax, k_shear=S_sh, T_per_bond=+T0, rho=rho)
    neg = extract_prestress_Cij(pos, bonds, k_axial=S_ax, k_shear=S_sh, T_per_bond=-T0, rho=rho)
    nu_pos = moduli_from_Cij(pos_["C11"], pos_["C12"], pos_["C44"])["nu_Hill"]
    nu_neg = moduli_from_Cij(neg["C11"], neg["C12"], neg["C44"])["nu_Hill"]
    assert nu_pos < NU_2_7        # T>0 drops nu below 2/7
    assert nu_neg > NU_2_7        # T<0 raises nu above 2/7 (toward 1/2) -- narrative inverts


# --------------------------------------------------------------------------
# Anti-tune guard: read-off constants are never fit
# --------------------------------------------------------------------------
def test_readoff_constants_are_readoff_only():
    """RHO_STAR_IMPORTED / NU_2_7 / A_WALL_518_CROSSING are comparison constants, never sweep inputs."""
    assert RHO_STAR_IMPORTED == 9.7734
    assert abs(NU_2_7 - 2.0 / 7.0) < 1e-12
    assert A_WALL_518_CROSSING == 0.99479
    # A_core is the def-vyvsn1 sqrt(alpha) echo, not a tuned value
    from ave.core.constants import ALPHA
    assert abs(A_CORE_SQRT_ALPHA - np.sqrt(ALPHA)) < 1e-15


def test_two_hand_crossval_agrees(srs):
    """The pre-stressed tensor is trustworthy on the same footing as the cold one (long-wave vs
    [100] direct eigensolve agree at the matter crossing, with branch-matching for near-iso-bond)."""
    from scripts.vol_1_foundations.prestress_elastic_tensor import _two_hand_crossval
    pos, bonds, rho = srs
    cv = _two_hand_crossval(pos, bonds, rho)
    assert cv["ALL_AGREE"]
