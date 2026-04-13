[↑ Simulation Architecture](./index.md)
<!-- leaf: verbatim -->
<!-- sec:s11_cascade / sec:multiscale_energy — DUAL LABELS: both refer to the same content block (Taxonomy Design Note 4) -->

# Multi-Scale Impedance-Stratified Architecture

The architectural ceiling theorem demonstrates that a single 1D ABCD cascade cannot generate secondary structure above $\sim$23%. The fundamental issue is one of *scale conflation*: modeling every backbone bond as a distributed TL element treats a protein as one continuous microstrip, when it is physically a network of discrete components connected by traces.

Classical EE provides clear guidance via the **lumped/distributed/network** hierarchy. A circuit element is lumped when $\lambda \gg d$ (wavelength far exceeds size), distributed when $\lambda \sim d$, and requires full-wave analysis when $\lambda \ll d$. Mapping this to protein scales:

| **EE Concept** | **Protein Scale** | **Size** | **Model** | **Code** |
|---|---|---|---|---|
| Component (R,L,C) | Covalent bond | 1.5 \AA | Lumped element | `protein_bond_constants` |
| Stub | Sidechain | 3.8 \AA | Shunt $Y$ | $Z_\text{TOPO}$ table |
| Filter section | SS element | 10--60 \AA | Short TL cascade | `abcd_cascade_jax` |
| PCB network | Tertiary contacts | 20--100 \AA | $K \times K$ $Y$-matrix | `s_param_network` |
| Full-wave | Full protein | 20--300 \AA | FDTD | `fdtd_fold_engine` |

## Biological Process $\to$ EE $\to$ Solver

Protein synthesis follows a fixed pipeline that maps directly to classical EE design flow:

1. **Gene $\to$ Sequence** (Schematic $\to$ Netlist). The amino acid sequence IS the netlist: each residue is a component with impedance $Z_\text{TOPO}[\text{aa}]$.

2. **Peptide Bond** (Solder Joint). Covalent N--C link with fixed $Z = \sqrt{m/n_e}$. Bond lengths and angles are manufacturing constraints, not design variables.

3. **SS Nucleation** (Filter Section Self-Assembly). Local H-bonds form when 4+ helix-propensity residues are adjacent ($i \to i{+}4$ coupling). This is a quasi-periodic TL section creating a bandpass filter. The structural energy within each section follows the bond solver pattern: $E_k = \langle Z_\text{seg} \rangle$.

4. **Hydrophobic Collapse** (Impedance Matching). Hydrophobic sidechains in water have high $\Gamma$; burying them against other hydrophobic residues *matches* impedances ($\Gamma \to 0$).

5. **Tertiary Packing** (PCB Layout). SS elements connect via H-bonds, hydrophobic contacts, and disulfide cross-links. Modeled as a $K \times K$ admittance matrix.

## Segmentation at Impedance Discontinuities

The key innovation is partitioning the chain into SS elements at *impedance discontinuities* --- the protein-scale analog of segmenting a TL at connectors and vias. Three types of boundary are detected:

1. **Proline** --- rigid pyrrolidine ring, no H-bond donor. Always a boundary (helix breaker).
2. **Glycine** --- minimal sidechain ($|Z| = 0.30$), maximal flexibility. Boundary when isolated (strand breaker).
3. **Large $\Delta Z$** --- when the local reflection coefficient exceeds the cavity threshold:

$$|\Gamma_i| = \frac{|Z_{i+1} - Z_i|}{|Z_{i+1} + Z_i|} > \frac{1}{\sqrt{2Q}} \approx 0.267$$

This is the *same* threshold used for turn detection: it is the reflection coefficient at which $|\Gamma|^2 = 1/(2Q)$, the critical coupling point.

Validation on three test proteins shows the segmentation correctly identifies known SS boundaries:

| **Protein** | **$K$ elements** | **Boundaries** | **Known SS matched** |
|---|---|---|---|
| Trp-cage (N=20) | 5 | D--G $\Delta Z$, Pro, Gly, Pro | Helix, turn, 3$_{10}$, polyPro |
| Villin (N=35) | 4 | V--F $\Delta Z$, Pro, K--E $\Delta Z$ | 3 helices |
| GB1 (N=56) | 5 | L--N $\Delta Z$, K--G $\Delta Z$, D--N $\Delta Z$, V--D $\Delta Z$ | $\beta_1$, helix, $\beta_2 + \beta_3$ |

## Energy Function: Nodal $Y$-Matrix $S_{11}$

The multi-scale fold engine uses segmentation for initialisation and the full $S_{11}$ network loss from the S-parameter engine for gradient descent.

**Why lumped approximations fail.** Early iterations attempted to replace the full network loss with lumped per-segment averages:

$$E_\text{lumped} = \bigl\langle Z_\text{seg} \times \sqrt{1+R^2} \times \sqrt{1+\kappa_\text{steric}} \times \sqrt{1-\kappa_\text{HB}} \times (1 + \text{exposure} \times |\Gamma|^2) \bigr\rangle$$

