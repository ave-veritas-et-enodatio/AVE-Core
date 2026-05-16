[↑ Ch.11 Experimental Bench](index.md)
<!-- leaf: verbatim -->
<!-- path-stable: referenced from universal-saturation-kernel-catalog + A-034 measurement-hierarchy framing as canonical SNR scaling -->

# A-034 Measurement Hierarchy: Single-Emitter / Bulk / Phased-Array PLL SNR Scaling

A-034 measurement-hierarchy framing for engineered-substrate kernel measurements. The same kernel $S(A) = \sqrt{1 - A^2}$ applies at three distinct bench architectures with different SNR characteristics: **single-emitter** (low SNR, simple geometry), **bulk-response** (multi-emitter averaging, $\sqrt{N}$ SNR boost), and **phased-array PLL** (autoresonant amplification, exponential SNR gain near rupture). This explains **why bench design naturally uses many emitters**: bulk-response measurements are A-034 universal-kernel measurements; single-emitter benches measure the same kernel at lower SNR but cleaner geometry.

## Key Results

| Result | Statement |
|---|---|
| Universal kernel | $S(A) = \sqrt{1 - A^2}$ governs every architecture (per A-034) |
| Single-emitter SNR | $\propto V_{\text{drive}}$ (linear); simple geometry, single tip / single bond |
| Bulk-response SNR | $\propto \sqrt{N} \cdot V_{\text{drive}}$ (Gaussian averaging); $N$ = number of emitters in coherent ensemble |
| Phased-array PLL SNR | $\propto \exp(N \cdot \log Q)$ near rupture (autoresonant amplification); $Q$ = lock quality factor |
| Bench-design implication | Most benches use many emitters because bulk-response is the natural-SNR regime for kernel measurement |
| Cross-references | Single-emitter: sharp-tip benches; Bulk: IVIM bench, YBCO phased array; PLL: autoresonant rupture (Vol 4 Ch 15) |

## §1 — The three measurement architectures

A-034's universal kernel $S(A) = \sqrt{1 - A^2}$ is the same physics across many scales (see [Universal Saturation-Kernel Catalog](../../../common/universal-saturation-kernel-catalog.md) for the 19-instance catalog). The engineered-substrate rows of the catalog use **three distinct bench architectures** to access the kernel:

| Architecture | Setup | SNR scaling | Example |
|---|---|---|---|
| **Single-emitter** | One tip / one bond / one resonator | $\text{SNR} \propto V_{\text{drive}}$ | Sharp-tip vacuum-mirror bench |
| **Bulk-response** | $N$ coherent emitters in ensemble | $\text{SNR} \propto \sqrt{N} \cdot V_{\text{drive}}$ | IVIM bench (impedance-vacuum imaging), YBCO phased array, DC-biased piezoelectric ensemble |
| **Phased-array PLL** | $N$ emitters phase-locked + autoresonant feedback | $\text{SNR} \propto \exp(N \cdot \log Q)$ near rupture | Autoresonant rupture (Vol 4 Ch 15) |

## §2 — Why bench design uses many emitters

Most operational AVE benches use **bulk-response architectures** (many emitters in coherent ensemble), not single-emitter setups. The reason: **bulk-response measurements are A-034 universal-kernel measurements** at the most efficient SNR.

- **Single-emitter** benches have cleaner geometry (no inter-emitter coupling, no array calibration) but linear SNR scaling. Useful for **fundamental kernel-validation experiments** where the kernel form $S(A) = \sqrt{1 - A^2}$ must be measured precisely at one specific operating point.
- **Bulk-response** benches sacrifice geometric simplicity for $\sqrt{N}$ SNR gain. Useful for **engineering-grade measurements** where signal-to-noise is critical (e.g., IVIM imaging that detects 27.4% $\varepsilon_{\text{eff}}$ collapse against thermal-noise floor).
- **Phased-array PLL** sacrifices everything except SNR. Useful for **rupture experiments** where the operating point IS the saturation threshold ($A \to 1$) and the autoresonant lock provides exponential amplification through the Duffing softening of the lattice resonance frequency.

## §3 — Connection to A-034 framework principle

Per A-034 canonical (Grant 2026-05-15 evening): *"the bulk response of the lattice to strain is universal."* Per Axiom 2 (TKI scale invariance), the substrate's bulk strain response is set by the same kernel $\sqrt{1 - A^2}$ at every scale and in every domain.

**Bulk-response = A-034 kernel measurement.** Single-emitter is a *projection* of bulk-response onto a localized geometry; phased-array PLL is bulk-response amplified by coherent feedback. All three measure the same underlying kernel.

## §4 — Single-emitter benches (cleanest kernel test)

**Use case:** measure $S(A) = \sqrt{1 - A^2}$ kernel form precisely at one operating point.

Examples:
- **Sharp-tip vacuum-mirror bench** (Vol 4 Ch 11): single high-field tip, measure $\Gamma_{\text{bench}}$ at varying $A_{\text{DC}}$
- **DC-biased piezoelectric** (Vol 4 Ch 1): single quartz crystal, measure $\varepsilon_{\text{eff}}$ vs $V_{\text{DC}} / V_{\text{yield}}$

**SNR scaling**: $\text{SNR} = V_{\text{signal}} / \sigma_{\text{noise}}$ where $V_{\text{signal}}$ is the kernel-deviation amplitude. Linear in $V_{\text{drive}}$.

