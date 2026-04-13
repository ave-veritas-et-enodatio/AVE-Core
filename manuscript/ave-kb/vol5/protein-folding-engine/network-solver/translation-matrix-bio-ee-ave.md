[↑ Network Solver](./index.md)
<!-- leaf: verbatim -->

# Translation Matrix: Biology $\to$ EE $\to$ AVE

Table provides the complete mapping between biological, electrical engineering, and AVE axiomatic terminology. Any reader familiar with *one* column can reconstruct the solver in their native domain.

> → Primary: [Translation: Protein Solver Domain](../../common/translation-protein-solver.md) — full Bio $\leftrightarrow$ EE $\leftrightarrow$ AVE mapping table (source: `common/translation_protein_solver.tex`)

## Multi-Path Transmission Line Architecture

The v4/v7 solver models h-bond and contact interactions as mutual admittances in the backbone Y-matrix. While the *topology* is correct (contacts connect node $i$ to node $j$, not to ground), the coupling *values* were dimensionless coefficients. First-principles analysis using Operator 4 corrects this.

### H-Bond Impedance (Operator 4 + Axiom 4)

Operator 4 gives the local impedance at distance $r$ from a covalent saturation centre:

$$Z(r) = \frac{Z_0}{\bigl(1 - (d_\text{sat}/r)^2\bigr)^{1/4}}$$

At the H-bond detection distance $r = D_\text{HB} = 2.24$ Å with $d_\text{sat} = d_\text{C-N} = 1.33$ Å:

$$A = \frac{d_\text{sat}}{D_\text{HB}} = 0.594, \qquad Z_\text{HB} = Z_\text{bb} \times \frac{1}{(1 - 0.353)^{1/4}} \approx 1.115\,Z_\text{bb} \approx 3.72$$

This places H-bonds in **Regime II** (nonlinear, $A \in [0.121, 0.866]$) --- the same regime as nuclear forces at the meson exchange range.

### Key Insight: Near-Perfect Impedance Match

$Z_\text{HB} \approx Z_\text{bb}$ --- the H-bond is *nearly impedance-matched* to the backbone ($\Gamma = 0.027$, $T^2 = 0.999$). The weakness of H-bonds does not come from impedance mismatch but from three *geometric gating* factors:

1. **Directional coupler angle** $\cos\theta_\text{donor}$: N-H must point toward C=O.
2. **Yukawa decay** $\exp(-d/d_0)$: exponential attenuation.
3. **Proximity threshold**: sigmoid cutoff at $d > D_\text{HB}$.

### $\pi$-Equivalent TL Model

Each H-bond is modelled as a TL segment with impedance $Z_\text{HB}$ and propagation parameter $\gamma\ell = (\alpha + j\beta) \times d_\text{NC}/d_0$, where $\alpha = 1/Q$ and $\beta = 2\pi/Q$. The $\pi$-equivalent admittance is

$$y_\text{HB}(i,j) = \frac{1}{Z_\text{HB}\,|\!\sinh(\gamma\ell)|} \times \cos\theta_\text{donor} \times g_\text{proximity}$$

which has correct admittance dimensions $[1/\text{impedance}]$, resolving the dimensional inconsistency of the previous model.

### Regime Map

| $r$ (Å) | $A = d_\text{sat}/r$ | $S(r)$ | $Z/Z_0$ | $\Gamma$ | Regime |
|---|---|---|---|---|---|
| 1.33 (covalent) | 1.000 | 0 | $\infty$ | $+1.00$ | Saturated |
| 2.00 | 0.665 | 0.75 | 1.157 | $+0.07$ | II |
| **2.24 (H-bond)** | **0.594** | **0.80** | **1.115** | **$+0.03$** | **II** |
| 3.80 (C$_\alpha$ sep.) | 0.350 | 0.94 | 1.033 | $+0.02$ | II |

