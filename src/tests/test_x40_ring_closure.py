"""x40 — 10-ring closure transient: gates G-A..G-E + sabotage S1/S2/S3 (P11).

The gates certify the frozen prereg
(research/2026-07-10_x40-ring-closure-transient_prereg_FROZEN.md); the sabotage
cases plant violations and assert the corresponding gate FIRES (P11: a gate that
cannot fail is not a gate). Vocabulary: reactive/trapped/radiated — never "loss".
"""

from __future__ import annotations

import numpy as np
import pytest

from scripts.vol_1_foundations.x40_ring_closure_transient import (
    Ring,
    derive_ring,
    gate_metrics,
    mutual_inductance,
    neumann_second_axis,
    scan_for_dimensional_constants,
    simulate,
)

# Frozen tolerances (prereg §GATES).
TOL_LAMBDA = 1e-12  # G-A
TOL_PLATEAU = 1e-6  # G-B
TOL_LEDGER = 1e-12  # G-C

_DRIVER = "src/scripts/vol_1_foundations/x40_ring_closure_transient.py"
_S2_PLANT = "src/scripts/vol_1_foundations/_x40_s2_antiinstall_planted.py"


@pytest.fixture(scope="module")
def ring() -> Ring:
    return derive_ring()


@pytest.fixture(scope="module")
def transient(ring: Ring):
    return simulate(ring.N, n_ticks=300)


# ─────────────────────────────────────────────────────────────────────────────
# G-D — ring count is DERIVED from the srs net, asserted == 10.
# ─────────────────────────────────────────────────────────────────────────────


def test_g_d_ring_count_derived(ring: Ring):
    assert ring.N == 10, "srs girth must be 10 (10,3)-a); N is derived, not hardcoded"
    assert len(ring.nodes) == 10
    assert ring.coords.shape == (10, 3)


def test_g_d_rejects_subcritical_supercell():
    """L=2 folds girth-10 into spurious 8-rings; derive_ring must refuse it."""
    with pytest.raises(ValueError, match="MIN_SRS_L"):
        derive_ring(L=2)


# ─────────────────────────────────────────────────────────────────────────────
# G-A — the Lambda-conservation theorem (the DC trap), machine-exact.
# ─────────────────────────────────────────────────────────────────────────────


def test_g_a_lambda_conserved(transient):
    dev = np.max(np.abs(transient.Lambda - transient.Lambda0) / abs(transient.Lambda0))
    assert dev < TOL_LAMBDA, f"Lambda drifted {dev:.2e} (>= {TOL_LAMBDA})"
    assert transient.Lambda0 == pytest.approx(1.0), "Lambda(0) = L_bond * I_parent = 1"


# ─────────────────────────────────────────────────────────────────────────────
# G-B — the plateau: settled uniform DC current = 1/N (= L_bond/L_loop).
# ─────────────────────────────────────────────────────────────────────────────


def test_g_b_plateau_reaches_theorem(transient, ring):
    i_final = transient.currents_final
    target = 1.0 / ring.N
    assert np.max(np.abs(i_final - target)) < TOL_PLATEAU, "profile not flat at 1/N by 300 tau"
    # mean current = Lambda/N exactly at all ticks (a check, not the plateau content)
    assert i_final.mean() == pytest.approx(target, abs=1e-12)


def test_headline_split_is_one_tenth(transient):
    """The deliverable number: trapped f_E = 1/10, radiated 9/10 (substrate-native TLM)."""
    f_E = transient.E_ring[-1] / transient.E0
    f_rad = transient.E_rad[-1] / transient.E0
    assert f_E == pytest.approx(0.1, abs=1e-9)
    assert f_rad == pytest.approx(0.9, abs=1e-9)


# ─────────────────────────────────────────────────────────────────────────────
# G-C — the lossless energy ledger E_ring + E_rad = E0, machine-exact.
# ─────────────────────────────────────────────────────────────────────────────


def test_g_c_energy_ledger(transient):
    dev = np.max(np.abs(transient.E_ring + transient.E_rad - transient.E0) / transient.E0)
    assert dev < TOL_LEDGER, f"ledger drifted {dev:.2e} (>= {TOL_LEDGER}) — not lossless"
    assert transient.E0 == pytest.approx(0.5), "E0 = 1/2 L_bond I_parent^2 = 1/2"


# ─────────────────────────────────────────────────────────────────────────────
# G-E — the anti-install scanner: clean on the driver, no dimensional constants.
# ─────────────────────────────────────────────────────────────────────────────


