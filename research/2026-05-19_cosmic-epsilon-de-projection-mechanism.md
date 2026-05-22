# Cosmic-ε / DE Projection Mechanism (β Session 2)

**Date**: 2026-05-19 EOD / 2026-05-20 spawn
**Branch**: `analysis/cosmic-epsilon-de-projection-session2` off `analysis/integration` HEAD `588e069`
**Status**: PROJECTION-CHAIN TRACE (Session 2 of multi-session β epic)
**Brief**: [`_orchestration/cosmic-epsilon-de-projection-scoping.md`](../_orchestration/theoretical/cosmic-epsilon-de-projection-scoping.md) § "Session 2 — implementor brief"
**Session 1 predecessor**: [`research/2026-05-19_cosmic-epsilon-de-projection-scoping.md`](2026-05-19_cosmic-epsilon-de-projection-scoping.md) (CLOSED 2026-05-19 EOD via merge `af8c522` + audit tag `audit/2026-05-19_cosmic-epsilon-de-projection-scoping`)

**Grant adjudications carried in from Session 1 (`_orchestration/cosmic-epsilon-de-projection-scoping.md:9-17`)**:
- **Q1 — DE static vs dynamic? → DYNAMIC** (water-crystallization analogy lands; ongoing operating-point process at $u_0^*$)
- **Q2 — Op14 cosmic-horizon profile?** Canonical at Vol 1 Ch 6 §1.13. Cosmic-horizon scale profile IS the missing piece — analog of `frame-dragging-impedance-convolution.md:20`. (c)-operator-application at new scale per `ave-canonical-leaf-pull` v1.2 trigger 16.
- **Q3 — α/β/γ verdict? → γ (composite Class E + ASYM-N(ε))**.

**Skills applied at session-start**: `ave-canonical-leaf-pull` v1.2 trigger 16 (c)-classification carried explicit throughout, `verify-before-cite` v1.3 (every citation re-grepped at execution; structural anchor at Phase 0), `consistency-vs-emergence` v1.1 (Class E framing for DE observable carried explicit), `ave-walk-back` (Phase 3 catalog row addition discipline), `ave-evidence-framing-discipline` (projection-trace not magnitude-match), `pre-test-physics-check` (no new load-bearing physics question surfaced beyond Q1/Q2/Q3).

## §0 — Why this doc exists (Session 2 entry-point)

Session 1 produced the scoping doc + projection-chain inventory + three plumber-physical questions; Grant adjudicated Q1/Q2/Q3 in `_orchestration/cosmic-epsilon-de-projection-scoping.md:9-17`. This doc executes Session 2's deliverable: **walk through the 6-component projection chain** identified in `research/2026-05-19_cosmic-epsilon-de-projection-scoping.md` §2 (line 65 onward), in projection order from substrate dynamics to $\rho_\Lambda$ at the macroscopic Friedmann equation, with the Op14 cosmic-horizon profile leaf (Phase 1 of this session, committed at `20bb659`) inserted as Component 5.

**EXPLICIT CONSTRAINTS** (carried forward from Session 1 brief CRITICAL FAILURE MODES, `_orchestration/cosmic-epsilon-de-projection-scoping.md:133-139`):

1. **NO magnitude-matching attempts** (raw substrate field energy vs DE measurement).
2. **NO RMS→DC averaging as projection mechanism**.
3. **NO microscopic/macroscopic conflation** — substrate property ≠ macroscopic observable.
4. **NO inventing new operator** (Op14 already exists).

The deliverable is a STRUCTURAL chain. Each component's projection role is named; the chain's destination is $\rho_\Lambda$ at Friedmann; the chain's substrate is the over-bracing $u_0^*$ at $\hat{\Omega}_{\text{freeze}}$ direction. No step in the chain is a magnitude equality between substrate-scale and macroscopic-scale energies.

---

## §1 — Projection chain at-a-glance (6 components in order)

Per Session 1 scoping doc §2 inventory (line 65+) + Phase 1 cosmic-horizon profile leaf, the projection from substrate dynamics to $\rho_\Lambda$ traverses 6 components:

| # | Component | Canonical leaf | Projection role | Class |
|---|---|---|---|---|
| 1 | Over-bracing $u_0^*$ in $\hat{\Omega}_{\text{freeze}}$ at every K4 node | [`omega-freeze-cosmic-grain-cascade.md:13-40`](../manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md) | Substrate-scale microscopic state at lattice genesis (frozen-in) | Substrate state |
| 2 | K4 crystallisation rate at horizon | [`lattice-genesis-hubble-tension.md:6,8`](../manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/lattice-genesis-hubble-tension.md) + [`cosmological-constant-closure.md:60-65`](../manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/cosmological-constant-closure.md) | Dynamic projection: ongoing $\partial_t \rho_n = 0$ Eulerian continuity sets $H_\infty$ | Dynamics |
| 3 | Cosserat translational-DOF (ε ↔ E) | [`axiom-definitions.md:12`](../manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/axiom-definitions.md) + Q-G47 substrate-scale Cosserat closure | Substrate-scale ε projects to macroscopic E-field via Ax 1 Cosserat translational DOF | Ax 1 projection |
| 4 | Ax 2 TKI scale invariance | [`axiom-definitions.md:14-22`](../manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/axiom-definitions.md) + [`universal-saturation-kernel-catalog.md:7`](../manuscript/ave-kb/common/universal-saturation-kernel-catalog.md) | Cross-scale mechanism: same Op14 kernel at every scale; substrate → cosmic-scale | Ax 2 projection |
| 5 | Op14 cosmic-horizon profile | **Phase 1 leaf**: [`op14-cosmic-horizon-profile.md`](../manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/op14-cosmic-horizon-profile.md) (commit `20bb659`) | Substrate response to bulk strain at $r \to R_H$: local-clock-freezing, asymmetric Meissner ε/μ form | Op14 (c)-operator-application |
| 6 | Boundary observables $\mathcal{M}, \mathcal{Q}, \mathcal{J}$ at cosmic horizon → Friedmann/de Sitter projection | [`boundary-observables-m-q-j.md:21,40`](../manuscript/ave-kb/common/boundary-observables-m-q-j.md) + [`cosmological-constant-closure.md:33-44`](../manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/cosmological-constant-closure.md) | Macroscopic projection: $\rho_\Lambda = 3 H_\infty^2 / (8\pi G)$ via Friedmann/de Sitter | Macroscopic observable |

