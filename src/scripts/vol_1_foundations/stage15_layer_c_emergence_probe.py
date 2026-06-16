"""Stage-1.5 LAYER (c) — α-FREE winding-emergence probe (the chord read).

Prereg (FROZEN): research/2026-06-16_stage15-alphafree-winding-emergence-prereg.md
Build-order DAG layer (c): "seed generic precursor, run α-FREE; observe whether
the (2,3) winding + Γ=−1 SELF-FORM (no planted (2,3)) and whether an α-free Q
emerges (~137 without being told)."

GATED on Layer (b): the emergence loop requires the winding to source the cage
(close the energize-LOCK loop). Layer (b) FOUND that loop INERT for a generic
untrapped transverse photon (the front-vs-interior + extended-vs-compact
co-location obstruction). This probe RUNS the emergence measurement anyway and
reports the honest answer — a clean negative with a NAMED mechanism is the
discipline working (Rule 11), NOT a forced result.

THE MEASUREMENT (A46 phase-space, NOT real-space lattice — the trap that voided
30+ prior tests). The validated _contour_winding extractor (ported from
crystal_engine_alpha_emergence.py) traces the phase of the (V_inc, V_ref) phasor
on torus contours: toroidal loop → the "2" (=p); poloidal loop → the "3" (=q).
Measured in BOTH:
  - the BULK reactance phase-space (V, ∂_tV) — the scalar cage (crystal_engine
    found this carries NEITHER winding: w_tor=0, w_pol=0);
  - the COSSERAT ω winding phase-space (ω_x, ω_y) — the VECTOR U(1)-fibre carrier
    this engine ADDS (the carrier the scalar bulk lacked).

SEED-AUDIT (CP8 non-circularity): the t=0 seed (sub-yield bulk + generic
transverse photon, NO planted (2,3)) must NOT close the (2,3) — else a laundered
positive. Verified before the run.

α-FREE (load-bearing): κ̃=6/5; V_yield=1.0; ω_yield=π. Zero ALPHA in dynamics.
The α-free Q (if a (2,3) resonator self-forms) would be read from the trapped
mode's stored/leaked energy ratio — NOT inserted (the form-chord readout). With
no resonator, there is nothing for Q to be (the joint-ledger guard).

Run:  PYTHONPATH=src ./.venv/bin/python \
        src/scripts/vol_1_foundations/stage15_layer_c_emergence_probe.py
Env overrides: S15_N (default 24), S15_PERIODS (default 12).
"""
from __future__ import annotations

import json
import os

import numpy as np

import ave.core.constants as _avc
from ave.core.constants import ALPHA, ALPHA_COLD_INV
from ave.core.a1_cosserat_convergence_engine import A1CosseratConvergenceEngine

HERE = os.path.dirname(os.path.abspath(__file__))

N = int(os.environ.get("S15_N", "24"))
PML = 4
DX = 0.5
SEED_FRAC = 0.85
SEED_SIGMA = 2.5
PHOTON_AMP = 0.3
PHOTON_SIGMA = 3.0
PHOTON_LAM = 6.0

OMEGA_C_NATURAL = 1.0
T_COMPTON = 2.0 * np.pi / OMEGA_C_NATURAL
N_PERIODS = float(os.environ.get("S15_PERIODS", "12"))


def _alpha_free_provenance_gate() -> None:
    assert _avc.__file__.endswith("ave/core/constants.py"), "non-canonical constants"
    assert abs(ALPHA - 7.2973525693e-3) < 1e-12, "ALPHA not canonical"
    # ALPHA / ALPHA_COLD_INV asserted for COMPARISON-ONLY provenance; NEVER inserted.


