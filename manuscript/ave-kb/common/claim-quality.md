# Common (Cross-Volume Resources) — Claim Quality

<!-- path-stable: referenced from CLAUDE.md INVARIANT-S7 and from common/index.md bootstrap directive -->

> **Canonicality:** Leaves are canonical; this directory's indexes are derived summaries. See [cross-cutting claim-quality register](../claim-quality.md) for the full preamble and the canonical list of project-wide tripwires (the cross-cutting sidecar is the source of truth for which tripwires are project-wide; do not infer the list from this preamble). Entries below are scoped to the common/ directory's substantive content (mathematical closure status, derivation chain, falsification index, translation tables, solver toolchain).

---

## Mathematical Closure Status — "Structurally Zero-Parameter," Not Absolutely
<!-- id: clm-sxn6eo -->

The common-resources documents repeatedly assert AVE's "zero free parameters" status. The unqualified headline collapses a real distinction the leaves make explicit: the chain is *structurally* zero-parameter, conditional on Layer 8 closure of $\{m_e, \alpha, G\}$, with one currently-fitted scalar.

- _Specific Claims_
  - The forward derivation DAG (Layers 0–7) is acyclic by inspection: every derived quantity depends only on Layer-0 inputs $\{m_e, \alpha, G, \hbar, c, e, \mu_0, \varepsilon_0, T_{CMB}\}$ + Axioms 1–4 + earlier-layer derivations.
  - 26 Standard Model parameters reduce to a 3-element bounding set $\{m_e, \alpha, G\}$ + four axioms. The reduction is rigorous; closure of the bounding set itself is the additional Layer-8 step.
  - Cold-lattice $\alpha^{-1}_{ideal} = 4\pi^3 + \pi^2 + \pi$ (Vol 1 Ch 8 Golden Torus) is an algebraically self-contained closure of $\alpha$ — acyclic by inspection.
  - $G$-closure via $\xi = 4\pi(R_H/\ell_{node})\alpha^{-2}$ is acyclic *conditional on the prior $\alpha$ and $m_e$ closures*.
  - "Structure predicted, magnitude fit" is the same disclosure pattern Vol 6 carries for nuclear masses (one fitted scalar per nucleus); both are structurally disclosed, not silently fit.
