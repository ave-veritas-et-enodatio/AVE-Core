"""
Scalar-grade Lane-1 standing V seed on K4 V_inc (Phase C′ Increment A).

Ports genesis-24 ``_seed_v_partner`` / ``UnifiedGenesisEngine.seed_lane1`` shape
to the LOOP GAP harness. Topology-NULL precursor — no planted (2,3).

Prereg: research/2026-06-13_loop-gap-scalar-grade-restoration_prereg_FROZEN.md §2 Increment A
"""

from __future__ import annotations

from typing import Literal

import numpy as np

from ave.core.constants import ALPHA
from ave.core.loop_gap_seeds import A_YIELD
from ave.topological.cosserat_field_3d import TETRA_OFFSETS, _beltrami_helicity
from ave.topological.k4_cosserat_coupling import CoupledK4Cosserat
from ave.topological.vacuum_engine import VacuumEngine3D

ScalarSeedMode = Literal["lane1_standing"]

_TETRA = np.array(TETRA_OFFSETS, dtype=float)
SCALAR_SIGMA_FRAC = 4.0 / 24.0
SCALAR_LAM_FRAC = 6.0 / 24.0
A2_V_FLOOR_FRAC = 0.25  # F1: A²_V > 0.25·A_yield²
# In-plane (Vx,Vy) → tetra ports divides by 3 per port; |V_inc|² = 4/9·|V_vec|² at peak.
K4_INPLANE_A2_SCALE = 4.0 / 9.0


def _interior_active(coupled: CoupledK4Cosserat) -> np.ndarray:
    return np.asarray(coupled._interior_mask(), dtype=bool) & np.asarray(
        coupled.k4.mask_active, dtype=bool
    )


def _gaussian_window(
    N: int,
    center: tuple[float, float, float],
    sigma: float,
) -> np.ndarray:
    cx, cy, cz = center
    x = (np.arange(N)[:, None, None] - cx).astype(float)
    y = (np.arange(N)[None, :, None] - cy).astype(float)
    z = (np.arange(N)[None, None, :] - cz).astype(float)
    return np.exp(-(x**2 + y**2 + z**2) / (2.0 * sigma**2))


def seed_lane1_standing_v(
    engine: VacuumEngine3D,
    *,
    frac: float = 0.85,
    sigma: float | None = None,
    center: tuple[float, float, float] | None = None,
    mode: ScalarSeedMode = "lane1_standing",
    clear_k4: bool = False,
) -> None:
    """Standing longitudinal V on K4 V_inc — CP8 precursor-only (no (2,3) knot).

    Circularly-polarized in-plane V-vector structure (genesis-24) so the tetra
    port basis carries a transverse winding component the extractor can read.
    """
    if mode != "lane1_standing":
        raise ValueError(f"unknown scalar seed mode {mode!r}")

    coupled = engine._coupled
    k4 = coupled.k4
    N = coupled.N
    if center is None:
        center = (N / 2.0, N / 2.0, N / 2.0)
    if sigma is None:
        sigma = max(2.0, SCALAR_SIGMA_FRAC * N)

    if clear_k4:
        k4.V_inc[:] = 0.0
        k4.V_ref[:] = 0.0
        k4.Phi_link[:] = 0.0

    v_snap = float(k4.V_SNAP)
    amp = float(frac) * v_snap
    lam = max(4.0, SCALAR_LAM_FRAC * N)
    cx, cy, cz = center

    x = (np.arange(N)[:, None, None] - cx).astype(float)
    y = (np.arange(N)[None, :, None] - cy).astype(float)
    z = (np.arange(N)[None, None, :] - cz).astype(float)
    env = np.exp(-(x**2 + y**2 + z**2) / (2.0 * sigma**2))
    phase = 2.0 * np.pi * x / lam
    vx = amp * env * np.cos(phase)
    vy = amp * env * np.sin(phase)

    from ave.core.scalar_grade_source import store_beltrami_template_from_v_plane

    store_beltrami_template_from_v_plane(coupled, vx, vy)

    mask = np.asarray(k4.mask_active, dtype=float)
    for port in range(4):
        k4.V_inc[..., port] += (vx * _TETRA[port, 0] + vy * _TETRA[port, 1]) / 3.0 * mask
    k4.V_inc *= mask[..., None]
    active = _interior_active(coupled)
    a2_planted = a2_v_field(k4)
    coupled._scalar_seed_a2_peak = (
        float(np.max(a2_planted[active])) if active.any() else 0.0
    )
    k4._scatter_all()

    coupled._scalar_seed_frac = float(frac)
    coupled._scalar_seed_window = _gaussian_window(N, center, sigma)
    coupled._scalar_seed_mode = mode
    coupled._scalar_trapped_e_v = float(np.max(a2_planted[active])) if active.any() else 0.0


