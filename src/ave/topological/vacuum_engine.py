"""
AVE Fundamental 3D Vacuum Engine.

Implements the design from `research/_archive/L3_electron_soliton/46_vacuum_engine_scope.md`:
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

A-034 + Q-G47 framework context (2026-05-15 evening)
----------------------------------------------------
This engine instantiates the substrate-scale instance of A-034 (Universal
Saturation-Kernel Strain-Snap Mechanism). The Axiom-4 saturation kernel
S(A) = √(1−A²) is the universal mechanism governing every topological-
reorganization event at every scale (19-instance catalog spanning 21 orders
of magnitude). At substrate scale, the K4 magic-angle K(u_0*) = 2G(u_0*)
IS the substrate-scale expression of S(A*) = 0 — the substrate is
"frozen at the saturation boundary" where bound-state solitons stabilize.

`AutoresonantCWSource` implements the phased-array PLL autoresonant mode
of the A-034 measurement-hierarchy framing (per Grant 2026-05-15: "phased
array creates a standing wave if PLL/autoresonant"). Same mechanism as
Propulsion Ch 5 autoresonant rupture, applied to coherent kernel
amplification rather than energy delivery.

Cross-refs: research/_archive/L5/axiom_derivation_status.md (A-032 + A-034);
backmatter/07_universal_saturation_kernel.tex (catalog);
research/_archive/L3_electron_soliton/2026-05-15_A-034_measurement_hierarchy_*.md.

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
- research/_archive/L3_electron_soliton/46_vacuum_engine_scope.md (design scope + C-findings)
- research/_archive/L3_electron_soliton/47_thermal_lattice_noise.md (σ_V, σ_ω derivations)
- research/_archive/L3_electron_soliton/49_dark_wake_bemf_foc_synthesis.md (ecosystem synthesis)
- research/_archive/L3_electron_soliton/42_coupled_simulator_validation.md (Phase II Coupled* core)
- AVE-Propulsion/src/scripts/simulate_warp_metric_tensors.py (τ_zx source)
- AVE-Propulsion/manuscript/vol_propulsion/chapters/05_autoresonant_dielectric_rupture.tex (PLL picture)
- AVE-PONDER/src/scripts/generate_ponder_01_spice_netlist.py (η_vac calibration K_0=0.208)
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Callable, Optional

import numpy as np

from ave.core.constants import ALPHA
from ave.topological.k4_cosserat_coupling import (
    CoupledK4Cosserat,
    _cosserat_A_squared,
    _v_squared_per_site,
)

# ─────────────────────────────────────────────────────────────────
# K4 port-direction geometry (for plane-source port weighting)
# ─────────────────────────────────────────────────────────────────
# Port-direction unit vectors (A→B direction vectors, normalized).
# Needed here to avoid a library-imports-from-script dependency on
# photon_propagation.py (where this logic previously lived).
_PORT_HAT = np.array(
    [
        [+1, +1, +1],
        [+1, -1, -1],
        [-1, +1, -1],
        [-1, -1, +1],
    ],
    dtype=float,
) / np.sqrt(3.0)


def _forward_t2_port_weights(direction: tuple[float, float, float]) -> np.ndarray:
    """T₂-projected forward port weights for a +d̂ plane-wave source.

    See `research/_archive/L3_electron_soliton/30_photon_identification.md` and the
    original `photon_propagation.forward_port_weights`. Raw weights
    `max(0, −d̂·p̂_n)`, then A₁ projection (subtract mean) to get the
    T₂-only photon pattern, then L² normalization.
    """
    d = np.asarray(direction, dtype=float)
    d = d / np.linalg.norm(d)
    w = np.maximum(0.0, -_PORT_HAT @ d)
    w = w - w.mean()  # project onto T₂
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
_REGIME_I_BOUND_A2 = 2.0 * ALPHA  # ≈ 0.0146
_REGIME_II_BOUND_A2 = 3.0 / 4.0  # = 0.75
_RUPTURE_BOUND_A2 = 1.0


def amp_to_vsnap_units(amp: float, convention: str) -> float:
    """Convert user-supplied amplitude to V_SNAP internal units."""
    if convention == "V_SNAP":
        return float(amp)
    elif convention == "V_YIELD":
        return float(amp) * _V_YIELD_FRAC
    else:
        raise ValueError(f"Unknown convention {convention!r}; " "use 'V_SNAP' or 'V_YIELD'")


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
        amplitude: float,  # in user convention units
        omega: float,  # carrier frequency (natural units)
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
        self._yz_profile = np.exp(-r2 / (2.0 * self.sigma_yz**2))

    def apply(self, engine: "VacuumEngine3D", t: float) -> None:
        self._init_if_needed(engine)
        env = np.exp(-((t - self.t_center) ** 2) / (2.0 * self.t_sigma**2))
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
                per_step_energy += float(np.sum(contrib**2))
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
        amplitude: float,  # in user convention units
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
        self._yz_profile = np.exp(-r2 / (2.0 * self.sigma_yz**2))

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
                per_step_energy += float(np.sum(contrib**2))
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
        A2_k4 = V_sq / (engine.V_SNAP**2)
        A2_cos = _cosserat_A_squared(
            engine.cos.u,
            engine.cos.omega,
            engine.cos.dx,
            engine.cos.omega_yield,
            engine.cos.epsilon_yield,
        )
        A2 = A2_k4 + A2_cos
        alive = engine.k4.mask_active
        rg1 = int(np.sum(alive & (A2 < _REGIME_I_BOUND_A2)))
        rg2 = int(np.sum(alive & (A2 >= _REGIME_I_BOUND_A2) & (A2 < _REGIME_II_BOUND_A2)))
        rg3 = int(np.sum(alive & (A2 >= _REGIME_II_BOUND_A2) & (A2 < _RUPTURE_BOUND_A2)))
        rupture = int(np.sum(alive & (A2 >= _RUPTURE_BOUND_A2)))
        return {
            "t": engine.time,
            "rg_I": rg1,
            "rg_II": rg2,
            "rg_III": rg3,
            "rupture": rupture,
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
      - research/_archive/L3_electron_soliton/54_pair_production_axiom_derivation.md §3, §9.2
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
        A2_k4 = V_sq / (engine.V_SNAP**2)
        A2_cos = _cosserat_A_squared(
            engine.cos.u,
            engine.cos.omega,
            engine.cos.dx,
            engine.cos.omega_yield,
            engine.cos.epsilon_yield,
        )
        return A2_k4 + A2_cos  # Pythagorean sum, both canonical r²

    def _capture(self, engine: "VacuumEngine3D") -> dict:
        Phi = engine.k4.Phi_link
        mask_A = engine.k4.mask_A

        # Site-level A²_yield for saturation detection
        A2_yield = self._compute_A2_yield(engine)
        saturated_site = A2_yield >= self.saturation_frac

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
        phi_sat_flat = []  # bonds with both endpoints saturated
        phi_unsat_flat = []  # bonds with at least one unsaturated endpoint
        for port, shift_to_B in enumerate(port_shifts):
            # To get the B-neighbor's A²_yield at each A-site position,
            # we roll the saturated_site field OPPOSITE the shift_to_B
            # direction (because B is at -shift_to_B relative to A's
            # storage slot — see the k4_tlm.py connect step comments).
            inverse_shift = tuple(-s for s in shift_to_B)
            sat_B_at_A = np.roll(
                saturated_site,
                shift=inverse_shift,
                axis=(0, 1, 2),
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
            return float(np.sqrt(np.mean(x**2))) if x.size > 0 else 0.0

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
      - research/_archive/L3_electron_soliton/54_pair_production_axiom_derivation.md §4
      - manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex:127-142
    """

    def _capture(self, engine: "VacuumEngine3D") -> dict:
        # Under Vol 4 Ch 1:711 subatomic override, V_yield ≡ V_SNAP at
        # VacuumEngine3D's operating scale. A²_K4 = V²/V_SNAP² IS canonical
        # r² per Vol 1 Ch 7:12; no /α conversion needed. Cosserat's A² is
        # yield-normalized to its own ε_yield/ω_yield thresholds, also
        # canonical r² at subatomic scale (ε_yield=1 is TKI-derived).
        # See research/_archive/L3_electron_soliton/50_autoresonant_pair_creation.md
        # §0.1 r3 and VACUUM_ENGINE_MANUAL §17 A14 r6.
        V_sq = _v_squared_per_site(engine.k4.V_inc)
        A2_k4 = V_sq / (engine.V_SNAP**2)
        A2_cos = _cosserat_A_squared(
            engine.cos.u,
            engine.cos.omega,
            engine.cos.dx,
            engine.cos.omega_yield,
            engine.cos.epsilon_yield,
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
            self.threshold_frac = min(threshold_fracs) if threshold_fracs else 0.3
        else:
            self.threshold_frac = float(threshold_frac)
        self.threshold_fracs = [float(t) for t in threshold_fracs] if threshold_fracs else None

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

    Implementation (Stage 4c → Phase-5-prep G-12, 2026-04-23):
        The instantaneous local strain A² = V²/V_SNAP² near the source
        shifts the lattice's effective resonance per Axiom-4 varactor
        softening. The source tracks this shift by adjusting its drive
        frequency via the **axiom-native varactor form**:

            ω(t) = ω_0 · max(ε, (1 − A²_probe(t))^(1/4))

        This is the Ω_node / ω_0 softening from Vol 4 Ch 1:127-142 and
        doc 54_ §4 — the same form implemented in NodeResonanceObserver.
        Zero free parameters.

        **Previously (Stage 4c, pre-G-12):** linear-Taylor approximation
            ω(t) = ω_0 · (1 − K_drift · A²_probe)
        with empirical K_drift = 0.5. The linear form diverges from the
        varactor by ~5 % at A² > 0.3 — fatal for Phase 5's autoresonant
        lock condition `|Ω_node − ω_drive| < δ_lock = ω_0·α ≈ 7×10⁻³·ω_0`
        (700× the precision window). G-12 replaces with the exact form;
        see VACUUM_ENGINE_MANUAL §17 A7 and plan file Phase 3.5 step 16.

    Key implementation detail: maintains an internal PHASE ACCUMULATOR
    rather than using t directly. Otherwise changes in ω would cause
    phase discontinuities.

    Args:
        x0, direction, amplitude, omega, sigma_yz, t_ramp, t_sustain, ...:
            same as CWSource
        K_drift: DEPRECATED as of G-12. Retained for backward-compat of
            existing driver scripts; not used in the axiom-native form.
            Non-default values (≠ 0.5) emit DeprecationWarning.
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
            x0=x0,
            direction=direction,
            amplitude=amplitude,
            omega=omega,
            sigma_yz=sigma_yz,
            t_ramp=t_ramp,
            t_sustain=t_sustain,
            t_decay=t_decay,
            y_c=y_c,
            z_c=z_c,
        )
        # K_drift deprecated per G-12 (axiom-native varactor form).
        # Retained as attribute for backward compat of external inspectors
        # (e.g., existing driver scripts that log K_drift). Non-default
        # values emit a DeprecationWarning since the axiom-native form
        # has no tunable gain.
        if not np.isclose(K_drift, 0.5):
            import warnings

            warnings.warn(
                "AutoresonantCWSource.K_drift is deprecated (G-12, Phase 5 "
                "prep). The axiom-native varactor form ω(t) = ω_0·(1−A²)^(1/4) "
                "replaces the linear-Taylor approximation and has no tunable "
                "gain. K_drift is ignored. See doc 54_ §4 and VACUUM_ENGINE_"
                "MANUAL §17 A7.",
                DeprecationWarning,
                stacklevel=2,
            )
        self.K_drift = float(K_drift)  # retained as attribute; not used
        self.probe_x_offset = int(probe_x_offset)
        self._omega_0 = float(omega)  # nominal (unshifted) frequency
        self._omega_current = self._omega_0  # shifts over time
        self._accumulated_phase = 0.0
        self._last_t = None
        self._omega_history: list[float] = []
        self._probe_A_sq_history: list[float] = []

    def _measure_probe_A_sq(self, engine: "VacuumEngine3D") -> float:
        dx_sign = int(np.sign(self.direction[0])) if self.direction[0] != 0 else 1
        probe_x = self.x0 + self.probe_x_offset * dx_sign
        probe_x = int(np.clip(probe_x, 0, engine.N - 1))
        V_inc_slab = engine.k4.V_inc[probe_x]  # (ny, nz, 4)
        V_sq = np.sum(V_inc_slab**2, axis=-1)  # (ny, nz)
        active = engine.k4.mask_active[probe_x]
        if not active.any():
            return 0.0
        return float(V_sq[active].max() / (engine.V_SNAP**2))

    def apply(self, engine: "VacuumEngine3D", t: float) -> None:
        self._init_if_needed(engine)

        # Advance phase accumulator by ω_current · dt (dt = outer_dt)
        dt = engine.outer_dt if self._last_t is not None else 0.0
        self._accumulated_phase += self._omega_current * dt
        self._last_t = t

        # Measure probe strain
        A_sq_probe = self._measure_probe_A_sq(engine)
        self._probe_A_sq_history.append(A_sq_probe)

        # Autoresonant frequency shift — Ax4-native varactor form
        # (G-12, Phase 5 precision prereq). Ω_node / ω_0 = (1 − A²_probe)^(1/4)
        # per Vol 4 Ch 1:127-142 + doc 54_ §4. Clip A² < 1 for past-rupture
        # numerical safety; floor shift_factor at 1e-3 to prevent ω → 0
        # integration singularity (same convention as pre-G-12).
        A_clipped = min(A_sq_probe, 1.0 - 1e-12)
        shift_factor = max(1e-3, (1.0 - A_clipped) ** 0.25)
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
                per_step_energy += float(np.sum(contrib**2))
        self.cumulative_energy_injected += per_step_energy


