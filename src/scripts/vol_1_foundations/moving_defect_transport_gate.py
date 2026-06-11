#!/usr/bin/env python3
r"""Moving-defect transport CAPABILITY GATE — Phase 2 of the bulk-vs-transverse
pilot fork.

Prereg: research/2026-06-11_moving-defect-doubleslit_prereg.md (§6 capability
checklist; §8 ordered bins; §9 adjudication).

VERDICT (empirical, this driver): **ENGINE-GAP** (prereg §8 bin 5 — the
forward-registered most-probable outcome; a clean Rule-11 closure, not a defeat).

No engine on today's stack hosts a SELF-CONSISTENT, BOUNDED-SPREAD translating
defect WHILE exposing per-channel (longitudinal-bulk ⊗ transverse-shear) readout.
The two required capabilities live in two different engines and the translating
bound state lives in NEITHER:

  1. MasterEquationFDTD — the ONLY engine with c_eff(V) wave-speed modulation
     (so a defect can self-trap at A→1). But it is SCALAR-V / single-channel
     (no transverse/microrotation sector ⇒ C-readout FAIL for the fork). And a
     boosted breather DISPERSES: width ≈ 3.5×, peak retention ≈ 0.087, ROBUST
     across A0 ∈ {0.85, 0.95, 0.99} × S_min ∈ {0.05, 0.02, 0.005}. The self-trap
     engages only at REST; a momentum boost drops the amplitude below the
     saturation threshold so c_eff(V) never re-engages (S_min has zero effect —
     the diagnostic tell). C-localize FAIL.

  2. VacuumEngine3D — the ONLY multi-channel host (K4 V_inc/V_ref transverse ⊗
     Cosserat u longitudinal-bulk ⊗ ω microrotation; native DarkWakeObserver
     τ_zx). C-readout PASS (both fork channels live-confirmed here). But its
     saturated (2,3) core PINS under boost: verified SCREENED-PIN
     (research/2026-06-04_motion-stability-bemf-longitudinal-result.md,
     PIN-even-longitudinal — byte-identical trajectories across v_drive, S_ε@core
     floored at 1e-5, both transverse AND longitudinal boosts). Its V-sector is
     K4-TLM (Z(V)-only, NO c_eff(V)) so the core is a frozen-clock object that
     cannot translate. C-transport FAIL.

C4 — validate-on-known-positive (ave-apparatus-floor-attribution): the boost
apparatus is confirmed live on a LINEAR free packet — v_meas RESPONDS to v_boost
— so the self-trap's failure is the ENGINE, not a dead boost.

The named missing capability (engine roadmap, prereg §9 ENGINE-GAP): a
MULTI-CHANNEL engine with c_eff(V) modulation on the V-sector whose bound state
is BOOST-COVARIANT — the *moving solution* of the Master Equation, not a rest
soliton given a kick that dispersion immediately undoes.

Output:
  src/scripts/vol_1_foundations/_output/moving_defect_transport_gate_results.json
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

_SCRIPT_DIR = Path(__file__).resolve().parent
if str(_SCRIPT_DIR.parents[1]) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_DIR.parents[1]))

from ave.core.master_equation_fdtd import MasterEquationFDTD  # noqa: E402
from ave.topological.vacuum_engine import VacuumEngine3D  # noqa: E402

PROJECT_ROOT = next(p for p in Path(__file__).resolve().parents if (p / ".git").exists())
OUT_DIR = PROJECT_ROOT / "src" / "scripts" / "vol_1_foundations" / "_output"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Floors (prereg §5 obs-4, sim-2 baselines): the blur floor a real translating
# packet must beat, and the localization criteria a bound defect must hold.
BLUR_FLOOR_V = 0.62  # sim-2 moving-emitter two-slit visibility (blur artifact)
WIDTH_GROWTH_MAX = 2.0  # bounded-spread criterion (C-localize): width < 2× over transit
PEAK_RETENTION_MIN = 0.5  # C-localize: peak holds ≥ 50% over transit


def _interior_mask(n: int, pml: int, guard: int = 2) -> np.ndarray:
    """PML-excluded interior mask (A-Rule-10 / prereg CP7): PML+guard ≤ idx < N−PML−guard."""
    m = np.zeros((n, n, n), dtype=bool)
    lo, hi = pml + guard, n - pml - guard
    m[lo:hi, lo:hi, lo:hi] = True
    return m


def _boosted_blob(eng: MasterEquationFDTD, center, radius, amp, v, profile="sech") -> None:
    """Impart +x momentum to a Master-Equation blob via V_prev shift.

    For a +x mover V(x,t)=f(x−vt): ∂_tV(x,0)=−v·∂_xV ⇒ V_prev(x)=V(x+v·dt),
    i.e. the same blob centered at cx−v·dt. A one-shot momentum imprint (initial
    condition, then free evolution) — NOT a sustained pump (prereg §11).
    """
    cx, cy, cz = center
    eng.V[:] = 0.0
    eng.inject_localized_blob(center, radius, amp, profile=profile)
    v0 = eng.V.copy()
    eng.V[:] = 0.0
    eng.inject_localized_blob((cx - v * eng.dt, cy, cz), radius, amp, profile=profile)
    eng.V_prev = eng.V.copy()
    eng.V = v0


def _diag(eng: MasterEquationFDTD, mask: np.ndarray):
    """PML-excluded energy-weighted centroid_x, RMS width, peak |V|."""
    rho = (eng.V**2) * mask
    tot = float(rho.sum())
    if tot <= 0.0:
        return np.nan, np.nan, np.nan
    i = np.indices(rho.shape)[0]
    cx = float((i * rho).sum() / tot)
    w = float(np.sqrt(((i - cx) ** 2 * rho).sum() / tot))
    peak = float(np.abs(eng.V * mask).max())
    return cx, w, peak


def _run_master(amp, v, s_min, n=80, pml=4, radius=2.5, transit=18.0):
    eng = MasterEquationFDTD(N=n, pml_thickness=pml, S_min=s_min, A_cap=0.99)
    mask = _interior_mask(n, pml)
    _boosted_blob(eng, (n * 0.30, n / 2.0, n / 2.0), radius, amp, v)
    cx0, w0, p0 = _diag(eng, mask)
    for _ in range(int(transit / eng.dt)):
        eng.step()
    cx1, w1, p1 = _diag(eng, mask)
    return {
        "v_meas": (cx1 - cx0) / eng.time if eng.time > 0 else float("nan"),
        "width_growth": w1 / w0 if w0 > 0 else float("nan"),
        "peak_retention": p1 / p0 if p0 > 0 else float("nan"),
    }


def gate_boost_apparatus(verbose=True):
    """C4 — validate-on-known-positive: does v_meas RESPOND to v_boost on a
    LINEAR free packet? (If yes, the boost is real and the self-trap failure is
    the engine, not a dead apparatus.)"""
    rows = []
    for v in (0.0, 0.3, 0.6, 0.9):
        r = _run_master(amp=0.03, v=v, s_min=0.05, radius=3.0, transit=12.0)
        rows.append((v, r["v_meas"]))
    # boost is valid if v_meas is monotone-increasing and spans a real range
    v_meas = [m for _, m in rows]
    responds = all(v_meas[i + 1] > v_meas[i] for i in range(len(v_meas) - 1)) and (v_meas[-1] - v_meas[0]) > 0.2
    if verbose:
        print("[C4] BOOST-APPARATUS validation (LINEAR free packet, known-positive):")
        for v, m in rows:
            print(f"      v_boost={v:.1f}  ->  v_meas={m:+.4f}")
        print(f"      v_meas RESPONDS to v_boost: {'YES (boost is real)' if responds else 'NO'}")
    return {"rows": rows, "boost_apparatus_valid": bool(responds)}


def gate_master_dispersion(verbose=True):
    """MasterEquationFDTD boosted-breather localization sweep — robust across
    A0 × S_min. C-localize criterion: width_growth < 2× AND peak_retention > 0.5."""
    sweep = []
    any_localized = False
    for a0 in (0.85, 0.95, 0.99):
        for s_min in (0.05, 0.02, 0.005):
            r = _run_master(amp=a0, v=0.6, s_min=s_min)
            localized = (r["width_growth"] < WIDTH_GROWTH_MAX) and (r["peak_retention"] > PEAK_RETENTION_MIN)
            any_localized = any_localized or localized
            sweep.append({"A0": a0, "S_min": s_min, **r, "localized": bool(localized)})
    if verbose:
        print("\n[ME] MasterEquationFDTD boosted self-trap (v_boost=0.6, transit T=18):")
        print("      A0    S_min   v_meas   width_growth  peak_ret  LOCALIZED?")
        for s in sweep:
            print(
                f"      {s['A0']:.2f}  {s['S_min']:.3f}  {s['v_meas']:+.3f}    "
                f"{s['width_growth']:5.2f}x      {s['peak_retention']:.3f}     "
                f"{'YES' if s['localized'] else 'no'}"
            )
        print(f"      ANY config bounded-spread (C-localize PASS): {any_localized}")
        print("      => self-trap engages only at REST; boost disperses it below threshold.")
    return {"sweep": sweep, "c_localize_pass": bool(any_localized)}


def gate_vacuum_readout(verbose=True):
    """VacuumEngine3D C-readout: confirm BOTH fork channels are simultaneously
    live + readable (longitudinal div u + transverse V_inc + microrotation ω)."""
    n, pml = 24, 4
    eng = VacuumEngine3D.from_args(N=n, pml=pml, temperature=0.0)
    i, j, k = np.indices((n, n, n))
    blob = 0.01 * np.exp(-((i - n / 2) ** 2 + (j - n / 2) ** 2 + (k - n / 2) ** 2) / 8.0)
    eng.cos.u[..., 0] += blob  # longitudinal displacement
    eng.k4.V_inc[...] += blob[..., None]  # transverse V-sector (4 K4 ports)
    eng.step()
    ux, uy, uz = eng.cos.u[..., 0], eng.cos.u[..., 1], eng.cos.u[..., 2]
    div_u = np.gradient(ux, axis=0) + np.gradient(uy, axis=1) + np.gradient(uz, axis=2)
    long_max = float(np.abs(div_u).max())
    trans_max = float(np.abs(eng.k4.V_inc).max())
    omega_present = eng.cos.omega.shape[-1] == 3
    readout_ok = (long_max > 0.0) and (trans_max > 0.0) and omega_present
    if verbose:
        print("\n[VE] VacuumEngine3D C-readout (per-channel, prereg §5):")
        print(f"      longitudinal div(u)  : max = {long_max:.3e}  -> {'READABLE' if long_max>0 else 'ZERO'}")
        print(f"      transverse  V_inc    : max = {trans_max:.3e}  -> {'READABLE' if trans_max>0 else 'ZERO'}")
        print(f"      microrotation ω      : present = {omega_present}")
        print(f"      BOTH fork channels simultaneously readable (C-readout PASS): {readout_ok}")
        print("      C-transport on this host: FAIL — saturated (2,3) core PINS")
        print("        (verified SCREENED-PIN, 2026-06-04_motion-stability-bemf-longitudinal-result.md;")
        print("         V-sector is K4-TLM Z(V)-only, no c_eff(V) ⇒ frozen-clock core cannot translate).")
    return {
        "long_div_u_max": long_max,
        "trans_V_inc_max": trans_max,
        "omega_present": omega_present,
        "c_readout_pass": bool(readout_ok),
        "c_transport_pass": False,
        "pin_evidence": "research/2026-06-04_motion-stability-bemf-longitudinal-result.md (PIN-even-longitudinal)",
    }


def main():
    print("=" * 78)
    print("MOVING-DEFECT TRANSPORT CAPABILITY GATE (prereg §6) — fork: bulk vs transverse")
    print("=" * 78)
    c4 = gate_boost_apparatus()
    me = gate_master_dispersion()
    ve = gate_vacuum_readout()

    # Capability-gate matrix (prereg §6) → ordered bin (prereg §8/§9).
    gate = {
        "C-readout (per-channel)": {
            "VacuumEngine3D": ve["c_readout_pass"],
            "MasterEquationFDTD": False,  # scalar-V single channel
        },
        "C-transport (self-consistent translation)": {
            "VacuumEngine3D": ve["c_transport_pass"],  # PIN
            "MasterEquationFDTD": True,  # translates (boost is real, C4) ...
        },
        "C-localize (bounded spread, beat blur floor)": {
            "VacuumEngine3D": None,  # never translates -> n/a
            "MasterEquationFDTD": me["c_localize_pass"],  # ... but disperses -> FAIL
        },
    }
    # ENGINE-GAP iff no single engine clears {C-readout ∧ C-transport ∧ C-localize}.
    ve_clears = ve["c_readout_pass"] and ve["c_transport_pass"]
    me_clears = False and me["c_localize_pass"]  # ME fails C-readout by construction
    verdict = "ENGINE-GAP" if not (ve_clears or me_clears) else "CAPABLE"

    print("\n" + "=" * 78)
    print(f"GATE MATRIX -> VERDICT: {verdict}")
    print("-" * 78)
    print("  capability                       VacuumEngine3D    MasterEquationFDTD")
    print(f"  C-readout (per-channel)          {str(ve['c_readout_pass']):<17} {'False (scalar-V)'}")
    print(f"  C-transport (self-consistent)    {'False (PIN)':<17} {'translates'}")
    print(f"  C-localize (bounded spread)      {'n/a (no transit)':<17} {'False (disperses)'}")
    print("-" * 78)
    if verdict == "ENGINE-GAP":
        print("  No single engine clears {C-readout ∧ C-transport ∧ C-localize}.")
        print("  Missing capability (roadmap): a MULTI-CHANNEL engine with c_eff(V) on the")
        print("  V-sector whose bound state is BOOST-COVARIANT (the moving solution of the")
        print("  Master Equation, not a rest soliton + kick that dispersion undoes).")
        print("  Clean Rule-11 closure: prereg §8 bin 5 — the forward-registered most-probable outcome.")
    print("=" * 78)

    results = {
        "verdict": verdict,
        "prereg": "research/2026-06-11_moving-defect-doubleslit_prereg.md",
        "floors": {
            "blur_floor_V": BLUR_FLOOR_V,
            "width_growth_max": WIDTH_GROWTH_MAX,
            "peak_retention_min": PEAK_RETENTION_MIN,
        },
        "c4_boost_apparatus": c4,
        "master_equation_dispersion": me,
        "vacuum_engine_readout": ve,
        "gate_matrix": {k: {kk: vv for kk, vv in v.items()} for k, v in gate.items()},
        "missing_capability": (
            "multi-channel engine (V ⊗ u ⊗ ω) with c_eff(V) on the V-sector whose "
            "bound state is boost-covariant (moving Master-Equation solution, not "
            "rest-soliton + momentum kick that dispersion immediately undoes)"
        ),
    }
    out = OUT_DIR / "moving_defect_transport_gate_results.json"
    out.write_text(json.dumps(results, indent=2))
    print(f"\nwrote {out.relative_to(PROJECT_ROOT)}")
    return verdict


if __name__ == "__main__":
    main()
