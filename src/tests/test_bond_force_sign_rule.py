"""Tests for the end-to-end bond FORCE per loading path (resolves the #526 sign fork).

Prereg (FROZEN): research/2026-07-04_bond-force-sign-rule_prereg_FROZEN.md.
Verdict: [SIGN-RULE-DERIVED] -- the two loading paths give OPPOSITE-sign end forces
from the same fixed-arc-length constraint A^2+S^2=arc*^2: pluck->tension->capped,
end-load->compression->uncapped. The fork resolves into a channel-keyed rule.

These tests lock the LOAD-BEARING physics: the sympy symbolic backbone (every
derivative exact-zero), both arm signs + their positive controls, the bit-exact tie
of arm-b magnitude to the MERGED #526 bond_tension, the four-track sign-keyed
cap-vs-uncap structure through the remap, the frozen bin verdict, and -- critically
-- the DISCREPANT-HALT synthetic trigger (closing the #521/#526 dead-else gap).
"""
from __future__ import annotations

import numpy as np
import pytest

from scripts.vol_1_foundations.bond_force_sign_rule import (
    ARC_STAR_BAND,
    A_CORE_SQRT_ALPHA,
    DiscrepantHalt,
    arm_a_magnitude,
    arm_a_pluck_tension,
    arm_a_pluck_tension_leading,
    arm_b_endload_force,
    arm_b_magnitude,
    arm_b_plateau_buckling_load,
    arm_b_prebuckle_hooke,
    four_tracks,
    run_positive_controls,
    select_bin,
    symbolic_backbone,
)
from scripts.vol_1_foundations.prestress_elastic_tensor import bond_tension
from scripts.vol_1_foundations.srs_elastic_tensor import srs_primitive


@pytest.fixture(scope="module")
def srs():
    return srs_primitive("right")


# --------------------------------------------------------------------------
# The sympy symbolic backbone -- every derivative/chain-rule step EXACT ZERO
# --------------------------------------------------------------------------
def test_symbolic_backbone_all_exact_zero():
    """Prereg PC-dim: all 12 residuals exactly 0 (sympy), incl phi'==#526, Maxwell recovery."""
    res = symbolic_backbone()
    for name, val in res.items():
        assert val == 0, f"symbolic residual {name} = {val} (must be exactly 0)"


def test_symbolic_backbone_covers_both_arms_and_quarter():
    """The backbone verifies both arms AND the 1/4 plateau factor trace (condition 4)."""
    res = symbolic_backbone()
    for key in ("arm_a_at_0", "arm_a_leading_minus_2ka_y2_over_ell", "arm_a_from_energy",
                "arm_b_plateau_minus_kb_ell_over_4", "quarter_factor_trace",
                "phi_prime_matches_526", "phi_second_at_0_minus_k0"):
        assert key in res and res[key] == 0


# --------------------------------------------------------------------------
# ARM (a) TRANSVERSE PLUCK -> TENSION (positive controls PC-a1, PC-a2)
# --------------------------------------------------------------------------
def test_arm_a_pluck_vanishes_at_zero():
    """PC-a1: T_a(0)=0 exactly -- no force at zero pluck (guitar-string slack limit)."""
    assert arm_a_pluck_tension(0.0) == 0.0


def test_arm_a_pluck_is_tension_positive():
    """Arm (a) sign = TENSION (>0) for any nonzero pluck."""
    for y in (0.1, 0.3, 0.7, 0.99):
        assert arm_a_pluck_tension(y) > 0.0


def test_arm_a_small_y_matches_elementary_string():
    """PC-a2: small-y limit matches the elementary fixed-ends result 2 k_a y^2/ell."""
    y = 1e-3
    exact = arm_a_pluck_tension(y)
    lead = arm_a_pluck_tension_leading(y)
    assert abs(exact - lead) / abs(lead) < 1e-4     # O(y^2) deviation at y=1e-3


def test_arm_a_second_order_not_first():
    """The pluck tension is 2nd-order geometric: halving y quarters T (not halves)."""
    r = arm_a_pluck_tension(0.02) / arm_a_pluck_tension(0.01)
    assert abs(r - 4.0) < 0.05                        # ~4x, quadratic


# --------------------------------------------------------------------------
# ARM (b) AXIAL END-LOAD -> COMPRESSION (positive controls PC-b1, PC-b2, PC-recon)
# --------------------------------------------------------------------------
def test_arm_b_endload_is_compression_negative():
    """Arm (b) sign = COMPRESSION (<0) for any nonzero amplitude."""
    for A in (0.1, 0.3, 0.7, 0.95):
        assert arm_b_endload_force(A) < 0.0


def test_arm_b_magnitude_ties_to_526_bit_exact():
    """PC-recon: |arm_b phi_prime| == #526 bond_tension BIT-EXACT (consumed fn, not reimplemented)."""
    for A in np.linspace(0.05, 0.95, 19):
        assert abs(arm_b_magnitude(float(A), "phi_prime")) == float(bond_tension(A))


