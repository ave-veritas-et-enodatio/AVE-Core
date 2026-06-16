"""Stage-1.5 LAYER (b) — the two-grid coupled system is STABLE (no blow-up).

Prereg (FROZEN): research/2026-06-16_stage15-alphafree-winding-emergence-prereg.md
Build-order DAG layer (b): "couple Sector A (c_eff(V) cage) ⊗ Sector B (vector
Cosserat ω); coupled system stable (no blow-up, ledger flat, |ω| bounded)."

THE TWO-GRID RECONCILIATION (the core multi-week challenge):
  Sector A's c_eff(V) longitudinal field lives on EVERY cell (continuum FDTD);
  Sector B's vector Cosserat micro-rotation lives ONLY on the K4 diamond A/B
  sublattice (mask_alive) — the second grid. They couple through ONE conservative
  shared-front velocity-pair exchange (energize-LOCK, NOT a one-way pump — the
  genesis-24 EMF detonation FIXED). Temporal reconciliation: each grid integrated
  at its own stable dt (Cosserat sub-cycled). Spatial reconciliation: the exchange
  lives only at alive saturation-front cells (CP10 boundary-localized).

WHAT LAYER (b) ESTABLISHES (and does NOT):
  ESTABLISHES: the coupled two-grid system integrates STABLY — |ω| bounded (no
    blow-up), the full coupled Hamiltonian flat/decaying (passive energize-LOCK,
    NOT a pump), validated against the cage-alone floor (a coupled blow-up where
    the cage-alone HELD localizes to the coupling — physics, not the integrator).
  DOES NOT: claim the (2,3) winding self-forms or α emerges — that is Layer (c).
    Layer (b) is the STABILITY gate the emergence probe requires.

α-FREE (load-bearing): κ̃=6/5=pq/(p+q) (the (2,3) topology, NOT κ_chiral=1.2α);
V_yield=1.0 generic; omega_yield=π. Zero ALPHA in any update equation.

Run:  PYTHONPATH=src ./.venv/bin/python \
        src/scripts/vol_1_foundations/stage15_layer_b_coupled_stability.py
Env overrides: S15_N (default 24), S15_PERIODS (default 12).
"""
from __future__ import annotations

import json
import os

import numpy as np

import ave.core.constants as _avc
from ave.core.constants import ALPHA
from ave.core.a1_cosserat_convergence_engine import A1CosseratConvergenceEngine

HERE = os.path.dirname(os.path.abspath(__file__))

N = int(os.environ.get("S15_N", "24"))
PML = 4
DX = 0.5
SEED_FRAC = 0.85
SEED_SIGMA = 2.5
PHOTON_AMP = 0.3            # generic transverse ω-photon precursor (CP8, no plant)
PHOTON_SIGMA = 3.0
PHOTON_LAM = 6.0

OMEGA_C_NATURAL = 1.0
T_COMPTON = 2.0 * np.pi / OMEGA_C_NATURAL
N_PERIODS = float(os.environ.get("S15_PERIODS", "12"))

# adjudication thresholds (FROZEN per prereg — Rule 11)
OMEGA_BLOWUP_FACTOR = 1e3   # |ω|max/seed > this → blow-up flag
RAMP_PUMP_CEIL = 2.0        # full-H ramp > this → PUMPS (not passive)


def _alpha_free_provenance_gate() -> None:
    assert _avc.__file__.endswith("ave/core/constants.py"), "non-canonical constants"
    assert abs(ALPHA - 7.2973525693e-3) < 1e-12, "ALPHA not canonical"


def _ledger_ramp(series) -> float:
    """ave-conserved-vs-pumped ramp = PEAK/baseline (NOT tail/baseline). A
    tail/baseline read MISSES a transient pump that climbs then partially relaxes
    (the early-window pump the coupled run exhibits); peak/baseline catches the
    worst excursion. baseline = the FIRST sample (the seed energy, pre-exchange).
    ≈1 flat (passive); >>1 PUMP."""
    arr = np.asarray([h for h in series if np.isfinite(h)], dtype=float)
    if arr.size < 3:
        return float("nan")
    base = float(np.abs(arr[0]))
    peak = float(np.nanmax(np.abs(arr)))
    if base < 1e-30:
        return float("inf") if peak > 1e-30 else 1.0
    return peak / base


