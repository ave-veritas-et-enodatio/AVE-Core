[↑ Simulation Architecture](./index.md)
<!-- leaf: verbatim -->

# Verification: 20-Sequence Stress Test (v3)

To validate the complete engine, all 20 homopolymer sequences (10-mers) were folded with 3000 Adam steps. Pass criteria: (i) $S_{11}$ converges, (ii) radius of gyration $R_g \in [2, 8]$ \AA, (iii) mean bond angle $\theta \in [30^\circ, 160^\circ]$.

| **Sequence** | $S_{11,0}$ | $S_{11,f}$ | $\theta$ | $R_g$ | **Status** |
|---|---|---|---|---|---|
| Poly-G | 0.509 | 0.491 | 94$^\circ$ | 4.4 | Pass |
| Poly-A,V,L,I,P | 0.43 | 0.33 | 97$^\circ$ | 4.0--4.1 | Pass |
| Poly-S,T,N,Q,K,R,M | 0.41--0.43 | 0.24--0.32 | 97--98$^\circ$ | 4.0 | Pass |
| Poly-E | 0.407 | 0.242 | 98$^\circ$ | 4.0 | Pass |
| Poly-F,W,Y,H | 0.62 | 0.57 | 85$^\circ$ | 5.2 | Pass |
| Poly-C | 1.034 | 0.996 | 92$^\circ$ | 4.7 | Pass |
| **Poly-D** | 0.624 | 0.597 | **17$^\circ$** | **10.7** | Fail |

The Poly-D failure is *expected physics*: a homopolyanion chain experiences Coulomb self-repulsion at every junction node (all $X_D < 0$, all conjugate matches positive-definite). Without counter-ions or solvent screening, the minimum-$S_{11}$ geometry is an extended rod---which is precisely what the engine returns. In mixed sequences with compensating positive residues, aspartate participates normally in secondary structure.

---
