"""
O.1d — Real-Space Winding Measurement v2 (multiplicative extraction).

Per A47 v5: division-based chirality normalization breaks at c=0
zero-crossings (sets phasor to 0/0 fallback, breaks unwrap). Use
multiplicative formulation:

  V_inc[0] · c_2 = envelope · c_0·c_2 · cos(theta_wind)
  V_inc[2] · c_0 = envelope · c_0·c_2 · sin(theta_wind)
  Phase = arctan2(V_inc[2]·c_0, V_inc[0]·c_2) = theta_wind exactly

The c_0·c_2 product modulates magnitude but not phase. Robust to
individual c_0 or c_2 zero-crossings.

Same configuration as O.1b/O.1c: N=48, amp=0.1, R=8, r=4.
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

PORTS = np.array([
    [+1.0, +1.0, +1.0],
    [+1.0, -1.0, -1.0],
    [-1.0, +1.0, -1.0],
    [-1.0, -1.0, +1.0],
]) / np.sqrt(3.0)


def chirality_weight_at(phi, psi, R, r, port_idx):
    """Match IC seeder's chirality_weight formula at (phi, psi)."""
    dphi_x = -(R + r * np.cos(psi)) * np.sin(phi)
    dphi_y = (R + r * np.cos(psi)) * np.cos(phi)
    dphi_z = 0.0
    dpsi_x = -r * np.sin(psi) * np.cos(phi)
    dpsi_y = -r * np.sin(psi) * np.sin(phi)
    dpsi_z = r * np.cos(psi)
    t_x = 2.0 * dphi_x + 3.0 * dpsi_x
    t_y = 2.0 * dphi_y + 3.0 * dpsi_y
    t_z = 2.0 * dphi_z + 3.0 * dpsi_z
    t_mag = np.sqrt(t_x**2 + t_y**2 + t_z**2 + 1e-12)
    t_hat = np.array([t_x, t_y, t_z]) / t_mag
    return float(np.dot(PORTS[port_idx], t_hat))


def winding_via_multiplicative(V_inc_field, R, r, N,
                                psi_value, phi_array, port_pair=(0, 2)):
    """A47 v5 corrected: phase = arctan2(V[p2]·c_0, V[p0]·c_2)."""
    cx, cy, cz = (N - 1) / 2.0, (N - 1) / 2.0, (N - 1) / 2.0
    p0, p2 = port_pair
    re_vals = []
    im_vals = []
    c0_vals = []
    c2_vals = []
    for phi in phi_array:
        x_real = cx + (R + r * np.cos(psi_value)) * np.cos(phi)
        y_real = cy + (R + r * np.cos(psi_value)) * np.sin(phi)
        z_real = cz + r * np.sin(psi_value)
        ix = max(1, min(N - 2, int(round(x_real))))
        iy = max(1, min(N - 2, int(round(y_real))))
        iz = max(1, min(N - 2, int(round(z_real))))

        v_p0 = V_inc_field[ix, iy, iz, p0]
        v_p2 = V_inc_field[ix, iy, iz, p2]
        c0 = chirality_weight_at(phi, psi_value, R, r, p0)
        c2 = chirality_weight_at(phi, psi_value, R, r, p2)

        re_vals.append(v_p0 * c2)
        im_vals.append(v_p2 * c0)
        c0_vals.append(c0)
        c2_vals.append(c2)

    re = np.array(re_vals)
    im = np.array(im_vals)
    angles = np.arctan2(im, re)
    unwrapped = np.unwrap(angles)
    closure = np.angle(np.exp(1j * (np.arctan2(im[0], re[0])
                                     - np.arctan2(im[-1], re[-1]))))
    total = (unwrapped[-1] - unwrapped[0]) + closure
    return total / (2.0 * np.pi), np.array(c0_vals), np.array(c2_vals)


def winding_poloidal_multiplicative(V_inc_field, R, r, N,
                                     phi_value, psi_array, port_pair=(0, 2)):
    """Poloidal winding via multiplicative extraction."""
    cx, cy, cz = (N - 1) / 2.0, (N - 1) / 2.0, (N - 1) / 2.0
    p0, p2 = port_pair
    re_vals, im_vals = [], []
    for psi in psi_array:
        x_real = cx + (R + r * np.cos(psi)) * np.cos(phi_value)
        y_real = cy + (R + r * np.cos(psi)) * np.sin(phi_value)
        z_real = cz + r * np.sin(psi)
        ix = max(1, min(N - 2, int(round(x_real))))
        iy = max(1, min(N - 2, int(round(y_real))))
        iz = max(1, min(N - 2, int(round(z_real))))

        v_p0 = V_inc_field[ix, iy, iz, p0]
        v_p2 = V_inc_field[ix, iy, iz, p2]
        c0 = chirality_weight_at(phi_value, psi, R, r, p0)
        c2 = chirality_weight_at(phi_value, psi, R, r, p2)

        re_vals.append(v_p0 * c2)
        im_vals.append(v_p2 * c0)

    re = np.array(re_vals)
    im = np.array(im_vals)
    angles = np.arctan2(im, re)
    unwrapped = np.unwrap(angles)
    closure = np.angle(np.exp(1j * (np.arctan2(im[0], re[0])
                                     - np.arctan2(im[-1], re[-1]))))
    total = (unwrapped[-1] - unwrapped[0]) + closure
    return total / (2.0 * np.pi)


