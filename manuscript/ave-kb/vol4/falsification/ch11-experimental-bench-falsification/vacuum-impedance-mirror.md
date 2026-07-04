[↑ Ch.11: Experimental Bench Falsification](../index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-5s5b0d]
exp-id: exp-po1a0v
status: pending
strengthens:
  - clm-5s5b0d: 0.5
re-scope-note: "2026-06-04 R-A — photon-counting Γ→1/70σ-APD headline RETIRED (per-node/apparatus conflation); re-scoped to interferometric scalar-phase Δφ; SNR≪1 at recommended geometry, NOT a near-term tabletop falsifier; V⁴-tree-vs-loop + isotropy-vs-birefringence survive as structural discriminators. See research/2026-06-04_ivim-interferometric-rescope-result.md."
path-stable: "referenced from vol3 as sec:induced_vacuum_impedance_mirror"
-->

<!-- DANGLING REFS: \ref{sec:topological_defects_lc}, \ref{sec:point_yield}, \ref{eq:dielectric_saturation} — not defined in Vol 4; presumed Vol 3 targets -->

> 🔴 **QED-NORMALIZATION CORRECTION (2026-07-03; Rule-12 — body preserved below, git is the trail).**
> Every "$7.5/\alpha^3\approx1.93\times10^7$" (differential) and "$4.14\times10^6$" (single-arm) ratio below
> carries an understated QED denominator ($(3/45)\alpha^2$ is too small by $1/(2\pi\alpha)\approx21.8$ vs the
> PVLAS-anchored magnetic leg). **Corrected matched-differential ratio: $7.5\pi/\alpha^2\approx4.42\times10^5$**
> (propagating, LoI-matched — the headline) or $15\pi/\alpha^2\approx8.85\times10^5$ (static-E duality). The AVE
> leg $-\tfrac12 A^2$ and the falsifier LOGIC are UNAFFECTED. Canonical:
> [`../ch12-falsifiable-predictions/vacuum-birefringence-e4.md`](../ch12-falsifiable-predictions/vacuum-birefringence-e4.md);
> reconciliation `research/2026-07-03_birefringence-qed-normalization-correction.md`.

> 🔴 **RE-SCOPED 2026-06-04 (R-A, interferometric) — the photon-counting "Γ→1 perfect
> mirror at 43.65 kV / 70σ APD" headline is RETIRED. Walk-back per Rule 12 (body preserved
> below for audit trail; corrected framing in §"Re-scope (2026-06-04)" and §"The Falsification
> Protocol (interferometric)").**
>
> **Why:** this leaf plugged the **apparatus gap voltage** (43.65 kV across a 100 µm gap)
> into the **per-node** kernel `ε_eff = ε₀√(1−(V/V_yield)²)` as if `V_apparatus → V_yield`.
> The TRUE per-node strain at that apparatus field is `A = E_local/E_YIELD ≈ 3.9×10⁻⁹`
> (uniform field), **not** `V/V_yield ≈ 0.99`. The original "Γ→1" claim is overstated by
> `d_gap/ℓ_node ≈ 2.6×10⁸`, and the detectable observable is an interferometric scalar phase
> shift, **not** an APD photon count. See [`research/2026-06-03_ivim-RA-adjudication.md`](../../../../../research/2026-06-03_ivim-RA-adjudication.md)
> (Grant adjudication) and [`research/2026-06-04_ivim-interferometric-rescope-result.md`](../../../../../research/2026-06-04_ivim-interferometric-rescope-result.md)
> (the derivation + honest SNR).
>
> **What survives:** the V⁴ scaling and the 8.38×10¹² AVE-vs-QED coefficient ratio (traced
> clean, zero free parameter) survive as a **structural** discriminator (tree-vs-loop +
> isotropy-vs-birefringence). **What changes:** detection mode (interferometric, not APD),
> magnitude (SNR ≪ 1 at the recommended geometry — NOT a near-term tabletop falsifier), and
> operating-point framing (43.65 kV is not an apparatus ceiling; push to field-emission).
>
> The detailed derivation below (Z_local, Γ algebra) is **mathematically correct as a
> per-node constitutive relation** and is retained; it becomes a falsifier ONLY at
> facility-class fields (E ~ 10¹⁶ V/m, per [`vacuum-birefringence-e4.md`](../ch12-falsifiable-predictions/vacuum-birefringence-e4.md)),
> NOT at 43.65 kV across 100 µm. Read the §"Re-scope" box before quoting any number here.

