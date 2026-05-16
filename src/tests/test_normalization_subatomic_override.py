"""Phase 3.5.B R4 invariant test — subatomic override convention.

Pins the R4 adjudication (VACUUM_ENGINE_MANUAL §17 A14 r6) that
under Vol 4 Ch 1:711's subatomic-scale override, V_yield ≡ V_SNAP,
and the engine's `A² = V²/V_SNAP²` IS canonical `r²` per Vol 1
Ch 7:12's universal form.

Load-bearing invariants:

1. **V_SNAP serves as V_yield at subatomic scale** — per
   [manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex:711]:
   "Subatomic-scale simulations (e.g., bond energy solvers, Yang-Mills
   confinement) should override with v_yield=V_SNAP (≈ 511 kV)."
   VacuumEngine3D is subatomic-scale (K4 lattice at ℓ_node = Compton
   wavelength); its hardcoded V_SNAP denominator is the subatomic V_yield.

2. **A²_SNAP = 1 IS the Regime IV boundary** — the `_RUPTURE_BOUND_A2 = 1.0`
   constant at [vacuum_engine.py:153] is Vol 1 Ch 7:12 canonical `r² = 1`
   under the subatomic convention; at this scale r=1 is both AVE pair-
   production onset AND Schwinger field (they collapse per Vol 1 Ch
   7:53,115 and Vol 4 Ch 1:711).

3. **Three observers agree on A²_total under subatomic convention** —
   `RegimeClassifierObserver`, `NodeResonanceObserver`, and `BondObserver`
   each compute A²_total = A²_K4 + A²_cos from the same lattice state.
   After the R4 patch (remove `/α` from NodeResonance and BondObserver),
   all three must return the same r² per the Pythagorean substrate-strain
   theorem (A²_total = A²_K4 + A²_cos; orthogonal-sector additivity).

References:
    - research/L3_electron_soliton/50_autoresonant_pair_creation.md §0.1 r3
    - research/L3_electron_soliton/VACUUM_ENGINE_MANUAL.md §17 A14 r6
    - manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex:711
    - manuscript/vol_1_foundations/chapters/07_regime_map.tex:12,:33,:53
"""
from __future__ import annotations

import numpy as np
import pytest

from ave.core.constants import ALPHA, V_SNAP
from ave.topological.vacuum_engine import (
    BondObserver,
    NodeResonanceObserver,
    RegimeClassifierObserver,
    VacuumEngine3D,
    _RUPTURE_BOUND_A2,
    _REGIME_I_BOUND_A2,
    _REGIME_II_BOUND_A2,
)


class TestSubatomicYieldEqualsSnap:
    """Vol 4 Ch 1:711 subatomic override: V_yield = V_SNAP for engine use."""

    def test_engine_v_snap_constant_is_canonical_subatomic_v_yield(self):
        """VacuumEngine3D.V_SNAP (in natural units = 1.0) IS subatomic V_yield.

        The engine's internal `A² = V²/V_SNAP²` calculation uses V_SNAP
        as the Axiom-4 saturation reference. Under Vol 4 Ch 1:711, at
        subatomic scale that V_SNAP serves as v_yield.
        """
        engine = VacuumEngine3D.from_args(
            N=6, pml=0, temperature=0.0, amplitude_convention="V_SNAP"
        )
        # Natural-unit internal V_SNAP = 1.0
        assert engine.V_SNAP == pytest.approx(1.0, abs=1e-12)

    def test_macroscopic_v_yield_differs_from_v_snap_by_sqrt_alpha(self):
        """At macroscopic scale (non-engine context), V_yield = √α · V_SNAP.

        This test documents the scale-dependence. `V_SNAP` as an SI
        physical constant from `constants.py` is the Schwinger / rupture
        voltage (~511 kV). The MACROSCOPIC V_yield is √α times this.
        The SUBATOMIC V_yield override (Vol 4 Ch 1:711) sets V_yield
        back to V_SNAP — which is what the engine uses.
        """
        # SI V_SNAP from constants.py: ~511 kV
        assert V_SNAP > 5.0e5  # 500 kV lower bound
        assert V_SNAP < 5.2e5  # 520 kV upper bound
        # Macroscopic V_yield = √α · V_SNAP ≈ 43.65 kV
        macro_v_yield = np.sqrt(ALPHA) * V_SNAP
        assert macro_v_yield == pytest.approx(4.365e4, rel=1e-3)


