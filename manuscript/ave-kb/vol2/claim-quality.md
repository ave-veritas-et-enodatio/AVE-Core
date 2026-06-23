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
  - The minimum ropelength $2\pi$ is **forced**, not chosen: it is the unique minimum-non-self-intersecting closed loop length on a discrete lattice of pitch $\ell_{node}$ when the flux-tube diameter is bounded by Axiom 1's hard-sphere exclusion ($d \equiv 1\,\ell_{node}$). The electron's role as the "structural mass-gap" of the substrate follows directly.
  - Brief running-coupling content in the leaf: Axiom 4 dynamic capacitive yielding $C_{eff}(\Delta\phi) = C_0/\sqrt{1 - (\Delta\phi/\alpha)^2}$ provides the continuous-mechanical analog of the QED running of $\alpha$. **This is a sketch**, not a quantitative reproduction of the QED $\beta$-function; treat as a mechanism claim, not as a numerical-prediction match.
- _Specific Non-Claims and Caveats_
  - Does NOT claim independent first-principles derivation of $m_e$ as a numerical mass — the absolute scale of $m_e$ enters via $T_{EM} = m_e c^2/\ell_{node}$ and $\ell_{node} = \hbar/(m_e c)$, which is a definitional couple, not a downstream prediction. The framework's claim is that the **geometric content** ($0_1$ unknot, ropelength $2\pi$, $C_{loop} = \ell_{node}$) is forced by the lattice axioms; the absolute numerical anchor is the same as in standard physics.
  - Does NOT claim the brief running-coupling derivation reproduces QED's $\beta$-function. The Resultbox $C_{eff}(\Delta\phi) = C_0/\sqrt{1-(\Delta\phi/\alpha)^2}$ is the static dielectric-saturation form, not a momentum-dependent renormalization-group flow. A rigorous AVE running-coupling derivation is an open problem.
  - The g=2 mention is brief; the canonical claim-quality entry for spin-1/2 gyroscopic precession is "Spin-1/2 as Macroscopic Gyroscopic Precession" (`clm-salw2h`) with the canonical leaf at `spin-gyroscopic-isomorphism.md` and the spin chapter. This entry's mention is pedagogical, not the canonical g=2 derivation.
  - Does NOT claim the Beltrami / $\nabla \times \mathbf{A} = k\mathbf{A}$ form is a derivation; it is an **ansatz** for the closed-loop standing-wave structure consistent with the topological unknot identification.

> **Leaf references:** [electron-unknot](./particle-physics/ch01-topological-matter/electron-unknot.md).

### Quality
- confidence: 0.7
- depends-on:
  - INVARIANT-S2 / Axiom 1 (lattice pitch $\ell_{node}$; minimum tube diameter $d \equiv 1\,\ell_{node}$ forcing ropelength $2\pi$)
  - INVARIANT-S2 / Axiom 2 (topo-kinematic isomorphism; 1D ropelength integral replacing the 3D point-volume integral)
  - INVARIANT-S2 / Axiom 4 (saturation kernel — for the running-coupling sketch only)
- solidity: 0.70 (ok to build on, see caveats) [= min(0.70, 1.00)]
- rationale: The ropelength self-energy resolution $U_{AVE}=\oint T_{EM}\,ds = T_{EM}\cdot\ell_{node}=1.0\,m_ec^2$ closes cleanly as a 1D-loop integral, and $C_{loop}=\ell_{node}$ follows by algebra. But the absolute $m_e$ scale enters through the definitional couple $T_{EM}=m_ec^2/\ell_{node}$ (not derived), the Beltrami $\nabla\times\mathbf{A}=k\mathbf{A}$ form is an explicit ansatz, and the running-coupling content is flagged in the leaf as a sketch (static dielectric-saturation form, not a $\beta$-function). Disclosed-bound rather than a fully closed first-principles derivation.
- strengthen-by:
  - Derive the Beltrami closed-loop ansatz from Axiom 1 + Axiom 3 (minimum reflection) rather than positing it.
  - Replace the running-coupling sketch with a momentum-dependent RG flow derived from the Axiom 4 kernel, with a bounded comparison to the QED $\beta$-function.

---

## Proton Mass Eigenvalue ($m_p/m_e \approx 1836.12$)
<!-- id: clm-mnb3lt -->

- $x_{core} = \mathcal{I}_{scalar} + (\mathcal{V}_{total}\cdot p_c)\,x_{core}$ with $\mathcal{V}_{total} = 2.0$, $p_c = 8\pi\alpha$, $\mathcal{I}_{scalar} \approx 1162$, plus $+1$ integer twist for charge → $x = 1836.12$.
- _Specific Claims_
  - The $0.002\%$ agreement with empirical $m_p/m_e$ is computed from the cinquefoil-confined ($r_{opt} = \kappa_{FS}/5$) Faddeev-Skyrme functional with thermal softening $\delta_{th} = 1/(14\pi^2)$ and Axiom 4 gradient saturation inside the integrand. Per the cross-cutting Master Prediction Table classification: this is a **category (iv) derived prediction**, not an identity or fit.
  - The $+1$ integer twist contribution is a structurally mandated topological invariant (charge constraint), not a fitted offset.
  - $\kappa_{FS}^{(cold)} = p_c/\alpha = 8\pi$ is a **derived geometric coupling** (solid-angle $4\pi$ × bilateral chiral factor $2$), not a phenomenological input.
- _Specific Non-Claims and Caveats_
  - The $\rho_{threshold} = 1 + \sigma/4 \approx 1.1062$ mutual-coupling derivation is **closed-form conditional on a Gaussian radial profile** with FWHM $= \ell_{node}$. Axiom 1 fixes the FWHM but not the functional form; the Gaussian is an explicit ansatz. Replacing it with the framework-consistent Axiom-4 LC profile is an acknowledged outstanding rigour gap (see `mathematical-closure.md`) — but the gap binds $\rho_{threshold}$ **only**. It does NOT bind $\mathcal{V}_{total} = 2$: that "2" is the **profile-independent dual-reactance count** ($X_C + X_L$ sectors, Axiom 1; counted, not integrated; canonical at `common/dual-reactance-storage-taxonomy.md`), mass-confirmed via $m_p$ irrespective of profile. (The legacy "FEM convergence to $\mathcal{V}_{sat} = 2.0$" is a voxel-quadrature integral of the Gaussian-ansatz saturated overlap volume — a $\rho_{threshold}$ consistency check — NOT a derivation of the reactance count; do not fuse the two.)
  - Does NOT claim a derivation of $\delta_{th} = 1/(14\pi^2)$ that is independent of the proton-mass calibration. The factor combines $\nu_{vac}/\kappa_{cold} \times 2/\pi$ with prior gradient-saturation already inside the functional; treat as a structural correction, not an additional free parameter.
  - $\mathcal{I}_{scalar} \approx 1162$ is a **numerical** output of the 1D Faddeev-Skyrme solver at the cinquefoil radius with thermal softening; it is not algebraically closed-form.

> **Leaf references:** [self-consistent-mass-oscillator](./particle-physics/ch02-baryon-sector/self-consistent-mass-oscillator.md), [thermal-softening](./particle-physics/ch02-baryon-sector/thermal-softening.md), [topological-fractionalization](./particle-physics/ch02-baryon-sector/topological-fractionalization.md).

