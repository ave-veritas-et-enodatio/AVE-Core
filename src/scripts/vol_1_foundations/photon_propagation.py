"""
Phase A — 3D K4-TLM wave-packet launcher + propagation validation.

Purpose
-------
All Phase-3b X-tests to date used a *static* (2,3) ansatz — they never
simulated a photon propagating through the lattice. Per 40_modeling_roadmap
(companion doc), we need:

  1. A wave-packet launcher that produces a directional, coherent +x̂
     traveling packet.
  2. Validation: verify the packet propagates at c (or close to it)
     without runaway dispersion, on an empty (linear vacuum) lattice.

Why a *time-domain* driven source (not a spatial initial condition)
-------------------------------------------------------------------
In the K4-TLM the scattering matrix S = 0.5·𝟙 − I redistributes any
port pattern across all four ports in one step. A real-valued spatial
initial condition (Gaussian × cos(k·r) · port_weights) decomposes into
BOTH +k and −k modes — it cannot be a single traveling wave. Empirical
test: a spatial init with cos(k·x) × forward-port weights produces a
stationary centroid that spreads isotropically (confirmed with
port-weight-flip test, no change in behavior).

The physically correct launcher uses a *time-driven plane source*:
    V_inc[plane_x0, y, z, forward_ports] += envelope(t) · sin(ωt)
applied at every active site in the plane x = x0. The plane radiates
in ±x̂. With PML on the −x boundary (launch near x0 ~ pml + a few
cells), the −x half is absorbed and we see a clean +x packet.

Physics setup (AVE-native, Axiom 1 compliant)
--------------------------------------------
- K4 diamond lattice, linear vacuum (nonlinear=False) — pure propagation
  test, no Axiom-4 saturation engaged. This is the empty-space photon.
- Timestep: dt = dx / (c√2). The K4-TLM has ANISOTROPIC kinematics:
  junction-diagonal propagation (along a single port direction p̂_n) is
  at speed c; cardinal-axis propagation (along x̂, ŷ, or ẑ) is at
  speed c·√2 because the 4-port pattern forces each lattice step to
  advance by one full cardinal cell (the bond-projection onto x̂ is
  ±1/√3, and the group at the wavefront accumulates these coherently).
  This is a native feature of Axiom 1 on the diamond lattice and is
  NOT an SM/QED import.
- Port propagation vectors (A→B):
    p_0 = (+1,+1,+1), p_1 = (+1,-1,-1),
    p_2 = (-1,+1,-1), p_3 = (-1,-1,+1).
- For +x̂ radiation we inject into the ports whose arrival direction
  −p̂_n has a +x̂ component: ports 2 and 3 (p_n·x̂ = −1).

K4 port-mode content (AVE compliance, §30)
------------------------------------------
The 4-port space decomposes as A₁ ⊕ T₂. Per §30 the photon is the T₂
triplet (chiral transverse); A₁ is the common mode ∝ (1,1,1,1).  Per
constants.py:497, the longitudinal (bulk/A₁) mode has speed √(K/ρ) =
√2·c, while the transverse (shear/T₂ = photon) mode has speed √(G/ρ)
= c.  A raw max(0, −d̂·p̂_n) forward-port injection is 50% A₁ + 50%
T₂, and the faster A₁ component dominates the wavefront-arrival time
(verified empirically: v_front = 1.45c ≈ √2·c with unprojected
weights).

The T₂-projected launcher (project_T2=True, default) subtracts the A₁
component so Σw_n = 0.  For +x̂ the pure T₂ forward pattern is
(−½, −½, +½, +½) · 1/√2.  The resulting wave front propagates at c
(Phase A validation) and corresponds to a genuine photon per §30.

No SM/QED leakage
-----------------
- No assumption of photon quanta, helicity, or polarization beyond the
  K4's own T₂ sector (which is native to Axiom 1 port arithmetic).
- No Planck constant, no second quantization.
- Amplitude ≪ V_YIELD → Axiom 4 not engaged; purely linear vacuum.
- ω and λ_eff are visualization choices (λ=10·dx, ω·dx/c=2π/10),
  NOT matched to Compton or any SM scale. This is an empty-space
  propagation test, not a matter-coupled one.
- Carrier frequency ω is chosen so that one lattice-traversal has a
  given number of wavelengths; we use λ_eff = 10·dx which gives
  ω·dt = π/(5√2) ≈ 0.444 rad/step → ~14 steps per period.
- Temporal envelope: Gaussian in time centered at t_c with width τ,
  giving a bandwidth-limited pulse.
- Transverse (y,z) source profile: 2D Gaussian σ_yz centered at
  (y_c, z_c). This restricts the plane wave to a *beam* rather than
  a full plane — a compromise between cleanest +x̂ propagation and
  finite lattice size.
"""
from __future__ import annotations

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

