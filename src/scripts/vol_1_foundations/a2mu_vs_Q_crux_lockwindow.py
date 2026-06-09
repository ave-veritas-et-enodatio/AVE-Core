"""Focused confirmation: is there a STABLE A2_mu ~ 1 lock window at intermediate
drive between the under-driven floor (flat ~0.004) and the rupture detonation?

Legacy pump ON (the only config with a dynamical V->omega force), seed omega at
the 0.012 phase-5e anchor, fine amplitude sweep across the rupture transition.
For each, track the full A2_mu(t) and report whether A2_mu ever sits in a
"bound-state band" [0.5, 2.0] for a SUSTAINED window (>=3 consecutive records)
-- the Gamma=-1 boundary-lock the electron-stability hypothesis needs -- vs
flat-floor vs monotone detonation.

Reuses helpers from a2mu_vs_Q_crux.py.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

_HERE = Path(__file__).resolve()
_SRC = _HERE.parents[3] / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))
sys.path.insert(0, str(_HERE.parent))

from a2mu_vs_Q_crux import (  # noqa: E402
    add_k4_drive,
    interior_mask,
    make_engine,
    measure,
    seed_beltrami_omega,
)
from ave.topological.vacuum_engine import PairNucleationGate  # noqa: E402

np.seterr(all="ignore")


def run(amp: float, seed_target: float, n_steps: int = 260, record_every: int = 5) -> dict:
    eng = make_engine(disable_lc=False, temperature=0.0)  # legacy pump ON
    realized = seed_beltrami_omega(eng, seed_target)
    add_k4_drive(eng, amp, resonant=True)
    gate = PairNucleationGate(cadence=record_every)
    eng.add_observer(gate)
    imask = interior_mask(eng)
    traj = []
    for _ in range(n_steps):
        eng.step()
        if eng.step_count % record_every == 0:
            traj.append(measure(eng, gate, imask))
    a2 = np.array([m["A2_mu"] for m in traj])
    in_band = (a2 >= 0.5) & (a2 <= 2.0)
    # longest run of consecutive in-band records
    longest = cur = 0
    for b in in_band:
        cur = cur + 1 if b else 0
        longest = max(longest, cur)
    return {
        "amp": amp,
        "realized_seed": realized,
        "max_A2_mu": float(a2.max()),
        "final_A2_mu": float(a2[-1]),
        "peak_A2_K4": float(max(m["A2_K4"] for m in traj)),
        "rupture": bool(any(m["rupture"] for m in traj)),
        "longest_in_band_records": int(longest),
        "n_records_above_1e3": int((a2 > 1e3).sum()),
    }


def main() -> None:
    # Calibrate seed to realize ~0.012 (the phase-5e anchor)
    eng0 = make_engine(disable_lc=False, temperature=0.0)
    r_lo = seed_beltrami_omega(eng0, 0.012)
    seed_target = 0.012 * (0.012 / max(r_lo, 1e-9))  # linear A2 ~ target scaling
    eng1 = make_engine(disable_lc=False, temperature=0.0)
    r_hi = seed_beltrami_omega(eng1, seed_target)
    print(f"seed calibration: target 0.012 -> realized {r_lo:.5f}; "
          f"rescaled target {seed_target:.4f} -> realized {r_hi:.5f}", flush=True)

    print("\namp   realized_seed  max_A2_mu     final_A2_mu  peak_A2_K4  rupture  in_band_run  n>1e3")
    for amp in [1.00, 1.10, 1.15, 1.20, 1.25, 1.30, 1.40]:
        res = run(amp, seed_target)
        print(
            f"{res['amp']:.2f}  {res['realized_seed']:.5f}      "
            f"{res['max_A2_mu']:.4e}   {res['final_A2_mu']:.4e}  "
            f"{res['peak_A2_K4']:.3e}   {str(res['rupture']):>5s}    "
            f"{res['longest_in_band_records']:>4d}        {res['n_records_above_1e3']:>3d}",
            flush=True,
        )


if __name__ == "__main__":
    main()
