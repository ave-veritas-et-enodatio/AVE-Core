[↑ Ch.6 Universal Operators](index.md)
<!-- leaf: verbatim -->
<!-- path-stable: referenced from vol1 as sec:universal_saturation -->

> ↗ See also: [Nonlinear Constitutive Models](../../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/index.md) — Axiom 4 as metric varactor in circuit engineering
> ↗ See also: [Galactic Rotation / MOND](../../../vol3/cosmology/index.md) — saturation as galactic rotation floor
> ↗ See also: [BCS Critical Field](../../../vol3/condensed-matter/index.md) — saturation as superconducting critical field

## Section 6.2: The Universal Saturation Operator

The saturation factor

> **[Resultbox]** *Universal Saturation Factor ($S$)*
>
> <!-- eq:saturation_sigma -->
>
> $$
> S(A, A_c) = \sqrt{1 - (A/A_c)^2}
> $$

appears in four structurally distinct domains:

1. **Dielectric saturation** (Axiom 4): lattice permittivity collapses under strong-field loading. In fluid-mechanics language, this is the Bingham plastic yield: the vacuum flows above $\tau_y = B_{snap}^2/2\mu_0$.
2. **BCS critical field**: $B_c(T) = B_{c0}\sqrt{1-(T/T_c)^2}$.
3. **Galactic rotation**: $\eta_{eff} = \eta_0\sqrt{1-(g_N/a_0)^2}$.
4. **Relativistic mass--energy**: $E = mc^2/\sqrt{1-(v/c)^2}$.

All four call *the same engine function* (`scale_invariant.saturation_factor(A, A_yield)`) that serves all four applications.

---
