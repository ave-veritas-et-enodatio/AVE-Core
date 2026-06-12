"""
LOOP GAP seed protocols — generative precursors on VacuumEngine3D.

Maps entrainment §4 stratification → ∇A₀ approach to asymmetric yield surface.
No external Source injectors (genesis-24 pump falsified).

DAG: _orchestration/2026-06-12_loop-gap-engine-dag.md Phase 2
"""

from __future__ import annotations

from typing import Literal

import numpy as np

from ave.core.constants import ALPHA, N_PHI_PACK, R_II
from ave.core.cross_sector_coupling import scale_cosserat_to_front
from ave.core.genesis_v18_coupled import pair_seed_cosserat
from ave.topological.k4_cosserat_coupling import CoupledK4Cosserat, _cosserat_A_squared
from ave.topological.vacuum_engine import VacuumEngine3D

SeedMode = Literal["pair", "photon_lock", "graded_a0"]

# genesis-23 energize-lock defaults (reflection_genesis_23_self_assembly.py).
A_LOCK_DEFAULT = 3.0
PHOTON_SIGMA_FRAC = 3.0 / 24.0  # scale σ with N
PHOTON_LAM_FRAC = 6.0 / 24.0

# Membrane LLCP buffered yield analogue: A_yield_buffered = 1 + φ_packing (Vol 5).
A_YIELD_BUFFERED = 1.0 + float(N_PHI_PACK)


def _clear_k4_ports(coupled: CoupledK4Cosserat) -> None:
    coupled.k4.V_inc[:] = 0.0
    coupled.k4.V_ref[:] = 0.0
    coupled.k4.Phi_link[:] = 0.0


def seed_photon_lock(
    engine: VacuumEngine3D,
    *,
    a_lock: float = A_LOCK_DEFAULT,
    helicity: float = 1.0,
) -> None:
    """Transverse ω-photon precursor at soft-moderate wall engagement (CP8)."""
    coupled = engine._coupled
    N = coupled.N
    _clear_k4_ports(coupled)
    coupled.cos.u[:] = 0.0
    coupled.cos.u_dot[:] = 0.0
    coupled.cos.omega[:] = 0.0
    coupled.cos.omega_dot[:] = 0.0

    sigma = max(2.0, PHOTON_SIGMA_FRAC * N)
    lam = max(4.0, PHOTON_LAM_FRAC * N)
    center = (N / 2.0, N / 2.0, N / 2.0)
    coupled.cos.initialize_gaussian_wavepacket_omega(
        center,
        sigma=sigma,
        direction=(1.0, 0.0, 0.0),
        wavelength=lam,
        amplitude=float(a_lock),
        axis=2,
        helicity=helicity,
    )


def seed_graded_a0(
    engine: VacuumEngine3D,
    *,
    amp: float | None = None,
    axis: int = 2,
    ramp_strength: float = 0.85,
) -> None:
    """Pair seed with ∇A₀ ramp — sub-yield periphery → buffered-yield core (Mapping C).

    Creates spatial impedance gradient via amplitude modulation, not node density.
    """
    if amp is None:
        amp = float(np.sqrt(ALPHA))
    coupled = engine._coupled
    N = coupled.N
    pair_seed_cosserat(coupled, amp=amp)

    x = np.arange(N, dtype=float)[:, None, None]
    y = np.arange(N, dtype=float)[None, :, None]
    z = np.arange(N, dtype=float)[None, None, :]
    axis_field = (x, y, z)[axis]
    center = N // 2
    span = max(N / 4.0, 1.0)
    z_ax = axis_field
    z_norm = (z_ax - center) / span
    # tanh ramp: approach yield from −z (sub-yield) toward +z (buffered band).
    ramp = 1.0 + float(ramp_strength) * np.tanh(z_norm)
    ramp = np.clip(ramp, 0.35, A_YIELD_BUFFERED)

    coupled.cos.u *= ramp[..., None]
    coupled.cos.omega *= ramp[..., None]

    A_cos_sq = _cosserat_A_squared(
        coupled.cos.u,
        coupled.cos.omega,
        coupled.cos.dx,
        coupled.cos.omega_yield,
        coupled.cos.epsilon_yield,
    )
    coupled.cos.u, coupled.cos.omega = scale_cosserat_to_front(
        coupled.cos.u, coupled.cos.omega, A_cos_sq, target=R_II
    )
    coupled.cos.u_dot[:] = 0.0
    coupled.cos.omega_dot[:] = 0.0


def apply_seed(
    engine: VacuumEngine3D,
    mode: SeedMode,
    *,
    amp: float | None = None,
    a_lock: float = A_LOCK_DEFAULT,
) -> None:
    """Apply conservative IC; caller must freeze_converter_wall() after."""
    if mode == "pair":
        amp_val = float(np.sqrt(ALPHA)) if amp is None else float(amp)
        if amp_val <= 0.0:
            _clear_k4_ports(engine._coupled)
            engine._coupled.cos.u[:] = 0.0
            engine._coupled.cos.omega[:] = 0.0
            engine._coupled.cos.u_dot[:] = 0.0
            engine._coupled.cos.omega_dot[:] = 0.0
            return
        pair_seed_cosserat(engine._coupled, amp=amp_val)
    elif mode == "photon_lock":
        seed_photon_lock(engine, a_lock=a_lock)
    elif mode == "graded_a0":
        seed_graded_a0(engine, amp=amp)
    else:
        raise ValueError(f"unknown seed mode {mode!r}")
