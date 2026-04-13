[↑ Protein Folding Engine](../index.md)

# Network Solver — Ch.5 Multi-Path TL Network Solver

This chapter upgrades the 1D ABCD cascade to a 2D S-parameter network, where every bond type---backbone, H-bond, through-space contact---becomes a full transmission-line segment connecting two nodes in an admittance matrix. Derives folding timescales, validates against 20 PDB structures, and extends the TL framework to neural circuitry and broader biological phenomena.

## Key Results

| Result | Statement |
|---|---|
| Full Kramers Folding Time | $\tau_\text{fold} = Q^2 \cdot N \cdot \tau_\text{water} \cdot \exp\!\bigl(\ln(3) \cdot \frac{3}{7} \cdot N \cdot \text{CO}\bigr)$; barrier exponent $\beta = 0.471$ matches empirical $0.452$ within 4.1% |
| Folding Speed Limit | $\tau_\text{min} = QN/f_0 = 7N/(23\;\text{THz})$ |
| 20-Protein PDB Validation | $R_g$ median error 3.5%, mean SS 21%, zero crashes, zero empirical parameters |
| $\tau_\text{fold}$ validation | $R = 0.87$, MAE $= 1.4$ decades across 15 two-state folders; zero fitted parameters |
| Beta-Sheet Antiparallel Coupling | $Y_{\beta}(i,j) = \kappa_\text{HB} \cdot \max(0, -\cos(\hat{u}_i, \hat{u}_j)) \cdot \cos\theta_{ij} \cdot \sigma(D_\text{HB} + d_0 - d_{\text{N}_i\text{C}_j})$; zero new parameters |
| Bend Discontinuity Admittance | $C_\text{bend} = (1-\cos\theta_i)/(2\pi^2)$, $Y_\text{bend}(\omega) = \omega\,C_\text{bend}$; zero new constants |
| Derived Ramachandran Basins | $\varphi_\alpha = -60^\circ$, $\psi_\alpha = -37.3^\circ$, $\varphi_\beta \approx -125.3^\circ$, $\psi_\beta = +125.3^\circ$; within $5^\circ$ of crystallography |
| Backbone Y-Parameters | $y^\text{mutual}_{i,i+1} = -\operatorname{csch}(\gamma\ell)/Z_\text{eff}$, $y^\text{self}_{i} = \coth(\gamma\ell)/Z_\text{eff}$ |
| Eigenvalue Root Target (v5) | $f(\boldsymbol{\theta}) = \lambda_{\min}(S^\dagger S) \cdot S_\text{pack}(\eta) + \mathcal{P}_\text{steric}$; convergence at $\|f\| < 1/Q^2$ |
| SPICE Transient Equations | Euler integration with derived damping $R \approx 0.887$ (two channels: bend loss + solvent shunt) |
| v7 Segmented Cascade | 3-phase cotranslational solver; Protein G sub-10 Å (9.91 Å vs 18.62 Å v4) |
| VSWR golden ratio | 34-residue uniform backbone: VSWR $= \varphi \approx 1.618$ from topology alone |
| EEG cavity modes | $f_n = n \cdot v_\text{axon}/(2L_\text{eff})$; $\delta$=1 Hz, $\gamma$=20 Hz predicted |
| Synaptic reflection | $\Gamma_\text{synapse} = (Z_\text{post} - Z_\text{pre})/(Z_\text{post} + Z_\text{pre})$ |

## Derivations and Detail

