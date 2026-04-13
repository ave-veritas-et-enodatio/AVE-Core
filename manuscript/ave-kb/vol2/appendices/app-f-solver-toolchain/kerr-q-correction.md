[↑ App F: Universal Solver Toolchain](./index.md)
<!-- leaf: verbatim -->
<!-- PATH-STABLE: sec:kerr_q_correction, eq:kerr_q, eq:r_omega -->

## Kerr Q Correction: Co-Rotating Frame Decomposition

For a *spinning* black hole ($a_* > 0$), the lattice vortex co-rotates with the mode, reducing the effective differential velocity and hence the radiation rate. The decay rate becomes:

> **[Resultbox]** *Kerr QNM Decay Rate*
>
> $$
> \boxed{\omega_I = \frac{\omega_R - m\,\Omega}{2\,\ell}}
> $$

where $m = \ell$ for the dominant co-rotating mode and $\Omega$ is the lattice frame-dragging angular velocity evaluated at the **Poisson-augmented photon sphere**:

$$
r_\Omega = r_{ph}(a_*) \cdot \sqrt{1 + \nu_{\mathrm{vac}}} = r_{ph} \cdot \sqrt{\tfrac{9}{7}}
$$

The same $\nu_{\mathrm{vac}} = 2/7$ that corrects the eigenfrequency ($r_{\mathrm{eff}} = r_{\mathrm{sat}}/(1+\nu)$) also corrects the spin evaluation radius ($r_\Omega = r_{ph} \cdot \sqrt{1+\nu}$). The Kerr frame-dragging angular velocity at this radius is:

$$
\Omega = \frac{2\,a_*}{r_\Omega^3 + a_*^2\,r_\Omega + 2\,a_*^2}
\qquad (\text{in units of } c/M_g)
$$

At the **superradiance** threshold ($\omega_R = m\,\Omega$): $\omega_I \to 0$, $Q \to \infty$. The mode gains energy from the BH spin --- no net radiation. This is the first-principles prediction of superradiance from pure lattice geometry.

### Accuracy

For the LIGO observing band ($a_* = 0.3$--$0.8$), this formula reproduces the quality factor to **sub-2%** with zero free parameters:

| $a_*$ | $Q_{\mathrm{AVE}}$ | $Q_{\mathrm{GR}}$ | Error |
|---|---|---|---|
| 0.30 | 2.24 | 2.25 | $-0.6\%$ |
| 0.50 | 2.54 | 2.54 | $+0.1\%$ |
| 0.67 | 3.02 | 3.01 | $+0.5\%$ |
| 0.80 | 3.75 | 3.81 | $-1.5\%$ |
| 0.90 | 4.93 | 5.23 | $-5.7\%$ |

The formula diverges at $a_* > 0.9$ (error grows to $\sim$40% at $a_* = 0.99$), indicating higher-order coupling is needed near the extremal Kerr limit.

### FOC / Park Transform Analogy

This co-rotating frame decomposition is *structurally identical* to **Field-Oriented Control (FOC)** of a brushless DC motor. The Park transform decomposes stator currents into a frame co-rotating with the rotor magnetic field:

| FOC Motor | BH QNM | Physical Role |
|---|---|---|
| Rotor angle $\theta_r$ | Lattice spin phase $\Omega_H t$ | Reference frame |
| d-axis (flux) | $m \cdot \Omega$ component | Reactive / non-radiating |
| q-axis (torque) | $(\omega_R - m \cdot \Omega)$ component | Real / radiating |
| Back-EMF | Curvature radiation $\omega_I$ | Energy loss per cycle |
| Stall current | Superradiance ($\omega_R = m\Omega$) | $Q \to \infty$ |

The q-axis (torque-producing) component drives radiation; the d-axis (flux-aligning) component co-rotates reactively. This isomorphism suggests the same universal operator governs QNM decay, motor torque, and any co-rotating coupled oscillator.

---
