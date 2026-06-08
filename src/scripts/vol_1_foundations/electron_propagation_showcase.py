#!/usr/bin/env python3
r"""Single-purpose electron propagation GIF at sub-yield amp=0.48.

Shows translating defect on native VacuumEngine3D (co-moving longitudinal drive).
Not a full Γ=-1 soliton — honest sub-yield propagation picture.

Output: assets/sim_outputs/electron_propagation_native.gif
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

_SCRIPT_DIR = Path(__file__).resolve().parent
if str(_SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_DIR))

from native_electron_propagation import render_gif, run_amplitude  # noqa: E402

from ave_path_util import sim_output  # noqa: E402

PROPAGATION_AMP = 0.48


def main() -> None:
    print(f"Electron propagation showcase (amp={PROPAGATION_AMP}×V_SNAP)")
    row = run_amplitude(PROPAGATION_AMP, record_frames=True)
    out_path = sim_output("electron_propagation_native.gif")
    render_gif(row, out_path)
    print(
        f"  Δx={row['centroid_x_delta']:.1f}  Γ_min={row['gamma_min_at_centroid']}"
        f"  moved={row['centroid_moved']}"
    )
    print(f"  gif: {out_path}")


if __name__ == "__main__":
    main()
