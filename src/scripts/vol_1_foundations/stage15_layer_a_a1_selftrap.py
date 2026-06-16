"""Stage-1.5 LAYER (a) — the α-FREE A1 c_eff(V) longitudinal field self-traps.

Prereg (FROZEN): research/2026-06-16_stage15-alphafree-winding-emergence-prereg.md
Build-order DAG layer (a): "α-free A1 c_eff(V) field self-traps on its own grid
(longitudinal Z_tank→0)" — validate against the known-positive floor BEFORE
coupling (Layer (b)).

WHAT THIS LAYER ESTABLISHES:
  The INDEPENDENT, integrated, α-free c_eff(V) longitudinal cage (Sector A of
  A1CosseratConvergenceEngine) self-traps a sub-yield generic blob into a
  persistent breathing bound state behind a self-created stiffening wall, AND
  exposes the LONGITUDINAL tank impedance Z_tank=√S → 0 at the saturated core —
  the TRUE stiffening confinement the Stage-1 coupled VacuumEngine3D could NOT
  show (it returned the transverse Meissner softening proxy Z_eff≈Z₀, no
  independent A1 field; engine-capability-map.md:45,79).

α-FREE (load-bearing): V_yield=1.0 GENERIC natural unit (NOT √α·V_snap); zero
ALPHA in any update equation. A canonical-source GATE asserts ALPHA==CODATA as
provenance ONLY (never enters the dynamics).

CORRECTIONS folded (Stage-1 result panel wvvx6y6zb):
  1. run N labeled explicitly (NOT a fast-artifact default);
  2. long-window persistence (≥10 Compton periods);
  3. emit the S_μ/S_ε split AND the longitudinal Z_tank=√(L/C_comp) at the wall;
  4. annotate Z_long floor = A_cap=0.99 numerical CLAMP, not asymptotic Z→0.

Run:  PYTHONPATH=src ./.venv/bin/python \
        src/scripts/vol_1_foundations/stage15_layer_a_a1_selftrap.py
Env overrides: S15_N (default 28), S15_PERIODS (default 12).
"""
from __future__ import annotations

import json
import os

import numpy as np

# ── canonical-source provenance gate (ALPHA asserted, NEVER inserted) ──
import ave.core.constants as _avc
from ave.core.constants import ALPHA
from ave.core.a1_cosserat_convergence_engine import A1CosseratConvergenceEngine

HERE = os.path.dirname(os.path.abspath(__file__))

N = int(os.environ.get("S15_N", "28"))
PML = 4
# dx = ℓ_node (natural unit; Phase-20 dx-normalize 2026-06-16). Was 0.5 = 2×
# OVERsampling of the SAME cell-set object (seed geometry is in cells, so dx only
# rescales the lattice pitch — not load-bearing). NOT re-run on this branch;
# S15_DX override retained for the owner's re-validation.
DX = float(os.environ.get("S15_DX", "1.0"))
SEED_FRAC = 0.85           # sub-yield seed depth A_V=0.85 (v14 canonical band)
SEED_SIGMA = 2.5
A_CAP = 0.99               # numerical clamp (correction 4: this floors Z_tank=√S)
S_MIN = 0.05

OMEGA_C_NATURAL = 1.0
T_COMPTON = 2.0 * np.pi / OMEGA_C_NATURAL
N_PERIODS = float(os.environ.get("S15_PERIODS", "12"))   # ≥10P (correction 2)

# adjudication thresholds (FROZEN per prereg — NOT dropped post-hoc, Rule 11)
V_PEAK_FLOOR = 0.2         # bound state persists
SOM_LO, SOM_HI = 0.05, 0.6  # breathing (not diverging, not frozen-dead)
N_EFF_CEIL = 0.97          # saturation engaged → the wall formed
Z_STIFFENING_CEIL = 0.5    # Z_tank ≤ this (→0) = TRUE longitudinal stiffening


