"""Move 6 — Natural-attractor characterization (post-Move-5 settled orbit).

Per `P_phase6_natural_attractor_characterization` (frozen at this commit).

CONTEXT: Move 5 ([`r8_self_consistent_orbit_hunt.py`](r8_self_consistent_orbit_hunt.py))
returned Mode III-orbit per pre-reg (persistence 0.329 < 0.50) BUT
empirically observed:
    Plateau (t ∈ [50P, 200P]):
      peak |ω| = 0.3044 to 4 decimals across 150 consecutive
      Compton periods, c = 3 preserved continuously, shell_frac
      drifted 0.31 → 0.14 (orbit migrated off corpus shell).

The system relaxed AWAY from corpus seed (R=10, r=R/φ², peak |ω|=0.3π)
to a different (2,3)-topological attractor at smaller amplitude and
different geometry. Corpus framework substantively right; corpus's
specific (R, r, amp) parameters wrong.

MOVE 6 GOAL: characterize the natural attractor — answer "where is the
engine's actual self-stable (2,3) orbit?" before deciding Round 8 next
test (Move 3 hybrid eigsolve, Move 4 (p,q) sweep, etc.).

THREE INTEGRATED EXTRACTIONS:

  (a) GEOMETRY: fit (R_relaxed, r_relaxed) of the natural attractor
      by shell-localization maximization on the t=200P ω-energy
      density. Compare R_relaxed/r_relaxed against corpus φ²=2.618.

  (b) PHASOR: for the relaxed shell, sample V_inc at 8 spatial points
      along it, compute spatial R/r per doc 26_ §3 (mean and std of
      time-averaged |V_inc| envelope across spatial samples). This is
      doc 28_ §5.1's actual test (corpus phase-space (2,3) Golden Torus)
      run on the SYSTEM'S NATURAL ATTRACTOR rather than on a
      corpus-imposed seed.

  (c) SPECTRUM: FFT of peak |ω|(t) over the recording window. Confirm
      dominant frequency at ω_C (= 1.0 in natural units) and look for
      (2,3)-signature 3:2 harmonic ratio.

ADJUDICATION (3-mode primary on geometry; phasor + spectrum are
diagnostic sub-criteria):

  Mode I-natural:    R_relaxed/r_relaxed = φ² ± 0.10 (well-defined shell)
                     → CORPUS ASPECT-RATIO VINDICATED at non-corpus
                       absolute scale. Corpus R/r=φ² claim correct;
                       only the absolute (R_anchor) was wrong.

  Mode II-natural:   well-defined shell with shell_frac_opt ≥ 0.4
                     AND R_relaxed/r_relaxed ≠ φ² ± 0.10
                     → engine prefers different aspect ratio. Corpus
                       φ² ratio empirically falsified.

  Mode III-natural:  no well-defined shell (max shell_frac across
                     (R, r) sweep < 0.4)
                     → natural attractor is delocalized despite
                       topological invariant; different methodology.

DIAGNOSTIC SUB-CRITERIA (informational):
  - R_phase/r_phase from spatial phasor envelope on the relaxed shell
    (matches doc 28_ §5.1 corpus claim if = φ² ± 0.10)
  - Dominant FFT frequency in peak |ω|(t) (= ω_C if corpus standing-wave)
  - (2,3) Lissajous spectral signature (3/2 harmonic ratio)
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from ave.topological.vacuum_engine import VacuumEngine3D
from tlm_electron_soliton_eigenmode import initialize_2_3_voltage_ansatz


# ─── Constants (match Move 5 pred exactly for deterministic reproduction) ────

PHI = 0.5 * (1.0 + np.sqrt(5.0))
PHI_SQ = PHI * PHI

N_LATTICE = 32
PML = 4
R_ANCHOR = 10.0
R_MINOR = R_ANCHOR / PHI_SQ                      # ≈ 3.82

A26_AMP_SCALE = 0.3 / (np.sqrt(3.0) / 2.0)
GT_PEAK_OMEGA = 0.3 * np.pi
V_AMP_INIT = 0.14

OMEGA_C = 1.0
COMPTON_PERIOD = 2.0 * np.pi / OMEGA_C
N_PERIODS_TOTAL = 200.0
DT = 1.0 / np.sqrt(2.0)
N_STEPS = int(N_PERIODS_TOTAL * COMPTON_PERIOD / DT) + 1

# Recording window: t ∈ [100P, 200P]
T_RECORD_START_PERIOD = 100.0
STEP_RECORD_START = int(T_RECORD_START_PERIOD * COMPTON_PERIOD / DT)

# Snapshot timesteps for full-field saves
SNAPSHOT_PERIODS = [100.0, 150.0, 200.0]
SNAPSHOT_STEPS = sorted({int(p * COMPTON_PERIOD / DT) for p in SNAPSHOT_PERIODS})

# Adjudication
R_OVER_R_TARGET = PHI_SQ
R_OVER_R_TOL = 0.10
SHELL_FRAC_OPT_THRESH = 0.4

# Shell-fit search ranges
R_SEARCH_VALUES = np.linspace(2.0, 14.0, 25)
R_MINOR_SEARCH_VALUES = np.linspace(0.5, 6.0, 23)
SHELL_BAND_WIDTH = 1.0   # half-width of the shell band in lattice cells

OUTPUT_JSON = Path(__file__).parent / "r8_natural_attractor_characterization_results.json"


def build_engine():
    return VacuumEngine3D.from_args(
        N=N_LATTICE, pml=PML, temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,
        enable_cosserat_self_terms=True,
    )


def seed_corpus_2_3_joint(engine):
    engine.cos.initialize_electron_2_3_sector(
        R_target=R_ANCHOR, r_target=R_MINOR,
        use_hedgehog=True, amplitude_scale=A26_AMP_SCALE,
    )
    initialize_2_3_voltage_ansatz(
        engine.k4, R=R_ANCHOR, r=R_MINOR, amplitude=V_AMP_INIT,
    )


def shell_localized_fraction(omega_energy, R_test, r_test, center, band):
    """Fraction of ω-energy within `band` of the (R_test, r_test) torus shell."""
    nx = omega_energy.shape[0]
    i, j, k = np.indices((nx, nx, nx))
    rho_xy = np.sqrt((i - center[0]) ** 2 + (j - center[1]) ** 2)
    rho_tube = np.sqrt((rho_xy - R_test) ** 2 + (k - center[2]) ** 2)
    in_shell = rho_tube < band
    e_shell = float(omega_energy[in_shell].sum())
    e_total = float(omega_energy.sum())
    return e_shell / max(e_total, 1e-30), in_shell


def fit_natural_shell(omega_field):
    """Sweep (R, r) at the lattice center and find the shell that maximizes
    shell-localized fraction. Returns (R_opt, r_opt, shell_frac_opt, center)."""
    nx = omega_field.shape[0]
    cx = (nx - 1) / 2.0
    center = (cx, cx, cx)

    omega_energy = np.sum(omega_field ** 2, axis=-1)

    # Search over R only first (the "tube" half-width is implicit via
    # SHELL_BAND_WIDTH). r_minor influences spatial extent but for a
    # localized blob, R-sweep at fixed band catches it.
    best_frac = 0.0
    best_R = R_ANCHOR
    best_r = R_MINOR
    fit_grid = []
    for R_test in R_SEARCH_VALUES:
        for r_test in R_MINOR_SEARCH_VALUES:
            frac, _ = shell_localized_fraction(
                omega_energy, R_test, r_test, center,
                band=max(SHELL_BAND_WIDTH, 0.5 * r_test),
            )
            fit_grid.append({"R": float(R_test), "r": float(r_test), "frac": float(frac)})
            if frac > best_frac:
                best_frac = frac
                best_R = R_test
                best_r = r_test

    return float(best_R), float(best_r), float(best_frac), center, fit_grid


def select_shell_sampling_points(omega_energy, R_opt, r_opt, center, n_points=8):
    """Pick the top-N cells with highest |ω|² that are also on the relaxed shell."""
    nx = omega_energy.shape[0]
    i, j, k = np.indices((nx, nx, nx))
    rho_xy = np.sqrt((i - center[0]) ** 2 + (j - center[1]) ** 2)
    rho_tube = np.sqrt((rho_xy - R_opt) ** 2 + (k - center[2]) ** 2)
    band = max(SHELL_BAND_WIDTH, 0.5 * r_opt)
    in_shell = rho_tube < band

    # Mask non-shell cells with -inf so argpartition picks shell cells only
    masked_energy = np.where(in_shell, omega_energy, -np.inf)
    flat = masked_energy.flatten()
    if not np.any(np.isfinite(flat)):
        return []
    n_avail = int(np.isfinite(flat).sum())
    n_pick = min(n_points, n_avail)
    top_idx = np.argpartition(flat, -n_pick)[-n_pick:]
    cells = [tuple(np.unravel_index(idx, omega_energy.shape)) for idx in top_idx]
    return cells


def measure_global_stats(engine):
    omega = np.asarray(engine.cos.omega)
    v_inc = np.asarray(engine.k4.V_inc)
    peak_omega = float(np.linalg.norm(omega, axis=-1).max())
    peak_vinc_norm = float(np.linalg.norm(v_inc, axis=-1).max())
    v_total_peak = float(np.sqrt(np.sum(v_inc ** 2, axis=-1)).max())
    c = int(engine.cos.extract_crossing_count())
    return peak_omega, peak_vinc_norm, v_total_peak, c


def main():
    print("=" * 78, flush=True)
    print(f"  Move 6 — Natural-attractor characterization (post-Move-5)")
    print(f"  P_phase6_natural_attractor_characterization")
    print("=" * 78, flush=True)
    print(f"  Lattice: N={N_LATTICE}, pml={PML}")
    print(f"  Reproducing Move 5 dynamics (corpus seed); recording from "
          f"t={T_RECORD_START_PERIOD}P → {N_PERIODS_TOTAL}P")
    print(f"  Snapshots at t = {SNAPSHOT_PERIODS} Compton periods")
    print(f"  Shell-fit search: R ∈ [2, 14], r ∈ [0.5, 6]")
    print(f"  Adjudication: Mode I if R_relaxed/r_relaxed = "
          f"{R_OVER_R_TARGET:.4f} ± {R_OVER_R_TOL}")
    print()

    engine = build_engine()
    seed_corpus_2_3_joint(engine)

    # ─── Run + record ─────────────────────────────────────────────────────────
    snapshots = {}    # step → {"omega": np.array, "v_inc": np.array}
    stats_stream = []  # per-step (peak_omega, peak_vinc, c)

    print(f"  Running {N_STEPS} steps...")
    t0 = time.time()
    last_progress = t0
    for step in range(1, N_STEPS + 1):
        engine.step()
        if step >= STEP_RECORD_START:
            peak_om, peak_vi, v_tot, c = measure_global_stats(engine)
            stats_stream.append({
                "step": int(step),
                "t_period": float(step * DT / COMPTON_PERIOD),
                "peak_omega": peak_om,
                "peak_vinc": peak_vi,
                "v_total_peak": v_tot,
                "c": c,
            })
        if step in SNAPSHOT_STEPS:
            snapshots[step] = {
                "omega": np.asarray(engine.cos.omega).copy(),
                "v_inc": np.asarray(engine.k4.V_inc).copy(),
            }
            print(f"    snapshot at step {step} (t={step*DT/COMPTON_PERIOD:.1f}P)",
                  flush=True)
        if (time.time() - last_progress) > 30.0:
            print(f"    [progress] step {step}, "
                  f"elapsed {time.time() - t0:.1f}s",
                  flush=True)
            last_progress = time.time()
    elapsed = time.time() - t0
    print(f"  Run complete: {elapsed:.1f}s")
    print()

    # ─── Post-hoc analysis ────────────────────────────────────────────────────

    # (a) GEOMETRY — fit (R_relaxed, r_relaxed) on t=200P snapshot
    final_step = max(SNAPSHOT_STEPS)
    omega_final = snapshots[final_step]["omega"]
    v_inc_final = snapshots[final_step]["v_inc"]
    omega_energy_final = np.sum(omega_final ** 2, axis=-1)

    R_opt, r_opt, shell_frac_opt, center, fit_grid = fit_natural_shell(omega_final)
    R_over_r_geometry = R_opt / max(r_opt, 1e-30)
    print(f"  (a) GEOMETRY — t={final_step*DT/COMPTON_PERIOD:.1f}P shell fit:")
    print(f"      R_opt = {R_opt:.4f}, r_opt = {r_opt:.4f}")
    print(f"      R_opt / r_opt = {R_over_r_geometry:.4f}  "
          f"(corpus φ² = {R_OVER_R_TARGET:.4f})")
    print(f"      shell_frac_opt = {shell_frac_opt:.4f}  "
          f"(threshold for well-defined shell = {SHELL_FRAC_OPT_THRESH})")
    print()

    # (b) PHASOR — sample V_inc at top cells on the relaxed shell across
    #     all 3 snapshots, compute spatial R_phase/r_phase per doc 26_ §3
    sample_cells = select_shell_sampling_points(
        omega_energy_final, R_opt, r_opt, center, n_points=8,
    )

    rho_per_cell = []
    cell_labels = []
    for cell_idx in sample_cells:
        rhos_across_snapshots = []
        for step_key in sorted(snapshots.keys()):
            v_inc = snapshots[step_key]["v_inc"]
            v_inc_at_cell = v_inc[cell_idx[0], cell_idx[1], cell_idx[2], :]  # 4 ports
            # Use total V_inc magnitude across 4 ports as the per-cell amplitude
            rhos_across_snapshots.append(float(np.linalg.norm(v_inc_at_cell)))
        rho_per_cell.append(float(np.mean(rhos_across_snapshots)))
        cell_labels.append(list(cell_idx))

    if len(rho_per_cell) > 0:
        R_spatial = float(np.mean(rho_per_cell))
        r_spatial = float(np.std(rho_per_cell))
        R_over_r_phasor = R_spatial / max(r_spatial, 1e-30)
        rel_std = r_spatial / max(R_spatial, 1e-30)
    else:
        R_spatial = r_spatial = R_over_r_phasor = rel_std = float("nan")

    print(f"  (b) PHASOR — V_inc spatial envelope on relaxed shell:")
    print(f"      Sampled cells (top {len(sample_cells)} on relaxed shell): {cell_labels}")
    print(f"      Per-cell ρ_i: {[f'{r:.4f}' for r in rho_per_cell]}")
    print(f"      R_spatial = {R_spatial:.4f}, r_spatial = {r_spatial:.4f}")
    print(f"      R/r phasor = {R_over_r_phasor:.4f}  "
          f"(corpus φ² = {R_OVER_R_TARGET:.4f}, rel_std = {rel_std:.4f})")
    print()

    # (c) SPECTRUM — FFT of peak |ω|(t) over recording window
    if len(stats_stream) >= 4:
        peak_omega_series = np.array([s["peak_omega"] for s in stats_stream])
        peak_vinc_series = np.array([s["peak_vinc"] for s in stats_stream])

        # Detrend
        peak_omega_detrended = peak_omega_series - peak_omega_series.mean()
        peak_vinc_detrended = peak_vinc_series - peak_vinc_series.mean()

        # FFT
        fft_omega = np.abs(np.fft.rfft(peak_omega_detrended)) ** 2
        fft_vinc = np.abs(np.fft.rfft(peak_vinc_detrended)) ** 2
        # Frequency resolution: dt = DT, signal length N = len(stream)
        freqs = np.fft.rfftfreq(len(peak_omega_detrended), d=DT)

        # Top peaks
        def top_peaks(fft_power, freqs, n=3):
            idx = np.argsort(fft_power)[::-1]
            top = []
            for i in idx:
                if freqs[i] > 0 and len(top) < n:
                    top.append((float(freqs[i]), float(fft_power[i])))
            return top

        omega_peaks = top_peaks(fft_omega, freqs, n=3)
        vinc_peaks = top_peaks(fft_vinc, freqs, n=3)
        # Convert ω from cycles/timestep to natural-units angular frequency
        omega_peaks_natural = [(2 * np.pi * f, p) for f, p in omega_peaks]
        vinc_peaks_natural = [(2 * np.pi * f, p) for f, p in vinc_peaks]

        print(f"  (c) SPECTRUM — FFT over t={T_RECORD_START_PERIOD}P→{N_PERIODS_TOTAL}P:")
        print(f"      peak |ω|(t): top freqs (natural-units ω) = "
              f"{[f'{w:.4f}' for w, _ in omega_peaks_natural]}")
        print(f"      peak |V_inc|(t): top freqs (natural-units ω) = "
              f"{[f'{w:.4f}' for w, _ in vinc_peaks_natural]}")
        print()
    else:
        omega_peaks_natural = vinc_peaks_natural = []

    # ─── Adjudication ─────────────────────────────────────────────────────────
    print("=" * 78, flush=True)
    print("  Adjudication")
    print("=" * 78, flush=True)

    geom_ratio_ok = abs(R_over_r_geometry - R_OVER_R_TARGET) <= R_OVER_R_TOL
    well_defined_shell = shell_frac_opt >= SHELL_FRAC_OPT_THRESH

    if not well_defined_shell:
        mode = "III-natural"
        verdict = (
            f"MODE III-natural — Natural attractor is DELOCALIZED. Best shell "
            f"fit at (R={R_opt:.2f}, r={r_opt:.2f}) achieves only "
            f"shell_frac={shell_frac_opt:.4f} (< threshold "
            f"{SHELL_FRAC_OPT_THRESH}). The (2,3) topology (c=3) is preserved "
            f"but the energy density doesn't localize on any clean torus shell. "
            f"Different methodology needed to characterize the natural attractor."
        )
    elif geom_ratio_ok:
        mode = "I-natural"
        verdict = (
            f"MODE I-natural — CORPUS ASPECT-RATIO VINDICATED at non-corpus "
            f"absolute scale. Natural attractor at (R={R_opt:.2f}, r={r_opt:.2f}) "
            f"with shell_frac={shell_frac_opt:.4f} ≥ {SHELL_FRAC_OPT_THRESH}; "
            f"R/r = {R_over_r_geometry:.4f} matches corpus φ² = "
            f"{R_OVER_R_TARGET:.4f} within ±{R_OVER_R_TOL}. Corpus's R/r = φ² "
            f"claim empirically validated. The corpus seed parameters at "
            f"(R=10, r=R/φ²=3.82) had the WRONG ABSOLUTE SCALE; the engine's "
            f"natural electron lives at (R={R_opt:.2f}, r={r_opt:.2f}) — same "
            f"aspect ratio. Round 7+8 narrative substantially inverts: corpus "
            f"qualitatively right, only R_anchor calibration was wrong."
        )
    else:
        mode = "II-natural"
        verdict = (
            f"MODE II-natural — Well-defined natural attractor at "
            f"(R={R_opt:.2f}, r={r_opt:.2f}) with shell_frac={shell_frac_opt:.4f}; "
            f"BUT R/r = {R_over_r_geometry:.4f} ≠ corpus φ² = "
            f"{R_OVER_R_TARGET:.4f} (off by "
            f"{abs(R_over_r_geometry - R_OVER_R_TARGET):.4f}, tol "
            f"{R_OVER_R_TOL}). Engine's natural electron exists with (2,3) "
            f"topology but at a DIFFERENT aspect ratio than corpus claims. "
            f"Corpus φ² ratio empirically falsified at the natural attractor."
        )
    print(f"  {verdict}")
    print()

    payload = {
        "pre_registration": "P_phase6_natural_attractor_characterization",
        "test": "Move 6 — natural-attractor characterization post-Move-5",
        "N": N_LATTICE,
        "phi_sq": PHI_SQ,
        "n_periods_total": N_PERIODS_TOTAL,
        "n_steps": N_STEPS,
        "elapsed_seconds": elapsed,
        "snapshot_periods": SNAPSHOT_PERIODS,
        "geometry": {
            "R_opt": R_opt,
            "r_opt": r_opt,
            "R_over_r": R_over_r_geometry,
            "shell_frac_opt": shell_frac_opt,
            "center": list(center),
        },
        "phasor_shell_envelope": {
            "n_sample_cells": len(sample_cells),
            "cell_labels": cell_labels,
            "rho_per_cell": rho_per_cell,
            "R_spatial": R_spatial,
            "r_spatial": r_spatial,
            "R_over_r": R_over_r_phasor,
            "rel_std": rel_std,
        },
        "spectrum": {
            "omega_top_freqs_natural": [list(p) for p in omega_peaks_natural],
            "vinc_top_freqs_natural": [list(p) for p in vinc_peaks_natural],
        },
        "stats_stream_first_last": [stats_stream[0], stats_stream[-1]] if stats_stream else [],
        "stats_stream_n_samples": len(stats_stream),
        "R_over_r_target": R_OVER_R_TARGET,
        "R_over_r_tol": R_OVER_R_TOL,
        "shell_frac_opt_thresh": SHELL_FRAC_OPT_THRESH,
        "fit_grid_top_5": sorted(fit_grid, key=lambda d: -d["frac"])[:5],
        "mode": mode,
        "verdict": verdict,
    }
    OUTPUT_JSON.write_text(json.dumps(payload, indent=2, default=str))
    print(f"  Result: {OUTPUT_JSON}")
    return payload


if __name__ == "__main__":
    main()
