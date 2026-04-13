[↑ Network Solver](./index.md)
<!-- leaf: verbatim -->

# Dynamic Allostery via Impedance Perturbation

Tiers 1--4 evaluated the protein backbone as a static network converging to an energy minimum. This section addresses the dynamic response: what happens when an external impedance load---a ligand, cofactor, or phosphorylation event---is introduced into the already-folded native state?

## RF Filter-Tuning Analogy

In microwave engineering, a tuned bandpass filter is characterised by its center frequency $f_0$ and quality factor $Q$. Inserting an external reactive element (a tuning stub of impedance $Z_\text{stub}$) at position $x$ along the transmission line shifts the resonance:

$$f_0' = \frac{1}{2\pi\sqrt{L\,(C + C_\text{stub})}}$$

The phase of the standing wave rotates, and nodes/antinodes shift position along the entire line---not just at $x$. This is the RF analogue of biological allostery.

## Protein Ligand as Tuning Stub

A ligand binding at residue $i$ modifies the local topological impedance:

$$Z_\text{topo}(i) \;\longrightarrow\; Z_\text{topo}(i) \parallel Z_\text{ligand} = \frac{Z_\text{topo}(i)\cdot Z_\text{ligand}}{Z_\text{topo}(i) + Z_\text{ligand}}$$

This changes the local reflection coefficient $\Gamma_i = (Z_\text{new} - Z_\text{bb})/(Z_\text{new} + Z_\text{bb})$, which propagates as a reflected wave along the backbone standing-wave network. The protein must re-minimise $|S_{11}|^2$ by adjusting its torsion angles $\{\phi, \psi, \chi_1, \chi_2\}$ at *every* residue---not just the binding site.

## Simulation Protocol

The allosteric perturbation test follows a two-phase protocol:

1. **Phase 1 --- Native fold.** A 15-residue polyalanine chain ($Z_\text{topo}[\text{Ala}] \approx 2.0$) is folded to convergence using the standard $S_{11}$ torsion-angle minimiser (3,000 Adam steps, $\text{lr} = 2 \times 10^{-3}$). The final angles $\{\phi, \psi\}_\text{native}$ are recorded.
2. **Phase 2 --- Ligand injection.** A synthetic reactive load $Z_\text{ligand} = 15.0 + 15.0j$ is applied at the central residue ($i = 7$), replacing its native $Z_\text{topo}$. The minimiser is re-activated from the native angles with no stochastic annealing (2,000 steps, $\text{lr} = 10^{-3}$), allowing strictly deterministic mechanical relaxation.

## Results: Distal Conformational Shift

Angular displacement $\Delta\theta_k = \sqrt{(\Delta\phi_k)^2 + (\Delta\psi_k)^2}$ between the native and holo conformations at each residue $k$. Allosteric angular displacement for a 15-residue polyalanine helix upon injection of $Z_\text{ligand} = 15 + 15j$ at residue 7. Zero empirical parameters.

| **Residue** | $\Delta\phi$ ($^\circ$) | $\Delta\psi$ ($^\circ$) | $\Delta\theta$ ($^\circ$) | |
|---|---|---|---|---|
| A0 | $-82.1$ | $-14.1$ | 83.3 | |
| A1 | $+4.5$ | $+43.7$ | 43.9 | |
| A2 | $+25.2$ | $-15.7$ | 29.7 | |
| A3 | $+3.5$ | $+34.3$ | 34.5 | |
| A4 | $-41.9$ | $-45.7$ | 62.0 | |
| A5 | $+13.8$ | $+39.4$ | 41.7 | |
| A6 | $-11.1$ | $+24.1$ | 26.6 | |
| **A7** | $-43.1$ | $-7.1$ | **43.7** | $\longleftarrow$ target |
| A8 | $+16.2$ | $-23.0$ | 28.1 | |
| A9 | $+5.7$ | $+7.7$ | 9.6 | |
| A10 | $+23.2$ | $-11.5$ | 25.9 | |
| A11 | $+22.3$ | $-10.8$ | 24.8 | |
| A12 | $-22.9$ | $+14.4$ | 27.0 | |
| A13 | $-5.3$ | $-13.8$ | 14.8 | |
| A14 | $+2.7$ | $+0.0$ | 2.7 | |

