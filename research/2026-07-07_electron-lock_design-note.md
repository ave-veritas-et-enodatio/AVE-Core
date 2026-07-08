# Electron-Lock (Round-2 / "B") — Design-Rationale Note

**Date:** 2026-07-07
**Arc:** `analysis/electron-lock-design-note`
**Nature:** **DESIGN-RATIONALE / HYPOTHESIS.** This is DOCUMENTATION of a
Grant-ratified in-chat design walk for the round-2 ("B") electron engine. It is
**not a result.** Every physics statement below is of the form *"the walk
motivates TESTING X"* or *"the walk's design rationale is Y"* — never *"X is
established."* No result-claims. No emergence-claims. Nothing here has been run.
**Register (per `consistency-vs-emergence`):** the note is entirely
design/hypothesis class; any measurement it motivates is tagged where it would
land, and no such tag is asserted as achieved.
**Predecessor context:** the tick-floor arc (PR #567, branch
`analysis/electron-tick-floor`, OPEN — not on `main` as of this note) was
honestly re-scoped in the in-chat walk: its `N_min = 7` is a **linear-regime
sampling-representability floor** (a lower bound), its engine leg was a
**readout tautology** (the estimator reads back what the sampler encodes), and
the "derived twice" framing was **withdrawn**. Round-2 ("B") is the
genuinely-dynamical successor. THIS note documents B's design rationale only; it
adjudicates nothing about #567 and lands no result of its own.

---

## FIREWALL (mechanical exclusion — load-bearing)

The following are **EXCLUDED from every derivation this note motivates.** B may
compare against them only in an explicitly firewalled §COMPARISON *after* a blind
derivation has closed; they may never enter a derivation path as input, target,
tuning knob, or convergence check:

- **α** and **α⁻¹** (the fine-structure constant — canonically a *Class-B echo*
  at the value level; scale forced, value = calibration identity).
- **m_e** (electron rest mass) — canon itself flags this **"CALIBRATION ANCHOR,
  not derivation"** (`electron-identification.md:60`).
- **ƛ_C** (reduced Compton wavelength) — canon itself flags this
  **"DEFINITIONAL, not derivation"** (`electron-identification.md:66`).
- **the VALUE of ω_C** treated as *the* electron scale (the AVE-native ↔ SI
  conversion of the m_e calibration anchor).
- **Q = 1/α** (the tank quality-factor identity — an IDENTITY, never a
  derivation input; homonym guard: any small integer B derives, e.g. a floor
  ~7, is >3 OOM from 137 and has ZERO α contact).
- **every measured mass ratio** (e.g. muon/electron ≈ 206.77) — see the ⟨N⟩
  knife immediately below.

## THE ⟨N⟩ KNIFE (the sharpest discipline hazard in B)

A non-integer average sampling count **⟨N⟩** — or any continuous ratio B might
report — is *exactly the kind of free real number that can be tuned to reproduce
206.77* (the muon/electron mass ratio). Therefore:

> **⟨N⟩, and any ratio B outputs, MUST be DERIVED BLIND from the settled
> dynamics — never fit to, tuned toward, seeded from, or checked against a mass
> ratio during the derivation.** The number **206.77 is named here solely to
> mark the forbidden target.** If a mass ratio ever touches a derivation path,
> that path is DEAD by construction (it has re-imported the value it claims to
> explain). A blind-derived ⟨N⟩ that only *afterward* is priced against a ratio
> in a firewalled comparison is the only admissible route.

---

## §0 — Canon anchors (verified verbatim, two-method: `Read` + `grep`)

All quotes below were read from the working tree at HEAD `bdf48720` (== `origin/main`)
and cross-checked by `grep`. Line numbers are as of that HEAD.

