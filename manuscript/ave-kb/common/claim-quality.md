# Common (Cross-Volume Resources) — Claim Quality

<!-- path-stable: referenced from CLAUDE.md INVARIANT-S7 and from common/index.md bootstrap directive -->

> **Canonicality:** Leaves are canonical; this directory's indexes are derived summaries. See [cross-cutting claim-quality register](../claim-quality.md) for the full preamble and the canonical list of project-wide tripwires (the cross-cutting sidecar is the source of truth for which tripwires are project-wide; do not infer the list from this preamble). Entries below are scoped to the common/ directory's substantive content (mathematical closure status, derivation chain, falsification index, translation tables, solver toolchain).

---

## Mathematical Closure Status — "Structurally Zero-Parameter," Not Absolutely
<!-- id: clm-sxn6eo -->

The common-resources documents repeatedly assert AVE's "zero free parameters" status. The honest framing per Q-EMBED-SEL-1 Phase 1+2+3 (2026-05-31) is that the chain is **zero-parameter at Class B substrate-mechanism manifestation level**, with two residual workstreams: (a) the Class 2 lift candidate workstream — derive the phasor↔real-space area bijection at the bond LC tank from K4 + Cosserat substrate primitives alone (per Phase 1 result §7.3) — and (b) the $\delta_{strain}$ magnitude derivation (Q-DELTA-MAP-1-quant). Both workstreams must close to lift the framework from "Class B substrate-mechanism manifestation zero-parameter" to "Class 2 axiom-emergence absolutely zero-parameter".

