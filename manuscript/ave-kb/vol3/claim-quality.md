# Vol 3 — Macroscopic Physics — Claim Quality

<!-- path-stable: referenced from CLAUDE.md INVARIANT-S7 and from vol3/index.md bootstrap directive -->

> **Canonicality:** Leaves are canonical; this volume's indexes are derived summaries. See [cross-cutting claim-quality register](../claim-quality.md) for the full preamble and the canonical list of project-wide tripwires (the cross-cutting sidecar is the source of truth for which tripwires are project-wide; do not infer the list from this preamble). Entries below are scoped to Vol 3; cross-cutting tripwires with vol3-specific manifestations are noted but not duplicated.

---

## Asymptotic Hubble Constant $H_\infty$
<!-- id: wx5324 -->

- $H_{\infty} = 28\pi m_{e}^{3}cG / (\hbar^{2}\alpha^{2}) \approx 69.32$ km/s/Mpc
- _Specific Claims_
  - The relation between $G$ and $H_\infty$ is a **geometric consistency proof**, not an independent first-principles prediction of $H_0$. The Machian coupling $\xi = 4\pi(R_H/\ell_{node})\alpha^{-2}$ embeds $R_H \equiv c/H_\infty$ in the definition of $G$; rearranging back to "compute" $H_\infty$ from $G$ is structurally an identity, not a downstream evaluation.
  - Numerically the relation evaluates to $\sim 69.32$ km/s/Mpc when CODATA $G$ is substituted; this lies between Planck (67.4) and SH0ES (73.0), within $\sim 1\sigma$ of TRGB (69.8).
  - The framework's claim is that "Hubble Tension" reflects different thermodynamic regime measurements of a single underlying lattice crystallisation rate, not that AVE outputs $H_0$ ab initio.
- _Specific Non-Claims and Caveats_
  - Does NOT claim a parameter-free derivation of $H_0$ from axioms 1–4 alone. The lattice-genesis leaf explicitly flags this and points to [Outstanding Rigour Gaps](../common/mathematical-closure.md).
  - Does NOT claim AVE resolves the Hubble Tension by selecting one measurement over the other; the claim is that both are compatible with the same geometric constraint.
  - Promoting this to a true downstream prediction requires deriving $G$ from a local thermodynamic balance independent of $R_H$ — open problem.

> **Leaf references:** `gravity/ch01-gravity-yield/asymptotic-hubble-constant.md`, `gravity/ch01-gravity-yield/optical-refraction-gravity.md`, `cosmology/ch04-generative-cosmology/lattice-genesis-hubble-tension.md`, `cosmology/ch04-generative-cosmology/asymptotic-expansion-limit.md` (alternate algebraic form via the topological packing fraction $p_c$).

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Refractive Index of Gravity $n(r) = 1 + 2GM/(c^2 r)$
<!-- id: rd9cjm -->

- $n(r) = 1 + \nu_{vac}\,\varepsilon_{11} = 1 + (2/7)\,\varepsilon_{11}$ with $\varepsilon_{11}(r) = 7GM/(c^2 r)$
- _Specific Claims_
  - The refractive form $n(r) = 1 + 2GM/(c^2 r)$ is the **temporal component** of the lattice metric (governs clock rate / redshift).
  - Light deflection couples to a **separate spatial component** $n_{spatial} = (9/7)\varepsilon_{11}$. The Einstein deflection $\delta = 4GM/(bc^2)$ comes from integrating the full bidirectional metric; the temporal-only $n(r)$ alone reproduces the Newtonian half-deflection, not the GR value.
  - Solar deflection at the Einstein value is a **category (iii) consistency check** (per cross-cutting Master Prediction Table tripwire) — the framework reproduces the standard result via metric refraction, not an independent novel prediction.
- _Specific Non-Claims and Caveats_
  - Does NOT claim that the same $n(r)$ governs both clock-rate and light-deflection observables. LIVING_REFERENCE.md Pitfall #3: using full lattice density $n = 1 + (11/7)\varepsilon_{11}$ for redshift, or the temporal-only $n$ for deflection, are both errors.
  - Does NOT claim Snell-ray ray-tracing of $n(r)$ alone yields $\delta = 4GM/(bc^2)$ without the trace-reversal projection through $\nu_{vac}$.
  - "Speed of light slows near mass" ($c_{local} = c_0/n$) is **local phase velocity**, not energy transport speed. See cross-cutting Symmetric vs Asymmetric Saturation entry: the impedance is invariant ($Z = Z_0$), so this is not a dispersive medium in the dissipative sense.
  - The $c_{max}$ inference (intergalactic $c$ exceeds local $c$ by $\sim 3{,}600$ m/s, "warp transit baseline") is an extrapolation of the same local refraction relation to $\Phi \to 0$; treat as illustrative of the framework's interpretation, not as an experimentally validated prediction.

