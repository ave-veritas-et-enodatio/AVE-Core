"""Stage-1 GR-extension — the saturating-modulus correction ON the linear core.

Tests the FIRST increment of the GR/QED-extension engine: a saturating-modulus
correction on the inherited GR (elastic-Poisson) solver. The inherited LINEAR core
is the weak-field limit (ε₁₁ = 7GM/c²r, n = 1 + (2/7)ε₁₁) and is NOT re-derived
here — these tests target ONLY the correction.

TWO-TEST DOCTRINE (every correction gets BOTH):
  1. RECOVER-THE-KNOWN  (consistency-class): at r ≫ r_sat, S → 1, D → 1, the
     corrected ε₁₁ reproduces the linear elastic-Poisson / Schwarzschild profile
     (ε₁₁ = r_sat/r = 7GM/c²r) and the refractive index n = 1 + (2/7)ε₁₁ to tol.
  2. ACTIVATE-AT-THE-EXTREME  (manifestation-class): the radial strain hits A = 1
     at r_sat = 3.5·r_s; the BULK stiffness D = 1/S → ∞ (halts the collapse); a
     yield SHELL appears.

LOAD-BEARING GATE (clip-independence): the yield-shell radius AND the integrated
source M_eff must be CLIP / S_min-INDEPENDENT. If they move with S_min, the
numerical clamp (not the physics) set the wall ⇒ FAIL.

The kernel is the canonical Op14 S(A) = (1 − A²)^{1/2} (graded_vacuum_network), the
ONE expression (F1). Per-channel sign-lock (INVARIANT-S2): BULK stiffens D = 1/S,
SHEAR softens c_shear = c₀√S, EM stays matched (refractive_index() UNCHANGED — a
spectator; an explicit guard test asserts it is untouched).

α-CLEAN: no ALPHA / Q_TANK import. The heavy finite-core relaxation + gate are
routed to the engine_sim lane (conftest allowlist; #411 OOM-class discipline).
"""

import numpy as np
import pytest

from ave.gravity.gw_propagation import (
    bulk_stiffness_D,
    clip_independence_gate,
    distributed_source_T00,
    refractive_index,
    relax_finite_core_strain,
    saturated_radial_strain,
    saturation_radius,
    schwarzschild_radius,
)

M_SUN = 1.989e30  # Solar mass [kg]


def _r_s(M_solar: float = 30.0) -> float:
    return schwarzschild_radius(M_solar * M_SUN)


# ═══════════════════════════════════════════════════════════════════════════════
# α-CLEAN guard — no ALPHA / Q_TANK leaked into the new Stage-1 code path.
# ═══════════════════════════════════════════════════════════════════════════════


class TestAlphaClean:
    """The Stage-1 functions must not import or depend on ALPHA / Q_TANK."""

    def test_module_source_is_alpha_free_in_stage1_block(self) -> None:
        import inspect

        import ave.gravity.gw_propagation as mod

        for fn in (
            saturated_radial_strain,
            bulk_stiffness_D,
            distributed_source_T00,
            relax_finite_core_strain,
            clip_independence_gate,
        ):
            src = inspect.getsource(fn)
            assert "ALPHA" not in src, f"{fn.__name__} references ALPHA"
            assert "Q_TANK" not in src, f"{fn.__name__} references Q_TANK"
        # the kernel reuse path imports from graded_vacuum_network, which is itself
        # α-guarded (asserts no Q_TANK/ALPHA in its globals).
        assert mod is not None


# ═══════════════════════════════════════════════════════════════════════════════
# TEST 1 — RECOVER-THE-KNOWN (consistency-class).
# ═══════════════════════════════════════════════════════════════════════════════


