# FT-Cold-Fusion η(x) Result — Parameter-free Pd-D fusion-rate-vs-loading curve

**Date**: 2026-05-31
**Branch**: `analysis/ft-coldfusion-eta-x-derivation` (off `main`)
**Pre-registration**: [`2026-05-31_FT-coldfusion-eta-x-curve_prereg.md`](2026-05-31_FT-coldfusion-eta-x-curve_prereg.md) (PREREG-FROZEN, this branch)
**Mechanism foundation**: [`2026-05-31_Q-EMBED-SEL-1_step_c_phase3_cold_fusion_result.md`](2026-05-31_Q-EMBED-SEL-1_step_c_phase3_cold_fusion_result.md) (Class B, 5/5 multi-falsifier PASS)
**Driver**: [`src/scripts/vol_2_subatomic/coldfusion_eta_x_curve.py`](../src/scripts/vol_2_subatomic/coldfusion_eta_x_curve.py)
**Figure**: [`assets/figures/coldfusion_eta_x_curve.png`](../assets/figures/coldfusion_eta_x_curve.png)

---

## §0 — Verdict (TL;DR)

**OUTCOME C — the parameter-free forward curve is well-formed and falsifiable, but the published LENR data landscape contains NO loading-resolved excess-heat / fusion-rate curve to test the predicted SHAPE + threshold LOCATION against. The discriminating experiment is specified in §5.**

This is a fully valid pre-registered result (prereg §5 + §7: "Outcome C (untestable) is a live and honest possibility — pre-register it as a legitimate result, not a failure to avoid"). The forward curve is computed, plotted, and its three thresholds marked; the falsifier (§6 of the prereg) is sharp and would fire against a future loading-resolved dataset. What is absent is the *data axis*: no public dataset reports excess heat or D-D fusion rate **as a function of** the D/Pd loading ratio `x`.

---

## §1 — The forward curve (computed, parameter-free)

The driver computes, from canonical constants only (`ALPHA` = `constants.py:133`, `R_I = √(2α)` = `constants.py:402`) plus the single flagged metallurgical coefficient `0.13`:

$$A_0(x) = \frac{0.13\,x}{\sqrt{2\alpha}}, \quad S(A_0)=\sqrt{1-A_0^2}, \quad n_{scalar}=\frac1S, \quad \frac{\eta(x)}{\eta_0}=S(A_0), \quad \frac{P_{fusion}(x)}{P_{fusion}(0)}=e^{-2\eta_0(S-1)}.$$

The substrate **narrows the Gamow tunnelling distance** (coordinate compression $\mathrm{d}r_{lab}=\mathrm{d}r_{vac}/n$, AVE-Fusion Ch3:51) — it does **not** lower the Coulomb barrier height. Driver output over $x\in[0.80,0.93]$:

| x (D/Pd) | $A_0$ | $S=\eta/\eta_0$ | $n_{scalar}$ | regime |
|---|---|---|---|---|
| 0.800 | 0.8609 | 0.5088 | 1.965 | $\Gamma>0$ (discrete radiation channels) |
| 0.820 | 0.8824 | 0.4705 | 2.125 | $\Gamma>0$ |
| 0.840 | 0.9039 | 0.4277 | 2.338 | $\Gamma>0$ |
| **0.852** | 0.9168 | 0.3993 | **2.504** | **$\Gamma\to0$ (radiation-less; heat-not-$\gamma$)** |
| 0.870 | 0.9362 | 0.3515 | 2.845 | $\Gamma\to0$ |
| 0.900 | 0.9685 | 0.2491 | 4.014 | $\Gamma\to0$ |
| 0.920 | 0.9900 | 0.1411 | 7.087 | $\Gamma\to0$ |
| **0.929** | 0.9997 | 0.0253 | 39.589 | **$A_0\ge1$ (shatter / yield)** |

**Parameter-free content** (prereg §4): the SHAPE $\eta(x)/\eta_0 = S(A_0)$ and the threshold LOCATIONS are fully fixed by $\sqrt{2\alpha}$ + the `0.13` coefficient. $\eta_0$ (vacuum Gamow exponent) sets only the absolute rate and additionally carries environmental-screening uncertainty; the driver therefore plots $\eta(x)/\eta_0$ as the primary curve (no $\eta_0$ needed) and shows $\log_{10}(P/P_0)$ for an **explicit $\eta_0$ scale family** $\{3,5,7\}$ — drawn as a band, NOT fitted to any data.