> **Leaf references:** Canonical for the temporal/spatial split: `gravity/ch01-gravity-yield/temporal-spatial-lattice-decomposition.md` (Derived Consequence 2 of Axiom 3, verbatim from `manuscript/common_equations/eq_axiom_3.tex`). Refractive-index derivations: `gravity/ch03-macroscopic-relativity/refractive-index-of-gravity.md`, `gravity/ch03-macroscopic-relativity/transverse-refractive-index.md`, `gravity/ch03-macroscopic-relativity/einstein-lensing-deflection.md`, `gravity/ch01-gravity-yield/optical-refraction-gravity.md`. Companion bound on α invariance under symmetric gravity: `gravity/ch01-gravity-yield/alpha-invariance-symmetric-gravity.md`. Supporting derivation chain (continuum-mechanics origin of $\nu_{vac} = 2/7$ and the $1/7$ projection): `gravity/ch01-gravity-yield/trace-reversal-mechanism.md`, `gravity/ch01-gravity-yield/topological-packing-fraction.md`, `gravity/ch01-gravity-yield/one-seventh-impedance-projection.md`, `gravity/ch03-macroscopic-relativity/cauchy-implosion-resolution.md`, `gravity/ch03-macroscopic-relativity/gordon-optical-metric.md`. Newtonian / equivalence-principle reduction: `gravity/ch03-macroscopic-relativity/ponderomotive-equivalence.md`, `gravity/ch03-macroscopic-relativity/newtonian-gravity-optical-gradient.md`. Yield/lifetime scale (kinetic point-yield, static nodal tension, leaky-cavity decay): `gravity/ch01-gravity-yield/kinetic-yield-threshold.md`, `gravity/ch01-gravity-yield/static-nodal-tension.md`, `gravity/ch01-gravity-yield/leaky-cavity-decay.md`. Achromatic / impedance-matched lensing and frame-dragging consequences: `gravity/ch03-macroscopic-relativity/achromatic-impedance-matching.md`, `gravity/ch03-macroscopic-relativity/gravitomagnetism-frame-dragging.md`, `gravity/ch02-general-relativity/gravitational-refractive-index-gradient.md`, `gravity/ch02-general-relativity/frame-dragging-impedance-convolution.md`, `gravity/ch02-general-relativity/k4-tlm-lensing-validation.md` (numerical cross-check via TLM lattice).

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Gravitational Wave Propagation — Invariant Impedance
<!-- id: 07kd5v -->

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

> **Leaf references:** `gravity/ch08-gravitational-waves/invariant-gravitational-impedance.md`, `gravity/ch08-gravitational-waves/gw-propagation-lossless.md`, `gravity/ch08-gravitational-waves/ligo-gw-saturation-ratio.md`, `gravity/ch02-general-relativity/einstein-field-equation.md`. Detection-side consequences (impedance perturbation, Fabry-Perot phase accumulation, SQL, antenna framing — all read out the lossless propagation result): `gravity/ch08-gravitational-waves/gw-impedance-perturbation.md`, `gravity/ch08-gravitational-waves/fabry-perot-phase-shift.md`, `gravity/ch08-gravitational-waves/standard-quantum-limit.md`, `gravity/ch08-gravitational-waves/gw-detection-antenna.md`.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Black Hole Interior — Lattice Phase Transition, Not Impedance Mismatch
<!-- id: ir8h78 -->

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

> **Leaf references:** Primary for $\Gamma = 0$ (BH boundary absorbs, no reflection): `cosmology/ch15-black-hole-orbitals/electron-bh-isomorphism.md` (states "no impedance mismatch and no reflection coefficient ($\Gamma = 0$ everywhere)"). Phase-transition / saturation framing: `cosmology/ch15-black-hole-orbitals/interior-singularity-resolution.md`, `gravity/ch03-macroscopic-relativity/dielectric-rupture-event-horizon.md`. Constructive vs destructive interior asymmetry (electron preserves topology, BH destroys it — direct statement of the framing): `cosmology/ch15-black-hole-orbitals/constructive-destructive-paradox.md`. Note: `cosmology/ch04-generative-cosmology/black-holes-impedance-mismatch.md` carries "$\Gamma = -1$" in its title and uses different framing — see followups (interpretive tension between leaves on horizon impedance). Cross-cutting: see Symmetric vs Asymmetric Saturation.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## AVE Compactness Limit ($2/7$ vs Buchdahl)
<!-- id: x19btt -->

- $R > 7GM/c^2 \;\Longleftrightarrow\; 2GM/(c^2 R) < 2/7 = \nu_{vac}$
- _Specific Claims_
  - The lattice cannot support $\varepsilon_{11} > 1$; any static configuration with surface radius $R < 7GM/c^2$ has its surface inside Regime IV (ruptured).
  - This bound is **stricter** than the GR Buchdahl bound ($2GM/(c^2 R) < 8/9 \approx 0.889$). AVE limit: $2/7 \approx 0.286$.
  - A 1.4 $M_\odot$ neutron star at $R = 10$ km has $\varepsilon_{11} = 1.46 > 1$, implying a Regime-IV core with a Regime-III crust held by the saturation phase transition. This is consistent with the established quark-matter / colour-superconductor picture but is **not derived from observation**; it is what the AVE bound implies given the canonical NS parameters.
- _Specific Non-Claims and Caveats_
  - Does NOT claim AVE has been validated against observed neutron star equation-of-state data. The compactness statement is a kinematic upper bound on lattice strain, not a competing EOS calculation.
  - Does NOT claim the Buchdahl bound is wrong — AVE is **strictly more restrictive** within its own framework, but the GR bound remains valid in standard GR.
  - The recurrence of $2/7 = \nu_{vac}$ across packing fraction, compliance modes, Hubble derivation, and compactness is a **scale-invariance claim** (the same Poisson ratio projecting through K4/SRS geometry), not an empirical numerology coincidence — but treat the recurrence as an interpretive thread, not as independent evidence for any single instance.

> **Leaf references:** `cosmology/ch15-black-hole-orbitals/ave-compactness-limit.md`, `gravity/ch01-gravity-yield/vacuum-poisson-ratio.md`.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## AVE Merger Ringdown $\omega_R M_g = 18/49$
<!-- id: 395gps -->

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

