"""
L3 Phase-3 convergence study — does the TLM converge to the analytical
prediction in the continuum limit?

Per the audit at `research/_archive/L3_electron_soliton/21_first_principles_audit.md`
and the dialogue thereafter: the TLM at finite resolution is a discrete-
lattice approximation of the continuum-limit Golden Torus. The right
question isn't "does 96³ give α⁻¹ = 137" (it doesn't) but "does the
discrete-lattice approximation CONVERGE to the analytical prediction
as N → ∞?"

This is the standard discrete-physics validation method (lattice QCD,
discrete elasticity, etc.).

Protocol:
  1. Run TLM at increasing lattice resolutions N ∈ {24, 48, 96}
     - Hold the GEOMETRY fixed at Golden-Torus proportions
       (R = N/4, r = R/φ², so R/r = φ² = 2.618 by construction)
     - Initialize with (2,3) Cosserat-phasor ansatz
     - Evolve with op3_bond_reflection enabled
     - Extract (R_rms, r_rms) from time-RMS V_phys² envelope
  2. Compute α⁻¹ at each N from extracted (R_rms, r_rms) via Ch 8 formula
  3. Plot α⁻¹(N) vs 1/N (continuum-limit extrapolation)
  4. Linear extrapolate 1/N → 0 to get continuum-limit prediction
  5. Compare to ALPHA_COLD_INV = 137.036

Pre-registered prediction:
  - If trend extrapolates to 137 ± 5%: convergent — supports analytical theorem
  - If trend extrapolates elsewhere: framework gap revealed
  - If no clear trend: discrete-lattice dynamics inconsistent with continuum

This is the AVE-NATIVE validation: lattice approximation → continuum limit.
NOT a single-resolution match. NOT a Y-matrix. NOT a chirality extraction.
Just convergence of α⁻¹.
"""

import numpy as np
import time

from ave.core.constants import V_YIELD, ALPHA_COLD_INV
from scripts.vol_1_foundations.tlm_electron_soliton_eigenmode import (
    PHI,
    run_tlm_electron,
    extract_alpha_inverse,
)