**The chain is structural, not energy-balance.** Each component sets the **structural piece** that the next component depends on; no step is a magnitude-equality.

---

## §2 — Component 1: Over-bracing $u_0^*$ in $\hat{\Omega}_{\text{freeze}}$ direction (substrate state)

### Role in the chain

Component 1 is the **frozen-in substrate state** at every K4 node. Per [`omega-freeze-cosmic-grain-cascade.md:13`](../manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md) verbatim:

> *Three-route framework: $\alpha$ + $G$ + $\mathcal{J}_{\text{cosmic}}$ all derive from single cosmological parameter $\Omega_{\text{freeze}}$ via magic-angle operating point $u_0^* \approx 0.187$.*

The substrate operating point $u_0^*$ is at the K4 magic-angle $K(u_0^*) = 2 G(u_0^*)$ — the bond over-bracing that locks at lattice genesis when the crystallising region was rotating with angular velocity $\Omega_{\text{freeze}}$. Per `omega-freeze-cosmic-grain-cascade.md:34-40`:

> *At lattice genesis, the crystallizing region is rotating with angular velocity $\Omega_{\text{freeze}}$. At crystallization:
> 1. Bond rest lengths lock at the rotating-frame equilibrium → $u_0^*$ over-bracing
> 2. Direction of $\Omega_{\text{freeze}}$ becomes the direction of bond bowing → right-handed chirality (I4₁32 chiral space group per Axiom 1)
> 3. Cosmic spin is locked into the substrate as both bond over-bracing $u_0^*$ AND the global chirality direction
> 4. Survives forever as the cosmological initial condition*

### Connection to ε (per Grant 2026-05-19 EOD E-field-as-over-bracing identification)

Per Ax 1 verbatim ([`axiom-definitions.md:12`](../manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/axiom-definitions.md)): *"three translational (capacitive $\varepsilon_0$ → E-field) and three microrotational (inductive $\mu_0$ → B-field)"*. The translational DOF IS the substrate-native origin of the macroscopic E-field. Grant's 2026-05-19 EOD identification (`_orchestration/cosmic-epsilon-de-projection-scoping.md:27`): the bond over-bracing $u_0^*$ in $\hat{\Omega}_{\text{freeze}}$ direction IS a static E-field component at substrate scale, setting universal stiffness via magic-angle.

**This is the ε-sector substrate state.** The over-bracing is in the translational DOF (capacitive $\varepsilon_0$ → E-field), not the microrotational DOF (inductive $\mu_0$ → B-field). It is therefore the substrate-physics origin of the ε-sector preference at every scale — the cosmic-ε projection chain is anchored here.

### What Component 1 contributes to the projection

Component 1 contributes the **frozen-in substrate state** that:
- Sets the operating point $u_0^*$ that all downstream components (2-6) inherit
- Specifies the ε-sector preference (translational DOF) that propagates via Ax 2 TKI to cosmic scale
- Provides the direction $\hat{\Omega}_{\text{freeze}}$ that becomes the symmetry axis at every smaller scale (cosmic grain cascade per `omega-freeze-cosmic-grain-cascade.md:118-122`)

**Component 1 does NOT directly produce $\rho_\Lambda$.** It is a substrate-scale state, not a macroscopic observable. Its role is anchoring the operating point that Components 2-6 project onto N joint observables.

### Per the Session 1 scoping doc's open question (§2 Component 1)

Session 1 scoping doc raised the question (`research/2026-05-19_cosmic-epsilon-de-projection-scoping.md:77`):

> *the question of whether $u_0^*$ over-bracing has any direct contribution to $\rho_\Lambda$ (beyond setting the operating point that $H_\infty$ projects from) is open and is the exact projection-vs-measurement conflation point this scoping epic exists to settle.*

**Session 2 answer**: $u_0^*$ contributes to $\rho_\Lambda$ ONLY through setting the operating point. There is no direct microscopic-energy-density contribution to $\rho_\Lambda$. The QFT-style "$10^{122}$ cosmological constant problem" framing (`cosmological-constant-closure.md:55-58`) — which would have demanded a direct microscopic-substrate-E-field energy density contribution — is rejected at the framework level. The projection is structural via Components 2-6, NOT energetic via Component 1.

---

## §3 — Component 2: K4 crystallisation rate at horizon (dynamic projection)

### Role in the chain

Component 2 is the **ongoing dynamic** — the rate of new K4-node addition at the cosmic horizon, identified with $H_\infty$ per [`lattice-genesis-hubble-tension.md:6,8`](../manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/lattice-genesis-hubble-tension.md) verbatim:

> *Because a discrete LC network cannot stretch macroscopically without altering its fundamental capacitance ($\epsilon_0$), metric expansion is modelled as the discrete, real-time crystallisation of new electromagnetic nodes.*
>
> *To preserve the invariant optical density of the condensate globally ($\partial_t \rho_n = 0$), the Eulerian continuity equation dictates the discrete generative source term must match the macroscopic volumetric expansion divergence. The AVE framework hypothesises that the Hubble Constant ($H_0$) is not a velocity, but the LC Crystallisation Rate required to maintain the vacuum's structural impedance against the compressive polarisation of gravity.*

