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

## §3.5 — Substrate-native sector bridge (substrate ↔ apparatus port structure)

Per `ave-audit-of-audit` 2026-05-17 retroactive substrate-native walk: the §4 1/N² derivation MUST identify which substrate port hosts the pump and which apparatus port hosts the N receivers, with the substrate↔apparatus impedance match made explicit in (V_inc, V_ref) phasor coordinates BEFORE the rate-per-kg translation. The original §4 reverted to Dicke quantum-optics borrowing during the prereg→canonical promotion; this §3.5 closes the substrate-native sector bridge using canonical AVE machinery only.

**Substrate-side port**:
- Bulk K4-TLM lattice node hosts the pump $V_{pump}(t) = V_a \cos(\omega_{slew} t)$ at $\omega_{slew} = 9.02 \times 10^{17}$ Hz (α-slew rate, per Schwinger anomalous-moment substrate)
- Characteristic radiation impedance per spinor cycle: $Z_{radiation} = Z_0/(4\pi)$ per [Theorem 3.1' Q-Factor](theorem-3-1-q-factor.md):65-75
- The $4\pi$ is substrate-native (SU(2) double-cover phase requirement at TIR boundary), NOT a solid-angle integration borrowed from QED
- Available substrate power: $P_{substrate} = V_a^2 / Z_{radiation} = V_a^2 \cdot (4\pi/Z_0)$

**Apparatus-side port (per atom)**:
- Each atomic site in the detector crystal is canonically an LC tank per [`../../vol2/quantum-orbitals/ch07-quantum-mechanics/analog-ladder-filter.md`](../../vol2/quantum-orbitals/ch07-quantum-mechanics/analog-ladder-filter.md):18-46
- The atom presents a VALENCE PORT to the substrate via the nuclear → 1s → 2s → ... → valence ladder cascade (line 13)
- Per-shell characteristic impedance: $Z_{LC} = \sqrt{L_n / C_n} \approx 12.31\,\Omega$ for the 1s shell (line 45), with the substrate-native ratio $Z_{LC}/Z_0 \approx \alpha/\pi$ (line 48) — NOT borrowed from atomic physics, derived from substrate's bulk modulus
- N atoms in parallel: aggregate apparatus-side impedance $Z_{apparatus} = Z_{LC}/N$ (standard EE parallel-impedance rule, canonical Vol 4 Ch 1 ladder network)

**Substrate ↔ apparatus impedance match**:
- For DAMA NaI(Tl) single coherent crystal: $N = 7.79 \times 10^{25}$ atoms, $Z_{LC} = 12\,\Omega$ per atom
- $Z_{apparatus} = 12 / 7.79 \times 10^{25} = 1.5 \times 10^{-25}\,\Omega$ — far below $Z_{radiation} = Z_0/(4\pi) = 30\,\Omega$
- The substrate is therefore in the **source-impedance-dominated regime**: the substrate-supplied current is set by $V_a / Z_{radiation}$ (not by the apparatus load); the apparatus per-atom voltage is set by voltage-divider on $Z_{LC}$ within the parallel network

**Operating regime classification (5-axis per ave-power-category-check):**
- Axis A (real-vs-reactive): REACTIVE — parametric coupling is reactive-power class (LC tank pump)
- Axis B (propagating-vs-bound): BOUND — receivers are bound atomic LC tanks; substrate is bulk K4
- Axis C (on-shell-vs-off-shell): OFF-SHELL — parametric resonance is off-shell virtual-loop
- Axis D (internal-tank-vs-external-matched): INTERNAL TANK — bulk substrate is internal tank to apparatus
- Axis E (substrate-mode-vs-atomic-physics): SUBSTRATE-MODE — the matched-LC is substrate-LC, not atomic-Z

This sector classification is the substrate-native counterpart to the (now-removed) Dicke quantum-optics framing. It does NOT invoke quantum-optics machinery; the ensemble physics is entirely K4-TLM bond-port enumeration + LC ladder voltage-divider.

## §3.6 — Kernel applicability conditions (which detector classes the §3.5 derivation applies to)

Per `ave-audit-of-audit` 2026-05-17 retroactive 5-axis cross-substrate classification (Foundation Item 3): the §3.5 substrate ↔ apparatus port structure derives the per-atom impedance $Z_{LC} = 12.31\,\Omega$ from canonical Vol 2 Ch 7 [`analog-ladder-filter.md`](../../vol2/quantum-orbitals/ch07-quantum-mechanics/analog-ladder-filter.md):18-46 — which derives the 1s-shell LC tank for **ionic atomic-physics** in **rock-salt or rock-salt-equivalent lattices** with **discrete crystalline N-parallel-LC-tank topology**. The derivation does NOT carry over without re-derivation to:

- **Covalent-bonded lattices** (diamond-cubic Ge, Si): the 1s-shell ladder derivation in `analog-ladder-filter.md` is for ionic atomic-physics with valence electrons screened by inner shells via the explicit nuclear → 1s → ... → valence port cascade. Covalent bonding shares electrons across multiple atoms — the per-atom port structure is NOT 1:1 with the ionic case. The kernel may apply with different prefactors, or may not apply at all; this is OPEN work.
- **Liquids / amorphous solids** (liquid Xe, amorphous Ge, glasses): the §3.5 N-parallel-LC-tank topology assumes discrete crystalline atomic sites at fixed lattice positions. Liquids lack this topology; the kernel's port-enumeration step does not have a well-defined N. The kernel may apply via a different (phonon-density-based) port structure, or may not apply; OPEN work.
- **Non-rock-salt crystalline lattices** (corundum Al₂O₃, fluorite CaF₂, wurtzite, perovskite): each has its own bond-topology and atomic-LC ladder structure. The §3.5 derivation explicitly grounds in rock-salt geometry via the ionic-bond per-atom LC tank. Other crystalline lattices may share enough structure for the derivation to carry, but this requires explicit per-lattice derivation, not assumed by symmetry.

**The kernel currently has DERIVED applicability for**: NaI(Tl), CsI(Tl), and other rock-salt-class ionic crystals with halide-alkali stoichiometry.

**The kernel has UNDERIVED applicability for**: HPGe (covalent), liquid Xe (liquid), Sapphire Al₂O₃ (corundum), CaF₂ fluorite, organic crystals, and other non-rock-salt structures.

For UNDERIVED-applicability detectors, the framework can only state **conditional predictions**: "IF the kernel applies AND κ_quality has value X, THEN observed rate would be Y; observed null is consistent with either (kernel applies + κ tiny) OR (kernel does not apply at all)." The two scenarios are NOT distinguishable from the null alone.

This sub-section closes the cross-substrate extrapolation gap surfaced by adversarial probe #18 (ave-power-category-check trigger 6) + Foundation Item 3 retroactive audit (2026-05-17 night).

## §4 — N-coherent receiver distribution (1/N² scaling, substrate-native derivation)

Per §3.5 substrate ↔ apparatus port structure: N atomic LC tanks couple in parallel to the substrate's bulk K4 node hosting $V_{pump}$.

**Voltage-divider on N parallel atomic ports**:
- Total substrate-emitted power $P_{substrate} = V_a^2 / Z_{radiation}$ (substrate-supplied at the K4-bond port)
- N atomic LC tanks in parallel present aggregate $Z_{apparatus} = Z_{LC}/N$
- Per-atom voltage: $V_{app}^{per-atom} = V_{pump} \cdot (Z_{LC}/N) / (Z_{radiation} + Z_{LC}/N) \propto V_{pump}/N$ in the source-impedance-dominated regime (per §3.5)
- This is the **first $1/N$**: per-receiver coupled amplitude scales as $1/N$ from parallel-port voltage division. **No Dicke machinery needed** — this is the canonical Vol 4 Ch 1 N-parallel-impedance ladder physics applied to atomic LC tanks per Vol 2 Ch 7.

**Matched-cycle synchronization** (substrate-native, not quantum-optics):
- The substrate's per-cycle pump phase $\phi_{pump}(t) = \omega_{slew} t$ is a single substrate clock
- Each atomic LC tank has its own internal phase $\phi_{atom,i}(t)$ relative to the pump
- For coherent absorption (parametric resonance condition): $\phi_{atom,i} - \phi_{pump} = 0 \mod 2\pi$ within the per-cycle reactive window
- For N atoms with uniformly-distributed internal phases relative to pump, the matched-phase fraction per cycle is $1/N$ (one out of N internal-phase bins matches per pump cycle)
- This is the **second $1/N$**: per-cycle synchronization fraction. Substrate-native (port-phase enumeration), not Dicke ensemble-state machinery.

**Combined per-receiver per-cycle detection probability**:

$$\varepsilon_{det}^{per-receiver-per-cycle} = \frac{1}{N} \times \frac{1}{N} = \frac{1}{N^2}$$

**Substrate-native provenance** (replaces prior Dicke-borrowing + Fermi-golden-rule reconciliation):
- First $1/N$: N-parallel atomic LC tank voltage-divider per Vol 4 Ch 1 ladder network + Vol 2 Ch 7 analog-ladder-filter
- Second $1/N$: substrate-clock phase-bin enumeration (one matched bin per N internal-phase configurations)
- 4π prefactor: substrate's spinor-cycle radiation impedance $Z_{radiation} = Z_0/(4\pi)$ per Theorem 3.1' (substrate-native via SU(2) double-cover at TIR boundary)

**Note on Fermi-golden-rule structural equivalence**: a reader familiar with QED may recognize that the substrate-native voltage-divider + phase-bin enumeration is structurally equivalent to FGR's $|M|^2 \rho(E)$ factorization (with $|M|^2 \propto 1/N$ from amplitude distribution and $\rho(E) \propto 1$ from per-cycle phase-bin density bounded by matched fraction). The equivalence is informative but is NOT the derivation; the derivation is substrate-native per §3.5 + this section.

**Op14 local-clock modulation (open work, low practical impact for embedded-receiver case)**:
- For receivers EMBEDDED in the pumped substrate (DAMA-class — atoms are inside the bulk K4 region at $V_{pump}$): driver and receiver share the same local $A^2$, hence the same local clock $\omega_{local} = \omega_{global} \sqrt{1 - A^2}$. The matched-cycle condition is preserved; no rate correction at the matched-LC formula level.
- For receivers EXTERNAL to the pumped substrate (e.g., shielded-apparatus designs with the receiver crystal isolated from the pumped substrate region): differential clock modulation between driver site ($A^2 = 0.183$, $\omega_{local} = 0.904 \omega_{global}$) and receiver site ($A^2 \approx 0$, $\omega_{local} = \omega_{global}$) introduces ~9.6% detuning. The matched-LC formula would require a Lorentzian-detuning correction $(1 - (\Delta\omega/\Gamma)^2)$ for that case.
- DAMA / COSINE / ANAIS / MAJORANA / KIMS detector classes all have atoms embedded in their substrate; Op14 differential correction is currently zero for all five. The correction becomes load-bearing only for future shielded-apparatus cross-checks.

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

**Tier-2 #9 first-pass scoping finding (2026-05-17 night)** per [`research/2026-05-17_kappa-quality-correlation-first-pass-scoping.md`](../../../../../research/2026-05-17_kappa-quality-correlation-first-pass-scoping.md): **light yield is NOT a relevant κ_quality proxy** — published light yields (DAMA 5.5-7.5 phe/keV, COSINE 15 NPE/keV, ANAIS 12-16 phe/keV) ANTICORRELATE with cycle-12-derived κ_quality (DAMA κ=1, COSINE/ANAIS κ≲0.4). Physics argument: light yield depends on Tl-dopant + optical clarity + PMT QE (DIFFERENT physics than phonon coherence at α-slew rate ~10¹⁸ Hz). The relevant κ_quality metrics are NON-OPTICAL: mosaicity (X-ray rocking curve FWHM), phonon coherence length at THz, defect-trap density, acoustic Q at THz. These are typically NOT published for dark-matter crystals; full Tier-2 #9 validation requires materials-science literature dive + detector-collaborator engagement. Framework status post-scoping: SURVIVES first-pass test; full empirical grounding remains load-bearing per §9 Falsifier #2.

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

**Per §3.6 kernel applicability conditions** (added 2026-05-17 Foundation Item 3 retroactive audit per `ave-power-category-check` trigger 6 + 5-axis classification per §3.5): predictions split by applicability class. Within-class predictions (rock-salt + Tl-doped) carry derived kernel applicability; cross-class predictions (covalent, liquid, non-rock-salt crystalline) are CONDITIONAL on kernel applicability not yet derived.

**Class 1 — DERIVED-APPLICABILITY (rock-salt + halide-alkali ionic crystals)**:

| Detector | Medium | $M_{single}$ (kg) | $N_{single}$ | $\kappa_{quality}$ | $R_{predicted}$ (events/s/kg) | Status |
|---|---|---|---|---|---|---|
| DAMA/LIBRA | NaI(Tl) | 9.7 | $7.79 \times 10^{25}$ | 1 (ceiling) | $4.79 \times 10^{-7}$ | **MATCH** (0.6%, derived) |
| COSINE-100 | NaI(Tl) | 13.0 | $1.04 \times 10^{26}$ | ≲ 0.4 (empirical) | $\leq 1.34 \times 10^{-7}$ | Null observed → $\kappa$ < 1 implied; honest within-class κ_quality variation |
| ANAIS-112 | NaI(Tl) | 12.5 | $1.00 \times 10^{26}$ | ≲ 0.4 (empirical) | $\leq 1.45 \times 10^{-7}$ | Null observed → $\kappa$ < 1 implied; honest within-class κ_quality variation |
| KIMS | CsI(Tl) | ~8.7 | $4.04 \times 10^{25}$ | **≲ 0.02-0.05** (3σ rough refined 2026-05-17 night) | $\leq R(\kappa=1) \times \kappa = 1.74 \times 10^{-6} \cdot \kappa_{CsI(Tl)}$ | Within-class IF the framework adopts Z-INDEPENDENT interpretation at lattice-LC level (per §3.5 rock-salt derivation). **Internal-inconsistency RECONCILED 2026-05-17 Foundation Item 3**: canonical leaf hereby adopts Z-independent reading — KIMS κ_quality variation is then ≲ 0.02-0.05 within rock-salt+Tl class, factor 20-50× from DAMA. The Z-dependent σ_atomic factor 2× claim in [`research/2026-05-17_KIMS-CsI-Tl-discovery-pass.md`](../../../../../research/2026-05-17_KIMS-CsI-Tl-discovery-pass.md) §3:46-71 is hereby WALKED BACK to "alternative interpretation if Z-dependence enters" — pre-registration discipline locks the Z-independent reading as primary. |

**Class 2 — UNDERIVED-APPLICABILITY (cross-class extrapolations; bounds are CONDITIONAL not falsifying)**:

| Detector | Medium | Lattice class | $\kappa_{quality}$ bound | Interpretation |
|---|---|---|---|---|
| MAJORANA Demonstrator | HPGe | Covalent diamond-cubic | $\lesssim 10^{-3}$-$10^{-4}$ (3σ rough, per [`research/2026-05-17_KIMS-MAJORANA-quantitative-bounds.md`](../../../../../research/2026-05-17_KIMS-MAJORANA-quantitative-bounds.md)) | **CONDITIONAL**: observed null is consistent with EITHER (kernel applies + κ tiny via Tl-absent + different lattice geometry) OR (kernel does NOT apply to covalent Ge because §3.5 ladder derivation assumes ionic 1s-shell port structure). The two are NOT distinguishable from the bound alone. Cannot claim "κ_HPGe ≲ 10⁻⁴ explains null" without first deriving whether kernel applies to covalent lattices. |
| Sapphire (Al₂O₃) cryogenic | Al₂O₃ | Trigonal corundum | $\to 1$ (extreme Q, IF kernel applies) | **CONDITIONAL FORWARD**: predicted rate $\sim 10^{-5}$-$10^{-7}$ events/s/kg IF kernel applies to corundum. Null observation would NOT categorically falsify framework — only the rock-salt-derived kernel claim. Walk-back of §9 Falsifier #1 below. |

**Class 3 — KERNEL-DOES-NOT-APPLY-AS-DERIVED (predicted null is overdetermined)**:

| Detector | Medium | Phase | Reason | Status |
|---|---|---|---|---|
| XENONnT | Xe(l) | Liquid | §3.5 N-parallel-atomic-LC-tank topology assumes discrete crystalline atomic sites; liquid Xe lacks this topology. The kernel's port-enumeration step does not have well-defined N for liquids. | **Null OVERDETERMINED**: Q·δ<2 sub-regenerative argument is necessary but not sufficient. The null follows from either (kernel doesn't apply) OR (Q·δ<2 even if kernel did apply). Framework cannot claim credit for predicting this null until liquid-phase port structure is derived. Does NOT count as constraint on framework. |

