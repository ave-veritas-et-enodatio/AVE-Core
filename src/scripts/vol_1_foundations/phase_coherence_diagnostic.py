"""F17-K Phase 2/5 — phase-coherence diagnostic for the K4-TLM coupled engine.

**REBUILT 2026-04-25 after Phase 5b fallacy audit:** the previous version
measured per-node reactive-energy temporal variance, which doesn't
distinguish "Ax-3 phase-coherent eigenmode" from "monotonically draining
dissipative trajectory." Both have low temporal variance over short
windows. New diagnostic tests the actual Ax-3 conditions explicitly.

Per [doc 68_](../../../research/L3_electron_soliton/68_phase_quadrature_methodology.md)
the AVE-native (Axiom-3 / Effective Action Principle / Least Reflected
Action) eigenmode condition is impedance-matching reactive cycling. To
distinguish reactive cycling from dissipation, this diagnostic measures
five distinct AVE-native observables:

(1) **Total energy conservation** — E_total = E_cos + E_k4 should be
    conserved for an Ax-3 eigenmode. Reports std/mean over a sliding
    window. Low ⟹ conserved (eigenmode candidate); high or
    monotonically drifting ⟹ dissipative or unstable.

(2) **Inter-sector LC-coupling** — for a coupled K4↔Cosserat eigenmode,
    the two sectors exchange energy at the LC frequency. E_k4 and E_cos
    should oscillate in anti-phase. Reports Pearson correlation of
    detrended (E_k4, E_cos) over the window. Negative correlation
    ⟹ LC coupling firing; ~0 or positive ⟹ no exchange.

(3) **Phasor angular velocity** — at sampled lattice sites with
    nontrivial amplitude, the per-port phasor angle
    θ_p(x, t) = arctan2(V_ref, V_inc) should advance at constant rate
    (≈ ω_C). Reports mean and std of dθ/dt across sample sites.
    Constant rate ⟹ steady oscillation; high std ⟹ chaotic or
    not-yet-converged.

(4) **Phase-space winding (major-axis equatorial contour)** — sample
    per-port phasor angle on the (R_target, z=center) circle, count
    winding. Expected winding for (2,3) electron eigenmode along
    major-axis: **2** (the toroidal winding), not 3 (which is the
    poloidal/minor-axis winding).

(5) **Phase-space winding (minor-axis poloidal contour)** — sample
    per-port phasor angle on the (φ=0, ψ varies) poloidal circle of
    radius r_target around the soliton tube. Expected winding for the
    poloidal direction: **3**.

Per-port aggregation is necessary because chirality-weighted seeds have
χ_p that sums to zero across tetrahedral ports (sum-port aggregation
zeros out under chirality=1.0). All winding extractions therefore
operate on a single chosen port (defaulting to port 0).
"""
from __future__ import annotations

import sys
import time
from collections import deque

import numpy as np

sys.path.insert(0, "/Users/grantlindblom/AVE-staging/AVE-Core/src/scripts/vol_1_foundations")

from ave.topological.vacuum_engine import VacuumEngine3D


PHI = (1.0 + np.sqrt(5.0)) / 2.0
PHI_SQ = PHI ** 2


def compute_total_k4_energy(engine: VacuumEngine3D) -> float:
    """E_k4 = Σ (V_inc² + V_ref²) over all active K4 sites and ports."""
    V_inc = np.asarray(engine.k4.V_inc)
    V_ref = np.asarray(engine.k4.V_ref)
    return float(np.sum(V_inc ** 2 + V_ref ** 2))


def compute_total_cos_energy(engine: VacuumEngine3D) -> float:
    return float(engine.cos.total_energy())


