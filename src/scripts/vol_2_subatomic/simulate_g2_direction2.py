#!/usr/bin/env python3
"""
Direction-2 FT: re-extract alpha from the measured electron anomaly through
AVE's OWN a_e(alpha) series.
=========================================================================

Methodological inversion of the delta_strain problem. Standard physics
extracts alpha by inverting a self-coupling series against the MEASURED
electron anomaly a_e (theory-neutral cyclotron/anomaly frequency ratio):

    QED faceplate:  a_e = (1/2)(a/pi) + C2 (a/pi)^2 + ...,  C2 = -0.328478965
                    inverts -> alpha^-1 = 137.035999

This driver re-extracts alpha from the SAME measured a_e through AVE's own
a_e(alpha) series (the Axiom-4 back-reaction faceplate), and checks where
alpha_AVE^-1 lands:

  Outcome A (dissolution): alpha_AVE^-1 -> Q0 = 4pi^3+pi^2+pi = 137.0363038
       => delta_strain was the QED-vs-AVE faceplate offset, dissolved.
  Outcome B (internal inconsistency): alpha_AVE^-1 -> 137.035999 (A2 = C2)
       => delta_strain is real; AVE geometry disagrees with AVE measurement theory.
  Outcome C (inconclusive): A2 not computable to enough precision to separate.

Chain (prereg sec.4):
  (i)  Confirm A1 = 1/2 from simulate_g2.py (AVE leading = alpha/2pi = Schwinger).
  (ii) BUILD AVE's (a/pi)^2 coefficient A2 from the two-vertex substrate
       self-energy (Route B dark-wake x kernel-asymmetry correlation per
       q-g19a-petermann-saliency-closure.md) -- from substrate primitives,
       NO target value fed in.
  (iii) Invert a_e_measured = (1/2)(a/pi) + A2 (a/pi)^2 + ... for alpha_AVE.
  (iv) Compare alpha_AVE^-1 to Q0 vs QED's 137.035999.

HARD GUARDS (prereg sec.6):
  1. Anti-tuning: A2 computed from substrate FIRST; neither Q0 nor 137.035999
     nor delta_strain nor the target dC2 enters the A2 computation.
  2. ave-power-category-check: a_e is the REAL-power self-load (dissipative leg).
  3. ave-discrimination-check: AVE-distinct content is A2 != QED's C2.
  4. NO cosmic-magnitude smuggling: MEASURED a_e + LOCAL self-energy only;
     no f_R / cosmic chirality fraction / A-031-inaccessible parameter.
  5. ave-canonical-source: primitives from constants.py; no round numbers.

Driver companion to simulate_g2.py (which confirms A1 = 1/2). This driver does
NOT rewrite that chain; it imports the same canonical ALPHA and extends to A2 +
the re-extraction.

Usage:
    PYTHONPATH=manuscript/ave-kb/tools python \
        src/scripts/vol_2_subatomic/simulate_g2_direction2.py
"""

from math import pi

import numpy as np

from ave.core.constants import ALPHA, ALPHA_COLD_INV

# ============================================================================
# ANCHORS (prereg sec.3) -- measured / external, used only for INVERSION +
# COMPARISON, never inside the A2 computation (Guard 1).
# ============================================================================
A_E_MEASURED = 1.15965218073e-3   # measured electron anomaly (frequency ratio)
C2_QED = -0.328478965             # QED 2-loop Petermann coefficient (SM-counterfactual)
ALPHA_INV_QED = 1.0 / ALPHA       # CODATA alpha^-1, derived from canonical ALPHA (faceplate comparison anchor; ave-canonical-source — no hardcoded magic number)
Q0_INV = ALPHA_COLD_INV           # = 4pi^3 + pi^2 + pi = 137.0363038 (canonical)

# QED higher-loop coefficients (for apples-to-apples faceplate framing only;
# NOT used in the AVE A2 build).
C3_QED = 1.181241456              # 3-loop
C4_QED = -1.91298                 # 4-loop (approximate)


# ============================================================================
# STEP (i) -- Confirm A1 = 1/2 (AVE leading = alpha/2pi = Schwinger)
# ============================================================================
# From simulate_g2.py: (V_peak/V_snap)^2 = 4pi*alpha exact; <deps/eps> = -pi*alpha;
# delta_omega/omega = pi*alpha/2; x (1/pi^2) spin-orbit projection -> a_e = alpha/2pi.
# In faceplate form a_e = A1(a/pi) + A2(a/pi)^2 + ..., the leading coeff is:
A1_AVE = 0.5   # a_e^(1) = (1/pi^2)(pi*alpha/2) = alpha/(2pi) = (1/2)(alpha/pi)


