[↑ Vol 1: Foundations](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-3zz0f6, clm-5xon03, clm-0ktpcn, clm-unk0bd]
-->

# Ch.8: Zero-Parameter Closure — $\alpha$ from the Golden Torus
<!-- claim-quality: clm-0ktpcn -->

**Source:** `manuscript/vol_1_foundations/chapters/08_alpha_golden_torus.tex`

**Scripts:**
- [`derive_alpha_from_golden_torus.py`](../../../src/scripts/vol_1_foundations/derive_alpha_from_golden_torus.py) — multipole evaluation, renders Fig. of trefoil at Golden Torus
- [`verify_clifford_half_cover.py`](../../../src/scripts/vol_1_foundations/verify_clifford_half_cover.py) — rigorous 5-step derivation of $\Lambda_{\text{surf}} = \pi^2$ from spin-1/2 half-cover of $\mathbb{T}^2 \subset S^3 \subset \mathbb{C}^2$
- [`verify_lambda_line.py`](../../../src/scripts/vol_1_foundations/verify_lambda_line.py) — rigorous derivation of $\Lambda_{\text{line}} = \pi \cdot d$ from regime (a) Nyquist + regime (b) diameter convention; verifies multipole closure
- [`ropelength_trefoil_golden_torus.py`](../../../src/scripts/vol_1_foundations/ropelength_trefoil_golden_torus.py) — numerical convergence of composite ropelength + Clifford-torus screening objective to Golden Torus
- [`verify_golden_torus_s11.py`](../../../src/scripts/vol_1_foundations/verify_golden_torus_s11.py) — ABCD cascade infrastructure + algebraic verification

**Engine constants** (from [`ave.core.constants`](../../../src/ave/core/constants.py)):
- `ALPHA_COLD_INV` $= 4\pi^3 + \pi^2 + \pi \approx 137.0363038$
- `ALPHA_COLD` $= 1/\text{ALPHA\_COLD\_INV}$
- `DELTA_STRAIN` $\approx 2.225 \times 10^{-6}$ (CMB thermal correction)

## Topological identity of the electron

The electron is the $0_1$ **unknot** in real space — the simplest closed flux-tube loop with no real-space crossings. The "(2,3) trefoil" that appears throughout this derivation refers to the **phase-space Clifford-torus winding pattern** of the electron's bond-pair LC tank (2 windings on the d-axis, 3 windings on the q-axis), NOT a real-space trefoil knot. The trefoil lives in phase space; the soliton lives in real space.

> → Primary: [$(2,3)$ Torus-Knot Uniqueness](../vol2/particle-physics/ch01-topological-matter/torus-knot-uniqueness.md) — derivation of why $(2,3)$ specifically (vs $(4,3)$, $(5,2)$, etc.) is forced as the electron's phase-space winding: coprimality $\gcd(p,q)=1$ for single-component-knot vs link + both windings $\geq 2$ for non-trivial knotting + minimality (smallest such pair is $(2,3)$, crossing number $c=3$) + electron-is-lightest-non-trivial-lepton. The Phase 2 sub-item 1 (2026-05-25) wiring of this Primary cross-ref closes the prior "(2,3) winding asserted, not derived" caveat on clm-unk0bd and clm-0ktpcn (see [vol1/claim-quality.md](./claim-quality.md)).

## Substrate derivation of the Golden Torus geometry $(R, r, d)$

> **Framing-precision note (Phase 3-A1 reframe, 2026-05-26)**: this section's content is **Class 2 axiom-manifestation** on the substrate-mechanism axis (per `consistency-vs-emergence` v1.2): each of the three regimes is forced by one of the four AVE axioms acting on the electron's $(2,3)$ phase-space Clifford-torus winding, and the three forced equations jointly fix $(R, r, d)$. The standard-physics-community names ("multipole expansion", "fine-structure constant α") that appear later in the chapter are translation references; the substrate-mechanism content lives in this section.

