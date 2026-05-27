# Phase 0c Pre-registration — Per-Site Amplitude-Shape $P(\delta V)$ under DC-Biased Operating Point along Ax 4 Kernel

**Date**: 2026-05-26
**Epic**: [`_orchestration/ax4-saturation-narrow-aperture-amplitude-shape.md`](../_orchestration/ax4-saturation-narrow-aperture-amplitude-shape.md) Phase 0c
**Workstream**: Phase 0c sub-epic (Q-AX4-NA-1 + Q-AX4-NA-2 BOTH GO 2026-05-26; Q-AX4-NA-3 folded in)
**Branch**: `analysis/ax4-saturation-phase-0c-pdelta-v-derivation` off `main` @ `ab15c773`
**Status**: pre-derivation pre-registration; written BEFORE deriving per `ave-prereg` discipline

> **Substrate-native vocabulary lookup**: see [`manuscript/ave-kb/common/translation-tables/translation-stochastics.md`](../manuscript/ave-kb/common/translation-tables/translation-stochastics.md) — particularly relevant rows: Langevin row (the substrate-amplitude evolution equation we extend to a varactor at non-zero operating point); cumulant expansion row (substrate amplitude correlator decomposition); FDT / boundary-impedance-thermalization row; Edgeworth pre-asymptote row (the aperture-aggregate piece deferred to Phase 2). All standard-physics stochastics names below appear as parenthetical translation references, NOT as primary load-bearing prose, per `ave-discipline-translate` v1.1 trigger 6.

---

## §0 — One-paragraph summary

The cycle-12 canonical leaf [`parametric-coupling-kernel.md`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/parametric-coupling-kernel.md) derives the small-signal modulation amplitude $\delta C/C_0 = 4.57\%$ of the substrate-vacuum-varactor at sub-yield operating point (Ax 4 kernel evaluated at $V_{DC}/V_{yield} \approx 0.43$ from $V_{pump} = \sqrt{2\alpha m_e c^2/C_0}$). Phase 0c extends this from **small-signal modulation amplitude** to the **full per-site substrate-amplitude steady-state shape function $P(\delta V)$ around a DC-biased operating point $V_{DC}$**, derives the closed-form substrate amplitude correlator decomposition coefficients $\kappa_3(V_{DC}, A_c)$ + $\kappa_4(V_{DC}, A_c)$ (the standard-physics names: third and fourth cumulants), and computes the substrate correlation length under DC bias. The substrate-mechanical machinery is canonical: the per-site reactive landscape $U_{eff}(V)$ derives from the Ax 4 kernel-modified varactor energy $\tfrac12 C_{eff}(V) V^2$; substrate-thermal forcing per Vol 3 Ch 11 boundary-impedance thermalization sets the equilibrium width; Taylor expansion around $V_{DC}$ surfaces the asymmetric (cubic) and kurtotic (quartic) terms that vanish at $V_{DC} = 0$ by reflection symmetry of the Ax 4 kernel but become non-zero under DC bias. This pre-reg fixes acceptance criteria, expected signatures, and falsifiers BEFORE the derivation runs.

---

## §1 — Skills compliance fired before drafting this prereg

