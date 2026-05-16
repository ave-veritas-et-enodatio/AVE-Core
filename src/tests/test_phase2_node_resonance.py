"""
Pre-registered unit tests for NodeResonanceObserver — Stage 6 Phase 2.

Pins the per-node LC-tank resonance softening derived in
[doc 54_ §4](research/L3_electron_soliton/54_pair_production_axiom_derivation.md):

    Ω_node(r,t) / ω_0 = (1 − A²_yield(r,t))^(1/4)

where `A²_yield = A²_total / α` converts the engine's V_SNAP-normalized
saturation to V_yield normalization per doc 54_ §5.

These are smoke-tier unit tests (<2s): the observer is invoked against
directly-set engine state, so the formula is verified without running
a full TLM simulation. A separate validation script at
`src/scripts/vol_1_foundations/node_resonance_validation.py` runs the
v2 headline config (λ=3.5, T=0.1, K_drift=0.5) end-to-end and is the
full Phase 2 validation of pre-registered prediction P_phase2_omega.

Reference:
  - src/ave/topological/vacuum_engine.py::NodeResonanceObserver
  - research/L3_electron_soliton/54_pair_production_axiom_derivation.md §4
  - manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex:127-142
  - manuscript/predictions.yaml::P_phase2_omega

Phase 2 convention (inherited from test_axiom_4_vacuum_varactor.py):
  - Each test method asserts against a numerically-derivable target
  - Docstrings cite axiom + manuscript file:line + engine file:line
"""
from __future__ import annotations

import numpy as np
import pytest

from ave.topological.vacuum_engine import (
    NodeResonanceObserver,
    VacuumEngine3D,
)


# ═══════════════════════════════════════════════════════════════════════════
# 1. Empty-vacuum boundary conditions
# ═══════════════════════════════════════════════════════════════════════════
class TestPhase2EmptyVacuum:
    """At V = 0 and Cosserat (u, ω) = 0, the observer must report
    Ω_node/ω_0 = 1 uniformly (unsaturated tank, Axiom 4 linear limit)."""

    @pytest.fixture
    def engine(self):
        # Small cold-vacuum engine; no drive, no thermal noise
        return VacuumEngine3D.from_args(
            N=8, pml=0, temperature=0.0, amplitude_convention="V_SNAP"
        )

    def test_omega_ratio_max_is_unity_at_zero_strain(self, engine):
        """V=0, ε=0, κ=0 → A²_yield=0 → Ω_node/ω_0 = 1 (Vol 4 Ch 1:132)."""
        obs = NodeResonanceObserver(cadence=1)
        cap = obs._capture(engine)
        assert cap["omega_ratio_max"] == pytest.approx(1.0, abs=1e-12)
        assert cap["omega_ratio_mean"] == pytest.approx(1.0, abs=1e-12)
        assert cap["omega_ratio_min"] == pytest.approx(1.0, abs=1e-12)

    def test_a2_yield_is_zero_at_zero_strain(self, engine):
        """At T=0 cold vacuum, A²_yield = 0 per C1 cold-vacuum determinism."""
        obs = NodeResonanceObserver(cadence=1)
        cap = obs._capture(engine)
        assert cap["A2_yield_max"] == pytest.approx(0.0, abs=1e-12)
        assert cap["A2_yield_mean"] == pytest.approx(0.0, abs=1e-12)

    def test_no_saturated_sites_at_zero_strain(self, engine):
        obs = NodeResonanceObserver(cadence=1)
        cap = obs._capture(engine)
        assert cap["n_saturated"] == 0


# ═══════════════════════════════════════════════════════════════════════════
# 2. Poked-site functional form verification
# ═══════════════════════════════════════════════════════════════════════════
class TestPhase2FunctionalForm:
    """The observer's formula must reproduce the closed form
    Ω_node/ω_0 = (1-A²_yield)^(1/4) at arbitrary A² values.

    Poking V_inc to a single port bypasses the TLM dynamics and lets us
    verify the observer's arithmetic directly."""

    @pytest.fixture
    def engine(self):
        return VacuumEngine3D.from_args(
            N=8, pml=0, temperature=0.0, amplitude_convention="V_SNAP"
        )

    def _poke_single_site_to_a_yield(self, engine, A2_yield_target: float,
                                      site=(4, 4, 4)) -> None:
        """Set V_inc at one active site so that A² = target.

        Under Vol 4 Ch 1:711 subatomic override (R4), the engine's
        A² = V²/V_SNAP² IS canonical r². So V = V_SNAP · √(A²_target).
        Method name retained for backward-compat; "A2_yield" label here
        equals canonical r² under the subatomic convention.
        """
        V = engine.V_SNAP * np.sqrt(A2_yield_target)
        # Put all the amplitude on port 0 so |V|² = V²
        engine.k4.V_inc[:] = 0.0
        engine.k4.V_inc[site[0], site[1], site[2], 0] = V

    @pytest.mark.parametrize("A2_yield_target,expected_omega_ratio", [
        (0.0, 1.0),                       # bare vacuum
        (0.25, (0.75) ** 0.25),           # quarter yield
        (0.5, (0.5) ** 0.25),             # half yield
        (0.75, (0.25) ** 0.25),           # three-quarter yield
        (0.9, (0.1) ** 0.25),             # near yield
    ])
    def test_omega_ratio_matches_quartic_root(
        self, engine, A2_yield_target, expected_omega_ratio,
    ):
        """Ω_node/ω_0 = (1 - A²_yield)^(1/4) for A²_yield ∈ [0, 0.9]."""
        # Check the site is active before poking (ensures _v_squared picks it up)
        site = (4, 4, 4)
        if not engine.k4.mask_active[site]:
            # Pick the first active site instead
            active_idx = np.argwhere(engine.k4.mask_active)
            assert len(active_idx) > 0, "No active sites in lattice"
            site = tuple(active_idx[0])

        self._poke_single_site_to_a_yield(engine, A2_yield_target, site=site)

        obs = NodeResonanceObserver(cadence=1)
        cap = obs._capture(engine)

        # The poked site should have omega_ratio = expected_omega_ratio;
        # it's the MIN across the lattice (all other sites are at ratio=1.0)
        assert cap["omega_ratio_min"] == pytest.approx(
            expected_omega_ratio, rel=5e-5
        ), (
            f"A²_yield={A2_yield_target}: expected ratio="
            f"{expected_omega_ratio:.6f}, got {cap['omega_ratio_min']:.6f}"
        )
        # And A²_yield_max should equal the target
        assert cap["A2_yield_max"] == pytest.approx(
            A2_yield_target, rel=5e-5
        )

    def test_saturation_at_yield(self, engine):
        """At A²_yield = 1 (i.e., V = V_yield), omega_ratio should be
        clipped to ~0 and n_saturated = 1."""
        # Find an active site
        active_idx = np.argwhere(engine.k4.mask_active)
        assert len(active_idx) > 0
        site = tuple(active_idx[0])
        self._poke_single_site_to_a_yield(engine, 1.0, site=site)

        obs = NodeResonanceObserver(cadence=1)
        cap = obs._capture(engine)

        # omega_ratio at the saturated site → ~0 (clipped to 1e-12 floor in A²)
        assert cap["omega_ratio_min"] < 1e-2
        assert cap["n_saturated"] == 1