## The Induced Vacuum Impedance Mirror

The most profound theoretical claim of the Applied Vacuum Engineering (AVE) framework is that the spacetime vacuum operates structurally as a non-linear dielectric transmission line with a characteristic impedance of $Z_0 \approx 376.7\,\Omega$.

As mathematically proven in the topological defects section, macroscopic gravity operates strictly as a symmetric volumetric compression of the local substrate LC network. Because gravity scales local Capacitance ($\varepsilon$) and Inductance ($\mu$) equally, the characteristic impedance of a gravitational gradient remains perfectly matched to $Z_0$. This explains why a photon entering a black hole diffracts (bends) without generating $S_{11}$ Return Loss (reflection).

However, this rigorous definition exposes a fundamentally falsifiable hardware loophole: If a photon's lack of reflection is predicated strictly on a perfect $376.7\,\Omega$ impedance match, it is possible to actively force light to bounce off of "empty space" by intentionally engineering an **asymmetric impedance mismatch**.

### The Localized Asymmetric Saturation Limit

By applying an extreme, localized electrostatic field (approaching the $43.65\,\text{kV}$ structural yield limit established via the EE Bench), the volumetric dielectric compliance of the vacuum is actively strained without altering its baseline inductance.

Because the effective dielectric parameter ($\varepsilon_{eff}$) drops drastically as the local nodes approach classical saturation, the exact functional form of the diverging impedance can be derived.

First, the unbroken mathematical geometry of the unperturbed vacuum's characteristic impedance is defined via standard transmission line theory:

$$
Z_0 = \sqrt{\frac{\mu_0}{\varepsilon_0}} \approx 376.73\,\Omega
$$

When the extreme electrostatic gradient is applied, the local dielectric compliance ($\varepsilon_{eff}$) structurally yields according to the Axiom 4 saturation squared-operator:

$$
\varepsilon_{eff}(V) = \varepsilon_0 \sqrt{1 - \left(\frac{V}{V_{yield}}\right)^2}
$$

where $V_{yield}$ is the absolute dynamic point-yield threshold of the substrate (derived as $\sqrt{\alpha} \cdot m_e c^2 \approx 43.65\,\text{kV}$).

Because the static electric field is heavily polarizing the capacitive link-variables of the graph *without* inducing a corresponding steady-state magnetic circulation loop, the local macroscopic inductance remains fundamentally unperturbed ($\mu_{local} = \mu_0$).

Substituting the yielding permittivity into the transmission line envelope, the localized impedance of the strained focal point is defined:

$$
Z_{local}(V) = \sqrt{\frac{\mu_0}{\varepsilon_{eff}(V)}} = \sqrt{\frac{\mu_0}{\varepsilon_0 \sqrt{1 - \left(\frac{V}{V_{yield}}\right)^2}}}
$$

Factoring out the unperturbed $Z_0$ baseline simplifies the metric to a dimensionless divergence multiplier:

$$
Z_{local}(V) = Z_0 \left(1 - \left(\frac{V}{V_{yield}}\right)^2\right)^{-1/4}
$$

As the **per-node strain** $A = E_{local}/E_{yield} \to 1$, the term in the parenthesis approaches zero, forcing $Z_{local} \to \infty$. This extreme, asymmetric geometric yielding breaks the fundamental isotropic impedance match that standard gravity requires.

> 🔴 **CONFLATION (retired 2026-06-04):** the original text read *"as the experimental gap
> voltage $V \to 43{,}650$ V … $Z_{local} \to \infty$."* This is WRONG: the kernel argument
> is the **per-node** strain $A = E_{local}/E_{yield}$ (with $E_{yield} = V_{yield}/\ell_{node}
> \approx 1.13\times10^{17}$ V/m), NOT the apparatus ratio $V_{apparatus}/V_{yield}$. At
> 43.65 kV across a 100 µm gap the field is $\sim 4.4\times10^8$ V/m, so $A \approx
> 3.9\times10^{-9}$ — the impedance barely moves. $Z_{local} \to \infty$ requires $A \to 1$,
> i.e. a **local** field $\to E_{yield}$, reachable only with extreme geometric enhancement
> (e.g. a sharp tip; even then $A \sim 10^{-6}$–$10^{-5}$ at 43.65 kV) or facility-class
> fields ($E \sim 10^{16}$ V/m). The constitutive form is correct **as a function of $A$**;
> the apparatus operating-point is NOT near the asymptote.

