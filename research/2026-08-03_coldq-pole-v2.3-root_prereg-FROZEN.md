# The cold-Q pole **v2.3** — FROZEN pre-registration (**ROOT certification; a one-defect re-freeze of v2.2**)

**Date:** 2026-08-03
**Class:** DERIVATION pre-registration (research-doc; **mints no `clm-`/`def-`; propagates to no KB/manuscript leaf; changes no solidity; edits no falsification ledger — regardless of outcome**). Committed **ALONE** and pushed **before any driver code and before any number produced by this instrument exists**.
**Result-doc pointer requirement.** The result doc that resolves these bins MUST carry `Prereg-file: research/2026-08-03_coldq-pole-v2.3-root_prereg-FROZEN.md` near its top, and every criterion it labels `Frozen:` MUST byte-match a quoted string in THIS file (`manuscript/ave-kb/tools/verify-frozen-provenance.py`).
**Provenance:** Grant's standing ruling of 2026-08-03 on the PR #854 audit's Q2 — **certify the located root, not the rectangle** — carried forward unchanged. This lane changes **one gate specification** of v2.2 and nothing else.
**Written against** `origin/main` = `184db4b6`.

---

## ★ SUPERSESSION NOTE (2026-08-03) — full auditable provenance, and the ONE change

*(Written to be auditable without any other document open. Every predecessor is cited by path AND commit SHA so the citation resolves regardless of which branch is checked out. This lane edits no predecessor file, by any byte.)*

### §S.1 What came before, in order

| lane | prereg (path @ commit) | outcome |
|---|---|---|
| **v1 / PR #845** (MERGED, `052ccbba`) | `research/2026-08-02_coldq-pole-derivation_prereg-FROZEN.md` | `SOLVER-NOT-CERTIFIED`. Real-axis asymptotic far-field matching; killed by an asymptotic (divergent) `1/r` series plus an `exp(2\|Im ω\| R_match)`-ill-conditioned subdominant-coefficient extraction. All four bins `N/A`. |
| **v2** | `research/2026-08-03_coldq-pole-v2_prereg-FROZEN.md` @ `00724432` (2026-08-02T20:23:09-07:00) | Frozen and pushed ALONE; **superseded pre-measurement** by v2.1. No driver code, no number. **BYTE-UNTOUCHED by this lane.** |
| **v2.1** | `research/2026-08-03_coldq-pole-v2.1_prereg-FROZEN.md` @ `7d8fe484` (2026-08-02T20:37:37-07:00) | Frozen and pushed ALONE. Battery at `bdcfa678`. `SOLVER-NOT-CERTIFIED` (C1, C9 FAIL; FT-B did not fire). All four bins `N/A`. **BYTE-UNTOUCHED by this lane.** |
| **v2.2** | `research/2026-08-03_coldq-pole-v2.2-root_prereg-FROZEN.md` @ `f15a6e4d` (2026-08-03T06:23:52-07:00) | Frozen and pushed ALONE. Battery at `8b9befed`; result doc `research/2026-08-03_coldq-pole-v2.2-root_result.md` @ `982c4c9b`. **`ROOT-NOT-CERTIFIED` on exactly one gate, G2.** Ten of eleven gates PASSED; all eleven self-tests FIRED. **BYTE-UNTOUCHED by this lane.** |

