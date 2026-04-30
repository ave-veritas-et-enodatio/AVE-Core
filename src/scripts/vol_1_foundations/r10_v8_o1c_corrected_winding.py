"""
O.1c — Corrected V_inc Real-Space Winding Measurement.

Per auditor + implementer 2026-04-30 code review:
- (γ) confirmed: IC seeder encodes real-space (2,3) — theta = 2*phi + 3*psi
- (δ) confirmed: O.1b measurement was at psi=0/π singularity AND mixed
  phase modulation with chirality weights at ports [0,2]

This driver fixes both:
1. Sample toroidal contour at psi = π/4 (z-offset) — away from singularity
2. Sample poloidal contour at phi = 0 — independent winding measurement
3. Normalize V_inc per port by chirality_weight per cell — isolates pure
   phase modulation

Tests whether engine SUSTAINS the IC's real-space (2,3) pattern over 50P
closed evolution. Independent of corpus phase-space (2,3) question
(which is Rule 16 to Grant — separate track).

== Pre-registered observables ==

PRIMARY:
  (1) Toroidal winding at psi = π/4: target 2 (around major axis)
  (2) Poloidal winding at phi = 0: target 3 (around minor cross-section)

PASS criterion: (toroidal=2) AND (poloidal=3) → engine sustains real-space
(2,3) topology over 50P closed evolution. Mode III-equivalent at corpus
geometry resolved as positive at the seeder's encoded topology.

If toroidal winding returns nonzero but ≠2, OR poloidal nonzero but ≠3,
that's an interesting partial result — engine sustains some topology but
modified during transient.

== Configuration ==

Same as O.1b: N=48, PML=4, amp=0.1, R=8, r=4, 50P.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))
from ave.topological.vacuum_engine import VacuumEngine3D
from scripts.vol_1_foundations.tlm_electron_soliton_eigenmode import (
    initialize_2_3_voltage_ansatz,
)


COMPTON_PERIOD = 2.0 * np.pi
DT = 1.0 / np.sqrt(2.0)


# K4 tetrahedral port directions (from IC seeder)
PORTS = np.array([
    [+1.0, +1.0, +1.0],
    [+1.0, -1.0, -1.0],
    [-1.0, +1.0, -1.0],
    [-1.0, -1.0, +1.0],
]) / np.sqrt(3.0)


def chirality_weight_at(phi, psi, R, r, port_idx):
    """Compute chirality_weight per IC seeder formula at (phi, psi, port_idx)."""
    # (2,3) tangent components (matches IC seeder lines 80-91)
    dphi_x = -(R + r * np.cos(psi)) * np.sin(phi)
    dphi_y = (R + r * np.cos(psi)) * np.cos(phi)
    dphi_z = 0.0
    dpsi_x = -r * np.sin(psi) * np.cos(phi)
    dpsi_y = -r * np.sin(psi) * np.sin(phi)
    dpsi_z = r * np.cos(psi)
    t_x = 2.0 * dphi_x + 3.0 * dpsi_x
    t_y = 2.0 * dphi_y + 3.0 * dpsi_y
    t_z = 2.0 * dphi_z + 3.0 * dpsi_z
    t_mag = np.sqrt(t_x ** 2 + t_y ** 2 + t_z ** 2 + 1e-12)
    t_hat = np.array([t_x, t_y, t_z]) / t_mag
    return float(np.dot(PORTS[port_idx], t_hat))


def sample_v_inc_at(V_inc_field, phi_array, psi_value, R, r, N):
    """Sample V_inc at toroidal contour: vary phi, fixed psi.

    Returns chirality-normalized phasor (V_inc[0] + i V_inc[2]) at each phi,
    plus also raw values for diagnostic.
    """
    cx, cy, cz = (N - 1) / 2.0, (N - 1) / 2.0, (N - 1) / 2.0
    re_norm = []
    im_norm = []
    re_raw = []
    im_raw = []
    for phi in phi_array:
        # Position on toroidal shell at (phi, psi_value)
        x_real = cx + (R + r * np.cos(psi_value)) * np.cos(phi)
        y_real = cy + (R + r * np.cos(psi_value)) * np.sin(phi)
        z_real = cz + r * np.sin(psi_value)

        ix = int(round(x_real)); iy = int(round(y_real)); iz = int(round(z_real))
        ix = max(1, min(N - 2, ix))
        iy = max(1, min(N - 2, iy))
        iz = max(1, min(N - 2, iz))

        # Raw values
        v0 = V_inc_field[ix, iy, iz, 0]
        v2 = V_inc_field[ix, iy, iz, 2]
        re_raw.append(v0)
        im_raw.append(v2)

        # Chirality-normalized values
        c0 = chirality_weight_at(phi, psi_value, R, r, port_idx=0)
        c2 = chirality_weight_at(phi, psi_value, R, r, port_idx=2)
        # Avoid division by zero
        v0_norm = v0 / c0 if abs(c0) > 1e-3 else 0.0
        v2_norm = v2 / c2 if abs(c2) > 1e-3 else 0.0
        re_norm.append(v0_norm)
        im_norm.append(v2_norm)

    return (np.array(re_raw), np.array(im_raw),
            np.array(re_norm), np.array(im_norm))


def sample_v_inc_poloidal(V_inc_field, psi_array, phi_value, R, r, N):
    """Sample V_inc at poloidal contour: vary psi, fixed phi."""
    cx, cy, cz = (N - 1) / 2.0, (N - 1) / 2.0, (N - 1) / 2.0
    re_norm = []
    im_norm = []
    for psi in psi_array:
        x_real = cx + (R + r * np.cos(psi)) * np.cos(phi_value)
        y_real = cy + (R + r * np.cos(psi)) * np.sin(phi_value)
        z_real = cz + r * np.sin(psi)
        ix = int(round(x_real)); iy = int(round(y_real)); iz = int(round(z_real))
        ix = max(1, min(N - 2, ix))
        iy = max(1, min(N - 2, iy))
        iz = max(1, min(N - 2, iz))

        v0 = V_inc_field[ix, iy, iz, 0]
        v2 = V_inc_field[ix, iy, iz, 2]
        c0 = chirality_weight_at(phi_value, psi, R, r, port_idx=0)
        c2 = chirality_weight_at(phi_value, psi, R, r, port_idx=2)
        v0_norm = v0 / c0 if abs(c0) > 1e-3 else 0.0
        v2_norm = v2 / c2 if abs(c2) > 1e-3 else 0.0
        re_norm.append(v0_norm)
        im_norm.append(v2_norm)

    return np.array(re_norm), np.array(im_norm)


def winding_number(re_arr, im_arr):
    """Compute total winding number around contour (closed loop)."""
    angles = np.arctan2(im_arr, re_arr)
    # Unwrap
    unwrapped = np.unwrap(angles)
    # Add closure
    closure = np.angle(np.exp(1j * (np.arctan2(im_arr[0], re_arr[0])
                                     - np.arctan2(im_arr[-1], re_arr[-1]))))
    total = (unwrapped[-1] - unwrapped[0]) + closure
    return total / (2.0 * np.pi)


def main():
    print("=" * 78, flush=True)
    print("  O.1c — Corrected V_inc Real-Space Winding (psi-offset + chirality-normalized)")
    print("=" * 78, flush=True)

    N, PML = 48, 4
    n_steps = int(50 * COMPTON_PERIOD / DT)
    R_torus = 8.0
    r_torus = 4.0
    amp_ic = 0.1

    print(f"\n  Same config as O.1b: N={N}, R={R_torus}, r={r_torus}, amp={amp_ic}")

    t_start = time.time()
    engine = VacuumEngine3D.from_args(
        N=N, pml=PML, temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,
        enable_cosserat_self_terms=True,
        use_asymmetric_saturation=True,
        axiom_4_enabled=True,
    )

    initialize_2_3_voltage_ansatz(
        engine.k4, R=R_torus, r=r_torus, amplitude=amp_ic,
    )

    # Verify IC encodes (2,3) BEFORE evolution
    print(f"\n  Pre-evolution windings on initial V_inc field:")
    n_samples = 64
    phis = np.linspace(0, 2 * np.pi, n_samples, endpoint=False)
    psis = np.linspace(0, 2 * np.pi, n_samples, endpoint=False)

    # Toroidal at psi = π/4
    psi_tor = np.pi / 4
    re_raw_t0, im_raw_t0, re_norm_t0, im_norm_t0 = sample_v_inc_at(
        engine.k4.V_inc, phis, psi_tor, R_torus, r_torus, N
    )
    w_tor_raw_t0 = winding_number(re_raw_t0, im_raw_t0)
    w_tor_norm_t0 = winding_number(re_norm_t0, im_norm_t0)
    print(f"    Toroidal @ ψ=π/4: raw={w_tor_raw_t0:.3f}, "
          f"chirality-normalized={w_tor_norm_t0:.3f} (target 2)")

    # Poloidal at phi = 0 (slightly off to avoid x-axis singularity)
    phi_pol = 0.1
    re_pol_t0, im_pol_t0 = sample_v_inc_poloidal(
        engine.k4.V_inc, psis, phi_pol, R_torus, r_torus, N
    )
    w_pol_norm_t0 = winding_number(re_pol_t0, im_pol_t0)
    print(f"    Poloidal @ φ=0.1: chirality-normalized={w_pol_norm_t0:.3f} (target 3)")

    # Run evolution
    print(f"\n  Running {n_steps} steps...", flush=True)
    energy_traj = []
    for step_i in range(n_steps):
        engine.step()
        if step_i % 50 == 0:
            t_p = step_i * DT / COMPTON_PERIOD
            a2 = np.sum(engine.k4.V_inc ** 2, axis=-1)
            mask = engine.k4.mask_active
            a2_int = a2 * mask.astype(float)
            a2_int[:PML, :, :] = 0; a2_int[N-PML:, :, :] = 0
            a2_int[:, :PML, :] = 0; a2_int[:, N-PML:, :] = 0
            a2_int[:, :, :PML] = 0; a2_int[:, :, N-PML:] = 0
            e_total = float(a2_int.sum())
            energy_traj.append((t_p, e_total))
            if step_i % 100 == 0:
                print(f"    t={t_p:5.2f}P  E={e_total:.3e}  "
                      f"({time.time() - t_start:.0f}s)", flush=True)

    elapsed = time.time() - t_start
    print(f"\n  Engine evolution complete in {elapsed:.0f}s")

    # Post-evolution windings
    print(f"\n  Post-evolution windings on final V_inc field (t=50P):")

    re_raw_t50, im_raw_t50, re_norm_t50, im_norm_t50 = sample_v_inc_at(
        engine.k4.V_inc, phis, psi_tor, R_torus, r_torus, N
    )
    w_tor_raw_t50 = winding_number(re_raw_t50, im_raw_t50)
    w_tor_norm_t50 = winding_number(re_norm_t50, im_norm_t50)

    re_pol_t50, im_pol_t50 = sample_v_inc_poloidal(
        engine.k4.V_inc, psis, phi_pol, R_torus, r_torus, N
    )
    w_pol_norm_t50 = winding_number(re_pol_t50, im_pol_t50)

    print(f"    Toroidal @ ψ=π/4: raw={w_tor_raw_t50:.3f}, "
          f"chirality-normalized={w_tor_norm_t50:.3f} (target 2)")
    print(f"    Poloidal @ φ=0.1: chirality-normalized={w_pol_norm_t50:.3f} (target 3)")

    # Comparison summary
    print(f"\n  WINDING COMPARISON (IC → 50P evolution):")
    print(f"  {'measure':>30} {'@ t=0':>10} {'@ t=50P':>10} {'target':>8}")
    print(f"  {'Toroidal raw (no chirality)':>30} {w_tor_raw_t0:>10.3f} {w_tor_raw_t50:>10.3f} {'2':>8}")
    print(f"  {'Toroidal chirality-normalized':>30} {w_tor_norm_t0:>10.3f} {w_tor_norm_t50:>10.3f} {'2':>8}")
    print(f"  {'Poloidal chirality-normalized':>30} {w_pol_norm_t0:>10.3f} {w_pol_norm_t50:>10.3f} {'3':>8}")

    # Verdict
    tor_pass = abs(w_tor_norm_t50 - 2) < 0.5
    pol_pass = abs(w_pol_norm_t50 - 3) < 0.5
    h_pass = tor_pass and pol_pass

    print(f"\n  VERDICT")
    print(f"  Toroidal winding (target 2): {'PASS' if tor_pass else 'FAIL'}")
    print(f"  Poloidal winding (target 3): {'PASS' if pol_pass else 'FAIL'}")
    print(f"  Engine sustains real-space (2,3) topology: "
          f"{'PASS' if h_pass else 'FAIL'}")

    # Energy retention
    if energy_traj:
        e0 = energy_traj[0][1]
        e_end = energy_traj[-1][1]
        retention = e_end / max(e0, 1e-30)
        print(f"\n  Energy retention 50P: {retention:.3f}")

    out = {
        "test": "O.1c: corrected V_inc real-space winding",
        "config": {"N": N, "PML": PML, "R": R_torus, "r": r_torus, "amp": amp_ic},
        "windings_at_t0": {
            "toroidal_raw": float(w_tor_raw_t0),
            "toroidal_chirality_normalized": float(w_tor_norm_t0),
            "poloidal_chirality_normalized": float(w_pol_norm_t0),
        },
        "windings_at_t50P": {
            "toroidal_raw": float(w_tor_raw_t50),
            "toroidal_chirality_normalized": float(w_tor_norm_t50),
            "poloidal_chirality_normalized": float(w_pol_norm_t50),
        },
        "verdict": {
            "toroidal_pass": bool(tor_pass),
            "poloidal_pass": bool(pol_pass),
            "real_space_2_3_sustained": bool(h_pass),
        },
        "elapsed_total_s": float(elapsed),
    }
    out_path = Path(__file__).parent / "r10_v8_o1c_corrected_winding_results.json"
    out_path.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nSaved {out_path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
