# FT-Cold-Fusion η(x) Prereg — Parameter-free Pd-D fusion-rate-vs-loading curve

**Date**: 2026-05-31
**Branch**: `analysis/forward-pred-darkwake-coldfusion-preregs`
**Status**: PREREG-FROZEN (pre-derivation).
**Lineage**: lifts the just-closed Phase-3 cold-fusion consistency result ([`2026-05-31_Q-EMBED-SEL-1_step_c_phase3_cold_fusion_result.md`](2026-05-31_Q-EMBED-SEL-1_step_c_phase3_cold_fusion_result.md), Class B, 5/5 PASS) from "consistent with NASA Glenn" to a pre-registered **parameter-free forward curve**.

## §0 — TL;DR

The Phase-3 substrate-mechanism already DERIVES — but frames as consistency rather than pre-registering as a forward prediction:
$$\eta(x) = \eta_0\sqrt{1 - \left(\tfrac{0.13\,x}{\sqrt{2\alpha}}\right)^2}, \qquad P_{fusion}(x) = e^{-2\eta(x)},$$
with a radiation-less ($\Gamma\to 0$) threshold at $x \ge 0.852$ and a razor-thin operational window at $x \approx 0.929 = \sqrt{2\alpha}/0.13$ (the substrate shatter point).

**Target:** pre-register the curve SHAPE + threshold LOCATION as a parameter-free forward prediction (parameter-free given the canonical $\sqrt{2\alpha}$ and the metallurgical $0.13$), and test it against loading-resolved excess-heat / fusion-rate data. SM predicts cold fusion impossible at any loading; AVE predicts a specific $\eta(x)$ curve with a sharp onset.

## §1 — Derivation target

Produce the explicit, plotted $P_{fusion}(x)$ curve and its key parameter-free features:
- the loading $x_{onset}$ where the Gamow-exponent reduction becomes significant,
- the radiation-less threshold $x \ge 0.852$ ($n_{scalar}\ge 2.5$, $\Gamma\to 0$),
- the shatter / operational-window edge $x \approx 0.929$,

and identify which features are parameter-free (shape + threshold) vs which carry the $\eta_0$ + screening uncertainty (absolute rate).

## §2 — Physical picture (mechanical)

1. Macroscopic Pd-D loading $x$ → volumetric strain $\Delta V/V \approx 0.13x$ (metallurgical) → substrate scalar strain $A_0(x) = 0.13x/\sqrt{2\alpha}$ via Ax-2 TKI.
2. Ax-4 kernel $S(A_0)=\sqrt{1-A_0^2}$ → local refractive index $n_{scalar} = 1/S(A_0)$.
3. Coordinate compression **narrows the Gamow tunneling distance (NOT the barrier height):** $\eta(x) = \eta_0\,S(A_0)$. Tunneling $P=e^{-2\eta}$ exponentially enhanced as $n$ rises.
4. At $n_{scalar}\ge 2.5$ ($x \ge 0.852$): $\Gamma\to 0$ impedance match → acoustic-phonon regime → **heat, not $\gamma$** (the "missing radiation" of FP).
5. At $x \approx 0.929$: $A_0=1$, Ax-4 yield (shatter); the operational window is the 2.9% sliver below.

## §3 — Corpus state

- **Phase-3 result (2026-05-31):** the mechanism + all formulas, validated 5/5 at order-of-magnitude. $\eta(x)$, the $x\ge 0.852$ threshold, and $x\approx 0.929$ are all DERIVED there but framed "consistency," not pre-registered forward curve. **Class B** ($n_{scalar}=1/S$ is canonical input, not Class-2-derived from K4+Cosserat primitives).
- **Canonical anchors:** $\sqrt{2\alpha}$ shatter point + $R_I=\sqrt{2\alpha}$ ([`constants.py`](../src/ave/core/constants.py), symbol `R_I`); the $0.13$ metallurgical coefficient (Fusion vol Ch4:67, standard Pd hydrogen-loading scaling — **the one non-substrate input; flagged**).
- **Empirical landscape:** NASA Glenn (~keV, ~$10^2$ reduction) is the one solid peer-reviewed anchor (Steinetz et al., NASA TM-2020-5001734); Fleischmann-Pons is empirically disputed. Corpus framing: FP = stochastic-irreproducibility at the 2.9% sliver, NOT "AVE validates FP."

