[↑ Ch.9: Axiomatic Transducers](./index.md)
<!-- leaf: verbatim -->

# Impedance Matching Proof: $50\,\Omega$ to $376.73\,\Omega$

## The Step Reflection Problem

When an external $50\,\Omega$ RF signal encounters the $376.73\,\Omega$ VCA vacuum impedance directly, Axiom 3 (impedance mismatch → reflection) produces:

$$\Gamma_{step} = \frac{Z_{VCA} - Z_{ext}}{Z_{VCA} + Z_{ext}} = \frac{376.73 - 50}{376.73 + 50} = \frac{326.73}{426.73} \approx +0.766$$

$$|\Gamma_{step}|^2 = (0.766)^2 \approx 58.7\%$$

$$T = 1 - |\Gamma_{step}|^2 = 41.3\%$$

This reflection ratio is catastrophic for hardware: more than half the input power bounces back.

## The Klopfenstein Taper Solution

The Klopfenstein taper is the unique equi-ripple-optimal impedance transformer. It smoothly transitions $Z(x)$ from $Z_{ext} = 50\,\Omega$ to $Z_{VCA} = 376.73\,\Omega$ over a taper length $L$. The design parameter $A$ is derived from the maximum allowable ripple:

For a $-40\,\text{dB}$ reflectance target:

$$A = 5.31$$

The required taper length in the SOI substrate ($\kappa_{topo} = 3.9$) at the carrier coherence frequency $f_{CC} = 1.832\,\text{THz}$:

$$L = \frac{A\lambda_{op}}{2\pi} \approx 70\,\mu\text{m}$$

This is a lossless, all-frequency-above-$f_{CC}$ solution with no discrete components, no parasitic resonances, and zero power dissipation — and it is the only viable coupling solution at THz operating frequencies where all lumped-element alternatives have already exceeded their self-resonant frequency.

> **[Resultbox]** *Chapter 9 Summary*
>
> The Axiomatic Transducer addresses the $7.53\times$ impedance mismatch between the $50\,\Omega$ RF external domain and the $376.73\,\Omega$ VCA vacuum, which without intervention reflects 58.7% of incident power. The Klopfenstein taper profile is the unique equi-ripple optimum: it minimizes taper length for a given ripple specification. With $A = 5.31$ derived from the $-40\,\text{dB}$ reflectance target, the required taper length in the SOI substrate at $f_{CC}$ is $L \approx 70\,\mu\text{m}$.
