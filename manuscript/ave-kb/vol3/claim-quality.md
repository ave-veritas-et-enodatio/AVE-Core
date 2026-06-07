# Vol 3 — Macroscopic Physics — Claim Quality

<!-- path-stable: referenced from CLAUDE.md INVARIANT-S7 and from vol3/index.md bootstrap directive -->

> **Canonicality:** Leaves are canonical; this volume's indexes are derived summaries. See [cross-cutting claim-quality register](../claim-quality.md) for the full preamble and the canonical list of project-wide tripwires (the cross-cutting sidecar is the source of truth for which tripwires are project-wide; do not infer the list from this preamble). Entries below are scoped to Vol 3; cross-cutting tripwires with vol3-specific manifestations are noted but not duplicated.

---

## Asymptotic Hubble Constant $H_\infty$
<!-- id: clm-wx5324 -->

- $H_{\infty} = 28\pi m_{e}^{3}cG / (\hbar^{2}\alpha^{2}) \approx 69.32$ km/s/Mpc
- _Specific Claims_
  - The relation between $G$ and $H_\infty$ is a **geometric consistency proof**, not an independent first-principles prediction of $H_0$. The Machian coupling $\xi = 4\pi(R_H/\ell_{node})\alpha^{-2}$ embeds $R_H \equiv c/H_\infty$ in the definition of $G$; rearranging back to "compute" $H_\infty$ from $G$ is structurally an identity, not a downstream evaluation.
  - Numerically the relation evaluates to $\sim 69.32$ km/s/Mpc when CODATA $G$ is substituted; this lies between Planck (67.4) and SH0ES (73.0), within $\sim 1\sigma$ of TRGB (69.8).
  - The framework's claim is that "Hubble Tension" reflects different thermodynamic regime measurements of a single underlying lattice crystallisation rate, not that AVE outputs $H_0$ ab initio.
- _Specific Non-Claims and Caveats_
  - Does NOT claim a parameter-free derivation of $H_0$ from axioms 1–4 alone. The lattice-genesis leaf explicitly flags this and points to [Outstanding Rigour Gaps](../common/mathematical-closure.md).
  - Does NOT claim AVE resolves the Hubble Tension by selecting one measurement over the other; the claim is that both are compatible with the same geometric constraint.
  - Promoting this to a true downstream prediction requires deriving $G$ from a local thermodynamic balance independent of $R_H$ — open problem.

> **Leaf references:** [asymptotic-expansion-limit](./cosmology/ch04-generative-cosmology/asymptotic-expansion-limit.md), [lattice-genesis-hubble-tension](./cosmology/ch04-generative-cosmology/lattice-genesis-hubble-tension.md), [asymptotic-hubble-constant](./gravity/ch01-gravity-yield/asymptotic-hubble-constant.md), [optical-refraction-gravity](./gravity/ch01-gravity-yield/optical-refraction-gravity.md).

### Quality
- confidence: 0.7
- depends-on:
  - Axiom 3 (Minimum Reflection Principle — the action that fixes $G$)
  - `clm-m3z5ux` (Vol 1 $H_\infty$ / MOND derivation, solidity X)
  - `clm-mroghg` (Vol 2 $H_\infty$ framing, solidity X)
  - `clm-9s9apq` (Vol 1 $p_c = 8\pi\alpha$ packing relation, solidity X)
