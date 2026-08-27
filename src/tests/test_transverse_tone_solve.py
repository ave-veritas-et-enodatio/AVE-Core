"""Gates for BUILD-EO1-T2X — the tone-solve harness on the transverse container.

Module under test: `ave.solvers.transverse_tone_solve` (instrument-grade; mints
no physics claims, adjudicates no fork). Every test here is
IMPLEMENTATION-VERIFICATION of an instrument -- the consistency /
known-case / instrument-cross-validation classes of consistency-vs-emergence.
Nothing in this file is in the emergence class and nothing here asserts physics
beyond what the shipped operator and the canonical kernel already carry.

Three families:
  * PARITY   -- the port must reproduce the SCALAR container exactly in the
                c = 1 restriction (operator, coefficients, solved field,
                fitted k, de-embedded Gamma);
  * FL-4     -- the silent-zero trap is pinned on the scalar twin (so the
                defect cannot silently disappear and make the fix look
                unnecessary) and shown FIXED, in both directions, on the port;
  * KNOWN    -- the frozen chain fixture reproduces the ANALYTIC Fresnel step
                Gamma = (sqrt(S)-1)/(sqrt(S)+1), with the A = 0 control.
                GUARD (b): that A = 0 null is a UNIFORM-BROADCAST null -- an
                instrument control, guaranteed by the cancellation identity,
                never evidence about a wall.
"""

from __future__ import annotations

import ast
import inspect

import numpy as np
import pytest

import ave.solvers.harmonic_balance_srs as hb
import ave.solvers.transverse_tone_solve as tt
from ave.core.chiral_lattice import build_srs_net
from ave.core.chiral_lattice_dynamics import ANALYTIC_NETWORK_FACTOR
from ave.solvers import transverse_graded_scatter as tgs

BANKED_L24_A099_SCALAR_GAMMA = -0.45409225467790404
"""The scalar validation driver's de-embedded L=24, A=0.99 interface Gamma,
verbatim from research/drivers/data/harmonic_balance_validation/receipts.json
("gamma_solver"). Quoted as a REGRESSION TARGET for the port, not as physics."""


# ---------------------------------------------------------------------------
# fixtures
# ---------------------------------------------------------------------------
@pytest.fixture(scope="module")
def srs4():
    net = build_srs_net(L=4)
    return net, hb.build_bond_table(net), net.connect_index()


def slab(bt, A, lo=1.0, hi=3.0):
    """Per-bond slab grading: A on bonds strictly inside (lo, hi) cells, else cold.
    NON-BROADCAST BY CONSTRUCTION (the point of guard (b)): the grading is mixed
    across the ports of every boundary node, which is what
    tgs.gate_t1b_boundary_set verifies."""
    x0, x1 = bt.b_x0, bt.b_x0 + bt.b_dx
    lo_x, hi_x = np.minimum(x0, x1), np.maximum(x0, x1)
    Ab = np.zeros(bt.n_bonds)
    Ab[(lo_x > lo) & (hi_x < hi)] = A
    return Ab


def chain_term(kc, pol=(1.0, 0.0), d_load=0.0 + 0j):
    """The frozen chain's scaffold: a +x drive at x_src with its backward slot
    absorbed, and a far-side load plane whose +x direction is left FREE."""
    g = kc["geom"]
    src = np.array([[pol[0] + 0j, pol[1] + 0j]])
    back = np.array([[d_load * pol[0], d_load * pol[1]]])
    return tt.plane_termination(
        kc["net"], kc["bt"], kc["conn"],
        [(g["x_src"], src, np.zeros((1, 2), dtype=np.complex128)),
         (g["x_abs"], None, back)],
        1,
    )


