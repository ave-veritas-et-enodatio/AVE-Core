[↑ Ch.11 Index](index.md)

<!-- kb-frontmatter
kind: leaf
no-claim: "by-methodology condensed duplicate of the canonical Sagnac-RLVE experiment leaf"
experiments: [exp-rth12t]
-->

> **Scope correction (2026-06-03 audit — RETIRED forward "kill-switch" → corroborative-null).** Condensed mirror of the canonical [`../ch11-experimental-bench-falsification/sagnac-rlve.md`](../ch11-experimental-bench-falsification/sagnac-rlve.md), which carries the full scope-correction header. A2-SAGNAC joins C17/C18 in walk-back: the same $\kappa = \rho_{rotor}/\rho_{bulk}$ applied to Earth-as-rotor predicts a $+7\times10^{-4}$ rotation-rate bias already excluded by ring-laser-gyro Earth-rotation geodesy by $7\times10^4\times$ (`AVE-PONDER/research/2026-06-03_sagnac-rlve-fog-question-verdict.md`). The $\Psi = 7.15$ "discriminator" below is **not** a forward AVE-vs-GR test (the verdict, citing PONDER PR #1 `eb7a49b`, finds GR Lense-Thirring scales with rotor $I \propto \rho$ too, so both predict $\Psi = \rho_W/\rho_{Al}$). The "GR prediction $\Psi = 1$" line in §"The $\Psi$ Discriminator" below is in tension with that finding and is flagged for Grant/auditor adjudication (NOT silently resolved here). The surviving leg is the paired W-vs-Al $\Psi$ **self-consistency** scaling check, not a kill-switch.

## Sagnac-RLVE: rotor-local mutual-inductance (corroborative null)

> → Primary: [Regimes of Operation](../../circuit-theory/ch2-topological-thrust-mechanics/regimes-of-operation.md) — $V_{yield}$ threshold and $\mathcal{M}_A$ bulk density definitions

The Sagnac Rotational Lattice Mutual Inductance Experiment bypasses the $G/c^2$ scalar gap by coupling *magnetically* and measuring *interferometrically*.

### Mechanism

A rapidly rotating high-density mass induces vacuum drift via **macroscopic mutual inductance**. Unlike scalar metric strain, mutual inductance operates at first-order ($v_{network}/c$).

### Derivation

**Inductive coupling** (Tungsten, $\rho_W = 19{,}300$ kg/m³):

$$\kappa_{entrain} = \frac{\rho_W}{\rho_{bulk}} = \frac{19{,}300}{7.916 \times 10^6} \approx 0.00244$$

**Vacuum drift** (15 cm radius, 10k RPM → $v_{tan} \approx 157$ m/s):

$$v_{network} = v_{tan} \times \kappa_{entrain} \approx 0.38 \text{ m/s}$$

> **[Resultbox]** *Sagnac Phase Shift*
>
> $$\Delta\phi = \frac{4\pi L_{fiber} \cdot v_{network}}{\lambda c} \approx \mathbf{2.07 \text{ Radians}}$$

### Hardware BOM (~$1,600)

| Component | Specification | Cost |
|---|---|---|
| Laser | 1550 nm telecom diode (Thorlabs S1FC1550) | $450 |
| Fiber coupler | 50/50 SMF-28 splitter | $120 |
| Sensing fiber | 200 m SMF-28 Ultra | $50 |
| Photodetector | InGaAs PIN diode (Thorlabs DET01CFC) | $180 |
| Rotors | 15 cm radius (1× Tungsten, 1× Aluminum) | $800 |

### The $\Psi$ Discriminator

Run the same experiment with Aluminum ($\rho_{Al} = 2{,}700$ kg/m³):

$$\Psi = \frac{\Delta\phi_W}{\Delta\phi_{Al}} = \frac{\rho_W}{\rho_{Al}} \approx 7.15$$

- **AVE prediction**: $\Psi \approx 7.15$ (density-dependent constitutive response)
- **GR prediction**: $\Psi = \rho_W/\rho_{Al} \approx 7.15$ — the **same** ratio as AVE (corrected 2026-06-03; Lense-Thirring frame-drag scales with the rotor's angular momentum $J = I\omega$, $I \propto \rho$, so it is **not** density-independent). The GR–AVE difference is the **magnitude**, not the ratio: GR is $G/c^2$-suppressed to $\sim 10^{-20}$ rad; AVE predicts $\sim$20 OOM more — and that magnitude leg is the one excluded by RLG geodesy (next bullet).
- **Self-consistency scaling check** (NOT a forward kill-switch — retired 2026-06-03): a measured $\Psi$ tests whether the AVE signal scales linearly with rotor density; the absolute-magnitude leg that would be a kill-switch is excluded by existing RLG Earth-rotation geodesy (Earth-as-rotor $+7\times10^{-4}$ bias)

---
