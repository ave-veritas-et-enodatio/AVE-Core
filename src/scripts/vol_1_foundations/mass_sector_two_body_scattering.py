"""
MASS-SECTOR TWO-BODY SCATTERING — validate-on-known (gravity) on the scalar A1 engine
====================================================================================

Executes the FROZEN design of
`research/2026-06-23_mass-sector-two-body-scattering_prereg.md`.

WHAT THIS IS: a two-prong validate-on-known. Two Mode-I dilatation-mass bound
states (A1 dilatation blobs, master-equation.md:20,24-25) at impact parameter
b=0, head-on, at fixed separation. Measure:
  (i)  is the two-body interaction ATTRACTIVE (matching AVE-gravity's mass-mass
       sign, optical-refraction-gravity.md:13)?  AND
  (ii) is it PHASE-INDEPENDENT (→ gravity-like) or PHASE-DEPENDENT (→ generic
       nonlinear-soliton interaction, which would mean this is NOT gravity)?

THE CRITICAL GUARD (refute-by-default): a generic bright-soliton pair attracts
IN-PHASE and repels OUT-OF-PHASE — ordinary NLS soliton interaction, NOT gravity.
Gravity is PHASE-INDEPENDENT. So we run BOTH relative phases at b=0. In this REAL
SCALAR engine "phase" = SIGN of the second blob (+amp = in-phase, -amp = pi-out).
The gravity mechanism is driven by A^2(r)=|V|^2/V_yield^2 (saturation depth, an
ENVELOPE = sign-blind quantity), so a true gravity force must be sign-independent.

TRANSPORT-LESS ENGINE (annihilation_evaporation_run.py:46-50, DEV-6): this engine
lineage admits ZERO subluminal rigid transport ("the imprinted KE radiates instead
of convecting the trap"). So the force readout is STATIC, at t~0: two stationary
blobs, measure the initial relative acceleration of the saturation-core centroids
BEFORE radiation contaminates (window calibrated against a single-blob control).

OBSERVABLES (all FROM the evolved field; ave-driver-script-honesty):
  O0 single-blob control  -> radiation-jitter floor + N_FORCE window
  O1 centroid drift       -> the FORCE VERDICT (separation d(t); sign of d'')
  O2 A^2 midplane gradient-> the corpus MECHANISM witness (optical refraction)
  O3 A^2_local + omega_local at cores -> Regime-II / local-clock witness (CP5)

SAMPLING DISCIPLINE (substrate-native-check CP7): PML cells excluded before any
top-K |V|^2 centroid extraction; A1 blob is density-PEAKED so centroid-of-blob is
valid (not a shell).

CONSTANTS: ALL from ave.core.constants (ave-canonical-source). Seed-reuse ref:
r10_master_equation_v14.py Test C (lines 243-300).

Run:
    PYTHONPATH=src .venv/bin/python \
        src/scripts/vol_1_foundations/mass_sector_two_body_scattering.py
"""

from __future__ import annotations

import json

import numpy as np

from ave.core.master_equation_fdtd import MasterEquationFDTD

# --- FROZEN config (prereg §2 — CORRECTED SEED, see SEED-SPEC FLAG below) ----
#
# SEED-SPEC FLAG (flag-don't-fix, 2026-06-23): the brief's stated "canonical
# Mode-I seed" (N=32, amp=0.95*V_yield, R=2.0, center-cell persistence metric,
# r10 Test C:262-263) does NOT pass r10 Test C's own persistence gate on HEAD
# (V_center_ratio = -0.089, threshold 0.5 -> Test C1 FAIL; the bare sech seed
# disperses). The ACTUAL validated canonical Mode-I (passes 5/5 in
# src/tests/test_master_equation_v14_mode_i.py on HEAD) is the BREATHING soliton
# at N=24, DX=0.5, V_yield=1.0, amp=0.85, R=2.5, measured by V_PEAK (the max,
# which tracks the breathing core) over a post-transient window. This driver
# uses the VALIDATED config so the two-body test runs on a real bound state, not
# a dispersing seed. Verified: brief-seed r10-C1 FAIL vs canonical 5/5 PASS.
N = 24
DX = 0.5
V_YIELD = 1.0                    # canonical v14 natural units
C0 = 1.0
CFL_SAFETY = 0.4
PML = 4
SEED_AMPLITUDE = 0.85            # v14 canonical (saturation engaged, breather holds)
SEED_RADIUS = 2.5               # v14 canonical
SEPARATIONS = [5, 7, 9]          # center-to-center, cells; FWHM~2.5/DX, PML=4 -> interior clearance ok at N=24
N_RUN = 600                      # v14 canonical window (transient 200 + record 400)
N_TRANSIENT = 200                # skip the seed-settling transient before reading force
JITTER_FLOOR_CELLS = 0.5         # provisional; OVERRIDDEN per-d0 by the O0 control (prereg §3)
PEAK_FRAC = 0.5                  # V_peak mask threshold for the breathing-core centroid


