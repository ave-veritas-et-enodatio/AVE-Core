"""Tests for the harmonic-balance solver (ave.solvers.harmonic_balance_srs).

Build brief: _orchestration/2026-08-24_static-existence-build-brief.md (Stage 2).
Consistency-vs-emergence: every test here is IMPLEMENTATION-VERIFICATION of an
instrument (consistency / known-case classes); nothing asserts physics beyond
what the certified engine + canonical kernel already carry. The three
validation gates each COMPUTE their pass (reconcile-don't-declare):

  gate 1 (cold linear limit -> arccos band): T_gate1_* here (fast twins) + the
         full sweep in research/drivers/harmonic_balance_validation.py;
  gate 2 (single-tone graded limit -> the MEASURED Class-C response map):
         T_gate2_* smoke vs the canonical core locus + the regression binding
         against the committed receipts JSON (test_receipts_*), with the full
         L=24 measured-map comparison in the validation driver;
  gate 3 (source-idle machinery on the known driven-vs-autonomous pair):
         T_gate3_*.

Structural keepers exercise consumer-side wiring of every public surface
(module-library discipline): bond tables, scatter weights, apply, solve,
envelope, terminations, fits, de-embedding, idle report.
"""

from __future__ import annotations

import ast
import copy
import json
from pathlib import Path

import numpy as np
import pytest

import ave.solvers.harmonic_balance_srs as hb
from ave.core.chiral_lattice import build_srs_net, scatter_matrix, scalar_tlm_step
from ave.core.chiral_lattice_dynamics import ANALYTIC_NETWORK_FACTOR

_REPO = Path(__file__).resolve().parents[2]

# ─────────────────────────────────────────────────────────────────────────────
# shared small fixtures (module-scope: build once)
# ─────────────────────────────────────────────────────────────────────────────


@pytest.fixture(scope="module")
def srs2():
    net = build_srs_net(L=2)
    bt = hb.build_bond_table(net)
    return net, bt, net.connect_index()


@pytest.fixture(scope="module")
def ring12():
    net = hb.build_ring_net(12)
    bt = hb.build_bond_table(net)
    return net, bt, net.connect_index()


def _cold(bt):
    return hb.scatter_weights(bt, hb.bond_admittance(np.zeros(bt.n_bonds)))


def _plane_term(net, bt, conn, planes_drives, n_tones=1):
    specs = []
    for plane, drive_fwd, drive_bwd in planes_drives:
        f, b = hb.crossing_ports(net, bt, plane)
        specs.append((f, np.asarray(drive_fwd, dtype=np.complex128)))
        specs.append((b, np.asarray(drive_bwd, dtype=np.complex128)))
    return hb.make_termination(net, bt, conn, specs, n_tones)


# ─────────────────────────────────────────────────────────────────────────────
# structural keepers
# ─────────────────────────────────────────────────────────────────────────────