class CosseratBeltramiSource(Source):
    """Direct-injection Cosserat-ω chirality source — Phase 5 prereq G-11(c).

    Bypasses K4-port circular-polarization ambiguity (forward K4 ports
    p₀=(+1,+1,+1), p₁=(+1,−1,−1) both lie along the (y+z)/√2 transverse
    axis, so "circular polarization" via port weights is underdetermined)
    by directly injecting a time-varying helical ω pattern at a source
    slab. The Cosserat integrator then propagates the helical structure
    downstream; Phase 4's `_beltrami_helicity` reads h_local from the
    resulting ω field.

    Physical setup: for a Beltrami wave traveling in +x with ∇×ω = ±k·ω:

        ω(x, t) = A · (0, cos(kx − ω_drive·t), ∓sin(kx − ω_drive·t))

    Sign convention: upper sign is RH (∇×ω = +k·ω, h_local = +1, biases
    A²_μ higher per doc 54_ §6); lower sign is LH.

    At a fixed source slab x = x₀:
        RH: ω_source(t) = A · env(t) · (0, cos(ω_drive·t), +sin(ω_drive·t))
        LH: ω_source(t) = A · env(t) · (0, cos(ω_drive·t), −sin(ω_drive·t))

    Transverse (y, z) profile is a Gaussian (same as CWSource), weighted
    by the Cosserat active-site mask. ω is OVERWRITTEN at the source slab
    each step (not added) — additive semantics would accumulate across
    steps and give non-physical drift.

    Amplitude sizing for Phase 4 Meissner regime:
        |κ| = |∂_x ω| ~ amp · k on a Beltrami wave
        A²_μ_base = (|κ| / ω_yield)² = (amp·k/π)²  (with ω_yield=π default)
        For A²_μ_base = 1 (saturation), amp_sat = π / k = λ / 2
        Phase III-B canonical λ=3.5: amp_sat ≈ 1.75

    Coupling to K4: this source does NOT inject V. The K4 sector
    responds to Cosserat ω via the asymmetric coupling path
    (_update_z_local_total + _compute_coupling_force_on_cosserat).
    Helical ω → helical Γ² confinement wall → K4 scatter sees modified
    Z_eff. This tests the Phase 4 Meissner mechanism under driven
    chirality — the minimum-viable pair-creation-drive scenario.

    References:
    - doc 54_ §6 (asymmetric μ/ε saturation mechanism)
    - research/_archive/L3_electron_soliton/20_chirality_projection_sub_theorem.md
      (κ_chiral = 1.2·α derivation for electron (2,3) winding)
    - STAGE6_V4_HANDOFF §9 G-11 option (c)
    - Vol 1 Ch 7:252 (symmetric vs asymmetric saturation)

    Usage:
        engine.add_source(CosseratBeltramiSource(
            x0=4, propagation_axis=0, amplitude=1.75,
            omega=2*np.pi/3.5,        # Phase III-B canonical λ
            handedness="RH",          # or "LH"
            sigma_yz=3.0,
            t_ramp=20, t_sustain=200,
        ))

    Args:
        x0: source slab index along propagation axis
        propagation_axis: 0=x, 1=y, 2=z — axis along which the wave
            propagates; ω rotates in the transverse plane
        amplitude: peak |ω| magnitude (natural-unit rad; no V_SNAP
            conversion since this is Cosserat sector, not K4)
        omega: drive carrier frequency (natural units, rad/τ_node)
        handedness: "RH" or "LH"
        sigma_yz: transverse Gaussian width at source slab
        t_ramp, t_sustain, t_decay: envelope timing (same semantics as CWSource)
        y_c, z_c: transverse Gaussian center (default: lattice center)
    """

    def __init__(
        self,
        x0: int,
        propagation_axis: int,
        amplitude: float,
        omega: float,
        handedness: str,
        sigma_yz: float,
        t_ramp: float,
        t_sustain: float,
        t_decay: Optional[float] = None,
        y_c: Optional[float] = None,
        z_c: Optional[float] = None,
    ):
        if propagation_axis not in (0, 1, 2):
            raise ValueError(f"propagation_axis must be 0/1/2, got {propagation_axis}")
        if handedness not in ("RH", "LH"):
            raise ValueError(f"handedness must be 'RH' or 'LH', got {handedness!r}")
        self.x0 = int(x0)
        self.propagation_axis = int(propagation_axis)
        self.amplitude = float(amplitude)
        self.omega = float(omega)
        self.handedness = str(handedness)
        self.sigma_yz = float(sigma_yz)
        self.t_ramp = float(t_ramp)
        self.t_sustain = float(t_sustain)
        self.t_decay = float(t_decay) if t_decay is not None else 0.0
        self.y_c = y_c
        self.z_c = z_c
        self._transverse_profile = None
        # Helicity sign: +1 for RH, -1 for LH
        self._sign = +1 if handedness == "RH" else -1
        # Transverse axes (the two axes orthogonal to propagation_axis)
        self._trans_axes = tuple(i for i in (0, 1, 2) if i != self.propagation_axis)
        self.cumulative_action_injected = 0.0

    def envelope(self, t: float) -> float:
        """Ramp/sustain/decay envelope (same as CWSource)."""
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
        if self._transverse_profile is not None:
            return
        N = engine.N
        # Build 2D Gaussian profile on the transverse plane
        ax1, ax2 = self._trans_axes
        yc = (N - 1) / 2.0 if self.y_c is None else self.y_c
        zc = (N - 1) / 2.0 if self.z_c is None else self.z_c
        j, k = np.indices((N, N), dtype=float)
        r2 = (j - yc) ** 2 + (k - zc) ** 2
        self._transverse_profile = np.exp(-r2 / (2.0 * self.sigma_yz**2))

    def apply(self, engine: "VacuumEngine3D", t: float) -> None:
        """Overwrite ω at source slab with helical drive pattern.

        Strategy: at each step, explicitly SET ω at the source slab to
        the desired helical pattern. Cosserat velocity-Verlet propagates
        the pattern downstream. The source slab's ω history acts as a
        Dirichlet-style boundary condition on the Cosserat dynamics.
        """
        self._init_if_needed(engine)
        env = self.envelope(t)
        if env <= 0:
            return

        amp_current = self.amplitude * env
        # Transverse ω components (the two non-propagation axes)
        # RH: (cos(ω·t), +sin(ω·t))
        # LH: (cos(ω·t), −sin(ω·t))
        c_t = np.cos(self.omega * t)
        s_t = np.sin(self.omega * t) * self._sign

        # Apply to the propagation-axis slab of the Cosserat ω field
        # Cosserat ω has shape (N, N, N, 3); we index along propagation_axis
        active_slab = self._slab_active_mask(engine)  # (N, N)
        pattern = amp_current * self._transverse_profile * active_slab  # (N, N)

        ax1, ax2 = self._trans_axes
        # Build full (N, N, N, 3) field with zeros elsewhere, set the slab
        slab_view = self._slab_omega_view(engine)  # view into ω at x=x0 slab, shape (N, N, 3)
        # Zero the source slab first (clean overwrite)
        slab_view[...] = 0.0
        slab_view[..., ax1] = pattern * c_t
        slab_view[..., ax2] = pattern * s_t

        # Track injected action (|ω|² integrated, for diagnostics)
        self.cumulative_action_injected += float(np.sum(pattern**2) * (c_t**2 + s_t**2))

    def _slab_active_mask(self, engine: "VacuumEngine3D") -> np.ndarray:
        """Return (N, N) boolean mask of active Cosserat sites at x0 slab."""
        if self.propagation_axis == 0:
            return engine.cos.mask_alive[self.x0].astype(float)
        if self.propagation_axis == 1:
            return engine.cos.mask_alive[:, self.x0].astype(float)
        return engine.cos.mask_alive[:, :, self.x0].astype(float)

    def _slab_omega_view(self, engine: "VacuumEngine3D") -> np.ndarray:
        """Return a WRITEABLE view/slice of engine.cos.omega at the source slab."""
        if self.propagation_axis == 0:
            return engine.cos.omega[self.x0]
        if self.propagation_axis == 1:
            return engine.cos.omega[:, self.x0]
        return engine.cos.omega[:, :, self.x0]


