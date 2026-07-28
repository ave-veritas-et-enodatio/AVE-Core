# D1 — the sector-of-storage question and the inertia-route options — scoping report (2026-07-26)

**Class: SCOPING (pre-lane). ORCHESTRATION-LANE output, NOT adversarially reviewed; prototype/analytic-grade; all criteria herein DRAFT-NOT-FROZEN; mints no `clm-`, mints no `def-`; banks no verdict; ratifies nothing.** Engine byte-untouched (isolated worktree off `origin/main` @ `c8ceacc3`; no driver run, no solver code). **⚠ NOT REVIEWED — nothing below is Grant-ratified except where a verbatim `[sic]` quote is marked as his.**

**Why this doc exists.** The analysis in §2–§6 was produced in an orchestration conversation on 2026-07-21/26 and was **tracked nowhere in the corpus** — while the live sector-of-storage walk and the charter decision **D1** both depend on it. This banks it so the corpus owns its own evidence and every claim below is checkable against a path. It is the citation basis, not an adjudication.

---

## 1 The question

**Charter D1**, verbatim from [`research/2026-07-21_continuum-radial-solver_CHARTER.md`](2026-07-21_continuum-radial-solver_CHARTER.md) §0 — the T2 storage wording lands at **`:15` (the D1 entry)**; the **`:54` I8 table row** attributes only `clm-m5swh9` (`A1 ⊥ T2`; "which sector's `c²` … is not automatic"). The charter itself calls them "the D1/I8 object" (`:16`, `:35`, `:52`), so the identification is corpus-supported

> **D1 — the sector-crossed c² choice (the plumber-physical question; the pre-test-physics-check surfaced to Grant).** In the E=mc² import `ρ_contribution = E_trapped / c² · (participation)`, **which sector's wave-speed sets c²** — the A1 compression speed `c_P` (`0.519`), the shear speed `c_S` (`0.286`), or the transverse-EM speed `c_EM`? … **OPEN — surfaced, not picked.**

The reason it is not automatic is the `A1 ⊥ T2` sector-ownership watch: the trapped energy is labelled `T2`/swing-class while the carrier whose inertia it would load is `A1` ([`manuscript/ave-kb/common/relative-offset-principle.md`](../manuscript/ave-kb/common/relative-offset-principle.md):49, `clm-m5swh9` — the OPEN magnitude leaf). §6 below records that **this label itself is in contradiction with older Grant-ratified canon**, which is why the question has a walk attached rather than a solver.

## 2 The `m*` route — DECORATION (the negative)

A route surfaced in the same window was: read the caged medium's dispersion, take the band-bottom curvature, and call `m* = ħ²/(d²E/dk²)` the loaded inertia — thereby reading D1's `c²` off a lattice measurement. **That route cannot answer D1.** Two independent reasons, both structural.

**(a) Wrong loading topology — INTRA-band vs INTER-object.** The semiconductor `m*` is an **intra-band** statement: it dresses *the same carrier whose dispersion you are reading*. One band, one carrier, one number — the curvature *is* that carrier's own inertia. D1's loading is **inter-object**: a bound cage's trapped energy loading a **different** propagating carrier's effective density. Those are not the same physical relation, and the semiconductor formula is silent about the second.

**(b) The band-bottom curvature read is SECTOR-BLIND (the decisive point).** The correct physics home for inter-object loading is the **locally-resonant acoustic metamaterial** effective density

```
ρ_eff(ω) = ρ_0 · [ 1 + θ · ω_0² / (ω_0² − ω²) ]
```

where `ω_0` is the internal resonance of the embedded inclusion and `θ` its bare mass fraction. The corpus's own working form `ρ_eff/ρ_0 = 1 + β·φ` ([`relative-offset-principle.md`](../manuscript/ave-kb/common/relative-offset-principle.md):41, C-load; scanned `β ∈ {0,1,3}` in the `#782` RVE arc) is **exactly its `ω → 0` static limit**. But in that limit — equivalently `k → 0` on the host branch, which is exactly where a band-bottom curvature is read — the resonant factor `ω_0²/(ω_0² − ω²) → 1`, so **`ω_0` divides out**:

```
ρ_eff(0) = ρ_0 · (1 + θ)
```

The static/band-bottom number carries **only the bare-mass fraction `θ`** and **no sector information whatsoever**. Whichever sector's speed sets `ω_0`, the `ω → 0` read returns the same number.

