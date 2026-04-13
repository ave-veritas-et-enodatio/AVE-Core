[↑ Protein Folding](../index.md)
<!-- leaf: verbatim -->

# The 3D Gradient Descent Engine

The folding visualizations are produced by a purpose-built 3D gradient descent engine that translates the 1D topological impedance $Z_{topo}$ into local 3D spatial driving potentials. The engine operates on five simultaneous force channels:

## 0. Excluded-Volume Repulsion (Pauli Exclusion)

Non-bonded $C_\alpha$ pairs separated by $\geq 3$ residues experience a soft repulsive force when closer than the contact distance $d_0 = 3.8$ Å:

$$\mathbf{F}_{\text{excl},ij} = k_{\text{excl}} \, (d_0 - d_{ij}) \, \hat{\mathbf{r}}_{ij} \quad \text{for } d_{ij} < d_0,\; |i-j| \geq 3$$

with $k_{\text{excl}} = 30$. This prevents chain self-intersection and is the lattice-scale manifestation of Pauli exclusion: no two flux tube segments can occupy the same spatial node.

## 1. Backbone Integrity (Hooke Springs)

Sequential $C_\alpha$--$C_\alpha$ pairs are connected by stiff harmonic bond springs:

$$\mathbf{F}_{\text{bond},i} = k_{\text{bond}} \left( |\mathbf{r}_{i+1} - \mathbf{r}_i| - d_0 \right) \hat{\mathbf{r}}_{i,i+1}$$

where $d_0 = 3.8$ Å is the standard $C_\alpha$--$C_\alpha$ distance and $k_{\text{bond}} = 50$ is the dimensionless stiffness constant. This preserves the physical chain connectivity throughout the folding trajectory.

## 2. Bend-Angle Potentials (Z-Driven Torques)

At each interior residue $i$, the engine computes the cosine of the angle formed by the triplet $(i{-}1, i, i{+}1)$:

$$\cos\theta_i = \hat{\mathbf{u}}_{i-1,i} \cdot \hat{\mathbf{u}}_{i,i+1}$$

The target angle depends on the local topological impedance:

- If $Z_{topo} \leq 1.0$ (helix-former): the engine drives $\cos\theta$ toward $\sim 0.5$, corresponding to the $\sim 100^\circ$ bend angle of an ideal $\alpha$-helix, with strength $k_{\text{bend}} \propto 1/Z_{topo}$.
- If $Z_{topo} > 1.0$ (sheet-former): the engine drives $\cos\theta$ toward $\sim 0.87$ ($\sim 150^\circ$), with strength $k_{\text{bend}} \propto Z_{topo}$.

The gradient of the bending potential $U_{\text{bend}} = \tfrac{1}{2} k_{\text{bend}} (\cos\theta - \cos\theta_{\text{target}})^2$ applied to the flanking residues generates a genuine torque that either curls or straightens the backbone at each node.

## 3. Chirality Torque (Right-Handed Helical Driver)

For helical residues ($Z_{topo} \leq 1.0$), a cross-product torque enforces right-handed chirality:

$$\mathbf{F}_{\text{chiral},i+2} = -\kappa_{\text{twist}} \left( \hat{\mathbf{u}}_{i-1,i} \times \hat{\mathbf{u}}_{i,i+1} \right) \times \hat{\mathbf{u}}_{i+1,i+2}$$

This ensures that helical collapses converge to the biologically correct right-handed $\alpha$-helix geometry, consistent with the L-amino acid chirality established in Chapter 2.

## 4. Inter-Strand H-Bond Pairing ($\beta$-Sheet Driver)

For sheet-forming residues ($Z_{topo} > 1.5$) separated by $\geq 5$ positions along the sequence, an attractive spring drives non-local pairs toward the antiparallel $\beta$-sheet $C_\alpha$--$C_\alpha$ distance of $d_\beta = 4.7$ Å:

$$\mathbf{F}_{\text{H-bond},ij} = k_{\text{hb}} \, (d_{ij} - d_\beta) \, \hat{\mathbf{r}}_{ij} \quad \text{for } d_{ij} < 12\,\text{Å},\; Z_i,\, Z_j > 1.5$$

with $k_{\text{hb}} = 3.0$. Additionally, an antiparallel alignment torque penalises parallel strand orientations:

$$E_{\text{align}} = \tfrac{1}{2} k_{\text{align}} \left( \hat{\mathbf{d}}_i \cdot \hat{\mathbf{d}}_j + 1 \right)^2$$