# ═══════════════════════════════════════════════════════════════════════════
# PARITY — the c = 1 restriction must reproduce the scalar container
# ═══════════════════════════════════════════════════════════════════════════
class TestScalarParity:
    def test_admittance_and_coefficients_are_bit_identical(self, srs4):
        """The magnetic (mu-load) map Y = Y0/sqrt(S) is the scalar harness's
        one and only map, so the bridge must agree BIT-FOR-BIT on the measured
        grid -- not merely allclose. (The shipped clip A_cap=0.99 / floor
        S_min=0.05 are inactive on A in [0, 0.99], which is what makes the
        exact-vs-clipped kernels identical there.)"""
        _net, bt, _conn = srs4
        # the whole measured grid, INCLUDING A = 0.99 -- the banked L=24
        # regression compares a tgs-kernel build against a driver number built
        # on the hb (clipped) kernel at exactly that amplitude, so parity there
        # is load-bearing and not incidental.
        grid = np.array([0.0, 0.1, 0.5, 0.8, 0.9, 0.95, 0.9682, 0.98, 0.99])
        assert np.array_equal(
            tgs.bond_admittance(grid, "magnetic"), hb.bond_admittance(grid)
        )
        A = slab(bt, 0.9)
        assert np.array_equal(tgs.bond_admittance(A, "magnetic"), hb.bond_admittance(A))
        a_v, Y_v = tt.graded_coeffs(bt, A, "magnetic")
        a_s, Y_s = hb.scatter_weights(bt, hb.bond_admittance(A))
        assert np.array_equal(a_v, a_s)
        assert np.array_equal(Y_v, Y_s)

    def test_apply_M_vector_is_apply_M_at_c_equals_1(self, srs4):
        """apply_M_vector IS vector_graded_step on complex phasors, and the
        scalar apply_M is its c = 1 restriction: bit-exact, both components."""
        net, bt, conn = srs4
        a, _ = tt.graded_coeffs(bt, slab(bt, 0.9), "magnetic")
        rng = np.random.default_rng(4)
        vs = rng.standard_normal((net.n_nodes, net.degree)) + 1j * rng.standard_normal(
            (net.n_nodes, net.degree)
        )
        v = np.zeros((net.n_nodes, net.degree, 2), dtype=np.complex128)
        v[:, :, 0] = vs
        v[:, :, 1] = 1j * vs  # an INDEPENDENT second component, not a copy
        got = tt.apply_M_vector(a, conn, v)
        ref = hb.apply_M(a, conn, vs)
        assert np.array_equal(got[:, :, 0], ref)
        assert np.array_equal(got[:, :, 1], 1j * ref)

    def test_bond_tables_of_the_two_modules_agree(self, srs4):
        """The bridge gathers a per-BOND grading onto ports through the scalar
        harness's port_bond table; the transverse module's own BondTables must
        index bonds identically or an A_bond array would mean different things
        in the two modules (and the reused tgs gates would be testing a
        different grading than the solve)."""
        net, bt, _conn = srs4
        tables = tgs.BondTables(net)
        assert np.array_equal(tables.port_bond, bt.port_bond)
        A = slab(bt, 0.9)
        assert np.array_equal(
            tt.port_admittance(bt, A, "electric"), tables.port_admittance(A, "electric")
        )

    def test_solved_field_matches_the_scalar_solve(self, srs4):
        """Full-chain parity: same net, same grading, same tone, same scaffold.
        Component 1 must be IDENTICALLY zero (the operator is component-diagonal
        and the drive imposes 0 there), and component 0 must match the scalar
        solve to solver precision."""
        net, bt, conn = srs4
        A = slab(bt, 0.9)
        a_v, _ = tt.graded_coeffs(bt, A, "magnetic")
        a_s, _ = hb.scatter_weights(bt, hb.bond_admittance(A))
        f, b = hb.crossing_ports(net, bt, 0.5)
        _f2, b2 = hb.crossing_ports(net, bt, 2.5)
        term_s = hb.make_termination(
            net, bt, conn,
            [(f, np.array([1.0 + 0j])), (b, np.array([0j])), (b2, np.array([0j]))], 1,
        )
        term_v = tt.plane_termination(
            net, bt, conn,
            [(0.5, np.array([[1.0 + 0j, 0j]]), np.zeros((1, 2), dtype=np.complex128)),
             (2.5, None, np.zeros((1, 2), dtype=np.complex128))], 1,
        )
        s_s = hb.solve_tone(a_s, conn, 0.2, term_s, 0, warmstart=300, tol=1e-13)
        s_v = tt.solve_tone_vector(a_v, conn, 0.2, term_v, 0, warmstart=300, tol=1e-13)
        assert s_v.nontrivial and s_v.converged
        assert float(np.max(np.abs(s_v.v[:, :, 1]))) == 0.0
        dev = float(np.max(np.abs(s_v.v[:, :, 0] - s_s.v)))
        assert dev / np.linalg.norm(s_s.v) < 1e-12, dev
        assert s_v.residual_rel == pytest.approx(s_s.residual_rel, rel=1e-6)

    def test_vector_fit_agrees_with_the_scalar_fit_per_component(self):
        """The vector two-wave fit is the multi-RHS form of the scalar one, so
        on any single component it must return exactly the scalar coefficients.
        This is the receipt behind the module docstring's claim of per-component
        agreement -- without it, the multi-RHS lstsq would be an unverified
        second implementation of an algebra the tree already has."""
        k = 0.31
        x = np.linspace(0.0, 20.0, 41)
        a0, b0, a1, b1 = 1.3 - 0.4j, -0.22 + 0.05j, 0.7 + 0.9j, 0.05 - 0.11j
        V = np.column_stack([
            a0 * np.exp(-1j * k * x) + b0 * np.exp(1j * k * x),
            a1 * np.exp(-1j * k * x) + b1 * np.exp(1j * k * x),
        ])
        fit_v = tt.fit_two_waves_vector(x, V, k)
        for c, (ta, tb) in enumerate(((a0, b0), (a1, b1))):
            fit_s = hb.fit_two_waves(x, V[:, c], k)
            assert complex(fit_v["a"][c]) == pytest.approx(fit_s["a"], abs=1e-12)
            assert complex(fit_v["b"][c]) == pytest.approx(fit_s["b"], abs=1e-12)
            assert complex(fit_v["a"][c]) == pytest.approx(ta, abs=1e-10)
            assert complex(fit_v["b"][c]) == pytest.approx(tb, abs=1e-10)
        assert fit_v["resid_rel"] < 1e-12


