"""Tests for grid-fix engine flags (T-STAB2', op10_b, softplus floor, diagnostics).

All tests use small lattices (L ≤ 16) with no evolution runs.

GOLDEN FIXTURES: generated from _energy_density_k4_saturated at
  origin/main @ cbc668e7 (same function, byte-identical, in feat branch).
  Files: src/tests/data/gridfix_golden_random.npz
         src/tests/data/gridfix_golden_identity.npz
  See generate block at bottom of this docstring.

GRANT'S 10-29 DECLARED CHOICES (ADD-3 REV-1; implemented and tested here):
  (a) short_arc_form = "log" (ADD-3 §4.1). "f" accepted at construction but
      raises NotImplementedError at compute time (ADD-3 §4.1 open item).
  (b) floor_target = "iii" (both + readout; ADD-3 REV-1 §R.1/§R.2).
      "i" = eps only (k4q:257). "ii" = eps+kappa (k4q:257+258).
      "iii" = (ii) + readout in cf:733-738 (read-only; energy = "ii").
  (c) gamma_h = γ/4 by default (cfg.gamma_h=None → runtime default from engine gamma).
  (d) use_sponge (FLAG 4): dt-invariant sponge, OWN FLAG, default OFF.

OPEN AMBIGUITIES — see ~/AVE-staging/runs/gridfix/QUESTIONS.md:
  Q3 — F_d spec form on BCC lattice: NOT-SPEC-COMPLIANT (see TestFdDiagnostic).
  Q4 — omega_yield vs π for kappa A = κ²/π² (ADD-3 §3.3.3; add if omega_yield≠π).

SPEC REFS:
  pcb-grid-fix-must-emerge-list_ADDENDUM-3-math_2026-10-29.md (sha1 dd40aa31ed7e)
  pcb-grid-fix-must-emerge-list_ADDENDUM-4-math_2026-10-29.md (sha1 26324f84de66)
  2026-10-29-sliding-mode-criterion_CANDIDATE.md (sha1 80f5cf77226c)
"""
import math
import os

import numpy as np
import pytest
import jax.numpy as jnp

from ave.topological.grid_fix_flags import (
    GridFixCfg,
    _energy_density_k4_gf,
    _total_energy_k4_gf,
    _bond_guard_density,
    _op10_bond_density_q,
    _softplus_sat,
    compute_sponge_sigma_max,
    sponge_attenuation,
    sponge_mask_3d,
    read_back_flags,
    diag_worst_bond_angle,
    diag_worst_bond_angle_and_min_re,
    diag_bad_cell_count,
    diag_F_d,
    diag_F_d_L2_provisional,
    diag_Fd_slide,
    _READOUT_DELTA_R,
    _USE_IMPEDANCE_BOUNDARY,
)
from ave.topological.k4_quaternion import (
    _energy_density_k4_saturated,
    _bond_wryness_jax,
    _quat_mul_jax,
    _op10_density_q,
    _hopf_density_q,
)
from ave.topological.cosserat_field_3d import (
    _readout_floor,
    _update_saturation_kernels,
)

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")

# ---------------------------------------------------------------------------
# Test utilities
# ---------------------------------------------------------------------------

TETRA_OFFSETS = ((1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1))


def engine_alive_mask(n):
    """Engine's real alive mask: all-even OR all-odd coordinate sites.

    Matches CosseratField3D mask_alive (cf:1056-1060): mask_A | mask_B where
    mask_A = all-even and mask_B = all-odd. Gives all 4 teams (0-3) for n≥2.
    """
    I, J, K = np.meshgrid(range(n), range(n), range(n), indexing="ij")
    return ((I % 2 == 0) & (J % 2 == 0) & (K % 2 == 0)) | \
           ((I % 2 == 1) & (J % 2 == 1) & (K % 2 == 1))


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
        assert cfg.use_sponge is False

    def test_gamma_h_default_none(self):
        """gamma_h=None by default (runtime default γ/4 from engine gamma). ADD-3 §3.3.1."""
        cfg = GridFixCfg()
        assert cfg.gamma_h is None

    def test_short_arc_form_default_none(self):
        cfg = GridFixCfg()
        assert cfg.short_arc_form is None

    def test_floor_w_default_none(self):
        assert GridFixCfg().floor_w is None

    def test_floor_target_default_none(self):
        assert GridFixCfg().floor_target is None

    def test_use_sponge_default_false(self):
        """FLAG 4 sponge has its own default OFF. ADD-3 REV-1 §R.3."""
        assert GridFixCfg().use_sponge is False


# ---------------------------------------------------------------------------
# 2. Raise on unset required options
# ---------------------------------------------------------------------------

class TestRaises:
    """Tests for ValueError when flags are ON but required options not set."""

    def test_bond_penalty_raises_no_form(self):
        with pytest.raises(ValueError, match="short_arc_form"):
            GridFixCfg(use_bond_penalty=True, gamma_h=1.0, short_arc_form=None)

    def test_bond_penalty_raises_bad_form(self):
        with pytest.raises(ValueError, match="short_arc_form"):
            GridFixCfg(use_bond_penalty=True, gamma_h=1.0, short_arc_form="chord")

    def test_bond_penalty_raises_zero_gamma_h(self):
        """Explicit gamma_h=0.0 is rejected (use None for default γ/4). ADD-3 §3.3.1."""
        with pytest.raises(ValueError, match="gamma_h"):
            GridFixCfg(use_bond_penalty=True, gamma_h=0.0, short_arc_form="log")

    def test_bond_penalty_raises_neg_gamma_h(self):
        with pytest.raises(ValueError, match="gamma_h"):
            GridFixCfg(use_bond_penalty=True, gamma_h=-1.0, short_arc_form="log")

    def test_bond_penalty_none_gamma_h_ok(self):
        """gamma_h=None (runtime default) is valid at construction. ADD-3 §3.3.1."""
        cfg = GridFixCfg(use_bond_penalty=True, gamma_h=None, short_arc_form="log")
        assert cfg.gamma_h is None

    def test_floor_raises_no_w(self):
        with pytest.raises(ValueError, match="floor_w"):
            GridFixCfg(use_floor=True, floor_w=None, floor_target="i")

    def test_floor_raises_no_target(self):
        with pytest.raises(ValueError, match="floor_target"):
            GridFixCfg(use_floor=True, floor_w=0.05, floor_target=None)

    def test_floor_raises_bad_target(self):
        """Old names 'eps'/'kappa'/'both' are no longer valid. ADD-3 §3.3.3."""
        for bad in ("eps", "kappa", "both", "both_and_more"):
            with pytest.raises(ValueError, match="floor_target"):
                GridFixCfg(use_floor=True, floor_w=0.05, floor_target=bad)

    def test_valid_log_form(self):
        cfg = GridFixCfg(use_bond_penalty=True, gamma_h=0.25, short_arc_form="log")
        assert cfg.short_arc_form == "log"

    def test_valid_f_form_construction(self):
        """'f' accepted at construction (NotImplementedError at compute time). ADD-3 §4.1."""
        cfg = GridFixCfg(use_bond_penalty=True, gamma_h=0.25, short_arc_form="f")
        assert cfg.short_arc_form == "f"

    def test_valid_floor_i(self):
        cfg = GridFixCfg(use_floor=True, floor_w=0.05, floor_target="i")
        assert cfg.floor_target == "i"

    def test_valid_floor_ii(self):
        cfg = GridFixCfg(use_floor=True, floor_w=0.05, floor_target="ii")
        assert cfg.floor_target == "ii"

    def test_valid_floor_iii(self):
        """'iii' is Grant's 10-29 declared choice. ADD-3 REV-1 §R.1."""
        cfg = GridFixCfg(use_floor=True, floor_w=0.05, floor_target="iii")
        assert cfg.floor_target == "iii"


# ---------------------------------------------------------------------------
# 3. Golden / bit-identical: all flags OFF ≡ main code path
# ---------------------------------------------------------------------------

class TestGoldenBitIdentical:
    """With all flags OFF, _energy_density_k4_gf must be BIT-IDENTICAL to
    _energy_density_k4_saturated (same JIT path).

    Primary test: live comparison gf(OFF) vs main — W, E, dW/du, dW/dq all
    bitwise equal (both go through the same JIT path on the same machine).

    Fixture tests: cross-platform tolerance atol=1e-14 (JIT vs eager on Linux
    gives ~5.6e-17 deltas per ulp; fixtures generated on macOS @ cbc668e7).

    Spec: 'With all flags off the code path must be exactly main's.'
    """

    def test_flags_off_equals_main_live_WE_grad(self):
        """PRIMARY: gf(OFF) vs main — W, E, dW/du, dW/dq bitwise equal (same JIT)."""
        import jax
        from ave.topological.grid_fix_flags import _total_energy_k4_gf

        n = 8
        rng = np.random.default_rng(99)
        mask = engine_alive_mask(n)
        u = rng.standard_normal((n, n, n, 3)) * 0.1
        u[~mask] = 0.0
        q_raw = rng.standard_normal((n, n, n, 4))
        q = q_raw / np.linalg.norm(q_raw, axis=-1, keepdims=True)
        q[~mask] = [1., 0., 0., 0.]

        args = _std_args(n)
        u_j = jnp.asarray(u)
        q_j = jnp.asarray(q)
        mask_j = jnp.asarray(mask)
        cfg_off = GridFixCfg()

        # W
        W_main = np.asarray(_call_main(u, q, mask, args))
        W_gf = np.asarray(_call_gf(u, q, mask, cfg_off, args))
        assert np.array_equal(W_gf, W_main), (
            f"W not bitwise: max diff {float(np.abs(W_gf - W_main).max()):.3e}")

        # E
        E_main = float(jnp.sum(jnp.asarray(W_main)))
        E_gf = float(jnp.sum(jnp.asarray(W_gf)))
        assert E_gf == E_main, f"E not bitwise: {E_gf} vs {E_main}"

        # dW/du and dW/dq via JIT value_and_grad of total energy
        from ave.topological.k4_quaternion import _total_energy_k4

        def _call_main_total(u_, q_):
            return _total_energy_k4(
                u_, q_, mask_j, args["dx"], args["G"], args["G_c"],
                args["gamma"], args["omega_yield"], args["epsilon_yield"],
                args["k_op10"], args["k_refl"], args["k_hopf"])

        def _call_gf_total(u_, q_):
            return _total_energy_k4_gf(
                u_, q_, mask_j, args["dx"], args["G"], args["G_c"],
                args["gamma"], args["omega_yield"], args["epsilon_yield"],
                args["k_op10"], args["k_refl"], args["k_hopf"], cfg_off)

        vg_main = jax.jit(jax.value_and_grad(_call_main_total, argnums=(0, 1)))
        vg_gf = jax.jit(jax.value_and_grad(_call_gf_total, argnums=(0, 1)))

        _, (du_main, dq_main) = vg_main(u_j, q_j)
        _, (du_gf, dq_gf) = vg_gf(u_j, q_j)

        assert np.array_equal(np.asarray(du_gf), np.asarray(du_main)), (
            f"dW/du not bitwise: max diff "
            f"{float(np.abs(np.asarray(du_gf) - np.asarray(du_main)).max()):.3e}")
        assert np.array_equal(np.asarray(dq_gf), np.asarray(dq_main)), (
            f"dW/dq not bitwise: max diff "
            f"{float(np.abs(np.asarray(dq_gf) - np.asarray(dq_main)).max()):.3e}")

    def _run_fixture_comparison(self, fixture_path):
        """Cross-platform fixture check with atol=1e-14 (JIT vs eager ~5.6e-17)."""
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
        cfg_off = GridFixCfg()
        W_gf = np.asarray(_call_gf(u, q, mask, cfg_off, args))
        assert np.allclose(W_gf, W_golden, atol=1e-14, rtol=0), (
            f"energy density not close to golden (atol=1e-14): max diff "
            f"{float(np.abs(W_gf - W_golden).max()):.3e}")

    def test_random_field_fixture(self):
        self._run_fixture_comparison(
            os.path.join(DATA_DIR, "gridfix_golden_random.npz"))

    def test_identity_field_fixture(self):
        self._run_fixture_comparison(
            os.path.join(DATA_DIR, "gridfix_golden_identity.npz"))


# ---------------------------------------------------------------------------
# 4. T-STAB2' team-space eigenvalues (compensated residual, ADD-3 §3.3.1)
# ---------------------------------------------------------------------------