### Quality
- confidence: 0.7
- depends-on:
  - INVARIANT-S2 / Axiom 1 (lattice pitch; FWHM $=\ell_{node}$; Borromean skew-line geometry)
  - INVARIANT-S2 / Axiom 4 (gradient saturation inside the Faddeev-Skyrme integrand)
  - clm-9s9apq (packing fraction $p_c=8\pi\alpha$; vol1)
  - clm-h9aqmt (electron unknot / $m_e$ baseline for the $+1$ integer-twist mass)
  - clm-8c3yhs ($(2,3)$ torus-knot uniqueness — the $(2,q_{odd})$ ladder structure tabulated in this leaf rests on the same coprimality + minimality knot-theoretic foundation that selects $(2,3)$ as the smallest non-trivial coprime torus knot; the ladder's starting point at $q=3$ is structurally downstream of clm-8c3yhs)
- solidity: 0.63 (use as input only, don't build deeper) [= min(0.70, 0.63)]
- rationale: The self-consistent eigenvalue $x=\mathcal{I}_{scalar}/(1-\mathcal{V}_{total}p_c)+1$ closes algebraically with $\mathcal{V}_{total}=2$ the profile-independent dual-reactance count (forced reactance-sector count $X_C+X_L$, Axiom 1; mass-confirmed). The band is pinned by two disclosed dependencies the leaf states explicitly: $\mathcal{I}_{scalar}\approx1162$ is a numerical solver output (not closed-form), and the $\rho_{threshold}=1.1062$ derivation is closed-form only *conditional on a Gaussian flux-tube ansatz* (Axiom 1 fixes the FWHM but not the profile — an acknowledged outstanding rigour gap that binds $\rho_{threshold}$, NOT $\mathcal{V}_{total}$). Disclosed methodology bound.
- strengthen-by:
  - Derive the flux-tube radial profile from Axiom 4 LC dynamics (or substitute the algebraic $\sqrt{1-r^2}$ kernel) and re-evaluate $\rho_{threshold}$, closing the Gaussian-ansatz gap.
  - Document the 1D Faddeev-Skyrme solver and demonstrate $\mathcal{I}_{scalar}$ has no tunable parameter.

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

> **Leaf references:** [knot-mode-isomorphism](./appendices/app-f-solver-toolchain/knot-mode-isomorphism.md), [torus-knot-ladder-toolchain](./appendices/app-f-solver-toolchain/torus-knot-ladder-toolchain.md), [torus-knot-ladder](./particle-physics/ch01-topological-matter/torus-knot-ladder.md), [torus-knot-ladder-baryons](./particle-physics/ch02-baryon-sector/torus-knot-ladder-baryons.md).

### Quality
- confidence: 0.6
- depends-on:
  - INVARIANT-S2 / Axiom 1 ($(2,q)$ odd-$q$ torus-knot stability; crossing-number confinement)
  - INVARIANT-S2 / Axiom 4 (gradient saturation in the eigenvalue functional)
  - clm-9s9apq (packing fraction $p_c=8\pi\alpha$; vol1)
  - clm-mnb3lt (proton-mass eigenvalue method, $c=5$ anchor and shared $\kappa_{FS}$, $\mathcal{V}_{total}$, $p_c$)
  - clm-8c3yhs ($(2,3)$ torus-knot uniqueness — the $(2,q_{odd})$ ladder enumerated in this leaf rests on the same coprimality + both-windings-$\geq 2$ + minimality argument; the ladder starts at $(2,3)$ and excludes $(2,4)$, $(2,6)$, etc. because those are not single-component knots, exactly the coprimality requirement clm-8c3yhs derives)
- solidity: 0.60 (use as input only, don't build deeper) [= min(0.60, 0.63)]
- rationale: The same closed-form eigenvalue $m(c)$ is applied across the odd-$c$ ladder with no parameters re-tuned between states, which is the load-bearing structural claim. But agreement is a $\sim2\%$ band against PDG $\Delta$/N resonances (proton row is by-construction $0.00\%$), and the "best hit" framing is one row, not a global accuracy claim. Inherits clm-mnb3lt's Gaussian-ansatz and numerical-$\mathcal{I}_{scalar}$ bounds. Disclosed-bound consistency family rather than a precision derivation.
- strengthen-by:
  - Report the full per-row error distribution and state-assignment provenance so the headline is not read off one best hit.
  - Close the upstream Gaussian-ansatz / $\mathcal{I}_{scalar}$ gaps inherited from clm-mnb3lt.

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

> **Leaf references:** [gauge-boson-masses](./particle-physics/ch05-electroweak-mechanics/gauge-boson-masses.md), [weinberg-angle](./particle-physics/ch05-electroweak-mechanics/weinberg-angle.md), [higgs-mechanism](./particle-physics/ch06-electroweak-higgs/higgs-mechanism.md).

### Quality
- confidence: 0.85
- depends-on:
  - INVARIANT-S2 / Axiom 1 (cylindrical flux-tube model, $d\equiv1\,\ell_{node}$, giving PAT $J=2I$)
  - $\nu_{vac}=2/7$ (vacuum Poisson ratio; substrate-anchored framework input)
- solidity: 0.85 (ok to build on) [= min(0.85, 1.00)]
- rationale: A clean closed algebraic chain: $J=2I$ is the Perpendicular Axis Theorem for any circular cross-section (geometric identity), the isotropic relation $E=2G(1+\nu)$ is standard elasticity, and substituting $\nu_{vac}=2/7$ gives $(M_W/M_Z)^2=7/9$ and $\sin^2\theta_W=2/9$ with zero free parameters. The only disclosed imports are $\nu_{vac}$ and the on-shell-scheme caveat (must not be compared to $\overline{MS}$). Derivation closes end-to-end modulo those imports.
- strengthen-by:
  - Derive $\nu_{vac}=2/7$ inside this leaf (or pin its primary source) so the chain is self-contained.
  - Add the one-loop on-shell$\to\overline{MS}$ map to show the framework can reach the running scheme rather than only the tree pole ratio.

---

## $W$/$Z$ Boson Masses
<!-- id: clm-q8un7j -->

- $m_W = m_e/(\alpha^2 p_c \sqrt{3/7})$, $m_Z = m_W \cdot 3/\sqrt{7}$
- _Specific Claims_
  - Both $M_W$ ($-0.57\%$ vs $80{,}379$ MeV) and $M_Z$ ($-0.62\%$ vs $91{,}188$ MeV) are derived from $m_e$, $\alpha$, $\nu_{vac} = 2/7$, and $p_c = 8\pi\alpha$. The $\alpha^2$ scaling reflects the $W$ self-energy as a **two-vertex process** (second-order perturbation theory in the chiral susceptibility); the $\sqrt{3/7}$ factor is the PAT torsion-shear projection. <!-- 🔴 OPEN FLAG (Rule 12): the "PAT torsion-shear" label on $\sqrt{3/7}$ is contested — $\sqrt{3/7} = \sqrt{1-2\nu_{vac}}$ at $\nu_{vac}=2/7$ is the dilatational/bulk elastic signature, not deviatoric/shear. See the canonical 🔴 flag in ch06-electroweak-higgs/lepton-spectrum.md (Generation 2) + common/full-derivation-chain.md. Grant's physics adjudication pending; label preserved unchanged. -->
- _Specific Non-Claims and Caveats_
  - Does NOT claim derivation of the Higgs VEV $v = 246$ GeV from independent first principles. The Higgs mechanism is reinterpreted (see Higgs Mass entry below) — VEV is identified with $Z_0 = 376.73\,\Omega$ characteristic impedance.
  - Does NOT claim the $W$/$Z$ widths or branching ratios are derived in the same chain. Only the pole masses and the on-shell mixing angle.
  - The $+1.24\%$ muon and $-0.95\%$ tau mass agreements reuse the same $\alpha$, $p_c$, $\sqrt{3/7}$ structure (Cosserat lepton spectrum); these are **not** independent validations of $W$/$Z$ — they are siblings on the same hierarchy $m_e \xrightarrow{\alpha\sqrt{3/7}} m_\mu \xrightarrow{\alpha\,p_c} m_\tau \xrightarrow{\alpha\,p_c} M_W$.

> **Leaf references:** [gauge-boson-masses](./particle-physics/ch05-electroweak-mechanics/gauge-boson-masses.md), [weak-coupling](./particle-physics/ch05-electroweak-mechanics/weak-coupling.md), [higgs-mass](./particle-physics/ch06-electroweak-higgs/higgs-mass.md), [lepton-spectrum](./particle-physics/ch06-electroweak-higgs/lepton-spectrum.md), [spontaneous-symmetry-breaking](./particle-physics/ch06-electroweak-higgs/spontaneous-symmetry-breaking.md).

### Quality
- confidence: 0.7
- depends-on:
  - INVARIANT-S2 / Axiom 1 (ring topology $2\pi$ enhancement; PAT $\sqrt{3/7}$ from $J=2I$)
  - INVARIANT-S2 / Axiom 4 ($\alpha^2$ two-vertex dielectric coupling)
  - clm-9s9apq (packing fraction $p_c=8\pi\alpha$; vol1)
  - clm-5zuo7g (on-shell mixing ratio $M_W/M_Z=\sqrt{7}/3$ used for $M_Z$)
- solidity: 0.63 (use as input only, don't build deeper) [= min(0.70, 0.63)]
- rationale: The $M_W=m_e/(\alpha^2 p_c\sqrt{3/7})$ factor-chain is given a first-principles origin for each factor ($\pi$ spherical, $2\pi$ ring, $\alpha^2$ two-vertex, $p_c$ packing, $\sqrt{3/7}$ PAT) and closes to a number ($-0.57\%$ on $M_W$, $-0.62\%$ on $M_Z$). The $\alpha^2$-as-two-vertex identification and the torsional permittivity decomposition are asserted (motivated by analogy to Coulomb self-energy), and the chain rests on disclosed imports ($p_c$, $\sqrt{3/7}$, the $m_e$ baseline). Disclosed methodology bound.
- strengthen-by:
  - Derive the torsional permittivity ratio $\varepsilon_T/\mu=\pi\alpha^2 p_c\sqrt{3/7}$ from the Cosserat constitutive law rather than assembling it factor-by-factor by analogy.
  - Add an independent check of the $W$/$Z$ widths from the same self-energy structure.

---

## Higgs Mechanism Reinterpretation
<!-- id: clm-p7rfkb -->

- _Specific Claims_
  - AVE identifies the Standard Model VEV $v = 246$ GeV with the **characteristic impedance of free space** $Z_0 = \sqrt{\mu_0/\varepsilon_0} \approx 376.73\,\Omega$. Inertial mass is reinterpreted as Lenz's-law induction drag against this baseline impedance.
  - The empirical $125$ GeV LHC resonance is interpreted as a **transient acoustic relaxation mode** of the LC network, not a fundamental scalar field excitation.
  - $m_H/v = 1/\sqrt{N_{K4}}$ with $N_{K4} = 4$ (K4 cell breathing), consistent with Master Prediction Table #25 ($-0.55\%$).
- _Specific Non-Claims and Caveats_
  - This is an **ontological reinterpretation**: the same numerical $v = 246$ GeV underlies all SM electroweak predictions. AVE does not produce a Higgs-free Standard Model with different observable predictions at the EW scale.
  - Does NOT claim the $125$ GeV LHC peak is "not the Higgs". The framework asserts the resonance exists with a different physical mechanism (acoustic relaxation), not that the experimental signal is absent or misidentified.
  - The reinterpretation does not produce new electroweak observables distinguishable from the SM Higgs picture without testing the acoustic-relaxation hypothesis directly (e.g., width, decay channel anomalies) — none currently demonstrated.

> **Leaf references:** [higgs-mass](./particle-physics/ch06-electroweak-higgs/higgs-mass.md), [higgs-mechanism](./particle-physics/ch06-electroweak-higgs/higgs-mechanism.md), [spontaneous-symmetry-breaking](./particle-physics/ch06-electroweak-higgs/spontaneous-symmetry-breaking.md).

### Quality
- confidence: 0.3
- depends-on:
  - INVARIANT-S2 / Axiom 1 (LC network; $Z_0=\sqrt{\mu_0/\varepsilon_0}$ baseline impedance)
  - INVARIANT-S2 / Axiom 4 (saturation/relaxation framing for the 125 GeV acoustic mode)
- solidity: 0.30 (do not build on, rework needed) [= min(0.30, 1.00)]
- rationale: An ontological reinterpretation asserted at the mechanism level: VEV $\leftrightarrow Z_0=376.73\,\Omega$, inertia as Lenz-law induction drag, the 125 GeV peak as an acoustic relaxation mode, and $m_H/v=1/\sqrt{N_{K4}}$ with $N_{K4}=4$. The numerical $v=246$ GeV is unchanged from the SM and no new distinguishable observable is produced; the $1/\sqrt{4}$ mass ratio is a structural identification, not a closed derivation. Claimed mechanism without derivation.
- strengthen-by:
  - Derive $m_H/v=1/\sqrt{N_{K4}}$ from the K4-cell breathing dynamics quantitatively rather than asserting $N_{K4}=4$.
  - Produce at least one acoustic-relaxation observable (width/decay-channel signature) that distinguishes the reinterpretation from the SM Higgs.

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

> **Leaf references:** [higgs-mass](./particle-physics/ch06-electroweak-higgs/higgs-mass.md).

### Quality
- confidence: 0.75
- depends-on:
  - INVARIANT-S2 / Axiom 1 (unknot ring diameter $2R=\ell/\pi$ giving form factor $1/\pi^2$)
  - INVARIANT-S2 / Axiom 4 (nonlinear capacitive saturation $\to \langle\delta C/C\rangle=\pi\alpha$)
  - clm-h9aqmt (unknot geometry / on-site strain identity)
- solidity: 0.70 (ok to build on, see caveats) [= min(0.75, 0.70)]
- rationale: The chain $a_e=(1/\pi^2)\times(\pi\alpha/2)=\alpha/2\pi$ reproduces the Schwinger value ($+0.09\%$) from stated geometry: $(V_{peak}/V_{snap})^2=4\pi\alpha$ is an exact on-site-strain identity, the time-average gives $\pi\alpha$, and the form factor $1/\pi^2=(2R/\ell)^2$ from Axiom 1. Classification is a consistency check (reproduces a known QED result via an alternative mechanism); the decomposition into form-factor $\times$ resonance-shift is mildly assembled-to-target. Clean local derivation modulo that assembly.
- strengthen-by:
  - Show the $1/\pi^2$ form factor and the $\pi\alpha/2$ resonance shift arise jointly from one variational calculation, not as two independently-motivated factors multiplied to land on $\alpha/2\pi$.
  - Extend the mechanism to the $\alpha^2$ term to test whether it tracks the QED higher-order coefficient.

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

> **Leaf references:** [chiral-screening](./particle-physics/ch03-neutrino-sector/chiral-screening.md), [delta-cp-violation](./particle-physics/ch03-neutrino-sector/delta-cp-violation.md), [pmns-eigenvalues](./particle-physics/ch03-neutrino-sector/pmns-eigenvalues.md), [pmns-junction-model](./particle-physics/ch03-neutrino-sector/pmns-junction-model.md).

### Quality
- confidence: 0.6
- depends-on:
  - INVARIANT-S2 / Axiom 1 (K4 3-connectivity = trefoil $c=3$ = $\Delta c_{crit}$; torus-knot crossing numbers)
  - $\nu_{vac}=2/7$ (compliance-mode allocation $\to \sin^2\theta_{12}^{(0)}$)
- solidity: 0.60 (use as input only, don't build deeper) [= min(0.60, 1.00)]
- rationale: The four PMNS parameters are closed crossing-number/regime-boundary expressions ($\le1.0\%$ vs NuFIT 5.2, all within 1$\sigma$), and the $\delta_{CP}$ three components have distinct disparate-physics origins (not post-hoc summed). But each boundary-condition identification (compliance / impedance-matched / screened) is asserted, and the leaf's own 2026-05-17 scope-correction box states the starting value $c_1=5$ is NOT derived from substrate primitives, reclassifying $\sin^2\theta_{13}$ from emergence to consistency check. Disclosed methodology bound with an acknowledged un-derived input.
- strengthen-by:
  - Derive the absolute ladder start $c_1=5$ from substrate primitives (currently only the $\Delta c=2$ spacing is derived from $\nu_{vac}$).
  - Replace the three asserted regime-boundary identifications with a single mode-coupling calculation that produces all three $\sin^2\theta$ values.

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

> **Leaf references:** [delta-cp-violation](./particle-physics/ch03-neutrino-sector/delta-cp-violation.md), [pmns-eigenvalues](./particle-physics/ch03-neutrino-sector/pmns-eigenvalues.md), [lepton-spectrum](./particle-physics/ch06-electroweak-higgs/lepton-spectrum.md).

### Quality
- confidence: 0.55
- depends-on:
  - INVARIANT-S2 / Axiom 1 (torus-knot crossing-number flavor splitting; $1/c^2$ torsional coupling)
  - INVARIANT-S2 / Axiom 4 (dielectric coupling $\alpha$ between Cosserat sectors)
  - clm-q8un7j (W-boson scale $M_W$ entering $m_\nu=m_e\,\alpha\,(m_e/M_W)$)
- solidity: 0.55 (use as input only, don't build deeper) [= min(0.55, 0.63)]
- rationale: The suppression form $m_\nu=m_e\,\alpha\,(m_e/M_W)\approx0.024$ eV is a closed formula once $M_W$ is in hand, and the $\Delta m^2$-ratio agreement ($\sim3\%$) follows from $m_i\propto1/c_i^2$. But the factor identification ($\alpha$ = inter-sector dielectric coupling, $m_e/M_W$ = translational/torsional energy ratio) is asserted as physical-meaning labels, per-eigenstate values are inferred from baryon pairing (not measured), and the $\sum m_\nu$ comparison is a cosmological upper bound (consistency, not validation). The inverted-hierarchy commitment is the falsifiable load-bearing content.
- strengthen-by:
  - Derive the $\alpha\,(m_e/M_W)$ suppression factor from the Cosserat inter-sector coupling rather than labeling it.
  - Pin the three per-eigenstate masses to an independent constraint instead of inferring them from the torus-knot pairing.

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

> **Leaf references:** [quark-flavors](./particle-physics/ch02-baryon-sector/quark-flavors.md), [topological-fractionalization](./particle-physics/ch02-baryon-sector/topological-fractionalization.md).

### Quality
- confidence: 0.75
- depends-on:
  - INVARIANT-S2 / Axiom 1 ($6^3_2$ Borromean linkage with $\mathbb{Z}_3$ permutation symmetry)
  - INVARIANT-S2 / Axiom 2 (charge = integer topological winding; $Q_{total}=+1e$)
- solidity: 0.75 (ok to build on, see caveats) [= min(0.75, 1.00)]
- rationale: Given the Witten relation $q_{eff}=n+(\theta/2\pi)e$ and $\theta\in\{0,\pm2\pi/3,\pm4\pi/3\}$, the fractional charges $\pm1/3,\pm2/3$ follow by exact substitution — a clean closed evaluation. The two disclosed imports are the Witten Effect itself (standard topological-field-theory result, adopted) and the restriction of $\theta$ to thirds, which rests on the asserted $\mathbb{Z}_3$ symmetry of the Borromean cage. Does not derive quark masses (those are separate scale-invariance entries). Disclosed methodology bound.
- strengthen-by:
  - Derive the $\theta$-vacuum / Witten-charge coupling from the AVE lattice dielectric response rather than importing it.
  - Show $\mathbb{Z}_3$ is forced (not merely consistent) for the proton's Borromean ground state.

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

> **Leaf references:** [sm-translation-toolchain](./appendices/app-f-solver-toolchain/sm-translation-toolchain.md), [methodological-contamination](./proofs-computation/ch09-computational-proof/methodological-contamination.md), [analog-ladder-filter](./quantum-orbitals/ch07-quantum-mechanics/analog-ladder-filter.md), [atom-as-radial-waveguide](./quantum-orbitals/ch07-quantum-mechanics/atom-as-radial-waveguide.md), [chiral-factor](./quantum-orbitals/ch07-quantum-mechanics/chiral-factor.md), [complete-solver-architecture](./quantum-orbitals/ch07-quantum-mechanics/complete-solver-architecture.md), [de-broglie-n](./quantum-orbitals/ch07-quantum-mechanics/de-broglie-n.md), [de-broglie-standing-wave](./quantum-orbitals/ch07-quantum-mechanics/de-broglie-standing-wave.md), [dual-formalism-architecture](./quantum-orbitals/ch07-quantum-mechanics/dual-formalism-architecture.md), [geometry-pipeline](./quantum-orbitals/ch07-quantum-mechanics/geometry-pipeline.md), [helium-coupling-first-principles](./quantum-orbitals/ch07-quantum-mechanics/helium-coupling-first-principles.md), [ionization-energy-validation](./quantum-orbitals/ch07-quantum-mechanics/ionization-energy-validation.md), [knot-vs-orbital-table](./quantum-orbitals/ch07-quantum-mechanics/knot-vs-orbital-table.md), [macro-cavity-saturation](./quantum-orbitals/ch07-quantum-mechanics/macro-cavity-saturation.md), [ode-verification](./quantum-orbitals/ch07-quantum-mechanics/ode-verification.md), [operator-domain-table](./quantum-orbitals/ch07-quantum-mechanics/operator-domain-table.md), [orbital-penetration-penalties](./quantum-orbitals/ch07-quantum-mechanics/orbital-penetration-penalties.md), [scale-separation](./quantum-orbitals/ch07-quantum-mechanics/scale-separation.md), [stepped-impedance-resonator](./quantum-orbitals/ch07-quantum-mechanics/stepped-impedance-resonator.md), [subshell-junction-scattering](./quantum-orbitals/ch07-quantum-mechanics/subshell-junction-scattering.md).

### Quality
- confidence: 0.55
- depends-on:
  - INVARIANT-S2 / Axiom 1 (radial waveguide; standing-wave $r_n=n^2a_0/Z$; angular momentum)
  - INVARIANT-S2 / Axiom 2 (Coulomb $V=-Z_{net}\alpha\hbar c/r$; Gauss screening)
  - INVARIANT-S2 / Axiom 4 (soliton mass / dispersion $\to k(r)$)
  - INVARIANT-N3 (Op2–Op6 operator chain)
  - clm-h9aqmt (single-electron unknot mass/Compton baseline underlying the Step-1 eigenvalue)
  - clm-qde5gn (deterministic Helmholtz-cavity basis for the radial eigenvalue solver)
- solidity: 0.55 (use as input only, don't build deeper) [= min(0.55, 0.70)]
- rationale: The single-electron eigenvalue ($Ry$ emergent, $r_n=n^2a_0/Z$) and H/He/Li results ($\le1.5\%$) close cleanly, and the corrections A–D have stated gate conditions. But the leaf documents that for Be ($11.9\%$) and B the corrections are applied *outside* the phase integral — "violating the action principle" — with the complete-phase-integral architecture (E2k) still in-progress and unvalidated $Z\ge5$; the Li residual is internally inconsistent ($+2.46\%$ vs $-1.2\%$). The $\pm2.8\%$ headline averages over a real per-element spread. Substantive acknowledged open dependency.
- strengthen-by:
  - Land the E2k complete-phase-integral architecture (all operators inside $V(r)$) and re-validate $Z=5$–14 end-to-end.
  - Reconcile the Li per-element residual so a single canonical value is reported.

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

> **Leaf references:** [atom-as-radial-waveguide](./quantum-orbitals/ch07-quantum-mechanics/atom-as-radial-waveguide.md), [bonding-mode-formula](./quantum-orbitals/ch07-quantum-mechanics/bonding-mode-formula.md), [chiral-factor](./quantum-orbitals/ch07-quantum-mechanics/chiral-factor.md), [helium-coupling-first-principles](./quantum-orbitals/ch07-quantum-mechanics/helium-coupling-first-principles.md), [helium-symmetric-cavity](./quantum-orbitals/ch07-quantum-mechanics/helium-symmetric-cavity.md), [hierarchical-cascade-correction](./quantum-orbitals/ch07-quantum-mechanics/hierarchical-cascade-correction.md), [radial-eigenvalue-solver](./quantum-orbitals/ch07-quantum-mechanics/radial-eigenvalue-solver.md), [scale-separation](./quantum-orbitals/ch07-quantum-mechanics/scale-separation.md), [screening-rule](./quantum-orbitals/ch07-quantum-mechanics/screening-rule.md), [subshell-junction-scattering](./quantum-orbitals/ch07-quantum-mechanics/subshell-junction-scattering.md).

### Quality
- confidence: 0.5
- depends-on:
  - INVARIANT-S2 / Axiom 2 (cross-shell Gauss screening $\sigma_{cross}=N_{inner}$)
  - INVARIANT-S2 / Axiom 4 (same-shell chiral coupling $J_{shell}$ via Op4)
  - INVARIANT-N3 (Op4 potential well; coupled-line even/odd-mode formalism)
  - clm-9s9apq (packing fraction $p_c$ in $J_{1s^2}=(1+p_c)/2$; vol1)
- solidity: 0.50 (use as input only, don't build deeper) [= min(0.50, 0.63)]
- rationale: The two-screening-physics distinction (integer Gauss cross-shell vs chiral $J_{shell}$ same-shell) and the He bonding-mode result ($-0.88\%$) are clean. But the leaf explicitly states "Be and B remain open: the corrections are applied outside the phase integral, violating the action principle," and the complete-phase-integral architecture (E2k) is presented as in-progress, not yet validated end-to-end for $Z\ge5$. The same-shell coupled-microstrip formalism is asserted by cross-scale isomorphism with no independent atomic-scale validation past the Hopf-pair Be result. Substantive open dependency the leaf acknowledges.
- strengthen-by:
  - Complete and validate the E2k action-consistent same-shell treatment for B and beyond.
  - Independently validate the coupled-line even/odd-mode same-shell coupling at the atomic scale rather than importing it from protein/antenna analogy.

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

> **Leaf references:** [spin-half-paradox](./appendices/app-b-paradoxes/spin-half-paradox.md), [finkelstein-misner-spin-half-derivation](./particle-physics/ch01-topological-matter/finkelstein-misner-spin-half-derivation.md), [spin-gyroscopic-isomorphism](./particle-physics/ch01-topological-matter/spin-gyroscopic-isomorphism.md), [larmor-derivation](./particle-physics/ch04-quantum-spin/larmor-derivation.md), [spin-as-precession](./particle-physics/ch04-quantum-spin/spin-as-precession.md), [visual-equivalence](./particle-physics/ch04-quantum-spin/visual-equivalence.md).

### Quality
- confidence: 0.8
- depends-on:
  - INVARIANT-S2 / Axiom 1 (extended $0_1$ unknot; $SU(2)\to SO(3)$ double cover via Finkelstein-Misner kink)
  - clm-h9aqmt (electron-unknot topological-flywheel identification)
- solidity: 0.70 (ok to build on, see caveats) [= min(0.80, 0.70)]
- rationale: Given the topological-flywheel premise, the Larmor result $\omega_L=\gamma B_0$ follows from clean classical gyroscope mechanics ($d\mathbf{L}/dt=\gamma\mathbf{L}\times\mathbf{B}$), and the gyroscope-ODE $\leftrightarrow$ Bloch-sphere $SU(2)$ equivalence is standard mathematics (the $\sim10^{-8}$ deviation is integration tolerance) — a consistency check reproducing standard QM single-particle spin observables. The disclosed import is the flywheel ontology itself; multi-particle entanglement is explicitly out of scope. Clean derivation on a disclosed premise.
- strengthen-by:
  - Provide the explicit projection map showing the classical $\mathbf{L}$-vector and the Pauli spinor evolve identically, not just numerically close, including the $4\pi$ vs $2\pi$ period bookkeeping.
  - State which (if any) multi-spin correlation the mechanism can/cannot reproduce, to bound the equivalence claim.

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

> **Leaf references:** [yang-mills-steps1-2](./nuclear-field/ch12-millennium-prizes/yang-mills-steps1-2.md), [yang-mills-steps3-5](./nuclear-field/ch12-millennium-prizes/yang-mills-steps3-5.md).

### Quality
- confidence: 0.65
- depends-on:
  - INVARIANT-S2 / Axiom 1 (discrete pitch $\to$ UV cutoff; lattice dispersion)
  - INVARIANT-S2 / Axiom 4 (saturation cap $H_{cell}\le m_ec^2$)
  - clm-h9aqmt (unknot $0_1$ as the lightest topological defect = mass gap)
  - clm-oygz1i (Faddeev-Skyrme topological mass functional for the defect spectrum)
- solidity: 0.60 (use as input only, don't build deeper) [= min(0.65, 0.60)]
- rationale: Within the lattice framework the result is rigorous: $H\ge0$, $H_{cell}\le m_ec^2$, self-adjointness, and a Bogomol'nyi bound $E\ge2\pi^3c/\kappa_{FS}>0$ all close. The leaf carries a thorough, honest scope correction: the continuum limit is explicitly NOT taken, SU($N$) emergence from $(2,q)$ knots is an ansatz (not derived from YM field equations), Osterwalder-Schrader reconstruction is absent, and $\Delta=m_ec^2$ is the assumed lightest defect's energy. Framework-conditional, not Clay-rigorous; the SU($N$) step pins the band below the Navier-Stokes case.
- strengthen-by:
  - Derive SU($N$) emergence from the gauge dynamics rather than identifying it from torus-knot topology.
  - Prove (within ZFC, on the lattice) that the unknot is the unique globally-lightest stable defect.

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

> **Leaf references:** [navier-stokes-prize](./nuclear-field/ch12-millennium-prizes/navier-stokes-prize.md).

### Quality
- confidence: 0.7
- depends-on:
  - INVARIANT-S2 / Axiom 1 (rigid pitch $\ell$ $\to$ bounded discrete Laplacian $\|\nabla^2_\ell\|=4/\ell^2$)
  - INVARIANT-S2 / Axiom 4 (velocity clamp $|\mathbf{u}|\le c$)
- solidity: 0.70 (ok to build on, see caveats) [= min(0.70, 1.00)]
- rationale: The mathematics closes cleanly: a bounded discrete Laplacian + velocity cap + bounded enstrophy gives a Lipschitz ODE on a bounded domain, and Picard-Lindelöf then yields unique global existence — that step is sound. The leaf carries an explicit, honest scope correction: the result holds for a *modified* problem (UV cutoff + speed limit), not the Clay continuum statement, and promoting it requires a lattice-to-continuum limit theorem (open). Disclosed methodology bound: the derivation closes on a clearly-stated assumption.
- strengthen-by:
  - Supply (or cite) a lattice$\to$continuum limit theorem that preserves the enstrophy bound as $\ell\to0$.
  - Address the internal tension with Regime IV "topology rupture," which would itself be a singularity event.

---

## Strong CP Problem ($\theta = 0$ Exactly)
<!-- id: clm-gfs4j8 -->

- _Specific Claims_
  - On the AVE lattice the vacuum angle $\theta = 0$ exactly: the unique ground state has $\mathbf{E}_n = \mathbf{B}_n = 0$ and zero topological charge. Transitions between $\theta$-sectors require creating a topological defect, which costs energy $\ge \Delta$ (the mass gap), so the vacuum cannot tunnel between sectors.
  - **No axion is needed** — the framework has zero free parameters for this prediction (vs Peccei-Quinn's $f_a$).
- _Specific Non-Claims and Caveats_
  - This is **NOT a Clay-rigorous result** and is not on the Clay list — but the same lattice-conditional caveat applies, as flagged in Master Prediction Table note #16. The "uniqueness of the AVE vacuum topology" is asserted, not formally proven against all possible competing ground states within ZFC.
  - Does NOT claim falsification of the QCD axion search programme. AVE asserts the axion is unnecessary within its framework, not that experimental axion searches will falsify a particle whose existence the framework already excludes.

> **Leaf references:** [quantitative-resolutions](./nuclear-field/ch10-open-problems/quantitative-resolutions.md), [strong-cp](./nuclear-field/ch10-open-problems/strong-cp.md).

### Quality
- confidence: 0.5
- depends-on:
  - INVARIANT-S2 / Axiom 1 (gauge structure from $(2,q)$ torus knots; quantized phase winding)
  - clm-q5izb7 (mass-gap barrier preventing inter-$\theta$-sector tunneling)
- solidity: 0.50 (use as input only, don't build deeper) [= min(0.50, 0.60)]
- rationale: The five-step proof has clean structure (zero-charge unique ground state $\to$ mass-gap barrier $\to$ no tunneling $\to \theta=0$), but the load-bearing step 1 asserts the AVE vacuum is *the unique* ground state with zero topological charge — a uniqueness against all competing ground states that the leaf itself flags as not formally proven within ZFC. The $\theta=0$ result is therefore as strong as that asserted uniqueness. Substantive open dependency.
- strengthen-by:
  - Prove the uniqueness of the zero-charge AVE vacuum topology against competing ground states.
  - Quantify the inter-sector tunneling suppression to show it is exactly (not approximately) zero.

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

> **Leaf references:** [baryon-asymmetry](./nuclear-field/ch10-open-problems/baryon-asymmetry.md), [g-star-derivation](./nuclear-field/ch10-open-problems/g-star-derivation.md), [g-star-prediction](./nuclear-field/ch10-open-problems/g-star-prediction.md), [quantitative-resolutions](./nuclear-field/ch10-open-problems/quantitative-resolutions.md).

### Quality
- confidence: 0.4
- depends-on:
  - INVARIANT-S2 / Axiom 1 (lattice/torus-knot chirality for C and CP violation)
  - $\nu_{vac}=2/7$ ($g_*=7^3/4$ degrees-of-freedom count)
  - clm-5zuo7g (weak coupling $\alpha_W=\alpha/\sin^2\theta_W$)
- solidity: 0.40 (do not build on, rework needed) [= min(0.40, 0.85)]
- rationale: The $0.38\%$ headline is a composite of factors each *assigned* a lattice origin rather than cleanly derived: $\delta_{CP}=\pi/\kappa_{FS}$ "the fraction asymmetric under mirror reflection" is asserted, $g_*=7^3/4$ is a numerological "$7$ modes cubed / $4$ K4 nodes" identification, and $C_{sph}=28/79$ uses asserted $N_f=3,N_H=1$ assignments — all fed into the imported electroweak-baryogenesis formula. Multi-factor cancellations make per-factor sensitivity hard to attribute. Asserted-partial.
- strengthen-by:
  - Derive $g_*=7^3/4$ from a genuine relativistic-DoF count rather than the mode-cubed-over-nodes heuristic.
  - Derive $\delta_{CP}=\pi/\kappa_{FS}$ from the lattice chirality dynamics, with a sensitivity analysis of the composite formula.

---

## Hubble Constant $H_\infty \approx 69.32$ km/s/Mpc — Vol 2 Framing
<!-- id: clm-mroghg -->

See cross-cutting [Master Prediction Table reading conventions](../claim-quality.md). Vol3 sidecar carries the full $H_\infty$ entry (lattice-genesis circularity caveat; CODATA $G$ substitution; geometric self-consistency proof, not first-principles ab initio prediction). Vol2 framing notes:

- _Specific Claims_
  - Vol 2 Ch 10's Hubble Tension leaf presents $H_\infty = 28\pi m_e^3 c G/(\hbar^2 \alpha^2) \approx 69.32$ km/s/Mpc as "every factor rigorously derived from lattice structure and bounding limits", positioned $+2.9\%$ above Planck (CMB) and $-5.1\%$ below SH0ES (local).
- _Specific Non-Claims and Caveats_
  - The framing-of-asymmetric-systematics ("CMB low-density-void calibration" vs "local Cepheid impedance calibration") is an **interpretive consequence**, not an independent quantitative derivation of either measurement's residual.
  - The cross-cutting circularity caveat (Vol3 sidecar: $R_H \equiv c/H_\infty$ enters $G$ via $\xi$, so rearranging back to "compute" $H_\infty$ from CODATA $G$ is structurally an identity) applies here as well. Treat the vol2 leaf's "every factor rigorously derived" wording as inheriting the vol3-documented caveat; do NOT summarise vol2's framing as a parameter-free first-principles prediction of $H_0$.

> **Leaf references:** [hubble-tension](./nuclear-field/ch10-open-problems/hubble-tension.md), [quantitative-resolutions](./nuclear-field/ch10-open-problems/quantitative-resolutions.md).

### Quality
- confidence: 0.7
- depends-on:
  - INVARIANT-S2 / Axiom 3 (Machian-impedance closure of $G$ that the $H_\infty$ identity rearranges)
- solidity: 0.70 (ok to build on, see caveats) [= min(0.70, 1.00)]
- rationale: The vol2 leaf is honest about what it is: $H_\infty=28\pi m_e^3 cG/(\hbar^2\alpha^2)\approx69.32$ km/s/Mpc is explicitly a geometric self-consistency identity (the same algebraic relation as $G$'s Machian closure written two ways), with the $R_H\equiv c/H_\infty$ circularity disclosed verbatim. The algebra closes by identity; the numerical value follows from CODATA $G$. It carries no novel first-principles content (its own framing), and the asymmetric-systematics CMB-vs-local explanation is interpretive. Disclosed-bound identity rearrangement — clean but content-light.
- strengthen-by:
  - Supply the open Chain B' derivation of $G$ from substrate-local thermodynamics that does not route through $R_H$, which would promote this from consistency identity to a prediction.
  - Quantify the claimed CMB-void vs local-Cepheid impedance-calibration residuals rather than framing them qualitatively.

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

> **Leaf references:** [planck-scale-derivation](./nuclear-field/ch08-planck-string/planck-scale-derivation.md), [string-theory-translation](./nuclear-field/ch08-planck-string/string-theory-translation.md).

### Quality
- confidence: 0.65
- depends-on:
  - INVARIANT-S2 / Axiom 1 (finite transverse flux-tube radius $d\equiv1\,\ell_{node}$)
  - INVARIANT-S2 / Axiom 4 (UV regulator; Faddeev-Skyrme 3D stabilization)
  - clm-h9aqmt (unknot inductive energy $\to T_{AVE}=m_e^2c^3/\hbar$)
  - clm-mnb3lt (baryon mass-stiffening $m_p/m_e$ for $\alpha'_{baryon}$)
- solidity: 0.63 (use as input only, don't build deeper) [= min(0.65, 0.63)]
- rationale: $T_{AVE}=m_e^2c^3/\hbar\approx0.212$ N is clean dimensional algebra from the unknot tension, and $\alpha'=1/(2\pi T)$ is the standard Nambu-Goto relation — dimensionally exact. But the result is explicitly $17\%$ off the empirical hadronic $\alpha'\approx0.9$ GeV$^{-2}$ (order-of-magnitude, not precision), the $\alpha'_{baryon}$ match is "within an order of magnitude," and equating the fundamental EM string tension to the hadronic Regge slope is an asserted identification. Disclosed-bound: clean algebra, disclosed accuracy gap, asserted EM$\leftrightarrow$hadronic mapping.
- strengthen-by:
  - Account for the $17\%$ gap (e.g. derive the EM$\to$hadronic correction) rather than reporting it as order-of-magnitude consistency.
  - Derive a meson Regge trajectory (mass vs spin) from the same tension to test beyond the single slope number.

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

> **Leaf references:** [cross-domain-physics-mappings](./appendices/app-f-solver-toolchain/cross-domain-physics-mappings.md), [overdrive-comparison](./proofs-computation/ch11-overdrive/overdrive-comparison.md), [overdrive-nuclear](./proofs-computation/ch11-overdrive/overdrive-nuclear.md), [overdrive-protein](./proofs-computation/ch11-overdrive/overdrive-protein.md), [universal-energy](./proofs-computation/ch11-overdrive/universal-energy.md).

### Quality
- confidence: 0.55
- depends-on:
  - INVARIANT-S2 / Axiom 3 (impedance-minimizing gradient descent / minimum reflection)
  - INVARIANT-S2 / Axiom 4 (saturation inside the coupling)
  - INVARIANT-N3 (shared operator chain across domains)
- solidity: 0.55 (use as input only, don't build deeper) [= min(0.55, 1.00)]
- rationale: The strain functional $U_{total}=\sum K_{mutual}/d_{ij}+\sum U_{bond}$ and gradient-descent are stated as a standard energy-minimization form; the load-bearing content is the "single unmodified $O(N^2)$ solver across two domains" scale-invariance claim plus the computational results (U-235 binding sub-% through actinides / $<0.01\%$ for $A\le28$; polyalanine $\phi,\psi$ dihedrals). But $K_{mutual}=(5\pi/2)\alpha\hbar c/(1-\alpha/3)$ is asserted/imported with a nuclear-specific $\alpha/3$ correction, per-actinide errors are not reported, and the protein result is structural (geometry recovered, not folding thermodynamics). Computational validation with disclosed bounds.
- strengthen-by:
  - Derive $K_{mutual}$ (including the $\alpha/3$ nuclear correction) from AVE primitives rather than asserting the coupling constant.
  - Report per-actinide error breakdowns to substantiate the "sub-percent through actinides" claim.

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

> **Leaf references:** [sm-translation-toolchain](./appendices/app-f-solver-toolchain/sm-translation-toolchain.md), [methodological-contamination](./proofs-computation/ch09-computational-proof/methodological-contamination.md), [precision-policy](./proofs-computation/ch09-computational-proof/precision-policy.md), [ode-verification](./quantum-orbitals/ch07-quantum-mechanics/ode-verification.md), [qm-ave-translation](./quantum-orbitals/ch07-quantum-mechanics/qm-ave-translation.md).

### Quality
- confidence: 0.7
- depends-on:
  - INVARIANT-S2 / Axiom 1 (cavity saturation boundary $r_{sat}=a_0=\ell_{node}/\alpha$; standing-wave radii)
  - INVARIANT-S2 / Axiom 2 (Gauss cross-shell screening)
  - INVARIANT-N3 (operator-boundary tripwires Op4/Op6 etc.)
  - clm-oltvwy (atomic IE solver this discipline governs)
- solidity: 0.55 (use as input only, don't build deeper) [= min(0.70, 0.55)]
- rationale: This is a methodological discipline statement (true-by-construction within the framework: "all atomic states must emerge from the 5-step method, never $Z_{eff}^2 Ry/n^2$"), not an empirical prediction — so it cannot be falsified by a measurement, but it is backed by clean supporting derivations ($Ry$ emergent from the cavity-saturation boundary; $r_n\propto n^2$ from the standing-wave condition, both shown algebraically). The band reflects a well-grounded boundary plus its clean supporting algebra rather than a closed numerical prediction.
- strengthen-by:
  - Add a mechanical contamination-detector check (e.g. a unit test) that flags any downstream reuse of the forbidden $Z_{eff}^2 Ry/n^2$ form.
  - Strengthen by closing the clm-oltvwy E2k action-consistent architecture so the discipline is satisfied end-to-end, not just stated.

---

## Holographic Principle Recovery (Stress Test, Not Independent Prediction)
<!-- id: clm-nhlo1e -->

- _Specific Claims_
  - Even though the AVE vacuum is a discrete 3D lattice, the Holographic Principle's $R^2$ entropy scaling is recovered: information transmission traverses 1D inductive flux tubes whose bandwidth is bounded by their 2D cross-sectional porosity $\Phi_A \equiv \alpha^2$. Nyquist-Shannon projects channel capacity onto the 2D causal-horizon bounding surface.
- _Specific Non-Claims and Caveats_
  - This is a **stress-test resolution** (App B paradoxes), demonstrating internal consistency of the lattice picture against an established constraint — not an independent quantitative derivation of the Bekenstein-Hawking entropy formula. The cross-sectional-porosity argument is presented as the geometric mechanism, not a calculation of $S_{BH} = A/(4\ell_P^2)$ ab initio.
  - Does NOT claim falsification of any specific holographic-duality framework (AdS/CFT, dS/CFT). The framework asserts the principle is recoverable in AVE, not that competing formulations are excluded.

> **Leaf references:** [holographic-paradox](./appendices/app-b-paradoxes/holographic-paradox.md).

### Quality
- confidence: 0.3
- depends-on:
  - INVARIANT-S2 / Axiom 1 (1D inductive flux tubes with 2D cross-sectional porosity $\Phi_A\equiv\alpha^2$)
- solidity: 0.30 (do not build on, rework needed) [= min(0.30, 1.00)]
- rationale: A qualitative stress-test resolution: the $R^2$ entropy scaling is asserted to be recovered because information traverses 1D flux tubes whose bandwidth is bounded by 2D cross-sectional porosity, projected via Nyquist-Shannon onto the causal-horizon surface. No calculation of $S_{BH}=A/(4\ell_P^2)$ ab initio; the porosity-to-area argument is presented as a geometric mechanism, not a derivation. Asserted mechanism.
- strengthen-by:
  - Compute the Bekenstein-Hawking entropy coefficient $1/4$ from the flux-tube channel-capacity argument.
  - Show the $R^3\to R^2$ projection is forced, not merely consistent.

---

## Topological Mass Definition: Faddeev-Skyrme Functional and Hopf Charge
<!-- id: clm-oygz1i -->

- $E[\vec{n}] = \int [\tfrac{1}{2}(\partial_\mu \vec{n})^2 + \tfrac{1}{4e^2}(\partial_\mu \vec{n}\times\partial_\nu \vec{n})^2]\,d^3x$; topological index $Q = \tfrac{1}{16\pi^2}\int \epsilon_{ijk}\,\vec{n}\cdot(\partial_i\vec{n}\times\partial_j\vec{n})\,d^3x$.
- _Specific Claims_
  - Stable particles in the continuous non-linear substrate are defined as finite-energy soliton solutions of the Faddeev-Skyrme energy functional. The first (kinematic) term is the standard gradient energy; the second (Skyrme) term, scaled by the dielectric yield bound $e$, repels the strands and prevents collapse to a singularity (Derrick-type stabiliser).
  - The Hopf charge / Gauss linking number $Q$ is a conserved topological integer; conservation laws (baryon number, lepton number) are derived as topological invariants rather than imposed quantum numbers.
- _Specific Non-Claims and Caveats_
  - The Faddeev-Skyrme functional with the $1/e^2$ Skyrme term is a **chosen ansatz** for a stable soliton model — it is the standard form in the topological-soliton literature, here adopted as the AVE continuum field theory. The leaf does not derive the Skyrme term independently from Axioms 1–4.
  - "All conservation laws derived from $Q$" is asserted at the formula level (any continuous deformation preserves $Q$). The mapping from $Q$-sectors to specific Standard Model quantum numbers (baryon number, lepton number) is the structural identification used downstream — see `clm-mnb3lt`, `clm-67jn9o`, and `clm-q5izb7` for the load-bearing applications.

> **Leaf references:** [mathematical-topology-of-mass](./particle-physics/ch01-topological-matter/mathematical-topology-of-mass.md).

### Quality
- confidence: 0.6
- depends-on:
  - INVARIANT-S2 / Axiom 1 (continuous non-linear substrate hosting finite-energy solitons)
  - INVARIANT-S2 / Axiom 4 (dielectric yield bound $e$ scaling the Skyrme term)
- solidity: 0.60 (use as input only, don't build deeper) [= min(0.60, 1.00)]
- rationale: The Faddeev-Skyrme energy functional and the Hopf-charge/Gauss-linking integral are stated as standard, correct topological-soliton forms. But the leaf adopts them as an ansatz (the $1/e^2$ Skyrme stabilizer is the standard literature form, not derived from Axioms 1–4), and the mapping from $Q$-sectors to specific SM quantum numbers (baryon/lepton number) is asserted at the formula level. Correct standard forms adopted as ansatz rather than derived.
- strengthen-by:
  - Derive the quartic Skyrme term (and its $1/e^2$ scaling) from the Axiom 4 dielectric saturation dynamics.
  - Make the $Q$-sector $\to$ baryon/lepton-number identification explicit and forced rather than asserted.

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

> **Leaf references:** [dark-wake-bemf-foc-synthesis](../common/dark-wake-bemf-foc-synthesis.md), [newtonian-inertia-as-lenz](./particle-physics/ch01-topological-matter/newtonian-inertia-as-lenz.md).

### Quality
- confidence: 0.3
- depends-on:
  - INVARIANT-S2 / Axiom 1 (distributed vacuum inductance $\mu_0$; closed flux loop)
  - INVARIANT-S2 / Axiom 2 (topo-kinematic isomorphism $[L]\equiv[M]$)
- solidity: 0.30 (do not build on, rework needed) [= min(0.30, 1.00)]
- rationale: An ontological reinterpretation asserted at the formula level: $E_{mass}=\frac12 L_{eff}|\mathbf{A}|^2$ is stated and $F=ma$ is "derived as the macroscopic phenomenological consequence" of Lenz's law, but no actual $F=ma$ derivation is carried out — the back-EMF$\to$inertia mapping is claimed, not shown. Macroscopic dynamics are unchanged. Claimed mechanism without closed derivation.
- strengthen-by:
  - Carry out the explicit derivation of $F=ma$ (or $p=mv$) from the back-EMF on the closed loop, showing $m=L_{eff}$ quantitatively.
  - Extend to relativistic mass $E=\gamma m_0c^2$ from $L_{eff}=L_0/\sqrt{1-v^2/c^2}$ within this leaf.

---

## Regime Classification of Topological Matter
<!-- id: clm-ou2jym -->

- _Specific Claims_
  - Every stable particle (photon, neutrino, electron, proton, $W$/$Z$, black hole) operates within a definite regime of the Axiom 4 saturation kernel: Regime I (Linear, $\Delta\phi \ll \alpha$), Regime II (Yield, $\Delta\phi = \alpha$), or Regime III (Rupture, $\Delta\phi > \alpha$). The regime placement determines the particle's qualitative dynamical character: free propagation (photon, Regime I), self-confinement (electron, Regime II), Borromean linkage at saturation (proton, Regime II), transient defect (W/Z, Regime III), metric collapse (black hole, Regime III).
  - The neutrino sits at the I–II boundary (chiral phase below yield), making its lattice-coupling qualitatively distinct from massive bound topological defects.
- _Specific Non-Claims and Caveats_
  - The regime table is a structural taxonomy, not a quantitative prediction. The numerical mass, charge, and lifetime values for each entry are derived in their respective per-particle entries (e.g., proton in `clm-mnb3lt`, electron in `clm-h9aqmt`, W/Z in `clm-q8un7j`). This entry indexes which regime each particle inhabits and asserts regime-character claims; it does not duplicate the per-particle quantitative results.
  - "Black hole as macroscopic soliton in Regime III" is the vol2 framing of the gravitational-saturation result developed in vol3. Treat the black-hole row as a forward reference into vol3, not a self-contained vol2 derivation.

> **Leaf references:** [regime-classification](./particle-physics/ch01-topological-matter/regime-classification.md).

### Quality
- confidence: 0.3
- depends-on:
  - INVARIANT-S2 / Axiom 4 (saturation-kernel regimes I/II/III; $\Delta\phi$ vs $\alpha$)
- solidity: 0.30 (do not build on, rework needed) [= min(0.30, 1.00)]
- rationale: A structural taxonomy table asserting each particle's regime placement (photon I, electron/proton II, W/Z and black hole III, neutrino at the I–II boundary). It is a manifestation of the Axiom 4 regime structure applied to known particles, not a derivation — the per-particle quantitative values live in their own entries. The regime assignments are asserted/qualitative. Asserted taxonomy.
- strengthen-by:
  - For each row, compute the regime parameter $\Delta\phi/\alpha$ from the particle's own derived quantities to substantiate the placement.
  - Justify the neutrino's I–II boundary placement quantitatively rather than by qualitative "chiral phase below yield."

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

> **Leaf references:** [chirality-and-antimatter](./particle-physics/ch01-topological-matter/chirality-and-antimatter.md).

### Quality
- confidence: 0.3
- depends-on:
  - INVARIANT-S2 / Axiom 1 (chiral lattice; twist direction as charge polarity)
  - clm-h9aqmt (unknot identity; $e^\pm$ as opposite-handed unknots)
- solidity: 0.30 (do not build on, rework needed) [= min(0.30, 0.70)]
- rationale: A mechanism-claim reinterpretation of pair annihilation. The energy balance $2m_ec^2=1.022$ MeV is a trivial identity given $m_e$; the load-bearing content (Mazur-square-knot paradox resolved by optical phase cancellation $\boldsymbol\omega+(-\boldsymbol\omega)=0$ severing the topological boundary) is asserted, and the leaf does not show the cancellation is a continuous lattice evolution (an open formalization question the entry acknowledges). The observable $2\gamma$ at 511 keV is the standard QED result. Asserted mechanism.
- strengthen-by:
  - Demonstrate (or formalize) that the phase-cancellation event is a continuous lattice evolution rather than a singular boundary discontinuity.
  - Extend beyond the two-photon channel to recover the relative $3\gamma$ rate or other channels.

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

> **Leaf references:** [proton-neutron-mass-split](./particle-physics/ch02-baryon-sector/proton-neutron-mass-split.md).

### Quality
- confidence: 0.4
- depends-on:
  - INVARIANT-S2 / Axiom 1 (flux-tube minimum thickness $\ell_{node}$; $K_4$ tetrahedral Borromean braid)
  - INVARIANT-S2 / Axiom 3 (Machian closure expression for $G=c^4\ell_{node}/(7\xi m_ec^2)$)
  - clm-mnb3lt (proton mass / $m_p/m_e$ in the mass-stiffening factor)
- solidity: 0.40 (do not build on, rework needed) [= min(0.40, 0.63)]
- rationale: The He-4 strain consistency check ($\Delta x=E_{bond}/T_{nuc}\approx1.93$ fm, $\approx0.50\%$ strain) is a clean calculation, but it uses the asserted scaling $T_{nuc}=T_{EM}(m_p/m_e)$ (the leaf calls this "a key observation in the computational audit," not a closed derivation) and the empirical 28.3 MeV binding energy as input. The Hierarchy Bridge is explicitly algebraic substitution of two framework choices ($G$ via Axiom 3, $T_{nuc}$ via the assertion), disclosed as not an independent $G$ derivation; neutron decay is structural with no $\tau_n$ derived. Asserted-with-consistency-checks.
- strengthen-by:
  - Derive $T_{nuc}=T_{EM}(m_p/m_e)$ (rule out nearby functional forms) rather than asserting the mass-stiffening scaling.
  - Predict the He-4 binding energy from the topology instead of taking 28.3 MeV as input.

---

## U(1) and SU(3) Gauge Group Emergence from Lattice Topology
<!-- id: clm-jkpfd4 -->

- U(1): $S_{lattice} = \sum_P (1 - \cos\Phi_P) \to \int \tfrac{1}{4} F_{\mu\nu}F^{\mu\nu}\,d^4x$ in the $\ell_{node}\to 0$ limit. SU(3): $S_3$ permutation symmetry of three indistinguishable Borromean flux loops $\to$ Weyl group of SU(3); $\mathbb{Z}_3$ centre enforces colour-singlet confinement.
- _Specific Claims_
  - **U(1) electromagnetism.** Constructing the standard Wilson lattice action from unitary link variables $U_{ij} = e^{i\theta_{ij}}$ over triangular plaquettes recovers $-\tfrac{1}{4}F_{\mu\nu}F^{\mu\nu}$ in the continuum limit. AVE's contribution is the *physical* identification of the lattice as the substrate (rather than a numerical regularisation): U(1) is reinterpreted as enforcement of unitary topological continuity across a discrete physical substrate graph.
  - **SU(3) colour charge.** The three indistinguishable interlocked flux loops of the proton ($6^3_2$ Borromean) are governed by the symmetric group $S_3$. Since $S_3$ is the Weyl group of SU(3), the smallest continuous Lie group whose discrete quotient contains $S_3$ as its Weyl is SU(3). The fundamental flux loops transform in the **3** of SU(3); the $\mathbb{Z}_3$ centre enforces topological confinement (only colour-singlet composites propagate as free particles).
- _Specific Non-Claims and Caveats_
  - The Wilson-action argument is **standard lattice-gauge-theory mathematics**; AVE's claim is the physical interpretation that the lattice is a real substrate lattice, not a computational regulator. The Wilson construction itself is not original to AVE.
  - "Smallest continuous Lie group whose discrete quotient contains $S_3$ as a Weyl-subgroup is SU(3)" is asserted as the structural identification. The leaf does not enumerate alternative continuous embeddings (e.g., higher-rank groups whose Weyl groups also contain $S_3$) or formally rule them out via additional topological constraints. The identification with SU(3) is supported by the three-loop fundamental-representation count and $\mathbb{Z}_3$ centre / confinement match, but is not a uniqueness theorem.
  - Does NOT claim a derivation of the QCD running coupling $\alpha_s(\mu)$ or the gluon spectrum from this leaf. The "colour quantum number = which loop carries the dominant phase winding" is an ontological identification, not a calculational replacement for QCD perturbation theory.
  - The chapter's title "Forward to Ch.6" indicates the gauge-emergence content is positioned as a bridge into the electroweak chapter; downstream quantitative results (Weinberg angle, $W$/$Z$ masses) are indexed under their own entries (`clm-5zuo7g`, `clm-q8un7j`).

> **Leaf references:** [forward-to-ch6](./particle-physics/ch05-electroweak-mechanics/forward-to-ch6.md).

### Quality
- confidence: 0.55
- depends-on:
  - INVARIANT-S2 / Axiom 1 (lattice plaquette / Wilson link variables; $S_3$ symmetry of the three Borromean loops)
  - clm-67jn9o (Borromean $\mathbb{Z}_3$ / quark structure underpinning the SU(3) identification)
- solidity: 0.55 (use as input only, don't build deeper) [= min(0.55, 0.75)]
- rationale: The U(1) half is clean, standard lattice-gauge math: the Wilson plaquette action $\sum_P(1-\cos\Phi_P)\to\int\frac14 F_{\mu\nu}F^{\mu\nu}$ in the continuum limit (correct, and disclosed as not original to AVE — AVE adds the physical-substrate interpretation). The SU(3) half rests on the asserted "smallest continuous Lie group whose Weyl group contains $S_3$ is SU(3)" — supported by the three-loop fundamental-rep count and $\mathbb{Z}_3$-centre confinement, but explicitly not a uniqueness theorem (alternative embeddings not ruled out). Half clean-standard, half asserted structural identification.
- strengthen-by:
  - Rule out higher-rank Lie groups whose Weyl groups also contain $S_3$, converting the SU(3) identification into a uniqueness result.
  - Derive the QCD running coupling $\alpha_s(\mu)$ from the lattice to go beyond the structural symmetry match.

---

## Schrödinger Equation as Helmholtz Acoustic Cavity (Deterministic Reinterpretation)
<!-- id: clm-qde5gn -->

- $-\tfrac{\hbar^2}{2m}\nabla^2\Psi + V(r)\Psi = E\Psi \;\Longleftrightarrow\; \nabla^2\Psi + k^2(r)\Psi = 0$ with $k^2(r) = (2m/\hbar^2)(E - V(r))$; $a_0 = \ell_{node}/\alpha = 137\,\ell_{node}$.
- _Specific Claims_
  - The time-independent Schrödinger equation is algebraically identical to the Helmholtz acoustic-cavity equation with a spatially varying sound speed $c_{eff}(r) = \omega/k(r)$. Under AVE, $\Psi$ is reinterpreted as the spatial amplitude of the LC pressure field rather than a probability amplitude. Classically forbidden regions ($E < V(r)$) correspond to imaginary acoustic impedance and evanescent decay; orbital boundaries are physical impedance discontinuities.
  - The Bohr radius is recovered as $a_0 = \ell_{node}/\alpha = \hbar/(m_e c\,\alpha) = 137\,\ell_{node}$ — the cavity size at which the de Broglie standing-wave condition $2\pi r = n\lambda$ is satisfied for the LC phase-locking of the unknot's inductive angular momentum against the proton's static impedance gradient.
  - Hydrogen energy levels $E_n = -m_e c^2 \alpha^2/(2n^2)$ are recovered exactly (sub-1 ppm vs CODATA), with the formula carrying the ontological reinterpretation rather than numerical novelty.
  - The matter-wave / acoustic-cavity distinction is sharp: the electron interacts with the vacuum's **bulk modulus** (longitudinal acoustic), not its shear modulus (transverse EM). Atomic orbitals are bulk-modulus acoustic resonances of the LC mesh.
  - Falsification proposal: a topological-matter-interferometry (Mach-Zehnder electron interferometer) parallax test predicts a deterministic differential phase shift $\Delta\Phi$ from the local gravitational impedance gradient ($n_s = 1 + (9/7)\varepsilon_{11}$, $n_t = 1 + (2/7)\varepsilon_{11}$).
- _Specific Non-Claims and Caveats_
  - This is a **category (i) ontological reinterpretation**. At the formula level, AVE recovers the standard Bohr/Schrödinger spectrum exactly; observable predictions for hydrogen are unchanged. The novelty is the bulk-modulus acoustic-cavity ontology, not new numerics.
  - The "falsification" of standard QM via the parallax test depends on the AVE-specific spatial/temporal index ratios $n_s, n_t$; whether such an asymmetry survives careful Lorentz-invariance analysis at experimentally accessible baselines is an open theoretical and experimental question. Treat the parallax test as a **proposed** falsification, not a current experimental result.
  - Does NOT claim multi-electron Schrödinger / Hartree-Fock / DFT is replaced by the acoustic-cavity picture at the level of every observable. The atomic ionization energy entry (`clm-oltvwy`) is the load-bearing quantitative claim for multi-electron atoms; this entry is the single-electron ontology + Bohr-radius identity.
  - Does NOT claim derivation of relativistic Dirac corrections, fine structure, or hyperfine structure from this leaf. The non-relativistic limit is the explicit scope.
  - Angular momentum quantisation $L = \hbar\sqrt{l(l+1)}$ and magnetic-quantum-number-as-nodal-planes recovery is **standard spherical-harmonic mode counting** for any spherical resonator — AVE adds the ontological identification ("orbitals are not probability densities; they are LC pressure-mode geometries"), not a different quantisation rule.

> **Leaf references:** [de-broglie-standing-wave](./quantum-orbitals/ch07-quantum-mechanics/de-broglie-standing-wave.md).

### Quality
- confidence: 0.8
- depends-on:
  - INVARIANT-S2 / Axiom 1 (LC pressure field; standing-wave $2\pi r=n\lambda$; $a_0=\ell_{node}/\alpha$)
  - INVARIANT-S2 / Axiom 2 (Coulomb impedance gradient $V(r)$)
  - INVARIANT-S2 / Axiom 4 (soliton dispersion $\to k(r)$)
  - clm-h9aqmt (unknot Compton-wavelength $\ell_{node}$ baseline)
- solidity: 0.70 (ok to build on, see caveats) [= min(0.80, 0.70)]
- rationale: The core equations are clean: the Schrödinger$\leftrightarrow$Helmholtz rearrangement is exact algebra, and the Bohr radius $a_0=\ell_{node}/\alpha$ and hydrogen spectrum $E_n=-m_ec^2\alpha^2/(2n^2)$ are recovered exactly (the leaf states they are algebraically identical to Bohr, sub-1 ppm vs CODATA). Classification is largely a consistency check / identity-rearrangement carrying an ontological reinterpretation; the one novel piece (the $n_s,n_t$ differential-phase parallax falsifier) is explicitly *proposed*, with Lorentz-invariance survival an open question. Clean local derivation, modest novel content.
- strengthen-by:
  - Carry the parallax $\Delta\Phi$ prediction through a Lorentz-invariance analysis to establish whether the $n_s\neq n_t$ asymmetry survives at accessible baselines.
  - Derive (not assert) that $\Psi$ is the bulk-modulus (longitudinal acoustic) amplitude, distinguishing it observably from the standard probability amplitude.

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

> **Leaf references:** [quantitative-resolutions](./nuclear-field/ch10-open-problems/quantitative-resolutions.md), [scale-invariance-table](./nuclear-field/ch10-open-problems/scale-invariance-table.md), [unification](./nuclear-field/ch10-open-problems/unification.md).

### Quality
- confidence: 0.4
- depends-on:
  - $\nu_{vac}=2/7$ (master integer-ratio input)
  - INVARIANT-S2 / Axiom 1 (torus-knot crossing numbers $c_1,c_2,c_3$)
  - clm-gfs4j8 ($\theta_{QCD}\equiv0$ structural elimination)
  - clm-5zuo7g ($\sin^2\theta_W=2/9$ row)
  - clm-7o8clt (PMNS rows)
  - clm-4vwsjc ($g_*=7^3/4$ row)
- solidity: 0.40 (do not build on, rework needed) [= min(0.40, 0.40)]
- rationale: A headline aggregation: "26 of 26 SM parameters, max residual $<4.1\%$" assembled from per-chapter results that live in (and are scored under) their own entries. As an aggregation it is a structural-unification claim about a common derivation principle (lattice scale invariance + integer ratios), not a single computed result; the leaf does not provide a complete CKM derivation (Wolfenstein parameters not fitted to PMNS accuracy), and $\alpha_s=\alpha^{3/7}$ is an AVE-native-scheme identification with no running-coupling. Per-parameter accuracy spans $0.09\%$ to $\sim4\%$. Aggregation with several asserted/scheme-specific rows.
- strengthen-by:
  - Provide the full CKM matrix derivation (all four Wolfenstein parameters) at the same rigor as the PMNS matrix.
  - Tabulate which of the 26 are derived predictions vs consistency checks vs identities, so the "26 of 26" headline is not read uniformly.

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

> **Leaf references:** [birch-swinnerton-dyer](./nuclear-field/ch12-millennium-prizes/birch-swinnerton-dyer.md), [hodge-conjecture](./nuclear-field/ch12-millennium-prizes/hodge-conjecture.md), [p-vs-np](./nuclear-field/ch12-millennium-prizes/p-vs-np.md), [poincare-conjecture](./nuclear-field/ch12-millennium-prizes/poincare-conjecture.md), [riemann-hypothesis](./nuclear-field/ch12-millennium-prizes/riemann-hypothesis.md).

### Quality
- confidence: 0.4
- depends-on:
  - INVARIANT-S2 / Axiom 1 (lattice spectral structure; $(2,q)$ torus-knot quantization; impedance relaxation)
  - INVARIANT-S2 / Axiom 4 (energy-density boundedness used in the Riemann below-cutoff argument)
  - clm-q5izb7 (mass-gap barrier reused in several reinterpretations)
- solidity: 0.40 (do not build on, rework needed) [= min(0.40, 0.60)]
- rationale: Five framework-conditional reinterpretations, each explicitly NOT Clay-rigorous (Poincaré is interpretive-only, Perelman's proof being canonical; P-vs-NP is "rendered moot," an explicit non-resolution). They are structural physical interpretations (rank$\leftrightarrow$mutual-inductance, $\zeta$-zeros$\leftrightarrow$spectral-cutoff, Hodge-classes$\leftrightarrow$standing-waves), not algorithmic or ZFC-level derivations; e.g. BSD computes no specific curve's rank, Riemann's below-cutoff step is physical not a zero-free-strip proof. A routing index over five distinct arguments. Asserted/interpretive.
- strengthen-by:
  - For at least one problem (e.g. BSD), demonstrate the physical identification computes a known answer for a specific instance.
  - Sharpen each reinterpretation's scope caveat at the individual-leaf level so the consolidated index is not read as five proofs.

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

> **Leaf references:** [computational-graph](./proofs-computation/ch09-computational-proof/computational-graph.md).

### Quality
- confidence: 0.4
- depends-on:
  - INVARIANT-S2 / Axiom 4 (single saturation kernel $S(x,x_{yield})=\sqrt{1-(x/x_{yield})^2}$ across 39 OOM)
  - INVARIANT-N3 (shared impedance-operator chain)
  - clm-dboxok (operator chain on nuclear + protein)
  - clm-d9ivj1 (regime-boundary eigenvalue method shared across the domain modules)
- solidity: 0.40 (do not build on, rework needed) [= min(0.40, 0.55)]
- rationale: This leaf is an aggregation/routing table: 13 domain rows whose canonical derivations and caveats live in other vol2/3/4/5 chapters. The verifiable load-bearing fact is the *software* identity — one `scale_invariant.py` imported by 13 modules, test-checked to give identical results across scales — but the per-row physical predictions (5%–10% to "exact" regime checks) are not derived here, and "exact" rows are regime/identity checks, not sub-percent waveform matches. As a derivation the leaf asserts agreement and points elsewhere. Aggregation index.
- strengthen-by:
  - Replace the summary table with per-row links to the canonical derivation + its own confidence, so the headline cannot be read as uniform sub-percent.
  - Distinguish "exact" regime/identity rows from quantitative matches explicitly in the table.

---

## Peierls-Nabarro Friction Paradox: STZ / Dielectric Saturation-Plastic Resolution
<!-- id: clm-ghs75o -->

- _Specific Claims_
  - The Peierls-Nabarro objection (a charged particle traversing a discrete vacuum grid would stutter and radiate away its kinetic energy via Bremsstrahlung) is resolved by reinterpreting the vacuum substrate as an **amorphous Dielectric Saturation-Plastic Network**, not a cold rigid periodic crystal. The translating electron's leading-edge shear stress dynamically exceeds the dielectric saturation threshold ($\tau_{local} > \tau_{yield}$), initiating a localised **Shear Transformation Zone (STZ)**: the particle generates its own continuous frictionless zero-impedance phase slipstream. The lattice thixotropically re-freezes behind it, permitting smooth kinematic translation and forbidding unprovoked Bremsstrahlung radiation.
- _Specific Non-Claims and Caveats_
  - This is a **stress-test resolution** (App B paradox), demonstrating internal consistency of the lattice picture against an established condensed-matter constraint. It is not an independent prediction of a new observable.
  - The STZ mechanism is asserted at the qualitative level (dielectric-saturation-plastic flow on the leading edge); the leaf does not produce a quantitative threshold for the onset velocity or a coupling constant for the slipstream dynamics. Treat as a mechanism claim, not a numerical prediction.
  - Does NOT claim falsification of the standard PN-stress framework in real crystallographic dislocations; the framework's claim is that the AVE vacuum's plastic regime preempts the rigid-PN-barrier picture for fundamental charged particles, not that real-material PN dynamics is wrong.

> **Leaf references:** [peierls-nabarro-paradox](./appendices/app-b-paradoxes/peierls-nabarro-paradox.md).

### Quality
- confidence: 0.3
- depends-on:
  - INVARIANT-S2 / Axiom 1 (amorphous dielectric-saturation-plastic network, not a rigid periodic crystal)
  - INVARIANT-S2 / Axiom 4 (local yield $\tau_{local}>\tau_{yield}$ initiating the STZ slipstream)
- solidity: 0.30 (do not build on, rework needed) [= min(0.30, 1.00)]
- rationale: A qualitative stress-test resolution: the PN-stuttering/Bremsstrahlung objection is dissolved by reinterpreting the substrate as an amorphous saturation-plastic network where the leading edge liquefies into a frictionless Shear Transformation Zone. The STZ slipstream mechanism is asserted at the qualitative level — no onset-velocity threshold and no slipstream coupling constant are produced (the entry acknowledges this). Asserted mechanism.
- strengthen-by:
  - Derive a quantitative onset velocity / shear threshold for STZ formation from Axiom 4.
  - Show (quantitatively) that the re-freezing rate suppresses Bremsstrahlung below an observable bound.

---

## App C Exact Analytical Derivation Catalog
<!-- id: clm-e1pdfd -->

- _Specific Claims_
  - The App C index is a consolidated catalog of vol2's exact closed-form bounds and identities derived from first-principles continuum elastodynamics, thermodynamic boundary conditions, and finite-element graph limits with **zero arbitrary phenomenological parameters**. Sections: Hardware Substrate ($\ell_{node}$, $\xi_{topo}$, $V_0$, $p_c$, $\rho_{bulk}$, $\nu_{vac}$, $\tau_{yield}$); Signal Dynamics and Topological Matter (Continuous Action Lagrangian, Topological Mass Functional, Faddeev-Skyrme cold/effective coupling, Thermal Lattice Softening, Proton Rest Mass eigenvalue with conditional Gaussian-ansatz caveat, Macroscopic Strong Force, Witten Effect, Weinberg angle); Cosmological Dynamics (Trace-Reversed Gravity, $H_\infty$, $R_H$, $t_H$, Phantom Dark Energy, MOND floor, Symplectic Raymarching).
- _Specific Non-Claims and Caveats_
  - **App C is a derivation summary, not the source of any claim.** Every individual equation in the catalog is the load-bearing content of another vol2 entry: proton mass (`clm-mnb3lt`), Weinberg angle (`clm-5zuo7g`), W/Z masses (`clm-q8un7j`), Witten-effect quark charges (`clm-67jn9o`), $H_\infty$ Hubble framing (`clm-mroghg`), universal energy functional (`clm-dboxok`), etc. Citing this catalog without consulting the per-result entry's caveats inherits the catalog's brevity rather than the derivation's actual conditions.
  - The catalog explicitly carries forward the proton-mass Gaussian-ansatz caveat ("conditional on Gaussian flux-tube ansatz" for $\rho_{threshold} = 1.1062$) and the rigour-gap pointer to `mathematical-closure.md` — the same caveat documented in `clm-mnb3lt`.
  - Does NOT introduce any new derivation not already in a per-result entry; this entry exists so that consumers searching the catalog can find the canonical source.

> **Leaf references:** [index](./appendices/app-c-derivations/index.md).

### Quality
- confidence: 0.5
- depends-on:
  - clm-mnb3lt (proton mass eigenvalue, with Gaussian-ansatz caveat carried forward)
  - clm-5zuo7g (Weinberg angle)
  - clm-q8un7j (W/Z masses)
  - clm-67jn9o (Witten-effect quark charges)
  - clm-mroghg (Hubble framing)
  - clm-dboxok (universal energy functional)
  - clm-oygz1i (topological mass functional)
- solidity: 0.50 (use as input only, don't build deeper) [= min(0.50, 0.55)]
- rationale: Explicitly a derivation-summary catalog that introduces no new derivation — every equation is the load-bearing content of another vol2 entry, and the catalog faithfully carries forward those entries' caveats verbatim (including the proton-mass Gaussian-ansatz "conditional" flag and the `mathematical-closure.md` rigour-gap pointer). Its local rigor is the rigor of a faithful, caveat-preserving aggregation, not of an independent derivation. Pinned mid-band as a non-source summary.
- strengthen-by:
  - Add per-entry confidence annotations so a consumer reading the catalog sees each result's actual band, not just the headline list.
  - Keep the caveat-preservation under CI so the catalog cannot drift from its per-result entries.

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

> **Leaf references:** [graph-architecture](./appendices/app-d-computational-graph/graph-architecture.md).

### Quality
- confidence: 0.5
- depends-on:
  - INVARIANT-S2 / Axiom 1 (Poisson-disk hard-sphere genesis; $K=2G$ trace-reversed micropolar state)
  - clm-9s9apq (analytic QED packing fraction $p_c\approx0.1834$ the genesis targets; vol1)
- solidity: 0.50 (use as input only, don't build deeper) [= min(0.50, 0.63)]
- rationale: An engine-specification leaf. The Poisson-disk genesis $\to p_c\approx0.17$–$0.18$ is presented as a simulation/analytical *agreement* (the simulation reproduces the analytic $p_c$ given the right exclusion radius — not a derivation of $p_c$ from genesis dynamics). The $C_{ratio}=(p_{cauchy}/p_c)^{1/3}\approx1.187$ over-bracing relation is clean algebra but uses the simulation-reported $p_{cauchy}\approx0.3068$, and the $k_{couple}$ thresholds are simulation-reported, not analytically derived. Engine spec with computationally-supported, partly-asserted constants.
- strengthen-by:
  - Derive the $k_{couple}$ Cauchy$\to$trace-reversed transition thresholds analytically rather than reading them off simulation.
  - Show the Poisson-disk packing fraction follows from genesis dynamics, not just that it can be tuned to match $p_c$.

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

> **Leaf references:** [dcve-specification](./appendices/app-e-dcve/dcve-specification.md).

### Quality
- confidence: 0.5
- depends-on:
  - INVARIANT-S2 / Axiom 1 (micropolar $K=2G$ continuum; lattice pitch $a\equiv\ell_{node}$)
  - INVARIANT-S2 / Axiom 4 (Nyquist band-limit; saturation cap)
  - clm-mnb3lt ($\kappa_{FS}=8\pi$ tying the Vakulenko-Kapitanski constant)
- solidity: 0.50 (use as input only, don't build deeper) [= min(0.50, 0.63)]
- rationale: Engine-specification leaf mixing clean algebraic identities with imported/asserted choices. Solid pieces: the exact discrete commutator $[\hat x,\hat p_{discrete}]=i\hbar\sqrt{1-(ap/\hbar)^2}$ (correct finite-difference algebra), the flux-basis dimensional-exactness argument, and the standard micropolar constitutive law. Asserted/imported pieces: the Vakulenko-Kapitanski bound $M_{rest}\ge C_{VK}|Q_H|^{3/4}$ with $C_{VK}$ tied to $\kappa_{FS}$ (adopted, not independently derived) and the AQUAL $a_0=cH_\infty/(2\pi)$ identification. Engineering discipline, partly identity-grounded.
- strengthen-by:
  - Derive $C_{VK}$ from substrate primitives independent of the proton-mass calibration.
  - Show the discrete commutator is the physically correct sub-lattice QM commutator (vs merely an engine-stable one) against a standard-QM benchmark.

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

> **Leaf references:** [cross-scale-isomorphism-table](./appendices/app-f-solver-toolchain/cross-scale-isomorphism-table.md), [derived-numerology](./appendices/app-f-solver-toolchain/derived-numerology.md), [kerr-q-correction](./appendices/app-f-solver-toolchain/kerr-q-correction.md), [knot-mode-isomorphism](./appendices/app-f-solver-toolchain/knot-mode-isomorphism.md), [lattice-phase-transition](./appendices/app-f-solver-toolchain/lattice-phase-transition.md), [nuclear-eigenvalue](./appendices/app-f-solver-toolchain/nuclear-eigenvalue.md), [protein-eigenvalue](./appendices/app-f-solver-toolchain/protein-eigenvalue.md), [regime-eigenvalue-method](./appendices/app-f-solver-toolchain/regime-eigenvalue-method.md), [semiconductor-junction-analogy](./appendices/app-f-solver-toolchain/semiconductor-junction-analogy.md).

### Quality
- confidence: 0.7
- depends-on:
  - INVARIANT-S2 / Axiom 4 (saturation boundary $\varepsilon_{11}=1$; lattice phase transition $G\to0$)
  - $\nu_{vac}=2/7$ (Poisson correction $r_{eff}=r_{sat}/(1+\nu_{vac})$)
  - clm-mnb3lt (proton/pion eigenvalue uses $\mathcal{I}_{baryon}\approx1836$ from proton mass)
- solidity: 0.63 (use as input only, don't build deeper) [= min(0.70, 0.63)]
- rationale: The universal closed form $\omega\cdot r_{char}=\ell(1+\nu_{vac})/x_{sat}$ produces the Schwarzschild QNM $18/49=0.367$ vs GR $0.3737$ (1.7%) via a clean 5-step chain — a consistency check reproducing the GR ringdown through an alternative (saturation-boundary) value problem. The disclosed imports are the factor-7 Machian boundary and the asserted $Q=\ell$ (the leaf states $Q=\ell$ is consistent with observed quality factors but not shown to be the unique resolution); per-domain errors range $0.1\%$ to $\sim40\%$ (extremal Kerr). Disclosed methodology bound.
- strengthen-by:
  - Derive $Q=\ell$ as the unique consequence of the perfect-reflector saturation boundary rather than a consistent identification.
  - Extend the Kerr correction to recover the extremal-$a_*$ regime (currently $\sim40\%$ at $a_*=0.99$).

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

> **Leaf references:** [universal-constants-exchange](./appendices/app-f-solver-toolchain/universal-constants-exchange.md).

### Quality
- confidence: 0.3
- depends-on:
  - INVARIANT-C2 ($\xi_{topo}=e/\ell_{node}$ length$\leftrightarrow$charge exchange rate)
  - INVARIANT-S2 / Axiom 1 (lattice pitch $\ell_{node}$ as the reference geometric scale)
- solidity: 0.30 (do not build on, rework needed) [= min(0.30, 1.00)]
- rationale: An ontological reinterpretation: $c,\hbar,G,\varepsilon_0,e,k_B$ recast as domain-exchange rates. The individual pairings (e.g. $c$: m$\leftrightarrow$s, $\hbar c$: J$\leftrightarrow$m) are valid dimensional conversions — essentially near-identities — but the leaf derives no value and produces no new content; the CODATA values are unchanged and the "zero free parameters" headline rests on the calibration triad ($\ell_{node},\alpha,G$) being accepted as input. Asserted reinterpretation (dimensionally valid, content-light).
- strengthen-by:
  - Derive at least one exchange-rate value from a more primitive principle to move beyond restating dimensional relations.
  - Make explicit which quantities are genuinely eliminated vs which are just relabeled, to substantiate "zero free parameters."
## Electron — Canonical Identification + First-Principles Axiom Audit
<!-- id: clm-uatcql -->

AVE-native canonical identification of the electron as a self-trapped photon — the same K4 transverse-Cosserat-microrotation wave above the dielectric yield amplitude ($V_{yield} = \sqrt{\alpha}\,V_{snap} \approx 43.65$ kV) where Axiom 4 saturation engages and self-creates a $\Gamma = -1$ TIR cavity. Provides a 4-property definition ($0_1$ unknot real-space + $(2,3)$ phase-space Clifford-torus + $\Gamma=-1$ TIR cavity + T₂-microrotation core), a first-principles axiom audit per property, and an 8-framing cross-corpus translation guide with reconciliation matrix.

- _Specific Claims_
  - The electron is the same K4-substrate wave as the photon, above the saturation threshold (not an ontologically distinct particle).
  - Electron real-space topology is the $0_1$ unknot; the $(2,3)$ "trefoil" is the phase-space Clifford-torus winding, not a real-space knot.
  - 8/8 topological-dynamical properties are axiom-derived; **5/8 observables are axiom-derived** (corrected 2026-06-21 from 6/8 — the leading $g = 2$ is POSITED, not derived; see the Rule-12 scope-note in the Caveats).
- _Specific Non-Claims and Caveats_
  - $m_e$ is honestly scoped as a calibration anchor, not an axiom-derived value.
  - g-2 closure is partial, pending K4-Cosserat numerical confirmation.
  - 🔴 **Rule-12 scope-note (2026-06-21, workflow wwpskpweb):** distinguish two separate items the prior wording conflated. (i) The **leading $g = 2$** value is **POSITED** (the imported Dirac value), NOT axiom-derived — the $2\pi$/$4\pi$ double-cover forces **spin-½**, not the $\mu/S$ ratio (proton $g_p \approx 5.586$ / neutron $g_n \approx -3.826$ are also spin-½ with the same double-cover yet $g \neq 2$). (ii) The separate **anomalous** part $a_e = g{-}2$ Petermann coefficient is the partial-closure / $n_q$-additivity item (Q-G27 thread). The "6/8 observables axiom-derived" tally above counted the leading $g = 2$ as derived; the corrected tally is **5/8 axiom-derived** (spin-½ stays derived; leading $g = 2$ → posited) per [`electron-identification.md`](./particle-physics/ch01-topological-matter/electron-identification.md) §2 honest-scoping summary.
  - Flagged corpus citation issue (sm-translation-toolchain.md:22 "longitudinal wave" vs canonical transverse).

> **Leaf references:** [electron-identification](./particle-physics/ch01-topological-matter/electron-identification.md).

### Quality
- confidence: 0.75
- depends-on:
  - INVARIANT-S2 / Axioms 1–4 (per-property axiom audit: K4 lattice, TKI, minimum reflection, saturation)
  - clm-h9aqmt (electron-unknot ropelength / self-energy, framing #2)
- solidity: 0.70 (ok to build on, see caveats) [= min(0.75, 0.70)]
- rationale: A rigorous, self-critical per-property axiom audit: 8/8 topological-dynamical properties and 5/8 observables are traced to axioms (corrected 2026-06-21 from 6/8 — the LEADING g=2 value is POSITED/Dirac, not axiom-derived; the 2π/4π double-cover forces spin-½, not the μ/S ratio, with proton/neutron the decisive counterexample), with $m_e$ honestly scoped as a calibration anchor (not derived), the Compton wavelength as definitional, and the separate ANOMALOUS g−2 Petermann part flagged as partial closure (pending $n_q$-additivity); one Clifford-torus uniqueness sub-item is disclosed and does not affect predictions. The audit is honest and well-grounded with explicit calibration/circularity flagging; it is an identification+audit, not a numerical prediction. Disclosed-bound.
- strengthen-by:
  - Close the g-2 Petermann $n_q$-additivity item via the K4-Cosserat Lagrangian numerical confirmation.
  - Resolve the flagged longitudinal-vs-transverse corpus citation (sm-translation-toolchain.md:22) pending Grant adjudication.

---

## Bracket-Golden-Torus Electron-Unknot Cosserat Seeder
<!-- id: clm-gfdplp -->

A-024 operationalization: the canonical AVE electron-soliton seeder injects a Cosserat $\omega$-field hedgehog on a horn-torus unknot at $R = r = \ell_{\text{node}}/(2\pi)$. Validated by 9 unit tests covering topological preservation, three-layer canonical structure (real-space curve + SU(2) bundle + phase-space $(2,3)$ winding), and Bounding Limit 1 saturation. Establishes the canonical injection protocol for electron-soliton initialization in any engine.

- _Specific Claims_
  - The seeder preserves the $0_1$ unknot topology under finite-time evolution (9/9 unit tests pass).
  - Canonical injection protocol is engine-agnostic (K4-TLM or Master Equation FDTD).
- _Specific Non-Claims and Caveats_
  - Mode III on K4-TLM; Mode I PASS only on Master Equation FDTD, per the two-engine architecture.
  - Operationalizes a seeding/initialization protocol — not an independent empirical confirmation of the electron model.

> **Leaf references:** [electron-unknot-cosserat-seeder](./particle-physics/ch01-topological-matter/electron-unknot-cosserat-seeder.md).

### Quality
- confidence: 0.5
- depends-on:
  - INVARIANT-S2 / Axiom 1 (horn-torus unknot at $R=r=\ell_{node}/(2\pi)$; Bounding Limit 1 saturation)
  - clm-uatcql (canonical electron definition the seeder instantiates)
  - clm-8c3yhs ($(2,3)$ torus-knot uniqueness fixing the electron topology seeded)
- solidity: 0.50 (use as input only, don't build deeper) [= min(0.50, 0.70)]
- rationale: This operationalizes a seeding/initialization protocol, validated by 9/9 unit tests (topology preservation under finite-time evolution, three-layer real-space + SU(2) + $(2,3)$ structure, Bounding Limit 1). It closes cleanly as what it claims — a validated, engine-agnostic injection protocol — but it is an operationalization, not an independent empirical confirmation or a physics derivation; the "results" are test-passes confirming the protocol behaves as designed. Modest local rigor.
- strengthen-by:
  - Add a long-time-evolution stability test (beyond finite-time) confirming the seeded unknot is a true attractor, not a metastable seed.
  - Demonstrate Mode I PASS on K4-TLM (currently Mode III; Mode I PASS only on Master Equation FDTD).

---

## L3 Electron-Soliton Closure Synthesis: $(2,q)$ Particle Family
<!-- id: clm-8zpicx -->

Canonical AVE-native description of the $(2,q)$ stable-particle family ($q$ odd: electron $q=3$, proton $q=5$, $\Delta$ baryon $q=7$) as lemniscate-with-$q$-half-twists threaded through saturated K4 node-pairs. Integrates rest-energy structural derivation, the $m_{\text{Cosserat}} = 2 m_e$ factor from bipartite K4, three-layer chirality structure with $\chi_{(2,3)} = 1.2\alpha$ (AVE-HOPF birefringence prediction), substrate-native Pauli, and a Meissner-asymmetric magnetic-moment generator.

- _Specific Claims_
  - $(2,q)$ family realized as lemniscate-with-$q$-half-twists; $m_{\text{Cosserat}} = 2 m_e$ from bipartite K4.
  - $\chi_{(2,3)} = 1.2\alpha$ three-layer chirality (AVE-HOPF birefringence forward prediction).
  - Empirical state: Mode III canonical across 10 pre-registered tests + structural partial-positive at 100% CCW chirality (Meissner mechanism anchored).
- _Specific Non-Claims and Caveats_
  - Substrate-native Pauli is provisional.
  - $R/r$ ladder remains open across three surviving structural reasons.
  - Corpus electron substrate is elsewhere (sub-$\ell_{\text{node}}$ FDTD or different scale).

> **Leaf references:** [l3-electron-soliton-synthesis](./particle-physics/ch01-topological-matter/l3-electron-soliton-synthesis.md).

### Quality
- confidence: 0.4
- depends-on:
  - INVARIANT-S2 / Axiom 1 (bipartite K4 lobe-count = 2; lemniscate-with-$q$-half-twists)
  - INVARIANT-S2 / Axiom 4 (Meissner-asymmetric saturation collapse)
  - clm-h9aqmt (electron rest-energy / virial baseline)
  - clm-8c3yhs ($(2,3)$ trefoil uniqueness anchoring the $(2,q)$ family)
- solidity: 0.40 (do not build on, rework needed) [= min(0.40, 0.70)]
- rationale: An integrative $(2,q)$-family synthesis with several explicitly-open pieces: the rest-energy virial sum is labeled "structural, not predicted"; substrate-native Pauli is "PROVISIONAL"; the $R/r$ ladder is "open across three surviving structural reasons." The forward $\chi_{(2,3)}=1.2\alpha$ birefringence prediction and $m_{Cosserat}=2m_e$ from bipartite K4 are the more concrete elements; empirical state is "Mode III canonical + one structural partial-positive." Asserted-partial synthesis with disclosed open/provisional items.
- strengthen-by:
  - Resolve the $R/r=\varphi^2$ ladder across the three surviving structural reasons.
  - Promote substrate-native Pauli from provisional to derived (per-node $A^2\le1$ budget made rigorous).

---

## Mass-Closure Theorem: $mc^2 = E_{\text{reactive}}$
<!-- id: clm-ka5zdx -->

Derived theorem (NOT a new axiom) from Axioms 1+2+4 acting together: mass is the reactive energy of a saturation-locked closed-tube standing wave, and vacuum is the absence of closed tubes. Complementary to the Vol 2 Ch 6 Higgs mechanism — closure creates the standing-wave LC tank; $Z_0$ drag is what that closure feels when accelerated.

- _Specific Claims_
  - $mc^2 = E_{\text{reactive}}$: rest mass equals the reactive energy of a saturation-locked closed-tube standing wave.
  - The result is a theorem derivable from Axioms 1, 2, and 4 — no fifth axiom required.
- _Specific Non-Claims and Caveats_
  - Status explicitly: derived theorem, not a fundamental constant or new axiom.

> **Leaf references:** [mass-closure-theorem](./particle-physics/ch01-topological-matter/mass-closure-theorem.md).

### Quality
- confidence: 0.5
- depends-on:
  - INVARIANT-S2 / Axiom 1 (per-node LC reactance)
  - INVARIANT-S2 / Axiom 2 (TKI: winding number = conserved charge stabilizing closure)
  - INVARIANT-S2 / Axiom 3 (minimum-reflection selecting the closed-tube configuration)
  - INVARIANT-S2 / Axiom 4 (saturation boundary $\Gamma\to1$ at $A\to1$)
- solidity: 0.50 (use as input only, don't build deeper) [= min(0.50, 1.00)]
- rationale: A coherent four-step derivation chain assembling $mc^2=E_{reactive}$ from Axioms 1+2+4 (+3): open$\to$massless, saturation-locked reflection, topological closure, reactive energy = rest mass. The mechanism steps are sound, but the load-bearing final identity $E_{reactive}=mc^2$ is reached by *identifying* the closed-loop standing-wave invariant with the rest energy (no quantity computed) — honestly labeled "a statement about what mass IS, not a computational program." Real derivation-chain with the closing step asserted by identification.
- strengthen-by:
  - Compute $E_{reactive}=\frac12 L_{tube}I_{max}^2$ for the unknot and show it equals $m_ec^2$ numerically, closing the identification.
  - Demonstrate the minimum-action (Axiom 3) selection of the closed-tube geometry is unique among competing reflected configurations.

---

## Pair Production as Saturated Flux-Tube Rupture at an A-B Node Pair
<!-- id: clm-ezai5b -->

AVE-native canonical derivation of pair production as rupture of a saturated flux tube around an A-B K4 node pair (NOT Breit–Wheeler), gated by the node's rotational-mode resonance tracking the driving frequency (Duffing-like) until autoresonant lock fires. Fuses four AVE-derived pieces: electron = 2 adjacent saturated K4 nodes carrying $(2,3)$ winding; saturated flux tube = TIR impedance cable; $c_{\text{local}} \to 0$ shatter of linear KE into transverse curl producing two contra-rotating Beltrami vortices; Duffing-softened autoresonant rupture timing.

- _Specific Claims_
  - Pair production is saturated-flux-tube rupture at an A-B node pair, not a Breit–Wheeler virtual-photon process.
  - Three nucleation conditions C1+C2+C3 hold at the node pair; $V_{\text{yield}}$ and $V_{\text{SNAP}}$ are different stages of the same process.
  - No new Lagrangian term, no minimal-coupling leak, no Breit–Wheeler postulate.
- _Specific Non-Claims and Caveats_
  - Mechanism-level derivation; quantitative rate not the subject of this leaf.

> **Leaf references:** [pair-production-axiom-derivation](./particle-physics/ch01-topological-matter/pair-production-axiom-derivation.md).

### Quality
- confidence: 0.4
- depends-on:
  - INVARIANT-S2 / Axiom 1 (electron = 2 adjacent saturated K4 nodes with $(2,3)$ bond)
  - INVARIANT-S2 / Axiom 4 ($\Gamma=-1$ TIR walls at $A^2=1$; $c_{local}\to0$ transverse-curl shatter)
  - clm-h9aqmt (electron unknot / bond geometry)
  - clm-ka5zdx (closure/rupture as the generation mechanism)
- solidity: 0.40 (do not build on, rework needed) [= min(0.40, 0.50)]
- rationale: A mechanism-level derivation fusing four AVE-derived pieces with three nucleation conditions (C1 amplitude + C2 frequency + C3 phase). The pieces are internally consistent with the framework's other leaves, but the core dynamical claim ($c_{local}\to0$ shatters linear KE sideways into two contra-rotating Beltrami vortices, Duffing-autoresonant rupture timing) is a structural assertion, and the quantitative rate is explicitly out of scope. Asserted-partial mechanism.
- strengthen-by:
  - Derive the nucleation rate / threshold field quantitatively from the C1+C2+C3 conditions.
  - Show the $c_{local}\to0$ "shatter into transverse curl" is a continuous lattice evolution producing exactly two $m_ec^2$ vortices.

---

## Q-G18 Schwinger Pair Production: Saturation-Kernel WKB Structural Closure
<!-- id: clm-lj4ok5 -->

The QED Schwinger formula for strong-field vacuum pair production emerges from substrate dynamics via the saturation kernel's WKB action integral $\int_0^1\sqrt{1-A^2}\,dA = \pi/4$, generating QED's $\exp(-\pi E_S/E)$ exponent identically (the same integral with different physical labels), with no fit parameters.

- _Specific Claims_
  - The saturation-kernel WKB action integral reproduces QED's Schwinger exponential suppression structurally and identically.
  - No fit parameters are used.
- _Specific Non-Claims and Caveats_
  - AVE-distinct predictions appear only at the sharp $E = E_S$ lattice cutoff and in autoresonant sub-Schwinger production (PLL frequency tracking).

> **Leaf references:** [q-g18-schwinger-pair-wkb](./particle-physics/ch01-topological-matter/q-g18-schwinger-pair-wkb.md).

### Quality
- confidence: 0.65
- depends-on:
  - INVARIANT-S2 / Axiom 4 (saturation-kernel WKB action $\int_0^1\sqrt{1-A^2}\,dA=\pi/4$)
  - clm-ezai5b (A-B node-pair nucleation as the AVE-native realization of the tunneling event)
- solidity: 0.40 (do not build on, rework needed) [= min(0.65, 0.40)]
- rationale: The structural match is genuine: $\int_0^1\sqrt{1-A^2}\,dA=\pi/4$ is literally the QED instanton action $\int_0^{m_ec}\sqrt{m_e^2c^2-p^2}\,dp$ under the substitution $A=p/(m_ec)$, so the exponent $\exp(-\pi E_S/E)$ matches "by construction." But the AVE-action assembly ($2\cdot2\cdot E_S\cdot\pi/4\cdot1/E$) places the pair-factor and dimensional factors somewhat to-target, the prefactor matching is explicitly pending, and it is a consistency check (reproduces QED's exponent). Clean exponent identity, open prefactor, mild factor-assembly.
- strengthen-by:
  - Complete the prefactor matching to $\sim1\%$ via the bound-state integration the leaf defers.
  - Justify the pair-tunneling factor placement from first principles rather than assembling to the QED exponent.

---

## What the Substrate "Sees" of the Canonical Electron
<!-- id: clm-jupq56 -->

The substrate-perspective operational view of the canonical electron: what each lattice node locally experiences (rather than the field-theorist's view). The lattice sees a localized region of high $A^2$ saturation, a self-formed TIR wall at the loop boundary, a topologically conserved circulation pattern, a B-flux-generating circulating current, a long-range refractive-index tail (gravitational mass), and a coupled K4-Cosserat field structure.

- _Specific Claims_
  - Charge, mass, spin, magnetic moment, gravitational coupling, and Compton wavelength are emergent readings of the substrate's joint state at the canonical electron configuration — not properties added on top.
  - Six substrate-level observables compose into the macroscopic electron observables.
- _Specific Non-Claims and Caveats_
  - Operational/interpretive framing of the canonical electron model; introduces no new derivation beyond it.

> **Leaf references:** [substrate-perspective-electron](./particle-physics/ch01-topological-matter/substrate-perspective-electron.md).

### Quality
- confidence: 0.35
- depends-on:
  - INVARIANT-S2 / Axiom 1 (per-node K4 + Cosserat observables)
  - clm-uatcql (canonical electron this leaf views from the substrate side)
  - clm-8c3yhs ($(2,3)$ torus-knot uniqueness — the K4-phasor Layer 3 in this leaf's substrate view IS the $(2,3)$ phase-space winding on the Clifford torus; derivation lives at `vol2/particle-physics/ch01-topological-matter/torus-knot-uniqueness.md`)
- solidity: 0.35 (do not build on, rework needed) [= min(0.35, 0.70)]
- rationale: An operational/interpretive reframing: what each lattice node locally experiences at the canonical electron configuration (high-$A^2$ region, self-formed TIR wall, topological circulation, B-flux, Op14 refractive tail, K4-Cosserat coupling). The six substrate observables are asserted to compose into the macroscopic electron observables, but the leaf "introduces no new derivation beyond" the electron-identification leaf — it is a perspective, not a derivation. Low local rigor as a standalone derivation.
- strengthen-by:
  - Show explicitly (with the composition map) how the six substrate observables sum to charge/mass/spin/$\mu$/Compton, rather than asserting emergence.
  - Tie each substrate observable to a measurable to make the perspective falsifiable on its own terms.

---

## $(2,3)$ Torus-Knot Uniqueness: Why the Electron Is the Trefoil
<!-- id: clm-8c3yhs -->

Derivation of why the electron's phase-space topology is specifically $(2,3)$. $(2,3)$ is uniquely the smallest non-trivial coprime torus knot, with the lowest crossing number ($c = 3$) of any non-trivial knot; coprimality is required for a connected single-component knot, and both windings $\geq 2$ for non-trivial winding in both directions. As the lightest stable lepton with non-trivial topology, the electron must be $(2,3)$.

- _Specific Claims_
  - $(2,3)$ is the unique smallest non-trivial coprime torus knot (gcd=1, both windings $\geq 2$, lowest crossing $c=3$).
  - The electron is forced to $(2,3)$ as the lightest stable non-trivial lepton.
- _Specific Non-Claims and Caveats_
  - $(2,3)$ is the phase-space Clifford-torus winding; the electron's real-space topology is the $0_1$ unknot (per Vol 1 Ch 8).

> **Leaf references:** [torus-knot-uniqueness](./particle-physics/ch01-topological-matter/torus-knot-uniqueness.md).

### Quality
- confidence: 0.7
- depends-on:
  - INVARIANT-S2 / Axiom 1 (K4 chiral lattice supporting torus-knot windings)
  - clm-h9aqmt (electron = lightest stable lepton, the identification premise)
- solidity: 0.70 (ok to build on, see caveats) [= min(0.70, 0.70)]
- rationale: The mathematical half is clean standard knot theory (essentially a theorem): $(2,3)$ is provably the smallest non-trivial coprime torus knot (gcd=1, both windings $\ge2$, lowest crossing $c=3$), with the candidate enumeration correct. The one clearly-disclosed assumption is the physical identification "electron = lightest stable non-trivial lepton $\Rightarrow$ simplest knot $\Rightarrow(2,3)$"; the leaf labels this explicitly as the AVE assertion atop the standard math, and carries a resolved muon/proton $(2,5)$ consistency flag. Clean standard-math derivation + one disclosed identification.
- strengthen-by:
  - Derive (not assert) that "lightest stable lepton = simplest non-trivial knot" follows from a Faddeev-Skyrme energy ordering on K4.
  - Establish that the lepton ladder is the Cosserat-torsion ladder (fixed $(2,3)$) from dynamics, closing the FI-13 framing rather than asserting it.

---

## Neutron — Canonical Identification + First-Principles Axiom Audit
<!-- id: clm-6kwzot -->

AVE-native canonical identification of the neutron as $6_2^3 \cup 0_1$ (the proton Borromean linkage plus a threaded electron unknot), structured to parallel the proton and electron identification leaves. Provides a 4-property definition, a first-principles axiom audit per property, and an 8-framing cross-corpus translation guide.

- _Specific Claims_
  - Canonical AVE neutron topology is $6_2^3 \cup 0_1$ (proton Borromean + threaded electron unknot).
  - 4-property definition with first-principles axiom audit per property.
- _Specific Non-Claims and Caveats_
  - Honest scoping of 2 derivation gaps: mass split (1.293 MeV) mechanism is canonical but the FS energy is not derived; mean lifetime (880 s) mechanism is canonical but the WKB tunneling rate is not derived.
  - 3 stale corpus framings flagged for revision (Vol 4 trefoil-threading, Vol 6 axial-twist, SM udd-quark translation).

> **Leaf references:** [neutron-identification](./particle-physics/ch02-baryon-sector/neutron-identification.md).

### Quality
- confidence: 0.5
- depends-on:
  - INVARIANT-S2 / Axiom 1 (composite $6^3_2\cup0_1$ topology; flux-tube minimum thickness)
  - INVARIANT-S2 / Axiom 2 (charge neutrality via additive $+1+(-1)=0$ twist count)
  - clm-mnb3lt (proton $6^3_2$ / $m_p$ that the neutron composite builds on)
  - clm-uatcql (threaded electron $0_1$ identification)
  - clm-cmic3e (proton canonical identification the neutron composite incorporates)
- solidity: 0.50 (use as input only, don't build deeper) [= min(0.50, 0.63)]
- rationale: A rigorous, self-critical audit: the composite topology $n=6^3_2\cup0_1$ and charge neutrality are clean axiom-derived, but the leaf explicitly flags TWO load-bearing derivation gaps — the mass split $m_n-m_p\approx1.293$ MeV is mechanism-named (elastic-expansion tension) but NOT derived from a Faddeev-Skyrme calculation, and the lifetime $\tau_n\approx880$ s mechanism is named but the rate is NOT derived. Magnetic moment and charge radius are structural-only. Substantive acknowledged open dependencies on the two main quantitative observables.
- strengthen-by:
  - Derive the 1.293 MeV mass split as $E_{FS}(6^3_2\cup0_1)-E_{FS}(6^3_2)$ from the threaded-knot Faddeev-Skyrme energy.
  - Derive $\tau_n$ from WKB tunneling through the threaded-knot dielectric barrier (would also address the bottle-vs-beam anomaly).

---

## Proton — Canonical Identification + First-Principles Axiom Audit
<!-- id: clm-cmic3e -->

AVE-native canonical identification of the proton, structured to parallel the electron and photon identification leaves. Provides a 4-property definition (🔴 *[2026-06-08 relabels — walk-back from proton-identification.md corrections 1+2]* $(2,5)$ cinquefoil **phase-space per-loop polarization winding** [~~"cinquefoil topology"~~ — NOT real-space; cf electron-identification.md:23 + constants.py:689-694] + $6_2^3$ Borromean linkage **as the real-space topology** + dimensionless confinement-budget ratio $r_{opt} = \kappa_{FS}/5 = 8\pi/5 \approx 5.03$ [~~"$\approx 4.97\,\ell_{node}$"~~ — a pure number, NOT a length; $\kappa_{FS}=8\pi$ is a pure geometric constant per constants.py:683-687; the only measured proton size is the sub-node $D_p=0.841$ fm, $\approx 460\times$ smaller than $\ell_{node}$] + Axiom-4-saturated core), a first-principles axiom audit per property, and a per-input audit of the mass eigenvalue across 6 inputs (all first-principles, no fit parameters), plus a 6-framing cross-corpus translation guide.

- _Specific Claims_
  - Unlike $m_e$ (a calibration anchor), $m_p/m_e = 1836.12$ is derived with zero baryon-data-tuned parameters (electron-physics-provenanced: $m_e + \alpha$, replacing Skyrme's $F_\pi + e$) — AVE's flagship mass prediction (axiom-derived; the per-channel loop-role is a matched structural assignment, same class as the lepton couplings — see the parameter ledger). 🔴 *[framing precision 2026-06-08 — walk-back from correction 3]* bare topology predicts **+0.74%** (emergence vs baryon sector, zero baryon input); the canonical $\delta_{th}=1/(14\pi^2)$ thermal correction (precision-setter) refines to **−0.002%** from CODATA. The $-0.002\%$ is topology + one contained thermal-residual, ~~0.002% from CODATA~~ NOT pure-geometry-to-ppm.
  - All 6 mass-eigenvalue inputs ($\kappa_{FS}=8\pi$, $c_5=5$, $\mathcal{I}_{scalar}\approx 1162$, $\mathcal{V}_{total}=2$ dual-reactance count ($X_C + X_L$; NOT a FEM-integrated volume), $p_c=8\pi\alpha$, +1.0 charge twist) are first-principles.
- _Specific Non-Claims and Caveats_
  - 🔴 *[2026-06-08 — walk-back from correction 2]* open audit items: $\mathcal{I}_{scalar}$ solver documentation; corpus hygiene on duplicate subsection titles; **and the proton's real-space sub-node geometry** — the body is $D_p=0.841$ fm, $\approx 460\times$ smaller than $\ell_{node}=386$ fm; the $r_{opt}=8\pi/5$ ratio is dimensionless (NOT a $\sim 5\,\ell_{node}$ real-space extent), so the sub-node geometry is underived ~~(was previously mis-stated as a "$\sim 5$ lattice-spacing genuinely extended object")~~.

> **Leaf references:** [proton-identification](./particle-physics/ch02-baryon-sector/proton-identification.md).

### Quality
- confidence: 0.7
- depends-on:
  - INVARIANT-S2 / Axioms 1–4 (per-property axiom audit; $(2,5)$ cinquefoil + $6^3_2$ Borromean + saturated core)
  - clm-mnb3lt (the $m_p/m_e=1836.12$ eigenvalue this leaf audits input-by-input)
  - clm-67jn9o (Witten-effect fractional quark charges)
  - clm-9s9apq (packing fraction $p_c$; vol1)
  - clm-8c3yhs ($(2,3)$ torus-knot uniqueness — the proton's $(2,5)$ cinquefoil assignment is "the next stable entry after the electron's $(2,3)$" on the $(2,q_{odd})$ ladder, which rests on the coprimality + minimality argument that anchors $(2,3)$ as the lightest non-trivial coprime torus knot)
- solidity: 0.63 (use as input only, don't build deeper) [= min(0.70, 0.63)]
- rationale: A rigorous per-input audit of the flagship $m_p/m_e=1836.12$ (🔴 *[2026-06-08]* bare topology $+0.74\%$ emergence vs baryon sector; canonical $\delta_{th}=1/(14\pi^2)$ thermal correction refines to $-0.002\%$ — ~~0.002%~~ not pure-geometry-to-ppm; zero baryon-data-tuned parameters): $\kappa_{FS}=8\pi$, $c_5=5$, $\mathcal{V}_{total}=2$ (dual-reactance count $X_C + X_L$, NOT a FEM-integrated volume), $p_c=8\pi\alpha$, and the $+1.0$ charge twist are each traced to axioms (the per-channel loop-gain $=p_c$ identification is a matched structural assignment, same class as the lepton couplings — see ledger). The audit is honest that $\mathcal{I}_{scalar}\approx1162$ is a computational input flagged for solver verification, and it inherits the Gaussian-ansatz bound of clm-mnb3lt. Consistent with the clm-mnb3lt band — disclosed methodology bound.
- strengthen-by:
  - Verify the 1D Faddeev-Skyrme solver implementation has no tunable parameter and document the $\mathcal{I}_{scalar}$ convergence.
  - Close the inherited Gaussian flux-tube ansatz gap upstream in clm-mnb3lt.

---

## AVE-Native Petermann Coefficient via Route B
<!-- id: clm-v2sg8z -->

Two-loop Petermann coefficient $C_2$ derived from substrate dynamics in two stages with explicit honesty about derived-vs-postulated content. Stage 1 (symmetric Route B forward) gives $C_2 = -0.3416$ → 4% off PDG with no postulate and no fit. Stage 2 (saliency closure with the n_q-additivity postulate $\delta = -3\alpha/2$) gives $C_2 = -0.32846$ → 50 ppm at $C_2$ / ≈10 ppm at $a_e$ total.

- _Specific Claims_
  - Stage 1 symmetric Route B forward: $C_2 = -0.3416$, 4% off PDG, no postulate, no fit.
  - Stage 2 with n_q-additivity postulate: $C_2 = -0.32846$, ≈10 ppm at $a_e$ total.
- _Specific Non-Claims and Caveats_
  - The ppm-level headline is postulate-conditional (n_q-additivity), made explicit per Action 2 of the 2026-05-18 walk-back; the corpus admits n_q-additivity is the "single remaining intuitive step."

> **Leaf references:** [q-g19a-petermann-saliency-closure](./particle-physics/ch06-electroweak-higgs/q-g19a-petermann-saliency-closure.md).

### Quality
- confidence: 0.6
- depends-on:
  - INVARIANT-S2 / Axiom 4 (saturation-kernel asymmetry; dark-resonance near-field back-reaction)
  - clm-stgx1i (leading-order $a_e=\alpha/2\pi$ that the $1/\pi^2$ form factor and two-loop build on)
  - clm-8c3yhs ($(2,3)$ phase-space trefoil $d/q$-axis structure)
- solidity: 0.60 (use as input only, don't build deeper) [= min(0.60, 0.70)]
- rationale: Two-stage with explicit honesty. Stage 1 (symmetric Route B, no postulate, no fit) yields $C_2=-0.3416$, 4% off PDG — a genuine substrate-mechanism prediction. Stage 2's ppm headline ($C_2=-0.32846$, $\approx10$ ppm at $a_e$) is explicitly conditional on the $n_q$-additivity postulate, which the leaf itself admits is "the single remaining intuitive step." The two-stage framing makes derived-vs-postulated visible (per the 2026-05-18 walk-back). Disclosed methodology bound: closes at 4% with no postulate, ppm precision postulate-gated.
- strengthen-by:
  - Derive $n_q$-additivity ($\delta=-\alpha n_q/2$) from the K4-Cosserat Lagrangian, converting the ppm closure from postulate-conditional to derived.
  - Land the independent bisection verification (`verify/electron_g2_petermann.py`) to confirm $\delta^*=-0.01093$.

---

## Q-G20f Vacuum Polarization: Matches QED via RT-Equivalence
<!-- id: clm-bqtasn -->

The one-loop vacuum polarization function $\Pi(q^2)$ in AVE matches QED at all observable scales via a Renormalization-Theorem equivalence: AVE's saturation kernel + lattice cutoff and QED's UV-renormalized polynomial expansion produce structurally identical results at $q \ll 1/\ell_{node}$. The lattice geometric cutoff at $\pi/\ell_{node}$ removes QED's Landau pole structurally.

- _Specific Claims_
  - $\Pi(q^2)$ matches QED at all observable scales via RT-equivalence.
  - The lattice cutoff at $\pi/\ell_{node}$ removes the QED Landau pole structurally.
- _Specific Non-Claims and Caveats_
  - Differences appear only at sub-Compton scales (pair-production physics) and ultra-high energies.
  - The AVE-distinct chiral piece is $\alpha$-suppressed (relevant only for precision polarimetry).

> **Leaf references:** [q-g20f-vacuum-polarization](./particle-physics/ch06-electroweak-higgs/q-g20f-vacuum-polarization.md).

### Quality
- confidence: 0.6
- depends-on:
  - INVARIANT-S2 / Axiom 1 (Brillouin-zone geometric cutoff at $\pi/\ell_{node}$)
  - INVARIANT-S2 / Axiom 3 (local relativistic action; same low-energy U(1) gauge content as QED)
  - INVARIANT-S2 / Axiom 4 (saturation-kernel inverse $K(V)$ giving the cubic vertex)
- solidity: 0.60 (use as input only, don't build deeper) [= min(0.60, 1.00)]
- rationale: The match-to-QED is argued structurally via Renormalization-Theorem equivalence: AVE is a local relativistic field theory with the same low-energy U(1) content, so its loop predictions must agree with QED after renormalization — a sound consistency-check argument. The cubic vertex + BZ-cutoff mechanism is sketched and the $\Pi(q^2)$ match is argued (not independently computed here); the Landau-pole removal via the geometric cutoff is a clean structural consequence. Disclosed consistency check, match argued rather than computed.
- strengthen-by:
  - Compute $\Pi(q^2)$ from the cubic vertex with the BZ cutoff and show it equals QED's $-(\alpha/3\pi)q^2\ln(q^2/m_e^2)$ explicitly.
  - Quantify the $\alpha$-suppressed AVE-distinct chiral piece so the sub-Compton discriminator is testable.

---

## Q-G27 Muon Cosserat Torsion Saliency
<!-- id: clm-8niffj -->

AVE forward-predicts a topological/Cosserat second-order effect contributing to the muon g−2 anomaly that the Standard Model does not capture, with zero fit parameters. The muon Cosserat torsion-quantum saliency $\delta_{\text{Cosserat}}^\mu = -\alpha\sqrt{3/7}/(2\pi)$; textbook QED conversion gives a forward $\Delta a_\mu^{(2)} = +502 \times 10^{-11}$.

- _Specific Claims_
  - Forward prediction $\Delta a_\mu^{(2)} = +502 \times 10^{-11}$ from $\delta_{\text{Cosserat}}^\mu = -\alpha\sqrt{3/7}/(2\pi)$, zero fit parameters.
  - The same $\sqrt{3/7}$ mechanism that gives $m_\mu$ at 1.24% drives the saliency.
- _Specific Non-Claims and Caveats_
  - 4.6σ tension above Fermilab Run-3 ($+245(56)\times 10^{-11}$) on the e+e- baseline; BMW-baseline-conditional.
  - Prior corpus $+247$ value was a factor-2 conversion error walked back 2026-05-18.

> **Leaf references:** [q-g27-muon-cosserat-saliency](./particle-physics/ch06-electroweak-higgs/q-g27-muon-cosserat-saliency.md).

### Quality
- confidence: 0.45
- depends-on:
  - INVARIANT-S2 / Axiom 4 (Cosserat torsional excitation; $\sqrt{3/7}$ PAT torsion-shear projection)
  - clm-v2sg8z (Q-G19α electron Petermann closure this parallels / builds on)
  - clm-rji99i (shared $\sqrt{3/7}$ mechanism that also gives $m_\mu$)
- solidity: 0.45 (use as input only, don't build deeper) [= min(0.45, 0.55)]
- rationale: A zero-fit forward prediction $\delta^\mu_{Cosserat}=-\alpha\sqrt{3/7}/(2\pi)$ reusing the same $\sqrt{3/7}$ PAT projection that yields $m_\mu$ at 1.24% — a clean structural assembly. But the Cosserat-saliency identification (one torsion quantum adds exactly this $\delta$) is asserted/structural, the textbook-QED conversion gives $\Delta a_\mu^{(2)}=+502\times10^{-11}$ which is currently in **4.6$\sigma$ tension** with Fermilab on the e+e- baseline (BMW-baseline-conditional, so not refuted), and a prior $+247$ value was a walked-back factor-2 error. Asserted-structural with disclosed experimental tension.
- strengthen-by:
  - Resolve the e+e- vs BMW baseline ambiguity and state the prediction against the adjudicated SM baseline.
  - Derive the single-Cosserat-quantum saliency contribution from the K4-Cosserat Lagrangian rather than identifying it by analogy to the electron closure.

---

## Q-G20a Lamb Shift: Structural Closure via Today's Inputs
<!-- id: clm-3i66gp -->

The 2S–2P hydrogen Lamb shift ($+1057.85$ MHz measured) is reproduced at 0.65% structural precision at leading order by composing three substrate-native inputs, each with a separately-closed AVE derivation: finite-size self-energy ($+1010$ MHz) + Q-G20f vacuum polarization ($-27$ MHz) + Q-G19α anomalous moment ($+68$ MHz), totaling $\approx +1051$ MHz.

- _Specific Claims_
  - Lamb shift $\approx +1051$ MHz vs measured $+1057.85$ MHz (0.65%), composed from three separately-closed AVE derivations.
- _Specific Non-Claims and Caveats_
  - Structural-precision match at leading order only.

> **Leaf references:** [q-g20a-lamb-shift-structural-closure](./quantum-orbitals/ch07-quantum-mechanics/q-g20a-lamb-shift-structural-closure.md).

### Quality
- confidence: 0.45
- depends-on:
  - INVARIANT-S2 / Axiom 1 (finite-size electron; geometric UV cutoff $1/\ell_{node}$)
  - clm-h9aqmt (finite-size self-energy $T_{EM}\ell_{node}=m_ec^2$)
  - clm-bqtasn (Q-G20f vacuum-polarization contribution, $-27$ MHz)
  - clm-v2sg8z (Q-G19α anomalous-moment contribution, $+68$ MHz)
- solidity: 0.45 (use as input only, don't build deeper) [= min(0.45, 0.60)]
- rationale: A three-input composition reaching $\approx+1051$ MHz vs measured $+1057.85$ (0.65%). The vacuum-polarization and anomalous-moment terms inherit separately-closed AVE derivations, but the dominant self-energy term ($+1010$ MHz) has an acknowledged log discrepancy: the AVE Bethe-log-equivalent ($\approx9.84$) differs from QED's ($\approx2.81$) by 3.5×, glossed as "same magnitude — agree at the few-percent level." The total lands right, but the load-bearing self-energy magnitude effectively leans on the QED value rather than being cleanly derived. Disclosed-bound composition with a papered-over dominant-term discrepancy.
- strengthen-by:
  - Resolve the Bethe-log magnitude gap (9.84 vs 2.81) so the $+1010$ MHz self-energy is a clean AVE output, not a "same-magnitude" match.
  - Carry the composition to the next-order ($\alpha^5$ Bethe-log, recoil, nuclear size) to test beyond leading order.

---
