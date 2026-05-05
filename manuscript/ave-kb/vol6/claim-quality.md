# Vol 6 — Periodic Table of Knots — Claim Quality

<!-- path-stable: referenced from CLAUDE.md INVARIANT-S7 and from vol6/index.md bootstrap directive -->

> **Canonicality:** Leaves are canonical; this volume's indexes are derived summaries. See [cross-cutting claim-quality register](../claim-quality.md) for the full preamble and the canonical list of project-wide tripwires (the cross-cutting sidecar is the source of truth for which tripwires are project-wide; do not infer the list from this preamble). Entries below are scoped to Vol 6; cross-cutting tripwires with vol6-specific manifestations are noted but not duplicated.

---

## Mass-Defect Accuracy: Fitted Geometry, Not Ab-Initio Mass Prediction

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

---

## Mutual Coupling Constant $K \approx 11.337$ MeV·fm — Derived but Path-Dependent

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

---

## Period 1–3 Per-Element IE Accuracy and Correction Stack

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

---

## Heavy Element Catalog ($Z=15$–$119$): Accuracy Tiers, Not a Uniform Bound

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

> **Leaf references:** `appendix/heavy-element-catalog/full-element-table.md`; `appendix/heavy-element-catalog/mass-prediction-accuracy.md`; `appendix/heavy-element-catalog/index.md`; `appendix/geometric-inevitability/fibonacci-packing-proxy.md`; `appendix/geometric-inevitability/platonic-progression.md`; `framework/computational-mass-defect/abcd-transfer-matrix.md` (ABCD cascade as the open problem). Cross-cutting: Master Prediction Table reading conventions in `../claim-quality.md`.

---

## Topological Horizon at Boron-11 ($R = 4\pi - \sqrt{2}/2 \approx 11.86\,d$)

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

---

## Topology-Determined Halo Distance: Structure, Not Curve Fit

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

---

## Magic Numbers as Geometric Closure (Partial Coverage)

- _Specific Claims_
  - The first four nuclear magic numbers ($Z = 2, 8, 20, 28$) are identified with closed Platonic / Archimedean alpha-cluster packings: Single Tank, Tetrahedron, Bicapped Antiprism, FCC-14 respectively.
  - The mechanism is impedance matching ($S_{11} \to 0$, maximum Q-factor) when every alpha cluster is symmetrically equivalent and the strain field has zero net dipole moment.
  - This is a category (iii)/(iv) hybrid: reproduces the empirical magic-number sequence via an alternative mechanism (geometric closure rather than spin-orbit shell-model coupling).
- _Specific Non-Claims and Caveats_
  - Vol 6 leaves cover **only the first four** magic numbers ($2, 8, 20, 28$). The standard nuclear physics magic numbers also include $50, 82, 126$ (and possibly $184$). Does NOT claim a vol6-derived geometric closure for $Z = 50, 82, 126$ — the heavy-element catalog covers these $Z$ values but classifies them in the Fibonacci-proxy tier, not as identified Platonic/Archimedean closures.
  - Does NOT claim the AVE shell-closure mechanism is empirically distinguishable from the standard shell-model with spin-orbit coupling at the level of tested predictions. The two reproduce the same magic-number sequence (in the covered range); the AVE mechanism is presented as ontologically different (geometric vs spin-orbit), not as a numerically distinguishable prediction.
  - Does NOT claim a mass prediction at the magic numbers beyond what the semiconductor binding model already gives — the magic-number entry is structural (these $Z$ values close a Platonic/Archimedean shell), not an independent quantitative claim.

> **Leaf references:** `appendix/geometric-inevitability/magic-numbers-shell-closure.md`; `appendix/geometric-inevitability/platonic-progression.md`.

---

## Geometric-Inevitability Constants: $\alpha_s$, $\lambda_H$, $g_*$

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

---

## Golden Ratio $\varphi$ and Fibonacci Lattice — Forced, Not Mystical

