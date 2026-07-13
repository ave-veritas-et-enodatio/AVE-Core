[↑ Ch.12 Index](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-trgqtf]
-->

## EE Bench: Macroscopic Dielectric Plateau

> **A-034 anchor (canonical 2026-05-15 evening).** The EE bench dielectric-plateau prediction at $V_{yield} = 43.65$ kV is the **atomic-scale row (SYM symmetry class)** in the Universal Saturation-Kernel Catalog — the same $S(A) = \sqrt{1 - A^2}$ kernel governs BCS $B_c(T)$ at 0.00% error, solar flares (NOAA validation pending live fetch — LF-03), BH ring-down at 1.7% from GR, and cosmic K4 crystallization. <!-- 🔴 Rule-12 2026-06-15 LF-03: was "NOAA-validated solar flares". Superseded per KB leaf ../../../vol3/cosmology/ch14-orbital-mechanics/solar-flares-led-avalanche.md: synthesized illustrative timeline, not a live fetch; forward prediction, not a validated anchor. --> The bench measurement is the **most cost-accessible empirical anchor** ($\sim$\$25k BOM) for the 26-instance cross-scale catalog. KB synthesis: [`trampoline-framework.md §7.5`](../../../common/trampoline-framework.md).

> → Primary: [Regimes of Operation](../../circuit-theory/ch2-topological-thrust-mechanics/regimes-of-operation.md) — $V_{yield}$ and $E_{yield}$ derivations
> ↗ See also: [Nonlinear Vacuum Capacitance](../../circuit-theory/ch1-vacuum-circuit-analysis/nonlinear-vacuum-capacitance.md) — Axiom 4 saturation kernel $S(E)$

Standard QED: $\epsilon_0$ is a fixed linear constant.
AVE (Axiom 4): $\epsilon_{eff}(E) = \epsilon_0 \sqrt{1 - (E/E_{yield})^2}$, with $E_{yield} \approx 1.13 \times 10^{17}$ V/m.

As $E \to E_{yield}$: $\varepsilon_{eff} = \varepsilon_0 S \to 0$, and the **across-gap** capacitance an LCR meter reads **rolls off** with it — the large-signal (chord) $C_{diel}=C_0 S \to 0$, the small-signal (tangent) $C_{ss}=C_0(S-A^2/S)$ crosses zero at $E/E_{yield}=1/\sqrt2$ (NDC snap-back). The divergent $C_0/S\to\infty$ is the **orthogonal longitudinal-$A_1$ bond compliance keyed on $V_{snap}\approx511$ kV**, which an across-gap meter does NOT read.

> **★ Supersession (KEEP-BOTH; roll-off ruling ratified 2026-07-06/07, PR #562/#558).** The superseded line read: *"As $E \to E_{yield}$: $\varepsilon_{eff} \to 0$ and $C_{eff} = C_0/S \to \infty$."* — a **spike, sign-inverted** vs the ratified across-gap roll-off. The across-gap precision LCR couples to the **transverse-$T_2$ dielectric** ($C\propto S$, roll-off, keyed on $V_{yield}\approx43.65$ kV), not to the longitudinal-$A_1$ $C_0/S$ divergence (keyed on the higher $V_{snap}$). Canonical leaf: [`dielectric-plateau-prediction.md`](dielectric-plateau-prediction.md):25-38.

### Falsification Protocol

Ultra-stiff vacuum gap (below Paschen curve minimum, UHV) swept toward $\sim 10^{16}$ V/m using asymmetric sharp emission tips.

**Dual-sensor measurement:**

1. **LCR capacitance tracking**: Standard physics → flat $C(E)$. AVE → across-gap capacitance **roll-off** (transverse-$T_2$ dielectric $C_{diel}=C_0 S$, keyed on $V_{yield}$); the small-signal tangent $C_{ss}=C_0(S-A^2/S)$ crosses **zero at $E/E_{yield}=1/\sqrt2$** (NDC snap-back). The sign of the deviation (roll-off toward zero, NOT a $C_0/S$ spike) is the discriminating signature. *(Superseded, KEEP-BOTH: this line formerly read "AVE → asymptotic spike at $\sim 85\%$ of $E_{yield}$" — a sign-inverted spike; corrected to the roll-off per the 2026-07-06/07 ruling, [`dielectric-plateau-prediction.md`](dielectric-plateau-prediction.md):25-38.)*
2. **Interferometry**: Stabilized laser transverse through gap. As $E \to E_{yield}$, the transverse index $n_{eff}=\sqrt S$ *decreases* — anomalous drop in refractive index ($\delta n\approx-\tfrac14(E/E_{yield})^2$; a static field loads $\varepsilon$ only, $\mu$ unchanged). *(Superseded, KEEP-BOTH: this line formerly read "$n_{eff} \propto S$" — a $\propto S$ both-scale form with a $-\tfrac12 A^2$ leading shift; reconciled to $n_\perp=\sqrt S$, $\delta n\approx-\tfrac14 A^2$ per the 2026-07-06/07 ruling, [`dielectric-plateau-prediction.md`](dielectric-plateau-prediction.md):32,:39. Same factor-2 correction as clm-pp3qwf.)*

Detection of geometric asymptote prior to atomic plasma ionization confirms the hardware limits of the spatial lattice.

### PONDER-01: Maxwell Stress Rectification

Thrust from divergence of Maxwell Stress Tensor across asymmetric boundary:

$$F_i = \oint_{\partial V} \sigma_{ij} n_j \, da - \int_V \frac{\partial \mathbf{g}}{\partial t} \, d^3x$$

- Optimal geometry: 1000:1 asymmetry ratio (1 µm emitter vs 1 mm collector)
- 30 kV RMS, swept 1 MHz → 100 MHz (VHF)
- Thrust scales as $V^2 f^2$
- Detection: vacuum torsion balance, $> 1\;\mu$N target

---
