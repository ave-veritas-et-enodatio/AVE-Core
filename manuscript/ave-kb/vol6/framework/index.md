[↑ Vol 6: Periodic Table](../index.md)
<!-- claim-quality (subtree): 5965y1, 6tuqjh, 7tk051, 86gq2d, jy8h1x, llqd1n, lqanmt, mlwm3h, nk6c43 -->

> ⛔ **Bootstrap.** Leaves are canonical; this index, the volume index, and the entry-point are *derived* summaries and may suggest implications not supported by the leaves. Before forming any claim about results in this subtopic, load [`../claim-quality.md`](../claim-quality.md) (volume scope) and [`../../claim-quality.md`](../../claim-quality.md) (cross-cutting). Treat the summary text and Key Results entries below as routing only — qualifications and conditions live in the cited leaves and the claim-quality documents.

# Framework

The framework domain establishes the computational and conceptual machinery used throughout Vol 6 to derive nuclear masses, binding energies, and chemical properties from topological mutual impedance. It includes the mass defect summary table, the executive abstract, the full computational derivation chain (nucleon spacing, coupling constant, semiconductor analysis), and a chemistry translation guide.

## Key Results

| Result | Expression |
|---|---|
| Mass defect summary | $1/d_{ij}$ mutual impedance against CODATA for $Z=1$--$14$; errors $\le 0.027\%$ |
| Nucleon spacing from Axiom 1 | $d = 4\hbar/(m_p c) \approx 0.841$ fm |
| Intra-alpha distance | $D_{\text{intra}} = d\sqrt{8} \approx 2.379$ fm |
| Mutual coupling constant | $K = \frac{5\pi}{2} \cdot \frac{\alpha \hbar c}{1 - \alpha/3} \approx 11.337$ MeV$\cdot$fm |
| Topologic yield mass defect | $E_{\text{binding(max)}} = \alpha \cdot M_{\text{proton}} c^2 \approx 6.847$ MeV |
| Breakdown voltage | $V_{BR} = 6\,\alpha\hbar c / D_{\text{intra}} \approx 3.631$ MeV |
| Miller avalanche | $M = 1/(1 - (V_R/V_{BR})^n)$, $n = c_{\text{proton}} = 5$ |
| Complete nuclear mass | $M_{\text{nucleus}} = N_\alpha M_\alpha - \sum K/r_{ij} + M \cdot \sum f_{pp}\,\alpha\hbar c/r_{ij}$ |
| Helium-4 mass | $M(^{4}\text{He}) = (2m_p + 2m_n) - 6(K/(d_{\text{core}}\sqrt{8})) = 3727.379$ MeV |
| Bohr radius (topological) | $a_0 = l_{node}/\alpha_{\text{geom}} \approx 5.291 \times 10^{-11}$ m |
| Polar Conjugate TIR (Correction D) | $E_{val} = E_{base} \times (\text{core\_d\_knots} + 1)$; corrects $70\%$ underestimates to sub-$5\%$ up to $Z=86$ |

## Derivations and Detail

| Document | Contents |
|---|---|
| [Mass Defect Summary](mass-defect-summary.md) | Unnumbered summary table: topological vs CODATA masses for $Z=1$--$14$ |
| [Executive Abstract](executive-abstract.md) | Overview: alpha-series symmetric cores, asymmetric valency, golden ratio emergence, deterministic simulation |
| [Computational Mass Defect](computational-mass-defect/index.md) | Full derivation chain: reactive load model, circuit conventions, simulator, network analytics, spacing/coupling derivations, p-n junction, ABCD cascade, operating regimes, semiconductor analysis, radioactive decay |
| [Chemistry Translation Guide](chemistry-translation/index.md) | Mapping of quantum orbitals, Lewis dots, VSEPR, and semiconductor regime classification to AVE equivalents |
| [Ionization Energy Summary](./ionization-energy-summary.md) | First Ionization Energy table ($Z=1$--$14$, $Z=31$--$36$); Corrections A--D |
| [Polar Conjugate Bounding](./polar-conjugate-bounding.md) | Correction D derivation for heavy elements ($Z \geq 31$); $d^{10}$ TIR compartmentalization; valence energy scaling |
