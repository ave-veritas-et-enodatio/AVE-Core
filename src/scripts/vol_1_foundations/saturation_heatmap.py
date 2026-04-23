"""
Phase III Prereq 3 — Saturation heatmap diagnostic.

Given a `CoupledK4Cosserat` state, render a side-by-side visualization
of:
    A²_K4(r)         — scalar saturation from photon field V
    A²_Cosserat(r)   — rotational saturation from strain + curvature
    A²_total(r)      — sum; at-Γ=−1 when A² = 1 (TIR threshold)

Key for Phase III-B (photon-photon collision → pair creation):
when two photons collide, A²_total should locally exceed Regime II
boundaries and trigger Cosserat response. This diagnostic makes that
visible.

The three regime thresholds from constants.py / Vol 4 Ch 1:
    √(2α) ≈ 0.121  — Regime I → II passband boundary
    √3/2  ≈ 0.866  — Regime II → III transition boundary
    1.0             — Rupture / TIR limit (Axiom 4)
"""
from __future__ import annotations

from typing import Optional

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors

from ave.core.constants import V_SNAP as _V_SNAP_CONST
from ave.topological.k4_cosserat_coupling import (
    CoupledK4Cosserat,
    _v_squared_per_site,
    _cosserat_A_squared,
)


# Regime thresholds (Axiom-4, Regime I/II/III from Vol 4 Ch 1)
ALPHA = 1.0 / 137.036
A2_REGIME_I_II = 2.0 * ALPHA          # ≈ 0.0146   (√(2α) in A, but A² here)
A2_REGIME_II_III = 3.0 / 4.0          # = 0.75     ((√3/2)² = 3/4)
A2_RUPTURE = 1.0                      # rupture limit


def saturation_fields(sim: CoupledK4Cosserat) -> dict:
    """Return (A²_K4, A²_Cosserat, A²_total) full 3D fields."""
    V_sq = _v_squared_per_site(sim.k4.V_inc)
    A_sq_k4 = V_sq / (sim.V_SNAP ** 2)
    A_sq_cos = _cosserat_A_squared(
        sim.cos.u, sim.cos.omega, sim.cos.dx,
        sim.cos.omega_yield, sim.cos.epsilon_yield,
    )
    A_sq_total = A_sq_k4 + A_sq_cos
    return {
        "A_sq_k4": A_sq_k4,
        "A_sq_cos": A_sq_cos,
        "A_sq_total": A_sq_total,
    }


def render_heatmap(
    sim: CoupledK4Cosserat,
    out_path: str = "/tmp/saturation_heatmap.png",
    z_slice: Optional[int] = None,
    title_suffix: str = "",
) -> dict:
    """Render a 3-panel heatmap of the saturation fields at a z-slice.

    Returns the fields dict (same as `saturation_fields`).
    """
    fields = saturation_fields(sim)
    if z_slice is None:
        z_slice = sim.N // 2

    fig, axes = plt.subplots(1, 3, figsize=(14, 5))
    fig.patch.set_facecolor("#111")
    for ax in axes:
        ax.set_facecolor("#1a1a1a")
        ax.tick_params(colors="#ccc")
        for spine in ax.spines.values():
            spine.set_edgecolor("#666")

    panels = [
        ("A²_K4   (photon, from V²)", fields["A_sq_k4"][:, :, z_slice], "inferno"),
        ("A²_Cos (rotational, from ε²+κ²)", fields["A_sq_cos"][:, :, z_slice], "viridis"),
        ("A²_total (= sum; TIR when → 1)", fields["A_sq_total"][:, :, z_slice], "magma"),
    ]

    vmax = max(p[1].max() for p in panels) * 1.05
    vmax = max(vmax, 0.02)  # at least show thresholds
    for ax, (title, data, cmap) in zip(axes, panels):
        im = ax.imshow(data.T, origin="lower", cmap=cmap, vmin=0.0, vmax=vmax)
        ax.set_title(title, color="#eee", fontsize=10)
        ax.set_xlabel("x (cells)", color="#ccc")
        ax.set_ylabel("y (cells)", color="#ccc")
        cbar = plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
        cbar.ax.tick_params(colors="#ccc")
        # Mark regime boundaries as horizontal lines on the colorbar
        for thr, col, lbl in [
            (A2_REGIME_I_II, "yellow", "√(2α)=Rg I/II"),
            (A2_REGIME_II_III, "orange", "√3/2=Rg II/III"),
            (A2_RUPTURE, "red", "A²=1 TIR"),
        ]:
            if thr <= vmax:
                cbar.ax.axhline(thr, color=col, lw=1.2)

    regime_report = _regime_summary(fields, sim.k4.mask_active)
    fig.suptitle(
        f"Saturation regimes, t = {sim.time:.3f}  {title_suffix}\n"
        f"Regime-III (A²>3/4): {regime_report['cells_rg_III']:d} cells   "
        f"Rupture (A²>1): {regime_report['cells_rupture']:d} cells   "
        f"max A²_total = {regime_report['max_A_sq_total']:.3f}",
        color="#eee", fontsize=11,
    )
    plt.tight_layout()
    plt.savefig(out_path, dpi=110, facecolor="#111")
    plt.close()
    fields["regime_report"] = regime_report
    return fields


def _regime_summary(fields: dict, mask_active: np.ndarray) -> dict:
    """Count cells in each regime and report max values."""
    A2 = fields["A_sq_total"]
    active = mask_active
    return {
        "cells_rg_I": int(np.sum(active & (A2 < A2_REGIME_I_II))),
        "cells_rg_II": int(np.sum(active & (A2 >= A2_REGIME_I_II) & (A2 < A2_REGIME_II_III))),
        "cells_rg_III": int(np.sum(active & (A2 >= A2_REGIME_II_III) & (A2 < A2_RUPTURE))),
        "cells_rupture": int(np.sum(active & (A2 >= A2_RUPTURE))),
        "max_A_sq_total": float(A2[active].max()) if active.any() else 0.0,
        "max_A_sq_k4": float(fields["A_sq_k4"][active].max()) if active.any() else 0.0,
        "max_A_sq_cos": float(fields["A_sq_cos"][active].max()) if active.any() else 0.0,
    }


if __name__ == "__main__":
    # Quick self-test: empty sim → all zeros
    sim = CoupledK4Cosserat(N=32, pml=4)
    fields = render_heatmap(sim, out_path="/tmp/saturation_heatmap_test.png",
                            title_suffix="(empty sim)")
    print(f"Empty sim regime report: {fields['regime_report']}")
    print(f"Saved /tmp/saturation_heatmap_test.png")
