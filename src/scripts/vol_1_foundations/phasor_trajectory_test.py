"""
Phasor trajectory test — L3 Phase-3 empirical check of the two-node
electron hypothesis (synthesis §5.1).

Hypothesis (pre-registered):
    If the electron is a two-node flux oscillation whose Golden Torus
    geometry lives in PHASE SPACE rather than real space, then the
    (V_inc, V_ref) trajectory on a single A-B bond near the soliton
    core should trace a torus-like limit cycle in phase space.

Predicted outcomes:
    (A) Trajectory is a torus with R_phase / r_phase ≈ φ² ≈ 2.618
        → Phase-space Golden Torus hypothesis confirmed.
    (B) Trajectory is a torus with ratio ≈ 2.0 or ≈ 2.27
        → Classical (p,q)=(2,3) configuration without spin-1/2 half-cover.
    (C) Trajectory is chaotic / dispersive / no clean ratio
        → Phase-space framing is falsified; revisit the synthesis.

This script reuses the TLM machinery in
tlm_electron_soliton_eigenmode.py and adds per-step per-bond recording
at four A-sublattice sites on the toroidal equator.
"""
from __future__ import annotations

import numpy as np

from ave.core.k4_tlm import K4Lattice3D
from tlm_electron_soliton_eigenmode import initialize_2_3_voltage_ansatz

PHI = (1.0 + np.sqrt(5.0)) / 2.0


def find_nearest_A_site(lattice: K4Lattice3D, target):
    """Return (i,j,k) of the mask_A site closest to the target position."""
    nx, ny, nz = lattice.nx, lattice.ny, lattice.nz
    A_idx = np.argwhere(lattice.mask_A)
    dists = np.linalg.norm(A_idx - np.array(target), axis=1)
    return tuple(A_idx[np.argmin(dists)])


def principal_axes(trajectory_xy: np.ndarray) -> tuple[float, float, float]:
    """Return (semi_major, semi_minor, ratio) of an ellipse-like
    point cloud via PCA on centered coordinates."""
    centered = trajectory_xy - trajectory_xy.mean(axis=0)
    cov = np.cov(centered.T)
    eigvals, _ = np.linalg.eigh(cov)
    eigvals = np.sort(eigvals)[::-1]
    semi_major = float(np.sqrt(eigvals[0]))
    semi_minor = float(np.sqrt(max(eigvals[1], 1e-30)))
    ratio = semi_major / semi_minor if semi_minor > 0 else float("inf")
    return semi_major, semi_minor, ratio


def run_phasor_test(
    N: int = 64,
    R: float = 16.0,      # 0.25 * N — matches existing conv. study scaling
    r: float = 6.108,     # R / φ² — Golden Torus aspect seeded in real space
    n_steps: int = 400,
    amplitude: float = 0.5,
    pml_thickness: int = 6,
) -> dict:
    lattice = K4Lattice3D(
        N, N, N, dx=1.0,
        pml_thickness=pml_thickness,
        nonlinear=False,
        op3_bond_reflection=True,
    )
    initialize_2_3_voltage_ansatz(lattice, R=R, r=r, amplitude=amplitude)

    cx = (lattice.nx - 1) / 2.0
    cy = (lattice.ny - 1) / 2.0
    cz = (lattice.nz - 1) / 2.0

    # Four probe sites around the toroidal equator at radius R,
    # each snapped to the nearest A-sublattice node.
    probe_targets = [
        (cx + R, cy,     cz),   # +x equator
        (cx,     cy + R, cz),   # +y equator
        (cx - R, cy,     cz),   # -x equator
        (cx,     cy - R, cz),   # -y equator
    ]
    probes = [find_nearest_A_site(lattice, t) for t in probe_targets]

    # Record all 4 ports of V_inc and V_ref for each probe — allows
    # multiple candidate phasor decompositions in post-analysis.
    V_inc_series = np.zeros((len(probes), n_steps, 4), dtype=float)
    V_ref_series = np.zeros((len(probes), n_steps, 4), dtype=float)

    # Also record a global energy trace as sanity check
    energy_trace = np.zeros(n_steps, dtype=float)

    for step in range(n_steps):
        lattice.step()
        for idx, (i, j, k) in enumerate(probes):
            V_inc_series[idx, step, :] = lattice.V_inc[i, j, k, :]
            V_ref_series[idx, step, :] = lattice.V_ref[i, j, k, :]
        energy_trace[step] = float(
            np.sum(lattice.V_inc ** 2) + np.sum(lattice.V_ref ** 2)
        )

    return {
        "probes": probes,
        "probe_targets": probe_targets,
        "V_inc": V_inc_series,       # shape (n_probes, n_steps, 4)
        "V_ref": V_ref_series,       # shape (n_probes, n_steps, 4)
        "energy_trace": energy_trace,
        "R_real": R,
        "r_real": r,
        "N": N,
        "n_steps": n_steps,
    }


