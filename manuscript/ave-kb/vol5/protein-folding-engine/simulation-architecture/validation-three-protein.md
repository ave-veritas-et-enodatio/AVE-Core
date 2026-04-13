[↑ Simulation Architecture](./index.md)
<!-- leaf: verbatim -->

# Validation: Three-Protein Test

The engine was validated on four proteins spanning 20--76 residues with random torsion-angle initialisation (no structural seed), Adam($\eta = 2 \times 10^{-3}$) with simulated annealing ($T_0 = 0.05$), and 5-start selection.

## 1D Cascade Engine Validation (Final)

$R_g^{(\eta_\text{eq})}$ is the equilibrium radius from $\eta_\text{eq} = P_C(1-\nu)$. All simulations start from random $(\varphi, \psi)$ --- no structural bias.

| **Protein** | $N$ | Steps | $R_g$ (\AA) | $R_g^{(\eta_\text{eq})}$ | Err | H% | E% |
|---|---|---|---|---|---|---|---|
| Trp-cage | 20 | 20k | 7.31 | 7.04 | **3.8%** | 17 | 17 |
| Villin HP35 | 35 | 20k | 8.44 | 8.48 | **0.5%** | 12 | 12 |
| GB1 hairpin | 56 | 50k | 9.37 | 9.92 | **5.5%** | 9 | 13 |
| Ubiquitin | 76 | 100k | 10.14 | 10.98 | **7.6%** | 12 | 15 |

## Derived Equilibrium Packing

The equilibrium packing fraction is:

$$\eta_\text{eq} = P_C \times (1 - \nu_\text{vac}) = 8\pi\alpha \times \frac{5}{7} \approx 0.1310$$

giving $R_g^{(\eta_\text{eq})} = r_{C_\alpha} \cdot (N/\eta_\text{eq})^{1/3} \cdot \sqrt{3/5}$. The same Poisson ratio $\nu = 2/7$ that sets $\sin^2\theta_W = 2/9$, $\alpha_s = \alpha^{3/7}$, CKM mixing, and PMNS oscillation angles now correctly predicts protein equilibrium size to $\lesssim 8\%$ for all four proteins.

Key observations:

1. **Equilibrium size**: $R_g$ matches $\eta_\text{eq}$-predicted values to 0.5--7.6% across 20--76 residues (no size fitting).
2. **Secondary structure**: Both helix (H) and sheet (E) emerge from first-principles coupling --- no empirical basin coordinates. Mean SS $\approx 26\%$ across all proteins.
3. **Bond geometry**: Bond lengths are exact by construction (torsion-angle parameterisation: 0.000 \AA\ std).
4. **Scalability**: Larger proteins require more optimisation steps (20k for $N=20$ vs. 100k for $N=76$).

## 5-Atom Backbone Steric Validation (Villin HP35, $N=35$)

| **Engine Version** | $R_g$ (\AA) | Err($\eta_\text{eq}$) | RMSD (\AA) | SS% |
|---|---|---|---|---|
| Old Ramachandran (lookup) | 8.42 | 0.8% | 7.25 | 94% |
| **5-atom steric (Axiom 2)** | **8.47** | **0.1%** | **6.22** | 3% |

**Derived equilibrium packing.** $\eta_\text{eq} = P_C(1 - \nu_\text{vac}) = 8\pi\alpha \times 5/7 \approx 0.1310$, giving $R_g^{(\eta_\text{eq})} = r_{C_\alpha} (N/\eta_\text{eq})^{1/3} \sqrt{3/5} = 8.48$ \AA.

Key observations: (1) $R_g = 8.47$ matches prediction to 0.1%; (2) RMSD 6.22 \AA\ is 14% better than the Ramachandran engine; (3) SS = 3% indicates that steric exclusion constrains forbidden regions but does not *drive* helix formation (the attractive LJ well is needed); (4) bond lengths exact by construction.

**Critical correction: coupled 2D Ramachandran basins.** The Ramachandran basins arise from Pauli steric exclusion (Axiom 2) acting *simultaneously* on both $\phi$ and $\psi$. An earlier implementation penalised $\phi$ and $\psi$ independently:

$$V_\text{rama}^\text{(old)} = \min(\Delta\phi_\alpha^2, \Delta\phi_\beta^2) + \min(\Delta\psi_\alpha^2, \Delta\psi_\beta^2)$$

This allows $(\phi=-60^\circ,\; \psi=130^\circ)$ with *zero penalty* --- a sterically forbidden region between the $\alpha$ and $\beta$ islands. The correct formulation computes 2D distance to the nearest coupled basin:

$$V_\text{rama}^\text{(2D)} = \min\!\bigl(\Delta\phi_\alpha^2 + \Delta\psi_\alpha^2,\;\; \Delta\phi_\beta^2 + \Delta\psi_\beta^2\bigr) / \sigma^2$$