where $\hat{\mathbf{d}}_i = (\mathbf{r}_{i+1} - \mathbf{r}_{i-1})/|\ldots|$ is the local chain direction. This drives $\beta$-hairpin formation: the chain folds back on itself with antiparallel backbone hydrogen bonds, which is the physical basis for $\beta$-sheet secondary structure.

## 5. Hydrophobic Mutual Coupling (Impedance Mismatch with Water)

Nonpolar sidechains present maximal impedance mismatch with the aqueous termination (water $\varepsilon_r \approx 80$). In transmission line terms, they act as high-reflection stubs: each nonpolar sidechain reflects energy back into the backbone rather than coupling to the solvent. When two such stubs are spatially adjacent, they share a low-loss microstrip channel, reducing the total stored energy. The result is a net attractive force between nonpolar residues:

$$\mathbf{F}_{\text{hp},ij} = k_{\text{hp}} \, h_i \, h_j \, (d_{ij} - d_{\text{core}}) \, \hat{\mathbf{r}}_{ij} \quad \text{for } h_i, h_j > 0.3$$

where $h_i \in [0, 1]$ is the hydrophobicity of residue $i$ (1.0 for nonpolar sidechains with zero H-bond donors/acceptors; 0.0 for charged/polar sidechains), $d_{\text{core}} = 6.0$ Å is the core packing distance, and $k_{\text{hp}} = 1.5$. The hydrophobicity scores are directly derived from the sidechain polar group census in the Ramachandran derivation section: residues with no polar groups (A, V, L, I, F) receive $h = 1.0$; those with multiple donors and acceptors (D, E, N, Q, K, R, S, T) receive $h = 0.0$.

## 6. Helical Backbone $i \to i{+}4$ H-Bond Springs (Feedback Coupling)

In a real $\alpha$-helix, the backbone NH group at position $i{+}4$ hydrogen-bonds to the CO group at position $i$, creating a *resonant feedback loop with period 4*. In transmission line terms, this is inter-turn coupling in a helical slow-wave structure: without it, the helix is merely a coiled wire; with it, the helix functions as a travelling-wave-tube (TWT)-like resonant cavity with characteristic group delay. The force drives helix-forming pairs toward the ideal pitch distance:

$$\mathbf{F}_{\text{hb},i,i+4} = k_{\text{hb}}^{\text{helix}} \, (d_{i,i+4} - d_{\text{hb}}) \, \hat{\mathbf{r}}_{i,i+4} \quad \text{for } Z_i, Z_{i+4} \leq 1.2$$

where $d_{\text{hb}} = 5.4$ Å is the ideal $C_\alpha(i)$--$C_\alpha(i{+}4)$ distance in an $\alpha$-helix and $k_{\text{hb}}^{\text{helix}} = 4.0$.

## 7. $S_{11}$ Feedback Gain Modulation (PID Error Signal)

The preceding forces operate in an open-loop fashion: each is computed independently from the current geometry. To close the loop between the 1D impedance model and the 3D engine, the local reflection coefficient $\Gamma(i)$ is computed at each backbone junction:

> **[Resultbox]** *$S_{11}$ Feedback Gain Modulation (PID Error Signal)*
>
> $$\Gamma_i = \frac{Z_{topo}^{(i+1)} - Z_{topo}^{(i)}}{Z_{topo}^{(i+1)} + Z_{topo}^{(i)}}, \qquad g_i = 1 + |\Gamma_i|^2$$

The gain factor $g_i \in [1, 2]$ multiplies all forces at residue $i$. Where $S_{11}$ is high (impedance mismatch), forces are amplified to drive more aggressive structural adjustment. Where $S_{11}$ is low (good match), forces relax---the chain is locally converged. In PID terms: $|\Gamma|^2$ is the proportional error, and the gain modulation is the controller output. This feedback is computed every 500 gradient steps to amortise cost.

## Numerical Stability

All forces are clamped to a maximum magnitude of 20.0 units per step (analogous to automatic gain control in a receiver chain), and the system is re-centered at its center of mass after each iteration to prevent translational drift. The learning rate $\eta = 0.01$ provides smooth convergence over $\sim 15{,}000$ steps. The chain is initialised with $Z_{topo}$-dependent geometry: helix-forming residues receive a helical seed ($100^\circ$/residue rotation, $1.5$ Å rise), while sheet-forming residues start in an extended zigzag conformation.

---
