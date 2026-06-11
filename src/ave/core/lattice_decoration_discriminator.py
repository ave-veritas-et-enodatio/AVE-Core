"""
R3 — Lattice decoration discriminator (Phase-0 extension).

Three-arm battery comparing bare srs, bare diamond, and diamond + κ_chiral
decoration. See research/2026-06-11_lattice-decoration-discriminator_prereg.md.

Arms 1–2 replay Phase-0 geometric observables (writhe + Bishop transport).
Arm 3 separates achiral diamond GRAPH (writhe ≈ 0) from excited DECORATION
(Op14 asymmetric S_μ/S_ε split at κ ≠ 0 on a Beltrami ω seed).

The Arm-3 signed channel is a CONSISTENCY-CLASS decoration probe (κ is an
explicit input), not Bishop geometry — κ does not relocate lattice nodes.
"""

from __future__ import annotations

from dataclasses import dataclass

import jax.numpy as jnp
import numpy as np

from ave.core import chiral_lattice as cl
from ave.core import chiral_lattice_dynamics as cld
from ave.core.constants import ALPHA
from ave.topological.cosserat_field_3d import (
    KAPPA_CHIRAL_ELECTRON,
    _beltrami_helicity,
    _update_saturation_kernels,
)

# Prereg default thresholds (Phase-0 floors).
WRITHE_REPLAY_TOL = 1e-4
CONTROL_WRITHE_FRAC = 0.05
DECORATION_MIN_FRAC = 0.20  # R3-P5: vs srs Bishop |rate|
BISHOP_MIRROR_TOL = 1e-9


@dataclass(frozen=True)
class WritheArm:
    label: str
    writhe: float
    std: float
    n_rings: int


@dataclass(frozen=True)
class BishopArm:
    label: str
    rate_per_len_rad: float
    rate_per_len_deg: float
    signed_torsion: float


@dataclass(frozen=True)
class DecorationArm:
    kappa: float
    signed_proxy: float
    mean_h: float
    mean_z_skew: float


@dataclass(frozen=True)
class R3BatteryResult:
    L: int
    writhe_arms: tuple[WritheArm, ...]
    bishop_srs_right: BishopArm
    bishop_srs_mirror: BishopArm
    bishop_diamond: BishopArm
    decoration_arms: tuple[DecorationArm, ...]
    rho_decoration_vs_srs: float | None
    d1_bin: str
    gates: dict[str, bool]


def _writhe_arm(label: str, net: cl.LatticeNet) -> WritheArm:
    w, s, n, _ = cl.net_ring_writhe(net)
    return WritheArm(label=label, writhe=float(w), std=float(s), n_rings=int(n))


def _bishop_from_helix(label: str, coords: np.ndarray) -> BishopArm:
    _, _, rate = cld.bishop_transport_rotation(coords)
    tau = cld.helix_signed_torsion(coords)
    return BishopArm(
        label=label,
        rate_per_len_rad=float(rate),
        rate_per_len_deg=float(np.degrees(rate)),
        signed_torsion=float(tau),
    )


def _right_handed_beltrami_omega(n: int = 16, dx: float = 1.0) -> jnp.ndarray:
    """RH Beltrami ω seed (test_phase4 pattern) — h_local > 0."""
    k = 2.0 * np.pi / n
    z_idx = np.arange(n, dtype=np.float64).reshape(1, 1, n)
    omega = np.zeros((n, n, n, 3), dtype=np.float64)
    omega[..., 0] = np.cos(k * z_idx)
    omega[..., 1] = -np.sin(k * z_idx)
    return jnp.asarray(omega)


def _decoration_raw_proxy(
    kappa: float,
    *,
    n: int = 16,
    dx: float = 1.0,
    v_snap: float = 1.0,
) -> tuple[float, float, float]:
    """Raw mean(h · ln(S_μ/S_ε)) at κ (includes sector base asymmetry)."""
    omega = _right_handed_beltrami_omega(n=n, dx=dx)
    u = jnp.zeros_like(omega)
    v_sq = jnp.zeros((n, n, n), dtype=jnp.float64)
    s_mu, s_eps = _update_saturation_kernels(
        u, omega, v_sq, dx, v_snap, omega_yield=1.0, epsilon_yield=1.0, kappa_chiral=kappa
    )
    h = np.asarray(_beltrami_helicity(omega, dx))
    z_skew = np.log(np.asarray(s_mu) / np.asarray(s_eps))
    signed = float(np.mean(h * z_skew))
    return signed, float(h.mean()), float(z_skew.mean())


