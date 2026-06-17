"""Keystone bug-vs-substrate discriminator — PIECE 2: the nested conservation ladder.

Prereg (FROZEN, Rule-11): research/2026-06-16_keystone-discriminator-ladder-prereg.md
Spec (authoritative): _orchestration/2026-06-16_keystone-discriminator-spec.md (PIECE 2)
Builds on: research/2026-06-16_stage16-k4tlm-bounded-wall_result.md (Phase-22 PUMPS,
  coupling-pump reattribution).

THE QUESTION: the Phase-22 PUMPS (H: 856→8.2e9) is reattributed to a pre-existing
pump in the energize-LOCK coupling + the two-grid integration. Is it a FIXABLE
DISCRETIZATION ARTIFACT or a GENUINE SUBSTRATE NEGATIVE?

A naive single-grid known-positive is DEGENERATE (≥4 confounds — mask projection,
wall, PML, two-grid roll — all survive it). This driver strips them one rung at a
time, measuring the conserved witness H = E_bulk + H_cosserat + H_c on a CLOSED
INTERIOR BOX B_int (guard band ≥ stencil_radius + c·dt·nsteps, so no roll/wall/PML
cell leaks in within the run):

  RUNG-0  BASELINE-CLEAN: couple_off, wall_off, PML off, single grid, projection OFF,
          compact sub-yield smooth seed inside B_int. H over B_int must be FLAT to
          O(dt²). Drift ⇒ HARNESS-DIRTY ⇒ STOP (the discriminator is uncalibrated).
  RUNG-1  +PROJECTION: the alive-mask projection back ON (the genesis-24 prime
          suspect). Flat at RUNG-0 but drifts at RUNG-1 ⇒ PROJECTION-PUMP.
  RUNG-2  +COUPLING, FORCED-OVERLAP, dt→0: coupling on, supports overlap, sweep
          dt→0, measure the H-climb RATE. Rate→0 ⇒ INTEGRATOR-ARTIFACT (bug,
          keystone open). Rate plateaus ⇒ SUBSTRATE-PUMP (keystone leans negative).

α-FREE (load-bearing): no ALPHA/KAPPA in the update path. wall_on=False on the
ladder rungs; the kappa_chiral=0 geometric override is unused here. The (2,3)
readout is untouched.

Run:  PYTHONPATH=src ./.venv/bin/python \
        src/scripts/vol_1_foundations/keystone_discriminator_ladder.py
Env overrides: KL_N (default 32), KL_TWIN (default 4.0 physical-time window),
  KL_H (default 8 box half-extent), KL_NDT (default 4 dt-sweep points).
"""
from __future__ import annotations

import json
import os

import numpy as np

import ave.core.constants as _avc
from ave.core.constants import ALPHA
from ave.core.a1_cosserat_moving_wall_engine import A1CosseratMovingWallEngine

HERE = os.path.dirname(os.path.abspath(__file__))

# ── FROZEN geometry (prereg §1, §3) ──────────────────────────────────────────
N = int(os.environ.get("KL_N", "32"))
DX = 1.0
PML = 0                       # RUNG-0..2: PML genuinely off (box guard handles the edge)
CENTER = N / 2.0
H_BOX = int(os.environ.get("KL_H", "8"))      # B_int = [c−h, c+h]³ → guard 8 to the edge
T_WIN = float(os.environ.get("KL_TWIN", "4.0"))  # FROZEN physical recording window
N_DT = int(os.environ.get("KL_NDT", "4"))     # dt grid points: dt_base/2^k, k=0..N_DT−1
STENCIL_RADIUS = 2            # bare energy-gradient + tetrahedral-curl stencil radius

# Compact, sub-yield, smooth Cosserat ω-photon seed (peak |ω| = AMP < omega_yield=π,
# so the bare integrator is in its conservative regime — a super-yield steep seed
# makes a t=0 nonlinear-regime transient that is projection-INDEPENDENT and would
# confound RUNG-0; verified pre-reg). FROZEN across the whole ladder (only dt varies
# at RUNG-2), so the t=0 transient is constant and only the integrator's dt-scaling
# moves the climb rate.
SEED_AMP = 0.1
SEED_SIGMA = 2.0
SEED_LAM = 6.0
# RUNG-2 bulk blob (sub-yield A1 mass co-located with the ω-seed, provides the V the
# coupling needs; FORCED-OVERLAP via coupling_support='saturated_interior').
BULK_FRAC = 0.7
BULK_SIGMA = 2.5


def _alpha_free_provenance_gate() -> None:
    """α-free: the canonical constants module is loaded for COMPARISON-ONLY (ALPHA is
    NEVER inserted into the update path). The ladder rungs run wall_on=False, so the
    α-bearing KAPPA_CHIRAL_ELECTRON Γ path is not even reached."""
    assert _avc.__file__.endswith("ave/core/constants.py"), "non-canonical constants"
    assert abs(ALPHA - 7.2973525693e-3) < 1e-12, "ALPHA not canonical"


