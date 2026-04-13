[↑ Ch.2 General Relativity](index.md)
<!-- leaf: verbatim -->

---

**Topological Frame-Dragging (Lense-Thirring):** The rotation of the mass singularity creates an asymmetric strain footprint in the surrounding dielectric matrix. Unlike standard aerospace models, this is not a circulating fluid current. The angular momentum convolutes the static $Z_{local}$ impedance gradient into a non-reciprocal topological bias. In a Kerr spacetime with angular momentum parameter $a = a_\star M$, the saturation metric acquires an angular dependence:

> **[Resultbox]** *Frame-Dragging Impedance Convolution*
>
> $$
> \omega(r) = \frac{2Mar}{(r^2 + a^2)^2}
> $$

which is strongest at the horizon and decays as $\sim r^{-3}$ at large radii, generating differential phase-delays for co-rotating versus counter-rotating light.

By applying **Hamiltonian Symplectic Euler Integration** to track the momentum $\vec{p}$ of photon rays backwards through this refractive impedance gradient, the Python CFD engine derives the "bent accretion disk" architecture described by Kip Thorne.

The simulation renders a Shakura--Sunyaev thin accretion disk ($T_{\text{in}} = 10\,000$ K at the inner edge, $r_{\text{in}} = 1.0\,r_{\text{iso}}$) around a near-extremal Kerr-analogue defect ($a_\star = 0.999$). Three distinct observational signatures emerge naturally from the topological model:

- **The D-shaped shadow**: The spinning mass acts as a macroscopic topological impeller generating an asymmetric impedance gradient. Rays traversing the retrograde side encounter a stricter Op14 saturation profile, increasing their refractive capture radius. Conversely, rays on the prograde side propagate through a mechanically relaxed tensor, allowing them to graze closer to the horizon before capture. This differential refractive trap flattens the shadow boundary on the prograde side, producing the characteristic "D-shape" predicted by the Kerr metric without continuous manifolds.
- **Relativistic Doppler beaming**: The approaching side of the orbiting accretion disk is blue-shifted and brightened ($I_{\text{obs}} = I_{\text{emit}} \times \delta^3$ for optically thick emission).
- **Gravitational redshift**: The isotropic-coordinate redshift factor $z = W/U = (1 + r_h/r)/(1 - r_h/r)$ suppresses emission from the innermost disk annuli, producing the dark gap between the photon ring and the bright disk body.

---