- _Specific Claims_
  - $\varphi$ appears in Cr-52 (centered-icosahedron, $0.0001\%$) because the icosahedron is the unique Thomson-problem solution at $N=12$ and its vertex coordinates are permutations of $(0, \pm 1, \pm \varphi)$. Forced by geometry, not chosen.
  - Fibonacci lattice in the $Z \ge 28$ catalog is identified as a **numerical proxy** for icosahedral / minimum-impedance distribution on $S^2$ (Fibonacci-ratio convergence to $\varphi$ is the reason the proxy works).
- _Specific Non-Claims and Caveats_
  - Does NOT claim the Fibonacci lattice IS the true ground-state geometry — the leaf explicitly identifies it as an **approximation** and an "accidental approximation of what the actual icosahedral ground-state geometry requires."
  - Does NOT claim $\varphi$ appears across vol6 wherever icosahedral imagery suggests it; the load-bearing claim is the Cr-52 case (and the related claim that icosahedral packings drive minimum impedance at $N=12$ generally).
  - The "Death of Numerology" framing is interpretive — the constants $\varphi$, $\pi$, Fibonacci, magic numbers reduce to packing theorems within the AVE framework. Does NOT claim this rules out alternative explanations for $\varphi$'s appearance in non-AVE contexts (sunflower spirals, etc., are asserted to follow the same packing logic but not separately validated in vol6).

> **Leaf references:** `appendix/geometric-inevitability/golden-ratio-min-impedance.md`; `appendix/geometric-inevitability/fibonacci-packing-proxy.md`; `appendix/geometric-inevitability/conclusion-death-of-numerology.md`; `framework/executive-abstract.md` ($\varphi$ at 13-alpha shell).

---

## Binding Energy Ceiling $E_{\text{binding(max)}} = \alpha \cdot M_p c^2 \approx 6.847$ MeV

- _Specific Claims_
  - The "$\sim 8$ MeV per nucleon" SEMF curve maximum is reinterpreted as a deterministic Axiom-4 yield ceiling: per-nucleon binding cannot exceed $\alpha \cdot M_p c^2 \approx 6.847$ MeV before the localized phase geometry ruptures.
  - Heavier nuclei reach the observed peak near $\sim 8$ MeV via Miller amplification of $p$-$n$ couplings around this geometric base, not via SEMF curve fitting.
- _Specific Non-Claims and Caveats_
  - Does NOT claim $6.847$ MeV is a directly measurable binding-per-nucleon limit. The empirical peak (Fe-56, $\sim 8.79$ MeV/nucleon) exceeds this base ceiling; the framework attributes the excess to Miller amplification across geometric $p$-$n$ arrays. The base ceiling is a per-nucleon **rupture limit on a single isolated $6^3_2$ knot**, not the observed binding peak.
  - Does NOT claim a quantitative derivation of the gap between $6.847$ MeV (base ceiling) and $\sim 8.79$ MeV (Fe-56 peak) at the level of the geometric-inevitability appendix entries. The bridge is via Miller amplification with $n = c_{\text{proton}} = 5$; does NOT claim this amplification factor reproduces the entire empirical binding curve at sub-percent accuracy. (The mass-defect entries cover what the framework actually validates per-element.)

> **Leaf references:** `framework/computational-mass-defect/pn-junction-coupling.md` (resultbox); `framework/index.md` (Key Results "Binding energy ceiling" row).

---

## Quality Factor and $S_{11}$ as Stability/Reactivity Proxies

- _Specific Claims_
  - Topological Q-factor (ratio of stored mutual inductance to effective topological radius) is the framework's stability metric: He-4 at $Q \approx 19.2$, Be-9 at $Q \approx 7.9$, Li-7 at $Q \approx 2.85$, Tritium at $Q \approx 3.2$.
  - High-Q nuclei (Alpha-clustered, symmetric) are predicted to be inert / stable; low-Q nuclei (asymmetric, halo-extended) are predicted to be reactive / decay-prone.
  - Applied to specific cases: Tritium $\to ^3$He decay is driven by Q-factor optimization ($3.20 \to 19.52$); Be-8 fission into 2$\alpha$ is driven by missing central bridging neutron (open Wheatstone bridge).
