[↑ Protein Folding Engine (Framework)](./index.md)
<!-- leaf: verbatim -->

## Topological Impedance $Z_{\text{topo}}$: Framework Definition

For each amino acid, the sidechain R-group attaches as a **shunt stub** branching off the backbone transmission line. Its loading effect on the backbone's high-frequency passband (the amide-V resonance, $\omega_0 \approx 2\pi \times 23$ THz) is captured by the complex topological impedance:

> **[Resultbox]** *Topological Impedance (sidechain shunt loading)*
>
> $$
> Z_{\text{topo}} \;\equiv\; \frac{|Z_{\text{backbone}}(\omega_0)|}{|Z_R(\omega_0)|} \;=\; R + jX
> $$

where:
- $Z_{\text{backbone}} = \sqrt{L_{\text{bb}}/C_{\text{bb}}} \approx 17.0\,\Omega$ — characteristic impedance of the peptide unit C$_\alpha$--C'(=O)--N(--H)--C$_\alpha$
- $Z_R = \sqrt{L_R/C_R}$ — sidechain impedance with $L_R = \sum_{\text{atoms}} m_a/\xi_{\text{topo}}^2$, $C_R = \sum_{\text{bonds}} \xi_{\text{topo}}^2/k_b$ summed over the sidechain
- $\omega_0 \approx 2\pi \times 23$ THz — amide-V resonance frequency

### Real / imaginary decomposition

The split $Z_{\text{topo}} = R + jX$ decomposes:
- $R$ (real part) — hydrophobic coupling strength
- $X$ (imaginary part) — charge reactance (frequency-dependent phase shift contribution)

### What's IP-clean vs IP-protected

**This leaf has** (IP-clean framework):
- The definition formula $Z_{\text{topo}} = R + jX$
- The construction principle: sidechain as shunt stub on backbone TL
- The $L_R, C_R$ summation rules over sidechain atoms and bonds

**Held in AVE-Protein engineering compendium** (per Vol 5 Ch 2:722, IP-protected):
- The per-amino-acid quantitative table $Z_{\text{topo}}^i$ for all 20 standard residues (with $R_i$, $X_i$, $|Z|_i$ columns)
- The cascaded ABCD-matrix folding solver implementation
- Multiplexed basis-state initialization for gradient-descent escape

### Why "no empirical fits"

Every $L$ and $C$ comes from atomic mass and bond force constants already derived from substrate axioms in [Vol 5 Ch 2 Organic Circuitry](../../../vol_5_biology/chapters/02_organic_circuitry.tex). Specifically:
- $L = m/\xi_{\text{topo}}^2$ (Axiom 2 TKI: mass-to-inductance via electromechanical transduction constant; see [Electromechanical Transduction Constant](../molecular-foundations/organic-circuitry/electromechanical-transduction-constant.md))
- $C = \xi_{\text{topo}}^2/k_{\text{bond}}$ (Axiom 4 dielectric: stiffness-to-capacitance; see [Bond Stiffness to Capacitance](../molecular-foundations/organic-circuitry/bond-stiffness-to-capacitance.md))
- $k_{\text{bond}}$ derived from Fabry-Pérot bond eigenvalues (see [First-Principles Bond Force Constants](../molecular-foundations/organic-circuitry/first-principles-bond-force-constants.md))

The $Z_{\text{topo}}$ definition therefore inherits the zero-empirical-fit chain from the canonical substrate axioms — only the production-grade evaluation across all 20 residues is held in the engineering compendium.

### Cross-references

> → Primary: [Vol 5 Ch 2 §sec:z_topo_framework](../../../vol_5_biology/chapters/02_organic_circuitry.tex) lines 684-693 — canonical manuscript source
>
> → Primary: [Levinthal's Paradox: Mechanical Resolution](./levinthal-mechanical-resolution.md) — how $Z_{\text{topo}}$ drives the folding mechanism
>
> ↗ See also: [Electromechanical Transduction Constant](../molecular-foundations/organic-circuitry/electromechanical-transduction-constant.md) — derivation of $\xi_{\text{topo}}$ that goes into $L_R, C_R$