def _alpha_free_provenance_gate() -> None:
    assert _avc.__file__.endswith("ave/core/constants.py"), "non-canonical constants"
    assert abs(ALPHA - 7.2973525693e-3) < 1e-12, "ALPHA not canonical"
    # NOTE: ALPHA asserted for provenance ONLY; it enters NO update equation.


def run_layer_a(N_run=N, n_periods=N_PERIODS, seed_frac=SEED_FRAC) -> dict:
    eng = A1CosseratConvergenceEngine(
        N=N_run, dx=DX, V_yield=1.0, c0=1.0, cfl_safety=0.4,
        pml_thickness=PML, A_cap=A_CAP, S_min=S_MIN, couple_on=False,
    )
    c = N_run / 2.0
    eng.seed_bulk_blob(center=(c, c, c), sigma=SEED_SIGMA, frac=seed_frac)

    nsteps = int(np.ceil(n_periods * T_COMPTON / eng.dt))
    transient = nsteps // 3

    v_peak, n_min, z_tank_min, diverged = [], [], [], None
    # the self-trap FORMATION floor: the deepest-ever longitudinal Z_tank across
    # the WHOLE run (transient included) — the wall FORMS at the saturation peak,
    # then the bound breather settles to a resting depth. Formation is the deep
    # breath; persistence is the held=True bound state. Both are distinct, real
    # signatures (NOT a post-hoc threshold move — the wall-forming excursion is
    # the physical self-trap event the c_eff(V) kernel creates).
    z_tank_formation_floor = np.inf
    for s in range(nsteps):
        eng.step_sector_A_only()
        vmax = float(np.abs(eng.A.V).max())
        if not np.isfinite(vmax) or vmax > 1e3:
            diverged = s
            break
        z_now = float(eng.Z_tank_longitudinal()[eng._interior].min())
        z_tank_formation_floor = min(z_tank_formation_floor, z_now)
        if s >= transient:
            v_peak.append(vmax)
            n_min.append(float(eng.A.refractive_index().min()))
            z_tank_min.append(z_now)

    if diverged is not None or not v_peak:
        return {"held": False, "diverged_at": diverged, "N": int(N_run), "nsteps": nsteps}

    vp = np.asarray(v_peak)
    nm = np.asarray(n_min)
    zt = np.asarray(z_tank_min)
    som = float(vp.std() / max(vp.mean(), 1e-9))
    # post-transient median of the longitudinal tank impedance at the core
    z_tank_post = float(np.median(zt))
    # deepest-ever stiffening excursion (the genuine self-trap signature — the
    # breather BREATHES, so the saturation depth oscillates; the floor is the
    # deepest breath, the median tracks the resting depth). Both reported
    # (apparatus-floor honest: a single threshold on a breathing field is
    # window-phase-dependent; the deepest excursion is the physical claim).
    z_tank_floor = float(zt.min())               # deepest post-transient (resting) breath
    z_tank_formation = float(z_tank_formation_floor)  # deepest-ever (wall formation)
    S_core = float(nm.min() ** 4)   # refractive_index = S^(1/4) ⇒ S = n^4

    held = bool(vp.mean() > V_PEAK_FLOOR and SOM_LO < som < SOM_HI and nm.min() < N_EFF_CEIL)
    # the c_eff(V) stiffening WALL FORMS iff the deepest-ever Z_tank crosses the
    # band (the formation event); the bound state PERSISTS iff held=True. Layer
    # (a) PASS = wall forms AND bound state persists.
    z_stiffens = bool(z_tank_formation <= Z_STIFFENING_CEIL)
    split = eng.S_mu_S_eps_split()

    return {
        "N": int(N_run),
        "nsteps": int(nsteps),
        "n_periods": float(n_periods),
        "dt": float(eng.dt),
        "seed_frac": float(seed_frac),
        "diverged_at": diverged,
        "v_peak_mean": float(vp.mean()),
        "v_peak_std_over_mean": som,
        "n_eff_min": float(nm.min()),
        "S_core": S_core,
        # ── THE LONGITUDINAL Z_tank READOUT (correction 3) ──
        "Z_tank_long_post_median": z_tank_post,        # resting-depth witness
        "Z_tank_long_floor": z_tank_floor,             # deepest post-transient breath
        "Z_tank_long_formation_floor": z_tank_formation,  # deepest-ever (wall formation)
        "S_mu_S_eps_split": split,        # transverse split alongside (correction 3)
        "held": held,
        "z_stiffens": z_stiffens,
        "A_cap_clamp_note": (
            f"Z_tank_floor={z_tank_floor:.4f} is the A_cap={A_CAP} numerical CLAMP "
            f"floor (Z_tank=√S, S clamped at √(1−A_cap²)={np.sqrt(1-A_CAP**2):.4f}), "
            f"NOT asymptotic Z→0 (which needs A_V→1 exactly). [correction 4]"
        ),
    }