def test_g_e_driver_is_dimensionless():
    assert scan_for_dimensional_constants(_DRIVER) == [], "driver must import NO dimensional constant"


# ─────────────────────────────────────────────────────────────────────────────
# E4 — the Neumann geometric second axis (characterization; KEEP-BOTH).
# ─────────────────────────────────────────────────────────────────────────────


def test_e4_sum_m_is_a_geometric_invariant(ring):
    res = neumann_second_axis(ring)
    # frozen value computed on the srs 10-ring (ring-choice & enantiomorph invariant)
    assert res["sum_m_jk"] == pytest.approx(0.6448522896, abs=1e-8)
    assert res["f_E_geom"] == pytest.approx(0.0939421208, abs=1e-8)
    # mixed footing: geometric loop inductance exceeds N self-terms (net positive mutual)
    assert res["L_loop_geom_over_mu0l"] > ring.N


def test_e4_mutual_matches_gauss_legendre(ring):
    """Non-adjacent M_jk from the 1-D reduction agrees with 32x32 Gauss (< 1e-9)."""
    P = ring.coords
    N = ring.N
    segs = [np.array([P[k], P[(k + 1) % N]]) for k in range(N)]

    def m_gauss(sj, sk, n=32):
        x, w = np.polynomial.legendre.leggauss(n)
        a0, a1 = sj
        c0, c1 = sk
        da, dc = a1 - a0, c1 - c0
        L1, L2 = np.linalg.norm(da), np.linalg.norm(dc)
        ah, ch = da / L1, dc / L2
        s = (x + 1) / 2 * L1
        t = (x + 1) / 2 * L2
        ws, wt = w / 2 * L1, w / 2 * L2
        tot = 0.0
        for i in range(n):
            R = np.linalg.norm((a0 + s[i] * ah)[None, :] - (c0[None, :] + t[:, None] * ch[None, :]), axis=1)
            tot += ws[i] * np.sum(wt / R)
        return (ah @ ch) * tot / (4 * np.pi)

    for j, k in [(0, 3), (0, 5), (1, 6)]:
        assert mutual_inductance(segs[j], segs[k]) == pytest.approx(m_gauss(segs[j], segs[k]), abs=1e-9)


def test_e4_mutual_is_symmetric(ring):
    P = ring.coords
    s0 = np.array([P[0], P[1]])
    s5 = np.array([P[5], P[6]])
    assert mutual_inductance(s0, s5) == pytest.approx(mutual_inductance(s5, s0), abs=1e-12)


# ─────────────────────────────────────────────────────────────────────────────
# SABOTAGE — every gate proven able to FAIL (P11). Each plants a violation and
# asserts the corresponding gate FIRES.
# ─────────────────────────────────────────────────────────────────────────────


def test_s1_series_resistance_fires_g_a_and_g_b(ring):
    """S1: planted series resistance on one ring bond -> Lambda decays, plateau undershoots."""
    tr = simulate(ring.N, n_ticks=300, bond_loss=0.05, loss_bond=0)
    gm = gate_metrics(tr)
    assert gm["G_A_lambda_max_rel_dev"] > TOL_LAMBDA, "G-A did NOT fire under planted resistance"
    assert gm["G_B_i_dc_mean"] < 1.0 / ring.N - TOL_PLATEAU, "G-B did NOT fire (plateau not undershot)"


def test_s3_dropped_stub_fires_g_c_only(ring):
    """S3: drop one stub from the radiated ledger -> G-C fires; dynamics (G-A) unchanged."""
    tr = simulate(ring.N, n_ticks=300, drop_stub=3)
    gm = gate_metrics(tr)
    assert gm["G_C_ledger_max_rel_dev"] > TOL_LEDGER, "G-C did NOT fire under a dropped stub"
    # discriminator: the dynamics are untouched, so Lambda is still conserved exactly
    assert gm["G_A_lambda_max_rel_dev"] < TOL_LAMBDA, "S3 must not perturb the dynamics"


def test_s2_planted_import_fires_g_e():
    """S2: a variant importing OMEGA_C -> G-E fires; the real driver stays clean."""
    plant = scan_for_dimensional_constants(_S2_PLANT)
    assert plant, "G-E did NOT fire on the planted anti-install variant"
    assert any("OMEGA_C" in v for v in plant)
    assert scan_for_dimensional_constants(_DRIVER) == [], "the real driver must remain clean"
