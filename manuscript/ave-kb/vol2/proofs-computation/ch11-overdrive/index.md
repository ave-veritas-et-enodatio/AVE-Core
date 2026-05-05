[↑ Proofs and Computation](../index.md)
<!-- claim-quality (subtree): dboxok -->

# Ch. 11: The Standard Model Overdrive

Chapter 11 demonstrates computational supremacy of the Universal Topological Optimisation Engine by applying a single $O(N^2)$ impedance-minimising gradient descent — unmodified — to two of modern physics' most computationally demanding grand challenge problems: heavy nuclear assembly and first-principles protein folding.

## Key Results

| Result | Statement |
|---|---|
| Universal strain energy | $U_{total} = \sum_{i < j}^{N} \frac{K_{mutual}}{d_{ij}} + \sum_{i} U_{bond}(\theta_i, \phi_i)$ |
| Nuclear coupling constant | $K_{mutual} = \frac{5\pi}{2} \cdot \frac{\alpha \hbar c}{1 - \alpha/3} \approx 11.337$ MeV $\cdot$ fm (zero-parameter) |
| U-235 binding energy | Converges to empirical value with $< 0.01\%$ error for $A \leq 28$, sub-percent through actinides |
| Inter-nucleon geometry | Dense-packed lattice with $d_{intra} = d_p \sqrt{8} \approx 2.38$ fm |
| Polyalanine folding | Backbone dihedrals ($\phi \approx -57°$, $\psi \approx -47°$) emerge from impedance minimisation with no imposed Ramachandran constraint |
| Computational scaling | AVE: $O(N^2)$, 0 params, single core (seconds) vs Lattice QCD: $O(N^3)$+, ~6 params, supercomputer (months) vs AlphaFold: $O(N^2)$, ~$10^8$ NN weights, GPU cluster (hours) |

## Derivations and Detail

| Document | Contents |
|---|---|
| [Universal Energy](./universal-energy.md) | Universal strain energy functional and gradient descent update rule |
| [Overdrive Nuclear](./overdrive-nuclear.md) | Nuclear coupling constant derivation and Uranium-235 assembly demonstration |
| [Overdrive Protein](./overdrive-protein.md) | Biological coupling constant and Polyalanine folding demonstration |
| [Overdrive Comparison](./overdrive-comparison.md) | Computational scaling comparison table: AVE vs Lattice QCD, AlphaFold, DFT |
| [Axiom Survey](./axiom-survey.md) | GAP — no axiombox environments found in ch11 source |

---