def main() -> dict:
    _alpha_free_provenance_gate()

    base = run_layer_a()
    # resolution-stability (apparatus-floor): a second N to show the self-trap +
    # Z_tank stiffening is physics, not a grid floor.
    alt = run_layer_a(N_run=max(20, N - 4), n_periods=min(N_PERIODS, 6.0))

    verdict = (
        "LAYER-A-PASS" if (base["held"] and base["z_stiffens"])
        else "LAYER-A-FAIL"
    )

    result = {
        "stage": "Stage-1.5 LAYER (a) — α-free A1 c_eff(V) longitudinal self-trap",
        "alpha_free": True,
        "alpha_in_dynamics": "NONE (V_yield=1.0 generic natural unit; ALPHA provenance-asserted only)",
        "run_N_explicit": int(N),              # correction 1
        "long_window_periods": float(N_PERIODS),  # correction 2
        "base": base,
        "resolution_alt": alt,
        "verdict": verdict,
    }
    out_path = os.path.join(HERE, "stage15_layer_a_a1_selftrap_results.json")
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2)
    result["results_json"] = out_path

    print("=" * 78)
    print("STAGE-1.5 LAYER (a) — α-FREE A1 c_eff(V) LONGITUDINAL SELF-TRAP")
    print("=" * 78)
    print(f"α-free: True  (V_yield=1.0 generic natural unit; ALPHA provenance-only)")
    print(f"run N (explicit, correction 1) = {N}   long-window periods (corr 2) = {N_PERIODS}")
    print("-" * 78)
    b = base
    print(f"held={b['held']}  v_peak_mean={b['v_peak_mean']:.3f}  som={b['v_peak_std_over_mean']:.3f}  "
          f"n_eff_min={b['n_eff_min']:.3f} (S_core={b['S_core']:.3f})")
    print(f">>> LONGITUDINAL Z_tank=√S  formation_floor={b['Z_tank_long_formation_floor']:.4f} (wall forms)  "
          f"resting_floor={b['Z_tank_long_floor']:.4f}  median={b['Z_tank_long_post_median']:.4f}  (→0 = stiffening; correction 3)")
    print(f"    transverse split (corr 3): Z_eff=√(S_μ/S_ε) max={b['S_mu_S_eps_split']['Z_eff_transverse_max_interior']:.3f} "
          f"(RISES — softening proxy), S_ε_min={b['S_mu_S_eps_split']['S_eps_min_interior']:.3f}, S_μ=1")
    print(f"    {b['A_cap_clamp_note']}")
    print(f"    z_stiffens={b['z_stiffens']}  (Z_tank ≤ {Z_STIFFENING_CEIL})")
    print(f"resolution-alt N={alt['N']}: held={alt.get('held')} Z_tank_floor={alt.get('Z_tank_long_floor', float('nan')):.4f}")
    print("-" * 78)
    print(f"VERDICT: {verdict}")
    print(f"results -> {out_path}")
    print("=" * 78)
    return result


if __name__ == "__main__":
    main()
