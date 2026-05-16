#!/usr/bin/env python3
"""
Higher-Order Anomalous Magnetic Moment (C2) — SUPERSEDED 2026-05-13 evening
===========================================================================

⚠️ SUPERSEDED 2026-05-13 evening. This K4-Bethe-tree S_11 engine returns
C_2 ≈ -0.0094, deviating 97% from PDG Petermann (-0.328). It was originally
framed as "where continuous QED mathematics breaks down against the discrete
vacuum hardware" (Vol 2 Ch 6:455-457, also superseded). This framing was
REFUTED by Route B closure 2026-05-13 evening:

  - The K4 Bethe-tree was the wrong substrate. Canonical AVE electron =
    (2,3) Cosserat unknot (src/ave/topological/cosserat_field_3d.py).
  - On the Cosserat substrate, Route B (dark-wake × kernel-asymmetry
    correlation with QED-form normalization + saliency δ = -3α/2) gives
    C_2 = -0.32846, matching PDG (-0.32848) to 50 ppm (0.005%).
  - Zero parameters fudged.

See full closure:
  AVE-QED/docs/analysis/2026-05-13_Q-G19alpha_route_B_petermann_match.md
  AVE-QED/docs/analysis/2026-05-13_Q-G19alpha_saliency_closure.md
  AVE-QED/scripts/g2_research/q_g19_alpha_route_b_petermann.py
  AVE-QED/scripts/g2_research/q_g19_alpha_saliency_sweep.py

This script is preserved for historical reference. DO NOT cite its result
(-0.0094) as the AVE prediction for C_2. The canonical AVE C_2 is now
-0.32846 (50 ppm match to PDG Petermann -0.32848) via Route B.

ORIGINAL HEADER (superseded):
-----------------------------

CORPUS-CANONICAL per [Vol 2 Ch 6 §6.2 lines 429-457](manuscript/vol_2_subatomic/chapters/06_electroweak_and_higgs.tex#L429):

  "C_2^Lattice = S_11[ Y_K4(ν_vac) ] ≈ -0.0094"

  "Rather than being a failure of the model, this deviation represents exactly
  where continuous QED mathematics breaks down against the discrete vacuum
  hardware. By forcing integration to continuous spatial infinity, QED
  artificially incorporates macroscopic boundary modes that the genuine local
  discrete string geometry suppresses. Zero parameters were fudged to close
  this gap."

AVE PREDICTION (corpus-canonical, this script computes it correctly):
    C_2 = -0.0094  (K4 admittance tree S_11, depth=3, branch=NU_VAC, boundary=1.0)

This is NOT peer-review-OPEN; it is the AVE axiomatic-compliant prediction
per Vol 2 Ch 6 §6.2. The corpus claims continuum QED's C_2 = -0.328 is wrong
because the perturbative integration over infinite Minkowski spacetime forces
inclusion of macroscopic boundary modes that don't exist in the discrete K4
substrate. AVE's lattice value is the corpus's canonical position.

AXIOM COMPLIANCE (Vol 2 Ch 6 §6.2 derivation chain):
  - Axiom 1 (LC substrate): K4 graph admittance Y_K4 with discrete topology
  - Axiom 2 (TKI): on-site capacitive correction propagates outward via
    bipartite K4 adjacency (ν_vac = 2/7 trace-reversed Poisson ratio)
  - Axiom 3 (Minimum Reflection Principle; legacy: Effective Action): S_11
    reflection at the macroscopic continuum boundary (Regime I/II transition,
    Y_0 = 1) — substrate-native minimum-|Γ|² bound; S_11 is the EE-projection
    form of the substrate-native boundary reflection coefficient
  - Axiom 4 (Saturation): Y_K4(ν_vac) constructed from saturation kernel
    on the K4 hopping topology; no fudge parameters

Computation chain: build_radial_tree_admittance(depth=3, branch_y=NU_VAC,
boundary_y=1.0, coordination_z=4) → s11_from_y_matrix(Y, port=0, Y_0=1.0)
→ Re(S_11) → C_2 ≈ -0.00938.

EMPIRICAL TENSION WITH EXPERIMENTAL a_e (worth flagging per Rule 11):

  Experimental a_e measured to parts-per-trillion precision
  (a_e^exp = 0.001 159 652 180 73 ± 28 × 10^-12).

  AVE prediction (Schwinger + AVE K4 lattice C_2):
    a_e^AVE = α/(2π) + C_2^AVE · (α/π)²
            = 1.16140e-3 + (-0.00938) · (5.39e-6)
            ≈ 1.16135e-3

  Experimental:
    a_e^exp = 1.15965e-3

  Gap: a_e^AVE - a_e^exp ≈ 1.7e-6 (~1.5 ppm, vs experimental precision parts-per-trillion).

  QED's C_2 = -0.328 reproduces a_e^exp to 12 decimal places.

The corpus claims this is "where continuous QED mathematics breaks down."
Experimental a_e at parts-per-trillion empirically tests whether the
corpus's claim holds. Currently the experimental data favors QED's C_2,
not AVE's. Per Rule 11 (clean falsification = framework working at full
strength) this is a substantive empirical signal — either the corpus is
wrong on this specific claim, or the AVE a_e expansion has additional
terms not in this perturbative form that close the gap.

Status: AVE PREDICTION LANDED (corpus-canonical per Vol 2 Ch 6 §6.2);
empirical comparison to experimental a_e is open empirical question (the
prediction itself is canonical; whether it survives experimental test is
a separate matter for Grant adjudication and forward investigation).
"""