class SpatialDipoleCPSource(Source):
    """Circularly-polarized K4 V_inc source via spatial-dipole modulation —
    G-11(a) option per STAGE6_V4_HANDOFF §9.

    Physical approach: two 90°-phase-shifted dipole patterns at the
    source plane give effectively circularly-polarized EM radiation
    along the propagation axis. The transverse (y, z) structure is a
    Gaussian-windowed linear gradient in y AND z, with quadrature phase:

        V(y, z, t) = A · env(t) · [
            cos(ω·t) · (y − y_c) · exp(−r²/2σ²) · port_weights_y
            + sin(ω·t) · ε_hand · (z − z_c) · exp(−r²/2σ²) · port_weights_z
        ]

    where r² = (y−y_c)² + (z−z_c²) and ε_hand ∈ {+1, −1} selects RH/LH.

    Design rationale vs G-11(c) CosseratBeltramiSource:
        (c) CosseratBeltramiSource bypasses the K4-port circular-
            polarization ambiguity by injecting ω directly. Useful for
            MECHANISM tests (chirality→Meissner coupling).
        (a) SpatialDipoleCPSource drives K4 V_inc directly — the
            coupling chain K4 V → Cosserat ω → asymmetric saturation
            is exercised end-to-end. Closer to a physical EM drive
            (think: a focused CP laser entering the vacuum).

    Port weighting (for propagation_axis=0, +x direction):
        Forward ports are p₀=(+1,+1,+1) and p₁=(+1,−1,−1). Their y-
        components are (+1, −1) and z-components are (+1, −1). So:
            y-dipole weights:  port_0 = +1, port_1 = −1
            z-dipole weights:  port_0 = +1, port_1 = −1
        Both dipole patterns share the same port weights because both
        forward ports have coincident (y+z)-axis alignment (this is
        the very (y+z)/√2 spanning that motivated the G-11 design
        question in the first place). Dipole MODULATION g_y(y,z) vs
        g_z(y,z) is what distinguishes y-pol from z-pol — not port
        weight differences.

    **Physics caveat:** the resulting wave is a dipole-radiation
    pattern, NOT a pure plane wave. For Gaussian focal spots (as used
    in real laser experiments), this is actually closer to physical
    reality than a flat plane wave would be. Full validation of the
    CP signature at the source and in the downstream coupling is
    deferred to Phase 5 + a driver script (see handoff §9-13).

    Args:
        x0: source plane index along propagation axis
        propagation_axis: 0/1/2 for x/y/z
        amplitude: peak V amplitude in user convention (V_SNAP units by default)
        omega: carrier frequency (natural rad/τ_node)
        handedness: "RH" or "LH"
        sigma_yz: Gaussian width of transverse envelope
        t_ramp, t_sustain, t_decay: envelope timing (CWSource semantics)
        y_c, z_c: transverse center (default: lattice center)

    References:
        - STAGE6_V4_HANDOFF.md §9 G-11 option (a)
        - research/_archive/L3_electron_soliton/54_pair_production_axiom_derivation.md §6
        - existing CWSource for envelope + port-weight conventions
    """

    def __init__(
        self,
        x0: int,
        propagation_axis: int,
        amplitude: float,
        omega: float,
        handedness: str,
        sigma_yz: float,
        t_ramp: float,
        t_sustain: float,
        t_decay: Optional[float] = None,
        y_c: Optional[float] = None,
        z_c: Optional[float] = None,
    ):
        if propagation_axis not in (0, 1, 2):
            raise ValueError(f"propagation_axis must be 0/1/2, got {propagation_axis}")
        if handedness not in ("RH", "LH"):
            raise ValueError(f"handedness must be 'RH' or 'LH', got {handedness!r}")
        self.x0 = int(x0)
        self.propagation_axis = int(propagation_axis)
        self.amplitude = float(amplitude)
        self.omega = float(omega)
        self.handedness = str(handedness)
        self.sigma_yz = float(sigma_yz)
        self.t_ramp = float(t_ramp)
        self.t_sustain = float(t_sustain)
        self.t_decay = float(t_decay) if t_decay is not None else 0.0
        self.y_c = y_c
        self.z_c = z_c
        self._eps_hand = +1 if handedness == "RH" else -1
        self._trans_axes = tuple(i for i in (0, 1, 2) if i != self.propagation_axis)
        # Lazy-init: per-direction port weights + dipole profiles
        self._port_w_prop = None
        self._g_y_profile = None  # (N, N) y-dipole Gaussian
        self._g_z_profile = None  # (N, N) z-dipole Gaussian
        self.cumulative_energy_injected = 0.0

    def envelope(self, t: float) -> float:
        """Ramp/sustain/decay envelope (same as CWSource)."""
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
        if self._port_w_prop is not None:
            return
        # Port weights for propagation direction (reuse T₂ projection from CWSource)
        direction = tuple(1.0 if i == self.propagation_axis else 0.0 for i in range(3))
        self._port_w_prop = _forward_t2_port_weights(direction)
        # Build 2D transverse-plane dipole profiles
        N = engine.N
        yc = (N - 1) / 2.0 if self.y_c is None else self.y_c
        zc = (N - 1) / 2.0 if self.z_c is None else self.z_c
        j, k = np.indices((N, N), dtype=float)
        r2 = (j - yc) ** 2 + (k - zc) ** 2
        gauss_env = np.exp(-r2 / (2.0 * self.sigma_yz**2))
        # y-dipole: Gaussian × (y − y_c)
        self._g_y_profile = (j - yc) * gauss_env
        # z-dipole: Gaussian × (z − z_c)
        self._g_z_profile = (k - zc) * gauss_env

    def apply(self, engine: "VacuumEngine3D", t: float) -> None:
        """Inject CP V_inc at the source plane via dipole modulation."""
        self._init_if_needed(engine)
        env = self.envelope(t)
        if env <= 0:
            return
        c_t = np.cos(self.omega * t)
        s_t = np.sin(self.omega * t) * self._eps_hand
        amp_internal = amp_to_vsnap_units(self.amplitude, engine.amplitude_convention)
        amp_volts = amp_internal * engine.V_SNAP * env
        if abs(amp_volts) < 1e-30:
            return

        # Combined spatial pattern at source plane (2D y, z)
        # Y-pol component (cos) + Z-pol component (sin·ε_hand)
        pattern = amp_volts * (c_t * self._g_y_profile + s_t * self._g_z_profile)
        # Respect K4 active mask at source plane
        active_slice = engine.k4.mask_active[self.x0].astype(float)
        injection = pattern * active_slice

        per_step_energy = 0.0
        for n in range(4):
            if self._port_w_prop[n] != 0:
                contrib = self._port_w_prop[n] * injection
                engine.k4.V_inc[self.x0, :, :, n] += contrib
                per_step_energy += float(np.sum(contrib**2))
        self.cumulative_energy_injected += per_step_energy