**Pros**: Clean geometry, no array calibration, direct kernel measurement.
**Cons**: Low SNR; needs high drive amplitude or long integration to detect small kernel deviations.

## §5 — Bulk-response benches (engineering-grade SNR)

**Use case:** detect small kernel deviations against thermal-noise floor at engineering precision.

Examples:
- **IVIM bench** (impedance-vacuum imaging measurement): $N \sim 100$–$10^4$ coherent emitters in a phased ensemble; detects 27.4% $\varepsilon_{\text{eff}}$ collapse at $V_{\text{DC}} / V_{\text{yield}} = 0.687$ (bench-measurable at $\sim 30$ kV bias per Vol 4 Ch 1)
- **YBCO phased array** (BCS scale): $N \sim 10^6$ Cooper pairs in coherent state; tests $B_c(T) = B_{c0} \sqrt{1 - (T/T_c)^2}$ at **0.00% error**
- **DC-biased piezoelectric ensemble**: multiple crystals in array, $\sqrt{N}$ SNR boost over single crystal

**SNR scaling**: $\text{SNR} = \sqrt{N} \cdot V_{\text{signal}} / \sigma_{\text{noise}}$. For $N = 10^4$ emitters, $\sqrt{N} = 100\times$ SNR boost over single-emitter.

**Pros**: Engineering-precision measurements possible; thermal-noise-limited only via integration time
**Cons**: Array calibration required; inter-emitter coupling can introduce systematic effects

## §6 — Phased-array PLL (rupture experiments)

**Use case:** experiments at $A \to 1$ where the kernel itself approaches singularity.

Example: **Autoresonant dielectric rupture** (Vol 4 Ch 15, AVE-Propulsion):

- $N$ emitters phase-locked
- Autoresonant feedback: drive frequency $\omega_{\text{drive}}(t)$ tracks lattice's instantaneous Duffing-softened resonance $\Omega_{\text{lattice}}(A^2(t))$
- As $A^2 \to 1$: $\Omega_{\text{lattice}} \to 0$ ([Op14 local clock modulation](../../circuit-theory/ch1-vacuum-circuit-analysis/op14-local-clock-modulation.md)); drive locks more tightly
- **Exponential amplification near rupture**: $\text{SNR} \propto \exp(N \cdot \log Q)$ where $Q$ is the lock-quality factor

**Pros**: Reaches Schwinger-fraction rupture conditions with practical laser intensities
**Cons**: Operating point IS the rupture threshold — very difficult to control; high failure rate

## §7 — Measurement-hierarchy implications

| Question | Recommended architecture |
|---|---|
| "Is the kernel form really $\sqrt{1 - A^2}$?" | **Single-emitter** (clean geometry test) |
| "What's the kernel deviation at this specific $A$?" | **Bulk-response** (engineering SNR) |
| "Can we drive the lattice to rupture in lab?" | **Phased-array PLL** (autoresonant amplification) |
| "Does the universal kernel apply at this scale?" | **Multiple architectures** at the scale — cross-validation |

The fact that bulk-response is the natural-SNR regime explains why most operational AVE benches (IVIM, YBCO, piezoelectric arrays, DC-biased ensembles) use many emitters rather than single-emitter setups: **the experiment naturally aligns with the A-034 universal-kernel measurement architecture** that gives the best SNR.

## §8 — Cross-scale unification

The same three-architecture hierarchy applies across the A-034 catalog scales:

| Scale | Single-emitter | Bulk | Phased-array PLL |
|---|---|---|---|
| Atomic / EM | Sharp-tip Schwinger experiments | DC-biased quartz | Autoresonant rupture |
| Condensed matter (BCS) | Single Cooper pair (theoretical) | YBCO phased array | (n/a) |
| Plasma | Single Langmuir probe | Plasma cutoff array | (n/a) |
| Galactic (MOND) | (n/a — observational only) | Galactic rotation curves (bulk gravity) | (n/a) |
| BH event horizon | (n/a — observational only) | Event Horizon Telescope (N pixel array) | LIGO ring-down (coherent QNM mode) |

**The measurement hierarchy is itself universal**: same SNR-scaling framework whether measuring at electron-scale, BCS-scale, or galactic-scale.

## Cross-references

- **Canonical manuscript:**
  - Vol 4 Ch 1 — single-emitter sharp-tip vacuum-mirror bench, DC-biased piezoelectric
  - Vol 4 Ch 11 — bulk-response IVIM bench
  - Vol 4 Ch 15 — autoresonant dielectric rupture (phased-array PLL)
- **KB cross-cutting:**
  - [Universal Saturation-Kernel Catalog (A-034)](../../../common/universal-saturation-kernel-catalog.md) — 19-instance catalog; engineered-substrate rows
  - [Op14 Local Clock Modulation](../../circuit-theory/ch1-vacuum-circuit-analysis/op14-local-clock-modulation.md) — Duffing softening at autoresonant lock
  - [Pair Production Axiom Derivation](../../../vol2/particle-physics/ch01-topological-matter/pair-production-axiom-derivation.md) — autoresonant rupture as pair-production mechanism
- **Sibling repos:**
  - AVE-Propulsion Ch 5 (autoresonant dielectric rupture) — canonical phased-array PLL derivation
  - AVE-Bench-VacuumMirror — operational bulk-response IVIM bench