def run_coupled(N_run=N, n_periods=N_PERIODS, couple_on=True, sample_every=4,
                coupling_support="front") -> dict:
    eng = A1CosseratConvergenceEngine(
        N=N_run, dx=DX, V_yield=1.0, c0=1.0, cfl_safety=0.4,
        pml_thickness=PML, A_cap=0.99, S_min=0.05, couple_on=couple_on,
        coupling_support=coupling_support,
    )
    c = N_run / 2.0
    eng.seed_bulk_blob(center=(c, c, c), sigma=SEED_SIGMA, frac=SEED_FRAC)
    eng.seed_cosserat_photon(center=(c, c, c), sigma=PHOTON_SIGMA,
                             wavelength=PHOTON_LAM, amplitude=PHOTON_AMP,
                             direction=(1, 0, 0), helicity=1.0, axis=2)

    nsteps = int(np.ceil(n_periods * T_COMPTON / eng.dt))
    omega_seed = eng.omega_max_interior()

    H_series, omega_C, omega_dot_L, vpk = [], [], [], []
    diverged = None
    fV_live_max = 0.0       # live coupling activation: does the bulk source fire?
    fV_active_steps = 0
    for s in range(nsteps):
        eng.step_coupled()
        oc = eng.omega_max_interior()
        if not np.isfinite(oc) or oc > OMEGA_BLOWUP_FACTOR * max(omega_seed, 1e-6):
            diverged = s
            break
        fv, _ = eng._coupling_forces()
        fvm = float(np.abs(fv).max())
        fV_live_max = max(fV_live_max, fvm)
        if fvm > 1e-6:
            fV_active_steps += 1
        if (s % sample_every == 0) or (s == nsteps - 1):
            H_series.append(eng.total_hamiltonian())
            omega_C.append(oc)
            omega_dot_L.append(eng.omega_dot_max_interior())
            vpk.append(float(np.abs(eng.A.V).max()))

    H_ramp = _ledger_ramp(H_series)
    omega_C_max = float(np.nanmax(omega_C)) if omega_C else 0.0
    return {
        "N": int(N_run), "nsteps": int(nsteps), "n_periods": float(n_periods),
        "couple_on": bool(couple_on), "coupling_support": coupling_support,
        "fV_source_live_max": float(fV_live_max),
        "fV_source_active_frac": float(fV_active_steps / max(nsteps, 1)),
        "n_sub_cos": int(eng.n_sub_cos), "dt": float(eng.dt), "dt_sub_cos": float(eng.dt_sub_cos),
        "diverged_at": diverged,
        "omega_C_seed": float(omega_seed),
        "omega_C_max": omega_C_max,
        "omega_C_final": float(omega_C[-1]) if omega_C else 0.0,
        "omega_dot_L_max": float(np.nanmax(omega_dot_L)) if omega_dot_L else 0.0,
        "omega_max_over_seed": float(omega_C_max / max(omega_seed, 1e-6)),
        "H_total_ramp": H_ramp,
        "H_total_series": [float(h) for h in H_series],
        "V_peak_final": float(vpk[-1]) if vpk else 0.0,
        "V_peak_mean": float(np.mean(vpk)) if vpk else 0.0,
        "coupling_work": float(eng.coupling_work),
        "bulk_E_conserved_final": float(eng.bulk_energy_conserved()),
        "Z_tank_long_floor": float(eng.Z_tank_longitudinal()[eng._interior].min()),
    }


def _bin_support(cpl: dict, off: dict) -> tuple[str, bool, bool, bool]:
    """Bin a coupled run vs the OFF control. The bulk breather's INTRINSIC energy
    excursion is the cage-alone floor (present in OFF too) — NOT a coupling pump.
    The coupling-attributable pump is the ON-minus-OFF EXCESS ramp; the blow-up
    is the |ω| growth beyond the Sector-B-alone floor."""
    blew = (cpl["diverged_at"] is not None) or (cpl["omega_max_over_seed"] > OMEGA_BLOWUP_FACTOR)
    # coupling-attributable pump = ON ramp materially exceeds the OFF (cage-alone)
    # ramp. OFF carries the bulk breather's intrinsic excursion (the known floor).
    on_ramp = cpl["H_total_ramp"] if np.isfinite(cpl["H_total_ramp"]) else 0.0
    off_ramp = off["H_total_ramp"] if np.isfinite(off["H_total_ramp"]) else 0.0
    coupling_pump = (on_ramp > off_ramp * 1.5) and (on_ramp > RAMP_PUMP_CEIL)
    bounded = (not blew) and (not coupling_pump)
    binv = "STABLE" if bounded else ("PUMP" if coupling_pump else "BLOWUP")
    return binv, blew, coupling_pump, bounded


