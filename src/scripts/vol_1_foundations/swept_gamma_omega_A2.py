"""
Swept Γ(ω, A²) — the electron as a parametric oscillator at threshold.

Characterizes the 2-D (A², ω_drive) parametric-instability surface of the
saturating bond LC tank — the EE-correct step that should have preceded the
genesis seed-and-watch attempts (which were 1-D amplitude cuts of this surface).

FRAME (Grant, electron-synthesis epic; see
research/2026-06-07_swept-gamma-omega-A2-parametric-characterization.md):
  electron = PARAMETRIC OSCILLATOR AT THRESHOLD.
    - varactor reactance C_eff = C₀/S(A) (Axiom 4)         = the GAIN
    - dark-wake back-reaction (DarkWakeObserver)           = the LOSS
    - threshold (gain = loss) self-oscillates as ω_C       = the Compton clock

SUBSTRATE-NATIVE MODEL (substrate-native-check §1, replaces the SM-bracketed
"Dynamical Casimir" derivation): the bond LC with Op14-saturation-modulated
stiffness is a MATHIEU/HILL parametric oscillator. The tank ringing at peak
strain A₀ self-modulates its stiffness ω_C²·S(A(t)) at the pump frequency
ω_drive = 2×(ring), giving parametric gain. We map the (A², ω_drive) Floquet
tongue (the GAIN), the static Op3 reflection Γ(A²) (the CAVITY), and the
dark-wake threshold locus (the LOSS).

NO engine mutation; reduced bond-LC model. Canonical constants imported, never
hard-coded (ave-canonical-source). ω_C = 1 engine-natural (the Compton clock =
LC eigenfrequency; theorem-3-1-q-factor.md:28).

Outputs:
  swept_gamma_omega_A2_results.json
  swept_gamma_omega_A2_tongue_map.png
"""

import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))

# ── Canonical source (ave-canonical-source): import, never hard-code ──────────
from ave.core.constants import (
    ALPHA,            # 7.2973525693e-3  fine-structure constant
    ALPHA_COLD_INV,   # 4π³+π²+π ≈ 137.0363  (geometric α⁻¹, the SEPARATE axis)
    R_I,              # √(2α)  Linear→NonLinear A-onset
    R_II,             # √3/2   NonLinear→Saturated A-onset
    R_III,            # 1.0    Saturated→Rupture
    V_YIELD,          # √α·V_SNAP ≈ 43.65 kV  (A ≡ V/V_yield, so A_yield = 1)
    V_SNAP,           # m_e c²/e ≈ 511 kV
)

# canonical-source verification (catch package shadowing / wrong import)
import ave.core.constants as _avc
assert _avc.__file__.endswith("ave/core/constants.py"), "wrong ave.core.constants"
assert abs(ALPHA - 7.2973525693e-3) < 1e-12, "ALPHA drift"
assert abs(R_I - np.sqrt(2.0 * ALPHA)) < 1e-12, "R_I = √(2α) drift"
assert abs(ALPHA_COLD_INV - (4.0 * np.pi**3 + np.pi**2 + np.pi)) < 1e-9, "α_cold drift"

OMEGA_C = 1.0  # Compton clock = LC eigenfrequency, engine-natural units
A2_YIELD = 1.0  # A ≡ V/V_yield → A_yield = 1 (S(A)=√(1−A²) ⇒ S(A_yield)=0)


# ── Op14 saturation kernel (Axiom 4) ──────────────────────────────────────────
def S_kernel(A2):
    """S(A) = √(1 − A²), the universal quarter-arc saturation kernel (Op14).
    A² already normalized to A_yield (A = V/V_yield). Clipped below rupture."""
    return np.sqrt(np.clip(1.0 - A2, 1e-12, 1.0))


