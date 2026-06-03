"""
alpha_chiral_dressing_chisweep_scoped.py -- SCOPED, KILL-SAFE re-run of the
alpha Class-2 lift Test 4 (chiral Meissner dressing) chi-SWEEP to COMPLETION.

WHY THIS HARNESS EXISTS
-----------------------
alpha_chiral_dressing_test.py::main() runs THREE expensive phases (the full
(R,r) landscape prong + the LH hand-flip + the chi-sweep) = ~77 eigensolves and
writes its JSON only at the very end (line ~1518). Its prior run was KILLED at
1/20 of the FULL-GRID prong, leaving NO persisted chi-vs-R/r curve.

This harness imports the COMMITTED driver's machinery UNCHANGED (build_step_
operator, chiral_z_local_from_seed, eig_near_thetaC, _select_modes, the AST
alpha-guard, the canonical-source check) and runs ONLY the chi-sweep, scoped per
the brief, writing the results JSON INCREMENTALLY after every single (seed, chi)
point so a kill preserves all partials. NO physics is altered: every eigensolve
goes through the exact committed build_step_operator + eig_near_thetaC.

SCOPE (per the re-run brief)
----------------------------
  Seeds (3):     R/r in {2.0, 2.8, 4.0}  (straddling phi^2 = 2.618).
  chi-sweep (7): {0, 0.001, 0.00875682(=1.2*alpha), 0.03, 0.1, 0.3, 0.9}.
  N_LATTICE:     24 (q=3 resolution; the Test-3-validated floor). NOT reduced.
  Measure:       the dressed BOUND-eigenmode R/r in the K4 V-tank (V_inc,V_ref)
                 phasor plane -- NOT the (0,0) red-herring mode.
  Guards reused: AST alpha-guard, canonical-source, PML-excluded interior-only
                 measures, forward-not-fit, V-tank coordinate -- all inherited
                 from the committed module (this harness adds none, weakens none).

KILL-SAFETY
-----------
After EACH (seed, chi) eigensolve the full partial results dict is re-serialised
to alpha_chiral_dressing_chisweep_scoped_results.json. A kill at point k leaves
points 0..k-1 fully on disk with the verdict-so-far recomputed from whatever is
complete.

Branch: analysis/alpha-chiral-dressing (do NOT merge).
"""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))

import importlib.util  # noqa: E402

# --- Import the COMMITTED driver module unchanged (machinery reuse) ---
_DRIVER = Path(__file__).resolve().parent / "alpha_chiral_dressing_test.py"
_spec = importlib.util.spec_from_file_location("alpha_chiral_dressing_test", _DRIVER)
acdt = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(acdt)

# ======================================================================
# SCOPED CONFIG (the ONLY deviation from the committed module: the sweep
# SETS, not the physics). N_LATTICE stays 24. The committed module's
# build/eigensolve/measure/guard functions are used verbatim.
# ======================================================================
# Brief chi-sweep: physical chi (=1.2*alpha=KAPPA_CHIRAL_ELECTRON) at index 2.
SCOPED_CHI_SWEEP = (
    0.0,
    0.001,
    float(acdt.KAPPA_CHIRAL_ELECTRON),  # 0.00875682... = 1.2*alpha (PHYSICAL)
    0.03,
    0.1,
    0.3,
    0.9,
)
SCOPED_CHI_PHYSICAL_INDEX = 2

# Brief seeds: R/r in {2.0, 2.8, 4.0}. Reuse the committed R_MAJOR_SWEEP scale
# (major radii in cells) so the (R, r) geometry is identical to the committed
# driver's; only the ratio subset is scoped. R chosen so r = R/ratio resolves
# q=3 (r >= ~2 cells): R=6 -> r in {3.0, 2.14, 1.5}; we lift R for the 4.0 ratio
# to keep r >= 2 (R=8 -> r=2.0 at ratio 4.0).
SCOPED_SEEDS = (
    (6.0, 6.0 / 2.0),  # R/r_seed = 2.0  -> r = 3.00
    (6.0, 6.0 / 2.8),  # R/r_seed = 2.8  -> r = 2.14  (straddles phi^2)
    (8.0, 8.0 / 4.0),  # R/r_seed = 4.0  -> r = 2.00  (R lifted to keep r>=2)
)
# Drop-to-2-seeds fallback (brief): if a soft wall-clock budget is exceeded, the
# 2.8 (middle) seed is skipped and only {2.0, 4.0} are run. Controlled by env.
import os  # noqa: E402

