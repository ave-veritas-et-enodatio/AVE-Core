[↑ Ch.7 Regime Map](index.md)
<!-- leaf: verbatim -->
<!-- claim-quality: 2dwzib, b2anl4 -->

## Section 7.1: The Four Universal Regimes

Every physical domain in the AVE framework reduces to a single dimensionless control parameter $r = A/A_c$, where $A$ is the local strain amplitude and $A_c$ is the domain-specific critical threshold derived from the four axioms. The saturation operator $S(r) = \sqrt{1 - r^2}$ (Axiom 4) changes character at well-defined boundaries, partitioning all of physics into four universal regimes.

This chapter establishes the regime classification as a **prerequisite gate**: no domain analysis proceeds without first identifying its regime and verifying the appropriate equation set.

<!-- claim-quality: b2anl4 -->

> **[Resultbox]** *Universal Regime Classification*
>
> $$
> S(r) = \sqrt{1 - r^2}, \qquad r \equiv \frac{A}{A_c}
> $$

| **Regime** | **Name** | **$r$ range** | **$S$ range** | **Physics** | **EE Analog** |
|---|---|---|---|---|---|
| I | Linear | $r < \sqrt{2\alpha}$ | $S > 0.993$ | Standard equations | Small-Signal |
| II | Nonlinear | $\sqrt{2\alpha} \leq r < \frac{\sqrt{3}}{2}$ | $0.500 < S < 0.993$ | Axiom 4 active | Large-Signal |
| III | Yield | $\frac{\sqrt{3}}{2} \leq r < 1$ | $0 < S < 0.500$ | Phase transition | Avalanche ($M \geq 2$) |
| IV | Ruptured | $r \geq 1.0$ | $S = 0$ | Topology destroyed | Breakdown ($M \to \infty$) |

The boundary values are **derived from first principles**, not chosen by convention:

- **$r_1 = \sqrt{2\alpha} \approx 0.1208$ (Small-Signal Limit):** The perturbative expansion (Eq. below) gives a first-order correction $\Delta S = r^2/2$. The lattice's own self-coupling is $\alpha$ (the fine-structure constant = packing fraction / $8\pi$). When $\Delta S = \alpha$:

$$
\frac{r^2}{2} = \alpha \qquad \Longrightarrow \qquad r_1 = \sqrt{2\alpha} \approx 0.1208
$$

Below $r_1$, Axiom 4 corrections are *sub-$\alpha$*: smaller than the lattice's own coupling strength and therefore physically unresolvable. This is the exact analog of small-signal linearization in semiconductor analysis, where perturbations smaller than $V_T = kT/q$ are absorbed by thermal noise.

- **$r_2 = \sqrt{3}/2 \approx 0.8660$ (Avalanche Onset, spin-2 sector):** The quality factor $Q(r) = 1/S(r)$ measures energy trapping efficiency. A mode with $Q \geq \ell$ stores more energy per cycle than it radiates. For the **spin-2 (gravitational-wave / shear) sector**, the minimum non-trivial multipole is $\ell_{\min} = 2$ (dipole cannot radiate gravitational waves; monopole cannot radiate at all). The yield regime begins when $Q$ first reaches this minimum:

$$
Q(r) = \frac{1}{S(r)} = \ell_{\min} = 2 \qquad \Longrightarrow \qquad S = \frac{1}{2}, \quad r_2^{(\ell=2)} = \sqrt{1 - \frac{1}{4}} = \frac{\sqrt{3}}{2}
$$

