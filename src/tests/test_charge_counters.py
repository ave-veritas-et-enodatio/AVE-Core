"""Analytic-field unit tests and gate-mutant tests for charge_counters.py.

Grid sizes:
  Dense 64³ (rc=8): integer-verdict C-exact (QSTARS), C-det4, C-link, dipole, hedgehog²
  Dense 96³ (rc=12): C-det4 convergence, hedgehog within ±0.005 of 1
  Alive BCC 96³ (rc=12): C-exact (5 qstars, bcc_bad=0), C-det-alive4, C-link

Known-answer source (proto JSON sha1s from setup sheet 920c213bd3b4):
  run_checks.json  sha1 b00b3a94eafa (dense 64/96)
  run_bcc.json     sha1 eb07ec231940 (BCC 64/96/128)
  cdet_alive4.json sha1 9440142f588f

Gate-mutant ladder §5 R0 trips documented inline and cross-referenced.

Seed conventions (setup sheet, MUST NOT change):
  QSTARS: random_regular_values(5, seed=20261008) — q0 ≤ 0
  NSTARS: random_n_vectors(4, seed=20261009) — n_z < -0.2
"""
import numpy as np
import pytest

import ave.topological.charge_counters as _CC
from ave.topological.charge_counters import (
    BCC_TETS,
    TETS,
    bcc_alive_mask,
    c_det,
    c_det4,
    c_det_alive4,
    c_exact,
    c_link,
    cold_control,
    dipole,
    embed_ktl,
    embed_spec,
    grid,
    hedgehog,
    hedgehog_sq,
    hopf_engine,
    projection_check,
    random_n_vectors,
    random_regular_values,
    rational,
)

# ── Canonical seed tables (setup sheet sha1 920c213bd3b4) ─────────────────────

QSTARS = random_regular_values(5, seed=20261008, max_q0=0.0)
NSTARS = random_n_vectors(4, seed=20261009, max_nz=-0.2)


# ── Module-scope grid fixtures (built once for all tests in the session) ──────


@pytest.fixture(scope="module")
def q_axial_64():
    return rational(64, rc=8)


@pytest.fixture(scope="module")
def q_axial_64_fields():
    """Returns (q, A0, A1) for projection_check gate."""
    return rational(64, rc=8, return_fields=True)


@pytest.fixture(scope="module")
def q_axial_96_fields():
    """Returns (q, A0, A1) for projection_check gate at 96³."""
    return rational(96, rc=12, return_fields=True)


@pytest.fixture(scope="module")
def q_hedgehog_64():
    return hedgehog(64, rc=8)


@pytest.fixture(scope="module")
def q_hedgehog_mirror_64():
    return hedgehog(64, rc=8, mirror=True)


@pytest.fixture(scope="module")
def q_hedgehog_mirror_96():
    return hedgehog(96, rc=12, mirror=True)


@pytest.fixture(scope="module")
def q_dipole_64():
    """Dipole seed: dipole(n, rc/2) per run_checks.py; rc=8 → rc/2=4."""
    return dipole(64, 4)


@pytest.fixture(scope="module")
def q_hedgehog_sq_64():
    return hedgehog_sq(64, rc=8)


@pytest.fixture(scope="module")
def q_axial_96():
    return rational(96, rc=12)


@pytest.fixture(scope="module")
def q_axial_mirror_64():
    return rational(64, rc=8, mirror=True)


@pytest.fixture(scope="module")
def q_hedgehog_96():
    return hedgehog(96, rc=12)


@pytest.fixture(scope="module")
def q_cold_64():
    return cold_control(64, rc=8)


@pytest.fixture(scope="module")
def alive_96():
    return bcc_alive_mask((96, 96, 96))


# ── Module-scope computed C-exact results ─────────────────────────────────────


@pytest.fixture(scope="module")
def res_exact_axial_64(q_axial_64):
    return c_exact(q_axial_64, QSTARS)


@pytest.fixture(scope="module")
def res_exact_hedgehog_64(q_hedgehog_64):
    return c_exact(q_hedgehog_64, QSTARS)


@pytest.fixture(scope="module")
def res_exact_hedgehog_mirror_64(q_hedgehog_mirror_64):
    return c_exact(q_hedgehog_mirror_64, QSTARS)


@pytest.fixture(scope="module")
def res_exact_hedgehog_mirror_96_bcc(q_hedgehog_mirror_96):
    return c_exact(q_hedgehog_mirror_96, QSTARS, tets=BCC_TETS, s=2)


@pytest.fixture(scope="module")
def res_exact_dipole_64(q_dipole_64):
    return c_exact(q_dipole_64, QSTARS)


@pytest.fixture(scope="module")
def res_exact_hedgehog_sq_64(q_hedgehog_sq_64):
    return c_exact(q_hedgehog_sq_64, QSTARS)


@pytest.fixture(scope="module")
def res_exact_axial_mirror_64(q_axial_mirror_64):
    return c_exact(q_axial_mirror_64, QSTARS)


@pytest.fixture(scope="module")
def res_exact_cold_64(q_cold_64):
    return c_exact(q_cold_64, QSTARS)


@pytest.fixture(scope="module")
def res_exact_axial_96_bcc(q_axial_96):
    return c_exact(q_axial_96, QSTARS, tets=BCC_TETS, s=2)


# ── Module-scope computed C-link results (dense 64³) ─────────────────────────


@pytest.fixture(scope="module")
def res_link_hedgehog_64(q_hedgehog_64):
    """C-link hedgehog +1 at 64³ dense. run_checks.json Lk≈1.000."""
    return c_link(hopf_engine(q_hedgehog_64), NSTARS)


@pytest.fixture(scope="module")
def res_link_hedgehog_mirror_64(q_hedgehog_mirror_64):
    """C-link hedgehog mirror −1 at 64³ dense."""
    return c_link(hopf_engine(q_hedgehog_mirror_64), NSTARS)


@pytest.fixture(scope="module")
def res_link_axial_mirror_64(q_axial_mirror_64):
    """C-link axial mirror −6 at 64³ dense. run_checks.json Lk≈−6.000."""
    return c_link(hopf_engine(q_axial_mirror_64), NSTARS)


@pytest.fixture(scope="module")
def res_link_dipole_64(q_dipole_64):
    """C-link dipole 0 at 64³ dense. run_checks.json Lk≈0."""
    return c_link(hopf_engine(q_dipole_64), NSTARS)


@pytest.fixture(scope="module")
def res_link_hedgehog_sq_64(q_hedgehog_sq_64):
    """C-link hedgehog² +2 at 64³ dense. run_checks.json Lk≈2.000."""
    return c_link(hopf_engine(q_hedgehog_sq_64), NSTARS)


@pytest.fixture(scope="module")
def res_link_cold_64(q_cold_64):
    """C-link cold control 0 at 64³ dense. spec A2.4; ladder #12."""
    return c_link(hopf_engine(q_cold_64), NSTARS)


@pytest.fixture(scope="module")
def res_link_axial_96_bcc(q_axial_96):
    n = hopf_engine(q_axial_96)
    return c_link(n, NSTARS, tets=BCC_TETS, s=2)


@pytest.fixture(scope="module")
def q_axial_mirror_96():
    return rational(96, rc=12, mirror=True)


