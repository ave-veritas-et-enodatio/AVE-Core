"""Tests for the F6 NO-FULL-DISCHARGE calibration scan (Phase 0).

Finding: research/2026-07-19_f6-no-discharge-scan_INSTRUMENT-INCOMPATIBLE.md
Data:    research/2026-07-19_f6-no-discharge-scan_result.json
Driver:  src/scripts/vol_1_foundations/f6_no_discharge_scan.py
Instrument: src/ave/thermal/f6_bath_meter.py (BYTE-UNTOUCHED)

These tests LOCK the Phase-0 negative (outcome (c) INSTRUMENT-INCOMPATIBLE):

  (a) ★the (kappa, g0) BIT-IDENTICAL degeneracy — coupling enters only as kappa*g0
      (f6_bath_meter.py:198), so g0-scaling IS kappa-scaling and a g0<1.0 cell runs
      OUTSIDE the certified [0.030,0.030] band (the central scope finding, live);
  (b) ★the in-scope full-discharge fact — the densest certified comb (g0=1.0,
      Delta_omega=0.010) drives E_bath -> ~E0 and E_lat -> ~0 (the clamp precursor), live;
  (c) ★the INDEPENDENT re-derivation of the outcome from the RAW banked series
      (NOT the driver's own satisfies_scan/n_usable/outcome booleans — the #726 F9
      lesson): USABLE cells = 0 => C_INSTRUMENT_INCOMPATIBLE; every in-scope
      quasi-continuum comb clamps; the lone raw-satisfier is doubly disqualified.

Locking the negative prevents a silent rescue (Rule 11). NO meter file is edited.
All tests are fast (no full-scan re-run; the banked JSON carries the grid).
"""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import numpy as np
import pytest

_REPO = Path(__file__).resolve().parents[2]
_DRIVER = _REPO / "src" / "scripts" / "vol_1_foundations" / "f6_no_discharge_scan.py"
_JSON = _REPO / "research" / "2026-07-19_f6-no-discharge-scan_result.json"

KAPPA_CERT = 0.030  # the certified single-point band [0.030,0.030]
NOCC_GATE = 10      # inherited #726 frozen regime gate
T63_GATE = 0.5
PEAK_MAX = 0.85


@pytest.fixture(scope="module")
def scan():
    spec = importlib.util.spec_from_file_location("f6_no_discharge_scan", _DRIVER)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = mod  # required so @dataclass can resolve the module
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture(scope="module")
def banked():
    assert _JSON.exists(), f"banked scan JSON missing: {_JSON}"
    return json.loads(_JSON.read_text())


# --- (a) the central scope finding: (kappa,g0) bit-identical degeneracy (live) ----
def test_kappa_g0_degeneracy_bit_identical(scan):
    """(kappa=0.030, g0=0.5) is BIT-FOR-BIT identical to (kappa=0.015, g0=1.0) — the
    coupling enters the meter only as kappa*g0. So g0-scaling IS kappa-scaling; a
    g0<1.0 'no-discharge' cell runs at kappa_eff<0.030, OFF the certified instrument."""
    d = scan.degeneracy_check()
    assert d["bit_identical"] is True
    assert d["max_ebath_absdiff"] == 0.0
    assert d["max_elat_absdiff"] == 0.0
    assert d["e0_match"] is True
    assert d["n_occ_match"] is True


def test_in_scope_only_at_g0_one(scan):
    """kappa_eff == KAPPA (in scope) iff g0 == 1.0; any g0 < 1.0 exits the band."""
    dummy = scan.ScanCell  # noqa: F841 — presence check
    assert abs(scan.KAPPA * 1.0 - KAPPA_CERT) < 1e-12
    for g0 in (0.7, 0.5, 0.35, 0.25):
        assert scan.KAPPA * g0 < KAPPA_CERT - 1e-9


