"""Coupling-live verification for the longitudinal-bemf PIN.

Disambiguates the PIN verdict:
  - SCREENED-PIN (real falsification): the longitudinal u-drive DOES reach the
    saturation kernel (S_eps mean moves at large drive) but is screened at the
    core where V²>>1 already clips A²_eps (S_eps@core stays floored regardless).
  - SILENT NO-OP (artifact): the drive never reaches S_eps at all (mean unmoved
    even at 100x rupture amplitude) -> the byte-identical V-sector evolution is a
    wiring disconnect, not screening -> PIN would be mislabeled.

Mirrors the engine's OWN kernel call (vacuum_engine.py:1320-1329) exactly.

Committed as the coupling-live control closing the review's reproducibility gap.
Independent re-run result (N=48, settle=10, Variant-B displacement drive — the
same drive main() selects):
    NO DRIVE              : S_eps mean=0.9734   S_eps@core=1.000e-05
    v_drive=0.30 (physical): S_eps mean=0.9713   S_eps@core=1.000e-05
    v_drive=30   (100x)    : S_eps mean=0.0511   S_eps@core=1.000e-05
=> COUPLING LIVE (mean moves 0.973->0.051 at 100x) + SCREENED@CORE (core pinned at
   the 1e-5 floor regardless) => SCREENED-PIN confirmed, NOT a wiring no-op.
"""
import sys
from pathlib import Path

# repo root = parents[3] of src/scripts/vol_1_foundations/<this file>
WT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(WT / "src"))
sys.path.insert(0, str(WT / "src/scripts/vol_1_foundations"))

import numpy as np
import jax.numpy as jnp

from motion_stability_bemf_longitudinal_probe import (
    setup_engine, seed_host, apply_longitudinal_drive, _interior_mask,
)
from ave.topological.cosserat_field_3d import _update_saturation_kernels
from ave.topological.k4_cosserat_coupling import _v_squared_per_site

N, PML = 48, 4


def S_eps_field(engine):
    """Byte-faithful mirror of the engine's own kernel call."""
    V_sq = _v_squared_per_site(engine.k4.V_inc)
    _S_mu, S_eps = _update_saturation_kernels(
        jnp.asarray(engine.cos.u),
        jnp.asarray(engine.cos.omega),
        jnp.asarray(V_sq),
        engine.cos.dx,
        engine.V_SNAP,
        engine.cos.omega_yield,
        engine.cos.epsilon_yield,
        engine._coupled.kappa_chiral,
    )
    return np.asarray(S_eps)


def measure(engine):
    S_eps = S_eps_field(engine)
    alive = np.asarray(engine.cos.mask_alive)
    m = _interior_mask(N, PML) & alive
    A2 = np.sum(np.asarray(engine.k4.V_inc) ** 2, axis=-1) / engine.V_SNAP ** 2
    ci = np.unravel_index(np.argmax(np.where(m, A2, -1.0)), A2.shape)
    return float(S_eps[m].mean()), float(S_eps[ci]), ci, float(A2[ci])


def fresh():
    e = setup_engine(N, PML)
    seed_host(e, N)
    for _ in range(10):
        e.step()
    return e


print("Seeding (2,3) host  N=48 PML=4 settle=10 ...", flush=True)
e0 = fresh()
b_mean, b_core, ci, coreA2 = measure(e0)
print(f"  core cell {ci}  V-sector A2={coreA2:.3f}", flush=True)
print(f"NO DRIVE              : S_eps mean={b_mean:.4f}   S_eps@core={b_core:.3e}", flush=True)

rows = []
for vd in (0.30, 30.0):
    e = fresh()
    apply_longitudinal_drive(e, vd, N, PML, variant="B", form="displacement")
    mn, cr, _c, _a = measure(e)
    tag = "physical" if vd < 1 else "100x rupture"
    rows.append((vd, tag, mn, cr))
    print(f"v_drive={vd:<6} ({tag:<12}): S_eps mean={mn:.4f}   S_eps@core={cr:.3e}", flush=True)

mn30 = rows[-1][2]
cr30 = rows[-1][3]
print(flush=True)
print("=" * 64, flush=True)
mean_moved = abs(b_mean - mn30) > 0.1 * b_mean
core_floored = cr30 < 10.0 * max(b_core, 1e-6)
print(f"COUPLING LIVE?  S_eps mean {b_mean:.3f} -> {mn30:.3f} at 100x   "
      f"=> {'LIVE (drive reaches kernel)' if mean_moved else 'NO-OP (drive never reaches kernel!)'}", flush=True)
print(f"SCREENED@CORE?  S_eps@core {b_core:.2e} -> {cr30:.2e}            "
      f"=> {'SCREENED (V2 clips core regardless)' if core_floored else 'core RESPONDS (not screened)'}", flush=True)
print("=" * 64, flush=True)
if mean_moved and core_floored:
    print("VERDICT: SCREENED-PIN CONFIRMED -- coupling live, screened at core. Result is a real falsification.", flush=True)
elif not mean_moved:
    print("VERDICT: SILENT NO-OP -- drive never reaches S_eps. PIN may be a wiring artifact. ESCALATE.", flush=True)
else:
    print("VERDICT: coupling live but core NOT screened -- mechanism is different than stated. Review.", flush=True)