_DROP_TO_2 = os.environ.get("CHISWEEP_DROP_TO_2", "0") == "1"
if _DROP_TO_2:
    SCOPED_SEEDS = (SCOPED_SEEDS[0], SCOPED_SEEDS[2])  # {2.0, 4.0}

PHI_SQ = acdt.PHI_SQ_TARGET  # 2.6180339887 -- read-side comparison constant ONLY.
BAND = acdt.ASPECT_BAND      # 0.20 fractional band around phi^2 (committed value,
#                              used for the headline near-phi^2 test, unchanged).
# PLATEAU/CROSSING band (KEEP-BOTH axis, NOT a redefinition of BAND): the +/-20%
# BAND spans [2.094, 3.142], whose LOWER RAIL (~2.094) a generic seed parked at
# R/r~2.1 clears by edge-effect WITHOUT being anywhere near phi^2=2.618 -- so the
# wide band gives a FALSE "in-band/plateau" read for a curve that merely sits at
# ~2.1 and trends DOWN. The plateau / phi^2-reaching question ("does R/r genuinely
# climb to phi^2") demands a TIGHTER, symmetric proximity: +/-10% -> [2.356, 2.880],
# which a bottom-rail ~2.1 fails decisively. BAND (the committed +/-20% headline
# test) is left untouched for audit continuity; PLATEAU_BAND is the added axis.
PLATEAU_BAND = 0.10

_OUT = Path(__file__).resolve().parent / "alpha_chiral_dressing_chisweep_scoped_results.json"


def _phi2_crossing(chis: list[float], aspects: list[float]) -> dict:
    """Where (if anywhere) R/r(chi) GENUINELY reaches phi^2. 'reaches' uses the
    TIGHT PLATEAU_BAND (+/-10% -> [2.356, 2.880]) so a bottom-rail ~2.1 that only
    clears the wide +/-20% lower edge does NOT count as reaching phi^2. Also reports
    a linear-interp crossing chi if R/r passes THROUGH phi^2 exactly between two
    swept points. Pure read-side comparison to the numeric 2.618 (no phi imported
    into any measure). Both bands reported so the distinction is auditable."""
    in_tight = [c for c, a in zip(chis, aspects) if a is not None and abs(a - PHI_SQ) <= PLATEAU_BAND * PHI_SQ]
    in_wide = [c for c, a in zip(chis, aspects) if a is not None and abs(a - PHI_SQ) <= BAND * PHI_SQ]
    cross_chi = None
    for (c0, a0), (c1, a1) in zip(zip(chis, aspects), list(zip(chis, aspects))[1:]):
        if a0 is None or a1 is None:
            continue
        if (a0 - PHI_SQ) * (a1 - PHI_SQ) < 0:  # straddles phi^2 exactly
            frac = (PHI_SQ - a0) / (a1 - a0)
            cross_chi = float(c0 + frac * (c1 - c0))
            break
    return {
        "reaches_phi2_within_band": bool(in_tight),  # TIGHT (+/-10%): genuine reach
        "first_in_band_chi": float(min(in_tight)) if in_tight else None,
        "in_wide_band_only": bool(in_wide and not in_tight),  # FLAG: wide-band edge artifact
        "interp_crossing_chi": cross_chi,
        "plateau_band_frac": PLATEAU_BAND,
        "wide_band_frac": BAND,
        "phi2": PHI_SQ,
    }


