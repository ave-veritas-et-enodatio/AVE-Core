"""
AVE Fundamental 3D Vacuum Engine.

Implements the design from `research/L3_electron_soliton/46_vacuum_engine_scope.md`:
a general-purpose simulator for all four Axiom-4 operating regimes with
temperature-dependent vacuum states, rigorous unit conventions, and
composable sources / observers.

Architectural overview
----------------------
The engine wraps `CoupledK4Cosserat` (the physics core: K4 scatter+connect
photon propagation + Cosserat (u, ω) rotational sector + S1-D coupling per
42_coupled_simulator_validation.md) with a clean user-facing API:

    engine = VacuumEngine3D.from_args(
        N=48, pml=6,
        temperature=0.1,            # m_e c² units (0 → deterministic vacuum)
        amplitude_convention="V_SNAP",
        coupling_kappa=1.0,
    )
    engine.add_source(AutoresonantCWSource(...))
    engine.add_observer(DarkWakeObserver())
    engine.run(n_steps=300)

Source types
------------
- `PulsedSource`       — Gaussian-pulse plane source (transient, for single-photon
                         propagation tests). Phase A/B-style.
- `CWSource`           — Sinusoidal plane source with ramp/sustain/decay envelope
                         (fixed frequency). Phase III-B v1 default.
- `AutoresonantCWSource` — PLL-tracked CW source that adjusts drive frequency
                         based on probe-point strain (Duffing-like resonance
                         shift). Phase III-B v2 default. Implements the FOC
                         q-axis analog per AVE-Propulsion Ch 5. Novel to
                         AVE-Core — no sibling reference implementation.

Observer types
--------------
- `ScalarObserver`            — generic user-function wrapper
- `RegimeClassifierObserver`  — counts lattice cells per Axiom-4 regime
                                (I linear, II E-H transition, III saturated,
                                IV rupture) at each step
- `TopologyObserver`          — Q_H (Hopf invariant), soliton centroid count,
                                shell radii (for (2,3) structures)
- `EnergyBudgetObserver`      — E_K4, E_cos, T_cos, E_coupling, H_total
- `DarkWakeObserver`          — τ_zx longitudinal shear strain (back-EMF
                                signature); ports formula from AVE-Propulsion's
                                simulate_warp_metric_tensors.py. Uses
                                tetrahedral gradient (NOT np.gradient) because
                                K4 active sites alternate sublattices.

Temperature regimes
-------------------
- `T = 0`  — deterministic cold vacuum (V = u = ω = 0 exactly). Correct AVE
              prediction per doc 47_ §2.1 (C1): no sub-ℓ_node reality.
- `T > 0`  — classical Maxwell-Boltzmann thermal init of Cosserat (u, ω) fields
              only. V_inc stays at zero unless thermalize_V=True is explicitly
              set (which requires T < α/(4π) ≈ 5.8e-4 for vacuum stability;
              equivalently T < 3.44×10⁶ K in SI — see doc 47_ §2.2 for the
              AVE Schwinger-temperature derivation).

Unit conventions
----------------
- `amplitude_convention="V_SNAP"`:  user provides amp as fraction of V_SNAP
                                    (= m_e c²/e ≈ 511 kV SI; rupture threshold).
                                    Rupture boundary is A² = 1.
- `amplitude_convention="V_YIELD"`: user provides amp as fraction of V_YIELD
                                    (= √α·V_SNAP ≈ 43.65 kV SI; Regime II onset).
                                    Converted internally via √α.

Physics parameters (S-gate resolutions 2026-04-22)
--------------------------------------------------
- S1 = D: coupling form `(V²/V_SNAP²) · W_refl(u, ω)` — pure Axiom-4 reuse
- S2 = γ: port-quadrature pairing deferred (S1-D is phase-insensitive)
- S3 = A: no amplitude gate (S1-D is naturally gated by 1/S² in W_refl)
- S4 = A: natural units ρ = I_ω = 1
- S5 = B: unified leapfrog integrator
- S6 = A: topological charge Q measured, not projected

Phase III-B results (v1 + v2)
-----------------------------
- v1 (fixed-f CW): `σ(ω)` peaks at ω·τ_relax ≈ 0.9 (detuning-limited);
                    max A²_cos ≈ 0.96 (doc 48_).
- v2 (autoresonant): `σ(ω)` monotonic rise, reaches A²_cos = 1.009 at
                      ω·τ = 1.8 (rupture boundary crossed; doc 50_).
- Pair creation (localized centroids) NOT yet observed — see 51_handoff
  for follow-up hypotheses.

References
----------
- research/L3_electron_soliton/46_vacuum_engine_scope.md (design scope + C-findings)
- research/L3_electron_soliton/47_thermal_lattice_noise.md (σ_V, σ_ω derivations)
- research/L3_electron_soliton/49_dark_wake_bemf_foc_synthesis.md (ecosystem synthesis)
- research/L3_electron_soliton/42_coupled_simulator_validation.md (Phase II Coupled* core)
- AVE-Propulsion/src/scripts/simulate_warp_metric_tensors.py (τ_zx source)
- AVE-Propulsion/manuscript/vol_propulsion/chapters/05_autoresonant_dielectric_rupture.tex (PLL picture)
- AVE-PONDER/src/scripts/generate_ponder_01_spice_netlist.py (η_vac calibration K_0=0.208)
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Optional

import numpy as np

from ave.core.constants import ALPHA
from ave.topological.k4_cosserat_coupling import (
    CoupledK4Cosserat,
    _v_squared_per_site,
    _cosserat_A_squared,
)


# ─────────────────────────────────────────────────────────────────
# K4 port-direction geometry (for plane-source port weighting)
# ─────────────────────────────────────────────────────────────────
# Port-direction unit vectors (A→B direction vectors, normalized).
# Needed here to avoid a library-imports-from-script dependency on
# photon_propagation.py (where this logic previously lived).
_PORT_HAT = np.array([
    [+1, +1, +1], [+1, -1, -1], [-1, +1, -1], [-1, -1, +1],
], dtype=float) / np.sqrt(3.0)


def _forward_t2_port_weights(direction: tuple[float, float, float]) -> np.ndarray:
    """T₂-projected forward port weights for a +d̂ plane-wave source.

    See `research/L3_electron_soliton/30_photon_identification.md` and the
    original `photon_propagation.forward_port_weights`. Raw weights
    `max(0, −d̂·p̂_n)`, then A₁ projection (subtract mean) to get the
    T₂-only photon pattern, then L² normalization.
    """
    d = np.asarray(direction, dtype=float)
    d = d / np.linalg.norm(d)
    w = np.maximum(0.0, -_PORT_HAT @ d)
    w = w - w.mean()   # project onto T₂
    norm = np.sqrt((w * w).sum())
    if norm > 0:
        w = w / norm
    return w


# ─────────────────────────────────────────────────────────────────
# Amplitude conventions
# ─────────────────────────────────────────────────────────────────
# V_SNAP in lattice natural units: 1 by definition for a "natural-units" sim.
# V_YIELD = √α · V_SNAP = √α in natural units (≈ 0.0854).
# User's `amp` parameter is always relative to their convention, converted
# to V_SNAP-units internally.
_V_YIELD_FRAC = np.sqrt(ALPHA)  # ≈ 0.0854
_REGIME_I_BOUND_A2 = 2.0 * ALPHA          # ≈ 0.0146
_REGIME_II_BOUND_A2 = 3.0 / 4.0           # = 0.75
_RUPTURE_BOUND_A2 = 1.0


def amp_to_vsnap_units(amp: float, convention: str) -> float:
    """Convert user-supplied amplitude to V_SNAP internal units."""
    if convention == "V_SNAP":
        return float(amp)
    elif convention == "V_YIELD":
        return float(amp) * _V_YIELD_FRAC
    else:
        raise ValueError(f"Unknown convention {convention!r}; "
                         "use 'V_SNAP' or 'V_YIELD'")


def amp_to_display(amp_vsnap: float, convention: str) -> float:
    """Convert internal V_SNAP-units back to user convention for display."""
    if convention == "V_SNAP":
        return float(amp_vsnap)
    elif convention == "V_YIELD":
        return float(amp_vsnap) / _V_YIELD_FRAC
    else:
        raise ValueError(f"Unknown convention {convention!r}")


# ─────────────────────────────────────────────────────────────────
# Sources
# ─────────────────────────────────────────────────────────────────
class Source:
    """Base class for vacuum-engine sources. Each step the engine calls
    `apply(engine, t)` on every source, allowing the source to inject V
    (or modulate ω) at the current time."""

    def apply(self, engine: "VacuumEngine3D", t: float) -> None:
        raise NotImplementedError


class PulsedSource(Source):
    """Gaussian-pulse plane source (transient).

    Replaces the old photon_propagation.PlaneSource with unit-clean
    amplitude handling.
    """

    def __init__(
        self,
        x0: int,
        direction: tuple[float, float, float],
        amplitude: float,            # in user convention units
        omega: float,                # carrier frequency (natural units)
        sigma_yz: float,
        t_center: float,
        t_sigma: float,
        y_c: Optional[float] = None,
        z_c: Optional[float] = None,
    ):
        self.x0 = int(x0)
        self.direction = tuple(direction)
        self.amplitude = float(amplitude)
        self.omega = float(omega)
        self.sigma_yz = float(sigma_yz)
        self.t_center = float(t_center)
        self.t_sigma = float(t_sigma)
        self.y_c = y_c
        self.z_c = z_c
        self._port_w = None
        self._yz_profile = None
        self.cumulative_energy_injected = 0.0

    def _init_if_needed(self, engine: "VacuumEngine3D") -> None:
        if self._port_w is not None:
            return
        self._port_w = _forward_t2_port_weights(self.direction)
        N = engine.N
        ny, nz = N, N
        yc = (ny - 1) / 2.0 if self.y_c is None else self.y_c
        zc = (nz - 1) / 2.0 if self.z_c is None else self.z_c
        j, k = np.indices((ny, nz), dtype=float)
        r2 = (j - yc) ** 2 + (k - zc) ** 2
        self._yz_profile = np.exp(-r2 / (2.0 * self.sigma_yz ** 2))

    def apply(self, engine: "VacuumEngine3D", t: float) -> None:
        self._init_if_needed(engine)
        env = np.exp(-((t - self.t_center) ** 2) / (2.0 * self.t_sigma ** 2))
        osc = np.sin(self.omega * (t - self.t_center))
        # Convert user amp to V_SNAP-internal
        amp_internal = amp_to_vsnap_units(self.amplitude, engine.amplitude_convention)
        amp_volts = amp_internal * engine.V_SNAP * env * osc
        if abs(amp_volts) < 1e-30:
            return
        active = engine.k4.mask_active[self.x0].astype(float)
        injection = amp_volts * self._yz_profile * active
        per_step_energy = 0.0
        for n in range(4):
            if self._port_w[n] != 0:
                contrib = self._port_w[n] * injection
                engine.k4.V_inc[self.x0, :, :, n] += contrib
                per_step_energy += float(np.sum(contrib ** 2))
        self.cumulative_energy_injected += per_step_energy


class CWSource(Source):
    """Continuous-wave (CW) plane source with ramp-up and sustain phases.

    Shape: sin(ω·t) × envelope(t), where envelope ramps from 0 to 1 over
    t_ramp, holds at 1 for t_sustain, then optionally decays.

    Primary source type for Phase III-B pair creation (standing-wave regime).
    """

    def __init__(
        self,
        x0: int,
        direction: tuple[float, float, float],
        amplitude: float,            # in user convention units
        omega: float,
        sigma_yz: float,
        t_ramp: float,
        t_sustain: float,
        t_decay: Optional[float] = None,
        y_c: Optional[float] = None,
        z_c: Optional[float] = None,
    ):
        self.x0 = int(x0)
        self.direction = tuple(direction)
        self.amplitude = float(amplitude)
        self.omega = float(omega)
        self.sigma_yz = float(sigma_yz)
        self.t_ramp = float(t_ramp)
        self.t_sustain = float(t_sustain)
        self.t_decay = float(t_decay) if t_decay is not None else 0.0
        self.y_c = y_c
        self.z_c = z_c
        self._port_w = None
        self._yz_profile = None
        self.cumulative_energy_injected = 0.0

    def envelope(self, t: float) -> float:
        if t < 0:
            return 0.0
        if t < self.t_ramp:
            return t / self.t_ramp
        sustain_end = self.t_ramp + self.t_sustain
        if t < sustain_end:
            return 1.0
        if self.t_decay > 0 and t < sustain_end + self.t_decay:
            return 1.0 - (t - sustain_end) / self.t_decay
        return 0.0

    def _init_if_needed(self, engine: "VacuumEngine3D") -> None:
        if self._port_w is not None:
            return
        self._port_w = _forward_t2_port_weights(self.direction)
        N = engine.N
        ny, nz = N, N
        yc = (ny - 1) / 2.0 if self.y_c is None else self.y_c
        zc = (nz - 1) / 2.0 if self.z_c is None else self.z_c
        j, k = np.indices((ny, nz), dtype=float)
        r2 = (j - yc) ** 2 + (k - zc) ** 2
        self._yz_profile = np.exp(-r2 / (2.0 * self.sigma_yz ** 2))

    def apply(self, engine: "VacuumEngine3D", t: float) -> None:
        self._init_if_needed(engine)
        env = self.envelope(t)
        if env <= 0:
            return
        osc = np.sin(self.omega * t)
        amp_internal = amp_to_vsnap_units(self.amplitude, engine.amplitude_convention)
        amp_volts = amp_internal * engine.V_SNAP * env * osc
        if abs(amp_volts) < 1e-30:
            return
        active = engine.k4.mask_active[self.x0].astype(float)
        injection = amp_volts * self._yz_profile * active
        per_step_energy = 0.0
        for n in range(4):
            if self._port_w[n] != 0:
                contrib = self._port_w[n] * injection
                engine.k4.V_inc[self.x0, :, :, n] += contrib
                per_step_energy += float(np.sum(contrib ** 2))
        self.cumulative_energy_injected += per_step_energy


# ─────────────────────────────────────────────────────────────────
# Observers
# ─────────────────────────────────────────────────────────────────
class Observer:
    """Base class for vacuum-engine observers. The engine calls `record(engine)`
    on every observer after each step (or every N steps per cadence)."""

    def __init__(self, cadence: int = 1):
        self.cadence = int(cadence)
        self.history: list = []

    def record(self, engine: "VacuumEngine3D") -> None:
        if engine.step_count % self.cadence != 0:
            return
        self.history.append(self._capture(engine))

    def _capture(self, engine: "VacuumEngine3D") -> Any:
        raise NotImplementedError


class ScalarObserver(Observer):
    """Records the result of a user-supplied scalar function of the engine."""

    def __init__(self, name: str, fn: Callable[["VacuumEngine3D"], float], cadence: int = 1):
        super().__init__(cadence=cadence)
        self.name = name
        self.fn = fn

    def _capture(self, engine: "VacuumEngine3D") -> dict:
        return {"t": engine.time, "value": float(self.fn(engine))}


class RegimeClassifierObserver(Observer):
    """Counts lattice cells per Axiom-4 regime each step."""

    def _capture(self, engine: "VacuumEngine3D") -> dict:
        V_sq = _v_squared_per_site(engine.k4.V_inc)
        A2_k4 = V_sq / (engine.V_SNAP ** 2)
        A2_cos = _cosserat_A_squared(
            engine.cos.u, engine.cos.omega, engine.cos.dx,
            engine.cos.omega_yield, engine.cos.epsilon_yield,
        )
        A2 = A2_k4 + A2_cos
        alive = engine.k4.mask_active
        rg1 = int(np.sum(alive & (A2 < _REGIME_I_BOUND_A2)))
        rg2 = int(np.sum(alive & (A2 >= _REGIME_I_BOUND_A2) & (A2 < _REGIME_II_BOUND_A2)))
        rg3 = int(np.sum(alive & (A2 >= _REGIME_II_BOUND_A2) & (A2 < _RUPTURE_BOUND_A2)))
        rupture = int(np.sum(alive & (A2 >= _RUPTURE_BOUND_A2)))
        return {
            "t": engine.time,
            "rg_I": rg1, "rg_II": rg2, "rg_III": rg3, "rupture": rupture,
            "max_A2_k4": float(A2_k4[alive].max()) if alive.any() else 0.0,
            "max_A2_cos": float(A2_cos[alive].max()) if alive.any() else 0.0,
            "max_A2_total": float(A2[alive].max()) if alive.any() else 0.0,
        }


class BondObserver(Observer):
    """Read-only observer of per-bond magnetic flux linkage `Φ_link`.

    Each directed A→B bond in the K4 lattice carries
    `Φ_link = ∫V_bond dt` per doc 54_ §3. `K4Lattice3D` accumulates
    this in `_connect_all` during the scatter-to-connect transit;
    this observer summarizes the field's statistics each step.

    Primary metrics:
      - `phi_abs_max`: max |Φ_link| across all A-site bonds
      - `phi_rms`: √⟨Φ²⟩ across A-site bonds
      - `phi_at_saturated_bonds_rms`: RMS of Φ_link restricted to bonds
        whose BOTH endpoints have A²_yield ≥ saturation_frac (default 0.5).
        This is the signal channel for flux-tube confinement (doc 54_ §3):
        saturated endpoints form Γ = -1 walls, trapping the LC oscillation
        as persistent flux linkage.
      - `phi_at_unsaturated_bonds_rms`: same, for bonds with at least one
        unsaturated endpoint. This is the propagating / decaying channel.

    Comparing the two RMS ratios over time gives the Phase-3 prediction
    signal: after drive shutoff, the saturated-bond channel should persist
    (≥ 10 Compton periods) while the unsaturated channel decays (~3
    Compton periods).

    Saturation detection reuses the same A²_yield normalization as
    NodeResonanceObserver (V_SNAP → V_yield via factor 1/α).

    References:
      - research/L3_electron_soliton/54_pair_production_axiom_derivation.md §3, §9.2
      - manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex:223-227
      - src/ave/core/k4_tlm.py::K4Lattice3D.Phi_link

    Predictions.yaml entry: P_phase3_flux_tube.
    """

    def __init__(self, cadence: int = 1, saturation_frac: float = 0.5):
        super().__init__(cadence=cadence)
        self.saturation_frac = float(saturation_frac)

    def _compute_A2_yield(self, engine: "VacuumEngine3D") -> np.ndarray:
        # Under Vol 4 Ch 1:711 subatomic override, V_yield ≡ V_SNAP.
        # A²_K4 = V²/V_SNAP² IS canonical r²; no /α needed (R4 direction).
        # Method name kept as `_compute_A2_yield` for backward-compat; the
        # returned value is the canonical Pythagorean r²_total per Vol 1
        # Ch 7:12 + AVE-APU Vol 1 Ch 5. See VACUUM_ENGINE_MANUAL §17 A14 r6.
        V_sq = _v_squared_per_site(engine.k4.V_inc)
        A2_k4 = V_sq / (engine.V_SNAP ** 2)
        A2_cos = _cosserat_A_squared(
            engine.cos.u, engine.cos.omega, engine.cos.dx,
            engine.cos.omega_yield, engine.cos.epsilon_yield,
        )
        return A2_k4 + A2_cos  # Pythagorean sum, both canonical r²

    def _capture(self, engine: "VacuumEngine3D") -> dict:
        Phi = engine.k4.Phi_link
        mask_A = engine.k4.mask_A

        # Site-level A²_yield for saturation detection
        A2_yield = self._compute_A2_yield(engine)
        saturated_site = (A2_yield >= self.saturation_frac)

        # Each bond has an A-site and a B-site endpoint.
        # Bond is "saturated" when BOTH endpoints are saturated.
        # For A-sites: port_shifts[port] gives the A→B direction;
        # the B endpoint is at np.roll(..., -shift_to_B) from A.
        # We use the inverse shift to check the B neighbor.
        # (port_shifts in k4_tlm.py:297-302 are NEGATED directions for np.roll;
        #  so to find B's position from A's, we apply the -shift_to_B direction)
        port_shifts = [(-1, -1, -1), (-1, +1, +1), (+1, -1, +1), (+1, +1, -1)]

        # Phi restricted to A-sites (the canonical bond-index location)
        # We'll partition by whether each bond's B-neighbor is saturated
        phi_sat_flat = []       # bonds with both endpoints saturated
        phi_unsat_flat = []     # bonds with at least one unsaturated endpoint
        for port, shift_to_B in enumerate(port_shifts):
            # To get the B-neighbor's A²_yield at each A-site position,
            # we roll the saturated_site field OPPOSITE the shift_to_B
            # direction (because B is at -shift_to_B relative to A's
            # storage slot — see the k4_tlm.py connect step comments).
            inverse_shift = tuple(-s for s in shift_to_B)
            sat_B_at_A = np.roll(
                saturated_site, shift=inverse_shift, axis=(0, 1, 2),
            )
            bond_both_sat = mask_A & saturated_site & sat_B_at_A
            bond_any_unsat = mask_A & ~(saturated_site & sat_B_at_A)
            phi_port = Phi[..., port]
            phi_sat_flat.append(phi_port[bond_both_sat])
            phi_unsat_flat.append(phi_port[bond_any_unsat])

        phi_sat = np.concatenate(phi_sat_flat) if phi_sat_flat else np.array([])
        phi_unsat = np.concatenate(phi_unsat_flat) if phi_unsat_flat else np.array([])

        # Overall stats across all A-site bonds
        all_A_phi = Phi[mask_A, :]

        def _rms(x: np.ndarray) -> float:
            return float(np.sqrt(np.mean(x ** 2))) if x.size > 0 else 0.0

        return {
            "t": engine.time,
            "phi_abs_max": float(np.max(np.abs(all_A_phi))) if all_A_phi.size > 0 else 0.0,
            "phi_rms": _rms(all_A_phi),
            "phi_at_saturated_bonds_rms": _rms(phi_sat),
            "phi_at_unsaturated_bonds_rms": _rms(phi_unsat),
            "n_saturated_bonds": int(phi_sat.size),
            "n_unsaturated_bonds": int(phi_unsat.size),
        }


class NodeResonanceObserver(Observer):
    """Read-only observer of per-node LC-tank resonance softening derived
    from Axiom 4's Vacuum Varactor.

    Each active site's LC tank has a natural resonance `ω_0` (bare
    Compton frequency at the bond scale per [24_step3 §4.2]) that
    softens under local saturation per the Vol 4 Ch 1:127-142 varactor:

        C_eff(V) = C_0 / √(1 − (V/V_yield)²) = C_0 / S(V)

    giving a node resonance

        Ω_node(r,t) / ω_0 = S(r,t)^(1/2) = (1 − A²_yield(r,t))^(1/4)

    where `A²_yield = A²_total / α` converts the engine's V_SNAP-
    normalized saturation (A²_k4 = V²/V_SNAP²) to V_yield normalization
    per doc 54_ §5. The Cosserat contribution A²_cos is already yield-
    normalized in its own sector (ε/ε_yield, κ/ω_yield); it is added
    directly to A²_k4_yield by the Pythagorean vacuum strain theorem
    (AVE-APU Vol 1 Ch 5:26-37; FUTURE_WORK.md G-7).

    This is a READ-ONLY observer — it does not touch engine dynamics.
    The ratio is clipped to [0, 1) for numerical safety at saturation.

    Pre-registered prediction P_phase2_omega: the recorded
    `omega_ratio_*` trajectory must match `(1 - A²_yield)^(1/4)`
    within 5% across `A² ∈ (0, α/2)` on the v2 headline config.

    References:
      - research/L3_electron_soliton/54_pair_production_axiom_derivation.md §4
      - manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex:127-142
    """

    def _capture(self, engine: "VacuumEngine3D") -> dict:
        # Under Vol 4 Ch 1:711 subatomic override, V_yield ≡ V_SNAP at
        # VacuumEngine3D's operating scale. A²_K4 = V²/V_SNAP² IS canonical
        # r² per Vol 1 Ch 7:12; no /α conversion needed. Cosserat's A² is
        # yield-normalized to its own ε_yield/ω_yield thresholds, also
        # canonical r² at subatomic scale (ε_yield=1 is TKI-derived).
        # See research/L3_electron_soliton/50_autoresonant_pair_creation.md
        # §0.1 r3 and VACUUM_ENGINE_MANUAL §17 A14 r6.
        V_sq = _v_squared_per_site(engine.k4.V_inc)
        A2_k4 = V_sq / (engine.V_SNAP ** 2)
        A2_cos = _cosserat_A_squared(
            engine.cos.u, engine.cos.omega, engine.cos.dx,
            engine.cos.omega_yield, engine.cos.epsilon_yield,
        )
        # Pythagorean quadrature sum of orthogonal DoFs (AVE-APU Vol 1 Ch 5)
        A2_total = A2_k4 + A2_cos
        # Clip to [0, 1) for numerical safety past saturation
        A2_clipped = np.clip(A2_total, 0.0, 1.0 - 1e-12)
        # Axiom-4 saturation kernel
        S = np.sqrt(1.0 - A2_clipped)
        # Ω_node/ω_0 = S^(1/2) = (1 − A²)^(1/4)  (doc 54_ §4)
        omega_ratio = np.sqrt(S)

        alive = engine.k4.mask_active
        if alive.any():
            return {
                "t": engine.time,
                "omega_ratio_max": float(omega_ratio[alive].max()),
                "omega_ratio_mean": float(omega_ratio[alive].mean()),
                "omega_ratio_min": float(omega_ratio[alive].min()),
                "A2_yield_max": float(A2_total[alive].max()),
                "A2_yield_mean": float(A2_total[alive].mean()),
                "n_saturated": int(np.sum(alive & (A2_total >= 1.0))),
            }
        return {
            "t": engine.time,
            "omega_ratio_max": 1.0,
            "omega_ratio_mean": 1.0,
            "omega_ratio_min": 1.0,
            "A2_yield_max": 0.0,
            "A2_yield_mean": 0.0,
            "n_saturated": 0,
        }


class TopologyObserver(Observer):
    """Records Q_H, centroids, shell radii.

    `threshold_frac` is the primary detection threshold and determines the
    top-level `n_centroids` / `centroids` keys (used by downstream summaries).
    `threshold_fracs`, if provided, records additional centroid captures at
    each listed threshold under the `per_threshold` key — for H1-style
    measurement-sensitivity studies (see 51_handoff §1). When
    `threshold_fracs` is given and `threshold_frac` is omitted, the smallest
    value in the list becomes the primary threshold so aggregate counts
    reflect the most sensitive detection.
    """

    def __init__(
        self,
        cadence: int = 5,
        threshold_frac: Optional[float] = None,
        threshold_fracs: Optional[list[float]] = None,
    ):
        super().__init__(cadence=cadence)
        if threshold_frac is None:
            self.threshold_frac = (
                min(threshold_fracs) if threshold_fracs else 0.3
            )
        else:
            self.threshold_frac = float(threshold_frac)
        self.threshold_fracs = (
            [float(t) for t in threshold_fracs] if threshold_fracs else None
        )

    def _capture(self, engine: "VacuumEngine3D") -> dict:
        cents = engine.cos.find_soliton_centroids(threshold_frac=self.threshold_frac)
        record = {
            "t": engine.time,
            "Q_hopf": engine.cos.extract_hopf_charge(),
            "n_centroids": len(cents),
            "centroids": cents,
        }
        if self.threshold_fracs is not None:
            per = {}
            for tf in self.threshold_fracs:
                if tf == self.threshold_frac:
                    c = cents
                else:
                    c = engine.cos.find_soliton_centroids(threshold_frac=tf)
                per[tf] = {"n_centroids": len(c), "centroids": c}
            record["per_threshold"] = per
        return record


class EnergyBudgetObserver(Observer):
    """Records E_K4, E_cos (potential), T_cos (kinetic), E_coupling, H_total."""

    def _capture(self, engine: "VacuumEngine3D") -> dict:
        return {
            "t": engine.time,
            "E_K4": float(engine.k4.total_energy()),
            "E_cos": float(engine.cos.total_energy()),
            "T_cos": float(engine.cos.kinetic_energy()),
            "E_coupling": engine._coupled.coupling_energy(),
            "H_total": engine._coupled.total_hamiltonian(),
        }


class AutoresonantCWSource(CWSource):
    """CW plane source with autoresonant frequency tracking (PLL q-axis analog).

    Per AVE-Propulsion/manuscript/vol_propulsion/chapters/05_autoresonant_dielectric_rupture.tex:
        "If a fixed-frequency extreme-intensity laser is fired into the vacuum,
        the increasing metric strain lowers the local vacuum's resonant
        frequency, and the laser detunes and reflects rather than couples
        energy. A phase-locked regenerative feedback loop overcomes this
        limitation."

    Implementation (Stage 4c — novel to AVE-Core, no sibling reference code):
        The instantaneous local strain A² = V²/V_SNAP² near the source
        shifts the lattice's effective resonance per Duffing-oscillator
        behavior. The source tracks this shift by adjusting its drive
        frequency downward:

            ω(t) = ω_0 · max(ε, 1 - K_drift · A²_probe(t))

        where A²_probe is measured at a downstream probe point. This is
        the minimum viable autoresonant behavior; Stage 4d runs will
        validate whether this level of feedback is sufficient, or whether
        a full PI-PLL with proper phase detection is needed.

    Key implementation detail: maintains an internal PHASE ACCUMULATOR
    rather than using t directly. Otherwise changes in ω would cause
    phase discontinuities.

    Args:
        x0, direction, amplitude, omega, sigma_yz, t_ramp, t_sustain, ...:
            same as CWSource
        K_drift: autoresonant shift gain (default 0.5; higher = more
            aggressive frequency tracking). Tune empirically in 4c.
        probe_x_offset: cells downstream of x0 to probe for A² (default 4)
    """

    def __init__(
        self,
        x0: int,
        direction: tuple[float, float, float],
        amplitude: float,
        omega: float,
        sigma_yz: float,
        t_ramp: float,
        t_sustain: float,
        t_decay: Optional[float] = None,
        y_c: Optional[float] = None,
        z_c: Optional[float] = None,
        K_drift: float = 0.5,
        probe_x_offset: int = 4,
    ):
        super().__init__(
            x0=x0, direction=direction, amplitude=amplitude,
            omega=omega, sigma_yz=sigma_yz,
            t_ramp=t_ramp, t_sustain=t_sustain, t_decay=t_decay,
            y_c=y_c, z_c=z_c,
        )
        self.K_drift = float(K_drift)
        self.probe_x_offset = int(probe_x_offset)
        self._omega_0 = float(omega)       # nominal (unshifted) frequency
        self._omega_current = self._omega_0  # shifts over time
        self._accumulated_phase = 0.0
        self._last_t = None
        self._omega_history: list[float] = []
        self._probe_A_sq_history: list[float] = []

    def _measure_probe_A_sq(self, engine: "VacuumEngine3D") -> float:
        dx_sign = int(np.sign(self.direction[0])) if self.direction[0] != 0 else 1
        probe_x = self.x0 + self.probe_x_offset * dx_sign
        probe_x = int(np.clip(probe_x, 0, engine.N - 1))
        V_inc_slab = engine.k4.V_inc[probe_x]   # (ny, nz, 4)
        V_sq = np.sum(V_inc_slab ** 2, axis=-1)  # (ny, nz)
        active = engine.k4.mask_active[probe_x]
        if not active.any():
            return 0.0
        return float(V_sq[active].max() / (engine.V_SNAP ** 2))

    def apply(self, engine: "VacuumEngine3D", t: float) -> None:
        self._init_if_needed(engine)

        # Advance phase accumulator by ω_current · dt (dt = outer_dt)
        dt = engine.outer_dt if self._last_t is not None else 0.0
        self._accumulated_phase += self._omega_current * dt
        self._last_t = t

        # Measure probe strain
        A_sq_probe = self._measure_probe_A_sq(engine)
        self._probe_A_sq_history.append(A_sq_probe)

        # Autoresonant frequency shift (Duffing: resonance drops with strain)
        shift_factor = max(1e-3, 1.0 - self.K_drift * A_sq_probe)
        self._omega_current = self._omega_0 * shift_factor
        self._omega_history.append(self._omega_current)

        # Envelope (same as CWSource)
        env = self.envelope(t)
        if env <= 0:
            return

        # Oscillator — uses accumulated phase (NOT ω·t directly)
        osc = np.sin(self._accumulated_phase)

        amp_internal = amp_to_vsnap_units(self.amplitude, engine.amplitude_convention)
        amp_volts = amp_internal * engine.V_SNAP * env * osc
        if abs(amp_volts) < 1e-30:
            return

        active_slice = engine.k4.mask_active[self.x0].astype(float)
        injection = amp_volts * self._yz_profile * active_slice

        per_step_energy = 0.0
        for n in range(4):
            if self._port_w[n] != 0:
                contrib = self._port_w[n] * injection
                engine.k4.V_inc[self.x0, :, :, n] += contrib
                per_step_energy += float(np.sum(contrib ** 2))
        self.cumulative_energy_injected += per_step_energy


class DarkWakeObserver(Observer):
    """Dark wake diagnostic — the longitudinal shear strain τ_zx wave that
    propagates backward from any coherent V excitation (per AVE-PONDER
    vol_ponder/ch01 and AVE-Propulsion simulate_warp_metric_tensors.py:84-85).

    Formula (ported from AVE-Propulsion Ch 5 description):
        τ_zx(r) ∝ Z_local(r) · ∂/∂x [|V(r)|²/V_SNAP²]

    Physical interpretation (per doc 49_):
        The dark wake IS the mutual-inductance back-EMF response of the
        K4 lattice. Any propagating coherent V creates a shear-strain
        wave behind it, carrying the Newton-3rd-law reaction momentum.

    Captures:
        tau_zx_slab(y, z): the x-axis-averaged τ_zx, sliced through the
            lattice — shows the wake pattern in the propagation plane.
        max_tau_zx: peak magnitude (physically must grow then saturate
            when A² → 1 regime is entered).
        wake_centroid_x: x-position of max|τ_zx| to verify backward
            propagation at c.

    Dimensional note: τ_zx has dimensions [1/length²] (per strain tensor
    convention); numerically O(|V|² gradient × z_local) in natural units.

    Usage:
        engine.add_observer(DarkWakeObserver(
            cadence=5,
            propagation_axis=0,   # 0=x, 1=y, 2=z
        ))
    """

    def __init__(self, cadence: int = 5, propagation_axis: int = 0):
        super().__init__(cadence=cadence)
        self.propagation_axis = int(propagation_axis)

    def _capture(self, engine: "VacuumEngine3D") -> dict:
        # K4 active sites alternate (even,even,even) ⊕ (odd,odd,odd), so
        # np.gradient with Cartesian centered differences gives 0 at every
        # active site (both axis-neighbors are inactive). Use the
        # tetrahedral gradient (cosserat_field_3d module) which computes
        # via K4 bond directions — same operator the Cosserat code uses
        # for ε, κ strain tensors.
        from ave.topological.cosserat_field_3d import tetrahedral_gradient

        V_sq = _v_squared_per_site(engine.k4.V_inc)
        A_sq = V_sq / (engine.V_SNAP ** 2)

        # tetrahedral_gradient returns shape (nx, ny, nz, 3) — the 3D
        # vector gradient at each site via K4 bond differences.
        grad_A_sq = tetrahedral_gradient(A_sq) / engine.k4.dx
        grad_axis = grad_A_sq[..., self.propagation_axis]

        # τ_zx proportional to z_local · ∂|V|²/∂x (per AVE-Propulsion
        # simulate_warp_metric_tensors.py:84-85)
        z_local = engine.k4.z_local_field
        tau_zx = z_local * grad_axis

        alive = engine.k4.mask_active
        tau_on_active = tau_zx * alive

        # Slab along the propagation axis — averaged over transverse cells
        axes = [0, 1, 2]
        transverse = [a for a in axes if a != self.propagation_axis]
        tau_slab = np.mean(np.abs(tau_on_active), axis=tuple(transverse))

        # Find wake peak position along the propagation axis (ignore
        # anything in the PML region — those are boundary artifacts)
        N = engine.N
        pml = engine.config.pml
        interior_slice = slice(pml, N - pml)
        tau_interior = tau_slab[interior_slice]
        if tau_interior.max() > 0:
            peak_idx = int(np.argmax(tau_interior)) + pml
        else:
            peak_idx = -1

        # Max |τ_zx| across the whole lattice (excluding PML)
        interior_mask = np.zeros_like(alive)
        interior_mask[pml:N - pml, pml:N - pml, pml:N - pml] = True
        interior_alive = alive & interior_mask
        max_tau_zx = float(np.abs(tau_zx[interior_alive]).max()) if interior_alive.any() else 0.0

        return {
            "t": engine.time,
            "tau_zx_slab": tau_slab,         # 1D along propagation axis
            "max_tau_zx": max_tau_zx,
            "wake_peak_x": peak_idx,         # -1 if no wake
        }


# ─────────────────────────────────────────────────────────────────
# VacuumEngine3D main class
# ─────────────────────────────────────────────────────────────────
@dataclass
class EngineConfig:
    """Numerical + physical parameters of the engine.

    All amplitudes use V_SNAP internally. User-side `amplitude_convention`
    controls what gets passed IN.
    """
    N: int
    pml: int = 6
    temperature: float = 0.0            # in m_e c² units (dimensionless)
    amplitude_convention: str = "V_SNAP"
    rho: float = 1.0
    I_omega: float = 1.0
    coupling_kappa: float = 1.0         # S1-D prefactor (C2 proxy for η_vac)
    axiom_4_enabled: bool = True
    V_SNAP_override: Optional[float] = None  # override if using non-SI


class VacuumEngine3D:
    """AVE-native fundamental 3D vacuum engine.

    See doc 46_ for design rationale. Internally holds a CoupledK4Cosserat
    instance and a registry of sources and observers.

    Example:
        >>> engine = VacuumEngine3D.from_args(N=32, temperature=0.0)
        >>> engine.add_source(CWSource(x0=8, direction=(1,0,0), amplitude=0.5,
        ...                            omega=2*np.pi/8, sigma_yz=3.0,
        ...                            t_ramp=10, t_sustain=100))
        >>> engine.add_observer(RegimeClassifierObserver(cadence=5))
        >>> engine.run(n_steps=150)
        >>> print(engine.history())
    """

    def __init__(self, config: EngineConfig):
        self.config = config
        self.N = config.N
        self.amplitude_convention = config.amplitude_convention
        self.coupling_kappa = config.coupling_kappa
        self.V_SNAP = (
            config.V_SNAP_override if config.V_SNAP_override is not None
            else 1.0     # natural units by default
        )

        # Core physics: delegate to CoupledK4Cosserat
        self._coupled = CoupledK4Cosserat(
            N=config.N, pml=config.pml,
            rho=config.rho, I_omega=config.I_omega,
            V_SNAP=self.V_SNAP,
        )

        self.k4 = self._coupled.k4
        self.cos = self._coupled.cos
        self.time = 0.0
        self.step_count = 0

        self._sources: list[Source] = []
        self._observers: list[Observer] = []

        # Apply thermal initialization per C1
        self.initialize_thermal(config.temperature)

    @classmethod
    def from_args(cls, **kwargs) -> "VacuumEngine3D":
        """Convenience constructor: VacuumEngine3D.from_args(N=64, temperature=0.0, ...)."""
        cfg_kwargs = {k: v for k, v in kwargs.items() if k in EngineConfig.__dataclass_fields__}
        return cls(EngineConfig(**cfg_kwargs))

    # -----------------------------------------------------------------
    # Thermal initialization (per doc 47_)
    # -----------------------------------------------------------------
    def initialize_thermal(self, T: float, seed: Optional[int] = None,
                           thermalize_V: bool = False) -> None:
        """Initialize (V_inc, u, ω, u_dot, ω_dot) per classical equipartition
        at temperature T. Units: T in m_e c² (so T=1 means kT = electron mass).

        For T > 0:
            σ_V per port = √(4π·T/α) · V_SNAP   (ONLY if thermalize_V=True)
            σ_ω          = √(T · 1.14 / (4π²·I_ω))
            σ_ω_dot      = √(T / I_ω)
            σ_u          = √(T / (2π·ρ))
            σ_u_dot      = √(T / ρ)

        For T == 0, all fields are set to zero (C1: cold vacuum is deterministic).

        IMPORTANT (added 2026-04-22):
            The V-thermalization σ_V = √(4π·T/α)·V_SNAP diverges quickly with T:
            stability requires T < α/(4π) ≈ 5.8e-4 in m_ec² units to keep
            σ_V < V_SNAP. Above that threshold, the thermal V field alone
            ruptures the vacuum — the numerical simulation explodes before any
            source is applied.

            Physically this is CORRECT AVE behavior (the early universe at
            T >> 10⁷ K was literally above the Schwinger limit and the vacuum
            was unstable — nucleosynthesis era). But for Phase III-B, we want
            a CONTROLLED pair-creation experiment: stable cold K4 vacuum,
            thermal (u, ω) floor to seed Cosserat cascades when driven by CW
            photon sources.

            Default `thermalize_V=False`: leave V_inc = 0. Only thermalize
            the Cosserat rotational sector. Physically this is the "cold EM
            vacuum + warm matter-precursor" approximation valid below the
            Schwinger temperature.

            Set `thermalize_V=True` explicitly only if simulating the early-
            universe regime where both sectors are hot. Expect numerical
            instability above T ~ 1e-3.
        """
        if T <= 0.0:
            self.k4.V_inc[:] = 0.0
            self.k4.V_ref[:] = 0.0
            self.cos.u[:] = 0.0
            self.cos.u_dot[:] = 0.0
            self.cos.omega[:] = 0.0
            self.cos.omega_dot[:] = 0.0
            return

        rng = np.random.default_rng(seed)

        # Scalar V on K4 — only if thermalize_V (see docstring for stability warning)
        if thermalize_V:
            sigma_V = np.sqrt(4.0 * np.pi * T / ALPHA) * self.V_SNAP
            self.k4.V_inc[:] = rng.standard_normal(self.k4.V_inc.shape) * sigma_V
            self.k4.V_inc *= self.k4.mask_active[..., None]
        else:
            self.k4.V_inc[:] = 0.0
        self.k4.V_ref[:] = 0.0

        # Cosserat ω (massive mode; mode integral ≈ 1.14 for m²=4 per doc 47_)
        mode_int = np.pi - 2.0 * np.arctan(np.pi / 2.0)
        sigma_omega = np.sqrt(T * mode_int / (4.0 * np.pi ** 2 * self.cos.I_omega))
        sigma_omega_dot = np.sqrt(T / self.cos.I_omega)
        self.cos.omega[:] = rng.standard_normal(self.cos.omega.shape) * sigma_omega
        self.cos.omega_dot[:] = rng.standard_normal(self.cos.omega_dot.shape) * sigma_omega_dot
        self.cos.omega *= self.cos.mask_alive[..., None]
        self.cos.omega_dot *= self.cos.mask_alive[..., None]

        # Cosserat u
        sigma_u = np.sqrt(T / (2.0 * np.pi * self.cos.rho))
        sigma_u_dot = np.sqrt(T / self.cos.rho)
        self.cos.u[:] = rng.standard_normal(self.cos.u.shape) * sigma_u
        self.cos.u_dot[:] = rng.standard_normal(self.cos.u_dot.shape) * sigma_u_dot
        self.cos.u *= self.cos.mask_alive[..., None]
        self.cos.u_dot *= self.cos.mask_alive[..., None]

    # -----------------------------------------------------------------
    # Source + observer registration
    # -----------------------------------------------------------------
    def add_source(self, source: Source) -> None:
        self._sources.append(source)

    def add_observer(self, observer: Observer) -> None:
        self._observers.append(observer)

    # -----------------------------------------------------------------
    # Stepping
    # -----------------------------------------------------------------
    @property
    def outer_dt(self) -> float:
        return self._coupled.outer_dt

    def step(self) -> None:
        """Advance one outer timestep. Order: sources inject V, then
        CoupledK4Cosserat steps K4+Cosserat+coupling, then observers record."""
        t_pre = (self.step_count + 1) * self.outer_dt
        for src in self._sources:
            src.apply(self, t_pre)

        # Note: coupling_kappa is applied by overriding the coupling force
        # if κ != 1.0. For now, default κ=1.0 matches CoupledK4Cosserat baseline.
        # TODO: expose κ knob to _coupled if Phase III-B shows we need it.
        self._coupled.step()
        self.time = self._coupled.time
        self.step_count += 1

        for obs in self._observers:
            obs.record(self)

    def run(self, n_steps: int) -> None:
        for _ in range(n_steps):
            self.step()

    # -----------------------------------------------------------------
    # Diagnostics
    # -----------------------------------------------------------------
    def snapshot(self) -> dict:
        """Full instantaneous state — merges all observer captures at
        the current step (or computes directly if no observers)."""
        rc = RegimeClassifierObserver()
        topo = TopologyObserver(cadence=1)
        energy = EnergyBudgetObserver()
        return {
            "t": self.time,
            "step_count": self.step_count,
            "regime": rc._capture(self),
            "topology": topo._capture(self),
            "energy": energy._capture(self),
        }

    def history(self) -> dict[str, list]:
        """Return all observer histories keyed by observer class name."""
        out = {}
        for obs in self._observers:
            key = obs.__class__.__name__
            if isinstance(obs, ScalarObserver):
                key = obs.name
            out[key] = obs.history
        return out

    # -----------------------------------------------------------------
    # User-facing conversions
    # -----------------------------------------------------------------
    def amp_display(self, amp_vsnap: float) -> float:
        """Convert internal V_SNAP amplitude back to user-convention units."""
        return amp_to_display(amp_vsnap, self.amplitude_convention)

    def regime_of(self, A2: float) -> str:
        """Classify a given A² value into one of Rg I/II/III/IV."""
        if A2 < _REGIME_I_BOUND_A2:
            return "I"
        if A2 < _REGIME_II_BOUND_A2:
            return "II"
        if A2 < _RUPTURE_BOUND_A2:
            return "III"
        return "IV"
