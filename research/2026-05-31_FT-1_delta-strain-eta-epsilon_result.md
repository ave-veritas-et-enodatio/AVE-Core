[↑ Research](index.md)

# FT-1 Result (Q-DELTA-MAP-1-quant) — OUTCOME C: E-mode Bose-Einstein occupation UNDERSHOOTS η_ε by ~31 OOM; the Cosserat-thermal mechanism does NOT supply the magnitude

**Branch**: `analysis/ft-1-delta-strain-eta-epsilon` (off `main` @ 93823898)
**Prereg**: [`2026-05-31_FT-1_delta-strain-eta-epsilon_prereg.md`](2026-05-31_FT-1_delta-strain-eta-epsilon_prereg.md) (FROZEN)
**Driver**: [`src/scripts/vol_3_macroscopic/ft1_delta_strain_eta_epsilon_driver.py`](../src/scripts/vol_3_macroscopic/ft1_delta_strain_eta_epsilon_driver.py)
**Date**: 2026-05-31
**Outcome**: **C (honest NEGATIVE)** — the most likely result per the prereg diagnostic, and a valid, valuable finding. δ_strain stays a fitted scalar; clm-009nkt confidence STAYS at its current value; clm-hp7nlm stays Class B (mechanism identified, magnitude NOT derived).

**Skills fired**: `substrate-native-check` (E/B bipartite Debye spectrum, phase-vs-real-space discipline); `pre-test-physics-check` (the BE-vs-equipartition direction question — see §2); `ave-canonical-source` (all primitives from `constants.py`, no round numbers); `ave-discrimination-check` (SM-counterfactual — §5, MANDATORY per prereg); `consistency-vs-emergence` (classification — §6); `verify-before-cite` (load-bearing citations re-grepped at execution); `ave-evidence-framing-discipline` (anti-tuning honesty bar — §7).

---

## §1 — Executive summary (the one-line chain + the verdict)

**One-line chain**: gapless E-mode Debye spectrum (ω_E = c_E|k|, c_E = c₀, ℏω_D ≈ 3.9·m_e c² ≈ 1.6 MeV, Θ_Debye ≈ 2.3×10¹⁰ K) → substrate-Bose-Einstein occupation at T_CMB (deeply quantum: x_D = ℏω_D/k_B T_CMB ≈ 8.5×10⁹, only k_th/k_D ~ 1.5×10⁻¹⁰ of the Brillouin zone populated → Debye-T⁴ energy density) → Ax-4 ε-coupling (η_ε ≈ ½⟨(A_th/A_yield)²⟩) → **η_ε ≈ 2×10⁻³⁷, which is ~31 OOM below the 4.45×10⁻⁶ target.**

**The dispositive finding** (this is the whole result): **Bose-Einstein occupation does NOT supply amplification over the ½kT equipartition foil — it SUPPRESSES by ~28.5 OOM.** The prereg's PASS condition was "BE-occupation of the gapless E-spectrum supplies the amplification the naive ½kT equipartition lacked." That hypothesis is **falsified by the physics of the Debye integral itself**: at T ≪ Θ_Debye, BE occupation gives the Debye-T⁴ (radiation-like) energy density, which is far *below* the Dulong-Petit-T¹ (classical equipartition) value, never above it. BE occupation equals equipartition at ℏω ≪ kT (Rayleigh-Jeans) and falls exponentially below it at ℏω ≳ kT — it has no regime where it exceeds equipartition. Since equipartition itself already undershot by ~2.7 OOM (reproducing the Phase 3-A3 P2/P3 diagnostic), and BE is 28.5 OOM below equipartition, the BE chain undershoots by ~31 OOM. There is no first-principles amplification.

**Numbers (driver, all from canonical primitives; target enters at the final compare ONLY):**

| Quantity | Value | OOM gap vs 4.45×10⁻⁶ |
|---|---|---|
| η_ε target (back-substituted; compare-only) | 4.447×10⁻⁶ | — |
| η_ε **forward (Bose-Einstein)** | 2.2×10⁻³⁸ … 2.6×10⁻³⁷ | **≈ 31.2 undershoot** |
| η_ε classical-equipartition FOIL | 6.9×10⁻¹⁰ … 8.1×10⁻⁹ | ≈ 2.7 undershoot |
| BE below classical foil | — | **28.5 (suppression, not amplification)** |