- solidity: 0.55 (use as input only, don't build deeper) [= min(0.70, 0.55)]
- rationale: The resultbox states $H_\infty = 28\pi m_e^3 cG/(\hbar^2\alpha^2)$, but the leaf itself frames this as a **geometric consistency proof** — $G$ and $H_\infty$ are "the same geometric limit evaluated from different topological reference frames," not an ab-initio prediction of $H_0$. The Machian coupling embeds $R_H \equiv c/H_\infty$ in the definition of $G$, so rearranging to "compute" $H_\infty$ is structurally circular. The algebra closes cleanly; the disclosed circularity (an unbroken open dependency on a $G$ that is not independently derived) pins the band below a clean derivation.
- strengthen-by:
  - Derive $G$ from a local thermodynamic balance independent of $R_H$ (the leaf's named open problem), converting the consistency proof into a true downstream prediction.
  - Close the Class-E joint-constraint at $u_0^*$ so $\{G, H_\infty, \alpha\}$ are not co-defined.

---

## Refractive Index of Gravity $n(r) = 1 + 2GM/(c^2 r)$
<!-- id: clm-rd9cjm -->

- $n(r) = 1 + \nu_{vac}\,\varepsilon_{11} = 1 + (2/7)\,\varepsilon_{11}$ with $\varepsilon_{11}(r) = 7GM/(c^2 r)$
- _Specific Claims_
  - The refractive form $n(r) = 1 + 2GM/(c^2 r)$ is the **temporal component** of the lattice metric — specifically the slope-2 **bulk/coordinate-time propagation index** ($\approx 1/g_{00}$, Shapiro). The genuine **local clock rate / redshift** is the slope-1 $\sqrt{g_{00}} \approx 1 - GM/rc^2$, $z = GM/rc^2 = (n-1)/2$. (W2 relabel 2026-06-05; bulk-vs-local disambiguation, value unchanged.)
  - Light deflection couples to a **separate spatial component** $n_{spatial} = 1 + (9/7)\varepsilon_{11}$. The Einstein deflection $\delta = 4GM/(bc^2)$ comes from integrating the full bidirectional metric; the temporal-only $n(r)$ alone reproduces the Newtonian half-deflection, not the GR value.
  - Solar deflection at the Einstein value is a **category (iii) consistency check** (per cross-cutting Master Prediction Table tripwire) — the framework reproduces the standard result via metric refraction, not an independent novel prediction.
- _Specific Non-Claims and Caveats_
  - Does NOT claim that the same $n(r)$ governs both clock-rate and light-deflection observables. LIVING_REFERENCE.md Pitfall #3: using full lattice density $n = 1 + (11/7)\varepsilon_{11}$ for redshift, or the temporal-only $n$ for deflection, are both errors.
  - Does NOT claim Snell-ray ray-tracing of $n(r)$ alone yields $\delta = 4GM/(bc^2)$ without the trace-reversal projection through $\nu_{vac}$.
  - "Speed of light slows near mass" ($c_{local} = c_0/n$) is **local phase velocity**, not energy transport speed. See cross-cutting Symmetric vs Asymmetric Saturation entry: the impedance is invariant ($Z = Z_0$), so this is not a dispersive medium in the dissipative sense.
  - The $c_{max}$ inference (intergalactic $c$ exceeds local $c$ by $\sim 3{,}600$ m/s, "warp transit baseline") is an extrapolation of the same local refraction relation to $\Phi \to 0$; treat as illustrative of the framework's interpretation, not as an experimentally validated prediction.

> **Leaf references:** [alpha-invariance-symmetric-gravity](./gravity/ch01-gravity-yield/alpha-invariance-symmetric-gravity.md), [kinetic-yield-threshold](./gravity/ch01-gravity-yield/kinetic-yield-threshold.md), [leaky-cavity-decay](./gravity/ch01-gravity-yield/leaky-cavity-decay.md), [one-seventh-impedance-projection](./gravity/ch01-gravity-yield/one-seventh-impedance-projection.md), [optical-refraction-gravity](./gravity/ch01-gravity-yield/optical-refraction-gravity.md), [static-nodal-tension](./gravity/ch01-gravity-yield/static-nodal-tension.md), [temporal-spatial-lattice-decomposition](./gravity/ch01-gravity-yield/temporal-spatial-lattice-decomposition.md), [topological-packing-fraction](./gravity/ch01-gravity-yield/topological-packing-fraction.md), [trace-reversal-mechanism](./gravity/ch01-gravity-yield/trace-reversal-mechanism.md), [frame-dragging-impedance-convolution](./gravity/ch02-general-relativity/frame-dragging-impedance-convolution.md), [gravitational-refractive-index-gradient](./gravity/ch02-general-relativity/gravitational-refractive-index-gradient.md), [k4-tlm-lensing-validation](./gravity/ch02-general-relativity/k4-tlm-lensing-validation.md), [achromatic-impedance-matching](./gravity/ch03-macroscopic-relativity/achromatic-impedance-matching.md), [cauchy-implosion-resolution](./gravity/ch03-macroscopic-relativity/cauchy-implosion-resolution.md), [einstein-lensing-deflection](./gravity/ch03-macroscopic-relativity/einstein-lensing-deflection.md), [gordon-optical-metric](./gravity/ch03-macroscopic-relativity/gordon-optical-metric.md), [gravitomagnetism-frame-dragging](./gravity/ch03-macroscopic-relativity/gravitomagnetism-frame-dragging.md), [newtonian-gravity-optical-gradient](./gravity/ch03-macroscopic-relativity/newtonian-gravity-optical-gradient.md), [ponderomotive-equivalence](./gravity/ch03-macroscopic-relativity/ponderomotive-equivalence.md), [refractive-index-of-gravity](./gravity/ch03-macroscopic-relativity/refractive-index-of-gravity.md), [transverse-refractive-index](./gravity/ch03-macroscopic-relativity/transverse-refractive-index.md).

### Quality
- confidence: 0.9
- depends-on:
  - Axiom 3 (Minimum Reflection Principle — trace-reversal boundary)
  - Axiom 4 (Universal Saturation Kernel — radial strain $\varepsilon_{11}$)
  - `clm-iouqn9` (common: K4 magic-angle $\nu_{vac} = 2/7$, solidity X)
  - `clm-9s9apq` (Vol 1 EMT $p_c = 8\pi\alpha$, solidity X)
- solidity: 0.55 (use as input only, don't build deeper) [= min(0.90, 0.55)]
- rationale: $n(r) = 1 + (2/7)(7GM/c^2r) = 1 + 2GM/c^2r$ is clean algebra once $\nu_{vac} = 2/7$ (trace-reversal, EMT-verified in the companion leaf) and the radial strain $\varepsilon_{11} = 7GM/c^2r$ are in hand. The temporal/spatial split (deflection couples to $1 + (9/7)\varepsilon_{11}$) is disclosed and consistent. The $c_{max}$ "warp baseline" extrapolation to $\Phi\to0$ is explicitly flagged interpretive and does not load-bear on the core refractive identity. Solar deflection is a category-(iii) consistency check, not novelty.
- strengthen-by:
  - Derive $\varepsilon_{11} = 7GM/c^2r$ (the factor-7 Machian stress boundary $T_{max} = c^4/7G$) from primitives within this leaf rather than importing it.
  - Make the temporal/spatial projection ratio $9/7$ vs $2/7$ explicit in this leaf instead of the companion.

---

## Gravitational Wave Propagation — Invariant Impedance
<!-- id: clm-07kd5v -->

- $Z(r) = \sqrt{\mu_{eff}(r)/\varepsilon_{eff}(r)} \equiv Z_0$; $\Gamma = 0$ across any gravitational gradient
- _Specific Claims_
  - GWs are transverse inductive shear waves in the LC lattice; under Symmetric Scaling ($\mu, \varepsilon$ both scale by $n(r)$) the macroscopic impedance is invariant and the reflection coefficient across any gravitational gradient is identically zero. Lossless propagation matches LIGO observation.
  - All observed GW signals are far in **Regime I** (deeply linear) but at very different saturation ratios per signal class (`einstein-field-equation.md` regime table): GW150914 (BBH) at $V_{GW}/V_{snap} \sim 10^{-28}$; GW170817 (BNS) at $\sim 10^{-29}$; pulsar timing at $\sim 10^{-22}$. The vacuum acts as a perfect lossless transmission line; nonlinear corrections are negligible at observed strains.
  - Near-merger ($r \lesssim 10\,r_s$) reaches the I–II boundary at $V_{GW}/V_{snap} \sim 10^{-8}$; nonlinear corrections to waveforms become relevant only here.
- _Specific Non-Claims and Caveats_
  - Does NOT claim GWs experience refractive bending, scattering, or dispersion in transit. $\Gamma = 0$ everywhere under Symmetric Gravity.
  - The "Symmetric Scaling axiom" wording in the GW leaves is a **derived consequence** of Axiom 3 (gravity scales mass-energy and thus both $\mu$ and $\varepsilon$), not an independent fifth axiom.
  - Does NOT claim AVE predicts deviations from GR's lossless GW propagation in the linear regime — the prediction is the same as linearized GR for currently observed signals. Distinguishing AVE from GR requires either near-merger nonlinear waveform residuals or polarization tests.
  - The shear-wave freeze inside the saturation boundary ($c_{shear} \to 0$ as $\varepsilon_{11} \to 1$) is the cross-cutting Symmetric Saturation result; see cross-cutting Symmetric vs Asymmetric Saturation. GWs cannot propagate through the ruptured BH interior.

> **Leaf references:** [einstein-field-equation](./gravity/ch02-general-relativity/einstein-field-equation.md), [fabry-perot-phase-shift](./gravity/ch08-gravitational-waves/fabry-perot-phase-shift.md), [gw-detection-antenna](./gravity/ch08-gravitational-waves/gw-detection-antenna.md), [gw-impedance-perturbation](./gravity/ch08-gravitational-waves/gw-impedance-perturbation.md), [gw-propagation-lossless](./gravity/ch08-gravitational-waves/gw-propagation-lossless.md), [invariant-gravitational-impedance](./gravity/ch08-gravitational-waves/invariant-gravitational-impedance.md), [ligo-gw-saturation-ratio](./gravity/ch08-gravitational-waves/ligo-gw-saturation-ratio.md), [standard-quantum-limit](./gravity/ch08-gravitational-waves/standard-quantum-limit.md).

### Quality
- confidence: 0.9
- depends-on:
  - Axiom 3 (Minimum Reflection Principle)
  - Axiom 4 (Universal Saturation Kernel — symmetric scaling of $\mu,\varepsilon$)
  - `clm-gdd70j` (Vol 1 universal operators $Z,S,\Gamma$, solidity X)
  - `clm-rd9cjm` (Vol 3 refractive index $n(r)$, solidity X)
- solidity: 0.55 (use as input only, don't build deeper) [= min(0.90, 0.55)]
- rationale: $Z(r) = \sqrt{\mu_0 n/\varepsilon_0 n} \equiv Z_0$ is an exact algebraic identity given symmetric scaling, so $\Gamma = 0$ across any gradient follows immediately. The leaf is honest that "Symmetric Scaling" is a **derived consequence of Axiom 3**, not a fifth axiom. The regime table (GW150914/170817/pulsar saturation ratios) is order-of-magnitude but the lossless-propagation conclusion is a clean consequence. Band held just below 1.0 because the per-source $V_{GW}/V_{snap}$ values are stated, not derived in this leaf.
- strengthen-by:
  - Derive the per-source saturation ratios from source parameters within the leaf rather than tabulating them.
  - Spell out the I–II boundary onset ($\sim 10^{-8}$) as a calculation, not an assertion.

---

## Black Hole Interior — Lattice Phase Transition, Not Impedance Mismatch
<!-- id: clm-ir8h78 -->

- $r_{sat} = 7GM/c^2 = 3.5\,r_s$ (saturation boundary); interior: $G_{shear} \to 0$, $c_g \to 0$
- _Specific Claims_
  - The event horizon at $r_s = 2GM/c^2$ marks the dielectric saturation limit ($\varepsilon_{11}(r_s) = 1$ in the GW-gauge formulation); the interior beyond $r_{sat}$ is in **Regime IV** (ruptured topology).
  - Confinement of the BH interior is via a **phase transition** ($G_{shear} \to 0$, shear restoring force vanishes) — NOT via an impedance mismatch. Under Symmetric Gravity $Z(r) = Z_0$ everywhere and $\Gamma = 0$.
  - The interior is a "dissipative sink" / perfect absorber for shear waves; this is the macroscopic $S = 0$ boundary, not a $\Gamma \to -1$ reflection (the latter is the **electron** mechanism, not the BH).
  - The classical singularity is replaced by a topological halting: $\rho_{eff} \to \infty$ as $\varepsilon_{11} \to 1$ freezes infalling matter at $r \approx r_{sat}$, forming a hollow / densely compact shell.
- _Specific Non-Claims and Caveats_
  - Does NOT claim the BH event horizon reflects radiation. No reflection ($\Gamma = 0$) — the boundary absorbs.
  - Does NOT claim BH and electron use the same confinement mechanism. The cross-scale "isomorphism" (Master Prediction Table #45) is operator-level (same $S = 0$ kernel) at different saturation symmetries — BH is symmetric (hole / topology destruction), electron is asymmetric (knot / topology preservation). Conflating these is the most common reading error in the cross-scale leaves.
  - Does NOT claim a numerical match to BH interior observations. The interior is observationally inaccessible; the claim is structural (a phase transition exists at $r_{sat}$), not numerical.
  - The "pre-geometric plasma" and "information loss siding with Hawking" framings are interpretive consequences of the lattice picture, not independent results.

> **Leaf references:** [black-holes-impedance-mismatch](./cosmology/ch04-generative-cosmology/black-holes-impedance-mismatch.md), [constructive-destructive-paradox](./cosmology/ch15-black-hole-orbitals/constructive-destructive-paradox.md), [electron-bh-isomorphism](./cosmology/ch15-black-hole-orbitals/electron-bh-isomorphism.md), [interior-singularity-resolution](./cosmology/ch15-black-hole-orbitals/interior-singularity-resolution.md), [dielectric-rupture-event-horizon](./gravity/ch03-macroscopic-relativity/dielectric-rupture-event-horizon.md).

### Quality
- confidence: 0.7
- depends-on:
  - Axiom 4 (Universal Saturation Kernel — $\varepsilon_{11}(r_{sat}) = 1$)
  - `clm-iouqn9` (common: $\nu_{vac} = 2/7$, solidity X)
  - `clm-rd9cjm` (Vol 3 refractive index / radial strain, solidity X)
  - `clm-07kd5v` (Vol 3 symmetric impedance $Z = Z_0$, solidity X)
- solidity: 0.55 (use as input only, don't build deeper) [= min(0.70, 0.55)]
- rationale: The confinement mechanism ($G_{shear}\to0$, $c_g\to0$ at $r_{sat} = 7GM/c^2$) follows cleanly from $\varepsilon_{11}(r_{sat}) = 1$ plus the symmetric-impedance result ($\Gamma = 0$). The electron-vs-BH contrast (knot $\Gamma=-1$ vs hole phase-transition) is structural and internally consistent. Band sits at disclosed-bound rather than clean-derivation because the interior is explicitly **observationally inaccessible** — the claim is structural (a phase transition exists), and the saturation picture it rests on is an imported/asserted regime rather than a closed interior solution.
- strengthen-by:
  - Provide a worked interior solution (even schematic) showing $G_{shear}(r)\to0$ continuously across $r_{sat}$.
  - Reconcile the "$\Gamma=0$ everywhere" framing here with the "$\Gamma=-1$" titled sibling leaf (`black-holes-impedance-mismatch.md`) to remove the disclosed inter-leaf tension.

---

## AVE Compactness Limit ($2/7$ vs Buchdahl)
<!-- id: clm-x19btt -->

- $R > 7GM/c^2 \;\Longleftrightarrow\; 2GM/(c^2 R) < 2/7 = \nu_{vac}$
- _Specific Claims_
  - The lattice cannot support $\varepsilon_{11} > 1$; any static configuration with surface radius $R < 7GM/c^2$ has its surface inside Regime IV (ruptured).
  - This bound is **stricter** than the GR Buchdahl bound ($2GM/(c^2 R) < 8/9 \approx 0.889$). AVE limit: $2/7 \approx 0.286$.
  - A 1.4 $M_\odot$ neutron star at $R = 10$ km has $\varepsilon_{11} = 1.46 > 1$, implying a Regime-IV core with a Regime-III crust held by the saturation phase transition. This is consistent with the established quark-matter / colour-superconductor picture but is **not derived from observation**; it is what the AVE bound implies given the canonical NS parameters.
- _Specific Non-Claims and Caveats_
  - Does NOT claim AVE has been validated against observed neutron star equation-of-state data. The compactness statement is a kinematic upper bound on lattice strain, not a competing EOS calculation.
  - Does NOT claim the Buchdahl bound is wrong — AVE is **strictly more restrictive** within its own framework, but the GR bound remains valid in standard GR.
  - The recurrence of $2/7 = \nu_{vac}$ across packing fraction, compliance modes, Hubble derivation, and compactness is a **scale-invariance claim** (the same Poisson ratio projecting through K4/SRS geometry), not an empirical numerology coincidence — but treat the recurrence as an interpretive thread, not as independent evidence for any single instance.

> **Leaf references:** [ave-compactness-limit](./cosmology/ch15-black-hole-orbitals/ave-compactness-limit.md), [vacuum-poisson-ratio](./gravity/ch01-gravity-yield/vacuum-poisson-ratio.md).

### Quality
- confidence: 0.9
- depends-on:
  - Axiom 4 (Universal Saturation Kernel — $\varepsilon_{11}(r_{sat}) = 1$)
  - `clm-iouqn9` (common: $\nu_{vac} = 2/7$, solidity X)
  - `clm-rd9cjm` (Vol 3 radial strain / refractive index, solidity X)
- solidity: 0.55 (use as input only, don't build deeper) [= min(0.90, 0.55)]
- rationale: The compactness bound $R > 7GM/c^2 \Leftrightarrow 2GM/c^2R < 2/7$ is direct algebra from $\varepsilon_{11}(R) = 1$ and $\nu_{vac} = 2/7$; the comparison to Buchdahl ($8/9$) is exact. The NS test case (1.4 $M_\odot$ at 10 km → $\varepsilon_{11} = 1.46$) is illustrative and the leaf is careful to call it "what the AVE bound implies," not a validated EOS. Clean derivation; the $2/7$ recurrence is flagged interpretive (not extra evidence).
- strengthen-by:
  - Derive the factor-7 ($T_{max} = c^4/7G$) within the leaf rather than carrying it from the strain definition.

---

## AVE Merger Ringdown $\omega_R M_g = 18/49$
<!-- id: clm-395gps -->

- $\omega_R \cdot M_g = \ell(1 + \nu_{vac})/x_{sat} = 18/49 \approx 0.3673$ for $\ell = 2$
- _Specific Claims_
  - The Schwarzschild $\ell = 2$ fundamental QNM is derived from Axioms 1–4 with **zero free parameters**: $r_{sat} = 7M_g$ (Axiom 4), $r_{eff} = r_{sat}/(1 + \nu_{vac}) = 49M_g/9$ (Poisson), $\omega_R = \ell c/r_{eff}$ (mode).
  - Schwarzschild value: $0.3673$ vs GR exact $0.3737$, **error 1.7%** — a category (iv) derived prediction, not an identity or consistency check.
  - Quality factor $Q = \ell$ (so $Q = 2$ for $\ell = 2$); $\omega_I M = 9/98$ vs GR $0.0890$, error 3.2%.
- _Specific Non-Claims and Caveats_
  - Does NOT claim sub-percent agreement on ringdown frequency for spinning remnants. The Kerr-corrected LIGO ringdown comparisons (GW150914, GW170104, GW151226) show **10–18%** frequency error and 10–14% decay-time error, not the sub-percent precision the Schwarzschild case suggests.
  - Does NOT claim derivation of the Kerr radial structure from first principles; the Kerr correction inherits the Schwarzschild AVE structure via a phenomenological photon-sphere shift formula and the assumption that the "Lense-Thirring frequency" is reinterpreted as an asymmetric impedance convolution rate.
  - The Kerr quality factor matches GR sub-2% only for $a_* = 0.3$–$0.8$; behaviour outside this spin range is not validated in the leaf.
  - "$Q = \ell$" is the lattice-derived form; for higher modes ($\ell > 2$) this disagrees with GR overtone structure — the claim is the fundamental mode, not the full QNM spectrum.

> **Leaf references:** [accretion-disk-resonance](./cosmology/ch15-black-hole-orbitals/accretion-disk-resonance.md), [ave-merger-ringdown-eigenvalue](./cosmology/ch15-black-hole-orbitals/ave-merger-ringdown-eigenvalue.md), [axiom-coverage-audit](./cosmology/ch15-black-hole-orbitals/axiom-coverage-audit.md), [cross-scale-emission](./cosmology/ch15-black-hole-orbitals/cross-scale-emission.md), [first-principles-predictions](./cosmology/ch15-black-hole-orbitals/first-principles-predictions.md), [qnm-quality-factor](./cosmology/ch15-black-hole-orbitals/qnm-quality-factor.md), [qpo-frequency-impedance-resonance](./cosmology/ch15-black-hole-orbitals/qpo-frequency-impedance-resonance.md).

### Quality
- confidence: 0.8
- depends-on:
  - Axiom 4 (Universal Saturation Kernel — $\varepsilon_{11}(r_{sat}) = 1$)
  - `clm-iouqn9` (common: $\nu_{vac} = 2/7$, solidity X)
  - `clm-rd9cjm` (Vol 3 radial strain, solidity X)
  - `clm-x19btt` (Vol 3 compactness limit / $r_{sat}$, solidity X)
- solidity: 0.55 (use as input only, don't build deeper) [= min(0.80, 0.55)]
- rationale: The Schwarzschild $\ell=2$ eigenvalue $18/49 \approx 0.3673$ closes end-to-end from three axiom-grounded steps ($r_{sat} = 7M_g$, $r_{eff} = 49M_g/9$ via Poisson, $\omega_R = \ell c/r_{eff}$) with zero free parameters — a genuine 1.7%-error category-(iv) derived prediction. Band held below 0.9 because the Kerr extension rests on a **disclosed phenomenological** photon-sphere shift + Cosserat back-reaction fit (v2, refined post-hoc against LIGO), and $Q = \ell$ disagrees with GR overtone structure for $\ell > 2$. The Schwarzschild core is clean; the spinning-remnant comparisons (10–18% pre-Kerr-correction) are the disclosed weak edge.
- strengthen-by:
  - Derive the Kerr $x_{sat}(a_*)$ photon-sphere/Cosserat back-reaction form from primitives rather than fitting the rigid/compliant split.
  - Extend the mode rule to $\ell > 2$ and reconcile $Q = \ell$ with GR overtones, or scope the claim explicitly to the fundamental mode.

---

## Hawking Temperature as Classical Nyquist Noise
<!-- id: clm-c6k5om -->

- $T_H = \hbar c^3 / (8\pi G M k_B)$ (numerically the standard Hawking formula)
- _Specific Claims_
  - AVE reinterprets $T_H$ as the **Nyquist noise temperature** of the vacuum lattice evaluated at the impedance boundary, with the leakage rate set by $\partial_r S$ at $r_{sat}$ (Fluctuation-Dissipation Theorem at the imperfect phase boundary).
  - This is the macroscopic analogue of an excited atomic orbital's spontaneous emission spectrum, driven (per the cited leaf) by "classical thermodynamic leakage of lattice noise through the imperfect phase boundary," not by quantum tunnelling.
  - The numerical formula reproduces the standard Hawking expression — a category (iii) consistency check (alternative mechanism, same value).
- _Specific Non-Claims and Caveats_
  - Does NOT claim a novel numerical prediction distinguishable from the standard Hawking temperature at the formula level.
  - Does NOT claim the spectrum is exactly Planck-thermal in detail; the leaf gives a rate proportional to $\partial_r S$ at $r_{sat}$, not a worked-out spectral shape.
  - The mechanism ("classical thermodynamic leakage of lattice noise") is an **interpretive** claim — to falsify against standard QFT-Hawking requires an experimentally observed BH evaporation spectrum (none currently exists).
  - "AVE sides with Hawking on information loss" is a framework-internal interpretive consequence of the topology-destroying phase transition, not an independent derivation against unitarity arguments.

> **Leaf references:** [black-holes-impedance-mismatch](./cosmology/ch04-generative-cosmology/black-holes-impedance-mismatch.md), [hawking-temperature-nyquist-noise](./cosmology/ch15-black-hole-orbitals/hawking-temperature-nyquist-noise.md).

### Quality
- confidence: 0.5
- depends-on:
  - Axiom 4 (Universal Saturation Kernel — FDT at the phase boundary)
  - `clm-x19btt` (Vol 3 compactness / $r_{sat}$, solidity X)
  - `clm-ir8h78` (Vol 3 BH interior phase transition, solidity X)
- solidity: 0.50 (use as input only, don't build deeper) [= min(0.50, 0.55)]
- rationale: The leaf reproduces the standard $T_H = \hbar c^3/(8\pi GMk_B)$ but the AVE mechanism is asserted via a proportionality $P_{transmitted}\propto\partial_r S|_{r_{sat}}$ with no worked spectral shape and the standard formula imported, not derived. This is a category-(iii) consistency check at the formula level; the FDT/Nyquist reinterpretation is the new (interpretive) content. The unbridged step (rate-to-temperature with the standard coefficient assumed) and absence of a derived spectrum pin it at substantive-open-dependency.
- strengthen-by:
  - Derive the $T_H$ prefactor $\hbar c^3/(8\pi Gk_B)$ from $\partial_r S$ at $r_{sat}$ rather than quoting the standard result.
  - Produce the emission spectral shape and show where (if anywhere) it departs from Planck-thermal.

---

## MOND Acceleration Scale $a_0$ (Derived but Regime-Gated)
<!-- id: clm-u86caq -->

- $a_0 = c H_\infty / (2\pi) \approx 1.07 \times 10^{-10}$ m/s²
- _Specific Claims_
  - $a_0$ is **derived** from $H_\infty$ and $c$ (no free parameter); value is **10.7% below** the empirical $a_0 \approx 1.2 \times 10^{-10}$ m/s². The error is reported, not hidden.
  - The galactic MOND form $g_{eff} = g_N + \sqrt{g_N a_0}\sqrt{1 - g_N/a_0}$ is the Axiom 4 saturation operator with $g_N$ as the saturation amplitude and $a_0$ as the yield limit. This is a category (iv) derived prediction.
  - The "dark matter problem IS the Regime III→IV phase transition": outer galaxy ($g_N \ll a_0$) is unsaturated lattice with full mutual-inductive drag; inner galaxy ($g_N \gg a_0$) is saturated with zero drag (Keplerian).
- _Specific Non-Claims and Caveats_
  - Does NOT claim $a_0$ matches empirical to better than $\sim 11\%$. Treat the 10.7% deficit as the predictive accuracy; it is **not** a small-parameter result.
  - Does NOT claim MOND drag applies in the saturated inner-galaxy regime. LIVING_REFERENCE.md Pitfall #4: at $g_N \gg a_0$, $S(g_N/a_0) = 0$ and lattice drag is **zero**, not enhanced. Surface gravity of WD/NS ($g \sim 10^6$ m/s²) is far above $a_0$, hence zero MOND correction at stellar surfaces.
  - At $g_N \ge a_0$ the radical $\sqrt{1 - g_N/a_0}$ becomes imaginary; the leaf interprets this as an evanescent (non-propagating) drag mode that decays to zero. It is **not** an analytic continuation to a real negative drag.
  - Multi-galaxy validation table errors range 3–17% across the SPARC sample. The dwarf galaxy DDO 154 shows 17% error; do not extract a single "X%-accurate" headline.
  - The Tully-Fisher relation arises automatically from the deep-MOND limit; this is a structural consequence, not an independent fit.

> **Leaf references:** [asymptotic-limits](./cosmology/ch05-dark-sector/asymptotic-limits.md), [derived-mond-acceleration-scale](./cosmology/ch05-dark-sector/derived-mond-acceleration-scale.md), [effective-galactic-acceleration-mond](./cosmology/ch05-dark-sector/effective-galactic-acceleration-mond.md), [mcgaugh-empirical-rar](./cosmology/ch05-dark-sector/mcgaugh-empirical-rar.md), [multi-galaxy-validation](./cosmology/ch05-dark-sector/multi-galaxy-validation.md), [saturated-lattice-mutual-inductance](./cosmology/ch05-dark-sector/saturated-lattice-mutual-inductance.md).

### Quality
- confidence: 0.7
- depends-on:
  - Axiom 4 (Universal Saturation Kernel — saturation operator $S$)
  - `clm-wx5324` (Vol 3 $H_\infty$, solidity X)
  - `clm-m3z5ux` (Vol 1 $H_\infty$ / MOND, solidity X)
- solidity: 0.55 (use as input only, don't build deeper) [= min(0.70, 0.55)]
- rationale: $a_0 = cH_\infty/(2\pi)$ is a clean parameter-free derivation and the 10.7% deficit vs empirical $1.2\times10^{-10}$ is honestly reported (not a small-parameter result). The galactic form is the Axiom-4 saturation operator with $g_N$ as amplitude. Band sits at disclosed-bound because $a_0$ inherits the disclosed import of $H_\infty$ (itself a consistency proof, see clm-wx5324) and the multi-galaxy table errors range 3–17% — the derivation closes but rests on a disclosed approximation. Regime-gating (zero drag at $g_N\gg a_0$) is correctly stated.
- strengthen-by:
  - Derive the $2\pi$ Hoop-Stress projection factor from primitives within the leaf.
  - Close the $H_\infty$ dependency so $a_0$ is not downstream of a consistency proof.

---

## Anomalous Perihelion Advance — Consistency Check
<!-- id: clm-qyn8t0 -->

- $\Delta\phi = 6\pi G M_\odot / (c^2 a (1-e^2))$
- _Specific Claims_
  - The standard GR perihelion advance formula is reproduced via a $1/r^3$ tidal correction to the Newtonian potential, derived from the asymmetric impedance gradient of the displaced LC medium.
  - For Mercury, this gives $\sim 43$ arcsec/century — identical to GR; a category (iii) consistency check.
  - The framework asserts no "curved spacetime" is required; the same observable arises from mechanical impedance asymmetry.
- _Specific Non-Claims and Caveats_
  - Does NOT claim a novel numerical prediction distinguishable from GR for perihelion advance.
  - Does NOT claim the AVE derivation is independently confirmed against observational data beyond what already validates GR. This is reproduction-via-alternative-mechanism, with the same testable consequences as GR for the precession test.

> **Leaf references:** [anomalous-perihelion-advance](./cosmology/ch14-orbital-mechanics/anomalous-perihelion-advance.md), [macroscopic-avalanche-transconductance](./cosmology/ch14-orbital-mechanics/macroscopic-avalanche-transconductance.md), [orbital-regime-table](./cosmology/ch14-orbital-mechanics/orbital-regime-table.md), [saturn-ring-integrator](./cosmology/ch14-orbital-mechanics/saturn-ring-integrator.md), [solar-flares-led-avalanche](./cosmology/ch14-orbital-mechanics/solar-flares-led-avalanche.md).

### Quality
- confidence: 0.7
- depends-on:
  - Axiom 3 (Minimum Reflection Principle — Ponderomotive Equivalence pathway)
  - `clm-rd9cjm` (Vol 3 scalar refractive index $n_{scalar}$, solidity X)
  - `clm-iouqn9` (common: $\nu_{vac} = 2/7$ Poisson, solidity X)
- solidity: 0.55 (use as input only, don't build deeper) [= min(0.70, 0.55)]
- rationale: $\Delta\phi = 6\pi GM/c^2a(1-e^2)$ reproduces the GR value (43"/century) exactly — a category-(iii) consistency check. The leaf's own Grant-adjudication scope-notes (Foundation Items 4–6, preserved verbatim) disclose the chain honestly: the $1/r^3$ tidal term was initially GR-PPN-taken-as-input (Item 4), then shown substrate-native at leading PPN-1 via the Ponderomotive Equivalence pathway with the "3" coefficient recovered exactly (Item 5). The recovery closes but rests on the disclosed reduction to PPN-1 order; the AVE-distinct chirality correction is explicitly bracketed across 4 OOM and walked back (Item 6).
- strengthen-by:
  - Close the chirality-amplitude bracket ($\alpha^1\to\alpha^4$) by resolving the cosmic chirality fraction $f_R$, or scope the AVE-distinct test out of single-binary periastron.
  - Carry the substrate-native PPN-1 derivation (Item 5) into the leaf body rather than the scope-note.

---

## Solar System Boundaries (Oort, Kirkwood, Magnetopause)
<!-- id: clm-3kmt3p -->

- _Specific Claims_
  - Oort Cloud inner edge: $r_{sat} = \sqrt{GM_\odot/a_0} \approx 7{,}400$ AU — the radius where solar $g_N$ drops to the MOND threshold. Falls within the observed Hills Cloud range (2,000–5,000 AU); reported as "consistent with" rather than as a sub-percent match.
  - Kirkwood gaps: cavity-mode formula $a_{gap} = a_J (q/p)^{2/3}$ reproduces all five major gaps to $< 0.3\%$.
  - Planetary magnetopause: standoff radius from pressure balance $B^2/(2\mu_0) = (1/2)\rho_{sw} v_{sw}^2$ — Earth at 8.7%, Jupiter at 11.8% (Master Prediction Table #20, #21).
- _Specific Non-Claims and Caveats_
  - Magnetopause errors of 8.7% (Earth) and 11.8% (Jupiter) are not sub-percent; do not summarise these as "exact".
  - The Kirkwood-gap formula is the standard mean-motion-resonance result reinterpreted as an impedance cavity mode — a category (iii) consistency check, not a novel mechanism distinguishable from classical resonance theory.
  - Oort Cloud derivation depends on the $a_0$ prediction (which itself carries 10.7% systematic deficit; see MOND entry).

> **Leaf references:** [chapman-ferraro-enhancement](./cosmology/ch06-solar-system/chapman-ferraro-enhancement.md), [dipole-loss-cone-fraction](./cosmology/ch06-solar-system/dipole-loss-cone-fraction.md), [heliospheric-impedance-profile](./cosmology/ch06-solar-system/heliospheric-impedance-profile.md), [kirkwood-gaps-cavity-modes](./cosmology/ch06-solar-system/kirkwood-gaps-cavity-modes.md), [oort-cloud-saturation-boundary](./cosmology/ch06-solar-system/oort-cloud-saturation-boundary.md), [orbital-lc-friction-paradox](./cosmology/ch06-solar-system/orbital-lc-friction-paradox.md), [oumuamua-acceleration](./cosmology/ch06-solar-system/oumuamua-acceleration.md), [planetary-magnetopause-standoff](./cosmology/ch06-solar-system/planetary-magnetopause-standoff.md), [planetary-magnetospheres](./cosmology/ch06-solar-system/planetary-magnetospheres.md), [plasma-standoff-vs-gravitational-stator](./cosmology/ch06-solar-system/plasma-standoff-vs-gravitational-stator.md).

### Quality
- confidence: 0.6
- depends-on:
  - `clm-u86caq` (Vol 3 MOND $a_0$ — Oort boundary, solidity X)
  - `clm-gdd70j` (Vol 1 universal operators $Z,S,\Gamma$ — reflection coefficient, solidity X)
- solidity: 0.55 (use as input only, don't build deeper) [= min(0.60, 0.55)]
- rationale: Mixed-bag entry. Oort inner edge $r = \sqrt{GM_\odot/a_0} \approx 7400$ AU is a clean one-line formula but inherits the disclosed 10.7% $a_0$ deficit and lands only "within" (not on) the observed Hills range. Kirkwood $a_{gap} = a_J(q/p)^{2/3}$ reproduces all five gaps to <0.3% but is the standard mean-motion-resonance result reinterpreted (category-(iii)). Magnetopause uses standard pressure balance with errors 8.7%/11.8% (not sub-percent, correctly flagged). Each sub-result closes cleanly but uses empirical inputs / standard forms — disclosed-bound, averaged down for the heterogeneity.
- strengthen-by:
  - Derive the Kirkwood cavity-mode reinterpretation as distinguishable from classical MMR (currently a relabeling).
  - Remove the $a_0$ deficit dependency from the Oort prediction.

---

## Flyby Anomaly — Sagnac Shear Reinterpretation
<!-- id: clm-a71inj -->

- $\Delta V_{flyby} = V_\infty \cdot 2 (U_\oplus / c_0) \cos(\alpha_{geo}) \cos(\delta_{geo}) \approx 13.4$ mm/s
- _Specific Claims_
  - The flyby anomaly is interpreted as a Sagnac-RLVE shear-layer phase slip at the Earth's rotational boundary.
  - The pure geometrical formula yields $\sim 13.4$ mm/s without fitting parameters.
  - The leaf claims this **falsifies Lense-Thirring** as the mechanism (LT predicts an effect $\sim 10^6 \times$ smaller than observed).
- _Specific Non-Claims and Caveats_
  - Does NOT claim per-event match across Pioneer, Galileo, NEAR with quoted error bars. The leaf names those three missions as the empirical anomalies "resolved precisely" but gives only a single representative magnitude; per-event validation is asserted rather than tabulated.
  - "Falsifies Lense-Thirring" applies to the Lense-Thirring **mechanism for flyby anomalies specifically** (where the magnitudes disagree by $10^6$); does NOT claim Lense-Thirring is falsified as a gravitomagnetic effect generally.
  - The $\Gamma_{sagnac} \approx 1836$ acoustic shear factor reused in lunar/geodynamo derivations is a numerical coincidence with the proton/electron mass ratio asserted as cross-scale; this is a structural claim, not an independent derivation per application.

> **Leaf references:** [flyby-anomaly-sagnac-operator](./cosmology/ch14-orbital-mechanics/flyby-anomaly-sagnac-operator.md).

### Quality
- confidence: 0.7
- depends-on:
  - Axiom 4 (Universal Saturation Kernel — Regime-IV stator boundary $S(A)\to0$)
  - `clm-ce8dg1` (Vol 1 substrate-equilibrium velocity / preferred frame, solidity X)
- solidity: 0.50 (use as input only, don't build deeper) [= min(0.70, 0.50)]
- rationale: $\Delta V = V_\infty\cdot2(U_\oplus/c)(\cos\delta_{in} - \cos\delta_{out})$ is derived as a Sagnac-loop integral over the hyperbolic transit at the rigid Regime-IV stator boundary $R_\oplus$. The leaf's own 2026-05-18 walk-back is exemplary disclosure: it corrects the prior `cos α·cos δ` notation, removes the universal "13.4 mm/s" headline (NEAR-specific), and reports the verified Anderson-2008 anchor as 2/6 within 1σ, 3/6 within 2σ, 3/6 outliers. The mechanism closes against the empirical fit form; the disclosed partial per-spacecraft match (not all six) is what pins the band at disclosed-bound.
- strengthen-by:
  - Add per-spacecraft geometric corrections (atmospheric/magnetospheric) to capture the three >2σ outliers.
  - Derive the stator-boundary lock at $R_\oplus$ from the saturation kernel quantitatively (currently the 465 m/s vs 0.324 m/s factor is named as the "saturation amplification" without independent derivation).

---

## Lunar Inductive Heating — Tidal Inputs Required
<!-- id: clm-av2o4v -->

- $P_{topo} \approx 1.04$ TW via $\Gamma_{sagnac}$ amplification of standard tidal formula
- _Specific Claims_
  - Reproduces the empirical $\sim 1$–$2$ TW lunar heat budget that classical tidal-friction models underpredict by $\sim 1000\times$.
  - The $\sim 1000\times$ amplification is identified as the same $\Gamma_{sagnac}$ acoustic-shear factor used in flyby and geodynamo derivations.
- _Specific Non-Claims and Caveats_
  - Does NOT claim a parameter-free derivation of the lunar heat budget. The formula **uses** the Love number $k_2 \approx 0.022$ and dissipation $Q \approx 38$ as inputs — these are empirical lunar quantities, not AVE-derived.
  - The $\Gamma_{sagnac} \approx 1836$ factor is reused across applications without per-application derivation; treat its appearance here as cross-scale consistency, not as an independent prediction.

> **Leaf references:** [lunar-inductive-heating](./cosmology/ch14-orbital-mechanics/lunar-inductive-heating.md).

### Quality
- confidence: 0.5
- depends-on:
  - `clm-a71inj` (Vol 3 flyby Sagnac stator boundary — $\Gamma_{sagnac}$ mechanism, solidity X)
  - `clm-k3p9wz` (common: macroscopic Sagnac amplification = $m_p/m_e \approx 1836$ — asserted cross-scale identity supplying the $\Gamma_{sagnac}$ value, solidity X)
- solidity: 0.20 (do not build on, rework needed) [= min(0.50, 0.20)]
- rationale: $P_{topo} = (\text{standard tidal formula})\times\Gamma_{sagnac}$ recovers the ~1 TW lunar budget that classical tidal friction underpredicts by ~1000×. The leaf openly states the Love number $k_2 \approx 0.022$ and $Q \approx 38$ are **empirical lunar inputs**, not AVE-derived, and the $\Gamma_{sagnac}$ amplification is reused cross-application without per-application derivation. So the derivation closes only modulo a substantive imported amplification factor and two empirical inputs — substantive open dependency. (Note: leaf body says "$\Gamma\sim1000$" while the cross-ref note says "$\approx1836$"; flagged in worksheet.)
- strengthen-by:
  - Derive $\Gamma_{sagnac}$ (whether ~1000 or 1836) from the Earth–Moon orbital LC geometry within this leaf, resolving the internal value inconsistency.
  - Replace the empirical $k_2, Q$ with AVE-derived lunar response values, or scope the claim as "amplification of an empirically-anchored baseline."

---

## Geodynamo as VCA Back-EMF
<!-- id: clm-wd5rs0 -->

- $M_\oplus \approx 1.5 \times 10^{23}$ A·m² vs empirical $8.0 \times 10^{22}$ A·m²
- _Specific Claims_
  - Earth's magnetic dipole moment is recovered from a structural AC-motor formula combining solar-wind magnetopause $B$, Earth's core radius/conductivity, and the same $\Gamma_{sagnac} \approx 1836$ baryon-phase shear factor.
  - Falsifiability via Venus (slow rotation → no Sagnac amplification → near-zero field) and Mars (solid core → infinite DC resistance → collapsed eddy current).
- _Specific Non-Claims and Caveats_
  - Numerical match is $\sim 2\times$ the empirical value ($1.5 \times 10^{23}$ vs $8.0 \times 10^{22}$), not sub-percent. Treat as order-of-magnitude consistency, not a precision derivation.
  - The Venus/Mars "natural failures" are qualitative consistency arguments, not independent quantitative predictions of those bodies' field strengths.
  - The $\Gamma_{sagnac} = \mu_B \approx 1836$ identification (proton/electron mass ratio doubling as baryonic-phase-boundary acoustic shear) is asserted, not derived in this leaf.

> **Leaf references:** [geodynamo-vca-back-emf](./applied-physics/ch13-geophysics/geodynamo-vca-back-emf.md).

### Quality
- confidence: 0.3
- depends-on:
  - `clm-a71inj` (Vol 3 flyby Sagnac stator boundary — $\Gamma_{sagnac}$ mechanism, solidity X)
  - `clm-k3p9wz` (common: macroscopic Sagnac amplification = $m_p/m_e \approx 1836$ — asserted cross-scale identity supplying the $\Gamma_{sagnac}$ value, solidity X)
- solidity: 0.20 (do not build on, rework needed) [= min(0.30, 0.20)]
- rationale: The AC-motor back-EMF chain ($\mathcal{E}_{emf} = \omega_\oplus R_{core}\Gamma_{sagnac}\cdot B_{stator}\cdot2R_{core}$ → $M_\oplus$) is assembled from several plugged values (solar-wind $B\sim400$ nT, core reactance $Z$, and $\Gamma_{sagnac}\approx1836$ **asserted** as the baryon-phase shear factor, not derived). Result is ~$1.5\times10^{23}$ vs empirical $8.0\times10^{22}$ — a ~2× order-of-magnitude match, correctly flagged as not precision. The Venus/Mars "natural failures" are qualitative. This is a sketch with plausible support, not a closed derivation.
- strengthen-by:
  - Derive $\Gamma_{sagnac} = \mu_B \approx 1836$ from substrate primitives rather than asserting the proton/electron-mass-ratio identification.
  - Reduce the ~2× discrepancy by deriving (not plugging) $B_{stator}$ and the core impedance.

---

## Sonoluminescence as Tabletop Relativity
<!-- id: clm-91adfe -->

- $\rho_{eff} = \rho_0 / (1 - \mathrm{M}^2)^{3/2}$, Mach number $\mathrm{M} = |\dot{R}|/c_{sound}$
- _Specific Claims_
  - The Rayleigh-Plesset bubble-collapse equation with $\rho_0 \to \rho_{eff}$ (Axiom 4 saturation in the acoustic medium) autonomously halts before $R = 0$ via the Mach $\to 1$ topological wall.
  - The $3/2$ exponent (vs the standard $1/2$ Lorentz factor) arises from longitudinal inertia in 3D spherical collapse.
  - This is presented as an **acoustic emulation** of Special Relativity, not literal SR — Axiom 4 has the same structural form across acoustic / EM / gravitational media.
- _Specific Non-Claims and Caveats_
  - Does NOT claim sonoluminescence experimentally validates Special Relativity. The mapping is structural (same kernel form), not phenomenological.
  - Pure-vapor "bubble interior emulates a black-hole transition" is a Regime-III→IV identification at the acoustic scale; does NOT claim physically equivalent thermodynamics or that the bubble core is a literal BH analog beyond the saturation operator.
  - Flash temperatures vary with payload gas (ionization-energy gated); the table gives ranges, not point predictions.

> **Leaf references:** [sonoluminescence-derivation](./applied-physics/ch14-sonoluminescence/sonoluminescence-derivation.md).

### Quality
- confidence: 0.8
- depends-on:
  - Axiom 4 (Universal Saturation Kernel — acoustic-medium $\rho_{eff}$)
  - `clm-gz7ryg` (common: A-034 single-kernel unification, solidity X)
- solidity: 0.62 (use as input only, don't build deeper) [= min(0.80, 0.62)]
- rationale: The saturated Rayleigh-Plesset ODE with $\rho_{eff} = \rho_0/(1-M^2)^{3/2}$ closes as a well-posed substitution into the classical equation, and the Mach→1 topological wall (autonomous halt before $R=0$) follows directly from $\rho_{eff}\to\infty$. The framing as acoustic *emulation* of SR (not literal SR) is honest. Band held below 0.9 because the $3/2$ exponent is asserted from "longitudinal inertia in 3D spherical collapse" without an explicit derivation in the leaf, and flash temperatures are tabulated ranges (ionization-gated), not point predictions.
- strengthen-by:
  - Derive the $3/2$ exponent (vs Lorentz $1/2$) from the 3D spherical inertia explicitly.
  - Show the ODE-halt radius as a function of drive amplitude rather than asserting "before $R=0$."

---

## Superconductor Type Classification ($\kappa = \lambda_L/\xi_0$)
<!-- id: clm-qky559 -->

See cross-cutting [BCS Critical Field $B_c(T)$](../claim-quality.md) for the $B_c(T)$ axiom-manifestation tripwire. Vol3-specific aspects:

- $\kappa < 1/\sqrt{2}$: Type I (uniform $\mu \to 0$); $\kappa > 1/\sqrt{2}$: Type II (vortex lattice)
- _Specific Claims_
  - The Ginzburg-Landau $\kappa$ classification is reproduced; AVE re-interprets Type I as **uniform** Regime IV and Type II as **localized** Regime IV vortices (Abrikosov flux tubes), with inter-vortex regions remaining in Regime I.
  - Numerical validation against four materials (Al, Pb, Nb, MgB$_2$) — $B_c(T)$ matches to 0.0000% (axiom manifestation, see cross-cutting); $\lambda_L$ and $\xi_0$ from the catalog formulas have material-dependent errors.
- _Specific Non-Claims and Caveats_
  - The $\lambda_L$ catalog uses **free-electron $n_s$** estimates, which are wrong for d-band metals like Nb. LIVING_REFERENCE.md Pitfall #6: this misclassifies Nb as Type I ($\kappa = 0.172$) when corrected $n_s$ from measured $\lambda_L = 39$ nm yields $\kappa \approx 1.0$ (Type II, matching experiment).
  - Treat the Nb classification in the catalog as a **catalog limitation**, not an operator failure. The published table marks Nb's classification with $\times$ to flag this.
  - Lead's $\xi_0^{AVE} = 284$ nm vs $\xi_0^{exp} = 83$ nm is a $3.4\times$ overestimate — the coherence-length predictions are not sub-percent.
  - The Kuramoto phase-locking framework is presented as an **alternative** to BCS Cooper-pair condensation, not as its derivation. AVE asserts classical synchronisation produces the same $R = 0$ phenomenology; the equivalence with BCS macroscopic quantum coherence is a structural identification, not an experimental discrimination.

> **Leaf references:** [bcs-alternative-framework](./condensed-matter/ch09-condensed-matter-superconductivity/bcs-alternative-framework.md), [critical-field-validation](./condensed-matter/ch09-condensed-matter-superconductivity/critical-field-validation.md), [inertial-london-penetration-depth](./condensed-matter/ch09-condensed-matter-superconductivity/inertial-london-penetration-depth.md), [kuramoto-phase-locking](./condensed-matter/ch09-condensed-matter-superconductivity/kuramoto-phase-locking.md), [meissner-gear-train](./condensed-matter/ch09-condensed-matter-superconductivity/meissner-gear-train.md), [superconductor-catalog-predictions](./condensed-matter/ch09-condensed-matter-superconductivity/superconductor-catalog-predictions.md), [superconductor-type-classification](./condensed-matter/ch09-condensed-matter-superconductivity/superconductor-type-classification.md), [universal-saturation-operator](./condensed-matter/ch09-condensed-matter-superconductivity/universal-saturation-operator.md).

### Quality
- confidence: 0.7
- depends-on:
  - Axiom 4 (Universal Saturation Kernel — $\mu_{eff}\to0$ Regime IV)
  - `clm-gdd70j` (Vol 1 universal operators $Z,S,\Gamma$, solidity X)
  - `clm-gz7ryg` (common: A-034 single-kernel unification, solidity X)
- solidity: 0.62 (use as input only, don't build deeper) [= min(0.70, 0.62)]
- rationale: The GL $\kappa = \lambda_L/\xi_0$ classification ($1/\sqrt2$ threshold) is reproduced and reinterpreted (Type I = uniform Regime IV, Type II = localized vortex Regime IV) cleanly; $B_c(T)$ matches to 0.0000% (an axiom manifestation, flagged cross-cutting). Band held at disclosed-bound because the leaf openly documents that the $\lambda_L$ catalog uses free-electron $n_s$ (mis-classifying Nb), Pb's $\xi_0$ is a 3.4× overestimate, and the Kuramoto-vs-BCS equivalence is a structural identification, not an experimental discrimination. Derivation closes given the disclosed catalog limitations.
- strengthen-by:
  - Use measured $n_s$ (or derive d-band $n_s$ from AVE) so the catalog classifies Nb as Type II without the manual $\times$ override.
  - Derive $\xi_0$ from primitives to remove the 3.4× Pb overestimate.

---

## Effective Degrees of Freedom $g_* = 343/4 = 85.75$
<!-- id: clm-uu6dl5 -->

- $g_* = n^3/N_{K4} = 7^3/4 = 85.75$
- _Specific Claims_
  - The lattice-derived effective DoF replaces SM $g_{*,SM} = 106.75$. With $g_* = 85.75$, the baryon asymmetry formula yields $\eta = 6.08 \times 10^{-10}$ vs observed $6.1 \times 10^{-10}$ (0.38% error).
  - Using $g_{*,SM} = 106.75$ in the same formula yields 20% error, asserted as evidence that the lattice count is the correct DoF count for cosmological thermodynamics.
- _Specific Non-Claims and Caveats_
  - Does NOT claim the SM particle catalog is wrong — claims that the **DoF-counting metric for cosmological partition** uses lattice modes (7 compliance × $7^2$ angular sectors / 4 K4 cell) rather than particle species count.
  - The 0.38% baryon asymmetry agreement uses $g_* = 85.75$ together with $\alpha_W^4$, $C_{sph} = 28/79$, and $\kappa_{FS} = 8\pi$ — a multi-factor formula with several lattice-derived inputs. Treat the 0.38% as a composite consistency check, not a single-quantity prediction.
  - Does NOT claim $g_* = 85.75$ is a separately measurable cosmological observable; the validation is via the downstream baryon ratio.

> **Leaf references:** [baryon-asymmetry-derivation](./condensed-matter/ch11-thermodynamics/baryon-asymmetry-derivation.md), [baryon-asymmetry](./condensed-matter/ch11-thermodynamics/baryon-asymmetry.md), [effective-dof-g-star](./condensed-matter/ch11-thermodynamics/effective-dof-g-star.md), [mode-counting-heat-capacity](./condensed-matter/ch11-thermodynamics/mode-counting-heat-capacity.md), [thermal-softening-correction](./condensed-matter/ch11-thermodynamics/thermal-softening-correction.md), [thermal-softening-skyrme](./condensed-matter/ch11-thermodynamics/thermal-softening-skyrme.md), [vacuum-heat-capacity](./condensed-matter/ch11-thermodynamics/vacuum-heat-capacity.md).

### Quality
- confidence: 0.7
- depends-on:
  - Axiom 1 (Substrate Topology — K4 lattice / $N_{K4} = 4$)
  - `clm-iouqn9` (common: K4 $|T| = 12$ / magic-angle geometry, solidity X)
  - `clm-4vwsjc` (Vol 2 baryon asymmetry $\eta$, solidity X)
- solidity: 0.40 (do not build on, rework needed) [= min(0.70, 0.40)]
- rationale: $g_* = n^3/N_{K4} = 7^3/4 = 85.75$ is clean lattice mode-counting (7 compliance × $7^2$ angular / 4 K4 cell). The leaf is a single resultbox; the validation is the downstream $\eta = 6.08\times10^{-10}$ (0.38%), which the entry honestly flags as a **composite multi-factor formula** ($\alpha_W^4$, $C_{sph} = 28/79$, $\kappa_{FS} = 8\pi$, $g_*$). The mode-count itself closes cleanly given the K4 geometry; band held at disclosed-bound because $g_*$ is not separately measurable and rides on the composite baryon validation.
- strengthen-by:
  - Justify the $7^3$ ($n^3$) angular-sector count from the compliance manifold in this leaf rather than the companion mode-counting leaf.
  - Isolate $g_*$'s contribution to $\eta$ from the other lattice-derived factors.

---

## Kolmogorov Spectral Cutoff and Bounded Enstrophy
<!-- id: clm-hk81zp -->

- $k_{\max} = \pi/\ell_{node}$; $E(k) = C_K \varepsilon^{2/3} k^{-5/3} S(k/k_{\max})$; $n_{3D} = 38/21$
- _Specific Claims_
  - The lattice pitch sets a hard wavenumber ceiling; the Axiom 4 saturation envelope rolls the inertial spectrum smoothly to zero before the cutoff.
  - The 3D avalanche exponent $n_{3D} = 2(1 - \nu_{vac}/3) = 38/21 \approx 1.8095$ — within $\sim 0.5\%$ of empirical solar-flare measurements.
  - On a finite discrete lattice, total enstrophy is rigorously bounded by $Z_{max} = 2Nc^2 \, dx$ — claimed as a **constructive resolution** of Navier-Stokes global regularity within the AVE discrete framework.
- _Specific Non-Claims and Caveats_
  - Does NOT claim a Clay-rigorous proof of Navier-Stokes regularity in the continuum. The claim is **lattice-conditional**: bounded on any finite discrete lattice, by virtue of the lattice cutoff itself. See LIVING_REFERENCE.md Master Prediction Table notes #14, #15 for Yang-Mills and NS framework-derived (not Clay-rigorous) caveats — same caveat applies here.
  - Does NOT claim $n_{3D} = 38/21$ is the universal turbulence exponent; the agreement is with solar-flare avalanche statistics specifically, and the comparison is to "$\sim 1.8$" (single empirical figure), not a precision dataset.
  - The Kolmogorov constant $C_K = 1.5$ is the classical empirical value; the framework asserts compatibility, not a new derivation.

> **Leaf references:** [kolmogorov-spectral-cutoff](./condensed-matter/ch11-thermodynamics/kolmogorov-spectral-cutoff.md).

### Quality
- confidence: 0.6
- depends-on:
  - Axiom 1 (Substrate Topology — lattice pitch $\ell_{node}$ Nyquist cutoff)
  - Axiom 3 (Minimum Reflection Principle)
  - Axiom 4 (Universal Saturation Kernel — spectral envelope $S$)
  - `clm-iouqn9` (common: $\nu_{vac} = 2/7$, solidity X)
- solidity: 0.55 (use as input only, don't build deeper) [= min(0.60, 0.55)]
- rationale: Three results each close cleanly: $k_{max} = \pi/\ell_{node}$ (Nyquist), $n_{3D} = 2(1-\nu_{vac}/3) = 38/21$ (from the $1D$ value 2 leaking via Poisson), and bounded enstrophy $Z_{max} = 2Nc^2dx$ (from max gradient $2c/dx$). The leaf is explicit that this is **lattice-conditional**, NOT a Clay-rigorous continuum NS proof, and that $C_K = 1.5$ is the imported classical constant; the $n_{3D}$ comparison is to "$\sim1.8$" (single solar-flare figure). Disclosed methodology bound — the closure rests on the lattice cutoff itself and an imported constant.
- strengthen-by:
  - State the continuum limit explicitly and bound the gap between the lattice-conditional bound and the Clay continuum problem.
  - Compare $n_{3D} = 38/21$ against a precision turbulence dataset rather than a single "$\sim1.8$".

---

## Per-Element Impedance Table (Two Families)
<!-- id: clm-nxfmh0 -->

- _Specific Claims_
  - Diagonalising the nuclear Hessian for Z = 1–14 yields a binary partition: closed-shell alpha cores ($Z_{atom} \approx 1.37$, $Q = 2.0$, $E_{rupt} \approx 0.82$ MeV) vs open-shell halo elements ($Z_{atom} \sim 0.37$–$0.46$, $Q = 3$–$16$, $E_{rupt} \ll 0.82$).
  - The alpha-core family (He-4, C-12, O-16, Ne-20, Mg-24, Si-28) is structurally identified as built from tetrahedral alpha clusters; $Q = 2.0$ is the tetrahedral-symmetry signature.
  - Inter-element bonding via the same `reflection_coefficient(Z₁, Z₂)` operator: same-family $|\Gamma| \to 0$ (resonant), cross-family $|\Gamma| \sim 0.5$ (ionic).
- _Specific Non-Claims and Caveats_
  - Does NOT claim numerical match of $K_{bulk}$, $G_{shear}$, $E_{rupt}$ to experimental bulk-modulus / shear-modulus / rupture-energy values per element. The table lists eigenvalue **proxies** of the lattice Hessian, not direct experimental moduli.
  - The two-family classification is a structural / qualitative claim; cross-family $|\Gamma|$ being "ionic" is a structural identification, not a quantitative bonding-energy derivation.
  - Hydrogen-1 has no characterisation (single nucleon, no Hessian).

> **Leaf references:** [diamond-hardness-alpha-clusters](./condensed-matter/ch10-material-properties/diamond-hardness-alpha-clusters.md), [helium-metamaterial-paradox](./condensed-matter/ch10-material-properties/helium-metamaterial-paradox.md), [inter-element-reflection-coefficient](./condensed-matter/ch10-material-properties/inter-element-reflection-coefficient.md), [metallicity-magnetic-asymmetry](./condensed-matter/ch10-material-properties/metallicity-magnetic-asymmetry.md), [nuclear-hessian](./condensed-matter/ch10-material-properties/nuclear-hessian.md), [per-element-impedance-table](./condensed-matter/ch10-material-properties/per-element-impedance-table.md).

### Quality
- confidence: 0.7
- depends-on:
  - `clm-gdd70j` (Vol 1 universal operators / reflection coefficient, solidity X)
  - `clm-iouqn9` (common: $\nu_{vac} = 2/7$ — alpha-core $Q = 2$ tetrahedral signature, solidity X)
- solidity: 0.55 (use as input only, don't build deeper) [= min(0.70, 0.55)]
- rationale: The $3N\times3N$ Hessian eigendecomposition (Goldstone-mode removal, breathing/rocking/ejection classification) is a genuine numerical derivation, and the two-family partition (closed-shell alpha cores $Z_{atom}\approx1.37$, $Q=2$ vs open-shell halos) is a real structural result with an internally-consistent tetrahedral-symmetry rationale. Band held at disclosed-bound because the leaf is explicit that $K_{bulk}$, $G_{shear}$, $E_{rupt}$ are eigenvalue **proxies**, not experimental moduli, and the cross-family $|\Gamma|\sim0.5$ "ionic" identification is structural, not a quantitative bonding-energy derivation.
- strengthen-by:
  - Calibrate the eigenvalue proxies against experimental bulk/shear moduli for at least the alpha-core family.
  - Derive the $K_{mutual}/d$ energy functional's $K_{mutual}$ from AVE primitives rather than treating it as a fitted scale.

---

## Dirac Large Numbers and Planck Mass
<!-- id: clm-1klgo2 -->

- $\alpha_G = G m_e^2 / (\hbar c) = 1/(7\xi)$; $m_P = m_e\sqrt{7\xi}$; $R_H/\ell_{node} = \alpha^2/(28\pi\alpha_G)$
- _Specific Claims_
  - The Dirac Large Numbers Hypothesis ratio between cosmological and quantum scales is **algebraically derivable** from $G = \hbar c/(7\xi m_e^2)$ via direct substitution.
  - The Planck mass becomes $m_P = m_e\sqrt{7\xi}$ — recast as the electron rest mass scaled by the cosmological geometric coupling. The leaf interprets this as: the Planck scale is **not a fundamental microscopic threshold**; the discrete quantization limit is the electron mass-gap, $\ell_{node} = \hbar/(m_e c)$.
- _Specific Non-Claims and Caveats_
  - These derivations are **algebraic identities** within the AVE definition of $G$, not independent predictions. They follow from Axiom 3 by substitution.
  - Does NOT claim a measurement of the Planck mass at $m_e\sqrt{7\xi}$ as a novel prediction — both sides match because $\xi$ was defined to make this hold, given the empirical $G$.
  - "$\ell_{node}$ is the true quantization limit (not the Planck length)" is a **framework-internal interpretive** claim about which length scale is fundamental; it does not introduce new observables vs the standard Planck-length picture.

> **Leaf references:** [asymptotic-hubble-constant](./gravity/ch01-gravity-yield/asymptotic-hubble-constant.md), [gravitational-coupling-constant](./gravity/ch01-gravity-yield/gravitational-coupling-constant.md), [optical-refraction-gravity](./gravity/ch01-gravity-yield/optical-refraction-gravity.md), [planck-mass](./gravity/ch01-gravity-yield/planck-mass.md).

### Quality
- confidence: 1.0
- depends-on:
  - Axiom 2 (Topo-Kinematic Isomorphism — $\ell_{node} = \hbar/m_ec$ scale)
  - Axiom 3 (Minimum Reflection Principle — definition of $G$)
  - `clm-wx5324` (Vol 3 $H_\infty$ — same Machian-coupling geometric limit, solidity X)
- solidity: 0.55 (use as input only, don't build deeper) [= min(1.00, 0.55)]
- rationale: $G = c^4/(7\xi T_{EM})$ with $T_{EM} = m_ec^2/\ell_{node}$ and $\ell_{node} = \hbar/m_ec$ gives $G = \hbar c/(7\xi m_e^2)$, hence $\alpha_G = Gm_e^2/\hbar c = 1/(7\xi)$ and $m_P = m_e\sqrt{7\xi}$ — these are **pure algebraic identities by substitution** into the AVE definition of $G$, carrying zero predictive content (the leaf states this explicitly: "not independent predictions… both sides match because $\xi$ was defined to make this hold"). Definitional; no observation could falsify the substitution itself. Classification: identity.
- strengthen-by:
  - (Not applicable to local rigor — an identity is maximal at 1.0. Predictive content would require an independent derivation of $\xi$ or $G$, which is a separate claim.)

---

## JWST Exponential Accretion Time Constant $\tau_{ind} \approx 65.1$ Myr
<!-- id: clm-9fnieq -->

- $M(t) = M_{seed} e^{t/\tau_{ind}}$
- _Specific Claims_
  - The framework predicts an exponential mass-growth law from mutual-inductive accretion in the dense early-universe lattice, in contrast to $\Lambda$CDM's $M \propto t^{2.5}$.
  - This makes the JWST early-galaxy observations compatible with AVE without invoking modified initial conditions.
- _Specific Non-Claims and Caveats_
  - $\tau_{ind} \approx 65.1$ Myr is **fitted to the JWST data** (constrained by the requirement that $M$ grow from $10^{10} M_\odot$ at $t = 350$ Myr to $10^{11} M_\odot$ at $t = 500$ Myr). It is **not** an independent prediction from axioms.
  - The framework supplies the *form* (exponential), not the *time constant*. Treat $\tau_{ind} = 65.1$ Myr as a derived consequence of the form fit to two data points, not an axiom-derived numerical prediction.

> **Leaf references:** [jwst-constraint-equation](./cosmology/ch04-generative-cosmology/jwst-constraint-equation.md), [mutual-inductive-accretion-time-constant](./cosmology/ch04-generative-cosmology/mutual-inductive-accretion-time-constant.md).

### Quality
- confidence: 0.5
- depends-on:
  - Axiom 4 (Universal Saturation Kernel — mutual-inductive accretion regime)
- solidity: 0.50 (use as input only, don't build deeper) [= min(0.50, 1.00)]
- rationale: The framework supplies the **form** ($M = M_{seed}e^{t/\tau}$, from $dM/dt = \lambda M$ mutual-inductive drag) cleanly, but $\tau_{ind} \approx 65.1$ Myr is **fitted** to two JWST data points ($10^{10}M_\odot$ at 350 Myr, $10^{11}M_\odot$ at 500 Myr), as the leaf's own constraint equation $10 = e^{150/\tau}$ makes explicit. The exponential-vs-$\Lambda$CDM-$t^{2.5}$ contrast is the substantive content; the time constant is a two-point fit, not an axiom-derived number — substantive open dependency on the fit.
- strengthen-by:
  - Derive $\tau_{ind}$ (the primordial mutual-inductance time constant) from the early-universe lattice density and $\xi_{topo}$ rather than fitting it to JWST.
  - Add a third data point to test the exponential form independently of the two anchors.

---

## Phantom Energy Equation of State $w < -1$
<!-- id: clm-3ii690 -->

- $w_{vac} = -1 - \rho_{latent}/\rho_{vac}$
- _Specific Claims_
  - "Dark energy" is reinterpreted as the latent heat of continuous lattice crystallisation; positive $\rho_{latent}$ guarantees $w < -1$ (phantom regime).
  - The framework forbids the Big Rip singularity within this reinterpretation.
- _Specific Non-Claims and Caveats_
  - Does NOT claim a numerical value of $w_{vac}$ to compare with observational constraints (current data: $w \approx -1$ within $\sim 0.05$; phantom regime $w < -1$ is consistent but not required).
  - "Forbids Big Rip" is a framework-internal consequence of the latent-heat injection / asymptotic Unruh-Hawking attractor; it is an interpretive prediction, not a quantitative bound on $w$ time-evolution.
  - The CMB asymptotic-attractor picture (radiation density floors at $\frac{3}{4}\rho_{latent}$, asymptoting to Unruh-Hawking $\sim 10^{-30}$ K) is structural, not numerically validated against observation.

> **Leaf references:** [cmb-thermal-attractor](./cosmology/ch04-generative-cosmology/cmb-thermal-attractor.md), [phantom-energy-equation-of-state](./cosmology/ch04-generative-cosmology/phantom-energy-equation-of-state.md).

### Quality
- confidence: 0.7
- depends-on:
  - Axiom 4 (Universal Saturation Kernel — latent-heat / crystallisation regime)
  - `clm-wx5324` (Vol 3 $H_\infty$ / crystallisation rate, solidity X)
- solidity: 0.55 (use as input only, don't build deeper) [= min(0.70, 0.55)]
- rationale: $w_{vac} = -1 - \rho_{latent}/\rho_{vac}$ follows from a first-law argument (latent heat $\rho_{latent}dV$ expelled while funding new-volume internal energy → strictly negative total pressure), and positive $\rho_{latent}$ then guarantees $w < -1$ cleanly. Band held at disclosed-bound because the leaf gives **no numerical $w$** to compare against the $w\approx-1\pm0.05$ data, and "forbids Big Rip" / the CMB asymptotic-attractor floor are interpretive consequences, not quantitative bounds on $w(t)$. The sign argument closes; the magnitude and Big-Rip claims rest on the disclosed latent-heat picture.
- strengthen-by:
  - Derive $\rho_{latent}/\rho_{vac}$ numerically (from crystallisation energetics) to give a falsifiable $w$ value.
  - Show the Big-Rip-forbidding bound on $w(t)$ as a quantitative time-evolution, not a verbal attractor argument.

---

## Einstein Field Equation Reinterpretation
<!-- id: clm-y9old1 -->

- $R_{\mu\nu} - \tfrac{1}{2}R g_{\mu\nu} + \Lambda g_{\mu\nu} = (8\pi G/c^4) T_{\mu\nu}$ with $T_{\mu\nu} \equiv U_{\mu\nu}$ (LC EM energy density)
- _Specific Claims_
  - AVE identifies the GR stress-energy tensor with the local LC vacuum's classical electromagnetic energy density and the metric tensor with the impedance moduli ($\varepsilon_{eff}, \mu_{eff}$).
  - This is presented as an **ontological reinterpretation** (variable scalar capacitance/inductance of a structured dielectric superfluid), not as new field equations.
  - The Schwarzschild radius $r_s$ is identified as the saturation impedance boundary where $\mu_{eff}, \varepsilon_{eff} \to 0$ — but note the cross-cutting Symmetric Saturation result: under symmetric scaling $Z = Z_0$ everywhere; "$Z \to 0$ at the horizon" is a different gauge / interpretation choice that needs care to reconcile.
- _Specific Non-Claims and Caveats_
  - Does NOT claim derivation of the Einstein equation from AVE axioms ab initio. The reinterpretation maps the **same** equation onto LC quantities; it does not produce modified field equations.
  - There is interpretive tension between "Symmetric Gravity → $Z = Z_0$ invariant" (GW propagation leaves) and "$Z \to 0$ at the horizon" (Einstein-equation leaf). The two coexist: the impedance is invariant for **transverse** propagation while the **constitutive** $\mu_{eff}, \varepsilon_{eff}$ collapse to zero at saturation. Summaries that quote one without the other create apparent contradictions.

> **Leaf references:** [einstein-field-equation](./gravity/ch02-general-relativity/einstein-field-equation.md), [stress-energy-lc-density](./gravity/ch02-general-relativity/stress-energy-lc-density.md).

### Quality
- confidence: 0.7
- depends-on:
  - Axiom 3 (Minimum Reflection Principle)
  - Axiom 4 (Universal Saturation Kernel — $\mu_{eff},\varepsilon_{eff}\to0$ at $r_s$)
  - `clm-07kd5v` (Vol 3 symmetric impedance $Z = Z_0$, solidity X)
  - `clm-rd9cjm` (Vol 3 refractive index $n(r)$, solidity X)
- solidity: 0.55 (use as input only, don't build deeper) [= min(0.70, 0.55)]
- rationale: This is explicitly an **ontological reinterpretation** ($T_{\mu\nu}\equiv U_{\mu\nu}$ LC energy density; $g_{\mu\nu}\leftrightarrow\varepsilon_{eff},\mu_{eff}$), NOT a derivation of the Einstein equation ab initio nor modified field equations — the leaf states this. The mapping is internally consistent and the apparent "$Z=Z_0$ invariant" vs "$Z\to0$ at horizon" tension is explicitly surfaced and reconciled (transverse impedance invariant while constitutive $\mu,\varepsilon$ collapse). The reinterpretation closes as a consistent identification; band at disclosed-bound because it imports the standard EFE rather than deriving it.
- strengthen-by:
  - Derive (even schematically) the EFE from the LC Lagrangian rather than mapping onto the existing equation.
  - Make the constitutive-collapse vs transverse-invariance reconciliation a worked calculation, not a prose statement, to fully retire the cross-leaf tension.

---

## Seismic Reflection Coefficient (Moho)
<!-- id: clm-zsqh87 -->

- $\Gamma_{Moho} = (\rho_2 V_{p2} - \rho_1 V_{p1})/(\rho_2 V_{p2} + \rho_1 V_{p1}) \approx 0.29$
- _Specific Claims_
  - The seismic Moho reflection uses **the same** `reflection_coefficient(Z₁, Z₂)` operator as Pauli exclusion, plasma cutoff, superconductor boundary, and antenna $S_{11}$ — a category (i) operator-identity claim across scales.
- _Specific Non-Claims and Caveats_
  - Does NOT claim the value $\Gamma \approx 0.29$ is AVE-derived. The inputs $\rho_i, V_{pi}$ are seismological measurements; AVE asserts the **operator form** is the same one used elsewhere, not a novel numerical derivation.
  - The cross-scale operator unity is structural (same formula reused), not a prediction at any single scale.

> **Leaf references:** [constitutive-mapping](./applied-physics/ch13-geophysics/constitutive-mapping.md), [prem-layers-waveguide](./applied-physics/ch13-geophysics/prem-layers-waveguide.md), [seismic-fdtd-engine](./applied-physics/ch13-geophysics/seismic-fdtd-engine.md), [seismic-reflection-coefficient-moho](./applied-physics/ch13-geophysics/seismic-reflection-coefficient-moho.md).

### Quality
- confidence: 1.0
- depends-on:
  - Axiom 3 (Minimum Reflection Principle — reflection-coefficient operator)
  - `clm-gdd70j` (Vol 1 universal operators $Z,S,\Gamma$, solidity X)
- solidity: 0.80 (ok to build on, see caveats) [= min(1.00, 0.80)]
- rationale: $\Gamma_{Moho} = (\rho_2V_{p2} - \rho_1V_{p1})/(\rho_2V_{p2} + \rho_1V_{p1})$ is the standard impedance-mismatch reflection coefficient — the leaf's claim is the **operator-identity**: the same `reflection_coefficient(Z_1,Z_2)` used for Pauli exclusion, plasma cutoff, superconductor boundary, and antenna $S_{11}$. The inputs $\rho_i,V_{pi}$ are seismological measurements and the leaf does not claim $\Gamma\approx0.29$ is AVE-derived. As an operator-reuse identity (true by the operator's definition), this is category-(i)/definitional.
- strengthen-by:
  - (Not applicable to local rigor of the identity itself; the operator-reuse claim is maximal. A *predictive* version would derive a seismic discontinuity location from AVE primitives rather than plugging measured moduli.)

---

## Ideal Gas Law as LC Energy Balance
<!-- id: clm-cul4it -->

- $U \cdot V = N \cdot k_B \cdot \overline{T_{jitter}}$ → recovers $PV = nRT$ at STP
- _Specific Claims_
  - The classical ideal gas law is reinterpreted as an LC energy-balance equation; gas pressure becomes an electromagnetic-jitter (lattice noise) phenomenon at the molecular scale.
- _Specific Non-Claims and Caveats_
  - Does NOT claim a corrected ideal gas law that deviates from $PV = nRT$. The framework reproduces the standard formula at STP — a category (iii) consistency check via reinterpreted variables.
  - The mapping introduces no new measurable predictions at the macroscopic gas-law level; deviations would appear (if at all) only in regimes where lattice-noise structure becomes resolvable.

> **Leaf references:** [gas-dynamics-foundations](./applied-physics/ch12-ideal-gas-law/gas-dynamics-foundations.md), [ideal-gas-law](./applied-physics/ch12-ideal-gas-law/ideal-gas-law.md), [lc-energy-balance-equation](./applied-physics/ch12-ideal-gas-law/lc-energy-balance-equation.md), [recovering-r-at-stp](./applied-physics/ch12-ideal-gas-law/recovering-r-at-stp.md).

### Quality
- confidence: 0.7
- depends-on:
  - `clm-gdd70j` (Vol 1 universal operators — LC energy balance, solidity X)
- solidity: 0.70 (ok to build on, see caveats) [= min(0.70, 0.80)]
- rationale: $U\cdot V = Nk_B\overline{T_{jitter}}$ → $PV = nRT$ at STP is a reinterpretation (pressure as EM-jitter/lattice-noise) that recovers the standard law — a category-(iii) consistency check via reinterpreted variables, with **no** new measurable macroscopic prediction (the leaf is a single resultbox stating $PV = nRT$). The mapping is internally consistent; band at disclosed-bound because the recovery of $R$ at STP imports the standard thermodynamic identification and the ontological content is verbal, not a closed numerical derivation of $R$ from primitives.
- strengthen-by:
  - Derive the gas constant $R$ (or $k_B$) from the lattice-noise spectral density rather than recovering it at STP.
  - Identify the regime where lattice-noise structure makes $PV=nRT$ deviate, giving a falsifiable prediction.

---

## Neutrino MSW Matter Potential
<!-- id: clm-o6kgkz -->

- $V_{CC} = \sqrt{2}\, G_F\, n_e$
- _Specific Claims_
  - The standard MSW charged-current matter potential is reproduced from AVE-derived $G_F$ (3.9% accurate per LIVING_REFERENCE.md and Master Prediction Table #13 at 2.09%).
- _Specific Non-Claims and Caveats_
  - Does NOT claim a novel matter-potential formula. The leaf reproduces the SM expression; the AVE input is the value of $G_F$, not the form of the potential.
  - LIVING_REFERENCE.md Critical Distinctions #5 caveat applies: SPICE RC muon model is qualitative; quantitative neutrino-related lifetimes go through the standard Fermi formula with AVE $G_F$.
  - The flavor-mixing energy-dependent table (pp / $^7$Be / $^8$B) reports agreement with Borexino/SNO; treat as consistency with the SM-MSW prediction using AVE $G_F$, not as an independent AVE-only validation.

> **Leaf references:** [msw-resonance-critical-density](./applied-physics/ch07-stellar-interiors/msw-resonance-critical-density.md), [neutrino-flavor-mixing](./applied-physics/ch07-stellar-interiors/neutrino-flavor-mixing.md), [neutrino-msw-matter-potential](./applied-physics/ch07-stellar-interiors/neutrino-msw-matter-potential.md), [stellar-interior-impedance-profiles](./applied-physics/ch07-stellar-interiors/stellar-interior-impedance-profiles.md), [stellar-regime-classification](./applied-physics/ch07-stellar-interiors/stellar-regime-classification.md).

### Quality
- confidence: 0.7
- depends-on:
  - `clm-gdd70j` (Vol 1 universal operators $Z,S,\Gamma$ — reflection coefficient, solidity X)
- solidity: 0.70 (ok to build on, see caveats) [= min(0.70, 0.80)]
- rationale: $V_{CC} = \sqrt2 G_F n_e$ is the **standard SM MSW charged-current potential**, reproduced verbatim; the AVE contribution is the value of $G_F$ (derived elsewhere, ~2–4% per Master Prediction Table #13), not the form of the potential. The leaf is a single resultbox; the flavor-mixing validation against Borexino/SNO is consistency with the SM-MSW prediction using AVE $G_F$. Disclosed import bound — the derivation closes only by importing the SM potential form and an externally-derived $G_F$.
- strengthen-by:
  - Cite/carry the AVE $G_F$ derivation as an explicit dependency once its Vol 2/Vol 7 claim-id is pinned (currently referenced via Master Prediction Table, not a clm-id in this footer).
  - Show whether the AVE substrate modifies the potential's *form* (vs only its $G_F$ input) in any regime.

---

## Thermodynamics as LC Mechanics — Temperature, Entropy, Arrow of Time
<!-- id: clm-t05mvx -->

- $T \propto \langle U_{noise} \rangle = \langle \tfrac{1}{2}\varepsilon_0 |\mathbf{E}|^2 + \tfrac{1}{2}\mu_0 |\mathbf{H}|^2 \rangle = \tfrac{3}{2} k_B T$; entropy = irreversibility of spherical FDTD radiation
- _Specific Claims_
  - Macroscopic temperature is **defined** in the framework as the RMS displacement-current jitter of the LC vacuum grid. The RHS recovers the standard equipartition $\tfrac{3}{2} k_B T$ — a category (iii) consistency check (alternate ontology, same scalar).
  - Entropy is reinterpreted as the geometric impossibility of reversing spherical wave radiation on a Cartesian grid: a coherent local source spreads its energy across $4\pi r^2$ nodes, and reversal would require synchronous reflective convergence whose probability is "effectively zero". The Second Law is therefore an FDTD propagation property, not a statistical postulate over microstates.
  - The Arrow of Time is identified with this same one-way property of outward spherical radiation through the LC mesh.
- _Specific Non-Claims and Caveats_
  - Does NOT claim a quantitative correction to the equipartition theorem or to thermodynamic state functions. The macroscopic predictions agree with classical thermodynamics; the contribution is ontological, not numerical.
  - "Probability of geometric reversal is effectively zero" is a structural / verbal argument; the leaf does not produce a quantitative bound on entropy decrease analogous to a fluctuation theorem.
  - Does NOT claim to derive the Boltzmann constant $k_B$ from first principles; $k_B$ enters as the standard scaling constant linking macroscopic noise energy to a temperature scale.
  - The "spherical wave on a Cartesian grid" framing is a continuum analogue; for the discrete K4 lattice the same conclusion is asserted but is not separately worked out leaf-by-leaf.

> **Leaf references:** [arrow-of-time](./condensed-matter/ch11-thermodynamics/arrow-of-time.md), [entropy-redefinition](./condensed-matter/ch11-thermodynamics/entropy-redefinition.md), [macroscopic-temperature-lc-noise](./condensed-matter/ch11-thermodynamics/macroscopic-temperature-lc-noise.md).

### Quality
- confidence: 0.7
- depends-on:
  - `clm-gdd70j` (Vol 1 universal operators $Z,S,\Gamma$, solidity X)
- solidity: 0.70 (ok to build on, see caveats) [= min(0.70, 0.80)]
- rationale: $T\propto\langle U_{noise}\rangle = \langle\tfrac12\varepsilon_0|E|^2 + \tfrac12\mu_0|H|^2\rangle = \tfrac32 k_BT$ recovers equipartition exactly — a category-(iii) consistency check (alternate ontology, same scalar). The entropy reinterpretation (geometric irreversibility of spherical FDTD radiation on a Cartesian grid) and the Arrow-of-Time identification are structural/verbal arguments; the leaf does **not** produce a quantitative entropy-decrease bound (no fluctuation-theorem analogue) and does not derive $k_B$. Disclosed-bound: the temperature identity closes, the entropy/arrow content is asserted-structural and the discrete-K4 version is not separately worked out.
- strengthen-by:
  - Produce a quantitative bound on entropy-reversal probability (fluctuation-theorem-style) rather than "effectively zero."
  - Work the spherical-wave-irreversibility argument on the discrete K4 lattice explicitly, not only the continuum analogue.

---

## Phase Transitions as Impedance Matching Events
<!-- id: clm-refjr6 -->

- Solid$\to$liquid: $Z_{shear} \to 0$; normal$\to$superconducting: $Z_{eff} \to 0$, $|\Gamma| \to 1$; paramagnetic$\to$ferromagnetic: $Z_\mu \to 0$ locally; BEC: $|\Gamma| \to 1$ globally; deconfinement: $Z_{int} \to Z_0$. Casimir cooling: $T_{eff} = T_{ambient}\sqrt{1 - (f_c/f_{max})^2}$ with $f_c = c_0/(2d)$.
- _Specific Claims_
  - All classical phase transitions are reinterpreted as abrupt changes in the local LC reflection/transmission coefficients. The critical temperature $T_c$ is the point at which RMS thermal noise crosses the impedance-mismatch threshold required to maintain (or break) a particular structural resonance.
  - The superconducting transition specifically is identified with the Kuramoto order parameter going from $R \approx 0$ to $R = 1$, equivalently $Z_{eff} \to 0$, $|\Gamma| \to 1$, and $\mu_{eff} \to 0$ (Axiom 4 saturation in the magnetic sector — the same kernel that governs plasma E-field expulsion).
  - The Casimir formula gives an explicit prediction: a conductor inside a nanoscale cavity of gap $d$ experiences a high-pass filter on the ambient noise spectrum, and when $T_{eff} < T_c$ the conductor undergoes a *geometric* phase transition into the superconducting state at room ambient temperature. Stated as a falsifiable engineering claim about cavity-induced superconductivity.
- _Specific Non-Claims and Caveats_
  - Does NOT claim novel critical temperatures for any of the listed transitions; the framework reproduces the standard $T_c$ values via reinterpretation, not by predicting them ab initio.
  - "Casimir cooling drives a conductor superconducting at room temperature" is a strong falsifiable claim — to date there is no experimental confirmation of geometric-phase-transition superconductivity at room ambient via this mechanism. Treat as an engineering proposal, not a confirmed result.
  - The mapping from each transition to an impedance change is structural; magnitudes (e.g., the rate at which $Z_{shear} \to 0$ during melting) are not derived per transition.
  - The BEC and deconfinement entries are descriptive identifications, not independent quantitative derivations of condensation temperature or deconfinement scale.

> **Leaf references:** [casimir-effective-temperature](./condensed-matter/ch11-thermodynamics/casimir-effective-temperature.md), [phase-transition-classification](./condensed-matter/ch11-thermodynamics/phase-transition-classification.md), [phase-transitions-impedance](./condensed-matter/ch11-thermodynamics/phase-transitions-impedance.md).

### Quality
- confidence: 0.5
- depends-on:
  - Axiom 4 (Universal Saturation Kernel — $\mu_{eff}\to0$ at $T_c$)
  - `clm-gdd70j` (Vol 1 universal operators $Z,S,\Gamma$, solidity X)
- solidity: 0.50 (use as input only, don't build deeper) [= min(0.50, 0.80)]
- rationale: The mappings (solid→liquid $Z_{shear}\to0$; normal→SC $Z_{eff}\to0$, $|\Gamma|\to1$; ferromagnetic $Z_\mu\to0$; BEC $|\Gamma|\to1$; deconfinement $Z_{int}\to Z_0$) are **structural reinterpretations** with no per-transition magnitudes derived (the leaf states "magnitudes… are not derived per transition"). The Casimir $T_{eff} = T_{ambient}\sqrt{1-(f_c/f_{max})^2}$ with $f_c = c_0/2d$ is a concrete formula but the room-temperature-superconductivity-via-cavity claim is a strong, **falsifiable but experimentally unconfirmed** engineering proposal. Substantive open dependency — the central new prediction is asserted, not closed or validated.
- strengthen-by:
  - Derive the rate at which each $Z\to0$ during its transition (currently only the endpoints are given).
  - Provide a quantitative Casimir-cavity geometry that drives a named conductor below its $T_c$, with a testable predicted gap $d$.

---

## Vacuum Nyquist Baseline and Boundary Thermalization
<!-- id: clm-eaiqj1 -->

- $\langle V^2_{vac}(f) \rangle = 4 k_B T \, Z_0 \, \Delta f$; thermal noise enters via boundary impedance mismatches, not bulk injection
- _Specific Claims_
  - The Johnson-Nyquist relation is applied **literally** to the LC vacuum: at temperature $T$, the vacuum baseline noise spectral density is $4 k_B T Z_0 \Delta f$ with $Z_0 \approx 376.73\;\Omega$ as the lattice's characteristic impedance. The framework asserts this is not an analogy: the lattice *is* a transmission line.
  - "Boundary-impedance thermalization": a topological structure with internal impedance $Z_{int}$ embedded in the lattice couples to the ambient $T$-bath only through its boundary nodes via $\Gamma = (Z_0 - Z_{int})/(Z_0 + Z_{int})$. The transmitted noise power is $4 Z_0 Z_{int}/(Z_0 + Z_{int})^2$ times the incident; bulk interior of a well-matched structure remains thermally quiet.
  - For a transmon qubit, this means stochastic noise must be injected only at the lead boundaries (where the junction impedance meets the cryogenic feedline), not uniformly across the bulk field. The simulation produces a Cauchy-Schwarz overlap $C(t)$ that decays via oscillatory relaxation, reproducing observed cryo-cooled qubit error timelines.
  - Fluctuation-Dissipation balance is closed by the Ohmic damping $\gamma = (Z_0/2)/(\omega_0 L_{eff})$ on each standing-wave mode, with dissipation rate $P_{diss} = \langle V^2 \rangle/(4R) = k_B T \Delta f$ matching the Nyquist injection.
- _Specific Non-Claims and Caveats_
  - Does NOT claim the Nyquist formula is derived from new principles; it is **applied** to the lattice substrate via the structural identification $Z_0 = \sqrt{\mu_0/\varepsilon_0}$. The lattice ontology is the new content; the relation itself is the standard FDT.
  - The transmon coherence model is qualitative: the leaf states the simulation reproduces "observed error-rate timelines" but does not give a per-device quantitative prediction (e.g., $T_1$ in microseconds for a specific transmon design).
  - Does NOT claim the boundary-only injection prescription is the unique correct prescription for all decoherence sources — explicitly scoped to thermal noise from the room-temperature reservoir entering through impedance mismatches.
  - The FDT closure ($P_{noise,in} = P_{Ohmic,out}$) is asserted as a structural balance; it is not derived as a per-mode equilibrium calculation in this leaf.

> **Leaf references:** [nyquist-noise-fdt](./condensed-matter/ch11-thermodynamics/nyquist-noise-fdt.md), [transmon-decoherence](./condensed-matter/ch11-thermodynamics/transmon-decoherence.md), [vacuum-nyquist-baseline](./condensed-matter/ch11-thermodynamics/vacuum-nyquist-baseline.md).

### Quality
- confidence: 0.7
- depends-on:
  - `clm-gdd70j` (Vol 1 universal operators $Z,S,\Gamma$ — reflection coefficient $\Gamma$, solidity X)
- solidity: 0.70 (ok to build on, see caveats) [= min(0.70, 0.80)]
- rationale: The Johnson-Nyquist relation $\langle V^2_{vac}\rangle = 4k_BTZ_0\Delta f$ is **applied literally** to the lattice (with $Z_0\approx376.73\,\Omega$) and the boundary-thermalization transmission $4Z_0Z_{int}/(Z_0+Z_{int})^2$ follows from the standard $\Gamma$. The leaf is explicit that the relation itself is standard FDT (imported), not newly derived — the lattice ontology is the new content. The transmon coherence model is qualitative (reproduces "observed error-rate timelines," no per-device $T_1$) and the FDT closure $P_{noise,in}=P_{Ohmic,out}$ is asserted as a structural balance, not a per-mode calculation. Disclosed import bound.
- strengthen-by:
  - Carry out the per-mode FDT equilibrium ($P_{noise}=P_{Ohmic}$) as a calculation rather than a structural assertion.
  - Give a quantitative $T_1$ for a specified transmon to convert the qualitative coherence model into a prediction.

---

## Water $4\,^{\circ}$C Anomaly via Two-State LC Partition
<!-- id: clm-jpfbm6 -->

- $S(r) = f_{yield}\sqrt{1 - (r_{th}/r_{crit})^2}$ with $r_{crit} = \sqrt{2\alpha}$; melting eigenmode $T_m = 279.5$ K; macroscopic structural-fluid bound at $\approx +29.4\,^{\circ}\text{C}$
- _Specific Claims_
  - Water occupies two LC structural extremes: (I) tetrahedral H-bonded lattice with $V = a^3$, $a = 4 r_{OO}/\sqrt{3}$, $r_{OO} = 2.727\,\text{\AA}$ (from Op4 Vol 5 cross-volume primary); (II) FCC random close-packing ($\varphi = \pi\sqrt{2}/6 \approx 0.7405$, Axiom 2). The macroscopic transition between the two is governed by the Axiom 4 saturation kernel above.
  - The $+4\,^{\circ}$C density maximum emerges as a *statistical* consequence of cooperative 3D LC-network averaging within this two-state domain, not as a closed-form output. Pure 1D polynomial fits cannot reproduce it without empirical fudging because the underlying 3D Ising-like cooperative grid is NP-hard.
  - The dielectric constant follows the same partition via the Kirkwood-Frohlich form $g_{kirkwood} = 1 + z\cos^2(\theta/2) f_I$ with $z = 4$ tetrahedral symmetry.
  - The 2026 Nilsson sub-femtosecond X-ray laser observation of supercooled water LDL/HDL splitting is asserted to corroborate the two-state geometry: LDL = expanded tetrahedral phase $V_I$, HDL = collapsed FCC $V_{II}$.
- _Specific Non-Claims and Caveats_
  - Does NOT claim a closed-form ab initio derivation of the $+3.98\,^{\circ}$C density-maximum temperature; the leaf is explicit that this requires explicit numerical 3D cooperative-lattice simulation and that no 1D continuous polynomial yields it without iteration. Treat the agreement as qualitative / numerically demonstrated rather than a closed-form prediction.
  - The melting temperature $T_m = 279.5$ K and the H-bond Void energy $0.2158$ eV are sourced from Vol 5 (Op4 H-bond equilibrium) and Vol 7 (proton-transfer melting eigenmode); the cross-volume primaries are explicitly cited in the leaf and must be loaded to evaluate the chain.
  - The Nilsson 2026 LDL/HDL identification is presented as a structural consistency claim, not an experimental discrimination against competing two-state models of water.
  - The structural-fluid upper bound at $+29.4\,^{\circ}$C is the lattice $r_{crit}$ envelope; the empirical density anomaly persists only through the lower part of this envelope, and the leaf does not claim a sharp lattice-derived signature at exactly $+29.4\,^{\circ}$C in observation.
  - Engine implementation (`CooperativeHexagonalLattice.evaluate_structural_fraction(T)`) is named in the leaf but its numerical convergence and parameter sensitivity are not characterised here; treat as a code-pointer, not a separately validated derivation.

> **Leaf references:** [water-anomaly-lc-partition](./condensed-matter/ch11-thermodynamics/water-anomaly-lc-partition.md).

### Quality
- confidence: 0.5
- depends-on:
  - Axiom 2 (Topo-Kinematic Isomorphism — FCC packing $\varphi = \pi\sqrt2/6$)
  - Axiom 4 (Universal Saturation Kernel — yield boundary $r_{crit} = \sqrt{2\alpha}$)
  - `clm-iouqn9` (common: $\nu_{vac} = 2/7$ / K = 2G yield, solidity X)
- solidity: 0.50 (use as input only, don't build deeper) [= min(0.50, 0.55)]
- rationale: The two-state LC partition (State I tetrahedral $V = a^3$, State II FCC close-packing) and the yield boundary $S(r) = f_{yield}\sqrt{1-(r_{th}/r_{crit})^2}$ are structurally derived, and the $+29.4°$C structural-fluid bound follows from $r_{crit}$. But the leaf is **explicit** that the $+3.98°$C density maximum is NOT a closed-form output — it requires NP-hard 3D cooperative-lattice numerical simulation and "no 1D continuous polynomial yields it without fudging." Also imports $T_m = 279.5$ K (Vol 7) and $d_{OO} = 2.727$ Å (Vol 5) as cross-volume primaries. Substantive open dependency: the headline anomaly is numerically demonstrated, not derived in closed form.
- strengthen-by:
  - Characterise the `CooperativeHexagonalLattice` engine's convergence/parameter sensitivity so the $+4°$C result is a validated numerical derivation, not a code-pointer.
  - Reduce the cross-volume imports ($T_m$, $d_{OO}$) to in-leaf derivations or cite them as explicit clm-deps.
# vol3 L3-migration register entries (NEW-IN-L3 minted claims) — confidence pending (deferred rescore)

## Discrete-Lattice Horizon Entropy Constant
<!-- id: clm-cfd5yf -->

Under the corpus symmetric-saturation picture ($\Gamma_{\text{continuum}} = 0$ at the BH horizon), the discrete K4 lattice structure at scale $\ell_{\text{node}}$ generates a finite second-order residual reflection per cell, $|\Gamma|^2 \sim (\ell_{\text{node}}/r_{\text{sat}})^2$. Summed over $N_{\text{cells}} \sim (r_{\text{sat}}/\ell_{\text{node}})^2$ horizon cells, the per-cell suppression cancels the cell count, leaving a universal mass-independent entropy constant $\hat S_{\text{horizon}} \approx 4\pi \log 2 \cdot k_B \approx 8.7\,k_B$ (Flag 62-G closure).

- _Specific Claims_
  - Discrete-lattice corrections give a universal horizon entropy $\hat S_{\text{horizon}} \approx 4\pi\log 2 \cdot k_B \approx 8.7\,k_B$, independent of BH mass.
  - Per-cell $|\Gamma|^2 \sim (\ell_{\text{node}}/r_{\text{sat}})^2$ exactly cancels $N_{\text{cells}} \sim (r_{\text{sat}}/\ell_{\text{node}})^2$, leaving an $O(1)$ product.
  - Interpreted as a one-time horizon-formation cost (topological invariant), not a degrees-of-freedom count.
- _Specific Non-Claims and Caveats_
  - Leading-order dimensional estimate only; rigorous WKB hits a near-horizon coordinate singularity (numerical prefactor / possible log corrections open, §9).
  - NOT a candidate for thermodynamic $S_{BH}$ (does not scale with area or mass).

> **Leaf references:** [discrete-lattice-entropy-constant](./condensed-matter/ch11-thermodynamics/discrete-lattice-entropy-constant.md).

### Quality
- confidence: 0.5
- depends-on:
  - Axiom 1 (Substrate Topology — discrete K4 lattice at $\ell_{node}$)
  - Axiom 4 (Universal Saturation Kernel — symmetric saturation $\Gamma_{continuum}=0$)
  - `clm-07kd5v` (Vol 3 symmetric impedance $Z = Z_0$, solidity X)
  - `clm-rd9cjm` (Vol 3 refractive index $n(r)$ — used in §3 expansion, solidity X)
  - `clm-x19btt` (Vol 3 $r_{sat} = 7GM/c^2$ saturation radius, solidity X)
- solidity: 0.50 (use as input only, don't build deeper) [= min(0.50, 0.55)]
- rationale: The cancellation argument is structurally clean — per-cell $|\Gamma|^2\sim(\ell_{node}/r_{sat})^2$ against $N_{cells}\sim(r_{sat}/\ell_{node})^2$ leaves an $O(1)$ product $4\pi\log2\,k_B\approx8.7\,k_B$. But §4 explicitly labels the per-cell $|\Gamma|^2$ a "pragmatic dimensional estimate" / "leading dimensional correction," and §9 discloses that a rigorous WKB calculation hits a near-horizon coordinate singularity, leaving the numerical prefactor and possible log corrections open. The order-of-magnitude and mass-independence are robust; the numerical constant is a leading-order dimensional estimate, not a closed derivation — substantive acknowledged open step.
- strengthen-by:
  - Complete the near-horizon WKB calculation with a coordinate regulator to fix the prefactor and confirm/exclude log corrections.
  - Derive the per-cell $|\Gamma|^2$ second-order correction from the discrete K4 bond impedance rather than the dimensional estimate.

---

## Four Distinct Entropy Quantities at the BH Horizon
<!-- id: clm-4o0f0h -->

AVE distinguishes four physically distinct entropy quantities at a BH horizon — AVE-native geometric $\hat S_{\text{geo}} = k_B A \log 2/\ell_{\text{node}}^2$ (Op14 scattering irreversibility at A-B interface cells), thermodynamic $S_{BH} = A/(4\ell_P^2)$ (imported via the first law), microstate count $2^{A/\ell_{\text{node}}^2}$, and volume-thermalization $S_v$ (Boltzmann) — which coexist with ratios spanning $\sim 10^{44}$. The ratio $\hat S_{\text{geo}}/S_{BH} = 4\log 2/(7\xi) \approx 2.8\times 10^{-44}$ is the Machian dilution factor; the first-law $T\,dS = dE$ recovers standard $S_{BH}$ only via imported equipartition that AVE rejects.

- _Specific Claims_
  - Four entropy quantities are distinct, coexisting, and measure different physics (not redundant).
  - AVE-native geometric entropy $\hat S_{\text{geo}} = k_B A \log 2/\ell_{\text{node}}^2$ from a $|\Gamma|^2 = 1/2$ A-B-interface beam-splitter per horizon cell.
  - Machian dilution ratio $\hat S_{\text{geo}}/S_{BH} \approx 2.8\times 10^{-44}$.
- _Specific Non-Claims and Caveats_
  - First-law $T\,dS = dE$ recovery of $S_{BH}$ is via imported Boltzmann counting AVE rejects (not axiom-first); AVE-native $\hat S_{\text{geo}}$ violates the first law by $\sim 10^{-44}$.
  - $S_v$ is factor-of-4 off and uses Boltzmann mode-counting; $S_\mu$ is an informal microstate framing.

> **Leaf references:** [four-entropy-distinction](./condensed-matter/ch11-thermodynamics/four-entropy-distinction.md).

### Quality
- confidence: 0.7
- depends-on:
  - Axiom 1 (Substrate Topology — A-B sublattice interface)
  - Axiom 4 (Universal Saturation Kernel — symmetric saturation, $\Gamma_{horizon}=0$)
  - `clm-07kd5v` (Vol 3 symmetric impedance $Z = Z_0$, solidity X)
  - `clm-x19btt` (Vol 3 $r_{sat}$ / compactness-limit saturation radius, solidity X)
  - `clm-ze4clw` (common: M,Q,J boundary observables, solidity X)
- solidity: 0.55 (use as input only, don't build deeper) [= min(0.70, 0.55)]
- rationale: The four-way distinction is laid out cleanly and the AVE-native $\hat S_{geo} = k_BA\log2/\ell_{node}^2$ follows from a $|\Gamma|^2 = 1/2$ frustrated-bond beam-splitter (a 50/50 split = one bit/cell), with the Machian dilution ratio $\hat S_{geo}/S_{BH} = 4\log2/(7\xi)\approx2.8\times10^{-44}$ being clean algebra. The leaf is exemplary in disclosing that the standard $S_{BH}$ recovery requires **imported Boltzmann equipartition that AVE rejects**, that $S_v$ is a factor-of-4 off, that $S_\mu$ is informal, and that the first law is violated by $\sim10^{-44}$ on AVE-native quantities. Disclosed-bound: the distinction and $\hat S_{geo}$ close; the $|\Gamma|^2=1/2$ value is an assigned interface eigenmode, not independently derived.
- strengthen-by:
  - Derive $|\Gamma|^2 = 1/2$ at the frustrated A-B bond from the chirality-mismatch impedance rather than asserting the symmetric beam-splitter value.
  - Resolve whether the first-law $\sim10^{-44}$ violation is a genuine prediction (observable) or an artifact of the rejected equipartition import.

---

## Op14 Cosmic-Horizon Saturation Profile
<!-- id: clm-48g5qf -->

Applies the canonical Op14 long-range coupling operator ($Z_{\text{eff}}(r) = Z_0/\sqrt{S(A)}$, Vol 1 Ch 6 §1.13) at cosmic-horizon scale during ongoing K4 crystallisation. As $r \to R_H$, $A^2 \to 1$, $S(A) \to 0$, $\Gamma \to -1$ (the universal saturation surface), local clocks freeze ($\omega_{\text{local}} \to 0$), and an asymmetric ε/μ-decoupled Meissner-type impedance form arises if cosmic crystallisation saturates the ε-sector preferentially. Distinct from the BH event horizon (frozen one-shot Schwarzschild lock) and from BCS symmetric μ-saturation.

- _Specific Claims_
  - At the cosmic horizon, the substrate reaches the canonical $\Gamma = -1$ saturation surface with $Z_{\text{eff}} \to \infty$ and local-clock freezing $\omega_{\text{local}} \to 0$.
  - Asymmetric ε/μ-decoupled Meissner form $Z_{\text{eff}} = Z_0\sqrt{S_\mu/S_\varepsilon}$ when sectors saturate unequally during ongoing crystallisation.
  - Dynamic (crystallising) cosmic horizon is structurally distinct from the frozen BH event horizon.
- _Specific Non-Claims and Caveats_
  - Canonical-piece assembly, NOT a new operator or new derivation; it is a (c)-operator-application of Op14.
  - Class E operating-point projection (joint-constrained with $\{G, H_\infty, \hat\Omega_{\text{freeze}}, \alpha\}$ at $u_0^* \approx 0.187$), not an independent prediction.

> **Leaf references:** [op14-cosmic-horizon-profile](./cosmology/ch04-generative-cosmology/op14-cosmic-horizon-profile.md).

### Quality
- confidence: 0.7
- depends-on:
  - Axiom 4 (Universal Saturation Kernel — $S(A)\to0$ at horizon)
  - `clm-sysqaf` (common: universal operator catalog Op1–Op22, incl. Op14, solidity X)
  - `clm-gz7ryg` (common: A-034 single-kernel unification, solidity X)
  - `clm-ze4clw` (common: $\Gamma=-1$ M,Q,J boundary observables, solidity X)
  - `clm-dsb560` (common: three-route $\alpha$/$G$/$J_{cosmic}$ from $\Omega_{freeze}$, solidity X)
  - `clm-1eg13f` (Vol 4 Op14 saturation modulating local clock rate, solidity X) [vol3→vol4 exception, D11]
- solidity: 0.45 (use as input only, don't build deeper) [= min(0.70, 0.45)]
- rationale: The leaf is **explicit and disciplined** that this is a (c)-operator-application — canonical Op14 ($Z_{eff} = Z_0/\sqrt{S(A)}$) applied at cosmic-horizon scale, NOT a new operator or new derivation. The profile forms ($Z_{eff}\to\infty$, $\omega_{local}\to0$, asymmetric Meissner $Z_{eff} = Z_0\sqrt{S_\mu/S_\varepsilon}$) follow directly from the canonical kernel and disclosed canonical pieces. It is explicitly a Class-E operating-point projection at $u_0^*$, NOT an independent prediction. Disclosed-import bound: the assembly is clean but the rigor is inherited from the (vol4-canonical) Op14 derivation, which cannot be cited as a vol3 dependency (acyclicity — see worksheet flag).
- strengthen-by:
  - Once Op14's canonical derivation is reachable as a non-cyclic dependency (relocate to common, or express as a support node), bind it explicitly so this leaf's solidity reflects the operator's own rigor.
  - Close the open $\rho_{latent}$ / $\Gamma_{cryst}$ substrate derivations (§8) that the cosmic-horizon profile is meant to anchor.

---

## Cosmological Constant Closure
<!-- id: clm-s4n33u -->

From the corpus-derived $H_\infty = 28\pi m_e^3 cG/(\hbar^2\alpha^2)$ applied through the Friedmann/de Sitter relation, AVE predicts $\rho_\Lambda = 9.03\times 10^{-27}$ kg/m³ — within a factor $1.54$ of the Planck-2018 measurement (exact in the de Sitter asymptote) with no $\rho_\Lambda$-specific fit parameters. QED's naive zero-point-energy prediction is off by $\sim 10^{122}$, so AVE represents a $\sim 10^{122}$ improvement on the standard QFT estimate of the cosmological constant.

- _Specific Claims_
  - $\rho_\Lambda = 9.03\times 10^{-27}$ kg/m³ and $\Lambda = 1.68\times 10^{-52}$ m⁻², both within factor 1.54 of Planck-2018.
  - $\sim 10^{122}$ improvement over QED's naive ZPE prediction.
  - Derived from canonical corpus inputs with no $\rho_\Lambda$-specific fit parameter.
- _Specific Non-Claims and Caveats_
  - Carries the framework-wide $\delta_{\text{strain}} \approx 2.225\times 10^{-6}$ CMB thermal-running residual, currently empirically calibrated at $T_{\text{CMB}}$ pending quantitative substrate-physics derivation (Q-DELTA-MAP-1 closed at mechanism-class identification 2026-05-28 via Cosserat-rotation-sector mass-gap thermal-mode-population ASYM at clm-hp7nlm; **Q-DELTA-MAP-1-quant** ATTEMPTED→NEGATIVE (FT-1 2026-05-31: E-mode Bose-Einstein occupation undershoots $\eta_\varepsilon$ by ~31 OOM, [`research/2026-05-31_FT-1_delta-strain-eta-epsilon_result.md`](../../../research/2026-05-31_FT-1_delta-strain-eta-epsilon_result.md)) — so the δ_strain magnitude is a **definitional residual** ($1-$CODATA$/\alpha_\text{cold}$), not a derived thermal observable; the 2026-06-04 bijection closure confirms the broader named-identification framing, see [`research/2026-05-28_phase-3-a3-delta-strain-machian-projection-result.md`](../../../research/2026-05-28_phase-3-a3-delta-strain-machian-projection-result.md) §3 for earlier WALK-BACK history), inherited via $\alpha$ closure.
  - Downstream of the open $G$/$H_\infty$ Machian closure (Class E joint constraint), not a fully first-principles single-observable prediction.

> **Leaf references:** [cosmological-constant-closure](./cosmology/ch05-dark-sector/cosmological-constant-closure.md).

### Quality
- confidence: 0.7
- depends-on:
  - `clm-wx5324` (Vol 3 $H_\infty = 28\pi m_e^3 cG/\hbar^2\alpha^2$, solidity X)
  - `clm-3ii690` (Vol 3 phantom-energy / latent-heat equation of state, solidity X)
  - `clm-dsb560` (common: three-route $\alpha$/$G$/$J_{cosmic}$ from $\Omega_{freeze}$, solidity X)
  - `clm-q4c615` (common: A-031 cosmic-parameter horizon / strain-snap, solidity X)
- solidity: 0.45 (use as input only, don't build deeper) [= min(0.70, 0.45)]
- rationale: Given $H_\infty$, the chain $\rho_\Lambda = 3H_\infty^2/(8\pi G) = 9.03\times10^{-27}$ kg/m³ via standard Friedmann/de Sitter is clean, and the factor-1.54 vs Planck-2018 is honestly attributed to $\Omega_\Lambda = 0.685 < 1$ (de Sitter asymptote vs current epoch) with the arithmetic shown ($1.54\times0.685\approx1$). The "$10^{122}$ improvement over QED" is a fair framing. Band at disclosed-bound because the leaf is explicit it is **downstream of the open $G$/$H_\infty$ Machian closure** (Class-E projection, not independent single-observable prediction), carries the empirically-calibrated $\delta_{strain}\approx2.225\times10^{-6}$ CMB residual, and lists $\rho_{latent}$/$\Gamma_{cryst}$ derivations as open work.
- strengthen-by:
  - Derive $\rho_{latent}$ from substrate crystallisation energetics ($\Delta E_{cryst}$ from $\ell_{node},\alpha,G$) and verify the Friedmann route equals the latent-heat route (the leaf's named open items 1–3).
  - Derive $\delta_{strain}$ from first principles rather than calibrating it at $T_{CMB}$.



---

## DAMA Energy Quantum via α-Slew Substrate-Rate
<!-- id: clm-b27pnp -->

Predicts a DAMA/LIBRA coupling quantum at $E = \alpha\, m_e c^2 \approx 3.728$ keV via a Schwinger anomalous-moment substrate-rate (Axiom-4 saturation-kernel back-reaction on the LC tank, projected through the Hoop-Stress $2\pi$ factor), landing in the observed 2–6 keV annual-modulation window. After the 8th–9th audit cycles the energy-scale status is honest-scoped: the value coincides within 1% with Ca Kα (Moseley), so the numerical match alone does not discriminate AVE from SM atomic physics; the AVE-distinguishing content is the reactive-power categorical reframe plus the §11 cross-experiment tests.

- _Specific Claims_
  - Substrate derivation gives a coupling quantum $E = \alpha\,m_e c^2 \approx 3.728$ keV in the DAMA window.
  - AVE-distinguishing claims (§11): Z-independence under cross-crystal swap; CMB-velocity phase-lock of the annual modulation; solid-vs-liquid binary gate (DAMA positive / XENONnT null).
  - α m_e c² is the per-cycle reactive power of the electron LC tank ($P_{real}=0$), not a real radiated photon quantum.
- _Specific Non-Claims and Caveats_
  - Energy-scale "zero-parameter CONFIRMED" status DEMOTED (2026-05-17 audit): 1% coincidence with Ca Kα via Moseley; magnitude alone does not discriminate.
  - Rate magnitude / single-Q-factor closure PAUSED pending anti-anchor + substrate-mode-density work. (Preserves the leaf's 🔴 scope-correction author marker.)

> **Leaf references:** [dama-alpha-slew-derivation](./cosmology/ch05-dark-sector/dama-alpha-slew-derivation.md).

### Quality
- confidence: 0.5
- depends-on:
  - Axiom 4 (Universal Saturation Kernel — saturation back-reaction on the LC tank)
  - `clm-stgx1i` (Vol 2 $g-2$ Schwinger $a_e = \alpha/2\pi$, solidity X)
  - `clm-u86caq` (Vol 3 MOND $a_0$ — shared Hoop-Stress $2\pi$ projection, solidity X)
  - `clm-ce8dg1` (Vol 1 substrate-equilibrium $v=\alpha c/2\pi$ — shared α-slew rate, solidity X)
  - `clm-rtdmsn` (Vol 4 electron Q-factor LC tank — α-slew LC mechanism, solidity X) [vol3→vol4 exception, D11]
  - `clm-1eg13f` (Vol 4 Op14 saturation modulating local clock rate, solidity X) [vol3→vol4 exception, D11]
  - `clm-v6ti0v` (Vol 4 orbital friction reactive-vs-real power, solidity X) [vol3→vol4 exception, D11]
- solidity: 0.50 (use as input only, don't build deeper) [= min(0.50, 0.50)]
- rationale: $E = a_e\,m_ec^2 = \alpha m_ec^2 = 3.728$ keV follows by a clean substitution chain ($\nu_{slew} = a_e\nu_{Compton}$, $\ell_{node} = \hbar/m_ec$) and lands in the DAMA 2–6 keV window. But the leaf's own 8th/9th-cycle audit (preserved 🔴 author markers) **demotes** the "zero-parameter CONFIRMED" energy-scale status: it is a 1% coincidence with Ca Kα via Moseley, so magnitude alone does not discriminate AVE from SM atomic physics. Rate magnitude is explicitly PAUSED. The AVE-distinct content (Z-independence, CMB phase-lock, solid/liquid gate) is partly confirmed but the load-bearing energy claim rests on a disclosed unresolved anti-anchor — substantive open dependency.
- strengthen-by:
  - Resolve the Ca Kα anti-anchor via the cross-crystal Z-independence test (NaI/Sapphire/Ge) so the energy line discriminates AVE from Moseley.
  - Close the rate magnitude (single-Q-factor) derivation that the leaf pauses pending anti-anchor + substrate-mode-density work.

---

## DAMA Rate Magnitude — Matched-LC-Coupling Formula
<!-- id: clm-5em8fx -->

Candidate formula for the DAMA rate magnitude from matched-impedance coupling between the electron's reactive α-slew LC tank and a coherent NaI crystal LC mode: per-cycle efficiency $\epsilon_{det} = 4\pi/N_{single}^2$ (with $4\pi$ the observable-Compton-cycle radiation-impedance averaging factor — substrate-mechanism bipartite K4 lobe-count, SU(2) double-cover as standard-physics translation reference), giving $R_{predicted} = 4.80\times 10^{-7}$ events/s/kg vs DAMA/LIBRA Phase-2 observed $4.77\times 10^{-7}$ — a 0.6% consistency. Cross-detector forward predictions follow (HPGe 9.39 kg is the cleanest single-experiment test for 4 AVE-distinct claims).

- _Specific Claims_
  - $\epsilon_{det} = 4\pi/N_{single}^2$ yields rate within 0.6% of DAMA Phase-2 observed.
  - Cross-detector forward predictions (e.g., HPGe 9.39 kg) discriminate AVE-distinct claims.
  - Cycle-12 form excises $\kappa_{entrain}$ (real-power class) and unifies into a single $\epsilon_{param}\times\kappa_{quality}$ parametric-coupling kernel.
- _Specific Non-Claims and Caveats_
  - The 0.6% match is a POST-HOC consistency check, NOT a forward prediction — the $4\pi$ prefactor was selected after inspecting the rate gap (§3.2). (Preserves the leaf's honest-scope / Grant-adjudication CANONIZED-status marker.)
  - Rigor refinements pending (parametric-coupling-kernel §12).

> **Leaf references:** [dama-matched-lc-coupling](./cosmology/ch05-dark-sector/dama-matched-lc-coupling.md).

### Quality
- confidence: 0.3
- depends-on:
  - Axiom 3 (Minimum Reflection Principle — matched-impedance coupling)
  - Axiom 4 (Universal Saturation Kernel — vacuum varactor at sub-yield)
  - `clm-b27pnp` (Vol 3 DAMA α-slew energy quantum / $\nu_{slew}$, solidity X)
  - `clm-6t3p6x` (Vol 4 parametric coupling kernel — matched-LC varactor coupling, solidity X) [vol3→vol4 exception, D11]
  - `clm-rtdmsn` (Vol 4 electron Q-factor LC tank — matched-impedance coupling, solidity X) [vol3→vol4 exception, D11]
- solidity: 0.30 (do not build on, rework needed) [= min(0.30, 0.50)]
- rationale: $\epsilon_{det} = 4\pi/N_{single}^2$ yields a rate $4.80\times10^{-7}$ within 0.6% of DAMA Phase-2. But the leaf is explicit (§3.2, preserved honest-scope / CANONIZED-status Grant marker) that this is a **POST-HOC consistency check, NOT a forward prediction** — the $4\pi$ prefactor was selected from five canonical candidates *after* inspecting the rate gap. The Theorem 3.1′ "inheritance" argument is structurally clean but acknowledged as assembled post-hoc, and the $1/N^2$ scaling is a heuristic Dicke-amplitude argument with full QM derivation pending (§12). Sketch with structural support, not a closed forward derivation — asserted-partial.
- strengthen-by:
  - Run the forward-predictive cross-detector tests (HPGe 9.39 kg at 3.728 keV is the cleanest) to convert the post-hoc match into a forward result.
  - Complete the full QM many-body derivation of the $1/N^2$ scaling and the $\kappa_{quality}$ sub-regenerative envelope (the leaf's §12 pending items). (Note: Theorem 3.1′ and the parametric-coupling kernel live in vol4 and are omitted as cyclic deps — see worksheet flag.)

---

## DM-Mechanism Unification (Substrate-Shared, Operator-Distinct)
<!-- id: clm-tt8j0v -->

Three independently-validated AVE dark-sector observables share one foundational substrate (K4 Cosserat micropolar lattice + Axiom 4) but operate through three distinct operators: galactic rotation via the $\eta_{eff}$ saturation kernel, cluster (bullet) via a ponderomotive halo, and atomic-scale via parametric coupling. Unification is at the substrate level (shared Ax1 + Ax4), not at the operator level; limbs i + iii sit in a Hoop-Stress $2\pi$ projection sub-family (`mond-hoop-stress.md §4.5`) while limb ii (cluster) is a separate ponderomotive operator class (C13c META row of the divergence-test substrate map).

- _Specific Claims_
  - Three DM observables are unified at the substrate level (shared K4 + Ax4) while remaining operator-distinct.
  - Limbs i (cosmic) + iii (atomic) share the Hoop-Stress $2\pi$ projection; limb ii (cluster) is a distinct ponderomotive operator.
  - Cross-limb predictions: cosmological constant from $a_0$; substrate-equilibrium velocity from Hoop-Stress $2\pi$; $\eta_{eff}$ drag connecting rotation to bullet cluster; AVE-PONDER lab-scale parametric coupling.
- _Specific Non-Claims and Caveats_
  - Explicitly NOT a one-Lagrangian deep unification (intentionally): three observables, three operators, one substrate.

> **Leaf references:** [dm-mechanism-unification](./cosmology/ch05-dark-sector/dm-mechanism-unification.md).

### Quality
- confidence: 0.7
- depends-on:
  - Axiom 1 (Substrate Topology — shared K4 Cosserat substrate)
  - Axiom 4 (Universal Saturation Kernel — shared $S(A)$ across limbs)
  - `clm-u86caq` (Vol 3 MOND $a_0$ — limb i, solidity X)
  - `clm-527k22` (Vol 1 bullet-cluster ponderomotive halo — limb ii, solidity X)
  - `clm-b27pnp` (Vol 3 DAMA α-slew — limb iii, solidity X)
  - `clm-6t3p6x` (Vol 4 parametric coupling kernel — shared vacuum-varactor operator, solidity X) [vol3→vol4 exception, D11]
- solidity: 0.40 (do not build on, rework needed) [= min(0.70, 0.40)]
- rationale: This is a **classification/synthesis** claim and it closes cleanly *as such*: three dark-sector observables share one substrate (Ax1+Ax4) but operate via three distinct operators, with limbs i+iii sharing the Hoop-Stress $2\pi$ projection sub-pattern and limb ii (cluster) a separate ponderomotive class. The leaf is disciplined — it explicitly states this is NOT a one-Lagrangian deep unification and scopes each limb to its own canonical derivation. Band at disclosed-bound rather than higher because the unification claim is only as solid as the disclosed-partial limbs it aggregates (limb iii post-hoc, limb ii qualitatively confirmed) and limb iii's parametric kernel is vol4-canonical (omitted as cyclic dep).
- strengthen-by:
  - Close the cross-limb predictions (bullet-cluster halo magnitude from the same parameters as $a_0$; AVE-PONDER lab-scale parametric coupling) to make the "shared substrate" claim quantitatively load-bearing rather than structural.
  - Firm up the weakest limb (iii, DAMA rate, currently post-hoc) so the unification does not inherit an asserted-partial branch.

---

## AVE BH Horizon: $r_{\text{sat}} = 7GM/c^2$ + Area Theorem
<!-- id: clm-law1ho -->

Axiom-first derivation of the AVE-native BH horizon at $r_{\text{sat}} = 7GM/c^2 = 3.5\,r_s$, where the Axiom-4 strain $\varepsilon_{11}(r_{\text{sat}}) = 1$; the factor 7 = $1/\nu_{\text{vac}}$ from the Poisson-ratio projection ($\nu_{\text{vac}} = 2/7$). The horizon area $A = 196\pi G^2 M^2/c^4$ and the area theorem $\delta A = 392\pi G^2 M\,\delta M/c^4 \geq 0$ follow directly from Axiom 4 plus mass-energy conservation — stronger than Hawking's 1971 theorem in that it derives WHY the horizon can only grow (saturation threshold $\propto M$) without invoking energy conditions.

- _Specific Claims_
  - $r_{\text{sat}} = 7GM/c^2 = 3.5\,r_s$ from $\varepsilon_{11}(r_{\text{sat}}) = 1$ and $\nu_{\text{vac}} = 2/7$.
  - Area theorem $\delta A \geq 0$ derived from Axiom 4 + mass-energy conservation (no energy conditions); derives why the horizon can only grow.
  - Prefactor $196\pi G^2/c^4$ vs standard $16\pi G^2/c^4$ (factor 12.25); falsifiable via matter/shear-mode horizon-radius observables.
- _Specific Non-Claims and Caveats_
  - $r_{\text{sat}} = 3.5\,r_s$ is a shear-mode + matter boundary, NOT photon-geometric: EHT shadow / photon-ring radius do NOT discriminate $r_{\text{sat}}$ from $r_s$ (prior EHT-falsifier overclaim retracted 2026-05-16 per Grant audit).
  - The first-law / entropy pillar is only partially axiom-derived (see four-entropy leaf); only area + mass-energy pillars are axiom-first here.

> **Leaf references:** [ave-bh-horizon-area-theorem](./cosmology/ch15-black-hole-orbitals/ave-bh-horizon-area-theorem.md).

### Quality
- confidence: 0.9
- depends-on:
  - Axiom 2 (Topo-Kinematic Isomorphism — mass as inductance, $dE = dM c^2$)
  - Axiom 4 (Universal Saturation Kernel — $\varepsilon_{11}(r_{sat}) = 1$)
  - `clm-iouqn9` (common: $\nu_{vac} = 2/7$ / factor 7 Poisson projection, solidity X)
  - `clm-x19btt` (Vol 3 compactness limit / Buchdahl derivation, solidity X)
- solidity: 0.55 (use as input only, don't build deeper) [= min(0.90, 0.55)]
- rationale: $r_{sat} = 7GM/c^2$ from $\varepsilon_{11}(r_{sat}) = 1$ with the factor $7 = 1/\nu_{vac}$, and the area theorem $\delta A = 392\pi G^2 M\delta M/c^4 \geq 0$ both close cleanly from Axiom 4 (saturation boundary $\propto M$) plus mass-energy conservation — no energy conditions needed, deriving *why* the horizon grows. $dE = dM c^2$ is itself a disclosed Ax2 identity. The leaf honestly scopes the falsifier (preserved Grant 2026-05-16 audit marker): the EHT-shadow falsifier was retracted because $r_{sat}$ is a shear/matter boundary, photon-geometric observables are silent. Clean derivation; the only disclosed gap (entropy/first-law pillar) is correctly delegated to the four-entropy leaf and not claimed here.
- strengthen-by:
  - Pursue the surviving matter/shear falsifiers (inner-disk Fe-Kα edge vs ISCO, GW echoes) to give the $3.5\,r_s$ prediction an empirical test.
  - Carry the $\nu_{vac} = 2/7$ → factor-7 projection as an in-leaf derivation rather than referencing the Buchdahl-bound leaf.

---

## The Double Deflection — Light Bends Twice as Much as Matter
<!-- id: clm-zf8eah -->

- $\delta_{\text{light}}/\delta_{\text{matter}} = (n_\perp - 1)/(n_{\text{scalar}} - 1) = (2/7)/(1/7) = 2$; $\delta_{\text{light}} = 4GM/(bc^2)$ (Einstein), $\delta_{\text{matter}} = 2GM/(bc^2)$ (Soldner), with $\chi_{vol} = 7GM/(c^2 r)$
- _Specific Claims_
  - Matter (an isotropic 3D volumetric massive wave packet) couples to the *scalar* bulk strain via the $1/7$ volumetric projection: $n_{\text{scalar}} = 1 + (1/7)\chi_{vol}$.
  - Light (a purely transverse Cosserat shear wave) is mechanically blind to the bulk and couples to the transverse cross-sectional strain via the Poisson ratio: $n_\perp = 1 + \nu_{vac}\chi_{vol} = 1 + (2/7)\chi_{vol}$.
  - The deflection is linear in the projection coefficient in the eikonal limit; since $2/7$ is exactly double $1/7$, the photon refracts through a gradient exactly twice as severe, giving the Einstein $4GM/(bc^2)$ vs the Soldner $2GM/(bc^2)$ — Sun grazing $\to 1.75''$.
  - The GR "factor of 2" is reframed as the transverse:isotropic Poisson ratio of a $K = 2G$ trace-reversed Cosserat solid, not a curved-4-manifold signature nor null-geodesic geometry.
- _Specific Non-Claims and Caveats_
  - This is a **consistency check** (category iii): AVE reproduces the standard Einstein deflection via mechanical Poisson projection, not an independent novel prediction beyond GR.
  - The coupling-selection step — that a massive packet couples only to the scalar $1/7$ bulk while the photon, mechanically blind to bulk, couples only to the $2/7$ transverse sector — is asserted by **mechanical analogy**, not derived from a wave-equation projection. This is the one soft joint in the derivation.

> **Leaf references:** [double-deflection](./gravity/ch02-general-relativity/double-deflection.md).

### Quality
- confidence: 0.78
- depends-on:
  - `clm-rd9cjm` (Vol 3 refractive index of gravity / $\nu_{vac} = 2/7$ trace-reversal / $1$-$7$ impedance projection cluster, solidity X)
- solidity: 0.55 (use as input only, don't build deeper) [= min(0.78, 0.55)]
- rationale: consistency-check. The arithmetic $\delta_{\text{light}}/\delta_{\text{matter}} = (2/7)/(1/7) = 2$ is clean once the two projection coefficients are in hand, and reproduces both the Soldner and Einstein deflections plus the $1.75''$ solar value. The single soft joint is the coupling-selection step (massive packet → scalar $1/7$ bulk only; photon → transverse $2/7$ sector only), asserted by mechanical analogy rather than derived from a wave-equation projection. Confidence 0.78 set by the applied-mathematician pass.
- strengthen-by:
  - Derive the coupling selection (matter→scalar-bulk, light→transverse-shear) from a wave-equation projection of the massive vs massless dispersion onto the Cosserat strain tensor, replacing the mechanical-analogy assertion.

---

## White Dwarf Gravitational Redshift — Saturation Correction
<!-- id: clm-at7x0y -->

- $z_{\text{AVE}} = 1/(\sqrt{1 - 2GM/c^2R}\cdot S(\varepsilon_{11})) - 1$, $S(\varepsilon_{11}) = \sqrt{1 - \varepsilon_{11}^2}$, $\varepsilon_{11} = 7GM/c^2R = 7\phi$; $\delta z = z_{\text{AVE}} - z_{\text{GR}} \approx z_{\text{GR}}\cdot\varepsilon_{11}^2/2 = 49\phi^2/2$ = $12.25\times$ the PPN $2\phi^2$ term
- _Specific Claims_
  - The AVE gravitational redshift carries an Axiom-4 saturation factor $S(\varepsilon_{11}) = \sqrt{1 - \varepsilon_{11}^2}$ beyond the Schwarzschild term; the correction over GR scales as $49\phi^2/2$, 12.25 times larger than the standard PPN second-order $2\phi^2$ correction, due to the Machian stress boundary $T_{\max} = c^4/(7G)$ ($\varepsilon_{11} = 7\phi$).
  - For Sirius B: $v_{\text{obs}} = 80.65 \pm 0.77$ km/s, $v_{\text{GR}} = 77.75$ km/s, $v_{\text{AVE}} = 77.80$ km/s; the AVE correction is $\sim 0.05$ km/s, in the correct (upward) direction.
- _Specific Non-Claims and Caveats_
  - **Not currently discriminating.** The $\sim 0.05$ km/s AVE correction is far below the $2.9$ km/s observed$-$GR residual, which is dominated by the 3–5% mass-radius relation uncertainty, not by missing physics. The prediction is correct-direction but not yet a test that distinguishes AVE from GR at current M-R precision.
  - The shear-eigenmode prediction (clm-mi6ils) modifies only $g_{rr}$ (spatial metric), not $g_{00}$ (temporal); standing shear waves do NOT contribute to spectral redshift.

> **Leaf references:** [white-dwarf-gravitational-predictions](./gravity/ch20-white-dwarf-predictions/white-dwarf-gravitational-predictions.md).

### Quality
- confidence: 0.52
- depends-on:
  - Axiom 4 (Universal Saturation Kernel — saturation factor $S(\varepsilon_{11}) = \sqrt{1 - \varepsilon_{11}^2}$ on the redshift)
  - `clm-rd9cjm` (Vol 3 $\nu_{vac} = 2/7$ → $\varepsilon_{11} = 7\phi$ Machian stress boundary, solidity X)
- solidity: 0.52 (use as input only, don't build deeper) [= min(0.52, 0.55)]
- rationale: emergence-test. The redshift formula $z_{\text{AVE}} = 1/(\sqrt{1-2GM/c^2R}\cdot S) - 1$ follows cleanly from the Axiom-4 saturation factor applied to the Schwarzschild term, and the $12.25\times$ amplification over the PPN $2\phi^2$ correction is a clean consequence of $\varepsilon_{11} = 7\phi$. The caveat is empirical, not derivational: the $\sim 0.05$ km/s correction is far below the $2.9$ km/s residual (dominated by 3–5% M-R uncertainty), so the prediction is correct-direction but not currently discriminating. Confidence 0.52 set by the applied-mathematician pass.
- strengthen-by:
  - Tighten the white-dwarf mass-radius constraints (e.g. improved JWST M-R) so the $\sim 0.05$ km/s saturation correction rises above the measurement residual and becomes a discriminating AVE-vs-GR test.

---

## White Dwarf Standing Shear-Wave Eigenfrequencies
<!-- id: clm-mi6ils -->

- WD surface = shear reflector ($\Gamma \approx -1$); $r_{\text{eff}} = R/(1 + \nu_{vac}) = 7R/9$; $f_\ell = \ell c/(2\pi r_{\text{eff}})$, $Q = \ell$; $\ell = 2$ modes $\sim 13$–$21$ Hz (LIGO band) for the five named white dwarfs
- _Specific Claims_
  - The WD interior is evanescent for shear perturbations (plasma frequency $\omega_p \gg$ any GW frequency), so the surface acts as a near-perfect shear reflector ($\Gamma \approx -1$); the effective cavity radius is $r_{\text{eff}} = R/(1 + \nu_{vac}) = 7R/9$ with $\nu_{vac} = 2/7$.
  - Eigenfrequencies $f_\ell = \ell c/(2\pi r_{\text{eff}})$ with quality factor $Q = \ell$; the $\ell = 2$ modes land at $\sim 13$–$21$ Hz (Sirius B 21.15, 40 Eridani B 13.63, Procyon B 14.27, Stein 2051 B 15.34, GD 358 13.94 Hz) — the LIGO / Einstein Telescope band.
  - These standing shear modes modify $g_{rr}$ (spatial metric) only; their observational signature is gravitational-wave ringdown, not spectral line shift. They are a different mode family from interior g-modes/p-modes of ZZ Ceti asteroseismology.
- _Specific Non-Claims and Caveats_
  - The Schwarzschild-BH QNM cross-check ($\omega M_{\text{geom}} = 0.3673$ vs GR exact $0.3737$, 1.7%) is a **cross-regime consistency check using a DIFFERENT boundary radius** ($r_{\text{sat}} = 7GM/c^2$, not the WD surface $R$). It validates the *formula's shape*, NOT the WD-boundary choice — it must not be presented as corroboration of the WD eigenfrequency prediction.
  - No prediction-manifest bridge: the shear-eigenmode result is not currently a manifest prediction entry (the WD redshift, clm-at7x0y, is the P41 bridge target).

> **Leaf references:** [white-dwarf-gravitational-predictions](./gravity/ch20-white-dwarf-predictions/white-dwarf-gravitational-predictions.md).

### Quality
- confidence: 0.50
- depends-on:
  - `clm-rd9cjm` (Vol 3 $\nu_{vac} = 2/7$ → $r_{\text{eff}} = 7R/9$, solidity X)
- solidity: 0.50 (use as input only, don't build deeper) [= min(0.50, 0.55)]
- rationale: emergence-test. The eigenfrequency chain (surface shear reflector $\Gamma \approx -1$ from evanescent degenerate interior → $r_{\text{eff}} = R/(1+\nu_{vac}) = 7R/9$ → $f_\ell = \ell c/(2\pi r_{\text{eff}})$) closes cleanly and lands the $\ell=2$ modes in the LIGO band for all five named WDs. The honest caveat: the BH-QNM 1.7% cross-check uses a DIFFERENT boundary radius ($r_{\text{sat}} = 7GM/c^2$ vs the WD surface $R$) — it validates the formula's shape, not the WD-boundary choice, and must not be read as corroboration of the WD prediction. Confidence 0.50 set by the applied-mathematician pass.
- strengthen-by:
  - Validate the WD-surface boundary choice directly (e.g. against a WD-merger ringdown observation), independent of the BH-QNM shape cross-check, to convert the LIGO-band prediction into a tested result.

---

## δ_strain Substrate-Mechanism: Cosserat-Rotation-Sector Mass-Gap Thermal-Mode-Population ASYM
<!-- id: clm-hp7nlm -->

The substrate-mechanism class for the CMB-thermal-running of $\alpha$ ($\delta_{strain} \approx 2.225 \times 10^{-6}$ at $T_{CMB}$), identified via `ave-ee-first-mapping` v1.0 + Grant 2026-05-28 adjudication. Distinct from the magnitude-back-subtraction at clm-009nkt (Vol 1) — this entry is the substrate-mechanism identification; clm-009nkt is the observable identity.

- _Specific Claims_
  - Substrate carries bipartite thermal-mode structure per Ax 1: 3 translational E-DOFs/node (gapless acoustic, thermally populated at any $T > 0$) + 3 microrotational B-DOFs/node (Cosserat couple-stress mass-gap $\omega_m^2 = 4 G_c / I_\omega$ per canonical [`trampoline-framework.md:188`](../common/trampoline-framework.md); $\omega_m \sim 1$ MeV in physical units).
  - At cosmic temperature $T_{CMB} \approx 2.725$ K: ratio $k_B T_{CMB}/\hbar\omega_m \sim 2 \times 10^{-10}$ → B-modes thermally completely frozen; only E-modes participate in substrate thermal-mode population.
  - Asymmetric E vs B occupation breaks SYM-class scaling: $\varepsilon_{eff} = \varepsilon_0(1-\eta_\varepsilon)$ modulated, $\mu_{eff} = \mu_0$ frozen. Substituting into the α formula using the canonical c_EM phase velocity per clm-8nkvwy:111 ($c_{EM} = 1/\sqrt{\mu_{eff}\varepsilon_{eff}}$): $\alpha_{eff}/\alpha_0 \approx 1 + \eta_\varepsilon/2$, giving $\delta_{strain} \approx \eta_\varepsilon/2$.
  - Sign check: E-mode thermal jiggling counter-charges substrate → $\varepsilon_{eff}$ decreases → $\alpha_{eff}$ increases → $\alpha^{-1}_{eff} < \alpha^{-1}_{ideal}$. CODATA $\alpha^{-1} = 137.035999 < \alpha^{-1}_{ideal} = 137.0363038$ — $\checkmark$ matches observation.
  - Joint-constraint with weak force: same Cosserat couple-stress modulus $\gamma_c$ that sets weak force range $r_W = l_c = \sqrt{\gamma_c/G_{vac}}$ per canonical [`gauge-boson-masses.md:39`](../vol2/particle-physics/ch05-electroweak-mechanics/gauge-boson-masses.md) also sets $\omega_m^2 = 4 G_c/I_\omega$ producing δ_strain. Falsification of the weak-force derivation via the right-handed-neutrino kill-switch (clm-gw2wgc) simultaneously falsifies δ_strain mechanism.
  - EE analog per `ave-ee-first-mapping` v1.0: substrate behaves as high-Q LC oscillator with TCC ceramic capacitor (ε side, thermally modulated) + ferrite inductor below Curie temperature (μ side, frozen). The substrate Cosserat-rotation-sector mass-gap IS the substrate-native Curie analog at substrate-temperature $\sim 10^{10}$ K; ferrite Curie at $\sim 600$ K is the material-specific manifestation of the same mechanism.
  - Forward prediction (substrate-distinct): substrate α drifts roughly linearly with cosmic temperature $T$ for $T \ll T_{B-gap} \sim 10^{10}$ K; quasar absorption-line $\Delta\alpha/\alpha$ at higher redshift tests the substrate TCC mechanism.
- _Specific Non-Claims and Caveats_
  - Does NOT close the quantitative substrate-statistical-mechanics derivation of $\eta_\varepsilon$ from substrate E-mode dispersion + Bose-Einstein occupation at $T_{CMB}$. The numerical δ_strain ≈ $2.225 \times 10^{-6}$ magnitude remains back-subtracted from CODATA at clm-009nkt. The leaf identifies the mechanism class; it does not promote the back-subtraction to a derivation.
  - Class B substrate-mechanism manifestation per `consistency-vs-emergence` v1.3 — NOT Class 2 substrate-mechanism axiom-manifestation. A Class 2 lift requires the quantitative substrate-statistical-mechanics computation that this leaf does not perform.
  - Closes **Q-DELTA-MAP-1** at substrate-mechanism-class identification level ONLY. The three candidate paths P1/P2/P3 enumerated in the Phase 3-A3 WALK-BACK result ([`research/2026-05-28_phase-3-a3-delta-strain-machian-projection-result.md`](../../../research/2026-05-28_phase-3-a3-delta-strain-machian-projection-result.md) §3) are superseded by this leaf's fourth path (P4 — Cosserat-Curie mechanism), but the substrate-mechanism direction-setting that Q-DELTA-MAP-1 originally requested for δ_strain magnitude derivation remains future workstream (named Q-DELTA-MAP-1-quant in the leaf body).
  - Does NOT promote δ_strain to Class E new prediction at this rigor level. Observable axis is Class 4 consistency (the numerical match is by construction at CODATA back-subtraction). Future Class E lift route: substrate-distinct cosmic-temperature-dependent α-drift forward prediction (§6 of leaf) becoming a substrate-distinct empirical handle at higher-redshift quasar measurements.
  - The substrate is NATURAL — engineering observes its behavior; AVE derives the mechanism. This leaf is the AVE-substrate-physics derivation; engineering datasheets are the empirical phenomenology. Same epistemic status as a Cu elemental datasheet vs an atomic-orbital band-structure derivation.

> **Leaf references:** [delta-strain-cosmic-tcc](./cosmology/ch05-dark-sector/delta-strain-cosmic-tcc.md).

### Quality
- confidence: 0.55
- depends-on:
  - clm-3zz0f6 — α Invariance Under Symmetric Gravity — load-bearing: SYM scaling gives α invariance; the Cosserat-Curie ASYM is what breaks SYM to produce δ_strain (the asymmetric scaling voids the SYM α-invariance condition canonical at the gravity-yield leaf)
  - clm-8nkvwy — Symmetric vs Asymmetric saturation case — load-bearing: the c_EM vs c_shear distinction at lines 111/113; the δ_strain derivation uses c_EM in α (NOT c_shear, per Phase 3-A3 walk-back lesson)
  - clm-5zuo7g — Weak Force Range from Cosserat $l_c$ — joint-constraint substrate-primitive ($\gamma_c$ underlies both weak force range AND B-mode mass-gap producing δ_strain); falsification of either falsifies both
- solidity: 0.55 (use as input only, don't build deeper) [= min(0.55, 0.85)]
- rationale: Substrate-mechanism class identified via `ave-ee-first-mapping` v1.0 prototype case + Grant 2026-05-28 adjudication, closing Q-DELTA-MAP-1 at mechanism-identification level (was OPEN per Phase 3-A3 WALK-BACK 2026-05-27; three candidate paths P1/P2/P3 all failed order-of-magnitude estimates). The fourth path P4 (Cosserat-rotation-sector mass-gap thermal-mode-population ASYM) is grounded in canonical Ax 1 bipartite-DOF structure + canonical Cosserat couple-stress primitive $\gamma_c$ (same primitive that sets weak force range per `gauge-boson-masses.md:39`). The EE-first-mapping discipline identified the substrate as a high-Q LC oscillator with TCC ceramic capacitor + ferrite-Curie-frozen inductor — the substrate-Cosserat-Curie mass-gap IS the substrate-native Curie analog. Sign check passes (E-mode counter-charging reduces $\varepsilon_{eff}$, increases $\alpha$, decreases $\alpha^{-1}$ below cold-lattice — CODATA $< \alpha^{-1}_{ideal}$ matches). Class B substrate-mechanism manifestation (NOT Class 2 emergence: the quantitative substrate-statistical-mechanics derivation of $\eta_\varepsilon$ from E-mode dispersion + Bose-Einstein occupation at $T_{CMB}$ is not closed). Class 4 observable consistency on the observable axis (numerical δ_strain ≈ $2.225 \times 10^{-6}$ is back-subtracted from CODATA; not Class E new prediction). Confidence 0.55 reflects: (a) substrate-mechanism class IS identified + load-bearing assumptions explicitly named (Class B); (b) quantitative-derivation gap holds confidence below 0.60 (Class 2 requires substrate-statistical-mechanics work); (c) joint-constraint structure with weak force range adds substantive substrate-physics content beyond canonical SYM/ASYM. Solidity bounded by clm-009nkt observable dependency (0.55 confidence target post-PR amendment; floored at 0.55) and clm-8nkvwy SYM/ASYM canonical-structure dependency.
- strengthen-by:
  - **Q-DELTA-MAP-1-quant** — **ATTEMPTED → NEGATIVE (FT-1, 2026-05-31)**: the quantitative E-mode dispersion + substrate-Bose-Einstein occupation derivation of $\eta_\varepsilon$ at $T_{CMB}$ was run and **undershoots the target $\eta_\varepsilon \approx 4.45\times10^{-6}$ by ~31 OOM** (BE occupation gives ~$10^{-38}$; at $T_{CMB} \ll \Theta_\text{Debye}$ it suppresses *below* equipartition by ~28.5 OOM and cannot amplify). The Class B → Class 2 lift via this route **does NOT occur**; clm-009nkt stays 0.55. The thermal mechanism is **sign-only** — δ_strain's magnitude is a **definitional residual** ($1-$CODATA$/\alpha_\text{cold}$), not a thermal derivation; and per the SM-counterfactual even a match would be generic-thermal, not AVE-distinct. Anchor: [`research/2026-05-31_FT-1_delta-strain-eta-epsilon_result.md`](../../../research/2026-05-31_FT-1_delta-strain-eta-epsilon_result.md). (Reinforced by the 2026-06-04 golden-torus bijection closure: α⁻¹=4π³+π²+π is a named identification on both lift-routes.)
  - Strengthen the joint-constraint cross-check: derive the substrate's $T$-dependent α drift forward prediction (§6.1 of leaf — roughly linear scaling for $T_{CMB} \ll T \ll T_{B-gap}$) to a precision testable against current quasar absorption-line $\Delta\alpha/\alpha$ bounds ($\sim 10^{-5}$); this would lift the observable axis to Class E new prediction.
  - Cross-validate the engineering-scale instance prediction (§6.3 of leaf): TCC of ceramic + ferrite-Curie-frozen LC oscillator frequency-temperature curve should follow the substrate-Cosserat-Curie thermal-mode-population ASYM mechanism scaled to engineering temperatures; quantitative test against empirical EE-component frequency-temperature data validates the substrate-mechanism extrapolation across $\sim 10^{10}$ K temperature range.

---
