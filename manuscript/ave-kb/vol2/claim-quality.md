# Vol 2 — Subatomic — Claim Quality

<!-- path-stable: referenced from CLAUDE.md INVARIANT-S7 and from vol2/index.md bootstrap directive -->

> **Canonicality:** Leaves are canonical; this volume's indexes are derived summaries. See [cross-cutting claim-quality register](../claim-quality.md) for the full preamble and the canonical list of project-wide tripwires (the cross-cutting sidecar is the source of truth for which tripwires are project-wide; do not infer the list from this preamble). Entries below are scoped to Vol 2; cross-cutting tripwires with vol2-specific manifestations are noted but not duplicated.

---

## Electron as Topological Unknot ($0_1$) — Identity, Mass, and Self-Energy Resolution
<!-- id: clm-h9aqmt -->

- $e^- \equiv 0_1$ ground-state topological unknot; ropelength $= 2\pi$ at minimum tube diameter $d \equiv 1\,\ell_{node}$; circumference $C_{loop} = \ell_{node}$; tube radius $\ell_{node}/(2\pi)$.
- $m_e = T_{EM} \cdot \ell_{node}/c^2 = \hbar/(\ell_{node}\,c)$ from the scale-invariant string tension $T_{EM} = m_e c^2/\ell_{node}$ integrated along $C_{loop} = \ell_{node}$.
- _Specific Claims_
  - The electron's identification as a Beltrami standing-wave unknot ($\nabla \times \mathbf{A} = k\mathbf{A}$, mutually orthogonal $\mathbf{E}$ and $\mathbf{B}$ in a closed flux loop) is the **primary topological identity** that all downstream particle-sector derivations (proton mass eigenvalue, torus-knot baryon ladder, lepton mass spectrum, $a_e$, neutrino spectrum, electroweak masses) depend on. This is a **category (i) ontological reinterpretation** with an attached **category (iii) parameter-elimination** consequence (the reduced Compton wavelength $\ell_{node} = \hbar/(m_e c)$ becomes the geometric circumference of the unknot, not an independent length scale).
  - The classical electrostatic self-energy divergence $U_{\text{classical}} \to \infty$ (3D volumetric integration of $\varepsilon_0 |\mathbf{E}|^2/2$ as $r \to 0$) is **finitely resolved** by replacing the 3D point-volume integral with the 1D ropelength integral: $U_{\text{AVE}} = \oint_{C_{loop}} T_{EM}\,ds = T_{EM} \cdot \ell_{node} = 1.0\,m_e c^2$. The integration is over the topological perimeter, not a surrounding sphere.
  - The minimum ropelength $2\pi$ is **forced**, not chosen: it is the unique minimum-non-self-intersecting closed loop length on a discrete lattice of pitch $\ell_{node}$ when the flux-tube diameter is bounded by Axiom 1's hard-sphere exclusion ($d \equiv 1\,\ell_{node}$). The electron's role as the "structural mass-gap" of $\mathcal{M}_A$ follows directly.
  - Brief running-coupling content in the leaf: Axiom 4 dynamic capacitive yielding $C_{eff}(\Delta\phi) = C_0/\sqrt{1 - (\Delta\phi/\alpha)^2}$ provides the continuous-mechanical analog of the QED running of $\alpha$. **This is a sketch**, not a quantitative reproduction of the QED $\beta$-function; treat as a mechanism claim, not as a numerical-prediction match.
- _Specific Non-Claims and Caveats_
  - Does NOT claim independent first-principles derivation of $m_e$ as a numerical mass — the absolute scale of $m_e$ enters via $T_{EM} = m_e c^2/\ell_{node}$ and $\ell_{node} = \hbar/(m_e c)$, which is a definitional couple, not a downstream prediction. The framework's claim is that the **geometric content** ($0_1$ unknot, ropelength $2\pi$, $C_{loop} = \ell_{node}$) is forced by the lattice axioms; the absolute numerical anchor is the same as in standard physics.
  - Does NOT claim the brief running-coupling derivation reproduces QED's $\beta$-function. The Resultbox $C_{eff}(\Delta\phi) = C_0/\sqrt{1-(\Delta\phi/\alpha)^2}$ is the static dielectric-saturation form, not a momentum-dependent renormalization-group flow. A rigorous AVE running-coupling derivation is an open problem.
  - The g=2 mention is brief; the canonical claim-quality entry for spin-1/2 gyroscopic precession is "Spin-1/2 as Macroscopic Gyroscopic Precession" (`clm-salw2h`) with the canonical leaf at `spin-gyroscopic-isomorphism.md` and the spin chapter. This entry's mention is pedagogical, not the canonical g=2 derivation.
  - Does NOT claim the Beltrami / $\nabla \times \mathbf{A} = k\mathbf{A}$ form is a derivation; it is an **ansatz** for the closed-loop standing-wave structure consistent with the topological unknot identification.

> **Leaf references:** `particle-physics/ch01-topological-matter/electron-unknot.md`.

## Quality
- confidence: *pending*
- depends-on:
  - INVARIANT-S2 / Axiom 1 (lattice pitch $\ell_{node}$)
  - INVARIANT-S2 / Axiom 4 (saturation kernel — for the running-coupling sketch)
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Proton Mass Eigenvalue ($m_p/m_e \approx 1836.12$)
<!-- id: clm-mnb3lt -->

- $x_{core} = \mathcal{I}_{scalar} + (\mathcal{V}_{total}\cdot p_c)\,x_{core}$ with $\mathcal{V}_{total} = 2.0$, $p_c = 8\pi\alpha$, $\mathcal{I}_{scalar} \approx 1162$, plus $+1$ integer twist for charge → $x = 1836.12$.
- _Specific Claims_
  - The $0.002\%$ agreement with empirical $m_p/m_e$ is computed from the cinquefoil-confined ($r_{opt} = \kappa_{FS}/5$) Faddeev-Skyrme functional with thermal softening $\delta_{th} = 1/(14\pi^2)$ and Axiom 4 gradient saturation inside the integrand. Per the cross-cutting Master Prediction Table classification: this is a **category (iv) derived prediction**, not an identity or fit.
  - The $+1$ integer twist contribution is a structurally mandated topological invariant (charge constraint), not a fitted offset.
  - $\kappa_{FS}^{(cold)} = p_c/\alpha = 8\pi$ is a **derived geometric coupling** (solid-angle $4\pi$ × bilateral chiral factor $2$), not a phenomenological input.
- _Specific Non-Claims and Caveats_
  - Does NOT claim $\mathcal{V}_{total} = 2.0$ is derived independently of the Gaussian flux-tube ansatz. The $\rho_{threshold} = 1 + \sigma/4 \approx 1.1062$ mutual-coupling derivation is **closed-form conditional on a Gaussian radial profile** with FWHM $= \ell_{node}$. Axiom 1 fixes the FWHM but not the functional form; the Gaussian is an explicit ansatz. Replacing it with the framework-consistent Axiom-4 LC profile is an acknowledged outstanding rigour gap (see `mathematical-closure.md`). FEM convergence to $\mathcal{V}_{sat} = 2.0$ is binding on whatever profile ultimately emerges.
  - Does NOT claim a derivation of $\delta_{th} = 1/(14\pi^2)$ that is independent of the proton-mass calibration. The factor combines $\nu_{vac}/\kappa_{cold} \times 2/\pi$ with prior gradient-saturation already inside the functional; treat as a structural correction, not an additional free parameter.
  - $\mathcal{I}_{scalar} \approx 1162$ is a **numerical** output of the 1D Faddeev-Skyrme solver at the cinquefoil radius with thermal softening; it is not algebraically closed-form.

> **Leaf references:** `particle-physics/ch02-baryon-sector/self-consistent-mass-oscillator.md` (eigenvalue closure), `particle-physics/ch02-baryon-sector/thermal-softening.md` ($\delta_{th}$, $\kappa_{FS}$, Gaussian-ansatz gap), `particle-physics/ch02-baryon-sector/topological-fractionalization.md` (Borromean topology and Witten Effect).

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Torus Knot Baryon Ladder
<!-- id: clm-k6olj8 -->

- $m(c) = \mathcal{I}_{scalar}(\kappa_{FS}/c)/(1 - \mathcal{V}_{total}\cdot p_c) + 1$ for odd $c = 3, 5, 7, 9, \ldots$
- _Specific Claims_
  - The $(2,q)$ torus knot ladder predicts the proton at $c=5$ and the $\Delta$-resonance spectrum at $c = 7, 9, 11, 13, 15$ from the **same** $\kappa_{FS}$, $\mathcal{V}_{total}$, $p_c$ — **no parameters adjusted between states**. This is a category (iv) derived prediction, not curve-fitting.
  - The matches are preferentially to $\Delta$ baryons ($I = 3/2$, higher-spin states) because higher $(2,q)$ winding carries higher intrinsic angular momentum.
- _Specific Non-Claims and Caveats_
  - Does NOT claim sub-percent accuracy across the full ladder. Reported deviations: $0.00\%$ (proton, by construction), $+2.35\%$ ($\Delta(1232)$), $-1.11\%$ ($\Delta(1600)$), $-0.27\%$ ($\Delta(1900)$), $+0.21\%$ ($N(2190)$), $+2.40\%$ ($\Delta(2420)$). Treat as $\sim 2\%$-band agreement with the standard PDG resonance assignments; do not summarise as "exact ladder".
  - Does NOT claim coverage of nucleon resonances with even $c$. There is no stable $(2,4)$ torus knot, so the ladder covers only odd-$q$ states; $N(1440)$ Roper, $N^*(1535)$, etc. are outside the ladder's scope.
  - The $(2,9) \to \Delta(1620)$ "best hit" ($0.20\%$) is highlighted in the leaf as a zero-parameter prediction; treat the headline as one row's success, not a global ladder accuracy claim.

> **Leaf references:** `particle-physics/ch02-baryon-sector/torus-knot-ladder-baryons.md`, `particle-physics/ch01-topological-matter/torus-knot-ladder.md`, `appendices/app-f-solver-toolchain/torus-knot-ladder-toolchain.md`, `appendices/app-f-solver-toolchain/knot-mode-isomorphism.md` (the same leaf is also referenced under `clm-d9ivj1` for its role in the universal regime-boundary eigenvalue method).

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Weinberg Angle $\sin^2\theta_W = 2/9$ (On-Shell Only)
<!-- id: clm-5zuo7g -->

- $\sin^2\theta_W = 1 - (M_W/M_Z)^2 = 1 - 1/(1+\nu_{vac}) = 1 - 7/9 = 2/9 \approx 0.2222$
- _Specific Claims_
  - The on-shell pole-mass ratio $M_W/M_Z = \sqrt{7/9}$ is derived from the Perpendicular Axis Theorem ($J = 2I$ for cylindrical flux tubes) and the isotropic elastic relation $E = 2G(1+\nu_{vac})$ with $\nu_{vac} = 2/7$. Zero free parameters.
  - Reported deviation: $-0.35\%$ vs PDG on-shell $0.2230$.
