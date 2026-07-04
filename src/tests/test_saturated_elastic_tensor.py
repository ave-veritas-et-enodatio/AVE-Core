"""
Regression gate for THE SATURATED srs ELASTIC-TENSOR arc.

Verdict (frozen prereg research/2026-07-04_saturated-elastic-tensor_prereg_FROZEN.md):
  [SAME-TENSOR-POINT] on BOTH channel assignments.
    - The saturated small-signal Cauchy C_ij, from Born-Huang on the SATURATED
      Phi_b(A) = k_a0*S(A_axial)*P + k_s0*S(A_shear)*(I-P), is the cold tensor with
      rho -> rho_eff = rho_cold*(S_axial/S_shear). The nu(rho_eff) map is NOT deformed.
    - SHEAR-LOADS: rho_eff=9.7734 (A_wall=0.99479) => nu_Hill=2/7, K/G=2, Zener=1.229
      EXACTLY -- tensor-equivalent to cold rho*=9.7734. The regime gap (518 section 6) CLOSES.
    - AXIAL-LOADS mirror: SOFTENING, rho_eff->0, no 9.77 crossing; map undeformed.

These tests lock: the load-bearing homogeneity (C_ij deg-1 => ratios deg-0), the
cold positive-control recovery, saturated==cold-at-matched-rho_eff, the two-hand
cross-validation, and the knife (crossing A_wall NOT canon-distinguished; no tuning
toward 2/7, 9.7734, or 0.99479).
"""

import numpy as np
import pytest

from ave.core.constants import ALPHA, NU_VAC
from scripts.vol_1_foundations.saturated_elastic_tensor import (  # type: ignore
    A_CORE_SQRT_ALPHA,
    A_WALL_518_CROSSING,
    RHO_COLD,
    RHO_STAR_IMPORTED,
    k_axial_over_k0,
    k_shear_over_k0,
    operating_point,
    run_sweep,
    run_two_hand_crossval,
    run_validation,
    saturated_tensor,
)
from scripts.vol_1_foundations.srs_elastic_tensor import srs_primitive  # type: ignore


@pytest.fixture(scope="module")
def net():
    return srs_primitive("right")


# ─────────────────────────────────────────────────────────────────────────
# Validate-on-known (HALT-gated in the driver)
# ─────────────────────────────────────────────────────────────────────────
def test_validation_all_pass(net):
    """VS1 cold-recovery + VS2 homogeneity + VS3 saturated==cold-at-matched-rho_eff."""
    pos, bonds, rho = net
    v = run_validation(pos, bonds, rho)
    assert v["ALL_PASS"] is True
    assert v["VS1_cold_recovery"]["PASS"]
    assert v["VS2_homogeneity"]["PASS"]
    assert v["VS3_saturated_equals_cold_at_matched_rho_eff"]["PASS"]


def test_stiffness_maps_are_S(net):
    """k_a/k0 = S(A_axial) and k_s/k0 = S(A_shear) -- both equal the Ax4 kernel."""
    for A in [0.1, 0.5, 0.9, 0.99]:
        S = float(np.sqrt(1.0 - A**2))
        assert float(k_axial_over_k0(np.asarray(A))) == pytest.approx(S, rel=1e-12)
        assert float(k_shear_over_k0(np.asarray(A))) == pytest.approx(S, rel=1e-12)


# ─────────────────────────────────────────────────────────────────────────
# The load-bearing homogeneity: ratios depend ONLY on rho_eff
# ─────────────────────────────────────────────────────────────────────────
def test_ratios_scale_invariant_absolute_moduli_scale(net):
    """Born-Huang C_ij is homogeneous deg-1: ratios (nu,Zener,K/G) are deg-0 (identical
    under overall stiffness scaling), absolute K scales by the scale factor."""
    pos, bonds, rho = net
    base = saturated_tensor(pos, bonds, rho, 1.0, 1.0 / 3.0)  # rho_eff = 3
    lam = 0.41
    scaled = saturated_tensor(pos, bonds, rho, lam, lam / 3.0)  # same rho_eff, scaled by lam
    assert scaled["rho_eff"] == pytest.approx(base["rho_eff"], rel=1e-12)
    for k in ("nu_Hill", "Zener_A", "KG_Hill"):
        assert scaled[k] == pytest.approx(base[k], rel=1e-6)
    assert scaled["K_bulk"] == pytest.approx(lam * base["K_bulk"], rel=1e-6)


def test_cold_positive_control(net):
    """A_wall=0 both channels off => saturated tensor == merged cold tensor at rho=1
    (planted-source gate: C11/C12/C44=+/-0.17678, K<0 unstable, Zener=1)."""
    pos, bonds, rho = net
    t = saturated_tensor(pos, bonds, rho, 1.0, 1.0)
    assert t["rho_eff"] == pytest.approx(1.0, abs=1e-12)
    assert t["C11"] == pytest.approx(0.17678, rel=1e-4)
    assert t["C12"] == pytest.approx(-0.17678, rel=1e-4)
    assert t["C44"] == pytest.approx(0.17678, rel=1e-4)
    assert t["K_bulk"] < 0.0  # iso-bond point is mechanically UNSTABLE (cold arc finding)
    assert t["Zener_A"] == pytest.approx(1.0, abs=1e-5)


