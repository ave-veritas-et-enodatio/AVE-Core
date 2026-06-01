"""FT-b — STRESS-TEST of the Outcome-C verdict (anti-confirmation-bias).

The Step-1 finding (per-axis kernel load is q-FLAT) could MISS a q-dependence
that lives in the FULL Route-B correlation ⟨(S_d − S_q)·τ_zx⟩ — the actual C_2
mechanism — rather than in the per-axis time-average. doc 115 §3 + the saliency
leaf say the saliency IS this correlation's response to the d/q split.

Two stress-tests that could OVERTURN Outcome C (→ A or B):

  TEST I — does the correlation-based saliency shift scale with q?
    For each q ∈ {1,3,5,7}, build the (2,q) Route-B currents, and ask: at what
    saliency δ does C_2(q,δ) hit its q-specific 'symmetric-budget' structure?
    More directly: compute dC_2/dδ at δ=0 for each q. If the SENSITIVITY of the
    correlation to δ scales with q, there IS a q-dependent mechanism and the
    per-axis flatness was the wrong probe.

  TEST II — does the kernel ASYMMETRY (S_d − S_q), not the per-axis load, carry q?
    The saliency shifts A_q² relative to A_d². The mechanism that 'wants' a
    nonzero δ is whatever makes the d-axis and q-axis kernel responses differ.
    Compute ⟨S_d − S_q⟩ and ⟨(S_d − S_q)·τ_zx⟩ at the SYMMETRIC budget for each
    q. If these are q-flat, the kernel has no q-preference and Outcome C holds.

If EITHER test shows clean q-linear structure that selects δ=−3α/2, the verdict
flips. If both confirm q-flatness / no-selection, Outcome C is robust.

Run: python3 research/2026-05-31_FT-b-saliency-derivability_stresstest.py
"""

from math import pi
import numpy as np

ALPHA = 7.2973525693e-3
TWO_PI_ALPHA = 2.0 * pi * ALPHA


def kernel_S(A_sq):
    return np.sqrt(np.clip(1.0 - A_sq, 0.0, 1.0))


def route_b_correlation(q, delta, Nt=2_000_000, tau_retard=1.0):
    """Full Route-B correlation ⟨(S_d − S_q)·τ_zx⟩ for the (2,q) currents with
    saliency δ. Generalizes q_g19_alpha_saliency_sweep.py from q=3 to arbitrary q.
    d-axis fixed at n_d=2 (bipartite); q-axis at n_q=q.
    """
    t = np.linspace(0.0, 2.0 * pi, Nt, endpoint=False)
    dt = t[1] - t[0]

    Id = np.cos(2.0 * t)
    Iq = np.sin(q * t)

    A_d_peak_sq = (1.0 + delta) * TWO_PI_ALPHA
    A_q_peak_sq = (1.0 - delta) * TWO_PI_ALPHA

    S_d = kernel_S(A_d_peak_sq * Id**2)
    S_q = kernel_S(A_q_peak_sq * Iq**2)
    kernel_diff = S_d - S_q

    # dV²/dt with V² = Id² + Iq²; analytic derivative
    # d/dt[cos²(2t)] = -2·sin(4t); d/dt[sin²(qt)] = q·sin(2qt)
    dV2_dt = -2.0 * np.sin(4.0 * t) + q * np.sin(2.0 * q * t)
    shift_idx = int(np.round(tau_retard / dt)) % Nt
    tau_zx = -np.roll(dV2_dt, shift_idx)

    return np.mean(kernel_diff * tau_zx)


def C2(corr):
    return (2.0 / (pi * ALPHA)) * corr


