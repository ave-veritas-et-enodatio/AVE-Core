"""Cleave-01 registry-pump Chern — validation gates + the frozen-bin verdict gate.

FROZEN PRE-REG: research/2026-07-02_cleave-registry-pump-chern_prereg.md.
RESULT DOC    : research/2026-07-02_cleave-registry-pump-chern_result.md.
RECEIPTS      : research/2026-07-02_cleave-coupling-derivation_adjudication.md.

Grant ruling (b): run BOTH substrate readings (sliding/Eulerian vs locked/
Lagrangian); whichever reproduces the OA anchor earns the canon slot. The driver
computes the occupied-band Chern number of the srs screw channel over the
(k_z, theta) registry torus in each reading.

  G-TOY  VALIDATE-ON-KNOWN (FAST keeper): the Fukui-Hatsugai integrator reads
         C=+-1 on the Rice-Mele/Thouless toy pump AND flips sign with pump
         direction. If not -> INCONCLUSIVE (machinery untrusted). Gating lane.
  G-SLOPE  the three frozen slopes (146.7/414.9/586.8 fC/um) reproduce from
         canonical constants; 414.9 needs non-integer C (NOT integer-reachable).
         FAST keeper, gating lane.
  G-ANCHOR  srs-R reproduces the OA bulk g0 = 2.21589 rad/z-unit to 0.25%.
         FAST keeper, gating lane.
  G-VERDICT  the frozen outcome bin (engine_sim): the dual-reading srs Chern is
         computed over the torus; the frozen bin is asserted. CI cannot silently
         flip the committed verdict.

The srs (k_z, theta) torus Chern + gap scan (run_all / srs_registry_chern) is the
T2 driver -> engine_sim (run via `make test-engine`); the toy/slope/anchor FAST
structural checks stay in the gating lane. Partition registered in conftest.py.
"""

from __future__ import annotations

import numpy as np

from scripts.vol_4_engineering.cleave_registry_pump_chern import (
    adjudicate,
    expected_slopes_fc_per_um,
    rice_mele_chern,
    run_all,
    srs_anchor,
    srs_registry_chern,
)


# ── G-TOY — VALIDATE-ON-KNOWN (FAST keeper; gating lane) ─────────────────────
def test_gtoy_rice_mele_reads_pm1_and_flips():
    """The Chern machinery MUST read C=+-1 on the Rice-Mele toy pump and flip sign
    with pump direction — the frozen validate-on-known gate (prereg SS2)."""
    tp = rice_mele_chern(pump_sign=+1)
    tm = rice_mele_chern(pump_sign=-1)
    assert abs(abs(tp["chern"]) - 1.0) < 0.1, tp
    assert abs(abs(tm["chern"]) - 1.0) < 0.1, tm
    assert tp["chern_int"] == -tm["chern_int"] != 0, (tp, tm)
    # well-resolved: plaquette phases far below pi/2
    assert tp["max_plaquette"] < 1.0


# ── G-SLOPE — the three frozen slopes from canonical constants (FAST keeper) ─
def test_gslope_frozen_slopes_from_constants():
    """146.7 / 414.9 / 586.8 fC/um reproduce from ave.core.constants; the bench
    414.9 needs a NON-integer C (2sqrt2), impossible for a Chern pump (prereg SS5)."""
    s = expected_slopes_fc_per_um()
    assert abs(s["bench_e_over_lnode"] - 414.9) < 0.1
    assert abs(s["full_cell_e_over_acell"] - 146.7) < 0.1
    assert abs(s["quarter_e_over_p"] - 586.8) < 0.1
    # bench / full-cell = 2sqrt2 (non-integer C); quarter / bench = sqrt2
    assert abs(s["bench_e_over_lnode"] / s["full_cell_e_over_acell"] - 2 * np.sqrt(2)) < 1e-3
    assert abs(s["quarter_e_over_p"] / s["bench_e_over_lnode"] - np.sqrt(2)) < 1e-3


