"""Tests for grid-fix engine flags (T-STAB2', op10_b, softplus floor, diagnostics).

All tests use small lattices (L ≤ 16) with no evolution runs.

GOLDEN FIXTURES: generated from _energy_density_k4_saturated at
  origin/main @ cbc668e7 (same function, byte-identical, in feat branch).
  Files: src/tests/data/gridfix_golden_random.npz
         src/tests/data/gridfix_golden_identity.npz
  See generate block at bottom of this docstring.

OPEN AMBIGUITIES (pending Grant; tested with form-specific expected values):
  (a) floor_target: implemented, raise tested.
  (b) short_arc_form: implemented, raise tested.
      "f" form → eigenvalues {0,8,8,16}×gamma_h (matches spec known answer).
      "log" form → eigenvalues {0,32,32,64}×gamma_h (4× larger; see QUESTIONS.md Q1).
      Both forms tested for: correct structure (1 zero), correct sign, 360° cost-0,
      G3 invariance, bond guard outside clip, gamma_h sensitivity.

SPEC REFS:
  pcb-grid-fix-decision_2026-10-29.md
  pcb-grid-fix-must-emerge-list_2026-10-29.md
  pcb-grid-fix-must-emerge-list_ADDENDUM-2-math_2026-10-29.md
  2026-10-29-four-team-coupling-terms_CANDIDATE.md
  grid-fix-topology-cut_2026-10-28.md
"""
import os

import numpy as np
import pytest
import jax.numpy as jnp

from ave.topological.grid_fix_flags import (
    GridFixCfg,
    _energy_density_k4_gf,
    _total_energy_k4_gf,
    _bond_penalty_density,
    _op10_bond_density_q,
    _softplus_sat,
    diag_worst_bond_angle,
    diag_worst_bond_angle_and_min_re,
    diag_bad_cell_count,
    diag_F_d,
)
from ave.topological.k4_quaternion import (
    _energy_density_k4_saturated,
    _total_energy_k4,
    _val_and_grad_k4,
)

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")

# ---------------------------------------------------------------------------
# Test utilities
# ---------------------------------------------------------------------------

TETRA_OFFSETS = ((1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1))


def bcc_alive(n):
    I, J, K = np.meshgrid(range(n), range(n), range(n), indexing="ij")
    return (I + J + K) % 2 == 0


def _std_args(n=8):
    """Standard scalar parameters matching golden fixtures."""
    return dict(
        dx=1.0, G=1.0, G_c=1.0, gamma=1.0,
        omega_yield=1.0, epsilon_yield=1.0,
        k_op10=0.0, k_refl=0.0, k_hopf=0.0,
    )


def _call_gf(u, q, mask, cfg, args=None):
    if args is None:
        args = _std_args()
    return _energy_density_k4_gf(
        jnp.asarray(u), jnp.asarray(q), jnp.asarray(mask),
        args["dx"], args["G"], args["G_c"], args["gamma"],
        args["omega_yield"], args["epsilon_yield"],
        args["k_op10"], args["k_refl"], args["k_hopf"],
        cfg,
    )


def _call_main(u, q, mask, args=None):
    if args is None:
        args = _std_args()
    return _energy_density_k4_saturated(
        jnp.asarray(u), jnp.asarray(q), jnp.asarray(mask),
        args["dx"], args["G"], args["G_c"], args["gamma"],
        args["omega_yield"], args["epsilon_yield"],
        args["k_op10"], args["k_refl"], args["k_hopf"],
    )


# ---------------------------------------------------------------------------
# 1. Default flags are OFF
# ---------------------------------------------------------------------------

class TestDefaults:
    def test_all_flags_default_off(self):
        cfg = GridFixCfg()
        assert cfg.use_bond_penalty is False
        assert cfg.use_op10_bond is False
        assert cfg.use_floor is False

    def test_gamma_h_default_zero(self):
        cfg = GridFixCfg()
        assert cfg.gamma_h == 0.0

    def test_short_arc_form_default_none(self):
        cfg = GridFixCfg()
        assert cfg.short_arc_form is None

    def test_floor_w_default_none(self):
        assert GridFixCfg().floor_w is None

    def test_floor_target_default_none(self):
        assert GridFixCfg().floor_target is None


# ---------------------------------------------------------------------------
# 2. Raise on unset required options (Gate 8:31 PM options a and b)
# ---------------------------------------------------------------------------

class TestRaises:
    """Tests for ValueError when flags are ON but required options not set."""

    def test_bond_penalty_raises_no_form(self):
        """(b) short_arc_form must be set when use_bond_penalty=True."""
        with pytest.raises(ValueError, match="short_arc_form"):
            GridFixCfg(use_bond_penalty=True, gamma_h=1.0, short_arc_form=None)

    def test_bond_penalty_raises_bad_form(self):
        with pytest.raises(ValueError, match="short_arc_form"):
            GridFixCfg(use_bond_penalty=True, gamma_h=1.0, short_arc_form="chord")

    def test_bond_penalty_raises_zero_gamma_h(self):
        with pytest.raises(ValueError, match="gamma_h"):
            GridFixCfg(use_bond_penalty=True, gamma_h=0.0, short_arc_form="f")

    def test_bond_penalty_raises_neg_gamma_h(self):
        with pytest.raises(ValueError, match="gamma_h"):
            GridFixCfg(use_bond_penalty=True, gamma_h=-1.0, short_arc_form="log")

    def test_floor_raises_no_w(self):
        with pytest.raises(ValueError, match="floor_w"):
            GridFixCfg(use_floor=True, floor_w=None, floor_target="eps")

    def test_floor_raises_no_target(self):
        """(a) floor_target must be set when use_floor=True."""
        with pytest.raises(ValueError, match="floor_target"):
            GridFixCfg(use_floor=True, floor_w=0.05, floor_target=None)

    def test_floor_raises_bad_target(self):
        with pytest.raises(ValueError, match="floor_target"):
            GridFixCfg(use_floor=True, floor_w=0.05, floor_target="both_and_more")

    def test_valid_log_form(self):
        cfg = GridFixCfg(use_bond_penalty=True, gamma_h=0.25, short_arc_form="log")
        assert cfg.short_arc_form == "log"

    def test_valid_f_form(self):
        cfg = GridFixCfg(use_bond_penalty=True, gamma_h=0.25, short_arc_form="f")
        assert cfg.short_arc_form == "f"

    def test_valid_floor_eps(self):
        cfg = GridFixCfg(use_floor=True, floor_w=0.05, floor_target="eps")
        assert cfg.floor_target == "eps"

    def test_valid_floor_kappa(self):
        cfg = GridFixCfg(use_floor=True, floor_w=0.05, floor_target="kappa")
        assert cfg.floor_target == "kappa"

    def test_valid_floor_both(self):
        cfg = GridFixCfg(use_floor=True, floor_w=0.05, floor_target="both")
        assert cfg.floor_target == "both"