**SM-counterfactual verdict (§5)**: the η_ε *scale* is **generic-thermal, NOT AVE-distinct**. The BE occupation arithmetic is framework-neutral (any Debye solid at T ≪ Θ_D gives T⁴); the only AVE-distinct content (the E/B mode-shape asymmetry) sets the *direction/sign* of the modulation (ε softens, μ frozen) but not the *magnitude*, and the magnitude is the entire FT-1 question. The 28.5-OOM suppression would be predicted by ANY framework with a ~MeV-scale Debye cutoff and a 2.7 K bath.

---

## §2 — Pre-registered prediction (anti-tuning firewall)

Per prereg §6.3, the predicted η_ε from the independent chain is registered HERE, **before** the compare to 4.45×10⁻⁶:

> **Pre-registered forward prediction (before compare):** The substrate E-mode spectrum has a Debye cutoff at ℏω_D ≈ π·m_e c² ≈ 1.6 MeV (the lattice pitch ℓ_node sets k_D; c_E = c₀). At T_CMB the dimensionless ratio x_D = ℏω_D/k_B T_CMB ≈ 8.5×10⁹ places the substrate **deeply** in the quantum (frozen) regime, T_CMB/Θ_Debye ≈ 1.2×10⁻¹⁰. In that regime the Bose-Einstein thermal energy density follows the **Debye-T⁴ law** (the standard low-T phonon result), which is suppressed below the classical-equipartition (Dulong-Petit-T¹) value by a factor ~(T/Θ_Debye)³ × O(1) ~ 10⁻²⁹. Since the equipartition strain-fraction itself is ~10⁻⁹ (reproducing Phase 3-A3 P2/P3), the BE strain-fraction is ~10⁻³⁸, and η_ε = ½⟨(A_th/A_yield)²⟩ ~ 10⁻³⁸–10⁻³⁷. **Predicted OOM gap vs 4.45×10⁻⁶: ≈ 31 undershoot → OUTCOME C.**

The target 4.447×10⁻⁶ is computed in the driver as `2*C.DELTA_STRAIN` and is **read by exactly one function**, `step_iv_compare_and_adjudicate`, the final compare. No forward-chain function (`step_i`, `step_ii`, `step_iii`) reads it, reads `DELTA_STRAIN`, or reads the CODATA `ALPHA`. The forward chain uses only `{L_NODE, C_0, M_E, HBAR, K_B, G_VAC, RHO_BULK, E_YIELD_KINETIC, ALPHA_COLD}` — all topological / cold-lattice inputs (see §7 guard audit). The prediction above was fixed by the physics of the Debye integral before the compare; the compare confirmed it.

## §3 — The derivation chain (steps i–iv)

### (i) E-mode dispersion ω_E(k) = c_E|k| from substrate primitives

The gapless E-mode (translational, 3 acoustic branches per node) has transverse wave speed c_E = √(G_vac/ρ_bulk) = **c₀** — this is canonical: `constants.py` defines `G_VAC = RHO_BULK * C_0**2` (photons propagate at c on the LC lattice). No CODATA-α enters: both G_vac and ρ_bulk are built from (ℓ_node, m_e, c) topological inputs. The Brillouin-zone Debye cutoff is fixed **self-consistently** by the mode count (3 E-DOF per node, 1 node per ℓ_node³):

- k_D = (6π²n)^{1/3}, n = 1/ℓ_node³ → k_D ≈ 1.01×10¹³ m⁻¹ (= 1.24·π/ℓ_node)
- ω_D = c_E·k_D ≈ 3.03×10²¹ rad/s
- **ℏω_D ≈ 3.19×10⁻¹³ J ≈ 3.90·m_e c² ≈ 1.6 MeV**; Θ_Debye = ℏω_D/k_B ≈ **2.31×10¹⁰ K**