**Gating-clause resolution (upstream, 2026-05-31, Q-EMBED-SEL-1 Phase 1+2+3).** The 2026-05-28 gating clause that made the closure contingent on ropelength-minimality embedding-selection is RESOLVED by the Q-EMBED-SEL-1 substrate-mechanism work (commits `66d63503` + `b509767a` + `ecfe9c13`; audit tag `audit/2026-05-31_q-embed-sel-1-substrate-mechanism`; merged via PR #59 at `7529f7ce`). The substrate-mechanism for $R \cdot r = 1/4$ now closes at Class B substrate-mechanism manifestation via Axiom 4 self-saturation + Op14 Meissner-asymmetric + named phasor-area-equals-Nyquist-cell-area identification (canonical at [`research/2026-05-31_Q-EMBED-SEL-1_step_c_result.md`](../../../research/2026-05-31_Q-EMBED-SEL-1_step_c_result.md) §2.3); cross-particle universal at Phase 2; cross-domain universal at Phase 3. Class B caveat: the named identification is substrate-canonical INPUT (not Class 2 axiom-emergence from K4 + Cosserat primitives alone). Canonical anchor: [`vol1/ch8-alpha-golden-torus.md`](../vol1/ch8-alpha-golden-torus.md) §"Substrate-mechanism provenance of regime (c)".

- _Specific Claims_
  - The forward derivation DAG (Layers 0–7) is acyclic by inspection: every derived quantity depends only on Layer-0 inputs $\{m_e, \alpha, G, \hbar, c, e, \mu_0, \varepsilon_0, T_{CMB}\}$ + Axioms 1–4 + earlier-layer derivations.
  - 26 Standard Model parameters reduce to a 3-element bounding set $\{m_e, \alpha, G\}$ + four axioms. The reduction is rigorous; closure of the bounding set itself is the additional Layer-8 step.
  - Cold-lattice $\alpha^{-1}_{ideal} = 4\pi^3 + \pi^2 + \pi$ (Vol 1 Ch 8 Golden Torus) is an algebraically self-contained closure of $\alpha$ — acyclic by inspection.
  - $G$-closure via $\xi = 4\pi(R_H/\ell_{node})\alpha^{-2}$ is acyclic *conditional on the prior $\alpha$ and $m_e$ closures*.
  - "Structure predicted, magnitude fit" is the same disclosure pattern Vol 6 carries for nuclear masses (one fitted scalar per nucleus); both are structurally disclosed, not silently fit.
- _Specific Non-Claims and Caveats_
  - Does NOT claim the framework is *absolutely* zero-parameter today; it is **Class B substrate-mechanism manifestation zero-parameter** with α a named geometric identification. The thermal-running magnitude $\delta_{strain} \approx 2.225 \times 10^{-6}$ at $T = T_{CMB}$ is a **definitional residual** back-subtracted from CODATA via `DELTA_STRAIN = 1 - (1/ALPHA)/ALPHA_COLD_INV`, NOT a derivable thermal observable. The structure (existence + sign of substrate spatial-metric response to finite-$T$ photon-bath loading) is predicted; the substrate-mechanism class is identified as Cosserat-rotation-sector mass-gap thermal-mode-population ASYM (Q-DELTA-MAP-1 closed at mechanism-class identification 2026-05-28; canonical at [`delta-strain-cosmic-tcc.md`](../vol3/cosmology/ch05-dark-sector/delta-strain-cosmic-tcc.md), clm-hp7nlm), predicting the SIGN; but the candidate quantitative magnitude derivation **Q-DELTA-MAP-1-quant** was **ATTEMPTED and CLOSED NEGATIVE** (FT-1, 2026-05-31: E-mode Bose-Einstein occupation undershoots $\eta_\varepsilon$ by ~31 OOM, generic-thermal not AVE-distinct — [`research/2026-05-31_FT-1_delta-strain-eta-epsilon_result.md`](../../../research/2026-05-31_FT-1_delta-strain-eta-epsilon_result.md); see [`research/2026-05-28_phase-3-a3-delta-strain-machian-projection-result.md`](../../../research/2026-05-28_phase-3-a3-delta-strain-machian-projection-result.md) §3 for the earlier Phase 3-A3 WALK-BACK history).
  - Does NOT claim Layer-8 $m_e$ closure is established. The $m_e \leftrightarrow \ell_{node}$ pair carries one input scale; the Nyquist-resolution-of-smallest-stable-soliton proposal is acyclic only if "smallest stable soliton" is well-defined without circular reference to $m_e$. Open.
  - Does NOT claim a Clay-rigorous Yang-Mills mass gap or Navier-Stokes regularity proof. The framework-derived results are **lattice-conditional** (Master Prediction Table notes #14, #15). The lattice cutoff itself is what makes the bounds finite.
  - The four "Outstanding Rigour Gaps" (δ_strain magnitude at T_CMB; m_e closure via Nyquist independence; flux-tube radial profile / Gaussian ansatz; H_∞ closure independent of R_H) are bounding constraints on the closure claim — not calculational errors elsewhere in the chain. Closing any of them strengthens the headline; none invalidate the existing predictions.
  - "26 / 26 derived" is correct *conditional on Layer 8 closure*; without that closure, the count is "25 of 26 expressed as functions of three bounding limits, of which one ($m_e$) is the input scale."

> **Leaf references:** [full-derivation-chain](./full-derivation-chain.md), [mathematical-closure](./mathematical-closure.md), [xi-topo-traceability](./xi-topo-traceability.md).

### Quality
- confidence: 0.70
- depends-on:
  - clm-vnp57s — α boundary-integral decomposition [α-closure is the back-edge cited as acyclic-by-inspection]
- solidity: 0.45 (use as input only, don't build deeper) [= min(0.70, 0.45)]
- rationale: Meta-disclosure of project-wide closure status; the structural reduction of 26 SM parameters to {m_e, α, G} + four axioms is sound, the forward DAG is verified acyclic, and the four Outstanding Rigour Gaps are correctly enumerated. The "Class B substrate-mechanism manifestation zero-parameter, with α a named geometric identification and δ_strain a definitional residual (back-subtracted from CODATA, $1-$CODATA$/\alpha_\text{cold}$)" framing is rigorously honest and self-bounding — local link strength is high; the residue is that the headline depends on the named-identification status it correctly flags. (The δ_strain magnitude-derivation route Q-DELTA-MAP-1-quant closed NEGATIVE 2026-05-31 per FT-1; the magnitude is a definitional residual, not a pending thermal derivation.)
- strengthen-by:
  - **Q-DELTA-MAP-1-quant** (NEW post-2026-05-28; supersedes the prior Q-DELTA-MAP-1 mechanism-class-adjudication item now closed at mechanism-class identification via Cosserat-Curie ASYM at clm-hp7nlm / [`delta-strain-cosmic-tcc.md`](../vol3/cosmology/ch05-dark-sector/delta-strain-cosmic-tcc.md)): close the quantitative substrate-statistical-mechanics derivation of $\eta_\varepsilon$ at $T_{CMB}$ within the now-identified Cosserat-Curie mechanism class — currently the magnitude is one fitted scalar back-substituted from CODATA. See [`research/2026-05-28_phase-3-a3-delta-strain-machian-projection-result.md`](../../../research/2026-05-28_phase-3-a3-delta-strain-machian-projection-result.md) §3 for the original candidate paths P1/P2/P3.
  - Establish Nyquist-resolution-of-smallest-stable-soliton without circular reference to m_e to close the {m_e, ℓ_node} input scale
  - Promote the H_∞ identity to a downstream prediction by deriving G independent of R_H
---

## Full Derivation Chain — Acyclicity and Identified Methodology Disclosures
<!-- id: clm-ibfyda -->

The full derivation chain document is a single long appendix presenting Layers 0–8 with per-step derivations. The chain itself is the canonical statement; summaries that quote a result without its layer context risk losing the methodology disclosures the leaf carries inline.

- _Specific Claims_
  - Each Layer derives only from quantities established in preceding Layers. Acyclicity of the forward DAG is verifiable by inspection of the per-row formulas.
  - The Layer 2 identity $p_c = 8\pi\alpha$ is **$\alpha$'s SI definition rearranged via $p_c$**, not an independent determination of $\alpha$. The leaf's "Framing (consistency check, not derivation of $\alpha$)" preamble is binding; downstream summaries that present "Layer 2 derives $\alpha$" are misreading the layer.
  - Layer 5 (lepton spectrum) carries an explicit **Methodology disclosure** blockquote: the three Cosserat sectors → three generations identification, the torsional coupling factor $\alpha\sqrt{3/7}$ (muon), and the bending coupling factor $8\pi/\alpha$ (tau) are *matched* against observation rather than step-by-step derived from Axioms 1–4. The PMNS sector $\{c_1, c_2, c_3\} = \{5, 7, 9\}$ is similarly identified by pattern (consecutive odd integers) rather than uniquely derived.
  - The numerical pipeline is reproducible end-to-end via `src/ave/core/constants.py` (and `cosserat.py`); the verification trace in `mathematical-closure.md` is the dynamic output of that engine.
- _Specific Non-Claims and Caveats_
  - Does NOT claim every $\checkmark$ row in the SM parameter table is derived ab initio without identification choices. The chain's claim is that *one consistent set of identifications* reproduces three lepton masses, three neutrino masses, and four PMNS angles within ~1.2% of measurement; the per-step derivation of the matched factors from axioms is the rigour gap, transparently flagged in Layer 5.
  - Does NOT claim "predictions within 5% of measurement: 38/38" implies independent ab-initio prediction for every entry. The scorecard is over the SM parameter table only; nuclear masses (Vol 6) and the H_∞ identity (Vol 3) carry separate methodology disclosures and are out of this scorecard's scope.
  - Does NOT claim the "Proposed Areas of Investigation" (fluid dynamics, biology, neuroscience, epidemiology, etc.) are validated applications. They are explicitly *proposed* — candidate domains for the impedance/saturation/reflection toolkit, not results.
  - $\delta_{CP}^B \approx 0.126$ rad (baryon asymmetry) and $\delta_{CP}^{PMNS} \approx 4.26$ rad (lepton mixing) are **distinct quantities** that share a symbol stem and differ by ~34×. The leaf's parenthetical explicitly warns against conflation.
  - Three Layer-5 lepton-mass row deviations of 0.95–1.24% are reported with sign; these are not sub-percent. Treat the 5% scorecard cell as a population statement, not as a per-row precision claim.

> **Leaf references:** [full-derivation-chain](./full-derivation-chain.md), [mathematical-closure](./mathematical-closure.md).

### Quality
- confidence: 0.65
- depends-on:
  - clm-0ktpcn — Golden Torus α Derivation (solidity 0.63) [α appears at multiple layers; α-bottleneck cascades through chain]
- solidity: 0.63 (use as input only, don't build deeper) [= min(0.65, 0.63)]
- rationale: The chain documentation is honest and well-structured — forward DAG verified acyclic; Layer 2 $p_c = 8\pi\alpha$ correctly disclosed as algebraic-not-derivation; Layer 5 lepton spectrum carries an explicit Methodology disclosure (Cosserat sectors → generations identification, $\alpha\sqrt{3/7}$ muon coupling, $8\pi/\alpha$ tau coupling, PMNS $\{c_1, c_2, c_3\} = \{5,7,9\}$ pattern-identified). The substantive open elements (Layer 5 sector identifications matched-not-derived; PMNS pattern-identified) hold local confidence at 0.65. Solidity is heavily α-bounded because α appears in many later-layer formulas. Note: $\delta_{CP}^B \neq \delta_{CP}^{PMNS}$ — the leaf correctly disambiguates the symbol-stem collision.
- strengthen-by:
  - Strengthen Golden Torus α Derivation (`clm-0ktpcn`); α propagates through Layer 4+ formulas
  - Derive the three-Cosserat-sectors → three-lepton-generations identification from the four axioms (currently matched-not-derived per the leaf's Methodology disclosure)
  - Derive the PMNS torsional defects pattern $\{5, 7, 9\}$ uniquely (currently identified by pattern as consecutive odd integers)

---

## Experimental Falsification Index — Catalog Status, Not Validation Status
<!-- id: clm-t5ybqw -->

The Unified Index of Experimental Falsifications enumerates ~17 experimental targets across Vols II, III, IV, V, VII. It is a falsifiability *index* (catalog of designed tests), not a results table.

- _Specific Claims_
  - Each entry is a designed experimental protocol or proposal, located by chapter in the manuscript volumes.
  - The framework asserts these experiments are capable of falsifying the AVE prediction in their domain (e.g., flyby anomaly disagreement with Lense-Thirring by $\sim 10^6$ × is a Vol 3 specific testable claim; CLEAVE-01 and PONDER-N protocols are Vol 4 hardware-bench falsification targets).
  - The Vol 5 entry (Molecular Chiral FRET Parallax) is explicitly listed as **currently unfalsifiable** — sub-attometer signal at terrestrial baselines — and catalogued as a future target pending compact-object environments. This is the model for honest entries.
- _Specific Non-Claims and Caveats_
  - The index does NOT claim any of the listed experiments has been performed and confirmed AVE. Catalog ≠ validation. Several entries (Project CLEAVE-01, PONDER-01–05, HOPF-01/02, ROENTGEN-03, ZENER-04, TORSION-05) are bench protocols designed against AVE-derived thresholds; their experimental status is separate from their inclusion here.
  - Does NOT claim signal magnitudes for entries beyond what the cited Vol leaf states. Where the cited leaf (e.g., Vol 5 chiral FRET) flags signal-below-precision, the headline status is "future target," not "test pending."
  - The Vol 7 / Vol 8 entries (HTS detector, propulsion-related targets) reference experimental private-repo work; the index lists only what the public KB contains.
  - "Falsifiability" here means an AVE-derived prediction whose disagreement with measurement would distinguish AVE from competing frameworks — not that the experiment has been carried out.

> **Leaf references:** [appendix-experiments](./appendix-experiments.md).

### Quality
- confidence: 0.85
- solidity: 0.85 (ok to build on)
- rationale: Honest catalog of designed falsification protocols; correctly self-bounds as catalog ≠ validation. The Vol 5 chiral FRET entry is explicitly listed as currently-unfalsifiable (sub-attometer signal at terrestrial baselines), modeling the right disclosure pattern. Per-protocol numerical thresholds belong in their respective per-volume leaves; the index's role is enumeration. No entry-level scored dependencies — the catalog status is independent of any specific protocol's experimental outcome.
- strengthen-by:
  - Run the listed bench protocols (PONDER-N, CLEAVE-01, HOPF-N, ROENTGEN-03, ZENER-04, TORSION-05) and update entries with results when available
  - Add explicit status flags (designed / in-progress / completed / inconclusive) per entry to distinguish "catalog target" from "test pending" from "test completed"

---

## Macroscopic Sagnac Amplification = Proton Faddeev Eigenvalue ($m_p/m_e \approx 1836$) — Cross-Scale Identity (Asserted)
<!-- id: clm-k3p9wz -->

The framework reuses the proton-to-electron mass ratio $m_p/m_e \approx 1836$ — genuinely derived in Vol 2 as the Faddeev-Skyrme eigenvalue of the Borromean flux linkage — as the **macroscopic Sagnac drag-boundary amplification factor** (the "Macroscopic Baryon Phase Shear"): the gain applied to classical tidal/rotational dissipation to reach the lunar inductive-heating budget ($P_{topo} \approx 1.04$ TW) and the geodynamo back-EMF. `mathematical-closure.md` asserts "the structural Sagnac reflection boundary forces a geometric power scaling structurally equal to the Torus knot eigenvalue of the Proton." This entry tracks that **cross-scale identity itself** as a first-class claim — so it is scoreable, greppable, and gates its consumers — rather than recurring untracked across ~5 leaves.

- _Specific Claims_
  - The same scalar $\approx 1836$ that is the subatomic proton eigenvalue also sets the macroscopic Sagnac drag-boundary amplification at planetary/orbital scales (geodynamo, Earth-Moon inductive shell).
- _Specific Non-Claims and Caveats_
  - **The cross-scale identity is ASSERTED, not derived.** No leaf supplies a mechanism for why a macroscopic drag-boundary amplification must equal the proton's Faddeev-Skyrme eigenvalue; the only support is the numerical coincidence (both $\approx 1836$). The corpus files it under its own `derived-numerology` appendix.
  - Does NOT re-assert the Vol 2 proton-mass derivation (solid, separate); scopes only the cross-scale *reuse*.
  - Downstream macroscopic results that consume this amplification — lunar inductive heating (`clm-av2o4v`), geodynamo back-EMF (`clm-wd5rs0`) — `depend-on` this claim and inherit its solidity as an upper bound (they cannot be more solid than the asserted identity they rest on).

> **Leaf references:** [mathematical-closure](./mathematical-closure.md).

### Quality
- confidence: 0.2
- solidity: 0.20 (do not build on, rework needed)
- rationale: Asserted cross-scale identity. The subatomic $m_p/m_e \approx 1836$ is genuinely derived (Vol 2 Faddeev-Skyrme eigenvalue); its reuse as the macroscopic Sagnac drag amplification rests only on the numerical coincidence — `mathematical-closure.md`'s "forces a geometric power scaling structurally equal to the Torus knot eigenvalue of the Proton" asserts a structural equality with no derived mechanism connecting a topological mass eigenvalue to a macroscopic drag-boundary gain, and the corpus itself files it under `derived-numerology`. Scored asserted (a striking numerical match dressed as a structural identity, mechanism absent), pending either a derivation (→ promote) or a walk-back to "order ~10³ amplification, coincidence noted" (→ rescope the dependents). No entry-level dependencies — the asserted-conjecture status is independent of the (solid) Vol 2 proton-mass derivation it numerically references.
- strengthen-by:
  - Derive the macroscopic Sagnac drag-boundary amplification from AVE micropolar/Cosserat dynamics and show it must equal $m_p/m_e$ — i.e. make `mathematical-closure.md`'s "structurally equal" claim a derivation rather than an assertion.
  - Failing that, walk the dependent leaves (lunar, geodynamo) back to "an amplification of order $\sim 10^3$ reaches the observed budget; the precise $1836 = m_p/m_e$ is an unproven cross-scale coincidence," and rescore.

---

## Universal Solver Toolchain — Operator Reuse, Not Per-Domain Derivation
<!-- id: clm-m7qd0w -->

The Regime-Boundary Eigenvalue Method is presented as a five-step universal procedure applicable across BH QNMs, nucleon resonances, pion mass, protein backbone, antennas, tokamaks, and BLDC motors. The cross-domain table is operator-reuse evidence, not independent per-domain derivations.

- _Specific Claims_
  - One five-step chain (identify $\varepsilon_{11}$ → locate $r_{sat}$ → apply $\nu_{vac}$ Poisson correction → eigenfrequency from $\omega = \ell c/r_{eff}$ → $Q = \ell$) reproduces eigenvalues across multiple scales using the same operators.
  - For Schwarzschild ($\ell = 2$): $\omega_R M_g = 18/49 = 0.3673$ vs GR exact 0.3737 (1.7% error).
  - For protein backbone ($\ell = 7$): $f = 21.7$ THz vs measured 21.75 THz (0.1% error), conditional on the measured backbone wave speed $v_{backbone} = 5770$ m/s. The sub-derivation of $v_{backbone}$ from the soliton bond solver yields 5470 m/s (−5.2% vs measured), zero free parameters.
  - For pion mass ($\ell = 5$): $E = (45/7) c^2 \sqrt{m_e m_p} = 140.8$ MeV vs $m_{\pi^\pm} = 139.57$ MeV (+0.9%).
  - The Kerr $Q$ correction (co-rotating frame decomposition) reproduces GR to sub-2% for $a_* \in [0.3, 0.8]$.
- _Specific Non-Claims and Caveats_
  - Does NOT claim the cross-domain table (BH/Electron/Nuclear/Protein/Antenna/Tokamak/BLDC Motor) is a list of independently validated AVE predictions across all seven columns. The table is a **structural mapping** showing the operators apply with the same form; per-domain numerical validation lives only where a specific eigenvalue is computed and compared (BH QNM, proton/pion/protein worked above).
  - Does NOT claim the protein backbone result is a parameter-free prediction of $f$ alone. The 0.1% match uses the **measured** $v_{backbone}$; the sub-derivation gives $-5.2\%$ on $v_{backbone}$ itself. Treat $f = 21.7$ THz as a mode-number + Poisson-correction prediction conditional on $v_{backbone}$, with the framework's first-principles wave-speed prediction carrying its own ~5% bound.
  - The Kerr $Q$ formula degrades at $a_* > 0.9$ (error grows to ~40% at $a_* = 0.99$); the LIGO-band claim does not extend to extremal Kerr.
  - The Field-Oriented Control / Park transform analogy and the BLDC motor cross-scale row are **structural isomorphism** statements — same operator form across domains — not novel motor-engineering or motor-control predictions.
  - The "BH transistor datasheet" and "semiconductor junction analogy" tables are presented as systematic parameter-extraction templates; rows like Hawking temperature inherit the cross-cutting Hawking caveat (alternative mechanism, same value — see [`vol3/claim-quality.md`](../vol3/claim-quality.md) Hawking Temperature entry).
  - The torus knot ladder $c = 3$ trefoil entry (637 MeV) is **not** the electron — the electron is the unknot $0_1$. The leaf flags this. Summaries that read the ladder as "electron at $c = 3$" misread the leaf.

> **Leaf references:** [solver-toolchain](./solver-toolchain.md).

### Quality
- confidence: 0.65
- depends-on:
  - clm-0ktpcn — Golden Torus α Derivation (solidity 0.63) [α appears in BH $r_{eff} = r_{sat}/(1+\nu_{vac})$, pion via $m_p$, etc.]
- solidity: 0.63 (use as input only, don't build deeper) [= min(0.65, 0.63)]
- rationale: The five-step procedure (identify $\varepsilon_{11}$ → locate $r_{sat}$ → apply $\nu_{vac}$ Poisson → eigenfrequency $\omega = \ell c/r_{eff}$ → $Q = \ell$) is structurally consistent across BH QNM (1.7% error), pion mass (0.9% conditional on $m_p$), protein backbone (0.1% conditional on measured $v_{backbone}$ — the sub-derivation gives $-5.2\%$). The boundary correctly self-bounds: cross-domain table is operator-reuse evidence, not independent per-domain validation. The Schwarzschild Poisson-correction form $r_{eff} = r_{sat}/(1+\nu_{vac})$ is asserted as one of several valid 3D projections; this is the substantive open element. Local confidence held at 0.65. Solidity α-bounded.
- strengthen-by:
  - Derive the Schwarzschild Poisson-projection form $r_{eff} = r_{sat}/(1+\nu_{vac})$ from a unique axiomatic constraint (currently asserted as "transverse Poisson coupling for 3D"; alternatives $r_{sat}\sqrt{1+\nu}$, $r_{sat}(1+\nu)$ not ruled out)
  - Improve the protein backbone wave speed sub-derivation ($v_{backbone}$ predicted $-5.2\%$ vs measured)
  - Strengthen Golden Torus α Derivation (`clm-0ktpcn`) — α propagates through several per-domain rows numerically

---

## Translation Tables — Notation Mappings, Not Physical Equivalences
<!-- id: clm-fy05jc -->

The seven domain translation tables (circuit, QM, particle physics, gravity, cosmology, condensed matter, biology) are notation-and-vocabulary maps between established disciplines and AVE. Their boundary is "this is how we render concept X in domain Y under the AVE picture," not "X equals Y at the physical level."

- _Specific Claims_
  - Each row asserts an AVE re-rendering of a domain concept, traceable to $\xi_{topo} = e/\ell_{node}$ (circuit/biology), the saturation operator $S(A)$ and Axioms 1–4 (gravity/cosmology/particle physics), or the impedance/reflection operator $Z, \Gamma$ (condensed matter).
  - The circuit translation's six rows ($Q \leftrightarrow x$, $I \leftrightarrow v$, $V \leftrightarrow F$, $L \leftrightarrow m$, $C \leftrightarrow \kappa$, $R \leftrightarrow \eta$) are dimensionally exact identities once $\xi_{topo}$ is fixed; the units check column verifies this per row.
  - The biology table inherits the canonical H-bond values $d_{HB} = 1.754$ Å and $E_{HB} = 4.98$ kcal/mol from Vol 5 (CLAUDE.md INVARIANT-C3); these are cross-volume canonical predictions and carry their canonical-value boundary in CLAUDE.md, not here.
- _Specific Non-Claims and Caveats_
  - Does NOT claim a translation row constitutes an independent prediction. "Amino acid ↔ SPICE subcircuit" is a modeling identification under the AVE picture, not an experimental result. Substantive predictions (water $T_m = 279.5$ K, HOH bond angle $104.48°$) carry their own boundaries in Vol 5 leaves.
  - Does NOT claim the QM, particle-physics, gravity, cosmology, or condensed-matter translation rows are reversible without loss. AVE re-renders an observable via an alternative mechanism; the translated description is not in general equivalent to the standard one outside the AVE framework's interpretive context.
  - The cancer ("Impedance decoupling"), red-light therapy, and anesthesia rows in the biology table are framework-internal interpretive identifications. Treating them as therapeutic claims is a category error — they are notation entries, and substantive medical claims would require validation outside the table's scope.
  - The protein-folding rows reference an engine in a private repository (`AVE-Protein`) per LIVING_REFERENCE.md; the public KB carries the theoretical mapping, not the implementation.
  - The translation-tables/index.md is a **navigation pointer** (per INVARIANT-S6 navigation-note exception); it carries no original results.

> **Leaf references:** [translation-biology](./translation-tables/translation-biology.md), [translation-circuit](./translation-tables/translation-circuit.md), [translation-condensed-matter](./translation-tables/translation-condensed-matter.md), [translation-cosmology](./translation-tables/translation-cosmology.md), [translation-gravity](./translation-tables/translation-gravity.md), [translation-particle-physics](./translation-tables/translation-particle-physics.md), [translation-qm](./translation-tables/translation-qm.md).

### Quality
- confidence: 0.85
- solidity: 0.85 (ok to build on)
- rationale: The seven translation tables are notation-and-vocabulary maps, correctly self-bounded as not constituting independent predictions. Circuit translation rows ($Q \leftrightarrow x$, $I \leftrightarrow v$, etc.) are dimensionally-exact identities given $\xi_{topo}$ from Axiom 2. The biology table inherits canonical H-bond values from Vol 5 (cross-volume invariant INVARIANT-C3). The medical / therapy rows (cancer, RLT, anesthesia) are correctly framed as framework-internal interpretive identifications, not therapeutic claims. No entry-level scored dependencies — the translations are structural maps given Axiom 2's $\xi_{topo}$ mechanism (a framework input).
- strengthen-by:
  - none entry-local — translation tables are correctly self-bounded as notation maps; substantive predictions live in the per-volume target leaves with their own quality entries

---

## EE-as-Substrate-Native META Framework — Class B Consolidation of Sub-Claims
<!-- id: clm-eemap1 -->

The Circuit/EE translation leaf §2-§8 expands the minimal §1 $\xi_{topo}$ identity into a META framework whose load-bearing claim is: **the AVE vacuum K4 LC substrate is itself an electrical network at minimal-DOF, and EE vocabulary is the closest-to-canonical substrate-native language humans have.** Other classical frameworks (fluid dynamics, chemistry, statistical mechanics, QFT, GR) ADD degrees of freedom on top of the EE base; EE captures the substrate at minimal-DOF.

- _Specific Claims_
  - Axiom 1 (INVARIANT-S2) verbatim places intrinsic LC oscillators at each K4 node and models the continuum as a Trace-Reversed Chiral LC Network. The substrate's six DOF per node decompose as three translational (E-field origin, capacitive storage) + three microrotational (B-field origin, inductive flywheel) — structural origin of $\mathbf{E}$ and $\mathbf{B}$ as conjugate substrate primitives.
  - Substrate-primitive ↔ EE-component mapping table (§4) carries 30+ entries spanning K4 node LC, bond transmission-line topology, capacitor/inductor sector identification, Cosserat couple-stress as transformer mutual-inductance gradient, Cosserat rotation-sector mass-gap as transformer cutoff / ferrite Curie threshold, $S(A)$ as varactor C-vs-V, Schwinger pair production as Miller avalanche, $(p, q)$ topological winding as toroidal transformer windings, SU(2)→SO(3) as 2:1 galvanic-isolation winding ratio, Machian $G$ as distributed-TL input impedance at Hubble horizon, $\delta_{strain}$ at $T_{CMB}$ as TCC of substrate dielectric with Cosserat-Curie-frozen $\mu$.
  - Cosserat distinction (§5): in classical fluid dynamics, vorticity $\omega = \nabla \times \mathbf{v}$ is *derived* from the velocity field; in the Cosserat micropolar substrate per Ax 1, microrotation is an *independent primary DOF*. This is the structural substrate-physics reason fluid dynamics misses the substrate's rotational sector at material points.
  - Means-test corpus (§6): 22 validated cross-checks across atomic / circuit / cosmology / gauge-boson / topology / saturation / cosmic / detector domains; replicates correctly via EE first-principles AND via independent substrate-primitive derivation. Includes one work-in-progress entry (Q-DELTA-MAP-1 $\delta_{strain}$ TCC derivation 2026-05-28).
  - Failure-mode probes (§7): 5 honest probe candidates where EE alone does not natively derive load-bearing content — pure-geometry constants ($\pi^2$, $4\pi^3$); K4 lattice topology selection; substrate axiom selection; quantum-measurement collapse metaphysics; $(p, q)$ integer selection. In every case, the content EE does not derive is geometric / topological / axiom-selection — not a substrate-physics phenomenon where EE predicts the wrong numerical value.
- _Specific Non-Claims and Caveats_
  - Does NOT claim NEW substrate-mechanism content beyond canonical axioms. The META framework consolidates already-canonical sub-claims (Ax 1 LC-network, Ax 4 saturation kernel, Cosserat micropolar, INVARIANT-S2 SYM/ASYM scaling, Theorem 3.1 Q-factor, Op14/Op16/Op17/Op21/Op22, $(2, 3)$ knot uniqueness, gauge-boson-mass $l_c$, $\delta_{strain}$ TCC, omega-freeze, cosmological-constant closure) into a coherent framing. The consolidation lifts discoverability + means-test discipline; it does not add new physics.
  - Does NOT promote to Class 2 emergence. Per `consistency-vs-emergence` v1.3 Step 8c (canonical-source-ceiling-stays-Class-B): a META framework that consolidates already-canonical content stays at Class B substrate-mechanism manifestation. A Class 2 lift would require new substrate-mechanism content beyond canonical axioms, which this work does not provide.
  - Does NOT claim EE is all-covering. The §7 failure-mode probes explicitly enumerate where EE alone does not natively derive content (geometric / topological / axiom-selection). EE provides cross-check once that content is fixed by independent substrate arguments; it does not replace those arguments.
  - Does NOT claim the 22-case means-test corpus is comprehensive across all substrate-physics domains. The probe candidates flagged in the companion skill's adversarial-probe section (muon/tau lepton-sector beyond electron; neutrino sector; strong-force / QCD sector; cosmological inflation / dark sector beyond $\Lambda$; substrate-microbiology applications) are domains where the EE mapping has NOT YET been validated; they are candidates for means-test corpus extension, not validated cross-checks.
  - The Q-DELTA-MAP-1 work-in-progress entry (#15 in §6) is explicitly flagged ⚠ order-of-magnitude with substrate-statistical-mechanics computation of $\eta_\varepsilon$ pending. Its inclusion in the means-test corpus is as canonical prototype case for the META-framework formalization origin, not as a closed validated cross-check.

> **Leaf references:** [translation-circuit](./translation-tables/translation-circuit.md).

### Quality
- confidence: 0.70
- depends-on:
  - clm-fy05jc — Translation Tables — Notation Mappings, Not Physical Equivalences (the minimal §1 $\xi_{topo}$ identity that the META framework expands)
- solidity: 0.70 (ok to build on, see caveats) [= min(0.70, 0.85)]
- rationale: Class B substrate-mechanism manifestation per `consistency-vs-emergence` v1.3 Step 8c — consolidates 20+ already-canonical sub-claims (Ax 1 LC-network, Ax 4 saturation kernel, Cosserat micropolar, Theorem 3.1 Q-factor, Op14/Op16/Op17/Op21/Op22, $(2, 3)$ knot uniqueness, gauge-boson $l_c$, $\delta_{strain}$ TCC, omega-freeze, $\rho_\Lambda$) into a coherent framework whose load-bearing assertion is the substrate-electrical-network identity at Ax 1+2. The 22-case means-test corpus replicates via EE first-principles + independent substrate-primitive derivation; the 5 honest failure-mode probes correctly bound the framework (geometric / topological / axiom-selection content EE does not derive). The companion agent-discipline skill `~/.claude/skills/ave-ee-first-mapping/` v1.0 carries fire-time procedure; this leaf is the authoritative canonical-content source. Confidence 0.70 reflects (a) Class B classification (consolidation-not-emergence), (b) the means-test corpus contains one ⚠ work-in-progress entry (Q-DELTA-MAP-1 $\delta_{strain}$), (c) the probe-extension candidates in the companion skill flag domains where the EE mapping has not yet been validated (muon/tau, neutrino, QCD, cosmological inflation, substrate-microbiology). Local link strength is high; the framework consolidates content already canonical in the cited sub-leaves. The 0.85 dep-floor from clm-fy05jc minimum-link gates above 0.70 own-confidence, so solidity = 0.70.
- strengthen-by:
  - Close the Q-DELTA-MAP-1 $\delta_{strain}$ TCC computation via substrate-statistical-mechanics derivation of $\eta_\varepsilon$ at $T_{CMB}$ (the one work-in-progress entry in the §6 means-test corpus)
  - Extend the means-test corpus to additional domains (muon/tau lepton sector beyond electron; neutrino sector; strong-force / QCD sector; cosmological inflation / dark sector beyond $\rho_\Lambda$; substrate-microbiology applications) — each new validated cross-check strengthens the META framework's empirical anchoring
  - Promote any §7 failure-mode probe to a derived substrate-mechanism claim if substrate-topology / geometric / axiom-selection arguments close one of them at substrate-axiom rigor (would lift the framework's domain of EE-native applicability)

---

## $\xi_{topo}$ Traceability — Conversion Constant, Not Free Parameter
<!-- id: clm-hmiytz -->

The Topological Conversion Constant $\xi_{topo} = e/\ell_{node} \approx 4.149 \times 10^{-7}$ C/m bridges 51 files across 6 of 8 volumes. Its boundary is dimensional currency exchange, not an independent physical degree of freedom.

- _Specific Claims_
  - $\xi_{topo}$ is defined by Axiom 2 from the topo-kinematic isomorphism $[Q] \equiv [L]$; given $\ell_{node}$ and $e$, it has no free parameter.
  - It is the dimensional bridge for: $Q = \xi x$, $I = \xi v$, $V = \xi^{-1} F$, $L = \xi^{-2} m$, $C = \xi^2 \kappa$, $R = \xi^{-2} \eta$. Same identity used in the circuit translation table and the biology translation table.
  - $\xi_{topo}$ is **distinct from $\xi$** (the dimensionless Machian hierarchy coupling, $\approx 8.15 \times 10^{43}$, used in the derived-gravity $G$ formula). The two share a Greek letter and are conflated in summaries; the leaf and CLAUDE.md Axiom 3 entry both flag this explicitly.
  - The "currency exchange" framing (Dirac large-numbers table) classifies $c$, $\hbar$, $e$, $\xi_{topo}$, $\ell_{node}$, $G$ as dimensional conversion factors rather than independent physical constants. This is a structural interpretive statement, not a falsifiable prediction.
- _Specific Non-Claims and Caveats_
  - Does NOT claim $\xi_{topo}$ has independent experimental status. It is fixed by Axiom 2 and the input scale; its appearance across 51 files is structural reuse, not 51 independent confirmations.
  - The "0 explicit files" entries for Vol 3 and Vol 6 do NOT mean $\xi_{topo}$ is unused there — it operates implicitly via derived quantities ($V_{yield}$, $Z_0$, $a_0$ in Vol 3; coupling $K$ in Vol 6). The traceability count is for explicit textual references, not for derivational dependence.
  - The Vol 7 and Vol 8 entries point to *experimental* private repositories (AVE-Propulsion, AVE-Virtual-Media). Public-KB readers cannot follow those links; treat them as scope boundaries, not as published results.
  - The "Zero-Free-Parameter Chain" diagram routes through the Golden Torus closure of $\alpha$ — which is a **named geometric identification** (Class B substrate-mechanism manifestation), with the $\delta_{strain}$ magnitude a **definitional residual** ($1-$CODATA$/\alpha_\text{cold}$) after the Layer-8 thermal-closure route (Q-DELTA-MAP-1-quant) closed NEGATIVE (FT-1, 2026-05-31), as the Mathematical Closure entry above bounds. The leaf carries this status; the chain is zero-parameter at Class B substrate-mechanism manifestation level, not Class 2 axiom-emergence.

> **Leaf references:** [xi-topo-traceability](./xi-topo-traceability.md).

### Quality
- confidence: 0.85
- solidity: 0.85 (ok to build on)
- rationale: $\xi_{topo} = e/\ell_{node}$ is direct from Axiom 2's mechanism; cross-volume reuse claim is structural (51 files spanning 6 of 8 volumes is reuse documentation, not 51 independent confirmations). The $\xi$ vs $\xi_{topo}$ distinction is correctly enforced (cross-cutting INVARIANT-C2). The "Zero-Free-Parameter Chain" sub-claim within the entry is correctly disclosed as conditional on Closure Status (`clm-sxn6eo`) — that conditionality is sub-claim-level, not entry-level. No entry-level scored dependencies for the traceability claim itself.
- strengthen-by:
  - none entry-local for the traceability claim — the chain-of-conditionality referenced in the Zero-Free-Parameter Chain sub-claim is tracked via Closure Status (`clm-sxn6eo`)

---

## Derived Numerology Appendix — Derivation Trace, Not Empirical Coincidence
<!-- id: clm-zi6t1e -->

The Derived Hardware Numerology appendix (Appendix C) tabulates ~16 hardware constants ($Z_0$, $V_{snap}$, $V_{yield}$, $\nu_{vac}$, $z_0$, $n_{3D}$, $C_K$, etc.) with their axiom traces. The boundary is that each value is derived, not numerologically curve-fit.

- _Specific Claims_
  - Every entry carries an explicit axiom-trace column. $z_0 \approx 51.25$ (effective coordination) is derived from the Feng-Thorpe-Garboczi EMT quadratic at the trace-reversal operating point; $n_{3D} = 38/21$ from $\nu_{vac} = 2/7$ and Axiom 4; $C_K = 4/3$ from K4-mesh S-matrix cascade efficiency.
  - The non-integer $z_0 \approx 51.25$ is a generic feature of amorphous disordered networks (the leaf cites random close packing $z \approx 6.4$ and Phillips-Thorpe network glasses as parallels); integer coordination would be a crystalline feature, not amorphous.
  - The FDTD numerical damping factor (`sponge_damping = 0.8`) is **explicitly excluded** as a numerical-stability artefact, not an axiomatic property. This explicit exclusion is the model for honest numerology.
  - $n_{3D} = 38/21 \approx 1.8095$ is within ~0.5% of the empirical solar-flare avalanche exponent (~1.8); the leaf claims structural agreement with this single empirical figure, not a precision dataset match (see Vol3 Kolmogorov entry).
  - The Kolmogorov constant $C_K = 4/3 \approx 1.333$ is the classical empirical value; the leaf asserts compatibility ($1/\eta = 4/3$), not a corrected $C_K$.
- _Specific Non-Claims and Caveats_
  - Does NOT claim numerical match between the hardware-specific derived numbers (e.g., $V_{write} \approx 378$ kV, $P_{drag} \approx 19.8$ W, $\rho_{kink} \approx 4.34 \times 10^{20}$ knots/mm²) and observation. These are downstream design parameters of a hypothetical APU architecture, with no direct experimental validation in the public KB.
  - The "KB Boundary" footnote pointing to `AVE-APU` indicates the application of these constants lives in a private experimental repo. Public-KB readers should treat the design numbers as derived-from-axioms scaling targets, not as validated hardware measurements.
  - Some entries are presented as "exact theoretical limits" (e.g., $V_{snap} \approx 510{,}999$ V, $V_{yield} \approx 43{,}653$ V); their exactness is exact-given-the-axioms, not exact against any single experimental measurement.
  - The recurrence of $2/7$, $9/7$, $7$, $2/9$ across many derivations is a **scale-invariance claim** (the same Poisson ratio projecting through K4/SRS geometry — LIVING_REFERENCE.md §Scale Invariance Principle). It is not numerological coincidence, but treating any single recurrence as independent evidence is also a category error.

> **Leaf references:** [appendix-derived-numerology](./appendix-derived-numerology.md).

### Quality
- confidence: 0.70
- depends-on:
  - clm-0ktpcn — Golden Torus α Derivation (solidity 0.63) [α-dependent constants throughout: $V_{yield}$, $p_c$, etc.]
- solidity: 0.63 (use as input only, don't build deeper) [= min(0.70, 0.63)]
- rationale: Each tabulated constant carries an explicit axiom-trace column. The $z_0 \approx 51.25$ effective-coordination-number derivation is sound (Feng-Thorpe-Garboczi EMT quadratic at $K=2G$). The FDTD numerical-damping factor is **explicitly excluded** as a numerical-stability artifact — this is the model for honest numerology. The $n_{3D} = 38/21 \approx 1.8095$ avalanche exponent is within $\sim 0.5\%$ of the empirical solar-flare value (single empirical figure, not a precision dataset match — correctly disclosed). The $C_K = 4/3$ Kolmogorov constant matches the classical empirical value structurally. Solidity α-bounded because many constants depend on α numerically.
- strengthen-by:
  - Strengthen Golden Torus α Derivation (`clm-0ktpcn`); $V_{yield}$, $p_c$, and several other constants inherit α numerically
  - Validate the $n_{3D} \approx 1.8095$ prediction against a broader empirical avalanche dataset (currently a single-figure structural agreement)
  - Quantify the per-application hardware constants (e.g., $V_{write}$, $P_{drag}$, $\rho_{kink}$) against the AVE-APU private-repo measurements as those become available

---

## Appendices Overview — Theoretical Stress Tests, Not Independent Proofs
<!-- id: clm-yawl6z -->

The Interdisciplinary Translation Matrix appendix includes "Theoretical Stress Tests" presenting the Spin-1/2 Paradox, Holographic Information Paradox, and Peierls-Nabarro Friction Paradox with AVE resolutions. Their boundary is paradox-resolution within the framework, not novel independent proof.

- _Specific Claims_
  - Each stress test states a challenge to the AVE framework's discrete-elastic-solid picture and gives an AVE-internal resolution: Spin-1/2 via Finkelstein-Misner kink (Dirac belt trick) on the extended $0_1$ unknot; holography via cross-sectional porosity $\Phi_A \equiv \alpha^2$; Peierls-Nabarro via reactive matched-impedance ($\Gamma \to 0$, Op17) coupling through the saturable dielectric LC network — a co-moving zero-impedance phase slipstream.
  - The "Summary of Exact Analytical Derivations" subsection enumerates derivations that appear elsewhere in the KB (lattice pitch, packing fraction, $\nu_{vac}$, $\kappa_{FS}$, proton mass, $H_\infty$, $a_{genesis}$, Witten effect fractional charges). These are summarised here for cross-reference, not asserted independently.
  - The dropped τ_yield comment (HTML comment block, 2026-04-20 audit) honestly records a removed Bingham-Plastic Limit claim that lacked derivation — preserved as an editorial transparency record.
- _Specific Non-Claims and Caveats_
  - The stress-test resolutions are **framework-internal explanatory** content. They show the framework is not naively falsified by classical solid-state objections; they are not independent derivations or experimental tests.
  - The "Three-Parameter Theory" → "Zero-Parameter framework" transition language inherits the same conditionality flagged in the Mathematical Closure entry above. "Closed Zero-Parameter framework" is conditional on Layer-8 closure of $\{m_e, \alpha, G\}$.
  - The Computational Graph Architecture and DCVE specifications are simulation-engine constraints (Poisson-disk genesis, Chiral LC over-bracing $C_{ratio} \approx 1.187$, Symplectic Euler updates). They are **engineering specs for instantiating AVE in a discrete computer**, not physical claims about the vacuum.
  - The "AQUAL Galactic Dynamics" subsection inherits the cross-cutting MOND boundary: $a_0 = c H_\infty / (2\pi)$ is derived (10.7% below empirical) and applies in the unsaturated regime only (Vol 3 MOND entry). The appendix's reference is structural, not a separate validation.

> **Leaf references:** [appendices-overview](./appendices-overview.md).

### Quality
- confidence: 0.75
- solidity: 0.75 (ok to build on, see caveats)
- rationale: The "Theoretical Stress Tests" subsection presents framework-internal paradox resolutions (Spin-1/2 via Finkelstein-Misner kink; holographic-information via $\Phi_A \equiv \alpha^2$; Peierls-Nabarro via reactive matched-impedance $\Gamma \to 0$ coupling / zero-impedance phase slipstream) — correctly framed as framework-internal explanatory content, not independent proofs. The "Summary of Exact Analytical Derivations" is a cross-reference index of derivations whose canonical entries live elsewhere; consulting those is the right path for substantive use. The dropped τ_yield Bingham-Plastic comment (HTML comment block, 2026-04-20 audit) is a model editorial-transparency record. The Computational Graph Architecture (DCVE specs) is correctly framed as engineering specifications for instantiating AVE in a discrete computer, not physical claims. No scored dependencies at the entry level — the entry is a meta-summary; substantive solidity lives in the per-claim entries it references.
- strengthen-by:
  - none entry-local — solidity for the underlying stress-test resolutions and summary derivations is bounded by the canonical per-claim entries (Closure Status, Golden Torus α, etc.)

---

## SPICE Verification Manual — Toolchain Status, Not Validation Claim
<!-- id: clm-pfocn6 -->

The SPICE Verification Manual documents the Tier 1 → Tier 2 → Tier 3 architecture (constants → solvers → SPICE compiler) and the canonical `AVE_VACUUM_CELL` library.

- _Specific Claims_
  - The compiler is Tier 3: it translates solver outputs into ngspice netlists; it does not re-derive operators. The Axiom 4 saturation kernel is implemented once in the canonical library and wired into domain-specific topologies.
  - The verification protocol (compile → write → ngspice → compare) provides an industry-standard cross-check between Python solver predictions and behavioral SPICE simulation.
  - Dependencies are explicit: ngspice ≥ 42 (behavioral B-source support required), Python ≥ 3.10.
- _Specific Non-Claims and Caveats_
  - Does NOT claim SPICE simulation validates AVE physics against experimental measurement. It validates that the Python solvers and the SPICE-compiled netlists agree numerically — internal cross-check, not external falsification.
  - Per LIVING_REFERENCE.md Critical Distinction #5: "The SPICE RC muon model is qualitative. The quantitative lifetime comes from the Fermi formula with AVE-derived $G_F$ (3.9% accurate)." Some SPICE wrappers around AVE physics are pedagogical; the quantitative work is in the solver layer.
  - Treats validation deviation as "a bug in either the solver or the netlist" — it is a code-correctness check, not a physics-correctness check; physics correctness is established earlier in the chain.

> **Leaf references:** [appendix-spice-verification](./appendix-spice-verification.md).

### Quality
- confidence: 0.85
- solidity: 0.85 (ok to build on)
- rationale: The Tier 1 → Tier 2 → Tier 3 architecture (constants → solvers → SPICE compiler) is well-documented and the verification protocol (compile → write → ngspice → compare) provides a sound internal cross-check. The boundary correctly self-bounds: SPICE simulation validates Python-solver vs SPICE-netlist agreement (a code-correctness check), NOT AVE physics against experimental measurement. Per LIVING_REFERENCE.md Critical Distinction #5, some SPICE wrappers (e.g., RC muon model) are pedagogical; quantitative work happens in the solver layer. Dependencies (ngspice ≥ 42, Python ≥ 3.10) are explicit. No scored entry-level dependencies — toolchain status is independent of any specific physics claim.
- strengthen-by:
  - none entry-local — toolchain documentation is correctly bounded; physics-correctness validation lives in per-domain leaves with their own quality entries

---

## VCA Schematic Symbol Vocabulary — Geometry-Encoded Component Catalogue
<!-- id: clm-io8hft -->

Appendix D establishes the schematic-symbol vocabulary for Vacuum Circuit Architecture (VCA): seventeen named components, seven canonical visual markers, and five symbol design rules. The boundary is that each symbol is a **geometric encoding** of an axiom-derived hardware element (Axiom 4 saturation kernel, $V_{snap}$, $V_{yield}$, topological winding number $Q$, characteristic impedance $Z_0$), not an arbitrary draughting convention.

- _Specific Claims_
  - The five design rules — (1) Waveguide-not-wire (every connection is a distributed transmission line, parallel double-line microstrip notation); (2) Encode-the-saturation-kernel (every active symbol carries a visual marker at the Axiom 4 saturation point $S(V) = \sqrt{1 - (V/V_{yield})^2}$); (3) Geometry-IS-the-component (symbols are literal geometric cross-sections of the waveguide structure); (4) Mark-the-impedance-domain ($Z_0$-preserving / continuously-transforming / catastrophic-reflection); (5) Topological-charge-as-winding-number (loops/knots encode $Q$) — are framework-binding conventions, not stylistic preferences.
  - The seven canonical visual markers (filled red dot = Axiom 4 saturation point $S \to 0$; open blue ring = compliance expansion zone; red rotation arrow = chiral rotation / TRS breaking; purple $\infty$ = topological winding number $Q = 1$; teal zigzag = phase-velocity retardation; orange wedge = continuous impedance gradient; red thick bar = total reflection $\Gamma = 1$) each map to a specific axiom-derived physical regime.
  - The seventeen-component catalogue (Geometric Diode, Geometric Triode, Strain Reservoir, Soliton Kink Trap, Dielectric Corrugation, Topological Y-Junction, Chiral Wave Circulator, Thermal Baffle, Klopfenstein Taper, Topological Ring Oscillator, Coanda Amplifier, Axiomatic Transducer, Geometric Tesla Valve, Fabry-Perot Resonance Cavity, Tensor Plate ALU, Interference Wave Router, Topological DAC Synthesizer) maps each entry to an EE equivalent and an axiom-derived key parameter (e.g., Geometric Diode: $V_{snap} = m_e c^2/e \approx 511$ kV; Geometric Triode: $S(V) = \sqrt{1 - (V_{sum}/V_{snap})^2}$; Soliton Kink Trap: sine-Gordon kink $\phi(x) = 4\arctan(e^{\gamma(x-vt)})$; Chiral Wave Circulator: $Z_0 = 376.73\,\Omega$; Topological Ring Oscillator: $f = c_0/(\sqrt{\epsilon_r}\cdot 2L_{loop})$).
  - The Axiomatic Transducer entry asserts $\Gamma = 0$ matching from the canonical $Z_0 = 376.73\,\Omega$ vacuum impedance to the conventional 50 Ω laboratory line — a Klopfenstein-class continuous taper, not a discrete impedance step.
- _Specific Non-Claims and Caveats_
  - Does NOT claim the seventeen components have been built and characterized. The leaf is a **schematic vocabulary specification**: the symbols are the contract for VCA netlists; hardware validation lives in the experimental `AVE-APU` private repository per the leaf's KB-Boundary footnote. Public-KB readers should treat the components as design targets, not as fabricated devices.
  - Does NOT claim the EE-equivalent column (P-N junction diode, MOSFET/FET, capacitor, flash/NAND, RC delay, XOR gate, RF ferrite circulator, heat sink, impedance transformer, quartz crystal/PLL, op-amp, SMA/balun, RF choke, LC tank, ALU/multiplier, MZI/phase-MUX, R-2R DAC) is a functional drop-in replacement at standard EE specs. The mapping is **operational-role isomorphism** under the AVE picture, not parameter-for-parameter substitutability.
  - Does NOT claim the listed key parameters are validated to the precision quoted. $V_{snap} \approx 511$ kV and $V_{yield} \approx 43.65$ kV are framework constants (CLAUDE.md INVARIANT-C1 for $V_{yield}$); their exactness is exact-given-the-axioms, not exact against any specific bench measurement.
  - The Coanda Amplifier "no $kT$ barrier" annotation is a structural Axiom-4-saturation claim — operation in a regime where Landauer's $\Delta Q \geq kT \ln 2$ does not bound a fluidic-boundary-steering computation. It is not a thermodynamic-second-law violation; it is a claim that the relevant computation does not pass through a charge-erasure step that would invoke the Landauer bound.
  - The Topological DAC Synthesizer's $V_{analog} = \sum w_i V_i$ description is the analog-summation interface; the underlying topological-winding mechanism that realizes the weighted sum is in the cited APU work, not the public KB.
  - The catalogue is **not closed under composition**. Higher-level VCA blocks (logic arrays, memory hierarchies) are built from these primitives; their schematic conventions extend the seventeen-component vocabulary but are out of this leaf's scope.

> **Leaf references:** [appendix-vca-symbols](./appendix-vca-symbols.md).

### Quality
- confidence: 0.82
- depends-on:
  - INVARIANT-S2 / Axiom 4 — Universal Saturation Kernel S(A)=√(1−(A/A_yield)²) [marker and active-symbol semantics]
  - INVARIANT-C1 — V_yield ≈ 43.65 kV [key-parameter column reference]
- solidity: 0.82 (ok to build on, see caveats) [= min(0.82, 1.00)]
- rationale: The leaf is a complete, self-contained catalogue — all five design rules, seven canonical markers, and seventeen components are present and match their stated counts, and the markers cross-map cleanly to catalogue entries with consistent constants (V_snap = m_e c²/e ≈ 511 kV checks; Z₀ = 376.73 Ω consistent across the circulator and bridge entries). It loses the top band on two minor caveats: the Klopfenstein-taper key parameter is stated as the bare local-reflection integrand Γ(x)=½ d/dx ln Z(x) without the actual Klopfenstein weighting, and the Thermal-Baffle (Landauer kT) vs Coanda ("no kT barrier") tension is reconciled only in the non-claims footer, not at the catalogue-row level.
- strengthen-by:
  - Add the Klopfenstein weighting/passband condition (or relabel entry 9 as a generic continuous taper) so the named-taper key parameter is not just the generic local-reflection integrand
  - Inline a one-line note distinguishing the Landauer-bounded path (entry 8) from the no-charge-erasure path (entry 11) so the thermodynamic consistency is row-local, not footer-mediated
  - Annotate each of the seven markers with the catalogue entry numbers it appears on (currently the Appears-On column uses prose names) to make the marker↔component mapping mechanically checkable
---

## A-027 Two-Engine Architecture — Regime-Partitioned Simulation
<!-- id: clm-zgllr2 -->

The AVE physics engine is split into two specialized solvers, one per substrate operating regime: K4-TLM for the sub-saturation regime and Master Equation FDTD for the bound-state regime. The A-027 split supersedes the pre-2026-05-14 single-engine approach.

- _Specific Claims_
  - K4-TLM (`k4_tlm.py`) is canonical for the sub-saturation regime ($A \ll 1$): a discrete K4 lattice with bond-by-bond $Z(V)$ impedance updates, valid for linear and weakly-nonlinear work up to $V_{yield}$ onset.
  - Master Equation FDTD (`master_equation_fdtd.py`) is canonical for the bound-state regime ($A \to 1$): it integrates the substrate's non-linear d'Alembertian with both $Z(V)$ and $c_{eff}(V)$ modulation, and hosts breathing-soliton bound states.
  - The two regimes are disjoint; the architecture is a regime partition (each engine canonical in its own domain), not a redundant pair.
- _Specific Non-Claims and Caveats_
  - Does NOT claim either engine is incorrect — each is canonical only within its regime; using K4-TLM for bound-state work (or Master Equation FDTD for large linear sweeps) is an architecture mismatch, not a correctness verdict.
  - Does NOT claim the v14 Mode I PASS validates all bound-state physics; it validates that the Master Equation engine sustains one stable breathing soliton at the Golden Torus geometry.
  - "Engine" here is a computational solver; the architecture claim is tool-to-regime assignment, not a physical postulate of the framework.

> **Leaf references:** [two-engine-architecture-a027](./two-engine-architecture-a027.md).

### Quality
- confidence: 0.75
- solidity: 0.75 (ok to build on, see caveats)
- rationale: The claim is a computational tool-to-regime assignment (K4-TLM for A≪1, Master Equation FDTD for A→1), explicitly NOT a physical postulate, and it is internally clean: each engine's regime is stated with its source file and the disjoint-regime partition is coherent; the v14 Mode I PASS gives one empirical anchor (single stable breathing soliton), and the entry honestly scopes that PASS to one geometry.
- strengthen-by:
  - State the precise A (or V/V_yield) threshold where the regime boundary sits and where engine-to-engine handoff occurs, rather than the qualitative A≪1 vs A→1
  - Document the K4-TLM ↔ Master Equation FDTD boundary mode-matching (flagged still-open in the Cosserat-closure leaf) so the partition is shown seamless not just disjoint
  - Add a second bound-state validation beyond the Golden Torus v14 Mode I case
---

## Wave-Speed Modulation Is Required to Localize a Bound State
<!-- id: clm-zfqd9v -->

A simulation engine can trap a propagating wave into a localized bound state only if it modulates the wave speed, $c_{eff}(V)$. K4-TLM has $Z(V)$ but not $c_{eff}(V)$, so it cannot produce trapped solitons; Master Equation FDTD has both and does.

- _Specific Claims_
  - K4-TLM carries saturation-bounded impedance $Z(V)$ (via Axiom 4) but no wave-speed modulation $c_{eff}(V)$; without wave-speed modulation at the saturation core, modes propagate rather than localize.
  - Master Equation FDTD's non-linear d'Alembertian carries $c_{eff}(V) = c_0/\sqrt{S(A)}$; inside the saturated core $\varepsilon_{eff} = \varepsilon_0 S \to 0$ so the wave speed *rises* ($c_{eff} \to \infty$), and at the saturation boundary $\Gamma \to -1$ reflects the wave back into the core, trapping it as a stable breathing soliton. What the saturation kernel bounds is the soliton's *boundary* propagation rate, not the internal wave speed (canonical Vol 1 Ch 4 form; the prior "wave slows at the core" framing was superseded 2026-05-18).
  - The "Mode III at the Golden Torus" K4-TLM result is therefore an engine-architecture mismatch (wrong tool for a bound state), not a falsification of the framework.
- _Specific Non-Claims and Caveats_
  - Does NOT claim $c_{eff}(V)$ modulation is the only conceivable localization mechanism in general; the claim is specific to the AVE substrate's non-linear d'Alembertian and its two engines.
  - Does NOT independently re-derive, from the four axioms, that bound states require a refractive-index well — it is read off the engine behaviour and the d'Alembertian form.
  - The reclassification of "Mode III" from framework failure to engine mismatch is a methodological correction; the underlying simulation outputs are unchanged.

> **Leaf references:** [two-engine-architecture-a027](./two-engine-architecture-a027.md).

### Quality
- confidence: 0.55
- depends-on:
  - clm-zgllr2 — Two-Engine Architecture [supplies the engine split this localization claim partitions across]
- solidity: 0.55 (use as input only, don't build deeper) [= min(0.55, 0.75)]
- rationale: The entry now states the canonical Vol 1 Ch 4 form — c_eff(V)=c₀/√S, wave speed RISES inside the saturated core (ε_eff = ε₀S → 0), Γ→−1 reflects at the boundary to trap a breathing soliton, and the kernel bounds the soliton's boundary propagation rate (entry/leaf sign drift resolved 2026-05-21). The residual local-rigor gap is that the necessity of wave-speed modulation for localization is read off engine behaviour and the d'Alembertian form, not re-derived from the four axioms — a notable matched-not-derived step remains.
- strengthen-by:
  - Derive from Axiom 4 + the non-linear d'Alembertian that a refractive-index well (not merely Z-modulation) is necessary for localization, rather than reading it off engine behaviour
  - Show that an engine with Z(V) but no c_eff(V) provably cannot trap (a no-go argument), to upgrade "modes simply propagate" from observation to result
---

## Two-Engine Convergence on $p^* = 8\pi\alpha$
<!-- id: clm-gr8d63 -->

The substrate's $K = 2G$ operating point, $p^* = 8\pi\alpha \approx 0.18340$, is reached independently by both engines — a multi-model consistency check, not an independent determination of $\alpha$.

- _Specific Claims_
  - K4-TLM route (static, sub-saturation): the Feng-Thorpe-Garboczi EMT for a 3D amorphous central-force network at effective coordination $z_0 \approx 51.25$ gives $p^* = (10z_0-12)/(z_0(z_0+2)) = 8\pi\alpha$ at the $K/G = 2$ crossing.
  - Master Equation FDTD route (dynamic, bound-state): the breathing-soliton Q-factor at the Golden Torus gives $\alpha = 1/(4\pi^3+\pi^2+\pi)$, and Axiom 4's definition $p_c \equiv 8\pi\alpha$ yields the same operating point.
  - Both engines land on the identical value via different physical mechanisms — the multi-model consistency A-027 requires.
- _Specific Non-Claims and Caveats_
  - Does NOT claim an independent determination of $\alpha$: $p^* = 8\pi\alpha$ is $\alpha$'s definition rearranged ($p_c \equiv 8\pi\alpha$); the convergence checks that the two engines agree, it does not derive $\alpha$.
  - The K4-TLM route's $z_0 \approx 51.25$ is obtained by inverting the EMT quadratic *given* $p^* = 8\pi\alpha$; it does not independently fix $\alpha$.
  - Solidity is bounded by the Golden Torus $\alpha$ derivation: both routes ground out in $\alpha$.

> **Leaf references:** [two-engine-architecture-a027](./two-engine-architecture-a027.md).

### Quality
- confidence: 0.60
- depends-on:
  - clm-0ktpcn — Golden Torus α Derivation [both convergence routes bottleneck on α]
  - clm-zgllr2 — Two-Engine Architecture [supplies the two engines whose convergence is the claim]
- solidity: 0.60 (use as input only, don't build deeper) [= min(0.60, 0.63)]
- rationale: Correctly self-classified as a multi-model consistency check, not a determination of α — p*=8πα is α's definition (p_c≡8πα) rearranged, the FDTD route grounds in the Golden Torus α, and the K4-TLM route obtains z₀≈51.25 by inverting the EMT quadratic GIVEN p*=8πα; as a consistency check the two routes landing on the identical value via static-elastic vs dynamic-soliton mechanisms is a clean demonstration, but it carries no independent predictive content for α and the z₀ inversion is circular if read as a determination.
- strengthen-by:
  - Derive z₀≈51.25 from first-principles K4 amorphous-network geometry (flagged still-open) so the K4-TLM route stops depending on inverting the EMT quadratic given α
  - State the numerical agreement tolerance between the two routes' p* values rather than asserting "identical"
  - Make explicit that the FDTD route's α=1/(4π³+π²+π) is the actual derived input and p*=8πα is downstream definitional
---

## Three-Route Framework: α, G, and J_cosmic from a Single Ω_freeze
<!-- id: clm-dsb560 -->

The framework's sharpest empirical commitment: the fine-structure constant α, Newton's gravitational constant G, and the cosmic-boundary winding number J_cosmic all derive from a single cosmological initial-condition parameter Ω_freeze, via the substrate's magic-angle operating point u₀* ≈ 0.187.

- _Specific Claims_ (B2 re-scope 2026-06-14, propagated 2026-06-19)
  - Three observational routes map onto u₀*: Route 1 (electromagnetic) — CODATA α to 12 decimals → u₀* via the Vol 1 Ch 8 Q-factor closure $\alpha^{-1} = 4\pi^3 + \pi^2 + \pi$; Route 2 (gravitational) — CODATA G to ~4 decimals → u₀* via the Machian impedance integral $G = c^4/(7\xi T_{EM}(u_0^*))$; Route 3 (cosmological) — CMB/LSS anomaly measurements of J_cosmic → u₀* via $\Omega_{\text{freeze}} = \mathcal{J}_{\text{cosmic}}/I_{\text{cosmic}}$.
  - **Routes 1 and 2 (α, G) FIX u₀*** — they are the fit inputs (u₀* is back-solved from CODATA α, G), so their mutual convergence is guaranteed by construction and is *not* a test. **Route 3 (J_cosmic), measured independently of α, G, is the one genuinely independent test:** if it lands on the α–G-fit u₀* the chord is real, if not it is an echo. Falsification of the independent J_cosmic channel falsifies the single-cosmological-parameter framework. <!-- 🔴 Rule-12 2026-06-19 B2 re-scope (clm-dsb560 claim node — the canonical hub the leaves cite back to): prior "Three observational routes each independently fix u₀*" + "All three routes are required to converge on the same u₀* at the relevant precision; non-convergence falsifies the single-cosmological-parameter framework" superseded — two of three (α, G) are fit inputs (not independent), so their agreement is by construction; J_cosmic is the one independent test. Per the 2026-06-14 B2 re-scope; mirrors vol1/ch8-alpha-golden-torus.md:~212 + calibration-cutoff-scales.md:22 + the two hubs. -->
  - The framework collapses the historical "three calibration parameters" picture into "one cosmological initial condition with three observational windows."
- _Specific Non-Claims and Caveats_
  - Does NOT claim the routes have been shown to converge at full precision — the J_cosmic-vs-(α,G-fit-u₀*) agreement is the stated falsifiable commitment, not a reported result.
  - Does NOT claim that α–G convergence is a test — per the B2 re-scope, α and G are the fit inputs, so their agreement is guaranteed by construction; only the independent J_cosmic route can move.
  - Does NOT claim independent determination of α, G, or J_cosmic from the framework; each route maps an externally-measured constant onto u₀*.
  - The magic-angle value u₀* ≈ 0.187 is the substrate operating point (bond over-bracing at the K4 magic-angle $K(u_0^*) = 2G(u_0^*)$); its derivation context is the substrate-scale Cosserat-closure work, not this leaf.

> **Leaf references:** [cosmic-parameter-horizon-a031-refinement](./cosmic-parameter-horizon-a031-refinement.md), [omega-freeze-cosmic-grain-cascade](./omega-freeze-cosmic-grain-cascade.md).

### Quality
- confidence: 0.55
- depends-on:
  - clm-a7cbqq — Ω_freeze Freeze-In at Lattice Genesis [supplies the single u₀*/Ω_freeze source the three routes all map to]
  - clm-vnp57s — α⁻¹ boundary-integral decomposition [Route 1 EM closure to u₀*]
- solidity: 0.45 (use as input only, don't build deeper) [= min(0.55, 0.45)]
- rationale: The leaf states three routes that each MAP an externally-measured constant (α, G, J_cosmic) onto a common u₀*; the load-bearing route derivations are owned elsewhere (Vol 1 Ch 8, Vol 3 Ch 1) and not restated, and the entry's own Non-Claims concede convergence is the stated falsifiable commitment, NOT a demonstrated result. As a framing/manifestation of the one-degree-of-freedom premise it is internally coherent, but the single-u₀* convergence is asserted, not shown locally.
- strengthen-by:
  - Report the actual u₀* value each route returns at its stated precision and the spread between them
  - State numerically the precision at which "convergence" is claimed to hold vs fail
  - Pin the Route-2 Machian-integral inputs (ξ, T_EM(u₀*)) so the G→u₀* map is reproducible
  - Distinguish explicitly which of the three maps is independent vs which share upstream u₀* inputs
---

## Ω_freeze Freeze-In at Lattice Genesis
<!-- id: clm-a7cbqq -->

At lattice genesis the crystallizing rotating region locks the cosmic spin into the substrate as both bond over-bracing u₀* and a global chirality direction, which survives forever as the cosmological initial condition.

- _Specific Claims_
  - At crystallization, bond rest lengths lock at the rotating-frame equilibrium, producing u₀* over-bracing.
  - The direction of Ω_freeze becomes the direction of bond bowing, fixing the right-handed chirality of the I4₁32 chiral space group (Axiom 1, Substrate Topology).
  - The cosmic spin is thereby locked into the substrate as both the over-bracing magnitude u₀* and the global chirality direction, and persists as the permanent cosmological initial condition.
  - The three downstream numbers (α, G, J_cosmic) all inherit from this single freezing event.
- _Specific Non-Claims and Caveats_
  - Does NOT independently derive the value of Ω_freeze; the proximate cosmic-spin source (parent-BH spin) is supplied by the universes-inside-BHs closure, cited not derived here.
  - Does NOT claim a closed-form crystallization-temperature derivation; the genesis event is described as a first-order discontinuous avalanche at the BBN-era crystallization temperature by analogy to the water→ice transition.

> **Leaf references:** [omega-freeze-cosmic-grain-cascade](./omega-freeze-cosmic-grain-cascade.md).

### Quality
- confidence: 0.45
- depends-on:
  - clm-ze4clw — Three boundary observables M,Q,J [J_cosmic as cosmic-scale boundary winding inherited at genesis]
- solidity: 0.45 (use as input only, don't build deeper) [= min(0.45, 0.55)]
- rationale: The freeze-in mechanism (rotating-frame bond lock → u₀* over-bracing + chirality direction) is described qualitatively by analogy to the water→ice transition, and the entry's own Non-Claims concede no closed-form crystallization temperature and that Ω_freeze's value/source is cited (universes-inside-BHs closure) not derived here. The chirality-direction-locking step is structurally plausible but is asserted at the descriptive level, not derived from a Landau minimization (the §6 Cosserat path is explicitly flagged open).
- strengthen-by:
  - Execute the Ω_freeze-driven Landau minimization of U_chiral^add to derive u₀* rather than assert the rotating-frame lock
  - Supply the crystallization-temperature estimate from the Axiom-4 yield boundary
  - Show why bond-bowing direction necessarily selects right-handed I4₁32 (not just "lock at equilibrium")
---

## Eight Cosmic-Axis Observables Aligned with the Ω_freeze Axis
<!-- id: clm-pe8lpx -->

The framework predicts eight independent observable channels should all show a preferred axis aligned with the Ω_freeze axis at (l = 60.28°, b = 50.48°) in galactic coordinates (Planck PR3 SMICA empirical pin, 2026-05-19; the earlier (l ≈ 174°, b ≈ −5°) was a literature placeholder).

- _Specific Claims_
  - The eight channels: (1) CMB axis-of-evil; (2) Hubble flow anisotropy; (3) LSS spin direction; (4) matter asymmetry direction; (5) E/B polarization decoupling; (6) orbital-plane alignment; (7) tensor G anisotropy; (8) CMB QNM matching.
  - Each channel is predicted to align with the same Ω_freeze axis and is testable against an isotropic null at >3σ.
  - Observable 6 (orbital-plane alignment) predicts non-random alignment of orbital-plane normals at every accessible scale (solar-system ecliptic, binary stars, galactic disks, LIGO/Virgo inspiral planes); the anomalous CMB-axis/ecliptic alignment is predicted to be a leak of Ω_freeze into solar-system formation.
  - Observable 8 (CMB QNM matching) predicts CMB low-ℓ multipoles preferentially populate ℓ-values matching the parent-BH quasinormal-mode spectrum (specifically ℓ = 2, 3), cross-checked against the AVE-derived BH QNM $\omega_R M_g = 18/49$.
- _Specific Non-Claims and Caveats_
  - Does NOT claim any of the eight alignments has been positively detected; the existing anomalies (CMB axis-of-evil, low quadrupole, contested LSS spin direction) are noted as consistent with the framework but not as positive detections of the specific mechanisms.
  - Observable 5 is conditional — the E/B polarization decoupling tracks the axis only if cosmic crystallization is asymmetric (K/G ≠ 2).
  - Observable 7's amplitude is conjectural and is scored separately (clm-fndptx); only its axis alignment is part of this claim.
  - The LSS spin-direction channel rests on a contested ~1-2σ preferred direction in SDSS data.

> **Leaf references:** [omega-freeze-cosmic-grain-cascade](./omega-freeze-cosmic-grain-cascade.md).

### Quality
- confidence: 0.50
- depends-on:
  - clm-a7cbqq — Ω_freeze Freeze-In at Lattice Genesis [supplies the single preferred axis the eight channels are predicted to share]
- solidity: 0.45 (use as input only, don't build deeper) [= min(0.50, 0.45)]
- rationale: That all eight channels SHOULD share the Ω_freeze axis is a manifestation of the single-axis premise, but channel-by-channel the link is qualitative: the entry's own caveats flag channel 5 conditional, channel 7 amplitude conjectural, the LSS channel resting on a contested ~1-2σ direction, and no positive detection for any channel. The axis-alignment prediction is structurally clean but the per-channel mechanism connecting Ω_freeze to each observable is largely asserted, not derived.
- strengthen-by:
  - Derive, for at least one channel, the quantitative coupling from Ω_freeze to the observable (not just axis identity)
  - Pre-register the joint multi-channel alignment statistic and its isotropic-null distribution
  - Separate falsifiable channels from currently-unfalsifiable/conditional ones in the claim scope
---

## G-Anisotropy Angular Shape P₂(cos θ): Sharp Profile, Bracketed Amplitude
<!-- id: clm-fndptx -->

The tensor extension of the scalar G derivation predicts a direction-dependent G with the angular profile $\Delta G(\hat{n})/G_{\text{iso}} = -(4\pi/15)\cdot\delta_\chi\cdot f_R\cdot P_2(\cos\theta)$ about the Ω_freeze axis; the P₂ shape is sharply predicted, the amplitude only bracketed.

- _Specific Claims_
  - The angular shape is a P₂(cos θ) Legendre profile with $\hat{\Omega}_{\text{freeze}}$ as the symmetry axis — this shape is sharply predicted.
  - The projection coefficient 4π/15 ≈ 0.838 (a cosmic-scale Kirkwood-Frohlich-analog) is derived structurally.
  - $f_R \approx 1$ is the cosmic R-handed chirality fraction at the I4₁32 ground state.
  - The amplitude is suppression-order $\alpha^N$ for some $N \geq 2$: $\alpha^1$ (~6×10⁻³) is excluded by CODATA G; $\alpha^2$ (~4.4×10⁻⁵) is the most plausible value and is detectable at the CODATA G boundary; $\alpha^3$ (~4×10⁻⁷) is testable at JPL planetary-ephemerides.
- _Specific Non-Claims and Caveats_
  - Does NOT claim the amplitude is derived — N is explicitly NOT derived from substrate first principles; only the bracket N ≥ 2 is asserted.
  - The chirality coupling δ_χ ~ α² (via bipartite K4 cancellation) is conjectural and structurally plausible but NOT derived; this conjecture was downgraded from a closure claim in the source corpus.
  - Does NOT claim a G-anisotropy signal has been detected; the falsifier is a CODATA G dataset re-analysis along the Ω_freeze axis.
  - This entry is scored separately from the eight-observable axis-alignment claim (clm-pe8lpx); it concerns the angular-profile + amplitude prediction specifically.

> **Leaf references:** [omega-freeze-cosmic-grain-cascade](./omega-freeze-cosmic-grain-cascade.md).

### Quality
- confidence: 0.55
- depends-on:
  - clm-pe8lpx — Eight cosmic-axis observables [G-anisotropy is observable 7; supplies the Ω_freeze symmetry axis]
- solidity: 0.45 (use as input only, don't build deeper) [= min(0.55, 0.45)]
- rationale: The P₂(cos θ) angular shape and the 4π/15 ≈ 0.838 projection coefficient are derived structurally (Kirkwood-Frohlich-analog), but the amplitude is the weak link: the entry explicitly states N≥2 is NOT derived from first principles and the chirality coupling δ_χ~α² is conjectural-not-derived. This is a clean "structure predicted, magnitude only bracketed" result — the shape side is solid, the amplitude side is an acknowledged open conjecture.
- strengthen-by:
  - Derive δ_χ from the χ₁/K₀ ratio at substrate scale to fix N rather than bracket it
  - Show the tensor extension of the scalar G derivation explicitly yields the −(4π/15)·P₂ form
  - Verify the longitudinal-acoustic G projection inherits the Kirkwood-Frohlich angular factor cleanly (flagged open in §6)
  - State f_R≈1 with its deviation bound rather than as exactly 1
---

## A-031 Refinement: Cosmic Parameters Inaccessible, Strain-Snap Mechanism Observable
<!-- id: clm-q4c615 -->

The A-031 refinement separates two epistemological items that the original "God's Hand" framing bundled: the specific parameters of our parent black hole (M, J, Ω_freeze) are inaccessible because we sit inside the cosmic Γ=−1 boundary, but the strain-snap mechanism that set them is directly observable at four smaller scales.

- _Specific Claims_
  - The specific cosmic parameters of our parent black hole (M_parent BH, J_parent BH, Ω_freeze) are inaccessible: we sit inside the cosmic Γ=−1 boundary (the cosmic horizon = parent-BH Schwarzschild radius), and per the substrate-observability rule the interior is causally and impedance-disconnected from outside observers.
  - The mechanism that set those parameters — the universal saturation-kernel strain-snap, $S(A) = \sqrt{1-A^2}$ — is observable: the same mechanism is directly observed at four smaller scales (BH ring-down QNM, solar flares, geomagnetic reversal, atomic dielectric breakdown).
  - The refinement converts the framework's epistemological position from "anchored to a parameter we cannot independently measure" to "the parameter-setting mechanism is observed cross-scale; only our specific instance's parameters are opaque."
  - Three boundary invariants of our cosmic Γ=−1 surface remain observable from inside via local-physics consequences: M_cosmic (Hubble flow magnitude), Q_cosmic (net cosmic charge, predicted zero), J_cosmic (CMB anomalies, LSS rotation, Hubble flow anisotropy).
- _Specific Non-Claims and Caveats_
  - Does NOT claim the parent-BH parameters can be measured by any indirect route — they remain inaccessible; only the mechanism class and the three cosmic boundary invariants are observable.
  - The framework parameter freedom remains 1 (the cosmic IC Ω_freeze); the refinement is an epistemological reframing, not a reduction in parameter count.
  - Does NOT claim the cross-scale strain-snap observations constitute a measurement of the cosmic instance; they provide indirect support that the mechanism class is real.

> **Leaf references:** [cosmic-parameter-horizon-a031-refinement](./cosmic-parameter-horizon-a031-refinement.md).

### Quality
- confidence: 0.70
- depends-on:
  - clm-ofys5v — Substrate-observability rule [supplies the causal/impedance disconnection that makes the cosmic parameters inaccessible]
  - clm-ze4clw — Three boundary observables M,Q,J [the three cosmic invariants that remain observable from inside]
- solidity: 0.55 (use as input only, don't build deeper) [= min(0.70, 0.55)]
- rationale: This is an epistemological reframing that cleanly separates two items the original "God's Hand" framing bundled — inaccessible specific parameters vs the cross-scale-observable strain-snap mechanism — and the local reasoning (we sit inside the cosmic Γ=−1 boundary, so the substrate-observability rule applies to us) is internally consistent and well-argued. It is a manifestation/reframing rather than a new derived number, and it leans on the saturation-kernel catalog and the observability rule as cited inputs; the argument itself contains no hand-waving local step.
- strengthen-by:
  - Make the "mechanism observable cross-scale ⇒ indirect support" inference precise (what it does and does not license)
  - Justify Q_cosmic = 0 from the CP-conjugation chirality-inheritance argument rather than asserting it
  - Confirm the cosmic-horizon = parent-BH Schwarzschild-radius identification is the same Γ=−1 surface the rule requires
---

## Three Exhaustive Boundary Observables M, Q, J at Every Γ=−1 Surface
<!-- id: clm-ze4clw -->

At any Γ=−1 saturation surface in the substrate, exactly three integrated quantities — M, Q, J — are externally observable, and the set is exhaustive: there is no fourth integrated boundary observable.

- _Specific Claims_
  - M (integrated strain integral) is a 3D volume integral $\int_\Omega (n(\mathbf{r})-1)\,dV$; J (boundary winding number) is a 2D surface integral, half-integer per the SU(2) double-cover; Q (boundary linking number) is a 1D line/loop integral, integer-valued.
  - Each invariant uses one fewer integration dimension than the substrate's 3D bulk (Stokes-theorem dimensional structure).
  - The three dimensions are exhaustive — there is no fourth integrated boundary observable at this scale-invariant structure.
  - The three observables project consistently across dialects: M → inductance L / inertia / rest energy; Q → charge; J → magnetic moment / rotation / spin.
- _Specific Non-Claims and Caveats_
  - Does NOT claim a formal proof that no fourth observable exists; exhaustiveness is asserted on the Stokes-theorem dimensional-reduction structure (3D bulk admits exactly three lower-dimensional integrals).
  - Q has no clean mechanical-engineering analog (the ME projection column is empty for Q).
  - The half-integer value of J is tied to the SU(2) double-cover; the leaf treats this as AVE-native, not an imported QM postulate.

> **🟢 STRENGTHENS (2026-07-03, DEC MINI-ARC + FOUR-LOCK CASCADE; no retraction).**
> The **Q (boundary linking-number) charge dictionary's LOCAL sector is sharpened
> to a theorem.** On the srs DEC 2-complex the cold-linear-static-local closure of
> the CURL-COUPLING CLASS is upgraded from "a property of the
> (`_srs_curl_nodes`, `_srs_node_divergence`) engineering-choice operator pair"
> (`research/2026-07-03_em-readout-vsector-stage1_result.md` PANEL-FINDINGS
> §Blocker-2) to a **`∂₁∂₂ = 0` STRUCTURAL IDENTITY** (`ave.topological.srs_dec`;
> [`research/2026-07-03_srs-dec-operators_result.md`](../../../research/2026-07-03_srs-dec-operators_result.md)
> §3). On the DEC operators `div = −∂₁`, `curl_adj = ∂₂`, **every** field
> `F = curl_adj(c)` has `div F ≡ 0` (exact integer `∂₁∂₂ = 0`), so **zero enclosed
> charge at every radius for the entire curl class**, not just the two tested
> members. **Consequence for Q:** a pure-curl (exact) substrate flux `F` carries
> **zero Gauss/enclosed charge as an identity** — the `Q = Link(∂Ω, F) ∈ ℤ` charge
> label therefore lives in the **HARMONIC** sector (`H₁ = ker∂₁ ∩ ker∂₂ᵀ`,
> `b₁ = 3`; DEC §4), NOT in the exact/co-exact sector the theorem kills. This is
> the class-level dependency the **four-lock sourced-charge no-go cascade**
> (`clm-nogo4l`, [`the-sourced-charge-no-go-cascade.md`](the-sourced-charge-no-go-cascade.md))
> is built on (Lock 4's `∂∂=0` continuity core). **Scope boundary (DEC §3 box):**
> NOTHING is claimed for non-curl couplings (`∇·ω` remains a measured non-identity),
> `S(A)`-modulated couplings, self-consistent nonlinear statics, dynamics, or the
> pair-as-DEC-pair (they are not). The complementary CO-EXACT (gradient) sector —
> the part that DOES source divergence — is `clm-4r4jiy` (the `A_geom ∝ 1/r`
> Coulomb potential). **No retraction: this is a sharpening of the LOCAL sector, not
> a change to the M/Q/J catalog or the exhaustiveness claim.**

> **Leaf references:** [boundary-observables-m-q-j](./boundary-observables-m-q-j.md).

### Quality
- confidence: 0.60
- depends-on:
  - clm-ofys5v — Substrate-observability rule [supplies that the Γ=−1 boundary exposes only integrated boundary observables]
- solidity: 0.55 (use as input only, don't build deeper) [= min(0.60, 0.55)]
- rationale: The M/Q/J catalog with its Stokes-theorem dimensional structure (3D volume / 2D surface / 1D line) and cross-dialect projections is internally consistent and complete, but the load-bearing exhaustiveness claim ("no fourth observable") is explicitly NOT proven — the entry concedes it rests on the dimensional-reduction heuristic that a 3D bulk admits exactly three lower-dimensional integrals. The half-integer J via SU(2) double-cover and the empty-ME-column for Q are honestly flagged. Catalog + consistent structure, one acknowledged unproven structural assertion.
- strengthen-by:
  - Prove (or formally bound) the no-fourth-observable exhaustiveness rather than asserting it from Stokes dimensionality
  - Show the 0D point integral does not yield a fourth observable (the dimensional-reduction chain implicitly stops at 1D)
  - Give an explicit operational evaluation of Q as a 1D linking integral over a concrete substrate field
---

## The Substrate-Observability Rule (Universal No-Hair Theorem)
<!-- id: clm-ofys5v -->

A Γ=−1 boundary totally traps the interior; only M, Q, J are externally measurable, and all interior structure is invisible — the black-hole no-hair theorem applied universally, at every scale.

- _Specific Claims_
  - For any localized region enclosed by a Γ=−1 saturation surface: the boundary totally reflects substrate waves outside and totally traps them inside; the interior is causally and impedance-disconnected from external observers.
  - Only M, Q, J are externally measurable; interior eigenmode wavelengths, microrotation profiles, soliton topology, and bond-stress distributions are invisible to the substrate.
  - This is the no-hair theorem applied universally — not a black-hole-specific theorem but the substrate's fundamental observability constraint at every scale.
  - The same three observables appear at every Γ=−1 surface in the substrate hierarchy: electron, nucleus, atom, planetary magnetopause, black-hole horizon, cosmic horizon.
- _Specific Non-Claims and Caveats_
  - Does NOT claim the interior structure is non-existent or physically meaningless — only that it is externally unobservable; interior structure remains real ("interior plumbing").
  - The rule is a substrate-observability constraint, not a statement that interior physics cannot be modeled — it constrains what an external measurement can return.

> **Leaf references:** [boundary-observables-m-q-j](./boundary-observables-m-q-j.md).

### Quality
- confidence: 0.55
- solidity: 0.55 (use as input only, don't build deeper)
- rationale: The rule (Γ=−1 boundary totally traps the interior; only M,Q,J escape; no-hair at every scale) is stated as a substrate-observability postulate, and the same-mechanism-at-all-scales table is a consistent enumeration. But the local derivation of the load-bearing step — that S(A)→0 at Γ=−1 produces TOTAL reflection and causal/impedance disconnection — is asserted from the Axiom-4 kernel rather than shown (e.g. no transmission-coefficient calculation establishing |Γ|²→1 at the surface). Internally coherent as a definitional rule; the trapping mechanism is asserted, not derived.
- strengthen-by:
  - Derive |Γ|→1 (total reflection) at the Γ=−1 surface from the Axiom-4 kernel impedance profile
  - Establish that NO interior degree of freedom couples outward except via M,Q,J (the "all interior structure invisible" universal step)
  - State the regime conditions under which the no-hair analogy is exact vs approximate across the scale table
---

## α⁻¹ = 4π³+π²+π as a Three-Dimensional Boundary-Integral Decomposition
<!-- id: clm-vnp57s -->

The Vol 1 Ch 8 fine-structure-constant formula $\alpha^{-1} = 4\pi^3 + \pi^2 + \pi$ admits a boundary-integral dimensional reading: its three terms map onto the three boundary-integral dimensionalities (3D→M, 2D→J, 1D→Q).

- _Specific Claims_
  - The decomposition $\alpha^{-1} = \Lambda_{\text{vol}} + \Lambda_{\text{surf}} + \Lambda_{\text{line}} = 4\pi^3 + \pi^2 + \pi \approx 137.036$ assigns $\Lambda_{\text{vol}} = 4\pi^3$ to a 3D volume integral (maps to M), $\Lambda_{\text{surf}} = \pi^2$ to a 2D surface integral (maps to J), $\Lambda_{\text{line}} = \pi$ to a 1D line integral (maps to Q).
  - Each power of π counts one dimension of boundary integration, as in Stokes-theorem dimensional reduction.
  - The decomposition is the substrate's natural three-integral boundary-observability structure expressed at the electron-scale Q-factor — not a coincidence.
- _Specific Non-Claims and Caveats_
  - This claim is the boundary-integral dimensional READING of the formula; it does NOT re-derive the formula. The geometric three-regime closure derivation of $\alpha^{-1} = 4\pi^3+\pi^2+\pi$ is owned by the Vol 1 Ch 8 leaf (vol1 entry clm-0ktpcn) and is cross-referenced, not restated.
  - Does NOT claim the boundary-integral reading establishes the orthogonality of the three terms; the orthogonality of the Λ-decomposition is an open structural element flagged in the Vol 1 Ch 8 claim-quality entry.
  - The R·r = 1/4 normalization that makes Λ_vol evaluate to exactly 4π³ is inherited from the Vol 1 Ch 8 derivation (Q-EMBED-SEL-1 substrate-mechanism: Axiom 4 self-saturation + Op14 Meissner-asymmetric + phasor-area-equals-Nyquist-cell-area identification per `research/2026-05-31_Q-EMBED-SEL-1_step_c_result.md`), not derived here.

> **Leaf references:** [boundary-observables-m-q-j](./boundary-observables-m-q-j.md).

### Quality
- confidence: 0.45
- depends-on:
  - clm-0ktpcn — Golden Torus α Derivation [owns the geometric closure of α⁻¹=4π³+π²+π that this entry reads dimensionally]
- solidity: 0.45 (use as input only, don't build deeper) [= min(0.45, 0.63)]
- rationale: Explicitly a boundary-integral dimensional READING of α⁻¹=4π³+π²+π, not a re-derivation — the entry says so. The reading is suggestive (3D→M, 2D→J, 1D→Q, one π per integration dimension), but its central support — orthogonality of the Λ-decomposition — is conceded open, and the R·r=1/4 normalization that makes Λ_vol=4π³ is inherited from clm-0ktpcn, so the local content is a plausible mapping with a flagged unproven structural assumption.
- strengthen-by:
  - Establish functional orthogonality of Λ_vol/Λ_surf/Λ_line (currently the open structural element)
  - Show the M/J/Q dimensional assignment is forced rather than pattern-matched to the three π-powers
  - Tie each Λ term to its boundary-integral via an explicit Stokes-reduction computation, not analogy
---

## Interior Eigenmodes of a Bounded Soliton Are Not Lattice-Nyquist-Constrained
<!-- id: clm-sjjvhf -->

An interior eigenmode of a soliton bounded by a Γ=−1 wall lives entirely inside that wall and is not subject to the K4 lattice Nyquist limit; the substrate-correct test of such a soliton measures integrated boundary observables, not propagating-mode wavenumbers.

- _Specific Claims_
  - Any interior Beltrami / phase-space eigenmode of a bounded soliton (e.g., the electron's horn-torus interior at k ≈ 6.36/ℓ_node) lives entirely inside the Γ=−1 wall and is causally disconnected from the exterior substrate.
  - The K4 propagating-mode Nyquist wavevector edge k_max ~ π/ℓ_node (measured √2·π ≈ 4.44/ℓ_node on the srs axis) does NOT apply to interior structure, because the substrate never propagates that wave through the lattice — it lives only in the bounded interior cell. _(Relabeled 2026-06-16 from "0.577/ℓ_node": that was the network-velocity factor 1/√3 = c(k→0)/c_link mislabeled as a wavevector; empirical settle b72045d4.)_
  - Forcing a multi-cell propagating-eigenmode test on a bounded interior is a category error; the substrate-correct test measures the integrated boundary observables M, Q, J.
- _Specific Non-Claims and Caveats_
  - Does NOT claim the interior wavenumber is unphysical — it is a real interior eigenmode; the claim is that it is exempt from the lattice Nyquist bound because it does not propagate through the lattice.
  - Applies specifically to structure interior to a Γ=−1 boundary; modes that do propagate through the K4 lattice remain Nyquist-constrained.

> **Leaf references:** [boundary-observables-m-q-j](./boundary-observables-m-q-j.md).

### Quality
- confidence: 0.60
- depends-on:
  - clm-ofys5v — Substrate-observability rule [supplies causal/impedance disconnection of the Γ=−1 interior]
- solidity: 0.55 (use as input only, don't build deeper) [= min(0.60, 0.55)]
- rationale: Given the substrate-observability rule (interior of a Γ=−1 wall is causally and impedance-disconnected), the conclusion that interior eigenmodes (e.g. k≈6.36/ℓ_node) are exempt from the K4 propagating-mode Nyquist wavevector edge k_max~π/ℓ_node (measured √2·π≈4.44/ℓ_node on the srs axis; relabeled 2026-06-16 from the earlier "0.577/ℓ_node", which was the 1/√3 network-velocity factor mislabeled as a wavevector — empirical settle b72045d4) follows cleanly — the lattice never propagates that wave, so the propagating-mode bound does not bind. The local logic is tight; the one caveat is that "the mode lives entirely inside and never couples to the lattice" is taken from the boundary-observability rule rather than shown for the specific horn-torus interior mode. 🟡 **EXPOSURE-DEMOTED 0.65 → 0.60 (2026-07-03, verdict-exposure sweep — status-demotion, NOT retraction).** The 2026-06-24 additive-corroboration banner in [boundary-observables-m-q-j](./boundary-observables-m-q-j.md):91 "partially discharged" the caveat above using the Stage-2 native-cage MODE-III DISPERSE result as empirical evidence that "the bulk interior hosts no propagating self-trapped mode." That DISPERSE evidence is now **HIGH-exposed** — its operator (diamond `TETRA_OFFSETS` `L_D`) is nullspace-heavy/sublattice-decoupled and its only positive control ran on a *different* (Cartesian) engine ([`research/2026-07-03_engine-verdict-exposure-sweep_result.md`](../../../research/2026-07-03_engine-verdict-exposure-sweep_result.md)). So the empirical *discharge* of this claim's rationale caveat is itself under re-adjudication: the caveat ("shown for the specific interior mode") is **re-opened**, and the confidence returns toward its pre-discharge level. The claim's *core* (interior-mode Nyquist exemption from the observability rule, via clm-ofys5v) is unaffected — this demotes the empirical strengthening, not the logical conclusion; **mass = A1 (PR#260) is untouched**.
- strengthen-by:
  - Demonstrate for the specific electron horn-torus interior mode that it has zero projection onto propagating K4 lattice modes
  - State the boundary condition under which an interior mode would leak and thus re-acquire the Nyquist constraint
  - Confirm the integrated-boundary-observable test (M,Q,J) recovers the expected electron observables from this interior structure
---

## Near-Soliton "Compression" Is Impedance-Gradient, Not Bond-Length Compression
<!-- id: clm-3bwhad -->

The substrate's apparent "compression" near matter is a refractive-index / impedance-gradient modulation via the Axiom 4 kernel, not a geometric compression of bond rest lengths.

- _Specific Claims_
  - The canonical gravity-as-substrate-strain prediction $n(r) = 1 + 2GM/(rc^2)$ is refractive-index modulation — impedance modulation $\varepsilon_{\text{eff}}, \mu_{\text{eff}}$ via the Axiom 4 kernel S(A) at each cell — NOT geometric bond-length compression.
  - Bond rest length L_spring is a cosmological-genesis frozen value (per the substrate-scale cooled-equilibrium closure), not a per-cell dynamic field.
  - Engine implementations using fixed-dx Eulerian small-strain on rigid grid geometry are correct for substrate-observability purposes — the right physics for boundary-only observability, not a limitation.
- _Specific Non-Claims and Caveats_
  - Does NOT claim bond rest lengths never change at all — they are set once at cosmological genesis; the claim is that near-matter "compression" is not a dynamic per-cell bond-length field.
  - The correctness of fixed-dx Eulerian engines is asserted relative to substrate-observability (boundary-only observables); it is not a general claim about all simulation requirements.

> **Leaf references:** [boundary-observables-m-q-j](./boundary-observables-m-q-j.md).

### Quality
- confidence: 0.60
- depends-on:
  - clm-ofys5v — Substrate-observability rule [supplies boundary-only observability that motivates fixed-grid Eulerian correctness]
- solidity: 0.55 (use as input only, don't build deeper) [= min(0.60, 0.55)]
- rationale: A conceptual distinction grounded in the canonical n(r)=1+2GM/(rc²) prediction being refractive-index/impedance modulation via the Axiom-4 kernel rather than geometric bond-length change; the local reasoning is internally coherent. The load-bearing assertion that L_spring is a cosmological-genesis frozen value (not a dynamic per-cell field) is stated by reference to the cooled-equilibrium closure rather than derived here, which is the main local gap.
- strengthen-by:
  - Derive (or cite the explicit derivation of) bond rest length as genesis-frozen rather than asserting it
  - Show ε_eff, μ_eff modulation reproduces n(r)=1+2GM/(rc²) quantitatively to confirm the impedance-gradient reading
  - State the regime where fixed-dx Eulerian small-strain is "correct for observability" vs where it would fail, to bound the engine-correctness claim
---

## Substrate-Native Lenz Back-EMF Freezes Topological ω at the Yield Crossing
<!-- id: clm-exjfai -->

When the Cosserat-sector voltage drops through V_yield slowly enough (crossing time ≥ τ_relax), a diverging effective inductance L_eff near S→0 generates a diverging Lenz back-EMF that freezes any topologically non-trivial ω configuration present at the crossing — derived from Axiom 1 + Op14 + Lenz, with no SM/QFT machinery.

> **Field/port retag note (2026-06-10, Grant rename-queue adjudication R2, classical lexicon — claim body above preserved unedited):** the **"Lenz Back-EMF"** named in this claim's title and body is the **PORT** object — the Faraday–Lenz terminal reaction (induced only against changes), the *mechanism* that freezes ω. It must **not** be conflated with the dark-wake $\tau_{zx}$ **WAKE FIELD** (shear channel), whose own port signature is the **radiation resistance** $R_{rad,L}$ (wave-making drag). Field and port are **distinct objects, NOT interchangeable** (corr $0.117$ receipt, `2026-06-10_bemf-feedback-smoke_result.md:79`). This claim is correct as a *port-mechanism* statement; the annotation only fences it off from the field/port conflation flagged at `vacuum_engine.py:46,1478,1487` and `dark-wake-bemf-foc-synthesis.md:125`. Registry §5 R2 (Rule 2).

- _Specific Claims_
  - When V(t) drops through V_yield in the Cosserat sector such that the crossing takes ≥ τ_relax, any topologically non-trivial ω configuration present at the start of the window FREEZES — it cannot unwind because the diverging L_eff (Op14 near S = 0) generates a diverging Lenz back-EMF that blocks dω/dt during the τ_relax window.
  - The frozen residues persist for ≥ 100 Compton periods in the post-heal solid regime.
  - This is the AVE-native mechanism for matter precipitation from cooling vacuum (cosmological lifecycle); it is derived from Axiom 1 (Substrate Topology) + Op14 + Lenz's law, NOT a Kibble-Zurek import.
- _Specific Non-Claims and Caveats_
  - Does NOT claim a closed-form derivation of τ_relax in this leaf; the τ_relax window is taken from the Op14 vacuum-circuit work.
  - The freeze applies in the slow-crossing regime (crossing ≥ τ_relax); the leaf does not characterize the fast-crossing regime.
  - The Op14 cross-sector-trading correlation ρ = −0.990 is an empirical-validation figure for the energy-trading mechanism; the freeze claim is the dynamical consequence at the yield crossing, not itself that correlation measurement.

> **Leaf references:** [dark-wake-bemf-foc-synthesis](./dark-wake-bemf-foc-synthesis.md).

### Quality
- confidence: 0.50
- depends-on:
  - clm-jwyy6l — Mass IS Inductive Resistance [the L_eff↔inductive-impedance identification the freeze mechanism rides on]
  - clm-nxc9gy — Six-Fold Lattice Impedance Decomposition [supplies Z_eff(r)=Z₀/√S → L_eff divergence as S→0]
- solidity: 0.30 (do not build on, rework needed) [= min(0.50, 0.30)]
- rationale: The mechanism is a coherent qualitative chain — Op14 gives L_eff→∞ as S→0, a diverging inductance yields a diverging Lenz back-EMF, which blocks dω/dt across the τ_relax crossing window and freezes topologically non-trivial ω — and the entry honestly flags that τ_relax is imported (not derived here) and that only the slow-crossing regime is treated. It is held at mid-band because the leaf supplies no quantitative comparison of the back-EMF magnitude against the unwinding drive, the ≥100-Compton-period persistence is asserted, and the L_eff divergence rate near S=0 versus the crossing rate is not made explicit, so the "freezes" conclusion is argued, not demonstrated.
- strengthen-by:
  - Show quantitatively that the diverging back-EMF dominates the topological-unwinding torque over the τ_relax window (a magnitude inequality, not a word argument)
  - Derive or cite a closed form for τ_relax and the crossing-rate criterion (≥τ_relax) that defines the slow regime
  - Characterize the fast-crossing regime so the slow/fast boundary is a stated threshold rather than an unbounded caveat
  - Support the ≥100-Compton-period residue persistence with a simulation or decay-rate estimate
---

## FOC d-q Decomposition Is Canonical at Spatial-90° (Temporal Within-Tank Framing Retracted)
<!-- id: clm-533gvm -->

The Field-Oriented Control d-q decomposition is canonical in two Core homes, both at SPATIAL 90° orientation orthogonality (the BH QNM co-rotating frame; atomic-shell orthogonality); the temporal within-LC-tank d-q framing is implementer synthesis and is retracted.

- _Specific Claims_
  - FOC d-q has two canonical Core homes: (a) the BH QNM co-rotating frame, where the Park transform decomposes the lattice spin-phase Ω_H·t into a d-axis (reactive/non-radiating) and q-axis (real/radiating), with back-EMF as curvature radiation; (b) the atomic shell, where the helium 1s² inner core acts as a primary inductive rotor and the 2s² valence pair phase-locks perpendicularly (90° orientation) — isomorphic to FOC stator/rotor 90° decoupling.
  - Both canonical framings are SPATIAL 90° orientation orthogonality.
  - Asynchronous cross-shell decoupling — each filled shell as an independent AC motor winding with $\langle M\rangle \propto \int\cos((\omega_1-\omega_2)t)\,dt \to 0$ — eliminates cross-shell mutual inductance.
  - The temporal within-LC-tank E-vs-B 90° phase split as "FOC d-q" is implementer terminology, not stated in the cited corpus locations, and is RETRACTED from the canonical set.
- _Specific Non-Claims and Caveats_
  - Does NOT claim the temporal within-LC-tank d-q framing is wrong physics — only that it is implementer synthesis pending corpus canonicalization, and is not currently canonical.
  - The FOC isomorphism is structural (operational-role correspondence between motor-drive d-q control and the QNM / atomic-shell decompositions), not a quantitative motor-parameter substitution.
  - The retraction preserves the body content per the retraction-preserves-body convention; the temporal framing is recorded but de-canonicalized.

> **Leaf references:** [dark-wake-bemf-foc-synthesis](./dark-wake-bemf-foc-synthesis.md).

### Quality
- confidence: 0.60
- depends-on:
  - clm-jwyy6l — Mass IS Inductive Resistance [the back-EMF/inductive-rotor framing the FOC homes lean on]
- solidity: 0.30 (do not build on, rework needed) [= min(0.60, 0.30)]
- rationale: The leaf documents two canonical FOC d-q homes (BH QNM co-rotating frame and the helium 1s²/2s² spatial-90° shell) with explicit role-mapping tables and cleanly retracts the temporal within-LC-tank framing as implementer synthesis, so the canonicalization decision is internally consistent and well-scoped. It is held at mid-band because, as the entry concedes, the FOC isomorphism is a structural operational-role correspondence (analogy), not a quantitative motor-parameter substitution, and the asynchronous cross-shell ⟨M⟩→0 integral is asserted at the level of a time-average argument rather than derived.
- strengthen-by:
  - State the explicit Park-transform map (the actual d-q rotation matrix and reference angle) for each canonical home, not just a role-correspondence table
  - Derive the ⟨M⟩∝∫cos((ω₁-ω₂)t)dt→0 decoupling with finite-window bounds rather than asserting the long-time limit
  - Pin the BH-QNM identification to the cited Backmatter Ch.5 derivation so it is not read as a free-standing analogy
  - Confirm in the cited corpus locations that the spatial-90° framing is stated there (the retraction hinges on temporal-90° being absent from the same locations)
---

## A-034 Single-Kernel Unification — One Saturation Kernel at All Scales
<!-- id: clm-gz7ryg -->

A single Axiom 4 kernel $S(A) = \sqrt{1 - A^2}$ (Born–Infeld $n = 2$ squared-limit form) governs every topological-reorganization event in the universe; its vertical tangent at $A = 1$ makes every such event sharp and impulsive across all scales.

- _Specific Claims_
  - The kernel $S(A) = \sqrt{1 - A^2}$ is the same dimensionless function at every scale; $A$ is the same dimensionless quantity (substrate strain / local saturation) regardless of whether the observable manifests as voltage, magnetic field, or frame-dragging strain.
  - The kernel applies cross-scale per Axiom 2 (Topo-Kinematic Isomorphism scale invariance); it is inherited from Axiom 4, not re-postulated per scale.
  - When $S(A) = 0$ locally (at $A = 1$), the substrate cannot continue linear response and must reorganize topologically to a new configuration with $A < 1$.
  - The kernel's vertical tangent at $A = 1$ is the structural reason every topological-reorganization event is sharp and impulsive at all scales.
- _Specific Non-Claims and Caveats_
  - Does NOT derive Axiom 4 itself; the kernel is the postulated Axiom 4 form. This entry asserts its single-kernel cross-scale applicability, not its first-principles origin.
  - Does NOT claim the kernel form is verified at every one of the 26 scales to the same precision; per-scale empirical anchors vary in tightness (BCS at 0.00% error; BH ring-down at 1.7% from GR; several rows carry no quantitative anchor).
  - Born–Infeld $n = 2$ is the squared-limit form; the identification with the AVE saturation kernel is structural, not a derivation of Born–Infeld electrodynamics.

> **Leaf references:** [universal-saturation-kernel-catalog](./universal-saturation-kernel-catalog.md).

### Quality
- confidence: 0.62
- depends-on:
  - clm-sysqaf — Universal Operator Catalog / Axiom 4 kernel form [supplies S(A)=√(1−A²) as the postulated kernel]
- solidity: 0.62 (use as input only, don't build deeper) [= min(0.62, 0.80)]
- rationale: The single-kernel thesis is a manifestation of Axiom 4 (kernel form) conjoined with Axiom 2 (TKI scale invariance); the entry correctly disclaims deriving Axiom 4 and disclaims uniform per-scale validation. The core local move — "same dimensionless A at every scale, kernel inherited not re-postulated" — is asserted via TKI rather than shown that the strain ratio A is genuinely the same dimensionless object across voltage/B-field/frame-drag manifestations, which is the load-bearing unstated step.
- strengthen-by:
  - Show explicitly that the A-ratio reduces to one dimensionless quantity in each manifestation (voltage, B-field, frame-drag strain) rather than asserting it via TKI
  - Distinguish the falsifiable content (Ax2+Ax4 hold at a new scale) from the non-novel restatement, so the unification thesis is not read as a derived prediction
  - State the precision band per scale so "governs every event" is not over-read where no quantitative anchor exists
---

## A-034 Catalog — 26 Canonical Cross-Scale Instances
<!-- id: clm-dxdsvt -->

The A-034 catalog enumerates 26 canonical cross-scale instances of the saturation kernel, spanning 21 orders of magnitude: 17 physical-substrate, 2 biological-substrate, and 5 engineered-substrate instances, plus 2 companion rows scoped for Sessions 4/5.

- _Specific Claims_
  - 26 canonical instances are catalogued, spanning ~21 orders of magnitude from atomic ($\sim 10^{-15}$ m) to cosmic ($\sim 10^{26}$ m) scale.
  - Physical-substrate instances (17): atomic/EM, K4 substrate, DT fusion, Pd hydrogen-loading shatter, BCS, water two-state LC partition, plasma, Kolmogorov turbulence, geomagnetic, planetary spin-axis (Row 9-a, NEW 2026-05-20 Session 2), planetary mag-vs-spin offset (Row 9-b, NEW 2026-05-20 Session 2), solar flare, MOND, galactic spin-axis (Row 11-a, scoped Session 4), BH event horizon, BH ring-down, Big Bang, cosmic DE / ε-sector (Row 14b, NEW 2026-05-19 EOD β Session 2), LSS spin-axis (Row 14-a, scoped Session 5 conditional).
  - Biological-substrate instances (2): lipid bilayer, protein folding.
  - Engineered-substrate instances (5): DC-biased piezoelectric, asymmetric-electrode vacuum-mirror bench, active topological metamaterials, sine-Gordon kink memory, autoresonant rupture.
  - Each instance has a defined $A$ ratio and a saturation event; the catalog records empirical anchors where they exist (BCS $B_c(T)$ at 0.00% error; BH ring-down 1.7% from GR; Schwarzschild exact; Nilsson 2026 X-ray LLCP for water; SPARC galactic rotation 11.5% Q=1 mean residual; planetary scoring 14-15/16 class matches). The stellar solar-flare instance is a forward prediction, with NOAA GOES 40-yr validation pending a live catalog fetch (LF-03). <!-- 🔴 Rule-12 2026-06-15 LF-03: was "...; NOAA GOES 40-yr solar flares; Schwarzschild exact; ...". Superseded per KB leaf vol3/cosmology/ch14-orbital-mechanics/solar-flares-led-avalanche.md: the NOAA GOES comparison is a synthesized illustrative timeline, not a live fetch; forward prediction, not a validated anchor. -->
- _Specific Non-Claims and Caveats_
  - The 26 instances are NOT 26 claims of this leaf; per-instance physics is owned by the respective per-instance leaves elsewhere in the KB. This entry asserts the catalog's membership and cross-scale span, not each instance's individual derivation.
  - Catalog count grew from 21 (2026-05-16 growth notes; water + Pd hydrogen-loading shatter added) to 26 across two further expansion events: +1 cosmic-DE row (β Session 2, 2026-05-19 EOD); +4 planetary/galactic/LSS spin-axis and mag-tilt rows (Soliton-Lattice Coupling Session 2, 2026-05-20). The catalog is explicitly described as growing as evidence accumulates.
  - Row 11-a (galactic spin-axis) and Row 14-a (LSS spin-axis) are scoped for Session 4 and Session 5 adjudication respectively; their symmetry classifications are TBD.
  - Several rows carry no quantitative empirical anchor (e.g., "plasma canonical", "substrate instance"); for those the instance is a structural classification, not a validated measurement.
  - LLM SiLU activation saturation is explicitly kept OUT of the 26: same kernel form but applied in activation space during neural-net training, tracked as a parallel thread.

> **Leaf references:** [universal-saturation-kernel-catalog](./universal-saturation-kernel-catalog.md).

### Quality
- confidence: 0.75
- depends-on:
  - clm-gz7ryg — A-034 Single-Kernel Unification [supplies the one-kernel premise the catalog enumerates instances of]
- solidity: 0.62 (use as input only, don't build deeper) [= min(0.75, 0.62)]
- rationale: Catalog/enumeration claim scored on completeness + internal consistency. The current leaf (`universal-saturation-kernel-catalog.md`) is now arithmetically clean: title, Key-Result row, and the symmetry-classification body all agree on 26 = 19 + 4 + 2 + 1 (SYM 19 / ASYM-N 4 / TBD 2 / ASYM-E 1). The "21 orders of magnitude" is a span axis (atomic $\sim 10^{-15}$ m → cosmic $\sim 10^{26}$ m), not an instance count, so it is no inconsistency. Per-instance derivations are correctly disclaimed as owned elsewhere, anchor-less rows are honestly flagged, and scoped Session-4/5 rows (11-a, 14-a) are tagged TBD. The prior 0.68 was depressed by a count mismatch that no longer exists — a complete, internally consistent enumeration.
- strengthen-by:
  - Tag each row with anchor-tightness (validated / structural-only / scoped-TBD) so "26 canonical" is not read as 26 validated predictions
  - Resolve the scoped Session 4/5 rows (11-a, 14-a) or move them to a clearly-separated pending appendix
---

## The Parity Theorem — Sub-Yield Difference Tone Forbidden by Inversion Symmetry (Difference Channel = Inversion-Symmetry Meter)
<!-- id: clm-invmtr -->

The reversible sub-yield vacuum is a pure-$\chi^3$, inversion-symmetric varactor: the even Axiom-4 kernel $U(r) = 1 - \sqrt{1 - r^2}$ gives an odd restoring force $F(r) = r + \tfrac12 r^3 + \cdots$, so a two-tone spectral line at $m\,\omega_{\text{lo}} + n\,\omega_{\text{hi}}$ exists iff $m+n$ is odd. The literal difference tone $\omega_{\text{hi}} - \omega_{\text{lo}}$ is FORBIDDEN sub-yield by inversion symmetry (forbidden, not suppressed), making the difference channel an inversion-symmetry meter with a measured response law.

- _Specific Claims_
  - FORM-derived, no value import: an even saturation kernel $\Rightarrow$ odd restoring force $\Rightarrow$ pure $\chi^3$ response $\Rightarrow$ a combination tone at $m\,\omega_{\text{lo}} + n\,\omega_{\text{hi}}$ is allowed iff $m+n$ is odd. The difference tone ($m+n = 0$) and DC / rectification are forbidden below yield.
  - Measured (1D mechanism substrate) at the reference pair $(2.6, 4.2)\,\omega_C$: $P_{\text{diff}}/P_{\text{FWM}} \approx 3.4\times10^{-11}$ (at the numerical floor), while the allowed four-wave-mixing product $2\omega_{\text{lo}} - \omega_{\text{hi}}$ ($m+n=1$) carries the beat.
  - Generatively verified in-driver: planting an even ($\chi^2$) term $F(r) \to F(r) + \beta\,r^2$ lights the forbidden difference tone monotonically, power $\propto \beta^2$ (fitted exponent 2.000, $R^2 = 0.99999999$); the allowed FWM sideband stays $\beta$-blind. $\beta = 0$ is the physical reversible vacuum ($P_{\text{diff}} = 1.17\times10^{-16}$ at floor vs FWM $3.46\times10^{-6}$).
  - The difference channel is therefore an inversion-symmetry meter (the vacuum as a biased-varactor difference-tone mixer, conversion $\propto$ bias): a nonzero reading flags an even-order (rectifying) leak. The DC small-signal bias calibration rides on the tangent capacitance $C_{ss} = C_0/S^3$ (clm-vca7r1).
- _Specific Non-Claims and Caveats_
  - MANIFESTATION (Class B), not emergence: a direct consequence of the odd Axiom-4 kernel; no CODATA / SI value is imported.
  - Sub-yield / reactive (lossless, Axiom 3) only: $\beta > 0$ is a planted diagnostic, not a physical vacuum kernel; even-order rectification (pair production) is out of scope (runs stay $\max r \le 0.55$).
  - Interface-scoped: 1D mechanism substrate, drive-clamp geometry. The separate *frequency form factor* claim (whether the $\chi^3$ vertex is frequency-blind above band) is WITHDRAWN — the bulk vertex was NOT probed (the bulk beat collapses $\approx 17.1$ orders toward skin suppression at sep $\ge 3$; see the leaf's SCOPE VERDICT). The super-band coupling fork stays OPEN; the assigned resolution arc is a 3D clamp-free run.
  - Adversarially reviewed: PR #610 BLOCKED (drive-interface artifact) $\to$ repaired (banked what survives, voided the artifact) $\to$ CLEARED. No Letter / clm-gg4wmx edit is licensed by this run.

> **Leaf references:** [universal-saturation-kernel-catalog](./universal-saturation-kernel-catalog.md).

### Quality
- confidence: 0.80
- depends-on:
  - clm-sysqaf — Universal Operator Catalog / Axiom 4 kernel form [supplies the even kernel $S(A) = \sqrt{1 - A^2}$ whose parity forces the odd restoring force]
- solidity: 0.80 (ok to build on, see caveats) [= min(0.80, 0.80)]
- rationale: The core move — even kernel $\Rightarrow$ odd force $\Rightarrow$ pure-$\chi^3$ $\Rightarrow$ combination tones only at odd $m+n$ — is a rigorous parity theorem of the postulated Axiom-4 kernel (FORM-derived, no value import), and the forbidden-ness is not asserted but generatively demonstrated in-driver (planted $\chi^2$ lights the tone $\propto \beta^2$ at exponent 2.000, $R^2$ = eight nines). Held at 0.80 (not higher) because the demonstration is on the 1D mechanism substrate and the meter's operating envelope (sub-yield, reactive) bounds its scope; the interface-vs-bulk frequency question it is often quoted alongside is explicitly WITHDRAWN and carried as a caveat, not folded into this claim.
- strengthen-by:
  - Reproduce the parity-forbidden null and the $\propto \beta^2$ meter law on the 3D clamp-free substrate (the assigned resolution arc), confirming the theorem is geometry-independent as the FORM derivation implies
  - Bound the meter's sensitivity floor (the smallest even-order leak $\beta$ resolvable above the $3.4\times10^{-11}$ difference/FWM floor) as a bench specification
---

## The A⁶ Amplitude Law — χ³ Four-Wave-Mixing Fingerprint of the Odd Kernel
<!-- id: clm-a6chi3 -->

The four-wave-mixing beat power of the reversible sub-yield vacuum scales as $A^6$ (field $\propto A^3$, power $\propto A^6$) — the direct fingerprint of the cubic ($\tfrac12 r^3$) term of the odd Axiom-4 kernel restoring force.

- _Specific Claims_
  - Clean-regime exponent 6.02 (max bond $r < 0.15$, 3 points, $R^2 = 0.999999$) — the $\chi^3$ figure of merit, measured where higher-order ($\chi^5$) terms are negligible.
  - Global exponent 6.16 (all 5 points, $R^2 = 0.9997$) — steeper than 6 because the $\chi^5$ ($\tfrac38 r^5$) term stiffens the slope at the two largest-amplitude points ($r = 0.27, 0.55$).
  - Casting-independent: an $r/\sqrt{S}$ casting reproduces the amplitude shape with prefactor $\tfrac14$ the $r/S$ run (the $\tfrac12{:}\tfrac14$ vertex-coefficient ratio squared).
- _Specific Non-Claims and Caveats_
  - MANIFESTATION (Class B): a consequence of the odd ($\chi^3$) Axiom-4 kernel; no value imported.
  - The two $R^2$ values pair with different exponents and must NEVER be fused: 6.02 $\leftrightarrow$ $R^2 = 0.999999$ (clean regime); 6.16 $\leftrightarrow$ $R^2 = 0.9997$ (global). (An earlier draft conflated them; the review corrected it.)
  - Every measured point is $\ge 10$ orders above the kernel-off floor ($5.1\times10^{-23}$); the floor is a characterization control, not a limit the data reaches (dynamic range $2.7\times10^7$, corrected from a first-draft $2.6\times10^5$).
  - Interface-scoped 1D mechanism substrate; the bulk frequency vertex is the separate WITHDRAWN claim (clm-invmtr SCOPE VERDICT).

> **Leaf references:** [universal-saturation-kernel-catalog](./universal-saturation-kernel-catalog.md).

### Quality
- confidence: 0.78
- depends-on:
  - clm-invmtr — Parity Theorem [establishes the pure-$\chi^3$ (odd-kernel) structure whose cubic term this amplitude law scales]
- solidity: 0.78 (ok to build on, see caveats) [= min(0.78, 0.80)]
- rationale: The $A^6$ power law is the textbook $\chi^3$ four-wave-mixing signature (field $\propto A^3$), and here it is measured cleanly (clean-regime exponent 6.02, $R^2$ = six nines) with a mechanistic account of the $\chi^5$ stiffening at large amplitude (the 6.16 global slope) and a casting-independent cross-check. Held at 0.78 (below the parity theorem it depends on) because it is an amplitude-scaling measurement on the 1D substrate rather than a theorem, and its figure of merit rests on a 3-point clean-regime fit.
- strengthen-by:
  - Extend the clean-regime ($r < 0.15$) fit to more points to tighten the 6.02 exponent beyond the current 3-point basis
  - Reproduce the $A^6$ scaling and the $\chi^5$-stiffening crossover on the 3D clamp-free substrate
---

## A-034 Symmetry Classification — SYM / ASYM-N / ASYM-E
<!-- id: clm-hvvvop -->

The 26 A-034 instances admit a symmetry classification by how the $\varepsilon$ and $\mu$ sectors saturate: SYM (19 instances), ASYM-N (4), ASYM-E (1), TBD (2, scoped Sessions 4/5).

- _Specific Claims_
  - SYM (Symmetric) — vacuum $K = 2G$; $\varepsilon$ and $\mu$ saturate together: 19 instances.
  - ASYM-N (Asymmetric natural) — single-sector saturation (only $\varepsilon$ or only $\mu$): 4 instances — BCS ($\mu$-only), plasma ($\varepsilon$-only), planetary mag-vs-spin offset (Row 9-b, $\mu$-vs-spin candidate), and cosmic-DE $\varepsilon$-only (Row 14b, β Session 2).
  - ASYM-E (Asymmetric engineered) — decoupled $K/G \neq 2$ by design: 1 instance — active topological metamaterials.
  - TBD (pending Session 4/5 adjudication) — 2 instances: galactic spin-axis (Row 11-a) and LSS spin-axis (Row 14-a).
  - The classes partition all 26 instances ($19 + 4 + 1 + 2 = 26$).
- _Specific Non-Claims and Caveats_
  - The asymmetric-saturation variant ($K_{\text{wedge}}/G_{\text{wedge}} \neq 2$) is flagged as a novel kernel topology for separate framework exploration; it is not claimed to be fully developed here.
  - Does NOT claim the ASYM-N / ASYM-E classifications are independently empirically validated as asymmetric; they are structural classifications based on which sector(s) saturate.
  - The classification count tracks the catalog count; if the catalog grows, the per-class counts may change.

> **Leaf references:** [universal-saturation-kernel-catalog](./universal-saturation-kernel-catalog.md).

### Quality
- confidence: 0.60
- depends-on:
  - clm-dxdsvt — A-034 Catalog [supplies the instance set being partitioned]
- solidity: 0.60 (use as input only, don't build deeper) [= min(0.60, 0.62)]
- rationale: A structural classification by which sector (ε/μ) saturates, explicitly NOT independently validated as asymmetric — the entry concedes this. With the count drift resolved (entry and leaf now agree: 19 SYM + 4 ASYM-N + 1 ASYM-E + 2 TBD = 26), the local work is a coherent, exhaustively-bookkept partition of the 26-instance set. Residual local-rigor limits: the TBD bucket leaves 2 scoped rows un-adjudicated, and the SYM-vs-ASYM-N sector assignments (BCS μ-only, plasma ε-only) are structural labels, not derived from a discriminator — holding it below the derived band.
- strengthen-by:
  - Update the entry partition counts to the leaf's current 20/4/1 + 2 TBD and confirm exhaustiveness
  - Provide an empirical or structural discriminator that confirms BCS is μ-only and plasma is ε-only rather than asserting the sector assignment
  - Specify what observation would falsify a SYM-vs-ASYM-N assignment, since the classes are presently structural labels
---

## A-034 ε/μ Axis Classification — Substrate Electromagnetic Dual Resolution
<!-- id: clm-5fu303 -->

The asymmetric-natural (ASYM-N) instances in the A-034 catalog split along an orthogonal axis from the SYM/ASYM-N/ASYM-E classification: which sector (ε or μ) of the substrate's electromagnetic dual saturates preferentially. This makes explicit the gap-cell structure where physics suggests paired ε/μ instances should exist at each scale.

- _Specific Claims_
  - ASYM-N(ε): single-sector ε saturation — plasma cutoff (atomic-EM scale) + cosmic DE / ε-sector (cosmic scale, β Session 2 addition per `op14-cosmic-horizon-profile.md`). Two instances currently.
  - ASYM-N(μ): single-sector μ saturation — BCS $B_c(T)$ (condensed-matter scale). One instance currently (galactic MOND adjudicated SYM per 2026-05-19 EOD).
  - ASYM-N (sector-undetermined): planetary mag-vs-spin offset (Row 9-b, NEW 2026-05-20 Session 2) is a μ-channel-vs-spin-channel relative-saturation candidate; ε-channel of Row 9-a + μ-channel of Row 9-b are companion projections of the same per-node Cosserat rotational coordinate.
  - ASYM-E: engineered metamaterials are designer-controllable decoupled (ε/μ asymmetry by design); single instance.
  - The gap-cell structure (where physics suggests a paired ε/μ instance should exist but corpus does not yet have one) is pre-registered for future research-doc filling at: atomic-EM (μ-companion to plasma GAP), condensed-matter (ε-companion to BCS GAP), planetary (PAIR FILLED 2026-05-20 Session 2), galactic (PARTIAL FILL pending Session 4 via Row 11-a), cosmic (FILLED β Session 2 + Row 14-a Session 5 conditional).
- _Specific Non-Claims and Caveats_
  - This entry asserts the existence and current state of the ε/μ classification axis, not the per-instance derivation of why ε or μ saturates first in any given physical instance.
  - Gap-cells are pre-registered for future filling, NOT claims that the gap is empty. Two interpretive routes remain: (a) corpus has the physics but hasn't enumerated it as a row, or (b) the framework genuinely has only single-sector saturation at those scales for substrate-physics reasons.
  - The Row 11-a galactic spin-axis classification (ε-companion vs μ-extension of MOND) is open and pending Session 4 adjudication.
  - The Row 14-a LSS spin-axis classification is conjectural and scoped for Session 5 conditional.

> **Leaf references:** [universal-saturation-kernel-catalog](./universal-saturation-kernel-catalog.md).

### Quality
- confidence: 0.45
- depends-on:
  - clm-hvvvop — A-034 Symmetry Classification [supplies the ASYM-N set this axis sub-divides]
- solidity: 0.45 (use as input only, don't build deeper) [= min(0.45, 0.60)]
- rationale: Newly minted; asserts the existence and current state of an ε/μ sub-axis on the ASYM-N instances rather than deriving why ε or μ saturates first in any instance (explicitly disclaimed). Several entries are sector-undetermined (Row 9-b candidate), conjectural (Row 14-a), or pending adjudication (Row 11-a), and the gap-cells are pre-registered placeholders, so the populated content is thin relative to the structural scaffold.
- strengthen-by:
  - Derive (or give a substrate-physics argument for) why a given instance saturates in ε vs μ, for at least the two anchored cases (plasma ε, BCS μ)
  - Resolve the sector-undetermined Row 9-b and the pending Row 11-a / 14-a classifications before counting them on the axis
  - Decide each gap-cell between "corpus has it, unenumerated" vs "framework forbids the companion," since the symmetry-completeness argument hinges on which
---

## A-034 Cosmic-Scale Instance — Big Bang as Saturation-Kernel Crystallization
<!-- id: clm-l4o7hv -->

The Big Bang is the cosmic-scale A-034 instance: a spinning parent black hole's frame-drag strain pushes local $A$ to 1, triggering a K4 crystallization front that propagates outward at $c$ and becomes our observable universe.

- _Specific Claims_
  - A spinning parent BH in its embedding parent lattice imparts bulk strain via frame-dragging; the strain extends inside the parent BH's event horizon (Kerr interior frame-dragging continues), which is our universe's pre-crystallization phase.
  - The strain pushes local $A$ toward 1 at the point of maximum concentration (probably along the parent BH's spin axis); at $A = 1$, $S(A) = 0$ and the substrate phase-transitions to K4 lattice.
  - The K4 crystallization front propagates outward at lattice wave speed $c$, sweeping the inherited volume that becomes the observable universe.
  - The Big Bang is therefore not a separate cosmological law but Axiom 4 applied at cosmic scale via the universal kernel.
- _Specific Non-Claims and Caveats_
  - The point of maximum strain concentration is stated as "probably along the parent BH's spin axis" — a hedge, not a settled claim.
  - Does NOT claim the cosmic-formation parameters (parent BH spin, formation temperature) are accessible; per the A-031 cosmic-parameter horizon they are not.
  - Cosmic symmetry of this instance is marked testable (CMB E/B polarization signature) — predicted, not yet confirmed.
  - The cross-scale validation paths (CMB axis-of-evil alignment, universe-age $R_H/c \approx 14.5$ Gyr vs observed $\sim 13.8$ Gyr, avalanche statistics, CMB power-spectrum peaks) are predictions of the catalog, registered as a formal pre-registration; they are not claimed as confirmed results.

> **Leaf references:** [universal-saturation-kernel-catalog](./universal-saturation-kernel-catalog.md).

### Quality
- confidence: 0.40
- depends-on:
  - clm-gz7ryg — A-034 Single-Kernel Unification [supplies Axiom-4 kernel applied at cosmic scale]
- solidity: 0.40 (do not build on, rework needed) [= min(0.40, 0.62)]
- rationale: A qualitative mechanism (parent-BH frame-drag strain → A→1 → K4 crystallization front at c) applied at cosmic scale; the key spatial localization is explicitly hedged ("probably along the spin axis"), the formation parameters are declared inaccessible per the A-031 horizon, and the cross-scale validations (CMB axis alignment, R_H/c age) are registered as predictions, not confirmed. Locally it is a plausibility narrative more than a derivation: no quantitative step ties the parent-BH strain magnitude to the A=1 crossing.
- strengthen-by:
  - Derive the strain-concentration locus (replace the "probably along spin axis" hedge with a Kerr-interior frame-drag argument)
  - Supply a quantitative bridge from parent-BH frame-drag strain to the A=1 saturation crossing
  - Sharpen the R_H/c ≈ 14.5 Gyr vs 13.8 Gyr (~5%) comparison into a stated prediction band with error sources
---

## Universal Operator Catalog (Op1–Op22) — Catalog of Record
<!-- id: clm-sysqaf -->

The 22 universal scale-invariant operators (Op1–Op22) are the AVE engine's named operator basis; this leaf is the catalog of record, anchored to Vol 1 Ch 6.

- _Specific Claims_
  - Vol 1 Ch 6 defines 22 Universal Operators "used identically across all spatial scales of the physics engine"; this catalog is the consolidation single-source-of-truth for their canonical names and formulas.
  - The catalog tags each entry CANONICAL (grep-verified verbatim at ≥3 cross-citations to corpus sources, or explicit equation in Vol 1 Ch 6) or SYNTHESIS (formula is implementer/auditor synthesis without canonical anchor).
  - The Vol 1 Ch 6 Op# set (Op2 Saturation, Op3 Reflection, Op4 Pairwise Potential, Op8 Packing Reflection, Op9 Steric, Op14 Dynamic Impedance) is a different operator set from the CLAUDE.md INVARIANT-N3 Op# list (chemistry/molecular descriptions) — a flagged naming-namespace collision; Vol 1 Ch 6 is the canonical primary.
- _Specific Non-Claims and Caveats_
  - This is a CATALOG leaf — it does NOT own the individual operator formulae. Each operator formula is a claim of its respective Vol 1 Ch 6 leaf; where this catalog restates a formula it cites the Ch 6 leaf (e.g., the Op1 $Z = \sqrt{\mu/\varepsilon}$ formula is owned by `impedance-operator.md`, cited as clm-gdd70j).
  - SYNTHESIS-labelled entries (Op15, Op18, Op20; Op22's doc-81 variant) are explicitly flagged as not canonically anchored; Op20's $\omega_{regime}$ formula and Op22's $M = 1/(1-S)$ doc-81 form are flagged A43 v10/v11 synthesis-as-corpus corrections.
  - The INVARIANT-N3 namespace-collision resolution is left open for auditor-lane review; the catalog does not assert which of the two Op# schemes is correct, only that they differ.

> **Leaf references:** [operators](./operators.md).

### Quality
- confidence: 0.80
- depends-on:
  - clm-gdd70j — Op1 Universal Impedance formula [the one operator formula this catalog restates rather than only pointing to]
- solidity: 0.80 (ok to build on, see caveats) [= min(0.80, 0.80)]
- rationale: As a catalog-of-record this scores high on completeness and internal honesty: every entry is tagged CANONICAL (≥3 cross-citations or explicit Vol 1 Ch 6 equation) or SYNTHESIS, the Op#-namespace collision with INVARIANT-N3 is explicitly flagged not silently merged, and the A43 v10/v11 synthesis-as-corpus corrections (Op20, Op22) are surfaced; it correctly disclaims ownership of the individual formulae.
- strengthen-by:
  - Close the SYNTHESIS-labelled entries (Op15, Op18, Op20) by landing a canonical manuscript or KB anchor, or downgrade them explicitly in the table
  - Resolve the INVARIANT-N3 vs Vol 1 Ch 6 Op# namespace collision in the auditor lane rather than leaving it open
  - Grep-verify the line-number anchors (e.g. Op2 line 101, Op14 line 311) against current Vol 1 Ch 6 source to guard against drift
---

## Op1 Universal Impedance — the Single Structural Invariant
<!-- id: clm-6mvtsf -->

Op1 Universal Impedance $Z = \sqrt{\mu/\varepsilon}$ is the single structural invariant of the AVE framework; all 22 universal operators inherit scale-invariance from it.

- _Specific Claims_
  - Per Vol 1 Ch 6 §1.1, the characteristic impedance $Z = \sqrt{\mu/\varepsilon}$ is the single structural invariant of the framework — no scale-specific modifications, fitting parameters, or domain-dependent redefinitions are required, and every phenomenon in the derivation chain reduces to boundary conditions on this operator.
  - Op2 ($S$) and Op3 ($\Gamma$) are dimensionless ratios (of strain and of impedances respectively), automatically scale-invariant; Op4–Op22 compose Op1+Op2+Op3 with dimensionless coefficients, so all 22 inherit scale-invariance from Op1.
  - Scale-invariance is the framework's distinguishing claim: the same operator code path runs from vacuum lattice ($10^{-13}$ m) to gravitational scale ($10^{26}$ m) — 14 orders of magnitude.
- _Specific Non-Claims and Caveats_
  - The Op1 formula $Z = \sqrt{\mu/\varepsilon}$ itself is owned by the Vol 1 Ch 6 §6.1 Universal Impedance Operator leaf (clm-gdd70j); this entry asserts the catalog-level thesis that Op1 is the inheritance root, not the Op1 formula derivation.
  - The inheritance argument is structural (dimensionless ratios + dimensionless-coefficient composition); it is not an independent per-operator proof that every Op4–Op22 application is scale-invariant in practice.
  - Scale-invariance is stated as the framework's distinguishing claim; whether it holds empirically at every cited scale is the subject of the per-domain leaves, not this catalog.

> **Leaf references:** [operators](./operators.md).

### Quality
- confidence: 0.60
- depends-on:
  - clm-gdd70j — Op1 Universal Impedance Z=√(μ/ε) [supplies the invariant operator this thesis names as the inheritance root]
  - clm-sysqaf — Universal Operator Catalog [supplies the Op1–Op22 set whose scale-invariance is being asserted]
- solidity: 0.60 (use as input only, don't build deeper) [= min(0.60, 0.80)]
- rationale: The inheritance argument is structurally sound for Op2 (dimensionless strain ratio) and Op3 (dimensionless impedance ratio), and the leaf §4 quotes the Vol 1 Ch 6 verbatim single-invariant claim, but "Op4–Op22 compose Op1+Op2+Op3 with dimensionless coefficients, so all inherit" is asserted by construction, not shown per-operator; the entry's own Non-Claims concede this is not an independent per-operator proof, so the local link is a plausible structural argument rather than a derivation.
- strengthen-by:
  - Exhibit the explicit dimensionless-coefficient composition for at least the dimensionful-looking operators (Op4 U(r), Op8 R_g_target, Op19 n(r)) to show invariance survives, rather than asserting it
  - Identify any operator (e.g. Op22 avalanche M=1/S², Op16 c_shear) whose form carries a dimensional scale and confirm it reduces to boundary conditions on Z
  - Cite a worked cross-scale instance where the identical operator code path is verified at two of the named scales (10⁻¹³ m vs 10²⁶ m)
---

## K4 Magic-Angle Condition — K = 2G at u₀* ≈ 0.187, ν_vac = 2/7
<!-- id: clm-iouqn9 -->

The K4 lattice's bulk and shear moduli lock at the magic-angle operating point $K(u_0^*) = 2G(u_0^*)$ with $u_0^* \approx 0.187$; the vacuum Poisson ratio $\nu_{\text{vac}} = 2/7$ follows.

- _Specific Claims_
  - $K(u_0)$ and $G(u_0)$ are functions of the over-bracing parameter $u_0$ (dimensionless ratio of secondary-link length to primary-bond length); at the magic-angle point they lock to $K(u_0^*) = 2G(u_0^*)$ with $u_0^* \approx 0.187$.
  - $K = 2G$ is the trace-reversal identity required by General Relativity for transverse-traceless gravitational-wave propagation.
  - Per the A-034 reframing, the magic-angle condition is equivalent to the substrate-scale saturation condition $S(A^*) = 0$ at the K4 scale.
  - The vacuum Poisson ratio $\nu_{\text{vac}} = 2/7$ follows from $K = 2G$ via the standard isotropic-solid relation.
- _Specific Non-Claims and Caveats_
  - This is the substrate-scale ($u_0^*$ over-bracing, K4 micromechanics) magic-angle claim. It is distinct from the vol1 EMT consistency entry `clm-9s9apq` ("EMT $p_c = 8\pi\alpha$"), which treats $K = 2G$ as the EMT trace-reversal *operating point* given $\alpha$ — a consistency relation at the amorphous-network scale, not the magic-angle over-bracing condition. POSSIBLE-OVERLAP FLAGGED: if a future rescore judges these the same claim, this entry should cite `clm-9s9apq` instead of standing alone.
  - The closure is described as "structural" — the magic-angle equation is explicit and $u_0^* \approx 0.187$ is **asserted, not exhibited** (this entry's own rationale; 2026-06-14 magic-angle-provenance audit), and the individual Cosserat prefactors are not yet derived (see clm-bjceop).
  - $\nu_{\text{vac}} = 2/7$ being load-bearing for $\sin^2\theta_W = 2/9$ and other downstream results is noted as a dependency direction, not derived here.

> **Leaf references:** [q-g47-substrate-scale-cosserat-closure](./q-g47-substrate-scale-cosserat-closure.md).

### Quality
- confidence: 0.60
- depends-on:
  - clm-bjceop — Substrate-Scale Cosserat Prefactors [supplies the constitutive constants behind K(u₀),G(u₀)]
- solidity: 0.55 (use as input only, don't build deeper) [= min(0.60, 0.55)]
- rationale: The ν_vac=2/7 step is rigorous and I verified it — ν=(3K-2G)/(2(3K+G)) at K=2G gives 4G/14G=2/7 exactly — and K=2G is correctly identified as the GR trace-reversal/TT-propagation condition; however the functional forms K(u₀),G(u₀) and the value u₀*≈0.187 are asserted, not exhibited in the leaf, and the entry concedes the closure is "structural" with prefactors not fully derived, so the magic-angle locus itself is the soft link while the ν_vac consequence is firm.
- strengthen-by:
  - Exhibit the explicit K(u₀) and G(u₀) functions and show the K=2G root lands at u₀*≈0.187 (currently both the forms and the root are asserted)
  - Justify the A-034 equivalence "magic-angle ⇔ S(A*)=0 at K4 scale" with the mapping that takes u₀* to A*=1, not just assert it
  - Confirm isotropy: ν_vac=(3K-2G)/(2(3K+G)) assumes an isotropic solid; verify the K4 micropolar medium is effectively isotropic at this scale before applying the relation
---

## |T| = 12 Universality — Four Independent K4 Routes Force χ_K = 12
<!-- id: clm-qwmnhn -->

The tetrahedral rotation group order $|T| = 12$ appears in K4 physics via four independent routes, all converging on 12 — making $\chi_K = 12$ structurally forced by K4 symmetry rather than a fitted parameter.

- _Specific Claims_
  - The proper tetrahedral rotation group $T$ has order $|T| = 12$.
  - Route 1 (baseline coordination): K4 path-count geometry — 4 B-neighbors × 3 other-A sublattices = 12 secondary paths per node.
  - Route 2 (Cosserat dimensional): $(\ell_c/d)^2 \times 2 = 12$ (Cosserat characteristic length squared × bilateral factor).
    - _Naming note (2026-06-10, Grant rename-queue adjudication R4; line above preserved unedited):_ "Cosserat characteristic length" is a first-use alias for the **normative name "Cosserat coupling length"** ($\ell_c = \sqrt{6}\,\ell_{\text{node}}$). One object, three names in canon ("coupling" normative; "couple-stress" at `substrate-temporal-values-definition.md:32`; "characteristic" here). Registry §5 R4; Rule 1.
  - Route 3 (magic-angle unity): $f_{\text{Cosserat}}(u_0^*) = 1$ at the substrate saturation boundary, an orbit-count multiplicity of 12.
  - Route 4 (axiom-level constitutive ratio): $\xi_{K2}/\xi_{K1} = 12$, the K4-symmetry-forced ratio of substrate-scale Cosserat prefactors.
  - Four independent calculations converging on the same integer is strong evidence that $\chi_K = 12$ is structurally forced by K4 symmetry, not a calibration coincidence.
- _Specific Non-Claims and Caveats_
  - The four routes are described as "strong evidence" that 12 is structurally forced — convergence, not a single first-principles proof.
  - Route 4 ($\xi_{K2}/\xi_{K1} = 12$) is itself a self-consistency result (see clm-bjceop); it fixes the ratio, not the individual prefactors.
  - The claim replaces "12 as a fit parameter" with "12 as the tetrahedral rotation group order" — it does not independently derive every downstream use of 12.

> **Leaf references:** [q-g47-substrate-scale-cosserat-closure](./q-g47-substrate-scale-cosserat-closure.md).

### Quality
- confidence: 0.55
- depends-on:
  - Axiom 1 (Substrate Topology — $\chi_K = 12$ is structurally forced by the K4 tetrahedral symmetry of the substrate)
- solidity: 0.55 (use as input only, don't build deeper) [= min(0.55, 1.00)]
- rationale: The four routes converging on 12 is a convergence/plausibility argument explicitly framed as "strong evidence," not a single first-principles proof; |T|=12 (proper tetrahedral rotation group order) is exact, and route 1 (4 B-neighbors × 3 sublattices) is a clean count, but route 2 ((ℓ_c/d)²×2) presupposes ℓ_c/d=√6 and the bilateral factor, route 3 (f_Cosserat(u₀*)=1) is asserted, and route 4 is itself the self-consistency result of clm-bjceop — so the routes are not all manifestly independent and some are partly post-hoc identifications of the integer 12.
- strengthen-by:
  - Demonstrate independence: show routes 2, 3, 4 do not all secretly trace back to the same K4 symmetry input (route 4 ξ_K2/ξ_K1=12 and route 2 (ℓ_c/d)²×2 with ℓ_c/d=√6 look related, since √6²×2=12)
  - Derive ℓ_c/d=√6 and the ×2 bilateral factor in route 2 from K4 geometry rather than from the prefactor cross-check
  - State route 3's orbit-count multiplicity construction explicitly so f_Cosserat(u₀*)=1 → 12 is a calculation, not a label
---

## Substrate-Scale Cosserat Prefactors — μ+κ, β+γ and the Forced ξ_K2/ξ_K1 = 12
<!-- id: clm-bjceop -->

The substrate's continuous Cosserat micropolar constitutive constants satisfy $\mu+\kappa = \xi_{K1}\cdot T_{EM}$ and $\beta+\gamma = \xi_{K2}\cdot T_{EM}\cdot\ell_{\text{node}}^2$; self-consistency forces $\xi_{K2}/\xi_{K1} = 12$, independent of $T_{EM}$.

- _Specific Claims_
  - The substrate's continuous Cosserat micropolar field has constitutive constants $(\mu, \kappa, \beta, \gamma)$ at the axiom level.
  - Q-G47 Sessions 16–17 closed the dimensional framework: $\mu + \kappa = \xi_{K1}\cdot T_{EM}$ and $\beta + \gamma = \xi_{K2}\cdot T_{EM}\cdot\ell_{\text{node}}^2$, with $T_{EM}$ the lattice's electromagnetic string tension and $\ell_{\text{node}}$ the lattice pitch.
  - Self-consistency forces $\xi_{K2}/\xi_{K1} = 12$; the ratio is independent of $T_{EM}$ and is purely K4-symmetry-forced (the same route 4 of the $|T|=12$ universality).
  - Q-G47 Sessions 19 (2026-05-18) closed the individual prefactors: $\xi_{K1} = 8/3$ and $\xi_{K2} = 32$ (clean rationals), derived from the Session 13 discrete moduli $K_0 = 16/7$, $G_0 = 8/7$ via the Lamé identity $\kappa = K - \tfrac{2}{3}\mu$, consistent with the forced ratio $\xi_{K2}/\xi_{K1} = 12$ and cross-checked by recovering the canonical $\ell_c/\ell_{\text{node}} = \sqrt{6}$.
- _Specific Non-Claims and Caveats_
  - The individual prefactors $\xi_{K1} = 8/3$, $\xi_{K2} = 32$ are closed (Sessions 19, 2026-05-18); the residual gap is upstream — the closure chain takes the $K = 2G$ operating-point spring constants $k_a = 2/7$, $k_s = 1/7$ as given rather than deriving them from the K4 unit-cell Cosserat Lagrangian.
  - The substrate-scale prefactors $\xi_{K1}, \xi_{K2}$ are a distinct namespace from the Machian $\xi_M \approx 8.15 \times 10^{43}$ (cosmic-scale impedance integral; its cell-count factor $R_H/\ell_{node}\sim10^{38}$ is *inside* $\xi_M$, not $\xi$ itself — consistent with this leaf's $\xi_{topo}$ entry above) and from $\xi_{\text{topo}} = e/\ell_{\text{node}}$ (charge-displacement conversion); the three-way de-collision is owned by `xi-topo-traceability.md` and cross-referenced, not re-derived here.
  - The dimensional framework is "closed" in the sense of being dimensionally consistent and fixing the ratio; it is not a complete derivation of the constitutive tensor.

> **Leaf references:** [q-g47-substrate-scale-cosserat-closure](./q-g47-substrate-scale-cosserat-closure.md).

### Quality
- confidence: 0.70
- depends-on:
  - clm-qwmnhn — |T|=12 Universality [supplies the K4-symmetry orbit factor that forces the ratio]
- solidity: 0.55 (use as input only, don't build deeper) [= min(0.70, 0.55)]
- rationale: The dimensional closure μ+κ=ξ_K1·T_EM and β+γ=ξ_K2·T_EM·ℓ_node² is dimensionally consistent and the T_EM-independent ratio ξ_K2/ξ_K1=12 is a clean self-consistency result; the individual prefactors are closed (ξ_K1=8/3, ξ_K2=32, Sessions 19 2026-05-18) via a full chain (discrete K_0=16/7, G_0=8/7; Lamé κ=K-(2/3)μ; cross-check recovering ℓ_c/ℓ_node=√6). Confidence held at 0.70 because that closure chain rests on the K=2G operating-point spring constants k_a=2/7, k_s=1/7 taken as given rather than derived.
- strengthen-by:
  - Derive the K=2G operating-point spring constants k_a=2/7, k_s=1/7 that the ξ_K1=8/3 chain takes as inputs
  - Show the self-consistency that "forces" ξ_K2/ξ_K1=12 explicitly (the leaf states it forces but routes the derivation to route 4 of |T|=12)
---

## AVE Analytical Toolkit Index — Canonical Tool-Selection Catalog by Problem Class
<!-- id: clm-h3acr9 -->

The `ave-analytical-toolkit-index` leaf is the canonical consolidating index of the ~30 canonical AVE analytical tools (operators, theorems, kernels, coupling formulas) organized by the 9 recognized analytical-problem classes (coupling, resonance, saturation, time-domain, power, mode, boundary, network, numerical). The catalog asserts: every AVE derivation that maps to one or more problem classes should consult this index before deriving, and the `ave-analytical-tool-selection` skill enforces that consultation. The index status is "canonical tool-selection guide" — not a derivation source, but the authoritative routing layer between problem class and canonical tool leaf.

- _Specific Claims_
  - The 9 problem-class taxonomy (§1 Coupling, §2 Resonance, §3 Saturation, §4 Time-domain, §5 Power, §6 Mode, §7 Boundary, §8 Network, §9 Numerical) exhaustively partitions the AVE analytical-derivation space; any AVE derivation can be located by enumerating which classes it spans.
  - For each problem class, the listed canonical tools (file:line cited from operators.md, Vol 4 Ch 1/11/13/14-20 leaves, Vol 1 Ch 1/6 leaves) are the authoritative entry points; pulling them is mandatory before deriving a new formula in that class.
  - The §10 cross-class composition table is the canonical pattern for problems that span multiple classes (DAMA, Sagnac-RLVE, electron tank Q-factor, cosmological constant closure, MOND).
  - The catalog is LIVING — new canonical tools land via the §12 maintenance discipline, and surfaced gaps (§11) are tracked open until closed.
- _Specific Non-Claims and Caveats_
  - Does NOT claim independent derivation of any tool listed. Tools are pointers to the canonical leaves that own each derivation; the toolkit index is a routing layer, not a derivation chapter.
  - Does NOT claim the 9-class taxonomy is unique or maximally orthogonal — it is a working partition that has so far covered the AVE corpus's analytical-derivation patterns; future physics may surface a §10 new class.
  - Does NOT claim consultation of the index closes the cross-class enumeration discipline by itself — the `ave-canonical-leaf-pull` skill (Step 3) is the upstream catalog enumeration; this index is the problem-class routing layer downstream of that.
  - The skill-enforced consultation is a process claim about how derivations should be done, not a falsifiable physics prediction.

> **Leaf references:** [ave-analytical-toolkit-index](./ave-analytical-toolkit-index.md).

### Quality
- confidence: 0.80
- solidity: 0.80 (ok to build on, see caveats)
- rationale: As a tool-selection routing index the leaf scores high on completeness and internal consistency: a 9-class taxonomy with per-class canonical-tool tables (each with file:line anchor, WHEN-TO-USE trigger, worked example, and load-bearing pitfall), an explicit §10 cross-class composition table, tracked §11 gaps and §12 maintenance discipline; it correctly disclaims independent derivation of any tool and self-flags the taxonomy as a working (non-unique) partition rather than a proven exhaustive one, so the "exhaustively partitions" claim is the only mild overreach.
- strengthen-by:
  - Soften or substantiate the §0 "exhaustively partitions the AVE analytical-derivation space" claim — the entry's own Non-Claim concedes the partition is not unique/maximally orthogonal
  - Add a coverage audit: confirm every Op1–Op22 and every cited Vol 4 tool appears in at least one class so the routing layer has no orphans
  - Grep-verify the file:line anchors across the cited Vol 4 leaves to guard against drift, since the index is meant to be the pre-reg verification gate
---

## Divergence-Test Substrate Map — Operational Falsification-Test Index Over the AVE Prediction Matrix
<!-- id: clm-s3i0lw -->

The `divergence-test-substrate-map` leaf is the operational tracking layer over the canonical narrative catalog (`appendix-experiments.md`) and per-project bench-design leaves under `vol4/falsification/ch11-*`. It catalogues every AVE-distinct prediction that diverges from Standard Model + General Relativity + ΛCDM, mapped to the actual hardware, simulation, or data substrate where the test would run. The Tier A/B/C/D classification (hardware-exists / simulation-exists / Core-only / structural-internal) and the per-row falsification-logic + lifecycle-status + axiom-impact-severity + sibling-repo-substrate columns together constitute the operational falsification-test index of the AVE corpus. Companion to `appendix-experiments.md` (narrative catalog) and to `divergence-test-substrate-map.md`'s own cascade Mermaid diagrams and three tracking matrices (ν_vac=2/7, α=1/(4π³+π²+π), ξ_topo, G, J_cosmic+Ω_freeze, master cross-cascade).

- _Specific Claims_
  - Every row in the map names a specific AVE-distinct prediction with its (a) AVE claim, (b) Standard-physics counterclaim, (c) discriminator, (d) test type (new experiment vs existing-data re-analysis), (e) substrate (hardware / simulation / Core-only / structural), and (f) KB anchors.
  - The Tier A/B/C/D taxonomy (hardware substrate exists / simulation substrate exists / Core-internal derivation only / structural-internal-consistency wins) is the operational scope-and-readiness classification used by orchestration to prioritize executable observers.
  - The cascade diagrams + tracking matrices anchored to ν_vac, α, ξ_topo, G, and J_cosmic+Ω_freeze capture how falsification of a single foundational constant or invariant propagates to which rows.
  - The leaf is the canonical "where to run which test" index; updates land here when a row's lifecycle status, substrate availability, or discriminator changes.
- _Specific Non-Claims and Caveats_
  - Does NOT claim any listed prediction has been experimentally confirmed. Catalog ≠ validation; the index enumerates falsification targets, not validated results.
  - Does NOT independently derive any of the listed AVE predictions — derivations live in the per-row KB anchors and per-project leaves; this map is the routing-and-tracking layer.
  - The Tier D ("structural-internal consistency wins") category is explicitly NOT field-falsifiable by single experiment; treating Tier D rows as falsification targets is a category error.
  - The cascade diagrams capture which-rows-propagate dependencies, not numerical sensitivity coefficients; treating a cascade arrow as a quantitative coupling is over-reading.
  - Sibling-repo substrate references (AVE-PONDER, AVE-HOPF, AVE-Fusion, AVE-Protein, AVE-QED, AVE-APU, AVE-Metamaterials) point into private-repo experimental work; public-KB readers should treat those as scope boundaries for the listed substrate, not as published results.

> **Leaf references:** [divergence-test-substrate-map](./divergence-test-substrate-map.md).

### Quality
- confidence: 0.80
- solidity: 0.80 (ok to build on, see caveats)
- rationale: Scored as an operational catalog/index on completeness and internal consistency: the leaf is thorough (33-row Tier A/B/C/D taxonomy with per-row AVE-claim / standard-counterclaim / discriminator / test-type / substrate / KB-anchor columns, three tracking matrices, and five cascade diagrams), and its scope discipline is explicit and correct (catalog ≠ validation; Tier D not single-experiment falsifiable; sibling-repo refs are scope boundaries not results). It derives nothing itself by design — a routing/tracking layer — so it cannot exceed the catalog band, but within that band it is well-organized and self-consistent.
- strengthen-by:
  - Add a verifier that every row's KB-anchor link resolves and every cited sibling-repo path exists
  - Make the cascade arrows' "which-rows-propagate" semantics machine-checkable against the dependency index
  - Flag rows whose lifecycle-status or substrate-availability is stale relative to the per-project leaves
  - State a coverage check that every AVE-distinct prediction in appendix-experiments.md appears as a row here
---

## Temporal Saturation Regime Classifier — δ_AVE Trichotomy as Orthogonal Third Axis
<!-- id: clm-f0jwtk -->

The `temporal-saturation-regime-classifier` leaf introduces the substrate-native loss tangent $\delta_{\text{AVE}} \equiv t_{\text{sat}}/t_{\text{period}}$ as a temporal-axis classifier orthogonal to (i) the canonical spatial Regime I/II/III/IV taxonomy and (ii) the power-domain phase-angle θ classifier. The temporal trichotomy (Lossless / Cyclic / Lossy) captures how a system EVOLVES through saturation space over its observation window — distinct from where it instantaneously sits and from whether power is dissipated vs cycled. The leaf classifies cross-disciplinary regime taxonomies (fluid dynamics, electromagnetics, semiconductor physics, plasma physics, MHD, nonlinear optics, cavity QED, Casimir, phonons, magnonics, tribology, biological / ion channels, polymer dynamics, quantum coherence) under this temporal axis and maps every row of the A-034 universal-saturation-kernel catalog to a temporal regime.

- _Specific Claims_
  - $\delta_{\text{AVE}} \equiv t_{\text{sat}}/t_{\text{period}}$ is well-defined for any system whose Axiom 4 saturation kernel $S(A) = \sqrt{1-A^2}$ can be evaluated over an observation window; range $\delta_{\text{AVE}} \in [0, 1]$.
  - The trichotomy Lossless ($\delta_{\text{AVE}} \to 0$, persistent Regime I) / Cyclic ($0 < \delta_{\text{AVE}} \ll 1$, oscillating Regime I↔III/IV per cycle) / Lossy ($\delta_{\text{AVE}} \to 1$, persistent Regime III/IV) is the substrate-native temporal partition.
  - The temporal axis is orthogonal to the spatial Regime I/II/III/IV axis and the power-domain θ axis; a complete regime characterization of a system requires all three.
  - The 14 cross-disciplinary tables (fluid, EM, semiconductor, plasma, MHD, nonlinear optics, cavity QED, Casimir, phonon, magnonics, tribology, biological/ion channels, polymer, quantum coherence) classify standard-discipline regimes under the temporal axis; the tag distribution is 4 CANONICAL / 5 EXTENSION / 7 NEW MAPPING / 1 PARTIAL.
  - $\delta_{\text{AVE}}$ at substrate scale is the analogue of EM $\tan\delta$, fluid Reynolds-class distance from inviscid, and cavity-QED $\kappa/g$ — the leaf positions cavity-QED $g/\kappa$ as the closest established-physics homolog.
- _Specific Non-Claims and Caveats_
  - The leaf classifies $\delta_{\text{AVE}}$ as **Class 1 (definitional construct)** per `consistency-vs-emergence` v1.1 — the parameter is defined to classify regimes, NOT to predict observations. Downstream USES of the trichotomy (predictability-scaling, methodology-systematic resolution) ARE Class 4 (emergence), but the classifier itself is taxonomic.
  - The cross-disciplinary unification claim is **TAXONOMIC, not derivational**. The leaf labels EM $\tan\delta$ + fluid Reynolds + cavity QED $g/\kappa$ under a common substrate-physics axis recognizing they all measure the same time-fraction-at-saturation pattern; it does NOT derive their numerical values from $S(A)$ first principles. To make the AVE-distinct unification load-bearing as more-than-taxonomy, the leaf flags: pick one classical-physics value and FORWARD-PREDICT it from $S(A)$ + the $t_{\text{sat}}/t_{\text{period}}$ structure.
  - The Item-1-adjudication methodology-systematic application (Ganalyzer vs Longo cos-γ at 2.99σ separation on SDSS spin-orientation cross-comparison) is explicitly demoted to PROVISIONAL per `ave-discrimination-check` audit; the temporal axis is one of four interpretive alternatives, NOT the load-bearing discriminator until McAdam & Shamir 2023 (same-parent-sample test) lands.
  - The "21-OOM unification via single kernel" framing in commit message `98994c1` was overstated; the leaf's framing-discipline correction (Class 1 definitional per `consistency-vs-emergence`) is the honest level.
  - Several cross-disciplinary tables (cavity QED, tribology, magnonics, polymer dynamics, T1/T2 notation, etc.) are flagged NEW MAPPING — flagged for follow-up KB leaves only if any becomes load-bearing for downstream work.

> **Leaf references:** [temporal-saturation-regime-classifier](./temporal-saturation-regime-classifier.md).

### Quality
- confidence: 0.50
- solidity: 0.50 (use as input only, don't build deeper)
- rationale: δ_AVE ≡ t_sat/t_period is cleanly defined given the Axiom-4 kernel and the Lossless/Cyclic/Lossy trichotomy is a coherent partition, but the entry and leaf both explicitly self-classify it Class 1 (definitional construct, taxonomic NOT derivational) per consistency-vs-emergence, the cross-disciplinary unification is conceded TAXONOMIC-not-derived (no value forward-predicted from S(A)), and the methodology-systematic application is demoted PROVISIONAL. A self-flagged definitional/taxonomic classifier with an open forward-prediction and an unproven orthogonality assertion lands mid-band.
- strengthen-by:
  - Forward-predict one classical value (e.g. tan δ of water at 1 GHz) from S(A)+t_sat/t_period to lift it past taxonomy
  - Prove (not assert) orthogonality of the temporal axis to the spatial Regime I-IV and power-domain θ axes
  - Operationally define t_sat for a system whose A(t) only grazes A_yield (boundary-touching trajectories)
  - Resolve the PROVISIONAL Item-1 methodology application once McAdam & Shamir 2023 lands

---

## Support: C1 LIGO Ringdown Re-Analysis — ω_R·M_g = 18/49 (PASS −0.45%)
<!-- id: sup-5zs5s6 -->

Non-physical analytical support (INVARIANT-S10): a re-analysis of existing LIGO
O1–O3 ringdown fits against the AVE black-hole QNM prediction ω_R·M_g = 18/49,
catalogued as the C1 row of `divergence-test-substrate-map.md`. The Phase-3
v2 Cosserat-back-reaction formula validated at a −0.45% mean (max 2.0% per
event) across three LIGO events vs the GR Kerr QNM reference — analytic
re-analysis work, not a new physical experiment, so it lifts the DERIVATION
branch of its beneficiary. Free-standing (no own dependencies). Wiring the graph
only — the local rigor `quality` and the on-point fraction to the beneficiary
are both `*pending*` (unassessed).

> **Leaf references:** [divergence-test-substrate-map](./divergence-test-substrate-map.md).

### Quality
- quality: *pending*
- solidity: *pending*
- rationale: *pending*
- supports:
  - clm-395gps (f=*pending*) — BH QNM ω_R·M_g = 18/49

---

## Support: C13a SPARC Galactic-Rotation Re-Analysis (CONFIRMED 15.5%)
<!-- id: sup-s1h0og -->

Non-physical analytical support (INVARIANT-S10): the C13a re-analysis of public
SPARC galactic-rotation-curve data against the AVE a₀ + η_eff saturation-kernel
fit, catalogued in `divergence-test-substrate-map.md`. An analytic re-analysis
of existing data (not a new physical experiment), so it feeds the DERIVATION
branch of its beneficiary, the MOND-scale acceleration a₀ claim. Free-standing
(no own dependencies). Both the local rigor `quality` and the on-point fraction
are `*pending*` (wiring the graph, not scoring it).

> **Leaf references:** [divergence-test-substrate-map](./divergence-test-substrate-map.md).

### Quality
- quality: *pending*
- solidity: *pending*
- rationale: *pending*
- supports:
  - clm-u86caq (f=*pending*) — MOND a₀ acceleration scale

---

## Support: C5 CMB Cosmic-Axis Re-Analysis (Outcome-D)
<!-- id: sup-msv2xy -->

Non-physical analytical support (INVARIANT-S10): the C5 executable-observer
re-analysis of Planck PR3 SMICA CMB data for the cosmic-axis alignment, returning
Outcome-D (data insufficient at 3σ) per the C5-CMB-AXIS row of
`divergence-test-substrate-map.md`. An analytic re-analysis of existing data, so
it bears on the DERIVATION branch of the "Eight Cosmic-Axis Observables" claim.
Free-standing (no own dependencies). The local rigor `quality` and the on-point
fraction are both `*pending*` (graph-wiring only; an Outcome-D re-analysis is not
yet scored).

> **Leaf references:** [divergence-test-substrate-map](./divergence-test-substrate-map.md).

### Quality
- quality: *pending*
- solidity: *pending*
- rationale: *pending*
- supports:
  - clm-pe8lpx (f=*pending*) — Eight Cosmic-Axis Observables aligned with the Ω_freeze axis

---

## The Sourced-Charge No-Go Cascade — Four Locks Close One Route
<!-- id: clm-nogo4l -->

The 2026-07-03 EM-readout derivation epic (Axiom 2's last underived leg — does the winding's charge label emerge as a **sourced static exterior field**?) closed the sourced-static-monopole route through **four independent locks**, each discovered by a different instrument and each with its own proof class. This is the SYNTHESIS claim: the four locks close **one route** (the *sourced* co-exact/gradient monopole readout), and the survivors are structurally distinct from the closed sector. Prose umbrella + per-lock cites: [`common/the-sourced-charge-no-go-cascade.md`](the-sourced-charge-no-go-cascade.md).

- _Specific Claims_
  - **Lock 1 — blind-readout retraction (INSTRUMENT class; PR #477).** The Stage-1 blind-readout panel caught a merged null read on a structurally-degenerate observable without a same-pipeline positive control (CLASS-2 apparatus pathology), motivating the 31-row verdict-exposure sweep. An instrument-audit, not a physics negative: it grades evidentiary standing and hard-wired the same-pipeline-liveness requirement into every subsequent Stage.
  - **Lock 2 — sourced-solve tautology (INSTRUMENT/identity class; Stage-1b).** A linear static solve `L φ = b` with a hand-assembled `b` is informationally transparent: `∇·E = +(source − mean)` by construction, so `Q_enc = Σ_Ω(b − mean)` returns its own RHS. A mirror, not an instrument — a tautology of the discrete Gauss theorem. Closes the sourced branch: any reported monopole was assembled by hand.
  - **Lock 3 — [NO-FLUX-STRUCTURAL] maximum principle (THEOREM class; ε > 0).** For the source-free variable-coefficient problem `L_w φ = 0`, `L_w = Bᵀ diag(ε_eff) B`, the Dirichlet energy `φᵀ L_w φ = Σ_edge ε_eff·(Δφ)²` vanishes iff every term does, forcing `φ = const` on the connected srs graph — zero flux for ANY `ε_eff = S(A) > 0`, ANY texture, ANY composition rule (Q/M/X), ANY regime. Established three ways (maximum-principle analytic + panel ablation `max|φ| = 0` exact + 1-D-nullspace check). Honest caveat: the hypothesis is `S > 0` *strictly*; the `S = 0` (rupture-point, `ε → 0`) puncture is out-of-scope and is lane Z's doorway.
  - **Lock 4 — ∂∂=0 continuity (DERIVATION GRADE; Stage-2b step-0 + the β-arc coupling-zoo derivation, PR #488).** Taking the discrete divergence of the chartered Ampère update and using `∇·∇× ≡ 0` (the exact `∂₁∂₂ = 0` boundary-of-boundary identity, PR #483): `∂_t(∇·E) = −∇·J_coupling`, and for the default Ampère-form curl coupling `J_coupling = ∇×(g ω) = curl_adj(·)` the divergence is identically zero, so the enclosed charge is a **conserved constant of motion** set by initial data, not emergent. An algebraic identity needing no integrator. **The step-0 LEAN is now closed at derivation grade** (2026-07-03, β-arc note `research/2026-07-03_jcoupling-divergence-derivation_note.md`): `J_coupling` was derived from Axiom 1, the corpus coupling zoo swept before deriving fresh, and `∇·J` computed per branch on the exact srs DEC → **[NO-AXIOM-NATIVE-TERM]** at the net-monopole grade. The one J-mixed candidate that sources a nonzero local `∇·J` (the A44 gyrotropic converter `W(A)⊙curl_adj(ω)`) sources only a **globally-neutral polarization texture** (`sum(∇·J)=0` exact by Gauss-no-boundary), NOT a net monopole; the chirality candidate is **closed-negative** (both enantiomorphs identical neutral texture; the chiral-difference divergence was a cross-complex category error, corrected). The one residue is a framing fork on the target interpretation (is the electron's charge a net-`∇·E` monopole at all in AVE, or the far-field of a harmonic/winding holonomy?), surfaced to Grant — it does not affect the bin.
  - **The unifying observation.** Locks 3 and 4 are one theorem operating twice: statics dies because `F = ∇×ω = curl_adj(ω)` is a curl (`∇·F ≡ 0`); curl-coupled dynamics dies because `J_coupling = ∇×(gω)` is again `curl_adj(·)`. The same `∂₁∂₂ = 0` theorem closes both routes.
  - **The survivor map.** Lane Z — the harmonic sector `H₁ = ker∂₁ ∩ ker∂₂ᵀ` (the structural complement; `b₁ = 3`, L-independent; the part `∇·∇×≡0` does NOT reach, requiring an edge-field E representation) is where `Q = Link(∂Ω, F) ∈ ℤ` (`clm-ze4clw`) would land. Lane W — winding pairs (`clm-wcoul2`, the inter-winding force). The **J-mixed entry condition is now RESOLVED at derivation grade** (β-arc, PR #488): no axiom-native coupling sources a net monopole; the one J-mixed candidate (A44 converter) sources a globally-neutral polarization texture, so it is NOT a survivor route to net charge (it names a future *bound-charge form-factor* study, not a sourced-charge escape). **Surviving routes = lane Z (harmonic) + lane W (pairs).**
- _Specific Non-Claims and Caveats_
  - **Does NOT claim charge fails.** The claim is that charge is UNSOURCED (no sourced static exterior monopole from constitutive texture or curl-coupled dynamics). Topology (lane Z) and pairs (lane W) remain live; the `Q = Link` label (`clm-ze4clw`) is untouched.
  - **Does NOT touch mass = A1 (PR #260).** Only the sourced-monopole route to the charge readout is closed; the mass sector is unaffected.
  - **The `ε → 0` puncture is a doorway, not a closed door.** Lock 3's honest caveat (a bond exactly at the rupture point, `S = 0`) is where the maximum-principle hypothesis fails; it routes to lane Z, not booked as a closed escape.
  - **CONSISTENCY-class synthesis, not a chord.** This claim consolidates settled adjudications (two instrument-class, two theorem-class) into one route-closure statement; it originates no new emergence content. Lane W's `clm-wcoul2` is itself CONSISTENCY-class (signed-Coulomb is SM-shared).
  - **Lock 4 was a LEAN; the lean is now DERIVATION-closed (2026-07-03, β-arc PR #488).** The `∂₁∂₂ = 0` core was always theorem-grade; the route-closure originally *leaned* on the coupling being a pure curl (the default, not then canon-forced — the J-mixed term was a flag-don't-fix surface to Grant). That open question is now settled by derivation: `J_coupling` derived from Axiom 1, the coupling zoo swept, `∇·J` computed per branch → [NO-AXIOM-NATIVE-TERM] at the net-monopole grade (the one J-mixed candidate sources a globally-neutral texture, `sum(∇·J)=0` exact; chirality closed-negative). One residual **framing fork** on the target interpretation (net-monopole vs holonomy-far-field) is surfaced to Grant — it is a question about what "the electron's charge" IS, not an open route to a sourced monopole.

> **Leaf references:** [the-sourced-charge-no-go-cascade](./the-sourced-charge-no-go-cascade.md).

### Quality
- confidence: 0.80
- depends-on:
  - clm-ze4clw — Q = Link(∂Ω, F) ∈ ℤ, the boundary linking-number charge dictionary (the label the cascade routes to the harmonic sector)
  - clm-4r4jiy — the A_geom ∝ 1/r Coulomb potential in the gapless EM-ε channel (the co-exact/gradient sector the cascade closes)
  - clm-wcoul2 — the engine-derived Axiom-2 winding-pair interaction leg (lane W survivor)
- solidity: 0.55 (use as input only, don't build deeper) [= min(0.80, 0.55)]
- rationale: CONSISTENCY-class SYNTHESIS. Consolidates four independently-established locks into one route-closure statement: two instrument-class (Lock 1 blind-readout, PR #477; Lock 2 sourced-solve tautology, Stage-1b — records of what an apparatus can/cannot read, not physics negatives) and two theorem/derivation-class (Lock 3 [NO-FLUX-STRUCTURAL] maximum principle, established three independent ways; Lock 4 ∂∂=0 continuity, an algebraic identity on the chartered update grounded in the srs DEC `∂₁∂₂=0` theorem, PR #483). **Own-confidence raised 0.75 → 0.80 (2026-07-03, β-arc PR #488): Lock 4's LEAN is now DERIVATION-closed** — the coupling-zoo derivation swept every axiom-native `J_coupling` and computed `∇·J` per branch, returning [NO-AXIOM-NATIVE-TERM] at the net-monopole grade (the one J-mixed candidate sources a globally-neutral polarization texture, `sum(∇·J)=0` exact; chirality closed-negative). So (a) all four locks are now solid — two instrument, one theorem, one derivation — with the two structural locks (3, 4) mutually reinforcing (the unifying observation: one theorem operating twice); (b) the residual open item is a *framing fork* on the target interpretation (net-monopole vs holonomy-far-field), surfaced to Grant, not an open route; (c) the scope guard is load-bearing: this is UNSOURCED-charge, not failed-charge — topology (lane Z, `b₁=3` harmonic sector) and pairs (lane W, `clm-wcoul2`) remain live, and the `ε→0` puncture is a doorway. Solidity 0.55 is still the dep-floor from `clm-wcoul2` (minimum-link), gating below own-confidence 0.80 — the confidence rose but the buildability floor is unchanged (the synthesis is no more buildable-upon than its weakest live dep). An organizing-frame synthesis, not a new emergence claim.
- strengthen-by:
  - [RESOLVED 2026-07-03, β-arc PR #488] ~~Establish (or refute) the J-mixed coupling term's divergence analytically BEFORE any Stage-2b integrator build~~ — DONE: [NO-AXIOM-NATIVE-TERM] at derivation grade; the J-mixed term sources a globally-neutral texture, not a net monopole. Residue: the target-interpretation framing fork (β-note §6) routes to Grant.
  - Build the lane-Z edge-field E instrument (the DEC harmonic projector `H₁ = ker∂₁ ∩ ker∂₂ᵀ` on the 1-cochain) and test whether the winding's Link charge lands on the harmonic sector (the fluxoid hypothesis — lane-Z step-0 confirmed the DOF exists on `H₁` for the (2,3) torus core but is value-unpinned; see `clm-ze4clw` neighborhood)
  - If a *bound-charge / vacuum-polarization form-factor* study is ever built, the (J-mixed) A44 converter is its axiom-native transducer (the β-note §5.2 named term) — a polarization, not a net-charge, instrument

---

## The AC/DC Carve — the Epistemological Mechanism of FORM/VALUE
<!-- id: clm-acdc07 -->

The organizing-principle META-FINDING (Grant-ratified 2026-07-03; evidence = the entire 2026-07 arc ledger): **modern physics is a perfected AC theory that demoted the DC sector to bookkeeping; AVE's distinctive bet is that the DC sector is a physical medium state.** This is the epistemological MECHANISM underneath the FORM/VALUE split — the reason the per-constant record reads "FORM = chord, VALUE = echo." Prose home + evidence cites: [`common/form-deriving-value-importing.md`](form-deriving-value-importing.md) §"The AC/DC carve" (this claim is hosted there).

- _Specific Claims_
  - **The carve.** The incumbent frameworks systematically removed the static/longitudinal/uniform-offset DOFs from the dynamics and kept them only as bookkeeping: Gauss's law is a **constraint, not an evolution equation** (`∇·E = ρ/ε₀` fixes the longitudinal field, does not propagate); the longitudinal/static DOFs are **gauge-quotiented** (Coulomb-gauge static field non-dynamical; longitudinal + timelike photon cancel; free photon transverse by construction); **vacuum energy is renormalized away** (the DC offset subtracted, only differences observable). AVE's bet re-physicalizes each discarded DC quantity as a real medium operating-point state: gravity = the `S(A)` operating-point field; dark energy = a real DC offset; charge = topological boundary data (`Q = Link(∂Ω, F) ∈ ℤ`); yield walls = material limits (`V_yield`).
  - **(i) Measurement principle.** All measurement is AC — a uniform DC bias is gauge-relative and self-cancels (= relativity, with the constructive-relativity mechanism: wave-made rulers/clocks ride the same offset). Every AVE-distinct observable is an AC reading of a DC gradient or topology — differential BY PRINCIPLE, not by experimental limitation (the PHASE-ONLY north-star, mechanized).
  - **(ii) FORM/VALUE unification.** The FORMS AVE derives are the shared AC equations (⇒ peer-with-SM recurs BY CONSTRUCTION); the VALUES it imports are DC calibrations (`α` = operating point `A = √α`; `m_e` = bias scale; `G` = boundary termination). "FORM = chord / VALUE = echo" and "AC = shared / DC = where the bet lives" are the SAME statement — this is why the carve extends the FORM/VALUE leaf.
  - **(iii) Falsification asymmetry.** AC agreement cannot distinguish (consistency, never a chord); AC disagreement = an AVE bug (Maxwell recovery mandatory in the `S → 1` linear limit); distinctive kills AND wins live DC-side or in DC→AC coupling.
  - **(iv) Selection rule.** A candidate discriminating test must be DC→AC coupling class (take a DC medium state, read it out through an AC channel where the DC-blind incumbent predicts nothing distinctive). The lone bankable forward falsifier — E-route vacuum birefringence (`clm-pp3qwf`) — IS one: a DC E-bias loads the ε-varactor DC operating point, the AC probe-index readout sees a tree-level coefficient the incumbent loop-suppresses by `α³`. Confirming instance.
  - **Consistent-with illustration (NOT independent validation — cold-eyes 2026-07-03).** The 2026-07-03 sourced-charge no-go cascade (`clm-nogo4l`) is the carve operating in code: the statics deaths (Stage-1b sourced-solve tautology `∇·E = +(source − mean)`; Stage-2a [NO-FLUX-STRUCTURAL] `φ = const`) re-find "you cannot AC-source a DC monopole" (Gauss-is-a-constraint, on the lattice); the `∂∂=0` continuity closure (`∂_t(∇·E) ≡ 0`) re-finds "vacuum DC content is not created by AC dynamics" (theorem grade). The survivors (lane Z harmonic-DC, lane W DC-linking pair, the J-mixed DC→AC coupling) are exactly the carve's selection rule read off the engine output. **Caveat (cold-eyes audit `research/2026-07-03_cold-eyes-program-audit_result.md` §1):** the cascade's arc designs were steered by the carve's own selection rule (iv), so this is a *consistent-with instance*, NOT independent empirical support — the cascade's core facts (∂₁∂₂=0, the maximum principle) are true independent of the carve, but "validation" is reserved for a forward DC→AC falsifier (`clm-pp3qwf`).
- _Specific Non-Claims and Caveats_
  - **Organizing PRINCIPLE, not a theorem.** The carve is the reason the accumulated FORM/VALUE record reads the way it does (a strong, evidence-backed frame) — it is NOT derived from the axioms. A single AC-side discriminating chord, or a DC-side null on the selection rule, would revise it. Booked at consistency / meta-finding class, the same standing as the FORM/VALUE umbrella it mechanizes.
  - **Not an emergence claim.** It mints no new value, forces no new number; it re-reads the settled provenance record through the DC/AC lens. Do NOT headline it as emergence.
  - **Does NOT redefine the per-constant table.** Added KEEP-BOTH — the α/G/K=2G/E_yield/m_e verdicts stand unchanged; the carve supplies WHY they land where they do.
  - **The DC-side bet is itself untested.** That gravity, dark energy, charge, and yield walls ARE physical DC medium states (not bookkeeping) is AVE's distinctive HYPOTHESIS — the thing the framework is betting on, not a result. The carve names the bet cleanly; it does not confirm it.

> **Leaf references:** [form-deriving-value-importing](./form-deriving-value-importing.md).

### Quality
- confidence: 0.65
- depends-on:
  - clm-pp3qwf — E-route vacuum birefringence coefficient (the confirming DC→AC coupling-class instance of selection rule iv)
  - clm-nogo4l — the sourced-charge no-go cascade (the 2026-07-03 consistent-with illustration: the carve operating in code — steered by the carve's own selection rule, so NOT independent validation; cold-eyes audit §1)
- solidity: 0.55 (use as input only, don't build deeper) [= min(0.65, 0.55)]
- rationale: ORGANIZING-PRINCIPLE / META-FINDING, consistency-class — NOT a theorem and NOT an emergence claim. Own-confidence 0.65 reflects that the carve is a strong evidence-backed FRAME (it is the mechanism the accumulated FORM/VALUE record already exhibits: the incumbent's Gauss-constraint / gauge-quotient / renormalized-vacuum DC bookkeeping vs AVE's DC-medium-state bet, each documented in canon), with one confirming forward DC→AC selection-rule instance (`clm-pp3qwf`, the non-circular leg) and one consistent-with illustration (the 2026-07-03 cascade, `clm-nogo4l`, the carve operating in code — steered by the carve's OWN selection rule (iv), so NOT independent validation; cold-eyes audit `research/2026-07-03_cold-eyes-program-audit_result.md` §1) — but it is NOT derived from the axioms, and (a) a single AC-side discriminating chord or (b) a DC-side null on the selection rule would revise it. Independent validation is still owed (a forward `clm-pp3qwf`-class falsifier landing). Booked at the same standing as the FORM/VALUE umbrella it mechanizes (`def-ch0rd1`/`def-ech0v1`/`def-fmv001`), not headlined as emergence. The DC-side bet itself (gravity/DE/charge/yield ARE physical DC states, not bookkeeping) is AVE's distinctive HYPOTHESIS — named cleanly, not confirmed. Solidity 0.55 is the dep-floor from the confirming instances (minimum-link), gating below own-confidence 0.65 — honest: a meta-frame is no stronger than its strongest confirming test. (Confidence UNCHANGED at 0.65 — the claim was already honestly graded as an organizing principle; the cold-eyes correction sharpens the "validation" wording, not the grade.)
- strengthen-by:
  - Land a second independent DC→AC coupling-class forward falsifier beyond `clm-pp3qwf` (the selection rule iv predicts the discriminating tests cluster here; a second instance would move the carve from one-example to a pattern)
  - Convert the DC-side bet from hypothesis to test on ONE of its four medium-state claims (gravity = `S(A)` operating point / DE = real DC offset / charge = topological boundary data / yield = material limit) — the `𝒥_cosmic` three-route operating-point test is the standing candidate (one DC operating point setting EM + gravity + cosmology)
  - Formalize the "all measurement is AC" principle against a concrete uniform-bias null (the retired rotor-Sagnac / static-fiber corroborative-nulls) as a machine-checkable selection filter in `ave-discrimination-check`
