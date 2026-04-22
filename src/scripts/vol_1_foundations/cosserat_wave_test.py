"""
Phase I validation — time-domain Cosserat wave propagation.

Tests the new `step()` method (velocity-Verlet) added to CosseratField3D:

  T1a — GAPLESS rotational wave.  G_c = 0, γ = 1, use_saturation = False,
        k_op10 = k_refl = k_hopf = 0.  The Lagrangian reduces to
            L = ½·I_ω·|ω̇|² − ½·γ·|∇ω|²
        giving wave equation  ∂_t² ω = (γ/I_ω)·∇² ω.  Expected group
        velocity  c_R = √(γ/I_ω) = 1  (natural units).

  T1b — GAPPED rotational wave.  Same as T1a but G_c = 1 (full micropolar
        coupling).  The micropolar term W_micropolar = Σᵢⱼ (ε_antisym,ij)²
        evaluates to 2·|ω|² for uniform ω_z (both ε_xy = −ω_z and
        ε_yx = +ω_z contribute equally), so the effective mass term is
        2·G_c·|ω|². The dispersion gaps to
            ω² = c²·k² + m²   with  m² = 4·G_c/I_ω.
        (derived empirically 2026-04-22; the naive "|ε|² = |ω|²" estimate
        giving m² = 2G_c/I_ω is off by 2).
        Group velocity drops to v_g = c²·k / √(c²·k² + m²).

  T2  — Uniform-ω oscillation (mass-gap confirmation).  Seed a uniform
        ω_z(r) = A₀ and run with G_c = 1 (all other terms off).  Field
        oscillates at frequency ω_m = √(4·G_c/I_ω) = 2.  Measured
        period should be 2π/2 = π ≈ 3.14 time units.

  T3  — Hamiltonian conservation.  Velocity-Verlet should give O(dt²)
        energy drift; on T1 we expect |ΔH/H|_max ≲ 1 % over many steps.

AVE FINDING (Phase I, for S4 adjudication):
  The Cosserat rotational sector natively carries MASSIVE excitations
  because of the micropolar coupling term G_c·|ε_antisym|² = G_c·|ω|².
  This is PHYSICALLY appropriate — the electron IS massive, and its
  mass emerges from the Lagrangian gap m² = 2·G_c/I_ω.  The K4 photon
  sector (scalar V_inc) is separately MASSLESS, as required by §30.
  The coupled simulator will therefore have a massless photon sector
  AND a massive rotational sector co-evolving.  This answers S4 in
  the affirmative: the Cosserat rho/I_omega parameters set the MASS
  SCALE of the rotational sector, not the propagation speed.

All runs use `use_saturation=False` (Axiom 4 off — linear regime).
"""
from __future__ import annotations

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from ave.topological.cosserat_field_3d import CosseratField3D


# ─────────────────────────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────────────────────────
def _linear_solver(N: int, G_c: float, gamma: float, rho: float = 1.0, I_omega: float = 1.0) -> CosseratField3D:
    """Linear-only Cosserat: Cauchy + (optional) micropolar + curvature.
    Op10, Hopf, reflection, and saturation all off."""
    s = CosseratField3D(nx=N, ny=N, nz=N, dx=1.0, use_saturation=False,
                        rho=rho, I_omega=I_omega)
    s.G = 1.0
    s.G_c = G_c
    s.gamma = gamma
    s.k_op10 = 0.0
    s.k_refl = 0.0
    s.k_hopf = 0.0
    return s


def _packet_centroid_axis(field: np.ndarray, mask: np.ndarray, axis_component: int) -> float:
    """Centroid along x-axis, weighted by field[...,axis_component]²."""
    rho = (field[..., axis_component] ** 2) * mask
    total = rho.sum()
    if total <= 0:
        return float("nan")
    ix = np.arange(field.shape[0], dtype=float)[:, None, None]
    return float((rho * ix).sum() / total)


