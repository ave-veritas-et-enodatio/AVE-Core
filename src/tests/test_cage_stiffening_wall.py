"""Keeper: cage stiffening-wall self-focus test (A1 dilatation, crystal_engine.self.V).

Locks in the empirical result of `research/2026-06-13_cage-stiffening-wall_result.md`
(prereg `2026-06-13_cage-stiffening-wall_prereg_FROZEN.md`, Amendments 1 & 2):

  1. CONSISTENCY ANCHOR (the positive) — the bare standing A1-dilatation `self.V`
     SELF-FOCUSES into the persistent breathing cage when seeded with the soliton
     EIGEN-PROFILE (sech): max|A| grows beyond the seed, gamma_bulk_min deepens
     below t=0, and it persists (bounded, no genesis-24 detonation). This confirms
     self.V is the self-trapping grade, CONSISTENT with v14 Mode I (NOT a new cage,
     NOT "scalar beats transverse").
  2. PRIMARY NEGATIVE — the prereg §2 `seed_bulk` GAUSSIAN profile DISPERSES at
     every frac (no growth, no deepening, no critical-frac). The cage's nucleation
     is PROFILE-selective; the Gaussian is not in the breather's basin.
  3. The five-bin classifier is sound (incl. PLANTED-ONLY vs SELF-FOCUS — the F3
     plant-not-create guard, prereg A2.1), proven on synthetic records.

Magnitude is APPARATUS-QUALIFIED, never binned on Γ=−1: A_cap=0.99 floors
gamma_bulk_min at −0.2400 (S^{1/4} index).
"""

import numpy as np
import pytest

from scripts.vol_1_foundations.cage_stiffening_wall import (
    DETONATION_MAX_V,
    classify,
    naive_gamma_floor,
    run_arm,
)


# --------------------------------------------------------------- engine arms
@pytest.fixture(scope="module")
def sech_anchor():
    """v14 consistency anchor: sech eigen-profile, amp 0.85, converter OFF."""
    return run_arm("sech", 0.85, 2.5, False, 400, N=24, dx=0.5, transient_frac=0.5)


@pytest.fixture(scope="module")
def gauss_arm():
    """Prereg §2 seed_bulk Gaussian, frac 0.85, converter OFF (the bare V arm)."""
    return run_arm("gauss", 0.85, 3.0, False, 300, N=37, dx=1.0, transient_frac=0.5)


def test_f0_no_seed_no_wall():
    """F0: no seed -> no wall (a wall without a seed would be a code artifact)."""
    r = run_arm("gauss", 0.0, 3.0, False, 120, N=37, dx=1.0)
    assert abs(r["gamma_min_t0"]) < 1e-9
    assert abs(r["gamma_min_deepest"]) < 1e-3


def test_sech_eigenprofile_self_focuses(sech_anchor):
    """ANCHOR (the positive): the A1 scalar self-focuses from the sech eigen-
    profile — max|A| grows beyond seed AND gamma deepens below t0 AND persists,
    bounded. Consistent with v14 Mode I (self.V is the self-trapping grade)."""
    r = sech_anchor
    assert classify(r) == "SELF-FOCUS", r
    assert r["max_A_peak"] > r["max_A_t0"] * 1.1, "F1: must grow beyond the seed"
    assert r["gamma_min_deepest"] < r["gamma_min_t0"], "F3: wall must deepen below t0"
    assert r["max_A_persist"] > r["max_A_t0"] * 0.5, "must persist as a bound state"
    assert r["max_V_max"] < DETONATION_MAX_V, "F4: bounded, not a genesis-24 pump"


def test_gaussian_seed_bulk_disperses(gauss_arm):
    """PRIMARY NEGATIVE: the prereg §2 seed_bulk Gaussian DISPERSES — it does NOT
    grow beyond the seed and the wall does NOT deepen below t0 (F1-FAIL, F3-FAIL).
    The Gaussian is not in the breather's basin (profile-selective nucleation)."""
    r = gauss_arm
    assert classify(r) == "DISPERSES", r
    assert r["max_A_peak"] <= r["max_A_t0"] * 1.02, "must NOT grow beyond the seed"
    assert r["gamma_min_deepest"] >= r["gamma_min_t0"] - 1e-6, "wall must NOT deepen"
    assert r["max_A_persist"] < r["max_A_t0"] * 0.5, "amplitude must shrink (disperse)"


