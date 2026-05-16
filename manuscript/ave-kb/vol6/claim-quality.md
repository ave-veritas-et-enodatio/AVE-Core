# Vol 6 — Periodic Table of Knots — Claim Quality

<!-- path-stable: referenced from CLAUDE.md INVARIANT-S7 and from vol6/index.md bootstrap directive -->

> **Canonicality:** Leaves are canonical; this volume's indexes are derived summaries. See [cross-cutting claim-quality register](../claim-quality.md) for the full preamble and the canonical list of project-wide tripwires (the cross-cutting sidecar is the source of truth for which tripwires are project-wide; do not infer the list from this preamble). Entries below are scoped to Vol 6; cross-cutting tripwires with vol6-specific manifestations are noted but not duplicated.

---

## Mass-Defect Accuracy: Fitted Geometry, Not Ab-Initio Mass Prediction
<!-- id: clm-llqd1n -->

The vol6 index, framework summary, and per-element leaves report mass-defect errors of $0.00001\%$ (H-1) to $0.02739\%$ (Mg-24) across $Z=1$–$14$, with several entries marked $0.0000\%$. These figures read like ab-initio predictions but are **fit residuals** under a one-parameter-per-nucleus geometry fit.

- $M_{\text{nucleus}} = N_\alpha M_\alpha - \sum K/r_{ij} + M \cdot \sum f_{pp}\,\alpha\hbar c/r_{ij}$
- _Specific Claims_
  - The axiom-derived constants ($K \approx 11.337$ MeV·fm, $d = 4\hbar/(m_p c) \approx 0.841$ fm, $D_{\text{intra}} = d\sqrt{8} \approx 2.379$ fm, $V_{BR} = 6\alpha\hbar c/D_{\text{intra}} \approx 3.631$ MeV, Miller exponent $n = c_{\text{proton}} = 5$) carry **zero empirical fit**. They derive from Axioms 1 and 2 plus the cinquefoil $(2,5)$ knot crossing count.
  - For each nucleus, the $\alpha$-cluster topology is **forced by $(Z, A)$**, and a single scalar $R$ (inter-alpha distance) is adjusted so the computed $\sum K/r_{ij}$ recovers the observed CODATA mass.
  - The substantive axiomatic claim is that **one scalar parameter per nucleus, constrained by topology, suffices** — not that the absolute mass is predicted ab initio.
  - Two genuine zero-parameter exceptions exist: He-4 (no inter-alpha distance — single tank) and the closed-shell symmetric geometries where $R$ snaps to the unique impedance-matched Platonic/Archimedean vertex set (the $0.000\,000\%$ "exact" entries in C-12, O-16, Ne-20, Mg-24, Si-28 are stated by the leaves; the Platonic Progression table reports $0.000\,000\%$ for these). Even here the $R$-value is what is solved; the topology is the prediction.
- _Specific Non-Claims and Caveats_
  - Does NOT claim the $0.00001\%$–$0.03\%$ figures are ab-initio mass predictions. They are **fitting tolerances**: a measure of how tightly a one-parameter geometric compression reproduces the target mass given the topology and $K$. The semiconductor-nuclear-analysis leaf flags this explicitly with a methodology note; the Macroscopic Mass Defect Summary table does not, and a reader of the summary alone may misread the numbers.
  - Does NOT claim the **topology** $(N_\alpha, \text{geometry})$ is derived independently of empirical input for every element. Period 1–3 topologies (Tetrahedron, Ring, Tetrahedron of $\alpha$, Bipyramid, Octahedron, Pentagonal Bipyramid) are the unique minimum-impedance packings for those $N_\alpha$ counts; the engine identifies them rather than fitting them — but the *assignment* of cluster count to element relies on the empirical $(Z, A)$.
  - Does NOT claim the framework predicts which isotope is stable. Stability arguments (e.g., F-19 as the unique stable Fluorine isotope, $^9$Be margin) are *post-hoc* structural rationalizations of empirical isotope ratios, not novel predictions of binding-energy minima.
  - The Master Prediction Table classification framework (cross-cutting) applies row-by-row. The $0.000\%$ entries here are a mix of geometric-identity (Platonic packing) and one-parameter fit; do not collapse them under a global "AVE achieves $0.0000\%$ on N nuclei" headline.

> **References:** `framework/computational-mass-defect/semiconductor-nuclear-analysis.md` (methodology note explicitly flags fit-vs-prediction); `framework/mass-defect-summary.md` (the table that omits the qualifier); `framework/computational-mass-defect/mutual-coupling-constant.md` (zero-parameter $K$ derivation); `framework/computational-mass-defect/nucleon-spacing-derivation.md` (zero-parameter $d$, $D_{\text{intra}}$); `appendix/geometric-inevitability/platonic-progression.md`.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Mutual Coupling Constant $K \approx 11.337$ MeV·fm — Derived but Path-Dependent
<!-- id: clm-lqanmt -->

- $K = (5\pi/2) \cdot \alpha\hbar c / (1 - \alpha/3) \approx 11.337$ MeV·fm
- _Specific Claims_
  - $K$ is built from three already-derived quantities: the cinquefoil crossing number $c_{\text{proton}} = 5$ (Axiom 2 / vol2 torus-knot identification of the proton as $(2,5)$), the per-crossing $\pi/2$ flux-linkage phase, and the Coulomb constant $\alpha\hbar c$.
  - The $1/(1 - \alpha/3)$ proximity-correction factor is a first-order radiative enhancement; $\alpha/3$ is identified as the isotropic 3D spatial average of the EM vertex correction.
  - When applied to the He-4 alpha (6 pairs at uniform $D_{\text{intra}}$), $K$ recovers the empirical mass to $\sim 0.001\%$ — a category (iv) zero-parameter prediction at this single point.
- _Specific Non-Claims and Caveats_
  - The proximity-correction form $1/(1 - \alpha/3)$ is asserted by analogy to EE transformer proximity effects and the isotropic 3D spatial averaging argument. The leaf does not derive the specific $\alpha/3$ geometry from first principles within the leaf itself — it is presented as a structural identification.
  - Does NOT claim $K$ is an independent input. Treat the $K = 11.337$ MeV·fm value as **derived from the assembled three-factor expression**; alternative groupings of the same three factors (different per-crossing phase, different proximity correction) would yield different $K$ values, and the chain is structurally argued rather than first-principles-rigorous in the leaf.
  - The He-4 mass match at $0.001\%$ is a single-point validation; the same $K$ is then **applied** to all heavier nuclei where the inter-alpha distance $R$ becomes the per-nucleus fit parameter (see "Mass-Defect Accuracy" entry above).

> **Leaf references:** `framework/computational-mass-defect/mutual-coupling-constant.md`; `framework/computational-mass-defect/nucleon-spacing-derivation.md`. Cross-volume: vol2 torus-knot identification of the proton as $(2,5)$ cinquefoil ($c=5$).

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Period 1–3 Per-Element IE Accuracy and Correction Stack
<!-- id: clm-7tk051 -->

The atomic ionization solver `radial_eigenvalue.py` computes first IEs for $Z=1$–$14$ with three corrections (A: hierarchical cascade for Be-type; B: SIR boundary for Mg-type; C: Op10 junction projection for Al/Si-type co-resonant shells) and for $Z=31$–$36$ with Correction D (Topo-Kinematic Polar Conjugate Mirror).