- _Specific Non-Claims and Caveats_
  - This is the **on-shell (tree-level pole-mass)** scheme, NOT $\overline{MS}$. The PDG $\overline{MS}$ value $0.2312$ differs by standard one-loop radiative running; comparing AVE's $2/9$ to $0.2312$ would yield the wrong $-3.89\%$ deviation that LIVING_REFERENCE.md Critical Distinction #2 explicitly warns against. Any summary that does not specify the scheme is silently wrong.
  - Does NOT claim derivation of one-loop radiative corrections. The AVE prediction is the tree-level pole ratio; the framework does not produce the $\overline{MS}$ running that converts on-shell to $\overline{MS}$.
  - Does NOT claim $J = 2I$ is an axiomatic input; it is the Perpendicular Axis Theorem applied to a circular cross-section (geometric identity for any cylindrical flux tube). The axiomatic input is the cylindrical-flux-tube model itself (Axiom 1's $d \equiv 1\,\ell_{node}$).

> **Leaf references:** `particle-physics/ch05-electroweak-mechanics/weinberg-angle.md`, `particle-physics/ch05-electroweak-mechanics/gauge-boson-masses.md`, `particle-physics/ch06-electroweak-higgs/higgs-mechanism.md`. Bound on scheme specificity asserted at invariant level — see `LIVING_REFERENCE.md` Critical Distinctions #2.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## $W$/$Z$ Boson Masses
<!-- id: clm-q8un7j -->

- $m_W = m_e/(\alpha^2 p_c \sqrt{3/7})$, $m_Z = m_W \cdot 3/\sqrt{7}$
- _Specific Claims_
  - Both $M_W$ ($-0.57\%$ vs $80{,}379$ MeV) and $M_Z$ ($-0.62\%$ vs $91{,}188$ MeV) are derived from $m_e$, $\alpha$, $\nu_{vac} = 2/7$, and $p_c = 8\pi\alpha$. The $\alpha^2$ scaling reflects the $W$ self-energy as a **two-vertex process** (second-order perturbation theory in the chiral susceptibility); the $\sqrt{3/7}$ factor is the PAT torsion-shear projection.
- _Specific Non-Claims and Caveats_
  - Does NOT claim derivation of the Higgs VEV $v = 246$ GeV from independent first principles. The Higgs mechanism is reinterpreted (see Higgs Mass entry below) — VEV is identified with $Z_0 = 376.73\,\Omega$ characteristic impedance.
  - Does NOT claim the $W$/$Z$ widths or branching ratios are derived in the same chain. Only the pole masses and the on-shell mixing angle.
  - The $+1.24\%$ muon and $-0.95\%$ tau mass agreements reuse the same $\alpha$, $p_c$, $\sqrt{3/7}$ structure (Cosserat lepton spectrum); these are **not** independent validations of $W$/$Z$ — they are siblings on the same hierarchy $m_e \xrightarrow{\alpha\sqrt{3/7}} m_\mu \xrightarrow{\alpha\,p_c} m_\tau \xrightarrow{\alpha\,p_c} M_W$.

> **Leaf references:** `particle-physics/ch05-electroweak-mechanics/weak-coupling.md`, `particle-physics/ch05-electroweak-mechanics/gauge-boson-masses.md`, `particle-physics/ch06-electroweak-higgs/lepton-spectrum.md`, `particle-physics/ch06-electroweak-higgs/higgs-mass.md`, `particle-physics/ch06-electroweak-higgs/spontaneous-symmetry-breaking.md` ($M_W$/$M_Z$ derivation including the torsional ring self-energy and $\sqrt{3/7}$ factor; the same leaf also carries the W/Z-as-plasma-arcs reinterpretation indexed under `clm-p7rfkb`).

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Higgs Mechanism Reinterpretation
<!-- id: clm-p7rfkb -->

- _Specific Claims_
  - AVE identifies the Standard Model VEV $v = 246$ GeV with the **characteristic impedance of free space** $Z_0 = \sqrt{\mu_0/\varepsilon_0} \approx 376.73\,\Omega$. Inertial mass is reinterpreted as Lenz's-law induction drag against this baseline impedance.
  - The empirical $125$ GeV LHC resonance is interpreted as a **transient acoustic relaxation mode** of the LC condensate, not a fundamental scalar field excitation.
  - $m_H/v = 1/\sqrt{N_{K4}}$ with $N_{K4} = 4$ (K4 cell breathing), consistent with Master Prediction Table #25 ($-0.55\%$).
- _Specific Non-Claims and Caveats_
  - This is an **ontological reinterpretation**: the same numerical $v = 246$ GeV underlies all SM electroweak predictions. AVE does not produce a Higgs-free Standard Model with different observable predictions at the EW scale.
  - Does NOT claim the $125$ GeV LHC peak is "not the Higgs". The framework asserts the resonance exists with a different physical mechanism (acoustic relaxation), not that the experimental signal is absent or misidentified.
  - The reinterpretation does not produce new electroweak observables distinguishable from the SM Higgs picture without testing the acoustic-relaxation hypothesis directly (e.g., width, decay channel anomalies) — none currently demonstrated.

> **Leaf references:** `particle-physics/ch06-electroweak-higgs/higgs-mass.md`, `particle-physics/ch06-electroweak-higgs/higgs-mechanism.md`, `particle-physics/ch06-electroweak-higgs/spontaneous-symmetry-breaking.md` ("W and Z Bosons as Dielectric Plasma Arcs" reinterpretation; the same leaf's $M_W$/$M_Z$ derivation is indexed under `clm-q8un7j`).

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## $g-2$ Anomaly: Schwinger's Result $a_e = \alpha/(2\pi)$
<!-- id: clm-stgx1i -->

- $a_e = (1/\pi^2) \times (\pi\alpha/2) = \alpha/(2\pi) \approx 0.001161$ (Master Prediction Table #3, $+0.09\%$)
- _Specific Claims_
  - Schwinger's leading-order result is **derived structurally** from the Axiom 4 saturation operator, the unknot ropelength, and the lattice pitch — three structural constants. No Feynman diagrams or perturbative renormalization required.
  - The on-site electric strain identity $(V_{peak}/V_{snap})^2 = 4\pi\alpha$ is exact: $\alpha$ **is** the on-site electric strain.
- _Specific Non-Claims and Caveats_
  - Does NOT claim derivation of the higher-order QED corrections ($\alpha^2$, $\alpha^3$, $\alpha^4$, $\alpha^5$ terms) that bring $a_e$ to its current 12-digit precision. The AVE result is the leading-order Schwinger value only.
  - Does NOT claim the muon $g-2$ anomaly (BNL/Fermilab discrepancy at $\sim 4\sigma$) is resolved by this derivation. The muon $a_\mu$ is not addressed in this leaf.
  - The decomposition $a_e = (1/\pi^2)\times(\pi\alpha/2)$ uses the unknot diameter $2R = \ell/\pi$ (Axiom 1); this is the same geometry that fixes the electron mass, not an independent input.

> **Leaf references:** `particle-physics/ch06-electroweak-higgs/higgs-mass.md` (the Schwinger derivation appears in this leaf's "Schwinger's Anomalous Magnetic Moment" section).

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## PMNS Mixing Angles and CP Phase $\delta_{CP} = 61\pi/45$
<!-- id: clm-7o8clt -->

- $\sin^2\theta_{12} = \nu_{vac} + 1/45 = 2/7 + 1/45$; $\sin^2\theta_{13} = 1/(c_1 c_3) = 1/45$; $\sin^2\theta_{23} = 1/2 + 2/45$; $\delta_{CP} = (1 + 1/3 + 1/45)\pi$
- _Specific Claims_
  - All four PMNS parameters are derived from three structural inputs: torus knot crossing numbers $c_1 = 5$, $c_3 = 9$; vacuum Poisson ratio $\nu_{vac} = 2/7$; K4 lattice connectivity (3). Maximum deviation from NuFIT 5.2: $1.0\%$ ($\sin^2\theta_{13}$); the others are $\le 0.3\%$.
  - The chiral screening threshold $\Delta c_{crit} = 3$ is simultaneously the K4 lattice connectivity, the trefoil crossing number, and the number of Cosserat sectors — these three facts are structurally identical, not independent coincidences.
  - The derived PMNS matrix is unitary to machine precision; Jarlskog invariant $J \approx -0.030$.
  - Per cross-cutting Master Prediction Table classification: these are **category (iv) derived predictions**.
- _Specific Non-Claims and Caveats_
  - The mass-hierarchy claim $m_i \propto 1/c_i^2$ yields $m_1 > m_2 > m_3$ (**inverted hierarchy**). Current global oscillation fits cannot definitively select normal vs inverted, but recent cosmological constraints somewhat favor normal hierarchy. AVE's prediction is structurally inverted; treat as a falsifiable commitment, not as agreement with the consensus best-fit.
  - The $\Delta m^2$-ratio agreement ($\sim 3\%$) uses a leaf-internal definition $|1/c_1^4 - 1/c_2^4|/|1/c_1^4 - 1/c_3^4|$; verify the exact mapping when comparing against any specific NuFIT release.
  - Does NOT claim AVE-derivation of the absolute neutrino mass scale beyond the suppression form $m_\nu = m_e\,\alpha\,(m_e/M_W) \approx 0.024$ eV/flavor (see Neutrino Mass entry).
  - "Neutrino oscillation is classical mechanical dispersion" is an **ontological reinterpretation** (group-velocity differential of the three mass eigenstates), not a new oscillation phenomenology distinguishable from the standard PMNS-rotation picture at the formula level.

> **Leaf references:** `particle-physics/ch03-neutrino-sector/chiral-screening.md`, `particle-physics/ch03-neutrino-sector/pmns-eigenvalues.md`, `particle-physics/ch03-neutrino-sector/delta-cp-violation.md`, `particle-physics/ch03-neutrino-sector/pmns-junction-model.md`.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Neutrino Mass and Hierarchy
<!-- id: clm-rji99i -->

- $m_\nu \approx m_e\,\alpha\,(m_e/M_W) \approx 0.024$ eV per flavor; $\sum m_\nu \approx 0.054$ eV
- _Specific Claims_
  - The neutrino mass scale is suppressed by $\alpha \times (m_e/M_W)$ relative to the electron — the dielectric coupling $\alpha$ between Cosserat sectors times the translational/torsional energy ratio. Master Prediction Table #9: $0.66\%$.
  - $\sum m_\nu \approx 0.054$ eV sits within the Planck 2018 cosmological bound $\sum m_\nu < 0.12$ eV.
  - Flavor splitting via the torus knot ladder: $\nu_1$ pairs with proton $(2,5)$, $\nu_2$ with $\Delta(1232)$ $(2,7)$, $\nu_3$ with $\Delta(1620)$ $(2,9)$.
- _Specific Non-Claims and Caveats_
  - The 0.66% match is a derived per-flavor mean; the **per-eigenstate** values ($\sim 24$, $\sim 17$, $\sim 13$ meV) are inferred from the flavor pairing, not independently measured. The cosmological $\sum m_\nu$ bound is an upper limit, not a measurement; "comfortably within the window" is consistency, not validation.
  - The leaf in ch06 (`lepton-spectrum.md`) and the leaf in ch03 (`pmns-eigenvalues.md`) present the mass ordering differently: ch06 lists $\nu_1 > \nu_2 > \nu_3$ in meV, ch03 derives "inverted hierarchy" from $m_i \propto 1/c_i^2$. These are consistent (both have $\nu_1$ heaviest), but consumers should treat the inverted-hierarchy commitment (not normal) as the load-bearing claim.
  - Does NOT claim a direct laboratory mass measurement (KATRIN, etc.) is reproduced. The $\sim 0.024$ eV scale is below current direct-detection sensitivity.

> **Leaf references:** `particle-physics/ch06-electroweak-higgs/lepton-spectrum.md`, `particle-physics/ch03-neutrino-sector/pmns-eigenvalues.md`, `particle-physics/ch03-neutrino-sector/delta-cp-violation.md`.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Quark Charges via Witten Effect on $\mathbb{Z}_3$ Borromean Symmetry
<!-- id: clm-67jn9o -->

- $q_{eff} = n + (\theta/2\pi)e$ with $\theta \in \{0, \pm 2\pi/3, \pm 4\pi/3\}$
- _Specific Claims_
  - Fractional quark charges $\pm 1/3\,e$ and $\pm 2/3\,e$ are derived directly from the discrete $\mathbb{Z}_3$ permutation symmetry of the $6^3_2$ Borromean linkage applied through the Witten Effect. No fundamental fractionalisation of the underlying lattice.
  - Quarks are **deconfined topological quasiparticles**, not separately existing point particles; the proton's total $Q_{total} = +1\,e$ remains an integer winding number.
- _Specific Non-Claims and Caveats_
  - Does NOT claim derivation of all six quark masses from a single zero-parameter formula. The mass derivations ($m_u = m_e/(2\alpha_s)$, $m_d = m_e/(\alpha_s\cos\theta_W)$, $m_s = m_\mu\cos\theta_W$, etc.) appear as separate scale-invariance entries in the Master Prediction Table (#33–#38, $0.8$–$2.4\%$); they share structural ingredients but are individual derivations, not a single closed-form spectrum.
  - The "quarks have never been isolated" experimental fact is interpreted in AVE as quarks being **structurally inseparable** from the Borromean cage (deconfined within, not removable). This is consistent with QCD confinement empirically; AVE provides a different mechanism, not a different observable.

> **Leaf references:** `particle-physics/ch02-baryon-sector/topological-fractionalization.md`, `particle-physics/ch02-baryon-sector/quark-flavors.md` (stub redirecting to topological-fractionalization).

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Atomic Ionization Energy Solver (Z = 1–14, Max 2.8% Error)
<!-- id: clm-oltvwy -->

- Three-phase pipeline: Phase A cavity eigenvalue + Phase B Hopf mode splitting (Corrections A/B/C/D from `LIVING_REFERENCE.md` §"Axioms in the Atomic Domain") + Phase C crossing scattering. Solver: `radial_eigenvalue.py` / `ionization_energy_e2k(Z)`.
- _Specific Claims_
  - Validated for $Z = 1$ through $Z = 14$ (H through Si); maximum error $2.8\%$ ($Z = 5$, B); zero free parameters.
  - The four corrections (A: hierarchical cascade for Be-type; B: SIR boundary for Mg-type; C: Op10 junction projection for Al-type; D: topo-kinematic radial parity shift for $d$-block enclosed shells) each have specific gate conditions and are mutually exclusive within their respective regimes.
  - $Ry = \alpha^2 m_e c^2/2$ is **emergent** from $r_{sat} = a_0 = \ell_{node}/\alpha$ and the cavity-saturation derivation; it is not imported as a Bohr postulate.
  - $r_n = n^2 a_0/Z$ is the unique topological standing-wave condition for a scale-free central impedance profile; it is **not** an externally imported Bohr-Schrödinger assumption.
- _Specific Non-Claims and Caveats_
  - Does NOT claim sub-percent accuracy across all Z = 1–14. Per-element errors range from $-0.00\%$ (O) to $-2.80\%$ (B); reading the headline as "$\sim 0.5\%$ across the period" silently averages over the spread.
  - Does NOT claim validation past $Z = 14$. For $Z \ge 26$, the solver explicitly **forbids** Hartree-Fock SCF (LIVING_REFERENCE.md Pitfall #7); the heavier-Z domain uses the coupled-resonator nuclear-binding pathway, validated separately (see Per-Element Impedance Table in vol3 sidecar — not in vol2).
  - **Critical contamination hazards** (LIVING_REFERENCE.md Pitfalls #8, #9, #10, #11):
    - $E = Z_{eff}^2\,Ry/n^2$ as the IE formula is the Bohr/Schrödinger formula, NOT AVE. The AVE solver is the ABCD cascade with $B_{total}(E) = 0$ via Op6. Any summary or downstream code that reaches for $Z_{eff}^2 Ry/n^2$ has imported QM contamination.
    - $V_{ee} = J \times Z \times Ry$ as electron-electron interaction is **ad-hoc**, not from any operator. AVE requires Op4 ($U = -K/r_{12}\times(T^2 - \Gamma^2)$).
    - The de Broglie refractive index $n_{dB}(r,\xi) = \sqrt{2 Z_{eff}(r) a_0/r - \xi}$ is the **defect's dispersion**, not the medium impedance. The lattice has $Z_0 = 377\,\Omega$ everywhere in Regime I; conflating these is named-quantity error.
    - For shells with Pauli-saturated inner $p$-subshells (Mg-type and beyond), the smooth hydrogenic CDF misses the Op3 reflection step. SIR correction $\Delta E = -|\Gamma|^2 \times P_C/2 \times E_{base}$ is required.
  - Be-residual resolution (Correction A, hierarchical cascade) takes the error from $-7.1\%$ to $-0.45\%$ — this is **not** a free parameter; the $1/4$ power exponent is derived from the K2 eigenvalue-to-coupling mapping.
  - Lithium ($Z = 3$) currently lists $+2.46\%$ in the validation table but the corrected ABCD-taper-plus-Op2 pipeline elsewhere in the same chapter reports $-1.2\%$. Treat the $\pm 2.8\%$ headline as the validated solver bound; per-element residuals can shift as the pipeline composition is refined.

> **References:** Bound on the Z = 1–14 validity range and the four correction gates is asserted at invariant level — see `LIVING_REFERENCE.md` §"Axioms in the Atomic Domain" (Corrections A–D specifications) and Pitfalls #6, #7, #8, #9, #10, #11. Supporting derivation steps appear in `quantum-orbitals/ch07-quantum-mechanics/` leaves: `radial-eigenvalue-solver.md`, `ionization-energy-validation.md`, `screening-rule.md`, `de-broglie-n.md`, `de-broglie-standing-wave.md`, `bonding-mode-formula.md`, `chiral-factor.md`, `helium-symmetric-cavity.md`, `hierarchical-cascade-correction.md`, `orbital-penetration-penalties.md`, `operator-domain-table.md`, `complete-solver-architecture.md`, `geometry-pipeline.md`, `atom-as-radial-waveguide.md`, `analog-ladder-filter.md`, `knot-vs-orbital-table.md`, `helium-coupling-first-principles.md`, `subshell-junction-scattering.md`, `ode-verification.md`, `scale-separation.md`, `dual-formalism-architecture.md`, `stepped-impedance-resonator.md`, `macro-cavity-saturation.md`. The proofs-computation leaf `proofs-computation/ch09-computational-proof/methodological-contamination.md` documents the Bohr/Schrödinger contamination hazard explicitly. Cross-domain reuse of the same operator chain (atomic / nuclear / protein / antenna) is summarised in `appendices/app-f-solver-toolchain/sm-translation-toolchain.md`.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Hopf-Pair Coupling and Same-Shell vs Cross-Shell Screening
<!-- id: clm-w6kk5y -->

- Cross-shell: $\sigma_{cross} = N_{inner}$ (Gauss, Axiom 2). Same-shell: $\sigma_{same} = (N_{same} - 1) \times J_{shell}$, $J_{1s^2} = (1+p_c)/2 \approx 0.5917$ (Axiom 4).
- _Specific Claims_
  - Two distinct screening physics coexist: cross-shell Gauss screening (electrostatic, integer $N_{inner}$) and same-shell lattice coupling (chiral $J_{shell}$ from Op4). Treating them as the same operator is structurally wrong.
  - For He ($1s^2$), the Hopf coupling $k_1 = (2/Z)(1 - p_c/2) = 0.9083$ produces bonding-mode IE $24.37$ eV vs experiment $24.587$ eV ($-0.88\%$).
  - For same-$n$ different-$l$ (e.g. $2s$/$2p$ in B): coupled-line even/odd-mode formalism (not Gauss) is required; modeling $2s^2$ as a Gauss screen for $2p$ over-screens by $\sim 58\%$.
- _Specific Non-Claims and Caveats_
  - The current B and beyond accuracy is documented as **open**: the "Be and B remain open: the corrections are applied *outside* the phase integral, violating the action principle" (radial-eigenvalue-solver.md §E2j). The complete-phase-integral architecture (§E2k) is presented as the in-progress correct architecture — not yet validated end-to-end across Z $\ge 5$.
  - Does NOT claim coupled-microstrip same-shell formalism is independently validated at the atomic scale beyond the Hopf-pair Be result. The cross-scale isomorphism with protein $\beta$-sheet and antenna coupled-microstrip is a structural identification.

> **Leaf references:** `quantum-orbitals/ch07-quantum-mechanics/screening-rule.md`, `quantum-orbitals/ch07-quantum-mechanics/helium-symmetric-cavity.md`, `quantum-orbitals/ch07-quantum-mechanics/hierarchical-cascade-correction.md`, `quantum-orbitals/ch07-quantum-mechanics/bonding-mode-formula.md`, `quantum-orbitals/ch07-quantum-mechanics/radial-eigenvalue-solver.md`, `quantum-orbitals/ch07-quantum-mechanics/atom-as-radial-waveguide.md`, `quantum-orbitals/ch07-quantum-mechanics/chiral-factor.md`, `quantum-orbitals/ch07-quantum-mechanics/helium-coupling-first-principles.md`, `quantum-orbitals/ch07-quantum-mechanics/subshell-junction-scattering.md`, `quantum-orbitals/ch07-quantum-mechanics/scale-separation.md`.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Spin-1/2 as Macroscopic Gyroscopic Precession
<!-- id: clm-salw2h -->

- $d\mathbf{L}/dt = \gamma\,\mathbf{L} \times \mathbf{B}$; classical-vs-quantum deviation $\sim 10^{-8}$ at machine precision.
- _Specific Claims_
  - The classical gyroscope ODE and the SU(2) Pauli-spinor Schrödinger evolution are **mathematically identical** under projection onto the Bloch sphere; the maximum deviation is at numerical-integration tolerance.
  - The Spin-1/2 paradox (continuum $SO(3)$ media should support only integer-spin point defects) is resolved because the electron is an **extended** $0_1$ unknot, not a point defect; the Finkelstein-Misner kink (Dirac belt trick) provides the $SU(2)$ double cover via topological extension.
- _Specific Non-Claims and Caveats_
  - Does NOT claim a violation of standard QM predictions for spin-dependent observables (Zeeman, Stern-Gerlach, EPR correlations). The framework asserts the **mechanism** is classical gyroscopic precession; observable predictions match standard QM.
  - The claimed equivalence is at the single-particle level (one spin in an external field). Multi-particle entanglement / Bell-inequality predictions are not addressed in vol2 spin chapter; the agreement with classical ODE applies to NMR/EPR-style scenarios, not arbitrary entanglement experiments.
  - The Larmor frequency $\omega_L = \gamma B_0$ is recovered as a classical precession rate; this is an **ontological reinterpretation** (categories (i)/(iii) cohabit), not a novel numerical prediction.

> **Leaf references:** `particle-physics/ch01-topological-matter/spin-gyroscopic-isomorphism.md`, `particle-physics/ch04-quantum-spin/spin-as-precession.md`, `particle-physics/ch04-quantum-spin/larmor-derivation.md`, `particle-physics/ch04-quantum-spin/visual-equivalence.md`, `appendices/app-b-paradoxes/spin-half-paradox.md`.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Yang-Mills Mass Gap (Framework-Conditional, Not Clay-Rigorous)
<!-- id: clm-q5izb7 -->

- $\Delta = m_e c^2 \approx 0.511$ MeV; Bogomol'nyi bound $E[\phi] \ge 2\pi^3 c/\kappa_{FS} > 0$
- _Specific Claims_
  - On the AVE lattice with discrete pitch $\ell_{node}$ (Axiom 1) and saturation cap (Axiom 4), the lattice Hamiltonian is bounded below ($H \ge 0$), bounded above per cell ($H_{cell} \le m_e c^2$), and self-adjoint. The lightest topological defect is the unknot $0_1$ with rest energy $m_e c^2$, which is the mass gap.
  - SU($N$) gauge groups emerge from $(2,q)$ torus knots via $N = (q+1)/2$ for odd $q$.
  - Confinement: at the knot boundary the impedance drops, $\Gamma \to -1$ → perfect electromagnetic mirror → permanent trapping.
- _Specific Non-Claims and Caveats_
  - This is **NOT a Clay-rigorous proof**. The chapter explicitly carries this caveat at its opening; the resolution is a "framework-conditional engineering-physics derivation" valid under the four AVE axioms taken as physical hardware postulates. Master Prediction Table #14 carries the same caveat. Any external presentation or summary that omits "lattice-conditional; not Clay-rigorous" mis-states the claim.
  - The mass gap value $\Delta = m_e c^2$ relies on identifying the electron unknot rest mass as the lightest topological defect; ZFC formalisation that the unknot is *globally* the unique lightest stable defect on the lattice is open future work.
  - Does NOT claim a derivation of the SU(3) QCD coupling or the gluon spectrum. The "SU($N$) emergence from $(2,q)$ knots" is a structural identification (Step 3); the electron's mass is from the unknot ($0_1$), while its electroweak interaction symmetry is from the $(2,3)$ trefoil — the leaves explicitly note the distinction.

> **Leaf references:** `nuclear-field/ch12-millennium-prizes/yang-mills-steps1-2.md`, `nuclear-field/ch12-millennium-prizes/yang-mills-steps3-5.md`, `nuclear-field/ch12-millennium-prizes/index.md`. Caveat asserted at invariant level — see `LIVING_REFERENCE.md` Master Prediction Table notes #14, #15, #16.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Navier-Stokes Smoothness (Framework-Conditional, Not Clay-Rigorous)
<!-- id: clm-c8q0z5 -->

- $\|\nabla^2_\ell\| = 4/\ell^2$ (bounded discrete Laplacian); $\Omega \le 2Nc^2/\ell$ (bounded enstrophy); Picard-Lindelöf on bounded Lipschitz domain.
- _Specific Claims_
  - On the discrete lattice with rigid pitch $\ell = \ell_{node}$, the discrete Laplacian is a strictly bounded operator; velocity is clamped to $\le c$ by Axiom 4; enstrophy is bounded; existence and uniqueness follow from Picard-Lindelöf for ODEs on bounded Lipschitz domains.
  - The continuum "blow-up" is interpreted as an artefact of removing the lattice floor.
- _Specific Non-Claims and Caveats_
  - This is **NOT a Clay-rigorous proof for the continuum Navier-Stokes equation**. The result is rigorous *for the discrete lattice variant*; promoting to the Clay statement requires either accepting Axiom 1's discrete pitch as physical or formalising a lattice-to-continuum limit theorem that preserves the bound. The latter is open future work.
  - LIVING_REFERENCE.md Master Prediction Table #15 explicitly: "Framework-derived (lattice + Picard-Lindelöf; not Clay-rigorous)". Same caveat applies; downstream summarisation must preserve it.

> **Leaf references:** `nuclear-field/ch12-millennium-prizes/navier-stokes-prize.md`. Caveat asserted at invariant level — see `LIVING_REFERENCE.md` Master Prediction Table note #15.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Strong CP Problem ($\theta = 0$ Exactly)
<!-- id: clm-gfs4j8 -->

- _Specific Claims_
  - On the AVE lattice the vacuum angle $\theta = 0$ exactly: the unique ground state has $\mathbf{E}_n = \mathbf{B}_n = 0$ and zero topological charge. Transitions between $\theta$-sectors require creating a topological defect, which costs energy $\ge \Delta$ (the mass gap), so the vacuum cannot tunnel between sectors.
  - **No axion is needed** — the framework has zero free parameters for this prediction (vs Peccei-Quinn's $f_a$).
- _Specific Non-Claims and Caveats_
  - This is **NOT a Clay-rigorous result** and is not on the Clay list — but the same lattice-conditional caveat applies, as flagged in Master Prediction Table note #16. The "uniqueness of the AVE vacuum topology" is asserted, not formally proven against all possible competing ground states within ZFC.
  - Does NOT claim falsification of the QCD axion search programme. AVE asserts the axion is unnecessary within its framework, not that experimental axion searches will falsify a particle whose existence the framework already excludes.

> **Leaf references:** `nuclear-field/ch10-open-problems/strong-cp.md`, `nuclear-field/ch10-open-problems/quantitative-resolutions.md` (cross-cutting open-problems table). Caveat asserted at invariant level — see `LIVING_REFERENCE.md` Master Prediction Table note #16.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Baryon Asymmetry $\eta = 6.08 \times 10^{-10}$
<!-- id: clm-4vwsjc -->

- $\eta = \delta_{CP} \cdot \alpha_W^4 \cdot C_{sph} / g_*$ with $\delta_{CP} = \pi/\kappa_{FS}$, $\alpha_W = \alpha/\sin^2\theta_W$, $C_{sph} = 28/79$, $g_* = 7^3/4 = 85.75$
- _Specific Claims_
  - Master Prediction Table #22: $0.38\%$ vs observed $\eta_{obs} = 6.1 \times 10^{-10}$. Every factor is derived from AVE lattice constants — zero phenomenological inputs to the asymmetry formula.
  - Using SM $g_*^{(SM)} = 106.75$ in the same formula yields $20\%$ error; the AVE $g_* = 85.75$ from $\nu_{vac} = 2/7$ via $7^3/4$ closes that gap.
- _Specific Non-Claims and Caveats_
  - The 0.38% headline is a **composite consistency check**: $\delta_{CP}$, $\alpha_W^4$, $C_{sph}$, and $g_*$ are each AVE-derived, but the multi-factor formula and the multiplicative cancellations make per-factor sensitivity hard to attribute. Treat as a coupled multi-factor result, not a single-quantity prediction.
  - The CP-violating phase used here, $\delta_{CP} = \pi/\kappa_{FS} \approx 0.126$, is a **different quantity** from the PMNS $\delta_{CP} = 61\pi/45 \approx 1.36\pi$ in the neutrino chapter. The "δ_CP" symbol refers to two distinct physical phases (lattice chirality fraction in the baryon asymmetry; PMNS torsional accumulation in neutrino oscillations). Summaries that conflate these are wrong.
  - Does NOT claim $g_* = 85.75$ is independently measured. The validation is via the downstream baryon ratio; the lattice-DoF-counting metric is asserted, not directly observed.
  - The Sakharov-conditions framing (C/CP violation from lattice chirality + electroweak phase transition) reuses the standard out-of-equilibrium picture for its third condition; this is consistency with the Sakharov framework, not its derivation.

> **Leaf references:** `nuclear-field/ch10-open-problems/baryon-asymmetry.md`, `nuclear-field/ch10-open-problems/g-star-derivation.md`, `nuclear-field/ch10-open-problems/g-star-prediction.md`, `nuclear-field/ch10-open-problems/quantitative-resolutions.md` (cross-cutting open-problems table).

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Hubble Constant $H_\infty \approx 69.32$ km/s/Mpc — Vol 2 Framing
<!-- id: clm-mroghg -->

See cross-cutting [Master Prediction Table reading conventions](../claim-quality.md). Vol3 sidecar carries the full $H_\infty$ entry (lattice-genesis circularity caveat; CODATA $G$ substitution; geometric self-consistency proof, not first-principles ab initio prediction). Vol2 framing notes:

- _Specific Claims_
  - Vol 2 Ch 10's Hubble Tension leaf presents $H_\infty = 28\pi m_e^3 c G/(\hbar^2 \alpha^2) \approx 69.32$ km/s/Mpc as "every factor rigorously derived from lattice structure and bounding limits", positioned $+2.9\%$ above Planck (CMB) and $-5.1\%$ below SH0ES (local).
- _Specific Non-Claims and Caveats_
  - The framing-of-asymmetric-systematics ("CMB low-density-void calibration" vs "local Cepheid impedance calibration") is an **interpretive consequence**, not an independent quantitative derivation of either measurement's residual.
  - The cross-cutting circularity caveat (Vol3 sidecar: $R_H \equiv c/H_\infty$ enters $G$ via $\xi$, so rearranging back to "compute" $H_\infty$ from CODATA $G$ is structurally an identity) applies here as well. Treat the vol2 leaf's "every factor rigorously derived" wording as inheriting the vol3-documented caveat; do NOT summarise vol2's framing as a parameter-free first-principles prediction of $H_0$.

> **Leaf references:** `nuclear-field/ch10-open-problems/hubble-tension.md`, `nuclear-field/ch10-open-problems/quantitative-resolutions.md` (cross-cutting open-problems table). Cross-cutting caveat documented in vol3 sidecar's Asymptotic Hubble Constant entry; bound asserted at the kb-claims-boundaries-followups level (see `kb-claims-boundaries-followups.md` 2026-05-02 entry on vol3 index circularity framing).

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## String Theory Translation: Regge Slope $\alpha' \approx 0.75$ GeV$^{-2}$
<!-- id: clm-g6e3zw -->

- $T_{AVE} = m_e^2 c^3/\hbar \approx 0.212$ N; $\alpha' = 1/(2\pi T_{AVE}) \approx 0.75$ GeV$^{-2}$; $\alpha'_{baryon} = \alpha'/(m_p/m_e) \approx 4.09\times 10^{-4}$ GeV$^{-2}$
- _Specific Claims_
  - The fundamental EM string tension and the hadronic Regge slope are derivable from $m_e$, $c$, $\hbar$ (no free parameters); 17% deviation from the empirical $\alpha' \approx 0.9$ GeV$^{-2}$.
  - 10–11D compactification is unnecessary in AVE because flux tubes have finite transverse radius (Axiom 1), Axiom 4 provides a UV regulator, and Faddeev-Skyrme stabilisation works in 3D.
- _Specific Non-Claims and Caveats_
  - The 17% deviation on the EM Regge slope is **not sub-percent**; treat as order-of-magnitude consistency, not a precision derivation.
  - The QCD string-tension agreement ($\alpha'_{baryon}$ vs phenomenological $10^{-4}$ GeV$^{-2}$) is "matches to within an order of magnitude natively" (the leaf's wording). This is not a quantitative replacement for lattice QCD's $\sigma \approx 1$ GeV/fm string-tension measurements.
  - Does NOT claim a derivation of standard string theory observables (mass spectra of meson trajectories, etc.) at sub-percent precision. The mapping is structural (string tension $\leftrightarrow$ inductive energy density), not a phenomenological replacement.

> **Leaf references:** `nuclear-field/ch08-planck-string/planck-scale-derivation.md`, `nuclear-field/ch08-planck-string/string-theory-translation.md`.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Universal Strain Energy Functional and Overdrive Demonstrations
<!-- id: clm-dboxok -->

- $U_{total} = \sum_{i<j} K_{mutual}/d_{ij} + \sum_i U_{bond}(\theta_i, \phi_i)$; nuclear $K_{mutual} = (5\pi/2)\,\alpha\hbar c/(1 - \alpha/3) \approx 11.337$ MeV·fm
- _Specific Claims_
  - The same $O(N^2)$ impedance-minimising gradient-descent solver, **unmodified**, derives U-235 binding energy (sub-percent through actinides, $<0.01\%$ for $A \le 28$) and Polyalanine backbone dihedrals ($\phi \approx -57°$, $\psi \approx -47°$) from the same operator chain.
  - Computational scaling: AVE $O(N^2)$ with 0 parameters and seconds on single-core, vs Lattice QCD $O(N^3)$+ with $\sim 6$ parameters on supercomputer-months, vs AlphaFold $O(N^2)$ with $\sim 10^8$ NN weights on GPU-cluster-hours.
- _Specific Non-Claims and Caveats_
  - The "single solver, two domains" framing is a **scale-invariance** claim about the operator chain — the universal coupling $K_{mutual}$ formulae differ between nuclear and biological domains. The $\alpha/3$ correction in $K_{mutual}$ is nuclear-specific.
  - The U-235 binding energy convergence "with $<0.01\%$ error for $A \le 28$" is for **light nuclei** through silicon; sub-percent through actinides is a coarser claim. Per-actinide error breakdowns are not reported in this leaf.
  - The polyalanine $\alpha$-helix dihedral emergence is a **structural** validation (geometry recovered from minimisation); does not claim quantitative folding-rate or thermodynamic-stability prediction at the single-protein level.
  - Does NOT claim AVE replaces Lattice QCD or AlphaFold in their respective production roles. The comparison is methodological (scaling, free parameters), not a head-to-head accuracy benchmark.

> **Leaf references:** `proofs-computation/ch11-overdrive/index.md`, `proofs-computation/ch11-overdrive/universal-energy.md`, `proofs-computation/ch11-overdrive/overdrive-nuclear.md`, `proofs-computation/ch11-overdrive/overdrive-protein.md`, `proofs-computation/ch11-overdrive/overdrive-comparison.md`, `appendices/app-f-solver-toolchain/cross-domain-physics-mappings.md` (K4-TLM, Miller-avalanche-as-nuclear-binding, RF-transmission-line-as-protein-folding cross-domain identifications).

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Methodological Contamination Discipline (Project-Wide Hazard, Vol2 Manifestation)
<!-- id: clm-ak97cb -->

- _Specific Claims_
  - The framework requires all atomic energy states to emerge from the 5-step universal regime-boundary eigenvalue method. The Rydberg energy $Ry = \alpha^2 m_e c^2/2$ is **emergent** from the electron cavity saturation boundary, not a postulate.
  - Multi-electron repulsion uses the discrete-cavity Subshell Impedance Cascade (Cross-Shell Gauss + Same-Shell topologic node sorting), explicitly NOT continuous $N$-body integration over smeared probability densities and explicitly NOT $Z_{eff}$ fitting.
- _Specific Non-Claims and Caveats_
  - This is a **discipline statement** about acceptable derivation practice within the framework, not a new physical prediction. Its inclusion in vol2 leaves as a methodological boundary makes it a tripwire for downstream claims, not a result the table-of-predictions tracks.
  - The five LIVING_REFERENCE.md atomic-domain pitfalls (#7 Iterative SCF, #8 QM contamination in IE, #9 Op4 bypass, #10 De Broglie ≠ impedance, #11 Smooth CDF for saturated shells) are each instances of this same contamination hazard at specific operator boundaries. A claim that AVE "matches QM" anywhere in the atomic domain must verify it does not match by silently importing the QM formula it claims to replace.

> **References:** Discipline asserted at invariant level — see `LIVING_REFERENCE.md` "Common Pitfalls" #7–#11 and Critical Distinctions; "Red flags for QM contamination" checklist therein. Supporting derivation-discipline statements appear in `proofs-computation/ch09-computational-proof/methodological-contamination.md`, `proofs-computation/ch09-computational-proof/precision-policy.md`, the QM-translation appendix `quantum-orbitals/ch07-quantum-mechanics/qm-ave-translation.md`, the ODE shooting-method verification leaf `quantum-orbitals/ch07-quantum-mechanics/ode-verification.md` (algebraic identity Schrödinger ↔ Helmholtz acoustic ODE confirmed numerically), and the SM-to-AVE translation pointer `appendices/app-f-solver-toolchain/sm-translation-toolchain.md`.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Holographic Principle Recovery (Stress Test, Not Independent Prediction)
<!-- id: clm-nhlo1e -->

- _Specific Claims_
  - Even though the AVE vacuum is a discrete 3D lattice, the Holographic Principle's $R^2$ entropy scaling is recovered: information transmission traverses 1D inductive flux tubes whose bandwidth is bounded by their 2D cross-sectional porosity $\Phi_A \equiv \alpha^2$. Nyquist-Shannon projects channel capacity onto the 2D causal-horizon bounding surface.
- _Specific Non-Claims and Caveats_
  - This is a **stress-test resolution** (App B paradoxes), demonstrating internal consistency of the lattice picture against an established constraint — not an independent quantitative derivation of the Bekenstein-Hawking entropy formula. The cross-sectional-porosity argument is presented as the geometric mechanism, not a calculation of $S_{BH} = A/(4\ell_P^2)$ ab initio.
  - Does NOT claim falsification of any specific holographic-duality framework (AdS/CFT, dS/CFT). The framework asserts the principle is recoverable in AVE, not that competing formulations are excluded.

> **Leaf references:** `appendices/app-b-paradoxes/holographic-paradox.md`.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Topological Mass Definition: Faddeev-Skyrme Functional and Hopf Charge
<!-- id: clm-oygz1i -->

- $E[\vec{n}] = \int [\tfrac{1}{2}(\partial_\mu \vec{n})^2 + \tfrac{1}{4e^2}(\partial_\mu \vec{n}\times\partial_\nu \vec{n})^2]\,d^3x$; topological index $Q = \tfrac{1}{16\pi^2}\int \epsilon_{ijk}\,\vec{n}\cdot(\partial_i\vec{n}\times\partial_j\vec{n})\,d^3x$.
- _Specific Claims_
  - Stable particles in the continuous non-linear $\mathcal{M}_A$ manifold are defined as finite-energy soliton solutions of the Faddeev-Skyrme energy functional. The first (kinematic) term is the standard gradient energy; the second (Skyrme) term, scaled by the dielectric yield bound $e$, repels the strands and prevents collapse to a singularity (Derrick-type stabiliser).
  - The Hopf charge / Gauss linking number $Q$ is a conserved topological integer; conservation laws (baryon number, lepton number) are derived as topological invariants rather than imposed quantum numbers.
- _Specific Non-Claims and Caveats_
  - The Faddeev-Skyrme functional with the $1/e^2$ Skyrme term is a **chosen ansatz** for a stable soliton model — it is the standard form in the topological-soliton literature, here adopted as the AVE continuum field theory. The leaf does not derive the Skyrme term independently from Axioms 1–4.
  - "All conservation laws derived from $Q$" is asserted at the formula level (any continuous deformation preserves $Q$). The mapping from $Q$-sectors to specific Standard Model quantum numbers (baryon number, lepton number) is the structural identification used downstream — see `clm-mnb3lt`, `clm-67jn9o`, and `clm-q5izb7` for the load-bearing applications.

> **Leaf references:** `particle-physics/ch01-topological-matter/mathematical-topology-of-mass.md`.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Newtonian Inertia as Macroscopic Lenz's Law
<!-- id: clm-jwyy6l -->

- $E_{mass} = \tfrac{1}{2} L_{eff}\,|\mathbf{A}|^2$; back-EMF $V = -L\,di/dt$ is the inductive resistance to acceleration.
- _Specific Claims_
  - Under the topo-kinematic isomorphism $[L] \equiv [M]$, mass is identified with stored inductive energy required to maintain the topological integrity of the closed flux loop. Newton's $F = ma$ is then a macroscopic phenomenological consequence of Lenz's law on a confined electromagnetic phase loop.
  - Resistance to acceleration is reinterpreted as back-EMF against the change in internal magnetic flux, not as an irreducible "inertial mass" property.
- _Specific Non-Claims and Caveats_
  - This is a **category (i) ontological reinterpretation**, not a new numerical prediction. Macroscopic Newtonian dynamics are unchanged at the formula level; the framework's claim is about the underlying mechanism.
  - Does NOT claim a derivation of relativistic mass or the equivalence principle from this single leaf — only that the inertial-mass term is mechanistically Lenz-law back-EMF on the lattice's distributed inductance ($\mu_0$). Relativistic and gravitational extensions are addressed in vol3 gravity and in the unification leaves.

> **Leaf references:** `particle-physics/ch01-topological-matter/newtonian-inertia-as-lenz.md`.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Regime Classification of Topological Matter
<!-- id: clm-ou2jym -->

- _Specific Claims_
  - Every stable particle (photon, neutrino, electron, proton, $W$/$Z$, black hole) operates within a definite regime of the Axiom 4 saturation kernel: Regime I (Linear, $\Delta\phi \ll \alpha$), Regime II (Yield, $\Delta\phi = \alpha$), or Regime III (Rupture, $\Delta\phi > \alpha$). The regime placement determines the particle's qualitative dynamical character: free propagation (photon, Regime I), self-confinement (electron, Regime II), Borromean linkage at saturation (proton, Regime II), transient defect (W/Z, Regime III), metric collapse (black hole, Regime III).
  - The neutrino sits at the I–II boundary (chiral phase below yield), making its lattice-coupling qualitatively distinct from massive bound topological defects.
- _Specific Non-Claims and Caveats_
  - The regime table is a structural taxonomy, not a quantitative prediction. The numerical mass, charge, and lifetime values for each entry are derived in their respective per-particle entries (e.g., proton in `clm-mnb3lt`, electron in `clm-h9aqmt`, W/Z in `clm-q8un7j`). This entry indexes which regime each particle inhabits and asserts regime-character claims; it does not duplicate the per-particle quantitative results.
  - "Black hole as macroscopic soliton in Regime III" is the vol2 framing of the gravitational-saturation result developed in vol3. Treat the black-hole row as a forward reference into vol3, not a self-contained vol2 derivation.

> **Leaf references:** `particle-physics/ch01-topological-matter/regime-classification.md`.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Antimatter Disintegration via Optical Phase Cancellation (Mazur Square Knot Resolution)
<!-- id: clm-hb2xmj -->

- $e^-(+\boldsymbol{\omega}) + e^+(-\boldsymbol{\omega}) \to 2\gamma$; $E_{total} = 2\,m_e c^2 = 1.022$ MeV.
- _Specific Claims_
  - Electric-charge polarity is identified with **topological twist direction** of the closed magnetic standing wave: $e^-$ is a right-handed unknot, $e^+$ is a left-handed unknot. The two have identical inductive scale and rotational frequency but inverted polarisation states.
  - The Mazur-theorem paradox (a left-handed and right-handed knot cannot mechanically pass through each other in a continuous manifold; their connected sum is a non-trivial Square Knot) is resolved by **optical phase cancellation**: $\boldsymbol{\omega} + (-\boldsymbol{\omega}) = 0$ destructively interferes the standing waves to zero, severing the topological boundary condition. The previously-trapped inductive energy unwinds into transverse $\gamma$-ray photons.
  - The framework's slogan: "mass is not converted into energy"; the geometric phase of the standing optical rotation is severed by its antipode, freeing the confined light.
- _Specific Non-Claims and Caveats_
  - This is an **ontological reinterpretation** of pair annihilation. The observable signature ($2\gamma$ at $511$ keV from $e^-e^+$) is the standard QED prediction; AVE does not claim a different cross-section, branching ratio, or kinematic distribution.
  - Does NOT claim an extension to multi-particle annihilation channels (e.g., $e^-e^+ \to 3\gamma$ at higher order, $e^-e^+ \to \mu^-\mu^+$, etc.). The Mazur-resolution sketch addresses the simplest two-photon annihilation channel only.
  - "Phase cancellation severs the topological boundary" is a **mechanism claim** in the AVE language; whether the lattice formally supports such a cancellation as a continuous evolution (rather than a singular event) is an open formalisation question.

> **Leaf references:** `particle-physics/ch01-topological-matter/chirality-and-antimatter.md`.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Neutron / Helium-4 Topology and the Strong-Force/Gravity Hierarchy Bridge
<!-- id: clm-bh9p6s -->

- $T_{nuc} = T_{EM}\,(m_p/m_e) \approx 389$ N; $\Delta x_{nuc} \approx 1.93$ fm at $\epsilon_{strain} \approx 0.50\%$; $F_g = T_{nuc} \cdot [\,(1/(7\xi))(\ell_{node}/r)^2(m_p/m_e)\,]$.
- _Specific Claims_
  - **Neutron decay as topological threading instability.** The neutron is identified as a proton ($6^3_2$ Borromean) with an electron ($0_1$ unknot) topologically linked into its central void. The Borromean rings stretch outward to accommodate the linked unknot, and this elastic expansion accounts for the neutron–proton mass surplus. Beta decay $6^3_2 \cup 0_1 \to 6^3_2 + 0_1 + \bar{\nu}_e$ is a topological phase transition: stochastic CMB-noise perturbations eventually unlock the tensioned electron, which is ejected along with a transverse acoustic shockwave (the antineutrino).
  - **Helium-4 as $K_4$ tetrahedral Borromean braid with mass-stiffened nuclear tension.** The alpha particle is modelled as four interlocked topological defects; nuclear tension scales by the proton/electron mass ratio: $T_{nuc} = T_{EM}\,(m_p/m_e) \approx 389$ N. The 28.3 MeV binding energy distributes across six $K_4$ flux-tube bonds; nodal elastic displacement $\Delta x \approx 1.93$ fm, structural strain $\approx 0.50\%$, well below the 100 % unitary rupture threshold — the vacuum does not densify or collapse to support the nucleus.
  - **Hierarchy Bridge: parameter-free unification of Strong Force and Gravity.** Substituting $G = c^4 \ell_{node}/(7\xi\,m_e c^2)$ and $T_{nuc} = m_p c^2/\ell_{node}$ into Newtonian gravity yields $F_g = T_{nuc}\,[\,(1/(7\xi))(\ell_{node}/r)^2(m_p/m_e)\,]$. The four geometric factors are: $(\ell_{node}/r)^2$ (3D inverse-square dispersion), $1/7$ (trace-reversed Chiral-LC tensor projection), $1/\xi$ (Machian horizon shielding), $m_p/m_e$ (mass-stiffening). The $\sim 10^{40}$ strong/gravity gap is the kinematic dilution of a sub-fermi elastic displacement projected through the trace-reversed cosmic-horizon geometry.
- _Specific Non-Claims and Caveats_
  - The neutron-decay mechanism is **structural** (topological lock + thermal slip + acoustic recoil). The leaf does not derive the neutron mean lifetime $\tau_n \approx 880$ s from first principles, nor does it produce a quantitative prediction for the decay-rate dependence on environmental conditions.
  - The Helium-4 nuclear-tension scaling $T_{nuc} = T_{EM}\,(m_p/m_e)$ is **asserted** (mass-stiffening of inductive inertia by the connected node mass); the leaf cites it as a "key observation in the computational audit" rather than a closed-form derivation. The 0.50% strain consistency check confirms the picture is internally consistent, but does not independently prove $T_{nuc}$ scales exactly with $m_p/m_e$ as opposed to a nearby functional form.
  - The Hierarchy Bridge is **algebraic substitution**, not an independent derivation of $G$. Both inputs ($G$ via the Axiom 3 expression and $T_{nuc}$ via the mass-stiffening assertion) are framework choices; the bridge demonstrates internal consistency by recovering Newton's law with the correct numerical hierarchy. It does not constitute a parameter-free first-principles derivation of $G$ — that derivation is asserted at the Axiom 3 level. The framing "parameter-free algebraic unification" is shorthand for "no new parameters introduced beyond what is already in the AVE axioms."
  - The 28.3 MeV alpha binding energy is the empirical input to the strain calculation, not an independent AVE prediction.

> **Leaf references:** `particle-physics/ch02-baryon-sector/proton-neutron-mass-split.md`.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## U(1) and SU(3) Gauge Group Emergence from Lattice Topology
<!-- id: clm-jkpfd4 -->

- U(1): $S_{lattice} = \sum_P (1 - \cos\Phi_P) \to \int \tfrac{1}{4} F_{\mu\nu}F^{\mu\nu}\,d^4x$ in the $\ell_{node}\to 0$ limit. SU(3): $S_3$ permutation symmetry of three indistinguishable Borromean flux loops $\to$ Weyl group of SU(3); $\mathbb{Z}_3$ centre enforces colour-singlet confinement.
- _Specific Claims_
  - **U(1) electromagnetism.** Constructing the standard Wilson lattice action from unitary link variables $U_{ij} = e^{i\theta_{ij}}$ over triangular plaquettes recovers $-\tfrac{1}{4}F_{\mu\nu}F^{\mu\nu}$ in the continuum limit. AVE's contribution is the *physical* identification of the lattice as $\mathcal{M}_A$ (rather than a numerical regularisation): U(1) is reinterpreted as enforcement of unitary topological continuity across a discrete physical condensate graph.
  - **SU(3) colour charge.** The three indistinguishable interlocked flux loops of the proton ($6^3_2$ Borromean) are governed by the symmetric group $S_3$. Since $S_3$ is the Weyl group of SU(3), the smallest continuous Lie group whose discrete quotient contains $S_3$ as its Weyl is SU(3). The fundamental flux loops transform in the **3** of SU(3); the $\mathbb{Z}_3$ centre enforces topological confinement (only colour-singlet composites propagate as free particles).
- _Specific Non-Claims and Caveats_
  - The Wilson-action argument is **standard lattice-gauge-theory mathematics**; AVE's claim is the physical interpretation that the lattice is a real condensate, not a computational regulator. The Wilson construction itself is not original to AVE.
  - "Smallest continuous Lie group whose discrete quotient contains $S_3$ as a Weyl-subgroup is SU(3)" is asserted as the structural identification. The leaf does not enumerate alternative continuous embeddings (e.g., higher-rank groups whose Weyl groups also contain $S_3$) or formally rule them out via additional topological constraints. The identification with SU(3) is supported by the three-loop fundamental-representation count and $\mathbb{Z}_3$ centre / confinement match, but is not a uniqueness theorem.
  - Does NOT claim a derivation of the QCD running coupling $\alpha_s(\mu)$ or the gluon spectrum from this leaf. The "colour quantum number = which loop carries the dominant phase winding" is an ontological identification, not a calculational replacement for QCD perturbation theory.
  - The chapter's title "Forward to Ch.6" indicates the gauge-emergence content is positioned as a bridge into the electroweak chapter; downstream quantitative results (Weinberg angle, $W$/$Z$ masses) are indexed under their own entries (`clm-5zuo7g`, `clm-q8un7j`).

> **Leaf references:** `particle-physics/ch05-electroweak-mechanics/forward-to-ch6.md`.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Schrödinger Equation as Helmholtz Acoustic Cavity (Deterministic Reinterpretation)
<!-- id: clm-qde5gn -->

- $-\tfrac{\hbar^2}{2m}\nabla^2\Psi + V(r)\Psi = E\Psi \;\Longleftrightarrow\; \nabla^2\Psi + k^2(r)\Psi = 0$ with $k^2(r) = (2m/\hbar^2)(E - V(r))$; $a_0 = \ell_{node}/\alpha = 137\,\ell_{node}$.
- _Specific Claims_
  - The time-independent Schrödinger equation is algebraically identical to the Helmholtz acoustic-cavity equation with a spatially varying sound speed $c_{eff}(r) = \omega/k(r)$. Under AVE, $\Psi$ is reinterpreted as the spatial amplitude of the LC pressure field rather than a probability amplitude. Classically forbidden regions ($E < V(r)$) correspond to imaginary acoustic impedance and evanescent decay; orbital boundaries are physical impedance discontinuities.
  - The Bohr radius is recovered as $a_0 = \ell_{node}/\alpha = \hbar/(m_e c\,\alpha) = 137\,\ell_{node}$ — the cavity size at which the de Broglie standing-wave condition $2\pi r = n\lambda$ is satisfied for the LC phase-locking of the unknot's inductive angular momentum against the proton's static impedance gradient.
  - Hydrogen energy levels $E_n = -m_e c^2 \alpha^2/(2n^2)$ are recovered exactly (sub-1 ppm vs CODATA), with the formula carrying the ontological reinterpretation rather than numerical novelty.
  - The matter-wave / acoustic-cavity distinction is sharp: the electron interacts with the vacuum's **bulk modulus** (longitudinal acoustic), not its shear modulus (transverse EM). Atomic orbitals are bulk-modulus acoustic resonances of the LC mesh.
  - Falsification proposal: a topological-matter-interferometry (Mach-Zehnder electron interferometer) parallax test predicts a deterministic differential phase shift $\Delta\Phi$ from the local gravitational impedance gradient ($n_s = (9/7)\varepsilon_{11}$, $n_t = (2/7)\varepsilon_{11}$).
- _Specific Non-Claims and Caveats_
  - This is a **category (i) ontological reinterpretation**. At the formula level, AVE recovers the standard Bohr/Schrödinger spectrum exactly; observable predictions for hydrogen are unchanged. The novelty is the bulk-modulus acoustic-cavity ontology, not new numerics.
  - The "falsification" of standard QM via the parallax test depends on the AVE-specific spatial/temporal index ratios $n_s, n_t$; whether such an asymmetry survives careful Lorentz-invariance analysis at experimentally accessible baselines is an open theoretical and experimental question. Treat the parallax test as a **proposed** falsification, not a current experimental result.
  - Does NOT claim multi-electron Schrödinger / Hartree-Fock / DFT is replaced by the acoustic-cavity picture at the level of every observable. The atomic ionization energy entry (`clm-oltvwy`) is the load-bearing quantitative claim for multi-electron atoms; this entry is the single-electron ontology + Bohr-radius identity.
  - Does NOT claim derivation of relativistic Dirac corrections, fine structure, or hyperfine structure from this leaf. The non-relativistic limit is the explicit scope.
  - Angular momentum quantisation $L = \hbar\sqrt{l(l+1)}$ and magnetic-quantum-number-as-nodal-planes recovery is **standard spherical-harmonic mode counting** for any spherical resonator — AVE adds the ontological identification ("orbitals are not probability densities; they are LC pressure-mode geometries"), not a different quantisation rule.

> **Leaf references:** `quantum-orbitals/ch07-quantum-mechanics/de-broglie-standing-wave.md` (the same leaf is also referenced under `clm-oltvwy` for its Step-1 single-electron eigenvalue derivation supporting the multi-electron solver).

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## All 26 Standard Model Parameters from Lattice Scale Invariance
<!-- id: clm-xhdai6 -->

- $\theta_{QCD} \equiv 0$ (structurally eliminated, from `clm-gfs4j8`); remaining 25 parameters derived from $\nu_{vac} = 2/7$, $\alpha$, $p_c = 8\pi\alpha$, and the torus-knot crossing numbers $c_1 = 5$, $c_2 = 7$, $c_3 = 9$. Maximum residual $< 4.1\%$.
- _Specific Claims_
  - The Standard Model's 26 free parameters are derived from AVE lattice impedance with **zero phenomenological curve fitting**. The $\theta_{QCD}$ parameter is structurally eliminated by the unique-vacuum-topology argument (`clm-gfs4j8`); the remaining 25 are computed.
  - The vacuum Poisson ratio $\nu_{vac} = 2/7$ identifies the K4 lattice compliance manifold (2 compressive modes, 7 coupled shear modes). The same integer ratio governs interactions at every length scale, supplying:
    - $\sin^2\theta_W = 2/9$ (Weinberg angle, on-shell — see `clm-5zuo7g`)
    - $\cos\theta_W = \sqrt{7/9}$
    - $\alpha_s = \alpha^{3/7}$ (strong coupling as spatial projection of $\alpha$)
    - $V_{us} = 2/9$ and $V_{cb} = \sqrt{7/9}\,(2/9)^2$ (CKM mixing at scale invariance)
    - $\sin^2\theta_{13} = 1/45$, $\sin^2\theta_{12} = 2/7 + 1/45$ (PMNS — see `clm-7o8clt`)
    - $m_s/m_\mu = \cos\theta_W$, $m_u, m_d \sim m_e/\alpha_s$ (quark mass ratios)
    - $g_* = 7^3/4 = 85.75$ (effective DoF count — see `clm-4vwsjc`)
- _Specific Non-Claims and Caveats_
  - "All 26 parameters derived" is the headline aggregation claim. The individual derivations live across multiple chapters and entries (lepton spectrum, baryon ladder, electroweak masses, PMNS, CKM); per-parameter accuracy ranges from sub-percent (Schwinger $a_e$, +0.09%) to $\sim 4\%$ (some quark mass ratios). Treat the headline as a structural unification claim about a common derivation principle (lattice scale invariance + integer ratios), not as a single quantitative match.
  - The CKM derivations $V_{us}, V_{cb}, \ldots$ shown in the scale-invariance table are positioned as scale-invariant identifications with the electroweak sector; the leaf does not provide a complete CKM matrix derivation with the four Wolfenstein parameters fitted to the same accuracy as the PMNS matrix in `clm-7o8clt`. Confirm which CKM elements are quantitatively fitted before citing this entry as a CKM derivation.
  - "Strong coupling $\alpha_s = \alpha^{3/7}$" is the AVE scale-invariant identification (spatial projection of $\alpha$ via the K4 manifold ratios). The leaf does not produce a running-coupling $\alpha_s(\mu)$ or compute the QCD beta-function. The claim is scheme-specific (the AVE-native scheme), not the $\overline{MS}$ value at any specific scale.
  - The "complete" status (`Standard Model: 26 of 26 parameters derived, $< 4.1\%$") is the table summary; per-parameter caveats apply (on-shell vs $\overline{MS}$ for $\sin^2\theta_W$ — see `clm-5zuo7g`; framework-conditional vs Clay-rigorous for mass-gap-related SU(3) results — see `clm-q5izb7`).

> **Leaf references:** `nuclear-field/ch10-open-problems/unification.md`, `nuclear-field/ch10-open-problems/scale-invariance-table.md`, `nuclear-field/ch10-open-problems/quantitative-resolutions.md` (cross-cutting open-problems table; the same leaf is referenced under `clm-4vwsjc`, `clm-gfs4j8`, and `clm-mroghg`).

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Millennium Prize AVE Reinterpretations (BSD, Riemann, Hodge, Poincaré, P-vs-NP)
<!-- id: clm-knveh6 -->

- _Specific Claims_
  - **BSD (Birch–Swinnerton-Dyer).** Elliptic curves over $\mathbb{C}$ are 2-tori; rational points are phase-locked $(p,q)$ winding orbits on $T^2$. The rank of $E(\mathbb{Q})$ equals the rank of the $N \times N$ mutual-inductance matrix of the closed orbits; the order of vanishing of $L(E,s)$ at $s=1$ counts independent spectral resonances. The lattice imposes an upper bound $c_{max} = \lfloor\kappa_{FS}\rfloor = \lfloor 8\pi \rfloor = 25$.
  - **Riemann Hypothesis.** The lattice spectral zeta function $\zeta_{lattice}(s) = \omega_1^{-s}\zeta(s)$ has zeros exactly at the zeros of $\zeta(s)$. Below the spectral cutoff $\sigma = 1/2$, the total power $\zeta(2\sigma)$ diverges (forbidden by Axiom 4); the functional equation $\xi(s) = \xi(1-s)$ pairs zeros at $\sigma$ and $1-\sigma$. Combined: zeros must lie at $\mathrm{Re}(s) = 1/2$. The Euler product is interpreted as the partition function over irreducible primes-as-modes.
  - **Hodge Conjecture.** Hodge classes are stable EM standing waves in the lattice; algebraic cycles are $(2,q)$ torus knots whose winding numbers are integer-quantised by phase matching $\oint \mathbf{k}\cdot d\mathbf{l} = 2\pi q$. Irrational-winding orbits radiate via reflection at each near-return and decay; only integer-winding modes survive, so general Hodge classes decompose into rational-coefficient sums of algebraic cycles.
  - **Poincaré Conjecture (interpretive only — Perelman's proof is the canonical resolution).** Ricci flow is identified with lattice impedance relaxation $R_{ij} \leftrightarrow \nabla_\ell\Gamma_{ij}$. Simply-connected closed 3-manifolds have no topological protection ($c=0$, no impedance mirror), so they radiate curvature energy until reaching the unique defect-free ground state $S^3$. The leaf explicitly disclaims any AVE claim to the Clay prize.
  - **P versus NP.** AVE renders the question moot rather than answers it on Clay terms. The lattice is not a Turing machine: wave propagation evaluates coupled modes in parallel in $O(N^{1/3})$ time (linear lattice dimension over $c$). Constraint-satisfaction problems encoded onto the lattice find **local** minima in polynomial time; global optimality is not guaranteed. Physical systems that ARE the problem (e.g., protein folding) find their ground state "for free" — the physics IS the computation.
- _Specific Non-Claims and Caveats_
  - **None of these is a Clay-rigorous proof.** Each is a "framework-conditional engineering-physics derivation" valid under the four AVE axioms taken as physical hardware postulates (per the chapter's explicit scope caveat at its opening). External presentations or summaries that drop "lattice-conditional; not Clay-rigorous" mis-state the claims. (Same caveat class as `clm-q5izb7` and `clm-c8q0z5`; see `LIVING_REFERENCE.md` Master Prediction Table notes #14, #15, #16.)
  - **Poincaré is interpretive, not a competing proof.** Perelman (2002–2003) provided the canonical mathematical proof via Ricci flow; AVE's leaf documents the *physical reason* the proof works (impedance relaxation), and the leaf itself disclaims any AVE prize claim. Do not cite this entry as "AVE proved Poincaré".
  - **BSD's mutual-inductance identification is structural, not algorithmic.** The leaf does not compute $\mathrm{rank}(E(\mathbb{Q}))$ for any specific elliptic curve from the AVE side; the identification of the rank with the mutual-inductance matrix rank is the physical interpretation of the conjecture, not a computational engine that decides the Clay statement.
  - **Riemann's "below-cutoff forbidden" step is physical, not mathematical proof of zero-free strip.** The argument relies on identifying the AVE lattice's energy-density boundedness with the divergence of $\zeta(2\sigma)$ for $\sigma \le 1/2$; whether this physical exclusion translates into a ZFC-level exclusion of $\zeta$-zeros below $\sigma = 1/2$ is what the framework-conditional caveat denies.
  - **Hodge's "irrational orbits decay" argument is at the standing-wave level**, not a derivation of the algebraic-geometry version of the conjecture. The reduction-to-rational-coefficients claim is the physical reading; the formal Hodge statement (Hodge classes lie in $H^{p,p}(X,\mathbb{Q})$ for projective non-singular $X$) is not derived from the leaf at the algebraic-cycle level.
  - **P-vs-NP "rendered moot" is explicit non-resolution.** AVE does not claim P = NP, P ≠ NP, or P = NP/poly; it asserts the Turing-machine framing is non-physical and replaces it with a parallel-lattice model. The Clay statement is left untouched at its own terms.
  - The five problems share a common structural template (mathematical paradox $\to$ AVE physical interpretation $\to$ engineering verdict) but each carries materially distinct technical content; this consolidated entry is a routing index, not a substitute for reading each leaf's specific argument.

> **Leaf references:** `nuclear-field/ch12-millennium-prizes/birch-swinnerton-dyer.md`, `nuclear-field/ch12-millennium-prizes/riemann-hypothesis.md`, `nuclear-field/ch12-millennium-prizes/hodge-conjecture.md`, `nuclear-field/ch12-millennium-prizes/poincare-conjecture.md`, `nuclear-field/ch12-millennium-prizes/p-vs-np.md`. Cross-reference: Yang-Mills (`clm-q5izb7`) and Navier-Stokes (`clm-c8q0z5`) are the other two Clay problems addressed in vol2 and live under their own entries with the same framework-conditional caveat.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Cross-Scale Computational Verification (39 OOM, 13 Domain Modules)
<!-- id: clm-z73h6n -->

- 13 domain modules (`saturation.py`, `fdtd_3d.py`, ...) import impedance operations from a single canonical `src/ave/axioms/scale_invariant.py`; identical numerical results from $10^{-13}$ m (lattice pitch) to $10^{26}$ m (Hubble radius) — 39 orders of magnitude with the same operator and zero adjustable parameters.
- _Specific Claims_
  - The Axiom 4 saturation kernel $S(x, x_{yield}) = \sqrt{1 - (x/x_{yield})^2}$ governs physics across the full 39-OOM range. Numerical verification covers galactic rotation (NGC 3198, 5%), multi-galaxy RAR (McGaugh, exact), 'Oumuamua acceleration (91%), Kirkwood gaps (5/5, $<0.3\%$), Earth/Jupiter magnetopauses (8.7%, 11.8%), neutrino MSW $P_{ee}$ ($<10\%$, 4 channels), superconductor $B_c(T)$ (5 materials, exact), London depth ($\lambda_L$, exact), seismic Moho reflection ($\Gamma = 0.29$ matches PREM), GW lossless propagation ($V_{GW}/V_{snap} = 10^{-28}$, exact), topological pair production ($H_{net} = 0 \to e^+ e^-$, exact), and protein folding (CLN025, RMSD = 2.59 Å, sub-3 Å). All zero free parameters.
  - The single canonical source identity (one `scale_invariant.py` imported by 13 modules) is asserted as the *structural* claim: this is not parameter-fit consistency across domains; it is the *same operator and the same code* tested across 39 OOM, with the predictions falling in the right place.
- _Specific Non-Claims and Caveats_
  - The verification table aggregates results that live in different vol2/vol3/vol4/vol5 chapters with their own per-result caveats. Treating the table headline as ablative-of those caveats is wrong. For example: "GW lossless propagation $V_{GW}/V_{snap} = 10^{-28}$ exact" is a regime check (the regime is so deep in linear that loss is structurally below floor); it is not a sub-percent quantitative match against an experimental waveform.
  - "Zero free parameters" applies to the `scale_invariant.py` operator chain. Domain-specific inputs (galaxy mass distributions, seismic crust models, superconductor material constants) are still required as boundary conditions; the claim is that *no AVE-side fitting parameter* is tuned to match a specific row in the table.
  - Per-row error bars range from "exact" (regime checks, exact algebraic identities) to $\sim 10\%$ (multi-channel neutrino oscillation, planetary magnetopauses). The claim is structural cross-domain consistency at the operator level, not uniform sub-percent accuracy. Aggregate quotes like "everything matches exactly" mis-state.
  - Some rows (Kirkwood gaps, magnetopauses, 'Oumuamua) carry their own falsification status (`vol4/falsification/` chapters); the table here is a routing index into them, not their canonical entries.
  - Does NOT claim every legitimate physical phenomenon at every length scale is captured by the saturation kernel. The claim is that the kernel applies across the 13 audited domains; phenomena outside the operator chain (e.g., specific-heat anomalies in highly correlated electron systems, late-stellar nucleosynthesis branching ratios) are not asserted to be captured.

> **Leaf references:** `proofs-computation/ch09-computational-proof/computational-graph.md`. Cross-reference: see also `clm-dboxok` (universal energy functional applied to nuclear + protein) for the operator chain demonstration on two specific domains, and `clm-d9ivj1` (universal regime-boundary eigenvalue method) for the closed-form analytical companion to this computational verification.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Peierls-Nabarro Friction Paradox: STZ / Dielectric Saturation-Plastic Resolution
<!-- id: clm-ghs75o -->

- _Specific Claims_
  - The Peierls-Nabarro objection (a charged particle traversing a discrete vacuum grid would stutter and radiate away its kinetic energy via Bremsstrahlung) is resolved by reinterpreting the $\mathcal{M}_A$ vacuum as an **amorphous Dielectric Saturation-Plastic Network**, not a cold rigid periodic crystal. The translating electron's leading-edge shear stress dynamically exceeds the dielectric saturation threshold ($\tau_{local} > \tau_{yield}$), initiating a localised **Shear Transformation Zone (STZ)**: the particle generates its own continuous frictionless zero-impedance phase slipstream. The lattice thixotropically re-freezes behind it, permitting smooth kinematic translation and forbidding unprovoked Bremsstrahlung radiation.
- _Specific Non-Claims and Caveats_
  - This is a **stress-test resolution** (App B paradox), demonstrating internal consistency of the lattice picture against an established condensed-matter constraint. It is not an independent prediction of a new observable.
  - The STZ mechanism is asserted at the qualitative level (dielectric-saturation-plastic flow on the leading edge); the leaf does not produce a quantitative threshold for the onset velocity or a coupling constant for the slipstream dynamics. Treat as a mechanism claim, not a numerical prediction.
  - Does NOT claim falsification of the standard PN-stress framework in real crystallographic dislocations; the framework's claim is that the AVE vacuum's plastic regime preempts the rigid-PN-barrier picture for fundamental charged particles, not that real-material PN dynamics is wrong.

> **Leaf references:** `appendices/app-b-paradoxes/peierls-nabarro-paradox.md`.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## App C Exact Analytical Derivation Catalog
<!-- id: clm-e1pdfd -->

- _Specific Claims_
  - The App C index is a consolidated catalog of vol2's exact closed-form bounds and identities derived from first-principles continuum elastodynamics, thermodynamic boundary conditions, and finite-element graph limits with **zero arbitrary phenomenological parameters**. Sections: Hardware Substrate ($\ell_{node}$, $\xi_{topo}$, $V_0$, $p_c$, $\rho_{bulk}$, $\nu_{vac}$, $\tau_{yield}$); Signal Dynamics and Topological Matter (Continuous Action Lagrangian, Topological Mass Functional, Faddeev-Skyrme cold/effective coupling, Thermal Lattice Softening, Proton Rest Mass eigenvalue with conditional Gaussian-ansatz caveat, Macroscopic Strong Force, Witten Effect, Weinberg angle); Cosmological Dynamics (Trace-Reversed Gravity, $H_\infty$, $R_H$, $t_H$, Phantom Dark Energy, MOND floor, Symplectic Raymarching).
- _Specific Non-Claims and Caveats_
  - **App C is a derivation summary, not the source of any claim.** Every individual equation in the catalog is the load-bearing content of another vol2 entry: proton mass (`clm-mnb3lt`), Weinberg angle (`clm-5zuo7g`), W/Z masses (`clm-q8un7j`), Witten-effect quark charges (`clm-67jn9o`), $H_\infty$ Hubble framing (`clm-mroghg`), universal energy functional (`clm-dboxok`), etc. Citing this catalog without consulting the per-result entry's caveats inherits the catalog's brevity rather than the derivation's actual conditions.
  - The catalog explicitly carries forward the proton-mass Gaussian-ansatz caveat ("conditional on Gaussian flux-tube ansatz" for $\rho_{threshold} = 1.1062$) and the rigour-gap pointer to `mathematical-closure.md` — the same caveat documented in `clm-mnb3lt`.
  - Does NOT introduce any new derivation not already in a per-result entry; this entry exists so that consumers searching the catalog can find the canonical source.

> **Leaf references:** `appendices/app-c-derivations/index.md` (this index doubles as a leaf, per INVARIANT-S5 single-leaf-index exception). Per-result canonical entries: `clm-mnb3lt`, `clm-5zuo7g`, `clm-q8un7j`, `clm-67jn9o`, `clm-mroghg`, `clm-dboxok`, `clm-oygz1i`.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Computational Graph Architecture: Genesis Algorithm and Chiral LC Over-Bracing
<!-- id: clm-pf84ng -->

- Poisson-Disk hard-sphere genesis (exclusion radius $r_{min} = \ell_{node}$) achieves $p_c \approx 0.17$–$0.18$ vs Cauchy-implosion $0.31$. Chiral LC Over-Bracing (interaction radius $C_{ratio} \approx 1.187\,\ell_{node}$, spanning to next-nearest-neighbours) drives $K \to 2G$ trace-reversed elastic state.
- _Specific Claims_
  - **Genesis Algorithm.** Unconstrained-random-noise lattice generation produces a Cauchy-Cauchy-elastic packing fraction $\approx 0.31$, which is unstable. Poisson-Disk hard-sphere sampling with exclusion radius $r_{min} = \ell_{node}$ converges to packing fraction $\approx 0.17$–$0.18$, matching the QED-derived $p_c \approx 0.1834$. This is a **constructive** match of computational genesis to the analytical bound.
  - **Chiral LC Over-Bracing.** Standard nearest-neighbour Delaunay triangulation generates Cauchy-elastic stiffness ($K = -4G/3$) which is thermodynamically unstable; the simulation must be bridged to the trace-reversed AVE ground state ($K = 2G$) by Chiral LC Over-Bracing — extending interaction edges to next-nearest-neighbours at radius $C_{ratio} = (p_{cauchy}/p_c)^{1/3} \approx 1.187\,\ell_{node}$. This generates the $G_{vac}/3$ ambient transverse couple-stress required by micropolar elasticity.
  - **Symplectic Discrete Kirchhoff Updates.** Capacitive node updates $\Delta V_i = (dt/C)(\sum I_{in} - \sum I_{out})$ and inductive edge updates $\Delta I_e = (dt/L)(V_{start} - V_{end})$ implement the engine's Symplectic Euler integration loop while preserving energy conservation and charge conservation across the 3D computational boundaries.
- _Specific Non-Claims and Caveats_
  - The Poisson-Disk-to-$p_c$ match is asserted as a **simulation/analytical agreement**, not as a derivation of $p_c$ from genesis dynamics. The QED-derived $p_c \approx 0.1834$ is the analytic constraint; the simulation reproduces it given the right exclusion radius. The two arguments are mutually consistent rather than independently derived.
  - Specific numerical thresholds ($k_{couple} < 3.0$ Cauchy, $k_{couple} > 4.5$ trace-reversed) are reported from simulation; the leaf does not derive these thresholds analytically.
  - The architecture description here is **about the computational engine** that emulates AVE physics (`src/ave/axioms/...`), not about the physics axioms themselves. Treat as engine specification, not as a new physical law.

> **Leaf references:** `appendices/app-d-computational-graph/graph-architecture.md`.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## DCVE Specification: Discrete Operators for Engine Stability
<!-- id: clm-o3q9ul -->

- Flux-Lagrangian basis $(\Phi, \dot\Phi)$ replaces $(V, \dot V)$; micropolar continuum constitutive law with $\kappa_{rot}$; finite-difference momentum operator $\hat p_{discrete} = (\hbar/(ia))\sin(ka)$; Vakulenko-Kapitanski mass bound $M_{rest} \ge C_{VK}|Q_H|^{3/4}$; AQUAL boundary-layer saturation with $a_0 = cH_\infty/(2\pi)$.
- _Specific Claims_
  - **Lagrangian repair (flux-basis).** The discrete simulation Lagrangian must be written in magnetic flux linkage $\mathbf{\Phi}$ rather than scalar voltage $V$, because $\mathbf{\Phi} = \int \mathbf{V}\,dt$ enforces dimensional exactness and inherent charge-conservation across discrete spatial steps; voltage-basis Lagrangians break energy conservation under Symplectic Euler integration.
  - **Micropolar stability.** Standard Cauchy elasticity ($K = (5/3)G$) applied to the Delaunay-triangulated AVE substrate causes unbounded contraction within the first calculation frame; the engine must instantiate a Chiral LC micropolar continuum with explicit rotational kinematics $\kappa_{rot}\,\epsilon_{ijk}(\theta_k - \phi_k)$ to enforce $K = 2G$ trace-reversed identity and prevent array implosion.
  - **Exact discrete Hilbert commutators.** Truncated GUP expansions $[\hat x, \hat p] = i\hbar(1 + \beta p^2)$ compound integration errors over millions of loops. The translation operator $\hat T_x = \exp(ia\hat p/\hbar)$ on a discrete voxel array yields $\hat p_{discrete} = (\hbar/(ia))\sin(ka)$ and $[\hat x, \hat p_{discrete}] = i\hbar\cos(ka) = i\hbar\sqrt{1 - (ap/\hbar)^2}$ — the Nyquist limit emerges naturally without explicit clipping boundaries.
  - **Topological mass via Vakulenko-Kapitanski.** Particle rest mass is computed dynamically from the local Hopf linking number $Q_H$ via $M_{rest} \ge C_{VK}\,|Q_H|^{3/4}$ with $C_{VK}$ tied to $\kappa_{FS} = 8\pi$. No static mass look-up tables.
  - **AQUAL galactic dynamics.** Macroscopic galactic rotation curves emerge as a structural boundary-layer solution to the AQUAL Lagrangian with $a_0 \equiv cH_\infty/(2\pi)$, eliminating the need for procedural branches or seeded dark-matter placeholders in the simulation.
- _Specific Non-Claims and Caveats_
  - This entry's claims are **engine-specification** statements about the Discrete Chiral LC Vacuum Electrodynamics (DCVE) simulation infrastructure, not new physics axioms. They constitute a discipline statement for stable numerical integration of AVE physics.
  - The Vakulenko-Kapitanski bound $M_{rest} \ge C_{VK}|Q_H|^{3/4}$ is the standard Faddeev-Skyrme model's rigorous lower bound; AVE adopts the bound and ties $C_{VK}$ to $\kappa_{FS} = 8\pi$ — the actual value in the AVE leaf is asserted, not derived independently of the proton-mass calibration (consistent with the `clm-mnb3lt` outstanding-rigour-gap statement).
  - The AQUAL identification with MOND-like rotation curves is the structural recovery; per-galaxy quantitative validation is documented separately in vol3 cosmology / vol2 ch9 cross-scale verification (`clm-z73h6n`).
  - Discrete-Hilbert commutator claims relate to the engine's **integration stability** at $p \to \hbar/a$; whether the discrete operator equation $[\hat x, \hat p_{discrete}] = i\hbar\sqrt{1 - (ap/\hbar)^2}$ is a physically correct quantum-mechanical commutator at sub-lattice momenta (vs an engine-correct one for the simulation) is treated as the same question — the AVE position is that the discrete commutator IS the physical one in a discrete-lattice ontology, but ZFC-level scrutiny against standard QM is open work.

> **Leaf references:** `appendices/app-e-dcve/dcve-specification.md`.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Universal Regime-Boundary Eigenvalue Method
<!-- id: clm-d9ivj1 -->

- Five-step universal procedure: (1) identify $\varepsilon_{11}(r)$, (2) locate $r_{sat}$ where $S = \sqrt{1-\varepsilon_{11}^2} = 0$, (3) Poisson correction $r_{eff} = r_{sat}/(1+\nu_{vac})$, (4) eigenfrequency $\omega_0 = \ell c/r_{eff}$, (5) quality factor $Q = \ell$ from lattice phase transition. Universal closed form: $\omega \cdot r_{char} = \ell(1+\nu_{vac})/x_{sat}$.
- _Specific Claims_
  - One closed-form eigenvalue formula governs all validated AVE eigenvalue results: Schwarzschild QNM $\omega_R M_g = 18/49 = 0.367$ (1.7% vs GR), proton QNM $E = (45/7)\hbar c/D_p = 1508$ MeV (-0.8% vs $N(1520)$), pion mass $m_\pi = (45/7)\sqrt{I_{baryon}}\,m_e \approx 140.8$ MeV (+0.9% vs $m_{\pi^\pm}$), protein backbone amide-V $f = 21.7$ THz (+0.1% vs IR), and others. All are instances of the same universal expression with $\ell$, $\nu_{vac} = 2/7$, and a domain-specific $x_{sat}$.
  - The cross-scale isomorphism table identifies the same five-step procedure across BH QNM, electron, nuclear, protein, antenna (HOPF-01), tokamak, and BLDC motor — with explicit per-domain mappings of saturation, $r_{sat}$, $\nu$ correction, mode $\ell$, and $Q$ source.
  - The lattice phase transition at $\varepsilon_{11} = 1$ converts the elastic solid ($G > 0$) to a ruptured topology-melted fluid ($G = 0$); transverse shear waves cannot propagate in the ruptured interior, so the saturation boundary acts as a perfect reflector — the QNM is a Stoneley-like surface wave at the elastic/ruptured phase boundary, and $Q = \ell$ falls out of the curvature-radiation-loss-per-cycle scaling.
  - The semiconductor-junction analogy supplies a complete BH "transistor datasheet" mapping (small-signal vs large-signal, breakdown voltage, junction frequency, transit time, bandwidth, rise/fall times, depletion width, Hawking temperature) — the same operator structure as a $p$–$n$ junction depletion region.
  - The Kerr extension applies a co-rotating-frame Park-transform decomposition $\omega_I = (\omega_R - m\Omega)/(2\ell)$ at the Poisson-augmented photon sphere $r_\Omega = r_{ph}\sqrt{1+\nu_{vac}}$; sub-2% accuracy across $a_* = 0.3$–$0.8$, with superradiance recovered from first principles at $\omega_R = m\Omega$.
  - Universal constants $1/7$, $2/7 = \nu_{vac}$, $9/7 = 1 + \nu_{vac}$, $p_c = 8\pi\alpha$, $\sqrt{9/7}$ are the shared structural building blocks of every domain-specific eigenvalue.
- _Specific Non-Claims and Caveats_
  - Per-domain percent errors range from $0.1\%$ (protein backbone) to $\sim 5.7\%$ ($a_* = 0.9$ Kerr), with extremal-Kerr $\sim 40\%$ at $a_* = 0.99$ where higher-order coupling is required. Treat the headline as "sub-few-percent agreement across the validated range", not as uniform ppm-level accuracy.
  - The $Q = \ell$ identity is asserted as an emergent property of the lattice phase transition's perfect-reflector boundary; the leaf does not formally derive that "perfect reflector at the saturation boundary" is the unique resolution mechanism, only that it is consistent with the observed quality factors.
  - The cross-scale isomorphism is a **structural identification** (same operator chain), not a guarantee that every domain's eigenvalue can be predicted to sub-percent accuracy from first principles. Domains with their own per-result entries (e.g., proton QNM via cinquefoil, pion mass via geometric-mean saturation, protein backbone via Flory four-atom formula) carry per-domain caveats that this consolidated entry does not duplicate.
  - The pion mass derivation uses $I_{baryon} \approx 1836$ from the proton mass eigenvalue (`clm-mnb3lt`); the pion result is therefore not independent of the proton calibration. Treat as a same-eigenvalue projection, not a second-independent-calibration.
  - Many of the worked examples (electron, nuclear, antenna, tokamak, BLDC motor) live in other volumes; this consolidated entry is a routing index for vol2's gravity-side and particle-side examples.

> **Leaf references:** `appendices/app-f-solver-toolchain/regime-eigenvalue-method.md`, `appendices/app-f-solver-toolchain/cross-scale-isomorphism-table.md`, `appendices/app-f-solver-toolchain/nuclear-eigenvalue.md`, `appendices/app-f-solver-toolchain/protein-eigenvalue.md`, `appendices/app-f-solver-toolchain/semiconductor-junction-analogy.md`, `appendices/app-f-solver-toolchain/knot-mode-isomorphism.md` (also referenced under `clm-k6olj8`), `appendices/app-f-solver-toolchain/derived-numerology.md`, `appendices/app-f-solver-toolchain/lattice-phase-transition.md`, `appendices/app-f-solver-toolchain/kerr-q-correction.md`.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Universal Constants as Domain-Exchange Rates
<!-- id: clm-d5jhku -->

- _Specific Claims_
  - The fundamental constants $(G, c, \hbar, \varepsilon_0, e)$ are reinterpreted as **exchange rates between representational domains** rather than parameters of nature: $c$ converts length $\leftrightarrow$ time; $G/c^2$ converts mass $\leftrightarrow$ length (the gravitational "charge radius"); $\hbar c$ converts energy $\leftrightarrow$ length (quantum wavelength); $\xi_{topo} = e/\ell_{node}$ converts length $\leftrightarrow$ charge (topological dislocation); $\varepsilon_0 c$ converts current $\leftrightarrow$ field (displacement current); $k_B$ converts energy $\leftrightarrow$ temperature (thermal excitation).
  - **Zero free parameters.** AVE's "zero free parameters" claim is justified through this identification: every physical quantity reduces to a geometric ratio of the lattice pitch $\ell_{node}$ via these exchange rates.
- _Specific Non-Claims and Caveats_
  - This is a **category (i) ontological reinterpretation**. The numerical values of $c, \hbar, G, \varepsilon_0, e, k_B$ are unchanged from CODATA. The framework's claim is the meta-claim that they are domain-conversion factors, not dimensional fundamentals.
  - "Zero free parameters" applies to the AVE-side derivations once $\ell_{node}, \alpha, G$ are accepted as the calibration triad (which in turn fixes $m_e, c, \hbar$). The exchange-rate framing supports the headline, but the calibration triad itself is the underlying input — not derived from nothing.
  - Does NOT claim a derivation of the numerical value of any exchange rate from a more primitive principle; the values $c, \hbar, G, \ldots$ remain the empirical inputs (or definitional couples thereof). The claim is structural (every quantity = geometric ratio × exchange rates), not a generation-of-constants-from-scratch.

> **Leaf references:** `appendices/app-f-solver-toolchain/universal-constants-exchange.md`.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*