def _contour_winding(fx, fy, center, R, r_minor, plane="poloidal", n=128):
    """Phase winding of (fx+i·fy) on a torus contour (ported verbatim from the
    validated crystal_engine_alpha_emergence.py extractor; A46 phase-space).
    plane='toroidal' → major ring (the "2"); 'poloidal' → tube loop (the "3").
    Returns (winding, reliability=min/max amp, max_amp)."""
    cx, cy, cz = center
    t = np.linspace(0.0, 2.0 * np.pi, n, endpoint=False)
    if plane == "poloidal":
        xs = cx + (R + r_minor * np.cos(t))
        ys = cy + np.zeros_like(t)
        zs = cz + r_minor * np.sin(t)
    else:
        xs = cx + R * np.cos(t)
        ys = cy + R * np.sin(t)
        zs = cz + np.zeros_like(t)
    nx, ny, nz = fx.shape
    ix = np.clip(xs.astype(int), 0, nx - 2)
    iy = np.clip(ys.astype(int), 0, ny - 2)
    iz = np.clip(zs.astype(int), 0, nz - 2)
    dx_, dy_, dz_ = xs - ix, ys - iy, zs - iz

    def samp(F):
        return (
            (1 - dx_) * (1 - dy_) * (1 - dz_) * F[ix, iy, iz]
            + dx_ * (1 - dy_) * (1 - dz_) * F[ix + 1, iy, iz]
            + (1 - dx_) * dy_ * (1 - dz_) * F[ix, iy + 1, iz]
            + (1 - dx_) * (1 - dy_) * dz_ * F[ix, iy, iz + 1]
            + dx_ * dy_ * (1 - dz_) * F[ix + 1, iy + 1, iz]
            + dx_ * (1 - dy_) * dz_ * F[ix + 1, iy, iz + 1]
            + (1 - dx_) * dy_ * dz_ * F[ix, iy + 1, iz + 1]
            + dx_ * dy_ * dz_ * F[ix + 1, iy + 1, iz + 1]
        )

    ox, oy = samp(fx), samp(fy)
    amp = np.sqrt(ox**2 + oy**2)
    max_amp = float(amp.max())
    if max_amp < 1e-30:
        return 0.0, 0.0, max_amp
    phase = np.unwrap(np.arctan2(oy, ox))
    winding = (phase[-1] - phase[0]) / (2.0 * np.pi)
    return float(winding), float(amp.min() / max_amp), max_amp


def _measure_23(fx, fy, center, R, n_minor=6):
    """Best (w_tor, w_pol) over a minor-radius scan, with reliabilities. Closes
    iff |w_tor−2|<0.5 AND |w_pol−3|<0.5 on a reliable (rel>0.1) populated contour."""
    out = {}
    amp_seen = 0.0
    for plane in ("toroidal", "poloidal"):
        w_best, rel_best = 0.0, 0.0
        for r_minor in np.linspace(1.0, max(3.0, R * 0.6), n_minor):
            w, rel, amp = _contour_winding(fx, fy, center, R, r_minor, plane)
            amp_seen = max(amp_seen, amp)
            if rel > rel_best:
                w_best, rel_best = w, rel
        out[f"w_{plane[:3]}"] = round(w_best, 2)
        out[f"rel_{plane[:3]}"] = round(rel_best, 3)
    out["amp"] = float(amp_seen)
    wt, wp = abs(out["w_tor"]), abs(out["w_pol"])
    rel = min(out["rel_tor"], out["rel_pol"])
    out["closes_23"] = bool(amp_seen > 1e-9 and rel > 0.1 and abs(wt - 2.0) < 0.5 and abs(wp - 3.0) < 0.5)
    return out


def _winding_read(eng, omega_char=1.0) -> dict:
    """Measure the (2,3) winding in BOTH phase-spaces at their density peaks."""
    # bulk reactance phase-space at the |V|² peak
    bpk = eng.density_peak_interior()
    bvx, bvy, _, _ = eng.bulk_phase_space_vinc_vref(omega_char)
    R_b = max(eng.N * 0.18, 3.0)
    bulk = _measure_23(bvx, bvy, bpk, R_b)
    # Cosserat ω winding phase-space at the |ω|² peak (the NEW vector carrier)
    wpk = eng.omega_density_peak_interior()
    wvx, wvy, _, _ = eng.cosserat_phase_space_vinc_vref(omega_char)
    R_w = max(eng.N * 0.18, 3.0)
    cos = _measure_23(wvx, wvy, wpk, R_w)
    return {
        "bulk_reactance": {"peak": list(bpk), **bulk},
        "cosserat_winding": {"peak": list(wpk), **cos},
        "any_closes_23": bool(bulk["closes_23"] or cos["closes_23"]),
    }