# ═══════════════════════════════════════════════════════════════════════════
# REUSED GATES — the existing SO(2)-equivariance / energy / cancellation gates,
# run AS-IS on the coefficients this module's bridge builds
# ═══════════════════════════════════════════════════════════════════════════
class TestReusedGates:
    @pytest.mark.parametrize("load", ["magnetic", "electric"])
    def test_so2_equivariance_gate_as_is(self, srs4, load):
        net, bt, _conn = srs4
        g = tgs.gate_so2_equivariance(net, tgs.BondTables(net), slab(bt, 0.9), load, steps=40)
        assert g["pass"], g

    def test_solve_is_so2_equivariant(self, srs4):
        """NEW gate (the reused one covers the STEP, not the SOLVE): rotating
        the drive polarization by phi must rotate the solved field by phi. If
        the port had leaked a component-asymmetry into the termination or the
        mask packing, this fires."""
        net, bt, conn = srs4
        a, _ = tt.graded_coeffs(bt, slab(bt, 0.9), "magnetic")
        phi = 0.7
        c, s = np.cos(phi), np.sin(phi)
        sols = []
        for pol in ((1.0, 0.0), (c, s)):
            term = tt.plane_termination(
                net, bt, conn,
                [(0.5, np.array([[pol[0] + 0j, pol[1] + 0j]]),
                  np.zeros((1, 2), dtype=np.complex128)),
                 (2.5, None, np.zeros((1, 2), dtype=np.complex128))], 1,
            )
            sols.append(tt.solve_tone_vector(a, conn, 0.2, term, 0, warmstart=300, tol=1e-13).v)
        rot = np.empty_like(sols[0])
        rot[..., 0] = c * sols[0][..., 0] - s * sols[0][..., 1]
        rot[..., 1] = s * sols[0][..., 0] + c * sols[0][..., 1]
        assert float(np.max(np.abs(rot - sols[1]))) < 1e-11

    def test_energy_Y_phasor_extends_the_reused_real_field_gate(self, srs4):
        """energy_Y_phasor must AGREE with the reused real-field
        tgs.energy_Y on a real field (so it is an extension, not a rival), and
        must be conserved by apply_M_vector on COMPLEX phasors (Ax3)."""
        net, bt, conn = srs4
        a, Y = tt.graded_coeffs(bt, slab(bt, 0.9), "magnetic")
        rng = np.random.default_rng(11)
        Vr = rng.standard_normal((net.n_nodes, net.degree, 2))
        assert tt.energy_Y_phasor(Vr, Y) == pytest.approx(tgs.energy_Y(Vr, Y), rel=0, abs=0)
        v = Vr + 1j * rng.standard_normal((net.n_nodes, net.degree, 2))
        E0 = tt.energy_Y_phasor(v, Y)
        drift = 0.0
        for _ in range(100):
            v = tt.apply_M_vector(a, conn, v)
            drift = max(drift, abs(tt.energy_Y_phasor(v, Y) - E0) / E0)
        assert drift < 1e-12, drift

    def test_structural_null_trap_is_inherited(self, srs4):
        """GUARD (b), both directions. A per-node-UNIFORM (broadcast) grading
        cancels identically in the bridge's coefficients -- so a null obtained
        that way is an artifact. A per-bond-MIXED grading does NOT cancel, and
        the deviating-node set equals the mixed-admittance set."""
        net, bt, _conn = srs4
        tables = tgs.BondTables(net)
        assert tgs.gate_t1a_global_uniform(net, tables, 0.9, "magnetic")["pass"]
        a_uniform, _ = tt.graded_coeffs(bt, np.full(bt.n_bonds, 0.9), "magnetic")
        assert np.max(np.abs(a_uniform - 2.0 / net.degree)) <= 1e-13
        g = tgs.gate_t1b_boundary_set(tables, slab(bt, 0.9), "magnetic")
        assert g["pass"], g
        a_graded, _ = tt.graded_coeffs(bt, slab(bt, 0.9), "magnetic")
        assert np.max(np.abs(a_graded - 2.0 / net.degree)) > 1e-3


