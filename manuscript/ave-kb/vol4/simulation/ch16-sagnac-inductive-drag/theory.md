[↑ Ch.16: Sagnac Inductive Drag](../index.md)
<!-- leaf: verbatim -->

## The Rotating LC Frame

If a massive physical object (like the Earth, or the glass of a fiber-optic ring) rotates, its internal atomic charges are physically moving. This moving bulk charge creates a weak, macroscopic $\mathbf{B}$-field via induction. This induced field phase-drags the local inductive capacity ($\mu$) of the surrounding vacuum LC network.

Because $c = \frac{1}{\sqrt{\mu \varepsilon}}$, any fractional shift in the local inductance $\mu_{local}$ physically alters the localized propagation speed of the electromagnetic wave.

- **Co-Rotating Wave:** A photon traveling in the same direction as the macroscopic phase-drag experiences an inductively "thinner" vacuum path (reduced $\mu_{eff}$), propagating physically faster than $c_0$.
- **Counter-Rotating Wave:** A photon plowing against the induced "headwind" of the frame experiences an inductively "denser" vacuum path (increased $\mu_{eff}$), propagating physically slower than $c_0$.

## The SPICE Equivalent: A Differential LC Ring

This simulation uses a standard 1D discrete LC topology. A closed ring of 50 purely classical inductors and capacitors is constructed.

### Circuit Schematic (Sagnac Ring Segment)

```
 ... Node N-1          Node N          Node N+1 ...
---->---+--->-( >0: L_eff = L_0*(1-drag) )->---+---->
-<---+--<---( <0: L_eff = L_0*(1+drag) )---<---+----<
        |                              |
      +-+-+                          +-+-+
      | C |                          | C |
      | 0 |                          | 0 |
      +-+-+                          +-+-+
        |                              |
       GND                            GND
```

A segment of the complete 50-node Sagnac topology. The inductors dynamically shift their value based on the direction of the passing photon pulse, simulating the differential "headwind" of an inductively rotated frame.

The core SPICE mechanism relies on arbitrary behavioral inductors or behavioral current sources to implement the directional logic.

To model the rotation of the massive frame, no relativistic tensor math is applied to the simulation clocks or spatial coordinates. Instead, the SPICE solver is instructed to dynamically evaluate the direction of the current $I$. If the current was flowing clockwise (co-rotating), the solver encountered an inductor valued at $L_0(1 - \delta)$. If the current flowed counter-clockwise, the solver encountered an inductor valued at $L_0(1 + \delta)$.

[Figure: sagnac_inductive_drag.png — see manuscript/vol_4_engineering/chapters/]

The two waves arrive at the detector at different times.

The analog solver natively reproduces the Lense-Thirring phase shift. It proves that one does not need the Lorentz Transformations or Einstein's field equations to derive the Sagnac effect; one only needs the macroscopic equivalent of Faraday's Law of Induction operating across the pure spacetime metric.

---