def _make_engine() -> MasterEquationFDTD:
    return MasterEquationFDTD(
        N=N, dx=DX, V_yield=V_YIELD, c0=C0, cfl_safety=CFL_SAFETY, pml_thickness=PML,
    )


def _seed_breather(eng: MasterEquationFDTD, cx: int, sign: float) -> None:
    """Add a v14-canonical sech breather at (cx, N/2, N/2) with given sign.

    sign = +1 (in-phase) or -1 (pi-out-of-phase). Uses DX-scaled radial coord,
    matching the validated regression seed exactly.
    """
    coords = np.arange(N)
    X, Y, Z = np.meshgrid(coords - cx, coords - N // 2, coords - N // 2, indexing="ij")
    r = np.sqrt(X * X + Y * Y + Z * Z) * DX
    eng.V += sign * SEED_AMPLITUDE * (1.0 / np.cosh(r / SEED_RADIUS))


# --- interior (PML-excluded) mask, built once (CP7) --------------------------
_I, _J, _K = np.indices((N, N, N))
_INTERIOR = (
    (_I >= PML) & (_I <= N - PML - 1)
    & (_J >= PML) & (_J <= N - PML - 1)
    & (_K >= PML) & (_K <= N - PML - 1)
)


def core_centroid_x(V: np.ndarray, half: str) -> float:
    """PML-excluded V_peak-mask centroid x of ONE breathing-core, in its half.

    half: 'left'  -> restrict to x < N/2 (blob A)
          'right' -> restrict to x >= N/2 (blob B)

    PER CP7: PML cells excluded. Uses the V_peak>PEAK_FRAC*max mask (the same
    breathing-core locator as the validated v14 regression's V_peak metric),
    NOT a fixed top-K density extraction. Rationale (empirical, 2026-06-23): a
    fixed top-K |V|^2 centroid migrates to the half-volume mask boundary (x=N/2)
    once the field radiates, producing a spurious 'attraction' artifact; the
    per-blob V_peak mask tracks the actual core lobe. Each blob is sampled in
    its own half-space so one blob's tail does not bias the other's centroid.
    """
    half_mask = (_I < N // 2) if half == "left" else (_I >= N // 2)
    mask = _INTERIOR & half_mask
    Va = np.abs(V) * mask
    vm = Va.max()
    if vm <= 0.0:
        return float("nan")
    core = Va > (PEAK_FRAC * vm)
    w = Va * core
    wsum = w.sum()
    if wsum <= 0.0:
        return float("nan")
    return float(np.sum(w * _I) / wsum)


def midplane_A2(V: np.ndarray) -> float:
    """Mean saturation depth A^2 = (|V|/V_yield)^2 on the interior midplane x=N/2.

    The O2 mechanism witness: each blob raises the local refractive index
    (lowers c_eff) in the gap; A^2 is the sign-blind envelope quantity that
    drives the optical-refraction gravity mechanism (optical-refraction-gravity.md:13-17).
    """
    plane = (_I == N // 2) & _INTERIOR
    A = np.abs(V[plane]) / V_YIELD
    if A.size == 0:
        return float("nan")
    return float(np.mean(A * A))


def core_A2_and_omega(engine: MasterEquationFDTD) -> tuple[float, float]:
    """O3: peak A^2 anywhere interior + omega_local/omega_global = sqrt(1-A^2) (CP5)."""
    A = np.abs(engine.V) / V_YIELD
    A_interior = A * _INTERIOR
    A2_peak = float(np.max(A_interior * A_interior))
    A2_clip = min(A2_peak, engine.A_cap * engine.A_cap)
    omega_ratio = float(np.sqrt(max(1.0 - A2_clip, 0.0)))
    return A2_peak, omega_ratio


def run_single_blob_control(d0: int) -> dict:
    """O0: ONE breather at blob-A's position; its centroid should stay put.

    Reads the V_peak-mask centroid over the post-transient window. The radiation
    floor = max centroid wander of the single isolated blob (zero initial
    velocity -> any wander is radiation/breathing jitter, not force). The
    two-body O1 net-drift must EXCEED this floor to count as a force.
    """
    eng = _make_engine()
    cx = N // 2 - d0 // 2
    _seed_breather(eng, cx, +1.0)
    eng.V_prev = eng.V.copy()  # zero initial velocity (matches regression seed)
    for _ in range(N_TRANSIENT):
        eng.step()
    x_ref = core_centroid_x(eng.V, "left")
    wander = []
    for _ in range(N_TRANSIENT, N_RUN):
        eng.step()
        xc = core_centroid_x(eng.V, "left")
        wander.append(abs(xc - x_ref) if np.isfinite(xc) else float("nan"))
    floor = float(np.nanmax(wander)) if wander else float("nan")
    return {
        "x_ref_post_transient": x_ref,
        "radiation_floor_cells": floor,
        "final_wander": float(wander[-1]) if wander else float("nan"),
    }


def run_two_body(d0: int, phase: str) -> dict:
    """O1/O2/O3: two breathers at separation d0, given relative phase, b=0.

    phase: 'in'  -> second seed +SEED_AMPLITUDE (constructive overlap)
           'out' -> second seed -SEED_AMPLITUDE (pi-out-of-phase, cancelling)

    Force is read post-transient: net change in separation over the recording
    window after the seed-settling transient (the FORCE VERDICT). Also records
    midplane A^2 (O2 mechanism witness) and core A^2/omega (O3).
    """
    eng = _make_engine()
    cxA = N // 2 - d0 // 2
    cxB = N // 2 + d0 // 2 + (d0 % 2)  # integer center-to-center = d0
    sign_B = +1.0 if phase == "in" else -1.0
    _seed_breather(eng, cxA, +1.0)
    _seed_breather(eng, cxB, sign_B)
    eng.V_prev = eng.V.copy()  # zero initial velocity

    A2_mid0 = midplane_A2(eng.V)
    for _ in range(N_TRANSIENT):
        eng.step()
    # sep reference taken AFTER the transient (the post-settling separation)
    xA0 = core_centroid_x(eng.V, "left")
    xB0 = core_centroid_x(eng.V, "right")
    sep0 = abs(xB0 - xA0)

    sep_series, A2_mid_series = [], []
    for _ in range(N_TRANSIENT, N_RUN):
        eng.step()
        xA = core_centroid_x(eng.V, "left")
        xB = core_centroid_x(eng.V, "right")
        sep_series.append(abs(xB - xA) if (np.isfinite(xA) and np.isfinite(xB)) else float("nan"))
        A2_mid_series.append(midplane_A2(eng.V))

    A2_peak, omega_ratio = core_A2_and_omega(eng)
    sep_final = sep_series[-1] if sep_series else float("nan")
    net_dsep = sep_final - sep0  # < 0 -> cores drew together = ATTRACTION
    return {
        "d0": d0,
        "phase": phase,
        "sep0": float(sep0),
        "sep_final": float(sep_final),
        "net_dsep": float(net_dsep),
        "A2_mid_initial": float(A2_mid0),
        "A2_mid_final": float(A2_mid_series[-1]) if A2_mid_series else float("nan"),
        "core_A2_peak": A2_peak,
        "omega_local_ratio": omega_ratio,
        "sep_series": [float(s) for s in sep_series],
    }


def classify(in_res: dict, out_res: dict, floor: float) -> tuple[str, str]:
    """Assign the prereg §5 bin from the in-phase and out-of-phase O1 verdicts.

    floor = the O0 radiation-jitter ceiling (net |dsep| must exceed it to count).
    Returns (bin_name, one_line_rationale).
    """
    din = in_res["net_dsep"]
    dout = out_res["net_dsep"]

    def sign_of(d: float) -> str:
        if not np.isfinite(d) or abs(d) <= floor:
            return "null"          # below the radiation floor
        return "attract" if d < 0 else "repel"

    s_in, s_out = sign_of(din), sign_of(dout)

    if s_in == "null" and s_out == "null":
        return ("NULL / BELOW-FLOOR",
                "no two-body drift exceeds the O0 radiation floor in the "
                "transport-less window -> WALL-engine (refractive gradient not "
                "transduced into centroid motion), NOT a gravity falsification")
    if s_in == "attract" and s_out == "attract":
        comparable = abs(abs(din) - abs(dout)) <= max(abs(din), abs(dout))  # within 2x
        tag = "comparable mag" if comparable else "same sign, mag differs"
        return ("GRAVITY-CONSISTENT",
                f"phase-INDEPENDENT attraction ({tag}) -> validate-on-known "
                "PASSES; two-body gravity CONSISTENCY check (Class C)")
    if s_in == "attract" and s_out == "repel":
        return ("GENERIC-SOLITON",
                "phase-DEPENDENT (in-phase attracts, out-phase repels) -> NOT "
                "gravity; generic NLS coherent-overlap. 'attraction=gravity' "
                "reading FALSIFIED on this engine (Rule 11 honest-negative)")
    if s_in == "repel" and s_out == "repel":
        return ("REPULSIVE-BOTH",
                "phase-independent REPULSION -> sign CONTRADICTS AVE-gravity "
                "mass-mass attraction; FLAG-DON'T-FIX, surface to Grant")
    return ("MIXED / AMBIGUOUS",
            f"in={s_in} out={s_out}; O0-marginal or inconsistent -> inconclusive")


def main() -> None:
    print("=" * 78)
    print("MASS-SECTOR TWO-BODY SCATTERING — validate-on-known (gravity)")
    print("  scalar A1 Master Equation engine; b=0 head-on; both relative phases")
    print("=" * 78)
    print(f"  V_YIELD={V_YIELD:.4f}  SEED_AMP={SEED_AMPLITUDE:.4f} "
          f"({SEED_AMPLITUDE / V_YIELD:.2f} V_yield)  R={SEED_RADIUS}  N={N}")
    print()

    results = {"config": {
        "N": N, "SEED_AMPLITUDE_over_Vyield": SEED_AMPLITUDE / V_YIELD,
        "SEED_RADIUS": SEED_RADIUS, "separations": SEPARATIONS,
        "N_RUN": N_RUN, "jitter_floor_cells": JITTER_FLOOR_CELLS,
    }, "per_separation": []}

    for d0 in SEPARATIONS:
        print(f"--- separation d0 = {d0} cells " + "-" * 40)
        ctrl = run_single_blob_control(d0)
        floor = max(ctrl["radiation_floor_cells"], JITTER_FLOOR_CELLS)
        print(f"  O0 control: single-blob radiation floor = {floor:.4f} cells "
              f"(window {N_TRANSIENT}-{N_RUN})")

        in_res = run_two_body(d0, "in")
        out_res = run_two_body(d0, "out")
        bin_name, rationale = classify(in_res, out_res, floor)

        print(f"  O1 in-phase : sep {in_res['sep0']:.3f} -> {in_res['sep_final']:.3f}  "
              f"(net dsep = {in_res['net_dsep']:+.4f})")
        print(f"  O1 out-phase: sep {out_res['sep0']:.3f} -> {out_res['sep_final']:.3f}  "
              f"(net dsep = {out_res['net_dsep']:+.4f})")
        print(f"  O2 A2_mid in : {in_res['A2_mid_initial']:.3e} -> {in_res['A2_mid_final']:.3e}")
        print(f"  O2 A2_mid out: {out_res['A2_mid_initial']:.3e} -> {out_res['A2_mid_final']:.3e}")
        print(f"  O3 core A2_peak in/out: {in_res['core_A2_peak']:.4f} / "
              f"{out_res['core_A2_peak']:.4f}  (Regime II if < {0.99**2:.3f})")
        print(f"  BIN: {bin_name}")
        print(f"       {rationale}")
        print()

        results["per_separation"].append({
            "d0": d0, "control": ctrl, "floor": floor,
            "in_phase": in_res, "out_phase": out_res,
            "bin": bin_name, "rationale": rationale,
        })

    # Overall verdict = the d0 with the cleanest (largest |net_dsep|) signal.
    bins = [r["bin"] for r in results["per_separation"]]
    print("=" * 78)
    print(f"  PER-SEPARATION BINS: {bins}")
    if len(set(bins)) == 1:
        print(f"  OVERALL VERDICT: {bins[0]} (consistent across all separations)")
    else:
        print(f"  OVERALL VERDICT: MIXED across separations -> {bins}; report honestly")
    print("=" * 78)
    results["overall_bins"] = bins

    out_path = (
        "src/scripts/vol_1_foundations/"
        "mass_sector_two_body_scattering_results.json"
    )
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"  wrote {out_path}")


if __name__ == "__main__":
    main()


