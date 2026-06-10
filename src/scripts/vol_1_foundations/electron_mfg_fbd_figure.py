#!/usr/bin/env python3
"""
Free-body-diagram schematic for the electron-manufacturing process-flow doc (§3).

Renders a wedge of the locked annulus with the four force/stress contributions
labeled with DATA-DERIVED values (rho_cav and the pocket pressure deficit are
computed from the canonical candidate EOS in this run, not hard-coded), plus a
right panel showing R/r as a FUNCTION of the chosen outer-wall density under the
v=const closure -- the §4 UNDERDETERMINED result made visual (phi^2 is a single
point on a continuous curve, reached only at a non-canonical rho_wall).

Canonical-source: PHI (constants.py:199), Golden-Torus radii (constants.py:200-201).
Output: research/figures/electron_mfg_fbd.png
"""
import os
import sys

import numpy as np

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Wedge

_REPO_SRC = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
for _p in (os.path.join(_REPO_SRC, "src"), _REPO_SRC):
    if os.path.isdir(os.path.join(_p, "ave")) and _p not in sys.path:
        sys.path.insert(0, _p)

from ave.core.constants import PHI, R_GOLDEN_TORUS, R_GOLDEN_TORUS_MINOR

PHI2 = R_GOLDEN_TORUS / R_GOLDEN_TORUS_MINOR


def c_eff_sq(rho):
    return 1.0 + rho / (1.0 - rho**2)


def pressure_excess_over_rho0c0sq(rho):
    """P(rho)-P0 = integral_0^rho (1 + s/(1-s^2)) ds = rho - 0.5 ln(1-rho^2)."""
    return rho - 0.5 * np.log(1.0 - rho**2)


def G_const_v(rho):
    return -0.25 * np.log(1.0 - rho) + 1.25 * np.log(1.0 + rho) + 0.5 / (1.0 + rho)


