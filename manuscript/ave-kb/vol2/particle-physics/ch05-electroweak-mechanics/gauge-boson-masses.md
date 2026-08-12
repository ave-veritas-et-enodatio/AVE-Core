[↑ Ch.5 — Electroweak Mechanics](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-5zuo7g, clm-q8un7j]
-->

## Electrodynamics: The Gradient of Topological Phase

A localized charged node exerts a continuous rotational phase twist ($\theta$) on the surrounding LC network. Because the unsaturated vacuum acts as a linear dielectric in the far-field, the static structural phase strain obeys the 3D **Laplace Equation** ($\nabla^2 \theta = 0$).

The spherically symmetric geometric solution dictates that the twist amplitude decays inversely with distance ($\theta(r) \propto 1/r$). The continuous electric displacement field ($\mathbf{D}$) is the spatial gradient of this structural phase twist ($\mathbf{D} = \nabla\theta \propto -1/r^2 \mathbf{\hat{r}}$), deriving Coulomb's Law.

### Magnetism as Convective Vorticity

When a twisted node translates at a velocity $\mathbf{v}$, it induces a convective shear flow in the momentum field. In classical network dynamics, the time evolution of a translating steady-state strain field $\mathbf{D}(\mathbf{r} - \mathbf{v}t)$ is governed by the convective material derivative:

> **[Resultbox]** *Convective Material Derivative*
>
> $$
> \partial_t \mathbf{D} = -(\mathbf{v} \cdot \nabla)\mathbf{D} \implies \nabla \times (\mathbf{v} \times \mathbf{D})
> $$

Equating this to the Maxwell-Ampere law derives the macroscopic magnetic field from network dynamics: $\mathbf{H} = \mathbf{v} \times \mathbf{D}$.

This relationship is supported by dimensional analysis. Applying the topological conversion constant ($\xi_{topo} \equiv e/l_{node}$), the displacement field reduces to $[\mathbf{D}] = \xi_{topo}[1/\text{m}]$. Evaluating the cross product $[\mathbf{v} \times \mathbf{D}]$ yields $\xi_{topo}[1/\text{s}]$. Standard SI units for magnetic field intensity $\mathbf{H}$ ($[\text{A/m}]$) reduce to this same dimensional basis ($\xi_{topo}[1/\text{s}]$). Magnetism is thereby dimensionally shown to represent the continuous kinematic vorticity of the vacuum medium.

### The Inductive Origin of Gauge Invariance

Standard Quantum Field Theory mandates that the vector potential is a gauge field, where transformations of the form $\mathbf{A} \to \mathbf{A} + \nabla \Lambda$ leave physical observables ($\mathbf{B}$ and $\mathbf{E}$) unchanged. A common critique of identifying $\mathbf{A}$ as a physical momentum field is that this gauge freedom would imply the unphysical, spontaneous shifting of macroscopic mass, violating Noether's theorem.

This paradox is resolved via the **Helmholtz Decomposition Theorem** in classical network dynamics. Any continuous vector field can be decomposed into a solenoidal (divergence-free) component and an irrotational (curl-free) component. Adding the gradient of a scalar field ($\nabla \Lambda$) to the mass flow introduces a uniform, irrotational velocity potential to the background network.