**Figure** (`assets/figures/coldfusion_eta_x_curve.png`):
- Top panel — parameter-free $\eta(x)/\eta_0 = S(A_0)$, monotonically dropping from $\approx0.51$ at $x=0.80$ to $\approx0$ at the shatter line, with the $S=0.4$ ($n=2.5$) reference and the operational-window shading.
- Bottom panel — $\log_{10}[P_{fusion}(x)/P_{fusion}(0)]$ for $\eta_0\in\{3,5,7\}$; identical shape, $\eta_0$ only rescales the vertical axis.

## §2 — The three marked loadings (all parameter-free, all from canonical constants)

| Marker | Loading $x$ | Substrate condition | Physical meaning |
|---|---|---|---|
| **$x_{onset}$** | **0.8048** | $n_{scalar}=2.0$ ($S=0.5$) | Tunnelling distance halved; compression becomes order-unity significant. Sits at the left edge of the operational window. |
| **$x_{radiationless}$** | **0.8517** | $n_{scalar}=2.5$ ($S=0.4$); $Z_{matrix}=Z_0/2.5=Z_{node}$ → $\Gamma\to0$ | The radiation-less ($\Gamma\to0$) threshold: acoustic-phonon (heat) channel opens, discrete $\gamma$ emission suppressed. The substrate-mechanism for FP's "missing radiation". Reproduces prereg's 0.852. |
| **$x_{shatter}$** | **0.9293** | $A_0=1$ exactly; Ax-4 yield; $\Delta V/V_0=\sqrt{2\alpha}\approx12.08\%$ | Substrate shatter / zero-impedance phase fault. Reproduces prereg's 0.929 = $\sqrt{2\alpha}/0.13$. Brackets the empirical 10–12% Pd metallurgical destruction bound. |

Reference (not a primary marker): the FP extreme corner $n_{scalar}=200$ lands at $x=0.9293$ — i.e. within the ~2.9% operational sliver $[0.852, 0.929]$, matching the Phase-3 result's 0.92929 and the canonical Topological Survival Window (AVE-Fusion Ch4:64–80).

## §3 — Data survey (loading-resolved excess-heat / fusion-rate data)

The prereg discriminators are the curve **SHAPE** and the **threshold LOCATION**, both of which require data plotted with **loading ratio `x` on the x-axis**. The survey targeted exactly that: published datasets reporting excess heat or D-D fusion rate *as a function of* `x = D/Pd` (or `D/metal`).

### §3.1 — NASA Glenn lattice-confinement fusion (Steinetz et al., the solid peer-reviewed anchor)

- **Source**: NASA Glenn lattice-confinement-fusion program page (`nasa.gov/glenn/.../lattice-confinement-fusion/`); NASA TM-2020-5001734 + *Phys. Rev. C* 101, 044610 (2020).
- **Method (verified)**: deuterated **erbium (ErD₃)** and titanium hosts; deuterons photodissociated by a **2.9⁺ MeV γ (bremsstrahlung) beam**; neutrons (~2.5 MeV from D-D → n + ³He, plus 4–5 MeV from secondary processes) and protons (D-D → p + T) detected. Lattice electrons "screen" the deuteron Coulomb barrier.
- **Loading-resolved?** **NO.** NASA Glenn reports the fusion-evidence at the program's fixed high-density loading and emphasises overall fuel density ("a billion times denser than tokamak"), but does **not** report fusion rate as a function of the D/metal loading ratio. There is no NASA Glenn curve with `x` on the x-axis.
- **Verdict**: NASA Glenn is a *strong, qualitative* anchor for the **mechanism direction** (lattice loading → barrier screening → keV-scale fusion at room temperature, SM-anomalous) and is consistent with the predicted radiation-less heat-not-γ regime in spirit. But it provides **no loading-resolved curve** to test the predicted SHAPE or threshold LOCATION. It pins one operating point, not a curve.

### §3.2 — Google-funded program (Berlinguette et al., *Nature* 570, 45 (2019))

