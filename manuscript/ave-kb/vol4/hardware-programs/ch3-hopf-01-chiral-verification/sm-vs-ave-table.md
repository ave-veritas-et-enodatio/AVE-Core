[↑ Ch.3 HOPF-01 Chiral Verification](index.md)
<!-- leaf: verbatim -->

## SM vs. AVE Prediction Comparison

The critical question: how does the SM baseline differ from the AVE prediction? The AVE chiral correction shifts each resonant frequency by $f_{AVE} = f_{SM}/(1 + \alpha \cdot pq/(p+q))$.

| Knot | $f_{SM}$ (GHz) | $f_{AVE}$ (GHz) | $\Delta$(SM$\to$AVE) | AVE (ppm) | SNR |
|---|---|---|---|---|---|
| $(2,3)$ | 1.047 | 1.038 | $9.1$ MHz | 8,681 | $11\times$ |
| $(2,5)$ | 0.787 | 0.778 | $8.1$ MHz | 10,317 | $11\times$ |
| $(3,5)$ | 0.740 | 0.730 | $10.0$ MHz | 13,498 | $8\times$ |
| $(3,7)$ | 0.630 | 0.621 | $9.5$ MHz | 15,093 | $8\times$ |
| $(3,11)$ | 0.505 | 0.496 | $8.5$ MHz | 16,910 | $7\times$ |
| CONTROL | 1.047 | 1.047 | $0.0$ MHz | 0 | --- |

The AVE chiral signal (8.1--10.0 MHz shift) exceeds the classical crossing coupling noise by $7$--$11\times$ across all knots. Crucially, the two effects have different functional dependences: the AVE shift scales as $pq/(p+q)$ (sublinear, topological invariant) while the classical coupling scales as $N_{cross}/L_{self}$ (superlinear, geometry-dependent). The zero-topology control antenna provides a direct null test.

### Discriminating Observables

| Observable | SM prediction | AVE prediction | Discriminating? |
|---|---|---|---|
| $\Delta f/f$ at harmonics | frequency-dependent | constant (same ppm) | **Yes** |
| $Q$ vs. topology | topology-independent | topology-independent | No (null test) |
| Temperature dependence | none | none | No (null test) |
| Enantiomeric shift | identical | potentially different | **Yes**$^*$ |
| Wire length scaling | $\propto 1/L$ | constant | **Yes** |
| Radiation polarization | geometry-determined | geometry-determined | No (null test) |

$^*$Depends on whether chiral coupling has a signed or unsigned winding number.

The null tests (items 2, 3, 6) are valuable because they constrain the *absence* of systematic errors. The positive discriminators (items 1, 4, 5) provide independent falsification tests that can be performed with the existing HOPF-01 hardware.

### Classical Coupling as Confounding Variable

The scaling shapes are **fundamentally different**: AVE scales smoothly as $pq/(p+q)$ (sublinear, ratio 1.95$\times$ across the range), while classical coupling scales as $N_{cross}/L_{self}$ (superlinear, ratio 3.96$\times$).

| Knot | $pq/(p{+}q)$ | $N_{cross}$ | AVE (norm) | Classical (norm) |
|---|---|---|---|---|
| $(2,3)$ | 1.200 | 3 | 1.00 | 1.00 |
| $(2,5)$ | 1.429 | 5 | 1.19 | 1.31 |
| $(3,5)$ | 1.875 | 10 | 1.56 | 2.49 |
| $(3,7)$ | 2.100 | 14 | 1.74 | 3.04 |
| $(3,11)$ | 2.357 | 22 | 1.95 | 3.96 |

An experiment with five knots plus a zero-topology control can distinguish these functional forms by model selection (AIC/BIC).

---
