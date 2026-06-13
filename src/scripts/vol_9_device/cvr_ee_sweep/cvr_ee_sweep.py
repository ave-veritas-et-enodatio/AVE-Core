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

from ave.core.constants import ALPHA  # noqa: E402

# cvr_model lives beside this driver
sys.path.insert(0, str(Path(__file__).resolve().parent))
import cvr_model as M  # noqa: E402

OUT = Path(__file__).parent / "_output"
OUT.mkdir(exist_ok=True)

ALPHA_INV = 1.0 / ALPHA


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
    fig.suptitle("CVR View 1 — DC Operating Point: the vacuum varactor C-V characteristic", fontsize=12)

    ax = axes[0, 0]
    ax.plot(A, Ceff, "b-", lw=2, label=r"$C_{eff}/C_0 = 1/S(A_0)$")
    ax.axvline(M.A_CAP, color="grey", ls=":", lw=1)
    ax.text(M.A_CAP, 2, " A_CAP\n(apparatus clip)", fontsize=7, color="grey", va="bottom")
    ax.set_yscale("log")
    ax.set_xlabel(r"operating point $A_0 = |V|/V_{yield}$")
    ax.set_ylabel(r"$C_{eff}/C_0$")
    ax.set_title("Vacuum varactor (diverges as A→1)", fontsize=10)
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    ax = axes[0, 1]
    ax.plot(A, Zc, "r-", lw=2, label=r"$Z_{core}/Z_0 = \sqrt{S(A_0)}$")
    ax.axhline(0, color="k", lw=0.5)
    ax.set_xlabel(r"operating point $A_0$")
    ax.set_ylabel(r"$Z_{core}/Z_0$")
    ax.set_title("Magnetic-branch impedance → 0 (Γ=−1 wall)", fontsize=10)
    ax.text(0.05, 0.5, "magnetic μ_eff→0 (PRIMARY, clm-lv3uw1)\n≡ capacitive C_eff→∞ trajectory\n(sector-attribution FLAG-2)",
            fontsize=6.5, transform=ax.transAxes, va="center",
            bbox=dict(boxstyle="round", fc="wheat", alpha=0.6))
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    ax = axes[1, 0]
    ax.plot(A, cEM, "m-", lw=2, label=r"$c_{EM}/c_0 = 1/S$  (Maxwell, →∞)")
    ax.plot(A, cSh, "g-", lw=2, label=r"$c_{shear}/c_0 = \sqrt{S}$  (mechanical, →0)")
    ax.set_yscale("log")
    ax.set_xlabel(r"operating point $A_0$")
    ax.set_ylabel(r"$c_{eff}/c_0$")
    ax.set_title("Two substrate speeds (INVARIANT-S2; do not conflate)", fontsize=10)
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # exponent-defect panel: n_engine = S^0.25 vs n_physical = S^0.5
    ax = axes[1, 1]
    ax.plot(A, M.n_physical(A), "k-", lw=2, label=r"$n_{phys}=S^{0.5}$ (corrected)")
    ax.plot(A, M.n_engine(A), "b--", lw=2, label=r"$n_{eng}=S^{0.25}$ (as-coded)")
    ax.fill_between(A, M.n_physical(A), M.n_engine(A), color="orange", alpha=0.25)
    ax.set_xlabel(r"operating point $A_0$")
    ax.set_ylabel(r"refractive index $n$")
    ax.set_title("EXPONENT DEFECT (master_equation_fdtd.py:165)", fontsize=10)
    ax.text(0.04, 0.05, "engine S^0.25 UNDERSTATES wall depth\n(physics-review item; Grant/auditor)",
            fontsize=6.5, transform=ax.transAxes, color="darkorange")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(OUT / "fig1_dc_operating_point.png", dpi=130)
    plt.close(fig)

    return {
        "A_grid_max": float(M.A_CAP),
        "Ceff_over_C0_at_A0.9": float(M.c_eff_capacitance(np.array(0.9))),
        "Zcore_over_Z0_at_A0.9": float(M.z_core(np.array(0.9)) / M.Z_0),
        "n_engine_minus_n_physical_max_gap": float(np.max(M.n_engine(A) - M.n_physical(A))),
    }


