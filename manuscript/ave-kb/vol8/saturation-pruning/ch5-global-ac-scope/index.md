[↑ Saturation and Pruning](../index.md)

# Ch.5 Global $A_c$ Scope

The per-layer vs global $A_c$ collapse paradox, the first-principles correction requiring global sampling of $A^2$, and the evolution to $\Gamma$-driven per-layer pruning.

## Key Results

| Result | Location |
|---|---|
| Per-layer $A_c$ induced catastrophic collapse (40--55% pruned/layer) | [Per-Layer Paradox](per-layer-paradox.md) |
| Global $A_c^2 = \frac{1}{N_{total}} \sum_L \sum_j A_{L,j}^2$ required by Axiom 1 continuity | [Global $A_c$ Correction](global-ac-correction.md) |
| $\Gamma$-driven per-layer sort-and-prune: axiomatically correct solution implementing Axiom 3 | [Gamma Per-Layer](gamma-per-layer.md) |

## Derivations and Detail

| Document | Contents |
|---|---|
| [Per-Layer Paradox](per-layer-paradox.md) | Why local $A_c$ violates Axiom 1 LC cascade continuity |
| [Global $A_c$ Correction](global-ac-correction.md) | Global yield limit formula (pending autotune) |
| [Runtime Shift](runtime-shift.md) | Distribution shift: early layers 2--15% pruned, late layers 60--86% |
| [Gamma Per-Layer](gamma-per-layer.md) | Per-layer reflection budget algorithm; three-generation evolution |

## Contents

- [The Paradox of Per-Layer Buckling](per-layer-paradox.md) — per-layer $A_c$ causes catastrophic collapse
- [The First-Principles Correction: Global $A_c$](global-ac-correction.md) — global yield limit derivation
- [Runtime Distribution Shift](runtime-shift.md) — early passband vs late strain pruning distribution
- [Evolution to $\Gamma$-Driven Per-Layer Pruning](gamma-per-layer.md) — corrected algorithm; Axiom 3 implementation
