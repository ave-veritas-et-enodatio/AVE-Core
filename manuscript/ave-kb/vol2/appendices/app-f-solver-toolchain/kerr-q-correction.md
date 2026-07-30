[↑ App F: Universal Solver Toolchain](./index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-d9ivj1]
-->

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

~~For the LIGO observing band ($a_* = 0.3$--$0.8$), this formula reproduces the quality factor to **sub-2%** with zero free parameters:~~

> **🔴 RETRACTED 2026-07-21 (Grant Ruling B1; original struck, preserved per Rule 12).** The "sub-2%"
> Kerr-$Q$ match was computed against the **corrupt $\omega_R$/$\omega_I$ Kerr reference tables +
> source-frame masses** (#774) — the same MATCH-ARTIFACT that produced the retracted $-0.45\%$/$-0.47\%$
> LIGO ringdown figures. **Corrected picture:** the topological **flat $Q = \ell = 2$ is scoped to the
> $a_* = 0$ cold anchor** (the $\Omega \to 0$ limit of the m$\Omega$ law); at catalog spins the flat-$Q$
> reading **fails at $\bar D_Q = -38\%$** (corrected-Kerr $Q$ rises $3.07 \to 3.49$). The **spin-refined
> m$\Omega$ law** $\omega_I = (\omega_R - m\Omega)/(2\ell)$ under the standing v1 mapping lands at
> **$-5.44\%$** (Resultbox form) / **$-4.57\%$** (exact-equatorial-ZAMO variant) — an **OPEN near-miss
> tension**, the named next ringdown work; **NOT** a sub-2% match and **NOT** a zero-free-parameter
> benchmark (the only zero-parameter content is the cold $18/49$ eigenvalue). The *structure* above
> (the m$\Omega$ law, superradiance at $\omega_R = m\Omega$) is untouched by this retraction — only the
> accuracy claim is retracted.
>
> Honest grade / truth-source: [`vol3/claim-quality.md`](../../../vol3/claim-quality.md) `clm-395gps`
> (the model banner, at `:204`) and
> [`ave-merger-ringdown-eigenvalue.md` § GRANT RULING B1](../../../vol3/cosmology/ch15-black-hole-orbitals/ave-merger-ringdown-eigenvalue.md)
> (solidity 0.55, `use as input only`, disclosed-phenomenological, *"NOT a zero-free-parameter
> benchmark"*). Receipts: `research/2026-07-20_kerr-table-correction_result.md`,
> `research/2026-07-20_v1-spin-mapping-adjudication_result.md`.

> **⚠ The $Q_{\mathrm{AVE}}$/$Q_{\mathrm{GR}}$ table below was computed against the CORRUPT Kerr
> reference** (#774) — preserved verbatim per Rule 12 as the record of the retracted claim, **not** as
> honest numbers. The $Q_{\mathrm{GR}}$ column is the corrupt table, so every figure derived from it —
> the per-row errors **and** the "$\sim$40% at $a_* = 0.99$" divergence statement below — inherits the
> same corruption. Corrected-Kerr comparisons live in
> `research/2026-07-20_v1-spin-mapping-adjudication_result.md`.

| $a_*$ | $Q_{\mathrm{AVE}}$ | $Q_{\mathrm{GR}}$ | Error |
|---|---|---|---|
| 0.30 | 2.24 | 2.25 | $-0.6\%$ |
| 0.50 | 2.54 | 2.54 | $+0.1\%$ |
| 0.67 | 3.02 | 3.01 | $+0.5\%$ |
| 0.80 | 3.75 | 3.81 | $-1.5\%$ |
| 0.90 | 4.93 | 5.23 | $-5.7\%$ |

The formula diverges at $a_* > 0.9$ (error grows to $\sim$40% at $a_* = 0.99$), indicating higher-order coupling is needed near the extremal Kerr limit. **[Corrupt-reference inheritance, 2026-07-21: this divergence figure is read off the corrupt-reference table above — see the ⚠ banner.]**

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