**A0.1 — Canonical 4-property electron definition**
(`manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/electron-identification.md:28–31`):
> 1. **Real-space topology: $0_1$ unknot** — the simplest closed flux-tube loop
>    at minimum ropelength $2\pi$ on the K4 lattice. […]
> 2. **Phase-space winding: $(2,3)$ Clifford-torus** — […] **The $(2,3)$
>    "trefoil" is the phase-space winding pattern, NOT a real-space trefoil
>    knot.**
> 3. **Self-saturated TIR cavity ($\Gamma = -1$ at $V_{yield}$)** — […] The
>    lattice self-creates a perfect TIR mirror […] trapping it as a standing
>    wave inside the self-created cavity.
> 4. **T₂-only Cosserat-microrotation core** — […] only the boundary condition
>    flips from impedance-matched ($\Gamma = 0$) to TIR ($\Gamma = -1$).

**A0.2 — (2,3) is a nonlinear-saturation-confined soliton, NOT a linear mode**
(`electron-identification.md:33`, mirrored at `ch8-alpha-golden-torus.md:35`):
> **(p,q) is fundamentally a nonlinear-saturation-confined-soliton topological
> property at the K4-bond-pair LC-tank phase-space level; NOT a linear-regime
> substrate-mode-eigenvalue label** — Path B-prime K4-TLM linear-regime
> band-splitting test FALSIFIED 2026-05-27 empirically per outcome C […]

**A0.3 — phase-space vs real-space** (`ch8-alpha-golden-torus.md:31`):
> The trefoil lives in phase space; the soliton lives in real space.

**A0.4 — sector orthogonality at linear order (T_d forces A₁ ⊕ T₂)**
(`electron-identification.md:52`):
> Ax1 ($T_d$ symmetry forces $A_1 \oplus T_2$ decomposition; Gauss's law forbids
> $A_1$ longitudinal → $T_2$ survives)