def main():
    # data-derived labels
    rho_cav = float(min(np.roots([1.0, -1.0, -1.0])))  # -1/phi
    dP_pocket = -pressure_excess_over_rho0c0sq(rho_cav)  # deficit P0 - P(rho_cav) > 0

    fig = plt.figure(figsize=(13, 6.2))

    # ---------------- LEFT: the FBD wedge ----------------
    ax = fig.add_subplot(1, 2, 1)
    ax.set_aplot = None
    ax.set_aspect("equal")
    ax.axis("off")
    r_in, r_out = 1.0, 2.0
    th0, th1 = 30.0, 60.0  # wedge angular span (deg)

    # annulus wedge
    w = Wedge((0, 0), r_out, th0, th1, width=r_out - r_in,
              facecolor="#cfe3f7", edgecolor="#1f4e79", lw=1.8, zorder=1)
    ax.add_patch(w)
    # inner cavity (the rarefied pocket)
    cav = Wedge((0, 0), r_in, th0, th1, facecolor="#f7e0e0", edgecolor="#a33",
                lw=1.2, ls="--", zorder=0)
    ax.add_patch(cav)

    thm = np.radians((th0 + th1) / 2.0)
    rm = (r_in + r_out) / 2.0

    def arrow(r1, a1, r2, a2, color, lw=2.2):
        p1 = (r1 * np.cos(a1), r1 * np.sin(a1))
        p2 = (r2 * np.cos(a2), r2 * np.sin(a2))
        ax.add_patch(FancyArrowPatch(p1, p2, arrowstyle="-|>", mutation_scale=16,
                                     color=color, lw=lw, zorder=5))

    # 1. pocket pressure OUT at r_inner (rarefied -> net inward ambient; shown as
    #    the pocket's outward push, weaker than ambient = a DEFICIT)
    arrow(r_in, thm, r_in + 0.42, thm, "#a33")
    ax.text((r_in + 0.5) * np.cos(thm) + 0.05, (r_in + 0.5) * np.sin(thm),
            r"$P_{\rm pocket}$ (rarefied)" + "\n" + r"$\bar\rho=\bar\rho_{cav}$",
            color="#a33", fontsize=9, ha="left", va="center")
    # 2. saturation-wall reaction IN at r_outer
    arrow(r_out + 0.42, thm, r_out, thm, "#1f4e79")
    ax.text((r_out + 0.5) * np.cos(thm), (r_out + 0.5) * np.sin(thm) + 0.06,
            r"$P_{\rm wall}$ ($\Gamma=-1$ sat.)", color="#1f4e79", fontsize=9,
            ha="left", va="bottom")
    # 3. hoop tension (circumferential, both edges) -> net inward
    for aedge in (np.radians(th0), np.radians(th1)):
        tang = aedge + (np.pi / 2 if aedge < thm else -np.pi / 2)
        p = (rm * np.cos(aedge), rm * np.sin(aedge))
        ax.add_patch(FancyArrowPatch(
            p, (p[0] + 0.33 * np.cos(tang), p[1] + 0.33 * np.sin(tang)),
            arrowstyle="-|>", mutation_scale=12, color="#2e7d32", lw=2.0, zorder=6))
    ax.text(rm * np.cos(thm) - 0.15, rm * np.sin(thm) - 0.02, r"$T_{\rm hoop}$",
            color="#2e7d32", fontsize=9, ha="center")
    # 4. centrifugal load OUT at centroid
    arrow(rm, thm - 0.12, rm + 0.3, thm - 0.12, "#e08a00")
    ax.text((rm + 0.35) * np.cos(thm - 0.16), (rm + 0.35) * np.sin(thm - 0.16) - 0.18,
            r"$\rho\,v_\theta^2/r$" + "\n(centrifugal)", color="#e08a00",
            fontsize=8.5, ha="center", va="top")

    # radii labels
    ax.annotate("", xy=(r_in * np.cos(np.radians(th0 - 6)), r_in * np.sin(np.radians(th0 - 6))),
                xytext=(0, 0), arrowprops=dict(arrowstyle="-", color="gray", lw=0.8))
    ax.annotate("", xy=(r_out * np.cos(np.radians(th0 - 6)), r_out * np.sin(np.radians(th0 - 6))),
                xytext=(0, 0), arrowprops=dict(arrowstyle="-", color="gray", lw=0.8))
    ax.text(0.62 * np.cos(np.radians(th0 - 9)), 0.62 * np.sin(np.radians(th0 - 9)),
            r"$r$", fontsize=11, color="gray")
    ax.text(1.55 * np.cos(np.radians(th0 - 9)), 1.55 * np.sin(np.radians(th0 - 9)),
            r"$R$", fontsize=11, color="gray")

    ax.set_xlim(-0.15, 3.1)
    ax.set_ylim(-0.1, 2.3)
    ax.set_title("FBD: wedge of the locked annulus (real-space $O_1$ ring)",
                 fontsize=11)
    ax.text(0.0, 2.18,
            r"$\bar\rho_{cav}=-1/\varphi=%.4f$  |  pocket deficit $=%.3f\,\rho_0 c_0^2$"
            % (rho_cav, dP_pocket), fontsize=9, color="#333")

    # ---------------- RIGHT: R/r vs outer-wall density (the UNDERDETERMINED curve)
    ax2 = fig.add_subplot(1, 2, 2)
    rho_wall = np.linspace(0.0, 0.85, 400)
    rr = np.exp(G_const_v(rho_wall) - G_const_v(rho_cav))
    ax2.plot(rho_wall, rr, color="#1f4e79", lw=2.2,
             label=r"$R/r$ (forward, $v_\theta=c_0$ closure)")
    ax2.axhline(PHI2, color="#a33", ls="--", lw=1.5, label=r"$\varphi^2=%.4f$" % PHI2)
    # the non-canonical fit point -- back-solved on a dense grid (1e-6 spacing) so the
    # annotation deterministically matches the rr_balance JSON (rho_wall ~= 0.4401),
    # not a coarse 400-point-grid rounding artifact
    _rho_dense = np.linspace(0.30, 0.55, 250001)
    _rr_dense = np.exp(G_const_v(_rho_dense) - G_const_v(rho_cav))
    rho_fit = _rho_dense[np.argmin(np.abs(_rr_dense - PHI2))]
    ax2.plot([rho_fit], [PHI2], "o", color="#a33", ms=8, zorder=6)
    ax2.annotate(r"forced match needs $\bar\rho_{wall}\approx%.3f$" % rho_fit
                 + "\n(NON-canonical $\\Rightarrow$ FITTED)",
                 xy=(rho_fit, PHI2), xytext=(rho_fit + 0.04, PHI2 - 0.9),
                 fontsize=8.5, color="#a33",
                 arrowprops=dict(arrowstyle="->", color="#a33", lw=1.0))
    # canonical landmark walls
    for val, name in [(1.0 / PHI, r"$+1/\varphi$"), (1.0 / PHI**2, r"$+1/\varphi^2$"),
                      (0.5, r"$+0.5$")]:
        y = np.exp(G_const_v(val) - G_const_v(rho_cav))
        ax2.plot([val], [y], "s", color="#2e7d32", ms=6)
        ax2.annotate(name, xy=(val, y), xytext=(val - 0.02, y + 0.12), fontsize=8.5,
                     color="#2e7d32", ha="center")
    ax2.set_xlabel(r"outer saturation-wall density $\bar\rho_{wall}$ (the missing 2nd BC)")
    ax2.set_ylabel(r"equilibrium $R/r$")
    ax2.set_title(r"§4: $R/r$ is a CURVE, not a point $\Rightarrow$ UNDERDETERMINED",
                  fontsize=11)
    ax2.set_ylim(1.5, 4.2)
    ax2.legend(fontsize=8.5, loc="upper left")
    ax2.grid(alpha=0.3)

    fig.suptitle("Electron-manufacturing FBD (§3-§4): forward radial balance vs the Golden-Torus $\\varphi^2$",
                 fontsize=12, y=0.99)
    fig.tight_layout(rect=[0, 0, 1, 0.96])

    outdir = os.path.join(_REPO_SRC, "research", "figures")
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "electron_mfg_fbd.png")
    fig.savefig(path, dpi=130)
    print("wrote", path)
    print("rho_cav=%.6f  pocket_deficit=%.4f rho0c0^2  phi2=%.6f  fit_wall=%.4f"
          % (rho_cav, dP_pocket, PHI2, rho_fit))


if __name__ == "__main__":
    main()
