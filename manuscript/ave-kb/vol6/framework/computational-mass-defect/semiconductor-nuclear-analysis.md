[↑ Computational Mass Defect](../index.md)
<!-- leaf: verbatim -->
<!-- path-stable: referenced from vol6 as sec:semiconductor_nuclear -->

## Semiconductor Circuit Analysis of Nuclear Binding

The nuclear binding problem maps precisely onto the large-signal analysis of semiconductor junction devices. This is not an analogy---the vacuum LC lattice *is* the dielectric medium, the nucleon knots *are* the junction dopants, and the Coulomb field *is* the reverse-bias voltage. Every parameter derives from the four AVE axioms with zero empirical fits.

### Two Binding Models: Bare vs Semiconductor

The AVE framework implements two progressively refined binding models, both sourcing all constants from the physics engine (`ave.core.constants`):

1. **Bare $K/r$ Model** (`simulate_element.py`, individual solver scripts). This zeroth-order model treats all nucleon pairs identically via the strong mutual inductance $M_{ij} = K_{\text{MUTUAL}} / r_{ij}$. It is accurate for $^4$He and light elements through Silicon but does not account for Coulomb repulsion between proton-proton pairs. Used for: coordinate geometry generation, EE network visualization, and density heatmaps.

2. **Semiconductor Junction Model** (`semiconductor_binding_engine.py`). This full-physics model incorporates reverse-bias Coulomb repulsion ($\alpha\hbar c / r_{pp}$) with Miller avalanche amplification ($n_{\text{Miller}} = c_{\text{proton}} = 5$) and depletion-layer breakdown ($V_{BR} = 6\alpha\hbar c / D_{\text{intra}}$). It produces the **definitive mass-validated $R$-values** reported throughout this text.

Because the semiconductor model includes the repulsive Coulomb correction, its solved inter-alpha distances $R$ differ from the bare model. This difference is physically significant---for Fluorine-19, the bare $K/r$ model *cannot* solve the halo distance because the O-16 core is over-bound by the strong force alone. Only the semiconductor model's Coulomb correction creates the asymmetric strain that generates Fluorine's extreme electronegativity.

| **Element** | **Bare $K/r$** | **Semiconductor** | **Note** |
|---|---|---|---|
| C-12 ($3\alpha$) | $50.2d$ | $56.6d$ | Ring radius |
| O-16 ($4\alpha$) | $50.2d$ | $33.4d$ | Tetrahedron, Coulomb compresses |
| Ne-20 ($5\alpha$) | $78.9d$ | $81.2d$ | Bipyramid |
| Mg-24 ($6\alpha$) | $80.6d$ | $78.0d$ | Octahedron |
| Si-28 ($7\alpha$) | $85.6d$ | $83.0d$ | Pentagonal bipyramid |

*Comparison of inter-alpha distances from the two binding models. All values in units of $d = 4\hbar/(m_p c) \approx 0.841$ fm (`D_PROTON`). The semiconductor model R values are the definitive mass-validated quantities.*

### Parameter Derivation Table

Every constant used in this model traces directly to a named identifier in the `ave.core.constants` physics engine module (`src/ave/core/constants.py`). No empirical device parameters exist.

