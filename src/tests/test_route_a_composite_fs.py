"""Tests for ROUTE A -- the composite Faddeev-Skyrme neutron build
(research/2026-07-14_route-a-composite-fs_prereg_FROZEN.md).

GATES THAT FIRE ON PLANTS, per the prereg: a refit plant trips the no-refit abort, a seed plant trips
the seed guard, a mint plant trips the provenance guard, an ablation-bypass plant (single-kappa) trips
the ablation gate, and a d-refit plant (verdict on a tuned d) trips the primary-d guard.

This file (prefix test_) is EXEMPT from the EFT magic-number gate, so the frozen HEAD literals live here.
No expected SPLIT value is hard-coded (that would be a refit/seed); structural properties are asserted
against CODATA-anchor-derived bands, so they auto-track the anchors.
"""

from __future__ import annotations

import math
import types

import pytest

from ave.core import constants
from ave.topological.faddeev_skyrme import TopologicalHamiltonian1D
from scripts.vol_2_subatomic import route_a_composite_fs as R
from scripts.vol_2_subatomic.route_a_composite_fs import (
    D_PRIMARY,
    D_SWEEP,
    Split,
    _guarded_split_component,
    ablation_loading,
    classify_bin,
    codata_target,
    composite_energies,
    primary_split,
    route_a_frozen_head_reference,
    run_route_a,
    split_at,
    target_split_me,
)
from scripts.vol_2_subatomic.np_mass_split_gate import forbidden_seeds, no_refit_audit

# ---------------------------------------------------------------------------
# FROZEN HEAD LITERALS -- the prereg-frozen reference (constants.py @ 240d59d8).
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
# No-refit: live == frozen HEAD; refit plant trips the abort
# ---------------------------------------------------------------------------
@pytest.mark.parametrize("name", list(FROZEN_HEAD))
def test_live_constants_equal_frozen_head(name: str) -> None:
    live = float(getattr(constants, name))
    assert math.isclose(live, FROZEN_HEAD[name], rel_tol=1e-12), (
        f"{name} drifted from prereg-frozen HEAD: live={live!r} vs frozen={FROZEN_HEAD[name]!r}"
    )


def test_json_sidecar_matches_frozen_head() -> None:
    ref = route_a_frozen_head_reference()
    for name, val in FROZEN_HEAD.items():
        assert math.isclose(ref[name], val, rel_tol=1e-12), f"{name}: sidecar {ref[name]} vs {val}"
    assert "KAPPA_FS" in ref and "P_C" in ref


def test_no_refit_audit_passes_on_live_module() -> None:
    r = no_refit_audit(constants, reference=route_a_frozen_head_reference())
    assert r.ok, f"no-refit audit failed against frozen HEAD: {r.mismatches}"
    assert math.isclose(r.proton_ratio_reproduced, FROZEN_HEAD["PROTON_ELECTRON_RATIO"], rel_tol=1e-12)


def test_run_route_a_aborts_on_refit(monkeypatch: pytest.MonkeyPatch) -> None:
    """run_route_a() raises NO-REFIT ABORT on a source-level refit of a consumed constant."""
    monkeypatch.setattr(constants, "DELTA_THERMAL", constants.DELTA_THERMAL * 1.10)
    with pytest.raises(RuntimeError, match="NO-REFIT ABORT"):
        run_route_a()


# ---------------------------------------------------------------------------
# The one new capability: solve_composite_trace(0) reduces EXACTLY to the bare
# ---------------------------------------------------------------------------
@pytest.mark.parametrize("kappa_label,attr", [("warm", "KAPPA_FS"), ("cold", "KAPPA_FS_COLD")])
def test_composite_d_zero_reduces_to_bare(kappa_label: str, attr: str) -> None:
    kappa = float(getattr(constants, attr))
    ce = composite_energies(kappa_label, kappa, D_PRIMARY)
    assert ce.d_zero_consistency_ok, "solve_composite_trace(0) must equal solve_scalar_trace() (bare)"


def test_solve_composite_trace_d_zero_matches_solver_directly() -> None:
    l_node = constants.HBAR / (constants.M_E * constants.C_0)
    s = TopologicalHamiltonian1D(node_pitch=l_node, scaling_coupling=constants.KAPPA_FS)
    assert math.isclose(s.solve_composite_trace(0.0, 5), s.solve_scalar_trace(5), rel_tol=1e-9)


def test_composite_surplus_is_positive() -> None:
    """The shift-outward rendering must produce E_comp > E_bare (the canon-required positive surplus)."""
    ce = composite_energies("warm", float(constants.KAPPA_FS), D_PRIMARY)
    assert ce.i_comp > ce.i_bare, "composite FS energy must EXCEED bare -- the elastic-expansion surplus"


# ---------------------------------------------------------------------------
# MINT guard -- fabricated provenance is rejected on the emit path
# ---------------------------------------------------------------------------
def test_mint_plant_is_rejected() -> None:
    with pytest.raises(ValueError, match="MINT VIOLATION"):
        _guarded_split_component("E_elastic", 3.14159, provenance="invented")


def test_canonical_provenance_passes() -> None:
    assert _guarded_split_component("m_e", 1.0, provenance="electron_rest_mass_0_1_unknot") == 1.0
    assert _guarded_split_component("elastic", 7.5, provenance="fs_composite_minus_bare") == 7.5


# ---------------------------------------------------------------------------
# SEED guard -- a component whose VALUE equals the answer is rejected
# ---------------------------------------------------------------------------
@pytest.mark.parametrize("idx", range(5))
def test_seed_plant_is_caught(idx: int) -> None:
    seed = forbidden_seeds(constants)[idx]
    with pytest.raises(ValueError, match="SEED VIOLATION"):
        _guarded_split_component("planted", seed, provenance="fs_composite_minus_bare")


