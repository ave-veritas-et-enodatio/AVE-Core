[↑ Ch.11: Experimental Bench Falsification](../index.md)

<!-- kb-frontmatter
kind: leaf
exp-id: exp-rth12t
status: pending
strengthens:
  - clm-qx9bb8: 1.0
path-stable: "canonical Sagnac-RLVE experiment leaf; referenced from the by-methodology ch11-experimental-bench/sagnac-rlve.md duplicate + matrix A2-SAGNAC"
-->

> **Scope correction (2026-06-03 audit — RETIRE forward "kill-switch" → corroborative-null).** This protocol was originally framed as a forward AVE-vs-GR kill-switch (a measured $\Psi = 1$ "decisively and permanently falsifies" AVE; $\Psi \approx 7.15$ "falsifies GR"). Audit (`AVE-PONDER/research/2026-06-03_sagnac-rlve-fog-question-verdict.md`) found the **same** coupling $\kappa = \rho_{rotor}/\rho_{bulk}$ that yields the 2.07 rad flagship, applied to the rotating **Earth** that every ring-laser gyroscope already watches (Earth is also a rigid rotor: curl $= 2\Omega \neq 0$, rotor-local vorticity, distinct from C17's uniform-bulk), predicts a **$+7\times10^{-4}$ fractional bias on every rotation-rate measurement** ($\kappa_{earth} = \rho_{earth}/\rho_{bulk} = 6.97\times10^{-4}$) — excluded by G-ring / ROMY / GINGER ring-laser-gyro Earth-rotation geodesy (~1 part in $10^8$, agreeing with VLBI/IERS) by $7\times10^4\times$. The co-wound 2.07 rad is reproduced but **inseparable** from the falsified Earth-rotor bias. **A2-SAGNAC joins C17/C18 in walk-back: corroborative null (existing RLG/VLBI/IERS geodesy already constrains it), NOT a forward kill-switch** — same lifecycle bin as C17/C18, different suppression physics (rotor-local vorticity vs bulk preferred-frame). The one surviving fragment is the paired W-vs-Al $\Psi = 7.15$ **self-consistency** scaling check (PONDER PR #1 `eb7a49b` already demoted $\Psi = 7.15$ from "discriminator vs GR" to "AVE-coupling scaling confirmation," since GR frame-drag scales as $I \propto \rho$ too), which is **not** a forward discriminator and still inherits the absolute-magnitude tension with RLG geodesy. KB anchor: `AVE-PONDER/research/sagnac-rlve-experimental-leaf.md`. Full reconciliation at [`preferred-frame-and-emergent-lorentz.md`](../../../vol1/dynamics/ch4-continuum-electrodynamics/preferred-frame-and-emergent-lorentz.md) §4 (A2/C17 classification) + §6 (matrix implications).

## Sagnac-RLVE: rotor-local mutual-inductance (corroborative null)

Because it is physically impossible to measurably advect the hyper-dense vacuum LC network using pure electromagnetic momentum, and because scalar metric fluctuations are heavily suppressed by $G/c^2$, the coupling must occur *magnetically*, and the measurement must proceed *interferometrically*.

This section proposes the **Sagnac Rotational Lattice Mutual Inductance Experiment (Sagnac-RLVE)** as the definitive, sub-\$5,000 tabletop falsification test.

By rapidly rotating a high-density physical mass adjacent to a high-finesse Sagnac fiber-optic loop, a primary sweeping magnetic field is literally synthesized, inducing a secondary phase shift in the local substrate LC network via **Macroscopic Mutual Inductance**. Unlike scalar elastic metric strain, mutual inductance completely bypasses the $G/c^2$ suppression limit, creating a massive, directly measurable optical phase shift ($\Delta \phi$).

### Exact Derivation of the Macroscopic Shift

A macroscopic physical rotor is composed of fundamental nucleons (topological inductive loops). The degree to which these loops physically pack and magnetically couple to the vacuum impedance is strictly proportional to the object's physical mass density ratio ($\rho_{rotor} / \rho_{bulk}$).

For a solid Tungsten rotor ($\rho_W = 19{,}300\,\text{kg/m}^3$), the volumetric inductive coupling is precisely:

$$
\kappa_{entrain} = \frac{19{,}300}{7.916 \times 10^6} \approx \mathbf{0.00244}
$$

As the Tungsten mass rotates at a tangential velocity $v_{tan}$, the embedded topological loops act as a primary inductor sweeping the bulk continuous vacuum network. If a safe, standard machine-shop Tungsten rotor ($15\,\text{cm}$ radius) spins at $10{,}000$ RPM ($v_{tan} \approx 157\,\text{m/s}$), the macroscopic induced drift velocity (the secondary phase shift) of the local vacuum is exactly:

$$
v_{network} = 157\,\text{m/s} \times 0.00244 \approx \mathbf{0.38\,\text{m/s}}
$$

**The Fiber-Optic Amplification (The Optical Lever Arm):** When light passes through this magnetically biased network, its phase velocity is shifted. Unlike the RVR, this relies on a **First-Order Inductive Vector ($v_{network}/c$)**, entirely bypassing the $G/c^2$ scalar gap. The experiment utilizes a Sagnac topology, where a $1550\,\text{nm}$ telecom laser is split and sent in counter-propagating directions through a $L_{fiber} = 200\,\text{m}$ spool of standard SMF-28 single-mode optical fiber wound co-linearly around the perimeter of the rotor. This geometrically multiplies the optical interaction length:

$$
\Delta \phi = \frac{4\pi L_{fiber} v_{network}}{\lambda c} = \frac{4\pi (200) (0.38)}{(1550 \times 10^{-9}) (299792458)} \approx \mathbf{2.07\,\text{Radians}}
$$

A phase shift of over $2.0$ Radians is substantial. It is trivially detectable by standard commercial photodetectors on a standard optical bench.

[Figure: tabletop_falsification_thresholds.png — see manuscript/vol_4_engineering/chapters/]

### Hardware Specification and Protocol

To rigorously distinguish AVE from standard General Relativity (GR), the experiment employs a specific comparative protocol using standard optical hardware.

| Component | Specification | Est. Cost |
|---|---|---|
| Laser Source | 1550nm Telecom Diode (Thorlabs S1FC1550) | \$450 |
| Fiber Coupler | 50/50 SMF-28 Splitter (Thorlabs TN1550R5A2) | \$120 |
| Sensing Fiber Coil | 200m SMF-28 Ultra (Bare) | \$50 |
| Photodetector | InGaAs PIN Diode (Thorlabs DET01CFC) | \$180 |
| Mechanical Rotors | 15cm Radius (1x Tungsten, 1x Aluminum) | \$800 |

The Metric Mutual Inductance Ratio ($\Psi$) is defined as follows. GR also predicts a Lense-Thirring frame-drag, and — contrary to an earlier framing here — it is **not** density-independent: the drag scales with the rotor's angular momentum $J = I\omega$, and $I \propto \rho$ at fixed geometry, so at fixed RPM the GR effect scales with mass density exactly as the AVE signal does. Both frameworks therefore predict the **same** ratio $\Psi = \rho_W/\rho_{Al} \approx 7.15$; they differ only in **magnitude** — GR's frame-drag is $G/c^2$-suppressed to $\sim 10^{-20}$ rad (unmeasurable), while AVE predicts a constitutive electrical response $\sim$20 orders of magnitude larger. The discriminator was always the magnitude, never the ratio — and that magnitude is the leg the RLG-geodesy objection (below) defeats.

If the exact same experiment is run using an Aluminum rotor ($\rho_{Al} = 2{,}700\,\text{kg/m}^3$) of identical physical dimensions, AVE strictly predicts the optical signal will plummet exactly in proportion to the material magnetic density:

$$
\Psi = \frac{\Delta \phi_{Tungsten}}{\Delta \phi_{Aluminum}} = \frac{\rho_W}{\rho_{Al}} \approx \mathbf{7.15}
$$

**The Metric Null-Result Kill-Switch — RETIRED to corroborative-null (2026-06-03; see scope-correction header above).** The original framing read: "If the Sagnac-RLVE yields a null result ($\Delta\phi \approx 0$, or $\Psi = 1$), the macroscopic electrodynamics of AVE are decisively and permanently falsified; a measured $\Psi \approx 7.15$ falsifies the 'frictionless void' GR model." This **forward kill-switch claim is walked back**: the absolute-magnitude leg (2.07 rad, the leg that *would* be a kill-switch) is the leg the FOG/RLG objection defeats — the same $\kappa$ applied to Earth-as-rotor predicts a $+7\times10^{-4}$ rotation-rate bias already excluded by ring-laser geodesy. The $\Psi = 7.15$ ratio is **not** a forward AVE-vs-GR discriminator either, because GR Lense-Thirring frame-drag scales with rotor moment of inertia $I \propto \rho$ too — both frameworks predict $\Psi = \rho_W/\rho_{Al}$ (PONDER PR #1 `eb7a49b`). What survives is the paired W-vs-Al $\Psi = 7.15$ as a **self-consistency** scaling check (does the AVE signal scale linearly with rotor density), still tension-carrying against RLG geodesy, not a kill-switch.

[Figure: sagnac_rlve_prediction.png — see manuscript/vol_4_engineering/chapters/]

---
