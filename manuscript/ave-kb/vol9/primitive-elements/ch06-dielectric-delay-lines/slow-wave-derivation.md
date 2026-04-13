[↑ Ch.6: Dielectric Delay Lines](./index.md)
<!-- leaf: verbatim -->

# Slow-Wave Derivation from Axiom 1

The Telegraphist equations for a distributed LC transmission line follow directly from Axiom 1:

$$\frac{\partial V}{\partial x} = -L' \frac{\partial I}{\partial t}, \qquad \frac{\partial I}{\partial x} = -C' \frac{\partial V}{\partial t}$$

Combining yields the 1D wave equation:

$$\frac{\partial^2 V}{\partial x^2} = L' C' \frac{\partial^2 V}{\partial t^2}$$

The phase velocity is:

$$v_{ph} = \frac{\omega}{k} = \frac{1}{\sqrt{L' C'}}$$

By periodically corrugating the waveguide walls with pitch $\Lambda$ and depth $d$, the effective per-unit-length inductance $L'_{eff}$ and capacitance $C'_{eff}$ increase (larger surface area → more stored magnetic and electric energy per unit length). The phase velocity reduces accordingly without introducing loss:

$$v_{ph,corr} = \frac{1}{\sqrt{L'_{eff} C'_{eff}}} < \frac{1}{\sqrt{L' C'}} = v_{ph,smooth}$$

The characteristic impedance $Z = \sqrt{L'/C'}$ can be independently controlled by adjusting the ratio of corrugation depth to waveguide width, allowing delay tuning without impedance mismatch.

> **[Resultbox]** *Chapter 6 Summary*
>
> Dielectric Corrugation Slow-Wave Structures derive from Axiom 1 alone. The Telegraphist equations establish that phase velocity $v_{ph} = 1/\sqrt{L'C'}$. Periodic corrugations of pitch $\Lambda$ and depth $d$ increase the effective per-unit-length inductance and capacitance, slowing the wave without introducing dispersion within the operating band.