Following the structural pattern used in [Vol 2 Ch 3 §Step 2 PMNS-eigenvalues](../vol2/particle-physics/ch03-neutrino-sector/pmns-eigenvalues.md) — which produces three mixing-angle values by identifying three distinct substrate regimes — the electron unknot's phase-space $(2,3)$ Clifford-torus winding partitions into three substrate regimes, each forcing one independent equation in the unknowns $(R, r, d)$:

| Regime | Substrate-mechanism content | Forced equation |
|---|---|---|
<!-- claim-quality: clm-unk0bd -->
| **(a) Nyquist** | **Ax 1 lattice sampling cutoff**: discrete K4 substrate cannot resolve transverse-cross-section structure below the lattice pitch; the smallest stable soliton (the $0_1$ unknot carrying $(2,3)$ phase-space winding per `clm-unk0bd`) saturates at the Nyquist scale | $d = 1\,\ell_{\text{node}}$ |
| **(b) Crossings** | **Ax 2 topo-kinematic isomorphism + dielectric-rupture self-avoidance**: at topologically-marked phase-space crossings, two flux-tube strands just touch at their edges without dielectric rupture; centerline separation $2(R - r)$ must equal the tube diameter $d$ | $2(R - r) = d \Rightarrow R - r = 1/2$ |
| **(c) Screening (substrate spinor half-cover)** | **Ax 3 minimum-reflection principle + K4-derived spinor structure**: spin-½ on the substrate emerges from the K4 rotation group chain $T = A_4 \to 2T \subset SU(2) \to SO(3)$ (canonical at [`finkelstein-misner-spin-half-derivation`](../vol2/particle-physics/ch01-topological-matter/finkelstein-misner-spin-half-derivation.md), `clm-salw2h`); the 2-to-1 cover forces the electron's physically-distinct observable surface to be half of the standard Clifford-torus surface area on $S^3$ | $(2\pi R)(2\pi r) = \pi^2 \Rightarrow R \cdot r = 1/4$ |

**Substrate-mechanism provenance of regime (c)'s $\pi^2$ surface scale.** The standard Clifford torus $(z_1, z_2) = (r_1 e^{i\theta_1}, r_2 e^{i\theta_2})$ at $r_1 = r_2 = 1/\sqrt{2}$ on $S^3$ has total surface area $A_{\text{standard}} = 2\pi^2$ (a complex-geometry theorem on $S^3$, framework-external mathematics). The electron's substrate spinor structure forces only half of the Clifford torus to correspond to physically distinct observable amplitudes — the other half is the spinor-conjugate image identified to the first by the substrate's 2-to-1 cover. Therefore $\Lambda_{\text{surf}} = \tfrac{1}{2} A_{\text{standard}} = \pi^2$, forced by the substrate spinor structure acting on the substrate-mathematics torus surface area.

**The spinor half-cover is substrate-derived (Class 2 axiom-manifestation), not imported as a standard-physics postulate.** The derivation chain is substrate-native end-to-end:

| Step | Substrate-mechanism content | Status |
|---|---|---|
| 1 | **K4 rotation group**: $T = A_4$ (proper tetrahedral rotation group, $\|T\| = 12$; canonical at [|T|=12 Universality](./axioms-and-lattice/ch1-fundamental-axioms/tetrahedral-t-universality.md)) | Derived (from Ax 1 substrate topology — the K4 lattice symmetry group) |
| 2 | **Double cover**: $2T \subset SU(2)$ | Definitional given step 1 (standard-mathematics double cover of $A_4$) |
| 3 | **Spin-½ extended-defect mechanism**: Finkelstein–Misner / Dirac-belt-trick mechanism on the extended $0_1$ unknot defect embedded in the SO(3) manifold (canonical at [`finkelstein-misner-spin-half-derivation`](../vol2/particle-physics/ch01-topological-matter/finkelstein-misner-spin-half-derivation.md), `clm-salw2h`) | Derived (from steps 1+2 + substrate extended-defect requirement; see [spin-half-paradox](../vol2/appendices/app-b-paradoxes/spin-half-paradox.md) for the standard-physics-community translation context) |
| 4 | **$\pi^2$ half-cover area**: the substrate-distinct observable surface is half of $A_{\text{standard}} = 2\pi^2$, giving $\Lambda_{\text{surf}} = \pi^2$ | Derived (definitional given step 3 substrate-spinor identification of the two cover sheets) |