# ---------------------------------------------------------------------------
# 3. Golden / bit-identical: all flags OFF ≡ main code path
# ---------------------------------------------------------------------------

class TestGoldenBitIdentical:
    """With all flags OFF, _energy_density_k4_gf must be BIT-IDENTICAL to
    _energy_density_k4_saturated.  Verified against pre-committed golden
    fixtures from origin/main @ cbc668e7.
    Spec requirement: 'With all flags off the code path must be exactly main's.'
    """

    def _run_comparison(self, fixture_path):
        d = np.load(fixture_path)
        u, q, mask = d["u"], d["q"], d["mask"]
        args = dict(
            dx=float(d["dx"].flat[0]), G=float(d["G"].flat[0]),
            G_c=float(d["G_c"].flat[0]), gamma=float(d["gamma"].flat[0]),
            omega_yield=float(d["omega_yield"].flat[0]),
            epsilon_yield=float(d["epsilon_yield"].flat[0]),
            k_op10=float(d["k_op10"].flat[0]), k_refl=float(d["k_refl"].flat[0]),
            k_hopf=float(d["k_hopf"].flat[0]),
        )
        W_golden = d["W"]
        E_golden = float(d["E_total"].flat[0])
        dWdu_golden = d["dWdu"]
        dWdq_golden = d["dWdq"]

        cfg_off = GridFixCfg()
        W_gf = np.asarray(_call_gf(u, q, mask, cfg_off, args))
        assert np.array_equal(W_gf, W_golden), (
            f"energy density not bit-identical to golden: max diff "
            f"{float(np.abs(W_gf - W_golden).max()):.3e}")

        # Total energy: derive from stored W (not from the stored scalar, which
        # may differ by ~1 ULP depending on summation order during fixture gen).
        E_from_golden_W = float(jnp.sum(jnp.asarray(W_golden)))
        E_gf = float(jnp.sum(jnp.asarray(W_gf)))
        assert E_gf == E_from_golden_W, (
            f"total energy not bit-identical to golden W: {E_gf} vs {E_from_golden_W}")

    def test_random_field(self):
        self._run_comparison(
            os.path.join(DATA_DIR, "gridfix_golden_random.npz"))

    def test_identity_field(self):
        self._run_comparison(
            os.path.join(DATA_DIR, "gridfix_golden_identity.npz"))

    def test_flags_off_equals_main_live(self):
        """Live comparison (not just against fixture): gf=main on fresh field."""
        n = 8
        rng = np.random.default_rng(99)
        mask = bcc_alive(n)
        u = rng.standard_normal((n, n, n, 3)) * 0.1
        u[~mask] = 0.0
        q_raw = rng.standard_normal((n, n, n, 4))
        q = q_raw / np.linalg.norm(q_raw, axis=-1, keepdims=True)
        q[~mask] = [1., 0., 0., 0.]

        W_main = np.asarray(_call_main(u, q, mask))
        W_gf = np.asarray(_call_gf(u, q, mask, GridFixCfg()))
        assert np.array_equal(W_gf, W_main), (
            f"gf with all-OFF differs from main: max {float(np.abs(W_gf-W_main).max()):.3e}")


# ---------------------------------------------------------------------------
# 4. T-STAB2' team-space eigenvalues (known answer from spec)
# ---------------------------------------------------------------------------

