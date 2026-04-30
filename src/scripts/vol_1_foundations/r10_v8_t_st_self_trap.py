"""
T-ST: Photon Self-Trap Test — Grant's rifling-bullet + cavitation-bubble reframe.

Tests whether a chirally-spinning T₂ propagating photon at ω_C with peak
amplitude > V_yield, injected into bare K4 substrate, self-traps as a
(2,3) phase-space soliton at the bond where Op14 saturation engages.

== Pre-registered hypothesis (frozen 2026-04-30) ==

H_self_trap (Grant's reframe of doc 30 §4):
    A propagating circularly-polarized T₂ photon at ω = ω_C with peak
    amplitude exceeding V_yield = √α · V_SNAP, injected into a bare
    K4 substrate, behaves as a "rifled bullet" — a cavitation-bubble
    wave packet whose intrinsic spin frequency aligns with the K4
    lattice's chirality, providing impedance match for free
    propagation. At the bond where local |V| crosses V_yield, Op14
    saturation engages, the chirality match breaks, the bubble
    coherence fails, and the photon's two intrinsic frequencies
    (forward propagation ω_C + spin ω_C·ε_hand) topology-lock at
    the breakdown site, producing a (2,3) torus-knot phase-space
    standing wave.

Per A28 architectural choice (doc 67 §15), engine substitutes Op14
z_local saturation reflection for loop-level Faraday-law BEMF; the
wake observable is the discriminator between "Grant's classical-EM
BEMF wake IS the engine mechanism" vs "Grant's reframe IS corpus-
physics, engine substitutes Op14 reflection."

== PASS criterion (BOTH must pass) ==

1. FREQUENCY: post-trap steady-state at trapped bond at ω_C ± α
   (1.0 ± 0.0073 in natural units) measured via FFT over the last
   25 Compton periods.

2. TOPOLOGY (corpus-canonical per A42): c=3 crossings via Op10 on
   the Cosserat ω field, computed via cosserat.extract_crossing_count()
   at end of run.

== Load-bearing secondary observables ==

(A) VELOCITY PROFILE (rifling-bullet kinematics, per Grant 2026-04-30):
    - v_g(t) = d⟨x⟩/dt, energy-weighted centroid velocity along +x
    - Predicted: ≈ √2 (Cartesian-axis K4-TLM speed) during free
      propagation; decelerates as ⟨A²⟩ grows; → 0 at trap
    - Compare against A-010 local-clock prediction:
      c_eff(A²) = c · √(1 - A²)

(B) SATURATION ENGAGEMENT: A² at trap site reaches √(2α) ≈ 0.117
    (Op14 onset threshold)

(C) TIR SIGNATURE: post-trap, Γ at saturation cells → -1 ± 0.1

(D) WAKE SIGNATURE (BEMF/Op14 discriminator per auditor 2026-04-30):
    - dV/dt opposite-sign behind photon's leading edge for ≥1 wavelength
    - PASS+wake → Grant's classical-EM BEMF reframe IS engine mechanism
    - PASS+no-wake → Grant's reframe is corpus-physics-correct;
      engine substitutes Op14 reflection (A28 substitution)

(E) SELF-SUSTENANCE: post-shutoff, configuration sustains ≥5 Compton
    periods at A² > A²_yield/2

(F) CHIRALITY ALIGNMENT (rifling-spin observable):
    - Cosserat ω rotation rate at wave-packet centroid
    - Should track ε_hand·ω_C during free propagation
    - At trap: locked or broken?

(G) PHASE-SPACE DIAGNOSTIC (R_phase/r_phase per A46, informational only):
    - (V_inc, V_ref) trajectory at trapped bond, post-trap
    - R_phase/r_phase aspect ratio — does it match φ²?
    - NOT pass-criterion (per A42 corpus-canonical = c via Op10);
      diagnostic only

== Configuration ==

- N=48 (active region 40 cells = 6.4 Compton wavelengths headroom)
- PML=4
- Cosserat ON, A28-corrected coupling per doc 67 §15:
    disable_cosserat_lc_force=True
    enable_cosserat_self_terms=True
    use_asymmetric_saturation=True (default; chirality bias enabled)
    axiom_4_enabled=True (saturation enabled)
- Source: SpatialDipoleCPSource
    x0 = 8 (just inside PML, leaves room for free propagation)
    propagation_axis = 0 (+x)
    handedness = "RH" (matches K4 right-handed chirality per doc 28 §3)
    amplitude = 0.10 V_SNAP (~1.17·V_yield, just above saturation onset)
    omega = 1.0 (ω_C natural units)
    sigma_yz = 4.0 (focused beam waist, ~λ_C/1.5 = 4.2 at λ_C=2π)
    envelope: t_ramp=2P, t_sustain=2P, t_decay=2P (6 Compton periods total
              source on; then off for 44 periods to test self-sustenance)
- Run: 50 Compton periods total (444 timesteps at dt=1/√2)
- State capture cadence: every 5 timesteps (~89 captures over run)

== A47 feasibility arithmetic ==

- λ_C = 2π · ℓ_node ≈ 6.28 cells
- Active region 40 cells = 6.4 wavelengths
- Wave packet of 6P envelope ≈ 6 wavelengths ≈ 38 cells
- Photon at v ≈ √2 traverses 40 cells in ~28 time units = 4.5 P
- Trap, if it happens, after 4-5 P; remaining 45 P observe sustenance
- Compute: 48³·4·8 bytes V_inc ≈ 14 MB/capture × 89 captures ≈ 1.2 GB
  → keep only V_inc + Cosserat ω; full-state on cadence is fine
- Run time estimate: ~60-90 min wall clock
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


# Constants in natural units
ALPHA = 1.0 / 137.035999
V_YIELD = float(np.sqrt(ALPHA))     # ≈ 0.0854 V_SNAP
A2_YIELD = ALPHA                    # A² at saturation onset
A2_OP14 = float(np.sqrt(2.0 * ALPHA))  # ≈ 0.117 (Op14 engagement)
OMEGA_C = 1.0
COMPTON_PERIOD = 2.0 * np.pi
DT = 1.0 / np.sqrt(2.0)


def setup_engine(N=48, PML=4):
    """A28-corrected coupled engine (doc 67 §15 + Cosserat self-terms)."""
    engine = VacuumEngine3D.from_args(
        N=N, pml=PML, temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,    # A28 correction
        enable_cosserat_self_terms=True,   # A28 strengthening (topology-stabilizing)
        use_asymmetric_saturation=True,    # default: chirality bias
        axiom_4_enabled=True,              # saturation enabled
    )
    return engine


def setup_source(N, ramp_periods=2.0, sustain_periods=2.0, decay_periods=2.0):
    """Chirally-spinning T₂ propagating photon, RH-handed, +x propagation."""
    return SpatialDipoleCPSource(
        x0=8,
        propagation_axis=0,
        amplitude=0.10,           # V_SNAP units; ~1.17 × V_yield
        omega=OMEGA_C,
        handedness="RH",          # K4 is RH-chiral per doc 28 §3
        sigma_yz=4.0,             # focused beam waist
        t_ramp=ramp_periods * COMPTON_PERIOD,
        t_sustain=sustain_periods * COMPTON_PERIOD,
        t_decay=decay_periods * COMPTON_PERIOD,
        y_c=None,                 # default: lattice center
        z_c=None,
    )


def compute_a2_field(V_inc, V_SNAP=1.0):
    """A² = |V_inc|² / V_SNAP² per port-summed strain."""
    v_total_sq = np.sum(V_inc ** 2, axis=-1)
    return v_total_sq / (V_SNAP ** 2)


def compute_centroid(V_inc, mask_active, axis=0, pml=4):
    """Energy-weighted centroid along propagation axis (PML excluded)."""
    N = V_inc.shape[0]
    energy = np.sum(V_inc ** 2, axis=-1)  # (N, N, N)
    energy = energy * mask_active.astype(float)

    # Exclude PML region per Rule 10 PML-cell-exclusion corollary
    interior = np.zeros_like(energy)
    interior[pml:N - pml, pml:N - pml, pml:N - pml] = (
        energy[pml:N - pml, pml:N - pml, pml:N - pml]
    )

    total = float(np.sum(interior))
    if total < 1e-30:
        return float("nan"), 0.0

    coords = np.arange(N, dtype=float)
    if axis == 0:
        marg = np.sum(interior, axis=(1, 2))
    elif axis == 1:
        marg = np.sum(interior, axis=(0, 2))
    else:
        marg = np.sum(interior, axis=(0, 1))

    centroid = float(np.sum(coords * marg) / total)
    return centroid, total


def compute_front(V_inc, mask_active, axis=0, pml=4, frac=0.5):
    """Leading edge along propagation axis: rightmost x where E(x)/E_max > frac."""
    N = V_inc.shape[0]
    energy = np.sum(V_inc ** 2, axis=-1) * mask_active.astype(float)
    interior = np.zeros_like(energy)
    interior[pml:N - pml, pml:N - pml, pml:N - pml] = (
        energy[pml:N - pml, pml:N - pml, pml:N - pml]
    )
    if axis == 0:
        marg = np.sum(interior, axis=(1, 2))
    elif axis == 1:
        marg = np.sum(interior, axis=(0, 2))
    else:
        marg = np.sum(interior, axis=(0, 1))

    if marg.max() < 1e-30:
        return float("nan")

    threshold = frac * marg.max()
    above = np.where(marg > threshold)[0]
    if len(above) == 0:
        return float("nan")
    return float(above[-1])


def fft_at(V_inc_traj_at_cell, dt, target_freqs):
    """FFT power at target angular freqs (rad/time unit)."""
    n = len(V_inc_traj_at_cell)
    if n < 16:
        return {f: 0.0 for f in target_freqs}
    fft_vals = np.fft.rfft(V_inc_traj_at_cell)
    freqs = np.fft.rfftfreq(n, d=dt) * 2.0 * np.pi
    fft_amp = 2.0 * np.abs(fft_vals) / n
    out = {}
    for f_target in target_freqs:
        idx = int(np.argmin(np.abs(freqs - f_target)))
        out[float(f_target)] = float(fft_amp[idx])
    return out


def main():
    print("=" * 78, flush=True)
    print("  T-ST: Photon Self-Trap Test")
    print("  Grant's rifling-bullet + cavitation-bubble reframe of doc 30 §4")
    print("  Pre-registered: H_self_trap (frequency at ω_C ± α + c=3 via Op10)")
    print("=" * 78, flush=True)

    N = 48
    PML = 4
    n_periods = 50
    n_steps = int(n_periods * COMPTON_PERIOD / DT)
    capture_cadence = 5

    print(f"\n  Lattice: N={N}, PML={PML} (active region {N - 2*PML} cells)")
    print(f"  Run: {n_periods} Compton periods = {n_steps} timesteps at dt={DT:.4f}")
    print(f"  Capture cadence: every {capture_cadence} steps "
          f"(~{n_steps // capture_cadence} captures)")
    print(f"  V_yield = √α = {V_YIELD:.4f}, A²_yield = {A2_YIELD:.4f}, "
          f"A²_op14 = {A2_OP14:.4f}")

    t_start = time.time()

    # Build engine + source
    engine = setup_engine(N=N, PML=PML)
    source = setup_source(N=N)
    engine.add_source(source)

    print(f"\n  Engine: A28-corrected coupling (disable_cosserat_lc_force=True, "
          f"enable_cosserat_self_terms=True)")
    print(f"  Source: SpatialDipoleCPSource RH @ x0=8, ω=1.0, A=0.10·V_SNAP "
          f"(~{0.10/V_YIELD:.2f}·V_yield)")
    print(f"  Source envelope: 2P ramp + 2P sustain + 2P decay = 6P on, "
          f"then off for 44P (self-sustenance window)")

    # Capture buffers
    captures = []   # list of dicts with t, centroid_x, max_a2_interior, ...
    centroid_traj = []
    front_traj = []
    centroid_a2_traj = []
    max_a2_traj = []
    max_a2_loc = []  # (x, y, z) of peak A² at each capture

    # Trap-bond V_inc time series (filled after we identify trap location)
    # We'll record per-cell V_inc for cells along propagation axis at lattice center y,z
    # for later FFT at the eventual trap site
    yc = N // 2
    zc = N // 2
    axial_v_inc_port0 = np.zeros((n_steps, N))   # port 0 at (x, yc, zc)
    axial_v_ref_port0 = np.zeros((n_steps, N))

    # Cosserat ω trajectory at axial centerline
    axial_omega_x = np.zeros((n_steps, N))   # ω_x at (x, yc, zc)
    axial_omega_y = np.zeros((n_steps, N))
    axial_omega_z = np.zeros((n_steps, N))

    print(f"\n  Running...", flush=True)

    for step_i in range(n_steps):
        engine.step()

        # Per-step axial samples (cheap)
        axial_v_inc_port0[step_i, :] = engine.k4.V_inc[:, yc, zc, 0]
        axial_v_ref_port0[step_i, :] = engine.k4.V_ref[:, yc, zc, 0]
        axial_omega_x[step_i, :] = engine.cos.omega[:, yc, zc, 0]
        axial_omega_y[step_i, :] = engine.cos.omega[:, yc, zc, 1]
        axial_omega_z[step_i, :] = engine.cos.omega[:, yc, zc, 2]

        # Periodic full-state capture
        if step_i % capture_cadence == 0:
            t_now = step_i * DT
            V_inc = engine.k4.V_inc
            mask = engine.k4.mask_active
            a2_field = compute_a2_field(V_inc, V_SNAP=engine.V_SNAP)
            # Mask interior + active
            a2_interior = a2_field.copy()
            a2_interior[~mask] = 0.0
            a2_interior[:PML, :, :] = 0.0
            a2_interior[N - PML:, :, :] = 0.0
            a2_interior[:, :PML, :] = 0.0
            a2_interior[:, N - PML:, :] = 0.0
            a2_interior[:, :, :PML] = 0.0
            a2_interior[:, :, N - PML:] = 0.0

            cx, total_e = compute_centroid(V_inc, mask, axis=0, pml=PML)
            front_x = compute_front(V_inc, mask, axis=0, pml=PML, frac=0.5)
            max_a2 = float(a2_interior.max())
            max_a2_idx = np.unravel_index(int(np.argmax(a2_interior)), a2_interior.shape)

            # A² at centroid (interpolate to nearest cell)
            if not np.isnan(cx):
                cx_int = int(np.clip(cx, 0, N - 1))
                a2_at_centroid = float(a2_interior[cx_int, yc, zc])
            else:
                a2_at_centroid = 0.0

            centroid_traj.append((t_now, cx))
            front_traj.append((t_now, front_x))
            centroid_a2_traj.append((t_now, a2_at_centroid))
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

            if step_i % (capture_cadence * 10) == 0:
                t_p = t_now / COMPTON_PERIOD
                elapsed = time.time() - t_start
                print(f"    t={t_p:5.2f}P  centroid_x={cx if not np.isnan(cx) else 0:6.2f}  "
                      f"front_x={front_x if not np.isnan(front_x) else 0:6.2f}  "
                      f"max_A²={max_a2:.4f} @ {tuple(max_a2_idx)}  "
                      f"({elapsed:.0f}s elapsed)")

    total_elapsed = time.time() - t_start
    print(f"\n  Engine evolution complete in {total_elapsed:.0f}s")

    # ============================================================
    # Post-hoc adjudication
    # ============================================================
    print("\n" + "=" * 78)
    print("  ADJUDICATION (per pre-registered criteria)")
    print("=" * 78)

    # Identify trap location: cell with max A² in the second half of run
    # (post-source-shutoff regime)
    second_half = [c for c in captures if c["t"] > 6.0 * COMPTON_PERIOD]
    if not second_half:
        print("\n  No captures in post-source regime — adjudication failed.")
        return

    # Trap candidate = cell with max time-integrated A² in second half
    max_a2_cells = [c["max_a2_loc"] for c in second_half]
    max_a2_vals = [c["max_a2_interior"] for c in second_half]

    # Most frequently visited peak location
    from collections import Counter
    cell_counter = Counter(tuple(loc) for loc in max_a2_cells)
    trap_cell, trap_count = cell_counter.most_common(1)[0]
    trap_x, trap_y, trap_z = trap_cell

    print(f"\n  Trap candidate cell: ({trap_x}, {trap_y}, {trap_z}) "
          f"(peak A² location in {trap_count}/{len(second_half)} post-shutoff captures)")

    # Saturation engagement check
    a2_at_trap_2nd_half = [
        c["max_a2_interior"] for c in second_half if tuple(c["max_a2_loc"]) == trap_cell
    ]
    if a2_at_trap_2nd_half:
        a2_trap_mean = float(np.mean(a2_at_trap_2nd_half))
        a2_trap_max = float(max(a2_at_trap_2nd_half))
    else:
        a2_trap_mean = 0.0
        a2_trap_max = 0.0
    saturation_engaged = a2_trap_max > A2_OP14
    print(f"  A² at trap (post-shutoff): max={a2_trap_max:.4f}, mean={a2_trap_mean:.4f}")
    print(f"  Saturation engagement (A² > {A2_OP14:.4f} = √(2α)): "
          f"{'YES' if saturation_engaged else 'NO'}")

    # FFT at trap cell over the post-shutoff window (last 25 P)
    post_shutoff_start = int(25.0 * COMPTON_PERIOD / DT)
    if post_shutoff_start < n_steps and trap_y == yc and trap_z == zc:
        v_at_trap = axial_v_inc_port0[post_shutoff_start:, trap_x]
        v_ref_at_trap = axial_v_ref_port0[post_shutoff_start:, trap_x]
        fft_targets = [OMEGA_C * (1.0 - 2 * ALPHA), OMEGA_C, OMEGA_C * (1.0 + 2 * ALPHA),
                       1.5, 2.96]
        fft_at_trap = fft_at(v_at_trap, DT, fft_targets)
        peak_freq_idx = int(np.argmax([fft_at_trap[f] for f in fft_targets]))
        peak_freq = fft_targets[peak_freq_idx]
        peak_amp = fft_at_trap[peak_freq]
        freq_match = abs(peak_freq - OMEGA_C) <= ALPHA
    else:
        # Trap not on axial line; FFT not extractable from current sampling
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
        print(f"    PEAK at f = {peak_freq:.4f}, amp = {peak_amp:.3e}")
        print(f"    Frequency match (|ω - ω_C| ≤ α): {'PASS' if freq_match else 'FAIL'}")
    else:
        print(f"    Trap off axial-sampling line; FFT not extractable from cheap capture.")

    # c via Op10
    try:
        c_op10 = int(engine.cos.extract_crossing_count())
    except Exception as exc:
        print(f"  Op10 extract_crossing_count failed: {exc}")
        c_op10 = -1
    topology_match = (c_op10 == 3)
    print(f"\n  TOPOLOGY criterion (target c=3 via Op10):")
    print(f"    extract_crossing_count = {c_op10}")
    print(f"    Topology match (c=3): {'PASS' if topology_match else 'FAIL'}")

    # Velocity profile
    print(f"\n  VELOCITY PROFILE (rifling-bullet kinematics):")
    centroid_arr = np.array([(t, x) for t, x in centroid_traj if not np.isnan(x)])
    if len(centroid_arr) > 5:
        ts = centroid_arr[:, 0]
        xs = centroid_arr[:, 1]
        # Free-propagation segment: first 4 P (before saturation)
        free_mask = ts < 4.0 * COMPTON_PERIOD
        if free_mask.sum() > 3:
            v_free = float(np.polyfit(ts[free_mask], xs[free_mask], 1)[0])
            print(f"    Free-propagation v_g (t < 4P): {v_free:.3f} cells/time-unit "
                  f"(predicted ≈ √2 = {np.sqrt(2):.3f})")
        # Late-time velocity (after presumed trap)
        late_mask = ts > 15.0 * COMPTON_PERIOD
        if late_mask.sum() > 3:
            v_late = float(np.polyfit(ts[late_mask], xs[late_mask], 1)[0])
            print(f"    Late-time v_g (t > 15P): {v_late:.3f} cells/time-unit "
                  f"(predicted ≈ 0 if trapped)")
            v_drop = (v_free - v_late) / max(v_free, 1e-6) if free_mask.sum() > 3 else 0.0
            print(f"    Velocity drop fraction: {v_drop:.3f} "
                  f"(close to 1.0 if cleanly trapped)")

    # Self-sustenance check: total energy in interior over time
    print(f"\n  SELF-SUSTENANCE (post-shutoff energy retention):")
    if len(captures) > 10:
        late_caps = [c for c in captures if c["t"] > 7.0 * COMPTON_PERIOD]
        if late_caps:
            e_traj = [c["total_energy"] for c in late_caps]
            e_first = e_traj[0]
            e_last = e_traj[-1]
            retention = e_last / e_first if e_first > 0 else 0.0
            print(f"    Energy at t=7P (post-source): {e_first:.3e}")
            print(f"    Energy at t=50P:                {e_last:.3e}")
            print(f"    Retention fraction: {retention:.3f} "
                  f"(near 1.0 if self-sustaining; near 0 if dissipates)")

    # Phase-space (V_inc, V_ref) trajectory at trap cell — post-shutoff
    if v_at_trap is not None and v_ref_at_trap is not None:
        # Crude R/r aspect from PCA on (V_inc, V_ref) cloud
        pts = np.stack([v_at_trap, v_ref_at_trap], axis=1)
        pts = pts - pts.mean(axis=0, keepdims=True)
        cov = (pts.T @ pts) / max(len(pts) - 1, 1)
        evals, _ = np.linalg.eigh(cov)
        evals = np.sort(np.maximum(evals, 0.0))[::-1]
        if evals[1] > 0:
            R_phase_over_r_phase = float(np.sqrt(evals[0] / evals[1]))
        else:
            R_phase_over_r_phase = float("inf")
        phi_squared = ((1.0 + np.sqrt(5.0)) / 2.0) ** 2
        print(f"\n  PHASE-SPACE diagnostic (R_phase/r_phase, informational only per A42):")
        print(f"    PCA aspect ratio: {R_phase_over_r_phase:.3f} (φ² = {phi_squared:.3f})")
    else:
        R_phase_over_r_phase = float("nan")
        phi_squared = float("nan")

    # Wake signature: dV/dt opposite-sign behind leading edge
    # Crude check: at a fixed time (mid-run), does dV/dt at front have opposite sign
    # from dV/dt at trail (1 wavelength behind)?
    print(f"\n  WAKE SIGNATURE (BEMF/Op14 discriminator):")
    mid_step = n_steps // 4   # ~12.5 P
    if mid_step + 5 < n_steps:
        v_now = axial_v_inc_port0[mid_step, :]
        v_next = axial_v_inc_port0[mid_step + 5, :]
        dv_dt = (v_next - v_now) / (5 * DT)
        # find leading edge (rightmost cell with |V|² > 0.1·peak)
        v_sq = v_now ** 2
        if v_sq.max() > 1e-20:
            front_x_idx = int(np.where(v_sq > 0.1 * v_sq.max())[0][-1])
            wavelength_cells = int(round(2 * np.pi))   # λ_C ≈ 6.28 cells
            trail_x_idx = max(front_x_idx - wavelength_cells, PML)
            sign_front = float(np.sign(dv_dt[front_x_idx]))
            sign_trail = float(np.sign(dv_dt[trail_x_idx]))
            opposite_signs = (sign_front * sign_trail < 0)
            print(f"    At t={mid_step * DT / COMPTON_PERIOD:.2f}P:")
            print(f"      front_x={front_x_idx}, dV/dt sign={sign_front:+.0f}")
            print(f"      trail_x={trail_x_idx}, dV/dt sign={sign_trail:+.0f}")
            print(f"    Opposite-sign wake (Grant's BEMF reframe): "
                  f"{'YES' if opposite_signs else 'NO'}")
        else:
            opposite_signs = False
            print(f"    Insufficient field amplitude to test wake signature")
    else:
        opposite_signs = False

    # ============================================================
    # Verdict
    # ============================================================
    print(f"\n{'=' * 78}")
    print(f"  VERDICT")
    print(f"{'=' * 78}")
    h_pass = freq_match and topology_match
    print(f"\n  PASS criterion:")
    print(f"    Frequency at ω_C ± α: {'PASS' if freq_match else 'FAIL'}")
    print(f"    Topology c=3 via Op10: {'PASS' if topology_match else 'FAIL'}")
    print(f"\n  H_self_trap: {'PASS' if h_pass else 'FAIL'}")

    if h_pass:
        print(f"  → Self-trap CONFIRMED at corpus criteria.")
        if opposite_signs:
            print(f"  → Wake signature PRESENT: Grant's BEMF reframe IS engine mechanism.")
        else:
            print(f"  → Wake signature ABSENT: Grant's reframe is corpus-physics-correct;")
            print(f"    engine substitutes Op14 saturation reflection (A28).")
    else:
        if saturation_engaged and topology_match:
            print(f"  → Trap formed (saturation + topology) but frequency mismatch — "
                  f"investigate.")
        elif saturation_engaged and not topology_match:
            print(f"  → Saturation engaged, configuration formed, but NOT (2,3) topology.")
            print(f"    Mode II/III: characterize-as-itself per Rule 10.")
        else:
            print(f"  → No clear self-trap. Photon may have passed through, "
                  f"dissipated, or dispersed.")

    # Save results
    out = {
        "test": "T-ST: Photon Self-Trap Test",
        "hypothesis": "H_self_trap (Grant's rifling-bullet reframe of doc 30 §4)",
        "config": {
            "N": N, "PML": PML, "n_periods": n_periods, "n_steps": n_steps,
            "amplitude_VSNAP": 0.10, "omega": OMEGA_C, "handedness": "RH",
            "x0": 8, "sigma_yz": 4.0,
            "envelope_periods": [2.0, 2.0, 2.0],
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
            "R_phase_over_r_phase": float(R_phase_over_r_phase) if not np.isnan(R_phase_over_r_phase) else None,
            "phi_squared_target": float(phi_squared) if not np.isnan(phi_squared) else None,
        },
        "captures": captures,
        "centroid_trajectory": [[float(t), float(x) if not np.isnan(x) else None]
                                for t, x in centroid_traj],
        "front_trajectory": [[float(t), float(x) if not np.isnan(x) else None]
                             for t, x in front_traj],
        "elapsed_total_s": total_elapsed,
    }
    out_path = Path(__file__).parent / "r10_v8_t_st_self_trap_results.json"
    out_path.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nSaved {out_path.relative_to(Path.cwd())}")

    # Save axial trajectories as npz (for post-hoc detailed analysis)
    npz_path = Path(__file__).parent / "r10_v8_t_st_self_trap_capture.npz"
    np.savez_compressed(
        npz_path,
        axial_v_inc_port0=axial_v_inc_port0,
        axial_v_ref_port0=axial_v_ref_port0,
        axial_omega_x=axial_omega_x,
        axial_omega_y=axial_omega_y,
        axial_omega_z=axial_omega_z,
        dt=DT, N=N, PML=PML, n_steps=n_steps,
    )
    print(f"Saved {npz_path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