# ─────────────────────────────────────────────────────────────────
# T1 — propagation tests
# ─────────────────────────────────────────────────────────────────
def test_wave_speed(
    N: int, G_c: float, gamma: float,
    wavelength: float = 12.0, sigma: float = 3.0,
    n_steps: int = 200, record_every: int = 5,
) -> dict:
    s = _linear_solver(N=N, G_c=G_c, gamma=gamma)
    x0 = N // 4
    s.initialize_gaussian_wavepacket_omega(
        center=(x0, N // 2, N // 2), sigma=sigma, direction=(1.0, 0.0, 0.0),
        wavelength=wavelength, amplitude=1e-3, axis=2,
    )

    mask = s.mask_alive
    times, cents, Ts, Vs, Hs = [], [], [], [], []
    for step in range(n_steps + 1):
        if step > 0:
            s.step()
        if step % record_every == 0:
            times.append(s.time)
            cents.append(_packet_centroid_axis(s.omega, mask, axis_component=2))
            Ts.append(s.kinetic_energy())
            Vs.append(s.total_energy())
            Hs.append(Ts[-1] + Vs[-1])

    times_a = np.asarray(times)
    cents_a = np.asarray(cents)
    Hs_a = np.asarray(Hs)

    fit_mask = np.isfinite(cents_a) & (cents_a > x0 + 0.5) & (cents_a < N - sigma * 2)
    if fit_mask.sum() >= 4:
        v_meas = np.polyfit(times_a[fit_mask], cents_a[fit_mask], 1)[0]
    else:
        v_meas = float("nan")

    c_R_theory = np.sqrt(gamma / s.I_omega)
    # Gapped dispersion: ω² = c²k² + m² with m² = 2·G_c/I_ω (natural units here)
    k_wave = 2.0 * np.pi / wavelength
    m_sq = 4.0 * G_c / s.I_omega
    v_g_theory = (c_R_theory ** 2 * k_wave) / np.sqrt(c_R_theory ** 2 * k_wave ** 2 + m_sq)
    H_drift = float(np.abs(Hs_a / max(Hs_a[0], 1e-30) - 1).max())

    return {
        "G_c": G_c, "gamma": gamma,
        "wavelength": wavelength, "sigma": sigma,
        "N": N, "n_steps": n_steps,
        "cfl_dt": s.cfl_dt,
        "c_R_theory_continuum": float(c_R_theory),
        "v_g_theory_gapped": float(v_g_theory),
        "v_measured": float(v_meas),
        "v_over_c_R": float(v_meas / c_R_theory) if np.isfinite(v_meas) else float("nan"),
        "v_over_v_g_theory": float(v_meas / v_g_theory) if np.isfinite(v_meas) and v_g_theory > 0 else float("nan"),
        "H_drift_max": H_drift,
        "times": times_a,
        "centroids": cents_a,
        "H_history": Hs_a,
        "T_history": np.asarray(Ts),
        "V_history": np.asarray(Vs),
    }


# ─────────────────────────────────────────────────────────────────
# T2 — uniform-ω mass-gap oscillation
# ─────────────────────────────────────────────────────────────────
def test_mass_gap_oscillation(N: int = 32, G_c: float = 1.0, n_steps: int = 150) -> dict:
    """Uniform ω_z(r) = A₀. ∂²_t ω_z = -(2·G_c/I_ω)·ω_z → period 2π/√(2G_c/I_ω)."""
    s = _linear_solver(N=N, G_c=G_c, gamma=1.0)
    # Note: the gamma term contributes nothing here (uniform ω has ∇ω = 0)
    A0 = 0.05
    omega_init = np.zeros_like(s.omega)
    omega_init[..., 2] = A0
    omega_init *= s.mask_alive[..., None]
    s.omega = omega_init
    s.u = np.zeros_like(s.u)
    s.u_dot = np.zeros_like(s.u_dot)
    s.omega_dot = np.zeros_like(s.omega_dot)

    omega_history: list[float] = []   # average ω_z over alive sites
    times: list[float] = []
    H_history: list[float] = []

    n_alive = int(s.mask_alive.sum())
    def avg_omega_z():
        return float(s.omega[..., 2].sum() / max(n_alive, 1))

    omega_history.append(avg_omega_z())
    times.append(s.time)
    H_history.append(s.total_hamiltonian())

    for step in range(1, n_steps + 1):
        s.step()
        omega_history.append(avg_omega_z())
        times.append(s.time)
        H_history.append(s.total_hamiltonian())

    times_a = np.asarray(times)
    omega_a = np.asarray(omega_history)

    # Detect period: use zero-crossings or peaks. The field oscillates about 0
    # if we interpret "equilibrium" as ω = 0, OR about A₀ if there's no net
    # force. Since the micropolar term is quadratic in ω, the equilibrium IS
    # ω = 0, so we expect sinusoidal oscillation about 0.
    from scipy.signal import find_peaks
    peaks, _ = find_peaks(omega_a, height=0.5 * A0)
    if len(peaks) >= 2:
        period_meas = float(np.mean(np.diff(times_a[peaks])))
    else:
        # Fall back to FFT
        dt_avg = np.diff(times_a).mean()
        freqs = np.fft.rfftfreq(len(omega_a), d=dt_avg)
        spec = np.abs(np.fft.rfft(omega_a - omega_a.mean()))
        spec[0] = 0
        idx_peak = int(np.argmax(spec))
        period_meas = 1.0 / freqs[idx_peak] if freqs[idx_peak] > 0 else float("nan")

    # W_micropolar = Σᵢⱼ (ε_antisym,ij)² = 2·|ω|² for uniform ω_z
    # (ε_xy = −ω_z and ε_yx = +ω_z contribute equally).
    # So W = 2·G_c·|ω|² → ∂W/∂ω_z = 4·G_c·ω_z
    # → I_ω·ω̈ = −4·G_c·ω  → ω_mass² = 4·G_c/I_ω.
    omega_mass = np.sqrt(4.0 * G_c / s.I_omega)
    period_theory = 2.0 * np.pi / omega_mass
    H_drift = float(np.abs(np.asarray(H_history) / max(H_history[0], 1e-30) - 1).max())

    return {
        "G_c": G_c,
        "A0": A0,
        "omega_mass_theory": float(omega_mass),
        "period_theory": float(period_theory),
        "period_measured": period_meas,
        "period_ratio": period_meas / period_theory if np.isfinite(period_meas) else float("nan"),
        "times": times_a,
        "omega_avg_history": omega_a,
        "H_history": np.asarray(H_history),
        "H_drift_max": H_drift,
    }


# ─────────────────────────────────────────────────────────────────
# Plotting
# ─────────────────────────────────────────────────────────────────
def render_plots(
    t1a: dict, t1b: dict, t2: dict,
    out_path: str = "/tmp/cosserat_wave_test.png",
) -> None:
    fig, axes = plt.subplots(2, 2, figsize=(13, 9))

    # Top-left: T1a (G_c=0, gapless)
    ax = axes[0, 0]
    ax.plot(t1a["times"], t1a["centroids"], "o-", ms=3, lw=1.3, color="#2a7",
            label="centroid x")
    t = t1a["times"]
    ax.plot(t, t1a["centroids"][0] + t1a["c_R_theory_continuum"] * t,
            "--", lw=1, color="#666",
            label=f"c_R continuum = {t1a['c_R_theory_continuum']:.2f}")
    ax.plot(t, t1a["centroids"][0] + t1a["v_g_theory_gapped"] * t,
            ":", lw=1, color="#f90",
            label=f"v_g gapped = {t1a['v_g_theory_gapped']:.3f}")
    ax.set_xlabel("t (natural units)")
    ax.set_ylabel("packet centroid x (cells)")
    ax.set_title(
        f"T1a — GAPLESS rotation (G_c=0, γ=1)\n"
        f"v_measured = {t1a['v_measured']:.3f}   v / c_R = {t1a['v_over_c_R']:.2f}"
    )
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3)

    # Top-right: T1b (G_c=1, gapped)
    ax = axes[0, 1]
    ax.plot(t1b["times"], t1b["centroids"], "o-", ms=3, lw=1.3, color="#c33",
            label="centroid x")
    t = t1b["times"]
    ax.plot(t, t1b["centroids"][0] + t1b["v_g_theory_gapped"] * t,
            ":", lw=1, color="#f90",
            label=f"v_g gapped = {t1b['v_g_theory_gapped']:.3f}")
    ax.set_xlabel("t")
    ax.set_ylabel("packet centroid x (cells)")
    ax.set_title(
        f"T1b — GAPPED rotation (G_c=1, γ=1)\n"
        f"v_measured = {t1b['v_measured']:.3f}   v / v_g_th = {t1b['v_over_v_g_theory']:.2f}"
    )
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3)

    # Bottom-left: T2 mass-gap oscillation
    ax = axes[1, 0]
    ax.plot(t2["times"], t2["omega_avg_history"] / t2["A0"], "-", lw=1.5, color="#47c",
            label="⟨ω_z⟩ / A₀")
    ax.axhline(0, color="#666", ls="--", lw=0.5)
    # Overlay theoretical sinusoid
    omega_th = np.cos(t2["omega_mass_theory"] * t2["times"])
    ax.plot(t2["times"], omega_th, "--", lw=1.0, color="#f90",
            label=f"cos(√(2G_c/I_ω)·t)  T = {t2['period_theory']:.2f}")
    ax.set_xlabel("t")
    ax.set_ylabel("⟨ω_z⟩ / A₀")
    ax.set_title(
        f"T2 — Mass-gap oscillation (uniform ω_z)\n"
        f"T_meas = {t2['period_measured']:.3f}   T_th = {t2['period_theory']:.3f}   "
        f"ratio = {t2['period_ratio']:.3f}"
    )
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3)

    # Bottom-right: Hamiltonian conservation across all 3 tests
    ax = axes[1, 1]
    for res, lbl, col in [(t1a, "T1a gapless", "#2a7"),
                          (t1b, "T1b gapped", "#c33"),
                          (t2, "T2 mass-gap", "#47c")]:
        t = res["times"]
        H = res["H_history"]
        ax.plot(t, H / max(abs(H[0]), 1e-30) - 1.0,
                lw=1.2, label=f"{lbl}  |ΔH/H|max = {res['H_drift_max']:.2e}",
                color=col)
    ax.axhline(0, color="#666", ls="--", lw=0.5)
    ax.set_xlabel("t")
    ax.set_ylabel("ΔH / H₀")
    ax.set_title("T3 — Velocity-Verlet energy conservation\n(O(dt²) drift expected)")
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig(out_path, dpi=110)
    plt.close()
    print(f"Saved {out_path}")


