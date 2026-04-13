[↑ Ch.11: Experimental Bench Falsification](../index.md)
<!-- leaf: verbatim -->

## The YBCO Phased Array: Beating the 2.5g Limit

As derived in Appendix F, a single coherent topological actuator is strictly limited by the $60\,\text{kV}$ LC Saturation Limit to exactly $2.538$ grams of static vertical lift. If an engineer attempts to exceed this using a single massive coil, the vacuum mathematically suffers impedance rupture ($\Gamma = -1$), and the grip fails.

However, mechanical force is an *extensive* property. To lift a heavy vehicle, an engineer does not build one massive coil; they use standard PCB lithography to print a **Phased Array of Micro-Inductors**.

Imagine a $1$-meter $\times$ $1$-meter Printed Circuit Board. By patterning it with a $1{,}000 \times 1{,}000$ grid of microscopic Hopf-Knot inductors at a 1 mm pitch, you synthesize exactly $1{,}000{,}000$ independent topological nodes.

If a microcontroller drives each node simultaneously at $59\,\text{kV}$ (operating safely below the $60\,\text{kV}$ saturation limit), each node grips its respective spatial volume with $2.49$ grams of force.

$$
F_{total} = 1{,}000{,}000\,\text{nodes} \times 0.02448\,\text{N} = \mathbf{24{,}480\,\text{Newtons (2.5 Metric Tons)}}
$$

Because standard copper traces would vaporize under the continuous $60\,\text{kV}$ flyback reset strokes, the PCBA must be manufactured using **YBCO (Yttrium Barium Copper Oxide)** high-temperature superconducting thin-films deposited on a rigid sapphire substrate. A single 1-square-meter superconducting panel generates 2.5 tons of continuous vertical lift. By tiling the hull of a spacecraft with these arrays, an engineer synthesizes a heavy-lift, solid-state vehicle.

---