- _Specific Non-Claims and Caveats_
  - Does NOT claim the Q-factor formula derives nuclear half-lives quantitatively. The stability arguments are qualitative (high-Q $\to$ stable, low-Q $\to$ reactive); does NOT predict $T_{1/2}$ values at the quantitative level the empirical decay tables provide.
  - Does NOT claim the $S_{11}$ scattering cross-section reproduces measured cross-sections at quantitative precision per-element. The $S_{11}$ argument is structural (compact topology = small cross-section, extended halo = large cross-section); per-event cross-section comparisons are not tabulated in the leaves.
  - Tritium $\to ^3$He release of "$\sim 11.3$ MeV" is the framework's identification of the decay energetics in Q-factor terms; the empirical $\beta$-decay $Q$-value for tritium is $18.6$ keV, not $11.3$ MeV. Reviewers should note that "$\sim 11.3$ MeV" in the vol6 leaf refers to the **mass-defect difference between the unstable and stable topologies** as the framework computes them, not the $\beta$-particle endpoint energy. Treat the $11.3$ MeV figure as an internal framework quantity, not a measurement match.

> **Leaf references:** `framework/computational-mass-defect/network-analytics.md`; `framework/computational-mass-defect/topological-circuit-conventions.md`; `framework/computational-mass-defect/radioactive-decay-impedance.md`.

---

## ABCD Transfer Matrix Cascade — Open Problem for $Z \ge 15$

- _Specific Claims_
  - The bare $K/r$ all-pairs summation is acknowledged as an over-counting model; the physically accurate framework is an ABCD transfer-matrix cascade through nucleon ports (each Alpha as a 4-port resonator).
  - Solving the ABCD cascade order and junction impedances for the alpha-cluster network is identified as the **key open problem** for $Z \ge 15$.
- _Specific Non-Claims and Caveats_
  - Does NOT claim the heavy-element catalog ($Z=15$–$119$) currently uses the ABCD cascade. The catalog is on Fibonacci-proxy sphere packing pending the ABCD solution. The leaf is explicit that this is an open problem.
  - Does NOT claim the ABCD reformulation will preserve the current Tier-C accuracy figures — when solved, it is expected to **replace** the current heuristic, and the current Tier-C $0.1$–$1.5\%$ residuals could shift in either direction.

> **Leaf references:** `framework/computational-mass-defect/abcd-transfer-matrix.md`.

---

## Semiconductor / Operating Regimes — Vol6-Specific Manifestation

The cross-cutting Symmetric vs Asymmetric Saturation entry (in `../claim-quality.md`) covers the universal $S$-kernel framing. Vol 6 specializes this into nuclear operating regimes.

- _Specific Claims_
  - Three regimes: Linear (Small Signal, $V \ll V_{\text{yield}}$, $\epsilon_{\text{eff}} \approx \epsilon_0$), Non-Linear (Large Signal, $V_{\text{yield}} \le V < V_{\text{snap}}$), Saturated (Breakdown, $V \ge V_{\text{snap}}$, $\epsilon_{\text{eff}} \to 0$).
  - Empirical Small/Large boundary at S-32 ($Z=16$): $V_R/V_{BR}$ jumps from $0.050$ (Si-28) to $0.994$ (S-32). Carbon through Silicon assemble exothermically; $^{28}\text{Si} + \alpha \to ^{32}\text{S}$ is endothermic by $\sim 75$ MeV (silicon-burning supernova condition).
  - Si-28 sitting at the Small/Large boundary ($V_R/V_{BR} = 0.050$, deep Small Signal but adjacent to the transition) is the framework's structural account of why silicon dominates microelectronics: stable in bulk, dynamically switchable.
