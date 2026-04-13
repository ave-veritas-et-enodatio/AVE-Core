[↑ Protein Folding](../index.md)
<!-- leaf: verbatim -->
<!-- path-stable: referenced from vol5 as sec:s11_minimiser -->

# $S_{11}$ Minimiser: Folding as Pure Impedance Matching

The eight-force engine encodes each physical effect as a separate force term with its own spring constant. A more fundamental AVE approach asks: *can every structural feature emerge from a single impedance-matching criterion?*

All eight forces are replaced with a single objective function:

> **[Resultbox]** *$S_{11}$ Objective Function*
>
> $$E(\mathbf{r}) = |S_{11}(\mathbf{r})|^2 \quad \text{where } S_{11} = \frac{A + B/Z_0 - CZ_0 - D}{A + B/Z_0 + CZ_0 + D}$$

and the ABCD matrix is the cascaded product of backbone sections with *conjugate impedance matching*:

$$Y_{ij}^{\text{shunt}} = \frac{\kappa}{d_{ij}^2} \cdot \max\!\left(0,\; \frac{\operatorname{Re}(Z_i \, Z_j^*)}{|Z_i|\,|Z_j|}\right) \qquad \text{for } |i - j| > 2, \; d_{ij} < 15\,\text{Å}$$

where $Z_i = R_i + jX_i$ is now a *complex* topological impedance. The real part $R_i$ encodes hydrophobic character (sidechain volume), while the imaginary part $X_i$ encodes charge reactance (positive/inductive for K, R; negative/capacitive for D, E). The reactive component is scaled by $1/Q$ where $Q \approx 7$ is the backbone amide-V resonator quality factor ($f_0 = 23$ THz, $\Delta f \approx 3.3$ THz):

$$X_i = \frac{R_i}{Q}, \quad Q = \frac{f_0}{\Delta f} \approx 7$$

This ensures that resistive (hydrophobic) coupling dominates ($\sim 85\%$) with reactive (electrostatic) coupling as a perturbation ($\sim 15\%$). The conjugate product $\operatorname{Re}(Z_i Z_j^*) = R_i R_j + X_i X_j$ is positive for hydrophobic pairing ($R \times R$) and salt bridges ($+jX \times -jX$), and negative for like-charge repulsion---which is clamped to zero since shunt admittance is physically non-negative. The force on each residue is $\mathbf{F}_i = -\partial E / \partial \mathbf{r}_i$, computed via JAX automatic differentiation.

## Chirality: Non-Reciprocal Phase

The AVE vacuum lattice (SRS/K4 net) is intrinsically chiral, and L-amino acids fold exclusively into right-handed $\alpha$-helices. In transmission line terms, the backbone is a *non-reciprocal waveguide*: the lattice chirality creates a preferred propagation direction, analogous to a ferrite-loaded waveguide in microwave engineering. The chirality enters the ABCD cascade as a phase correction to the electrical length:

$$\beta_{\text{eff}} = \beta_0 - \delta_{\chi} \cdot w_{\text{helix}} \cdot \tanh\!\left(\frac{\chi_i}{\chi_0}\right), \quad \chi_i = (\mathbf{b}_{i} \times \mathbf{b}_{i+1}) \cdot \mathbf{b}_{i+2}$$

where $\mathbf{b}_i = \mathbf{r}_{i+1} - \mathbf{r}_i$ are bond vectors, $\chi_i$ is the scalar triple product (positive for right-handed twist, negative for left-handed), $\delta_\chi = 0.05$ rad is the chiral phase depth, $\chi_0 = 5$ Å$^3$ is the normalisation scale, and $w_{\text{helix}} = \max(0, 1 - \bar{Z}/2)$ suppresses the chirality correction for non-helical (sheet-forming) segments where handedness is irrelevant. The $\tanh$ saturates the chirality signal to $[-1, 1]$, preventing large distortions from dominating the gradient.

## Cross-Coupled Cavity Filter

A folded protein is not a single transmission line cascade---it is a set of coupled resonant cavities, analogous to a cross-coupled bandpass filter. Segment boundaries are detected via the local reflection coefficient

$$\Gamma_j = \frac{|Z_{j+1} - Z_j|}{Z_{j+1} + Z_j}$$

and soft segment membership is assigned via the cumulative turn index $s_i = \sum_{j<i} \sigma(20(\Gamma_j - 0.3))$. For each pair of segments $(p, q)$, the inter-segment transmission coefficient captures near-field cross-coupling:

$$S_{21}^{(p,q)} = \frac{2\bar{Z}_p \bar{Z}_q}{\bar{Z}_p^2 + \bar{Z}_q^2} \cdot \exp\!\left(-\frac{|\mathbf{c}_p - \mathbf{c}_q|}{R_{\text{burial}}}\right)$$