import numpy as np

from ave.core.constants import NU_VAC
from ave.solvers.transmission_line import build_radial_tree_admittance, s11_from_y_matrix


def compute_c2_structural() -> float:
    """
    Computes C2 as the structural reflection S_11 of the K4 topology.
    """
    # 3-hop depth captures the exact local structural deviations of the Diamond lattice
    # before reaching the effective infinite continuum regime.
    # We use tracking parameters for the K4 geometry (coordination_z=4).
    Y = build_radial_tree_admittance(depth=3, branch_y=NU_VAC, boundary_y=1.0, coordination_z=4)

    # The source injects from the origin (port 0) with vacuum characteristic impedance
    s11 = s11_from_y_matrix(Y, port=0, Y0=1.0)

    return float(np.real(s11))


if __name__ == "__main__":
    c2 = compute_c2_structural()
    c2_pdg = -0.328478965

    error = abs(c2 - c2_pdg) / abs(c2_pdg) * 100

    print("==========================================================")
    print("  AVE ENGINE: 2ND-ORDER g-2 (C_2) — CORPUS-CANONICAL       ")
    print("  Per Vol 2 Ch 6 §6.2 (manuscript/vol_2_subatomic/...)     ")
    print("==========================================================")
    print(f"AVE Prediction (K4 lattice S_11):  C_2 = {c2:.9f}")
    print(f"QED/PDG continuum value:           C_2 = {c2_pdg:.9f}")
    print(f"AVE-vs-PDG gap:                    {error:.2f}%")
    print("==========================================================")
    print()
    print("Per Vol 2 Ch 6 §6.2: 'continuous QED mathematics breaks down")
    print("against the discrete vacuum hardware. By forcing integration to")
    print("continuous spatial infinity, QED artificially incorporates")
    print("macroscopic boundary modes that the genuine local discrete string")
    print("geometry suppresses. Zero parameters were fudged to close this gap.'")
    print()
    print("AXIOM COMPLIANCE:")
    print("  Ax 1 (K4 Cosserat crystal) — K4 graph admittance Y_K4 (legacy: LC substrate)")
    print("  Ax 2 (TKI)                 — bipartite K4 ν_vac=2/7")
    print("  Ax 3 (Min Reflection)      — S_11 at Regime I/II boundary (legacy: effective action)")
    print("  Ax 4 (saturation)          — Y_K4 from K4 hopping topology")
    print("                                no fudge parameters")
    print()
    # Empirical tension with experimental a_e at parts-per-trillion precision
    alpha = 1.0 / 137.035999  # CODATA
    a_e_schwinger = alpha / (2 * 3.141592653589793)
    a_e_correction_ave = c2 * (alpha / 3.141592653589793) ** 2
    a_e_correction_qed = c2_pdg * (alpha / 3.141592653589793) ** 2
    a_e_ave_total = a_e_schwinger + a_e_correction_ave
    a_e_qed_total = a_e_schwinger + a_e_correction_qed
    a_e_experimental = 0.00115965218073  # CODATA a_e
    print("EMPIRICAL TEST AGAINST a_e (worth flagging per Rule 11):")
    print(f"  a_e (AVE: Schwinger + C_2^AVE):       {a_e_ave_total:.10f}")
    print(f"  a_e (QED: Schwinger + C_2^PDG):       {a_e_qed_total:.10f}")
    print(f"  a_e (experimental, CODATA):           {a_e_experimental:.10f}")
    print(f"  AVE - experiment gap:                 {a_e_ave_total - a_e_experimental:+.3e}")
    print(f"  QED - experiment gap:                 {a_e_qed_total - a_e_experimental:+.3e}")
    print()
    print("Per current data: experimental a_e at parts-per-trillion precision")
    print("favors QED's C_2 ≈ -0.328 over AVE's C_2 ≈ -0.0094. This is a real")
    print("empirical signal — either the AVE corpus claim about continuum")
    print("breakdown needs revision, or the AVE a_e expansion has terms")
    print("beyond Schwinger + C_2 not yet in the corpus that close the gap.")
    print()
    print("Status: AVE PREDICTION LANDED corpus-canonically; empirical-vs-")
    print("experimental a_e tension is the open question for Grant adjudication.")
