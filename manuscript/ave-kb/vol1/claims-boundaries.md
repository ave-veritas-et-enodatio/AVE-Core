# Vol 1 — Foundations — Claim Boundaries

<!-- path-stable: referenced from CLAUDE.md INVARIANT-S7 and from vol1/index.md bootstrap directive -->

> **Canonicality:** Leaves are canonical; this volume's indexes are derived summaries. See [cross-cutting boundaries](../claims-boundaries.md) for the full preamble and the canonical list of project-wide tripwires (the cross-cutting sidecar is the source of truth for which tripwires are project-wide; do not infer the list from this preamble). Entries below are scoped to Vol 1; cross-cutting tripwires with vol1-specific manifestations are noted but not duplicated.

---

## Zero-Parameter Closure Status (Conditional on Thermal Closure)
<!-- id: 5xon03 -->

The framework's "zero free parameters" headline rests on a layered closure that is currently *conditional*. Vol 1's own ch0 introduction and Ch.8 disclose this; reviewers should not read the headline without the conditions.

- _Specific Claims_
  - Vol 1 reduces 26 Standard Model parameters to a 3-element bounding set $\{m_e, \alpha, G\}$ + four axioms.
  - **Predicted (axiom-derived):** the cold-lattice asymptote $\alpha^{-1}_{\text{ideal}} = 4\pi^3 + \pi^2 + \pi \approx 137.0363038$ (Ch.8); the existence and sign of a positive thermal running of $\alpha^{-1}$ below this asymptote at $T > 0$; the falsifiable claim that $\alpha^{-1}$ decreases further in regions of higher local thermal energy.
  - **Fitted (one scalar at $T_{\text{CMB}}$):** the numerical magnitude $\delta_{strain} \approx 2.225 \times 10^{-6}$ is back-subtracted from CODATA, definitional given the engine's `DELTA_STRAIN = 1 - (1/ALPHA)/ALPHA_COLD_INV`. The attribution to spatial-metric thermal expansion at $T_{\text{CMB}} = 2.725$ K is a physical narrative consistent with the predicted sign, not a derivation of magnitude.
  - **Tested:** that *one* thermal scalar suffices to bridge the cold-lattice asymptote to CODATA across temperature regimes (collider cores, primordial $\alpha$, ultracold cavity).
- _Specific Non-Claims and Caveats_
  - Does NOT claim full ab-initio derivation of the CODATA $\alpha$ from axioms alone in the current edition. The claim is "structurally zero-parameter conditional on thermal closure of $\delta_{strain}$ at $T_{\text{CMB}}$" — the magnitude of $\delta_{strain}$ from $G_{vac}$ + equipartition is an open derivation, not present in the corpus.
  - Does NOT claim $\ell_{node}$ and $m_e$ are independently derived. Per Ch.8 closure status (c): one of $\{m_e, \ell_{node}\}$ remains the input mass scale; the other follows via the unknot ground state.
  - Summaries that cite "$4\pi^3 + \pi^2 + \pi = 137.0363038$" without the CMB-correction caveat conflate the predicted cold-lattice asymptote with the measured CODATA value (these differ at the ~$2\times 10^{-6}$ level, requiring the fitted $\delta_{strain}$).

> **Leaf references:** [`ch0-intro.md`](./ch0-intro.md) Chapter Summary bullet; [`ch8-alpha-golden-torus.md`](./ch8-alpha-golden-torus.md) "Closure status (honest)" + "Status disclosure (current edition; predicted/fitted split)"; [`axioms-and-lattice/ch1-fundamental-axioms/calibration-cutoff-scales.md`](./axioms-and-lattice/ch1-fundamental-axioms/calibration-cutoff-scales.md).

## Quality
- confidence: 0.70
- solidity: 0.70 (ok to build on, see caveats)
- rationale: Structural reduction of 26 SM parameters to $\{m_e, \alpha, G\}$ + four axioms is sound and explicit; conditionality on $\delta_{strain}$ magnitude derivation, Nyquist-independence proof for $m_e/\ell_{node}$, and $G$ closure independent of $R_H$ is correctly disclosed. No entry-level dependencies — this entry IS the disclosure of the closure conditions.
- strengthen-by:
  - Derive $\delta_{strain}$ magnitude at $T_{CMB}$ from $G_{vac}$ + equipartition (currently back-subtracted from CODATA)
  - Demonstrate Nyquist-resolution-of-smallest-stable-soliton without circular reference to $m_e$ (closes the $\{m_e, \ell_{node}\}$ input scale)
  - Derive $G$ from local thermodynamic balance (lattice tension, equipartition, generation rate per node) independent of $R_H$ (closes the $H_\infty$ identity into a true downstream prediction)

---

## Golden Torus α Derivation (Three-Regime Closure)
<!-- id: 0ktpcn -->

- $\alpha^{-1}_{\text{ideal}} = \Lambda_{\text{vol}} + \Lambda_{\text{surf}} + \Lambda_{\text{line}} = 4\pi^3 + \pi^2 + \pi \approx 137.0363038$
- _Specific Claims_
  - Three independent physical regimes — Nyquist quantization (regime a, $d = 1$), self-avoidance at trefoil crossings (regime b, $R - r = 1/2$), and spin-1/2 half-cover of the standard Clifford torus $\mathbb{T}^2 \subset S^3 \subset \mathbb{C}^2$ (regime c, $R\cdot r = 1/4$) — together fix the Golden Torus geometry $R = \varphi/2$, $r = (\varphi-1)/2$.
  - The $\pi^2$ surface normalization is rigorously forced by topology: $\Lambda_{\text{surf}} = \tfrac{1}{2}A_{\text{standard}} = \pi^2$, where $A_{\text{standard}} = 2\pi^2$ is the standard Clifford-torus surface area on $S^3$ and the half-cover is the spin-1/2 SU(2)$\to$SO(3) double-cover.
  - The $4\pi$ in $\Lambda_{\text{vol}}$ and the half-cover in $\Lambda_{\text{surf}}$ derive from the *same* SU(2) double-cover structure (temporal and spatial expressions of one fact), not as ad hoc separate factors.
  - Numerical convergence is verified by an independent ropelength + Clifford-screening optimization (`ropelength_trefoil_golden_torus.py`) converging from arbitrary starting point to $(R, r) = (\varphi/2, (\varphi-1)/2)$.
- _Specific Non-Claims and Caveats_
  - The sum $\alpha^{-1}_{\text{ideal}} = \Lambda_{\text{vol}} + \Lambda_{\text{surf}} + \Lambda_{\text{line}}$ is an **identification step** (the three orthogonal codimensions of the Clifford embedding map onto the three independent self-impedance contributions), not an additional derivation step. Orthogonality of the three sectors is what justifies the absence of cross-terms; this identification is a non-trivial part of the argument and should not be hand-waved as "obvious".
  - The cold-lattice value $137.0363038$ is the **absolute-zero asymptote**, not the measured CODATA value. CODATA $\alpha^{-1} = 137.035999$ requires the additional CMB-strain correction $\delta_{strain} \approx 2.225\times 10^{-6}$; see Zero-Parameter Closure Status entry above for the predicted/fitted split on $\delta_{strain}$.
  - $\Lambda_{\text{line}} = \pi \cdot d$ takes $\pi$ (not $2\pi$) because regime (b) self-avoidance fixes $d$ as the tube *diameter* (not radius). Summaries that quote $\Lambda_{\text{line}} = \pi$ without this convention warning lose the derivation of why it is not $2\pi$.

> **Leaf references:** [`ch8-alpha-golden-torus.md`](./ch8-alpha-golden-torus.md) Derivation Summary, $\Lambda_{\text{line}}$ derivation, Multipole Decomposition, "Unified axiomatic origin" subsection.

