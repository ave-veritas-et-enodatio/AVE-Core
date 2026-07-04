"""Regression gate — THE PARENT-CONDITION DERIVATION [MECHANISM-DERIVED].

Locks the verdict: the matched-line property (Ax3 Minimum Reflection Principle,
internal-boundary form) FORCES k_s=k_a on the chiral srs-z3 net. The MATCH /
BALANCE / HEAVISIDE conditions CO-LOCATE at ρ_bond=1 knob-free; Ax3 is the parent.

Prereg (FROZEN): research/2026-07-04_parent-condition-match-forces-balance_prereg_FROZEN.md
Driver: src/scripts/vol_4_engineering/parent_condition_match_forces_balance.py
"""

from __future__ import annotations

import numpy as np
import pytest

from scripts.vol_4_engineering.parent_condition_match_forces_balance import (
    acoustic_speeds,
    internal_gamma_functional,
    locate_min,
    photon_branch_isotropy,
    srs_primitive,
    heaviside_distortion,
    main,
)


@pytest.fixture(scope="module")
def srs():
    pos, a, bonds = srs_primitive("right")
    bond_len = float(np.linalg.norm(bonds[0][2]))
    return pos, bonds, bond_len


# ---- VALIDATE-ON-KNOWN: the instrument genuinely measures reflection ----------
def test_V1_gamma_zero_on_isotropic(srs):
    """V1: the internal-Γ functional reads ~0 on the isotropic control (k_s=k_a)."""
    pos, bonds, bl = srs
    g = internal_gamma_functional(pos, bonds, k_axial=1.0, k_shear=1.0, bond_len=bl)
    assert g["gamma_worst"] < 1e-6


def test_V2_gamma_nonzero_on_anisotropic(srs):
    """V2 (load-bearing): the functional MUST see anisotropy — nonzero at k_s≠k_a.
    Guards against validating a blind instrument."""
    pos, bonds, bl = srs
    g = internal_gamma_functional(pos, bonds, k_axial=2.0, k_shear=1.0, bond_len=bl)
    assert g["gamma_worst"] > 1e-3


# ---- THE MECHANISM: Ax3 |Γ|²-min lands on k_s=k_a knob-free -------------------
def test_match_locus_is_ks_eq_ka_knob_free(srs):
    """The internal-boundary |Γ|² minimiser (unseeded golden-section) lands at ρ=1."""
    pos, bonds, bl = srs
    rstar, gmin = locate_min(
        lambda r: internal_gamma_functional(pos, bonds, k_axial=r, k_shear=1.0,
                                            bond_len=bl)["gamma_worst"])
    assert abs(rstar - 1.0) < 1e-4
    assert gmin < 1e-6


def test_true_minimum_positive_curvature(srs):
    """ρ=1 is a true minimum (positive curvature), not a saddle or edge artifact."""
    pos, bonds, bl = srs
    h = 1e-3
    f = lambda r: internal_gamma_functional(pos, bonds, k_axial=r, k_shear=1.0,
                                            bond_len=bl)["gamma_rms"]
    curv = (f(1 + h) - 2 * f(1) + f(1 - h)) / h ** 2
    assert curv > 1.0


# ---- THREE-CONDITIONS CO-LOCATION (the parent exists) ------------------------
def test_three_conditions_co_locate(srs):
    """MATCH / BALANCE / HEAVISIDE all minimise at the SAME ρ_bond=1."""
    pos, bonds, bl = srs
    r_match, _ = locate_min(
        lambda r: internal_gamma_functional(pos, bonds, k_axial=r, k_shear=1.0,
                                            bond_len=bl)["gamma_worst"])
    r_bal, _ = locate_min(
        lambda r: photon_branch_isotropy(pos, bonds, k_axial=r, k_shear=1.0, bond_len=bl))
    r_hv, _ = locate_min(
        lambda r: heaviside_distortion(pos, bonds, k_axial=r, k_shear=1.0, bond_len=bl))
    spread = max(r_match, r_bal, r_hv) - min(r_match, r_bal, r_hv)
    assert spread < 1e-3          # co-located
    assert abs(r_match - 1.0) < 1e-4


# ---- INDEPENDENCE CONTROL: co-location is physics, not construction ----------
def test_stability_locus_does_not_colocate(srs):
    """The bulk-modulus (K) sign locus is ρ≥2 (K<0 at ρ=1), NOT ρ=1. An independent
    quantity sits elsewhere ⇒ the MATCH/BALANCE/HEAVISIDE co-location is genuine."""
    pos, bonds, bl = srs

    def k_proxy(rho):
        cs = acoustic_speeds([1, 1, 1], pos, bonds, k_axial=rho, k_shear=1.0, bond_len=bl)
        return cs[2] ** 2 - (4.0 / 3.0) * cs[0] ** 2  # ~ K/ρ

    assert k_proxy(1.0) < 0        # match point is mechanically UNSTABLE (honest flag)
    assert k_proxy(2.0) > -1e-2    # K crosses zero near ρ=2 (separate locus)


# ---- FULL ISOTROPY over the direction sphere at ρ=1 --------------------------
def test_full_sphere_isotropy_at_match(srs):
    """At ρ=1 all acoustic branches are degenerate over 100 random directions."""
    pos, bonds, bl = srs
    rng = np.random.default_rng(0)
    zs = []
    for _ in range(100):
        q = rng.standard_normal(3)
        cs = acoustic_speeds(q, pos, bonds, k_axial=1.0, k_shear=1.0, bond_len=bl)
        zs.extend(cs.tolist())
    zs = np.array(zs)
    assert (zs.max() - zs.min()) / (zs.max() + zs.min()) < 1e-6


# ---- ENANTIOMORPH PARITY (cold) ----------------------------------------------
def test_enantiomorph_parity(srs):
    """The match locus is hand-independent (4₁-screw handedness is saturation-only)."""
    posR, _, blR = srs
    r_R, _ = locate_min(
        lambda r: internal_gamma_functional(posR, srs[1], k_axial=r, k_shear=1.0,
                                            bond_len=blR)["gamma_worst"])
    posL, aL, bondsL = srs_primitive("left")
    blL = float(np.linalg.norm(bondsL[0][2]))
    r_L, _ = locate_min(
        lambda r: internal_gamma_functional(posL, bondsL, k_axial=r, k_shear=1.0,
                                            bond_len=blL)["gamma_worst"])
    assert abs(r_R - r_L) < 1e-4


# ---- END-TO-END: the driver returns [MECHANISM-DERIVED] / Ax3-parent ---------
def test_driver_verdict():
    out = main()
    assert out["validate_on_known"]["ALL_PASS"] is True
    assert out["VERDICT"]["BIN"] == "[MECHANISM-DERIVED]"
    assert out["VERDICT"]["ax3_is_the_parent"] is True
    assert out["step4_three_conditions_loci"]["CO_LOCATED"] is True