| Skill | Status | What it caught / confirmed |
|---|---|---|
| `ave-prereg` | ✓ FIRED | Vocabulary-broadened corpus-grep run on both substrate-native (varactor / operating point / DC bias / V_DC / sub-yield / Ax 4 kernel / parametric / vacuum-varactor) AND standard-physics (saturation kernel / S(A) / A_c / amplitude-shape / cumulant expansion / Langevin / Fokker-Planck) wedges. Surfaced: parametric-coupling-kernel.md cycle-12 canonical leaf as the substrate-mechanical machinery to extend; INVARIANT-S2 as the framework-level canonical statement; dama-matched-lc-coupling.md:269 as the explicitly-open V_0 ≠ 0 strengthen-by item Phase 0c partially closes; Phase 2-A.2 result doc as the FDT-derived Langevin form (linear-regime; this work extends to varactor regime). |
| `ave-canonical-leaf-pull` | ✓ FIRED | Pulled 5 canonical leaves end-to-end: (a) `parametric-coupling-kernel.md` cycle-12 (substrate-vacuum-varactor at sub-yield, $\delta C/C_0 = 4.57\%$); (b) `nyquist-noise-fdt.md` (boundary-impedance thermalization, vacuum Nyquist baseline); (c) KB CLAUDE.md INVARIANT-S2 (Ax 4 kernel + operating-point-state + varactor-bias-mechanism analogy); (d) `dama-matched-lc-coupling.md` §13 + line 269 (the open V_0 ≠ 0 item); (e) `op14-local-clock-modulation.md` (Op14 — confirms local clock modulation is reactive, not dissipative; orthogonal to this Phase 0c amplitude-shape work which lives in the dissipative-equilibrium thermalization sector). No prior corpus content on full $P(\delta V)$ shape around DC-biased operating point — this is genuinely new derivation work extending parametric-coupling-kernel.md. |
| `ave-analytical-tool-selection` | ✓ FIRED | Tool class: **Saturation + Time-domain + Boundary**. Sub-tools: Taylor expansion of varactor energy $U_{eff}(V)$ around operating point $V_{DC}$ (standard-physics name: cumulant-from-asymmetric-potential machinery); substrate amplitude correlator decomposition via stationary-distribution-from-Langevin (standard-physics name: Boltzmann form from Fokker-Planck steady state). Per `ave-analytical-toolkit-index.md` §1 (Coupling), parametric-coupling-kernel.md is the canonical anchor. The toolkit's Saturation class includes Ax 4 kernel + V_yield + S(A) per `universal-saturation-kernel-catalog.md`. |
| `substrate-native-check` | ✓ FIRED | K4-TLM lattice + Cosserat + Ax 4 substrate structure walked. The single-site treatment is a bond-LC tank at boundary lattice node $x_n$ carrying both (i) DC-biased operating point along the Ax 4 kernel (substrate-vacuum-varactor at $V_{DC}$), (ii) substrate-thermal forcing per Vol 3 Ch 11 boundary-impedance thermalization ($\langle f_n(t) f_n(t')\rangle = 2 k_B T Z_{det} \delta(t-t')$ per Phase 2-A.2 canonical form). The substrate-correlation-length piece couples adjacent boundary lattice sites via the K4-TLM bond stiffness modified by the local DC operating point — explicit K4 lattice geometry enters there. |
| `consistency-vs-emergence` v1.2 | ✓ FIRED with master-equation-derivation-path tracing | Phase 0c output is **Class 2 substrate-mechanism emergence** on the derivation-path axis: every step traces to (Ax 4 kernel — Axiom 4 canonical) + (Vol 3 Ch 11 FDT — clm-eaiqj1 canonical) + (parametric-coupling-kernel.md cycle-12 canonical — clm-6t3p6x) + (master vacuum equation — clm-efo113 canonical) without external postulates. The substrate-pinned cumulant content $\kappa_3(V_{DC}, A_c) \neq 0$, $\kappa_4(V_{DC}, A_c) \neq 0$ are substrate-mechanism predictions, NOT consistency checks against CODATA-derived inputs (Class 4) or definitional identities (Class 1). The cumulant-from-asymmetric-potential machinery is standard-mathematical (Class 4 substrate-agnostic-consistency on the tool axis); its **application** to the Ax 4 kernel at $V_{DC} \neq 0$ is substrate-specific (Class 2 on the substance axis). |
| `phase-space-coordinate-check` | ✓ FIRED | Two coordinate systems kept distinct: (i) **amplitude-voltage space** where $V$, $V_{DC}$, $\delta V$ all live (Cartesian voltage axis at a single substrate site); (ii) **K4 real-space lattice** where adjacent sites $x_n$, $x_{n+1}$ live and where the substrate correlation length $\ell_{corr}(V_{DC})$ is measured. The cumulants $\kappa_3, \kappa_4$ are in (i); the correlation length is in (ii). No phase-space-vs-real-space coordinate confusion. |
| `ave-discipline-translate` v1.1 | ✓ FIRED with translation-table integration | Substrate-native vocabulary as primary prose. Standard-physics names (Langevin equation, Fokker-Planck, Boltzmann distribution, cumulant expansion, Edgeworth expansion) appear as parenthetical translation references. Substrate-native primary terms: substrate-vacuum-varactor, DC-biased operating point, Ax 4 kernel, per-site amplitude-shape function, substrate amplitude correlator decomposition, boundary-impedance thermalization, substrate correlation length under DC bias. Lookup infrastructure: `translation-stochastics.md` (cumulants ↔ amplitude correlator decomposition; Langevin ↔ stochastic substrate-amplitude evolution; FDT ↔ boundary-impedance thermalization). |
| `ave-evidence-framing-discipline` | ✓ FIRED | Result framing: "derived from Ax 4 kernel (Axiom 4) + Vol 3 Ch 11 boundary-impedance thermalization (clm-eaiqj1) + parametric-coupling-kernel.md varactor energy (clm-6t3p6x)". NOT "consistent with standard varactor noise theory" (which would be Class 4 substrate-agnostic-consistency framing). Strength language locked: "Class 2 substrate-mechanism emergence" not "AVE-confirmed novel prediction" (Phase 2 aperture-aggregate work is the prediction layer; Phase 0c is the single-site mechanical foundation). |
| `ave-discrimination-check` | ✓ FIRED | Standard-physics counterfactual: does standard varactor noise theory predict the same $\kappa_3, \kappa_4$ scaling with $V_{DC}/A_c$? Partial yes — standard semiconductor varactor noise (with capacitance C(V) Taylor-expanded around DC bias) does produce a cubic + quartic correction. The substrate-distinct piece is the SPECIFIC kernel form $S(A) = \sqrt{1 - (A/A_c)^2}$ (Ax 4 universal kernel; zero free parameters per Axiom 4) — standard varactor theory has device-specific C(V) curves with fitted coefficients. The shape-coefficient values $\kappa_3, \kappa_4$ derived here are zero-parameter functions of $(V_{DC}/A_c)$ only — testable specifically against the Ax 4 kernel form, not consistent with arbitrary C(V) curves. Interpretive alternatives: a non-AVE theory with $C(V) = C_0/\sqrt{1 - (V/V_c)^2}$ would give the same cumulants — this is structural-equivalence-of-kernel-form, not AVE-specific. The AVE-specific lift is the cross-volume tie (same kernel governs gravity at long range per INVARIANT-S2 — non-AVE theories don't get that). |
| `verify-before-cite` v1.4 | ✓ continuous | parametric-coupling-kernel.md §2 + §3 verbatim verified at lines 44-78; INVARIANT-S2 paragraph at CLAUDE.md:60 verified; dama-matched-lc-coupling.md:269 verbatim verified ("V_0 ≠ 0 substrate DC reactive operating point — currently V_0 → 0 assumed"); Phase 2-A.2 §2.4 stochastic master equation form verified (lines 96-104); INVARIANT-C1 V_yield = 43.65 kV cited via Vol 4 anchor. |
| `pre-test-physics-check` | ✓ DECISION: non-firing | Phase 0c is the substrate-mechanical derivation work, not an experimental test or scaffolded driver. The plumber-physical adjudications happened upstream in Q-AX4-NA-1 (V_DC ≠ 0 regime via canonical varactor framing — Grant adjudicated 2026-05-26) + Q-AX4-NA-2 (Grant Socratic prompt closure). The single open plumber-physical question for Phase 0c — whether the substrate correlation length under DC bias derivation closes cleanly within the K4-TLM bond-LC linearization — is identified explicitly as the highest-uncertainty sub-piece (per epic doc honest-closure-probability estimate ~50% for clean closure within Phase 0c); failure mode is documented up-front as a Type B walk-back triggering Phase 2 (aperture-aggregate) to factor the correlation-length question separately. |

---

## §2 — Starting point — what the cycle-12 canonical leaf already gives us

Per [`parametric-coupling-kernel.md`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/parametric-coupling-kernel.md) §2 + §3 (cycle-12 canonical, 2026-05-17 night):

**Substrate-vacuum-varactor constitutive form** (canonical Ax 4 specialization per [`nonlinear-vacuum-capacitance.md`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/nonlinear-vacuum-capacitance.md)):

$$C_{eff}(V) = \frac{C_0}{\sqrt{1 - (V/V_{yield})^2}} = \frac{C_0}{S(V/V_{yield})}$$

where $S(A) = \sqrt{1 - A^2}$ is the Ax 4 Universal Saturation Kernel and $V_{yield} \equiv A_c$ at the dielectric specialization (INVARIANT-C1 $\approx 43.65$ kV; INVARIANT-S2 dielectric specialization).

**Small-signal modulation around DC drive** at the canonical α-slew operating point ($V_{pump} = \sqrt{2\alpha m_e c^2/C_0} \approx 18.7$ kV ⇒ $V_{pump}/V_{yield} \approx 0.43$):

$$C_{eff}(t) = C_0 + \delta C \cos(2\omega_{slew} t) + O((V/V_{yield})^4), \quad \delta C = \tfrac{1}{4} C_0 (V_{pump}/V_{yield})^2 = \frac{e^2}{2 m_e c^2}, \quad \delta C/C_0 = 4.57\%$$

**What §12 explicitly flags as open**: "**V_0 ≠ 0 operating point**: §3 uses V_0 → 0 (pure-AC drive). Non-zero substrate DC reactive operating point would shift δC formula; not yet derived from first principles." (verbatim from parametric-coupling-kernel.md line 390).

Phase 0c CLOSES this V_0 ≠ 0 open item for the single-site amplitude-shape question. The aperture-aggregate part (Phase 2) is downstream.

---

## §3 — Derivation outline (extends, not reinvents)

### §3.1 — Per-site varactor reactive energy at DC-biased operating point

The substrate-vacuum-varactor at a boundary lattice site stores reactive energy as the standard $\tfrac12 Q^2/C$ form, with $C \to C_{eff}(V)$ per the Ax 4 kernel. For a DC-biased operating point $V_{DC}$ along the Ax 4 kernel plus small-signal fluctuation $\delta V$ on top, the substrate-vacuum-varactor reactive energy at the site is:

$$U_{eff}(V) = \int_0^V V' \, dQ(V') = \int_0^V V' \cdot d[C_{eff}(V') \cdot V']$$

