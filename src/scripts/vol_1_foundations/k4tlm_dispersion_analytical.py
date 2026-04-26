"""K4-TLM dispersion analytical sanity check at uniform z=1.

Per doc 74_ §4 follow-up + auditor concern #2: verify that the eigenvalue
cluster at phase ω·dt ≈ 0.7158 rad observed in the multi-seed sweep
(`r7_k4tlm_scattering_lctank.py`) sits on the canonical K4-TLM dispersion
at uniform impedance. If yes → cluster is real lattice physics; Mode III
finding for the V-block stands. If no → third operator-construction issue
lurking; halt for re-audit.

Method:
  At uniform z=1, the K4-TLM scatter matrix is S = 0.5·11ᵀ - I (independent
  of port). Per Bloch theorem on the bipartite diamond lattice, the
  transmission operator factorizes per wavevector k:
      T(k) = D(k) · S
  where D(k) = diag(exp(i·k·PORTS[p])) for p ∈ {0,1,2,3}, and PORTS are the
  tetrahedral A→B offsets.

  T(k) is a 4×4 unitary at each k. Eigenvalues λ_n(k) = exp(i·θ_n(k)) give
  the discrete K4-TLM dispersion phases θ_n(k) for the 4 bands.

  At N=32 with periodic BC, k-vectors are k_n = (2π/N)·(n_x, n_y, n_z) for
  n_i ∈ {0..N-1}, sampled on the K4 active-site sublattice.

References:
  - doc 73_ §2 (operator construction)
  - doc 74_ §4.4 (Mode III result + 0.7158 cluster framing)
  - k4_tlm.py:36-65 (build_scattering_matrix at z=1)
  - k4_tlm.py:348-426 (_connect_all port shifts)

Usage:
  python k4tlm_dispersion_analytical.py
"""
from __future__ import annotations

import sys
import json
from pathlib import Path

import numpy as np

PORTS = np.array([
    [+1, +1, +1],
    [+1, -1, -1],
    [-1, +1, -1],
    [-1, -1, +1],
], dtype=int)

# Universal scatter at z=1: S_pq = 0.5 - δ_pq
S_UNIFORM = 0.5 * np.ones((4, 4)) - np.eye(4)

# Target phase from the multi-seed run
TARGET_PHASE_OMEGA_C = 1.0 / np.sqrt(2.0)  # ω_C·dt = 1/√2 ≈ 0.7071 rad
OBSERVED_CLUSTER_PHASE = 0.71574  # GT_corpus closest mode phase (doc 74_ §2)
ALPHA = 1.0 / 137.036
PASS_TOL = ALPHA * TARGET_PHASE_OMEGA_C  # ≈ 0.00516 rad


def T_at_k(k: np.ndarray) -> np.ndarray:
    """T(k) = D(k) · S where D(k)_pp = exp(i·k·PORTS[p])."""
    phases = np.array([np.exp(1j * np.dot(k, p)) for p in PORTS])
    return np.diag(phases) @ S_UNIFORM


def discrete_k_grid_N(N: int) -> list[np.ndarray]:
    """Discrete wavevectors at periodic BC of N×N×N lattice.

    For K4 active sites (all-even ∪ all-odd), the effective Brillouin zone
    is half-size; k components are 2π·n/N for n in {0,...,N-1}.
    """
    grid = []
    for nx in range(N):
        for ny in range(N):
            for nz in range(N):
                k = (2.0 * np.pi / N) * np.array([nx, ny, nz], dtype=float)
                grid.append(k)
    return grid


def collect_dispersion(N: int = 32) -> tuple[np.ndarray, np.ndarray]:
    """Compute all eigenvalue phases at all k-vectors in N=N grid.

    Returns:
        all_phases: shape (N³ × 4,) — 4 phases per k-vector
        all_ks: shape (N³, 3) — the wavevectors
    """
    ks = discrete_k_grid_N(N)
    n_k = len(ks)
    all_phases = np.zeros(n_k * 4, dtype=float)
    for i, k in enumerate(ks):
        T = T_at_k(k)
        eigvals = np.linalg.eigvals(T)  # 4 complex eigenvalues
        phases = np.angle(eigvals)  # in [-π, π]
        all_phases[4 * i: 4 * (i + 1)] = phases
    return all_phases, np.array(ks)


