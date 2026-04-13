[↑ Ch.11: Phase-Locked Routing](./index.md)
<!-- leaf: verbatim -->

# Phase-Locked Routing: Eliminating Bus Reflections

Orthogonal trace routing on conventional PCBs introduces impedance discontinuities ($\Gamma > 0$) at every bend, generating thermal phonon losses proportional to the mismatch magnitude. By replacing discrete 90° copper turns with continuously curved waveguide bends whose local $Z(s)$ profile is matched via the Klopfenstein identity around every corner, all parasitic reflections are eliminated natively.

The VCA routing paradigm treats every interconnect as a reactive transmission line segment. The double-line waveguide notation enforces this identity: no trace is permitted to introduce an impedance step, and all width transitions use the Klopfenstein exponential taper to guarantee $\Gamma \to 0$.

> **[Resultbox]** *Chapter 11 Summary*
>
> Orthogonal trace routing on conventional PCBs introduces impedance discontinuities ($\Gamma > 0$) at every bend, generating thermal phonon losses proportional to the mismatch magnitude. By replacing discrete bends with continuously curved waveguide profiles, all parasitic reflections are eliminated, enabling lossless signal propagation across the entire monolithic APU plane.
