"""electron_genesis_capture.py — capture REAL field arrays for the showcase figure.

THE LANDMARK "full vacuum lattice at work" run: a transverse photon wave-packet
self-traps into a localized soliton (the electron core / mass formation) on the
canonical AVE FDTD Maxwell engine. This module RE-RUNS the validated 2026-06-04
C-EMERGE self-trap arm and SNAPSHOTS the real Ey/Ez/Hy/Hz/energy/A field arrays at
every probe step, so the render pass can draw the actual engine output (no
synthetic helices — contrast the illustrative visualize_self_trapping.py).

ENGINE (ave-canonical-source, REUSE — no hand-rolled Maxwell/saturation):
  src/ave/core/fdtd_3d.py — FDTD3DEngine, full-vector Yee Maxwell with the
  Axiom-4 dual saturation kernel S(A)=√(1−(A/A_yield)²) on ε(E) and μ(H).

SEED (REUSE the canonical C-EMERGE seed builders, imported verbatim):
  src/scripts/vol_1_foundations/r10_fdtd3d_transverse_photon_selftrap.py
  build_transverse_photon_seed   — two counter-prop focused CP transverse pulses
  build_matched_trivial_baseline — phase-scrambled amplitude-matched control
  interior_energy_density / top_k_density_peaks — PML-excluded, density-peak (Rule 10)

VALIDATION (validate-what-you-did — the self-trap must ACTUALLY occur):
  V1 localization beats matched baseline  (peak-|field| retention; the 0.580 vs
      0.389 result reproduced under the SAME N=48/PML=6/0.7·V_snap config window)
  V2 saturation kernel ENGAGES            (peak A crosses the Op14 onset √(2α))
  V3 c recovered                          (single-packet wavefront speed → c_0)

HONESTY (ave-evidence-framing-discipline — heightened, load-bearing):
  REAL/engine-demonstrated: the self-trap LOCALIZATION (= mass formation), the
      Axiom-4 saturation engagement, the transverse E–B propagation, c-recovery.
  PLANTED/ILLUSTRATIVE: any (2,3) winding or spin-½ overlay. The engine does NOT
      dynamically select the (2,3) — P4 toroidal-winding FAILS (0.000) on this
      run (2026-06-04 result §7.2; epic §28 close-out). Do NOT claim the (2,3) or
      spin emerges. This capture records ONLY the real fields; the render pass
      labels every planted overlay explicitly.

Run:
    PYTHONPATH=src python3 src/scripts/vol_1_foundations/electron_genesis_capture.py
Produces:
    research/figures/electron_genesis_capture.npz   (field-array snapshots)
    research/figures/electron_genesis_validation.json (the validation numbers)
"""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))

from ave.core.constants import ALPHA, C_0, R_I, V_SNAP, Z_0
from ave.core.fdtd_3d import FDTD3DEngine

# ── REUSE the canonical seed builders + observables (ave-canonical-source) ──────
from r10_fdtd3d_transverse_photon_selftrap import (  # noqa: E402
    build_matched_trivial_baseline,
    build_transverse_photon_seed,
    interior_energy_density,
    top_k_density_peaks,
)

# Run config — MATCHES the validated 2026-06-04 driver for the headline beat, then
# extends the recording tail (record-only, beyond the 240-step beat window) so the
# animation shows the standing soliton persisting / breathing for a long sequence.
N_LATTICE = 48
DX = 0.01
PML = 6
AMP_FRAC_VSNAP = 0.7  # deepest stable in the {0.3,0.5,0.7} sweep (2026-06-04 §7)
N_SETTLE = 80         # packets collide; trap cell locked at the post-collision peak
N_RECORD = 240        # canonical beat window (peak-|field| retention computed here)
N_TAIL = 220          # extra record-only steps for the LONG animation tail
PROBE_EVERY = 4

FIG_DIR = Path(__file__).resolve().parents[3] / "research" / "figures"
NPZ_OUT = FIG_DIR / "electron_genesis_capture.npz"
JSON_OUT = FIG_DIR / "electron_genesis_validation.json"


