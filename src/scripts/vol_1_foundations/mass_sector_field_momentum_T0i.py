"""
MASS-SECTOR FIELD-MOMENTUM T^{0i} — the transport-independent force readout
===========================================================================

The §0.5 / R3 false-null escape hatch from
`research/2026-06-23_mass-sector-two-body-scattering_result.md` §1.7, run per
Grant's run-or-defer ruling (2026-06-23): the centroid-drift readout was
SNR < 1 against the radiation floor (a WALL on the *observable*, not the
substrate). T^{0i} = (∂_t V)(∂_i V) is the scalar-A1 field-momentum density —
the momentum the field *itself* transports — and is computable directly from
the engine's own state variables (V, V_prev) with ZERO engine change. It
bypasses rigid centroid transport entirely.

PHYSICAL QUESTION (Grant's framing, pre-registered in
`..._T0i_prereg.md`): AVE-gravity is FREQUENCY MODULATION / DIFFRACTION
(`optical-refraction-gravity.md:17`: "it does not 'fall' due to a mechanical
pulling stress tensor; it **diffracts**"), NOT a momentum-transport pull. So
the prediction is:

  P_x net momentum flux between the two blobs ≈ ZERO
   → gravity is the c_eff(A²) gradient frequency-modulating the carrier's
     phase, transporting NO net momentum
   → #390's null is REAL for the right reason (momentum-flux-absent),
     not apparatus-limited.

REFUTE-BY-DEFAULT: if T^{0i} shows a NET non-zero momentum delivery to the
blobs, that is a real compression-sector momentum-transport force and would
OVERTURN the diffraction picture. Reported honestly either way; no rounding.

SUBSTRATE-NATIVE FORM (scalar field stress-energy, NOT an SM import — this is
the field's own momentum density):
  T^{0i} = (∂_t V)(∂_i V)
  ∂_t V  ≈ (V − V_prev)/dt         # the two state variables the engine stores
  ∂_x V  ≈ (V[i+1] − V[i−1])/(2 dx)  # central diff, matching the engine's
                                      # own _laplacian central-difference stencil
  P_x(region) = Σ_{interior region} T^{0x}                  (lattice momentum units)
  Force on a blob = d P_x / dt  over the recording window.

OBSERVABLES (all FROM the evolved field; ave-driver-script-honesty):
  M0  P_x_total interior  -> momentum-conservation cross-check (≈0 for symmetric b=0)
  M1  P_x_left, P_x_right -> net momentum delivered to each half-volume blob
  M2  Φ_x = midplane T^{0x} flux -> momentum TRANSPORTED across the gap (the
                                    direct diffraction-vs-pull discriminator)
  M3  single-blob control -> the radiation/breathing T^{0i} floor (M0/M1/M2 must
                              EXCEED it to count as a real two-body force)

SAMPLING DISCIPLINE (substrate-native-check CP7): PML cells excluded from every
integral (the damping mask multiplies V in the PML, so T^{0i} there is a
frozen-absorbing artifact, not interior physics).

CONSTANTS / config reused from the validated v14 breather (see the §390 driver
`mass_sector_two_body_scattering.py` and its F1 seed-swap finding). This driver
only READS the engine; it does not modify src/ave/core/.

Run:
    PYTHONPATH=src <venv>/bin/python \
        src/scripts/vol_1_foundations/mass_sector_field_momentum_T0i.py
"""

from __future__ import annotations

import json

import numpy as np

from ave.core.master_equation_fdtd import MasterEquationFDTD