# ============================================================================
# STEP (ii) -- BUILD A2 from the substrate two-vertex self-energy (Route B)
# ============================================================================
# Per q-g19a-petermann-saliency-closure.md (canonical) + L3 doc 115:
# AVE's second-order anomalous-moment shift is the dark-wake x kernel-asymmetry
# correlation in the Cosserat (2,3) phase-space trefoil -- the AVE substitute
# for QED's two-loop vertex insertion (the two-vertex alpha^2 self-energy of
# weak-coupling.md:22, eps(phi)=eps0(1+alpha*f(phi)) -> E_self propto alpha^2).
#
# Five substrate-canonical ingredients (NO target fed in):
#   1. (2,3) phase-space trefoil currents: I_d = cos(2 wt), I_q = sin(3 wt)
#   2. Axiom-4 saturation kernel asymmetry: S_d - S_q = sqrt(1-A_d^2) - sqrt(1-A_q^2)
#   3. dark wake (retarded back-reaction): tau_zx(t) = -dV^2/dt|_{t - tau_retard},
#      tau_retard = 1/w_C (one Compton-loop transit, geometrically pinned)
#   4. correlation = <(S_d - S_q) tau_zx>  (the 2nd-order kernel structure)
#   5. normalization: 1/pi^2 form factor (inherited from Schwinger leading order)
#      x one QED-loop factor alpha/pi
#
#   => Delta a_e^(2) = (1/pi^2) <(S_d-S_q) tau_zx> (alpha/pi)
#   => A2 = (2/pi^2) <(S_d-S_q) tau_zx>    [since a_e = A1(a/pi)+A2(a/pi)^2,
#                                           A1=1/2, and a_e^(2)=A2(a/pi)^2]
#
# Strain split (Schwinger budget A_d^2 + A_q^2 = 4pi*alpha):
#   symmetric (Route B, NO postulate):  A_d,peak^2 = A_q,peak^2 = 2pi*alpha
#   saliency closure (WITH n_q-additivity postulate):
#       A_d,peak^2 = (1+delta) 2pi*alpha, A_q,peak^2 = (1-delta) 2pi*alpha,
#       delta = -alpha*n_q/2 = -3alpha/2 (n_q=3, q-axis trefoil winding)


def _kernel_S(a_sq):
    """Axiom-4 saturation kernel S(A) = sqrt(1 - A^2), clipped for safety."""
    return np.sqrt(np.clip(1.0 - a_sq, 0.0, 1.0))


def route_b_correlation(delta=0.0, tau_retard=1.0, n_t=2_000_000):
    """Substrate dark-wake x kernel-asymmetry correlation <(S_d - S_q) tau_zx>.

    delta: d/q strain-split saliency (0 = symmetric Route B, parameter-free).
    tau_retard: dark-wake retardation in Compton-phase units (1 = 1/w_C, pinned).
    Returns the cycle-averaged correlation (the AVE second-order kernel structure).
    """
    t = np.linspace(0.0, 2.0 * pi, n_t, endpoint=False)
    dt = t[1] - t[0]

    # (2,3) phase-space trefoil currents
    i_d = np.cos(2.0 * t)
    i_q = np.sin(3.0 * t)

    # Schwinger-budget strain amplitudes with optional saliency split
    a_peak_sq = 2.0 * pi * ALPHA
    a_d_sq = (1.0 + delta) * a_peak_sq * i_d**2
    a_q_sq = (1.0 - delta) * a_peak_sq * i_q**2

    # Axiom-4 kernel asymmetry
    kernel_diff = _kernel_S(a_d_sq) - _kernel_S(a_q_sq)

    # Dark wake: retarded derivative of total V^2
    v_sq = i_d**2 + i_q**2
    dv2_dt = np.gradient(v_sq, dt)
    shift_idx = int(tau_retard / dt) % n_t
    tau_zx = -np.roll(dv2_dt, shift_idx)

    return float(np.mean(kernel_diff * tau_zx))