| **LaTeX Symbol** | **Python Identifier** | **Value** | **Unit** | **Source** |
|---|---|---|---|---|
| $l_\text{node}$ | `L_NODE` | $3.862\times10^{-13}$ | m | Axiom 1 |
| $\alpha$ | `ALPHA` | $0.007297$ | --- | Axiom 2 |
| $\hbar$ | `HBAR` | $1.055\times10^{-34}$ | J$\cdot$s | Axiom 1 |
| $c_0$ | `C_0` | $2.998\times10^{8}$ | m/s | Axiom 1 |
| $\kappa_\text{FS}$ | `KAPPA_FS` | $24.951$ | --- | Axiom 3 |
| $c_\text{proton}$ | `CROSSING_NUMBER_PROTON` | $5$ | --- | Axiom 2 |
| $K$ | `K_MUTUAL` | $11.337$ | MeV$\cdot$fm | Axiom 2 |
| $\alpha\hbar c$ | $\alpha \times$ `HBAR` $\times$ `C_0` | $1.440$ | MeV$\cdot$fm | Axiom 2 |
| $p_c$ | `P_C` | $0.1834$ | --- | Axioms 1+2 |
| $m_p/m_e$ | `PROTON_ELECTRON_RATIO` | $1836.1$ | --- | Axioms 1--3 |
| $d$ | $4\hbar/(m_p c)$ | $0.841$ | fm | Derived |
| $D_\text{intra}$ | $d\sqrt{8}$ | $2.379$ | fm | Axiom 1 |
| $V_{BR}$ | $6\alpha\hbar c / D_\text{intra}$ | $3.631$ | MeV | Axiom 2 |
| $\beta_0$ | $K/\alpha\hbar c$ | $7.873$ | --- | Axiom 2 |
| $n_\text{Miller}$ | `CROSSING_NUMBER_PROTON` | $5$ | --- | Axiom 2 |

*Physics Engine Traceability. Every nuclear parameter maps 1:1 to a named constant in `ave.core.constants`. Values shown are computed at import time from the four AVE axioms.*

| **Semiconductor** | **Nuclear (AVE)** | **Engine Constant** |
|---|---|---|
| $I_S$ (saturation current) | $K / D_\text{intra}$ | `K_MUTUAL`/($d\sqrt{8}$) |
| $V_T$ (thermal voltage) | $m_e c^2$ | $0.511$ MeV |
| $V_{bi}$ (built-in potential) | $\alpha\hbar c / d$ | `ALPHA`$\times\hbar c / d$ |
| $V_{BR}$ (breakdown voltage) | $6\alpha\hbar c / D_\text{intra}$ | $6 \times$`ALPHA`$\times\hbar c / D$ |
| $\beta_0$ (intrinsic gain) | $K / \alpha\hbar c$ | `K_MUTUAL`/(`ALPHA`$\hbar c$) |
| $n$ (Miller exponent) | $c_\text{proton}$ (crossings) | `CROSSING_NUMBER_PROTON` |
| Forward bias ($p$--$n$) | $K/r_{ij}$ (strong coupling) | `K_MUTUAL`$/r$ |
| Reverse bias ($p$--$p$) | $\alpha\hbar c / r_{ij}$ (Coulomb) | `ALPHA`$\times\hbar c / r$ |

*Semiconductor $\leftrightarrow$ Nuclear parameter mapping. Each semiconductor concept has an exact AVE equivalent with no free parameters.*

### Derivation of the Breakdown Voltage

The breakdown voltage $V_{BR}$ is the maximum reverse Coulomb stress that one alpha cluster can absorb internally before its dielectric junction avalanches. Each alpha cluster contains exactly 6 nucleon-nucleon pair channels, of which one is a proton-proton pair. The total internal Coulomb capacity is therefore the energy stored in all 6 pair slots at the intra-alpha separation:

$$
V_{BR} = \frac{6 \, \alpha\hbar c}{D_\text{intra}} = \frac{6 \, \alpha\hbar c}{d\sqrt{8}} \approx 3.631 \text{ MeV}
$$

This is derived entirely from Axiom 2 ($\alpha\hbar c$) and Axiom 1 ($D_\text{intra} = d\sqrt{8}$). No empirical device parameter is introduced.

### Miller Avalanche Multiplication

When the cumulative Coulomb repulsion per alpha cluster exceeds $V_{BR}$, the vacuum dielectric between clusters undergoes avalanche breakdown, amplifying the repulsive term nonlinearly. The multiplication factor follows the standard Miller equation:

$$
M = \frac{1}{1 - \left(\dfrac{V_R}{V_{BR}}\right)^{n}}
$$

where the reverse voltage per cluster is:

$$
V_R = \frac{1}{N_\alpha} \sum_{\substack{i<j \\ \alpha_i \neq \alpha_j}} \frac{f_{pp} \, \alpha\hbar c}{r_{ij}}
$$