class PairNucleationGate(Observer):
    """Phase 5 pair nucleation gate — observer-with-side-effect per doc 54_ §7.

    The physical event: a Kelvin-style vortex pair nucleates inside a
    Bingham-plastic capsule. This is the axiom-native AVE picture of an
    electron-positron pair.

    **Bingham-plastic vacuum** (Vol 4 Ch 1:189-203 TVS Zener / Slipstream
    Transition):
        Below V_yield: η_eff = η₀ > 0 — solid, high drag, rigid
        Above V_yield: η_eff = 0     — Zero-Impedance Slipstream,
                                       frictionless (the Kelvin regime)

    **Capsule mechanism:** when both endpoints of an A→B bond reach
    Meissner saturation (A²_μ ≥ 1), the local material is punched past
    yield into the slipstream regime. Γ → −1 walls form at each
    endpoint (impedance boundaries between the slipstream pocket and
    the surrounding sub-yield solid). A Bingham-plastic capsule is
    formed: flowing-slipstream interior, rigid-solid exterior, Γ=-1
    walls at A and B. Inside this capsule, Kelvin's "perfect
    incompressible frictionless fluid" theorem applies — vortex knots
    are topologically protected (Kelvin 1867: "two ring atoms linked
    together or one knotted in any manner... can never deviate from
    its own peculiarity of multiple continuity").

    The gate detects capsule formation and INJECTS the vortex pair:
        LH Beltrami vortex at r_A
        RH Beltrami vortex at r_B
        Φ_link[A, port] = ±Φ_critical  (sign from lattice chirality)

    Gate conditions per doc 54_ §7:
        C1 (both endpoints Meissner-saturated):
            A²_μ(r_A) ≥ sat_frac AND A²_μ(r_B) ≥ sat_frac
        C2 (autoresonant lock at this pair — drive frequency hits
            the Duffing-softened resonance of the saturated tank):
            |Ω_node(r_A) − ω_drive| < δ_lock
            where δ_lock = ω_drive · α (Q = 1/α per doc 27_).

    Zero free parameters: sat_frac = 1 (Ax4 rupture threshold; default
    0.95 for numerical safety), δ_lock_fraction = α (Q = 1/α derived
    per doc 27_), Beltrami amp calibrated to bond energy = m_e c²
    (= 1 in natural units with I_ω = 1).

    Gate never fires twice for the same bond (tracked in _nucleated_bonds).

    **Injection profile (first-pass): point-rotation Beltrami.**
        ω_A = -amp · p̂_bond    (rotation axis anti-aligned with bond, LH)
        ω_B = +amp · p̂_bond    (rotation axis aligned, RH)
        amp = √2  (so ½·I_ω·|ω|² per site = 1 = m_e c² rest energy)

    Per STAGE6_V4_HANDOFF §9 open question #1: if Beltrami pair
    dissipates faster than 10 Compton periods post-drive-shutoff
    (pre-registered P_phase5_nucleation), upgrade to localized Hopf
    fibration or (2,3) torus-knot injection. Grant's chosen test
    plan (#1): Beltrami first, test persistence, escalate if needed.
    Kelvin's topological-protection claim is what this tests at
    discrete-lattice scale.

    References:
        - research/_archive/L3_electron_soliton/54_pair_production_axiom_derivation.md §7
        - research/_archive/L3_electron_soliton/27_step6_phase_space_Q.md (Q=1/α derivation)
        - manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex:189-203
          (Bingham plastic / TVS Zener / Slipstream)
        - Kelvin 1867 "On Vortex Atoms" — topological protection in frictionless fluid
        - STAGE6_V4_HANDOFF.md §9 G-13 / Phase 5 deferred items
    """

    # Tetrahedral A→B port vectors (from k4_tlm.py:164)
    _PORT_VECTORS = np.array(
        [
            [+1, +1, +1],
            [+1, -1, -1],
            [-1, +1, -1],
            [-1, -1, +1],
        ],
        dtype=float,
    )

    def __init__(
        self,
        cadence: int = 1,
        saturation_frac: float = 0.95,
        delta_lock_fraction: Optional[float] = None,
        injection_amplitude: Optional[float] = None,
        phi_critical: float = 1.0,
    ):
        """
        Args:
            cadence: observer step cadence
            saturation_frac: C1 threshold on A²_μ per endpoint.
                0.95 default for numerical safety (exact 1.0 is the
                Ax4 rupture boundary — near-singular kernel).
            delta_lock_fraction: fraction of ω_drive for δ_lock
                tolerance. None → use ALPHA = 7.297e-3 (Q = 1/α per
                doc 27_). Override only for calibration experiments.
            injection_amplitude: Beltrami-rotor amplitude per site.
                None → √2 (calibrated to ½·I_ω·|ω|² = 1 = m_e c² per
                vortex in natural units, with I_ω = 1).
            phi_critical: |Φ_link| magnitude at injection time.
                Default 1.0 = V_SNAP·τ_node natural unit.
        """
        super().__init__(cadence=cadence)
        self.saturation_frac = float(saturation_frac)
        self.delta_lock_fraction = float(delta_lock_fraction) if delta_lock_fraction is not None else float(ALPHA)
        self.injection_amplitude = (
            float(injection_amplitude) if injection_amplitude is not None else float(np.sqrt(2.0))
        )
        self.phi_critical = float(phi_critical)
        # Bonds already nucleated — prevent re-firing
        self._nucleated_bonds: set[tuple[int, int, int, int]] = set()
        # Total firing count across engine lifetime
        self._total_firings: int = 0

    def _compute_A2_mu(self, engine: "VacuumEngine3D") -> np.ndarray:
        """Return A²_μ field across the lattice (magnetic sector only).

        Under Phase 4 asymmetric saturation, A²_μ = κ²/ω_yield² +
        chirality bias. For gate-detection purposes we compute the
        per-site A²_μ directly from the Cosserat curvature.
        """
        import jax.numpy as jnp

        from ave.topological.cosserat_field_3d import (
            KAPPA_CHIRAL_ELECTRON,
            _beltrami_helicity,
            _compute_curvature,
        )

        w_j = jnp.asarray(engine.cos.omega)
        kappa = _compute_curvature(w_j, engine.cos.dx)
        kappa_sq = jnp.sum(kappa * kappa, axis=(-1, -2))
        A2_mu_base = kappa_sq / (engine.cos.omega_yield**2)
        # Chirality bias (same form as _update_saturation_kernels)
        h_local = _beltrami_helicity(w_j, engine.cos.dx)
        kappa_chi = engine._coupled.kappa_chiral if engine._coupled.use_asymmetric_saturation else 0.0
        A2_mu = (1.0 + kappa_chi * h_local) * A2_mu_base
        return np.asarray(A2_mu)

    def _compute_Omega_node(self, engine: "VacuumEngine3D") -> np.ndarray:
        """Ω_node / ω_yield = (1 − A²_yield)^(1/4) per doc 54_ §4.

        Same form NodeResonanceObserver uses. Under R4 subatomic
        override (Vol 4 Ch 1:711), A²_yield = A²_total in the engine's
        canonical units (no /α conversion).
        """
        import jax.numpy as jnp

        from ave.topological.cosserat_field_3d import _update_saturation_kernels

        V_sq = _v_squared_per_site(engine.k4.V_inc)
        S_mu, S_eps = _update_saturation_kernels(
            jnp.asarray(engine.cos.u),
            jnp.asarray(engine.cos.omega),
            jnp.asarray(V_sq),
            engine.cos.dx,
            engine.V_SNAP,
            engine.cos.omega_yield,
            engine.cos.epsilon_yield,
            engine._coupled.kappa_chiral,
        )
        # Pythagorean-like combined kernel for Ω_node
        S_combined = np.sqrt(np.asarray(S_mu) * np.asarray(S_eps))
        # Ω_node / ω_yield ~ S^(1/2) = (1-A²)^(1/4)
        return engine.cos.omega_yield * np.sqrt(np.maximum(S_combined, 1e-12))

    def _candidate_bonds(self, engine: "VacuumEngine3D") -> list[tuple]:
        """Enumerate A-site bonds to scan. Returns list of (A_idx, port, B_idx)."""
        N = engine.N
        # Find A-sites (mask_A), check each of 4 ports for in-bounds B-neighbor
        A_coords = np.argwhere(engine.k4.mask_A)
        bonds = []
        for A_coord in A_coords:
            A_idx = tuple(A_coord)
            for port in range(4):
                p = self._PORT_VECTORS[port].astype(int)
                B_idx = tuple(A_coord + p)
                # In-bounds + B-site active check
                if all(0 <= B_idx[i] < N for i in range(3)):
                    if engine.k4.mask_B[B_idx]:
                        bonds.append((A_idx, port, B_idx))
        return bonds

    def _drive_frequencies(self, engine: "VacuumEngine3D") -> list[float]:
        """Extract drive frequencies from any sources that have an omega."""
        freqs = []
        for src in engine._sources:
            if hasattr(src, "omega"):
                # For autoresonant sources, use current (shifted) ω
                if hasattr(src, "_omega_current"):
                    freqs.append(float(src._omega_current))
                else:
                    freqs.append(float(src.omega))
        return freqs

    def _c2_lock(
        self,
        omega_node_at_A: float,
        drive_freqs: list[float],
    ) -> Optional[float]:
        """Return the drive frequency that satisfies C2, or None if none does."""
        for omega_drive in drive_freqs:
            delta_lock = self.delta_lock_fraction * omega_drive
            if abs(omega_node_at_A - omega_drive) < delta_lock:
                return omega_drive
        return None

    def _inject_pair(
        self,
        engine: "VacuumEngine3D",
        A_idx: tuple[int, int, int],
        port: int,
        B_idx: tuple[int, int, int],
    ) -> None:
        """Write the Beltrami vortex pair + Φ_link at the bond.

        LH at A, RH at B, per doc 54_ §7. Point-rotation first-pass
        profile (see class docstring): rotation axis along bond
        direction, opposite signs at A and B.
        """
        p_vec = self._PORT_VECTORS[port]
        p_hat = p_vec / np.linalg.norm(p_vec)
        amp = self.injection_amplitude

        # LH at A: ω antiparallel to p̂_bond
        engine.cos.omega[A_idx[0], A_idx[1], A_idx[2], :] = -amp * p_hat
        # RH at B: ω parallel to p̂_bond
        engine.cos.omega[B_idx[0], B_idx[1], B_idx[2], :] = +amp * p_hat

        # Set velocity to zero at injection (pair born at rest)
        engine.cos.omega_dot[A_idx[0], A_idx[1], A_idx[2], :] = 0.0
        engine.cos.omega_dot[B_idx[0], B_idx[1], B_idx[2], :] = 0.0

        # Φ_link on the directed A→B bond (port index)
        # Lattice-chirality sign: alternating per port index (first-pass;
        # could be refined via κ_chiral projection on bond direction)
        sign = +1 if (port % 2 == 0) else -1
        engine.k4.Phi_link[A_idx[0], A_idx[1], A_idx[2], port] = sign * self.phi_critical

    def _capture(self, engine: "VacuumEngine3D") -> dict:
        """Per-step scan: detect C1 ∧ C2, inject pair if both + not yet nucleated.

        Returns diagnostic dict with firing count + this-step firings.
        """
        drive_freqs = self._drive_frequencies(engine)
        fired_this_step: list[tuple] = []

        if not drive_freqs:
            # No driving source → C2 cannot be satisfied → gate idle
            return {
                "t": engine.time,
                "n_nucleated_total": self._total_firings,
                "n_fired_this_step": 0,
                "fired_bonds": [],
                "gate_active": False,
            }

        A2_mu = self._compute_A2_mu(engine)
        Omega_node = self._compute_Omega_node(engine)

        for A_idx, port, B_idx in self._candidate_bonds(engine):
            bond_key = (A_idx[0], A_idx[1], A_idx[2], port)
            if bond_key in self._nucleated_bonds:
                continue  # Never re-fire the same bond
            # C1: both endpoints Meissner-saturated
            if A2_mu[A_idx] < self.saturation_frac or A2_mu[B_idx] < self.saturation_frac:
                continue
            # C2: autoresonant lock
            omega_at_A = float(Omega_node[A_idx])
            locked_drive = self._c2_lock(omega_at_A, drive_freqs)
            if locked_drive is None:
                continue
            # Both conditions met — fire
            self._inject_pair(engine, A_idx, port, B_idx)
            self._nucleated_bonds.add(bond_key)
            self._total_firings += 1
            fired_this_step.append(bond_key)

        return {
            "t": engine.time,
            "n_nucleated_total": self._total_firings,
            "n_fired_this_step": len(fired_this_step),
            "fired_bonds": fired_this_step,
            "gate_active": True,
        }