The standard-physics community calls the structure carried in steps 1-4 the "SU(2) → SO(3) double cover" and the consequence "spin-½ representation theory". The substrate-mechanism content is steps 1-4 above; the standard-physics-community language is a translation reference.

**Remaining open formal-rigor sub-item (substrate-mechanism, regime (c) only):** prove that ropelength-minimality on the K4 substrate uniquely selects the canonical Clifford-torus embedding $r_1 = r_2 = 1/\sqrt{2}$ (a substrate-topology question). The substrate spinor half-cover itself is substrate-derived end-to-end via steps 1-4 above; the open piece is the substrate-mechanism derivation of why ropelength-minimality lands at the canonical embedding rather than at a deformed embedding. A second open formal-rigor item — the functional-orthogonality of the additive assembly — is documented separately in §Topological self-impedance shape factors below.

**Solving (b) ∧ (c):** substitute $r = R - 1/2$ into $R \cdot r = 1/4$:
$$
R(R - 1/2) = 1/4 \implies 2R^2 - R - 1/2 = 0 \implies R = \frac{1 + \sqrt{5}}{4} = \frac{\varphi}{2}
$$
giving the **Golden Torus**: $R = \varphi/2 \approx 0.809$, $r = (\varphi-1)/2 \approx 0.309$.

## Substrate derivation of $\Lambda_{\text{line}} = \pi \cdot d$ from regime (a) + regime (b)

The line shape factor $\Lambda_{\text{line}} = \pi \cdot d$ is forced by two substrate ingredients drawn from the same regime structure that fixed $\Lambda_{\text{vol}}$ and $\Lambda_{\text{surf}}$: regime (a) Ax 1 Nyquist quantization of the substrate tube diameter, and the codimensional identification of the 1-cycle integral with the transverse cross-section perimeter. The factor $\pi$ (not $2\pi$) is forced by the regime (b) self-avoidance convention that makes $d$ a diameter rather than a radius. Each step is parallel in rigor (Class 2 axiom-manifestation) to the substrate spinor half-cover derivation above.

**Identification of $\Lambda_{\text{line}}$ as the substrate 1-cycle integral.**
The codimensional decomposition on $\mathbb{T}^2 \subset S^3 \subset \mathbb{C}^2$ assigns one shape factor per geometric codimension: $\Lambda_{\text{vol}}$ to the 3-cycle phase volume, $\Lambda_{\text{surf}}$ to the 2-cycle Clifford-torus surface, and $\Lambda_{\text{line}}$ to the 1-cycle around the flux tube's transverse cross-section. On the substrate K4-LC network (Ax 1), this 1-cycle integral is realized substrate-mechanically as the Ampère loop $\oint \mathbf{B} \cdot d\boldsymbol{\ell}$ that links transverse flux to circulating displacement current — the natural 1-D codimension integral on the substrate LC network. The line shape factor is the dimensionless length of this substrate Ampère loop.

**Substrate diameter convention from regime (b).**
Regime (b) self-avoidance forces $2(R - r) = d$, where $2(R - r)$ is the closest centerline-to-centerline approach of the unknot's substrate flux-tube strands at a topologically-marked phase-space crossing. For two substrate flux tubes to just touch at their edges (without substrate dielectric rupture), this centerline separation must equal the tube *diameter*, not its radius. This makes $d$ unambiguously the substrate tube diameter throughout the closure system; the corresponding tube radius is $d/2$.