with $f_{pp} = 0.25$ (four $pp$ pairs out of sixteen inter-alpha nucleon pairs), and the Miller exponent $n = c_\text{proton} = 5$ is the cinquefoil crossing number---each crossing represents one stage of the avalanche multiplication chain, directly from Axiom 2.

### Complete Binding Energy Formula

The total nuclear mass for an $N_\alpha$-cluster nucleus is:

$$
\boxed{
M_\text{nucleus} = N_\alpha \, M_\alpha \;-\; \underbrace{\sum_{\substack{i<j \\ \alpha_i \neq \alpha_j}} \frac{K}{r_{ij}}}_{\text{forward bias (attractive)}} \;+\; \underbrace{M \cdot \sum_{\substack{i<j \\ \alpha_i \neq \alpha_j}} \frac{f_{pp}\,\alpha\hbar c}{r_{ij}}}_{\text{reverse bias + avalanche (repulsive)}}
}
$$

where all sums run over the $16 \times \binom{N_\alpha}{2}$ inter-alpha nucleon-nucleon pairs. The three terms map to:

- **Alpha cluster mass** $M_\alpha$: the resonant tank eigenvalue (Axiom 1 geometry, Axiom 2 coupling).
- **Forward bias** $K/r$: mutual inductance between $p$--$n$ pairs across junctions (Axiom 2).
- **Reverse bias + avalanche** $M \cdot f_{pp} \cdot \alpha\hbar c / r$: Coulomb repulsion between $p$--$p$ pairs, amplified by the Miller multiplier when cumulative stress exceeds $V_{BR}$ (Axioms 2 and 4).

### Results: Small Signal to Large Signal Transition

| **Element** | $N_\alpha$ | $V_R / V_{BR}$ | $M$ | **Error** | **Regime** |
|---|---|---|---|---|---|
| He-4 | 1 | --- | --- | $0.0000\%$ | Single tank |
| C-12 | 3 | 0.022 | 1.000 | $0.0000\%$ | Small Signal |
| O-16 | 4 | 0.033 | 1.000 | $0.0000\%$ | Small Signal |
| Ne-20 | 5 | 0.035 | 1.000 | $0.0000\%$ | Small Signal |
| Mg-24 | 6 | 0.043 | 1.000 | $0.0001\%$ | Small Signal |
| Si-28 | 7 | 0.050 | 1.000 | $0.0002\%$ | Small Signal |
| **S-32** | **8** | **0.994** | **32.8** | $\mathbf{0.0000\%}$ | **Large Signal** |

*Predicted nuclear masses from the semiconductor avalanche model. All parameters are axiom-derived; zero empirical fits. The avalanche multiplier $M$ remains at unity for $Z \le 14$ (Small Signal) and jumps to $32.8$ at $Z=16$ (Large Signal).*

### Topology as Semiconductor Device Type

An essential consequence of this framework: each nuclear topology behaves as a distinct semiconductor *device*, fabricated on the same vacuum lattice *material*. The breakdown voltage $V_{BR}$ is a material constant (derived from $\alpha\hbar c$ and $D_\text{intra}$), but each topology determines a different $V_R / V_{BR}$ ratio---exactly as a silicon BJT and a gallium-nitride HEMT share the same semiconductor physics but have different breakdown characteristics due to their crystal geometries.

