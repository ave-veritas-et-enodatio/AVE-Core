"""
CVR EE-sweep — the six computed views of the vacuum resonant cavity.
====================================================================

Driver for the Vacuum-Circuit-Analysis (VCA) full circuit analysis. Every curve
is a projection of the one constitutive spine in ``cvr_model.py`` (canonical
constants, Axiom-4 kernel, the 2x2 chiral H(s)). Re-runnable and deterministic:
the audit reproduces every curve by running this one script.

    PYTHONPATH=$PWD/src python src/scripts/vol_9_device/cvr_ee_sweep/cvr_ee_sweep.py

THE SIX VIEWS (each -> one KB leaf in vol4/circuit-theory/ch1):
  1. DC operating point   C_eff/Z/c vs A0 + load line + electron op-point   -> cvr-dc-operating-point
  2. AC transfer function Bode |H|,arg(H) + pole-zero, Q=1/alpha, BW=alpha*w0 -> cvr-transfer-function
  3. Reflection / Smith   Gamma(A) locus + |Gamma|^2=1-alpha + chiral S       -> cvr-reflection-smith
  4. Phasor / reactance   V_inc/V_ref + C<->L Lissajous breather              -> cvr-phasor-reactance
  5. Stability / eigenmode root-locus + Nyquist (the eigenmode loop)          -> cvr-stability-eigenmode
  6. Parameter basin      bias x amplitude -> region-of-attraction map        (folds into #5)

HONESTY (ave-driver-script-honesty): every number is computed from cvr_model;
figures caption the actual data; the carried flags (sector-attribution,
S^0.5-vs-S^0.25 exponent defect, S_min clip) are drawn ON the figures, not hidden.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))  # repo/src on path

import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.colors import ListedColormap  # noqa: E402

from ave.core.constants import ALPHA  # noqa: E402
from ave.viz import style  # noqa: E402

# cvr_model lives beside this driver
sys.path.insert(0, str(Path(__file__).resolve().parent))
import cvr_model as M  # noqa: E402

OUT = Path(__file__).parent / "_output"
OUT.mkdir(exist_ok=True)

ALPHA_INV = 1.0 / ALPHA

# House figure style (ave-figure-discipline): print profile, white bg, Okabe-Ito
# palette. Applied once before any figure is created.
style.apply()
print(f"[style] ave.viz.style applied — profile=print (white bg), palette=Okabe-Ito")


# ===========================================================================
# View 1 — DC operating point (the varactor C-V characteristic + load line)
# ===========================================================================
def view1_dc_operating_point() -> dict:
    A = np.linspace(0.0, M.A_CAP, 400)
    S = M.saturation_kernel(A)
    Ceff = M.c_eff_capacitance(A)  # C_eff/C0
    Zc = M.z_core(A) / M.Z_0  # Z_core/Z0
    cEM = M.c_em(A) / M.C_0  # c_EM/c0
    cSh = M.c_shear(A) / M.C_0  # c_shear/c0

    fig, axes = plt.subplots(2, 2, figsize=(11, 8))

    ax = axes[0, 0]
    ax.plot(A, Ceff, "-", color=style.COLORS["ave"], lw=2, label=r"$C_{eff}/C_0 = 1/S(A_0)$")
    ax.axvline(M.A_CAP, color=style.COLORS["muted"], ls=":", lw=1)
    ax.text(M.A_CAP, 2, " A_CAP\n(apparatus clip)", fontsize=7, color=style.COLORS["muted"], va="bottom")
    ax.set_yscale("log")
    ax.set_xlabel(style.axis_label("Operating point", "A_0 = |V|/V_{yield}", ""))
    ax.set_ylabel(style.axis_label("Effective capacitance", "C_{eff}/C_0", ""))
    style.legend(ax, fontsize=8, where="below")
    ax.grid(alpha=0.3)

    ax = axes[0, 1]
    ax.plot(A, Zc, "-", color=style.COLORS["comparison"], lw=2, label=r"$Z_{core}/Z_0 = \sqrt{S(A_0)}$")
    ax.axhline(0, color=style.COLORS["data"], lw=0.5)
    ax.set_xlabel(style.axis_label("Operating point", "A_0", ""))
    ax.set_ylabel(style.axis_label("Core impedance", "Z_{core}/Z_0", ""))
    # NEUTRAL framing (PR#260 B3-DEGENERATE): the mu-vs-eps fork is a sign/spin
    # selector, degenerate on the equilibrium observables — NOT a "magnetic
    # PRIMARY" adjudication (that was walked back; sector-attribution resolved).
    ax.text(0.05, 0.5, r"$\mu$-vs-$\varepsilon$ fork = sign/spin selector," + "\n"
            + r"degenerate on $Z(A)=Z_0\sqrt{S}$" + "\n(both routes, same trajectory)",
            fontsize=6.5, transform=ax.transAxes, va="center",
            bbox=dict(boxstyle="round", fc="white",
                      ec=style.COLORS["muted"], alpha=0.85))
    style.legend(ax, fontsize=8, where="below")
    ax.grid(alpha=0.3)

    ax = axes[1, 0]
    ax.plot(A, cEM, "-", color=style.COLORS["ave"], lw=2, label=r"$c_{EM}/c_0 = 1/S$  (Maxwell, →∞)")
    ax.plot(A, cSh, "--", color=style.COLORS["accent"], lw=2, label=r"$c_{shear}/c_0 = \sqrt{S}$  (mechanical, →0)")
    ax.set_yscale("log")
    ax.set_xlabel(style.axis_label("Operating point", "A_0", ""))
    ax.set_ylabel(style.axis_label("Substrate speed", "c_{eff}/c_0", ""))
    style.legend(ax, fontsize=8, where="below")
    ax.grid(alpha=0.3)

    # refractive index: single-sourced exponent (defect closed — engine n_EM = S^{1/2})
    ax = axes[1, 1]
    ax.plot(A, M.n_physical(A), "-", color=style.COLORS["data"], lw=2, label=r"$n_{\mathrm{EM}}=S^{1/2}$ (single-sourced)")
    ax.set_xlabel(style.axis_label("Operating point", "A_0", ""))
    ax.set_ylabel(style.axis_label("Refractive index", "n", ""))
    style.legend(ax, fontsize=8, where="below")
    ax.grid(alpha=0.3)

    style.save(fig, OUT / "fig1_dc_operating_point.png", formats=("png",))
    plt.close(fig)

    return {
        "A_grid_max": float(M.A_CAP),
        "Ceff_over_C0_at_A0.9": float(M.c_eff_capacitance(np.array(0.9))),
        "Zcore_over_Z0_at_A0.9": float(M.z_core(np.array(0.9)) / M.Z_0),
        "n_EM_at_A0.9": float(M.n_physical(np.array(0.9))),
    }


# ===========================================================================
# View 2 — AC transfer function (Bode + pole-zero), Q=1/alpha, BW=alpha*w0
# ===========================================================================
def view2_transfer_function() -> dict:
    A0 = 0.0  # cold reference operating point
    w0 = M.omega_local(A0)
    w = np.logspace(np.log10(w0) - 4, np.log10(w0) + 4, 2000)
    H = M.ELECTRON.H_scalar(1j * w, A0=A0)  # electron instance binds its own Q
    mag_db = 20 * np.log10(np.abs(H))
    phase = np.degrees(np.angle(H))

    p1, p2 = M.ELECTRON.poles(A0=A0)
    BW = w0 / M.Q_TANK  # = alpha*w0

    fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))

    ax = axes[0]
    ax.semilogx(w / w0, mag_db, "-", color=style.COLORS["ave"], lw=1.5)
    ax.axhline(20 * np.log10(M.Q_TANK), color=style.COLORS["comparison"], ls="--", lw=1,
               label=fr"peak $=20\log_{{10}}Q={20*np.log10(M.Q_TANK):.1f}$ dB")
    ax.axvline(1.0, color=style.COLORS["muted"], ls=":", lw=1)
    ax.set_xlabel(style.axis_label("Normalized frequency", r"\omega/\omega_C", ""))
    ax.set_ylabel(style.axis_label("Magnitude", "|H|", "dB"))
    style.legend(ax, fontsize=8, where="below")
    ax.grid(alpha=0.3, which="both")

    ax = axes[1]
    ax.semilogx(w / w0, phase, "-", color=style.COLORS["accent"], lw=1.5)
    ax.axvline(1.0, color=style.COLORS["muted"], ls=":", lw=1)
    ax.set_xlabel(style.axis_label("Normalized frequency", r"\omega/\omega_C", ""))
    ax.set_ylabel(style.axis_label("Phase", r"\arg H", "deg"))
    ax.grid(alpha=0.3, which="both")

    # pole-zero (normalized by w0)
    ax = axes[2]
    ax.plot([p1.real / w0, p2.real / w0], [p1.imag / w0, p2.imag / w0], "x",
            color=style.COLORS["comparison"], ms=12, mew=2,
            label=r"poles $s=-\alpha\omega_0/2 \pm j\omega_d$")
    ax.axvline(0, color=style.COLORS["data"], lw=0.5)
    ax.axhline(0, color=style.COLORS["data"], lw=0.5)
    ax.set_xlabel(style.axis_label(r"Re$(s)$", r"\mathrm{Re}(s)/\omega_0", ""))
    ax.set_ylabel(style.axis_label(r"Im$(s)$", r"\mathrm{Im}(s)/\omega_0", ""))
    # anchor repointed :81 -> :85 (per-cycle-leak content drifted; :85 is the
    # "fraction 1/Q = alpha leaks per cycle" line, :81 is the Z_0 definition)
    ax.text(0.04, 0.5, "distance from jω axis\n= α/2 = the per-cycle leak\n(theorem-3-1-q-factor.md:85)",
            fontsize=6.5, transform=ax.transAxes, va="center",
            bbox=dict(boxstyle="round", fc="white", ec=style.COLORS["muted"], alpha=0.85))
    style.legend(ax, fontsize=8, where="below")
    ax.grid(alpha=0.3)
    ax.set_xlim(-0.02, 0.005)

    style.save(fig, OUT / "fig2_transfer_function_bode.png", formats=("png",))
    plt.close(fig)

    return {
        "omega_C_rad_s": float(w0),
        "Q_tank": float(M.Q_TANK),
        "pole_real_over_w0": float(p1.real / w0),
        "minus_alpha_over_2": float(-ALPHA / 2),
        "bandwidth_rad_s": float(BW),
        "peak_mag_dB": float(20 * np.log10(M.Q_TANK)),
    }


# ===========================================================================
# View 3 — Reflection on the Smith chart: |Gamma|^2 = 1 - alpha + chiral S
# ===========================================================================
def _draw_smith(ax):
    """Minimal Smith chart: unit circle + a few constant-R and constant-X arcs."""
    th = np.linspace(0, 2 * np.pi, 400)
    ax.plot(np.cos(th), np.sin(th), "-", color=style.COLORS["data"], lw=1)
    for r in (0.5, 1.0, 2.0):  # constant-resistance circles
        c, rad = r / (1 + r), 1 / (1 + r)
        ax.plot(c + rad * np.cos(th), rad * np.sin(th), color=style.COLORS["muted"], lw=0.5, alpha=0.6)
    for x in (0.5, 1.0, 2.0, -0.5, -1.0, -2.0):  # constant-reactance arcs
        c, rad = 1.0, 1 / abs(x)
        t = np.linspace(0, 2 * np.pi, 400)
        xc, yc = 1 + rad * np.cos(t), (1 / x) + rad * np.sin(t)
        m = xc**2 + yc**2 <= 1.001
        ax.plot(xc[m], yc[m], color=style.COLORS["muted"], lw=0.5, alpha=0.6)
    ax.axhline(0, color=style.COLORS["muted"], lw=0.5, alpha=0.6)


def view3_reflection_smith() -> dict:
    A = np.linspace(0.0, M.A_CAP, 300)
    G = M.gamma_of_A(A)  # real, runs 0 -> -1 as A: 0 -> 1

    # the electron operating point: |Gamma|^2 = 1 - alpha
    g_elec = np.sqrt(M.gamma_mag_sq_leak())  # |Gamma| = sqrt(1-alpha)
    elec_pt = -g_elec  # phase ~180deg (short)

    fig, axes = plt.subplots(1, 2, figsize=(12, 5.6))

    ax = axes[0]
    _draw_smith(ax)
    ax.plot(G.real, G.imag, "-", color=style.COLORS["ave"], lw=2.5, label=r"$\Gamma(A_0)$ locus, matched→short")
    ax.plot([0], [0], "o", color=style.COLORS["accent"], ms=8, label=r"$A_0{=}0$: $\Gamma{=}0$ (free photon, matched)")
    ax.plot([elec_pt], [0], "*", color=style.COLORS["comparison"], ms=18,
            label=fr"electron wall: $|\Gamma|^2{{=}}1{{-}}\alpha={1-ALPHA:.4f}$")
    ax.annotate("the gap to |Γ|=1\nIS α (the leak)", xy=(elec_pt, 0), xytext=(-0.55, 0.45),
                fontsize=7, color=style.COLORS["comparison"],
                arrowprops=dict(arrowstyle="->", color=style.COLORS["comparison"]))
    ax.set_aspect("equal")
    ax.set_xlim(-1.15, 1.15)
    ax.set_ylim(-1.15, 1.15)
    ax.set_xlabel(style.axis_label(r"Re$(\Gamma)$", r"\mathrm{Re}(\Gamma)", ""))
    ax.set_ylabel(style.axis_label(r"Im$(\Gamma)$", r"\mathrm{Im}(\Gamma)", ""))
    style.legend(ax, fontsize=7, where="below")

    # chiral 2x2 S asymmetry (the winding handedness, parity-odd)
    ax = axes[1]
    A0 = 0.0
    w0 = M.omega_local(A0)
    w = np.linspace(0.2 * w0, 1.8 * w0, 600)
    Hc = M.ELECTRON.H_chiral(1j * w, A0=A0)  # electron instance binds its own Q
    S_LR = Hc[0, 1]
    S_RL = Hc[1, 0]
    nonrecip = np.abs(S_LR - np.conjugate(S_RL))  # parity-odd signature; 0 iff reciprocal
    ax.plot(w / w0, np.abs(S_LR), "-", color=style.COLORS["ave"], lw=1.5, label=r"$|S_{LR}|$")
    ax.plot(w / w0, np.abs(S_RL), "--", color=style.COLORS["comparison"], lw=1.5, label=r"$|S_{RL}|$ (= $|S_{LR}|$)")
    ax.plot(w / w0, nonrecip, "-", color=style.COLORS["accent"], lw=2, label=r"$|S_{LR}-S_{RL}^*|$ (parity-odd)")
    ax.set_xlabel(style.axis_label("Normalized frequency", r"\omega/\omega_C", ""))
    ax.set_ylabel(style.axis_label("Off-diagonal scatter", "|S|", ""))
    ax.text(0.03, 0.74, "STATED / AVE-distinct candidate:\nS_LR ≠ S_RL* = (2,3) winding handedness.\n"
            "Magnitude χ needs chiral-crystal engine\n(cubic FDTD averages chirality out, FLAG-4)",
            fontsize=6.3, transform=ax.transAxes,
            bbox=dict(boxstyle="round", fc="white", ec=style.COLORS["muted"], alpha=0.85))
    style.legend(ax, fontsize=8, where="below")
    ax.grid(alpha=0.3)

    style.save(fig, OUT / "fig3_reflection_smith.png", formats=("png",))
    plt.close(fig)

    return {
        "gamma_mag_sq_leak_1_minus_alpha": float(M.gamma_mag_sq_leak()),
        "gamma_mag_electron": float(g_elec),
        "nonreciprocity_peak": float(np.max(nonrecip)),
    }


# ===========================================================================
# View 4 — Phasor / reactance: V_inc/V_ref + C<->L Lissajous breather
# ===========================================================================
def view4_phasor_reactance() -> dict:
    A0 = 0.0
    w0 = M.omega_local(A0)
    t = np.linspace(0, 4 * np.pi / w0, 1000)
    # incident/reflected at the near-matched cold point and near the wall
    fig, axes = plt.subplots(1, 2, figsize=(12, 5.4))

    ax = axes[0]
    for A0v, col, lab in [(0.0, style.COLORS["accent"], "A₀=0 (matched, |Γ|≈0)"),
                          (0.95, style.COLORS["comparison"], "A₀=0.95 (near wall, |Γ|→1)")]:
        G = float(M.gamma_of_A(np.array(A0v)))
        Vinc = np.cos(w0 * t)
        Vref = G * np.cos(w0 * t + np.pi)  # phase-inverted on reflection (Γ<0)
        E = Vinc + Vref
        B = (Vinc - Vref)  # /Z, normalized
        ax.plot(E, B, "-", color=col, lw=1.5, label=lab)
    ax.set_xlabel(style.axis_label("E-field", r"E \sim (V_{inc}+V_{ref})", ""))
    ax.set_ylabel(style.axis_label("B-field", r"B \sim (V_{inc}-V_{ref})", ""))
    ax.set_aspect("equal")
    style.legend(ax, fontsize=8, where="below")
    ax.grid(alpha=0.3)

    # C<->L Lissajous breather: capacitive vs inductive energy trade
    ax = axes[1]
    Ec = np.cos(w0 * t) ** 2  # capacitive energy ~ V^2
    El = np.sin(w0 * t) ** 2  # inductive energy ~ I^2 (90deg out of phase)
    ax.plot(Ec, El, "-", color=style.COLORS["ave"], lw=1.5)
    ax.plot(Ec[::80], El[::80], ".", color=style.COLORS["ave"], ms=4)
    ax.set_xlabel(style.axis_label("Capacitive energy (E-sector)", r"E_C \propto V^2", ""))
    ax.set_ylabel(style.axis_label("Inductive energy (B-sector)", r"E_L \propto I^2", ""))
    ax.text(0.5, 0.5, "Virial: ⟨E_C⟩=⟨E_L⟩=½m_ec²\n(resonant-lc-solitons.md:23)",
            fontsize=7, ha="center", transform=ax.transAxes,
            bbox=dict(boxstyle="round", fc="white", ec=style.COLORS["muted"], alpha=0.85))
    ax.set_aspect("equal")
    ax.grid(alpha=0.3)

    style.save(fig, OUT / "fig4_phasor_reactance.png", formats=("png",))
    plt.close(fig)

    return {"phasor_quadrature": "E~(Vinc+Vref), B~(Vinc-Vref)/Z", "breather": "C<->L virial-balanced"}


# ===========================================================================
# View 5 — Stability / eigenmode: root-locus + Nyquist (the eigenmode loop)
# ===========================================================================
def view5_stability_eigenmode() -> dict:
    A0 = 0.0
    w0 = M.omega_local(A0)
    fig, axes = plt.subplots(1, 2, figsize=(12, 5.4))

    # root-locus as Q sweeps from low (lossy) to 1/alpha (electron): poles migrate
    # toward the jω axis (the high-Q confined eigenmode)
    ax = axes[0]
    Qs = np.linspace(2.0, M.Q_TANK, 60)
    res, ims = [], []
    for Q in Qs:
        p, _ = M.poles(A0=A0, Q=Q)
        res.append(p.real / w0)
        ims.append(p.imag / w0)
    sc = ax.scatter(res, ims, c=Qs, cmap=style.CMAP_SEQ, s=18)
    ax.axvline(0, color=style.COLORS["data"], lw=0.5)
    ax.set_xlabel(style.axis_label(r"Re$(s)$", r"\mathrm{Re}(s)/\omega_0", ""))
    ax.set_ylabel(style.axis_label(r"Im$(s)$", r"\mathrm{Im}(s)/\omega_0", ""))
    ax.text(0.03, 0.10, "high-Q boundary = the electron eigenmode\n(matched-resonance genesis,\nNOT spontaneous nucleation)",
            fontsize=6.5, transform=ax.transAxes,
            bbox=dict(boxstyle="round", fc="white", ec=style.COLORS["muted"], alpha=0.85))
    plt.colorbar(sc, ax=ax, label=style.axis_label("Quality factor", r"Q \to 1/\alpha", ""))
    ax.grid(alpha=0.3)

    # Nyquist of the open-loop resonator
    ax = axes[1]
    w = np.concatenate([-np.logspace(np.log10(3 * w0), np.log10(0.3 * w0), 800),
                        np.logspace(np.log10(0.3 * w0), np.log10(3 * w0), 800)])
    H = M.ELECTRON.H_scalar(1j * w, A0=A0)  # electron instance binds its own Q
    ax.plot(H.real, H.imag, "-", color=style.COLORS["ave"], lw=1.2)
    ax.plot([-1], [0], "x", color=style.COLORS["comparison"], ms=10, label="−1 point")
    ax.set_xlabel(style.axis_label(r"Re$H(j\omega)$", r"\mathrm{Re}\,H(j\omega)", ""))
    ax.set_ylabel(style.axis_label(r"Im$H(j\omega)$", r"\mathrm{Im}\,H(j\omega)", ""))
    style.legend(ax, fontsize=8, where="below")
    ax.grid(alpha=0.3)
    ax.set_aspect("equal")

    style.save(fig, OUT / "fig5_stability_eigenmode.png", formats=("png",))
    plt.close(fig)

    return {"Q_max": float(M.Q_TANK), "locus": "poles approach jω axis as Q→1/α"}


# ===========================================================================
# View 6 — Parameter basin: bias x amplitude -> region of attraction
# ===========================================================================
def view6_parameter_basin() -> dict:
    A0 = np.linspace(0.0, M.A_CAP, 200)
    # "confinement depth" proxy: |Gamma(A0)| — how reflective the wall is at each bias
    G = np.abs(M.gamma_of_A(A0))
    drive = np.linspace(0.0, 1.0, 200)
    AA, DD = np.meshgrid(A0, drive)
    # basin proxy: a state is "confined" when |Gamma| exceeds the drive that would
    # un-trap it (illustrative region-of-attraction map; structural, not dynamical)
    GG = np.abs(M.gamma_of_A(AA))
    confined = (GG > DD).astype(float)

    fig, ax = plt.subplots(figsize=(7.5, 6))
    # Okabe-Ito-derived 2-colour categorical (retires colourblind-hostile RdYlGn):
    # muted gray = un-trapped, AVE blue = confined. Binary field, so a 2-entry
    # ListedColormap reads cleanly and prints to distinct greys.
    basin_cmap = ListedColormap([style.COLORS["muted"], style.COLORS["ave"]])
    im = ax.pcolormesh(AA, DD, confined, cmap=basin_cmap, shading="auto", vmin=0, vmax=1)
    ax.plot(A0, G, "-", color=style.COLORS["data"], lw=2, label=r"$|\Gamma(A_0)|$ wall edge")
    ax.set_xlabel(style.axis_label("Operating-point bias", "A_0", ""))
    ax.set_ylabel(style.axis_label("Normalized drive", "d", ""))
    ax.text(0.03, 0.90, "STRUCTURAL region-of-attraction proxy\n(not a dynamical basin; substrate-native-check CP8)",
            fontsize=6.5, transform=ax.transAxes,
            bbox=dict(boxstyle="round", fc="white", ec=style.COLORS["muted"], alpha=0.85))
    style.legend(ax, fontsize=8, where="below")
    cbar = fig.colorbar(im, ax=ax, ticks=[0.25, 0.75])
    cbar.set_ticklabels(["un-trapped", "confined"])
    cbar.set_label(style.axis_label("Region of attraction", "", ""))
    style.save(fig, OUT / "fig6_parameter_basin.png", formats=("png",))
    plt.close(fig)
    return {"basin": "structural region-of-attraction proxy (|Gamma|>drive)"}


def main() -> None:
    consts = M.verify_constants()
    metrics = {
        "_canonical_constants": consts,
        "_alpha": ALPHA,
        "_alpha_inv": ALPHA_INV,
        "view1_dc_operating_point": view1_dc_operating_point(),
        "view2_transfer_function": view2_transfer_function(),
        "view3_reflection_smith": view3_reflection_smith(),
        "view4_phasor_reactance": view4_phasor_reactance(),
        "view5_stability_eigenmode": view5_stability_eigenmode(),
        "view6_parameter_basin": view6_parameter_basin(),
    }
    (OUT / "cvr_ee_sweep_metrics.json").write_text(json.dumps(metrics, indent=2))
    print(json.dumps(metrics, indent=2))
    print(f"\n[OK] 6 figures + metrics written to {OUT}")


if __name__ == "__main__":
    main()