**Substrate Nyquist-quantized cross-section perimeter.**
Regime (a) Ax 1 Nyquist quantizes the minimum substrate-lattice-resolvable tube diameter at $d = 1\,\ell_{\text{node}}$. Below this substrate scale, the discrete K4-LC network cannot represent any transverse cross-section structure at all — sub-pitch "shape" distinctions are unphysical at the substrate level. The 1-cycle integral evaluated around the tube cross-section — in the substrate LC network's continuous-mode envelope, the only meaningful representation at the substrate Nyquist resolving limit — gives the substrate-derived perimeter form for a closed 1-cycle of diameter $d$:

$$
\Lambda_{\text{line}} = 2\pi \cdot (d/2) = \pi \cdot d
$$

This is the *full* perimeter of a 1-cycle of diameter $d$ (equivalently $2\pi$ times its radius $d/2$). The factor $\pi$, rather than $2\pi$, is the substrate consequence of $d$ being expressed as a diameter (regime (b) convention); there is no half-loop in the line shape factor. The $\pi$ itself is the substrate continuous angular factor of the closed 1-cycle integral, structurally parallel to the $2\pi$ factors that enter $\Lambda_{\text{vol}}$ and $\Lambda_{\text{surf}}$ through their 2- and 3-cycle integrals on $\mathbb{T}^2 \subset S^3 \subset \mathbb{C}^2$.

**Closure of regime (a) + regime (b) on $\Lambda_{\text{line}}$.**
At the substrate Nyquist-quantized minimum $d = 1\,\ell_{\text{node}}$:

$$
\Lambda_{\text{line}} = \pi \cdot d = \pi
$$

Each of the three shape factors now carries the same substrate-mechanism structural form: a substrate continuous angular factor (powers of $\pi$ from the closed substrate cycles on $\mathbb{T}^2 \subset S^3 \subset \mathbb{C}^2$) multiplied by a substrate regime-fixed scale. $R \cdot r = 1/4$ from regimes (b) ∧ (c) fixes the scales of $\Lambda_{\text{vol}}$ and $\Lambda_{\text{surf}}$; $d = 1$ from regime (a) Ax 1 Nyquist fixes the scale of $\Lambda_{\text{line}}$. The three substrate regimes do uniform structural work across the three shape factors — $\Lambda_{\text{line}}$ is no longer the odd one out in the substrate-mechanism content. Numerical verification: [`verify_lambda_line.py`](../../../src/scripts/vol_1_foundations/verify_lambda_line.py).

## Topological self-impedance shape factors at the Golden Torus

At the substrate-derived Golden Torus $(R, r, d) = (\varphi/2, (\varphi-1)/2, 1)$, the electron unknot's **topological self-impedance** (the substrate-native name for the dimensionless impedance the unknot presents to itself across its three geometric codimensions — see [`lc-condensate-vacuum.md`](./axioms-and-lattice/ch1-fundamental-axioms/lc-condensate-vacuum.md) for the structural-self-impedance / Q-factor framing) carries three shape factors, one per geometric codimension of the Clifford-torus embedding $\mathbb{T}^2 \subset S^3 \subset \mathbb{C}^2$. With $R \cdot r = 1/4$ and $d = 1$:

| Shape factor | Codimension | Formula | Value | Substrate-mechanism content |
|---|---|---|---|---|
| $\Lambda_{\text{vol}}$ | 3-cycle (phase volume) | $(2\pi R)(2\pi r)(2\pi \cdot 2) = 16\pi^3(R \cdot r)$ | $4\pi^3 \approx 124.025$ | 3-torus phase volume; substrate-spinor temporal $4\pi$ closure (from same K4-rotation-group chain that forces regime (c)) |
| $\Lambda_{\text{surf}}$ | 2-cycle (Clifford-torus surface) | $(2\pi R)(2\pi r) = 4\pi^2(R \cdot r)$ | $\pi^2 \approx 9.870$ | Half of standard Clifford-torus surface area on $S^3$, substrate-spinor spatial half-cover (regime (c) derivation) |
| $\Lambda_{\text{line}}$ | 1-cycle (transverse cross-section perimeter) | $\pi \cdot d$ | $\pi \approx 3.142$ | Ampère 1-cycle around the flux-tube cross-section at Nyquist-quantized diameter $d = 1$ (regime (a) derivation) |