# ===========================================================================
# View 2 — AC transfer function (Bode + pole-zero), Q=1/alpha, BW=alpha*w0
# ===========================================================================
def view2_transfer_function() -> dict:
    A0 = 0.0  # cold reference operating point
    w0 = M.omega_local(A0)
    w = np.logspace(np.log10(w0) - 4, np.log10(w0) + 4, 2000)
    H = M.H_scalar(1j * w, A0=A0)
    mag_db = 20 * np.log10(np.abs(H))
    phase = np.degrees(np.angle(H))

    p1, p2 = M.poles(A0=A0)
    BW = w0 / M.Q_TANK  # = alpha*w0

    fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))
    fig.suptitle(r"CVR View 2 — AC Transfer Function $H(s)$: the electron tank, $Q=1/\alpha$", fontsize=12)

    ax = axes[0]
    ax.semilogx(w / w0, mag_db, "b-", lw=1.5)
    ax.axhline(20 * np.log10(M.Q_TANK), color="r", ls="--", lw=1,
               label=fr"peak $=20\log_{{10}}Q={20*np.log10(M.Q_TANK):.1f}$ dB")
    ax.axvline(1.0, color="grey", ls=":", lw=1)
    ax.set_xlabel(r"$\omega/\omega_C$")
    ax.set_ylabel("|H| (dB)")
    ax.set_title(fr"Bode magnitude — $Q=\alpha^{{-1}}={M.Q_TANK:.2f}$", fontsize=10)
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3, which="both")

    ax = axes[1]
    ax.semilogx(w / w0, phase, "g-", lw=1.5)
    ax.axvline(1.0, color="grey", ls=":", lw=1)
    ax.set_xlabel(r"$\omega/\omega_C$")
    ax.set_ylabel("arg H (deg)")
    ax.set_title(fr"Bode phase (BW $=\alpha\omega_C={BW:.2e}$ rad/s)", fontsize=10)
    ax.grid(alpha=0.3, which="both")

    # pole-zero (normalized by w0)
    ax = axes[2]
    ax.plot([p1.real / w0, p2.real / w0], [p1.imag / w0, p2.imag / w0], "rx", ms=12, mew=2,
            label=r"poles $s=-\alpha\omega_0/2 \pm j\omega_d$")
    ax.axvline(0, color="k", lw=0.5)
    ax.axhline(0, color="k", lw=0.5)
    ax.set_xlabel(r"Re$(s)/\omega_0$")
    ax.set_ylabel(r"Im$(s)/\omega_0$")
    ax.set_title(fr"Pole pair — Re$=-\alpha/2={p1.real/w0:.5f}$", fontsize=10)
    ax.text(0.04, 0.5, "distance from jω axis\n= α/2 = the per-cycle leak\n(theorem-3-1-q-factor.md:81)",
            fontsize=6.5, transform=ax.transAxes, va="center",
            bbox=dict(boxstyle="round", fc="lightblue", alpha=0.6))
    ax.legend(fontsize=8, loc="lower left")
    ax.grid(alpha=0.3)
    ax.set_xlim(-0.02, 0.005)

    fig.tight_layout(rect=[0, 0, 1, 0.95])
    fig.savefig(OUT / "fig2_transfer_function_bode.png", dpi=130)
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
    ax.plot(np.cos(th), np.sin(th), "k-", lw=1)
    for r in (0.5, 1.0, 2.0):  # constant-resistance circles
        c, rad = r / (1 + r), 1 / (1 + r)
        ax.plot(c + rad * np.cos(th), rad * np.sin(th), color="grey", lw=0.5, alpha=0.6)
    for x in (0.5, 1.0, 2.0, -0.5, -1.0, -2.0):  # constant-reactance arcs
        c, rad = 1.0, 1 / abs(x)
        t = np.linspace(0, 2 * np.pi, 400)
        xc, yc = 1 + rad * np.cos(t), (1 / x) + rad * np.sin(t)
        m = xc**2 + yc**2 <= 1.001
        ax.plot(xc[m], yc[m], color="grey", lw=0.5, alpha=0.6)
    ax.axhline(0, color="grey", lw=0.5, alpha=0.6)


