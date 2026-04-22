"""
Phase-space discovery — let the K4 TLM reveal its own phase-space
structure for the (2,3) bound state, without imposing Ch 8 / synthesis
expectations.

Pivot from phasor_trajectory_test.py: that script pre-registered
aspect-ratio predictions and saw degenerate 1D trajectories at
antinodes — confirming, but not discriminating hypotheses. This
script instead samples the full soliton state across space at a
fixed time and asks: given the (2,3) winding bound state the TLM
actually produces, what 2D phase-space structures are natively
present?

Projections examined (none pre-registered — discovery mode):

  P1. LC-tank Lissajous: (V_phys, I_phys) per port, across active
      lattice sites. V_phys = V_inc + V_ref, I_phys = V_inc - V_ref.
      If the soliton is a standing LC tank, each port's cloud traces
      a characteristic 2D shape. Aspect ratio = Q-like invariant.

  P2. Complex-amplitude: c(r) = V_inc_p0(r) + i * V_inc_p2(r). The
      ansatz encodes theta_wind = 2*phi + 3*psi as port-quadrature
      (cos on ports 0,1; sin on ports 2,3). Plotting (Re c, Im c)
      across shell sites reveals the phase-winding topology.

  P3. Port-pair correlation matrix: full 4x4 correlation across
      ports at each shell site, averaged. Principal components
      reveal the intrinsic dimensionality of the port-space.

  P4. Shell-radial distribution: |V| as a function of (toroidal
      angle phi, poloidal angle psi). Reveals whether the (2,3)
      winding is preserved after relaxation.

Outputs printed to stdout; raw data saved to /tmp for optional
plotting downstream.
"""
from __future__ import annotations

import numpy as np

from ave.core.k4_tlm import K4Lattice3D
from tlm_electron_soliton_eigenmode import initialize_2_3_voltage_ansatz

PHI = (1.0 + np.sqrt(5.0)) / 2.0


def run_and_snapshot(
    N: int = 64,
    R: float = 16.0,
    r: float = 6.108,
    n_steps: int = 300,
    amplitude: float = 0.5,
    pml_thickness: int = 6,
    snapshot_steps: tuple[int, ...] = (100, 200, 300),
) -> dict:
    """Run TLM, snapshot full state at requested steps."""
    lattice = K4Lattice3D(
        N, N, N, dx=1.0,
        pml_thickness=pml_thickness,
        nonlinear=False,
        op3_bond_reflection=True,
    )
    initialize_2_3_voltage_ansatz(lattice, R=R, r=r, amplitude=amplitude)

    snapshots = {}
    for step in range(1, n_steps + 1):
        lattice.step()
        if step in snapshot_steps:
            snapshots[step] = {
                "V_inc": lattice.V_inc.copy(),
                "V_ref": lattice.V_ref.copy(),
                "mask_A": lattice.mask_A.copy(),
                "mask_B": lattice.mask_B.copy(),
            }
    return {
        "lattice": lattice,
        "snapshots": snapshots,
        "N": N, "R": R, "r": r, "n_steps": n_steps,
    }


def select_shell_sites(V_inc, V_ref, mask_active, threshold_frac=0.3):
    """Return boolean mask of sites where total |V|^2 exceeds
    threshold_frac of the maximum. These are the soliton-shell sites."""
    V_total_sq = np.sum(V_inc ** 2 + V_ref ** 2, axis=-1)
    V_total_sq_active = V_total_sq * mask_active
    peak = V_total_sq_active.max()
    return (V_total_sq_active > threshold_frac * peak) & mask_active


def principal_axes(points_xy: np.ndarray) -> tuple[float, float, float]:
    centered = points_xy - points_xy.mean(axis=0)
    cov = np.cov(centered.T)
    eigvals, _ = np.linalg.eigh(cov)
    eigvals = np.sort(eigvals)[::-1]
    if eigvals[0] <= 0 or eigvals[1] <= 0:
        return 0.0, 0.0, float("inf")
    return float(np.sqrt(eigvals[0])), float(np.sqrt(eigvals[1])), \
        float(np.sqrt(eigvals[0] / max(eigvals[1], 1e-30)))