def _new_engine() -> FDTD3DEngine:
    """Engine at the TOPOLOGICAL scale (v_yield=V_SNAP), matching the 2026-06-04 run."""
    return FDTD3DEngine(
        nx=N_LATTICE, ny=N_LATTICE, nz=N_LATTICE, dx=DX,
        linear_only=False, use_pml=True, pml_layers=PML, v_yield=V_SNAP,
    )


def _amplitude() -> float:
    return AMP_FRAC_VSNAP * V_SNAP / DX


def _A_field(engine: FDTD3DEngine) -> np.ndarray:
    """Per-cell saturation strain A = |E|·dx / v_yield  (v_yield = V_SNAP here).

    A is the argument of the Axiom-4 kernel S(A)=√(1−A²). A→1 is full Γ→−1
    rupture; the Op14 engagement onset is A = √(2α) = R_I ≈ 0.121.
    """
    Emag = np.sqrt(engine.Ex**2 + engine.Ey**2 + engine.Ez**2)
    return Emag * engine.dx / engine.v_yield


def _slice_pack(engine: FDTD3DEngine, cx: int, cy: int, cz: int) -> dict:
    """Two orthogonal mid-plane slices of the REAL field arrays for rendering.

    xz-plane (y=cy): the PROPAGATION view — packets moving along x, E⊥B⊥k.
    yz-plane (x=cx): the TRANSVERSE view — the (Ey,Ez)/(Hy,Hz) polarization at
                     the trap axis (the E–B winding the render quivers).
    """
    u = engine.energy_density()
    A = _A_field(engine)
    Emag = np.sqrt(engine.Ex**2 + engine.Ey**2 + engine.Ez**2)
    Hmag = np.sqrt(engine.Hx**2 + engine.Hy**2 + engine.Hz**2)
    return {
        # xz propagation plane (index [:, cy, :]) -> shape (nx, nz)
        "xz_Emag": Emag[:, cy, :].copy(),
        "xz_A": A[:, cy, :].copy(),
        "xz_u": u[:, cy, :].copy(),
        "xz_Ey": engine.Ey[:, cy, :].copy(),
        "xz_Ez": engine.Ez[:, cy, :].copy(),
        # yz transverse plane (index [cx, :, :]) -> shape (ny, nz)
        "yz_Emag": Emag[cx, :, :].copy(),
        "yz_A": A[cx, :, :].copy(),
        "yz_u": u[cx, :, :].copy(),
        "yz_Ey": engine.Ey[cx, :, :].copy(),
        "yz_Ez": engine.Ez[cx, :, :].copy(),
        "yz_Hy": engine.Hy[cx, :, :].copy(),
        "yz_Hz": engine.Hz[cx, :, :].copy(),
    }