def test_I_sensitivity():
    print("=" * 78)
    print("TEST I — does dC_2/dδ (correlation sensitivity to saliency) scale with q?")
    print("=" * 78)
    print("  If the correlation's response to δ scales with q, a q-dependent")
    print("  mechanism exists and Step-1 per-axis flatness was the wrong probe.")
    print()
    print(f"  {'q':>3} {'C_2(δ=0)':>14} {'dC_2/dδ |_0':>16} {'δ for C_2=PDG':>16}")
    print("  " + "-" * 60)
    eps = 1e-4
    target = -0.328479
    for q in [1, 3, 5, 7]:
        c0 = C2(route_b_correlation(q, 0.0))
        cp = C2(route_b_correlation(q, +eps))
        cm = C2(route_b_correlation(q, -eps))
        dC2_ddelta = (cp - cm) / (2 * eps)
        # δ that would bring THIS q's C_2 to the PDG target (local-linear est.)
        delta_for_pdg = (target - c0) / dC2_ddelta if abs(dC2_ddelta) > 1e-9 else float("nan")
        print(f"  {q:>3} {c0:>14.6f} {dC2_ddelta:>16.4f} {delta_for_pdg:>16.6f}")
    print()
    print("  INTERPRETATION: the q=3 row reproduces the canonical bisection")
    print("  (C_2(0)=−0.342, δ*≈−0.0109). Read whether dC_2/dδ or δ_for_PDG")
    print("  scales LINEARLY in q. If δ_for_PDG ∝ q (i.e. δ_for_PDG(q)/q is")
    print("  constant ≈ −α/2), the correlation SELECTS the linear law and")
    print("  Outcome flips toward A. If δ_for_PDG does NOT track −qα/2, the")
    print("  match at q=3 is a coincidence of that single q.")
    print()
    # Explicit linear-law test
    print("  LINEAR-LAW TEST: is δ_for_PDG(q) ≈ −q·α/2 ?")
    print(f"  {'q':>3} {'δ_for_PDG':>14} {'−q·α/2':>14} {'ratio':>10}")
    for q in [1, 3, 5, 7]:
        c0 = C2(route_b_correlation(q, 0.0))
        cp = C2(route_b_correlation(q, +eps))
        cm = C2(route_b_correlation(q, -eps))
        dC2_ddelta = (cp - cm) / (2 * eps)
        delta_for_pdg = (target - c0) / dC2_ddelta if abs(dC2_ddelta) > 1e-9 else float("nan")
        linear_law = -q * ALPHA / 2.0
        ratio = delta_for_pdg / linear_law if abs(linear_law) > 1e-12 else float("nan")
        print(f"  {q:>3} {delta_for_pdg:>14.6f} {linear_law:>14.6f} {ratio:>10.4f}")
    print()


def test_II_kernel_asymmetry():
    print("=" * 78)
    print("TEST II — does the kernel ASYMMETRY ⟨S_d−S_q⟩ carry q at symmetric budget?")
    print("=" * 78)
    print("  The mechanism that 'wants' nonzero δ is whatever makes the d-axis and")
    print("  q-axis kernel responses DIFFER. If ⟨S_d−S_q⟩ and the correlation are")
    print("  q-flat at δ=0, the kernel has no intrinsic q-preference → Outcome C.")
    print()
    Nt = 2_000_000
    t = np.linspace(0.0, 2.0 * pi, Nt, endpoint=False)
    Id = np.cos(2.0 * t)
    S_d = kernel_S(TWO_PI_ALPHA * Id**2)
    print(f"  d-axis (n_d=2) ⟨1−S_d⟩ = {np.mean(1.0 - S_d):.10e}")
    print()
    print(f"  {'q':>3} {'⟨1−S_q⟩':>18} {'⟨S_d−S_q⟩':>18} {'corr⟨(S_d−S_q)τ⟩':>20}")
    print("  " + "-" * 64)
    for q in [1, 3, 5, 7]:
        Iq = np.sin(q * t)
        S_q = kernel_S(TWO_PI_ALPHA * Iq**2)
        mean_1mSq = np.mean(1.0 - S_q)
        mean_diff = np.mean(S_d - S_q)
        corr = route_b_correlation(q, 0.0, Nt=Nt)
        print(f"  {q:>3} {mean_1mSq:>18.10e} {mean_diff:>18.6e} {corr:>20.6e}")
    print()
    print("  READ: ⟨1−S_q⟩ is q-flat (= d-axis value), so ⟨S_d−S_q⟩ ≈ 0 at the")
    print("  symmetric budget for ALL q — the kernel has NO intrinsic d-vs-q")
    print("  preference and NO q-scaling of that (non)preference. The nonzero")
    print("  CORRELATION comes from the RETARDED τ_zx phase structure (dark wake),")
    print("  not from a kernel q-asymmetry. Whether THAT correlation's δ-response")
    print("  is q-linear is decided by Test I.")
    print()


def main():
    print()
    print("#" * 78)
    print("# FT-b STRESS-TEST — can Outcome C be overturned to A/B?")
    print("#" * 78)
    print()
    test_II_kernel_asymmetry()
    test_I_sensitivity()
    print("=" * 78)
    print("STRESS-TEST VERDICT")
    print("=" * 78)
    print("""
  Read the Test-I 'LINEAR-LAW TEST' table:
    - If δ_for_PDG(q)/(−qα/2) ≈ 1.0 for ALL q ∈ {1,3,5,7}: the correlation
      mechanism SELECTS the linear law across the family → Outcome A/B, verdict
      OVERTURNED. The linearity would be a property of the Route-B correlation,
      not an inserted postulate.
    - If the ratio is ≈ 1.0 ONLY at q=3 and drifts for other q: the q=3 match is
      a single-point coincidence → Outcome C CONFIRMED.
  (Numerical readout printed above is the decider — do not pre-judge.)
""")


if __name__ == "__main__":
    main()
