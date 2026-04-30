"""
T-ST v2: Photon Self-Trap Test at Saturation-Engaged Regime.

Re-run of T-ST with tactical fixes per Grant's Rule 14 substrate walk:
  - Lattice N=48 → N=96 (active region 80 cells = 12.7·λ_C; photon has room
    to propagate before PML absorbs leading edge)
  - PML 4 → 8 (deeper PML for cleaner outer boundary)
  - Source amplitude 0.10 → 0.50 V_SNAP (5.9× V_yield, ensures peak lattice
    A² > √(2α) = 0.121 somewhere during propagation)
  - Source focus sigma_yz 4.0 → 2.0 (tighter beam, higher peak per cell)
  - Source position x0 8 → 16 (deeper PML buffer)

Same hypothesis (Grant's rifling-bullet single-frequency reframe per Rule
14 substrate walk) and same dual-criterion as T-ST v1 — only test geometry
changes. v1 didn't engage saturation (peak A²=0.0097, 12× below threshold);
v2 should engage cleanly.

== Pre-registered hypothesis (frozen 2026-04-30, same as T-ST v1) ==

H_self_trap (Grant's reframe of doc 30 §4 — single-frequency rifling
bullet, AVE-native per Rule 14 substrate walk):
    Photon at ω_C with intrinsic CP spin = ω_C · ε_hand (single
    frequency, just rotating with chirality). Propagates as cavitation
    bubble through K4 substrate; lattice dispersion at ω_C gives
    v_g ≈ 0.5·c_TLM (structural lattice property, doesn't affect LC
    resonance condition). At bond where local |V| crosses V_yield, Op14
    saturation engages, chirality match breaks, bubble loses coherence,
    photon traps. The (2,3) topology emerges from the trap cavity's
    torus geometry — purely spatial winding (poloidal 2 × toroidal 3),
    NOT a frequency ratio.

== PASS criterion (BOTH must pass) — same as v1 ==

1. FREQUENCY: post-trap steady-state at trapped bond at ω_C ± α
   (1.0 ± 0.0073 in natural units)
2. TOPOLOGY (corpus-canonical, A42): c=3 via cosserat.extract_crossing_count()

== Load-bearing secondary (subset, focused on saturation-engaged regime) ==

(A) Saturation engagement: peak A² in active region exceeds √(2α) ≈ 0.121
(B) Velocity profile: v_g(t) — should slow further as A²(centroid) grows
(C) TIR signature: Γ at saturation cells → -1 ± 0.1
(D) Wake signature: dV/dt opposite-sign behind leading edge ≥1 wavelength
    (now actually testable since saturation engages)
(E) Self-sustenance: post-shutoff, A² > A²_yield/2 sustained ≥5 P

== Configuration ==

- N=96, PML=8 (active region 80 cells = 12.7 Compton wavelengths)
- Cosserat ON, A28-corrected (disable_cosserat_lc_force=True,
  enable_cosserat_self_terms=True)
- Source: SpatialDipoleCPSource
    x0 = 16 (8 PML + 8 buffer)
    propagation_axis = 0 (+x)
    handedness = "RH"
    amplitude = 0.50 V_SNAP (~5.86 · V_yield)
    omega = 1.0 (ω_C)
    sigma_yz = 2.0 (tight focus, peak ~0.61·σ from center)
    envelope: t_ramp=2P, t_sustain=2P, t_decay=2P
- Run: 50 Compton periods (444 timesteps)

== Sampling design ==

Per-step axial samples at 5 transverse lines to catch off-center CP peaks:
  - (x, yc, zc)         — central axis
  - (x, yc+2, zc)       — y-peak of σ=2 dipole
  - (x, yc-2, zc)       — y-peak (other side)
  - (x, yc, zc+2)       — z-peak
  - (x, yc, zc-2)       — z-peak (other side)

Per-capture (every 10 steps) summaries:
  - centroid_x(t), front_x(t), max_a2(t) and its location

== A47 feasibility ==

- N=96³ × 4 ports × 8 bytes = 28 MB per V_inc snapshot (8× T-ST v1)
- Engine evolution: ~24 min wall clock (8× T-ST v1's 185s)
- 5 axial lines × 96 cells × 4 ports × 444 steps × 8B = 13 MB time-series
- Total compute estimate: ~25-40 min
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path
from collections import Counter

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))

from ave.topological.vacuum_engine import (
    VacuumEngine3D,
    SpatialDipoleCPSource,
)


ALPHA = 1.0 / 137.035999
V_YIELD = float(np.sqrt(ALPHA))
A2_YIELD = ALPHA
A2_OP14 = float(np.sqrt(2.0 * ALPHA))
OMEGA_C = 1.0
COMPTON_PERIOD = 2.0 * np.pi
DT = 1.0 / np.sqrt(2.0)


def setup_engine(N=96, PML=8):
    return VacuumEngine3D.from_args(
        N=N, pml=PML, temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,
        enable_cosserat_self_terms=True,
        use_asymmetric_saturation=True,
        axiom_4_enabled=True,
    )


def setup_source():
    return SpatialDipoleCPSource(
        x0=16,
        propagation_axis=0,
        amplitude=0.50,
        omega=OMEGA_C,
        handedness="RH",
        sigma_yz=2.0,
        t_ramp=2.0 * COMPTON_PERIOD,
        t_sustain=2.0 * COMPTON_PERIOD,
        t_decay=2.0 * COMPTON_PERIOD,
    )


def compute_a2_field(V_inc, V_SNAP=1.0):
    return np.sum(V_inc ** 2, axis=-1) / (V_SNAP ** 2)


def mask_interior(field, mask_active, pml):
    N = field.shape[0]
    out = field * mask_active.astype(float)
    out[:pml, :, :] = 0.0
    out[N - pml:, :, :] = 0.0
    out[:, :pml, :] = 0.0
    out[:, N - pml:, :] = 0.0
    out[:, :, :pml] = 0.0
    out[:, :, N - pml:] = 0.0
    return out


def compute_centroid(V_inc, mask_active, pml):
    energy = mask_interior(np.sum(V_inc ** 2, axis=-1), mask_active, pml)
    total = float(np.sum(energy))
    if total < 1e-30:
        return float("nan"), 0.0
    N = V_inc.shape[0]
    coords = np.arange(N, dtype=float)
    marg = np.sum(energy, axis=(1, 2))
    return float(np.sum(coords * marg) / total), total


def compute_front(V_inc, mask_active, pml, frac=0.5):
    energy = mask_interior(np.sum(V_inc ** 2, axis=-1), mask_active, pml)
    marg = np.sum(energy, axis=(1, 2))
    if marg.max() < 1e-30:
        return float("nan")
    above = np.where(marg > frac * marg.max())[0]
    if len(above) == 0:
        return float("nan")
    return float(above[-1])


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
    print("  T-ST v2: Photon Self-Trap at Saturation-Engaged Regime")
    print("  N=96, PML=8, A=0.50 V_SNAP (~5.9·V_yield), sigma_yz=2.0")
    print("=" * 78, flush=True)

    N = 96
    PML = 8
    n_periods = 50
    n_steps = int(n_periods * COMPTON_PERIOD / DT)
    capture_cadence = 10

    print(f"\n  Lattice: N={N}, PML={PML} (active region {N - 2*PML} cells)")
    print(f"  Run: {n_periods} P = {n_steps} timesteps at dt={DT:.4f}")
    print(f"  V_yield={V_YIELD:.4f}, A²_op14={A2_OP14:.4f}")
    print(f"  Source amp = 0.50·V_SNAP = {0.50/V_YIELD:.2f}·V_yield")

    t_start = time.time()
    engine = setup_engine(N=N, PML=PML)
    source = setup_source()
    engine.add_source(source)

    yc, zc = N // 2, N // 2
    sample_lines = [
        ("center",    yc,     zc),
        ("y_plus",    yc + 2, zc),
        ("y_minus",   yc - 2, zc),
        ("z_plus",    yc,     zc + 2),
        ("z_minus",   yc,     zc - 2),
    ]
    # axial_v_inc[line_idx, step, x, port]
    axial_v_inc = np.zeros((len(sample_lines), n_steps, N, 4))
    axial_v_ref = np.zeros((len(sample_lines), n_steps, N, 4))
    axial_omega = np.zeros((len(sample_lines), n_steps, N, 3))

    captures = []
    centroid_traj = []
    front_traj = []
    max_a2_traj = []
    max_a2_loc = []

    print(f"\n  Running...", flush=True)

    for step_i in range(n_steps):
        engine.step()

        # Per-step axial samples on 5 transverse lines
        for li, (_, ly, lz) in enumerate(sample_lines):
            axial_v_inc[li, step_i] = engine.k4.V_inc[:, ly, lz, :]
            axial_v_ref[li, step_i] = engine.k4.V_ref[:, ly, lz, :]
            axial_omega[li, step_i] = engine.cos.omega[:, ly, lz, :]

        if step_i % capture_cadence == 0:
            t_now = step_i * DT
            V_inc = engine.k4.V_inc
            mask = engine.k4.mask_active
            cx, total_e = compute_centroid(V_inc, mask, pml=PML)
            front_x = compute_front(V_inc, mask, pml=PML)
            a2 = compute_a2_field(V_inc, V_SNAP=engine.V_SNAP)
            a2_int = mask_interior(a2, mask, PML)
            max_a2 = float(a2_int.max())
            max_a2_idx = np.unravel_index(int(np.argmax(a2_int)), a2_int.shape)
            cx_int = int(np.clip(cx, 0, N - 1)) if not np.isnan(cx) else 0
            a2_at_centroid = float(a2_int[cx_int, yc, zc])

            centroid_traj.append((t_now, cx))
            front_traj.append((t_now, front_x))
            max_a2_traj.append((t_now, max_a2))
            max_a2_loc.append(max_a2_idx)

            captures.append({
                "t": float(t_now),
                "step": int(step_i),
                "centroid_x": cx,
                "front_x": front_x,
                "total_energy": total_e,
                "a2_at_centroid": a2_at_centroid,
                "max_a2_interior": max_a2,
                "max_a2_loc": [int(v) for v in max_a2_idx],
            })

            if step_i % (capture_cadence * 5) == 0:
                t_p = t_now / COMPTON_PERIOD
                elapsed = time.time() - t_start
                print(f"    t={t_p:5.2f}P  cx={cx if not np.isnan(cx) else 0:6.2f}  "
                      f"front_x={front_x if not np.isnan(front_x) else 0:6.2f}  "
                      f"max_A²={max_a2:.4f} @ {tuple(max_a2_idx)}  "
                      f"({elapsed:.0f}s)")

    total_elapsed = time.time() - t_start
    print(f"\n  Engine evolution complete in {total_elapsed:.0f}s")

    # ============================================================
    # Adjudication
    # ============================================================
    print("\n" + "=" * 78)
    print("  ADJUDICATION")
    print("=" * 78)

    # Identify trap location: most-frequent peak A² location post-shutoff
    second_half = [c for c in captures if c["t"] > 6.0 * COMPTON_PERIOD]
    if not second_half:
        print("\n  No post-shutoff captures.")
        return

    cell_counter = Counter(tuple(loc) for loc in
                           [c["max_a2_loc"] for c in second_half])
    trap_cell, trap_count = cell_counter.most_common(1)[0]
    trap_x, trap_y, trap_z = trap_cell

    print(f"\n  Trap candidate cell: ({trap_x}, {trap_y}, {trap_z}) "
          f"({trap_count}/{len(second_half)} post-shutoff captures)")

    # Saturation
    a2_at_trap_2nd_half = [c["max_a2_interior"] for c in second_half
                           if tuple(c["max_a2_loc"]) == trap_cell]
    a2_trap_max = float(max(a2_at_trap_2nd_half)) if a2_at_trap_2nd_half else 0.0
    a2_trap_mean = float(np.mean(a2_at_trap_2nd_half)) if a2_at_trap_2nd_half else 0.0
    saturation_engaged = a2_trap_max > A2_OP14
    print(f"  A² at trap (post-shutoff): max={a2_trap_max:.4f}, mean={a2_trap_mean:.4f}")
    print(f"  Saturation engagement (A² > {A2_OP14:.4f}): "
          f"{'YES' if saturation_engaged else 'NO'}")

    # Find which sample line is closest to trap
    line_dists = [
        ((trap_y - ly) ** 2 + (trap_z - lz) ** 2, li, name)
        for li, (name, ly, lz) in enumerate(sample_lines)
    ]
    line_dists.sort()
    closest_dist, closest_li, closest_name = line_dists[0]
    print(f"  Closest sample line to trap: '{closest_name}' "
          f"(d²={closest_dist})")

    # FFT at trap on closest sample line, port 0
    post_shutoff_start = int(25.0 * COMPTON_PERIOD / DT)
    if post_shutoff_start < n_steps and closest_dist <= 8:
        v_at_trap = axial_v_inc[closest_li, post_shutoff_start:, trap_x, 0]
        v_ref_at_trap = axial_v_ref[closest_li, post_shutoff_start:, trap_x, 0]
        fft_targets = [
            OMEGA_C * (1.0 - 2 * ALPHA), OMEGA_C, OMEGA_C * (1.0 + 2 * ALPHA),
            1.5, 2.96, 0.5
        ]
        fft_at_trap = fft_at(v_at_trap, DT, fft_targets)
        if any(fft_at_trap.values()):
            peak_freq = max(fft_at_trap, key=fft_at_trap.get)
            peak_amp = fft_at_trap[peak_freq]
            freq_match = abs(peak_freq - OMEGA_C) <= ALPHA
        else:
            peak_freq = float("nan")
            peak_amp = 0.0
            freq_match = False
    else:
        v_at_trap = None
        v_ref_at_trap = None
        fft_at_trap = {}
        peak_freq = float("nan")
        peak_amp = 0.0
        freq_match = False

    print(f"\n  FREQUENCY criterion (target ω_C ± α = 1.0 ± {ALPHA:.4f}):")
    if v_at_trap is not None:
        for f, a in fft_at_trap.items():
            flag = " ★" if a == peak_amp else ""
            print(f"    f = {f:.4f}: amp = {a:.3e}{flag}")
        print(f"    Peak at f = {peak_freq:.4f}, |ω - ω_C| = "
              f"{abs(peak_freq - OMEGA_C):.4f} (criterion {ALPHA:.4f})")
        print(f"    Frequency match: {'PASS' if freq_match else 'FAIL'}")
    else:
        print(f"    Trap not on sampled lines (closest d²={closest_dist}); FFT skipped.")

    # Op10 c
    try:
        c_op10 = int(engine.cos.extract_crossing_count())
    except Exception as exc:
        print(f"  Op10 failed: {exc}")
        c_op10 = -1
    topology_match = (c_op10 == 3)
    print(f"\n  TOPOLOGY criterion (c=3 via Op10):")
    print(f"    extract_crossing_count = {c_op10}")
    print(f"    Topology match (c=3): {'PASS' if topology_match else 'FAIL'}")

    # Velocity profile
    print(f"\n  VELOCITY PROFILE:")
    centroid_arr = np.array([(t, x) for t, x in centroid_traj if not np.isnan(x)])
    if len(centroid_arr) > 5:
        ts = centroid_arr[:, 0]
        xs = centroid_arr[:, 1]
        free_mask = ts < 4.0 * COMPTON_PERIOD
        late_mask = ts > 15.0 * COMPTON_PERIOD
        if free_mask.sum() > 3:
            v_free = float(np.polyfit(ts[free_mask], xs[free_mask], 1)[0])
            print(f"    Free-prop v_g (t<4P): {v_free:.3f} cells/time-unit "
                  f"(predicted ≈ 0.7 from dispersion check at low amp)")
        if late_mask.sum() > 3:
            v_late = float(np.polyfit(ts[late_mask], xs[late_mask], 1)[0])
            print(f"    Late v_g (t>15P): {v_late:.3f} (predicted ≈ 0 if trapped)")

    # Self-sustenance
    print(f"\n  SELF-SUSTENANCE:")
    if len(captures) > 10:
        late_caps = [c for c in captures if c["t"] > 7.0 * COMPTON_PERIOD]
        if late_caps:
            e_first = late_caps[0]["total_energy"]
            e_last = late_caps[-1]["total_energy"]
            retention = e_last / e_first if e_first > 0 else 0.0
            print(f"    Energy at t=7P: {e_first:.3e}")
            print(f"    Energy at t=50P: {e_last:.3e}")
            print(f"    Retention: {retention:.3f}")

    # Wake signature (now testable since saturation should engage)
    print(f"\n  WAKE SIGNATURE:")
    mid_step = n_steps // 4
    if mid_step + 5 < n_steps:
        v_now = axial_v_inc[0, mid_step, :, 0]   # center line, port 0
        v_next = axial_v_inc[0, mid_step + 5, :, 0]
        dv_dt = (v_next - v_now) / (5 * DT)
        v_sq = v_now ** 2
        if v_sq.max() > 1e-20:
            front_idx = int(np.where(v_sq > 0.1 * v_sq.max())[0][-1])
            wavelength_cells = int(round(2 * np.pi))
            trail_idx = max(front_idx - wavelength_cells, PML)
            sign_front = float(np.sign(dv_dt[front_idx]))
            sign_trail = float(np.sign(dv_dt[trail_idx]))
            opposite_signs = (sign_front * sign_trail < 0)
            print(f"    front_x={front_idx} dV/dt={sign_front:+.0f}")
            print(f"    trail_x={trail_idx} dV/dt={sign_trail:+.0f}")
            print(f"    Opposite-sign wake: {'YES' if opposite_signs else 'NO'}")
        else:
            opposite_signs = False
    else:
        opposite_signs = False

    # Verdict
    print(f"\n{'=' * 78}")
    print(f"  VERDICT")
    print(f"{'=' * 78}")
    h_pass = freq_match and topology_match
    print(f"  Frequency at ω_C ± α: {'PASS' if freq_match else 'FAIL'}")
    print(f"  Topology c=3 via Op10: {'PASS' if topology_match else 'FAIL'}")
    print(f"  H_self_trap: {'PASS' if h_pass else 'FAIL'}")
    if h_pass:
        print(f"  → Self-trap CONFIRMED.")
        if opposite_signs:
            print(f"  → Wake signature PRESENT: BEMF reframe IS engine mechanism.")
        else:
            print(f"  → Wake signature ABSENT: corpus-physics-correct, "
                  f"engine substitutes Op14.")
    else:
        if saturation_engaged:
            print(f"  → Saturation engaged but trap criteria unmet — "
                  f"characterize-as-itself per Rule 10.")
        else:
            print(f"  → Saturation still didn't engage. Source needs more amplitude/focus.")

    # Save
    out = {
        "test": "T-ST v2: Photon Self-Trap at Saturation-Engaged Regime",
        "config": {
            "N": N, "PML": PML, "n_periods": n_periods,
            "amplitude_VSNAP": 0.50, "omega": OMEGA_C, "handedness": "RH",
            "x0": 16, "sigma_yz": 2.0,
        },
        "criteria": {
            "frequency_match": bool(freq_match),
            "peak_freq": float(peak_freq) if not np.isnan(peak_freq) else None,
            "peak_amp": float(peak_amp),
            "topology_match": bool(topology_match),
            "c_op10": int(c_op10),
            "h_self_trap_PASS": bool(h_pass),
        },
        "secondary": {
            "trap_cell": [int(trap_x), int(trap_y), int(trap_z)],
            "saturation_engaged": bool(saturation_engaged),
            "a2_trap_max": float(a2_trap_max),
            "a2_trap_mean": float(a2_trap_mean),
            "a2_op14_threshold": float(A2_OP14),
            "wake_opposite_signs": bool(opposite_signs),
        },
        "captures": captures,
        "centroid_trajectory": [[float(t), float(x) if not np.isnan(x) else None]
                                for t, x in centroid_traj],
        "front_trajectory": [[float(t), float(x) if not np.isnan(x) else None]
                             for t, x in front_traj],
        "max_a2_trajectory": [[float(t), float(a)] for t, a in max_a2_traj],
        "elapsed_total_s": total_elapsed,
    }
    out_path = Path(__file__).parent / "r10_v8_t_st_v2_n96_results.json"
    out_path.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nSaved {out_path.relative_to(Path.cwd())}")

    npz_path = Path(__file__).parent / "r10_v8_t_st_v2_n96_capture.npz"
    np.savez_compressed(
        npz_path,
        axial_v_inc=axial_v_inc,
        axial_v_ref=axial_v_ref,
        axial_omega=axial_omega,
        sample_lines_yz=np.array([(ly, lz) for _, ly, lz in sample_lines]),
        sample_line_names=np.array([name for name, _, _ in sample_lines]),
        dt=DT, N=N, PML=PML, n_steps=n_steps,
    )
    print(f"Saved {npz_path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