- _Specific Claims_
  - Solver validated $Z=1$–$14$ at $\le 2.80\%$ max residual (Boron, $-2.80\%$); most entries within $\pm 1.5\%$. Zero free parameters across the suite — corrections are operator chains gated by shell structure, not fit constants.
  - Corrections are **mutually exclusive by structural gates**: Correction A fires only for $n_{\text{adjacent}} = 1$ (pure $s$-shell inner core); Correction B fires for $n_{\text{adjacent}} \ge 2$ AND nesting ratio $n_{\text{out}}^2/n_{\text{inner}}^2 \ge 4$; Correction C fires for $l_{\text{out}} > 0$ AND nesting ratio $< 4$; Correction D fires for $Z \ge 31$ with appropriate enclosed $d^{10}$ shells.
  - The B/C/D corrections all derive from the same operator stack (Op3 reflection at impedance step → Malus's-law angle → Op10 junction projection or polar-conjugate TIR mirror); same scale-invariant operators that appear in protein backbone bend loss (Op10) and nuclear hierarchical binding (Correction A analog).
- _Specific Non-Claims and Caveats_
  - Does NOT claim the solver uses the Bohr / Schrödinger formula $E = Z_{\text{eff}}^2 \mathrm{Ry}/n^2$. LIVING_REFERENCE.md Pitfall #8 is a project-wide tripwire: any AVE-labeled IE derivation that uses the Bohr formula is QM contamination; `radial_eigenvalue.py` uses ODE cavity eigenvalues + Hopf mode splitting + crossing scattering. Reviewers should reject any sidecar reading or summary that recasts these IEs as Bohr-formula outputs.
  - Does NOT claim the solver uses ad-hoc electron-electron formulas. LIVING_REFERENCE.md Pitfall #9 (Op4 Bypass) is the cross-cutting tripwire: $V_{ee}$ MUST come from Op4 ($U = -K/r_{12}(T^2 - \Gamma^2)$), not a $J \times Z \times \mathrm{Ry}$ shortcut.
  - Does NOT claim the smooth hydrogenic CDF applies to Pauli-saturated inner shells. LIVING_REFERENCE.md Pitfall #11 is the project-wide bound: a saturated inner torus creates a discrete impedance step the smooth CDF misses; SIR boundary correction (Correction B) is mandatory for shells with $p$-subshells. Treating the smooth CDF as universal across Period 3 is an error.
  - Does NOT claim the solver is a Hartree-Fock SCF method. LIVING_REFERENCE.md Pitfall #7 is project-wide: SCF $\ne$ AVE; "iterative SCF for $Z \ge 26$" is QM not AVE. Vol 6's IE coverage stops at $Z=14$ for the main p/s-block + $Z=31$–$36$ for Period 4 $d^{10}$-enclosed elements; broader Period 4 nuclear binding for $Z \ge 26$ uses the **coupled resonator** (`coupled_resonator.py`), not SCF.
  - Does NOT claim de Broglie dispersion is a medium impedance. LIVING_REFERENCE.md Pitfall #10 is project-wide: $n_{\text{dB}}(r)$ is the defect's dispersion; lattice impedance is $Z_0 = 377\,\Omega$ in Regime I. Reviewers should reject readings that conflate these in vol6 chapters.
  - The B-Boron $-2.80\%$ residual is the largest in the $Z=1$–$14$ sweep. The leaf does not flag a known correction; treat as the current accuracy floor for the unaugmented Phase A→B→C pipeline.

> **References:** `framework/ionization-energy-summary.md` (full table, $Z=1$–$14$ and $Z=31$–$36$); `period-2/beryllium/ionization-energy-correction.md` (A); `period-3/magnesium/ionization-energy-correction.md` (B); `period-3/aluminum/ionization-energy-correction.md`, `period-3/silicon/ionization-energy-correction.md` (C); `framework/polar-conjugate-bounding.md` (D). Cross-cutting: LIVING_REFERENCE.md Common Pitfalls #7, #8, #9, #10, #11; "4. Axioms in the Atomic Domain" Corrections A–D.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Heavy Element Catalog ($Z=15$–$119$): Accuracy Tiers, Not a Uniform Bound
<!-- id: clm-nk6c43 -->

The catalog reports masses for $Z=15$ through $Z=119$ in a single table; the index summarizes "Fibonacci proxy accuracy $< 0.5\%$ across 105 elements." The actual error distribution is tiered and the entries are not all the same kind of result.

- _Specific Claims_
  - **Tier A (exact analytical, $0.000\%$):** S-32 and Ca-40 — Large Signal closed avalanche solutions ($M = 32.8$ and $32.9$ respectively, $V_R/V_{BR} = 0.994$). Treated as zero-parameter Large-Signal solutions in the leaves.
  - **Tier B (near-exact Platonic/Archimedean, $\le 0.0002\%$):** Ar-40 (Bicapped Antiprism), Ti-48 (Cuboctahedron), Cr-52 (Centered Icosahedron), Fe-56 (FCC-14). Geometry forced by minimum-impedance packing.
  - **Tier C (Fibonacci-proxy, typically $< 0.5\%$):** All other entries $Z=15$–$119$. The Fibonacci lattice is a numerical proxy that approximates icosahedral / minimum-impedance distribution on $S^2$.
  - The Cr-52 centered-icosahedron solution is the load-bearing case for the Golden Ratio claim: $\varphi$ is **forced by** the unique Thomson-problem solution at $N=12$, not chosen.
- _Specific Non-Claims and Caveats_
  - Does NOT claim "$< 0.5\%$ across 105 elements" is a uniform predictive accuracy. Individual-element errors range from $0.000\%$ (Tier A) up to $1.465\%$ (Cl-35, in the table) and $0.898\%$ (Zn-65) and $0.849\%$ (Rb-85). The "$< 0.5\%$" headline is a **typical**, not a maximum. Several Tier-C entries exceed it.
  - Does NOT claim Tier-C masses are ab-initio predictions. The leaves identify the Fibonacci packing as a **proxy** ("the Fibonacci lattice works *because* it approximates the true minimum-impedance geometry") and the catalog regimes carry residual errors pending re-solution with the resolved geometry.
  - Does NOT claim the topology assignments for $Z \ge 28$ are first-principles-derived in vol6. The mass-prediction-accuracy leaf calls Tier C "Fibonacci lattice packing as a geometric proxy"; the abcd-transfer-matrix leaf (`abcd-transfer-matrix.md`) explicitly states the port-connected network topology for $Z \ge 15$ is the **key open problem** — the current heavy-element predictions use sphere packing rather than the deterministic ABCD cascade.
  - The Large-Signal $0.000\%$ for S-32 and Ca-40 is one specific instance of the cross-cutting Master-Prediction-Table tripwire: "$0.000\%$" entries are not all the same category. These two are zero-parameter Large-Signal closures (closer to category iv "derived prediction" given the avalanche $M$ also derives from $c_{\text{proton}} = 5$); Ar-40 / Ti-48 / Cr-52 / Fe-56 are geometric-identity packing solutions; Tier-C entries are proxy fits. Do not present a global "AVE achieves $< 0.5\%$ across $Z=15$–$119$" claim without per-tier breakout.

> **Leaf references:** `appendix/heavy-element-catalog/full-element-table.md`; `appendix/heavy-element-catalog/mass-prediction-accuracy.md`; `appendix/heavy-element-catalog/selected-heavy-orbital-topology.md` (Tier-A/B per-element soliton placements); `appendix/heavy-element-catalog/index.md`; `appendix/geometric-inevitability/fibonacci-packing-proxy.md`; `appendix/geometric-inevitability/platonic-progression.md`; `framework/computational-mass-defect/abcd-transfer-matrix.md` (ABCD cascade as the open problem). Cross-cutting: Master Prediction Table reading conventions in `../claim-quality.md`.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Topological Horizon at Boron-11 ($R = 4\pi - \sqrt{2}/2 \approx 11.86\,d$)
<!-- id: clm-l416hl -->

- $\text{Horizon}_{\text{limit}} = 4\pi - \sqrt{2}/2 \approx 11.859$; $R_{\text{halo}}(^{11}\text{B}) = 11.8404\,d$
- _Specific Claims_
  - Solver places the Boron-11 7-nucleon halo at $R_{\text{halo}} = 11.84\,d$ when constrained to recover the CODATA mass of $10252.548$ MeV.
  - The proximity to $4\pi - \sqrt{2}/2$ is interpreted as Boron-11 sitting at the **Topological Horizon** — the maximum reactive coherence radius before the halo decouples.
  - The $4\pi$ factor is identified as the total isotropic solid angle of a sphere (Gauss's law over a complete spherical surface), not numerology. The $-\sqrt{2}/2$ subtraction is the leaf's identified subleading correction (interpreted via the Pythagorean unit-cube diagonal half).
- _Specific Non-Claims and Caveats_
  - Does NOT claim a first-principles derivation of $-\sqrt{2}/2$ as the unique subleading correction. The $4\pi$ piece is rigorously Gauss-law; the $-\sqrt{2}/2$ piece is asserted as the structural bounding term but is not derived in the leaf with the same rigor. Treat the **proximity** of $R_{\text{halo}}$ to $\text{Horizon}_{\text{limit}}$ as the structural claim; the **exact form** $4\pi - \sqrt{2}/2$ is the leaf's identification, not a separately validated formula.
  - Does NOT claim $R_{\text{halo}}$ is a first-principles output. It is the per-nucleus fit parameter for $^{11}$B (see "Mass-Defect Accuracy" entry); the substantive claim is that the fit value lands at the Horizon limit, which the framework calls **structural** rather than coincidental.
  - The Horizon limit applies to halo nucleons around a single saturated alpha core; does NOT claim a universal $4\pi - \sqrt{2}/2$ bound for any reactive-coherence radius across vol6 elements. Other halo distances (F-19 at $398d$, Na-23 at $50d$, Al-27 at $52.6d$) operate under different core-density regimes and are not bounded by this same formula.

> **Leaf references:** `period-2/boron/structure-isotope-stability.md`; `appendix/geometric-inevitability/pi-topological-horizon.md`.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Topology-Determined Halo Distance: Structure, Not Curve Fit
<!-- id: clm-8psuqe -->

The optimizer outputs strikingly different $R_{\text{halo}}$ values for the same Tritium halo across cores: F-19 at $\sim 398d$, Na-23 at $\sim 50d$, Al-27 at $\sim 53d$. The vol6 narrative argues this proves the framework is not curve-fitting because the variation predicts the observed chemistry (Halogen vs Alkali vs post-transition metal).

- _Specific Claims_
  - Same structural-element (Tritium $^3\mathrm{H} = 1p+2n$) halo, different optimal radii, different chemistry — and the **direction** of the variation matches the empirical electronegativity ordering.
  - The framework's claim is that the **mechanical asymmetry** (long lever arm vs short bulge) IS the chemical electronegativity, not an interpretive overlay.
- _Specific Non-Claims and Caveats_
  - Does NOT claim the absolute $R_{\text{halo}}$ values are independently derived; each is the per-nucleus fit parameter that recovers the CODATA mass under the assumed core+halo topology. The substantive claim is qualitative: large $R$ for Halogen, small $R$ for Alkali, intermediate $R$ for post-transition metal.
  - Does NOT claim quantitative electronegativity values ($\chi$ on the Pauling or Mulliken scale) are predicted from $R_{\text{halo}}$. The mapping $R_{\text{halo}} \to \chi$ is structural ("long lever = receiver, short lever = donor"), not a numerical correlation.
  - Does NOT claim the same argument extends parameter-free to all heavy halogens / alkali metals. The argument is strongest for the F/Na pair (same Tritium halo, opposite core scale); extrapolating to Cl/K, Br/Rb, etc., requires the corresponding core+halo topology assignments, which for $Z \ge 17$ are in the Tier-C Fibonacci-proxy regime.
  - The Neon "curve-fitting fallacy" leaf is an **interpretive defense**, not an independent validation; it argues *why* the variation is meaningful but does not constitute a separate empirical test.

> **Leaf references:** `period-2/neon/curve-fitting-fallacy.md`; `period-2/fluorine/structure-isotope-stability.md`; `period-3/sodium/core-proximity-effect.md`; `period-3/aluminum/gradual-halo-separation.md`.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Magic Numbers as Geometric Closure (Partial Coverage)
<!-- id: clm-sjixaw -->

- _Specific Claims_
  - The first four nuclear magic numbers ($Z = 2, 8, 20, 28$) are identified with closed Platonic / Archimedean alpha-cluster packings: Single Tank, Tetrahedron, Bicapped Antiprism, FCC-14 respectively.
  - The mechanism is impedance matching ($S_{11} \to 0$, maximum Q-factor) when every alpha cluster is symmetrically equivalent and the strain field has zero net dipole moment.
  - This is a category (iii)/(iv) hybrid: reproduces the empirical magic-number sequence via an alternative mechanism (geometric closure rather than spin-orbit shell-model coupling).
- _Specific Non-Claims and Caveats_
  - Vol 6 leaves cover **only the first four** magic numbers ($2, 8, 20, 28$). The standard nuclear physics magic numbers also include $50, 82, 126$ (and possibly $184$). Does NOT claim a vol6-derived geometric closure for $Z = 50, 82, 126$ — the heavy-element catalog covers these $Z$ values but classifies them in the Fibonacci-proxy tier, not as identified Platonic/Archimedean closures.
  - Does NOT claim the AVE shell-closure mechanism is empirically distinguishable from the standard shell-model with spin-orbit coupling at the level of tested predictions. The two reproduce the same magic-number sequence (in the covered range); the AVE mechanism is presented as ontologically different (geometric vs spin-orbit), not as a numerically distinguishable prediction.
  - Does NOT claim a mass prediction at the magic numbers beyond what the semiconductor binding model already gives — the magic-number entry is structural (these $Z$ values close a Platonic/Archimedean shell), not an independent quantitative claim.

> **Leaf references:** `appendix/geometric-inevitability/magic-numbers-shell-closure.md`; `appendix/geometric-inevitability/platonic-progression.md`.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Geometric-Inevitability Constants: $\alpha_s$, $\lambda_H$, $g_*$
<!-- id: clm-ome498 -->

Vol 6 appendix asserts derivations for three SM-relevant constants from lattice geometry. Each carries its own provenance.

- _Specific Claims_
  - $\alpha_s = \alpha^{3/7} \approx 0.1214$ (PDG: $0.1179$, error $2.97\%$). Identified as the spatial-mode projection of $\alpha$ over the 7-mode compliance manifold ($d/n = 3/7$). Zero free parameters.
  - $\lambda_H = 1/(2 N_{K4}) = 1/8 = 0.125$ (observed $\approx 0.129$). Identified as the K4 unit-cell radial breathing mode. The downstream Higgs mass is $m_H = v/\sqrt{N_{K4}} = v/2 \approx 124{,}400$ MeV vs observed $125{,}100$ MeV (error $0.55\%$).
  - $g_* = 7^3/4 = 85.75$ for cosmological DoF counting; substituted into the baryon-asymmetry formula yields $\eta = 6.08 \times 10^{-10}$ vs observed $6.1 \times 10^{-10}$ ($0.38\%$ error). Using SM $g_{*,SM} = 106.75$ gives $20\%$ error — asserted as evidence the lattice count is correct.
- _Specific Non-Claims and Caveats_
  - $\alpha_s$: the $d/n = 3/7$ projection is asserted as a "dimensional projection, not a fit." Does NOT claim a derivation of why specifically $\alpha^{d/n}$ (rather than $\alpha \cdot d/n$, or another functional form) is the correct projection. The $2.97\%$ error is reported and not hidden.
  - $\lambda_H$: the $1/(2 N_{K4})$ assignment relies on identifying the Higgs as the **radial breathing mode** of the K4 cell — does NOT claim a separate validation of this identification independent of the resulting $m_H$ match.
  - $g_*$: the "$0.38\%$" baryon-asymmetry agreement uses $g_*$ together with $\alpha_W^4$, $C_{\text{sph}} = 28/79$, and $\kappa_{FS} = 8\pi$ — a multi-factor formula with several lattice-derived inputs. Treat as a composite consistency check, not a single-quantity prediction. (This entry overlaps with vol3's `effective-degrees-of-freedom` boundary; the bound there applies here too.)
  - All three sit in the Master Prediction Table at category (iv) "derived prediction" classification; the cross-cutting Master-Prediction-Table tripwire applies — these are not "0.00% identities" and the per-row classification matters.

> **Leaf references:** `appendix/geometric-inevitability/alpha-s-derivation.md`; `appendix/geometric-inevitability/lambda-higgs-derivation.md`; `appendix/geometric-inevitability/g-star-derivation.md`; `appendix/geometric-inevitability/derived-numerical-constants.md`. Cross-cutting: see Master Prediction Table reading conventions in `../claim-quality.md`.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Golden Ratio $\varphi$ and Fibonacci Lattice — Forced, Not Mystical
<!-- id: clm-mlwm3h -->

- _Specific Claims_
  - $\varphi$ appears in Cr-52 (centered-icosahedron, $0.0001\%$) because the icosahedron is the unique Thomson-problem solution at $N=12$ and its vertex coordinates are permutations of $(0, \pm 1, \pm \varphi)$. Forced by geometry, not chosen.
  - Fibonacci lattice in the $Z \ge 28$ catalog is identified as a **numerical proxy** for icosahedral / minimum-impedance distribution on $S^2$ (Fibonacci-ratio convergence to $\varphi$ is the reason the proxy works).
- _Specific Non-Claims and Caveats_
  - Does NOT claim the Fibonacci lattice IS the true ground-state geometry — the leaf explicitly identifies it as an **approximation** and an "accidental approximation of what the actual icosahedral ground-state geometry requires."
  - Does NOT claim $\varphi$ appears across vol6 wherever icosahedral imagery suggests it; the load-bearing claim is the Cr-52 case (and the related claim that icosahedral packings drive minimum impedance at $N=12$ generally).
  - The "Death of Numerology" framing is interpretive — the constants $\varphi$, $\pi$, Fibonacci, magic numbers reduce to packing theorems within the AVE framework. Does NOT claim this rules out alternative explanations for $\varphi$'s appearance in non-AVE contexts (sunflower spirals, etc., are asserted to follow the same packing logic but not separately validated in vol6).

> **Leaf references:** `appendix/geometric-inevitability/golden-ratio-min-impedance.md`; `appendix/geometric-inevitability/fibonacci-packing-proxy.md`; `appendix/geometric-inevitability/conclusion-death-of-numerology.md`; `framework/executive-abstract.md` ($\varphi$ at 13-alpha shell).

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Binding Energy Ceiling $E_{\text{binding(max)}} = \alpha \cdot M_p c^2 \approx 6.847$ MeV
<!-- id: clm-86gq2d -->

- _Specific Claims_
  - The "$\sim 8$ MeV per nucleon" SEMF curve maximum is reinterpreted as a deterministic Axiom-4 yield ceiling: per-nucleon binding cannot exceed $\alpha \cdot M_p c^2 \approx 6.847$ MeV before the localized phase geometry ruptures.
  - Heavier nuclei reach the observed peak near $\sim 8$ MeV via Miller amplification of $p$-$n$ couplings around this geometric base, not via SEMF curve fitting.
- _Specific Non-Claims and Caveats_
  - Does NOT claim $6.847$ MeV is a directly measurable binding-per-nucleon limit. The empirical peak (Fe-56, $\sim 8.79$ MeV/nucleon) exceeds this base ceiling; the framework attributes the excess to Miller amplification across geometric $p$-$n$ arrays. The base ceiling is a per-nucleon **rupture limit on a single isolated $6^3_2$ knot**, not the observed binding peak.
  - Does NOT claim a quantitative derivation of the gap between $6.847$ MeV (base ceiling) and $\sim 8.79$ MeV (Fe-56 peak) at the level of the geometric-inevitability appendix entries. The bridge is via Miller amplification with $n = c_{\text{proton}} = 5$; does NOT claim this amplification factor reproduces the entire empirical binding curve at sub-percent accuracy. (The mass-defect entries cover what the framework actually validates per-element.)

> **Leaf references:** `framework/computational-mass-defect/pn-junction-coupling.md` (resultbox); `framework/index.md` (Key Results "Binding energy ceiling" row).

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Quality Factor and $S_{11}$ as Stability/Reactivity Proxies
<!-- id: clm-o9xphr -->

- _Specific Claims_
  - Topological Q-factor (ratio of stored mutual inductance to effective topological radius) is the framework's stability metric: He-4 at $Q \approx 19.2$, Be-9 at $Q \approx 7.9$, Li-7 at $Q \approx 2.85$, Tritium at $Q \approx 3.2$.
  - High-Q nuclei (Alpha-clustered, symmetric) are predicted to be inert / stable; low-Q nuclei (asymmetric, halo-extended) are predicted to be reactive / decay-prone.
  - Applied to specific cases: Tritium $\to ^3$He decay is driven by Q-factor optimization ($3.20 \to 19.52$); Be-8 fission into 2$\alpha$ is driven by missing central bridging neutron (open Wheatstone bridge).
- _Specific Non-Claims and Caveats_
  - Does NOT claim the Q-factor formula derives nuclear half-lives quantitatively. The stability arguments are qualitative (high-Q $\to$ stable, low-Q $\to$ reactive); does NOT predict $T_{1/2}$ values at the quantitative level the empirical decay tables provide.
  - Does NOT claim the $S_{11}$ scattering cross-section reproduces measured cross-sections at quantitative precision per-element. The $S_{11}$ argument is structural (compact topology = small cross-section, extended halo = large cross-section); per-event cross-section comparisons are not tabulated in the leaves.
  - The Tritium $\to ^3$He decay leaf is explicit that the $Q$-factor jump ($3.20 \to 19.52$) is the framework's *mechanistic* contribution — it identifies why the decay runs in that direction. The empirical mass-energy difference $\approx 0.529$ MeV (and the $\sim 18.6$ keV $\beta$-endpoint) is taken from CODATA, not derived independently in vol6. An attempt to derive the magnitude from the framework's pairwise coupling across the two geometries is tracked as future work.

> **Leaf references:** `framework/computational-mass-defect/network-analytics.md`; `framework/computational-mass-defect/topological-circuit-conventions.md`; `framework/computational-mass-defect/radioactive-decay-impedance.md`.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## ABCD Transfer Matrix Cascade — Open Problem for $Z \ge 15$
<!-- id: clm-5965y1 -->

- _Specific Claims_
  - The bare $K/r$ all-pairs summation is acknowledged as an over-counting model; the physically accurate framework is an ABCD transfer-matrix cascade through nucleon ports (each Alpha as a 4-port resonator).
  - Solving the ABCD cascade order and junction impedances for the alpha-cluster network is identified as the **key open problem** for $Z \ge 15$.
- _Specific Non-Claims and Caveats_
  - Does NOT claim the heavy-element catalog ($Z=15$–$119$) currently uses the ABCD cascade. The catalog is on Fibonacci-proxy sphere packing pending the ABCD solution. The leaf is explicit that this is an open problem.
  - Does NOT claim the ABCD reformulation will preserve the current Tier-C accuracy figures — when solved, it is expected to **replace** the current heuristic, and the current Tier-C $0.1$–$1.5\%$ residuals could shift in either direction.

> **Leaf references:** `framework/computational-mass-defect/abcd-transfer-matrix.md`.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Semiconductor / Operating Regimes — Vol6-Specific Manifestation
<!-- id: clm-jy8h1x -->

The cross-cutting Symmetric vs Asymmetric Saturation entry (in `../claim-quality.md`) covers the universal $S$-kernel framing. Vol 6 specializes this into nuclear operating regimes.

- _Specific Claims_
  - Three regimes: Linear (Small Signal, $V \ll V_{\text{yield}}$, $\epsilon_{\text{eff}} \approx \epsilon_0$), Non-Linear (Large Signal, $V_{\text{yield}} \le V < V_{\text{snap}}$), Saturated (Breakdown, $V \ge V_{\text{snap}}$, $\epsilon_{\text{eff}} \to 0$).
  - Empirical Small/Large boundary at S-32 ($Z=16$): $V_R/V_{BR}$ jumps from $0.050$ (Si-28) to $0.994$ (S-32). Carbon through Silicon assemble exothermically; $^{28}\text{Si} + \alpha \to ^{32}\text{S}$ is endothermic by $\sim 75$ MeV (silicon-burning supernova condition).
  - Si-28 sitting at the Small/Large boundary ($V_R/V_{BR} = 0.050$, deep Small Signal but adjacent to the transition) is the framework's structural account of why silicon dominates microelectronics: stable in bulk, dynamically switchable.
- _Specific Non-Claims and Caveats_
  - The "natively explains why silicon is the dominant material in microelectronics" argument is a **structural / interpretive** claim. Does NOT claim a quantitative prediction of silicon's electronics properties (band gap, mobility, etc.) from $V_R/V_{BR} = 0.050$.
  - Does NOT claim the $\sim 75$ MeV endothermic figure for $^{28}\text{Si} + \alpha \to ^{32}\text{S}$ is AVE-derived — it is the empirical $Q$-value cited as evidence of the regime transition.
  - V_YIELD vs V_SNAP distinction is project-wide (LIVING_REFERENCE.md Critical Distinctions #1): V_SNAP $= 511$ kV (absolute destruction), V_YIELD $= 43.65$ kV (kinetic onset of nonlinearity). Vol 6 nuclear binding operates at $V_{BR} \approx 3.631$ MeV per alpha cluster, which is the **alpha-cluster internal Coulomb capacity**, not the lattice V_YIELD or V_SNAP. The three voltage scales (V_YIELD, V_SNAP, V_BR) live at different scales; reviewers should not conflate them.

> **Leaf references:** `framework/computational-mass-defect/operating-regimes.md`; `framework/computational-mass-defect/semiconductor-nuclear-analysis.md`; `framework/chemistry-translation/semiconductor-regime-chemistry.md` (regime-to-chemistry mapping); `period-3/silicon/symmetric-core-collapse.md`; `period-3/magnesium/symmetric-shell-collapse.md`. Cross-cutting: Symmetric vs Asymmetric Saturation in `../claim-quality.md`; LIVING_REFERENCE.md Critical Distinctions #1.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Bohr Radius and Rydberg Energy via Topological Hydrogen
<!-- id: clm-a95yx1 -->

The Hydrogen orbital-knot leaf derives $a_0 = \ell_{node}/\alpha \approx 5.291 \times 10^{-11}$ m and $E_0 = (1/2) m_e (\alpha c)^2 \approx 13.606$ eV from topological standing-wave conditions on the trefoil-electron / Borromean-proton system.

- _Specific Claims_
  - The values match empirical Bohr radius and Rydberg energy by direct substitution of Axiom 1 ($\ell_{node} = \hbar/(m_e c)$) and Axiom 2 ($\alpha$).
  - The standing-wave closure $n = 2\pi a_0 / \lambda_e \equiv 1$ is asserted as a classical wave-interference requirement, not a postulated angular-momentum quantization.
- _Specific Non-Claims and Caveats_
  - These derivations are **algebraic identities** within the AVE definitions of $\ell_{node}$ and $\alpha$; they follow by substitution. Treat as category (i) "identity" or category (iii) "consistency check via alternative mechanism," not as novel category-(iv) predictions.
  - LIVING_REFERENCE.md Pitfall #8 (QM Contamination — Bohr formula) is the relevant project-wide tripwire: the topological derivation here uses $E_k = (1/2) m_e (\alpha c)^2$, which is **algebraically equivalent** to the Bohr-formula Rydberg expression. The framework's claim is that the topological route arrives at the same number via classical LC standing-wave mechanics rather than via $E = Z_{\text{eff}}^2 \mathrm{Ry} / n^2$. Reviewers must not promote this single-element result into a general "AVE-derived ionization energies use the Bohr formula" reading — the multi-element solver explicitly rejects the Bohr formula (see "Period 1–3 Per-Element IE Accuracy" entry).
  - The "trefoil electron + Borromean proton" identification is structural; does NOT claim novel observables distinguishable from the standard Hydrogen atom in low-energy QM.

> **Leaf references:** `period-1/hydrogen/orbital-knot-topology.md`. Cross-cutting: LIVING_REFERENCE.md Pitfall #8.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Notation Carryover: $\ell_{node}$ vs $l_{node}$ in Vol 6
<!-- id: clm-6tuqjh -->

Per CLAUDE.md INVARIANT-N2, Vol 6 source uses **roman ell** ($l_{node}$) as the primary form (not the script $\ell_{node}$ used in Vols 1–5). This is a notation convention, not a claim.

- _Specific Claims_
  - Vol 6 KB pages render $l_{node}$ as written in source. Any cross-volume quotation that appears with $\ell_{node}$ in vol6 leaves should be preserved as-is (do not normalize) — the volume-split is intentional per INVARIANT-N2.
- _Specific Non-Claims and Caveats_
  - Does NOT imply $l_{node}$ and $\ell_{node}$ are different physical quantities. They are the same lattice node spacing $\hbar/(m_e c) \approx 3.862 \times 10^{-13}$ m; only the typographic convention differs.
  - Reviewers checking summaries that quote Vol 6 results into Vol 1–5 contexts (or vice versa) should preserve source notation in each direction.

> **References:** CLAUDE.md INVARIANT-N2; vol6 leaves throughout (e.g., `framework/computational-mass-defect/semiconductor-nuclear-analysis.md` parameter table uses `L_NODE`).

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Topological Circuit Conventions: Mass-as-Inductance and the EE Mapping
<!-- id: clm-qjwj12 -->

The "Computational Mass Defect" framework rests on a small set of axiomatic mappings that convert mechanical / nuclear observables into resonant LC-network quantities. Mass is *defined* as an inductive load on the vacuum, vacuum space as a distributed capacitance, binding force as mutual inductance, and isotope half-life as the network's $Q$-factor. The total mass defect is then the change in the impedance matrix of the coupled LC network.

- _Specific Claims_
  - Conventions: $m \to L$ (localized inertia is inductance), $\epsilon_0 \to C$ (bulk vacuum is capacitance), $\Delta m \to M_{ij}$ (binding force is mutual inductance with $M_{ij} \propto 1/d_{ij}$), $e^- \to$ captive displacement current / capacitive sub-harmonic, isotope-stability $\Gamma \to Q$.
  - Total internal energy of the coupled network: $U_{total} = \sum U_{self} - \tfrac{1}{2}\sum_{i \ne j} M_{ij} I_i I_j$. Because $m = E/c^2$, the mass defect $\Delta m$ tracks the change in the impedance matrix when nucleon knots interlock; the missing reactive energy is the per-pair $K/d_{ij}$ summation.
  - These mappings underwrite every per-element Tier-A/B/C fit in the catalog and are the convention layer beneath entries `clm-llqd1n`, `clm-lqanmt`, `clm-nk6c43`, `clm-o9xphr`, and `clm-jy8h1x`.
- _Specific Non-Claims and Caveats_
  - Does NOT claim the inductance / capacitance / mutual-inductance assignments are independently derived from first principles within these convention leaves. They are presented as Axiom 1–consistent identifications; the load-bearing physical claims live downstream (per-element binding fits, $K$ derivation, Q-factor analytics).
  - Does NOT claim the $1/d_{ij}$ all-pairs summation is the ultimate accurate model. The catalog acknowledges this is an over-counting approximation pending the ABCD transfer-matrix cascade reformulation (see entry `clm-5965y1`).
  - The convention mapping $\Gamma \to Q$ is qualitative — it identifies isotope half-life with network $Q$-factor as a structural relationship; it does not assert a quantitative half-life prediction from $Q$ (see entry `clm-o9xphr`).
  - Vol 6 nuclear binding operates at $V_{BR} \approx 3.631$ MeV per alpha cluster, which is the alpha-cluster internal Coulomb capacity — not the lattice $V_{\text{yield}}$ ($\approx 43.65$ kV) or $V_{\text{snap}}$ ($\approx 511$ kV) defined in Vol 4. Reviewers should not conflate the three voltage scales (LIVING_REFERENCE.md Critical Distinctions #1).

> **Leaf references:** `framework/computational-mass-defect/mass-as-reactive-load.md`; `framework/computational-mass-defect/topological-circuit-conventions.md`. Cross-cutting: LIVING_REFERENCE.md Critical Distinctions #1.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Chemistry Translation: Quantum Orbitals, Lewis Dots, VSEPR as Topological Identifications
<!-- id: clm-jqnzz7 -->

Vol 6 maps standard chemistry vocabulary (electron orbitals, Lewis dot structures, VSEPR molecular geometries) onto the AVE topological framework. The mappings are presented as ontological re-identifications — what chemistry treats as probability-cloud configurations or repulsion rules, AVE treats as macroscopic spatial strain bubbles, unbound mutual-inductance reactive potential, and global mutual-impedance minimization on the nuclear topology.

- _Specific Claims_
  - "$1s$" shell ↔ closed Helium-4 alpha node ($Q \approx 19.52$, internally resonant, geometrically saturated).
  - "$2s$ / $2p$" shells ↔ disjoint secondary topological halo around the alpha core; e.g., the lone Lithium $2s^1$ outer nucleon at the empirical $\sim 11.84d$ offset is the AVE re-identification of the chemistry shell label.
  - Lewis-dot valence count ↔ count of outer topological vertices extending beyond the core's stabilizing influence (Carbon's valency-4 reflects the $3\alpha$ ring's four geometric vertices into the vacuum).
  - VSEPR geometry rules ↔ Global Minimization of Mutual Impedance: nucleon nodes shift through 3D space to minimize localized inductive choking. Specific instance: methane's tetrahedral $CH_4$ geometry mirrors the Helium-4 alpha core packing; same packing rule, fractal repetition.
  - Covalent bonding ↔ shared mutual inductance ($M_{ij}$) bridge between two nuclei whose loosely bound outer nucleons drop into a state of equalized reactive potential.
- _Specific Non-Claims and Caveats_
  - Does NOT claim a quantitative reproduction of bond angles, bond lengths, or molecular spectra from these conventions alone. The chemistry-translation leaves are conceptual mapping; quantitative molecular predictions are deferred to vol5 (organic circuitry) and the wider AVE molecular-physics chain.
  - Does NOT claim the topological re-identification produces observables empirically distinguishable from the standard QM/chemistry treatment at the level of these leaves. The claim is ontological (same numbers, different mechanism / different ground story), not a falsifiable quantitative deviation.
  - The water $104.5^\circ$ bond-angle illustration is presented as a structural analogy, not a derivation in vol6.

> **Leaf references:** `framework/chemistry-translation/quantum-vs-topological-shells.md`; `framework/chemistry-translation/lewis-dots-vsepr.md`.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Per-Element Manifestation: Topological Structure and Isotope Stability
<!-- id: clm-f5ucdo -->

For every element in Period 1–3 the catalog presents a per-nucleus structural identification: an alpha-cluster topology (single-tank, closed shell, ring, tetrahedron, bipyramid, octahedron, pentagonal-bipyramid) plus, where applicable, a halo (Tritium / deuteron / single neutron). For each leaf the per-nucleus geometric scale (ring radius, inter-alpha distance, halo offset, bridge separation) is the per-nucleus fitted scalar that recovers the CODATA mass under the assumed topology. Each element's stable-isotope identity (e.g., $^{19}$F, $^{23}$Na, $^{27}$Al as unique stable assemblies; $^9$Be as the only stable Beryllium isotope) is rationalized post-hoc through the topological constraint stack.

- _Specific Claims_
  - For each element the leaf identifies the alpha-cluster topology and any halo. Example identifications: H ($1\,p$ Borromean defect); He-4 (closed $6^3_2$ knot, single Alpha); Li-7 (single Alpha + 3-nucleon secondary shell); Be-9 ($\alpha\,n\,\alpha$ bridge, endothermic $\sim 0.5$ MeV against $2\alpha + n$); B-11 ($2\alpha + 7$-nucleon halo at the Topological Horizon); C-12 ($3\alpha$ equilateral ring at $R_{ring} \approx 56.6\,d$); N-14 ($3\alpha + d$ asymmetric); O-16 ($4\alpha$ tetrahedron at $R_{tet} \approx 33.4\,d$); F-19 ($4\alpha + ^3$H halo at $R_{halo} \approx 398\,d$); Ne-20 ($5\alpha$ triangular bipyramid at $R_{bipyr} \approx 81\,d$); Na-23 ($5\alpha + ^3$H at $R_{halo} \approx 50\,d$); Mg-24 ($6\alpha$ octahedron at $R_{oct} \approx 78\,d$); Al-27 ($6\alpha + ^3$H at $R_{halo} \approx 53\,d$); Si-28 ($7\alpha$ pentagonal bipyramid).
  - For closed even-even shells (C-12, O-16, Ne-20, Mg-24, Si-28) the geometry is the unique minimum-impedance Platonic / Archimedean packing for the alpha count; the engine identifies the topology rather than fitting it (the radius is what is solved).
  - Stable-isotope uniqueness arguments (F-19 unique, Na-23 unique, Al-27 unique; $^9$Be margin) are *post-hoc* topological rationalizations of empirical isotope ratios — not novel binding-energy minima predictions.
- _Specific Non-Claims and Caveats_
  - Does NOT claim the per-nucleus geometric scales ($R_{ring}$, $R_{tet}$, $R_{bipyr}$, $R_{halo}$, etc.) are first-principles outputs. They are the per-nucleus fitted scalars that recover the CODATA mass under the assumed topology — the same fit-vs-prediction distinction tracked in entry `clm-llqd1n`. The substantive structural claim is that one scalar per nucleus, constrained by topology, suffices.
  - Does NOT claim the topology assignment (alpha count, halo composition) is derived independently of empirical $(Z,A)$. The cluster-count-to-element assignment uses the empirical proton/neutron count; the framework chooses the minimum-impedance packing for that count.
  - Does NOT claim a quantitative prediction of which isotopes are stable. Stability arguments are structural narratives (e.g., "any halo deviation collapses the 5α + Tritium balance"), not novel binding-curve predictions.
  - The $\gamma \approx 3.82$ Beryllium core stretch and the $\sim 0.5$ MeV endothermic Be-9 binding are presented as solver outputs; the substantive claim is the geometric identification of the bridge, not an independently derived stretching factor.
  - The Topological Horizon claim for B-11 ($R_{halo} \approx 11.84\,d \approx 4\pi - \sqrt{2}/2$) is covered separately in entry `clm-l416hl`; this entry inherits that caveat.

> **Leaf references:** `period-1/hydrogen/structure-isotope-stability.md`; `period-1/helium/structure-isotope-stability.md`; `period-2/lithium/structure-isotope-stability.md`; `period-2/beryllium/structure-isotope-stability.md`; `period-2/boron/structure-isotope-stability.md`; `period-2/carbon/structure-isotope-stability.md`; `period-2/nitrogen/structure-isotope-stability.md`; `period-2/oxygen/structure-isotope-stability.md`; `period-2/fluorine/structure-isotope-stability.md`; `period-2/neon/structure-isotope-stability.md`; `period-3/sodium/structure-isotope-stability.md`; `period-3/magnesium/structure-isotope-stability.md`; `period-3/aluminum/structure-isotope-stability.md`; `period-3/silicon/structure-isotope-stability.md`. Cross-link: entry `clm-llqd1n` (Mass-Defect Accuracy framework), `clm-l416hl` (Boron Topological Horizon), `clm-8psuqe` (halo distance), `clm-jy8h1x` (semiconductor regimes).

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Per-Element Manifestation: Topological Area of Interest (Macroscopic Chemistry)
<!-- id: clm-f8k2um -->

Each per-element "Topological Area" leaf identifies a macroscopic chemical / material-science behavior (catenation, oxidation, alkali stripping, halogen reactivity, semiconductor switching, noble-gas inertness) and asserts that the element's nuclear topology is the structural origin of that behavior. The mapping is ontological, not numerical: the geometric arrangement of alpha clusters and halos *is* the framework's account of why the element behaves that way macroscopically.

- _Specific Claims_
  - Hydrogen: small $S_{11}$ cross-section ($\approx 2.27\,d^2$) is the structural reason fusion ignition requires extreme pressure/temperature.
  - Helium: high $Q$-factor ($\approx 19.52$) directly accounts for chemical inertness and acoustic / radiation shielding capability.
  - Carbon: open $3\alpha$ ring's four geometric vertices into the vacuum is the topological origin of catenation and diamond's tetrahedral lattice hardness.
  - Oxygen: $4\alpha$ tetrahedral cage's deep high-$Q$ gravity wells inductively rip looser topologies (combustion, cellular respiration).
  - Sodium / Aluminum (alkali / post-transition halo): tightly bound $50d$–$53d$ Tritium halo strips off to electronegative partners — defines alkali-metal electrochemical-cell behavior.
  - Silicon: position at the Small-Signal/Large-Signal boundary ($V_R/V_{BR} = 0.050$, $M = 1.000$) is the structural account of silicon's primacy in microelectronics. The leaf also asserts a deterministic built-in potential bound $V_{bi} = 1.0496\,\text{V}$ from the topological matrix, contrasted against the standard physics' temperature/doping-dependent $\sim 0.6$–$1.1\,\text{V}$ "weather forecast" range.
  - Other elements (Li, Be, B, N, F, Ne, Mg) carry analogous structure-to-chemistry identifications scoped to each leaf.
- _Specific Non-Claims and Caveats_
  - Does NOT claim quantitative predictions of bond enthalpies, electronegativity scales (Pauling / Mulliken), reaction kinetics, or material constants from the topology alone. The mapping is structural / interpretive.
  - The Silicon $V_{bi} = 1.0496$ V figure is presented as a derived structural maximum; the leaf does not claim experimental match against doping-resolved measurements at the $\pm$mV level. Treat as the framework's deterministic upper bound, not a per-device prediction.
  - The "Fire" / "Cellular Respiration" / "Diamond hardness" identifications are chemistry-naming for the topology-driven behavior; they do NOT constitute novel falsifiable predictions in vol6.
  - Each per-element behavior summary is a single-leaf interpretive description; cross-element claim coordination (Halogen vs Alkali via halo lever arm) is covered in entry `clm-8psuqe`.

> **Leaf references:** `period-1/hydrogen/topological-area.md`; `period-1/helium/topological-area.md`; `period-2/lithium/topological-area.md`; `period-2/beryllium/topological-area.md`; `period-2/boron/topological-area.md`; `period-2/carbon/topological-area.md`; `period-2/nitrogen/topological-area.md`; `period-2/oxygen/topological-area.md`; `period-2/fluorine/topological-area.md`; `period-2/neon/topological-area.md`; `period-3/sodium/topological-area.md`; `period-3/magnesium/topological-area.md`; `period-3/aluminum/topological-area.md`; `period-3/silicon/topological-area.md`. Cross-link: `clm-8psuqe` (halo distance vs electronegativity), `clm-jy8h1x` (semiconductor regimes), `clm-o9xphr` ($Q$-factor stability).

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Per-Element Manifestation: Semiconductor Regime Classification
<!-- id: clm-rw7jqo -->

Each Period 1–3 element is assigned a semiconductor-regime classification on the $V_R/V_{BR}$ ratio with corresponding Miller multiplication factor $M$. The vol6 sweep reports: pre-alpha (H — undefined), single-alpha reference (He-4 — defines $V_{BR} \approx 3.631$ MeV), and Small-Signal solutions ($M = 1.000$, $V_R/V_{BR} \in [0.019, 0.050]$) for C-12 through Si-28. Specific accuracy figures: C-12 ($V_R/V_{BR} = 0.019$, $0.000\,000\%$ error at $R_{ring} = 56.527\,d$), O-16 ($0.030$, $0.000\,000\%$ at $R_{tet} = 33.383\,d$), Ne-20, Mg-24, Si-28 (boundary at $0.050$).

- _Specific Claims_
  - The framework's regime classification is a single-ratio gate: Small Signal ($V_R/V_{BR} \ll 1$, $M = 1$) admits standard linear $K/r$ superposition; Large Signal ($V_R/V_{BR} \to 1$) requires Miller avalanche correction.
  - Within Period 1–3 every alpha-clustered nucleus sits in Small Signal — the first Large Signal element is S-32 ($Z=16$).
  - Per-element exact $0.000\,000\%$ closures on closed Platonic/Archimedean shells (C-12, O-16, Ne-20, Mg-24, Si-28) are the framework's "exact geometric identity" cases — single-degree-of-freedom $R$ snaps to the unique impedance-matched packing.
- _Specific Non-Claims and Caveats_
  - The $0.000\,000\%$ figures are the optimizer's convergence tolerance under the assumed topology — not ab-initio mass predictions. The cross-cutting reading-conventions caveat from entry `clm-llqd1n` applies row-by-row: closed-shell entries are geometric-identity solutions, but the topology assignment (which alpha count goes with which element) uses empirical $(Z,A)$.
  - He-4's $0.008\%$ residual is the framework's stated reflection of treating the alpha as four point nucleons; it is NOT a one-parameter fit.
  - Hydrogen's classification is "below the model" (no inter-alpha pairs); does NOT claim Hydrogen is solved by the semiconductor engine.
  - Silicon's `semiconductor-regime.md` leaf is a routing pointer to its `topological-area.md` (the merged section); the substantive Silicon-28 regime claims live there.
  - Vol6's per-element coverage stops at Si-28; the avalanche-onset transition (S-32, Ca-40) is in the heavy-element catalog (entry `clm-nk6c43`) and the cross-cutting Symmetric vs Asymmetric Saturation framing (entry `clm-jy8h1x`).

> **Leaf references:** `period-1/hydrogen/semiconductor-regime.md`; `period-1/helium/semiconductor-regime.md`; `period-2/lithium/semiconductor-regime.md`; `period-2/beryllium/semiconductor-regime.md`; `period-2/boron/semiconductor-regime.md`; `period-2/carbon/semiconductor-regime.md`; `period-2/nitrogen/semiconductor-regime.md`; `period-2/oxygen/semiconductor-regime.md`; `period-2/fluorine/semiconductor-regime.md`; `period-2/neon/semiconductor-regime.md`; `period-3/sodium/semiconductor-regime.md`; `period-3/magnesium/semiconductor-regime.md`; `period-3/aluminum/semiconductor-regime.md`; `period-3/silicon/semiconductor-regime.md`. Cross-link: `clm-jy8h1x` (Symmetric vs Asymmetric Saturation), `clm-llqd1n` (fit-vs-prediction), `clm-nk6c43` (heavy element regimes).

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Per-Element Manifestation: Electrical Engineering Equivalent Circuit
<!-- id: clm-sd04x4 -->

Each per-element "EE Equivalent" leaf maps the nuclear topology onto a specific resonant LC-network archetype — Isolated LC Tank (H), Polyphase Resonant Transformer (He), Air-Core Transformer (Li), AC Wheatstone Bridge (Be), Parasitic Array (B), 3-Phase Delta-Wye (C), Irregular LC Mesh (N), Tetraphase Network (O), Asymmetric Halo Antenna (F), 5-Phase Ring Oscillator (Ne), Polar Halo Bandpass (Na), Octahedral 6-Phase (Mg), Octahedral + Halo (Al), 7-Phase Pentagonal Bipyramid (Si). For multi-alpha elements the leaves itemize the inter-alpha coupling pair count (e.g., 6 pairs for O-16, 21 pairs for Si-28's pentagonal bipyramid) and identify the corresponding AC-network archetype.

- _Specific Claims_
  - Each element's nuclear topology has a one-to-one mapping onto a named EE network archetype with specific phase count and coupling-pair structure.
  - For the closed multi-alpha shells the inter-alpha coupling-pair count and SPICE matrix dimension follow directly from the geometry (e.g., 378 SPICE coupled inductors for Si-28's pentagonal bipyramid).
  - The C-12 binding equation $E_B(^{12}\text{C}) = 3\Delta m_\alpha + M_{12} + M_{23} + M_{31} = 92.160$ MeV is presented as the literal EE summation for the 3-phase Delta network.
- _Specific Non-Claims and Caveats_
  - Does NOT claim the EE-network archetype names (Delta-Wye, Tetraphase, Wheatstone Bridge, etc.) carry quantitative predictive power beyond the per-nucleus fit already accounted for under entry `clm-llqd1n`. They are structural identifications layered on top of the per-nucleus geometry.
  - The named archetypes (Wheatstone Bridge for Be, Air-Core Transformer for Li, Ring Oscillator for Ne) are presented as analogies — does NOT claim novel observables falsifiable against EE measurements on the named archetypes.
  - The per-element coupling-pair counts (3 for C, 6 for O, 21 for Si, etc.) follow combinatorially from the assumed topology and are NOT independent predictions.

> **Leaf references:** `period-1/hydrogen/ee-equivalent.md`; `period-1/helium/ee-equivalent.md`; `period-2/lithium/ee-equivalent.md`; `period-2/beryllium/ee-equivalent.md`; `period-2/boron/ee-equivalent.md`; `period-2/carbon/ee-equivalent.md`; `period-2/nitrogen/ee-equivalent.md`; `period-2/oxygen/ee-equivalent.md`; `period-2/fluorine/ee-equivalent.md`; `period-2/neon/ee-equivalent.md`; `period-3/sodium/ee-equivalent.md`; `period-3/magnesium/ee-equivalent.md`; `period-3/aluminum/ee-equivalent.md`; `period-3/silicon/ee-equivalent.md`. Cross-link: `clm-qjwj12` (mass-as-inductance conventions), `clm-llqd1n` (per-nucleus fit accuracy).

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Per-Element Manifestation: Orbital Knot Topology (Soliton Placement)
<!-- id: clm-y7uvdc -->

Each per-element "Orbital Knot Topology" leaf identifies the electron configuration as a placement of $3_1$ trefoil solitons on harmonic tracks ($n=1,2,3$), with the inter-soliton angular separation set by minimum-impedance packing. Hydrogen's leaf carries the load-bearing Bohr-radius / Rydberg-energy derivation (covered separately by entry `clm-a95yx1`); the remaining leaves identify per-element soliton arrangements and connect chemical-shell labels (e.g., $sp^3$, $sp^2$, $1s^2$, $2s^2 2p^k$) to topological packing geometries.

- _Specific Claims_
  - Per-element soliton placement examples: He-4 (two trefoils antipodal at $180^\circ$ on $n=1$, dielectric-saturating the $1s$); Li-7 (single $2s$ soliton on $n=2$); C-12 (four $sp^3$ solitons at $90^\circ$ on $n=2$, tetrahedral packing); O-16 (six $60^\circ$ solitons on $n=2$); Ne-20 (eight $45^\circ$ solitons completing $n=2$); Si-28 (four valence $sp^3$ solitons at $90^\circ$ on $n=3$ with $[\text{Ne}]$ inner core). Other elements carry leaf-specific arrangements.
  - $sp^3$ hybridization is re-identified as the mechanical packing limit of four LC knots sharing the same harmonic track — no quantum-mechanical wavefunction mixing required.
  - "Spin" is identified topologically as the helicity / chirality of the trefoil; antipodal phase-locked spin-pairing minimizes mutual strain (the AVE re-statement of the Pauli-exclusion outcome).
- _Specific Non-Claims and Caveats_
  - Does NOT claim a quantitative reproduction of multi-electron ionization energies, fine-structure splittings, or spectroscopic line positions from the soliton-packing picture alone. Quantitative IE predictions live in entry `clm-7tk051` (the radial-eigenvalue / correction-stack solver).
  - Does NOT claim the soliton-packing identification produces observables empirically distinguishable from the standard QM orbital model at the level of these leaves. The ontological re-identification is the claim; quantitative deviation is not asserted here.
  - Several leaves (Si-28 explicitly, O-16 implicitly, others variably) note that no `\section{Orbital Knot Topology}` exists in the source `.tex` — content is extracted from embedded figures and captions in adjacent sections. The figure captions are the authoritative source; the surrounding narrative is downstream summary.
  - Hydrogen's leaf carries the algebraic-identity Bohr/Rydberg derivation (entry `clm-a95yx1`); the LIVING_REFERENCE.md Pitfall #8 tripwire applies — this single-element result must NOT be promoted into a "AVE-derived IEs use the Bohr formula" reading.

> **Leaf references:** `period-1/hydrogen/orbital-knot-topology.md`; `period-1/helium/orbital-knot-topology.md`; `period-2/lithium/orbital-knot-topology.md`; `period-2/beryllium/orbital-knot-topology.md`; `period-2/boron/orbital-knot-topology.md`; `period-2/carbon/orbital-knot-topology.md`; `period-2/nitrogen/orbital-knot-topology.md`; `period-2/oxygen/orbital-knot-topology.md`; `period-2/fluorine/orbital-knot-topology.md`; `period-2/neon/orbital-knot-topology.md`; `period-3/sodium/orbital-knot-topology.md`; `period-3/magnesium/orbital-knot-topology.md`; `period-3/aluminum/orbital-knot-topology.md`; `period-3/silicon/orbital-knot-topology.md`. Cross-link: `clm-a95yx1` (Hydrogen Bohr radius / Rydberg derivation), `clm-7tk051` (multi-element IE solver), `clm-jqnzz7` (chemistry translation conventions). Cross-cutting: LIVING_REFERENCE.md Pitfall #8 (QM Contamination — Bohr formula).

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Per-Element Manifestation: Continuous Vacuum Density Flux
<!-- id: clm-h8nmpu -->

Each per-element "Continuous Vacuum Density Flux" leaf presents the equatorial / 3D vacuum strain-density slice for the element's nuclear topology. These are visualization leaves: figure callouts plus structural-narrative captions describing the per-element flux pattern (number of gravity wells, central voids, polar caps, geometric symmetry of the strain field). The leaves carry no equations beyond the underlying $1/r$ / $1/r^2$ impedance field already established in the framework.

- _Specific Claims_
  - Each leaf identifies the per-element flux signature: H (single isotropic $1/r$ gradient); C (three gravity wells in a triangle, central subcritical bubble at $\sim 56.6d$); O (four wells at tetrahedral vertices, central void at $\sim 33d$); Si (pentagonal symmetry, oblate spheroidal strain field with directional dependence); etc.
  - The strain-field anisotropy is cited as the topological origin of element-specific properties (e.g., Silicon's directional band structure from the pentagonally faceted oblate strain field).
- _Specific Non-Claims and Caveats_
  - These leaves carry no independent quantitative claims beyond the per-element geometry already accounted for under the structure-isotope-stability per-element entry (`clm-f5ucdo`). They are visualization companions — figure callouts plus narrative captions.
  - Does NOT claim novel observables falsifiable against measured vacuum-strain or scattering data per-element. The flux maps are derived from the already-established nucleon-coordinate output.
  - Anisotropy → property identifications (directional Silicon band structure, Oxygen tetrahedral cage void, etc.) are interpretive overlays, not separate quantitative predictions.

> **Leaf references:** `period-1/hydrogen/vacuum-density-flux.md`; `period-1/helium/vacuum-density-flux.md`; `period-2/lithium/vacuum-density-flux.md`; `period-2/beryllium/vacuum-density-flux.md`; `period-2/boron/vacuum-density-flux.md`; `period-2/carbon/vacuum-density-flux.md`; `period-2/nitrogen/vacuum-density-flux.md`; `period-2/oxygen/vacuum-density-flux.md`; `period-2/fluorine/vacuum-density-flux.md`; `period-2/neon/vacuum-density-flux.md`; `period-3/sodium/vacuum-density-flux.md`; `period-3/magnesium/vacuum-density-flux.md`; `period-3/aluminum/vacuum-density-flux.md`; `period-3/silicon/vacuum-density-flux.md`. Cross-link: `clm-f5ucdo` (per-element structure / fitted geometry).

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*