[↑ Biophysics Introduction](../index.md)

<!-- kb-frontmatter
kind: leaf
claims: [u4vmgk, a3rby3]
-->

<!-- original-label: sec:protein_bridge DUPLICATE (also in Ch.3) -->

---

## Protein Backbone: From Proton Radius to Folding
<!-- claim-quality: a3rby3 ($S_{11}$ here is the protein-folding free-energy functional, not the EE reflection coefficient — Vol 5's notation-hazard meaning) -->

The protein $S_{11}$ folding engine uses the C$\alpha$--C$\alpha$
virtual bond distance $d_0 \approx 3.80$ Å as its fundamental
length scale. This traces back to the AVE axioms via:

> **[Resultbox]** *Proton-to-Backbone Length Scale*
>
> $$
> d_p = \frac{4\hbar}{m_p c} \approx 0.841\;\text{fm}
> \;\xrightarrow{\text{nuclear bond}}
> r_{\text{cov}}
> \;\xrightarrow{\text{backbone}}
> d_0 \approx 3.80\;\text{Å}
> $$

The ratio $d_0 / a_0 \approx 7.18$ (where $a_0 = \ell_{\text{node}}
/\alpha$ is the Bohr radius) suggests a geometric origin in the
peptide repeat unit. The amino acid impedance table $Z_{\text{topo}}$
assigns complex impedances (R + jX) to each of the 20 residues,
with $Q_{\text{backbone}} \approx 7$ suppressing reactive coupling.

<!-- claim-quality: u4vmgk (the parameter-free backbone-length-scale derivation chain $d_p \to r_{\rm cov} \to d_0 = 3.80$ Å and the Γ-driven inter-residue impedance map established here are the foundation feeding the Chignolin 2.59 Å backbone-RMSD validation) -->
**Figure: fig:protein_backbone** — Protein backbone impedance from AVE axioms.
**Left:** Full derivation chain from $\ell_{node}$ to
the C$\alpha$--C$\alpha$ peptide bond length $d_0 = 3.80$ Å.
**Centre:** Amino acid impedance spectrum — hydrophobic
(gold), positive/inductive (blue), negative/capacitive (red).
**Right:** Local inter-residue reflection coefficient
$\Gamma$ along a sample peptide sequence; high $|\Gamma|$
indicates folding-driving impedance mismatch.

---