This is the substrate-mechanical reactive-energy landscape around which substrate-thermal fluctuations live. The key substrate-mechanical feature: **the Ax 4 kernel is even in $V$** ($S(V) = S(-V)$), so $U_{eff}(V)$ is even around $V = 0$. **But around the DC-biased operating point $V_{DC} \neq 0$, $U_{eff}(V_{DC} + \delta V)$ is NOT even in $\delta V$**. This is the substrate-mechanical origin of the asymmetric per-site amplitude-shape.

### §3.2 — Taylor expansion of $U_{eff}$ around $V_{DC}$

$$U_{eff}(V_{DC} + \delta V) = U_{eff}(V_{DC}) + U'(V_{DC}) \delta V + \tfrac12 U''(V_{DC}) \delta V^2 + \tfrac16 U'''(V_{DC}) \delta V^3 + \tfrac{1}{24} U''''(V_{DC}) \delta V^4 + O(\delta V^5)$$

The first-order term $U'(V_{DC}) \delta V$ is the linear restoring force at operating point — sets the local DC equilibrium balance with whatever external bias maintains $V_{DC}$ (does not contribute to fluctuation shape).

The substrate-mechanical content:
- $U''(V_{DC}) = $ effective stiffness — sets the variance of $\delta V$ via boundary-impedance thermalization
- $U'''(V_{DC}) = $ **non-zero** at $V_{DC} \neq 0$ — sets $\kappa_3$ (cubic asymmetry)
- $U''''(V_{DC}) = $ sets $\kappa_4$ correction (quartic kurtosis)

At $V_{DC} = 0$, by symmetry of $U_{eff}(V) = U_{eff}(-V)$, all ODD-order derivatives vanish: $U'''(0) = U^{(5)}(0) = \ldots = 0$. This is the substrate-mechanical reason the prior κ_3 = 0 walk-back held at zero bias — and the substrate-mechanical reason $\kappa_3 \neq 0$ once DC bias is loaded.