@pytest.fixture(scope="module")
def q_cold_96():
    return cold_control(96, rc=12)


@pytest.fixture(scope="module")
def q_axial_96_deadzero(q_axial_96, alive_96):
    """Axial BCC 96³ with dead sites zeroed (engine-style storage)."""
    return q_axial_96 * alive_96[..., None]


@pytest.fixture(scope="module")
def res_link_axial_64(q_axial_64):
    """C-link axial +6 at 64³ dense."""
    return c_link(hopf_engine(q_axial_64), NSTARS)


@pytest.fixture(scope="module")
def res_exact_hedgehog_96_bcc(q_hedgehog_96):
    return c_exact(q_hedgehog_96, QSTARS, tets=BCC_TETS, s=2)


@pytest.fixture(scope="module")
def res_link_hedgehog_96_bcc(q_hedgehog_96):
    return c_link(hopf_engine(q_hedgehog_96), NSTARS, tets=BCC_TETS, s=2)


@pytest.fixture(scope="module")
def res_exact_axial_mirror_96_bcc(q_axial_mirror_96):
    return c_exact(q_axial_mirror_96, QSTARS, tets=BCC_TETS, s=2)


@pytest.fixture(scope="module")
def res_link_axial_mirror_96_bcc(q_axial_mirror_96):
    return c_link(hopf_engine(q_axial_mirror_96), NSTARS, tets=BCC_TETS, s=2)


@pytest.fixture(scope="module")
def res_exact_cold_96_bcc(q_cold_96):
    return c_exact(q_cold_96, QSTARS, tets=BCC_TETS, s=2)


@pytest.fixture(scope="module")
def res_link_cold_96_bcc(q_cold_96):
    return c_link(hopf_engine(q_cold_96), NSTARS, tets=BCC_TETS, s=2)


@pytest.fixture(scope="module")
def res_link_hedgehog_mirror_96_bcc(q_hedgehog_mirror_96):
    return c_link(hopf_engine(q_hedgehog_mirror_96), NSTARS, tets=BCC_TETS, s=2)


@pytest.fixture(scope="module")
def res_exact_bcc96_deadzero(q_axial_96_deadzero):
    """C-exact on axial BCC 96³ with dead sites zeroed (engine-style). Must resolve to +6."""
    return c_exact(q_axial_96_deadzero, QSTARS, tets=BCC_TETS, s=2)


# ── Dense 64³ (rc=8) integer-verdict tests ────────────────────────────────────


class TestDense64CExact:
    """C-exact integer verdict on dense 64³ grid.

    Implements: spec A3.3 #1, #3; ladder v3 §5 R0.
    Known answers from run_checks.json sha1 b00b3a94eafa.
    """

    def test_axial_resolved(self, res_exact_axial_64):
        """Ladder v3 §5 R0 #1: axial 64³ resolves to integer."""
        assert res_exact_axial_64['resolved'], (
            f"axial 64³ UNRESOLVED: {res_exact_axial_64['reason']}"
        )

    def test_axial_value(self, res_exact_axial_64):
        """Ladder v3 §5 R0 #1: axial C-exact = +6."""
        assert res_exact_axial_64['value'] == 6

    def test_axial_all_qstars_agree(self, res_exact_axial_64):
        pq = res_exact_axial_64['per_qstar']
        assert all(v == 6 for v in pq), f"per_qstar disagreement: {pq}"

    def test_axial_no_bad_tets(self, res_exact_axial_64):
        assert res_exact_axial_64['n_bad'] == 0

    def test_hedgehog_resolved(self, res_exact_hedgehog_64):
        assert res_exact_hedgehog_64['resolved'], (
            f"hedgehog 64³ UNRESOLVED: {res_exact_hedgehog_64['reason']}"
        )

    def test_hedgehog_value(self, res_exact_hedgehog_64):
        """Ladder v3 §5 R0 #3; spec A3.3 #1: hedgehog C-exact = +1."""
        assert res_exact_hedgehog_64['value'] == 1

    def test_hedgehog_no_bad_tets(self, res_exact_hedgehog_64):
        assert res_exact_hedgehog_64['n_bad'] == 0

    def test_dipole_resolved(self, res_exact_dipole_64):
        assert res_exact_dipole_64['resolved'], (
            f"dipole 64³ UNRESOLVED: {res_exact_dipole_64['reason']}"
        )

    def test_dipole_value_zero(self, res_exact_dipole_64):
        """Spec A3.3 #3: dipole C-exact = 0."""
        assert res_exact_dipole_64['value'] == 0

    def test_dipole_has_two_preimage_hits_per_qstar(self, res_exact_dipole_64):
        """Dipole has exactly 2 preimage points; each qstar sees both."""
        assert all(h == 2 for h in res_exact_dipole_64['n_hits']), (
            f"expected 2 hits per qstar, got {res_exact_dipole_64['n_hits']}"
        )

    def test_hedgehog_sq_resolved(self, res_exact_hedgehog_sq_64):
        assert res_exact_hedgehog_sq_64['resolved'], (
            f"hedgehog² 64³ UNRESOLVED: {res_exact_hedgehog_sq_64['reason']}"
        )

    def test_hedgehog_sq_value(self, res_exact_hedgehog_sq_64):
        """Ladder v3 §5 R0 #3: hedgehog² C-exact = 2."""
        assert res_exact_hedgehog_sq_64['value'] == 2


# ── Hedgehog mirror −1 ────────────────────────────────────────────────────────


class TestHedgehogMirror:
    """Mirror hedgehog (Y-negated) carries degree −1.

    Implements: ladder v3 §5 R0 #3; spec A3.3 #1 mirror case.
    Proto: run_checks.json axial23_ktl_mirror pattern; mirror hedgehog = -1 by symmetry.
    """

    def test_hedgehog_mirror_resolved_64(self, res_exact_hedgehog_mirror_64):
        """Dense 64³: hedgehog mirror resolves."""
        assert res_exact_hedgehog_mirror_64['resolved'], (
            f"hedgehog-mirror 64³ UNRESOLVED: {res_exact_hedgehog_mirror_64['reason']}"
        )

    def test_hedgehog_mirror_value_minus_one_64(self, res_exact_hedgehog_mirror_64):
        """Dense 64³: hedgehog mirror C-exact = −1."""
        assert res_exact_hedgehog_mirror_64['value'] == -1

    def test_hedgehog_mirror_no_bad_tets_64(self, res_exact_hedgehog_mirror_64):
        assert res_exact_hedgehog_mirror_64['n_bad'] == 0

    def test_hedgehog_mirror_cdet4_near_minus_one(self, q_hedgehog_mirror_64):
        """Dense 64³: hedgehog mirror C-det4 ≈ −1. Ladder v3 §5 R0 #1."""
        val = c_det4(q_hedgehog_mirror_64)
        assert abs(val - (-1.0)) < 0.05, (
            f"hedgehog-mirror 64³ c_det4 = {val:.4f}, expected ≈−1"
        )

    def test_hedgehog_mirror_link_minus_one_64(self, res_link_hedgehog_mirror_64):
        """Dense 64³: hedgehog mirror C-link = −1. Ladder v3 §5 R0 #3."""
        res = res_link_hedgehog_mirror_64
        assert res['resolved'], f"hedgehog-mirror link UNRESOLVED: {res['reason']}"
        assert res['value'] == -1
        for lk in res['pair_lk']:
            assert abs(lk - (-1)) < 1e-6, f"|Lk-round| = {abs(lk+1):.2e} ≥ 1e-6"

    def test_hedgehog_mirror_bcc_resolved_96(self, res_exact_hedgehog_mirror_96_bcc):
        """BCC 96³: hedgehog mirror resolves with bcc_bad=0."""
        assert res_exact_hedgehog_mirror_96_bcc['resolved'], (
            f"hedgehog-mirror BCC 96³ UNRESOLVED: "
            f"{res_exact_hedgehog_mirror_96_bcc['reason']}"
        )

    def test_hedgehog_mirror_bcc_value_minus_one_96(self, res_exact_hedgehog_mirror_96_bcc):
        """BCC 96³: hedgehog mirror C-exact = −1."""
        assert res_exact_hedgehog_mirror_96_bcc['value'] == -1

    def test_hedgehog_mirror_bcc_no_bad_tets_96(self, res_exact_hedgehog_mirror_96_bcc):
        assert res_exact_hedgehog_mirror_96_bcc['n_bad'] == 0


