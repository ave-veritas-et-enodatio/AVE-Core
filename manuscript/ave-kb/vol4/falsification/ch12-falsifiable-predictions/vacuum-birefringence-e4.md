[↑ Ch.12: Falsifiable Predictions](../index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-pp3qwf, clm-sve3xc]
-->

> 🔴 **QED-NORMALIZATION CORRECTION (2026-07-03; Rule-12 — body preserved below, git is the trail).**
> The QED denominator of the matched-differential ratio in this leaf, $\delta n_{QED}=(3/45)\alpha^2(E/E_{crit})^2$,
> is **understated by exactly $1/(2\pi\alpha)\approx21.8$**. Two independent external arbiters fix it:
> **(a)** the module's OWN PVLAS-anchored magnetic leg ($3A_e B^2$, $A_e=1.32\times10^{-24}$ T$^{-2}$, textbook) —
> at the $E\leftrightarrow cB$ duality point the leading Euler-Heisenberg $(E^2-B^2)^2$ invariant gives IDENTICAL
> differentials, so the electric coefficient MUST equal $3A_eB_{crit}^2=\alpha/(30\pi)=1.454\,\alpha^2$, NOT
> $3/45=0.0667\,\alpha^2$; **(b)** the BIREF@HIBEF LoI Eq.19 (focus-integrated) reproduces $\sim10^{-12}$ at
> $10^{21}$ W/cm$^2$ and implies, for a **propagating** plane-wave pump, $\alpha/(15\pi)$ (a further factor 2).
> **Corrected ratio:** $\delta n_{AVE}/\delta n_{QED}=\mathbf{7.5\pi/\alpha^2\approx4.42\times10^5}$ (propagating,
> LoI-matched, the headline) or $15\pi/\alpha^2\approx8.85\times10^5$ (pure-static-E duality). The **AVE leg
> $-\tfrac12 A^2$ is UNAFFECTED** (independently re-derived); only the QED co-prediction and the ratio change.
> **Falsifier LOGIC survives intact:** AVE flip-prob $\sim5\times10^{-3}$ still sits $\sim7$ OOM above the
> $\sim10^{-10}$ polarimeter floor; the corrected QED flip-prob ($\sim3\times10^{-14}$ single-pass) still sits
> $\sim4$ OOM below it. Every "$7.5/\alpha^3$", "$1.93\times10^7$", and "$4.14\times10^6$" (single-arm) below is
> superseded by the corrected values. Reconciliation harness: `src/ave/bench/birefringence.py`
> (`delta_n_qed_electric_pvlas`, `coefficient_ratio_differential_pvlas`).

> 🔵 **FOOTING RE-FREEZE (2026-07-05; Grant-ratified via the Letter v2 Arm-2 round — KEEP-BOTH, the
> $7.5\pi/\alpha^2$ value above is preserved as v1 convention history).** The QED-normalization header
> above quotes $\mathbf{7.5\pi/\alpha^2\approx4.42\times10^5}$ as the propagating headline. That value
> pairs the **instantaneous** SVE kernel ($-\tfrac12(E/E_c)^2$, algebraic in $|E|^2$ at the pump) against
> the **cycle-averaged** one-loop coefficient $\alpha/(15\pi)$ — a **mixed temporal footing**. The
> flagship Letter re-froze the headline to a **single consistent footing** (both coefficients
> instantaneous / peak-field), pairing the instantaneous SVE kernel against the **instantaneous** one-loop
> coefficient $2\alpha/(15\pi)$ [the $\alpha/(15\pi)$ headline is its $\langle\cos^2\rangle=\tfrac12$
> carrier average]:
> $$\boxed{\;\frac{\delta n_{AVE}}{\delta n_{QED}}=\frac{\tfrac12}{2\alpha/(15\pi)}\left(\frac{E_{crit}}{E_c}\right)^2=\frac{15\pi}{4\alpha^2}=\frac{3.75\pi}{\alpha^2}\approx2.2\times10^5\;}$$
> — **exactly HALF** the mixed-footing $7.5\pi/\alpha^2$, the difference being precisely the
> $\langle\cos^2\rangle=\tfrac12$ carrier average. **The $7.5\pi/\alpha^2$ value is KEEP-BOTH-preserved
> above as v1 convention history**, not deleted (the OTS anchor is on the v1 content; git is the trail).
> The **static-to-propagating decomposition** carried by the QED-normalization header — $\alpha/(30\pi)$
> (static $E\leftrightarrow cB$ duality) $\xrightarrow{\times4}$ $2\alpha/(15\pi)$ (head-on crossing
> geometry, the birefringence living in the pump--probe cross terms) $\xrightarrow{\times\tfrac12}$
> $\alpha/(15\pi)$ (carrier average) — is the same $\times4$-geometry $\times\tfrac12$-carrier chain; the
> instantaneous headline stops it at the $2\alpha/(15\pi)$ step (no carrier average), which is why the
> consistent-footing ratio is a factor 2 below the mixed one. **No order of magnitude and no falsifier
> verdict changes** (the SVE $P_{flip}\sim5\times10^{-3}$ headline is footing-invariant; the kill
> criterion $P_{flip}<10^{-8}$ is unchanged). Provenance: the flagship Letter's
> `papers/2026_birefringence_letter/provenance.md` §9 (Arm-2 re-freeze, Grant ruling verbatim) and §10
> (electrostatic-sector scope round). The Letter's own §II.B honesty-item (iv) carries both footings
> with the $7.5\pi/\alpha^2$ mixed value ledgered as convention history.

