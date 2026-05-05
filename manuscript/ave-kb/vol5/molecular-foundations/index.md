[↑ Vol 5: Topological Biology](../index.md)
<!-- claim-quality (subtree): 239tr4, 4jy0t8, a3rby3, j9l3ww, lm9b3j, oilm45, r6uef4, rppigm, u4vmgk, uowffm, x5z09x, yyhczl -->

> ⛔ **Bootstrap.** Leaves are canonical; this index, the volume index, and the entry-point are *derived* summaries and may suggest implications not supported by the leaves. Before forming any claim about results in this subtopic, load [`../claim-quality.md`](../claim-quality.md) (volume scope) and [`../../claim-quality.md`](../../claim-quality.md) (cross-cutting). Treat the summary text and Key Results entries below as routing only — qualifications and conditions live in the cited leaves and the claim-quality documents.

# Molecular Foundations

This domain establishes the atomic translation layer that converts AVE lattice parameters into biological circuit quantities. Ch. 1 derives the protein backbone length scale from $\ell_{node}$. Ch. 2 derives the electromechanical transduction constant $\xi_\text{topo} = e/\ell_\text{node}$, maps atomic mass to inductance ($L = m/\xi^2$) and bond stiffness to capacitance ($C = \xi^2/k$), validates amino acid SPICE models against FTIR spectroscopy, derives all biological force constants from first principles via Fabry-Perot bond eigenvalues, computes the hydrogen bond from Op4 equilibrium ($d_\text{HB} = 1.754$ Å, $E_\text{HB} = 4.98$ kcal/mol), and establishes membrane phase buffering.

## Key Results

| Result | Statement |
|---|---|
| Electromechanical Transduction Constant | $\xi_\text{topo} \equiv e / \ell_\text{node} = e \, m_e \, c / \hbar \approx 4.149 \times 10^{-7}$ C/m |
| Topological Inductance | $L_\text{atom} = m_\text{atom} / \xi^2_\text{topo}$ [H] |
| Topological Capacitance | $C_\text{bond} = \xi^2_\text{topo} / k_\text{bond}$ [F] |
| Proton-to-Backbone Length Scale | $d_p = 4\hbar/(m_p c) \approx 0.841$ fm $\to$ $d_0 \approx 3.80$ Å |
| Bond eigenvalue formula | $d_\text{eq} = \sqrt{2}\,\sqrt{r_A \cdot r_B} \times \sqrt{T^2(N_\text{eff})/T^2(2)}$ |
| Unified mode loading | $N_\text{eff} = 2 \times (\text{Bond Order}) + \max(N_{s_A}, N_{s_B})/2$ |
| Projected force constant | $k_\text{pred} = (\text{Isotropy}) \times (\text{Balance}) \times d^2E/dd^2 \vert_{d_{eq}}$; 11 biological bonds within $\leq 10\%$ |
| Hydrogen bond distance | $d_\text{HB} = 1.754$ Å (Op4 equilibrium, zero free parameters) |
| Hydrogen bond energy | $E_\text{HB} = 0.2158$ eV $= 4.98$ kcal/mol (experimental: $5.02 \pm 0.05$ kcal/mol) |
| FTIR validation | 10/11 peaks within predicted passband for Glycine and Alanine |
| Batch SPICE | 18/20 amino acids share primary absorption at 1192 cm$^{-1}$ |
| Chignolin RMSD | 2.59 Å backbone RMSD, zero adjustable parameters |
| Membrane yield | $T_c = 278.3$ K ($+5.1^\circ$C); cholesterol buffers to $\sim$485 K |

## Derivations and Detail

| Document | Contents |
|---|---|
| [Biophysics Introduction](./biophysics-intro/index.md) | Ch. 1: lattice pitch to backbone length scale, amino acid impedance classification, Chignolin validation, chiral FRET parallax |
| [Organic Circuitry](./organic-circuitry/index.md) | Ch. 2: transduction constant, mass→inductance, stiffness→capacitance, amino acid SPICE circuits, FTIR test, first-principles force constants, H-bond derivation, membrane phase buffering |
