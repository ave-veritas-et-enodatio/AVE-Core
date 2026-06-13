#!/usr/bin/env python3
"""Genesis-23 converter replay — photon-only GAP-1 re-test with trilinear source.

Pre-reg: research/2026-06-12_cross-sector-engine-integration_prereg_FROZEN.md
Reuses genesis-23 machinery (reflection_genesis_23_self_assembly.py) — same
photon seed, impedance wall, NO planted (2,3). Adds converter ON vs OFF ablation.

Does NOT claim (2,3) self-assembly. Tests whether the historical genesis-23 null
(max|V_inc|≈0 from photon alone) lifts when the conserved cross-sector source is ON.

Uses **gyrotropic** converter mode for photon IC: genesis-23 seeds u=0 Beltrami ω
where w·(∇×ω)=0 identically; gyrotropic f_V uses (∇×w)·x̂ with w=ω̇ proxy.
"""

from __future__ import annotations

import importlib.util
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SMOKE = os.environ.get("G23CONV_SMOKE", "0") == "1" or "--smoke" in sys.argv
os.environ.setdefault("GEN23_N", "16" if SMOKE else "24")
os.environ.setdefault("GEN23_STEPS", "20" if SMOKE else "50")

_g23_path = os.path.join(HERE, "reflection_genesis_23_self_assembly.py")
_spec = importlib.util.spec_from_file_location("genesis23", _g23_path)
g23 = importlib.util.module_from_spec(_spec)
sys.modules["genesis23"] = g23
_spec.loader.exec_module(g23)

from ave.core.constants import R_II  # noqa: E402
from ave.core.cross_sector_coupling import scale_cosserat_to_front  # noqa: E402
from ave.topological.k4_cosserat_coupling import _cosserat_A_squared  # noqa: E402
from ave.topological.vacuum_engine import EngineConfig, VacuumEngine3D  # noqa: E402

PROJECT_ROOT = next(p for p in __import__("pathlib").Path(__file__).parents if (p / ".git").exists())
OUT = PROJECT_ROOT / "assets" / "sim_outputs"


def _make_engine(*, converter_on: bool) -> VacuumEngine3D:
    cfg = EngineConfig(
        N=g23.N,
        pml=g23.PML,
        use_impedance_boundary=True,
        couple_v_sector=True,
        impedance_implicit=True,
        impedance_clamp_strength=g23.K_WALL,
        impedance_cfl_safety=g23.CFL_SAFE,
        use_asymmetric_saturation=True,
        disable_cosserat_lc_force=True,
        use_trilinear_converter=converter_on,
        converter_mode="gyrotropic",
    )
    return VacuumEngine3D(cfg)


def _prepare_photon_engine(eng: VacuumEngine3D, *, helicity: float = 1.0) -> None:
    g23._seed_photon(eng, g23.A_LOCK, helicity)
    A_cos_sq = _cosserat_A_squared(
        eng.cos.u, eng.cos.omega, eng.cos.dx, eng.cos.omega_yield, eng.cos.epsilon_yield
    )
    eng.cos.u, eng.cos.omega = scale_cosserat_to_front(
        eng.cos.u, eng.cos.omega, A_cos_sq, target=R_II
    )
    eng.freeze_converter_wall()


def _run_arm(label: str, converter_on: bool) -> dict:
    eng = _make_engine(converter_on=converter_on)
    _prepare_photon_engine(eng)
    v0 = float(np.abs(eng.k4.V_inc).max())
    h0 = g23._hamiltonian(eng)
    g23._run(eng, g23.N_STEPS, record=False)
    vend = float(np.abs(eng.k4.V_inc).max())
    loc, _ = g23._localization(eng)
    return {
        "label": label,
        "converter_on": converter_on,
        "max_V_inc_t0": v0,
        "max_V_inc_end": vend,
        "localization": loc,
        "H_end": g23._hamiltonian(eng),
        "H_delta": g23._hamiltonian(eng) - h0,
        "omega_max": g23._omega_max(eng),
        "L_spin": g23._spin_L(eng),
    }


def main() -> None:
    g23._canonical_source_gate()
    off = _run_arm("PHOTON+CONVERTER-OFF", converter_on=False)
    on = _run_arm("PHOTON+CONVERTER-ON", converter_on=True)

    gap1 = on["max_V_inc_end"] > off["max_V_inc_end"] + 1e-9 and on["max_V_inc_end"] > 1e-9
    bounded = on["omega_max"] < 1e4 and abs(on["H_delta"]) < 1e3

    print("=" * 72)
    print("GENESIS-23 CONVERTER REPLAY", "(SMOKE)" if SMOKE else "(PRODUCTION)")
    print(f"N={g23.N} steps={g23.N_STEPS}")
    print("=" * 72)
    for row in (off, on):
        print(
            f"  {row['label']}: V_inc {row['max_V_inc_t0']:.3e} → {row['max_V_inc_end']:.3e} "
            f"loc={row['localization']:.3f} |ω|max={row['omega_max']:.3f} |L|={row['L_spin']:.3f}"
        )
    print("-" * 72)
    print("GAP-1 lift (ON > OFF):", gap1)
    print("Bounded (no detonation):", bounded)
    print("=" * 72)

    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / "genesis_23_converter_replay.json"
    payload = {"smoke": SMOKE, "off": off, "on": on, "GAP1_lift": gap1, "bounded": bounded}
    path.write_text(json.dumps(payload, indent=2))
    print("Wrote", path)


if __name__ == "__main__":
    main()
