"""
Pre-registered unit tests for PairNucleationGate — Stage 6 Phase 5.

Pins the observer-with-side-effect gate that nucleates Kelvin-style
vortex pairs inside Bingham-plastic capsules per
[doc 54_ §7](research/_archive/L3_electron_soliton/54_pair_production_axiom_derivation.md):

    C1: both endpoints of an A→B bond reach Meissner saturation
        A²_μ(r_A) ≥ sat_frac  AND  A²_μ(r_B) ≥ sat_frac
    C2: autoresonant lock — a drive frequency ω_drive matches
        the Duffing-softened tank at r_A:
        |Ω_node(r_A) − ω_drive| < δ_lock  with  δ_lock = ω_drive·α (Q=1/α)

When C1 ∧ C2 fire, the gate injects:
    ω_A = -amp · p̂_bond     (LH Beltrami vortex, point-rotation)
    ω_B = +amp · p̂_bond     (RH Beltrami vortex, point-rotation)
    Φ_link[A, port] = ±Φ_critical
    ω̇ zeroed at both endpoints (pair born at rest)

Tests are smoke-tier: we exercise the gate-logic + injection-profile
code paths against engine state that we directly manipulate (or monkeypatch
the two expensive helper methods to feed synthetic fields). The full
P_phase5_nucleation headline — "Beltrami pair persists ≥ 10 Compton
periods post-drive-shutoff" — runs in a separate driver script
(src/scripts/vol_1_foundations/phase5_pair_nucleation.py).

Reference:
  - src/ave/topological/vacuum_engine.py::PairNucleationGate
  - research/_archive/L3_electron_soliton/54_pair_production_axiom_derivation.md §7
  - research/_archive/L3_electron_soliton/27_step6_phase_space_Q.md (Q=1/α)
  - manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex:189-203
    (Bingham plastic / TVS Zener / Slipstream)
"""
from __future__ import annotations

import numpy as np
import pytest

from ave.core.constants import ALPHA
from ave.topological.vacuum_engine import (
    AutoresonantCWSource,
    PairNucleationGate,
    VacuumEngine3D,
)


# ═══════════════════════════════════════════════════════════════════════════
# 1. Construction defaults
# ═══════════════════════════════════════════════════════════════════════════
class TestPhase5Construction:
    """The gate's zero-free-parameter defaults match axiom-native values."""

    def test_default_delta_lock_fraction_is_alpha(self):
        """δ_lock = α·ω_drive (Q = 1/α per doc 27_)."""
        gate = PairNucleationGate()
        assert gate.delta_lock_fraction == pytest.approx(float(ALPHA), rel=1e-12)

    def test_default_injection_amplitude_is_sqrt2(self):
        """|ω| = √2 ⇒ ½·I_ω·|ω|² = 1 = m_e c² (I_ω=1 natural units)."""
        gate = PairNucleationGate()
        assert gate.injection_amplitude == pytest.approx(np.sqrt(2.0), rel=1e-12)

    def test_default_saturation_frac_is_0p95(self):
        """sat_frac=0.95 default for numerical safety (A²_μ=1 is Ax4 rupture)."""
        gate = PairNucleationGate()
        assert gate.saturation_frac == pytest.approx(0.95, rel=1e-12)

    def test_default_phi_critical_is_one(self):
        """Default Φ_critical = 1.0 (natural-unit V_SNAP·τ_node)."""
        gate = PairNucleationGate()
        assert gate.phi_critical == pytest.approx(1.0, rel=1e-12)

    def test_nucleated_bonds_starts_empty(self):
        gate = PairNucleationGate()
        assert gate._nucleated_bonds == set()
        assert gate._total_firings == 0

    def test_port_vectors_are_tetrahedral(self):
        """Class constant must match K4 p0..p3 tetrahedral layout."""
        expected = np.array([
            [+1, +1, +1],
            [+1, -1, -1],
            [-1, +1, -1],
            [-1, -1, +1],
        ], dtype=float)
        np.testing.assert_array_equal(PairNucleationGate._PORT_VECTORS, expected)

    def test_custom_overrides_respected(self):
        gate = PairNucleationGate(
            cadence=5,
            saturation_frac=0.8,
            delta_lock_fraction=1e-2,
            injection_amplitude=1.0,
            phi_critical=0.5,
        )
        assert gate.cadence == 5
        assert gate.saturation_frac == pytest.approx(0.8)
        assert gate.delta_lock_fraction == pytest.approx(1e-2)
        assert gate.injection_amplitude == pytest.approx(1.0)
        assert gate.phi_critical == pytest.approx(0.5)


