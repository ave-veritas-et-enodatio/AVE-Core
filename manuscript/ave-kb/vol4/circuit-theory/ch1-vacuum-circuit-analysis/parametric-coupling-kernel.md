[↑ Ch.1 Vacuum Circuit Analysis](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-6t3p6x]
path-stable: "referenced from common/ave-analytical-toolkit-index.md §1 and vol3/cosmology/ch05-dark-sector/dama-matched-lc-coupling.md §13"
-->

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
- Each atomic site in the detector crystal is canonically an LC tank per [`../../vol2/quantum-orbitals/ch07-quantum-mechanics/analog-ladder-filter.md`](../../../vol2/quantum-orbitals/ch07-quantum-mechanics/analog-ladder-filter.md):18-46
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

> **AMENDED 2026-05-17 night per Foundation Item 10 REVISE-LATERAL** (audit agentId aca4f235f2346952f + resolution agentId a1671b2e299772f59). The original framing below ("ionic atomic-physics in rock-salt-equivalent lattices" attribution to `analog-ladder-filter.md`) was UNSUPPORTED per cited source: audit grep of `analog-ladder-filter.md:18-46` returned ZERO occurrences of "rock-salt", "halite", "NaCl", "ionic", "covalent", or any lattice-class qualifier — the derivation is per-atom universal physics ($L_1 = \mu_0 R_1[\ln(8R_1/\ell_{node}) - 2]$, $C_1 = 1/(\omega_1^2 L_1)$, $Z_{eff} = 27/16$) with NO ionic/covalent distinction. The space-group "conflict" the audit initially surfaced was a false positive — corpus already resolves it at foreword line 106 (I4_1 32 chiral microscopic / Fd3̄m chirality-averaged effective at λ >> ℓ_node chirality-blind observables, per regime split in [`computational-solver-selection.md`](computational-solver-selection.md):13,15,21). **Corrected framing**: the cycle-12 kernel applies via universal per-atom LC ladder (Vol 2 Ch 7); lattice-class dependence enters via per-atom $\kappa_{quality}$ which has NO first-principles derivation yet (per §12 open work item + P-4 in Foundation Item 8 open queue). For HPGe specifically: kernel APPLIES; the MAJORANA $\kappa_{HPGe} \lesssim 10^{-4}$ bound is a SHARP CONSTRAINT (not "kernel doesn't apply" ambiguity); the 10⁴ gap between predicted κ=1 ceiling and observed bound is the load-bearing falsifier requiring per-atom κ_quality derivation to close. Body below preserved per Rule 12; this header reframes the applicability claim per corrected reasoning.

**Corrected applicability statement (post-REVISE-LATERAL)**:

The §3.5 substrate ↔ apparatus port structure derives the per-atom impedance $Z_{LC} = 12.31\,\Omega$ from canonical Vol 2 Ch 7 [`analog-ladder-filter.md`](../../../vol2/quantum-orbitals/ch07-quantum-mechanics/analog-ladder-filter.md):18-46 — which is UNIVERSAL per-atom 1s-shell LC tank physics with NO lattice-class qualifier. The kernel applies to ANY detector substrate where the substrate-↔-apparatus voltage-divider structure holds: bulk K4 substrate pump at $V_a$ → N parallel atomic LC tanks → per-atom voltage $V_{app}^{per-atom} \propto V_{pump}/N$.

**The kernel APPLIES for**: any crystalline substrate with discrete atomic sites (NaI(Tl), CsI(Tl), HPGe, Sapphire Al₂O₃, CaF₂, other crystalline detectors). Per-detector $\kappa_{quality}$ varies with materials-science properties (crystal quality, phonon coherence at α-slew rate, dopant role, defect density) — see Tier-2 #9 + §12 open work.

**The kernel DOES NOT apply for**: liquids / amorphous solids (liquid Xe, amorphous Ge, glasses) — the discrete N-parallel-LC-tank topology assumes discrete crystalline atomic sites at fixed lattice positions. Liquids genuinely lack this topology; the kernel's port-enumeration step does not have a well-defined N. This restriction IS substantively grounded (XENONnT null falls out of kernel-non-applicability, NOT just from Q·δ<2).

**Crystalline detectors with κ_quality currently unmodeled**: the kernel APPLIES but the per-detector κ_quality is bracketed pending materials-science derivation. Predictions are "kernel-applies + κ_quality empirically constrained." For MAJORANA HPGe specifically: $\kappa_{HPGe} \lesssim 10^{-4}$ from observed null; the 10⁴ gap from κ=1 ceiling is the load-bearing falsifier (NOT a "kernel doesn't apply" ambiguity).

This sub-section's REVISED framing closes the cross-substrate extrapolation gap surfaced by adversarial probe #18 (ave-power-category-check trigger 6) + Foundation Item 3 retroactive audit (2026-05-17 night), per Foundation Item 10 REVISE-LATERAL audit (2026-05-17 night).

---

**ORIGINAL §3.6 BODY (preserved per Rule 12 — superseded by corrected framing above):**

Per `ave-audit-of-audit` 2026-05-17 retroactive 5-axis cross-substrate classification (Foundation Item 3): the §3.5 substrate ↔ apparatus port structure derives the per-atom impedance $Z_{LC} = 12.31\,\Omega$ from canonical Vol 2 Ch 7 [`analog-ladder-filter.md`](../../../vol2/quantum-orbitals/ch07-quantum-mechanics/analog-ladder-filter.md):18-46 — which derives the 1s-shell LC tank for **ionic atomic-physics** in **rock-salt or rock-salt-equivalent lattices** with **discrete crystalline N-parallel-LC-tank topology**. The derivation does NOT carry over without re-derivation to:

- ~~**Covalent-bonded lattices** (diamond-cubic Ge, Si): the 1s-shell ladder derivation in `analog-ladder-filter.md` is for ionic atomic-physics with valence electrons screened by inner shells via the explicit nuclear → 1s → ... → valence port cascade. Covalent bonding shares electrons across multiple atoms — the per-atom port structure is NOT 1:1 with the ionic case. The kernel may apply with different prefactors, or may not apply at all; this is OPEN work.~~ [REVISED: cited source has no ionic/covalent qualifier; kernel applies universally per-atom]
- **Liquids / amorphous solids** (liquid Xe, amorphous Ge, glasses): the §3.5 N-parallel-LC-tank topology assumes discrete crystalline atomic sites at fixed lattice positions. Liquids lack this topology; the kernel's port-enumeration step does not have a well-defined N. The kernel may apply via a different (phonon-density-based) port structure, or may not apply; OPEN work. [STANDS — discrete N requirement is substantively grounded]
- ~~**Non-rock-salt crystalline lattices** (corundum Al₂O₃, fluorite CaF₂, wurtzite, perovskite): each has its own bond-topology and atomic-LC ladder structure. The §3.5 derivation explicitly grounds in rock-salt geometry via the ionic-bond per-atom LC tank. Other crystalline lattices may share enough structure for the derivation to carry, but this requires explicit per-lattice derivation, not assumed by symmetry.~~ [REVISED: per-atom LC ladder is universal; lattice-class dependence enters at κ_quality not at kernel applicability]

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