def test_arm_b_plateau_is_finite_compressive_buckling_load():
    """PC-b1: plateau P_c=-k_b*ell/4 -- FINITE compressive force as bow->0+ (Euler analog)."""
    pc = arm_b_plateau_buckling_load(k_b=1.0, ell=1.0)
    assert np.isfinite(pc) and pc < 0.0 and abs(pc + 0.25) < 1e-15


def test_arm_b_prebuckle_hooke_vanishes_at_zero():
    """PC-b2: pre-buckling Hooke branch -> 0 as u->0, compressive for u>0."""
    assert arm_b_prebuckle_hooke(0.0) == 0.0
    assert arm_b_prebuckle_hooke(0.1) < 0.0


# --------------------------------------------------------------------------
# The two arms have OPPOSITE SIGNS -- the load-bearing finding
# --------------------------------------------------------------------------
def test_arms_have_opposite_signs():
    """The whole verdict: pluck TENSION (+) vs end-load COMPRESSION (-) at the same amplitude."""
    A = 0.5
    assert arm_a_pluck_tension(A) > 0.0
    assert arm_b_endload_force(A) < 0.0
    assert np.sign(arm_a_pluck_tension(A)) != np.sign(arm_b_endload_force(A))


# --------------------------------------------------------------------------
# Positive controls (HALT-gated) -- all pass
# --------------------------------------------------------------------------
def test_positive_controls_all_pass(srs):
    pos, bonds, rho = srs
    pc = run_positive_controls(pos, bonds, rho)
    assert pc["ALL_PC_PASS"] is True
    assert pc["PC_recon_max_abs_dev"] == 0.0        # arm-b magnitude bit-exact to #526


# --------------------------------------------------------------------------
# The four tracks -- sign-keyed cap vs uncap through the MERGED #526 remap
# --------------------------------------------------------------------------
def test_four_tracks_present(srs):
    pos, bonds, rho = srs
    tr = four_tracks(pos, bonds, rho, arc_star=0.96)
    assert set(tr) == {"arm_a_geometric", "arm_a_phi_prime",
                       "arm_b_geometric", "arm_b_phi_prime"}


def test_tension_arm_caps_compression_arm_uncaps(srs):
    """Arm a (tension, T>0) GROWS k_shear_eff (caps rho'); arm b (T<0) SHRINKS it (uncaps).

    IN-REGIME (item 2): the pluck is at the fixed-arc premise's bow ceiling, so the cap is
    WEAKER than the old out-of-regime numbers (arm_a rho' in [1.97, 7.10], not [1.17, 2.04]).
    """
    pos, bonds, rho = srs
    for arc_star in (0.70, 0.96):
        tr = four_tracks(pos, bonds, rho, arc_star=arc_star)
        for name, t in tr.items():
            if t["arm"] == "a_pluck":
                assert t["T_signed"] > 0 and t["k_shear_eff"] > t["S_shear"]
                assert t["rho_prime"] < 8.0            # capped (in-regime, weaker)
            else:
                assert t["T_signed"] < 0 and t["k_shear_eff"] < t["S_shear"]
                assert t["rho_prime"] > 10.0           # uncapped large


def test_arm_a_in_regime_bow_replaces_out_of_regime(srs):
    """Item 2: the pluck bow is the fixed-arc ceiling, NOT y=0.99479 (arc=2.23*ell)."""
    from scripts.vol_1_foundations.bond_force_sign_rule import in_regime_pluck_bow
    # tent arc*=0.96 -> small bow ~0.14; elastica arc*=0.70 -> ~0.42; both << 0.99479
    assert in_regime_pluck_bow(0.96) < 0.2
    assert in_regime_pluck_bow(0.70) < 0.5
    assert in_regime_pluck_bow(0.96) < in_regime_pluck_bow(0.70)   # tighter arc, smaller bow
    tr = four_tracks(pos=srs[0], bonds=srs[1], rho=srs[2], arc_star=0.96)
    for name, t in tr.items():
        if t["arm"] == "a_pluck":
            assert abs(t["y_pluck_in_regime"] - in_regime_pluck_bow(0.96)) < 1e-12


def test_arm_b_phi_prime_reproduces_526_t_negative_arm(srs):
    """arm_b_phi_prime at the tent edge (arc*=0.96, dy=1) reproduces #526's T<0 arm:
    nu=+0.466, rho'=59.93 at the crossing (bit-consistent with the merged remap)."""
    pos, bonds, rho = srs
    tr = four_tracks(pos, bonds, rho, arc_star=0.96)
    t = tr["arm_b_phi_prime"]
    assert abs(t["nu"] - 0.46594) < 1e-3
    assert abs(t["rho_prime"] - 59.93) < 0.1