def main():
    print("=" * 78, flush=True)
    print("  O.1d — Multiplicative winding extraction (A47 v5 fix)")
    print("=" * 78, flush=True)

    N, PML = 48, 4
    n_steps = int(50 * COMPTON_PERIOD / DT)
    R, r = 8.0, 4.0
    amp = 0.1
    n_samples = 64

    t_start = time.time()
    engine = VacuumEngine3D.from_args(
        N=N, pml=PML, temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,
        enable_cosserat_self_terms=True,
        use_asymmetric_saturation=True,
        axiom_4_enabled=True,
    )
    initialize_2_3_voltage_ansatz(engine.k4, R=R, r=r, amplitude=amp)

    phis = np.linspace(0, 2 * np.pi, n_samples, endpoint=False)
    psis = np.linspace(0, 2 * np.pi, n_samples, endpoint=False)

    # IC verification
    print(f"\n  Pre-evolution windings (multiplicative extraction):")
    w_tor_ic, c0_ic, c2_ic = winding_via_multiplicative(
        engine.k4.V_inc, R, r, N, np.pi / 4, phis
    )
    w_pol_ic = winding_poloidal_multiplicative(
        engine.k4.V_inc, R, r, N, 0.1, psis
    )
    print(f"    Toroidal @ ψ=π/4: {w_tor_ic:.3f} (target 2)")
    print(f"    Poloidal @ φ=0.1: {w_pol_ic:.3f} (target 3)")
    print(f"    c_0 range: [{c0_ic.min():.3f}, {c0_ic.max():.3f}], "
          f"# sign-changes: {(np.diff(np.sign(c0_ic)) != 0).sum()}")
    print(f"    c_2 range: [{c2_ic.min():.3f}, {c2_ic.max():.3f}], "
          f"# sign-changes: {(np.diff(np.sign(c2_ic)) != 0).sum()}")

    # Run
    print(f"\n  Running {n_steps} steps...", flush=True)
    for step_i in range(n_steps):
        engine.step()
        if step_i % 100 == 0:
            t_p = step_i * DT / COMPTON_PERIOD
            print(f"    t={t_p:5.2f}P  ({time.time() - t_start:.0f}s)", flush=True)

    elapsed = time.time() - t_start
    print(f"\n  Engine evolution complete in {elapsed:.0f}s")

    # Post-evolution
    print(f"\n  Post-evolution windings (multiplicative extraction):")
    w_tor_50P, _, _ = winding_via_multiplicative(
        engine.k4.V_inc, R, r, N, np.pi / 4, phis
    )
    w_pol_50P = winding_poloidal_multiplicative(
        engine.k4.V_inc, R, r, N, 0.1, psis
    )
    print(f"    Toroidal @ ψ=π/4: {w_tor_50P:.3f} (target 2)")
    print(f"    Poloidal @ φ=0.1: {w_pol_50P:.3f} (target 3)")

    # Cross-check at additional psi values
    print(f"\n  Cross-check toroidal at multiple ψ values (final state):")
    for psi_test in [np.pi / 6, np.pi / 4, np.pi / 3, np.pi / 2, 2 * np.pi / 3]:
        w, _, _ = winding_via_multiplicative(
            engine.k4.V_inc, R, r, N, psi_test, phis
        )
        print(f"    ψ={psi_test:.3f} ({psi_test/np.pi:.2f}π): toroidal = {w:.3f}")

    print(f"\n  Cross-check poloidal at multiple φ values (final state):")
    for phi_test in [0.1, np.pi / 4, np.pi / 2, np.pi, 3 * np.pi / 2]:
        w = winding_poloidal_multiplicative(
            engine.k4.V_inc, R, r, N, phi_test, psis
        )
        print(f"    φ={phi_test:.3f} ({phi_test/np.pi:.2f}π): poloidal = {w:.3f}")

    # Verdict
    tor_ic_pass = abs(w_tor_ic - 2) < 0.5
    pol_ic_pass = abs(w_pol_ic - 3) < 0.5
    tor_50P_pass = abs(w_tor_50P - 2) < 0.5
    pol_50P_pass = abs(w_pol_50P - 3) < 0.5

    print(f"\n  IC matches (2,3): toroidal={tor_ic_pass}, poloidal={pol_ic_pass}")
    print(f"  Engine sustains (2,3) at 50P: toroidal={tor_50P_pass}, poloidal={pol_50P_pass}")

    out = {
        "test": "O.1d: multiplicative winding extraction",
        "config": {"N": N, "amp": amp, "R": R, "r": r},
        "windings_ic": {
            "toroidal_at_psi_pi_4": float(w_tor_ic),
            "poloidal_at_phi_0p1": float(w_pol_ic),
            "c0_signs_changes_toroidal": int((np.diff(np.sign(c0_ic)) != 0).sum()),
            "c2_signs_changes_toroidal": int((np.diff(np.sign(c2_ic)) != 0).sum()),
        },
        "windings_50P": {
            "toroidal_at_psi_pi_4": float(w_tor_50P),
            "poloidal_at_phi_0p1": float(w_pol_50P),
        },
        "ic_pass": {"toroidal": bool(tor_ic_pass), "poloidal": bool(pol_ic_pass)},
        "evolution_pass": {"toroidal": bool(tor_50P_pass), "poloidal": bool(pol_50P_pass)},
        "elapsed_total_s": float(elapsed),
    }
    out_path = Path(__file__).parent / "r10_v8_o1d_winding_v2_results.json"
    out_path.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nSaved {out_path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
