[↑ Protein Folding Engine (Framework)](./index.md)
<!-- leaf: verbatim -->

## Regime Classification of Biological Length Scales

| Scale | Regime | $\Delta\phi/\alpha$ | Physical Character |
|---|---|---|---|
| Covalent bond (~1.5 Å) | II (Yield) | ~0.5 | Soliton potential well |
| Backbone (C$_\alpha$--C$_\alpha$ 3.8 Å) | I--II | ~0.1 | LC transmission line |
| R-group stub (~5--10 Å) | I (Linear) | ≪ 0.1 | Passive shunt filter |
| Peptide chain (~nm) | I (Linear) | ≪ 0.01 | Cascaded resonator network |
| Folded protein (~2--10 nm) | I (Linear) | ≪ 0.01 | Impedance-matched cavity |

**All biological circuitry operates in Regime I (linear, lossless), except at the covalent bond core where the vacuum strain approaches the Axiom 4 yield limit.** This explains why biology is fundamentally an AC resonance phenomenon: the linear regime permits lossless energy transfer across the entire molecular network.

### Why this matters for the folding framework

The regime classification is what makes the [Levinthal mechanical resolution](./levinthal-mechanical-resolution.md) work:

- **Covalent bond cores in Regime II** (yield) are where the [A-034 saturation kernel](../../common/universal-saturation-kernel-catalog.md) operates — these are the "snap points" of the folding mechanism (where $A \to 1$ on a critical bond)
- **Backbone in Regime I-II** (transition) carries the transmission-line cascade that supports the impedance-matching dynamics
- **R-group, chain, and folded-protein scales all in Regime I** (linear) means the [$Z_{\text{topo}}$ shunt loading](./z-topo-definition.md) and $|S_{11}|^2$ minimization are well-defined linear-circuit-theory calculations, NOT requiring non-linear saturation-kernel treatment at those scales

This is what justifies the "no configuration search" framing: the non-linear physics (A-034 snap) operates ONLY at the covalent-bond core; everything else is linear cascaded-TL impedance matching, which has a unique solution (the native fold).

### Cross-references

> → Primary: [Vol 5 Ch 2 §sec:z_topo_framework](../../../vol_5_biology/chapters/02_organic_circuitry.tex) lines 725-741 — canonical manuscript source (regime table)
>
> → Primary: [Levinthal's Paradox: Mechanical Resolution](./levinthal-mechanical-resolution.md) — how regime classification enables the folding mechanism
>
> → Primary: [Universal Saturation-Kernel Catalog (A-034)](../../common/universal-saturation-kernel-catalog.md) — covalent-bond Regime II yield is the A-034 protein-folding instance
>
> ↗ See also: Vol 1 Ch 7 regime classification (canonical four-regime framework) — biological scales as application of the general regime framework
