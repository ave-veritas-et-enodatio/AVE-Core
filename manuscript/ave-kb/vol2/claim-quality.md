# Vol 2 — Subatomic — Claim Quality

<!-- path-stable: referenced from CLAUDE.md INVARIANT-S7 and from vol2/index.md bootstrap directive -->

> **Canonicality:** Leaves are canonical; this volume's indexes are derived summaries. See [cross-cutting boundaries](../claim-quality.md) for the full preamble and the canonical list of project-wide tripwires (the cross-cutting sidecar is the source of truth for which tripwires are project-wide; do not infer the list from this preamble). Entries below are scoped to Vol 2; cross-cutting tripwires with vol2-specific manifestations are noted but not duplicated.

---

## Proton Mass Eigenvalue ($m_p/m_e \approx 1836.12$)

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

---

## Torus Knot Baryon Ladder

- $m(c) = \mathcal{I}_{scalar}(\kappa_{FS}/c)/(1 - \mathcal{V}_{total}\cdot p_c) + 1$ for odd $c = 3, 5, 7, 9, \ldots$
- _Specific Claims_
  - The $(2,q)$ torus knot ladder predicts the proton at $c=5$ and the $\Delta$-resonance spectrum at $c = 7, 9, 11, 13, 15$ from the **same** $\kappa_{FS}$, $\mathcal{V}_{total}$, $p_c$ — **no parameters adjusted between states**. This is a category (iv) derived prediction, not curve-fitting.
  - The matches are preferentially to $\Delta$ baryons ($I = 3/2$, higher-spin states) because higher $(2,q)$ winding carries higher intrinsic angular momentum.
- _Specific Non-Claims and Caveats_
  - Does NOT claim sub-percent accuracy across the full ladder. Reported deviations: $0.00\%$ (proton, by construction), $+2.35\%$ ($\Delta(1232)$), $-1.11\%$ ($\Delta(1600)$), $-0.27\%$ ($\Delta(1900)$), $+0.21\%$ ($N(2190)$), $+2.40\%$ ($\Delta(2420)$). Treat as $\sim 2\%$-band agreement with the standard PDG resonance assignments; do not summarise as "exact ladder".
  - Does NOT claim coverage of nucleon resonances with even $c$. There is no stable $(2,4)$ torus knot, so the ladder covers only odd-$q$ states; $N(1440)$ Roper, $N^*(1535)$, etc. are outside the ladder's scope.
  - The $(2,9) \to \Delta(1620)$ "best hit" ($0.20\%$) is highlighted in the leaf as a zero-parameter prediction; treat the headline as one row's success, not a global ladder accuracy claim.

> **Leaf references:** `particle-physics/ch02-baryon-sector/torus-knot-ladder-baryons.md`, `particle-physics/ch01-topological-matter/torus-knot-ladder.md`.

---

## Weinberg Angle $\sin^2\theta_W = 2/9$ (On-Shell Only)

- $\sin^2\theta_W = 1 - (M_W/M_Z)^2 = 1 - 1/(1+\nu_{vac}) = 1 - 7/9 = 2/9 \approx 0.2222$
- _Specific Claims_
  - The on-shell pole-mass ratio $M_W/M_Z = \sqrt{7/9}$ is derived from the Perpendicular Axis Theorem ($J = 2I$ for cylindrical flux tubes) and the isotropic elastic relation $E = 2G(1+\nu_{vac})$ with $\nu_{vac} = 2/7$. Zero free parameters.
  - Reported deviation: $-0.35\%$ vs PDG on-shell $0.2230$.
