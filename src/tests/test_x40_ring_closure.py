"""x40 — 10-ring closure transient: gates G-A..G-E + sabotage S1/S2/S3 (P11).

The gates certify the frozen prereg
(research/2026-07-10_x40-ring-closure-transient_prereg_FROZEN.md); the sabotage
cases plant violations and assert the corresponding gate FIRES (P11: a gate that
cannot fail is not a gate). Vocabulary: reactive/trapped/radiated — never "loss".
"""

from __future__ import annotations

import numpy as np
import pytest

from ave.core.chiral_lattice import build_srs_net
from ave.topological.srs_dec import enumerate_girth_faces
from scripts.vol_1_foundations.x40_ring_closure_transient import (
    Ring,
    _bfs_girth,
    assert_srs_girth,
    derive_ring,
    gate_metrics,
    hodge_split_fullnet,
    hodge_split_injected_current,
    mutual_inductance,
    neumann_second_axis,
    ring_orientation_ensemble,
    scan_for_dimensional_constants,
    simulate,
)

# Frozen tolerances (prereg §GATES).
TOL_LAMBDA = 1e-12  # G-A
TOL_PLATEAU = 1e-6  # G-B
TOL_LEDGER = 1e-12  # G-C
TOL_HODGE = 1e-12  # G-F

_DRIVER = "src/scripts/vol_1_foundations/x40_ring_closure_transient.py"
_S2_PLANT = "src/scripts/vol_1_foundations/_x40_s2_antiinstall_planted.py"
_S2B_PLANT = "src/scripts/vol_1_foundations/_x40_s2b_antiinstall_aliased_planted.py"


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
    assert ring.N == 10, "srs girth must be 10 (10,3)-a); N is verified, not hardcoded"
    assert len(ring.nodes) == 10
    assert ring.coords.shape == (10, 3)


def test_g_d_independent_bfs_girth_agrees():
    """The genuine G-D witness: an INDEPENDENT BFS girth of the L=3 net == 10."""
    net = build_srs_net(L=3)
    assert _bfs_girth(net.neighbors) == 10
    assert assert_srs_girth(net) == 10


def test_g_d_rejects_subcritical_supercell():
    """L=2 folds girth-10 into spurious 8-rings; derive_ring must refuse it."""
    with pytest.raises(ValueError, match="MIN_SRS_L"):
        derive_ring(L=2)


def test_s5_bfs_girth_fires_g_d_on_spurious_net():
    """S5: an L=2 net has TRUE girth 8, but enumerate_girth_faces returns spurious
    length-10 cycles (the pre-filter defect). The independent BFS-girth G-D check
    must FIRE — this is the sabotage that closes the P11 gap for G-D."""
    net = build_srs_net(L=2)
    faces = enumerate_girth_faces(net)
    # the enumeration is silent — it is pre-filtered to length 10 (the defect)
    assert sorted({len(f) for f in faces}) == [10]
    # the independent BFS witness sees the true girth 8 ...
    assert _bfs_girth(net.neighbors) == 8
    # ... so the genuine three-way G-D assertion FIRES
    with pytest.raises(RuntimeError, match="BFS girth 8"):
        assert_srs_girth(net, faces=faces)


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


def test_s2b_aliased_forbidden_name_fires_g_e():
    """S2b: a forbidden constant NAME imported ALIASED from a NON-constants module
    (the slip the review found) must now FIRE G-E — a forbidden name is forbidden
    wherever it is re-exported from. The real driver stays clean."""
    plant = scan_for_dimensional_constants(_S2B_PLANT)
    assert plant, "G-E did NOT fire on an aliased forbidden-name import (F2 slip)"
    assert any("OMEGA_C" in v for v in plant)
    assert scan_for_dimensional_constants(_DRIVER) == [], "the real driver must remain clean"


# ─────────────────────────────────────────────────────────────────────────────
# E5 (amendment) — the cut/cycle Hodge split + G-F gate + S4 sabotage.
# ─────────────────────────────────────────────────────────────────────────────


def test_e5_cut_cycle_split_is_nine_to_one(ring):
    """The T-even cut / T-odd cycle split of i(0) on the tree-local ring = 9/10 : 1/10."""
    s = hodge_split_injected_current(ring)
    assert s["cut_fraction_T_even"] == pytest.approx(0.9, abs=1e-9)
    assert s["cycle_fraction_T_odd"] == pytest.approx(0.1, abs=1e-9)
    assert s["b1_cycle_dim"] == 1.0  # a single completed ring => b1 = 1


def test_e5_cycle_fraction_equals_energy_split(ring, transient):
    """The load-bearing coincidence: the T-odd cycle projection = the E2 energy split.

    The divergence-free loop current is exactly the part the matched stubs cannot
    drain — so the bounce sim's trapped fraction EQUALS the cycle-space projection.
    """
    cyc = hodge_split_injected_current(ring)["cycle_fraction_T_odd"]
    f_E = transient.E_ring[-1] / transient.E0
    assert cyc == pytest.approx(f_E, abs=1e-9)


def test_g_f_hodge_orthogonality_completeness(ring):
    """G-F: cut _|_ cycle, |P_cut i|^2 + |P_cyc i|^2 = |i|^2, and P_cut + P_cyc = I."""
    s = hodge_split_injected_current(ring)
    assert abs(s["G_F_ortho"]) < TOL_HODGE, "cut and cycle not orthogonal"
    assert s["G_F_completeness"] < TOL_HODGE, "projections do not sum to |i|^2"
    assert s["G_F_projsum_max"] < TOL_HODGE, "P_cut + P_cyc != I on the edge space"


def test_s4_nonorthogonal_projector_fires_g_f(ring):
    """S4: a planted non-orthogonal (oblique) projector -> G-F fires on all three legs."""
    s = hodge_split_injected_current(ring, perturb=0.1)
    assert abs(s["G_F_ortho"]) > TOL_HODGE, "G-F ortho did NOT fire under a skewed projector"
    assert s["G_F_completeness"] > TOL_HODGE, "G-F completeness did NOT fire"
    assert s["G_F_projsum_max"] > TOL_HODGE, "G-F projector-sum did NOT fire"


def test_e5_fullnet_qualifier_is_load_bearing():
    """The tree-local qualifier matters: on the full srs net the cycle fraction != 1/10."""
    f = hodge_split_fullnet()
    assert f["cycle_fraction_T_odd_fullnet"] > 0.1 + 1e-3, "full-net cycle fraction must exceed 1/10"
    assert f["b1_fullnet"] == pytest.approx(109.0)


def test_e5_orientation_ensemble_is_isotropic_balanced():
    """Omega enters as a unit axis only (no scale). The srs ring planes are isotropic/balanced."""
    o = ring_orientation_ensemble()
    eig = np.array(o["Q_eigenvalues"])
    # sign-free orientation tensor is trace-1; isotropic => all eigenvalues ~ 1/3
    assert np.allclose(eig, 1.0 / 3.0, atol=1e-6), f"ring planes not isotropic: {eig}"
    assert o["signed_mean_normal_magnitude"] < 0.1, "ensemble not balanced (net normal too large)"


def test_e5_orientation_axis_is_not_a_scale():
    """Anti-install: the orientation deliverable introduces NO dimensional constant."""
    assert scan_for_dimensional_constants(_DRIVER) == []