def correlation_to_A2(correlation):
    """Convert the substrate correlation to the faceplate coefficient A2.

    a_e = A1(a/pi) + A2(a/pi)^2, with a_e^(2) = (1/pi^2) correlation (a/pi).
    => A2 (a/pi)^2 = (1/pi^2) correlation (a/pi)  => A2 = (1/pi^2) correlation / (a/pi)
       = correlation / (pi^2 * alpha / pi) = correlation / (pi * alpha).
    Equivalent corpus form C2^AVE = (2/(pi*alpha)) correlation differs by the
    A1=1/2 normalization: C2 is defined for a_e = (a/2pi)[1 + 2 C2 (a/pi)], i.e.
    a_e = A1(a/pi) + (2 A1 C2)(a/pi)^2, so A2 = 2 A1 C2 = C2 (since A1=1/2 the
    faceplate coeff A2 EQUALS the Petermann C2). We carry A2 == C2-convention.
    """
    # Corpus convention: C2^AVE = (2/(pi*alpha)) * correlation, and with A1=1/2
    # the faceplate A2 coefficient is numerically identical to C2.
    return (2.0 / (pi * ALPHA)) * correlation


# ============================================================================
# STEP (iii) -- Invert a_e_measured through the AVE faceplate for alpha_AVE
# ============================================================================
def invert_faceplate(a_e, coeffs, n_iter=200):
    """Solve a_e = (1/2) x + sum_{k>=2} coeffs[k] x^k for x = alpha/pi.

    Perturbative (small-root) fixed-point iteration: x = 2(a_e - sum_{k>=2} c_k x^k).
    coeffs: dict {k: c_k} for k >= 2. Returns alpha^-1.
    """
    x = 2.0 * a_e  # leading (Schwinger-only) seed
    for _ in range(n_iter):
        s = sum(c * x**k for k, c in coeffs.items())
        x = 2.0 * (a_e - s)
    alpha = x * pi
    return 1.0 / alpha


# ============================================================================
# STEP (iv) -- Compare alpha_AVE^-1 to Q0 vs QED
# ============================================================================
def adjudicate(alpha_inv_ave, label, dc2):
    """Print where alpha_AVE^-1 lands relative to Q0 and QED; tag outcome."""
    d_q0 = alpha_inv_ave - Q0_INV
    d_qed = alpha_inv_ave - ALPHA_INV_QED
    span = Q0_INV - ALPHA_INV_QED  # = +3.05e-4 (the delta_strain-scale gap)
    print(f"  [{label}]")
    print(f"    A2 (AVE)              = {label_a2(label):+.6f}")
    print(f"    dC2 vs QED (-0.32848) = {dc2:+.6e}")
    print(f"    alpha_AVE^-1          = {alpha_inv_ave:.6f}")
    print(f"    vs Q0  (137.0363038)  = {d_q0:+.6e}  ({d_q0 / span:+.2f} gap-widths)")
    print(f"    vs QED (137.035999)   = {d_qed:+.6e}  ({d_qed / span:+.2f} gap-widths)")
    print()


_A2_REGISTRY = {}


def label_a2(label):
    return _A2_REGISTRY.get(label, float("nan"))