# ═══════════════════════════════════════════════════════════════════════════
# 2. Idle conditions — cold vacuum / no drive
# ═══════════════════════════════════════════════════════════════════════════
class TestPhase5IdleConditions:
    """The gate must stay dormant under conditions where either C1 or C2
    is impossible."""

    @pytest.fixture
    def cold_engine(self):
        return VacuumEngine3D.from_args(
            N=8, pml=0, temperature=0.0, amplitude_convention="V_SNAP",
        )

    def test_no_firing_on_cold_vacuum_with_no_source(self, cold_engine):
        """T=0, no drive, no strain → gate inactive."""
        gate = PairNucleationGate(cadence=1)
        cap = gate._capture(cold_engine)
        assert cap["n_fired_this_step"] == 0
        assert cap["n_nucleated_total"] == 0
        assert cap["gate_active"] is False

    def test_no_firing_without_drive_even_if_saturated(self, cold_engine, monkeypatch):
        """C2 needs drive_freqs. If no sources registered, gate stays idle
        regardless of A²_μ state."""
        gate = PairNucleationGate(cadence=1)
        # Force all sites to full saturation
        N = cold_engine.N
        monkeypatch.setattr(
            gate, "_compute_A2_mu",
            lambda eng: np.ones((N, N, N), dtype=float),
        )
        monkeypatch.setattr(
            gate, "_compute_Omega_node",
            lambda eng: np.ones((N, N, N), dtype=float),
        )
        cap = gate._capture(cold_engine)
        assert cap["n_fired_this_step"] == 0
        assert cap["gate_active"] is False

    def test_no_firing_with_drive_but_empty_field(self, cold_engine):
        """Source registered, A²_μ = 0 everywhere → C1 fails → no firing."""
        src = AutoresonantCWSource(
            x0=3, direction=(1.0, 0.0, 0.0),
            amplitude=0.01, omega=2.0 * np.pi / 3.5,
            sigma_yz=2.0, t_ramp=1.0, t_sustain=1.0,
        )
        cold_engine.add_source(src)
        gate = PairNucleationGate(cadence=1)
        cap = gate._capture(cold_engine)
        assert cap["n_fired_this_step"] == 0
        assert cap["n_nucleated_total"] == 0