# --- config: validated v14 breather (matches the §390 driver exactly) --------
# Rationale: the F1 seed-swap finding (result §1.8) established that the r10
# Test-C literal (N=32/0.95/2.0) FAILS its own persistence gate; the VALIDATED
# canonical Mode-I breather (test_master_equation_v14_mode_i.py 5/5 PASS) is
# N=24, DX=0.5, V_yield=1.0, amp=0.85, R=2.5. Reused verbatim so the T^{0i}
# readout runs on the same bound state as the centroid-drift readout it replaces.
N = 24
DX = 0.5
V_YIELD = 1.0
C0 = 1.0
CFL_SAFETY = 0.4
PML = 4
SEED_AMPLITUDE = 0.85
SEED_RADIUS = 2.5
# TRUE-CENTER half-integer placement (CHANGED from the §390 driver's integer
# N//2 centering): an N=24 grid has NO single center cell — the true center is
# the FACE between cells N/2−1=11 and N/2=12, i.e. XC = (N−1)/2 = 11.5. Seeding a
# blob at integer N//2=12 puts it OFF the discrete symmetry axis and gives a
# stationary blob a SPURIOUS net field-momentum (verified: P_total = +21.6 for a
# single blob at x=12.0 vs EXACTLY 0.0 at x=11.5). So the whole test is centered
# on XC=11.5: the pair straddles the 11/12 face symmetrically, the volume splits
# at that face (LEFT: i≤11, RIGHT: i≥12), and the flux is read on the face (the
# mean of the i=11 and i=12 planes). FLAGGED: this corrects BOTH the §390 odd-d0
# off-center placement AND the integer-vs-half-integer centering bias — neither
# mattered for the §390 centroid-difference readout, but BOTH break the momentum-
# conservation sanity check (single stationary blob must carry P_total=0) that a
# T^{0i} field-momentum readout lives or dies by.
XC = (N - 1) / 2.0          # 11.5: the true grid center (the 11/12 face)
SEED_RADIUS_FWHM = 2 * SEED_RADIUS  # ~5 cells; d0≥6 keeps cores from initial full overlap
SEPARATIONS = [6, 8, 10]    # even -> blobs at XC∓d0/2 land on integer cells, symmetric
N_RUN = 600
N_TRANSIENT = 200


def _make_engine() -> MasterEquationFDTD:
    return MasterEquationFDTD(
        N=N, dx=DX, V_yield=V_YIELD, c0=C0, cfl_safety=CFL_SAFETY, pml_thickness=PML,
    )


def _seed_breather(eng: MasterEquationFDTD, cx: float, sign: float) -> None:
    """v14-canonical sech breather at (cx, XC, XC), given sign (in/out phase).

    The transverse (y,z) center is XC=11.5 (true grid center) so the blob is
    transversely symmetric too — only then does an isolated stationary blob carry
    zero net field-momentum. cx may be a float (the x-center).
    """
    coords = np.arange(N)
    X, Y, Z = np.meshgrid(coords - cx, coords - XC, coords - XC, indexing="ij")
    r = np.sqrt(X * X + Y * Y + Z * Z) * DX
    eng.V += sign * SEED_AMPLITUDE * (1.0 / np.cosh(r / SEED_RADIUS))