class TestRegimeIVBoundaryAtRSquaredOne:
    """`_RUPTURE_BOUND_A2 = 1.0` IS the Regime IV entry under subatomic convention."""

    def test_rupture_bound_equals_one(self):
        """Ax4 Regime IV entry at r² = 1 (Vol 1 Ch 7:33)."""
        assert _RUPTURE_BOUND_A2 == pytest.approx(1.0, abs=1e-15)

    def test_regime_i_to_ii_at_two_alpha(self):
        """Small-signal boundary at r² = 2α (Vol 1 Ch 7:41-44)."""
        assert _REGIME_I_BOUND_A2 == pytest.approx(2.0 * ALPHA, abs=1e-15)

    def test_regime_ii_to_iii_at_three_quarters(self):
        """Yield boundary at r² = 3/4 per Q=ℓ_min=2 (Vol 1 Ch 7:47-51)."""
        assert _REGIME_II_BOUND_A2 == pytest.approx(0.75, abs=1e-15)

    def test_v_equals_vsnap_gives_a2_equals_one(self):
        """V = V_SNAP at a port site → A²_K4 = 1 (Regime IV entry).

        Under subatomic override, this single-port V = V_SNAP injection
        should put that site exactly at the Ax4 rupture boundary.
        """
        engine = VacuumEngine3D.from_args(
            N=6, pml=0, temperature=0.0, amplitude_convention="V_SNAP"
        )
        A_idx = np.argwhere(engine.k4.mask_active)
        assert len(A_idx) > 0
        site = tuple(A_idx[0])

        # Set V = V_SNAP on a single port → V² = V_SNAP² → A²_K4 = 1
        engine.k4.V_inc[site[0], site[1], site[2], 0] = engine.V_SNAP

        V_sq = np.sum(engine.k4.V_inc ** 2, axis=-1)
        A2_k4 = V_sq / (engine.V_SNAP ** 2)
        assert A2_k4[site] == pytest.approx(1.0, abs=1e-12)


class TestThreeObserversAgreeUnderR4:
    """After R4 patch, Regime / NodeResonance / Bond observers agree on A²_total."""

    @pytest.fixture
    def engine_with_k4_poke(self):
        """Engine with a single-port V_inc poke producing A²_K4 ≈ 0.3."""
        engine = VacuumEngine3D.from_args(
            N=8, pml=0, temperature=0.0, amplitude_convention="V_SNAP"
        )
        A_idx = np.argwhere(engine.k4.mask_active)
        assert len(A_idx) > 0
        site = tuple(A_idx[0])
        # V = V_SNAP · √0.3 → A²_K4 = 0.3 at that port (canonical r² under R4)
        engine.k4.V_inc[site[0], site[1], site[2], 0] = (
            engine.V_SNAP * np.sqrt(0.3)
        )
        return engine, site

    def test_regime_and_node_observers_agree_on_a2_total(self, engine_with_k4_poke):
        """RegimeClassifierObserver.max_A2_total matches NodeResonanceObserver.A2_yield_max."""
        engine, site = engine_with_k4_poke

        regime = RegimeClassifierObserver(cadence=1)
        node = NodeResonanceObserver(cadence=1)

        regime_cap = regime._capture(engine)
        node_cap = node._capture(engine)

        # Both should report A²_total = 0.3 at the poked site
        assert regime_cap["max_A2_total"] == pytest.approx(0.3, rel=1e-5)
        assert node_cap["A2_yield_max"] == pytest.approx(0.3, rel=1e-5)
        # And they must agree
        assert regime_cap["max_A2_total"] == pytest.approx(
            node_cap["A2_yield_max"], rel=1e-10
        )

    def test_node_and_bond_observers_agree_on_site_a2(self, engine_with_k4_poke):
        """NodeResonanceObserver.A2_yield_max = BondObserver._compute_A2_yield.max()."""
        engine, site = engine_with_k4_poke

        node = NodeResonanceObserver(cadence=1)
        bond = BondObserver(cadence=1)

        node_cap = node._capture(engine)
        bond_a2 = bond._compute_A2_yield(engine)

        alive = engine.k4.mask_active
        assert node_cap["A2_yield_max"] == pytest.approx(
            float(bond_a2[alive].max()), rel=1e-10
        )

    def test_all_three_observers_report_identical_a2_field(
        self, engine_with_k4_poke,
    ):
        """The underlying A²_total field is identical across all three observers."""
        engine, site = engine_with_k4_poke

        V_sq = np.sum(engine.k4.V_inc ** 2, axis=-1)
        A2_k4 = V_sq / (engine.V_SNAP ** 2)

        # RegimeClassifier computes A²_cos via _cosserat_A_squared; at T=0 it's zero
        # so A²_total should equal A²_k4 exactly
        regime = RegimeClassifierObserver(cadence=1)
        cap = regime._capture(engine)
        assert cap["max_A2_k4"] == pytest.approx(0.3, rel=1e-5)
        assert cap["max_A2_cos"] == pytest.approx(0.0, abs=1e-12)
        assert cap["max_A2_total"] == pytest.approx(
            cap["max_A2_k4"] + cap["max_A2_cos"], rel=1e-10
        )

        # BondObserver's A²_yield field equals A²_k4 at the poked site (A²_cos=0)
        bond = BondObserver(cadence=1)
        bond_a2 = bond._compute_A2_yield(engine)
        assert float(bond_a2[site]) == pytest.approx(0.3, rel=1e-5)