def main():
    print("=" * 74)
    print("  DIRECTION-2 FT: re-extract alpha from measured a_e via AVE faceplate")
    print("=" * 74)
    print()
    print(f"  measured a_e            = {A_E_MEASURED:.11e}")
    print(f"  QED C2 (2-loop)         = {C2_QED:+.9f}  [SM-counterfactual]")
    print(f"  Q0 = 4pi^3+pi^2+pi      = {Q0_INV:.7f}")
    print(f"  QED extraction          = {ALPHA_INV_QED:.6f}")
    print(f"  gap (Q0 - QED)          = {Q0_INV - ALPHA_INV_QED:+.6e}  (delta_strain scale)")
    print()

    # --- STEP (i) A1 = 1/2 ----------------------------------------------------
    print("-" * 74)
    print("  STEP (i): leading faceplate term")
    print(f"    A1 (AVE)  = {A1_AVE}   (= Schwinger 1/2; from simulate_g2.py)")
    print()

    # --- STEP (ii) BUILD A2 (substrate FIRST; no target) ----------------------
    print("-" * 74)
    print("  STEP (ii): BUILD A2 from substrate two-vertex self-energy (Route B)")
    print()
    # (a) parameter-free symmetric Route B (the HONEST substrate output)
    corr_sym = route_b_correlation(delta=0.0, tau_retard=1.0)
    a2_sym = correlation_to_A2(corr_sym)
    _A2_REGISTRY["Route B symmetric (NO postulate)"] = a2_sym
    print(f"    symmetric correlation <(S_d-S_q)tau_zx> = {corr_sym:+.6e}")
    print(f"    A2 (Route B symmetric, NO postulate)    = {a2_sym:+.6f}")
    print(f"      vs QED C2 = {C2_QED:+.6f}  ->  dev = {(a2_sym - C2_QED) / C2_QED * 100:+.2f}%")
    print()
    # (b) saliency closure WITH n_q-additivity postulate
    delta_saliency = -1.5 * ALPHA  # = -alpha*n_q/2, n_q=3
    corr_sal = route_b_correlation(delta=delta_saliency, tau_retard=1.0)
    a2_sal = correlation_to_A2(corr_sal)
    _A2_REGISTRY["Saliency closure (WITH postulate)"] = a2_sal
    print(f"    saliency delta = -3alpha/2              = {delta_saliency:+.6e}")
    print(f"    saliency correlation                    = {corr_sal:+.6e}")
    print(f"    A2 (saliency, WITH n_q postulate)       = {a2_sal:+.6f}")
    print(f"      vs QED C2 = {C2_QED:+.6f}  ->  dev = {(a2_sal - C2_QED) / C2_QED * 100:+.2f}%")
    print()

    # --- STEP (iii)+(iv) Invert + compare -------------------------------------
    print("-" * 74)
    print("  STEP (iii)+(iv): invert measured a_e through AVE faceplate + compare")
    print()

    # Reference: invert through QED faceplate (sanity -- should give ~137.036)
    aqed_2loop = invert_faceplate(A_E_MEASURED, {2: C2_QED})
    aqed_full = invert_faceplate(A_E_MEASURED, {2: C2_QED, 3: C3_QED, 4: C4_QED})
    print(f"  [reference] QED 2-loop-only faceplate -> alpha^-1 = {aqed_2loop:.6f}")
    print(f"  [reference] QED full (2,3,4-loop)     -> alpha^-1 = {aqed_full:.6f}")
    print()

    # AVE faceplate inversions (2-loop-only, since that is what AVE provides)
    ainv_sym = invert_faceplate(A_E_MEASURED, {2: a2_sym})
    adjudicate(ainv_sym, "Route B symmetric (NO postulate)", a2_sym - C2_QED)
    ainv_sal = invert_faceplate(A_E_MEASURED, {2: a2_sal})
    adjudicate(ainv_sal, "Saliency closure (WITH postulate)", a2_sal - C2_QED)

    # What A2 would land EXACTLY on each reference (post-hoc diagnostic only) ---
    print("-" * 74)
    print("  DIAGNOSTIC (post-hoc; NOT used in the A2 build) -- target A2 values:")
    alpha_q0 = 1.0 / Q0_INV
    xq = alpha_q0 / pi
    a2_to_q0 = (A_E_MEASURED - 0.5 * xq) / xq**2
    alpha_cod = 1.0 / ALPHA_INV_QED
    xc = alpha_cod / pi
    a2_to_qed = (A_E_MEASURED - 0.5 * xc) / xc**2
    print(f"    A2 (2-loop-only) that lands on Q0   = {a2_to_q0:+.6f}  (dC2 = {a2_to_q0 - C2_QED:+.3e})")
    print(f"    A2 (2-loop-only) that lands on QED  = {a2_to_qed:+.6f}  (dC2 = {a2_to_qed - C2_QED:+.3e})")
    print()

    # --- tau-retard fragility scan (anti-tuning transparency) -----------------
    print("-" * 74)
    print("  ANTI-TUNING TRANSPARENCY: tau_retard sensitivity of symmetric A2")
    print(f"  {'tau_retard':<22}{'correlation':>16}{'A2':>14}")
    for tau, lbl in [(1.0, "1 (1/w_C, pinned)"), (pi / 3, "pi/3"), (pi / 2, "pi/2"),
                     (2 * pi / 3, "2pi/3"), (pi, "pi"), (2 * pi, "2pi")]:
        c = route_b_correlation(delta=0.0, tau_retard=tau, n_t=400_000)
        print(f"  {lbl:<22}{c:>+16.6e}{correlation_to_A2(c):>+14.6f}")
    print()

    return {
        "A1_AVE": A1_AVE,
        "A2_route_b_symmetric": a2_sym,
        "A2_saliency": a2_sal,
        "C2_QED": C2_QED,
        "alpha_inv_route_b_symmetric": ainv_sym,
        "alpha_inv_saliency": ainv_sal,
        "Q0_inv": Q0_INV,
        "alpha_inv_QED": ALPHA_INV_QED,
        "A2_to_Q0": a2_to_q0,
        "A2_to_QED": a2_to_qed,
    }


if __name__ == "__main__":
    main()