- **Source**: *Nature* 570, 45–51 (2019), "Revisiting the cold case of cold fusion" (paywalled; findings via Science/Nature news coverage + Wikipedia summary).
- **Finding (verified)**: a 3-year, multi-institution, ~$10M effort across Pd-D electrolysis, metal-deuteride gas loading, and ion-beam implantation. Bottom line: **"no evidence that the phenomenon exists"** — no reproducible excess heat.
- **Loading as a variable**: the program's documented central obstacle was *achieving and maintaining the high loading* (D/Pd near 1) that FP-era researchers believed necessary — Pd cracks under the loading pressure and the deuterium escapes (the same metallurgical-fracture mechanism the AVE survival-window invokes). They did **not** publish excess heat as a *function* of a controlled, resolved loading ratio; loading was the hard-to-reach confound, not a swept independent axis.
- **Verdict**: a careful **null**, but **not loading-resolved**. It does not provide a heat-vs-`x` curve. Notably, the program's own difficulty in reaching/holding `x≈0.9` is *qualitatively consistent* with the AVE razor-thin-window framing — but this is interpretive resonance, not a test of the curve.

### §3.3 — Classic Pd-D electrolysis loading-threshold claims (McKubre / ENEA / Storms)

- **Source**: secondary (Wikipedia cold-fusion article + standard LENR reviews).
- **Finding (verified)**: McKubre (since 1994) and ENEA (2011) **speculated** that a cell loaded below D/Pd ≈ 1:1 will not produce excess heat — i.e. a *threshold near full loading* is part of the LENR folklore. High loading "is hard to obtain, and some batches of palladium never reach it because the pressure causes cracks in the palladium, allowing the deuterium to escape." Pd suppliers later changed manufacturing, frustrating replication.
- **Loading-resolved?** **NO published curve.** The threshold claim exists as a *qualitative speculation* (excess heat needs `x` near 1), directionally consistent with the AVE prediction of an onset near `x ~ 0.85`. But there is no systematic dataset plotting excess heat vs a controlled `x` across $[0.8, 0.93]$ — loading is an "acknowledged but uncontrolled variable."

### §3.4 — Modern programs (ARPA-E LENR, 2023→)

- **Source**: DOE ARPA-E LENR program announcements (2023, ~$10M, 8 projects).
- **Finding (verified)**: one University of Michigan project's *stated goal* is to "systematically evaluate claims of excess heat generation during deuteration and **correlate it to nuclear and chemical reaction products**" with ±0.5% calorimetry. The program exists **precisely because** the field "historically has not provided such controlled, systematic data."
- **Loading-resolved?** **NOT YET.** As of this survey these are project descriptions, not published datasets. The loading-resolved correlation the AVE curve needs is exactly what ARPA-E was funded to *produce* — it does not yet exist in the literature.

### §3.5 — Survey verdict

| Source | Peer-reviewed? | Loading on x-axis? | Tests AVE SHAPE? | Tests AVE threshold? |
|---|---|---|---|---|
| NASA Glenn (ErD₃, γ-stim) | Yes (solid anchor) | No (single operating point) | No | No (qualitative direction only) |
| Berlinguette 2019 (*Nature*) | Yes | No (loading = unreached confound) | No | No (null overall) |
| McKubre / ENEA / Storms | Mixed / disputed | No (speculation only) | No | Qualitative: "threshold near `x≈1`" |
| ARPA-E LENR (2023→) | Not yet published | Designed to, not yet | Pending | Pending |

**No published loading-resolved excess-heat / fusion-rate curve exists.** Every source either pins a single operating point (NASA Glenn), reports a loading-unreached null (Berlinguette), states a qualitative threshold-near-full-loading speculation (McKubre/ENEA), or is a not-yet-published future program (ARPA-E). The predicted curve SHAPE and the precise threshold LOCATION ($x=0.852$, $x=0.929$) cannot be confronted with data because **the data axis the prediction lives on has not been measured.**

## §4 — Outcome classification (A / B / C)

Mapping the survey onto the prereg's §5 discriminating outcomes:

- **Outcome A (chord)** — requires loading-resolved data showing the predicted shape (sharp onset near $x\sim0.85$, steep rise toward $x\sim0.93$) + the radiation-less threshold. **Not satisfied**: no loading-resolved data exists.
- **Outcome B (threshold, not shape)** — requires a measured loading threshold near the predicted `x` but a differing curve form. **Not satisfied**: the threshold claims (McKubre/ENEA "near `x≈1`") are *qualitative speculation*, not a measured threshold location, and no curve form is measured to compare against.
- **Outcome C (null / untestable)** — "no matching loading-dependence, OR the data is too disputed/noisy to discriminate ⇒ honest null; the LENR data can't test it." **This is the case.**

