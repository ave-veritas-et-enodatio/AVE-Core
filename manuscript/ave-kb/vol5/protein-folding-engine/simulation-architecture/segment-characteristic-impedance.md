[↑ Simulation Architecture](./index.md)
<!-- leaf: verbatim -->

# Layer 4: Full Backbone ABCD Cascade

The backbone is modelled as $3N{-}1$ cascaded transmission line sections---one per individual covalent bond (Ch. 2: "$L$-$C$ ladder from bond stiffness"). Each residue contributes three segments:

$$\underbrace{\text{N}_i \!-\! \text{C}_\alpha^i}_{d_0 = 1.46~\text{\AA}} \;\longrightarrow\; \underbrace{\text{C}_\alpha^i \!-\! \text{C}_i}_{d_0 = 1.52~\text{\AA}} \;\longrightarrow\; \underbrace{\text{C}_i \!-\! \text{N}_{i+1}}_{d_0 = 1.33~\text{\AA}}$$

giving a total of $3N{-}1$ sections (the last residue lacks the inter-residue C--N bond).

## Segment Impedances from Nuclear Mass and Shared Electrons

The characteristic impedance of each segment uses the *full* impedance formula from `place_nuclear_defect` in `bond_energy_solver.py`: local permeability $\mu \propto m_{\text{atoms}}$ (mass is inductance, B-field, repulsion) and local permittivity $\varepsilon \propto n_e$ (shared electrons, E-field, attraction):

> **[Resultbox]** *Segment Characteristic Impedance*
>
> $$Z_\text{seg} = \sqrt{\frac{\mu}{\varepsilon}} = \sqrt{\frac{m_\text{Da}}{n_e}}$$

where $m_\text{Da}$ is the total mass (in Daltons) of the two bonded atoms.

| **Bond** | **Type** | $m_\text{Da}$ | $n_e$ | $Z = \sqrt{m/n_e}$ |
|---|---|---|---|---|
| N--C$_\alpha$ | single | 26 | 2 | 3.606 |
| C$_\alpha$--C | single | 24 | 2 | 3.464 |
| C--N (peptide) | partial double | 26 | 3 | 2.944 |

The 22% impedance mismatch at each peptide bond junction is the protein-scale analog of a semiconductor band-gap junction. Additionally, the N atom's higher mass (14 Da vs 12 Da for C) breaks the N--C$_\alpha$ / C$_\alpha$--C symmetry by 4.1%, creating a subtle chiral asymmetry.

## Per-Residue $\mu$ Enhancement

Each sidechain contributes local mass to the backbone, enhancing $\mu$ at its C$_\alpha$ position---the protein-scale analog of `place_nuclear_defect`:

$$Z_\text{eff}^{(i)} = Z_\text{seg} \times \sqrt{1 + R_i^2}$$

where $R_i = |Z_{\text{topo},i}|$ encodes the sidechain mass via $L = m/\xi^2$. Glycine ($R = 0.30$) receives a 4% boost; tryptophan ($R = 0.89$) receives 34%. This creates sequence-dependent impedance variation that drives tertiary folding.

## Lossy Propagation (Strain Loss)

The ABCD matrix uses a *complex* propagation constant $\gamma = \alpha + j\beta$:

$$\alpha_i = \frac{|d_i - d_0^{(i)}|}{d_0^{(i)}}, \qquad \beta_i = \omega \cdot \frac{d_i}{d_0^{(i)}} - \delta_\chi^{(i)}$$

where $d_i$ is the actual bond distance and $d_0^{(i)}$ is the target length from `BACKBONE_BONDS`. The strain loss $\alpha$ *breaks the periodicity* of $\cos\beta\ell$: at $d = d_0$, $\alpha = 0$ (lossless, minimum $S_{11}$); at $d \neq d_0$, $\alpha > 0$ (lossy, $S_{11}$ increases monotonically). This is confirmed by a pure $S_{11}$ diagnostic (commit `9fc8f9c`): the C--N peptide bond *emerges* at $1.38 \pm 0.10$ \AA\ (target 1.33, 4% off) without any geometric penalty.

The ABCD matrix for each lossy section is:

$$\mathbf{T}_i = \begin{pmatrix} \cosh\gamma\ell & Z_c\sinh\gamma\ell \\ \sinh\gamma\ell/Z_c & \cosh\gamma\ell \end{pmatrix} \cdot \begin{pmatrix} 1 & 0 \\ Y_i & 1 \end{pmatrix}$$

which reduces to the lossless case ($\cos/\sin$) when $\alpha = 0$. The sidechain shunt admittance $Y_i$ is applied only at C$_\alpha$ junctions (where R-groups attach). The total cascade $\mathbf{T} = \prod_{i=0}^{3N-2} \mathbf{T}_i$ is computed via `jax.lax.fori_loop` for $O(N)$ scaling.

The port reflection coefficient is:

$$S_{11} = \frac{A + B/Z_0 - CZ_0 - D}{A + B/Z_0 + CZ_0 + D}$$

---
