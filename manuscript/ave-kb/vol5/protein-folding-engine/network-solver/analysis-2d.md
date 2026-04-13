[↑ Network Solver](./index.md)
<!-- leaf: verbatim -->

# Analysis: 2D Network

## Where the Network Wins

1. **Impedance matching**: The network $|S_{11}|^2$ is 15$\times$ lower than the cascade (0.075 vs 0.82), confirming that multi-path wave propagation provides fundamentally better impedance matching.
2. **Villin secondary structure**: 27% vs 24%---the first case where the 2D topology outperforms the 1D cascade on SS.
3. **JIT scalability**: Compilation time is nearly constant (1.8--2.3 s) regardless of $N$, because the vectorised Y-matrix assembly scales as $O(N^2)$ tensor operations rather than $O(N^2)$ traced Python loops.

## Where the Cascade Still Wins

1. **$R_g$ accuracy**: The 1D engine achieves 0.5--7.6% error; the 2D engine consistently over-compacts at $\sim$11%. The through-space coupling may need a size-dependent attenuation floor.
2. **SS for small proteins**: Trp-cage SS dropped from 34% to 6%. With $N=20$, the $N^2$ through-space TL segments create too many coupling paths relative to the $3N-1$ backbone segments, drowning the resonance structure.
3. **Speed**: 6$\times$ slower per optimisation step ($\sim$90 s vs 14 s) due to the $(3N-1) \times (3N-1)$ matrix solve at each frequency.

## Physical Interpretation

The 1D cascade has higher $|S_{11}|^2$ but better structural accuracy because its Y-shunt couplings, while physically approximate, preserve the standing-wave resonance structure that drives SS emergence. The 2D network has lower $|S_{11}|^2$ but the optimizer finds minima where the multi-path propagation "short-circuits" the backbone instead of setting up the precise resonance patterns needed for helices and sheets.

This suggests the next step is not adding more coupling paths, but improving how existing paths interact---enforcing the *resonance condition* that standing waves in the backbone must match the periodicity of secondary structure elements.

## Loss Decomposition

Impedance ($\Sigma|\Gamma_i|^2$) contributes $>99.8\%$; packing ($\Gamma_\text{pack}^2$) and steric ($\langle\Gamma_\text{steric}^2\rangle$) together contribute $<0.1\%$.

| **Protein** | $N$ | $\Sigma|\Gamma_i|^2$ | $\Gamma_\text{pack}^2$ | $\langle\Gamma^2_\text{ster}\rangle$ | imp/total |
|---|---|---|---|---|---|
| Chignolin | 10 | 3.29 | 0.0004 | 0.0003 | 99.98% |
| GB1 hairpin | 16 | 5.68 | 0.0049 | 0.0033 | 99.86% |
| Trp-cage | 20 | 7.43 | 0.0051 | 0.0007 | 99.92% |
| Villin HP35 | 35 | 15.01 | 0.0070 | 0.0015 | 99.94% |

Despite contributing $<0.1\%$ of the total loss, the packing and steric terms are *essential*: removing them causes structures to over-expand by $+25\%$ to $+211\%$. The packing term provides a direct gradient from $R_g$ to torsion angles that the weak contact-mediated gradient alone cannot replicate.

## Impedance Landscape of the Solvent Boundary

Each port's $S_{11}$ is referenced to its topological impedance:

$$Y_{0,i} = \frac{1}{|Z_\text{topo}(i)|}, \qquad Y_{0,i} \in [0.30,\; 0.95]$$

The solvent admittance is:

$$Y_\text{solvent} = \frac{\text{exposure}}{Z_\text{water}} = \frac{\text{exposure}}{\sqrt{\varepsilon_s}} \leq \frac{1}{\sqrt{78.4}} \approx 0.113$$

Since $Y_\text{solvent} < Y_{0,i}$ for *all 20 amino acids*, the solvent *under-loads* every port relative to its reference admittance. The Y-matrix gradient therefore favours *exposure*, not burial.

| **Class** | **Residue** | $|Z_\text{topo}|$ | $\Gamma_\text{exposed}$ |
|---|---|---|---|
| Hydrophobic | Gly | 0.304 | $-0.93$ |
| | Leu | 0.610 | $-0.87$ |
| | Trp | 0.895 | $-0.82$ |
| Polar | Ser | 0.766 | $-0.84$ |
| | Asn | 0.842 | $-0.83$ |
| Charged | Asp | 0.957 | $-0.80$ |
| | Lys | 0.644 | $-0.86$ |

---
