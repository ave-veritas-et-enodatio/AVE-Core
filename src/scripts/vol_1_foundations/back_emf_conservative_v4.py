#!/usr/bin/env python3
r"""Path B: Zero-Parameter Conservative BEMF Simulation.

Executes the K4-Cosserat electron soliton model with Loop 1 (Op14 saturation)
and Loop 2 (Conservative Inductive BEMF), verifying the kill-switch criteria
set in the peer review: zero free parameters (κ_L = 1.2, η = 0).

Output:
  _output/back_emf_conservative_results.json
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path
from typing import Any

import numpy as np

_SCRIPT_DIR = Path(__file__).resolve().parent
if str(_SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_DIR))

from native_electron_model import (
    N_LATTICE,
    PML,
    SHELL_RADIUS,
    _seed_canonical,
)

from ave.core.constants import ALPHA_COLD, V_SNAP
from ave.topological.vacuum_engine import VacuumEngine3D

OUT_DIR = next(p for p in Path(__file__).resolve().parents if (p / ".git").exists())
OUT_DIR = OUT_DIR / "src" / "scripts" / "vol_1_foundations" / "_output"
OUT_DIR.mkdir(parents=True, exist_ok=True)

AMPLITUDE = 0.92
N_STEPS = 400
CADENCE = 2


def apply_conservative_bemf_v4(engine: VacuumEngine3D, *, kappa_L: float = 1.2):
    """
    Applies the conservative inductive BEMF forces:
        f_V^BEMF = -kappa_L * g * [ w . (curl omega_dot) ]
        f_omega^BEMF = +kappa_L * curl( g * V_dot * w )
    """
    V_scalar = np.asarray(engine.k4.V_inc).mean(axis=-1)
    
    if not hasattr(engine, "_script_V_prev"):
        engine._script_V_prev = V_scalar.copy()
        
    V_dot = (V_scalar - engine._script_V_prev) / engine.k4.dt
    engine._script_V_prev = V_scalar.copy()
    
    omega_dot = np.asarray(engine.cos.omega_dot)
    
    V_sq = np.sum(np.asarray(engine.k4.V_inc) ** 2, axis=-1)
    A_k4 = np.sqrt(np.maximum(V_sq, 0.0)) / engine.V_SNAP
    A = np.minimum(A_k4, 1.0 - 1e-12)
    g = np.exp(-((A - 1.2247) ** 2) / (2.0 * 0.18**2))
    
    u = np.asarray(engine.cos.u)
    omega = np.asarray(engine.cos.omega)
    # Simple director assumption for this test
    w = np.zeros_like(u)
    w[..., 0] = 1.0 
    
    def curl_central(F, dx):
        Fx, Fy, Fz = F[..., 0], F[..., 1], F[..., 2]
        def d(a, axis):
            return (np.roll(a, -1, axis=axis) - np.roll(a, 1, axis=axis)) / (2.0 * dx)
        return np.stack([d(Fz, 1) - d(Fy, 2), d(Fx, 2) - d(Fz, 0), d(Fy, 0) - d(Fx, 1)], axis=-1)
    
    A_vec = (g * V_dot)[..., None] * w
    f_omega = kappa_L * curl_central(A_vec, engine.cos.dx)
    
    # 1. Apply to Cosserat omega_dot
    engine.cos.omega_dot += f_omega * engine.k4.dt / engine.cos.I_omega

    # 2. Apply reciprocal EMF to K4 ports
    # f_V^BEMF = -kappa_L * g * [ w . (curl omega_dot) ]
    curl_omega_dot = curl_central(omega_dot, engine.cos.dx)
    f_V = -kappa_L * g * np.sum(w * curl_omega_dot, axis=-1)
    
    # Distribute the scalar EMF equally across the 4 incident wave ports
    # Mask active sites only
    mask = engine.k4.mask_active
    out = np.broadcast_to(f_V[..., None], (*f_V.shape, 4)).copy()
    out /= 4.0
    inj = out * mask[..., None]
    
    # In K4, V_inc has units of voltage. Update is V += EMF * dt
    engine.k4.V_inc += inj * engine.k4.dt


def _build_engine() -> VacuumEngine3D:
    return VacuumEngine3D.from_args(
        N=N_LATTICE,
        pml=PML,
        temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True, # Disable the unstable Loop 2 Lagrangian force
        enable_cosserat_self_terms=True,
        use_asymmetric_saturation=True,
        axiom_4_enabled=True,
        use_lagrangian_emf_coupling=False,
    )


def run_arm():
    print(f"============================================================")
    print(f"ARM: Path B (Conservative BEMF, κ_L=1.2, η=0)")
    print(f"============================================================")
    
    engine = _build_engine()
    center = (N_LATTICE // 2, N_LATTICE // 2, N_LATTICE // 2)
    _seed_canonical(engine, amplitude=AMPLITUDE)
    
    omega0_max = float(np.abs(np.asarray(engine.cos.omega)).max())
    
    records = []
    
    for step in range(N_STEPS + 1):
        if step % CADENCE == 0:
            omega_max = float(np.abs(np.asarray(engine.cos.omega)).max())
            e_k4 = engine._coupled.k4_energy()
            e_cos = engine._coupled.cosserat_energy()
            z_core = float(np.asarray(engine.k4.z_local_field)[center])
            
            print(f"    Step {step:3d}: z_core={z_core:.4f} |ω|_max={omega_max:.4f} E_K4={e_k4:.4f} E_Cos={e_cos:.6f}")
            records.append({
                "step": step,
                "omega_max": omega_max,
                "e_k4": e_k4,
                "e_cos": e_cos,
            })
            
        # apply conservative BEMF
        apply_conservative_bemf_v4(engine, kappa_L=1.2)
        engine.step()

    omega_f_max = float(np.abs(np.asarray(engine.cos.omega)).max())
    persistence = omega_f_max / max(omega0_max, 1e-12)
    
    print(f"\n  FINAL: ω_persist={persistence:.3f}x")
    
    return {
        "omega0_max": omega0_max,
        "omega_f_max": omega_f_max,
        "persistence": persistence,
        "records": records,
    }


def main():
    print("Path B Conservative BEMF Simulation")
    print(f"  N={N_LATTICE}, A={AMPLITUDE}, steps={N_STEPS}, cadence={CADENCE}")
    
    results = run_arm()
    
    out_path = OUT_DIR / "back_emf_conservative_results.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved JSON to {out_path}")

if __name__ == "__main__":
    main()