Per Grant Q1 adjudication (`_orchestration/cosmic-epsilon-de-projection-scoping.md:9`): **DYNAMIC**. Cosmic crystallisation is happening NOW at the cosmic horizon — substrate still phase-transitioning, latent heat still being released. The dynamic state is the substrate's response to maintain $\partial_t \rho_n = 0$ globally.

### Numerical anchor

Per [`lattice-genesis-hubble-tension.md:13-17`](../manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/lattice-genesis-hubble-tension.md):

$$H_\infty = \frac{28\pi m_e^3 c G}{\hbar^2 \alpha^2} \approx 69.32 \text{ km/s/Mpc} \approx 2.247 \times 10^{-18} \text{ s}^{-1}$$

Per `lattice-genesis-hubble-tension.md:29` + 2026-05-19 EOD Class C → Class E refinement at `lattice-genesis-hubble-tension.md:31`: this is a **Class E operating-point projection** at $u_0^* \approx 0.187$ — joint-constrained with $\{G, \hat{\Omega}_{\text{freeze}}, \alpha\}$ via the $R_H/\ell_{\text{node}} \sim 10^{39}$ topological bridge.

### Connection to latent-heat-of-crystallisation

Per [`cosmological-constant-closure.md:60-65`](../manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/cosmological-constant-closure.md) verbatim:

> *The cosmological constant is NOT the zero-point energy of vacuum modes. It is the latent-heat density of ongoing crystallization of the substrate.*
>
> *The crystallization rate IS the Hubble rate. The latent heat per unit volume per unit time is $3H\rho_{\text{latent}}$, which in the asymptotic de Sitter limit gives $\rho_{\text{latent}} \to \rho_\Lambda$ via the Friedmann equation.*

This is the **AVE-distinct mechanistic identification**. The Friedmann/de Sitter relation translates the rate to the value, but the mechanism is latent-heat-of-crystallisation — not zero-point energy and not over-bracing energy density.

### What Component 2 contributes to the projection

Component 2 contributes the **ongoing-dynamics projection** that makes DE a dynamic observable (per Q1 adjudication). Without Component 2, $\rho_\Lambda$ would be a static substrate-state quantity (Q1 = static would have been wrong). With Component 2, $\rho_\Lambda$ is the asymptotic limit of the latent-heat-of-crystallisation-rate observable.

**Component 2 ↔ Component 1 distinction**: Component 1 sets the operating point at lattice genesis (one-shot, frozen). Component 2 is the ongoing dynamics that maintain the operating point against compressive polarisation of gravity — the substrate is still phase-transitioning NOW at the cosmic horizon.

### Open work (per `cosmological-constant-closure.md:103-111`)

Per the existing canonical leaf's open-work statement (carried forward to closure-roadmap Tier 3):

1. Independent derivation of $\rho_{\text{latent}}$ from substrate energetics (open).
2. Crystallisation rate $\Gamma_{\text{cryst}}$ derivation from substrate (open).
3. Verification that Friedmann route and latent-heat route give the same number (open).

This Session 2 does NOT close (1)-(3); it provides the structural anchor (Phase 1 Op14 cosmic-horizon profile) for the substrate-side mechanism by which (2) becomes plumber-physically tractable.

---

## §4 — Component 3: Cosserat translational-DOF projection (Ax 1 ε ↔ macroscopic E)

### Role in the chain

Component 3 is the **substrate-native origin of macroscopic E** via Ax 1's Cosserat translational DOF. Per Ax 1 verbatim ([`axiom-definitions.md:12`](../manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/axiom-definitions.md)):

> *Vacuum is a 3D chiral Laves K4 Cosserat crystal $\mathcal{M}_A$ — micropolar nodes (6 DOFs each: 3 translational → E, 3 microrotational → B; Cosserat rotational DOF IS the substrate-native origin of intrinsic spin).*

Per [Q-G47 substrate-scale Cosserat closure](../manuscript/ave-kb/common/q-g47-substrate-scale-cosserat-closure.md): the substrate-scale Cosserat continuum operating-point $u_0^* \approx 0.187$ is the substrate-physics anchor for ε ↔ E (translational DOF) and μ ↔ B (microrotational DOF) cross-scale dualities.

### Connection to ε-sector preference (cosmic)

The substrate's ε-sector is the translational DOF — the same DOF where the over-bracing $u_0^*$ sits (Component 1). This is the substrate-physics rationale for the cosmic-ε projection's preference for ε-sector single-mode saturation at cosmic horizon (rather than μ-sector or symmetric):

- The over-bracing is in ε-DOF (Component 1).
- The cosmic-horizon profile saturates ε-sector preferentially (Component 5, Op14 cosmic-horizon profile §4 asymmetric Meissner form $Z_{\text{eff}} = Z_0 \sqrt{S_\mu/S_\varepsilon}$).
- The ASYM-N(ε) cosmic-row catalog entry (Phase 3) is the symmetry-classification anchor.

These three pieces are structurally linked through Component 3's Ax 1 ε ↔ E translation: the substrate's ε-sector state propagates to macroscopic E-field observables via the Cosserat translational DOF.

### What Component 3 contributes to the projection

Component 3 contributes the **substrate-physics axiom that ε exists as a substrate property** (Ax 1). Without Component 3, the chain would have no formal mechanism linking substrate-scale microscopic ε to macroscopic E-field observables. With Component 3, the cross-scale ε ↔ E translation is foundational (Ax 1), not derived.