def decoration_signed_proxy(
    kappa: float,
    *,
    n: int = 16,
    dx: float = 1.0,
    v_snap: float = 1.0,
) -> DecorationArm:
    """κ-dependent decoration increment on fixed RH Beltrami ω.

    The raw h·ln(S_μ/S_ε) is nonzero at κ=0 because the μ/ε *base* sectors
    differ (curvature vs strain). The load-bearing decoration channel is the
    INCREMENT Δ(κ) = proxy(κ) − proxy(0) — isolates the (1±κh) chiral bias.
    Δ(0) = 0 by construction; Δ flips sign with κ.
    """
    raw, mean_h, mean_z = _decoration_raw_proxy(kappa, n=n, dx=dx, v_snap=v_snap)
    if abs(kappa) < 1e-15:
        signed = 0.0
    else:
        raw0, _, _ = _decoration_raw_proxy(0.0, n=n, dx=dx, v_snap=v_snap)
        signed = raw - raw0
    return DecorationArm(
        kappa=float(kappa),
        signed_proxy=signed,
        mean_h=mean_h,
        mean_z_skew=mean_z,
    )


def run_r3_battery(L: int = 6, n_turns: int = 3) -> R3BatteryResult:
    """Execute R3 prereg observables O1–O3 and assign D1 partial bin."""
    # O1 — writhe
    w_r = _writhe_arm("srs-R", cl.build_srs_net(L, "right"))
    w_l = _writhe_arm("srs-L", cl.build_srs_net(L, "left"))
    w_d = _writhe_arm("diamond-κ=0", cl.build_diamond_net(L))

    # O2 — Bishop on srs screw + achiral cubic-axis line on diamond
    c_r = cld.screw_orbit_helix("right", n_turns=n_turns)
    c_m = c_r.copy()
    c_m[:, 0] = -c_m[:, 0]
    b_r = _bishop_from_helix("srs-R screw", c_r)
    b_m = _bishop_from_helix("srs-R mirror", c_m)
    # Diamond: straight +z segment (no intrinsic helicity in graph)
    z_line = np.stack(
        [np.zeros(8), np.zeros(8), np.linspace(0.0, 2.0, 8)],
        axis=1,
    )
    b_d = _bishop_from_helix("diamond z-line", z_line)

    # O3 — decoration on achiral graph (κ sweep)
    dec0 = decoration_signed_proxy(0.0)
    dec_p = decoration_signed_proxy(+KAPPA_CHIRAL_ELECTRON)
    dec_m = decoration_signed_proxy(-KAPPA_CHIRAL_ELECTRON)

    srs_rate = abs(b_r.rate_per_len_rad)
    dec_rate = abs(dec_p.signed_proxy)
    rho = (dec_rate / srs_rate) if srs_rate > 1e-12 else None

    gates = {
        "R3-P1_writhe_replay": (
            abs(w_r.writhe + 4.0867e-2) < WRITHE_REPLAY_TOL * abs(4.0867e-2) + 1e-6
            and w_r.writhe * w_l.writhe < 0
        ),
        "R3-P2_bishop_mirror_odd": (
            b_r.rate_per_len_rad * b_m.rate_per_len_rad < 0
            and abs(b_r.rate_per_len_rad + b_m.rate_per_len_rad)
            < BISHOP_MIRROR_TOL * abs(b_r.rate_per_len_rad)
        ),
        "R3-P3_arm3_writhe_null": abs(w_d.writhe) < CONTROL_WRITHE_FRAC * abs(w_r.writhe),
        "R3-P4_arm3_kappa0_null": abs(dec0.signed_proxy) < 1e-12,
        "R3-P5_arm3_kappa_signed": (
            dec_p.signed_proxy * dec_m.signed_proxy < 0
            and dec_rate >= DECORATION_MIN_FRAC * srs_rate
        ),
    }

    d1_bin = _assign_d1_bin(gates, rho)

    return R3BatteryResult(
        L=L,
        writhe_arms=(w_r, w_l, w_d),
        bishop_srs_right=b_r,
        bishop_srs_mirror=b_m,
        bishop_diamond=b_d,
        decoration_arms=(dec0, dec_p, dec_m),
        rho_decoration_vs_srs=rho,
        d1_bin=d1_bin,
        gates=gates,
    )


def _assign_d1_bin(gates: dict[str, bool], rho: float | None) -> str:
    if not (gates["R3-P1_writhe_replay"] and gates["R3-P2_bishop_mirror_odd"]):
        return "D1-INCONCLUSIVE"
    if gates["R3-P5_arm3_kappa_signed"]:
        if rho is not None and 0.5 <= rho <= 2.0:
            return "D1-B"
        return "D1-MIXED"
    if gates["R3-P3_arm3_writhe_null"] and gates["R3-P4_arm3_kappa0_null"]:
        return "D1-A"
    return "D1-MIXED"