**Sector-dependence note.** The $\ell_{\min} = 2$ argument is specific to the spin-2 sector. Other sectors have different minimum multipoles and therefore different $r_2$ boundaries:
- *Scalar sector* ($\ell_{\min} = 0$): the "$Q \geq \ell$" criterion is trivially satisfied for all $r$; no avalanche-onset boundary in this sector. Practical avalanche onset is set by other physics (e.g., Schwinger pair production at $V_{yield}$).
- *Photon / vector sector* ($\ell_{\min} = 1$): $Q = 1 \Rightarrow S = 1$, so $r_2^{(\ell=1)} = 0$ — i.e., avalanche onset is concurrent with linear-Maxwell breakdown. The vector sector has no separate "regime III" between linear and yield; the practical photon-sector boundary is again set by $V_{yield}$ (Axiom 2).
- *Spin-2 sector* ($\ell_{\min} = 2$): $r_2^{(\ell=2)} = \sqrt{3}/2$, as derived above. This is the GW / shear-mode result.

The "universal regime map" framing in the chapter title is the spin-2 form; the lower-spin sectors collapse two boundaries together. When this chapter cites $r_2 = \sqrt{3}/2$ without qualification, the spin-2 sector is implicit.

In semiconductor terms (an effectively spin-2 / shear-mode analog), the spin-2 boundary is the onset of **avalanche multiplication**: the Miller factor $M = 1/(1-(V_R/V_{BR})^n)$ reaches $M = 2$, meaning each cycle doubles the stored charge.

- **$r_3 = 1.0$ (Breakdown):** Axiomatic from Axiom 4. The saturation factor reaches zero, compliance vanishes, and the topology is destroyed. In different domains this manifests as: pair production (EM), event horizon formation (gravity), quark deconfinement (nuclear), or superconducting transition (BCS). In semiconductor terms: $V_R = V_{BR}$, $M \to \infty$, the device is destroyed.

  > **Note (cross-link with Ch.3).** <!-- claim-quality: 2dwzib --> This $r_3 = 1.0$ boundary is the same $V_{yield} = \sqrt{\alpha}\,V_{snap} \approx 43.65$ kV described in [Ch.3 §3.3 Zero-Impedance Boundary](../../dynamics/ch3-quantum-signal-dynamics/zero-impedance-boundary.md) as ``matter assembly begins.'' The two descriptions are the same phase transition viewed from opposite sides: from sub-threshold trapping a wave reflects inward at $\Gamma = -1$ and forms a stable standing wave (matter); a super-threshold mode driven through the same boundary ruptures the existing topology. Same Axiom 4 saturation, two operational faces.

### Semiconductor Device Analogy

The four regimes map exactly to the standard operating regions of a semiconductor p-n junction:

| **Regime** | **Semiconductor** | **AVE Universal** |
|---|---|---|
| **I: Small-Signal** | DC bias, linearised $g_m$, $r_\pi$, $C_\pi$ | $S \approx 1$, standard Maxwell/Newton |
| **II: Large-Signal** | Switching transient, saturation onset | $S(r) = \sqrt{1-r^2}$ required in full |
| **III: Avalanche** | Miller $M \geq 2$, carrier multiplication | $Q \geq 2$, energy trapping dominates |
| **IV: Breakdown** | $V_R = V_{BR}$, $M \to \infty$, junction failure | $S = 0$, topology destroyed |

This is not an analogy---it is the **same operator** ($S = \sqrt{1 - (V/V_{BR})^2}$ in the semiconductor case) applied at different scales. The nuclear periodic table already classifies each element by its $V_R/V_{BR}$ ratio and Miller exponent $n$ (the proton's cinquefoil crossing number $c = 5$).

### Perturbative Expansion (Regime I)

In Regime I, the saturation factor admits a convergent Taylor expansion:

<!-- eq:S_taylor -->

$$
S(r) = 1 - \frac{r^2}{2} - \frac{r^4}{8} - \frac{r^6}{16} - \cdots
$$

To leading order, $\Delta S \approx r^2/2$. At the derived boundary $r_1 = \sqrt{2\alpha}$, $\Delta S = \alpha \approx 1/137$. This validates the use of unmodified Maxwell/Newton equations in all terrestrial laboratory experiments except those explicitly designed to approach $V_{yield}$ (e.g., asymmetrical high-voltage capacitors).

---