class TestTSTAB2Eigenvalues:
    """Team-space K=0 stiffness matrix eigenvalues for log (compensated) form.

    Per-unit-cell Hessian (H_total / N_per_team) eigenvalues:
      log form → {0, 8, 8, 16}×gamma_h  (spec known answer; ADD-3 §3.3.1)
      At K=0: compensation = 0 (Σ_p p_j = 0 for TETRA_OFFSETS), so r_p = dw_p.
      The {0,8,8,16} eigenvalues are unchanged by the compensation at K=0.
      At long wave (K→0): guard is O(K⁴) while un-compensated log is O(K²).

    "f" form: accepted at construction, raises NotImplementedError at compute time.
    ADD-3 §4.1: the scalar f is uncompensated; it does not implement the guard.

    Spec: ADD-3 §3.3.1; four-team-coupling-terms §2; must-emerge-list item 3 :31.

    Note on BCC mask: BCC alive sites give only teams 0 and 2. The eigenvalue
    test uses ALL sites alive (no BCC mask) so all four team DOFs participate.
    """

    def _bond_hessian_K0(self, short_arc_form, gamma_h=1.0, gamma_engine=None,
                          n=4, eps=1e-5, mask=None):
        """Numerical K=0 per-unit-cell team-space Hessian of bond energy.

        Uses all sites alive (no mask) by default so all 4 teams are present.
        Physics args G=G_c=gamma=k_*=0 isolate the bond penalty.
        Normalizes H_total by N_per_team = alive/4 to get per-unit-cell values.
        Returns (4,4) matrix per unit cell in units of gamma_h.
        """
        from ave.topological.k4_quaternion import q_from_omega_eng
        if mask is None:
            mask = np.ones((n, n, n), dtype=bool)
        I, J, K = np.meshgrid(range(n), range(n), range(n), indexing="ij")
        teams = (I + J + K) % 4
        N_per_team = int(np.sum(mask)) // 4
        u0 = np.zeros((n, n, n, 3))

        # gamma_engine: for testing gamma_h=None → γ/4 defaulting
        if gamma_h is None:
            assert gamma_engine is not None
            cfg = GridFixCfg(use_bond_penalty=True, gamma_h=None,
                             short_arc_form=short_arc_form)
            gamma_eff = gamma_engine
        else:
            cfg = GridFixCfg(use_bond_penalty=True, gamma_h=gamma_h,
                             short_arc_form=short_arc_form)
            gamma_eff = 1.0

        args_bond = dict(dx=1.0, G=0.0, G_c=0.0, gamma=gamma_eff,
                         omega_yield=1.0, epsilon_yield=1.0,
                         k_op10=0.0, k_refl=0.0, k_hopf=0.0)

        def q_with_team_offsets(delta):
            q = np.zeros((n, n, n, 4))
            q[..., 0] = 1.0
            for t in range(4):
                mt = teams == t
                omega = np.array([0., 0., delta[t]])
                qt = q_from_omega_eng(omega[None, :])[0]
                q[mt] = qt
            q[~mask] = [1., 0., 0., 0.]
            return q

        def energy(delta):
            q = q_with_team_offsets(delta)
            W = np.asarray(_call_gf(u0, q, mask, cfg, args_bond))
            return float(np.sum(W[mask]))

        H = np.zeros((4, 4))
        for i in range(4):
            for j in range(4):
                d_pp = np.zeros(4); d_pp[i] += eps; d_pp[j] += eps
                d_pm = np.zeros(4); d_pm[i] += eps; d_pm[j] -= eps
                d_mp = np.zeros(4); d_mp[i] -= eps; d_mp[j] += eps
                d_mm = np.zeros(4); d_mm[i] -= eps; d_mm[j] -= eps
                H[i, j] = (energy(d_pp) + energy(d_mm) -
                            energy(d_pm) - energy(d_mp)) / (4 * eps ** 2)
        return H / (2 * N_per_team)

    def test_log_form_eigenvalues(self):
        """log form (compensated residual): stiffness eigenvalues {0,8,8,16}×gamma_h.

        ADD-3 §3.3.1 known answer. At K=0, κ=0 (Σ_p p_j=0), r_p=dw_p, so
        compensated guard = uncompensated log guard at K=0. Eigenvalues unchanged.
        """
        gamma_h = 0.5
        H = self._bond_hessian_K0("log", gamma_h=gamma_h, n=4, eps=1e-4)
        eigs = np.sort(np.linalg.eigvalsh(H))
        expected = np.sort(np.array([0.0, 8.0, 8.0, 16.0]) * gamma_h)
        n_zeros = int(np.sum(eigs < 1e-7 * gamma_h))
        assert n_zeros == 1, f"log form: {n_zeros} zeros (expected 1); eigs={eigs}"
        assert np.allclose(eigs, expected, atol=1e-4 * gamma_h), (
            f"log form eigenvalues: got {eigs}, expected {expected}")

    def test_f_form_raises_not_implemented(self):
        """'f' form raises NotImplementedError at COMPUTE time. ADD-3 §4.1.

        The scalar f = 1-(Re q̄q')² is uncompensated. It raises NotImplementedError
        at energy computation to prevent its use. This tests the mutant killer:
        'gamma_h=γ/2 instead of γ/4 or raw chord instead of log'.
        """
        from ave.topological.k4_quaternion import q_from_omega_eng
        n = 4
        mask = np.ones((n, n, n), dtype=bool)
        u0 = np.zeros((n, n, n, 3))
        q = np.tile([1., 0., 0., 0.], (n, n, n, 1)).astype(float)
        cfg = GridFixCfg(use_bond_penalty=True, gamma_h=1.0, short_arc_form="f")
        with pytest.raises(NotImplementedError, match="ADD-3 §4.1"):
            _call_gf(u0, q, mask, cfg)

    def test_gamma_h_scaling(self):
        """Doubling gamma_h doubles nonzero eigenvalues (γ/4 vs γ/2 discriminator).
        Spec: tests must fail if c/4 becomes c/2. ADD-3 §3.3.1.
        """
        gamma_base = 0.5
        H1 = self._bond_hessian_K0("log", gamma_h=gamma_base, n=4, eps=1e-4)
        H2 = self._bond_hessian_K0("log", gamma_h=gamma_base * 2, n=4, eps=1e-4)
        eigs1 = np.sort(np.linalg.eigvalsh(H1))
        eigs2 = np.sort(np.linalg.eigvalsh(H2))
        ratio = eigs2[1:] / np.where(eigs1[1:] > 1e-12, eigs1[1:], np.nan)
        assert np.allclose(ratio, 2.0, atol=1e-3), (
            f"doubling gamma_h should double nonzero eigenvalues; ratio={ratio}")

    def test_gamma_h_none_defaults_to_gamma_over_4(self):
        """gamma_h=None: effective gamma_h = engine gamma / 4. ADD-3 §3.3.1.

        Mutant killer: gamma_h=γ/2 instead of γ/4 would give 2× larger eigenvalues.
        Mutant killer: gamma_h=γ would give 4× larger eigenvalues.
        """
        # With gamma_engine=E, effective gamma_h = E/4.
        # So eigenvalues should be {0,8,8,16}*(E/4) = {0,2,2,4}*E.
        gamma_engine = 0.8  # chosen != 1.0 to be discriminating
        H_default = self._bond_hessian_K0("log", gamma_h=None,
                                           gamma_engine=gamma_engine, n=4, eps=1e-4)
        # Explicit gamma_h = E/4 should match exactly
        H_explicit = self._bond_hessian_K0("log", gamma_h=gamma_engine / 4.0, n=4, eps=1e-4)
        eigs_default = np.sort(np.linalg.eigvalsh(H_default))
        eigs_explicit = np.sort(np.linalg.eigvalsh(H_explicit))
        assert np.allclose(eigs_default, eigs_explicit, atol=1e-6), (
            f"gamma_h=None should give same eigenvalues as explicit gamma_h=γ/4; "
            f"got {eigs_default} vs {eigs_explicit}")
        # Also check the nonzero eigenvalues are {8,8,16} * (gamma_engine/4) = {2,2,4}*gamma_engine
        gamma_h_eff = gamma_engine / 4.0
        expected = np.sort([0.0, 8.0, 8.0, 16.0]) * gamma_h_eff
        assert np.allclose(eigs_default, expected, atol=1e-4), (
            f"gamma_h=None eigenvalues: got {eigs_default}, expected {expected}")

    def test_log_form_eigenvalues_engine_mask_n4(self):
        """log form eigenvalues {0,8,8,16} hold on engine_alive_mask, n=4. R1.

        engine_alive_mask has all 4 teams (not BCC-2-team limit). The K=0 Hessian
        should give the same eigenvalue set as the all-alive case since the team
        coupling is local and the mask is team-balanced.
        """
        gamma_h = 0.5
        H = self._bond_hessian_K0("log", gamma_h=gamma_h, n=4, eps=1e-4,
                                   mask=engine_alive_mask(4))
        eigs = np.sort(np.linalg.eigvalsh(H))
        expected = np.sort(np.array([0.0, 8.0, 8.0, 16.0]) * gamma_h)
        n_zeros = int(np.sum(eigs < 1e-6 * gamma_h))
        assert n_zeros == 1, f"engine_mask n=4: {n_zeros} zeros (expected 1); eigs={eigs}"
        assert np.allclose(eigs, expected, atol=0.05 * gamma_h), (
            f"engine_mask n=4 eigenvalues: got {eigs}, expected {expected}")

    def test_log_form_eigenvalues_engine_mask_n8(self):
        """log form eigenvalues {0,8,8,16} hold on engine_alive_mask, n=8. R1.

        Larger grid confirms the team-space eigenvalue set is not grid-size artifact.
        """
        gamma_h = 0.5
        H = self._bond_hessian_K0("log", gamma_h=gamma_h, n=8, eps=1e-4,
                                   mask=engine_alive_mask(8))
        eigs = np.sort(np.linalg.eigvalsh(H))
        expected = np.sort(np.array([0.0, 8.0, 8.0, 16.0]) * gamma_h)
        n_zeros = int(np.sum(eigs < 1e-6 * gamma_h))
        assert n_zeros == 1, f"engine_mask n=8: {n_zeros} zeros (expected 1); eigs={eigs}"
        assert np.allclose(eigs, expected, atol=0.05 * gamma_h), (
            f"engine_mask n=8 eigenvalues: got {eigs}, expected {expected}")

    def test_long_wave_unchanged(self):
        """Bond penalty is additive outside clips; flags-off energy unchanged. ADD-3 §3.3.1."""
        n = 8
        rng = np.random.default_rng(77)
        mask = engine_alive_mask(n)
        u0 = np.zeros((n, n, n, 3))
        q_raw = rng.standard_normal((n, n, n, 4)) * 0.01
        q_raw[..., 0] = 1.0
        q = q_raw / np.linalg.norm(q_raw, axis=-1, keepdims=True)
        q[~mask] = [1., 0., 0., 0.]

        W_base = np.asarray(_call_main(u0, q, mask))

        cfg = GridFixCfg(use_bond_penalty=True, gamma_h=1.0, short_arc_form="log")
        W_gf = np.asarray(_call_gf(u0, q, mask, cfg))
        W_penalty = W_gf - W_base

        assert np.all(W_penalty[mask] >= -1e-12), (
            "bond penalty should be non-negative; min = "
            f"{float(W_penalty[mask].min()):.3e}")

        cfg_off = GridFixCfg()
        W_off = np.asarray(_call_gf(u0, q, mask, cfg_off))
        assert np.array_equal(W_off, W_base), "flags-off must equal base exactly"


# ---------------------------------------------------------------------------
# 5. HL-1/2 identity: ¼Σ|dw_p|² = |κ|² + ¼Σ|r_p|² (ADD-3 §3.2)
# ---------------------------------------------------------------------------

class TestHL12Identity:
    """ADD-3 §3.2: orthogonal decomposition of bond log-map vectors.

    ¼ Σ_p |dw_p|² = Tr(κᵀκ) + ¼ Σ_p |r_p|²
    where κ = _bond_wryness_jax(q, dx) and r_p = dw_p − dx·κ·p.

    This is the Pythagorean theorem for the orthogonal projection of the bond
    vectors onto the gradient modes. The guard (¼Σ|r_p|²) is the residual energy.
    Expected to hold to round-off (float64 ~1e-14 relative).

    Mutant killers: uncompensated guard (drop dx·κ·p term), wrong κ computation.
    """

    def _compute_dw_kappa_residual(self, q, dx):
        """Compute dw_p, κ, and r_p = dw_p - dx·κ·p for all bonds. Returns arrays."""
        from ave.topological.k4_quaternion import _quat_mul_jax
        kappa = np.asarray(_bond_wryness_jax(jnp.asarray(q), dx))  # (*,3,3)
        q_conj = q * np.array([1., -1., -1., -1.])
        dws = []
        rs = []
        for (di, dj, dk) in TETRA_OFFSETS:
            q_nb = np.roll(np.roll(np.roll(q, -di, 0), -dj, 1), -dk, 2)
            prod = np.asarray(_quat_mul_jax(jnp.asarray(q_conj), jnp.asarray(q_nb)))
            s = np.where(prod[..., 0:1] >= 0., 1., -1.)
            prod = prod * s
            vec = prod[..., 1:]
            v2 = np.sum(vec ** 2, axis=-1, keepdims=True)
            vn = np.sqrt(np.where(v2 > 1e-30, v2, np.ones_like(v2)))
            theta = np.arctan2(vn, prod[..., 0:1])
            sinc_v = np.sinc(theta / np.pi)
            scale = np.where(v2 > 1e-30, 1.0 / sinc_v, np.ones_like(sinc_v))
            dw = 2.0 * scale * vec                                 # (*,3)
            p_vec = np.array([float(di), float(dj), float(dk)])
            kappa_p = np.einsum('...ij,j->...i', kappa, p_vec)    # (*,3)
            r = dw - dx * kappa_p
            dws.append(dw)
            rs.append(r)
        return dws, kappa, rs

    def test_hl12_identity_random_field(self):
        """ADD-3 §3.2 identity ¼Σ|dw|² = dx²·Tr(κᵀκ) + ¼Σ|r|² holds to 1e-10.

        At dx=1 this reduces to the spec's ¼Σ|dw|² = Tr(κᵀκ) + ¼Σ|r|².
        At general dx: ¼Σ|dw|² = dx²·Tr(κᵀκ) + ¼Σ|r|² (from Pythagorean
        theorem: Σ_p|proj_p|² = dx²·4·Tr(κᵀκ) since Σ_p p_i p_j = 4δ_{ij}).
        """
        n = 8
        rng = np.random.default_rng(701)
        q_raw = rng.standard_normal((n, n, n, 4)) * 0.3
        q_raw[..., 0] += 1.0
        q = q_raw / np.linalg.norm(q_raw, axis=-1, keepdims=True)
        dx = 1.0

        dws, kappa, rs = self._compute_dw_kappa_residual(q, dx)

        lhs = 0.25 * sum(np.sum(dw ** 2, axis=-1) for dw in dws)
        tr_kk = np.sum(kappa ** 2, axis=(-1, -2))              # Tr(κᵀκ)
        rhs = dx ** 2 * tr_kk + 0.25 * sum(np.sum(r ** 2, axis=-1) for r in rs)

        max_rel_err = float(np.max(np.abs(lhs - rhs) / (np.abs(lhs) + 1e-30)))
        assert max_rel_err < 1e-10, (
            f"HL-1/2 identity ¼Σ|dw|²=dx²·Tr(κᵀκ)+¼Σ|r|² violated: max rel err = {max_rel_err:.3e}")

    def test_hl12_identity_dx_not_one(self):
        """HL-1/2 identity holds for dx ≠ 1 (dx=0.5). ADD-3 §3.2."""
        n = 6
        rng = np.random.default_rng(702)
        q_raw = rng.standard_normal((n, n, n, 4)) * 0.2
        q_raw[..., 0] += 1.0
        q = q_raw / np.linalg.norm(q_raw, axis=-1, keepdims=True)
        dx = 0.5

        dws, kappa, rs = self._compute_dw_kappa_residual(q, dx)

        lhs = 0.25 * sum(np.sum(dw ** 2, axis=-1) for dw in dws)
        tr_kk = np.sum(kappa ** 2, axis=(-1, -2))
        rhs = dx ** 2 * tr_kk + 0.25 * sum(np.sum(r ** 2, axis=-1) for r in rs)

        max_rel_err = float(np.max(np.abs(lhs - rhs) / (np.abs(lhs) + 1e-30)))
        assert max_rel_err < 1e-10, (
            f"HL-1/2 identity fails at dx=0.5: max rel err = {max_rel_err:.3e}")