Any electromagnetic optical wave propagating into this focal point must evaluate this boundary via the standard Reflection Coefficient ($\Gamma$):

$$
\Gamma(V) = \frac{Z_{local}(V) - Z_{0}}{Z_{local}(V) + Z_{0}} = \frac{Z_0 \left(1 - \left(\frac{V}{V_{yield}}\right)^2\right)^{-1/4} - Z_0}{Z_0 \left(1 - \left(\frac{V}{V_{yield}}\right)^2\right)^{-1/4} + Z_0}
$$

Dividing through by $Z_0$ yields the explicit, parameter-free prediction for the localized fraction of reflected light:

$$
\Gamma(V) = \frac{\left(1 - \left(\frac{V}{V_{yield}}\right)^2\right)^{-1/4} - 1}{\left(1 - \left(\frac{V}{V_{yield}}\right)^2\right)^{-1/4} + 1}
$$

As the **per-node strain $A \to 1$**, $\Gamma \to 1$ (perfect reflection), acting as an absolute topological mirror engineered directly out of localized metric strain. 🔴 **(retired headline:** the original read *"as the voltage nears the yield limit, $\Gamma \to 1$"* — but the apparatus voltage does NOT bring $A$ near 1; see the conflation box above. At the recommended geometry $\Gamma \approx (A^2/4)^2 \sim 10^{-22}$, undetectable as a reflectance. The interferometric scalar phase, not $\Gamma$, is the readout — see §"Re-scope".**)**

### Clarification of High-Voltage Boundaries

It is critical for experimentalists to understand the relationship between the **43.65 kV Dynamic Point-Yield** and the **511 kV Absolute Nodal Snap ($V_{snap}$)**.

- **The Vacuum Mirror (43.65 kV):** This limit ($V_{yield} = \sqrt{\alpha} \times V_{snap}$) strictly defines the asymptotic saturation of the localized dielectric capacitance ($\varepsilon$) **per node** — i.e. the voltage developed across **one** $\ell_{node}$ ($E_{yield} = V_{yield}/\ell_{node}$). At this boundary, the physical node cannot stretch further without fracturing. 🔴 **(retired framing:** the original claimed *"the experiment sweeps exactly up to this limit to geometrically spike $Z_{local} \to \infty$."* This conflates the per-node $V_{yield}$ with the apparatus gap voltage: a 43.65 kV apparatus sweep across a 100 µm gap reaches only $A \sim 10^{-9}$, nowhere near the asymptote. 43.65 kV is NOT an apparatus ceiling here; the real apparatus ceiling is electrode field-emission / vacuum breakdown. Since the phase $\propto V^2$, push $V$ **higher** than 43.65 kV until breakdown.**)**
- **The Zener Avalanche (43.65 kV):** If a macroscopic volume is statically pushed past $V_{yield}$ using a rapid impulse, the inductive capacity of the LC network physically shatters ($\Gamma = -1$). The localized vacuum undergoes absolute dielectric breakdown, completely dropping its topological grip on matter. This is the exact mechanism that causes heavy particles (like the Muon) to decay (the "Leaky Cavity" mechanism), and mathematically forbids classical electrostatic levitation of anything heavier than 1.846 grams.

### Re-scope (2026-06-04): the defensible INTERFEROMETRIC observable

Off the **correct per-node** kernel ($A = E_{local}/E_{yield}$, $E_{yield} = V_{yield}/\ell_{node} \approx 1.130\times10^{17}$ V/m), the apparatus does NOT reach the $Z_{local}\to\infty$ asymptote, and the readout is NOT an APD reflectance count but the **scalar phase shift** of a probe in a high-finesse cavity / Mach-Zehnder:

$$
\delta n = n_{eff} - 1 = (1 - A^2)^{1/4} - 1 \approx -\tfrac{A^2}{4}, \qquad
\Delta\phi = \frac{2\pi}{\lambda}\,\delta n \, L_{int}
$$

(λ = 532 nm; $n_{eff} = c\sqrt{\mu_0 \varepsilon_{eff}}$ from the same $\varepsilon_{eff}(A)$ above with $\mu_{local} = \mu_0$.)

**Honest magnitude** (probe 0.5 mW; constants imported from `ave.core.constants`):