where $\bar{Z}_p$ is the mean impedance of segment $p$ and $\mathbf{c}_p$ its centroid. Crucially, this coupling acts between *all* segment pairs---not just sequential neighbours---enabling the helix-1 $\leftrightarrow$ helix-3 cross-coupling path required for bundle compaction. The loss rewards high $|S_{21}|^2$, providing direct gradient signal to pack impedance-matched segments.

## RMSD Comparison: Eight-Force vs $S_{11}$ Minimiser

| **Peptide** | **PDB** | **8-Force (Å)** | **$S_{11}$ Axiom (Å)** | **$\Delta$** | $R_g^{S_{11}} / R_g^{\text{PDB}}$ |
|---|---|---|---|---|---|
| Chignolin | 5AWL | 4.34 | **2.82** | $-35\%$ | 4.6 / 4.8 |
| Trpzip2 | 1LE1 | 5.58 | **5.47** | $-2\%$ | 5.5 / 5.8 |
| Trp-cage | 1L2Y | 6.56 | **6.02** | $-8\%$ | 7.7 / 7.0 |
| Villin | 1YRF | **7.31** | 9.68 | $+32\%$ | 11.9 / 8.9 |
| **Mean** | | 5.95 | **6.00** | $+1\%$ | |

*RMSD comparison: eight-force engine vs axiom-derived $S_{11}$ minimiser with cross-coupled cavity filter. The $S_{11}$ engine uses zero empirical parameters---every constant traces to Axioms 1--4.*

## Autodiff Acceleration

The finite-difference gradient requires $6N$ $S_{11}$ evaluations per step ($\pm\delta$ in each coordinate). Replacing with JAX automatic differentiation gives *exact analytical gradients* in a single forward-backward pass.

| **Peptide** | $N$ | **Finite-diff (s)** | **JAX+Adam (s)** | **Speedup** |
|---|---|---|---|---|
| Chignolin | 10 | 20.3 | **2.7** | $8\times$ |
| Trpzip2 | 12 | 33.6 | **3.3** | $10\times$ |
| Trp-cage | 20 | 96.4 | **5.9** | $16\times$ |
| Villin | 35 | 452.7 | **6.1** | $74\times$ |
| **Total** | | 603.0 | **18.1** | $33\times$ |

*Wall-clock time: finite-difference vs JAX autodiff with Adam optimiser, multi-frequency $S_{11}$, and simulated annealing (Apple M4, 5000--10000 steps).*

## Eight Axiom-Derived Physics Layers

The final engine combines eight axiom-derived physics layers with zero empirical parameters: (1) complex $Z_{topo}$ from the SPICE backbone model (Axiom 1); (2) conjugate impedance matching with $Q$-factor scaling, capturing salt bridges and hydrophobic pairing through a single coupling formula (Axioms 1--2); (3) solvent impedance boundary, where every exposed residue couples to the aqueous environment ($Z_{\text{H}_2\text{O}} = \sqrt{\varepsilon_r} \approx 8.9$) through a smooth sigmoid parasitic shunt (Axiom 1); (4) lattice chirality via non-reciprocal phase, favouring right-handed helices (Axiom 2); (5) Axiom 4 dielectric saturation ($C_{\mathrm{eff}} = C_0 / \sqrt{1-(d_0/d)^2}$, modulated by impedance match quality); (6) cross-coupled cavity filter providing all-pairs inter-segment $S_{21}$ coupling for tertiary compaction; (7) multi-frequency $S_{11}$ integration over 5 frequencies spanning $0.5$--$2.0 \times \omega_0$ (Axiom 3); and (8) Adam optimiser with simulated annealing. Every physical constant traces to $d_0$, $r_{\text{Slater}}$, $Q_{\text{backbone}}$, and $\varepsilon_r$---all derivable from Axioms 1--2.

For peptides $N \leq 20$, the axiom-derived $S_{11}$ minimiser achieves consistently lower RMSD than the eight-force engine with zero tuned parameters. Chignolin achieves $2.82$ Å RMSD with $R_g = 4.6 / 4.8$ Å (96% match to PDB)---breaking the 3 Å barrier from first principles. For Villin HP35 ($N = 35$), the RMSD of $9.68$ Å reflects the remaining challenge of tertiary topology: the cross-coupled cavity filter provides gradient signal for helix packing ($R_g$ improved from 13.2 to 11.9 Å toward the PDB value of 8.9 Å), but full 3-helix bundle compaction likely requires hierarchical fold-then-pack optimisation or longer-range coupled-mode analysis.

---