The Helmholtz decomposition is exact at *any* compressibility, and that is all this argument needs: adding $\nabla\Lambda$ changes only the irrotational component, and **the irrotational component sources no transverse observable**. The curl identity $\nabla \times \nabla\Lambda \equiv 0$ leaves the transverse vorticity $\nabla \times \mathbf{A}$ pointwise unchanged, and the loop integral $\oint \nabla\Lambda \cdot d\boldsymbol{\ell} = 0$ around any closed contour (single-valued $\Lambda$) leaves every winding and linking integer unchanged — so no topological defect is created or destroyed. The remaining observable named in the critique, the electric field, is closed by the same channel argument rather than by a cancellation: $\delta\mathbf{E} = -\partial_t \nabla\Lambda$ is itself irrotational ($\nabla \times \partial_t\nabla\Lambda \equiv 0$), so it lands *wholly* in the EM longitudinal channel $\nabla\cdot\mathbf{A}$, and the curl-only EM Lagrangian gives that channel **no restoring force** ([`../../../common/vocabulary-register.md`](../../../common/vocabulary-register.md)`:870`, `def-l0ngdu`). **This closure holds for time-independent $\Lambda$ ONLY** (rescoped 2026-08-10 under R43; see the second-failure note below). For $\partial_t\Lambda = 0$ the electric leg closes identically and needs no channel argument at all: $\delta\mathbf{E} = -\partial_t\nabla\Lambda = 0$ pointwise, and $\mathbf{A} \to \mathbf{A} + \nabla\Lambda(\mathbf{x})$ is an *exact* symmetry of the written action. For time-*dependent* $\Lambda$ the argument does **not** close, because the step it would need is false: the curl-only Lagrangian does give the longitudinal channel no restoring force, but it does *not* follow that the channel stores no energy — the kinetic term $\tfrac12\varepsilon_0|\partial_t\mathbf{A}_L|^2$ stores energy in precisely that channel, and correspondingly the written action is *not* invariant under time-dependent $\Lambda$, shifting by $\varepsilon_0(\partial_t\mathbf{A})\cdot\nabla(\partial_t\Lambda) + \tfrac12\varepsilon_0|\nabla(\partial_t\Lambda)|^2$. What this leaf therefore derives is the **residual, time-independent** gauge family — the classical network-dynamic freedom to shift the irrotational background coordinate velocity without altering the physical observables, transverse or longitudinal, isomorphic to performing a **Galilean or Lorentz coordinate boost** of the observer's reference frame — and *not* the full time-dependent U(1) group. Full U(1) is recovered only on the Gauss-constrained initial-data surface in the covariant completion, where the missing constraint is supplied by Axiom 5 (Substrate DC Bias, [`eq_axiom_5.tex`](../../../../common_equations/eq_axiom_5.tex); *which* clause supplies it is left open, riding the deferred FORK-1).