class DarkWakeObserver(Observer):
    """Dark wake diagnostic — the longitudinal shear strain τ_zx wave that
    propagates backward from any coherent V excitation (per AVE-PONDER
    vol_ponder/ch01 and AVE-Propulsion simulate_warp_metric_tensors.py:84-85).

    Formula (ported from AVE-Propulsion Ch 5 description):
        τ_zx(r) ∝ Z_local(r) · ∂/∂x [|V(r)|²/V_SNAP²]

    Axiom chain (per A47 v11d discipline, added 2026-05-01):
      • Ax 1 (K4 Cosserat crystal; legacy: LC network substrate) provides
        the local impedance Z_local through the bond-LC structure;
        Z_local = √(L_bond / C_bond) at the node level, modulated by the
        saturation kernel.
      • Ax 2 (topo-kinematic isomorphism [Q] ≡ [L]) gives the topological
        charge → flux-linkage equivalence that makes the V_inc/V_ref
        scattering cycle observable as a propagating standing-wave packet.
      • Ax 3 (Minimum Reflection Principle; legacy: effective action
        principle) → Noether currents → momentum conservation. The dark
        wake IS the field-theoretic form of the
        Newton-3rd-law back-reaction: every forward soliton/photon must
        carry an equal-and-opposite longitudinal-shear-strain wave behind
        it, mass-equivalent to the inductive back-EMF (M_inertial ≡ L_drag,
        per higgs_impedance_mapping.py:48-52).
      • Ax 4 (Op14 saturation kernel S(A) = √(1 − A²)) modulates Z_local
        spatially: at A² → A²_yield, Z_eff steepens locally, creating the
        gradient that drives ∂|V|²/∂x → τ_zx. Without saturation modulation,
        the back-EMF response would be uniform; saturation gives it spatial
        structure.

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
        A_sq = V_sq / (engine.V_SNAP**2)

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
        interior_mask[pml : N - pml, pml : N - pml, pml : N - pml] = True
        interior_alive = alive & interior_mask
        max_tau_zx = float(np.abs(tau_zx[interior_alive]).max()) if interior_alive.any() else 0.0

        return {
            "t": engine.time,
            "tau_zx_slab": tau_slab,  # 1D along propagation axis
            "max_tau_zx": max_tau_zx,
            "wake_peak_x": peak_idx,  # -1 if no wake
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
    temperature: float = 0.0  # in m_e c² units (dimensionless)
    amplitude_convention: str = "V_SNAP"
    rho: float = 1.0
    I_omega: float = 1.0
    coupling_kappa: float = 1.0  # S1-D prefactor (C2 proxy for η_vac)
    axiom_4_enabled: bool = True
    V_SNAP_override: Optional[float] = None  # override if using non-SI
    # Phase 4 — asymmetric μ/ε saturation (doc 54_ §6, VACUUM_ENGINE_MANUAL
    # §17 A14 r6 + plan file Phase 3.5 step 17). Default True enables the
    # axiom-native (S_μ, S_ε) split with chirality bias; False restores the
    # pre-Phase-4 single-kernel symmetric form (legacy S1=D).
    use_asymmetric_saturation: bool = True
    # Phase 5.6 — memristive Op14 (doc 59_ §9-§10). Default False opt-in
    # preserves legacy instantaneous Op14. When True, K4 per-cell saturation
    # S(t) evolves via dS/dt = (S_eq − S)/τ_relax with backward Euler —
    # enables hysteresis, stabilizes sustained high-amplitude drive, and
    # makes cool-from-above experiments observe correct yield dynamics.
    use_memristive_saturation: bool = False
    # Path 1 / F17-H — Lagrangian-derived EMF coupling (doc 67_).
    # Default False preserves legacy Op14-only behavior. When True, the engine
    # ALSO adds an EMF source per port from δL_c/δV_sq via JAX autograd —
    # the missing reciprocal Cosserat→K4 channel. Op14 z_local stays
    # unchanged (axiom-correct per Vol 1 Ch 7:252) — ADDITIVE, not replacement.
    use_lagrangian_emf_coupling: bool = False
    # A28 correction (doc 67_ §15) — disable redundant ∂L_c/∂(u, ω) force on
    # Cosserat. Op14 z_local IS the K4↔Cosserat coupling channel; the
    # gradient force is double-counting. Default False preserves all
    # existing behavior (and runaway). Set True for the A28-corrected
    # coupling: empirically validates that Cosserat |ω| stays bounded
    # under mixed-mode small-amplitude drive (vs legacy 1700× growth in
    # one step). Test F17-I three-mode under True to validate (2,3)
    # eigenmode formation.
    disable_cosserat_lc_force: bool = False
    # Restore Cosserat self-terms (k_op10=1, k_refl=1, k_hopf=π/3) under
    # coupled-engine mode. Legacy disables these because "reflection is
    # carried by the coupling term"; under A28 (disable_cosserat_lc_force=True),
    # the coupling term is double-counting and Cosserat needs its self-terms
    # BACK for topology-stabilizing dynamics. Default False preserves legacy.
    enable_cosserat_self_terms: bool = False


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
        self.V_SNAP = config.V_SNAP_override if config.V_SNAP_override is not None else 1.0  # natural units by default

        # Core physics: delegate to CoupledK4Cosserat
        self._coupled = CoupledK4Cosserat(
            N=config.N,
            pml=config.pml,
            rho=config.rho,
            I_omega=config.I_omega,
            V_SNAP=self.V_SNAP,
            use_asymmetric_saturation=config.use_asymmetric_saturation,
            use_memristive_saturation=config.use_memristive_saturation,
            use_lagrangian_emf_coupling=config.use_lagrangian_emf_coupling,
            disable_cosserat_lc_force=config.disable_cosserat_lc_force,
            enable_cosserat_self_terms=config.enable_cosserat_self_terms,
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
    # State persistence (Phase 0.1, per round_10_plan.md)
    # -----------------------------------------------------------------
    # Save the engine's live state (K4 + Cosserat field arrays + time + config)
    # to a single .npz file. Sources + observers are NOT serialized — re-attach
    # after load. Use case: cache mid-run attractor states (e.g., Move 5 saturated
    # attractor at 15 P) to amortize pre-evolve + selection overhead across
    # multiple post-cache experiments.

    def save(self, path: str | Path) -> Path:
        """Save engine state to .npz. Returns the resolved path written.

        Captures:
          - K4: V_inc, V_ref, Phi_link, S_field
          - Cosserat: u, omega, u_dot, omega_dot
          - engine.time
          - EngineConfig dataclass (JSON-encoded inside the npz)

        Sources + observers are NOT serialized; re-attach after load.
        """
        path = Path(path)
        if not path.suffix:
            path = path.with_suffix(".npz")
        path.parent.mkdir(parents=True, exist_ok=True)
        config_json = json.dumps(asdict(self.config))
        np.savez_compressed(
            path,
            V_inc=self.k4.V_inc,
            V_ref=self.k4.V_ref,
            Phi_link=self.k4.Phi_link,
            S_field=self.k4.S_field,
            u=self.cos.u,
            omega=self.cos.omega,
            u_dot=self.cos.u_dot,
            omega_dot=self.cos.omega_dot,
            time=np.asarray(self.time),
            config_json=np.asarray(config_json),
        )
        return path

    @classmethod
    def load(cls, path: str | Path) -> "VacuumEngine3D":
        """Load engine state from .npz. Rebuilds engine via from_args(config),
        then overwrites live state arrays. Returns new engine matching the saved
        instance at engine.time. Sources + observers are NOT restored.
        """
        path = Path(path)
        if not path.suffix:
            path = path.with_suffix(".npz")
        data = np.load(path, allow_pickle=False)
        config_dict = json.loads(str(data["config_json"]))
        config = EngineConfig(**config_dict)
        engine = cls(config)
        engine.k4.V_inc[:] = data["V_inc"]
        engine.k4.V_ref[:] = data["V_ref"]
        engine.k4.Phi_link[:] = data["Phi_link"]
        engine.k4.S_field[:] = data["S_field"]
        engine.cos.u[:] = data["u"]
        engine.cos.omega[:] = data["omega"]
        engine.cos.u_dot[:] = data["u_dot"]
        engine.cos.omega_dot[:] = data["omega_dot"]
        # _coupled.time is the source of truth (step() does self.time = self._coupled.time
        # at the end of every step). Restoring engine.time alone leaves _coupled.time at 0;
        # the next step() then clobbers engine.time back to dt instead of saved_time + dt.
        t_saved = float(data["time"])
        engine._coupled.time = t_saved
        engine.time = t_saved
        return engine

    # -----------------------------------------------------------------
    # Thermal initialization (per doc 47_)
    # -----------------------------------------------------------------
    def initialize_thermal(self, T: float, seed: Optional[int] = None, thermalize_V: bool = False) -> None:
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
        sigma_omega = np.sqrt(T * mode_int / (4.0 * np.pi**2 * self.cos.I_omega))
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
