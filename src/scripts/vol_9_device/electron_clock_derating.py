"""
Electron DEVICE datasheet — Curve (b): internal-clock derating vs translation.

AVE picture: the soliton's internal clock is a transverse shear-wave bouncing in
the medium, whose speed is the CONSTANT lattice shear speed c (de-broglie:245,
"c_S ≡ c"; photons ARE transverse waves, Axiom 1). When the soliton translates at
v, the wave must cover a diagonal path at the SAME constant c, so the internal
rate derates.

We DERIVE f(v)/f0 GEOMETRICALLY (solve the constant-c diagonal-path timing, not
assume the closed form) and PLOT it against the exact gamma^-1 = sqrt(1 - v^2/c^2).

Forward-registration (ave-evidence-framing-discipline): the script states up front
whether the two are identical or differ. They are IDENTICAL-BY-CONSTRUCTION — the
constant-c transverse-wave clock IS the kinematic time-dilation geometry. This is
NOT presented as an independent "match to relativity"; it is the same construction.

ave-canonical-source: no fitted constants; c is set to 1 (lattice-natural shear
speed). Consistency/identity-class, not emergence.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

OUT = Path(__file__).parent / "_output"
OUT.mkdir(exist_ok=True)

C = 1.0  # lattice-natural transverse shear speed (de-broglie:245 c_S ≡ c)
L = 1.0  # transverse reflector separation (sets t0 = 2L/c; cancels in f/f0)


def derate_geometric(beta: float) -> float:
    """f(v)/f0 from the constant-c diagonal-path timing, solved GEOMETRICALLY.

    Rest-frame half-tick: c * (t0/2) = L.
    Lab frame (clock moving v=beta*c): in half-tick dt/2 the clock moves v*dt/2,
    the wave covers the hypotenuse sqrt(L^2 + (v*dt/2)^2) at speed c:
        c*(dt/2) = sqrt(L^2 + (v*dt/2)^2)
    Solve the quadratic for dt (the geometric derivation), then f/f0 = t0/dt.
    """
    v = beta * C
    t0 = 2.0 * L / C  # rest-frame period
    # (c^2 - v^2) * dt^2 / 4 = L^2  ->  dt = 2L / sqrt(c^2 - v^2)
    a = (C**2 - v**2) / 4.0
    dt = np.sqrt(L**2 / a)  # positive root, solved from the geometry
    return t0 / dt


def main() -> dict:
    betas = np.linspace(0.0, 0.999, 400)
    f_geom = np.array([derate_geometric(b) for b in betas])
    f_exact = np.sqrt(1.0 - betas**2)  # gamma^-1 (kinematic)
    resid = np.abs(f_geom - f_exact)
    max_resid = float(resid.max())
    identical = max_resid < 1e-12

    verdict = (
        "IDENTICAL-BY-CONSTRUCTION" if identical else f"DIFFER (max resid {max_resid:.2e})"
    )
    print(f"[clock] geometric constant-c derivation vs exact γ⁻¹: {verdict}")
    print(f"[clock] max |f_geom - γ⁻¹| = {max_resid:.3e} over β∈[0,0.999]")
    print("[clock] the constant-c transverse-wave clock IS the kinematic γ⁻¹ —")
    print("[clock] NOT an independent confirmation of relativity; the same geometry.")

    fig, ax = plt.subplots(1, 2, figsize=(12.0, 4.8))
    ax[0].plot(betas, f_exact, color="gray", lw=6, alpha=0.5, label="exact γ⁻¹ = √(1−β²)")
    ax[0].plot(betas, f_geom, color="C3", lw=1.6, ls="--", label="derived (constant-c geometry)")
    ax[0].set_xlabel("β = v/c")
    ax[0].set_ylabel("internal rate  f(v)/f₀")
    ax[0].set_title(
        "Clock derating — constant-c shear-clock\n"
        f"{verdict} (curves overlie)"
    )
    ax[0].legend(fontsize=9)
    ax[0].grid(alpha=0.2)

    ax[1].semilogy(betas, np.maximum(resid, 1e-18), color="C0", lw=1.5)
    ax[1].set_xlabel("β = v/c")
    ax[1].set_ylabel("|f_geom − γ⁻¹|")
    ax[1].set_title(
        f"residual (derived − exact)\nmax = {max_resid:.2e} → identical-by-construction"
    )
    ax[1].grid(alpha=0.2)
    fig.tight_layout()
    p = OUT / "electron_clock_derating.png"
    fig.savefig(p, dpi=120)
    plt.close(fig)

    res = {
        "max_residual": max_resid,
        "identical_by_construction": bool(identical),
        "verdict": verdict,
        "figure": p.name,
    }
    print(f"[clock] figure -> {p}")
    return res


if __name__ == "__main__":
    main()