def compute_phasor_angle_at_port(
    engine: VacuumEngine3D, port: int = 0
) -> np.ndarray:
    """Per-site phasor angle from one port: θ(x) = arctan2(V_ref[p], V_inc[p]).

    Returns angle in radians, shape (nx, ny, nz). Per-port avoids the
    chirality-induced cancellation in sum-port aggregation when the
    seeder uses chirality≠0 (where Σ_p χ_p ≈ 0 zeros out sum_port).
    """
    V_inc = np.asarray(engine.k4.V_inc[..., port])
    V_ref = np.asarray(engine.k4.V_ref[..., port])
    return np.arctan2(V_ref, V_inc)


def compute_winding_along_circle(
    engine: VacuumEngine3D,
    cx: float, cy: float, cz: float,
    radius: float,
    plane: str,
    port: int = 0,
    n_samples: int = 128,
) -> int:
    """Winding number of per-port phasor angle along a parametric circle.

    plane ∈ {"xy", "xz", "yz"} — selects the 2D slice plane.
    Returns the integer winding (Σ Δθ / 2π over the closed loop).
    """
    nx, ny, nz = engine.k4.nx, engine.k4.ny, engine.k4.nz
    phis = np.linspace(0.0, 2.0 * np.pi, n_samples, endpoint=False)

    if plane == "xy":
        xs = cx + radius * np.cos(phis)
        ys = cy + radius * np.sin(phis)
        zs = np.full_like(xs, cz)
    elif plane == "xz":
        xs = cx + radius * np.cos(phis)
        ys = np.full_like(xs, cy)
        zs = cz + radius * np.sin(phis)
    elif plane == "yz":
        xs = np.full_like(phis, cx)
        ys = cy + radius * np.cos(phis)
        zs = cz + radius * np.sin(phis)
    else:
        raise ValueError(f"unknown plane {plane!r}")

    ix = np.clip(xs.astype(int), 0, nx - 1)
    iy = np.clip(ys.astype(int), 0, ny - 1)
    iz = np.clip(zs.astype(int), 0, nz - 1)

    phasor_field = compute_phasor_angle_at_port(engine, port=port)
    angles = phasor_field[ix, iy, iz]
    diffs = np.diff(np.unwrap(angles))
    return int(np.round(np.sum(diffs) / (2.0 * np.pi)))


def major_axis_winding(
    engine: VacuumEngine3D, R_major: float, port: int = 0
) -> int:
    """Toroidal winding (around major axis): φ varies, ψ=0.

    Expected winding for (2,3) electron eigenmode: **2**.
    Contour is xy-plane circle at z=center, radius R_major.
    """
    nx, ny, nz = engine.k4.nx, engine.k4.ny, engine.k4.nz
    cx = (nx - 1) / 2.0
    cy = (ny - 1) / 2.0
    cz = (nz - 1) / 2.0
    return compute_winding_along_circle(
        engine, cx, cy, cz, radius=R_major, plane="xy", port=port,
    )


def minor_axis_winding(
    engine: VacuumEngine3D, R_major: float, r_minor: float, port: int = 0
) -> int:
    """Poloidal winding (around minor axis): ψ varies, φ=0.

    Expected winding for (2,3) electron eigenmode: **3**.
    Contour is xz-plane circle at (x=R_major, y=center, z=center),
    radius r_minor — the poloidal circle around the tube at φ=0.
    """
    nx, ny, nz = engine.k4.nx, engine.k4.ny, engine.k4.nz
    cy = (ny - 1) / 2.0
    cz = (nz - 1) / 2.0
    # Center the contour at (R_major, 0) in xz plane (φ=0)
    cx_contour = (nx - 1) / 2.0 + R_major
    return compute_winding_along_circle(
        engine, cx_contour, cy, cz, radius=r_minor, plane="xz", port=port,
    )


