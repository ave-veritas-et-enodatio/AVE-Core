"""
Φ_link Sector Measurement — long-standing gap closure.

Per [doc 75 line 140](research/L3_electron_soliton/75_cosserat_energy_conservation_violation.md):
"the corpus electron, if it exists, lives somewhere we haven't probed
(Φ_link sector / hybrid V≠0 ∧ ω≠0 / different topology)"

Per A43 catalog: V_inc and Φ_link are L-C conjugate on each bond LC tank
(doc 66 §17.2). Across 30+ tests in Round 7+8 + foundation audit + T-ST
v1+v2, V_inc has been measured extensively but **Φ_link has never been
captured directly.** Engine accumulates Phi_link += V_avg·dt every step
(k4_tlm.py:384-391) but no test has read it back.

== Test design ==

Re-runs T-ST v1 exactly (N=48, A=0.10, ω=ω_C, RH-CP, Cosserat ON,
A28-corrected) with one added capture line: axial Phi_link saved per
timestep alongside the existing V_inc, V_ref, Cosserat ω axial lines.

Direct comparison to T-ST v1 capture: same engine state, just the
inductive-side observable now visible.

== Pre-registered observable questions (frozen 2026-04-30) ==

(a) Is Phi_link non-zero anywhere along propagation? V_inc decayed to 1e-5
    after t=7P; if Phi_link is also dissipated, the trap doesn't live in
    Phi_link sector either. If Phi_link RETAINS energy after V_inc decays,
    that's the long-standing doc 75 hypothesis confirmed empirically.

(b) FFT of Phi_link at residual cell (post-shutoff). Same frequency as
    V_inc, or different? Doc 66 says Φ_link is V_inc phase-shifted 90°,
    so frequency should match; if different, structural finding.

(c) Phi_link spatial distribution at end of run. Where is the
    "remaining" energy stored — V_inc field, Cosserat ω field, Phi_link?

(d) Phi_link / V_inc ratio over time. If conjugate as corpus says,
    ratio should be ~ω_C·dt (dimensional from ½LI² = ½CV² at resonance).

== NOT pre-registered as PASS/FAIL ==

This is a characterize-as-itself diagnostic per Rule 10. No hypothesis
about "trap criterion" — we're filling a 30+-test gap by reading a
sector that's never been read.

== Compute estimate ==

Same as T-ST v1: ~3-5 min wall clock. One added array.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))

from ave.topological.vacuum_engine import (
    VacuumEngine3D,
    SpatialDipoleCPSource,
)


ALPHA = 1.0 / 137.035999
OMEGA_C = 1.0
COMPTON_PERIOD = 2.0 * np.pi
DT = 1.0 / np.sqrt(2.0)


def setup_engine(N=48, PML=4):
    return VacuumEngine3D.from_args(
        N=N, pml=PML, temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,
        enable_cosserat_self_terms=True,
        use_asymmetric_saturation=True,
        axiom_4_enabled=True,
    )


def setup_source():
    """Same source params as T-ST v1."""
    return SpatialDipoleCPSource(
        x0=8,
        propagation_axis=0,
        amplitude=0.10,
        omega=OMEGA_C,
        handedness="RH",
        sigma_yz=4.0,
        t_ramp=2.0 * COMPTON_PERIOD,
        t_sustain=2.0 * COMPTON_PERIOD,
        t_decay=2.0 * COMPTON_PERIOD,
    )


def fft_at(traj, dt, target_freqs):
    n = len(traj)
    if n < 16:
        return {f: 0.0 for f in target_freqs}
    fft_vals = np.fft.rfft(traj)
    freqs = np.fft.rfftfreq(n, d=dt) * 2.0 * np.pi
    fft_amp = 2.0 * np.abs(fft_vals) / n
    out = {}
    for f_target in target_freqs:
        idx = int(np.argmin(np.abs(freqs - f_target)))
        out[float(f_target)] = float(fft_amp[idx])
    return out


def main():
    print("=" * 78, flush=True)
    print("  Φ_link Sector Measurement — Doc 75 line 140 long-standing gap")
    print("  Re-run of T-ST v1 with axial Phi_link capture added")
    print("=" * 78, flush=True)

    N = 48
    PML = 4
    n_periods = 50
    n_steps = int(n_periods * COMPTON_PERIOD / DT)

    print(f"\n  Lattice: N={N}, PML={PML}")
    print(f"  Run: {n_periods} P = {n_steps} timesteps at dt={DT:.4f}")
    print(f"  Source: SpatialDipoleCPSource RH @ x0=8, ω=ω_C, A=0.10·V_SNAP, σ=4.0")

    t_start = time.time()
    engine = setup_engine(N=N, PML=PML)
    source = setup_source()
    engine.add_source(source)

    yc, zc = N // 2, N // 2

    # Axial captures — same as T-ST v1 plus Phi_link
    axial_v_inc = np.zeros((n_steps, N, 4))
    axial_v_ref = np.zeros((n_steps, N, 4))
    axial_omega = np.zeros((n_steps, N, 3))
    axial_phi_link = np.zeros((n_steps, N, 4))   # NEW

    # Energy budget over time
    energy_v_inc = np.zeros(n_steps)
    energy_phi_link = np.zeros(n_steps)
    energy_omega = np.zeros(n_steps)

    print(f"\n  Running...", flush=True)

    for step_i in range(n_steps):
        engine.step()

        axial_v_inc[step_i] = engine.k4.V_inc[:, yc, zc, :]
        axial_v_ref[step_i] = engine.k4.V_ref[:, yc, zc, :]
        axial_omega[step_i] = engine.cos.omega[:, yc, zc, :]
        axial_phi_link[step_i] = engine.k4.Phi_link[:, yc, zc, :]    # NEW

        # Total energy in each sector (interior only, PML excluded)
        mask = engine.k4.mask_active
        v_sq = np.sum(engine.k4.V_inc ** 2, axis=-1) * mask.astype(float)
        v_sq[:PML, :, :] = 0.0; v_sq[N - PML:, :, :] = 0.0
        v_sq[:, :PML, :] = 0.0; v_sq[:, N - PML:, :] = 0.0
        v_sq[:, :, :PML] = 0.0; v_sq[:, :, N - PML:] = 0.0
        energy_v_inc[step_i] = float(np.sum(v_sq))

        phi_sq = np.sum(engine.k4.Phi_link ** 2, axis=-1) * mask.astype(float)
        phi_sq[:PML, :, :] = 0.0; phi_sq[N - PML:, :, :] = 0.0
        phi_sq[:, :PML, :] = 0.0; phi_sq[:, N - PML:, :] = 0.0
        phi_sq[:, :, :PML] = 0.0; phi_sq[:, :, N - PML:] = 0.0
        energy_phi_link[step_i] = float(np.sum(phi_sq))

        omega_sq = np.sum(engine.cos.omega ** 2, axis=-1)
        omega_sq[:PML, :, :] = 0.0; omega_sq[N - PML:, :, :] = 0.0
        omega_sq[:, :PML, :] = 0.0; omega_sq[:, N - PML:, :] = 0.0
        omega_sq[:, :, :PML] = 0.0; omega_sq[:, :, N - PML:] = 0.0
        energy_omega[step_i] = float(np.sum(omega_sq))

        if step_i % 50 == 0:
            t_p = step_i * DT / COMPTON_PERIOD
            print(f"    t={t_p:5.2f}P  E_V_inc={energy_v_inc[step_i]:.3e}  "
                  f"E_Phi_link={energy_phi_link[step_i]:.3e}  "
                  f"E_omega={energy_omega[step_i]:.3e}  "
                  f"({time.time() - t_start:.0f}s)")

    elapsed = time.time() - t_start
    print(f"\n  Engine evolution complete in {elapsed:.0f}s")

    # ============================================================
    # Diagnostic readout
    # ============================================================
    print("\n" + "=" * 78)
    print("  Φ_link DIAGNOSTIC READOUT (characterize-as-itself per Rule 10)")
    print("=" * 78)

    # Energy retention by sector at end of run
    print(f"\n  (a) Energy budget by sector at key times:")
    print(f"  {'time':>10} {'E_V_inc':>15} {'E_Phi_link':>15} {'E_omega':>15}  {'Phi/V':>8}")
    for t_p_target in [0.5, 2.0, 4.0, 6.0, 7.0, 10.0, 25.0, 49.0]:
        step_idx = int(t_p_target * COMPTON_PERIOD / DT)
        if step_idx < n_steps:
            ev = energy_v_inc[step_idx]
            ep = energy_phi_link[step_idx]
            eo = energy_omega[step_idx]
            ratio = ep / max(ev, 1e-30)
            print(f"  {t_p_target:>9.1f}P {ev:>15.3e} {ep:>15.3e} {eo:>15.3e}  "
                  f"{ratio:>8.3f}")

    # Phi_link decay vs V_inc decay
    e_v_first = energy_v_inc[max(int(7.0 * COMPTON_PERIOD / DT), 0)]
    e_v_last = energy_v_inc[-1]
    e_p_first = energy_phi_link[max(int(7.0 * COMPTON_PERIOD / DT), 0)]
    e_p_last = energy_phi_link[-1]

    print(f"\n  (b) Decay characteristics post-source-shutoff (t=7P → t=49P):")
    if e_v_first > 0:
        print(f"      V_inc retention (E_49/E_7): {e_v_last/e_v_first:.3e}")
    if e_p_first > 0:
        print(f"      Phi_link retention:         {e_p_last/e_p_first:.3e}")
    else:
        print(f"      Phi_link energy at t=7P: {e_p_first:.3e}")

    # FFT analysis: is Phi_link at same frequency as V_inc?
    # Use cell with peak Phi_link energy in second half of run
    print(f"\n  (c) Phi_link spatial peak vs V_inc spatial peak (post-shutoff):")
    post_shutoff_start = int(25.0 * COMPTON_PERIOD / DT)
    if post_shutoff_start < n_steps:
        # |Phi_link|² summed over ports + averaged over post-shutoff window
        phi_sq_axial = np.mean(np.sum(axial_phi_link[post_shutoff_start:] ** 2,
                                       axis=-1), axis=0)
        v_sq_axial = np.mean(np.sum(axial_v_inc[post_shutoff_start:] ** 2,
                                     axis=-1), axis=0)

        peak_phi_x = int(np.argmax(phi_sq_axial))
        peak_v_x = int(np.argmax(v_sq_axial))
        print(f"      Phi_link spatial peak at x={peak_phi_x} "
              f"(amp²={phi_sq_axial[peak_phi_x]:.3e})")
        print(f"      V_inc spatial peak at x={peak_v_x} "
              f"(amp²={v_sq_axial[peak_v_x]:.3e})")

        # FFT at peak Phi_link cell
        if phi_sq_axial[peak_phi_x] > 1e-20:
            phi_traj = axial_phi_link[post_shutoff_start:, peak_phi_x, 0]
            v_traj = axial_v_inc[post_shutoff_start:, peak_phi_x, 0]
            target_freqs = [
                OMEGA_C * (1.0 - 2 * ALPHA), OMEGA_C, OMEGA_C * (1.0 + 2 * ALPHA),
                1.5, 2.96, 0.5, 0.577
            ]
            print(f"\n  (d) FFT at Phi_link peak cell x={peak_phi_x} "
                  f"(post-shutoff window):")
            phi_fft = fft_at(phi_traj, DT, target_freqs)
            v_fft = fft_at(v_traj, DT, target_freqs)
            print(f"      {'f':>10} {'V_inc amp':>15} {'Phi_link amp':>15}  "
                  f"{'Phi/V ratio':>12}")
            for f in target_freqs:
                v_amp = v_fft[f]
                p_amp = phi_fft[f]
                r = p_amp / max(v_amp, 1e-30)
                print(f"      {f:>10.4f} {v_amp:>15.3e} {p_amp:>15.3e}  "
                      f"{r:>12.3f}")

            phi_peak_freq = max(phi_fft, key=phi_fft.get) if any(phi_fft.values()) else None
            v_peak_freq = max(v_fft, key=v_fft.get) if any(v_fft.values()) else None
            print(f"\n      V_inc peak freq at this cell: {v_peak_freq}")
            print(f"      Phi_link peak freq at this cell: {phi_peak_freq}")
        else:
            phi_peak_freq = None
            v_peak_freq = None
    else:
        phi_peak_freq = None
        v_peak_freq = None
        peak_phi_x = -1
        peak_v_x = -1

    # Summary
    print(f"\n{'=' * 78}")
    print(f"  HEADLINE")
    print(f"{'=' * 78}")
    if e_p_first > e_v_first * 0.1:
        print(f"  → Phi_link sector carries SUBSTANTIAL energy at trap regime")
        print(f"    (Phi/V ratio at t=7P: {e_p_first/max(e_v_first, 1e-30):.3f})")
    elif e_p_first > 0:
        print(f"  → Phi_link sector active but minor "
              f"(Phi/V at t=7P: {e_p_first/max(e_v_first, 1e-30):.3f})")
    else:
        print(f"  → Phi_link sector negligible at this regime.")

    if e_p_last > e_v_last * 10:
        print(f"  → Phi_link RETAINS energy after V_inc decays — corpus electron")
        print(f"    candidate per doc 75 line 140 hypothesis CONFIRMED empirically.")
    elif e_p_last > 0 and e_v_last > 0:
        ratio_end = e_p_last / e_v_last
        print(f"  → Phi/V ratio at t=49P: {ratio_end:.3f}")
        if ratio_end > 1.0:
            print(f"    Phi_link decays slower than V_inc — partial corpus-electron")
            print(f"    candidate; doc 75 line 140 partially supported.")
        else:
            print(f"    Phi_link decays faster than or with V_inc — corpus electron")
            print(f"    NOT in Phi_link sector at this regime.")
    else:
        print(f"  → Both sectors decayed to noise floor; doc 75 hypothesis NOT")
        print(f"    supported at T-ST v1 regime.")

    # Save
    out = {
        "test": "Phi_link Sector Measurement (T-ST v1 regime)",
        "config": {"N": N, "PML": PML, "amplitude_VSNAP": 0.10, "omega": OMEGA_C},
        "energy_at_t7P": {
            "v_inc": float(e_v_first),
            "phi_link": float(e_p_first),
            "phi_v_ratio": float(e_p_first / max(e_v_first, 1e-30)),
        },
        "energy_at_t49P": {
            "v_inc": float(e_v_last),
            "phi_link": float(e_p_last),
            "phi_v_ratio": float(e_p_last / max(e_v_last, 1e-30)),
        },
        "phi_link_spatial_peak_x": int(peak_phi_x),
        "v_inc_spatial_peak_x": int(peak_v_x),
        "phi_link_peak_freq": phi_peak_freq,
        "v_inc_peak_freq": v_peak_freq,
        "elapsed_total_s": float(elapsed),
    }
    out_path = Path(__file__).parent / "r10_v8_phi_link_capture_results.json"
    out_path.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nSaved {out_path.relative_to(Path.cwd())}")

    npz_path = Path(__file__).parent / "r10_v8_phi_link_capture.npz"
    np.savez_compressed(
        npz_path,
        axial_v_inc=axial_v_inc,
        axial_v_ref=axial_v_ref,
        axial_omega=axial_omega,
        axial_phi_link=axial_phi_link,
        energy_v_inc=energy_v_inc,
        energy_phi_link=energy_phi_link,
        energy_omega=energy_omega,
        dt=DT, N=N, PML=PML, n_steps=n_steps,
    )
    print(f"Saved {npz_path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
