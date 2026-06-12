"""
Rarefaction bulk-density sector (GAP-A) — shared by UnifiedGenesisEngine port + VacuumEngine3D.

EOS (candidate-claim, Propulsion-derived):
    c_bulk²(ρ̄) = c₀² (1 + ρ̄/(1 − ρ̄²))

Prereg: research/2026-06-12_loop-gap-harness-bulk-channel_prereg_DRAFT.md
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

PHI = (1.0 + np.sqrt(5.0)) / 2.0
# Engine lattice natural units: c0 = 1 per scatter step (not SI C_0).
ENGINE_C0 = 1.0
RHO_CAV = -1.0 / PHI


def c_bulk2_raw(rho: np.ndarray, *, c0: float, eps_den: float) -> np.ndarray:
    denom = 1.0 - rho**2
    denom = np.where(
        np.abs(denom) < eps_den,
        np.sign(denom) * eps_den + eps_den,
        denom,
    )
    return (c0**2) * (1.0 + rho / denom)


def c_bulk2_clipped(
    rho: np.ndarray,
    *,
    c0: float,
    c2_floor: float,
    eps_den: float,
) -> np.ndarray:
    return np.maximum(c_bulk2_raw(rho, c0=c0, eps_den=eps_den), c2_floor * c0**2)


def bulk_pressure(rho: np.ndarray, *, c0: float, eps_den: float) -> np.ndarray:
    arg = np.maximum(1.0 - rho**2, eps_den)
    return (c0**2) * (rho - 0.5 * np.log(arg))


def _d(f: np.ndarray, axis: int, dx: float) -> np.ndarray:
    return (np.roll(f, -1, axis=axis) - np.roll(f, 1, axis=axis)) / (2.0 * dx)


def _laplacian(f: np.ndarray, dx: float) -> np.ndarray:
    return (
        np.roll(f, 1, 0)
        + np.roll(f, -1, 0)
        + np.roll(f, 1, 1)
        + np.roll(f, -1, 1)
        + np.roll(f, 1, 2)
        + np.roll(f, -1, 2)
        - 6.0 * f
    ) / (dx**2)


def _div3(mx: np.ndarray, my: np.ndarray, mz: np.ndarray, dx: float) -> np.ndarray:
    return _d(mx, 0, dx) + _d(my, 1, dx) + _d(mz, 2, dx)


def build_pml_damping(N: int, pml: int, *, rate: float = 0.12) -> np.ndarray:
    """Per-step multiplicative absorber in the PML shell (CP7)."""
    if pml <= 0:
        return np.ones((N, N, N), dtype=np.float64)
    i, j, k = np.indices((N, N, N))
    d = np.minimum.reduce([i, N - 1 - i, j, N - 1 - j, k, N - 1 - k])
    damp = np.ones((N, N, N), dtype=np.float64)
    in_pml = d < pml
    damp[in_pml] = 1.0 - rate * ((pml - d[in_pml]) / float(pml)) ** 2
    return damp


def interior_mask(N: int, pml: int) -> np.ndarray:
    m = np.ones((N, N, N), dtype=bool)
    if pml > 0:
        m[:pml, :, :] = False
        m[-pml:, :, :] = False
        m[:, :pml, :] = False
        m[:, -pml:, :] = False
        m[:, :, :pml] = False
        m[:, :, -pml:] = False
    return m


@dataclass
class BulkRarefactionConfig:
    c0: float = ENGINE_C0
    c2_floor: float = 1e-3
    rho_floor: float = -0.95
    eps_den: float = 1e-6
    nu_art_bulk: float = 5e-4
    rho_diff: float = 5e-4
    pml_rate: float = 0.12


class BulkRarefactionSector:
    """3D barotropic bulk-density flow (port of UnifiedGenesisEngine GAP-A)."""

    def __init__(self, N: int, dx: float, pml: int, cfg: BulkRarefactionConfig | None = None):
        self.N = int(N)
        self.dx = float(dx)
        self.pml = int(pml)
        self.cfg = cfg or BulkRarefactionConfig()
        self.rho_bar = np.zeros((N, N, N), dtype=np.float64)
        self.u_adv = np.zeros((N, N, N, 3), dtype=np.float64)
        self._damping = build_pml_damping(N, pml, rate=self.cfg.pml_rate)
        self._interior = interior_mask(N, pml)
        self.clip_rho_hits = 0
        self.clip_c2_hits = 0
        self.step_count = 0

    def clear(self) -> None:
        self.rho_bar[:] = 0.0
        self.u_adv[:] = 0.0

    def apply_probe_ic(self, *, amp: float = 0.08, sigma_frac: float = 0.18) -> None:
        """Localized rarefaction dip — sector-live probe only (Increment A, not GAP-C)."""
        if amp <= 0.0:
            self.clear()
            return
        N = self.N
        sigma = max(2.0, sigma_frac * N)
        cc = (N - 1) / 2.0
        i, j, k = np.indices((N, N, N))
        r2 = (i - cc) ** 2 + (j - cc) ** 2 + (k - cc) ** 2
        env = np.exp(-r2 / (2.0 * sigma**2))
        self.rho_bar[:] = -float(amp) * env
        self.u_adv[:] = 0.0

    def energize_rotation_column(
        self,
        *,
        m_edge: float,
        r_core: float,
        axis: int = 2,
        taper_frac: float = 0.15,
    ) -> float:
        """Solid-body rotation column (GAP-D / OP-3 motor seed).

        Port of ``UnifiedGenesisEngine.energize_rotation_column``: circulation
        is set once; ``ρ̄`` starts at zero and rarefaction emerges via continuity
        (CP9 — not an algebraic centrifugal paint).
        """
        c0 = self.cfg.c0
        r_core = max(float(r_core), self.dx)
        omega = float(m_edge) * c0 / r_core
        cc = (self.N - 1) / 2.0
        i, j, k = np.indices((self.N, self.N, self.N))
        if axis == 2:
            a1 = (i - cc) * self.dx
            a2 = (j - cc) * self.dx
        elif axis == 1:
            a1 = (i - cc) * self.dx
            a2 = (k - cc) * self.dx
        else:
            a1 = (j - cc) * self.dx
            a2 = (k - cc) * self.dx
        rc = np.sqrt(a1**2 + a2**2)
        taper = taper_frac * self.N * self.dx
        ramp = (rc - r_core) / max(taper, 1e-12)
        env = np.where(
            rc <= r_core,
            1.0,
            np.clip(0.5 * (1.0 + np.cos(np.pi * np.clip(ramp, 0.0, 1.0))), 0.0, 1.0),
        )
        env = np.where(rc > r_core + taper, 0.0, env)
        self.u_adv[:] = 0.0
        if axis == 2:
            self.u_adv[..., 0] = -omega * a2 * env
            self.u_adv[..., 1] = omega * a1 * env
        elif axis == 1:
            self.u_adv[..., 0] = -omega * a2 * env
            self.u_adv[..., 2] = omega * a1 * env
        else:
            self.u_adv[..., 1] = -omega * a2 * env
            self.u_adv[..., 2] = omega * a1 * env
        self.rho_bar[:] = 0.0
        return omega

    def _rhs(self, rho: np.ndarray, u: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        cfg = self.cfg
        dx = self.dx
        ux, uy, uz = u[..., 0], u[..., 1], u[..., 2]
        one_p = 1.0 + rho
        div_m = _div3(one_p * ux, one_p * uy, one_p * uz, dx)
        drho_dt = -div_m + cfg.rho_diff * _laplacian(rho, dx)
        c2 = c_bulk2_clipped(rho, c0=cfg.c0, c2_floor=cfg.c2_floor, eps_den=cfg.eps_den)
        pref = c2 / np.maximum(one_p, cfg.eps_den)
        drx = _d(rho, 0, dx)
        dry = _d(rho, 1, dx)
        drz = _d(rho, 2, dx)
        du = np.empty_like(u)
        for comp, (dudc, drc) in enumerate(
            ((u[..., 0], drx), (u[..., 1], dry), (u[..., 2], drz))
        ):
            adv = (
                ux * _d(dudc, 0, dx)
                + uy * _d(dudc, 1, dx)
                + uz * _d(dudc, 2, dx)
            )
            du[..., comp] = (
                -adv - pref * drc + cfg.nu_art_bulk * _laplacian(dudc, dx)
            )
        return drho_dt, du

    def _cfl_dt_sub(self, dt: float) -> float:
        """Sub-timestep for explicit RK2 (matches cavitation_flow envelope)."""
        c_max = 3.0 * self.cfg.c0
        dt_cfl = 0.25 * self.dx / (c_max * np.sqrt(3.0))
        return min(dt, max(dt_cfl, 1e-12))

    def _step_once(self, dt: float) -> None:
        k1r, k1u = self._rhs(self.rho_bar, self.u_adv)
        rm = self.rho_bar + 0.5 * dt * k1r
        um = self.u_adv + 0.5 * dt * k1u
        k2r, k2u = self._rhs(rm, um)
        self.rho_bar = self.rho_bar + dt * k2r
        self.u_adv = self.u_adv + dt * k2u
        self.rho_bar *= self._damping
        self.u_adv *= self._damping[..., None]
        m = self._interior
        below = (self.rho_bar < self.cfg.rho_floor) & m
        self.clip_rho_hits += int(np.count_nonzero(below))
        np.maximum(self.rho_bar, self.cfg.rho_floor, out=self.rho_bar)
        c2raw = c_bulk2_raw(self.rho_bar, c0=self.cfg.c0, eps_den=self.cfg.eps_den)
        self.clip_c2_hits += int(
            np.count_nonzero((c2raw < self.cfg.c2_floor * self.cfg.c0**2) & m)
        )

    def step(self, dt: float) -> None:
        remaining = float(dt)
        n_sub = 0
        max_sub = max(64, int(np.ceil(dt / max(self._cfl_dt_sub(dt), 1e-12))) + 8)
        while remaining > 0.0:
            dt_sub = min(self._cfl_dt_sub(remaining), remaining)
            if dt_sub <= 0.0:
                break
            self._step_once(dt_sub)
            remaining -= dt_sub
            n_sub += 1
            if n_sub > max_sub:
                raise RuntimeError(
                    f"BulkRarefactionSector CFL substep cap exceeded ({max_sub}); "
                    f"check c0 uses engine natural units (1.0), not SI C_0"
                )
        self.step_count += 1

    def snapshot(self) -> dict[str, float]:
        m = self._interior
        rho_int = self.rho_bar[m]
        finite = np.isfinite(rho_int)
        c2 = c_bulk2_clipped(
            self.rho_bar,
            c0=self.cfg.c0,
            c2_floor=self.cfg.c2_floor,
            eps_den=self.cfg.eps_den,
        )
        c2_int = c2[m & np.isfinite(c2)]
        rho_fin = rho_int[finite] if finite.any() else rho_int
        return {
            "rho_bar_min": float(np.min(rho_fin)) if rho_fin.size else 0.0,
            "rho_bar_max": float(np.max(rho_fin)) if rho_fin.size else 0.0,
            "c_bulk2_min": float(np.min(c2_int)) if c2_int.size else self.cfg.c0**2,
            "c_bulk2_max": float(np.max(c2_int)) if c2_int.size else self.cfg.c0**2,
            "max_abs_u_adv": float(np.max(np.abs(self.u_adv[m]))) if m.any() else 0.0,
            "bulk_steps": float(self.step_count),
        }