class TestBondTableAndWeights:
    def test_cold_weights_recover_bedrock_exactly(self, srs2):
        """A=0 => uniform Y => a_nodes == 2/3 == the bedrock (2/n)J-I weights,
        bit-level (the vacuum_varactor_scatter gate-1 twin)."""
        net, bt, conn = srs2
        a_nodes, Yp = _cold(bt)
        assert np.array_equal(a_nodes, np.full_like(a_nodes, 2.0 / 3.0))
        assert np.array_equal(Yp, np.ones_like(Yp))
        S3 = scatter_matrix(3)
        # scatter row weights: S_ij + delta_ij == a_j
        assert np.array_equal(S3 + np.eye(3), np.full((3, 3), 2.0 / 3.0))

    def test_per_node_uniform_saturation_cancels(self, srs2):
        """The structural-null trap (vacuum_varactor_scatter.py:54; epic guard
        4): a per-node-uniform grading MUST cancel at the shunt junction."""
        net, bt, conn = srs2
        a_uniform, _ = hb.scatter_weights(bt, hb.bond_admittance(np.full(bt.n_bonds, 0.7)))
        assert np.allclose(a_uniform, 2.0 / 3.0, atol=1e-13)

    def test_per_bond_varying_saturation_is_read(self, srs2):
        """A per-bond-varying grading MUST change the weights (operator reads
        saturation — the Fork-B unblocker twin)."""
        net, bt, conn = srs2
        rng = np.random.default_rng(12345)
        Ab = rng.uniform(0.2, 0.9, size=bt.n_bonds)
        a_graded, _ = hb.scatter_weights(bt, hb.bond_admittance(Ab))
        assert np.max(np.abs(a_graded - 2.0 / 3.0)) > 1e-3

    def test_bond_ports_are_a_perfect_pairing(self, srs2):
        net, bt, conn = srs2
        flat = bt.bond_ports.ravel()
        assert len(np.unique(flat)) == net.n_nodes * net.degree
        # each bond's two ports belong to its two endpoint nodes
        for bi in (0, bt.n_bonds // 2, bt.n_bonds - 1):
            u0 = bt.bond_ports[bi, 0] // net.degree
            u1 = bt.bond_ports[bi, 1] // net.degree
            assert u0 != u1


class TestOperator:
    def test_apply_matches_certified_step_cold(self, srs2):
        """apply_M on the cold net == scalar_tlm_step (consumer-side wiring of
        the certified engine; identical arithmetic on real fields)."""
        net, bt, conn = srs2
        a_nodes, _ = _cold(bt)
        rng = np.random.default_rng(7)
        V = rng.standard_normal((net.n_nodes, net.degree))
        ref = scalar_tlm_step(net, V, scatter_matrix(3), conn)
        got = hb.apply_M(a_nodes, conn, V.astype(np.complex128))
        assert np.allclose(got.imag, 0.0, atol=0.0)
        assert np.allclose(got.real, ref, atol=1e-14)

    def test_graded_step_conserves_Y_weighted_energy(self, srs2):
        """Ax3-losslessness receipt: the graded scatter+connect conserves
        E_Y = sum Y_p |V_p|^2 (the Class-C driver's ledger) for complex phasors."""
        net, bt, conn = srs2
        rng = np.random.default_rng(11)
        Ab = rng.uniform(0.0, 0.9, size=bt.n_bonds)
        a_nodes, Yp = hb.scatter_weights(bt, hb.bond_admittance(Ab))
        v = rng.standard_normal((net.n_nodes, net.degree)) + 1j * rng.standard_normal(
            (net.n_nodes, net.degree)
        )
        E0 = float(np.sum(Yp * np.abs(v) ** 2))
        E1 = float(np.sum(Yp * np.abs(hb.apply_M(a_nodes, conn, v)) ** 2))
        assert abs(E1 - E0) / E0 < 1e-12

    def test_graded_node_scatter_is_involutory(self, srs2):
        """S_u = 1 a^T - I with sum a_j = 2 => S_u^2 = I even when graded."""
        net, bt, conn = srs2
        rng = np.random.default_rng(3)
        Ab = rng.uniform(0.0, 0.9, size=bt.n_bonds)
        a_nodes, _ = hb.scatter_weights(bt, hb.bond_admittance(Ab))
        for u in (0, net.n_nodes // 2):
            S_u = np.tile(a_nodes[u], (3, 1)) - np.eye(3)
            assert np.allclose(S_u @ S_u, np.eye(3), atol=1e-12)


class TestToneAndTermination:
    def test_degenerate_tones_raise(self):
        with pytest.raises(ValueError):
            hb.ToneSet(thetas=(0.3, 0.3))

    def test_tone_canonical_domain_enforced(self):
        """Post-review repair receipt: pairwise distinctness is NOT the DP-1
        precondition — {theta, 2pi-theta} is the same physical line on integer
        steps and theta = 0/pi is self-conjugate. The canonical (0, pi) guard
        must reject all of these (and accept a genuine 2-line set)."""
        for bad in ((0.3, 2.0 * np.pi - 0.3), (0.0,), (np.pi,), (-0.3,), (4.0,)):
            with pytest.raises(ValueError):
                hb.ToneSet(thetas=bad)
        assert hb.ToneSet(thetas=(0.3, 0.45)).n_tones == 2

    def test_crossing_ports_wrap_aware(self):
        """Post-review repair receipt (can-fire both ways): a plane within one
        bond-x-extent of the periodic boundary must find the same crossing-bond
        count as its translation-equivalent interior plane (by lattice
        translation symmetry), and must be non-empty."""
        net = build_srs_net(L=4)
        bt = hb.build_bond_table(net)
        f_edge, b_edge = hb.crossing_ports(net, bt, 3.9)
        f_int, b_int = hb.crossing_ports(net, bt, 1.9)
        assert len(f_edge) > 0
        assert len(f_edge) == len(f_int)
        assert len(b_edge) == len(b_int)
        # plane folding: an out-of-box plane maps to its canonical image
        f_fold, b_fold = hb.crossing_ports(net, bt, 3.9 + 4.0)
        assert np.array_equal(np.sort(f_fold), np.sort(f_edge))

    def test_termination_shape_guards(self, srs2):
        net, bt, conn = srs2
        f, b = hb.crossing_ports(net, bt, 0.5)
        with pytest.raises(ValueError):
            hb.make_termination(net, bt, conn, [(f, np.zeros((2, 3)))], 2)
        # overlapping slots rejected
        with pytest.raises(ValueError):
            hb.make_termination(
                net, bt, conn, [(f, np.zeros(1)), (f, np.zeros(1))], 1
            )

    def test_solve_tone_imposes_drive_and_reports_residual(self, srs2):
        net, bt, conn = srs2
        a_nodes, _ = _cold(bt)
        term = _plane_term(net, bt, conn, [(0.5, [1.0 + 0j], [0.0 + 0j])])
        sol = hb.solve_tone(a_nodes, conn, 0.3, term, 0, warmstart=200)
        assert sol.converged
        assert sol.residual_rel < 1e-9
        # terminated slots carry the imposed phasors exactly
        assert np.allclose(sol.v.ravel()[term.ports], term.drive[0])


class TestEnvelope:
    def test_dp1_envelope_rule(self, srs2):
        """A_b^2 = sum_m (|v_fwd|^2 + |v_bwd|^2)/2 / v_norm^2 — computed
        directly and compared against envelope_A_bond (consumer wiring)."""
        net, bt, conn = srs2
        rng = np.random.default_rng(5)
        sols = []
        for th in (0.2, 0.31):
            v = rng.standard_normal((net.n_nodes, net.degree)) + 1j * rng.standard_normal(
                (net.n_nodes, net.degree)
            )
            sols.append(
                hb.ToneSolution(theta=th, v=v, residual_rel=0.0, converged=True, n_matvec=0, method="synthetic")
            )
        A = hb.envelope_A_bond(bt, sols, v_norm=2.0)
        vf = np.stack([s.v.ravel() for s in sols])
        expect = np.sqrt(
            ((np.abs(vf[:, bt.bond_ports[:, 0]]) ** 2 + np.abs(vf[:, bt.bond_ports[:, 1]]) ** 2) / 2.0).sum(
                axis=0
            )
        ) / 2.0
        assert np.allclose(A, expect, atol=1e-14)

    def test_envelope_normalization_fork_is_exactly_sqrt2(self, srs2):
        """The OPEN envelope-normalization fork's receipt (re-audit, 2026-08-25):
        the DP-3 full-tank arm exceeds the C-state arm by EXACTLY sqrt(2) in A
        at fixed v_norm — an algebraic identity via
        |v_f+v_b|^2 + |v_f-v_b|^2 == 2(|v_f|^2+|v_b|^2), content-independent.
        The module claims no resolution (G2 freezes); this test pins the exact
        relation so neither arm can silently drift."""
        net, bt, conn = srs2
        rng = np.random.default_rng(17)
        v = rng.standard_normal((net.n_nodes, net.degree)) + 1j * rng.standard_normal(
            (net.n_nodes, net.degree)
        )
        sol = hb.ToneSolution(theta=0.4, v=v, residual_rel=0.0, converged=True, n_matvec=0, method="synthetic")
        A_c = hb.envelope_A_bond(bt, [sol], mode="c-state")
        A_t = hb.envelope_A_bond(bt, [sol], mode="full-tank")
        assert np.allclose(A_t, np.sqrt(2.0) * A_c, rtol=1e-14, atol=0.0)
        # the identity behind the full-tank arm, verified directly on a bond
        vf = v.ravel()[bt.bond_ports[:, 0]]
        vb = v.ravel()[bt.bond_ports[:, 1]]
        lhs = np.abs(vf + vb) ** 2 + np.abs(vf - vb) ** 2
        rhs = 2.0 * (np.abs(vf) ** 2 + np.abs(vb) ** 2)
        assert np.allclose(lhs, rhs, rtol=1e-14)
        with pytest.raises(ValueError):
            hb.envelope_A_bond(bt, [sol], mode="nonsense")

    def test_envelope_validates_tone_lines(self, srs2):
        """envelope_A_bond accepts bare ToneSolution lists, so it enforces the
        canonical-domain precondition itself (re-audit hardening): out-of-domain
        or degenerate tone lines raise."""
        net, bt, conn = srs2
        v = np.ones((net.n_nodes, net.degree), dtype=np.complex128)

        def mk(th):
            return hb.ToneSolution(theta=th, v=v, residual_rel=0.0, converged=True, n_matvec=0, method="synthetic")

        for bad in ([mk(0.0)], [mk(np.pi)], [mk(4.0)], [mk(0.3), mk(0.3)]):
            with pytest.raises(ValueError):
                hb.envelope_A_bond(bt, bad)


class TestDeEmbedding:
    def test_two_port_recovers_synthetic_exactly(self):
        G, T, Gp, Tp = -0.3 + 0.02j, 0.9 - 0.05j, 0.31 + 0.01j, 0.88 + 0.03j
        rng = np.random.default_rng(9)
        runs = []
        for _ in range(3):
            a = rng.standard_normal() + 1j * rng.standard_normal()
            d = rng.standard_normal() + 1j * rng.standard_normal()
            runs.append({"a": a, "d": d, "b": G * a + Tp * d, "c": T * a + Gp * d})
        out = hb.interface_two_port(runs)
        assert abs(out["gamma"] - G) < 1e-12
        assert abs(out["t"] - T) < 1e-12
        assert out["resid_rel"] < 1e-12

    def test_two_port_needs_two_loads(self):
        with pytest.raises(ValueError):
            hb.interface_two_port([{"a": 1.0, "b": 0.1, "c": 0.9, "d": 0.0}])

    def test_signed_gamma_convention(self):
        g, ph = hb.signed_gamma(0.2 * np.exp(1j * (np.pi - 0.1)))
        assert g == pytest.approx(-0.2)
        g2, _ = hb.signed_gamma(0.2 * np.exp(1j * 0.05))
        assert g2 == pytest.approx(+0.2)

    def test_gamma_at_plane_referencing(self):
        """Consumer wiring for gamma_at_plane: on a synthetic two-wave field the
        plane-referenced Gamma is (b/a) e^{2ik x_ref} exactly, and |Gamma| is
        reference-plane invariant."""
        k, a, b = 0.31, 1.3 - 0.4j, -0.22 + 0.05j
        x = np.linspace(0.0, 20.0, 40)
        V = a * np.exp(-1j * k * x) + b * np.exp(1j * k * x)
        fit = hb.fit_two_waves(x, V, k)
        g5 = hb.gamma_at_plane(fit, 5.0)
        assert g5 == pytest.approx((b / a) * np.exp(2j * k * 5.0), abs=1e-12)
        assert abs(g5) == pytest.approx(abs(b / a), abs=1e-12)
        with pytest.raises(ValueError):
            hb.gamma_at_plane({"a": 0.0, "b": b, "k": k}, 0.0)

    def test_bond_midpoints_wrap_into_box(self, srs2):
        """Consumer wiring for BondTable.b_mid (the taper-grading hook, the
        Class-C Rig's b_mid twin): midpoints lie in [0, box) and equal the
        wrapped mean of the unwrapped span."""
        # PINNED to the srs2 (L=2) fixture: L=2 is the net where the
        # np.mod==box float wart actually fires (raw midpoint -5.55e-17);
        # L>=4 never trips it, so re-pointing this fixture would silently
        # make the invariant assertion vacuous.
        net, bt, conn = srs2
        assert np.all((bt.b_mid >= 0.0) & (bt.b_mid < bt.box_cells))
        # equivalence modulo box against the unwrapped midpoint
        raw = bt.b_x0 + 0.5 * bt.b_dx
        d = np.mod(bt.b_mid - raw + 0.5 * bt.box_cells, bt.box_cells) - 0.5 * bt.box_cells
        assert np.max(np.abs(d)) < 1e-9


class TestAlphaFree:
    def test_no_alpha_symbols_in_module(self):
        for sym in ("ALPHA", "Q_TANK", "ELECTRON", "V_SNAP"):
            assert sym not in vars(hb)

    def test_no_constants_reference_anywhere_in_module_code(self):
        """WIDENED (adversarial round 2, L4-5). `vars(hb)` only sees four
        hard-coded names bound at module level, so an import-time capture under
        ANY other name (`_Y_SCALE = 1 + ALPHA`) slipped it — and the doubling
        test below is structurally blind to import-time captures too. This walks
        the module's own AST and rejects ANY reference to the constants module
        or to a calibration symbol, under any binding name, anywhere in the
        CODE (docstrings and comments are not AST nodes, so the header's
        prose about being alpha-free does not self-trip this)."""
        import ast
        import inspect

        banned = {"ALPHA", "Q_TANK", "ELECTRON", "V_SNAP", "V_YIELD", "alpha", "constants"}
        tree = ast.parse(inspect.getsource(hb))
        hits = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Name) and node.id in banned:
                hits.append(node.id)
            elif isinstance(node, ast.Attribute) and node.attr in banned:
                hits.append(node.attr)
            elif isinstance(node, ast.Import):
                hits += [a.name for a in node.names if "constants" in a.name]
            elif isinstance(node, ast.ImportFrom):
                if node.module and "constants" in node.module:
                    hits.append(node.module)
                hits += [a.name for a in node.names if a.name in banned]
        assert not hits, f"calibration symbols referenced in module code: {sorted(set(hits))}"

    def test_operator_bit_identical_under_alpha_doubling(self, srs2):
        """BOUNDED CLAIM (stated 2026-08-25, adversarial round 2): this is a
        CALL-TIME probe. It mutates C.ALPHA between two operator builds, so it
        fires on a RUNTIME alpha read anywhere in the scatter chain — and it is
        structurally BLIND to a constant baked at IMPORT time (already captured
        before the doubling). The import-time hole is covered separately, for
        THIS module, by test_no_constants_reference_anywhere_in_module_code;
        for the shared downstream (vacuum_varactor_scatter / crystal_engine)
        it is covered only by the same call-time bound as the pre-existing
        varactor gate-3 precedent, i.e. it is a CARRIED limitation, not a new
        one. Do not quote this test as an unqualified "alpha-free" proof."""
        import ave.core.constants as C

        net, bt, conn = srs2
        rng = np.random.default_rng(21)
        Ab = rng.uniform(0.2, 0.9, size=bt.n_bonds)
        v = rng.standard_normal((net.n_nodes, net.degree)) + 0j
        a1, _ = hb.scatter_weights(bt, hb.bond_admittance(Ab))
        out1 = hb.apply_M(a1, conn, v)
        orig = C.ALPHA
        try:
            C.ALPHA = 2.0 * orig
            a2, _ = hb.scatter_weights(bt, hb.bond_admittance(Ab))
            out2 = hb.apply_M(a2, conn, v)
        finally:
            C.ALPHA = orig
        assert np.array_equal(out1, out2)


# ─────────────────────────────────────────────────────────────────────────────
# gate 1 fast twin — cold linear limit -> arccos band structure
# ─────────────────────────────────────────────────────────────────────────────


class TestGate1ColdBand:
    def test_nearest_band_gate_can_fire(self, srs2):
        """Anti-tautology / can-it-fire: a deliberately wrong (k, theta) pair
        must sit far from EVERY band, so the 1e-3 rad gate genuinely fires on a
        bad fit (the folded bands are sparse at any k)."""
        net, bt, conn = srs2
        band = hb.nearest_band_theta(net, 0.5, 0.2)  # true acoustic k(0.2) ~ 0.347
        assert band["dev"] > 0.05

    def test_bloch_spectrum_at_gamma_point(self, srs2):
        """mu(k=0) must contain the acoustic mu=3 (row sums, theta=0) and the
        canonical Gamma-optical triplet theta = arccos(-1/3)
        (srs-band-structure.md:44: 3.3093 omega_C = sqrt(3) arccos(-1/3))."""
        net, bt, conn = srs2
        mu = hb.bloch_mu(net, np.zeros(3))
        assert mu[-1] == pytest.approx(3.0, abs=1e-9)
        th = hb.arccos_theta(mu)
        target = np.arccos(-1.0 / 3.0)
        assert np.sum(np.abs(th - target) < 1e-9) >= 3

    def test_driven_dispersion_matches_arccos_map(self):
        """Gate-1 fast twin: drive a cold L=4 net at theta, fit k, and check
        (i) theta_arccos(k_fit) == theta (the canonical TL map,
        srs-band-structure.md:38 — NOT the rejected sqrt(lambda) map) and
        (ii) c = theta/k within the frozen 2% CS-2 velocity gate of
        ANALYTIC_NETWORK_FACTOR (imported, never hard-coded)."""
        net = build_srs_net(L=4)
        bt = hb.build_bond_table(net)
        conn = net.connect_index()
        a_nodes, _ = _cold(bt)
        term = _plane_term(
            net, bt, conn, [(0.5, [1.0 + 0j], [0.0 + 0j]), (2.5, [0.0 + 0j], [0.0 + 0j])]
        )
        theta = 0.2
        sol = hb.solve_tone(a_nodes, conn, theta, term, 0, warmstart=300)
        assert sol.residual_rel < 1e-9
        x, V = hb.plane_binned_voltage(net, a_nodes, sol.v, 0.8, 2.2)
        k0 = theta / ANALYTIC_NETWORK_FACTOR
        fit = hb.fit_k(x, V, 0.6 * k0, 1.4 * k0)
        assert fit["resid_rel"] < 1e-6
        band = hb.nearest_band_theta(net, fit["k"], theta)
        assert band["dev"] < 1e-3
        # below the first band crossing the nearest band IS the mu_max acoustic
        # branch — pin the identification so the nearest-band rule cannot
        # silently drift (anti-tautology cross-check)
        mu_acoustic = hb.bloch_mu(net, np.array([fit["k"], 0.0, 0.0]))[-1]
        assert band["theta_band"] == pytest.approx(float(hb.arccos_theta(mu_acoustic)), abs=1e-12)
        c = theta / fit["k"]
        assert abs(c - ANALYTIC_NETWORK_FACTOR) / ANALYTIC_NETWORK_FACTOR < 0.02


# ─────────────────────────────────────────────────────────────────────────────
# gate 2 fast twin — graded interface Gamma vs the canonical core locus
# ─────────────────────────────────────────────────────────────────────────────


def _gj_interface_gamma(L, x_I, x_B, A, theta, load_planes, feed, slab_margin=0.3):
    """Solve the G-J-style graded interface at each load plane and de-embed
    the interface's own Gamma (the module's documented gate-2 chain)."""
    net = build_srs_net(L=L)
    bt = hb.build_bond_table(net)
    conn = net.connect_index()
    x0, x1 = bt.b_x0, bt.b_x0 + bt.b_dx
    lo, hi = np.minimum(x0, x1), np.maximum(x0, x1)
    inside = (lo > x_I) & (hi < x_B)
    Ab = np.zeros(bt.n_bonds)
    Ab[inside] = A
    a_nodes, Yp = hb.scatter_weights(bt, hb.bond_admittance(Ab))
    k0 = theta / ANALYTIC_NETWORK_FACTOR
    xref = x_I * net.a_cell
    runs = []
    for x_abs in load_planes:
        term = _plane_term(
            net, bt, conn, [(0.5, [1.0 + 0j], [0.0 + 0j]), (x_abs, [0.0 + 0j], [0.0 + 0j])]
        )
        sol = hb.solve_tone(a_nodes, conn, theta, term, 0, warmstart=600)
        assert sol.residual_rel < 1e-9
        xf, Vf = hb.plane_binned_voltage(net, a_nodes, sol.v, feed[0], feed[1])
        fitf = hb.fit_k(xf, Vf, 0.6 * k0, 1.4 * k0)
        k = fitf["k"]
        xs, Vs = hb.plane_binned_voltage(net, a_nodes, sol.v, x_I + slab_margin, x_abs - slab_margin)
        fits = hb.fit_two_waves(xs, Vs, k)
        runs.append(
            {
                "a": fitf["a"] * np.exp(-1j * k * xref),
                "b": fitf["b"] * np.exp(+1j * k * xref),
                "c": fits["a"] * np.exp(-1j * k * xref),
                "d": fits["b"] * np.exp(+1j * k * xref),
            }
        )
    return hb.interface_two_port(runs)


class TestGate2GradedInterface:
    def test_graded_interface_draws_core_locus(self):
        """Gate-2 fast twin at L=6: the de-embedded interface Gamma lands on
        the canonical core locus Gamma = (Z-Z0)/(Z+Z0), Z = Z0 sqrt(S(A))
        (cvr-reflection-smith.md:24) with the far side matched — the same locus
        the MEASURED Class-C G-J drew to ~1%. Full measured-map comparison at
        L=24 lives in research/drivers/harmonic_balance_validation.py."""
        A = 0.9
        out = _gj_interface_gamma(
            L=6, x_I=3.0, x_B=6.0, A=A, theta=0.15, load_planes=(4.5, 5.0, 5.5), feed=(0.8, 2.8)
        )
        assert out["resid_rel"] < 1e-4
        S = float(np.sqrt(np.clip(1.0 - A * A, 0.0, 1.0)))
        z = np.sqrt(S)
        gamma_core = (z - 1.0) / (z + 1.0)
        g_signed, ph = hb.signed_gamma(out["gamma"])
        assert g_signed < 0.0  # polarity-inverted (the mu-load short side)
        assert abs(g_signed - gamma_core) < 0.01

    def test_cold_interface_gamma_is_null(self):
        """A=0 through the identical chain must give Gamma ~ 0 (the CS-5-style
        null: de-embedding removes the scaffold's own load artifact)."""
        out = _gj_interface_gamma(
            L=6, x_I=3.0, x_B=6.0, A=0.0, theta=0.15, load_planes=(4.5, 5.0, 5.5), feed=(0.8, 2.8)
        )
        assert abs(out["gamma"]) < 1e-3
        assert abs(out["t"] - 1.0) < 1e-3


# ─────────────────────────────────────────────────────────────────────────────
# gate 3 — source-idle machinery on the known driven-vs-autonomous pair
# ─────────────────────────────────────────────────────────────────────────────


class TestGate3SourceIdle:
    def test_initialized_lossless_ring_is_source_idle(self, ring12):
        """The trivial side of the brief's known pair: a ring eigenmode is a
        source-free fixed point of the intact network (r_auto ~ 0)."""
        net, bt, conn = ring12
        a_nodes, Yp = _cold(bt)
        v, k = hb.ring_mode(12, 2)
        # exact fixed point receipt
        defect = np.linalg.norm(np.exp(1j * k) * v - hb.apply_M(a_nodes, conn, v))
        assert defect / np.linalg.norm(v) < 1e-13
        sol = hb.ToneSolution(theta=k, v=v, residual_rel=0.0, converged=True, n_matvec=0, method="exact")
        rep = hb.source_idle_report(a_nodes, conn, None, [sol], Yp)
        verdict = hb.idle_verdict(rep, source_tol=1e-12, exchange_tol=1e-12, r_auto_tol=1e-10)
        assert verdict["idle"]

    def test_driven_cold_tank_never_goes_idle(self, srs2):
        """The driven side: a source-terminated cold srs tank at a generic tone
        carries scaffold exchange O(drive) and a large autonomous defect."""
        net, bt, conn = srs2
        a_nodes, Yp = _cold(bt)
        term = _plane_term(net, bt, conn, [(0.5, [1.0 + 0j], [0.0 + 0j])])
        sol = hb.solve_tone(a_nodes, conn, 0.3, term, 0, warmstart=200)
        rep = hb.source_idle_report(a_nodes, conn, term, [sol], Yp)
        verdict = hb.idle_verdict(rep, source_tol=1e-12, exchange_tol=1e-12, r_auto_tol=1e-10)
        assert not verdict["idle"]
        assert rep["max_source_amp"] == pytest.approx(1.0)
        assert rep["max_exchange_amp"] > 0.1  # the lossless tank returns O(1) to the scaffold
        assert rep["max_r_auto"] > 0.01

    def test_ring_driven_then_scaffold_removed_distinguishes(self, ring12):
        """Cross-wiring guard: the SAME machinery, applied to the ring's exact
        mode with a termination PRESENT but untouched by the mode, still reads
        idle only because the observables are computed (nothing is declared)."""
        net, bt, conn = ring12
        a_nodes, Yp = _cold(bt)
        v, k = hb.ring_mode(12, 3)
        f, b = hb.crossing_ports(net, bt, 5.5)
        term = hb.make_termination(
            net, bt, conn, [(f, np.zeros((1, len(f)))), (b, np.zeros((1, len(b))))], 1
        )
        sol = hb.ToneSolution(theta=k, v=v, residual_rel=0.0, converged=True, n_matvec=0, method="exact")
        rep = hb.source_idle_report(a_nodes, conn, term, [sol], Yp)
        # the traveling mode DOES cross the cut plane => the scaffold absorbs it
        # => NOT idle in this configuration; the observable says so.
        verdict = hb.idle_verdict(rep, source_tol=1e-12, exchange_tol=1e-12, r_auto_tol=1e-10)
        assert rep["max_exchange_amp"] > 0.5
        assert not verdict["idle"]


# ─────────────────────────────────────────────────────────────────────────────
# self-consistent S-field fixed point
# ─────────────────────────────────────────────────────────────────────────────


class TestSelfConsistent:
    def test_outer_fixed_point_converges_and_reads_saturation(self, srs2):
        """Driven L=2 net at finite amplitude: the outer S-field loop converges
        (computed dA receipt) and the converged A equals the DP-1 envelope of
        the final tone solutions."""
        net, bt, conn = srs2
        term = _plane_term(net, bt, conn, [(0.5, [0.6 + 0j], [0.0 + 0j])])
        tones = hb.ToneSet(thetas=(0.3,))
        res = hb.solve_self_consistent(
            net,
            bt,
            tones,
            term,
            relax=0.7,
            outer_tol=1e-11,
            max_outer=200,
            solve_kwargs={"warmstart": 200},
        )
        assert res.converged
        assert res.history[-1]["dA_inf"] < 1e-11
        A_env = hb.envelope_A_bond(bt, res.sols)
        assert np.max(np.abs(A_env - res.A_bond)) < 1e-9
        # the solution genuinely engages the kernel (A > 0 somewhere)
        assert res.A_bond.max() > 0.05
        assert res.S_bond.min() < 1.0 - 1e-4

    def test_two_tone_set_couples_through_shared_S_field(self, srs2):
        """End-to-end MULTI-tone machinery (the brief's unknowns are 'phasors
        at the posited tone set' + the S-field): a 2-tone driven solve
        converges, both tones' fixed-point residuals hold on the SAME graded
        network, the envelope sums both tones (DP-1), and the coupling is
        real — the second tone's presence CHANGES the first tone's solution
        relative to its single-tone solve (through the shared S-field only)."""
        net, bt, conn = srs2
        f, b = hb.crossing_ports(net, bt, 0.5)
        drive2 = hb.make_termination(
            net, bt, conn,
            [(f, np.array([0.6 + 0j, 0.5 + 0j])), (b, np.zeros((2, len(b))))],
            2,
        )
        tones2 = hb.ToneSet(thetas=(0.3, 0.45))
        res2 = hb.solve_self_consistent(
            net, bt, tones2, drive2, relax=0.7, outer_tol=1e-11, max_outer=300,
            solve_kwargs={"warmstart": 200},
        )
        assert res2.converged
        assert all(s.residual_rel < 1e-8 for s in res2.sols)
        assert np.max(np.abs(hb.envelope_A_bond(bt, res2.sols) - res2.A_bond)) < 1e-9
        # single-tone reference at the same drive for tone 0
        drive1 = hb.make_termination(
            net, bt, conn,
            [(f, np.array([0.6 + 0j])), (b, np.zeros((1, len(b))))],
            1,
        )
        res1 = hb.solve_self_consistent(
            net, bt, hb.ToneSet(thetas=(0.3,)), drive1, relax=0.7, outer_tol=1e-11,
            max_outer=300, solve_kwargs={"warmstart": 200},
        )
        assert res1.converged
        dv = np.max(np.abs(res2.sols[0].v - res1.sols[0].v))
        assert dv > 1e-6  # the shared S-field genuinely couples the tones
        # CAN-FIRE control (re-audit repair, 2026-08-25 — the earlier "cold
        # decoupling control" compared two bitwise-identical solves and could
        # never fail): the coupling channel is the S-field ALONE, so tone 0
        # re-solved on the FROZEN 2-tone converged S-field, with tone 1's
        # drive absent, must reproduce the 2-tone solution's tone-0 phasors.
        # Any non-S coupling channel in the solve would break this.
        Yb_frozen = hb.bond_admittance(res2.A_bond)
        a_frozen, _ = hb.scatter_weights(bt, Yb_frozen)
        s0_frozen = hb.solve_tone(a_frozen, conn, 0.3, drive1, 0, warmstart=400)
        assert s0_frozen.residual_rel < 1e-8
        assert np.max(np.abs(s0_frozen.v - res2.sols[0].v)) < 1e-7
        # and the same re-solve on the SINGLE-tone converged S-field differs
        # from the 2-tone tone-0 solution (the control can fire both ways)
        a_single, _ = hb.scatter_weights(bt, hb.bond_admittance(res1.A_bond))
        s0_single = hb.solve_tone(a_single, conn, 0.3, drive1, 0, warmstart=400)
        assert np.max(np.abs(s0_single.v - res2.sols[0].v)) > 1e-6


# ─────────────────────────────────────────────────────────────────────────────
# regression binding — committed validation receipts stay reconciled
# ─────────────────────────────────────────────────────────────────────────────

_RECEIPTS = _REPO / "research" / "drivers" / "data" / "harmonic_balance_validation" / "receipts.json"
_MEASURED = _REPO / "research" / "drivers" / "engine_gamma_meanstest_results.json"
_DRIVER = _REPO / "research" / "drivers" / "harmonic_balance_validation.py"


def _frozen_driver_params():
    """The driver's `P = {...}` block, read from the driver SOURCE by AST.

    Adversarial round 3 (L5-1, second surface): the gating checker
    (research/drivers/harmonic_balance_number_check.py) reconciles the
    receipts' tolerances against this frozen literal, but THIS arm still
    consumed `g1["velocity_tol"]`, `g2["tol_abs_floor"]`, `g2["tol_rel"]`,
    `g3["thresholds"][...]` etc. as self-declared receipt fields — the exact
    'gate consuming self-declared fields is a checklist not a gate' shape. An
    on-disk tamper that widened a tolerance and recomputed every per-point
    verdict consistently passed this class silently. The equivalent binding is
    added below (test_receipt_tolerances_reconcile_against_frozen_driver).

    The driver is parsed, never imported and never executed."""
    tree = ast.parse(_DRIVER.read_text(), filename=str(_DRIVER))
    for node in tree.body:
        if (
            isinstance(node, ast.Assign)
            and len(node.targets) == 1
            and isinstance(node.targets[0], ast.Name)
            and node.targets[0].id == "P"
        ):
            return ast.literal_eval(node.value)
    return None


def _same(a, b):
    """Structural equality for a declared-constant reconciliation (mirrors the
    number check's `same`): floats by tolerance, sequences elementwise, else ==."""
    if isinstance(a, bool) or isinstance(b, bool):
        return a == b
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return abs(float(a) - float(b)) <= max(1e-12, 1e-12 * max(abs(a), abs(b)))
    if isinstance(a, (list, tuple)) and isinstance(b, (list, tuple)):
        return len(a) == len(b) and all(_same(x, y) for x, y in zip(a, b))
    return a == b


def test_receipts_of_record_exist():
    """FAIL-LOUD, not skip (adversarial round 2, L5-6). This class used to sit
    behind `@pytest.mark.skipif(not _RECEIPTS.exists())`. The receipts ARE
    committed, so that guard could never legitimately fire on a checkout — its
    only live effect was to make the four regression-binding tests VANISH
    SILENTLY (green suite) if receipts.json were deleted or moved. A missing
    evidence file is a failure, and it is now reported as one."""
    assert _RECEIPTS.exists(), (
        f"committed validation receipts are missing: {_RECEIPTS}. They are the "
        "evidence the regression-binding tests bind to — a missing evidence file "
        "FAILS this suite, it does not skip it. Regenerate with: PYTHONPATH=src "
        "python research/drivers/harmonic_balance_validation.py"
    )
    assert _MEASURED.exists(), f"committed measured Class-C source is missing: {_MEASURED}"
    assert _DRIVER.exists(), (
        f"the frozen driver source is missing: {_DRIVER}. Its `P` literal is the "
        "frozen source the receipts' tolerances reconcile against."
    )


class TestReceiptsReconciled:
    """Bind the committed gate receipts to the committed measured data: the
    reported verdicts must recompute from the numbers in the files (the
    test_f6_floor_battery.py / test_stage2_native_cage_imex_result_gate.py
    precedent — a reported verdict cannot silently drift from its evidence).
    Regenerate: PYTHONPATH=src python research/drivers/harmonic_balance_validation.py
    """

    @pytest.fixture(scope="class")
    def receipts(self):
        return json.loads(_RECEIPTS.read_text())

    def test_receipt_tolerances_reconcile_against_frozen_driver(self, receipts):
        """reconcile-don't-declare AT THE TOLERANCE LAYER (adversarial round 3,
        L5-1 second surface). Every verdict this class recomputes is recomputed
        AGAINST A TOLERANCE READ OUT OF THE RECEIPTS. That closes drift in the
        measured numbers and leaves the yardstick self-declared: widen
        `gate2.tol_abs_floor` on disk from 0.01 to 1.0, recompute every
        `tol_point` and `pass` consistently, and every other test in this class
        still passes — the gate becomes unfalsifiable and stays green.

        The gating checker already reconciles these against the driver's frozen
        `P` literal; this is the same binding on the pytest arm, so the hole is
        closed in both places rather than only on the `make verify` path.
        Failing here means one of: someone widened a tolerance in the receipts
        without changing the driver, or changed the driver without regenerating
        the receipts. Both are FAILs, not drift to be absorbed."""
        P = _frozen_driver_params()
        assert P is not None, (
            f"could not read the frozen `P` parameter literal out of {_DRIVER} — the "
            "tolerance reconciliation has no frozen source to check against, and a "
            "reconciler with no source is a checklist. Keep P a literal dict."
        )
        g1, g2, g3 = receipts["gate1"], receipts["gate2"], receipts["gate3"]
        thr = g3["thresholds"]
        assert set(receipts["parameters"]) == set(P)
        for key in P:
            assert _same(receipts["parameters"][key], P[key]), (
                f"receipts.parameters[{key!r}] = {receipts['parameters'][key]!r} "
                f"contradicts the driver's frozen P[{key!r}] = {P[key]!r}"
            )
        for name, val, key in (
            ("gate1.L", g1["L"], "g1_L"),
            ("gate1.velocity_tol", g1["velocity_tol"], "g1_velocity_tol"),
            ("gate1.arccos_tol", g1["arccos_tol"], "g1_arccos_tol"),
            ("gate1.band_edge_tol", g1["band_edge_tol"], "g1_band_edge_tol"),
            ("gate2.theta", g2["theta"], "g2_theta"),
            ("gate2.load_planes", g2["load_planes"], "g2_load_planes"),
            ("gate2.tol_abs_floor", g2["tol_abs_floor"], "g2_tol_abs_floor"),
            ("gate2.tol_rel", g2["tol_rel"], "g2_tol_rel"),
            ("gate3.thresholds.source_tol", thr["source_tol"], "g3_source_tol"),
            ("gate3.thresholds.exchange_tol", thr["exchange_tol"], "g3_exchange_tol"),
            ("gate3.thresholds.r_auto_tol", thr["r_auto_tol"], "g3_r_auto_tol"),
            ("gate3.ring.N", g3["ring"]["N"], "g3_ring_N"),
            ("gate3.ring.m", g3["ring"]["m"], "g3_ring_m"),
            ("gate3.driven_tank.L", g3["driven_tank"]["L"], "g3_tank_L"),
            ("gate3.driven_tank.theta", g3["driven_tank"]["theta"], "g3_tank_theta"),
        ):
            assert key in P, f"driver P lost {key!r}, which receipts.{name} is bound to"
            assert _same(val, P[key]), (
                f"receipts.{name} = {val!r} contradicts the driver's frozen "
                f"P[{key!r}] = {P[key]!r}"
            )
        assert _same([p["theta"] for p in g1["points"]], P["g1_theta_sweep"])
        assert receipts.get("driver") == "research/drivers/harmonic_balance_validation.py"

    def test_tolerance_reconciler_can_fire(self, receipts):
        """Anti-tautology control for the test above: the on-disk tamper the
        review demonstrated must actually break it. Mutates an IN-MEMORY copy
        (no file is touched) exactly as the checker's `_mut_tol` does — widen
        the gate-2 floor to a value at which |dGamma| <= tol is unfalsifiable
        and recompute every per-point tolerance and verdict consistently — and
        asserts (i) the arithmetic tests in this class still see nothing wrong,
        which is the hole, and (ii) the reconciler above rejects it."""
        r = copy.deepcopy(receipts)
        g2 = r["gate2"]
        g2["tol_abs_floor"] = 1.0
        for pt in g2["points"]:
            pt["tol_point"] = max(1.0, g2["tol_rel"] * abs(pt["gamma_measured"]))
            pt["pass"] = abs(pt["gamma_solver"] - pt["gamma_measured"]) <= pt["tol_point"]
        # (i) the hole: the self-consistent tamper survives the arithmetic arm
        self.test_gate2_verdict_recomputes_against_measured_map(r)
        # (ii) the reconciler catches it
        with pytest.raises(AssertionError):
            self.test_receipt_tolerances_reconcile_against_frozen_driver(r)

    def test_committed_receipts_are_passing(self, receipts):
        """The landed instrument's receipts of record must be PASSING ones —
        and the all_pass composition is recomputed HERE from the three per-gate
        fields (whose own verdicts the tests below recompute from evidence), so
        no self-declared field is consumed bare."""
        composed = (
            receipts["gate1"]["pass"] and receipts["gate2"]["pass"] and receipts["gate3"]["pass"]
        )
        assert receipts["all_pass"] == composed
        assert receipts["all_pass"] is True

    def test_gate1_verdict_recomputes(self, receipts):
        g1 = receipts["gate1"]
        c0 = g1["c_smallest_theta"]
        rel = abs(c0 - ANALYTIC_NETWORK_FACTOR) / ANALYTIC_NETWORK_FACTOR
        assert rel == pytest.approx(g1["velocity_rel_dev"], rel=1e-9)
        assert (rel < g1["velocity_tol"]) == g1["velocity_pass"]
        dev = max(abs(r["theta_arccos"] - r["theta"]) for r in g1["points"])
        assert dev == pytest.approx(g1["max_arccos_dev"], rel=1e-9, abs=1e-15)
        assert (dev < g1["arccos_tol"]) == g1["arccos_pass"]
        assert g1["pass"] == (g1["velocity_pass"] and g1["arccos_pass"] and g1["band_edge_pass"])

    def test_gate2_verdict_recomputes_against_measured_map(self, receipts):
        g2 = receipts["gate2"]
        measured = json.loads(_MEASURED.read_text())["table"]["GJ"]
        meas_by_A = {row["A"]: row for row in measured}
        n_checked = 0
        worst = 0.0
        for pt in g2["points"]:
            row = meas_by_A[pt["A"]]
            assert row["valid"], "gate-2 points must be the measured-valid ones"
            assert pt["gamma_measured"] == pytest.approx(row["gamma"], rel=1e-12)
            dev = abs(pt["gamma_solver"] - pt["gamma_measured"])
            assert dev == pytest.approx(pt["abs_dev"], rel=1e-9, abs=1e-15)
            tol_pt = max(g2["tol_abs_floor"], g2["tol_rel"] * abs(pt["gamma_measured"]))
            assert (dev <= tol_pt) == pt["pass"]
            worst = max(worst, dev)
            n_checked += 1
        assert n_checked == g2["n_points"]
        assert worst == pytest.approx(g2["max_abs_dev"], rel=1e-9, abs=1e-15)
        assert g2["pass"] == all(pt["pass"] for pt in g2["points"])

    def test_gate3_verdict_recomputes(self, receipts):
        g3 = receipts["gate3"]
        ring, tank = g3["ring"], g3["driven_tank"]
        thr = g3["thresholds"]
        ring_idle = (
            ring["max_source_amp"] <= thr["source_tol"]
            and ring["max_exchange_amp"] <= thr["exchange_tol"]
            and ring["max_r_auto"] <= thr["r_auto_tol"]
        )
        tank_idle = (
            tank["max_source_amp"] <= thr["source_tol"]
            and tank["max_exchange_amp"] <= thr["exchange_tol"]
            and tank["max_r_auto"] <= thr["r_auto_tol"]
        )
        assert ring_idle == ring["idle"]
        assert tank_idle == tank["idle"]
        assert g3["pass"] == (ring["idle"] and not tank["idle"])