### **VERDICT: OUTCOME C — untestable against the present literature.**

The LENR data landscape is a mix of (i) one solid single-operating-point anchor (NASA Glenn) with no loading axis, (ii) a careful but loading-unreached null (Berlinguette), (iii) disputed qualitative threshold folklore (McKubre/ENEA), and (iv) a not-yet-published future program (ARPA-E). **None of these is a loading-resolved curve.** Per the prereg (§5 Outcome C, §7 anti-overclaim guard, §8 step 5), Outcome C is a **fully valid pre-registered result** — the discipline working as designed, not a failure to be debugged toward a rescue.

The forward prediction itself is **well-formed and sharp**: it commits to a specific monotone $S(A_0)$ shape, a radiation-less threshold at $x=0.852$, and a shatter edge at $x=0.929$, all parameter-free given $\sqrt{2\alpha}$ + the flagged `0.13`. It is **falsifiable** (prereg §6: excess-heat onset far from $x\sim0.85$, or no threshold structure, falsifies the $n_{scalar}=1/S$ coordinate-compression mechanism at the Pd-D scale). What is missing is the measurement, not the prediction.

**Honest-closure note (Rule 11)**: Outcome C is recorded as a clean result with its mechanism named (the absent data axis). No adjudication criterion was dropped to convert this to A or B; the qualitative threshold-near-full-loading folklore is explicitly *not* counted as a passed test.

## §5 — The experiment that WOULD test it (prereg §8 step 5)

A single instrument resolves Outcome C → A/B: **loading-resolved calorimetry + γ-spectroscopy across $x\in[0.80, 0.93]$.**

**Protocol**:
1. **Controlled, resolved loading sweep.** Electrochemically (or by gas-phase / ion-implantation) load a Pd (or Pd-alloy) cathode and hold it at a *sequence of stable* D/Pd ratios spanning $x\in[0.80, 0.93]$ in steps of $\Delta x \lesssim 0.01$. Loading measured in situ per-point (resistance-ratio R/R₀ or in-situ neutron/X-ray densitometry), *not* inferred or assumed. This is the hard part the field has never controlled — modern Pd-alloy or thin-film cathodes engineered against the $\sqrt{2\alpha}$ fracture limit (AVE-Fusion Ch4:43) are the enabling technology.
2. **Calorimetry per loading point.** Excess power vs `x` with ARPA-E-class ±0.5% precision. The AVE prediction: a **monotone rise** tracking $\exp(-2\eta_0(S(A_0)-1))$, with a sharp knee near $x_{onset}\approx0.805$ and steepening toward the shatter edge.
3. **γ-spectroscopy + neutron counting per loading point** (the discriminator unique to AVE). The AVE prediction is **NOT** just "more heat at higher loading" — it is a **regime change** at $x=0.852$: below it, discrete radiation channels ($\Gamma>0$, neutrons/γ) should dominate; above it, the $\Gamma\to0$ acoustic-phonon channel should make the signature shift from **discrete ejecta to lattice heat** (heat rises while hard-radiation yield *drops* relative to heat). A measured **discrete-radiation-to-heat crossover near $x=0.852$** is the chord; its absence (heat and radiation tracking together, or onset far from 0.85) is the falsifier.
4. **Shatter signature near $x=0.929$.** Approaching $x\to0.929$, expect mechanical failure (acoustic emission / resistance jumps / cracking) as $A_0\to1$ — the operational window should *close* on the high side, not keep rising. A measured upper edge near $0.929$ (window closes, not opens) is a second parameter-free check.

**Why this discriminates where the existing data cannot**: it puts loading on a *controlled, resolved* x-axis (which NASA Glenn, Berlinguette, and the classic electrolysis work all lack), and it measures the *radiation-channel composition* (γ/neutron vs heat) per loading point — the AVE-distinct $\Gamma\to0$ regime-change signature that no SM screening model predicts. The curve SHAPE + the $0.852$ crossover + the $0.929$ closure are three independent parameter-free hits.

## §6 — Flag-don't-fix items surfaced (not silently resolved)