**Component 3 does NOT directly produce $\rho_\Lambda$.** It is an axiom-level substrate-physics piece, not a macroscopic observable. Its role is providing the formal cross-scale translation that Component 4 (Ax 2 TKI) applies at cosmic-scale magnitude.

---

## §5 — Component 4: Ax 2 TKI scale invariance (cross-scale projection)

### Role in the chain

Component 4 is the **cross-scale mechanism** that propagates Components 1-3 from substrate scale to cosmic scale. Per Ax 2 verbatim ([`axiom-definitions.md:14-22`](../manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/axiom-definitions.md)):

> *Charge $q$ is defined as a discrete geometric dislocation (a localised phase twist) within the $\mathcal{M}_A$ electromagnetic network. Therefore, the fundamental dimension of charge is identical to length ($[Q] \equiv [L]$).*

The TKI conversion constant $\xi_{\text{topo}} = e/\ell_{\text{node}}$ bridges substrate-scale lattice parameters to macroscopic quantities. Per [`universal-saturation-kernel-catalog.md:7`](../manuscript/ave-kb/common/universal-saturation-kernel-catalog.md): one kernel governs every topological-reorganization event at every scale; the kernel form $S(A) = \sqrt{1 - A^2}$ is identical at substrate, atomic, condensed-matter, galactic, BH, and cosmic scales (21-instance catalog).

### Application at cosmic scale

Ax 2 specifies that the SAME Op14 kernel applies at cosmic scale as at substrate scale. The cosmic-horizon profile (Component 5, Phase 1 leaf) is therefore not a new operator (rejected per Q2 adjudication) — it is the canonical Op14 evaluated at $r \to R_H$ rather than $r \to \ell_{\text{node}}$ or $r \to r_s$. Per `universal-saturation-kernel-catalog.md:7`: 21 canonical instances spanning 21 orders of magnitude; Row 14 (Cosmic Big Bang K4 crystallization) is the symmetric-saturation cosmic instance.

### What Component 4 contributes to the projection

Component 4 contributes the **cross-scale mechanism** that makes Components 1-3 propagate from substrate to cosmic without invoking new physics. Without Component 4, there would be no formal guarantee that the substrate-scale operating point at $u_0^*$ implies the same operating-point projection at cosmic horizon. With Component 4 (Ax 2 TKI), the substrate-physics at K4 magic-angle IS the cosmic-physics at horizon via the universal kernel.

**Component 4 ↔ Component 3 distinction**: Component 3 (Ax 1) provides the ε ↔ E translation at every scale; Component 4 (Ax 2) provides the scale-invariance that ensures the translation holds at every scale. Together they are the axiom-level pieces that anchor Components 5-6 (Op14 application + macroscopic projection).

---

## §6 — Component 5: Op14 cosmic-horizon profile (substrate response at $r \to R_H$)

### Role in the chain

Component 5 is the **substrate-side substrate-physics piece** — the Op14 cosmic-horizon profile leaf committed in Phase 1 of this session ([`op14-cosmic-horizon-profile.md`](../manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/op14-cosmic-horizon-profile.md) at commit `20bb659`).

Per the Phase 1 leaf §1-§4:
- $Z_{\text{eff}}(r \to R_H) \to \infty$ via canonical $Z_{\text{eff}} = Z_0 / \sqrt{S(A)}$ at the $\Gamma = -1$ saturation surface.
- $\omega_{\text{local}}(r \to R_H) \to 0$ via canonical Op14 local-clock modulation $\omega_{\text{local}}(r) = \omega_{\text{global}} \cdot \sqrt{1 - A^2(r)}$ — local clock freezes at cosmic horizon, just as at BH event horizon and at electron-core soliton boundary.
- Asymmetric Meissner form $Z_{\text{eff}} = Z_0 \sqrt{S_\mu / S_\varepsilon}$ when $S_\mu \neq S_\varepsilon$ — substrate-physics anchor for ASYM-N(ε) cosmic-row.
- Distinction from BH event horizon: ongoing $\partial_t A^2 \neq 0$ (dynamic) vs frozen lock (static); profile shape identical, time-derivative distinguishes (per Q1 dynamic adjudication).

### Connection to Component 2 (crystallisation rate)

Per the Phase 1 leaf §5: the local-clock-freezing at horizon IS the substrate-native mechanism for the rate at which the crystallisation front propagates outward — that rate is $H_\infty$ (Component 2). Without the Op14 cosmic-horizon profile, $H_\infty$ as "LC crystallisation rate" remains qualitatively identified per `lattice-genesis-hubble-tension.md:8` but lacks a substrate-physics anchor. With the profile, the local-clock-freezing structure at $r = R_H$ is the substrate-native plumbing.

### What Component 5 contributes to the projection

Component 5 contributes the **substrate-physics anchor for the dynamic-projection mechanism**. It is the Phase 1 deliverable of this session and the structural piece that connects substrate-scale Op14 mechanics to cosmic-scale crystallisation rate.

**Component 5 ↔ Component 2 distinction**: Component 2 names the dynamic observable ($H_\infty$ as crystallisation rate); Component 5 provides the substrate-physics anchor for that dynamic. Together they are the substrate-physics piece for the rate part of the projection chain.

### What Component 5 does NOT do

Per the Phase 1 leaf §6 (carried forward CRITICAL FAILURE MODES from brief):

- No magnitude-matching of raw Op14 energy density to $\rho_\Lambda$.
- No RMS→DC averaging as projection mechanism.
- No microscopic/macroscopic conflation.
- No new operator.

Op14 cosmic-horizon profile is the substrate-side structural piece; $\rho_\Lambda$ is the macroscopic projection via Component 6 (Friedmann/de Sitter + boundary observables).