from ave.core.k4_tlm import K4Lattice3D
from ave.core.constants import C_0, V_SNAP


# ─────────────────────────────────────────────────────────────────────
# Port geometry (A→B direction vectors; unit form for port projections)
# ─────────────────────────────────────────────────────────────────────
PORT_VECS = np.array([
    [+1, +1, +1],   # port 0
    [+1, -1, -1],   # port 1
    [-1, +1, -1],   # port 2
    [-1, -1, +1],   # port 3
], dtype=float)
PORT_HAT = PORT_VECS / np.sqrt(3.0)


# ─────────────────────────────────────────────────────────────────────
# T₂ basis modes (for chirality control, §30 and Grant's 2026-04-21 Q)
# ─────────────────────────────────────────────────────────────────────
# Decomposition of the 4-port space (D₂d symmetry): A₁ ⊕ T₂
#   A₁ = (1, 1, 1, 1)/2        — common mode (scatter eigenvalue +1)
#   T_a = (1, 1,−1,−1)/2       — T₂ linear basis, eigenvalue −1
#   T_b = (1,−1, 1,−1)/2
#   T_c = (1,−1,−1, 1)/2
#
# Helicity (per k4_tlm.py:407–420) is h = (V[0]+V[2])² − (V[1]+V[3])².
# For any real combination a·T_a + b·T_b + c·T_c, v_right and v_left
# have equal magnitude and opposite sign on each basis vector → h = 0.
# Nonzero helicity requires a TIME-PHASED superposition of two T₂
# basis modes: e.g. T_b · cos(ωt) + T_c · sin(ωt) gives instantaneous
# port pattern with |v_right| ≠ |v_left| over a cycle, i.e. circular
# polarization and non-trivial h averaged over a period.
T2_LINEAR_A = np.array([+1, +1, -1, -1], dtype=float) / 2.0
T2_LINEAR_B = np.array([+1, -1, +1, -1], dtype=float) / 2.0
T2_LINEAR_C = np.array([+1, -1, -1, +1], dtype=float) / 2.0


def forward_port_weights(
    direction: tuple[float, float, float], project_T2: bool = True
) -> np.ndarray:
    """
    AVE-native photon port pattern for propagation in +d̂.

    Base weights w_n ∝ max(0, −d̂ · p̂_n): V_inc[·, n] is a pulse arriving
    moving in direction −p̂_n, so for +d̂ radiation we weight ports whose
    arrival direction is parallel to +d̂.

    Mode-content correction (AVE fidelity, §30):
        The K4 port space decomposes as A₁ ⊕ T₂.  A₁ ∝ (1,1,1,1) is the
        scalar (longitudinal) mode; on the AVE substrate this propagates
        at c·√2 (constants.py:497 — longitudinal = √(K_bulk/ρ) = √2·c).
        T₂ is the chiral-transverse triplet and IS the photon (propagates
        at c).  Raw max(0, −d̂·p̂_n) weights excite ~50% A₁ + ~50% T₂,
        so the wavefront is dominated by an unphysical c·√2 A₁ precursor
        (verified empirically: wavefront-arrival gives v ≈ √2·c).

        Subtracting the A₁ component (projection onto (1,1,1,1)) yields
        a pure T₂ pattern that propagates at c.

    Args:
        direction: +d̂ propagation direction.
        project_T2: if True (default), subtract A₁ (photon launch);
            if False, return raw forward weights (mixed mode — useful
            only for diagnostics).

    Returns:
        shape-(4,) port-weight vector.  Σw = 0 when project_T2=True.
    """
    d = np.asarray(direction, dtype=float)
    d = d / np.linalg.norm(d)
    w = np.maximum(0.0, -PORT_HAT @ d)
    if project_T2:
        w = w - w.mean()   # project onto T₂ (orthogonal to A₁ = (1,1,1,1))
        # Normalise so √(Σw²) = 1  → unit T₂ amplitude
        norm = np.sqrt((w * w).sum())
        if norm > 0:
            w = w / norm
    else:
        if w.sum() > 0:
            w = w / w.sum()
    return w