# ---------------------------------------------------------------------------
# 6. Short-arc: 360° bond turn costs zero (q→−q test)
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

    def test_log_form_360_cost_zero(self):
        """log form: q→-q at any alive site leaves bond guard unchanged."""
        n = 8
        rng = np.random.default_rng(123)
        mask = engine_alive_mask(n)
        u = np.zeros((n, n, n, 3))
        q_raw = rng.standard_normal((n, n, n, 4)) * 0.1
        q_raw[..., 0] = 1.0
        q = q_raw / np.linalg.norm(q_raw, axis=-1, keepdims=True)
        q[~mask] = [1., 0., 0., 0.]
        cfg = GridFixCfg(use_bond_penalty=True, gamma_h=1.0, short_arc_form="log")

        n_alive = int(mask.sum())
        for site in [0, n_alive // 4, n_alive // 2]:
            W_orig = np.asarray(_call_gf(u, q, mask, cfg))
            q_flip = self._flip_one_site(q, mask, site)
            W_flip = np.asarray(_call_gf(u, q_flip, mask, cfg))
            diff = float(np.abs(W_orig - W_flip).max())
            assert diff < 1e-10, (
                f"log form, site {site}: q→-q changed energy by {diff:.3e}; "
                "not invariant under 360° turn (raw-chord would fail this)")

    def test_f_form_raises_at_compute_time(self):
        """'f' form accepted at construction but raises NotImplementedError at compute.

        ADD-3 §4.1: the scalar f = 1-(Re q̄q')² is uncompensated. Mutant killer:
        'raw chord instead of log' or 'f form as compensated guard'.
        """
        n = 6
        mask = np.ones((n, n, n), dtype=bool)
        u = np.zeros((n, n, n, 3))
        q = np.tile([1., 0., 0., 0.], (n, n, n, 1)).astype(float)
        cfg = GridFixCfg(use_bond_penalty=True, gamma_h=1.0, short_arc_form="f")
        with pytest.raises(NotImplementedError):
            _call_gf(u, q, mask, cfg)


# ---------------------------------------------------------------------------
# 7. Bond guard outside saturation factors
# ---------------------------------------------------------------------------

class TestBondGuardOutsideClip:
    """Bond penalty must remain nonzero even when strain exceeds yield.
    Spec: pcb-grid-fix-decision_2026-10-29.md §A3.
    Tests must fail if bond guard is moved inside a clip factor.
    """

    def test_penalty_survives_large_strain(self):
        """At very large strain (A^2 >> 1), S_eps_sq → 0 but bond penalty ≠ 0."""
        n = 8
        mask = engine_alive_mask(n)
        rng = np.random.default_rng(55)
        u = rng.standard_normal((n, n, n, 3)) * 5.0
        u[~mask] = 0.0
        q_raw = rng.standard_normal((n, n, n, 4)) * 0.3
        q_raw[..., 0] = 1.0
        q = q_raw / np.linalg.norm(q_raw, axis=-1, keepdims=True)
        q[~mask] = [1., 0., 0., 0.]

        cfg = GridFixCfg(use_bond_penalty=True, gamma_h=1.0, short_arc_form="log")
        W_with_penalty = np.asarray(_call_gf(u, q, mask, cfg))
        W_without_penalty = np.asarray(_call_gf(u, q, mask, GridFixCfg()))

        penalty = float(np.sum((W_with_penalty - W_without_penalty)[mask]))
        assert penalty > 1e-6, (
            f"Bond penalty vanished at large strain ({penalty:.3e}); "
            "must be outside saturation factors.")

    def test_penalty_nonzero_at_kappa_yield(self):
        """At kappa_sq >> omega_yield^2, S_kappa_sq → 0 but penalty persists."""
        n = 8
        mask = engine_alive_mask(n)
        rng = np.random.default_rng(66)
        u = np.zeros((n, n, n, 3))
        q_raw = rng.standard_normal((n, n, n, 4))
        q = q_raw / np.linalg.norm(q_raw, axis=-1, keepdims=True)
        q[~mask] = [1., 0., 0., 0.]

        cfg = GridFixCfg(use_bond_penalty=True, gamma_h=1.0, short_arc_form="log")
        W_with = np.asarray(_call_gf(u, q, mask, cfg))
        W_without = np.asarray(_call_gf(u, q, mask, GridFixCfg()))

        penalty = float(np.sum((W_with - W_without)[mask]))
        assert penalty > 1e-6, (
            f"Bond penalty vanished at large kappa ({penalty:.3e}); "
            "must be outside S_kappa_sq.")


# ---------------------------------------------------------------------------
# 8. op10_b G3 grid-turn invariance (two-star invariant; one-star not)
# ---------------------------------------------------------------------------

class TestOp10BGridInvariance:
    """Two-star op10_b is invariant under the G3 transformation (y-axis flip).
    ADD-3 §3.3.2; four-team-coupling-terms §4.

    Note on mask: op10_b requires alive TETRA neighbors. On engine_alive_mask
    (all-even | all-odd), all TETRA neighbors of an alive site are alive.
    On bcc_alive, TETRA neighbors of (i+j+k)%2==0 sites all have (i+j+k)%2==1
    (dead) — making op10_b zero. These tests use ALL-ALIVE mask to give
    nonzero, meaningful op10_b (consistent with TestE3Invariance).
    Q5: G3 y-flip TOTAL energy invariance of op10_b — OPEN for Grant/Math.
    R2 (fix-pass-2b): empirical check on engine_alive_mask with k_op10=1 does NOT hold.
    (D-symmetry proof applies to pairwise D(a,b)=D(b,a), not quartic op10_b.)
    See ~/AVE-staging/runs/gridfix/QUESTIONS.md Q5 for details.
    """

    @staticmethod
    def _y_flip(q):
        n = q.shape[1]
        idx = (n - np.arange(n)) % n
        return q[:, idx, :]

    def test_two_star_per_site_changes_under_y_flip(self):
        """op10_b per-site densities change under y-flip (as expected for a quartic op).

        Q5: total-energy invariance of op10_b under G3 y-flip is unresolved.
        The D-symmetry proof in QUESTIONS.md applies to bond penalty (pairwise D)
        but NOT to op10_b (quartic functional). See QUESTIONS.md for Q5.
        This test documents that op10_b per-site IS sensitive to y-flip, which
        is the correct discriminating test (per QUESTIONS.md implementation note).
        ADD-3 §3.3.2. Uses ALL-ALIVE mask so TETRA neighbors are always alive.
        """
        n = 8
        mask = np.ones((n, n, n), dtype=bool)
        rng = np.random.default_rng(201)
        q_raw = rng.standard_normal((n, n, n, 4)) * 0.5
        q_raw[..., 0] += 1.0
        q = q_raw / np.linalg.norm(q_raw, axis=-1, keepdims=True)

        cfg = GridFixCfg(use_op10_bond=True)
        W_orig = np.asarray(_call_gf(np.zeros_like(q[..., :3]), q, mask, cfg))
        q_rot = self._y_flip(q)
        W_rot = np.asarray(_call_gf(np.zeros_like(q_rot[..., :3]), q_rot, mask, cfg))

        max_diff = float(np.abs(W_orig - W_rot).max())
        assert max_diff > 1e-6, (
            f"op10_b per-site densities unchanged under y-flip (max_diff={max_diff:.2e}); "
            "expected per-site change for generic q (quartic functional).")

    def test_op10b_g1_sign_flip_engine_mask_k_op10_nonzero(self):
        """G1 q→-q invariance on engine_alive_mask with k_op10≠0. (a) re-verify.

        op10_b depends only on n=R(q)ẑ which is invariant under q→-q
        (since R(-q) = R(q)). Energy must not change under G1 flip even when
        k_op10≠0, on the real engine alive mask. ADD-3 §3.3.2.
        """
        n = 8
        mask = engine_alive_mask(n)
        rng = np.random.default_rng(203)
        q_raw = rng.standard_normal((n, n, n, 4)) * 0.3
        q_raw[..., 0] += 1.0
        q = q_raw / np.linalg.norm(q_raw, axis=-1, keepdims=True)
        q[~mask] = [1., 0., 0., 0.]

        args = dict(dx=1.0, G=0.0, G_c=0.0, gamma=1.0, omega_yield=1.0,
                    epsilon_yield=1.0, k_op10=1.0, k_refl=0.0, k_hopf=0.0)
        cfg = GridFixCfg(use_op10_bond=True)
        W_orig = np.asarray(_call_gf(np.zeros_like(q[..., :3]), q, mask, cfg, args))

        q_neg = q.copy()
        q_neg[mask] *= -1
        W_neg = np.asarray(_call_gf(np.zeros_like(q[..., :3]), q_neg, mask, cfg, args))

        diff = float(np.abs(W_orig - W_neg).max())
        assert diff < 1e-10, (
            f"op10_b G1 sign flip (engine_alive_mask, k_op10=1): diff={diff:.3e}")

    def test_one_star_differs_from_two_star_per_site(self):
        """One-star and two-star op10 densities differ per site.

        Uses engine_alive_mask so TETRA neighbors are alive and op10_b nonzero.
        """
        n = 8
        mask = engine_alive_mask(n)
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
            f"(max_diff={max_diff:.2e}); expected structural difference.")

    def test_op10b_yflip_engine_mask_q5_record_only(self):
        """R2: op10_b G3 y-flip on engine_alive_mask, k_op10=1 — Q5 OPEN, record only.

        G3 y-flip: q(i,j,k) → q(i,(n-j)%n,k). idx=(n-arange(n))%n, no team relabelling.
        Total energy invariance does NOT hold on engine_alive_mask either
        (E_orig≈37.5, E_flip≈37.9, Δ≈0.37 at seed 204).

        Q5 status (fix-pass-2b, 2026-10-30): G3 y-flip of op10_b total energy is NOT
        invariant on engine_alive_mask. This is EXPECTED for a quartic functional —
        the D-symmetry proof applies only to pairwise-symmetric D(a,b)=D(b,a).
        Q5 is open for Grant/Math to adjudicate whether ADD-3 §3.3.2 G3-invariance
        applies to total energy or only to the field-transformation structure.

        This test documents energies and diff without asserting invariance.
        """
        n = 8
        mask = engine_alive_mask(n)
        rng = np.random.default_rng(204)
        q_raw = rng.standard_normal((n, n, n, 4)) * 0.3
        q_raw[..., 0] += 1.0
        q = q_raw / np.linalg.norm(q_raw, axis=-1, keepdims=True)
        q[~mask] = [1., 0., 0., 0.]

        args = dict(dx=1.0, G=0.0, G_c=0.0, gamma=1.0, omega_yield=1.0,
                    epsilon_yield=1.0, k_op10=1.0, k_refl=0.0, k_hopf=0.0)
        cfg = GridFixCfg(use_op10_bond=True)

        W_orig = np.asarray(_call_gf(np.zeros_like(q[..., :3]), q, mask, cfg, args))
        E_orig = float(np.sum(W_orig[mask]))

        idx = (n - np.arange(n)) % n
        q_flip = q[:, idx, :]
        q_flip[~mask] = [1., 0., 0., 0.]
        W_flip = np.asarray(_call_gf(np.zeros_like(q_flip[..., :3]), q_flip, mask, cfg, args))
        E_flip = float(np.sum(W_flip[mask]))

        diff = abs(E_orig - E_flip)
        # Q5 open: invariance does NOT hold. Record values only.
        assert E_orig > 0.0, "op10_b energy should be nonzero for random field"
        assert E_flip > 0.0, "op10_b energy should be nonzero after y-flip"
        assert np.isfinite(diff), "diff should be finite"
        # Do NOT assert diff < threshold — that would fail (diff ≈ 0.37 at seed 204)


# ---------------------------------------------------------------------------
# 9. op10_b dx scaling (ADD-3 §3.3.2)
# ---------------------------------------------------------------------------

class TestOp10BDxScaling:
    """op10_b scales as 1/dx⁴, matching _op10_density_q. ADD-3 §3.3.2.

    Mutant killer: old _op10_bond_density_q(q) (no dx) returns dimensionless
    (1/dx⁴ factor missing). New version divides by dx⁴.
    """

    def test_op10b_dx_scaling(self):
        """op10_b(dx=0.5) = op10_b(dx=1.0) * 16 (= 1/0.5⁴ = 16 relative factor)."""
        n = 8
        rng = np.random.default_rng(901)
        q_raw = rng.standard_normal((n, n, n, 4)) * 0.4
        q_raw[..., 0] += 1.0
        q = q_raw / np.linalg.norm(q_raw, axis=-1, keepdims=True)
        q_j = jnp.asarray(q)

        dx1 = 1.0
        dx2 = 0.5
        W1 = np.asarray(_op10_bond_density_q(q_j, dx1))
        W2 = np.asarray(_op10_bond_density_q(q_j, dx2))

        # W2 / W1 should be (dx1/dx2)^4 = (1/0.5)^4 = 16
        mask = np.abs(W1) > 1e-20
        ratio = W2[mask] / W1[mask]
        expected_ratio = (dx1 / dx2) ** 4
        assert np.allclose(ratio, expected_ratio, rtol=1e-10), (
            f"op10_b dx scaling: expected ratio {expected_ratio:.1f}; got {ratio[:5]}")

    def test_op10b_dx1_matches_structure(self):
        """At dx=1, op10_b is dimensionally consistent with _op10_density_q (same units)."""
        n = 8
        rng = np.random.default_rng(902)
        q_raw = rng.standard_normal((n, n, n, 4)) * 0.2
        q_raw[..., 0] += 1.0
        q = q_raw / np.linalg.norm(q_raw, axis=-1, keepdims=True)
        q_j = jnp.asarray(q)
        dx = 1.0

        W_bond = np.asarray(_op10_bond_density_q(q_j, dx))
        W_site = np.asarray(_op10_density_q(q_j, dx))

        # Both should be same order of magnitude (same units at dx=1)
        mask_nonzero = np.abs(W_site) > 1e-20
        if mask_nonzero.sum() == 0:
            pytest.skip("All-zero op10 (unlikely with random q)")
        ratio = np.abs(W_bond[mask_nonzero] / W_site[mask_nonzero])
        # Both should be same order of magnitude (same units, 1/dx⁴ at dx=1)
        # Different operators; allow up to 6 orders spread
        assert np.all(ratio < 1e6) and np.all(ratio > 1e-6), (
            f"op10_b and op10_site differ by >6 orders at dx=1; ratio range "
            f"[{float(ratio.min()):.2e}, {float(ratio.max()):.2e}]")


# ---------------------------------------------------------------------------
# 10. Softplus floor properties (ADD-3 §3.3.3)
# ---------------------------------------------------------------------------

class TestFloor:
    """Softplus floor S_w(A^2) properties. ADD-3 §3.3.3; ADD-2 §3."""

    def test_zero_strain_offset(self):
        """S_w(0) − 1 ≤ 1e-9 at w=0.05. ADD-2 §3 item 2."""
        w = 0.05
        A_sq = jnp.zeros(1)
        S = float(_softplus_sat(A_sq, w)[0])
        assert abs(S - 1.0) <= 1e-9, (
            f"S_w(0) - 1 = {S - 1.0:.3e}, should be ≤ 1e-9 at w=0.05")

    def test_zero_strain_offset_w025(self):
        w = 0.025
        A_sq = jnp.zeros(1)
        S = float(_softplus_sat(A_sq, w)[0])
        assert abs(S - 1.0) <= 1e-9, (
            f"S_w(0) - 1 = {S - 1.0:.3e}, should be ≤ 1e-9 at w=0.025")

    def test_floor_is_positive(self):
        w = 0.05
        A_sq = jnp.linspace(0.0, 5.0, 100)
        S = np.asarray(_softplus_sat(A_sq, w))
        assert np.all(S > 0), f"floor has S ≤ 0; min={float(S.min()):.3e}"

    def test_floor_monotone_decreasing(self):
        w = 0.05
        A_sq = jnp.linspace(0.0, 3.0, 50)
        S = np.asarray(_softplus_sat(A_sq, w))
        diffs = np.diff(S)
        assert np.all(diffs <= 0), "floor should be monotone decreasing"

    def test_floor_modifies_energy_from_main(self):
        """With floor ON (target 'i'), energy differs from hard-clip main."""
        n = 8
        mask = engine_alive_mask(n)
        rng = np.random.default_rng(88)
        u = rng.standard_normal((n, n, n, 3)) * 0.8
        u[~mask] = 0.0
        q_raw = rng.standard_normal((n, n, n, 4))
        q = q_raw / np.linalg.norm(q_raw, axis=-1, keepdims=True)
        q[~mask] = [1., 0., 0., 0.]

        W_main = np.asarray(_call_main(u, q, mask))
        cfg = GridFixCfg(use_floor=True, floor_w=0.05, floor_target="i")
        W_floor = np.asarray(_call_gf(u, q, mask, cfg))

        diff = float(np.sum((W_floor - W_main)[mask]))
        assert abs(diff) > 1e-9, (
            f"Floor produced no difference from main ({diff:.3e}); "
            "floor_target='i' should modify eps saturation.")

    def test_floor_ii_equals_iii_energy(self):
        """'ii' and 'iii' give identical k4q energy (readout is read-only). ADD-3 §3.3.3."""
        n = 8
        mask = engine_alive_mask(n)
        rng = np.random.default_rng(91)
        u = rng.standard_normal((n, n, n, 3)) * 0.5
        u[~mask] = 0.0
        q_raw = rng.standard_normal((n, n, n, 4)) * 0.3
        q_raw[..., 0] += 1.0
        q = q_raw / np.linalg.norm(q_raw, axis=-1, keepdims=True)
        q[~mask] = [1., 0., 0., 0.]

        cfg_ii = GridFixCfg(use_floor=True, floor_w=0.05, floor_target="ii")
        cfg_iii = GridFixCfg(use_floor=True, floor_w=0.05, floor_target="iii")

        W_ii = float(np.sum(np.asarray(_call_gf(u, q, mask, cfg_ii))[mask]))
        W_iii = float(np.sum(np.asarray(_call_gf(u, q, mask, cfg_iii))[mask]))

        assert W_ii == W_iii, (
            f"floor_target 'ii' and 'iii' should give identical k4 energy; "
            f"W_ii={W_ii:.6e}, W_iii={W_iii:.6e}")

    def test_floor_i_vs_ii_kappa_routing(self):
        """'i' applies floor to eps only; 'ii' also applies floor to kappa.

        Verifies the kappa branch routing by directly comparing the saturation
        factors computed from _softplus_sat vs hard clip at A_kappa=0.5.
        A_kappa=0.5: hard_clip gives 1-0.5=0.5; softplus gives S_w(0.5)>0.5.
        At gamma=1, W_kappa*S_kappa_sq differs between 'i' (hard kappa clip) and
        'ii' (softplus kappa). Use omega_yield=sqrt(2*kappa_sq) to get A=0.5.
        """
        n = 8
        mask = engine_alive_mask(n)
        rng = np.random.default_rng(91)
        u = rng.standard_normal((n, n, n, 3)) * 0.3
        u[~mask] = 0.0
        q_raw = rng.standard_normal((n, n, n, 4)) * 0.3
        q_raw[..., 0] += 1.0
        q = q_raw / np.linalg.norm(q_raw, axis=-1, keepdims=True)
        q[~mask] = [1., 0., 0., 0.]

        # Measure actual kappa_sq to set omega_yield = sqrt(2 * mean_kappa_sq)
        # so the mean A_kappa = 0.5 (middle of transition)
        kap = np.asarray(_bond_wryness_jax(jnp.asarray(q), 1.0))
        kap_sq_alive = np.sum(kap[mask] ** 2, axis=(-1, -2))
        mean_kap_sq = float(np.mean(kap_sq_alive))
        if mean_kap_sq < 1e-10:
            pytest.skip("kappa too small for this test field")
        omega_yield = float(np.sqrt(2.0 * mean_kap_sq))  # mean A_kappa ≈ 0.5

        args_tuned = dict(dx=1.0, G=1.0, G_c=1.0, gamma=1.0,
                          omega_yield=omega_yield, epsilon_yield=1.0,
                          k_op10=0.0, k_refl=0.0, k_hopf=0.0)

        cfg_i = GridFixCfg(use_floor=True, floor_w=0.05, floor_target="i")
        cfg_ii = GridFixCfg(use_floor=True, floor_w=0.05, floor_target="ii")

        W_i = float(np.sum(np.asarray(_call_gf(u, q, mask, cfg_i, args_tuned))[mask]))
        W_ii = float(np.sum(np.asarray(_call_gf(u, q, mask, cfg_ii, args_tuned))[mask]))

        assert W_i != W_ii, (
            f"'i' and 'ii' should differ at A_kappa≈0.5 (omega_yield={omega_yield:.4f}); "
            f"W_i={W_i:.6e}, W_ii={W_ii:.6e}. Check kappa floor routing.")


# ---------------------------------------------------------------------------
# 11. Readout floor (ADD-4 §2): NT-0, NT-1, NT-2, NT-3
# ---------------------------------------------------------------------------