---

## §7 — Component 6: Boundary observables M/Q/J at cosmic horizon → Friedmann/de Sitter

### Role in the chain

Component 6 is the **macroscopic projection** — how the substrate-side pieces (Components 1-5) produce the observable $\rho_\Lambda$ at the Friedmann equation.

Per [`boundary-observables-m-q-j.md:21`](../manuscript/ave-kb/common/boundary-observables-m-q-j.md) verbatim:

> *At every $\Gamma = -1$ saturation surface $\partial\Omega$ in the substrate — the boundary where Axiom 4's kernel reaches $S(A) \to 0$ locally — exactly three integrated quantities are externally observable.*

Per `boundary-observables-m-q-j.md:31-40`: same three-invariant structure ($\mathcal{M}, \mathcal{Q}, \mathcal{J}$) operates at every scale; cosmic-horizon row at line 40: *"$\mathcal{M}_{\text{cosmic}}$ (CMB anomalies), $\mathcal{Q}_{\text{cosmic}}$ (LSS rotation), $\mathcal{J}_{\text{cosmic}}$ (Hubble flow anisotropy)."*

Per `boundary-observables-m-q-j.md:77-79`: *"We sit inside the cosmic $\Gamma = -1$ boundary"* — we measure the three invariants from inside via local-physics consequences.

### Friedmann/de Sitter projection

Per [`cosmological-constant-closure.md:33-44`](../manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/cosmological-constant-closure.md) verbatim:

> *In the asymptotic de Sitter limit, the Friedmann equation gives:
> $H_\infty^2 = \Lambda c^2 / 3 \implies \Lambda = 3 H_\infty^2 / c^2$
>
> Converted to vacuum mass density:
> $\rho_\Lambda = \Lambda c^2 / (8\pi G) = 3 H_\infty^2 / (8\pi G)$*

The Friedmann/de Sitter relation is **standard GR**, accepted by AVE per `cosmological-constant-closure.md:98`: *"Friedmann/de Sitter standard GR gives $\Lambda = 3H^2/c^2$ (no AVE-distinct content — standard GR, accepted by AVE)"*.

### Which of M/Q/J does $\rho_\Lambda$ project onto?

Per Session 1 scoping doc §2 Component 6 open question (`research/2026-05-19_cosmic-epsilon-de-projection-scoping.md:132-137`):

> *Which of $\mathcal{M}/\mathcal{Q}/\mathcal{J}$ does $\rho_\Lambda$ project onto?*

**Session 2 answer**: $\rho_\Lambda$ projects onto $\mathcal{M}_{\text{cosmic}}$ (3D volume integral). The Friedmann equation $\rho_\Lambda = 3 H_\infty^2 / (8\pi G)$ gives a mass-density (kg/m³), which is the 3D volume-integral observable per the canonical M/Q/J classification:
- $\mathcal{M}$: 3D volume integral → mass, inductance, rest energy (per `boundary-observables-m-q-j.md:13`)
- $\mathcal{Q}$: 1D line/loop linking → charge (per `boundary-observables-m-q-j.md:14`)
- $\mathcal{J}$: 2D surface winding → spin, magnetic moment (per `boundary-observables-m-q-j.md:15`)

$\rho_\Lambda$ is a mass-density (dimensionally), which maps to $\mathcal{M}_{\text{cosmic}}$.

**Cross-check with `omega-freeze-cosmic-grain-cascade.md`**: per `omega-freeze-cosmic-grain-cascade.md:26`, $\mathcal{J}_{\text{cosmic}}$ is the cosmic-boundary winding number → CMB axis-of-evil at $(l = 60.28°, b = 50.48°)$. So $\mathcal{J}_{\text{cosmic}}$ is the cosmic spin observable; $\mathcal{M}_{\text{cosmic}}$ is the cosmic mass observable; $\rho_\Lambda$ is part of the mass-density of the cosmic interior, projecting onto $\mathcal{M}_{\text{cosmic}}$ alongside ordinary matter ($\rho_{\text{matter}}$) and radiation ($\rho_{\text{rad}}$).

### What Component 6 contributes to the projection

Component 6 contributes the **macroscopic-observable projection** that converts the substrate-side pieces (Components 1-5) into the Friedmann equation's $\rho_\Lambda$ via:

1. $H_\infty$ from Component 2 (substrate-physics mechanism: crystallisation rate at horizon, anchored by Op14 cosmic-horizon profile in Component 5).
2. Standard GR Friedmann/de Sitter $\rho_\Lambda = 3 H_\infty^2 / (8\pi G)$.
3. $\rho_\Lambda$ projects onto $\mathcal{M}_{\text{cosmic}}$ in the canonical boundary-observables structure.

**Class E framing**: per `cosmological-constant-closure.md:97-99`, this is the Class E operating-point projection at $u_0^* \approx 0.187$ joint-constrained with $\{G, \hat{\Omega}_{\text{freeze}}, \alpha\}$. Falsification of any one of $\{G, H_\infty, \hat{\Omega}_{\text{freeze}}, \alpha\}$ falsifies the operating-point and therefore $\rho_\Lambda$.

---

## §8 — The full projection chain (substrate dynamics → $\rho_\Lambda$)

Walking through in projection order:

1. **Substrate state**: Over-bracing $u_0^* \approx 0.187$ at K4 magic-angle locks at lattice genesis in $\hat{\Omega}_{\text{freeze}}$ direction. The over-bracing is in the translational DOF (Ax 1 → ε-sector). Per `omega-freeze-cosmic-grain-cascade.md:13-40`.