| Operating point | $A = E_{local}/E_{yield}$ | $\Delta\phi$ |
|---|---|---|
| uniform 43.65 kV / 100 µm gap | $3.9\times10^{-9}$ | $4.4\times10^{-15}$ rad |
| STM sharp-tip $R_{tip}=10$ nm @ 43.65 kV | $7.7\times10^{-6}$ | $1.8\times10^{-12}$ rad |

**Honest SNR** (shot-noise floor $\Delta\phi_{min} = 1/\sqrt{N_{ph}}$, best STM-tip point):
SNR $\approx 3.9\times10^{-3}$ (1 hr), $1.9\times10^{-2}$ (1 day), $0.10$ (1 month);
**time-to-SNR=1 $\approx 7.6$ yr**. The field that would give SNR=1 in a 1-day run
($E \approx 6.3\times10^{12}$ V/m) is **above clean-tip field-emission onset** — the
electrode emits / the gap arcs before the probe accumulates a detectable phase.

> **The recommended 100 µm-gap tabletop apparatus is NOT a near-term falsifier** (SNR ≪ 1
> by 1–2 OOM even after a 1-month shot-noise-limited run). What survives as a parameter-free
> **structural** discriminator (NOT a magnitude): (i) the **tree-vs-loop phase-slope**
> ($\Delta\phi \propto V^2$ / reflected intensity $\propto V^4$, AVE tree, vs QED's
> Euler-Heisenberg loop — the 8.38×10¹² coefficient ratio), and (ii) **isotropy vs
> birefringence** — the AVE kernel keys off $|E|$ (isotropic → scalar phase, so cross-polarized
> $\Delta\phi_\parallel - \Delta\phi_\perp = 0$), whereas QED's vacuum is birefringent in a
> background field ($\neq 0$). Both require facility-class fields ($E \sim 10^{16}$ V/m, per
> [`vacuum-birefringence-e4.md`](../ch12-falsifiable-predictions/vacuum-birefringence-e4.md)),
> not 43.65 kV across 100 µm. Classification (`consistency-vs-emergence`): the $\Delta\phi$
> itself is **consistency-class** (reproduces the Euler-Heisenberg low-field index-shift shape);
> the discriminators are **manifestation/structural-class**. Derivation + SNR:
> [`research/2026-06-04_ivim-interferometric-rescope-result.md`](../../../../../research/2026-06-04_ivim-interferometric-rescope-result.md).