**Key observations.**

1. The **maximum** angular displacement ($83.3^\circ$) occurs at residue 0---the N-terminus, seven residues distant from the injection site. The displacement at the target itself is $43.7^\circ$, ranking only fifth.
2. The strain profile is **non-monotonic**: large displacements alternate with small ones, consistent with a standing-wave node/antinode pattern.
3. No empirical force field, Go-model potential, or elastic-network model is used. The allosteric propagation emerges *exclusively* from the $|S_{11}|^2$ gradient flowing through the universal reflection operator $\Gamma = (Z_2 - Z_1)/(Z_2 + Z_1)$.

## Cross-Domain Interpretation

The ligand-binding event maps directly onto established phenomena in other domains:

| **Domain** | **Perturbation** | **Response** |
|---|---|---|
| RF / Microwave | Tuning stub soldered to line | Bandpass shift, node migration |
| Seismology | Fault stress $>$ rock compliance | Rupture propagation (earthquake) |
| Cosmology | BH merger event | QNM ring-down ($Q = 7$ cycles) |
| Biology | Ligand at residue $i$ | Allosteric shift at residue $j \neq i$ |

All four cases are governed by the same operator chain: $Z \to \Gamma \to S_{11}$ minimisation.

## Bingham Yield Limit

As the ligand impedance magnitude increases, the local reflection coefficient approaches unity:

$$|\Gamma_i| = \left|\frac{Z_\text{ligand} - Z_\text{bb}}{Z_\text{ligand} + Z_\text{bb}}\right| \;\xrightarrow{\;|Z_\text{ligand}| \to \infty\;}\; 1$$

At $|\Gamma| = 1$, the backbone can no longer absorb the perturbation through torsional adjustment. The secondary structure at the injection site *breaks*---the helix unwinds locally, analogous to the Bingham plastic yield stress $\tau_y = B_\text{snap}^2 / 2\mu_0$ (Axiom 4) in the fluid domain. This represents the structural failure mode of the transmission-line network.

## Full Pathway Map: $N \times N$ Coupling Matrix

The single-site perturbation demonstrates that allostery exists; the next question is whether the pathway topology is reproducible. To answer this, the ligand injection is swept across *every* residue position $i = 0 \ldots N{-}1$, and the angular displacement is recorded at every response site $j$. The result is an $N \times N$ allosteric coupling matrix:

$$M_{ij} = \sqrt{(\Delta\phi_j)^2 + (\Delta\psi_j)^2} \Bigr|_{\text{ligand at } i}$$

**Protocol.** A 12-residue polyalanine helix is folded to native convergence (3,000 steps). For each of the 12 injection sites, a reactive load $Z_\text{ligand} = 15 + 15j$ is applied and the backbone is re-equilibrated (1,500 steps, no annealing). Total sweep time: 29 s on a single CPU.

**Results.**

| **Metric** | **Value** |
|---|---|
| Diagonal mean (local strain) | $26.5^\circ$ |
| Off-diagonal mean (distal strain) | $24.6^\circ$ |
| Off-diagonal max (strongest path) | $62.5^\circ$ |
| Distal/local ratio | 0.93 |
| Distal-dominant injections | 11/12 |

**Standing-wave antinode topology.** The coupling matrix reveals that **residue 2** acts as a universal strain sink: injecting the ligand at any of residues 6--10 (the C-terminal half) produces maximum displacement at residue 2. This is the transmission-line equivalent of a *standing-wave antinode*---a point of minimal mechanical stiffness where the backbone impedance profile has the least resistance to torsional deformation.

In RF engineering, the analogous measurement is a *Voltage Standing Wave Ratio (VSWR) map*: probing the magnitude of the reflected wave along the physical length of a stripline to identify nodes (high impedance, rigid) and antinodes (low impedance, compliant). The allosteric coupling matrix $M_{ij}$ is the biological VSWR map of the protein backbone.

**Falsifiable prediction.** If the TL model is correct, then residues located at standing-wave antinodes should exhibit the largest crystallographic B-factors (thermal displacement parameters) in X-ray structures, because they are the mechanically softest points on the backbone. Conversely, residues at nodes should have the smallest B-factors.

---