def _converge_or_shift(per_seed: list[dict]) -> dict:
    """Across seeds: at the PHYSICAL chi, do the dressed bound-mode R/r values
    CONVERGE (selection -- the dressing pulls disparate seeds toward one aspect)
    or SHIFT independently (no selection -- each seed keeps ~ its own R/r)? Read
    by comparing the spread of dressed-bound R/r at physical chi to the spread of
    the BARE (achiral) baselines: convergence => dressed spread << bare spread."""
    phys_vals = []
    bare_vals = []
    seed_ratios = []
    for ps in per_seed:
        seed_ratios.append(ps["R_over_r_seed"])
        if ps.get("bare_aspect") is not None:
            bare_vals.append(ps["bare_aspect"])
        for rec in ps["sweep"]:
            if rec["is_physical_chi"] and rec["R_over_r_phase_bound"] is not None:
                phys_vals.append(rec["R_over_r_phase_bound"])
    if len(phys_vals) < 2:
        return {"verdict": "insufficient", "n_seeds_at_physical": len(phys_vals)}
    phys = np.asarray(phys_vals)
    bare = np.asarray(bare_vals) if bare_vals else None
    phys_spread = float(phys.max() - phys.min())
    bare_spread = float(bare.max() - bare.min()) if bare is not None and bare.size >= 2 else None
    # CONVERGE if the dressed-at-physical spread collapses well below both the
    # seed-ratio spread AND the bare-baseline spread (the dressing erased the
    # seed dependence). SHIFT if the dressed spread tracks the seed spread.
    seed_spread = float(max(seed_ratios) - min(seed_ratios))
    converged = bool(
        phys_spread < 0.25 * seed_spread
        and (bare_spread is None or phys_spread < 0.5 * bare_spread)
    )
    return {
        "verdict": "CONVERGE (selection)" if converged else "SHIFT independently (no selection)",
        "converged": converged,
        "dressed_physical_R_over_r": [float(v) for v in phys_vals],
        "dressed_physical_spread": phys_spread,
        "bare_baseline_R_over_r": [float(v) for v in bare_vals] if bare_vals else None,
        "bare_baseline_spread": bare_spread,
        "seed_ratio_spread": seed_spread,
    }