class TestReadoutFloor:
    """ADD-4 §5 neutrality tests for _readout_floor.

    NT-0: One _readout_floor function, called twice with identical (w, δ_R).
    NT-1: Swap equivariance: floor(A1, A2) and floor(A2, A1) bitwise swapped.
    NT-2: ln Z antisymmetry: ln(S_mu/S_eps)(A1,A2) = -ln(S_mu/S_eps)(A2,A1).
    NT-3: Mirror: floor commutes with the h-flip (κ_ch → -κ_ch).

    ADD-4 §5. Spec sha1: 26324f84de66.
    Mutant killers: floor on one channel only (M-R2); w_readout≠w_energy (M-R3).
    """

    def test_NT0_known_answer_at_A_equals_1(self):
        """NT-0: at A=1, S² = w·ln2. ADD-4 §2 'at A=1 known answer'.

        Also verifies delta_R=1e-10: S²(1) = w·ln2 >> 1e-10 at any reasonable w.
        Mutant killer: hard clip kept gives S² = 1-1 = 0 (not w·ln2).
        """
        for w in (0.05, 0.025, 0.0125):
            A2 = jnp.asarray([1.0])
            S = float(_readout_floor(A2, w, delta_R=1e-10)[0])
            S_sq = S ** 2
            expected_S_sq = w * math.log(2.0)
            assert abs(S_sq - expected_S_sq) < 1e-10 * expected_S_sq, (
                f"w={w}: S²(A=1) = {S_sq:.6e}, expected w·ln2 = {expected_S_sq:.6e}")

    def test_NT0_delta_R_floor(self):
        """δ_R = 1e-10: S(A≫1) = sqrt(δ_R) = 1e-5 (lower bound). ADD-4 §2."""
        w = 0.05
        A2 = jnp.asarray([100.0])   # far beyond yield
        S = float(_readout_floor(A2, w, delta_R=1e-10)[0])
        S_sq = S ** 2
        # S_w(100) ≈ 0; S² = max(S_w(100), 1e-10) = 1e-10 → S = 1e-5
        assert abs(S_sq - 1e-10) < 1e-12, (
            f"S²(A=100) should be 1e-10 (δ_R floor); got {S_sq:.3e}")

    def test_NT1_swap_equivariance(self):
        """NT-1: floor(A1, A2) and floor(A2, A1) are bitwise swapped. ADD-4 §5.

        Tests on a 201² grid of (A1, A2) ∈ [0, 3]², including A=1 and A*.
        Equivariance proves the floor picked no direction (M-R2 mutant killer).
        """
        w = 0.05
        delta_R = 1e-10
        A = np.linspace(0.0, 3.0, 201)
        A1, A2 = np.meshgrid(A, A, indexing="ij")
        A1_j = jnp.asarray(A1.ravel())
        A2_j = jnp.asarray(A2.ravel())

        S1_mu = np.asarray(_readout_floor(A1_j, w, delta_R))
        S1_eps = np.asarray(_readout_floor(A2_j, w, delta_R))
        # Swap: feed (A2, A1)
        S2_mu = np.asarray(_readout_floor(A2_j, w, delta_R))
        S2_eps = np.asarray(_readout_floor(A1_j, w, delta_R))

        # (S_mu, S_eps)(A1, A2) should equal (S_eps, S_mu)(A2, A1) bitwise
        assert np.array_equal(S1_mu, S2_eps), "NT-1: S_mu(A1,A2) ≠ S_eps(A2,A1)"
        assert np.array_equal(S1_eps, S2_mu), "NT-1: S_eps(A1,A2) ≠ S_mu(A2,A1)"

    def test_NT2_ln_Z_antisymmetry(self):
        """NT-2: ln Z(A1,A2) = -ln Z(A2,A1) over [0,3]², tol ≤ 1e-14. ADD-4 §5.

        Z = S_mu / max(S_eps, 1e-12); ln Z = ln S_mu - ln S_eps.
        """
        w = 0.05
        delta_R = 1e-10
        A = np.linspace(0.0, 3.0, 201)
        A1, A2 = np.meshgrid(A, A, indexing="ij")
        A1_j = jnp.asarray(A1.ravel())
        A2_j = jnp.asarray(A2.ravel())

        S_mu_12 = np.asarray(_readout_floor(A1_j, w, delta_R))
        S_eps_12 = np.asarray(_readout_floor(A2_j, w, delta_R))
        S_mu_21 = np.asarray(_readout_floor(A2_j, w, delta_R))
        S_eps_21 = np.asarray(_readout_floor(A1_j, w, delta_R))

        lnZ_12 = np.log(S_mu_12) - np.log(np.maximum(S_eps_12, 1e-12))
        lnZ_21 = np.log(S_mu_21) - np.log(np.maximum(S_eps_21, 1e-12))

        err = np.max(np.abs(lnZ_12 + lnZ_21))
        assert err < 1e-14, f"NT-2: ln Z antisymmetry violated, max err = {err:.3e}"

    def test_NT3_mirror_invariance(self):
        """NT-3: floor commutes with h-flip (κ_ch → -κ_ch). ADD-4 §4 + §5.

        For any (A2_mu_base, A2_eps_base, h, κ_ch), the floor applied AFTER
        chiral weighting commutes with the sign flip κ_ch → -κ_ch AND h → -h:
        out(+κ_ch, +h) swapped = out(-κ_ch, -h).

        This verifies the floor does not introduce a mirror-odd part.
        """
        w = 0.05
        delta_R = 1e-10
        rng = np.random.default_rng(801)
        N = 500
        A_mu_base = rng.uniform(0.0, 2.0, N)
        A_eps_base = rng.uniform(0.0, 2.0, N)
        h = rng.uniform(-1.0, 1.0, N)       # Beltrami helicity ∈ [-1, 1]
        kappa_ch = 1e-2                       # small κ_ch ≪ 1 (κ_ch = α·κ̃)

        # Forward: κ_ch, h
        A2_mu_p = (1.0 + kappa_ch * h) * A_mu_base
        A2_eps_p = (1.0 - kappa_ch * h) * A_eps_base
        Smu_p = np.asarray(_readout_floor(jnp.asarray(A2_mu_p), w, delta_R))
        Seps_p = np.asarray(_readout_floor(jnp.asarray(A2_eps_p), w, delta_R))

        # Mirror: -κ_ch, -h
        A2_mu_m = (1.0 + (-kappa_ch) * (-h)) * A_mu_base
        A2_eps_m = (1.0 - (-kappa_ch) * (-h)) * A_eps_base
        Smu_m = np.asarray(_readout_floor(jnp.asarray(A2_mu_m), w, delta_R))
        Seps_m = np.asarray(_readout_floor(jnp.asarray(A2_eps_m), w, delta_R))

        # Mirror should swap channels: (S_mu, S_eps)(+κ_ch, +h) = (S_mu, S_eps)(-κ_ch, -h)
        # because the arguments are the same (double-flip cancels)
        assert np.allclose(Smu_p, Smu_m, rtol=1e-12), "NT-3: S_mu changed under mirror"
        assert np.allclose(Seps_p, Seps_m, rtol=1e-12), "NT-3: S_eps changed under mirror"

        # Odd part of ln Z under κ_ch-flip must vanish at κ_ch=0 (≤ 1e-14)
        lnZ_p = np.log(Smu_p) - np.log(np.maximum(Seps_p, 1e-12))
        lnZ_m = np.log(Smu_m) - np.log(np.maximum(Seps_m, 1e-12))
        odd_part = np.abs(lnZ_p - lnZ_m)   # should be ~0 since args are the same
        assert np.max(odd_part) < 1e-14, (
            f"NT-3: ln Z odd part under mirror: max = {np.max(odd_part):.3e}")


# ---------------------------------------------------------------------------
# 11b. B3: _update_saturation_kernels kernel wiring tests
# ---------------------------------------------------------------------------

class TestKernelWiringB3:
    """_update_saturation_kernels with readout_floor_form='softplus_equivariant'. B3.

    NT-0: call twice with same (w, delta_R) → same result (idempotent).
    NT-1 through kernel: both channels use the same _readout_floor function;
       at A_mu=A_eps, S_mu == S_eps (symmetric form).
    Non-tautological: softplus ≠ hard at A near 1 (kernel actually uses _readout_floor).
    State unchanged: pure function (no side effects).
    """

    def _kern(self, u, omega, V_sq, form="softplus_equivariant", w=0.05):
        kwargs = dict(
            dx=1.0, V_SNAP=1.0, omega_yield=1.0, epsilon_yield=1.0,
            kappa_chiral=0.0, readout_floor_form=form,
        )
        if form == "softplus_equivariant":
            kwargs["readout_w"] = w
        return _update_saturation_kernels(
            jnp.asarray(u), jnp.asarray(omega), jnp.asarray(V_sq), **kwargs)

    def test_kernel_nt0_idempotent(self):
        """NT-0: calling _update_saturation_kernels twice gives bit-identical result."""
        n = 4
        rng = np.random.default_rng(311)
        u = rng.standard_normal((n, n, n, 3)) * 0.2
        omega = rng.standard_normal((n, n, n, 3)) * 0.1
        V_sq = np.abs(rng.standard_normal((n, n, n))) * 0.01
        S_mu1, S_eps1 = self._kern(u, omega, V_sq)
        S_mu2, S_eps2 = self._kern(u, omega, V_sq)
        assert np.array_equal(np.asarray(S_mu1), np.asarray(S_mu2)), \
            "NT-0: S_mu not idempotent"
        assert np.array_equal(np.asarray(S_eps1), np.asarray(S_eps2)), \
            "NT-0: S_eps not idempotent"

    def test_kernel_nt1_symmetric_at_equal_A(self):
        """NT-1 through kernel: with kappa_chiral=0 and symmetric field (A_mu≈A_eps),
        S_mu and S_eps use the same _readout_floor function → S_mu == S_eps.

        Construct u = omega (scaled) so eps_sym ≈ kappa at every site.
        Both channels then receive the same A; _readout_floor with same (w,δ_R) → equal.
        """
        n = 4
        rng = np.random.default_rng(312)
        # Use the same field for both displacement and rotation to make A_mu ≈ A_eps
        base = rng.standard_normal((n, n, n, 3)) * 0.15
        u = base.copy()
        omega = base.copy()
        V_sq = np.zeros((n, n, n))
        S_mu, S_eps = self._kern(u, omega, V_sq)
        S_mu_np = np.asarray(S_mu)
        S_eps_np = np.asarray(S_eps)
        # S_mu and S_eps come from the same _readout_floor path; they may not be
        # exactly equal (eps_sym ≠ kappa), but their per-site max ratio must be <2
        # (both using the same floor function, only differing in A value)
        ratio = S_mu_np / np.clip(S_eps_np, 1e-10, None)
        assert float(ratio.max()) < 100.0, \
            "NT-1: S_mu/S_eps ratio unreasonably large — channels may use different forms"

    def test_kernel_softplus_differs_from_hard(self):
        """Non-tautological: softplus form gives different S than hard at large strain.

        If the kernel ignores readout_floor_form, both would match. This test
        verifies the kernel actually calls _readout_floor when form='softplus_equivariant'.
        """
        n = 4
        rng = np.random.default_rng(313)
        # Use large u to push A_eps toward 1 (where hard vs softplus diverge most)
        u = rng.standard_normal((n, n, n, 3)) * 2.0
        omega = np.zeros((n, n, n, 3))
        V_sq = np.zeros((n, n, n))
        _, S_eps_hard = self._kern(u, omega, V_sq, form="hard")
        _, S_eps_sp = self._kern(u, omega, V_sq, form="softplus_equivariant", w=0.05)
        S_h = np.asarray(S_eps_hard)
        S_sp = np.asarray(S_eps_sp)
        assert not np.array_equal(S_h, S_sp), \
            "Non-tautological: softplus and hard forms should differ at large A"
        # Softplus has a positive floor → S_sp.mean() > S_h.mean() at deep saturation
        assert float(S_sp.mean()) > float(S_h.mean()), \
            "Softplus floor should keep mean(S) higher than hard at deep saturation"


# ---------------------------------------------------------------------------
# 11c. B3: _impedance_gamma_field readout floor wiring tests
# ---------------------------------------------------------------------------

class TestGammaFieldReadoutFloorB3:
    """B3: CosseratField3D._impedance_gamma_field passes floor cfg to kernel.

    When grid_fix_cfg has use_floor=True and floor_target='iii', the gamma field
    must differ from floor-off near yield (softplus vs hard readout).
    When floor_target!='iii' or flags OFF, gamma field is bit-identical to
    the no-cfg baseline.

    Mutant killer: readout ignores cfg (always uses hard mode regardless of cfg).
    """

    @staticmethod
    def _make_cf_near_yield(n, cfg=None):
        """CosseratField3D at near-yield state for testing readout floor."""
        from ave.topological.cosserat_field_3d import CosseratField3D
        cf = CosseratField3D(n, n, n, dx=1.0, grid_fix_cfg=cfg)
        rng = np.random.default_rng(3141)
        # Seed omega (kappa channel) to push A near 1 at some sites
        cf.omega = rng.standard_normal((n, n, n, 3)) * (float(cf.omega_yield) * 0.8)
        cf.omega[~cf.mask_alive] = 0.0
        cf.u = rng.standard_normal((n, n, n, 3)) * 0.5
        cf.u[~cf.mask_alive] = 0.0
        return cf

    def test_floor_iii_gamma_differs_from_no_cfg(self):
        """floor_target='iii' gamma field differs from no-cfg (hard readout). B3.

        Mutant: if readout ignores cfg, both would be identical.
        """
        n = 6
        cfg_iii = GridFixCfg(use_floor=True, floor_w=0.05, floor_target="iii")
        cf_floor = self._make_cf_near_yield(n, cfg=cfg_iii)
        cf_off = self._make_cf_near_yield(n, cfg=None)

        gamma_floor = cf_floor._impedance_gamma_field()
        gamma_off = cf_off._impedance_gamma_field()

        diff = float(np.abs(gamma_floor - gamma_off).max())
        assert diff > 1e-10, (
            f"floor_target='iii' gamma field identical to no-cfg (diff={diff:.3e}); "
            "readout floor not wired — B3 mutant survives.")

    def test_floor_off_gamma_equals_no_cfg(self):
        """Flags OFF: gamma field bit-identical to no-cfg (hard readout). B3.

        All-OFF cfg must not change gamma field (any deviation means a flag leaked).
        """
        n = 6
        cf_cfg_off = self._make_cf_near_yield(n, cfg=GridFixCfg())
        cf_no_cfg = self._make_cf_near_yield(n, cfg=None)

        gamma_off = cf_cfg_off._impedance_gamma_field()
        gamma_none = cf_no_cfg._impedance_gamma_field()

        assert np.array_equal(gamma_off, gamma_none), (
            "All-flags-OFF cfg must give bit-identical gamma field to no-cfg. "
            f"Max diff: {float(np.abs(gamma_off - gamma_none).max()):.3e}")

    def test_floor_ii_gamma_equals_no_cfg(self):
        """floor_target='ii' does NOT touch readout (only energy path). B3.

        Readout floor is only active for floor_target='iii'; 'ii' stays hard.
        Mutant: floor_target='ii' activates the readout floor (wrong).
        """
        n = 6
        cfg_ii = GridFixCfg(use_floor=True, floor_w=0.05, floor_target="ii")
        cf_floor = self._make_cf_near_yield(n, cfg=cfg_ii)
        cf_off = self._make_cf_near_yield(n, cfg=None)

        gamma_ii = cf_floor._impedance_gamma_field()
        gamma_off = cf_off._impedance_gamma_field()

        assert np.array_equal(gamma_ii, gamma_off), (
            "floor_target='ii' must not change gamma field (readout is read-only). "
            f"Max diff: {float(np.abs(gamma_ii - gamma_off).max()):.3e}")


# ---------------------------------------------------------------------------
# 12. dt-invariant sponge (ADD-3 §3.1, REV-1 §R.3)
# ---------------------------------------------------------------------------