def analyze_snapshot(snap, N: int, step_label: int) -> dict:
    """Apply projections P1-P4 to a snapshot, return summary dict."""
    V_inc = snap["V_inc"]
    V_ref = snap["V_ref"]
    mask_A = snap["mask_A"]
    mask_B = snap["mask_B"]
    mask_active = mask_A | mask_B

    shell = select_shell_sites(V_inc, V_ref, mask_active, threshold_frac=0.3)
    n_shell = int(shell.sum())

    V_phys = V_inc + V_ref
    I_phys = V_inc - V_ref    # Z_0 normalized to 1

    # Shell-site values, shape (n_shell, 4)
    V_shell = V_phys[shell]
    I_shell = I_phys[shell]
    V_inc_shell = V_inc[shell]

    print(f"\n--- Step {step_label}: {n_shell} shell sites above threshold ---")

    # P1: LC-tank Lissajous (V_phys, I_phys) per port
    print("P1  (V_phys, I_phys) Lissajous per port across shell sites:")
    print(f"    {'port':>4s} {'V_rms':>10s} {'I_rms':>10s} "
          f"{'major':>10s} {'minor':>10s} {'aspect':>10s}")
    p1_ratios = []
    for port in range(4):
        pts = np.column_stack([V_shell[:, port], I_shell[:, port]])
        smaj, smin, ratio = principal_axes(pts)
        p1_ratios.append(ratio)
        v_rms = np.sqrt(np.mean(V_shell[:, port] ** 2))
        i_rms = np.sqrt(np.mean(I_shell[:, port] ** 2))
        print(f"    {port:>4d} {v_rms:>10.3e} {i_rms:>10.3e} "
              f"{smaj:>10.3e} {smin:>10.3e} {ratio:>10.3f}")

    # P2: complex amplitude c = V_inc_p0 + i * V_inc_p2 across shell
    c_shell = V_inc_shell[:, 0] + 1j * V_inc_shell[:, 2]
    pts_c = np.column_stack([c_shell.real, c_shell.imag])
    smaj_c, smin_c, ratio_c = principal_axes(pts_c)
    c_mag = np.abs(c_shell)
    c_mag_min = float(c_mag.min())
    c_mag_max = float(c_mag.max())
    c_mag_mean = float(c_mag.mean())
    print(f"P2  Complex amplitude c = V_inc[p0] + i*V_inc[p2] across shell:")
    print(f"    Re-Im cloud: major = {smaj_c:.3e}, minor = {smin_c:.3e}, "
          f"aspect = {ratio_c:.3f}")
    print(f"    |c| stats: min = {c_mag_min:.3e}, max = {c_mag_max:.3e}, "
          f"mean = {c_mag_mean:.3e}")
    print(f"    |c| ratio max/min = {c_mag_max / max(c_mag_min, 1e-30):.3f}")

    # P3: port correlation matrix (average over shell sites)
    # C_pq = <V_inc_p * V_inc_q> / sqrt(<V_inc_p^2><V_inc_q^2>)
    corr_matrix = np.corrcoef(V_inc_shell.T)   # shape (4, 4)
    eigvals_corr = np.sort(np.linalg.eigvalsh(corr_matrix))[::-1]
    print(f"P3  Port correlation eigenvalues: {eigvals_corr.round(3).tolist()}")
    print(f"    (4 ports; if {eigvals_corr[0]:.2f} dominates, ports collapse"
          f" to 1 effective dim)")

    # P4: shell geometry in real space — parameterize by (phi, psi)
    # Find shell-site positions in (toroidal_angle, poloidal_angle).
    idx_shell = np.argwhere(shell)
    cx = (N - 1) / 2.0
    cy = (N - 1) / 2.0
    cz = (N - 1) / 2.0
    xs = idx_shell[:, 0] - cx
    ys = idx_shell[:, 1] - cy
    zs = idx_shell[:, 2] - cz
    rho = np.sqrt(xs ** 2 + ys ** 2)
    phi_tor = np.arctan2(ys, xs)
    # Poloidal angle: angle in the (rho, z) plane relative to torus center
    # at radius R_torus ≈ radius where shell peaks
    R_peak = float(np.median(rho))
    psi_pol = np.arctan2(zs, rho - R_peak)
    print(f"P4  Shell geometry: R_peak (real space) = {R_peak:.3f}")
    print(f"    rho range = [{float(rho.min()):.2f}, "
          f"{float(rho.max()):.2f}]")
    print(f"    z   range = [{float(zs.min()):.2f}, "
          f"{float(zs.max()):.2f}]")
    # Fit (2,3) winding: does theta_measured = arg(c) track 2*phi + 3*psi?
    theta_meas = np.angle(c_shell)
    theta_pred = 2 * phi_tor + 3 * psi_pol
    # Wrap both into [-pi, pi]
    delta = np.angle(np.exp(1j * (theta_meas - theta_pred)))
    # Measure alignment: fraction of sites with |delta| < pi/4
    frac_aligned = float(np.mean(np.abs(delta) < np.pi / 4))
    print(f"    (2,3) winding preserved: {frac_aligned * 100:.1f}% of shell "
          f"sites within pi/4 of theta=2phi+3psi")

    return {
        "step": step_label,
        "n_shell": n_shell,
        "p1_ratios": p1_ratios,
        "p2_aspect": ratio_c,
        "p2_mag_max_min": c_mag_max / max(c_mag_min, 1e-30),
        "p3_eigvals": eigvals_corr.tolist(),
        "p4_R_peak": R_peak,
        "p4_winding_alignment": frac_aligned,
        "shell_points": {
            "re_c": pts_c[:, 0], "im_c": pts_c[:, 1],
            "V_port0": V_shell[:, 0], "I_port0": I_shell[:, 0],
            "phi": phi_tor, "psi": psi_pol, "c_mag": c_mag,
        },
    }


