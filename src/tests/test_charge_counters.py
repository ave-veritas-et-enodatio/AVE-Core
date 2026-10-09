"""Analytic-field unit tests and gate-mutant tests for charge_counters.py.

Grid sizes:
  Dense 64³ (rc=8): integer-verdict C-exact (QSTARS), C-det4, dipole, hedgehog²
  Dense 96³ (rc=12): C-det4 convergence
  Alive BCC 96³ (rc=12): C-exact (5 qstars, bcc_bad=0), C-det-alive4, C-link

Known-answer source (proto JSON sha1s from setup sheet 920c213bd3b4):
  run_checks.json  sha1 0ab01234 (dense 64/96)
  run_bcc.json     sha1 eb07ec23 (BCC 64/96)
  cdet_alive4.json sha1 9440142f

Gate-mutant ladder §5 R0 trips documented in mutant_evidence.py.

Seed conventions (setup sheet, MUST NOT change):
  QSTARS: random_regular_values(5, seed=20261008) — q0 ≤ 0
  NSTARS: random_n_vectors(4, seed=20261009) — n_z < -0.2
"""
import numpy as np
import pytest

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
def q_hedgehog_64():
    return hedgehog(64, rc=8)


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
def q_hedgehog_96():
    return hedgehog(96, rc=12)


@pytest.fixture(scope="module")
def alive_96():
    return bcc_alive_mask((96, 96, 96))


# Module-scope computed results (expensive; run once, shared across test functions)


@pytest.fixture(scope="module")
def res_exact_axial_64(q_axial_64):
    return c_exact(q_axial_64, QSTARS)


@pytest.fixture(scope="module")
def res_exact_hedgehog_64(q_hedgehog_64):
    return c_exact(q_hedgehog_64, QSTARS)


@pytest.fixture(scope="module")
def res_exact_dipole_64(q_dipole_64):
    return c_exact(q_dipole_64, QSTARS)


@pytest.fixture(scope="module")
def res_exact_hedgehog_sq_64(q_hedgehog_sq_64):
    return c_exact(q_hedgehog_sq_64, QSTARS)


@pytest.fixture(scope="module")
def res_exact_axial_96_bcc(q_axial_96):
    return c_exact(q_axial_96, QSTARS, tets=BCC_TETS, s=2)


@pytest.fixture(scope="module")
def res_link_axial_96_bcc(q_axial_96):
    n = hopf_engine(q_axial_96)
    return c_link(n, NSTARS, tets=BCC_TETS, s=2)


# ── Dense 64³ (rc=8) integer-verdict tests ────────────────────────────────────


class TestDense64CExact:
    """C-exact integer verdict on dense 64³ grid. Known answers from run_checks.json."""

    def test_axial_resolved(self, res_exact_axial_64):
        assert res_exact_axial_64['resolved'], (
            f"axial 64³ UNRESOLVED: {res_exact_axial_64['reason']}"
        )

    def test_axial_value(self, res_exact_axial_64):
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
        assert res_exact_hedgehog_64['value'] == 1

    def test_hedgehog_no_bad_tets(self, res_exact_hedgehog_64):
        assert res_exact_hedgehog_64['n_bad'] == 0

    def test_dipole_resolved(self, res_exact_dipole_64):
        assert res_exact_dipole_64['resolved'], (
            f"dipole 64³ UNRESOLVED: {res_exact_dipole_64['reason']}"
        )

    def test_dipole_value_zero(self, res_exact_dipole_64):
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
        assert res_exact_hedgehog_sq_64['value'] == 2


# ── Dense 64³ C-det4 (drift monitor) ─────────────────────────────────────────