Plus **mass = A1** (the mass sector is the A₁ dilatation channel, `#260`; stated
repeatedly in the leaf's Rule-12 banners, `electron-identification.md:13,15,17`).

**A0.5 — two-way back-reaction = the engine-architecture MAKE-OR-BREAK**
(`manuscript/ave-kb/vol3/gravity/ch02-general-relativity/saturating-modulus-and-backreaction.md:20–23`):
> **Stage-3** […] the **TWO-WAY** back-reaction: the gravitational field sources
> ITSELF, and the effective mass **emerges** from the converged field's own
> integrated energy. This is the ARCHITECTURAL win (item #86, the make-or-break
> the engine-architecture frontier flagged ABSENT); it is the REVERSIBLE half
> only (the irreversible depletion / DE-tracks-matter chord is a separate,
> unbuilt Stage-4 primitive).

---

## §1 — The question B answers: is the electron a SELECTIVE LOCK?

**HYPOTHESIS-class framing.** B is designed to ask one question: *do the
electron's coupled structures phase-lock into ONE self-consistent ratio, or do
they drift / decay?* The walk motivates TESTING whether the electron is a
**selective lock** — a configuration the dynamics settle *into* and hold — as
opposed to a configuration that only *appears* stable because it was imposed.

**What B deliberately does NOT ask.** B is *not* asking "does the substrate BUILD
the electron" — genesis / buildability from a free precursor is a **separate,
later question** (and one the keystone energize-LOCK arc already leans-negative
on). Assuming an *already-formed* object is a deliberate design choice: it
**isolates self-consistency from buildability**, so a lock-or-drift verdict is
not confounded by whether the substrate can reach the configuration in the first
place.

**Why this framing is the fix for the #567 readout tautology.** In #567 the
winding was *imposed* on the sampler, and the estimator then *read it back*; the
"lock" was a definition, not an attractor. B's design rationale is that the
winding must be an **output of the settled dynamics**, so that "the electron
locks" is a *measured* property of an attractor and not a restatement of the
seed. §2 makes the three spaces that carry this real.

## §2 — Three coupled spaces (all real DOFs, none hard-wired)

**HYPOTHESIS-class framing.** The walk motivates building B on **three coupled
spaces, each a real degree of freedom the engine must carry independently.** The
discipline point — the direct fix for the #567 readout tautology — is that
**none of the three is hard-wired**; the topological content must EMERGE from,
and be READ OUT of, the settled dynamics.

1. **(a) The $0_1$ unknot RING — real space.** A closed flux-tube loop with a
   real, *pulsing* circumference. This is a real-space DOF the engine evolves;
   it is not a fixed scaffold.
2. **(b) The $(2,3)$ PHASE-winding — Clifford-torus phase space.** In the
   bond-pair LC tank's $(V_{inc}, V_{ref})$ phasor space, the windings are to be
   **READ OUT of the settled dynamics, NEVER imposed.** Per A0.3 the winding
   lives in phase space; the soliton lives in real space — the note keeps these
   coordinate systems distinct (per phase-space-coordinate discipline).
3. **(c) The ENVELOPE / breather amplitude — emergent.** The amplitude profile
   is an output: it may settle **flat** (a steady standing wave) or **breathing**
   (an amplitude-modulated cycle). Which one it is is a *measurement B makes*,
   not an input.

**Canon grounding (all HYPOTHESIS-class as USED here, canon as CITED).** The
round-2 target object is the canonical electron: the $0_1$ unknot in real space
+ the $(2,3)$ Clifford-torus phase-space winding + the confined LC tank held at
the $\Gamma=-1$ TIR wall + the T₂-only Cosserat-microrotation core (A0.1, A0.2,
A0.3). The design claim B TESTS is that these three spaces, evolved as real
coupled DOFs, settle into *one* mutually-consistent configuration — the canon's
four properties are the *target* of the lock test, not an assumed output.

## §3 — Lifecycle / phase-dependence of the sampling floor

**HYPOTHESIS-class framing.** The walk motivates treating the sampling count as
**phase-dependent over the object's lifecycle**, and the topology as
phase-invariant:

- **Near formation** the field is close to uniform → the sampling count sits at
  its **lower bound** (the linear-limit regime where a small integer — the ~7 of
  #567 — is representationally sufficient).
- **At full-amplitude, anharmonic operation** the settled soliton is strongly
  nonlinear → the sampling count is **higher** (finer structure demands more
  ticks/period to represent without aliasing).
- **The $(2,3)$ TOPOLOGY is CONSERVED across all phases** — an integer winding
  cannot change smoothly (A0.2: it is a nonlinear-saturation-confined-soliton
  topological property, not a linear-mode label). **The sampling COUNT is NOT
  conserved** — it tracks amplitude / anharmonicity.

**Re-scoping the #567 floor (explicit).** `N_min = 7` was a **linear-limit
snapshot** — a lower bound sampled where the field is nearly uniform — **NOT the
operating count of the full-amplitude confined soliton.** Canon is explicit that
the physical $(2,3)$ is the nonlinear-saturation-confined object, not the linear
mode (A0.2); the linear-regime band-splitting route was falsified empirically
(A0.2, outcome C, 2026-05-27). B is the genuinely-*nonlinear* successor.

**Design consequence (empirical-driver discipline).** B must sample at the
**full-amplitude saturated phase**, at the **energy-density peaks** of the shell
(top-K $|field|^2$, PML cells excluded), **not** at the near-uniform formation
phase and **not** at a centroid (the centroid of a shell is the empty middle).
Sampling the formation phase would merely re-derive the linear floor and
mislabel it the operating answer — the exact tautology B exists to escape.

## §4 — The A1↔T2 coupling (the transduction mechanism)

**HYPOTHESIS-class framing — the deepest content of the walk.** How does the
mass sector (A₁ dilatation) talk to the charge sector (the T₂ Cosserat
microrotation carrying the winding)? The walk motivates a specific, testable
answer.

**Linear order, at ZONE CENTER: ORTHOGONAL.** A₁ (dilatation) and T₂ (Cosserat
shear) are *different lattice point-group irreps* — canon: $T_d$ symmetry forces
the $A_1 \oplus T_2$ decomposition (A0.4). Distinct irreps ⇒ **for the homogeneous
($k = 0$) linear response the response block-diagonalizes**: at zone center, at
linear order, the two sectors do not talk. (This is also why the sectors are
cleanly "mass = A₁" vs "charge = T₂-winding" — A0.4, and mass = A₁ per `#260`,
A0.5 grounding lines.)

**Scope of the block-diagonalization (finite-$k$ caveat — precise only at $k=0$).**
The orthogonality above holds **at zone center ($k = 0$ / homogeneous response)
only.** $T_d$ is **non-centrosymmetric**, so at *finite* $k$ a Lifshitz-type
gradient cross-term $A_1 \cdot (\nabla \cdot T_2)$ is symmetry-allowed and the
sectors *can* couple at linear order in a gradient. That finite-$k$ Lifshitz
coupling **exists but is OUT OF SCOPE** for the homogeneous coupling B tests:
B's varactor claim (§4, below) is an **adiabatic / homogeneous ($k = 0$) bias**,
exactly the regime where the block-diagonalization holds — so **the claim is
unaffected**; only the blanket "linear response block-diagonalizes" phrasing
over-reached, and it is now scoped to $k = 0$.

**The coupling is PURELY NONLINEAR, and its lowest term is forced by symmetry.**
The symmetry-lowest cross term is
$$A_1 \cdot |T_2|^2$$
— dilatation times the **scalar invariant** of the shear. The bare product
$A_1 \cdot T_2$ is **FORBIDDEN**: $T_2$ is not a scalar (it carries the $T_2$
irrep), so $A_1 \cdot T_2$ is not a group scalar and cannot enter a scalar
energy. $|T_2|^2$ *is* the quadratic $T_2$-invariant (a scalar), so
$A_1 \cdot |T_2|^2$ is the lowest-order scalar cross-invariant that can exist.
This is a group-theory design *rationale* B must confirm the engine reproduces —
NOT an asserted result.

**It is PARAMETRIC, not resistive — and Ax3 SELECTS that.** In this term A₁
**modulates the T₂ tank's L/C** — a *varactor bias tuning the mode*, not a force
pushing it. The walk motivates this as the physically-correct form because the
*alternative* — a dissipative A₁→T₂ transduction — would be a **velocity-coupled
loss term, which Axiom 3 forbids below yield** (the substrate is lossless in the
reactive regime). So below yield the coupling is *necessarily* reactive /
parametric; Ax3 is not decoration here, it is the selection rule.

**Consequence: topology robust, count mobile.** A smooth parametric retune
**cannot cut a winding** — the $(2,3)$ integer is protected (consistent with
A0.2's saturation-confined-soliton topology). But the same retune **shifts
$\omega_{(2,3)}$**, so the *sampling count is mobile* (ties directly to §3: count
tracks amplitude, topology does not). B TESTS exactly this split: winding
invariant, count moving, under an A₁ bias.

**The SAME term read BACKWARD = the two-way back-reaction (flag-don't-fix).**
Read $A_1 \cdot |T_2|^2$ the other direction and the time-average of the shear
sources the dilatation:
$$\langle |T_2|^2 \rangle \;\longrightarrow\; A_1
\qquad(\text{EM / charge energy gravitates} \to \text{mass}).$$
The term is *symmetric* under read-direction — so the mechanism that lets A₁
retune the tank is the *same* mechanism by which the tank's stored energy sources
mass. **Status, stated without collapsing the two facts:**

- **symmetry-PRESENT.** The $A_1 \cdot |T_2|^2$ invariant is the same object
  read backward; nothing forbids the sourcing direction.
- **engine-UNVERIFIED (for this object).** Canon records the *general*
  gravity-sector two-way loop as **LANDED** — Stage-3, the REVERSIBLE half, item
  #86, "the make-or-break the engine-architecture frontier flagged ABSENT"
  (A0.5) — while the **irreversible / DE-tracks-matter half (Stage-4) is
  UNBUILT** (A0.5). The **electron-LOCAL instantiation** — *this* object's own
  confined $\langle|T_2|^2\rangle$ self-consistently sourcing *its own* A₁ mass
  inside B — is not something the round-2 electron engine has demonstrated. B's
  **forward** direction (A₁ retunes T₂) is the tractable near-term test; the
  **backward** sourcing is the symmetry-present / engine-unverified make-or-break
  and is flagged as such, not assumed.

## §5 — Ratio-of-change: N-invariance is a NECESSARY CONSEQUENCE of gravitational-dilation universality

**HYPOTHESIS-class framing — the payoff of the walk.** Write the settled
sampling count's response to a uniform substrate compression $S$ as
$$N \;\propto\; S^{\,p},
\qquad p = (\text{clock sector's saturation exponent}) - (\text{$(2,3)$ mode's saturation exponent}).$$
$p$ is the *difference of the two sectors' saturation exponents*. The walk's
payoff is that $p$ is **not free** — it is pinned by an observation.

**The key implication (ONE-DIRECTIONAL — not an equivalence).**
> **"gravitational time dilation is universal"** $\;\Longrightarrow\;$ **"$N$ is
> invariant under uniform compression."**
> The converse does **NOT** hold: one invariant ratio does not imply *all* ratios
> are fixed. So $N$-invariance is a **necessary consequence / consistency
> requirement** of universal dilation — **not** a proof or reproduction of it.

Universal dilation means: a clock lowered into a potential well slows by **one
common factor across all of its frequencies** (redshift is achromatic — no
dispersion). If every frequency redshifts by the same factor, **every frequency
RATIO is fixed** under a change of potential. $N$ is such a ratio (ticks of the
sampling clock per mode period), so universality **forces** $p = 0$. This is the
**forward direction only** (universality $\Rightarrow$ $N$-invariant); it does
**not** run backward — $N$-invariance alone (one ratio fixed) would **not**
establish that *every* ratio is fixed, i.e. would not prove universality.
Therefore **$p = 0$ is a consistency requirement REQUIRED of B by an observed
fact** (achromatic gravitational redshift) — not a value fit to make B work, and
not something B's passing the gate would *prove*. *(Consistency-class use: B must
be CONSISTENT with universal dilation; no value is fit.)*

**$p = 0$ forces EQUAL saturation exponents — and, given the channels differ,
co-keying.** Strictly, $p = 0$ forces the two **saturation exponents to be
equal**. The step from *equal exponents* to *same channel* rests on a
**load-bearing premise**: the canon channels **scale differently** — shear
$\propto S^{+1/2}$ vs EM $\propto S^{-1}$ — so **distinct channels carry distinct
saturation exponents.** *Given* that premise, equal exponents can be realised
only by putting the **sampling clock and the $(2,3)$ mode on the SAME $S$-channel**
(co-keyed). Make the premise explicit: it is precisely
*distinct-channels-⇒-distinct-exponents* that converts "equal exponents" into
"same channel" — were two channels to happen to share an exponent, equal-exponent
would *not* force co-keying. If the clock and mode rode *different* channels (hence
different exponents), $p \neq 0$ and dilation would be dispersive.

**Why cross-keying would visibly break dilation.** The canon channels do *not*
scale alike. The impedance branches are anchored:
`Z_eff = Z0·√S → 0 ⟹ Γ → −1` (the μ/shear "mass-cage SHORT") versus the
`ε`-load `Z_eff = Z0/√S → ∞ ⟹ Γ = +1` (the "OPEN anti-trap")
(`research/2026-06-20_mass-sector-characterization_synthesis.md:110–116`). The
corresponding *channel-speed* scalings — **shear $\propto S^{+1/2}$ (i.e.
$c_{shear} = c_0\sqrt S$) vs EM $\propto S^{-1}$ (i.e. $c_{EM} = c_0/S$)** — are
**SETTLED, not an open ambiguity.** The shear-speed exponent is canonically
$\sqrt S$ (`manuscript/ave-kb/CLAUDE.md:80`, `c_{shear}(A_0) = c_0\sqrt{S(A_0)}`,
canonical at `clm-8nkvwy:113`); the apparent "$\sqrt S$-vs-$S^{1/4}$" ambiguity
was an **already-corrected code defect** — an $S^{1/4}$ exponent attached to a
**refractive-index / Op14 diagnostic, NOT the shear speed**
(`src/ave/core/crystal_engine.py:431–432`: "The legacy magnitude was S^{1/4} (an
exponent defect — half the physical power). Corrected to ½ here") — **resolved
by Grant's F1 ruling** (`research/2026-06-30_electron-portmap-derivation_result.md:550`:
"**(R2) The `S^{0.25}`-vs-`S^{0.5}` exponent — RESOLVED = `S^{0.5}` canonical
(Grant F1, this session).**"). The genuinely-open item is a *different* thing:
the **near-yield SATURATED $\sqrt S$-shear validation** (the saturated $G$-modulus
dynamics), which is the **unbuilt Stage-4 primitive**
(`research/2026-06-23_engine-stage1-transverse-modes_result.md:196`: "The full
near-yield √S-shear validation (the saturated G-modulus dynamics) is Stage 4").
So B inherits the *exponent* as settled ($\sqrt S$); what remains open for B to
establish dynamically is the **saturated near-yield behaviour**, not the sign of
the power. *Given* those settled scalings, cross-keying (clock on one channel,
mode on the other) yields an exponent difference of order one — the walk's
estimate is $p \approx 3/2$ (design-input, not asserted) — which would **visibly
break dilation universality.**

**The sky constrains the internal channel architecture.** This is the deep
turn: an astronomical fact (achromatic redshift) constrains B's *internal* wiring
(the clock and the mode must share a channel). **B's uniform-$N$ gate is a
FALSIFIER, not a proof.** A measured $p \neq 0$ under uniform $S$-scaling is
**inconsistent with universal dilation** (the engine would predict dispersive
gravitational redshift, which is not observed) and **falsifies** the co-keyed
design — **not a knob to tune.** A *passing* uniform-$N$ result does **not**
reproduce or prove universality (the backward direction fails — one invariant
ratio is not all of them); it shows only that B is **consistent with** universal
dilation on this one ratio.

## §6 — Balloon → cavity (the confinement correction); decay kept distinct

**HYPOTHESIS-class framing — a continuum-mechanics correction the walk makes.**

**Uniform compression loads A₁ ONLY.** Correct continuum mechanics: a hydrostatic
pressure is a **pure dilatation with zero shear.** So a uniform $S$-scaling loads
*only* the A₁ (dilatation) sector — it does not, at leading order, drive T₂. This
is why §5's "uniform compression" is an A₁-only probe.

**A₁ is the MASS, not the surface tension.** The confining "tension" of the
electron is **not** a bulk elastic tension in A₁ — it is the **T₂ $\Gamma=-1$ TIR
wall** (a boundary condition), with mass = A₁ (A0.1 property 3/4; mass = A₁ per
`#260`, A0.5 grounding lines). Keeping this straight is the whole correction.

**Balloon (collapse-prone) vs cavity (stable).**
- A **balloon** is held by an *elastic tension that SOFTENS under compression* —
  the compliance divergence $C_0/S$ **is** a softening, so compression begets
  more compression: a **positive-feedback runaway → COLLAPSE.** A balloon
  electron would be unstable.
- The electron is instead a **resonant CAVITY.** The **TIR mode-number is
  dilation-INVARIANT** — a protected integer (consistent with §3/§4: the winding
  is topological, count-mobility is separate). The balloon is the *collapse-prone
  precursor*; the **$\Gamma=-1$ wall is what makes the object stable.**

**DECAY is a DISTINCT effect (homonym discipline — do NOT conflate with the
ratio effect).** Decay is **not** a frequency-ratio phenomenon; it is a
**boundary** phenomenon:
> An **asymmetric** load breaks the impedance match. When **$\varepsilon$ scales
> without $\mu$**, the channel impedance shifts off the matched short: the μ/shear
> branch sits at `Z=Z0·√S→0 ⟹ Γ→−1` (wall closed) while the ε-only branch runs
> to `Z=Z0/√S→∞ ⟹ Γ→+1` (open)
> (`research/2026-06-20_mass-sector-characterization_synthesis.md:110–116`). So
> $\Gamma$ **deviates from $-1$ → the TIR wall LEAKS.**

**The clean summary.**
- **Uniform** load → co-keyed → **$p = 0$** → ratio protected (§5). *(ratio
  effect)*
- **Asymmetric** load → $\Gamma \neq -1$ → **wall leaks → decay**. *(boundary
  effect — e.g. a heavier lepton "breathes harder" and cracks its own wall.)*

These two are **different mechanisms in different coordinates** and the note
keeps them apart on purpose.

## §7 — The test + two can-fail gates

**HYPOTHESIS-class framing — no result is admissible without a DEMONSTRATED
fail.** A gate that cannot fire is not a gate. B is designed around **two
can-fail gates**; a lock verdict is reportable only if both gates were shown
capable of failing on the same rig.

**(i) NEIGHBOR gate (selectivity).** Seed neighbouring / off-ratio
configurations — $(2,2)$, $(2,5)$, and at least one deliberately off-ratio seed —
and require that **at least one does NOT lock.** The $(2,3)$ must be a
**SELECTIVE attractor**, not merely a **seeded fixed point** that persists
because it was planted. *Can-fail condition:* if *everything* locks (neighbours
included), the "lock" carries no information ⇒ route to **[NON-SELECTIVE →
NO-CONSTRAINT].**

**(ii) N-INVARIANCE gate (the §5 dilation check, made operational).** Apply a
**uniform** $S$-scaling and require **$N$ invariant** (co-keyed, $p = 0$); apply
an **asymmetric** load and require **$N$ shifts**. *Can-fail condition:* $N$
moving under *uniform* $S$ is a consistency failure (dispersive dilation) ⇒ route
to **[CONSISTENCY-FAIL].** This gate is a *falsifier*, not a fit.

**Two design-critical PRECONDITIONS on the N-invariance gate (OPEN — B must
satisfy both; this note does NOT resolve them).**

- **(P1) $\omega_{clock}$ IDENTITY — pin what the sampling clock physically IS.**
  The whole $p = (\text{clock exp}) - (\text{mode exp})$ framework presumes the
  sampling clock is a **physical substrate mode riding an $S$-channel with its own
  saturation exponent.** If $\omega_{clock}$ is instead the **integrator tick-rate**
  (a numerical cadence with *no* $S$-exponent), then the uniform-$N$ gate tests
  the **integrator, not the physics** — $p = 0$ becomes an artifact of the
  time-step, not a statement about dilation. **B must PIN $\omega_{clock}$ as a
  real $S$-keyed substrate mode BEFORE the uniform-$N$ gate is meaningful.** This
  is the **same fork** as the §9 gut-check (is there a physical bias/signal split
  at all?); it is surfaced here, not resolved.

- **(P2) EMERGENT-CO-KEYING GUARD — co-keying must be READ OUT, never HARD-WIRED
  (the #567-tautology preemption).** If B **hard-wires** co-keying — building the
  clock and the $(2,3)$ mode as harmonics of the *same tank by construction* —
  then $N$-invariance under uniform $S$ is **DEFINITIONAL** and the gate **cannot
  fire**, re-importing the exact #567 readout tautology this note exists to escape.
  Two hard design constraints follow: **(1)** the **clock and the $(2,3)$ mode
  must be INDEPENDENT evolved DOFs** whose channel-keying is **read out of the
  settled dynamics, not planted**; and **(2)** B must **DEMONSTRATE the uniform-$S$
  gate CAN fail** — seed a deliberately *cross-keyed* configuration and show $N$
  **moves** under uniform $S$ — **before any uniform-$S$ PASS is informative.**
  This is the **can-fire discipline** of §7 applied to the physics of §5: a gate
  that is definitionally satisfied is not a gate.

**Result bins (pre-registered; the note asserts NONE of them — B decides).**
- **[SELECTIVE-LOCK]** — $(2,3)$ selectively locks; report the settled ratio and
  the blind-derived $\langle N\rangle$ (subject to the §FIREWALL ⟨N⟩ knife: $\langle N\rangle$
  derived blind, priced against a mass ratio only *afterward*, if at all).
- **[NO-LOCK]** — $(2,3)$ does not lock; the electron-as-selective-lock
  hypothesis is falsified.
- **[NON-SELECTIVE → NO-CONSTRAINT]** — everything locks, including neighbours;
  the test constrains nothing.
- **[CONSISTENCY-FAIL]** — $N$ moves under uniform $S$; the engine predicts
  dispersive gravitational dilation. Falsified per §5.

## §8 — Staged plan (pilot-before-scale)

**HYPOTHESIS-class framing — cheapest can-fail first.**

- **Stage-1 (minimal, kill-cheap).** Model the $(2,3)$ as **two real coupled
  oscillators** plus the **NEIGHBOR gate** only. Single question: *does $(2,3)$
  selectively lock AT ALL?* If it does not lock, or locks non-selectively,
  **kill the branch cheaply** — no need to build the ring/envelope/saturation
  machinery to learn there is no selective attractor.
- **Stage-2 (scale-up, gated on Stage-1).** Add the **$0_1$ ring**, the
  **emergent envelope**, and the **saturation N-INVARIANCE gate** (the full §5
  dilation-universality check on the full three-space object of §2). Run this
  **only if Stage-1 passes.**

## §9 — The open gut-check (surfaced to Grant, UNRESOLVED)

**Flag-don't-fix / lane discipline — this is Grant's call, surfaced not
resolved.** §4's *varactor* framing assumes a **timescale split**: A₁ is a **slow
bias** and T₂ a **fast small-signal**, so A₁ "tunes" the T₂ tank. The open
question:

> **Is the A₁-bias / T₂-small-signal hierarchy REAL** (mass slow, charge fast —
> the varactor framing of §4 holds), **or are the two sectors CO-EQUAL
> two-mode-resonance oscillators** with **no clean bias/signal split** (in which
> case §4's varactor picture is the wrong model and B needs a genuine two-mode
> resonance model)?

This decides the **modelling backbone** of B: parametric-varactor (one slow, one
fast) vs coupled two-mode resonance (co-equal). It is **UNRESOLVED** and is
**Grant's framing call** (Grant is the third source of truth for framing-level
physics; per lane discipline the implementer surfaces it rather than picking).
The rest of the note is written under §4's varactor framing *as the leading
hypothesis*; §9 flags that its load-bearing assumption is not yet settled. A
closely-related **operational** form of this same fork — that $\omega_{clock}$
must be a *physical* $S$-keyed substrate mode (not the integrator tick-rate) for
the §5 / §7 uniform-$N$ gate to mean anything — is folded into §7 as precondition
**(P1)**; §9 and (P1) are the same open question viewed from the framing side and
the gate side respectively.

---

**Closing register reminder.** Nothing above is a result. Every section states
what B is designed to TEST and why the walk motivates that design. The FIREWALL
and the ⟨N⟩ knife bind every derivation B may run; the two can-fail gates (§7)
bind every verdict B may report. This note lands *design rationale only.*
