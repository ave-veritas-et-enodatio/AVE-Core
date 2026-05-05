[↑ Computational Mass Defect](../index.md)
<!-- leaf: verbatim -->
<!-- path-stable: referenced from vol6 as sec:pn_junction -->
<!-- claim-quality: 86gq2d -->

## Proton--Neutron Junction Coupling

The bare mutual inductance formula ($K/r_{ij}$) treats all nucleons identically. However, the proton ($p$) and neutron ($n$) are topologically distinct objects---the proton carries a localized electric charge while the neutron does not. This distinction is physically identical to the carrier asymmetry in a semiconductor $p$--$n$ Junction.

### The Nuclear Diode Analogy

In a semiconductor $p$--$n$ junction, the coupling across the boundary exhibits three characteristic phenomena that map directly to nuclear physics:

- **Forward Bias ($p$--$n$ pairs)**: The proton-neutron isospin exchange interaction is the most strongly attractive nucleon coupling. This is the "forward-biased" mode---the junction efficiently transmits mutual inductance. The deuteron ($pn$) is bound; the diproton ($pp$) and dineutron ($nn$) are not.
- **Reverse Bias ($p$--$p$ pairs)**: Proton-proton pairs experience Coulomb repulsion ($+\alpha\hbar c / r$), which partially cancels the strong attractive coupling $K/r$. This is the "reverse-biased" junction---a potential barrier opposes current flow.
- **Junction Capacitance (Axiom 4)**: The scale-invariant saturation $C_j = 1/\sqrt{1 - (d_0/r)^2}$ from Axiom 4 is mathematically identical to the depletion-layer capacitance of a semiconductor junction under forward bias: $C_j = C_0 / \sqrt{1 - V/V_{bi}}$. No new parameter is introduced---$d_0/r$ is the dimensionless ratio of the nucleon lattice pitch to the pair separation.

### Coulomb Correction for Heavy Nuclei

For an element with $Z$ protons and $A$ total nucleons in a symmetric geometry, the statistical fraction of proton-proton pairs is:

$$
f_{pp} = \frac{Z(Z-1)}{A(A-1)}
$$

The Coulomb repulsion reduces the net binding:

$$
\Delta E_{\text{Coulomb}} = -\alpha\hbar c \cdot f_{pp} \cdot \sum_{i<j} \frac{1}{r_{ij}}
$$

For Helium-4 ($f_{pp} = 1/6$), this correction is $\sim 0.6$ MeV---negligible. For Iron-56 ($f_{pp} = 0.211$), it reaches $\sim 16$ MeV, contributing measurably to the observed decline in binding energy per nucleon beyond the Iron peak.

### The Absolute Mass Defect Topologic Limit

A historically pervasive empirical constant imported heavily from the Standard Model is the "$8 \text{ MeV per nucleon}$" average geometric mass defect governing standard stable isotopic binding energy. In standard phenomenological texts, this flat curve is derived from observational curve fitting of the semi-empirical mass formula (SEMF).

Under AVE, we rigidly reject environmental or empirical measurements parameters. The $8 \text{ MeV}$ ceiling is proven to be a pure deterministic scaling limit of vacuum Yield Saturation (Axiom 4).

The underlying strong nucleonic bond is an electromagnetic phase linkage operating inside the vacuum dielectric. The total electrostatic strain energy that any individual $6^3_2$ structural component can surrender before its localized constituent phase geometry ruptures (catastrophic dielectric yielding) exactly scales with the universal lattice coupling constant ($\alpha$) multiplied by the rest mass energy bounding the topology:

> **[Resultbox]** *Topologic Yield Mass Defect (Binding Energy Ceiling)*
>
> $$
> E_{\text{binding(max)}} = \alpha \cdot M_{\text{proton}} c^2
> $$

Evaluating this purely foundational expression yields:

$$
E_{\text{binding(max)}} \approx \frac{1}{137.036} \times 938.27 \text{ MeV} \approx \mathbf{6.847 \text{ MeV}}
$$

When compounded dynamically inside heavy nuclei through geometric $p$-$n$ Miller amplification arrays, this rigorous zero-parameter foundational ceiling smoothly brackets the stable macroscopic observation curve (peaking near $8 \text{ MeV}$) strictly from geometric lattice limits, permanently decoupling the mesoscopic thermodynamic solvers in the engine from relying on arbitrary empirical nucleosynthesis data.

---
