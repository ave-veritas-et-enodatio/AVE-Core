[↑ Protein Folding](../index.md)
<!-- leaf: verbatim -->

# Op2 vs. Op9: Complementary Corrections

The Op2 crossing correction and the Op9 steric reflection operate on different levels:

| | **Op9 (steric)** | **Op2 (crossing)** |
|---|---|---|
| Nature | Pairwise, geometric | Global, topological |
| Input | Interatomic distances $d_{ij}$ | Crossing number $c_{\min}$ |
| Scale | Continuous (soft wall) | Quantised (integer $c$) |
| Effect | Penalises spatial overlap | Penalises chain threading |
| Status | Implemented (Op9) | Predicted (this section) |

Op9 prevents atoms from occupying the same space. Op2 prevents the backbone from *threading through itself* without spatial overlap---a purely topological constraint. Together, they constitute the complete geometric $+$ topological exclusion principle for folded proteins.

---