# ═══════════════════════════════════════════════════════════════════════════
# 3. Gate-logic decision table (C1, C2, C1∧C2)
# ═══════════════════════════════════════════════════════════════════════════
class TestPhase5GateLogic:
    """Monkeypatch the expensive per-site field helpers to directly test
    the C1 ∧ C2 decision boundary."""

    @pytest.fixture
    def engine_with_source(self):
        engine = VacuumEngine3D.from_args(
            N=6, pml=0, temperature=0.0, amplitude_convention="V_SNAP",
        )
        src = AutoresonantCWSource(
            x0=3, direction=(1.0, 0.0, 0.0),
            amplitude=0.01, omega=2.0 * np.pi / 3.5,
            sigma_yz=2.0, t_ramp=1.0, t_sustain=1.0,
        )
        engine.add_source(src)
        return engine, src

    def _patch_fields(self, gate, A2_mu_field, omega_node_field, monkeypatch):
        monkeypatch.setattr(gate, "_compute_A2_mu", lambda eng: A2_mu_field)
        monkeypatch.setattr(gate, "_compute_Omega_node", lambda eng: omega_node_field)

    def test_c1_fails_single_endpoint_unsaturated(
        self, engine_with_source, monkeypatch,
    ):
        """A-site saturated, B-site unsaturated → no firing."""
        engine, src = engine_with_source
        gate = PairNucleationGate(cadence=1)
        N = engine.N
        A2 = np.zeros((N, N, N))
        # Find a bond pair and saturate just A
        bonds = gate._candidate_bonds(engine)
        assert len(bonds) > 0
        A_idx, port, B_idx = bonds[0]
        A2[A_idx] = 1.0  # saturated
        A2[B_idx] = 0.1  # NOT saturated
        # Ω_node at A locked to drive (but C1 fails, so this shouldn't matter)
        Omega_node = np.full((N, N, N), float(src._omega_current or src.omega))
        self._patch_fields(gate, A2, Omega_node, monkeypatch)

        cap = gate._capture(engine)
        assert cap["n_fired_this_step"] == 0
        assert gate._total_firings == 0

    def test_c2_fails_drive_far_from_node_resonance(
        self, engine_with_source, monkeypatch,
    ):
        """Both endpoints saturated but drive freq far outside δ_lock."""
        engine, src = engine_with_source
        gate = PairNucleationGate(cadence=1)
        N = engine.N
        A2 = np.ones((N, N, N))  # Every site saturated
        # Set Ω_node far from ω_drive (10x higher → well outside δ_lock = α·ω)
        omega_drive = float(src.omega)
        Omega_node = np.full((N, N, N), 10.0 * omega_drive)
        self._patch_fields(gate, A2, Omega_node, monkeypatch)

        cap = gate._capture(engine)
        assert cap["n_fired_this_step"] == 0
        assert gate._total_firings == 0

    def test_c1_and_c2_both_met_fires(
        self, engine_with_source, monkeypatch,
    ):
        """Both endpoints saturated + Ω_node locked to drive → gate fires."""
        engine, src = engine_with_source
        gate = PairNucleationGate(cadence=1)
        N = engine.N
        A2 = np.ones((N, N, N))
        omega_drive = float(src.omega)
        Omega_node = np.full((N, N, N), omega_drive)  # perfectly locked
        self._patch_fields(gate, A2, Omega_node, monkeypatch)

        cap = gate._capture(engine)
        assert cap["n_fired_this_step"] >= 1
        assert gate._total_firings >= 1
        assert cap["gate_active"] is True

    def test_delta_lock_edge_just_inside(
        self, engine_with_source, monkeypatch,
    ):
        """Ω_node = ω·(1 + 0.5·α) is inside δ_lock = α·ω → fires."""
        engine, src = engine_with_source
        gate = PairNucleationGate(cadence=1)
        N = engine.N
        A2 = np.ones((N, N, N))
        omega_drive = float(src.omega)
        # Edge of the lock-band, 50% inside
        Omega_node = np.full((N, N, N), omega_drive * (1.0 + 0.5 * ALPHA))
        self._patch_fields(gate, A2, Omega_node, monkeypatch)

        cap = gate._capture(engine)
        assert cap["n_fired_this_step"] >= 1

    def test_delta_lock_edge_just_outside(
        self, engine_with_source, monkeypatch,
    ):
        """Ω_node = ω·(1 + 2·α) is outside δ_lock = α·ω → no fire."""
        engine, src = engine_with_source
        gate = PairNucleationGate(cadence=1)
        N = engine.N
        A2 = np.ones((N, N, N))
        omega_drive = float(src.omega)
        Omega_node = np.full((N, N, N), omega_drive * (1.0 + 2.0 * ALPHA))
        self._patch_fields(gate, A2, Omega_node, monkeypatch)

        cap = gate._capture(engine)
        assert cap["n_fired_this_step"] == 0