def main():
    print("=" * 72)
    print("PHASOR TRAJECTORY TEST — L3 Phase-3 synthesis §5.1 verification")
    print("=" * 72)
    print("Pre-registered predictions:")
    print("  (A) Phase-space Golden Torus: R_phase/r_phase ≈ 2.618 (φ²)")
    print("  (B) Classical (2,3) / full Clifford: ≈ 2.0 or ≈ 2.27")
    print("  (C) Chaotic / dispersive: framing falsified")
    print()

    result = run_phasor_test(N=64, n_steps=400)

    print(f"Lattice: {result['N']}³, steps = {result['n_steps']}")
    print(f"Real-space seed: R = {result['R_real']}, r = {result['r_real']:.3f}")
    print(f"Golden-target R/r = φ² = {PHI**2:.4f}")
    print()
    print("Probe sites (A-sublattice):")
    for i, (target, probe) in enumerate(zip(result["probe_targets"], result["probes"])):
        print(f"  Probe {i}: target ≈ {tuple(round(t, 1) for t in target)}, "
              f"snapped to {tuple(int(x) for x in probe)}")
    print()

    # Discard initial transient (first 20% of steps)
    transient_cutoff = result["n_steps"] // 5
    print(f"Discarding first {transient_cutoff} steps as transient; "
          f"analyzing steps {transient_cutoff}..{result['n_steps']}")
    print()

    # Three candidate phase-space decompositions, analyzed in turn.
    #
    #  D1: (V_inc_port0, V_ref_port0)   — synthesis's literal framing
    #  D2: (V_inc_port0, V_inc_port2)   — port-quadrature across the
    #                                      ansatz's cos/sin split
    #  D3: (V_phys_port0, V_phys_port2) — physical-voltage quadrature
    #                                      where V_phys = V_inc + V_ref
    decompositions = [
        ("D1 (V_inc, V_ref) same port",
         lambda r, i: np.column_stack([r["V_inc"][i, transient_cutoff:, 0],
                                       r["V_ref"][i, transient_cutoff:, 0]])),
        ("D2 (V_inc_p0, V_inc_p2) quadrature",
         lambda r, i: np.column_stack([r["V_inc"][i, transient_cutoff:, 0],
                                       r["V_inc"][i, transient_cutoff:, 2]])),
        ("D3 (V_phys_p0, V_phys_p2) voltage quadrature",
         lambda r, i: np.column_stack([
             r["V_inc"][i, transient_cutoff:, 0] + r["V_ref"][i, transient_cutoff:, 0],
             r["V_inc"][i, transient_cutoff:, 2] + r["V_ref"][i, transient_cutoff:, 2]])),
    ]

    all_ratios = {}
    for label, extractor in decompositions:
        print(f"Decomposition {label}:")
        print(f"{'probe':>5s} {'x_rms':>12s} {'y_rms':>12s} "
              f"{'semi_major':>11s} {'semi_minor':>11s} {'ratio':>8s}")
        ratios = []
        for i in range(len(result["probes"])):
            traj = extractor(result, i)
            smaj, smin, rat = principal_axes(traj)
            ratios.append(rat)
            x_rms = np.sqrt(np.mean(traj[:, 0] ** 2))
            y_rms = np.sqrt(np.mean(traj[:, 1] ** 2))
            print(f"{i:5d} {x_rms:12.4e} {y_rms:12.4e} "
                  f"{smaj:11.4e} {smin:11.4e} {rat:8.3f}")
        print(f"  mean ratio = {np.mean(ratios):.3f}, "
              f"range = [{min(ratios):.3f}, {max(ratios):.3f}]")
        all_ratios[label] = ratios
        print()

    e_trace = result["energy_trace"]
    e_initial = e_trace[0]
    e_final = e_trace[-1]
    e_max = float(np.max(e_trace))
    e_min = float(np.min(e_trace))
    print(f"Energy sanity:")
    print(f"  initial = {e_initial:.4e}, final = {e_final:.4e}")
    print(f"  range   = [{e_min:.4e}, {e_max:.4e}]")
    print(f"  drift   = {(e_final - e_initial) / e_initial * 100:.2f}%")
    print()

    # Verdict against predictions, per decomposition
    print("=" * 72)
    print("VERDICTS per decomposition:")
    for label, ratios in all_ratios.items():
        mean_ratio = float(np.mean(ratios))
        if abs(mean_ratio - PHI ** 2) < 0.2:
            verdict = f"(A) Phase-space Golden Torus: ≈ φ² = {PHI**2:.3f}"
        elif abs(mean_ratio - 2.0) < 0.15:
            verdict = "(B) Classical (2,3) / full Clifford ≈ 2.0"
        elif abs(mean_ratio - 2.27) < 0.15:
            verdict = "(B') Matches real-space TLM R/r ≈ 2.27"
        elif mean_ratio > 20:
            verdict = "(C) Degenerate line — trajectory 1D"
        else:
            verdict = "(other) no pre-registered match"
        print(f"  {label}:\n      mean ratio = {mean_ratio:.3f} → {verdict}")
    print("=" * 72)

    # Save raw data for plotting / further analysis
    out_path = "/tmp/phasor_trajectory_test.npz"
    np.savez(
        out_path,
        V_inc=result["V_inc"],
        V_ref=result["V_ref"],
        energy_trace=result["energy_trace"],
        probes=np.array(result["probes"]),
        N=result["N"],
        n_steps=result["n_steps"],
        R_real=result["R_real"],
        r_real=result["r_real"],
    )
    print(f"Raw data saved: {out_path}")


if __name__ == "__main__":
    main()