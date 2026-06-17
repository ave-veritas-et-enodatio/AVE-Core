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


# ── shared rung runner ───────────────────────────────────────────────────────
def _build_rung_engine(couple_on, wall_on, project_alive, coupling_support, with_bulk, dt):
    """Build a ladder engine at a given dt with the compact sub-yield ω-seed (and an
    optional co-located sub-yield bulk blob for RUNG-2's FORCED-OVERLAP coupling).
    pml=0 on every rung (PML off; the box guard band handles the domain edge)."""
    eng = A1CosseratMovingWallEngine(
        N=N, dx=DX, pml_thickness=PML, couple_on=couple_on, wall_on=wall_on,
        coupling_support=coupling_support, project_alive=project_alive,
    )
    if with_bulk:
        eng.seed_bulk_blob(center=(CENTER, CENTER, CENTER), sigma=BULK_SIGMA, frac=BULK_FRAC)
    eng.seed_cosserat_photon(
        center=(CENTER, CENTER, CENTER), sigma=SEED_SIGMA, wavelength=SEED_LAM,
        amplitude=SEED_AMP, direction=(1, 0, 0), helicity=1.0, axis=2,
    )
    # honor the requested dt (default = engine CFL dt); the dt-sweep at RUNG-2
    # rebuilds with a halved dt — re-derive the sub-cycle at the new dt so the
    # outer step still advances one bulk dt.
    if abs(dt - eng.dt) > 1e-30:
        eng.dt = float(dt)
        eng.A.dt = float(dt)
        c_omega_max = eng.c0 / np.sqrt(eng.cL2_over_cT2 * eng.A.S_min)
        dt_cos = 0.30 * eng.dx / (c_omega_max * np.sqrt(3.0))
        eng.n_sub_cos = max(1, int(np.ceil(eng.dt / max(dt_cos, 1e-30))))
        eng.dt_sub_cos = eng.dt / eng.n_sub_cos
    return eng