This forces each residue to commit to a single consistent $(\phi,\psi)$ basin. Adding sequence-dependent basin asymmetry from the per-residue impedance $|Z_\text{topo}|$ yields the full Ramachandran potential:

$$V_\text{rama}^{(i)} = \min\!\bigl(|z_i| \cdot d_\alpha^2,\;\; d_\beta^2 / |z_i|\bigr) / \sigma^2$$

The basin weights $w_\alpha = |z_i|$ and $w_\beta = 1/|z_i|$ arise from impedance matching (Axiom 1):

- **$\alpha$-helix**: tight $100^\circ$/residue turns $\to$ high conformational impedance $\to$ large sidechains are mismatched (high $S_{11}$)
- **$\beta$-sheet**: extended backbone $\to$ low conformational impedance $\to$ large sidechains fit without mismatch

This is the *same* impedance matching that determines boson masses in the electroweak sector: $M_W$ from $Z_\text{load}$ at saturation, $M_Z/M_W = 3/\sqrt{7}$ from the compliance ratio. The coupling $\kappa_\text{HB} = 1/(2Q)$ mirrors $\lambda_\text{Higgs} = 1/(2N_{K4})$ --- critical coupling $\kappa = 1/2$ divided by the mode count. The result: 55% $\alpha$-helix (approaching the experimental $\sim$60%), with low-$|Z|$ residues (Ala, Leu, Val, Lys) correctly adopting $\alpha$ and high-$|Z|$ residues (Asp, Phe, Asn) adopting $\beta$.

## Upgrade 8: Backbone H-Bond and Peptide-Plane Coupling

To address $\alpha/\beta$ selectivity, the engine implements two physically-derived coupling mechanisms (Layers 3b and 3c):

1. **H-bond backbone-node coupling** (Layer 3b): Directional mutual inductance between non-adjacent N$_i$ and C$_j$ atoms. These are TL circuit nodes, not dipole endpoints.
2. **Adjacent peptide-plane coupling** (Layer 3c): Mutual inductance between adjacent peptide planes, proportional to $\cos(\hat{\mathbf{n}}_i \cdot \hat{\mathbf{n}}_{i+1})$. No empirical basin coordinates---secondary structure emerges from plane alignment.

Both use $\kappa_\text{HB} = 1/(2Q) = 1/14$ from the amide-V quality factor, requiring zero new constants.

**Current status:** With torsion-angle parameterisation (NERF), bond lengths are enforced exactly by construction (0.000 \AA\ std) and the loss function reduces to $S_{11}$ + steric + backbone H-bond + peptide-plane + port coupling + NEXT cross-talk. No bond, angle, or $\omega$ penalties are needed.

## Y-Shunt Component Balance

Y-shunt component balance: Trp-cage ($N=20$) vs. Ubiquitin ($N=76$). The peptide-plane coupling (the *only* term that drives SS) goes from 14.6% to $-3\%$.

| **Component** | **Trp-cage ($N\!=\!20$)** | **Ubiquitin ($N\!=\!76$)** |
|---|---|---|
| Hydrophobic coupling | 63% | 77% |
| H-bond | 10% | 13% |
| **Peptide-plane (SS)** | **14.6%** | **$-3\%$** |
| Tertiary | 12% | 13% |
| $\cos(\hat{n}\cdot\hat{n})$ mean | $+0.166$ | $-0.034$ |

**Root cause**: Hydrophobic coupling scales as $N^2$ (all pairwise contacts). Peptide-plane coupling scales as $N$ (adjacent pairs only). For $N=76$: the $N^2/N = 76$-fold excess drowns the plane-alignment signal.

## Q-Decay Weighting Results

The backbone has quality factor $Q = 7$ (amide-V resonance, derived from Axiom 1). A standing wave at position $i$ decays as $e^{-|\Delta i|/(2\pi Q)}$ along the chain. Coupling between residues $i$ and $j$ can only reinforce backbone periodicity if $j$ is within the Q-decay envelope of $i$:

$$Y_\text{hydro}(i,j) \;\leftarrow\; Y_\text{hydro}(i,j) \times \exp\!\left(-\frac{|i-j|}{2\pi Q}\right)$$

The decay length $2\pi Q \approx 44$ residues. For helix contacts ($|i-j|=4$): factor $= 0.86$. For $N=76$ end-to-end: factor $= 0.18$. Zero new parameters ($Q$ already derived).

| | **Baseline** | | **Q-decay** | |
|---|---|---|---|---|
| **Protein** | SS | $R_g$ err | SS | $R_g$ err |
| Trp-cage | 11% | 3.3% | **33%** | 0.0% |
| Villin | 6% | 2.0% | **24%** (H$=$15%) | 4.0% |
| GB1 | 9% | 0.1% | **20%** | 8.9% |
| Ubiquitin | 4% | 1.1% | **14%** | 11.2% |
| **Average** | 7.5% | 1.6% | **22.8%** | 6.0% |

---