The values of the individual shape factors are forced from substrate primitives by the three-regime derivation above (Class 2 axiom-manifestation). The standard-physics community would call $\Lambda_{\text{vol}} / \Lambda_{\text{surf}} / \Lambda_{\text{line}}$ a "multipole expansion" of the soliton's self-impedance kernel; the substrate-mechanism content is the codimensional decomposition forced by the Clifford-torus embedding plus the three substrate regimes.

**Common substrate-mechanism origin of the $4\pi$ and $\pi^2$ factors.** Both the substrate-spinor temporal $4\pi$ closure (in $\Lambda_{\text{vol}}$, via $r_{\text{phase}} = 2$) and the substrate-spinor spatial half-cover (in $\Lambda_{\text{surf}}$) derive from the same step-1-through-4 chain above: the substrate K4 rotation group → $A_4 \to 2T \subset SU(2) \to SO(3)$ 2-to-1 cover. The electron's substrate phase space traverses $4\pi$ of temporal phase to return to its initial spinor state but only $2\pi$ of spatial phase to close the spatial loop. The $4\pi$ in $\Lambda_{\text{vol}}$ and the half-cover in $\Lambda_{\text{surf}}$ are temporal and spatial substrate-mechanism expressions of one underlying substrate-spinor structure, not independent ad-hoc factors.

### Additive assembly of the shape factors (open structural element)

The framework asserts the additive assembly

$$
\alpha^{-1}_{\text{ideal}} \;\equiv\; \Lambda_{\text{vol}} + \Lambda_{\text{surf}} + \Lambda_{\text{line}} = 4\pi^3 + \pi^2 + \pi \approx 137.0363038
$$

as the **identification** of the three orthogonal codimensions of the Clifford-torus embedding with three independent substrate-mechanism contributions to the unknot's dimensionless topological self-impedance. The codimensional structure justifies the absence of cross-terms only IF the three substrate-mechanism contributions are functionally independent (orthogonal in the sense of irreducible-representation decomposition).

**Honest open-structure note** (carried verbatim from the `clm-0ktpcn` rationale block; see [`vol1/claim-quality.md`](./claim-quality.md)): the leaf's own forms give $\Lambda_{\text{vol}} = 16\pi^3(R \cdot r)$ and $\Lambda_{\text{surf}} = 4\pi^2(R \cdot r)$, so the $(R, r, d) \to \Lambda$ map has only 2-dimensional image — "orthogonality" cannot mean parameter-independence. Establishing functional orthogonality at the substrate-mechanism level (e.g., via Schur orthogonality of substrate-symmetry-group irreducible representations acting on the $(2,3)$ Clifford-torus mode space) is the central remaining open derivation step on this leaf. Phase 3-A2 of the `clm-0ktpcn` strengthening workstream attempts this derivation; until it closes, the additive assembly is best classified as a Class 4 consistency-pattern step (a dimensionally-compatible Clifford-embedded combination hitting the standard-physics-community-measured $\alpha^{-1}$ value to ~10⁻⁶ precision) rather than as Class 2 axiom-manifestation. The Phase 3-A1 prose reframe does **not** close this question.

### Cold-lattice asymptote — substrate prediction vs standard-physics-community-measured target

The substrate-derived cold-lattice asymptote sits at:

> **[Resultbox]** *Cold-lattice topological self-impedance asymptote*
>
> $$
> \alpha^{-1}_{\text{ideal}} = \Lambda_{\text{vol}} + \Lambda_{\text{surf}} + \Lambda_{\text{line}} = 4\pi^3 + \pi^2 + \pi \approx 137.0363038
> $$

**Dual-axis classification per `consistency-vs-emergence` v1.2**:

- **Substrate-mechanism axis**: the $(R, r, d)$ geometry derivation from Ax 1 + Ax 2 + Ax 3 is **Class 2 substrate-mechanism emergence** (each regime is traced step-by-step to its axiom); the additive assembly of $\Lambda_{\text{vol}} + \Lambda_{\text{surf}} + \Lambda_{\text{line}}$ is **Class B substrate-mechanism manifestation** (the framework points at the codimensional structure without deriving functional orthogonality from substrate symmetry group representation theory; Phase 3-A2 open).
- **Observable axis**: the assembled value $137.0363038$ matches the standard-physics-community-measured value (the "fine-structure constant" $\alpha^{-1}_{\text{CODATA}} \approx 137.035999$) to within the cold-lattice / CMB-strain bridge $\delta_{\text{strain}} \approx 2.225 \times 10^{-6}$ documented in §CMB thermal-bridge correction below; this is **Class 4 observable consistency** (the substrate-derived assembly recovers the standard-physics target up to one thermal-bridge scalar). The AVE-distinct content is the substrate-mechanism derivation path of $(R, r, d)$, not the numerical match itself.

## CMB thermal-bridge correction (running of the substrate self-impedance asymptote)
<!-- claim-quality: clm-3zz0f6 -->

The standard-physics-community-measured value is $\alpha^{-1}_{\text{CODATA}} = 137.035999$. This sits below the substrate-derived cold-lattice asymptote by a fractional amount identified as the **vacuum strain coefficient** $\delta_{\text{strain}}$:

$$
\delta_{\text{strain}} = 1 - \frac{137.035999}{137.036304} \approx 2.225 \times 10^{-6}
$$

Substrate-mechanism content: this is the thermal expansion of the substrate's spatial metric at the current cosmological epoch ($T_{\text{CMB}} \approx 2.725$ K), bridging the substrate's $T \to 0$ asymptote to the measured value at finite $T$.

**Predicted / fitted / tested disclosure (per `consistency-vs-emergence` v1.2 master-equation-derivation-path discipline).**

- **Predicted (substrate-derived, Class 2 axiom-manifestation)**: the cold-lattice asymptote $\alpha^{-1}_{\text{ideal}} = 4\pi^3 + \pi^2 + \pi \approx 137.0363038$ from the substrate $(R, r, d)$ geometry derivation above (subject to the additive-assembly open caveat); the *existence* of a positive thermal running of $\alpha^{-1}$ below this asymptote at $T > 0$ (forced by substrate thermal expansion of the spatial metric); the *sign* (substrate gets less stiff at higher $T$, lattice expands, characteristic impedance shifts); the falsifiable substrate claim that $\alpha^{-1}$ decreases further in regions of higher local thermal energy (collider cores, early universe).
- **Fitted (Class 1 identity / one scalar at $T_{\text{CMB}}$)**: the numerical magnitude $\delta_{\text{strain}} \approx 2.225 \times 10^{-6}$, computed by back-substitution from the standard-physics-community-measured value: $\delta_{\text{strain}} \equiv 1 - \alpha^{-1}_{\text{CODATA}}/\alpha^{-1}_{\text{ideal}}$, definitional given the engine's `DELTA_STRAIN = 1 - (1/ALPHA)/ALPHA_COLD_INV` (`src/ave/core/constants.py`). This is a Class A identity at the back-substitution step — the value is **defined** as the difference between substrate prediction and CODATA target, not derived from a substrate thermal-expansion coefficient. The narrative attribution to spatial-metric thermal expansion at $T_{\text{CMB}} = 2.725$ K is a substrate-mechanism story consistent with the predicted sign; it is **not yet** a substrate derivation of the magnitude from $T_{\text{CMB}}$ + a substrate elastic modulus.
- **Tested (Class 4 observable consistency)**: that **one** thermal scalar suffices to bridge the cold-lattice asymptote to the standard-physics-community-measured value. Multi-temperature measurements (collider cores, primordial-nucleosynthesis-era $\alpha$, ultracold cavity experiments) test the same one-scalar substrate-structural claim at different $T$ — falsification on any one kills the one-scalar bridge structure.

