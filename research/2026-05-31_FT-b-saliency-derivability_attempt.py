"""FT-b saliency-derivability — the derivation attempt.

PREREG (FROZEN c38d2b7e):
  research/2026-05-31_FT-b-saliency-derivability_prereg.md

QUESTION (and only this): can the n_q-LINEAR α-order saliency δ = −α·n_q/2 = −3α/2
be DERIVED from the K4-Cosserat substrate kernel back-reaction on the (2,q)
phase-space currents, WITHOUT assuming additivity, INDEPENDENT of the g-2 target?

α ✓ and 1/2 ✓ are taken as corpus-derived (doc 115 §3, §4). The ENTIRE load here
is the power law: does the q-axis kernel-feedback shift scale as n_q (linear),
√n_q (collective), or n_q² (interference)?

METHOD (prereg §4, in order):
  Step 1: kernel back-reaction on the (2,q) phase-space currents, expanded to
          α-order, total budget A_d²+A_q²=4πα fixed. Run q ∈ {1,3,5,7}, read off
          the power law STRUCTURALLY (no inserted independence assumption).
  Step 2: independent-vs-coupled twist criterion — do the leading-α-order cross
          terms vanish by parity/orthogonality (→ linear derived) or survive
          (→ not linear)?
  Step 4: cross-check vs the OTHER substrate winding law χ = α·pq/(p+q) (doc 79 §5).

CRITICAL (do-NOT-mis-frame, prereg §6): the target is the α-ORDER kernel-feedback
n_q-scaling, NOT plugging a geometric ratio (Beltrami 1/(2π), Cosserat-PCA) into δ.
Any geometric O(1) anisotropy is the WRONG mechanism (doc 115 §3).

Run: python3 research/2026-05-31_FT-b-saliency-derivability_attempt.py
"""

from math import pi, sqrt
import numpy as np

ALPHA = 7.2973525693e-3  # canonical, from sweep script (CODATA-consistent)
TWO_PI_ALPHA = 2.0 * pi * ALPHA  # the per-axis Schwinger budget at symmetric split


def kernel_S(A_sq):
    """Ax-4 saturation kernel S(A) = sqrt(1 - A^2), clipped for safety."""
    return np.sqrt(np.clip(1.0 - A_sq, 0.0, 1.0))


# =====================================================================
# STEP 1 — kernel back-reaction on the (2,q) phase-space currents.
#
# The substrate question: at the SYMMETRIC budget (A_d_peak² = A_q_peak² = 2πα),
# the Ax-4 kernel acts on each axis. Per-axis time-averaged kernel deviation from
# unity is the "kernel load" on that axis. The saliency is the asymmetry that the
# kernel back-reaction WANTS to introduce — the kernel does NOT load the d-axis
# (cos 2ωt, n_d=2) and the q-axis (sin qωt, n_q=q) equally, because the harmonic
# content differs.
#
# We compute, WITHOUT assuming any composition law, the per-axis time-averaged
# kernel deviation ⟨1 − S(A_axis²)⟩ at the symmetric budget, for the d-axis and
# for q-axes at q ∈ {1,3,5,7}. The q-DEPENDENCE of (q-load − d-load) is the power
# law we are after. We then ask whether that q-dependence is linear.
# =====================================================================

def per_axis_kernel_load(n_winding, peak_A_sq, Nt=4_000_000):
    """Time-averaged kernel deviation ⟨1 − S(A²(t))⟩ for a single axis with
    current I(t) = sin(n·ωt) (or cos; the time-average is identical), peak
    amplitude² = peak_A_sq. This is the α-order 'how hard the kernel pulls on
    this axis' load, with NO composition assumption — it's a raw time-average.

    At leading order S(A²) ≈ 1 − A²/2, so ⟨1−S⟩ ≈ ⟨A²⟩/2 = peak_A_sq·⟨sin²⟩/2
    = peak_A_sq · (1/2) · (1/2) = peak_A_sq/4 — INDEPENDENT of n (because
    ⟨sin²(nωt)⟩ = 1/2 for every integer n ≥ 1). That n-independence at leading
    order is the crux; we compute the EXACT kernel (not just leading order) to
    catch any n-dependence in the higher-order tail.
    """
    t = np.linspace(0.0, 2.0 * pi, Nt, endpoint=False)
    I = np.sin(n_winding * t)
    A_sq = peak_A_sq * I**2
    return np.mean(1.0 - kernel_S(A_sq))