class TestRecoverTheKnown:
    """At r ≫ r_sat: S → 1, D → 1 ⇒ reproduce the linear elastic-Poisson core."""

    def test_far_field_strain_matches_linear_core(self) -> None:
        """ε₁₁^sat(r) → r_sat/r (= 7GM/c²r) for r ≫ r_sat."""
        r_s = _r_s()
        r_sat = saturation_radius(r_s)
        r = np.array([1e2, 1e3, 1e4, 1e6]) * r_sat
        eps_sat = saturated_radial_strain(r, r_s)
        eps_linear = r_sat / r  # inherited elastic-Poisson core
        assert np.allclose(eps_sat, eps_linear, rtol=1e-12), (
            f"far-field strain departs from linear core: {eps_sat} vs {eps_linear}"
        )

    def test_far_field_stiffness_recovers_unity(self) -> None:
        """D(A) → 1 as A → 0 (no saturation, vacuum modulus)."""
        A = np.array([0.0, 1e-6, 1e-3, 1e-2])
        D = bulk_stiffness_D(A)
        assert np.allclose(D, 1.0, atol=2e-4), f"D should → 1 in weak field: {D}"

    def test_far_field_refractive_index_is_linear(self) -> None:
        """n = 1 + (2/7)ε₁₁ in the recovered limit (Op19; EM spectator UNCHANGED)."""
        from ave.core.constants import NU_VAC

        r_s = _r_s()
        r_sat = saturation_radius(r_s)
        r = np.array([1e2, 1e3, 1e4]) * r_sat
        eps = saturated_radial_strain(r, r_s)
        n = refractive_index(r, r_s)
        n_linear = 1.0 + NU_VAC * (r_sat / r)
        # refractive_index uses the EM r_s/r channel; in the weak field it matches
        # the (2/7)·ε₁₁ linear form (consistency).
        assert np.allclose(n, n_linear, rtol=1e-3), f"n departs from linear: {n} vs {n_linear}"

    def test_finite_core_far_tail_is_unsaturated(self) -> None:
        """The relaxed finite-core field has an UNSATURATED (A < 1) exterior tail
        — the recover-the-known regime exists outside the shell."""
        res = relax_finite_core_strain(N=24)
        A = res["A"]
        N = 24
        c = N // 2
        # at the far interior edge (just inside the Dirichlet boundary), A < 1
        # (unsaturated exterior — the recover-the-known regime exists outside the shell).
        assert A[c, c, N - 3] < 0.4, f"far tail not unsaturated: A={A[c, c, N - 3]}"


# ═══════════════════════════════════════════════════════════════════════════════
# TEST 2 — ACTIVATE-AT-THE-EXTREME (manifestation-class).
# ═══════════════════════════════════════════════════════════════════════════════


class TestActivateAtTheExtreme:
    """Strain hits A = 1 at r_sat = 3.5·r_s; bulk stiffens (D → ∞); shell appears."""

    def test_saturation_radius_is_3p5_rs(self) -> None:
        """r_sat = 7GM/c² = 3.5·r_s = (2/ν_vac)·r_s."""
        r_s = _r_s()
        assert saturation_radius(r_s) == pytest.approx(3.5 * r_s)

    def test_strain_reaches_unity_at_r_sat(self) -> None:
        """ε₁₁^sat(r_sat) = 1 (the yield), and is capped at 1 inside."""
        r_s = _r_s()
        r_sat = saturation_radius(r_s)
        assert saturated_radial_strain(r_sat, r_s) == pytest.approx(1.0)
        assert saturated_radial_strain(0.3 * r_sat, r_s) == pytest.approx(1.0)

    def test_bulk_stiffness_diverges_at_yield(self) -> None:
        """D = 1/S → ∞ (capped at 1/S_min) as A → 1: the medium goes rigid."""
        assert bulk_stiffness_D(0.9) > bulk_stiffness_D(0.5)
        assert bulk_stiffness_D(0.99) > bulk_stiffness_D(0.9)
        # at A = 1 the kernel floor caps D at exactly 1/S_min.
        assert bulk_stiffness_D(1.0, S_min=1e-3) == pytest.approx(1e3, rel=1e-9)
        assert bulk_stiffness_D(1.0, S_min=1e-4) == pytest.approx(1e4, rel=1e-9)

    def test_bulk_stiffens_shear_does_not_uniform_scale(self) -> None:
        """Per-channel sign-lock: BULK D = 1/S (stiffen) is NOT a uniform C·S.
        The shear projection is c_shear = c₀√S → 0 (soften) — opposite sign.
        Assert D·S = 1 (reciprocal), distinguishing it from any D ∝ S form."""
        A = np.array([0.0, 0.3, 0.6, 0.9])
        from ave.solvers.graded_vacuum_network import saturation_kernel

        S = saturation_kernel(A, exponent=0.5, S_min=1e-12)
        D = bulk_stiffness_D(A, S_min=1e-12)
        assert np.allclose(D * S, 1.0, rtol=1e-9), "BULK must be D = 1/S (stiffen), not D ∝ S"


# ═══════════════════════════════════════════════════════════════════════════════
# EM-SPECTATOR guard — refractive_index() must be UNCHANGED (the correction is on
# the radial/shear ε₁₁ channel ONLY).
# ═══════════════════════════════════════════════════════════════════════════════