# ═══════════════════════════════════════════════════════════════════════════
# 4. Re-fire prevention
# ═══════════════════════════════════════════════════════════════════════════
class TestPhase5RefirePrevention:
    """Once a bond fires, it must never fire again in the same engine lifetime."""

    def test_bond_fires_exactly_once_across_repeated_captures(self, monkeypatch):
        engine = VacuumEngine3D.from_args(
            N=6, pml=0, temperature=0.0, amplitude_convention="V_SNAP",
        )
        src = AutoresonantCWSource(
            x0=3, direction=(1.0, 0.0, 0.0),
            amplitude=0.01, omega=2.0 * np.pi / 3.5,
            sigma_yz=2.0, t_ramp=1.0, t_sustain=1.0,
        )
        engine.add_source(src)
        gate = PairNucleationGate(cadence=1)
        N = engine.N
        A2 = np.ones((N, N, N))
        Omega_node = np.full((N, N, N), float(src.omega))
        monkeypatch.setattr(gate, "_compute_A2_mu", lambda eng: A2)
        monkeypatch.setattr(gate, "_compute_Omega_node", lambda eng: Omega_node)

        cap1 = gate._capture(engine)
        first_firings = gate._total_firings
        assert first_firings >= 1

        # Second call: same saturated state → all bonds already in _nucleated_bonds
        cap2 = gate._capture(engine)
        assert cap2["n_fired_this_step"] == 0
        assert gate._total_firings == first_firings


# ═══════════════════════════════════════════════════════════════════════════
# 5. Injection profile — LH/RH Beltrami + Φ_link + ω̇=0
# ═══════════════════════════════════════════════════════════════════════════
class TestPhase5InjectionProfile:
    """_inject_pair writes the correct point-rotation Beltrami + Φ."""

    @pytest.fixture
    def engine(self):
        return VacuumEngine3D.from_args(
            N=6, pml=0, temperature=0.0, amplitude_convention="V_SNAP",
        )

    def test_omega_lh_at_A_rh_at_B(self, engine):
        """ω_A antiparallel, ω_B parallel to p̂_bond (LH at A, RH at B)."""
        gate = PairNucleationGate()
        # Pick the first candidate bond
        bonds = gate._candidate_bonds(engine)
        assert len(bonds) > 0
        A_idx, port, B_idx = bonds[0]
        p_vec = PairNucleationGate._PORT_VECTORS[port]
        p_hat = p_vec / np.linalg.norm(p_vec)

        gate._inject_pair(engine, A_idx, port, B_idx)

        omega_A = engine.cos.omega[A_idx[0], A_idx[1], A_idx[2], :]
        omega_B = engine.cos.omega[B_idx[0], B_idx[1], B_idx[2], :]

        amp = gate.injection_amplitude
        np.testing.assert_allclose(omega_A, -amp * p_hat, rtol=1e-12, atol=1e-15)
        np.testing.assert_allclose(omega_B, +amp * p_hat, rtol=1e-12, atol=1e-15)

    def test_omega_magnitude_is_sqrt2_at_both_endpoints(self, engine):
        """|ω| = √2 → ½·I_ω·|ω|² = 1 = m_e c² rest energy."""
        gate = PairNucleationGate()
        A_idx, port, B_idx = gate._candidate_bonds(engine)[0]
        gate._inject_pair(engine, A_idx, port, B_idx)

        mag_A = np.linalg.norm(engine.cos.omega[A_idx[0], A_idx[1], A_idx[2], :])
        mag_B = np.linalg.norm(engine.cos.omega[B_idx[0], B_idx[1], B_idx[2], :])
        assert mag_A == pytest.approx(np.sqrt(2.0), rel=1e-12)
        assert mag_B == pytest.approx(np.sqrt(2.0), rel=1e-12)

    def test_omega_dot_zeroed_at_injection_sites(self, engine):
        """Pair born at rest: ω̇ = 0 at both A and B endpoints."""
        gate = PairNucleationGate()
        A_idx, port, B_idx = gate._candidate_bonds(engine)[0]
        # Poke some non-zero ω_dot first
        engine.cos.omega_dot[A_idx[0], A_idx[1], A_idx[2], :] = 7.0
        engine.cos.omega_dot[B_idx[0], B_idx[1], B_idx[2], :] = -3.0

        gate._inject_pair(engine, A_idx, port, B_idx)

        assert np.all(engine.cos.omega_dot[A_idx[0], A_idx[1], A_idx[2], :] == 0.0)
        assert np.all(engine.cos.omega_dot[B_idx[0], B_idx[1], B_idx[2], :] == 0.0)

    def test_phi_link_magnitude_at_fired_bond(self, engine):
        """|Φ_link[A, port]| = phi_critical after injection."""
        gate = PairNucleationGate(phi_critical=0.7)
        A_idx, port, B_idx = gate._candidate_bonds(engine)[0]
        gate._inject_pair(engine, A_idx, port, B_idx)
        phi = engine.k4.Phi_link[A_idx[0], A_idx[1], A_idx[2], port]
        assert abs(phi) == pytest.approx(0.7, rel=1e-12)

    def test_phi_sign_alternates_by_port(self, engine):
        """First-pass: sign = +1 for even port, -1 for odd port."""
        gate = PairNucleationGate(phi_critical=1.0)
        # Scan bonds until we find one on each port index
        seen = {}
        for (A_idx, port, B_idx) in gate._candidate_bonds(engine):
            if port not in seen:
                # Use a fresh copy of engine per port to avoid state bleed
                eng_fresh = VacuumEngine3D.from_args(
                    N=6, pml=0, temperature=0.0, amplitude_convention="V_SNAP",
                )
                g = PairNucleationGate(phi_critical=1.0)
                g._inject_pair(eng_fresh, A_idx, port, B_idx)
                seen[port] = eng_fresh.k4.Phi_link[
                    A_idx[0], A_idx[1], A_idx[2], port
                ]
                if len(seen) == 4:
                    break
        for port, phi_val in seen.items():
            expected_sign = +1.0 if (port % 2 == 0) else -1.0
            assert np.sign(phi_val) == expected_sign, (
                f"Port {port}: expected sign {expected_sign}, got Φ={phi_val}"
            )


