[↑ Ch.8 Gravitational Waves](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-07kd5v]
path-stable: "referenced from vol3 as sec:gw_detection"
-->

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

Twenty-eight orders of magnitude below saturation. The vacuum is a *perfect* lossless transmission line for gravitational waves, ~~exactly as observed~~ *(clause struck 2026-08-02 per Rule 12 --- preserved, not deleted; see the note below)*.

> **[2026-08-02 --- Reading-A bulk admixture (sibling propagation)]** The "exactly as observed" completeness framing is struck for the same reason as in [`gw-propagation-lossless.md`](gw-propagation-lossless.md), which carries the canonical 2026-08-02 statement. Under **Reading-A** (the standing physics as of 2026-07-20) the framework **additionally** predicts a bulk (longitudinal P-wave) admixture radiating on top of the shear decay at $O(1)$ coupling, $F_{\text{bulk}}/F_{\text{shear}} \approx 0.03$--$0.12$ --- carrying a **LIVE** pulsar exclusion of an independent $O(1)$ bulk radiative port plus an **OPEN** constituent-cage fork. The deeply-linear-regime losslessness of the *shear* channel stated above is unaffected and stands; the claim of an exact and complete match to observation does not. Note this leaf describes **detection**: what LIGO's antenna reads out is the observed transverse-shear channel, and that identification is Reading-independent and untouched. Ruled state: Grant's F4 → option (a) (`_orchestration/2026-07-10_rulings-docket.md:2573`; `_orchestration/2026-07-20_pending-rulings-and-frontier-queue.md:113`), executed in the printed chapter by PR #771 (`manuscript/vol_3_macroscopic/chapters/08_gravitational_waves.tex:107`). **The bulk/shear double-count contradiction (Q1-REVERT) remains LIVE and routed** ([`common/port-register.md`](../../../common/port-register.md) line 5) --- Reading-A is the standing physics, not a closure of that contradiction.

---
