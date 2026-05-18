# Pre-Registration: Substrate-Native Derivation of Hulse-Taylor PSR B1913+16 Periastron Advance

**Date pre-registered**: 2026-05-17 night
**Pre-registered by**: agent + Grant directive ("derive the perihelion 3 coefficient from K4-Cosserat substrate independent of GR")
**Status**: PRE-REGISTERED (this doc lands BEFORE any derivation work)

## Discipline stack invoked

Per session-encoded discipline (Foundation Items 1-4 establish "solid foundation before next physics"):

1. **ave-prereg** (THIS DOC): pre-register predictions before deriving
2. **ave-canonical-leaf-pull**: pull canonical substrate-native gravity machinery (corpus-grep completed 2026-05-17 night — see "Corpus state" section below)
3. **ave-analytical-tool-selection**: identify analytical classes (Class 5 Power + Class 7 Boundary + Class 10 Topology + Class 11 Cosserat-mechanics + Class 6 Mode for orbital dynamics)
4. **ave-power-category-check**: classify regime (REACTIVE / BOUND / OFF-SHELL / INTERNAL-TANK / SUBSTRATE-MODE — same axes as cycle-12 §3.5 with gravity-specific adjustments)
5. **substrate-native-check trigger 6** (prose-derivation construction of operator-equivalent — added by probe #15 + Foundation Item 2): walk 7 checkpoints BEFORE writing derivation
6. **consistency-vs-emergence** classification: pre-register which 4-class category the result will fall into
7. **ave-canonical-source**: any code/script must import canonical constants

## Physical picture (Step 1.5 ave-prereg — mechanical/topological, no equations)

- **Setup**: Hulse-Taylor PSR B1913+16 binary. Two neutron stars, masses $M_1 = 1.44 \, M_\odot$ + $M_2 = 1.39 \, M_\odot$, orbital period $P_b = 7.7515$ hours, semi-major axis $a = 1.95 \times 10^9$ m, eccentricity $e = 0.617$
- **Substrate environment**: each NS is a massive object embedded in K4-Cosserat substrate. Substrate strain $\varepsilon_{11}(r) = 7GM/c^2r$ at distance $r$ from each NS (per Vol 3 Ch 1 canonical derivation)
- **Operating regime at orbital position**: at $r = a$, $\phi/c^2 = G(M_1+M_2)/c^2 a \approx 2.16 \times 10^{-6}$. Substrate strain $\varepsilon_{11}^{orbital} \approx 7 \times 2.16 \times 10^{-6} = 1.5 \times 10^{-5}$. $A^2 = (\varepsilon_{11})^2 \approx 2.3 \times 10^{-10}$. **DEEPLY LINEAR REGIME** per Grant's "GR = linear regime" framing. Op14 saturation parameter is essentially zero at orbital position
- **What's happening physically**: each NS moves through the other's substrate strain field. The strain transmits gravitational interaction via substrate impedance-gradient mechanism (Vol 3 Ch 1 optical-refraction-gravity). Orbit is in linear Hooke's-law regime. Cosserat-rotational coupling provides frame-dragging contribution (canonical Vol 3 Ch 3 frame-dragging-impedance-convolution). Higher-order Op14 corrections at orbital position are $O(\varepsilon_{11}^4) \sim 10^{-20}$ relative to leading order — observationally inaccessible
- **What's being measured**: rate of advance of periastron (rotation of orbital ellipse's argument of pericenter) per orbital period. GR PPN-1 formula: $\dot{\omega}_{GR} = 6\pi G(M_1+M_2)/c^2 a(1-e^2) \cdot 1/P_b$. Measured value: $\dot{\omega}_{measured} = 4.226595(5) \, °/\text{yr}$ — precision ~1 part in $10^6$. GR prediction matches to better than 0.1%.

**What the substrate-native derivation must produce**: a coefficient in front of the $1/r^3$ correction to V_tidal that, when integrated around the binary orbit, gives the periastron-advance rate. The "3 coefficient" in $V_{tidal}(r) = -(GM/r)(1 + 3GM/c^2r)$ is the PPN-1 Schwarzschild-metric structural quantity. Substrate-native derivation must derive this coefficient independently from K4-Cosserat axioms, NOT borrow from GR.

## Corpus state (from corpus-grep 2026-05-17 night, agentId afe8966a1f678cdbd)