# ─────────────────────────────────────────────────────────────────────────
# SAME-TENSOR-POINT: the saturated map is the cold map with rho -> rho_eff
# ─────────────────────────────────────────────────────────────────────────
def test_saturated_equals_cold_at_matched_rho_eff(net):
    """saturated (S_axial,S_shear) tensor SHAPE + Zener == cold at rho=S_axial/S_shear."""
    pos, bonds, rho = net
    for Sa, Ss in [(0.9927, 0.1019), (0.7, 0.35), (0.99, 0.05), (0.8, 0.2)]:
        t_sat = saturated_tensor(pos, bonds, rho, Sa, Ss)
        from scripts.vol_1_foundations.srs_elastic_tensor import (  # type: ignore
            extract_cubic_Cij,
            moduli_from_Cij,
        )
        rho_eff = Sa / Ss
        r_cold = extract_cubic_Cij(pos, bonds, k_axial=rho_eff, k_shear=1.0, rho=rho)
        m_cold = moduli_from_Cij(r_cold["C11"], r_cold["C12"], r_cold["C44"])
        # scale-free tensor shape (pole-free) must be identical
        assert t_sat["C11"] / t_sat["C44"] == pytest.approx(
            r_cold["C11"] / r_cold["C44"], rel=1e-6)
        assert t_sat["Zener_A"] == pytest.approx(m_cold["Zener_A"], rel=1e-6)


def test_nu_2_7_at_the_crossing_shear_loads(net):
    """SHEAR-LOADS: rho_eff=9.7734 => nu_Hill=2/7, K/G=2, Zener=1.229 (cold-precision)."""
    pos, bonds, rho = net
    sweep = run_sweep(pos, bonds, rho)
    d = sweep["SHEAR_LOADS"]
    assert d["direction"] == "STIFFENING"
    assert d["crosses_rho_star_9.77"] is True
    assert d["nu_Hill_at_crossing"] == pytest.approx(float(NU_VAC), rel=1e-4)
    assert d["KG_Hill_at_crossing"] == pytest.approx(2.0, abs=1e-3)
    assert d["Zener_at_crossing"] == pytest.approx(1.2293, rel=1e-3)


def test_axial_loads_softens_no_crossing(net):
    """AXIAL-LOADS mirror control: SOFTENING, rho_eff->0, never reaches 9.77."""
    pos, bonds, rho = net
    sweep = run_sweep(pos, bonds, rho)
    d = sweep["AXIAL_LOADS"]
    assert d["direction"] == "SOFTENING"
    assert d["crosses_rho_star_9.77"] is False
    assert d["rho_eff_at_yield_limit"] < 1.0


# ─────────────────────────────────────────────────────────────────────────
# The knife: the crossing amplitude is NOT canon-distinguished (value imported)
# ─────────────────────────────────────────────────────────────────────────
def test_crossing_amplitude_not_canon_distinguished(net):
    """A_wall at the 9.77 crossing is NOT sqrt(alpha), NOT 1-alpha, NOT the A->1 wall.
    The value 9.7734 stays GR-imported (the knife holds; no smuggled tuning)."""
    pos, bonds, rho = net
    sweep = run_sweep(pos, bonds, rho)
    cross = sweep["SHEAR_LOADS"]["crossing_A_wall"]
    assert cross is not None
    assert abs(cross - float(np.sqrt(ALPHA))) > 1e-3  # not sqrt(alpha)
    assert abs(cross - (1.0 - ALPHA)) > 1e-3          # not 1-alpha
    assert cross < 0.999                               # not the A->1 yield wall
    # it IS the 518 read-off crossing (consistency with the merged canon)
    assert cross == pytest.approx(A_WALL_518_CROSSING, abs=1e-3)


def test_stability_boundary_scale_invariant(net):
    """sign(K) boundary is set by rho_eff (=2), NOT shifted by saturation magnitude:
    K<0 below rho_eff=2, K>0 above -- the same cold ρ=2 floor, mapped through rho_eff."""
    pos, bonds, rho = net
    # rho_eff just below 2 => K<0; just above => K>0
    below = saturated_tensor(pos, bonds, rho, 0.9, 0.5)   # rho_eff = 1.8
    above = saturated_tensor(pos, bonds, rho, 0.9, 0.4)   # rho_eff = 2.25
    assert below["K_bulk"] < 0.0
    assert above["K_bulk"] > 0.0


# ─────────────────────────────────────────────────────────────────────────
# Two-hand cross-validation + enantiomorph parity
# ─────────────────────────────────────────────────────────────────────────
def test_two_hand_crossval_agrees(net):
    """long-wave least-squares C_ij == [100] direct eigensolve at >=3 points incl crossing."""
    pos, bonds, rho = net
    cv = run_two_hand_crossval(pos, bonds, rho)
    assert cv["ALL_AGREE"] is True
    labels = {p["label"] for p in cv["points"]}
    assert "nu2_7_crossing_rho9.7734" in labels


def test_enantiomorph_parity():
    """Both hands give the SAME saturated C_ij at a prescribed operating point
    (kappa_chiral is saturation-kernel-only; the arc prescribes A)."""
    pos_r, bonds_r, rho_r = srs_primitive("right")
    pos_l, bonds_l, rho_l = srs_primitive("left")
    _, _, Sa, Ss = operating_point(A_WALL_518_CROSSING, True)
    t_r = saturated_tensor(pos_r, bonds_r, rho_r, Sa, Ss)
    t_l = saturated_tensor(pos_l, bonds_l, rho_l, Sa, Ss)
    for k in ("C11", "C12", "C44"):
        assert t_r[k] == pytest.approx(t_l[k], rel=1e-6)


def test_anti_tune_constants_are_readoff_only():
    """RHO_COLD=1 (Ax3), RHO_STAR_IMPORTED=9.7734 + A_WALL_518_CROSSING are read-off
    comparison constants -- the sweep never fits to them."""
    assert RHO_COLD == 1.0
    assert RHO_STAR_IMPORTED == 9.7734
    assert A_WALL_518_CROSSING == 0.99479
    assert A_CORE_SQRT_ALPHA == pytest.approx(float(np.sqrt(ALPHA)), rel=1e-12)