# ═══════════════════════════════════════════════════════════════════════════
# 6. Candidate bonds — K4 lattice topology
# ═══════════════════════════════════════════════════════════════════════════
class TestPhase5CandidateBonds:
    """_candidate_bonds returns in-bounds (A_idx, port, B_idx) tuples with
    A_idx on mask_A, B_idx on mask_B, and B = A + p_port."""

    @pytest.fixture
    def engine(self):
        return VacuumEngine3D.from_args(
            N=6, pml=0, temperature=0.0, amplitude_convention="V_SNAP",
        )

    def test_all_bonds_have_A_on_mask_A(self, engine):
        gate = PairNucleationGate()
        bonds = gate._candidate_bonds(engine)
        assert len(bonds) > 0
        for A_idx, port, B_idx in bonds:
            assert engine.k4.mask_A[A_idx], (
                f"A_idx={A_idx} not on mask_A"
            )

    def test_all_bonds_have_B_on_mask_B(self, engine):
        gate = PairNucleationGate()
        bonds = gate._candidate_bonds(engine)
        for A_idx, port, B_idx in bonds:
            assert engine.k4.mask_B[B_idx], (
                f"B_idx={B_idx} not on mask_B"
            )

    def test_B_equals_A_plus_port_vector(self, engine):
        gate = PairNucleationGate()
        for A_idx, port, B_idx in gate._candidate_bonds(engine):
            p = PairNucleationGate._PORT_VECTORS[port].astype(int)
            expected_B = tuple(np.array(A_idx) + p)
            assert B_idx == expected_B

    def test_no_out_of_bounds_bonds(self, engine):
        gate = PairNucleationGate()
        N = engine.N
        for A_idx, port, B_idx in gate._candidate_bonds(engine):
            for axis in range(3):
                assert 0 <= B_idx[axis] < N


# ═══════════════════════════════════════════════════════════════════════════
# 7. Drive frequency extraction
# ═══════════════════════════════════════════════════════════════════════════
class TestPhase5DriveFrequencies:
    """_drive_frequencies pulls ω from any registered source."""

    def test_empty_when_no_sources(self):
        engine = VacuumEngine3D.from_args(
            N=6, pml=0, temperature=0.0, amplitude_convention="V_SNAP",
        )
        gate = PairNucleationGate()
        assert gate._drive_frequencies(engine) == []

    def test_returns_autoresonant_omega_current(self):
        engine = VacuumEngine3D.from_args(
            N=6, pml=0, temperature=0.0, amplitude_convention="V_SNAP",
        )
        src = AutoresonantCWSource(
            x0=3, direction=(1.0, 0.0, 0.0),
            amplitude=0.01, omega=2.0 * np.pi / 3.5,
            sigma_yz=2.0, t_ramp=1.0, t_sustain=1.0,
        )
        engine.add_source(src)
        gate = PairNucleationGate()
        freqs = gate._drive_frequencies(engine)
        assert len(freqs) == 1
        assert freqs[0] == pytest.approx(
            float(src._omega_current or src.omega), rel=1e-10
        )