**Substrate-native gravity machinery already in corpus** (relevant subset):
- $G = \hbar c / (7\xi m_e^2)$ — substrate-derived gravitational coupling
- $\nu_{vac} = 2/7$ — substrate Poisson ratio from $K = 2G$ trace-reversal + Feng-Thorpe-Garboczi EMT verification
- $\varepsilon_{11}(r) = 7GM/c^2 r$ — substrate strain (Vol 3 Ch 1 + 3)
- $n(r) = 1 + (2/7) \cdot \varepsilon_{11}(r) = 1 + 2GM/c^2 r$ — refractive index after ν_vac reduction
- Gordon optical-metric isomorphism: $g_{\mu\nu}^{AVE} = \eta_{\mu\nu} + (1 - 1/n^2) u_\mu u_\nu$
- Op14 saturation $\omega_{local} = \omega_{global}\sqrt{1-A^2}$ — local clock modulation
- Frame-dragging as classical macroscopic mutual inductance (Vol 3 Ch 2)
- Cosserat ω-field rotational DOF (canonical Axiom 1 per CLAUDE.md S2)
- WD second-order redshift 12.25× larger than PPN second-order — the $(7/2)^2 = 49/4$ amplification at next order

**Open gaps confirmed by corpus-grep**:
- PSR B1913+16 has ZERO hits in AVE-KB
- S-stars near Sgr A* has ZERO hits in AVE-KB
- Mercury "3" coefficient borrowed from GR PPN per Foundation Item 4 walk-back
- Cosserat ω engine implementation deferred (Master Equation FDTD lacks Cosserat layer)

**The 12.25 amplification factor**: load-bearing AVE-distinct emergence claim at PPN-2 (second-order redshift). At PPN-1 (first-order periastron advance), Gordon isomorphism suggests EXACT GR recovery — but this needs substrate-native derivation to confirm, not just assert.

## Pre-registered prediction (substrate-native expected outcome)

**Primary prediction (most likely, $\sim 70\%$ confidence)**: substrate-native derivation produces $V_{tidal}^{AVE}(r) = -(GM/r)(1 + 3GM/c^2 r) + O((GM/c^2r)^2)$ — IDENTICAL "3" coefficient to GR Schwarzschild. Periastron advance rate from integration:

$$\dot{\omega}_{AVE} = \frac{6\pi G(M_1+M_2)}{c^2 a(1-e^2)} \cdot \frac{1}{P_b}$$

**Substrate-native prediction at Hulse-Taylor parameters**: $\dot{\omega}_{AVE} = 4.226 \, °/\text{yr}$, matching measured value to within calculation precision.

**Reasoning for primary prediction**: Gordon optical-metric isomorphism at PPN-1 is structurally exact in the weak-field limit. The "3" coefficient is geometric — it emerges from the metric signature + radial-vs-tangential decomposition of the orbit. Substrate-native derivation that produces $n(r) = 1 + 2GM/c^2 r$ exactly (which it does — Vol 3 Ch 3 canonical) inherits the same PPN-1 structure. The (7/2)² = 12.25 amplification kicks in at PPN-2, which for Hulse-Taylor at $\phi/c^2 \sim 10^{-6}$ contributes $\sim 12.25 \times 10^{-6}$ relative to PPN-1 contribution — below the ~10⁻⁴ measurement precision.

**Alternative prediction (~20% confidence)**: substrate-native derivation produces a DIFFERENT "3" coefficient — e.g., from a Cosserat-rotational coupling term not present in Schwarzschild metric. If substrate gives "3'" ≠ 3, the periastron rate scales linearly:

$$\dot{\omega}_{AVE} = (3'/3) \cdot \dot{\omega}_{GR}$$

For this to be observable at Hulse-Taylor precision, $|3'/3 - 1| > 10^{-4}$.

**Reasoning for alternative**: GR's Schwarzschild metric treats spacetime curvature directly; AVE's K4-Cosserat substrate has explicit rotational DOF (Cosserat ω-field) that contributes to angular-momentum transport in ways not captured by Schwarzschild. The MOND $a_0$ derivation via Hoop Stress shows substrate-native gravity has terms GR doesn't have at long range; binary pulsar regime is intermediate but Cosserat-coupling effects could in principle contribute additional terms at $O(1/r^3)$.

**Null prediction (~10% confidence)**: substrate-native derivation cannot be completed without invoking GR's Schwarzschild metric as input — the corpus's substrate-native machinery is INSUFFICIENT for the two-body weak-field PPN-1 problem.

**Reasoning for null**: Cosserat-rotational coupling beyond frame-dragging is engine-deferred per `breathing-soliton-v14-mode-i.md:108`. The corpus's gravity-sector machinery may not extend to N-body weak-field problems without additional substrate-native derivations that don't yet exist. If the corpus tools genuinely run out, the discipline forces explicit acknowledgement of the gap rather than smuggling GR back in.

## Discriminating outcomes

| Outcome | Predicted | Measured comparison | Framework consequence |
|---|---|---|---|
| **A. Substrate "3" coefficient = 3 exactly** | $\dot{\omega}_{AVE} = 4.226$ °/yr | matches measured to ~10⁻⁴ | Consistency-check at PPN-1 confirmed at DEEPER level (substrate-native, not GR-borrowed). Framework's PPN-1 weak-field gravity emergence claim permanently retired. Emergence claims confined to PPN-2 (12.25× WD redshift) + saturation (BH ringdown 1.7%) + trans-Planckian (GRB dispersion). |
| **B. Substrate "3'" ≠ 3 by $> 10^{-4}$** | $\dot{\omega}_{AVE}$ deviates from 4.226 °/yr by $> 0.0004$ °/yr | INCONSISTENT with measured 4.226595 ± 0.000005 °/yr | Framework PPN-1 prediction FALSIFIED at Hulse-Taylor precision. Either AVE wrong, or derivation has substrate-native gap. Walk-back required. |
| **B'. Substrate "3'" ≠ 3 by $< 10^{-4}$** | $\dot{\omega}_{AVE}$ deviates from 4.226 °/yr by $< 0.0004$ °/yr | within Hulse-Taylor precision but observably different from GR at higher precision (e.g., J0737-3039 at ~10⁻⁵ precision) | Framework PPN-1 prediction makes AVE-distinct testable claim at J0737-3039 precision; promote to forward-prediction surface. |
| **C. Substrate derivation runs out without GR input** | N/A — no derivation completes | N/A | Substrate-native gravity has a derivation gap. Open work item: derive additional Cosserat-coupling machinery to close the gap. |

## Falsifier

If substrate-native derivation produces $V_{tidal}^{AVE}(r)$ that gives $\dot{\omega}_{AVE}$ inconsistent with measured $4.226595(5)$ °/yr by more than $5\sigma$ (i.e., $> 2.5 \times 10^{-5}$ °/yr deviation), the framework's PPN-1 weak-field gravity claim is FALSIFIED at Hulse-Taylor.

## What this test would resolve (epistemic stakes)

This test resolves the load-bearing question Foundation Item 4 left open: **does the substrate's gravitational sector reproduce GR exactly at PPN-1 via Gordon isomorphism, or does it diverge at PPN-1 by some Cosserat-rotational coupling term?**

If Outcome A: framework's gravitational emergence is permanently scoped to PPN-2 + saturation + trans-Planckian regimes. Weak-field PPN-1 is consistency-check (already retired in Foundation Item 4); now confirmed at deeper level. Framework's predictive surface is narrower-but-cleaner.

If Outcome B/B': framework gets a NEW AVE-distinct PPN-1 prediction at the highest-precision GR-test regime we have measurement of (50 years of Hulse-Taylor + double-pulsar timing). Major emergence claim.

If Outcome C: framework's gravity sector has a structural derivation gap that the corpus has been masking by borrowing GR. Multi-session theoretical work to close.

All three outcomes are valuable. The test is genuinely discriminating.

## Why this test now

Per session-state: foundation work (Items 1-4) just narrowed the framework's claimed predictive surface; Foundation Item 4 explicitly identified the "Mercury 3 coefficient from substrate" as the open gap. Hulse-Taylor is the binary-pulsar generalization of the Mercury question, at much higher measurement precision (10⁻⁶ vs 10⁻³). Same physics class; better empirical surface. Pre-registered prediction + substrate-native derivation closes Foundation Item 4 open gap with a 50-year empirical test rather than a 2-century one.

## Open question pre-registered to Grant

Q: Cosserat ω-field engine implementation is deferred per `breathing-soliton-v14-mode-i.md:108` (Master Equation FDTD lacks Cosserat layer). If substrate-native derivation requires explicit Cosserat-coupling beyond the frame-dragging mutual-inductance map, does the derivation proceed analytically (prose-LaTeX) using canonical Vol 3 Ch 2 frame-dragging machinery, OR does it require engine work first?

Default plan: proceed analytically with canonical Vol 3 frame-dragging + Op14 + Gordon isomorphism + ν_vac = 2/7 machinery. If derivation gap surfaces at a Cosserat-coupling step that needs engine work, surface to Grant before proceeding.

---

**Next step**: execute substrate-native derivation per the discipline stack. Will produce result doc at `research/2026-05-17_hulse-taylor-substrate-native-derivation-result.md` with the actual computation.

**Pre-registration LOCKED 2026-05-17 night**.
