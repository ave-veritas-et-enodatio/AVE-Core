"""Tests for the F6 floor-battery — pre-occupied-bath meter revalidation (STAGE 1).

Result: research/2026-07-19_f6-floor-battery_result.md
Data:   research/2026-07-19_f6-floor-battery_result.json
Driver: src/scripts/vol_1_foundations/f6_floor_battery.py
Charter: research/2026-07-16_f6-bath-meter_CHARTER.md §D + §D-post (FROZEN)
Instrument: src/ave/thermal/f6_bath_meter.py (BYTE-UNTOUCHED; floor = config-only)

These tests LOCK the STAGE-1 verdict FLOOR-METER-VALID-BAND[0,5]:

  (a) ★INDEPENDENT re-derivation of the verdict from the RAW banked per-ρ series
      (NOT the driver's own fb1_ok/fb2_ok/verdict booleans — the #726 F9 lesson):
      the clean-floor band top ρ_hi=5; FB1-FB5 pass in-band; frozen-literal =
      FLOOR-LEDGER-ARTIFACT (both-ways honesty record); FB4 CoV bounded.
  (b) ★LIVE floor-seed checks (config-only; meter BYTE-UNTOUCHED): the seed returns
      exactly M*e_floor_per_mode; ρ=0 is BIT-IDENTICAL to un-seeded (FB5); an in-band
      cell keeps the identity <1e-6; the band edge is real (a high-ρ near-discharge
      comb degrades). Locks the genuine finding, not the classifier's word.

Locking both the valid-band AND the band edge prevents a silent rescue (Rule 11).
NO meter file is edited. Fast (banked JSON + short live cells).
"""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import numpy as np
import pytest

_REPO = Path(__file__).resolve().parents[2]
_DRIVER = _REPO / "src" / "scripts" / "vol_1_foundations" / "f6_floor_battery.py"
_JSON = _REPO / "research" / "2026-07-19_f6-floor-battery_result.json"

LEDGER_ID_TOL = 1e-6
MACHINE_TOL = 1e-10
COV_CHAOS = 1.0


@pytest.fixture(scope="module")
def bat():
    spec = importlib.util.spec_from_file_location("f6_floor_battery", _DRIVER)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = mod  # required so @dataclass can resolve the module
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture(scope="module")
def banked():
    assert _JSON.exists(), f"banked battery JSON missing: {_JSON}"
    return json.loads(_JSON.read_text())


# --- (a) INDEPENDENT re-derivation from the RAW banked per-ρ series ---------------
def test_independent_band_top_from_raw(banked):
    """ρ_hi re-derived from the raw per-ρ clean ingredients (identity<tol ∧ no over-tx
    ∧ no clamp), NOT from the banked rho_hi/verdict. Must equal 5."""
    per_rho = banked["fb_primary"]["per_rho"]
    rho_hi = 0.0
    for pr in per_rho:
        clean = (pr["max_drift"] < LEDGER_ID_TOL
                 and pr["n_over_transfer"] == 0 and pr["n_clamp"] == 0
                 and pr["n_identity_fail"] == 0 and pr["non_secular_all"])
        if clean:
            rho_hi = pr["rho"]
        else:
            break
    assert rho_hi == 5.0
    assert banked["fb_primary"]["rho_hi"] == rho_hi  # reconcile banked vs re-derived


def test_independent_fb_pass_in_band(banked):
    """FB1/FB2/FB3 hold at every in-band ρ from the raw fields (identity, excess-
    identity, seed-exact, c finite, forms agree)."""
    for pr in banked["fb_primary"]["per_rho"]:
        if pr["rho"] > 5.0:
            continue
        assert pr["max_drift"] < LEDGER_ID_TOL            # FB1 identity
        assert pr["max_excess_identity"] < LEDGER_ID_TOL  # FB2 D2 identity
        assert pr["seed_exact"] is True                   # FB2 seed exact
        assert pr["c_finite_all"] is True                 # FB3 corrected tare
        assert pr["c_form_diff_max"] < 0.02               # FB3 forms agree
        assert pr["n_occ_excess_min"] >= 0