## Sidechain Orbitals: Nearly Reactive Resonant Tanks

Each amino acid sidechain has topological impedance $Z_\text{topo}$ with both reactive (imaginary) and resistive (real) components.

**Reactive component (Axiom 1).** $Z_R = \sqrt{L_R/C_R}$ where $L_R$ encodes kinetic energy and $C_R$ encodes potential energy. For ground-state conformations, $Q_\text{SC} \to \infty$ because there is no lower state to decay into.

**Resistive component (Axiom 2).** $S(r) = \sqrt{1 - (A/A_y)^2}$ requires every system to have a yield threshold; a purely reactive tank ($Q = \infty$, $R = 0$) would require $S = 1$ everywhere. Sidechains dissipate through:

1. **Bend radiation** at C$_\alpha$--C$_\beta$: $R_\text{bend} = 1/Q \approx 0.135$.
2. **H-bond coupling**: $R_\text{HB} = \kappa_\text{HB} Z_\text{bb}^2 \approx 0.75$.
3. **Solvent coupling**: Debye relaxation of the water shell provides resistive termination.

**Implication.** If sidechains were purely reactive, they would ring indefinitely and the protein would never fold. Folding occurs *because* the tanks have finite $Q$: energy dissipates until the system reaches the minimum-reflection eigenstate. Sidechain rotamer precision gives diminishing returns compared to fixing the backbone topology, since the dissipation that drives folding lives primarily in the backbone network.

## Engine Architecture: Universal Operators Applied to Protein Folding

The protein fold engine uses eight universal operators (documented in Volume II, Ch. 1) with zero domain-specific modifications. Universal operator catalog applied to protein folding.

| **Op** | **Operator** | **Axiom** | **Protein instantiation** |
|---|---|---|---|
| 1 | $Z = \sqrt{\mu/\varepsilon}$ | Ax. 1 | $Z_\text{topo}$ per residue |
| 2 | $S(A) = \sqrt{1-A^2}$ | Ax. 4 | Pauli steric exclusion |
| 3 | $\Gamma = (Z_2-Z_1)/(Z_2+Z_1)$ | Ax. 3 | Inter-residue reflection |
| 4 | $U(r) = -(K/r)(T^2-\Gamma^2)$ | Ax. 1--4 | H-bond impedance ($Z_\text{HB}$) |
| 5 | $[S] = (I+Y/Y_0)^{-1}(I-Y/Y_0)$ | Ax. 3 | Backbone $Y$-matrix $\to$ S-params |
| 6 | $\lambda_\text{min}(S^\dagger S)$ | Ax. 3 | Fold eigenstate |
| 7 | FFT($Z_\text{seq}$) | DSP | $\alpha/\beta$ secondary structure ID |
| **8** | **$\Gamma_\text{pack}$** | **Ax. 3+4** | **Hydrophobic collapse** |
| **Op2$_\times$** | **$\delta E = c_{\min} \times 2\pi\alpha \times E$** | **Ax. 3** | **Topological crossing penalty** |

### Self-Consistent Loss Function

The total target balances three additive, axiom-derived terms:

$$f(\theta) = \underbrace{\lambda_\text{min}(S^\dagger S)}_{\text{microscopic (Op 6)}} + \underbrace{\Gamma_\text{pack}^2}_{\text{macroscopic (Op 8)}} + \underbrace{P_\text{steric}}_{\text{geometric (Op 2)}}$$

All three terms are bounded $[0,1]$ and self-balancing: no relative weight parameters are required.

### Validation: GB1 Hairpin ($\beta$-sheet)

Before the macroscopic boundary condition (Op 8), the 16-residue GB1 hairpin was predicted at $R_g = 12.2$ Å ($+96\%$ error). After: $R_g = 5.6$ Å ($-10\%$ error vs. experimental 6.2 Å). The packing reflection provides the far-field boundary condition that the microscopic eigenvalue alone cannot impose.

---
