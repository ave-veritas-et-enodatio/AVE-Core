"""
Regression gate for THE MATTER-STIFFENING DERIVATION.

Verdict (frozen prereg research/2026-07-04_matter-stiffening-rho_prereg_FROZEN.md):
  [DRIVES-STIFF-QUALITATIVE] compound [WRONG-DIRECTION] (anti-lean assignment).
    - SHEAR-LOADS: STIFFENING, crosses 9.77 at an ARBITRARY (non-canon) A_wall.
    - AXIAL-LOADS: SOFTENING (control confirms the direction is assignment-set).
    - Radiation control: ρ_eff = ρ_cold identically for all pure-AC drives.

These tests lock the CANON-FORCED composition ρ_eff = ρ_cold·(S_axial/S_shear),
the validation harness, and the honest verdict (crossing amplitude NOT
canon-distinguished — the value 9.77 stays imported).
"""

import numpy as np
import pytest

from ave.axioms.scale_invariant import saturation_factor
from ave.core.constants import ALPHA
from scripts.vol_4_engineering.matter_stiffening_rho import (  # type: ignore
    RHO_COLD,
    RHO_STAR_IMPORTED,
    k_axial_over_k0,
    k_shear_over_k0,
    rho_eff,
    run_derivation,
    run_radiation_control,
    run_validation,
)


def test_validation_harness_all_pass():
    """All validate-on-known checks pass (HALT-gated in the driver)."""
    v = run_validation()
    assert v["ALL_PASS"] is True
    assert v["V1_cold_recovery"]["pass"]
    assert v["V2_symmetric_null"]["pass"]
    assert v["V3_kernel_identity"]["pass"]
    assert v["V4_monotonicity"]["pass"]
    assert v["V5_compliance_inversion_sign"]["pass"]


def test_cold_point_recovers_rho_one():
    """A=0 on both channels ⟹ ρ_eff = 1 (the Ax3-forced cold point, PR#516)."""
    assert rho_eff(np.array(0.0), np.array(0.0)) == pytest.approx(1.0, abs=1e-12)


def test_symmetric_loading_is_identically_cold():
    """S_axial = S_shear ⟹ ρ_eff = ρ_cold IDENTICALLY (radiation-control null)."""
    for A in [0.1, 0.5, 0.9, 0.99, 0.999]:
        assert rho_eff(np.array(A), np.array(A)) == pytest.approx(RHO_COLD, abs=1e-12)


def test_composition_is_canon_forced_S_ratio():
    """ρ_eff = S_axial/S_shear, with k_a/k_0 = S and k_s/k_0 = S from canon maps."""
    A_ax, A_sh = np.array(0.3), np.array(0.7)
    expected = float(saturation_factor(A_ax, yield_limit=1.0)) / float(
        saturation_factor(A_sh, yield_limit=1.0)
    )
    assert float(rho_eff(A_ax, A_sh)) == pytest.approx(expected, rel=1e-12)


def test_axial_stiffness_softens_via_compliance_inversion():
    """k_a/k_0 = C_0/C_eff = S (guards the compliance-inversion sign, prereg §5.5)."""
    for A in [0.1, 0.5, 0.9]:
        assert float(k_axial_over_k0(np.array(A))) == pytest.approx(
            float(saturation_factor(A, yield_limit=1.0)), rel=1e-12
        )


def test_shear_stiffness_softens():
    """k_s/k_0 = G/G_0 = S (canon shear_modulus_ratio)."""
    for A in [0.1, 0.5, 0.9]:
        assert float(k_shear_over_k0(np.array(A))) == pytest.approx(
            float(saturation_factor(A, yield_limit=1.0)), rel=1e-12
        )


def test_shear_loads_stiffens_axial_loads_softens():
    """The DIRECTION is assignment-set: shear-loading stiffens, axial-loading softens."""
    d = run_derivation()
    assert d["SHEAR_LOADS"]["direction"] == "STIFFENING"
    assert d["AXIAL_LOADS"]["direction"] == "SOFTENING"
    assert d["SHEAR_LOADS"]["crosses_rho_star_9.77"] is True
    assert d["AXIAL_LOADS"]["crosses_rho_star_9.77"] is False


def test_9p77_crossing_is_NOT_canon_distinguished():
    """THE KNIFE: the 9.77 crossing lands at an ARBITRARY A_wall — value stays imported."""
    d = run_derivation()
    crossing = d["SHEAR_LOADS"]["crossing"]
    assert crossing is not None
    # The crossing is NOT at √α, NOT at 1−α, NOT at the yield wall A→1.
    assert crossing["canon_distinguished"] is False
    assert not crossing["near_sqrt_alpha"]
    assert not crossing["near_1_minus_alpha"]
    # It sits deep in the near-yield interior (~0.995) but the electron's actual
    # T2 wall is A→1 (S_shear→0), which OVERSHOOTS 9.77 toward infinity.
    assert 0.99 < crossing["A_wall_at_crossing"] < 0.9999


def test_electron_wall_overshoots_9p77():
    """def-vyvsn1 T2 wall at A→1 ⟹ ρ_eff → ∞, badly overshooting 9.77 (not a landing)."""
    S_core = float(saturation_factor(np.sqrt(ALPHA), yield_limit=1.0))
    # As the wall approaches yield, ρ_eff blows up past 9.77.
    rho_deep = S_core / float(saturation_factor(0.99999, yield_limit=1.0))
    assert rho_deep > RHO_STAR_IMPORTED  # overshoots
    assert rho_deep > 100.0  # by a lot — 9.77 is not an attractor


def test_radiation_control_null():
    """Pure-AC ⟨A⟩=0 ⟹ ρ_eff = ρ_cold for all drives (clm-clvchn provenance)."""
    r = run_radiation_control()
    assert r["rho_eff_equals_rho_cold_for_all_AC"] is True
    for entry in r["results"]:
        assert entry["mean_A_time_averaged"] == pytest.approx(0.0, abs=1e-12)
        assert entry["equals_rho_cold"]
