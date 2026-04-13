[↑ Protein Folding](../index.md)
<!-- leaf: verbatim -->
<!-- path-stable: referenced from vol5 as sec:op2_crossing -->

# Op2 Topological Crossing Correction

## Physical Origin

At the atomic scale, the $2s$ soliton crosses through the $1s$ worldline twice per radial oscillation. Each same-spin crossing costs $\delta E = E_{\rm ABCD} \times P_C/4$, where $P_C = 8\pi\alpha \approx 0.1834$ is the lattice packing fraction (Axiom 3). This is not a steric effect---it is a *topological* cost arising from the Op2 crossing operator.

At the protein scale, the backbone chain can form loops and knots. When one backbone segment crosses through another, the crossing event is topologically identical to the atomic Op2: the propagating soliton (backbone vibrational mode) must traverse a region already occupied by another soliton (the crossed segment).

## Derivation

Let $c_{\min}$ be the minimum crossing number of the backbone knot type---a topological invariant:

| Knot type | $c_{\min}$ | |
|---|---|---|
| Unknot (trivial) | 0 | Most natural proteins |
| Trefoil $3_1$ | 3 | YibK, YbeA |
| Figure-eight $4_1$ | 4 | Rare |
| Cinquefoil $5_1$ | 5 | Not yet observed |

Each crossing carries the same Op2 cost as the atomic case. The total topological crossing energy penalty is:

> **[Resultbox]** *Op2 Crossing Correction (Protein Scale)*
>
> $$\delta E_{\rm knot} = c_{\min} \times \frac{P_C}{4} \times E_{\rm coupling} = c_{\min} \times 2\pi\alpha \times E_{\rm coupling}$$

where $E_{\rm coupling}$ is the backbone coupling energy (bond eigenvalue from the $S_{11}$ minimiser) and $P_C/4 = 2\pi\alpha \approx 0.04587$ is the per-crossing fractional cost.

## Computing $c_{\min}$

Given the 3D backbone coordinates $\{\mathbf{r}_1, \ldots, \mathbf{r}_N\}$, the crossing number is computed from the Gauss linking integral applied to the closed backbone curve (with a virtual closure connecting the termini):

$$c = \frac{1}{4\pi} \oint \oint \frac{(\mathbf{r}_1 - \mathbf{r}_2) \cdot (d\mathbf{r}_1 \times d\mathbf{r}_2)}{|\mathbf{r}_1 - \mathbf{r}_2|^3}$$

In practice, the Alexander polynomial or the KnotFinder algorithm provides $c_{\min}$ from any smoothly closed backbone trace.

## Quantitative Predictions

For a backbone coupling energy $E_{\rm coupling} \sim 15$ kcal/mol (typical amide bond eigenvalue):

| **Knot type** | $c_{\min}$ | $\delta E_{\rm knot}$ | **Prediction** |
|---|---|---|---|
| Unknot | 0 | 0 | Energetically preferred |
| Trefoil | 3 | 2.1 kcal/mol | Rare; requires deep topology |
| Figure-eight | 4 | 2.7 kcal/mol | Very rare |
| Cinquefoil | 5 | 3.4 kcal/mol | Not observed |

Three testable consequences emerge:

1. **Most proteins are unknotted.** The Op2 penalty makes $c = 0$ the global minimum in the vast majority of sequence/topology space. Experimentally, $\sim 1\%$ of PDB structures contain knots---consistent with a $\sim 2$ kcal/mol barrier.
2. **Knotted proteins require compensating stabilisation.** Known trefoil-knotted proteins (e.g., YibK, YbeA) have deeply buried hydrophobic cores whose packing energy exceeds the 2.1 kcal/mol Op2 penalty.
3. **The crossing penalty is quantised.** Unlike the continuous steric potential (Op9), the Op2 correction is an integer multiple of $2\pi\alpha \times E_{\rm coupling}$. This predicts discrete "allowed" and "forbidden" knot types---a topological selection rule for protein architecture.

---