# ── Dense 64³ C-link for all known-answer seeds ───────────────────────────────


class TestDense64CLink:
    """C-link integer verdict for all five seeds at 64³ dense.

    Implements: ladder v3 §5 R0 #3; spec A3.3 #3.
    Both Lk pairs must agree, |Lk − round| < 1e-6, open = broken = 0.
    Known answers from run_checks.json sha1 b00b3a94eafa.
    """

    def _check_link(self, res, expected, label):
        assert res['resolved'], f"{label} C-link UNRESOLVED: {res['reason']}"
        assert res['value'] == expected, (
            f"{label} C-link value = {res['value']}, expected {expected}"
        )
        assert res['n_open'] == 0, f"{label} n_open = {res['n_open']}"
        assert res['n_broken'] == 0, f"{label} n_broken = {res['n_broken']}"
        for lk in res['pair_lk']:
            assert abs(lk - expected) < 1e-6, (
                f"{label} |Lk-round| = {abs(lk - expected):.2e} ≥ 1e-6"
            )

    def test_hedgehog_link_plus_one(self, res_link_hedgehog_64):
        """Hedgehog +1: C-link = +1. run_checks.json Lk≈1.000."""
        self._check_link(res_link_hedgehog_64, 1, "hedgehog")

    def test_hedgehog_mirror_link_minus_one(self, res_link_hedgehog_mirror_64):
        """Hedgehog mirror −1: C-link = −1."""
        self._check_link(res_link_hedgehog_mirror_64, -1, "hedgehog-mirror")

    def test_axial_mirror_link_minus_six(self, res_link_axial_mirror_64):
        """Axial mirror −6: C-link = −6. run_checks.json axial_mirror Lk≈−6.000."""
        self._check_link(res_link_axial_mirror_64, -6, "axial-mirror")

    def test_dipole_link_zero(self, res_link_dipole_64):
        """Dipole 0: C-link = 0. run_checks.json Lk≈0. Spec A3.3 #3."""
        self._check_link(res_link_dipole_64, 0, "dipole")

    def test_axial_link_plus_six(self, res_link_axial_64):
        """Axial +6: C-link = +6. run_checks.json Lk≈6.000."""
        self._check_link(res_link_axial_64, 6, "axial")

    def test_hedgehog_sq_link_two(self, res_link_hedgehog_sq_64):
        """Hedgehog² +2: C-link = +2. run_checks.json Lk≈2.000."""
        self._check_link(res_link_hedgehog_sq_64, 2, "hedgehog²")


# ── C0-cold degree-0 control ──────────────────────────────────────────────────


class TestColdControl:
    """C0-cold seed (spec A2.4): f = 0.04·4s²/(1+s²)², s=r/rc.

    Implements: spec A2.4; ladder v3 §5 R0, #12.
    Proto measured C-det4 = −1.5e-10 at this size.
    """

    def test_cdet4_near_zero(self, q_cold_64):
        """|C-det4| ≤ 0.01. Ladder #12 spec; proto measured −1.5e-10."""
        val = c_det4(q_cold_64)
        assert abs(val) < 0.01, (
            f"cold_control 64³ c_det4 = {val:.4e}, expected |val| < 0.01"
        )

    def test_cexact_zero(self, res_exact_cold_64):
        """C-exact = 0. Spec A2.4; ladder #12."""
        assert res_exact_cold_64['resolved'], (
            f"cold_control C-exact UNRESOLVED: {res_exact_cold_64['reason']}"
        )
        assert res_exact_cold_64['value'] == 0, (
            f"cold_control C-exact = {res_exact_cold_64['value']}, expected 0"
        )

    def test_clink_zero(self, res_link_cold_64):
        """C-link = 0, resolved. Spec A2.4; ladder #12."""
        assert res_link_cold_64['resolved'], (
            f"cold_control C-link UNRESOLVED: {res_link_cold_64['reason']}"
        )
        assert res_link_cold_64['value'] == 0, (
            f"cold_control C-link = {res_link_cold_64['value']}, expected 0"
        )


# ── Dense 64³ C-det4 (drift monitor) ─────────────────────────────────────────


class TestDense64CDet4:
    """4th-order C-det on dense 64³. Proto known answers (run_checks.json).

    Implements: spec A3.2; ladder v3 §5 R0 #1.
    """

    def test_axial_cdet4_near_six(self, q_axial_64):
        """C-det4 axial 64³ ≈ 5.91. Ladder v3 §5 R0 #1."""
        val = c_det4(q_axial_64)
        assert abs(val - 6.0) < 0.2, f"axial 64³ c_det4 = {val:.4f}, expected ≈5.91"

    def test_axial_cdet4_proto_value(self, q_axial_64):
        """Within 1% of proto value 5.9129 (run_bcc.json C_det_4th_dense)."""
        val = c_det4(q_axial_64)
        assert abs(val - 5.9129) < 0.1, f"axial 64³ c_det4 = {val:.4f}"

    def test_hedgehog_cdet4_near_one(self, q_hedgehog_64):
        val = c_det4(q_hedgehog_64)
        assert abs(val - 1.0) < 0.05, f"hedgehog 64³ c_det4 = {val:.4f}, expected ≈0.9996"

    def test_hedgehog_cdet4_proto_value(self, q_hedgehog_64):
        val = c_det4(q_hedgehog_64)
        assert abs(val - 0.9996) < 0.005, f"hedgehog 64³ c_det4 = {val:.4f}"


# ── Dense 96³ C-det4 (higher-resolution convergence) ─────────────────────────


class TestDense96CDet4:
    """4th-order C-det on dense 96³. Proto known answers (run_bcc.json).

    Implements: spec A3.2; ladder v3 §5 R0 #1; tolerance 5.98±0.02.
    """

    def test_axial_cdet4_proto_value(self, q_axial_96):
        """axial 96³ C-det4 = 5.9801 ± 0.02 (ladder v3 §5 R0 #1; run_bcc.json)."""
        val = c_det4(q_axial_96)
        assert abs(val - 5.9801) < 0.02, f"axial 96³ c_det4 = {val:.4f}"

    def test_hedgehog_cdet4_within_005_of_one(self, q_hedgehog_96):
        """Hedgehog 96³ C-det4 within 0.005 of 1. Ladder v3 §5 R0 #1."""
        val = c_det4(q_hedgehog_96)
        assert abs(val - 1.0) < 0.005, f"hedgehog 96³ c_det4 = {val:.4f}"

    def test_hedgehog_cdet4_proto_value(self, q_hedgehog_96):
        val = c_det4(q_hedgehog_96)
        # Proto: 0.9999
        assert abs(val - 0.9999) < 0.005, f"hedgehog 96³ c_det4 = {val:.4f}"