# ═══════════════════════════════════════════════════════════════════════════
# FL-4 — the live silent-zero trap: PINNED on the twin, FIXED on the port
# ═══════════════════════════════════════════════════════════════════════════
class TestFL4:
    def test_scalar_twin_silent_zero_is_pinned(self):
        """PIN THE DEFECT (not a regression test of the port -- a regression
        test of the REASON the port needed a fix). If the scalar harness is
        ever repaired upstream this test turns red, which is the signal to
        re-scope the port's guard rather than to quietly assume it is moot.

        All four configurations return ||v|| = 0 with converged=True AND
        residual_rel = 0.0 -- including the one warm-started AT the exact ring
        mode, because theta is an INPUT and the right-hand side is zero."""
        net = hb.build_ring_net(12)
        bt = hb.build_bond_table(net)
        conn = net.connect_index()
        a, _ = hb.scatter_weights(bt, hb.bond_admittance(np.zeros(bt.n_bonds)))
        v_true, k = hb.ring_mode(12, 2)
        # the mode really is an exact fixed point of the intact operator
        assert np.linalg.norm(np.exp(1j * k) * v_true - hb.apply_M(a, conn, v_true)) < 1e-13
        for warm, x0 in ((0, None), (50, None), (0, v_true), (300, v_true)):
            s = hb.solve_tone(a, conn, k, None, 0, warmstart=warm, x0=x0)
            assert float(np.linalg.norm(s.v)) == 0.0
            assert s.converged is True
            assert s.residual_rel == 0.0

    def test_port_refuses_the_homogeneous_case(self):
        """Layer 1 of the fix: term=None and an all-zero drive are BOTH
        refused before the solve is even attempted."""
        kc = tt.known_case_chain(0.0)
        a, conn = kc["a_nodes"], kc["conn"]
        with pytest.raises(ValueError, match="HOMOGENEOUS"):
            tt.solve_tone_vector(a, conn, kc["geom"]["theta"], None, 0)
        dead = chain_term(kc, pol=(0.0, 0.0))
        assert dead.is_homogeneous(0)
        with pytest.raises(ValueError, match="HOMOGENEOUS"):
            tt.solve_tone_vector(a, conn, kc["geom"]["theta"], dead, 0)

    def test_degenerate_branch_is_opt_in_and_self_reporting(self):
        """Layer 2: with require_nontrivial=False the trivial branch is
        available, but it CANNOT be mistaken for a solve -- nontrivial is
        False and residual_rel is +inf, so a gate written `residual_rel < tol`
        FAILS on it (where the scalar twin's 0.0 would pass)."""
        kc = tt.known_case_chain(0.0)
        s = tt.solve_tone_vector(
            kc["a_nodes"], kc["conn"], kc["geom"]["theta"], None, 0, require_nontrivial=False
        )
        assert s.v_norm == 0.0
        assert s.nontrivial is False
        assert s.homogeneous is True
        assert s.converged is True  # the solver flag is reported verbatim
        assert s.residual_rel == float("inf")
        assert not (s.residual_rel < 1e-9)  # the gate a caller would write FIRES

    def test_driven_solve_fires_the_other_way(self):
        """Both-directions fireability: a genuinely driven solve must come back
        nontrivial with a FINITE, small residual -- otherwise the guard above
        would be passing by always refusing."""
        kc = tt.known_case_chain(0.9)
        s = tt.solve_tone_vector(
            kc["a_nodes"], kc["conn"], kc["geom"]["theta"], chain_term(kc), 0, tol=1e-13
        )
        assert s.nontrivial is True
        assert s.homogeneous is False
        assert s.v_norm > 1.0
        assert s.residual_rel < 1e-11