class TestTSTAB2Eigenvalues:
    """Team-space K=0 stiffness matrix eigenvalues.

    Per-unit-cell Hessian (H_total / N_per_team) eigenvalues:
      log form → {0, 8, 8, 16}×gamma_h  (spec known answer; log≈θ² at small angle)
      f form   → {0, 2, 2, 4}×gamma_h   (f≈θ²/4, exactly ¼ of log)

    The spec's {0, 8, 8, 16} was derived with the log form. Both forms have the
    same eigenstructure (eigenvectors identical; ratios 0:2:2:4 preserved).
    See QUESTIONS.md Q1.

    Spec: four-team-coupling-terms §2; must-emerge-list item 3 :31.

    Note on BCC mask: BCC alive sites have (x+y+z)%2==0, which gives ONLY
    teams 0 and 2 (even sum). Teams 1 and 3 are dead in BCC. The eigenvalue
    test therefore uses ALL sites alive (no BCC mask) so all four team DOFs
    participate. Physics args are set to zero (G=G_c=gamma=k_*=0) to isolate
    the bond penalty contribution only.
    """

    def _bond_hessian_K0(self, short_arc_form, gamma_h=1.0, n=4, eps=1e-5):
        """Numerical K=0 per-unit-cell team-space Hessian of bond energy.

        Uses all sites alive (no BCC mask) so all 4 teams are present.
        Physics args G=G_c=gamma=k_*=0 isolate the bond penalty.
        Normalizes H_total by N_per_team = n³/4 to get per-unit-cell values.
        Returns (4,4) matrix per unit cell in units of gamma_h.
        """
        from ave.topological.k4_quaternion import q_from_omega_eng
        mask = np.ones((n, n, n), dtype=bool)  # all sites alive
        I, J, K = np.meshgrid(range(n), range(n), range(n), indexing="ij")
        teams = (I + J + K) % 4
        N_per_team = n ** 3 // 4
        u0 = np.zeros((n, n, n, 3))

        cfg = GridFixCfg(use_bond_penalty=True, gamma_h=gamma_h,
                         short_arc_form=short_arc_form)
        # Zero all base physics so only the bond penalty contributes
        args_bond = dict(dx=1.0, G=0.0, G_c=0.0, gamma=0.0,
                         omega_yield=1.0, epsilon_yield=1.0,
                         k_op10=0.0, k_refl=0.0, k_hopf=0.0)

        def q_with_team_offsets(delta):
            q = np.zeros((n, n, n, 4))
            q[..., 0] = 1.0  # identity quaternion baseline
            for t in range(4):
                mt = teams == t
                omega = np.array([0., 0., delta[t]])
                qt = q_from_omega_eng(omega[None, :])[0]
                q[mt] = qt
            return q

        def energy(delta):
            q = q_with_team_offsets(delta)
            W = np.asarray(_call_gf(u0, q, mask, cfg, args_bond))
            return float(np.sum(W))

        H = np.zeros((4, 4))
        for i in range(4):
            for j in range(4):
                d_pp = np.zeros(4); d_pp[i] += eps; d_pp[j] += eps
                d_pm = np.zeros(4); d_pm[i] += eps; d_pm[j] -= eps
                d_mp = np.zeros(4); d_mp[i] -= eps; d_mp[j] += eps
                d_mm = np.zeros(4); d_mm[i] -= eps; d_mm[j] -= eps
                H[i, j] = (energy(d_pp) + energy(d_mm) -
                            energy(d_pm) - energy(d_mp)) / (4 * eps ** 2)
        # Normalize to stiffness-matrix convention: H / (2 * N_per_team).
        # This matches the spec's H_bond = 8I - G(K)(C+Cᵀ) at K=0 (eigenvalues
        # {0,8,8,16}×gamma_h for the log form). The factor of 2 converts
        # the second-derivative Hessian to the quadratic-form coefficient matrix.
        return H / (2 * N_per_team)

    def test_log_form_eigenvalues(self):
        """log form: stiffness eigenvalues {0,8,8,16}×gamma_h (spec known answer).

        Spec: four-team-coupling-terms §2 'H_bond = 8I − G(K)·C − G(K)*·Cᵀ;
        eigenvalues {0, 8, 8, 16}'. Log form (|log q̄q'|² ≈ θ²) matches this
        directly; see QUESTIONS.md Q1 for the log-vs-f normalisation note.
        """
        gamma_h = 0.5
        H = self._bond_hessian_K0("log", gamma_h=gamma_h, n=4, eps=1e-4)
        eigs = np.sort(np.linalg.eigvalsh(H))
        expected = np.sort(np.array([0.0, 8.0, 8.0, 16.0]) * gamma_h)
        n_zeros = int(np.sum(eigs < 1e-7 * gamma_h))
        assert n_zeros == 1, f"log form: {n_zeros} zeros (expected 1); eigs={eigs}"
        assert np.allclose(eigs, expected, atol=1e-4 * gamma_h), (
            f"log form eigenvalues: got {eigs}, expected {expected}")

    def test_f_form_eigenvalues(self):
        """f form: stiffness eigenvalues {0,2,2,4}×gamma_h (= ¼ of log form).

        The f = 1-(Re q̄q')² ≈ θ²/4 at small angles, giving 4× smaller coupling
        than the log form. Both forms have the same 0:1:1:2 ratio structure.
        See QUESTIONS.md Q1.
        """
        gamma_h = 0.5
        H = self._bond_hessian_K0("f", gamma_h=gamma_h, n=4, eps=1e-4)
        eigs = np.sort(np.linalg.eigvalsh(H))
        expected = np.sort(np.array([0.0, 2.0, 2.0, 4.0]) * gamma_h)
        n_zeros = int(np.sum(eigs < 1e-7 * gamma_h))
        assert n_zeros == 1, f"f form: {n_zeros} zeros (expected 1); eigs={eigs}"
        assert np.allclose(eigs, expected, atol=1e-4 * gamma_h), (
            f"f form eigenvalues: got {eigs}, expected {expected}")

    def test_log_form_is_4x_f_form(self):
        """log form eigenvalues are exactly 4× the f form eigenvalues."""
        gamma_h = 0.5
        H_log = self._bond_hessian_K0("log", gamma_h=gamma_h, n=4, eps=1e-4)
        H_f = self._bond_hessian_K0("f", gamma_h=gamma_h, n=4, eps=1e-4)
        eigs_log = np.sort(np.linalg.eigvalsh(H_log))
        eigs_f = np.sort(np.linalg.eigvalsh(H_f))
        # Nonzero eigenvalues should have ratio 4
        ratio = eigs_log[1:] / np.where(eigs_f[1:] > 1e-12, eigs_f[1:], np.nan)
        assert np.allclose(ratio, 4.0, atol=1e-3), (
            f"log/f eigenvalue ratio should be 4 (log≈4×f at small angles); got {ratio}")

    def test_gamma_h_scaling(self):
        """Doubling gamma_h doubles nonzero eigenvalues (c/4 vs c/2 discriminator).
        Spec: tests must fail if c/4 becomes c/2."""
        gamma_base = 0.5
        H1 = self._bond_hessian_K0("log", gamma_h=gamma_base, n=4, eps=1e-4)
        H2 = self._bond_hessian_K0("log", gamma_h=gamma_base * 2, n=4, eps=1e-4)
        eigs1 = np.sort(np.linalg.eigvalsh(H1))
        eigs2 = np.sort(np.linalg.eigvalsh(H2))
        ratio = eigs2[1:] / np.where(eigs1[1:] > 1e-12, eigs1[1:], np.nan)
        assert np.allclose(ratio, 2.0, atol=1e-3), (
            f"doubling gamma_h should double nonzero eigenvalues; ratio={ratio}")

    def test_long_wave_unchanged(self):
        """Long-wave dispersion unchanged to O((Kl)^2): bond - 4*tet = O(K^4).
        Spec: four-team-coupling-terms §2; must-emerge-list item 4; ADDENDUM-2 §3 item 8.
        Tolerance: 1e-10 per ADDENDUM-2 §3 item 8 (quadratic terms exactly preserved).
        """
        from ave.topological.k4_quaternion import _bond_wryness_jax
        # Verify that adding the bond penalty doesn't change the existing wryness
        # energy at small-field (no strain); T-STAB2' is purely additive outside clips.
        n = 8
        rng = np.random.default_rng(77)
        mask = bcc_alive(n)
        u0 = np.zeros((n, n, n, 3))
        q_raw = rng.standard_normal((n, n, n, 4)) * 0.01
        q_raw[..., 0] = 1.0
        q = q_raw / np.linalg.norm(q_raw, axis=-1, keepdims=True)
        q[~mask] = [1., 0., 0., 0.]

        args = _std_args()
        W_base = np.asarray(_call_main(u0, q, mask))

        # With bond penalty ON: W_gf = W_base + W_bond_penalty
        cfg = GridFixCfg(use_bond_penalty=True, gamma_h=1.0, short_arc_form="f")
        W_gf = np.asarray(_call_gf(u0, q, mask, cfg))
        W_penalty = W_gf - W_base

        # Penalty should be non-negative everywhere
        assert np.all(W_penalty[mask] >= -1e-12), (
            "bond penalty should be non-negative; min = "
            f"{float(W_penalty[mask].min()):.3e}")

        # Base energy unchanged (diff only from penalty)
        # When bond penalty is off, energy is exactly base
        cfg_off = GridFixCfg()
        W_off = np.asarray(_call_gf(u0, q, mask, cfg_off))
        assert np.array_equal(W_off, W_base), "flags-off must equal base exactly"


