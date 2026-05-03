# Common (Cross-Volume Resources) — Claim Boundaries

<!-- path-stable: referenced from CLAUDE.md INVARIANT-S7 and from common/index.md bootstrap directive -->

> **Canonicality:** Leaves are canonical; this directory's indexes are derived summaries. See [cross-cutting boundaries](../claims-boundaries.md) for the full preamble and the canonical list of project-wide tripwires (the cross-cutting sidecar is the source of truth for which tripwires are project-wide; do not infer the list from this preamble). Entries below are scoped to the common/ directory's substantive content (mathematical closure status, derivation chain, falsification index, translation tables, solver toolchain).

---

## Mathematical Closure Status — "Structurally Zero-Parameter," Not Absolutely

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

---

## Full Derivation Chain — Acyclicity and Identified Methodology Disclosures

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

---

## Experimental Falsification Index — Catalog Status, Not Validation Status

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

---

## Universal Solver Toolchain — Operator Reuse, Not Per-Domain Derivation

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
  - The "BH transistor datasheet" and "semiconductor junction analogy" tables are presented as systematic parameter-extraction templates; rows like Hawking temperature inherit the cross-cutting Hawking caveat (alternative mechanism, same value — see [`vol3/claims-boundaries.md`](../vol3/claims-boundaries.md) Hawking Temperature entry).
  - The torus knot ladder $c = 3$ trefoil entry (637 MeV) is **not** the electron — the electron is the unknot $0_1$. The leaf flags this. Summaries that read the ladder as "electron at $c = 3$" misread the leaf.

> **Leaf references:** `solver-toolchain.md` §Regime-Boundary Eigenvalue Method, §Protein Backbone Eigenvalue, §Nuclear Eigenvalue, §Cross-Scale Isomorphism Table; cross-cutting Symmetric vs Asymmetric Saturation in [`../claims-boundaries.md`](../claims-boundaries.md); BH-specific tripwires in [`vol3/claims-boundaries.md`](../vol3/claims-boundaries.md).

---

## Translation Tables — Notation Mappings, Not Physical Equivalences

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

---

## $\xi_{topo}$ Traceability — Conversion Constant, Not Free Parameter

The Topological Conversion Constant $\xi_{topo} = e/\ell_{node} \approx 4.149 \times 10^{-7}$ C/m bridges 51 files across 6 of 8 volumes. Its boundary is dimensional currency exchange, not an independent physical degree of freedom.

- _Specific Claims_
  - $\xi_{topo}$ is defined by Axiom 2 from the topo-kinematic isomorphism $[Q] \equiv [L]$; given $\ell_{node}$ and $e$, it has no free parameter.
  - It is the dimensional bridge for: $Q = \xi x$, $I = \xi v$, $V = \xi^{-1} F$, $L = \xi^{-2} m$, $C = \xi^2 \kappa$, $R = \xi^{-2} \eta$. Same identity used in the circuit translation table and the biology translation table.
  - $\xi_{topo}$ is **distinct from $\xi$** (the dimensionless Machian hierarchy coupling, $\approx 8.15 \times 10^{43}$, used in Axiom 3's $G$ formula). The two share a Greek letter and are conflated in summaries; the leaf and CLAUDE.md Axiom 3 entry both flag this explicitly.
  - The "currency exchange" framing (Dirac large-numbers table) classifies $c$, $\hbar$, $e$, $\xi_{topo}$, $\ell_{node}$, $G$ as dimensional conversion factors rather than independent physical constants. This is a structural interpretive statement, not a falsifiable prediction.
- _Specific Non-Claims and Caveats_
  - Does NOT claim $\xi_{topo}$ has independent experimental status. It is fixed by Axiom 2 and the input scale; its appearance across 51 files is structural reuse, not 51 independent confirmations.
  - The "0 explicit files" entries for Vol 3 and Vol 6 do NOT mean $\xi_{topo}$ is unused there — it operates implicitly via derived quantities ($V_{yield}$, $Z_0$, $a_0$ in Vol 3; coupling $K$ in Vol 6). The traceability count is for explicit textual references, not for derivational dependence.
  - The Vol 7 and Vol 8 entries point to *experimental* private repositories (AVE-Propulsion, AVE-Virtual-Media). Public-KB readers cannot follow those links; treat them as scope boundaries, not as published results.
  - The "Zero-Free-Parameter Chain" diagram routes through the Golden Torus closure of $\alpha$ — and is therefore conditional on the same Layer-8 thermal closure of $\delta_{strain}$ at $T_{CMB}$ that the Mathematical Closure entry above bounds. The leaf carries this conditional statement; the chain is not unconditionally zero-parameter.

> **Leaf references:** `xi-topo-traceability.md` §Physical Meaning, §Coverage Summary, §Zero-Free-Parameter Chain; ξ vs ξ_topo distinction at [CLAUDE.md INVARIANT-C2](../CLAUDE.md#invariant-c2-electromechanical-transduction-constant) and [LIVING_REFERENCE.md](../../../LIVING_REFERENCE.md) Axiom 3 entry.

---

## Derived Numerology Appendix — Derivation Trace, Not Empirical Coincidence

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

---

## Appendices Overview — Theoretical Stress Tests, Not Independent Proofs

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

> **Leaf references:** `appendices-overview.md` §Theoretical Stress Tests, §Summary of Exact Analytical Derivations, §Computational Graph Architecture; MOND entry at [`vol3/claims-boundaries.md`](../vol3/claims-boundaries.md).

---

## SPICE Verification Manual — Toolchain Status, Not Validation Claim

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