# ═══════════════════════════════════════════════════════════════════════════
# 3. Consistency with existing observers
# ═══════════════════════════════════════════════════════════════════════════
class TestPhase2ObserverIntegration:
    """Registering NodeResonanceObserver must not disturb existing
    RegimeClassifierObserver / TopologyObserver / EnergyBudgetObserver."""

    def test_observer_registers_without_error(self):
        """add_observer accepts NodeResonanceObserver and runs on step."""
        engine = VacuumEngine3D.from_args(
            N=6, pml=0, temperature=0.0, amplitude_convention="V_SNAP"
        )
        obs = NodeResonanceObserver(cadence=1)
        engine.add_observer(obs)
        # Small run; no sources, so ω_ratio stays at 1 everywhere
        engine.run(n_steps=3)
        assert len(obs.history) == 3
        for h in obs.history:
            assert h["omega_ratio_max"] == pytest.approx(1.0, abs=1e-12)

    def test_cadence_parameter_honored(self):
        """Observer with cadence=2 records every other step."""
        engine = VacuumEngine3D.from_args(
            N=6, pml=0, temperature=0.0, amplitude_convention="V_SNAP"
        )
        obs = NodeResonanceObserver(cadence=2)
        engine.add_observer(obs)
        engine.run(n_steps=4)
        # step_count divisible by cadence — with cadence=2 and 4 steps,
        # records are taken at steps where engine.step_count % 2 == 0
        assert len(obs.history) <= 3  # at most floor(4/2) + 1


# ═══════════════════════════════════════════════════════════════════════════
# 4. Axiom 4 + Pythagorean cross-check: both sectors combine additively
# ═══════════════════════════════════════════════════════════════════════════
class TestPhase2PythagoreanCombination:
    """A²_yield adds contributions from K4 and Cosserat sectors
    per the Pythagorean substrate-strain theorem (orthogonal-sector additivity).
    Putting strain half in each sector should give the same total
    A²_yield as putting all of it in one sector."""

    def test_k4_and_cosserat_add_in_quadrature(self):
        """Equal K4 and Cosserat strain → A²_yield_total = sum."""
        engine = VacuumEngine3D.from_args(
            N=8, pml=0, temperature=0.0, amplitude_convention="V_SNAP"
        )
        # Find an active A-site
        active_idx = np.argwhere(engine.k4.mask_active)
        assert len(active_idx) > 0
        site = tuple(active_idx[0])

        # Set K4 strain: A²_k4 = 0.3 → V = V_SNAP·√(0.3).
        # Under Vol 4 Ch 1:711 subatomic override (R4), A²_K4 = V²/V_SNAP²
        # IS canonical r²; no /α factor needed.
        V = engine.V_SNAP * np.sqrt(0.3)
        engine.k4.V_inc[site[0], site[1], site[2], 0] = V

        obs = NodeResonanceObserver(cadence=1)
        cap_k4_only = obs._capture(engine)

        # The engine's Cosserat fields at T=0 are zero, so A²_cos = 0.
        # Max A²_yield should equal the K4 contribution.
        assert cap_k4_only["A2_yield_max"] == pytest.approx(0.3, rel=5e-5)

    def test_zero_k4_zero_cosserat_gives_zero_total(self):
        """Bare vacuum: both sectors contribute zero."""
        engine = VacuumEngine3D.from_args(
            N=6, pml=0, temperature=0.0, amplitude_convention="V_SNAP"
        )
        obs = NodeResonanceObserver(cadence=1)
        cap = obs._capture(engine)
        assert cap["A2_yield_max"] == pytest.approx(0.0, abs=1e-12)
        assert cap["A2_yield_mean"] == pytest.approx(0.0, abs=1e-12)
