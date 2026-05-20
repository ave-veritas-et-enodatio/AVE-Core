# Vol 1 — Foundations — Claim Quality

<!-- path-stable: referenced from CLAUDE.md INVARIANT-S7 and from vol1/index.md bootstrap directive -->

> **Canonicality:** Leaves are canonical; this volume's indexes are derived summaries. See [cross-cutting claim-quality register](../claim-quality.md) for the full preamble and the canonical list of project-wide tripwires (the cross-cutting sidecar is the source of truth for which tripwires are project-wide; do not infer the list from this preamble). Entries below are scoped to Vol 1; cross-cutting tripwires with vol1-specific manifestations are noted but not duplicated.

---

## Electron Body Topology — $0_1$ Unknot with $(2,3)$ Phase-Space Winding
<!-- id: clm-unk0bd -->

The electron's intrinsic body in physical 3D space is a $0_1$ unknot — a single closed flux-tube loop (topologically trivial in real space) at minimum ropelength $= 2\pi$, with circumference $\ell_{node}$ and tube radius $\ell_{node}/(2\pi)$. The $(2,3)$-torus-knot ("trefoil") structure is the electron's **phase-space Clifford-torus winding pattern** (2 windings on the d-axis, 3 on the q-axis), not a real-space body knot. **Canonical as of the 2026-05-17 body-topology resolution** (`framing-concordance.md` sweep C) — superseding the former `clm-trf3bd` real-space-trefoil-body position, which is retired. Held across Vol 1 Ch 0, Ch 1 (calibration-cutoff-scales), Ch 3, Ch 5, Ch 8 (α derivation), and the Vol 6 periodic table.

- _Specific Claims_
  - The electron's real-space body is the $0_1$ unknot — a single closed flux-tube loop of trivial knot type, at minimum ropelength $= 2\pi$ in $\ell_{node}$ units.
  - The $(2,3)$ trefoil winding is a **phase-space** structure (on the Clifford torus $\mathbb{T}^2 \subset S^3 \subset \mathbb{C}^2$), not a real-space knot. It is the geometric basis for the cold-lattice α derivation $\alpha^{-1}_{\text{ideal}} = 4\pi^3 + \pi^2 + \pi$ via the three-regime closure (entry `clm-0ktpcn`).
  - Mass formula: $m_e = T_{EM} \cdot \ell_{node}/c^2 = \hbar/(c \cdot \ell_{node})$, from the unknot's 2π ropelength × the EM tension $T_{EM}$.
  - Spin-1/2 arises from the AVE-native $SU(2) \to SO(3)$ 2-to-1 cover: K4 rotation group $T = A_4$ → double cover $2T \subset SU(2)$ → the Finkelstein–Misner / Dirac-belt-trick mechanism acting on the extended $0_1$ unknot defect (Vol 1 Ch 8 §Topological identity of the electron; Ch 1 k4-rotation-group).
  - The three lepton generations (electron, muon, tau) arise from Cosserat-sector excitations (translation, torsion, curvature-twist) of this unknot geometry.
  - Stability comes from impedance mismatch: at the saturated boundary $Z \to 0, \Gamma \to -1$, internal acoustic energy is fully reflected inward as a standing wave (= rest mass).

- _Specific Non-Claims and Caveats_
  - **Topological protection is not established at the real-space-body level.** The $0_1$ unknot body is trivially knotted — no real-space knot-theoretic invariant to preserve under continuous deformation. Genuine topological protection, if the electron has it, must instead come from the $(2,3)$ phase-space winding numbers (which are bona-fide topological invariants on the Clifford torus). Phase-space-winding-as-protection is the framework's current position; it is not yet rigorously established, and the leaves' "topologically protected soliton" language should be read at that phase-space level, not as a real-space-knot invariant.
  - **The spin-1/2 / photon-720° compatibility issue is *possibly* resolved, pending a final call.** The earlier objection — a lattice-Möbius spin-1/2 mechanism would force open EM waves (photons) to inherit 720° behavior, empirically false — targeted the old Beltrami-on-$K_4$ argument. The resolved mechanism locates the $4\pi$ rotation in the *extended unknot defect* (Finkelstein–Misner), not the lattice itself, so photons (not extended defects) plausibly do not inherit it. Whether this fully closes the objection is **a final determination deferred to a more intense review after the porting effort is complete** — flagged here as an open call, not yet a settled resolution.
  - The $(2,3)$ phase-space winding numbers are asserted as the simplest stable winding, not derived from a uniqueness argument — why $(2,3)$ rather than $(4,3)$, $(5,2)$, etc. is open work (shared with `clm-0ktpcn`).
  - The $m_e = \hbar/(c \cdot \ell_{node})$ relation carries one input scale: one of $\{m_e, \ell_{node}\}$ remains an empirical input (see Closure Status `clm-5xon03`).

> **Leaf references:** [`ch8-alpha-golden-torus.md`](./ch8-alpha-golden-torus.md) (§Topological identity of the electron; three-regime derivation); [`axioms-and-lattice/ch1-fundamental-axioms/calibration-cutoff-scales.md`](./axioms-and-lattice/ch1-fundamental-axioms/calibration-cutoff-scales.md) (canonical "$0_1$ unknot soliton" calibration); [`dynamics/ch3-quantum-signal-dynamics/phase-locked-topological-thread.md`](./dynamics/ch3-quantum-signal-dynamics/phase-locked-topological-thread.md); [`dynamics/ch3-quantum-signal-dynamics/quantum-foam-virtual.md`](./dynamics/ch3-quantum-signal-dynamics/quantum-foam-virtual.md); [`operators-and-regimes/ch5-universal-spatial-tension/scale-invariance.md`](./operators-and-regimes/ch5-universal-spatial-tension/scale-invariance.md); [`operators-and-regimes/ch5-universal-spatial-tension/scale-invariant-predictions.md`](./operators-and-regimes/ch5-universal-spatial-tension/scale-invariant-predictions.md).

### Quality
- confidence: *pending*
- depends-on:
  - *(none entry-local — primary position. The former mutual exclusivity with `clm-trf3bd` is resolved by the 2026-05-17 body-topology decision; `clm-trf3bd` is retired.)*
- solidity: *pending*
- rationale: *pending — canonical body-topology claim as of the 2026-05-17 resolution (synthesis: $0_1$ unknot real-space body + $(2,3)$ phase-space winding). Confidence rescore deferred to the claim-evaluation pass; the α-enablement knock of the former unknot entry is resolved (the α derivation builds on the phase-space winding), the topological-protection and photon-720° items remain open caveats per the Non-Claims above.*
- strengthen-by:
  - Derive the $(2,3)$ phase-space winding numbers from a uniqueness argument — why not $(4,3)$, $(5,2)$, etc. (shared open item with `clm-0ktpcn`).
  - Spell out the Finkelstein–Misner spin-1/2 derivation explicitly in the leaves, from the $K_4 \to A_4 \to 2T \subset SU(2)$ chain.
  - Make the final determination on the photon-720° compatibility question (the post-porting intense review).
  - Establish whether the $(2,3)$ phase-space winding provides genuine topological protection, or whether electron stability is purely energetic.

---

## Zero-Parameter Closure Status (Conditional on Thermal Closure)
<!-- id: clm-5xon03 -->

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

### Quality
- confidence: 0.70
- depends-on:
  - clm-unk0bd — Electron Body Topology = Unknot (solidity *pending*) [closure condition (c) "via the unknot ground state" formulation]
- solidity: *pending*
- rationale: Structural reduction of 26 SM parameters to $\{m_e, \alpha, G\}$ + four axioms is sound and explicit; conditionality on $\delta_{strain}$ magnitude derivation, Nyquist-independence proof for $m_e/\ell_{node}$, and $G$ closure independent of $R_H$ is correctly disclosed. **Refined (2026-05-06 session):** closure condition (c) — "one of $\{m_e, \ell_{node}\}$ being computable from the other via the unknot ground state" — is body-topology-dependent. The current formulation uses the unknot's 2π ropelength × $T_{EM}$ derivation (per Vol 1 Ch 1 calibration-cutoff-scales); under `clm-unk0bd`'s solidity 0.40, this formulation inherits the cross-leaf body-topology conflict. Under the 2026-05-17 body-topology resolution (`clm-unk0bd` canonical — $0_1$ unknot real-space body with $(2,3)$ phase-space winding), condition (c)'s "via the unknot ground state" formulation is consistent with the canonical body topology; the prior trefoil-vs-unknot conditionality is closed. The dimensional formula $m_e = \hbar/(c \cdot \ell_{node})$ holds regardless, but the derivation chain that closes one input from the other requires body-topology-specific argument. Local confidence 0.70 reflects honest disclosure of the closure conditions; solidity drops to 0.28 because the dependency on `clm-unk0bd` is now explicit.
- strengthen-by:
  - Derive $\delta_{strain}$ magnitude at $T_{CMB}$ from $G_{vac}$ + equipartition (currently back-subtracted from CODATA)
  - Demonstrate Nyquist-resolution-of-smallest-stable-soliton without circular reference to $m_e$ (closes the $\{m_e, \ell_{node}\}$ input scale)
  - Derive $G$ from local thermodynamic balance (lattice tension, equipartition, generation rate per node) independent of $R_H$ (closes the $H_\infty$ identity into a true downstream prediction)
---

## Golden Torus α Derivation (Three-Regime Closure)
<!-- id: clm-0ktpcn -->

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