2. **Substrate dynamics**: Ongoing K4 crystallisation at cosmic horizon maintains $\partial_t \rho_n = 0$ globally via Eulerian continuity. Rate is $H_\infty = 28\pi m_e^3 c G / (\hbar^2 \alpha^2) \approx 69.32$ km/s/Mpc. Mechanism: latent-heat-of-crystallisation release per `cosmological-constant-closure.md:60-65`.

3. **Ax 1 substrate-physics**: ε ↔ macroscopic E translation via Cosserat translational DOF. The substrate's ε-sector preference (Component 1) propagates to macroscopic E observables via Ax 1. Per `axiom-definitions.md:12`.

4. **Ax 2 cross-scale**: The same Op14 kernel applies at every scale via TKI scale invariance. Substrate-scale physics at $u_0^*$ IS cosmic-scale physics at $R_H$ via universal kernel $S(A) = \sqrt{1 - A^2}$. Per `universal-saturation-kernel-catalog.md:7`.

5. **Op14 cosmic-horizon profile (Phase 1 leaf)**: $Z_{\text{eff}}(r \to R_H) \to \infty$ via canonical Op14 form; local-clock-freezing at horizon $\omega_{\text{local}}(R_H) \to 0$ is the substrate-physics anchor for the crystallisation-rate mechanism in step 2. Asymmetric Meissner form $Z_{\text{eff}} = Z_0 \sqrt{S_\mu/S_\varepsilon}$ when $S_\varepsilon \to 0$ before $S_\mu \to 0$ — ε-sector single-mode saturation drives the cosmic-horizon dynamics. Distinction from BH: dynamic ($\partial_t A^2 \neq 0$) per Q1.

6. **Macroscopic projection**: $\rho_\Lambda = 3 H_\infty^2 / (8\pi G)$ via Friedmann/de Sitter (standard GR). Projects onto $\mathcal{M}_{\text{cosmic}}$ in the canonical boundary-observables structure. Class E operating-point projection at $u_0^*$, joint-constrained with $\{G, H_\infty, \hat{\Omega}_{\text{freeze}}, \alpha\}$.

### Sanity check: what's NOT in the chain

Per the brief's CRITICAL FAILURE MODES — what we explicitly did NOT do:

1. **No magnitude-equality at step 1.** Over-bracing $u_0^*$ is a substrate-scale microscopic state; we do NOT claim $\rho_\Lambda$ comes from microscopic E-field energy summed over modes (the QFT $10^{122}$ trap).

2. **No RMS→DC at step 2.** Crystallisation rate is the substrate-native mechanism; we do NOT average over modes to get a static-substrate quantity.

3. **No microscopic/macroscopic conflation between step 1 and step 6.** Step 1 is substrate-scale microscopic; step 6 is macroscopic observable; they are joint-constrained at $u_0^*$ via Class E, NOT energy-equated.

4. **No new operator at step 5.** Op14 cosmic-horizon profile is (c)-operator-application of canonical Op14 (Vol 1 Ch 6 §1.13), per Q2 adjudication.

### Visual structural diagram

```
Component 1 (substrate state):  Over-bracing u_0* in Ω_freeze direction
                                ε-sector (Cosserat translational DOF)
                                [LATTICE GENESIS, FROZEN-IN]
                                              |
                                              | (Ax 1 ε ↔ E translation = Component 3)
                                              v
Component 2 (substrate dynamics): K4 crystallisation rate at horizon
                                  = H_∞ via LC crystallisation rate
                                  [ONGOING per Q1 dynamic adjudication]
                                              |
                                              | (Ax 2 TKI scale invariance = Component 4)
                                              v
Component 5 (substrate response): Op14 cosmic-horizon profile (Phase 1 leaf)
                                  Z_eff(r→R_H) → ∞, ω_local → 0
                                  Asymmetric Meissner: S_ε → 0 before S_μ → 0
                                  [SUBSTRATE-PHYSICS ANCHOR FOR RATE MECHANISM]
                                              |
                                              | (Friedmann/de Sitter standard GR)
                                              v
Component 6 (macroscopic projection): ρ_Λ = 3 H_∞² / (8πG)
                                       Projects onto M_cosmic
                                       Class E joint-constraint at u_0*
                                       [DE OBSERVABLE]
```

The chain is **structural**, not magnitude-equating. Each component sets the structural piece that the next depends on.

---

## §9 — Implications for the γ catalog classification (Q3 verdict)

Per Grant Q3 adjudication (`_orchestration/cosmic-epsilon-de-projection-scoping.md:13-16`): **γ (composite Class E + ASYM-N(ε))**. Both axes complementary:

- **Class E captures the joint-constraint structure** at operating-point $u_0^*$: DE is one of N joint observables of $\{G, H_\infty, \hat{\Omega}_{\text{freeze}}, \alpha\}$.
- **ASYM-N(ε) captures the saturation-mechanism class** at cosmic-scale ε: cosmic-ε saturation companion to Row 14 K4-crystallisation-SYM*.

The projection chain above demonstrates how the two framings are complementary:

- **Class E framing** is the WHAT: $\rho_\Lambda$ is the Friedmann projection of $H_\infty$, which is one observable of $u_0^*$. Class E captures Components 1-2-6 (substrate state → dynamics → macroscopic observable, joint-constrained at $u_0^*$).
- **ASYM-N(ε) framing** is the HOW: the ε-sector single-mode saturation at cosmic horizon (Component 5 asymmetric Meissner form) is the substrate-physics mechanism class within A-034's universal saturation kernel catalog. ASYM-N(ε) captures Components 3-4-5 (Ax 1 ε translation → Ax 2 scale invariance → Op14 cosmic-horizon profile).

The two framings answer different questions and are simultaneously true; they are different projection axes, not redundant. **The γ verdict is confirmed by the projection chain.**