## The Vacuum Birefringence Limit: the COEFFICIENT (AVE $\sim 10^7\times$ QED at the matched differential observable)
<!-- claim-quality: clm-pp3qwf (this section is the canonical statement of the E-route field-induced birefringence COEFFICIENT discriminator — the matched par−perp differential δn≈−½A² vs QED's differenced Euler-Heisenberg) -->

> **Route scope (E-route only; DERIVED via the node-up dual).** This birefringence prediction is
> the **static-E (E-route)** prediction: it requires biasing the **$V$-keyed varactor**
> ($\varepsilon$-grade, operating-point regime R2), which a static (or DC-biased) electric field does.
> A **static $\mathbf B$ does NOT produce this birefringence** — the $\mu$-grade is an ideal
> relativistic inductor keyed on the circulating current $I$, so a static $\mathbf B$
> ($\partial\mathbf B/\partial t=0$) leaves it unloaded ($S_\mu=1$, $\delta n_\mu = 0$ exactly). The
> node-up small/large-signal derivation
> ([`node-up-small-large-signal.md`](../../circuit-theory/ch1-vacuum-circuit-analysis/node-up-small-large-signal.md):§2–§4)
> supplies this E-route scope; the static-B null verdict (PVLAS/BMV **consistent** with AVE, plus the
> **bold no-static-B side-prediction**) is canonical at
> [`pvlas-static-b-verdict.md`](../ch11-experimental-bench-falsification/pvlas-static-b-verdict.md).
> **Side-prediction:** AVE predicts NO static-B vacuum birefringence at any field strength; the
> matched differential E-route ratio is $\delta n_{AVE}/\delta n_{QED}=7.5/\alpha^3\approx1.93\times10^7$.

A core distinction between standard Quantum Electrodynamics (QED) and the Applied Vacuum Engineering (AVE) framework is the *magnitude* of vacuum optical nonlinearity under extreme fields — not its leading power. **Both predict an $E^2$-leading index shift; the discriminator is the COEFFICIENT.**

A birefringence instrument (polarimeter / ellipsometer, PVLAS/BMV lineage) measures the **DIFFERENCE** $n_\parallel - n_\perp$ between the two polarization eigenmodes of the pumped vacuum — a pure phase/interference observable. The isotropic (common-mode) index shift, shared by both eigenmodes, is **rejected by the instrument**. The falsifier observable is therefore the *differential*, and the AVE-vs-QED comparison must be made differential-against-differential (matched observables).

Under a linearly-polarized pump, the AVE vacuum is **uniaxial** (optic axis $\parallel$ the pump). The probe-response tensor is $\varepsilon_{ij}=\varepsilon\,\delta_{ij}+2\varepsilon' E_{0i}E_{0j}$ (the exact differential of the scalar Axiom-4 kernel $S=\sqrt{1-(E/E_{yield})^2}$, optic axis $\parallel \hat E_0$; DERIVED, OQ-1 Step 1). The two eigen-indices and the **birefringence** are

$$n_\perp = (1-A^2)^{1/4} \approx 1-\tfrac14 A^2, \qquad n_\parallel = \sqrt{\tfrac{1-2A^2}{\sqrt{1-A^2}}} \approx 1-\tfrac34 A^2,$$
$$\boxed{\;\delta n_{bir} = n_\parallel - n_\perp \approx -\tfrac12 A^2\;}\qquad A \equiv E/E_{yield}.$$

This is **negative**, **$E^2$-leading**, and **exactly $2\times$ the scalar single-arm (isotropic) shift** $\delta n_{iso}=\sqrt{S}-1\approx-\tfrac14 A^2$ — which is the **common-mode** quantity the polarimeter is blind to (see below). The AVE coefficient is O(1) against an un-suppressed yield field $E_{yield}=V_{yield}/\ell_{node}\approx 1.13\times10^{17}$ V/m.

Standard QED (Euler-Heisenberg) must be differenced the **same** way: its birefringence rides the **difference** coefficient $3/45$ (the parallel $7/45$ and perpendicular $4/45$ eigen-indices differenced — the standard Euler-Heisenberg result), not the single $7/45$. So the matched, like-for-like, field-independent ratio is

$$\frac{\delta n_{AVE}}{\delta n_{QED}} = \frac{1/2}{(3/45)\,\alpha^2}\left(\frac{E_{crit}}{E_{yield}}\right)^2 = \frac{45/6}{\alpha^3} = \frac{7.5}{\alpha^3}\quad\left(\text{using }E_{crit}=\alpha^{-1/2}E_{yield},\ \text{so }(E_{crit}/E_{yield})^2=\tfrac1\alpha\right) \approx 1.93\times10^7.$$

> **The common-mode (isotropic) shift the polarimeter is blind to.** The historical single quantity, $\delta n_{iso}=\sqrt{S}-1=(1-A^2)^{1/4}-1\approx-\tfrac14 A^2-\tfrac{3}{32}A^4+\cdots$, is the **isotropic index shift** — the *common-mode* permittivity softening shared by both eigenmodes. A birefringence instrument rejects it; it is **not** the birefringence. (Comparing this AVE single-arm $-\tfrac14 A^2$ against QED's *parallel single-mode* $7/45$ gives the **single-arm/isotropic-vs-parallel** ratio $1/(4\cdot\tfrac{7}{45}\,\alpha^3)\approx4.14\times10^6$ — a comparison of MISMATCHED observables, retained here only for traceability, **not** the falsifier headline.)

> **Provenance note.** The earlier formulation "$\Delta n_{eff} = 1 - \sqrt{1 - (E/E_{yield})^2}$, leading $E^4$ term" was a $\sqrt{\varepsilon}$ conflation: the quantity $1-S = +A^2/2 + A^4/8$ is the **permittivity saturation DEPTH** (itself $E^2$-leading, NOT $E^4$-leading), whereas the refractive-index observable is $n=\sqrt{S}$, giving $\delta n_{iso} = \sqrt{S}-1 \approx -A^2/4$. The corrected discriminator is the coefficient, not the exponent; the corrected *observable* is the par$-$perp **differential** $-\tfrac12 A^2$, not the isotropic single-arm.

> **Chord vs echo (honest split, symmetric standard).** The AVE-distinct **CHORD** is that the vacuum *saturates at all* — a tree-level O(1) birefringence-bearing structure the QED vacuum lacks (QED's birefringence is an $\alpha^2$-loop effect). The **MAGNITUDE** $1.93\times10^7=7.5/\alpha^3$ is an **$\alpha$-echo** at the value level: AVE does not derive $\alpha$, so the number rides $\alpha^{-3}$. Symmetric standard: QED's $a_{EH}\alpha^2$ is *equally* $\alpha$-rooted — QED does not derive $\alpha$ either. The chord is the existence/form; the magnitude is an echo. Do not headline the magnitude as a chord.

### The Falsification Protocol

To test this, an ultra-high-Q optical fiber ring resonator (or high-finesse Fabry-Perot cavity) is placed transverse to an extreme-voltage DC electric field (approaching $10^{16}\,\text{V/m}$).

1. A stabilized probe laser monitors the precise resonance frequency of the cavity.
2. As the DC electric field is ramped up, the local metric stiffness alters, causing a measurable phase shift ($\Delta \Phi$) and pushing the resonance fringes.
3. The shift in resonance frequency is mapped dynamically against the applied field magnitude.

[Figure: vacuum_birefringence_differential.png — see manuscript/vol_4_engineering/chapters/]

A linearly-polarized pump + a 45°-launched probe in a high-finesse cavity, read out by an ellipsometer, measures the **par$-$perp differential** $\delta n_{bir}\approx-\tfrac12 A^2$ as accumulated ellipticity $\psi$ (the birefringence readout is a polarization-**phase** difference, accumulated as ellipticity $\psi$ — a dissipationless retardance, not absorption). At the **matched differential observable**, AVE sits a field-independent $\delta n_{AVE}/\delta n_{QED}=7.5/\alpha^3\approx1.93\times10^7$ above QED's differenced Euler-Heisenberg ($3/45$) birefringence, present at **all** fields. A **QED-sized differential coefficient** ($\delta n_{bir}\sim(3/45)\alpha^2(E/E_{crit})^2$) falsifies AVE; an AVE-sized coefficient falsifies QED at this observable. (An $E^2$ slope does **not** falsify AVE — QED is also $E^2$-leading. The discriminator is the coefficient, not the exponent.)

> **OQ-1 strengthen-by — CLOSED (field→cavity-phase coupling DERIVED; FLAG-A adjudicated).** The
> field→cavity-phase coupling that maps the index shift to a polarimeter readout is now **DERIVED**
> from the scalar Axiom-4 kernel (focal-E → uniaxial probe-response tensor
> $\varepsilon_{ij}=\varepsilon\delta_{ij}+2\varepsilon'E_{0i}E_{0j}$ → cavity round-trip birefringent
> phase → ellipticity), with the geometry factor $g$ **pinned per apparatus config**: see
> [`research/2026-06-21_oq1-field-to-cavity-phase-coupling-derivation.md`](../../../../../research/2026-06-21_oq1-field-to-cavity-phase-coupling-derivation.md)
> and the facility proposal [`research/2026-06-21_birefringence-coefficient-bankable-falsifier.md`](../../../../../research/2026-06-21_birefringence-coefficient-bankable-falsifier.md).
> This closes the prior "Gaussian-overlap asserted" residual — the coupling is no longer asserted.
>
> **FLAG-A PROMOTED (Grant-ratified 2026-07-03: "the matched-differential"; supersedes the 2026-06-21
> adjudication).** The par$-$perp **differential** $\delta n_{bir}=n_\parallel-n_\perp\approx-\tfrac12 A^2$
> (DERIVED) is the **canonical falsifier identity** of this leaf and of `clm-pp3qwf`, headlined above at
> the matched-observable ratio $7.5/\alpha^3\approx1.93\times10^7$ (AVE $-\tfrac12$ vs QED differenced $3/45$).
> The scalar $\delta n_{iso}\approx-\tfrac14 A^2$ is retained **KEEP-BOTH** as the **isotropic (common-mode)
> index shift** the polarimeter is blind to; paired against the QED parallel single-mode $7/45$ it gives the
> **single-arm-retardance-probe** ratio $4.14\times10^6$ — the ratio a distinct interferometric single-pass-phase
> instrument (not the polarimeter/ellipsometer) would read. **Scope:** single-arm-retardance probe $\to4.14\times10^6$;
> differential ellipsometer/polarimeter $\to1.93\times10^7$. The single-arm is a scoped secondary, NOT the falsifier
> headline. Ruling note: [`research/2026-07-03_birefringence-flagA-promotion_ruling.md`](../../../../../research/2026-07-03_birefringence-flagA-promotion_ruling.md).
>
> **Named residuals carried (do NOT over-state "closed"):**
> (a) **CHECK-3** — the gated-cavity round-trip $\tau_{rt}$ factor-of-2 / "recovers both finesse and
> temporal overlap" approximation (axial overlap integral exact; transverse/config trade study
> modeled, not uniquely derived).
> (b) **Polarimetry-floor validate-on-known** still owed against a published cavity. **The COEFFICIENT
> ($7.5/\alpha^3$) does not depend on either residual** — it is field- and apparatus-independent.

---

## The HIBEF facility point (engine-exact)

![The HIBEF moment: the birefringence discriminator at HIBEF's demonstrated ReLaX pump (single-pass, X-ray dark-field polarimeter, no Fabry-Perot). Left: the E²-leading SVE |δn|(E) at the demonstrated-pump point A²=5.92e-7. Centre: the probe polarization walk-off — SVE Δφ=0.148 rad (NJP 9835 eV) vs QED Δφ=3.3e-7 rad. Right: the single-pass flip probability P=sin²(Δφ/2) — SVE P≈5.4e-3 sits ~7 OOM above the required (1.4e-10) and demonstrated (2.4e-10) polarimeter floors; QED P≈2.8e-14 sits ~4 OOM below.](../../../../vol_4_engineering/figures/hibef_moment_panels.png)

*Figure — the falsifier-floor logic of the 🔴 header (line 19–20) rendered at the facility point. The plotted numbers are engine-exact driver outputs at their stated observables (Δφ, P=sin²(Δφ/2), δn). This render does NOT restate the matched-differential COEFFICIENT ratio; the `7.5/α³≈1.93e7` δn-ratio in this leaf's body carries the open QED-normalization correction of the 🔴 header (→ `7.5π/α²≈4.42e5`), tracked there and unresolved by this figure. Amplitude of the displayed pump stripe exaggerated ×3e5 for visibility (labelled). CONSISTENCY-class: FORM=SVE chord, magnitude ratio=α-echo (symmetric-standard). Driver: `src/scripts/viz/hibef_moment_scene.py` (`scripts.vol_9_device.birefringence_gap1_hibef_feasibility` + `ave.bench.delta_n_ave_differential_exact` + `graded_vacuum_network.saturation_kernel`); provenance ledger `viz/README.md` Visual 2.*

---

## Scope boundary: the SVE static-E kernel is EXCLUDED down to atomic scales ([C-EXCLUDED], Problem 3)
<!-- claim-quality: clm-sve3xc (this section is the canonical statement of the static-E atomic-sector exclusion of the SVE continuum kernel; the pump-probe birefringence prediction above survives as a DIFFERENT sector) -->

The birefringence prediction above lives in the **deep-cold, weak-field, dynamic AC pump–probe** sector ($A^2\sim6\times10^{-7}$, $\partial_t\neq0$, read at optical/X-ray). A separate arc (Grant-ratified fork memo FROZEN 2026-07-05; Problem 3, `research/2026-07-05_problem3-muonic-lamb_RESULT.md`, merged #538/#539) exposed the SAME continuum constitutive law $\varepsilon_{eff}=\varepsilon_0\sqrt{1-(E/E_c)^2}$ in the **atomic static-DC** sector — where atomic Coulomb fields are NOT weak against $E_c\approx1.13\times10^{17}$ V/m and are measured to sub-µeV precision. The verdict is **[C-EXCLUDED]**: the continuum static-E extrapolation is falsified as a universal claim down to atomic scales.

**What the arc established (canonical):**
- **The analytic tail (sympy-verified):** inverting $E\sqrt{1-(E/E_c)^2}=E_{Coulomb}$ on the lower branch gives the potential shift tail $\delta V(r)=k^3/(10\,E_c^2 r^5)\Leftrightarrow\delta V/V_C=\tfrac1{10}A^2(r)$, $A^2(r)=(E_C(r)/E_c)^2$ — the expected $(E/E_c)^2$-class near-nucleus enhancement.
- **Both arms violate the muonic-H window by 4–7 orders of magnitude.** The continuum arm's SVE correction to the muonic-H Lamb shift $\Delta E(2P_{1/2}-2S_{1/2})$ is $[1.5\times10^6,\,2.3\times10^7]$ µeV = **7.5×–114× the entire 202.37 meV Lamb shift**; the lattice-scoped arm (kernel cut to $r\gg\ell_{node}=386$ fm) is $[4.9\times10^4,\,6.2\times10^5]$ µeV = **0.24×–3× the full Lamb shift** — smallest variant still $\sim2\times10^4\times$ the 2.3 µeV CREMA window. Routing is sign-independent (magnitudes route; the variant-to-variant sign varies).
- **Non-perturbatively large.** A correction many times the full level structure means first-order perturbation theory has already broken down; the exact multiples are illustrative of scale. This STRENGTHENS the exclusion — a leading term larger than the thing corrected cannot be hidden by a higher-order rescue.
- **The ~300 fm protective-scale is refuted.** The fork memo's data-derived $\sim300$ fm ($\approx0.78\,\ell_{node}$) floor is $\sim12\times$ too small: making the hard-cutoff lattice-scoped shift clear the 2.3 µeV window requires the cutoff at $r_{cut}\approx9\cdot\ell_{node}\approx3.5$ pm (bisection on the leading-tail hard-cutoff shift). A cutoff at ~3.5 pm is far above any lattice/substrate scale and would be an independent free parameter — precisely the [C] failure mode.
- **U91+ is INCOMPUTABLE.** At Z=92 the 1s Bohr radius (575 fm) sits inside the no-solution radius ($r_{ns}=1082.6$ fm); 72.5% of the 1s density and 90% inside $r_{turn}$ sit where the continuum elliptic kernel has NO real solution ($A^2=12.6>1$). The continuum static-E law does not merely violate windows at high Z — it has no solution at all.
- **µ⁻ sign convention (stated once):** the bound particle is the µ⁻ ($q=-e$); because $\delta V>0$ (SVE field enhanced ⟹ deeper binding), the penetrating 2S is pulled down and the measured 2P−2S splitting INCREASES — a positive $\delta[\Delta E]$, same direction as Uehling. Magnitudes are convention-independent; routing is by $|\text{value}|$.

**What DIES:** the continuum static-E constitutive law $\varepsilon_{eff}=\varepsilon_0\sqrt{1-(E/E_c)^2}$ as a UNIVERSAL claim down to atomic scales. It cannot be the vacuum's response to arbitrary static fields at atomic scales.

**What SURVIVES (separate sectors, KEEP-BOTH):** (i) the **pump–probe AC birefringence** of this leaf — a deep-cold, weak-field, *dynamic* ε-varactor response read at optical/X-ray, NOT the atomic static-DC sector; its $\sim5\times10^{-3}$ HIBEF flip-prob falsifier is untouched. (ii) The **µ-sector circulation-keying** (`clm-pvlas1`, keyed on $\partial_t B$, not static flux; see [`pvlas-static-b-verdict.md`](../ch11-experimental-bench-falsification/pvlas-static-b-verdict.md)). A [C] verdict excludes the continuum static-E *extrapolation*, NOT the registered birefringence prediction and NOT the magnetic-sector side-prediction.

> **Object-distinction guard (paired with Q-G20a).** This is the **SVE constitutive static-E** Lamb correction (a saturating-permittivity effect). It is a DIFFERENT object from the **QED vacuum-fluctuation** Bethe-log Lamb mechanism at [`../../../vol2/quantum-orbitals/ch07-quantum-mechanics/q-g20a-lamb-shift-structural-closure.md`](../../../vol2/quantum-orbitals/ch07-quantum-mechanics/q-g20a-lamb-shift-structural-closure.md) (electronic H, $+1057.85$ MHz). The [C-EXCLUDED] verdict here does not touch that leaf's self-energy match; do not conflate the two Lamb objects.

**PENDING-DERIVATION (named, NOT landed):** the [B-AVE] rescue/scoping arm of the fork memo — whether a lattice-scale regime boundary with cutoff-dependent effective coefficients (scalar $(q\ell_{node})^2$ / anisotropic $(q\ell_{node})^4$, computation-adjudicated) can protect the windows and turn the exposure into a forward prediction — is an OPEN derivation, not a landed result. The **exclusion is SETTLED regardless** (both arms violate as written); the derivation decides the RESCUE, not the exclusion. Provenance: `research/2026-07-05_electrostatic-sector-fork-memo_FROZEN.md` (FROZEN, Grant-ratified); `research/2026-07-05_problem3-muonic-lamb_RESULT.md` ([C-EXCLUDED]).