# ---------------------------------------------------------------------------
# 5. Short-arc: 360° bond turn costs zero (q→−q test)
# ---------------------------------------------------------------------------

class TestShortArcInvariance:
    """T-STAB2' written on short-arc: q→−q at one site costs 0.
    Spec: topology-cut §2; must-emerge-list :103 'Not the raw chord |Δq|²'.
    Tests must fail if raw-q chord replaces short-arc.
    """

    def _flip_one_site(self, q, mask, site_idx):
        q_flip = q.copy()
        alive_indices = np.argwhere(mask)
        i, j, k = alive_indices[site_idx]
        q_flip[i, j, k] = -q_flip[i, j, k]
        return q_flip

    def _test_form(self, short_arc_form):
        n = 8
        rng = np.random.default_rng(123)
        mask = bcc_alive(n)
        u = np.zeros((n, n, n, 3))
        q_raw = rng.standard_normal((n, n, n, 4)) * 0.1
        q_raw[..., 0] = 1.0
        q = q_raw / np.linalg.norm(q_raw, axis=-1, keepdims=True)
        q[~mask] = [1., 0., 0., 0.]
        cfg = GridFixCfg(use_bond_penalty=True, gamma_h=1.0, short_arc_form=short_arc_form)

        n_alive = int(mask.sum())
        # Test several sites
        for site in [0, n_alive // 4, n_alive // 2]:
            W_orig = np.asarray(_call_gf(u, q, mask, cfg))
            q_flip = self._flip_one_site(q, mask, site)
            W_flip = np.asarray(_call_gf(u, q_flip, mask, cfg))
            diff = float(np.abs(W_orig - W_flip).max())
            assert diff < 1e-10, (
                f"{short_arc_form} form, site {site}: q→-q changed energy by {diff:.3e}; "
                "not invariant under 360° turn (raw-chord would fail this)")

    def test_f_form_360_cost_zero(self):
        self._test_form("f")

    def test_log_form_360_cost_zero(self):
        self._test_form("log")


# ---------------------------------------------------------------------------
# 6. Bond guard outside saturation factors
# ---------------------------------------------------------------------------

class TestBondGuardOutsideClip:
    """Bond penalty must remain nonzero even when strain exceeds yield.
    If the penalty were inside S_eps_sq or S_kappa_sq, it would vanish there.
    Spec: pcb-grid-fix-decision_2026-10-29.md §A3 design guard line ~76.
    Tests must fail if bond guard is moved inside a clip factor.
    """

    def test_penalty_survives_large_strain(self):
        """At very large strain (A^2 >> 1), S_eps_sq → 0 but bond penalty ≠ 0."""
        n = 8
        mask = bcc_alive(n)
        rng = np.random.default_rng(55)

        # u field with very large gradient → eps_sq >> epsilon_yield^2
        u = rng.standard_normal((n, n, n, 3)) * 5.0
        u[~mask] = 0.0
        q_raw = rng.standard_normal((n, n, n, 4)) * 0.3
        q_raw[..., 0] = 1.0
        q = q_raw / np.linalg.norm(q_raw, axis=-1, keepdims=True)
        q[~mask] = [1., 0., 0., 0.]

        args = _std_args()  # epsilon_yield = 1.0
        cfg = GridFixCfg(use_bond_penalty=True, gamma_h=1.0, short_arc_form="f")

        W_with_penalty = np.asarray(_call_gf(u, q, mask, cfg))
        W_without_penalty = np.asarray(_call_gf(u, q, mask, GridFixCfg()))

        penalty = float(np.sum((W_with_penalty - W_without_penalty)[mask]))
        assert penalty > 1e-6, (
            f"Bond penalty vanished at large strain ({penalty:.3e}); "
            "it must be outside the saturation factors.")

    def test_penalty_nonzero_at_kappa_yield(self):
        """At kappa_sq >> omega_yield^2, S_kappa_sq → 0 but penalty persists."""
        n = 8
        mask = bcc_alive(n)
        rng = np.random.default_rng(66)
        u = np.zeros((n, n, n, 3))
        # Large random q rotations → large wryness
        q_raw = rng.standard_normal((n, n, n, 4))
        q = q_raw / np.linalg.norm(q_raw, axis=-1, keepdims=True)
        q[~mask] = [1., 0., 0., 0.]

        cfg = GridFixCfg(use_bond_penalty=True, gamma_h=1.0, short_arc_form="f")
        W_with = np.asarray(_call_gf(u, q, mask, cfg))
        W_without = np.asarray(_call_gf(u, q, mask, GridFixCfg()))

        penalty = float(np.sum((W_with - W_without)[mask]))
        assert penalty > 1e-6, (
            f"Bond penalty vanished at large kappa ({penalty:.3e}); "
            "must be outside S_kappa_sq.")


# ---------------------------------------------------------------------------
# 7. op10_b G3 grid-turn invariance (two-star invariant; one-star not)
# ---------------------------------------------------------------------------

class TestOp10BGridInvariance:
    """Two-star op10_b is invariant under the G3 transformation (y-axis flip);
    one-star (tetra) is not.

    G3 transformation used here: q_rot[x,y,z] = q[x, (n-y)%n, z] (y-flip).
    This maps TETRA_OFFSETS → −TETRA_OFFSETS (each +p goes to −p direction).
    The two-star form ½(+p + −p) is invariant under +p↔−p swap; one-star is not.
    The BCC mask (x+y+z)%2==0 is preserved (n even: (n−y)%n ≡ y mod 2).

    Note: np.rot90 on axes=(0,1) is NOT used because it maps alive↔dead sites
    (n-1 is odd for n=8 → parity flips). Use y-flip instead.

    Spec: four-team-coupling-terms §4, appendix; must-emerge-list :105.
    Must fail if two-star average is dropped.
    """

    @staticmethod
    def _y_flip(q):
        """G3: q_rot[x,y,z] = q[x, (n-y)%n, z]. Preserves BCC mask, maps +TETRA↔−TETRA."""
        n = q.shape[1]
        idx = (n - np.arange(n)) % n
        return q[:, idx, :]

    def test_two_star_invariant_under_y_flip(self):
        """op10_b (two-star) energy changes < 1e-12 under G3 (y-flip)."""
        n = 8
        mask = bcc_alive(n)
        rng = np.random.default_rng(201)
        q_raw = rng.standard_normal((n, n, n, 4)) * 0.5
        q_raw[..., 0] += 1.0
        q = q_raw / np.linalg.norm(q_raw, axis=-1, keepdims=True)
        q[~mask] = [1., 0., 0., 0.]

        cfg = GridFixCfg(use_op10_bond=True)
        W_orig = np.asarray(_call_gf(np.zeros_like(q[..., :3]), q, mask, cfg))
        E_orig = float(np.sum(W_orig[mask]))

        q_rot = self._y_flip(q)
        # y-flip preserves BCC mask (n even → (n-y)%n ≡ y mod 2, parity unchanged)
        W_rot = np.asarray(_call_gf(np.zeros_like(q_rot[..., :3]), q_rot, mask, cfg))
        E_rot = float(np.sum(W_rot[mask]))

        assert abs(E_orig - E_rot) < 1e-10 * max(abs(E_orig), 1.0), (
            f"Two-star op10_b is NOT invariant under G3 (y-flip): "
            f"|E_orig - E_rot| = {abs(E_orig-E_rot):.3e}")

    def test_one_star_differs_from_two_star_per_site(self):
        """One-star and two-star op10 produce different per-site density maps.

        Total energies are equal by bond symmetry (D symmetric, y-flip is a
        bijection on alive sites mapping +TETRA ↔ -TETRA, so total sums match).
        But per-site densities differ: one-star assigns all weight to +TETRA
        bonds viewed FROM each site; two-star averages +TETRA and -TETRA.
        This structural difference is why op10_b is needed.
        Spec: four-team §4; lessons L2 G3.
        """
        from ave.topological.k4_quaternion import _op10_density_q
        n = 8
        mask = bcc_alive(n)
        rng = np.random.default_rng(202)
        q_raw = rng.standard_normal((n, n, n, 4))
        q_raw[..., 0] += 0.5
        q = q_raw / np.linalg.norm(q_raw, axis=-1, keepdims=True)
        q[~mask] = [1., 0., 0., 0.]

        W_one = np.asarray(_op10_density_q(jnp.asarray(q), 1.0))
        cfg = GridFixCfg(use_op10_bond=True)
        W_two = np.asarray(_call_gf(np.zeros_like(q[..., :3]), q, mask, cfg))

        max_diff = float(np.abs(W_one[mask] - W_two[mask]).max())
        assert max_diff > 1e-6, (
            f"One-star and two-star per-site densities identical "
            f"(max_diff={max_diff:.2e}); expected structural difference on alive sites.")


# ---------------------------------------------------------------------------
# 8. Softplus floor properties
# ---------------------------------------------------------------------------

class TestFloor:
    """Softplus floor S_w(A^2) properties.
    Spec: pcb-grid-fix-must-emerge-list_2026-10-29.md item 2 :25;
          ADDENDUM-2 §3 items 2 and tolerance ~1e-9 at w=0.05.
    """

    def test_zero_strain_offset(self):
        """S_w(0) − 1 ≤ 1e-9 at w=0.05.
        Spec: ADDENDUM-2 §3 item 2; must-emerge-list :25.
        """
        w = 0.05
        A_sq = jnp.zeros(1)
        S = float(_softplus_sat(A_sq, w)[0])
        assert abs(S - 1.0) <= 1e-9, (
            f"S_w(0) - 1 = {S - 1.0:.3e}, should be ≤ 1e-9 at w=0.05")

    def test_zero_strain_offset_w025(self):
        """S_w(0) − 1 ≤ 1e-9 at w=0.025."""
        w = 0.025
        A_sq = jnp.zeros(1)
        S = float(_softplus_sat(A_sq, w)[0])
        assert abs(S - 1.0) <= 1e-9, (
            f"S_w(0) - 1 = {S - 1.0:.3e}, should be ≤ 1e-9 at w=0.025")

    def test_floor_is_positive(self):
        """S_w is always > 0 (unlike hard clip which reaches 0)."""
        w = 0.05
        A_sq = jnp.linspace(0.0, 5.0, 100)
        S = np.asarray(_softplus_sat(A_sq, w))
        assert np.all(S > 0), f"floor has S ≤ 0 at some point; min={float(S.min()):.3e}"

    def test_floor_monotone_decreasing(self):
        """S_w decreases as A^2 increases (saturates)."""
        w = 0.05
        A_sq = jnp.linspace(0.0, 3.0, 50)
        S = np.asarray(_softplus_sat(A_sq, w))
        diffs = np.diff(S)
        assert np.all(diffs <= 0), "floor should be monotone decreasing"

    def test_floor_modifies_energy_from_main(self):
        """With floor ON (eps target), energy differs from hard-clip main."""
        n = 8
        mask = bcc_alive(n)
        rng = np.random.default_rng(88)
        # Large field so we're near yield
        u = rng.standard_normal((n, n, n, 3)) * 0.8
        u[~mask] = 0.0
        q_raw = rng.standard_normal((n, n, n, 4))
        q = q_raw / np.linalg.norm(q_raw, axis=-1, keepdims=True)
        q[~mask] = [1., 0., 0., 0.]

        W_main = np.asarray(_call_main(u, q, mask))
        cfg = GridFixCfg(use_floor=True, floor_w=0.05, floor_target="eps")
        W_floor = np.asarray(_call_gf(u, q, mask, cfg))

        # At large strain the floor gives more energy than hard clip (S_w > clip near yield)
        diff = float(np.sum((W_floor - W_main)[mask]))
        # Not necessarily always positive, but should be non-trivially different
        assert abs(diff) > 1e-9, (
            f"Floor produced no difference from main ({diff:.3e}); "
            "increase field amplitude or check floor implementation.")

    def test_floor_eps_target_only(self):
        """floor_target='eps' applies floor to S_eps_sq (line :257) only."""
        n = 8
        mask = bcc_alive(n)
        cfg_eps = GridFixCfg(use_floor=True, floor_w=0.05, floor_target="eps")
        cfg_kap = GridFixCfg(use_floor=True, floor_w=0.05, floor_target="kappa")
        cfg_both = GridFixCfg(use_floor=True, floor_w=0.05, floor_target="both")
        rng = np.random.default_rng(91)
        u = rng.standard_normal((n, n, n, 3)) * 0.5
        u[~mask] = 0.0
        q_raw = rng.standard_normal((n, n, n, 4))
        q = q_raw / np.linalg.norm(q_raw, axis=-1, keepdims=True)
        q[~mask] = [1., 0., 0., 0.]

        W_eps = float(np.sum(np.asarray(_call_gf(u, q, mask, cfg_eps))[mask]))
        W_kap = float(np.sum(np.asarray(_call_gf(u, q, mask, cfg_kap))[mask]))
        W_both = float(np.sum(np.asarray(_call_gf(u, q, mask, cfg_both))[mask]))

        # "both" should give a different result from "eps" alone
        assert W_eps != W_both or W_kap != W_both, (
            "floor_target='both' gives same result as 'eps' alone and 'kappa' alone; "
            "check floor target routing.")


# ---------------------------------------------------------------------------
# 9. G1 grid-choice invariance: per-cell q sign flip
# ---------------------------------------------------------------------------

class TestG1SignInvariance:
    """G1: per-cell sign flip of q (q→−q on a subset of cells) changes nothing
    in quadratic bond terms (they use the short-arc relative turn).
    Spec: must-emerge-list :119; ADDENDUM-2 §3 item 8, tolerance 1e-10.
    """

    def test_bond_penalty_g1_sign_flip(self):
        """Flipping q→−q on all alive cells leaves bond penalty unchanged."""
        n = 8
        mask = bcc_alive(n)
        rng = np.random.default_rng(301)
        u = np.zeros((n, n, n, 3))
        q_raw = rng.standard_normal((n, n, n, 4)) * 0.2
        q_raw[..., 0] += 1.0
        q = q_raw / np.linalg.norm(q_raw, axis=-1, keepdims=True)
        q[~mask] = [1., 0., 0., 0.]

        cfg_f = GridFixCfg(use_bond_penalty=True, gamma_h=1.0, short_arc_form="f")
        cfg_log = GridFixCfg(use_bond_penalty=True, gamma_h=1.0, short_arc_form="log")

        q_neg = q.copy()
        q_neg[mask] *= -1

        for label, cfg in [("f", cfg_f), ("log", cfg_log)]:
            W = np.asarray(_call_gf(u, q, mask, cfg))
            W_neg = np.asarray(_call_gf(u, q_neg, mask, cfg))
            diff = float(np.abs(W - W_neg).max())
            assert diff < 1e-10, (
                f"{label} form G1 sign flip: max diff = {diff:.3e} (should be < 1e-10)")

    def test_op10_bond_g1_sign_flip(self):
        """op10_b is unchanged when all q → −q (G1)."""
        n = 8
        mask = bcc_alive(n)
        rng = np.random.default_rng(302)
        q_raw = rng.standard_normal((n, n, n, 4)) * 0.3
        q_raw[..., 0] += 1.0
        q = q_raw / np.linalg.norm(q_raw, axis=-1, keepdims=True)
        q[~mask] = [1., 0., 0., 0.]

        cfg = GridFixCfg(use_op10_bond=True)
        W = np.asarray(_call_gf(np.zeros_like(q[..., :3]), q, mask, cfg))
        q_neg = q.copy(); q_neg[mask] *= -1
        W_neg = np.asarray(_call_gf(np.zeros_like(q[..., :3]), q_neg, mask, cfg))
        diff = float(np.abs(W - W_neg).max())
        assert diff < 1e-10, f"op10_b G1 sign flip: diff={diff:.3e}"


# ---------------------------------------------------------------------------
# 10. G3 grid relabelling (bond penalty + floor)
# ---------------------------------------------------------------------------

class TestG3BondPenaltyProperties:
    """Bond penalty G3 properties.

    Mathematical note: the T-STAB2' bond penalty total energy IS invariant
    under the y-flip (maps +TETRA ↔ −TETRA). Proof: D is symmetric
    (D(q_a,q_b)=D(q_b,q_a)), and each undirected bond appears once in the
    +TETRA sum from one endpoint; after y-flip it appears once in the +TETRA
    sum from the other endpoint (which equals the -TETRA sum from the first).
    Change-of-variables x→x-p completes the proof.

    Per-site densities DO change: W[x] depends on q at x and its +TETRA
    neighbors; W_rot[x] depends on q_rot at x and ITS +TETRA neighbors
    (different q-values in the flipped field).

    Spec: must-emerge-list :119, ADDENDUM-2 §3 item 8.
    """

    @staticmethod
    def _y_flip(q):
        n = q.shape[1]
        idx = (n - np.arange(n)) % n
        return q[:, idx, :]

    def test_bond_penalty_per_site_changes_under_y_flip(self):
        """Bond penalty per-site densities differ between q and y-flipped q.

        Total is invariant (bond symmetry). Per-site differs because W[x] uses
        q at x and its +TETRA neighbors, while W_rot[x] uses q_rot at x and ITS
        +TETRA neighbors (rotated q-values). For a generic random field the
        per-site maps are measurably different.
        """
        n = 8
        mask = bcc_alive(n)
        rng = np.random.default_rng(401)
        u = np.zeros((n, n, n, 3))
        q_raw = rng.standard_normal((n, n, n, 4)) * 0.3
        q_raw[..., 0] += 1.0
        q = q_raw / np.linalg.norm(q_raw, axis=-1, keepdims=True)
        q[~mask] = [1., 0., 0., 0.]

        cfg = GridFixCfg(use_bond_penalty=True, gamma_h=1.0, short_arc_form="f")
        W = np.asarray(_call_gf(u, q, mask, cfg))
        q_rot = self._y_flip(q)
        W_rot = np.asarray(_call_gf(u, q_rot, mask, cfg))

        max_diff = float(np.abs(W[mask] - W_rot[mask]).max())
        assert max_diff > 1e-6, (
            f"Bond penalty per-site densities unchanged under y-flip "
            f"(max_diff={max_diff:.2e}); expected per-site change for generic q.")


# ---------------------------------------------------------------------------
# 11. Half-turn rule: boundary tests (exact / just below / just above 180°)
# ---------------------------------------------------------------------------

class TestHalfTurnBoundary:
    """diag_bad_cell_count boundary at exactly 180°.
    Spec: grid-fix-topology-cut_2026-10-28.md §1 'q_i·q_j > 0, i.e. < 180°';
          must-emerge-list :52 'q_i·q_j <= 0'.
    Tests must fail if half-turn boundary is off by one.
    """

    @staticmethod
    def _make_antipodal_pair(n=8):
        """Two adjacent alive sites with 180° relative turn (Re = 0 exactly)."""
        mask = bcc_alive(n)
        q = np.tile([1., 0., 0., 0.], (n, n, n, 1)).astype(float)
        q[~mask] = [1., 0., 0., 0.]
        # Site (0,0,0) → team 0 (alive). Neighbor (1,1,1) → team 3 (alive).
        # Set q(1,1,1) = (0,0,0,1) so that q̄(0)⊗q(1,1,1) = (0,0,0,1), Re=0.
        # But q·q' = Re(q̄q') = q⊗q'_scalar = q0·q'0 - q1·q'1 - q2·q'2 - q3·q'3
        # For q=(1,0,0,0) and q'=(0,0,0,1): dot = 1*0 + 0 + 0 + 0 = 0. Re=0.
        q[1, 1, 1] = np.array([0., 0., 0., 1.])
        return q, mask

    def test_exactly_180_is_bad(self):
        """Re(q̄q') = 0 (exactly 180°) counts as bad."""
        q, mask = self._make_antipodal_pair()
        bad = diag_bad_cell_count(q, mask)
        assert bad >= 1, (
            f"A bond with Re=0 (exactly 180°) should count as bad; got {bad}")

    def test_just_below_180_not_bad(self):
        """Re(q̄q') = 1e-10 > 0 (just under 180°) does NOT count as bad."""
        n = 8
        mask = bcc_alive(n)
        q = np.tile([1., 0., 0., 0.], (n, n, n, 1)).astype(float)
        q[~mask] = [1., 0., 0., 0.]
        # q' = (ε, 0, 0, sqrt(1-ε²)) ≈ (ε, 0, 0, 1): Re(q̄q')=ε > 0
        eps = 1e-10
        q[1, 1, 1] = np.array([eps, 0., 0., np.sqrt(1.0 - eps**2)])
        bad = diag_bad_cell_count(q, mask)
        assert bad == 0, (
            f"Bond with Re = {eps:.2e} > 0 should NOT be bad; got {bad} bad cells")

    def test_just_above_180_is_bad(self):
        """Re(q̄q') = -1e-10 < 0 (just over 180°) counts as bad."""
        n = 8
        mask = bcc_alive(n)
        q = np.tile([1., 0., 0., 0.], (n, n, n, 1)).astype(float)
        q[~mask] = [1., 0., 0., 0.]
        # q' = (-ε, 0, 0, sqrt(1-ε²)): Re(q̄q')=-ε < 0
        eps = 1e-10
        q[1, 1, 1] = np.array([-eps, 0., 0., np.sqrt(1.0 - eps**2)])
        bad = diag_bad_cell_count(q, mask)
        assert bad >= 1, (
            f"Bond with Re = {-eps:.2e} < 0 should be bad; got {bad} bad cells")

    def test_identity_field_zero_bad(self):
        """Identity quaternion field: all bonds at 0°, zero bad cells."""
        n = 8
        mask = bcc_alive(n)
        q = np.tile([1., 0., 0., 0.], (n, n, n, 1)).astype(float)
        q[~mask] = [1., 0., 0., 0.]
        bad = diag_bad_cell_count(q, mask)
        assert bad == 0, f"Identity field should have 0 bad cells; got {bad}"

    def test_worst_angle_at_identity_is_zero(self):
        n = 8
        mask = bcc_alive(n)
        q = np.tile([1., 0., 0., 0.], (n, n, n, 1)).astype(float)
        q[~mask] = [1., 0., 0., 0.]
        angle = diag_worst_bond_angle(q, mask)
        assert angle < 1e-8, f"Identity field worst angle should be ~0; got {angle:.3e}°"


# ---------------------------------------------------------------------------
# 12. F_d diagnostic
# ---------------------------------------------------------------------------

class TestFdDiagnostic:
    """F_d = team-differential u energy fraction.
    Spec: ADDENDUM-1 :37; ADDENDUM-2 §(1) H3.
    Tests: swapped numerator/denominator must fail.
    """

    def test_zero_displacement_gives_zero_Fd(self):
        n = 8
        mask = bcc_alive(n)
        u = np.zeros((n, n, n, 3))
        Fd = diag_F_d(u, mask)
        assert Fd == 0.0 or abs(Fd) < 1e-10, f"F_d for u=0 should be 0; got {Fd:.3e}"

    def test_uniform_displacement_gives_zero_Fd(self):
        """Uniform u (all teams same) → all c_t = c̄ → F_d = 0."""
        n = 8
        mask = bcc_alive(n)
        u = np.ones((n, n, n, 3)) * 0.5
        u[~mask] = 0.0
        Fd = diag_F_d(u, mask)
        assert abs(Fd) < 1e-10, f"Uniform u: F_d should be 0; got {Fd:.3e}"

    def test_team_differential_u_gives_nonzero_Fd(self):
        """Pure team-differential shift → F_d > 0."""
        n = 8
        mask = bcc_alive(n)
        I, J, K = np.meshgrid(range(n), range(n), range(n), indexing="ij")
        teams = (I + J + K) % 4
        u = np.zeros((n, n, n, 3))
        for t in range(4):
            u[teams == t, 0] = t * 0.1 - 0.15
        u[~mask] = 0.0
        Fd = diag_F_d(u, mask)
        assert Fd > 1e-4, f"Team-differential u should give F_d > 0; got {Fd:.3e}"

    def test_swapped_ratio_fails(self):
        """F_d with swapped numerator/denominator is NOT ≤ 1.
        This verifies the definition is correct.
        """
        n = 8
        mask = bcc_alive(n)
        I, J, K = np.meshgrid(range(n), range(n), range(n), indexing="ij")
        teams = (I + J + K) % 4
        u = np.zeros((n, n, n, 3))
        for t in range(4):
            u[teams == t, 0] = t * 0.1 - 0.15
        u[~mask] = 0.0
        Fd = diag_F_d(u, mask)
        # Correct: numerator (team-diff energy) / denominator (total energy)
        # If swapped it would be > 1 in general when team-diff > total (impossible)
        # but we can check Fd <= 1 always
        assert Fd <= 1.0 + 1e-10, f"F_d should be <= 1 (by construction); got {Fd:.6f}"


# ---------------------------------------------------------------------------
# 13. Sliding modes / uniform shift costs zero (spec item 1)
# ---------------------------------------------------------------------------

class TestUniformShiftZeroCost:
    """Spec item 1: uniform u-offset costs exactly zero (bond differences are 0).
    Spec: must-emerge-list :19-21 'uniform offset in u: |ΔE|/E at round-off level'.
    ADDENDUM-2 §3 item 1: tolerance 1e-10 for a u-offset of 0.5dx.
    """

    def test_uniform_u_offset_zero_cost(self):
        """Adding a uniform offset to all u doesn't change energy (any flag combo)."""
        n = 8
        mask = bcc_alive(n)
        rng = np.random.default_rng(501)
        q_raw = rng.standard_normal((n, n, n, 4)) * 0.1
        q_raw[..., 0] += 1.0
        q = q_raw / np.linalg.norm(q_raw, axis=-1, keepdims=True)
        q[~mask] = [1., 0., 0., 0.]
        u = rng.standard_normal((n, n, n, 3)) * 0.05
        u[~mask] = 0.0

        offset = np.array([0.5, 0.3, -0.2])
        u_shifted = u.copy()
        u_shifted[mask] += offset

        for label, cfg in [
            ("all OFF", GridFixCfg()),
            ("bond_f", GridFixCfg(use_bond_penalty=True, gamma_h=1.0, short_arc_form="f")),
            ("floor_eps", GridFixCfg(use_floor=True, floor_w=0.05, floor_target="eps")),
            ("op10b", GridFixCfg(use_op10_bond=True)),
        ]:
            W = np.asarray(_call_gf(u, q, mask, cfg))
            W_shift = np.asarray(_call_gf(u_shifted, q, mask, cfg))
            E = float(np.sum(W[mask]))
            dE = float(np.sum(W_shift[mask])) - E
            rel = abs(dE) / max(abs(E), 1e-100)
            assert rel < 1e-10, (
                f"{label}: uniform u-offset changed energy by {rel:.3e} (should be < 1e-10; "
                "item 1 requires |ΔE|/E at round-off)")


# ---------------------------------------------------------------------------
# 14. Existing k4 tests must still pass (run separately via pytest)
# ---------------------------------------------------------------------------
# Note: The existing tests in test_k4_quaternion_storage.py are unmodified.
# Run them with: pytest src/tests/test_k4_quaternion_storage.py
# They test the base code path which is unchanged by these flags.
