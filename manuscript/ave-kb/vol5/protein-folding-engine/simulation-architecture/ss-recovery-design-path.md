[↑ Simulation Architecture](./index.md)
<!-- leaf: verbatim -->

# SS Recovery: Design Path and Scale-Invariant Methodology

This section documents the systematic exploration of secondary structure (SS) recovery within the axiom-derived engine. Each approach is traced to the fundamental physics, and both successes and failures are catalogued as a methodological template for future scale-invariant efforts.

## Approach 2: Mode Projection Theorem ($\nu_\text{vac} = 2/7$)

The K4/SRS lattice has 7 compliance modes. The 1D ABCD cascade models 2 longitudinal modes. When 3D contacts enter the 1D cascade as $Y_\text{shunt}$, the mode projection factor is $\nu_\text{vac} = 2/7$---the *same* $\nu_\text{vac}$ that governs the PMNS mixing angle ($\sin^2\theta_{12} = \nu_\text{vac} + 1/45$), equilibrium packing ($\eta_\text{eq} = P_C \times 5/7$), and the strong coupling constant ($\alpha_s = \alpha^{3/7}$).

**Result**: Flat $\nu_\text{vac} = 2/7$ multiplication *killed* SS ($33\% \to 6\%$). It equally weakened both the SS-driving (peptide-plane) and SS-drowning (hydrophobic) terms, providing no differential advantage.

**Lesson**: Comparison with the galactic rotation solver revealed that the saturation factor $S = \sqrt{1 - (g_N/a_0)^2}$ serves as a *dynamic* mode projection---varying spatially, not as a flat scalar. The projection is *already encoded* in Axiom 4; applying it again as a multiplicative constant double-counts the effect.

## Approach 3: Semiconductor Depletion Region Analysis

The correct physical mechanism emerged from the analogy with semiconductor small-signal vs. large-signal analysis:

### MOSFET--Backbone Mapping

The backbone is the channel; local packing is the gate voltage.

| **MOSFET** | **Protein backbone** |
|---|---|
| $V_\text{GS}$ (gate voltage) | $\eta_i$ (local packing fraction) |
| $V_\text{th}$ (threshold) | $P_C = 8\pi\alpha$ (saturation threshold) |
| $I_D$ (drain current) | $Y_\text{shunt}$ (coupling strength) |
| Channel depletion width | Impedance contrast along backbone |
| $g_m = dI_D/dV_\text{GS}$ | $dS/d\eta$ (transconductance of saturation) |

In a MOSFET, the depletion region has *spatially varying* width---this is what enables amplification ($g_m$). The previous engine applied Axiom 4 saturation *globally* (single $\eta$ for the whole protein). This is like a MOSFET with uniform channel---no spatial variation, no amplification, no impedance contrast.

**Per-residue local saturation**: Each residue's local packing fraction $\eta_i = n_\text{neighbors}/n_\text{max}$ controls its own saturation level:

$$S(\eta_i) = \sqrt{1 - (\eta_i / P_C)^2}$$

The Axiom 4 saturation curve has three operating regimes:

$$\begin{align}
\text{Linear:}     \quad & \eta_i \ll P_C \;\Rightarrow\; S \approx 1 \quad\text{(full coupling, no contrast)} \\
\text{Depletion:}  \quad & \eta_i \approx 0.5\,P_C \;\Rightarrow\; |dS/d\eta| \;\text{maximum (max.\ transconductance)} \\
\text{Saturation:} \quad & \eta_i \to P_C \;\Rightarrow\; S \to 0 \quad\text{(pinch-off, no coupling)}
\end{align}$$

Dense core residues ($\eta_i$ high) $\Rightarrow$ $S$ small $\Rightarrow$ weak $Y_\text{shunt}$ $\Rightarrow$ reflective segment. Exposed loop residues ($\eta_i$ low) $\Rightarrow$ $S$ large $\Rightarrow$ strong coupling $\Rightarrow$ transparent segment. At helix/loop boundaries, the impedance change creates *reflections* along the backbone---and reflections create standing waves from which secondary structure emerges.

## SPICE Model Analysis

In semiconductor SPICE simulation, each transistor has a `.model` card specifying its nonlinear I--V characteristics ($V_\text{th}$, $K$, $W/L$, etc.). The protein backbone already provides an exact analog:

- **Per-residue model card**: $Z_\text{topo}$ from the periodic table solver (20 unique impedances for 20 amino acids). This is derived solely from atomic composition via Axioms 1--2.
- **Netlist**: The ABCD cascade backbone with $Y_\text{shunt}$ shunt admittances at each C$_\alpha$ node.
- **SPICE solver**: The frequency-swept $S_{11}$ calculation via `lax.fori_loop` is equivalent to an AC analysis in SPICE.

The axioms require *no additional per-residue parameters* beyond $Z_\text{topo}$:

- Burial threshold ($\beta$): geometric, from Axiom 1 (sigmoid slope from contact distance)
- Coupling constant ($\kappa$): universal, from Axiom 1 ($Z_0 / Z_\text{bb}$)
- Quality factor ($Q = 7$): backbone resonance, from Axiom 1 (amide-V $f_0/\Delta f$)
- Saturation threshold ($P_C = 8\pi\alpha$): from Axiom 4

---
