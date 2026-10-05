"""
Generator for src/tests/fixtures/u0_golden_16x16x16_seed42.npz.

Reproduces the golden fixture committed with PR #1059 (ENV-D bond reflection).
Run against a clean checkout of the intended base commit (50fdb644) to obtain
an authoritative fixture; running against any head that leaves the default
CosseratField3D code path bitwise-unchanged from 50fdb644 produces the same
file (verified in the PR #1059 audit).

Usage (from repo root, base commit or any compatible head):
    PYTHONPATH=src ~/AVE-staging/AVE-Core/.venv/bin/python src/scripts/gen_u0_golden.py

The output path defaults to src/tests/fixtures/u0_golden_16x16x16_seed42.npz
relative to the script's directory.  Pass a different path as sys.argv[1] to
override.

Setup mirrors TestU0GoldenFixture._make_solver_with_velocities:
    CosseratField3D(16, 16, 16, use_saturation=True)
    rng_seed=42  → omega, u
    rng_seed=7   → u_dot, omega_dot
    jax_enable_x64=True, dt=0.05, 10 steps
"""

import os
import sys
import numpy as np
import jax

jax.config.update("jax_enable_x64", True)

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from ave.topological.cosserat_field_3d import CosseratField3D

_DEFAULT_OUT = os.path.join(
    os.path.dirname(__file__), "..", "tests", "fixtures",
    "u0_golden_16x16x16_seed42.npz",
)

out_path = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else _DEFAULT_OUT)

solver = CosseratField3D(16, 16, 16, use_saturation=True)
rng = np.random.default_rng(42)
solver.omega = rng.uniform(-0.05, 0.05, solver.omega.shape) * solver.mask_alive[..., None]
solver.u = rng.uniform(-0.02, 0.02, solver.u.shape) * solver.mask_alive[..., None]
rng2 = np.random.default_rng(7)
solver.u_dot = rng2.uniform(-1e-3, 1e-3, solver.u_dot.shape) * solver.mask_alive[..., None]
solver.omega_dot = rng2.uniform(-1e-3, 1e-3, solver.omega_dot.shape) * solver.mask_alive[..., None]

E0 = solver.total_energy()
gu, gw = solver.energy_gradient()

for _ in range(10):
    solver.step(0.05)

E10 = solver.total_energy()

np.savez(
    out_path,
    E0=np.float64(E0),
    gu_norm=np.float64(np.linalg.norm(gu)),
    gw_norm=np.float64(np.linalg.norm(gw)),
    gu=gu,
    gw=gw,
    u10=solver.u,
    omega10=solver.omega,
    u_dot10=solver.u_dot,
    omega_dot10=solver.omega_dot,
    E10=np.float64(E10),
)
print(f"Wrote {out_path}")
print(f"  E0={E0:.15g}  E10={E10:.15g}")
print(f"  Module: {CosseratField3D.__module__}")
