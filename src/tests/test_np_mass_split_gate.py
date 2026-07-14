"""Tests for THE N-P MASS-SPLIT GATE (research/2026-07-13_np-mass-split-gate_prereg.md).

These are GATES THAT FIRE ON PLANTS, per the prereg: a refit plant trips the no-refit abort,
a seed plant trips the no-seed guard, a mint plant trips the provenance guard, and a bin-flip
plant moves the reported bin off (iv) -- proving (iv) is a physics/corpus verdict, not an
instrument that cannot fire.

This file (prefix test_) is EXEMPT from the EFT magic-number gate (verify_universe.py), so it is
where the frozen HEAD reference literals live -- the authoritative prereg-vs-HEAD no-refit anchor.
The driver itself hard-codes NO physics number (it imports/derives all of them).
"""

from __future__ import annotations

import math
import types

import pytest

from ave.core import constants
from scripts.vol_2_subatomic.np_mass_split_gate import (
    CONSUMED_CONSTANTS,
    MagnitudeResult,
    assert_no_seed,
    classify_bin,
    codata_target,
    forbidden_seeds,
    magnitude_computability_leg,
    no_refit_audit,
    provenance_guarded_magnitude,
    reference_from_constants,
    run_gate,
    sign_leg,
    target_split_me,
)

# ---------------------------------------------------------------------------
# FROZEN HEAD LITERALS -- the prereg-frozen reference (constants.py @ 9bfc50ef).
# This is the no-refit anchor; a drift of ANY consumed constant is caught below.
# ---------------------------------------------------------------------------
FROZEN_HEAD: dict[str, float] = {
    "I_SCALAR_1D": 1161.9870305252678,
    "V_TOROIDAL_HALO": 2.0,
    "ALPHA": 7.2973525693e-3,
    "KAPPA_FS_COLD": 8.0 * math.pi,
    "DELTA_THERMAL": 1.0 / (14.0 * math.pi**2),
    "PROTON_ELECTRON_RATIO": 1836.1170402290593,
}


# ---------------------------------------------------------------------------
# LEG A -- no-refit: live == frozen HEAD (the prereg-vs-HEAD assertion)
# ---------------------------------------------------------------------------
@pytest.mark.parametrize("name", list(FROZEN_HEAD))
def test_live_constants_equal_frozen_head(name: str) -> None:
    """Every consumed constant on the live module still equals the prereg-frozen HEAD literal."""
    live = float(getattr(constants, name))
    assert math.isclose(live, FROZEN_HEAD[name], rel_tol=1e-12), (
        f"{name} drifted from prereg-frozen HEAD: live={live!r} vs frozen={FROZEN_HEAD[name]!r}"
    )


def test_consumed_set_matches_frozen_keys() -> None:
    assert set(CONSUMED_CONSTANTS) == set(FROZEN_HEAD)


def test_no_refit_audit_passes_on_live_module() -> None:
    r = no_refit_audit(constants, reference=FROZEN_HEAD)
    assert r.ok, f"no-refit audit failed against frozen HEAD: {r.mismatches}"
    assert math.isclose(r.proton_ratio_reproduced, FROZEN_HEAD["PROTON_ELECTRON_RATIO"], rel_tol=1e-12)
    assert math.isclose(r.proton_ratio_reproduced, r.proton_ratio_live, rel_tol=1e-12)


def _refit_plant(name: str, factor: float) -> types.SimpleNamespace:
    """A stand-in constants source with ONE consumed constant refit (mutated)."""
    ns = types.SimpleNamespace()
    for attr in (*CONSUMED_CONSTANTS, "P_C"):
        setattr(ns, attr, float(getattr(constants, attr)))
    setattr(ns, name, float(getattr(constants, name)) * factor)
    return ns


@pytest.mark.parametrize("name", ["I_SCALAR_1D", "V_TOROIDAL_HALO", "ALPHA", "DELTA_THERMAL"])
def test_refit_plant_trips_the_abort(name: str) -> None:
    """Mutating any consumed constant (a refit) must be caught by the no-refit audit vs frozen HEAD."""
    plant = _refit_plant(name, factor=1.0 + 1e-6)  # a 1 ppm refit
    r = no_refit_audit(plant, reference=FROZEN_HEAD)
    assert not r.ok, f"refit plant on {name} was NOT caught -- the no-refit gate is dead"
    caught = {m[0] for m in r.mismatches}
    assert any(name in c for c in caught), f"{name} refit not in mismatches {caught}"


def test_run_gate_aborts_on_refit(monkeypatch: pytest.MonkeyPatch) -> None:
    """run_gate() raises NO-REFIT ABORT when a consumed constant is refit (caught by reproduction)."""
    # Mutate I_SCALAR_1D only; the live reproduction I_scalar/(1-V*p_c)+1 no longer matches
    # the (unchanged) PROTON_ELECTRON_RATIO -> the default snapshot audit trips.
    monkeypatch.setattr(constants, "I_SCALAR_1D", constants.I_SCALAR_1D * 1.001)
    with pytest.raises(RuntimeError, match="NO-REFIT ABORT"):
        run_gate()