### What this means for Phase 3 (A-034 catalog row addition)

The Phase 3 catalog row addition (next phase of this session) implements the ASYM-N(ε) part of the γ verdict at the catalog level:

```
| Cosmic (DE / ε-sector) | ASYM-N(ε) | substrate ε-strain at R_H / saturation threshold | Ongoing crystallisation maintaining ∂_t ρ_n = 0 | ρ_Λ measurement (supernova + CMB + BAO) |
```

This row is the companion to Row 14 (Cosmic Big Bang K4 crystallisation, SYM*); the companion-row links table at `universal-saturation-kernel-catalog.md:99-110` will be updated to show the explicit pairing. The closure-roadmap entry will be added to track this addition.

The Class E part of the γ verdict is **already in corpus** — `cosmological-constant-closure.md:97-99` carries Class E framing through Step 1 and 3 of the $\rho_\Lambda$ derivation; `omega-freeze-cosmic-grain-cascade.md` is the canonical Class E operating-point projection leaf. No new corpus piece is needed for the Class E side.

---

## §10 — Falsifiable consequences of the projection chain

The projection chain has consequences testable downstream (not adjudicated in this Session):

1. **CMB E/B polarization decoupling at $\hat{\Omega}_{\text{freeze}}$ axis** per `omega-freeze-cosmic-grain-cascade.md:54` Observable 5: if cosmic crystallisation is asymmetric ($K/G \neq 2$, ε-sector preferentially saturating), the substrate's local-clock-freezing at horizon should imprint asymmetric E vs B polarization at low-$\ell$ CMB scales. Direct test: Planck PR3 + LiteBIRD.

2. **G anisotropy via tensor extension** per `omega-freeze-cosmic-grain-cascade.md:77-100` Observable 7: $\Delta G/G \sim \alpha^N$ along $P_2(\cos\theta)$ axis with $\hat{\Omega}_{\text{freeze}}$ as symmetry axis. The Op14 cosmic-horizon profile's asymmetric Meissner form (Component 5) is the substrate-physics anchor for the anisotropy mechanism. Test: CODATA G dataset re-analysis along $\hat{\Omega}_{\text{freeze}}$ at $(l = 60.28°, b = 50.48°)$.

3. **CMB QNM matching of parent-BH** per `omega-freeze-cosmic-grain-cascade.md:102-116` Observable 8: CMB low-$\ell$ multipoles should preferentially populate $\ell$ values matching parent-BH QNM spectrum. The Op14 cosmic-horizon profile is the substrate-physics mechanism by which the imprint propagates from horizon to CMB observable.

4. **Phantom equation-of-state** $w_{\text{vac}} = -1 - \rho_{\text{latent}}/\rho_{\text{vac}} < -1$ per `phantom-energy-equation-of-state.md:12`: the ongoing $\partial_t A^2 \neq 0$ feature (Component 5 dynamic distinction from BH) drives the phantom equation-of-state. Test: DESI / Euclid $w(z)$ precision.

5. **Falsification of any joint-constraint observable** falsifies the operating-point $u_0^*$ and therefore the entire substrate model — per Class E discipline at `consistency-vs-emergence` v1.1 + `omega-freeze-cosmic-grain-cascade.md:7`. The projection chain is **falsifiable as a whole**, not as N independent components.

---

## §11 — Open derivation work

Per `cosmological-constant-closure.md:103-111` carried forward + Phase 1 Op14 cosmic-horizon profile leaf §8:

1. **Independent $\rho_{\text{latent}}$ derivation from substrate energetics** — open. Would close the magnitude side of Component 2.
2. **$\Gamma_{\text{cryst}}$ derivation from substrate** — open. Phase 1 Op14 cosmic-horizon profile provides the structural anchor (local-clock-freezing rate) but not the closed-form rate.
3. **Friedmann-route ↔ latent-heat-route consistency check** — open.
4. **Chain B' independent G derivation** (per `closure-roadmap.md:38` Tier 3) — open. Would promote the projection chain from Class E (joint constraint) to N independent emergence-class predictions.
5. **Substrate-physics anchor for asymmetric Meissner form at cosmic horizon** — partially addressed by Phase 1 Op14 cosmic-horizon profile §4; the question of whether ε-sector preferentially saturates at cosmic horizon (vs symmetric saturation) is a substrate-physics question that this chain does not close.

These open items are queued for future sessions or future epics; Session 2 produces the structural projection chain (this doc) + Phase 1 cosmic-horizon profile leaf + Phase 3 catalog row addition, NOT the closed-form magnitude derivation.

---

## §12 — (a)-(e) classification verdict

Per `ave-canonical-leaf-pull` v1.2 trigger 16 carried explicit:

**Verdict**: This Session's deliverable is a **composite (c)-operator-application + (a)-missing-row**:

- The Phase 1 Op14 cosmic-horizon profile leaf is **(c)-operator-application** — Op14 canonical at Vol 1 Ch 6 §1.13 applied at new scale ($r \to R_H$); not a new operator.
- The Phase 3 A-034 catalog row addition is **(a)-missing-row** — fills the explicit gap-cell at `universal-saturation-kernel-catalog.md:94` cosmic-ε column; not a new row class.
- The Phase 2 projection chain (this doc) is the structural assembly of canonical pieces (Components 1-6 all canonical) — no (b)/(d)/(e) elements; it is the framework's existing pieces in projection-order.

**None of (b) scale-invariance instance, (d) translator extension, or (e) genuinely-new framework piece are involved.** The deliverable lands cleanly in (a)+(c) class — Op14 application + missing catalog row.

---

## §13 — Anomalies surfaced

