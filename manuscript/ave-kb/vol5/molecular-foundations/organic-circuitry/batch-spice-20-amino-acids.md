[↑ Organic Circuitry](../index.md)
<!-- leaf: verbatim -->

---

## Batch SPICE Computation of 20 Standard Amino Acids
<!-- label: sec:batch_spice -->

To extend the single-molecule validation (Glycine and Alanine) to the full biological alphabet, topological SPICE netlists were generated for all 20 standard L-amino acids and solved computationally. This subsection documents every step required for independent reproduction.

### Circuit Template

Every amino acid shares the same backbone circuit topology, differing only in the R-group stub network:

1. **Source (NH$_3^+$):** A voltage source $V_\text{amino}$ at 30 THz (Wien's-law body temperature) drives through an inductor $L_{\text{NH}_3} = m_N / \xi^2$ and a coupling capacitor $C_{NC} = \xi^2 / k_{C\text{--}N}$.
2. **Alpha Carbon:** An inductance $L_\alpha = m_C / \xi^2$ bridges the amino terminus to the R-group junction node.
3. **R-Group Stub:** A branching subtree of $L$ and $C$ elements specific to each amino acid's side chain, connected at the $\alpha$-carbon node. The exact topology for each of the 20 amino acids is defined procedurally in `generate_amino_spice.py`.
4. **Carboxyl Sink (COO$^-$):** A capacitor $C_{CC}$ feeds through $L_\text{carboxyl}$, which splits into a double-bonded oxygen stub ($C_{C=O}$, $L_O$) and a single-bonded output branch ($C_{C\text{--}O}$, $L_O$), terminated by a resistive load $R_\text{load} = Z_0 \approx 376.73\;\Omega$ (vacuum impedance, derived from Axioms 1--2).

All component values are computed from the transduction equations (Eqs. eq:L_atom, eq:C_bond) using force constants derived from first principles (sec:first_principles_k) — no empirical parameters enter the computation.

### Modified Nodal Analysis (MNA) Solver

Because the computation must be fully self-contained (independent of external SPICE simulators), a native Python AC solver was implemented using Modified Nodal Analysis. At each angular frequency $\omega = 2\pi f$, the solver:

1. **Parses** the `.cir` netlist to extract nodes and component values ($R$, $L$, $C$).
2. **Builds** the nodal admittance matrix $\mathbf{Y}(\omega) \in \mathbb{C}^{N_u \times N_u}$, where $N_u$ is the number of unknown-voltage nodes (excluding ground and the forced source node). Each passive element contributes:

$$
y_R = \frac{1}{R}, \qquad y_C = j\omega C, \qquad y_L = \frac{1}{j\omega L}
$$

Diagonal entries accumulate the sum of branch admittances at each node; off-diagonal entries are $-y$ for every branch between two unknown nodes.

3. **Injects** the known source voltage ($V_\text{in} = 1$ V) into the right-hand-side vector $\mathbf{J}$ wherever a component connects an unknown node to the source node.
4. **Solves** the linear system $\mathbf{Y} \cdot \mathbf{V} = \mathbf{J}$ via LU decomposition (`numpy.linalg.solve`).
5. **Extracts** the voltage at the output node (`out`) and computes the power transfer: $|H(\omega)|^2 = |V_\text{out}/V_\text{in}|^2$.

The full solver is implemented in `batch_amino_spice_solver.py` (110 lines of Python, no external dependencies beyond NumPy and Matplotlib).

### Reproduction Procedure

The entire computation is reproduced in three commands from the repository root:

```
# Step 1: Generate all 20 SPICE netlists (.cir files)
python src/scripts/vol_5_biology/generate_amino_spice.py

# Step 2: Solve all 20 netlists and generate the batch plot
python src/scripts/vol_5_biology/batch_amino_spice_solver.py

# Step 3 (optional): Verify Glycine/Alanine against NIST FTIR
python src/scripts/vol_5_biology/simulate_ftir_comparison.py
```

Step 1 calls `spice_organic_mapper.py`, which in turn calls `soliton_bond_solver.py` to derive all force constants from first principles at import time. No manual parameter entry is required.

### Results

Table tab:batch_resonance lists the primary absorption notch (deepest transmission minimum) for each amino acid, sorted by resonant wavenumber.

| **Amino Acid** | **Primary Notch (cm$^{-1}$)** | **Depth (dB)** |
|---|---|---|
| Alanine | 1192.1 | $-78.6$ |
| Arginine | 1192.1 | $-73.1$ |
| Asparagine | 1192.1 | $-73.5$ |
| Aspartate | 1192.1 | $-73.5$ |
| Cysteine | 1192.1 | $-79.4$ |
| Glutamate | 1192.1 | $-73.3$ |
| Glutamine | 1192.1 | $-73.3$ |
| Histidine | 1192.1 | $-73.2$ |
| Isoleucine | 1192.1 | $-75.4$ |
| Leucine | 1192.1 | $-74.5$ |
| Lysine | 1192.1 | $-73.5$ |
| Methionine | 1192.1 | $-73.3$ |
| Phenylalanine | 1192.1 | $-79.3$ |
| Proline | 1192.1 | $-74.2$ |
| Serine | 1192.1 | $-75.5$ |
| Threonine | 1192.1 | $-75.6$ |
| Tryptophan | 1192.1 | $-72.9$ |
| Tyrosine | 1192.1 | $-73.0$ |
| Valine | 1343.9 | $-73.1$ |
| Glycine | 2819.1 | $-104.0$ |

*Primary topological absorption notch for all 20 standard L-amino acids, computed via native MNA solver with zero adjustable parameters. 18 of the 20 share an identical resonance at 1192 cm$^{-1}$ (amide fingerprint region).*

**Figure: fig:batch_resonance** — Batch transmission sweep of all 20 standard amino acids via native MNA SPICE solver. Despite varying R-group masses, the topological constraint forces 18 of the 20 amino acids to share a tightly clustered primary absorption pole at 1192 cm$^{-1}$, deep within the amide fingerprint region.

### Physical Interpretation

Three distinct spectral clusters emerge from a computation with *zero* adjustable parameters:

- **General Cluster (18 amino acids):** 1192.1 cm$^{-1}$ ($-73$ to $-79$ dB). The shared $\alpha$-carbon backbone topology dominates the macro-impedance. Because the R-group attaches as a *stub* (shunt branch off the main transmission line), its mass loads the junction node but does not shift the primary series resonance of the backbone chain. This explains why amino acids with widely varying R-group masses — from Alanine (15 Da) to Tryptophan (130 Da) — share the same dominant absorption.

- **Valine Anomaly:** 1343.9 cm$^{-1}$. Valine's isopropyl group branches immediately at the $\beta$-carbon into two methyl stubs, creating an unusually symmetric Y-junction that competes with the backbone's own impedance splitting. This shifts the primary transmission pole by $\sim$12% relative to the main cluster.

- **Glycine (The Hydrogen Stub):** 2819.1 cm$^{-1}$ ($-104$ dB). Glycine's R-group is a single hydrogen atom ($m_H = 1.008$ Da), providing negligible shunt inductance ($L_H \approx 9.7$ fH vs. $L_C \approx 116$ fH for carbon). The vanishing stub load allows the backbone to resonate at a much higher frequency, governed by $f \propto 1/\sqrt{L_\text{eff} C}$ where $L_\text{eff}$ is now dominated by the backbone carbon chain alone. This provides a quantitative, parameter-free explanation for Glycine's anomalous flexibility in protein folding: its electromagnetic transmission window is radically mismatched to all other amino acids, making it a natural impedance discontinuity — a *hinge* — in any peptide chain.

---