- _Specific Non-Claims and Caveats_
  - This is the **on-shell (tree-level pole-mass)** scheme, NOT $\overline{MS}$. The PDG $\overline{MS}$ value $0.2312$ differs by standard one-loop radiative running; comparing AVE's $2/9$ to $0.2312$ would yield the wrong $-3.89\%$ deviation that LIVING_REFERENCE.md Critical Distinction #2 explicitly warns against. Any summary that does not specify the scheme is silently wrong.
  - Does NOT claim derivation of one-loop radiative corrections. The AVE prediction is the tree-level pole ratio; the framework does not produce the $\overline{MS}$ running that converts on-shell to $\overline{MS}$.
  - Does NOT claim $J = 2I$ is an axiomatic input; it is the Perpendicular Axis Theorem applied to a circular cross-section (geometric identity for any cylindrical flux tube). The axiomatic input is the cylindrical-flux-tube model itself (Axiom 1's $d \equiv 1\,\ell_{node}$).

> **Leaf references:** `particle-physics/ch05-electroweak-mechanics/weinberg-angle.md`, `particle-physics/ch05-electroweak-mechanics/gauge-boson-masses.md`, `particle-physics/ch06-electroweak-higgs/higgs-mechanism.md`. Bound on scheme specificity asserted at invariant level — see `LIVING_REFERENCE.md` Critical Distinctions #2.

---

## $W$/$Z$ Boson Masses

- $m_W = m_e/(\alpha^2 p_c \sqrt{3/7})$, $m_Z = m_W \cdot 3/\sqrt{7}$
- _Specific Claims_
  - Both $M_W$ ($-0.57\%$ vs $80{,}379$ MeV) and $M_Z$ ($-0.62\%$ vs $91{,}188$ MeV) are derived from $m_e$, $\alpha$, $\nu_{vac} = 2/7$, and $p_c = 8\pi\alpha$. The $\alpha^2$ scaling reflects the $W$ self-energy as a **two-vertex process** (second-order perturbation theory in the chiral susceptibility); the $\sqrt{3/7}$ factor is the PAT torsion-shear projection.
- _Specific Non-Claims and Caveats_
  - Does NOT claim derivation of the Higgs VEV $v = 246$ GeV from independent first principles. The Higgs mechanism is reinterpreted (see Higgs Mass entry below) — VEV is identified with $Z_0 = 376.73\,\Omega$ characteristic impedance.
  - Does NOT claim the $W$/$Z$ widths or branching ratios are derived in the same chain. Only the pole masses and the on-shell mixing angle.
  - The $+1.24\%$ muon and $-0.95\%$ tau mass agreements reuse the same $\alpha$, $p_c$, $\sqrt{3/7}$ structure (Cosserat lepton spectrum); these are **not** independent validations of $W$/$Z$ — they are siblings on the same hierarchy $m_e \xrightarrow{\alpha\sqrt{3/7}} m_\mu \xrightarrow{\alpha\,p_c} m_\tau \xrightarrow{\alpha\,p_c} M_W$.

> **Leaf references:** `particle-physics/ch05-electroweak-mechanics/weak-coupling.md`, `particle-physics/ch05-electroweak-mechanics/gauge-boson-masses.md`, `particle-physics/ch06-electroweak-higgs/lepton-spectrum.md`, `particle-physics/ch06-electroweak-higgs/higgs-mass.md`.

---

## Higgs Mechanism Reinterpretation

- _Specific Claims_
  - AVE identifies the Standard Model VEV $v = 246$ GeV with the **characteristic impedance of free space** $Z_0 = \sqrt{\mu_0/\varepsilon_0} \approx 376.73\,\Omega$. Inertial mass is reinterpreted as Lenz's-law induction drag against this baseline impedance.
  - The empirical $125$ GeV LHC resonance is interpreted as a **transient acoustic relaxation mode** of the LC condensate, not a fundamental scalar field excitation.
  - $m_H/v = 1/\sqrt{N_{K4}}$ with $N_{K4} = 4$ (K4 cell breathing), consistent with Master Prediction Table #25 ($-0.55\%$).
- _Specific Non-Claims and Caveats_
  - This is an **ontological reinterpretation**: the same numerical $v = 246$ GeV underlies all SM electroweak predictions. AVE does not produce a Higgs-free Standard Model with different observable predictions at the EW scale.
  - Does NOT claim the $125$ GeV LHC peak is "not the Higgs". The framework asserts the resonance exists with a different physical mechanism (acoustic relaxation), not that the experimental signal is absent or misidentified.
  - The reinterpretation does not produce new electroweak observables distinguishable from the SM Higgs picture without testing the acoustic-relaxation hypothesis directly (e.g., width, decay channel anomalies) — none currently demonstrated.

> **Leaf references:** `particle-physics/ch06-electroweak-higgs/higgs-mass.md`, `particle-physics/ch06-electroweak-higgs/higgs-mechanism.md`.

---

## $g-2$ Anomaly: Schwinger's Result $a_e = \alpha/(2\pi)$

- $a_e = (1/\pi^2) \times (\pi\alpha/2) = \alpha/(2\pi) \approx 0.001161$ (Master Prediction Table #3, $+0.09\%$)
- _Specific Claims_
  - Schwinger's leading-order result is **derived structurally** from the Axiom 4 saturation operator, the unknot ropelength, and the lattice pitch — three structural constants. No Feynman diagrams or perturbative renormalization required.
  - The on-site electric strain identity $(V_{peak}/V_{snap})^2 = 4\pi\alpha$ is exact: $\alpha$ **is** the on-site electric strain.
- _Specific Non-Claims and Caveats_
  - Does NOT claim derivation of the higher-order QED corrections ($\alpha^2$, $\alpha^3$, $\alpha^4$, $\alpha^5$ terms) that bring $a_e$ to its current 12-digit precision. The AVE result is the leading-order Schwinger value only.
  - Does NOT claim the muon $g-2$ anomaly (BNL/Fermilab discrepancy at $\sim 4\sigma$) is resolved by this derivation. The muon $a_\mu$ is not addressed in this leaf.
  - The decomposition $a_e = (1/\pi^2)\times(\pi\alpha/2)$ uses the unknot diameter $2R = \ell/\pi$ (Axiom 1); this is the same geometry that fixes the electron mass, not an independent input.

> **Leaf references:** `particle-physics/ch06-electroweak-higgs/higgs-mass.md` (the Schwinger derivation appears in this leaf's "Schwinger's Anomalous Magnetic Moment" section).

---

## PMNS Mixing Angles and CP Phase $\delta_{CP} = 61\pi/45$

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

> **Leaf references:** `particle-physics/ch03-neutrino-sector/chiral-screening.md`, `particle-physics/ch03-neutrino-sector/pmns-eigenvalues.md`, `particle-physics/ch03-neutrino-sector/delta-cp-violation.md`.

---

## Neutrino Mass and Hierarchy

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

---

## Quark Charges via Witten Effect on $\mathbb{Z}_3$ Borromean Symmetry

- $q_{eff} = n + (\theta/2\pi)e$ with $\theta \in \{0, \pm 2\pi/3, \pm 4\pi/3\}$
- _Specific Claims_
  - Fractional quark charges $\pm 1/3\,e$ and $\pm 2/3\,e$ are derived directly from the discrete $\mathbb{Z}_3$ permutation symmetry of the $6^3_2$ Borromean linkage applied through the Witten Effect. No fundamental fractionalisation of the underlying lattice.
  - Quarks are **deconfined topological quasiparticles**, not separately existing point particles; the proton's total $Q_{total} = +1\,e$ remains an integer winding number.
- _Specific Non-Claims and Caveats_
  - Does NOT claim derivation of all six quark masses from a single zero-parameter formula. The mass derivations ($m_u = m_e/(2\alpha_s)$, $m_d = m_e/(\alpha_s\cos\theta_W)$, $m_s = m_\mu\cos\theta_W$, etc.) appear as separate scale-invariance entries in the Master Prediction Table (#33–#38, $0.8$–$2.4\%$); they share structural ingredients but are individual derivations, not a single closed-form spectrum.
  - The "quarks have never been isolated" experimental fact is interpreted in AVE as quarks being **structurally inseparable** from the Borromean cage (deconfined within, not removable). This is consistent with QCD confinement empirically; AVE provides a different mechanism, not a different observable.

> **Leaf references:** `particle-physics/ch02-baryon-sector/topological-fractionalization.md`, `particle-physics/ch02-baryon-sector/quark-flavors.md` (stub redirecting to topological-fractionalization).

---

## Atomic Ionization Energy Solver (Z = 1–14, Max 2.8% Error)

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

> **References:** Bound on the Z = 1–14 validity range and the four correction gates is asserted at invariant level — see `LIVING_REFERENCE.md` §"Axioms in the Atomic Domain" (Corrections A–D specifications) and Pitfalls #6, #7, #8, #9, #10, #11. Supporting derivation steps appear in `quantum-orbitals/ch07-quantum-mechanics/` leaves: `radial-eigenvalue-solver.md`, `ionization-energy-validation.md`, `screening-rule.md`, `de-broglie-n.md`, `de-broglie-standing-wave.md`, `bonding-mode-formula.md`, `chiral-factor.md`, `helium-symmetric-cavity.md`, `hierarchical-cascade-correction.md`, `orbital-penetration-penalties.md`. The proofs-computation leaf `proofs-computation/ch09-computational-proof/methodological-contamination.md` documents the Bohr/Schrödinger contamination hazard explicitly.

---

## Hopf-Pair Coupling and Same-Shell vs Cross-Shell Screening

- Cross-shell: $\sigma_{cross} = N_{inner}$ (Gauss, Axiom 2). Same-shell: $\sigma_{same} = (N_{same} - 1) \times J_{shell}$, $J_{1s^2} = (1+p_c)/2 \approx 0.5917$ (Axiom 4).
- _Specific Claims_
  - Two distinct screening physics coexist: cross-shell Gauss screening (electrostatic, integer $N_{inner}$) and same-shell lattice coupling (chiral $J_{shell}$ from Op4). Treating them as the same operator is structurally wrong.
  - For He ($1s^2$), the Hopf coupling $k_1 = (2/Z)(1 - p_c/2) = 0.9083$ produces bonding-mode IE $24.37$ eV vs experiment $24.587$ eV ($-0.88\%$).
  - For same-$n$ different-$l$ (e.g. $2s$/$2p$ in B): coupled-line even/odd-mode formalism (not Gauss) is required; modeling $2s^2$ as a Gauss screen for $2p$ over-screens by $\sim 58\%$.
- _Specific Non-Claims and Caveats_
  - The current B and beyond accuracy is documented as **open**: the "Be and B remain open: the corrections are applied *outside* the phase integral, violating the action principle" (radial-eigenvalue-solver.md §E2j). The complete-phase-integral architecture (§E2k) is presented as the in-progress correct architecture — not yet validated end-to-end across Z $\ge 5$.
  - Does NOT claim coupled-microstrip same-shell formalism is independently validated at the atomic scale beyond the Hopf-pair Be result. The cross-scale isomorphism with protein $\beta$-sheet and antenna coupled-microstrip is a structural identification.

> **Leaf references:** `quantum-orbitals/ch07-quantum-mechanics/screening-rule.md`, `quantum-orbitals/ch07-quantum-mechanics/helium-symmetric-cavity.md`, `quantum-orbitals/ch07-quantum-mechanics/hierarchical-cascade-correction.md`, `quantum-orbitals/ch07-quantum-mechanics/bonding-mode-formula.md`, `quantum-orbitals/ch07-quantum-mechanics/radial-eigenvalue-solver.md`.

---

## Spin-1/2 as Macroscopic Gyroscopic Precession

- $d\mathbf{L}/dt = \gamma\,\mathbf{L} \times \mathbf{B}$; classical-vs-quantum deviation $\sim 10^{-8}$ at machine precision.
- _Specific Claims_
  - The classical gyroscope ODE and the SU(2) Pauli-spinor Schrödinger evolution are **mathematically identical** under projection onto the Bloch sphere; the maximum deviation is at numerical-integration tolerance.
  - The Spin-1/2 paradox (continuum $SO(3)$ media should support only integer-spin point defects) is resolved because the electron is an **extended** $0_1$ unknot, not a point defect; the Finkelstein-Misner kink (Dirac belt trick) provides the $SU(2)$ double cover via topological extension.
- _Specific Non-Claims and Caveats_
  - Does NOT claim a violation of standard QM predictions for spin-dependent observables (Zeeman, Stern-Gerlach, EPR correlations). The framework asserts the **mechanism** is classical gyroscopic precession; observable predictions match standard QM.
  - The claimed equivalence is at the single-particle level (one spin in an external field). Multi-particle entanglement / Bell-inequality predictions are not addressed in vol2 spin chapter; the agreement with classical ODE applies to NMR/EPR-style scenarios, not arbitrary entanglement experiments.
  - The Larmor frequency $\omega_L = \gamma B_0$ is recovered as a classical precession rate; this is an **ontological reinterpretation** (categories (i)/(iii) cohabit), not a novel numerical prediction.

> **Leaf references:** `particle-physics/ch01-topological-matter/spin-gyroscopic-isomorphism.md`, `particle-physics/ch04-quantum-spin/spin-as-precession.md`, `particle-physics/ch04-quantum-spin/larmor-derivation.md`, `appendices/app-b-paradoxes/spin-half-paradox.md`.

---

## Yang-Mills Mass Gap (Framework-Conditional, Not Clay-Rigorous)

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

---

## Navier-Stokes Smoothness (Framework-Conditional, Not Clay-Rigorous)

- $\|\nabla^2_\ell\| = 4/\ell^2$ (bounded discrete Laplacian); $\Omega \le 2Nc^2/\ell$ (bounded enstrophy); Picard-Lindelöf on bounded Lipschitz domain.
- _Specific Claims_
  - On the discrete lattice with rigid pitch $\ell = \ell_{node}$, the discrete Laplacian is a strictly bounded operator; velocity is clamped to $\le c$ by Axiom 4; enstrophy is bounded; existence and uniqueness follow from Picard-Lindelöf for ODEs on bounded Lipschitz domains.
  - The continuum "blow-up" is interpreted as an artefact of removing the lattice floor.
- _Specific Non-Claims and Caveats_
  - This is **NOT a Clay-rigorous proof for the continuum Navier-Stokes equation**. The result is rigorous *for the discrete lattice variant*; promoting to the Clay statement requires either accepting Axiom 1's discrete pitch as physical or formalising a lattice-to-continuum limit theorem that preserves the bound. The latter is open future work.
  - LIVING_REFERENCE.md Master Prediction Table #15 explicitly: "Framework-derived (lattice + Picard-Lindelöf; not Clay-rigorous)". Same caveat applies; downstream summarisation must preserve it.

> **Leaf references:** `nuclear-field/ch12-millennium-prizes/navier-stokes-prize.md`. Caveat asserted at invariant level — see `LIVING_REFERENCE.md` Master Prediction Table note #15.

---

## Strong CP Problem ($\theta = 0$ Exactly)

- _Specific Claims_
  - On the AVE lattice the vacuum angle $\theta = 0$ exactly: the unique ground state has $\mathbf{E}_n = \mathbf{B}_n = 0$ and zero topological charge. Transitions between $\theta$-sectors require creating a topological defect, which costs energy $\ge \Delta$ (the mass gap), so the vacuum cannot tunnel between sectors.
  - **No axion is needed** — the framework has zero free parameters for this prediction (vs Peccei-Quinn's $f_a$).
- _Specific Non-Claims and Caveats_
  - This is **NOT a Clay-rigorous result** and is not on the Clay list — but the same lattice-conditional caveat applies, as flagged in Master Prediction Table note #16. The "uniqueness of the AVE vacuum topology" is asserted, not formally proven against all possible competing ground states within ZFC.
  - Does NOT claim falsification of the QCD axion search programme. AVE asserts the axion is unnecessary within its framework, not that experimental axion searches will falsify a particle whose existence the framework already excludes.

> **Leaf references:** `nuclear-field/ch10-open-problems/strong-cp.md`. Caveat asserted at invariant level — see `LIVING_REFERENCE.md` Master Prediction Table note #16.

---

## Baryon Asymmetry $\eta = 6.08 \times 10^{-10}$

- $\eta = \delta_{CP} \cdot \alpha_W^4 \cdot C_{sph} / g_*$ with $\delta_{CP} = \pi/\kappa_{FS}$, $\alpha_W = \alpha/\sin^2\theta_W$, $C_{sph} = 28/79$, $g_* = 7^3/4 = 85.75$
- _Specific Claims_
  - Master Prediction Table #22: $0.38\%$ vs observed $\eta_{obs} = 6.1 \times 10^{-10}$. Every factor is derived from AVE lattice constants — zero phenomenological inputs to the asymmetry formula.
  - Using SM $g_*^{(SM)} = 106.75$ in the same formula yields $20\%$ error; the AVE $g_* = 85.75$ from $\nu_{vac} = 2/7$ via $7^3/4$ closes that gap.
- _Specific Non-Claims and Caveats_
  - The 0.38% headline is a **composite consistency check**: $\delta_{CP}$, $\alpha_W^4$, $C_{sph}$, and $g_*$ are each AVE-derived, but the multi-factor formula and the multiplicative cancellations make per-factor sensitivity hard to attribute. Treat as a coupled multi-factor result, not a single-quantity prediction.
  - The CP-violating phase used here, $\delta_{CP} = \pi/\kappa_{FS} \approx 0.126$, is a **different quantity** from the PMNS $\delta_{CP} = 61\pi/45 \approx 1.36\pi$ in the neutrino chapter. The "δ_CP" symbol refers to two distinct physical phases (lattice chirality fraction in the baryon asymmetry; PMNS torsional accumulation in neutrino oscillations). Summaries that conflate these are wrong.
  - Does NOT claim $g_* = 85.75$ is independently measured. The validation is via the downstream baryon ratio; the lattice-DoF-counting metric is asserted, not directly observed.
  - The Sakharov-conditions framing (C/CP violation from lattice chirality + electroweak phase transition) reuses the standard out-of-equilibrium picture for its third condition; this is consistency with the Sakharov framework, not its derivation.

> **Leaf references:** `nuclear-field/ch10-open-problems/baryon-asymmetry.md`, `nuclear-field/ch10-open-problems/g-star-derivation.md`, `nuclear-field/ch10-open-problems/g-star-prediction.md`.

---

## Hubble Constant $H_\infty \approx 69.32$ km/s/Mpc — Vol 2 Framing

See cross-cutting [Master Prediction Table reading conventions](../claim-quality.md). Vol3 sidecar carries the full $H_\infty$ entry (lattice-genesis circularity caveat; CODATA $G$ substitution; geometric self-consistency proof, not first-principles ab initio prediction). Vol2 framing notes:

- _Specific Claims_
  - Vol 2 Ch 10's Hubble Tension leaf presents $H_\infty = 28\pi m_e^3 c G/(\hbar^2 \alpha^2) \approx 69.32$ km/s/Mpc as "every factor rigorously derived from lattice structure and bounding limits", positioned $+2.9\%$ above Planck (CMB) and $-5.1\%$ below SH0ES (local).
- _Specific Non-Claims and Caveats_
  - The framing-of-asymmetric-systematics ("CMB low-density-void calibration" vs "local Cepheid impedance calibration") is an **interpretive consequence**, not an independent quantitative derivation of either measurement's residual.
  - The cross-cutting circularity caveat (Vol3 sidecar: $R_H \equiv c/H_\infty$ enters $G$ via $\xi$, so rearranging back to "compute" $H_\infty$ from CODATA $G$ is structurally an identity) applies here as well. Treat the vol2 leaf's "every factor rigorously derived" wording as inheriting the vol3-documented caveat; do NOT summarise vol2's framing as a parameter-free first-principles prediction of $H_0$.

> **Leaf references:** `nuclear-field/ch10-open-problems/hubble-tension.md`. Cross-cutting caveat documented in vol3 sidecar's Asymptotic Hubble Constant entry; bound asserted at the kb-claims-boundaries-followups level (see `kb-claims-boundaries-followups.md` 2026-05-02 entry on vol3 index circularity framing).

---

## String Theory Translation: Regge Slope $\alpha' \approx 0.75$ GeV$^{-2}$

- $T_{AVE} = m_e^2 c^3/\hbar \approx 0.212$ N; $\alpha' = 1/(2\pi T_{AVE}) \approx 0.75$ GeV$^{-2}$; $\alpha'_{baryon} = \alpha'/(m_p/m_e) \approx 4.09\times 10^{-4}$ GeV$^{-2}$
- _Specific Claims_
  - The fundamental EM string tension and the hadronic Regge slope are derivable from $m_e$, $c$, $\hbar$ (no free parameters); 17% deviation from the empirical $\alpha' \approx 0.9$ GeV$^{-2}$.
  - 10–11D compactification is unnecessary in AVE because flux tubes have finite transverse radius (Axiom 1), Axiom 4 provides a UV regulator, and Faddeev-Skyrme stabilisation works in 3D.
- _Specific Non-Claims and Caveats_
  - The 17% deviation on the EM Regge slope is **not sub-percent**; treat as order-of-magnitude consistency, not a precision derivation.
  - The QCD string-tension agreement ($\alpha'_{baryon}$ vs phenomenological $10^{-4}$ GeV$^{-2}$) is "matches to within an order of magnitude natively" (the leaf's wording). This is not a quantitative replacement for lattice QCD's $\sigma \approx 1$ GeV/fm string-tension measurements.
  - Does NOT claim a derivation of standard string theory observables (mass spectra of meson trajectories, etc.) at sub-percent precision. The mapping is structural (string tension $\leftrightarrow$ inductive energy density), not a phenomenological replacement.

> **Leaf references:** `nuclear-field/ch08-planck-string/planck-scale-derivation.md`, `nuclear-field/ch08-planck-string/string-theory-translation.md`.

---

## Universal Strain Energy Functional and Overdrive Demonstrations

- $U_{total} = \sum_{i<j} K_{mutual}/d_{ij} + \sum_i U_{bond}(\theta_i, \phi_i)$; nuclear $K_{mutual} = (5\pi/2)\,\alpha\hbar c/(1 - \alpha/3) \approx 11.337$ MeV·fm
- _Specific Claims_
  - The same $O(N^2)$ impedance-minimising gradient-descent solver, **unmodified**, derives U-235 binding energy (sub-percent through actinides, $<0.01\%$ for $A \le 28$) and Polyalanine backbone dihedrals ($\phi \approx -57°$, $\psi \approx -47°$) from the same operator chain.
  - Computational scaling: AVE $O(N^2)$ with 0 parameters and seconds on single-core, vs Lattice QCD $O(N^3)$+ with $\sim 6$ parameters on supercomputer-months, vs AlphaFold $O(N^2)$ with $\sim 10^8$ NN weights on GPU-cluster-hours.
- _Specific Non-Claims and Caveats_
  - The "single solver, two domains" framing is a **scale-invariance** claim about the operator chain — the universal coupling $K_{mutual}$ formulae differ between nuclear and biological domains. The $\alpha/3$ correction in $K_{mutual}$ is nuclear-specific.
  - The U-235 binding energy convergence "with $<0.01\%$ error for $A \le 28$" is for **light nuclei** through silicon; sub-percent through actinides is a coarser claim. Per-actinide error breakdowns are not reported in this leaf.
  - The polyalanine $\alpha$-helix dihedral emergence is a **structural** validation (geometry recovered from minimisation); does not claim quantitative folding-rate or thermodynamic-stability prediction at the single-protein level.
  - Does NOT claim AVE replaces Lattice QCD or AlphaFold in their respective production roles. The comparison is methodological (scaling, free parameters), not a head-to-head accuracy benchmark.

> **Leaf references:** `proofs-computation/ch11-overdrive/index.md`, `proofs-computation/ch11-overdrive/universal-energy.md`, `proofs-computation/ch11-overdrive/overdrive-nuclear.md`, `proofs-computation/ch11-overdrive/overdrive-protein.md`, `proofs-computation/ch11-overdrive/overdrive-comparison.md`.

---

## Methodological Contamination Discipline (Project-Wide Hazard, Vol2 Manifestation)

- _Specific Claims_
  - The framework requires all atomic energy states to emerge from the 5-step universal regime-boundary eigenvalue method. The Rydberg energy $Ry = \alpha^2 m_e c^2/2$ is **emergent** from the electron cavity saturation boundary, not a postulate.
  - Multi-electron repulsion uses the discrete-cavity Subshell Impedance Cascade (Cross-Shell Gauss + Same-Shell topologic node sorting), explicitly NOT continuous $N$-body integration over smeared probability densities and explicitly NOT $Z_{eff}$ fitting.
- _Specific Non-Claims and Caveats_
  - This is a **discipline statement** about acceptable derivation practice within the framework, not a new physical prediction. Its inclusion in vol2 leaves as a methodological boundary makes it a tripwire for downstream claims, not a result the table-of-predictions tracks.
  - The five LIVING_REFERENCE.md atomic-domain pitfalls (#7 Iterative SCF, #8 QM contamination in IE, #9 Op4 bypass, #10 De Broglie ≠ impedance, #11 Smooth CDF for saturated shells) are each instances of this same contamination hazard at specific operator boundaries. A claim that AVE "matches QM" anywhere in the atomic domain must verify it does not match by silently importing the QM formula it claims to replace.

> **References:** Discipline asserted at invariant level — see `LIVING_REFERENCE.md` "Common Pitfalls" #7–#11 and Critical Distinctions; "Red flags for QM contamination" checklist therein. Supporting derivation-discipline statements appear in `proofs-computation/ch09-computational-proof/methodological-contamination.md`, `proofs-computation/ch09-computational-proof/precision-policy.md`, and the QM-translation appendix `quantum-orbitals/ch07-quantum-mechanics/qm-ave-translation.md`.

---

## Holographic Principle Recovery (Stress Test, Not Independent Prediction)

- _Specific Claims_
  - Even though the AVE vacuum is a discrete 3D lattice, the Holographic Principle's $R^2$ entropy scaling is recovered: information transmission traverses 1D inductive flux tubes whose bandwidth is bounded by their 2D cross-sectional porosity $\Phi_A \equiv \alpha^2$. Nyquist-Shannon projects channel capacity onto the 2D causal-horizon bounding surface.
- _Specific Non-Claims and Caveats_
  - This is a **stress-test resolution** (App B paradoxes), demonstrating internal consistency of the lattice picture against an established constraint — not an independent quantitative derivation of the Bekenstein-Hawking entropy formula. The cross-sectional-porosity argument is presented as the geometric mechanism, not a calculation of $S_{BH} = A/(4\ell_P^2)$ ab initio.
  - Does NOT claim falsification of any specific holographic-duality framework (AdS/CFT, dS/CFT). The framework asserts the principle is recoverable in AVE, not that competing formulations are excluded.

> **Leaf references:** `appendices/app-b-paradoxes/holographic-paradox.md`.
