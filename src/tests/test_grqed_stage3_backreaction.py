"""Stage-3 TWO-WAY gravitational back-reaction — the self-gravitation loop (#86).

Tests the make-or-break increment: the field SOURCES ITSELF. Stage-1 solved the
one-way T₀₀^matter → ε₁₁; Stage-3 closes the loop T₀₀^total = matter + field(ε₁₁)
and iterates to a self-consistent fixed point, from which M_eff EMERGES (with the
binding-deficit subtraction M_eff c² = ∫ρ_matter c² − ∫u_bind, u_bind=½κ|∇ε₁₁|²).

THE FOUR AT-RISK CHECKS (the REAL gates — the tautological "reproduce 7GM/c²r" is
DEMOTED, not used as a gate):
  1. EXTENDED (non-δ) SOURCE → 1/r EXTERIOR (an unlabeled blob sources 1/r gravity).
  2. S_min-INDEPENDENT EMERGENT M_eff/r_s (the clamp did NOT set the mass).
  3. RAY-TRACED 4GM/bc² AS OUTPUT (the GR doubling falls out of the emergent metric).
  4. TWO-MASS SUPERPOSITION (the nonlinearity ENGAGES — combined ≠ linear sum).
plus RECOVER-GR (consistency-class, weak field) and the BOUNDEDNESS/ENERGY gate
(Picard contraction ρ < 1 proven, not asserted; |dH/H| stationary at the fixed
point — no damping bought the metric).

SUBSTRATE-NATIVE: |∇ε₁₁|² and the elliptic solve share the SAME native diamond-K4
Grad/Div (_build_native_grad_div) — no Cartesian gradient. ONE Op14 kernel
S(A)=(1−A²)^{1/2} (Stage-1's stiffness_profile). The field self-energy lives on the
radial/bulk ε₁₁ (A1-dilatation) channel — NOT cross-wired to shear/EM.

HONEST FRAMING (NOT overclaimed): M_eff EMERGES from the field's own integrated
energy (the architectural win), BUT r_s=2G·M_eff/c² IMPORTS G (the modulus c⁴/7G
embeds the back-solved ξ; K=2G is GR-imported, PR#261). So "TWO-WAY back-reaction
making M_eff EMERGENT", NOT "replaces GR" / NOT "derives gravity". Recover-GR is
consistency-class.

α-CLEAN: gravity sector, NO ALPHA / Q_TANK (source-level guard test).

The heavy two-way solves (sparse Picard spsolve × outer self-consistency loop) are
routed to the engine_sim lane (conftest allowlist; #411 cost+role discipline). The
fast closed-form / single-solve checks STAY gating.
"""

import inspect

import numpy as np
import pytest

from ave.gravity.backreaction import (
    KAPPA_GRAV,
    binding_energy_density,
    boundedness_energy_gate,
    check1_extended_source_recovers_inverse_r,
    check2_smin_independent_emergent_rs,
    check3_raytrace_recovers_4GM,
    check4_two_mass_superposition_engages_nonlinearity,
    effective_mass,
    field_energy_density,
    gaussian_blob,
    recover_gr_weak_field,
    solve_backreaction,
)
from ave.gravity.gw_propagation import _build_native_grad_div


# ═══════════════════════════════════════════════════════════════════════════════
# α-CLEAN guard — no ALPHA / Q_TANK leaked into the Stage-3 code path.
# ═══════════════════════════════════════════════════════════════════════════════


class TestAlphaClean:
    def test_function_bodies_are_alpha_free(self) -> None:
        for fn in (
            field_energy_density,
            binding_energy_density,
            effective_mass,
            solve_backreaction,
            gaussian_blob,
            check1_extended_source_recovers_inverse_r,
            check2_smin_independent_emergent_rs,
            check3_raytrace_recovers_4GM,
            check4_two_mass_superposition_engages_nonlinearity,
            recover_gr_weak_field,
            boundedness_energy_gate,
        ):
            src = inspect.getsource(fn)
            assert "ALPHA" not in src, f"{fn.__name__} references ALPHA"
            assert "Q_TANK" not in src, f"{fn.__name__} references Q_TANK"

    def test_modulus_is_gravity_sector_not_alpha(self) -> None:
        """KAPPA_GRAV = c⁴/7G is a gravity-sector constant (G-imported), NOT α."""
        from ave.core.constants import C_0, G

        assert KAPPA_GRAV == pytest.approx(C_0**4 / (7.0 * G))


