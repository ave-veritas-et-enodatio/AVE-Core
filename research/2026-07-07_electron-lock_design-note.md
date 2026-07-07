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

<!-- section body: commit 2 -->

## §2 — Three coupled spaces (all real DOFs, none hard-wired)

<!-- section body: commit 2 -->

## §3 — Lifecycle / phase-dependence of the sampling floor

<!-- section body: commit 2 -->

## §4 — The A1↔T2 coupling (the transduction mechanism)

<!-- section body: commit 3 -->

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