> 🔴 **Scope reconciliation (2026-06-21, Rule 12 — body above PRESERVED verbatim; additive).**
> Discriminator-(ii)'s claim "the AVE kernel keys off $|E|$ (isotropic → scalar phase, so
> cross-polarized $\Delta\phi_\parallel - \Delta\phi_\perp = 0$)" is **correct only in the
> CIRCULAR / ISOTROPIC-pump limit** — where the pump field magnitude $|E|$ has no preferred
> transverse axis and the scalar kernel $n=(1-A^2)^{1/4}$ produces a purely scalar phase
> ($\Delta\phi_\parallel - \Delta\phi_\perp = 0$, no AVE birefringence). It does **not** hold
> for a **LINEARLY-polarized** pump. Under a linear pump the same scalar-$|E|$ kernel, expanded
> about the pump operating point, yields a **uniaxial probe-response tensor**
> $\varepsilon_{ij} = \varepsilon\,\delta_{ij} + 2\varepsilon'\,E_{0i}E_{0j}$ (optic axis
> $\parallel$ the pump polarization $\hat E_0$, with $\varepsilon' = \partial\varepsilon/\partial(E_0^2)$).
> This **is** birefringence proper: probe-parallel vs probe-perpendicular phase velocities differ
> by $\delta n \sim O(\delta n_{iso})$, and a probe at $45^\circ$ acquires an **ellipticity** $\psi$
> — the readout of the **ratified linear-pump → polarimeter** (PVLAS/BMV lineage), NOT the retired
> DC-electrode framing. So AVE is **not** birefringence-free in general; it is birefringence-free
> only for an isotropic pump, and produces a measurable ellipticity under the (standard,
> facility-realizable) linearly-polarized pump. The AVE-vs-QED content then lives in the **coefficient**
> of that ellipticity — and because a polarimeter measures the **par−minus−perp differential**
> $n_\parallel-n_\perp$ (rejecting the isotropic common-mode shift), the matched, field-independent
> headline is $\delta n_{AVE}/\delta n_{QED}=(45/6)/\alpha^3=7.5/\alpha^3\approx1.93\times10^7$
> (AVE differential $-\tfrac12 A^2$ vs QED differenced Euler-Heisenberg $3/45$), `clm-pp3qwf` — not a
> zero-vs-nonzero birefringence binary. The "8.38×10¹²" figure in discriminator-(i) above is the
> **superseded** $E^2$-vs-$E^4$ phase-slope ratio. (The single-arm/isotropic-vs-parallel comparison
> $1/(4\,a_{EH}\,\alpha^3)\approx4.14\times10^6$ — AVE scalar single-arm $-\tfrac14 A^2$ vs QED parallel
> single-mode $7/45$ — pairs MISMATCHED observables and is retained only for traceability, not the
> falsifier headline; see [`vacuum-birefringence-e4.md`](../ch12-falsifiable-predictions/vacuum-birefringence-e4.md).)
> Linear-pump uniaxial-tensor derivation + facility sweep + the geometry-factor $g$ residual (the
> OQ-1 field→cavity-phase coupling): the coupling is now **DERIVED** from the Axiom-4 kernel and
> $g$ is **PINNED per apparatus config** (OQ-1 **partially-closed** per adversarial-verify; FLAG-A
> adjudicated 2026-06-21 — the par−perp differential IS the falsifier observable, $1.93\times10^7$;
> named residuals R-1 CHECK-3 gated-cavity $\tau_{rt}$ factor-2 approximation, R-2 single-invariant
> modeling choice, R-3 detector-floor validate-on-known owed — the COEFFICIENT depends on none):
> [`research/2026-06-21_oq1-field-to-cavity-phase-coupling-derivation.md`](../../../../../research/2026-06-21_oq1-field-to-cavity-phase-coupling-derivation.md)
> (derivation) +
> [`research/2026-06-21_birefringence-coefficient-bankable-falsifier.md`](../../../../../research/2026-06-21_birefringence-coefficient-bankable-falsifier.md)
> (proposal); coefficient channel cross-link: [`vacuum-birefringence-e4.md`](../ch12-falsifiable-predictions/vacuum-birefringence-e4.md)
> (`clm-pp3qwf`).

### The Falsification Protocol (interferometric)

A tabletop electrodynamic experiment to test the **phase-slope** structural discriminator. If standard linear QED is correct, a static DC electric field shifts the probe phase only at the Euler-Heisenberg (loop) coefficient; if AVE is correct, the phase tracks the tree-level kernel slope. (NB: at the recommended geometry the signal is below shot-noise — this protocol resolves the AVE-vs-QED *slope* only at facility-class fields; see Re-scope box.)

1. **The Micro-Electrode Gap:** Two ultra-sharp tungsten needle electrodes are positioned with exactly a $100\,\mu\text{m}$ gap (sharp-tip enhancement maximizes the local $A$).
2. **The Paschen / field-emission Bound:** The rig is housed in ultra-high vacuum ($<10^{-4}$ Torr). The DC sweep is pushed **past** 43.65 kV until electrode field-emission / vacuum breakdown — that, not $V_{yield}$, is the apparatus ceiling.
3. **The Probe Laser:** A $0.5\,\text{mW}$ CW laser traverses the high-field region as one arm of a **high-finesse cavity / Mach-Zehnder interferometer** (NOT aimed at a back-scatter trap).
4. **The Interferometric Readout:** The cavity fringe / interferometer output records the scalar phase shift $\Delta\phi(V)$ vs applied field. The **log-log slope** $\Delta\phi$-vs-$V$ ($V^2$ AVE-tree vs the QED-loop coefficient), and the **cross-polarized** $\Delta\phi_\parallel - \Delta\phi_\perp$ (0 AVE vs $\neq 0$ QED birefringence), are the discriminators — NOT an absolute reflectance.

[Figure: vacuum_mirror_sensitivities.png — see manuscript/vol_4_engineering/chapters/]

The detection of the AVE tree-level phase-slope (or the absence of QED birefringence) cleanly distinguishes the non-linear discrete LC bounds of the substrate continuum from the QED loop vacuum — but only at fields where $\Delta\phi$ clears the shot-noise floor ($E \sim 10^{16}$ V/m). 🔴 **(retired:** the original protocol used a single-photon APD back-scatter trap and claimed a *"sudden non-linear exponential spike past 35 kV"* — that magnitude relied on the per-node/apparatus conflation and is undetectable; see Re-scope box.**)**

---