1. **The `0.852` (exact-kernel) vs `0.90` (canonical-floor) threshold figure.** The prereg + this driver compute the $\Gamma\to0$ ($n_{scalar}=2.5$) onset at **$x=0.8517$** directly from the Ax-4 kernel. The canonical AVE-Fusion Ch4:75 states the same $n_{scalar}\ge2.5$ condition "physically demands a density floor of $x\ge0.90$", and the Topological Survival Window is quoted as $0.90\le x\le0.929$ (Ch4:77). **These are not in contradiction** — 0.8517 is the *exact* loading where $n=2.5$; 0.90 is the canonical *rounded/conservative operational floor* the survival-window prose uses (and the Phase-3 result §2.4 reproduces 0.852 exactly while §3.1 uses the $[0.85,0.92]$ band). **Surfaced, not reconciled in-place**: the driver reports the exact-kernel value; if the corpus wants a single canonical onset figure, that is a Grant/auditor framing call, not an implementer fix. I did not edit Ch4 or the survival-window prose.

2. **$n_{scalar}$ at $x=0.929$ is finite (39.6), not ∞, in the table.** Because the table samples $x=0.929$ (not $0.92930$), $A_0=0.9997<1$, so $n=39.6$. $A_0=1$ exactly at $x=0.92930=\sqrt{2\alpha}/0.13$. The `x_shatter` marker reports the exact 0.9293; the table row is the nearest sampled grid point. Flagged so the 39.6 is not misread as the shatter value.

3. **Berlinguette null vs AVE framing — kept honest.** The Berlinguette 2019 *Nature* result is a careful **null** ("no evidence the phenomenon exists"). Per `ave-evidence-framing-discipline`, this result does **NOT** claim "AVE explains away the Berlinguette null." The most that is said: the program's *documented difficulty reaching/holding $x\approx0.9$* (Pd cracking) is *qualitatively consistent* with the AVE razor-thin-window framing. That is interpretive resonance flagged as such, not a test passed and not a rescue of FP.

4. **Driver figure landed at repo-root `assets/figures/`** (where the committed corpus figures live, e.g. `chiral_dispersion_relation.png`), even though the in-dir `plot_chiral_dispersion.py` *code path* resolves to `src/assets/figures/`. I matched the committed-figure location, not the stale code path. Flagged as a pre-existing inconsistency in the vol_2 driver output-path convention (not fixed here — would touch unrelated drivers).

## §7 — Classification + anti-overclaim guards

### Class (consistency-vs-emergence v1.3): **Class B substrate-mechanism manifestation.**

This result is the same **Class B** as the Phase-3 foundation. The load-bearing $n_{scalar}=1/S(A_0)$ identification is substrate-canonical INPUT (anchored at `ponderomotive-equivalence.md:14` + AVE-Fusion Ch3+4), **not** Class-2-derived from K4 + Cosserat primitives alone. This is:

- **NOT Class 2** — no lift; the identification remains canonical input.
- **NOT an emergence-class claim** — the inputs ($\sqrt{2\alpha}$, $\alpha$, the `0.13` metallurgy) are canonical-substrate + one flagged metallurgical coefficient; the curve is a *manifestation* of the Ax-4 kernel, not an emergent CODATA-target match.
- **NOT an empirical validation of cold fusion** — Outcome C is explicitly *untestable against present data*. NASA Glenn validates a keV-scale operating point experimentally; everything else is analytical forward prediction.

### Anti-overclaim guards (prereg §7):
- **NASA Glenn** = solid peer-reviewed anchor for mechanism *direction* (kept; not overstated to "tests the curve" — it pins one point).
- **Fleischmann-Pons** = stays framed as stochastic-irreproducibility at the 2.9% sliver. **NO claim that "AVE validates FP."**
- **The `0.13` metallurgical coefficient is the one non-substrate input** — flagged in the driver header, in the curve formula, and here. The parameter-free claim is *conditional on it*.
- **Outcome C is pre-registered as legitimate**, not dodged. The discriminating experiment (§5) is fully specified.

### SM-counterfactual (`ave-discrimination-check`):
SM predicts cold fusion **impossible at any loading** (Coulomb barrier environment-invariant; Debye screening gives $\lesssim2\times$, inadequate). The AVE curve commits to a *specific* monotone $S(A_0)$ shape + a $\Gamma\to0$ radiation-channel **regime change** at $x=0.852$ + a window-closure at $x=0.929$. The $\Gamma\to0$ heat-not-γ crossover (§5 step 3) is the AVE-distinct signature no SM screening model produces.