class TestEMSpectatorUnchanged:
    """refractive_index() is the EM channel and must NOT carry the saturating
    modulus: Z_EM = Z₀, Γ_EM = 0 (matched). The Stage-1 correction touches only the
    radial/shear ε₁₁ channel."""

    def test_em_refractive_index_uses_em_horizon_not_r_sat(self) -> None:
        """n(r) diverges at the EM horizon r_s (= 2GM/c²), NOT at r_sat (= 3.5·r_s)
        — the EM channel is on a DIFFERENT boundary, untouched by the bulk yield."""
        r_s = _r_s()
        # n is large near r_s (EM horizon), finite at r_sat (deeper).
        n_near_rs = refractive_index(1.001 * r_s, r_s)
        n_at_rsat = refractive_index(saturation_radius(r_s), r_s)
        assert n_near_rs > n_at_rsat
        # n at r_sat = 3.5 r_s: ratio = 1/3.5, n = 1/(1 − 1/3.5) = 3.5/2.5 = 1.4.
        assert float(n_at_rsat) == pytest.approx(1.4, rel=1e-6)


# ═══════════════════════════════════════════════════════════════════════════════
# Fast closed-form smoke of the source + relaxation outputs (GATING tier).
# ═══════════════════════════════════════════════════════════════════════════════


class TestDistributedSource:
    """The finite-core demo uses a DISTRIBUTED T₀₀, NOT the inherited δ-source."""

    def test_source_is_distributed_not_delta(self) -> None:
        T = distributed_source_T00(16, sigma=2.0, amplitude=0.8)
        N = 16
        c = N // 2
        # smooth Gaussian: peak at centre, > a few cells wide (NOT a single δ spike).
        assert T[c, c, c] == pytest.approx(0.8)
        assert T[c + 2, c, c] > 0.1 * T[c, c, c], "source too sharp (δ-like)"
        # mass is spread over many cells (no single dominant cell).
        assert T[c, c, c] / T.sum() < 0.1, "source concentrated like a δ"

    def test_source_integral_is_clip_independent_invariant(self) -> None:
        """M_eff = Σ T₀₀ depends only on the source, never on S_min."""
        m1 = relax_finite_core_strain(N=16, S_min=1e-4)["M_eff"]
        m2 = relax_finite_core_strain(N=16, S_min=1e-2)["M_eff"]
        assert m1 == pytest.approx(m2, rel=1e-12)


# ═══════════════════════════════════════════════════════════════════════════════
# HEAVY — finite-core relaxation + the LOAD-BEARING clip-independence gate.
# Routed to the engine_sim lane via the conftest allowlist (cost+role; #411).
# ═══════════════════════════════════════════════════════════════════════════════


class TestFiniteCoreShellForms:
    """ACTIVATE-AT-THE-EXTREME, full relaxation: a strain-saturated shell forms."""

    def test_relaxation_forms_saturated_shell(self) -> None:
        res = relax_finite_core_strain(N=24)
        assert res["converged"], f"relaxation did not converge (n_iter={res['n_iter']})"
        assert res["max_A"] == pytest.approx(1.0, abs=1e-6), "core did not saturate"
        assert res["shell_radius"] > 0.0, "no saturation shell formed"
        # the shell is interior (the wall is well inside the box, not at the edge).
        assert res["shell_radius"] < 24 // 2, "shell at box edge (boundary artefact)"

    def test_core_saturated_exterior_unsaturated(self) -> None:
        """Monotone-ish: saturated core (A ≈ 1), unsaturated tail (A < 1)."""
        res = relax_finite_core_strain(N=24)
        A = res["A"]
        N = 24
        c = N // 2
        assert A[c, c, c] == pytest.approx(1.0, abs=1e-6), "core not saturated"
        assert A[c, c, N - 3] < 0.5, "exterior tail not unsaturated"


class TestClipIndependenceGate:
    """★ LOAD-BEARING GATE: the shell radius + M_eff must be S_min-INDEPENDENT.

    If they move with S_min, the numerical clamp (not the physics) set the wall
    ⇒ FAIL. A passing gate is the signature that the yield-physics set the wall.
    """

    def test_shell_radius_and_M_eff_are_S_min_independent(self) -> None:
        gate = clip_independence_gate(N=24, s_min_values=(1e-4, 1e-3, 1e-2))
        # M_eff is source-only: exactly invariant.
        assert gate["M_eff_rel_spread"] == pytest.approx(0.0, abs=1e-12), (
            "M_eff moved with S_min — the integrated source must be clip-independent"
        )
        # shell radius: the wall must not move with the clamp.
        assert gate["shell_radius_rel_spread"] <= 0.05, (
            f"FAIL — shell moved with S_min "
            f"(rel_spread={gate['shell_radius_rel_spread']:.3e}); "
            f"the numerical clamp set the wall: {gate['rows']}"
        )
        assert gate["passed"], gate["verdict"]