if __name__ == "__main__":
    import json

    print("── Phase I validation: time-domain Cosserat ──\n")

    print("T1a — gapless (G_c=0, γ=1)…")
    t1a = test_wave_speed(N=64, G_c=0.0, gamma=1.0)
    print(f"  c_R continuum  = {t1a['c_R_theory_continuum']:.4f}")
    print(f"  v_g theory     = {t1a['v_g_theory_gapped']:.4f}")
    print(f"  v_measured     = {t1a['v_measured']:.4f}")
    print(f"  v / c_R        = {t1a['v_over_c_R']:.4f}")
    print(f"  H drift max    = {t1a['H_drift_max']:.3e}")
    print()

    print("T1b — gapped (G_c=1, γ=1)…")
    t1b = test_wave_speed(N=64, G_c=1.0, gamma=1.0)
    print(f"  c_R continuum  = {t1b['c_R_theory_continuum']:.4f}")
    print(f"  v_g theory     = {t1b['v_g_theory_gapped']:.4f}")
    print(f"  v_measured     = {t1b['v_measured']:.4f}")
    print(f"  v / v_g_th     = {t1b['v_over_v_g_theory']:.4f}")
    print(f"  H drift max    = {t1b['H_drift_max']:.3e}")
    print()

    print("T2 — uniform ω_z mass-gap oscillation…")
    t2 = test_mass_gap_oscillation(N=32, G_c=1.0, n_steps=150)
    print(f"  ω_mass theory  = √(2G_c/I_ω) = {t2['omega_mass_theory']:.4f}")
    print(f"  T theory        = 2π/ω_mass    = {t2['period_theory']:.4f}")
    print(f"  T measured     = {t2['period_measured']:.4f}")
    print(f"  ratio T/T_th   = {t2['period_ratio']:.4f}")
    print(f"  H drift max    = {t2['H_drift_max']:.3e}")
    print()

    render_plots(t1a, t1b, t2)

    summary = {
        "T1a_G_c": t1a["G_c"], "T1a_v_measured": t1a["v_measured"],
        "T1a_c_R_theory": t1a["c_R_theory_continuum"],
        "T1a_v_over_c_R": t1a["v_over_c_R"],
        "T1a_v_over_v_g_gapped": t1a["v_over_v_g_theory"],
        "T1a_H_drift_max": t1a["H_drift_max"],
        "T1b_G_c": t1b["G_c"], "T1b_v_measured": t1b["v_measured"],
        "T1b_v_g_theory": t1b["v_g_theory_gapped"],
        "T1b_v_over_v_g_gapped": t1b["v_over_v_g_theory"],
        "T1b_H_drift_max": t1b["H_drift_max"],
        "T2_omega_mass_theory": t2["omega_mass_theory"],
        "T2_period_theory": t2["period_theory"],
        "T2_period_measured": t2["period_measured"],
        "T2_period_ratio": t2["period_ratio"],
        "T2_H_drift_max": t2["H_drift_max"],
    }
    print("── Summary ──")
    print(json.dumps(summary, indent=2))
    np.savez("/tmp/cosserat_wave_test.npz", **summary)