def main() -> dict:
    _alpha_free_provenance_gate()

    eng = A1CosseratConvergenceEngine(
        N=N, dx=DX, V_yield=1.0, c0=1.0, cfl_safety=0.4,
        pml_thickness=PML, A_cap=0.99, S_min=0.05, couple_on=True,
        coupling_support="front",
    )
    c = N / 2.0
    eng.seed_bulk_blob(center=(c, c, c), sigma=SEED_SIGMA, frac=SEED_FRAC)
    eng.seed_cosserat_photon(center=(c, c, c), sigma=PHOTON_SIGMA,
                             wavelength=PHOTON_LAM, amplitude=PHOTON_AMP,
                             direction=(1, 0, 0), helicity=1.0, axis=2)

    # ── SEED-AUDIT (CP8 non-circularity): t=0 must NOT close the (2,3) ──
    seed_read = _winding_read(eng)
    seed_circular = seed_read["any_closes_23"]

    nsteps = int(np.ceil(N_PERIODS * T_COMPTON / eng.dt))
    diverged = None
    omega_seed = eng.omega_max_interior()
    for s in range(nsteps):
        eng.step_coupled()
        oc = eng.omega_max_interior()
        if not np.isfinite(oc) or oc > 1e4 * max(omega_seed, 1e-6):
            diverged = s
            break

    # ── THE EMERGENCE READ (post-run, evolved field) ──
    final_read = _winding_read(eng)
    self_formed_23 = final_read["any_closes_23"] and not seed_circular

    # ── α-free Q read: ONLY meaningful if a (2,3) resonator self-formed (the
    #    joint-ledger guard — no resonator ⇒ nothing for Q to be) ──
    if self_formed_23:
        q_note = "(2,3) resonator self-formed — Q read is Stage-2 work (not computed here)"
        q_emerged = None
    else:
        q_note = (
            "NO (2,3) resonator self-formed → there is NO resonator whose Q an "
            "α-free leak could be. 'α=Q⁻¹ of the (2,3) Golden-Torus' presupposes a "
            "(2,3); absent it, NO α-free Q to read (joint-ledger guard, "
            "crystal_engine_result.md §3.4). α NOT emergent — and NOT inserted."
        )
        q_emerged = False

    verdict = "LAYER-C-EMERGENCE-CANDIDATE" if self_formed_23 else "LAYER-C-EMERGENCE-NEGATIVE"

    result = {
        "stage": "Stage-1.5 LAYER (c) — α-free winding-emergence probe",
        "alpha_free": True,
        "alpha_in_dynamics": "NONE (κ̃=6/5; V_yield=1.0; ω_yield=π; ALPHA/ALPHA_COLD_INV comparison-only)",
        "run_N_explicit": int(N),
        "long_window_periods": float(N_PERIODS),
        "diverged_at": diverged,
        "seed_audit": {
            "t0_closes_23": bool(seed_circular),
            "non_circular": bool(not seed_circular),
            "seed_read": seed_read,
        },
        "emergence_read": final_read,
        "self_formed_23_from_generic_IC": bool(self_formed_23),
        "alpha_free_Q_emerged": q_emerged,
        "alpha_free_Q_note": q_note,
        "alpha_comparison_only": {"ALPHA_inv_CODATA": float(1.0 / ALPHA),
                                  "ALPHA_COLD_INV": float(ALPHA_COLD_INV)},
        "layer_b_gate_note": (
            "GATED on Layer (b): the energize-LOCK loop is INERT for a generic "
            "untrapped transverse photon (front-vs-interior + extended-vs-compact "
            "co-location obstruction). The winding does NOT source the cage, so it "
            "is not trapped/concentrated to self-form the (2,3). A negative here is "
            "the EXPECTED consequence of the Layer-(b) obstruction, reported honestly "
            "(Rule 11) — NOT a forced result. Closing the loop (the design fork for "
            "Grant/auditor) is the precondition for a meaningful emergence positive."
        ),
        "verdict": verdict,
    }
    out_path = os.path.join(HERE, "stage15_layer_c_emergence_probe_results.json")
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2)
    result["results_json"] = out_path

    print("=" * 78)
    print("STAGE-1.5 LAYER (c) — α-FREE WINDING-EMERGENCE PROBE")
    print("=" * 78)
    print(f"α-free: True (κ̃=6/5; V_yield=1.0; ω_yield=π; ALPHA comparison-only)")
    print(f"run N (explicit) = {N}   long-window periods = {N_PERIODS}")
    print("-" * 78)
    sa = result["seed_audit"]
    print(f"SEED-AUDIT (CP8 non-circularity): t0_closes_23={sa['t0_closes_23']} "
          f"non_circular={sa['non_circular']}")
    er = result["emergence_read"]
    b, cw = er["bulk_reactance"], er["cosserat_winding"]
    print(f"EMERGENCE READ (A46 phase-space, evolved field):")
    print(f"  BULK reactance (V,∂_tV) @peak={b['peak']}: w_tor={b['w_tor']} w_pol={b['w_pol']} "
          f"rel=({b['rel_tor']},{b['rel_pol']}) amp={b['amp']:.3e} closes={b['closes_23']}")
    print(f"  COSSERAT ω-winding (ω_x,ω_y) @peak={cw['peak']}: w_tor={cw['w_tor']} w_pol={cw['w_pol']} "
          f"rel=({cw['rel_tor']},{cw['rel_pol']}) amp={cw['amp']:.3e} closes={cw['closes_23']}")
    print(f"  → self-formed (2,3) from generic IC (no plant)? {result['self_formed_23_from_generic_IC']}")
    print(f"α-free Q: {result['alpha_free_Q_note']}")
    print("-" * 78)
    print(f"VERDICT: {verdict}")
    print(f"results -> {out_path}")
    print("=" * 78)
    return result


if __name__ == "__main__":
    main()
