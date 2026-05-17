"""
Pre-registered unit tests for per-bond flux linkage Φ_link — Stage 6 Phase 3.

Pins the K4-TLM engine's new per-bond magnetic flux linkage state:

    Φ_link[A_site, port] := ∫ V_bond(t) dt       where
    V_bond = ½(V_ref[A, port] + V_ref[B_shifted, port])

per doc 54_ §3 (`p_vac = Φ·ξ_topo` from Vol 4 Ch 11:38; memristance
`M(q) = dΦ/dq` from Vol 4 Ch 1:223-227).

Tests:
  1. Initial state: all Φ_link = 0
  2. reset_phi_link() zeros the field
  3. Scatter does not touch Φ_link (only connect does)
  4. Constant single-port injection accumulates Φ_link monotonically
  5. Observer reads Φ_link consistently with direct array access
  6. Observer partitions bonds by endpoint saturation correctly
  7. Backwards compat: existing RegimeClassifier / Topology / Energy
     observers still run with BondObserver registered

Reference:
  - src/ave/core/k4_tlm.py::K4Lattice3D.Phi_link
  - src/ave/core/k4_tlm.py::_connect_all (accumulation)
  - src/ave/topological/vacuum_engine.py::BondObserver
  - research/_archive/L3_electron_soliton/54_pair_production_axiom_derivation.md §3
  - manuscript/predictions.yaml::P_phase3_flux_tube

Phase 3 design note: end-to-end flux-tube persistence verification
(the P_phase3_flux_tube headline — "Φ_link persists ≥ 10 Compton
periods between saturated endpoints") runs in the driver
src/scripts/vol_1_foundations/flux_tube_persistence.py, not in
these unit tests. These smoke tests lock the accumulation arithmetic
and observer plumbing.
"""
from __future__ import annotations

import numpy as np
import pytest

from ave.core.k4_tlm import K4Lattice3D
from ave.topological.vacuum_engine import (
    BondObserver,
    EnergyBudgetObserver,
    NodeResonanceObserver,
    RegimeClassifierObserver,
    TopologyObserver,
    VacuumEngine3D,
)


# ═══════════════════════════════════════════════════════════════════════════
# 1. Initial state and reset
# ═══════════════════════════════════════════════════════════════════════════
class TestPhase3InitialState:
    """A fresh K4Lattice3D starts with zero flux linkage."""

    def test_phi_link_initialized_zero(self):
        lat = K4Lattice3D(nx=6, ny=6, nz=6, pml_thickness=0)
        assert lat.Phi_link.shape == (6, 6, 6, 4)
        assert np.all(lat.Phi_link == 0.0)

    def test_phi_link_dtype_is_float(self):
        lat = K4Lattice3D(nx=4, ny=4, nz=4, pml_thickness=0)
        assert lat.Phi_link.dtype == float

    def test_reset_phi_link_zeros(self):
        lat = K4Lattice3D(nx=6, ny=6, nz=6, pml_thickness=0)
        # Poke some flux in
        lat.Phi_link[0, 0, 0, 0] = 1.23
        lat.Phi_link[2, 2, 2, 1] = -0.45
        assert lat.Phi_link.sum() != 0.0
        lat.reset_phi_link()
        assert np.all(lat.Phi_link == 0.0)


