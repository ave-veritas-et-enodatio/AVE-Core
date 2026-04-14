[↑ Ch. 9: Computational Proof and Anomaly Catalog](./index.md)
<!-- leaf: verbatim -->

## Computational Proof of Scale Invariance

The full computational proof is implemented in the physics engine module `src/ave/axioms/scale_invariant.py`. Every domain module in the framework (`saturation.py`, `fdtd_3d.py`, and 13 other domain modules) imports its impedance operations from this single canonical source. The automated test suite verifies that the same function produces identical numerical results whether called with particle-scale, molecular-scale, laboratory-scale, geophysical-scale, or galactic-scale inputs.

This is not an analogy. It is a **structural identity**: the same operator, the same code, the same mathematics, from $10^{-13}$ m to $10^{26}$ m.

## Verification Summary

| Domain | Prediction | Regime | Agreement | Params |
|---|---|---|---|---|
| Galactic rotation (NGC 3198) | $v = 159$ km/s | I/IV | 5% | 0 |
| Multi-galaxy RAR | McGaugh curve | I--IV | exact | 0 |
| 'Oumuamua acceleration | $4.54 \times 10^{-6}$ m/s$^2$ | I | 91% | 0 |
| Kirkwood gaps (5/5) | $< 0.3\%$ error | I | $<$0.3% | 0 |
| Earth magnetopause | 9.1 R$_E$ | I | 8.7% | 0 |
| Jupiter magnetopause | 55.6 R$_J$ | I | 11.8% | 0 |
| Neutrino MSW $P_{ee}$ (4 channels) | 0.31--0.55 | I | $<$10% | 0 |
| Superconductor $B_c(T)$ (5 materials) | $\sqrt{1-(T/T_c)^2}$ | II/III | exact | 0 |
| London depth ($\lambda_L$) | 37--150 nm | II/III | exact | 0 |
| Seismic $\Gamma_{\text{Moho}}$ | 0.29 | I | matches PREM | 0 |
| GW lossless propagation | $V_{GW}/V_{snap} = 10^{-28}$ | I | exact | 0 |
| Topological Pair Production | $H_{net}=0 \to e^+ + e^-$ | IV | exact | 0 |
| Protein folding (CLN025) | RMSD = 2.59 A | I | sub-3 A | 0 |

[Figure: cross_scale_verification.png — The single Axiom 4 saturation kernel $S(x, x_{yield}) = \sqrt{1 - (x/x_{yield})^2}$ governs physics from the lattice pitch ($10^{-13}$ m) to the Hubble radius ($10^{26}$ m) — 39 orders of magnitude with the same operator, the same code, zero adjustable parameters. See manuscript/vol_2_subatomic/chapters/]

<!-- Anomaly A7: source uses \ref{ch:quantum_mechanics_and_orbitals} which is undefined; likely typo for ch:quantum_orbitals -->

---