def run_at_resolution(N: int, n_steps: int = 200, amp_frac: float = 0.5,
                      verbose: bool = True) -> dict:
    """Run TLM at lattice resolution N with Golden-Torus-proportioned geometry."""
    PHI_SQ = PHI ** 2
    R_target = N / 4.0           # ~quarter of lattice
    r_target = R_target / PHI_SQ  # Golden-Torus proportions
    amp = amp_frac * float(V_YIELD)

    if verbose:
        print(f"\n--- N = {N}³ ---")
        print(f"  R_target = {R_target:.3f}, r_target = {r_target:.3f}, "
              f"R/r = {PHI_SQ:.4f}")
        print(f"  Amplitude = {amp:.3e} ({amp_frac:.2f} × V_YIELD)")
        print(f"  n_steps = {n_steps}")

    t0 = time.time()
    result = run_tlm_electron(
        N=N, R=R_target, r=r_target, n_steps=n_steps,
        amplitude=amp, pml_thickness=0,
        sample_every=n_steps + 1,  # suppress per-step output
        verbose=False, op3_bond_reflection=True,
        rms_avg_last_n=max(50, n_steps // 3),
    )
    elapsed = time.time() - t0

    R_rms = result['R_rms']
    r_rms = result['r_rms']
    Rr_ratio = R_rms / max(r_rms, 1e-9)
    alpha_dict = extract_alpha_inverse(R_rms, r_rms, c=3)
    alpha_inv = alpha_dict['alpha_inv'] if alpha_dict['valid'] else float('nan')
    R_norm = R_rms / N  # geometry normalized to lattice (should converge to phi/2)

    if verbose:
        print(f"  Elapsed: {elapsed:.1f}s")
        print(f"  Extracted: R_rms={R_rms:.3f}, r_rms={r_rms:.3f}, "
              f"R/r={Rr_ratio:.4f}")
        print(f"  α⁻¹ = {alpha_inv:.4f} "
              f"(target {ALPHA_COLD_INV:.4f}, "
              f"err = {abs(alpha_inv - ALPHA_COLD_INV)/ALPHA_COLD_INV*100:.2f}%)")

    return {
        'N': N,
        'R_target': R_target, 'r_target': r_target,
        'R_rms': R_rms, 'r_rms': r_rms,
        'R_over_r': Rr_ratio,
        'R_norm': R_norm,
        'alpha_inv': alpha_inv,
        'amp': amp,
        'elapsed': elapsed,
    }


def linear_extrapolate(N_list, alpha_list):
    """Linear fit α⁻¹ = A + B/N, return A (continuum-limit α⁻¹).

    Returns (A, B, R²) where A is the 1/N → 0 extrapolation.
    """
    x = np.array([1.0 / N for N in N_list])
    y = np.array(alpha_list)
    # Drop NaNs
    mask = ~np.isnan(y)
    if mask.sum() < 2:
        return float('nan'), float('nan'), 0.0
    x_clean = x[mask]
    y_clean = y[mask]
    # Linear fit y = A + B*x
    coef = np.polyfit(x_clean, y_clean, 1)
    B, A = coef[0], coef[1]
    y_pred = A + B * x_clean
    ss_res = np.sum((y_clean - y_pred) ** 2)
    ss_tot = np.sum((y_clean - np.mean(y_clean)) ** 2)
    r_sq = 1.0 - ss_res / max(ss_tot, 1e-30)
    return A, B, r_sq


def main():
    print("=" * 78)
    print("L3 Phase-3 Convergence Study — does TLM α⁻¹ converge to 137?")
    print("=" * 78)
    print(f"\nTarget (continuum limit): α⁻¹ = ALPHA_COLD_INV = {ALPHA_COLD_INV:.4f}")
    print("Pre-registered: extrapolation to 1/N→0 within 5% of 137 = success.")

    # Convergence-study sequence
    N_values = [24, 48, 96]
    n_steps_per_N = {24: 100, 48: 150, 96: 200}

    results = []
    for N in N_values:
        res = run_at_resolution(N=N, n_steps=n_steps_per_N[N], amp_frac=0.5,
                                verbose=True)
        results.append(res)

    # Tabulate
    print("\n" + "=" * 78)
    print("CONVERGENCE TABLE")
    print("=" * 78)
    print(f"{'N':<6}{'1/N':<10}{'R_rms':<10}{'r_rms':<10}{'R/r':<10}"
          f"{'R/N':<10}{'α⁻¹':<14}{'err %':<10}")
    print("-" * 78)
    for r in results:
        err_pct = (abs(r['alpha_inv'] - ALPHA_COLD_INV) / ALPHA_COLD_INV * 100
                   if not np.isnan(r['alpha_inv']) else float('nan'))
        print(f"{r['N']:<6}{1.0/r['N']:<10.4f}{r['R_rms']:<10.3f}"
              f"{r['r_rms']:<10.3f}{r['R_over_r']:<10.4f}"
              f"{r['R_norm']:<10.4f}{r['alpha_inv']:<14.4f}{err_pct:<10.2f}")

    # Continuum-limit extrapolation
    N_list = [r['N'] for r in results]
    alpha_list = [r['alpha_inv'] for r in results]
    A, B, r_sq = linear_extrapolate(N_list, alpha_list)

    print("\n" + "=" * 78)
    print("CONTINUUM-LIMIT EXTRAPOLATION (linear: α⁻¹ = A + B/N)")
    print("=" * 78)
    print(f"  A (1/N → 0 extrapolation) = {A:.4f}")
    print(f"  B (coefficient of 1/N)     = {B:.4f}")
    print(f"  R² (fit quality)           = {r_sq:.4f}")
    print(f"  Target α⁻¹                 = {ALPHA_COLD_INV:.4f}")
    extrap_err = (abs(A - ALPHA_COLD_INV) / ALPHA_COLD_INV * 100
                  if not np.isnan(A) else float('nan'))
    print(f"  |A − target| / target      = {extrap_err:.2f}%")

    # R/r convergence
    Rr_list = [r['R_over_r'] for r in results]
    A_Rr, B_Rr, r_sq_Rr = linear_extrapolate(N_list, Rr_list)
    PHI_SQ = PHI ** 2
    extrap_Rr_err = abs(A_Rr - PHI_SQ) / PHI_SQ * 100
    print(f"\n  R/r convergence:")
    print(f"    A (1/N → 0)              = {A_Rr:.4f}")
    print(f"    Target (φ²)              = {PHI_SQ:.4f}")
    print(f"    err                      = {extrap_Rr_err:.2f}%")

    # Verdict
    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    if not np.isnan(A) and abs(A - ALPHA_COLD_INV) / ALPHA_COLD_INV < 0.05:
        print(f"  PASS: α⁻¹ extrapolates to {A:.3f}, within 5% of {ALPHA_COLD_INV:.3f}")
        print("  Discrete-lattice TLM is consistent with continuum-limit theorem.")
    elif not np.isnan(A) and r_sq > 0.9:
        print(f"  CLEAN TREND BUT WRONG VALUE: α⁻¹ → {A:.3f}, target {ALPHA_COLD_INV:.3f}")
        print(f"  Trend is clean (R² = {r_sq:.3f}) but extrapolation misses by "
              f"{extrap_err:.1f}%.")
        print("  Suggests systematic discrete-lattice correction OR theorem gap.")
    else:
        print(f"  NO CLEAN CONVERGENCE: A = {A:.3f}, R² = {r_sq:.3f}")
        print("  TLM doesn't show clear approach to continuum limit at tested N.")
        print("  Either need higher N or fundamental dynamics issue.")

    # Output for log
    print("\n" + "=" * 78)
    print("PROMPT FOR PREDICTION-LOG ENTRY (paste into handoff §2.4):")
    print("=" * 78)
    for r in results:
        print(f"  N={r['N']}: α⁻¹ = {r['alpha_inv']:.3f}, R/r = {r['R_over_r']:.3f}")
    print(f"  Extrapolation 1/N → 0: α⁻¹ → {A:.3f}, R/r → {A_Rr:.4f} "
          f"(target φ² = {PHI_SQ:.4f})")


if __name__ == "__main__":
    main()