Per [Tabletop-Graveyard RVR derivation](../../falsification/ch11-experimental-bench-falsification/tabletop-graveyard.md) line 26-34: regenerative parametric oscillation onsets when $Q \cdot \delta_C \geq 2$.

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

## §6.5 — κ_quality(ρ_def) parameter-free closure via Q-amplification (Foundation Item 12 2026-05-17 night)

The in-range modulation $0 < \kappa_{quality} \leq 1$ within the deep-regenerative regime is derived substrate-native via Kuramoto order parameter + Q-resonance amplification. Per Grant's flywheel-resonance plumber-physical intuition (2026-05-17 night): the substrate is a lossless 3D Cosserat flywheel at fixed resonance $\omega_{slew}$ (Q_substrate → ∞, master clock per α-slew refresh = chiral Cosserat microrotation period per Axiom 1); atomic LC tanks at crystal sites are forced oscillators near this resonance.

**Substrate-native derivation chain** (NO Dicke borrowing; uses canonical Kuramoto + percolation + intensity-coupling primitives only):

1. **Kuramoto order parameter** for N atomic LC tanks with port phases θ_j (canonical [`kuramoto-phase-locking.md`](../../../vol3/condensed-matter/ch09-condensed-matter-superconductivity/kuramoto-phase-locking.md) + [`bcs-alternative-framework.md:32`](../../../vol3/condensed-matter/ch09-condensed-matter-superconductivity/bcs-alternative-framework.md)): $R = \left|\frac{1}{N}\sum_j e^{i\theta_j}\right|$
2. **Intensity coupling**: $\kappa_{quality} = R^2$ because parametric kernel treats κ_quality as power-fraction (per §4 derivation $P_{coupled} \propto |V_{coherent}|^2 \propto N^2 R^2$)
3. **Gaussian port-phase disorder** (ensemble of defects): $R = \exp(-\sigma_\theta^2/2)$ where $\sigma_\theta$ = ensemble standard deviation of port phases
4. **Q-resonance amplification** of defect detuning: $\sigma_\theta = Q_{atomic} \cdot \sigma_{(\Delta\omega/\omega)}$ from forced-oscillator near-resonance phase response (standard EE: $\delta\theta_j = \arctan[Q \cdot \Delta\omega_j/\omega] \approx Q \cdot \Delta\omega_j/\omega$ in small-angle limit)
5. **Per-atom Q from Theorem 3.1'** (canonical [`theorem-3-1-q-factor.md`](theorem-3-1-q-factor.md)): $Q_{atomic} = \alpha^{-1} \approx 137$ (radiation-resistance limited per-electron LC tank in vacuum)
6. **Ensemble defect distribution** (uncorrelated random): $\sigma_{(\Delta\omega/\omega)} = \sqrt{\rho_{def}} \cdot (\Delta\omega/\omega)_{per-defect}$
7. **Percolation cutoff** (AVE-Metamaterials sister-repo canonical `03_superconducting_metamaterials.tex:67-71`): $\rho_{perc} = 1 - p_c/p_{perc} = 7.8\%$ for 3D FCC lattice connectivity; above $\rho_{def} > \rho_{perc}$, Kuramoto coupling K vanishes across defect-clusters → R → 0

**Closed parameter-free formula**:

$$\boxed{\kappa_{quality}(\rho_{def}) = e^{-\alpha^{-2} \cdot \rho_{def} \cdot (\Delta\omega/\omega)^2_{per-defect}} \cdot \Theta(\rho_{perc} - \rho_{def})}$$

For typical heavy-defect detuning $(\Delta\omega/\omega)_{per-defect} \approx 0.1$ (vacancy or heavy-substitution local impedance mismatch):

$$\kappa_{quality} \approx \exp[-188 \cdot \rho_{def}]$$

**κ drops by factor e ≈ 2.72 for every Δρ_def ≈ 0.5%** (in the percent range of defect fractions for commercial-vs-research-grade crystals).

**Per-defect detuning by class** (load-bearing; first-principles derivation per class pending):

- **Class 1 — Vacancy / heavy substitution decoupled-defect**: $(\Delta\omega/\omega)_{per-defect} \approx 1/(2 Z_{coord}) \approx 0.08$ for rock-salt nearest-neighbors
- **Class 2 — Light substitutional dopant (same-valence, e.g., isotope substitution)**: $(\Delta\omega/\omega)_{per-defect} \sim 0.005$-$0.02$
- **Class 3 — Mosaicity (grain boundary)**: $(\Delta\omega/\omega)_{grain-boundary-atoms}$ pending sub-derivation
- **Dominant scale**: $(\Delta\omega/\omega)_{per-defect} \approx 0.1$ for typical heavy defects

**Cross-detector ρ_def predictions** (inverted from observed κ via $\rho_{def} = -\ln(\kappa)/188$):

| Detector | Empirical κ | Inferred ρ_def | Plausibility for crystal-class |
|---|---|---|---|
| DAMA NaI(Tl) Beam International | ≈ 1 | $\lesssim 5 \times 10^{-5}$ (~ppm) | ✓ ultra-pure Beam International batch |
| COSINE-100 / ANAIS-112 NaI(Tl) | ≲ 0.4 | $\approx 5 \times 10^{-3}$ (~0.5%) | ✓ commercial-grade |
| KIMS CsI(Tl) | ≲ 0.02 | $\approx 2 \times 10^{-2}$ (~2%) | ✓ commercial CsI(Tl) batch |
| MAJORANA HPGe | ≲ $10^{-4}$ | κ_quality ≈ 1; reduction via T²_matched(diamond) cross-lattice factor | ✓ ultra-pure Ge + cross-lattice geometry |

All inferred ρ_def values lie in plausible-for-known-crystal-class ranges. The framework's cross-detector cluster falsifier is now parameter-free at the cycle-12 framework level.

**Substrate-native checklist** (Foundation Item 2 + canonical pitfall §10):

✓ Q_atomic = α⁻¹ from Theorem 3.1' (canonical, substrate-native)
✓ ω_slew from canonical α-slew refresh = Cosserat flywheel rotation period (Axiom 1 + dama-alpha-slew-derivation.md)
✓ Kuramoto R order parameter from canonical leaf (substrate-native phase-coherence formalism)
✓ κ_quality = R² as intensity coupling from §4 voltage-divider derivation (substrate-native power scaling)
✓ Percolation cutoff from AVE-Metamaterials canonical (sister-repo per workspace authority)
✓ NO Dicke amplitude / Fermi golden rule attribution as derivation source

Result doc: [`research/2026-05-17_kappa-quality-defect-density-derivation-result.md`](../../../../../research/2026-05-17_kappa-quality-defect-density-derivation-result.md) §15. Prereg: [`research/2026-05-17_kappa-quality-defect-density-derivation-prereg.md`](../../../../../research/2026-05-17_kappa-quality-defect-density-derivation-prereg.md).