def _interim_verdict(per_seed: list[dict]) -> dict:
    """Map the scoped curve -> A / FLAT-SMALL / CLOSE (recomputed after every
    point so the persisted JSON always carries a verdict-so-far). Logic mirrors
    the committed adjudicate(): physical-chi proximity to phi^2 + plateau across
    chi + the converge/shift selection read. Forward-not-fit."""
    # chiral increment per seed: R/r at physical chi MINUS R/r at chi=0 (bound mode).
    increments = []
    physical_aspects = []
    plateau_seeds = 0
    crossings = []
    for ps in per_seed:
        chis = [r["chi"] for r in ps["sweep"]]
        asp = [r["R_over_r_phase_bound"] for r in ps["sweep"]]
        val0 = next((a for c, a in zip(chis, asp) if abs(c) < 1e-15 and a is not None), None)
        valp = next((r["R_over_r_phase_bound"] for r in ps["sweep"] if r["is_physical_chi"] and r["R_over_r_phase_bound"] is not None), None)
        if val0 is not None and valp is not None:
            increments.append(valp - val0)
        if valp is not None:
            physical_aspects.append(valp)
        cr = _phi2_crossing(chis, asp)
        crossings.append({"R_over_r_seed": ps["R_over_r_seed"], **cr})
        # plateau: >=3 distinct chi GENUINELY near phi^2 (TIGHT PLATEAU_BAND, NOT the
        # wide +/-20% band whose lower rail a ~2.1 seed clears by edge-effect)
        # spanning >= 1 decade. Using the wide band here gave a FALSE 2/2 plateau for
        # a curve sitting at ~2.1 and trending DOWN -- corrected to PLATEAU_BAND.
        in_band_chi = [c for c, a in zip(chis, asp) if a is not None and abs(a - PHI_SQ) <= PLATEAU_BAND * PHI_SQ]
        nz = [c for c in in_band_chi if c > 0]
        if len(in_band_chi) >= 3 and nz and (max(nz) / min(nz) >= 10.0):
            plateau_seeds += 1
    incr_mean = float(np.mean(increments)) if increments else float("nan")
    phys_mean = float(np.mean(physical_aspects)) if physical_aspects else float("nan")
    n_seeds = max(len(per_seed), 1)
    has_plateau = plateau_seeds >= max(1, n_seeds // 2)
    selects_aspect = bool(np.isfinite(incr_mean) and abs(incr_mean) > 0.05 * PHI_SQ)
    # physical_near_phi2 uses the TIGHT PLATEAU_BAND: a physical-chi R/r of ~2.15 is
    # 17-19% BELOW phi^2=2.618 -- it must NOT register as "near phi^2" via the wide
    # band's lower edge. (The headline FLAT/SMALL verdict is gated by selects_aspect,
    # which is already correct; this tightening keeps the sub-diagnostic honest.)
    physical_near_phi2 = bool(np.isfinite(phys_mean) and abs(phys_mean - PHI_SQ) <= PLATEAU_BAND * PHI_SQ)

    if not selects_aspect:
        outcome = "FLAT/SMALL"
        reason = (
            f"CLOSE (FLAT/SMALL): the chiral coupling's increment on R/r as chi 0->physical(1.2*alpha) "
            f"is {incr_mean:+.5f} (bound-mode, mean over seeds) -- O(alpha)-small, far below the "
            f"{0.05 * PHI_SQ:.3f} needed to move a generic ~2 seed toward phi^2={PHI_SQ:.4f}. Physical "
            f"chirality is too weak to select the aspect; phi^2 would have to rest on R*r=1/4."
        )
    elif physical_near_phi2 and has_plateau:
        outcome = "A"
        reason = (
            f"LIFT LANDS (A): dressed bound-mode R/r reaches phi^2={PHI_SQ:.4f} at the PHYSICAL chi "
            f"(mean {phys_mean:.4f}) AND a phi^2 plateau spans >= 1 decade of chi in {plateau_seeds}/{n_seeds} "
            f"seeds -> topology-set (alpha-free). Check converge-vs-shift to confirm selection."
        )
    elif physical_near_phi2:
        outcome = "A (physical-only)"
        reason = (
            f"phi^2 reached at the physical chi (mean {phys_mean:.4f}) but NO decade-spanning plateau "
            f"({plateau_seeds}/{n_seeds}) -> phi^2 tied to the specific alpha-injected coupling, not the "
            f"(2,3) topology. Treat as alpha-INJECTED (circular) unless nearby-chi robustness holds."
        )
    else:
        # selects an aspect but not phi^2 at physical chi: only reaches phi^2 (if at all) at chi >> physical.
        any_band = any(c["reaches_phi2_within_band"] for c in crossings)
        if any_band:
            outcome = "FLAT/SMALL (CLOSE)"
            reason = (
                f"CLOSE (FLAT/SMALL): R/r reaches phi^2 ONLY at chi >> 1.2*alpha (physical-chi mean "
                f"{phys_mean:.4f} not in band); physical chirality too weak -> phi^2 needs unphysical "
                f"coupling -> rests on R*r=1/4."
            )
        else:
            outcome = "CLOSE"
            reason = (
                f"CLOSE: dressed R/r never reaches phi^2={PHI_SQ:.4f} anywhere in the scoped chi-sweep "
                f"(physical-chi mean {phys_mean:.4f}); the chiral dressing does not select phi^2."
            )

    return {
        "outcome": outcome,
        "reason": reason,
        "selects_aspect": selects_aspect,
        "chiral_increment_mean_bound": incr_mean,
        "physical_chi_mean_R_over_r": phys_mean,
        "has_plateau": has_plateau,
        "plateau_seeds": plateau_seeds,
        "per_seed_phi2_crossing": crossings,
        "converge_or_shift": _converge_or_shift(per_seed),
    }


def _persist(per_seed, started, finished, points_done, points_total, note=""):
    """Re-serialise the full partial state. Called after EVERY point (kill-safe)."""
    payload = {
        "harness": "alpha_chiral_dressing_chisweep_scoped",
        "driver_reused": str(_DRIVER.name),
        "driver_head_note": "machinery imported unchanged from committed alpha_chiral_dressing_test.py",
        "complete": points_done == points_total,
        "points_done": points_done,
        "points_total": points_total,
        "wall_seconds_so_far": round(time.time() - started, 1),
        "config": {
            "N_LATTICE": acdt.N_LATTICE,
            "PML": acdt.PML,
            "SCOPED_CHI_SWEEP": list(SCOPED_CHI_SWEEP),
            "SCOPED_CHI_PHYSICAL_INDEX": SCOPED_CHI_PHYSICAL_INDEX,
            "SCOPED_SEEDS_R_r": [[float(R), float(r)] for (R, r) in SCOPED_SEEDS],
            "KAPPA_CHIRAL_ELECTRON": float(acdt.KAPPA_CHIRAL_ELECTRON),
            "KAPPA_TILDE_ELECTRON": float(acdt.KAPPA_TILDE_ELECTRON),
            "SEED_AMPLITUDE_FRAC": acdt.SEED_AMPLITUDE_FRAC,
            "THETA_C": acdt.THETA_C,
            "PHI_SQ_TARGET": PHI_SQ,
            "ASPECT_BAND": BAND,
            "handedness": "RH",
            "dropped_to_2_seeds": _DROP_TO_2,
        },
        "per_seed": per_seed,
        "interim_verdict": _interim_verdict(per_seed) if per_seed else None,
        "note": note,
    }
    with open(_OUT, "w") as f:
        json.dump(payload, f, indent=2, default=lambda o: float(o) if isinstance(o, np.floating) else str(o))


def main() -> dict:
    started = time.time()
    print("=" * 78, flush=True)
    print("  alpha Class-2 lift Test 4 -- CHIRAL dressing chi-SWEEP (SCOPED, KILL-SAFE)")
    print(f"  N_interior={acdt.N_LATTICE}  PML={acdt.PML}  theta_C=1/sqrt(2) (ALPHA-FREE)")
    print(f"  Seeds R/r: {[round(R / r, 2) for (R, r) in SCOPED_SEEDS]}   chi-sweep: {SCOPED_CHI_SWEEP}")
    print(f"  Physical chi = KAPPA_CHIRAL_ELECTRON = {acdt.KAPPA_CHIRAL_ELECTRON:.8f} (=1.2*alpha, index {SCOPED_CHI_PHYSICAL_INDEX})")
    print("  Measure: dressed BOUND-eigenmode R/r in K4 V-tank (V_inc,V_ref) plane (NOT the (0,0) mode)")
    print("=" * 78, flush=True)

    # --- Inherited guards (unchanged from the committed module) ---
    acdt._self_audit_no_forbidden_tokens()
    acdt._verify_canonical_source()
    print(flush=True)

    points_total = len(SCOPED_SEEDS) * len(SCOPED_CHI_SWEEP)
    points_done = 0
    per_seed: list[dict] = []
    _persist(per_seed, started, False, points_done, points_total, note="run started")

    amp = acdt.SEED_AMPLITUDE_FRAC
    for (R, r) in SCOPED_SEEDS:
        ratio = R / r
        print(f"-- seed R={R:.1f} r={r:.2f} (R/r_seed={ratio:.2f}) --", flush=True)
        ps: dict = {"R": float(R), "r": float(r), "R_over_r_seed": float(ratio), "bare_aspect": None, "sweep": []}

        # Achiral (BARE) baseline once at this seed (chi-independent; bare matrix
        # is (N,PML)-cached inside build_step_operator across seeds).
        t = time.time()
        Mb, tb = acdt.build_step_operator(R, r, amp, dressed=False, chi=0.0, handedness="RH")
        vb, evb = acdt.eig_near_thetaC(Mb, n_eigs=acdt.N_EIGS)
        selb = acdt._select_modes(vb, evb, tb, R_major=R)
        if selb["most_bound"] is not None:
            ps["bare_aspect"] = float(selb["most_bound"]["R_over_r_phase"])
        print(f"   [bare baseline R/r = {ps['bare_aspect']}]  ({time.time() - t:.1f}s)", flush=True)
        per_seed.append(ps)
        _persist(per_seed, started, False, points_done, points_total, note="bare baseline done")

        for chi in SCOPED_CHI_SWEEP:
            t = time.time()
            M, template = acdt.build_step_operator(R, r, amp, dressed=True, chi=chi, handedness="RH")
            vals, vecs = acdt.eig_near_thetaC(M, n_eigs=acdt.N_EIGS)
            sel = acdt._select_modes(vals, vecs, template, R_major=R)
            d = sel["most_bound"]   # the dressed BOUND eigenmode (NOT (0,0))
            d23 = sel["best_2_3"]
            is_phys = bool(abs(chi - acdt.KAPPA_CHIRAL_ELECTRON) < 1e-9)
            rec = {
                "chi": float(chi),
                "is_physical_chi": is_phys,
                "R_over_r_phase_bound": float(d["R_over_r_phase"]) if d else None,
                "R_over_r_phase_2_3": float(d23["R_over_r_phase"]) if d23 else None,
                "localization_bound": float(d["localization"]) if d else None,
                "lambda_mod_bound": float(d["lambda_mod"]) if d else None,
                "theta_bound": float(d["theta"]) if d else None,
                "pq_bound": (int(d["p_major"]), int(d["q_minor"])) if d else None,
                "pq_2_3": (int(d23["p_major"]), int(d23["q_minor"])) if d23 else None,
                "n_in_band": int(sel["n_in_band"]),
                "wall_s": round(time.time() - t, 1),
            }
            ps["sweep"].append(rec)
            points_done += 1
            _persist(per_seed, started, False, points_done, points_total,
                     note=f"point {points_done}/{points_total}")
            ar = f"{rec['R_over_r_phase_bound']:.4f}" if rec["R_over_r_phase_bound"] is not None else "OOB"
            tag = "  <-- PHYSICAL chi=1.2*alpha" if is_phys else ""
            print(
                f"   chi={chi:.6f}: R/r_bound={ar}  loc={rec['localization_bound']}  "
                f"|lam|={rec['lambda_mod_bound']}  n_band={rec['n_in_band']}  ({rec['wall_s']}s){tag}",
                flush=True,
            )

    finished = time.time()
    _persist(per_seed, started, finished, points_done, points_total, note="COMPLETE")

    # --- Final curve + verdict to stdout ---
    verdict = _interim_verdict(per_seed)
    print(flush=True)
    print("=" * 78, flush=True)
    print("  SCOPED chi-SWEEP COMPLETE -- R/r-vs-chi curve (dressed BOUND mode)")
    print("=" * 78, flush=True)
    for ps in per_seed:
        print(f"  seed R/r={ps['R_over_r_seed']:.2f} (R={ps['R']:.1f}, r={ps['r']:.2f})  "
              f"bare={ps['bare_aspect']}", flush=True)
        for rec in ps["sweep"]:
            ar = f"{rec['R_over_r_phase_bound']:.4f}" if rec["R_over_r_phase_bound"] is not None else "OOB"
            tag = "  *PHYSICAL(1.2a)" if rec["is_physical_chi"] else ""
            print(f"      chi={rec['chi']:.6f}  R/r={ar}{tag}", flush=True)
    print(flush=True)
    print(f"  VERDICT: {verdict['outcome']}", flush=True)
    print(f"  {verdict['reason']}", flush=True)
    print(f"  chiral increment (R/r, chi:0->physical, bound, mean over seeds): "
          f"{verdict['chiral_increment_mean_bound']:+.5f}", flush=True)
    print(f"  physical-chi mean R/r = {verdict['physical_chi_mean_R_over_r']:.4f}  [phi^2={PHI_SQ:.4f}]", flush=True)
    print(f"  phi^2 plateau seeds: {verdict['plateau_seeds']}/{len(per_seed)}  -> "
          f"{'TOPOLOGY-SET (alpha-free)' if verdict['has_plateau'] else 'no robust plateau'}", flush=True)
    cs = verdict["converge_or_shift"]
    print(f"  converge-or-shift: {cs['verdict']}", flush=True)
    if cs.get("dressed_physical_R_over_r"):
        print(f"      dressed@physical R/r per seed = {[round(v,4) for v in cs['dressed_physical_R_over_r']]} "
              f"(spread {cs['dressed_physical_spread']:.4f})", flush=True)
        if cs.get("bare_baseline_R_over_r"):
            print(f"      bare baseline    R/r per seed = {[round(v,4) for v in cs['bare_baseline_R_over_r']]} "
                  f"(spread {cs['bare_baseline_spread']:.4f})", flush=True)
    for c in verdict["per_seed_phi2_crossing"]:
        bandc = c["first_in_band_chi"]
        interp = c["interp_crossing_chi"]
        msg = (
            f"reaches phi^2-band first at chi={bandc:.6f}" if bandc is not None
            else "NEVER reaches phi^2-band"
        )
        if interp is not None:
            msg += f" (interp crossing chi={interp:.6f})"
        print(f"      seed R/r={c['R_over_r_seed']:.2f}: {msg}", flush=True)
    print(flush=True)
    print(f"  wall time: {finished - started:.1f}s", flush=True)
    print(f"  [results] {_OUT.name}", flush=True)
    return {"per_seed": per_seed, "verdict": verdict}


if __name__ == "__main__":
    main()