# ═══════════════════════════════════════════════════════════════════════════
# KNOWN CASE — the frozen chain vs the ANALYTIC Fresnel step
# ═══════════════════════════════════════════════════════════════════════════
class TestKnownCaseChain:
    @pytest.mark.parametrize("A", [0.99, 0.9, 0.5])
    def test_exact_port_reading_is_the_analytic_fresnel_step(self, A):
        """The instrument's tightest known case: on the single-bond cut the
        bond's two directed incident phasors ARE the forward and backward
        amplitudes, so Gamma comes out with no fitted quantity in it. It must
        equal (sqrt(S)-1)/(sqrt(S)+1) at EVERY cold-side probe bond -- the
        agreement being probe-independent is what shows the phase referencing
        is right and not tuned at one plane."""
        kc = tt.known_case_chain(A)
        g = kc["geom"]
        sol = tt.solve_tone_vector(
            kc["a_nodes"], kc["conn"], g["theta"], chain_term(kc), 0, tol=1e-13
        )
        assert sol.residual_rel < 1e-12
        for x_probe in g["probe_bonds"]:
            r = tt.bond_gamma_vector(kc["net"], kc["bt"], sol.v, x_probe, g["theta"], g["x_I"])
            assert bool(r["excited"][0]) and not bool(r["excited"][1])
            assert complex(r["gamma"][0]).real == pytest.approx(kc["gamma_analytic"], abs=1e-12)
            assert abs(complex(r["gamma"][0]).imag) < 1e-12

    def test_cold_control_is_bit_exact_zero(self):
        """A = 0 CONTROL. |Gamma| == 0.0 EXACTLY -- the backward phasor is
        identically zero because nothing scatters backward on a uniform chain.

        GUARD (b), stated so it cannot be quoted wrong: this is a
        UNIFORM-BROADCAST null. It is guaranteed by the per-node cancellation
        identity (a common Y factors out of 2 Y_j / sum Y_k), so it demonstrates
        only that the measurement chain adds no echo of its own. It is an
        INSTRUMENT CONTROL and is NOT evidence about any wall."""
        kc = tt.known_case_chain(0.0)
        g = kc["geom"]
        sol = tt.solve_tone_vector(
            kc["a_nodes"], kc["conn"], g["theta"], chain_term(kc), 0, tol=1e-13
        )
        for x_probe in g["probe_bonds"]:
            r = tt.bond_gamma_vector(kc["net"], kc["bt"], sol.v, x_probe, g["theta"], g["x_I"])
            assert complex(r["v_bwd"][0]) == 0j          # identically, not approximately
            assert abs(complex(r["gamma"][0])) == 0.0    # bit-exact

    def test_electric_load_is_the_reciprocal_branch(self):
        """The canon-held OPEN reciprocal branch (Y = Y0 sqrt(S), Z -> inf) must
        come out at +|Gamma| through the SAME chain -- the sign is carried by
        the declared load, never by the instrument. Also pins that |t| > 1 here
        is the ordinary VOLTAGE transmission into a higher-impedance medium and
        not gain: the Y-weighted power ledger is what conserves."""
        kc_m = tt.known_case_chain(0.99, "magnetic")
        kc_e = tt.known_case_chain(0.99, "electric")
        assert kc_e["gamma_analytic"] == pytest.approx(-kc_m["gamma_analytic"], rel=1e-14)
        g = kc_e["geom"]
        sol = tt.solve_tone_vector(
            kc_e["a_nodes"], kc_e["conn"], g["theta"], chain_term(kc_e), 0, tol=1e-13
        )
        r = tt.bond_gamma_vector(kc_e["net"], kc_e["bt"], sol.v, 14.5, g["theta"], g["x_I"])
        assert complex(r["gamma"][0]).real == pytest.approx(kc_e["gamma_analytic"], abs=1e-12)

    def test_energy_is_conserved_on_the_solved_chain_field(self):
        kc = tt.known_case_chain(0.99)
        sol = tt.solve_tone_vector(
            kc["a_nodes"], kc["conn"], kc["geom"]["theta"], chain_term(kc), 0, tol=1e-13
        )
        v = sol.v.copy()
        E0 = tt.energy_Y_phasor(v, kc["Y_port"])
        drift = 0.0
        for _ in range(200):
            v = tt.apply_M_vector(kc["a_nodes"], kc["conn"], v)
            drift = max(drift, abs(tt.energy_Y_phasor(v, kc["Y_port"]) - E0) / E0)
        assert drift < 1e-12, drift