# ---------------------------------------------------------------------------
# HARD RAIL 4 -- no-seed guard (fires on a planted, answer-derived seed)
# ---------------------------------------------------------------------------
def test_forbidden_seeds_are_answer_derived() -> None:
    """The forbidden-seed set tracks the CODATA anchors (proton ratio, split, neutron mass)."""
    seeds = forbidden_seeds(constants)
    # proton ratio ~1836, split ~1.293 MeV, split ~2.531 m_e, neutron ~939.565 MeV all present
    assert any(1830.0 < s < 1840.0 for s in seeds)
    assert any(1.28 < s < 1.30 for s in seeds)
    assert any(2.50 < s < 2.56 for s in seeds)
    assert any(939.0 < s < 940.0 for s in seeds)


@pytest.mark.parametrize("idx", range(5))
def test_seed_plant_is_caught(idx: int) -> None:
    seed = forbidden_seeds(constants)[idx]
    with pytest.raises(ValueError, match="SEED VIOLATION"):
        assert_no_seed(seed, label="planted_input")


def test_non_seed_value_passes() -> None:
    # A legitimate non-target value (p_c) flows through untouched.
    assert assert_no_seed(float(constants.P_C), label="p_c") == float(constants.P_C)


# ---------------------------------------------------------------------------
# HARD RAIL 1+3 -- mint guard (fires on a fabricated elastic-tension constant)
# ---------------------------------------------------------------------------
def test_mint_plant_is_rejected() -> None:
    """A fabricated E_elastic with non-canonical provenance must be refused."""
    with pytest.raises(ValueError, match="MINT VIOLATION"):
        provenance_guarded_magnitude("E_elastic", 1.531, provenance="invented")


def test_canonical_provenance_passes() -> None:
    # The threaded electron rest mass IS canonical -> allowed.
    assert provenance_guarded_magnitude(
        "m_e_threaded", 1.0, provenance="electron_rest_mass_0_1_unknot"
    ) == 1.0


# ---------------------------------------------------------------------------
# LEG B -- sign sub-finding: forced positive
# ---------------------------------------------------------------------------
def test_sign_is_forced_positive() -> None:
    s = sign_leg()
    assert s.sign_delta_m == "+", "canonical construction must force neutron heavier"
    assert s.threaded_electron_rest_mass_me >= 0.0
    assert s.elastic_strain_sign.startswith(">= 0")


# ---------------------------------------------------------------------------
# LEG C + bin classifier -- (iv) on the real chain; bin-flip plant fires off (iv)
# ---------------------------------------------------------------------------
def test_real_chain_is_bin_iv() -> None:
    mag = magnitude_computability_leg()
    assert not mag.computable
    assert mag.computed_split_me is None
    bin_id, _ = classify_bin(mag)
    assert bin_id == "iv", "the canonical neutron construction must land bin (iv) CHAIN-INSUFFICIENT"
    assert len(mag.missing_choices) >= 5  # the deliverable for bin (iv)


def test_bin_flip_plant_moves_off_iv() -> None:
    """Force a computable finite split (a bin-flip plant): the classifier must leave (iv).

    Proves (iv) is a physics/corpus verdict, not an instrument that cannot fire a magnitude bin.
    """
    tgt = target_split_me()
    assert classify_bin(MagnitudeResult(True, {}, [], tgt, []))[0] == "i"          # in-band, +
    assert classify_bin(MagnitudeResult(True, {}, [], -1.0, []))[0] == "ii"        # wrong sign
    assert classify_bin(MagnitudeResult(True, {}, [], 10.0 * tgt, []))[0] == "iii"  # +, out of band


# ---------------------------------------------------------------------------
# TARGET band sanity -- the CODATA anchor is +2.531 m_e (naming only)
# ---------------------------------------------------------------------------
def test_codata_target_is_two_point_five_three_one_me() -> None:
    t = codata_target()
    assert t["m_n_minus_m_p_me"] > 0.0, "the experimental split is neutron-heavier (+)"
    assert math.isclose(t["m_n_minus_m_p_me"], target_split_me(), rel_tol=1e-12)
    assert math.isclose(t["m_n_minus_m_p_me"], 2.531, abs_tol=0.01), (
        f"target naming drifted: {t['m_n_minus_m_p_me']}"
    )


def test_full_gate_verdict_is_iv_positive_sign() -> None:
    r = run_gate()
    assert r["no_refit_ok"] is True
    assert r["bin"] == "iv"
    assert r["sign_delta_m"] == "+"
    assert r["computable"] is False
    assert r["computed_split_me"] is None