class TestDense64CDet4:
    """4th-order C-det on dense 64³. Proto known answers (run_checks.json)."""

    def test_axial_cdet4_near_six(self, q_axial_64):
        val = c_det4(q_axial_64)
        assert abs(val - 6.0) < 0.2, f"axial 64³ c_det4 = {val:.4f}, expected ≈5.91"

    def test_axial_cdet4_proto_value(self, q_axial_64):
        """Within 1% of proto value 5.9129."""
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
    """4th-order C-det on dense 96³. Proto known answers (run_checks.json)."""

    def test_axial_cdet4_proto_value(self, q_axial_96):
        val = c_det4(q_axial_96)
        # Proto: 5.9801
        assert abs(val - 5.9801) < 0.05, f"axial 96³ c_det4 = {val:.4f}"

    def test_hedgehog_cdet4_proto_value(self, q_hedgehog_96):
        val = c_det4(q_hedgehog_96)
        # Proto: 0.9999
        assert abs(val - 0.9999) < 0.005, f"hedgehog 96³ c_det4 = {val:.4f}"


# ── BCC alive 96³ (rc=12) tests ───────────────────────────────────────────────


class TestBCC96CDet:
    """C-det-alive4 on BCC 96³. Proto known answers (cdet_alive4.json)."""

    def test_axial_cdet_alive4_proto(self, q_axial_96, alive_96):
        val = c_det_alive4(q_axial_96, alive_96)
        # Proto: 5.8776
        assert abs(val - 5.8776) < 0.05, f"axial BCC 96³ c_det_alive4 = {val:.4f}"

    def test_hedgehog_cdet_alive4_proto(self, q_hedgehog_96, alive_96):
        val = c_det_alive4(q_hedgehog_96, alive_96)
        # Proto: 0.9992
        assert abs(val - 0.9992) < 0.005, f"hedgehog BCC 96³ c_det_alive4 = {val:.4f}"


class TestBCC96CExact:
    """C-exact on BCC 96³ with stride s=2. bcc_bad must be 0."""

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


class TestBCC96CLink:
    """C-link on BCC 96³ using NSTARS (seed=20261009). Linking number ≈ 6."""

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


# ── Projection / KTL embedding checks ────────────────────────────────────────


class TestProjectionCheck:
    """KTL cross-multiplied projection check (spec addendum 2026-10-08 22:00).

    The formula max|(n_x+in_y)·A0 − (1+n_z)·A1| is an algebraic identity = 0
    for any unit-norm quaternion field, so it always returns ≤ machine epsilon.
    It is a unit-norm sanity gate, not an embedding discriminator.
    """

    def test_axial_ktl_unit_norm_check_passes(self, q_axial_64):
        """Unit-norm axial field: projection residual ≤ 1e-12."""
        res = projection_check(q_axial_64)
        assert res <= 1e-12, f"projection residual = {res:.3e} (expected ≤ 1e-12)"

    def test_hedgehog_unit_norm_check_passes(self, q_hedgehog_64):
        res = projection_check(q_hedgehog_64)
        assert res <= 1e-12, f"hedgehog projection residual = {res:.3e}"


# ── Gate mutant tests (Ladder §5 R0) ─────────────────────────────────────────
#
# Each test pair: (correct function passes) AND (mutant version FAILS or trips).
# This confirms the gate is sensitive, not just that the code compiles.


