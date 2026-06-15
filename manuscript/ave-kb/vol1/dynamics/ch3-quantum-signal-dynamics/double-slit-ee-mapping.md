[↑ Ch.3 Quantum and Signal Dynamics](index.md)

<!-- kb-frontmatter
kind: leaf
no-claim: "consolidation / translation leaf — maps the canonical AVE double-slit mechanism (defect through one slit + ponderomotive transverse wake through both) and its component glossary to EE primitives. Originates no new derivation: the mechanism is owned by ohmic-decoherence-born.md (clm-7zuwtm/ldmvwi/zuf7g1, double-slit + Ohmic decoherence + Born rule), the electron=self-trapped-photon identification by photon-identification.md (clm-3npynp/i4p11y/fr3mos) + master-equation.md (clm-lv3uw1), and the EE component mappings by translation-circuit.md (clm-eemap1). Classified consistency/translation per consistency-vs-emergence — NOT an emergence test. Created per ave-ee-first-mapping Step 6."
-->

# Double-Slit EE / Glossary Mapping — Defect + Ponderomotive Wake

This leaf consolidates the AVE double-slit experiment's component glossary into a single substrate-primitive → electrical-engineering (EE) component mapping. The "particle" in the AVE double-slit is the **electron — a self-trapped photon** (see [Photon Identification](../ch4-continuum-electrodynamics/photon-identification.md), $T_2$-only Cosserat microrotation; electron = that wave at Axiom-4 self-saturation). The mechanism, its which-path decoherence, and its Born-rule screen are owned by [Ohmic Decoherence and the Born Rule](ohmic-decoherence-born.md); the EE-component vocabulary is owned by the [circuit translation table](../../../common/translation-tables/translation-circuit.md). This leaf re-states the correspondence; it derives nothing new.

## §1 — Scope and classification

> **[Resultbox]** *Classification — consistency / translation (NOT emergence)*
>
> Per `consistency-vs-emergence`: every row in this leaf is a **consistency / translation identification** between a substrate primitive (already canonical elsewhere) and its EE component. NONE of it is an emergence test, and NONE of it is a new derivation. This leaf carries `no-claim:` frontmatter and references its owning claims by cross-link.

The owning canonical content:

> → Primary: [Ohmic Decoherence and the Born Rule](ohmic-decoherence-born.md) — the double-slit mechanism (defect + ponderomotive wake), Ohmic which-path decoherence, and the master-equation-derived Born rule (clm-7zuwtm, clm-ldmvwi, clm-zuf7g1).
> → Primary: [Photon Identification (T₂-only Cosserat ω)](../ch4-continuum-electrodynamics/photon-identification.md) — the electron = self-trapped photon identification (clm-3npynp, clm-i4p11y, clm-fr3mos).
> → Primary: [Master Equation](../ch4-continuum-electrodynamics/master-equation.md) — the magnetic-branch ($\Gamma \to -1$, short-circuit) saturation that creates the electron's core (clm-lv3uw1).
> ↗ See also: [Circuit Translation Table](../../../common/translation-tables/translation-circuit.md) §4/§4.5 — the EE-component catalog this leaf draws on (clm-eemap1).
> ↗ See also: [Photon EE Mapping](../ch4-continuum-electrodynamics/photon-ee-mapping.md) — the companion leaf on free-photon vs self-trapped-electron EE structure (carrier × envelope, I/Q quadrature, V↔Φ_link).

## §2 — The reconciled mechanism (electron = self-trapped photon; defect + wake)

The AVE double-slit is a deterministic, continuous-medium interference problem — not a mysterious wave-function collapse. Three pieces:

1. **The particle is the electron's defect / core.** The electron is a **self-trapped photon**: a $T_2$-only transverse Cosserat-microrotation wave whose amplitude has crossed $V_{\text{yield}} = \sqrt{\alpha}\,V_{\text{snap}} \approx 43.65$ kV, triggering Axiom-4 self-saturation. On the **magnetic branch** the Cosserat $\mu_{eff} \to 0$, the local impedance $Z = \sqrt{\mu_{eff}/\varepsilon_0} \to 0$, and the reflection coefficient $\Gamma \to -1$ (a **short-circuit**, total internal reflection). The wave weaves its own spherical $0\,\Omega$ "Local Bubble" — a hyper-rigid envelope where $c_{local} \to 0$ — which is the localized topological defect (the matter core) that threads **one** slit. (Canonical: [Photon Identification](../ch4-continuum-electrodynamics/photon-identification.md) line 11; [Master Equation](../ch4-continuum-electrodynamics/master-equation.md) lines 78–79, clm-lv3uw1; [Zero-Impedance Boundary](zero-impedance-boundary.md) line 51; [Resonant LC Solitons](../../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md) line 50.)