# ── G-ANCHOR — srs-R reproduces the OA anchor g0 to 0.25% (FAST keeper) ──────
def test_ganchor_srs_r_reproduces_oa_pitch():
    """srs-R bare screw pitch reproduces the published bulk g0 = 2.21589 rad/z-unit
    to 0.25% (prereg SS3). The signed-torsion handedness channel is enantiomorph-
    distinct (the honest sign channel; the bare-pitch formula shares R across L/R)."""
    aR = srs_anchor("right")
    assert aR["pitch_matches_anchor_0p25pct"], aR
    assert aR["pitch_pct_off_anchor"] <= 0.251
    # the signed handedness channel exists and is nonzero (writhe/torsion carrier)
    aL = srs_anchor("left")
    assert aR["signed_torsion"] != 0.0 and aL["signed_torsion"] != 0.0


# ── G-VERDICT — the frozen outcome bin (engine_sim) ─────────────────────────
def test_gverdict_frozen_bin_null_derived():
    """The committed verdict: the operator-derived srs registry pump gives
    C_slide = 0 AND C_lock = 0 (both gapped + converged) -> NULL-DERIVED. CI cannot
    silently flip this. If a future engine change flips C, THAT is a new prereg."""
    results = run_all(n_grid=48)
    v = results["verdict"]
    assert v["toy_pass"], "GATE-TOY must pass for the verdict to count"
    assert v["slide_converged"] and v["lock_converged"], "srs Chern must converge"
    assert v["slide_enantio_odd"] and v["lock_enantio_odd"], "enantiomorph-odd guard"
    assert v["C_slide"] == 0 and v["C_lock"] == 0, (v["C_slide"], v["C_lock"])
    assert v["bin"] == "NULL-DERIVED", v


# ── srs Chern per reading is gapped + converged (engine_sim) ────────────────
def test_srs_chern_both_readings_gapped_and_converged():
    """Each reading's srs band is gapped over the torus (Chern well-defined) and
    the Chern rounds to a stable integer under grid refinement — rules out the
    INCONCLUSIVE (gap-closing / non-convergence) bin for this construction."""
    for reading in ("sliding", "locked"):
        for e in ("right", "left"):
            r = srs_registry_chern(e, reading, n_k=48, n_theta=48)
            assert r["min_band_gap"] > 1e-3, (reading, e, r["min_band_gap"])
            assert r["converged"], (reading, e, r)
            assert r["chern_int"] == 0, (reading, e, r["chern_int"])


# ── adjudicate() encodes the frozen bins (FAST unit test; gating lane) ──────
def test_adjudicate_bin_logic_is_frozen():
    """adjudicate() maps computed C's to the frozen bins exactly (prereg SS4).
    Synthetic inputs exercise each branch — the bin logic is not editable post-hoc."""

    def _mk(chern_int, converged=True):
        return {"chern": float(chern_int), "chern_int": chern_int, "converged": converged}

    toy = {+1: _mk(-1), -1: _mk(+1)}
    anchor = {"right": {"pitch_matches_anchor_0p25pct": True}, "left": {"pitch_matches_anchor_0p25pct": False}}

    def build(cs, cl):
        return {
            "toy": toy,
            "anchor": anchor,
            "srs": {
                ("sliding", "right"): _mk(cs),
                ("sliding", "left"): _mk(-cs),
                ("locked", "right"): _mk(cl),
                ("locked", "left"): _mk(-cl),
            },
        }

    assert adjudicate(build(0, 0))["bin"] == "NULL-DERIVED"
    assert adjudicate(build(1, 0))["bin"] == "CANON-CANDIDATE"
    assert adjudicate(build(0, 1))["bin"] == "CANON-CANDIDATE"
    assert adjudicate(build(1, 1))["bin"] == "BOTH-NONZERO"
    # same-sign nonzero across enantiomorphs -> RED FLAG -> INCONCLUSIVE
    red = build(1, 0)
    red["srs"][("sliding", "left")] = _mk(+1)  # same sign as right
    assert adjudicate(red)["bin"] == "INCONCLUSIVE"