> **Premise repaired — the incompressibility premise is struck (Grant ruling 2026-08-03).** Ruling verbatim `[sic]`: ***"5. repair"***. The step above deliberately does **not** assume an incompressible substrate.
>
> **Why the old premise was false.** It read *"Because the vacuum substrate is incompressible ($K = 2G$) …"*. The vacuum at $K = 2G$ is **definitively compressible**: the isotropic relation $\nu = (3K - 2G)/(2(3K+G))$ gives $\nu_{\text{Hill}} = 4G/14G = \mathbf{2/7}$ at $K = 2G$, and $\nu = 1/2$ is reached **only** in the limit $K \to \infty$ — **no finite $K$ is incompressible**. `K = 2G` is the corpus's *finite-modulus* trace-reversal lock, not a rigidity statement (`common/q-g47-substrate-scale-cosserat-closure.md:28`; GR-imported per PR [#261](https://github.com/ave-veritas-et-enodatio/AVE-Core/pull/261)). 🔴 **[DEMOTED 2026-08-11 — R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]**
>
> **Why it was load-bearing, not decorative.** For a general $\Lambda$, $\nabla\cdot(\nabla\Lambda) = \nabla^2\Lambda \neq 0$, so the clause *"generates no localised compression"* does **not** follow from Helmholtz alone — incompressibility was exactly what was being asked to kill it. The repair therefore **drops that leg rather than rescuing it**, and keeps only what the gauge conclusion actually needs.
>
> **The correct available premise (the ruled replacement).** The irrotational component sources **no transverse observable**: $\nabla \times \nabla\Lambda \equiv 0$ and $\oint \nabla\Lambda \cdot d\boldsymbol{\ell} = 0$ hold at **any** $\nu$, including $\nu_{\text{vac}} = 2/7$. The substrate-native grounding is the corpus's **adjudicated longitudinal-sector split**, [`../../../common/vocabulary-register.md`](../../../common/vocabulary-register.md)`:867` (`def-l0ngdu`; the quoted clauses below are at `:870`): the mechanical dilatation $\nabla\cdot\mathbf{u}$ is **DYNAMICAL** — it carries a genuine bulk restoring force $\tfrac12 K(\nabla\cdot\mathbf{u})^2$ and rides the gapless lattice-computed P-branch — while the EM longitudinal $\nabla\cdot\mathbf{A}$ is **GAUGE**, the curl-only EM Lagrangian giving it no restoring force. Verbatim: *"**One word each way — $\nabla\cdot\mathbf{u}$ propagates; $\nabla\cdot\mathbf{A}$ is gauge.**"* That split is the substrate-native reason the shift is unobservable, and it needs no compressibility assumption. 🔴 **[DEMOTED 2026-08-11 — R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]**
>
> **★ The split is LOAD-BEARING, not decoration — it is what closes the $\mathbf{E}$ leg (correction 2026-08-03, review finding 3).** The clause this repair struck was the section's **only** coverage of the electric field, and it was **garbled**: it called $-\partial_t\mathbf{A}$ *"localised compression"* when $-\partial_t\mathbf{A}$ **is** the electric field. Striking it therefore removed the $\mathbf{E}$ leg outright, and $\delta\mathbf{E} = -\partial_t\nabla\Lambda \neq 0$ **pointwise** — so the first form of the repair covered $\mathbf{B}$ and the topological integers but left $\mathbf{E}$ open. The textbook cancellation is **not available in this section's variables**: there is no scalar-potential companion here to absorb $\varphi \to \varphi - \partial_t\Lambda$. The closure is substrate-native instead, and it is exactly `def-l0ngdu`'s no-restoring-force clause promoted from grounding-decoration to a **step of the chain**: $\delta\mathbf{E}$ is irrotational ($\nabla\times\partial_t\nabla\Lambda \equiv 0$), hence lands *wholly* in the EM longitudinal channel; **a channel with no restoring force stores no energy and exerts no force**, so it supports no observable of any kind. The step is added to the body paragraph above and to the chain check below as **(3′)**.
>
> **Chain check (the repaired argument, end to end).** (1) Critique: a gauge shift on a *physical* $\mathbf{A}$ would spontaneously move macroscopic mass. (2) Helmholtz: $\nabla\Lambda$ is purely irrotational, so it enters only the longitudinal channel — exact at any $\nu$, no premise spent. (3) The physical transverse observables are built from the solenoidal channel ($\mathbf{B} = \nabla\times\mathbf{A}$), and $\nabla\times\nabla\Lambda \equiv 0$, so they are pointwise unchanged. **(3′) The electric field is *not* pointwise unchanged** — $\delta\mathbf{E} = -\partial_t\nabla\Lambda \neq 0$ — but it is **irrotational**, so the whole of $\delta\mathbf{E}$ sits in the EM longitudinal channel, which by `def-l0ngdu` has **no restoring force**; a channel with no restoring force stores no energy and exerts no force, so it carries no observable. (4) The topological content is loop/surface integrals of the solenoidal channel, and $\oint\nabla\Lambda\cdot d\boldsymbol{\ell} = 0$, so no defect is created or destroyed. (5) Therefore the shift is a coordinate re-labelling of the irrotational background — the boost reading — and the critique is answered. **No step uses compressibility**, and with (3′) in place **every** observable named in the critique ($\mathbf{B}$ *and* $\mathbf{E}$) is covered. *(Prior form of this note, preserved per Rule 12: it read "The chain reads soundly" with steps (1)–(5) and no (3′) — i.e. it asserted soundness while covering $\mathbf{B}$ only. That assertion was wrong as written and is corrected here, not deleted.)*
>
> **⚑ FLAGGED, NOT FIXED — and it is PREMISE-CRITICAL, not a wording nit (severity corrected 2026-08-03, review finding 4).** The paragraph above still describes $\nabla\Lambda$ as added *"to the mass flow"*, which reads $\mathbf{A}$ as the mechanical momentum field. The corpus's SOLID adjudication is that $\mathbf{u}$ and $\mathbf{A}$ are **counterpart sector variables — isomorphic structure, NOT one field** ([`../../../common/vocabulary-register.md`](../../../common/vocabulary-register.md)`:882`, `def-uatk1s`, SOLID 2026-07-21), differing **precisely** in constitutive stencil on the longitudinal channel. **Why the severity is higher than "wording":** the repair above rests on the added field being *EM*-longitudinal, where there is no restoring force. If $\nabla\Lambda$ is genuinely added to the **mass flow** $\mathbf{u}$, then by that same `def-l0ngdu` the channel it enters is the **mechanical** dilatation $\nabla\cdot\mathbf{u}$ — which **is** dynamical, carries $\tfrac12 K(\nabla\cdot\mathbf{u})^2$, and rides the propagating P-branch. On that reading the addition is **observable**, and the repaired premise is **refuted**, not merely mis-worded. The resolution therefore requires the $\mathbf{A}$-vs-$\mathbf{u}$ identification to be settled for this paragraph (`def-uatk1s`: counterpart sector variables, **NOT one field**), not a synonym swap. **Routed, still not taken here** — surfaced rather than absorbed silently into this repair. *(Prior severity label, preserved per Rule 12: "Whether the 'mass flow' wording needs its own correction is a separate question, routed.")* 🔴 **[DEMOTED 2026-08-11 — R40-B1; dated demotion note at the end of this file]**
>
> **Scope.** Premise-only. The conclusion, the boost reading, and every downstream result in this leaf ($m_W/m_Z = \sqrt{7}/3$, $\sin^2\theta_W = 2/9$) are **unchanged**; `clm-5zuo7g` and `clm-q8un7j` are untouched (no re-grade, no retraction). Mirrored byte-for-byte in the print at `manuscript/vol_2_subatomic/chapters/05_electroweak_gauge_theory.tex` §"The Inductive Origin of Gauge Invariance" (the `.tex` carries a condensed premise note; this leaf carries the explanation).