# ── C-det4 error convergence (ladder v3 §5 R0 #1, spec A3.2) ─────────────────


class TestCDet4Convergence:
    """Error |C-det4 − 6| falls monotonically 64 → 96, fitted order ≥ 0.8.

    Implements: ladder v3 §5 R0 #1 (convergence claim); spec A3.2.
    Proto (run_bcc.json C_det_4th_dense): 64³=5.9129, 96³=5.9801, 128³=5.9933.
    Errors: 0.0871, 0.0199, 0.0067. Fitted order ≈3.6 (4th-order diff, BCs clean).
    """

    def test_error_decreases_64_to_96(self, q_axial_64, q_axial_96):
        """Error |C-det4−6| strictly decreases from 64³ to 96³."""
        e64 = abs(c_det4(q_axial_64) - 6.0)
        e96 = abs(c_det4(q_axial_96) - 6.0)
        assert e96 < e64, (
            f"|err 96³|={e96:.4f} not < |err 64³|={e64:.4f}"
        )

    def test_convergence_order_ge_08(self, q_axial_64, q_axial_96):
        """Fitted convergence order ≥ 0.8 over 64→96. Proto order ≈3.6."""
        e64 = abs(c_det4(q_axial_64) - 6.0)
        e96 = abs(c_det4(q_axial_96) - 6.0)
        order = np.log(e64 / e96) / np.log(96.0 / 64.0)
        assert order >= 0.8, (
            f"c_det4 convergence order {order:.2f} < 0.8 "
            f"(e64={e64:.4f}, e96={e96:.4f})"
        )


# ── BCC alive 96³ (rc=12) tests ───────────────────────────────────────────────


class TestBCC96CDet:
    """C-det-alive4 on BCC 96³. Proto known answers (cdet_alive4.json sha1 9440142f).

    Implements: spec A3.2; ladder v3 §5 R0; BCC/alive tolerance 5.88±0.03.
    """

    def test_axial_cdet_alive4_proto(self, q_axial_96, alive_96):
        """Axial BCC 96³ C-det-alive4 = 5.8776 ± 0.03. Ladder v3 §5 R0; cdet_alive4.json."""
        val = c_det_alive4(q_axial_96, alive_96)
        assert abs(val - 5.8776) < 0.03, f"axial BCC 96³ c_det_alive4 = {val:.4f}"

    def test_hedgehog_cdet_alive4_proto(self, q_hedgehog_96, alive_96):
        val = c_det_alive4(q_hedgehog_96, alive_96)
        # Proto: 0.9992
        assert abs(val - 0.9992) < 0.005, f"hedgehog BCC 96³ c_det_alive4 = {val:.4f}"


class TestBCC96CExact:
    """C-exact on BCC 96³ with stride s=2. bcc_bad must be 0.

    Implements: spec A3.3 #3; ladder v3 §5 R0 (R0 precondition for R2).
    """

    def test_axial_bcc_resolved(self, res_exact_axial_96_bcc):
        assert res_exact_axial_96_bcc['resolved'], (
            f"axial BCC 96³ UNRESOLVED: {res_exact_axial_96_bcc['reason']}"
        )

    def test_axial_bcc_value(self, res_exact_axial_96_bcc):
        assert res_exact_axial_96_bcc['value'] == 6

    def test_axial_bcc_all_qstars_agree(self, res_exact_axial_96_bcc):
        pq = res_exact_axial_96_bcc['per_qstar']
        assert all(v == 6 for v in pq), f"per_qstar disagreement: {pq}"

    def test_axial_bcc_no_bad_tets(self, res_exact_axial_96_bcc):
        assert res_exact_axial_96_bcc['n_bad'] == 0, (
            f"bcc_bad = {res_exact_axial_96_bcc['n_bad']} (expected 0 at 96³ rc=12)"
        )

    def test_hedgehog_bcc_resolved(self, res_exact_hedgehog_96_bcc):
        """BCC 96³ hedgehog +1 resolves. Coverage item from Gate §9."""
        assert res_exact_hedgehog_96_bcc['resolved'], (
            f"hedgehog BCC 96³ UNRESOLVED: {res_exact_hedgehog_96_bcc['reason']}"
        )

    def test_hedgehog_bcc_value(self, res_exact_hedgehog_96_bcc):
        """BCC 96³ hedgehog C-exact = +1."""
        assert res_exact_hedgehog_96_bcc['value'] == 1

    def test_axial_mirror_bcc_resolved(self, res_exact_axial_mirror_96_bcc):
        """BCC 96³ axial mirror −6 resolves. Coverage item from Gate §9."""
        assert res_exact_axial_mirror_96_bcc['resolved'], (
            f"axial-mirror BCC 96³ UNRESOLVED: {res_exact_axial_mirror_96_bcc['reason']}"
        )

    def test_axial_mirror_bcc_value(self, res_exact_axial_mirror_96_bcc):
        """BCC 96³ axial mirror C-exact = −6."""
        assert res_exact_axial_mirror_96_bcc['value'] == -6

    def test_cold_bcc_resolved(self, res_exact_cold_96_bcc):
        """BCC 96³ C0-cold 0 resolves. Coverage item from Gate §9."""
        assert res_exact_cold_96_bcc['resolved'], (
            f"C0-cold BCC 96³ UNRESOLVED: {res_exact_cold_96_bcc['reason']}"
        )

    def test_cold_bcc_value(self, res_exact_cold_96_bcc):
        """BCC 96³ C0-cold C-exact = 0."""
        assert res_exact_cold_96_bcc['value'] == 0

    def test_deadzero_bcc_resolved(self, res_exact_bcc96_deadzero):
        """Axial BCC 96³ with dead sites zeroed (engine-style) resolves to +6.
        PR-B depends on alive-only boundary check; Gate nan_probe bcc96_deadzero_exact."""
        assert res_exact_bcc96_deadzero['resolved'], (
            f"bcc96 dead-zeroed UNRESOLVED: {res_exact_bcc96_deadzero['reason']}"
        )

    def test_deadzero_bcc_value(self, res_exact_bcc96_deadzero):
        """Axial BCC 96³ dead-zeroed C-exact = +6."""
        assert res_exact_bcc96_deadzero['value'] == 6