def compute_phasor_angular_velocity(
    phasor_t0: np.ndarray, phasor_t1: np.ndarray, mask: np.ndarray
) -> dict:
    """Per-site dθ/dt from two consecutive phasor-angle snapshots.

    Returns mean, std, and per-site values on the masked region.
    Handles 2π wraparound via shortest-arc differencing.
    """
    diff = phasor_t1 - phasor_t0
    diff = (diff + np.pi) % (2.0 * np.pi) - np.pi  # shortest-arc
    masked = diff[mask] if mask is not None and mask.any() else diff.ravel()
    if masked.size == 0:
        return {"mean": float("nan"), "std": float("nan"), "n": 0}
    return {
        "mean": float(np.mean(masked)),
        "std": float(np.std(masked)),
        "n": int(masked.size),
    }


def shell_mask(
    engine: VacuumEngine3D, R_target: float, r_target: float, dr: float = 1.5
) -> np.ndarray:
    """Boolean mask of lattice cells within the soliton shell tube."""
    nx, ny, nz = engine.k4.nx, engine.k4.ny, engine.k4.nz
    cx = (nx - 1) / 2.0
    cy = (ny - 1) / 2.0
    cz = (nz - 1) / 2.0
    ii, jj, kk = np.meshgrid(np.arange(nx), np.arange(ny), np.arange(nz), indexing="ij")
    rho = np.sqrt((ii - cx) ** 2 + (jj - cy) ** 2)
    z_off = kk - cz
    rho_tube = np.sqrt((rho - R_target) ** 2 + z_off ** 2)
    return (rho_tube >= max(r_target - dr, 0.0)) & (rho_tube <= r_target + dr)


class PhaseCoherenceDiagnostic:
    """Rolling Ax-3 diagnostic over engine trajectory.

    Maintains buffers of E_cos(t), E_k4(t), and phasor-angle snapshots
    over a sliding window of `window_size` samples. Surfaces:
      - E_total conservation: std/|mean| of (E_cos + E_k4)
      - LC coupling: Pearson correlation of detrended E_cos vs E_k4
      - Angular velocity: mean & std of phasor dθ/dt on shell
      - Major-axis winding (toroidal, expected 2)
      - Minor-axis winding (poloidal, expected 3)
    """

    def __init__(
        self,
        engine: VacuumEngine3D,
        R_target: float,
        r_target: float,
        window_size: int = 8,
        port_for_winding: int = 0,
    ) -> None:
        self.engine = engine
        self.R_target = float(R_target)
        self.r_target = float(r_target)
        self.window_size = int(window_size)
        self.port = int(port_for_winding)
        self.shell = shell_mask(engine, R_target, r_target)
        self._E_cos_history: deque = deque(maxlen=self.window_size)
        self._E_k4_history: deque = deque(maxlen=self.window_size)
        self._phasor_history: deque = deque(maxlen=2)

    def update(self) -> None:
        self._E_cos_history.append(compute_total_cos_energy(self.engine))
        self._E_k4_history.append(compute_total_k4_energy(self.engine))
        self._phasor_history.append(compute_phasor_angle_at_port(self.engine, self.port))

    def current(self) -> dict:
        out = {
            "E_cos": self._E_cos_history[-1] if self._E_cos_history else float("nan"),
            "E_k4": self._E_k4_history[-1] if self._E_k4_history else float("nan"),
        }
        out["E_total"] = out["E_cos"] + out["E_k4"]
        # E_total conservation: std/|mean| over window
        if len(self._E_cos_history) >= 3:
            E_cos_arr = np.array(self._E_cos_history)
            E_k4_arr = np.array(self._E_k4_history)
            E_total_arr = E_cos_arr + E_k4_arr
            mean_E = float(np.mean(E_total_arr))
            std_E = float(np.std(E_total_arr))
            out["E_total_cov"] = std_E / max(abs(mean_E), 1e-30)
            # LC coupling: Pearson correlation of detrended series
            cos_d = E_cos_arr - np.mean(E_cos_arr)
            k4_d = E_k4_arr - np.mean(E_k4_arr)
            denom = np.std(cos_d) * np.std(k4_d)
            out["E_correlation"] = (
                float(np.mean(cos_d * k4_d) / denom) if denom > 1e-30 else 0.0
            )
        else:
            out["E_total_cov"] = float("nan")
            out["E_correlation"] = float("nan")
        # Angular velocity from last two phasor snapshots on shell
        if len(self._phasor_history) >= 2:
            av = compute_phasor_angular_velocity(
                self._phasor_history[0], self._phasor_history[1], self.shell
            )
            out["dtheta_dt_mean"] = av["mean"]
            out["dtheta_dt_std"] = av["std"]
        else:
            out["dtheta_dt_mean"] = float("nan")
            out["dtheta_dt_std"] = float("nan")
        # Phase-space winding along major and minor axis
        out["winding_major"] = major_axis_winding(self.engine, self.R_target, port=self.port)
        out["winding_minor"] = minor_axis_winding(
            self.engine, self.R_target, self.r_target, port=self.port
        )
        return out