class TestR4PatchEliminatesAlphaConversion:
    """Under R4, NodeResonance and BondObserver do NOT apply /α to A²_K4."""

    def test_node_observer_does_not_divide_by_alpha(self):
        """V set to produce A²_K4 = 0.5 must yield observer.A2_yield_max = 0.5
        (NOT 0.5/α ≈ 68.5, which would indicate the pre-R4 /α conversion)."""
        engine = VacuumEngine3D.from_args(
            N=6, pml=0, temperature=0.0, amplitude_convention="V_SNAP"
        )
        A_idx = np.argwhere(engine.k4.mask_active)
        assert len(A_idx) > 0
        site = tuple(A_idx[0])
        # V = V_SNAP · √0.5 → V²/V_SNAP² = 0.5
        engine.k4.V_inc[site[0], site[1], site[2], 0] = (
            engine.V_SNAP * np.sqrt(0.5)
        )

        obs = NodeResonanceObserver(cadence=1)
        cap = obs._capture(engine)

        # Post-R4: 0.5 (canonical r² under subatomic override).
        # Pre-R4 (with /α): would be 0.5/α ≈ 68.5 → clipped to ~1.
        assert cap["A2_yield_max"] == pytest.approx(0.5, rel=1e-5), (
            f"A2_yield_max = {cap['A2_yield_max']:.4f}; expected 0.5 under R4 "
            f"(pre-R4 /α conversion would give ~{0.5/ALPHA:.1f})"
        )

    def test_bond_observer_does_not_divide_by_alpha(self):
        """Same invariant on BondObserver._compute_A2_yield."""
        engine = VacuumEngine3D.from_args(
            N=6, pml=0, temperature=0.0, amplitude_convention="V_SNAP"
        )
        A_idx = np.argwhere(engine.k4.mask_active)
        assert len(A_idx) > 0
        site = tuple(A_idx[0])
        engine.k4.V_inc[site[0], site[1], site[2], 0] = (
            engine.V_SNAP * np.sqrt(0.5)
        )

        obs = BondObserver(cadence=1)
        a2 = obs._compute_A2_yield(engine)
        assert float(a2[site]) == pytest.approx(0.5, rel=1e-5), (
            f"BondObserver A²[site] = {float(a2[site]):.4f}; expected 0.5 "
            f"under R4 (pre-R4 /α conversion would give ~{0.5/ALPHA:.1f})"
        )
