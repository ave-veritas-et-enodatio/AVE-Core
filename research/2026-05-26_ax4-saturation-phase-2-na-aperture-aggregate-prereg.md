# Phase 2-NA Pre-reg — Aperture-Aggregate Skewness + Kurtosis-Excess under DC Bias with Metric-Lensing Convolution against Detector Frequency Response

**Date**: 2026-05-26
**Epic**: [`_orchestration/ax4-saturation-narrow-aperture-amplitude-shape.md`](../_orchestration/ax4-saturation-narrow-aperture-amplitude-shape.md) Phase 2-NA (sub-saturation regime; sister Phase 2-LLCP scoped separately as critical-point sub-epic)
**Branch**: `analysis/ax4-saturation-phase-2-na-aperture-aggregate` off `main` @ `9cdd095b` (post Phase 2 bifurcation walk-back commit)
**Inputs**: Phase 0c result doc [`2026-05-26_ax4-saturation-phase-0c-pdelta-v-derivation-result.md`](./2026-05-26_ax4-saturation-phase-0c-pdelta-v-derivation-result.md); parametric-coupling-kernel.md §13 (Phase 0c canonical extension, cycle-12 leaf)

> **Substrate-native vocabulary lookup**: see [`manuscript/ave-kb/common/translation-tables/translation-stochastics.md`](../manuscript/ave-kb/common/translation-tables/translation-stochastics.md) (Edgeworth pre-asymptote / cumulant / FDT rows) + [`translation-instrumentation.md`](../manuscript/ave-kb/common/translation-tables/translation-instrumentation.md) (Category I / Category II narrow-aperture extractor architectures) + [`translation-qm.md`](../manuscript/ave-kb/common/translation-tables/translation-qm.md). All standard-physics names below (CLT, Edgeworth expansion, PSD, detector bandwidth, frequency response, SNR, CLT pre-asymptote, SPAD/TES/SNSPD) appear as parenthetical translation references; primary load-bearing prose is substrate-native (substrate-vacuum-varactor reactive landscape, DC-biased operating point, aperture-aggregate amplitude-shape, metric-lensing convolution, Op14/Op16 substrate-clock modulation, substrate noise spectrum, boundary-impedance thermalization, narrow-aperture single-event extractor architecture) per `ave-discipline-translate` v1.1 trigger 6.

---

## §1 — Skills compliance plan