class TestBCC96CLink:
    """C-link on BCC 96³ using NSTARS (seed=20261009). Linking number ≈ 6.

    Implements: spec A3.3 #3; ladder v3 §5 R0; run_bcc.json C_link_bcc≈5.9999.
    """

    def test_axial_bcc_link_resolved(self, res_link_axial_96_bcc):
        assert res_link_axial_96_bcc['resolved'], (
            f"axial BCC 96³ c_link UNRESOLVED: {res_link_axial_96_bcc['reason']}"
        )

    def test_axial_bcc_link_value(self, res_link_axial_96_bcc):
        assert res_link_axial_96_bcc['value'] == 6

    def test_axial_bcc_link_raw_near_six(self, res_link_axial_96_bcc):
        lk = res_link_axial_96_bcc['raw_lk']
        assert abs(lk - 6.0) < 0.02, f"raw_lk = {lk:.4f}, expected ≈6.0"

    def test_axial_bcc_link_no_open_broken(self, res_link_axial_96_bcc):
        assert res_link_axial_96_bcc['n_open'] == 0
        assert res_link_axial_96_bcc['n_broken'] == 0

    def test_hedgehog_bcc_link_resolved(self, res_link_hedgehog_96_bcc):
        """BCC 96³ hedgehog +1 C-link resolves. Coverage item from Gate §9."""
        assert res_link_hedgehog_96_bcc['resolved'], (
            f"hedgehog BCC 96³ C-link UNRESOLVED: {res_link_hedgehog_96_bcc['reason']}"
        )

    def test_hedgehog_bcc_link_value(self, res_link_hedgehog_96_bcc):
        """BCC 96³ hedgehog C-link = +1."""
        assert res_link_hedgehog_96_bcc['value'] == 1

    def test_axial_mirror_bcc_link_resolved(self, res_link_axial_mirror_96_bcc):
        """BCC 96³ axial mirror −6 C-link resolves. Coverage item from Gate §9."""
        assert res_link_axial_mirror_96_bcc['resolved'], (
            f"axial-mirror BCC 96³ C-link UNRESOLVED: {res_link_axial_mirror_96_bcc['reason']}"
        )

    def test_axial_mirror_bcc_link_value(self, res_link_axial_mirror_96_bcc):
        """BCC 96³ axial mirror C-link = −6."""
        assert res_link_axial_mirror_96_bcc['value'] == -6

    def test_cold_bcc_link_resolved(self, res_link_cold_96_bcc):
        """BCC 96³ C0-cold 0 C-link resolves. Coverage item from Gate §9."""
        assert res_link_cold_96_bcc['resolved'], (
            f"C0-cold BCC 96³ C-link UNRESOLVED: {res_link_cold_96_bcc['reason']}"
        )

    def test_cold_bcc_link_value(self, res_link_cold_96_bcc):
        """BCC 96³ C0-cold C-link = 0."""
        assert res_link_cold_96_bcc['value'] == 0

    def test_hedgehog_mirror_bcc_link_resolved(self, res_link_hedgehog_mirror_96_bcc):
        """BCC 96³ hedgehog-mirror −1 C-link resolves. Coverage item from Gate §9."""
        assert res_link_hedgehog_mirror_96_bcc['resolved'], (
            f"hedgehog-mirror BCC 96³ C-link UNRESOLVED: "
            f"{res_link_hedgehog_mirror_96_bcc['reason']}"
        )

    def test_hedgehog_mirror_bcc_link_value(self, res_link_hedgehog_mirror_96_bcc):
        """BCC 96³ hedgehog-mirror C-link = −1."""
        assert res_link_hedgehog_mirror_96_bcc['value'] == -1


# ── Under-resolution guard (ladder §5 R0; spec A3.3 #3) ──────────────────────


class TestUnderResolutionGuard:
    """BCC 64³ axial seed must return UNRESOLVED with n_bad > 0.

    Implements: ladder v3 §5 R0 under-resolution guard; spec A3.3 #3.
    Proto run_bcc.json bcc_bad=224 at 64^3 rc=8.
    Ladder note: '64³ BCC is not used for C-exact (224 bad tets)'.
    """

    def test_axial_bcc_64_unresolved(self):
        """Axial 64³ BCC returns UNRESOLVED due to bad tets."""
        q = rational(64, rc=8)
        res = c_exact(q, QSTARS, tets=BCC_TETS, s=2)
        assert not res['resolved'], (
            f"axial 64³ BCC should be UNRESOLVED (n_bad={res['n_bad']})"
        )
        assert res['n_bad'] > 0, f"expected n_bad > 0, got n_bad={res['n_bad']}"

    def test_axial_bcc_64_nbad_matches_proto(self):
        """n_bad = 224 pins against proto run_bcc.json (64^3 rc=8 bcc_bad: 224)."""
        q = rational(64, rc=8)
        res = c_exact(q, QSTARS, tets=BCC_TETS, s=2)
        assert res['n_bad'] == 224, (
            f"n_bad = {res['n_bad']}, expected 224 (proto run_bcc.json)"
        )


# ── Projection / KTL embedding checks (non-tautological, F1) ─────────────────


class TestProjectionCheck:
    """KTL cross-multiplied projection check (spec addendum 2026-10-08 22:00).

    The check max|(n_x+in_y)·A0_seed − (1+n_z)·A1_seed| ≤ 1e-12 is NOT
    algebraically trivial: it verifies the KTL embedding property
    σ(H_engine(q)) = A1/A0 by comparing the engine's n to the SEED fields
    A0, A1 (not recomputed from q).

    Gate evidence (xmult_box.py sha1 fa5b0c943c79):
      KTL embed: 1.26e-15/1.24e-15/1.40e-15/1.46e-15 at 48/64/96/128³
      Spec-literal embed: ≈2.00 at every grid
      Z0 flip (zsign=+1): ≈1e-15 (blind); C-exact = −6 catches it.

    Implements: spec A4.3 #3; ladder v3 §5 R0 #3 embedding-flip.
    """

    def test_axial_ktl_64_passes(self, q_axial_64_fields):
        """KTL axial 64³: projection residual ≤ 1e-12. Gate: 1.24e-15."""
        q, A0, A1 = q_axial_64_fields
        res = projection_check(q, A0, A1)
        assert res <= 1e-12, (
            f"axial 64³ KTL projection residual = {res:.3e} (expected ≤ 1e-12)"
        )

    def test_axial_ktl_96_passes(self, q_axial_96_fields):
        """KTL axial 96³: projection residual ≤ 1e-12. Gate: 1.40e-15."""
        q, A0, A1 = q_axial_96_fields
        res = projection_check(q, A0, A1)
        assert res <= 1e-12, (
            f"axial 96³ KTL projection residual = {res:.3e} (expected ≤ 1e-12)"
        )

    def test_spec_embed_fails_projection(self):
        """Spec-literal embed q=(Re A0,Im A0,Re A1,Im A1) trips projection check ≈2.00.

        Implements: ladder v3 §5 R0 #3 embedding-flip trip (gate 2.00).
        xmult_box.py sha1 fa5b0c943c79: MUT_spec_literal_embed gives ≈2.00.
        """
        _, A0, A1 = rational(32, rc=4, return_fields=True)
        q_spec = embed_spec(A0, A1)
        res = projection_check(q_spec, A0, A1)
        assert res > 1.0, (
            f"spec embed projection check = {res:.3e}, expected > 1 (≈2.00)"
        )

    def test_zsign_flip_passes_projection_blind(self):
        """zsign=+1 (Z0 sign flip) passes projection check ≈1e-15 — blind to flip.

        The projection check gates the EMBEDDING, not the seed orientation.
        KTL embedding preserves σ(H(q))=A1/A0 regardless of zsign.
        C-exact = −6 catches the sign flip (ladder v3 §5 R0 #3 Z0-flip).
        """
        q, A0, A1 = rational(64, rc=8, zsign=+1, return_fields=True)
        res = projection_check(q, A0, A1)
        # Blind to zsign: expect ≤ 1e-12 (same as zsign=-1)
        assert res <= 1e-12, (
            f"zsign=+1 projection = {res:.3e}; blind check expected ≤ 1e-12"
        )
        # Verify C-exact = −6 catches it (ladder §5 R0 #3)
        r = c_exact(q, QSTARS)
        assert r['resolved'] and r['value'] == -6, (
            f"zsign=+1 C-exact expected −6, got {r}"
        )