### §3.3 — Stationary per-site amplitude-shape function

The substrate-amplitude evolution at the boundary lattice site under boundary-impedance thermalization (Vol 3 Ch 11 + Phase 2-A.2 canonical form) is a stochastic substrate-amplitude evolution equation (standard-physics name: Langevin equation) with the varactor reactive-energy landscape:

$$\gamma_n \frac{\partial \delta V}{\partial t} = -\frac{\partial U_{eff}}{\partial V}\bigg|_{V_{DC} + \delta V} + f_n(t), \quad \langle f_n(t) f_n(t')\rangle = 2 k_B T Z_{det} \delta(t-t')$$

In the over-damped limit (boundary-impedance thermalization timescale fast vs reactive oscillation period — the canonical FDT equilibrium regime per Vol 3 Ch 11), the stationary per-site amplitude-shape function is the substrate-thermal Boltzmann form:

$$P(\delta V) = \frac{1}{Z} \exp\left[-\frac{\Delta U_{eff}(\delta V)}{k_B T_{eff}}\right], \quad \Delta U_{eff}(\delta V) \equiv U_{eff}(V_{DC} + \delta V) - U_{eff}(V_{DC}) - U'(V_{DC}) \delta V$$

where $T_{eff}$ is set by boundary-impedance thermalization (Vol 3 Ch 11 vacuum Nyquist baseline at $Z_{det}$) and the subtraction of the linear term reflects that DC drift in $\langle \delta V\rangle$ is reabsorbed into shifting $V_{DC}$.