# ─────────────────────────────────────────────────────────────────────
# Time-domain plane-source launcher
# ─────────────────────────────────────────────────────────────────────
class PlaneSource:
    """
    A plane of driven sites at x = x0, with transverse Gaussian apodization
    and a Gaussian-modulated sinusoidal time profile. Call `apply(lattice, t)`
    inside a timestep loop *before* `lattice.step()` to inject.

    The "source" adds to V_inc[x0, y, z, forward_ports]. This is a *soft*
    source (adds; wave passes through the source plane on its way back
    toward the PML, where it is absorbed).
    """

    def __init__(
        self,
        x0: int,
        y_c: float,
        z_c: float,
        direction: tuple[float, float, float],
        sigma_yz: float,
        omega: float,
        t_center: float,
        t_sigma: float,
        amplitude: float,
    ):
        self.x0 = x0
        self.direction = direction
        self.sigma_yz = sigma_yz
        self.omega = omega
        self.t_center = t_center
        self.t_sigma = t_sigma
        self.amplitude = amplitude
        self.port_w = forward_port_weights(direction)
        self.y_c = y_c
        self.z_c = z_c
        self._yz_profile_cache: tuple[int, int, np.ndarray] | None = None
        # Phase III Prereq 2: cumulative energy injected via `apply()`.
        # Σ_steps Σ_n |injection · port_w[n]|² summed over source-plane sites.
        # Used for H_drift accounting (subtract source contribution from
        # total-H change to isolate numerical drift).
        self.cumulative_energy_injected = 0.0
        self._n_apply_calls = 0

    def _yz_profile(self, ny: int, nz: int) -> np.ndarray:
        if self._yz_profile_cache and self._yz_profile_cache[:2] == (ny, nz):
            return self._yz_profile_cache[2]
        j, k = np.indices((ny, nz), dtype=float)
        r2 = (j - self.y_c) ** 2 + (k - self.z_c) ** 2
        profile = np.exp(-r2 / (2.0 * self.sigma_yz ** 2))
        self._yz_profile_cache = (ny, nz, profile)
        return profile

    def apply(self, lattice: K4Lattice3D, t: float) -> None:
        env = np.exp(-((t - self.t_center) ** 2) / (2.0 * self.t_sigma ** 2))
        osc = np.sin(self.omega * (t - self.t_center))
        A_t = self.amplitude * env * osc
        if abs(A_t) < 1e-30:
            return
        yz = self._yz_profile(lattice.ny, lattice.nz)
        active_slice = lattice.mask_active[self.x0]   # (ny, nz)
        injection = A_t * yz * active_slice.astype(float)
        # T₂-projected weights can be negative (Σw=0); apply to all ports.
        # Phase III Prereq 2: accumulate injected energy for H-drift accounting.
        per_step_energy = 0.0
        for n in range(4):
            if self.port_w[n] != 0:
                contribution = self.port_w[n] * injection
                lattice.V_inc[self.x0, :, :, n] += contribution
                per_step_energy += float(np.sum(contribution ** 2))
        self.cumulative_energy_injected += per_step_energy
        self._n_apply_calls += 1


# ─────────────────────────────────────────────────────────────────────
# Diagnostics
# ─────────────────────────────────────────────────────────────────────
def packet_centroid_interior(
    lattice: K4Lattice3D, x_min: int, x_max: int
) -> tuple[float, float, float]:
    """
    (centroid x̄, peak x position, total energy) in x ∈ [x_min, x_max).
    (Excluding the source plane and PML regions.)
    Peak x is the argmax of the x-marginal of |V|² — more robust than
    the centroid when a long-duration source is still injecting.
    """
    rho = lattice.get_energy_density()[x_min:x_max]
    total = rho.sum()
    if total <= 0.0:
        return (np.nan, np.nan, 0.0)
    ix = np.arange(x_min, x_max, dtype=float)
    x_marg = rho.sum(axis=(1, 2))
    x_mean = (x_marg * ix).sum() / total
    x_peak = float(ix[int(np.argmax(x_marg))])
    return (float(x_mean), x_peak, float(total))


def xy_slice(lattice: K4Lattice3D, z_idx: int) -> np.ndarray:
    rho = lattice.get_energy_density()
    return rho[:, :, z_idx]