class TestKnownCaseDeEmbedding:
    @staticmethod
    def _deembed(kc, pol=(1.0, 0.0), loads=(0.0 + 0j, 0.3 + 0.1j, -0.2 + 0.25j, 0.15 - 0.3j),
                 **kw):
        g = kc["geom"]
        th = g["theta"]
        runs = []
        for d_load in loads:
            sol = tt.solve_tone_vector(
                kc["a_nodes"], kc["conn"], th, chain_term(kc, pol, d_load), 0, tol=1e-13
            )
            xf, Vf = tt.plane_binned_voltage_vector(kc["net"], kc["a_nodes"], sol.v, *g["feed_fit"])
            fit_f = tt.fit_k_vector(xf, Vf, 0.6 * th, 1.4 * th)
            k = fit_f["k"]
            xs, Vs = tt.plane_binned_voltage_vector(kc["net"], kc["a_nodes"], sol.v, *g["slab_fit"])
            fit_s = tt.fit_two_waves_vector(xs, Vs, k)
            ref = g["x_I"] * kc["net"].a_cell
            runs.append({
                "a": fit_f["a"] * np.exp(-1j * k * ref), "b": fit_f["b"] * np.exp(+1j * k * ref),
                "c": fit_s["a"] * np.exp(-1j * k * ref), "d": fit_s["b"] * np.exp(+1j * k * ref),
            })
        return tt.interface_two_port_vector(runs, **kw), runs

    def test_fitted_k_is_the_posited_tone(self):
        """On this carrier one bond = one step, so the grading changes
        impedance and NOT delay: the measured k must equal theta on the cold
        side. Pinned because every de-embedded phase reference depends on it."""
        kc = tt.known_case_chain(0.99)
        g = kc["geom"]
        sol = tt.solve_tone_vector(
            kc["a_nodes"], kc["conn"], g["theta"], chain_term(kc), 0, tol=1e-13
        )
        x, V = tt.plane_binned_voltage_vector(kc["net"], kc["a_nodes"], sol.v, *g["feed_fit"])
        fit = tt.fit_k_vector(x, V, 0.6 * g["theta"], 1.4 * g["theta"])
        assert fit["k"] == pytest.approx(g["theta"], abs=1e-7)
        assert fit["resid_rel"] < 1e-7

    @pytest.mark.parametrize("A", [0.99, 0.9])
    def test_deembedded_gamma_reproduces_the_analytic_step(self, A):
        kc = tt.known_case_chain(A)
        out, _runs = self._deembed(kc)
        g_signed, _phase = tt.signed_gamma(out["gamma"])
        assert out["resid_rel"] < 1e-6
        assert g_signed < 0.0
        assert g_signed == pytest.approx(kc["gamma_analytic"], abs=1e-6)

    def test_cold_deembedding_control(self):
        """A = 0 through the identical de-embedding chain (a UNIFORM-BROADCAST
        null -- guard (b); an instrument control, not evidence). |Gamma| is not
        bit-zero here because a least-squares fit sits between the field and
        the number; that gap between 0.0 and ~1e-9 IS the fit chain's own
        noise floor, and it is what the tolerance above is set against."""
        kc = tt.known_case_chain(0.0)
        out, _runs = self._deembed(kc)
        assert abs(out["gamma"]) < 1e-6
        assert abs(out["t"] - 1.0) < 1e-6

    def test_isotropy_is_measured_not_assumed(self):
        """A launch polarized at 0.6 rad excites BOTH components; de-embedding
        them separately must give the same Gamma. This tests the S (x) I_2
        model rather than assuming it -- and it is the gate that would fire if
        a per-component loading or a per-component k ever leaked in."""
        kc = tt.known_case_chain(0.99)
        pol = (float(np.cos(0.6)), float(np.sin(0.6)))
        out, _runs = self._deembed(kc, pol=pol, per_component=True)
        assert out["per_component"][0] is not None
        assert out["per_component"][1] is not None
        assert out["anisotropy"] < 1e-12
        for c in (0, 1):
            assert out["per_component"][c]["gamma"].real == pytest.approx(
                kc["gamma_analytic"], abs=1e-6
            )

    def test_stacked_default_uses_only_rows_with_content(self):
        """A linearly polarized launch leaves component 1 identically zero; its
        rows carry no information and must be DROPPED rather than counted (an
        all-zero row constrains nothing but would inflate n_rows)."""
        kc = tt.known_case_chain(0.9)
        out, runs = self._deembed(kc)
        assert out["n_runs"] == len(runs)
        assert out["n_rows"] == len(runs)  # one excited component per run, not two