## §8 — Skills fired (with evidence)

| Skill | Trigger | Evidence in this work |
|---|---|---|
| `ave-canonical-source` | Numerical driver | `ALPHA` (constants.py:133) + `R_I = √(2α)` (constants.py:402) imported; `0.13` is the only literal, flagged as non-substrate metallurgy in the driver header + as `PD_VOL_COEFF`. No hard-coded $\sqrt{2\alpha}$, $\alpha$, or threshold. |
| `ave-driver-script-honesty` | Forward-prediction driver | Driver header + figure footer state "FORWARD PREDICTION (NOT a fit)"; $\eta_0$ drawn as an explicit *scale family* $\{3,5,7\}$, never fitted; the parameter-free $\eta/\eta_0$ curve is the primary output. No comparison-to-target tuning. |
| `ave-evidence-framing-discipline` | LENR strength-language | NASA Glenn = solid anchor (mechanism direction, one operating point — not "tests the curve"); FP = stochastic-irreproducibility, explicit NO "AVE validates FP"; Berlinguette null kept as null. §6.3 + §7 guards. |
| `consistency-vs-emergence` v1.3 | Class tagging | §7: Class B substrate-mechanism manifestation; explicit NOT-Class-2, NOT-emergence, NOT-empirical-validation. |
| `verify-before-cite` | All file:line + quote cites | constants.py:133 (`ALPHA`), :402 (`R_I`) grep-verified; kernel-catalog Pd row line 42 verified; AVE-Fusion Ch3:51,55 + Ch4:11,25,67,72,75,77,80 grep-verified verbatim in the sibling repo; data-survey claims sourced to fetched NASA Glenn page + Nature/Science/Wikipedia/ARPA-E summaries (paywalled primaries flagged as such). |
| `ave-discrimination-check` | "AVE-distinct" framing | §7 SM-counterfactual: SM cold-fusion-impossible-at-any-loading; AVE-distinct content = the $\Gamma\to0$ radiation-channel regime change at $x=0.852$ + window closure at $0.929$. |
| `substrate-native-check` | Pre-code substrate walk | Curve built from Ax-2 TKI strain + Ax-4 kernel + $n_{scalar}=1/S$ + Op14/$\Gamma$ impedance — all canonical substrate primitives (inherited from Phase-3); real-space (volumetric strain / Gamow distance), no phasor transform; no SM/Lagrangian defaults. |
| `phase-space-coordinate-check` | Coordinate match | Prediction + (hypothetical) measurement both live in **real-space loading-ratio** coordinates (`x` on the x-axis; excess power / radiation yield as observables). No phase-space↔real-space mismatch — the curve and the §5 experiment share the `x` axis. |
| `ave-prereg` | Execute frozen prereg | Read + executed the frozen prereg; mechanism foundation (Phase-3 result) read first; corpus anchors (kernel catalog, AVE-Fusion Ch3+4) pulled before coding. |

---

## §9 — Closure summary

**Outcome C (untestable against present literature) — a valid pre-registered result.** The parameter-free forward curve $\eta(x)/\eta_0 = S(A_0)$ is computed from canonical constants ($\sqrt{2\alpha}$, $\alpha$) + the one flagged metallurgical coefficient (0.13), plotted, and its three thresholds marked: $x_{onset}=0.805$ ($n=2$), $x_{radiationless}=0.852$ ($n=2.5$, $\Gamma\to0$), $x_{shatter}=0.929$ ($A_0=1$). The data survey finds **no loading-resolved excess-heat / fusion-rate curve** anywhere in the literature — NASA Glenn pins one operating point, Berlinguette reports a loading-unreached null, McKubre/ENEA offer qualitative threshold folklore, ARPA-E is not-yet-published. The curve is well-formed and falsifiable; the data axis it lives on has not been measured. The discriminating experiment — **loading-resolved calorimetry + γ-spectroscopy across $x\in[0.80,0.93]$**, looking for the $\Gamma\to0$ discrete-radiation→heat crossover at $x=0.852$ and window-closure at $x=0.929$ — is specified in §5.

**No corpus walk-back triggered**: this result *adds* a pre-registered forward curve; it does not retract any matrix row or prior claim. The Phase-3 Class B classification is unchanged. The `0.852`-vs-`0.90` figure discrepancy (§6.1) is surfaced for Grant/auditor adjudication, not fixed in-place.