| Document | Contents |
|---|---|
| [Cascade to Network Architecture](./cascade-to-network-architecture.md) | Y-shunt balance theorem, 2D network topology, Y-parameter formulation, $S_{11}$ via Schur complement |
| [Compaction Physics](./compaction-physics.md) | Conjugate impedance matching, Axiom 4 dielectric saturation, long-range saturation envelope |
| [Benchmark Results](./benchmark-results.md) | 1D vs 2D benchmark, v3 vs v4 benchmark, v4 all-derived constants benchmark |
| [Analysis: 2D Network](./analysis-2d.md) | Network wins/losses, physical interpretation, loss decomposition, impedance landscape |
| [Folding Speed Limit](./folding-speed-limit.md) | 8-step derivation chain: clock, ring-down, transit, speed limit, contact order, search factor, Kramers barrier, full $\tau_\text{fold}$ |
| [20-Protein PDB Validation](./pdb-validation-20-protein.md) | Full 20-protein table, $\tau_\text{fold}$ validation ($R = 0.87$) |
| [Dynamic Allostery](./dynamic-allostery.md) | Ligand as tuning stub, distal conformational shift, $N \times N$ coupling matrix, Bingham yield limit |
| [Beta-Sheet Antiparallel Coupler](./beta-sheet-antiparallel-coupler.md) | Backward-wave directional coupler, parameter-free $Y_\beta$ formulation, benchmark |
| [Bend Discontinuity Admittance](./bend-discontinuity-admittance.md) | Cross-domain consensus, capacitive bend admittance, protein Smith chart |
| [Ramachandran Basins (Steric)](./ramachandran-basins-steric.md) | Derived $\alpha$/$\beta$/PPII basins from sp$^3$ tetrahedral angle and $Q/2$ standing wave |
| [Backbone Y-Parameters](./backbone-y-parameters.md) | ABCD $\to$ Y conversion, nodal admittance matrix, S-parameter extraction, Y-matrix magnitude audit, constants audit |
| [Eigenvalue Root Target (v5)](./eigenvalue-root-target-v5.md) | Newton-Raphson root-finding, convergence criterion $1/Q^2$, VSWR proof-of-concept |
| [SPICE Transient Equations (v7)](./spice-transient-equations-v5.md) | Euler time-stepping, cotranslational cascade, derived damping $R = 0.887$, timestep scaling law |
| [Complete Circuit Model](./complete-circuit-model.md) | Biology $\to$ EE mapping (9 coupling mechanisms), chain termination, disulfide, aromatic, salt bridge admittances |
| [v7 Segmented Cascade](./v7-segmented-cascade.md) | NERF error problem, 3-phase cascade architecture, v7 benchmark |
| [Environment Parameter Sensitivity](./environment-parameter-sensitivity.md) | OAT sweep of $\varepsilon_s$, $\varepsilon_\infty$, $\tau_D$, $f_0$; engine insensitive to solvent dielectric |
| [Translation Matrix: Bio $\to$ EE $\to$ AVE](./translation-matrix-bio-ee-ave.md) | Operator catalog, H-bond impedance (Op4), sidechain reactive tanks, self-consistent loss function |
| [Y-Matrix Gradient Architecture](./y-matrix-gradient-architecture.md) | Loss decomposition, impedance landscape, hydrophobic hypothesis (disproven), architecture guard rails, Op2 crossing penalty |
| [Frequency-Domain Analysis](./frequency-domain-analysis.md) | Spatial FFT, autocorrelation, spectral SS prediction, FFT-guided basin initialisation |
| [Roadmap](./roadmap.md) | Sub-5 Å RMSD, real allosteric systems, 3D spatial impedance grid |
| [Neural TL Network](./neural-tl-network.md) | Axon as coaxial TL, $Z_\text{axon}$, synaptic reflection coefficient |
| [Memory as Impedance Locking](./future-memory.md) | LTP as impedance matching, memory capacity as eigenvalue count |
| [Sleep as S-Parameter Recalibration](./sleep-recalibration.md) | Slow-wave/REM as frequency sweeps, sleep deprivation as impedance drift |
| [Alzheimer's as Impedance Drift](./alzheimers-impedance.md) | Demyelination $\to$ $Z$ detuning $\to$ memory loss |
| [Anesthesia as Impedance Mismatch](./anesthesia-ch5.md) | Non-uniform $Z$ shift at nodes of Ranvier, MAC prediction |
| [EEG Cavity Modes](./eeg-modes.md) | $f_n = nv/(2L)$ cortical cavity modes, $\delta$ through $\gamma$ bands |
| [Phantom Limb](./phantom-limb.md) | Open-circuit termination, orphaned standing wave eigenstates |
| [Broader Research Avenues](./broader-research-avenues.md) | Research avenues table (7 operators), DNA as digital TL, morphogenesis, enzyme catalysis |

---
