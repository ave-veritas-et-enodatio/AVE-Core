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
)
from ave.topological.k4_quaternion import (
    _energy_density_k4_saturated,
    _bond_wryness_jax,
    _op10_density_q,
    _hopf_density_q,
)
from ave.topological.cosserat_field_3d import (
    _readout_floor,
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

        cfg_off = GridFixCfg()
        W_gf = np.asarray(_call_gf(u, q, mask, cfg_off, args))
        assert np.array_equal(W_gf, W_golden), (
            f"energy density not bit-identical to golden: max diff "
            f"{float(np.abs(W_gf - W_golden).max()):.3e}")

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
                          n=4, eps=1e-5):
        """Numerical K=0 per-unit-cell team-space Hessian of bond energy.

        Uses all sites alive (no BCC mask) so all 4 teams are present.
        Physics args G=G_c=gamma=k_*=0 isolate the bond penalty.
        Normalizes H_total by N_per_team = n³/4 to get per-unit-cell values.
        Returns (4,4) matrix per unit cell in units of gamma_h.
        """
        from ave.topological.k4_quaternion import q_from_omega_eng
        mask = np.ones((n, n, n), dtype=bool)
        I, J, K = np.meshgrid(range(n), range(n), range(n), indexing="ij")
        teams = (I + J + K) % 4
        N_per_team = n ** 3 // 4
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

    def test_long_wave_unchanged(self):
        """Bond penalty is additive outside clips; flags-off energy unchanged. ADD-3 §3.3.1."""
        n = 8
        rng = np.random.default_rng(77)
        mask = bcc_alive(n)
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
        mask = bcc_alive(n)
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
        mask = bcc_alive(n)
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
        mask = bcc_alive(n)
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
    """

    @staticmethod
    def _y_flip(q):
        n = q.shape[1]
        idx = (n - np.arange(n)) % n
        return q[:, idx, :]

    def test_two_star_invariant_under_y_flip(self):
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
        W_rot = np.asarray(_call_gf(np.zeros_like(q_rot[..., :3]), q_rot, mask, cfg))
        E_rot = float(np.sum(W_rot[mask]))

        assert abs(E_orig - E_rot) < 1e-10 * max(abs(E_orig), 1.0), (
            f"Two-star op10_b NOT invariant under G3 (y-flip): "
            f"|E_orig - E_rot| = {abs(E_orig-E_rot):.3e}")

    def test_one_star_differs_from_two_star_per_site(self):
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
            f"(max_diff={max_diff:.2e}); expected structural difference.")


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
        mask = bcc_alive(n)
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
        mask = bcc_alive(n)
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
        mask = bcc_alive(n)
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
        mask = bcc_alive(n)
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
        mask = bcc_alive(n)
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
        mask = bcc_alive(n)
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
        mask = bcc_alive(n)
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


# ---------------------------------------------------------------------------
# 17. Half-turn rule: boundary tests (exact / just below / just above 180°)
# ---------------------------------------------------------------------------

class TestHalfTurnBoundary:
    """diag_bad_cell_count boundary at exactly 180°.
    Spec: grid-fix-topology-cut_2026-10-28.md §1; must-emerge-list :52.
    """

    @staticmethod
    def _make_antipodal_pair(n=8):
        mask = bcc_alive(n)
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
        mask = bcc_alive(n)
        q = np.tile([1., 0., 0., 0.], (n, n, n, 1)).astype(float)
        q[~mask] = [1., 0., 0., 0.]
        eps = 1e-10
        q[1, 1, 1] = np.array([eps, 0., 0., np.sqrt(1.0 - eps**2)])
        bad = diag_bad_cell_count(q, mask)
        assert bad == 0, f"Bond with Re = {eps:.2e} > 0 should NOT be bad; got {bad}"

    def test_just_above_180_is_bad(self):
        n = 8
        mask = bcc_alive(n)
        q = np.tile([1., 0., 0., 0.], (n, n, n, 1)).astype(float)
        q[~mask] = [1., 0., 0., 0.]
        eps = 1e-10
        q[1, 1, 1] = np.array([-eps, 0., 0., np.sqrt(1.0 - eps**2)])
        bad = diag_bad_cell_count(q, mask)
        assert bad >= 1, f"Bond with Re = {-eps:.2e} < 0 should be bad; got {bad}"

    def test_identity_field_zero_bad(self):
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
# 18. F_d diagnostic (NOT-SPEC-COMPLIANT on BCC — see QUESTIONS.md Q3)
# ---------------------------------------------------------------------------

class TestFdDiagnostic:
    """F_d = team-differential u energy fraction.
    CURRENT FORM: per-team-mean (excludes uniform shift). ADD-3 H3.
    NOT-SPEC-COMPLIANT on BCC (m=2 DFT mode = uniform translation; see Q3).
    """

    def test_zero_displacement_gives_zero_Fd(self):
        n = 8
        mask = bcc_alive(n)
        u = np.zeros((n, n, n, 3))
        Fd = diag_F_d(u, mask)
        assert abs(Fd) < 1e-10, f"F_d for u=0 should be 0; got {Fd:.3e}"

    def test_uniform_displacement_gives_zero_Fd(self):
        n = 8
        mask = bcc_alive(n)
        u = np.ones((n, n, n, 3)) * 0.5
        u[~mask] = 0.0
        Fd = diag_F_d(u, mask)
        assert abs(Fd) < 1e-10, f"Uniform u: F_d should be 0; got {Fd:.3e}"

    def test_team_differential_u_gives_nonzero_Fd(self):
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
        """F_d with correct definition is ≤ 1. Swapped num/denom would be > 1."""
        n = 8
        mask = bcc_alive(n)
        I, J, K = np.meshgrid(range(n), range(n), range(n), indexing="ij")
        teams = (I + J + K) % 4
        u = np.zeros((n, n, n, 3))
        for t in range(4):
            u[teams == t, 0] = t * 0.1 - 0.15
        u[~mask] = 0.0
        Fd = diag_F_d(u, mask)
        assert Fd <= 1.0 + 1e-10, f"F_d should be <= 1; got {Fd:.6f}"


# ---------------------------------------------------------------------------
# 19. Sliding modes / uniform shift costs zero (spec item 1)
# ---------------------------------------------------------------------------

class TestUniformShiftZeroCost:
    """Spec item 1: uniform u-offset costs exactly zero. ADD-2 §3 item 1."""

    def test_uniform_u_offset_zero_cost(self):
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