# ═══════════════════════════════════════════════════════════════════════════
# 2. Accumulation semantics
# ═══════════════════════════════════════════════════════════════════════════
class TestPhase3Accumulation:
    """_connect_all adds V_avg·dt per bond per step; _scatter_all alone
    does not touch Φ_link."""

    def test_scatter_alone_does_not_change_phi(self):
        """Running _scatter_all without _connect_all leaves Φ_link untouched."""
        lat = K4Lattice3D(nx=6, ny=6, nz=6, pml_thickness=0)
        # Inject at an A-site
        lat.V_inc[0, 0, 0, 0] = 0.1
        lat._scatter_all()
        assert np.all(lat.Phi_link == 0.0), (
            "Scatter alone should not change Phi_link"
        )

    def test_connect_without_drive_keeps_phi_zero(self):
        """With V_inc = V_ref = 0 initially, a single step produces no flux."""
        lat = K4Lattice3D(nx=6, ny=6, nz=6, pml_thickness=0)
        lat.step()
        assert np.all(lat.Phi_link == 0.0)

    def test_sustained_injection_accumulates_phi(self):
        """Injecting a constant signal every step grows Phi_link."""
        lat = K4Lattice3D(nx=6, ny=6, nz=6, pml_thickness=0)
        # Need V_inc to be non-zero right before each scatter.
        # V_inc gets consumed by scatter+connect and replaced with the
        # incoming reflection; we re-inject each step.
        amp = 0.01
        magnitudes_over_time = []
        for _ in range(10):
            lat.V_inc[0, 0, 0, 0] += amp
            lat.step()
            magnitudes_over_time.append(float(np.max(np.abs(lat.Phi_link))))

        # Φ magnitude should grow from 0 during the first few steps as the
        # injected signal propagates and reflects
        assert magnitudes_over_time[0] >= 0.0
        assert magnitudes_over_time[-1] > magnitudes_over_time[0], (
            f"Phi_link should grow under sustained drive; got "
            f"{magnitudes_over_time}"
        )

    def test_phi_sign_follows_drive_sign(self):
        """Injecting +V vs -V gives opposite-sign Φ accumulation."""
        lat_plus = K4Lattice3D(nx=6, ny=6, nz=6, pml_thickness=0)
        lat_minus = K4Lattice3D(nx=6, ny=6, nz=6, pml_thickness=0)
        for _ in range(5):
            lat_plus.V_inc[0, 0, 0, 0] += 0.01
            lat_minus.V_inc[0, 0, 0, 0] -= 0.01
            lat_plus.step()
            lat_minus.step()

        # Φ_link should have opposite signs (within numerical tolerance)
        phi_plus = lat_plus.Phi_link
        phi_minus = lat_minus.Phi_link
        # Bonds with non-trivial flux should be anti-correlated
        nontrivial = np.abs(phi_plus) > 1e-15
        if nontrivial.any():
            signs_plus = np.sign(phi_plus[nontrivial])
            signs_minus = np.sign(phi_minus[nontrivial])
            # Sum of products should be negative (opposite signs)
            agreement = np.mean(signs_plus * signs_minus)
            assert agreement < -0.5, (
                f"Opposite drives should give opposite-sign Φ; "
                f"got sign-correlation {agreement}"
            )


# ═══════════════════════════════════════════════════════════════════════════
# 3. BondObserver reads Φ_link
# ═══════════════════════════════════════════════════════════════════════════
class TestPhase3BondObserver:
    """BondObserver accurately reports Φ_link statistics."""

    @pytest.fixture
    def engine(self):
        return VacuumEngine3D.from_args(
            N=8, pml=0, temperature=0.0, amplitude_convention="V_SNAP"
        )

    def test_observer_on_empty_vacuum(self, engine):
        """At (V, u, ω) = 0, phi_abs_max = 0 and all bonds are unsaturated."""
        obs = BondObserver(cadence=1)
        cap = obs._capture(engine)
        assert cap["phi_abs_max"] == 0.0
        assert cap["phi_rms"] == 0.0
        assert cap["n_saturated_bonds"] == 0
        assert cap["n_unsaturated_bonds"] > 0

    def test_observer_reads_direct_poke(self, engine):
        """Directly setting Phi_link at an A-site shows up in phi_abs_max."""
        # Find an A-site
        A_idx = np.argwhere(engine.k4.mask_A)
        assert len(A_idx) > 0
        site = tuple(A_idx[0])
        engine.k4.Phi_link[site[0], site[1], site[2], 2] = 0.567

        obs = BondObserver(cadence=1)
        cap = obs._capture(engine)
        assert cap["phi_abs_max"] == pytest.approx(0.567, rel=1e-12)

    def test_observer_registers_and_runs(self):
        """BondObserver registered via add_observer records each step."""
        engine = VacuumEngine3D.from_args(
            N=6, pml=0, temperature=0.0, amplitude_convention="V_SNAP"
        )
        obs = BondObserver(cadence=1)
        engine.add_observer(obs)
        engine.run(n_steps=3)
        assert len(obs.history) == 3
        for h in obs.history:
            assert "phi_abs_max" in h
            assert "phi_at_saturated_bonds_rms" in h

    def test_observer_partitions_by_saturation(self, engine):
        """Forcing one site past saturation puts its bonds in the saturated
        bucket; other bonds stay in the unsaturated bucket."""
        # Poke V at an A-site to saturate it. Under Vol 4 Ch 1:711 subatomic
        # override (R4), V_yield ≡ V_SNAP; setting V = V_SNAP gives canonical
        # A² = V²/V_SNAP² = 1 exactly (Regime IV entry boundary).
        A_idx = np.argwhere(engine.k4.mask_A)
        site = tuple(A_idx[0])
        V = engine.V_SNAP  # Exactly V_yield under subatomic override → A² = 1
        engine.k4.V_inc[site[0], site[1], site[2], 0] = V
        # Also set flux at that bond
        engine.k4.Phi_link[site[0], site[1], site[2], 0] = 2.0

        # Note: at this A-site, port 0, the BOND endpoint at the B-neighbor
        # is NOT saturated (it's bare vacuum). So the bond is "partially
        # saturated" → goes in the unsaturated bucket under the "BOTH
        # endpoints saturated" rule. This is intentional: the bucket labels
        # flux tubes that have FULL endpoint confinement.
        obs = BondObserver(cadence=1, saturation_frac=0.5)
        cap = obs._capture(engine)
        # Since only one endpoint is saturated, phi=2.0 goes to unsat bucket
        assert cap["phi_at_unsaturated_bonds_rms"] > 0.0
        # With one site saturated and its B-neighbor unsaturated, n_saturated_bonds = 0
        assert cap["n_saturated_bonds"] == 0