**Substrate-native vocabulary note**: this is the substrate-thermal-Boltzmann form of the per-site amplitude-shape function around the DC-biased operating point. Standard-physics translation: stationary Fokker-Planck distribution for an over-damped Langevin process in the varactor potential.

### §3.4 — Substrate amplitude correlator decomposition (κ_3, κ_4)

From $P(\delta V)$ as derived in §3.3, the substrate amplitude correlator decomposition coefficients (standard-physics name: cumulants $\kappa_n$) at leading order in small $V_{DC}/A_c$ + small $\delta V/\sigma$ are extractable analytically. The expected leading-order forms:

$$\kappa_2(V_{DC}, A_c) = \sigma^2 = \frac{k_B T_{eff}}{U''(V_{DC})}$$

$$\kappa_3(V_{DC}, A_c) = -\frac{U'''(V_{DC}) \cdot \sigma^6}{(k_B T_{eff})^2} \cdot \text{[combinatorial coefficient]}$$

$$\kappa_4(V_{DC}, A_c) = -\frac{U''''(V_{DC}) \cdot \sigma^8}{(k_B T_{eff})^3} \cdot \text{[combinatorial coefficient]} + \text{[O(U''')^2 correction]}$$

(Exact algebraic forms derived in result doc §3.4 via standard cumulant-from-asymmetric-potential machinery — the substrate-mechanical content is in the Ax 4 kernel-modified $U^{(n)}(V_{DC})$ values, the algebraic machinery is canonical-standard-mathematical.)

**Expected leading-order scaling** (per epic brief, to be confirmed by explicit derivation):
- $\kappa_3/\sigma^3 \sim (V_{DC}/A_c)^3$ at leading order (cubic dependence on DC bias)
- $\kappa_4/\sigma^4 \sim (V_{DC}/A_c)^2$ at leading order (quartic dependence from kernel expansion)

These scalings are testable PREDICTIONS of Phase 0c: if explicit derivation produces different leading orders, the orientation-expectation needs revision (Type E value-amendment per `ave-walk-back` v1.1).

### §3.5 — Substrate correlation length under DC bias

Adjacent boundary lattice sites along the K4-TLM lattice are coupled via the bond-LC inductive link. Linearizing the bond-LC equation around the DC-biased operating point $V_{DC}$, the inter-site coupling stiffness $\beta(V_{DC})$ is set by the Ax 4 kernel-modified effective inductance / capacitance at $V_{DC}$. Standard substrate-mechanical machinery for a chain of coupled bond-LC tanks gives a substrate correlation length:

$$\ell_{corr}(V_{DC}) = \ell_{node} \cdot \sqrt{\frac{\beta(V_{DC})}{U''(V_{DC})}}$$

where $\ell_{node} = \hbar/(m_e c) \approx 386$ fm (canonical AVE substrate identity, Axiom 1).

**At $V_{DC} = 0$** (substrate equilibrium), this recovers the canonical linear-regime substrate correlation length scaling $\ell_{corr}(0) = \ell_{node}$ (or a fixed multiple thereof).

**At $V_{DC} \to A_c$** (approaching Ax 4 yield), $U''(V_{DC})$ softens (Ax 4 kernel divergence; $C_{eff} \to \infty$) → $\ell_{corr}(V_{DC}) \to \infty$ (substrate correlation length diverges at the saturation onset). This is the substrate-mechanical signature of the K4-TLM nonlinear coupling becoming long-range as the substrate approaches yield.