# ═══════════════════════════════════════════════════════════════════════════
# 8. Engine integration — gate as registered observer
# ═══════════════════════════════════════════════════════════════════════════
class TestPhase5EngineIntegration:
    """The gate registers as a standard observer and runs without disturbing
    the rest of the engine."""

    def test_gate_registers_and_runs_on_cold_vacuum(self):
        engine = VacuumEngine3D.from_args(
            N=6, pml=0, temperature=0.0, amplitude_convention="V_SNAP",
        )
        gate = PairNucleationGate(cadence=1)
        engine.add_observer(gate)
        engine.run(n_steps=2)
        assert len(gate.history) == 2
        # Cold vacuum + no source → all idle
        for cap in gate.history:
            assert cap["n_fired_this_step"] == 0

    def test_no_nan_or_inf_post_injection(self):
        """After firing, the engine state must remain finite."""
        engine = VacuumEngine3D.from_args(
            N=6, pml=0, temperature=0.0, amplitude_convention="V_SNAP",
        )
        gate = PairNucleationGate()
        A_idx, port, B_idx = gate._candidate_bonds(engine)[0]
        gate._inject_pair(engine, A_idx, port, B_idx)
        assert np.all(np.isfinite(engine.cos.omega))
        assert np.all(np.isfinite(engine.cos.omega_dot))
        assert np.all(np.isfinite(engine.k4.Phi_link))

    def test_engine_can_step_after_injection(self):
        """Engine must advance one step post-injection without errors."""
        engine = VacuumEngine3D.from_args(
            N=6, pml=0, temperature=0.0, amplitude_convention="V_SNAP",
        )
        gate = PairNucleationGate()
        A_idx, port, B_idx = gate._candidate_bonds(engine)[0]
        gate._inject_pair(engine, A_idx, port, B_idx)
        # One step — should not NaN or raise
        engine.step()
        assert np.all(np.isfinite(engine.cos.omega))
        assert np.all(np.isfinite(engine.k4.V_inc))


# ═══════════════════════════════════════════════════════════════════════════
# 9. Capture dict contract
# ═══════════════════════════════════════════════════════════════════════════
class TestPhase5CaptureContract:
    """The capture dict must contain the required keys for downstream
    diagnostics and P_phase5_nucleation."""

    def test_idle_capture_has_required_keys(self):
        engine = VacuumEngine3D.from_args(
            N=6, pml=0, temperature=0.0, amplitude_convention="V_SNAP",
        )
        gate = PairNucleationGate()
        cap = gate._capture(engine)
        for key in ("t", "n_nucleated_total", "n_fired_this_step",
                    "fired_bonds", "gate_active"):
            assert key in cap, f"capture missing key: {key}"

    def test_active_capture_has_required_keys(self, monkeypatch):
        engine = VacuumEngine3D.from_args(
            N=6, pml=0, temperature=0.0, amplitude_convention="V_SNAP",
        )
        src = AutoresonantCWSource(
            x0=3, direction=(1.0, 0.0, 0.0),
            amplitude=0.01, omega=2.0 * np.pi / 3.5,
            sigma_yz=2.0, t_ramp=1.0, t_sustain=1.0,
        )
        engine.add_source(src)
        gate = PairNucleationGate()
        N = engine.N
        monkeypatch.setattr(gate, "_compute_A2_mu",
                            lambda eng: np.ones((N, N, N)))
        monkeypatch.setattr(gate, "_compute_Omega_node",
                            lambda eng: np.full((N, N, N), float(src.omega)))
        cap = gate._capture(engine)
        for key in ("t", "n_nucleated_total", "n_fired_this_step",
                    "fired_bonds", "gate_active"):
            assert key in cap
        assert cap["gate_active"] is True
