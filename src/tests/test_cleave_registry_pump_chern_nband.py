"""Cleave-01 registry-pump Chern N-band — validation gates + the frozen-bin verdict.

FROZEN PRE-REG: research/2026-07-02_cleave-registry-pump-chern-nband_prereg.md.
RESULT DOC    : research/2026-07-02_cleave-registry-pump-chern-nband_result.md.
UPSTREAM      : the 2-band NULL-DERIVED result (§5 scoped this N-band upgrade).

The LAST roll (Grant pre-commitment): the genuine 8-site srs-cell tight-binding
occupied-MANIFOLD Chern over (k_z, theta), both readings, both enantiomorphs.
A confirmed null CLOSES the coupling question permanently.

  G-VOK-A  recover the 2-band C=0 in a restricted subspace (both readings). FAST.
  G-VOK-B  detect a KNOWN multi-band nonzero (|C|=2, flips sign). FAST.
  G-ANCHOR srs-R reproduces g0=2.21589 rad/z-unit to 0.25%. FAST.
  G-HERMITIAN the srs Bloch H is exactly Hermitian + half-manifold gapped. FAST.
  G-SLIDING-FLAT sliding H is theta-INDEPENDENT (C_slide=0 by construction). FAST.
  G-VERDICT the frozen bin NULL-CONFIRMED-FINAL (engine_sim: full sweep).

The full convergence sweep (run_all_nband / srs_nband_convergence over n=24/36/48
x 12 transverse slices x 4 configs) is the T2 driver -> engine_sim (make
test-engine); the FAST VOK/anchor/Hermiticity/sliding-flat checks stay gating.
Partition registered in conftest.py.
"""

from __future__ import annotations

import numpy as np

from scripts.vol_4_engineering.cleave_registry_pump_chern_nband import (
    N_OCC,
    adjudicate_nband,
    run_all_nband,
    srs_anchor,
    srs_bloch_H,
    srs_bloch_H_grid,
    srs_nband_chern,
    vok_check_a_recover_2band,
    vok_check_b_known_multiband,
)


# ── G-VOK-A — recover the 2-band C=0 (FAST keeper) ──────────────────────────
def test_gvok_a_recovers_2band_zero():
    """The N-band non-Abelian integrator must recover the validated 2-band C=0 in
    the restricted screw-block subspace (both readings) — proves no spurious
    nonzero is introduced (prereg SS2 Check A)."""
    for reading in ("sliding", "locked"):
        r = vok_check_a_recover_2band(reading)
        assert r["chern_int"] == 0, (reading, r)


# ── G-VOK-B — detect a known multi-band nonzero (FAST keeper) ───────────────
def test_gvok_b_detects_known_multiband():
    """The integrator must DETECT a known multi-band pump (|C|=2) and flip sign
    with pump direction — proves it is not trivially returning 0 (prereg SS2
    Check B)."""
    bp = vok_check_b_known_multiband(pump_sign=+1)
    bm = vok_check_b_known_multiband(pump_sign=-1)
    assert abs(bp["chern_int"]) == 2, bp
    assert bp["chern_int"] == -bm["chern_int"], (bp, bm)


# ── G-ANCHOR — srs-R reproduces the OA anchor (FAST keeper) ─────────────────
def test_ganchor_srs_r_reproduces_oa_pitch():
    """srs-R bare screw pitch reproduces the published g0=2.21589 rad/z-unit to
    0.25% (prereg SS3; shared with the 2-band anchor)."""
    aR = srs_anchor("right")
    assert aR["pitch_matches_anchor_0p25pct"], aR


# ── G-HERMITIAN — srs Bloch H Hermitian + half-manifold gapped (FAST keeper) ─
def test_ghermitian_srs_bloch_gapped():
    """The 8-band srs Bloch H is exactly Hermitian and the half-filled occupied
    manifold is gapped from the unoccupied one over a coarse torus (rules out the
    gapless INCONCLUSIVE bin for the bulk construction)."""
    for reading in ("sliding", "locked"):
        min_gap = np.inf
        herm = 0.0
        for kz in np.linspace(0.0, 2.0 * np.pi, 8, endpoint=False):
            for th in np.linspace(0.0, 2.0 * np.pi, 8, endpoint=False):
                H = srs_bloch_H(0.7, 1.3, kz, th, "right", reading)
                herm = max(herm, float(np.max(np.abs(H - H.conj().T))))
                w = np.linalg.eigvalsh(H)
                min_gap = min(min_gap, float(w[N_OCC] - w[N_OCC - 1]))
        assert herm < 1e-12, (reading, herm)
        assert min_gap > 1e-3, (reading, min_gap)


