"""Comparison figure for the Option-D-impose-under-(II)-confinement re-test.

Reads the `_results.npz` trajectories (native / wall_only / wall_sector) and
renders the persistence discriminator: position-independent localization, peak
|ω|, the wall-engagement Γ_min, the reactance pair (C-state |ω| + L-state |ω̇| at
A), and the (2,3) winding c_cos — all vs Compton period, drive-end marked.

This is the evidence panel for the result doc (and, on verdict (I), the
"animation" the prereg calls for is the field montage — see --montage).

Usage:
  python phase5_optionD_under_reflective_confinement_figure.py \
      [results.npz] [out.png]
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = Path(__file__).parent
DEFAULT_NPZ = HERE / "phase5_optionD_under_reflective_confinement_results.npz"
COLORS = {"native": "#c33", "wall_only": "#39c", "wall_sector": "#2a7"}
CONFIGS = ("native", "wall_only", "wall_sector")
WAVELENGTH = 3.5  # Compton period in lattice units (matches the driver default)


def render(npz_path: Path, out_path: Path) -> None:
    d = np.load(npz_path)
    period = WAVELENGTH

    fig, axes = plt.subplots(2, 3, figsize=(16, 9))

    def _t(name):
        return d[f"{name}_t"] / period

    panels = [
        ("loc", "localization (density-peak, PML-excl.)", "the honest 'held anywhere' axis", False),
        ("peak|w|_global", "peak |ω| (global)", "collapse → blowup; held → bounded", True),
        ("g_min", "Γ_min (wall engagement)", "→−1 hard short; ≈0 wall never engaged", False),
        ("E_cos", "E_cos", "parametric pumping check", True),
        ("c_cos_global", "c_cos (the '2' winding)", "(2,3) topological winding", False),
    ]
    for ax, (key, title, sub, logy) in zip(axes.flat, panels):
        for name in CONFIGS:
            k = f"{name}_{key}"
            if k not in d.files:
                continue
            y = d[k]
            if np.all(np.isnan(y)):
                continue
            ax.plot(_t(name), y, color=COLORS[name], lw=1.5, label=name)
        ax.set_title(f"{title}\n{sub}", fontsize=10)
        ax.set_xlabel("Compton periods")
        if logy:
            ax.set_yscale("symlog")
        ax.grid(alpha=0.3)
        ax.legend(fontsize=8)

    # Final panel: the reactance pair at A (C-state |ω| + L-state |ω̇|), wall_sector.
    ax = axes.flat[5]
    name = "wall_sector"
    if f"{name}_|w|_A" in d.files:
        ax.plot(_t(name), d[f"{name}_|w|_A"], color="#2a7", lw=1.5, label="|ω|_A (C-state)")
        ax.plot(_t(name), d[f"{name}_|wdot|_A"], color="#a63", lw=1.2, ls="--", label="|ω̇|_A (L-state)")
    ax.set_title("reactance pair @ A (wall_sector)\nA-Rule 10: C + L both tracked", fontsize=10)
    ax.set_xlabel("Compton periods")
    ax.grid(alpha=0.3)
    ax.legend(fontsize=8)

    fig.suptitle(
        "Option-D (2,3) pair IMPOSE under the (II) moving-Γ=−1 reflective wall — "
        "native vs wall_only vs wall_sector",
        fontsize=13,
    )
    plt.tight_layout()
    plt.savefig(out_path, dpi=120)
    plt.close()
    print(f"Saved {out_path}")


if __name__ == "__main__":
    npz = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_NPZ
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else npz.with_suffix(".png")
    render(npz, out)