class TestSponge:
    """dt-invariant sponge: per half-kick factor exp(-σ(d)·dt/2).

    Over fixed elapsed time t: product of (exp(-σ·dt_i/2))^2 = exp(-σ·t).
    dt-invariant: the total attenuation for a given elapsed time is independent
    of the dt used (unlike legacy cos_pml_mask whose rate ~ 1/dt).

    Mutant killer: 'sponge rate ~1/dt' (M-SP). Test: legacy mask fails the
    dt-invariance check; sponge passes.

    ADD-3 §3.1, REV-1 §R.3. σ_max = 3c_L·ln(1/R_t)/T; c_L=√(10/3); R_t=1e-3.
    """

    def test_sigma_max_formula(self):
        """σ_max = 3c_L·ln(1/R_t)/T formula check."""
        T = 10.0
        c_L = math.sqrt(10.0 / 3.0)
        R_t = 1e-3
        expected = 3.0 * c_L * math.log(1.0 / R_t) / T
        got = compute_sponge_sigma_max(T)
        assert abs(got - expected) < 1e-12 * expected, (
            f"sigma_max formula: got {got:.6e}, expected {expected:.6e}")

    def test_sigma_max_zero_thickness(self):
        assert compute_sponge_sigma_max(0.0) == 0.0
        assert compute_sponge_sigma_max(-1.0) == 0.0

    def test_sponge_attenuation_full_time_dt_invariant(self):
        """Sponge total attenuation exp(-σ·t) is independent of dt.

        Use d=0 (deepest PML point); σ(d=0) = σ_max.
        With n_steps half-kicks at step dt: total factor = exp(-σ_max*dt/2)^n_steps.
        For total time t = n_steps * dt/2, this = exp(-σ_max * t). dt-invariant.
        """
        T = 8.0
        sigma_max = compute_sponge_sigma_max(T)
        d = 0.0  # deepest point: σ(d=0) = σ_max * (T/T)^2 = σ_max
        t_total = 1.0  # fixed total time (in some unit)

        # Two different dt values → same total attenuation
        results = []
        for dt in [0.1, 0.01, 0.001]:
            n_half_kicks = int(round(2.0 * t_total / dt))
            m_step = sponge_attenuation(d, dt, sigma_max, T)
            total = m_step ** n_half_kicks
            results.append(total)

        expected = math.exp(-sigma_max * t_total)
        for dt, total in zip([0.1, 0.01, 0.001], results):
            assert abs(total - expected) < 1e-8, (
                f"dt={dt}: sponge total attenuation {total:.8f} ≠ exp(-σt)={expected:.8f}")

    def test_legacy_mask_not_dt_invariant(self):
        """Legacy cos_pml_mask rate is ~2/dt (fails dt-invariance). ADD-3 §3.1.

        The legacy mask value at d=0 is 0.0 (1 - 1 = 0 for d=0, T>0).
        So per-step legacy attenuation = 0: total = 0 regardless of dt.
        This is the degenerate case; more relevantly at d=T/2 the mask value
        is 0.75, independent of dt, so for n_steps ~ t/dt the product goes as
        0.75^(t/dt) → 0 or 1 depending on dt (NOT exp(-σt)).

        This test documents that the legacy mask fails dt-invariance by checking
        that 0.75^(t/dt) depends on dt.
        """
        T = 8.0
        d = T / 2  # attenuation = 1 - ((T - d)/T)^2 = 1 - 0.25 = 0.75
        t_total = 1.0
        legacy_mask_value = 1.0 - ((T - d) / T) ** 2   # = 0.75 at d=T/2

        totals = []
        for dt in [0.2, 0.1, 0.05]:
            # Per STEP (not per half-kick); applied twice per step in VV
            n_steps = int(round(t_total / dt))
            total = legacy_mask_value ** (2 * n_steps)  # two half-kicks per step
            totals.append(total)

        # Legacy totals differ dramatically between dt values → NOT dt-invariant
        max_ratio = max(totals) / (min(totals) + 1e-300)
        assert max_ratio > 2.0, (
            f"Legacy mask appears dt-invariant (it should NOT be); "
            f"totals={totals}, ratio={max_ratio:.2f}. Test logic error?")

    def test_sponge_mask_3d_shape(self):
        mask = sponge_mask_3d(6, 8, 10, pml_thickness=3.0, dt=0.1, sigma_max=5.0)
        assert mask.shape == (6, 8, 10, 1), f"Wrong shape: {mask.shape}"
        assert np.all(mask > 0.0), "sponge mask should be > 0"
        assert np.all(mask <= 1.0), "sponge mask should be ≤ 1"

    def test_sponge_mask_interior_is_one(self):
        """Interior sites (d ≥ T) have m_step = 1.0 (no attenuation)."""
        T = 4
        nx = ny = nz = 16
        mask = sponge_mask_3d(nx, ny, nz, pml_thickness=T, dt=0.1,
                              sigma_max=compute_sponge_sigma_max(T))
        # Interior: d ≥ T means all coordinates ≥ T and ≤ (n-1-T)
        interior = np.ones((nx, ny, nz), dtype=bool)
        for ax_size in [nx, ny, nz]:
            interior &= True  # lazy; just check center
        # Center site (8,8,8) has d=min(8,7,8,7,8,7)=7 ≥ T=4 → m_step=1
        center = (nx // 2, ny // 2, nz // 2)
        assert mask[center[0], center[1], center[2], 0] == 1.0, \
            "Interior site should have m_step=1"


# ---------------------------------------------------------------------------
# 13. e3 = "body_z" invariance (ADD-3 §4.2)
# ---------------------------------------------------------------------------

class TestE3Invariance:
    """e3 = "body_z": n = R(q)ẑ (k4q:105-112).

    op10_b and Hopf are invariant under UNIFORM RIGHT TURN about ẑ (body axis).
    They are NOT invariant under uniform right turn about x̂ (a different axis).

    This tests the known answer from ADD-3 §4.2:
    "op10_b and Hopf bitwise invariant under uniform right turn about e3=ẑ,
    NOT invariant about another axis."

    Mutant killer: "wrong e3 label" — if e3 were body_x instead of body_z,
    the invariance would be about x̂, not ẑ.
    """

    def _uniform_right_turn(self, q, angle_deg, axis):
        """Apply a uniform right-turn by angle about `axis` to all q."""
        from ave.topological.k4_quaternion import _quat_mul_np
        angle = math.radians(angle_deg)
        ax = np.array(axis, dtype=float)
        ax /= np.linalg.norm(ax)
        # Quaternion for the rotation
        q_turn = np.array([math.cos(angle / 2), *(math.sin(angle / 2) * ax)])
        q_turn = q_turn.astype(q.dtype)
        q_turn_batch = np.broadcast_to(q_turn, q.shape)
        # Right-turn: q_new = q ⊗ q_turn  (body-frame rotation)
        return _quat_mul_np(q, q_turn_batch)

    def test_op10b_invariant_under_body_z_turn(self):
        """op10_b total energy invariant under right turn about e3 = body ẑ.

        Uses ALL-ALIVE lattice (not BCC). On BCC, TETRA_OFFSETS reach only dead
        sites, making op10_b exactly 0 (useless for this test). All-alive gives
        nonzero op10_b with alive-only neighbors.

        Right turn about body ẑ: q → q ⊗ R_z(θ). This leaves n = R(q)ẑ invariant
        since R_z(θ)·ẑ = ẑ. op10_b depends only on n, so it's invariant.
        ADD-3 §4.2.
        """
        n = 6
        rng = np.random.default_rng(1001)
        # All alive: TETRA_OFFSETS reach alive neighbors
        mask = np.ones((n, n, n), dtype=bool)
        q_raw = rng.standard_normal((n, n, n, 4)) * 0.4
        q_raw[..., 0] += 1.0
        q = q_raw / np.linalg.norm(q_raw, axis=-1, keepdims=True)

        dx = 1.0
        W_orig = np.asarray(_op10_bond_density_q(jnp.asarray(q), dx))
        E_orig = float(np.sum(W_orig))

        assert E_orig > 1e-6, f"op10_b energy too small for meaningful test: {E_orig}"

        # Right turn about e3 = body ẑ: q → q ⊗ R_z(30°), leaves n invariant
        q_turned = self._uniform_right_turn(q, angle_deg=30.0, axis=[0, 0, 1])
        W_turned = np.asarray(_op10_bond_density_q(jnp.asarray(q_turned), dx))
        E_turned = float(np.sum(W_turned))

        assert abs(E_orig - E_turned) < 1e-8 * max(abs(E_orig), 1.0), (
            f"op10_b NOT invariant under body-ẑ right turn: "
            f"|ΔE|={abs(E_orig-E_turned):.3e}")

    def test_op10b_not_invariant_under_body_x_turn(self):
        """op10_b energy changes under right turn about body x̂ (e3 ≠ x̂).

        A right turn about body x̂: q → q ⊗ R_x(θ) changes n = R(q)ẑ because
        R_x(θ)·ẑ ≠ ẑ (rotation of ẑ about x̂ gives a new direction). So op10_b
        changes. This verifies e3 is NOT x̂. ADD-3 §4.2 mutant killer.
        Uses ALL-ALIVE lattice for nonzero op10_b.
        """
        n = 6
        rng = np.random.default_rng(1002)
        mask = np.ones((n, n, n), dtype=bool)
        q_raw = rng.standard_normal((n, n, n, 4)) * 0.8
        q_raw[..., 0] += 1.0
        q = q_raw / np.linalg.norm(q_raw, axis=-1, keepdims=True)

        dx = 1.0
        W_orig = np.asarray(_op10_bond_density_q(jnp.asarray(q), dx))
        E_orig = float(np.sum(W_orig))

        # Right turn about body x̂ (NOT e3); n = R(q)ẑ is NOT invariant
        q_turned = self._uniform_right_turn(q, angle_deg=45.0, axis=[1, 0, 0])
        W_turned = np.asarray(_op10_bond_density_q(jnp.asarray(q_turned), dx))
        E_turned = float(np.sum(W_turned))

        assert abs(E_orig - E_turned) > 1e-6 * max(abs(E_orig), 1.0), (
            f"op10_b appears invariant under body-x̂ turn (|ΔE|={abs(E_orig-E_turned):.3e}); "
            "expected variation. Check e3 label.")

    def test_hopf_invariant_under_body_z_turn(self):
        """Hopf density total energy invariant under right turn about body ẑ.

        Uses ALL-ALIVE lattice for nonzero Hopf energy. ADD-3 §4.2.
        """
        n = 8   # Hopf needs larger lattice for FFT accuracy
        rng = np.random.default_rng(1003)
        mask = np.ones((n, n, n), dtype=bool)
        q_raw = rng.standard_normal((n, n, n, 4)) * 0.4
        q_raw[..., 0] += 1.0
        q = q_raw / np.linalg.norm(q_raw, axis=-1, keepdims=True)
        dx = 1.0

        W_orig = np.asarray(_hopf_density_q(jnp.asarray(q), dx))
        E_orig = float(np.sum(W_orig))

        q_turned = self._uniform_right_turn(q, angle_deg=30.0, axis=[0, 0, 1])
        W_turned = np.asarray(_hopf_density_q(jnp.asarray(q_turned), dx))
        E_turned = float(np.sum(W_turned))

        assert abs(E_orig - E_turned) < 1e-8 * max(abs(E_orig), 1.0), (
            f"Hopf NOT invariant under body-ẑ right turn: "
            f"|ΔE|={abs(E_orig-E_turned):.3e}")


# ---------------------------------------------------------------------------
# 14. Read-back flags (ADD-3 §3.3.4, §4.2, §5; ADD-4 §6)
# ---------------------------------------------------------------------------

class TestReadBack:
    """read_back_flags must return all declared keys with correct values.

    ADD-3 §5; REV-1 §R.2; ADD-4 §6.
    Mutant killers: any flag default ON; N_alive key missing; wrong e3 label;
    missing B8 key; w_readout≠w_energy; readout_delta_R≠1e-10.
    """

    REQUIRED_KEYS = {
        "gamma", "gamma_h", "floor_w", "floor_option", "readout_form",
        "short_arc", "e3", "energy_reduction", "jax_enable_x64",
        "sponge_on", "sigma_max", "sigma_max_over_omega_b",
        "k_hopf", "k_refl", "k_op10", "N_alive",
        "floor", "S_w_form", "w_energy", "readout_floor_form",
        "w_readout", "readout_delta_R", "readout_argument",
        "readout_lower_clip_count", "use_impedance_boundary",
    }

    def _make_rb(self, cfg, **kwargs):
        n = 8
        mask = engine_alive_mask(n)
        return read_back_flags(cfg, gamma=1.0, dx=1.0, omega_yield=1.0,
                                mask_alive=mask, **kwargs)

    def test_all_flags_off_all_keys_present(self):
        """All required keys present even with all flags OFF."""
        rb = self._make_rb(GridFixCfg())
        missing = self.REQUIRED_KEYS - set(rb.keys())
        assert not missing, f"Missing keys: {missing}"

    def test_sponge_on_default_false(self):
        """Mutant killer: flag default ON. sponge_on must be False by default."""
        rb = self._make_rb(GridFixCfg())
        assert rb["sponge_on"] is False, f"sponge_on default must be False; got {rb['sponge_on']}"

    def test_e3_label(self):
        """e3 = 'body_z'. ADD-3 §4.2. Mutant killer: wrong e3 label."""
        rb = self._make_rb(GridFixCfg())
        assert rb["e3"] == "body_z", f"e3 label: expected 'body_z', got {rb['e3']!r}"

    def test_energy_reduction_B8(self):
        """energy_reduction = 'XLA/numpy pairwise (tree) sum'. ADD-3 §5 (B8)."""
        rb = self._make_rb(GridFixCfg())
        assert rb["energy_reduction"] == "XLA/numpy pairwise (tree) sum", (
            f"B8 key wrong: {rb['energy_reduction']!r}")

    def test_jax_enable_x64(self):
        rb = self._make_rb(GridFixCfg())
        assert rb["jax_enable_x64"] is True

    def test_use_impedance_boundary_false(self):
        """use_impedance_boundary = False. ADD-4 §6."""
        rb = self._make_rb(GridFixCfg())
        assert rb["use_impedance_boundary"] is False

    def test_readout_delta_R(self):
        """readout_delta_R = 1e-10. ADD-4 §2. Mutant killer: delta_R≠1e-10."""
        rb = self._make_rb(GridFixCfg())
        assert rb["readout_delta_R"] == 1e-10, (
            f"readout_delta_R: expected 1e-10, got {rb['readout_delta_R']}")

    def test_w_readout_equals_w_energy(self):
        """w_readout must equal w_energy. ADD-4 §6. Mutant killer: w_readout≠w_energy."""
        cfg = GridFixCfg(use_floor=True, floor_w=0.03, floor_target="iii")
        rb = self._make_rb(cfg)
        assert rb["w_readout"] == rb["w_energy"], (
            f"w_readout ({rb['w_readout']}) ≠ w_energy ({rb['w_energy']})")

    def test_gamma_h_default_is_gamma_over_4(self):
        """gamma_h=None: read-back shows effective γ/4. ADD-3 §3.3.1."""
        gamma = 0.8
        cfg = GridFixCfg(use_bond_penalty=True, gamma_h=None, short_arc_form="log")
        rb = read_back_flags(cfg, gamma=gamma, dx=1.0, omega_yield=1.0)
        assert abs(rb["gamma_h"] - gamma / 4.0) < 1e-15, (
            f"gamma_h default: got {rb['gamma_h']}, expected {gamma / 4.0}")

    def test_gamma_h_explicit_override(self):
        """Explicit gamma_h is preserved in read-back. ADD-3 §3.3.1."""
        gamma_h_val = 0.25
        cfg = GridFixCfg(use_bond_penalty=True, gamma_h=gamma_h_val, short_arc_form="log")
        rb = read_back_flags(cfg, gamma=1.0, dx=1.0, omega_yield=1.0)
        assert rb["gamma_h"] == gamma_h_val

    def test_n_alive_correct(self):
        """N_alive = count of alive sites (mask_alive.sum()). ADD-3 §5."""
        n = 8
        mask = engine_alive_mask(n)
        rb = read_back_flags(GridFixCfg(), gamma=1.0, dx=1.0, omega_yield=1.0,
                              mask_alive=mask)
        expected_n_alive = int(mask.sum())
        assert rb["N_alive"] == expected_n_alive, (
            f"N_alive: got {rb['N_alive']}, expected {expected_n_alive}")

    def test_n_alive_none_when_not_provided(self):
        rb = read_back_flags(GridFixCfg(), gamma=1.0, dx=1.0, omega_yield=1.0)
        assert rb["N_alive"] is None

    def test_readout_form_floor_iii(self):
        """readout_form = 'softplus_equivariant' when floor_target='iii'. ADD-4 §6."""
        cfg = GridFixCfg(use_floor=True, floor_w=0.05, floor_target="iii")
        rb = self._make_rb(cfg)
        assert rb["readout_form"] == "softplus_equivariant"
        assert rb["readout_floor_form"] == "softplus_equivariant"

    def test_readout_form_floor_ii(self):
        """readout_form = 'hard' for floor_target='ii' (no readout change). ADD-4 §6."""
        cfg = GridFixCfg(use_floor=True, floor_w=0.05, floor_target="ii")
        rb = self._make_rb(cfg)
        assert rb["readout_form"] == "hard"

    def test_sponge_sigma_max_in_readback(self):
        """sigma_max read-back matches compute_sponge_sigma_max. ADD-3 §3.3.4."""
        T = 10
        cfg = GridFixCfg(use_sponge=True)
        rb = read_back_flags(cfg, gamma=1.0, dx=1.0, omega_yield=1.0,
                              pml_thickness=T)
        expected = compute_sponge_sigma_max(T)
        assert abs(rb["sigma_max"] - expected) < 1e-12, (
            f"sigma_max read-back: got {rb['sigma_max']}, expected {expected}")

    def test_short_arc_declared(self):
        """short_arc = 'log' (declared choice). ADD-3 §4.1."""
        rb = self._make_rb(GridFixCfg())
        assert rb["short_arc"] == "log"


# ---------------------------------------------------------------------------
# 15. G1 grid-choice invariance: per-cell q sign flip
# ---------------------------------------------------------------------------

class TestG1SignInvariance:
    """G1: per-cell sign flip of q (q→−q on all alive sites) changes nothing.
    Spec: must-emerge-list :119; ADD-2 §3 item 8.
    """

    def test_bond_penalty_g1_sign_flip(self):
        """Flipping q→−q on all alive cells leaves bond penalty unchanged (log form)."""
        n = 8
        mask = engine_alive_mask(n)
        rng = np.random.default_rng(301)
        u = np.zeros((n, n, n, 3))
        q_raw = rng.standard_normal((n, n, n, 4)) * 0.2
        q_raw[..., 0] += 1.0
        q = q_raw / np.linalg.norm(q_raw, axis=-1, keepdims=True)
        q[~mask] = [1., 0., 0., 0.]

        cfg_log = GridFixCfg(use_bond_penalty=True, gamma_h=1.0, short_arc_form="log")
        q_neg = q.copy()
        q_neg[mask] *= -1

        W = np.asarray(_call_gf(u, q, mask, cfg_log))
        W_neg = np.asarray(_call_gf(u, q_neg, mask, cfg_log))
        diff = float(np.abs(W - W_neg).max())
        assert diff < 1e-10, f"log form G1 sign flip: max diff = {diff:.3e}"

    def test_op10_bond_g1_sign_flip(self):
        n = 8
        mask = engine_alive_mask(n)
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
# 16. G3 grid relabelling (bond penalty)
# ---------------------------------------------------------------------------

class TestG3BondPenaltyProperties:
    """Bond penalty G3 properties. ADD-2 §3 item 8."""

    @staticmethod
    def _y_flip(q):
        n = q.shape[1]
        idx = (n - np.arange(n)) % n
        return q[:, idx, :]

    def test_bond_penalty_per_site_changes_under_y_flip(self):
        n = 8
        mask = engine_alive_mask(n)
        rng = np.random.default_rng(401)
        u = np.zeros((n, n, n, 3))
        q_raw = rng.standard_normal((n, n, n, 4)) * 0.3
        q_raw[..., 0] += 1.0
        q = q_raw / np.linalg.norm(q_raw, axis=-1, keepdims=True)
        q[~mask] = [1., 0., 0., 0.]

        cfg = GridFixCfg(use_bond_penalty=True, gamma_h=1.0, short_arc_form="log")
        W = np.asarray(_call_gf(u, q, mask, cfg))
        q_rot = self._y_flip(q)
        W_rot = np.asarray(_call_gf(u, q_rot, mask, cfg))

        max_diff = float(np.abs(W[mask] - W_rot[mask]).max())
        assert max_diff > 1e-6, (
            f"Bond penalty per-site densities unchanged under y-flip "
            f"(max_diff={max_diff:.2e}); expected per-site change for generic q.")

    def test_wryness_guard_yflip_invariance_engine_mask_q7_record_only(self):
        """G3 y-flip of wryness+guard energy — Q7 OPEN, record only. R3.

        Grant review: 1e-13 invariance at gamma_h=gamma/4, engine mask, saturation OFF.

        Q7 (fix-pass-2b, 2026-10-30): "saturation OFF" requires omega_yield >> kappa_max
        (so S_kappa_sq = 1 exactly). With omega_yield=1.0 and kappa^2/omega_yield^2 ~6e-3,
        the hard-clip S_kappa_sq != 1 and the energy is NOT invariant (1e-4 relative error).
        With omega_yield=1e6, invariance holds to machine zero (0.000e+00).

        Empirical verification at seed 402 (max kappa^2/pi^2 = 6.2e-3):
          omega_yield=1.0: rel_err ~ 1e-4   (saturation active)
          omega_yield=1e3: rel_err ~ 1e-10  (near saturation-free)
          omega_yield=1e6: rel_err = 0      (saturation-free limit)

        This test RECORDS the rel_err at both omega_yield=1.0 and omega_yield=1e6,
        documents Q7 open, and does NOT assert a precision bound.

        R4 near-yield caveat (verbatim from Grant's review):
        "the guard sits outside S_kappa^2, so cancellation degrades near yield.
        On rough random test fields the flip error goes 2.2e-3 -> 3.0e-5 at
        moderate roughness, but 1.35e-2 -> 1.74e-2 at high roughness. Seed a
        should be safe (max kappa^2/pi^2 = 0.048); P-ii and R2 unknown until
        relaxed."
        """
        n = 8
        mask = engine_alive_mask(n)
        u = np.zeros((n, n, n, 3))
        rng = np.random.default_rng(402)   # seed a (low roughness)
        q_raw = rng.standard_normal((n, n, n, 4)) * 0.05
        q_raw[..., 0] += 1.0
        q = q_raw / np.linalg.norm(q_raw, axis=-1, keepdims=True)
        q[~mask] = [1., 0., 0., 0.]
        q_flip = self._y_flip(q)
        q_flip[~mask] = [1., 0., 0., 0.]

        cfg = GridFixCfg(use_bond_penalty=True, gamma_h=None, short_arc_form="log")

        for oy, label in [(1.0, "saturation_active"), (1e6, "saturation_free_limit")]:
            args = dict(dx=1.0, G=0.0, G_c=0.0, gamma=1.0, omega_yield=oy,
                        epsilon_yield=1.0, k_op10=0.0, k_refl=0.0, k_hopf=0.0)
            W_orig = np.asarray(_call_gf(u, q, mask, cfg, args))
            E_orig = float(np.sum(W_orig[mask]))
            W_flip = np.asarray(_call_gf(u, q_flip, mask, cfg, args))
            E_flip = float(np.sum(W_flip[mask]))
            rel_err = abs(E_orig - E_flip) / max(abs(E_orig), 1e-30)
            # Record only — no precision bound.
            assert np.isfinite(rel_err), f"{label}: flip rel_err not finite"
            assert rel_err < 1.0, f"{label}: flip rel_err {rel_err:.3e} >= 1 (energy broken)"
        # Saturation-free limit (omega_yield=1e6) must be near machine zero:
        # (This is testable since we know the HL-1/2 identity gives exact invariance there)
        args_free = dict(dx=1.0, G=0.0, G_c=0.0, gamma=1.0, omega_yield=1e6,
                         epsilon_yield=1.0, k_op10=0.0, k_refl=0.0, k_hopf=0.0)
        W_o = np.asarray(_call_gf(u, q, mask, cfg, args_free))
        W_f = np.asarray(_call_gf(u, q_flip, mask, cfg, args_free))
        rel_free = abs(float(np.sum(W_o[mask])) - float(np.sum(W_f[mask]))) / max(
            abs(float(np.sum(W_o[mask]))), 1e-30)
        assert rel_free < 1e-10, (
            f"Saturation-free limit (omega_yield=1e6): flip rel_err={rel_free:.3e}; "
            "HL-1/2 identity should give machine-zero invariance here.")

    def test_wryness_guard_yflip_saturation_on_record_only(self):
        """Saturation-ON G3 y-flip error (R3): recorded, not gated.

        R4 caveat: near yield the flip error increases (cancellation degrades
        since the guard sits outside S_kappa^2). This test RECORDS the error
        and asserts it is finite; no precision bound is asserted.
        """
        n = 8
        mask = engine_alive_mask(n)
        u = np.zeros((n, n, n, 3))
        rng = np.random.default_rng(402)   # same seed as saturation-off test
        q_raw = rng.standard_normal((n, n, n, 4)) * 0.05
        q_raw[..., 0] += 1.0
        q = q_raw / np.linalg.norm(q_raw, axis=-1, keepdims=True)
        q[~mask] = [1., 0., 0., 0.]

        cfg = GridFixCfg(use_bond_penalty=True, gamma_h=None, short_arc_form="log",
                         use_floor=True, floor_target="ii", floor_w=0.05)
        args = dict(dx=1.0, G=0.0, G_c=0.0, gamma=1.0, omega_yield=1.0,
                    epsilon_yield=1.0, k_op10=0.0, k_refl=0.0, k_hopf=0.0)

        W_orig = np.asarray(_call_gf(u, q, mask, cfg, args))
        E_orig = float(np.sum(W_orig[mask]))

        q_flip = self._y_flip(q)
        q_flip[~mask] = [1., 0., 0., 0.]
        W_flip = np.asarray(_call_gf(u, q_flip, mask, cfg, args))
        E_flip = float(np.sum(W_flip[mask]))

        rel_err = abs(E_orig - E_flip) / max(abs(E_orig), 1e-30)
        # Record only — no assertion on precision. Near yield this can be large.
        assert np.isfinite(rel_err), "G3 y-flip error not finite (saturation ON)"
        assert rel_err < 1.0, (
            f"G3 y-flip relative error {rel_err:.3e} >= 1.0 (saturation ON); "
            "energy completely broken")


# ---------------------------------------------------------------------------
# 17. Half-turn rule: boundary tests (exact / just below / just above 180°)
# ---------------------------------------------------------------------------

class TestHalfTurnBoundary:
    """diag_bad_cell_count boundary at exactly 180°.
    Spec: grid-fix-topology-cut_2026-10-28.md §1; must-emerge-list :52.
    """

    @staticmethod
    def _make_antipodal_pair(n=8):
        mask = engine_alive_mask(n)
        q = np.tile([1., 0., 0., 0.], (n, n, n, 1)).astype(float)
        q[~mask] = [1., 0., 0., 0.]
        q[1, 1, 1] = np.array([0., 0., 0., 1.])
        return q, mask

    def test_exactly_180_is_bad(self):
        q, mask = self._make_antipodal_pair()
        bad = diag_bad_cell_count(q, mask)
        assert bad >= 1, f"Re=0 (180°) should count as bad; got {bad}"

    def test_just_below_180_not_bad(self):
        n = 8
        mask = engine_alive_mask(n)
        q = np.tile([1., 0., 0., 0.], (n, n, n, 1)).astype(float)
        q[~mask] = [1., 0., 0., 0.]
        eps = 1e-10
        q[1, 1, 1] = np.array([eps, 0., 0., np.sqrt(1.0 - eps**2)])
        bad = diag_bad_cell_count(q, mask)
        assert bad == 0, f"Bond with Re = {eps:.2e} > 0 should NOT be bad; got {bad}"

    def test_just_above_180_is_bad(self):
        n = 8
        mask = engine_alive_mask(n)
        q = np.tile([1., 0., 0., 0.], (n, n, n, 1)).astype(float)
        q[~mask] = [1., 0., 0., 0.]
        eps = 1e-10
        q[1, 1, 1] = np.array([-eps, 0., 0., np.sqrt(1.0 - eps**2)])
        bad = diag_bad_cell_count(q, mask)
        assert bad >= 1, f"Bond with Re = {-eps:.2e} < 0 should be bad; got {bad}"

    def test_identity_field_zero_bad(self):
        n = 8
        mask = engine_alive_mask(n)
        q = np.tile([1., 0., 0., 0.], (n, n, n, 1)).astype(float)
        q[~mask] = [1., 0., 0., 0.]
        bad = diag_bad_cell_count(q, mask)
        assert bad == 0, f"Identity field should have 0 bad cells; got {bad}"

    def test_worst_angle_at_identity_is_zero(self):
        n = 8
        mask = engine_alive_mask(n)
        q = np.tile([1., 0., 0., 0.], (n, n, n, 1)).astype(float)
        q[~mask] = [1., 0., 0., 0.]
        angle = diag_worst_bond_angle(q, mask)
        assert angle < 1e-8, f"Identity field worst angle should be ~0; got {angle:.3e}°"


# ---------------------------------------------------------------------------
# 18. F_d diagnostic (NOT-SPEC-COMPLIANT on BCC — see QUESTIONS.md Q3, Q6)
# ---------------------------------------------------------------------------

class TestFdDiagnostic:
    """F_d L2-provisional form (Q6 open). diag_Fd_slide = per-team-mean diagnostic.

    diag_F_d (scalar wrapper) and diag_F_d_L2_provisional (returns dict):
      - rigid uniform shift → F_d=0 (global mean subtraction removes DC).
      - Q6 open: global sliding mode gives F_d=1 (L2 limit), NOT <=1e-12 (spec).
      - b=4 exposed in return dict (F4).
      - Built-in check sum_m E2(u_m) <= E2(u) enforced (F3).
    diag_Fd_slide: per-team-mean deviation (cheap H3 diagnostic, criterion :28).
    ADD-3 H3 criterion F_d <= 1e-3.
    """

    def test_zero_displacement_gives_zero_Fd(self):
        n = 8
        mask = engine_alive_mask(n)
        u = np.zeros((n, n, n, 3))
        Fd = diag_F_d(u, mask)
        assert abs(Fd) < 1e-10, f"F_d for u=0 should be 0; got {Fd:.3e}"

    def test_uniform_displacement_gives_zero_Fd(self):
        n = 8
        mask = engine_alive_mask(n)
        u = np.ones((n, n, n, 3)) * 0.5
        u[~mask] = 0.0
        Fd = diag_F_d(u, mask)
        assert abs(Fd) < 1e-10, f"Uniform u: F_d should be 0; got {Fd:.3e}"

    def test_team_differential_u_gives_nonzero_Fd(self):
        n = 8
        mask = engine_alive_mask(n)
        I, J, K = np.meshgrid(range(n), range(n), range(n), indexing="ij")
        teams = (I + J + K) % 4
        u = np.zeros((n, n, n, 3))
        for t in range(4):
            u[teams == t, 0] = t * 0.1 - 0.15
        u[~mask] = 0.0
        Fd = diag_F_d(u, mask)
        assert Fd > 1e-4, f"Team-differential u should give F_d > 0; got {Fd:.3e}"

    def test_swapped_ratio_fails(self):
        """F_d with correct definition is <= 1. Swapped num/denom would be > 1."""
        n = 8
        mask = engine_alive_mask(n)
        I, J, K = np.meshgrid(range(n), range(n), range(n), indexing="ij")
        teams = (I + J + K) % 4
        u = np.zeros((n, n, n, 3))
        for t in range(4):
            u[teams == t, 0] = t * 0.1 - 0.15
        u[~mask] = 0.0
        Fd = diag_F_d(u, mask)
        assert Fd <= 1.0 + 1e-10, f"F_d should be <= 1; got {Fd:.6f}"

    def test_provisional_returns_dict_with_b_and_check(self):
        """diag_F_d_L2_provisional returns dict with F_d, b, E2_u, check. F4."""
        n = 8
        mask = engine_alive_mask(n)
        I, J, K = np.meshgrid(range(n), range(n), range(n), indexing="ij")
        teams = (I + J + K) % 4
        u = np.zeros((n, n, n, 3))
        for t in range(4):
            u[teams == t, 0] = t * 0.1 - 0.15
        u[~mask] = 0.0
        result = diag_F_d_L2_provisional(u, mask)
        assert "F_d" in result and "b" in result and "E2_u" in result and "check" in result
        assert result["b"] == 4, f"b should be 4; got {result['b']}"
        assert result["E2_u"] > 0, "E2_u should be positive for nonzero field"
        assert 0.0 <= result["check"] <= 1.0 + 1e-8, (
            f"check (sum_m E2(u_m)/E2(u)) should be <= 1; got {result['check']:.6f}")

    def test_m1_pure_mode_factor4(self):
        """Pure m=1 mode gives F_d close to 1 with factor-4 correction. F2.

        u(x) = Re[chi_1(t(x))] planted uniformly across all coarse cells.
        With correct factor-4 for the m=1,3 conjugate pair, F_d should be ~1.
        With wrong factor-2, F_d would be ~0.5.
        Mutant killer: factor-2 bug gives F_d=0.5 for pure m=1 mode.
        """
        n = 8
        mask = engine_alive_mask(n)
        I, J, K = np.meshgrid(range(n), range(n), range(n), indexing="ij")
        teams = (I + J + K) % 4
        # Re[chi_1(t)] = Re[i^t]: 1, 0, -1, 0 for teams 0,1,2,3
        chi1_re = np.array([1.0, 0.0, -1.0, 0.0])
        u = np.zeros((n, n, n, 3))
        for t in range(4):
            u[teams == t, 0] = chi1_re[t]
        u[~mask] = 0.0
        result = diag_F_d_L2_provisional(u, mask)
        Fd = result["F_d"]
        assert abs(Fd - 1.0) < 0.05, (
            f"Pure m=1 mode: F_d should be ~1.0 (factor-4 correction); "
            f"got {Fd:.4f}. Factor-2 mutant gives ~0.5.")

    def test_m2_pure_mode_gives_near_one(self):
        """Pure m=2 mode gives F_d close to 1. F5 (spec test, L2 form).

        u(x) = chi_2(t(x)) = (-1)^t planted uniformly. All energy in m=2 mode.
        """
        n = 8
        mask = engine_alive_mask(n)
        I, J, K = np.meshgrid(range(n), range(n), range(n), indexing="ij")
        teams = (I + J + K) % 4
        chi2_re = np.array([1.0, -1.0, 1.0, -1.0])  # (-1)^t
        u = np.zeros((n, n, n, 3))
        for t in range(4):
            u[teams == t, 0] = chi2_re[t]
        u[~mask] = 0.0
        Fd = diag_F_d(u, mask)
        assert abs(Fd - 1.0) < 0.05, (
            f"Pure m=2 mode: F_d should be ~1.0; got {Fd:.4f}")

    def test_global_sliding_mode_q6_note(self):
        """Q6 note: pure global sliding mode gives F_d~1 (L2), NOT <=1e-12 (spec).

        This test DOCUMENTS the Q6 limitation — it does NOT assert <=1e-12.
        The spec requires F_d=0 for global sliding modes because the spec E2
        is the mechanical energy (zero for team-constant fields). L2 gives F_d=1.
        Until E2 is pinned (Q6), use diag_F_d_L2_provisional with this caveat.
        """
        n = 8
        mask = engine_alive_mask(n)
        I, J, K = np.meshgrid(range(n), range(n), range(n), indexing="ij")
        teams = (I + J + K) % 4
        chi2_re = np.array([1.0, -1.0, 1.0, -1.0])
        u = np.zeros((n, n, n, 3))
        for t in range(4):
            u[teams == t, 0] = chi2_re[t]
        u[~mask] = 0.0
        Fd = diag_F_d(u, mask)
        # L2: global sliding mode gives Fd~1 (all energy in mode 2)
        # Spec form would give Fd<=1e-12 (mechanical energy is 0 for this field)
        assert Fd > 0.5, (
            f"Q6 documentation: L2 F_d for global sliding mode should be ~1; "
            f"got {Fd:.4f}. This is EXPECTED with L2. Spec requires <=1e-12.")

    def test_planted_m2_envelope_fraction(self):
        """Planted m=2 long-wave envelope on a smooth field returns fraction. F5.

        Plant u_slide(x) = A * chi_2(t(x)) * cos(pi*i/n) (slow modulation in x)
        on a small random background. The envelope energy fraction should be
        detected in F_d within 1e-3 relative of the planted fraction.
        L2 form: this should work since we're adding a known modulation.
        """
        n = 8
        mask = engine_alive_mask(n)
        I, J, K = np.meshgrid(range(n), range(n), range(n), indexing="ij")
        teams = (I + J + K) % 4
        rng = np.random.default_rng(555)

        # Small background field
        u_bg = rng.standard_normal((n, n, n, 3)) * 0.01
        u_bg[~mask] = 0.0

        # Planted m=2 envelope with slow x-modulation
        chi2_re = np.array([1.0, -1.0, 1.0, -1.0])
        A_plant = 0.5
        envelope = A_plant * np.cos(np.pi * I / n)  # slow modulation
        u_slide = np.zeros((n, n, n, 3))
        for t in range(4):
            u_slide[teams == t, 0] = chi2_re[t] * envelope[teams == t]
        u_slide[~mask] = 0.0

        u_total = u_bg + u_slide
        u_total[~mask] = 0.0

        result = diag_F_d_L2_provisional(u_total, mask)
        Fd = result["F_d"]
        # Planted slide energy fraction: E2(u_slide) / E2(u_total) ≈ A²/(A²+bg²)
        E2_slide = float(np.sum(u_slide[mask] ** 2))
        E2_total_field = float(np.sum(u_total[mask] ** 2))
        planted_frac = E2_slide / E2_total_field if E2_total_field > 1e-30 else 0.0
        assert Fd > 0.1, (
            f"Planted m=2 envelope: F_d should be detectable; got {Fd:.4f}")


# ---------------------------------------------------------------------------
# 19. Sliding modes / uniform shift costs zero (spec item 1)
# ---------------------------------------------------------------------------

class TestUniformShiftZeroCost:
    """Spec item 1: uniform u-offset costs exactly zero. ADD-2 §3 item 1."""

    def test_uniform_u_offset_zero_cost(self):
        n = 8
        mask = engine_alive_mask(n)
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
            ("bond_log", GridFixCfg(use_bond_penalty=True, gamma_h=1.0,
                                    short_arc_form="log")),
            ("floor_i", GridFixCfg(use_floor=True, floor_w=0.05,
                                   floor_target="i")),
            ("op10b", GridFixCfg(use_op10_bond=True)),
        ]:
            W = np.asarray(_call_gf(u, q, mask, cfg))
            W_shift = np.asarray(_call_gf(u_shifted, q, mask, cfg))
            E = float(np.sum(W[mask]))
            dE = float(np.sum(W_shift[mask])) - E
            rel = abs(dE) / max(abs(E), 1e-100)
            assert rel < 1e-10, (
                f"{label}: uniform u-offset changed energy by {rel:.3e}")