# ---------------------------------------------------------------------------
# ABLATION-BYPASS gate -- a single-kappa "ablation" is rejected
# ---------------------------------------------------------------------------
def test_ablation_requires_two_distinct_kappas() -> None:
    warm = split_at("warm", float(constants.KAPPA_FS), D_PRIMARY)
    # Same kappa relabeled "cold" == a single-kappa bypass.
    fake_cold = Split("cold", float(constants.KAPPA_FS), D_PRIMARY, warm.elastic_me,
                      warm.elastic_me_no_feedback, dict(warm.split_me), warm.sign)
    with pytest.raises(ValueError, match="ABLATION-BYPASS"):
        ablation_loading(warm, fake_cold)


def test_ablation_rejects_mislabeled_pair() -> None:
    warm = split_at("warm", float(constants.KAPPA_FS), D_PRIMARY)
    cold = split_at("cold", float(constants.KAPPA_FS_COLD), D_PRIMARY)
    with pytest.raises(ValueError, match="ABLATION-BYPASS"):
        ablation_loading(cold, warm)  # arguments swapped -> labels wrong


def test_ablation_rejects_mismatched_d() -> None:
    warm = split_at("warm", float(constants.KAPPA_FS), 1.0)
    cold = split_at("cold", float(constants.KAPPA_FS_COLD), 1.5)
    with pytest.raises(ValueError, match="ABLATION-BYPASS"):
        ablation_loading(warm, cold)


def test_ablation_loading_is_computed_and_small() -> None:
    """The delta_th-loading is the DIFFERENCE of two distinct-kappa splits; it is finite and (empirically)
    far smaller than the split itself (the split is delta_th-robust). No magic number asserted."""
    warm = split_at("warm", float(constants.KAPPA_FS), D_PRIMARY)
    cold = split_at("cold", float(constants.KAPPA_FS_COLD), D_PRIMARY)
    abl = ablation_loading(warm, cold)
    for r in ("X", "Y"):
        assert math.isfinite(abl.loading_me[r])
        assert abs(abl.loading_me[r]) < abs(warm.split_me[r]), "loading must be a fraction of the split"


# ---------------------------------------------------------------------------
# D-REFIT gate -- the verdict must consume the Ax1-floor d, never a tuned d
# ---------------------------------------------------------------------------
def test_primary_d_is_ax1_floor() -> None:
    assert D_PRIMARY == 1.0, "the Ax1 transverse-thickness floor fixes d=1.0 l_node"


def test_d_refit_plant_is_caught(monkeypatch: pytest.MonkeyPatch) -> None:
    """Tuning the primary d away from the Ax1 floor (a d-refit) must trip the primary-d guard."""
    monkeypatch.setattr(R, "D_PRIMARY", 0.14)  # a d tuned toward the target band
    with pytest.raises(ValueError, match="D-REFIT VIOLATION"):
        primary_split("warm", float(constants.KAPPA_FS))


# ---------------------------------------------------------------------------
# SIGN -- COMPUTED positive (stronger than the np-gate structural argument)
# ---------------------------------------------------------------------------
def test_sign_is_computed_positive() -> None:
    sp = primary_split("warm", float(constants.KAPPA_FS))
    assert sp.sign == "+", "the composite FS instrument must compute Delta m > 0 (neutron heavier)"


# ---------------------------------------------------------------------------
# BIN classifier -- real chain is bin (iii); bin-flip plants move to i/ii/iv
# ---------------------------------------------------------------------------
def test_real_chain_is_bin_iii() -> None:
    sp = primary_split("warm", float(constants.KAPPA_FS))
    for r in ("X", "Y"):
        b, _ = classify_bin(sp.split_me[r])
        assert b == "iii", f"Reading {r}: expected bin (iii) RIGHT-SIGN-WRONG-MAGNITUDE, got ({b})"


def test_bin_flip_plants() -> None:
    tgt = target_split_me()
    assert classify_bin(tgt)[0] == "i"          # in-band, + -> STRUCTURE
    assert classify_bin(-1.0)[0] == "ii"        # wrong sign
    assert classify_bin(10.0 * tgt)[0] == "iii"  # +, out of band (the real result)
    assert classify_bin(0.0, computable=False)[0] == "iv"  # build-insufficient


def test_bin_ii_consequence_has_frozen_verbatim() -> None:
    _, c = classify_bin(-1.0)
    assert "and it did not" in c and "COINCIDENCE" in c


# ---------------------------------------------------------------------------
# TARGET band + full-run verdict
# ---------------------------------------------------------------------------
def test_codata_target_is_two_point_five_three_one_me() -> None:
    t = codata_target()
    assert t["m_n_minus_m_p_me"] > 0.0
    assert math.isclose(t["m_n_minus_m_p_me"], 2.531, abs_tol=0.01)


def test_full_run_verdict() -> None:
    r = run_route_a()
    assert r["no_refit_ok"] is True
    assert r["headline_bin"] == "iii"
    assert r["sign_computed"] == "+"
    assert r["d_zero_consistency"]["warm"] and r["d_zero_consistency"]["cold"]
    # The split OVER-shoots the 2x band (the pre-registered leaning); no magic number asserted.
    assert r["primary_split"]["warm"]["split_me"]["Y"] > target_split_me() * 2.0
    # d-sweep monotone-increasing in d (structural: bigger displacement -> bigger surplus).
    ys = [r["d_sweep"][d]["warm"]["split_me"]["Y"] for d in D_SWEEP]
    assert ys == sorted(ys), "surplus must increase monotonically with the threading displacement d"
