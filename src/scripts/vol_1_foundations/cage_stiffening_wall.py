"""
Cage stiffening-wall self-focus test (A1 dilatation) — DRIVER
=============================================================

Implements `research/2026-06-13_cage-stiffening-wall_prereg_FROZEN.md`
(+ Amendments 1 & 2). DRIVER job on the v14-validated `CrystalEngine` bulk
branch — NOT a new build, NOT an engine modification.

WHAT THIS DOES
  Seeds the BARE standing A1-dilatation scalar `crystal_engine.self.V`
  (`∂_tV=0`, sub-saturation; CP8 generative precursor — NOT a pre-walled cage)
  and asks the prereg's self-create fork: does `max|A|_interior` GROW beyond the
  seed (the c_eff(V) self-steepening) and the wall deepen BELOW its t=0 value and
  PERSIST (SELF-FOCUS), or shrink (DISPERSE)? It classifies every arm into the
  FIVE frozen bins (A2.1) and reports the critical-frac (A4), the F1∧F4
  co-occurrence (A2.3), and the apparatus-qualified magnitude (A3 / §3).

WHAT THIS DOES NOT DO (scope honesty, ave-driver-script-honesty)
  - It does NOT bin on reaching Γ=−1. The wall depth is bench-capped (see
    `naive_gamma_floor`): A_cap=0.99 floors `gamma_bulk_min` at −0.2400 (S^{1/4}
    index). Magnitude is REPORTED, apparatus-qualified, never a verdict axis.
  - It does NOT fit any parameter against a target. Every number is read from the
    seeded/evolved field; the clip floor is computed from the clips alone.
  - It does NOT claim "built the electron cage" (v14 built it) or "scalar beats
    transverse". A positive = "confirms self.V is the self-trapping grade,
    consistent with v14 Mode I" (CONSISTENCY-class, prereg A2 / H1).

DISCRIMINATOR (CP9): `gamma_bulk()` is ALGEBRAIC in the instantaneous A, so a
seed reads `gamma_bulk<0` at t=0 from its amplitude alone — that is NOT the
signal. SELF-FOCUS is the DYNAMIC growth: `max|A|` grows beyond seed AND
`gamma_bulk_min` deepens below t=0 AND it persists (envelope trend, A2.4) AND it
stays bounded (no genesis-24 detonation). The `classify()` function is pure
(record -> bin) so all five bins are unit-testable on synthetic records.

Run:
    python cage_stiffening_wall.py --smoke        # CI-budget
    python cage_stiffening_wall.py --production    # resolve TRANSIENT-vs-persist
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))

from ave.core.crystal_engine import CrystalEngine  # noqa: E402

OUT = Path(__file__).parent

# Engine config: the PRIMARY Gaussian arms mirror the apparatus_floor_wall_run.py
# sibling (N=37 odd-center, dx=1.0, default clips) so this is a direct
# consistency check; the SECH consistency-anchor mirrors
# test_master_equation_v14_mode_i.py (N=24, dx=0.5, radius=2.5).
N_GAUSS = 37
DX_GAUSS = 1.0
SIGMA_GAUSS = 3.0
N_SECH = 24
DX_SECH = 0.5
RADIUS_SECH = 2.5
S_MIN = 0.05
A_CAP = 0.99
PML = 4

# Verdict tolerances (frozen here; the verdicts are robust to these — the
# sech/Gaussian separation is large, see the result doc).
GROW_TOL = 0.05  # peak must exceed seed by >5% to count as "grew"
PERSIST_FRAC = 0.50  # post-transient envelope must retain >50% of seed amplitude
FLAT_TOL = 0.08  # |persist - t0| within this frac of seed = "flat" (planted)
DEEPEN_ABS = 0.005  # gamma_min must go this much MORE negative than t0 to "deepen"
WALL_T0 = 0.01  # |gamma_min_t0| beyond this = a real planted wall (for PLANTED-ONLY)
DETONATION_MAX_V = 10.0  # max|V| beyond this = genesis-24 detonation (was ~1.08e4)


def naive_gamma_floor(s_min: float, a_cap: float) -> dict:
    """The DEEPEST Γ the clipped kernel can produce (the apparatus prediction;
    NOT a fit). S_floor = max(sqrt(1−A_cap²), S_min); reported with BOTH index
    powers — the S^{1/2} CORRECTED engine power (now the gamma_bulk default,
    sign-lock w35sn2bq3, 2026-06-17) AND the legacy S^{1/4} (regression anchor;
    was the exponent defect, now fixed in crystal_engine.gamma_bulk)."""
    s_a = float(np.sqrt(1.0 - a_cap**2))
    s_floor = max(s_a, s_min)
    binds = "A_cap" if s_a >= s_min else "S_min"
    n_q = s_floor**0.25
    n_h = s_floor**0.5
    return {
        "S_floor": s_floor,
        "binds": binds,
        "gamma_floor_S0.25": float((n_q - 1.0) / (n_q + 1.0)),
        "gamma_floor_S0.50": float((n_h - 1.0) / (n_h + 1.0)),
    }


def _seed(engine: CrystalEngine, profile: str, amp: float, width: float, dx: float):
    """Seed the bare standing A1-dilatation V (∂_tV=0).

    profile='gauss' -> the prereg §2 seed_bulk (Gaussian, helical=False).
    profile='sech'  -> the v14 eigen-profile direct-assign (the
                       test_master_equation_v14_mode_i.py method), the
                       CONSISTENCY-ANCHOR seed (NOT the prereg §2 seed_bulk).
    """
    ic = engine.N // 2
    if profile == "gauss":
        engine.seed_bulk((ic, ic, ic), sigma=width, frac=amp, helical=False)
    elif profile == "sech":
        c = engine.N // 2
        coords = np.arange(engine.N) - c
        xx, yy, zz = np.meshgrid(coords, coords, coords, indexing="ij")
        r = np.sqrt(xx**2 + yy**2 + zz**2) * dx
        seed = amp * (1.0 / np.cosh(r / width))
        engine.V[:] = seed
        engine.V_prev[:] = seed.copy()
    else:
        raise ValueError(f"unknown profile {profile!r}")


def run_arm(profile, amp, width, converter_on, n_steps, *, N, dx, transient_frac=0.5):
    """Run one arm; return a record of the self-create observables (print-what-
    you-compute — every field is read from the evolved engine state)."""
    e = CrystalEngine(N=N, dx=dx, S_min=S_MIN, A_cap=A_CAP, converter_on=converter_on, pml_thickness=PML)
    _seed(e, profile, amp, width, dx)
    m = e.interior_mask()

    def max_A():
        return float(np.max(e.strain_field()[m]))

    def max_V():
        return float(np.max(np.abs(e.V[m])))

    a0 = max_A()
    g0 = e.gamma_bulk()["gamma_min"]
    ec0 = e.bulk_energy_conserved()
    et0 = e.total_energy()

    a_series, g_series, v_series = [a0], [g0], [max_V()]
    ec_pk = ec0
    et_pk = et0
    for n in range(n_steps):
        e.step()
        a_series.append(max_A())
        g_series.append(e.gamma_bulk()["gamma_min"])
        v_series.append(max_V())
        if (n + 1) % 10 == 0:  # energy uses np.gradient — sample, don't every-step
            ec_pk = max(ec_pk, e.bulk_energy_conserved())
            et_pk = max(et_pk, e.total_energy())

    a_arr = np.array(a_series)
    g_arr = np.array(g_series)
    n_trans = int(transient_frac * len(a_arr))
    post = a_arr[n_trans:]
    mid = a_arr[n_trans : n_trans + max(1, len(post) // 2)]
    late = a_arr[n_trans + max(1, len(post) // 2) :]
    ec1 = e.bulk_energy_conserved()
    et1 = e.total_energy()
    fi = e.field_intensity()

    return {
        "profile": profile,
        "seed_amp": float(amp),
        "width": float(width),
        "converter_on": bool(converter_on),
        "N": N,
        "dx": dx,
        "n_steps": n_steps,
        "max_A_t0": float(a0),
        "max_A_end": float(a_arr[-1]),
        "max_A_peak": float(a_arr.max()),
        "max_A_persist": float(post.mean()),  # post-transient envelope (A2.4)
        "envelope_mid": float(mid.mean()),
        "envelope_late": float(late.mean()),
        "gamma_min_t0": float(g0),
        "gamma_min_end": float(g_arr[-1]),
        "gamma_min_deepest": float(g_arr.min()),
        "max_V_max": float(np.max(np.array(v_series))),
        "field_max_V_end": float(fi["max_V"]),
        "total_energy_t0": float(et0),
        "total_energy_end": float(et1),
        "total_energy_drift_pct": float((et1 - et0) / max(et0, 1e-30) * 100.0),
        "bulk_E_conserved_t0": float(ec0),
        "bulk_E_conserved_end": float(ec1),
        "bulk_E_conserved_drift_pct": float((ec1 - ec0) / max(ec0, 1e-30) * 100.0),
        "bulk_E_conserved_peak_pct": float((ec_pk - ec0) / max(ec0, 1e-30) * 100.0),
        "converter_work": float(e.converter_work),
    }


def classify(rec, *, grow_tol=GROW_TOL, persist_frac=PERSIST_FRAC, flat_tol=FLAT_TOL,
             deepen_abs=DEEPEN_ABS, wall_t0=WALL_T0, detonation_max_V=DETONATION_MAX_V):
    """Pure five-bin classifier (prereg §3 + A2.1/A2.2). Operates only on the
    recorded summaries so it is unit-testable on synthetic records.

    Bins: DETONATION-PUMP / SELF-FOCUS / TRANSIENT / PLANTED-ONLY / DISPERSES /
    UNRESOLVED. (DETONATION-PUMP is the F4-FAIL genesis-24 outcome; it is the
    "grew WITH energy detonation" half of the A2.3 co-occurrence and is reported
    distinctly so a numerical pump can never be scored SELF-FOCUS.)

    NOTE on F4 (flagged, not used to gate SELF-FOCUS): `bulk_E_conserved` is NOT
    flat for THIS engine's leapfrog breather (the canonical v14 sech grows it
    ~+480%, bounded/oscillating). So the operative self-focus/pump discriminator
    is BOUNDEDNESS (max|V| stays O(1), no genesis-24 detonation to ~1e4) +
    PERSISTENCE — NOT energy-flatness. The drift is reported for adjudication.
    """
    a0 = rec["max_A_t0"]
    apk = rec["max_A_peak"]
    apersist = rec["max_A_persist"]
    g0 = rec["gamma_min_t0"]
    gdeep = rec["gamma_min_deepest"]
    maxv = rec["max_V_max"]

    grew = apk > a0 * (1.0 + grow_tol)
    deepened = gdeep < (g0 - deepen_abs)
    persists = apersist > a0 * persist_frac
    decaying = rec["envelope_late"] < rec["envelope_mid"] * 0.6  # steep late decay
    shrank = apersist < a0 * (1.0 - flat_tol)
    flat = abs(apersist - a0) <= flat_tol * a0 and abs(gdeep - g0) <= deepen_abs
    detonated = maxv > detonation_max_V

    if detonated:
        return "DETONATION-PUMP"
    if grew and deepened and persists and not decaying:
        return "SELF-FOCUS"
    if grew and (not persists or decaying):
        return "TRANSIENT"
    if (g0 < -wall_t0) and flat and not deepened:
        return "PLANTED-ONLY"
    if shrank:
        return "DISPERSES"
    return "UNRESOLVED"


def fmt(rec, bin_):
    fl = naive_gamma_floor(S_MIN, A_CAP)["gamma_floor_S0.25"]
    on_floor = abs(rec["gamma_min_deepest"] - fl) < 0.01
    return (
        f"  {rec['profile']:5} amp={rec['seed_amp']:.2f} conv={int(rec['converter_on'])} "
        f"N={rec['N']} | A0={rec['max_A_t0']:.3f} Apk={rec['max_A_peak']:.3f} "
        f"Apersist={rec['max_A_persist']:.3f} | g0={rec['gamma_min_t0']:+.4f} "
        f"gdeep={rec['gamma_min_deepest']:+.4f}{'(=floor)' if on_floor else ''} | "
        f"dEc={rec['bulk_E_conserved_drift_pct']:+.0f}% maxV={rec['max_V_max']:.2f} "
        f"cw={rec['converter_work']:+.2e} -> {bin_}"
    )


def critical_frac(records_bins):
    """A4 primary read: the nucleation threshold (DISPERSES below, SELF-FOCUS
    above) from a list of (seed_amp, bin) pairs, sorted by amp. Returns the
    bracket (highest non-self-focus, lowest self-focus) or a 'no threshold'
    string when every arm lands on one side."""
    sf = sorted([a for a, b in records_bins if b == "SELF-FOCUS"])
    notsf = sorted([a for a, b in records_bins if b in ("DISPERSES", "TRANSIENT", "PLANTED-ONLY")])
    if not sf:
        return {"threshold": None, "note": "no SELF-FOCUS at any tested amp -> no critical-frac"}
    if not notsf:
        return {"threshold": f"< {sf[0]:.3f}", "note": "SELF-FOCUS at every tested amp -> threshold below the sweep floor"}
    lo = max([a for a in notsf if a < sf[0]], default=None)
    return {"threshold_bracket": [lo, sf[0]], "note": f"DISPERSES<= {lo} < {sf[0]} =<SELF-FOCUS"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--smoke", action="store_true", help="CI budget (short, fewer points)")
    ap.add_argument("--production", action="store_true", help="resolve TRANSIENT-vs-persist")
    args = ap.parse_args()
    smoke = args.smoke or not args.production
    ng = 250 if smoke else 700  # Gaussian-arm steps (N=37, dx=1.0)
    ns = 300 if smoke else 600  # sech-arm steps (N=24, dx=0.5)
    fracs = [0.50, 0.85] if smoke else [0.30, 0.50, 0.70, 0.85, 0.95]
    amps = [0.50, 0.85] if smoke else [0.20, 0.30, 0.50, 0.70, 0.85]

    t0 = time.time()
    fl = naive_gamma_floor(S_MIN, A_CAP)
    print("=" * 92)
    print("  CAGE STIFFENING-WALL SELF-FOCUS TEST (A1 dilatation, crystal_engine.self.V)")
    print(f"  mode={'SMOKE' if smoke else 'PRODUCTION'}  clip floor: gamma_min >= {fl['gamma_floor_S0.25']:+.4f} "
          f"(S^0.25, {fl['binds']} binds) | S^0.50 power -> {fl['gamma_floor_S0.50']:+.4f} [exponent-defect FLAG]")
    print("  DISCRIMINATOR: DYNAMIC max|A| growth + gamma_min deepening below t0, NOT the t=0 read (CP9).")
    print("=" * 92, flush=True)

    out = {"mode": "smoke" if smoke else "production", "clip_floor": fl, "arms": {}}

    # ---- F0: no seed -> no wall (baseline falsifier) -----------------------
    print("\n[F0] no seed -> no wall (baseline):", flush=True)
    f0 = run_arm("gauss", 0.0, SIGMA_GAUSS, False, ng, N=N_GAUSS, dx=DX_GAUSS)
    f0_bin = "NO-WALL" if abs(f0["gamma_min_t0"]) < 1e-6 and abs(f0["gamma_min_deepest"]) < 1e-3 else "WALL-WITHOUT-SEED(ARTIFACT)"
    print(f"  gamma_min_t0={f0['gamma_min_t0']:+.2e} gamma_min_deepest={f0['gamma_min_deepest']:+.2e} -> {f0_bin}")
    out["arms"]["F0"] = {"record": f0, "bin": f0_bin}

    # ---- S1: bare V self-trap (converter OFF) — the prereg §2 seed_bulk -----
    print("\n[S1] seed_bulk GAUSSIAN, converter_on=False (the bare V self-trap, the prereg §2 seed):", flush=True)
    s1 = []
    for fr in fracs:
        r = run_arm("gauss", fr, SIGMA_GAUSS, False, ng, N=N_GAUSS, dx=DX_GAUSS)
        b = classify(r)
        print(fmt(r, b))
        s1.append((fr, b, r))
    out["arms"]["S1"] = [{"record": r, "bin": b} for _, b, r in s1]
    out["S1_critical_frac"] = critical_frac([(a, b) for a, b, _ in s1])

    # ---- S2: + ADD-2 chiral converter (converter ON) -----------------------
    print("\n[S2] seed_bulk GAUSSIAN, converter_on=True (+ ADD-2 chiral converter):", flush=True)
    s2 = []
    for fr in fracs:
        r = run_arm("gauss", fr, SIGMA_GAUSS, True, ng, N=N_GAUSS, dx=DX_GAUSS)
        b = classify(r)
        print(fmt(r, b))
        s2.append((fr, b, r))
    out["arms"]["S2"] = [{"record": r, "bin": b} for _, b, r in s2]
    out["S2_critical_frac"] = critical_frac([(a, b) for a, b, _ in s2])

    # ---- ANCHOR: sech eigen-profile (converter OFF) — the v14 consistency ---
    print("\n[ANCHOR] SECH eigen-profile (v14 direct-assign, NOT seed_bulk), converter_on=False:")
    print("         consistency-with-v14: does self.V self-focus from the soliton eigen-profile?", flush=True)
    sa = []
    for am in amps:
        r = run_arm("sech", am, RADIUS_SECH, False, ns, N=N_SECH, dx=DX_SECH)
        b = classify(r)
        print(fmt(r, b))
        sa.append((am, b, r))
    out["arms"]["SECH_ANCHOR"] = [{"record": r, "bin": b} for _, b, r in sa]
    out["SECH_critical_frac"] = critical_frac([(a, b) for a, b, _ in sa])

    # ---- PROFILE: sech vs Gaussian, IDENTICAL box (the load-bearing contrast)
    print("\n[PROFILE] sech vs Gaussian in the IDENTICAL v14 box (N=24, dx=0.5, converter OFF):")
    print("          isolates the seed-PROFILE sensitivity at matched amplitude.", flush=True)
    prof = []
    for am in ([0.85] if smoke else [0.50, 0.85]):
        rs = run_arm("sech", am, RADIUS_SECH, False, ns, N=N_SECH, dx=DX_SECH)
        bs = classify(rs)
        print(fmt(rs, bs))
        prof.append({"record": rs, "bin": bs})
        for w in [1.0, 1.25]:  # PML-safe Gaussian widths in the v14 box
            rg = run_arm("gauss", am, w, False, ns, N=N_SECH, dx=DX_SECH)
            bg = classify(rg)
            print(fmt(rg, bg))
            prof.append({"record": rg, "bin": bg})
    out["arms"]["PROFILE_CONTRAST"] = prof

    out["elapsed_s"] = time.time() - t0
    (OUT / "cage_stiffening_wall_results.json").write_text(json.dumps(out, indent=2, default=str))
    print(f"\n  S1 critical-frac: {out['S1_critical_frac']}")
    print(f"  S2 critical-frac: {out['S2_critical_frac']}")
    print(f"  SECH critical-frac: {out['SECH_critical_frac']}")
    print(f"  wrote cage_stiffening_wall_results.json | elapsed {out['elapsed_s']:.1f}s", flush=True)
    return out


if __name__ == "__main__":
    main()