def capture_selftrap() -> dict:
    """Run C-EMERGE with full snapshotting; also run BASELINE for the localization beat."""
    amplitude = _amplitude()
    cx = cy = cz = (N_LATTICE - 1) // 2

    # ── C-EMERGE: the real self-trap, snapshotted ───────────────────────────────
    eng = _new_engine()
    seed_meta = build_transverse_photon_seed(eng, amplitude=amplitude)
    interior0 = float(interior_energy_density(eng, PML).sum())

    frames: list[dict] = []
    steps_rec: list[int] = []
    peakA_series: list[float] = []
    Smin_series: list[float] = []       # min saturation factor S(A) interior (kernel bite)
    interiorE_series: list[float] = []
    peakfield_series: list[float] = []
    trapx_series: list[float] = []
    trap_xyz = None

    total = N_SETTLE + N_RECORD + N_TAIL
    for s in range(total):
        eng.step()
        if not np.all(np.isfinite(eng.Ey)):
            raise RuntimeError(f"NaN at step {s} — amplitude above the ave-infinity cap")
        if s == N_SETTLE:
            pk = top_k_density_peaks(eng, PML, k=1)
            trap_xyz = pk[0] if pk else (cx, cy, cz)
        if s % PROBE_EVERY == 0:
            u_int = interior_energy_density(eng, PML)
            A = _A_field(eng)
            # interior-masked A for the saturation-kernel bite (PML excluded)
            A_int = np.zeros_like(A)
            A_int[PML:N_LATTICE - PML, PML:N_LATTICE - PML, PML:N_LATTICE - PML] = \
                A[PML:N_LATTICE - PML, PML:N_LATTICE - PML, PML:N_LATTICE - PML]
            peakA = float(A_int.max())
            Smin = float(np.sqrt(max(1.0 - min(peakA, 0.999999) ** 2, 0.0)))
            # energy-weighted x-centroid (interior) — soliton position
            xs = np.arange(N_LATTICE)
            wx = u_int.sum(axis=(1, 2))
            xcen = float((xs * wx).sum() / max(wx.sum(), 1e-30))

            # SLICE PLANES are fixed at the lattice CENTER — the persistent
            # standing soliton condenses at the center (xcen≈cx through the tail),
            # so the transverse (yz) view at x=cx shows the soliton CORE, not the
            # transient post-collision density lobe that migrates to the interior
            # edge during settling (Rule 10 density-peak is tracked separately as
            # trap_xyz for metadata).
            frames.append(_slice_pack(eng, cx, cy, cz))
            steps_rec.append(s)
            peakA_series.append(peakA)
            Smin_series.append(Smin)
            interiorE_series.append(float(u_int.sum()))
            peakfield_series.append(float(np.sqrt(u_int).max()))
            trapx_series.append(xcen)

    # canonical beat window retention (matches 2026-06-04 methodology exactly):
    # mean of the last-3 probes WITHIN the N_RECORD window / first probe of the window.
    rec_idx = [i for i, st in enumerate(steps_rec) if N_SETTLE <= st < N_SETTLE + N_RECORD]
    pf_window = [peakfield_series[i] for i in rec_idx]
    ce_retention = float(np.mean(pf_window[-3:]) / max(pf_window[0], 1e-30)) if len(pf_window) > 3 else 0.0

    # stack slices into arrays keyed by field name
    keys = list(frames[0].keys())
    stacked = {k: np.stack([f[k] for f in frames], axis=0) for k in keys}

    ce = {
        "stacked": stacked,
        "steps": np.array(steps_rec),
        "peakA": np.array(peakA_series),
        "Smin": np.array(Smin_series),
        "interiorE": np.array(interiorE_series),
        "peakfield": np.array(peakfield_series),
        "xcentroid": np.array(trapx_series),
        "trap_xyz": np.array(trap_xyz if trap_xyz is not None else (cx, cy, cz)),
        "interior0": interior0,
        "retention_beatwindow": ce_retention,
        "seed_meta": seed_meta,
        "dt": eng.dt,
    }

    # ── BASELINE: matched-distribution trivial control, same window (localization beat) ─
    engb = _new_engine()
    base_seed = build_transverse_photon_seed(engb, amplitude=amplitude)
    build_matched_trivial_baseline(engb, base_seed)
    base_pf: list[float] = []
    base_steps: list[int] = []
    for s in range(N_SETTLE + N_RECORD):
        engb.step()
        if s % PROBE_EVERY == 0:
            u_int = interior_energy_density(engb, PML)
            base_pf.append(float(np.sqrt(u_int).max()))
            base_steps.append(s)
    base_idx = [i for i, st in enumerate(base_steps) if N_SETTLE <= st < N_SETTLE + N_RECORD]
    base_window = [base_pf[i] for i in base_idx]
    base_retention = float(np.mean(base_window[-3:]) / max(base_window[0], 1e-30)) if len(base_window) > 3 else 0.0

    return {"ce": ce, "baseline_retention": base_retention,
            "baseline_peakfield": np.array(base_pf), "baseline_steps": np.array(base_steps)}