def view3_reflection_smith() -> dict:
    A = np.linspace(0.0, M.A_CAP, 300)
    G = M.gamma_of_A(A)  # real, runs 0 -> -1 as A: 0 -> 1

    # the electron operating point: |Gamma|^2 = 1 - alpha
    g_elec = np.sqrt(M.gamma_mag_sq_leak())  # |Gamma| = sqrt(1-alpha)
    elec_pt = -g_elec  # phase ~180deg (short)

    fig, axes = plt.subplots(1, 2, figsize=(12, 5.6))
    fig.suptitle(r"CVR View 3 — Reflection on the Smith Chart: $|\Gamma|^2 = 1-\alpha$ (AVE-distinct)", fontsize=12)

    ax = axes[0]
    _draw_smith(ax)
    ax.plot(G.real, G.imag, "b-", lw=2.5, label=r"$\Gamma(A_0)$ locus, matched→short")
    ax.plot([0], [0], "go", ms=8, label=r"$A_0{=}0$: $\Gamma{=}0$ (free photon, matched)")
    ax.plot([elec_pt], [0], "r*", ms=18,
            label=fr"electron wall: $|\Gamma|^2{{=}}1{{-}}\alpha={1-ALPHA:.4f}$")
    ax.annotate("the gap to |Γ|=1\nIS α (the leak)", xy=(elec_pt, 0), xytext=(-0.55, 0.45),
                fontsize=7, arrowprops=dict(arrowstyle="->", color="red"))
    ax.set_aspect("equal")
    ax.set_xlim(-1.15, 1.15)
    ax.set_ylim(-1.15, 1.15)
    ax.set_xlabel(r"Re$(\Gamma)$")
    ax.set_ylabel(r"Im$(\Gamma)$")
    ax.set_title("Electron sits just INSIDE the unit circle", fontsize=10)
    ax.legend(fontsize=7, loc="upper right")

    # chiral 2x2 S asymmetry (the winding handedness, parity-odd)
    ax = axes[1]
    A0 = 0.0
    w0 = M.omega_local(A0)
    w = np.linspace(0.2 * w0, 1.8 * w0, 600)
    Hc = M.H_chiral(1j * w, A0=A0)
    S_LR = Hc[0, 1]
    S_RL = Hc[1, 0]
    nonrecip = np.abs(S_LR - np.conjugate(S_RL))  # parity-odd signature; 0 iff reciprocal
    ax.plot(w / w0, np.abs(S_LR), "b-", lw=1.5, label=r"$|S_{LR}|$")
    ax.plot(w / w0, np.abs(S_RL), "r--", lw=1.5, label=r"$|S_{RL}|$ (= $|S_{LR}|$)")
    ax.plot(w / w0, nonrecip, "m-", lw=2, label=r"$|S_{LR}-S_{RL}^*|$ (parity-odd)")
    ax.set_xlabel(r"$\omega/\omega_C$")
    ax.set_ylabel("off-diagonal scatter")
    ax.set_title("Chiral 2×2 S: non-reciprocal off-diagonal", fontsize=10)
    ax.text(0.03, 0.74, "STATED / AVE-distinct candidate:\nS_LR ≠ S_RL* = (2,3) winding handedness.\n"
            "Magnitude χ needs chiral-crystal engine\n(cubic FDTD averages chirality out, FLAG-4)",
            fontsize=6.3, transform=ax.transAxes,
            bbox=dict(boxstyle="round", fc="lavender", alpha=0.7))
    ax.legend(fontsize=8, loc="upper right")
    ax.grid(alpha=0.3)

    fig.tight_layout(rect=[0, 0, 1, 0.95])
    fig.savefig(OUT / "fig3_reflection_smith.png", dpi=130)
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
    fig.suptitle(r"CVR View 4 — Phasor & Reactance: $E\sim(V_{inc}+V_{ref})$, $B\sim(V_{inc}-V_{ref})/Z$", fontsize=12)

    ax = axes[0]
    for A0v, col, lab in [(0.0, "g", "A₀=0 (matched, |Γ|≈0)"),
                          (0.95, "r", "A₀=0.95 (near wall, |Γ|→1)")]:
        G = float(M.gamma_of_A(np.array(A0v)))
        Vinc = np.cos(w0 * t)
        Vref = G * np.cos(w0 * t + np.pi)  # phase-inverted on reflection (Γ<0)
        E = Vinc + Vref
        B = (Vinc - Vref)  # /Z, normalized
        ax.plot(E, B, col + "-", lw=1.5, label=lab)
    ax.set_xlabel(r"$E \sim (V_{inc}+V_{ref})$")
    ax.set_ylabel(r"$B \sim (V_{inc}-V_{ref})$")
    ax.set_title("I/Q quadrature (photon-ee-mapping.md §4)", fontsize=10)
    ax.set_aspect("equal")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # C<->L Lissajous breather: capacitive vs inductive energy trade
    ax = axes[1]
    Ec = np.cos(w0 * t) ** 2  # capacitive energy ~ V^2
    El = np.sin(w0 * t) ** 2  # inductive energy ~ I^2 (90deg out of phase)
    ax.plot(Ec, El, "b-", lw=1.5)
    ax.plot(Ec[::80], El[::80], "b.", ms=4)
    ax.set_xlabel(r"capacitive energy $\propto V^2$ (E-sector)")
    ax.set_ylabel(r"inductive energy $\propto I^2$ (B-sector)")
    ax.set_title("C↔L breather: lossless reactive cycling", fontsize=10)
    ax.text(0.5, 0.5, "Virial: ⟨E_C⟩=⟨E_L⟩=½m_ec²\n(resonant-lc-solitons.md:23)",
            fontsize=7, ha="center", transform=ax.transAxes,
            bbox=dict(boxstyle="round", fc="lightyellow", alpha=0.7))
    ax.set_aspect("equal")
    ax.grid(alpha=0.3)

    fig.tight_layout(rect=[0, 0, 1, 0.95])
    fig.savefig(OUT / "fig4_phasor_reactance.png", dpi=130)
    plt.close(fig)

    return {"phasor_quadrature": "E~(Vinc+Vref), B~(Vinc-Vref)/Z", "breather": "C<->L virial-balanced"}