# ── Gate mutant tests (Ladder §5 R0) ─────────────────────────────────────────
#
# Each test pair: (correct function passes) AND (mutant version FAILS or trips).
# This confirms the gate is sensitive, not just that the code compiles.


class TestGateMutants:
    """Ladder §5 R0 mutant-trip tests. Gate evidence xmult_box.py fa5b0c943c79."""

    # ── m1: π² normalization (factor-2 error) — mutant-value demonstration ──────
    # These tests demonstrate the MUTANT VALUE (what a wrong formula would produce),
    # not a code-path deletion. The actual code-path protection is the known-answer
    # tests above (test_axial_cdet4_*), which the mutation harness shows DO catch the
    # mutant. Labels updated per Gate §10 item 8.

    def test_m1_correct_norm_passes(self, q_axial_64):
        """Mutant-value demonstration: correct 2π² normalization gives ≈5.91."""
        val = c_det4(q_axial_64)
        assert abs(val - 6.0) < 0.5, "baseline c_det4 failed"

    def test_m1_wrong_norm_trips(self, q_axial_64):
        """Mutant-value demonstration: π² instead of 2π² → result doubles (≈11.8).
        Ladder v3 §5 R0 #1. The known-answer tests catch the actual code mutant."""
        def d(a):
            q = q_axial_64
            return (
                -np.roll(q, -2, a) + 8 * np.roll(q, -1, a)
                - 8 * np.roll(q, 1, a) + np.roll(q, 2, a)
            ) / 12.0
        M = np.stack([d(0), d(1), d(2), q_axial_64], -1)
        bad_val = float(np.linalg.det(M).sum() / np.pi ** 2)  # π² not 2π²
        assert bad_val > 9.0, f"m1 mutant did not trip: got {bad_val:.3f} (expected >9)"

    # ── m2: wrong dV on alive (dx³ instead of 4dx³) — mutant-value demonstration

    def test_m2_correct_dv_passes(self, q_axial_96, alive_96):
        """Mutant-value demonstration: correct 4dx³ per alive site gives ≈5.88."""
        val = c_det_alive4(q_axial_96, alive_96)
        assert abs(val - 6.0) < 0.5, f"baseline c_det_alive4 failed: {val:.4f}"

    def test_m2_wrong_dv_trips(self, q_axial_96, alive_96):
        """Mutant-value demonstration: dV = h³ instead of 4h³ → ~¼ of correct (≈1.47).
        Ladder §5 R0 #1. The known-answer tests catch the actual code mutant."""
        q = q_axial_96
        dq = [np.zeros_like(q) for _ in range(3)]

        def R(k, p):
            return np.roll(q, (-k * p[0], -k * p[1], -k * p[2]), (0, 1, 2))

        TETRA_OFFSETS = ((1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1))
        for p in TETRA_OFFSETS:
            D = (8 * (R(1, p) - R(-1, p)) - (R(2, p) - R(-2, p))) / 12.0
            for j in range(3):
                dq[j] += p[j] * D / (4.0)
        M = np.stack([dq[0], dq[1], dq[2], q], -1)
        bad_val = float((np.linalg.det(M) * alive_96).sum() / (2 * np.pi ** 2))  # no 4×
        assert bad_val < 2.5, f"m2 mutant did not trip: got {bad_val:.3f} (expected <2.5)"

    # ── m3: wrong column order (q first, sign flip) — mutant-value demonstration

    def test_m3_correct_order_positive(self, q_hedgehog_64):
        """Mutant-value demonstration: det[∂xq,∂yq,∂zq,q] > 0 for hedgehog +1."""
        val = c_det4(q_hedgehog_64)
        assert val > 0, f"baseline c_det4 hedgehog not positive: {val:.4f}"

    def test_m3_q_first_trips(self, q_hedgehog_64):
        """Mutant-value demonstration: det[q,∂xq,∂yq,∂zq] changes sign → negative.
        Ladder §5 R0 #1. The known-answer tests catch the actual code mutant."""
        q = q_hedgehog_64

        def d(a):
            return (
                -np.roll(q, -2, a) + 8 * np.roll(q, -1, a)
                - 8 * np.roll(q, 1, a) + np.roll(q, 2, a)
            ) / 12.0
        M = np.stack([q, d(0), d(1), d(2)], -1)   # q first
        bad_val = float(np.linalg.det(M).sum() / (2 * np.pi ** 2))
        assert bad_val < 0, f"m3 mutant did not flip sign: got {bad_val:.4f}"

    # ── m4: unsigned preimage → dipole reads 2 instead of 0 ──────────────────

    def test_m4_signed_dipole_zero(self, res_exact_dipole_64):
        """Correct signed count: dipole value = 0. Ladder v3 §5 R0 #3."""
        assert res_exact_dipole_64['value'] == 0

    def test_m4_unsigned_would_give_two(self, q_dipole_64):
        """Unsigned count (drop sign on local degree) → 2 for dipole.

        We verify the mechanism by checking 2 hits per qstar; the signed sum = 0.
        Ladder v3 §5 R0 #3.
        """
        r = c_exact(q_dipole_64, QSTARS[:3])
        assert all(h == 2 for h in r['n_hits']), (
            f"expected 2 hits per qstar, got {r['n_hits']}"
        )
        assert r['value'] == 0, "signed degree must be 0 (two opposite-sign preimages)"

    # ── m5: degenerate nstars (n1 ≈ n2) → c_link UNRESOLVED ─────────────────

    def test_m5_degenerate_nstars_unresolved(self, q_axial_96):
        """Degenerate n1=n2 → NaN → UNRESOLVED. Ladder v3 §5 R0 #3."""
        n = hopf_engine(q_axial_96)
        # Replace pair 1: n1=n2 → degenerate
        bad_nstars = NSTARS.copy()
        bad_nstars[1] = bad_nstars[0]   # n1 = n2
        res = c_link(n, bad_nstars, tets=BCC_TETS, s=2)
        assert not res['resolved'], "m5: degenerate n1=n2 should be UNRESOLVED"
        assert res['reason'] is not None and 'DEGENERATE' in res['reason']

    # ── embedding_flip: embed_spec gives sign-flipped (mirror) degree ────────

    def test_embedding_flip_gives_negative_cdet4(self):
        """embed_spec is a mirror map: c_det4 < 0 (not +5.91).

        The real gate for embedding correctness is c_det4 sign; the cross-
        multiplied projection check (projection_check with A0/A1 from seed)
        also trips at ≈2.00 (xmult_box.py fa5b0c943c79).
        Ladder v3 §5 R0 #3.
        """
        q = rational(32, rc=4, embed=embed_spec)
        val = c_det4(q)
        assert val < 0, f"embed_spec c_det4 = {val:.4f}, expected negative (mirror)"

    def test_ktl_embed_gives_positive_cdet4(self):
        """KTL embedding gives positive c_det4 for axial seed. Ladder v3 §5 R0 #3."""
        q = rational(32, rc=4, embed=embed_ktl)
        val = c_det4(q)
        assert val > 0, f"embed_ktl c_det4 = {val:.4f}, expected positive"

    def test_projection_check_spec_embed_trips(self):
        """embed_spec trips projection_check ≈2.00 > 1.

        Gate evidence xmult_box.py sha1 fa5b0c943c79: MUT_spec_literal_embed≈2.00.
        Ladder v3 §5 R0 #3 embedding-flip.
        """
        _, A0, A1 = rational(32, rc=4, return_fields=True)
        q_spec = embed_spec(A0, A1)
        res = projection_check(q_spec, A0, A1)
        assert res > 1.0, f"embed_spec projection_check = {res:.3e}, expected > 1"

    # ── zsign flip: zsign=+1 gives -6 ────────────────────────────────────────

    def test_zsign_flip_gives_minus_six(self):
        """KTL §0: zsign=-1 is the correct sign. zsign=+1 (spec-literal) → C = −6.

        Projection check is blind (≈1e-15) but C-exact = −6 catches it.
        Ladder v3 §5 R0 #3 Z0-flip.
        """
        q_neg = rational(64, rc=8, zsign=-1)
        q_pos = rational(64, rc=8, zsign=+1)
        r_neg = c_exact(q_neg, QSTARS)
        r_pos = c_exact(q_pos, QSTARS)
        assert r_neg['resolved'] and r_neg['value'] == 6, (
            f"zsign=-1 should give +6, got {r_neg}"
        )
        assert r_pos['resolved'] and r_pos['value'] == -6, (
            f"zsign=+1 should give -6, got {r_pos}"
        )

    # ── cold_control: degree 0, |C-det4| < 0.01 ──────────────────────────────

    def test_cold_control_cdet4_near_zero(self):
        """|C-det4| < 0.01 for cold_control seed. Spec A2.4; ladder #12; proto −1.5e-10."""
        q = cold_control(64, rc=8)
        val = c_det4(q)
        assert abs(val) < 0.01, f"cold_control 64³ c_det4 = {val:.4e}, expected |val|<0.01"

    # ── mirror seed: degree −6 ────────────────────────────────────────────────

    def test_mirror_seed_c_exact_minus_six(self):
        """Mirror seed (Z1 → conj Z1) gives C = −6. Ladder v3 §5 R0 #3."""
        q = rational(64, rc=8, mirror=True)
        r = c_exact(q, QSTARS)
        assert r['resolved'] and r['value'] == -6, (
            f"mirror seed should give -6, got {r}"
        )