**★Therefore the literal `m*`-from-curvature read must not be headlined as answering D1.** Doing so would present a measurement of the **structural** added-mass term as if it were the **trapped-energy** term — the same conflation class the β scoping doc's three structural absences already named ([`research/2026-07-21_beta-tracking-feasibility_scoping.md`](2026-07-21_beta-tracking-feasibility_scoping.md) §3: no mass-energy equivalence, no advective pattern transport, the imposed grade IS the answer). Class: **DECORATION** — a real, measurable, publishable number that does not touch the question it is being pointed at.

**Cite note (`def-mstar1`).** A `def-mstar1` vocabulary node was expected to be the cross-reference for the `m*` term here. **It is NOT on `main`** at `c8ceacc3` (two-method: `git grep -n def-mstar1 origin/main` → 0 hits; working-tree recursive grep → 0 hits), and [`manuscript/ave-kb/common/vocabulary-register.md`](../manuscript/ave-kb/common/vocabulary-register.md) carries **no `m*` row at all** — so it is cited here by path only, with no line number, as the eventual home. The **live** corpus site for the `m*` tension is instead [`manuscript/ave-kb/common/translation-tables/translation-circuit.md`](../manuscript/ave-kb/common/translation-tables/translation-circuit.md):306, an **OPEN FLAG (flag-don't-fix — routed to Grant, NOT resolved)** recording that the corpus holds `m*` in tension (struck as SM-fitting-parameter in the vol-4 engineering chapters vs proposed as a substrate-native dispersion-read inertia to derive in its candidate-6). **This doc does not resolve that flag**; §2 is a scope statement about what the curvature read can measure, not an adjudication of whether `m*` is admissible vocabulary.

## 3 Where the sector signature DOES live — the cage resonance `ω_0`

The sector information that `ρ_eff(0)` throws away is the **pole location** of the same expression: the avoided-crossing / anti-resonance frequency

```
ω_0 ≈ π · c_sector / r_core
```

**Which sector's speed sets the cage's internal standing mode reveals which sector stores the trapped energy.** This is the only place in the metamaterial form where sector identity survives.

**Arithmetic** (re-derived here from the corpus speeds; see §8 for provenance). With `r_core ≈ 1.6` (the low end of the `r_core ≈ 1.6–2.2` band in [`2026-07-21_beta-tracking-feasibility_scoping.md`](2026-07-21_beta-tracking-feasibility_scoping.md) §2) and the lattice-measured cold speeds `c_P = 0.519`, `c_S = 0.286` (same §2, srs-z3 Bloch, grade-lock confirmed):

| sector | `c_sector` | `ω_0 = π·c_sector/r_core` |
|---|---|---|
| A1 compression | `0.519` | **`≈ 1.02`** |
| shear | `0.286` | **`≈ 0.56`** |

Separation factor `c_P/c_S = 1.81` — the two candidate resonances are **cleanly resolvable**, not a fine split needing a delicate lineshape fit.

**Why this read is α-clean and regime-portable.** The observable of record is the **dimensionless** ratio `ω_0 · r_core / c_P` (`≈ π` if A1 stores it, `≈ π/1.81 ≈ 1.73` if shear does). Per the α-circularity lesson, a chord — if any ever lands here — must be a dimensionless ratio; and **sector identity does not run with `r_core`**, so the read transfers across the lattice↔physical regime gap in a way a magnitude never would.

**Feasibility (favourable, and for a specific structural reason).** Two routes, both cheap:

1. **`L = 24–32` near-field BOUND-mode read.** The object is a *bound* cage mode, not a far-field radiated wave — so the `#775` radiative-sponge-vs-wavelength constraint does **not** bind. That constraint is what made the deep-quasistatic Lloyd tail infeasible on the lattice ([`research/2026-07-20_deep-rail-kscaling_derivation.md`](2026-07-20_deep-rail-kscaling_derivation.md) §2: the sponge "thickness must exceed the wavelength to absorb", forcing `k·r_core ~ O(1)`, and the `N>1` aggregation instrument needs `L ≳ O(10²–10³)`, "infeasible on this class of machine"). A near-field bound-mode read needs no giant sponge and no long-wavelength box.
2. **★Cheapest: an EIGENSOLVE of the caged sub-block.** *(Sizing and cost below are **extrapolated from the β-scoping cost table, not timed** — see §8.)* No time-domain drive at all — assemble the dynamical matrix over the cage neighbourhood, solve for the low-lying localized modes, read `ω_0` and the sector composition of each eigenvector. Seconds-to-minutes, not hours.

**★HONEST SCOPE LIMIT (the load-bearing fence).** This measures **which sector hosts the cage's stiffness/resonance mode** — it does **NOT** measure whether `E_trapped` converts to inertia at that rate. The `E = mc²` conversion is precisely the law the lossless small-displacement lattice **structurally lacks** ([`2026-07-21_beta-tracking-feasibility_scoping.md`](2026-07-21_beta-tracking-feasibility_scoping.md) §3, absence-1: node mass uniform and fixed, implicit `m = 1`, "trapped elastic energy carries zero inertia → `β_massload ≡ 0` analytically"). So the eigensolve is a **corroborating STRUCTURAL input** to the sector-of-storage question, not a magnitude measurement and not a closure of D1.

## 4 The virial consistency argument (the analytic lever)

This is the piece that changes D1's *shape*. It is an analytic argument, done on paper in the orchestration lane, re-checked here; it runs no code.

**Setup.** Treat the cage's trapped energy as a standing cavity mode of size `r_core` on some sector, at frequency `ω_0 = c_sector · k_mode` with `k_mode ≈ π/r_core`. For a standing elastic mode the virial theorem equipartitions kinetic and potential energy, so the total energy is set by the kinetic part:

```
E_trapped = ρ_0 · ω_0² · ⟨u²⟩ · V
```

Divide by that sector's own `c_sector²`, using `ω_0 = c_sector · k_mode`:

```
E_trapped / c_sector² = ρ_0 · k_mode² · ⟨u²⟩ · V
```

**The `c_sector²` cancels.** What is left — `ρ_0 · k_mode² · ⟨u²⟩ · V` — is a purely **geometric added mass**: it depends on the mode's wavenumber and amplitude and on the medium's bare density, and **not at all on any wave speed**.

**The consistency step.** Now impose the I5 import (`ρ_contribution = E_trapped/c² · participation`) as a density loading, and require it to equal the geometric added mass that the dressed dispersion **independently** fixes as `ρ_0 · θ · V` (the §2 static limit — the one thing the band-bottom read *does* measure). The two agree, with the `c_sector²` cancelling cleanly against the imported `c²`, **iff `c² = c_sector²`**. Any other choice leaves a dangling factor `(c_sector / c_chosen)²` — i.e. an added mass keyed to a channel the energy **is not stored in**, with no mechanism to supply the mismatch.

**⇒ D1 collapses from a free 3-way pick to a single physical question: WHICH SECTOR STORES `E_trapped`.** The `c²` is not an independent degree of freedom to be ruled on; it is entailed by the storage answer.

**Two honesty caveats — both load-bearing, state both:**

- **(i) The argument CONSUMES the I5 import; it does not certify it.** It assumes `E = mc²`-class trapped-energy inertia holds and asks only *which `c`*. Whether trapped energy carries inertia at all remains the tagged, un-derived import (charter §3, row **I5**: "★TAGGED IMPORT — NOT DERIVED") and the structurally-absent capability on the lattice (§3 fence above). This argument does not move that.
- **(ii) It is VACUOUS if "participation" is allowed to absorb a speed ratio.** The cancellation is exact only when `participation` is the pure kinematic **C-kin** fraction — the unconditional half of `clm-hu1jjw` ([`relative-offset-principle.md`](../manuscript/ave-kb/common/relative-offset-principle.md):39: "Trapped-energy patterns **participate in any carrier's oscillatory material motion** … It requires no sector ledger and is not conditioned on the open magnitude"). If instead `participation` is defined as a fitted coefficient free to carry a `(c_sector/c_chosen)²`, the dangling factor is simply reabsorbed and the argument constrains nothing. The argument's force is therefore conditional on holding `participation` kinematic by definition.

## 5 The Eötvös / MICROSCOPE external constraint

§4 reduces D1 to sector-of-storage. This section kills an entire *class* of answers to it before any measurement is taken.

**The mechanism.** Suppose inertia is **sector-split**: `m_i = Σ_sector E_sector / c_sector²`. Then `m_i` is **composition-dependent**, because different bodies store different fractions of their energy in different sectors (nuclear binding, EM binding, and rest energy do not sit in the same channel in the same proportions for titanium and platinum). If gravity meanwhile couples **sector-blind** (one universal gravitational charge), then `m_g/m_i` varies body-to-body — a direct Eötvös violation.

**The AVE sector spread is large, which makes the violation big rather than marginal.** Re-derived here:

```
c_P²/c_S² = (0.519/0.286)² = 3.29        →  a 229% spread between the two candidate divisors
```

**Order of magnitude.** With `Δ(m_g/m_i) ~ (c_P²/c_S² − 1) · Δf_sector = 2.29 · Δf_sector`:

| imbalance | `Δf_sector` | predicted `Δ(m_g/m_i)` | vs bound `~1e-15` |
|---|---|---|---|
| nuclear-binding *(Δf external, un-sourced — see §8)* | `~1e-3` | `~2e-3` | **~12 orders over** |
| EM-binding | `~1e-5` | `~2e-5` | **~10 orders over** |

The bound is the corpus's own imported WEP figure: **`WEP-CMRR ~1e-15` (Eötvös / MICROSCOPE)**, [`manuscript/ave-kb/common/translation-tables/translation-circuit.md`](../manuscript/ave-kb/common/translation-tables/translation-circuit.md):156 (also carried at [`research/2026-07-11_ep-cmrr-acceptance-test_prereg_FROZEN.md`](2026-07-11_ep-cmrr-acceptance-test_prereg_FROZEN.md):151).

**⇒ The branch "sector-split inertia WITH sector-blind gravity" is DECISIVELY DEAD.** Not marginal, not tension — 10–12 orders. No plausible refinement of the `Δf` estimates closes that.

**Two survivors, both legitimate:**

- **(a) Universality** — one effective conversion rate for all trapped energy, whatever its sector. Composition-independence by construction.
- **(b) A fully shared per-sector ledger** — each sector's trapped energy *gravitates* through the *same* `c_sector²` it *loads inertia* with, so the sector fractions cancel and `m_g/m_i = 1` body-by-body.

**★The corpus ALREADY DERIVES survivor (b)** — verified, quoted:

- [`manuscript/ave-kb/vol3/gravity/ch03-macroscopic-relativity/ponderomotive-equivalence.md`](../manuscript/ave-kb/vol3/gravity/ch03-macroscopic-relativity/ponderomotive-equivalence.md) (`clm-rd9cjm`), :12 — *"Standard physics invokes the Weak Equivalence Principle ($m_i = m_g$) as an axiomatic postulate. AVE derives it from macroscopic wave mechanics."* — and :30, the mechanism: *"Because the localised wave energy is defined by the particle's inductive inertia $m_i$, it cancels out of the acceleration equation ($F = ma$), guaranteeing that inertial mass and gravitational mass are identical ($m_i \equiv m_g$)."*
- [`research/2026-07-11_nordtvedt-eta_result.md`](2026-07-11_nordtvedt-eta_result.md):28–29 — *"η=0 is ENTAILED by the solver's single-`T₀₀^total` Gauss construction: the far-field gravitating charge IS the total-energy ledger by identity."* Its sector attribution is explicit at :71–73 — *"register-2 is the **radial/bulk ε₁₁ channel (A1-dilatation)** — the gravitational well's own strain energy. NOT cross-wired to shear/EM. Mass = A1-dilatation (PR#260/#311, untouched)."*
  - **Read the second cite honestly:** that solver installs a *single* ledger and therefore returns `η = 0` **by construction** — the same doc says so at :229–231 (*"the engine returns whatever ledger is installed; the test makes the installed ledger's Nordtvedt-status VISIBLE — it does not adjudicate whether one-ledger is physically correct"*). It is evidence that the corpus's installed ledger is the shared one, **not** independent proof that the shared ledger is right.

**Consensus-bias lens, applied explicitly.** A reflex reading would call a "the sector dependence cancels" argument an AVE excuse. Apply the symmetric standard: **GR passes Eötvös by construction via exactly this identity** — the equivalence principle is a *postulate* there, with the cancellation built into the geometry, and no one calls that an evasion. A shared-ledger cancellation that the framework *derives* rather than postulates is, if anything, on stronger footing than the consensus treatment. Survivor (b) is legitimate physics, not a rescue.

**What §5 does and does not do.** It is a **class-eliminator**: it removes sector-split-inertia-with-blind-gravity from the option set. It does **not** pick between (a) and (b), and it does **not** answer sector-of-storage — under survivor (b) *every* sector assignment passes Eötvös, so Eötvös carries no discriminating information about which sector stores `E_trapped`.

## 6 The upstream contradiction this exposes (the reason the walk exists)

§4 reduced D1 to sector-of-storage. Asking that question out loud immediately surfaces that **the corpus already answers it twice, incompatibly.** Both quoted verbatim, both two-method-verified at `c8ceacc3` (see §8).

**Site A — canon, Grant-ratified.** [`manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md`](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):20 —

> **🔴 TWO-"3"s DISAMBIGUATION (2026-06-10, Rule 12 — line above PRESERVED unedited; pre-adjudicated, Grant-ratified).** The phrase "the longitudinal re-engages at saturation = the electron" names the **A1 dilatation-MASS** "3" only — the Heaviside-excised longitudinal compression scalar (the A1 breather; `mₑc²` = trapped acoustic compression energy). It must **NOT** be conflated with the **second, orthogonal "3"**: the Cosserat **micro-rotation `(2,3)` WINDING** (T2 couple-stress, the Axiom-1 intrinsic-spin DOF; charge = Beltrami helicity `H_bel = ∫ω·(∇×ω)`).

**Site B — the proposed relative-offset leaf.** [`manuscript/ave-kb/common/relative-offset-principle.md`](../manuscript/ave-kb/common/relative-offset-principle.md):49, the body of `clm-m5swh9` —

> - **The effective inertia per pattern is EMERGENT field momentum and SECTOR-CROSSED.** The trapped energy is `T2`/swing-class energy sitting inside the `A1` compression carrier's budget; **which sector's `c²` divides `E`** to give the loaded inertia is **not automatic**.

**These cannot both name the store — with one important caveat the canon line itself supplies.** `master-equation.md:20` closes: *"The electron is the unknot dilatation-mass **carrying** the `(2,3)` winding — two objects, not one."* That clause is the on-line seed of exactly the DECOMPOSITION §6's honest remainder reaches by the independent AC/DC route: canon already says the electron is two objects, so the live question may be how `mₑc²` divides between them rather than which one wins outright. Site A says the trapped store IS A1 compression energy (`mₑc²` = trapped acoustic compression energy). Site B says the trapped energy is `T2`/swing-class *sitting inside* A1's budget — i.e. stored on T2, merely bookkept against A1. If Site A is right, D1's answer is `c_P` and the "sector-crossed" framing of I8 is misdescribed at the root; if Site B is right, the store is T2 and the §4 lever points elsewhere.

**Provenance, recorded honestly (this is the load-bearing part).** *(The propagation is **near-verbatim**, not verbatim: the leaf inserts "energy", re-punctuates `, and` → `;`, and splits the parenthetical into a following sentence.)* The **T2 label entered via the orchestrator's Fork-ρ walk framing** — it appears first at [`research/2026-07-21_fork-rho-walk_RECORD.md`](2026-07-21_fork-rho-walk_RECORD.md):55 (*"the trapped energy is `T2`/swing-class sitting inside the `A1` compression carrier's budget"*) and propagates from there into the leaf at :49 near-verbatim. The leaf itself is stamped *"⚠ STATUS: PROPOSED — Grant-ratification-at-merge"* at :11, and its magnitude node `clm-m5swh9` is `*pending*`/OPEN. The **A1 statement is older, and Grant-ratified canon** (2026-06-10, pre-adjudicated).

**★A sharper flag inside the provenance:** the walk record's own sentence **cites `master-equation.md:20`** — it invokes the canon line for the `A1 ⊥ T2` orthogonality *while assigning the store to T2*, which is what that same line assigns to A1. The **observable** fact, stated without any claim about a prior author's reading process: the cite is **bound to the orthogonality clause**, and the same line's **storage assignment is not engaged**. ★**Three instances of the same pattern, not two** — the third is [`relative-offset-principle.md`](../manuscript/ave-kb/common/relative-offset-principle.md):41, which likewise writes "nonzero acoustic inertia per unit sector-crossed trapped-`T2` energy" while citing `master-equation.md:20` for `A1 ⊥ T2`. ★**Self-evidencing corroboration:** leaf:49's own bullet juxtaposes BOTH assignments internally — "the trapped energy is `T2`/swing-class energy…" and, two clauses later, "mass is `A1` dilatation" — and that second clause is **not** in RECORD:55; it was added at the leaf. The flag therefore stands on the text alone.

**Status: OPEN — Grant is walking it.** *(Routing-cite caveat: the orchestration lane refers to this as "pending-rulings item 13". That item is **NOT on `main`** at `c8ceacc3` — [`_orchestration/2026-07-20_pending-rulings-and-frontier-queue.md`](../_orchestration/2026-07-20_pending-rulings-and-frontier-queue.md) §1 currently ends at item 12. It is therefore the **next unlanded §1 slot**, not a citable line; recorded that way deliberately rather than repeated as if it resolved.)*

**Grant's in-chat framing, verbatim `[sic]`:**

> "is this just ac vs dc analysis?"

**The orchestration-lane response to it — ⚠ ORCHESTRATION-LANE, NOT RATIFIED, NOT REVIEWED. This is the walk's current position, not a result.** The AC/DC carve ([`manuscript/ave-kb/common/form-deriving-value-importing.md`](../manuscript/ave-kb/common/form-deriving-value-importing.md) §"The AC/DC carve", `clm-acdc07`) reframes the contradiction rather than adjudicating it:

- **The store is the oscillating DOF — stated substrate-natively (2026-07-28 leak-audit fold; the earlier phrasing premised this step on `mₑc² = ℏω_Compton`, a quantum relation the argument does not need).** Canon independently assigns the oscillation: `master-equation.md:20` names the **A1 breather** as the rest-energy store ("trapped acoustic compression energy"), and the corpus's own resonant-LC-tank identification puts that breather's swing at the Compton frequency. The store is therefore the **dynamical, oscillating** DOF on canon's own assignments — no quantum import required. *(Consistency note, not a premise: this is consistent with `E = ℏω` read at the Compton frequency.)*
- The `(2,3)` winding is a **STATIC Link texture** — DC by construction. Per [`manuscript/ave-kb/common/saturation-rim-inversion.md`](../manuscript/ave-kb/common/saturation-rim-inversion.md):43: *"Charge is the **STATIC imposed Link** — `charge = Link(∂Ω, F)` STANDS per the Grant-ratified **#416 two-natured ruling** … the electron is two-natured — a DYNAMICAL energy-bound A1 mass + a STATIC topological `(2,3)`-Clifford-winding charge"*.
- If the store is the AC oscillation and the T2 object is DC texture, the **oscillation store sits in A1** — which would make `c² = c_P²` **consistency-forced** via §4, and would mean Site B's "T2/swing-class" label mis-assigns a static texture to a dynamical store.

**Honest remainder (do not let the above run away with it).** A **static Cosserat twist still carries elastic energy.** "DC" does not mean "zero energy" — a pre-strained spring stores energy without oscillating. So the fully honest form of the resolution may not be a sweep at all but a **DECOMPOSITION**:

```
E_rest = E_AC(oscillation store)  ⊕  E_DC(static texture self-energy)
```

with the sector assignment differing between the two terms. That decomposition is **measurable in principle by the §3 eigensolve** — the eigenvector's sector composition at `ω_0` reads the AC term's host directly, and a static-relaxation energy read on the same sub-block reads the DC term. That is a concrete follow-on, not a claim.

## 7 Bottom line + routing

**(a) What CLOSES D1: nothing on the lattice.** No driver, no eigensolve, and no continuum solver closes it, because the residual question is *which sector stores the trapped energy* and the corpus answers that in two incompatible places (§6). The **§4 consistency argument closes D1's STRUCTURE** — it converts a free 3-way pick (`c_P` / `c_S` / `c_EM`) into a single entailed consequence of the storage answer. The storage answer itself is a **corpus adjudication** (Grant), not a measurement.

**(b) What CONSTRAINS it.** Two things, neither of which closes it:

- **§5 Eötvös/MICROSCOPE — a CLASS-ELIMINATOR.** Kills sector-split-inertia-with-sector-blind-gravity outright (10–12 orders). Leaves universality and the shared per-sector ledger, and carries **no** discriminating information between sector assignments (under a shared ledger they all pass).
- **§3 eigensolve — a CORROBORATING STRUCTURAL READ.** Cheap (`L = 24–32`, or a sub-block eigensolve in minutes), α-clean (a dimensionless `ω_0·r_core/c_P`), and cleanly resolvable (`1.81×` separation). It reads which sector hosts the cage's stiffness mode — **not** whether `E_trapped` converts to inertia at that rate.

**(c) DECORATION: the literal `m*`-from-curvature read (§2).** Real number, wrong question — the band-bottom limit is sector-blind. Must not be headlined as answering D1.

**Best-plausible outcome.** Grant rules the store is the A1 breather (Site A, ratified canon); §4 then forces `c² = c_P²`; the §3 eigensolve independently returns `ω_0·r_core/c_P ≈ π` with an A1-dominant eigenvector; charter D1 closes as *entailed-not-picked*, with the I8 row rewritten from "open 3-way choice" to "consequence of the storage ruling", and `clm-m5swh9`'s sector-crossed clause retires while its magnitude stays open.

**Honest-most-likely outcome.** The §6 remainder bites: the rest-energy budget is a **decomposition** (AC oscillation store ⊕ static-texture self-energy), the two terms sit on different sectors, and D1 does not resolve to a single `c²` at all — it resolves to a two-term ledger whose *weights* are a new open magnitude. In that case §4's clean cancellation applies term-by-term rather than globally, and the practical output is a *sharper statement of the open question*, not a closure. This is the outcome to plan the charter around.

**Routing (nothing fires without Grant's word):**

| item | owner | state |
|---|---|---|
| The §6 sector-of-storage contradiction (Site A canon vs Site B walk-label) | **Grant** | OPEN — walking; the next unlanded `_orchestration/2026-07-20_pending-rulings-and-frontier-queue.md` §1 slot (see §6 caveat: §1 ends at item 12 on `main`) |
| The §3 caged sub-block eigensolve (`ω_0` + eigenvector sector composition) | implementer lane | **FIREABLE on his word** — scoped, cheap, structural-read-only; would need its own prereg |
| Charter **D1** (`2026-07-21_continuum-radial-solver_CHARTER.md` §0 / I8) | charter lane | **HELD** — build stays blocked; this doc supplies its evidence basis, not its ruling |

## 8 Cite ledger + number provenance (the checkability receipt)

The whole point of banking this doc is that chat-only claims become checkable. So: every corpus cite above was verified **two-method** at `origin/main` @ `c8ceacc3` — method 1 `git grep -n <pattern> origin/main`, method 2 `grep -n` on the checked-out worktree file (line numbers read from method 2, content compared byte-wise between the two).

**Cites that RESOLVED (verified, quotable):**

| cite | what it carries |
|---|---|
| `research/2026-07-21_continuum-radial-solver_CHARTER.md` §0 D1 / §3 I5–I8 | the question; the tagged-import ledger |
| `manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md`:20 | §6 Site A (canon, Grant-ratified) |
| `manuscript/ave-kb/common/relative-offset-principle.md`:11, :39, :41, :49 | leaf PROPOSED stamp; C-kin unconditional; C-load conditional + `1 + β·φ`; §6 Site B |
| `manuscript/ave-kb/vol3/gravity/ch03-macroscopic-relativity/ponderomotive-equivalence.md`:12, :30 (`clm-rd9cjm`) | the `m_i` cancels in `F=ma` ⇒ `m_i ≡ m_g` derivation |
| `research/2026-07-11_nordtvedt-eta_result.md`:28–29, :71–73, :229–231 | single-`T₀₀^total` ledger / η=0 entailment; A1-dilatation gravitating charge; the install-tautology caveat |
| `manuscript/ave-kb/common/translation-tables/translation-circuit.md`:156 | `WEP-CMRR ~1e-15` (Eötvös / MICROSCOPE) |
| `manuscript/ave-kb/common/translation-tables/translation-circuit.md`:306 | the live OPEN FLAG on `m*` (routed to Grant, unresolved) |
| `manuscript/ave-kb/common/saturation-rim-inversion.md`:43 | `(2,3)` = STATIC imposed Link, #416 two-natured ruling |
| `manuscript/ave-kb/common/form-deriving-value-importing.md` §"The AC/DC carve" (`clm-acdc07`) | the AC/DC carve |
| `research/2026-07-21_fork-rho-walk_RECORD.md`:55 | the T2/swing-class label's point of entry (§6 provenance) |
| `research/2026-07-21_beta-tracking-feasibility_scoping.md` §2, §3 | `c_P`/`c_S`/`r_core`; the three structural absences |
| `research/2026-07-20_deep-rail-kscaling_derivation.md` §2 | the `#775` sponge-vs-wavelength infeasibility (contrast for §3) |
| `research/2026-07-11_ep-cmrr-acceptance-test_prereg_FROZEN.md`:151 | second site for the WEP bound |

**Cites that FAILED verification — recorded, and NOT repeated as resolved:**

1. **`def-mstar1`** — **NOT on `main`** @ `c8ceacc3`. Two-method: `git grep -n "def-mstar1" origin/main` → 0 hits; recursive working-tree grep → 0 hits. Additionally `manuscript/ave-kb/common/vocabulary-register.md` carries **no `m*` row at all**. Handled in §2 by citing the vocabulary-register **by path with no line number** (as the eventual home) and pointing at the live flag site `translation-circuit.md`:306 instead.
2. **"pending-rulings item 13"** — **NOT on `main`** @ `c8ceacc3`. `_orchestration/2026-07-20_pending-rulings-and-frontier-queue.md` §1 runs items 1–12 and stops; `grep -rn "item 13"` across `_orchestration/` + `research/` returns only an unrelated hit (`research/2026-07-08_chiral-drive-selforbit_result.md`:122, a different lane's RETURN item). Handled in §6/§7 as "the next unlanded §1 slot", never as a citable anchor.

**Numbers — RE-DERIVED in this doc** (computed here from the cited inputs, not carried):

| quantity | value | from |
|---|---|---|
| `c_P/c_S` | `1.8147` (→ `1.81`) | `0.519 / 0.286` — ⚑ the cited source prints `1.813` (`research/2026-07-21_beta-tracking-feasibility_scoping.md`:11), which is off in the 4th figure; `1.8147` is the arithmetically correct value from the same inputs. Flagged so a reader comparing the two does not read this as a mis-copy. |
| `ω_0^A1 = π·c_P/r_core` | `1.0191` (→ `≈ 1.02`) | `r_core = 1.6` |
| `ω_0^S = π·c_S/r_core` | `0.5616` (→ `≈ 0.56`) | `r_core = 1.6` |
| `ω_0^A1/ω_0^S` | `1.8147` — identical to `c_P/c_S` (as it must be; `r_core` cancels) | — |
| `c_P²/c_S²` | `3.2931` (→ `3.29`) | — |
| sector spread | `229.3%` | `(c_P²/c_S² − 1)·100` |
| `Δ(m_g/m_i)`, nuclear (`Δf ~ 1e-3`) | `2.29e-3` → `12.4` orders above `1e-15` | `2.293 · Δf` |
| `Δ(m_g/m_i)`, EM (`Δf ~ 1e-5`) | `2.29e-5` → `10.4` orders above `1e-15` | `2.293 · Δf` |

**Numbers — CARRIED from the orchestration lane** (stated there, not re-measured here; each would need its own driver/prereg to bank):

- `r_core ≈ 1.6` as the working core radius — *bounded* by the cited `1.6–2.2` band in the β-scoping doc, but the specific choice is the orchestration lane's.
- `Δf_sector ~ 1e-3` (nuclear-binding) and `~1e-5` (EM-binding) energy-fraction imbalances — standard order-of-magnitude figures, **external/textbook**, not corpus-derived and not re-checked against a source here. They set the §5 headline exponents, so they are the §5 argument's softest input; the conclusion survives them being wrong by two orders in either direction.
- The `L = 24–32` near-field feasibility sizing and the "seconds-to-minutes" eigensolve cost — extrapolated from the β-scoping §2 cost table (L24 → 111k nodes @ 12 ms/step; L32 → 262k @ 26 ms), **not** timed on a real eigensolve of the caged sub-block.
- `ρ_eff(ω) = ρ_0[1 + θ·ω_0²/(ω_0²−ω²)]` — the locally-resonant metamaterial form, an **external import** (the standard Liu/Sheng-class result; the corpus's own nearest reference is the `Milton–Willis 2007` mention at `manuscript/ave-kb/common/physics-lineage-map.md`:488, which is a lineage note, not a derivation). Its `ω→0` limit and the pole-carries-the-sector observation are re-derived here from the form; the **form itself is imported**.
- The §4 virial argument — algebra done in the orchestration lane, re-checked line-by-line here; it is analytic, not numeric, so there is nothing to re-measure. Its two caveats (§4 i/ii) are the honest fences.

**What this doc mints: nothing.** No `clm-`, no `def-`, no verdict, no ruling, no status flip on any existing node. It changes no engine byte and runs no driver. It is a citation basis for a Grant adjudication that has not happened.
