[↑ Ch.11: Experimental Bench Falsification](../index.md)
<!-- leaf: verbatim -->

## Protocol 11: Sagnac-Parallax (Galactic Wind Vectoring) — AVE predicts NULL, corroborated by Brillet–Hall + Wolf

> **Scope correction (2026-05-16 audit):** This protocol was originally framed as a forward prediction of a 2 M-rad diurnal Sagnac modulation from Earth's 370 km/s motion through the $\mathcal{M}_A$ lattice rest frame. Audit found the prediction is **doubly killed by AVE's own physics**, before Brillet–Hall + Wolf null bounds are even considered. The protocol survives as a **corroborative-null** prediction (AVE predicts no signal; existing static-Sagnac null bounds CORROBORATE this prediction). Full reconciliation at [`vol1/dynamics/ch4-continuum-electrodynamics/preferred-frame-and-emergent-lorentz.md`](../../../vol1/dynamics/ch4-continuum-electrodynamics/preferred-frame-and-emergent-lorentz.md).

### Setup

The absolute rest-frame of the $\mathcal{M}_A$ lattice is identified with the CMB rest frame to high precision (per AVE-QED Q-G24). The solar system travels through this frame at $\sim 370$ km/s (CMB dipole velocity). A static Earth-bound Sagnac fiber-optic loop oriented horizontally and observed over 24 hours might naively be expected to register a diurnal sinusoidal phase modulation as the Earth's rotation vectors the static optical baseline against the galactic wind.

### Why AVE predicts NULL

**(i) Closed-loop geometry kills the signal independently of substrate physics.** The closed-loop integral of a uniform velocity field $\vec{v}_{\text{galactic}}$ around any Sagnac loop is identically zero: $\oint \vec{v} \cdot d\vec{l} = 0$ for any $\vec{v}$ that is spatially uniform across the loop. The galactic wind is uniform on the scale of a tabletop fiber loop, so the Sagnac integral cancels regardless of any drag mechanism.

**(ii) Open-loop Fizeau-style drift is cubic-symmetry-suppressed by $\sim 10^{-22}$.** Even if a non-closed-loop or path-asymmetric configuration is used to extract a Fizeau-class drift, the $\mathcal{M}_A$ lattice's diamond-cubic ($Fd\bar{3}m$) symmetry suppresses observable anisotropy at low momentum $q \ll \pi/\ell_{node}$ to $\delta_{aniso} \sim (q\ell_{node})^4$. At optical wavelengths ($\lambda \sim 1$ μm, $q \sim 10^7$ m$^{-1}$):

$$\delta_{aniso} \sim (q\ell_{node})^4 \approx 2.2 \times 10^{-22}$$

Any putative galactic-wind-driven phase shift is suppressed by this factor — far below detectability at any current or near-term precision.

### Empirical corroboration (existing bounds, NOT future tests)

- **Brillet–Hall (1979):** $\Delta c/c < 5 \times 10^{-9}$ at optical scales — null
- **Wolf et al. (2003–2010):** $\Delta c/c < 10^{-17}$ via fiber-based tests — null
- **Modern cavity comparisons:** $\Delta c/c < 10^{-18}$ — null

All three are consistent with AVE's prediction of $\delta_{aniso} \sim 10^{-22}$ at optical wavelengths. These are not falsifications of AVE; they are corroborations of cubic-symmetry suppression.

### What WOULD constitute a falsification

A genuinely AVE-distinctive preferred-frame test must probe wavelengths $\lesssim \ell_{node}$ where cubic-symmetry averaging no longer suppresses observable anisotropy. The surviving Trans-Planckian probe is [`vol4/falsification/ch12-falsifiable-predictions/binary-kill-switches.md`](../ch12-falsifiable-predictions/binary-kill-switches.md) — GRB Trans-Planckian dispersion (matrix row C7-GRB-DISPERSION). Optical-wavelength static-Sagnac tests cannot reach the precision required to discriminate $10^{-22}$ from $0$; this protocol class is observationally exhausted by the existing null bounds.

### Relationship to A2-SAGNAC (Sagnac-RLVE rotor test)

The rotor-based Sagnac-RLVE protocol ([`sagnac-rlve.md`](sagnac-rlve.md)) is a **rotor-local mutual-inductance test**, not a preferred-frame test. A2's mechanism is independent of which frame the bulk $\mathcal{M}_A$ is at rest in — a spinning rotor injects a localized drift $v_{network} = v_{rotor} \cdot (\rho_{rotor}/\rho_{bulk}) = 0.38$ m/s into the surrounding $\mathcal{M}_A$ via mass-density-dependent coupling, producing the $\Psi_{W/Al} = 7.15$ material-contrast signal. The uniform 370 km/s bulk-frame motion of Earth through the lattice integrates to zero around the rotor loop and does not contribute. **A2 stands as a forward prediction; C17 retires to corroborative-null status.** Both leaves are now consistent with the cohesive narrative in the preferred-frame-and-emergent-lorentz leaf.

---