The disclosure pattern is structurally identical to Vol 6 nuclear-mass methodology (one fitted scalar per nucleus, with substrate-predicted topology + parameter count): the substrate predicts structure; one numerical scalar is fitted per system; the substrate prediction is falsifiable across the relevant variable. To upgrade $\delta_{\text{strain}}$ from a one-scalar fit (Class A identity at back-substitution) to a full substrate prediction (Class 2 axiom-manifestation on the magnitude as well as the sign), the substrate chain needs to compute the lattice's effective thermal expansion coefficient from substrate primitives — the bulk modulus $G_{\text{vac}}$ (Vol 1 Ch 4) and the equipartition energy at $T_{\text{CMB}}$ — and verify that the substrate-derived $\delta_{\text{strain}}$ matches the back-substituted value within tolerance. That substrate-mechanism magnitude derivation does not currently appear in the corpus; it is queued as a `clm-0ktpcn` strengthen-by item ("Derive δ_strain magnitude at T_CMB to close the cold-lattice → CODATA bridge rather than back-substituting it").

**Falsifiable substrate prediction (sign, not magnitude).** The substrate self-impedance asymptote $\alpha^{-1}_{\text{ideal}}$ is a literal mechanical property of the substrate K4-LC lattice and acts as a running coupling — the substrate-mechanism content is that the substrate gets less stiff at higher $T$, so the asymptote shifts. In regions of extreme localized thermal energy (collider cores, early universe), $\alpha^{-1}$ decreases further below the standard-physics-community-measured $\approx 137.036$. The cold-lattice $137.0363038$ is the substrate's $T \to 0$ asymptote.

This is distinct from the proton thermal softening $\delta_{th} = 1/(14\pi^2) \approx 7.21 \times 10^{-3}$ at the $10^{13}$ K proton core — different temperature regime, different substrate quantity (the substrate-derived Skyrme coupling $\kappa_{FS}$), not the substrate self-impedance asymptote directly.

## Substrate-mechanism closure status
<!-- claim-quality: clm-5xon03 -->

Ax 1 calibrates $\ell_{\text{node}}$ to the ground-state rest-mass of the smallest topologically stable substrate soliton (the electron as the $0_1$ unknot carrying $(2,3)$ phase-space Clifford-torus winding). Because the electron is the absolute structural failure mode of the substrate, its substrate topological self-impedance ($\approx 137.036$) *physically becomes* the macroscopic non-linear saturation bound for the rest of the substrate's behavior. This is why the substrate self-impedance asymptote serves identically as the dielectric-saturation bound in Ax 4.

**Closure status disclosure (honest).** The framework reduces 26 standard-physics-community-named parameters (the SM parameter count) to a 3-element bounding set $\{m_e, \alpha, G\}$ + four substrate axioms. The "zero free parameters" headline depends on Layer 8 closure of those three, which itself rests on:

- **(a) Substrate $(R, r, d)$ geometry derivation at cold-lattice asymptote (Class 2 axiom-manifestation on (R, r, d); Class B + Class 4 on the additive assembly)**: the three substrate regimes (Ax 1 Nyquist + Ax 2 self-avoidance + Ax 3 spinor half-cover) jointly fix $(R, r, d)$ from substrate primitives. The additive assembly $\Lambda_{\text{vol}} + \Lambda_{\text{surf}} + \Lambda_{\text{line}}$ is currently a substrate-mechanism manifestation of the codimensional structure pointing at the standard-physics-community-measured $\alpha^{-1}$ to high precision; functional-orthogonality at the substrate symmetry-group level is the open derivation step (Phase 3-A2 of the `clm-0ktpcn` strengthening workstream).
- **(b) Thermal-bridge running $\alpha^{-1}(T) = \alpha^{-1}_{\text{ideal}}(1 - \delta_{\text{strain}}(T))$ (Class 2 sign + existence; Class A identity on magnitude)**: the *existence* and *sign* of positive $\delta_{\text{strain}}$ at $T > 0$ are substrate-derived from thermal expansion of the substrate spatial metric; the *magnitude* at $T_{\text{CMB}}$ is currently one back-substituted scalar (definitional given the engine constants module — see §CMB thermal-bridge correction above).
- **(c) One of $\{m_e, \ell_{\text{node}}\}$ being computable from the other via the substrate unknot ground state (Class 2 axiom-manifestation)**: the electron's ground-state substrate body is the $0_1$ unknot — see §Topological identity of the electron above. The other of $\{m_e, \ell_{\text{node}}\}$ remains the input mass scale.

