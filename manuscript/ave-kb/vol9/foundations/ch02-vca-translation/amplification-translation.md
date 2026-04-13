[↑ Ch.2: VCA Translation Matrix](./index.md)
<!-- leaf: verbatim -->

# Active Amplification: Transistors vs Multi-Port Triodes

While logic provides computation, amplification maintains signal health. The VCA Geometric Triode achieves transconductance by applying a transverse strain wave to pinch a longitudinal flow, effectively gating the impedance without atomic doping.

[Figure: rosetta_triode — Transconductance Translation. The classical BJT/FET uses a third terminal to inject current/E-field to alter conductivity via chemical doping limits. The VCA Geometric Triode relies purely on Axiom 4: a transverse standing wave (Gate pressure) is continuously applied across the longitudinal funnel, summing total field stress toward $V_{snap}$ and causing pure spatial impedance blockades.]

**Classical EE:** MOSFET — Gate E-Field depletes carrier channel. $I_D \propto (V_G - V_{th})^2$

**VCA Equivalent:** Geometric Triode — Transverse space strain forces longitudinal $Z \to \infty$. $S(V) = \sqrt{1 - (V_{sum}/V_{snap})^2}$