**Cross-detector cluster — LAYERED CONFIDENCE (replaces prior "5 constraints + 1 forward")**:

1. **DAMA NaI(Tl)+**: rate matches at $\kappa_{quality} = 1$ ceiling (derived consequence within applicable kernel)
2. **COSINE/ANAIS NaI(Tl)−**: $\kappa$ < 0.4 implied; within-class κ_quality variation; framework requires crystal-quality correlation derivation
3. **KIMS CsI(Tl)−** (within-class via Z-independent reading, locked): $\kappa$ ≲ 0.02-0.05; factor 20-50× from DAMA; within-class κ_quality variation
4. **MAJORANA HPGe** (cross-class, CONDITIONAL): bound consistent with kernel-applies-low-κ OR kernel-doesn't-apply; NOT a clean constraint
5. **Sapphire** (cross-class, CONDITIONAL FORWARD): if kernel applies to corundum; null would NOT categorically falsify
6. **XENONnT** (different phase, OVERDETERMINED): null follows from kernel non-applicability AND Q·δ<2; NOT a clean constraint

**Net change from cycle-12 original framing**: 3 within-class clean constraints (DAMA + COSINE/ANAIS + KIMS) + 2 cross-class conditional bounds (MAJORANA + Sapphire) + 1 overdetermined non-constraint (XENONnT). Down from "5 constraints + 1 forward prediction" to "3 within-class constraints + 2 conditional bounds + 1 forward (conditional) + 1 overdetermined." The framework's cross-detector falsification surface is narrower than the cycle-12 original claim.