v2, v2.1 live on branch `research/coldq-pole-v2` (PR #854); v2.2 lives on branch `research/coldq-pole-v2p2` (PR #856, **OPEN, DO-NOT-MERGE**). **None of these files is on `origin/main`**, which is why prior-lane numerals below are transcribed with their commit SHA rather than read programmatically from this branch.

### §S.2 The v2.2 outcome this lane supersedes — the G2 receipts, verbatim

v2.2's frozen G2 criterion, quoted verbatim from `research/2026-08-03_coldq-pole-v2.2-root_prereg-FROZEN.md` @ `f15a6e4d` (§5, gate G2):

> `the maximum pairwise relative separation of Omega_star(n, 0.0, 7.0, 50) over the frozen ladder n in {32, 48, 64, 80, 96} is <= 1e-10`

v2.2's measured value and verdict, quoted verbatim from `research/2026-08-03_coldq-pole-v2.2-root_result.md` @ `982c4c9b` (§1 gate table row G2):

> \| **G2** ★ \| `n`-independence over `n ∈ {32, 48, 64, 80, 96}` \| `1e-10` \| `1.2496816388248957e-10` \| **FAIL** \|

v2.2's own measured mechanism, quoted verbatim from the same result doc, §2.2 (its convergence table) and §2.3:

> \| `n` \| error vs `n = 96`, relative \| ratio to the next rung \|
> \| 32 \| `1.2497e-10` \| `1544.6` \|
> \| 48 \| `8.0906e-14` \| `690.97` \|
> \| 64 \| `1.1709e-16` \| `403.39` \|
> \| 80 \| `2.9026e-19` \| — \|
> \| 96 \| `0.0` (reference) \| — \|

> **"Only the `n = 32` rung puts the gate over.** Every rung from `n = 48` up sits within `8.0906e-14` of the `n = 96` reference, so by the triangle inequality the maximum pairwise separation over `{48, 64, 80, 96}` alone cannot exceed `1.6181e-13` — **three orders inside the frozen `1e-10`.**"

And v2.2's own self-diagnosis of the defect, verbatim from its result doc §2.3:

> **"And the prereg contains the evidence that `n = 32` did not belong there.** Its own §9 justifies G0's tolerance by citing v2.1's measured Chebyshev coefficient tail, which reaches `5.3e-16` only by `n = 40`. **An independence ladder whose lowest rung sits below the order at which the coefficient functions are resolved is not measuring the root's `n`-independence; it is measuring the basis's inadequacy at that rung.**"

### §S.3 The pre-existing receipt this lane's change rests on — located and verified, not asserted

The receipt is **not** new evidence produced after v2.2's failure. It is a **measurement published in the v2.1 prereg**, which was **frozen and pushed 9 h 46 min before v2.2's prereg was frozen**. Its exact location in the v2.1 corpus, verified by two independent methods (`git show <sha>:<path> | grep -n` and `git show <sha>:<path> | awk 'NR==489'`) at freeze time:

**`research/2026-08-03_coldq-pole-v2.1_prereg-FROZEN.md:489`** (§9 "SATISFIABILITY", item 7) @ commit `7d8fe484`, verbatim:

> *"7. **The graded coefficient functions are finite and analytic on the grid.** At `n = 24/40/60` the assembled `𝒜`, `ℬ`, `𝒞` contain zero non-finite entries and the Chebyshev coefficient tail of `𝒞` falls to `5.3e-16` by `n = 40`. **This is a property of the COEFFICIENTS, not of any solution, and is labeled as such** (the v1 trap, named and quarantined). **C3's and C9's order sets sit well past it. Satisfiable.**"*

The same measurement is used a second time in the same document, at **`research/2026-08-03_coldq-pole-v2.1_prereg-FROZEN.md:308`**, where the v2.1 lane froze its own order set against it:

> *"the binding requirement is instead the **analytic structure of the coefficient functions**, whose measured Chebyshev tail reaches `5.3e-16` by `n = 40` (§9 item 7)"*

**Timeline, stated so the "knowable at freeze" claim is checkable rather than rhetorical.** `7d8fe484` = 2026-08-02T20:37:37-07:00. `f15a6e4d` = 2026-08-03T06:23:52-07:00. **The receipt predates v2.2's freeze by 9 h 46 min 15 s, and v2.2's own prereg cites it** (its §6 FT-2 non-vacuity column, and its §9 G0 row). **v2.2's ladder defect was therefore knowable from v2.2's own frozen document against itself, at freeze time, with no new measurement.** v2.2 said so itself, and routed rather than repaired.

### §S.4 The v2.2 routing this lane executes, verbatim

From `research/2026-08-03_coldq-pole-v2.2-root_result.md` @ `982c4c9b`, §2.4, verbatim:

> **"Per Rule 12 the slot is not refilled.** The obvious successor move — a ladder whose lowest rung is derived from the coefficient tail rather than chosen — is **stated so a successor does not have to rediscover it, and explicitly NOT adopted here**: it would be a post-hoc parameter selection under a frozen fence, which is exactly what Rule 11 forbids. A v2.3 needs a new prereg, a new version number and its own verification chain. **G2 stays banked as FAIL.**"

**This document is that new prereg, with that new version number, and it opens its own verification chain.** v2.2's `ROOT-NOT-CERTIFIED` is **not** retracted, reversed, re-scored, or rescued: it stands as banked, on the ladder it froze. Rule 12 is honoured — the v2.2 slot keeps its body and its verdict; this is a **new** hypothesis with a **new** version number, not a refill of the old slot.

### §S.5 ★ THE ONE CHANGE, stated precisely and exhaustively

**CHANGED — exactly one gate specification:**

> **G2's certification ladder becomes `n ∈ {48, 64, 80, 96}`, at the SAME frozen tolerance `1e-10`.**

Every rung of that ladder sits **at or above `n = 48`**, which is above the `n = 40` order at which the v2.1 receipt of §S.3 measures the coefficient representation as converged (`5.3e-16`). The tolerance is **not** loosened: it stays `1e-10`, byte-identical to v2.2's.

**ADDED — one supplementary gate and one supplementary self-test, so that the certification is a positive statement about convergence and not merely the absence of the failing rung:**

> **G2b — geometric-convergence SHAPE.** The successive-error ratios of the certification ladder against its highest rung must each exceed a floor frozen at `50` (derived in §4.4).
> **FT-2b — G2b's fireability**, by a stagnation mutation that is algebraically guaranteed to drive every ratio to `≈ 1` (§6).

**RETAINED, NOT DELETED — the `n = 32` rung, in three distinct roles:**

1. **As a GATED rung of every other gate that sweeps the ladder.** `G4(b)`, `G5`, `FT-5(a)` and `FT-5(b)` continue to run over the **full** frozen ladder `n ∈ {32, 48, 64, 80, 96}`, byte-identically to v2.2. **`n = 32` is not removed from the battery; it is removed from exactly one gate, the one whose semantics require an asymptotically-resolved representation.**
2. **As a REPORTED DIAGNOSTIC of G2 itself.** The `n = 32` root, its relative separation from the certification ladder, and the max pairwise separation over the **full five-rung** ladder are all measured, shipped in the results object, and printed in the result doc's gate table as a **diagnostic row**, explicitly **not gated**, tagged `PRE-ASYMPTOTIC BY THE v2.1 n = 40 COEFFICIENT-TAIL RECEIPT -- REPORTED, NOT GATED`.
3. **As a pre-registered expectation.** This lane states in advance (§9) that it expects that diagnostic to read `≈ 1.25e-10`, reproducing v2.2. **If it does not, that is reported as measured and the discrepancy is surfaced, not smoothed.**

**UNCHANGED — everything else, carried over from `f15a6e4d` verbatim-in-substance and restated self-contained below:** the target and the seed; the non-claim; the physics; the operator; the compactification; the import ledger I1–I19; all other frozen numerics; gates G0, G1, G3, G4, G5, G6, G7, G8, G9, G10 and their tolerances; self-tests FT-0…FT-10 and their thresholds and non-vacuity arguments; `R_iso = 0.5` and its four derivation receipts; the certification classes; the Rule-11 fence; **every bin boundary of BIN-1 / BIN-2 / BIN-3**; the FLAG-1 robustness window; the precedence order; `BIN-4 = N/A BY CONSTRUCTION`; and every non-claim of §1.2/§1.3.

### §S.6 ★ KILL-SWITCH DISCLOSURE — an adversarial audit of v2.2 was RUNNING, UNREPORTED, when this document was frozen

**Stated before any measurement, because a disclosure made after a result is worth less than one made before it.**

An adversarial audit of PR #856 (the v2.2 lane) was **running concurrently and had not reported** at the moment this prereg was frozen. That audit's scope includes **v2.2's attribution of its own G2 failure** — i.e. the claim that the excess is spectral under-resolution at `n = 32` rather than the migrating pseudo-spectrum the PR #854 audit found elsewhere in this arc.

**That attribution is the load-bearing premise of this lane's one change.** If the audit refutes it — if the `n = 32` excess is contamination rather than under-resolution — then removing `n = 32` from G2's ladder is **removing the rung that was detecting a real defect**, and this lane's certification would be an artifact of the removal. Accordingly, frozen in advance:

Frozen: `this lane's ONE change rests on v2.2's attribution of its G2 excess to spectral under-resolution at n = 32; an adversarial audit of that attribution was RUNNING AND UNREPORTED when this prereg was frozen; if that audit refutes the attribution, this lane HALTS at its next commit boundary and reports state, and any certification it has produced is void`.

**This is not a hedge that lets the lane keep its result either way.** A refutation voids the certification outright. The disclosure exists so that a reader can see the dependency **before** seeing the number, and so that the ordering of "audit reported" versus "result produced" is on the record and not reconstructed afterwards.

**And the lane does not lean only on v2.2's word.** G2b (§5) measures the geometric-convergence shape **directly and as a gate**, and FT-2b demonstrates that gate can fail. If the certification ladder's errors do not fall geometrically, G2b fails and the lane reports `ROOT-NOT-CERTIFIED` — **regardless of what the audit says.** That is this lane's own, independent check on the same premise.

---
## §0 — SECTOR / REGIME / PHASE-STATE / COORDS header, declared BEFORE any physics word

**Re-walked fresh, not incorporated by reference.** A successor that inherits a header without re-walking it inherits the header's blind spots too. The walk below reaches the same conclusions v2.2's did — **which is the expected outcome, because this lane changes a discretization parameter and not one line of physics** — and that agreement is stated as a result of the walk, not assumed before it.

- **MODE.** Cold (`a_* = 0`, Schwarzschild-limit) post-merger remnant ringing down. The object is **one** quasinormal resonance of the saturation cavity — the `ℓ = 2` toroidal shear mode located by v1, v2.1 and v2.2 — and **not** its ladder.
- **SECTOR.** The **observable** is a **transverse shear (T2)** oscillation. The **bias field** that builds the cavity is the **A1 radial dilatation** `ε_11 = 7GM/(c²r)`. Orthogonal grades, **not cross-wired**: the A1 strain is the DC operating point that sets the constitutive profile; the T2 shear mode is the small-signal AC riding on it. Receipt for `ε_11` **being** the Axiom-4 amplitude `A`: [`common/vocabulary-register.md:309`](../manuscript/ave-kb/common/vocabulary-register.md), verbatim *"the A1-dilatation **radial "strain"** that IS the Axiom-4 saturation **amplitude $A$**"*.
- **REGIME.** Far field (`r ≫ r_sat`) = **Regime I** — linear, lossless, reactive; a legal radiating port. The graded exterior `r > r_sat` = Regime I with a spatially varying modulus (Op14 grade). The wall `r = r_sat` = the **Regime III→IV** soft-mode terminus, `G_shear → 0`. The interior `r < r_sat` = **Regime IV**, where shear cannot propagate at all and which is therefore **not part of the computational domain** — the domain is `[r_sat, ∞)`, and that is a physics statement, not a truncation.
- **PHASE-STATE.** Op14 ON throughout the graded exterior as a **static constitutive grade** (the DC bias is time-independent; the ringdown is the small-signal response). `A = 1` exactly at `r_sat = 7GM/c²`; `Γ_shear = −1` there.
- **COORDS (A46 / `phase-space-coordinate-check`).** The confrontation lives in the **dimensionless-eigenvalue register** (`ω_R M_g`, `ω_I M_g`, `Q`) that AVE and GR share — no phase-space/real-space mismatch. This lane solves for the **complex pole** directly, so what it returns *is* the pole-`Q` that the GR comparator is; **no port→pole transfer is performed, needed, or assumed.**
- **The eigenfunction's own coordinate.** The radial localization observable (BIN-3) is read in **real-space radius normalized to `r_sat`** and compared only against real-space radii. It is **not** compared against `r_eff = 49M_g/9`, which is a **spectral marker (a cutoff radius), not a place**.

### Substrate-native walk (`substrate-native-check`, fired BEFORE the first line of numerical code)

1. **K4 / srs connectivity.** This is a **CONTINUUM** instrument. Frozen disclosure: `the radial channel is a CONTINUUM representation of the shear constitutive law; it is not a discretization of the srs stencil and carries no K4 connectivity claim`. What it consumes from the lattice is the **constitutive law only**: the Ax-4 kernel and the Op16 shear-speed projection.
2. **Cosserat / channel basis.** The mode certified is on the **toroidal (odd-parity / axial) branch**, whose displacement field is **exactly divergence-free**, so the Lamé `λ` (bulk/A1) modulus drops out of the equations of motion **identically** rather than by assumption. Frozen: `the toroidal (odd-parity) branch is exactly divergence-free, so the bulk modulus drops out identically and there is no linear P-SV conversion partner; the single-channel classification is structural in this branch`.
3. **Op14 saturation.** Enters as the **static constitutive grade** `S(A) = sqrt(1 - A²)` with `A(r) = r_sat/r`, projected into shear by Op16. Frozen: `Op14 enters as a static constitutive grade S(A); the A -> 1 terminus is handled by an exact change of variable, not by a numerical cutoff or a regularized floor`.
4. **★ The compactification is the medium's own order parameter, and that is what makes the ROOT-LOCAL gates meaningful.** The radial coordinate is `A = r_sat/r` — the Axiom-4 saturation amplitude itself; `A = 1` IS the wall, `A = 0` IS infinity. Frozen: `the compactified radial coordinate is the Axiom-4 saturation amplitude A = r_sat/r itself, so A = 1 is the wall and A = 0 is infinity; the instrument adopts the medium's own order parameter as its coordinate rather than imposing a lattice-Cartesian one`. **Root-local consequence, stated in advance:** because `r_sat` appears in the discretized operator *only* through this coordinate and through `Ω = ω r_sat`, a root-local `x_sat`-invariance measurement (G8) is a check on the arithmetic path, not on the physics — the physics cancellation is structural. It is gated anyway, in mp, because v2.1's version of this measurement was corrupted by a `complex` cast (PR #854 audit WARN 7).
5. **Phase-space vs real-space (A46).** Every verdict-class observable is a **dimensionless ratio**: `ω M_g`, `Q`, `r_peak/r_sat`. **α-CLEAN** — `α` appears nowhere in the chain.
6. **Checkpoint: boundary-not-bulk.** The resonator is a **boundary/graded-shell** object, not a bulk-force object — consistent with the #403/#404 localization ruling. The loss is a **radiative port at infinity** (Ax-3-licensed), and there is **no** `Re{Z}` anywhere in the medium. **G10 tests exactly that, and it tests it ON THE CERTIFIED EIGENFUNCTION'S OWN OPERATOR** rather than on a separate closed cavity.
7. **Checkpoint: what the substrate does NOT supply.** The angular index `ℓ = 2` is **not** derived here; it is the quadrupole selection the corpus carries for the GW channel. **And the substrate does not here supply a low-frequency cutoff either, which is exactly why no completeness claim is made.** Stated so neither is mistaken for an output.
8. **★ NEW CHECKPOINT, forced by this lane's one change: is the Chebyshev order a physics knob or an engineering knob?** It is an **engineering knob**, and the check is that nothing physical depends on it: `n` enters the medium nowhere — not the profile `A = r_sat/r`, not the kernel `S = sqrt(1 − A²)`, not the Op16 projection, not the `Γ = −1` wall, not the port. It enters **only** the representation of the coefficient functions on the grid. Frozen: `the Chebyshev order n is an ENGINEERING knob that enters the representation and enters the medium nowhere; changing which orders a convergence gate is measured over changes no physical content, and the only thing it can legitimately change is whether the gate is measuring the root or measuring the basis`. **This is the checkpoint that licenses the one change as a numerics repair rather than a physics retune — and it is also the checkpoint that would forbid changing `x_sat`, `ℓ`, the kernel or the wall condition, none of which this lane touches.**

### Pre-test physics check (`pre-test-physics-check`, Rule 16 — ONE plumber question surfaced to Grant BEFORE the design locks)

> **Grant — this is a NEW question, and it is the one this lane creates rather than the one v2.2 asked.** v2.2's question was about the *bottom* of the sweep (the low-frequency cutoff) and it is still open, still deferred, and restated unchanged in FLAG-5. **My question is about where the energy sits, because this lane is the first in the arc that can actually reach BIN-3 and land a verdict on it.**
>
> Here is what the uncertified prior run saw. I walk outward from the wall at `r = r_sat` and integrate the mode's stored energy density. It does **not** peak anywhere inside my window — it keeps climbing all the way to `r/r_sat = 2.0`, which is just where I stopped looking. The wall itself holds about `4 %` of the window's maximum. **In plumber terms: I've got a shorted stub with a taper on it, I'm looking for the belly of the standing wave, and I can't find one — the amplitude just keeps growing as I walk away from the short.**
>
> Two readings, and I cannot tell them apart from inside the numerics:
> - **(a) It's real.** The cavity genuinely stores its energy far out on the taper, the "rim ring" picture is wrong, and `r_eff` is a spectral marker with no place attached to it.
> - **(b) It's the leak, not the mode.** Any leaky resonator's eigenfunction grows like `exp(|ω_I| r)` on the way out — that's the outgoing wave that left earlier, arriving with more amplitude because the thing was ringing harder back then. **On that reading "where does the mode live" is the wrong question for a radiating cavity, and any answer I compute is a statement about my window's right-hand edge.**
>
> **What I need from you is the plumber's call on whether (b) is simply what a leaky resonator does** — because if it is, `BIN-3-MONOTONE` is the honest verdict and the localization axis should be retired from this arc rather than re-measured with a wider window. I have **pre-registered `BIN-3-MONOTONE` as a reachable bin** (§7.4) precisely so this can land in a pre-registered slot instead of in prose after the fact. **I am not widening the window to hunt for a peak, and I am not re-defining the observable.** The window stays `[1.0, 2.0]`, byte-identical to v1/v2.1/v2.2.
>
> **Carried forward unchanged and NOT re-asked:** v2.2's deferred question — a **substrate-derived low-frequency cutoff** for the graded shear cavity, without which no completeness or overtone statement is honest. `BIN-4` stays `N/A BY CONSTRUCTION` for as long as that takes.

### Consistency-vs-emergence tag (`consistency-vs-emergence`), computed BEFORE any result — and it is not uniform across the bins

Written in units of `r_sat`, the problem has **no free parameter at all**: the profile is `A = r_sat/r`; the kernel is `S = sqrt(1 - A²)`; the speed is `c_shear = c₀·sqrt(S)`; the inertia is the cold `ρ₀`. Therefore `Ω ≡ ω·r_sat/c₀` is a **pure number** fixed by the profile SHAPE, the Ax-4 kernel, and `ℓ`.

| output | rides `r_sat`'s coefficient `7`? | class |
|---|---|---|
| `ω_R M_g` (BIN-1) | **YES** — `ω_R M_g = Re(Ω)/x_sat` with `x_sat = 7` | **VALUE-CONSISTENCY.** The `7` is the `1/7` trace-reversed bulk projection, which takes `ν_vac = 2/7` as **input** ([`one-seventh-impedance-projection.md:18`](../manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/one-seventh-impedance-projection.md): *"the $1/7$ boundary is a projection of a GR-imported ratio, not a first-principles lattice output"*). **May NOT be headlined as value-level emergence.** |
| **`Q = ω_R/(2\|ω_I\|)` (BIN-2)** | **NO — it cancels exactly** | **`ν_vac`-FREE, therefore EMERGENCE-CAPABLE at value level.** `Q = Re(Ω)/(2\|Im(Ω)\|)`; the `x_sat` conversion divides out identically. |
| `r_peak/r_sat` (BIN-3) | **NO** | `ν_vac`-free ratio; **FORM-class** statement about where the mode lives. |
| the existence + location of the root itself | **the LOCATION rides it; the SHAPE does not** | The certified object is `Ω`, a pure number. Its projection into `ω M_g` is what carries the imported `7`. |

Frozen tag: `Q and the localization ratio are exactly nu_vac-free (the r_sat scale divides out identically); omega_R*M_g is NOT and is VALUE-CONSISTENCY class because the 7 in r_sat = 7GM/c^2 is the 1/7 projection of the GR-imported nu_vac = 2/7`.

> **★ WHAT A CERTIFIED ROOT WOULD AND WOULD NOT MEAN, written before the run.** A `ROOT-CERTIFIED` verdict is a statement about an **instrument**, not about the world: it says *this discretization's eigenvalue at this location is a property of the continuous problem and not of the discretization*. It does **not** say the substrate rings there — that additional step needs the canonical input set of §3 to be right, and I7 in particular is **assumed, not tested** (FLAG-3). And it says **nothing whatever** about what else the substrate does or does not do at other frequencies (§1's non-claim). **Additionally, and specific to this lane:** a `ROOT-CERTIFIED` verdict here would be earned on a ladder that **excludes** `n = 32` from one gate, and any reader is entitled to the `n = 32` number, which is why it is reported as a diagnostic row rather than dropped.

---

## §1 — THE TARGET, AND THE EXPLICIT NON-CLAIM

### §1.1 The target

**Certification of the SINGLE located root of the graded spin-2 hyperboloidal problem near**

```
Omega_0  =  1.8536552108408788 - 1.0072567831433188 i
```

**Seed provenance.** That value is transcribed from the v2.1 shipped results object, `research/drivers/coldq_pole_v2_results.json`, at commit `bdcfa678` (branch `research/coldq-pole-v2`, PR #854, **OPEN, DO-NOT-MERGE — the file is not on `origin/main`, which is why it is transcribed rather than read**). It is the same seed v2.2 used, unchanged. It is carried in the driver as a named frozen constant with that citation in a comment.

Frozen: `the frozen seed Omega_0 = 1.8536552108408788 - 1.0072567831433188i is a SEED ONLY: at each order the polish is seeded from the double-precision linearized-pencil eigenvalue NEAREST the frozen seed, so the seed selects WHICH pencil eigenvalue is polished and enters no gate, no tolerance, no comparator and no bin as a value`.

**Certification means: ALL root-local gates G0..G10 (including G2b) of §5 PASS and ALL fireability self-tests FT-0..FT-10 (including FT-2b) of §6 FIRE.** There is no partial certification and no scoped certification in this lane: `ROOT-CERTIFIED` or `ROOT-NOT-CERTIFIED`.

### §1.2 The non-claim, written in advance and binding

> **This lane asserts the existence and location of THIS root; it asserts NOTHING about the absence or presence of other modes.**

Frozen: `this lane asserts the existence and location of THIS root; it asserts NOTHING about the absence or presence of other modes`.

Operationally, and each of these is a **prohibition on this lane's own result doc**:

- **NO winding, argument principle, or contour integral is computed over any rectangle, box or region, anywhere in this lane.** Frozen: `no argument-principle winding, no contour integral and no region count is computed anywhere in this lane; the pole-counting instrument the PR #854 audit impeached is not used, not repaired and not relied on`.
- **NO completeness claim, no "the only mode", no "no overtones", no mode count, no ladder.** `BIN-4` is `N/A BY CONSTRUCTION` (§7), stated **in advance**, and that status is **not** an outcome of any measurement.
- **NO claim that the certified root is the FUNDAMENTAL.** It is *a* root. Whether it is the least-damped, the lowest, or the physically-selected one is **not adjudicated here**.
- **The pseudo-spectrum the PR #854 audit found is not re-measured, not characterised, and not explained here.** G5 measures only whether it comes within a frozen radius of the certified root.
- **★ NEW, and binding on this lane specifically: a certification here is NOT a retroactive pass for v2.2.** Frozen: `a ROOT-CERTIFIED verdict in this lane does not certify, rescue, re-score or reverse v2.2, which stands ROOT-NOT-CERTIFIED on the ladder it froze; and it does not establish that the n = 32 rung was harmless, only that it is below the order at which the pre-existing v2.1 coefficient-tail receipt says the representation is converged`.

### §1.3 What this lane additionally does NOT do

- **X1 — does NOT derive `ℓ = 2`.** The quadrupole selection is an input.
- **X2 — does NOT derive `ν_vac`, `K = 2G`, or the `7` in `r_sat`.** Their value provenance is GR-IMPORT, closed by PR #261/#506 and untouched here.
- **X3 — does NOT touch the spin (`a_* > 0`) mapping.** This is the `a_* = 0` anchor only.
- **X4 — does NOT compute a port-`Q`, a radiation resistance, or a Chu/Collin–Rothschild stored-energy `Q`.**
- **X5 — does NOT adjudicate #814 FORK-12.** No `ℓ`-ladder is computed in this lane at all.
- **X6 — does NOT run FORK-3(b)** (`ρ_eff = ρ₀/S³` as the shear-wave inertia).
- **X7 — does NOT certify, rescue, re-adjudicate or repair PR #845, PR #854 or PR #856.** All three remain as they stand. **G6's two-instrument agreement is a check on THIS lane's transcription, not a certification of any predecessor** — see FLAG-2 in §10.
- **X8 — does NOT derive, assume, sketch or gesture at a low-frequency cutoff.** Deferred, with Grant's input owed first (§0).
- **X9 — does NOT land any claim, solidity change, KB row, manuscript edit or ledger entry**, whatever the outcome.
- **X10 — NEW: does NOT widen, move or re-define the BIN-3 localization window, and does NOT re-tune any bin boundary.** Every boundary in §7 is byte-identical to v2.2's, which were byte-identical to v2.1's and v2's and v1's.

---
## §2 — THE PHYSICS (inherited, ratified, NOT re-derived) AND THE OPERATOR THIS LANE CARRIES OVER

### §2.1 Inherited unchanged from the ratified v1/v2.1/v2.2 framing — stated, not re-derived

The BH ringdown as a **transmission line**: series `L = ρ`, shunt `C = 1/G(A)`; the DC strain profile `A(r) = 7GM/c²r` grades it; the wall is `Z_shear → 0`, a **SHORT** at `r_sat`; the exterior is the graded taper; and `Q` is read as **the pole**, not from a port formula. **Zero free inputs.**

- `ρ(r) = ρ₀` — the cold lattice inertia;
- `G_shear(r) = ρ₀ c_shear(r)²` with `c_shear = c₀·sqrt(S)` — **Op16, CANONICAL** ([`common/operators.md:56`](../manuscript/ave-kb/common/operators.md), row `Op16 | Universal Wave Speed | $c_{shear} = c_0\cdot\sqrt{S}$`), reinforced verbatim at [`saturating-modulus-and-backreaction.md:60`](../manuscript/ave-kb/vol3/gravity/ch02-general-relativity/saturating-modulus-and-backreaction.md): *"**SHEAR softens:** $c_{\text{shear}}=c_0\sqrt{S}=c_0(1-A^2)^{1/4}\to0$ — a **derived** $\sqrt{S}$ projection,"*
- `S(A) = (1 - A²)^{1/2}` and `A = ε_11/ε_yield` with `ε_yield = 1` — **Ax 4**, verbatim from the same leaf at `:51`–`:52`: *"\qquad A=\varepsilon_{11}/\varepsilon_{\text{yield}}\ (\varepsilon_{\text{yield}}=1),"* and *"\qquad D(A)=\frac{1}{S(A)},\qquad S(A)=(1-A^2)^{1/2}."*
- `ε_11 = 7GM/(c²r)` — [`temporal-spatial-lattice-decomposition.md:14`](../manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/temporal-spatial-lattice-decomposition.md), verbatim *"The principal radial strain $\varepsilon_{11} = 7GM/(c^2 r)$ compresses the lattice asymmetrically."*
- the SHORT — [`vol3/claim-quality.md:123`](../manuscript/ave-kb/vol3/claim-quality.md), verbatim *"a solid$\to$liquid free surface ($G_{shear} \to 0$) is exactly a $Z_{shear} \to 0$ short"*; and `r_sat` at `:121`, verbatim *"the **shear/bulk** rupture boundary is deeper, at $r_{sat} = 7GM/c^2 = 3.5\,r_s$ where the radial strain $\varepsilon_{11} = 1$"*.

The **toroidal (odd-parity)** radial system, inherited unchanged, in `W(r)` with conjugate traction `T(r) ≡ μ(r)·(W′ − W/r)`, `μ ≡ G_shear`:

```
W'' + (2/r + g)*W' + [ w^2 rho/mu - l(l+1)/r^2 - g/r ]*W = 0 ,   g = mu'/mu
```

with the spin-2 stored-energy weighting `(ℓ−1)(ℓ+2)` (NOT the spin-1 `ℓ(ℓ+1)`):

```
E_strain(r) ~ mu(r)*[ |W' - W/r|^2 + (l-1)(l+2)*|W|^2/r^2 ]*r^2
E_kin(r)    ~ rho(r)*|w|^2*|W|^2*r^2
```

Frozen: `the radial system is the toroidal (odd-parity, exactly divergence-free) branch of the shear-channel continuum equations; the impedance relation T = mu(W' - W/r) and the (l-1)(l+2) stored-energy weighting are the spin-2 ones and no spin-1 vector-multipole impedance is imported anywhere in this lane`.

### §2.2 The compactified, outgoing-factored operator (the object this lane discretizes)

Set `c₀ = ρ₀ = G₀ = 1`; `A ≡ r_sat/r ∈ (0, 1]`, so `μ = S = sqrt(1 − A²)`; `Ω ≡ ω·r_sat/c₀`. Factor the outgoing wave out **analytically**,

```
W = A * exp( i Om (1/A + lam A) ) * psi(A)
```

with `λ` a frozen **hyperboloidal gauge parameter**. At `λ = 0`,

```
A^2 psi_AA + [ -2 i Om + 2A + A^2 ghat ] psi_A
           + [ Om^2/(S(1+S)) - i Om ghat - l(l+1) + 2 A ghat ] psi = 0 ,   ghat = -A/(1-A^2)
```

Frozen: `no radiation boundary condition is imposed at infinity; the outgoing branch is the analytic branch of the compactified equation and the ingoing branch carries an essential singularity that is not in the discretization's function space, so no far-field matching, no asymptotic series and no subdominant-coefficient extraction occurs anywhere in this lane`.

The wall terminus is reached exactly by `A = 1 − η²`, `η ∈ [0,1]`, under which `η = 0` is an **ordinary regular point** and the traction-free SHORT is exactly `dψ/dη|_{η=0} = 0`. Frozen: `the wall is reached exactly via the A = 1 - eta^2 substitution, which makes eta = 0 an ordinary regular point of the transformed equation; the canonical traction-free SHORT is exactly the single linear condition dpsi/deta = 0 at eta = 0, with no offset, no series start, no regularized modulus floor and no shooting`.

Writing the `η`-form as `𝒜(η)ψ_ηη + ℬ(η,Ω)ψ_η + 𝒞(η,Ω)ψ = 0`, the discrete operator is the quadratic matrix pencil `M(Ω) = M0 + Ω·M1 + Ω²·M2` on Chebyshev–Gauss–Lobatto nodes, with row `0` replaced by the exact SHORT row.

### §2.3 ★ THE CARRY-OVER DISCLOSURE — this lane is NOT an independent third reimplementation, and that changes what G6 buys

**This is the single most important honesty statement in this document and it is written before any code exists.**

v2.2's §2.3 froze an **independent reimplementation** disclosure and argued that G6 was therefore a live check on a fresh transcription. **This lane does something different, deliberately, and the difference is disclosed rather than glossed:**

Frozen: `the v2.3 instrument CARRIES OVER v2.2's method into this lane's own file research/drivers/coldq_pole_v2p3_root.py by copy-with-attribution, so that the ONLY difference between the two batteries is the gate specification of section S.5; it is NOT an independent third reimplementation, and this lane may not claim reimplementation independence from v2.2`.

**Why carry over rather than reimplement a third time.** The scientific question this lane exists to answer is *"does the certification change when the one defective gate specification is repaired?"* A fresh third transcription would answer a **different** question — *"does a third instrument agree?"* — and would confound the two: any change in the gate table could then be the ladder **or** the new transcription. **Carrying the method over unchanged makes the gate-specification change the only variable.** That is a controlled comparison, and it is chosen for that reason.

**The four consequences, each stated as a limit on what this lane may claim:**

1. **G6 no longer demonstrates independence from v2.2.** It still gates this lane's file against v1's **different-in-kind** instrument (real-axis asymptotic matching, sharing no formulation with this one), and FT-6 still demonstrates it catches a coefficient corruption. **But a G6 pass here is not evidence that two independent implementations agree — v2.2 already established what it established, and this lane adds nothing to it.** Frozen: `G6 in this lane gates THIS file's transcription against v1's different-in-kind instrument and adds NO new implementation-independence beyond what v2.2 already reported; a G6 pass here may not be presented as a second independent confirmation`.
2. **Numerical agreement with v2.2 is EXPECTED, not corroborative.** Every unchanged gate should reproduce v2.2's number, and where it does that is a **regression check**, not a confirmation. Frozen: `agreement between this lane's unchanged gates and v2.2's is a REGRESSION CHECK on the carry-over and is not independent corroboration of any value`.
3. **A DISagreement on an unchanged gate is a defect, and it is reported as one.** If any unchanged gate's measured value differs from v2.2's published value by more than its own reporting precision, that is a carry-over error or a platform difference, and the result doc must surface it with both numbers. Frozen: `if any gate this lane did not change measures differently from the value v2.2 published, the result doc reports BOTH numbers and treats the difference as a defect to be surfaced, not as a new measurement`.
4. **Attribution is at the transcription site.** Every routine and every algebraic form carried over carries a comment naming its source file and lane. `research/drivers/coldq_pole_v2p2_root.py` and `research/drivers/coldq_pole_v2.py` are **neither imported nor edited nor executed** by this lane; they belong to PR #856 and PR #854 respectively and are byte-untouched here.

### §2.4 What is NOT the same as the spin-1 problem

The **impedance relation** is `T = μ(W′ − W/r)` — *not* `Z_ℓ ∝ h_ℓ′/h_ℓ`. The extra `−W/r` term is the tensor-rank content and it is what makes the wall condition genuinely different from the spin-1 one; likewise the stored-energy weighting carries `(ℓ−1)(ℓ+2)`, not `ℓ(ℓ+1)`. **G7 measures both differences AT THE CERTIFIED ROOT** — one on the eigenvalue (the wall row), one on the eigenfunction (the energy weighting).

---

## §3 — IMPORT LEDGER (every number the instrument consumes, tagged; `substrate-first-for-numbers`)

| # | Input | Value / form | Class | Source |
|---|---|---|---|---|
| **I1** | Saturation-wall radius | `r_sat = 7GM/c² = 7 M_g`, i.e. `x_sat = 7` | **`[canon]`** — form-derived, **VALUE rides the GR-imported `ν_vac`** | `vol3/claim-quality.md:121`; `temporal-spatial-lattice-decomposition.md:14`; provenance at `one-seventh-impedance-projection.md:18` |
| **I2** | Saturation amplitude profile | `A(r) = ε_11/ε_yield = r_sat/r`, `ε_yield = 1` | **`[canon]`** | `saturating-modulus-and-backreaction.md:51`; `vocabulary-register.md:309` |
| **I3** | Ax-4 kernel | `S(A) = (1 − A²)^{1/2}` | **`[canon]` — Axiom 4** | `saturating-modulus-and-backreaction.md:52` |
| **I4** | Shear-speed projection | `c_shear = c₀·S^{1/2}` (Op16) | **`[canon]`** | `common/operators.md:56`; `saturating-modulus-and-backreaction.md:60` |
| **I5** | Shear-wave inertia | `ρ(r) = ρ₀` (cold lattice inertia) | **`[canon, FORK-3 leading reading]`** — the naming gap at `vol3/claim-quality.md:122` is #814 CF-7, **routed not repaired** | `vol3/claim-quality.md:122` |
| **I6** | Inner boundary condition | traction-free, `T(r_sat) = 0` (`Z_shear → 0`, `Γ_shear = −1`) | **`[canon]`** | `vol3/claim-quality.md:123` |
| **I7** | Outer boundary condition | outgoing radiation into the cold matched lattice; **no far-field structure, no second reflection** | **`[canon]` — Regime-I radiative port, Ax-3-licensed. ASSUMED, NOT TESTED — see FLAG-3** | §0 REGIME header |
| **I8** | Angular index | `ℓ = 2` (quadrupole) | **`[canon, INPUT not derived]`** | §1.3 X1 |
| **I9** | Unit choice | `M_g = 1`, `c₀ = 1`, `ρ₀ = 1`, hence `G₀ = 1` | **`[dimensionless by construction]`** | this lane |
| **I10** | `ν_vac = 2/7` | imported **read-only** from `ave.core.constants.N_NU`; used ONLY to form the `r_eff = r_sat/(1+ν_vac)` comparator reported alongside BIN-1 | **`[canon]` — VALUE GR-IMPORTED (PR #261/#506)** | `src/ave/core/constants.py:397` |
| **I11** | GR cold comparator | `ω_R M = 0.37367`, `ω_I M = 0.08896` at `a_* = 0`, read **programmatically** from the frozen `KERR_QNM` dict | **`[GR-IMPORTED comparator — the frozen C-comparator, inherited unchanged from v1, v2.1 and v2.2]`** | `research/2026-07-20_v1-spin-mapping-adjudication_rerun.py:51` |
| **I12** | GR `ℓ=2` overtone real parts | `ω_R M (2,0) = 0.373672`, `(2,1) = 0.346711`, read **programmatically** from the in-repo `SCHW_OMEGA_R` dict | **`[GR-IMPORTED comparator]` — used ONLY to derive the G5 isolation radius's upper constraint (§4.3); enters no bin** | `research/2026-07-20_ringdown-systematics_checks.py:69`, `:72` |
| **I13** | GR `ℓ=2` overtone imaginary parts | `ω_I M (2,0) = 0.088962` from the in-repo `SCHW_OMEGA_I` dict; `ω_I M (2,1) = 0.273915` with in-repo carrier `research/drivers/coldq_pole_derivation.py:106` (merged with PR #845) | **`[GR-IMPORTED comparator]` — same restricted use as I12; enters no bin** | `research/2026-07-20_ringdown-systematics_checks.py:133`; `research/drivers/coldq_pole_derivation.py:106` |
| **I14** | Standing AVE comparators | `ω_R M_g = 18/49`, `Q = ℓ = 2`, `r_eff = 49M_g/9` | **`[corpus comparators — the objects under test]`** | `vol3/claim-quality.md:198`; `vol3/cosmology/ch15-black-hole-orbitals/qnm-quality-factor.md`; #814 CF-9 |
| **I15** | Prior-lane root, v2.1 | `Ω_0 = 1.8536552108408788 − 1.0072567831433188i` | **`[PRIOR-LANE SEED — selects which pencil eigenvalue is polished; enters no gate, tolerance, comparator or bin]`** | `research/drivers/coldq_pole_v2_results.json` @ `bdcfa678` |
| **I16** | Prior-lane root, v1 | `Ω_v1 = x_sat·(omega_R_M − i·omega_I_M)` reconstructed **programmatically** from the shipped v1 JSON row `x_sat = 7.0` | **`[PRIOR-LANE COMPARATOR — G6 only; NOT-ADJUDICATED prior-lane data, gates THIS lane's transcription and certifies nothing about #845]`** | `research/drivers/coldq_pole_derivation_results.json:505`, `:509`, `:510`, `:512` |
| **I17** | Prior-lane discretization artifact | `Ω_art = 0.30587571217415294 − 2.4674822214282157i`, banked by v2.1's own frozen physical-vs-artifact criterion | **`[PRIOR-LANE FIREABILITY TARGET — FT-5 and the G2b artifact diagnostic only]`** | `research/drivers/coldq_pole_v2_results.json` @ `bdcfa678` |
| **I18** | Prior-lane contaminated-edge probe | `Ω_edge = 0.1400 − 3.5035i`, one of v2.1's own frozen C9 probe points, measured there at `3.658e+00` | **`[PRIOR-LANE FIREABILITY TARGET — FT-5 only]`** | v2.1 result doc §3.2 probe table @ `bdcfa678` |
| **I19** | Instrument numerics | Chebyshev order `n`, gauge `λ`, mp precision `dps`, polish tolerance and iteration cap, dedupe radius, isolation radius `R_iso`, **the G2b ratio floor** | **`[ENGINEERING CHOICE — tagged, frozen in §4]`** | this lane |
| **I20 ★** | **Prior-lane coefficient-resolution receipt** | the Chebyshev coefficient tail of `𝒞` falls to `5.3e-16` by `n = 40` | **`[PRIOR-LANE MEASURED RECEIPT — used ONLY to place G2's certification-ladder lower rung; enters no tolerance, no comparator and no bin]`** | `research/2026-08-03_coldq-pole-v2.1_prereg-FROZEN.md:489` (§9 item 7) @ `7d8fe484`, restated at `:308` |
| **I21 ★** | **Prior-lane convergence diagnostic** | successive-error ratios `1544.6`, `690.97`, `403.39` over `n = 32→48→64→80` against `n = 96` | **`[PRIOR-LANE MEASURED DIAGNOSTIC — used ONLY to derive the G2b floor in §4.4; enters no bin. Produced by a ROOT-NOT-CERTIFIED instrument and used to set a floor with an order of headroom, never as a value]`** | `research/2026-08-03_coldq-pole-v2.2-root_result.md` §2.2 @ `982c4c9b` |

**R8 audit rule (frozen).** `every number the instrument consumes appears on this ledger with its tag; no SM/GR convention default enters anywhere, and in particular no spin-1 vector-multipole impedance, no Chu/Collin-Rothschild stored-energy weighting, and no Regge-Wheeler or Zerilli potential is used as an input`.

**★ Ledger discipline note on I20 and I21, stated at freeze.** Both are prior-lane numbers produced by instruments that are **not certified**. Neither is used as a **value**: I20 places a ladder rung at an order **above** the resolution it reports, and I21 sets a **floor** an order of magnitude **below** the ratios it reports. Frozen: `I20 and I21 are prior-lane numbers from uncertified instruments and are used ONLY to place a ladder rung above a measured resolution and a ratio floor an order below measured ratios; neither enters a bin, a comparator or a tolerance as a value, and a certification in this lane certifies neither predecessor`.

---
## §4 — THE METHOD AND ITS FROZEN NUMERICS

### §4.1 The method (frozen, unchanged from v2.2)

Frozen: `the method is a compactified hyperboloidal Chebyshev spectral discretization in the Axiom-4 amplitude coordinate A = r_sat/r with the outgoing wave divided out in closed form, the traction-free SHORT imposed exactly as dpsi/deta = 0 at eta = 0, no boundary condition imposed at infinity, root extraction by extended-precision determinant polish seeded from the double-precision linearized pencil, and eigenfunction extraction by extended-precision inverse iteration; there is no matching radius, no asymptotic series, no shooting, no subdominant-coefficient extraction and NO ARGUMENT-PRINCIPLE WINDING anywhere in the chain`.

**ENGINEERING-CHOICE TAG (`substrate-first-for-numbers`).** Frozen: `the method is NUMERICS and is tagged ENGINEERING CHOICE; the medium, the profile, the kernel, the wall condition and the radiative port are CANON; no physical content of any kind is derived from the choice of discretization, and the gauge parameter lambda, the Chebyshev order n, the extended-precision dps, the polish tolerance and the isolation radius are engineering knobs whose only permitted role is to be varied and shown not to move the answer, or to be justified from prior-lane evidence and frozen`.

### §4.2 Frozen numerics (every parameter fixed here, before any code)

- **Radial coordinate:** `A = r_sat/r`, `A = 1 − η²`, `η ∈ [0,1]` on Chebyshev–Gauss–Lobatto nodes.
- **Primary Chebyshev order:** `n = 48`.
- **★ FULL frozen ladder (unchanged from v2.2; used by G4(b), G5, FT-5(a), FT-5(b), and by G2's DIAGNOSTIC row):** `n ∈ {32, 48, 64, 80, 96}`.
- **★ G2 CERTIFICATION ladder (THE ONE CHANGE):** `n ∈ {48, 64, 80, 96}`.
- **Hyperboloidal gauge:** primary `λ = 0`; frozen set `λ ∈ {−0.25, 0.0, +0.25}`.
- **Extended precision:** primary `dps = 50`; high-precision cross-check `dps = 80`.
- **Polish:** deterministic complex secant on `det M(Ω)` computed by mp LU with partial pivoting, seeded from the double-precision linearized-pencil eigenvalue nearest the frozen seed, terminating at `|Δ| ≤ 1e-38·|Ω|` or `60` iterations. **No RNG anywhere; no adaptivity; fully deterministic.**
- **Eigenfunction:** `4` rounds of mp inverse iteration on the row-equilibrated `M(Ω*)`, started from the **deterministic** all-ones vector, normalized in the infinity norm after each round.
- **Row equilibration:** each row of `(M0, M1, M2)` divided by that row's max modulus across the three matrices, so `‖M‖_∞ = O(1)` and the residual G1 measures is scale-free.
- **Dedupe radius:** `1e-6` relative — applied to the pencil spectrum before any count.
- **`x_sat` set (G8):** `{5, 7, 11}`, run in mp end-to-end with **no** `complex` cast anywhere on the path from the polished root to the reported spread.
- **Localization window (BIN-3):** `r/r_sat ∈ [1.0, 2.0]`, `401` equispaced points in the `η` image of that window. **Byte-identical to v1/v2.1/v2.2; not widened.**
- **★ G2b ratio floor:** `50` (derived in §4.4).
- **Runtime:** frozen `total battery runtime <= 3600 s on the reference machine; a longer run is disclosed, not silently accepted`. The budget is **not** an adjudication criterion.
- **Engine fence:** Frozen: `engine src/ave BYTE-UNTOUCHED; the instrument lives entirely in research/drivers/ and imports ave.core.* read-only`.

### §4.3 THE G5 ISOLATION RADIUS — carried over from v2.2 unchanged, with its four receipts

> **DISCLOSURE.** Every number in this subsection is **arithmetic on already-published prior-lane values** (the v1 and v2.1 shipped JSONs and the frozen GR comparators I11–I13). The arithmetic is reproduced by the driver and registered by the number check.

`R_iso` is the radius of the exclusion annulus around the certified root inside which **no other eigenvalue of the discretization's spectrum may sit, at any order of the FULL frozen ladder**. It is bounded from ABOVE by physics (the gate must not forbid a genuine neighbouring overtone) and from BELOW by numerics (the gate must be more than a restatement of the dedupe radius).

**(a) Upper constraint — a genuine overtone must NOT trip the gate.** GR's Schwarzschild `ℓ = 2` fundamental and first overtone, converted to this lane's scale-free variable by `Ω = x_sat·ω M` at `x_sat = 7`:

```
Om_GR(n=0) = 7*(0.373672 - 0.088962i) = 2.615704 - 0.622734i        [I12, I13]
Om_GR(n=1) = 7*(0.346711 - 0.273915i) = 2.426977 - 1.917405i        [I12, I13]
|Om_GR(n=0) - Om_GR(n=1)| = 1.3083542634814167
```

**(b) Upper constraint — the nearest OTHER object in the prior-lane data.** The only other root v2.1 located over its rectangle is the artifact `Ω_art` (I17):

```
|Omega_0 - Omega_art| = 2.127881506829584
```

**(c) Lower constraints.** `|Ω_0| = 2.1096454365285577`. The frozen dedupe radius is `1e-6` relative, i.e. `2.1096e-06` absolute; the G2 root-drift tolerance is `1e-10` relative, i.e. `2.1096e-10` absolute.

**FROZEN CHOICE:**

```
R_iso = 0.5      (absolute, in Omega units; ENGINEERING CHOICE, tagged)
```

| receipt | value | reading |
|---|---|---|
| `1.3083542634814167 / R_iso` | `2.6167085269628334` | a genuine overtone at GR-like `ℓ=2` spacing sits **2.62×** outside the annulus and does **not** trip the gate |
| `2.127881506829584 / R_iso` | `4.255763013659168` | the nearest other prior-lane located object sits **4.26×** outside the annulus |
| `R_iso / \|Ω_0\|` | `0.23700665113790634` | the annulus is a **23.7 %** relative exclusion zone — a substantive separation statement, not a hair's breadth |
| `R_iso / (1e-6·\|Ω_0\|)` | `237006.65113790636` | the annulus is **2.37e5 ×** the dedupe radius, so the gate is not a restatement of dedupe |

Frozen: `the isolation radius is R_iso = 0.5 absolute in Omega units, chosen as an ENGINEERING CHOICE bounded ABOVE by the GR ell=2 fundamental-to-first-overtone spacing of 1.3083542634814167 in the same units (so a genuine overtone does not trip the gate) and by the 2.127881506829584 distance to the nearest other root in the v2.1 shipped data, and bounded BELOW by the 1e-6 relative dedupe radius; it is frozen once, is not adjusted after any measurement, and if it fires the lane reports ROOT-NOT-CERTIFIED`.

**What G5 counts (frozen).** Frozen: `G5 counts the eigenvalues of the double-precision linearized quadratic pencil of the SAME operator at the SAME order, deduped at the frozen 1e-6 relative radius, that lie within R_iso of the polished root at that order; the count must be EXACTLY ONE at every order of the FULL frozen ladder n in {32, 48, 64, 80, 96}, INCLUDING n = 32`.

### §4.4 ★ THE ONE CHANGE, DERIVED: G2's CERTIFICATION LADDER AND THE G2b FLOOR

> **DISCLOSURE, so the derivation is auditable and its risk is owned.** Every number in this subsection is arithmetic on **already-published prior-lane receipts** — I20 (the v2.1 coefficient tail) and I21 (v2.2's shipped convergence diagnostic). **No v2.3 instrument was built, run or consulted to produce any of them, and no eigenvalue of the v2.3 operator existed when this document was frozen.**

#### (a) Where the ladder's lowest rung goes, and why it is DERIVED rather than chosen

The `n`-independence gate asks: *does the root move as the representation is refined?* That question is only meaningful **where the representation actually represents the problem**. The pre-existing measurement of exactly that (I20, `research/2026-08-03_coldq-pole-v2.1_prereg-FROZEN.md:489` @ `7d8fe484`) is:

```
the Chebyshev coefficient tail of the operator's C coefficient falls to 5.3e-16 by n = 40
```

**Therefore the lowest rung of the certification ladder must sit at or above `n = 40`.** The frozen ladder's next available rung above `40` is `48`, which is also the primary order, so:

```
G2 certification ladder  =  {48, 64, 80, 96}          (every rung >= 40)
G2 tolerance             =  1e-10                      (UNCHANGED from v2.2)
```

Frozen: `G2's certification ladder is n in {48, 64, 80, 96}, DERIVED as the rungs of the full frozen ladder that sit at or above the n = 40 order at which the pre-existing v2.1 receipt measures the Chebyshev coefficient tail at 5.3e-16; the tolerance stays 1e-10, unchanged from v2.2, and is NOT loosened`.

**The knowable-at-freeze test applied to THIS document.** v2.2's defect was that its own frozen file contained the evidence against its own ladder. **This document is checked against that failure mode explicitly: the receipt is quoted in §S.3, its exact location is verified by two methods, its timestamp is compared to v2.2's, and the derivation above uses no other input.** If a reader finds a statement in this file that contradicts this ladder, that is a defect of the same class and it should be reported as such.

#### (b) The `n = 32` rung is RETAINED, not deleted — the three roles, frozen

Frozen: `the n = 32 rung is RETAINED in this lane in three roles: (i) as a GATED rung of G4(b), G5, FT-5(a) and FT-5(b), which sweep the FULL frozen ladder n in {32, 48, 64, 80, 96} unchanged from v2.2; (ii) as a REPORTED, NON-GATED DIAGNOSTIC row of G2 itself, shipping the n = 32 root, its relative separation from the certification ladder, and the max pairwise separation over the full five-rung ladder; (iii) as a pre-registered expectation of approximately 1.25e-10 whose failure to appear would itself be reported; NO measurement is hidden and the diagnostic row is mandatory in the result doc's gate table`.

**Why this is not "leaving the bad rung out".** If the lane simply dropped `n = 32`, the certification would rest on an absence. It does not: `n = 32` is still **gated** by four other measurements, and the one gate it is removed from is the only gate whose semantics require an asymptotically-converged basis. **A reader who believes `n = 32` belongs in G2 can read the diagnostic row and apply the v2.2 criterion themselves; the number is right there.**

#### (c) The G2b floor, derived from I21 with an order of headroom

A convergence ladder that merely *stays inside a tolerance* is a weaker statement than one that *converges geometrically*. The distinction is exactly the one v2.2's post-hoc diagnostic drew and that this lane promotes to a **pre-registered gate**: a spectrally-convergent representation's error against the finest rung falls geometrically; **a migrating pseudo-pole's does not.**

Define, over the G2 certification ladder with the finest rung as reference:

```
e(n)  =  |Omega_star(n) - Omega_star(96)| / |Omega_star(96)|     for n in {48, 64, 80}
r1    =  e(48) / e(64)
r2    =  e(64) / e(80)
```

**The floor's derivation from I21.** v2.2's shipped diagnostic measured these same two ratios (its §2.2 table) as:

| ratio | v2.2 measured (I21) | ratio ÷ a floor of `50` |
|---|---|---|
| `e(48)/e(64)` | `690.97` | `13.8194` |
| `e(64)/e(80)` | `403.39` | `8.0678` |
| *(out-of-ladder, for context only)* `e(32)/e(48)` | `1544.6` | `30.892` |

The **worst** ratio inside the certification ladder is `403.39`. **The floor is frozen at `50`, a factor of `8.0678` below the worst prior-lane measured ratio** — deliberate headroom, on the same principle every other tolerance in this arc is set by: far enough from the measured evidence that a small platform or transcription difference does not trip it, close enough that a **flat** error profile cannot pass.

```
G2b floor  =  50      (dimensionless ratio; ENGINEERING CHOICE, tagged, I19)
```

Frozen: `G2b requires that over the G2 certification ladder n in {48, 64, 80, 96}, with e(n) the relative separation of Omega_star(n) from Omega_star(96), each successive ratio e(48)/e(64) and e(64)/e(80) is >= 50; the floor 50 is an ENGINEERING CHOICE derived from the v2.2 shipped diagnostic whose worst in-ladder ratio was 403.39, i.e. the floor sits a factor of 8.0678 below the worst prior-lane measured ratio; if a denominator is exactly zero the ratio is recorded as infinite and treated as satisfying the floor, and that convention is frozen here rather than decided later`.

**★ THE HONEST LIMIT OF G2b, STATED BEFORE IT RUNS.** G2b is **not** a rung-exclusion device and it does not retroactively justify the ladder change: `e(32)/e(48) = 1544.6` **also** clears the floor, so G2b would have passed on the five-rung ladder too. **What G2b adds is a positive statement — "the errors fall geometrically, which is what a resolving spectral method does and what a migrating pseudo-pole does not" — where the ladder change alone would only have removed a rung.** Frozen: `G2b is a SHAPE statement about convergence and is NOT evidence that removing n = 32 was correct; the v2.2 diagnostic shows the n = 32 rung's own ratio also clears the floor, and that is stated here at freeze time so a passing G2b cannot later be presented as vindicating the ladder change`.

**The independent-of-the-audit property.** G2b is measured **by this lane, as a gate, on this lane's own roots**. If the concurrent PR #856 audit refutes the under-resolution attribution — if the `n = 32` excess is contamination — then the certification-ladder errors would be expected to stagnate rather than fall geometrically, and **G2b fails and this lane reports `ROOT-NOT-CERTIFIED` on its own evidence.** That is why G2b exists and why it is a gate rather than a diagnostic.

#### (d) The artifact ratio measurement — pre-registered as a DIAGNOSTIC, explicitly NOT a gate

The same ratio routine is additionally pointed at the v2.1-banked discretization artifact `Ω_art` (I17) over the same ladder, and its ratios are shipped. **This is pre-registered here, before any run, as a NON-GATING diagnostic** — deliberately, so that it is neither a post-hoc addition (v2.2's §2.2 diagnostic was added after its outcome was seen, and said so) nor a gate whose outcome cannot be derived at freeze time without scouting.

Frozen: `the artifact-centred successive-error ratios are a PRE-REGISTERED, NON-GATING DIAGNOSTIC; they are shipped and reported, they enter no gate and no bin, and no certification outcome depends on them`.

### §4.5 ★ TOOL-QUALITY CHANGE, DISCLOSED PRE-MEASUREMENT: the gating number check implements the #854 routed fixes

**Not a physics change, and disclosed here so it is on the record before any number is produced.**

The PR #854 docket fragment `_orchestration/docket-entries/2026-08-03-coldq-pole-v2.md` (@ `53bdd90f`) recorded two defects in that lane's result-doc number checker and **routed them to the successor rather than changing gating logic after a result**, verbatim:

> **"ROUTED TO THE v2.2 CHECKER AS A NAMED SUCCESSOR ITEM, NOT CHANGED HERE:** a **minimum significant-digit floor (≈`3`) below which a token must be allow-listed rather than matched**, and **per-site rather than global dedup**. **It is not changed here because that is gating logic, and changing gating logic after the result is exactly the post-result move Rule 11 forbids**"

**This lane is the successor that implements them, and it implements them BEFORE its own result exists.** Frozen: `this lane's gating number check implements the two fixes routed by the PR #854 docket: (i) a MINIMUM SIGNIFICANT-DIGITS FLOOR of 3, below which a numeral token may NOT be registered against the shipped JSON and MUST be allow-listed with a stated reason, machine-enforced so that a low-digit token cannot be silently counted as machine-tied; and (ii) PER-SITE rather than global dedup, so that every occurrence of a numeral in the result doc is checked rather than only its first occurrence, and the reported counts describe SITES not distinct tokens`.

**What the change buys and what it does not, stated honestly.** The sig-digit floor removes a real attribution defect: a one- or two-digit token "registering" against an unrelated JSON value is not machine-tied to anything, and counting it as registered overstates how much of a document is checked. Per-site dedup makes the reported counts describe the document rather than its distinct-token set. **Neither change can make a wrong number look right; both can only move tokens from `registered` to `allow-listed` and raise the site count.** The result doc reports the counts under the new rules, and the two rule changes are named there.

---
## §5 — THE ROOT-LOCAL CERTIFICATION GATES (G0–G10, plus G2b), with FROZEN numeric tolerances

**Every gate below is ROOT-LOCAL: it is a measurement on the root, on its eigenfunction, or on the discrete spectrum in a frozen neighbourhood of it. No gate integrates, counts or winds over a region.**

**Definitions used below, frozen.**
`Omega_star(n, lam, x_sat, dps)` = the mp-polished root at that setting, seeded from the double-precision linearized-pencil eigenvalue nearest the frozen seed `Ω_0`.
**The CERTIFIED ROOT** = `Omega_star(48, 0.0, 7.0, 50)`.
**The CERTIFIED EIGENFUNCTION** = the vector returned by `4` rounds of mp inverse iteration on the row-equilibrated `M(Omega_star(48, 0.0, 7.0, 50))` at `dps = 50`, started from the all-ones vector, infinity-normalized after each round.
**The FULL frozen ladder** = `n ∈ {32, 48, 64, 80, 96}`. **The G2 CERTIFICATION ladder** = `n ∈ {48, 64, 80, 96}`.

| Gate | What it certifies | FROZEN criterion |
|---|---|---|
| **G0** | **Operator-transcription identity** — the `η`-form is the `A`-form, as algebra | `the eta-form operator agrees with 4*eta^2 times the A-form operator to <= 1e-13 relative on the frozen set of arbitrary analytic test functions, over lambda in {-0.25, 0, +0.25}, ell in {2, 3} and Omega in {0.9-0.3i, 2.5-1.1i, 14.0-6.0i}` |
| **G1** | **Residual of the certified eigenfunction at the certified root** | `the infinity-norm residual max_i \|(M(Omega_star) psi)_i\| / max_i \|psi_i\| of the CERTIFIED EIGENFUNCTION on the row-equilibrated mp operator at dps = 50 is <= 1e-20` |
| **G2 ★** | **`n`-INDEPENDENCE of the root across the CERTIFICATION ladder** (**THE ONE CHANGED SPEC**) | `the maximum pairwise relative separation of Omega_star(n, 0.0, 7.0, 50) over the G2 certification ladder n in {48, 64, 80, 96} is <= 1e-10` |
| **G2b ★** | **GEOMETRIC-CONVERGENCE SHAPE across the certification ladder** (**NEW**) | `over the G2 certification ladder n in {48, 64, 80, 96}, with e(n) the relative separation of Omega_star(n, 0.0, 7.0, 50) from Omega_star(96, 0.0, 7.0, 50), each successive ratio e(48)/e(64) and e(64)/e(80) is >= 50` |
| **G3** | **Hyperboloidal-gauge independence** | `the maximum pairwise relative separation of Omega_star(48, lam, 7.0, 50) over lam in {-0.25, 0.0, +0.25} is <= 1e-12` |
| **G4** | **Precision and arithmetic-path independence** | `(a) \|Omega_star(48, 0, 7, 80) - Omega_star(48, 0, 7, 50)\| / \|Omega_star(48, 0, 7, 50)\| <= 1e-25, AND (b) at every order of the FULL frozen ladder n in {32, 48, 64, 80, 96} the double-precision linearized-pencil eigenvalue nearest the frozen seed agrees with the mp-polished root at that order to <= 1e-6 relative` |
| **G5 ★** | **ISOLATION — the root is locally separated from the discretization's pseudo-spectrum** | `G5 counts the eigenvalues of the double-precision linearized quadratic pencil of the SAME operator at the SAME order, deduped at the frozen 1e-6 relative radius, that lie within R_iso of the polished root at that order; the count must be EXACTLY ONE at every order of the FULL frozen ladder n in {32, 48, 64, 80, 96}, INCLUDING n = 32` |
| **G6** | **Two-instrument agreement** — this file's transcription against v1's different-in-kind instrument | `the certified root agrees with the v1 root reconstructed programmatically from research/drivers/coldq_pole_derivation_results.json row x_sat = 7.0 as x_sat*(omega_R_M - i*omega_I_M) to <= 1e-5 relative` |
| **G7** | **Spin-2-vs-spin-1 discrimination AT THE ROOT** — one measurement on the eigenvalue, one on the eigenfunction | `(a) replacing the spin-2 traction-free wall row by the spin-1 wall condition W'(r_sat) = 0 MOVES the root by >= 1e-3 relative, AND (b) replacing the spin-2 (ell-1)(ell+2) angular weighting by the spin-1 ell(ell+1) weighting in the mode-energy functional evaluated on the CERTIFIED EIGENFUNCTION changes the window-integrated strain-to-kinetic energy ratio by >= 1e-3 relative` |
| **G8** | **`nu_vac` cancellation AT THE ROOT, measured in mp end-to-end** | `across x_sat in {5, 7, 11} the mp-computed relative spreads of Q = Re(Omega)/(2*abs(Im(Omega))) and of abs(Omega) are each <= 1e-9, and omega_R*M_g = Re(Omega)/x_sat scales as 1/x_sat to <= 1e-9 relative; no value on the path from the polished root to these spreads is cast to a double-precision complex` |
| **G9** | **Determinism** | `two independent full driver runs produce an identical results digest (SHA-256 over the results object minus timing fields)` |
| **G10** | **Ax-3 reality / passivity ON the certified eigenfunction's own operator** | `(a) the row-equilibrated mp operator at n = 48 and every lam in {-0.25, 0.0, +0.25} has max\|Im M0\|/max\|M0\|, max\|Im M2\|/max\|M2\| and max\|Re M1\|/max\|M1\| each <= 1e-40, AND (b) the conjugate-mirror root polished from the seed -conj(Omega_star) satisfies \|Omega_mirror + conj(Omega_star)\| / \|Omega_star\| <= 1e-20` |

### The mandatory NON-GATED diagnostic row

Frozen: `the n = 32 rung is reported as a NON-GATED DIAGNOSTIC row of G2, shipping its polished root, its relative separation from every rung of the certification ladder, and the maximum pairwise relative separation over the FULL five-rung ladder n in {32, 48, 64, 80, 96}, tagged PRE-ASYMPTOTIC BY THE v2.1 n = 40 COEFFICIENT-TAIL RECEIPT -- REPORTED, NOT GATED; the result doc MUST print this row in its gate table, and the certification outcome does NOT depend on it`.

### Why G10(b) is the Ax-3 statement and not decoration

With a **real, lossless** constitutive law the `η`-form matrices satisfy `M0, M2` real and `M1` purely imaginary (`ℬ ∝ 4iη(1 − λA²)`, `𝒞`'s `Ω`-linear part `∝ 4iA/(2−η²)·(…)`), so `conj(M(−conj(Ω))) = M(Ω)` **identically** and the spectrum is symmetric under `Ω → −conj(Ω)`. That symmetry is the frequency-domain form of *"the time-domain equation has real coefficients"* — i.e. of *"the medium stores and does not dissipate; all the loss is the radiative port"*. **Smuggling any `Im(μ) ≠ 0` puts an imaginary part into `M2` and breaks it.** G10(a) checks the matrix structure; G10(b) checks the consequence on the certified root. FT-10 breaks both with one mutation.

### Certification classes (exhaustive, frozen)

- **`ROOT-CERTIFIED`** — `all of G0, G1, G2, G2b, G3, G4, G5, G6, G7, G8, G9 and G10 PASS and all of FT-0, FT-1, FT-2, FT-2b, FT-3, FT-4, FT-5, FT-6, FT-7, FT-8, FT-9 and FT-10 FIRE`.
- **`ROOT-NOT-CERTIFIED`** — `any gate FAILS, OR any self-test fails to fire`. **A gate that cannot fail voids the certification exactly as hard as a gate that fails.** Under this class **no physics bin is adjudicated** (§7 precedence).

**There is no scoped or partial class in this lane.** Frozen: `this lane has exactly two certification classes, ROOT-CERTIFIED and ROOT-NOT-CERTIFIED; there is no scoped, partial or provisional certification, and a gate that passes only over a reduced parameter set is a FAIL`.

**Rule-11 fence on the method itself, frozen and binding.** Frozen: `no gate, tolerance, frozen numeric parameter or method element in sections 4 and 5 may be changed after any gate result is seen; if this instrument fails certification the lane reports ROOT-NOT-CERTIFIED and routes to its own successor with a new version number, exactly as #845 routed to v2, v2 to v2.1, v2.1 to v2.2 and v2.2 to v2.3`.

**★ AND THE FENCE'S SHARPEST EDGE, WRITTEN FOR THIS LANE SPECIFICALLY.** This lane exists because a predecessor changed nothing after seeing a result and routed instead. Frozen: `if G2 fails on the certification ladder n in {48, 64, 80, 96}, or if G2b fails, the ladder is NOT changed again, no rung is added or removed, the floor is NOT lowered, and the lane reports ROOT-NOT-CERTIFIED; a second ladder repair in the same arc would be parameter selection under a frozen fence and is forbidden here in advance`.

---

## §6 — GATE-FIREABILITY SELF-TESTS (FT-0 … FT-10, plus FT-2b) — each MUST FIRE, each demonstrated on a MUTATED input BEFORE the real gate is read

**The rule (frozen).** Frozen: `a gate that cannot fail is not a gate; if any self-test fails to fire, the certification is ROOT-NOT-CERTIFIED regardless of how many gates passed`.

**The ordering rule (frozen).** Frozen: `every self-test is executed and recorded BEFORE its target gate's own measurement is read in the results object, and each self-test's mutation is shown here to be NON-VACUOUS against the object it mutates by an algebraic argument stated at freeze time, not by running`.

| # | Targets | Deliberate mis-specification | FROZEN firing criterion | Why the mutation is NON-VACUOUS (algebra, stated at freeze) |
|---|---|---|---|---|
| **FT-0** | **G0** | corrupt the `𝒞₀` coefficient by `1e-12` relative | `the corrupted eta-form coefficient MUST break the operator identity by >= 1e-13 relative` | `𝒞₀ = −4ℓ(ℓ+1)η² − 8A²/(2−η²)` is `O(1)` on the interior nodes and appears with unit weight in `𝓛_η`, so a `1e-12` relative corruption is a `~1e-12` relative change in the identity's residual — one order above the gate |
| **FT-1** | **G1** | evaluate the residual of the CERTIFIED EIGENFUNCTION on `M(Omega_star·(1 + 1e-10))` instead of `M(Omega_star)` | `the off-root residual MUST be >= 1e-15` | the residual is `≈ σ_min(M(Ω))`, and `dσ_min/dΩ` is `O(1)` for a simple root, so a `2.1e-10` absolute displacement produces an `O(1e-10)` residual — five orders above the threshold and ten above the gate |
| **FT-2** | **G2** | add `n = 8`, far below every order of either ladder | `the under-resolved order MUST deviate from Omega_star(48, 0, 7, 50) by >= 1e-6 relative` | at `n = 8` the Chebyshev basis cannot represent the coefficient functions, whose measured tail (I20) only reaches `5.3e-16` by `n = 40`; v2.1's FT-C and v2.2's FT-2 each measured `4.4038e-04` for exactly this mutation |
| **FT-2b ★** | **G2b** | **STAGNATION:** replace `Omega_star(n)` by `Omega_star(n) + 1e-12` at every NON-reference rung of the certification ladder (the `n = 96` reference is left untouched), then recompute the ratios | `the stagnation mutation MUST drive EVERY successive ratio BELOW the frozen floor of 50` | the true absolute rung differences from v2.2's shipped receipts (I21) are `1.7068e-13`, `2.4701e-16` and `6.1233e-19` (`e(n)·\|Ω\|` with `\|Ω\| = 2.1096454365285577`), **every one of them smaller than the injected `1e-12`** — the smallest margin being a factor of `5.858` at `n = 48`. So every mutated `e(n)` collapses to `≈ 1e-12/\|Ω\|` and every ratio collapses to a number between `0.829` and `1.171`, **at least `42×` below the floor even in the worst phase alignment.** The mutation is a POST-SOLVE perturbation of recorded values, the same class as FT-9's digest probe, and that class is disclosed rather than implied |
| **FT-3** | **G3** | **a CORRECTLY-SPECIFIED half-applied gauge**: carry `λ` into `ℬ₁` and `𝒞₁` but OMIT the `λ` terms from `𝒞₂`, i.e. use `𝒞₂ = 4η/(u(1+S))` and drop `+8η²λ − 4η²λ²A²` | `the gauge-omission mutation MUST make the G3 pairwise spread exceed 1e-6` | the omitted terms are `8η²λ − 4η²λ²A²`, which at `λ = +0.25` equal `2η² − 0.0625·4η²A²`, an `O(1)` quantity at `η → 1` — the mutation is NOT a no-op and NOT the logical negation of G3 |
| **FT-4** | **G4** | (a) run the mp operator at `dps = 20`; (b) build the double-precision pencil at `n = 8` while the mp root is at `n = 48` | `(a) the dps = 20 root MUST differ from the dps = 50 root by >= 1e-25 relative, AND (b) the mismatched-order double-vs-mp cross-check MUST exceed 1e-6 relative` | (a) `dps = 20` truncates every operator entry at `~1e-20` relative and the equilibrated Chebyshev operator's conditioning at `n = 48` is `O(n⁴) ≈ 5e6`, so the root moves by `~1e-14` — eleven orders above the threshold; (b) `n = 8` is the same under-resolution FT-2 uses |
| **FT-5 ★** | **G5** | run the identical isolation measurement centred on **(a)** the v2.1-banked discretization artifact `Ω_art` (I17) and **(b)** the v2.1 C9 probe point `Ω_edge = 0.1400 − 3.5035i` inside the contaminated left edge (I18), instead of on the certified root, over the FULL frozen ladder | `case (a) MUST return a count different from exactly one at at least one order of the FULL frozen ladder, OR a polished n-drift above the G2 tolerance at those orders; AND case (b) MUST return a count different from exactly one at at least one order of the FULL frozen ladder` | (a) `Ω_art` is banked by v2.1's OWN frozen physical-vs-artifact criterion as absent at some `n` in `{48, 56, 64}` within `1e-6` relative, so it cannot be both isolated and `n`-stable across a ladder containing three of those orders; **the OR is deliberate — the artifact must fail EITHER isolation OR stability, and which one it fails is reported, not chosen.** (b) `Ω_edge` sits where the PR #854 audit measured a migrating spectrum whose in-box count runs `2 → 9` over `n = 32 → 80`, so a count of exactly one there at every order would itself contradict `0a7dec1f` |
| **FT-6** | **G6** | corrupt the `𝒞₀` coefficient by `1e-3` relative and compare THAT root against the v1 comparator | `the corrupted-operator root MUST disagree with the v1 comparator by >= 1e-5 relative` | a `1e-3` relative change in an `O(1)` coefficient of the eigenvalue problem moves the eigenvalue by `O(1e-3)` relative — two orders above G6's tolerance |
| **FT-7** | **G7** | **REVERSE fireability (stated as such):** run both discriminators between IDENTICAL specifications — spin-2 wall against spin-2 wall, and spin-2 weighting against spin-2 weighting | `both null-mutation differences MUST be below 1e-3, demonstrating that G7's discriminator does not manufacture a difference between identical specifications` | G7's pass condition is a LARGE difference, so its failure mode is a small one; the correct fireability demonstration is a configuration in which the measurement returns small. Both null mutations are exact identities and must return `0` up to arithmetic |
| **FT-8** | **G8** | inject the `x_sat`-dependent profile perturbation `A -> A*(1 + 1e-6*(x_sat - 7)/7)` | `the x_sat-dependent perturbation MUST make the G8 spread exceed 1e-9` | the perturbation is identically zero at `x_sat = 7` and `±1.43e-06` relative at `x_sat = 5, 11`, so it breaks the scale invariance the gate measures without touching the primary run; v2.1's FT-E and v2.2's FT-8 each measured `6.0137e-07` for exactly this mutation |
| **FT-9** | **G9** | perturb one recorded gate value by `1e-15` relative in a COPY of the results object and re-digest | `the perturbed copy MUST produce a different digest` | SHA-256 over the serialized object; the demonstration is that the digest actually covers the gate payload rather than a header |
| **FT-10** | **G10** | smuggle loss `Im(mu)/Re(mu) = 1e-3` into the modulus, which enters the `η`-form only through the `Ω²ρ/μ` term of `𝒞₂` | `(a) the lossy operator MUST return max\|Im M2\|/max\|M2\| >= 1e-6, AND (b) the lossy conjugate-mirror residual MUST be >= 1e-5` | a constant complex factor on `μ` leaves `ĝ = μ′/μ` and the wall condition `ψ_η(0) = 0` unchanged and changes ONLY `𝒞₂`'s first term `4η/(u(1+S)) → 4η/(u(1+S)(1+iδ))`, giving `Im 𝒞₂/Re 𝒞₂ ≈ −δ = −1e-3`; the conjugate-mirror symmetry proof of §5 requires `M2` real, so it breaks at the same order |

---
## §7 — THE FROZEN PHYSICS BINS — adjudicated IFF ALL GATES PASS

**Every boundary in this section is byte-identical to v2.2's (`f15a6e4d` §7), which was byte-identical to v2.1's (`7d8fe484` §7), which inherited them from v2 (`00724432`) and v1. Not one is re-derived, adjusted, widened or narrowed here.**

**Rule-11 fence, stated up front and binding.** Frozen: `no adjudication criterion below may be dropped, widened or re-defined after any result is seen; no input in the section 3 ledger may be retuned; whatever the instrument returns is banked`. There is **no free parameter to tune** — that is the point of the lane.

**PRECEDENCE (frozen, evaluated in this order).** `BIN-F-NOROOT` > `BIN-F-ROOT` > `BIN-F-PROFILE` > `BIN-1/2/3`. If an earlier bin fires, the later ones are reported as `N/A — not adjudicated` and **no verdict language is used about them.** `BIN-4` is `N/A BY CONSTRUCTION` **at every precedence level, including a full pass** (§7.5).

### §7.1 Honest-failure bins (each reachable, each with a disposition)

| bin | condition | disposition |
|---|---|---|
| **`BIN-F-NOROOT`** | `the double-precision linearized pencil at n = 48 has no eigenvalue within R_iso of the frozen seed, or the mp polish from that seed fails to converge` | **A clean negative and a GOOD outcome.** It would say the object v1, v2.1 and v2.2 all located is not present in this carry-over of the same formulation — which would be a decisive statement about the carry-over. Banked as such; no bin adjudicated; routed to Grant and the auditor lane. |
| **`BIN-F-ROOT`** | `any gate FAILS or any self-test fails to fire` | **`ROOT-NOT-CERTIFIED`.** No physics bin adjudicated; the failing gate's numbers are reported; the lane returns the instrument failure as its result. No claim, no walk-back, no solidity change, **and no retune** — it routes to its own successor with a new version number. |
| **`BIN-F-PROFILE`** | `the canonical input set of section 3 is found to be internally inconsistent at solve time (two canonical statements that cannot both hold on the domain)` | **flag-don't-fix.** Both file paths + verbatim content surfaced to Grant and the auditor lane; **neither side reframed to match the other**; no bin adjudicated. |

### §7.2 BIN-1 — the real part `ω_R M_g`

`D_omega ≡ omega_R_derived / omega_R_GR − 1`, with `omega_R_GR = 0.37367` read programmatically from the frozen `KERR_QNM[0.00]` row (I11, `research/2026-07-20_v1-spin-mapping-adjudication_rerun.py:51`).

| sub-bin | FROZEN criterion |
|---|---|
| **`BIN-1-MATCH`** | `abs(D_omega) < 0.03` |
| **`BIN-1-NEAR`** | `0.03 <= abs(D_omega) < 0.10` |
| **`BIN-1-MISS`** | `abs(D_omega) >= 0.10` |

Reported alongside, **not a separate class**: `D_omega_shortcut ≡ omega_R_derived/(18/49) − 1`, the deviation from the standing corpus shortcut `18/49 = 0.36735`; and the sign of both. **Class line (mandatory in the result headline):** `BIN-1 is VALUE-CONSISTENCY class, not emergence: omega_R*M_g carries the GR-imported nu_vac through the 7 in r_sat`.

**The `(1+ν_vac)` rider, frozen:** `if BIN-1's derived omega_R*M_g deviates from 18/49 by more than 3 percent, the standing chain's r_eff = r_sat/(1+nu_vac) assertion is FALSIFIED as a derivation of the eigenfrequency, and that is a GOOD outcome recorded as such`.

**The advance identity, restated so two readings of one result cannot be presented as two results.** Frozen: `k_0*r_sat = x_sat * omega_R M_g identically, so the 9/7-above-cutoff test IS the omega_R versus 18/49 comparison re-expressed and is NOT an independent axis`.

### §7.3 BIN-2 — the quality factor `Q` (★ the `ν_vac`-free, emergence-capable axis)

`Q_derived ≡ Re(Omega)/(2*abs(Im(Omega)))`; `Q_GR ≡ 0.37367/(2*0.08896) = 2.1002135791366907` from the same frozen row; `D_Q ≡ Q_derived/Q_GR − 1`.

| sub-bin | FROZEN criterion |
|---|---|
| **`BIN-2-MATCH`** | `abs(D_Q) < 0.03` |
| **`BIN-2-NEAR`** | `0.03 <= abs(D_Q) < 0.10` |
| **`BIN-2-MISS`** | `abs(D_Q) >= 0.10` |

**And the three-way discriminator, frozen separately** (the axis that decides whether the substrate prefers GR's value or the corpus's `2π`-convention `Q = ℓ = 2`):

| sub-bin | FROZEN criterion |
|---|---|
| **`BIN-2-CLOSER-GR`** | `abs(Q_derived - Q_GR) < abs(Q_derived - 2.0)` |
| **`BIN-2-CLOSER-CONVENTION`** | `abs(Q_derived - 2.0) < abs(Q_derived - Q_GR)` |
| **`BIN-2-EQUIDISTANT`** | `abs(abs(Q_derived - Q_GR) - abs(Q_derived - 2.0)) <= 1e-6` |

> **⚑ FLAG-1 CARRIED FORWARD UNCHANGED, and the discriminator's robustness to BOTH corpus values is frozen HERE rather than argued afterwards.** Two `Q_GR` values exist in the corpus: the programmatic `2.1002135791366907` from `KERR_QNM[0.00] = (0.37367, 0.08896)`, and the rounded-prose `2.099438202247191` from the pair `0.3737`/`0.0890`, carried verbatim at `research/2026-07-30_qlaw-derivation_scoping.md:401`. **Both are the same table at different precision.** The frozen source does not move — the programmatic value is used, exactly as v1, v2.1 and v2.2 used it — and the robustness is stated as a *criterion*, not as a *reassurance*:
>
> - **`abs(D_Q)` bins.** The two comparators differ by `0.0007753768895` — `0.037 %` of `Q_GR`, two orders below `BIN-2-MATCH`'s `0.03` boundary. **No `abs(D_Q)` sub-bin can flip.**
> - **The three-way discriminator.** Its crossover is the midpoint between the comparator and `2.0`: `2.0501067895683455` for the programmatic value and `2.0497191011235955` for the rounded one, a window of width `0.00038768844`. **Only a `Q_derived` landing INSIDE that window could be flipped by the choice of comparator.**
>
> Frozen: `the BIN-2 three-way discriminator is robust to the FLAG-1 comparator ambiguity unless Q_derived lands inside the window between 2.0497191011235955 and 2.0501067895683455; the result doc MUST report whether it does, and if it does the discriminator is reported as AMBIGUOUS rather than adjudicated`.

**Class line (mandatory in the result headline):** `BIN-2 is the nu_vac-FREE axis: Q = Re(Omega)/(2*abs(Im(Omega))) contains no r_sat scale, so the GR-imported 7 cancels exactly`.

### §7.4 BIN-3 — where the mode actually lives (FORK-1, handed to the substrate)

Frozen observable: `u ≡ r_peak/r_sat`, where `r_peak` maximizes the frozen spin-2 mode-energy density `E(r) = rho|omega|^2|W|^2 r^2 + mu(|W' - W/r|^2 + (ell-1)(ell+2)|W|^2/r^2) r^2` over the frozen window `r/r_sat in [1.0, 2.0]`, evaluated on the CERTIFIED EIGENFUNCTION. A second, independent measure `u_kin` uses the kinetic term alone.

| sub-bin | FROZEN criterion |
|---|---|
| **`BIN-3-RIM`** | `1.00 <= u <= 1.10` — the mode hugs the wall; the rim-ring reading |
| **`BIN-3-RAMP`** | `1.10 < u <= 1.50` — the mode sits in the stiffness ramp. Sub-flag `BIN-3-RAMP-TURNING-POINT` if additionally `abs(u - 1.2247) <= 0.05` |
| **`BIN-3-OUTER`** | `u > 1.50` — neither standing picture locates the mode |
| **`BIN-3-MONOTONE`** | `the energy density has no interior maximum in the frozen window (the maximum sits at an endpoint)` — localization is not a well-posed observable for this mode; the endpoint is reported |
| **`BIN-3-DISCORDANT`** | `abs(u - u_kin) > 0.10` — the two frozen measures disagree; both are reported and no localization verdict is banked |

**The ill-posed sub-bin is PRESERVED, deliberately.** Frozen: `BIN-3-MONOTONE and BIN-3-DISCORDANT are preserved unchanged from v1, v2.1 and v2.2 so that an ill-posed or discordant localization reading lands in a pre-registered bin rather than in prose`.

### §7.5 BIN-4 — `N/A BY CONSTRUCTION`, declared in advance

Frozen: `BIN-4 is N/A BY CONSTRUCTION in this lane and is not adjudicated at any precedence level including a full gate pass; no overtone, no ladder, no mode count and no completeness statement is computed, and the deferral is an open instrument-scope question awaiting a substrate-derived low-frequency cutoff, not a failure of this lane`.

**This is a scoped non-claim, and the result doc is required to present it as one.** It is not `BIN-4-NONE` — that sub-bin asserted *"exactly one physical pole is located in the frozen rectangle"*, which is a **counting claim over a region** and is exactly what the PR #854 audit impeached and what §1.2 forbids. **`BIN-4-NONE`, `BIN-4-LADDER-MATCH` and `BIN-4-LADDER-DIFFERENT` are all unreachable in this lane by construction, and that is disclosed here rather than discovered later.**

### §7.6 Reachability audit (frozen)

- `BIN-F-ROOT` is reachable **and is demonstrated reachable every run**: every self-test drives an actual gate into its failing state (FT-7 by the reverse construction, stated as such).
- `BIN-F-NOROOT` is reachable: the pencil at `n = 48` either has an eigenvalue within `R_iso` of the seed or it does not.
- `BIN-F-PROFILE` is reachable: the canonical set carries live tensions this lane touches (#814 CF-7's unnamed `ρ` at `vol3/claim-quality.md:122`).
- `BIN-1/2/3` sub-bins are each reachable because each is an interval or a strict comparison on a continuously-valued measured quantity, and the intervals **partition** their axis with no gaps and no overlaps.
- `BIN-4`'s sub-bins are **deliberately unreachable**, disclosed in §7.5.
- **No outcome requires a criterion to be relaxed after the fact.**

### §7.7 ★ PREDICTABILITY DISCLOSURE — stated in advance so no bin outcome can later be presented as a blind prediction

**This lane knows, in advance and to several digits, where every bin will land if the gates pass — and says so here rather than after.**

v2.2 shipped these `NOT-ADJUDICATED` diagnostics at the same root, under a `ROOT-NOT-CERTIFIED` instrument (its result doc §5.1–§5.2, @ `982c4c9b`): `Ω = 1.8536552108408788 − 1.0072567831433188i`, `ω_R M_g = 0.2648078872629827`, `Q = 0.9201502744197102`, `u_energy = u_kinetic = 2.0000000000000004` with `interior_max = false`. **Anyone can compute where those fall in §7.2–§7.4, and this lane carries the same instrument, so it expects the same numbers.**

Frozen: `this lane's contribution is CERTIFICATION of an already-published prior-lane number under a repaired gate specification, not the discovery of a new one; the bin outcomes are predictable in advance from the v2.2 NOT-ADJUDICATED diagnostics and that predictability is disclosed here, so no bin outcome may be presented as a blind prediction and no headline may imply surprise`.

**And the honest reading of what that leaves.** The value of an adjudicated bin here is **not** that the number is new. It is that the number is produced by an instrument whose root-local behaviour has been gated end-to-end, so the bin verdict is a statement about the graded cavity rather than about an uncertified discretization. **That is a real difference and it is also a modest one, and both halves of that sentence belong in the result doc.**

---

## §8 — WHAT TRANSFERS, AND WHAT MUST BE RE-EARNED

**TRANSFERS (cited, not silently absorbed):**
- the **ratified physics framing** — the transmission-line reading, the graded profile, the SHORT at `r_sat`, the radiative port, the spin-2 channel, `Q` as a pole;
- the **compactified formulation** and its exact wall substitution, **as algebra re-verified by G0 every run**;
- the **shape** of the certification battery — frozen gates with numeric tolerances, self-tests that must FIRE, a determinism digest, an exhaustive outcome-class table with a reachability argument;
- the **frozen-first commit order**;
- the **bin boundaries**, byte-identical (§7);
- the **`x_sat`-generalized advance identity** `k₀ r_sat = x_sat · ω_R M_g`, minted in the v2.1 prereg §2.5 and cited as that lane's;
- **★ and, new in this lane and disclosed as such: the INSTRUMENT ITSELF, carried over from v2.2 by copy-with-attribution (§2.3).**

**DOES NOT TRANSFER — must be re-earned, and is (gate in brackets):**
- **the certification.** #845, #854 and #856 are all uncertified. Every gate is re-run on this file. [G0–G10, G2b]
- **v2.2's G2 result.** It stands as v2.2 banked it, on v2.2's ladder. This lane's G2 is a **different measurement on a different ladder** and does not overwrite it. [G2]
- **the pole-counting instrument.** Not re-earned; **not used at all** (§1.2).
- **any completeness statement.** Not re-earned; **abandoned as out of scope** (§7.5).
- **implementation independence.** **Explicitly NOT transferred and explicitly NOT claimed** (§2.3).

Frozen: `no gate, tolerance, certification class or measured number is inherited as PASSED from PR #845, PR #854 or PR #856; the physics framing, the compactified algebra, the bin boundaries and the instrument's method transfer, the certification does not, and every gate in section 5 is re-earned on this file`.

---

## §9 — SATISFIABILITY OF THE FROZEN REQUIREMENTS — DERIVED, WITH ZERO PRE-FREEZE COMPUTATION

> **★ DISCLOSURE.** **This lane ran NOTHING before this document was frozen.** No driver was written, no operator was assembled, no eigenvalue was computed, estimated, seeded or looked at. The only arithmetic performed before the freeze is the arithmetic of §4.3, §4.4 and §7.3 — **elementary arithmetic on already-published prior-lane values and frozen GR comparators** — which is reproduced by the driver and machine-checked by the number check.
>
> **The risk of that choice is disclosed and accepted:** a tolerance derived rather than scouted can be wrong, and if it is, the gate FAILS and this lane reports `ROOT-NOT-CERTIFIED`. **It will not be retuned.**

| gate | tolerance | where it comes from |
|---|---|---|
| **G0** `1e-13` | v2.1's C11 measured `8.9716e-16` and v2.2's G0 measured `1.0385e-15` on the same identity; `1e-13` sits ~2 orders above the worst prior evidence |
| **G1** `1e-20` | the polish terminates at `1e-38·\|Ω\|`, mp carries `50` digits, and the equilibrated operator's conditioning at `n = 48` is bounded by `O(n⁴) ≈ 5.3e6`, so an achievable residual floor is `~1e-40`; `1e-20` is frozen 20 orders above it. v2.2 measured `4.7268e-50` |
| **G2 ★** `1e-10` on `{48, 64, 80, 96}` | **UNCHANGED tolerance, DERIVED ladder.** v2.2's own shipped receipts bound the max pairwise separation over exactly this ladder by the triangle inequality at `1.6181e-13` — `618×` inside the frozen `1e-10`. The ladder's lower rung is placed by I20 (`5.3e-16` by `n = 40`), not by the outcome it produces |
| **G2b ★** ratio `>= 50` | derived in §4.4(c) from I21: the worst in-ladder ratio v2.2 measured is `403.39`, so the floor sits `8.0678×` below the worst prior-lane measured evidence |
| **G3** `1e-12` | v2.1's C2 measured `3.3268e-14` and v2.2's G3 measured `3.3323e-14` on the identical gauge set at the identical primary order; ~1.5 orders of measured margin |
| **G4(a)** `1e-25` | the polish's own termination is `1e-38` relative, so `dps = 50` and `dps = 80` cannot differ by more than `~1e-38`; `1e-25` is frozen 13 orders above. v2.2 measured `5.2778e-47` |
| **G4(b)** `1e-6` | v2.1's B1 disclosure measured the double-precision-operator floor at `2.73e-10 … 8.67e-08`; v2.2 measured `1.7559e-08` over the same full ladder including `n = 32`. `1e-6` is frozen about one order above the worst measured floor |
| **G5** `R_iso = 0.5`, count `== 1` | derived in §4.3 from four receipts, two upper constraints from physics and two lower from the instrument's own frozen numerics. v2.2 measured `[1, 1, 1, 1, 1]` on the full ladder |
| **G6** `1e-5` | the observed cross-lane agreement is `6.803232e-07`; `1e-5` is an ENGINEERING CHOICE with ~1.2 orders of headroom, so a rounding-level difference passes while a transcription error (FT-6 shows `O(1e-3)`) does not |
| **G7** `1e-3` | v2.1's FT-F(ii) measured the spin-1 wall condition moving the fundamental by `0.28424` and v2.2's G7(a) measured `0.28424`; `1e-3` is frozen ~2.5 orders below the measured effect |
| **G8** `1e-9` | v1's, v2.1's and v2.2's frozen tolerance, unchanged. v2.2's mp end-to-end measurement is `1.8619e-46`, ~37 orders inside the gate — which is why **FT-8 is mandatory**: without it this gate would be dead |
| **G9** identical digest | determinism has no tolerance |
| **G10(a)** `1e-40` | the quantities are exact zeros in mp by the structure argued in §5; the tolerance exists only to catch a structural transcription error, and **FT-10 supplies the fireability a zero-valued gate would otherwise lack** |
| **G10(b)** `1e-20` | both members of the mirror pair are polished to `1e-38` relative independently, so their symmetry residual is bounded by `~1e-38`; `1e-20` is frozen 18 orders above. v2.2 measured `9.2731e-47` |

**★ THE PRE-REGISTERED EXPECTATIONS, written so that a surprise is visible as a surprise.** Because this lane carries v2.2's instrument over, it expects — and states here, before running — that:

1. **the certified root reproduces** `1.8536552108408788 − 1.0072567831433188i`;
2. **the `n = 32` NON-GATED diagnostic reads** `≈ 1.2497e-10`, i.e. reproduces v2.2's failing G2 number;
3. **every unchanged gate reproduces v2.2's published value** at the precision v2.2 published it;
4. **G2 passes at `≈ 1.6e-13` or below**, and **G2b's ratios read `≈ 691` and `≈ 403`**.

Frozen: `these four expectations are stated BEFORE the run so that agreement is recorded as a REGRESSION CHECK and any disagreement is recorded as a DEFECT and surfaced with both numbers; no expectation is a gate, none may be used to adjust a measurement, and a disagreement is reported rather than reconciled`.

**Runtime.** v2.2's battery ran `256.15 s` and `254.41 s` inside the frozen `3600 s`. This lane adds one ratio computation on already-polished roots and one post-solve mutation, both negligible. A longer run is **disclosed, not silently accepted**.

**Mutual satisfiability of the gates (no gate contradicts another).**
1. **G2 and G2b probe different things and can disagree.** G2 asks whether the spread is small; G2b asks whether it is *shrinking geometrically*. A stagnating ladder at a small offset passes G2 and fails G2b — which is exactly the case FT-2b constructs.
2. **G2 and G5 probe different things and can disagree.** G2 asks whether the root moves with `n`; G5 asks whether anything else moves *toward* it. FT-5(a) is built on that independence.
3. **G3 and G4 probe genuinely different knobs.** `λ` changes the analytic prefactor and therefore every coefficient function; `dps` changes only the arithmetic.
4. **G6 does not presuppose G2.** A carry-over could be `n`-stable at the wrong place; G6 is the gate that would catch it, and FT-6 demonstrates it would.
5. **G7 and G10 are orthogonal.** G7 mutates the tensor rank; G10 mutates the losslessness.
6. **G8 does not presuppose G1.** `x_sat`-invariance is a statement about the arithmetic path; the residual is a statement about the solution.
7. **No gate's PASS condition is another gate's FAIL condition.** Checked explicitly, including the new pair: **FT-2b's firing condition (all ratios `< 50` under a stagnation mutation) is not G2b's failure condition (a ratio `< 50` unmutated) — they are measured on different value sets, one mutated and one not.**

---

## §10 — FLAGS RAISED AT FREEZE TIME (flag-don't-fix; surfaced, not resolved)

1. **⚑ FLAG-1 — the two `Q_GR` comparator values.** Fully stated in §7.3, with the robustness condition frozen as a criterion. The programmatic `2.1002135791366907` is frozen; the rounded-prose `2.099438202247191` at `research/2026-07-30_qlaw-derivation_scoping.md:401` is reported alongside. **Routed to the auditor lane as a corpus-precision question; not repaired here.**
2. **⚑ FLAG-2 — this lane DOES gate on a prior-lane number (G6), and the direction of inference is fixed in advance.** Frozen: `G6 gates THIS lane's transcription against a prior-lane comparator and certifies NOTHING about PR #845, which remains SOLVER-NOT-CERTIFIED; a G6 pass may not be reported as corroboration of #845, and no #845 number enters any bin, any other gate, or any comparator in this lane`.
3. **⚑ FLAG-3 — I7 is assumed, not tested.** The reflectionless Regime-I port at infinity is a **frozen canonical input**, and this lane's entire method divides out the corresponding analytic factor. If the substrate carries any far-field reflector, every number here is wrong in the same direction — **including the certified root.** Not tested here; routed. **A `ROOT-CERTIFIED` verdict does not touch this flag.**
4. **⚑ FLAG-4 — #814 CF-7's naming gap stands, untouched.** `vol3/claim-quality.md:122` writes `Z_{shear} = \rho\,c_{shear}` and never names which `ρ`. This lane consumes the leading reading (`ρ₀`, I5) as a frozen input and does **not** repair the leaf.
5. **⚑ FLAG-5 — the completeness question is OPEN.** The open item is: **derive a substrate low-frequency cutoff for the graded shear cavity.** Routed to Grant (§0) and to a successor lane; **not attempted, not sketched, not assumed here.**
6. **⚑ FLAG-6 — v2.1's I13 provenance is stale and the correction is recorded, not propagated.** Since PR #845 merged, `ω_I M (ℓ=2, n=1) = 0.273915` has an in-repo carrier at `research/drivers/coldq_pole_derivation.py:106`. **The v2.1 prereg is frozen and byte-untouched.**
7. **⚑ FLAG-9 CARRIED FORWARD FROM v2.2, UNRESOLVED — v1's `0.28430` is a CLAMPED-wall mutation, not the spin-1 one.** v1's FT-2 is `W(r_sat) = 0` (the `Γ = +1` alternative of #814 FORK-3(b)), verbatim at `research/2026-08-02_coldq-pole-derivation_prereg-FROZEN.md:229`; the spin-1 condition is a different row. v2.1's result-doc §5.4 places them in one row labelled *"spin-1 / clamped wall shift"*. **That row compares two different mutations.** Surfaced, not resolved, not repaired; the files of both other lanes are byte-untouched.
8. **★ ⚑ FLAG-10 — NEW: this lane's independence is WEAKER than v2.2's, by design, and the weakening is the price of the controlled comparison.** §2.3 states it in full: a carried-over instrument cannot corroborate itself. **A reader who wants implementation independence should read v2.2's G6, not this lane's.** The exterior-complex-rotation cross-check remains the genuinely independent third instrument, and it is **not built here** (§11).
9. **★ ⚑ FLAG-11 — NEW: the concurrent PR #856 audit is a live dependency of this lane's premise, and it had not reported at freeze.** Fully stated in §S.6 with the halt condition frozen. **This is the flag most likely to void this lane, and it is stated before any number exists.**
10. **⚑ FLAG-12 — the Makefile contact, disclosed at freeze time.** This lane's gating number check is wired as its **own** target; two single-line list appends (the `.PHONY` list and the `verify:` prerequisite list) and one `help` echo line are lines the concurrent PR #854 and PR #856 branches also append to. **This is an append-only textual contact, is disclosed here before any lane merges, and is for the orchestrator to sequence.** No physics, no gate and no result depends on it. **Every `research/` and `_orchestration/` file in this lane is new and shared with no open branch.**

---

## §11 — LEDGER TAGS + OWED FOLLOW-ONS (fenced; NOT executed here)

**Ledger tags (`consistency-vs-emergence`, frozen).** `omega_R*M_g` is `[derived]` but **VALUE-CONSISTENCY** class (rides the GR-imported `7`). `Q` and `r_peak/r_sat` are `[derived]` and `ν_vac`-**FREE**, hence **emergence-capable at value level**. The GR numbers are `[GR-IMPORTED comparators]` (I11–I13). `ν_vac = 2/7` is `[canon]`, read-only, value GR-imported. Chebyshev orders, gauge parameters, precisions, the polish tolerance, `R_iso` and the G2b floor are `[engineering]`. The v1, v2.1 and v2.2 numbers are `[PRIOR-LANE]` — a seed, a comparator, two receipts — and none is a bin input. **`α`-CLEAN. No manifestation-class claim. No claim of any kind is minted.**

**Owed follow-ons (fenced; Rule 12 — the slot is NOT refilled with an assertion):**
1. **★ The substrate low-frequency cutoff** for the graded shear cavity — the prerequisite for any completeness or overtone claim. Grant's input first (§0), then its own prereg. **Not sketched here.**
2. **★ The BIN-3 question of §0** — whether a leaky resonator's outward-growing eigenfunction makes "where does the mode live" ill-posed. Grant's plumber call owed; **the window is not widened in the meantime.**
3. **The spheroidal (even-parity / P–SV-coupled) branch.** Toroidal only here.
4. **FORK-3's naming gap** (FLAG-4). Routed to the auditor lane.
5. **FORK-9's formal half** — whether Op6's phase-matching condition applies to a graded shear cavity with a `Γ = −1` inner wall.
6. **FORK-12** — untouched here; no `ℓ`-ladder is computed at all.
7. **FLAG-3's far-field assumption** — a test that the Regime-I port really is reflectionless at the scales that matter.
8. **The exterior-complex-rotation cross-check** as a genuinely independent third instrument. **Not built here, and FLAG-10 makes it more owed than it was, not less.**

---

> **Pre-registration provenance.** Frozen pre-registration for the cold-Q pole **v2.3 ROOT certification** — a one-defect re-freeze of v2.2 under Grant's standing 2026-08-03 ruling *certify the located root, not the rectangle*. Written against `origin/main` = `184db4b6`. Committed **ALONE** and pushed before any driver code and before any number produced by this instrument existed. **THE ONE CHANGE** is §S.5: G2's certification ladder becomes `n ∈ {48, 64, 80, 96}` at the unchanged `1e-10` tolerance, derived from the v2.1 coefficient-tail receipt at `research/2026-08-03_coldq-pole-v2.1_prereg-FROZEN.md:489` @ `7d8fe484`; the `n = 32` rung is retained as a gated rung of G4(b)/G5/FT-5 and as a mandatory non-gated diagnostic row; G2b and FT-2b are added. **Predecessor lanes, all unmodified and byte-untouched by this lane:** `research/2026-08-02_coldq-pole-derivation_prereg-FROZEN.md` and `..._result.md` (PR #845, MERGED at `052ccbba`, `SOLVER-NOT-CERTIFIED`); `research/2026-08-03_coldq-pole-v2_prereg-FROZEN.md` (`00724432`); `research/2026-08-03_coldq-pole-v2.1_prereg-FROZEN.md` (`7d8fe484`) and its result doc (PR #854); `research/2026-08-03_coldq-pole-v2.2-root_prereg-FROZEN.md` (`f15a6e4d`) and `research/2026-08-03_coldq-pole-v2.2-root_result.md` (`982c4c9b`) and their driver (PR #856, OPEN, DO-NOT-MERGE, `ROOT-NOT-CERTIFIED`). Companion inputs cited by path: `research/2026-07-20_v1-spin-mapping-adjudication_rerun.py:51`; `research/2026-07-20_ringdown-systematics_checks.py:69`, `:72`, `:133`; `research/2026-07-30_qlaw-derivation_scoping.md:401`; `research/drivers/coldq_pole_derivation_results.json:505`, `:509`, `:510`, `:512`; `research/drivers/coldq_pole_derivation.py:106`; `src/ave/core/constants.py:397`. Mints no `clm-`/`def-`; propagates to no leaf; engine byte-untouched; falsification ledger untouched regardless of outcome. Companion: the docket fragment `_orchestration/docket-entries/2026-08-03-coldq-v2p3-root.md`.