def main():
    print("=" * 72)
    print("PHASE-SPACE DISCOVERY — let the K4 reveal its own structure")
    print("=" * 72)
    print(f"Target R/r for reference: Golden Torus = φ² = {PHI**2:.4f}")
    print(f"Target R/r for reference: TLM attractor ≈ 2.27")
    print(f"Target R/r for reference: full Clifford ≈ 2.0")
    print()

    result = run_and_snapshot(N=64, n_steps=300,
                              snapshot_steps=(100, 200, 300))
    print(f"Lattice N = {result['N']}, steps run = {result['n_steps']}")
    print(f"Seed (R, r) = ({result['R']:.2f}, {result['r']:.3f}) — Golden"
          f" Torus proportions in real space")

    summaries = []
    for step in sorted(result["snapshots"].keys()):
        summary = analyze_snapshot(
            result["snapshots"][step], result["N"], step
        )
        summaries.append(summary)

    print()
    print("=" * 72)
    print("TIME EVOLUTION SUMMARY:")
    print("=" * 72)
    print(f"{'step':>6s} {'shell':>6s} "
          f"{'p0_aspect':>10s} {'c_aspect':>10s} "
          f"{'|c| max/min':>12s} {'wind %':>8s} {'R_peak':>8s}")
    for s in summaries:
        print(f"{s['step']:>6d} {s['n_shell']:>6d} "
              f"{s['p1_ratios'][0]:>10.3f} {s['p2_aspect']:>10.3f} "
              f"{s['p2_mag_max_min']:>12.3f} "
              f"{s['p4_winding_alignment'] * 100:>8.1f} "
              f"{s['p4_R_peak']:>8.3f}")

    # Save for plotting
    np.savez(
        "/tmp/phasor_discovery.npz",
        **{f"step_{s['step']}_re_c": s["shell_points"]["re_c"] for s in summaries},
        **{f"step_{s['step']}_im_c": s["shell_points"]["im_c"] for s in summaries},
        **{f"step_{s['step']}_V0": s["shell_points"]["V_port0"] for s in summaries},
        **{f"step_{s['step']}_I0": s["shell_points"]["I_port0"] for s in summaries},
        **{f"step_{s['step']}_phi": s["shell_points"]["phi"] for s in summaries},
        **{f"step_{s['step']}_psi": s["shell_points"]["psi"] for s in summaries},
        **{f"step_{s['step']}_cmag": s["shell_points"]["c_mag"] for s in summaries},
    )
    print()
    print(f"Raw snapshots saved: /tmp/phasor_discovery.npz")


if __name__ == "__main__":
    main()