## The Weak Interaction: Inductive Cutoff Dynamics
<!-- claim-quality: clm-5zuo7g (the $m_W/m_Z = \sqrt{7}/3$ ratio derived in this section gives the on-shell Weinberg angle) -->

In classical electrodynamics, the ratio of the LC network's microrotational bending inductance ($\gamma_c$) to the macroscopic optical shear modulus ($G_{vac}$) defines a fundamental **Characteristic Length Scale** ($l_c = \sqrt{\gamma_c/G_{vac}}$). This length scale is identified as the physical origin of the weak force range ($r_W \approx 10^{-18}$ m).

Weak interactions lack the kinetic energy required to overcome the ambient LC rotational inductance. Any physical excitation operating *below* a medium's natural cutoff frequency becomes an **Evanescent Wave**. The static field equation transforms from the Laplace equation to the massive Helmholtz equation ($\nabla^2 \theta - \frac{1}{l_c^2}\theta = 0$). The solution yields the **Yukawa Potential**:

> **[Resultbox]** *Yukawa Potential as Evanescent Cutoff*
>
> $$
> V_{weak}(r) \propto \frac{e^{-r/l_c}}{r}
> $$

### Deriving the Gauge Bosons ($W^{\pm}/Z^{0}$) as Evanescent Modes
<!-- claim-quality: clm-q8un7j -->

The gauge bosons of the weak interaction represent the fundamental macroscopic evanescent cutoff excitations required to mechanically induce a localized phase twist.

- The charged $W^{\pm}$ bosons correspond to the pure longitudinal-torsional evanescent mode ($k\propto G_{vac}J$).
- The neutral $Z^{0}$ boson corresponds to the transverse-bending evanescent mode ($k\propto E_{vac}I$).

Because Axiom 1 bounds the physical diameter of a fundamental flux tube to $d \equiv 1 l_{node}$ (the hard-sphere exclusion limit), these topological connections act as volume-bearing physical 3D continuous cylinders at the macroscopic limit. Furthermore, because the tube is formed by a radially symmetric dielectric displacement field, the Perpendicular Axis Theorem dictates that its polar moment of inertia evaluates to $J=2I$. This is a geometric property for any circular cross-section, not an assumed relationship.

Because the rest mass of an evanescent cutoff mode scales with the square root of its ratio of structural stiffness to inertia ($\omega \propto \sqrt{k/m}$), the mass ratio evaluates to $m_W/m_Z = \sqrt{GJ / EI}$. Because the substrate metric is a discrete lumped-element LC network, the localised nodal inertia ($\mu_0$) is invariant across both the torsional and bending excitation modes. Because the mass term is constant, the geometric wave equations reduce to the square root of the stiffness ratio, avoiding the geometrically distinct inertial denominators required in classical continuum solid mechanics. Substituting the fundamental cylinder geometry ($J=2I$) yields $\sqrt{2G/E}$. Applying the standard isotropic elastic continuous identity ($E = 2G(1+\nu)$) reduces this stiffness ratio.

---

## ★ SECOND FAILURE AT THIS STEP (dated note, 2026-08-10, R43 item (c) — repair prose LANE-AUTHORED)