def test_profile_sensitivity_identical_box():
    """The load-bearing contrast: in the IDENTICAL box at matched amplitude, the
    sech self-focuses and the Gaussian disperses. The discriminator is the seed
    PROFILE, not the amplitude — the 'which seed' finding."""
    sech = run_arm("sech", 0.85, 2.5, False, 300, N=24, dx=0.5)
    gaus = run_arm("gauss", 0.85, 1.25, False, 300, N=24, dx=0.5)  # PML-safe width
    assert classify(sech) == "SELF-FOCUS", sech
    assert classify(gaus) == "DISPERSES", gaus


def test_converter_does_not_rescue_gaussian():
    """S2: the ADD-2 chiral converter (converter_on=True) does NOT make the
    Gaussian self-focus; it still DISPERSES, and converter_work stays bounded
    (energize-LOCK, no runaway)."""
    r = run_arm("gauss", 0.85, 3.0, True, 300, N=37, dx=1.0)
    assert classify(r) == "DISPERSES", r
    assert abs(r["converter_work"]) < 10.0, "converter_work must stay bounded"


def test_clip_floor_apparatus_qualified(sech_anchor):
    """Magnitude is APPARATUS-QUALIFIED: A_cap=0.99 floors gamma_min at −0.2400
    (S^{1/4} index); the deep self-focusing seed sits ON that floor, so the depth
    is bench-limited, NOT physics (never bin on Γ=−1)."""
    fl = naive_gamma_floor(0.05, 0.99)
    assert fl["binds"] == "A_cap"
    assert fl["gamma_floor_S0.25"] == pytest.approx(-0.2400, abs=1e-3)
    assert fl["gamma_floor_S0.50"] == pytest.approx(-0.4539, abs=1e-3)  # exponent-defect FLAG
    # the amp=0.85 sech reaches the clip floor -> magnitude is apparatus-limited
    assert sech_anchor["gamma_min_deepest"] == pytest.approx(fl["gamma_floor_S0.25"], abs=0.01)


# ------------------------------------------------------ classifier soundness
def _rec(**kw):
    base = dict(
        max_A_t0=0.5, max_A_peak=0.5, max_A_persist=0.5,
        gamma_min_t0=-0.018, gamma_min_deepest=-0.018,
        envelope_mid=0.5, envelope_late=0.5, max_V_max=0.5,
    )
    base.update(kw)
    return base


def test_classifier_self_focus():
    assert classify(_rec(max_A_peak=0.9, max_A_persist=0.6, gamma_min_deepest=-0.10)) == "SELF-FOCUS"


def test_classifier_planted_only_is_not_self_focus():
    """THE load-bearing guard (prereg A2.1 / A2.2): a flat planted wall — gamma<0
    at t0 from the seed, max|A| flat, no deepening — is PLANTED-ONLY, NOT
    SELF-FOCUS. The plant-masquerading-as-emergence failure this test exists to
    catch (#215 / CP9)."""
    planted = _rec(max_A_peak=0.5, max_A_persist=0.5, gamma_min_t0=-0.10, gamma_min_deepest=-0.10)
    assert classify(planted) == "PLANTED-ONLY"
    assert classify(planted) != "SELF-FOCUS"


def test_classifier_transient():
    """Grew then decayed (forms-then-decays) = TRANSIENT, distinct from never-formed."""
    assert classify(_rec(max_A_peak=0.9, max_A_persist=0.1, gamma_min_deepest=-0.10,
                         envelope_mid=0.4, envelope_late=0.05)) == "TRANSIENT"


def test_classifier_disperses():
    assert classify(_rec(max_A_peak=0.5, max_A_persist=0.06, gamma_min_deepest=-0.018,
                         envelope_mid=0.1, envelope_late=0.06)) == "DISPERSES"


def test_classifier_detonation_pump_not_self_focus():
    """A2.3: max|A| growing WITH detonation = a pump (genesis-24), NEVER
    SELF-FOCUS. Bounded growth is required for self-focus."""
    det = _rec(max_A_peak=50.0, max_A_persist=30.0, gamma_min_deepest=-0.24, max_V_max=1.0e4)
    assert classify(det) == "DETONATION-PUMP"
    assert classify(det) != "SELF-FOCUS"
