"""
Option-D V→ω Beltrami source from trapped V energy (Phase C′ Increment B′).

Implements tracereversal §5 **step 3** (Beltrami BC pinned to trapped V),
distinct from steps 1–2 (relu(−Γ) confinement clamp).

Gate: shared saturation front ``g_wall(A_combined)`` × seed window × trapped
``V_sq``. Amplitude: ``κ̃ · max(R, √(e_V)) · g`` with ``R=Γ²`` (Op17 bound).
Direction: CP Beltrami template from scalar seed geometry (bootstrap at ω=0).

Prereg: research/2026-06-13_loop-gap-scalar-grade-restoration_prereg_FROZEN.md §2 Increment B
"""

from __future__ import annotations

import numpy as np

from ave.core.cross_sector_coupling import KAPPA_TILDE
from ave.topological.k4_cosserat_coupling import CoupledK4Cosserat

_TETRA = np.array(
    [
        (+1, +1, +1),
        (+1, -1, -1),
        (-1, +1, -1),
        (-1, -1, +1),
    ],
    dtype=float,
)


def _v_plane_from_k4(V_inc: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Recover in-plane (Vx, Vy) from tetra port voltages."""
    vx = np.einsum("...p,p->...", V_inc, _TETRA[:, 0]) / 3.0
    vy = np.einsum("...p,p->...", V_inc, _TETRA[:, 1]) / 3.0
    return vx, vy


def beltrami_unit_from_v_plane(vx: np.ndarray, vy: np.ndarray) -> np.ndarray:
    """Right-handed CP Beltrami direction (−Vy, Vx, 0) from in-plane V seed."""
    ox = -vy
    oy = vx
    oz = np.zeros_like(vx)
    mag = np.sqrt(ox**2 + oy**2 + oz**2)
    floor = np.maximum(mag, 1e-30)
    return np.stack([ox / floor, oy / floor, oz / floor], axis=-1)


def store_beltrami_template_from_v_plane(
    coupled: CoupledK4Cosserat,
    vx: np.ndarray,
    vy: np.ndarray,
) -> None:
    """Cache unit Beltrami helm from genesis-24 CP (Vx, Vy) geometry."""
    coupled._beltrami_unit = beltrami_unit_from_v_plane(vx, vy)


def beltrami_unit_field(coupled: CoupledK4Cosserat) -> np.ndarray:
    """Unit Beltrami template — cached at seed or reconstructed from live V_inc."""
    cached = getattr(coupled, "_beltrami_unit", None)
    if cached is not None:
        return np.asarray(cached, dtype=float)
    vx, vy = _v_plane_from_k4(coupled.k4.V_inc)
    return beltrami_unit_from_v_plane(vx, vy)


def trapped_v_energy_density(coupled: CoupledK4Cosserat) -> np.ndarray:
    """Dimensionless trapped LC energy — live V_sq plus finite seed reservoir."""
    v_sq = np.sum(coupled.k4.V_inc**2, axis=-1)
    v_snap = float(coupled.k4.V_SNAP)
    live = np.clip(v_sq / (v_snap**2), 0.0, 1.0)
    window = getattr(
        coupled,
        "_scalar_seed_window",
        np.ones(live.shape, dtype=float),
    )
    reservoir = float(getattr(coupled, "_scalar_trapped_e_v", 0.0))
    if reservoir <= 0.0:
        return live
    return np.clip(np.maximum(live, reservoir * window), 0.0, 1.0)


def front_transfer_strength(coupled: CoupledK4Cosserat) -> np.ndarray:
    """Trapped-V-led gate × Op17 bound (B′ — not relu(−Γ))."""
    g_wall = coupled._converter_wall_window(live=True)
    window = getattr(
        coupled,
        "_scalar_seed_window",
        np.ones((coupled.N, coupled.N, coupled.N)),
    )
    e_v = trapped_v_energy_density(coupled)
    gamma = coupled._impedance_gamma_shared()
    r_op17 = np.clip(gamma**2, 0.0, 1.0)
    # Bootstrap from trapped reservoir when μ-short Γ not yet engaged.
    r_eff = np.maximum(r_op17, np.minimum(np.sqrt(e_v), 1.0))
    interior = np.asarray(coupled._interior_mask(), dtype=float)
    return g_wall * window * e_v * r_eff * interior


def boundary_v_to_omega_accel(coupled: CoupledK4Cosserat) -> np.ndarray:
    """Beltrami ω source from trapped V at the shared saturation front (§5 step 3)."""
    if not getattr(coupled, "v_to_omega_source_on", False):
        return np.zeros_like(coupled.cos.omega)

    strength = front_transfer_strength(coupled)
    if float(np.max(strength)) < 1e-30:
        return np.zeros_like(coupled.cos.omega)

    kappa = float(getattr(coupled, "converter_kappa_tilde", KAPPA_TILDE))
    beltrami = beltrami_unit_field(coupled)
    amp = kappa * strength
    return amp[..., None] * beltrami


def relative_h_drift(coupled: CoupledK4Cosserat, h0: float, h1: float) -> float:
    """Relative Hamiltonian drift for conservative-window falsifier F2."""
    denom = max(abs(h0), 1e-30)
    return abs(h1 - h0) / denom
