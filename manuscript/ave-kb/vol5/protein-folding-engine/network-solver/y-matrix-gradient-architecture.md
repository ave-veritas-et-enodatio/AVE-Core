[↑ Network Solver](./index.md)
<!-- leaf: verbatim -->

# Y-Matrix Gradient Architecture

The self-consistent loss function ($f(\theta) = \lambda_\text{min}(S^\dagger S) + \Gamma_\text{pack}^2 + P_\text{steric}$) achieves excellent $R_g$ predictions across all fold classes. However, a first-principles audit reveals that the three terms contribute unequally to the optimizer gradient, with implications for the long-term architecture of the solver.

## Loss Decomposition

Empirical decomposition at convergence quantifies the contribution of each channel.

Loss decomposition at convergence. Impedance ($\Sigma|\Gamma_i|^2$) contributes $>99.8\%$; packing ($\Gamma_\text{pack}^2$) and steric ($\langle\Gamma_\text{steric}^2\rangle$) together contribute $<0.1\%$.

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

Since $Y_\text{solvent} < Y_{0,i}$ for *all 20 amino acids*, the solvent *under-loads* every port relative to its reference admittance. Increasing exposure adds more $Y_\text{solvent}$ to the diagonal, moving the port *closer* to $Y_{0,i}$ and *lowering* $|\Gamma_i|$. The Y-matrix gradient therefore favours *exposure*, not burial.

| **Class** | **Residue** | $|Z_\text{topo}|$ | $\Gamma_\text{exposed}$ |
|---|---|---|---|
| Hydrophobic | Gly | 0.304 | $-0.93$ |
| | Leu | 0.610 | $-0.87$ |
| | Trp | 0.895 | $-0.82$ |
| Polar | Ser | 0.766 | $-0.84$ |
| | Asn | 0.842 | $-0.83$ |
| Charged | Asp | 0.957 | $-0.80$ |
| | Lys | 0.644 | $-0.86$ |

**Consequence.** The pure Axiom 3 target $f(\theta) = \Sigma|\Gamma_i|^2$ prefers extended structures where every port is maximally solvent-exposed. This is the correct $S_{11}$ physics for the current boundary conditions, but it means compaction must come from an additional mechanism in the Y-matrix that outweighs the solvent-exposure benefit.

## Hydrophobic Contact Hypothesis (Disproven)

A natural hypothesis is that the missing compaction driver could be a **hydrophobic contact admittance** derived from Axiom 1. In transmission-line theory, the mutual admittance between two parallel conductors at close proximity scales as $1/\bar{Z}$:

$$Y_\text{hydro}(i,j) = \frac{1}{\bar{Z}(i,j)} \cdot g(d_{ij}), \qquad \bar{Z} = \sqrt{Z_i \cdot Z_j}$$

This coupling is strong ($Y \approx 1.6{-}3.3$ for low-$Z$ pairs), and introduces zero new parameters.

**Experimental result.** When implemented in the Y-matrix, this dense $N^2$ coupling *degraded* solver performance:

| **Protein** | **Without hydro** | **With hydro** | **Experiment** |
|---|---|---|---|
| Chignolin | $R_g = 5.4$ (+23%) | $R_g = 6.0$ (+36%) | 4.4 Å |
| Villin | $R_g = 9.1$ ($-5\%$) | $R_g = 11.2$ (+17%) | 9.6 Å |

Villin degraded from $-5\%$ to $+17\%$ error. The dense coupling flooded the Y-matrix gradient with $N^2$ pairwise terms, overwhelming the physically specific contact signals (H-bonds, $\beta$-sheets, salt bridges) with a uniform background. **The hydrophobic contact hypothesis was reverted.**

## Architecture Guard Rails

The above experiments motivate three guard rails for the solver architecture.

**Guard Rail 1: All three loss terms are the same operator.** The loss function

$$f(\theta) = \underbrace{\sum_i |\Gamma_i|^2}_{\text{Op 5--6: microscopic}} + \underbrace{|\Gamma_\text{pack}|^2}_{\text{Op 8: macroscopic}} + \underbrace{\langle\Gamma_\text{steric}^2\rangle}_{\text{Op 2: pairwise}}$$

consists of three applications of the *same* universal reflection operator (Axiom 3) at three different spatial scales. None of the three terms is ad hoc --- each is $\Gamma = (Z_2 - Z_1)/(Z_2 + Z_1)$ applied to a different impedance boundary:

- **Microscopic:** residue port vs. Y-matrix environment
- **Macroscopic:** actual $R_g$ vs. equilibrium cavity ($R_{g,\text{target}}$ from Axiom 4 packing fraction $P_C$)
- **Pairwise:** C$\alpha$ separation vs. exclusion radius $d_0$

**Guard Rail 2: Op 8 provides irreplaceable long-range gradient.** Y-matrix contacts are *short-range*: the proximity gate $g(d) = \sigma(\beta(D + d_0 - d))$ activates only for $d < 7.6$ Å. Without Op 8, the optimizer has no gradient signal to bring distant residues close enough for contacts to form. Removing Op 8 causes structures to over-expand by $+100\%$ to $+200\%$ (measured for Chignolin and Villin).

This is not an implementation deficiency --- it is a fundamental property of local Y-matrix gradients. The packing operator provides a *global* gradient from $R_g$ through all torsion angles simultaneously, which no local contact coupling can replace.

**Guard Rail 3: Small loss contribution $\neq$ unimportant.** At convergence, Op 8 contributes $<0.1\%$ of the total loss. This small value does *not* indicate irrelevance --- it indicates that the term has succeeded: $R_g \approx R_{g,\text{target}}$ means $\Gamma_\text{pack} \approx 0$. The packing term is small **because it is working**.

## Op2 Topological Crossing Penalty

The dual-formalism analysis predicts a fourth loss term from the Op2 crossing operator:

$$f(\theta) = \underbrace{\sum_i |\Gamma_i|^2}_{\text{Op 5--6}} + \underbrace{|\Gamma_\text{pack}|^2}_{\text{Op 8}} + \underbrace{\langle\Gamma_\text{steric}^2\rangle}_{\text{Op 9}} + \underbrace{c_{\min} \times \frac{P_C}{4}}_{\text{Op2 crossing}}$$

where $c_{\min}$ is the minimum crossing number of the backbone knot type.

**Implementation roadmap.**

1. **Knot detection.** After fold convergence, close the backbone trace (N-terminus to C-terminus) and compute $c_{\min}$ via the Alexander polynomial. Libraries: `topoly` or `KnotProt`.
2. **Crossing penalty.** Add $c_{\min} \times P_C/4$ to the total loss. This is a post-convergence correction, not a gradient-driving term (crossing number is not differentiable).
3. **Validation.** Compare predicted vs. observed crossing numbers across the PDB. Target: $c_{\min} = 0$ for $\sim 99\%$ of structures.

---
