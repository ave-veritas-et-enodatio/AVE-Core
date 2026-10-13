"""Timing probe for the R2 K4 configuration — measures wall time per step.

NOT RUN without Grant's GO.  Guard: set AVE_TIMING_PROBE_GO=1 in the
environment before importing run_timing_probe or calling this as __main__.

Grids probed: 192³ and 288³ at R2 settings (γ=4320, k_op10=1.415e6, k_refl=0,
dt=2.24e-4, rotation_storage="quaternion").  The probe runs N_PROBE_STEPS=200
steps and reports wall-time-per-step for each grid; no output is saved.

Source: 2026-10-08-charged-seed-K4-BRIEF.md §Also ("a short timing probe config,
a few hundred steps at 192³ and 288³") + setup sheet (920c213bd3b4).

Usage (after GO):
    AVE_TIMING_PROBE_GO=1 PYTHONPATH=src \\
        python src/scripts/vol_4_engineering/csk4_timing_probe.py
"""

import os

# ---------------------------------------------------------------------------
# Guard — must be set before any simulation is attempted.
# Checked at function-call time (not at import time) so tests can import
# this module safely.
# ---------------------------------------------------------------------------

_GO_VAR = "AVE_TIMING_PROBE_GO"

N_PROBE_STEPS = 200

PROBE_GRIDS = [
    (192, 192, 192),
    (288, 288, 288),
]


def _require_go():
    if not os.environ.get(_GO_VAR):
        raise RuntimeError(
            f"Set {_GO_VAR}=1 to confirm Grant GO before running the timing probe."
        )


def run_timing_probe():
    """Allocate each grid, run N_PROBE_STEPS steps, report wall-time/step.

    Requires AVE_TIMING_PROBE_GO=1 in the environment.
    """
    _require_go()  # guard fires immediately; no expensive imports before this

    import time  # pragma: no cover
    import numpy as np  # pragma: no cover
    from csk4_r2_config import (  # pragma: no cover
        GAMMA, G, G_C, K_OP10, K_REFL, ROTATION_STORAGE, DT,
        assert_r2_config,
    )
    from ave.topological.cosserat_field_3d import CosseratField3D  # pragma: no cover

    for (nx, ny, nz) in PROBE_GRIDS:
        label = f"{nx}³"
        print(f"\nAllocating {label} K4 solver (γ={GAMMA}, k_op10={K_OP10})...")
        t_alloc = time.time()
        cf = CosseratField3D(
            nx, ny, nz,
            k_refl=K_REFL,
            rotation_storage=ROTATION_STORAGE,
        )
        cf.gamma = GAMMA
        cf.G = G
        cf.G_c = G_C
        cf.k_op10 = K_OP10
        assert_r2_config(cf)
        print(f"  Allocated in {time.time()-t_alloc:.2f}s")

        print(f"  Running {N_PROBE_STEPS} steps at dt={DT}...")
        t0 = time.time()
        for _ in range(N_PROBE_STEPS):
            cf.step(DT)
        elapsed = time.time() - t0
        per_step = elapsed / N_PROBE_STEPS
        n_alive = int(cf.mask_alive.sum())
        per_msite = per_step / (n_alive / 1e6)
        print(f"  {label}: {per_step*1e3:.1f} ms/step  "
              f"({per_msite:.2f} ms/Msite, {n_alive/1e6:.2f}M alive sites)")


if __name__ == "__main__":
    run_timing_probe()