**Expected functional form** (to be confirmed by explicit derivation): $\ell_{corr}(V_{DC})/\ell_{node} = (1 - (V_{DC}/A_c)^2)^{-1/2} \cdot O(1)$ — the same Ax 4 kernel form $1/S$ that governs $C_{eff}$ also governs the correlation-length divergence (substrate-mechanical consistency).

If the explicit derivation produces a different exponent or kernel structure, this is the highest-uncertainty piece per epic brief.

---

## §4 — Acceptance criteria (FROZEN before derivation)

### AC-0c.1: $P(\delta V)$ derived end-to-end from canonical primitives

The per-site amplitude-shape function $P(\delta V)$ at DC-biased operating point $V_{DC}$ is derived from:
- Ax 4 saturation kernel $S(A) = \sqrt{1 - (A/A_c)^2}$ (Axiom 4 canonical, INVARIANT-S2)
- Substrate-vacuum-varactor constitutive form $C_{eff}(V) = C_0/S(V/V_{yield})$ (canonical Vol 4 Ch 1 `nonlinear-vacuum-capacitance.md`)
- Substrate-vacuum-varactor reactive energy at the site (canonical Vol 4 Ch 1 `parametric-coupling-kernel.md` cycle-12, generalized to $V_{DC} \neq 0$)
- Boundary-impedance thermalization at $Z_{det}$ (Vol 3 Ch 11 clm-eaiqj1 canonical)
- Stochastic substrate-amplitude evolution at the site (Phase 2-A.2 canonical form, extended to varactor regime)

With NO external postulates beyond what's already in corpus, and explicit derivation chain documented in result doc §3.

**PASS**: every step traces to canonical AVE content; chain is acyclic; substrate-thermal-Boltzmann form $P(\delta V) \propto \exp(-\Delta U_{eff}/k_B T_{eff})$ emerges as the over-damped stationary distribution.