(The Debye closure — not the simple-cubic BZ edge k_max = π/ℓ — is the physically correct cutoff for a DOS integral; the driver's `n_dof_per_cell_check = 3.000000` verifies the normalization. Using k_max instead changes ω_D by 24% and is immaterial to the outcome, since the populated band ω ≪ ω_D is cutoff-insensitive.)

Note Θ_Debye ≈ 2.3×10¹⁰ K is the **same ~10¹⁰ K scale** the canonical leaf (`delta-strain-cosmic-tcc.md:101,142`) calls the "substrate-Curie temperature" at which B-modes thermally activate — consistent.

### (ii) Substrate-Bose-Einstein occupation ⟨A_E²⟩ at T_CMB (THE BUILD)

Thermal energy density over the 3-branch Debye DOS g(ω) = 3ω²/(2π²c_E³), ω ∈ [0, ω_D], occupation n_BE(ω) = 1/(e^{ℏω/k_BT} − 1):

$$u_{BE} = \int_0^{\omega_D} g(\omega)\, \hbar\omega\, n_{BE}(\omega)\, d\omega = 6.26\times10^{-14}\ \mathrm{J/m^3}$$

The numerical integral matches the closed-form Debye-T⁴ law u_BE = 3·(π²/30)·(k_BT)⁴/(ℏc_E)³ to **all 7 reported digits** — the BE build is correct and is the standard low-T phonon result. The classical-equipartition FOIL (k_BT per mode, `mode-counting-heat-capacity.md:34-46`) over the same spectrum gives u_classical = 1.96×10¹⁵ J/m³.

$$\boxed{u_{BE}/u_{classical} = 3.19\times10^{-29}}\quad\text{(BE is 28.5 OOM BELOW equipartition)}$$

Dimensionless strain-fractions vs substrate rest-energy density u_rest = m_e c²/ℓ_node³ = 1.42×10²⁴ J/m³:
- frac_classical = u_classical/u_rest = **1.38×10⁻⁹**
- frac_BE = u_BE/u_rest = **4.40×10⁻³⁸**

### (iii) E-mode → ε_eff coupling (Ax-1 + Ax-4 primitives) → η_ε (THE BUILD)

The substrate dielectric stiffness is the per-node LC tank at operating point A on the Axiom-4 kernel S(A) = √(1−(A/A_yield)²). Small-signal: ε_eff = ε₀·S(A) ≈ ε₀(1 − ½(A/A_yield)²), so a thermal E-mode amplitude drives

$$\eta_\varepsilon = 1 - \varepsilon_{eff}/\varepsilon_0 \approx \tfrac12\,\langle (A_{th}/A_{yield})^2\rangle = \tfrac12 \cdot \frac{u_{thermal}}{u_{yield}}.$$

Two honest normalizations bracket the yield-energy denominator (neither uses CODATA-α or δ_strain):
- **rest-energy norm** (u_yield = m_e c²/ℓ³): η_ε^BE = 2.20×10⁻³⁸; η_ε^classical = 6.89×10⁻¹⁰
- **kinetic-yield norm** (u_yield = E_yield/ℓ³, E_yield = √α_cold·m_e c² = Ax-4 dielectric yield, `E_YIELD_KINETIC`): η_ε^BE = 2.58×10⁻³⁷; η_ε^classical = 8.07×10⁻⁹

The √α_cold ≈ 0.085 and the factor-½ are O(0.1)–O(1) prefactors. **They cannot bridge a 28–31 OOM gap**, so the outcome is set entirely by step (ii), exactly as the prereg's "OOM-amplification diagnostic IS the test" guard anticipated.

### (iv) Compare to target → adjudicate

| | forward (BE) | classical foil |
|---|---|---|
| η_ε range | 2.2×10⁻³⁸ … 2.6×10⁻³⁷ | 6.9×10⁻¹⁰ … 8.1×10⁻⁹ |
| smallest OOM gap vs 4.447×10⁻⁶ | **31.2** | 2.7 |

Outcome logic (prereg §5): |OOM| > 2 on the forward chain → **C**. The classical foil's 2.7-OOM undershoot independently reproduces the Phase 3-A3 P2 (~20 OOM at their cruder amplitude estimate) / P3 (~3 OOM) diagnostic — the equipartition undershoot is real and is *worsened*, not cured, by the correct quantum (BE) occupation.

## §4 — Why BE occupation undershoots equipartition (the mechanism, named — single explanation for all failures)

Per Rule 11, a single mechanism explains every failure (the equipartition undershoot AND the deeper BE undershoot), so the branch closes cleanly:

**The substrate Debye temperature is enormous (Θ_Debye ≈ 2.3×10¹⁰ K) because the lattice pitch ℓ_node is tiny and c_E = c₀.** At T_CMB = 2.725 K the substrate is ~10¹⁰× colder than its Debye scale. This is the deepest possible quantum-frozen regime for an acoustic spectrum. There:

1. **Classical equipartition (the foil)** assigns k_BT to *every* mode out to ω_D regardless of ℏω/kT. It over-counts: the vast majority of modes (those with ℏω ≫ kT) are in fact frozen, but equipartition pretends they carry k_BT each. Even so, the total is only frac ~ 10⁻⁹ of the rest-energy density — already a ~2.7-OOM undershoot of the target (this is the Phase 3-A3 P2/P3 result, reproduced).

2. **Bose-Einstein occupation (the build)** correctly freezes the high-ω modes. The thermal energy collapses to the Debye-T⁴ law, populating only the ω ≲ k_BT/ℏ corner of the Brillouin zone (k_th/k_D ~ 1.5×10⁻¹⁰). This is **lower** than equipartition by ~(T/Θ_Debye)³ ~ 10⁻²⁹ — that is the entire 28.5-OOM BE-vs-classical gap.

**The prereg's amplification hypothesis runs the thermodynamics backwards.** BE occupation differs from ½kT equipartition by the occupation factor n_BE(ω) vs the classical 1; but n_BE(ω) ≤ k_BT/ℏω with equality only as ω→0, so **BE occupation is bounded ABOVE by equipartition mode-by-mode.** A spectrum can never carry more thermal energy under quantum BE statistics than under classical equipartition. The "amplification the naive ½kT equipartition lacked" cannot come from the occupation statistics — those run the only direction the prereg needed them not to. (This was the `pre-test-physics-check` surfaced question, §1.)

**What would be required for Outcome A** (recorded for the closure roadmap, NOT pursued — no rescue per Rule 11): a substrate-distinct amplification of ~10³¹ over the BE strain-fraction. Candidate sources, all currently absent from the corpus and none derivable from (ℓ_node, G_vac, T_CMB, Ax-1 ε-coupling): (a) a gapless E-spectrum with Θ_Debye comparable to T_CMB rather than ~10¹⁰ K (would require ℓ_node ~ 10⁻³ m, contradicting the canonical ℓ_node = ℏ/m_e c); (b) a resonant/collective ε-coupling that is non-perturbative in (A/A_yield) (the Ax-4 kernel is the canonical small-signal law and gives ½(A/A_yield)²); (c) δ_strain not being an E-mode-thermal-occupation effect at all (i.e., the clm-hp7nlm mechanism-class identification is itself the load-bearing assumption that does not survive quantitative closure). Flag-don't-fix: (c) is a contradiction between the engine result and the corpus mechanism-class claim — surfaced here, NOT resolved (see §8).

## §5 — SM-counterfactual (ave-discrimination-check, MANDATORY per prereg §6.1)

**State the SM-counterfactual explicitly:** Does the η_ε *scale* follow from generic thermal physics any framework shares, or specifically from the substrate E/B-asymmetry + Bose-Einstein occupation?

**Verdict: the η_ε scale is GENERIC-THERMAL, NOT AVE-distinct.** This is exactly what the corpus already states at `statistics-under-ave.md:105` (verbatim): the substrate-distinct content "is the **mode shape** … not the occupation arithmetic, which is standard Bose-Einstein." Decomposition:

- **Framework-neutral (AVE owns nothing):** the Debye-T⁴ thermal energy density of a gapless 3D acoustic spectrum at T ≪ Θ_D is textbook condensed-matter physics. Any framework — SM-with-a-lattice-regulator, lattice QCD, ordinary Debye solid — with a ~MeV-scale acoustic cutoff and a 2.7 K bath predicts the identical 28.5-OOM suppression vs equipartition. The magnitude η_ε ~ 10⁻³⁸ is a generic consequence of the ratio (T_CMB/Θ_Debye), not of any substrate-specific structure.
- **AVE-distinct (the only substrate-specific content):** the E/B mode-shape asymmetry — gapless E (translational) vs gapped B (microrotational, Cosserat mass-gap) — which makes the thermal modulation act on ε while leaving μ frozen. This sets the **sign/direction** of δα (ε softens → α_eff > α₀ → α⁻¹ drops below cold-lattice; the §3-sign-check in clm-hp7nlm). But it does **not** set the magnitude, and the magnitude is the entire FT-1 question.

**Consequence (this is the decisive point FT-2 skipped):** even if the magnitude had matched (it does not, by 31 OOM), a match at the generic-thermal scale would NOT have been AVE-distinct evidence — it would have been a generic Debye-suppression number any lattice framework shares. The AVE-distinct handle is the *direction* + the *forward prediction* of α-running with cosmic T (clm-hp7nlm §6.1), not the η_ε magnitude. So the magnitude derivation is doubly unsupported: it undershoots by 31 OOM AND, were it to match, the match would be generic.

## §6 — Classification (consistency-vs-emergence v1.3)

- **Substrate-mechanism axis: STAYS Class B substrate-mechanism manifestation.** The mechanism (E/B occupation asymmetry) remains *identified* (clm-hp7nlm), but the quantitative substrate-statistical-mechanics derivation of η_ε does **not** close — it produces 10⁻³⁸, not 4.45×10⁻⁶. FT-1 was the candidate Class B → Class 2 lift; it does **not** lift. clm-hp7nlm's §7 honest-gap statement ("does NOT derive η_ε quantitatively … remains back-subtracted from CODATA") is **confirmed and strengthened** by this negative result.
- **Observable axis: STAYS Class 4 observable consistency.** δ_strain = 2.225×10⁻⁶ remains back-subtracted from CODATA at clm-009nkt; this result does not promote it to a derivation (it falsifies the candidate derivation). NOT Class E.
- **This FT-1 result itself**: a **consistency/falsification** finding — it tests whether the BE-occupation chain *can* supply η_ε and finds it cannot, by a margin (31 OOM) that no O(1) prefactor uncertainty touches. It is emergence-class in *method* (forward derivation from primitives, no target fed in) but **negative** in outcome.

## §7 — Anti-tuning + guard audit; honest closure

**Guard 1 — c_EM not c_shear (Pitfall #5, killed Phase 3-A3).** This driver does **not** touch the α formula or any wave speed in the α-modulation step. It computes η_ε and hands it to the canonical OUTPUT form (`delta-strain-cosmic-tcc.md:82`, verbatim: α_eff/α₀ ≈ 1/(1−η_ε)^{1/2} ≈ 1 + η_ε/2), which is the ASYM single-√S form using c_EM = c₀/√S (only ε scales). Re-verified at execution against KB CLAUDE.md INVARIANT-S2 (`CLAUDE.md:64` c_EM = c₀/S(A₀) Maxwell phase velocity; `:65` c_shear = c₀√S; `:71` the c_shear→1/S^{3/2} substitution is the Phase 3-A3 error). The c_E = c₀ used in step (i) is the **mechanical E-mode group velocity** (√(G_vac/ρ_bulk), energy-transport speed) — correctly NOT the α phase velocity; it appears only inside the Debye DOS, never in α. Guard satisfied.

**Guard 2 — ave-discrimination-check.** Done, §5: SM-counterfactual stated explicitly; verdict generic-thermal, not AVE-distinct. (FT-2 skipped this; FT-1 does not.)

**Guard 3 — anti-tuning firewall.** The target 4.447×10⁻⁶ (= 2·`DELTA_STRAIN`) is read by exactly one function (`step_iv_compare_and_adjudicate`), the final compare. Grep-auditable in the driver:
- `step_i_dispersion`: inputs `{G_VAC, RHO_BULK, L_NODE, C_0, M_E, HBAR, K_B}` — topological only.
- `step_ii_occupation`: inputs `{HBAR, C_0, K_B, L_NODE, M_E}` + T_CMB — no α, no δ_strain.
- `step_iii_eps_coupling`: inputs `{M_E, C_0, L_NODE, E_YIELD_KINETIC, ALPHA_COLD}` — α_cold (cold-lattice 4π³+π²+π asymptote, NOT CODATA-α, NOT δ_strain).
- The predicted η_ε (§2) was fixed by the Debye-integral physics BEFORE the compare. No circular feedback. Falsifier-of-framing (prereg §5 HARD) NOT triggered: the result does not "match" by feeding the target back in — it undershoots by 31 OOM with the target firewalled.

**Guard 4 — OOM-amplification diagnostic IS the test.** The forward (BE) chain inherits and *deepens* the 3–20 OOM undershoot (to 31 OOM). The BE occupation, far from supplying the missing amplification, suppresses by a further 28.5 OOM. This is the prereg's Outcome C, verbatim.

**Guard 5 — canonical primitives.** All from `constants.py`; no round numbers (T_CMB = 2.725 K is the measured CMB monopole, the defining cosmic-epoch input, not a free parameter — flagged as such in the driver).

**Honest closure (Rule 11).** The pre-registered prediction failed decisively (31-OOM undershoot, no O(1) prefactor reaches it). A single mechanism — Θ_Debye ≈ 2.3×10¹⁰ K ≫ T_CMB forcing the deeply-quantum Debye-T⁴ regime — explains both the equipartition undershoot AND the deeper BE undershoot. The failure mechanism is named (§4). The branch closes as a clean negative. **No rescue attempted**: the §4 "what would be required for Outcome A" enumeration is recorded for the closure roadmap, explicitly NOT pursued (no debugging toward a fitted amplification factor).

**Substitution-not-retraction (Rule 12).** No corpus claim is retracted by this result — clm-hp7nlm's §7 honest-gap statement already disclosed that η_ε is not derived. This result **confirms** that disclosure quantitatively and supplies the missing magnitude estimate (10⁻³⁸) + the mechanism for why the chain cannot close. clm-009nkt and clm-hp7nlm STAY at confidence 0.55 (the Class 2 lift that would push >0.60 does not occur). No new hypothesis is slotted in.

## §8 — Cascading updates + cross-references

**Claim-quality updates (the auditor lane lands these; surfaced here):**
- **clm-009nkt** (δ_strain): confidence **STAYS 0.55**. Rationale should append the 2026-05-31 FT-1 OUTCOME-C note: the Q-DELTA-MAP-1-quant candidate derivation (E-mode BE-occupation) undershoots η_ε by ~31 OOM; the Class-2 lift gated on Q-DELTA-MAP-1-quant does not occur; the magnitude stays fitted. Strengthen-by item "Q-DELTA-MAP-1-quant: derive η_ε from E-mode dispersion + BE occupation" should be updated from OPEN to **ATTEMPTED → NEGATIVE (FT-1, 2026-05-31): BE occupation undershoots by 31 OOM; mechanism = Θ_Debye ≫ T_CMB; any first-principles closure needs a substrate-distinct ~10³¹ amplification absent from the corpus.**
- **clm-hp7nlm** (Cosserat-thermal ASYM mechanism): confidence **STAYS 0.55** (Class B). The §7 honest-gap statement is confirmed, not changed. The mechanism-class *identification* survives (E/B asymmetry sets the sign); the *magnitude* derivation is now a recorded negative, not merely open.

**Flag-don't-fix surfaced contradiction (for Grant adjudication, NOT resolved here):** the engine result (η_ε^BE ~ 10⁻³⁸) conflicts with the corpus mechanism-class claim (clm-hp7nlm: the E-mode-thermal-occupation ASYM mechanism produces δ_strain ≈ 2.225×10⁻⁶) **at the magnitude level by 31 OOM**. Two readings, both consistent with the data, NOT adjudicated:
  (i) the mechanism-class identification is correct for the *sign/direction* but δ_strain's *magnitude* is simply not an E-mode-thermal effect (it is something else — a genuinely open substrate question, Q-DELTA-MAP-1-quant returns to OPEN-with-a-falsified-candidate);
  (ii) the entire δ_strain ↔ thermal-occupation framing is a back-fit and δ_strain is a cold-lattice geometric residual (α_cold = 4π³+π²+π vs CODATA) with no thermal mechanism at all.
Both file paths: engine = `src/scripts/vol_3_macroscopic/ft1_delta_strain_eta_epsilon_driver.py` + `results/ft1_delta_strain_eta_epsilon.json`; corpus = `manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/delta-strain-cosmic-tcc.md:73-92`. Surfaced per flag-don't-fix; Grant adjudicates which reading (or a third) holds.

> → Primary: [`delta-strain-cosmic-tcc.md`](../manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/delta-strain-cosmic-tcc.md) (clm-hp7nlm) — α-modulation OUTPUT form (:73-92, reused unchanged); §7 honest-gap (confirmed by this result)
> → Primary: KB [`CLAUDE.md`](../manuscript/ave-kb/CLAUDE.md) INVARIANT-S2 (:64-71) — c_EM vs c_shear (Pitfall #5 guard re-verified)
> ↗ See also: [`2026-05-28_phase-3-a3-delta-strain-machian-projection-result.md`](2026-05-28_phase-3-a3-delta-strain-machian-projection-result.md) §3 — the P2/P3 naive-equipartition 3–20 OOM undershoot, now reproduced (foil: 2.7 OOM) and explained by the single Θ_Debye ≫ T_CMB mechanism
> ↗ See also: [`mode-counting-heat-capacity.md`](../manuscript/ave-kb/vol3/condensed-matter/ch11-thermodynamics/mode-counting-heat-capacity.md) (clm-uu6dl5) — classical g_* equipartition, used as the explicit FOIL to beat (BE falls 28.5 OOM below it)
> ↗ See also: [`statistics-under-ave.md`](../manuscript/ave-kb/common/statistics-under-ave.md) §6, §8 (:105,:121) — the parent leaf; "occupation arithmetic is standard Bose-Einstein" (the SM-counterfactual seed); Q-DELTA-MAP-1-quant open-lane

## §9 — Pure-AVE-corpus rule

NO external-context references in this result or any associated deliverable. Pure substrate physics throughout.