# ── QSTARS / NSTARS seed stability ───────────────────────────────────────────


class TestSeedStability:
    """Verify canonical seed tables match expected first-element values."""

    def test_qstars_q0_le_zero(self):
        assert (QSTARS[:, 0] <= 0).all(), "QSTARS must all have q0 ≤ 0"

    def test_qstars_unit_norm(self):
        norms = np.linalg.norm(QSTARS, axis=1)
        assert np.allclose(norms, 1.0, atol=1e-12), "QSTARS not unit quaternions"

    def test_qstars_count(self):
        assert len(QSTARS) == 5

    def test_nstars_nz_lt_thresh(self):
        assert (NSTARS[:, 2] < -0.2).all(), "NSTARS must all have n_z < -0.2"

    def test_nstars_unit_norm(self):
        norms = np.linalg.norm(NSTARS, axis=1)
        assert np.allclose(norms, 1.0, atol=1e-12), "NSTARS not unit 3-vectors"

    def test_nstars_count(self):
        assert len(NSTARS) == 4

    def test_qstars_first_row_pinned(self):
        """QSTARS[0] pinned to rng-20261008 exact values (Gate §10 item 6).
        Values computed from random_regular_values(5, seed=20261008, max_q0=0.0)."""
        expected = np.array([
            -3.896247510887675e-03,
            -5.089801526970469e-01,
            8.592503618283305e-01,
            -5.111593796173653e-02,
        ])
        assert np.allclose(QSTARS[0], expected, atol=1e-12), (
            f"QSTARS[0] changed from rng-20261008 seed: {QSTARS[0]}"
        )

    def test_nstars_first_row_pinned(self):
        """NSTARS[0] pinned to rng-20261009 exact values (Gate §10 item 6).
        Values computed from random_n_vectors(4, seed=20261009, max_nz=-0.2)."""
        expected = np.array([
            6.937011536471508e-01,
            -6.809262742185627e-01,
            -2.347724824323303e-01,
        ])
        assert np.allclose(NSTARS[0], expected, atol=1e-12), (
            f"NSTARS[0] changed from rng-20261009 seed: {NSTARS[0]}"
        )


# ── Input validation: NONFINITE / NONUNIT / K<3 / n3≈n4 / alive-boundary ──────


class TestInputValidation:
    """Non-finite / non-unit / K<3 / pair-2 degenerate / alive-boundary guards.

    Implements Gate §10 items 1, 2, 4, 5 (fix-pass-2).
    Each test requires the corresponding guard to be present; deleting the guard
    causes the field to silently resolve (or crash), failing the assertion.
    """

    def test_nan_core_r12_exact_unresolved(self):
        """NaN in core r<12 → c_exact UNRESOLVED NONFINITE. Gate nan_probe2.json."""
        q = rational(48, rc=6).copy()
        _, _, _, r = grid(48)
        q[r < 12] = np.nan
        res = c_exact(q, QSTARS)
        assert not res['resolved'], f"expected UNRESOLVED, got {res}"
        assert res['reason'] is not None and 'NONFINITE' in res['reason']

    def test_nan_core_r12_link_unresolved(self):
        """NaN in core r<12 → c_link UNRESOLVED NONFINITE. Gate nan_probe2.json."""
        q = rational(48, rc=6).copy()
        _, _, _, r = grid(48)
        q[r < 12] = np.nan
        n = hopf_engine(q)
        res = c_link(n, NSTARS)
        assert not res['resolved'], f"expected UNRESOLVED, got {res}"
        assert res['reason'] is not None and 'NONFINITE' in res['reason']

    def test_single_nan_exact_unresolved(self):
        """Single NaN site → c_exact UNRESOLVED NONFINITE. Gate nan_probe.json."""
        q = rational(48, rc=6).copy()
        q[20, 20, 20] = np.nan
        res = c_exact(q, QSTARS)
        assert not res['resolved'], f"single NaN site: expected UNRESOLVED, got {res}"
        assert res['reason'] is not None and 'NONFINITE' in res['reason']

    def test_nonunit_x10_exact_unresolved(self):
        """×10 core → c_exact UNRESOLVED NONUNIT. Gate nan_probe2.json."""
        q = rational(48, rc=6).copy()
        _, _, _, r = grid(48)
        q[r < 6] *= 10
        res = c_exact(q, QSTARS)
        assert not res['resolved'], f"×10 field: expected UNRESOLVED, got {res}"
        assert res['reason'] is not None and 'NONUNIT' in res['reason']

    def test_pair2_n3_eq_n4_unresolved(self):
        """n3 = n4 → c_link UNRESOLVED DEGENERATE (no ValueError). Gate nan_probe.json."""
        q = rational(48, rc=6)
        n = hopf_engine(q)
        bad_nstars = NSTARS.copy()
        bad_nstars[3] = bad_nstars[2]  # n3 = n4
        res = c_link(n, bad_nstars)
        assert not res['resolved'], f"n3=n4: expected UNRESOLVED, got {res}"
        assert res['reason'] is not None and 'DEGENERATE' in res['reason']

    def test_too_few_qstars_unresolved(self):
        """K = 2 < 3 → c_exact UNRESOLVED TOO_FEW_QSTARS. Gate §10 item 5."""
        q = rational(32, rc=4)
        res = c_exact(q, QSTARS[:2])
        assert not res['resolved'], f"K=2: expected UNRESOLVED, got {res}"
        assert res['reason'] is not None and 'TOO_FEW_QSTARS' in res['reason']

    def test_deadzero_bcc_exact_resolves(self, res_exact_bcc96_deadzero):
        """Axial BCC 96³ dead-zeroed resolves to +6 with alive-only boundary check.
        Gate §10 item 4: alive-only boundary; nan_probe.json bcc96_deadzero_exact."""
        assert res_exact_bcc96_deadzero['resolved'], (
            f"bcc96 dead-zeroed UNRESOLVED: {res_exact_bcc96_deadzero['reason']}"
        )
        assert res_exact_bcc96_deadzero['value'] == 6