# ═══════════════════════════════════════════════════════════════════════════
# END-TO-END PARITY on the srs carrier (the chain the discriminator will use)
# ═══════════════════════════════════════════════════════════════════════════
def _srs_deembed(module, L, x_I, x_B, A, theta, load_planes, feed, margin, vector: bool):
    net = build_srs_net(L=L)
    bt = hb.build_bond_table(net)
    conn = net.connect_index()
    x0, x1 = bt.b_x0, bt.b_x0 + bt.b_dx
    lo, hi = np.minimum(x0, x1), np.maximum(x0, x1)
    Ab = np.zeros(bt.n_bonds)
    Ab[(lo > x_I) & (hi < x_B)] = A
    k0 = theta / ANALYTIC_NETWORK_FACTOR
    ref = x_I * net.a_cell
    runs = []
    if vector:
        a, _ = tt.graded_coeffs(bt, Ab, "magnetic")
    else:
        a, _ = hb.scatter_weights(bt, hb.bond_admittance(Ab))
    for x_abs in load_planes:
        if vector:
            term = tt.plane_termination(
                net, bt, conn,
                [(0.5, np.array([[1.0 + 0j, 0j]]), np.zeros((1, 2), dtype=np.complex128)),
                 (x_abs, None, np.zeros((1, 2), dtype=np.complex128))], 1,
            )
            sol = tt.solve_tone_vector(a, conn, theta, term, 0, warmstart=600)
            xf, Vf = tt.plane_binned_voltage_vector(net, a, sol.v, *feed)
            fit_f = tt.fit_k_vector(xf, Vf, 0.6 * k0, 1.4 * k0)
            k = fit_f["k"]
            xs, Vs = tt.plane_binned_voltage_vector(net, a, sol.v, x_I + margin, x_abs - margin)
            fit_s = tt.fit_two_waves_vector(xs, Vs, k)
        else:
            f, b = hb.crossing_ports(net, bt, 0.5)
            _f2, b2 = hb.crossing_ports(net, bt, x_abs)
            term = hb.make_termination(
                net, bt, conn,
                [(f, np.array([1.0 + 0j])), (b, np.array([0j])), (b2, np.array([0j]))], 1,
            )
            sol = hb.solve_tone(a, conn, theta, term, 0, warmstart=600)
            xf, Vf = hb.plane_binned_voltage(net, a, sol.v, *feed)
            fit_f = hb.fit_k(xf, Vf, 0.6 * k0, 1.4 * k0)
            k = fit_f["k"]
            xs, Vs = hb.plane_binned_voltage(net, a, sol.v, x_I + margin, x_abs - margin)
            fit_s = hb.fit_two_waves(xs, Vs, k)
        runs.append({
            "a": fit_f["a"] * np.exp(-1j * k * ref), "b": fit_f["b"] * np.exp(+1j * k * ref),
            "c": fit_s["a"] * np.exp(-1j * k * ref), "d": fit_s["b"] * np.exp(+1j * k * ref),
        })
    return (tt.interface_two_port_vector(runs) if vector else hb.interface_two_port(runs))


class TestSrsEndToEndParity:
    def test_vector_and_scalar_chains_agree_on_the_srs_carrier(self):
        """The whole measurement chain -- solve, plane-bin, fit k, fit two
        waves, de-embed -- run through BOTH containers on the same srs L=6
        graded slab. The de-embedded Gammas must agree to solver precision.
        This is the test that makes the instrument substitutable for the
        scalar one in the lane that follows."""
        kw = dict(L=6, x_I=3.0, x_B=6.0, A=0.9, theta=0.15,
                  load_planes=(4.5, 5.0, 5.5), feed=(0.8, 2.8), margin=0.3)
        g_s, _ = hb.signed_gamma(_srs_deembed(hb, vector=False, **kw)["gamma"])
        g_v, _ = tt.signed_gamma(_srs_deembed(tt, vector=True, **kw)["gamma"])
        assert abs(g_v - g_s) < 1e-9, (g_v, g_s)
        # and both sit on the analytic core locus for this A
        S = float(np.sqrt(1.0 - 0.9 ** 2))
        z = np.sqrt(S)
        assert g_v == pytest.approx((z - 1.0) / (z + 1.0), abs=1e-3)