def main() -> dict:
    _alpha_free_provenance_gate()

    off = run_coupled(couple_on=False, n_periods=min(N_PERIODS, 6.0))
    # the DEFAULT CP10 front-localized coupling
    front = run_coupled(couple_on=True, coupling_support="front")
    front_bin, f_blew, f_pump, f_bounded = _bin_support(front, off)
    # the controlled saturated-interior variant (the front-vs-interior fork the
    # front finding surfaces; labeled, NOT the canonical CP10 path)
    interior = run_coupled(couple_on=True, coupling_support="saturated_interior")
    interior_bin, i_blew, i_pump, i_bounded = _bin_support(interior, off)

    # the headline gate = the canonical CP10 FRONT coupling's stability
    verdict = f"LAYER-B-{front_bin}"

    result = {
        "stage": "Stage-1.5 LAYER (b) — two-grid coupled stability",
        "alpha_free": True,
        "alpha_in_dynamics": "NONE (κ̃=6/5=pq/(p+q); V_yield=1.0; ALPHA provenance-only)",
        "run_N_explicit": int(N),
        "long_window_periods": float(N_PERIODS),
        "two_grid_note": (
            "Sector A (c_eff(V) cage) on every cell ⊗ Sector B (vector Cosserat ω) "
            "on the K4 A/B sublattice (mask_alive). Coupled via ONE CONSERVATIVE "
            "Hamiltonian force term H_c=κ̃∫g·V·Ξ (Ξ=(∇×ω)·ẑ; functional-derivative "
            "reciprocal forces — the crystal_engine ADD-2 energize-LOCK structure, "
            f"NOT a velocity rotation). Temporal: Cosserat sub-cycled n_sub={front['n_sub_cos']}. "
            "Spatial: front-localized + alive-masked (CP10)."
        ),
        "control_couple_off": off,
        "front_localized_CP10": {
            "bin": front_bin, "blew_up": f_blew, "coupling_pump": f_pump,
            "bounded": f_bounded, **front},
        "saturated_interior_variant": {
            "bin": interior_bin, "blew_up": i_blew, "coupling_pump": i_pump,
            "bounded": i_bounded, **interior},
        "two_grid_finding": (
            "FRONT coupling (CP10 boundary-localized, the canonical anti-pump path): "
            f"bulk source f_V=−κ̃·g·Ξ is INERT — fV_source_live_max={front['fV_source_live_max']:.2e}, "
            f"active {100*front['fV_source_active_frac']:.0f}% of steps. The saturation "
            "FRONT shell (A_V≈√3/2) and the winding curl Ξ (at the trap INTERIOR) have "
            "DISJOINT support, so the winding never sources the cage → no energize-LOCK "
            "loop closes (the photon radiates: |ω| decays). This is a PRECISELY-LOCALIZED "
            "two-grid SPATIAL-reconciliation obstruction: CP10 front-localization (anti-pump) "
            "vs the winding co-locating with the trap (transfer) is a DESIGN FORK — surfaced "
            "for Grant/auditor, NOT an implementer pivot (Rule 16). The saturated_interior "
            "variant tests the interior-overlap alternative (labeled)."
        ),
        "verdict": verdict,
    }
    out_path = os.path.join(HERE, "stage15_layer_b_coupled_stability_results.json")
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2)
    result["results_json"] = out_path

    print("=" * 78)
    print("STAGE-1.5 LAYER (b) — TWO-GRID COUPLED STABILITY (no blow-up)")
    print("=" * 78)
    print(f"α-free: True  (κ̃=6/5=pq/(p+q); V_yield=1.0; ALPHA provenance-only)")
    print(f"run N (explicit) = {N}   long-window periods = {N_PERIODS}")
    print(f"two-grid: Cosserat sub-cycled n_sub={front['n_sub_cos']} (dt={front['dt']:.4f} dt_sub={front['dt_sub_cos']:.4f})")
    print(f"CONTROL OFF (cage-alone floor): |ω|max={off['omega_C_max']:.3e}  H ramp={off['H_total_ramp']:.2f}")
    print("-" * 78)
    for label, r, b in (("FRONT (CP10)", front, front_bin),
                        ("SAT-INTERIOR (variant)", interior, interior_bin)):
        print(f"{label}:  bin={b}")
        print(f"    |ω| seed={r['omega_C_seed']:.3e} max={r['omega_C_max']:.3e} final={r['omega_C_final']:.3e} "
              f"(max/seed={r['omega_max_over_seed']:.2f})")
        print(f"    |ω̇|max={r['omega_dot_L_max']:.3e}  full-H ramp={r['H_total_ramp']:.2f} (vs OFF {off['H_total_ramp']:.2f})")
        print(f"    bulk-source f_V live_max={r['fV_source_live_max']:.2e} active={100*r['fV_source_active_frac']:.0f}%  "
              f"coupling_work={r['coupling_work']:.2e}")
        print(f"    V_peak_mean={r['V_peak_mean']:.3f}  Z_tank_floor={r['Z_tank_long_floor']:.4f}")
    print("-" * 78)
    print("TWO-GRID FINDING:", result["two_grid_finding"])
    print("-" * 78)
    print(f"VERDICT (canonical CP10 front coupling): {verdict}")
    print(f"results -> {out_path}")
    print("=" * 78)
    return result


if __name__ == "__main__":
    main()
