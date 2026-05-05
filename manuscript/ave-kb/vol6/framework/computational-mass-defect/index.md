[↑ Vol 6: Framework](../index.md)
<!-- claim-quality (subtree): 5965y1, 6tuqjh, 86gq2d, jy8h1x, llqd1n, lqanmt, nk6c43 -->

# Computational Mass Defect via Mutual Impedance

A fundamental challenge in standard continuous vacuum theories is calculating the total integrated strain (and therefore the total energy or mass) of complex overlapping geometrical fields. Because the AVE framework defines the vacuum as a discrete $LC$ network, established Electrical Engineering network theory is leveraged to compute nuclear masses via mutual impedance summation with zero empirical parameters.

## Key Results

| Result | Expression |
|---|---|
| Total internal energy | $U_{total} = \sum U_{self} - \frac{1}{2} \sum \sum_{i \neq j} M_{ij} I_i I_j$ |
| Nucleon spacing | $d = 4\hbar/(m_p c) \approx 0.841$ fm |
| Intra-alpha distance | $D_{\text{intra}} = d\sqrt{8} \approx 2.379$ fm |
| Mutual coupling constant | $K = \frac{5\pi}{2} \cdot \frac{\alpha \hbar c}{1 - \alpha/3} \approx 11.337$ MeV$\cdot$fm |
| Coulomb correction | $\Delta E_{\text{Coulomb}} = -\alpha\hbar c \cdot f_{pp} \cdot \sum_{i<j} 1/r_{ij}$ |
| Topologic yield ceiling | $E_{\text{binding(max)}} = \alpha \cdot M_{\text{proton}} c^2 \approx 6.847$ MeV |
| Breakdown voltage | $V_{BR} = 6\,\alpha\hbar c / D_{\text{intra}} \approx 3.631$ MeV |
| Miller multiplication | $M = 1/(1 - (V_R/V_{BR})^n)$, $n = c_{\text{proton}} = 5$ |
| Complete binding formula | $M_{\text{nucleus}} = N_\alpha M_\alpha - \sum K/r_{ij} + M \cdot \sum f_{pp}\,\alpha\hbar c/r_{ij}$ |
| Small-to-Large Signal transition | $V_R/V_{BR} = 0.994$ at S-32 ($M = 32.8$) |

## Derivations and Detail

| Document | Contents |
|---|---|
| [Mass as a Localized Reactive Load](mass-as-reactive-load.md) | Mass defect as mutual inductance change in coupled LC network |
| [Topological Circuit Conventions](topological-circuit-conventions.md) | Mapping of mass, vacuum space, binding force, electrons, isotope stability to LC network quantities |
| [Python Simulator](python-simulator.md) | EE-based thermodynamic integration code: $1/d$ mutual coupling energy subtraction |
| [Network Analytics](network-analytics.md) | Quality Factor ($Q$) and $S_{11}$ scattering cross-section analysis |
| [Nucleon Spacing Derivation](nucleon-spacing-derivation.md) | Derivation of $d$ from Axiom 1; intra-alpha distance $D_{\text{intra}}$ from tetrahedral packing |
| [Mutual Coupling Constant](mutual-coupling-constant.md) | Derivation of $K$ from cinquefoil crossing number, Coulomb constant, proximity correction |
| [Proton-Neutron Junction Coupling](pn-junction-coupling.md) | Nuclear diode analogy, Coulomb correction, topologic yield mass defect |
| [ABCD Transfer Matrix](abcd-transfer-matrix.md) | Transfer matrix cascade for alpha-cluster port networks |
| [Operating Regimes](operating-regimes.md) | Linear (Small Signal), Non-Linear (Large Signal), Saturated (Breakdown) regimes |
| [Semiconductor Nuclear Analysis](semiconductor-nuclear-analysis.md) | Full semiconductor junction model: parameter derivation, breakdown voltage, Miller avalanche, binding formula, topology as device type, coupled cavity resonators |
| [Radioactive Decay as Impedance Mismatch](radioactive-decay-impedance.md) | Tritium beta decay and Beryllium-8 alpha fission via Q-factor analysis |