- _Specific Non-Claims and Caveats_
  - The "natively explains why silicon is the dominant material in microelectronics" argument is a **structural / interpretive** claim. Does NOT claim a quantitative prediction of silicon's electronics properties (band gap, mobility, etc.) from $V_R/V_{BR} = 0.050$.
  - Does NOT claim the $\sim 75$ MeV endothermic figure for $^{28}\text{Si} + \alpha \to ^{32}\text{S}$ is AVE-derived — it is the empirical $Q$-value cited as evidence of the regime transition.
  - V_YIELD vs V_SNAP distinction is project-wide (LIVING_REFERENCE.md Critical Distinctions #1): V_SNAP $= 511$ kV (absolute destruction), V_YIELD $= 43.65$ kV (kinetic onset of nonlinearity). Vol 6 nuclear binding operates at $V_{BR} \approx 3.631$ MeV per alpha cluster, which is the **alpha-cluster internal Coulomb capacity**, not the lattice V_YIELD or V_SNAP. The three voltage scales (V_YIELD, V_SNAP, V_BR) live at different scales; reviewers should not conflate them.

> **Leaf references:** `framework/computational-mass-defect/operating-regimes.md`; `framework/computational-mass-defect/semiconductor-nuclear-analysis.md`; `period-3/silicon/symmetric-core-collapse.md`. Cross-cutting: Symmetric vs Asymmetric Saturation in `../claim-quality.md`; LIVING_REFERENCE.md Critical Distinctions #1.

---

## Bohr Radius and Rydberg Energy via Topological Hydrogen

The Hydrogen orbital-knot leaf derives $a_0 = \ell_{node}/\alpha \approx 5.291 \times 10^{-11}$ m and $E_0 = (1/2) m_e (\alpha c)^2 \approx 13.606$ eV from topological standing-wave conditions on the trefoil-electron / Borromean-proton system.

- _Specific Claims_
  - The values match empirical Bohr radius and Rydberg energy by direct substitution of Axiom 1 ($\ell_{node} = \hbar/(m_e c)$) and Axiom 2 ($\alpha$).
  - The standing-wave closure $n = 2\pi a_0 / \lambda_e \equiv 1$ is asserted as a classical wave-interference requirement, not a postulated angular-momentum quantization.
- _Specific Non-Claims and Caveats_
  - These derivations are **algebraic identities** within the AVE definitions of $\ell_{node}$ and $\alpha$; they follow by substitution. Treat as category (i) "identity" or category (iii) "consistency check via alternative mechanism," not as novel category-(iv) predictions.
  - LIVING_REFERENCE.md Pitfall #8 (QM Contamination — Bohr formula) is the relevant project-wide tripwire: the topological derivation here uses $E_k = (1/2) m_e (\alpha c)^2$, which is **algebraically equivalent** to the Bohr-formula Rydberg expression. The framework's claim is that the topological route arrives at the same number via classical LC standing-wave mechanics rather than via $E = Z_{\text{eff}}^2 \mathrm{Ry} / n^2$. Reviewers must not promote this single-element result into a general "AVE-derived ionization energies use the Bohr formula" reading — the multi-element solver explicitly rejects the Bohr formula (see "Period 1–3 Per-Element IE Accuracy" entry).
  - The "trefoil electron + Borromean proton" identification is structural; does NOT claim novel observables distinguishable from the standard Hydrogen atom in low-energy QM.

> **Leaf references:** `period-1/hydrogen/orbital-knot-topology.md`. Cross-cutting: LIVING_REFERENCE.md Pitfall #8.

---

## Notation Carryover: $\ell_{node}$ vs $l_{node}$ in Vol 6

Per CLAUDE.md INVARIANT-N2, Vol 6 source uses **roman ell** ($l_{node}$) as the primary form (not the script $\ell_{node}$ used in Vols 1–5). This is a notation convention, not a claim.

- _Specific Claims_
  - Vol 6 KB pages render $l_{node}$ as written in source. Any cross-volume quotation that appears with $\ell_{node}$ in vol6 leaves should be preserved as-is (do not normalize) — the volume-split is intentional per INVARIANT-N2.
- _Specific Non-Claims and Caveats_
  - Does NOT imply $l_{node}$ and $\ell_{node}$ are different physical quantities. They are the same lattice node spacing $\hbar/(m_e c) \approx 3.862 \times 10^{-13}$ m; only the typographic convention differs.
  - Reviewers checking summaries that quote Vol 6 results into Vol 1–5 contexts (or vice versa) should preserve source notation in each direction.

> **References:** CLAUDE.md INVARIANT-N2; vol6 leaves throughout (e.g., `framework/computational-mass-defect/semiconductor-nuclear-analysis.md` parameter table uses `L_NODE`).
