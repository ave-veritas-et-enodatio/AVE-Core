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

**Linear order: ORTHOGONAL.** A₁ (dilatation) and T₂ (Cosserat shear) are
*different lattice point-group irreps* — canon: $T_d$ symmetry forces the
$A_1 \oplus T_2$ decomposition (A0.4). Distinct irreps ⇒ the **linear response
block-diagonalizes**: at linear order the two sectors do not talk. (This is also
why the sectors are cleanly "mass = A₁" vs "charge = T₂-winding" — A0.4, and
mass = A₁ per `#260`, A0.5 grounding lines.)

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

## §5 — Ratio-of-change: p = 0 IS gravitational-dilation universality

<!-- section body: commit 4 -->

## §6 — Balloon → cavity (the confinement correction); decay kept distinct

<!-- section body: commit 4 -->

## §7 — The test + two can-fail gates

<!-- section body: commit 5 -->

## §8 — Staged plan (pilot-before-scale)

<!-- section body: commit 5 -->

## §9 — The open gut-check (surfaced to Grant, UNRESOLVED)

<!-- section body: commit 5 -->