def a2_v_field(k4) -> np.ndarray:
    """Per-site A²_V = |V_inc|² / V_SNAP²."""
    v_sq = np.sum(k4.V_inc**2, axis=-1)
    v_snap = float(k4.V_SNAP)
    return v_sq / (v_snap**2)


def scalar_seed_certificate(
    engine: VacuumEngine3D,
    *,
    frac: float | None = None,
) -> dict:
    """CP8 precursor-only certificate for the K4 scalar seed at t=0.

    topology_null: |H_bel|≈0, ω≡0 (no planted (2,3)).
    standing: Cosserat velocities zero at seed (energize-once, not pumped).
    """
    coupled = engine._coupled
    k4 = coupled.k4
    cos = coupled.cos
    m = _interior_active(coupled)
    frac_val = float(
        frac if frac is not None else getattr(coupled, "_scalar_seed_frac", 0.85)
    )
    window = getattr(
        coupled,
        "_scalar_seed_window",
        np.ones(k4.V_inc.shape[:3], dtype=float),
    )

    a2 = a2_v_field(k4)
    denom = float(np.sum(window * m)) + 1e-30
    a2_seed = float(np.sum(a2 * window * m) / denom) if m.any() else 0.0
    a2_peak_live = float(np.max(a2[m])) if m.any() else 0.0
    a2_peak = float(getattr(coupled, "_scalar_seed_a2_peak", a2_peak_live))
    frac2_k4 = K4_INPLANE_A2_SCALE * float(frac_val**2)

    omega_max = float(np.max(np.linalg.norm(cos.omega, axis=-1)))
    u_dot_max = float(np.max(np.abs(cos.u_dot)))
    omega_dot_max = float(np.max(np.abs(cos.omega_dot)))
    if omega_max > 1e-12:
        h_field = np.asarray(_beltrami_helicity(cos.omega, float(cos.dx)))
        h_bel = float(np.abs(h_field[m]).max()) if m.any() else 0.0
    else:
        h_bel = 0.0

    topology_null = (h_bel < 1e-12) and (omega_max < 1e-12)
    d_vdt_max = 0.0  # static V_inc IC before first step
    a2_floor = A2_V_FLOOR_FRAC * float(A_YIELD**2)
    passes_f1 = (
        topology_null
        and a2_peak > a2_floor
        and abs(a2_peak - frac2_k4) < 0.05 * max(frac2_k4, 1e-12)
        and u_dot_max < 1e-12
        and omega_dot_max < 1e-12
    )

    return {
        "A2_seed": a2_seed,
        "A2_peak": a2_peak,
        "A2_peak_live": a2_peak_live,
        "frac2": float(frac_val**2),
        "frac2_k4": frac2_k4,
        "A2_floor": a2_floor,
        "H_bel_abs": h_bel,
        "omega_max": omega_max,
        "dVdt_max": d_vdt_max,
        "topology_null": bool(topology_null),
        "passes": bool(passes_f1),
        "scalar_seed_mode": getattr(coupled, "_scalar_seed_mode", "lane1_standing"),
    }


def apply_scalar_seed_if_enabled(
    engine: VacuumEngine3D,
    *,
    scalar_seed_on: bool,
    scalar_seed_frac: float = 0.85,
    scalar_seed_mode: ScalarSeedMode = "lane1_standing",
) -> bool:
    """KEEP-BOTH hook: False ⇒ no-op."""
    if not scalar_seed_on:
        return False
    seed_lane1_standing_v(
        engine,
        frac=scalar_seed_frac,
        mode=scalar_seed_mode,
    )
    return True