def run_diagnostic_on_seed(
    seed_callable,
    label: str,
    N: int = 80,
    n_steps: int = 30,
    R: float = 20.0,
    port_for_winding: int = 0,
) -> None:
    """Generic driver: build engine + invoke seed_callable(engine) +
    run n_steps with per-step diagnostic output."""
    r = R / PHI_SQ
    print("=" * 78)
    print(f"  F17-K Phase 5b/2 (rebuilt diagnostic): {label}  N={N}  n_steps={n_steps}")
    print("=" * 78)
    print(f"  R={R}, r={r:.4f}, port_for_winding={port_for_winding}")
    print(f"  Engine: A28+self-terms")
    print()

    engine = VacuumEngine3D.from_args(
        N=N, pml=4, temperature=0.0,
        disable_cosserat_lc_force=True,
        enable_cosserat_self_terms=True,
    )
    seed_callable(engine, R, r)

    diag = PhaseCoherenceDiagnostic(engine, R_target=R, r_target=r, window_size=8,
                                    port_for_winding=port_for_winding)
    diag.update()

    print(f"  {'step':<5}{'c_cos':<6}{'w_maj':<7}{'w_min':<7}"
          f"{'E_cos':<11}{'E_k4':<11}{'E_tot_cov':<11}"
          f"{'corr':<8}{'dθ/dt mean':<12}{'dθ/dt std':<10}")

    t0 = time.time()
    for step in range(0, n_steps + 1):
        if step > 0:
            engine.step()
            diag.update()
        c_cos = int(engine.cos.extract_crossing_count())
        d = diag.current()
        cov = d["E_total_cov"]
        corr = d["E_correlation"]
        dt_m = d["dtheta_dt_mean"]
        dt_s = d["dtheta_dt_std"]
        cov_str = f"{cov:.4f}" if np.isfinite(cov) else "  nan "
        corr_str = f"{corr:+.3f}" if np.isfinite(corr) else " nan "
        dtm_str = f"{dt_m:+.4f}" if np.isfinite(dt_m) else "  nan "
        dts_str = f"{dt_s:.4f}" if np.isfinite(dt_s) else " nan "

        print(f"  {step:<5}{c_cos:<6}{d['winding_major']:<7}{d['winding_minor']:<7}"
              f"{d['E_cos']:<11.3e}{d['E_k4']:<11.3e}{cov_str:<11}"
              f"{corr_str:<8}{dtm_str:<12}{dts_str:<10}")

    elapsed = time.time() - t0
    print(f"\n  elapsed: {elapsed:.1f}s for {n_steps} steps")


def _path_b_seed(engine: VacuumEngine3D, R: float, r: float) -> None:
    cos_amp_scale = 0.3 / (np.sqrt(3.0) / 2.0)
    engine.cos.initialize_electron_2_3_sector(
        R_target=R, r_target=r, use_hedgehog=True, amplitude_scale=cos_amp_scale,
    )


if __name__ == "__main__":
    # Default: Path B for baseline (K4 dormant — should show E_k4=0, no LC, no winding).
    run_diagnostic_on_seed(_path_b_seed, label="Path B (Cosserat ω only — control)")