2. **The wake threads both slits.** The defect's motion through the lattice generates a continuous **transverse inductive wake** — a ponderomotive pressure field $\propto \nabla|\Psi|^2$. This wake is a low-amplitude field disturbance (not a saturated core), so it passes through **both** apertures and interferes with itself on the far side, producing the standing-wave trough pattern. (Canonical: [Ohmic Decoherence and the Born Rule](ohmic-decoherence-born.md) line 11.)

3. **Deterministic ponderomotive navigation.** The defect rides the transverse ponderomotive gradients of its own (self-interfered) wake: $\mathbf{F} \propto \nabla|\Psi|^2$ steers it into the quantized standing-wave troughs. The fringe pattern is built up by many such deterministic single-particle trajectories — the statistics are the Born rule (§4), not an axiom.

> **[Resultbox]** *The reconciled picture in one line*
>
> Defect (the electron's $\Gamma = -1$ core) through one slit; ponderomotive transverse wake ($\propto \nabla|\Psi|^2$) through both; deterministic navigation $\mathbf{F} \propto \nabla|\Psi|^2$ into the troughs. The screen intensity is $|\partial_t\mathbf{A}|^2 \equiv |\Psi|^2$.

**The EE picture of the core.** The electron's $\Gamma = -1$ self-created $0\,\Omega$ cavity maps to a **shorted $\lambda/4$ resonator** — the most fundamental EE mapping of the matter core (a shorted quarter-wave line presents a short at its mouth after a half-Γ-lap on the Smith chart; gate-(b) CLOSED 2026-06-04, [translation-circuit.md](../../../common/translation-tables/translation-circuit.md) §4.5(e) line 245 ("Half/quarter-wave resonator … Gate (b) RAN 2026-06-04 … CLOSED")). The trapped reactive energy of this resonator IS the electron's rest mass. The full free-photon-vs-self-trapped-electron EE structure is developed in the companion leaf [Photon EE Mapping](../ch4-continuum-electrodynamics/photon-ee-mapping.md).

## §3 — Component → substrate-primitive → EE-component table

Each row is a consistency / translation identification (§1). The "Status" column carries the honest state of each mapping; "✓-VERIFIED canonical" marks a mapping confirmed verbatim against its anchor at this leaf's authoring (`verify-before-cite`).

| Component | Substrate primitive | EE component | Anchor | Status |
|---|---|---|---|---|
| **Photon (free)** | $T_2$-only transverse Cosserat shear wave; $u=0$, $\omega\neq0$, $\Delta\phi\ll\alpha$ | matched ($\Gamma=0$) lossless transmission line at $Z_0\approx376.7\,\Omega$ | [photon-identification.md](../ch4-continuum-electrodynamics/photon-identification.md):11,24,77 ($\Gamma=0$ at every bond) | ✓-VERIFIED canonical |
| **Carrier** | oscillation frequency $\omega$ of the $T_2$ wave | RF carrier | (informal) photon-propagation visualization | informal — see [Photon EE Mapping](../ch4-continuum-electrodynamics/photon-ee-mapping.md) §3 |
| **Envelope** | Gaussian amplitude modulation in space/time | bandwidth-limited pulse envelope | (informal) photon-propagation visualization | informal — see [Photon EE Mapping](../ch4-continuum-electrodynamics/photon-ee-mapping.md) §3 |
| **Electron (the "particle")** | self-trapped photon — the $T_2$ wave at $\Delta\phi\to\alpha$; magnetic branch shorts | **shorted $\lambda/4$ resonator** | [photon-identification.md](../ch4-continuum-electrodynamics/photon-identification.md):11; [translation-circuit.md](../../../common/translation-tables/translation-circuit.md):245 (§4.5(e) "Half/quarter-wave resonator … Gate (b) … CLOSED") | ✓ (electron = self-trapped photon canonical; $\lambda/4$ gate-(b) CLOSED 2026-06-04) |
| **"Bubble" / core** | $\Gamma=-1$ self-created $0\,\Omega$ Local Bubble; $c_{local}\to0$, hyper-rigid envelope | $0\,\Omega$ short at the resonator mouth | [resonant-lc-solitons.md](../../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md):50; [zero-impedance-boundary.md](zero-impedance-boundary.md):51; [translation-circuit.md](../../../common/translation-tables/translation-circuit.md):115 | ✓ ($\Gamma=-1$ SHORT, magnetic branch, clm-lv3uw1) |
| **Rest mass** | trapped reactive energy in the $\Gamma=-1$ standing wave | stored reactive energy of the shorted resonator | [master-equation.md](../ch4-continuum-electrodynamics/master-equation.md):79; [zero-impedance-boundary.md](zero-impedance-boundary.md):51 | ✓ (clm-lv3uw1) |
| **Transverse wake** | continuous transverse inductive wake $\propto\nabla\lvert\Psi\rvert^2$ (ponderomotive, near-field) | near-field ponderomotive gradient — **NOT** the far-field $\tau^{far}_{zx}$ dark-wake | [ohmic-decoherence-born.md](ohmic-decoherence-born.md):11; regime-distinct from [translation-circuit.md](../../../common/translation-tables/translation-circuit.md):144 ("dark wake (far-field reaction)" row) | ✓ (Born-path closed); regime-tagged ≠ thrust dark-wake (§6) |
| **Slit wall** | aperture / impedance discontinuity in the lattice (wake transmits through both) | aperture / boundary discontinuity in the line | [ohmic-decoherence-born.md](ohmic-decoherence-born.md):11 | consistency |
| **Detector / observer** | resistive mechanical load coupling to the $\mathbf{A}$-field | resistive load $Z_{det}$ (Joule sink) | [ohmic-decoherence-born.md](ohmic-decoherence-born.md):20,25 ($P=V^2/R$ + $W_{extracted}$) | ✓ (clm-ldmvwi) |
| **Which-path decoherence** | Ohmic thermalization of the phase wave; $W_{extracted}\propto\lvert\partial_t\mathbf{A}\rvert^2/Z_{det}$ | $P=V^2/R$ Joule heating at the load | [ohmic-decoherence-born.md](ohmic-decoherence-born.md):20,25,36 ($P=V^2/R$; $W_{extracted}$; "irreversibly thermalizes") | ✓ (clm-ldmvwi) |
| **Screen / Born rule** | $P(\text{click}\mid x_n)=\lvert\partial_t\mathbf{A}(x_n)\rvert^2/\!\int\!\lvert\partial_t\mathbf{A}\rvert^2\equiv\lvert\Psi\rvert^2$ | detector capture-work at the Joule-integration boundary | [ohmic-decoherence-born.md](ohmic-decoherence-born.md):40 (7-step chain opens), :55 ("No Born rule input anywhere in the chain"), 36–61 | ✓ (Born-path CLOSED 2026-05-26; AC/sign-symmetric scope :61) |
| **de-Broglie wave** | transverse standing-wave troughs the defect navigates | standing-wave pattern on the line | [ohmic-decoherence-born.md](ohmic-decoherence-born.md):11 | consistency |
| **Visibility vs impedance** | fringe visibility $V$ vs $Z_{det}$ is **continuous** (Γ-detune) | continuous decoherence vs binary collapse | (driver) `double_slit_design_space.py`:17-20 | AVE-distinct falsifiable prediction (§5) |

## §4 — Which-path decoherence and the screen / Born rule (EE form)

**Which-path = Ohmic / Joule decoherence.** To extract which-path information, a detector must physically couple to the vacuum lattice and draw kinetic energy from the $\mathbf{A}$-field — i.e. it acts as a **resistive mechanical load** $Z_{det}$. The work it extracts over a measurement interval is governed by ordinary Joule heating ($P = V^2/R$):

$$W_{extracted} = \int P_{load}\,dt \;\propto\; \frac{\lvert\partial_t\mathbf{A}(x_n)\rvert^2}{Z_{det}}\,\Delta t$$

Drawing this energy **thermalizes** the local phase wave, permanently attenuating the interference gradients — continuous decoherence, not an instantaneous binary collapse. (Canonical: [Ohmic Decoherence and the Born Rule](ohmic-decoherence-born.md) lines 20, 25, 36 — $P=V^2/R$, $W_{extracted}$, "irreversibly thermalizes the spatial pressure wave".)

**The screen is the Born rule, derived.** The probability that the extracted work triggers a discrete click at screen position $x_n$ scales as the squared local field amplitude:

$$P(\text{click}\mid x_n) = \frac{\lvert\partial_t\mathbf{A}(x_n)\rvert^2}{\int\lvert\partial_t\mathbf{A}(\mathbf{x})\rvert^2\,d^3x} \;\equiv\; \lvert\Psi\rvert^2$$

This is **not asserted** — it is derived end-to-end from the master vacuum equation via a 7-step substrate-physics chain (master equation + Axiom-1 Ohmic boundary + FDT/Nyquist + AVE Lagrangian + standard probability theory; **no Born-rule input anywhere in the chain**). The derivation path was **closed 2026-05-26** (Phase 2-A). (Canonical: [Ohmic Decoherence and the Born Rule](ohmic-decoherence-born.md) line 40 — "derived end-to-end from the master vacuum equation via a 7-step substrate-physics chain"; line 55 — "No Born rule input anywhere in the chain"; chain table lines 36–61.)

> **[Resultbox]** *Scope qualifier (carry verbatim)*
>
> The Born-rule derivation applies to **AC signals or sign-symmetric signal ensembles** (the canonical photodetection regime — oscillating EM fields from photon sources). DC / sign-asymmetric signals retain a linear-in-$V_s$ contribution; the $\lvert V_s\rvert^2$ scaling is sub-leading there. (Anchor: [ohmic-decoherence-born.md](ohmic-decoherence-born.md):61, "Scope qualifier: derivation applies to AC signals or sign-symmetric signal ensembles".)

EE reading: the detector is a resistive tap on a transmission line carrying the wake; the click-rate is the time-integrated dissipated power crossing a threshold at the Joule-integration boundary (the "detector capture work-function" row in [translation-circuit.md](../../../common/translation-tables/translation-circuit.md) §4).

## §5 — The AVE-distinct prediction: visibility vs detector impedance

Because which-path decoherence is continuous Ohmic dissipation (§4), fringe **visibility $V$** should vary **continuously** with the detector's impedance $Z_{det}$ (equivalently, with how strongly the detector detunes the local $\Gamma$ from the matched condition) — not jump between two binary outcomes.

> **[Resultbox]** *AVE vs Copenhagen — the falsifiable distinction*
>
> - **Copenhagen:** wave-function collapse is **binary** — the path is either observed (fringes destroyed) or not (fringes intact).
> - **AVE:** decoherence is **continuous** — fringe visibility $V$ degrades in proportion to the detector's impedance perturbation (Γ-detune): a partial, tunable Ohmic tap gives partial visibility.
>
> This is a testable, falsifiable distinction. (Driver: `double_slit_design_space.py` lines 17–20 — Panel 4 sweeps observer impedance 0%→100% damping → continuous decoherence.)

This prediction is the discriminating content of the AVE double-slit: the mechanism reproduces the standard fringe pattern (consistency, §4) but predicts a continuous $V(Z_{det})$ curve where Copenhagen predicts a step.

## §6 — Distinctness guards (what this is NOT)

Three confusions the reconciled canon must not re-introduce:

1. **Ponderomotive wake $\neq$ thrust dark-wake.** The double-slit transverse wake is a **near-field ponderomotive** pressure field $\propto \nabla|\Psi|^2$ that navigates the defect. It is **not** the **far-field dark-wake** $\tau^{far}_{zx}$ (the radiated shear stress that carries reaction momentum for AVE thrust devices). The $\tau_{zx}$ derivation is an explicit **OPEN gap** ([dark-wake-bemf-foc-synthesis.md](../../../common/dark-wake-bemf-foc-synthesis.md):98–100; the symbol $\tau^{far}_{zx}$ is the "dark wake (far-field reaction)" row in [translation-circuit.md](../../../common/translation-tables/translation-circuit.md):144). **Do not import $\tau_{zx}$ / Op14-thrust math into the double-slit analysis.**

2. **The electron's "bubble" $\neq$ the free photon, and $\neq$ a cavitation bubble.** The electron's core is its own $\Gamma=-1$ self-created $0\,\Omega$ cavity (bubble-LIKE, self-confined — the matter core). The **free photon** has NO core and NO bubble (it is matched at $Z_0$, $\Gamma=0$). Separately, the sonoluminescence **cavitation bubble** proper is a DIFFERENT mechanism — saturated Rayleigh-Plesset inertia ($\rho_{eff}=\rho_0/(1-\mathrm{M}^2)^{3/2}$, [sonoluminescence-derivation.md](../../../vol3/applied-physics/ch14-sonoluminescence/sonoluminescence-derivation.md):25–27), NOT the $\Gamma=-1$ impedance cavity. The three must never merge.

3. **The "helical photon" framing is RETRACTED.** Any legacy script or doc calling the photon a "helical soliton" or a **dual-sector** ($u\neq0$ AND $\omega\neq0$) object is using the **empirically-wrong** framing retracted at [photon-identification.md](../ch4-continuum-electrodynamics/photon-identification.md):93 ("Doc 107 correction"). The canonical photon is **single-sector** ($T_2$ only: $\omega\neq0$, $u=0$). The double-slit driver `simulate_double_slit_observer.py` (line 6, "a 'photon' is a helical soliton") uses this **superseded** framing — it is **not** propagated here.

## §7 — Honest-status flags

Carried verbatim per `ave-evidence-framing-discipline`:

- **This leaf is consistency / translation, not emergence.** Every mapping is an identification of already-canonical content (§1). No new derivation; `no-claim:` frontmatter.
- **The Born-rule derivation is closed but scoped.** Closed 2026-05-26 for **AC / sign-symmetric signals** only ([ohmic-decoherence-born.md](ohmic-decoherence-born.md):61, "Scope qualifier"); DC / sign-asymmetric signals retain a sub-leading linear-in-$V_s$ term.
- **The visibility-vs-$Z_{det}$ continuity is a forward prediction, not a closed result.** It is the AVE-distinct falsifiable distinction (§5), driver-explored but not yet experimentally confirmed.
- **The electron-core EE map ($\Gamma=-1$ → shorted $\lambda/4$ resonator) is a DESCRIPTION, gate-(b) CLOSED 2026-06-04.** It describes the electron's trapped-reactive-energy structure; it does **not** derive $R\!\cdot\!r=\tfrac14$ (which is Class-B, `clm-0ktpcn` — see [Photon EE Mapping](../ch4-continuum-electrodynamics/photon-ee-mapping.md) §5 for the full flag).
- **🔴 Soliton self-lock / autoresonance at $\Gamma=-1$ — genesis-from-photon-precursor TESTED-NEGATIVE (2026-06-14; Rule-12 substitution, was "underived ✗ GAP").** The asserted self-lock from a flowing-photon precursor was tested on `crystal_engine` (near-yield-forming) and did NOT occur (NO-GENESIS); the general autoresonance↔substrate mapping + the PLV/autoresonance detector instrument remain open (phasor-redesign prereg deferred). See [photon-ee-mapping.md](../ch4-continuum-electrodynamics/photon-ee-mapping.md):98 + [`research/2026-06-14_t2-genesis-selflock_result.md`](../../../../../research/2026-06-14_t2-genesis-selflock_result.md) (commits `0affe18e`/`09722e2b`). *Prior framing preserved per Rule 12:* **Soliton self-lock / autoresonance at $\Gamma=-1$ is underived** (✗ GAP, [translation-circuit.md](../../../common/translation-tables/translation-circuit.md):207 (Autoresonance row, "GAP — not mapped"), :222 (gap-finding §)). The defect's stable confinement is asserted from the saturation mechanism, not yet derived from an autoresonance / self-lock argument.
- **Helical-photon framing RETRACTED** ([photon-identification.md](../ch4-continuum-electrodynamics/photon-identification.md):93); the `simulate_double_slit_observer.py` "helical soliton" framing is **superseded** (§6.3).