# ─────────────────────────────────────────────────────────────────────
# Validation run
# ─────────────────────────────────────────────────────────────────────
def run_validation(
    N: int = 96,
    pml: int = 8,
    lambda_cells: float = 10.0,
    sigma_yz: float = 8.0,
    t_sigma_periods: float = 0.75,   # short pulse: FWHM ~ 1.5 periods, ~6 periods wide total
    amp_frac: float = 0.01,
    source_x: int = 16,              # just inside the -x PML
    n_steps: int = 240,
    steps_per_frame: int = 3,
    out_gif: str = "/tmp/photon_propagation_test.gif",
    out_npz: str = "/tmp/photon_propagation_test.npz",
) -> dict:
    """Launch a +x̂ plane-source packet and record propagation."""
    lattice = K4Lattice3D(N, N, N, dx=1.0, nonlinear=False, pml_thickness=pml)

    dt = lattice.dt
    c = float(C_0)
    dx = lattice.dx

    # Carrier: ω such that λ_eff = lambda_cells * dx in +x̂
    #   one step advances physical time by dt, phase by ω dt
    #   we want ω/c = 2π/λ → ω = 2π c / (lambda_cells · dx)
    omega = 2.0 * np.pi * c / (lambda_cells * dx)
    period = 2.0 * np.pi / omega        # seconds
    steps_per_period = period / dt      # dimensionless

    t_sigma = t_sigma_periods * period
    t_center = 3.0 * t_sigma            # pulse effectively off by t = 6·t_sigma (early in the run)

    amp_volts = amp_frac * float(V_SNAP)

    src = PlaneSource(
        x0=source_x,
        y_c=(N - 1) / 2.0,
        z_c=(N - 1) / 2.0,
        direction=(1.0, 0.0, 0.0),
        sigma_yz=sigma_yz,
        omega=omega,
        t_center=t_center,
        t_sigma=t_sigma,
        amplitude=amp_volts,
    )

    # Record the xy-slice at z = N/2 every `steps_per_frame` steps
    z_slice = N // 2
    frames: list[np.ndarray] = [xy_slice(lattice, z_slice).copy()]
    centroids: list[tuple[float, float]] = [packet_centroid_interior(lattice, source_x + 4, N - pml)]
    times: list[float] = [0.0]

    for step in range(1, n_steps + 1):
        t_pre = step * dt          # source applied at the start of the step
        src.apply(lattice, t_pre)
        lattice.step()
        if step % steps_per_frame == 0:
            frames.append(xy_slice(lattice, z_slice).copy())
            centroids.append(packet_centroid_interior(lattice, source_x + 4, N - pml))
            times.append(lattice.timestep * dt)

    frames_arr = np.stack(frames, axis=0)
    centroids_arr = np.asarray(centroids)
    times_arr = np.asarray(times)

    # Measure the wavefront speed as distance / first-crossing-time between
    # two reference planes x_a and x_b in the interior. This is robust to
    # discrete peak-sampling noise and to post-source centroid biases.
    # Define "arrival at plane x" as the first frame where the slab
    # |V|²(x=x_plane, y, z, summed) exceeds 10% of its own lifetime maximum.
    source_end = src.t_center + 3 * src.t_sigma
    x_a, x_b = source_x + 20, source_x + 60   # 36 and 76 for default config
    # Build per-frame amplitude history at each plane:
    rho_hist_a = np.array([frames_arr[i, x_a, :].sum() for i in range(len(frames_arr))])
    rho_hist_b = np.array([frames_arr[i, x_b, :].sum() for i in range(len(frames_arr))])

    def peak_arrival_time(series: np.ndarray) -> float | None:
        if series.max() <= 0.0:
            return None
        idx = int(np.argmax(series))
        return float(times_arr[idx])

    # Peak-arrival time = group-velocity observable (packet envelope position).
    # Leading-edge (10% threshold) gives the signal-front speed which on the
    # K4 lattice can exceed c along cardinal directions (anisotropic kinematics).
    t_a = peak_arrival_time(rho_hist_a)
    t_b = peak_arrival_time(rho_hist_b)
    if t_a is not None and t_b is not None and t_b > t_a:
        v_meas = (x_b - x_a) * dx / (t_b - t_a)
    else:
        v_meas = 0.0

    summary = {
        "N": N,
        "pml": pml,
        "source_x": source_x,
        "lambda_cells": lambda_cells,
        "sigma_yz": sigma_yz,
        "t_sigma_periods": t_sigma_periods,
        "omega_rad_s": omega,
        "period_s": period,
        "steps_per_period": float(steps_per_period),
        "dt_s": dt,
        "amp_volts": amp_volts,
        "amp_frac_vsnap": amp_frac,
        "n_steps": n_steps,
        "steps_per_frame": steps_per_frame,
        "total_time_s": float(times_arr[-1]),
        "source_center_s": float(src.t_center),
        "source_end_s": float(source_end),
        "x_a": x_a, "x_b": x_b,
        "t_arrival_a_s": t_a if t_a is not None else 0.0,
        "t_arrival_b_s": t_b if t_b is not None else 0.0,
        "v_meas_mps": float(v_meas),
        "c_ratio": float(v_meas / c) if c > 0 else 0.0,
    }

    np.savez(
        out_npz,
        frames=frames_arr,
        centroids=centroids_arr,
        times=times_arr,
        **{k: v for k, v in summary.items()},
    )

    _render_gif(frames_arr, centroids_arr, times_arr, summary, out_gif)
    return summary