> **Placement note.** This note is appended at EOF rather than inside the repair blockquote above on purpose: inserting it there shifted this leaf's own `:52` (*"## The Weak Interaction: Inductive Cutoff Dynamics"*) and `:55`/`:57`/`:62`, which are live inbound cites. [`wall-taxonomy.md`](../../../common/wall-taxonomy.md):336 is the quote-drift row *"ALTERED -- emphasis re-scoped: source italicises 'below', leaf bolds it (declared in-row)"* (with `:337`/`:338` the Q21/Q22 rows), and [`translation-circuit.md`](../../../common/translation-tables/translation-circuit.md):214 is the row *"WKB tunneling / barrier penetration"*. Shifting a **quote-drift audit table** is the worst possible thing to shift, so cite stability wins and the note lives here; the repaired paragraph at `:34` points down to it.

**Authorship fence (matching the style of the Axiom-3 repair's transliteration note).** Unlike R43 items (a) and (b), item (c) had **no ratified repair text**: the source lane only FLAGGED this clause (Tier-2 finding C22 + consequence-audit flag (a)) and drafted no replacement, stating *"Zero corpus edits made; flag-don't-fix throughout."* **The repair prose and this note are therefore LANE-AUTHORED against that finding, not ratified text landed verbatim** — flagged in-artifact here, not only in the commit trail. *This is the second time the electric leg of this argument has failed, and it is recorded plainly rather than folded into the repair.* **First failure (2026-08-03):** the step rested on *"the vacuum substrate is incompressible ($K = 2G$)"* — false at any finite $K$. It was struck, and the `def-l0ngdu` no-restoring-force clause was promoted from grounding-decoration to a load-bearing step of the chain (step 3′) to close $\mathbf{E}$ in its place. **Second failure (2026-08-10):** that replacement clause is *itself* false. *"A channel with no restoring force stores no energy"* does not hold for time-dependent $\Lambda$: no restoring force means no **potential** term, but the **kinetic** term $\tfrac12\varepsilon_0|\partial_t\mathbf{A}_L|^2$ stores energy in exactly that channel. Both repairs targeted the same load-bearing joint — the $\mathbf{E}$ leg — and both substituted a claim that had not been machine-checked before it was made load-bearing. The step is therefore **rescoped rather than re-patched a third time**: only the residual time-independent family is derived here, and canon holds **no valid derivation of any full U(1) family** — the residual time-independent family is the only exact symmetry statement available, and supplying the first correct one is what the Axiom-3 repair does ([`eq_axiom_3.tex`](../../../../common_equations/eq_axiom_3.tex)). **Scope of THIS note:** the U(1) leg only. Every downstream result in this leaf ($m_W/m_Z = \sqrt{7}/3$, $\sin^2\theta_W = 2/9$) is **unchanged**; `clm-5zuo7g` and `clm-q8un7j` are untouched (no re-grade, no retraction). Basis: the bound-constitutive lane's Tier-2 finding C22 + consequence-audit flag (a), [`2026-08-10_bound-constitutive_result.md`](../../../../../research/2026-08-10_bound-constitutive_result.md); ruling [`2026-08-10-ruling-r43-ratification.md`](../../../../../_orchestration/docket-entries/2026-08-10-ruling-r43-ratification.md), whose companion S+G record names *"the twice-failed ch05 paragraph"*.

---

### 🔴 Dated demotion note — 2026-08-11 (R40 demotion sweep, batch 1)

**Class: DIES-WITH-THE-PHANTOM.** Status change only — the claim text is **preserved
verbatim** (honesty-lag pattern, Rule 12) and stamped in place; it is **no longer live
canon**. Nothing is deleted.

**Demoted in this file:**

- **`:48`** — *"the channel it enters is the **mechanical** dilatation $\nabla\cdot\mathbf{u}$ — which **is** dynamical, carries $\tfrac12 K(\nabla\cdot\mathbf{u})^2$, and rides the propagating P-branch"*
  Stamped in place at `:48`.
  **Why it dies (audited row rationale, verbatim):** The routed premise-critical refutation-threat (nabla-Lambda added to mass flow u would be OBSERVABLE) REQUIRES the propagating P-branch; under the carve div(u) is also constrained, the threat is void, and its voiding dissolves the flagged A-vs-u jeopardy.

**The arc, complete — the framing R40 rules every demotion note carries:**

1. **The kill fired** (#930) — the walk-back that closed the bulk radiative-port reading.
2. **The premise localized to the #261 K = 2G import** (G-RECON, unchallenged): the compressible
   far-field branch was minted by a GR-imported elastic modulus, not forced by the axioms.
3. **The axioms underdetermine the bulk sector** — the #935 flat-direction finding: the written
   action conserves the Gauss function pointwise and never fixes its value.
4. **The replacement is the RATIFIED bound-sector law — Axiom 5, Substrate DC Bias**
   (BC-SRC clauses **S** / **G** / **Q**), ratified per `_orchestration/docket-entries/2026-08-10-ruling-r43-ratification.md`, as reconciled by `_orchestration/docket-entries/2026-08-10-ruling-r44-r43-reconciliation.md` (R44 — the
   full-scope R43 record is FINAL and authoritative; the partial
   `_orchestration/docket-entries/2026-08-10-ruling-r43-sg-ratified.md` is SUPERSEDED and is **not**
   the resolution). Under the ratified law the A1 / bulk slot is a **bound response** — mechanism
   gloss **back-reaction** — with no independent propagating branch, no port, and zero longitudinal
   characteristic speed. A bulk *wave speed*, a bulk *radiative port*, a bulk *band-branch* and a
   bulk *transit clock* therefore have **no referent**.

**Standing named-open debt (the honest rider).** The ratified axiom does **not** discharge
everything: **THE BIAS PROPAGATION THEOREM** is Axiom 5's standing named-open entry — clause G's
elliptic law is the *static abstraction* of underived finite-speed bias dynamics (`_orchestration/2026-08-10_bias-propagation-brief.md`). Where a
demoted claim's replacement depends on finite-speed bias dynamics, the resolution is the ratified
axiom **with that debt open**, not a closed replacement.

**Records.** R40 ruling `_orchestration/docket-entries/2026-08-10-rulings-r40-r42.md` · verified worklist `research/drivers/r40_sweep_worklist_verified.json` · scope verification `_orchestration/2026-08-10_r40-sweep-scope-verification.md` ·
batch-1 record `_orchestration/2026-08-11_r40-sweep-batch1.md` · vocabulary R50 `_orchestration/docket-entries/2026-08-10-ruling-r50-vocab.md` (canonical: the displacement pattern u₀ around a
deposit is **the bound response**, mechanism gloss **back-reaction**; ε₁₁ is **the bias**;
"dress", "grade"-as-canonical-noun and "halo"-for-the-physics are retired; and the owed theorem is
renamed **THE BIAS PROPAGATION THEOREM**) · vocabulary **R49(b)** `_orchestration/docket-entries/2026-08-10-rulings-r48-r49.md` (*"retardation"
is RETIRED from this role. The canonical term is **propagation delay / finite propagation speed*** —
the retardation retirement is R49(b)'s, NOT R50's; corrected 2026-08-11 at review).

---

## R40 batch-2a — NEEDS-RE-DERIVATION status note (2026-08-11)

**Class:** status demotion under **R40**. This note mints no `clm-`/`def-`/`exp-`/`sup-`/`ilk-`,
**moves no solidity number**, adjudicates no channel and opens no fork. Every byte of each demoted
claim is preserved; the stamped line gains a status marker only (honesty-lag pattern, Rule 12).

**The arc, in four clauses (R40's header form; clause 4 points at the LANDED artifact, not at a
ruling record).**

1. **The kill fired** — the walk-back that closed the bulk radiative-port reading.
2. **The premise localized to the imported `K = 2G` elastic modulus** — the compressible far-field
   branch was minted by a GR-imported modulus, not forced by the axioms.
3. **The axioms underdetermine the bulk sector** — the flat-direction finding: the written action
   conserves the Gauss function pointwise and never fixes its value.
4. **The replacement is the LANDED ratified bound-sector law — Axiom 5, Substrate DC Bias**, clauses
   **S** (deposit), **G** (bias coupling / bridge) and **Q** (quiescence), canonical at
   [`eq_axiom_5.tex`](../../../../common_equations/eq_axiom_5.tex) with its register entry in
   [`axiom-register.md`](../../../common/axiom-register.md) (§ *Axiom 5 — Substrate DC Bias*). Under
   clause **G** the A1 / bulk slot is a **bound response** — $\mathbf{u}_0 =
   -\mathcal{A}_g\nabla\varepsilon_{11}$, mechanism gloss **back-reaction** — with **no independent
   propagating branch, no port and zero longitudinal characteristic speed**. A bulk *wave speed*, a
   bulk *radiative port*, a bulk *band-branch* and a bulk *transit clock* therefore have **no
   referent**, and each row below owes its re-derivation on that footing.
   $\mathcal{A}_g$ (the **bias-coupling area**) is an `UNVALUED-RATIFIED-CONSTANT` per **R48**
   ([`interlock-register.md`](../../../common/interlock-register.md), § *𝒜_g — the bias-coupling
   area*): it is **not valued here or anywhere**, and **the calibration count stays 3**.

**Standing named-open debt — the honesty rider.** The ratified axiom does **not** discharge
everything. **THE BIAS PROPAGATION THEOREM is Axiom 5's standing named-open debt**, stated by the
axiom's own phase-structure paragraph, clause **(c1)**: clause G's elliptic law is the *static
abstraction of underived finite-speed bias dynamics*, and the $(u,\pi)$ no-signalling theorem does
**not** cover the bias read — the bias's finite propagation speed is *owed, not held*. Every row
tagged **⚑ BIAS-DEBT** below re-derives against the ratified axiom **with that debt standing**, never
against a closed replacement.

**Vocabulary.** Canonical nouns authored here: **the bound response** ($\mathbf{u}_0$), **the bias**
($\varepsilon_{11}$), the **DC operating point / quiescent point (Q-point)**; **back-reaction** is
the mechanism gloss. *"dress"*, *"grade"* as $\varepsilon_{11}$'s canonical noun, and *"halo"* for
the physics (the physics noun is the **near-field store / added-mass**) are RETIRED by **R50**;
*"retardation"* is retired by **R49(b)** in favour of **propagation delay / finite propagation
speed**. Corpus text quoted below is byte-exact and is never reworded.

**Rows carried in this file.**

- **`:38`** — stamped at `:38`. *(family: K-static vs constitutive-fact; banked `uncertain`)*
  Quoted claim, byte-exact at HEAD:
  ```text
  The vacuum at $K = 2G$ is **definitively compressible** … **no finite $K$ is incompressible**
  ```
  Audited rationale, verbatim from the banked worklist:
  ```text
  The nu=2/7 arithmetic is static (static-import class, survives); but the Grant-ruled sentence asserts a live compression sector as a constitutive fact — exactly the reading the carve replaces (constraint class, not a finite-K statement). Uncertain: the static-import carve-out could route this NOT-A-CONSUMER; included per err-toward-inclusion.
  ```

  **Resolution.** The demoted carrier is the propagating A1 / bulk branch; under Axiom 5 clause G that slot is the **bound response**, so the re-derivation must be re-posed on the bound-sector constitutive law (bias $\varepsilon_{11}$, bound response $\mathbf{u}_0$, mechanism gloss back-reaction) rather than on a compression wave.

- **`:42`** — stamped at `:42`. *(family: def-l0ngdu propagating-divu)*  ⚑ **BIAS-DEBT**
  Quoted claim, byte-exact at HEAD:
  ```text
  the mechanical dilatation $\nabla\cdot\mathbf{u}$ is **DYNAMICAL** — it carries a genuine bulk restoring force $\tfrac12 K(\nabla\cdot\mathbf{u})^2$ and rides the gapless lattice-computed P-branch
  ```
  Audited rationale, verbatim from the banked worklist:
  ```text
  The 2026-08-03 gauge-invariance repair grounds itself on the def-l0ngdu split whose divu-propagates half is the phantom; the repair's CONCLUSION (unobservability of the Lambda-shift) survives and strengthens under the carve, but its stated grounding and the 'one word each way' contrast consume the P-branch.
  ```

  **Resolution.** The demoted carrier is the propagating A1 / bulk branch; under Axiom 5 clause G that slot is the **bound response**, so the re-derivation must be re-posed on the bound-sector constitutive law (bias $\varepsilon_{11}$, bound response $\mathbf{u}_0$, mechanism gloss back-reaction) rather than on a compression wave. **⚑ BIAS-DEBT:** this row's re-derivation turns on finite-speed bias dynamics, so the resolution is the ratified axiom **with THE BIAS PROPAGATION THEOREM standing** (clause (c1)) — the replacement is *owed, not held*.

**Records.** Ruling **R40** (the demotion sweep) · the banked worklist
[`r40_sweep_worklist_verified.json`](../../../../../research/drivers/r40_sweep_worklist_verified.json) · batch-0
scope verification and batch-1 execution records in `_orchestration/` · this batch's record
`_orchestration/2026-08-12_r40-sweep-batch2a.md`.