- _Specific Non-Claims and Caveats_
  - Does NOT claim the framework is *absolutely* zero-parameter today. The thermal-running magnitude $\delta_{strain} \approx 2.225 \times 10^{-6}$ at $T = T_{CMB}$ is **one currently-fitted scalar** back-subtracted from CODATA via `DELTA_STRAIN = 1 - (1/ALPHA)/ALPHA_COLD_INV`. The structure (existence + sign of thermal running below the cold-lattice asymptote) is predicted; the magnitude is pending derivation from $G_{vac}$ + equipartition.
  - Does NOT claim Layer-8 $m_e$ closure is established. The $m_e \leftrightarrow \ell_{node}$ pair carries one input scale; the Nyquist-resolution-of-smallest-stable-soliton proposal is acyclic only if "smallest stable soliton" is well-defined without circular reference to $m_e$. Open.
  - Does NOT claim a Clay-rigorous Yang-Mills mass gap or Navier-Stokes regularity proof. The framework-derived results are **lattice-conditional** (Master Prediction Table notes #14, #15). The lattice cutoff itself is what makes the bounds finite.
  - The four "Outstanding Rigour Gaps" (δ_strain magnitude at T_CMB; m_e closure via Nyquist independence; flux-tube radial profile / Gaussian ansatz; H_∞ closure independent of R_H) are bounding constraints on the closure claim — not calculational errors elsewhere in the chain. Closing any of them strengthens the headline; none invalidate the existing predictions.
  - "26 / 26 derived" is correct *conditional on Layer 8 closure*; without that closure, the count is "25 of 26 expressed as functions of three bounding limits, of which one ($m_e$) is the input scale."

> **Leaf references:** `mathematical-closure.md` §Outstanding Rigour Gaps, §Acyclicity verdict, §Back-edges; `full-derivation-chain.md` §Layer 7 → 8, §Standard Model Parameter Accounting; `xi-topo-traceability.md` §Zero-Free-Parameter Chain.

### Quality
- confidence: 0.70
- solidity: 0.70 (ok to build on, see caveats)
- rationale: Meta-disclosure of the project-wide closure status — structural reduction of 26 SM parameters to $\{m_e, \alpha, G\}$ + four axioms is sound, the four Outstanding Rigour Gaps are correctly enumerated, the forward DAG is verified acyclic, and the back-edge $\alpha$ closure (cold lattice = $4\pi^3+\pi^2+\pi$) is acyclic by inspection. The "*structurally* zero-parameter conditional on Layer-8 closure" framing is rigorously honest. Cross-references the same gaps tracked in vol1 Zero-Parameter Closure Status (`clm-5xon03`).
- strengthen-by:
  - Derive $\delta_{strain}$ magnitude at $T_{CMB}$ from $G_{vac}$ + equipartition (currently back-subtracted from CODATA — one fitted scalar)
  - Demonstrate Nyquist-resolution-of-smallest-stable-soliton without circular reference to $m_e$ (closes the $\{m_e, \ell_{node}\}$ input scale)
  - Replace the Vol 2 Layer-6 proton flux-tube Gaussian ansatz with an axiom-derived profile (sech² kink, Bessel J₀ fundamental, or Axiom-4 algebraic kernel); re-evaluate $\rho_{threshold}$ and $\mathcal{V}_{total}$ against the new profile
  - Derive $G$ from local thermodynamic balance independent of $R_H$, promoting the $H_\infty$ identity to a true downstream prediction

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

> **Leaf references:** `full-derivation-chain.md` §Layer 5 Methodology disclosure, §Standard Model Parameter Accounting, §Layer 8 closure; `mathematical-closure.md` §The Directed Acyclic Graph (DAG) Proof.

### Quality
- confidence: 0.65
- depends-on:
  - clm-0ktpcn — Golden Torus α Derivation (solidity 0.41) [α appears at multiple layers; α-bottleneck cascades through chain]
- solidity: 0.27 (do not build on, rework needed) [= 0.65 × 0.41]
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

> **Leaf references:** `appendix-experiments.md`; per-protocol detail lives in cited Vol IV Ch 11 (`falsification/...`) and Vol 3, Vol 5, Vol 7 leaves.

### Quality
- confidence: 0.85
- solidity: 0.85 (ok to build on)
- rationale: Honest catalog of designed falsification protocols; correctly self-bounds as catalog ≠ validation. The Vol 5 chiral FRET entry is explicitly listed as currently-unfalsifiable (sub-attometer signal at terrestrial baselines), modeling the right disclosure pattern. Per-protocol numerical thresholds belong in their respective per-volume leaves; the index's role is enumeration. No entry-level scored dependencies — the catalog status is independent of any specific protocol's experimental outcome.
- strengthen-by:
  - Run the listed bench protocols (PONDER-N, CLEAVE-01, HOPF-N, ROENTGEN-03, ZENER-04, TORSION-05) and update entries with results when available
  - Add explicit status flags (designed / in-progress / completed / inconclusive) per entry to distinguish "catalog target" from "test pending" from "test completed"

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

> **Leaf references:** `solver-toolchain.md` §Regime-Boundary Eigenvalue Method, §Protein Backbone Eigenvalue, §Nuclear Eigenvalue, §Cross-Scale Isomorphism Table; cross-cutting Symmetric vs Asymmetric Saturation in [`../claim-quality.md`](../claim-quality.md); BH-specific tripwires in [`vol3/claim-quality.md`](../vol3/claim-quality.md).

### Quality
- confidence: 0.65
- depends-on:
  - clm-0ktpcn — Golden Torus α Derivation (solidity 0.41) [α appears in BH $r_{eff} = r_{sat}/(1+\nu_{vac})$, pion via $m_p$, etc.]
- solidity: 0.27 (do not build on, rework needed) [= 0.65 × 0.41]
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

> **Leaf references:** `translation-tables/translation-circuit.md`, `translation-tables/translation-biology.md`, `translation-tables/translation-qm.md`, `translation-tables/translation-particle-physics.md`, `translation-tables/translation-gravity.md`, `translation-tables/translation-cosmology.md`, `translation-tables/translation-condensed-matter.md`; H-bond canonical values asserted at [CLAUDE.md INVARIANT-C3](../CLAUDE.md#invariant-c3-h-bond-canonical-values).

### Quality
- confidence: 0.85
- solidity: 0.85 (ok to build on)
- rationale: The seven translation tables are notation-and-vocabulary maps, correctly self-bounded as not constituting independent predictions. Circuit translation rows ($Q \leftrightarrow x$, $I \leftrightarrow v$, etc.) are dimensionally-exact identities given $\xi_{topo}$ from Axiom 2. The biology table inherits canonical H-bond values from Vol 5 (cross-volume invariant INVARIANT-C3). The medical / therapy rows (cancer, RLT, anesthesia) are correctly framed as framework-internal interpretive identifications, not therapeutic claims. No entry-level scored dependencies — the translations are structural maps given Axiom 2's $\xi_{topo}$ mechanism (a framework input).
- strengthen-by:
  - none entry-local — translation tables are correctly self-bounded as notation maps; substantive predictions live in the per-volume target leaves with their own quality entries

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
  - The "Zero-Free-Parameter Chain" diagram routes through the Golden Torus closure of $\alpha$ — and is therefore conditional on the same Layer-8 thermal closure of $\delta_{strain}$ at $T_{CMB}$ that the Mathematical Closure entry above bounds. The leaf carries this conditional statement; the chain is not unconditionally zero-parameter.

> **Leaf references:** `xi-topo-traceability.md` §Physical Meaning, §Coverage Summary, §Zero-Free-Parameter Chain; ξ vs ξ_topo distinction at [CLAUDE.md INVARIANT-C2](../CLAUDE.md#invariant-c2-electromechanical-transduction-constant) and [LIVING_REFERENCE.md](../../../LIVING_REFERENCE.md) Axiom 3 entry.

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

> **Leaf references:** `appendix-derived-numerology.md` §Core Constants, §Important Exclusion, §Effective Coordination Number Derivation, §The Macroscopic Avalanche Exponent, §The Kolmogorov Constant; scale-invariance pattern at [LIVING_REFERENCE.md §Scale Invariance Principle](../../../LIVING_REFERENCE.md#scale-invariance-principle).

### Quality
- confidence: 0.70
- depends-on:
  - clm-0ktpcn — Golden Torus α Derivation (solidity 0.41) [α-dependent constants throughout: $V_{yield}$, $p_c$, etc.]
- solidity: 0.29 (do not build on, rework needed) [= 0.70 × 0.41]
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
  - Each stress test states a challenge to the AVE framework's discrete-elastic-solid picture and gives an AVE-internal resolution: Spin-1/2 via Finkelstein-Misner kink (Dirac belt trick) on the extended $0_1$ unknot; holography via cross-sectional porosity $\Phi_A \equiv \alpha^2$; Peierls-Nabarro via dynamic Shear Transformation Zone in an amorphous Dielectric Saturation-Plastic substrate.
  - The "Summary of Exact Analytical Derivations" subsection enumerates derivations that appear elsewhere in the KB (lattice pitch, packing fraction, $\nu_{vac}$, $\kappa_{FS}$, proton mass, $H_\infty$, $a_{genesis}$, Witten effect fractional charges). These are summarised here for cross-reference, not asserted independently.
  - The dropped τ_yield comment (HTML comment block, 2026-04-20 audit) honestly records a removed Bingham-Plastic Limit claim that lacked derivation — preserved as an editorial transparency record.
- _Specific Non-Claims and Caveats_
  - The stress-test resolutions are **framework-internal explanatory** content. They show the framework is not naively falsified by classical solid-state objections; they are not independent derivations or experimental tests.
  - The "Three-Parameter Theory" → "Zero-Parameter framework" transition language inherits the same conditionality flagged in the Mathematical Closure entry above. "Closed Zero-Parameter framework" is conditional on Layer-8 closure of $\{m_e, \alpha, G\}$.
  - The Computational Graph Architecture and DCVE specifications are simulation-engine constraints (Poisson-disk genesis, Chiral LC over-bracing $C_{ratio} \approx 1.187$, Symplectic Euler updates). They are **engineering specs for instantiating AVE in a discrete computer**, not physical claims about the vacuum.
  - The "AQUAL Galactic Dynamics" subsection inherits the cross-cutting MOND boundary: $a_0 = c H_\infty / (2\pi)$ is derived (10.7% below empirical) and applies in the unsaturated regime only (Vol 3 MOND entry). The appendix's reference is structural, not a separate validation.

> **Leaf references:** `appendices-overview.md` §Theoretical Stress Tests, §Summary of Exact Analytical Derivations, §Computational Graph Architecture; MOND entry at [`vol3/claim-quality.md`](../vol3/claim-quality.md).

### Quality
- confidence: 0.75
- solidity: 0.75 (ok to build on, see caveats)
- rationale: The "Theoretical Stress Tests" subsection presents framework-internal paradox resolutions (Spin-1/2 via Finkelstein-Misner kink; holographic-information via $\Phi_A \equiv \alpha^2$; Peierls-Nabarro via Shear Transformation Zone) — correctly framed as framework-internal explanatory content, not independent proofs. The "Summary of Exact Analytical Derivations" is a cross-reference index of derivations whose canonical entries live elsewhere; consulting those is the right path for substantive use. The dropped τ_yield Bingham-Plastic comment (HTML comment block, 2026-04-20 audit) is a model editorial-transparency record. The Computational Graph Architecture (DCVE specs) is correctly framed as engineering specifications for instantiating AVE in a discrete computer, not physical claims. No scored dependencies at the entry level — the entry is a meta-summary; substantive solidity lives in the per-claim entries it references.
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

> **Leaf references:** `appendix-spice-verification.md` §Architecture, §Verification Protocol; LIVING_REFERENCE.md Critical Distinction #5.

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

> **Leaf references:** `appendix-vca-symbols.md` §Five Symbol Design Rules, §Seven Canonical VCA Markers, §Canonical Symbol Catalogue (17 Components); $V_{yield}$ canonical value at [CLAUDE.md INVARIANT-C1](../CLAUDE.md#invariant-c1-dielectric-yield-limit); Axiom 4 saturation kernel at [CLAUDE.md INVARIANT-S2](../CLAUDE.md#invariant-s2-ave-axiom-numbering).

### Quality
- confidence: *pending*
- depends-on:
  - INVARIANT-S2 / Axiom 4 (universal saturation kernel — markers and active-symbol semantics)
  - INVARIANT-C1 ($V_{yield} \approx 43.65$ kV — referenced in the catalogue's key-parameter column)
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

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

> **Leaf references:** `two-engine-architecture-a027.md` §The two engines, §Validation: v14 Mode I PASS, §Implications for simulation workstreams.

### Quality
- confidence: *pending*
- solidity: *pending*
- rationale: *pending — L3-migration port; quality scored at the rescore pass*
- strengthen-by:
  - *pending*

---

## Wave-Speed Modulation Is Required to Localize a Bound State
<!-- id: clm-zfqd9v -->

A simulation engine can trap a propagating wave into a localized bound state only if it modulates the wave speed, $c_{eff}(V)$. K4-TLM has $Z(V)$ but not $c_{eff}(V)$, so it cannot produce trapped solitons; Master Equation FDTD has both and does.

- _Specific Claims_
  - K4-TLM carries saturation-bounded impedance $Z(V)$ (via Axiom 4) but no wave-speed modulation; without slowing at the saturation core, modes propagate rather than localize.
  - Master Equation FDTD's non-linear d'Alembertian carries $c_{eff}(V) = c_0\sqrt{S(A)}$; the wave slows at the saturation core and localizes into a stable breathing soliton.
  - The "Mode III at the Golden Torus" K4-TLM result is therefore an engine-architecture mismatch (wrong tool for a bound state), not a falsification of the framework.
- _Specific Non-Claims and Caveats_
  - Does NOT claim $c_{eff}(V)$ modulation is the only conceivable localization mechanism in general; the claim is specific to the AVE substrate's non-linear d'Alembertian and its two engines.
  - Does NOT independently re-derive, from the four axioms, that bound states require a refractive-index well — it is read off the engine behaviour and the d'Alembertian form.
  - The reclassification of "Mode III" from framework failure to engine mismatch is a methodological correction; the underlying simulation outputs are unchanged.

> **Leaf references:** `two-engine-architecture-a027.md` §Why two engines, §What was superseded.

### Quality
- confidence: *pending*
- solidity: *pending*
- rationale: *pending — L3-migration port; quality scored at the rescore pass*
- strengthen-by:
  - *pending*

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

> **Leaf references:** `two-engine-architecture-a027.md` §Two-engine convergence example; `q-g47-substrate-scale-cosserat-closure.md` §Status (two-engine convergence on p* = 8πα, cited from this leaf).

### Quality
- confidence: *pending*
- depends-on:
  - clm-0ktpcn — Golden Torus α Derivation [both convergence routes bottleneck on α]
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending — L3-migration port; quality scored at the rescore pass*
- strengthen-by:
  - *pending*

---

## Three-Route Framework: α, G, and J_cosmic from a Single Ω_freeze
<!-- id: clm-dsb560 -->

The framework's sharpest empirical commitment: the fine-structure constant α, Newton's gravitational constant G, and the cosmic-boundary winding number J_cosmic all derive from a single cosmological initial-condition parameter Ω_freeze, via the substrate's magic-angle operating point u₀* ≈ 0.187.

- _Specific Claims_
  - Three observational routes each independently fix u₀*: Route 1 (electromagnetic) — CODATA α to 12 decimals → u₀* via the Vol 1 Ch 8 Q-factor closure $\alpha^{-1} = 4\pi^3 + \pi^2 + \pi$; Route 2 (gravitational) — CODATA G to ~4 decimals → u₀* via the Machian impedance integral $G = c^4/(7\xi T_{EM}(u_0^*))$; Route 3 (cosmological) — CMB/LSS anomaly measurements of J_cosmic → u₀* via $\Omega_{\text{freeze}} = \mathcal{J}_{\text{cosmic}}/I_{\text{cosmic}}$.
  - All three routes are required to converge on the same u₀* at the relevant precision; non-convergence falsifies the single-cosmological-parameter framework.
  - The framework collapses the historical "three calibration parameters" picture into "one cosmological initial condition with three observational windows."
- _Specific Non-Claims and Caveats_
  - Does NOT claim the three routes have been shown to converge at full precision — convergence is the stated falsifiable commitment, not a reported result.
  - Does NOT claim independent determination of α, G, or J_cosmic from the framework; each route maps an externally-measured constant onto u₀*.
  - The magic-angle value u₀* ≈ 0.187 is the substrate operating point (bond over-bracing at the K4 magic-angle $K(u_0^*) = 2G(u_0^*)$); its derivation context is the substrate-scale Cosserat-closure work, not this leaf.

> **Leaf references:** `omega-freeze-cosmic-grain-cascade.md` §1 (the three numbers Ω_freeze sets), Key Results table; `cosmic-parameter-horizon-a031-refinement.md` (three-route framework commitment, stated as a corollary).

### Quality
- confidence: *pending*
- solidity: *pending*
- rationale: *pending — L3-migration port; quality scored at the rescore pass*
- strengthen-by:
  - *pending*

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

> **Leaf references:** `omega-freeze-cosmic-grain-cascade.md` §2 (the mechanism, corpus-canonical).

### Quality
- confidence: *pending*
- solidity: *pending*
- rationale: *pending — L3-migration port; quality scored at the rescore pass*
- strengthen-by:
  - *pending*

---

## Eight Cosmic-Axis Observables Aligned with the Ω_freeze Axis
<!-- id: clm-pe8lpx -->

The framework predicts eight independent observable channels should all show a preferred axis aligned with the Ω_freeze axis at (l ≈ 174°, b ≈ −5°) in galactic coordinates.

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

> **Leaf references:** `omega-freeze-cosmic-grain-cascade.md` §3 (eight testable observables), §3.1, §3.3.

### Quality
- confidence: *pending*
- solidity: *pending*
- rationale: *pending — L3-migration port; quality scored at the rescore pass*
- strengthen-by:
  - *pending*

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

> **Leaf references:** `omega-freeze-cosmic-grain-cascade.md` §3.2 (Observable 7: G anisotropy via tensor extension).

### Quality
- confidence: *pending*
- solidity: *pending*
- rationale: *pending — L3-migration port; quality scored at the rescore pass*
- strengthen-by:
  - *pending*

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

> **Leaf references:** `cosmic-parameter-horizon-a031-refinement.md` §The refinement, §What remains observable for the cosmic instance.

### Quality
- confidence: *pending*
- solidity: *pending*
- rationale: *pending — L3-migration port; quality scored at the rescore pass*
- strengthen-by:
  - *pending*

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

> **Leaf references:** `boundary-observables-m-q-j.md` §The three invariants.

### Quality
- confidence: *pending*
- solidity: *pending*
- rationale: *pending — L3-migration port; quality scored at the rescore pass*
- strengthen-by:
  - *pending*

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

> **Leaf references:** `boundary-observables-m-q-j.md` §The substrate-observability rule, §Same mechanism at all scales.

### Quality
- confidence: *pending*
- solidity: *pending*
- rationale: *pending — L3-migration port; quality scored at the rescore pass*
- strengthen-by:
  - *pending*

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
  - The R·r = 1/4 normalization that makes Λ_vol evaluate to exactly 4π³ is inherited from the Vol 1 Ch 8 derivation (spin-½ half-cover of the standard Clifford torus), not derived here.

> **Leaf references:** `boundary-observables-m-q-j.md` §The fine-structure constant as electron-scale M+J+Q.

### Quality
- confidence: *pending*
- solidity: *pending*
- rationale: *pending — L3-migration port; quality scored at the rescore pass*
- strengthen-by:
  - *pending*

---

## Interior Eigenmodes of a Bounded Soliton Are Not Lattice-Nyquist-Constrained
<!-- id: clm-sjjvhf -->

An interior eigenmode of a soliton bounded by a Γ=−1 wall lives entirely inside that wall and is not subject to the K4 lattice Nyquist limit; the substrate-correct test of such a soliton measures integrated boundary observables, not propagating-mode wavenumbers.

- _Specific Claims_
  - Any interior Beltrami / phase-space eigenmode of a bounded soliton (e.g., the electron's horn-torus interior at k ≈ 6.36/ℓ_node) lives entirely inside the Γ=−1 wall and is causally disconnected from the exterior substrate.
  - The K4 Nyquist limit k_max = 0.577/ℓ_node does NOT apply to interior structure, because the substrate never propagates that wave through the lattice — it lives only in the bounded interior cell.
  - Forcing a multi-cell propagating-eigenmode test on a bounded interior is a category error; the substrate-correct test measures the integrated boundary observables M, Q, J.
- _Specific Non-Claims and Caveats_
  - Does NOT claim the interior wavenumber is unphysical — it is a real interior eigenmode; the claim is that it is exempt from the lattice Nyquist bound because it does not propagate through the lattice.
  - Applies specifically to structure interior to a Γ=−1 boundary; modes that do propagate through the K4 lattice remain Nyquist-constrained.

> **Leaf references:** `boundary-observables-m-q-j.md` §Implications: interior eigenmodes and "substrate compression".

### Quality
- confidence: *pending*
- solidity: *pending*
- rationale: *pending — L3-migration port; quality scored at the rescore pass*
- strengthen-by:
  - *pending*

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

> **Leaf references:** `boundary-observables-m-q-j.md` §Implications: interior eigenmodes and "substrate compression".

### Quality
- confidence: *pending*
- solidity: *pending*
- rationale: *pending — L3-migration port; quality scored at the rescore pass*
- strengthen-by:
  - *pending*

---

## Substrate-Native Lenz Back-EMF Freezes Topological ω at the Yield Crossing
<!-- id: clm-exjfai -->

When the Cosserat-sector voltage drops through V_yield slowly enough (crossing time ≥ τ_relax), a diverging effective inductance L_eff near S→0 generates a diverging Lenz back-EMF that freezes any topologically non-trivial ω configuration present at the crossing — derived from Axiom 1 + Op14 + Lenz, with no SM/QFT machinery.

- _Specific Claims_
  - When V(t) drops through V_yield in the Cosserat sector such that the crossing takes ≥ τ_relax, any topologically non-trivial ω configuration present at the start of the window FREEZES — it cannot unwind because the diverging L_eff (Op14 near S = 0) generates a diverging Lenz back-EMF that blocks dω/dt during the τ_relax window.
  - The frozen residues persist for ≥ 100 Compton periods in the post-heal solid regime.
  - This is the AVE-native mechanism for matter precipitation from cooling vacuum (cosmological lifecycle); it is derived from Axiom 1 (Substrate Topology) + Op14 + Lenz's law, NOT a Kibble-Zurek import.
- _Specific Non-Claims and Caveats_
  - Does NOT claim a closed-form derivation of τ_relax in this leaf; the τ_relax window is taken from the Op14 vacuum-circuit work.
  - The freeze applies in the slow-crossing regime (crossing ≥ τ_relax); the leaf does not characterize the fast-crossing regime.
  - The Op14 cross-sector-trading correlation ρ = −0.990 is an empirical-validation figure for the energy-trading mechanism; the freeze claim is the dynamical consequence at the yield crossing, not itself that correlation measurement.

> **Leaf references:** `dark-wake-bemf-foc-synthesis.md` §1.2 (Lenz back-EMF blocks dω/dt at yield crossing).

### Quality
- confidence: *pending*
- solidity: *pending*
- rationale: *pending — L3-migration port; quality scored at the rescore pass*
- strengthen-by:
  - *pending*

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

> **Leaf references:** `dark-wake-bemf-foc-synthesis.md` §2 (FOC d-q decomposition, with retraction caveat).

### Quality
- confidence: *pending*
- solidity: *pending*
- rationale: *pending — L3-migration port; quality scored at the rescore pass*
- strengthen-by:
  - *pending*

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
  - Does NOT claim the kernel form is verified at every one of the 21 scales to the same precision; per-scale empirical anchors vary in tightness (BCS at 0.00% error; BH ring-down at 1.7% from GR; several rows carry no quantitative anchor).
  - Born–Infeld $n = 2$ is the squared-limit form; the identification with the AVE saturation kernel is structural, not a derivation of Born–Infeld electrodynamics.

> **Leaf references:** `universal-saturation-kernel-catalog.md` §Key Result: 21 canonical instances of one kernel.

### Quality
- confidence: *pending*
- solidity: *pending*
- rationale: *pending — L3-migration port; quality scored at the rescore pass*
- strengthen-by:
  - *pending*

---

## A-034 Catalog — 21 Canonical Cross-Scale Instances
<!-- id: clm-dxdsvt -->

The A-034 catalog enumerates 21 canonical cross-scale instances of the saturation kernel, spanning 21 orders of magnitude: 14 physical-substrate, 2 biological-substrate, and 5 engineered-substrate instances.

- _Specific Claims_
  - 21 canonical instances are catalogued, spanning ~21 orders of magnitude from atomic ($\sim 10^{-15}$ m) to cosmic ($\sim 10^{26}$ m) scale.
  - The 21 split into 14 physical-substrate instances (atomic/EM, K4 substrate, DT fusion, Pd hydrogen-loading shatter, BCS, water two-state LC partition, plasma, Kolmogorov turbulence, geomagnetic, solar flare, MOND, BH event horizon, BH ring-down, Big Bang), 2 biological-substrate instances (lipid bilayer, protein folding), and 5 engineered-substrate instances (DC-biased piezoelectric, asymmetric-electrode vacuum-mirror bench, active topological metamaterials, sine-Gordon kink memory, autoresonant rupture).
  - Each instance has a defined $A$ ratio and a saturation event; the catalog records empirical anchors where they exist (BCS $B_c(T)$ at 0.00% error; BH ring-down 1.7% from GR; NOAA GOES 40-yr solar flares; Schwarzschild exact; Nilsson 2026 X-ray LLCP for water).
- _Specific Non-Claims and Caveats_
  - The 21 instances are NOT 21 claims of this leaf; per-instance physics is owned by the respective per-instance leaves elsewhere in the KB. This entry asserts the catalog's membership and cross-scale span, not each instance's individual derivation.
  - Catalog count is as of the 2026-05-16 growth notes (water added as 13th, Pd hydrogen-loading shatter as 14th physical instance); the catalog is explicitly described as growing as evidence accumulates.
  - Several rows carry no quantitative empirical anchor (e.g., "plasma canonical", "substrate instance"); for those the instance is a structural classification, not a validated measurement.
  - LLM SiLU activation saturation is explicitly kept OUT of the 21: same kernel form but applied in activation space during neural-net training, tracked as a parallel thread.

> **Leaf references:** `universal-saturation-kernel-catalog.md` §The 21-instance catalog.

### Quality
- confidence: *pending*
- solidity: *pending*
- rationale: *pending — L3-migration port; quality scored at the rescore pass*
- strengthen-by:
  - *pending*

---

## A-034 Symmetry Classification — SYM / ASYM-N / ASYM-E
<!-- id: clm-hvvvop -->

The 21 A-034 instances admit a 3-way symmetry classification by how the $\varepsilon$ and $\mu$ sectors saturate: SYM (18 instances), ASYM-N (2), ASYM-E (1).

- _Specific Claims_
  - SYM (Symmetric) — vacuum $K = 2G$; $\varepsilon$ and $\mu$ saturate together: 18 instances.
  - ASYM-N (Asymmetric natural) — single-sector saturation (only $\varepsilon$ or only $\mu$): 2 instances — BCS ($\mu$-only) and plasma ($\varepsilon$-only).
  - ASYM-E (Asymmetric engineered) — decoupled $K/G \neq 2$ by design: 1 instance — active topological metamaterials.
  - The three classes partition all 21 instances (18 + 2 + 1 = 21).
- _Specific Non-Claims and Caveats_
  - The asymmetric-saturation variant ($K_{\text{wedge}}/G_{\text{wedge}} \neq 2$) is flagged as a novel kernel topology for separate framework exploration; it is not claimed to be fully developed here.
  - Does NOT claim the ASYM-N / ASYM-E classifications are independently empirically validated as asymmetric; they are structural classifications based on which sector(s) saturate.
  - The classification count tracks the catalog count; if the catalog grows, the per-class counts may change.

> **Leaf references:** `universal-saturation-kernel-catalog.md` §Symmetry classification.

### Quality
- confidence: *pending*
- solidity: *pending*
- rationale: *pending — L3-migration port; quality scored at the rescore pass*
- strengthen-by:
  - *pending*

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

> **Leaf references:** `universal-saturation-kernel-catalog.md` §Cosmic-scale instance (Big Bang as A-034).

### Quality
- confidence: *pending*
- solidity: *pending*
- rationale: *pending — L3-migration port; quality scored at the rescore pass*
- strengthen-by:
  - *pending*

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

> **Leaf references:** `operators.md` §2 Canonical 22-operator catalog (Vol 1 Ch 6 anchor).

### Quality
- confidence: *pending*
- solidity: *pending*
- rationale: *pending — L3-migration port; quality scored at the rescore pass*
- strengthen-by:
  - *pending*

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

> **Leaf references:** `operators.md` §4 Scale-invariance argument (summary).

### Quality
- confidence: *pending*
- solidity: *pending*
- rationale: *pending — L3-migration port; quality scored at the rescore pass*
- strengthen-by:
  - *pending*

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
  - The closure is described as "structural" — the magic-angle equation is explicit and $u_0^* \approx 0.187$ is established, but the individual Cosserat prefactors are not yet derived (see clm-bjceop).
  - $\nu_{\text{vac}} = 2/7$ being load-bearing for $\sin^2\theta_W = 2/9$ and other downstream results is noted as a dependency direction, not derived here.

> **Leaf references:** `q-g47-substrate-scale-cosserat-closure.md` §The magic-angle condition.

### Quality
- confidence: *pending*
- solidity: *pending*
- rationale: *pending — L3-migration port; quality scored at the rescore pass*
- strengthen-by:
  - *pending*

---

## |T| = 12 Universality — Four Independent K4 Routes Force χ_K = 12
<!-- id: clm-qwmnhn -->

The tetrahedral rotation group order $|T| = 12$ appears in K4 physics via four independent routes, all converging on 12 — making $\chi_K = 12$ structurally forced by K4 symmetry rather than a fitted parameter.

- _Specific Claims_
  - The proper tetrahedral rotation group $T$ has order $|T| = 12$.
  - Route 1 (baseline coordination): K4 path-count geometry — 4 B-neighbors × 3 other-A sublattices = 12 secondary paths per node.
  - Route 2 (Cosserat dimensional): $(\ell_c/d)^2 \times 2 = 12$ (Cosserat characteristic length squared × bilateral factor).
  - Route 3 (magic-angle unity): $f_{\text{Cosserat}}(u_0^*) = 1$ at the substrate saturation boundary, an orbit-count multiplicity of 12.
  - Route 4 (axiom-level constitutive ratio): $\xi_{K2}/\xi_{K1} = 12$, the K4-symmetry-forced ratio of substrate-scale Cosserat prefactors.
  - Four independent calculations converging on the same integer is strong evidence that $\chi_K = 12$ is structurally forced by K4 symmetry, not a calibration coincidence.
- _Specific Non-Claims and Caveats_
  - The four routes are described as "strong evidence" that 12 is structurally forced — convergence, not a single first-principles proof.
  - Route 4 ($\xi_{K2}/\xi_{K1} = 12$) is itself a self-consistency result (see clm-bjceop); it fixes the ratio, not the individual prefactors.
  - The claim replaces "12 as a fit parameter" with "12 as the tetrahedral rotation group order" — it does not independently derive every downstream use of 12.

> **Leaf references:** `q-g47-substrate-scale-cosserat-closure.md` §|T| = 12 universality: four independent routes converge.

### Quality
- confidence: *pending*
- solidity: *pending*
- rationale: *pending — L3-migration port; quality scored at the rescore pass*
- strengthen-by:
  - *pending*

---

## Substrate-Scale Cosserat Prefactors — μ+κ, β+γ and the Forced ξ_K2/ξ_K1 = 12
<!-- id: clm-bjceop -->

The substrate's continuous Cosserat micropolar constitutive constants satisfy $\mu+\kappa = \xi_{K1}\cdot T_{EM}$ and $\beta+\gamma = \xi_{K2}\cdot T_{EM}\cdot\ell_{\text{node}}^2$; self-consistency forces $\xi_{K2}/\xi_{K1} = 12$, independent of $T_{EM}$.

- _Specific Claims_
  - The substrate's continuous Cosserat micropolar field has constitutive constants $(\mu, \kappa, \beta, \gamma)$ at the axiom level.
  - Q-G47 Sessions 16–17 closed the dimensional framework: $\mu + \kappa = \xi_{K1}\cdot T_{EM}$ and $\beta + \gamma = \xi_{K2}\cdot T_{EM}\cdot\ell_{\text{node}}^2$, with $T_{EM}$ the lattice's electromagnetic string tension and $\ell_{\text{node}}$ the lattice pitch.
  - Self-consistency forces $\xi_{K2}/\xi_{K1} = 12$; the ratio is independent of $T_{EM}$ and is purely K4-symmetry-forced (the same route 4 of the $|T|=12$ universality).
- _Specific Non-Claims and Caveats_
  - Only the ratio $\xi_{K2}/\xi_{K1} = 12$ is fixed; the individual prefactors $\xi_{K1}, \xi_{K2}$ are explicitly STILL OPEN — their first-principles computation from K4 unit-cell Cosserat-Lagrangian integration is flagged as multi-week analytical work not yet done.
  - The substrate-scale prefactors $\xi_{K1}, \xi_{K2}$ are a distinct namespace from the Machian $\xi \sim 10^{38}$ (cosmic-scale impedance integral) and from $\xi_{\text{topo}} = e/\ell_{\text{node}}$ (charge-displacement conversion); the three-way de-collision is owned by `xi-topo-traceability.md` and cross-referenced, not re-derived here.
  - The dimensional framework is "closed" in the sense of being dimensionally consistent and fixing the ratio; it is not a complete derivation of the constitutive tensor.

> **Leaf references:** `q-g47-substrate-scale-cosserat-closure.md` §Substrate-scale Cosserat prefactors ξ_K1, ξ_K2.

### Quality
- confidence: *pending*
- solidity: *pending*
- rationale: *pending — L3-migration port; quality scored at the rescore pass*
- strengthen-by:
  - *pending*
