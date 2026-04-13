[↑ Ch.3 HOPF-01 Chiral Verification](index.md)
<!-- leaf: verbatim -->

## Impedance Characterization

The characteristic impedance of a round wire at height $h$ above a ground plane is given by the image-charge model:

$$
Z_0 = \frac{60}{\sqrt{\varepsilon_{eff}}} \operatorname{acosh}\!\left(\frac{2h}{d}\right)
$$

where $d = 0.51$ mm is the wire diameter. Near the SMA feed point ($h \approx 1.86$ mm above the B.Cu ground patch), $Z_0 \approx 141\;\Omega$ in air and $107\;\Omega$ in mineral oil. The SMA-to-wire impedance mismatch produces a reflection coefficient $\Gamma = (Z_0 - 50)/(Z_0 + 50) \approx 0.48$ (return loss $\approx 6.4$ dB). This raises the S$_{11}$ baseline but does **not** shift the resonant frequency.

Away from the SMA patches, the wire has no continuous ground plane and behaves as a free-space resonator. The quality factor is limited by AC resistance at the operating frequency:

$$
Q = \frac{\pi Z_0}{R_{ac} \cdot L_{wire}}, \quad R_{ac} = \frac{1}{\sigma_{Cu} \cdot A_{skin}}
$$

where $A_{skin}$ is the skin-depth--limited cross-sectional area. At $\sim$1 GHz, the skin depth in copper is $\sim$2 $\mu$m, yielding $Q \approx 470$--$680$ depending on wire length.

### Wire-Stitched Torus Knot Fixture

The PCB serves as a mechanical fixture, not the antenna itself. Enameled magnet wire (24 AWG, 0.51 mm diameter) is threaded through unplated drill holes spaced 3 mm apart along each knot path, creating true 3D torus knots with real over/under crossings.

The standard 2-layer FR-4 board uses a ground-patch architecture: F.Cu copper ground patches (12$\times$12 mm) sit under each SMA connector and connect to a continuous F.Cu perimeter ground trace (0.5 mm wide, at 5 mm inset from the board edge). No ground vias are required---the SMA thru-hole pads inherently bridge both copper layers. B.Cu is bare, allowing the wire to route freely on both sides of the board. The board is elevated on 10 mm nylon standoffs, providing clearance for under-crossings.

Because the wire has no continuous ground plane underneath, it resonates as a **free-space wire resonator** rather than a microstrip line. The effective permittivity is dominated by air with a small correction from the polyurethane enamel coating ($\varepsilon_{enamel} \approx 3.5$, 30 $\mu$m thick), yielding $\varepsilon_{eff} \approx 1.295$.

All five knot topologies plus one zero-topology control antenna share a **single 160$\times$120 mm FR-4 panel** in a 3$\times$2 grid layout.

---