- **Triangle** (C-12, 3$\alpha$): Low vertex density $\rightarrow$ $V_R/V_{BR} = 0.022$ $\rightarrow$ deep Small Signal.
- **Tetrahedron** (O-16, 4$\alpha$): Moderate packing $\rightarrow$ $V_R/V_{BR} = 0.033$ $\rightarrow$ Small Signal.
- **Pentagonal bipyramid** (Si-28, 7$\alpha$): High packing but open faces $\rightarrow$ $V_R/V_{BR} = 0.050$ $\rightarrow$ boundary of Small Signal. *This mathematical positioning precisely at the edge of the non-linear transition fundamentally defines why Silicon is the dominant material in microelectronics: it is highly stable in bulk, yet sits close enough to the breakdown threshold that it can be easily manipulated (doped) to switch states dynamically.*
- **Cube** (S-32, 8$\alpha$): Maximum closed packing $\rightarrow$ $V_R/V_{BR} = 0.994$ $\rightarrow$ avalanche breakdown ($M = 32.8$).
- **Bicapped Antiprism** (Ar-40, 10$\alpha$): Open expansion restores $V_R/V_{BR} = 0.062$ $\rightarrow$ Small Signal.
- **Bicapped Antiprism** (Ca-40, 10$\alpha$): Same geometry, 2 additional protons push $V_R/V_{BR} = 0.994$ $\rightarrow$ second Large Signal solution ($M = 32.9$).
- **Cuboctahedron** (Ti-48, 12$\alpha$): Archimedean solid, 12 edge-midpoint vertices $\rightarrow$ $V_R/V_{BR} = 0.067$ $\rightarrow$ Small Signal.
- **Centered Icosahedron** (Cr-52, 13$\alpha$): 12-vertex icosahedron + central $\alpha$; vertex coordinates defined by the Golden Ratio $\varphi = (1+\sqrt{5})/2$ $\rightarrow$ $V_R/V_{BR} = 0.053$ $\rightarrow$ Small Signal.
- **FCC-14** (Fe-56, 14$\alpha$): Face-centered cubic packing (8 corners + 6 face centers) $\rightarrow$ $V_R/V_{BR} = 0.049$ $\rightarrow$ Small Signal. Iron-56 is the absolute thermodynamic endpoint of stellar fusion.

The cube (S-32) is the first topology where the cumulative Coulomb load per alpha cluster approaches the internal Coulomb capacity $V_{BR}$. Beyond the cube, the geometry opens up again and the nucleus re-enters Small Signal---except for Ca-40, where the additional proton charge pushes the same 10$\alpha$ bicapped antiprism back into avalanche. The progression from Ring $\rightarrow$ Tetrahedron $\rightarrow$ Bipyramid $\rightarrow$ Cube $\rightarrow$ Antiprism $\rightarrow$ Cuboctahedron $\rightarrow$ Icosahedron $\rightarrow$ FCC traces a systematic walk through the Platonic and Archimedean solids, with each geometry emerging from the minimum-impedance packing requirement---not from empirical fitting.

### Inter-Alpha Distances as Coupled Cavity Resonators

The inter-alpha distances ($R$) in this engine are not arbitrary static force equilibria; they are dynamic standing-wave resonance conditions. In the AVE framework, nucleons are not static DC point charges, but dynamic electromagnetic gyroscopes oscillating at the rest-mass Compton frequency ($\omega = mc^2/\hbar$).

At nuclear distances ($R < 80$ fm), the entire geometry exists deep inside a single macroscopic lattice node ($l_{node} \approx 386$ fm). Because the local metric strain evaluating to $\Delta\phi / \alpha = l_{node} / r$ is strictly greater than 1, the entire nuclear interior operates at the absolute Axiom 4 dielectric saturation limit ($C_{eff} \to \infty$, $Z \to 0\,\Omega$). The $K/r$ and $\alpha\hbar c/r$ terms used in the complete binding formula already represent the saturated internal coupling forces within this bounded zone.

Because the vacuum inside the nucleus is fully saturated, the static force terms share identical $1/r$ dependence and cannot produce an equilibrium location on their own. Instead, the equilibrium distance $R$ is determined dynamically by the topology acting as a **coupled cavity resonator**.

The alpha cluster itself is the fundamental tank circuit mode. When multiple alpha clusters assemble into higher-order topologies (rings, tetrahedrons, octahedrons), they form a continuous bandpass filter array. The distance $R$ between the clusters is physically set by the requirement that the resulting topological phase volume fits exactly an integer (or rational) number of standing half-wavelengths of the system's kinetic binding energy. In standard RF engineering, this is identical to structurally separating LC tank circuits by precisely tuned lengths of transmission line to achieve perfect impedance matching ($S_{11} \to 0$) and maximize the $Q$-factor of the assembly.

This reveals a fundamental physical insight: **the nucleus is a resonant AC standing wave structure operating within a continuous 0 $\Omega$ dielectric cavity**, natively explaining why phenomenological static liquid-drop models fail to predict exact geometric distributions.

---
