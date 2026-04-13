[↑ Ch.5 Dark Sector](index.md)
<!-- leaf: verbatim -->

## The Radial Acceleration Relation (RAR)

McGaugh et al. (2016) discovered a universal empirical law across 153 SPARC galaxies: the observed acceleration correlates tightly with the baryonic acceleration via a single parameter $a_0$. The empirical interpolation function is:

> **[Resultbox]** *McGaugh Empirical RAR*
>
> $$
> g_{obs} = \frac{g_{bar}}{1 - \exp\!\left(-\sqrt{g_{bar}/a_0}\right)}
> $$

<!-- label: eq:rar_mcgaugh -->

The AVE Axiom 4 saturation (Eq. eq:saturation\_mond) reproduces the same asymptotes:

- $g_{bar} \ll a_0$: both yield $g_{obs} \to \sqrt{g_{bar} \cdot a_0}$ (deep MOND)
- $g_{bar} \gg a_0$: both yield $g_{obs} \to g_{bar}$ (Newtonian)

The physics engine implements both via `galactic_rotation.radial_acceleration_relation()`.

---