Per `flag-don't-fix` discipline: any contradiction or corpus-structural inconsistency must be surfaced, not silently resolved.

### Anomaly B1 (no new anomaly)

Session 2 produces NO new anomalies beyond those carried forward from Session 1:

- **Anomaly A1** (Session 1 §7.A1): MOND SYM vs ASYM-N(μ) catalog-row classification inconsistency at `universal-saturation-kernel-catalog.md:83` — still flagged; not in Session 2 scope to resolve.
- **Anomaly A2** (Session 1 §7.A2): dual Class-E framing in `cosmological-constant-closure.md` — still flagged; not in Session 2 scope.
- **Anomaly A3** (Session 1 §7.A3): "Op14 cosmic-horizon profile is a corpus gap" — **CLOSED by Phase 1 leaf** at commit `20bb659`. The gap is filled.

### No anomaly B2

No new anomalies were surfaced in projection-chain trace execution. The chain assembles canonical pieces in projection order; no new corpus-structural inconsistencies found.

---

## §14 — Cross-references

- **Brief**: [`_orchestration/cosmic-epsilon-de-projection-scoping.md`](../_orchestration/theoretical/cosmic-epsilon-de-projection-scoping.md) — Session 2 implementor brief
- **Session 1 predecessor**: [`research/2026-05-19_cosmic-epsilon-de-projection-scoping.md`](2026-05-19_cosmic-epsilon-de-projection-scoping.md) — scoping doc with Q1/Q2/Q3 plumber-physical questions
- **Phase 1 deliverable (this Session)**: [`op14-cosmic-horizon-profile.md`](../manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/op14-cosmic-horizon-profile.md) at commit `20bb659` — Op14 (c)-operator-application leaf at cosmic-horizon scale
- **Canonical chain anchors** (verified at session start):
  - [`omega-freeze-cosmic-grain-cascade.md:7,13-40`](../manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md) — Class E operating-point + over-bracing $u_0^*$
  - [`lattice-genesis-hubble-tension.md:6,8,29,31`](../manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/lattice-genesis-hubble-tension.md) — $H_\infty$ as LC crystallisation rate, Class E refinement
  - [`cosmological-constant-closure.md:33-44,60-65,97-99`](../manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/cosmological-constant-closure.md) — Friedmann/de Sitter projection, latent-heat mechanism, Class E
  - [`boundary-observables-m-q-j.md:13-15,21,31-40,77-79`](../manuscript/ave-kb/common/boundary-observables-m-q-j.md) — M/Q/J canonical structure at cosmic horizon
  - [`axiom-definitions.md:12,14-22`](../manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/axiom-definitions.md) — Ax 1 Cosserat translational DOF, Ax 2 TKI
  - [`operators.md:44`](../manuscript/ave-kb/common/operators.md) — Op14 canonical row Vol 1 Ch 6 §1.13 + asymmetric Meissner form
  - [`lattice-impedance-decomposition.md:44`](../manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/lattice-impedance-decomposition.md) — $Z_{\text{eff}} = Z_0/\sqrt{S}$ decomposition
  - [`universal-saturation-kernel-catalog.md:7,94`](../manuscript/ave-kb/common/universal-saturation-kernel-catalog.md) — universal kernel + cosmic-ε gap-cell
- **Class E canonization 2026-05-19**: [`research/2026-05-19_class-e-candidate-corpus-sweep.md`](2026-05-19_class-e-candidate-corpus-sweep.md)
- **A-031 cosmic-parameter horizon refinement**: [`cosmic-parameter-horizon-a031-refinement.md`](../manuscript/ave-kb/common/cosmic-parameter-horizon-a031-refinement.md)

## §15 — Closure statement

This is Session 2 of the β cosmic-ε / DE projection scoping epic. Deliverable: Phase 2 projection-chain trace research doc (this artifact) — walking through the 6-component inventory from Session 1 §2 in projection order from substrate dynamics ($u_0^*$ over-bracing at $\hat{\Omega}_{\text{freeze}}$ direction) to $\rho_\Lambda$ at the macroscopic Friedmann equation ($\rho_\Lambda = 3 H_\infty^2 / 8\pi G$).

**Structural chain confirmed**. The chain is:
1. Substrate state (Component 1, frozen $u_0^*$)
2. → ongoing dynamics (Component 2, crystallisation rate $H_\infty$)
3. → Ax 1 substrate-physics (Component 3, ε ↔ E translation)
4. → Ax 2 cross-scale (Component 4, TKI universal kernel at every scale)
5. → Op14 substrate response at cosmic horizon (Component 5, Phase 1 leaf at `20bb659`)
6. → Friedmann/de Sitter macroscopic projection (Component 6, $\rho_\Lambda$ on $\mathcal{M}_{\text{cosmic}}$)

**γ verdict (Class E + ASYM-N(ε)) confirmed by chain structure**: Class E captures Components 1-2-6 (joint-constraint at $u_0^*$); ASYM-N(ε) captures Components 3-4-5 (Ax 1 ε → Ax 2 scale invariance → Op14 ε-asymmetric Meissner at cosmic horizon).

**No magnitude-matching attempted; no RMS→DC averaging proposed; no microscopic/macroscopic conflation; no new operator invented.** All 4 CRITICAL FAILURE MODES from brief avoided.

**No new anomalies surfaced.** Session 1 anomaly A3 (Op14 cosmic-horizon profile corpus gap) CLOSED by Phase 1 leaf.

**No new load-bearing physics question surfaced beyond Q1/Q2/Q3 adjudications.** `pre-test-physics-check` discipline satisfied.

Phase 3 (A-034 catalog row addition) is next-up; closure-roadmap entry will be added to track the cosmic-ε row addition + companion-row pairing with Row 14.
