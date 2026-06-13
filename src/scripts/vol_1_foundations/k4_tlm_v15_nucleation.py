#!/usr/bin/env python3
"""Genesis v15b — K4 V_inc nucleation probe (Lane A longitudinal read).

P15-V gate: max|V_inc| > floor after saturation-pair analogue seed on
CoupledK4Cosserat with trilinear converter ON.

Pre-reg: research/2026-06-12_genesis-v15-nucleation-from-latent_prereg_DRAFT.md §P15-V
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

from ave.core.constants import ALPHA, R_II
from ave.core.cross_sector_coupling import scale_cosserat_to_front
from ave.topological.k4_cosserat_coupling import CoupledK4Cosserat, _cosserat_A_squared

PROJECT_ROOT = next(p for p in Path(__file__).parents if (p / ".git").exists())
OUT = PROJECT_ROOT / "assets" / "sim_outputs"

P15_V_FLOOR = 1e-12


def _pair_seed_cosserat(sim: CoupledK4Cosserat, *, amp: float) -> None:
    """Minimal saturated pair analogue — two helical hotspots, no propagating packet."""
    N = sim.N
    cx, cy, cz = N // 2, N // 2, N // 2
    for dx, dy in ((0, 0), (1, 0)):
        ix = min(max(cx + dx, 0), N - 1)
        iy = min(max(cy + dy, 0), N - 1)
        env = np.exp(
            -(
                (np.arange(N)[:, None, None] - ix) ** 2
                + (np.arange(N)[None, :, None] - iy) ** 2
                + (np.arange(N)[None, None, :] - cz) ** 2
            )
            / (2.0 * 1.2**2)
        )
        sim.cos.u[..., 0] += amp * env
        sim.cos.omega[..., 2] += 0.5 * amp * env
    A_cos_sq = _cosserat_A_squared(
        sim.cos.u, sim.cos.omega, sim.cos.dx, sim.cos.omega_yield, sim.cos.epsilon_yield
    )
    sim.cos.u, sim.cos.omega = scale_cosserat_to_front(
        sim.cos.u, sim.cos.omega, A_cos_sq, target=R_II
    )
    sim.cos.u_dot[:] = 0.0
    sim.cos.omega_dot[:] = 0.0
    sim.k4.V_inc[:] = 0.0
    sim.k4.V_ref[:] = 0.0


def _run_arm(
    *,
    label: str,
    converter_on: bool,
    n_steps: int,
    N: int,
    amp: float,
) -> dict:
    sim = CoupledK4Cosserat(
        N=N,
        pml=3,
        use_trilinear_converter=converter_on,
        converter_mode="trilinear",
        disable_cosserat_lc_force=True,
        couple_v_sector=True,
    )
    _pair_seed_cosserat(sim, amp=amp)
    sim.freeze_converter_wall()
    v0 = float(np.max(np.abs(sim.k4.V_inc)))
    trace: list[float] = []
    for _ in range(n_steps):
        sim.step()
        trace.append(float(np.max(np.abs(sim.k4.V_inc))))
    vend = trace[-1] if trace else v0
    vpeak = max(trace) if trace else v0
    return {
        "label": label,
        "converter_on": converter_on,
        "amp": amp,
        "v_inc_max_t0": v0,
        "v_inc_max_end": vend,
        "v_inc_peak": vpeak,
        "H_couple_end": sim.converter_coupling_energy(),
        "max_A_sq": float(sim.max_A_squared()),
        "p15v_pass": vpeak > P15_V_FLOOR and (not converter_on or vend > v0 + 1e-15),
    }


def main() -> None:
    smoke = "--smoke" in sys.argv
    N = 10 if smoke else 14
    n_steps = 40 if smoke else 100
    amp = float(np.sqrt(ALPHA))

    off = _run_arm(
        label="pair seed CONVERTER-OFF",
        converter_on=False,
        n_steps=n_steps,
        N=N,
        amp=amp,
    )
    on = _run_arm(
        label="pair seed CONVERTER-ON",
        converter_on=True,
        n_steps=n_steps,
        N=N,
        amp=amp,
    )
    heal = _run_arm(
        label="zero seed CONVERTER-ON",
        converter_on=True,
        n_steps=n_steps,
        N=N,
        amp=0.0,
    )

    p15v_pass = on["p15v_pass"] and on["v_inc_peak"] > heal["v_inc_peak"] + 1e-15
    if on["v_inc_peak"] <= P15_V_FLOOR:
        verdict = "HEAL-CONFIRMED"
    elif p15v_pass:
        verdict = "V_INC-LANDED"
    elif on["v_inc_peak"] > off["v_inc_peak"]:
        verdict = "PARTIAL"
    else:
        verdict = "ENGINE-GAP"

    tag = "(SMOKE)" if smoke else "(PRODUCTION)"
    print("=" * 72)
    print("GENESIS v15b — K4 V_inc NUCLEATION (P15-V)", tag)
    print(f"N={N} steps={n_steps} amp=√α={amp:.4f} floor={P15_V_FLOOR:.0e}")
    print("=" * 72)
    for row in (off, on, heal):
        print(
            f"  {row['label']}: V_inc peak={row['v_inc_peak']:.3e} "
            f"end={row['v_inc_max_end']:.3e} P15-V={row['p15v_pass']}"
        )
    print("=" * 72)
    print("VERDICT:", verdict)
    print("=" * 72)

    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / "genesis_v15b_k4_nucleation.json"
    payload = {
        "smoke": smoke,
        "verdict": verdict,
        "P15_V_floor": P15_V_FLOOR,
        "off": off,
        "on": on,
        "heal": heal,
        "P15_V_pass": p15v_pass,
    }
    path.write_text(json.dumps(payload, indent=2))
    print(f"Wrote {path}")


if __name__ == "__main__":
    main()