def test_bands_move_magnitudes_not_signs(srs):
    """Over the arc* band the FORCE magnitude bands but the SIGN is invariant (verdict robust)."""
    pos, bonds, rho = srs
    lo, hi = ARC_STAR_BAND
    tlo = four_tracks(pos, bonds, rho, arc_star=lo)
    thi = four_tracks(pos, bonds, rho, arc_star=hi)
    for name in tlo:
        assert np.sign(tlo[name]["T_signed"]) == np.sign(thi[name]["T_signed"])
        # magnitude actually differs (a band, not a point)
        assert tlo[name]["T_signed"] != thi[name]["T_signed"]


# --------------------------------------------------------------------------
# The bin verdict -- FROZEN bins, no fall-through else
# --------------------------------------------------------------------------
def test_verdict_is_sign_rule_derived(srs):
    pos, bonds, rho = srs
    tr = four_tracks(pos, bonds, rho, arc_star=0.96)
    v = select_bin(tr)
    assert v["verdict"] == "SIGN-RULE-DERIVED"


def test_same_sign_bin_reachable():
    """[SAME-SIGN] bin is reachable: synthetic same-sign tracks (both tension) hit it."""
    tracks = {
        "arm_a_x": {"arm": "a_pluck", "T_signed": +0.5, "S_shear": 0.9, "k_shear_eff": 1.4},
        "arm_b_x": {"arm": "b_endload", "T_signed": +0.3, "S_shear": 0.9, "k_shear_eff": 1.2},
    }
    v = select_bin(tracks)
    assert v["verdict"] == "SAME-SIGN"


def test_path_indeterminate_bin_reachable():
    """[PATH-INDETERMINATE] bin is reachable: a zero-signed force hits it."""
    tracks = {
        "arm_a_x": {"arm": "a_pluck", "T_signed": 0.0, "S_shear": 0.9, "k_shear_eff": 0.9},
        "arm_b_x": {"arm": "b_endload", "T_signed": -0.3, "S_shear": 0.9, "k_shear_eff": 0.6},
    }
    v = select_bin(tracks)
    assert v["verdict"] == "PATH-INDETERMINATE"


# --------------------------------------------------------------------------
# DISCREPANT-HALT -- reachable AND triggers on synthetic input (the recurring gap)
# --------------------------------------------------------------------------
def test_discrepant_halt_fires_on_tension_that_uncaps():
    """A TENSION (T>0) whose remap UNCAPPED (k_shear_eff<S_shear) is a contradiction -> HALT."""
    bad = {"arm_a_bad": {"arm": "a_pluck", "T_signed": +0.5,
                         "S_shear": 0.9, "k_shear_eff": 0.2}}
    with pytest.raises(DiscrepantHalt):
        select_bin(bad)


def test_discrepant_halt_fires_on_compression_that_caps():
    """A COMPRESSION (T<0) whose remap strictly CAPPED (k_shear_eff>S_shear) -> HALT."""
    bad = {"arm_b_bad": {"arm": "b_endload", "T_signed": -0.5,
                         "S_shear": 0.9, "k_shear_eff": 1.4}}
    with pytest.raises(DiscrepantHalt):
        select_bin(bad)


def test_discrepant_halt_does_not_fire_on_consistent_tracks(srs):
    """The live four tracks are all sign<->structure consistent (no false HALT)."""
    pos, bonds, rho = srs
    tr = four_tracks(pos, bonds, rho, arc_star=0.96)
    v = select_bin(tr)                     # must not raise
    assert v["verdict"] == "SIGN-RULE-DERIVED"


# --------------------------------------------------------------------------
# Anti-tune guard -- the visible knife targets are never inputs
# --------------------------------------------------------------------------
def test_plateau_quarter_is_geometric_not_charge_fraction():
    """The 1/4 in P_c=-k_b*ell/4 is tent geometry (a FORCE), not a canon 1/4 -- KNIFE=noise."""
    assert arm_b_plateau_buckling_load(1.0, 1.0) == -0.25
    # a DIFFERENT bend stiffness gives a DIFFERENT plateau -> the 1/4 is not universal
    assert arm_b_plateau_buckling_load(2.0, 1.0) == -0.5


def test_a_core_is_sqrt_alpha_readoff():
    """A_core = sqrt(alpha) is read-off, not tuned (anti-tune guard)."""
    from ave.core.constants import ALPHA
    assert abs(A_CORE_SQRT_ALPHA - float(np.sqrt(ALPHA))) < 1e-15


def test_bulk_strain_to_per_bond_is_affine_uniform(srs):
    """Item 4: uniform bulk strain eps -> per-bond axial strain eps on EVERY bond (affine)."""
    from scripts.vol_1_foundations.bond_force_sign_rule import bulk_strain_to_per_bond_amplitude
    pos, bonds, rho = srs
    aff = bulk_strain_to_per_bond_amplitude(0.01, pos, bonds)
    assert aff["uniform"] is True                              # orientation-independent
    assert abs(aff["A_bond_affine"] - 0.01) < 1e-12           # A_bond == eps
    assert abs(aff["per_bond_axial_strain_max"]
               - aff["per_bond_axial_strain_min"]) < 1e-12    # min == max
