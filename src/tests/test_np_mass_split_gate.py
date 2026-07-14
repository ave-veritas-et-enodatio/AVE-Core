"""Tests for THE N-P MASS-SPLIT GATE (research/2026-07-13_np-mass-split-gate_prereg.md).

These are GATES THAT FIRE ON PLANTS, per the prereg: a refit plant trips the no-refit abort,
a seed plant trips the no-seed guard, a mint plant trips the provenance guard, and a bin-flip
plant moves the reported bin off (iv) -- proving (iv) is a physics/corpus verdict, not an
instrument that cannot fire.

This file (prefix test_) is EXEMPT from the EFT magic-number gate (verify_universe.py), so it is
where the frozen HEAD reference literals live -- one of the two operative no-refit anchors (the
other is the committed JSON sidecar np_mass_split_gate_frozen_head.json, which the driver's own
run_gate() diffs against on its live path). The driver .py itself hard-codes NO physics number.

Post-review (2026-07-14) additions: the gate-wiring repairs (R3/R5/R6/R8) are exercised here --
run_gate() now catches a source-level DELTA_THERMAL / KAPPA_FS_COLD refit on its OWN live path
(not only via the exempt test), the mint+seed guards are wired into the emitted component, and the
corpus-state detector flips off (iv) if a derived neutron mass appears.
"""

from __future__ import annotations

import math
import types

import pytest

