[↑ Ch.2 General Relativity](index.md)
<!-- claim-quality: clm-zbvfpi, clm-w5ez6i -->

<!-- kb-frontmatter
kind: leaf
claims: [clm-zbvfpi, clm-w5ez6i]
-->

# Saturating-Modulus Correction + Two-Way Gravitational Back-Reaction (engine capability)

> **Class + scope (load-bearing honesty).** This leaf distils two *engine-capability / consistency-class*
> increments on the inherited linear GR core (the elastic-Poisson / Schwarzschild solver of
> [`einstein-field-equation.md`](einstein-field-equation.md)), **not** new value-level chords:
> - **Stage-1** (clm-zbvfpi) — a saturating modulus $D(A)=1/S(A)$ on the elliptic operator; recovers the
>   linear core in the weak field (consistency) and produces a strain-saturated shell at the extreme
>   (manifestation). It is the *numerical elliptic-relaxation confirmation* of the analytic Topological
>   Halting already canonical at
>   [`interior-singularity-resolution.md`](../../cosmology/ch15-black-hole-orbitals/interior-singularity-resolution.md)
>   (clm-ir8h78) — plus a load-bearing clip-independence gate.
> - **Stage-3** (clm-w5ez6i) — the **TWO-WAY** back-reaction: the gravitational field sources ITSELF, and the
>   effective mass **emerges** from the converged field's own integrated energy. This is the ARCHITECTURAL win
>   (item #86, the make-or-break the engine-architecture frontier flagged ABSENT); it is the REVERSIBLE half
>   only (the irreversible depletion / DE-tracks-matter chord is a separate, unbuilt Stage-4 primitive).
>
> **Neither stage derives gravity or replaces GR.** Recover-GR is consistency-class; the value-map
> $r_s = 2GM_{\text{eff}}/c^2$ still imports $G$ (the modulus $c^4/7G$ is $G$-imported, $K{=}2G$ is GR-imported
> per PR#261). Both stages are **α-CLEAN** (gravity sector; source-level guard-tested). The FORM is
> substrate-forced (the 1/r monopole, the GR doubling, the emergent-from-field-energy architecture); the
> VALUE-scale is imported — consistent with the standing FORM-deriving / VALUE-importing meta-finding.
>
> Engine-canonical source: [`src/ave/gravity/gw_propagation.py`](../../../../../src/ave/gravity/gw_propagation.py)
> (Stage-1) and [`src/ave/gravity/backreaction.py`](../../../../../src/ave/gravity/backreaction.py) (Stage-3).
> Result docs: `research/2026-06-29_grqed-stage1-gr-extension_result.md`,
> `research/2026-06-29_grqed-stage3-backreaction_result.md`.

---

## §1 — Stage-1: the saturating-modulus correction
<!-- claim-quality: clm-zbvfpi -->

The inherited linear core is the **weak-field limit**:
$-(c^4/7G)\nabla^2\varepsilon_{11}=4\pi Mc^{2}\delta^{3}(r)\Rightarrow\varepsilon_{11}=7GM/c^2r$, $n=1+(2/7)\varepsilon_{11}$  *(source convention corrected TYPO-CLASS 2026-08-10, R49(a): the declared $4\pi$ convention per `gordon-optical-metric.md`:25, verbatim there — `-\left(\frac{c^{4}}{7G}\right)\nabla^{2}\epsilon_{11}(r) = 4\pi Mc^{2}\delta^{3}(r)` — / clm-rd9cjm; it previously read a bare $=T_{00}$.)*
(canonical at [`einstein-field-equation.md`](einstein-field-equation.md) and
[`gordon-optical-metric.md`](../ch03-macroscopic-relativity/gordon-optical-metric.md):25, clm-rd9cjm). *(Cite repaired 2026-08-10, R49(a): this line previously named `gravitational-refractive-index-gradient.md`, which carries neither formula; the convention-declaring leaf is the gordon one — verbatim there: `-\left(\frac{c^{4}}{7G}\right)\nabla^{2}\epsilon_{11}(r) = 4\pi Mc^{2}\delta^{3}(r)`.)*
Stage-1 multiplies the elliptic operator by a **saturating modulus**:

> **[Resultbox]** *Saturating-modulus elliptic operator*
>
> $$
> -\nabla\!\cdot\!\big[(c^4/7G)\,D(A)\,\nabla\varepsilon_{11}\big]=4\pi T_{00},
> \qquad A=\varepsilon_{11}/\varepsilon_{\text{yield}}\ (\varepsilon_{\text{yield}}=1),
> \qquad D(A)=\frac{1}{S(A)},\qquad S(A)=(1-A^2)^{1/2}.
> $$

The kernel $S(A)=(1-A^2)^{1/2}$ is the **one** canonical Op14 saturation kernel (Axiom 4), **reused** from
`graded_vacuum_network`, not minted. The per-channel **sign-lock** (INVARIANT-S2) keeps the three channels
physically distinct:

- **BULK stiffens:** $D=1/S\to\infty$ at $A\to1$ (the modulus goes rigid, halting the collapse). 🔴 **[DEMOTED 2026-08-11 — R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]**
- **SHEAR softens:** $c_{\text{shear}}=c_0\sqrt{S}=c_0(1-A^2)^{1/4}\to0$ — a **derived** $\sqrt{S}$ projection,
  NOT a second kernel.
- **EM matched:** $Z_{EM}=Z_0$, $\Gamma_{EM}=0$ — `refractive_index()` is untouched (guard-tested spectator).

In the weak field ($r\gg r_{\text{sat}}$: $A\to0$, $S\to1$, $D\to1$) the correction **vanishes** and the linear
GR core is reproduced identically (**consistency**). At the strong-field extreme the radial strain reaches the
yield $A=1$ at the saturation radius

$$r_{\text{sat}}=3.5\,r_s=7GM/c^2=(2/\nu_{\text{vac}})\,r_s,$$

the bulk modulus diverges, and a **strain-saturated shell** forms (**manifestation**). This is the
elliptic-relaxation numerical realisation of the **Topological Halting** already analytic at
[`interior-singularity-resolution.md`](../../cosmology/ch15-black-hole-orbitals/interior-singularity-resolution.md)
(clm-ir8h78): $\rho_{\text{eff}}=\rho_0/S_{\text{topo}}^3$ with $S_{\text{topo}}=\sqrt{1-\varepsilon_{11}^2}\to0$.

> **Honesty — RELOCATION, not removal.** The point singularity is **replaced by a shell** at $r_{\text{sat}}$;
> the inertial density **still diverges** there. True removal needs the yield→rupture→genesis physics (a
> separate frontier). The strain cap implemented ($\min(\varepsilon_{11},1)$) is a **numerical clip, NOT
> modeled yield-physics**. Stage-1 does **not** claim "regularizes the singularity."

## §2 — Stage-1 gate table (two-test doctrine + clip-independence)

| Gate | Class | Result | Verdict |
|---|---|---|---|
| Test 1 — recover-the-known ($r\gg r_{\text{sat}}$: $D\to1$, linear profile) | consistency | relaxed-field exterior tail $A=0.18$ at $r=N{-}3$ (unsaturated $A<0.4$ regime exists); $D\to1$ recovery | **PASS** |
| Test 2 — activate-at-the-extreme (yield shell at $r_{\text{sat}}$) | manifestation | $\max A=1.000000$; shell radius $=4.0$ sites (interior); $D(0.99)=7.089$ rising; $D\cdot S=1$ (reciprocal sign-lock, rtol $10^{-9}$) | **PASS** |
| ★ LOAD-BEARING — clip-independence gate | — | shell radius + $M_{\text{eff}}$ **bit-identical** across $S_{\min}\in\{10^{-4},10^{-3},10^{-2}\}$ (relative spread $0.00$) | **PASS** |

The ★ clip-independence gate is the load-bearing discriminator: the yield-shell radius and integrated source
$M_{\text{eff}}$ are set by the **yield-physics** ($r_{\text{sat}}$ geometry, where $A\to1$), **not** the
numerical clamp $S_{\min}$. Had the shell radius tracked $S_{\min}$, the clamp would have set the wall and the
gate would have FAILED — it does not. (A wider 6-decade sweep holds shell $=4.0=\sqrt{16}$ for
$S_{\min}\le10^{-2}$; only at the loose floor $S_{\min}=10^{-1}$ does it shift to the adjacent lattice ring
$\sqrt{17}$ — a $\pm1$-ring discretization granularity, within the 5% tolerance, NOT $S_{\min}$-dependence.)

> **Honest note (definitional vs load-bearing).** The far-field closed-form strain-match
> $\varepsilon_{11}^{\text{sat}}/(r_{\text{sat}}/r)=1$ is *definitional* ($\min(r_{\text{sat}}/r,1)\equiv
> r_{\text{sat}}/r$ for $r>r_{\text{sat}}$), not an independent recovery. The non-tautological consistency
> evidence is the relaxed-field exterior tail plus the $D\to1$ stiffness recovery. **α-CLEAN** (source-level
> guard test asserts no `ALPHA`/`Q_TANK`).

## §3 — Stage-3: the two-way self-gravitation loop
<!-- claim-quality: clm-w5ez6i -->

Stage-1 solved the ONE-WAY forward problem $T_{00}^{\text{matter}}\to\varepsilon_{11}$. **Stage-3 closes the
loop:** the gravitational field sources ITSELF. The field's own strain energy is added to the matter source and
the Stage-1 elliptic problem is re-solved to a self-consistent fixed point:

> **[Resultbox]** *Two-way fixed point + emergent mass (binding-DEFICIT ledger)*
>
> $$
> T_{00}^{\text{total}} = T_{00}^{\text{matter}} + \tfrac12 g\,|\nabla\varepsilon_{11}|^2,
> \qquad
> M_{\text{eff}}c^2 = \int\rho_{\text{matter}}c^2\,dV - \int u_{\text{bind}}\,dV,
> \qquad
> u_{\text{bind}} = \tfrac12\frac{c^4}{7G}|\nabla\varepsilon_{11}|^2.
> $$

The self-energy $T_{00}^{\text{field}}$ and the binding deficit $u_{\text{bind}}$ are both computed on the
**same native diamond-K4 `Grad`** operator (`_build_native_grad_div`, `TETRA_OFFSETS` 4-diagonal build) that the
elliptic solve uses — a Cartesian `np.gradient`/7-pt Laplacian is **never** used (the load-bearing K4
checkpoint; verified: native $|\nabla|^2$ of a unit-slope ramp is exactly 1.0). The self-energy lives on the
**radial/bulk $\varepsilon_{11}$ channel (A1-dilatation)**, the same sector as the matter source — not
cross-wired into shear or EM. The ONE kernel $S(A)=(1-A^2)^{1/2}$ is reused; no new kernel.

**The binding energy is SUBTRACTED, not added** (a gravitational well deficits its own ADM mass — adding it
double-counts). This sign was **Grant-ruled 2026-06-29 = SUBTRACT**: gravity is *attractive* and *local* (bound
systems are bound everywhere), and the substrate-native reason is **frequency down-regulation** — deeper in the
well the compliance reduces ($S\downarrow$, bulk stiffens), the local clock $\omega_{\text{local}}=\omega\sqrt{S}$
down-regulates; since $E=\hbar\omega$ and $m=E/c^2$, matter in the well weighs *less* (the mass defect). The
capacitor-ADD reading would predict a mass *excess* and *repulsive* gravity — falsified by every bound orbit.

The architectural content: an **unlabeled** energy blob (no mass label) sources its own $1/r$ gravity, and
$M_{\text{eff}}$ **emerges** from the converged field's integrated energy. This is the two-way coupling the
engine-architecture frontier flagged as the **make-or-break ABSENT capability (item #86)**. Recover-GR
(weak-field, $\text{amp}=0.02$, $\max A=0.07$) collapses onto the Stage-1 one-way core up to the 2.3% binding
deficit — **consistency-class**.

## §4 — Stage-3 at-risk gate table

All four at-risk checks PASS honestly — each with a boundary-/truncation-robust discriminator whose artifacts
were diagnosed against controls (Rule-10 discipline: running the driver early caught them), not papered over.

| At-risk check | Discriminator | Result | Verdict |
|---|---|---|---|
| 1 — extended (non-δ) blob → $1/r$ exterior | $a+b/r$ vs $a+b/r^2$ model competition; across-N $b$-stability | $1/r$ wins; $b$ stable to $<4\%$ ($0.399\to0.414$) across $N=24{-}32$; $R^2\approx0.88{-}0.94$ | **PASS** |
| 2 — $S_{\min}$-independent emergent $r_s$ | sweep $S_{\min}\in\{10^{-4},10^{-3},10^{-2}\}$ | $M_{\text{eff}}=4.802306$ **bit-identical** (spread $0.00$); $U_{\text{bind}}=4.7\%$ of $M_{\text{matter}}$ (non-zero back-reaction) | **PASS** |
| 3 — ray-traced $4GM/bc^2$ as OUTPUT | truncation-cancelling ratio $\delta_{\text{emergent}}/\delta_{(K/r)}$ + GR-vs-Newton doubling | ratio $0.90\approx1$; $\delta{\cdot}b/K=0.45$ closer to GR $4/7$ than Newton $2/7$, decisively past Newton | **PASS** |
| 4 — two-mass superposition engages nonlinearity | engagement ratio (back-reaction on/off) | $\Delta_{\text{nl}}$(on)$=0.0234$ vs (off)$=0.0098$ → **2.38×** engagement | **PASS** |
| Boundedness (Picard $\rho<1$ PROVEN) | $\rho=\lVert\Delta\varepsilon\rVert_n/\lVert\Delta\varepsilon\rVert_{n-1}$ **measured** | $\rho\in[0.012,0.098]$, grows with compactness as predicted (all $<1$) | **PASS** |
| Energy-honesty (no damping) | per-step $\lvert dH/H\rvert$ at fixed point, pure Picard (outer_mix$=1$) | $\lvert dH/H\rvert\le1\times10^{-4}$ (stationary) | **PASS** |

**FORM/VALUE precision (verify flag carried).** The GR-vs-Newton *doubling factor itself* is NOT dynamically
produced by the loop — it is the imported $\nu_{\text{vac}}=2/7$ (trace-reversed Poisson ratio, a gravity-sector
geometry constant, NOT α); the deflection is exactly linear in $\nu_{\text{vac}}$. The emergent content is the
monopole magnitude $K$ and the emergent field shape; the factor-of-2 is imported (same plumbing as a transformer
turns-ratio). The BH / O(1)-compactness regime ($\rho\to1$, seen at $\text{amp}=0.30$) is a **separate gated
stage**, NOT attempted here.

## §5 — Honest caveats (carried, not re-derived)

- **$M_{\text{eff}}$ emerges, but $G$ is imported.** The value-map $r_s=2GM_{\text{eff}}/c^2$ imports $G$: the
  modulus $c^4/7G$ embeds the back-solved $\xi$, and $K{=}2G$ is GR-imported (PR#261). The Stage-3 win is the
  **architecture** (two-way, $M_{\text{eff}}$ EMERGENT), **not** a new value-level chord. Recover-GR is
  consistency-class.
- **REVERSIBLE half only.** Stage-3 is the reversible back-reaction. The **irreversible depletion primitive**
  (F6 / the DE-tracks-matter chord) is a NEW second dissipation channel, **UNBUILT**, deferred to Stage-4 — see
  [`dark-energy-latent-heat-definition.md`](../../cosmology/ch04-generative-cosmology/dark-energy-latent-heat-definition.md)
  §5 (F6 = ABSENT-INVENTED; one prior `photon_deplete=True` attempt detonates). Stage-3's `solve_backreaction`
  is a **static-elliptic** fixed point; there is no $a(t)$ Friedmann time-evolver here (the de Sitter fate is
  asserted analytically, not simulated).
- **Both stages α-CLEAN** (gravity sector; source-level guard tests). The modulus $c^4/7G$ is a gravity constant
  ($G$-imported), tagged honestly — not α-derived.
- **The strong-field chord (Stage-4 target, per Grant's SUBTRACT ruling).** The chord is NOT the weak-field sign
  (that is the observed redshift/defect) — it is the *saturation* of the frequency down-regulation in the strong
  field, where $S\to0$ at the yield shell, $\omega_{\text{local}}\to0$ (the clock freezes) and AVE's $\sqrt{S}$
  can peel from GR's $\sqrt{1-r_s/r}$ — measurable only by a ruler that cannot leave the region of influence.
  Carried as the Stage-4 strong-field target, NOT claimed here.

## Cross-references

- [`einstein-field-equation.md`](einstein-field-equation.md) — the inherited linear GR core (EFE as variable-impedance LC; clm-y9old1, clm-07kd5v, clm-8nkvwy) that both stages correct-ON and recover.
- [`gravitational-refractive-index-gradient.md`](gravitational-refractive-index-gradient.md) / vol3 `clm-rd9cjm` — $n(r)=1+(2/7)\varepsilon_{11}$, $\varepsilon_{11}=7GM/c^2r$; the far-field target Stage-1 recovers.
- [`interior-singularity-resolution.md`](../../cosmology/ch15-black-hole-orbitals/interior-singularity-resolution.md) (clm-ir8h78) — the analytic Topological Halting ($\rho_{\text{eff}}=\rho_0/S_{\text{topo}}^3$, shell at $r_{\text{sat}}=3.5\,r_s$) that Stage-1 numerically realises via elliptic relaxation.
- [`lattice-extreme-bh-rationality.md`](../../cosmology/ch15-black-hole-orbitals/lattice-extreme-bh-rationality.md) — the $r_s$-vs-$r_{\text{sat}}$ channel split (EM horizon at $r_s$ vs matter/shear yield reflector at $r_{\text{sat}}=7GM/c^2$).
- [`dark-energy-latent-heat-definition.md`](../../cosmology/ch04-generative-cosmology/dark-energy-latent-heat-definition.md) §5 — the UNBUILT F6 / DE-tracks-matter chord (Stage-4), for which this two-way loop is the reversible precursor.
- [`../../../common/engine-capability-map.md`](../../../common/engine-capability-map.md) — the engine capability tracker; the two-way back-reaction is recorded there as landed (§Gravity-sector capabilities).
- Engine source: [`src/ave/gravity/gw_propagation.py`](../../../../../src/ave/gravity/gw_propagation.py) (`relax_finite_core_strain`, `clip_independence_gate`), [`src/ave/gravity/backreaction.py`](../../../../../src/ave/gravity/backreaction.py) (`solve_backreaction`, `effective_mass`, `ray_trace_deflection`, `boundedness_energy_gate`).

---


---

> **⚑ Sign-relativity declaration (Grant ruling 2026-08-04; [`wall-taxonomy.md`](../../../common/wall-taxonomy.md) §10; PR #869 FLAG-W).** The BULK-stiffens line (:59), read as a wall reflection, is the **SERIES-graded projection at the LOAD plane**. With this leaf's own $\rho_{eff}=\rho_0/S^3$ (:73), rigidity and $c_{bulk}\to0$ hold **simultaneously** — speed divides by density while impedance multiplies by it: $c=\sqrt{K/\rho}\to0$, $Z=\sqrt{K\rho}\to\infty$. The apparent conflict with [`bulk-impedance-at-saturation-boundary.md`](../../cosmology/ch15-black-hole-orbitals/bulk-impedance-at-saturation-boundary.md):39 and its channel table ($\Gamma_{bulk}\to-1$) — **three rows when this declaration was written 2026-08-04; FOUR since 2026-08-05**, row 4 being the Cosserat micro-rotation channel, which is *unwalled* at $r_{sat}$ **on the separate-kernel (L∞-across-grades) member of an open fork — canon records the cross-grade combine rule as underdetermined at $O(\alpha)$ ([`common/axiom-register.md`](../../../common/axiom-register.md):190,:232), and on the normalized-L2 member row 4 does not stand; fence added by the doc lane 2026-08-05, not in the ruled text ([`2026-08-05-ruling-kernel-collapse-rescope.md`](../../../../../_orchestration/docket-entries/2026-08-05-ruling-kernel-collapse-rescope.md)`:10`–`:21`, PR #897, landed), routed to Grant; full statement at [`wall-taxonomy.md`](../../../common/wall-taxonomy.md) §10.2** — is plane/projection/profile relativity, not a contradiction; any signed $\Gamma$ is **computed-not-chosen** from the branch-derived indicial wall row. Open physics: the constitutive grading near the wall ($\rho(A)$: FORK-3(b), axial run in flight; $K(A)$). Body above preserved per Rule 12. **⚑ FENCE RE-POINT, 2026-08-06 — this routing note now points at the v2 record.** The citable ruled text is the versioned re-issue [`2026-08-06-ruling-kernel-collapse-rescope-v2.md`](../../../../../_orchestration/docket-entries/2026-08-06-ruling-kernel-collapse-rescope-v2.md):13–29, which **carries the cross-grade combine-member fence inside the ruled text itself**; the 2026-08-05 v1 record is preserved and gains a dated pointer to it. **The earlier *"the omission is at the RULING … routed to Grant for a possible re-issue"* language is RESOLVED — the re-issue happened**, so the fence is now carried AT THE RULING and no print site has to supply it. **Nothing about the physics moves:** the carve-out is still conditional on the per-grade (L∞-across-grades) member, and the cross-grade combine rule is still canon-OPEN. Delta declaration (three deltas from v1, all declared) and the CORRECTED engine-residence map: [`2026-08-06-ruling-kernel-collapse-rescope-v2-correction.md`](../../../../../_orchestration/docket-entries/2026-08-06-ruling-kernel-collapse-rescope-v2-correction.md) C1/C2 — the engine codes the saturation amplitude **three** ways across two live functionals plus a separate objective, so *"the member the engine actually codes"* is over-broad; the carve-out's receipt is STRUCTURAL, not numerical. 🔴 **[DEMOTED 2026-08-11 — R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]**

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
speed**. Corpus text quoted below is reproduced from the banked audit and is
**content-verified at HEAD (markup-reduced, not byte-identical)**; it is never reworded.

**Rows carried in this file.**

- **`:59`** — stamped at `:59`. *(family: K-backed stability argument)*  ⚑ **R49 4π-CONVENTION**
  Quoted claim (content verified at HEAD; markup-reduced from the banked audit):
  ```text
  BULK stiffens: D=1/S→∞ at A→1 (the modulus goes rigid, halting the collapse).
  ```
  Audited rationale, verbatim from the banked worklist:
  ```text
  Same class as the prereg's cauchy-implosion expectation: stability delivered by a divergent bulk-modulus reservoir; under the carve stability is kinematic (no compression DOF to implode). The static elliptic D(A) dress profile itself survives (bound-response FORM); mirrored at vol3/claim-quality.md:1258.
  ```

  **Resolution.** The demoted carrier is the propagating A1 / bulk branch; under Axiom 5 clause G that slot is the **bound response**, so the re-derivation must be re-posed on the bound-sector constitutive law (bias $\varepsilon_{11}$, bound response $\mathbf{u}_0$, mechanism gloss back-reaction) rather than on a compression wave. **⚑ R49:** where this row's re-derivation runs through the elliptic bias law, that law carries the **declared 4π source convention** (canonical declaration in `gordon-optical-metric.md`, claim `clm-rd9cjm`); a correction of that class is an R31-style dated correction, not a re-ratification.

- **`:194`** — stamped at `:194`. *(family: Z_bulk = ρc_bulk formula)*  ⚑ **BIAS-DEBT**
  Quoted claim (content verified at HEAD; markup-reduced from the banked audit):
  ```text
  rigidity and c_bulk→0 hold simultaneously — speed divides by density while impedance multiplies by it: c=√(K/ρ)→0, Z=√(Kρ)→∞
  ```
  Audited rationale, verbatim from the banked worklist:
  ```text
  c_bulk=√(K/ρ) used as a formula treats K as a dynamical wave reservoir; the FLAG-W plane/projection/profile-relativity content (|Γ|=1 wall, sign computed-not-chosen) survives, the speed/impedance formula pair is the import's and is owed re-derivation.
  ```

  **Resolution.** The demoted carrier is the propagating A1 / bulk branch; under Axiom 5 clause G that slot is the **bound response**, so the re-derivation must be re-posed on the bound-sector constitutive law (bias $\varepsilon_{11}$, bound response $\mathbf{u}_0$, mechanism gloss back-reaction) rather than on a compression wave. **⚑ BIAS-DEBT:** this row's re-derivation turns on finite-speed bias dynamics, so the resolution is the ratified axiom **with THE BIAS PROPAGATION THEOREM standing** (clause (c1)) — the replacement is *owed, not held*.

**Records.** Ruling **R40** (the demotion sweep) · the banked worklist
[`r40_sweep_worklist_verified.json`](../../../../../research/drivers/r40_sweep_worklist_verified.json) · batch-0
scope verification and batch-1 execution records in `_orchestration/` · this batch's record
`_orchestration/2026-08-12_r40-sweep-batch2a.md`.