# ═══════════════════════════════════════════════════════════════════════════════
# Field self-energy + binding-deficit ledger (fast, closed-form).
# ═══════════════════════════════════════════════════════════════════════════════


class TestFieldEnergyAndBindingDeficit:
    def test_field_energy_is_positive_definite(self) -> None:
        """u_field = ½|∇ε₁₁|² ≥ 0 (self-reinforcing — the runaway risk)."""
        N = 12
        Grad, _ = _build_native_grad_div(N)
        rng = np.random.default_rng(0)
        eps = rng.standard_normal((N, N, N)) * 0.1
        u = field_energy_density(eps, Grad)
        assert np.all(u >= 0.0)

    def test_uniform_field_has_zero_energy(self) -> None:
        """A constant ε₁₁ has |∇ε₁₁|² = 0 — no field energy (gauge-correct)."""
        N = 10
        Grad, _ = _build_native_grad_div(N)
        eps = np.full((N, N, N), 0.37)
        u = field_energy_density(eps, Grad)
        assert np.allclose(u, 0.0, atol=1e-12)

    def test_native_gradient_unit_ramp(self) -> None:
        """The native K4 |∇|² of a unit-slope ramp is 1 (the gradient is native,
        NOT a Cartesian np.gradient — the load-bearing K4 checkpoint)."""
        N = 12
        Grad, _ = _build_native_grad_div(N)
        ii = np.arange(N)
        eps = np.broadcast_to(ii[None, None, :], (N, N, N)).astype(float)
        u = field_energy_density(eps, Grad, kappa=2.0)  # ½·2·|∇|² = |∇|²
        # interior (away from periodic-wrap faces) is exactly 1.
        assert u[3:-3, 3:-3, 3:-3].mean() == pytest.approx(1.0, rel=1e-9)

    def test_binding_deficit_subtracts_not_adds(self) -> None:
        """M_eff = M_matter − U_bind (a well DEFICITS its ADM mass; NOT +U_bind)."""
        N = 16
        Grad, _ = _build_native_grad_div(N)
        T = gaussian_blob(N, sigma=2.0, amplitude=0.1)
        c = N // 2
        i, j, k = np.indices((N, N, N))
        rr = np.sqrt((i - c) ** 2 + (j - c) ** 2 + (k - c) ** 2)
        rr[c, c, c] = 1.0
        eps = 0.5 / rr  # a monopole well (nonzero |∇ε|)
        info = effective_mass(T, eps, Grad, g_self=1.0)
        assert info["U_bind"] > 0.0
        assert info["M_eff"] == pytest.approx(info["M_matter"] - info["U_bind"])
        assert info["M_eff"] < info["M_matter"], "deficit must REDUCE the mass"


# ═══════════════════════════════════════════════════════════════════════════════
# The two-way loop — fast structural checks (g_self=0 recovers one-way; converges).
# ═══════════════════════════════════════════════════════════════════════════════


class TestTwoWayLoopStructure:
    def test_g_self_zero_recovers_one_way(self) -> None:
        """g_self=0 ⇒ no field source ⇒ U_bind=0, M_eff=M_matter (the Stage-1 limit)."""
        res = solve_backreaction(N=16, amplitude=0.03, g_self=0.0, max_outer=4)
        assert res["U_bind"] == pytest.approx(0.0, abs=1e-12)
        assert res["M_eff"] == pytest.approx(res["M_matter"], rel=1e-12)

    def test_loop_converges_and_binds_in_weak_regime(self) -> None:
        """Weak two-way loop converges, contracts (ρ<1), and binds (U_bind>0)."""
        res = solve_backreaction(N=16, amplitude=0.05, g_self=1.0, max_outer=40)
        assert res["converged"], f"loop did not converge (n_outer={res['n_outer']})"
        assert res["contraction_factor"] < 1.0, "non-contractive (runaway risk)"
        assert res["U_bind"] > 0.0, "no binding deficit — back-reaction inert"
        assert 0.0 < res["binding_fraction"] < 1.0