# ═══════════════════════════════════════════════════════════════════════════
# 4. Backwards compatibility
# ═══════════════════════════════════════════════════════════════════════════
class TestPhase3BackwardsCompat:
    """Registering BondObserver doesn't disturb existing observers or
    break the engine's step sequence."""

    def test_bond_observer_with_regime_observer(self):
        """Both observers record consistently on a short run."""
        engine = VacuumEngine3D.from_args(
            N=6, pml=0, temperature=0.0, amplitude_convention="V_SNAP"
        )
        regime_obs = RegimeClassifierObserver(cadence=1)
        bond_obs = BondObserver(cadence=1)
        engine.add_observer(regime_obs)
        engine.add_observer(bond_obs)
        engine.run(n_steps=3)
        assert len(regime_obs.history) == 3
        assert len(bond_obs.history) == 3
        # Empty run — no saturation, no flux
        for bh in bond_obs.history:
            assert bh["phi_abs_max"] == 0.0
        for rh in regime_obs.history:
            assert rh["max_A2_total"] == 0.0

    def test_bond_observer_with_all_other_observers(self):
        """Full observer stack including BondObserver runs without error."""
        engine = VacuumEngine3D.from_args(
            N=6, pml=0, temperature=0.0, amplitude_convention="V_SNAP"
        )
        observers = [
            RegimeClassifierObserver(cadence=1),
            NodeResonanceObserver(cadence=1),
            TopologyObserver(cadence=1, threshold_frac=0.3),
            EnergyBudgetObserver(cadence=1),
            BondObserver(cadence=1),
        ]
        for o in observers:
            engine.add_observer(o)
        engine.run(n_steps=2)
        for o in observers:
            assert len(o.history) == 2, (
                f"{type(o).__name__} did not record 2 steps"
            )

    def test_existing_phi_link_state_persists_across_engine_steps(self):
        """Poke Phi_link, run one step with no drive, flux should remain
        (possibly modified by one step's accumulation from residual V_ref
        but at this scale negligible)."""
        engine = VacuumEngine3D.from_args(
            N=6, pml=0, temperature=0.0, amplitude_convention="V_SNAP"
        )
        A_idx = np.argwhere(engine.k4.mask_A)
        site = tuple(A_idx[0])
        engine.k4.Phi_link[site[0], site[1], site[2], 1] = 1.5
        engine.run(n_steps=1)
        # With no drive, the bond voltage contribution is zero so flux
        # should be ~unchanged
        assert engine.k4.Phi_link[site[0], site[1], site[2], 1] == pytest.approx(
            1.5, abs=1e-10
        )