# ===========================================================================
# View 5 — Stability / eigenmode: root-locus + Nyquist (the eigenmode loop)
# ===========================================================================
def view5_stability_eigenmode() -> dict:
    A0 = 0.0
    w0 = M.omega_local(A0)
    fig, axes = plt.subplots(1, 2, figsize=(12, 5.4))
    fig.suptitle("CVR View 5 — Stability / Eigenmode: root-locus + Nyquist (genesis in EE form)", fontsize=12)

    # root-locus as Q sweeps from low (lossy) to 1/alpha (electron): poles migrate
    # toward the jω axis (the high-Q confined eigenmode)
    ax = axes[0]
    Qs = np.linspace(2.0, M.Q_TANK, 60)
    res, ims = [], []
    for Q in Qs:
        p, _ = M.poles(A0=A0, Q=Q)
        res.append(p.real / w0)
        ims.append(p.imag / w0)
    sc = ax.scatter(res, ims, c=Qs, cmap="viridis", s=18)
    ax.axvline(0, color="k", lw=0.5)
    ax.set_xlabel(r"Re$(s)/\omega_0$")
    ax.set_ylabel(r"Im$(s)/\omega_0$")
    ax.set_title("Root-locus: Q↑ → pole → jω axis (confinement)", fontsize=10)
    ax.text(0.03, 0.10, "high-Q boundary = the electron eigenmode\n(matched-resonance genesis,\nNOT spontaneous nucleation)",
            fontsize=6.5, transform=ax.transAxes,
            bbox=dict(boxstyle="round", fc="honeydew", alpha=0.7))
    plt.colorbar(sc, ax=ax, label="Q (→ 1/α)")
    ax.grid(alpha=0.3)

    # Nyquist of the open-loop resonator
    ax = axes[1]
    w = np.concatenate([-np.logspace(np.log10(3 * w0), np.log10(0.3 * w0), 800),
                        np.logspace(np.log10(0.3 * w0), np.log10(3 * w0), 800)])
    H = M.H_scalar(1j * w, A0=A0)
    ax.plot(H.real, H.imag, "b-", lw=1.2)
    ax.plot([-1], [0], "rx", ms=10, label="−1 point")
    ax.set_xlabel("Re H(jω)")
    ax.set_ylabel("Im H(jω)")
    ax.set_title("Nyquist locus (the eigenmode loop)", fontsize=10)
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)
    ax.set_aspect("equal")

    fig.tight_layout(rect=[0, 0, 1, 0.95])
    fig.savefig(OUT / "fig5_stability_eigenmode.png", dpi=130)
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
    fig.suptitle("CVR View 6 — Parameter basin: region of attraction (bias × drive)", fontsize=12)
    im = ax.pcolormesh(AA, DD, confined, cmap="RdYlGn", shading="auto", vmin=0, vmax=1)
    ax.plot(A0, G, "k-", lw=2, label=r"$|\Gamma(A_0)|$ wall edge")
    ax.set_xlabel(r"operating-point bias $A_0$")
    ax.set_ylabel("normalized drive")
    ax.set_title("green = confined (|Γ|>drive); red = un-trapped", fontsize=10)
    ax.text(0.03, 0.90, "STRUCTURAL region-of-attraction proxy\n(not a dynamical basin; substrate-native-check CP8)",
            fontsize=6.5, transform=ax.transAxes,
            bbox=dict(boxstyle="round", fc="white", alpha=0.8))
    ax.legend(fontsize=8, loc="lower right")
    fig.colorbar(im, ax=ax, label="confined")
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    fig.savefig(OUT / "fig6_parameter_basin.png", dpi=130)
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
