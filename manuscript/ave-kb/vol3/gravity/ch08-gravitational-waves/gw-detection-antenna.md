[↑ Ch.8 Gravitational Waves](index.md)
<!-- leaf: verbatim -->
<!-- path-stable: referenced from vol3 as sec:gw_detection -->

---

## GW Detection: The Impedance Antenna

A gravitational wave detector is an impedance antenna. LIGO's 4 km Fabry--Perot arms form resonant cavities in the LC vacuum, where each light bounce amplifies the GW-induced impedance modulation.

The passing GW strain $h$ perturbs the local vacuum impedance:

> **[Resultbox]** *GW-Induced Impedance Perturbation*
>
> $$
> \delta Z = Z_0 \cdot h
> $$

The accumulated phase shift after $N$ bounces is:

> **[Resultbox]** *Fabry-Perot Accumulated Phase Shift*
>
> $$
> \Delta\phi = \frac{2\pi f_{GW}}{c} \cdot L \cdot N \cdot h
> $$

For LIGO ($L = 4$ km, $N = 280$, $h = 10^{-21}$, $f = 100$ Hz), $\Delta\phi \approx 2.3 \times 10^{-21}$ rad---resolved via homodyne readout against 750 kW circulating laser power.

The strain sensitivity is bounded by two quantum noise sources: shot noise (phase) and radiation pressure (amplitude), whose geometric mean is the Standard Quantum Limit:

> **[Resultbox]** *Standard Quantum Limit (Strain)*
>
> $$
> h_{SQL}(f) = \sqrt{h_{shot}^2 + h_{RP}^2}
> $$

The lattice voltage ratio for LIGO GW is:

> **[Resultbox]** *LIGO GW Saturation Ratio*
>
> $$
> \frac{V_{GW}}{V_{\text{snap}}} \approx 1.4 \times 10^{-28}
> $$

Twenty-eight orders of magnitude below saturation. The vacuum is a *perfect* lossless transmission line for gravitational waves, exactly as observed.

---