## Quality
- confidence: 0.55
- solidity: 0.55 (use as input only, don't build deeper)
- rationale: Cold-lattice $\alpha^{-1} = 4\pi^3+\pi^2+\pi$ reproduces CODATA to $\sim 10^{-6}$ and the geometry $(R,r) = (\varphi/2, (\varphi-1)/2)$ is forced by intersection of three regimes (corroborated by independent ropelength + Clifford-screening optimization). However, the sum decomposition's orthogonality is asserted, not derived from the axioms — this is the substantive open structural element, which lands the entry at the 0.5 rubric band rather than 0.7. No entry-level dependencies (the identification step is internal to the derivation).
- strengthen-by:
  - Derive orthogonality of the three sum-decomposition sectors ($\Lambda_{\text{vol}}$, $\Lambda_{\text{surf}}$, $\Lambda_{\text{line}}$) from the four axioms; promotes the identification step to a derivation step
  - Derive the SU(2) double-cover identification's role producing both $\Lambda_{\text{surf}}$ halving ($\tfrac{1}{2}\cdot 2\pi^2 = \pi^2$) and the factor 2 in the third slot of $\Lambda_{\text{vol}}$ from a single axiom-grounded mechanism, closing the "two faces of one fact" claim
  - Derive $\delta_{strain}$ magnitude at $T_{CMB}$ to close the cold-lattice → CODATA bridge

---

## EMT $p_c = 8\pi\alpha$ — Consistency Relation, NOT α Derivation
<!-- id: 9s9apq -->

The Ch.2 dielectric-rupture argument shows that the AVE lattice's packing fraction sits at the EMT trace-reversal point ($K = 2G$). It is sometimes summarized as "$\alpha$ from EMT" — this conflation is wrong.

- $p_c = V_{node}/\ell_{node}^3 = 2e^2/(\epsilon_0 \hbar c) \equiv 8\pi\alpha$
- _Specific Claims_
  - Given $\alpha$ from Ch.8, the Schwinger yield density $u_{sat}$ places the lattice at $p_c \approx 0.1834$, which **is** the EMT trace-reversal operating point ($K = 2G$).
  - The 3D amorphous central-force EMT quadratic at $K/G = 2$ uniquely fixes coordination $z_0 \approx 51.25$, which fixes the rigidity threshold $p_G = 6/z_0 \approx 0.117$ — the vacuum operates 56.7% above the fluid–solid transition.
  - The "Over-Bracing Factor" $\mathcal{R}_{OB} = 0.3068/0.1834 \approx 1.673$ implies an effective secondary connectivity reach $r_{\text{secondary}} \approx 1.187\,\ell_{node}$, identifying the substrate as a chiral SRS net (coordination $z = 3$) rather than a Cauchy-Delaunay solid.
- _Specific Non-Claims and Caveats_
  - The identity $p_c = 8\pi\alpha$ is **$\alpha$'s SI definition rearranged via $p_c$**, not an independent derivation of $\alpha$'s numerical value. The $4\pi$ in $\alpha = e^2/(4\pi\epsilon_0 \hbar c)$ cancels the $8\pi$ in the numerator of $p_c$ — the equation is algebraic, not predictive.
  - The Schwinger yield density $u_{sat} = \tfrac{1}{2}\epsilon_0 (m_e^2 c^3/(e\hbar))^2$ is **taken as an external QED input** in this section. Deriving $u_{sat}$ from the four AVE axioms is not attempted here.
  - Read this section as: "given $\alpha$ from Ch.8, the lattice is at the $K = 2G$ point" — not "$\alpha$ is derived from EMT". The EMT argument is downstream of the Golden Torus closure, providing a self-consistency cross-check.

> **Leaf references:** [`axioms-and-lattice/ch2-macroscopic-moduli/dielectric-rupture.md`](./axioms-and-lattice/ch2-macroscopic-moduli/dielectric-rupture.md) (framing paragraphs explicitly call out the consistency-vs-derivation distinction); [`axioms-and-lattice/ch2-macroscopic-moduli/dielectric-snap-limit.md`](./axioms-and-lattice/ch2-macroscopic-moduli/dielectric-snap-limit.md); [`axioms-and-lattice/ch1-fundamental-axioms/zero-parameter-universe.md`](./axioms-and-lattice/ch1-fundamental-axioms/zero-parameter-universe.md).

## Quality
- confidence: 0.85
- depends-on:
  - 0ktpcn — Golden Torus α Derivation (solidity 0.55)
- solidity: 0.47 (use as input only, don't build deeper) [= 0.85 × 0.55]
- rationale: Local work is solid — the entry is correctly scoped, $p_c = 8\pi\alpha$ is algebraically exact, the $K=2G$ operating point with $z_0 \approx 51.25$ from Feng-Thorpe-Garboczi EMT is a sound consistency check given $\alpha$, and non-claims ($u_{sat}$ as external QED input; "$\alpha$ derived from EMT" disclaimer) are explicit. Solidity is bounded by the Golden Torus α Derivation entry (0.55) because every numerical claim here propagates from $\alpha$.
- strengthen-by:
  - Derive $u_{sat}$ from the four AVE axioms (currently taken as external QED input) — would close the only remaining unrepaired input local to this entry
  - Strengthen Golden Torus α Derivation (the dominant solidity bottleneck for this entry; closing its identification-step gap raises this entry's solidity proportionally toward local-confidence 0.85)

---

## $V_{snap}$ vs $V_{yield}$ — Two Distinct Thresholds
<!-- id: 2dwzib -->

- $V_{snap} = m_e c^2/e \approx 511.0$ kV; $V_{yield} = \sqrt{\alpha}\cdot V_{snap} \approx 43.65$ kV
- _Specific Claims_
  - $V_{snap}$ is the **absolute snap limit**: the maximum inter-node potential difference before the lattice structurally ruptures (per-node breakdown).
  - $V_{yield}$ is the **kinetic onset of nonlinearity** (Axiom 2): where saturation effects become dominant and a soliton begins to self-confine.
  - Lab/engineering applications operate near $V_{yield}$, not $V_{snap}$; even the most extreme macroscopic fields ($10^{10}$ V/m) impart $\Delta V_{lab}/V_{snap} \sim 7.5\times 10^{-9}$ across a single node.
- _Specific Non-Claims and Caveats_
  - Conflating $V_{snap}$ and $V_{yield}$ is explicitly catalogued as the first entry in [LIVING_REFERENCE.md "Critical Distinctions"](../../../LIVING_REFERENCE.md). Summaries that cite a single "saturation threshold" without specifying which one are wrong.
  - The Ch.7 regime boundary $r_3 = 1.0$ is the same physical phase transition as the Ch.3 zero-impedance boundary; both correspond to $V_{yield}$, viewed as either trapped-mode standing wave (matter assembly) or super-threshold rupture (topology destroyed). One transition, two faces — not two distinct boundaries.

> **Leaf references:** [`axioms-and-lattice/ch2-macroscopic-moduli/dielectric-snap-limit.md`](./axioms-and-lattice/ch2-macroscopic-moduli/dielectric-snap-limit.md); [`dynamics/ch3-quantum-signal-dynamics/zero-impedance-boundary.md`](./dynamics/ch3-quantum-signal-dynamics/zero-impedance-boundary.md) (explicit Ch.7 reconciliation note); [`operators-and-regimes/ch7-regime-map/four-regimes.md`](./operators-and-regimes/ch7-regime-map/four-regimes.md). Cross-cutting reference: LIVING_REFERENCE.md Critical Distinctions #1.

## Quality
- confidence: 0.95
- depends-on:
  - 0ktpcn — Golden Torus α Derivation (solidity 0.55) [for $V_{yield}$'s $\sqrt{\alpha}$ factor]
- solidity: 0.52 (use as input only, don't build deeper) [= 0.95 × 0.55]
- rationale: Both thresholds are direct consequences of axiom-level definitions — $V_{snap} = m_e c^2/e$ is the per-node energy-equivalent voltage; $V_{yield} = \sqrt{\alpha}\cdot V_{snap}$ follows from Axiom 2. Local distinction work is rock-solid and explicitly catalogued in LIVING_REFERENCE.md Critical Distinction #1. Solidity is bounded by $\alpha$ via $V_{yield}$'s $\sqrt{\alpha}$ factor; $V_{snap}$ alone (depending only on framework inputs) carries solidity ≈ 0.95.
- strengthen-by:
  - Strengthen Golden Torus α Derivation (the only dependency reducing this entry's solidity; closing it lifts $V_{yield}$ numerical solidity to the local-confidence level of 0.95)

---

## ξ vs ξ_topo — Distinct Quantities, Same Greek Letter
<!-- id: 3kzmt9 -->

- $\xi \approx 8.15\times 10^{43}$ (dimensionless Machian hierarchy coupling, Axiom 3); $\xi_{topo} = e/\ell_{node} \approx 4.149\times 10^{-7}$ C/m (electromechanical transduction, Axiom 2 mechanism)
- _Specific Claims_
  - $\xi = 4\pi(R_H/\ell_{node})\alpha^{-2}$ is the cosmological-horizon dilution that converts the un-shielded gravitational coupling ($G_{true} = \hbar c/m_e^2$) into the macroscopic Newton's $G$.
  - $\xi_{topo} = e/\ell_{node}$ is the topological conversion constant grounding the $[Q] \equiv [L]$ isomorphism; it carries dimensions C/m.
- _Specific Non-Claims and Caveats_
  - These are **different quantities sharing a Greek letter**. CLAUDE.md Axiom 3 explicitly flags this and the axiom-definitions leaf carries an inline notation warning.
  - Does NOT claim $\xi$ is independently observable; the Machian dilution factor of $\sim 10^{45}$ between $G_{true}$ and macroscopic $G$ is the "staggering" ratio that motivates the Machian framing — it is a derivation step, not a measurement.

> **Leaf references:** [`axioms-and-lattice/ch1-fundamental-axioms/axiom-definitions.md`](./axioms-and-lattice/ch1-fundamental-axioms/axiom-definitions.md) (notation warning); [`axioms-and-lattice/ch1-fundamental-axioms/lc-condensate-vacuum.md`](./axioms-and-lattice/ch1-fundamental-axioms/lc-condensate-vacuum.md) (un-shielding derivation). Bound also asserted at invariant level: CLAUDE.md Axiom 3 entry.

## Quality
- confidence: 0.90
- depends-on:
  - 0ktpcn — Golden Torus α Derivation (solidity 0.55) [for $\xi$'s $\alpha^{-2}$ factor]
  - 5xon03 — Zero-Parameter Closure Status (solidity 0.70) [for $\xi$'s $R_H/H_\infty$ factor — $H_\infty$ is a consistency identity conditional on $G$ closure]
- solidity: 0.50 (use as input only, don't build deeper) [= 0.90 × min(0.55, 0.70) = 0.90 × 0.55]
- rationale: Local distinction work is correctly enforced — $\xi_{topo} = e/\ell_{node}$ from Axiom 2's topo-kinematic isomorphism mechanism; $\xi = 4\pi(R_H/\ell_{node})\alpha^{-2}$ from Axiom 3's Machian dilution. Solidity bounded by $\alpha$ via $\xi$'s $\alpha^{-2}$ dependency (the tighter bottleneck); the $H_\infty/R_H$ consistency-identity dependency (Closure Status, 0.70) is also active. $\xi_{topo}$'s numerical value alone carries solidity 0.90 (depends only on framework inputs); $\xi$ inherits the dependency chain.
- strengthen-by:
  - Strengthen Golden Torus α Derivation (dominant solidity bottleneck for $\xi$)
  - Close the $H_\infty/R_H$ circularity via independent $G$ derivation (raises Closure Status solidity, tightening $\xi$'s secondary bound)

---

## "True Planck Length = $\ell_{node}$" — Algebraic Consequence, Interpretive
<!-- id: 219e8j -->

- $\ell_{P,\text{true}} = \sqrt{\hbar G_{true}/c^3} \equiv \hbar/(m_e c) = \ell_{node}$
- _Specific Claims_
  - Substituting the un-shielded $G_{true} = \hbar c/m_e^2$ into the standard Planck-length expression algebraically collapses to $\ell_{node}$.
  - The $G/G_{true} \sim 1.75 \times 10^{-45}$ ratio is the cumulative Machian/holographic shielding factor across the cosmological horizon mass.
- _Specific Non-Claims and Caveats_
  - This is an **algebraic identity** within the AVE definition of $G_{true}$, not an independent measurement-versus-prediction comparison. Both sides match because $G_{true}$ is defined to make this hold.
  - The interpretive claim ("$\ell_{node}$ is the true microscopic cutoff, the standard Planck length is a macroscopic-$G$ artifact") is a **framework-internal ontological** statement; it does not introduce new observables vs the standard Planck-length picture at the formula level.
  - See cross-cutting [vol3 Dirac Large Numbers and Planck Mass entry](../vol3/claims-boundaries.md) for the same algebraic-identity caveat applied to $m_P = m_e\sqrt{7\xi}$.

> **Leaf references:** [`axioms-and-lattice/ch1-fundamental-axioms/lc-condensate-vacuum.md`](./axioms-and-lattice/ch1-fundamental-axioms/lc-condensate-vacuum.md).

## Quality
- confidence: 0.95
- solidity: 0.95 (ok to build on)
- rationale: The identity $\ell_{P,\text{true}} = \sqrt{\hbar G_{true}/c^3} \equiv \ell_{node}$ is algebraic given the AVE definition of $G_{true} = \hbar c/m_e^2$, and the entry explicitly discloses this as algebra-not-prediction. The interpretive claim ("$\ell_{node}$ is the true microscopic cutoff") is correctly framed as framework-internal ontology, not a new observable. Depends only on framework inputs ($m_e$, $\hbar$, $c$) and the framework-internal definition of $G_{true}$; no entry-level dependencies that propagate solidity reduction.
- strengthen-by:
  - none — algebraic identity within the framework's existing definitions; the entry is correctly self-bounded as interpretive

---

## Master Equation EFT Validity (Leading-Order Regime)
<!-- id: efo113 -->

- $\nabla^2 V - \mu_0 \varepsilon_0 \sqrt{1 - (V/V_{yield})^2}\,\partial^2 V/\partial t^2 = 0$
- _Specific Claims_
  - The unifying Master Equation is the leading-order long-wavelength EFT obtained by substituting $\varepsilon_{eff}(V)$ into the linear D'Alembert form.
  - In Regime I ($V \ll V_{yield}$): exactly recovers the linear Maxwell-Heaviside wave equation.
  - In the saturation regime: governs particle confinement (magnetic-branch saturation $\mu_{eff} \to 0$, $Z \to 0$, $\Gamma \to -1$, standing wave = rest mass) and the symmetric-gravity refractive index $n(r) = 1 + 2GM/(c^2 r)$.
- _Specific Non-Claims and Caveats_
  - Direct substitution of $\varepsilon_{eff}(V)$ is **exact only in the leading-order EFT regime**. The form drops the field-gradient corrections that arise from $\nabla \cdot \mathbf{D} = \varepsilon_{eff}\nabla\cdot\mathbf{E} + (\nabla\varepsilon_{eff})\cdot\mathbf{E} = 0$. These are subdominant in the linear limit (where $d\varepsilon_{eff}/dV \to 0$); particle-confinement and standing-wave claims at $V \to V_{yield}$ depend on the dropped first-derivative gradient terms remaining negligible by symmetry at saturation.
  - Quantitative claims that depend on the wave-equation **form** near $V_{yield}$ (rather than on the saturation kernel $S$ alone) require a higher-order correction including $\nabla\varepsilon_{eff}\cdot\nabla V$. That correction is not derived in Vol 1.
  - The leaf flags this caveat explicitly; reviewers should not summarize the master equation as "exact" without the EFT qualifier.

> **Leaf references:** [`dynamics/ch4-continuum-electrodynamics/master-equation.md`](./dynamics/ch4-continuum-electrodynamics/master-equation.md) ("Domain of validity (EFT statement)" paragraph).

## Quality
- confidence: 0.50
- solidity: 0.50 (use as input only, don't build deeper)
- rationale: The leading-order EFT form $\nabla^2 V - \mu_0\varepsilon_0 \cdot S \cdot \partial^2 V/\partial t^2 = 0$ is sound and exactly recovers linear Maxwell-Heaviside in Regime I. The particle-confinement and refractive-index claims at saturation depend on the dropped first-derivative gradient terms ($\nabla\varepsilon_{eff}\cdot\nabla V$) remaining negligible by symmetry — this assumption is explicitly disclosed in the leaf but not derived from the axioms, which lands the entry in the 0.5 rubric band. No entry-level dependencies (the unverified-symmetry assumption is internal to the entry's claim space; Axiom 4 is a framework input at solidity 1.0).
- strengthen-by:
  - Derive whether $\nabla\varepsilon_{eff}\cdot\nabla V$ gradient corrections vanish by symmetry at saturation, OR carry the higher-order EFT correction and re-evaluate the particle-confinement and standing-wave claims at $V \to V_{yield}$ with the corrected form

---

## Magnetic-Branch Confinement vs Electric-Branch Rupture
<!-- id: lv3uw1 -->

The two saturation symmetry cases are catalogued in the cross-cutting [Symmetric vs Asymmetric Saturation](../claims-boundaries.md) entry. Vol 1's master-equation leaf is where this distinction is **first introduced** within the volume; Vol 1-specific clarification:

- _Specific Claims_
  - Particle confinement proceeds via the **magnetic branch** (a sub-case of the symmetric sector): at a torus-knot self-intersection, $\mathbf{B}$ saturates $\mu_{eff}$ first, driving $Z = \sqrt{\mu_{eff}/\varepsilon_0} \to 0$ and $\Gamma \to -1$ (short-circuit). The reflected wave traps as a standing mode = invariant rest mass, with no Higgs mechanism invoked.
  - Dielectric rupture (electric breakdown) proceeds via the **asymmetric (electric-only) branch**: $\varepsilon_{eff} \to 0$ with $\mu_{eff}$ intact drives $Z = \sqrt{\mu_0/\varepsilon_{eff}} \to \infty$ — the medium becomes evanescent (no energy transport), not a conductor.
  - Both branches are governed by the **same** kernel $S(A) = \sqrt{1 - (A/A_{yield})^2}$; they differ only in which constitutive parameter saturates first.
- _Specific Non-Claims and Caveats_
  - Does NOT claim the AVE confinement mechanism *competes* with the Higgs mechanism — it is a different ontology (impedance reflection vs gauge-symmetry breaking) reaching the same observable (mass).
  - Does NOT claim the magnetic branch is "asymmetric" in the cross-cutting sense. The magnetic-confinement branch is **a third sub-case of the symmetric sector** (see Ch.7 regime-equation-sets footnote): it saturates $\mu$ rather than $\varepsilon$, but is symmetric in that $Z \to 0$ rather than $Z \to \infty$.
  - For the canonical SYMMETRIC vs ASYMMETRIC tabulation (gravity, BH interior, GW shear vs strong EM), see [cross-cutting](../claims-boundaries.md).

> **Leaf references:** [`dynamics/ch4-continuum-electrodynamics/master-equation.md`](./dynamics/ch4-continuum-electrodynamics/master-equation.md) ("Particle Assembly" sub-bullet); [`operators-and-regimes/ch7-regime-map/regime-equation-sets.md`](./operators-and-regimes/ch7-regime-map/regime-equation-sets.md) (particle-confinement footnote); [`dynamics/ch3-quantum-signal-dynamics/zero-impedance-boundary.md`](./dynamics/ch3-quantum-signal-dynamics/zero-impedance-boundary.md). Cross-cutting: see [Symmetric vs Asymmetric Saturation](../claims-boundaries.md).

## Quality
- confidence: 0.65
- depends-on:
  - efo113 — Master Equation EFT Validity (solidity 0.50)
- solidity: 0.32 (do not build on, rework needed) [= 0.65 × 0.50]
- rationale: The structural classification — magnetic branch as a sub-case of the symmetric sector ($Z \to 0$ via $\mu_{eff} \to 0$); asymmetric/electric branch with $Z \to \infty$ via $\varepsilon_{eff} \to 0$ alone; both governed by the same kernel $S(A)$ — is sound algebra given the impedance and saturation definitions. However, the load-bearing AVE claim — that magnetic-branch confinement at a torus-knot self-intersection IS the mechanism for invariant particle rest mass — depends on the leading-order Master Equation EFT remaining valid through saturation, which itself is asserted-not-derived (gradient corrections negligible by symmetry). The classification alone has local quality ≈ 0.65; the rest-mass mechanism claim transitively inherits Master Equation EFT Validity's 0.50, dropping this entry to 0.32 overall.
- strengthen-by:
  - Strengthen Master Equation EFT Validity (the dominant solidity bottleneck for this entry; closing the gradient-corrections-at-saturation assumption raises this entry's solidity to local-confidence level)
  - Provide an axiom-grounded derivation that the standing-wave reflected mode at $\Gamma \to -1$ quantitatively reproduces invariant rest-mass spectra (currently a structural identification, not a derivation of mass values)

---

## GUP — Independent-Variances Assumption
<!-- id: nq2kcc -->

- $\Delta x_{AVE} = \sqrt{(\Delta x_{SM})^2 + (\ell_{node}/2)^2} \ge \ell_{node}/2$
- _Specific Claims_
  - On a discrete graph with pitch $\ell_{node}$, the canonical momentum is bounded to the Brillouin zone $[-\pi\hbar/\ell_{node}, +\pi\hbar/\ell_{node}]$; the discrete-graph commutator evaluates to $i\hbar\cos(\ell_{node}\hat p_c/\hbar)$.
  - In the low-energy limit $p_c \ll \hbar/\ell_{node}$, the cosine $\to 1$ and standard Heisenberg ($\Delta x\,\Delta p \ge \hbar/2$) is recovered.
  - The **GUP gap** $\ge \ell_{node}/2 \approx 1.93\times 10^{-13}$ m provides a built-in UV regularization — pressure waves cannot be localized below the lattice pitch.
- _Specific Non-Claims and Caveats_
  - The root-sum-square $\Delta x_{AVE} = \sqrt{(\Delta x_{SM})^2 + (\ell_{node}/2)^2}$ assumes the SM continuous-momentum uncertainty and the lattice node-spacing uncertainty are **statistically independent**. The leaf states this assumption explicitly; it is plausible (the SM bound arises in any single Brillouin zone; the lattice floor arises from Nyquist resolution independent of Bloch state) but should not be summarized as a derivation without the independence premise.
  - Does NOT claim the GUP magnitude is independently measurable at the engineering level; $\ell_{node}/2 \sim 10^{-13}$ m is far below current localization-experiment resolution.

> **Leaf references:** [`dynamics/ch3-quantum-signal-dynamics/gup-derivation.md`](./dynamics/ch3-quantum-signal-dynamics/gup-derivation.md).

## Quality
- confidence: 0.70
- solidity: 0.70 (ok to build on, see caveats)
- rationale: The discrete-graph commutator $i\hbar\cos(\ell_{node}\hat p_c/\hbar)$ follows from Brillouin-zone bounds on canonical momentum given Axiom 1's lattice pitch; recovery of standard Heisenberg in the low-energy limit is direct algebra; the GUP gap $\ge \ell_{node}/2$ derives from Nyquist resolution of the lattice. The root-sum-square combination $\Delta x_{AVE} = \sqrt{(\Delta x_{SM})^2 + (\ell_{node}/2)^2}$ explicitly assumes statistical independence of the SM continuous-momentum uncertainty and the lattice node-spacing uncertainty — the leaf flags this as a plausible-but-not-derived assumption (the SM bound arises in any single Brillouin zone; the lattice floor arises from Nyquist resolution independent of Bloch state). Methodology bound is properly disclosed, which lands the entry in the 0.7 rubric band. No entry-level dependencies — $\ell_{node}$ is treated as a framework input.
- strengthen-by:
  - Derive statistical independence of SM continuous-momentum uncertainty and lattice node-spacing uncertainty from the underlying Bloch-state theory of the discrete-graph wavefunction, OR derive the corrected combination rule (covariance-aware) if the variances are not independent

---

## Schrödinger Equation from Paraxial Envelope (Mechanism, Not Independent Derivation)
<!-- id: 7zuwtm -->

- $i\hbar\,\partial_t\Psi = -(\hbar^2/2m)\nabla^2\Psi + V(\mathbf{r})\Psi$ with $V(\mathbf{r}) = \tfrac{1}{2}m c^2\chi(\mathbf{r})$
- _Specific Claims_
  - Klein-Gordon arises as circuit resonance: a localized inductive load with $\omega_m = mc^2/\hbar$ mathematically transforms the Maxwell wave equation into the massive form.
  - Paraxial factoring $\mathbf{A} = \Psi\,e^{-i\omega_m t}$ for non-relativistic $v \ll c$ recovers the free-particle Schrödinger equation.
  - Spatial modulation $\varepsilon_{eff}(\mathbf{r}) = \varepsilon_0[1+\chi(\mathbf{r})]$ in the linear limit ($|\chi| \ll 1$) recovers the full Schrödinger equation with on-site potential $V(\mathbf{r}) = \tfrac{1}{2}mc^2\chi(\mathbf{r})$ — atomic Coulomb wells, applied static fields, and other knot strain fields enter through this same mechanism.
- _Specific Non-Claims and Caveats_
  - The bound-state derivation of $V(\mathbf{r})$ is **leading-order in $|\chi|$** (linear regime). Strong-field cases ($\chi$ approaching saturation) do not reduce to a simple position-dependent potential.
  - Recovery of hydrogenic energy levels $E_n = -m_e c^2\alpha^2/(2n^2)$ from the impedance-matching $2\pi r = n\lambda$ condition is asserted via a Vol 2 cross-reference; the explicit derivation lives in Vol 2 Ch 7, not in this leaf.
  - "No quantum postulates are imported" applies to the *form* of the equation. The Born rule (probability = $|\Psi|^2$) is derived separately in §3.5 from Ohmic measurement work; the two derivations together close the standard QM formalism, but each step is its own claim.

> **Leaf references:** [`dynamics/ch3-quantum-signal-dynamics/schrodinger-from-circuit.md`](./dynamics/ch3-quantum-signal-dynamics/schrodinger-from-circuit.md); [`dynamics/ch3-quantum-signal-dynamics/ohmic-decoherence-born.md`](./dynamics/ch3-quantum-signal-dynamics/ohmic-decoherence-born.md).

## Quality
- confidence: 0.50
- solidity: 0.50 (use as input only, don't build deeper)
- rationale: Paraxial factoring of Klein-Gordon to recover free-particle Schrödinger is standard math; spatial modulation $\varepsilon_{eff}(\mathbf{r})$ recovering on-site potential $V(\mathbf{r})$ is leading-order linear-in-$\chi$ (correctly disclosed). The substantively open element is the Klein-Gordon emergence step itself: a localized inductive load (topological defect with $\omega_m = mc^2/\hbar$) is asserted to produce a spatially uniform $(mc/\hbar)^2 \mathbf{A}$ mass term in the wave equation — but a localized load mathematically produces a localized $\delta(\mathbf{r}-\mathbf{r}_0)$ source, not a uniform background coefficient. This step is asserted by analogy rather than derived, lands the entry at the 0.5 rubric band. No entry-level scored dependencies; the Born rule cross-reference points at a sister leaf (`ohmic-decoherence-born.md`) not yet a separate boundary entry.
- strengthen-by:
  - Derive the spatially uniform Klein-Gordon mass term from the LC network's response to a localized topological defect (e.g., via long-wavelength averaging over distributed knot density, or via spectral analysis showing the localized resonance acts as a uniform background mode for waves in the surrounding medium)
  - Provide the explicit derivation of hydrogenic energy levels from the impedance-matching condition $2\pi r = n\lambda$ (currently cross-referenced to Vol 2 Ch 7, not present in this leaf)
  - Add a separate boundary entry for the Born rule derivation (`ohmic-decoherence-born.md`) so its quality and dependency status are tracked formally rather than implicitly

---

## CHSH Violation $|S|_{\max} = 2\sqrt{2}$ (Tsirelson Bound)
<!-- id: zuf7g1 -->

The phase-locked entanglement-thread leaf derives full quantum-mechanical angular correlations from AVE first principles.

- $E(\hat a, \hat b) = -\cos\theta_{ab}$; $|S|_{\max} = 2\sqrt{2}$ at $\delta = \pi/4$
- _Specific Claims_
  - Three AVE ingredients (spin-1/2 Möbius $\to$ half-angle coupling, Axiom 4 binary saturation outcome, Born rule from Ohmic extraction) yield the Bell correlation $E = -\cos\theta_{ab}$ and the Tsirelson bound $|S|_{\max} = 2\sqrt{2}$ — exactly matching the experimental CHSH violation envelope.
  - The "phase-locked topological thread" is identified as a lossless short-short LC resonator with $Z_0 \approx 377\,\Omega$, $Q = \infty$, fundamental mode $E_1 = \hbar\pi c/d$ (anti-confining: lighter as particles separate).
  - **Falsifiable prediction (distinguishing AVE from standard QM):** entanglement decoherence has a sharp temperature-dependent onset at the pair-creation threshold $T_{pair} = 2m_e c^2/k_B \approx 1.19\times 10^{10}$ K. Below this, only environmental coupling at thread endpoints causes decoherence; above it, the $2\pi$ winding can be unwrapped via spontaneous pair creation. Standard QM has no analogous intrinsic temperature threshold.
  - K4-TLM lattice simulation confirms vacuum and $T \ll T_{pair}$ noise scenarios are statistically indistinguishable (winding is topologically protected); $T \gg T_{pair}$ noise destroys the winding.
- _Specific Non-Claims and Caveats_
  - Does NOT claim CHSH violation > $2\sqrt{2}$; the AVE result hits the Tsirelson bound exactly, **the same** as standard QM. CHSH is **not** an experimental discriminator between AVE and QM at any laboratory temperature.
  - The no-signalling theorem is preserved (Bob's marginal is $1/2$ regardless of Alice's setting); the "topological thread" is **not** a faster-than-light communication channel.
  - The decoherence-temperature falsifiability is currently testable only in quark-gluon plasma / heavy-ion environments at $\sim 10^{12}$ K; standard cryogenic decoherence experiments operate at $T \ll T_{pair}$ where AVE and standard QM make identical predictions.
  - "Mechanically identical to the Meissner effect" is a structural identification (same saturation operator $S$ at $\Gamma \to -1$), not a literal claim that entanglement *is* superconductivity.

> **Leaf references:** [`dynamics/ch3-quantum-signal-dynamics/phase-locked-topological-thread.md`](./dynamics/ch3-quantum-signal-dynamics/phase-locked-topological-thread.md); [`dynamics/ch3-quantum-signal-dynamics/ohmic-decoherence-born.md`](./dynamics/ch3-quantum-signal-dynamics/ohmic-decoherence-born.md).

## Quality
- confidence: 0.60
- solidity: 0.60 (use as input only, don't build deeper)
- rationale: The Bell correlation $E(\hat a, \hat b) = -\cos\theta_{ab}$ and the Tsirelson bound $|S|_{\max} = 2\sqrt{2}$ emerge as algebra given three AVE ingredients (spin-1/2 Möbius half-angle coupling, Axiom 4 binary saturation at measurement, Born rule from Ohmic extraction); hitting Tsirelson exactly is significant corroboration. The substantive open element is the structural identification "phase-locked topological thread = lossless short-short LC resonator implementing the Bell correlation" — this is asserted as a constructive picture, not derived from axioms. The decoherence-onset prediction at $T_{pair} \approx 1.19 \times 10^{10}$ K is genuinely falsifiable (in QGP regimes). No entry-level scored dependencies; Born rule and spin-1/2 Möbius cross-references point at sister leaves not yet boundary entries.
- strengthen-by:
  - Derive the structural identification "phase-locked topological thread = lossless short-short LC resonator with $Z_0 \approx 377\,\Omega$, $Q = \infty$" from first principles (currently asserted as a constructive identification of the Bell-correlation carrier)
  - Document the spin-1/2 Möbius half-angle coupling derivation explicitly (currently summarized; the Finkelstein-Misner kink construction needs to be present here or pointed at an explicit derivation leaf)
  - Add a separate boundary entry for the Born rule derivation so the dependency chain is fully scored

---

## Quantum Foam as RMS Noise; Virtual Particles as Failed Topologies
<!-- id: t1okz0 -->

- _Specific Claims_
  - The "Quantum Foam" of standard cosmology is reframed as the irreducible thermal RMS noise floor of the LC network at $T > 0$ — the chaotic baseline electrical AC transients, not a literal boiling of geometry.
  - "Virtual particles" are reframed as **failed topologies**: transient localized phase twists from thermal node noise that lack the sustained inductive tension to close into a stable unknot, unwinding back into the noise floor.
  - This provides a deterministic mechanical origin for Zero-Point Energy bounded by the finite local node geometry.
- _Specific Non-Claims and Caveats_
  - Does NOT claim AVE solves the Cosmological Constant Problem at the formula level — the leaf cites the $\sim 120$-orders-of-magnitude discrepancy as motivation, but does not derive the observed dark energy density from the noise-floor reframing in this leaf. Cosmological-constant resolution lives in the Vol 3 dark-energy / phantom-energy chain (lattice latent-heat reinterpretation), not in Vol 1 Ch.3.
  - The "failed topologies" picture is **interpretive**; it does not produce new observables relative to standard QFT virtual-particle calculations at the perturbative level. Falsifiability rests on unrelated AVE predictions (running $\alpha$, GUP cutoff, etc.), not on the foam-as-noise reframing per se.

> **Leaf references:** [`dynamics/ch3-quantum-signal-dynamics/quantum-foam-virtual.md`](./dynamics/ch3-quantum-signal-dynamics/quantum-foam-virtual.md).

## Quality
- confidence: 0.70
- solidity: 0.70 (ok to build on, see caveats)
- rationale: The reframe — "Quantum Foam = irreducible thermal RMS noise of the LC network at $T > 0$" and "virtual particles = failed topologies (transient phase twists lacking sustained inductive tension to close into stable unknots)" — is a coherent ontological reinterpretation given Axiom 1's discrete LC network. The boundary entry correctly self-bounds: this is interpretive, not a new prediction; doesn't claim cosmological-constant resolution at the formula level; falsifiability rests on unrelated AVE predictions. Methodology is properly disclosed, lands the entry at the 0.7 rubric band. No entry-level scored dependencies.
- strengthen-by:
  - Quantitatively map AVE thermal-noise-floor predictions to specific QFT virtual-particle calculations at the perturbative level, establishing operational equivalence (or producing a falsifiable divergence)
  - Connect to the Vol 3 dark-energy / phantom-energy chain to clarify what the "failed topologies" reframe predicts (vs reframes) about cosmological-constant magnitude

---

## Asymptotic Hubble Constant $H_\infty$ and MOND $a_0$ (Vol 1 Derivation; Cross-Cutting Caveats)
<!-- id: m3z5ux -->

Vol 1 Ch.4.5 contains the original $H_\infty = 28\pi m_e^3 cG/(\hbar^2\alpha^2) \approx 69.32$ km/s/Mpc derivation and the MOND $a_0 = cH_\infty/(2\pi) \approx 1.07\times 10^{-10}$ m/s² hoop-stress projection. The substantive boundary caveats are catalogued in the [vol3 Asymptotic Hubble Constant entry](../vol3/claims-boundaries.md) and [vol3 MOND Acceleration Scale entry](../vol3/claims-boundaries.md). Vol 1-specific notes:

- _Specific Claims_
  - The two formulae are derived once in Vol 1 Ch.4.5 from the canonical hardware scales $\{\ell_{node}, \alpha, G\}$ + the Unruh-Hawking de Sitter horizon temperature; downstream chapters reuse them.
  - The hoop-stress projection $a_{genesis} = a_r/(2\pi)$ applies the classical continuum-mechanics result $T = F_r/(2\pi)$ to a 1D closed topological loop embedded in a 3D radially expanding manifold.
- _Specific Non-Claims and Caveats_
  - The Hubble-derivation "geometric-consistency-proof" caveat (the Machian $\xi$ embeds $R_H \equiv c/H_\infty$ in the definition of $G$) lives in the Vol 3 lattice-genesis leaf, not in Vol 1 Ch.4.5. The Vol 1 derivation should not be summarized as an independent ab-initio prediction of $H_0$ without consulting the Vol 3 boundary entry.
  - The MOND $a_0$ deficit (-10.7%) and the Pitfall #4 (no MOND drag at high $g$, $S(g_N/a_0) = 0$ when $g_N \gg a_0$) are documented in detail in the vol3 sidecar; flagged here because Vol 1 introduces the formula.
  - Vol 1 dark-sector framings ("Bullet Cluster as decoupled refractive shockwave"; "DAMA/LIBRA vs XENON as transverse-shear impedance mismatch") are **interpretive reinterpretations**, not quantitative predictions. They reframe established observations within the LC-substrate ontology but do not output new numerical values to test.

> **Leaf references:** [`dynamics/ch4-continuum-electrodynamics/mond-hoop-stress.md`](./dynamics/ch4-continuum-electrodynamics/mond-hoop-stress.md); [`dynamics/ch4-continuum-electrodynamics/dark-sector.md`](./dynamics/ch4-continuum-electrodynamics/dark-sector.md); [`dynamics/ch4-continuum-electrodynamics/bullet-cluster.md`](./dynamics/ch4-continuum-electrodynamics/bullet-cluster.md). Cross-cutting boundary detail in [vol3 Asymptotic Hubble Constant and MOND entries](../vol3/claims-boundaries.md).

## Quality
- confidence: 0.60
- depends-on:
  - 0ktpcn — Golden Torus α Derivation (solidity 0.55) [for $H_\infty$'s $\alpha^{-2}$ factor]
  - 5xon03 — Zero-Parameter Closure Status (solidity 0.70) [for the consistency-proof framing of $H_\infty$]
- solidity: 0.33 (do not build on, rework needed) [= 0.60 × min(0.55, 0.70) = 0.60 × 0.55]
- rationale: The $H_\infty = 28\pi m_e^3 cG/(\hbar^2\alpha^2)$ formula is correctly disclosed as a consistency-proof, not an independent ab-initio prediction (Machian $\xi$ embeds $R_H \equiv c/H_\infty$ in $G$'s definition; one identity in $(G, H_\infty)$, not two). The MOND $a_0 = cH_\infty/(2\pi)$ hoop-stress projection produces a $-10.7\%$ deficit vs empirical $1.2\times 10^{-10}$ m/s² — a real numerical gap. Local confidence is held below 0.7 because the underlying `mond-hoop-stress.md` leaf carries an unresolved longitudinal wave-speed formula ($v_L = \sqrt{2G/\rho} = \sqrt{2}c$ vs standard isotropic-elasticity $v_L = c\sqrt{10/3} \approx 1.826c$ for $K=2G$), and the hoop-stress projection factor $1/(2\pi)$ is asserted from classical continuum mechanics rather than derived from AVE micropolar dynamics.
- strengthen-by:
  - Resolve the longitudinal wave speed formula in `mond-hoop-stress.md` (currently $\sqrt{2}c$; standard isotropic elasticity at $K=2G$ gives $c\sqrt{10/3}$); either derive the AVE-specific formula from the micropolar / chiral LC continuum (which decouples transverse propagation from bulk modulus) or correct the leaf
  - Derive the hoop-stress projection factor $1/(2\pi)$ from AVE's micropolar dynamics rather than importing the classical continuum-mechanics result
  - Close the MOND $a_0$ -10.7% deficit by carrying higher-order corrections OR by re-deriving the hoop-stress geometry from AVE first principles
  - Strengthen Golden Torus α Derivation (`0ktpcn`); the $\alpha^{-2}$ factor in $H_\infty$ amplifies α's solidity into the strongest dependence
  - Close the Hubble identity into a true downstream prediction by deriving $G$ from local thermodynamic balance independent of $R_H$ (echoes the Closure Status entry)

---

## Macroscopic Yield Stress $\tau_{yield}$ — Order-of-Magnitude Bound, Not Precision
<!-- id: 8ep2b4 -->

- $\tau_{yield} = (\rho_{bulk} c^2)\cdot(6\,\mathcal{V}_{crossing})\cdot(p_c/8\pi) \approx 1.04\times 10^{22}$ Pa
- _Specific Claims_
  - The macroscopic yield stress is constructed from baseline bulk energy density $\rho_{bulk}c^2$, the per-crossing topological halo volume ($6\,\mathcal{V}_{crossing} = \mathcal{V}_{total} = 2.0$, FEM-verified to 0.13%), and the geometric porosity factor $\alpha = p_c/8\pi$.
  - The Sagnac-RLVE rotational-shear interferometer is proposed as a tabletop falsification test; the predicted phase shift scales with rotor density and shear rate, distinct from Lense-Thirring (which scales with Newtonian potential).
- _Specific Non-Claims and Caveats_
  - The "Asteroid Belt / Oort Cloud as transition traps at the saturation isocline" framing is an **interpretive prediction**, not a quantitative match to observed orbital-debris distributions. Specific numerical agreement (where present) lives in the vol3 solar-system entries.
  - The Sagnac-RLVE proposal requires the $1000:1$ asymmetric chevron geometry (1 µm tips against 1 mm troughs). The expected phase-shift magnitude is not given in this leaf; falsifiability is asserted in principle, not characterized in detail.
  - "Mutual inductance is annihilated ($\eta \to 0$) inside saturated regions" is the same claim as cross-cutting Symmetric Saturation ($Z = Z_0$ invariant, $\Gamma = 0$); it is not "drag goes to zero from infinity" — drag is bounded and structured throughout the regimes.

> **Leaf references:** [`dynamics/ch4-continuum-electrodynamics/magnetic-saturation.md`](./dynamics/ch4-continuum-electrodynamics/magnetic-saturation.md). Cross-cutting: see Symmetric vs Asymmetric Saturation.

## Quality
- confidence: 0.50
- depends-on:
  - 0ktpcn — Golden Torus α Derivation (solidity 0.55) [for $p_c = 8\pi\alpha$ in the porosity factor]
- solidity: 0.28 (do not build on, rework needed) [= 0.50 × 0.55]
- rationale: The formula $\tau_{yield} = (\rho_{bulk} c^2)\cdot(6\,\mathcal{V}_{crossing})\cdot(p_c/8\pi)$ uses the proton-specific Borromean topology ($\mathcal{V}_{total} = 6\,\mathcal{V}_{crossing} = 2.0$, FEM-verified to 0.13% for the proton's 6³₂ Borromean) as a load-bearing factor in a formula presented as governing **macroscopic / cosmological** lattice mechanics (planetary slipstreams, asteroid belts, dark-sector boundary-layer transitions). The justification for embedding proton-specific topology in a macroscopic vacuum formula is asserted, not derived — this is the substantive open structural question that lands the entry at the 0.5 rubric band. Order-of-magnitude framing is correctly disclosed; quantitative claims (specific $1.04\times 10^{22}$ Pa value, asteroid-belt / Oort-cloud isocline matching) are interpretive at this scope.
- strengthen-by:
  - Justify (or replace) the use of proton-specific 6-crossing Borromean topology ($\mathcal{V}_{total} = 2.0$) in a formula governing macroscopic / cosmological lattice mechanics; either derive why proton topology is universally embedded in the macroscopic vacuum, or replace with a generic topological factor derived from lattice properties alone
  - Quantify the predicted Sagnac-RLVE phase shift (currently "asserted in principle, not characterized in detail")
  - Quantitatively match "asteroid belt / Oort cloud" formation positions to $\tau_{yield}$ isoclines (currently interpretive, not numerical)
  - Strengthen Golden Torus α Derivation (`0ktpcn`); $p_c = 8\pi\alpha$ enters the formula

---

## Universal Spatial Tension Mass Scaling (Lepton + Nuclear)
<!-- id: zw6mut -->

- $M_{topo} = (\hbar/c)/\oint \vec r_{ij}\cdot d\vec\ell$
- _Specific Claims_
  - The same $1/r$ universal tension governs both lepton mass hierarchies and nuclear pairwise binding. Three Cosserat sectors (translation, rotation, curvature-twist) produce three lepton generations:
    - Electron: ground-state unknot, $m_e = \hbar/(c\,\ell_{node})$ (definitional).
    - Muon: torsion sector $\alpha\sqrt{3/7}$, $m_\mu \approx 107.0$ MeV ($+1.24\%$ vs CODATA).
    - Tau: curvature sector $8\pi/\alpha$, $m_\tau \approx 1760$ MeV ($-0.95\%$).
  - Nuclear binding uses the same operator: Neon-20 = $5\alpha$ Triangular Bipyramid with $K_{mutual} = m_p c^2$ summed over the 10 pairwise $\binom{5}{2}$ inductive links.
- _Specific Non-Claims and Caveats_
  - The Neon-20 result is **NOT zero-parameter ab initio**. Per the leaf's explicit "Methodology disclosure": within the $(Z,A)$-forced bipyramid topology, the inter-alpha distance $R_{bipyramid}$ is **the single fitted scalar adjusted per nucleus**. The optimizer converges at $R_{bipyramid} \approx 81.158\,d$.
  - The reported $<0.001\%$ Neon-20 residual is the **optimizer's convergence tolerance on $R$**, not an independent prediction error on the mass.
  - The falsifiable axiomatic content of the nuclear chain is: (1) cluster topology as a function of $(Z,A)$ via minimum-impedance packing, (2) coupling $K_{mutual} = m_p c^2$, and (3) the parameter count = one scalar per nucleus (vs $\sim 5$ in liquid-drop / shell models). This is **the** Vol 6 methodology; the Vol 1 Neon-20 mention is one application, not a demonstration of zero-parameter nuclear masses.
  - Lepton-mass derivations are quoted with errors ($+1.24\%$, $-0.95\%$). These are not sub-percent; summary tables that drop the error column over-claim. The full Cosserat-sector derivation lives in Vol 2 Ch 5; Vol 1 provides the headline result.

> **Leaf references:** [`operators-and-regimes/ch5-universal-spatial-tension/mass-unification.md`](./operators-and-regimes/ch5-universal-spatial-tension/mass-unification.md); [`operators-and-regimes/ch5-universal-spatial-tension/scale-invariance.md`](./operators-and-regimes/ch5-universal-spatial-tension/scale-invariance.md) (explicit Methodology disclosure paragraph); [`operators-and-regimes/ch5-universal-spatial-tension/scale-invariant-predictions.md`](./operators-and-regimes/ch5-universal-spatial-tension/scale-invariant-predictions.md).

## Quality
- confidence: 0.60
- depends-on:
  - 0ktpcn — Golden Torus α Derivation (solidity 0.55) [for muon's $\alpha\sqrt{3/7}$ and tau's $8\pi/\alpha$ sector factors]
- solidity: 0.33 (do not build on, rework needed) [= 0.60 × 0.55]
- rationale: The cross-scale operator framing — same universal $1/r$ tension governs lepton and nuclear binding — is structurally claimed but the three-Cosserat-sector-to-three-lepton-generation identification (translation/torsion/curvature-twist) is asserted, not derived from the four axioms. Lepton-mass deviations are non-trivial: muon $+1.24\%$, tau $-0.95\%$ — correctly disclosed but not sub-percent. Nuclear methodology is honestly disclosed as **one fitted scalar per nucleus** (Vol 6); the Vol 1 Neon-20 mention is one application. The reported "$<0.001\%$ Neon-20 residual" is the optimizer convergence tolerance, not an independent prediction error — boundary entry correctly flags this. Local confidence held at 0.6 because the structural identifications and the residual lepton-mass percentages are real open work.
- strengthen-by:
  - Derive the three-Cosserat-sectors-to-three-lepton-generations identification (translation/torsion/curvature-twist) from the four axioms (currently a structural identification with sector-specific coupling factors $\alpha\sqrt{3/7}$ and $8\pi/\alpha$ that are asserted, not derived)
  - Reduce the lepton-mass deviations (muon $+1.24\%$, tau $-0.95\%$) by carrying higher-order corrections in the Cosserat sector chain
  - Strengthen Golden Torus α Derivation (`0ktpcn`); α appears in both muon and tau sector factors
  - Add a separate boundary entry for the proton mass derivation; it feeds the Vol 6 nuclear methodology and the Vol 1 Neon-20 application as an unscored upstream input

---

## Universal Operators (Z, S, Γ) — Same Function, Different Scales
<!-- id: gdd70j -->

The eight Ch.6 universal operators are the engine-level shared code paths. Boundary entries:

- _Specific Claims_
  - Each operator (Z impedance, S saturation, Γ reflection, U pairwise, Y→S multiport, $\lambda_{\min}$ eigenvalue target, FFT spectral, $\Gamma_{pack}$ packing) is implemented as **one function** called by every domain — the cross-scale identity is computational, not analogical.
  - The cross-scale Z table spans 8 distinct domains (vacuum lattice, plasma, seismic, gravitational, protein, lattice-Boltzmann fluid, galactic, antenna), all routed through `scale_invariant.impedance(mu, eps)`.
- _Specific Non-Claims and Caveats_
  - Operator-identity claims are **structural** (same code path), not predictive at any single scale. Numerical agreement at any specific application is the responsibility of the per-domain leaf, not the operator's universal status.
  - The "Universal Reflection Coefficient" cross-scale list (Pauli exclusion at $\Gamma = -1$, Moho seismic $\Gamma \approx 0.17$, antenna $S_{11}$, etc.) exemplifies this: same operator, different inputs $(Z_1, Z_2)$, different physical phenomena. Summaries that quote a list of $\Gamma$ values as "AVE predicts" should be qualified with "the operator is universal; the inputs come from per-domain physics".
  - Cross-cutting [vol3 Seismic Reflection Coefficient (Moho) entry](../vol3/claims-boundaries.md) makes this distinction explicit.

> **Leaf references:** [`operators-and-regimes/ch6-universal-operators/impedance-operator.md`](./operators-and-regimes/ch6-universal-operators/impedance-operator.md); [`operators-and-regimes/ch6-universal-operators/saturation-operator.md`](./operators-and-regimes/ch6-universal-operators/saturation-operator.md); [`operators-and-regimes/ch6-universal-operators/reflection-coefficient.md`](./operators-and-regimes/ch6-universal-operators/reflection-coefficient.md); [`operators-and-regimes/ch6-universal-operators/pairwise-potential.md`](./operators-and-regimes/ch6-universal-operators/pairwise-potential.md).

## Quality
- confidence: 0.80
- solidity: 0.80 (ok to build on, see caveats)
- rationale: The eight universal operators (Z, S, Γ, U, Y→S, λ_min, FFT, Γ_pack) are framework-level constructs derived from Axiom 4's saturation kernel and from impedance/reflection algebra; the cross-scale identity is **structural** (same code path called by every domain), not predictive at any single scale. The boundary entry correctly self-bounds — operator identity claims do not certify per-domain numerical agreement, which is the responsibility of each per-domain leaf. This separation of concerns is exactly right; the entry's only caveat is that summaries which list cross-domain $\Gamma$ values as "AVE predicts" are misreading the structural-identity claim. No entry-level scored dependencies — operators are framework-level.
- strengthen-by:
  - none entry-local — per-domain numerical validations live in their own boundary entries; this entry's claim is just the operator-reuse structural identity, which is correctly bounded

---

## Four-Regime Map — Boundary Derivations are Sector-Dependent
<!-- id: b2anl4 -->

- $r_1 = \sqrt{2\alpha} \approx 0.121$ (Linear → Nonlinear); $r_2 = \sqrt{3}/2 \approx 0.866$ (Nonlinear → Yield, **spin-2 sector**); $r_3 = 1$ (Yield → Ruptured)
- _Specific Claims_
  - $r_1 = \sqrt{2\alpha}$ is derived: the leading Taylor correction $\Delta S = r^2/2$ equals the lattice's own self-coupling $\alpha$ at this point — sub-$\alpha$ corrections are physically unresolvable.
  - $r_3 = 1$ is axiomatic from Axiom 4 ($S = 0$, topology destroyed).
  - The $r_2 = \sqrt{3}/2$ boundary derives from $Q = 1/S = \ell_{\min}$ with $\ell_{\min} = 2$ for the **spin-2 sector** (gravitational waves, shear modes; minimum non-trivial multipole).
- _Specific Non-Claims and Caveats_
  - $r_2 = \sqrt{3}/2$ is **sector-dependent**, not universal. Other sectors have different $\ell_{\min}$ and thus different $r_2$:
    - Scalar sector ($\ell_{\min} = 0$): no avalanche-onset boundary in this sector; practical onset is set by other physics.
    - Photon / vector sector ($\ell_{\min} = 1$): $r_2 = 0$ (avalanche concurrent with linear breakdown); no separate Regime III.
    - Spin-2 sector ($\ell_{\min} = 2$): $r_2 = \sqrt{3}/2$ as derived.
  - The "universal regime map" framing in chapter titles is the **spin-2 form**; the lower-spin sectors collapse two boundaries together. Citations of $r_2 = \sqrt{3}/2$ without sector qualification implicitly assume spin-2.
  - The semiconductor analogy (Miller factor $M$, avalanche multiplication) is a **structural identity** (same $S$ operator), not a derivation of semiconductor breakdown from AVE axioms.

> **Leaf references:** [`operators-and-regimes/ch7-regime-map/four-regimes.md`](./operators-and-regimes/ch7-regime-map/four-regimes.md) (sector-dependence note); [`operators-and-regimes/ch7-regime-map/regime-equation-sets.md`](./operators-and-regimes/ch7-regime-map/regime-equation-sets.md); [`operators-and-regimes/ch7-regime-map/domain-catalog.md`](./operators-and-regimes/ch7-regime-map/domain-catalog.md).

## Quality
- confidence: 0.75
- depends-on:
  - 0ktpcn — Golden Torus α Derivation (solidity 0.55) [for $r_1 = \sqrt{2\alpha}$ numerical value]
- solidity: 0.41 (do not build on, rework needed) [= 0.75 × 0.55]
- rationale: The boundary derivations are individually sound — $r_1 = \sqrt{2\alpha}$ from leading-order Taylor truncation of $S(r)$ matching the lattice's self-coupling $\alpha$; $r_3 = 1$ axiomatic from Axiom 4 ($S = 0$); $r_2 = \sqrt{3}/2$ from $Q = 1/S = \ell_{\min}$ with $\ell_{\min} = 2$ for the spin-2 sector. The substantive open element is the **sector-specific identification of $\ell_{\min}$** (scalar/vector/spin-2 ℓ_min values are stated as "minimum non-trivial multipole" rather than derived from a specific axiom-grounded harmonic decomposition). Local confidence held at 0.75. Solidity bounded by α via $r_1$'s numerical value. The structural form $r_1 = \sqrt{2\alpha}$ survives any reasonable α value; the **numerical** boundary at 0.121 is α-dependent.
- strengthen-by:
  - Derive the sector-specific $\ell_{\min}$ values (scalar 0, vector 1, spin-2 2, ...) from axiom-grounded multipole decomposition rather than pattern-matching to "minimum non-trivial multipole"
  - Strengthen Golden Torus α Derivation (`0ktpcn`); $r_1 = \sqrt{2\alpha}$ inherits α's solidity for numerical evaluation

---

## Domain Catalog Operating-Point Examples
<!-- id: 82dxbj -->

The Ch.7.2 domain catalog tabulates $r$ values across EM, gravitational, BCS, magnetic, nuclear, GW, and galactic domains. Vol 1-specific tripwires:

- _Specific Claims_
  - Solar surface, white dwarf interiors, lab capacitors and magnets, MRI scanners, LIGO GW signals: all explicitly sit deep in **Regime I** ($r \ll 1$), justifying use of unmodified standard equations.
  - Neutron star at $1.4\,M_\odot$, $R = 10$ km: $\varepsilon_{11} \approx 1.46 > 1$ — **Regime IV** (ruptured topology). This is the AVE analog of the Buchdahl limit.
  - Black hole at $r_s = 2GM/c^2$: $\varepsilon_{11} = 7/2 = 3.5$ (the factor 7 arises from the K4/SRS lattice's 7 compliance modes via $\nu_{vac} = 2/7$). Deep Regime IV.
  - LIGO GW150914 strain $h \sim 10^{-21}$ corresponds to $r \sim 10^{-20}$ — "the most deeply linear measurement in physics".
- _Specific Non-Claims and Caveats_
  - The neutron-star Regime IV identification (lattice-strain $> 1$) is **the AVE-internal compactness bound**; the cross-cutting [vol3 AVE Compactness Limit entry](../vol3/claims-boundaries.md) elaborates that this is stricter than the GR Buchdahl bound but is **not** validated against observed neutron-star equations of state. It is what the AVE bound implies given canonical NS parameters.
  - The galactic-domain operating point uses the empirical $a_0 \approx 1.2\times 10^{-10}$ m/s², not the AVE-derived $a_0 \approx 1.07\times 10^{-10}$. Mixing the two leads to inconsistent regime locations.
  - LIGO's "sub-$\alpha$" classification (the $\Delta S = 0.007$ correction at NS-merger surface strain $h \sim 0.01$ is below the lattice's own $\alpha \sim 1/137$ coupling) means AVE corrections are **physically unresolvable** at LIGO sensitivities — not zero, but below the noise floor of the lattice itself.

> **Leaf references:** [`operators-and-regimes/ch7-regime-map/domain-catalog.md`](./operators-and-regimes/ch7-regime-map/domain-catalog.md); [`operators-and-regimes/ch7-regime-map/experimental-design-space.md`](./operators-and-regimes/ch7-regime-map/experimental-design-space.md). Cross-cutting: [vol3 AVE Compactness Limit](../vol3/claims-boundaries.md).

## Quality
- confidence: 0.70
- depends-on:
  - b2anl4 — Four-Regime Map (solidity 0.41) [uses $r_1, r_2, r_3$ boundaries to classify domains]
- solidity: 0.29 (do not build on, rework needed) [= 0.70 × 0.41]
- rationale: The catalog correctly applies the four-regime structure to specific physical systems (Solar surface, WD interiors, lab fields, NS interior, BH horizons, LIGO GW signals); the boundary entry honestly discloses that the AVE-internal compactness bound ($R_{\min} = 7GM/c^2$) is stricter than the GR Buchdahl bound but is **not validated** against observed neutron-star equations of state, and that the galactic-domain operating point uses empirical $a_0$ (not AVE-derived). Local confidence is sound for the application work. Solidity is heavily bounded transitively through Four-Regime Map's α dependency — every $r$ value tabulated for a specific system inherits regime-boundary numerical solidity.
- strengthen-by:
  - Validate the AVE-internal compactness bound ($R_{\min} = 7GM/c^2$) against observed neutron-star equations of state (currently disclosed as not-validated)
  - Reconcile the galactic operating-point's use of empirical $a_0 \approx 1.2\times 10^{-10}$ with the AVE-derived $a_0 \approx 1.07\times 10^{-10}$ from Asymptotic Hubble Constant + MOND (`m3z5ux`); using empirical introduces an undeclared empirical input
  - Strengthen Four-Regime Map (`b2anl4`); regime-boundary numerical solidity propagates here
  - Strengthen Golden Torus α Derivation (`0ktpcn`) transitively

---

## Vacuum Bulk Mass Density and Shear Modulus
<!-- id: crbl60 -->

- $\rho_{bulk} = \xi_{topo}^2\mu_0/(p_c\ell_{node}^2) \approx 7.92\times 10^6$ kg/m³; $G_{vac} = \rho_{bulk}c^2 \approx 7.11\times 10^{23}$ Pa
- _Specific Claims_
  - The dimensionally-corrected bulk mass density is derived via $L = \xi_{topo}^{-2}m$ inductance-mass isomorphism + Voronoi cell volume $V_{node} = p_c\ell_{node}^3$.
  - $G_{vac}$ is the macroscopic 3D shear modulus of $\mathcal{M}_A$; the Cauchy bulk modulus is fixed at $K_{vac} = 2G_{vac}$ (Cauchy relation for the isotropic lattice).
  - Kinematic mutual inductance $\nu_{kin} = \alpha c\,\ell_{node} \approx 8.45\times 10^{-7}$ m²/s — close to liquid water's value, asserted as parameter-free with the identification $\kappa \equiv \alpha$.
- _Specific Non-Claims and Caveats_
  - $G_{vac}$ (3D continuum shear modulus, $\sim 10^{23}$ Pa) must NOT be confused with $G_{string} = T_{EM}/\ell_{node} \approx 5.49\times 10^{11}$ N/m (1D string tension modulus, governing single-edge stiffness). These differ by $\sim 10^{12}$; the leaf flags this distinction explicitly.
  - The $\nu_{kin}$ "close to liquid water" comparison is an order-of-magnitude consistency observation, not a derivation that the vacuum *behaves like* water in any operationally relevant sense.
  - The identification $\kappa \equiv \alpha$ (geometric scattering threshold = packing-fraction-derived self-coupling) is **asserted** in the leaf as a consequence of the porosity argument; reviewers should treat it as a structural claim, not as an independent measurement of $\kappa$.

> **Leaf references:** [`dynamics/ch4-continuum-electrodynamics/lc-electrodynamics.md`](./dynamics/ch4-continuum-electrodynamics/lc-electrodynamics.md).

## Quality
- confidence: 0.65
- depends-on:
  - 0ktpcn — Golden Torus α Derivation (solidity 0.55) [for $p_c = 8\pi\alpha$ in $\rho_{bulk}$ and $\alpha$ in $\nu_{kin} = \alpha c \ell_{node}$]
- solidity: 0.36 (do not build on, rework needed) [= 0.65 × 0.55]
- rationale: $\rho_{bulk}$ and $G_{vac} = \rho_{bulk}c^2$ are dimensionally constructed from $\xi_{topo}$, $\mu_0$, $p_c$, $\ell_{node}$, $c$ — the construction itself is sound algebra. The Cauchy relation $K_{vac} = 2G_{vac}$ is the same operating point disclosed in the EMT entry and is structurally consistent. The substantive open element is the **identification $\kappa \equiv \alpha$** for the kinematic mutual inductance $\nu_{kin}$ — asserted as a consequence of the porosity argument but not derived. The "$\nu_{kin}$ close to liquid water" comparison is order-of-magnitude only. The distinction $G_{vac}$ (3D continuum) vs $G_{string}$ (1D edge tension, $\sim 10^{12}$ smaller) is correctly disclosed.
- strengthen-by:
  - Derive the $\kappa \equiv \alpha$ identification (geometric scattering threshold = packing-fraction-derived self-coupling) from first principles rather than asserting
  - Strengthen Golden Torus α Derivation (`0ktpcn`); $\rho_{bulk}$, $G_{vac}$, and $\nu_{kin}$ all inherit α numerically through $p_c$ and $\nu_{kin}$'s factor

---

## Implosion Paradox $\to$ Micropolar Vacuum
<!-- id: 9gh0a1 -->

- _Specific Claims_
  - A classical Cauchy elastic solid satisfying MacCullagh's transverse-wave condition ($\lambda = -\mu$) yields $K = -\mu/3 < 0$ — runaway implosion.
  - This forces the substrate to be a **Chiral LC (Micropolar) Continuum** with independent rotational degrees of freedom, decoupling transverse-wave propagation from the bulk modulus and permitting $K > 0$ alongside pure transverse gauge-boson propagation.
- _Specific Non-Claims and Caveats_
  - This is a **structural / no-go argument**: it rules out a Cauchy substrate, motivating the micropolar Chiral LC continuum. It does not derive the chiral SRS lattice geometry (that comes from the K4 packing / EMT closure separately).
  - Does NOT claim micropolar continua are uniquely the AVE substrate; the leaf rules out one alternative (Cauchy) and the rest of Vol 1 motivates the specific chiral choice.

> **Leaf references:** [`axioms-and-lattice/ch2-macroscopic-moduli/implosion-paradox.md`](./axioms-and-lattice/ch2-macroscopic-moduli/implosion-paradox.md).

## Quality
- confidence: 0.85
- solidity: 0.85 (ok to build on)
- rationale: A clean structural / no-go argument grounded in standard continuum mechanics: a classical Cauchy elastic solid satisfying MacCullagh's transverse-wave condition ($\lambda = -\mu$) requires $K = -\mu/3 < 0$, which is unphysical. The boundary entry correctly bounds this as a no-go argument that *rules out* a Cauchy substrate — it does not claim to uniquely identify the AVE substrate as micropolar (the chiral SRS specifics come from K4 packing / EMT, separately disclosed). No entry-level scored dependencies — pure classical continuum mechanics + Axiom 1's transverse-wave constraint.
- strengthen-by:
  - none — the no-go argument is correctly self-bounded; further pin-down of "the substrate must be chiral SRS specifically" lives in EMT (`9s9apq`) and Vacuum Bulk Mass Density (`crbl60`) entries

---

## Topo-Kinematic Isomorphism $[Q] \equiv [L]$
<!-- id: dfaiwj -->

- $\xi_{topo} \equiv e/\ell_{node}$ [C/m]; $1\,\Omega = \xi_{topo}^{-2}$ kg/s
- _Specific Claims_
  - The Axiom 2 mechanism reframes charge as a discrete geometric dislocation (localized phase twist); the SI dimensions of charge and length become identified at scaling $\xi_{topo}$.
  - The full SI-dimensional table (V↔F, I↔v, Z↔kinematic impedance, L↔m, C↔1/k, $\mu_0$↔linear density, $\varepsilon_0$↔inverse tension) follows from this single identification.
- _Specific Non-Claims and Caveats_
  - This is a **dimensional isomorphism**, not a claim that charge "becomes" length in any operationally measurable sense at the engineering scale. SI conversions are exact within the framework's definitions; experimental discrimination depends on AVE's downstream predictions, not on the isomorphism itself.
  - $\xi_{topo}$ is INVARIANT-C2 in the cross-volume invariants (Vol 2/4/5 reuse it for atomic mappings, circuit engineering, biological mass/stiffness translations). Its canonical leaf-level definition lives in Vol 5; Vol 1 establishes it via Axiom 2 mechanism.

> **Leaf references:** [`axioms-and-lattice/ch1-fundamental-axioms/axiom-definitions.md`](./axioms-and-lattice/ch1-fundamental-axioms/axiom-definitions.md) (Axiom 2 mechanism); [`axioms-and-lattice/ch2-macroscopic-moduli/constitutive-moduli.md`](./axioms-and-lattice/ch2-macroscopic-moduli/constitutive-moduli.md); [`axioms-and-lattice/ch2-macroscopic-moduli/topo-kinematic-isomorphism.md`](./axioms-and-lattice/ch2-macroscopic-moduli/topo-kinematic-isomorphism.md). Bound also asserted at invariant level: CLAUDE.md INVARIANT-C2.

## Quality
- confidence: 0.80
- solidity: 0.80 (ok to build on, see caveats)
- rationale: $\xi_{topo} = e/\ell_{node}$ is direct from Axiom 2's topo-kinematic isomorphism mechanism; the SI-dimensional table (V↔F, I↔v, Z↔kinematic impedance, L↔m, C↔1/k, μ_0↔linear density, ε_0↔inverse tension) follows from this single identification by dimensional algebra. The boundary entry correctly self-bounds: this is a **dimensional isomorphism**, not an operational claim that charge becomes length at the engineering scale. The cross-volume reuse (Vol 2 atomic mappings, Vol 4 circuit engineering, Vol 5 biology mass/stiffness translations) is structural. INVARIANT-C2 carries the same bound at project-wide invariant level. No entry-level scored dependencies — Axiom 2's mechanism is framework-input.
- strengthen-by:
  - none entry-local — the isomorphism is correctly self-bounded as a dimensional identity given Axiom 2's mechanism

---

## Pauli Exclusion as Impedance Reflection (Vol 1 Mechanism Statement)
<!-- id: b9eura -->

- $\Gamma = (Z_{knot} - Z_{vacuum})/(Z_{knot} + Z_{vacuum}) = (0 - 377)/(0 + 377) = -1$
- _Specific Claims_
  - At the saturated knot core, dynamic RF impedance drops to $0\,\Omega$ (RF short circuit); incoming waves at the $377\,\Omega$ vacuum boundary reflect with $\Gamma = -1$ (total phase-reversed reflection).
  - This provides the macroscopic impedance-mismatch mechanism for the Pauli Exclusion Principle and for cross-sectional area in particle physics. Two saturated knots cannot occupy the same coordinates because their respective $0\,\Omega$ boundaries reflect each other's inductive phase energy.
  - Solid matter emerges from vacuum wave mechanics through this macroscopic impedance reflection.
- _Specific Non-Claims and Caveats_
  - The "$Z_{knot} = 0$" boundary refers to **dynamic RF impedance** (transverse-wave reflection condition), not static DC impedance. Confusion of the two leads to the apparent contradiction with the Vol 3 Einstein-field-equation leaf which says "$Z \to 0$ at the horizon" while GW leaves say "$Z = Z_0$ invariant" (see [vol3 Einstein Field Equation Reinterpretation entry](../vol3/claims-boundaries.md) and followups file for the unresolved cross-leaf tension).
  - Does NOT claim derivation of the spin-statistics theorem or anti-symmetric wavefunction structure; the impedance-mismatch argument provides the *mechanism* for exclusion (no-overlap), not the algebraic structure of fermion statistics.
  - The cross-domain $\Gamma \to -1$ translation matrix (particle confinement / plasma cutoff / superconductor / entanglement thread) is a **structural-identity** claim across Vol 1, Vol 1 EM, Vol 3 condensed matter, Vol 1 quantum-info — same operator, different sectors.

> **Leaf references:** [`dynamics/ch3-quantum-signal-dynamics/zero-impedance-boundary.md`](./dynamics/ch3-quantum-signal-dynamics/zero-impedance-boundary.md); [`dynamics/ch3-quantum-signal-dynamics/phase-locked-topological-thread.md`](./dynamics/ch3-quantum-signal-dynamics/phase-locked-topological-thread.md) (Universal $\Gamma \to -1$ Translation Matrix). Cross-cutting tension flagged in [vol3 Einstein Field Equation Reinterpretation](../vol3/claims-boundaries.md) and `kb-claims-boundaries-followups.md` (interpretive-tension entry).

## Quality
- confidence: 0.55
- depends-on:
  - efo113 — Master Equation EFT Validity (solidity 0.50) [the saturated-knot $Z \to 0$ behavior depends on master-equation dynamics at saturation]
- solidity: 0.28 (do not build on, rework needed) [= 0.55 × 0.50]
- rationale: The $\Gamma = -1$ formula is straightforward impedance algebra given $Z_{knot} = 0$ and $Z_{vacuum} = 377\,\Omega$. The mechanism chain (saturated knot → $\mu_{eff} \to 0$ → $Z \to 0$ → reflection $\Gamma = -1$ → standing wave = no-overlap = exclusion) shares the same load-bearing dependency as Magnetic-Branch Confinement (`lv3uw1`): the master-equation EFT must remain valid through saturation. A separate concern is the cross-leaf tension flagged in the boundary disclosure: Vol 1 says $Z \to 0$ at the saturated knot core, while Vol 3 GW leaves say $Z = Z_0$ invariant in symmetric saturation — these may describe distinct physical situations (knot core vs GW horizon in symmetric gravity) but the impedance-operator usage is currently ambiguous across leaves. The entry also does NOT derive the spin-statistics theorem or anti-symmetric wavefunction structure from this mechanism — it provides exclusion-by-no-overlap, not the algebraic structure of fermion statistics.
- strengthen-by:
  - Strengthen Master Equation EFT Validity (`efo113`); $\Gamma \to -1$ at saturation depends on master-equation dynamics correctly describing $\mu_{eff} \to 0$
  - Resolve the cross-leaf $Z$-behavior tension between Vol 1 (saturated knot core: $Z \to 0$) and Vol 3 GW horizons ($Z = Z_0$ invariant in symmetric saturation); either disambiguate the contexts explicitly or correct whichever leaf is wrong
  - Provide an axiom-grounded derivation that Pauli exclusion's NO-OVERLAP constraint follows from the impedance mismatch (currently a structural identification, not a derivation that produces fermion statistics)