# ── G-SLIDING-FLAT — sliding H is theta-independent (FAST keeper) ────────────
def test_gsliding_flat_theta_independent():
    """SLIDING reading: matter drags no texture -> theta is an unobservable global
    wavefunction phase -> H is theta-INDEPENDENT -> C_slide = 0 by construction.
    (A theta-DEPENDENT sliding H would be the wrong reading; this guards it.)"""
    g1 = np.array([[1.0]])
    for th in (0.0, 1.0, 2.5):
        H0 = srs_bloch_H_grid(0.7, 1.3, g1, np.array([[0.0]]), "right", "sliding")[0, 0]
        Ht = srs_bloch_H_grid(0.7, 1.3, g1, np.array([[th]]), "right", "sliding")[0, 0]
        assert np.allclose(H0, Ht), f"sliding H must be theta-independent (theta={th})"


# ── G-VERDICT — the frozen bin NULL-CONFIRMED-FINAL (engine_sim) ────────────
def test_gverdict_null_confirmed_final():
    """The committed verdict: C_N = 0 in BOTH readings AND BOTH enantiomorphs
    (gapped + converged, VOK PASS) -> NULL-CONFIRMED-FINAL. CI cannot silently
    flip the coupling-question closure."""
    results = run_all_nband(grids=(24, 36, 48))
    v = results["verdict"]
    assert v["vok_pass"], "GATE-VOK must pass for the verdict to count"
    assert v["converged"], "srs Chern must converge across n=24/36/48"
    assert v["enantio_odd_ok"], "enantiomorph-odd guard"
    assert all(c == 0 for c in v["C"].values()), v["C"]
    assert v["bin"] == "NULL-CONFIRMED-FINAL", v


# ── srs config: all slices agree + gapped + converged (engine_sim) ──────────
def test_srs_all_configs_gapped_converged():
    """Each (reading x enantiomorph) srs config: gapped, grid-stable C=0, and all
    transverse slices agree (the slice-independence guard) — the offset HS-point
    sampling removes the Gamma/M-corner branch artifact."""
    for reading in ("sliding", "locked"):
        for e in ("right", "left"):
            r = srs_nband_chern(e, reading, n=36)
            assert r["min_manifold_gap"] > 1e-3, (reading, e, r["min_manifold_gap"])
            assert r["all_slices_agree"], (reading, e, r["per_slice_ints"])
            assert r["chern_int"] == 0, (reading, e, r["chern_int"])


# ── adjudicate_nband encodes the frozen bins (FAST unit test) ───────────────
def test_adjudicate_nband_bins_frozen():
    """adjudicate_nband() maps computed C's to the frozen bins exactly (prereg
    SS4). Synthetic inputs exercise each branch — not editable post-hoc."""

    def _c(ci, conv=True):
        return {"chern_int": ci, "converged": conv}

    vok = {"a_sliding": _c(0), "a_locked": _c(0), "b_plus": _c(-2), "b_minus": _c(2)}
    anchor = {"right": {"pitch_matches_anchor_0p25pct": True}}

    def build(cs, cl):
        return {
            "vok": vok,
            "anchor": anchor,
            "srs": {
                ("sliding", "right"): _c(cs), ("sliding", "left"): _c(-cs),
                ("locked", "right"): _c(cl), ("locked", "left"): _c(-cl),
            },
        }

    assert adjudicate_nband(build(0, 0))["bin"] == "NULL-CONFIRMED-FINAL"
    assert adjudicate_nband(build(1, 0))["bin"] == "REOPENS"
    assert adjudicate_nband(build(0, 1))["bin"] == "REOPENS"
    # same-sign nonzero across enantiomorphs -> RED FLAG -> INCONCLUSIVE
    red = build(1, 0)
    red["srs"][("sliding", "left")] = _c(1)
    assert adjudicate_nband(red)["bin"] == "INCONCLUSIVE"
    # VOK-B fails to detect nonzero -> INCONCLUSIVE
    bad = build(0, 0)
    bad["vok"] = {"a_sliding": _c(0), "a_locked": _c(0), "b_plus": _c(0), "b_minus": _c(0)}
    assert adjudicate_nband(bad)["bin"] == "INCONCLUSIVE"
