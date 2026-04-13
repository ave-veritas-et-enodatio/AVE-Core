[↑ Simulation Architecture](./index.md)
<!-- leaf: verbatim -->

# Tier 3: Physics Layers (Layers 3, 3b, 3c)

The loss function (Eq. $\ref{eq:total\_loss}$) consists of eight axiom-derived physics layers evaluated in sequence. Each layer contributes either to the $S_{11}$ cascade loss, the bond/steric penalty, or the port coupling loss.

Layers 1--2 (conjugate impedance matching and Axiom 4 dielectric saturation) are documented in [Dielectric Saturation Amplification](./dielectric-saturation-amplification.md).

## Layer 3: Solvent Impedance Boundary

Every residue couples to the aqueous environment through a parasitic shunt to ground:

$$Y_i^{\text{solvent}} = \frac{e_i}{Z_{\mathrm{H_2O}}}, \qquad e_i = \operatorname{clip}\!\left(1 - \frac{n_i}{n_\text{max}},\; 0,\; 1\right)$$

where $e_i$ is the fractional exposure (1 = fully solvent-exposed, 0 = fully buried), $n_i$ is the smooth neighbour count:

$$n_i = \sum_{|j-i|>2} \sigma\!\left(\beta_\text{burial}(R_\text{burial} - d_{ij})\right)$$

and $n_\text{max} = \max(N/3, 4)$. This creates a penalty for exposing hydrophobic residues: their high $R_i$ stubs reflect energy back into the backbone, but when exposed, the solvent shunt drains that energy to ground. Burial eliminates the shunt, reducing $S_{11}$.

## Layer 3b: Backbone H-Bond Coupling (TL Node Mutual Inductance)

Backbone hydrogen bonds are modelled as mutual inductance between non-adjacent transmission line nodes. The coupling uses the distance between backbone N and C atoms---these are *circuit nodes* in the ABCD cascade, not a proxy for O$\cdots$H distance.

**EE rationale.** In a transformer, the coupling coefficient $k$ depends on the distance between *coil centres*, not between magnetic field line endpoints. Analogously, the O and H atoms are field endpoints (dipole tips of the C$=$O and N--H bonds) while N$_i$ and C$_j$ are the circuit nodes where $Y_\text{shunt}$ enters the ABCD cascade. Testing with actual O$\cdots$H distances reduced SS from 24% to 15%, confirming that backbone node separation is the correct coupling variable.

The directional coupling admittance is:

$$Y_{ij}^\text{HB} = \lambda_\text{rama} \cdot \kappa_\text{HB} \cdot \cos\theta_{ij} \cdot \exp(-d_{ij}^\text{NC}/d_0) \cdot \sigma_\text{prox}$$

where $d_{ij}^\text{NC} = ||\mathbf{r}_{N_i} - \mathbf{r}_{C_j}||$ is the backbone node separation, $\cos\theta_{ij} = \hat{\mathbf{d}}_i \cdot (-\hat{\mathbf{s}}_{ij})$ with $\hat{\mathbf{d}}_i = (\mathbf{r}_{N_i} - \mathbf{r}_{C_\alpha^i})/||\cdot||$ being the TL current direction at node $i$, and $\sigma_\text{prox}$ is a sigmoid proximity filter. Only pairs with $|i-j| > 2$ are included.

The coupling strength is $\kappa_\text{HB} = 1/(2Q) = 1/14$, which equals the transformer coupling coefficient $\kappa_\text{dipole} = \sqrt{Z_\text{C=O} \cdot Z_\text{N-H}}/Z_\text{bb} \approx 0.81$ modulated by the resonance quality factor $2Q$:

$$Z_\text{C=O} = \sqrt{28/4} = 2.65, \quad Z_\text{N-H} = \sqrt{15/2} = 2.74, \quad Z_\text{bb} = \tfrac{1}{3}(Z_{\text{N-C}_\alpha} + Z_{\text{C}_\alpha\text{-C}} + Z_\text{C-N}) \approx 3.34$$

where each bond impedance $Z = \sqrt{m_\text{Da}/n_e}$ follows the same $\sqrt{\mu/\varepsilon}$ operator used at nuclear scale by the bond energy solver.

## Layer 3c: Adjacent Peptide-Plane Coupling

Each peptide unit defines a plane containing the C$_\alpha^i$--C$_i$--N$_{i+1}$ backbone triangle. Adjacent peptide planes are coupled LC oscillators (Axiom 1), and their mutual inductance depends on relative orientation:

$$M_{i,i+1} = \kappa_\text{HB} \cdot \cos(\hat{\mathbf{n}}_i \cdot \hat{\mathbf{n}}_{i+1})$$

where

$$\hat{\mathbf{n}}_i = \frac{(\mathbf{r}_{C_\alpha^i} - \mathbf{r}_{C_i}) \times (\mathbf{r}_{C_i} - \mathbf{r}_{N_{i+1}})}{||(\mathbf{r}_{C_\alpha^i} - \mathbf{r}_{C_i}) \times (\mathbf{r}_{C_i} - \mathbf{r}_{N_{i+1}})||}$$

is the peptide plane normal.

Parallel planes (cos $\approx +0.8$, $\alpha$-helix geometry) increase $Y_\text{shunt}$, lowering $|S_{11}|^2$. Alternating planes (cos $\approx -0.6$, $\beta$-sheet geometry) provide weaker coupling. Random orientations average to zero. This creates a natural gradient toward secondary structure without empirical basin coordinates.

The coupling enters $Y_\text{shunt}$ at positions $i+1$ (the C$_\alpha$ between two coupled planes):

$$Y_\text{peptide}^{(i)} = \lambda_\text{rama} \cdot \kappa_\text{HB} \cdot (\hat{\mathbf{n}}_i \cdot \hat{\mathbf{n}}_{i+1}), \qquad i = 1, \ldots, N{-}2$$

No new constants are introduced: $\kappa_\text{HB} = 1/(2Q)$ and $\lambda_\text{rama} = 2Z_0 \cdot (2r_{C_\alpha}/d_0)$ are both previously derived.

---