@pytest.mark.engine_sim
class TestBankedRegression:
    def test_vector_container_reproduces_the_banked_L24_gamma(self):
        """REGRESSION against the scalar validation driver's banked number
        (research/drivers/data/harmonic_balance_validation/receipts.json,
        "gamma_solver" = -0.45409225467790404) on its OWN measured geometry
        (L=24, x_I=9, x_B=15, theta=0.15, load planes 11.5/12.0/12.5, feed fit
        1.5-8.0, slab margin 0.5 -- all read off the driver's declared params).

        Slow (~30 s), so it is engine_sim-marked and routed out of the PR gate
        by cost, never by status. It is what turns "the port reproduces the
        scalar container" from an argument about einsum dtypes into a receipt
        at the number the other lane actually banked."""
        out = _srs_deembed(tt, L=24, x_I=9.0, x_B=15.0, A=0.99, theta=0.15,
                           load_planes=(11.5, 12.0, 12.5), feed=(1.5, 8.0),
                           margin=0.5, vector=True)
        g_v, _ = tt.signed_gamma(out["gamma"])
        # MEASURED |diff| on this branch: 2.819e-13. Tolerance set two decades
        # looser than that, to leave room for BLAS/platform drift in the LGMRES
        # path without letting a real regression through.
        assert g_v == pytest.approx(BANKED_L24_A099_SCALAR_GAMMA, abs=1e-11), g_v
        # and the analytic Fresnel step it is 1.7e-4 away from (the lattice
        # de-embed's own agreement with the continuum step -- an OTHER lane's
        # number, quoted, not re-derived here)
        S = float(np.sqrt(1.0 - 0.99 ** 2))
        z = np.sqrt(S)
        assert abs(g_v - (z - 1.0) / (z + 1.0)) == pytest.approx(1.7e-4, abs=0.2e-4)


# ═══════════════════════════════════════════════════════════════════════════
# FENCES — alpha-freedom and the input guards
# ═══════════════════════════════════════════════════════════════════════════
class TestFences:
    def test_no_constants_reference_anywhere_in_module_code(self):
        """GUARD (c). Walks the module's own AST and rejects any reference to
        the constants module or to a calibration symbol under ANY binding name,
        anywhere in the CODE. Docstrings are not AST Name/Attribute nodes, so
        the header's prose about being alpha-free does not self-trip this."""
        banned = {"ALPHA", "Q_TANK", "ELECTRON", "V_SNAP", "V_YIELD", "alpha", "constants"}
        tree = ast.parse(inspect.getsource(tt))
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

    def test_instrument_fence_is_stated_in_the_module_docstring(self):
        """The fence must travel with the module, not with a PR description."""
        doc = tt.__doc__ or ""
        assert "MINTS NO PHYSICS CLAIMS" in doc
        assert "adjudicates" in doc and "NO FORK" in doc
        for word in ("CHANNEL", "AXIS", "PHASE-STATE"):
            assert word in doc, f"sector header missing {word}"

    def test_load_string_guard_fires(self, srs4):
        _net, bt, _conn = srs4
        with pytest.raises(ValueError, match="sign-lock"):
            tt.port_admittance(bt, np.zeros(bt.n_bonds), "electirc")
        with pytest.raises(ValueError, match="per-bond"):
            tt.port_admittance(bt, np.zeros(bt.n_bonds + 1), "magnetic")

    def test_termination_shape_and_overlap_guards(self, srs4):
        net, bt, conn = srs4
        f, _b = hb.crossing_ports(net, bt, 0.5)
        with pytest.raises(ValueError, match="drive shape"):
            tt.make_vector_termination(net, bt, conn, [(f, np.zeros((1, 3)))], 1)
        with pytest.raises(ValueError, match="overlap"):
            tt.make_vector_termination(
                net, bt, conn, [(f, np.zeros((1, 2))), (f, np.zeros((1, 2)))], 1
            )
        with pytest.raises(ValueError, match="no boundary condition"):
            tt.plane_termination(net, bt, conn, [(0.5, None, None)], 1)

    def test_exact_port_reading_refuses_a_multi_bond_cut(self, srs4):
        """The 1-D scope fence must FIRE on a 3-D carrier rather than quietly
        return one bond's ratio as if it were a plane-wave reflection."""
        net, bt, _conn = srs4
        v = np.zeros((net.n_nodes, net.degree, 2), dtype=np.complex128)
        with pytest.raises(ValueError, match="SINGLE-bond"):
            tt.bond_gamma_vector(net, bt, v, 0.5, 0.2, 0.0)

    def test_de_embedding_needs_enough_information(self):
        run = {"a": np.array([1.0 + 0j, 0j]), "b": np.array([0.1 + 0j, 0j]),
               "c": np.array([0.9 + 0j, 0j]), "d": np.zeros(2, dtype=np.complex128)}
        with pytest.raises(ValueError, match=">= 2 load"):
            tt.interface_two_port_vector([run])
        dead = {k: np.zeros(2, dtype=np.complex128) for k in "abcd"}
        with pytest.raises(ValueError, match="underdetermined"):
            tt.interface_two_port_vector([dead, dead])

    def test_fit_rejects_a_scalar_container_array(self):
        x = np.linspace(0.0, 5.0, 6)
        with pytest.raises(ValueError, match=r"\(n_planes, 2\)"):
            tt.fit_two_waves_vector(x, np.ones(6, dtype=np.complex128), 0.3)