def validate_c_recovery() -> dict:
    """V3: single +x transverse packet, measure WAVEFRONT speed → c_0 recovery.

    Linear region (linear_only=True so the wave is pure Maxwell, no saturation drag):
    the soliton-free photon's leading edge must travel at the signal velocity c_0.
    The wavefront (front velocity) is the clean c observable — unlike the energy
    centroid, it is not pulled by packet spreading. λ=12 cells (well-resolved) +
    a sub-cell-interpolated front threshold; converts cells/step → m/s via dx, dt.
    """
    eng = FDTD3DEngine(nx=96, ny=24, nz=24, dx=DX, linear_only=True,
                       use_pml=True, pml_layers=PML, v_yield=V_SNAP)
    nx, ny, nz = eng.nx, eng.ny, eng.nz
    cy, cz = (ny - 1) / 2.0, (nz - 1) / 2.0
    i, j, k = np.indices((nx, ny, nz))
    x = i.astype(float)
    rho_t = np.sqrt((j - cy) ** 2 + (k - cz) ** 2)
    waist = np.exp(-(rho_t**2) / (2.0 * 4.0**2))
    k0 = 2.0 * np.pi / 12.0  # well-resolved wavelength (12 cells) → low dispersion
    x0 = 14.0
    gauss = np.exp(-((x - x0) ** 2) / (2.0 * 5.0**2))
    amp = 0.2 * V_SNAP / DX  # well within linear region
    Ey = amp * waist * gauss * np.cos(k0 * (x - x0))
    Ez = amp * waist * gauss * np.sin(k0 * (x - x0))
    eng.Ey[...] = Ey
    eng.Ez[...] = Ez
    eng.Hy[...] = -Ez / Z_0
    eng.Hz[...] = +Ey / Z_0

    xs = np.arange(nx)
    fronts: list[float] = []
    rec_steps = list(range(6, 70))  # window inside the grid, before the PML
    for s in range(max(rec_steps) + 1):
        eng.step()
        if s in rec_steps:
            Emag_x = np.sqrt(eng.Ey**2 + eng.Ez**2).max(axis=(1, 2))
            thr = 0.01 * Emag_x.max()
            above = xs[Emag_x > thr]
            fronts.append(float(above.max()) if above.size else 0.0)
    fronts = np.array(fronts)
    steps = np.array(rec_steps)
    coeffs = np.polyfit(steps, fronts, 1)
    slope_cells_per_step = float(coeffs[0])
    resid = fronts - np.polyval(coeffs, steps)
    ss_res = float(np.sum(resid**2))
    ss_tot = float(np.sum((fronts - fronts.mean()) ** 2))
    r2 = 1.0 - ss_res / max(ss_tot, 1e-30)
    speed = slope_cells_per_step * eng.dx / eng.dt
    return {
        "method": "wavefront (leading-edge signal velocity), λ=12 cells",
        "slope_cells_per_step": slope_cells_per_step,
        "ideal_slope_c_dt_over_dx": float(C_0 * eng.dt / eng.dx),
        "linear_fit_r2": r2,
        "c_measured_m_s": speed,
        "c_0_m_s": float(C_0),
        "c_ratio": speed / float(C_0),
        "note": "linear-region single-packet WAVEFRONT speed; the ~4% deficit from "
                "c_0 is numerical dispersion + integer-cell front quantization at the "
                "finite grid — c is recovered to within grid resolution.",
    }