> **Leaf references:** `cosmology/ch15-black-hole-orbitals/ave-merger-ringdown-eigenvalue.md`, `cosmology/ch15-black-hole-orbitals/qnm-quality-factor.md`. Phase-transition derivation of $Q = \ell$ and $\omega_I M_g = 9/98$ with axiom coverage table and three-event LIGO ringdown comparison: `cosmology/ch15-black-hole-orbitals/axiom-coverage-audit.md`. Sister standing-wave construction at the same scale (accretion-disk impedance bands, QPOs, cross-scale "photon" emission, EHT/iron-line/jet/GW-memory predictions — all derive the impedance-orbital framing the ringdown belongs to): `cosmology/ch15-black-hole-orbitals/accretion-disk-resonance.md`, `cosmology/ch15-black-hole-orbitals/qpo-frequency-impedance-resonance.md`, `cosmology/ch15-black-hole-orbitals/cross-scale-emission.md`, `cosmology/ch15-black-hole-orbitals/first-principles-predictions.md`.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Hawking Temperature as Classical Nyquist Noise
<!-- id: c6k5om -->

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

> **Leaf references:** `cosmology/ch15-black-hole-orbitals/hawking-temperature-nyquist-noise.md`, `cosmology/ch04-generative-cosmology/black-holes-impedance-mismatch.md`.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## MOND Acceleration Scale $a_0$ (Derived but Regime-Gated)
<!-- id: u86caq -->

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

> **Leaf references:** `cosmology/ch05-dark-sector/derived-mond-acceleration-scale.md`, `cosmology/ch05-dark-sector/effective-galactic-acceleration-mond.md`, `cosmology/ch05-dark-sector/asymptotic-limits.md`, `cosmology/ch05-dark-sector/multi-galaxy-validation.md`. Empirical interpolation matched against the Axiom 4 saturation form (asymptotes coincide; deep-MOND and Newtonian limits identical): `cosmology/ch05-dark-sector/mcgaugh-empirical-rar.md`. Galactic-scale realisation of the saturation operator on the lattice mutual inductance — the same kernel used at particle-confinement scale: `cosmology/ch05-dark-sector/saturated-lattice-mutual-inductance.md`.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Anomalous Perihelion Advance — Consistency Check
<!-- id: qyn8t0 -->

- $\Delta\phi = 6\pi G M_\odot / (c^2 a (1-e^2))$
- _Specific Claims_
  - The standard GR perihelion advance formula is reproduced via a $1/r^3$ tidal correction to the Newtonian potential, derived from the asymmetric impedance gradient of the displaced LC medium.
  - For Mercury, this gives $\sim 43$ arcsec/century — identical to GR; a category (iii) consistency check.
  - The framework asserts no "curved spacetime" is required; the same observable arises from mechanical impedance asymmetry.
- _Specific Non-Claims and Caveats_
  - Does NOT claim a novel numerical prediction distinguishable from GR for perihelion advance.
  - Does NOT claim the AVE derivation is independently confirmed against observational data beyond what already validates GR. This is reproduction-via-alternative-mechanism, with the same testable consequences as GR for the precession test.

> **Leaf references:** `cosmology/ch14-orbital-mechanics/anomalous-perihelion-advance.md`. Cross-scale orbital regime classification (Mercury, Saturn, solar flares, heliopause — same control parameter $\varepsilon_{11}$; Mercury entry is the perihelion test): `cosmology/ch14-orbital-mechanics/orbital-regime-table.md`. Sister classical-mechanics derivations using the same $1/d$ mutual-impedance topology — Saturn ring gaps as standing-wave cancellation zones, solar flares as a forward-biased macroscopic LED with Shockley-avalanche I–V and the empirical 0.46-yr FWHM "danger zone": `cosmology/ch14-orbital-mechanics/saturn-ring-integrator.md`, `cosmology/ch14-orbital-mechanics/solar-flares-led-avalanche.md`, `cosmology/ch14-orbital-mechanics/macroscopic-avalanche-transconductance.md`.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Solar System Boundaries (Oort, Kirkwood, Magnetopause)
<!-- id: 3kmt3p -->