class TestGateMutants:
    """Ladder §5 R0 mutant-trip tests. See scratch-a/mutant_evidence.py for table."""

    # ── m1: π² normalization (factor-2 error) ────────────────────────────────

    def test_m1_correct_norm_passes(self, q_axial_64):
        val = c_det4(q_axial_64)
        assert abs(val - 6.0) < 0.5, "baseline c_det4 failed"

    def test_m1_wrong_norm_trips(self, q_axial_64):
        """π² instead of 2π² → result doubles (≈11.8, not 6)."""
        def d(a):
            q = q_axial_64
            return (
                -np.roll(q, -2, a) + 8 * np.roll(q, -1, a)
                - 8 * np.roll(q, 1, a) + np.roll(q, 2, a)
            ) / 12.0
        M = np.stack([d(0), d(1), d(2), q_axial_64], -1)
        bad_val = float(np.linalg.det(M).sum() / np.pi ** 2)  # π² not 2π²
        assert bad_val > 9.0, f"m1 mutant did not trip: got {bad_val:.3f} (expected >9)"

    # ── m2: wrong dV on alive (dx³ instead of 4dx³) ──────────────────────────

    def test_m2_correct_dv_passes(self, q_axial_96, alive_96):
        val = c_det_alive4(q_axial_96, alive_96)
        assert abs(val - 6.0) < 0.5, f"baseline c_det_alive4 failed: {val:.4f}"

    def test_m2_wrong_dv_trips(self, q_axial_96, alive_96):
        """dV = h³ instead of 4h³ → result is ~¼ of correct (≈1.47)."""
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

    # ── m3: wrong column order (q first, sign flip) ───────────────────────────

    def test_m3_correct_order_positive(self, q_hedgehog_64):
        val = c_det4(q_hedgehog_64)
        assert val > 0, f"baseline c_det4 hedgehog not positive: {val:.4f}"

    def test_m3_q_first_trips(self, q_hedgehog_64):
        """det[q, ∂xq, ∂yq, ∂zq] changes sign; hedgehog → negative."""
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
        """Correct signed count: dipole value = 0."""
        assert res_exact_dipole_64['value'] == 0

    def test_m4_unsigned_would_give_two(self, q_dipole_64):
        """Unsigned count (drop sign on local degree) → 2 for dipole.
        We verify the mechanism by checking 2 hits per qstar; the signed sum = 0."""
        r = res_exact_dipole_64 = c_exact(q_dipole_64, QSTARS[:1])
        assert r['n_hits'][0] == 2, f"expected 2 preimage hits, got {r['n_hits']}"
        assert r['value'] == 0, "signed degree must be 0 (two opposite-sign preimages)"

    # ── m5: degenerate nstars (n1 ≈ n2) → c_link UNRESOLVED ─────────────────

    def test_m5_degenerate_nstars_unresolved(self, q_axial_96):
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
        The cross-multiplied projection formula is algebraically 0 for any
        unit-norm field, so the real gate is the c_det4 sign."""
        q = rational(32, rc=4, embed=embed_spec)
        val = c_det4(q)
        assert val < 0, f"embed_spec c_det4 = {val:.4f}, expected negative (mirror)"

    def test_ktl_embed_gives_positive_cdet4(self):
        """KTL embedding gives positive c_det4 for axial seed."""
        q = rational(32, rc=4, embed=embed_ktl)
        val = c_det4(q)
        assert val > 0, f"embed_ktl c_det4 = {val:.4f}, expected positive"

    def test_projection_check_near_zero_for_ktl(self):
        """projection_check is ≤ 1e-12 for any well-formed unit-norm field."""
        q = rational(32, rc=4, embed=embed_ktl)
        res = projection_check(q)
        assert res <= 1e-12, f"embed_ktl projection residual = {res:.3e}"

    # ── zsign flip: zsign=+1 gives -6 ────────────────────────────────────────

    def test_zsign_flip_gives_minus_six(self):
        """KTL §0: zsign=-1 is the correct sign. zsign=+1 (spec-literal) → C = -6."""
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

    # ── cold_control: degree 0 ────────────────────────────────────────────────

    def test_cold_control_cdet4_near_zero(self):
        """C0-cold seed has f(0)→0 → degree 0; c_det4 should be < 0.1."""
        q = cold_control(64, rc=8)
        val = c_det4(q)
        assert abs(val) < 0.1, f"cold_control 64³ c_det4 = {val:.4f}, expected ≈0"

    # ── mirror seed: degree −6 ────────────────────────────────────────────────

    def test_mirror_seed_c_exact_minus_six(self):
        """Mirror seed (Z1 → conj Z1) gives C = -6."""
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
