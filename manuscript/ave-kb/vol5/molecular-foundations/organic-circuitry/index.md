[↑ Molecular Foundations](../index.md)
<!-- claim-quality (subtree): 4jy0t8, j9l3ww, lm9b3j, oilm45, r6uef4, rppigm, uowffm, x5z09x, yyhczl -->

# Organic Circuitry

Ch. 2 derives the complete electromechanical translation layer that maps atomic mass to inductance and bond stiffness to capacitance via the transduction constant $\xi_\text{topo}$, constructs amino acid SPICE circuit models, validates against FTIR spectroscopy, derives all biological force constants from first principles, computes the hydrogen bond from Op4 equilibrium, and establishes membrane phase buffering via cholesterol.

## Key Results

| Result | Statement |
|---|---|
| Electromechanical Transduction Constant | $\xi_\text{topo} \equiv e / \ell_\text{node} = e \, m_e \, c / \hbar \approx 4.149 \times 10^{-7}$ C/m |
| Topological Inductance of an Atom | $L_\text{atom} = m_\text{atom} / \xi^2_\text{topo}$ [Henries] |
| Topological Capacitance of a Bond | $C_\text{bond} = \xi^2_\text{topo} / k_\text{bond}$ [Farads] |
| Self-consistency | $f_\text{res} = \frac{1}{2\pi\sqrt{LC}} = \frac{1}{2\pi}\sqrt{k/\mu}$ recovers mechanical resonance; C--H stretch: 3003 cm$^{-1}$ vs experimental $\sim$3000 cm$^{-1}$ |
| FTIR falsification | Glycine: 10/11 FTIR peaks within predicted passband; Alanine: 10/11 |
| Batch SPICE 20 amino acids | 18/20 share primary notch at 1192 cm$^{-1}$; Valine at 1344 cm$^{-1}$; Glycine at 2819 cm$^{-1}$ |
| Projected Macroscopic Force Constant | $k_\text{pred} = (\text{Isotropy}) \times (\text{Balance}) \times d^2E/dd^2 \vert_{d_{eq}}$ |
| Bond eigenvalue | $d_\text{eq} = \sqrt{2}\,\sqrt{r_A \cdot r_B} \times \sqrt{T^2(N_\text{eff})/T^2(2)}$; $N_\text{eff} = 2 \times (\text{Bond Order}) + \max(N_{s_A}, N_{s_B})/2$ |
| H-bond distance | $d_\text{HB} = 1.754$ Å (Op4 equilibrium) |
| H-bond energy | $E_\text{HB} = U_\text{raw} \times (1-\phi) = 0.2158$ eV $= 4.98$ kcal/mol ($<0.9\%$ of experimental $5.02 \pm 0.05$ kcal/mol) |
| O--O distance | $d_\text{OO} = d_\text{OH} + d_\text{HB} = 2.727$ Å (NIST ice I$_h$: 2.76 Å, $-1.2\%$) |
| Membrane yield temperature | $T_c = E_{HB} / (n_{coop} \cdot k_B) \approx 278.3$ K $= +5.1^\circ$C (water density max at $+4.0^\circ$C, $0.40\%$) |
| Cholesterol buffered yield | $A_{yield}^{\text{buffered}} = 1 + \varphi \approx 1.7405$; $T_c^{\text{buffered}} \approx 485$ K |

## Derivations and Detail

| Document | Contents |
|---|---|
| [Electromechanical Transduction Constant](./electromechanical-transduction-constant.md) | Resultbox; eq:xi_topo definition and derivation |
| [Mass to Inductance](./mass-to-inductance.md) | Resultbox "Topological Inductance of an Atom"; eq:L_atom; tab:inductances |
| [Bond Stiffness to Capacitance](./bond-stiffness-to-capacitance.md) | Resultbox "Topological Capacitance of a Bond"; eq:C_bond; tab:capacitances |
| [Self-Consistency Verification](./self-consistency-verification.md) | eq:f_check, eq:Z_check, eq:v_check; mechanical frequency/impedance/speed cross-check |
| [Transceiver Backbone](./transceiver-backbone.md) | Backbone RLC circuit model: source, payload, sink architecture |
| [Thermal THz Noise](./thermal-thz-noise.md) | Biological power supply: thermal phonons and ATP hydrolysis |
| [R-Group Filter Stack](./r-group-filter-stack.md) | Side-chain impedance filter classification |
| [Chirality as Phase Polarity](./chirality-phase-polarity.md) | L/D chirality as $\pm 90^\circ$ phase assignment |
| [Simulation Results: Zero-Parameter](./simulation-results-zero-parameter.md) | Transfer function results for 6 amino acids; fig:amino_resonance |
| [FTIR Falsification Test](./ftir-falsification-test.md) | AVE vs NIST comparison; fig:ftir_comparison; pass/fail criteria |
| [Peptide Chain Extension Test](./peptide-chain-extension-test.md) | Chain mass sensitivity; fig:chain_sensitivity |
| [Batch SPICE: 20 Amino Acids](./batch-spice-20-amino-acids.md) | sec:batch_spice; batch transmission sweep; tab:batch_resonance; fig:batch_resonance |
| [First-Principles Bond Force Constants](./first-principles-bond-force-constants.md) | sec:first_principles_k; Fabry-Perot bond eigenvalue derivation; resultbox "Projected Macroscopic Force Constant"; tab:first_principles_k |
| [H-bond Op4 Equilibrium](./hbond-op4-equilibrium.md) | sec:hbond_derivation; $d_\text{HB}=1.754$ Å, $E_\text{HB}=4.98$ kcal/mol; tab:translation_matrix |
| [Membrane Phase Buffering](./membrane-phase-buffering.md) | sec:membrane_phase_buffering; LLCP wedge topology; cholesterol as topological phase buffer |