Conditional on (a)+(b)+(c), the framework is zero-free-parameters at the SM level. Under the present edition, the cold-lattice asymptote and the existence + sign of the thermal-bridge running are substrate-predicted; the magnitude of $\delta_{\text{strain}}$ at $T_{\text{CMB}}$ is one back-substituted scalar — same predicted/fitted disclosure pattern as Vol 6 nuclear-mass methodology (predicted: substrate topology + parameter count; fitted: one scalar). See the [Full Derivation Chain](../common/full-derivation-chain.md) scorecard for the precise accounting per substrate-mechanism layer.

**Class E operating-point projection structure (substrate-cosmology hand-off, refined 2026-05-15 evening).** Per `consistency-vs-emergence` v1.2 Class E classification: the framework is reduced from "three independent calibration constants $(\alpha, G, \ell_{\text{node}})$" to a **one-cosmological-parameter** substrate model with three observational projections. The single cosmological initial-data parameter $\Omega_{\text{freeze}}$ (the substrate's rotation rate at lattice genesis) sets the substrate magic-angle operating point $u_0^*$; from $u_0^*$ the framework derives:

1. **Projection 1 (electromagnetic)**: the substrate self-impedance asymptote $\alpha^{-1}$ via the Golden Torus $(R, r, d)$ derivation above (substrate-mechanism content of the present chapter)
2. **Projection 2 (gravitational)**: $G = c^4 / (7\xi T_{EM}(u_0^*))$ via the Machian impedance integral (see Vol 3 Ch 4)
3. **Projection 3 (cosmological)**: $\mathcal{J}_{\text{cosmic}}$ via $\Omega_{\text{freeze}} = \mathcal{J}_{\text{cosmic}} / I_{\text{cosmic}}$ measured from CMB / LSS anomaly observables

**All three projections must yield the same $u_0^*$** or the one-cosmological-parameter substrate model is falsified. This is the Class E joint-constraint structure: substrate has ONE degree of freedom (the operating point); N observables project onto N separable measurable channels, joint-constrained — falsification of any one kills $u_0^*$ and therefore the substrate model. See [A-031 refined: cosmic-parameter horizon vs observable mechanism](../common/cosmic-parameter-horizon-a031-refinement.md) for the full three-projection framework commitment and the substrate-observability separation of inaccessible cosmic parameters from observable mechanism (per A-034). The 26 standard-physics-community-named SM parameters are then determined by four substrate axioms + the single cosmological IC + the substrate-topological requirement that the smallest stable soliton is the $0_1$ unknot carrying $(2,3)$ phase-space winding.

---

> → Primary: [Calibration and Cutoff Scales](./axioms-and-lattice/ch1-fundamental-axioms/calibration-cutoff-scales.md) — prerequisite framing of $\ell_{\text{node}}$, $\alpha$, $G$
>
> → Primary: [Zero-Parameter Universe](./axioms-and-lattice/ch1-fundamental-axioms/zero-parameter-universe.md) — original EMT-chain framing; this chapter provides the closure
>
> → Primary: [Full Derivation Chain](../common/full-derivation-chain.md) — Layer 8 Zero-Parameter Closure
>
> ↗ See also: [Vol 2 Ch 3 PMNS eigenvalues](../vol2/particle-physics/ch03-neutrino-sector/pmns-eigenvalues.md) — the three-regime rigor pattern this chapter applies