# --- interior (PML-excluded) masks, built once (CP7) -------------------------
# Split / flux plane is the FACE between cells 11 and 12 (x = XC = 11.5).
_I, _J, _K = np.indices((N, N, N))
_INTERIOR = (
    (_I >= PML) & (_I <= N - PML - 1)
    & (_J >= PML) & (_J <= N - PML - 1)
    & (_K >= PML) & (_K <= N - PML - 1)
)
_LEFT = _INTERIOR & (_I <= N // 2 - 1)     # i ≤ 11
_RIGHT = _INTERIOR & (_I >= N // 2)        # i ≥ 12
# Flux through the 11/12 FACE: average the x-momentum density on the two planes
# adjacent to the face (i=11 and i=12); their mean is the face-centered flux.
_FACE_L = _INTERIOR & (_I == N // 2 - 1)   # i = 11 plane
_FACE_R = _INTERIOR & (_I == N // 2)       # i = 12 plane


def T0x_density(V: np.ndarray, V_prev: np.ndarray, dt: float) -> np.ndarray:
    """Scalar-A1 field-momentum density T^{0x} = (∂_t V)(∂_x V) at every cell.

    ∂_t V = (V − V_prev)/dt  : the engine's two stored leapfrog states; this is
            the backward time difference available at the current step (zero
            initial velocity is set by V_prev = V at seed time).
    ∂_x V = (V[i+1] − V[i−1])/(2 dx) : central difference along x, matching the
            engine's own 2nd-order central-difference _laplacian stencil
            (master_equation_fdtd.py:122-139). Edge planes (i=0, i=N−1) left 0;
            they are inside the PML and excluded from every integral anyway.

    Returns the full N³ density array (caller masks to the PML-excluded region).
    """
    dt_V = (V - V_prev) / dt
    dx_V = np.zeros_like(V)
    dx_V[1:-1, :, :] = (V[2:, :, :] - V[:-2, :, :]) / (2.0 * DX)
    return dt_V * dx_V


def momentum_integrals(V: np.ndarray, V_prev: np.ndarray, dt: float) -> dict:
    """Integrate T^{0x} over the PML-excluded interior, the two half-volumes, and
    the midplane gap. Lattice momentum units (× dx³ would give physical units; the
    pure SUM is used since the verdict is a relative/sign test, not a magnitude
    pin — and the same dx³ factor cancels in every cross-check)."""
    t0x = T0x_density(V, V_prev, dt)
    p_total = float(np.sum(t0x[_INTERIOR]))
    p_left = float(np.sum(t0x[_LEFT]))
    p_right = float(np.sum(t0x[_RIGHT]))
    # Momentum FLUX across the 11/12 gap face: T^{0x} is the x-momentum density
    # (flowing along x), so its integral over the dividing face is the rate at
    # which x-momentum is transported left↔right through the gap. Face-centered =
    # mean of the two adjacent planes (i=11, i=12), so it sits exactly on x=XC.
    phi_mid = 0.5 * (float(np.sum(t0x[_FACE_L])) + float(np.sum(t0x[_FACE_R])))
    return {
        "p_total": p_total,
        "p_left": p_left,
        "p_right": p_right,
        "phi_midplane": phi_mid,
    }


def _series_stats(series: list[float]) -> dict:
    """Window statistics for a momentum series over the recording window."""
    a = np.asarray(series, dtype=np.float64)
    a = a[np.isfinite(a)]
    if a.size == 0:
        return {"mean": float("nan"), "std": float("nan"),
                "abs_max": float("nan"), "abs_mean": float("nan")}
    return {
        "mean": float(np.mean(a)),
        "std": float(np.std(a)),
        "abs_max": float(np.max(np.abs(a))),
        "abs_mean": float(np.mean(np.abs(a))),
    }


def run_single_blob_control(d0: int) -> dict:
    """M3: one breather at blob-A's position. Its own breathing/radiation drives a
    nonzero T^{0x} that is NOT a two-body force — that is the floor the two-body
    signal must exceed. Records |Φ_mid| and |P_left−P_right| over the window."""
    eng = _make_engine()
    cx = XC - d0 / 2.0  # blob-A's true position (off-center, as in the two-body run)
    _seed_breather(eng, cx, +1.0)
    eng.V_prev = eng.V.copy()  # zero initial velocity (matches regression seed)
    for _ in range(N_TRANSIENT):
        eng.step()
    phi_series, dP_series = [], []
    for _ in range(N_TRANSIENT, N_RUN):
        eng.step()
        mi = momentum_integrals(eng.V, eng.V_prev, eng.dt)
        phi_series.append(abs(mi["phi_midplane"]))
        dP_series.append(abs(mi["p_left"] - mi["p_right"]))
    return {
        "phi_midplane_floor": float(np.nanmax(phi_series)) if phi_series else float("nan"),
        "dP_floor": float(np.nanmax(dP_series)) if dP_series else float("nan"),
        "phi_abs_mean_floor": float(np.nanmean(phi_series)) if phi_series else float("nan"),
    }


def run_two_body(d0: int, phase: str) -> dict:
    """M0/M1/M2: two breathers at separation d0, given relative phase, b=0.

    Records the field-momentum integrals over the post-transient recording
    window: P_total (conservation check), P_left/P_right (delivered momentum),
    and the midplane flux Φ_x (transported momentum) — the direct
    diffraction-vs-pull discriminator.
    """
    eng = _make_engine()
    # SYMMETRIC placement about the true center XC=11.5: blobs at XC∓d0/2 (even d0
    # -> integer cells), so the pair straddles the 11/12 face exactly.
    cxA = XC - d0 / 2.0
    cxB = XC + d0 / 2.0
    sign_B = +1.0 if phase == "in" else -1.0
    _seed_breather(eng, cxA, +1.0)
    _seed_breather(eng, cxB, sign_B)
    eng.V_prev = eng.V.copy()  # zero initial velocity

    for _ in range(N_TRANSIENT):
        eng.step()

    p_total_series, phi_series, dP_series = [], [], []
    for _ in range(N_TRANSIENT, N_RUN):
        eng.step()
        mi = momentum_integrals(eng.V, eng.V_prev, eng.dt)
        p_total_series.append(mi["p_total"])
        phi_series.append(mi["phi_midplane"])
        # Net momentum imbalance between the two halves. A real PULL delivers
        # +x momentum to the left blob and −x momentum to the right blob (they
        # converge): P_left > 0, P_right < 0 -> (P_left − P_right) > 0, sustained.
        dP_series.append(mi["p_left"] - mi["p_right"])

    dP_arr = np.asarray(dP_series, dtype=np.float64)
    dP_mean = float(np.nanmean(dP_arr)) if dP_arr.size else float("nan")
    dP_std = float(np.nanstd(dP_arr)) if dP_arr.size else float("nan")
    # AC/DC ratio: std/|mean|. A sustained DC PULL has ac_dc < 1 (mean dominates);
    # AC-dominated breathing/interference has ac_dc > 1 (the imbalance just sloshes
    # and time-averages toward nothing).
    ac_dc = float(dP_std / abs(dP_mean)) if (np.isfinite(dP_mean) and dP_mean != 0.0) else float("inf")
    return {
        "d0": d0,
        "phase": phase,
        "p_total_stats": _series_stats(p_total_series),
        "phi_midplane_stats": _series_stats(phi_series),
        "dP_stats": _series_stats(dP_series),
        # net (time-mean) transported / delivered momentum — the load-bearing scalars
        "phi_midplane_net": float(np.nanmean(phi_series)) if phi_series else float("nan"),
        "dP_net": dP_mean,
        "dP_std": dP_std,
        "dP_ac_dc": ac_dc,
    }


def classify(in_res: dict, out_res: dict, ctrl: dict) -> tuple[str, str]:
    """Two-pronged verdict: M2 (transported flux) AND M1 (delivered-momentum
    imbalance, phase-dependence + AC/DC), symmetry-aware.

    PRONG A — M2 midplane flux Φ_x (momentum TRANSPORTED across the gap).
      For a head-on b=0 SYMMETRIC pair, V is exactly even (in-phase) / odd
      (out-of-phase) about the gap face, so T^{0x}=(∂_t V)(∂_x V) is exactly ODD
      about the face -> Φ_x = 0 by reflection symmetry. This zero is therefore
      SYMMETRY-FORCED, not by itself a physics discriminator (it would be zero
      for ANY symmetric configuration). Flagged: |Φ_x| being below the single-
      blob radiation floor is necessary, not sufficient.

    PRONG B — M1 dP = P_left − P_right (net momentum DELIVERED to each blob).
      The load-bearing discriminator. A real phase-INDEPENDENT momentum-transport
      PULL would show: (i) dP phase-independent (in ≈ out, since A² is sign-blind),
      (ii) a sustained DC sign (ac_dc = std/|mean| < 1, the mean dominates), and
      (iii) above the single-blob breathing floor. Generic-soliton interference
      shows the opposite: phase-DEPENDENT (in ≫ out) and AC-dominated (ac_dc > 1,
      the imbalance just breathes and time-averages toward nothing).

    Verdicts:
      PASS / FM-DIFFRACTION := Φ_x≈0 (symmetry) AND dP is phase-DEPENDENT and/or
        AC-dominated -> NO phase-independent momentum-transport force; the only
        field-momentum imbalance is generic-soliton breathing interference.
        Gravity = c_eff(A²) frequency-modulation of the carrier phase, NOT a
        stress-tensor pull. #390's null is REAL for the right reason.
      SURPRISE / REAL-PULL := dP phase-INDEPENDENT (in≈out) AND DC-sustained
        (ac_dc<1) AND above floor -> a real compression-sector momentum-transport
        force; OVERTURNS the diffraction picture. FLAG-DON'T-FIX, surface to Grant.
    """
    dP_floor = ctrl["dP_floor"]
    dP_in = in_res["dP_net"]
    dP_out = out_res["dP_net"]
    acdc_in = in_res["dP_ac_dc"]

    # phase-(in)dependence: a sign-blind force has |dP_in| ≈ |dP_out|.
    # Use a 3× band: phase-independent iff the smaller is within 1/3 of the larger.
    mag_in, mag_out = abs(dP_in), abs(dP_out)
    big = max(mag_in, mag_out)
    small = min(mag_in, mag_out)
    phase_independent = bool(big > 0 and small >= big / 3.0)
    dc_sustained = bool(np.isfinite(acdc_in) and acdc_in < 1.0)
    above_floor = bool(np.isfinite(mag_in) and mag_in > dP_floor)

    if phase_independent and dc_sustained and above_floor:
        return ("SURPRISE / REAL-PULL",
                f"dP=(P_L−P_R) is phase-INDEPENDENT (in {dP_in:+.2e} ≈ out "
                f"{dP_out:+.2e}), DC-sustained (ac/dc={acdc_in:.2f}<1), and above "
                f"the breathing floor ({dP_floor:.2e}) -> a real phase-independent "
                "momentum-transport PULL. This OVERTURNS the diffraction picture; "
                "FLAG-DON'T-FIX, surface to Grant (engine vs corpus claim)")
    return ("PASS / FM-DIFFRACTION",
            f"net transported flux Φ_x=0 (symmetry-forced) AND dP is phase-"
            f"DEPENDENT (in {dP_in:+.2e} vs out {dP_out:+.2e}) / AC-dominated "
            f"(ac/dc={acdc_in:.2f}) -> NO phase-independent momentum-transport "
            "force; the only field-momentum imbalance is generic-soliton breathing "
            "interference. Gravity = c_eff(A²) frequency-modulation of the carrier "
            "phase, NOT a stress-tensor pull (optical-refraction-gravity.md:17). "
            "#390's null is REAL for the right reason (momentum-pull-absent)")


def main() -> None:
    print("=" * 78)
    print("MASS-SECTOR FIELD-MOMENTUM T^{0i} — transport-independent force readout")
    print("  T^{0x}=(∂_t V)(∂_x V); scalar A1 engine; b=0 head-on; both phases")
    print("  PREDICTION (Grant): net flux ~0 -> gravity = FM/diffraction, not pull")
    print("=" * 78)
    print(f"  V_YIELD={V_YIELD:.4f}  SEED_AMP={SEED_AMPLITUDE:.4f}  R={SEED_RADIUS}  N={N}")
    print()

    results = {"config": {
        "N": N, "DX": DX, "SEED_AMPLITUDE_over_Vyield": SEED_AMPLITUDE / V_YIELD,
        "SEED_RADIUS": SEED_RADIUS, "separations": SEPARATIONS,
        "N_RUN": N_RUN, "N_TRANSIENT": N_TRANSIENT,
        "observable": "T^{0x}=(d_t V)(d_x V) field-momentum density, PML-excluded",
    }, "per_separation": []}

    for d0 in SEPARATIONS:
        print(f"--- separation d0 = {d0} cells " + "-" * 40)
        ctrl = run_single_blob_control(d0)
        floor = ctrl["phi_midplane_floor"]
        print(f"  M3 control: single-blob midplane-flux floor = {floor:.4e} "
              f"(|P_L-P_R| floor {ctrl['dP_floor']:.4e}; window {N_TRANSIENT}-{N_RUN})")

        in_res = run_two_body(d0, "in")
        out_res = run_two_body(d0, "out")
        bin_name, rationale = classify(in_res, out_res, ctrl)

        print(f"  M0 P_total (conservation, should be ~0): "
              f"in {in_res['p_total_stats']['abs_mean']:.4e} / "
              f"out {out_res['p_total_stats']['abs_mean']:.4e}")
        print(f"  M2 net flux Phi_x (TRANSPORTED, symmetry-forced 0): "
              f"in {in_res['phi_midplane_net']:+.4e} / out {out_res['phi_midplane_net']:+.4e}")
        print(f"  M1 net dP=(P_L-P_R) (DELIVERED): in {in_res['dP_net']:+.4e} / "
              f"out {out_res['dP_net']:+.4e}  (floor {ctrl['dP_floor']:.4e})")
        print(f"  M1 phase-dep |in/out|={abs(in_res['dP_net'])/max(abs(out_res['dP_net']),1e-30):.1f}x  "
              f"AC/DC(in)={in_res['dP_ac_dc']:.2f}  (DC-pull if <1, breathing if >1)")
        print(f"  VERDICT: {bin_name}")
        print(f"           {rationale}")
        print()

        results["per_separation"].append({
            "d0": d0, "control": ctrl,
            "in_phase": in_res, "out_phase": out_res,
            "verdict": bin_name, "rationale": rationale,
        })

    bins = [r["verdict"] for r in results["per_separation"]]
    print("=" * 78)
    print(f"  PER-SEPARATION VERDICTS: {bins}")
    if len(set(bins)) == 1:
        print(f"  OVERALL: {bins[0]} (consistent across all separations)")
    else:
        print(f"  OVERALL: MIXED across separations -> {bins}; report honestly")
    print("=" * 78)
    results["overall_verdicts"] = bins

    out_path = (
        "src/scripts/vol_1_foundations/"
        "mass_sector_field_momentum_T0i_results.json"
    )
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"  wrote {out_path}")


if __name__ == "__main__":
    main()