def _record_box_H(eng, box, dt, n_record=60, coupled=False):
    """Advance over the FROZEN physical window T_WIN, recording the closed-box
    witness H(t) (+ its 3 components), the energy-fraction in-box (transport vs
    pump attribution), and the reactance pair (|ω|, |ω̇|) at each recorded step."""
    nsteps = int(np.ceil(T_WIN / dt))
    every = max(1, nsteps // n_record)
    t_phys, H, E_bulk, H_cos, H_c = [], [], [], [], []
    frac_in, om_max, omdot_max = [], [], []
    diverged = None
    H0_scale = abs(eng.H_witness_box(box)["H"]) + 1e-30
    for s in range(nsteps + 1):
        if s > 0:
            if coupled:
                eng.step_coupled()
            else:
                eng.B.step(dt=dt)
        if s % every == 0 or s == nsteps:
            w = eng.H_witness_box(box)
            t_phys.append(s * dt)
            H.append(w["H"]); E_bulk.append(w["E_bulk"])
            H_cos.append(w["H_cosserat"]); H_c.append(w["H_c"])
            w2 = np.sum(np.asarray(eng.B.omega) ** 2, axis=-1)
            frac_in.append(float((w2 * box).sum() / max(w2.sum(), 1e-30)))
            om_max.append(float(np.abs(eng.B.omega).max()))
            omdot_max.append(float(np.abs(eng.B.omega_dot).max()))
            if not np.isfinite(w["H"]) or abs(w["H"]) > 1e6 * H0_scale:
                diverged = s
                break
    return {"t": t_phys, "H": H, "E_bulk": E_bulk, "H_cosserat": H_cos, "H_c": H_c,
            "frac_in_box": frac_in, "omega_max": om_max, "omega_dot_max": omdot_max,
            "nsteps": nsteps, "diverged": diverged}


def _flatness(tr):
    """Drift diagnostics of a box-H trajectory: signed end-drift + peak-rise +
    OLS climb-rate, all relative to H0."""
    H = np.asarray(tr["H"], dtype=float)
    t = np.asarray(tr["t"], dtype=float)
    H0 = float(H[0]) if H.size else 0.0
    scale = max(abs(H0), 1e-30)
    drift = float((H[-1] - H0) / scale) if H.size > 1 else 0.0
    peak_rise = float((H.max() - H0) / scale) if H.size > 1 else 0.0
    rate = _ols_slope(t, H)
    return {"H0": H0, "end_drift_frac": drift, "peak_rise_frac": peak_rise,
            "climb_rate_abs": rate, "climb_rate_frac_per_T": float(rate * T_WIN / scale)}


# ── RUNG-0 — BASELINE-CLEAN ───────────────────────────────────────────────────
def _run_rung0(result, box):
    """RUNG-0: couple_off, wall_off, PML off, single grid, projection OFF, compact
    sub-yield smooth seed inside B_int. H over B_int must be FLAT to O(dt²).

    The O(dt²) gate: run at dt_base AND dt_base/2; the box-H must be flat at BOTH,
    AND any residual drift must SHRINK ~4× under dt-halving (the integrator's O(dt²)
    truncation, not a pump). A pump would NOT shrink with dt. Flat tolerance: the
    peak-rise stays below 1e-3 (a pump climbs orders of magnitude; cf Phase-22 856→8.2e9)."""
    print("\n[RUNG-0 BASELINE-CLEAN] couple_off wall_off PML-off single-grid projection-OFF "
          "sub-yield seed inside B_int — H over B_int must be FLAT to O(dt²)")
    dt0 = result["b_int_geometry"]["dt_base"]
    rows = {}
    for label, dt in (("dt_base", dt0), ("dt_half", dt0 / 2.0)):
        eng = _build_rung_engine(couple_on=False, wall_on=False, project_alive=False,
                                 coupling_support="front", with_bulk=False, dt=dt)
        # seed-containment audit: the >1%-peak ω support must be inside B_int at t0.
        w2 = np.sum(np.asarray(eng.B.omega) ** 2, axis=-1)
        seed_idx = np.argwhere(w2 > 0.01 * w2.max())
        seed_in_box = bool(box[tuple(seed_idx.T)].all())
        tr = _record_box_H(eng, box, dt, coupled=False)
        fl = _flatness(tr)
        rows[label] = {"dt": dt, "flatness": fl, "trace": tr,
                       "seed_support_in_box": seed_in_box,
                       "frac_in_box_start": tr["frac_in_box"][0],
                       "frac_in_box_end": tr["frac_in_box"][-1]}
        print(f"  {label} (dt={dt:.4e}): H0={fl['H0']:.6e}  peak-rise={fl['peak_rise_frac']:+.3e}  "
              f"end-drift={fl['end_drift_frac']:+.3e}  rate/T={fl['climb_rate_frac_per_T']:+.3e}  "
              f"frac_in_box {tr['frac_in_box'][0]:.4f}→{tr['frac_in_box'][-1]:.4f}  seed⊂box={seed_in_box}")

    pr_base = abs(rows["dt_base"]["flatness"]["peak_rise_frac"])
    pr_half = abs(rows["dt_half"]["flatness"]["peak_rise_frac"])
    FLAT_TOL = 1e-3
    flat_base = pr_base < FLAT_TOL
    flat_half = pr_half < FLAT_TOL
    # O(dt²): halving dt should cut any residual drift ~4× (ratio ≈ 4 for 2nd-order).
    # Guard the ratio when both are at machine-precision floor (0/0 → treat as clean).
    floor = 1e-12
    if pr_base < floor and pr_half < floor:
        dt2_ratio = 4.0  # both at machine precision — trivially O(dt²)-clean
        dt2_ok = True
    else:
        dt2_ratio = float(pr_base / max(pr_half, floor))
        dt2_ok = bool(dt2_ratio >= 2.0)  # at least shrinks (≥2×); ideal 4× for 2nd-order
    H_flat = bool(flat_base and flat_half)
    result["rung0"] = {
        "config": "couple_off, wall_off, PML off (pml=0), n_sub_cos=1, projection OFF, "
                  "compact sub-yield smooth ω-seed inside B_int",
        "rows": {k: {kk: vv for kk, vv in v.items() if kk != "trace"} for k, v in rows.items()},
        "trace_dt_base": rows["dt_base"]["trace"],
        "trace_dt_half": rows["dt_half"]["trace"],
        "peak_rise_dt_base": pr_base, "peak_rise_dt_half": pr_half,
        "flat_tolerance": FLAT_TOL, "H_flat_both_dt": H_flat,
        "Odt2_shrink_ratio": dt2_ratio, "Odt2_consistent": dt2_ok,
        "seed_support_in_box": rows["dt_base"]["seed_support_in_box"],
        "PASS": bool(H_flat and dt2_ok and rows["dt_base"]["seed_support_in_box"]),
        "bin_if_fail": "HARNESS-DIRTY" if not (H_flat and dt2_ok) else None,
    }
    print(f"  → RUNG-0: H_flat(both dt, <{FLAT_TOL})={H_flat}  O(dt²) shrink-ratio={dt2_ratio:.2f} "
          f"(≥2 ⇒ truncation not pump)={dt2_ok}  seed⊂box={rows['dt_base']['seed_support_in_box']}  "
          f"→ PASS={result['rung0']['PASS']}")
    if not result["rung0"]["PASS"] and result["rung0"]["bin_if_fail"] != "HARNESS-DIRTY":
        # H flat + O(dt²) ok but seed not fully in box → a geometry warning, not dirty.
        print("  ⚠ seed support not fully inside B_int — geometry warning (H still flat)")


def _run_rung1(result, box):
    """RUNG-1: identical to RUNG-0 EXCEPT projection ON (project_alive=True — the
    mid-Verlet alive-mask _zero_outside_alive / _zero_velocities_outside_alive
    applied between the two half-kicks every substep, the genesis-24 prime suspect).
    Everything else as RUNG-0. If H was FLAT at RUNG-0 but DRIFTS here → the
    projection is the pump → PROJECTION-PUMP (a fixable harness bug, isolated)."""
    print("\n[RUNG-1 +PROJECTION] same as RUNG-0 but projection ON (mid-Verlet alive-mask "
          "projection — the genesis-24 prime suspect) — does it pump H over B_int?")
    dt0 = result["b_int_geometry"]["dt_base"]
    rows = {}
    for label, dt in (("dt_base", dt0), ("dt_half", dt0 / 2.0)):
        eng = _build_rung_engine(couple_on=False, wall_on=False, project_alive=True,
                                 coupling_support="front", with_bulk=False, dt=dt)
        tr = _record_box_H(eng, box, dt, coupled=False)
        fl = _flatness(tr)
        rows[label] = {"dt": dt, "flatness": fl, "trace": tr,
                       "frac_in_box_start": tr["frac_in_box"][0],
                       "frac_in_box_end": tr["frac_in_box"][-1]}
        print(f"  {label} (dt={dt:.4e}): H0={fl['H0']:.6e}  peak-rise={fl['peak_rise_frac']:+.3e}  "
              f"end-drift={fl['end_drift_frac']:+.3e}  rate/T={fl['climb_rate_frac_per_T']:+.3e}  "
              f"frac_in_box {tr['frac_in_box'][0]:.4f}→{tr['frac_in_box'][-1]:.4f}")

    pr_base = abs(rows["dt_base"]["flatness"]["peak_rise_frac"])
    pr_half = abs(rows["dt_half"]["flatness"]["peak_rise_frac"])
    FLAT_TOL = result["rung0"]["flat_tolerance"]
    # DRIFTS = a genuine RISE above the flat tolerance that does NOT shrink like
    # transport (a projection pump injects energy; it climbs and persists). We
    # compare peak-RISE (signed up) specifically — a negative drift is transport.
    rise_base = rows["dt_base"]["flatness"]["peak_rise_frac"]
    rise_half = rows["dt_half"]["flatness"]["peak_rise_frac"]
    drifts = bool(pr_base >= FLAT_TOL or pr_half >= FLAT_TOL)
    # contrast vs RUNG-0 (which was flat): the projection is the ONLY change.
    rung0_flat = result["rung0"]["H_flat_both_dt"]
    is_projection_pump = bool(drifts and rung0_flat)
    result["rung1"] = {
        "config": "RUNG-0 config but projection ON (project_alive=True)",
        "rows": {k: {kk: vv for kk, vv in v.items() if kk != "trace"} for k, v in rows.items()},
        "trace_dt_base": rows["dt_base"]["trace"],
        "trace_dt_half": rows["dt_half"]["trace"],
        "peak_rise_dt_base": rise_base, "peak_rise_dt_half": rise_half,
        "flat_tolerance": FLAT_TOL,
        "H_drifts_with_projection": drifts,
        "rung0_was_flat": rung0_flat,
        "bin": "PROJECTION-PUMP" if is_projection_pump else None,
        "note": ("RUNG-0 flat + RUNG-1 drift ⇒ the projection is the pump (fixable). "
                 "RUNG-1 also flat ⇒ the projection is NOT the pump; the coupling read "
                 "(RUNG-2) is licensed."),
    }
    if is_projection_pump:
        print(f"  → RUNG-1: H DRIFTS with projection (peak-rise {rise_base:+.3e}) while RUNG-0 "
              f"was FLAT → PROJECTION-PUMP (the mid-Verlet mask projection is the pump)")
    else:
        print(f"  → RUNG-1: H stays FLAT with projection (peak-rise {rise_base:+.3e} < {FLAT_TOL}) "
              f"→ projection is NOT the pump; RUNG-2 (coupling read) licensed")


def _run_rung2(result, box, dt_base):
    """RUNG-2: the actual bug-vs-substrate read. Coupling on, wall off, projection
    on, supports FORCED to overlap (coupling_support='saturated_interior' so g
    overlaps Ξ at the trap interior; the 'front' shell has disjoint support and
    f_V≡0 = vacuous). A sub-yield bulk blob co-located with the ω-seed provides V.
    Sweep dt→0 over the FROZEN grid; measure the H-climb RATE (dH/dt of the box
    witness over the SAME physical window). Climb-rate → 0 as dt→0 ⇒
    INTEGRATOR-ARTIFACT (bug). Climb-rate plateaus ⇒ SUBSTRATE-PUMP (keystone
    leans negative). The dt→0 extrapolation is the decider (prereg §4: Richardson
    + OLS-intercept cross-check; thresholds FROZEN)."""
    print("\n[RUNG-2 +COUPLING FORCED-OVERLAP dt→0] coupling on, supports overlap "
          "(saturated_interior), sub-yield bulk blob — sweep dt→0, measure the H-climb RATE")
    # FROZEN dt grid: dt_base / 2^k, k = 0..N_DT−1.
    dts = [dt_base / (2.0 ** k) for k in range(N_DT)]
    sweep = []
    for k, dt in enumerate(dts):
        eng = _build_rung_engine(couple_on=True, wall_on=False, project_alive=True,
                                 coupling_support="saturated_interior", with_bulk=True, dt=dt)
        # confirm the coupling fires at this dt (overlap + f_V live).
        fV, _ = eng._coupling_forces()
        fV_max = float(np.abs(fV).max())
        ov = int(eng.coupling_support_overlap()["overlap_cells_tetrahedral"])
        tr = _record_box_H(eng, box, dt, coupled=True)
        fl = _flatness(tr)
        # COUPLE-OFF CONTROL (the decisive isolation): the SAME bulk+ω seed with the
        # coupling switched OFF. If the box-H climbed from the bulk seed's own slow
        # self-trap redistribution (NOT the cross-sector coupling), couple-OFF would
        # climb identically. The climb-rate EXCESS (ON−OFF) is the pure coupling pump.
        eng_off = _build_rung_engine(couple_on=False, wall_on=False, project_alive=True,
                                     coupling_support="saturated_interior", with_bulk=True, dt=dt)
        tr_off = _record_box_H(eng_off, box, dt, coupled=False)
        rate_off = _flatness(tr_off)["climb_rate_abs"]
        rate = fl["climb_rate_abs"]              # dH/dt over the physical window (coupling ON)
        rate_excess = float(rate - rate_off)     # the pure coupling contribution
        H0 = fl["H0"]
        row = {"k": k, "dt": dt, "n_sub_cos": eng.n_sub_cos,
               "H0": H0, "climb_rate_abs": rate,
               "climb_rate_off_abs": rate_off, "climb_rate_excess_on_minus_off": rate_excess,
               "climb_rate_frac_per_T": fl["climb_rate_frac_per_T"],
               "peak_rise_frac": fl["peak_rise_frac"], "end_drift_frac": fl["end_drift_frac"],
               "fV_max": fV_max, "overlap_cells": ov, "diverged": tr["diverged"],
               "frac_in_box_end": tr["frac_in_box"][-1],
               "omega_max_end": tr["omega_max"][-1], "omega_dot_max_end": tr["omega_dot_max"][-1],
               "trace": tr}
        sweep.append(row)
        print(f"  k={k} dt={dt:.4e} (n_sub={eng.n_sub_cos}): rate_ON={rate:+.5e}  "
              f"rate_OFF={rate_off:+.5e}  EXCESS={rate_excess:+.5e}  "
              f"f_V={fV_max:.2e} overlap={ov}  |ω|max→{tr['omega_max'][-1]:.3e}  div={tr['diverged']}")

    # ── dt→0 extrapolation (prereg §4) ── on the EXCESS (ON−OFF) climb-rate = the
    #    pure coupling pump, isolated from the bulk seed's own (couple-OFF) dynamics.
    dts_arr = np.array([r["dt"] for r in sweep])
    rates = np.array([r["climb_rate_excess_on_minus_off"] for r in sweep])
    rates_on = np.array([r["climb_rate_abs"] for r in sweep])
    R0 = float(rates[0])
    # Richardson (primary): from the two FINEST dt (k=N_DT−1, k=N_DT−2), linear-in-dt
    # extrapolation to dt=0:  R∞ ≈ R_fine − (R_coarse − R_fine)·dt_fine/(dt_coarse − dt_fine).
    dt_fine, dt_coarse = dts_arr[-1], dts_arr[-2]
    R_fine, R_coarse = rates[-1], rates[-2]
    if abs(dt_coarse - dt_fine) > 1e-30:
        R_inf_rich = float(R_fine - (R_coarse - R_fine) * dt_fine / (dt_coarse - dt_fine))
    else:
        R_inf_rich = float(R_fine)
    # OLS cross-check (secondary): intercept of rate-vs-dt line over all points.
    if dts_arr.size >= 2:
        A = np.vstack([dts_arr, np.ones_like(dts_arr)]).T
        slope_ols, intercept_ols = np.linalg.lstsq(A, rates, rcond=None)[0]
        R_inf_ols = float(intercept_ols)
    else:
        R_inf_ols = float(R_fine)
    # the extrapolation uncertainty = spread between the two intercept estimates.
    delta = abs(R_inf_rich - R_inf_ols)
    R_inf = R_inf_rich                          # Richardson is primary
    ratio_inf = abs(R_inf) / max(abs(R0), 1e-30)
    # monotone-decreasing |R_k| in k (each halving cuts the rate)?
    abs_rates = np.abs(rates)
    monotone_decr = bool(np.all(np.diff(abs_rates) <= 1e-30 * max(abs(R0), 1e-30) + 1e-15) or
                         np.all(np.diff(abs_rates) < 0))
    # finest-two agreement (do the two finest dt agree on a finite plateau?)
    finest_spread = abs(abs_rates[-1] - abs_rates[-2]) / max(abs_rates[-1], 1e-30)

    # ── FROZEN decision (prereg §4) ──
    THRESH = 0.10
    agree_sign = bool(np.sign(R_inf_rich) == np.sign(R_inf_ols) or
                      (abs(R_inf_rich) < 1e-12 and abs(R_inf_ols) < 1e-12))
    ambiguous = bool(delta > abs(R_inf) and abs(R_inf) > 1e-12)
    if ratio_inf < THRESH and monotone_decr:
        bin_ = "INTEGRATOR-ARTIFACT"
        reason = (f"RUNG-2 coupling H-climb-rate EXCESS (ON−OFF) → 0 as dt→0 (|R∞|/|R0|="
                  f"{ratio_inf:.3e} < {THRESH}, |R_k| monotone-decreasing) — a fixable "
                  f"integrator/coupling discretization artifact. The keystone stays OPEN (fix the "
                  f"discrete coupling time-centering, re-test loop-closure).")
    elif ratio_inf >= THRESH:
        bin_ = "SUBSTRATE-PUMP"
        reason = (f"RUNG-2 coupling H-climb-rate EXCESS (ON−OFF) PLATEAUS at a finite value as "
                  f"dt→0 (|R∞|/|R0|={ratio_inf:.3e} ≥ {THRESH}; the continuum coupling pumps even "
                  f"at dt→0, isolated from the couple-OFF bulk dynamics) — the keystone leans "
                  f"NEGATIVE (a free precursor cannot losslessly close the energize-LOCK loop).")
    else:
        # ratio < THRESH but NOT monotone — ambiguous shrink pattern; report, do not force.
        bin_ = "INTEGRATOR-ARTIFACT"
        reason = (f"RUNG-2 coupling H-climb-rate EXCESS decreases toward 0 (|R∞|/|R0|="
                  f"{ratio_inf:.3e} < {THRESH}) but the |R_k| sequence is non-monotone — leans "
                  f"integrator-artifact; flagged for auditor re-check of the fit.")
    if ambiguous:
        reason += (f" ⚠ FIT-AMBIGUOUS: Richardson/OLS intercepts disagree by Δ={delta:.3e} "
                   f"> |R∞|={abs(R_inf):.3e} — auditor must re-check the dt→0 fit.")

    result["rung2"] = {
        "config": "couple_on=True, wall_off, projection ON, coupling_support="
                  "'saturated_interior' (FORCED-OVERLAP), sub-yield co-located bulk blob",
        "dt_grid": dts,
        "sweep": [{kk: vv for kk, vv in r.items() if kk != "trace"} for r in sweep],
        "traces": {f"k{r['k']}": r["trace"] for r in sweep},
        "climb_rates_excess_on_minus_off": rates.tolist(),
        "climb_rates_on": rates_on.tolist(),
        "decision_basis": "EXCESS (coupling ON − coupling OFF) climb-rate — isolates "
                          "the pure cross-sector coupling pump from the bulk seed's own "
                          "(couple-OFF) self-trap redistribution",
        "R0": R0,
        "dt_to_zero": {
            "R_inf_richardson": R_inf_rich, "R_inf_ols": R_inf_ols,
            "R_inf": R_inf, "ratio_R_inf_over_R0": ratio_inf,
            "extrapolation_uncertainty_delta": delta,
            "richardson_ols_sign_agree": agree_sign,
            "abs_rates_monotone_decreasing": monotone_decr,
            "finest_two_spread_frac": finest_spread,
            "fit_ambiguous": ambiguous,
        },
        "threshold": THRESH,
        "bin": bin_, "reason": reason,
    }
    print(f"  → dt→0: R0={R0:+.5e}  R∞(Rich)={R_inf_rich:+.5e}  R∞(OLS)={R_inf_ols:+.5e}  "
          f"|R∞|/|R0|={ratio_inf:.3e}  Δ={delta:.3e}  monotone↓={monotone_decr}  sign-agree={agree_sign}")
    print(f"  → RUNG-2 BIN: {bin_}")


if __name__ == "__main__":
    main()
