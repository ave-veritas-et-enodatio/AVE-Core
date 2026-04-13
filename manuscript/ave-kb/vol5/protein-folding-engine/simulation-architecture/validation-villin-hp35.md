[↑ Simulation Architecture](./index.md)
<!-- leaf: verbatim -->

# Validation: Villin HP35

Villin headpiece subdomain HP35 (PDB: 1VII, 35 residues, three-helix bundle) is a standard benchmark for protein folding algorithms. The engine was upgraded from C$_\alpha$-only to full N--C$_\alpha$--C backbone (3 atoms per residue, Upgrade 7b), enabling proper $\phi/\psi$ dihedral computation. Results with 10,000 Adam steps at $\eta = 2 \times 10^{-3}$:

| **Metric** | **Value** | **Expected** |
|---|---|---|
| Loss | $377 \to 3.53$ | Convergent |
| $R_g$ | 5.1 \AA | 8--10 \AA |
| End-to-end | 14.9 \AA | $<30$ \AA --- Pass |
| $\phi$ chirality | 100% negative | Pass |
| $\alpha$-helix | 64% | $\sim$60% --- Pass |
| $\beta$-sheet | 24% | --- |
| **Total SS** | **88%** | $>70\%$ --- Pass |

The full backbone representation enforces four constraint layers, each with an axiom-derived penalty weight:

| **Layer** | **Weight** | **Value** | **Derivation** |
|---|---|---|---|
| Bond stretch | $\lambda_\text{bond} = 2Z_0$ | 2.000 | Axiom 1 (backbone $Z$) |
| Angle bend | $\lambda_\text{angle} = 2(r_{C_\alpha}/d_0)^2$ | 0.400 | Geometric lever |
| $\omega$ planarity | $\lambda_\omega = 2\,d_{\text{N--C}_\alpha}/d_{\text{C--N}}$ | 2.195 | Bond stiffness ratio |
| $\phi/\psi$ Rama | $\lambda_\text{rama} = 2(2r_{C_\alpha}/d_0)$ | 1.789 | Pauli packing fraction |
| Steric exclusion | $\lambda_\text{steric} = \lambda_\text{bond} \cdot d_0/r_{C_\alpha}$ | 4.471 | Pauli $\gg$ Hooke (Ch. 2 Eq. 14) |
| Port coupling | $\max(0, \mathcal{L}_\text{port})$ | --- | Bounded $S_{21} \in [0,1]$ |

The packing fraction $2r_{C_\alpha}/d_0 = 0.895$ is noteworthy: it is the protein-scale analog of the electromagnetic packing fraction $P_C = 8\pi\alpha \approx 0.183$, reflecting the scale invariance of the impedance coupling structure (Axiom 1).

The engine correctly enforces backbone chirality (100% negative $\phi$).

## Upgrade 10: 5-Atom Backbone Steric (Replaces Ramachandran)

Earlier versions used an explicit Ramachandran potential with pre-defined $\alpha/\beta$ basin coordinates. While effective (94% SS), this was an *artificial constraint*: the basin locations were empirical inputs, not derived from the axioms.

The Ramachandran basins are *consequences* of steric clashes between backbone atoms---not a fundamental potential. The correct first-principles approach models these clashes directly using the **5-atom backbone**: N, C$_\alpha$, C, O (carbonyl), H (amide), plus C$_\beta$ (sidechain stub).

**Atom placement.** O and H positions are fully determined by the peptide plane geometry---no new DOFs. To maintain a strict zero-parameter theory, the empirical crystallographic averages (C=O $\approx 1.23$ \AA, N--H $\approx 1.01$ \AA) are discarded in favour of the pure first-principles predictions from the 1D soliton bond solver, alongside exact $sp^2$ trigonal planar angles:

$$\begin{align}
\mathbf{r}_{\text{O}_i} &= \mathbf{r}_{C_i} + 1.121\,\hat{\mathbf{e}}_O \qquad (120.0^\circ \text{ from } C_\alpha\text{--}C \text{ in peptide plane}) \\
\mathbf{r}_{\text{H}_i} &= \mathbf{r}_{N_i} + 0.817\,\hat{\mathbf{e}}_H \qquad (120.0^\circ \text{ from } C\text{--}N \text{; Pro excluded})
\end{align}$$

This forces the entire Ramachandran steric landscape to emerge natively from Axioms 1 and 2, without a single empirical geometric input.

**Steric exclusion radii.** The hard-sphere exclusion is the LJ repulsive distance $\sigma_{ij} = (r_i + r_j) / 2^{1/6} \approx 0.891 \times (r_i + r_j)$, not the raw VdW sum (which is the zero-crossing, not the wall).

**Bonded-pair masking.** O/H cross-terms use $|i-j| \geq 2$ (O$_i$--H$_{i+1}$ is bonded at 1.50 \AA\ through O=C--N--H). C$_\beta$ uses $|i-j| \geq 1$ (stub, not main chain).

## Upgrade 8: H-Bond Mutual Inductance

Directional hydrogen-bond coupling uses N$_i$--C$_j$ distance as proxy:

$$Y_{\text{HB}}^{ij} = \lambda_\text{rama}\, \kappa_\text{HB}\, \cos\theta\, e^{-d_{\text{NC}}/d_0}\, \sigma(D_\text{HB} + d_0 - d_{\text{NC}})$$

where $\kappa_\text{HB} = 1/(2Q) = 1/14$ and $\cos\theta$ provides angular dependence.

**Current status:** The loss function is $S_{11}$ + C$_\alpha$ steric + 5-atom backbone steric + port coupling + NEXT cross-talk + H-bond. No Ramachandran basin penalties are needed.

**JIT-compiled pairwise kernel.** The $O(N^2)$ pairwise distance matrix---required by steric, port coupling, and H-bond loss terms---is evaluated via a vectorized broadcast kernel in `regime_2_nonlinear/protein_fold.py`. The kernel replaces the original Python loop with `jnp.triu_indices`-based pairwise broadcasting, achieving $\sim$1500$\times$ speedup for nuclear-scale kernels and $\sim$3000$\times$ for molecular-scale kernels under JAX `@jit`. The cost function delegates to `universal_pairwise_energy_jax` for all energy evaluations, maintaining strict Tier 1 operator compliance.

---