- _Specific Claims_
  - Oort Cloud inner edge: $r_{sat} = \sqrt{GM_\odot/a_0} \approx 7{,}400$ AU — the radius where solar $g_N$ drops to the MOND threshold. Falls within the observed Hills Cloud range (2,000–5,000 AU); reported as "consistent with" rather than as a sub-percent match.
  - Kirkwood gaps: cavity-mode formula $a_{gap} = a_J (q/p)^{2/3}$ reproduces all five major gaps to $< 0.3\%$.
  - Planetary magnetopause: standoff radius from pressure balance $B^2/(2\mu_0) = (1/2)\rho_{sw} v_{sw}^2$ — Earth at 8.7%, Jupiter at 11.8% (Master Prediction Table #20, #21).
- _Specific Non-Claims and Caveats_
  - Magnetopause errors of 8.7% (Earth) and 11.8% (Jupiter) are not sub-percent; do not summarise these as "exact".
  - The Kirkwood-gap formula is the standard mean-motion-resonance result reinterpreted as an impedance cavity mode — a category (iii) consistency check, not a novel mechanism distinguishable from classical resonance theory.
  - Oort Cloud derivation depends on the $a_0$ prediction (which itself carries 10.7% systematic deficit; see MOND entry).

> **Leaf references:** `cosmology/ch06-solar-system/oort-cloud-saturation-boundary.md`, `cosmology/ch06-solar-system/kirkwood-gaps-cavity-modes.md`, `cosmology/ch06-solar-system/planetary-magnetopause-standoff.md`. Magnetopause-pressure / standing-wave construction (Chapman-Ferraro $B_{eff} = B_{dipole}(1 + |\Gamma|)$, dipole loss-cone trapped fraction, full per-planet table including Saturn/Uranus/Neptune): `cosmology/ch06-solar-system/chapman-ferraro-enhancement.md`, `cosmology/ch06-solar-system/dipole-loss-cone-fraction.md`, `cosmology/ch06-solar-system/planetary-magnetospheres.md`. Heliospheric impedance profile / heliopause as impedance boundary at $\sim 120$ AU: `cosmology/ch06-solar-system/heliospheric-impedance-profile.md`. Two-Winds decoupling (plasma magnetopause vs gravitational stator; Venus/Mars as control group) — frames *which* boundary the magnetopause result is about and isolates it from orbital coupling: `cosmology/ch06-solar-system/plasma-standoff-vs-gravitational-stator.md`. Lossless-orbit consistency at the same scale (no LC drag in Regime I; supports "no anomalous orbital decay" caveat): `cosmology/ch06-solar-system/orbital-lc-friction-paradox.md`. Single-body anomaly handled by ordinary radiation pressure on a high $A/m$ body (zero-free-parameter 91% match): `cosmology/ch06-solar-system/oumuamua-acceleration.md`.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Flyby Anomaly — Sagnac Shear Reinterpretation
<!-- id: a71inj -->

- $\Delta V_{flyby} = V_\infty \cdot 2 (U_\oplus / c_0) \cos(\alpha_{geo}) \cos(\delta_{geo}) \approx 13.4$ mm/s
- _Specific Claims_
  - The flyby anomaly is interpreted as a Sagnac-RLVE shear-layer phase slip at the Earth's rotational boundary.
  - The pure geometrical formula yields $\sim 13.4$ mm/s without fitting parameters.
  - The leaf claims this **falsifies Lense-Thirring** as the mechanism (LT predicts an effect $\sim 10^6 \times$ smaller than observed).
- _Specific Non-Claims and Caveats_
  - Does NOT claim per-event match across Pioneer, Galileo, NEAR with quoted error bars. The leaf names those three missions as the empirical anomalies "resolved precisely" but gives only a single representative magnitude; per-event validation is asserted rather than tabulated.
  - "Falsifies Lense-Thirring" applies to the Lense-Thirring **mechanism for flyby anomalies specifically** (where the magnitudes disagree by $10^6$); does NOT claim Lense-Thirring is falsified as a gravitomagnetic effect generally.
  - The $\Gamma_{sagnac} \approx 1836$ acoustic shear factor reused in lunar/geodynamo derivations is a numerical coincidence with the proton/electron mass ratio asserted as cross-scale; this is a structural claim, not an independent derivation per application.

> **Leaf references:** `cosmology/ch14-orbital-mechanics/flyby-anomaly-sagnac-operator.md`.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Lunar Inductive Heating — Tidal Inputs Required
<!-- id: av2o4v -->

- $P_{topo} \approx 1.04$ TW via $\Gamma_{sagnac}$ amplification of standard tidal formula
- _Specific Claims_
  - Reproduces the empirical $\sim 1$–$2$ TW lunar heat budget that classical tidal-friction models underpredict by $\sim 1000\times$.
  - The $\sim 1000\times$ amplification is identified as the same $\Gamma_{sagnac}$ acoustic-shear factor used in flyby and geodynamo derivations.
- _Specific Non-Claims and Caveats_
  - Does NOT claim a parameter-free derivation of the lunar heat budget. The formula **uses** the Love number $k_2 \approx 0.022$ and dissipation $Q \approx 38$ as inputs — these are empirical lunar quantities, not AVE-derived.
  - The $\Gamma_{sagnac} \approx 1836$ factor is reused across applications without per-application derivation; treat its appearance here as cross-scale consistency, not as an independent prediction.

> **Leaf references:** `cosmology/ch14-orbital-mechanics/lunar-inductive-heating.md`.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Geodynamo as VCA Back-EMF
<!-- id: wd5rs0 -->

- $M_\oplus \approx 1.5 \times 10^{23}$ A·m² vs empirical $8.0 \times 10^{22}$ A·m²
- _Specific Claims_
  - Earth's magnetic dipole moment is recovered from a structural AC-motor formula combining solar-wind magnetopause $B$, Earth's core radius/conductivity, and the same $\Gamma_{sagnac} \approx 1836$ baryon-phase shear factor.
  - Falsifiability via Venus (slow rotation → no Sagnac amplification → near-zero field) and Mars (solid core → infinite DC resistance → collapsed eddy current).
- _Specific Non-Claims and Caveats_
  - Numerical match is $\sim 2\times$ the empirical value ($1.5 \times 10^{23}$ vs $8.0 \times 10^{22}$), not sub-percent. Treat as order-of-magnitude consistency, not a precision derivation.
  - The Venus/Mars "natural failures" are qualitative consistency arguments, not independent quantitative predictions of those bodies' field strengths.
  - The $\Gamma_{sagnac} = \mu_B \approx 1836$ identification (proton/electron mass ratio doubling as baryonic-phase-boundary acoustic shear) is asserted, not derived in this leaf.

> **Leaf references:** `applied-physics/ch13-geophysics/geodynamo-vca-back-emf.md`.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Sonoluminescence as Tabletop Relativity
<!-- id: 91adfe -->

- $\rho_{eff} = \rho_0 / (1 - \mathrm{M}^2)^{3/2}$, Mach number $\mathrm{M} = |\dot{R}|/c_{sound}$
- _Specific Claims_
  - The Rayleigh-Plesset bubble-collapse equation with $\rho_0 \to \rho_{eff}$ (Axiom 4 saturation in the acoustic medium) autonomously halts before $R = 0$ via the Mach $\to 1$ topological wall.
  - The $3/2$ exponent (vs the standard $1/2$ Lorentz factor) arises from longitudinal inertia in 3D spherical collapse.
  - This is presented as an **acoustic emulation** of Special Relativity, not literal SR — Axiom 4 has the same structural form across acoustic / EM / gravitational media.
- _Specific Non-Claims and Caveats_
  - Does NOT claim sonoluminescence experimentally validates Special Relativity. The mapping is structural (same kernel form), not phenomenological.
  - Pure-vapor "bubble interior emulates a black-hole transition" is a Regime-III→IV identification at the acoustic scale; does NOT claim physically equivalent thermodynamics or that the bubble core is a literal BH analog beyond the saturation operator.
  - Flash temperatures vary with payload gas (ionization-energy gated); the table gives ranges, not point predictions.

> **Leaf references:** `applied-physics/ch14-sonoluminescence/sonoluminescence-derivation.md`.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Superconductor Type Classification ($\kappa = \lambda_L/\xi_0$)
<!-- id: qky559 -->

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

> **Leaf references:** `condensed-matter/ch09-condensed-matter-superconductivity/superconductor-type-classification.md`, `condensed-matter/ch09-condensed-matter-superconductivity/critical-field-validation.md`, `condensed-matter/ch09-condensed-matter-superconductivity/bcs-alternative-framework.md`, `condensed-matter/ch09-condensed-matter-superconductivity/universal-saturation-operator.md`. Phase-locking mechanism — Kuramoto order parameter + classical gear-train derivation of the London penetration depth as static rejection of boundary torque: `condensed-matter/ch09-condensed-matter-superconductivity/kuramoto-phase-locking.md`, `condensed-matter/ch09-condensed-matter-superconductivity/meissner-gear-train.md`, `condensed-matter/ch09-condensed-matter-superconductivity/inertial-london-penetration-depth.md`. Five-material catalog (Al, Pb, Nb, MgB$_2$, YBCO) with the regime classification — note the catalog limitation on Nb's $n_s$ documented in this entry's caveats: `condensed-matter/ch09-condensed-matter-superconductivity/superconductor-catalog-predictions.md`. Cross-cutting: see BCS Critical Field $B_c(T)$.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Effective Degrees of Freedom $g_* = 343/4 = 85.75$
<!-- id: uu6dl5 -->

- $g_* = n^3/N_{K4} = 7^3/4 = 85.75$
- _Specific Claims_
  - The lattice-derived effective DoF replaces SM $g_{*,SM} = 106.75$. With $g_* = 85.75$, the baryon asymmetry formula yields $\eta = 6.08 \times 10^{-10}$ vs observed $6.1 \times 10^{-10}$ (0.38% error).
  - Using $g_{*,SM} = 106.75$ in the same formula yields 20% error, asserted as evidence that the lattice count is the correct DoF count for cosmological thermodynamics.
- _Specific Non-Claims and Caveats_
  - Does NOT claim the SM particle catalog is wrong — claims that the **DoF-counting metric for cosmological partition** uses lattice modes (7 compliance × $7^2$ angular sectors / 4 K4 cell) rather than particle species count.
  - The 0.38% baryon asymmetry agreement uses $g_* = 85.75$ together with $\alpha_W^4$, $C_{sph} = 28/79$, and $\kappa_{FS} = 8\pi$ — a multi-factor formula with several lattice-derived inputs. Treat the 0.38% as a composite consistency check, not a single-quantity prediction.
  - Does NOT claim $g_* = 85.75$ is a separately measurable cosmological observable; the validation is via the downstream baryon ratio.

> **Leaf references:** `condensed-matter/ch11-thermodynamics/effective-dof-g-star.md`, `condensed-matter/ch11-thermodynamics/baryon-asymmetry.md`, `condensed-matter/ch11-thermodynamics/baryon-asymmetry-derivation.md`, `condensed-matter/ch11-thermodynamics/thermal-softening-correction.md`. Mode-counting derivation $g_* = n^3/N_{K4}$ with the 7-mode compliance manifold and equipartition pathway to the vacuum heat capacity (extracted bare-resultbox companion): `condensed-matter/ch11-thermodynamics/mode-counting-heat-capacity.md`, `condensed-matter/ch11-thermodynamics/vacuum-heat-capacity.md`. Independent thermal-softening derivation (Faddeev-Skyrme coupling) — uses $\nu_{vac}/\kappa_{cold} \times 2/\pi = 1/(14\pi^2)$, the same lattice geometry: `condensed-matter/ch11-thermodynamics/thermal-softening-skyrme.md`.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Kolmogorov Spectral Cutoff and Bounded Enstrophy
<!-- id: hk81zp -->

- $k_{\max} = \pi/\ell_{node}$; $E(k) = C_K \varepsilon^{2/3} k^{-5/3} S(k/k_{\max})$; $n_{3D} = 38/21$
- _Specific Claims_
  - The lattice pitch sets a hard wavenumber ceiling; the Axiom 4 saturation envelope rolls the inertial spectrum smoothly to zero before the cutoff.
  - The 3D avalanche exponent $n_{3D} = 2(1 - \nu_{vac}/3) = 38/21 \approx 1.8095$ — within $\sim 0.5\%$ of empirical solar-flare measurements.
  - On a finite discrete lattice, total enstrophy is rigorously bounded by $Z_{max} = 2Nc^2 \, dx$ — claimed as a **constructive resolution** of Navier-Stokes global regularity within the AVE discrete framework.
- _Specific Non-Claims and Caveats_
  - Does NOT claim a Clay-rigorous proof of Navier-Stokes regularity in the continuum. The claim is **lattice-conditional**: bounded on any finite discrete lattice, by virtue of the lattice cutoff itself. See LIVING_REFERENCE.md Master Prediction Table notes #14, #15 for Yang-Mills and NS framework-derived (not Clay-rigorous) caveats — same caveat applies here.
  - Does NOT claim $n_{3D} = 38/21$ is the universal turbulence exponent; the agreement is with solar-flare avalanche statistics specifically, and the comparison is to "$\sim 1.8$" (single empirical figure), not a precision dataset.
  - The Kolmogorov constant $C_K = 1.5$ is the classical empirical value; the framework asserts compatibility, not a new derivation.

> **Leaf references:** `condensed-matter/ch11-thermodynamics/kolmogorov-spectral-cutoff.md`.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Per-Element Impedance Table (Two Families)
<!-- id: nxfmh0 -->

- _Specific Claims_
  - Diagonalising the nuclear Hessian for Z = 1–14 yields a binary partition: closed-shell alpha cores ($Z_{atom} \approx 1.37$, $Q = 2.0$, $E_{rupt} \approx 0.82$ MeV) vs open-shell halo elements ($Z_{atom} \sim 0.37$–$0.46$, $Q = 3$–$16$, $E_{rupt} \ll 0.82$).
  - The alpha-core family (He-4, C-12, O-16, Ne-20, Mg-24, Si-28) is structurally identified as built from tetrahedral alpha clusters; $Q = 2.0$ is the tetrahedral-symmetry signature.
  - Inter-element bonding via the same `reflection_coefficient(Z₁, Z₂)` operator: same-family $|\Gamma| \to 0$ (resonant), cross-family $|\Gamma| \sim 0.5$ (ionic).
- _Specific Non-Claims and Caveats_
  - Does NOT claim numerical match of $K_{bulk}$, $G_{shear}$, $E_{rupt}$ to experimental bulk-modulus / shear-modulus / rupture-energy values per element. The table lists eigenvalue **proxies** of the lattice Hessian, not direct experimental moduli.
  - The two-family classification is a structural / qualitative claim; cross-family $|\Gamma|$ being "ionic" is a structural identification, not a quantitative bonding-energy derivation.
  - Hydrogen-1 has no characterisation (single nucleon, no Hessian).

> **Leaf references:** `condensed-matter/ch10-material-properties/per-element-impedance-table.md`, `condensed-matter/ch10-material-properties/nuclear-hessian.md`. Inter-element bonding via the universal `reflection_coefficient(Z_i, Z_j)` operator (intra-family $|\Gamma| \to 0$ covalent/metallic, cross-family $|\Gamma| \sim 0.5$ ionic): `condensed-matter/ch10-material-properties/inter-element-reflection-coefficient.md`. Macroscopic-hardness consequence (diamond as tri-alpha tetrahedral metamaterial, helium-metamaterial paradox resolution via internal flux routing): `condensed-matter/ch10-material-properties/diamond-hardness-alpha-clusters.md`, `condensed-matter/ch10-material-properties/helium-metamaterial-paradox.md`. Metallicity from magnetic susceptibility threshold ($\chi_{crit} \approx 0.3$): `condensed-matter/ch10-material-properties/metallicity-magnetic-asymmetry.md`. Caveat: the macroscopic dilution factor in the diamond-hardness derivation ($\sim 10^{-21}$) is asserted, not derived per element; the helium and metallicity entries are structural classifications using susceptibility values from the same table whose proxy/measurement caveat is recorded above.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Dirac Large Numbers and Planck Mass
<!-- id: 1klgo2 -->

- $\alpha_G = G m_e^2 / (\hbar c) = 1/(7\xi)$; $m_P = m_e\sqrt{7\xi}$; $R_H/\ell_{node} = \alpha^2/(28\pi\alpha_G)$
- _Specific Claims_
  - The Dirac Large Numbers Hypothesis ratio between cosmological and quantum scales is **algebraically derivable** from $G = \hbar c/(7\xi m_e^2)$ via direct substitution.
  - The Planck mass becomes $m_P = m_e\sqrt{7\xi}$ — recast as the electron rest mass scaled by the cosmological geometric coupling. The leaf interprets this as: the Planck scale is **not a fundamental microscopic threshold**; the discrete quantization limit is the electron mass-gap, $\ell_{node} = \hbar/(m_e c)$.
- _Specific Non-Claims and Caveats_
  - These derivations are **algebraic identities** within the AVE definition of $G$, not independent predictions. They follow from Axiom 3 by substitution.
  - Does NOT claim a measurement of the Planck mass at $m_e\sqrt{7\xi}$ as a novel prediction — both sides match because $\xi$ was defined to make this hold, given the empirical $G$.
  - "$\ell_{node}$ is the true quantization limit (not the Planck length)" is a **framework-internal interpretive** claim about which length scale is fundamental; it does not introduce new observables vs the standard Planck-length picture.

> **Leaf references:** `gravity/ch01-gravity-yield/gravitational-coupling-constant.md`, `gravity/ch01-gravity-yield/asymptotic-hubble-constant.md`, `gravity/ch01-gravity-yield/planck-mass.md`, `gravity/ch01-gravity-yield/optical-refraction-gravity.md`.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## JWST Exponential Accretion Time Constant $\tau_{ind} \approx 65.1$ Myr
<!-- id: 9fnieq -->

- $M(t) = M_{seed} e^{t/\tau_{ind}}$
- _Specific Claims_
  - The framework predicts an exponential mass-growth law from mutual-inductive accretion in the dense early-universe lattice, in contrast to $\Lambda$CDM's $M \propto t^{2.5}$.
  - This makes the JWST early-galaxy observations compatible with AVE without invoking modified initial conditions.
- _Specific Non-Claims and Caveats_
  - $\tau_{ind} \approx 65.1$ Myr is **fitted to the JWST data** (constrained by the requirement that $M$ grow from $10^{10} M_\odot$ at $t = 350$ Myr to $10^{11} M_\odot$ at $t = 500$ Myr). It is **not** an independent prediction from axioms.
  - The framework supplies the *form* (exponential), not the *time constant*. Treat $\tau_{ind} = 65.1$ Myr as a derived consequence of the form fit to two data points, not an axiom-derived numerical prediction.

> **Leaf references:** `cosmology/ch04-generative-cosmology/jwst-constraint-equation.md`, `cosmology/ch04-generative-cosmology/mutual-inductive-accretion-time-constant.md`.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Phantom Energy Equation of State $w < -1$
<!-- id: 3ii690 -->

- $w_{vac} = -1 - \rho_{latent}/\rho_{vac}$
- _Specific Claims_
  - "Dark energy" is reinterpreted as the latent heat of continuous lattice crystallisation; positive $\rho_{latent}$ guarantees $w < -1$ (phantom regime).
  - The framework forbids the Big Rip singularity within this reinterpretation.
- _Specific Non-Claims and Caveats_
  - Does NOT claim a numerical value of $w_{vac}$ to compare with observational constraints (current data: $w \approx -1$ within $\sim 0.05$; phantom regime $w < -1$ is consistent but not required).
  - "Forbids Big Rip" is a framework-internal consequence of the latent-heat injection / asymptotic Unruh-Hawking attractor; it is an interpretive prediction, not a quantitative bound on $w$ time-evolution.
  - The CMB asymptotic-attractor picture (radiation density floors at $\frac{3}{4}\rho_{latent}$, asymptoting to Unruh-Hawking $\sim 10^{-30}$ K) is structural, not numerically validated against observation.

> **Leaf references:** `cosmology/ch04-generative-cosmology/phantom-energy-equation-of-state.md`, `cosmology/ch04-generative-cosmology/cmb-thermal-attractor.md`.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Einstein Field Equation Reinterpretation
<!-- id: y9old1 -->

- $R_{\mu\nu} - \tfrac{1}{2}R g_{\mu\nu} + \Lambda g_{\mu\nu} = (8\pi G/c^4) T_{\mu\nu}$ with $T_{\mu\nu} \equiv U_{\mu\nu}$ (LC EM energy density)
- _Specific Claims_
  - AVE identifies the GR stress-energy tensor with the local LC vacuum's classical electromagnetic energy density and the metric tensor with the impedance moduli ($\varepsilon_{eff}, \mu_{eff}$).
  - This is presented as an **ontological reinterpretation** (variable scalar capacitance/inductance of a structured dielectric superfluid), not as new field equations.
  - The Schwarzschild radius $r_s$ is identified as the saturation impedance boundary where $\mu_{eff}, \varepsilon_{eff} \to 0$ — but note the cross-cutting Symmetric Saturation result: under symmetric scaling $Z = Z_0$ everywhere; "$Z \to 0$ at the horizon" is a different gauge / interpretation choice that needs care to reconcile.
- _Specific Non-Claims and Caveats_
  - Does NOT claim derivation of the Einstein equation from AVE axioms ab initio. The reinterpretation maps the **same** equation onto LC quantities; it does not produce modified field equations.
  - There is interpretive tension between "Symmetric Gravity → $Z = Z_0$ invariant" (GW propagation leaves) and "$Z \to 0$ at the horizon" (Einstein-equation leaf). The two coexist: the impedance is invariant for **transverse** propagation while the **constitutive** $\mu_{eff}, \varepsilon_{eff}$ collapse to zero at saturation. Summaries that quote one without the other create apparent contradictions.

> **Leaf references:** `gravity/ch02-general-relativity/einstein-field-equation.md`, `gravity/ch02-general-relativity/stress-energy-lc-density.md`.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Seismic Reflection Coefficient (Moho)
<!-- id: zsqh87 -->

- $\Gamma_{Moho} = (\rho_2 V_{p2} - \rho_1 V_{p1})/(\rho_2 V_{p2} + \rho_1 V_{p1}) \approx 0.29$
- _Specific Claims_
  - The seismic Moho reflection uses **the same** `reflection_coefficient(Z₁, Z₂)` operator as Pauli exclusion, plasma cutoff, superconductor boundary, and antenna $S_{11}$ — a category (i) operator-identity claim across scales.
- _Specific Non-Claims and Caveats_
  - Does NOT claim the value $\Gamma \approx 0.29$ is AVE-derived. The inputs $\rho_i, V_{pi}$ are seismological measurements; AVE asserts the **operator form** is the same one used elsewhere, not a novel numerical derivation.
  - The cross-scale operator unity is structural (same formula reused), not a prediction at any single scale.

> **Leaf references:** `applied-physics/ch13-geophysics/seismic-reflection-coefficient-moho.md`, `applied-physics/ch13-geophysics/constitutive-mapping.md`. PREM layer table with computed reflection coefficients at all major discontinuities (Moho, 670 km, CMB, ICB) and the LVZ waveguide-trapping condition: `applied-physics/ch13-geophysics/prem-layers-waveguide.md`. The same FDTD engine used elsewhere in the framework, with the constitutive mapping that lets it run seismic problems unchanged: `applied-physics/ch13-geophysics/seismic-fdtd-engine.md`.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Ideal Gas Law as LC Energy Balance
<!-- id: cul4it -->

- $U \cdot V = N \cdot k_B \cdot \overline{T_{jitter}}$ → recovers $PV = nRT$ at STP
- _Specific Claims_
  - The classical ideal gas law is reinterpreted as an LC energy-balance equation; gas pressure becomes an electromagnetic-jitter (lattice noise) phenomenon at the molecular scale.
- _Specific Non-Claims and Caveats_
  - Does NOT claim a corrected ideal gas law that deviates from $PV = nRT$. The framework reproduces the standard formula at STP — a category (iii) consistency check via reinterpreted variables.
  - The mapping introduces no new measurable predictions at the macroscopic gas-law level; deviations would appear (if at all) only in regimes where lattice-noise structure becomes resolvable.

> **Leaf references:** `applied-physics/ch12-ideal-gas-law/ideal-gas-law.md`, `applied-physics/ch12-ideal-gas-law/lc-energy-balance-equation.md`, `applied-physics/ch12-ideal-gas-law/recovering-r-at-stp.md`. Ontological mapping (P, V, n, R, T translated into LC-grid quantities — the framing the entry's reinterpretation rests on): `applied-physics/ch12-ideal-gas-law/gas-dynamics-foundations.md`.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Neutrino MSW Matter Potential
<!-- id: o6kgkz -->

- $V_{CC} = \sqrt{2}\, G_F\, n_e$
- _Specific Claims_
  - The standard MSW charged-current matter potential is reproduced from AVE-derived $G_F$ (3.9% accurate per LIVING_REFERENCE.md and Master Prediction Table #13 at 2.09%).
- _Specific Non-Claims and Caveats_
  - Does NOT claim a novel matter-potential formula. The leaf reproduces the SM expression; the AVE input is the value of $G_F$, not the form of the potential.
  - LIVING_REFERENCE.md Critical Distinctions #5 caveat applies: SPICE RC muon model is qualitative; quantitative neutrino-related lifetimes go through the standard Fermi formula with AVE $G_F$.
  - The flavor-mixing energy-dependent table (pp / $^7$Be / $^8$B) reports agreement with Borexino/SNO; treat as consistency with the SM-MSW prediction using AVE $G_F$, not as an independent AVE-only validation.

> **Leaf references:** `applied-physics/ch07-stellar-interiors/neutrino-msw-matter-potential.md`. Resonance-density companion ($n_e^{res}$ from $\Delta m^2$ and $G_F$, energy-dependent flavor-mixing validation table): `applied-physics/ch07-stellar-interiors/msw-resonance-critical-density.md`, `applied-physics/ch07-stellar-interiors/neutrino-flavor-mixing.md`. Stellar-interior context the resonance lives in (radial impedance profile, tachocline as impedance boundary using the universal `reflection_coefficient`, helioseismology cavity resonance, regime classification of stellar objects): `applied-physics/ch07-stellar-interiors/stellar-interior-impedance-profiles.md`, `applied-physics/ch07-stellar-interiors/stellar-regime-classification.md`.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Thermodynamics as LC Mechanics — Temperature, Entropy, Arrow of Time
<!-- id: t05mvx -->

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

> **Leaf references:** `condensed-matter/ch11-thermodynamics/macroscopic-temperature-lc-noise.md`, `condensed-matter/ch11-thermodynamics/entropy-redefinition.md`, `condensed-matter/ch11-thermodynamics/arrow-of-time.md`.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Phase Transitions as Impedance Matching Events
<!-- id: refjr6 -->

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

> **Leaf references:** `condensed-matter/ch11-thermodynamics/phase-transitions-impedance.md`, `condensed-matter/ch11-thermodynamics/phase-transition-classification.md`, `condensed-matter/ch11-thermodynamics/casimir-effective-temperature.md`.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Vacuum Nyquist Baseline and Boundary Thermalization
<!-- id: eaiqj1 -->

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

> **Leaf references:** `condensed-matter/ch11-thermodynamics/nyquist-noise-fdt.md`, `condensed-matter/ch11-thermodynamics/vacuum-nyquist-baseline.md`, `condensed-matter/ch11-thermodynamics/transmon-decoherence.md`.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Water $4\,^{\circ}$C Anomaly via Two-State LC Partition
<!-- id: jpfbm6 -->

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

> **Leaf references:** `condensed-matter/ch11-thermodynamics/water-anomaly-lc-partition.md`. Cross-volume primaries (loaded by the leaf, not duplicated): `vol5/molecular-foundations/organic-circuitry/hbond-op4-equilibrium.md` (Op4 H-bond, $d_{OO} = 2.727\,\text{\AA}$), `vol7/condensed-matter/ch4-phase-transitions/s03-melting-eigenmode.md` (melting eigenmode $T_m = 279.5$ K).

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*