def step1_power_law():
    print("=" * 78)
    print("STEP 1 — kernel back-reaction per-axis load vs winding count n")
    print("=" * 78)
    print(f"  symmetric budget: peak A² = 2πα = {TWO_PI_ALPHA:.6e} (each axis)")
    print(f"  d-axis winding n_d = 2 (bipartite K4, substrate-universal)")
    print()
    print(f"  {'n':>3} {'⟨1−S(A²)⟩ (exact kernel)':>28} {'/(per-winding unit)':>22}")
    print("  " + "-" * 70)

    d_load = per_axis_kernel_load(2, TWO_PI_ALPHA)
    loads = {}
    for n in [1, 2, 3, 4, 5, 6, 7]:
        load = per_axis_kernel_load(n, TWO_PI_ALPHA)
        loads[n] = load
        # leading-order per-winding unit = (peak_A_sq/2)·(1/2)/1 = peak_A_sq/4
        unit = TWO_PI_ALPHA / 4.0
        print(f"  {n:>3} {load:>28.10e} {load/unit:>22.8f}")
    print()
    print("  READ-OFF: ⟨1−S⟩ is the SAME for every n to leading α-order (= 2πα/4),")
    print("  because ⟨sin²(nωt)⟩ = 1/2 for all integer n ≥ 1. The per-axis kernel")
    print("  load is n-INDEPENDENT at α-order. There is NO n_q-scaling — linear,")
    print("  √n, or n² — in the raw per-axis kernel load.")
    print()
    # Quantify the residual n-dependence (higher-order kernel tail)
    print("  Residual n-dependence (deviation from n=1 load, in units of α²):")
    for n in [2, 3, 5, 7]:
        resid = (loads[n] - loads[1]) / ALPHA**2
        print(f"    n={n}: (load_n − load_1)/α² = {resid:+.6e}   (→ α²-order, sub-leading)")
    print()
    return loads


# =====================================================================
# STEP 2 — independent-vs-coupled twist criterion.
#
# doc 115 §6 asserts: each q-winding is a 'distinct twist'; cross-twist coupling
# is O(α²); so at leading α-order the n_q contributions 'add linearly'.
#
# Test the load-bearing claim: is there a sense in which the q-axis current
# DECOMPOSES into n_q independent unit-contributions that each carry one α-order
# kernel-shift, which then ADD? The q-axis current is a SINGLE sinusoid sin(qωt),
# NOT a sum of q independent sinusoids. We test both readings:
#   (2a) 'single harmonic at frequency q' — what the Route-B currents actually use.
#   (2b) 'sum of q independent unit windings' — what additivity would REQUIRE.
# =====================================================================

def step2_independence_criterion():
    print("=" * 78)
    print("STEP 2 — independent-vs-coupled twist criterion")
    print("=" * 78)
    print("  doc 115 §6 claim: n_q windings 'add linearly' because cross-twist")
    print("  coupling is O(α²). Test what 'add' means structurally.")
    print()

    Nt = 4_000_000
    t = np.linspace(0.0, 2.0 * pi, Nt, endpoint=False)

    # Reading (2a): the ACTUAL Route-B q-axis current — a single harmonic sin(qωt).
    print("  (2a) ACTUAL Route-B q-axis current I_q = sin(q·ωt) [single harmonic]:")
    print(f"       {'q':>3} {'⟨1−S(A_q²)⟩':>20}")
    for q in [1, 3, 5, 7]:
        I_q = np.sin(q * t)
        load = np.mean(1.0 - kernel_S(TWO_PI_ALPHA * I_q**2))
        print(f"       {q:>3} {load:>20.10e}")
    print("       → flat in q (Step 1 result). A single harmonic carries ONE")
    print("         kernel-load unit regardless of its frequency q. NOT q units.")
    print()

    # Reading (2b): what additivity REQUIRES — q independent unit windings, each
    # carrying its own kernel shift, summed. If the q-axis were q SEPARATE unit
    # oscillators each at the budget, the total load would be q × (unit load).
    print("  (2b) ADDITIVITY READING — q independent unit windings, each at budget:")
    print("       IF the q-axis hosted q separate unit oscillators each carrying")
    print("       one α-order kernel-shift unit, total q-load = q × (d-axis unit).")
    print(f"       {'q':>3} {'q × unit-load':>20} {'δ_implied = −(q·load)/(πα·norm)':>34}")
    unit_load = per_axis_kernel_load(1, TWO_PI_ALPHA)
    for q in [1, 3, 5, 7]:
        total = q * unit_load
        print(f"       {q:>3} {total:>20.10e} {'(linear in q BY CONSTRUCTION)':>34}")
    print("       → linear in q — but ONLY because we POSTULATED q independent")
    print("         unit windings. The (2,q) torus knot does NOT supply q separate")
    print("         oscillators; it supplies ONE current at frequency q. The step")
    print("         from (2a) to (2b) IS the additivity postulate. It is INSERTED,")
    print("         not derived.")
    print()