# ═══════════════════════════════════════════════════════════════════════════════
# HEAVY — the four at-risk checks + recover-GR + boundedness/energy gate.
# Routed to the engine_sim lane via the conftest allowlist (cost+role; #411).
# ═══════════════════════════════════════════════════════════════════════════════


class TestRecoverGR:
    """Consistency-class: weak-field two-way recovers the one-way GR core."""

    def test_recover_gr_weak_field(self) -> None:
        g = recover_gr_weak_field()
        assert g["passed"], g["verdict"]
        assert g["binding_fraction"] < 0.10
        assert g["exterior_is_inverse_r"]


class TestAtRiskCheck1InverseR:
    """AT-RISK 1: an unlabeled extended blob sources a 1/r exterior monopole."""

    def test_extended_source_recovers_inverse_r(self) -> None:
        r = check1_extended_source_recovers_inverse_r(N=28, sigma=2.0, amplitude=0.04)
        assert r["converged"]
        # the 1/r model wins over 1/r² (boundary-robust a+b/r discriminator).
        assert r["r2_inv_r"] > r["r2_inv_r2"], "1/r² fits better than 1/r"
        assert r["passed"], r["verdict"]


class TestAtRiskCheck2SminIndependent:
    """AT-RISK 2: the EMERGENT M_eff (→ r_s) is S_min/clip-independent."""

    def test_emergent_mass_is_smin_independent(self) -> None:
        r = check2_smin_independent_emergent_rs(N=24, s_min_values=(1e-4, 1e-3, 1e-2))
        assert r["M_eff_rel_spread"] <= 0.05, (
            f"M_eff moved with S_min (spread={r['M_eff_rel_spread']:.2e}): {r['rows']}"
        )
        assert r["passed"], r["verdict"]


class TestAtRiskCheck3Raytrace:
    """AT-RISK 3: ray-traced deflection comes out at the GR 4GM/bc² (not Newton)."""

    def test_raytrace_recovers_4GM(self) -> None:
        r = check3_raytrace_recovers_4GM(N=32, sigma=2.0, amplitude=0.04)
        assert r["converged"]
        # the GR-vs-Newton discriminator: closer to 2ν (GR) than ν (Newton).
        assert r["closer_to_gr"], (
            f"deflection coeff {r['delta_coeff']:.4f} is Newtonian, not GR"
        )
        assert r["decisively_past_newton"]
        assert r["passed"], r["verdict"]


class TestAtRiskCheck4Nonlinearity:
    """AT-RISK 4: two masses — the nonlinearity ENGAGES (combined ≠ linear sum)."""

    def test_two_mass_nonlinearity_engages(self) -> None:
        r = check4_two_mass_superposition_engages_nonlinearity()
        assert r["converged_on"] and r["converged_off"]
        # turning the back-reaction ON multiplies the superposition residual.
        assert r["engage_ratio"] >= 1.5, (
            f"back-reaction did not multiply nonlinearity (ratio={r['engage_ratio']:.2f})"
        )
        assert r["passed"], r["verdict"]


class TestBoundednessEnergyGate:
    """Picard contraction PROVEN (ρ<1) + energy stationary at the fixed point."""

    def test_contractive_and_energy_stationary(self) -> None:
        g = boundedness_energy_gate(amplitudes=(0.02, 0.05, 0.10, 0.20))
        assert g["all_contractive"], (
            f"a swept amplitude is non-contractive: {g['rows']}"
        )
        assert g["all_energy_stationary"], (
            f"energy not stationary at the fixed point: {g['rows']}"
        )
        assert g["passed"], g["verdict"]
        # ρ grows with field strength (the first-principles compactness prediction).
        rhos = [row["contraction_factor"] for row in g["rows"]]
        assert rhos[0] < rhos[-1], "ρ should grow with amplitude (compactness)"
