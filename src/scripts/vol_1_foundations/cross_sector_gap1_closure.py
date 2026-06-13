#!/usr/bin/env python3
"""GAP-1 closure probe — cross-sector ω/shear → K4 V_inc bootstrap.

Pre-reg: research/2026-06-12_cross-sector-engine-integration_prereg_FROZEN.md

Primary falsifier (genesis-23): max|V_inc| > 0 from Cosserat shear+ω seed with
K4 V_inc ≡ 0 at t=0, when the conserved trilinear converter is ON and the
saturation front g_wall is localized by combined K4+Cosserat strain.

Does NOT claim the (2,3) electron — only the cross-sector SOURCE channel.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

from ave.core.constants import R_II
from ave.core.cross_sector_coupling import scale_cosserat_to_front
from ave.topological.k4_cosserat_coupling import CoupledK4Cosserat, _cosserat_A_squared

PROJECT_ROOT = next(p for p in Path(__file__).parents if (p / ".git").exists())
OUT = PROJECT_ROOT / "assets" / "sim_outputs"


def _seed_helical(sim: CoupledK4Cosserat, *, amp_u: float = 0.4, amp_omega: float = 0.35) -> None:
    N = sim.N
    x = np.linspace(0, 2 * np.pi, N)
    y = np.linspace(0, 2 * np.pi, N)
    env = np.exp(
        -(
            (np.arange(N)[:, None, None] - N // 2) ** 2
            + (np.arange(N)[None, :, None] - N // 2) ** 2
            + (np.arange(N)[None, None, :] - N // 2) ** 2
        )
        / (2.0 * 2.5**2)
    )
    sim.cos.u[..., 1] += amp_u * np.sin(x)[:, None, None] * np.cos(y)[None, :, None] * env
    sim.cos.omega[..., 2] += amp_omega * np.cos(x)[:, None, None] * np.sin(y)[None, :, None] * env
    A_cos_sq = _cosserat_A_squared(
        sim.cos.u, sim.cos.omega, sim.cos.dx, sim.cos.omega_yield, sim.cos.epsilon_yield
    )
    sim.cos.u, sim.cos.omega = scale_cosserat_to_front(sim.cos.u, sim.cos.omega, A_cos_sq, target=R_II)
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
) -> dict:
    sim = CoupledK4Cosserat(
        N=N,
        pml=3,
        use_trilinear_converter=converter_on,
        converter_mode="trilinear",
        disable_cosserat_lc_force=True,
        couple_v_sector=True,
    )
    _seed_helical(sim)
    sim.freeze_converter_wall()
    v0 = float(np.max(np.abs(sim.k4.V_inc)))
    for _ in range(n_steps):
        sim.step()
    vend = float(np.max(np.abs(sim.k4.V_inc)))
    return {
        "label": label,
        "converter_on": converter_on,
        "v_inc_max_t0": v0,
        "v_inc_max_end": vend,
        "H_couple_end": sim.converter_coupling_energy(),
        "max_A_sq": float(sim.max_A_squared()),
    }


def main() -> None:
    smoke = "--smoke" in sys.argv
    N = 10 if smoke else 14
    n_steps = 30 if smoke else 80

    off = _run_arm(label="CONVERTER-OFF", converter_on=False, n_steps=n_steps, N=N)
    on = _run_arm(label="CONVERTER-ON", converter_on=True, n_steps=n_steps, N=N)

    gap1_pass = on["v_inc_max_end"] > 1e-6 and on["v_inc_max_end"] > off["v_inc_max_end"] + 1e-7

    print("=" * 72)
    print("CROSS-SECTOR GAP-1 CLOSURE PROBE", "(SMOKE)" if smoke else "(PRODUCTION)")
    print("=" * 72)
    for row in (off, on):
        print(
            f"  {row['label']}: V_inc(t=0)={row['v_inc_max_t0']:.3e} "
            f"V_inc(end)={row['v_inc_max_end']:.3e} H_couple={row['H_couple_end']:.4f}"
        )
    print("-" * 72)
    print("GAP-1 PASS (V_inc energizes from Cosserat seed):", gap1_pass)
    print("=" * 72)

    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / "cross_sector_gap1_closure.json"
    path.write_text(json.dumps({"smoke": smoke, "off": off, "on": on, "GAP1_pass": gap1_pass}, indent=2))
    print("Wrote", path)


if __name__ == "__main__":
    main()