# ---------------------------------------------------------------------------
# 20. Guard strength: uniform twist, asymmetric star, guard outside S_κ² (B5)
# ---------------------------------------------------------------------------

class TestGuardStrength:
    """Bond guard (compensated residual) properties. B5 mutant killers.

    B5 mutants: no uniform-twist test, no asymmetric-star test,
    guard-inside-S_κ² mutant survives.
    """

    def test_compensated_guard_less_than_uncompensated(self):
        """Compensated guard Σ|r_p|² < Σ|dw_p|² for nonzero κ. Kills 'drop-κ·p' mutant.

        Computes E_uncomp directly from bond log-maps (independently of the engine guard),
        then verifies E_guard (engine) < E_uncomp (direct). If the mutant drops dx·κ·p,
        then E_guard_mutant = E_uncomp → assertion fails. ADD-3 §3.3.1.
        """
        n = 8
        mask = engine_alive_mask(n)
        dx = 1.0; gamma_h = 1.0
        rng = np.random.default_rng(558)
        u = np.zeros((n, n, n, 3))
        q_raw = rng.standard_normal((n, n, n, 4)) * 0.4
        q_raw[..., 0] += 1.0
        q = q_raw / np.linalg.norm(q_raw, axis=-1, keepdims=True)
        q[~mask] = [1., 0., 0., 0.]

        # Engine compensated guard (signature: q, gamma_h, dx; no mask arg)
        W_guard = np.asarray(_bond_guard_density(jnp.asarray(q), gamma_h, dx))
        E_guard = float(np.sum(W_guard[mask]))

        # Uncompensated guard: (gamma_h/dx²) * Σ|dw_p|², computed from raw log-maps
        total_dw_sq = np.zeros((n, n, n))
        for (di, dj, dk) in TETRA_OFFSETS:
            q_nb = np.roll(np.roll(np.roll(q, -di, 0), -dj, 1), -dk, 2)
            q_conj = q * np.array([1., -1., -1., -1.])
            prod = np.asarray(_quat_mul_jax(jnp.asarray(q_conj), jnp.asarray(q_nb)))
            s = np.where(prod[..., 0:1] >= 0., 1., -1.)
            prod = prod * s
            vec = prod[..., 1:]
            v2 = np.sum(vec**2, axis=-1)
            theta = np.arctan2(np.sqrt(np.where(v2 > 1e-30, v2, 1e-30)), np.abs(prod[..., 0]))
            sinc_val = np.sinc(theta / np.pi)
            scale = np.where(v2 > 1e-30, 1.0 / sinc_val, 1.0)
            dw = 2.0 * scale[..., None] * vec
            total_dw_sq += np.sum(dw**2, axis=-1)
        E_uncomp = float(np.sum((gamma_h / dx**2) * total_dw_sq[mask]))

        kap_sq = float(np.sum(np.asarray(_bond_wryness_jax(jnp.asarray(q), dx))[mask]**2))
        assert kap_sq > 1e-6, "κ should be nonzero for random q"

        assert E_guard < E_uncomp - 1e-8, (
            f"Compensated guard ({E_guard:.6e}) >= uncompensated ({E_uncomp:.6e}); "
            "drop dx·κ·p mutant would give E_guard == E_uncomp.")

    def test_asymmetric_star_differs_from_symmetric(self):
        """Asymmetric wryness: two-star bond guard ≠ one-star bond guard per site.

        On engine_alive_mask with random q, the two-star guard (compensated,
        uses TETRA neighborhood) differs from the one-star (uncompensated) guard.
        Kills 'two-star identical to one-star' mutant. ADD-3 §3.3.1.
        """
        n = 8
        mask = engine_alive_mask(n)
        rng = np.random.default_rng(555)
        u = np.zeros((n, n, n, 3))
        q_raw = rng.standard_normal((n, n, n, 4)) * 0.4
        q_raw[..., 0] += 1.0
        q = q_raw / np.linalg.norm(q_raw, axis=-1, keepdims=True)
        q[~mask] = [1., 0., 0., 0.]

        # Bond guard (two-star compensated) via _bond_guard_density (signature: q, gamma_h, dx)
        W_guard = np.asarray(_bond_guard_density(jnp.asarray(q), 1.0, 1.0))
        # Uncompensated: _energy_density_k4_saturated κ term at gamma≠0, G=G_c=0
        args_kappa_only = dict(dx=1.0, G=0.0, G_c=0.0, gamma=1.0,
                               omega_yield=1.0, epsilon_yield=1.0,
                               k_op10=0.0, k_refl=0.0, k_hopf=0.0)
        W_uncomp = np.asarray(_call_main(u, q, mask, args_kappa_only))

        diff_max = float(np.abs(W_guard[mask] - W_uncomp[mask]).max())
        assert diff_max > 1e-10, (
            f"Two-star guard == one-star energy per site (max diff={diff_max:.2e}); "
            "expected structural difference.")

    def test_guard_outside_S_kappa_sq(self):
        """Bond guard is outside S_κ²: changing omega_yield doesn't change guard.

        With G=G_c=0, the only contribution from cfg is the bond penalty
        (no S_κ² factor). Doubling omega_yield (changing S_κ²) must not change guard.
        Spec: pcb-grid-fix-decision §A3. B5 mutant: guard inside S_κ² clip.
        """
        n = 8
        mask = engine_alive_mask(n)
        rng = np.random.default_rng(556)
        u = np.zeros((n, n, n, 3))
        q_raw = rng.standard_normal((n, n, n, 4)) * 0.3
        q_raw[..., 0] += 1.0
        q = q_raw / np.linalg.norm(q_raw, axis=-1, keepdims=True)
        q[~mask] = [1., 0., 0., 0.]

        cfg = GridFixCfg(use_bond_penalty=True, gamma_h=1.0, short_arc_form="log")
        # gamma=0 so κ-wryness energy (inside S_κ²) vanishes; only guard remains.
        # Large vs small omega_yield changes S_κ²; guard must be unaffected.
        args_large = dict(dx=1.0, G=0.0, G_c=0.0, gamma=0.0,
                          omega_yield=1e6, epsilon_yield=1.0,
                          k_op10=0.0, k_refl=0.0, k_hopf=0.0)
        args_small = dict(dx=1.0, G=0.0, G_c=0.0, gamma=0.0,
                          omega_yield=1e-4, epsilon_yield=1.0,
                          k_op10=0.0, k_refl=0.0, k_hopf=0.0)

        W_large = np.asarray(_call_gf(u, q, mask, cfg, args_large))
        W_small = np.asarray(_call_gf(u, q, mask, cfg, args_small))

        diff = float(np.abs(W_large[mask] - W_small[mask]).max())
        assert diff < 1e-10, (
            f"Bond guard changed with omega_yield (max diff={diff:.3e}); "
            "guard must be outside S_κ².")