# ── L1 positive controls for five UNRESOLVED branches ────────────────────────


class TestUnresolvedBranchControls:
    """L1 positive controls: each test FAILS when its UNRESOLVED branch is deleted.

    Implements Gate §10 item 3 (fix-pass-2). Constructed fields or monkeypatching
    of internal helpers per §10.3 suggestion. The corresponding mutants in the
    gate-rerun mutate.py are: no_qstar_disagreement, no_degen_tet,
    no_boundary_check, link_no_pair_disagree, link_open_ignored.
    """

    def test_qstar_disagreement_unresolved(self, monkeypatch):
        """q*-disagreement branch → UNRESOLVED. Monkeypatch injects N=1,2,3 per call."""
        call = [0]
        _orig = _CC._c_exact_qstar

        def _mock(q, qs, **kw):
            call[0] += 1
            r = _orig(q, qs, **kw)
            r['N'] = call[0]
            return r

        monkeypatch.setattr(_CC, '_c_exact_qstar', _mock)
        q = hedgehog(32, rc=4)
        res = c_exact(q, QSTARS[:3])
        assert not res['resolved'], f"q*-disagreement: expected UNRESOLVED, got {res}"
        assert res['reason'] is not None and 'QSTAR_DISAGREEMENT' in res['reason']

    def test_degenerate_tet_unresolved(self):
        """Degenerate-tet branch → UNRESOLVED. Constructive: qstar = exact tet-vertex value.
        q[0,0,0] of rational(16) is at corner (large r, near vacuum), unit-quaternion with
        q0>0 is fine for c_exact.  That value is v0 of every slab-0 Freudenthal tet, so
        _c_exact_qstar returns degenerate≥12.  The no_degen_tet mutant zeroes this, causing
        QSTAR_DISAGREEMENT (q[0,0,0] has zero preimages vs 1 for the regular q*'s)."""
        q = rational(16, rc=4)
        qstar = q[0, 0, 0].copy()
        qstars = np.vstack([qstar, QSTARS[:2]])
        res = c_exact(q, qstars)
        assert not res['resolved'], f"degen-tet: expected UNRESOLVED, got {res}"
        assert res['reason'] is not None and 'DEGENERATE' in res['reason'], res['reason']

    def test_boundary_check_unresolved(self):
        """Crafted dense field with unit q, q0 < 0.5 on face-centre boundary site →
        UNRESOLVED BOUNDARY. Uses hedgehog(64,rc=8) which has n_bad=0 so BOUNDARY
        is reached; single modified site doesn't affect preimage count."""
        q = hedgehog(64, rc=8).copy()
        # Valid unit quaternion with q0 = 0.3 placed at face-centre boundary
        q[0, 32, 32] = np.array([0.3, 0.0, 0.0, np.sqrt(1.0 - 0.09)])
        res = c_exact(q, QSTARS)
        assert not res['resolved'], f"boundary q0<0.5: expected UNRESOLVED, got {res}"
        assert res['reason'] is not None and 'BOUNDARY' in res['reason']

    def test_link_pair_disagreement_unresolved(self, monkeypatch):
        """Pair-disagreement branch → UNRESOLVED. Monkeypatch injects lk1=1, lk2=2."""
        call = [0]
        _orig = _CC._c_link_pair

        def _mock(n, ns1, ns2, h=1.0, tets=None, s=1):
            call[0] += 1
            lk, op, br, a, b = _orig(n, ns1, ns2, h=h, tets=tets, s=s)
            return (float(call[0]), op, br, a, b)

        monkeypatch.setattr(_CC, '_c_link_pair', _mock)
        q = hedgehog(32, rc=4)
        n = hopf_engine(q)
        res = c_link(n, NSTARS)
        assert not res['resolved'], f"pair-disagree: expected UNRESOLVED, got {res}"
        assert res['reason'] is not None and 'PAIR_DISAGREEMENT' in res['reason']

    def test_link_open_broken_unresolved(self, monkeypatch):
        """Open/broken-loops branch → UNRESOLVED. Monkeypatch injects open_tets=1."""
        _orig = _CC._c_link_pair

        def _mock(n, ns1, ns2, h=1.0, tets=None, s=1):
            lk, op, br, a, b = _orig(n, ns1, ns2, h=h, tets=tets, s=s)
            return (lk, 1, br, a, b)  # inject open_tets = 1

        monkeypatch.setattr(_CC, '_c_link_pair', _mock)
        q = hedgehog(32, rc=4)
        n = hopf_engine(q)
        res = c_link(n, NSTARS)
        assert not res['resolved'], f"open-loops: expected UNRESOLVED, got {res}"
        assert res['reason'] is not None and 'OPEN_OR_BROKEN' in res['reason']

    def test_nonfinite_lk_unresolved(self, monkeypatch):
        """NONFINITE_LK branch → UNRESOLVED. Monkeypatch injects NaN for lk1.
        Without the guard, round(NaN) raises ValueError — test errors on that mutant."""
        call = [0]
        _orig = _CC._c_link_pair

        def _mock(n, ns1, ns2, h=1.0, tets=None, s=1):
            call[0] += 1
            lk, op, br, a, b = _orig(n, ns1, ns2, h=h, tets=tets, s=s)
            if call[0] == 1:
                lk = float('nan')  # pair 1 lk is NaN
            return (lk, op, br, a, b)

        monkeypatch.setattr(_CC, '_c_link_pair', _mock)
        q = hedgehog(32, rc=4)
        n = hopf_engine(q)
        res = c_link(n, NSTARS)
        assert not res['resolved'], f"NONFINITE_LK: expected UNRESOLVED, got {res}"
        assert res['reason'] is not None and 'NONFINITE_LK' in res['reason']
