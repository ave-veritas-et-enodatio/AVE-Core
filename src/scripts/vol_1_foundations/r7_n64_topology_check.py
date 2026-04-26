"""V-block N=64 GT_corpus topology check — concern #1 from auditor on commit b5ecc89.

Per [doc 74_ §7.1](../../research/L3_electron_soliton/74_r7_k4tlm_lctank_run_result.md):
the Mode I candidate at N=64 GT_corpus passes the frequency criterion (gap
0.45% < α/√2 = 0.73%), but the auditor flags this as load-bearing rather
than confirmatory — at N=64 the K4-TLM band density is high enough that
SOME mode lands within α tolerance is non-trivial probability.

V-block eigvec doesn't have a direct (2,3) winding number (V_inc is 4-port
scalar, not Cosserat ω vector). The native-defensible topology measure is
LOCALIZATION at the seeded shell:
    shell_energy / total_energy = fraction of |V_inc|² within ±r of shell

Interpretation:
    > 0.50: eigvec strongly concentrated at (2,3) shell — consistent with
            bound-state interpretation; supports Mode I candidate.
    0.10-0.50: eigvec partially localized — ambiguous, could be hybrid mode.
    < 0.10: eigvec spread uniformly — bulk mode, NOT (2,3) bound state.
            Mode I candidate framing collapses.

Reuses build_T_operator + helpers from r7_k4tlm_scattering_lctank.py.

Per Rule 10 "data first, methodology after": this topology check is post-run
methodology development based on empirical N=64 result. Not a new pre-reg.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np
from scipy.sparse.linalg import eigs

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))

from ave.topological.vacuum_engine import VacuumEngine3D

sys.path.insert(0, str(Path(__file__).resolve().parent))
from r7_k4tlm_scattering_lctank import (
    PHI_SQ, A26_AMP_SCALE, GT_PEAK_OMEGA, ALPHA, OMEGA_COMPTON,
    DT, TARGET_PHASE, PHASE_TOL_V,
    A26_GUARD_LOW, A26_GUARD_HIGH,
    seed_2_3_hedgehog, a26_guard,
    build_T_operator, get_active_sites,
)

N_LATTICE = 64
PML = 4
R_ANCHOR = 10.0
R_TARGET = R_ANCHOR
R_MINOR = R_ANCHOR / PHI_SQ  # ≈ 3.82

OUTPUT_JSON = Path(__file__).parent / "r7_n64_topology_check_results.json"


def shell_localization(eigvec, sites, N, R_anchor, r_minor):
    """Fraction of |V_inc|² concentrated at the seeded (2,3) shell.

    The shell is centered at radius R_anchor in the xy-plane (z=N/2),
    with thickness ±r_minor. Lattice center is at (N/2, N/2, N/2).
    """
    cx, cy, cz = (N - 1) / 2.0, (N - 1) / 2.0, (N - 1) / 2.0

    total_energy = 0.0
    shell_energy = 0.0
    bulk_energy = 0.0

    # eigvec is shape (4*N_active,) = 4 ports per active site
    # We integrate |V_inc|² per site over all 4 ports
    for (x, y, z), i_global in sites.items():
        # Per-site energy: sum of |V_inc[port]|² over 4 ports
        site_energy = sum(abs(eigvec[4 * i_global + p]) ** 2 for p in range(4))
        total_energy += site_energy

        # Site distance from torus axis (z-axis through center)
        rho_xy = np.sqrt((x - cx) ** 2 + (y - cy) ** 2)
        rho_tube = np.sqrt((rho_xy - R_anchor) ** 2 + (z - cz) ** 2)

        if rho_tube <= r_minor:
            shell_energy += site_energy
        else:
            bulk_energy += site_energy

    if total_energy < 1e-30:
        return None
    return {
        "total_energy": float(total_energy),
        "shell_energy": float(shell_energy),
        "bulk_energy": float(bulk_energy),
        "shell_fraction": float(shell_energy / total_energy),
    }


def main():
    print("=" * 78, flush=True)
    print(f"  V-block N={N_LATTICE} GT_corpus topology check (concern #1)")
    print("=" * 78, flush=True)
    print(f"  Target phase ω_C·dt = {TARGET_PHASE:.4f} rad")
    print(f"  Shell geometry: R={R_TARGET}, r={R_MINOR:.4f}")
    print()

    engine = VacuumEngine3D.from_args(
        N=N_LATTICE, pml=PML, temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,
        enable_cosserat_self_terms=True,
    )

    seed_2_3_hedgehog(engine, R_TARGET, R_MINOR)
    peak = a26_guard(engine, "GT_corpus")
    print(f"  A26 guard OK (peak |ω|={peak:.4f})")
    print()

    print(f"  Building T operator at N={N_LATTICE}...", flush=True)
    t0 = time.time()
    T, sites, n_active = build_T_operator(engine)
    print(f"    T built in {time.time() - t0:.1f}s; dim={T.shape[0]}, nnz={T.nnz}")

    sigma = complex(np.cos(TARGET_PHASE), np.sin(TARGET_PHASE))
    print(f"  Eigsolve at sigma=exp(i·{TARGET_PHASE:.4f}), k=10...", flush=True)
    t1 = time.time()
    eigvals, eigvecs = eigs(T, k=10, sigma=sigma, which='LM', tol=1e-6, maxiter=2000)
    print(f"    Eigsolve: {time.time() - t1:.1f}s, {len(eigvals)} eigenvalues")
    print()

    # Find closest eigenvalue to target phase
    phases = np.angle(eigvals)
    diffs = np.minimum(np.abs(phases - TARGET_PHASE), np.abs(phases + TARGET_PHASE))
    idx = int(np.argmin(diffs))
    closest_phase = float(phases[idx])
    closest_gap = float(diffs[idx])

    print(f"  Closest eigenvalue at phase {closest_phase:.6f} rad")
    print(f"    gap to ω_C·dt: {closest_gap:.4e} rad ({100*closest_gap/TARGET_PHASE:.4f}%)")
    print(f"    PASS tolerance: {PHASE_TOL_V:.4e}; "
          f"{'PASS' if closest_gap < PHASE_TOL_V else 'FAIL'}")
    print()

    # Compute shell localization on the closest eigvec
    eigvec = eigvecs[:, idx]
    print(f"  Computing shell localization for closest eigvec...")
    loc = shell_localization(eigvec, sites, N_LATTICE, R_TARGET, R_MINOR)
    if loc is None:
        print(f"    ERROR: zero eigvec energy")
        return None

    print(f"    Total energy:  {loc['total_energy']:.4e}")
    print(f"    Shell energy:  {loc['shell_energy']:.4e}")
    print(f"    Bulk energy:   {loc['bulk_energy']:.4e}")
    print(f"    Shell fraction: {loc['shell_fraction']:.4f}")
    print()

    # Topology adjudication
    sf = loc['shell_fraction']
    print("=" * 78, flush=True)
    print("  Topology adjudication")
    print("=" * 78, flush=True)
    if sf > 0.50:
        verdict = (f"STRONG SHELL LOCALIZATION (fraction {sf:.3f} > 0.50): "
                   "eigvec concentrated at (2,3) shell. Consistent with bound-state "
                   "interpretation. Mode I candidate framing supported.")
    elif sf > 0.10:
        verdict = (f"PARTIAL LOCALIZATION (fraction {sf:.3f}): ambiguous. "
                   "Could be hybrid bulk-shell mode. Mode I candidate framing "
                   "neither confirmed nor falsified by topology alone.")
    else:
        verdict = (f"WEAK SHELL LOCALIZATION (fraction {sf:.3f} < 0.10): "
                   "eigvec is spread uniformly across lattice (bulk mode). "
                   "NOT a (2,3) bound state. Mode I candidate framing collapses.")
    print(f"  {verdict}")
    print()

    # For comparison, what fraction of LATTICE VOLUME is in the shell?
    # Approx: shell volume ≈ 4π²·R·r ≈ 4·π²·10·3.82 ≈ 1509 (continuous estimate)
    # Cubic lattice volume = N³ = 64³ = 262K cells, half are K4-active = ~131K sites
    # Bulk-uniform expectation: shell_fraction ≈ 1509/262K = 0.6%
    print(f"  Reference: bulk-uniform expectation ≈ shell_volume/lattice_volume")
    print(f"             ≈ 4π²·R·r / N³ ≈ {4*np.pi**2*R_TARGET*R_MINOR / N_LATTICE**3:.4f}")
    print(f"  Observed shell fraction is {sf:.4f} — "
          f"{sf / (4*np.pi**2*R_TARGET*R_MINOR / N_LATTICE**3):.1f}× bulk-uniform expectation")

    payload = {
        "context": "doc 74_ §7.1 concern #1 — V-block N=64 GT_corpus topology check",
        "N": N_LATTICE, "R_anchor": R_TARGET, "r_minor": R_MINOR,
        "closest_eigenvalue_phase": closest_phase,
        "gap_to_omega_C_dt": closest_gap,
        "PASS_at_frequency_only": closest_gap < PHASE_TOL_V,
        "shell_fraction": sf,
        "shell_energy": loc['shell_energy'],
        "bulk_energy": loc['bulk_energy'],
        "total_energy": loc['total_energy'],
        "bulk_uniform_expectation": float(4 * np.pi**2 * R_TARGET * R_MINOR / N_LATTICE**3),
        "localization_factor_vs_bulk": float(sf / (4 * np.pi**2 * R_TARGET * R_MINOR / N_LATTICE**3)),
        "verdict": verdict,
    }
    OUTPUT_JSON.write_text(json.dumps(payload, indent=2, default=str))
    print(f"\n  Result: {OUTPUT_JSON}")
    return payload


if __name__ == "__main__":
    main()
