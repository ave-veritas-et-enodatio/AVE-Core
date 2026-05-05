[↑ Organic Circuitry](../index.md)

<!-- kb-frontmatter
kind: leaf
claims: [j20lz8]
-->

---

## Peptide Chain Extension Test

If the amino acid functions as a true transmission line element, then cascading $N$ residues in series should produce predictable filter-like behavior: narrowing of the passband (higher selectivity) and preservation of R-group differentiation.

**Figure: fig:chain_sensitivity** — Peptide chain extension and sensitivity analysis. **Top left:** Polyglycine chains of length 1, 2, 5, and 10 residues — the backbone passband narrows with increasing chain length, confirming transmission line behavior. **Top right:** Polyalanine chains show the same narrowing but with a different passband shape due to the heavier R-group. **Bottom left:** R-group differentiation persists at chain length 5; mixed sequences produce unique spectral signatures. **Bottom right:** Mass sensitivity sweep — peak frequency scales as $f \propto 1/\sqrt{m}$ (verified to $<$0.03% for $0.5\times$ to $1.5\times$ mass), confirming genuine LC resonance behavior.

The mass sensitivity test (bottom right of Figure fig:chain_sensitivity) quantitatively verifies the LC resonance prediction: scaling all atomic masses by a factor $\alpha$ shifts the passband peak as $f_\text{peak} \propto 1/\sqrt{\alpha}$, matching the expected $f = 1/(2\pi\sqrt{LC})$ scaling to better than 0.03%. At extreme mass doubling ($\alpha = 2.0$), the transfer function undergoes a mode-hop to a different resonant peak — an honest physical effect where the lowest-loss transmission path through the circuit shifts to a higher-order mode.

---