def main() -> dict:
    print("=" * 70)
    print("  K4-TLM analytical dispersion at uniform z=1")
    print("=" * 70)
    print(f"  Target phase ω_C·dt = {TARGET_PHASE_OMEGA_C:.6f} rad")
    print(f"  Observed cluster phase = {OBSERVED_CLUSTER_PHASE:.6f} rad")
    print(f"  α/√2 PASS tolerance = ±{PASS_TOL:.6f} rad")
    print()

    N = 32
    print(f"  Computing T(k) eigenvalues at all {N}³ = {N**3} k-vectors...")
    phases, ks = collect_dispersion(N)
    print(f"  Total modes computed: {len(phases)}")
    print()

    # Statistics
    print("  Phase distribution (full circle [-π, π]):")
    for q in [0.0, 0.25, 0.5, 0.75, 1.0]:
        print(f"    q={q:.2f}: phase = {np.quantile(phases, q):+.4f} rad")
    print()

    # Density near observed cluster
    cluster_window = 0.01  # rad
    near_target = np.abs(phases - TARGET_PHASE_OMEGA_C) < cluster_window
    near_observed = np.abs(phases - OBSERVED_CLUSTER_PHASE) < cluster_window
    print(f"  Modes within ±{cluster_window} rad of target ω_C·dt = {TARGET_PHASE_OMEGA_C:.4f}: "
          f"{near_target.sum()} of {len(phases)}")
    print(f"  Modes within ±{cluster_window} rad of observed cluster {OBSERVED_CLUSTER_PHASE:.4f}: "
          f"{near_observed.sum()} of {len(phases)}")
    print()

    # Mode density histogram
    print("  Histogram of phase density (positive half [0, π]):")
    bins = np.linspace(0, np.pi, 21)
    pos_phases = phases[phases > 0]
    hist, _ = np.histogram(pos_phases, bins=bins)
    max_count = hist.max() if len(hist) > 0 else 1
    for i in range(len(bins) - 1):
        bar = "█" * int(40 * hist[i] / max_count)
        marker = ""
        if bins[i] <= TARGET_PHASE_OMEGA_C < bins[i + 1]:
            marker += "  ← target ω_C·dt"
        if bins[i] <= OBSERVED_CLUSTER_PHASE < bins[i + 1]:
            marker += "  ← observed cluster"
        print(f"    {bins[i]:5.3f} - {bins[i+1]:5.3f} rad: {hist[i]:5d}  {bar}{marker}")
    print()

    # Find phase nearest target / observed
    diffs_target = np.abs(phases - TARGET_PHASE_OMEGA_C)
    idx_nearest_target = int(np.argmin(diffs_target))
    diffs_observed = np.abs(phases - OBSERVED_CLUSTER_PHASE)
    idx_nearest_observed = int(np.argmin(diffs_observed))

    nearest_target_phase = float(phases[idx_nearest_target])
    nearest_observed_phase = float(phases[idx_nearest_observed])
    nearest_target_diff = float(diffs_target[idx_nearest_target])
    nearest_observed_diff = float(diffs_observed[idx_nearest_observed])

    print(f"  Nearest analytical mode to target ω_C·dt = {TARGET_PHASE_OMEGA_C:.6f}:")
    print(f"    phase = {nearest_target_phase:.10f} rad")
    print(f"    diff  = {nearest_target_diff:.6e} rad ({100*nearest_target_diff/TARGET_PHASE_OMEGA_C:.4f}%)")
    print(f"    PASS tolerance: |diff| < {PASS_TOL:.6e}; ",
          "PASS" if nearest_target_diff < PASS_TOL else "FAIL (no analytical mode at ω_C·dt)")
    print()
    print(f"  Nearest analytical mode to observed cluster {OBSERVED_CLUSTER_PHASE:.6f}:")
    print(f"    phase = {nearest_observed_phase:.10f} rad")
    print(f"    diff  = {nearest_observed_diff:.6e} rad")
    if nearest_observed_diff < 1e-6:
        print(f"    → analytical dispersion DOES contain phase {OBSERVED_CLUSTER_PHASE} (or very close)")
    elif nearest_observed_diff < 1e-3:
        print(f"    → analytical dispersion is near phase {OBSERVED_CLUSTER_PHASE}")
    else:
        print(f"    → analytical dispersion is FAR from phase {OBSERVED_CLUSTER_PHASE} — possible bug")

    # Verdict
    print()
    print("=" * 70)
    print("  VERDICT")
    print("=" * 70)
    cluster_match = nearest_observed_diff < 1e-3
    if cluster_match:
        print(f"  Observed cluster at {OBSERVED_CLUSTER_PHASE:.4f} rad sits on the canonical")
        print(f"  K4-TLM dispersion at uniform z=1 (analytical match within {nearest_observed_diff:.2e} rad).")
        print(f"  V-block Mode III result is real K4-TLM physics, not operator bug.")
    else:
        print(f"  Observed cluster at {OBSERVED_CLUSTER_PHASE:.4f} rad does NOT match the")
        print(f"  analytical K4-TLM dispersion (nearest analytical phase {nearest_observed_phase:.4f}")
        print(f"  rad, off by {nearest_observed_diff:.2e}).")
        print(f"  Possible third operator-construction issue. HALT for re-audit.")

    pass_at_target = nearest_target_diff < PASS_TOL
    if pass_at_target:
        print()
        print(f"  ALSO: analytical K4-TLM dispersion at z=1 contains a mode within")
        print(f"  PASS tolerance of ω_C·dt. The seeded multi-seed run's failure to find")
        print(f"  it would itself be the operator bug.")
    else:
        print()
        print(f"  AND: analytical K4-TLM dispersion at z=1 does NOT contain a mode within")
        print(f"  PASS tolerance ({PASS_TOL:.4e}) of ω_C·dt. The closest analytical mode is")
        print(f"  {nearest_target_diff:.4e} rad off — consistent with the V-block sweep's")
        print(f"  closest-mode finding at 1.22%. Mode III stands at uniform z=1 baseline.")

    return {
        "doc": "doc 73_ §2 + doc 74_ §4 follow-up (auditor concern #2)",
        "N": N,
        "n_modes_total": int(len(phases)),
        "target_phase": TARGET_PHASE_OMEGA_C,
        "observed_cluster_phase": OBSERVED_CLUSTER_PHASE,
        "pass_tolerance_rad": PASS_TOL,
        "nearest_target_phase": nearest_target_phase,
        "nearest_target_diff_rad": nearest_target_diff,
        "nearest_observed_phase": nearest_observed_phase,
        "nearest_observed_diff_rad": nearest_observed_diff,
        "cluster_on_canonical_dispersion": bool(nearest_observed_diff < 1e-3),
        "pass_at_target": bool(pass_at_target),
        "modes_within_001rad_of_target": int(near_target.sum()),
        "modes_within_001rad_of_observed": int(near_observed.sum()),
    }


if __name__ == "__main__":
    result = main()
    out_path = Path(__file__).parent / "k4tlm_dispersion_analytical_result.json"
    out_path.write_text(json.dumps(result, indent=2, default=str))
    print(f"\n  Result written to {out_path}")