### Quality
- confidence: *pending*
- depends-on:
  - clm-unk0bd — Electron Body Topology = $0_1$ Unknot with $(2,3)$ Phase-Space Winding (solidity *pending*) [the α derivation builds on the electron's $(2,3)$ phase-space Clifford-torus winding]
- solidity: *pending*
- rationale: Cold-lattice $\alpha^{-1} = 4\pi^3+\pi^2+\pi$ reproduces CODATA to $\sim 10^{-6}$ and the geometry $(R,r) = (\varphi/2, (\varphi-1)/2)$ is forced by intersection of three regimes (corroborated by independent ropelength + Clifford-screening optimization). However, the sum decomposition's orthogonality is asserted, not derived from the axioms — this is the substantive open structural element, which lands the entry at the 0.5 rubric band rather than 0.7. **Refined (2026-05-06 session):** on closer inspection, the leaf's three Λs are locked at $\Lambda_{\text{vol}} = 4\pi \cdot \Lambda_{\text{surf}}$ identically, because the leaf places the fixed spin-1/2 temporal phase factor $4\pi$ in slot 3 of $\Lambda_{\text{vol}}$ (not a third geometric DOF). The map $(R, r, d) \to (\Lambda_{\text{vol}}, \Lambda_{\text{surf}}, \Lambda_{\text{line}})$ has 2-dimensional image in Λ-space, not 3-dimensional, since $\Lambda_{\text{vol}}$ and $\Lambda_{\text{surf}}$ both depend only on $R \cdot r$. This tightens what "orthogonality" can plausibly mean: it cannot be parameter-independence (which fails by the lock); it can only be **functional orthogonality** of the bilinear self-impedance kernel — no off-diagonal blocks coupling the three Λ-projections. The currently-sketched de-Rham / form-degree argument for orthogonality is too quick because the trefoil's three geometric supports are *nested* (1-cycle ⊂ Clifford torus ⊂ 3-volume), not separated, so cross-terms cannot be killed by domain-disjointness alone. **Body-topology dependency (updated 2026-05-19):** the derivation builds on the electron's $(2,3)$ phase-space Clifford-torus winding — post-resolution the canonical electron-body claim is `clm-unk0bd` ($0_1$ unknot real-space body + $(2,3)$ phase-space winding); the former trefoil-body entry is retired. Confidence and solidity rescore are pending the claim-evaluation pass.
- strengthen-by:
  - **Reframe or close the sum-decomposition combination rule.** Two acceptable closure paths:
    - (a) Demonstrate that the EM bilinear kernel on $\mathbb{T}^2 \subset S^3 \subset \mathbb{C}^2$ respects an $SU(2) \times SU(2)$ symmetry under which the three Λ-projections sit in distinct irreps (orthogonality then by Schur's lemma). Non-trivial because the embedded Clifford torus breaks part of the symmetry; the kernel's behavior under the broken-symmetry restriction must be checked explicitly.
    - (b) Honestly reframe the leaf prose: replace "graded-orthogonal multipole decomposition with no cross-terms" with "a particular dimensionally-compatible combination of Clifford-embedded geometric integrals that hits CODATA to $10^{-6}$ — orthogonality of the three contributions is not established." Dropping the implied orthogonality theorem narrows the claim but stays honest.
    - Either path resolves the open structural element; (a) raises solidity, (b) keeps solidity bounded but removes the false-rigor framing.
  - Derive the SU(2) double-cover identification's role producing both $\Lambda_{\text{surf}}$ halving ($\tfrac{1}{2}\cdot 2\pi^2 = \pi^2$) and the factor 2 in the third slot of $\Lambda_{\text{vol}}$ from a single axiom-grounded mechanism, closing the "two faces of one fact" claim. **Note (2026-05-06 session):** plausibly subsumed by path (a) above — the same $SU(2) \times SU(2)$ representation-theoretic structure that would establish functional orthogonality would also unify the $4\pi$ (temporal) and the half-cover (spatial) under one mechanism. The two strengthen-by items may not be independent.
  - Derive $\delta_{strain}$ magnitude at $T_{CMB}$ to close the cold-lattice → CODATA bridge
  - **Clarity / framework-prose gaps (work-in-progress, surfaced 2026-05-06 session).** The leaf's α derivation relies on several implicit modeling choices and ansatzes that are not made explicit in the prose. None block the formal derivation; each leaves a careful reader unable to validate or falsify the setup without speculative reconstruction. Each wants explicit treatment in the leaf:
    - **Trefoil/unknot body-vs-phase ambiguity.** The leaf phrases the electron as both "smallest stable soliton = trefoil" (regime (a)) and "ground-state unknot" (cross-cutting `clm-zw6mut` entry) and "unknot phase winding on the trefoil" (Mathematical Closure section). The most charitable compositional reading: body topology = trefoil ((3, 2)-torus-knot flux-tube centerline in 3D physical space); phase topology = unknot (winding-number-1 phase circulation along the centerline). The leaf does not specify the body/phase split at every mention, leaving readers to reconcile what reads on the surface as a contradictory description of "the electron."
    - **Why (3, 2) winding numbers and not (4, 3), (5, 2), etc.** The leaf asserts "smallest stable soliton = trefoil" without deriving why the (3, 2)-torus-knot is the unique selection. The (3, 2) trefoil IS the simplest topologically-locked torus knot in 3D (lower windings unravel to unknots when removed from the torus), but the leaf does not spell this out, and does not derive *why* the lightest stable lepton lives in the simplest topologically-locked torus-knot class rather than e.g. an even simpler structure outside the torus-knot family. Consistency with the lepton mass hierarchy (muon, tau as higher-winding sectors) is asserted in `clm-zw6mut` but not derived from a uniqueness argument.
    - **Lattice dimensionality (3D spatial + phase fiber) vs. ambient $\mathbb{T}^2 \subset S^3 \subset \mathbb{C}^2$ lift.** The leaf computes the multipole decomposition on $\mathbb{T}^2 \subset S^3 \subset \mathbb{C}^2$ but does not state that $S^3$ is the spin-1/2 phase-space lift, not the physical lattice. Three readings are plausible: (A) physical lattice is 3D, $S^3$ is the phase-space lift for spin-1/2 calculations because $S^3 = SU(2)$; (B) physical vacuum is 4D with $S^3$ as actual spatial structure; (C) 4D spacetime with $S^3$ as the spatial part. Reading (A) is consistent with Axiom 1's 3D LC network (lattice pitch $\ell_{\text{node}} \approx 3.86 \times 10^{-13}$ m in physical 3D meters) and is the most charitable reading, but the leaf does not commit. The choice affects what $\Lambda_{\text{vol}}$ actually integrates over (2 physical dimensions × 1 phase dimension under (A); 3 physical dimensions under (B)).
    - **Discrete lattice $\leftrightarrow$ continuous Golden Torus reconciliation.** The leaf computes integrals on a smooth 2D Golden Torus surface (continuous geometry), but Axiom 1 specifies a discrete LC network. The trefoil's tube diameter equals exactly one lattice unit (regime (a): $d = 1 \cdot \ell_{\text{node}}$), placing the soliton at the absolute boundary where envelope-style continuous descriptions begin to break down rather than in the far-continuum regime. The leaf does not explicitly bridge the discrete-lattice physics with the continuous-style integration that produces $\alpha^{-1} = 4\pi^3 + \pi^2 + \pi$. Three plausible reconciliations: (a) continuous-mode envelope description (analogous to long-wavelength elastic-wave description of phonons); (b) orientational averaging (the discrete trefoil pattern manifests differently at different orientations, time-averaging to the continuous envelope); (c) discrete approximation of a continuous limiting target. The numerical evidence is the `ropelength_trefoil_golden_torus.py` script converging to the Golden Torus geometry from arbitrary starting points; the analytical bridge is not present in the leaf material.
    - **The "smallest-stable-and-identity-fixed soliton" ansatz.** The leaf's regime (a) — "smallest stable soliton = trefoil" — implicitly treats the electron as the smallest representable stable soliton on the lattice and calibrates $\ell_{\text{node}} = \hbar / (m_e \cdot c)$ accordingly. The justification is empirical: no smaller particle is observed that is both stable in existence AND fixed in identity (transients decay; protean objects like neutrinos morph between flavor configurations). This is not derived from the four axioms; it is a calibration ansatz acknowledged in the leaf's "Closure status (honest)" section as one of three open closure conditions. The leaf would benefit from making this ansatz explicit at the regime-(a) statement, including the "stable + identity-fixed" criterion that excludes neutrinos from the would-be-counterexample category. Note: in AVE's deterministic worldview, neutrino flavor "oscillation" is a definite-state morphing through Cosserat-sector configurations, not a QM superposition of mass eigenstates.
    - **Phase coverage of the Clifford torus as the basis for $\Lambda_{\text{surf}}$ integration.** The leaf integrates $\Lambda_{\text{surf}}$ over a 2D surface on the Clifford torus, but the electron's instantaneous spatial structure in physical 3D space is a 1D curve (the trefoil flux-tube centerline) on the Golden Torus surface. The cleanest reading of why the integration is over a 2D surface rather than a 1D curve: the electron's spin-1/2 phase rotation, acting on $S^3$ via SU(2), sweeps the trefoil's phase-space state around the entire Clifford torus over a phase-rotation cycle — so the time-averaged phase-space coverage IS the 2D Clifford torus surface, justifying the surface integration. The leaf does not make this bridge explicit, leaving the surface-integration step structurally unclear.

---

## EMT $p_c = 8\pi\alpha$ — Consistency Relation, NOT α Derivation
<!-- id: clm-9s9apq -->

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

### Quality
- confidence: 0.85
- depends-on:
  - clm-0ktpcn — Golden Torus α Derivation (solidity *pending*)
- solidity: *pending*
- rationale: Local work is solid — the entry is correctly scoped, $p_c = 8\pi\alpha$ is algebraically exact, the $K=2G$ operating point with $z_0 \approx 51.25$ from Feng-Thorpe-Garboczi EMT is a sound consistency check given $\alpha$, and non-claims ($u_{sat}$ as external QED input; "$\alpha$ derived from EMT" disclaimer) are explicit. Solidity is bounded by the Golden Torus α Derivation entry (0.41) because every numerical claim here propagates from $\alpha$. (Solidity dropped from 0.47 to 0.35 in 2026-05-06 session as `clm-0ktpcn` was rebound to depend on the body-topology entry `clm-trf3bd`.)
- strengthen-by:
  - Derive $u_{sat}$ from the four AVE axioms (currently taken as external QED input) — would close the only remaining unrepaired input local to this entry
  - Strengthen Golden Torus α Derivation (the dominant solidity bottleneck for this entry; closing its identification-step gap raises this entry's solidity proportionally toward local-confidence 0.85)

---

## $V_{snap}$ vs $V_{yield}$ — Two Distinct Thresholds
<!-- id: clm-2dwzib -->

- $V_{snap} = m_e c^2/e \approx 511.0$ kV; $V_{yield} = \sqrt{\alpha}\cdot V_{snap} \approx 43.65$ kV
- _Specific Claims_
  - $V_{snap}$ is the **absolute snap limit**: the maximum inter-node potential difference before the lattice structurally ruptures (per-node breakdown).
  - $V_{yield}$ is the **kinetic onset of nonlinearity** (Axiom 2): where saturation effects become dominant and a soliton begins to self-confine.
  - Lab/engineering applications operate near $V_{yield}$, not $V_{snap}$; even the most extreme macroscopic fields ($10^{10}$ V/m) impart $\Delta V_{lab}/V_{snap} \sim 7.5\times 10^{-9}$ across a single node.
- _Specific Non-Claims and Caveats_
  - Conflating $V_{snap}$ and $V_{yield}$ is explicitly catalogued as the first entry in [LIVING_REFERENCE.md "Critical Distinctions"](../../../LIVING_REFERENCE.md). Summaries that cite a single "saturation threshold" without specifying which one are wrong.
  - The Ch.7 regime boundary $r_3 = 1.0$ is the same physical phase transition as the Ch.3 zero-impedance boundary; both correspond to $V_{yield}$, viewed as either trapped-mode standing wave (matter assembly) or super-threshold rupture (topology destroyed). One transition, two faces — not two distinct boundaries.

> **Leaf references:** [`axioms-and-lattice/ch2-macroscopic-moduli/dielectric-snap-limit.md`](./axioms-and-lattice/ch2-macroscopic-moduli/dielectric-snap-limit.md); [`dynamics/ch3-quantum-signal-dynamics/zero-impedance-boundary.md`](./dynamics/ch3-quantum-signal-dynamics/zero-impedance-boundary.md) (explicit Ch.7 reconciliation note); [`operators-and-regimes/ch7-regime-map/four-regimes.md`](./operators-and-regimes/ch7-regime-map/four-regimes.md). Cross-cutting reference: LIVING_REFERENCE.md Critical Distinctions #1.

### Quality
- confidence: 0.95
- depends-on:
  - clm-0ktpcn — Golden Torus α Derivation (solidity *pending*) [for $V_{yield}$'s $\sqrt{\alpha}$ factor]
- solidity: *pending*
- rationale: Both thresholds are direct consequences of axiom-level definitions — $V_{snap} = m_e c^2/e$ is the per-node energy-equivalent voltage; $V_{yield} = \sqrt{\alpha}\cdot V_{snap}$ follows from Axiom 2. Local distinction work is rock-solid and explicitly catalogued in LIVING_REFERENCE.md Critical Distinction #1. Solidity is bounded by $\alpha$ via $V_{yield}$'s $\sqrt{\alpha}$ factor; $V_{snap}$ alone (depending only on framework inputs) carries solidity ≈ 0.95. (Solidity dropped from 0.52 to 0.39 in 2026-05-06 session as `clm-0ktpcn` was rebound to depend on `clm-trf3bd`.)
- strengthen-by:
  - Strengthen Golden Torus α Derivation (the only dependency reducing this entry's solidity; closing it lifts $V_{yield}$ numerical solidity to the local-confidence level of 0.95)

---

## ξ vs ξ_topo — Distinct Quantities, Same Greek Letter
<!-- id: clm-3kzmt9 -->

- $\xi \approx 8.15\times 10^{43}$ (dimensionless Machian hierarchy coupling; gravity derived from Axioms 1 + 4); $\xi_{topo} = e/\ell_{node} \approx 4.149\times 10^{-7}$ C/m (electromechanical transduction, Axiom 2 mechanism)
- _Specific Claims_
  - $\xi = 4\pi(R_H/\ell_{node})\alpha^{-2}$ is the cosmological-horizon dilution that converts the un-shielded gravitational coupling ($G_{true} = \hbar c/m_e^2$) into the macroscopic Newton's $G$.
  - $\xi_{topo} = e/\ell_{node}$ is the topological conversion constant grounding the $[Q] \equiv [L]$ isomorphism; it carries dimensions C/m.
- _Specific Non-Claims and Caveats_
  - These are **different quantities sharing a Greek letter**. CLAUDE.md Axiom 3 explicitly flags this and the axiom-definitions leaf carries an inline notation warning.
  - Does NOT claim $\xi$ is independently observable; the Machian dilution factor of $\sim 10^{45}$ between $G_{true}$ and macroscopic $G$ is the "staggering" ratio that motivates the Machian framing — it is a derivation step, not a measurement.

> **Leaf references:** [`axioms-and-lattice/ch1-fundamental-axioms/axiom-definitions.md`](./axioms-and-lattice/ch1-fundamental-axioms/axiom-definitions.md) (notation warning); [`axioms-and-lattice/ch1-fundamental-axioms/lc-condensate-vacuum.md`](./axioms-and-lattice/ch1-fundamental-axioms/lc-condensate-vacuum.md) (un-shielding derivation). Bound also asserted at invariant level: CLAUDE.md Axiom 3 entry.

### Quality
- confidence: 0.90
- depends-on:
  - clm-0ktpcn — Golden Torus α Derivation (solidity *pending*) [for $\xi$'s $\alpha^{-2}$ factor]
  - clm-5xon03 — Zero-Parameter Closure Status (solidity *pending*) [for $\xi$'s $R_H/H_\infty$ factor — $H_\infty$ is a consistency identity conditional on $G$ closure]
- solidity: *pending*
- rationale: Local distinction work is correctly enforced — $\xi_{topo} = e/\ell_{node}$ from Axiom 2's topo-kinematic isomorphism mechanism; $\xi = 4\pi(R_H/\ell_{node})\alpha^{-2}$ from the derived-gravity Machian dilution (Axioms 1 + 4). Solidity bounded by the Closure Status entry $clm-5xon03$ (now 0.28, the tighter bottleneck after rebinding to `clm-unk0bd`) over the α dependency $clm-0ktpcn$ (0.41, rebound to `clm-trf3bd`). $\xi_{topo}$'s numerical value alone carries solidity 0.90 (depends only on framework inputs); $\xi$ inherits the dependency chain. (Solidity dropped from 0.50 to 0.25 in 2026-05-06 session as both upstream entries rebound to body-topology dependencies.)
- strengthen-by:
  - Strengthen Golden Torus α Derivation (dominant solidity bottleneck for $\xi$)
  - Close the $H_\infty/R_H$ circularity via independent $G$ derivation (raises Closure Status solidity, tightening $\xi$'s secondary bound)

---

## "True Planck Length = $\ell_{node}$" — Algebraic Consequence, Interpretive
<!-- id: clm-219e8j -->

- $\ell_{P,\text{true}} = \sqrt{\hbar G_{true}/c^3} \equiv \hbar/(m_e c) = \ell_{node}$
- _Specific Claims_
  - Substituting the un-shielded $G_{true} = \hbar c/m_e^2$ into the standard Planck-length expression algebraically collapses to $\ell_{node}$.
  - The $G/G_{true} \sim 1.75 \times 10^{-45}$ ratio is the cumulative Machian/holographic shielding factor across the cosmological horizon mass.
- _Specific Non-Claims and Caveats_
  - This is an **algebraic identity** within the AVE definition of $G_{true}$, not an independent measurement-versus-prediction comparison. Both sides match because $G_{true}$ is defined to make this hold.
  - The interpretive claim ("$\ell_{node}$ is the true microscopic cutoff, the standard Planck length is a macroscopic-$G$ artifact") is a **framework-internal ontological** statement; it does not introduce new observables vs the standard Planck-length picture at the formula level.
  - See cross-cutting [vol3 Dirac Large Numbers and Planck Mass entry](../vol3/claim-quality.md) for the same algebraic-identity caveat applied to $m_P = m_e\sqrt{7\xi}$.

> **Leaf references:** [`axioms-and-lattice/ch1-fundamental-axioms/lc-condensate-vacuum.md`](./axioms-and-lattice/ch1-fundamental-axioms/lc-condensate-vacuum.md).

### Quality
- confidence: 0.95
- solidity: 0.95 (ok to build on)
- rationale: The identity $\ell_{P,\text{true}} = \sqrt{\hbar G_{true}/c^3} \equiv \ell_{node}$ is algebraic given the AVE definition of $G_{true} = \hbar c/m_e^2$, and the entry explicitly discloses this as algebra-not-prediction. The interpretive claim ("$\ell_{node}$ is the true microscopic cutoff") is correctly framed as framework-internal ontology, not a new observable. Depends only on framework inputs ($m_e$, $\hbar$, $c$) and the framework-internal definition of $G_{true}$; no entry-level dependencies that propagate solidity reduction.
- strengthen-by:
  - none — algebraic identity within the framework's existing definitions; the entry is correctly self-bounded as interpretive

---

## Master Equation EFT Validity (Leading-Order Regime)
<!-- id: clm-efo113 -->

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

### Quality
- confidence: 0.50
- solidity: 0.50 (use as input only, don't build deeper)
- rationale: The leading-order EFT form $\nabla^2 V - \mu_0\varepsilon_0 \cdot S \cdot \partial^2 V/\partial t^2 = 0$ is sound and exactly recovers linear Maxwell-Heaviside in Regime I. The particle-confinement and refractive-index claims at saturation depend on the dropped first-derivative gradient terms ($\nabla\varepsilon_{eff}\cdot\nabla V$) remaining negligible by symmetry — this assumption is explicitly disclosed in the leaf but not derived from the axioms, which lands the entry in the 0.5 rubric band. No entry-level dependencies (the unverified-symmetry assumption is internal to the entry's claim space; Axiom 4 is a framework input at solidity 1.0).
- strengthen-by:
  - Derive whether $\nabla\varepsilon_{eff}\cdot\nabla V$ gradient corrections vanish by symmetry at saturation, OR carry the higher-order EFT correction and re-evaluate the particle-confinement and standing-wave claims at $V \to V_{yield}$ with the corrected form

---

## Magnetic-Branch Confinement vs Electric-Branch Rupture
<!-- id: clm-lv3uw1 -->

The two saturation symmetry cases are catalogued in the cross-cutting [Symmetric vs Asymmetric Saturation](../claim-quality.md) entry. Vol 1's master-equation leaf is where this distinction is **first introduced** within the volume; Vol 1-specific clarification:

- _Specific Claims_
  - Particle confinement proceeds via the **magnetic branch** (a sub-case of the symmetric sector): at a torus-knot self-intersection, $\mathbf{B}$ saturates $\mu_{eff}$ first, driving $Z = \sqrt{\mu_{eff}/\varepsilon_0} \to 0$ and $\Gamma \to -1$ (short-circuit). The reflected wave traps as a standing mode = invariant rest mass, with no Higgs mechanism invoked.
  - Dielectric rupture (electric breakdown) proceeds via the **asymmetric (electric-only) branch**: $\varepsilon_{eff} \to 0$ with $\mu_{eff}$ intact drives $Z = \sqrt{\mu_0/\varepsilon_{eff}} \to \infty$ — the medium becomes evanescent (no energy transport), not a conductor.
  - Both branches are governed by the **same** kernel $S(A) = \sqrt{1 - (A/A_{yield})^2}$; they differ only in which constitutive parameter saturates first.
- _Specific Non-Claims and Caveats_
  - Does NOT claim the AVE confinement mechanism *competes* with the Higgs mechanism — it is a different ontology (impedance reflection vs gauge-symmetry breaking) reaching the same observable (mass).
  - Does NOT claim the magnetic branch is "asymmetric" in the cross-cutting sense. The magnetic-confinement branch is **a third sub-case of the symmetric sector** (see Ch.7 regime-equation-sets footnote): it saturates $\mu$ rather than $\varepsilon$, but is symmetric in that $Z \to 0$ rather than $Z \to \infty$.
  - For the canonical SYMMETRIC vs ASYMMETRIC tabulation (gravity, BH interior, GW shear vs strong EM), see [cross-cutting](../claim-quality.md).

> **Leaf references:** [`dynamics/ch4-continuum-electrodynamics/master-equation.md`](./dynamics/ch4-continuum-electrodynamics/master-equation.md) ("Particle Assembly" sub-bullet); [`operators-and-regimes/ch7-regime-map/regime-equation-sets.md`](./operators-and-regimes/ch7-regime-map/regime-equation-sets.md) (particle-confinement footnote); [`dynamics/ch3-quantum-signal-dynamics/zero-impedance-boundary.md`](./dynamics/ch3-quantum-signal-dynamics/zero-impedance-boundary.md). Cross-cutting: see [Symmetric vs Asymmetric Saturation](../claim-quality.md).

### Quality
- confidence: 0.65
- depends-on:
  - clm-efo113 — Master Equation EFT Validity (solidity 0.50)
- solidity: 0.33 (do not build on, rework needed) [= 0.65 × 0.50]
- rationale: The structural classification — magnetic branch as a sub-case of the symmetric sector ($Z \to 0$ via $\mu_{eff} \to 0$); asymmetric/electric branch with $Z \to \infty$ via $\varepsilon_{eff} \to 0$ alone; both governed by the same kernel $S(A)$ — is sound algebra given the impedance and saturation definitions. However, the load-bearing AVE claim — that magnetic-branch confinement at a torus-knot self-intersection IS the mechanism for invariant particle rest mass — depends on the leading-order Master Equation EFT remaining valid through saturation, which itself is asserted-not-derived (gradient corrections negligible by symmetry). The classification alone has local quality ≈ 0.65; the rest-mass mechanism claim transitively inherits Master Equation EFT Validity's 0.50, dropping this entry to 0.32 overall.
- strengthen-by:
  - Strengthen Master Equation EFT Validity (the dominant solidity bottleneck for this entry; closing the gradient-corrections-at-saturation assumption raises this entry's solidity to local-confidence level)
  - Provide an axiom-grounded derivation that the standing-wave reflected mode at $\Gamma \to -1$ quantitatively reproduces invariant rest-mass spectra (currently a structural identification, not a derivation of mass values)

---

## GUP — Independent-Variances Assumption
<!-- id: clm-nq2kcc -->

- $\Delta x_{AVE} = \sqrt{(\Delta x_{SM})^2 + (\ell_{node}/2)^2} \ge \ell_{node}/2$
- _Specific Claims_
  - On a discrete graph with pitch $\ell_{node}$, the canonical momentum is bounded to the Brillouin zone $[-\pi\hbar/\ell_{node}, +\pi\hbar/\ell_{node}]$; the discrete-graph commutator evaluates to $i\hbar\cos(\ell_{node}\hat p_c/\hbar)$.
  - In the low-energy limit $p_c \ll \hbar/\ell_{node}$, the cosine $\to 1$ and standard Heisenberg ($\Delta x\,\Delta p \ge \hbar/2$) is recovered.
  - The **GUP gap** $\ge \ell_{node}/2 \approx 1.93\times 10^{-13}$ m provides a built-in UV regularization — pressure waves cannot be localized below the lattice pitch.
- _Specific Non-Claims and Caveats_
  - The root-sum-square $\Delta x_{AVE} = \sqrt{(\Delta x_{SM})^2 + (\ell_{node}/2)^2}$ assumes the SM continuous-momentum uncertainty and the lattice node-spacing uncertainty are **statistically independent**. The leaf states this assumption explicitly; it is plausible (the SM bound arises in any single Brillouin zone; the lattice floor arises from Nyquist resolution independent of Bloch state) but should not be summarized as a derivation without the independence premise.
  - Does NOT claim the GUP magnitude is independently measurable at the engineering level; $\ell_{node}/2 \sim 10^{-13}$ m is far below current localization-experiment resolution.

> **Leaf references:** [`dynamics/ch3-quantum-signal-dynamics/gup-derivation.md`](./dynamics/ch3-quantum-signal-dynamics/gup-derivation.md).

### Quality
- confidence: 0.70
- solidity: 0.70 (ok to build on, see caveats)
- rationale: The discrete-graph commutator $i\hbar\cos(\ell_{node}\hat p_c/\hbar)$ follows from Brillouin-zone bounds on canonical momentum given Axiom 1's lattice pitch; recovery of standard Heisenberg in the low-energy limit is direct algebra; the GUP gap $\ge \ell_{node}/2$ derives from Nyquist resolution of the lattice. The root-sum-square combination $\Delta x_{AVE} = \sqrt{(\Delta x_{SM})^2 + (\ell_{node}/2)^2}$ explicitly assumes statistical independence of the SM continuous-momentum uncertainty and the lattice node-spacing uncertainty — the leaf flags this as a plausible-but-not-derived assumption (the SM bound arises in any single Brillouin zone; the lattice floor arises from Nyquist resolution independent of Bloch state). Methodology bound is properly disclosed, which lands the entry in the 0.7 rubric band. No entry-level dependencies — $\ell_{node}$ is treated as a framework input.
- strengthen-by:
  - Derive statistical independence of SM continuous-momentum uncertainty and lattice node-spacing uncertainty from the underlying Bloch-state theory of the discrete-graph wavefunction, OR derive the corrected combination rule (covariance-aware) if the variances are not independent

---

## Schrödinger Equation from Paraxial Envelope (Mechanism, Not Independent Derivation)
<!-- id: clm-7zuwtm -->

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

### Quality
- confidence: 0.50
- solidity: 0.50 (use as input only, don't build deeper)
- rationale: Paraxial factoring of Klein-Gordon to recover free-particle Schrödinger is standard math; spatial modulation $\varepsilon_{eff}(\mathbf{r})$ recovering on-site potential $V(\mathbf{r})$ is leading-order linear-in-$\chi$ (correctly disclosed). The substantively open element is the Klein-Gordon emergence step itself: a localized inductive load (topological defect with $\omega_m = mc^2/\hbar$) is asserted to produce a spatially uniform $(mc/\hbar)^2 \mathbf{A}$ mass term in the wave equation — but a localized load mathematically produces a localized $\delta(\mathbf{r}-\mathbf{r}_0)$ source, not a uniform background coefficient. This step is asserted by analogy rather than derived, lands the entry at the 0.5 rubric band. No entry-level scored dependencies; the Born rule cross-reference points at a sister leaf (`ohmic-decoherence-born.md`) not yet a separate claim-quality entry.
- strengthen-by:
  - Derive the spatially uniform Klein-Gordon mass term from the LC network's response to a localized topological defect (e.g., via long-wavelength averaging over distributed knot density, or via spectral analysis showing the localized resonance acts as a uniform background mode for waves in the surrounding medium)
  - Provide the explicit derivation of hydrogenic energy levels from the impedance-matching condition $2\pi r = n\lambda$ (currently cross-referenced to Vol 2 Ch 7, not present in this leaf)

---

## Born Rule from Ohmic Measurement Work
<!-- id: clm-ldmvwi -->

- $P(\text{click} \mid x_n) = |\partial_t \mathbf{A}(x_n)|^2 / \int |\partial_t \mathbf{A}(\mathbf{x})|^2\, d^3x \equiv |\Psi|^2$
- _Specific Claims_
  - A macroscopic detector couples to the lattice $\mathbf{A}$-field via a resistive mechanical load — by Axiom 1's impedance algebra, $1\,\Omega \equiv \xi_{topo}^{-2}\,\text{kg/s}$ — and extracts kinetic energy.
  - Classical Joule heating ($P = V^2/R$) over interval $\Delta t$ gives $W_{extracted} \propto |\partial_t \mathbf{A}(x_n)|^2 / Z_{detector} \cdot \Delta t$.
  - In a stochastic thermal substrate, the probability that extracted work triggers a macroscopic discrete event ("click") scales with $|\partial_t \mathbf{A}|^2$, identifying $P(\text{click} \mid x_n) \equiv |\Psi|^2$ — the Born rule as the thermodynamic equation for momentum extraction from a wave-bearing lattice by a thresholded Ohmic load.
  - Decoherence is the irreversible thermalization of the spatial pressure wave at the detector, attenuating interference gradients.
- _Specific Non-Claims and Caveats_
  - Does NOT derive the entire QM measurement formalism — only the $|\Psi|^2$ scaling of click probability.
  - The "click probability $\propto$ extracted work" identification is asserted as a thermal-substrate stochastic property; it is plausible (consistent with thresholded thermal detector physics) but is NOT derived from the four AVE axioms in this leaf.
  - Does NOT address the spin-statistics theorem or fermion anti-symmetric wavefunction structure — those are separate claims.
  - The detector model is a thresholded Ohmic load; non-thresholded or quantum-coherent detectors are out of scope.

> **Leaf references:** [`dynamics/ch3-quantum-signal-dynamics/ohmic-decoherence-born.md`](./dynamics/ch3-quantum-signal-dynamics/ohmic-decoherence-born.md).

### Quality
- confidence: 0.55
- solidity: 0.55 (use as input only, don't build deeper)
- rationale: The classical Joule-heating chain (Axiom 1 impedance + $V^2/R$ + $V \sim \partial_t \mathbf{A}$) is sound algebra. The substantive open element is the **probability identification step**: "in a stochastic thermal substrate, click probability $\propto$ extracted work" is asserted as a thermal-substrate stochastic property rather than derived from an explicit stochastic-threshold model — plausible (consistent with thresholded thermal detector physics) but lands the entry at the 0.55 rubric band. No entry-level scored dependencies (Axiom 1 + Axiom 2's $\xi_{topo}$ are framework inputs).
- strengthen-by:
  - Derive the "click probability $\propto$ extracted work" identification from an explicit stochastic-threshold model of thermal detectors (Poisson shot-noise statistics with detector dead-time corrections), not as an asserted thermal-substrate property
  - Derive uniqueness of the $|\Psi|^2$ form vs. alternative powers $|\Psi|^p$ for $p \neq 2$ given the stochastic-threshold detector framework (currently presumes $p = 2$ from the Joule-heating $V^2$ structure but does not establish uniqueness)
  - Validate quantitatively against single-photon detector statistics (detector dead time, non-Poissonian regimes) to bound the regime of applicability

---

## CHSH Violation $|S|_{\max} = 2\sqrt{2}$ (Tsirelson Bound)
<!-- id: clm-zuf7g1 -->

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

### Quality
- confidence: 0.60
- depends-on:
  - clm-ldmvwi — Born Rule from Ohmic Measurement Work (solidity 0.55) [Bell-correlation derivation uses Born rule as one of three ingredients]
- solidity: 0.33 (do not build on, rework needed) [= 0.60 × 0.55]
- rationale: The Bell correlation $E(\hat a, \hat b) = -\cos\theta_{ab}$ and the Tsirelson bound $|S|_{\max} = 2\sqrt{2}$ emerge as algebra given three AVE ingredients (spin-1/2 Möbius half-angle coupling, Axiom 4 binary saturation at measurement, Born rule from Ohmic extraction); hitting Tsirelson exactly is significant corroboration. The substantive open element local to this entry is the structural identification "phase-locked topological thread = lossless short-short LC resonator implementing the Bell correlation" — asserted as a constructive picture, not derived from axioms. The decoherence-onset prediction at $T_{pair} \approx 1.19 \times 10^{10}$ K is genuinely falsifiable (in QGP regimes). Solidity drops from local-confidence 0.60 to 0.33 once the Born rule dependency (`clm-ldmvwi`) is formally tracked — Born rule's 0.55 caps the chain. Spin-1/2 Möbius half-angle coupling remains a sister cross-reference, not yet a separate claim-quality entry.
- strengthen-by:
  - Strengthen Born Rule from Ohmic Measurement Work (`clm-ldmvwi`) — the dominant solidity bottleneck for this entry
  - Derive the structural identification "phase-locked topological thread = lossless short-short LC resonator with $Z_0 \approx 377\,\Omega$, $Q = \infty$" from first principles (currently asserted as a constructive identification of the Bell-correlation carrier)
  - Document the spin-1/2 Möbius half-angle coupling derivation explicitly (currently summarized; the Finkelstein-Misner kink construction needs to be present here or pointed at an explicit derivation leaf)
  - Add a separate claim-quality entry for the spin-1/2 Möbius half-angle coupling derivation so the dependency chain is fully scored

---

## Quantum Foam as RMS Noise; Virtual Particles as Failed Topologies
<!-- id: clm-t1okz0 -->

- _Specific Claims_
  - The "Quantum Foam" of standard cosmology is reframed as the irreducible thermal RMS noise floor of the LC network at $T > 0$ — the chaotic baseline electrical AC transients, not a literal boiling of geometry.
  - "Virtual particles" are reframed as **failed topologies**: transient localized phase twists from thermal node noise that lack the sustained inductive tension to close into a stable unknot, unwinding back into the noise floor.
  - This provides a deterministic mechanical origin for Zero-Point Energy bounded by the finite local node geometry.
- _Specific Non-Claims and Caveats_
  - Does NOT claim AVE solves the Cosmological Constant Problem at the formula level — the leaf cites the $\sim 120$-orders-of-magnitude discrepancy as motivation, but does not derive the observed dark energy density from the noise-floor reframing in this leaf. Cosmological-constant resolution lives in the Vol 3 dark-energy / phantom-energy chain (lattice latent-heat reinterpretation), not in Vol 1 Ch.3.
  - The "failed topologies" picture is **interpretive**; it does not produce new observables relative to standard QFT virtual-particle calculations at the perturbative level. Falsifiability rests on unrelated AVE predictions (running $\alpha$, GUP cutoff, etc.), not on the foam-as-noise reframing per se.

> **Leaf references:** [`dynamics/ch3-quantum-signal-dynamics/quantum-foam-virtual.md`](./dynamics/ch3-quantum-signal-dynamics/quantum-foam-virtual.md).

### Quality
- confidence: 0.70
- solidity: 0.70 (ok to build on, see caveats)
- rationale: The reframe — "Quantum Foam = irreducible thermal RMS noise of the LC network at $T > 0$" and "virtual particles = failed topologies (transient phase twists lacking sustained inductive tension to close into stable unknots)" — is a coherent ontological reinterpretation given Axiom 1's discrete LC network. The claim-quality entry correctly self-bounds: this is interpretive, not a new prediction; doesn't claim cosmological-constant resolution at the formula level; falsifiability rests on unrelated AVE predictions. Methodology is properly disclosed, lands the entry at the 0.7 rubric band. No entry-level scored dependencies.
- strengthen-by:
  - Quantitatively map AVE thermal-noise-floor predictions to specific QFT virtual-particle calculations at the perturbative level, establishing operational equivalence (or producing a falsifiable divergence)
  - Connect to the Vol 3 dark-energy / phantom-energy chain to clarify what the "failed topologies" reframe predicts (vs reframes) about cosmological-constant magnitude

---

## Asymptotic Hubble Constant $H_\infty$ and MOND $a_0$ (Vol 1 Derivation; Cross-Cutting Caveats)
<!-- id: clm-m3z5ux -->

Vol 1 Ch.4.5 contains the original $H_\infty = 28\pi m_e^3 cG/(\hbar^2\alpha^2) \approx 69.32$ km/s/Mpc derivation and the MOND $a_0 = cH_\infty/(2\pi) \approx 1.07\times 10^{-10}$ m/s² hoop-stress projection. The substantive boundary caveats are catalogued in the [vol3 Asymptotic Hubble Constant entry](../vol3/claim-quality.md) and [vol3 MOND Acceleration Scale entry](../vol3/claim-quality.md). Vol 1-specific notes:

- _Specific Claims_
  - The two formulae are derived once in Vol 1 Ch.4.5 from the canonical hardware scales $\{\ell_{node}, \alpha, G\}$ + the Unruh-Hawking de Sitter horizon temperature; downstream chapters reuse them.
  - The hoop-stress projection $a_{genesis} = a_r/(2\pi)$ applies the classical continuum-mechanics result $T = F_r/(2\pi)$ to a 1D closed topological loop embedded in a 3D radially expanding manifold.
- _Specific Non-Claims and Caveats_
  - The Hubble-derivation "geometric-consistency-proof" caveat (the Machian $\xi$ embeds $R_H \equiv c/H_\infty$ in the definition of $G$) lives in the Vol 3 lattice-genesis leaf, not in Vol 1 Ch.4.5. The Vol 1 derivation should not be summarized as an independent ab-initio prediction of $H_0$ without consulting the Vol 3 claim-quality entry.
  - The MOND $a_0$ deficit (-10.7%) and the Pitfall #4 (no MOND drag at high $g$, $S(g_N/a_0) = 0$ when $g_N \gg a_0$) are documented in detail in the vol3 sidecar; flagged here because Vol 1 introduces the formula.
  - Vol 1 dark-sector framings ("Bullet Cluster as decoupled refractive shockwave"; "DAMA/LIBRA vs XENON as transverse-shear impedance mismatch") are **interpretive reinterpretations**, not quantitative predictions. They reframe established observations within the LC-substrate ontology but do not output new numerical values to test.

> **Leaf references:** [`dynamics/ch4-continuum-electrodynamics/mond-hoop-stress.md`](./dynamics/ch4-continuum-electrodynamics/mond-hoop-stress.md); [`dynamics/ch4-continuum-electrodynamics/dark-sector.md`](./dynamics/ch4-continuum-electrodynamics/dark-sector.md); [`dynamics/ch4-continuum-electrodynamics/bullet-cluster.md`](./dynamics/ch4-continuum-electrodynamics/bullet-cluster.md). Cross-cutting boundary detail in [vol3 Asymptotic Hubble Constant and MOND entries](../vol3/claim-quality.md).

### Quality
- confidence: 0.60
- depends-on:
  - clm-0ktpcn — Golden Torus α Derivation (solidity *pending*) [for $H_\infty$'s $\alpha^{-2}$ factor]
  - clm-5xon03 — Zero-Parameter Closure Status (solidity *pending*) [for the consistency-proof framing of $H_\infty$]
- solidity: *pending*
- rationale: The $H_\infty = 28\pi m_e^3 cG/(\hbar^2\alpha^2)$ formula is correctly disclosed as a consistency-proof, not an independent ab-initio prediction (Machian $\xi$ embeds $R_H \equiv c/H_\infty$ in $G$'s definition; one identity in $(G, H_\infty)$, not two). The MOND $a_0 = cH_\infty/(2\pi)$ hoop-stress projection produces a $-10.7\%$ deficit vs empirical $1.2\times 10^{-10}$ m/s² — a real numerical gap. Local confidence is held below 0.7 because the underlying `mond-hoop-stress.md` leaf carries an unresolved longitudinal wave-speed formula ($v_L = \sqrt{2G/\rho} = \sqrt{2}c$ vs standard isotropic-elasticity $v_L = c\sqrt{10/3} \approx 1.826c$ for $K=2G$), and the hoop-stress projection factor $1/(2\pi)$ is asserted from classical continuum mechanics rather than derived from AVE micropolar dynamics. (Solidity dropped from 0.33 to 0.17 in 2026-05-06 session as both `clm-0ktpcn` and `clm-5xon03` rebound to body-topology dependencies; the Closure Status now-0.28 is the tighter bottleneck.)
- strengthen-by:
  - Resolve the longitudinal wave speed formula in `mond-hoop-stress.md` (currently $\sqrt{2}c$; standard isotropic elasticity at $K=2G$ gives $c\sqrt{10/3}$); either derive the AVE-specific formula from the micropolar / chiral LC continuum (which decouples transverse propagation from bulk modulus) or correct the leaf
  - Derive the hoop-stress projection factor $1/(2\pi)$ from AVE's micropolar dynamics rather than importing the classical continuum-mechanics result
  - Close the MOND $a_0$ -10.7% deficit by carrying higher-order corrections OR by re-deriving the hoop-stress geometry from AVE first principles
  - Strengthen Golden Torus α Derivation (`clm-0ktpcn`); the $\alpha^{-2}$ factor in $H_\infty$ amplifies α's solidity into the strongest dependence
  - Close the Hubble identity into a true downstream prediction by deriving $G$ from local thermodynamic balance independent of $R_H$ (echoes the Closure Status entry)

---

## Macroscopic Yield Stress $\tau_{yield}$ — Order-of-Magnitude Bound, Not Precision
<!-- id: clm-8ep2b4 -->

- $\tau_{yield} = (\rho_{bulk} c^2)\cdot(6\,\mathcal{V}_{crossing})\cdot(p_c/8\pi) \approx 1.04\times 10^{22}$ Pa
- _Specific Claims_
  - The macroscopic yield stress is constructed from baseline bulk energy density $\rho_{bulk}c^2$, the per-crossing topological halo volume ($6\,\mathcal{V}_{crossing} = \mathcal{V}_{total} = 2.0$, FEM-verified to 0.13%), and the geometric porosity factor $\alpha = p_c/8\pi$.
  - The Sagnac-RLVE rotational-shear interferometer is proposed as a tabletop falsification test; the predicted phase shift scales with rotor density and shear rate, distinct from Lense-Thirring (which scales with Newtonian potential).
- _Specific Non-Claims and Caveats_
  - The "Asteroid Belt / Oort Cloud as transition traps at the saturation isocline" framing is an **interpretive prediction**, not a quantitative match to observed orbital-debris distributions. Specific numerical agreement (where present) lives in the vol3 solar-system entries.
  - The Sagnac-RLVE proposal requires the $1000:1$ asymmetric chevron geometry (1 µm tips against 1 mm troughs). The expected phase-shift magnitude is not given in this leaf; falsifiability is asserted in principle, not characterized in detail.
  - "Mutual inductance is annihilated ($\eta \to 0$) inside saturated regions" is the same claim as cross-cutting Symmetric Saturation ($Z = Z_0$ invariant, $\Gamma = 0$); it is not "drag goes to zero from infinity" — drag is bounded and structured throughout the regimes.

> **Leaf references:** [`dynamics/ch4-continuum-electrodynamics/magnetic-saturation.md`](./dynamics/ch4-continuum-electrodynamics/magnetic-saturation.md). Cross-cutting: see Symmetric vs Asymmetric Saturation.

### Quality
- confidence: 0.50
- depends-on:
  - clm-0ktpcn — Golden Torus α Derivation (solidity *pending*) [for $p_c = 8\pi\alpha$ in the porosity factor]
- solidity: *pending*
- rationale: The formula $\tau_{yield} = (\rho_{bulk} c^2)\cdot(6\,\mathcal{V}_{crossing})\cdot(p_c/8\pi)$ uses the proton-specific Borromean topology ($\mathcal{V}_{total} = 6\,\mathcal{V}_{crossing} = 2.0$, FEM-verified to 0.13% for the proton's 6³₂ Borromean) as a load-bearing factor in a formula presented as governing **macroscopic / cosmological** lattice mechanics (planetary slipstreams, asteroid belts, dark-sector boundary-layer transitions). The justification for embedding proton-specific topology in a macroscopic vacuum formula is asserted, not derived — this is the substantive open structural question that lands the entry at the 0.5 rubric band. Order-of-magnitude framing is correctly disclosed; quantitative claims (specific $1.04\times 10^{22}$ Pa value, asteroid-belt / Oort-cloud isocline matching) are interpretive at this scope. (Solidity dropped from 0.28 to 0.21 in 2026-05-06 session as `clm-0ktpcn` rebound to depend on `clm-trf3bd`.)
- strengthen-by:
  - Justify (or replace) the use of proton-specific 6-crossing Borromean topology ($\mathcal{V}_{total} = 2.0$) in a formula governing macroscopic / cosmological lattice mechanics; either derive why proton topology is universally embedded in the macroscopic vacuum, or replace with a generic topological factor derived from lattice properties alone
  - Quantify the predicted Sagnac-RLVE phase shift (currently "asserted in principle, not characterized in detail")
  - Quantitatively match "asteroid belt / Oort cloud" formation positions to $\tau_{yield}$ isoclines (currently interpretive, not numerical)
  - Strengthen Golden Torus α Derivation (`clm-0ktpcn`); $p_c = 8\pi\alpha$ enters the formula

---

## Universal Spatial Tension Mass Scaling (Lepton + Nuclear)
<!-- id: clm-zw6mut -->

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

### Quality
- confidence: 0.60
- depends-on:
  - clm-0ktpcn — Golden Torus α Derivation (solidity *pending*) [for muon's $\alpha\sqrt{3/7}$ and tau's $8\pi/\alpha$ sector factors]
  - clm-unk0bd — Electron Body Topology = Unknot (solidity *pending*) [the "ground-state unknot" framing is load-bearing for the lepton mass formula and the "three structural dimensions of the unknot" Cosserat-sector argument]
- solidity: *pending*
- rationale: The cross-scale operator framing — same universal $1/r$ tension governs lepton and nuclear binding — is structurally claimed but the three-Cosserat-sector-to-three-lepton-generation identification (translation/torsion/curvature-twist) is asserted, not derived from the four axioms. Lepton-mass deviations are non-trivial: muon $+1.24\%$, tau $-0.95\%$ — correctly disclosed but not sub-percent. Nuclear methodology is honestly disclosed as **one fitted scalar per nucleus** (Vol 6); the Vol 1 Neon-20 mention is one application. The reported "$<0.001\%$ Neon-20 residual" is the optimizer convergence tolerance, not an independent prediction error — claim-quality entry correctly flags this. Local confidence held at 0.6 because the structural identifications and the residual lepton-mass percentages are real open work. **Body-topology dependency (2026-05-06 session):** the cited leaves (`scale-invariance.md`, `scale-invariant-predictions.md`, `mass-unification.md`) explicitly use the "ground-state unknot" framing for the electron and "the three structural dimensions of the unknot" for the lepton-generation hierarchy. Under `clm-unk0bd`'s solidity 0.40 (cross-leaf inconsistency vs `clm-trf3bd`), this entry inherits the lower bound. If the body-topology conflict resolves in favor of the trefoil, the Cosserat-sector mapping needs rederivation in trefoil terms; the asserted "three structural dimensions" argument is unknot-specific.
- strengthen-by:
  - Derive the three-Cosserat-sectors-to-three-lepton-generations identification (translation/torsion/curvature-twist) from the four axioms (currently a structural identification with sector-specific coupling factors $\alpha\sqrt{3/7}$ and $8\pi/\alpha$ that are asserted, not derived)
  - Reduce the lepton-mass deviations (muon $+1.24\%$, tau $-0.95\%$) by carrying higher-order corrections in the Cosserat sector chain
  - Strengthen Golden Torus α Derivation (`clm-0ktpcn`); α appears in both muon and tau sector factors
  - Resolve body-topology conflict (`clm-trf3bd` vs `clm-unk0bd`) at author level. The current leaves' "ground-state unknot" formulation is load-bearing here; under a trefoil resolution, both the lepton mass formula and the Cosserat-sector hierarchy need rederivation.
  - Add a separate claim-quality entry for the proton mass derivation; it feeds the Vol 6 nuclear methodology and the Vol 1 Neon-20 application as an unscored upstream input

---

## Universal Operators (Z, S, Γ) — Same Function, Different Scales
<!-- id: clm-gdd70j -->

The eight Ch.6 universal operators are the engine-level shared code paths. Boundary entries:

- _Specific Claims_
  - Each operator (Z impedance, S saturation, Γ reflection, U pairwise, Y→S multiport, $\lambda_{\min}$ eigenvalue target, FFT spectral, $\Gamma_{pack}$ packing) is implemented as **one function** called by every domain — the cross-scale identity is computational, not analogical.
  - The cross-scale Z table spans 8 distinct domains (vacuum lattice, plasma, seismic, gravitational, protein, lattice-Boltzmann fluid, galactic, antenna), all routed through `scale_invariant.impedance(mu, eps)`.
- _Specific Non-Claims and Caveats_
  - Operator-identity claims are **structural** (same code path), not predictive at any single scale. Numerical agreement at any specific application is the responsibility of the per-domain leaf, not the operator's universal status.
  - The "Universal Reflection Coefficient" cross-scale list (Pauli exclusion at $\Gamma = -1$, Moho seismic $\Gamma \approx 0.17$, antenna $S_{11}$, etc.) exemplifies this: same operator, different inputs $(Z_1, Z_2)$, different physical phenomena. Summaries that quote a list of $\Gamma$ values as "AVE predicts" should be qualified with "the operator is universal; the inputs come from per-domain physics".
  - Cross-cutting [vol3 Seismic Reflection Coefficient (Moho) entry](../vol3/claim-quality.md) makes this distinction explicit.

> **Leaf references:** [`operators-and-regimes/ch6-universal-operators/impedance-operator.md`](./operators-and-regimes/ch6-universal-operators/impedance-operator.md); [`operators-and-regimes/ch6-universal-operators/saturation-operator.md`](./operators-and-regimes/ch6-universal-operators/saturation-operator.md); [`operators-and-regimes/ch6-universal-operators/reflection-coefficient.md`](./operators-and-regimes/ch6-universal-operators/reflection-coefficient.md); [`operators-and-regimes/ch6-universal-operators/pairwise-potential.md`](./operators-and-regimes/ch6-universal-operators/pairwise-potential.md); [`../common/operators.md`](../common/operators.md) (Op1 universal-impedance formula cited by the common operator catalog).

### Quality
- confidence: 0.80
- solidity: 0.80 (ok to build on, see caveats)
- rationale: The eight universal operators (Z, S, Γ, U, Y→S, λ_min, FFT, Γ_pack) are framework-level constructs derived from Axiom 4's saturation kernel and from impedance/reflection algebra; the cross-scale identity is **structural** (same code path called by every domain), not predictive at any single scale. The claim-quality entry correctly self-bounds — operator identity claims do not certify per-domain numerical agreement, which is the responsibility of each per-domain leaf. This separation of concerns is exactly right; the entry's only caveat is that summaries which list cross-domain $\Gamma$ values as "AVE predicts" are misreading the structural-identity claim. No entry-level scored dependencies — operators are framework-level.
- strengthen-by:
  - none entry-local — per-domain numerical validations live in their own claim-quality entries; this entry's claim is just the operator-reuse structural identity, which is correctly bounded

---

## Four-Regime Map — Boundary Derivations are Sector-Dependent
<!-- id: clm-b2anl4 -->

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

### Quality
- confidence: 0.75
- depends-on:
  - clm-0ktpcn — Golden Torus α Derivation (solidity *pending*) [for $r_1 = \sqrt{2\alpha}$ numerical value]
- solidity: *pending*
- rationale: The boundary derivations are individually sound — $r_1 = \sqrt{2\alpha}$ from leading-order Taylor truncation of $S(r)$ matching the lattice's self-coupling $\alpha$; $r_3 = 1$ axiomatic from Axiom 4 ($S = 0$); $r_2 = \sqrt{3}/2$ from $Q = 1/S = \ell_{\min}$ with $\ell_{\min} = 2$ for the spin-2 sector. The substantive open element is the **sector-specific identification of $\ell_{\min}$** (scalar/vector/spin-2 ℓ_min values are stated as "minimum non-trivial multipole" rather than derived from a specific axiom-grounded harmonic decomposition). Local confidence held at 0.75. Solidity bounded by α via $r_1$'s numerical value. The structural form $r_1 = \sqrt{2\alpha}$ survives any reasonable α value; the **numerical** boundary at 0.121 is α-dependent. (Solidity dropped from 0.41 to 0.31 in 2026-05-06 session as `clm-0ktpcn` rebound to depend on `clm-trf3bd`.)
- strengthen-by:
  - Derive the sector-specific $\ell_{\min}$ values (scalar 0, vector 1, spin-2 2, ...) from axiom-grounded multipole decomposition rather than pattern-matching to "minimum non-trivial multipole"
  - Strengthen Golden Torus α Derivation (`clm-0ktpcn`); $r_1 = \sqrt{2\alpha}$ inherits α's solidity for numerical evaluation

---

## Domain Catalog Operating-Point Examples
<!-- id: clm-82dxbj -->

The Ch.7.2 domain catalog tabulates $r$ values across EM, gravitational, BCS, magnetic, nuclear, GW, and galactic domains. Vol 1-specific tripwires:

- _Specific Claims_
  - Solar surface, white dwarf interiors, lab capacitors and magnets, MRI scanners, LIGO GW signals: all explicitly sit deep in **Regime I** ($r \ll 1$), justifying use of unmodified standard equations.
  - Neutron star at $1.4\,M_\odot$, $R = 10$ km: $\varepsilon_{11} \approx 1.46 > 1$ — **Regime IV** (ruptured topology). This is the AVE analog of the Buchdahl limit.
  - Black hole at $r_s = 2GM/c^2$: $\varepsilon_{11} = 7/2 = 3.5$ (the factor 7 arises from the K4/SRS lattice's 7 compliance modes via $\nu_{vac} = 2/7$). Deep Regime IV.
  - LIGO GW150914 strain $h \sim 10^{-21}$ corresponds to $r \sim 10^{-20}$ — "the most deeply linear measurement in physics".
- _Specific Non-Claims and Caveats_
  - The neutron-star Regime IV identification (lattice-strain $> 1$) is **the AVE-internal compactness bound**; the cross-cutting [vol3 AVE Compactness Limit entry](../vol3/claim-quality.md) elaborates that this is stricter than the GR Buchdahl bound but is **not** validated against observed neutron-star equations of state. It is what the AVE bound implies given canonical NS parameters.
  - The galactic-domain operating point uses the empirical $a_0 \approx 1.2\times 10^{-10}$ m/s², not the AVE-derived $a_0 \approx 1.07\times 10^{-10}$. Mixing the two leads to inconsistent regime locations.
  - LIGO's "sub-$\alpha$" classification (the $\Delta S = 0.007$ correction at NS-merger surface strain $h \sim 0.01$ is below the lattice's own $\alpha \sim 1/137$ coupling) means AVE corrections are **physically unresolvable** at LIGO sensitivities — not zero, but below the noise floor of the lattice itself.

> **Leaf references:** [`operators-and-regimes/ch7-regime-map/domain-catalog.md`](./operators-and-regimes/ch7-regime-map/domain-catalog.md); [`operators-and-regimes/ch7-regime-map/experimental-design-space.md`](./operators-and-regimes/ch7-regime-map/experimental-design-space.md). Cross-cutting: [vol3 AVE Compactness Limit](../vol3/claim-quality.md).

### Quality
- confidence: 0.70
- depends-on:
  - clm-b2anl4 — Four-Regime Map (solidity *pending*) [uses $r_1, r_2, r_3$ boundaries to classify domains]
- solidity: *pending*
- rationale: The catalog correctly applies the four-regime structure to specific physical systems (Solar surface, WD interiors, lab fields, NS interior, BH horizons, LIGO GW signals); the claim-quality entry honestly discloses that the AVE-internal compactness bound ($R_{\min} = 7GM/c^2$) is stricter than the GR Buchdahl bound but is **not validated** against observed neutron-star equations of state, and that the galactic-domain operating point uses empirical $a_0$ (not AVE-derived). Local confidence is sound for the application work. Solidity is heavily bounded transitively through Four-Regime Map's α dependency — every $r$ value tabulated for a specific system inherits regime-boundary numerical solidity. (Solidity dropped from 0.29 to 0.22 in 2026-05-06 session as `clm-b2anl4` rebound transitively through `clm-0ktpcn` to `clm-trf3bd`.)
- strengthen-by:
  - Validate the AVE-internal compactness bound ($R_{\min} = 7GM/c^2$) against observed neutron-star equations of state (currently disclosed as not-validated)
  - Reconcile the galactic operating-point's use of empirical $a_0 \approx 1.2\times 10^{-10}$ with the AVE-derived $a_0 \approx 1.07\times 10^{-10}$ from Asymptotic Hubble Constant + MOND (`clm-m3z5ux`); using empirical introduces an undeclared empirical input
  - Strengthen Four-Regime Map (`clm-b2anl4`); regime-boundary numerical solidity propagates here
  - Strengthen Golden Torus α Derivation (`clm-0ktpcn`) transitively

---

## Vacuum Bulk Mass Density and Shear Modulus
<!-- id: clm-crbl60 -->

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

### Quality
- confidence: 0.65
- depends-on:
  - clm-0ktpcn — Golden Torus α Derivation (solidity *pending*) [for $p_c = 8\pi\alpha$ in $\rho_{bulk}$ and $\alpha$ in $\nu_{kin} = \alpha c \ell_{node}$]
- solidity: *pending*
- rationale: $\rho_{bulk}$ and $G_{vac} = \rho_{bulk}c^2$ are dimensionally constructed from $\xi_{topo}$, $\mu_0$, $p_c$, $\ell_{node}$, $c$ — the construction itself is sound algebra. The Cauchy relation $K_{vac} = 2G_{vac}$ is the same operating point disclosed in the EMT entry and is structurally consistent. The substantive open element is the **identification $\kappa \equiv \alpha$** for the kinematic mutual inductance $\nu_{kin}$ — asserted as a consequence of the porosity argument but not derived. The "$\nu_{kin}$ close to liquid water" comparison is order-of-magnitude only. The distinction $G_{vac}$ (3D continuum) vs $G_{string}$ (1D edge tension, $\sim 10^{12}$ smaller) is correctly disclosed. (Solidity dropped from 0.36 to 0.27 in 2026-05-06 session as `clm-0ktpcn` rebound to depend on `clm-trf3bd`.)
- strengthen-by:
  - Derive the $\kappa \equiv \alpha$ identification (geometric scattering threshold = packing-fraction-derived self-coupling) from first principles rather than asserting
  - Strengthen Golden Torus α Derivation (`clm-0ktpcn`); $\rho_{bulk}$, $G_{vac}$, and $\nu_{kin}$ all inherit α numerically through $p_c$ and $\nu_{kin}$'s factor

---

## Implosion Paradox $\to$ Micropolar Vacuum
<!-- id: clm-9gh0a1 -->

- _Specific Claims_
  - A classical Cauchy elastic solid satisfying MacCullagh's transverse-wave condition ($\lambda = -\mu$) yields $K = -\mu/3 < 0$ — runaway implosion.
  - This forces the substrate to be a **Chiral LC (Micropolar) Continuum** with independent rotational degrees of freedom, decoupling transverse-wave propagation from the bulk modulus and permitting $K > 0$ alongside pure transverse gauge-boson propagation.
- _Specific Non-Claims and Caveats_
  - This is a **structural / no-go argument**: it rules out a Cauchy substrate, motivating the micropolar Chiral LC continuum. It does not derive the chiral SRS lattice geometry (that comes from the K4 packing / EMT closure separately).
  - Does NOT claim micropolar continua are uniquely the AVE substrate; the leaf rules out one alternative (Cauchy) and the rest of Vol 1 motivates the specific chiral choice.

> **Leaf references:** [`axioms-and-lattice/ch2-macroscopic-moduli/implosion-paradox.md`](./axioms-and-lattice/ch2-macroscopic-moduli/implosion-paradox.md).

### Quality
- confidence: 0.85
- solidity: 0.85 (ok to build on)
- rationale: A clean structural / no-go argument grounded in standard continuum mechanics: a classical Cauchy elastic solid satisfying MacCullagh's transverse-wave condition ($\lambda = -\mu$) requires $K = -\mu/3 < 0$, which is unphysical. The claim-quality entry correctly bounds this as a no-go argument that *rules out* a Cauchy substrate — it does not claim to uniquely identify the AVE substrate as micropolar (the chiral SRS specifics come from K4 packing / EMT, separately disclosed). No entry-level scored dependencies — pure classical continuum mechanics + Axiom 1's transverse-wave constraint.
- strengthen-by:
  - none — the no-go argument is correctly self-bounded; further pin-down of "the substrate must be chiral SRS specifically" lives in EMT (`clm-9s9apq`) and Vacuum Bulk Mass Density (`clm-crbl60`) entries

---

## Topo-Kinematic Isomorphism $[Q] \equiv [L]$
<!-- id: clm-dfaiwj -->

- $\xi_{topo} \equiv e/\ell_{node}$ [C/m]; $1\,\Omega = \xi_{topo}^{-2}$ kg/s
- _Specific Claims_
  - The Axiom 2 mechanism reframes charge as a discrete geometric dislocation (localized phase twist); the SI dimensions of charge and length become identified at scaling $\xi_{topo}$.
  - The full SI-dimensional table (V↔F, I↔v, Z↔kinematic impedance, L↔m, C↔1/k, $\mu_0$↔linear density, $\varepsilon_0$↔inverse tension) follows from this single identification.
- _Specific Non-Claims and Caveats_
  - This is a **dimensional isomorphism**, not a claim that charge "becomes" length in any operationally measurable sense at the engineering scale. SI conversions are exact within the framework's definitions; experimental discrimination depends on AVE's downstream predictions, not on the isomorphism itself.
  - $\xi_{topo}$ is INVARIANT-C2 in the cross-volume invariants (Vol 2/4/5 reuse it for atomic mappings, circuit engineering, biological mass/stiffness translations). Its canonical leaf-level definition lives in Vol 5; Vol 1 establishes it via Axiom 2 mechanism.

> **Leaf references:** [`axioms-and-lattice/ch1-fundamental-axioms/axiom-definitions.md`](./axioms-and-lattice/ch1-fundamental-axioms/axiom-definitions.md) (Axiom 2 mechanism); [`axioms-and-lattice/ch2-macroscopic-moduli/constitutive-moduli.md`](./axioms-and-lattice/ch2-macroscopic-moduli/constitutive-moduli.md); [`axioms-and-lattice/ch2-macroscopic-moduli/topo-kinematic-isomorphism.md`](./axioms-and-lattice/ch2-macroscopic-moduli/topo-kinematic-isomorphism.md). Bound also asserted at invariant level: CLAUDE.md INVARIANT-C2.

### Quality
- confidence: 0.80
- solidity: 0.80 (ok to build on, see caveats)
- rationale: $\xi_{topo} = e/\ell_{node}$ is direct from Axiom 2's topo-kinematic isomorphism mechanism; the SI-dimensional table (V↔F, I↔v, Z↔kinematic impedance, L↔m, C↔1/k, μ_0↔linear density, ε_0↔inverse tension) follows from this single identification by dimensional algebra. The claim-quality entry correctly self-bounds: this is a **dimensional isomorphism**, not an operational claim that charge becomes length at the engineering scale. The cross-volume reuse (Vol 2 atomic mappings, Vol 4 circuit engineering, Vol 5 biology mass/stiffness translations) is structural. INVARIANT-C2 carries the same bound at project-wide invariant level. No entry-level scored dependencies — Axiom 2's mechanism is framework-input.
- strengthen-by:
  - none entry-local — the isomorphism is correctly self-bounded as a dimensional identity given Axiom 2's mechanism

---

## Pauli Exclusion as Impedance Reflection (Vol 1 Mechanism Statement)
<!-- id: clm-b9eura -->

- $\Gamma = (Z_{knot} - Z_{vacuum})/(Z_{knot} + Z_{vacuum}) = (0 - 377)/(0 + 377) = -1$
- _Specific Claims_
  - At the saturated knot core, dynamic RF impedance drops to $0\,\Omega$ (RF short circuit); incoming waves at the $377\,\Omega$ vacuum boundary reflect with $\Gamma = -1$ (total phase-reversed reflection).
  - This provides the macroscopic impedance-mismatch mechanism for the Pauli Exclusion Principle and for cross-sectional area in particle physics. Two saturated knots cannot occupy the same coordinates because their respective $0\,\Omega$ boundaries reflect each other's inductive phase energy.
  - Solid matter emerges from vacuum wave mechanics through this macroscopic impedance reflection.
- _Specific Non-Claims and Caveats_
  - The "$Z_{knot} = 0$" boundary refers to **dynamic RF impedance** (transverse-wave reflection condition), not static DC impedance. Confusion of the two leads to the apparent contradiction with the Vol 3 Einstein-field-equation leaf which says "$Z \to 0$ at the horizon" while GW leaves say "$Z = Z_0$ invariant" (see [vol3 Einstein Field Equation Reinterpretation entry](../vol3/claim-quality.md) and followups file for the unresolved cross-leaf tension).
  - Does NOT claim derivation of the spin-statistics theorem or anti-symmetric wavefunction structure; the impedance-mismatch argument provides the *mechanism* for exclusion (no-overlap), not the algebraic structure of fermion statistics.
  - The cross-domain $\Gamma \to -1$ translation matrix (particle confinement / plasma cutoff / superconductor / entanglement thread) is a **structural-identity** claim across Vol 1, Vol 1 EM, Vol 3 condensed matter, Vol 1 quantum-info — same operator, different sectors.

> **Leaf references:** [`dynamics/ch3-quantum-signal-dynamics/zero-impedance-boundary.md`](./dynamics/ch3-quantum-signal-dynamics/zero-impedance-boundary.md); [`dynamics/ch3-quantum-signal-dynamics/phase-locked-topological-thread.md`](./dynamics/ch3-quantum-signal-dynamics/phase-locked-topological-thread.md) (Universal $\Gamma \to -1$ Translation Matrix). Cross-cutting tension flagged in [vol3 Einstein Field Equation Reinterpretation](../vol3/claim-quality.md) and `kb-claims-boundaries-followups.md` (interpretive-tension entry).

### Quality
- confidence: 0.55
- depends-on:
  - clm-efo113 — Master Equation EFT Validity (solidity 0.50) [the saturated-knot $Z \to 0$ behavior depends on master-equation dynamics at saturation]
- solidity: 0.28 (do not build on, rework needed) [= 0.55 × 0.50]
- rationale: The $\Gamma = -1$ formula is straightforward impedance algebra given $Z_{knot} = 0$ and $Z_{vacuum} = 377\,\Omega$. The mechanism chain (saturated knot → $\mu_{eff} \to 0$ → $Z \to 0$ → reflection $\Gamma = -1$ → standing wave = no-overlap = exclusion) shares the same load-bearing dependency as Magnetic-Branch Confinement (`clm-lv3uw1`): the master-equation EFT must remain valid through saturation. A separate concern is the cross-leaf tension flagged in the claim-quality entry: Vol 1 says $Z \to 0$ at the saturated knot core, while Vol 3 GW leaves say $Z = Z_0$ invariant in symmetric saturation — these may describe distinct physical situations (knot core vs GW horizon in symmetric gravity) but the impedance-operator usage is currently ambiguous across leaves. The entry also does NOT derive the spin-statistics theorem or anti-symmetric wavefunction structure from this mechanism — it provides exclusion-by-no-overlap, not the algebraic structure of fermion statistics.
- strengthen-by:
  - Strengthen Master Equation EFT Validity (`clm-efo113`); $\Gamma \to -1$ at saturation depends on master-equation dynamics correctly describing $\mu_{eff} \to 0$
  - Resolve the cross-leaf $Z$-behavior tension between Vol 1 (saturated knot core: $Z \to 0$) and Vol 3 GW horizons ($Z = Z_0$ invariant in symmetric saturation); either disambiguate the contexts explicitly or correct whichever leaf is wrong
  - Provide an axiom-grounded derivation that Pauli exclusion's NO-OVERLAP constraint follows from the impedance mismatch (currently a structural identification, not a derivation that produces fermion statistics)

---

## Discrete Kirchhoff Network Solver Methodology
<!-- id: clm-q39qct -->

Vol 1 Ch.1 §1.5 specifies the explicit-discrete numerical engine that maps the four axioms into Symplectic Euler updates on a graph of $C$-nodes and $L$-edges, and tabulates the master-constants pipeline.

- _Specific Claims_
  - The simulation engine is a strict Discrete Kirchhoff Network Solver (e.g., `simulate_ponder_01_srs_lc_mesh.py`); the continuous PDE evaluations elsewhere in the manuscript are a macroscopic-fluid approximation, not the canonical engine.
  - Edge-strain and node-displacement updates take the explicit Symplectic-Euler form $I_{new} = I_{old} + (\Delta t/L)(V_A - V_B)$ and $V_{new} = V_{old} + (\Delta t/C)(\sum I_{in} - \sum I_{out})$ respectively, enforcing local gauge invariance and energy conservation across the discrete crystal.
  - The §1.5 master-constants table maps each AVE quantity ($\ell_{node}$, $Z_0$, $\alpha$, $V_{yield}$, $\xi_{topo}$, $V_{snap}$, $G$, $S(A)$) to a single derivation source (Axiom 1 / Axiom 2 / Axiom 2 mechanism / Axiom 4 / Ch.8 Golden Torus / derived Ax 1+4).
- _Specific Non-Claims and Caveats_
  - Symplectic Euler is **first-order**; it preserves an approximate energy invariant on bounded steps but is not a long-time-stable symplectic integrator on its own. Quantitative claims that depend on long-horizon integration accuracy require a higher-order method or step-size control; the leaf does not characterize the regime of validity.
  - The §1.5 master-constants pipeline is a **routing summary**, not an independent derivation. Each row's derivation lives in the cited source (notably $\alpha$ in Ch.8 Golden Torus, $G$'s $\xi$ closure in Vol 1 Ch.4 / Vol 3); summarizing this table as "all constants derived in §1.5" misreads the routing.
  - The 3-strut-per-node connectivity assumption is the K4/SRS choice elaborated in Ch.2; this leaf states it as a methodology fixture, not a derivation. The justification for $z = 3$ (over Cauchy-Delaunay $z \approx 6$) lives in `dielectric-rupture.md` (`clm-9s9apq`), not here.

> **Leaf references:** [`axioms-and-lattice/ch1-fundamental-axioms/kirchhoff-network-method.md`](./axioms-and-lattice/ch1-fundamental-axioms/kirchhoff-network-method.md); [`axioms-and-lattice/ch1-fundamental-axioms/lattice-structure.md`](./axioms-and-lattice/ch1-fundamental-axioms/lattice-structure.md) (forward-reference stub).

### Quality
- confidence: *pending*
- depends-on:
  - clm-9s9apq — EMT Consistency Relation (for $z = 3$ chiral-SRS justification used by the 3-strut-per-node connectivity)
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Dielectric Lagrangian and Vector Potential as Mass Flow
<!-- id: clm-yiyyi3 -->

- $\mathcal{L}_{AVE} = \tfrac{1}{2}\epsilon_0|\partial_t\mathbf{A}|^2 - \tfrac{1}{2\mu_0}|\nabla\times\mathbf{A}|^2$; $[\mathbf{A}] = \xi_{topo}^{-1}\,[\text{kg/s}]$
- _Specific Claims_
  - The standard QFT electromagnetic Lagrangian density is recast as bulk continuous mechanical stress (Pa) on the $\mathcal{M}_A$ manifold via the topological conversion $\xi_{topo} = e/\ell_{node}$; capacitive edge energy plays the role of kinetic, inductive node energy the role of potential.
  - Dimensional analysis with $\xi_{topo}$ substitution shows $[\mathbf{A}] = \xi_{topo}^{-1}\,[\text{kg/s}]$ (mass flow rate scaled by $\xi_{topo}^{-1}$), and the kinetic-energy density $\tfrac{1}{2}\epsilon_0|\partial_t\mathbf{A}|^2$ reduces to $[\text{N/m}^2]$ once $\epsilon_0 \equiv \xi_{topo}^2[\text{N}^{-1}]$ cancels the topological factor.
  - Minimizing the quantum action is therefore mathematically equivalent to minimizing inductive bulk stress in Pa.
- _Specific Non-Claims and Caveats_
  - This is a **dimensional / SI-units identification**: $[\mathbf{A}]$ acquires mass-flow units after multiplying by $\xi_{topo}^{-1}$, but the operational measurement of $\mathbf{A}$ does not change. It is a framework-internal isomorphism, not a new observable.
  - Does NOT derive the form of the Lagrangian from the four axioms; the standard EM Lagrangian is taken from Maxwell theory and rewritten in mechanical units. The identification of $\mathcal{T}$ with capacitive energy and $\mathcal{U}$ with inductive energy follows from Axiom 1 + the choice of $\mathbf{A}$ as the canonical field variable (whose generalized velocity is $\mathbf{E}$).
  - $\xi_{topo}$ is INVARIANT-C2; this leaf is one of the canonical Vol 1 sites where it is exercised (see `clm-dfaiwj` Topo-Kinematic Isomorphism for the standalone identity).

> **Leaf references:** [`dynamics/ch3-quantum-signal-dynamics/dielectric-lagrangian.md`](./dynamics/ch3-quantum-signal-dynamics/dielectric-lagrangian.md).

### Quality
- confidence: *pending*
- depends-on:
  - clm-dfaiwj — Topo-Kinematic Isomorphism $[Q] \equiv [L]$ (for $\xi_{topo} = e/\ell_{node}$ used throughout)
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Paley-Wiener / Quantum Hilbert-Space Isomorphism
<!-- id: clm-yc7fgm -->

- $\Psi(\mathbf{x},t) = \mathbf{A}(\mathbf{x},t) + i\,\mathcal{H}_{transform}[\mathbf{A}(\mathbf{x},t)]$
- _Specific Claims_
  - The $\mathcal{M}_A$ lattice acts as a spatial Nyquist sampling grid; band-limited signals on it form a Reproducing Kernel Hilbert Space — the Paley-Wiener space $PW_{\pi/\ell_{node}}$ with maximum spatial frequency $k_{max} = \pi/\ell_{node}$.
  - The complex quantum state vector $\Psi(\mathbf{x},t)$ is constructed from the real lattice potential $\mathbf{A}(\mathbf{x},t)$ via the standard signal-processing Hilbert transform (analytic-signal extension).
  - The complex Hilbert space of standard QM is **formally identical** to the Paley-Wiener / analytic-signal representation of the discrete vacuum hardware.
- _Specific Non-Claims and Caveats_
  - The identification is a **formal isomorphism** between two function spaces (band-limited signals on a Nyquist grid $\leftrightarrow$ complex QM state vectors) — it does not by itself derive the dynamical evolution (Schrödinger equation), the Born rule, or operator algebra. Those derivations live in sister leaves (`clm-7zuwtm` Schrödinger from circuit, `clm-ldmvwi` Born rule).
  - The Paley-Wiener / analytic-signal construction is **standard signal-processing mathematics**; the AVE-specific claim is the identification of the discrete lattice with the Nyquist grid (Axiom 1), not the analytic-signal machinery itself.
  - Does NOT claim the Hilbert transform is an operationally distinguishing experiment vs. standard QM; once the isomorphism is established, all standard-QM Hilbert-space predictions transfer automatically.

> **Leaf references:** [`dynamics/ch3-quantum-signal-dynamics/paley-wiener-hilbert.md`](./dynamics/ch3-quantum-signal-dynamics/paley-wiener-hilbert.md).

### Quality
- confidence: *pending*
- depends-on:
  - clm-nq2kcc — GUP / Brillouin Zone (same Nyquist / discrete-graph foundation; both rest on Axiom 1's lattice pitch)
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Nonlinear Telegrapher / Euler-Heisenberg $E^4$ / Kerr $\chi^{(3)}$
<!-- id: clm-ph2uux -->

- $U \approx \tfrac{1}{2}\epsilon_0(\Delta\phi)^2 - \tfrac{3}{8\alpha^2}\epsilon_0(\Delta\phi)^4$
- _Specific Claims_
  - The 1D continuous-transmission-line nonlinear telegrapher equation is the dimensional-homogeneity-preserving form on a single-edge limit of the Master Equation, with $\epsilon(\Delta\phi)$ supplied by Axiom 4's saturation kernel.
  - Taylor-expanding $\epsilon(\Delta\phi) = \epsilon_0\sqrt{1-(\Delta\phi/\alpha)^2}$ to leading order produces the $D \propto (\Delta\phi)^3$ Kerr ($\chi^{(3)}$) optical nonlinearity and the $U \propto (\Delta\phi)^4$ correction structurally identical to the **Euler-Heisenberg QED Lagrangian** density.
  - As $\Delta\phi \to \alpha$, the local wave speed $c_{eff} = c_0[1-(\Delta\phi/\alpha)^2]^{-1/4}$ diverges; the high-amplitude peak overruns its base, producing a forward structural shockwave that provides a continuous-mechanical origin for discrete pair-production.
- _Specific Non-Claims and Caveats_
  - The Euler-Heisenberg / Kerr identification is a **structural / dimensional match** at leading order in $\Delta\phi/\alpha$: the AVE expansion produces the same polynomial-in-field structure that QED produces. It does **not** independently derive the Euler-Heisenberg coefficient from the four AVE axioms vs. the QED loop-integral derivation; both arrive at compatible leading-order forms but the higher-order coefficients are derived from different machinery and have not been compared term-by-term.
  - Inherits the same EFT-validity caveat as `clm-efo113` (Master Equation EFT Validity): the 1D telegrapher form drops field-gradient corrections that may matter near $\Delta\phi \to \alpha$.
  - The "shockwave produces pair-production" claim is **mechanical / heuristic**; it does not predict the Schwinger pair-production rate $\propto \exp(-\pi m_e^2 c^3/(eE\hbar))$ from the shockwave dynamics. The $u_{sat}$ Schwinger threshold is treated as an external QED input elsewhere (`clm-9s9apq`).

> **Leaf references:** [`dynamics/ch3-quantum-signal-dynamics/nonlinear-telegrapher.md`](./dynamics/ch3-quantum-signal-dynamics/nonlinear-telegrapher.md).

### Quality
- confidence: *pending*
- depends-on:
  - clm-efo113 — Master Equation EFT Validity (the 1D telegrapher inherits the same EFT-validity caveat near $\Delta\phi \to \alpha$)
  - clm-0ktpcn — Golden Torus α Derivation (the $\alpha$ in $\epsilon(\Delta\phi)$ enters the $1/\alpha^2$ coefficient of the $E^4$ correction)
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Three-Regime Fluidic Classification (Ch.4 Operating Regimes)
<!-- id: clm-xy252u -->

- _Specific Claims_
  - Vol 1 Ch.4.3 categorises the spatial medium into **three** fluidic operating regimes by control parameter $\Delta\phi/\alpha$: Linear Acoustic ($\ll 1$, $C_{eff} \approx C_0$), Non-Linear Tensor ($\to 1$, $C_{eff} \propto 1/\sqrt{1-x^2}$), Dielectric Rupture ($\ge 1$, $\eta \to 0$).
  - The Dielectric Rupture regime is identified with Black-Hole Event Horizons, Tokamak L-H transitions, and thermal fusion ignition limits via the $V_{yield} \approx 43.65$ kV topological yield bound.
  - Linear Maxwell + scalar Newtonian gravity produce negligible error in Regime I; the full nonlinear stress-energy tensors (GR / nonlinear electrodynamics) are required as $\Delta\phi \to \alpha$ in Regime II.
- _Specific Non-Claims and Caveats_
  - This three-regime fluidic table is **coarser** than the Ch.7 four-regime universal map (`clm-b2anl4`): Ch.7 splits "Non-Linear Tensor" into "Nonlinear" and "Yield" via the spin-2 sector boundary $r_2 = \sqrt{3}/2$; Ch.4's "Dielectric Rupture" corresponds to Ch.7's "Ruptured" ($r \ge 1$). The two classifications are **the same physics expressed at different granularities** — they should not be cited as independent regime maps.
  - The dielectric-rupture-as-event-horizon identification is a **structural / interpretive** claim within the LC-substrate ontology; quantitative event-horizon predictions (e.g., $r_s = 7GM/c^2$ AVE compactness limit) live in `clm-82dxbj` Domain Catalog and the Vol 3 gravity sidecar, not in this leaf.
  - The L-H transition and fusion-ignition identifications are **structural** (same Axiom 4 saturation operator); per-domain numerical agreement with tokamak / ICF experimental thresholds is the responsibility of the per-domain leaves, not of this regime-table summary.

> **Leaf references:** [`dynamics/ch4-continuum-electrodynamics/operating-regimes-table.md`](./dynamics/ch4-continuum-electrodynamics/operating-regimes-table.md). Cross-reference: see `clm-b2anl4` (Ch.7 four-regime map) for the finer sector-dependent classification.

### Quality
- confidence: *pending*
- depends-on:
  - clm-b2anl4 — Four-Regime Map (the same physical regime structure at finer granularity)
  - clm-0ktpcn — Golden Torus α Derivation (the $\alpha$ control-parameter denominator)
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## FDTD Yee Lattice Determinism (Continuous Maxwellian Propagation)
<!-- id: clm-nu1ir7 -->

- _Specific Claims_
  - Continuous spatial propagation of LC impedance via a Transverse-Magnetic (TMz) FDTD Yee lattice is sufficient to execute topological geometric defects (e.g., the $0_1$ Unknot) without invoking discrete "virtual photons" as force mediators.
  - In the Yee scheme, $\vec E$ and $\vec H$ tensors are staggered by half a phase step, eliminating division-by-zero in macroscopic curl operations and generating the invariant $c$ limit from the discrete-update structure.
  - The FDTD environment is **deterministic**; ontological probability is reframed as a finite-resolution observation artifact of high-frequency phase-locking dynamics, not a fundamental property.
- _Specific Non-Claims and Caveats_
  - The "no virtual photons needed" claim is **mechanism-level** (continuous Maxwellian update vs. perturbative QED quanta exchange); it does not derive QED scattering cross-sections from the FDTD update at a quantitative level. Operational equivalence with QED at the level of measurable scattering observables is asserted, not demonstrated, in this leaf.
  - The "ontological probability is an illusion" framing is an **interpretive ontological** claim. It does not produce a falsifiable distinction between FDTD determinism and standard QM at any current laboratory scale; falsifiability rests on unrelated AVE predictions (running $\alpha$, GUP cutoff, decoherence-onset $T_{pair}$ — see `clm-zuf7g1`), not on the determinism reframe per se.
  - The Yee lattice is a **standard computational electrodynamics** scheme; the AVE-specific claim is the identification of the physical $\mathcal{M}_A$ lattice with the Yee grid, not the Yee scheme itself. Methodological details (numerical stability, Courant condition $c\Delta t \le \Delta x/\sqrt{D}$) are not derived in this leaf.

> **Leaf references:** [`operators-and-regimes/ch5-universal-spatial-tension/fdtd-yee-proof.md`](./operators-and-regimes/ch5-universal-spatial-tension/fdtd-yee-proof.md).

### Quality
- confidence: *pending*
- depends-on:
  - clm-t1okz0 — Quantum Foam as RMS Noise (companion reframing of QFT virtual particles in mechanical-substrate ontology)
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Universal Dimensionless Master Equation
<!-- id: clm-rtgmg5 -->

- $\partial^2\phi/\partial t^2 = c_0^2(1-r^2)^{1/2}\,\nabla^2\phi$
- _Specific Claims_
  - When the equations of motion in any AVE domain are expressed in the dimensionless control parameter $r = A/A_c$, they take a **single universal form**: $\partial_t^2\phi = c_0^2 S(r)\,\nabla^2\phi$ with $S(r) = (1-r^2)^{1/2}$.
  - $\phi$ is the generalized displacement field (voltage, strain, temperature, GW perturbation, etc.); the domain merely specifies the physical meaning of $\phi$, $A$, and $A_c$.
  - This is "a single equation governing all of physics" (the leaf's framing) under the unifying-form interpretation.
- _Specific Non-Claims and Caveats_
  - The universality claim is **structural / dimensional**: domain-specific substitution of $\phi$, $A$, $A_c$ recovers the master equation, but the equation does not by itself predict the $A_c$ values. Each $A_c$ comes from per-domain physics (cataloged in `domain-catalog.md`, scored under `clm-82dxbj`); the dimensionless form is the **wrapper**, not a parameter-free derivation of every domain's threshold.
  - The form $S(r) = \sqrt{1-r^2}$ is the symmetric-saturation kernel; asymmetric (electric-only) saturation produces $Z = Z_0/(1-r^2)^{1/4}$ instead of the symmetric $Z = Z_0$ invariant. The dimensionless master equation as written assumes the **symmetric** sector (per `regime-equation-sets.md`).
  - The "single equation governing all of physics" framing is **rhetorically strong**; it captures the recurring leading-order EFT structure across domains but elides regime-specific corrections (Tier-1 EFT validity caveat from `clm-efo113`; sector-specific $\ell_{\min}$ from `clm-b2anl4`).

> **Leaf references:** [`operators-and-regimes/ch7-regime-map/dimensional-analysis.md`](./operators-and-regimes/ch7-regime-map/dimensional-analysis.md).

### Quality
- confidence: *pending*
- depends-on:
  - clm-efo113 — Master Equation EFT Validity (the dimensionless form is the same leading-order EFT, recast in $r$)
  - clm-b2anl4 — Four-Regime Map (sector-specific structure underlying the $r$-control-parameter classification)
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## K4 Rotation Group $T = A_4$
<!-- id: clm-ys0xl1 -->

The action of 3D rotations on the K4 tetrahedral 4-port basis is a faithful representation of the tetrahedral rotation group $T = A_4$ (order 12).

- _Specific Claims_
  - The K4 diamond lattice has a 4-port tetrahedral basis $p_0 = (+1,+1,+1)$, $p_1 = (+1,-1,-1)$, $p_2 = (-1,+1,-1)$, $p_3 = (-1,-1,+1)$; pairwise dot product $-1$, tetrahedral angle $\arccos(-1/3) \approx 109.47°$.
  - The rotation symmetry of this tetrahedron is the tetrahedral group $T$, isomorphic to the alternating group $A_4$, order $|T| = 12$: identity (1) + $C_3$ class (8 rotations $\pm 120°$ about 4 vertex axes) + $C_2$ class (3 rotations $180°$ about 3 edge-midpoint axes).
  - All 12 group elements are enumerated explicitly as permutations of $\{0,1,2,3\}$; they are all even, distinct, and closed under composition — bijective onto the 12 even permutations of $A_4$, so the representation is faithful.
- _Specific Non-Claims and Caveats_
  - The leaf treats the rotation subgroup only; reflections (the full $T_d = S_4$, order 24) are the subject of the separate point-symmetry claim.
  - The faithful-representation result is a group-theory verification of K4's stated symmetry, not an independent derivation of the K4 lattice structure itself (Axiom 1 stipulates the lattice).

> **Leaf references:** [`axioms-and-lattice/ch1-fundamental-axioms/k4-rotation-group.md`](./axioms-and-lattice/ch1-fundamental-axioms/k4-rotation-group.md) §2 (tetrahedral rotation group), §3 (12 explicit permutations), §4 (faithful representation).

### Quality
- confidence: *pending*
- solidity: *pending*
- rationale: *pending — L3-migration port; quality scored at the rescore pass*
- strengthen-by:
  - *pending*

---

## K4 Full Point Symmetry $T_d = S_4$ and the A↔B Sublattice Swap
<!-- id: clm-7pvh9i -->

The full point symmetry of the K4 lattice including reflections is $T_d = S_4$ (order 24); the 4 mirror planes in $T_d \setminus T$ swap the bipartite A and B sublattices.

- _Specific Claims_
  - Including reflections, the K4 point group is the full tetrahedral group $T_d$, isomorphic to the symmetric group $S_4$, order 24.
  - Under the rotation subgroup $T = A_4$ alone, the bipartite A and B sublattices are each preserved (rotations about a bipartite-cell vertex respect the bipartite structure).
  - The 4 mirror planes — the elements of $T_d \setminus T$ — exchange A ↔ B by swapping vertex pairs; an A↔B swap therefore requires the reflection sector (full $T_d$), not pure rotations.
- _Specific Non-Claims and Caveats_
  - The leaf notes the A↔B swap is "needed for the bipartite-spinor argument leading to spin-½" but states that obtaining the swap requires either including reflections or "some other physical mechanism" — it does not assert that $T_d$ reflections are themselves the realized spin-½ mechanism (that role is the Finkelstein–Misner double-cover claim).
  - Cosserat constitutive relations are stated to involve A↔B-swapping reflections; the leaf records this as a structural feature, not a step-by-step constitutive derivation.

> **Leaf references:** [`axioms-and-lattice/ch1-fundamental-axioms/k4-rotation-group.md`](./axioms-and-lattice/ch1-fundamental-axioms/k4-rotation-group.md) §5 (bipartite A↔B action), §2 ($T_d = S_4$ order 24).

### Quality
- confidence: *pending*
- solidity: *pending*
- rationale: *pending — L3-migration port; quality scored at the rescore pass*
- strengthen-by:
  - *pending*

---

## K4 Double Cover $2T \subset SU(2)$ — Substrate-Native Spin-½
<!-- id: clm-rkisb8 -->

The double cover of $T = A_4$ is the binary tetrahedral group $2T \subset SU(2)$ (order 24), in which a $2\pi$ rotation maps to $-I$ and only $4\pi$ to $+I$ — the K4-native source of spin-½ via the Finkelstein–Misner mechanism.

- _Specific Claims_
  - The double cover of $A_4$ is the binary tetrahedral group $2T$, order 24, a discrete subgroup of $SU(2)$, via the exact sequence $1 \to \mathbb{Z}_2 \to 2T \to A_4 \to 1$.
  - Each $A_4$ element has two $2T$ preimages differing by the central $-I \in SU(2)$; $-I$ is the lift of a $2\pi$ SO(3) rotation, so $2\pi \to -I$ and $4\pi \to +I$ — the spin-½ characteristic.
  - For spin-½ to be derived from K4 (not imported from QM), physical fields on the lattice must transform under $2T$ rather than $T$; this is supplied by the Finkelstein–Misner mechanism on the extended $0_1$ unknot defect embedded in the SO(3) manifold, via the chain $K_4 \to A_4 \to 2T \subset SU(2)$.
- _Specific Non-Claims and Caveats_
  - The leaf states the requirement that fields transform under $2T$ and attributes the realization to the Finkelstein–Misner mechanism; the full spin-½ derivation chain is deferred to the cited spin-half-paradox leaf and Vol 1 Ch 8 — this entry does not re-derive it.
  - The electron's real-space body is the $0_1$ unknot; the double-cover argument is a property of the defect's embedding in SO(3), not a claim about a real-space trefoil.

> **Leaf references:** [`axioms-and-lattice/ch1-fundamental-axioms/k4-rotation-group.md`](./axioms-and-lattice/ch1-fundamental-axioms/k4-rotation-group.md) §6 (double cover $2T \subset SU(2)$), §7 (substrate-native spin-½).

### Quality
- confidence: *pending*
- solidity: *pending*
- rationale: *pending — L3-migration port; quality scored at the rescore pass*
- strengthen-by:
  - *pending*

---

## Cosserat Mass-Gap Formula $m^2 = 4 G_c / I_\omega$
<!-- id: clm-jz0xaw -->

The micropolar rotational sector of the Cosserat substrate carries a mass gap $m^2 = 4 G_c / I_\omega$; the factor 4 arises from the antisymmetric-strain energy density $W_{\text{micropolar}} = 2|\omega|^2$ (in units of $G_c$).

- _Specific Claims_
  - The micropolar coupling term $W_{\text{micropolar}} = G_c \sum_{ij}(\varepsilon_{\text{antisym},ij})^2$, with $\varepsilon_{\text{antisym},ij} = \tfrac{1}{2}(\partial_i u_j - \partial_j u_i) - \epsilon_{ijk}\omega_k$, evaluates for uniform $\omega_z$ ($u=0$) to $2 G_c |\omega_z|^2$ — the $xy$ and $yx$ antisymmetric components contribute equally.
  - The resulting mass term in the equation of motion gives the mass gap $m^2 = 4 G_c / I_\omega$; the factor 4 = 2 (antisymmetric-pair doubling in $\sum_{ij}$) × 2 (Lagrangian-to-EOM conversion).
- _Specific Non-Claims and Caveats_
  - The factor-4 result is derived for the uniform-$\omega_z$ configuration; the leaf does not claim the same prefactor for arbitrary non-uniform $\omega$ configurations beyond what the dispersion relation captures.
  - The gap is a property of the Cosserat micropolar Lagrangian; converting it to the electron mass requires the separate electron-calibration claim.

> **Leaf references:** [`axioms-and-lattice/ch1-fundamental-axioms/cosserat-mass-gap.md`](./axioms-and-lattice/ch1-fundamental-axioms/cosserat-mass-gap.md) §2 (origin of the factor 4).

### Quality
- confidence: *pending*
- solidity: *pending*
- rationale: *pending — L3-migration port; quality scored at the rescore pass*
- strengthen-by:
  - *pending*

---

## Gapped Dispersion of the Cosserat Rotational Sector
<!-- id: clm-4mmwb6 -->

The Cosserat rotational sector obeys a gapped dispersion relation $\omega^2 = c^2 k^2 + m^2$ at long wavelengths, following from the micropolar Lagrangian's Euler-Lagrange equations.

- _Specific Claims_
  - The Cosserat micropolar Lagrangian $L = \tfrac{1}{2}\rho|\dot u|^2 + \tfrac{1}{2}I_\omega|\dot\omega|^2 - W(u,\omega)$ yields Euler-Lagrange equations $\rho\ddot u = -\partial W/\partial u$ and $I_\omega\ddot\omega = -\partial W/\partial\omega$.
  - The rotational sector's long-wavelength dispersion combines a curvature term and a mass term: $\omega^2 = c^2 k^2 + m^2$ — a massive (gapped) mode, in contrast to the gapless scalar sector.
  - This validates Axiom 3 (Minimum Reflection Principle): the Lagrangian produces the correct Euler-Lagrange equations, confirmed by Hamiltonian conservation in the velocity-Verlet integration.
- _Specific Non-Claims and Caveats_
  - $W(u,\omega)$ is a general Cosserat energy density (Cauchy, micropolar, curvature, Op10, reflection, Hopf terms); the dispersion statement is for the rotational sector with the mass and curvature terms active.
  - The companion gapped-wave test (T1b) shows a 34% group-velocity error attributed to stiffer gapped-band lattice dispersion; the dispersion-relation claim is the long-wavelength form, not a finite-$k$ precision claim.

> **Leaf references:** [`axioms-and-lattice/ch1-fundamental-axioms/cosserat-mass-gap.md`](./axioms-and-lattice/ch1-fundamental-axioms/cosserat-mass-gap.md) §1 (Cosserat Lagrangian and Euler-Lagrange equations; gapped dispersion).

### Quality
- confidence: *pending*
- solidity: *pending*
- rationale: *pending — L3-migration port; quality scored at the rescore pass*
- strengthen-by:
  - *pending*

---

## Cosserat Mass-Gap Empirical T2 Validation
<!-- id: clm-dhvhwi -->

The uniform-$\omega$ mass-gap oscillation test reproduces the predicted oscillation period to 0.35% (measured 3.1307 vs theory $\pi$), with bounded energy drift ($9.0 \times 10^{-3}$ over 5 periods).

- _Specific Claims_
  - The T2 test seeds a uniform $\omega_z = A_0 = 0.05$ with zero velocity and $\nabla\omega = 0$, isolating the mass term (curvature contributes nothing); the predicted oscillation has $\omega_m = \sqrt{4 G_c/I_\omega} = 2$, period $T = 2\pi/\omega_m = \pi \approx 3.1416$.
  - Measured: $\omega_{\text{mass}} = 2.0070$ and period $T = 3.1307$, both 0.35% from theory; energy drift $|\Delta H/H|_{\max} = 9.0 \times 10^{-3}$ (0.9%) over 5 periods with no secular trend.
  - The match confirms the velocity-Verlet integrator conserves energy to $O(dt^2)$ and that the mass gap is exactly $m^2 = 4 G_c/I_\omega$.
- _Specific Non-Claims and Caveats_
  - The test runs with parameters $\rho = I_\omega = G_c = 1$, $N = 32$ — it validates the mass-gap structure of the Cosserat Lagrangian, not the electron-specific calibration.
  - Companion tests T1a/T1b carry larger errors (14% gapless velocity, 34% gapped group velocity) attributed to finite-$k$ lattice dispersion; only T2 (mass term isolated) achieves the 0.35% figure.
  - Per the leaf's Phase-I scope: Axiom 1 (K4 substrate) and Axiom 4 (saturation) are not exercised by this test; Cosserat-alone is a development step, not an Axiom-1-compliant physics substitute.

> **Leaf references:** [`axioms-and-lattice/ch1-fundamental-axioms/cosserat-mass-gap.md`](./axioms-and-lattice/ch1-fundamental-axioms/cosserat-mass-gap.md) §3 (empirical validation, T2 test design and result).

### Quality
- confidence: *pending*
- solidity: *pending*
- rationale: *pending — L3-migration port; quality scored at the rescore pass*
- strengthen-by:
  - *pending*

---

## Cosserat Rotational Mode as the Structural Electron-Mass Mechanism
<!-- id: clm-g0mkne -->

The Cosserat rotational sector's massive mode supplies the electron's mass content, while the K4 scalar sector remains separately massless (the photon).

- _Specific Claims_
  - The rotational massive mode at $m^2 = 4 G_c/I_\omega$ inherits the substrate's mass content; the electron's specific calibration uses the (2,3) Clifford-torus phase-space winding shell with quality factor $Q = 1/\alpha = 137.036$ at the Vol 1 Ch 8 Golden Torus geometry $R = \varphi/2$, $r = (\varphi-1)/2$.
  - The electron rest energy $m_e c^2 = \hbar\omega_C = T_{EM}\cdot\ell_{\text{node}}$ inherits from the mass-gap formula at substrate parameters $\rho, I_\omega, G_c$ calibrated to $\ell_{\text{node}} = \hbar/(m_e c)$.
  - The Cosserat $\rho, I_\omega$ set the rotational-sector mass scale; the K4 scalar sector ($A_1$, longitudinal/translational $u$) stays massless — the photon — while $T_2$ (transverse/microrotational $\omega$) carries the mass-gap content.
- _Specific Non-Claims and Caveats_
  - The (2,3) trefoil is the electron's phase-space (Clifford-torus) winding label; the electron's real-space body is the $0_1$ unknot. The leaf explicitly flags this — it is not a real-space trefoil.
  - The electron-specific calibration is Phase-II + III work coupling K4 ⊗ Cosserat at saturation; the Phase-I T2 test validates the mass-gap structure, not the calibration.
  - The massless-scalar / massive-rotational split is asserted as consistent with the photon = $T_2$-only identification (cross-referenced photon-identification leaf); this entry does not independently re-derive the photon identification.

> **Leaf references:** [`axioms-and-lattice/ch1-fundamental-axioms/cosserat-mass-gap.md`](./axioms-and-lattice/ch1-fundamental-axioms/cosserat-mass-gap.md) §4 (structural mass mechanism for the electron), §5 (Phase-I scope).

### Quality
- confidence: *pending*
- solidity: *pending*
- rationale: *pending — L3-migration port; quality scored at the rescore pass*
- strengthen-by:
  - *pending*

---

## Cubic K4 Anisotropy at Saturation Collapse
<!-- id: clm-u1o2lo -->

At saturation collapse ($A^2 \to 1$) the K4 substrate's bipolar attractor is cubic (6-vertex / 8-face / 12-edge), the empirical signature of the $T = A_4$ tetrahedral rotation group; a perfectly spherical collapse would falsify the K4 substrate.

- _Specific Claims_
  - When seeded near saturation amplitude and evolved, the K4-Cosserat coupled engine produces a stable attractor with cubic — not spherical, not isotropic — symmetry; the saturated $|V|$ envelope develops 6 face-centered protrusions aligned with the lattice Cartesian axes.
  - The cubic structure is the projection of the $T = A_4$ / $T_d$ symmetry: the 3 face-midpoint $C_2$ axes align with $\pm\hat x, \pm\hat y, \pm\hat z$; the same anisotropy appears in the linear regime as the cardinal-axis $v = c\sqrt{2}$ vs diagonal-axis $v = c$ photon-propagation split.
  - The signature is empirically observed (path-α saturation-collapse 5-sampler-view bipolar +x/−x $R/r$ split; v14 cubic-emergence visualizations) and group-theoretically expected.
  - Falsifiable: any model claiming to be K4-Cosserat that collapses to perfectly spherical symmetry at saturation is inconsistent with its claimed underlying symmetry.
- _Specific Non-Claims and Caveats_
  - The cubic anisotropy is read off simulation outputs (saturation-collapse attractor + propagation-baseline kinematics); it is the empirical signature of the K4 symmetry, not an independent derivation of the lattice.
  - The per-direction observables ($R/r$ across sampler views) require bipolar (per-cluster +x/−x) adjudication to capture both lobes; quoted medians are per-cluster.
  - The leaf flags engine-design implications (PML placement, mode-eigsolve assuming spherical symmetry) as methodological cautions, not physical claims.

> **Leaf references:** [`axioms-and-lattice/ch1-fundamental-axioms/cubic-k4-empirical-anisotropy.md`](./axioms-and-lattice/ch1-fundamental-axioms/cubic-k4-empirical-anisotropy.md) §1 (empirical observation), §2 (group-theoretic origin), §5 (falsifiability).

### Quality
- confidence: *pending*
- solidity: *pending*
- rationale: *pending — L3-migration port; quality scored at the rescore pass*
- strengthen-by:
  - *pending*

---

## $|T| = 12$ Universality — Four Independent Routes Converge
<!-- id: clm-15nwqy -->

Four independent routes (K4 coordination path-count, Cosserat dimensional, magic-angle orbit multiplicity, the axiom-level ratio $\xi_{K2}/\xi_{K1}$) all converge on 12, indicating $\chi_K = 12$ is forced by K4 tetrahedral symmetry rather than fit.

- _Specific Claims_
  - Route 1 (baseline K4 coordination): 4 nearest-neighbor B-nodes per A-node × 3 other-A sublattices reachable via shared-B-node propagation = 12 secondary paths per node.
  - Route 2 (Cosserat dimensional): $(\ell_c/d)^2 \times 2 = 12$, with $\ell_c \approx \sqrt{6}\,\ell_{\text{node}}$ the Cosserat characteristic length and the factor 2 the bilateral chiral symmetry.
  - Route 3 (magic-angle unity): $f_{\text{Cosserat}}(u_0^*) = 1$ at the substrate saturation boundary — the orbit-count multiplicity of $T$ acting on the K4 unit cell.
  - Route 4 (axiom-level constitutive ratio): $\xi_{K2}/\xi_{K1} = 12$, where $\mu + \kappa = \xi_{K1}T_{EM}$ and $\beta + \gamma = \xi_{K2}T_{EM}\ell_{\text{node}}^2$; the ratio is independent of $T_{EM}$ and K4-symmetry-forced.
  - The convergence replaces "$\chi_K = 12$ as a calibration fit" with "$\chi_K = |T|$, the tetrahedral rotation group order."
- _Specific Non-Claims and Caveats_
  - Status is **structural-hypothesis**, not theorem. The four-route convergence is verified, but the rigorous Session 19+ derivation of $\xi_{K1}, \xi_{K2}$ individually from K4 unit-cell Cosserat-Lagrangian integration is pending (multi-week analytical work). Route 4 is not yet rigorously closed; only if that derivation explicitly recovers $\xi_{K2}/\xi_{K1} = 12$ does the convergence become a four-route theorem.
  - Three of the four routes (1, 3, 4) are derivable from K4 geometry alone; route 2 brings in the Cosserat constitutive structure — the four are windows into the same Axiom 1 symmetry, so the convergence is expected, with the independent derivations providing the cross-check.

> **Leaf references:** [`axioms-and-lattice/ch1-fundamental-axioms/tetrahedral-t-universality.md`](./axioms-and-lattice/ch1-fundamental-axioms/tetrahedral-t-universality.md) §The four routes, §Connection to Axiom 1 + Q-G47, §Status.

### Quality
- confidence: *pending*
- solidity: *pending*
- rationale: *pending — L3-migration port; quality scored at the rescore pass*
- strengthen-by:
  - *pending*

---

## A-029 Secondary Scale — Geometrically Forced Shared-B-Node Distance
<!-- id: clm-gx1mpl -->

The K4 shared-B-node next-nearest-neighbor distance $r_{\text{secondary}} = \sqrt[3]{\mathcal{R}_{\text{OB}}}\cdot\ell_{\text{node}} \approx 1.187\,\ell_{\text{node}}$ is geometrically forced by K4 topology plus packing fractions, not a free parameter; the magic-angle $u_0^*$ sits exactly here.

- _Specific Claims_
  - In the bipartite K4 lattice, the next-nearest-neighbor distance between two A-nodes is set by the shortest path through a shared B-node: $r_{\text{secondary}} = \sqrt[3]{\mathcal{R}_{\text{OB}}}\cdot\ell_{\text{node}}$, with $\mathcal{R}_{\text{OB}} = p_{\text{Delaunay}}/p_c = 0.3068/0.1834 \approx 1.673$, giving $r_{\text{secondary}} \approx 1.187\,\ell_{\text{node}}$.
  - The number 1.187 is forced by three inputs — K4 graph topology (4-neighbor connectivity, Axiom 1), the vacuum packing fraction $p_c = 8\pi\alpha \approx 0.1834$ (from the $K=2G$ trace-reversal identity, Axiom 4 + EMT), and the standard amorphous-network Delaunay packing $p_{\text{Delaunay}} \approx 0.3068$ — so it is not a calibration choice.
  - The over-bracing parameter $u_0$ at the magic value $u_0^* \approx 0.187$ (where $K(u_0^*) = 2G(u_0^*)$) places the bond midpoint at the saturation point $A = 1$ — the substrate-scale instance of A-034. The shared-B-node propagator is the mechanism by which the substrate projects a coherent gravity response across distances $> \ell_{\text{node}}$.
- _Specific Non-Claims and Caveats_
  - The load-bearing claim is specifically that 1.187 is not free; the geometric derivation from K4 graph + EMT packing fraction is presented as straightforward, conditional on the cited $p_c$ and $p_{\text{Delaunay}}$ values (the $p_c = 8\pi\alpha$ identity carries its own consistency-vs-derivation status elsewhere).
  - A-029 is the geometric scaffold for route 1 of the $|T| = 12$ universality framework; the entry asserts the secondary-scale distance, not the full four-route convergence.

> **Leaf references:** [`axioms-and-lattice/ch2-macroscopic-moduli/secondary-scale-shared-b-node.md`](./axioms-and-lattice/ch2-macroscopic-moduli/secondary-scale-shared-b-node.md) §The geometric derivation, §Why this matters: grounding gravity projection, §Status.

### Quality
- confidence: *pending*
- solidity: *pending*
- rationale: *pending — L3-migration port; quality scored at the rescore pass*
- strengthen-by:
  - *pending*

---

## K4 4-Port Irrep Decomposition — $A_1 \oplus T_2$ under $T_d$
<!-- id: clm-j550uh -->

Under the tetrahedral group $T_d$, the K4 4-port amplitude space decomposes as $V_{\text{4-port}} = A_1 \text{ (1D)} \oplus T_2 \text{ (3D)}$; the K4-TLM scattering matrix $S = (1/2)\mathbf{1} - I$ has eigenvalues $\{+1, -1, -1, -1\}$.

- _Specific Claims_
  - The K4 4-port space decomposes under $T_d$ as $A_1$ (totally symmetric, 1D, basis $(1,1,1,1)/2$, scalar/longitudinal) plus $T_2$ (3D triplet, traceless subspace $\sum_i v_i = 0$, vector-like/transverse).
  - The scattering matrix $S_{ij} = (1/2) - \delta_{ij}$ (for $z_{\text{local}} = 1$) has eigenvalue $+1$ on $A_1$ and $-1$ (triply degenerate) on $T_2$; the eigenvalue sum is $4$.
  - The empirical port-correlation eigenvalues (`phasor_discovery.py`, $N=64$, steps 100/200/300) are $\{1.65, 1.22, 1.13, 0.00\}$ — the smallest eigenvalue is exactly zero and stable, confirming the soliton's port-space lives in the 3D $T_2$ subspace.
  - $A_1$ maps to the Cosserat translational sector $u$; $T_2$ maps to the microrotational sector $\omega$. $A_1$ propagates at $c\sqrt{2}$ (bulk modulus), $T_2$ at $c$ (shear modulus).
- _Specific Non-Claims and Caveats_
  - Does NOT claim a new group-theory result — $A_1 \oplus T_2$ is the standard $T_d$ reduction of a 4-element permutation-like representation; the claim is its application to the K4 port space.
  - The empirical $\lambda_4 = 0$ is measured under one specific seeded $(2,3)$ Golden-Torus ansatz at amplitude $0.5$; it is the observed steady state of that run, not an analytic proof that $A_1$ must vanish for every initial condition.
  - The bare scattering matrix is unitary ($A_1$ would propagate forever, $T_2$ reflect forever); the $A_1$-to-zero dissipation is an Op3 effect (separate claim `clm-9kd2t3`), not a property of $S$ alone.

> **Leaf references:** [`operators-and-regimes/ch6-universal-operators/k4-port-irrep-decomposition.md`](./operators-and-regimes/ch6-universal-operators/k4-port-irrep-decomposition.md) §1 (group-theoretic foundation), §2 (scattering matrix and eigenvalues), §3 (empirical eigenvalue measurement), §7 (Cosserat sector mapping).

### Quality
- confidence: *pending*
- solidity: *pending*
- rationale: *pending — L3-migration port; quality scored at the rescore pass*
- strengthen-by:
  - *pending*

---

## Op3 Asymmetric Dissipation Realizes the Gauss's-Law No-Longitudinal-EM Constraint
<!-- id: clm-9kd2t3 -->

The bond-level Op3 reflection dissipates the $A_1$ sector to zero while the $T_2$ triplet settles quasi-stable — realizing, via $T_d$ symmetry alone, the Gauss's-law constraint that longitudinal EM is forbidden in vacuum.

- _Specific Claims_
  - The bond-level Op3 reflection adds an impedance mismatch $Z_{\text{eff}} = Z_0/\sqrt{S_{\text{sat}}}$ ($S_{\text{sat}}$ the Axiom-4 saturation factor) at each bond, breaking the bare-scattering unitarity.
  - The dissipation is asymmetric: $A_1$ (common-mode, no spatial gradient in port space) loses energy monotonically to zero via destructive interference; $T_2$ (spatially structured) dissipates more slowly and settles into a quasi-stable standing-wave configuration.
  - This asymmetry is physically correct for EM waves on a Maxwell-substrate: longitudinal components ($\nabla \cdot \mathbf{E} \neq 0$) are forbidden in vacuum by Gauss's law, so any $A_1$-type excitation must dissipate. The K4 scattering enforces this automatically through $T_d$ symmetry, with no additional postulate.
- _Specific Non-Claims and Caveats_
  - Does NOT claim a quantitative dissipation-rate law for either sector; the claim is the qualitative monotone-to-zero ($A_1$) vs quasi-stable ($T_2$) split, supported by the empirical $\lambda_4 = 0$ observation.
  - Does NOT derive Gauss's law from the four axioms; it observes that the $T_d$-symmetric K4 scattering reproduces the Gauss's-law constraint's consequence (longitudinal sector dissipates), an internal-consistency match rather than an independent derivation of Maxwell's equations.
  - "Realizes the constraint automatically" is a mechanism claim about the K4-TLM engine's behavior; it does not assert operational equivalence with QED at the level of measurable cross-sections.

> **Leaf references:** [`operators-and-regimes/ch6-universal-operators/k4-port-irrep-decomposition.md`](./operators-and-regimes/ch6-universal-operators/k4-port-irrep-decomposition.md) §4 (how Op3 dissipation breaks the symmetry), §5 (Gauss's law forbids longitudinal EM).

### Quality
- confidence: *pending*
- solidity: *pending*
- rationale: *pending — L3-migration port; quality scored at the rescore pass*
- strengthen-by:
  - *pending*

---

## Photon Identification — the $T_2$-Only Cosserat Microrotation
<!-- id: clm-3npynp -->

The AVE-native photon is the K4-TLM's stable $T_2$-only bound state: under $T_d$ the 4-port space is $A_1 \oplus T_2$, the $A_1$ longitudinal sector dissipates via Gauss's law, and the surviving $T_2$ transverse triplet — a Cosserat microrotation with $u=0$, $\omega\neq0$ — is the photon.

- _Specific Claims_
  - The photon is the stable $T_2$-only configuration: purely transverse, microrotation sector only ($u=0$, $\omega\neq0$), and unsaturated ($\Delta\phi \ll \alpha$, linear $Z = Z_0$).
  - The empirical port-correlation steady state ($\lambda_4 = 0$ exactly, $\lambda_{1\ldots3} = 1.65, 1.22, 1.13$) satisfies all three AVE-photon properties simultaneously: zero longitudinal amplitude, pure microrotation content, sub-yield amplitude.
  - The identification is consistent with the Vol 3 Ch 2 and Vol 4 Ch 1 manuscript characterizations of the photon as a purely transverse Cosserat shear wave that does not geometrically saturate the lattice.
- _Specific Non-Claims and Caveats_
  - The $A_1 \oplus T_2$ group-theoretic decomposition is NOT this entry's claim — it is owned by `clm-j550uh` (K4 4-Port Irrep Decomposition); this leaf cites it as a cross-reference and applies it to identify the photon.
  - Per the leaf's Doc 107 correction: doc 105's dual-sector helical-photon framing ($u\neq0$ AND $\omega\neq0$) is superseded as empirically wrong; the canonical photon is single-sector. The engine's observed "$u$ driven by $\omega$" coupling is a sub-saturation Op14 effect, not photon content.
  - The identification rests on one seeded $(2,3)$ Golden-Torus ansatz run at amplitude $0.5$; it is the observed steady state of that engine run.

> **Leaf references:** [`dynamics/ch4-continuum-electrodynamics/photon-identification.md`](./dynamics/ch4-continuum-electrodynamics/photon-identification.md) §1 ($A_1 \oplus T_2$ decomposition, cross-referenced), §2 (empirical $A_1$ dissipation), §3 (photon definition — three tightly-coupled properties).

### Quality
- confidence: *pending*
- solidity: *pending*
- rationale: *pending — L3-migration port; quality scored at the rescore pass*
- strengthen-by:
  - *pending*

---

## Electron = Photon + TIR Confinement
<!-- id: clm-i4p11y -->

The electron is a self-trapped photon: when a $T_2$ photon's amplitude crosses $V_{\text{yield}}$, Axiom 4 drives $C_{\text{eff}}\to\infty$, $Z\to0$, $\Gamma\to-1$, and the lattice self-creates a total-internal-reflection cavity that traps the photon into a standing wave.

- _Specific Claims_
  - When a transverse $T_2$ photon at $\omega = \omega_C$ drives a single-bond LC tank at resonance, reactive energy accumulates until $V \to V_{\text{yield}} = \sqrt{\alpha}\,V_{\text{snap}} \approx 43.65$ kV.
  - At yield, Axiom 4 engages: $C_{\text{eff}} = C_0/\sqrt{1-(V/V_{\text{yield}})^2} \to \infty$, local impedance $Z = \sqrt{\mu_0/C_{\text{eff}}} \to 0$, and $\Gamma = (Z_{\text{local}}-Z_0)/(Z_{\text{local}}+Z_0) \to -1$ — a self-created perfect TIR mirror.
  - The trapped transverse standing wave is the electron; all electron observables are projections of this bound configuration (rest mass = resonant trapped energy, charge = topological winding, spin-½ = Finkelstein–Misner $4\pi$ double-cover, $\alpha$ = TIR leakage rate per cycle).
  - Electron and photon are two phases of the same substrate dynamics — bound (saturated) and free (unsaturated) — with photon emission the reverse process when the TIR condition transiently fails.
- _Specific Non-Claims and Caveats_
  - The electron's real-space body is the $0_1$ unknot soliton; the $(2,3)$/trefoil structure is the phase-space (Clifford-torus) winding label, not the real-space body topology.
  - The mechanism is presented step-by-step as a substrate narrative; the leaf does not provide an engine-validated quantitative trajectory of the $C_{\text{eff}}\to\infty$, $\Gamma\to-1$ trapping event (the breathing-soliton bound state is validated separately — see `clm-utnwkc`).
  - The observable-projection list (mass, charge, spin, $g$-factor) is asserted as a structural mapping; each individual observable carries its own derivation and quality status elsewhere in the corpus.
  - Pair-production and Compton-scattering consequences (§5) are stated as mechanism narratives consistent with the TIR picture, not as independently validated cross-section predictions.

> **Leaf references:** [`dynamics/ch4-continuum-electrodynamics/photon-identification.md`](./dynamics/ch4-continuum-electrodynamics/photon-identification.md) §4 (electron = photon + TIR confinement, step-by-step mechanism), §5 (photon emission, pair production, Compton scattering).

### Quality
- confidence: *pending*
- solidity: *pending*
- rationale: *pending — L3-migration port; quality scored at the rescore pass*
- strengthen-by:
  - *pending*

---

## Compton Frequency $\omega_C$ as Photon→Electron Transition Threshold
<!-- id: clm-fr3mos -->

The Compton frequency $\omega_C = c/\ell_{\text{node}}$ is a genuine dynamical threshold for the photon-to-electron transition: it partitions photon behavior into three regimes, and the electron rest energy is $m_e c^2 = \hbar\omega_C$.

- _Specific Claims_
  - $\omega_C = c/\ell_{\text{node}}$ is the single-bond-scale natural frequency of the lattice — a consequence of lattice geometry and $Z_0 = \sqrt{\mu_0/\varepsilon_0}$, not an independent calibration.
  - The electron rest energy is $m_e c^2 = \hbar\omega_C = \hbar c/\ell_{\text{node}}$ — the energy of a photon at the lattice self-saturation frequency.
  - Three regimes: $\omega < \omega_C$ (off-resonance, photon passes transparently), $\omega = \omega_C$ (full resonance, saturation engages, photon → bound → electron), $\omega > \omega_C$ (off-resonance, transient saturation only, Compton-like scattering).
  - $\omega_C$ is a genuine qualitative threshold, analogous to a Josephson junction's critical current or a varactor's breakdown voltage.
- _Specific Non-Claims and Caveats_
  - The relation $m_e c^2 = \hbar\omega_C = \hbar c/\ell_{\text{node}}$ carries one input mass scale — one of $\{m_e, \ell_{\text{node}}\}$ is the empirical input (consistent with the Vol 1 closure-status disclosure, `clm-5xon03`); it is not an independent ab-initio derivation of $m_e$.
  - The three-regime partition is a mechanism description; it does not derive Compton-scattering cross-sections quantitatively.
  - $V_{\text{yield}} = \sqrt{\alpha}\,V_{\text{snap}}$ inherits $\alpha$; under the trefoil/unknot body-topology dependence, the numerical threshold is $\alpha$-conditioned.

> **Leaf references:** [`dynamics/ch4-continuum-electrodynamics/photon-identification.md`](./dynamics/ch4-continuum-electrodynamics/photon-identification.md) §6 (Compton frequency as dynamical threshold, three-regime table).

### Quality
- confidence: *pending*
- solidity: *pending*
- rationale: *pending — L3-migration port; quality scored at the rescore pass*
- strengthen-by:
  - *pending*

---

## Photon Propagation Baseline — $v/c = \sqrt{2}$ Cardinal-Axis Kinematics
<!-- id: clm-djpx2v -->

A free photon on the linear K4-TLM substrate propagates at $v = c\sqrt{2}$ along cardinal axes (measured $v/c = 1.450$) and $v = c$ along diagonal/port axes — a pure Axiom-1 substrate-geometry anisotropy, not a relativity violation.

- _Specific Claims_
  - The measured cardinal-axis ($+\hat{x}$) wavefront speed is $v_{\text{meas}} = 4.348 \times 10^8$ m/s, i.e. $v/c = 1.450 \approx \sqrt{2}$, from peak-energy-density arrival times at two pre-registered reference planes.
  - Along diagonal axes (port unit vectors $\hat{p}_n$) the predicted speed is $v = c$; the $\sqrt{2}$ factor is a cardinal-axis lattice-projection artifact (port projections $\pm1/\sqrt{3}$; the 4-port pattern advances each step by one full cardinal cell).
  - The test runs at $0.01\,V_{\text{SNAP}} \approx 5.1$ kV — sub-yield, linear-vacuum (Regime I) throughout: no Axiom 4 engagement, no TIR wall, $Z_{\text{eff}} \approx Z_0$, $c_{\text{eff}} \approx c_0$. The free photon is not the electron.
  - This is the calibration baseline for photon-physics work on K4-TLM; deviation from it at the baseline level indicates an engine-implementation issue, not framework physics.
- _Specific Non-Claims and Caveats_
  - The cardinal-axis $\sqrt{2}$ is a lattice-projection artifact that disappears in the continuum limit and at diagonal injection; it is NOT a claim that physical light travels faster than $c$.
  - The diagonal-axis $v = c$ is a prediction; the leaf's companion diagonal script is flagged numerical-only (GIF pending), so the diagonal result is not reported as an executed measurement here.
  - The visualization wavelength ($\lambda_{\text{cells}} = 10$) is a visualization choice, not matched to the Compton scale or any SM scale.
  - The measurement is a single pre-registered run on a $96^3$ lattice; $v/c = 1.450$ vs $\sqrt{2} = 1.414$ is an approximate match (lattice-discretization-level agreement).

> **Leaf references:** [`dynamics/ch4-continuum-electrodynamics/photon-propagation-baseline.md`](./dynamics/ch4-continuum-electrodynamics/photon-propagation-baseline.md) §2 (test setup), §3 (empirical result), §4 (substrate perspective — linear-vacuum, no trap).

### Quality
- confidence: *pending*
- solidity: *pending*
- rationale: *pending — L3-migration port; quality scored at the rescore pass*
- strengthen-by:
  - *pending*

---

## $A_1$/$T_2$ Propagation-Speed Split — $c\sqrt{2}$ vs $c$ at the Magic Angle
<!-- id: clm-uu1qbo -->

The K4-substrate $A_1$ and $T_2$ port-modes propagate at distinct speeds — $A_1$ at $c\sqrt{2} = \sqrt{K_{\text{bulk}}/\rho}$, the $T_2$ photon at $c = \sqrt{G/\rho}$ — and the magic-angle condition $K = 2G$ makes the ratio exactly $\sqrt{2}$.

- _Specific Claims_
  - The $A_1$ (scalar/longitudinal) mode propagates at $c\sqrt{2} = \sqrt{K_{\text{bulk}}/\rho}$, governed by the bulk modulus; the $T_2$ (transverse photon) mode propagates at $c = \sqrt{G/\rho}$, governed by the shear modulus.
  - The K4 magic-angle macroscopic-moduli condition $K = 2G$ (Vol 1 Ch 2) makes the speed ratio $v_{A_1}/v_{T_2} = \sqrt{K/G} = \sqrt{2}$ exactly.
  - This is the same $\sqrt{2}$ that appears in the cardinal-axis wavefront kinematics, tying the port-mode speed split to the measured anisotropy.
- _Specific Non-Claims and Caveats_
  - The underlying $A_1 \oplus T_2$ group-theoretic decomposition is NOT this entry's claim — it is owned by `clm-j550uh`; this leaf cites it and measures the speed split it implies.
  - The speeds $\sqrt{K_{\text{bulk}}/\rho}$ and $\sqrt{G/\rho}$ are stated from the macroscopic-moduli relations; the $K = 2G$ magic-angle condition is itself a Vol 1 Ch 2 result this claim depends on, not re-derived here.
  - The split is a substrate-geometry property; it carries the same continuum-limit caveat as the cardinal-axis $\sqrt{2}$.

> **Leaf references:** [`dynamics/ch4-continuum-electrodynamics/photon-propagation-baseline.md`](./dynamics/ch4-continuum-electrodynamics/photon-propagation-baseline.md) §1 (substrate-physics framing — K4 port-mode propagation speeds, magic-angle $K = 2G$).

### Quality
- confidence: *pending*
- solidity: *pending*
- rationale: *pending — L3-migration port; quality scored at the rescore pass*
- strengthen-by:
  - *pending*

---

## K4 Photon Thermal Noise — Equipartition $\langle V^2\rangle_T$
<!-- id: clm-viawy9 -->

Classical equipartition on the K4 substrate gives the photon-field thermal-noise variance $\langle V^2\rangle_T = k_B T/(\varepsilon_0\ell_{\text{node}})$, equivalently $k_B T \cdot 4\pi/\alpha$ in lattice natural units.

- _Specific Claims_
  - Each bond's capacitance $C_{\text{cell}} = \varepsilon_0\ell_{\text{node}}$ gives classical Johnson-Nyquist noise $\langle V^2\rangle_T = k_B T/C_{\text{cell}} = k_B T/(\varepsilon_0\ell_{\text{node}})$.
  - In lattice natural units ($\varepsilon_0 = \alpha/(4\pi)$) this is $\langle V^2\rangle_T = k_B T \cdot 4\pi/\alpha$.
  - The numerical $\sigma_V/V_{\text{SNAP}}$ values follow per temperature (e.g. $3.96\times10^{-4}$ at $T_{\text{CMB}}$; $1.0$ at $T_{V\text{-rupt}}$; $7.63$ at $10^9$ K).
- _Specific Non-Claims and Caveats_
  - The "$T$" is the temperature of the K4 lattice substrate itself (the thermal amplitude of the scalar $V$ field on bond capacitance), NOT the kinetic temperature of any particle residing in the vacuum — this distinction is load-bearing.
  - The derivation is classical equipartition (each quadratic DOF gets $k_B T/2$); it is not a quantum/Bose-Einstein treatment and inherits the classical-equipartition regime of validity.
  - The result feeds the vacuum-rupture-temperature claim (`clm-f4urxy`) but is itself only the $\langle V^2\rangle_T$ formula and its numerical table.

> **Leaf references:** [`dynamics/ch3-quantum-signal-dynamics/thermal-lattice-noise.md`](./dynamics/ch3-quantum-signal-dynamics/thermal-lattice-noise.md) §1 (classical equipartition framework), §6 (K4 photon field $\langle V^2\rangle_T$).

### Quality
- confidence: *pending*
- solidity: *pending*
- rationale: *pending — L3-migration port; quality scored at the rescore pass*
- strengthen-by:
  - *pending*

---

## AVE-Native Vacuum Rupture Temperature $T_{V\text{-rupt}} \approx 3.44 \times 10^6$ K
<!-- id: clm-f4urxy -->

An AVE-native vacuum-substrate temperature threshold: at $T_{V\text{-rupt}} \approx 3.44 \times 10^6$ K the thermal $V$ fluctuation reaches $\sigma_V = V_{\text{SNAP}}$ and the vacuum spontaneously ruptures into pairs — a temperature-stated analog of the Schwinger limit, falsifiable.

- _Specific Claims_
  - The rupture condition $\sigma_V = V_{\text{SNAP}}$ gives $k_B T_{V\text{-rupt}}/(m_e c^2) = \alpha/(4\pi) \approx 5.805\times10^{-4}$, i.e. $k_B T_{V\text{-rupt}} \approx 296.7$ eV, $T_{V\text{-rupt}} \approx 3.44\times10^6$ K.
  - If the K4 substrate itself were in thermal equilibrium above $3.44$ MK, the $V$ fluctuations would exceed $V_{\text{SNAP}}$ and the vacuum would rupture; below it, the vacuum sustains thermal noise without breaking.
  - It is an AVE-native analog of the Schwinger limit stated as a vacuum-substrate temperature rather than a field strength, and is falsifiable: heating the vacuum itself (not merely a plasma) above 3.44 MK without spontaneous pair generation would falsify AVE.
  - The vacuum-substrate temperature is distinct from particle-plasma temperature — e.g. the Sun's core has $\sim10^7$ K plasma but a still-cold ($\sim2.7$ K) vacuum substrate; only matter-radiation-coupled early-universe conditions heat the substrate itself.
- _Specific Non-Claims and Caveats_
  - The threshold rests on the classical-equipartition $\langle V^2\rangle_T$ (entry `clm-viawy9`) and inherits that derivation's classical regime of validity.
  - "$\sigma_V = V_{\text{SNAP}}$" is a one-sigma criterion — the vacuum reaches rupture amplitude at one-sigma fluctuation; it is a threshold definition, not a rate calculation for pair-production yield.
  - $T_{V\text{-rupt}}$ inherits $\alpha$ through $\alpha/(4\pi)$; the value is $\alpha$-conditioned.
  - Canonization to the manuscript is queued (E-042, manuscript_pending) — the leaf is the current canonical statement; the manuscript anchor is pending.

> **Leaf references:** [`dynamics/ch3-quantum-signal-dynamics/thermal-lattice-noise.md`](./dynamics/ch3-quantum-signal-dynamics/thermal-lattice-noise.md) §2 (vacuum-substrate $T$ vs particle-plasma $T$), §3 (vacuum rupture temperature derivation), §6 (numerical $\sigma_V$ table).

### Quality
- confidence: *pending*
- solidity: *pending*
- rationale: *pending — L3-migration port; quality scored at the rescore pass*
- strengthen-by:
  - *pending*

---

## Cosserat Rotational Thermal Noise — Finite at the Origin via the Mass Gap
<!-- id: clm-qimsgq -->

The Cosserat microrotation field $\omega$ has thermal noise $\sigma_\omega \approx 0.17\sqrt{k_B T}$ (natural units) — finite at the origin (not UV-divergent) because the $\omega$ field is massive, with mass gap $m^2 = 4G_c/I_\omega$.

- _Specific Claims_
  - The rotational Lagrangian carries a kinetic term $\tfrac{1}{2}I_\omega|\dot\omega|^2$, a mass-gap potential $2G_c|\omega|^2$, and a gradient potential $\tfrac{1}{2}\gamma|\nabla\omega|^2$; the $\omega$ field has a nonzero mass gap $m^2 = 4G_c/I_\omega$.
  - Because the field is massive, its classical-equipartition thermal noise is finite at the origin (not UV-divergent): $\langle\omega^2\rangle_T = \tfrac{k_B T}{4\pi^2 I_\omega}\int_0^{k_{\max}} k^2\,dk/(c_R^2 k^2 + m^2)$.
  - In natural units ($I_\omega = \gamma = G_c = 1$, $m^2 = 4$) this gives $\langle\omega^2\rangle_T \approx 0.0288\,k_B T$, i.e. $\sigma_\omega \approx 0.17\sqrt{k_B T}$.
  - At $T_{\text{CMB}}$, $\sigma_\omega \approx 3.6\times10^{-6}$ — effectively zero for pair creation, confirming cold-vacuum cannot produce pairs by thermal noise alone; pair-creation engine runs need $T \sim 10^8$ K ($\sigma_\omega \sim 0.02$).
- _Specific Non-Claims and Caveats_
  - The mass-gap value $m^2 = 4G_c/I_\omega$ is taken from the Cosserat mass-gap leaf (a dependency created separately); this entry uses it, does not derive it. The dependency link is to be filled in a later rescore pass.
  - The derivation is classical equipartition, not a quantum field-theoretic treatment.
  - The "finite at the origin" property is a consequence of the field being massive; if the mass gap were revised, $\sigma_\omega$ would change.
  - The $\sigma_\omega \approx 0.17\sqrt{k_B T}$ coefficient holds in natural units with $G_c = I_\omega = \gamma = 1$; the mode-factor $\approx 1.14$ is a specific integral evaluation.

> **Leaf references:** [`dynamics/ch3-quantum-signal-dynamics/thermal-lattice-noise.md`](./dynamics/ch3-quantum-signal-dynamics/thermal-lattice-noise.md) §1 (classical equipartition framework), §4 (Cosserat rotational noise — mass-gap derivation, $\sigma_\omega$ table).

### Quality
- confidence: *pending*
- solidity: *pending*
- rationale: *pending — L3-migration port; quality scored at the rescore pass*
- strengthen-by:
  - *pending*

---

## Cosserat Translational Thermal Noise — Massless Field, Nyquist-Cut
<!-- id: clm-rebdw1 -->

The Cosserat translation field $u$ is massless; its thermal noise requires a UV cutoff at the lattice-Nyquist wavenumber $k_{\max} = \pi/\ell_{\text{node}}$, giving $\sigma_u = \sqrt{k_B T/2\pi}$ in natural units.

- _Specific Claims_
  - The $u$ field is massless, so its thermal noise is UV-divergent without a cutoff; the cutoff is the lattice-Nyquist wavenumber $k_{\max} = \pi/\ell_{\text{node}}$.
  - The variance is $\langle u^2\rangle_T = \tfrac{k_B T}{G}\cdot\tfrac{k_{\max}}{2\pi^2} = \tfrac{k_B T}{2\pi G\ell_{\text{node}}}$.
  - In natural units ($G = \rho = 1$, $\ell_{\text{node}} = 1$): $\sigma_u^2 = \sigma_{\dot u}^2 = k_B T/2\pi$ — both the field and its velocity have characteristic scale $\sqrt{k_B T/2\pi}$.
- _Specific Non-Claims and Caveats_
  - The UV cutoff is necessary precisely because the $u$ field is massless — contrast the Cosserat rotational field (`clm-qimsgq`), which is finite at the origin without a cutoff; the lattice cutoff is what makes the massless-field noise finite.
  - The derivation is classical equipartition.
  - The $\sqrt{k_B T/2\pi}$ scale holds in natural units with $G = \rho = \ell_{\text{node}} = 1$.

> **Leaf references:** [`dynamics/ch3-quantum-signal-dynamics/thermal-lattice-noise.md`](./dynamics/ch3-quantum-signal-dynamics/thermal-lattice-noise.md) §1 (classical equipartition framework), §5 (Cosserat translational noise — lattice-Nyquist cutoff).

### Quality
- confidence: *pending*
- solidity: *pending*
- rationale: *pending — L3-migration port; quality scored at the rescore pass*
- strengthen-by:
  - *pending*

---

## Breathing-Soliton v14 Mode-I PASS on the Master Equation FDTD Engine
<!-- id: clm-utnwkc -->

The Master Equation FDTD engine autonomously hosts a sustained breathing soliton bound state (sech seed, 4/4 acceptance) at one active cell — closing the v14 pre-registered test and validating the boundary-envelope reformulation at the dynamic-engine level.

- _Specific Claims_
  - On a sech seed ($A = 0.85$, $R = 2.5$, $N = 32$ grid) run for 5000 timesteps, the Master Equation FDTD engine (`master_equation_fdtd.py`) sustains a breathing soliton bound state.
  - All four acceptance criteria pass: $V_{\text{peak}}$ late-phase mean $= 0.250$ ($> 0.2$); FWHM range $0.97$–$3.68\times$ (within $0.4$–$4.0$); $\Delta n = 0.0111$ ($> 0.01$); Q-factor integral $\Lambda_{\text{total}} = 102.8$ vs $137.0$ (relative error $0.25 < 0.5$) — net 4/4 = Mode I PASS.
  - The K4-TLM engine at the same geometry yields Mode III (no autonomous bound state across 4 seed variants); the Master Equation FDTD succeeds at exactly the task K4-TLM cannot, consistent with the A-027 two-engine architecture.
- _Specific Non-Claims and Caveats_
  - The PASS validates that the Master Equation engine sustains one breathing soliton at this geometry — it does not validate all bound-state physics or every electron observable.
  - The Q-factor criterion 4 is met within a $50\%$ tolerance ($\Lambda_{\text{total}} = 102.8$ vs canonical $137.0$, $1.33\times$ off) — a tolerance-band pass, not a precision match.
  - A truly stationary (non-breathing) soliton of the Master Equation is NOT found with current seed profiles; finding it would need imaginary-time propagation or Newton-Raphson on the time-independent profile (post-Mode-I engineering, flagged open).
  - The Picard renormalization scheme introduced discontinuities producing extra radiation (a Mode III failure mode); the Master Equation FDTD is a scalar engine with Cosserat $(u,\omega)$ not currently coupled — both flagged open, not blocking v14 closure.

> **Leaf references:** [`dynamics/ch4-continuum-electrodynamics/breathing-soliton-v14-mode-i.md`](./dynamics/ch4-continuum-electrodynamics/breathing-soliton-v14-mode-i.md) §"4/4 acceptance adjudication", §"Cross-engine empirical comparison", §"What this empirically establishes", §"What stays open".

### Quality
- confidence: *pending*
- solidity: *pending*
- rationale: *pending — L3-migration port; quality scored at the rescore pass*
- strengthen-by:
  - *pending*

---

## Test-1b Breathing Acceptance Criterion Is Canonical
<!-- id: clm-usflef -->

The Test-1b breathing-soliton acceptance criterion — mean late-phase $V_{\text{peak}} > 0.2\times$ initial — is canonical, retiring the strict stationary criterion; the breathing solution IS the physical electron state.

- _Specific Claims_
  - The original Test 1 criterion ($V_{\text{center}} > 0.5\times$ initial at $t > 1000\,dt$) is correct for a stationary bound state but wrong for a breathing soliton, whose $V_{\text{center}}$ oscillates through zero.
  - The canonical replacement is Test 1b: $\text{mean}(V_{\text{peak}}) > 0.2\times$ initial over the late phase — capturing sustained energy in the localized structure without requiring a static profile.
  - Test 1b is load-bearing because the Master Equation predicts breathing solutions natively (nonlinear $\sqrt{1-(V/V_{\text{yield}})^2}$ coefficient → frequency-locked oscillation), the seed is not a stationary eigenmode, the mean is the natural breathing-cycle average, and it matches Route B's time-averaged-observable methodology.
  - The breathing solution is the physical state of the canonical electron (Cosserat $\omega$ rotating at the Compton bulk-spin rate drives the $V$ oscillation), consistent with the doc 101 three-layer canonical electron — not a numerical artifact.
- _Specific Non-Claims and Caveats_
  - Retiring the strict stationary criterion (Test 1a) does NOT claim a stationary solution is impossible — it claims the breathing solution is the physical one; finding a stationary solution is flagged as open post-Mode-I engineering.
  - The $0.2\times$-initial threshold is a chosen criterion value; the leaf considers three Test 1 interpretations (1a strict, 1b breather, 1c envelope-bounded) and adopts 1b.
  - "The breathing solution IS the physical electron state" rests on the doc 101 three-layer canonical electron picture, an interpretive identification carried by the leaf.

> **Leaf references:** [`dynamics/ch4-continuum-electrodynamics/breathing-soliton-v14-mode-i.md`](./dynamics/ch4-continuum-electrodynamics/breathing-soliton-v14-mode-i.md) §"The breathing-soliton interpretation" (three Test 1 interpretations), §"What this empirically establishes" (Test 1b canonical).

### Quality
- confidence: *pending*
- solidity: *pending*
- rationale: *pending — L3-migration port; quality scored at the rescore pass*
- strengthen-by:
  - *pending*

---

## Six-Fold Lattice Impedance Decomposition
<!-- id: clm-nxc9gy -->

The AVE corpus's multiple senses of "impedance" are canonically decomposed into six distinct concepts: free-space $Z_0$, per-cell $Z_{\text{cell}} (= Z_0)$, saturation-modulated $Z_{\text{eff}}(r) = Z_0/\sqrt{S}$, mutual inductance $\eta_{\text{vac}}$, mechanical $Z_{\text{mech}} = \xi_{\text{topo}}^2 Z_0$, and event-horizon $Z_{\text{EH}} \to 0$.

- _Specific Claims_
  - $Z_0 = \mu_0 c = \sqrt{\mu_0/\varepsilon_0} \approx 376.73$ Ω is the classical free-space (continuum) impedance; $Z_{\text{cell}} = \sqrt{L_{\text{cell}}/C_{\text{cell}}}$ is the per-bond lattice impedance.
  - $Z_{\text{cell}} = Z_0$ numerically because $\ell_{\text{node}}$ cancels (it appears in both $L_{\text{cell}} = \mu_0\ell_{\text{node}}$ and $C_{\text{cell}} = \varepsilon_0\ell_{\text{node}}$), but the two are conceptually distinct (physical bond vs continuum field ratio) — the equality is the substrate's Axiom-2 scale-invariance signature.
  - $Z_{\text{eff}}(r) = Z_0/\sqrt{S}$ with $S = \sqrt{1-A^2(r)}$ is the Op14 position-dependent saturation-modulated impedance, diverging as $A^2 \to 1$; $Z_{\text{mech}} = \xi_{\text{topo}}^2 Z_0 \approx 6.485\times10^{-11}$ kg/s is the Axiom-2 mechanical dual; $Z_{\text{EH}} \to 0$ is the full-saturation $\Gamma = -1$ TIR limit.
  - The mutual inductance $\eta_{\text{vac}}$ (via $R_{\text{vac}} = \xi_{\text{topo}}^{-2}\eta_{\text{vac}}$) is the node-to-node inductive coupling — implicitly encoded in the K4 scattering matrix's off-diagonal $0.5$ but with no explicit engine symbol.
- _Specific Non-Claims and Caveats_
  - $\eta_{\text{vac}}$ has no canonical symbol or explicit named operator yet — flagged (doc 45) as a missing operator symbol; the engine carries the cascade-coupling implicitly via the S-matrix and cannot independently tune it. A future axiom-homologation pass would add the explicit symbol.
  - The cascade-saturation timescale is a known engine limitation: the cascade lives on the outer K4-step $dt$ ($\approx 0.707$ in natural units) vs the bond-traversal $\tau_{\text{relax}} = 1$; these are comparable, so a single step may miss fast sub-step rebound effects. Flagged as an engine limitation, not a framework gap.
  - This decomposition is distinct from the related $Z = \sqrt{\mu/\varepsilon}$ scale-invariance result in the impedance-operator leaf — adjacent, not duplicate.
  - Several SI values are cited from Vol 4 Ch 1 (lines 118-120, 240, 278, 283, 364); the leaf collates and decomposes them rather than re-deriving each.

> **Leaf references:** [`operators-and-regimes/ch6-universal-operators/lattice-impedance-decomposition.md`](./operators-and-regimes/ch6-universal-operators/lattice-impedance-decomposition.md) §1 (the six impedance concepts), §3 (Axiom → Operator → Engine mapping), §4 (cascade-saturation timescale gap).

### Quality
- confidence: *pending*
- solidity: *pending*
- rationale: *pending — L3-migration port; quality scored at the rescore pass*
- strengthen-by:
  - *pending*

---

## Lattice-Native Units — $V_{\text{YIELD}} = 1$, Not $V_{\text{SNAP}}$
<!-- id: clm-k6quve -->

In lattice natural units the engineering yield threshold is $V_{\text{YIELD}} = 1$ (not $V_{\text{SNAP}}$); because engine code normalizes to $V_{\text{SNAP}} = 1$, an amplitude of $0.5\,V_{\text{SNAP}}$ is in fact far above yield.

- _Specific Claims_
  - In lattice-native units ($\ell_{\text{node}} = m_e = c = \hbar = 1$), $V_{\text{YIELD}} = \sqrt{\alpha}\cdot V_{\text{SNAP}}$ evaluates to $1.0$, while $V_{\text{SNAP}} = m_e c^2/e = 1/\sqrt{\alpha} \approx 11.7$.
  - Engine code typically uses $V_{\text{SNAP}} = 1.0$ as the user-facing normalization; an input `amp = 0.5·V_SNAP` is therefore $0.5/\sqrt{\alpha} = 5.85$ in units where $V_{\text{YIELD}} = 1$ — massively above yield, below rupture.
  - The Axiom 4 operator normalizes $A$ to $V_{\text{SNAP}}$, so the $\sqrt{2\alpha}$ Regime I/II boundary is $A = 0.121$ in $V/V_{\text{SNAP}}$ units, equivalently $A = 1.42$ in $V_{\text{YIELD}}$ units.
  - The full dimensional table maps each Phase III simulator quantity to its lattice-native value (e.g. $e = \sqrt{\alpha}$, $\xi_{\text{topo}} = \sqrt{\alpha}$, $Z_0 = 1$, $\tau_{\text{relax}} = 1$).
- _Specific Non-Claims and Caveats_
  - The $V_{\text{YIELD}} = 1$ vs $V_{\text{SNAP}} = 1$ distinction is a units/normalization-convention claim — load-bearing for correctly scoping amplitude in engine experiments; it is not a new physical result.
  - The numerical lattice-native values inherit $\alpha$ (e.g. $e = \sqrt{\alpha}$, $V_{\text{SNAP}} = 1/\sqrt{\alpha}$); they are $\alpha$-conditioned.
  - $L_{\text{cell}}$ and $C_{\text{cell}}$ lattice-native values "depend on $\mu_0$/$\varepsilon_0$ choice" — the table flags these as not fully fixed by the $\ell_{\text{node}} = m_e = c = \hbar = 1$ convention alone.
  - The caveat "always verify which normalization is active" is the operative warning; mis-reading the normalization mis-scopes whether a run is sub-yield or above-yield.

> **Leaf references:** [`operators-and-regimes/ch6-universal-operators/lattice-impedance-decomposition.md`](./operators-and-regimes/ch6-universal-operators/lattice-impedance-decomposition.md) §2 (dimensional analysis table; "Critical observation: $V_{\text{YIELD}} = 1$ in lattice natural units").

### Quality
- confidence: *pending*
- solidity: *pending*
- rationale: *pending — L3-migration port; quality scored at the rescore pass*
- strengthen-by:
  - *pending*