# ── Floquet monodromy of the parametrically-pumped bond LC ────────────────────
def floquet_max_multiplier(A2_op, omega_drive, gamma, n_steps=4000):
    """|λ_max| of the bond LC q̈ + γ q̇ + ω_C²·S(A(t))·q = 0, with the tank
    biased at peak strain A₀²=A2_op so A(t)² = A₀²·cos²(ω_drive·t/2) and the
    Op14-saturation stiffness self-modulates at the pump frequency ω_drive.

    Returns the largest |Floquet multiplier| over ONE pump period
    T = 2π/ω_drive. |λ_max| > 1 ⟺ parametric GAIN (the tongue);
    |λ_max| = the per-pump-period reflection gain |Γ|_eff (active medium).

    Vectorized over arbitrarily-shaped (A2_op, omega_drive, gamma) arrays.
    Normalized time τ = t/T ∈ [0,1]: ω_drive·t/2 = π·τ, so the stiffness shape
    cos²(πτ) is Ω-independent and only T=2π/ω_drive scales the RHS — lets one
    τ-loop serve the whole grid (per-point T scaling)."""
    A2_op = np.asarray(A2_op, dtype=float)
    omega_drive = np.asarray(omega_drive, dtype=float)
    gamma = np.asarray(gamma, dtype=float)
    A2_op, omega_drive, gamma = np.broadcast_arrays(A2_op, omega_drive, gamma)
    shape = A2_op.shape
    T = 2.0 * np.pi / omega_drive  # pump period per grid point

    # State M: columns = the two fundamental solutions (ICs (q,v)=(1,0),(0,1)).
    # q_cols[...,j], v_cols[...,j] for j∈{0,1}; M = [[q0,q1],[v0,v1]].
    q = np.stack([np.ones(shape), np.zeros(shape)], axis=-1)
    v = np.stack([np.zeros(shape), np.ones(shape)], axis=-1)

    dtau = 1.0 / n_steps
    Te = T[..., None]      # broadcast over the 2 IC columns
    ge = gamma[..., None]
    A2e = A2_op[..., None]

    def deriv(tau, q, v):
        A2_t = A2e * np.cos(np.pi * tau) ** 2          # instantaneous strain²
        k = OMEGA_C**2 * S_kernel(A2_t)                # Op14-modulated stiffness
        dq = Te * v
        dv = Te * (-ge * v - k * q)
        return dq, dv

    for i in range(n_steps):
        tau = i * dtau
        k1q, k1v = deriv(tau, q, v)
        k2q, k2v = deriv(tau + 0.5 * dtau, q + 0.5 * dtau * k1q, v + 0.5 * dtau * k1v)
        k3q, k3v = deriv(tau + 0.5 * dtau, q + 0.5 * dtau * k2q, v + 0.5 * dtau * k2v)
        k4q, k4v = deriv(tau + dtau, q + dtau * k3q, v + dtau * k3v)
        q = q + (dtau / 6.0) * (k1q + 2 * k2q + 2 * k3q + k4q)
        v = v + (dtau / 6.0) * (k1v + 2 * k2v + 2 * k3v + k4v)

    # Monodromy M = [[q[...,0], q[...,1]], [v[...,0], v[...,1]]]; eigenvalues of 2×2:
    a = q[..., 0]; b = q[..., 1]; c = v[..., 0]; d = v[..., 1]
    tr = a + d
    det = a * d - b * c
    disc = tr * tr - 4.0 * det
    sq = np.sqrt(disc.astype(complex))
    lam1 = 0.5 * (tr + sq)
    lam2 = 0.5 * (tr - sq)
    return np.maximum(np.abs(lam1), np.abs(lam2))


# ── Static Op3 reflection (the CAVITY-formation axis) ─────────────────────────
def gamma_op3(A2, polarity="low_Z"):
    """Static bond reflection Γ_Op3 = (Z−Z₀)/(Z+Z₀) at operating-point strain.
    Two polarities (FLAG-POLARITY / optionD-C4):
      low_Z  (canonical, Meissner μ-branch): Z = Z₀·√S  → Γ→−1 as A²→1 (short)
      high_Z (engine z_local default):       Z = Z₀/√S  → Γ→+1 as A²→1 (open)
    Magnitude |Γ| (cavity formation) is polarity-independent; sign is the fork."""
    S = S_kernel(A2)
    if polarity == "low_Z":
        Zr = np.sqrt(S)
    else:
        Zr = 1.0 / np.sqrt(S)
    return (Zr - 1.0) / (Zr + 1.0)