def _ols_slope(t, y):
    """Ordinary-least-squares slope of y vs t (the H-climb RATE = dH/dt)."""
    t = np.asarray(t, dtype=float)
    y = np.asarray(y, dtype=float)
    if t.size < 2:
        return 0.0
    tm, ym = t.mean(), y.mean()
    denom = float(((t - tm) ** 2).sum())
    if denom < 1e-30:
        return 0.0
    return float(((t - tm) * (y - ym)).sum() / denom)


def main() -> dict:
    _alpha_free_provenance_gate()
    print("=" * 80)
    print("KEYSTONE BUG-vs-SUBSTRATE DISCRIMINATOR — PIECE 2: NESTED CONSERVATION LADDER")
    print("=" * 80)

    # Reference engine to read the frozen dt + the guard-band geometry.
    ref = A1CosseratMovingWallEngine(N=N, dx=DX, pml_thickness=PML,
                                     couple_on=False, wall_on=False, project_alive=False)
    dt_base = float(ref.dt)
    c_T = float(np.sqrt(ref.B.G / ref.B.rho))
    guard = CENTER - H_BOX                       # box face → domain edge, in cells
    guard_req = STENCIL_RADIUS + c_T * T_WIN     # spec: ≥ stencil_radius + c·T_win
    box = ref.make_box_mask((CENTER, CENTER, CENTER), H_BOX)
    box_idx = np.argwhere(box)

    geom = {
        "N": N, "dx": DX, "pml_thickness": PML,
        "B_int_center": [CENTER, CENTER, CENTER], "B_int_half_extent": H_BOX,
        "B_int_bbox_min": box_idx.min(0).tolist(), "B_int_bbox_max": box_idx.max(0).tolist(),
        "B_int_cells": int(box.sum()),
        "guard_band_cells": float(guard), "guard_band_required_cells": float(guard_req),
        "guard_band_satisfied": bool(guard >= guard_req),
        "c_T": c_T, "T_win_physical": T_WIN, "dt_base": dt_base,
        "stencil_radius": STENCIL_RADIUS,
        "seed": {"amp": SEED_AMP, "sigma": SEED_SIGMA, "wavelength": SEED_LAM,
                 "omega_yield": float(np.pi), "sub_yield": bool(SEED_AMP < np.pi)},
    }
    print(f"N={N} dx={DX} PML={PML} | B_int=[{box_idx.min(0)}..{box_idx.max(0)}] "
          f"({int(box.sum())} cells) | guard={guard:.0f} ≥ req={guard_req:.2f} "
          f"→ {geom['guard_band_satisfied']}")
    print(f"c_T={c_T} T_win={T_WIN} dt_base={dt_base:.5e} | seed amp={SEED_AMP} "
          f"(sub-yield<π={geom['seed']['sub_yield']})")

    result = {
        "discriminator": "keystone bug-vs-substrate — PIECE 2 nested conservation ladder",
        "alpha_free": True,
        "alpha_in_dynamics": "NONE (wall_on=False on all rungs; no ALPHA/KAPPA in update path)",
        "b_int_geometry": geom,
        "frozen_bins": ["HARNESS-DIRTY", "PROJECTION-PUMP", "INTEGRATOR-ARTIFACT",
                        "SUBSTRATE-PUMP", "BOUNDARY-INJECTION"],
    }

    # RUNG-0, RUNG-1, RUNG-2 are appended by the section-builders below (added in
    # subsequent commits per incremental-write discipline).
    _run_rung0(result, box)
    if result["rung0"]["bin_if_fail"] == "HARNESS-DIRTY":
        # RUNG-0 FAILED → STOP (do NOT fabricate downstream rungs).
        result["verdict"] = "HARNESS-DIRTY"
        result["verdict_reason"] = (
            "RUNG-0 H over B_int is NOT flat to O(dt²) — the harness/projection is "
            "dirty; the whole discriminator is uncalibrated. STOP (no RUNG-1/2).")
    else:
        _run_rung1(result, box)
        if result["rung1"]["bin"] == "PROJECTION-PUMP":
            result["verdict"] = "PROJECTION-PUMP"
            result["verdict_reason"] = (
                "RUNG-0 flat but RUNG-1 (+projection) drifts — the mid-Verlet alive-mask "
                "projection is the pump (a fixable harness bug), isolated.")
        else:
            _run_rung2(result, box, dt_base)
            result["verdict"] = result["rung2"]["bin"]
            result["verdict_reason"] = result["rung2"]["reason"]

    print("\n" + "=" * 80)
    print(f"VERDICT: {result['verdict']}")
    print(f"  {result['verdict_reason']}")
    print("=" * 80)

    out_path = os.path.join(HERE, "keystone_discriminator_ladder_results.json")
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2, default=float)
    result["results_json"] = out_path
    print(f"results → {out_path}")
    return result


# ── RUNG section-builders (filled in subsequent commits) ─────────────────────
def _run_rung0(result, box):
    raise NotImplementedError("RUNG-0 — added next commit")


def _run_rung1(result, box):
    raise NotImplementedError("RUNG-1 — added next commit")


def _run_rung2(result, box, dt_base):
    raise NotImplementedError("RUNG-2 — added next commit")


if __name__ == "__main__":
    main()