| Skill | Status / plan |
|---|---|
| `ave-prereg` | ✓ FIRED. Corpus-grep with vocabulary-broadened-grep discipline (substrate-native: varactor / operating-point / aperture-aggregate / metric-lensing / Op14 / Op16 / c_eff / S_0 / parametric-coupling-kernel / PONDER-05; standard-physics: detector frequency response / H(omega) / Edgeworth / CLT / SPAD / TES / SNSPD / dark count). See §2. |
| `ave-canonical-leaf-pull` | ✓ FIRED. Canonical leaves pulled: parametric-coupling-kernel.md §13 (Phase 0c canonical); Vol 3 Ch 11 nyquist-noise-fdt.md (clm-eaiqj1); KB CLAUDE.md INVARIANT-S2 (operating-point + Op14/Op16 metric-lensing canonical statement); op14-local-clock-modulation.md (clm-1eg13f, $\omega_{local} = \omega_{global}\sqrt{1-A^2}$); translation-instrumentation.md (Category II narrow-aperture single-event extractor taxonomy). See §3. |
| `ave-canonical-source` | ✓ FIRED. Numerical evaluation chain uses canonical constants $\ell_{node} = \hbar/(m_e c)$, $V_y = 43.65$ kV (INVARIANT-C1), $C_0 = \epsilon_0 \ell_{node}$ (parametric-coupling-kernel.md §2), $k_B T$ at 300 K. No hard-coded values; all derive from canonical primitives. |
| `ave-analytical-tool-selection` | ✓ FIRED. Tool class: **Saturation + Time-domain + Boundary + Network**. Specific Op-level tools: Ax 4 kernel (per-site shape — already done Phase 0c); Op14/Op16 (metric-lensing convolution — new piece). Substrate-agnostic mathematical tools: Edgeworth pre-asymptote (cumulant decay across N-site aggregation; standard-stochastics row in translation-stochastics.md). |
| `ave-discipline-translate` v1.1 trigger 6 | ✓ continuous. Substrate-native primary; standard-physics parenthetical. The "detector frequency response convolution" piece must surface as Op14/Op16 metric-lensing convolution NOT as generic-detector-bandwidth analysis. |
| `substrate-native-check` | ✓ FIRED. K4-TLM bond-LC + Cosserat + Ax 4 + Op14/Op16 substrate structure walked. Aperture is real-space lattice region of width $W$ spanning $N$ independent substrate sites; per-site amplitude statistics (Phase 0c canonical) aggregate via substrate-agnostic central-aggregation; substrate noise spectrum convolves against detector frequency-domain response via Op14/Op16 metric-lensing convolution at the aperture-aggregate stage. |
| `consistency-vs-emergence` v1.2 | ✓ FIRED. Class 2 substrate-mechanism emergence on substance axis (load-bearing Ax 4 kernel form + Op14/Op16 metric-lensing as substrate-specific lifts over generic-detector-response treatments); Class 4 substrate-agnostic-consistency on mathematical-tool axis (central-aggregation 1/√N + 1/N scaling is generic). Combined verdict on aperture-aggregate observability axis: Class 2 — because the load-bearing dependency on Ax 4 + Op14/Op16 substrate parameters is explicit. See §5. |
| `phase-space-coordinate-check` | ✓ FIRED. Three coordinate systems kept distinct: (i) **voltage-amplitude space** for per-site δV and aperture-aggregate $V_{aperture} = \sum V_n$; (ii) **K4-TLM real-space lattice** for aperture geometry, width $W$, lattice site count $N$, correlation length $\ell_{corr}$; (iii) **frequency-domain** for substrate noise PSD $S_{substrate}(\omega; V_{DC})$ and detector frequency response $H(\omega)$ (architecture-fixed). The metric-lensing convolution lives in (iii); the per-site cumulants from Phase 0c live in (i); the geometric N count lives in (ii). |
| `ave-evidence-framing-discipline` | ✓ FIRED. Result framing: "derived from Phase 0c per-site $P(\delta V)$ + central-aggregation Edgeworth pre-asymptote across N sites + Op14/Op16 metric-lensing convolution against detector frequency response". NOT "consistent with standard varactor-noise CLT theory" (Class 4 framing). Strength language locked: **Class 2 substrate-mechanism emergence** on substance axis. Per-site signature $\sim 10^{-3}$ at PONDER-05 canonical operating point is the corrected magnitude per auditor Finding 1 on PR #41 (room T, $\eta_T \approx 8 \times 10^{-4}$). Honest event-count estimate for 3σ detection is load-bearing. |
| `ave-discrimination-check` | ✓ FIRED. Standard-physics counterfactual: does standard CLT pre-asymptote treatment (per arbitrary varactor with arbitrary $C(V)$ noise theory) predict the same aperture-aggregate signature? **NO** — because (a) the SPECIFIC kernel form $S(A) = \sqrt{1-A^2}$ (Ax 4 universal, zero free parameters) sets the per-site $\kappa_3$ and $\kappa_4$ scaling-with-$V_{DC}$ in a substrate-distinct way (Phase 0c result); (b) the metric-lensing convolution $c_{eff} \propto \sqrt{S_0}$ (Op14/Op16 canonical) is a substrate-specific lift over generic detector-response treatments (no standard-physics analog because no standard theory has a substrate-state-dependent wave speed). See §4. |
| `verify-before-cite` v1.4 | ✓ continuous. Every file:line cited is grep-verified at composition time. |
| `pre-test-physics-check` | ✓ DECISION: non-firing. Phase 2-NA is the substrate-mechanical derivation work (aperture-aggregate from Phase 0c primitives + metric-lensing convolution), not an experimental test or scaffolded driver. The plumber-physical adjudication happened upstream in the Phase 2 bifurcation walk-back (Grant 2026-05-26: refinement #2 metric-lensing coupling = load-bearing for Phase 2-NA; refinement #1 LLCP scoping = separate sub-epic). The single open plumber-physical question for Phase 2-NA — what is the right aperture geometry × $V_{DC}$ operating point that optimizes the aperture-aggregate observability under competing per-site-signature-shrinkage and site-count-growth effects — is identified explicitly as the optimization target in §3.4; the outcome may surface a structural finding (e.g., observability is monotonic in $V_{DC}$ rather than peaked) which would be a Type E walk-back. |
| `ave-walk-back` v1.1 | ✓ ready. Type E (value-amendment) is the likely walk-back class for sub-derivation surprises (e.g., $S_0^{1/4}$ kernel-correction factor might not be the leading-order behavior under the full metric-lensing convolution). Type B (mechanism re-scope) is possible if the metric-lensing convolution decouples observability from the geometric narrow-aperture constraint (e.g., detector bandwidth filtering completely dominates over geometric N count). |

---

## §2 — Corpus-grep pre-survey (vocabulary-broadened)

Per epic doc pre-survey targets section + 2026-05-26 Q-AX4-NA-2 + Phase 3-A2 Op21 vocabulary-broadened-grep discipline.

**Substrate-native vocabulary cluster** (REQUIRED):

```bash
grep -rn "aperture-aggregate\|aperture aggregate" manuscript/ave-kb/ research/    # epic + Phase 0c result + translation tables; no canonical-leaf hits yet
grep -rn "metric.lensing\|metric lensing\|c_eff.*S\|sqrt.*S_0" manuscript/ave-kb/  # Op16 canonical + INVARIANT-S2 + bullet-cluster (Gordon optical metric); op14-local-clock-modulation.md canonical
grep -rn "Op14\|Op16\|local clock\|universal wave speed" manuscript/ave-kb/       # op14-local-clock-modulation.md primary canonical home; op14-cross-sector-trading.md secondary; common/operators.md catalog
grep -rn "varactor\|operating point\|DC bias\|V_DC\|sub-yield" manuscript/ave-kb/  # parametric-coupling-kernel.md primary; INVARIANT-S2 canonical statement; PONDER-05 secondary
grep -rn "parametric-coupling-kernel\|alpha-slew\|nu_slew" manuscript/ave-kb/      # parametric-coupling-kernel.md cycle-12 + Phase 0c §13 extension
grep -rn "PONDER-05\|V_DC.*V_yield\|0.687\|DC.biased.quartz" manuscript/ave-kb/    # divergence-test-substrate-map B7-PONDER-05; INVARIANT-S2 canonical operating point
```

**Standard-physics vocabulary cluster** (REQUIRED per vocabulary-broadened-grep discipline):

```bash
grep -rn "Edgeworth\|cumulant.*pre.*asymptote\|1/sqrt.*N.*skew\|CLT.pre.*asymptote" manuscript/ave-kb/ research/  # translation-stochastics.md row + Phase 0c §8 + parametric-coupling-kernel.md §13.6
grep -rn "detector frequency response\|H(omega)\|H(\\\\omega)\|detector.*bandwidth" manuscript/ave-kb/ research/    # analog-ladder-filter.md (Z-shell ladder filter; nuclear→1s→valence cascade); cem-methods-survey (FFT-PML); Phase 2-A.2 + A.3 result docs (detector bandwidth ≪ k_B T/ℏ white-noise approximation)
grep -rn "SPAD\|TES\|SNSPD\|APD\|avalanche\|dark count" manuscript/ave-kb/                                          # translation-instrumentation.md Category II
grep -rn "PSD\|spectral density\|noise.*spectrum" manuscript/ave-kb/ research/                                      # Vol 3 Ch 11 nyquist-noise-fdt.md $\langle V^2(f)\rangle = 4 k_B T Z_0 \Delta f$ vacuum Nyquist baseline
grep -rn "frequency.domain\|spectral\|frequency.shift" manuscript/ave-kb/                                           # op14-local-clock-modulation.md §6 falsifiable predictions; Phase 0c §3.1 white-noise approximation
```

**Surveyed canonical leaves entering as load-bearing inputs**:

1. **[`parametric-coupling-kernel.md` §13](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/parametric-coupling-kernel.md):395-470** (Phase 0c canonical extension, 2026-05-26): per-site $P(\delta V)$ closed-form + cumulants + correlation length. **Verified** at cite time.
2. **[`op14-local-clock-modulation.md`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/op14-local-clock-modulation.md)** (clm-1eg13f): $\omega_{local}(r) = \omega_{global}\sqrt{1 - A^2(r)}$ canonical (Vol 4 Ch 1 §sec:thixotropic-relaxation; cross-volume Vol 3 Ch 3 gravity parallel). **Verified** at cite time.
3. **[`nyquist-noise-fdt.md`](../manuscript/ave-kb/vol3/condensed-matter/ch11-thermodynamics/nyquist-noise-fdt.md)** (clm-eaiqj1): vacuum Nyquist baseline $\langle V_{vac}^2(f)\rangle = 4 k_B T Z_0 \Delta f$ + boundary-impedance thermalization $P_{transmitted} = 4 Z_0 Z_{int}/(Z_0 + Z_{int})^2 \cdot P_{incident}$. **Verified** at cite time.
4. **KB CLAUDE.md INVARIANT-S2** (canonical operating-point + Op14/Op16 metric-lensing statement; PONDER-05 at $V_{DC}/V_y = 0.687$). **Verified** at cite time.
5. **[`translation-instrumentation.md`](../manuscript/ave-kb/common/translation-tables/translation-instrumentation.md)**: Category I (wide-aperture continuous-flux) vs Category II (narrow-aperture single-event threshold-triggered) taxonomy; APD/SPAD/TES/SNSPD/MKID substrate-architecture mappings; PONDER-05 secondary architecture (precision-impedance bench, histogram-statistics, not threshold-triggered). **Verified** at cite time.
6. **[`translation-stochastics.md`](../manuscript/ave-kb/common/translation-tables/translation-stochastics.md)** Edgeworth row: aperture-aggregate $\kappa_3/\sigma^3 \sim 1/\sqrt{N}$ + $\kappa_4/\sigma^4 \sim 1/N$ scaling is the substrate-agnostic central-aggregation pre-asymptote. **Verified** at cite time.
7. **[`measurement-hierarchy-snr.md`](../manuscript/ave-kb/vol4/falsification/ch11-experimental-bench/measurement-hierarchy-snr.md):66** — IVIM bench architecture spec, $V_{DC}/V_{yield} = 0.687$ canonical PONDER-05 operating point, $\sim 30$ kV bias. **Verified** at cite time.

**Pre-survey verdict**: corpus has Phase 0c canonical per-site machinery + Op14/Op16 metric-lensing canonical + Category I/II detector taxonomy + Edgeworth pre-asymptote translation row. **All ingredients for Phase 2-NA are canonical**. No upstream derivation gap. Aperture-aggregate central-aggregation + metric-lensing convolution combine canonical inputs through standard mathematical machinery (central-aggregation algebra; frequency-domain convolution). The substrate-distinct content lives in the SPECIFIC inputs (Ax 4 kernel form via Phase 0c; $c_{eff} \propto \sqrt{S_0}$ via Op14/Op16); the mathematical-tool axis is generic.

---

## §3 — A47 canonical-numerical-chain pre-check (mandatory at prereg time)

Per epic brief A47 auditor-arithmetic discipline + 2026-05-26 Phase 0c lesson (Finding 1 on PR #41 caught a 2.7-OOM magnitude error from missed dimensional check on $C_0 V_y^2$). **Explicit numerical evaluation of dimensionless ratios at canonical primitives BEFORE committing to scaling claims.**

### §3.1 Canonical constants

From `src/ave/core/constants.py` + INVARIANT-C1 + parametric-coupling-kernel.md §2 canonical $C_0 = \epsilon_0 \ell_{node}$:

| Quantity | Value | Source |
|---|---|---|
| $\hbar$ | $1.054571817 \times 10^{-34}$ J·s | CODATA |
| $m_e$ | $9.1093837015 \times 10^{-31}$ kg | CODATA |
| $c$ | $2.99792458 \times 10^{8}$ m/s | CODATA exact |
| $\varepsilon_0$ | $8.8541878128 \times 10^{-12}$ F/m | CODATA |
| $k_B$ | $1.380649 \times 10^{-23}$ J/K | CODATA exact |
| $\ell_{node} = \hbar/(m_e c)$ | $3.862 \times 10^{-13}$ m | derived |
| $V_y$ | $4.365 \times 10^{4}$ V | INVARIANT-C1 |
| $C_0 = \varepsilon_0 \ell_{node}$ | $3.419 \times 10^{-24}$ F | parametric-coupling-kernel.md §2 |
| $C_0 V_y^2$ | $6.515 \times 10^{-15}$ J | derived |
| $T$ | 300 K | room temperature |
| $k_B T$ | $4.142 \times 10^{-21}$ J | derived |
| $\eta_T = \sqrt{k_B T/(C_0 V_y^2)}$ | $7.97 \times 10^{-4}$ | substrate-thermal-energy ratio |

### §3.2 PONDER-05 canonical operating point

| Quantity | Value |
|---|---|
| $a = V_{DC}/V_y$ | 0.687 |
| $S_0 = \sqrt{1 - a^2}$ | 0.7267 |
| $S_0^{1/2}$ | 0.8524 |
| $S_0^{3/2}$ | 0.6194 |
| $1/\sqrt{S_0}$ | 1.173 |

### §3.3 Per-site cumulants at PONDER-05 operating point (Phase 0c inputs)

$$\kappa_3/\sigma^3 \big|_{per-site} = -3 a \eta_T \cdot S_0^{-1/2} = -3 \cdot 0.687 \cdot (7.97 \times 10^{-4}) \cdot 1.173 \approx -1.93 \times 10^{-3}$$

$$\kappa_4/\sigma^4 \big|_{per-site} = -3 (1 + 4 a^2) \eta_T^2 \cdot S_0^{-1} = -3 \cdot 2.888 \cdot (6.35 \times 10^{-7}) \cdot 1.376 \approx -7.58 \times 10^{-6}$$

**Sign convention**: $\kappa_3 < 0$ at $V_{DC} > 0$ per Phase 0c §3.4.2 = **substrate-polarity preference toward $\delta V < 0$** (Grant 2026-05-26 substrate-mechanical interpretation; refinement #3 in epic doc). Magnitude is the absolute value.

### §3.4 Substrate correlation length under DC bias

$$\ell_{corr}(0.687) = \ell_{corr}(0) \cdot S_0^{3/2} = \ell_{corr}(0) \cdot 0.6194$$

Linear-regime baseline correlation length (Phase 0c §4.3): $\ell_{corr}(0) \sim \lambda_T = \hbar c/(k_B T) \approx 7.63 \times 10^{-6}$ m at T = 300 K (substrate thermal de Broglie length; macroscopic ~ 10 μm). At PONDER-05 operating point: $\ell_{corr}(0.687) \approx 4.73 \times 10^{-6}$ m. Both scales are macroscopic relative to $\ell_{node} = 3.86 \times 10^{-13}$ m ($\lambda_T / \ell_{node} \approx 2 \times 10^7$).

### §3.5 Metric-lensing convolution numerical scoping

Per Op14 + Op16 canonical (INVARIANT-S2 + op14-local-clock-modulation.md):

$$c_{eff}(V_{DC}) = c_0 \sqrt{S_0} \to c_{eff}(0.687) = c_0 \cdot 0.8524$$

$$\omega_{local}(V_{DC}) = \omega_{global} \sqrt{S_0} \to \omega_{local}(0.687) = 0.8524 \cdot \omega_{global}$$

**Fractional frequency downshift at PONDER-05 operating point**: $1 - \sqrt{S_0} = 1 - 0.8524 = 0.148$ — substrate noise spectrum shifts DOWN by ~15% under DC bias.

### §3.6 A47 sanity-check chain (mandatory)

Cross-check $C_0 V_y^2$ via independent energy-budget identity (parametric-coupling-kernel.md §2 lines 54-56): the canonical α-slew operating point sets $\tfrac12 C_0 V_{pump}^2 = \alpha m_e c^2$ with $V_{pump}/V_y = 0.428$ → $V_{pump} = 18.7$ kV → $\tfrac12 C_0 V_{pump}^2 = \alpha m_e c^2 = (1/137.036) \cdot (8.187 \times 10^{-14})$ J $= 5.97 \times 10^{-16}$ J. From this: $C_0 V_y^2/2 = (V_y/V_{pump})^2 \cdot \alpha m_e c^2 = (1/0.428)^2 \cdot 5.97 \times 10^{-16} = 3.26 \times 10^{-15}$ J → $C_0 V_y^2 = 6.51 \times 10^{-15}$ J ✓ matches direct evaluation in §3.1 within rounding. **Canonical-arithmetic chain verifies.**

### §3.7 Aperture-aggregate scoping (anticipated, prereg expectation)

For an aperture of width $W$ spanning $N$ independent substrate lattice sites, **substrate-agnostic central-aggregation** (Edgeworth pre-asymptote across $N$ independent equal-variance per-site contributions):

$$\kappa_3^{(aperture, geo)}/\sigma_{aperture}^3 = \frac{\kappa_3^{(per-site)}/\sigma_{per-site}^3}{\sqrt{N}} = \frac{-3 a \eta_T S_0^{-1/2}}{\sqrt{N}}$$

$$\kappa_4^{(aperture, geo)}/\sigma_{aperture}^4 = \frac{\kappa_4^{(per-site)}/\sigma_{per-site}^4}{N} = \frac{-3 (1 + 4 a^2) \eta_T^2 S_0^{-1}}{N}$$

**Geometric-N at fixed aperture width**: $N(V_{DC}) = W/\ell_{corr}(V_{DC}) = (W/\ell_{corr}(0)) \cdot S_0^{-3/2}$. For 2D aperture ($d = 2$): $N(V_{DC}) = N(0) \cdot S_0^{-3 d/2} = N(0) \cdot S_0^{-3}$.

**Substituting into the aperture-aggregate skewness** (1D aperture for prereg; 2D treated in result):

$$\kappa_3^{(aperture, geo)}/\sigma_{aperture}^3 = \frac{-3 a \eta_T S_0^{-1/2}}{\sqrt{N(0) S_0^{-3/2}}} = \frac{-3 a \eta_T S_0^{1/4}}{\sqrt{N(0)}}$$

The kernel-correction factor $S_0^{1/4}$ is mild: at $a = 0.687$, $S_0^{1/4} = 0.923$. **Anticipated leading scaling**: aperture-aggregate skewness $\sim 10^{-3}/\sqrt{N(0)}$, i.e., ~$5 \times 10^{-4}$ at $N(0) = 10$.

**Numerical sanity-check at PONDER-05 operating point** ($a = 0.687$, $N = 10$):
- $\kappa_3^{(apt)}/\sigma_{apt}^3 \approx -1.93 \times 10^{-3} / \sqrt{10} \approx -6.1 \times 10^{-4}$
- $\kappa_4^{(apt)}/\sigma_{apt}^4 \approx -7.58 \times 10^{-6} / 10 \approx -7.6 \times 10^{-7}$
- $N_{events}$ for 3σ detection of $\kappa_3$: $\sim 9/(\kappa_3^{apt}/\sigma_{apt}^3)^2 \approx 2.4 \times 10^7$ events

**Anticipated `consistency-vs-emergence` classification of the aperture-aggregate observability**: Class 2 substrate-mechanism on substance axis (load-bearing on Ax 4 kernel form via Phase 0c per-site shape AND on Op14/Op16 metric-lensing via the convolution step); Class 4 substrate-agnostic-consistency on mathematical-tool axis (central-aggregation 1/√N decay is generic).

---

## §4 — Substrate-mechanical derivation outline (anticipated, locked at prereg time)

### §4.1 Aperture-aggregate central-aggregation across N independent sites

For an aperture spanning N independent substrate lattice sites with per-site amplitudes $V_n = V_{DC} + \delta V_n$ (with $\delta V_n$ statistically independent across sites by definition of $\ell_{corr}$), the aperture-aggregate amplitude is $V_{aperture} = \sum_{n=1}^N V_n$. Variance, skewness, and kurtosis of the aperture-aggregate follow from cumulant additivity over independent sites:

- $\sigma_{aperture}^2 = N \sigma_{per-site}^2$
- $\kappa_3^{aperture} = N \kappa_3^{per-site}$
- $\kappa_4^{aperture} = N \kappa_4^{per-site}$ (excess kurtosis cumulant additive form)

Dividing by powers of $\sigma_{aperture}$ for the dimensionless cumulants:

$$\kappa_3^{aperture}/\sigma_{aperture}^3 = \frac{N \kappa_3^{per-site}}{N^{3/2} (\sigma_{per-site}^2)^{3/2}} = \frac{\kappa_3^{per-site}/\sigma_{per-site}^3}{\sqrt{N}}$$

$$\kappa_4^{aperture}/\sigma_{aperture}^4 = \frac{N \kappa_4^{per-site}}{N^2 (\sigma_{per-site}^2)^2} = \frac{\kappa_4^{per-site}/\sigma_{per-site}^4}{N}$$

This is the substrate-agnostic Edgeworth pre-asymptote (per [`translation-stochastics.md`](../manuscript/ave-kb/common/translation-tables/translation-stochastics.md) Edgeworth row; standard-physics community names it "CLT correction" or "Edgeworth expansion").

### §4.2 Substrate correlation length and N under DC bias

Per Phase 0c §4.2 canonical: $\ell_{corr}(V_{DC}) = \ell_{corr}(0) \cdot S_0^{3/2}$ (INVARIANT-S2 SYM-class realization; shrinks toward yield).

For a $d$-dimensional aperture of characteristic linear size $W$ spanning real-space lattice region of volume $W^d$ (with $d = 1$ for a 1D linear aperture along an edge; $d = 2$ for a 2D surface aperture — typical for boundary-extraction geometries; $d = 3$ for a 3D bulk aperture):

$$N(V_{DC}) = \left(\frac{W}{\ell_{corr}(V_{DC})}\right)^d = N(0) \cdot S_0^{-3d/2}$$

Under DC bias, N **grows** as $S_0^{-3d/2}$ at fixed $W$ (more independent sites in same aperture width, because correlation length shrinks).

### §4.3 Combined sub-saturation regime $V_{DC}$-dependence (geometric-only, pre-metric-lensing)

Substituting §4.2 into §4.1:

$$\kappa_3^{(aperture, geo)}(V_{DC})/\sigma_{aperture}^3 = \frac{-3 a \eta_T S_0^{-1/2}}{\sqrt{N(0)} S_0^{-3d/4}} = \frac{-3 a \eta_T}{\sqrt{N(0)}} \cdot S_0^{(3d-2)/4}$$

For $d = 1$ (1D aperture): $S_0$ exponent is $1/4$ — mild correction; per Phase 0c §8.

For $d = 2$ (2D aperture): $S_0$ exponent is $1$ — competition between $a$-growth (linear) and $S_0$-shrinkage (linear). **Substrate-mechanical question**: does $\kappa_3^{(aperture)}$ peak at intermediate $V_{DC}/V_y$, or grow monotonically toward yield?

To find the peak (at fixed $W$, 2D aperture): take $d/da \left[a \cdot S_0\right] = S_0 + a \cdot dS_0/da = \sqrt{1-a^2} - a^2/\sqrt{1-a^2} = (1 - 2a^2)/\sqrt{1-a^2}$. Setting to zero: $a^2 = 1/2$ → $\boxed{a_{peak}^{(2D)} = 1/\sqrt{2} \approx 0.707}$.

**Anticipated finding**: at fixed 2D aperture width and 1D aperture-aggregate observable, the substrate-saturation × narrow-aperture observability **PEAKS at $V_{DC}/V_y = 1/\sqrt{2} \approx 0.707$** — within ~3% of the PONDER-05 canonical operating point $a = 0.687$. **This is a substantive substrate-mechanical prediction**: PONDER-05's $V_{DC}/V_y = 0.687$ operating point is within rounding of the substrate-saturation × narrow-aperture sweet spot for 2D aperture geometry.

For $d = 3$: $S_0$ exponent is $7/4$ — peak at $a^2 = ?$ derivable similarly; result is documented in result doc.

### §4.4 Metric-lensing convolution against detector frequency response (the new piece beyond pure central-aggregation)

Per INVARIANT-S2 + Op14 + Op16 canonical (op14-local-clock-modulation.md):

$$c_{eff}(V_{DC}) = c_0 \sqrt{S_0}, \qquad \omega_{local}(V_{DC}) = \omega_{global} \sqrt{S_0}$$

For a substrate mode at fixed wavelength $\lambda$ (set by aperture geometry + boundary impedance match), the corresponding frequency at the operating-point-loaded substrate is $\omega(V_{DC}) = c_{eff}/\lambda \propto \sqrt{S_0}$ — substrate noise spectrum shifts **down** under DC bias.

The detector has a fixed frequency response $H(\omega)$ (architecture-fixed; set by device-construction at fab time — not modulated by substrate operating point). Per Vol 3 Ch 11 nyquist-noise-fdt.md (clm-eaiqj1), the substrate noise PSD seen by a detector boundary-impedance-thermalized at $Z_{det}$ is:

$$S_{substrate}(\omega; V_{DC}) = 4 k_B T \cdot Z_{eff}(V_{DC}) \cdot |T_{boundary}(\omega; V_{DC})|^2$$

where $Z_{eff}(V_{DC}) = Z_0/\sqrt{S_0}$ (Op14 canonical) and $T_{boundary}(\omega; V_{DC})$ is the boundary transmission spectrum, which depends on substrate operating point through $c_{eff}$ (Op16). The full substrate-noise PSD shifts down in frequency by $\sqrt{S_0}$ under DC bias.

The effective detector-seen noise power per unit aperture area:

$$P_{detector}(V_{DC}) = \int_0^\infty |H(\omega)|^2 S_{substrate}(\omega; V_{DC}) \, d\omega$$

**Substrate-mechanical implication for the aperture-aggregate observable**: the detector might not respond to the shifted high-frequency tail of the substrate-noise spectrum, which changes the **effective $N_{detector}$** (how many independent substrate-mode contributions the detector actually integrates over) from the geometric $N_{geometric}(V_{DC})$ above.

### §4.5 Effective $N_{detector}(V_{DC})$ as a function of $N_{geometric}(V_{DC})$ + detector frequency response

**Substrate-native derivation** (anticipated; locked at prereg time):

The substrate noise PSD at the operating-point-loaded substrate is **band-limited** by the substrate's own characteristic frequencies. The relevant substrate frequency scales:

- **Upper substrate-mode frequency**: $\omega_{max}(V_{DC}) = c_{eff}/\ell_{node} = (c_0/\ell_{node}) \sqrt{S_0} = \omega_{Compton} \sqrt{S_0}$ — Compton-scale UV cutoff, shifts down by $\sqrt{S_0}$ under DC bias.
- **Lower substrate-mode frequency at aperture**: $\omega_{min}(V_{DC}, W) = c_{eff}/W = (c_0/W) \sqrt{S_0}$ — aperture-set IR cutoff, also shifts down by $\sqrt{S_0}$.
- **Substrate noise bandwidth**: $\Delta\omega(V_{DC}) = \omega_{max} - \omega_{min} \approx \omega_{max} = \omega_{Compton} \sqrt{S_0}$ for $W \gg \ell_{node}$.

The substrate-mode density per unit aperture area is $\rho_{modes} \propto N_{geometric}(V_{DC})$ (one substrate mode per independent lattice site by Nyquist counting in real-space).

**Detector frequency response**: parametrize $H(\omega)$ by a characteristic bandwidth $\Delta\omega_{det}$ and central frequency $\omega_{det}$. The detector integrates only those substrate modes whose frequencies fall within $|H(\omega)|^2$ support.

**Effective $N_{detector}$** = number of independent substrate modes the detector actually integrates over:

$$N_{detector}(V_{DC}) = N_{geometric}(V_{DC}) \cdot \mathcal{F}(\Delta\omega_{det}, \omega_{det}; V_{DC})$$

where $\mathcal{F}$ is the **frequency-domain visibility factor** — the fraction of the substrate-mode-density bandwidth that overlaps with detector response. **Substrate-mechanical reasoning** (locked at prereg time):

**Case A — broadband detector** ($\Delta\omega_{det} \gtrsim \omega_{max}(V_{DC})$): detector responds to all substrate modes → $\mathcal{F} \approx 1$ → $N_{detector} = N_{geometric}$. The metric-lensing convolution does not alter the aperture-aggregate signature (only the central-aggregation 1/√N scaling matters).

**Case B — narrowband detector at fixed central frequency $\omega_{det}$** (matched to substrate-mode at zero bias): under DC bias, the substrate-mode spectrum shifts down by $\sqrt{S_0}$; the detector central frequency does NOT shift (architecture-fixed). The detector's $|H(\omega)|^2$ support moves OUT of the substrate-mode-density support. → $\mathcal{F}(V_{DC}) < 1$ → $N_{detector}(V_{DC}) < N_{geometric}(V_{DC})$.

**Case C — narrowband detector at fixed central frequency tuned for the loaded operating point**: detector central frequency is co-designed with the DC bias operating point. → $\mathcal{F} \approx 1$ → $N_{detector} = N_{geometric}$. This is the **operationally optimal regime** for measuring the substrate-saturation × narrow-aperture observable.

**Anticipated finding**: $\mathcal{F}$ is the substrate-distinct Op14/Op16 convolution piece. Standard-physics treatments (which have no substrate-state-dependent wave speed) cannot generate this convolution factor. **This is the substrate-distinct lift over generic detector-response treatments**.

### §4.6 Aperture-aggregate observable signature with metric-lensing convolution

Combining §4.3 (geometric central-aggregation) and §4.5 (metric-lensing convolution):

$$\kappa_3^{(aperture)}/\sigma_{aperture}^3 = \frac{-3 a \eta_T}{\sqrt{N(0) \cdot \mathcal{F}(\Delta\omega_{det}, \omega_{det}; V_{DC})}} \cdot S_0^{(3d-2)/4}$$

For Case A (broadband detector), $\mathcal{F} \approx 1$ — recovers the geometric central-aggregation result; PONDER-05 canonical operating point near $a^{(2D)}_{peak} = 1/\sqrt{2}$.

For Case B (narrowband detector mistuned), $\mathcal{F} < 1$ — fewer effective independent contributions → weaker aperture-aggregate suppression of $\kappa_3$ → **STRONGER aperture-aggregate signature than geometric expectation**. The metric-lensing convolution can ENHANCE the observable signature when detector bandwidth is mistuned for the operating point.

For Case C (narrowband detector tuned for loaded operating point), $\mathcal{F} \approx 1$ — same as Case A; this is the operationally optimal regime.

### §4.7 Mapping to candidate boundary-extraction architectures

Per [`translation-instrumentation.md`](../manuscript/ave-kb/common/translation-tables/translation-instrumentation.md):

| Category | Architecture | $N_{geometric}$ regime | $\mathcal{F}$ regime | Anticipated observability |
|---|---|---|---|---|
| I | Photodiode / PMT / CCD / bolometer (wide-aperture continuous-flux) | $N \gg 10^9$ | broadband; $\mathcal{F} \approx 1$ | washed out (large N suppresses) |
| II | APD / SPAD / TES / SNSPD (narrow-aperture single-event threshold-triggered) | $N \sim 10^3$-$10^6$ | narrowband; $\mathcal{F}$ depends on design | event-by-event threshold; signature visible IF substrate-saturation regime engaged at aperture |
| II | **PONDER-05-class precision-impedance bench (DC-biased quartz, histogram-statistics)** | **$N \sim 10$-$10^4$** (narrow boundary aperture at quartz-vacuum interface) | **architecture-dependent; PONDER-05 designs for matched operating point — Case C** | **DIRECTLY observable at $V_{DC}/V_y = 0.687$ canonical operating point** ($\sim$3% off the 2D peak); $\sim 10^7$ events for 3σ |
| III | Superconducting qubit / transmon / SQUID | Coupled bidirectional; not one-way extractors | N/A — quantum-information substrate-mode coupling | not directly applicable |

**Empirical-engagement target**: PONDER-05-class precision-impedance bench. The PONDER-05 architecture sits at $a = 0.687$ which is within 3% of the 2D aperture-aggregate peak $a^{(2D)}_{peak} = 1/\sqrt{2} = 0.707$, AND PONDER-05 is designed Case C (detector frequency response matched to the loaded operating-point substrate-mode frequencies via the impedance-bench detection topology — Phase 2 result will verify this from the PONDER-05 architecture spec). **Phase 2-NA's headline prediction is the PONDER-05-class aperture-aggregate amplitude-statistics signature**: $\kappa_3^{(apt)}/\sigma^3 \sim 5 \times 10^{-4}$ at $N \sim 10$, $\sim 3 \times 10^7$ events for 3σ detection in room-T amplitude-statistics histograms.

### §4.8 Honest event-count estimate

For 3σ detection of the aperture-aggregate skewness $|\kappa_3^{(apt)}/\sigma^3| = K_3$, the event-count requirement (per Edgeworth pre-asymptote standard error $\sqrt{6/N_{events}}$):

$$N_{events}^{(3\sigma)} = \frac{9 \cdot 6}{K_3^2} = \frac{54}{K_3^2}$$

Wait — standard error on sample skewness in Edgeworth pre-asymptote is $\sqrt{6/N_{events}}$, so 3σ detection requires $K_3 / \sqrt{6/N_{events}} = 3$ → $N_{events} = 54/K_3^2$.

**At PONDER-05 operating point, $N(0) = 10$, $a = 0.687$, $\mathcal{F} = 1$ (Case C)**:
- $K_3^{(apt)} \approx 5 \times 10^{-4}$
- $N_{events}^{(3\sigma)} = 54 / (5 \times 10^{-4})^2 \approx 2.2 \times 10^8$ events

Conservative: **$\sim 10^8$ events for 3σ skewness detection in a room-T narrow-aperture histogram-statistics campaign**. At a sampling rate of $\sim 10^7$ events/s (achievable in modern precision-impedance benches), this corresponds to $\sim 10$ s of acquisition — operationally feasible. (Note: this is 1 OOM higher than the $3 \times 10^7$ estimate in parametric-coupling-kernel.md §13.6, which uses $9/K_3^2$; both are estimates of similar OOM. Result doc clarifies the exact statistical formula.)

Aperture-aggregate kurtosis is much harder: $K_4^{(apt)} \approx 7.6 \times 10^{-7}$, $N_{events}^{(3\sigma)} \sim 24 / K_4^2 \approx 4 \times 10^{13}$ events — kurtosis is operationally inaccessible at room T. **Skewness is the load-bearing observable for Phase 2-NA empirical engagement**.

---

## §5 — Acceptance criteria

| AC | Criterion | Adjudication |
|---|---|---|
| **AC-2NA.1** | Aperture-aggregate central-aggregation derived end-to-end from Phase 0c per-site $P(\delta V)$ + Edgeworth pre-asymptote | PASS if closed forms $\kappa_3^{(apt)}/\sigma^3$ + $\kappa_4^{(apt)}/\sigma^4$ derived with explicit $V_{DC}$-dependence + $N$-dependence + dimensionality $d$-dependence |
| **AC-2NA.2** | Combined sub-saturation regime $V_{DC}$-dependence with substrate correlation length shrinkage included | PASS if $S_0^{(3d-2)/4}$ kernel-correction factor derived for general dimensionality; peak operating point $a^{(d)}_{peak}$ derived for $d = 1, 2, 3$ |
| **AC-2NA.3** | Metric-lensing convolution against detector frequency response derived from Op14 + Op16 + boundary-impedance thermalization | PASS if $N_{detector}(V_{DC}) = N_{geometric}(V_{DC}) \cdot \mathcal{F}(\Delta\omega_{det}, \omega_{det}; V_{DC})$ derived with explicit broadband-vs-narrowband detector classification (Cases A/B/C) |
| **AC-2NA.4** | Mapping to candidate boundary-extraction architectures explicit | PASS if Category I (washed out) + Category II (visible IF saturation regime engaged at aperture) + PONDER-05 (directly observable at $a = 0.687$ near $a^{(2D)}_{peak}$) classification derived; PONDER-05 Case A/B/C classification surfaced |
| **AC-2NA.5** | Honest event-count estimate for 3σ skewness detection at PONDER-05 operating point | PASS if $N_{events}^{(3\sigma)}$ in range $10^7$-$10^9$ (anticipated $\sim 10^8$) with explicit calculation chain (sample-skewness standard-error formula → $K_3$ → event count); honest acknowledgment that kurtosis is operationally inaccessible at room T |
| **AC-2NA.6** | Class 2 / Class 4 classification on aperture-aggregate observability axis | PASS if §5 in result doc explicitly classifies: Class 2 substrate-mechanism on substance axis (Ax 4 kernel form via Phase 0c + Op14/Op16 metric-lensing); Class 4 substrate-agnostic-consistency on mathematical-tool axis (central-aggregation 1/√N + 1/N scaling) |
| **AC-2NA.7** | Honest closure of any structural sub-problem | PASS if any Type B (mechanism re-scope) or Type E (value-amendment) walk-back from prereg expectations is honestly documented in result doc §6 |
| **AC-2NA.8** | KB integration clean | PASS if either parametric-coupling-kernel.md §14 in-place extension OR new canonical leaf at vol4/circuit-theory/ch1-vacuum-circuit-analysis/ for aperture-aggregate prediction is well-scoped + non-disruptive to existing §13 (Phase 0c canonical) |

**Pre-locked PASS criteria**: All 8 ACs must pass for overall PASS. PARTIAL: AC-2NA.1, .2, .4, .5, .6, .8 pass + AC-2NA.3 stuck on sub-problem (e.g., detector-frequency-response model not canonicalize-able without device-specific input); document gap. WALK-BACK: derivation surfaces structural problem (e.g., substrate-correlation-length-shrinkage outpaces per-site-signature-growth + metric-lensing convolution forces aperture-aggregate observability to monotonically DECREASE with $V_{DC}$ → forces epic re-scope toward Phase 2-LLCP exclusively).

**Honest closure probability**: ~75% PASS / ~20% PARTIAL on metric-lensing convolution (AC-2NA.3) / ~5% WALK-BACK.

---

## §6 — Deliverables

1. **Pre-reg** (this doc) — locked before derivation begins; A47 numerical chain in §3 frozen
2. **Result doc** at `research/2026-05-26_ax4-saturation-phase-2-na-aperture-aggregate-result.md` — derivation end-to-end with adjudication against §5 ACs
3. **KB integration**: extend [`parametric-coupling-kernel.md`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/parametric-coupling-kernel.md) with new §14 aperture-aggregate prediction OR promote to new canonical leaf at `vol4/circuit-theory/ch1-vacuum-circuit-analysis/ax4-aperture-aggregate-amplitude-shape.md` — decision deferred to result-doc-writing time based on §13 vs §14 scope balance
4. **Epic doc update**: [`_orchestration/ax4-saturation-narrow-aperture-amplitude-shape.md`](../_orchestration/ax4-saturation-narrow-aperture-amplitude-shape.md) Phase 2-NA row from "READY TO SCOPE" to "✓ CLOSED" (if PASS) + Phase 2-NA execution log entry
5. **Refresh + verify pipeline PASS** before push (`make refresh-kb-metadata` + `make verify-kb-metadata`)

---

## §7 — Out of scope (deferred)

- **Phase 2-LLCP**: separate critical-point regime sub-epic per epic doc bifurcation walk-back. Phase 0c Boltzmann-around-V_DC framework does NOT apply at the substrate critical point (power-law tails + diverging correlation length + undefined moments). The substrate-mechanical observable in the critical-point regime is **avalanche trigger rate vs $V_{DC}$ proximity to substrate critical point** — SPAD/APD-class real-detector empirical-engagement path lives there.
- **Phase 3**: KB integration to divergence-test substrate map as new forward-prediction row(s).
- **Detector-specific frequency-response derivation for individual device classes** (SPAD vs TES vs SNSPD architectures): Phase 2-NA derives the metric-lensing convolution at the GENERIC narrowband-vs-broadband classification level; specific-device-class derivations are future Phase 4 work scoping individual empirical campaigns.
- **Cosserat-rotational DOF channel coupling at the aperture** (refinement #1 of Q-AX4-NA-2 sub-mechanisms): Phase 0c result doc §6 notes that Cosserat-rotational coupling could be a sub-mechanism affecting the per-site amplitude-shape; Phase 2-NA inherits Phase 0c per-site result and does not re-open this sub-question.

---

## §8 — Pre-survey cross-references

- **Epic anchor**: [`_orchestration/ax4-saturation-narrow-aperture-amplitude-shape.md`](../_orchestration/ax4-saturation-narrow-aperture-amplitude-shape.md) — full epic context including the 2026-05-26 Phase 2 bifurcation walk-back (Phase 2-NA = this scope; Phase 2-LLCP = separate critical-point regime sub-epic)
- **Phase 0c inputs**: [`2026-05-26_ax4-saturation-phase-0c-pdelta-v-derivation-result.md`](./2026-05-26_ax4-saturation-phase-0c-pdelta-v-derivation-result.md) + [`parametric-coupling-kernel.md` §13](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/parametric-coupling-kernel.md)
- **Op14/Op16 metric-lensing canonical**: [`op14-local-clock-modulation.md`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/op14-local-clock-modulation.md) (clm-1eg13f); INVARIANT-S2 in KB CLAUDE.md
- **Vol 3 Ch 11 nyquist-noise-fdt.md** (clm-eaiqj1): boundary-impedance thermalization scaffold for substrate noise PSD
- **Translation tables**: [`translation-stochastics.md`](../manuscript/ave-kb/common/translation-tables/translation-stochastics.md) Edgeworth row; [`translation-instrumentation.md`](../manuscript/ave-kb/common/translation-tables/translation-instrumentation.md) Category I/II taxonomy
- **PONDER-05 architecture**: [`measurement-hierarchy-snr.md`](../manuscript/ave-kb/vol4/falsification/ch11-experimental-bench/measurement-hierarchy-snr.md):66 (IVIM bench, 30 kV DC bias at $V_{DC}/V_y = 0.687$ canonical operating point); [`divergence-test-substrate-map.md`](../manuscript/ave-kb/common/divergence-test-substrate-map.md) B7-PONDER-05 row
- **dama-matched-lc-coupling.md:269 open strengthen-by item**: PARTIALLY closed by Phase 0c (single-site); Phase 2-NA does not directly touch this item (aperture-aggregate is a derived consequence, not an additional partial closure)

---

**Pre-reg locked 2026-05-26 prior to derivation work**. Single-deliverable session — Phase 2-NA aperture-aggregate derivation only. Phase 2-LLCP separate sub-epic; Phase 3 KB integration deferred.