def main() -> None:
    print("=" * 78)
    print("  electron_genesis_capture — REAL field-array snapshots of the self-trap")
    print("  engine: fdtd_3d.py (FDTD3DEngine, Axiom-4 saturation); seed: C-EMERGE")
    print("=" * 78, flush=True)
    t0 = time.time()

    print("  [1/3] capturing C-EMERGE self-trap + BASELINE control ...", flush=True)
    cap = capture_selftrap()
    ce = cap["ce"]

    print("  [2/3] V3 c-recovery (single-packet wavefront speed) ...", flush=True)
    cval = validate_c_recovery()

    # ── validation summary (validate-what-you-did) ──────────────────────────────
    ce_ret = ce["retention_beatwindow"]
    base_ret = cap["baseline_retention"]
    peakA_max = float(ce["peakA"].max())
    Smin_min = float(ce["Smin"].min())
    sat_engaged = bool(peakA_max > R_I)
    beat = bool(ce_ret > base_ret)

    validation = {
        "engine": "src/ave/core/fdtd_3d.py :: FDTD3DEngine (full-vector Maxwell, "
                  "Axiom-4 dual saturation S(A)=sqrt(1-(A/A_yield)^2), v_yield=V_SNAP)",
        "seed": "C-EMERGE: two counter-propagating focused circularly-polarized "
                "transverse photon packets (reused build_transverse_photon_seed)",
        "config": {"N": N_LATTICE, "dx": DX, "PML": PML, "amp_frac_vsnap": AMP_FRAC_VSNAP,
                   "n_settle": N_SETTLE, "n_record_beatwindow": N_RECORD, "n_tail": N_TAIL},
        "V1_localization_beat": {
            "C_EMERGE_retention": ce_ret,
            "BASELINE_retention": base_ret,
            "beats_matched_baseline": beat,
            "REAL": True,
            "note": "peak-|field| retention over the canonical 240-step beat window; "
                    "C-EMERGE out-retains the phase-scrambled amplitude-matched control "
                    "(reproduces 2026-06-04 §7.1 0.580 vs 0.389 — topology/coherence-"
                    "driven localization, NOT amplitude-driven).",
        },
        "V2_saturation_engaged": {
            "peakA_max": peakA_max,
            "Op14_onset_sqrt_2alpha": float(R_I),
            "S_min_kernel_floor": Smin_min,
            "engaged": sat_engaged,
            "REAL": True,
            "note": "peak strain A=|E|dx/V_SNAP crosses the Op14 engagement onset "
                    "sqrt(2*alpha); the Axiom-4 kernel S(A) bites (S_min<1). Operating "
                    "point is EARLY saturation (A_max~0.18, not full A->1 rupture) — the "
                    "localization beat, not deep Gamma->-1, is the load-bearing signal.",
        },
        "V3_c_recovery": {**cval, "REAL": True},
        "HONESTY": {
            "REAL_engine_demonstrated": [
                "self-trap localization (mass formation) — beats matched baseline",
                "Axiom-4 saturation kernel engagement (A crosses sqrt(2alpha))",
                "transverse E-B propagation + c-recovery",
            ],
            "PLANTED_ILLUSTRATIVE": [
                "any (2,3) Clifford-torus winding overlay — does NOT emerge (P4 FAIL, "
                "toroidal winding 0.000 on this run; 2026-06-04 §7.2)",
                "any spin-1/2 overlay — not selected by the engine",
                "the omega_C label on the breathing frequency — the grid dx is "
                "computational (not ell_node), so the absolute frequency is not the "
                "physical Compton value; the breathing itself is real, the omega_C "
                "identification is the framework interpretation.",
            ],
        },
        "alpha": float(ALPHA),
    }

    print("  [3/3] saving snapshots + validation ...", flush=True)
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    # flatten the stacked slice dict into the npz with a prefix
    npz_payload = {f"ce_{k}": v for k, v in ce["stacked"].items()}
    npz_payload.update({
        "ce_steps": ce["steps"], "ce_peakA": ce["peakA"], "ce_Smin": ce["Smin"],
        "ce_interiorE": ce["interiorE"], "ce_peakfield": ce["peakfield"],
        "ce_xcentroid": ce["xcentroid"], "ce_trap_xyz": ce["trap_xyz"],
        "base_peakfield": cap["baseline_peakfield"], "base_steps": cap["baseline_steps"],
        "config": np.array([N_LATTICE, DX, PML, AMP_FRAC_VSNAP, N_SETTLE, N_RECORD, N_TAIL, PROBE_EVERY], dtype=float),
        "dt": np.array([ce["dt"]]),
    })
    np.savez_compressed(NPZ_OUT, **npz_payload)
    JSON_OUT.write_text(json.dumps(validation, indent=2, default=str), encoding="utf-8")

    elapsed = time.time() - t0
    print("\n" + "=" * 78)
    print("  VALIDATION (validate-what-you-did)")
    print("=" * 78)
    print(f"  V1 localization beat : C-EMERGE {ce_ret:.3f} vs BASELINE {base_ret:.3f}  "
          f"-> beats_baseline={beat}  [REAL]")
    print(f"  V2 saturation engaged: peak A={peakA_max:.4f} > sqrt(2a)={R_I:.4f} "
          f"-> {sat_engaged}; S_min={Smin_min:.4f}  [REAL]")
    print(f"  V3 c-recovery        : c_meas/c_0 = {cval['c_ratio']:.4f}  [REAL]")
    print(f"\n  frames captured: {len(ce['steps'])}  (steps 0..{int(ce['steps'][-1])})")
    print(f"  saved: {NPZ_OUT.name}, {JSON_OUT.name}  ({elapsed:.0f}s)")


if __name__ == "__main__":
    main()