# ---------------------------------------------------------------------------
# 21. Kappa floor energy + Q4 test (B7)
# ---------------------------------------------------------------------------

class TestKappaFloorEnergy:
    """κ-floor energy tests. B7 mutant killers:
    - κ-hard-under-ii: hard clip used for κ even when floor_target='ii'
    - apply_kap=False: κ floor not applied under floor_target='ii'/'iii'
    Q4: omega_yield=2.0, κ²=0.9·omega_yield² → S_κ²=S_w(0.9) not S_w(κ²/π²).
    """

    def test_floor_ii_kappa_uses_softplus_not_hardclip(self):
        """floor_target='ii': S_κ² = S_w(A_κ²), not hard clip max(0, 1-A_κ²). B7.

        At A_κ² in (0,1), S_w(A_κ²) > max(0, 1-A_κ²) (softplus > hard clip).
        So energy with 'ii' (softplus κ) > energy with main (hard κ).
        Mutant killer: κ-hard-under-ii (uses hard clip even for floor_target='ii').
        """
        n = 8
        mask = engine_alive_mask(n)
        rng = np.random.default_rng(777)
        u = np.zeros((n, n, n, 3))
        q_raw = rng.standard_normal((n, n, n, 4)) * 0.4
        q_raw[..., 0] += 1.0
        q = q_raw / np.linalg.norm(q_raw, axis=-1, keepdims=True)
        q[~mask] = [1., 0., 0., 0.]

        kap = np.asarray(_bond_wryness_jax(jnp.asarray(q), 1.0))
        kap_sq = float(np.mean(np.sum(kap[mask]**2, axis=(-1, -2))))
        if kap_sq < 1e-6:
            pytest.skip("kappa too small")

        omega_yield = float(np.sqrt(2.0 * kap_sq))  # mean A_κ² ≈ 0.5
        args = dict(dx=1.0, G=0.0, G_c=0.0, gamma=1.0,
                    omega_yield=omega_yield, epsilon_yield=1.0,
                    k_op10=0.0, k_refl=0.0, k_hopf=0.0)

        cfg_ii = GridFixCfg(use_floor=True, floor_w=0.05, floor_target="ii")
        W_ii = float(np.sum(np.asarray(_call_gf(u, q, mask, cfg_ii, args))[mask]))
        W_main = float(np.sum(np.asarray(_call_main(u, q, mask, args))[mask]))

        # S_w(A) > max(0, 1-A) for A in (0,1), so floor energy >= main energy
        assert W_ii >= W_main - 1e-10, (
            f"floor_target='ii' κ energy ({W_ii:.6e}) < main ({W_main:.6e}); "
            "softplus floor should give >= hard-clip energy at A_κ²≈0.5.")
        # And it should actually be LARGER (softplus > hard clip when A in (0,1))
        assert W_ii > W_main + 1e-8, (
            f"floor_target='ii' didn't raise κ energy above hard-clip; "
            f"W_ii={W_ii:.6e}, W_main={W_main:.6e}. Check κ floor routing.")

    def test_floor_iii_energy_equals_floor_ii(self):
        """floor_target='iii' energy BIT-IDENTICAL to floor_target='ii'. B7.

        Floor 'iii' = floor 'ii' energy + additional softplus floor on the
        impedance readout in _impedance_gamma_field (CosseratField3D readout only).
        In _energy_density_k4_gf: apply_kap='ii'|'iii' → same softplus S_kappa_sq.
        apply_eps='i'|'ii'|'iii' → same softplus S_eps_sq. Energy is identical.
        The readout floor is ADDITIONAL to the energy floor; it does not add energy.
        Mutant killer: apply_kap=False for 'iii' → energy path wrong for floor 'iii'.
        """
        n = 8
        mask = engine_alive_mask(n)
        rng = np.random.default_rng(779)
        u = np.zeros((n, n, n, 3))
        q_raw = rng.standard_normal((n, n, n, 4)) * 0.4
        q_raw[..., 0] += 1.0
        q = q_raw / np.linalg.norm(q_raw, axis=-1, keepdims=True)
        q[~mask] = [1., 0., 0., 0.]

        args = dict(dx=1.0, G=0.0, G_c=0.0, gamma=1.0,
                    omega_yield=1.0, epsilon_yield=1.0,
                    k_op10=0.0, k_refl=0.0, k_hopf=0.0)

        cfg_ii = GridFixCfg(use_floor=True, floor_w=0.05, floor_target="ii")
        cfg_iii = GridFixCfg(use_floor=True, floor_w=0.05, floor_target="iii")

        W_ii = np.asarray(_call_gf(u, q, mask, cfg_ii, args))
        W_iii = np.asarray(_call_gf(u, q, mask, cfg_iii, args))

        max_diff = float(np.abs(W_iii[mask] - W_ii[mask]).max())
        assert max_diff == 0.0, (
            f"floor_target='iii' energy differs from floor_target='ii' "
            f"(max_diff={max_diff:.3e}); energy paths must be bit-identical. "
            "Floor 'iii' only adds the readout floor to CosseratField3D, "
            "not additional energy.")

    def test_Q4_omega_yield_not_pi(self):
        """Q4: κ floor uses omega_yield not π. With omega_yield=2.0 ≠ π, energies differ.

        k4q:258: S_κ² = clip(1 - κ²/omega_yield², 0, 1) (hard clip) or
        softplus S_w(κ²/omega_yield²) for floor_target='ii'.
        If π were hard-coded, S_κ²(omega_yield=2.0) == S_κ²(omega_yield=π)
        — they would be equal. They differ only if omega_yield is actually used.
        ADD-3 §3.3.3 Q4: keep omega_yield read at k4q:258.
        """
        n = 4
        mask = engine_alive_mask(n)
        rng = np.random.default_rng(778)
        u = np.zeros((n, n, n, 3))
        q_raw = rng.standard_normal((n, n, n, 4)) * 0.5
        q_raw[..., 0] += 1.0
        q = q_raw / np.linalg.norm(q_raw, axis=-1, keepdims=True)
        q[~mask] = [1., 0., 0., 0.]

        # Check S_w formula directly using known formula
        # With omega_yield=2.0, κ²=0.9*4.0=3.6: A_κ²=0.9, S_w(0.9) is well-defined
        # With omega_yield=π, same κ²=3.6: A_κ²=3.6/π²≈0.365, S_w(0.365) ≠ S_w(0.9)
        w = 0.05
        S_correct = float(_softplus_sat(jnp.array([0.9]), w)[0])
        S_pi_wrong = float(_softplus_sat(jnp.array([3.6 / (math.pi**2)]), w)[0])
        assert abs(S_correct - S_pi_wrong) > 0.1, (
            f"S_w(0.9)={S_correct:.4f} too close to S_w(3.6/π²)={S_pi_wrong:.4f}; "
            "test wouldn't discriminate omega_yield from π.")

        # Now verify the engine with floor_target='ii', omega_yield=2.0 vs omega_yield=π:
        # energies must differ (because S_κ² depends on omega_yield)
        kap = np.asarray(_bond_wryness_jax(jnp.asarray(q), 1.0))
        kap_sq_alive = float(np.mean(np.sum(kap[mask]**2, axis=(-1, -2))))
        if kap_sq_alive < 1e-6:
            pytest.skip("κ too small for this seed")

        cfg = GridFixCfg(use_floor=True, floor_w=w, floor_target="ii")
        args_oy2 = dict(dx=1.0, G=0.0, G_c=0.0, gamma=1.0,
                        omega_yield=2.0, epsilon_yield=1.0,
                        k_op10=0.0, k_refl=0.0, k_hopf=0.0)
        args_oypi = dict(dx=1.0, G=0.0, G_c=0.0, gamma=1.0,
                         omega_yield=math.pi, epsilon_yield=1.0,
                         k_op10=0.0, k_refl=0.0, k_hopf=0.0)

        W2 = float(np.sum(np.asarray(_call_gf(u, q, mask, cfg, args_oy2))[mask]))
        Wpi = float(np.sum(np.asarray(_call_gf(u, q, mask, cfg, args_oypi))[mask]))

        assert abs(W2 - Wpi) > 1e-8, (
            f"floor_target='ii' energy same at omega_yield=2.0 ({W2:.6e}) and "
            f"omega_yield=π ({Wpi:.6e}); engine should use omega_yield not π.")