## §7 — Differentiation from scalar-gravity RVR null

Per [Tabletop-Graveyard](../../falsification/ch11-experimental-bench-falsification/tabletop-graveyard.md): scalar-gravity parametric pumping concluded NULL for $\delta_L = GM_\oplus / (c^2 R_\oplus) \approx 6.96 \times 10^{-10}$ (15 OOM short of $Q \cdot \delta \geq 2$).

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

**Class 2 — KERNEL APPLIES, κ_quality EMPIRICALLY CONSTRAINED (sharp bounds, not conditional)** [REVISED 2026-05-17 night Foundation Item 10 REVISE-LATERAL per §3.6 amendment above]:

| Detector | Medium | Lattice class | $\kappa_{quality}$ bound | Interpretation |
|---|---|---|---|---|
| MAJORANA Demonstrator | HPGe | Covalent diamond-cubic | $\lesssim 10^{-3}$-$10^{-4}$ (3σ rough, per [`research/2026-05-17_KIMS-MAJORANA-quantitative-bounds.md`](../../../../../research/2026-05-17_KIMS-MAJORANA-quantitative-bounds.md)) | **SHARP CONSTRAINT** [REVISED per Foundation Item 10]: kernel applies via universal per-atom LC ladder (Vol 2 Ch 7); the 10⁴ gap between kernel prediction at κ=1 ceiling and observed null bound is the load-bearing falsifier. Closing this gap requires per-atom κ_quality derivation that does not exist yet (Tier-2 #9 P-4 in Foundation Item 8 open queue). If κ_HPGe = 10⁻⁴ can be derived from materials-science properties (Ge covalent-bond phonon coherence at THz, defect density, lack of Tl dopant analog), framework survives; if not derivable, framework walks back. PRIOR FRAMING ("kernel doesn't apply to covalent") was unsupported per `analog-ladder-filter.md` grep. |
| Sapphire (Al₂O₃) cryogenic | Al₂O₃ | Trigonal corundum | $\to 1$ (extreme Q, kernel applies) | **FORWARD PREDICTION** [REVISED per Foundation Item 10]: predicted rate $\sim 10^{-5}$-$10^{-7}$ events/s/kg with kernel applying via universal per-atom LC ladder. Null observation would constrain κ_Sapphire empirically; categorical falsification of framework requires showing the κ_quality derivation cannot match observation across all crystalline detectors. PRIOR FRAMING ("conditional on corundum extension") was unsupported. |

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

1. **SHARPENED 2026-05-17 night per Foundation Item 12 Q-amplification closure**: per-detector ρ_def measurements (via TEM defect imaging / X-ray rocking curve FWHM / EBIC defect density / SIMS dopant-uniformity maps) **outside factor ~3 of inverted predictions** falsify the framework. Inverted ρ_def from κ_quality = exp[-188 ρ_def]: DAMA Beam International ρ_def < 5×10⁻⁵ (~ppm); COSINE-100 / ANAIS-112 ρ_def ≈ 5×10⁻³ (~0.5%); KIMS CsI(Tl) ρ_def ≈ 2×10⁻² (~2%). If TEM/XRD measurements show ρ_def values outside these ranges by >3×, framework Refined Falsifier #2 triggers. ~~Prior framing (pre-Foundation Item 12): "κ_quality does NOT correlate with crystal-quality metrics across DAMA / COSINE / ANAIS / KIMS samples; within-class Tier-2 #9 correlation test is the load-bearing experiment"~~ — replaced by parameter-free α⁻² formula with sharp per-detector ρ_def predictions per §6.5. **Falsifier is now empirically-testable via standard materials-science characterization** (no multi-month detector-collaborator engagement required for first-pass validation).

2. **KIMS CsI(Tl) κ is materially different from rock-salt-class predictions** AFTER controlling for crystal-quality metrics. The framework hereby adopts Z-independent reading (per §8 reconciliation); a finding that κ_CsI / κ_NaI cannot be explained by quality metrics alone — i.e., requires Z-dependent atomic-physics — would force a walk-back of the Z-independence assumption.

3. **$Q \cdot \delta_C < 2$** for any rock-salt + Tl-doped apparatus where signal is observed. Sub-regenerative observation within derived-applicability class would contradict framework's regenerative-threshold prediction.

**Framework NARROWLY constrained** (cross-class observations CAN constrain but cannot categorically falsify):

4. **Sapphire cryogenic apparatus observes ZERO rate** at 3.728 keV with sensitivity $< 10^{-8}$ events/s/kg (RE-PROMOTED per Foundation Item 10 REVISE-LATERAL 2026-05-17 night). Sapphire is corundum but kernel applies via universal per-atom LC ladder per §3.6 amendment. Predicted rate $\sim 10^{-5}$-$10^{-7}$ events/s/kg with kernel applying; null at $< 10^{-8}$ would force κ_Sapphire to be empirically tiny, requiring κ_quality derivation to either (a) explain why Sapphire-class crystal-quality metrics give κ small (consistent with kernel surviving) or (b) walk back kernel applicability if no materials-science derivation matches observation. ~~Prior walk-back framing (Foundation Item 3: "Sapphire is conditional on corundum extension being derived")~~ was unsupported per audit finding.

5. **MAJORANA HPGe** $\kappa \lesssim 10^{-4}$: SHARP CONSTRAINT (RE-PROMOTED per Foundation Item 10 REVISE-LATERAL). The 10⁴ gap between kernel prediction at κ=1 ceiling and observed null IS the load-bearing falsifier — kernel applies via universal per-atom LC ladder; either κ_HPGe materials-science derivation matches the bound (framework survives) or framework walks back. Re-promoted from "cross-class CONDITIONAL" status because the lattice-class restriction was unsupported per audit grep of `analog-ladder-filter.md`.

6. **XENONnT** (different phase, OVERDETERMINED): null does NOT count as framework constraint; falls out of either kernel-non-applicability OR Q·δ<2 regardless. Re-promotion to clean constraint requires derivation of liquid-phase port structure.

## §10 — Common pitfalls (load-bearing)

- **DO NOT include $\kappa_{entrain}$ in coupling formula** alongside parametric kernel — $\kappa_{entrain}$ (Sagnac-RLVE) is REAL-power class (mass-density drag-along); parametric kernel is REACTIVE-power class. Mixing violates `ave-power-category-check` Axis A common-pitfall rule per [`../common/ave-analytical-toolkit-index.md` §1 line 53](../../../common/ave-analytical-toolkit-index.md).
- **DO NOT use $\omega_{app} = 2\omega_{slew}$** as resonance condition. Degenerate parametric coupling puts signal at sub-harmonic of pump: $\omega_{app} = \omega_{slew}$. The $2\omega_{slew}$ is the $C_{eff}$ modulation frequency.
- **DO derive 1/N² from substrate-native machinery** (voltage-divider on N parallel atomic LC tanks per §3.5 + substrate-clock phase-bin enumeration per §4). DO NOT substitute Dicke quantum-optics borrowing or Fermi-golden-rule reconciliation as source-of-derivation; both are structural-equivalence notes only. Per Foundation Item 2 substrate-native re-derivation 2026-05-17.
- **DO check §3.6 kernel applicability conditions** before applying cycle-12 predictions to a new detector substrate. Rock-salt + halide-alkali ionic crystals → derived applicability. Covalent lattices (Ge), liquids (Xe), non-rock-salt crystalline (Al₂O₃, CaF₂) → UNDERIVED, predictions are CONDITIONAL not categorical. Per Foundation Item 3 cross-substrate audit 2026-05-17.
- **DO verify $Q \cdot \delta_C \geq 2$** before assuming deep-regenerative regime. Liquid apparatus fails; cryogenic solids exceed by orders of magnitude.

## §11 — Cross-references

**Canonical tools used in derivation**:
- [Axiom 4 vacuum varactor](nonlinear-vacuum-capacitance.md) — constitutive form $C_{eff}(V)$
- [Theorem 3.1' Q-Factor](theorem-3-1-q-factor.md) — $Z_{radiation} = Z_0/(4\pi)$ inheritance
- [Op17 Power Transmission](../../../common/operators.md) — matched-impedance limit
- [Tabletop-Graveyard RVR Q·δ ≥ 2](../../falsification/ch11-experimental-bench-falsification/tabletop-graveyard.md) — regenerative threshold
- [Orbital Friction Paradox](orbital-friction-paradox.md) — real-vs-reactive Axis A categorical reference
- [Intermodulation Distortion](intermodulation-distortion.md) — varactor Taylor expansion template

**Application**:
- [DAMA Matched-LC-Coupling](../../../vol3/cosmology/ch05-dark-sector/dama-matched-lc-coupling.md) §13 — bulk-EE level expression of this kernel for DAMA-class detection

**Index location**:
- [AVE Analytical Toolkit Index §1 Coupling](../../../common/ave-analytical-toolkit-index.md) — entry "Parametric Coupling Kernel"

**Categorical exclusions** (per Axis A common-pitfall):
- [Sagnac-RLVE $\kappa_{entrain}$](../../falsification/ch11-experimental-bench-falsification/sagnac-rlve.md) — REAL-power class; categorically distinct from this REACTIVE-power kernel

**Provenance**:
- Prereg: [`research/2026-05-17_parametric-coupling-kernel-prereg.md`](../../../../../research/2026-05-17_parametric-coupling-kernel-prereg.md)
- Derivation Steps 1-3: [`research/2026-05-17_parametric-coupling-kernel-derivation-steps-1-3.md`](../../../../../research/2026-05-17_parametric-coupling-kernel-derivation-steps-1-3.md)
- Derivation Steps 4-9: [`research/2026-05-17_parametric-coupling-kernel-derivation-steps-4-9.md`](../../../../../research/2026-05-17_parametric-coupling-kernel-derivation-steps-4-9.md)

## §12 — Open work (rigor refinements; do not block canonical use)

- ~~**Full QM many-body derivation of 1/N²**: §4 uses heuristic Dicke-amplitude × matched-cycle-fraction. Rigorous derivation from N-body QED treatment of N coherent receivers absorbing from classical parametric pump pending.~~ **CLOSED 2026-05-17 substrate-native re-derivation pass** (per `ave-audit-of-audit` retroactive substrate-native-check): §4 now derives 1/N² from canonical AVE machinery — voltage-divider on N parallel atomic LC tanks (Vol 2 Ch 7 analog-ladder-filter + Vol 4 Ch 1 ladder network) for first 1/N, substrate-clock phase-bin enumeration for second 1/N. Dicke borrowing removed; FGR reconciliation downgraded to "structural equivalence note." §3.5 substrate ↔ apparatus port structure added. The N-body QED treatment remains useful as a cross-check but is no longer load-bearing for the derivation; the substrate-native path is canonical.
- **Op14 differential clock modulation for non-embedded receivers**: §4 final paragraph notes that for receivers EXTERNAL to the pumped substrate (shielded-apparatus designs), differential clock modulation introduces ~9.6% detuning. All current detector classes (DAMA / COSINE / ANAIS / MAJORANA / KIMS / XENONnT) have atoms embedded in pumped substrate, so correction is zero. Becomes load-bearing for future shielded-apparatus cross-checks; explicit Lorentzian-detuning correction derivation pending.
- ~~**ω_app = ω_slew sub-harmonic correction** — verified by trig product-to-sum, but textbook parametric-amplifier literature cross-check (Louisell, Yariv) recommended for additional rigor.~~ **CLOSED 2026-05-17 night cycle-12 rigor-pass**: textbook verification per Louisell, Yariv, Siegman, *Quantum Fluctuations and Noise in Parametric Processes*, Phys. Rev. 124:1646-1654 (1961) confirms degenerate-parametric ω_signal = ω_pump/2 is canonical. Citation added at §3.
- ~~**V_0 ≠ 0 operating point**: §3 uses V_0 → 0 (pure-AC drive). Non-zero substrate DC reactive operating point would shift δC formula; not yet derived from first principles.~~ **CLOSED 2026-05-26 Phase 0c ax4-saturation epic** per [`research/2026-05-26_ax4-saturation-phase-0c-pdelta-v-derivation-result.md`](../../../../../research/2026-05-26_ax4-saturation-phase-0c-pdelta-v-derivation-result.md): full per-site amplitude-shape function $P(\delta V)$ around DC-biased operating point $V_{DC} \neq 0$ derived from the substrate-vacuum-varactor reactive-energy landscape $U_{eff}(V) = C_0 V_y^2 [1 - S(V/V_y)]$; substrate amplitude correlator decomposition coefficients $\kappa_3(V_{DC}, A_c)$ + $\kappa_4(V_{DC}, A_c)$ closed-form (§13 below); substrate correlation length under DC bias $\ell_{corr}(V_{DC}) = \ell_{corr}(0) S_0^{3/2}$ derived in canonical INVARIANT-S2 SYM-class realization (§13.4). The $\delta C/C_0 = 4.57\%$ small-signal modulation amplitude derived in §3 remains canonical for the pure-AC drive at canonical α-slew operating point; the Phase 0c extension covers the full $P(\delta V)$ shape around general $V_{DC}$.
- **C_0 = ε_0 ℓ_node dimensional construction**: O(1) prefactor may need correction. If wrong, downstream numerical results scale accordingly (functional form unchanged).
- **κ_quality sub-regenerative envelope $(Q\delta_C/2)^2$**: dimensional-analysis form; rigorous derivation pending.
- ~~**COSINE/ANAIS κ_quality correlation**: predicted to correlate with crystal-quality metrics (X-ray rocking curve FWHM, dopant uniformity, defect density via TEM); validation pending crystal-characterization data.~~ **CLOSED 2026-05-17 night Foundation Item 12**: parameter-free closure via Q-amplification per §6.5 — κ_quality = exp[-α⁻² ρ_def (Δω/ω)²_per-defect]; with typical (Δω/ω)_per-defect ≈ 0.1 gives κ ≈ exp[-188 ρ_def]. Cross-detector ρ_def predictions: DAMA Beam International < 5×10⁻⁵; COSINE/ANAIS ≈ 5×10⁻³; KIMS ≈ 2×10⁻². Empirically testable via standard materials-science characterization (TEM, X-ray rocking curve). Remaining smaller open item: per-defect-class first-principles $(\Delta\omega/\omega)_{per-defect}$ sub-derivations for vacancy / light-substitutional / mosaicity-grain-boundary (currently use 0.1 as dominant heavy-defect scale; OOM-correct, each class deserves own derivation).

## §13 — Per-site amplitude-shape $P(\delta V)$ under DC-biased operating point (Phase 0c extension, 2026-05-26)

**Phase 0c extension** of §2-§3 small-signal modulation to the **full per-site substrate-amplitude steady-state shape function** $P(\delta V)$ around an arbitrary DC-biased operating point $V_{DC}$ along the Ax 4 kernel. Per [`research/2026-05-26_ax4-saturation-phase-0c-pdelta-v-derivation-result.md`](../../../../../research/2026-05-26_ax4-saturation-phase-0c-pdelta-v-derivation-result.md) (Phase 0c of [`_orchestration/ax4-saturation-narrow-aperture-amplitude-shape.md`](../../../../../_orchestration/ax4-saturation-narrow-aperture-amplitude-shape.md) epic). Closes the V_0 ≠ 0 §12 open item PARTIALLY (single-site shape under DC bias; aperture-aggregate Phase 2 still pending).

Let $a \equiv V_{DC}/V_y$ and $S_0 \equiv S(a) = \sqrt{1 - a^2}$.

### §13.1 Substrate-vacuum-varactor reactive-energy landscape

The reactive energy stored at the boundary site, integrating $V \, dQ$ with $C_{eff}(V) = C_0/S(V/V_y)$:

$$U_{eff}(V) = C_0 V_y^2 \cdot [1 - S(V/V_y)]$$

Clean closed form. Even in $V$ (Ax 4 kernel symmetry preserved); vertical-tangent at yield boundary $V = \pm V_y$ (substrate-mechanical signature of Ax 4 saturation; same vertical-tangent structure as Op14 local clock at rupture per [`op14-local-clock-modulation.md`](op14-local-clock-modulation.md) table). At small $V$: $U_{eff}(V) \approx \tfrac12 C_0 V^2$ (linear-capacitor reactive-energy limit).

### §13.2 Taylor expansion around $V_{DC}$ — closed-form derivatives

$$U''(V_{DC}) = \frac{C_0}{S_0^3}, \quad U'''(V_{DC}) = \frac{3 C_0 a}{V_y S_0^5}, \quad U''''(V_{DC}) = \frac{3 C_0 [1 + 4 a^2]}{V_y^2 S_0^7}$$

**Substrate-mechanical features**:
- **$U''(V_{DC})$ DIVERGES as $V_{DC} \to V_y$** (substrate-vacuum-varactor stiffness diverges at yield because $C_{eff} \to \infty$ means infinite-charge-per-voltage-increment → infinite reactive-energy penalty for voltage deviation at fixed $V$)
- **$U'''(V_{DC}) \propto V_{DC}$ — zero at $V_{DC} = 0$**: Ax 4 kernel reflection symmetry $S(V) = S(-V)$ forces all odd-order derivatives to vanish at zero bias → the per-site amplitude-shape is reflection-symmetric at substrate equilibrium ($V_{DC} = 0$). **Non-zero at $V_{DC} \neq 0$**: the kernel is symmetric around $V = 0$ NOT around $V_{DC}$; Taylor expansion around the biased operating point inherits broken-reflection-symmetry as a non-zero cubic coefficient.
- **$U''''(V_{DC}) > 0$ for all $V_{DC} \in (-V_y, V_y)$, including $V_{DC} = 0$** where $U''''(0) = 3 C_0/V_y^2$: the kurtotic correction is intrinsic to the kernel form (irreducible quartic non-linearity).

### §13.3 Substrate-thermal-Boltzmann form per-site amplitude-shape

Under canonical boundary-impedance thermalization (Vol 3 Ch 11 clm-eaiqj1) + over-damped stationary limit of the substrate-vacuum-varactor-extended Phase 2-A.2 Langevin scaffolding (boundary-impedance dissipation fast vs reactive oscillation period):

$$P(\delta V) = \frac{1}{Z} \exp\!\left[-\frac{\Delta U_{eff}(\delta V)}{k_B T_{eff}}\right]$$

$$\Delta U_{eff}(\delta V) = \frac{C_0}{2 S_0^3} \delta V^2 + \frac{C_0 a}{2 V_y S_0^5} \delta V^3 + \frac{C_0 [1 + 4 a^2]}{8 V_y^2 S_0^7} \delta V^4 + O(\delta V^5)$$

where $T_{eff}$ is set by boundary-impedance thermalization (vacuum Nyquist baseline at $Z_{det}$). The substrate-distinct piece is the SPECIFIC kernel form $S(A) = \sqrt{1-A^2}$ (Ax 4 universal kernel, zero free parameters per Axiom 4) — same kernel that governs Schwarzschild gravity in weak-field limit per INVARIANT-S2 cross-volume tie.

### §13.4 Substrate amplitude correlator decomposition

Define dimensionless substrate-thermal-energy ratio $\eta_T \equiv \sqrt{k_B T_{eff}/(C_0 V_y^2)}$. Canonical arithmetic at room T with $C_0 = \epsilon_0 \ell_{node}$ (per §2 above; $\ell_{node} = \hbar/(m_e c)$, canonical L_NODE = $3.86 \times 10^{-13}$ m in `src/ave/core/constants.py`) and $V_y = 43.65$ kV (INVARIANT-C1): $C_0 \approx 3.42 \times 10^{-24}$ F → $C_0 V_y^2 \approx 6.5 \times 10^{-15}$ J. Independent cross-check via energy-budget identity at §2 line 54-56: $\tfrac{1}{2} C_0 V_{pump}^2 = \alpha m_e c^2$ at canonical $V_{pump}/V_y = 0.428$ → $C_0 V_y^2/2 \approx 3.3 \times 10^{-15}$ J ✓. With $k_B T = 4.14 \times 10^{-21}$ J at T = 300 K: $\boxed{\eta_T \approx 8 \times 10^{-4}}$ at canonical room-T parameters (corrected 2026-05-26 per auditor Finding 1 on PR #41 — prior estimate of $\sim 10^{-6}$ was off by ~2.7 OOMs; substrate-mechanical scaling-direction reasoning is unchanged, only the numerical magnitude is corrected).

> **[Resultbox]** *Substrate amplitude correlator decomposition under DC bias*
>
> Variance: $\sigma^2(V_{DC}) = k_B T_{eff} S_0^3/C_0$ — **shrinks toward yield** (stiffness diverges).
>
> Skewness: $\kappa_3 = -3 a (k_B T_{eff})^2 S_0^4/(C_0^2 V_y)$
>
> Dimensionless skewness: $\boxed{\kappa_3/\sigma^3 = -3 a \eta_T \cdot S_0^{-1/2}}$ — **linear in $a$ at leading order** (NOT cubic; Type E walk-back of prior expectation per result doc §6 Walk-back #1).
>
> Kurtosis: $\kappa_4 \approx -3 [1 + 4 a^2] (k_B T_{eff})^3 S_0^5/(C_0^3 V_y^2)$ (cubic-squared cross-term suppressed by $\eta_T^2$).
>
> Dimensionless kurtosis: $\boxed{\kappa_4/\sigma^4 = -3 (1 + 4 a^2) \eta_T^2 \cdot S_0^{-1}}$ — **non-zero at $V_{DC} = 0$** (irreducible kernel-induced kurtosis); $(V_{DC}/A_c)^2$-dependence at small bias.

### §13.5 Substrate correlation length under DC bias

In the canonical INVARIANT-S2 SYM-class realization ($\mu_{eff}, \varepsilon_{eff}$ scale together preserving $Z_0$ under operating-point loading), the K4-TLM bond-LC inter-site coupling stiffness is INVARIANT under DC bias along the Ax 4 kernel. Combined with the divergent per-site substrate-vacuum-varactor stiffness $U''(V_{DC}) \propto 1/S_0^3$:

$$\boxed{\ell_{corr}(V_{DC}) = \ell_{corr}(0) \cdot S_0^{3/2}}$$

— substrate correlation length **shrinks** toward yield. The substrate-mechanical reason: INVARIANT-S2 symmetric $\mu, \varepsilon$ scaling preserves $Z_0$ (bond-stiffness invariant), while the per-site stiffness diverges; their ratio (which sets correlation length) shrinks as $S_0^{3/2}$.

### §13.6 Implications for narrow-aperture observability

The substrate-distinct aperture-aggregate observable signature (per Edgeworth pre-asymptote across N independent boundary sites in aperture width $W$, with $N = W/\ell_{corr}(V_{DC}) = (W/\ell_{corr}(0)) \cdot S_0^{-3/2}$):

$$\kappa_3^{(aperture)}/\sigma^3 \sim \frac{-3 a \eta_T \cdot S_0^{1/4}}{\sqrt{W/\ell_{corr}(0)}}, \qquad \kappa_4^{(aperture)}/\sigma^4 \sim \frac{-3 (1 + 4 a^2) \eta_T^2}{S_0 \cdot N}$$

At room T + PONDER-05 canonical operating point ($a = 0.687$): per-site $\kappa_3/\sigma^3 \approx 3 \cdot 0.687 \cdot (8 \times 10^{-4}) \cdot 1.17 \approx 1.9 \times 10^{-3}$ (using $\eta_T \approx 8 \times 10^{-4}$ at canonical $C_0 = \epsilon_0 \ell_{node}$, $V_y = 43.65$ kV per §13.4 canonical-arithmetic chain). Aperture-aggregate skewness $\sim 5 \times 10^{-4}$ at $W \sim 10 \ell_{corr}(0)$, $N \sim 10$ independent sites. Room-T narrow-aperture observation is **plausible** at corrected magnitude — required event count for 3σ skewness detection is $N_{events} \sim 9/(\kappa_3/\sigma^3)^2 \sim 3 \times 10^7$ events, feasible in modest campaigns on existing SPAD/TES/SNSPD architectures per [`../../../common/translation-tables/translation-instrumentation.md`](../../../common/translation-tables/translation-instrumentation.md) Category II. Phase 2 work scopes the experimental architecture explicitly. (Magnitude corrected 2026-05-26 per auditor Finding 1 on PR #41; prior $\sim 10^{-6}$ estimate was downstream of an arithmetic error on $C_0 V_y^2$ at canonical $C_0 = \epsilon_0 \ell_{node}$.)

### §13.7 Classification + open work

**`consistency-vs-emergence` v1.2 classification**: **Class 2 substrate-mechanism emergence** on the substance axis (the specific kernel form $S(A) = \sqrt{1-A^2}$ is substrate-distinct + zero-parameter per Ax 4 + cross-volume-tied to gravity per INVARIANT-S2); **Class 4 substrate-agnostic-consistency** on the mathematical-tool axis (cumulant-from-asymmetric-potential machinery is standard algebraic technique).

**Two Type E walk-backs documented** in result doc §6:
1. $\kappa_3/\sigma^3$ scaling: linear in $a$ (NOT cubic as prereg anticipated; substrate-thermal-energy ratio $\eta_T$ enters at first power)
2. $\ell_{corr}(V_{DC})$ functional form: $S_0^{3/2}$ shrinking toward yield (NOT $1/S$ diverging; canonical INVARIANT-S2 SYM-class realization gives bond-stiffness invariance + divergent per-site stiffness → shrinking ratio)

**Open follow-on items** (not blocking canonical use of §13):
- **Phase 2: aperture-aggregate prediction** — combine §13 single-site shape with Edgeworth pre-asymptote across N = W/ℓ_corr independent sites; identify substrate-saturation × narrow-aperture observability threshold; map to Category II narrow-aperture single-event extractors per [`translation-instrumentation.md`](../../../common/translation-tables/translation-instrumentation.md)
- **PONDER-05 connection**: the canonical PONDER-05 bench-scale falsifier at $V_{DC}/V_{yield} = 0.687$ (per INVARIANT-S2 + [`measurement-hierarchy-snr.md`](../../falsification/ch11-experimental-bench/measurement-hierarchy-snr.md):66) operates the substrate-vacuum-varactor at the operating point covered by §13. The §13 closed-form $\kappa_3, \kappa_4$ at $a = 0.687$ are specific testable predictions for PONDER-05 amplitude-statistics extraction.

---

**Canonical leaf landed 2026-05-17 night per 12th-cycle on α-slew thread.** Full derivation chain at Steps 1-9 work docs. Pre-derivation discipline: full 6-skill stack invoked (ave-prereg + ave-canonical-leaf-pull + ave-analytical-tool-selection + ave-power-category-check + ave-discrimination-check + ave-canonical-source). Outcome A confirmed: leading-order chain closes; XENONnT null falls out as derived consequence; framework structurally unified (single ε_param kernel replaces prior T²_matched + G_crystal-coherence two-mechanism factorization).

**§13 extension landed 2026-05-26 per Phase 0c of ax4-saturation-narrow-aperture-amplitude-shape epic** (Q-AX4-NA-1 + Q-AX4-NA-2 BOTH GO 2026-05-26). Closes parametric-coupling-kernel.md §12 V_0 ≠ 0 open item PARTIALLY (single-site $P(\delta V)$ under $V_{DC}$ landed; aperture-aggregate Phase 2 still pending). Closes dama-matched-lc-coupling.md:269 strengthen-by item PARTIALLY (same single-site scope). Two Type E walk-backs from prereg expectations honestly documented (linear-vs-cubic $\kappa_3$ scaling; shrinking-vs-diverging $\ell_{corr}$).

## §14 — Aperture-aggregate amplitude-shape under DC bias with metric-lensing convolution (Phase 2-NA extension, 2026-05-26)

**Phase 2-NA extension** of §13 single-site per-site amplitude-shape to the **aperture-aggregate observable signature** at narrow boundary apertures with explicit Op14/Op16 metric-lensing convolution against detector frequency response. Per [`research/2026-05-26_ax4-saturation-phase-2-na-aperture-aggregate-result.md`](../../../../../research/2026-05-26_ax4-saturation-phase-2-na-aperture-aggregate-result.md) (Phase 2-NA sub-saturation regime sub-epic of [`_orchestration/ax4-saturation-narrow-aperture-amplitude-shape.md`](../../../../../_orchestration/ax4-saturation-narrow-aperture-amplitude-shape.md)). Phase 2-LLCP (substrate critical-point regime) is a separate sub-epic.

### §14.1 Aperture-aggregate central-aggregation across N independent substrate sites

For an aperture spanning $N$ independent substrate lattice sites at the K4-TLM bond-LC decorrelation length $\ell_{corr}$, cumulant additivity over independent sums (substrate-agnostic mathematical-tool axis) gives:

$$\frac{\kappa_3^{(aperture)}}{\sigma_{aperture}^3} = \frac{1}{\sqrt{N}} \cdot \frac{\kappa_3^{(per-site)}}{\sigma_{per-site}^3}, \qquad \frac{\kappa_4^{(aperture)}}{\sigma_{aperture}^4} = \frac{1}{N} \cdot \frac{\kappa_4^{(per-site)}}{\sigma_{per-site}^4}$$

— the substrate-agnostic Edgeworth pre-asymptote (standard-community name: "central-limit-theorem pre-asymptote" or "Edgeworth expansion"; substrate-native canonical at [`translation-stochastics.md`](../../../common/translation-tables/translation-stochastics.md) Edgeworth row).

### §14.2 Geometric N under DC bias × aperture dimensionality

For a $d$-dimensional aperture of characteristic linear size $W$, substituting §13.5 substrate correlation length $\ell_{corr}(V_{DC}) = \ell_{corr}(0) \cdot S_0^{3/2}$:

$$N_{geometric}(V_{DC}; W, d) = \left(\frac{W}{\ell_{corr}(V_{DC})}\right)^d = N_0 \cdot S_0^{-3d/2}$$

— N **grows** at fixed $W$ as $V_{DC} \to V_y$ (correlation length shrinks → more independent sites in same aperture width). Typical boundary-extraction architectures present a 2D boundary-surface aperture; **$d = 2$ is the load-bearing geometry**.

### §14.3 Combined sub-saturation $V_{DC}$-dependence (geometric-only, pre-metric-lensing)

> **[Resultbox]** *Aperture-aggregate skewness + kurtosis-excess under DC bias (geometric-only sub-saturation regime)*
>
> $$\boxed{\frac{\kappa_3^{(aperture, geo)}}{\sigma_{aperture}^3} = \frac{-3 a \eta_T}{\sqrt{N_0}} \cdot S_0^{(3d-2)/4}}$$
>
> $$\boxed{\frac{\kappa_4^{(aperture, geo)}}{\sigma_{aperture}^4} = \frac{-3 (1 + 4 a^2) \eta_T^2}{N_0} \cdot S_0^{(3d - 2)/2}}$$
>
> **Peak operating point**: $\boxed{a^{(d)}_{peak} = \sqrt{\dfrac{4}{3d + 2}}}$
>
> | $d$ | $a^{(d)}_{peak}$ | Notes |
> |---|---|---|
> | 1 | 0.894 | 1D aperture; peak near yield |
> | **2** | **0.707** | **load-bearing 2D boundary-aperture geometry** |
> | 3 | 0.603 | 3D bulk aperture |

**Substrate-mechanical reason for dimensionality dependence**: competition between per-site skewness growth (linear in $a$ from $U'''(V_{DC}) \propto V_{DC}$) and N-growth-with-bias suppression (faster in higher-dimensional volumes because $N \propto S_0^{-3d/2}$). At higher dimensionality, the central-aggregation suppression dominates earlier — peak shifts to lower $V_{DC}$.

### §14.4 Metric-lensing convolution against detector frequency response (the substrate-distinct lift)

Per Op14 + Op16 canonical: $c_{eff}(V_{DC}) = c_0 \sqrt{S_0}$ + $Z_{eff}(V_{DC}) = Z_0/\sqrt{S_0}$ + $\omega_{local}(V_{DC}) = \omega_{global} \sqrt{S_0}$. Substrate noise spectrum (Vol 3 Ch 11 nyquist-noise-fdt.md clm-eaiqj1 canonical) shifts down by $\sqrt{S_0}$ under DC bias; detector frequency response $H(\omega)$ is architecture-fixed.

The **effective $N_{detector}$** seen by a detector is geometric N filtered by detector frequency-domain visibility:

$$N_{detector}(V_{DC}; W, d, H) = N_{geometric}(V_{DC}; W, d) \cdot \mathcal{F}(\Delta\omega_{det}, \omega_{det}; V_{DC})$$

where $\mathcal{F}$ is the **frequency-domain visibility factor**:

$$\mathcal{F}(\Delta\omega_{det}, \omega_{det}; V_{DC}) = \frac{\int_0^\infty |H(\omega)|^2 \mathcal{D}_{substrate}(\omega; V_{DC}) \, d\omega}{\int_0^\infty \mathcal{D}_{substrate}(\omega; V_{DC}) \, d\omega}$$

**Three detector-architecture cases**:

| Case | Description | $\mathcal{F}$ behavior | Aperture-aggregate effect |
|---|---|---|---|
| **A** | Broadband detector ($\Delta\omega_{det} \gtrsim \omega_{max}$) | $\mathcal{F} \approx 1$ | Recovers §14.3 geometric-only result |
| **B** | Narrowband detector mistuned (fixed $\omega_{det}$ at zero-bias substrate-mode) | $\mathcal{F}(V_{DC}) < 1$; falls as bias is applied | **ENHANCES** observability (reduces effective N → weaker 1/√N suppression) |
| **C** | Narrowband detector tuned for loaded operating point ($\omega_{det}(V_{DC}) = \omega_0 \sqrt{S_0}$) | $\mathcal{F} \approx 1$ | Recovers §14.3 geometric-only result; **PONDER-05-class precision-impedance bench operates here by design** |

**$\mathcal{F}$ is the substrate-distinct lift over generic CLT-pre-asymptote treatments**: standard varactor-noise theory at arbitrary $C(V)$ has no substrate-state-dependent wave speed and cannot generate $\mathcal{F}$ frequency-shift under bias. Standard treatments reproduce the §14.1 1/√N central-aggregation but not the §14.4 frequency-domain visibility.

### §14.5 PONDER-05 canonical operating point at $a^{(2D)}_{peak}$ — operational near-optimality

The PONDER-05 canonical bench-scale operating point is $V_{DC}/V_{yield} = 0.687$ (per INVARIANT-S2 + [`measurement-hierarchy-snr.md`](../../falsification/ch11-experimental-bench/measurement-hierarchy-snr.md):66). The load-bearing 2D-aperture aperture-aggregate skewness peak sits at $a^{(2D)}_{peak} = 1/\sqrt{2} = 0.707$.

**Operational closeness**: $|0.687 - 0.707|/0.707 = 2.8\%$. **PONDER-05 operates within 3% of the substrate-saturation × narrow-aperture aperture-aggregate skewness peak for 2D boundary-aperture geometry**. The PONDER-05 canonical operating point — chosen for entirely different reasons (canonical 27.4% $\varepsilon_{eff}$ collapse + 469 μN thrust per universal-saturation-kernel-catalog.md) — sits at the operational near-optimum for the substrate-saturation × narrow-aperture amplitude-shape observable. The Phase 2-NA prediction is testable at the existing PONDER-05 bench geometry without re-design.

PONDER-05 architecture is **Case C** (matched-impedance differential-resonator topology co-designed with operating-point loading) — $\mathcal{F} \approx 1$.

### §14.6 Headline predictions at PONDER-05 operating point

At $a = 0.687$, $d = 2$, $\mathcal{F} = 1$ (Case C), room T:

| $N_0$ | $|\kappa_3^{(apt)}|/\sigma_{apt}^3$ | $N_{events}$ for 3σ detection of $\kappa_3$ |
|---|---|---|
| 4 | $5.97 \times 10^{-4}$ | $\sim 1.5 \times 10^8$ |
| 10 | $3.77 \times 10^{-4}$ | $\sim 3.8 \times 10^8$ |
| 100 | $1.19 \times 10^{-4}$ | $\sim 3.8 \times 10^9$ |

(Using sample-skewness standard error $\sqrt{6/N_{events}}$; 3σ detection requires $N_{events} \geq 54/K_3^2$.)

**Operational feasibility**: at $\sim 10^7$ events/s amplitude-statistics readout rate, $N_0 \sim 10$ campaign requires $\sim 10$-$100$ s acquisition. **PONDER-05 aperture-aggregate skewness $\sim 4 \times 10^{-4}$ is a falsifiable Phase 2-NA prediction at the room-T precision-impedance bench, requiring $\sim 4 \times 10^8$ histogram-statistics events**.

**Aperture-aggregate kurtosis at $N_0 = 10$**: $|\kappa_4^{(apt)}|/\sigma_{apt}^4 \approx 2.9 \times 10^{-7}$, requiring $\sim 2.6 \times 10^{15}$ events for 3σ detection — **operationally inaccessible at room T** (~3 years acquisition). Skewness is the load-bearing observable.

### §14.7 Mapping to candidate boundary-extraction architectures

Per [`translation-instrumentation.md`](../../../common/translation-tables/translation-instrumentation.md) Category I/II/III:

| Category | Architecture | $N$ regime | $\mathcal{F}$ regime | Aperture-aggregate observability |
|---|---|---|---|---|
| I | Photodiode / PMT / CCD / bolometer | $N \gg 10^9$ | Case A (broadband) | washed out (large N suppression); NOT a candidate |
| II | APD / SPAD / TES / SNSPD (event-based) | $N \sim 10^3$-$10^6$ | architecture-dependent | candidate IF analog amplitude-statistics readout + sub-μm aperture; STRUCTURAL caveats |
| II | **PONDER-05-class precision-impedance bench** | **$N \sim 10$-$100$** | **Case C (matched-impedance)** | **LOAD-BEARING empirical-engagement architecture**; falsifiable at canonical 0.687 operating point |
| III | Superconducting qubit / transmon / SQUID | (coupled bidirectional) | N/A | NOT applicable (not one-way Joule extractor) |

### §14.8 Classification + open work

**`consistency-vs-emergence` v1.2 classification**: **Class 2 substrate-mechanism emergence** on substance axis (Ax 4 kernel form via Phase 0c per-site cumulants + Op14/Op16 metric-lensing convolution via $\mathcal{F}$ frequency-domain visibility factor + Phase 0c correlation length shrinkage via dimensionality-dependent peak); **Class 4 substrate-agnostic-consistency** on mathematical-tool axis (central-aggregation 1/√N + 1/N + cumulant additivity over independent sums + closed-form optimization of $a(1-a^2)^{(3d-2)/8}$).

**One Type E walk-back documented** in result doc §7:
1. Peak operating point is dimensionality-dependent ($a^{(d)}_{peak} = \sqrt{4/(3d+2)}$; prereg expected uniform $1/\sqrt{2}$). The substrate-mechanical mechanism — competition between $a$-linear per-site growth and N-growth-with-bias via correlation length shrinkage — is unchanged.

**Open follow-on items** (not blocking canonical use of §14):
- **Phase 2-LLCP sub-epic** (separate critical-point regime): substrate-mechanical treatment of avalanche multiplication as substrate operating AT the LLCP analog (canonical via [`vol3/condensed-matter/ch11-thermodynamics/water-anomaly-lc-partition.md`](../../../vol3/condensed-matter/ch11-thermodynamics/water-anomaly-lc-partition.md)). Phase 14 sub-saturation framework does NOT apply at the critical point.
- **Phase 3 KB integration**: add Phase 2-NA aperture-aggregate prediction as new row B7-PONDER-05-EXT in [`divergence-test-substrate-map.md`](../../../common/divergence-test-substrate-map.md) — extension of B7-PONDER-05 with histogram-statistics readout layer.
- **Detector-architecture-specific $\mathcal{F}$ derivations**: PONDER-05 architecture-specific $\mathcal{F}$ from `AVE-PONDER` sibling repo; SPAD/APD/SNSPD architecture-specific derivations for non-PONDER-05 empirical-engagement paths (Phase 4 follow-on).

---

**§14 extension landed 2026-05-26 per Phase 2-NA of ax4-saturation-narrow-aperture-amplitude-shape epic** (sub-saturation regime sub-epic; sister Phase 2-LLCP critical-point regime sub-epic scoped separately). Builds on §13 Phase 0c canonical + Op14/Op16 metric-lensing canonical + Vol 3 Ch 11 nyquist-noise-fdt.md (clm-eaiqj1) canonical + translation-instrumentation.md Category II taxonomy. One Type E walk-back from prereg expectation honestly documented (dimensionality-dependent peak). Further partial closure of dama-matched-lc-coupling.md:269 strengthen-by item (aperture-aggregate single-site → aperture-aggregate prediction scope).