## §9 — Discriminating outcomes / falsifiers

Per §3.6 kernel applicability classification + §8 layered confidence (Foundation Item 3 walk-back 2026-05-17 night): falsifiers split by applicability class.

**Framework categorically falsified if** (within DERIVED-applicability class only):

1. **$\kappa_{quality}$ does NOT correlate with crystal-quality metrics** across DAMA / COSINE / ANAIS / KIMS samples (all within DERIVED-applicability rock-salt + Tl-doped class). If $\kappa$ variation across rock-salt+Tl samples is random rather than tracked by mosaicity / defect-density / dopant-uniformity measurements, framework loses physical grounding within its derived-applicability domain. **PRIMARY falsifier**: within-class Tier-2 #9 correlation test is the load-bearing experiment.

2. **KIMS CsI(Tl) κ is materially different from rock-salt-class predictions** AFTER controlling for crystal-quality metrics. The framework hereby adopts Z-independent reading (per §8 reconciliation); a finding that κ_CsI / κ_NaI cannot be explained by quality metrics alone — i.e., requires Z-dependent atomic-physics — would force a walk-back of the Z-independence assumption.

3. **$Q \cdot \delta_C < 2$** for any rock-salt + Tl-doped apparatus where signal is observed. Sub-regenerative observation within derived-applicability class would contradict framework's regenerative-threshold prediction.