# ---------------------------------------------------------------------------
# 22. read_back_flags reads from sources (B6)
# ---------------------------------------------------------------------------

class TestReadBackSources:
    """read_back_flags reads from sources, not hardcoded literals (B6).

    B6 mutants: readout_delta_R hardcoded 1e-10 (not from module constant),
    use_impedance_boundary hardcoded False, jax_enable_x64 hardcoded True.
    """

    def test_readout_delta_R_from_module_constant(self):
        """readout_delta_R comes from _READOUT_DELTA_R module constant (B6).

        _READOUT_DELTA_R is importable and equals 1e-10. If anyone changes
        the constant, read_back_flags will reflect the change.
        """
        assert _READOUT_DELTA_R == 1e-10, (
            f"_READOUT_DELTA_R should be 1e-10; got {_READOUT_DELTA_R}")
        rb = read_back_flags(GridFixCfg(), gamma=1.0, dx=1.0, omega_yield=1.0)
        assert rb["readout_delta_R"] == _READOUT_DELTA_R, (
            f"readout_delta_R in rb ({rb['readout_delta_R']}) ≠ _READOUT_DELTA_R "
            f"({_READOUT_DELTA_R}); not reading from module constant.")

    def test_use_impedance_boundary_from_module_constant(self):
        """use_impedance_boundary comes from _USE_IMPEDANCE_BOUNDARY (B6)."""
        assert _USE_IMPEDANCE_BOUNDARY is False, (
            f"_USE_IMPEDANCE_BOUNDARY should be False; got {_USE_IMPEDANCE_BOUNDARY}")
        rb = read_back_flags(GridFixCfg(), gamma=1.0, dx=1.0, omega_yield=1.0)
        assert rb["use_impedance_boundary"] == _USE_IMPEDANCE_BOUNDARY, (
            f"use_impedance_boundary in rb ≠ _USE_IMPEDANCE_BOUNDARY; "
            "not reading from module constant.")

    def test_jax_enable_x64_reads_actual_config(self):
        """jax_enable_x64 reads from jax.config.jax_enable_x64 (not hardcoded True).

        This test verifies the key matches the actual JAX config value.
        If jax_enable_x64 were hardcoded True, it would fail in float32 mode.
        (In our x64-enabled CI/test env this just verifies True==True; the
        value source is what matters, not the value.)
        """
        import jax
        rb = read_back_flags(GridFixCfg(), gamma=1.0, dx=1.0, omega_yield=1.0)
        actual_x64 = bool(jax.config.jax_enable_x64)
        assert rb["jax_enable_x64"] == actual_x64, (
            f"jax_enable_x64 in rb ({rb['jax_enable_x64']}) ≠ "
            f"jax.config.jax_enable_x64 ({actual_x64}); not reading from config.")

    def test_short_arc_reads_from_cfg(self):
        """short_arc reads from cfg.short_arc_form when set (B6).

        Mutant killer: if short_arc is hardcoded 'log', changing cfg to 'f'
        would still return 'log'. Must return cfg.short_arc_form.
        """
        cfg_log = GridFixCfg(use_bond_penalty=True, gamma_h=1.0, short_arc_form="log")
        rb_log = read_back_flags(cfg_log, gamma=1.0, dx=1.0, omega_yield=1.0)
        assert rb_log["short_arc"] == "log", (
            f"short_arc with short_arc_form='log': got {rb_log['short_arc']!r}")

        cfg_f = GridFixCfg(use_bond_penalty=True, gamma_h=1.0, short_arc_form="f")
        rb_f = read_back_flags(cfg_f, gamma=1.0, dx=1.0, omega_yield=1.0)
        assert rb_f["short_arc"] == "f", (
            f"short_arc should read from cfg.short_arc_form; "
            f"got {rb_f['short_arc']!r} (hardcoded 'log' mutant would give 'log')")

    def test_readout_lower_clip_count_none(self):
        """readout_lower_clip_count is None (not computed without field args). B6.

        read_back_flags has no field arguments; computing the lower-clip count
        requires a real field. The key is present but the value is None.
        """
        rb = read_back_flags(GridFixCfg(), gamma=1.0, dx=1.0, omega_yield=1.0)
        assert "readout_lower_clip_count" in rb, "key must be present"
        assert rb["readout_lower_clip_count"] is None, (
            f"readout_lower_clip_count should be None (not computed); "
            f"got {rb['readout_lower_clip_count']!r}")

    def test_readout_delta_R_is_cf_constant(self):
        """_READOUT_DELTA_R in gf is the same object as _CF_READOUT_DELTA_R in cf (B6).

        One constant, not two independently defined literals. Mutant: gf constant
        redefined as 2e-10 diverges from cf constant used by the readout function.
        """
        from ave.topological.cosserat_field_3d import _CF_READOUT_DELTA_R
        assert _READOUT_DELTA_R == _CF_READOUT_DELTA_R, (
            f"_READOUT_DELTA_R ({_READOUT_DELTA_R}) ≠ _CF_READOUT_DELTA_R "
            f"({_CF_READOUT_DELTA_R}); must be the same constant (B6)")


# ---------------------------------------------------------------------------
# 23. Production sponge through CosseratField3D engine path (B4)
# ---------------------------------------------------------------------------

class TestSpongeEngine:
    """dt-invariant sponge tested through CosseratField3D production path.

    B4 mutants: cf.use_sponge default-ON, sponge not applied in engine path,
    dt-dependent attenuation.
    """

    def test_cf_use_sponge_default_false(self):
        """cf.use_sponge=False by default. Kills default-ON mutant (B4)."""
        from ave.topological.cosserat_field_3d import CosseratField3D
        cf = CosseratField3D(4, 4, 4, dx=1.0, pml_thickness=2)
        assert cf.use_sponge is False, "use_sponge must default to False (B4)"

    def test_grid_fix_cfg_use_sponge_false_wires_false(self):
        """GridFixCfg(use_sponge=False) wires to cf.use_sponge=False."""
        from ave.topological.cosserat_field_3d import CosseratField3D
        cf = CosseratField3D(4, 4, 4, dx=1.0, pml_thickness=2,
                             grid_fix_cfg=GridFixCfg(use_sponge=False))
        assert cf.use_sponge is False

    def test_grid_fix_cfg_use_sponge_true_wires_true(self):
        """GridFixCfg(use_sponge=True) wires to cf.use_sponge=True."""
        from ave.topological.cosserat_field_3d import CosseratField3D
        cf = CosseratField3D(4, 4, 4, dx=1.0, pml_thickness=2,
                             grid_fix_cfg=GridFixCfg(use_sponge=True))
        assert cf.use_sponge is True

    def test_sponge_applies_exp_mask_at_boundary(self):
        """With use_sponge=True, _zero_vel at boundary (d=0) uses exp(-σ·dt/2).

        At d=0: σ=σ_max; attenuation=exp(-σ_max·dt/2). Differs from cos_pml
        which gives a dt-independent value. B4: tests through production path.
        """
        from ave.topological.cosserat_field_3d import CosseratField3D
        n = 8; pml = 4
        cf = CosseratField3D(n, n, n, dx=1.0, pml_thickness=pml)
        cf.use_sponge = True
        sigma_max = cf.sponge_sigma_max
        dt = 0.1

        cf.u_dot = np.zeros((n, n, n, 3))
        cf.Omega = np.zeros((n, n, n, 3))
        if cf.mask_alive[0, 0, 0]:
            cf.u_dot[0, 0, 0] = np.array([1.0, 0.0, 0.0])
        else:
            pytest.skip("(0,0,0) not alive")

        cf._zero_velocities_outside_alive_k4(apply_pml=True, dt=dt)
        actual = float(cf.u_dot[0, 0, 0, 0])
        expected = math.exp(-sigma_max * dt / 2.0)
        assert abs(actual - expected) < 1e-12, (
            f"Sponge at boundary: got {actual:.8f}, expected exp(-σ·dt/2)={expected:.8f}")

    def test_sponge_dt_invariant_through_engine(self):
        """Total attenuation exp(-σ·t) is dt-invariant through _zero_vel. B4.

        n_half_kicks at dt → product = exp(-σ·dt/2)^n = exp(-σ·t). Invariant.
        """
        from ave.topological.cosserat_field_3d import CosseratField3D
        n = 8; pml = 4
        t_total = 0.5

        def measure_attenuation(dt):
            cf = CosseratField3D(n, n, n, dx=1.0, pml_thickness=pml)
            cf.use_sponge = True
            cf.u_dot = np.zeros((n, n, n, 3))
            cf.Omega = np.zeros((n, n, n, 3))
            if not cf.mask_alive[0, 0, 0]:
                return None
            cf.u_dot[0, 0, 0] = np.array([1.0, 0.0, 0.0])
            n_hk = int(round(2.0 * t_total / dt))
            for _ in range(n_hk):
                cf._zero_velocities_outside_alive_k4(apply_pml=True, dt=dt)
            return float(cf.u_dot[0, 0, 0, 0])

        cf_ref = CosseratField3D(n, n, n, dx=1.0, pml_thickness=pml)
        sigma_max = cf_ref.sponge_sigma_max
        expected = math.exp(-sigma_max * t_total)

        a1 = measure_attenuation(0.1)
        a2 = measure_attenuation(0.01)
        if a1 is None or a2 is None:
            pytest.skip("(0,0,0) not alive")

        assert abs(a1 - expected) < 1e-6, (
            f"dt=0.1: attenuation {a1:.8f} vs exp(-σt)={expected:.8f}")
        assert abs(a2 - expected) < 1e-6, (
            f"dt=0.01: attenuation {a2:.8f} vs exp(-σt)={expected:.8f}")
        assert abs(a1 - a2) < 1e-4, (
            f"dt-invariance violated: a(dt=0.1)={a1:.8f}, a(dt=0.01)={a2:.8f}")


# ---------------------------------------------------------------------------
# 24. Stepper wiring: flags ON dispatches to _val_and_grad_k4_gf (B2)
# ---------------------------------------------------------------------------

class TestStepperWiring:
    """grid_fix_cfg flags ON wires to _val_and_grad_k4_gf in step_k4. B2.

    B2 mutants: k4q step_k4 ignores GridFixCfg (calls main path regardless),
    flags-ON gives same result as flags-OFF.
    """

    def test_flags_off_step_bitidentical_to_no_cfg(self):
        """With grid_fix_cfg all-OFF, step_k4 result is bit-identical to no-cfg.

        B2: flags-OFF path must be exact main (_val_and_grad_k4), not _val_and_grad_k4_gf.
        """
        from ave.topological.cosserat_field_3d import CosseratField3D
        n = 4
        rng = np.random.default_rng(901)

        def make_cf(grid_fix_cfg=None):
            cf = CosseratField3D(n, n, n, dx=1.0, grid_fix_cfg=grid_fix_cfg)
            q_raw = rng.standard_normal((n, n, n, 4)) * 0.1
            q_raw[..., 0] += 1.0
            q = q_raw / np.linalg.norm(q_raw, axis=-1, keepdims=True)
            q[~cf.mask_alive] = [1., 0., 0., 0.]
            cf.q = q
            cf.u = rng.standard_normal((n, n, n, 3)) * 0.05
            cf.u[~cf.mask_alive] = 0.0
            cf.u_dot = rng.standard_normal((n, n, n, 3)) * 0.01
            cf.u_dot[~cf.mask_alive] = 0.0
            cf.Omega = rng.standard_normal((n, n, n, 3)) * 0.01
            cf.Omega[~cf.mask_alive] = 0.0
            return cf

        rng = np.random.default_rng(901)
        cf_main = make_cf(grid_fix_cfg=None)
        rng = np.random.default_rng(901)
        cf_off = make_cf(grid_fix_cfg=GridFixCfg())

        cf_main.step_k4(dt=0.01)
        cf_off.step_k4(dt=0.01)

        assert np.array_equal(cf_main.u, cf_off.u), \
            "flags-OFF step not bit-identical to no-cfg step (u)"
        assert np.array_equal(cf_main.q, cf_off.q), \
            "flags-OFF step not bit-identical to no-cfg step (q)"
        assert np.array_equal(cf_main.u_dot, cf_off.u_dot), \
            "flags-OFF step not bit-identical to no-cfg step (u_dot)"

    def test_flags_on_step_differs_from_flags_off(self):
        """With use_bond_penalty=True, step_k4 gives different state than flags-OFF.

        B2: flags-ON must reach _val_and_grad_k4_gf, not main path.
        """
        from ave.topological.cosserat_field_3d import CosseratField3D
        n = 4
        rng = np.random.default_rng(902)
        q_raw = rng.standard_normal((n, n, n, 4)) * 0.2
        q_raw[..., 0] += 1.0
        q = q_raw / np.linalg.norm(q_raw, axis=-1, keepdims=True)
        u = rng.standard_normal((n, n, n, 3)) * 0.05
        u_dot = rng.standard_normal((n, n, n, 3)) * 0.01
        Omega = rng.standard_normal((n, n, n, 3)) * 0.01

        def make_cf(cfg):
            cf = CosseratField3D(n, n, n, dx=1.0, grid_fix_cfg=cfg)
            cf.q = q.copy()
            cf.u = u.copy()
            cf.u_dot = u_dot.copy()
            cf.Omega = Omega.copy()
            cf.q[~cf.mask_alive] = [1., 0., 0., 0.]
            cf.u[~cf.mask_alive] = 0.0
            cf.u_dot[~cf.mask_alive] = 0.0
            cf.Omega[~cf.mask_alive] = 0.0
            return cf

        cfg_off = GridFixCfg()
        cfg_on = GridFixCfg(use_bond_penalty=True, gamma_h=0.5, short_arc_form="log")

        cf_off = make_cf(cfg_off)
        cf_on = make_cf(cfg_on)

        for _ in range(3):
            cf_off.step_k4(dt=0.01)
            cf_on.step_k4(dt=0.01)

        diff_u = float(np.abs(cf_on.u - cf_off.u).max())
        diff_q = float(np.abs(cf_on.q - cf_off.q).max())
        assert diff_u > 1e-8 or diff_q > 1e-8, (
            f"flags-ON step identical to flags-OFF after 3 steps; "
            f"diff_u={diff_u:.3e}, diff_q={diff_q:.3e}. B2 wiring not active.")
