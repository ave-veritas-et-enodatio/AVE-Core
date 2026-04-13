[↑ Architecture Analysis](../index.md)

# Ch.10 Attention Impedance

The QKV cascaded two-port model for attention heads: per-head impedance $Z_h$, GQA coupling constraints, impedance distribution, and the intersection constraint proving no head is universally dispensable.

## Key Results

| Result | Location |
|---|---|
| Per-head impedance: $Z_h = \|W_Q^{(h)}\|_F \times \|W_K^{(h)}\|_F \times \|W_V^{(h)}\|_F$ | [QKV Impedance](qkv-impedance.md) |
| GQA group impedance: $Z_{\text{group},g} = (\sum_{q \in g} \|W_Q^{(q)}\|_F) \times \|W_K^{(g)}\|_F \times \|W_V^{(g)}\|_F$ | [GQA Constraint](gqa-constraint.md) |
| $\bigcap_{\ell=1}^{L} \text{PruneMask}(\ell) = \emptyset$: zero universally pruneable KV groups | [Intersection Constraint](intersection-constraint.md) |
| Attention heads are topological phase dislocations (Axiom 2 confirmation) | [Axiom 2 Interpretation](axiom2-interpretation.md) |

## Derivations and Detail

| Document | Contents |
|---|---|
| [QKV Impedance](qkv-impedance.md) | Per-head $Z_h$ formula; $W_O$ exclusion rationale |
| [GQA Constraint](gqa-constraint.md) | Grouped-Query Attention coupling; KV-group level impedance |
| [Impedance Distribution](impedance-distribution.md) | Heavy-tailed per-layer distribution; cross-layer correlation |
| [Intersection Constraint](intersection-constraint.md) | Single-layer vs all-layer mask; empty intersection result |
| [Axiom 2 Interpretation](axiom2-interpretation.md) | Topological phase dislocations; inter-layer coupling via residual bus |

## Contents

- [QKV Impedance](qkv-impedance.md) — per-head impedance from Q, K, V norms
- [GQA Constraint](gqa-constraint.md) — Grouped-Query Attention coupling constraint
- [Impedance Distribution](impedance-distribution.md) — heavy-tailed distribution; cross-layer correlation
- [The Intersection Constraint](intersection-constraint.md) — empty intersection proves no universal pruning
- [Axiom 2 Interpretation](axiom2-interpretation.md) — attention heads as topological dislocations