def test_fb4_statistics_not_realization_raw(banked):
    """FB4 (Dp-2): realizations differ, excess-plateau CoV bounded (<1.0, not chaotic),
    ensemble mean is the stable read. The pairwise CoV<0.10 is the FROZEN-LITERAL gate
    (banked False) — NOT the corrected pass condition."""
    fb4 = banked["fb4"]
    assert fb4["realization_differs"] is True
    assert fb4["cov_bounded"] is True
    for r in fb4["rows"]:
        assert r["realization_maxdiff"] > 0.0            # realizations differ
        assert np.isfinite(r["excess_plateau_cov"]) and r["excess_plateau_cov"] < COV_CHAOS
        assert r["frozen_literal_cov_ok"] is False       # the too-tight literal gate
    assert fb4["arm_ensemble_budget_cov"] > 0.10          # the arm inherits a real spread


def test_fb5_cold_bitforbit_raw(banked):
    """FB5: ρ=0 seed no-op ⇒ bit-identical on BOTH combs (max ΔE_bath = 0.0)."""
    for cc in banked["fb5"]:
        assert cc["max_ebath_diff"] == 0.0
        assert cc["bit_for_bit"] is True


def test_frozen_literal_artifact_banked(banked):
    """The both-ways honesty record: the UN-amended §D.D3 binary criteria return
    FLOOR-LEDGER-ARTIFACT (banked), and the corrected verdict is the band."""
    assert banked["frozen_literal"]["verdict"] == "FLOOR-LEDGER-ARTIFACT"
    assert banked["frozen_literal"]["fb3_range_ok"] is False
    assert banked["verdict"] == "FLOOR-METER-VALID-BAND[0,5]"


def test_boundary_comb_edge_banked(banked):
    """The narrow-band boundary comb Δω=0.030: clean at ρ≤2, BREAKS at ρ=3 (clamp) —
    the band width grows as the comb transfers less (the mechanism)."""
    rows = {r["rho"]: r for r in banked["boundary_doc"]["rows"]}
    assert rows[1.0]["all_clean"] is True
    assert rows[2.0]["all_clean"] is True
    assert rows[3.0]["all_clean"] is False
    assert rows[3.0]["n_clamp"] >= 1


# --- (b) LIVE config-only floor-seed checks (meter BYTE-UNTOUCHED) ----------------
def test_live_seed_returns_exact_floor_energy(bat):
    """The config-only seed sets each mode to EXACTLY e_floor_per_mode: the returned
    bath energy == M*e_floor_per_mode to machine precision (meter untouched)."""
    from scripts.vol_1_foundations.f6_counting_arrow_arm import _build, _m_for
    dw = bat.DVW
    m = _m_for(dw)
    cpl = _build(dw, m, kappa=bat.KAPPA, scale=bat.SCALE_MILD)
    efm = 0.05
    ret = bat.seed_floor(cpl.bath, efm, bat.FLOOR_SEED)
    assert abs(ret - m * efm) < MACHINE_TOL
    # per-mode energies are all exactly efm
    e_m = cpl.bath.mode_energy()
    assert float(np.abs(e_m - efm).max()) < MACHINE_TOL


def test_live_rho0_is_noop_bitidentical(bat):
    """ρ=0 (e_floor_per_mode=0) is a NO-OP: bath stays zero, seed returns 0.0."""
    from scripts.vol_1_foundations.f6_counting_arrow_arm import _build, _m_for
    dw = bat.DVW
    cpl = _build(dw, _m_for(dw), kappa=bat.KAPPA, scale=bat.SCALE_MILD)
    ret = bat.seed_floor(cpl.bath, 0.0, bat.FLOOR_SEED)
    assert ret == 0.0
    assert float(np.abs(cpl.bath.x).max()) == 0.0
    assert float(np.abs(cpl.bath.p).max()) == 0.0


def test_live_inband_identity_holds(bat):
    """A live in-band cell (Δω=0.050, ρ=3) keeps the conservation identity <1e-6."""
    r = bat.run_floor_comb(bat.DVW, 3.0, seed=bat.FLOOR_SEED)
    assert r.max_cons_drift < LEDGER_ID_TOL
    assert r.clamped is False
    assert r.over_transfer is False


def test_live_band_edge_is_real(bat):
    """The band edge is REAL, not a label: a near-discharge comb (Δω=0.030) at ρ=3
    degrades for at least one seed (clamp OR identity break) — this is what single-seed
    FB1 masked and multi-seed FB caught."""
    degraded = False
    for s in bat.SEEDS:
        r = bat.run_floor_comb(bat.BOUNDARY_COMB, 3.0, seed=s)
        if r.clamped or r.max_cons_drift >= LEDGER_ID_TOL or r.over_transfer:
            degraded = True
            break
    assert degraded, "expected the Δω=0.030 comb to degrade at ρ=3 for some seed"