# =====================================================================
# STEP 4 — cross-check vs the OTHER substrate winding law χ = α·pq/(p+q).
#
# doc 79 §5 / doc 20: the chirality coupling combines the two channels via
# PARALLEL impedance χ = α·pq/(p+q) — a DERIVED, p-q-symmetric, NON-linear law.
# For electron (p=2,q=3): χ = α·6/5 = 1.2α. If the substrate's native
# winding-composition is parallel-impedance pq/(p+q), then the saliency 'should'
# inherit THAT law, not a linear one. We compare both against the bisection δ*.
# =====================================================================

def step4_competing_laws():
    print("=" * 78)
    print("STEP 4 — competing substrate winding-composition laws vs bisection δ*")
    print("=" * 78)
    delta_star_over_alpha = -1.4982  # from sweep bisection (re-verified this session)
    print(f"  Bisection target: δ*/α = {delta_star_over_alpha:.4f}  (= −1.498)")
    print()
    p, q = 2, 3
    laws = {
        "LINEAR  −n_q/2        (doc 115 postulate)": -q / 2.0,
        "√n_q    −√n_q/2       (collective)":        -sqrt(q) / 2.0,
        "n_q²    −n_q²/2       (interference)":      -(q**2) / 2.0,
        "pq/(p+q) −pq/(p+q)/2  (doc 79 §5 parallel)": -(p * q / (p + q)) / 2.0,
        "pq/(p+q) −pq/(p+q)    (full chirality χ)":   -(p * q / (p + q)),
        "n_q−n_d  −(n_q−n_d)/2 (difference)":         -(q - 2) / 2.0,
    }
    print(f"  {'law':>46} {'δ/α':>10} {'vs δ*=−1.498':>14}")
    print("  " + "-" * 74)
    for name, val in laws.items():
        dev = (val - delta_star_over_alpha) / delta_star_over_alpha * 100
        print(f"  {name:>46} {val:>10.4f} {dev:>+12.2f}%")
    print()
    print("  The LINEAR law (−1.500) matches δ*=−1.498 to 0.12%. NO OTHER clean")
    print("  substrate law comes close: pq/(p+q)/2 = −0.60 (60% off), √n_q/2 = −0.87")
    print("  (42% off), n_q²/2 = −4.5 (200% off), pq/(p+q) full = −1.20 (20% off).")
    print()
    print("  CRUX: linear is the law that MATCHES — but the substrate already")
    print("  CARRIES a different derived winding-composition (parallel-impedance")
    print("  pq/(p+q), doc 79 §5) for the SAME (2,q) two-channel structure. A")
    print("  derivation of the saliency must explain WHY saliency takes the linear")
    print("  law while chirality takes pq/(p+q). Nothing in Steps 1-2 supplies that")
    print("  reason: the kernel load is q-FLAT (Step 1), and linearity only appears")
    print("  when q independent unit windings are POSTULATED (Step 2b).")
    print()


def main():
    print()
    print("#" * 78)
    print("# FT-b — saliency δ=−3α/2 derivability attempt")
    print("# Can n_q-LINEAR additivity be DERIVED (not postulated) from the kernel?")
    print("#" * 78)
    print()
    step1_power_law()
    step2_independence_criterion()
    step4_competing_laws()
    print("=" * 78)
    print("VERDICT (see result doc for full adjudication)")
    print("=" * 78)
    print("""
  Step 1: raw per-axis kernel load is n-INDEPENDENT at α-order (⟨sin²(nωt)⟩=1/2
          for all n). No linear/√n/n² scaling emerges from the kernel acting on
          the actual single-harmonic (2,q) currents.
  Step 2: linearity-in-q appears ONLY under the 'q independent unit windings'
          reading (2b) — which is the additivity POSTULATE. The actual (2,q)
          torus knot supplies ONE q-frequency current, not q oscillators.
  Step 4: linear MATCHES δ* (0.12%) but is not SELECTED by substrate dynamics;
          the substrate's own derived winding-composition for the same (2,q)
          two-channel object is the DIFFERENT pq/(p+q) parallel-impedance law.

  → OUTCOME C: n_q-additivity cannot be derived without assuming it this session.
    The α-order kernel back-reaction does not, by itself, produce a q-scaling at
    all; linearity is INSERTED by the independent-winding postulate. δ=−3α/2 is a
    1-point fit to δ*, structurally motivated but not derived.
""")


if __name__ == "__main__":
    main()