from ave.core import constants
from scripts.vol_2_subatomic import np_mass_split_gate as G
from scripts.vol_2_subatomic.np_mass_split_gate import (
    CONSUMED_CONSTANTS,
    MagnitudeResult,
    _guarded_component,
    assert_no_seed,
    classify_bin,
    codata_target,
    corpus_has_derived_neutron_mass,
    forbidden_seeds,
    frozen_head_reference,
    magnitude_computability_leg,
    no_refit_audit,
    provenance_guarded_magnitude,
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
# The two frozen anchors agree (test-file literals vs the committed JSON sidecar)
# ---------------------------------------------------------------------------
def test_json_sidecar_matches_test_frozen_head() -> None:
    ref = frozen_head_reference()
    for name, val in FROZEN_HEAD.items():
        assert name in ref, f"{name} missing from JSON sidecar"
        assert math.isclose(ref[name], val, rel_tol=1e-12), f"{name}: sidecar {ref[name]} vs test {val}"
    # The sidecar additionally carries the derived KAPPA_FS + P_C (audited by run_gate's consistency check).
    assert "KAPPA_FS" in ref and "P_C" in ref


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
    r = no_refit_audit(constants)  # default reference is now the frozen JSON sidecar
    assert r.ok, f"no-refit audit failed against frozen HEAD: {r.mismatches}"
    assert math.isclose(r.proton_ratio_reproduced, FROZEN_HEAD["PROTON_ELECTRON_RATIO"], rel_tol=1e-12)
    assert math.isclose(r.proton_ratio_reproduced, r.proton_ratio_live, rel_tol=1e-12)


def _refit_plant(name: str, factor: float) -> types.SimpleNamespace:
    """A stand-in constants source with ONE consumed constant refit (mutated)."""
    ns = types.SimpleNamespace()
    for attr in (*CONSUMED_CONSTANTS, "P_C", "KAPPA_FS"):
        setattr(ns, attr, float(getattr(constants, attr)))
    setattr(ns, name, float(getattr(constants, name)) * factor)
    return ns


@pytest.mark.parametrize("name", list(FROZEN_HEAD))  # all SIX consumed constants (review R5)
def test_refit_plant_trips_the_abort(name: str) -> None:
    """Mutating any consumed constant (a refit) must be caught by the no-refit audit vs frozen HEAD."""
    plant = _refit_plant(name, factor=1.0 + 1e-6)  # a 1 ppm refit
    r = no_refit_audit(plant, reference=frozen_head_reference())
    assert not r.ok, f"refit plant on {name} was NOT caught -- the no-refit gate is dead"
    caught = {m[0] for m in r.mismatches}
    assert any(name in c for c in caught), f"{name} refit not in mismatches {caught}"


@pytest.mark.parametrize("name", ["DELTA_THERMAL", "KAPPA_FS_COLD"])
def test_run_gate_aborts_on_source_level_refit_of_focal_constants(
    name: str, monkeypatch: pytest.MonkeyPatch
) -> None:
    """R5/R8 fix: run_gate()'s OWN live path now trips on a source-level refit of the audit's focal
    constants (DELTA_THERMAL, KAPPA_FS_COLD) -- which the old self-snapshot default could NOT catch.
    """
    monkeypatch.setattr(constants, name, float(getattr(constants, name)) * 1.10)  # 10% source refit
    with pytest.raises(RuntimeError, match="NO-REFIT ABORT"):
        run_gate()


def test_run_gate_aborts_on_refit(monkeypatch: pytest.MonkeyPatch) -> None:
    """run_gate() raises NO-REFIT ABORT when I_SCALAR_1D is refit (caught by both diff + reproduction)."""
    monkeypatch.setattr(constants, "I_SCALAR_1D", constants.I_SCALAR_1D * 1.001)
    with pytest.raises(RuntimeError, match="NO-REFIT ABORT"):
        run_gate()


def test_kappa_fs_consistency_refit_is_caught() -> None:
    """A KAPPA_FS that no longer equals KAPPA_FS_COLD*(1-DELTA_THERMAL) is caught (consistency check)."""
    plant = _refit_plant("KAPPA_FS", factor=1.0 + 1e-3)
    r = no_refit_audit(plant, reference=frozen_head_reference())
    assert not r.ok
    assert any("KAPPA_FS" in m[0] for m in r.mismatches)


# ---------------------------------------------------------------------------
# HARD RAIL 4 -- no-seed guard (fires on a planted, answer-derived seed)
# ---------------------------------------------------------------------------
def test_forbidden_seeds_are_answer_derived() -> None:
    seeds = forbidden_seeds(constants)
    assert any(1830.0 < s < 1840.0 for s in seeds)  # proton ratio
    assert any(1.28 < s < 1.30 for s in seeds)      # split MeV
    assert any(2.50 < s < 2.56 for s in seeds)      # split m_e
    assert any(939.0 < s < 940.0 for s in seeds)    # neutron mass


@pytest.mark.parametrize("idx", range(5))
def test_seed_plant_is_caught(idx: int) -> None:
    seed = forbidden_seeds(constants)[idx]
    with pytest.raises(ValueError, match="SEED VIOLATION"):
        assert_no_seed(seed, label="planted_input")


def test_non_seed_value_passes() -> None:
    assert assert_no_seed(float(constants.P_C), label="p_c") == float(constants.P_C)


# ---------------------------------------------------------------------------
# HARD RAIL 1+3 -- mint guard (fires on a fabricated elastic-tension constant)
# ---------------------------------------------------------------------------
def test_mint_plant_is_rejected() -> None:
    with pytest.raises(ValueError, match="MINT VIOLATION"):
        provenance_guarded_magnitude("E_elastic", 1.531, provenance="invented")


def test_canonical_provenance_passes() -> None:
    assert provenance_guarded_magnitude(
        "m_e_threaded", 1.0, provenance="electron_rest_mass_0_1_unknot"
    ) == 1.0


# ---------------------------------------------------------------------------
# R3/R6b -- guards are WIRED INTO THE LIVE PATH (not plant-only): the single
# _guarded_component gateway that every emitted split component passes.
# ---------------------------------------------------------------------------
def test_guarded_component_passes_canonical() -> None:
    assert _guarded_component("m_e", 1.0, provenance="electron_rest_mass_0_1_unknot") == 1.0


def test_guarded_component_rejects_mint() -> None:
    with pytest.raises(ValueError, match="MINT VIOLATION"):
        _guarded_component("E_elastic", 1.531, provenance="invented")


def test_guarded_component_rejects_seed() -> None:
    """A component whose VALUE is the answer (2.531 m_e) is rejected even with canonical provenance."""
    seed = forbidden_seeds(constants)[3]  # split ~2.531 m_e
    with pytest.raises(ValueError, match="SEED VIOLATION"):
        _guarded_component("planted_split", seed, provenance="electron_rest_mass_0_1_unknot")


def test_magnitude_leg_emits_only_guarded_components(monkeypatch: pytest.MonkeyPatch) -> None:
    """The live magnitude leg routes its emitted component through the guard gateway (R3)."""
    calls: list[tuple[str, float, str]] = []
    real = G._guarded_component

    def spy(name: str, value: float, provenance: str) -> float:
        calls.append((name, value, provenance))
        return real(name, value, provenance)

    monkeypatch.setattr(G, "_guarded_component", spy)
    G.magnitude_computability_leg()
    assert calls, "magnitude leg did not route its emitted component through the guard gateway"


# ---------------------------------------------------------------------------
# R6c -- corpus-state DETECTOR: bin (iv) flips if a derived neutron mass appears
# ---------------------------------------------------------------------------
def test_detector_clean_on_current_corpus() -> None:
    assert corpus_has_derived_neutron_mass(constants) is False


def test_detector_fires_if_derived_neutron_mass_appears(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(constants, "M_N_MEV_AVE", 939.0, raising=False)
    assert corpus_has_derived_neutron_mass(constants) is True
    with pytest.raises(RuntimeError, match="CORPUS-STATE CHANGE"):
        magnitude_computability_leg(constants)


# ---------------------------------------------------------------------------
# LEG B -- sign sub-finding: forced positive + the STRONGER beta-decay bound
# ---------------------------------------------------------------------------
def test_sign_is_forced_positive() -> None:
    s = sign_leg()
    assert s.sign_delta_m == "+", "canonical construction must force neutron heavier"
    assert s.threaded_electron_rest_mass_me >= 0.0
    assert s.elastic_strain_sign.startswith(">= 0")


def test_sign_carries_c2_conditionality_and_beta_decay_bound() -> None:
    """R2: the positivity argument is conditional on C2; the beta-decay bound is stronger + C2-immune."""
    s = sign_leg()
    assert "C2" in s.conditionality
    assert s.beta_decay_lower_bound_me == 1.000  # Delta m > 1.000 m_e, stronger than sign-only
    assert "spontaneous" in s.beta_decay_bound_basis or "exothermic" in s.beta_decay_bound_basis


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
    # R1: C5 is relabeled UNDETERMINED (not 'new assumption'); the KEEP-BOTH tag preserves the old.
    c5 = mag.missing_choices[4]
    assert "UNDETERMINED" in c5 and "KEEP-BOTH" in c5


def test_bin_flip_plant_moves_off_iv() -> None:
    """Force a computable finite split (a bin-flip plant): the classifier must leave (iv)."""
    tgt = target_split_me()
    assert classify_bin(MagnitudeResult(True, {}, [], tgt, []))[0] == "i"          # in-band, +
    assert classify_bin(MagnitudeResult(True, {}, [], -1.0, []))[0] == "ii"        # wrong sign
    assert classify_bin(MagnitudeResult(True, {}, [], 10.0 * tgt, []))[0] == "iii"  # +, out of band


def test_bin_ii_consequence_is_full_frozen_verbatim() -> None:
    """R7: the driver's bin-(ii) string restores the full prereg frozen text (epic-40 sentence)."""
    _, consequence = classify_bin(MagnitudeResult(True, {}, [], -1.0, []))
    assert "and it did not" in consequence
    assert "epic-40" in consequence
    assert "proton-specific tightness = COINCIDENCE" in consequence


# ---------------------------------------------------------------------------
# TARGET band sanity + full-gate verdict
# ---------------------------------------------------------------------------
def test_codata_target_is_two_point_five_three_one_me() -> None:
    t = codata_target()
    assert t["m_n_minus_m_p_me"] > 0.0
    assert math.isclose(t["m_n_minus_m_p_me"], target_split_me(), rel_tol=1e-12)
    assert math.isclose(t["m_n_minus_m_p_me"], 2.531, abs_tol=0.01)


def test_full_gate_verdict_is_iv_positive_sign() -> None:
    r = run_gate()
    assert r["no_refit_ok"] is True
    assert r["bin"] == "iv"
    assert r["sign_delta_m"] == "+"
    assert r["beta_decay_lower_bound_me"] == 1.000
    assert r["computable"] is False
    assert r["computed_split_me"] is None