## §4 — Parameter-free content (dimensional analysis)

- The curve **SHAPE** $\eta(x)/\eta_0 = \sqrt{1-(0.13x/\sqrt{2\alpha})^2}$ is parameter-free given canonical $\sqrt{2\alpha}$ + metallurgical $0.13$.
- The radiation-less **threshold** $x=0.852$ ($n=2.5$) and shatter $x=0.929$ are parameter-free.
- $\eta_0$ (vacuum Gamow exponent) sets the ABSOLUTE rate but NOT the shape/threshold. The absolute rate also carries environmental-screening uncertainty (result §6.3).
- ⇒ **the parameter-free DISCRIMINATORS are the curve SHAPE + the threshold LOCATION, not the absolute rate.** Pre-register on shape + threshold.

## §5 — Discriminating outcomes

- **Outcome A (chord):** loading-resolved data shows the predicted shape (sharp onset near $x\sim 0.85$, steep rise toward $x\sim 0.93$) + the radiation-less (heat-not-$\gamma$) threshold. ⇒ AVE predicts a curve+threshold nobody else does (SM: impossible at any $x$). Novel + falsifiable.
- **Outcome B (threshold, not shape):** a loading threshold exists near the predicted $x$ but the curve form differs ⇒ mechanism direction right, quantitative form needs refinement.
- **Outcome C (null / untestable):** no matching loading-dependence, OR the data is too disputed/noisy to discriminate ⇒ honest null; the LENR data can't test it.

## §6 — Falsifier

If well-resolved loading data shows excess-heat onset at a loading far from $x\sim 0.85$, or no threshold structure at all, the $n_{scalar}=1/S$ coordinate-compression mechanism is falsified at the Pd-D scale.

## §7 — Anti-overclaim guards

- Class-B substrate-mechanism manifestation, NOT a Class-2 lift and NOT an empirical validation of cold fusion (`consistency-vs-emergence` + `ave-evidence-framing-discipline`).
- NASA Glenn is the solid anchor; FP stays framed as stochastic-irreproducibility (2.9% sliver), NOT "AVE validates FP."
- The data landscape is disputed; **Outcome C (untestable) is a live and honest possibility** — pre-register it as a legitimate result, not a failure to avoid.
- The $0.13$ metallurgical coefficient is the one non-substrate input — flag it; the parameter-free claim is conditional on it.

## §8 — Recommended execution (post-prereg)

Implementor: (1) compute + plot $P_{fusion}(x)$ with canonical constants ($\sqrt{2\alpha}$, $\alpha$); (2) mark $x_{onset}$, $x=0.852$ ($\Gamma\to 0$), $x=0.929$ (shatter); (3) survey for loading-resolved excess-heat data (NASA Glenn TM follow-ups, Google 2019 *Nature* program, any loading-vs-heat tables); (4) classify A/B/C; (5) if loading-resolved data is absent, record Outcome C honestly + **specify the experiment that WOULD test it** (loading-resolved calorimetry + $\gamma$-spectroscopy across $x\in[0.8,0.93]$).

## §9 — Cross-references

- [`2026-05-31_Q-EMBED-SEL-1_step_c_phase3_cold_fusion_result.md`](2026-05-31_Q-EMBED-SEL-1_step_c_phase3_cold_fusion_result.md) — Phase-3 substrate-mechanism + the η(x) / threshold / window formulas, 5/5 multi-falsifier PASS
- [`universal-saturation-kernel-catalog.md`](../manuscript/ave-kb/common/universal-saturation-kernel-catalog.md) — Pd hydrogen-loading row
- `AVE-Fusion/manuscript/vol_fusion/chapters/03_metric_catalyzed_fusion.tex` + Ch 4 — canonical Gamow-compression + survival-window (sibling repo)
- [`constants.py`](../src/ave/core/constants.py) — `R_I = √(2α)` shatter constant