def main():
    print("=" * 78, flush=True)
    print("  Swept Γ(ω, A²) — electron as parametric oscillator at threshold")
    print("=" * 78, flush=True)
    print(f"  ALPHA={ALPHA:.10e}  1/α={1/ALPHA:.4f}  α_cold⁻¹={ALPHA_COLD_INV:.4f}")
    print(f"  A-onsets: R_I=√(2α)={R_I:.4f} (lin→NL)  R_II={R_II:.4f} (NL→sat)  "
          f"R_III={R_III:.1f} (rupture)")
    print(f"  ω_C={OMEGA_C}  V_YIELD={V_YIELD:.1f}V  V_SNAP={V_SNAP:.1f}V", flush=True)

    # ── Grid ──────────────────────────────────────────────────────────────────
    A2_grid = np.linspace(0.01, 0.97, 49)          # operating-point peak strain
    omega_grid = np.linspace(0.20, 3.00, 141)      # pump/drive freq in ω_C units
    A2M, OM = np.meshgrid(A2_grid, omega_grid, indexing="ij")

    # ── (1) LOSSLESS tongue map |λ_max|(A², ω_drive) — the bare engine ─────────
    print("\n  [1] Lossless tongue map (γ=0) ...", flush=True)
    lam_lossless = floquet_max_multiplier(A2M, OM, 0.0)
    gain_lossless = np.log(np.clip(lam_lossless, 1e-300, None))  # ln|λ| ≥0 ⟺ gain

    # principal-tongue ridge per A²: the ω_drive of max gain
    ridge_idx = np.argmax(gain_lossless, axis=1)
    ridge_omega = omega_grid[ridge_idx]
    # analytic Op14-softened prediction: ω_drive = 2 ω_C √(1 − ¼A²)
    ridge_pred = 2.0 * OMEGA_C * np.sqrt(np.clip(1.0 - 0.25 * A2_grid, 0.0, 1.0))

    # tongue at the exact principal-resonance column (nearest to 2ω_C) vs A²
    j2 = int(np.argmin(np.abs(omega_grid - 2.0 * OMEGA_C)))
    gain_at_2wc = gain_lossless[:, j2]

    # ridge match ONLY where the tongue is resolved (gain appreciable); the
    # tongue half-width ∝ ¼A² vanishes as A²→0, so small-A² argmax is grid-noise.
    resolved = gain_lossless.max(axis=1) > 0.02
    ridge_err = np.abs(ridge_omega - ridge_pred)
    mean_ridge_err = float(np.mean(ridge_err[resolved])) if resolved.any() else float("nan")
    for a2t in (0.2, 0.5, 0.8):
        k = int(np.argmin(np.abs(A2_grid - a2t)))
        print(f"      ridge(A²={A2_grid[k]:.2f}) measured ω_drive={ridge_omega[k]:.3f}  "
              f"predict 2ω_C√(1−¼A²)={ridge_pred[k]:.3f}  (Op14 down-bend)")
    print(f"      mean |ridge−Op14pred| over resolved tongue (A²≳0.05) = {mean_ridge_err:.3f} ω_C")
    print(f"      max |λ| on lossless grid = {lam_lossless.max():.3f}  (>1 on ridge ⟹ "
          f"POSITIVE Floquet exponent = exponential pump = the lossless 4× artifact)")

    # ── (2) Static Op3 reflection Γ(A²) — the CAVITY axis (both polarities) ────
    print("\n  [2] Static Op3 reflection Γ(A²) — cavity formation ...", flush=True)
    A2_fine = np.linspace(0.0, 0.999, 400)
    gam_lowZ = gamma_op3(A2_fine, "low_Z")
    gam_highZ = gamma_op3(A2_fine, "high_Z")
    # cross-check against observed optionD genesis points
    obs = {"1x_A2": 0.23, "1x_Gamma_obs": -0.011, "4x_A2": 0.97, "4x_Gamma_obs": -0.994}
    g_1x = float(gamma_op3(np.array(obs["1x_A2"]), "low_Z"))
    g_4x = float(gamma_op3(np.array(obs["4x_A2"]), "low_Z"))
    print(f"      low-Z (canonical short):  Γ(A²=0.23)={g_1x:+.3f} "
          f"(obs {obs['1x_Gamma_obs']:+.3f})  Γ(A²=0.97)={g_4x:+.3f} "
          f"(obs {obs['4x_Gamma_obs']:+.3f})")
    # cavity-formation threshold: |Γ| crosses 0.9
    a2_cav = float(A2_fine[np.argmin(np.abs(np.abs(gam_lowZ) - 0.9))])
    print(f"      cavity (|Γ|>0.9) forms only at A² ≳ {a2_cav:.3f} (→1) — "
          f"a SEPARATE threshold from parametric gain")

    # ── (3) α-readout (the HEADLINE) ──────────────────────────────────────────
    # GAIN is α-free: nowhere above did α enter the Floquet map or the ridge.
    # Q=1/α is α-ENCODED: to land Q=1/α we must SET γ=α·ω_C by hand. Demonstrate.
    print("\n  [3] α-readout (consistency-vs-emergence headline) ...", flush=True)
    gamma_for_Q_alpha = ALPHA * OMEGA_C          # γ s.t. Q=ω_C/γ = 1/α (α INPUT)
    Q_alpha = OMEGA_C / gamma_for_Q_alpha
    print(f"      GAIN: pump depth, ridge, |λ| computed with ZERO α input "
          f"⟹ α-DECOUPLED (geometry of S(A)).")
    print(f"      Q=1/α requires γ:=α·ω_C={gamma_for_Q_alpha:.4e} ⟹ Q={Q_alpha:.3f}=1/α "
          f"is α-ENCODED (loss carries α; NOT an emergence of 137).")

    # ── (4) STRETCH — dark-wake LOSS → bounded threshold locus (gain=loss) ─────
    # For each A², find the loss γ (→ Q=ω_C/γ) at which the ridge gain |λ|=1.
    # That (A², Q) curve is the gain=loss threshold = where a stable self-osc lives.
    print("\n  [4] Dark-wake threshold locus (bounded, gain=loss) ...", flush=True)
    A2_thr = np.linspace(0.02, 0.95, 40)
    Q_threshold = np.zeros_like(A2_thr)
    gamma_threshold = np.zeros_like(A2_thr)
    for i, a2 in enumerate(A2_thr):
        # ridge ω for this A² (Op14-softened principal resonance)
        w_ridge = 2.0 * OMEGA_C * np.sqrt(max(1.0 - 0.25 * a2, 1e-6))
        # bisection on γ: find γ* where |λ_max(a2, w_ridge, γ)| = 1
        glo, ghi = 0.0, 2.0
        lam_lo = float(floquet_max_multiplier(a2, w_ridge, glo))
        lam_hi = float(floquet_max_multiplier(a2, w_ridge, ghi))
        if lam_lo <= 1.0:
            gamma_threshold[i] = 0.0
        elif lam_hi > 1.0:
            gamma_threshold[i] = ghi  # tongue survives even huge loss (shouldn't)
        else:
            for _ in range(50):
                gm = 0.5 * (glo + ghi)
                lam = float(floquet_max_multiplier(a2, w_ridge, gm))
                if lam > 1.0:
                    glo = gm
                else:
                    ghi = gm
            gamma_threshold[i] = 0.5 * (glo + ghi)
        Q_threshold[i] = OMEGA_C / gamma_threshold[i] if gamma_threshold[i] > 0 else np.inf

    # Where does the electron operating point sit? Solve: at Q=1/α (γ=α·ω_C),
    # what A² is exactly at threshold (gain=loss) — the SELF-SELECTED amplitude?
    # threshold γ(A²) is monotonic in A²; invert at γ=α.
    finite = gamma_threshold > 0
    if finite.sum() >= 2:
        A2_self = float(np.interp(gamma_for_Q_alpha, gamma_threshold[finite], A2_thr[finite]))
    else:
        A2_self = float("nan")
    print(f"      threshold loss γ*(A²) rises with A² (more gain ⟹ more loss to bound).")
    print(f"      at Q=1/α (γ=α·ω_C): self-selected gain=loss amplitude A²_self = {A2_self:.4f}")
    print(f"      compare canonical A-scales: R_I²=2α={R_I**2:.4f}, 8α={8*ALPHA:.4f}, "
          f"P_C=8πα={8*np.pi*ALPHA:.4f}, observed 1× A²≈0.23")

    # ── Save JSON ─────────────────────────────────────────────────────────────
    out = {
        "frame": "electron = parametric oscillator at threshold; gain=varactor, loss=dark-wake",
        "omega_C": OMEGA_C,
        "alpha": ALPHA,
        "alpha_inv": 1.0 / ALPHA,
        "alpha_cold_inv_geometric": ALPHA_COLD_INV,
        "A_onsets": {"R_I_sq_2alpha": R_I**2, "R_II": R_II, "R_III": R_III},
        "grid": {"A2": A2_grid.tolist(), "omega_drive": omega_grid.tolist()},
        "lossless_tongue": {
            "log_gain": gain_lossless.tolist(),
            "lam_max_global": float(lam_lossless.max()),
            "ridge_omega_measured": ridge_omega.tolist(),
            "ridge_omega_predicted_2wc_op14": ridge_pred.tolist(),
            "mean_ridge_err_resolved_omegaC": mean_ridge_err,
            "gain_at_2omegaC_vs_A2": gain_at_2wc.tolist(),
        },
        "static_cavity": {
            "A2": A2_fine.tolist(),
            "Gamma_lowZ_canonical": gam_lowZ.tolist(),
            "Gamma_highZ_engine": gam_highZ.tolist(),
            "observed": obs,
            "Gamma_lowZ_at_obs": {"1x": g_1x, "4x": g_4x},
            "cavity_threshold_A2": a2_cav,
        },
        "alpha_readout": {
            "gain_alpha_input": False,
            "gain_class": "D-eligible (alpha-DECOUPLED geometry of S(A))",
            "Q_eq_1_over_alpha_requires_gamma": gamma_for_Q_alpha,
            "Q_value": Q_alpha,
            "Q_class": "A/C identity-consistency (alpha-ENCODED via loss; theorem-3-1 PathA)",
            "headline": "gain is alpha-free; Q=1/alpha is alpha-in-alpha-out (NOT emergence of 137)",
        },
        "darkwake_threshold": {
            "A2": A2_thr.tolist(),
            "gamma_threshold": gamma_threshold.tolist(),
            "Q_threshold": [None if not np.isfinite(q) else q for q in Q_threshold],
            "gamma_for_Q_alpha": gamma_for_Q_alpha,
            "A2_self_selected_at_Q_alpha": A2_self,
        },
    }
    out_path = Path(__file__).parent / "swept_gamma_omega_A2_results.json"
    out_path.write_text(json.dumps(out, indent=2, default=str), encoding="utf-8")
    print(f"\n  Saved {out_path.name}")

    # ── Viz ───────────────────────────────────────────────────────────────────
    try:
        make_viz(A2_grid, omega_grid, gain_lossless, ridge_pred, A2_fine, gam_lowZ,
                 gam_highZ, obs, A2_thr, gamma_threshold, gamma_for_Q_alpha, A2_self)
    except Exception as e:  # plotting is non-load-bearing
        print(f"  (viz skipped: {e})")

    return out