where each multiplicative term has a clear EE motivation ($\mu$-enhancement, Pauli exclusion, transformer coupling, standing-wave solvation). While each term is physically correct in isolation, the *mean* impedance cannot capture the network effects---interference, resonance, and conformation-dependent coupling---that drive secondary structure formation. A helix creates a periodic impedance lattice with passband resonance at the helical pitch; this effect only emerges through wave propagation (ABCD cascade), not through averaging.

**The correct EE approach.** In circuit analysis, the standard tool for a complex network is nodal admittance analysis: build the $Y$-matrix, extract $S$-parameters. The loss function is therefore the same $|S_{11}|^2$ cascade, computed on the full conformation-dependent network:

$$\mathcal{L}(\varphi, \psi) = \overline{|S_{11}(\omega)|^2}\big|_{Y = Y(\varphi,\psi)} + \lambda_\text{steric} + \mathcal{L}_\text{Rama} + \mathcal{L}_\text{xtalk}$$

where the $Y$-matrix includes all conformation-dependent terms:

- **Backbone:** tridiagonal $Y$ from N--C$_\alpha$--C bond segments (ABCD cascade);
- **Sidechain stubs:** shunt $Y = 1/Z_\text{TOPO}$ at each C$_\alpha$ junction;
- **H-bond coupling:** transformer mutual inductance $\kappa_\text{HB}$ for pairs within $d < D_\text{HB}$;
- **Hydrophobic coupling:** through-space admittance $Y \propto \exp(-d/R_\text{burial})$ for nonpolar contacts;
- **Solvent loading:** shunt $Y_\text{solvent} = \text{exposure}/Z_\text{water}(\omega)$ at exposed C$_\alpha$ nodes;
- **Chirality:** non-reciprocal phase $\delta_\chi$ from triple products of bond vectors;
- **Packing saturation:** Axiom 4 factor $S(\eta) = \sqrt{1 - \eta^2/P_C^2}$ on total $Y_\text{shunt}$.

**Complex impedance and hydrophobicity.** A key insight: the hydrophilic/hydrophobic distinction emerges naturally from the *reactive* component of $Z_\text{TOPO}$. In the physics engine, $Z_\text{TOPO} = R + jX$ where:

- Nonpolar residues (G,A,V,I,L,M,F,W,P): $X = 0$ (purely resistive);
- Charged residues (D,E,K,R): $X = \pm R/Q$ (capacitive/inductive);
- Polar uncharged (S,T,C,Y,N,Q): $X = \pm R/(2Q)$ (weak reactance).

The complex reflection coefficient at the sidechain--water boundary is:

$$\Gamma_i = \frac{Z_{\text{TOPO},i} - Z_\text{water}(\omega)}{Z_{\text{TOPO},i} + Z_\text{water}(\omega)}$$

where $Z_\text{water}(\omega) = \sqrt{\varepsilon_\infty + (\varepsilon_s - \varepsilon_\infty)/(1 + j\omega\tau)}$ from the Debye model. Nonpolar residues have $|\Gamma|^2 \approx 0.14$ (high mismatch), while charged residues achieve $|\Gamma|^2 \approx 0.07$ through conjugate impedance matching of their reactive component with water's Debye relaxation. No empirical hydrophobicity scale is required---it emerges from the impedance physics.

**Optimisation strategy.** The multi-scale engine contributes the optimisation framework:

1. **Segmentation-aware initialisation**: element boundaries from impedance discontinuity detection;
2. **Extended optimisation**: 20,000 Adam steps (vs. 5,000 in v3 standalone);
3. **Multi-start**: 3 random restarts for better landscape sampling;
4. **Higher learning rate**: $\eta = 2 \times 10^{-3}$ (vs. $10^{-3}$).

## v7 Results

Multi-scale + $S_{11}$ network loss (v7) vs. lumped approximations and standalone $S_{11}$. All constants from AVE axioms; zero empirical fitting.

| **Version** | **Loss function** | **Trp-cage $R_g$ err.** | **Trp SS** | **Villin $R_g$ err.** | **Vil SS** |
|---|---|---|---|---|---|
| v2b (lumped) | $\langle Z_\text{seg} \rangle$ | 15.0% $\uparrow$ | 6% | 16.6% $\uparrow$ | 0% |
| v5 (standing wave) | $Z_\text{seg} \times (1 + e|\Gamma|^2)$ | 30.2% $\uparrow$ | 6% | 29.4% $\uparrow$ | 3% |
| v3 standalone | $|S_{11}|^2$ (5k steps) | 3.4% | 33% | 3.7% | 30% |
| **v7** | $|S_{11}|^2$ **(20k steps)** | **0.0%** | **39%** | **4.1%** | **24%** |

Implementation: `scripts/book_5_topological_biology/multiscale_fold_engine.py` (optimisation loop) calling `s11_fold_engine_v3_jax.py` (network loss).

---