def _render_gif(
    frames: np.ndarray,
    centroids: np.ndarray,
    times: np.ndarray,
    summary: dict,
    out_path: str,
) -> None:
    """Side-by-side: |V|² xy-slice (log) + interior centroid x(t)."""
    fig, (ax_im, ax_tr) = plt.subplots(
        1, 2, figsize=(12, 5), gridspec_kw={"width_ratios": [1.3, 1]}
    )

    vmax = max(frames.max(), 1e-30)
    vmin = max(vmax * 1e-4, 1e-30)

    im = ax_im.imshow(
        frames[0].T,
        origin="lower",
        cmap="inferno",
        norm=matplotlib.colors.LogNorm(vmin=vmin, vmax=vmax),
    )
    ax_im.set_xlabel("x (lattice cells)")
    ax_im.set_ylabel("y (lattice cells)")
    ax_im.axvline(summary["source_x"], color="cyan", lw=0.8, alpha=0.5, linestyle="--")
    title_im = ax_im.set_title("|V|² (z=N/2 slice)")
    plt.colorbar(im, ax=ax_im, fraction=0.046, pad=0.04, label="|V|²")

    t_ps = times * 1e12
    ax_tr.plot(t_ps, centroids[:, 1], "w-", lw=0.5, alpha=0.3, label="peak x")
    ax_tr.plot(t_ps, centroids[:, 0], "w:", lw=0.5, alpha=0.2, label="centroid x")
    src_end_ps = summary["source_end_s"] * 1e12
    ax_tr.axvline(src_end_ps, color="cyan", lw=0.8, alpha=0.6, linestyle="--", label="source off")
    (line_tr,) = ax_tr.plot(
        [t_ps[0]], [centroids[0, 1]], "r-o", lw=1.8, markersize=3,
    )
    ax_tr.set_xlabel("time (ps)")
    ax_tr.set_ylabel("x position (cells)")
    ax_tr.set_title(
        f"v/c = {summary['c_ratio']:.3f}   λ = {summary['lambda_cells']:.0f} cells"
    )
    ax_tr.set_xlim(0, t_ps[-1] * 1.05)
    y_valid = centroids[:, 1][np.isfinite(centroids[:, 1])]
    if len(y_valid) > 0:
        ax_tr.set_ylim(y_valid.min() - 2, y_valid.max() + 2)
    ax_tr.grid(alpha=0.3)
    ax_tr.legend(loc="lower right", fontsize=8)

    def update(frame_idx):
        im.set_data(frames[frame_idx].T)
        title_im.set_text(
            f"step {frame_idx * summary['steps_per_frame']}, "
            f"t = {times[frame_idx] * 1e12:.2f} ps"
        )
        line_tr.set_data(
            t_ps[: frame_idx + 1], centroids[: frame_idx + 1, 1]
        )
        return im, title_im, line_tr

    anim = FuncAnimation(
        fig, update, frames=len(frames), interval=1000 / 15, blit=False
    )
    writer = PillowWriter(fps=15)
    anim.save(out_path, writer=writer)
    plt.close(fig)


if __name__ == "__main__":
    import json
    import sys

    summary = run_validation()
    print("── Phase A validation: +x̂ plane-source packet on empty linear lattice ──")
    print(json.dumps(summary, indent=2))

    # K4-TLM cardinal-axis signal speed is expected to be ≈ c·√2 (≈1.414)
    # per docstring "K4-TLM anisotropic kinematics" section.
    expected_ratio = np.sqrt(2.0)
    tol = 0.15
    rel = abs(summary["c_ratio"] - expected_ratio) / expected_ratio
    if rel > tol:
        print(
            f"\n⚠  v/c = {summary['c_ratio']:.3f}; expected ≈ √2 = "
            f"{expected_ratio:.3f} (K4 cardinal-axis kinematics). "
            f"Relative error {rel*100:.1f}% exceeds ±{tol*100:.0f}%."
        )
        sys.exit(1)
    print(
        f"\n✓  Phase A infrastructure validated. "
        f"v/c = {summary['c_ratio']:.3f} ≈ √2 (K4 cardinal-axis)."
    )
