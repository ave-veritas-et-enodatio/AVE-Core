# Noise-Floor Arrow — Walk-Record (the ruling arc, the lowpass framing, the scope fences)

**Date:** 2026-07-19
**Class:** WALK-RECORD (Grant rulings + orchestrator walk; **the arm adjudicates; NOTHING here is new canon**)
**Provenance:** in-chat walk (Grant, 2026-07-19) + orchestrator walk (this session). This is the record of the **owed F6 design-walk** that the counting-arrow arc left open — the one flagged *"Design-walk OWED with Grant"* in the F6-arc closure record (engine-capability-map §8c.9, presently on the unmerged #728 branch `docs/tier1-kb-debt-batch`; see the KB-pointer section below).
**★ NOTHING here is new canon.** The three Grant rulings are recorded verbatim (with `[sic]` where transcribed as typed). Everything else is either **orchestrator-walk** (tagged as such and demoted to candidate-framing where it has no canonical home) or a **citation of an already-canonical leaf** (tagged adjudicated-canon). The **thermal-floor arm** (in flight, sibling lane) is what turns any of this into a testable result; **this doc originates no result and mints no `clm-`.** All file:line citations re-verified at HEAD (`6ff138b5`) before this record was frozen.

**★ ATTRIBUTION KEY (load-bearing — the #723/#728 lesson).** Every step below carries one of three tags:
- **[Grant-verbatim]** — Grant's own words, transcribed exactly (typos preserved, `[sic]`).
- **[orchestrator-walk]** — the orchestrator's reasoning in this session. Ratified-by-Grant where a verbatim ratification quote is recorded; otherwise candidate-framing.
- **[adjudicated-canon]** — a citation of an existing canonical leaf, re-verified at HEAD.

No orchestrator-walk sentence is tagged Grant-verbatim, and no Grant quote is paraphrased into canon.

**Sector / regime / phase-state declaration.** MODE: an ensemble of bound soliton LC tanks (clocks) coupling **locally** into a pre-occupied traveling bath (the noise floor). REGIME: sub-yield, lossless-reactive (Axiom 3) — the floor scrambles *phase*, not amplitude past the wall. PHASE-STATE: coherent-bound (solitons) + coherent-propagating (radiation) + **incoherent-propagating (the floor / heat register)**. SECTOR: A-class continuous coupling into the T2 entropic register — **not** A1 dilatation-mass, **not** Cosserat-winding genesis.

---

## §1 — THE ARC (chronological, each step attributed)

### (a) The static/dynamic conflation question

**[Grant-verbatim]** `[sic]`:

> "are we just cinflating the static picture with the diynamic effects, like exponential lattice node genesis?"

**[orchestrator-walk] — the walk answer.** The question puts two pictures side by side and asks whether the counting-arrow arm had been running them together:

- **The static, fixed-seat picture.** A fixed set of bath modes (fixed number of "seats"); the soliton's coherent structure spreads across them and — over a finite window — does not reconverge. The arrow here is *counting over a fixed mode set* (the mode-count-door discriminator, §4 anchor 3).
- **The growing-lattice picture.** New lattice nodes are minted (the "exponential node genesis" Grant names) — a **growing sink**. Here the arrow would be sourced by the *growth* of phase-space volume, not merely by spreading across a fixed set.
- **The growing-sink reframe.** These are physically different arrow-sources. If the sink is *growing*, the natural rate form is the crystallization-frontier expulsion rate — canonically `Γ = 3Hρ_latent` (adjudicated-canon: `manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/dark-energy-latent-heat-definition.md:30`, the "horizon crystallization **frontier** (rate Γ = 3Hρ_latent)"; the *form* is FORCED-by-continuity, the *rate* ASSERTED, `:121`).
- **The instrument option that would follow.** A growing-sink picture would demand a **growing-comb instrument** (option C) — a bath whose mode count increases during the run — rather than the fixed-comb sweep the certified meter runs. That option was on the table when Grant's ruling (b) landed.

The honest reading of the conflation question: the two arrow-sources had **not** been cleanly separated, and (b) resolves which one couples *locally*.

### (b) ★ THE RULING — the T2 sink couples locally as a static pre-occupied noise floor

**[Grant-verbatim]** `[sic]`:

> "my gut says its couples through a static noise floor"

and:

> "so wffectively constant"

**[orchestrator-walk] — reading of the ruling.** The T2 entropic sink couples to the local soliton dynamics **as a static, pre-occupied noise floor** — a background that is *already there*, at an effectively constant level, not one that is being minted mode-by-mode as the soliton radiates into it. Locally, the sink is a **standing floor the soliton rides on**, not a growing set of fresh empty seats.

**[adjudicated-canon] — the canonical anchor for a static vacuum noise floor.** This is exactly the **Johnson-Nyquist vacuum thermal-noise-floor** row in the circuit translation table:

> `manuscript/ave-kb/common/translation-tables/translation-circuit.md:151` (§4 catalog, header at `:91`):
> "**Vacuum thermal noise floor** | Johnson-Nyquist thermal noise at vacuum baseline (`$k_B T_{CMB}$` per mode per Hz)"

(the same row appears as the numbered catalog entry #22 at `:349` and as the Johnson-Nyquist formula row `$v_n^2 = 4 k_B T R \Delta f$` at `:546`). This is a **static, pre-occupied** floor: `k_B T_{CMB}` of strain-noise per mode per Hz, standing at the vacuum baseline. Grant's "static noise floor / effectively constant" ruling **maps the T2 local coupling onto this existing canonical row** — it does not mint a new object.

### (c) THE REFRAME CASCADE (orchestrator-walk; Grant-ratified)

**[Grant-verbatim] ratification of the whole cascade** `[sic]`:

> "word, that picture makes perfect sense to me"

Everything in this subsection is **[orchestrator-walk]**, ratified by that quote; the individual mechanisms are candidate-framing where they have no canonical home, and each is what the **arm** (not this doc) adjudicates.

**(i) The full-discharge pathology was bath EMPTINESS, not head-count.** The #726/#727 instrument-incompatibility (no cell reaches the quasi-continuum without full discharge) was read, at the time, as a *mode-count* problem. Under the static-floor picture it is instead a **bath-emptiness** problem: a **cold comb** initialized at `x=p=0` is a *drain* — the cavity discharges into an empty bath all the way to zero, and the "no cell avoids full discharge" wall follows. A **pre-occupied floor** changes the endpoint: the cavity relaxes **to the floor**, not to zero. The over-extraction **clamp** (the hard-zero absorbing state that terminated the #726 runs) then becomes **moot** — there is no full discharge to clamp, because the floor sets a non-zero relaxation target.

**(ii) The cold-comb recurrences were a coherent-initial-condition artifact — and this locates the local arrow.** The recurrences the cold comb showed (the #726 dips, §2) are **guaranteed by the coherent, zero-phase initial condition the instrument imposed**: a comb started at `x=p=0` is maximally phase-coherent, so it *must* re-phase (Poincaré-recurrent, adjudicated-canon `thermal-phase-registers.md:25`). A **random-phase floor never re-phases** — there is no coherent initial condition to return to. Therefore:

> **★ THE LOCAL ARROW = coherent returns dephasing into the pre-occupied random background** — irreversibility **by counting over the floor's random phases**, and it is **static** (it needs no growing sink, no minted modes, no valve). This is the retention/transition split's *counting-only* license discharged against a random floor (adjudicated-canon `retention-transition-split.md:31` "an arrow at the TRANSITION moment is admissible **only** from counting"; `:36` "the arrow comes from **mode-count or a click, never a valve**").

**(iii) The floor = the missing FLUCTUATION half of the FD pair.** The certified two-tank transduction result measured the **dissipation half** of a fluctuation-dissipation pair — "heat = reversible phase-scramble, not loss" (adjudicated-canon `thermal-phase-registers.md:25`, the Ax3-derived + PR #707-corroborated line). The static noise floor is the **fluctuation half** that was missing: the standing `k_B T_{CMB}` background against which the dissipation is defined. This routes to two open items, **not resolved here**: the **ℏ-as-FD-constant** open (UNBANKED — the FD constant's *form* was not derived; `mode-count-door_CHARTER.md:27`) and the **entropy definition** (still PROPOSED — `thermal-phase-registers.md:29,:42`).

**(iv) Growth / node-genesis re-homed to the cosmological rate rung; the DOS-balance A/B fork MOOT.** The "exponential node genesis" from question (a) does not vanish — it **re-homes** to the cosmological rate rung, where the frontier grows at `Γ = 3Hρ_latent` (adjudicated-canon `manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/dark-energy-latent-heat-definition.md:30,:121`). Locally, `H` is invisible (the Hubble rate is unmeasurable at the bench scale), so the growth term drops out of the local coupling — consistent with (b)'s "effectively constant." A direct consequence: the **DOS-balance A/B fork** that the F6-arc closure recorded as the *recommended direction* (engine-capability-map §8c.8, RULING 22, on the #728 branch) is **MOOT** under the static-floor reframe — the local arrow no longer turns on balancing bath-DOS against lattice-DOS; it turns on dephasing against a standing random floor. *(This is the update the design-walk owed; the arm/auditor lands it in §8c on the merged branch — see the KB-pointer section. This doc only records that the fork went moot.)*

**(v) Floor PROVENANCE is explicitly upstream, out of the arm's scope.** *Why* the floor sits at its level, and *why* its phases are random (the level + the randomness) is a **provenance** question — the AVE analog of the **past-hypothesis** (why the universe started in a low-entropy, phase-organized state). The **named candidate** for the provenance is the **crystallization frontier** (adjudicated-canon `manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/dark-energy-latent-heat-definition.md:30`, the horizon crystallization frontier). This is **explicitly upstream and out of the arm's scope**: the arm tests whether a static floor *sets the local arrow*, taking the floor's level + randomness as given; it does not derive them.

### (d) THE HYPOTHESIS QUESTION — "would the noise floor set the arrow of time?"

**[Grant-verbatim]** `[sic]`:

> "word, that picture makes perfect sense to me, and the noise floor woild set the arrow of time right?"

**[orchestrator-walk] — the honest scoping answer (recorded as given).**

- **YES — as a hypothesis under test.** The static noise floor setting the local arrow is a **hypothesis the thermal-floor arm adjudicates**, not a banked result. The arm's **revival-vs-ρ kill-shape** (§2) is what decides it: revivals present at `ρ=0`, suppressed as the floor is populated. Until that fires, the answer is *YES-as-hypothesis-under-test*, not YES-as-fact.
- **Even if confirmed, it is the LOCAL-mechanism rung only.** A confirming kill-shape would establish the *local mechanism* (dephasing-against-a-random-floor sets the bench-scale arrow). It would **not** by itself supply the floor's provenance — the level + randomness stay upstream (c-v), the past-hypothesis analog unresolved.
- **The rung ceiling.** So the confirmable claim is bounded: *local mechanism*, provenance upstream, cosmological growth re-homed to `Γ=3Hρ_latent` (c-iv). Nothing here reaches emergence-class, and nothing reaches "AVE derives the arrow of time" — it reaches "AVE has a candidate local mechanism for it, testable by the arm."

### (e) ★ THE LOWPASS FRAMING — "a frequency shift toward a baseline lowpass filter?"

**[Grant-verbatim]** `[sic]`:

> "and that direction is a frequency shift toward a baseline lowpass filter?"

**[orchestrator-walk] — adjudication of this framing (walk-level, labeled).** The floor interface acts as a **one-way lowpass for coherence**:

- **Amount / envelope (DC / slow) passes both ways.** The certified transduction is an **amount channel** that returns energy — demonstrated (adjudicated-canon `f6-certified-kappa-sweep_result.md` R-1/R-3: the amount channel *did* deliver recurrence-timed returns). So the slowly-varying envelope / amount passes through the interface in both directions.
- **Carrier-phase (fast / coherent structure) passes IN but not OUT.** Coherent carrier structure can enter the floor, but it does **not** come back out coherently — it is dephased against the floor's random phases (c-ii). So the retrievable coherent structure only decays.
- **⇒ The arrow = iterated lowpass on retrievable structure.** Each interaction passes amount both ways but strips a little more retrievable carrier-phase, so everything relaxes toward the baseline. The lowpass picture is **correct as the coherence / observable transfer-function statement**: the floor is a one-way lowpass on *retrievable coherence*, and the baseline it relaxes toward is the floor itself.

**★ PRECISION NOTE (mandatory, honest — linear vs nonlinear).** In the **linear** engine, per-mode energies do **not** literally shift frequency. What decays is the **cross-mode phase correlation** — which is *exactly* the banked two-tank result "heat = reversible phase-scramble" (adjudicated-canon `thermal-phase-registers.md:25`: the isolated Op14 differential phase is **bounded / reversible dephasing**, a scramble of the phase relationship, not a spectral downshift of any single mode). To an **envelope detector** this *looks like* power draining from the carrier line into the broadband baseline — so the lowpass picture reads true observationally. But **literal spectral downconversion** (power actually moving to a different frequency) requires the **nonlinear channel** — the measured **op3-grade self-generated harmonics** (adjudicated-canon `f6-meter-nonlinear-reval_result.md:69–74`, W4: 10 occupied bath modes, 5 of them at self-generated harmonics `n·ω_d`, `ω_d=0.524`; the 2nd harmonic `2·ω_d=1.048` measured at `ω=1.05`). So:

> **The lowpass picture is CORRECT as the coherence / observable transfer-function statement, and needs the linear-vs-nonlinear precision the moment it enters any derivation:** *linear* = cross-mode phase decorrelation that *looks like* a downshift to an envelope detector; *nonlinear (op3)* = genuine spectral content moved to `n·ω_d`. Conflating the two would overclaim a literal frequency shift the linear engine does not produce.

**Status of the lowpass framing:** **Grant-proposed** (the question above) / **orchestrator-adjudicated** (this subsection) / **arm-testable** — a candidate **secondary observable** for the arm is the **coherent-vs-envelope return split** (does amount return while coherent structure does not?), which is precisely the transfer-function asymmetry named here.

---

## §2 — Instrument implication (the thermal-floor arm, in flight)

**[orchestrator-walk] — what the ruling arc demands of the instrument.** The static-floor picture turns the abstract counting-arrow question into a concrete, falsifiable instrument: the **thermal-floor arm**.

- **In-flight, sibling lane.** The arm is being built concurrently on branch `feat/f6-thermal-floor-arm` (its **§D floor-battery**, its prereg, and its docket entries). **This walk-record does not duplicate that content** — it is the WALK/CONTEXT record and cross-references the arm as in-flight. *(The arm lane runs concurrently (branch `feat/f6-thermal-floor-arm`, pushed to origin during this doc's build). The docket-tail collision expected between this doc's continuation block and the arm lane's is anticipated and normal — see D3.)*
- **The §D floor-battery need.** The arm requires a validated way to *place* a pre-occupied random-phase floor at a controlled density `ρ` — the "floor-battery" — analogous to the meter's certified band-placement (`_place_detuned_band`), but now the floor is a **feature under test**, not a control. This is the sibling lane's deliverable.
- **The revival-vs-ρ kill-shape.** The discriminating observable is the **suppression of coherent revivals as a function of floor density `ρ`**: revivals present at `ρ=0`, monotonically suppressed as `ρ` rises (the coherent returns dephasing into the floor, §1c-ii). A revival-vs-ρ curve that suppresses is the mechanism's signature; one that does not is its falsifier.
- **The `ρ=0` positive control = the #726 dips (banked numbers).** At `ρ=0` (cold comb, no floor) the arm must reproduce the recurrence-timed returns already banked in the certified-κ sweep (adjudicated-canon `f6-certified-kappa-sweep_result.md`, R-1/R-3): the densest comb's `E_bath` **dips at each recurrence** — **14.9% returned at `x≈1.3` (1st recurrence), growing to 35.5% at `x≈2.46` (2nd recurrence)** — onsets locked to `k·T_rec`, growing per recurrence, and **not a transfer artifact** (`t63/T_rec = 0.193`; the transfer is **5.2× faster** than the `~T_rec` dip spacing). These banked dips are the `ρ=0` positive control the arm rides on.
- **★ The arm's frozen classes include NO-SUPPRESSION (ride-on-top) as the live falsifier.** Among the arm's frozen outcome bins (sibling-lane content) is **NO-SUPPRESSION**: the floor rides *on top* of the dynamics without dephasing the revivals — the revival-vs-ρ curve stays flat. That class is the **live falsifier** of the static-floor arrow: if a populated floor does not suppress coherent returns, the "dephasing-against-a-random-floor sets the arrow" mechanism is dead, and honest closure (Rule 11) applies. *(The bin definitions are the arm lane's to freeze; recorded here only as the falsification shape this walk implies.)*

---

## §3 — Scope fences

**[orchestrator-walk]** — the boundaries the ruling arc must not be read past. Each fence is what keeps the claim honest.

| Fence | What is IN | What is OUT / elsewhere |
|---|---|---|
| **Rung** | the **local-mechanism rung ONLY** — a candidate bench-scale mechanism (dephasing against a static random floor) that the arm can test | any "AVE derives the arrow of time" reading; nothing here reaches emergence-class |
| **Provenance** | taking the floor's **level + randomness as given** | the floor's *provenance* (why that level, why random) is **upstream** — the past-hypothesis analog; named candidate = the **crystallization frontier** (`manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/dark-energy-latent-heat-definition.md:30`) |
| **Cosmological rate** | the **local** coupling is effectively constant (`H` invisible locally) | the **growth / node-genesis** term re-homes to the cosmological rate rung, `Γ = 3Hρ_latent` (`manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/dark-energy-latent-heat-definition.md:30,:121`) — a **separate** rung |
| **Reversibility** | irreversibility is **window-relative**: a coherent return that does not reconverge *within the observation window* reads as the arrow | this is **Poincaré window-relativity, retained** — the two-tank result found the isolated dephasing **Poincaré-recurrent / bounded** (`thermal-phase-registers.md:25`); the arrow is a window-vs-recurrence statement, not an absolute one |
| **FORM / VALUE** | the **suppression FORM** (revival-vs-ρ kill-shape) is the claim under test | the **floor level** is a calibrated / imported value (the `k_B T_{CMB}` baseline, `translation-circuit.md:151`), not an emergence |
| **DOS-balance fork** | the local arrow turns on **dephasing against a standing random floor** | the DOS-balance A/B fork (the prior *recommended direction*, §8c.8 on #728) is **MOOT** under the static-floor reframe (§1c-iv) |

---

## §4 — Canon anchors (each verified at HEAD `6ff138b5`)

Every anchor below was re-verified in the worktree at HEAD before this record was frozen (verify-before-cite). **[adjudicated-canon]** throughout.

| # | Anchor | File:line (HEAD `6ff138b5`) | Load in this record |
|---|---|---|---|
| 1 | **Johnson-Nyquist vacuum thermal-noise-floor row** | `manuscript/ave-kb/common/translation-tables/translation-circuit.md:151` (§4, header `:91`); also catalog #22 `:349`; formula row `:546` | the canonical home of Grant's "static noise floor / effectively constant" ruling (§1b) — a pre-occupied `k_B T_{CMB}`-per-mode-per-Hz floor |
| 2 | **Two-tank "heat = reversible phase-scramble" result** | `manuscript/ave-kb/common/thermal-phase-registers.md:25` (Ax3-derived + PR #707-corroborated; §1 header `:16`); source `research/2026-07-15_two-tank-decoherence-check_NOTE.md` §4 | the **dissipation half** of the FD pair (§1c-iii); the **Poincaré-recurrent / bounded** dephasing that fixes the linear-vs-nonlinear precision (§1e); the window-relativity fence (§3) |
| 3 | **Mode-count door charter's counting-arrow question** | `research/2026-07-15_f6-mode-count-door_CHARTER.md:13` (the §0 discriminator) | the arrow-source the static-floor picture resolves *locally* (§1a): "*Can a bounded, energy-conserving, in-Hamiltonian ε→T2 transfer produce irreversibility from bath mode-count / phase-space volume increase, without importing sub-yield friction?*" |
| 4 | **Retention/transition split — the arrow-from-counting license** | `manuscript/ave-kb/common/retention-transition-split.md:31` ("admissible **only** from counting"); `:36` ("mode-count or a click, never a valve") | licenses the **static** local arrow (counting over the floor's random phases, §1c-ii) — no valve, no `Re(Z)` friction |
| 5 | **Dark-energy latent-heat definition — the arrow rows** | `manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/dark-energy-latent-heat-definition.md:77` (§3 "arrow of time = the T2 entropic sink, NOT chirality"); `:102–103,:125` (arrow **ASSERTED**, imported cross-chapter); `:30,:121` (`Γ = 3Hρ_latent`, crystallization frontier) | the cosmological rate rung (§1c-iv, §3) + the crystallization-frontier provenance candidate (§1c-v) |
| 6 | **op3-grade self-generated harmonics (W4)** | `research/2026-07-17_f6-meter-nonlinear-reval_result.md:69–74` (W4: 10 occupied modes, 5 at `n·ω_d`, `ω_d=0.524`; `2·ω_d=1.048` at `ω=1.05`) | the **nonlinear** channel that produces *literal* spectral downconversion — the precision the lowpass framing needs (§1e) |
| 7 | **#726 certified-κ sweep dips (the `ρ=0` positive control)** | `research/2026-07-18_f6-certified-kappa-sweep_result.md` R-1/R-3 (densest comb: 14.9% @ `x≈1.3`, 35.5% @ `x≈2.46`; `t63/T_rec=0.193`, transfer 5.2× the dip spacing) | the banked `ρ=0` positive control for the arm (§2) |
| 8 | **engine-capability-map §8c — the F6-arc state** | **NOT on main.** On the #728 branch `origin/docs/tier1-kb-debt-batch:manuscript/ave-kb/common/engine-capability-map.md` §8c (§8c.8 RULING 22 "KEEP THE INSTRUMENT; DOS-BALANCE = recommended direction, design-walk IN PROGRESS"; §8c.9 arc closure — *"Design-walk OWED with Grant"*) | this walk **is** that owed design-walk; the §8c update is owed there once #728 merges (see KB pointer). **Tagged unmerged-branch — not cited as main canon.** |

---

## KB pointer (D2 — owed placement)

**Where D2 landed, and why it lands here.** The D2 deliverable is a compact KB pointer at `engine-capability-map.md §8c`. **§8c does not exist on `main`** — it lives only on the unmerged #728 branch `docs/tier1-kb-debt-batch` (verified: `git show origin/docs/tier1-kb-debt-batch:manuscript/ave-kb/common/engine-capability-map.md` has §8c.1–§8c.9; `main`'s copy has no §8c). Per the D2 rule — *"if §8c is only on the unmerged #728 branch, put the pointer in the walk-record instead and note the owed placement — do NOT create a parallel §8c"* — the pointer is recorded here, and **no parallel §8c is created on main.**

> **★ OWED PLACEMENT (transplant when #728 merges).** Once PR #728 lands §8c on `main`, the following pointer paragraph is owed as a dated bottom-append to **§8c** (extending the §8c.9 arc-closure record). It is the **arm/auditor lane's** to land — this implementer lane surfaces it; it does not draft the auditor's manual entry into a branch it doesn't own.
>
> *Pointer paragraph (for §8c, when it is on main):*
> **2026-07-19 — the noise-floor ruling (the owed §8c.9 design-walk, resolved).** Grant ruled (in-chat) that the T2 sink couples **locally as a static, pre-occupied noise floor** ("effectively constant") — the Johnson-Nyquist vacuum-noise-floor row (`translation-circuit.md:151`). Consequence: the full-discharge pathology was **bath-emptiness** (a cold comb drains to zero; a floor relaxes *to* the floor, clamp moot); the **local arrow** = coherent returns dephasing into the floor's random phases (counting-only, static); growth/node-genesis **re-homes** to the cosmological rate rung (`Γ=3Hρ_latent`), which makes the prior **DOS-balance A/B fork MOOT** (§8c.8's recommended-direction slot resolves *away* from DOS-balance). The **thermal-floor arm** (branch `feat/f6-thermal-floor-arm`, in flight) adjudicates via a **revival-vs-ρ kill-shape** (`ρ=0` positive control = the #726 dips, 14.9%→35.5%; NO-SUPPRESSION = the live falsifier). Floor provenance (level + randomness) is **upstream** (past-hypothesis analog; crystallization-frontier candidate). Full arc + attribution: `research/2026-07-19_noise-floor-arrow-walk_RECORD.md`.

---

> **Walk-record provenance.** In-chat walk (Grant, 2026-07-19) + orchestrator walk (this session), recording the owed F6 design-walk left open at engine-capability-map §8c.9 (#728 branch). **Nothing here is new canon**; the arm adjudicates. Companion records: the KB pointer owed to `engine-capability-map.md §8c` when #728 merges (above); the docket continuation on `_orchestration/2026-07-10_rulings-docket.md`. All file:line citations re-verified at HEAD `6ff138b5`.