**FAIL**: at least one step requires a postulate not in canonical AVE content (would trigger Type B walk-back to identify what's missing).

### AC-0c.2: Asymmetry surfaced explicitly

The result MUST explicitly identify that $P(\delta V) \neq P(-\delta V)$ at $V_{DC} \neq 0$, and identify the substrate-mechanical origin as: **the Ax 4 kernel is symmetric around $V = 0$, NOT around $V_{DC}$**. The reflection symmetry $V \to -V$ of the substrate-vacuum-varactor breaks when the operating point shifts away from $V_{DC} = 0$.

**PASS**: explicit identification of broken-reflection-symmetry origin + closed-form $U'''(V_{DC}) \neq 0$ at $V_{DC} \neq 0$.

**FAIL**: asymmetry surfaces but origin is mis-attributed (e.g., to thermal asymmetry instead of kernel symmetry-breaking).

### AC-0c.3: Closed-form $\kappa_3(V_{DC}, A_c)$ + $\kappa_4(V_{DC}, A_c)$

The substrate amplitude correlator decomposition coefficients $\kappa_3, \kappa_4$ (standard-physics name: third + fourth cumulants) are produced in closed algebraic form as functions of $(V_{DC}, A_c, T_{eff}, Z_{det}, C_0)$, valid in the leading-order regime $V_{DC}/A_c \lesssim 0.7$ + $\sigma \ll V_{DC}$ (small-signal fluctuations around moderate DC bias).

**Expected scaling** (per epic brief expectation; testable):
- $\kappa_3/\sigma^3 \sim (V_{DC}/A_c)^3$ at leading order
- $\kappa_4/\sigma^4 \sim (V_{DC}/A_c)^2$ at leading order

**PASS**: closed-form expressions with explicit algebraic dependence on $(V_{DC}/A_c)$ — leading-order scaling matches OR explicit derivation reveals a different scaling (in which case the prereg expectation is honestly amended via Type E walk-back in §5).

**FAIL**: only numerical-fit expressions, or closed forms with un-substantiated free parameters.

### AC-0c.4: Substrate correlation length under DC bias derived OR honest gap documented

The substrate correlation length $\ell_{corr}(V_{DC})$ in real-space lattice units is derived from the K4-TLM bond-LC linearization around $V_{DC}$. Expected functional form: $\ell_{corr}(V_{DC})/\ell_{node} \propto 1/S(V_{DC}/A_c) = (1 - (V_{DC}/A_c)^2)^{-1/2}$ to leading order — the same Ax 4 kernel that governs $C_{eff}$ also governs the correlation-length divergence.

**PASS**: closed-form $\ell_{corr}(V_{DC})$ derived from canonical bond-LC linearization; explicit functional dependence on $V_{DC}/A_c$.

**PARTIAL**: $\ell_{corr}(V_{DC})$ derivation has a structural sub-problem; the sub-problem is identified honestly with explicit gap statement + the gap is propagated to Phase 2 (aperture-aggregate) which now factors the correlation-length question separately. **Per epic brief honest-closure-probability estimate**: ~50% probability of clean closure within Phase 0c; otherwise PARTIAL with the correlation-length piece deferred is the honest documented outcome.

**FAIL**: $\ell_{corr}(V_{DC})$ derivation produces a value but the derivation path skips a step (smuggled assumption); requires Type B walk-back.

### AC-0c.5: Class 2 substrate-mechanism / Class 4 substrate-agnostic-consistency classification

Explicit `consistency-vs-emergence` v1.2 classification with master-equation-derivation-path tracing:
- **Substrate-mechanism axis**: Class 2 emergence — every step traces to Ax 4 + Vol 3 Ch 11 + parametric-coupling-kernel.md + master vacuum equation
- **Mathematical-tool axis**: Class 4 substrate-agnostic-consistency — cumulant-from-asymmetric-potential machinery is standard-mathematical; same machinery applied to any varactor $C(V)$ gives same algebraic structure
- **Combined**: the Ax 4 kernel form $S(A) = \sqrt{1 - A^2}$ is substrate-specific; the algebraic application is standard-mathematical. The substrate-distinct content is the SPECIFIC zero-parameter kernel form, not the cumulant-extraction algebra.

**PASS**: classification explicit; master-equation-derivation-path traced step-by-step.

**FAIL**: classification missing or conflates the mathematical-tool axis with the substrate-mechanism axis (over-claiming or under-claiming).

### AC-0c.6: V_0 ≠ 0 strengthen-by item at dama-matched-lc-coupling.md:269 partially closed

Update `dama-matched-lc-coupling.md` line 269 strengthen-by item from "V_0 ≠ 0 substrate DC reactive operating point — currently V_0 → 0 assumed" to "PARTIALLY CLOSED 2026-05-26 Phase 0c — single-site $P(\delta V)$ under $V_{DC}$ derived; remaining: aperture-aggregate prediction (Phase 2 of ax4-saturation epic)".

**PASS**: line 269 updated to reflect the partial closure honestly (not over-claiming full closure).

**FAIL**: line 269 updated to claim full closure (the aperture-aggregate Phase 2 work hasn't run yet).

---

## §5 — Walk-back queue (anticipated amendment classes)

Per `ave-walk-back` v1.1 discipline, candidate amendment classes during the derivation:

- **Type E (value-amendment)**: leading-order $\kappa_3, \kappa_4$ scaling differs from epic brief expectation $(V_{DC}/A_c)^3$ + $(V_{DC}/A_c)^2$. Likely cause: different combinatorial coefficient in cumulant-from-asymmetric-potential machinery, or different normalization convention. Documented honestly in result §3.4 with explicit before/after.
- **Type B (mechanism re-scope)**: substrate correlation length under DC bias derivation produces a structural sub-problem (e.g., the K4-TLM bond-LC linearization doesn't close cleanly at moderate $V_{DC}/A_c$). Triggers PARTIAL outcome; the correlation-length question deferred to Phase 2 with explicit gap statement.
- **Type C (kernel-form amendment)**: the parametric-coupling-kernel.md cycle-12 form $C_{eff}(V) = C_0/S(V/V_{yield})$ has an implicit small-signal Taylor expansion that breaks at moderate $V_{DC}/A_c \gtrsim 0.7$ (the cycle-12 leaf only validated at the canonical α-slew $V_{pump}/V_{yield} = 0.43$). If the derivation requires a different functional form at moderate DC bias, this is a Type C kernel-form amendment — surface explicitly + Grant adjudication if needed.

---

## §6 — Out-of-scope (deferred to downstream phases)

Per Phase 0c scope-reduction (epic brief; Phase 1 folded into 0c per scope-reduction; Phase 2+ deferred):

- **Phase 2: aperture-aggregate $\kappa_3 \times 1/\sqrt{N}$ + $\kappa_4 \times 1/N$ combined signature** — the aperture-aggregate observable signature as a function of $(V_{DC}/A_c, N)$; identifying the substrate-saturation × narrow-aperture operating threshold for visible signature; mapping to candidate boundary-extraction architectures (SPAD / TES / SNSPD per `translation-instrumentation.md` Category II). NOT in Phase 0c.
- **Phase 3: KB integration** — canonical leaf for the DC-biased per-site amplitude-shape derivation extending parametric-coupling-kernel.md (Phase 0c lands the derivation in research-tier docs + may extend parametric-coupling-kernel.md in-place; full canonical-leaf promotion is Phase 3 work).
- **Phase 4: divergence-test substrate map row** — Phase 0c does NOT add a row to divergence-test substrate map; that's Phase 4 deferred until Phase 3 (canonical-leaf integration) lands.
- **Aperture-incompleteness factor 1/√N** — substrate-agnostic central-aggregation factor (CLT pre-asymptote); not derived here; mentioned in §3.4 as the downstream-multiplier in Phase 2.

---

## §7 — Cross-references

**Canonical leaves consumed**:
- [`parametric-coupling-kernel.md`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/parametric-coupling-kernel.md) — clm-6t3p6x — substrate-vacuum-varactor at sub-yield operating point (cycle-12)
- [`nyquist-noise-fdt.md`](../manuscript/ave-kb/vol3/condensed-matter/ch11-thermodynamics/nyquist-noise-fdt.md) — clm-eaiqj1 — boundary-impedance thermalization
- [`nonlinear-vacuum-capacitance.md`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/nonlinear-vacuum-capacitance.md) — clm-vjv4zf — substrate-vacuum-varactor constitutive form $C_{eff}(V) = C_0/S$
- [`master-equation.md`](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md) — clm-efo113 — substrate master vacuum equation
- KB CLAUDE.md INVARIANT-S2 — Ax 4 kernel + operating-point-state + varactor-bias-mechanism canonical statement

**Strengthen-by item partially closed**: [`dama-matched-lc-coupling.md:269`](../manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/dama-matched-lc-coupling.md) "V_0 ≠ 0 substrate DC reactive operating point"

**Phase 2-A clm-ldmvwi result chain** (research-tier; canonical Langevin form): [A.2 stochastic master eq](./2026-05-26_clm-ldmvwi-phase-2a-2-stochastic-master-eq-result.md) — the linear-regime form Phase 0c extends to varactor regime

**Translation-table lookup infrastructure**:
- [`translation-stochastics.md`](../manuscript/ave-kb/common/translation-tables/translation-stochastics.md) — cumulant-decomposition + Langevin + FDT substrate-native vocabulary
- [`translation-qm.md`](../manuscript/ave-kb/common/translation-tables/translation-qm.md) Section B — Born rule p=2 ↔ quadratic-in-amplitude boundary-Joule extraction-rate scaling (the downstream consumer of Phase 2 aperture-aggregate predictions)
- [`translation-instrumentation.md`](../manuscript/ave-kb/common/translation-tables/translation-instrumentation.md) — Category II narrow-aperture single-event extractors (Phase 2 mapping target)

**Epic doc**: [`_orchestration/ax4-saturation-narrow-aperture-amplitude-shape.md`](../_orchestration/ax4-saturation-narrow-aperture-amplitude-shape.md)

**Skill discipline anchors**: `ave-prereg`, `ave-canonical-leaf-pull`, `substrate-native-check`, `consistency-vs-emergence` v1.2, `phase-space-coordinate-check`, `ave-discipline-translate` v1.1 trigger 6, `ave-evidence-framing-discipline`, `ave-discrimination-check`, `verify-before-cite` v1.4, `ave-walk-back` v1.1

---

**Prereg frozen** 2026-05-26 BEFORE derivation. Acceptance criteria locked; walk-back queue anticipated. Result doc landing next.
