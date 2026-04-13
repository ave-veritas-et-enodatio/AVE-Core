[↑ Network Solver](./index.md)
<!-- leaf: verbatim -->

# Complete Circuit Model

The v4 Y-matrix captures three coupling mechanisms: backbone cascade (ABCD segments), H-bond off-diagonal admittance, and $\beta$-sheet even/odd mode coupling. A systematic mapping of biological interactions to circuit elements reveals four additional mechanisms that were computed but not connected to the Y-matrix.

## Biology--Circuit Mapping

Complete biology $\to$ EE circuit element mapping. All coupling constants are derived from the same first-principles parameters ($d_0$, $Q$, $\kappa_\text{HB}$, Slater radii). No new fitted parameters are introduced.

| **Biology** | **EE Circuit** | **Y-Matrix Entry** | **Status** |
|---|---|---|---|
| Backbone chain | Cascade TL | ABCD $\to$ Y diagonal | v3 |
| H-bond (N--H$\cdots$O=C) | Mutual admittance | $Y_{ij}$ off-diagonal | v3 |
| $\beta$-sheet coupling | Coupled microstrip | $Y_e$, $Y_o$ even/odd | v4 |
| Bend angle $\theta$ | Microstrip junction | $C_\text{bend} = (1{-}\cos\theta)/(2\pi^2)$ | v4 |
| Solvent exposure | Radiation conductance | $Y_0 \cdot \text{exposure}$ | v4 |
| N/C-terminus | **Matched termination** | $Y[0,0], Y[N{-}1,N{-}1] \mathrel{+}= Y_0$ | **v4.1** |
| Disulfide (C--C) | **Permanent coupling** | $Y_{ij} \propto \kappa_\text{HB} \cdot d_0/d_\text{SS}$ | **v4.1** |
| Aromatic stacking | **Capacitive coupling** | $Y_{ij} \propto \kappa_\text{HB} \cdot e^{-d/d_0}$ | **v4.1** |
| Salt bridge (D/E$\leftrightarrow$K/R) | **Transformer coupling** | $Y_{ij} \propto \kappa_\text{HB} \cdot d_0/d$ | **v4.1** |

## Chain Termination Impedances

The N- and C-termini carry formal charges (NH$_3^+$, COO$^-$) and are fully solvated. In the circuit model, an unterminated port reflects 100% of incident power ($|\Gamma| = 1$). Adding a matched load $Y_0$ at ports 0 and $N{-}1$ eliminates this artificial boundary reflection:

$$Y_\text{mat}[0,0] \mathrel{+}= Y_0, \qquad Y_\text{mat}[N{-}1,N{-}1] \mathrel{+}= Y_0$$

This is the protein analogue of the 50 $\Omega$ termination in RF filter design.

## Disulfide Bonds

Cysteine pairs forming covalent S--S bonds ($d_\text{SS} = 2.05$ Å) contribute a permanent, strong mutual admittance:

$$Y_\text{SS}(i,j) = \Lambda_\text{Rama} \cdot \kappa_\text{HB} \cdot \frac{d_0}{d_\text{SS}} \cdot \sigma\!\left(\beta(d_\text{SS} + d_0 - d_{ij})\right) \cdot C_i \cdot C_j$$

where $C_i, C_j$ are the cysteine masks and $\sigma$ is the logistic proximity gate.

## Aromatic $\pi$-Stacking

Aromatic sidechains (W, H, Y, F) interact via face-to-face $\pi$-orbital overlap, modelled as a capacitive mutual admittance:

$$Y_\text{arom}(i,j) = \kappa_\text{HB} \cdot e^{-d_{ij}/d_0} \cdot A_i \cdot A_j$$

where $A_i, A_j$ are the aromatic masks.

## Salt Bridges

Opposite-charge residues (D/E$^-$ $\leftrightarrow$ K/R$^+$) form ionic bonds with Coulombic distance dependence:

$$Y_\text{salt}(i,j) = \kappa_\text{HB} \cdot \frac{d_0}{d_{ij}} \cdot \sigma\!\left(\beta(D_\text{HB} + d_0 - d_{ij})\right) \cdot (n_i^- \cdot p_j^+ + p_i^+ \cdot n_j^-)$$

where $n^-$ and $p^+$ are the acidic and basic residue masks, respectively.

## Combined Contact Matrix

The full contact matrix sums all five off-diagonal coupling mechanisms:

$$Y_\text{contact}(i,j) = Y_\text{HB} + Y_\beta + Y_\text{SS} + Y_\text{arom} + Y_\text{salt}$$

<!-- Figure: protein_circuit.png — Protein backbone ABCD cascade as an RF circuit -->

---