# --- (b) the in-scope full-discharge fact (live, short horizon) --------------------
def test_in_scope_densest_fully_discharges(scan):
    """The densest CERTIFIED comb (g0=1.0, Delta_omega=0.010, kappa_eff=0.030) drives
    E_bath -> ~E0 (peak > 0.85, i.e. NOT partial) and E_lat -> ~0 within one recurrence
    — the clamp precursor. Locks the in-scope no-partial-transfer fact cheaply."""
    dw, m = 0.010, scan._m_for(0.010)
    cpl = scan._build_scan(dw, m, g0=1.0, kappa=scan.KAPPA)
    e0 = cpl.e_lat()
    peak = 0.0
    min_elat = e0
    for k in range(int(round(2 * np.pi / dw))):  # ~1 recurrence
        cpl.step(k + 1)
        peak = max(peak, cpl.e_bath())
        min_elat = min(min_elat, cpl.e_lat())
    assert peak / e0 > PEAK_MAX, f"expected full discharge, got peak_frac={peak / e0:.3f}"
    assert min_elat / e0 < 0.05, f"expected near-drained lattice, min E_lat/E0={min_elat / e0:.3e}"


# --- (c) INDEPENDENT re-derivation from the RAW banked series (F9 lesson) ----------
def test_independent_rederivation_no_usable_cell(banked):
    """Re-derive the outcome from the RAW per-cell numbers ONLY (kappa_eff, peak_frac,
    t63_over_trec, n_occ, clamp_fires) — NOT the driver's satisfies_scan / n_usable /
    outcome booleans. A USABLE cell must be in-scope AND transfer-live AND partial AND
    clamp-never AND reach the quasi-continuum. Independently: ZERO exist."""
    cells = banked["cells"]
    usable = [
        c for c in cells
        if abs(c["kappa_eff"] - KAPPA_CERT) < 1e-12     # in scope (degeneracy => g0==1.0)
        and c["t63_over_trec"] <= T63_GATE              # transfer-live
        and c["peak_frac"] <= PEAK_MAX                  # no full discharge
        and not c["clamp_fires"]                        # clamp-never
        and c["n_occ"] >= NOCC_GATE                     # quasi-continuum populated
    ]
    assert len(usable) == 0, f"independent re-derivation found usable cells: {usable}"
    assert banked["outcome"] == "C_INSTRUMENT_INCOMPATIBLE"


def test_independent_rederivation_quasicontinuum_all_clamp(banked):
    """Re-derived from raw fields: EVERY in-scope quasi-continuum comb (N_occ>=10)
    fully discharges (peak>0.85) AND clamps. There is no gap between 'populated' and
    'discharged' at the certified cell — the incompatibility mechanism (finding §5)."""
    in_scope_qc = [
        c for c in banked["cells"]
        if abs(c["kappa_eff"] - KAPPA_CERT) < 1e-12 and c["n_occ"] >= NOCC_GATE
    ]
    assert len(in_scope_qc) >= 1, "expected at least one in-scope quasi-continuum comb"
    for c in in_scope_qc:
        assert c["clamp_fires"] is True, f"quasi-continuum comb did not clamp: {c['delta_omega']}"
        assert c["peak_frac"] > PEAK_MAX, f"quasi-continuum comb not full-discharge: {c['delta_omega']}"


def test_lone_raw_satisfier_doubly_disqualified(banked):
    """The only cell tripping the three raw transfer conditions is disqualified on TWO
    pre-existing grounds (out-of-scope kappa_eff<0.030 AND REGIME-NOT-REACHED N_occ<10)
    — re-derived from raw fields, independent of the driver's disqualifier list."""
    raw_sat = [
        c for c in banked["cells"]
        if c["t63_over_trec"] <= T63_GATE and c["peak_frac"] <= PEAK_MAX and not c["clamp_fires"]
    ]
    assert len(raw_sat) == 1, f"expected exactly one raw-satisfier, got {len(raw_sat)}"
    c = raw_sat[0]
    out_of_scope = abs(c["kappa_eff"] - KAPPA_CERT) >= 1e-12
    regime_not_reached = c["n_occ"] < NOCC_GATE
    assert out_of_scope and regime_not_reached, (
        f"raw-satisfier not doubly-disqualified: kappa_eff={c['kappa_eff']}, n_occ={c['n_occ']}"
    )


def test_fence_no_return_quantities_in_banked_cells(banked):
    """The FENCE: no return/collapse quantity leaked into the banked cells — only
    transfer quantities + the regime-side N_occ. Guards against a future edit peeking
    at the answer during calibration."""
    forbidden = {"r_return_table", "r_cum_table", "x_50", "r_return", "r_cum"}
    for c in banked["cells"]:
        leaked = forbidden & set(c.keys())
        assert not leaked, f"return/collapse quantity leaked into scan cell: {leaked}"