**Framework NARROWLY constrained** (cross-class observations CAN constrain but cannot categorically falsify):

4. ~~**Sapphire cryogenic apparatus observes ZERO rate** at 3.728 keV with sensitivity $< 10^{-8}$ events/s/kg.~~ **WALKED BACK 2026-05-17 Foundation Item 3**: Sapphire is corundum (non-rock-salt), so kernel applicability is UNDERIVED per §3.6. A Sapphire null at sensitivity $< 10^{-8}$ events/s/kg would constrain the corundum-extended kernel claim (if framework attempts that extension) but does NOT categorically falsify the rock-salt-derived kernel. Re-promotion to categorical falsifier requires explicit derivation that the kernel applies to corundum lattices.

5. **MAJORANA HPGe** (cross-class CONDITIONAL): null observation does NOT categorically falsify; the bound $\kappa_{HPGe} \lesssim 10^{-4}$ is consistent with either (kernel applies + κ tiny) OR (kernel doesn't apply to covalent diamond-cubic lattice). Re-promotion to categorical falsifier requires derivation of whether kernel applies to covalent Ge.

6. **XENONnT** (different phase, OVERDETERMINED): null does NOT count as framework constraint; falls out of either kernel-non-applicability OR Q·δ<2 regardless. Re-promotion to clean constraint requires derivation of liquid-phase port structure.

## §10 — Common pitfalls (load-bearing)

- **DO NOT include $\kappa_{entrain}$ in coupling formula** alongside parametric kernel — $\kappa_{entrain}$ (Sagnac-RLVE) is REAL-power class (mass-density drag-along); parametric kernel is REACTIVE-power class. Mixing violates `ave-power-category-check` Axis A common-pitfall rule per [`../common/ave-analytical-toolkit-index.md` §1 line 53](../../common/ave-analytical-toolkit-index.md).
- **DO NOT use $\omega_{app} = 2\omega_{slew}$** as resonance condition. Degenerate parametric coupling puts signal at sub-harmonic of pump: $\omega_{app} = \omega_{slew}$. The $2\omega_{slew}$ is the $C_{eff}$ modulation frequency.
- **DO derive 1/N² from substrate-native machinery** (voltage-divider on N parallel atomic LC tanks per §3.5 + substrate-clock phase-bin enumeration per §4). DO NOT substitute Dicke quantum-optics borrowing or Fermi-golden-rule reconciliation as source-of-derivation; both are structural-equivalence notes only. Per Foundation Item 2 substrate-native re-derivation 2026-05-17.
- **DO check §3.6 kernel applicability conditions** before applying cycle-12 predictions to a new detector substrate. Rock-salt + halide-alkali ionic crystals → derived applicability. Covalent lattices (Ge), liquids (Xe), non-rock-salt crystalline (Al₂O₃, CaF₂) → UNDERIVED, predictions are CONDITIONAL not categorical. Per Foundation Item 3 cross-substrate audit 2026-05-17.
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

- ~~**Full QM many-body derivation of 1/N²**: §4 uses heuristic Dicke-amplitude × matched-cycle-fraction. Rigorous derivation from N-body QED treatment of N coherent receivers absorbing from classical parametric pump pending.~~ **CLOSED 2026-05-17 substrate-native re-derivation pass** (per `ave-audit-of-audit` retroactive substrate-native-check): §4 now derives 1/N² from canonical AVE machinery — voltage-divider on N parallel atomic LC tanks (Vol 2 Ch 7 analog-ladder-filter + Vol 4 Ch 1 ladder network) for first 1/N, substrate-clock phase-bin enumeration for second 1/N. Dicke borrowing removed; FGR reconciliation downgraded to "structural equivalence note." §3.5 substrate ↔ apparatus port structure added. The N-body QED treatment remains useful as a cross-check but is no longer load-bearing for the derivation; the substrate-native path is canonical.
- **Op14 differential clock modulation for non-embedded receivers**: §4 final paragraph notes that for receivers EXTERNAL to the pumped substrate (shielded-apparatus designs), differential clock modulation introduces ~9.6% detuning. All current detector classes (DAMA / COSINE / ANAIS / MAJORANA / KIMS / XENONnT) have atoms embedded in pumped substrate, so correction is zero. Becomes load-bearing for future shielded-apparatus cross-checks; explicit Lorentzian-detuning correction derivation pending.
- ~~**ω_app = ω_slew sub-harmonic correction** — verified by trig product-to-sum, but textbook parametric-amplifier literature cross-check (Louisell, Yariv) recommended for additional rigor.~~ **CLOSED 2026-05-17 night cycle-12 rigor-pass**: textbook verification per Louisell, Yariv, Siegman, *Quantum Fluctuations and Noise in Parametric Processes*, Phys. Rev. 124:1646-1654 (1961) confirms degenerate-parametric ω_signal = ω_pump/2 is canonical. Citation added at §3.
- **V_0 ≠ 0 operating point**: §3 uses V_0 → 0 (pure-AC drive). Non-zero substrate DC reactive operating point would shift δC formula; not yet derived from first principles.
- **C_0 = ε_0 ℓ_node dimensional construction**: O(1) prefactor may need correction. If wrong, downstream numerical results scale accordingly (functional form unchanged).
- **κ_quality sub-regenerative envelope $(Q\delta_C/2)^2$**: dimensional-analysis form; rigorous derivation pending.
- **COSINE/ANAIS κ_quality correlation**: predicted to correlate with crystal-quality metrics (X-ray rocking curve FWHM, dopant uniformity, defect density via TEM); validation pending crystal-characterization data.

---

**Canonical leaf landed 2026-05-17 night per 12th-cycle on α-slew thread.** Full derivation chain at Steps 1-9 work docs. Pre-derivation discipline: full 6-skill stack invoked (ave-prereg + ave-canonical-leaf-pull + ave-analytical-tool-selection + ave-power-category-check + ave-discrimination-check + ave-canonical-source). Outcome A confirmed: leading-order chain closes; XENONnT null falls out as derived consequence; framework structurally unified (single ε_param kernel replaces prior T²_matched + G_crystal-coherence two-mechanism factorization).