def make_viz(A2_grid, omega_grid, gain_lossless, ridge_pred, A2_fine, gam_lowZ,
             gam_highZ, obs, A2_thr, gamma_threshold, gamma_alpha, A2_self):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(1, 3, figsize=(18, 5.5))

    # Panel A — the lossless tongue map (the GAIN surface)
    extent = [omega_grid[0], omega_grid[-1], A2_grid[0], A2_grid[-1]]
    im = ax[0].imshow(gain_lossless, origin="lower", aspect="auto", extent=extent,
                      cmap="inferno", vmin=0)
    ax[0].plot(ridge_pred, A2_grid, "c--", lw=2,
               label=r"$2\omega_C\sqrt{1-A^2/4}$ (Op14)")
    ax[0].axvline(2.0, color="w", ls=":", lw=1, label=r"$2\omega_C$")
    ax[0].axvline(1.0, color="0.6", ls=":", lw=1, label=r"$\omega_C$ (signal)")
    ax[0].set_xlabel(r"pump / drive $\omega_{drive}/\omega_C$")
    ax[0].set_ylabel(r"operating-point strain $A^2$")
    ax[0].set_title("A. LOSSLESS parametric tongue  ln|λ|  (the GAIN)\n"
                    "unbounded ridge = the 4× pump artifact")
    ax[0].legend(loc="upper left", fontsize=8)
    fig.colorbar(im, ax=ax[0], label=r"ln|λ| (parametric gain/period)")

    # Panel B — static Op3 reflection (the CAVITY axis)
    ax[1].plot(A2_fine, gam_lowZ, "b-", lw=2, label=r"low-Z canonical ($Z=Z_0\sqrt{S}$, short)")
    ax[1].plot(A2_fine, gam_highZ, "r-", lw=2, label=r"high-Z engine ($Z=Z_0/\sqrt{S}$, open)")
    ax[1].plot(obs["1x_A2"], obs["1x_Gamma_obs"], "ko", ms=9, label="optionD 1× (A²=0.23, no wall)")
    ax[1].plot(0.999, obs["4x_Gamma_obs"], "k^", ms=9, label="optionD 4× (A²→1, Γ→−1)")
    ax[1].annotate("4× drives A²→1 (rupture);\nengine asym-μ wall steeper\nthan symmetric toy",
                   xy=(0.999, -0.994), xytext=(0.55, -0.75), fontsize=7,
                   arrowprops=dict(arrowstyle="->", lw=0.8))
    ax[1].axhline(0, color="0.7", lw=0.8)
    for rv in (2 * ALPHA, 0.75):
        ax[1].axvline(rv, color="0.8", ls=":", lw=1)
    ax[1].set_xlabel(r"operating-point strain $A^2$")
    ax[1].set_ylabel(r"static $\Gamma_{Op3}(A^2)$")
    ax[1].set_title("B. CAVITY formation (static Op3 wall)\n"
                    "|Γ|→1 only as A²→1 — separate threshold from gain")
    ax[1].legend(loc="lower left", fontsize=8)
    ax[1].set_ylim(-1.05, 1.05)

    # Panel C — dark-wake threshold locus (gain=loss), electron operating point
    okg = gamma_threshold > 0
    ax[2].plot(A2_thr[okg], gamma_threshold[okg], "g-o", ms=4, lw=2,
               label=r"threshold loss $\gamma^*(A^2)$ (gain=loss)")
    ax[2].axhline(gamma_alpha, color="m", ls="--", lw=2,
                  label=r"$\gamma=\alpha\,\omega_C$ (Q=1/α loss)")
    if np.isfinite(A2_self):
        ax[2].plot(A2_self, gamma_alpha, "m*", ms=18,
                   label=fr"self-osc A²={A2_self:.3f} @ Q=1/α")
    ax[2].axvline(2 * ALPHA, color="0.7", ls=":", lw=1, label=r"$2\alpha=R_I^2$")
    ax[2].set_xlabel(r"operating-point strain $A^2$")
    ax[2].set_ylabel(r"loss $\gamma/\omega_C$ to bound the tongue")
    ax[2].set_title("C. Dark-wake LOSS → BOUNDED threshold (the STRETCH)\n"
                    "where a stable parametric self-oscillator lives")
    ax[2].legend(loc="upper left", fontsize=8)
    ax[2].set_yscale("log")

    fig.suptitle("Swept Γ(ω, A²): electron = parametric oscillator at threshold — "
                 "GAIN (varactor) · CAVITY (Op3) · LOSS (dark-wake)", fontsize=12)
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    out = Path(__file__).parent / "swept_gamma_omega_A2_tongue_map.png"
    fig.savefig(out, dpi=130)
    print(f"  Saved {out.name}")


if __name__ == "__main__":
    main()
