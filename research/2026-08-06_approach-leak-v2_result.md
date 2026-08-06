# The APPROACH LEAK v2 — RESULT: **`LEAK-CERTIFIED-V2`.** Every gate passes, `FT-SLAST` fires on both parts, the entire v1 record reproduces with **zero mismatches over `1431` leaves**, and **the bins are ADJUDICATED**: `GAP-CLOSED` on every member canon or the engine actually states, co-firing with `UNDERDETERMINED-CANON`

**Date:** 2026-08-06 · **Branch:** `research/approach-leak-v2`
Prereg-file: research/2026-08-06_approach-leak-v2_prereg-FROZEN.md
(link: [`2026-08-06_approach-leak-v2_prereg-FROZEN.md`](2026-08-06_approach-leak-v2_prereg-FROZEN.md)) — commit `ebd1f4c7`, **pushed with no code**, before the v2 driver existed and before any number produced by the v2 instrument existed.
**Driver:** [`research/drivers/approach_leak_v2.py`](drivers/approach_leak_v2.py) → [`research/drivers/approach_leak_v2_results.json`](drivers/approach_leak_v2_results.json) (driver committed **before any v2 result JSON existed**).
**Number check:** [`research/drivers/approach_leak_v2_number_check.py`](drivers/approach_leak_v2_number_check.py) — gating via `make verify`, with a mutation receipt, and it **machine-gates `G-DET-V2`**.
**Class:** DERIVATION result — a **VERSIONED SUPERSEDE of ONE GATE**. **Mints no `clm-`/`def-`/`exp-`/`sup-`/`ilk-`; propagates to no KB/manuscript leaf; changes no solidity; edits no falsification ledger.** Engine `src/ave` **byte-untouched and never imported**.
**Predecessor:** [`research/2026-08-05_approach-leak_result.md`](2026-08-05_approach-leak_result.md) (branch `research/approach-leak`, PR #903, `[REVIEW: CLEARED]`, UNMERGED) — **byte-untouched by this lane, and gated as such.** *(AMENDED 2026-08-06 — §9.1: the predecessor branch was merged in at its REPAIRED tip `f3607be8`; two predecessor files moved, by the ORCHESTRATOR and not by this lane, and the `NC-BYTES` pin was amended onto them.)*
**SVA pilot case 9.** Per-row pilot notes in §7. **Written against `origin/main` = `c4fdced0`.**

---

## REGIME HEADER (mandatory, restated at the point of reading)

**MODE** — small-signal AC, a **scattering problem at REAL drive frequency**, not an eigenvalue
problem. **REGIME** — sub-yield lossless-reactive on `r > r_sat`; the `A ≥ 1` interior is Regime IV
and **is not in the domain**. **PHASE-STATE** — cold lattice, Op14 ON as a static constitutive
grade, `A(r) = r_sat/r`, `A = 1` exactly at `r_sat`. **SECTOR** — incident wave is **shear
(T2-translational, `G`-bond)**; converted quantity is the **Cosserat micro-rotation, channel 4**;
the conversion operator is the `G_c` antisymmetric-strain bond and nothing else. **No port is
crossed and no loss word is used anywhere in this lane.**

**AND THE REGIME OF THE THING THIS LANE RE-MEASURES:** `G-NC-SLAST` is a **negative control**, not a
physics gate. Its object is **an artifact's representation precision**. It owns no sector and
crosses no port, which is exactly why re-anchoring it changes not one digit of the physics —
and the `1431`-leaf byte-exact reproduction below is the receipt for that claim, not a promise.

---

## HEADLINE

> **★ CERTIFICATION, STATED FIRST AND WITHOUT SOFTENING. `LEAK-CERTIFIED-V2`.**
> Every one of the **`7`** v2 gates PASSES, `FT-SLAST` FIRES on **both** parts, and the entire v1
> record reproduces with **`0` mismatches over `1431` compared leaves** at exact string equality,
> recomputed digest `2af8acfe23aabb96` identical to v1's shipped digest. **The bins are therefore
> ADJUDICATED**, using the predecessor's frozen §7 definitions verbatim.
>
> **★ THE RE-ANCHOR, AND WHY IT IS A REPAIR AND NOT A RETUNE.** A reproduction gate's tolerance is
> bounded **by the precision at which the SOURCE SHIPPED its comparand**, not by the precision at
> which the consumer computes. v1 froze `1e-40` against a comparand rendered at `30` significant
> decimal digits, seeded from a rung carrying `17` — so `1e-40` sat **`10` orders below one floor
> and `23` below the other**, and **no correct instrument could ever have passed it**. That is an
> **ARTIFACT-class failure, not a falsification of reproducibility**. Both v2 tolerances are derived
> from **digit counts of the shipped strings and nothing else**, and were frozen before the run:
> **LEG-A `1e-27`** (bound `5e-30` = half a unit in the 30th significant digit, headroom `200`×) and
> **LEG-B `5e-16`** (bound `5e-17` = half a unit in the 17th, × a declared `10`× safety factor for
> the seed's unauditable upstream chain).
> *(AMENDED 2026-08-06 — §9.2(d): and a **new comparand pair** was added, not only a tolerance
> re-anchored. `LEG-B` is v1's comparison, re-anchored. **`LEG-A` is NEW** — shipped comparand vs a
> value recomputed from the source's **own shipped seed** — a different pair of objects.)*
>
> **★ AND THE ERROR MODEL CONFIRMED ITSELF RATHER THAN MERELY PASSING.** `LEG-A` measures
> `7.74183e-31` — **below its own derived `5e-30` rendering bound**, i.e. the residual landed at the
> comparand's rendering scale, exactly where the digit-count derivation put it. And the rendering is
> **STRING-IDENTICAL**: recomputing `S_last` from the shipped seed through the identical
> cancellation-free form reproduces `0.00000000109762455411903921151585733431` **character for
> character**. *(Reported as a NON-GATED diagnostic, per the freeze — the gate rides the derived
> tolerance, never on a 30-digit tie.)*
>
> **★ AND v1's OWN NUMBERS ARE UNCHANGED — ONLY THE ANCHOR MOVED.** `LEG-B(x) = 4.08817e-17` and
> `LEG-B(S) = 2.04408e-17` are **v1's measured separations, to the digit**, now read against an
> anchor sited inside the gate's domain of validity. Both also sit **below the bare `5e-17` rendering
> bound**, so the declared `10`× safety factor was **insurance, not a crutch** — said plainly,
> because a tolerance that needed its safety factor to pass would be a weaker result.
>
> **★ AND THE GATE CAN FAIL.** `FT-SLAST` fires on both parts. **COARSE**: perturbing the shipped
> seed by `1e-12` drives `LEG-A` to `5.00000e-13` and `LEG-B(x)` to `9.99959e-13` — **both FAIL**.
> **FINE**: perturbing the shipped comparand by `1e-26` drives `LEG-A` to `1.00008e-26` — **FAILS**,
> one decade above its tolerance — while `LEG-B` is untouched and still passes. **The fine part is
> what proves the `1e-27` leg is non-vacuous at its own scale**, which is precisely what v1's
> self-test-less `G-NC-SLAST` could not demonstrate.
>
> **★ THE ADJUDICATION, MEMBER BY MEMBER, NOT COLLAPSED.** `GAP-CLOSED` on `p = 0.5`, `1.0` and
> `1.5`; `CHANNEL-OPENS` on `p = 2.0`, `2.5` and `3.0`. **Every member canon or the engine actually
> states is `GAP-CLOSED`** — both the dispatch's `p = 1/2` and the engine's coded `p = 1`.
> **`UNDERDETERMINED-CANON` CO-FIRES**, and its absence receipts are **RE-VERIFIED on this branch,
> not inherited**: `P3` and `P4` return `0` hits on **both** engines across `4418` tracked files.
> **`SCALE-UNDERDETERMINED` co-fires on the residual prefactor `2(G_c/G)` and on nothing else.**
> **`p = 2.0` is on the knife-edge and is annotated SPLIT** — `{0}` at `θ = 1` and `{0, 1}` at
> `θ = 0.5`, the frozen `Ω < 4θ` criterion firing — **but the awarded bin is v1's frozen
> `CHANNEL-OPENS`, because the overlay reports a structure and does not move a boundary.**
>
> **⚑ AND TWO NEW FLAGS, BOTH MINTED AT FREEZE AND NEITHER REPAIRED.** `FLAG-RUNGPROV` (the
> last-bond rung literal's provenance is not auditable from any shipped artifact, and v1's "float64
> `repr`" attribution is not supported by one — v1 is right in KIND, unsupported in specifics) and
> `FLAG-SCANFRAG` (v1's `G-DET` machine-gate makes `make verify` a function of how many tracked
> files exist under three directories, so **any** later commit anywhere in that tree turns it RED).
> **Both surfaced, neither fixed, both ROUTED** — as is a third, `FLAG-FENCEBLIND` (§6.5),
> found while building this lane's own checker.

---

## §1 — THE GATE TABLES (measured against frozen; nothing dropped, widened or re-defined)

**No frozen criterion was dropped, widened, or re-defined.** The **only** tolerance that moved is
`G-NC-SLAST`'s, and it moved **before** any v2 number existed, on a derivation that takes v1's
measured `2.04408e-17` as **no input at all**.

> **AMENDED 2026-08-06 — §9.2(d). "ONE NEGATIVE-CONTROL TOLERANCE RE-ANCHORED" UNDERSTATES WHAT
> HAPPENED, SO SAY THE OTHER HALF IN THE HEADLINE AND NOT ONLY IN THE TABLE.** A tolerance moved
> **and a new comparand pair was added.** v1's single leg compared **this lane's mass-derived**
> quantities against the predecessor's shipped strings; that comparison survives **verbatim** as
> `LEG-B`, at a re-derived tolerance. **`LEG-A` is NEW** — it compares the shipped `S_last` against a
> value recomputed **from the source's own shipped seed** through the identical cancellation-free
> form. **That is a different pair of objects, not the same pair at a looser tolerance**, and it is
> the leg that carries the `1e-27` claim. §2.2's leg table disclosed it from the start in its
> *comparison form* column; the headline now carries it too, because a reader who stops at the
> headline should not come away thinking only a number was loosened.

### §1.1 The v2 gates

| gate | frozen criterion | frozen tolerance | measured | verdict |
|---|---|---|---|---|
| **`G-NC-SLAST`** ★ | LEG-A: `S_last` recomputed from the SHIPPED SEED through the identical cancellation-free form | `1e-27` rel | `7.74183e-31` | **PASS** |
| | LEG-B(x): this lane's mass-derived `ℓ_node/r_sat` at `62 M_⊙` | `5e-16` rel | `4.08817e-17` | **PASS** |
| | LEG-B(S): this lane's `S_1` at `M_ref`, `θ = 1` | `5e-16` rel | `2.04408e-17` | **PASS** |
| **`G-NC-REPRO`** ★ | the v1 instrument reproduces the shipped v1 JSON, exact string equality on every leaf but `_runtime_sec` | `0` mismatches | `0` over `1431` leaves | **PASS** |
| **`G-DET-V1-WRAPPED`** | v1's own `G-DET` criterion, preserved under the §1.1-of-prereg supersession | digest identity | `2af8acfe23aabb96` | **PASS** |
| **`NC-GATES`** | every v1 gate block reproduces, incl. v1's FAILING `G-NC-SLAST` at v1's own `1e-40` siting | exact strings | `9` pass:true, `1` pass:false, `2` pass:null | **PASS** |
| **`NC-FT`** | all v1 self-test blocks reproduce, every `fires` flag | exact strings | `6` of `6` firing | **PASS** |
| **`NC-SCAN`** | `n_files_scanned` and every `P1`–`P5` count/agreement/union reproduce | exact | `4418` files; `5` of `5` agree | **PASS** |
| **`NC-BYTES`** | every read-only predecessor artifact hashes to its blob at the pinned v1 commit — **AMENDED 2026-08-06 (§9.1): the pin is the REPAIRED v1 tip `f3607be8`, not the pre-repair ship `5e2694c0`** | byte-identical | `10` of `10`; `2` re-pinned, `8` unmoved | **PASS** |
| **`G-DET-V2`** ★ | two full v2 runs, identical digest, byte-identical apart from `_runtime_sec` | identical digest | `4da48b39074d9fbc` twice; bodies identical | **PASS** (machine-gated) |

### §1.2 The fireability self-test (a gate that cannot fail is not a gate)

| self-test | frozen firing condition | measured | fired? |
|---|---|---|---|
| **`FT-SLAST`** (i) COARSE | seed × `(1 + 1e-12)` ⇒ LEG-A **and** LEG-B(x) must FAIL | LEG-A `5.00000e-13` FAIL; LEG-B(x) `9.99959e-13` FAIL | **FIRES** |
| **`FT-SLAST`** (ii) FINE ★ | comparand × `(1 + 1e-26)` ⇒ LEG-A must FAIL while LEG-B is untouched and still passes | LEG-A `1.00008e-26` FAIL; LEG-B(x) PASS; LEG-B(S) PASS | **FIRES** |

**The FINE part is the load-bearing one.** A negative control that agrees to `30` digits could be
passing because the comparison *cannot separate*, not because the reproduction *is right*. Part (ii)
separates a `1e-26` perturbation and fails on it, so the `1e-27` leg is measuring something.

### §1.3 Scope split — RUN, N/A, UNRUN

| scope | gates RUN | N/A by construction | UNRUN by omission |
|---|---|---|---|
| the re-anchor | `G-NC-SLAST` (3 legs), `FT-SLAST` (2 parts) | — | **none** |
| reproduction | `G-NC-REPRO`, `NC-GATES`, `NC-FT`, `NC-SCAN`, `G-DET-V1-WRAPPED` | — | **none** |
| artifact integrity | `NC-BYTES` | — | **none** |
| reproducibility | `G-DET-V2` | — | **none** |
| **the v1 physics gates** | **none re-run independently — REPRODUCED, and that is a DIFFERENT and WEAKER claim than independent re-derivation** (§3.2) | — | **none** |

**Frozen:** `UNRUN ≠ PASSED`. **No gate in this lane is UNRUN by omission.**

---

## §2 — ★ THE SEED-AWARE ANCHOR: THE DERIVATION, AND THE MEASUREMENT AGAINST IT

### §2.1 The representation ladder, countable from the artifacts

**Rung 0 — the seed.** `last_bond_kernel_collapse.py`:59, verbatim:

```
ELL_OVER_RSAT_LADDER = ["6.0238983090250982e-19", "1e-12", "1e-6", "1e-3"]
```

consumed at `:343-346` by `ell = mp.mpf(ell_str)` — a **DECIMAL** parse at `dps = 60`, not a float64
bit pattern. **`17` significant decimal digits.**

**Rung 1 — the comparand.** `last_bond_kernel_collapse.py`:353 renders through `_s`, and `:71-73`:

```
def _s(x) -> str:
    return mp.nstr(x, 30, strip_zeros=False)
```

**`30` significant decimal digits**, shipped as `0.00000000109762455411903921151585733431`.

**The domain of validity, as a number.** A reproduction cannot be certified tighter than `~5e-30`
against the comparand's own rendering, nor tighter than `~5e-17` against the seed's if the seed is
**re-derived** rather than **re-read**. **v1's `1e-40` sat below both.**

### §2.2 The two comparison forms, and the two tolerances

| leg | comparison form | bound | derivation of the bound | frozen tolerance | headroom | measured |
|---|---|---|---|---|---|---|
| **A** (seed-exact) | `S_A = √(x_r(2+x_r)/(1+x_r)²)` from the SHIPPED `x_r`, vs the shipped `S_last` | `5e-30` | ½ unit in the 30th significant digit of an `mp.nstr(·, 30)` rendering; mp round-off at `dps = 60` adds `< 1e-58` | **`1e-27`** | `200`× | **`7.74183e-31`** |
| **B(x)** (seed-bounded) | this lane's `ℓ_node/r_sat` at `62 M_⊙`, vs the shipped seed | `5e-16` | ½ unit in the 17th significant digit (`5e-17`) × a declared `10`× safety factor for the seed's **unauditable** upstream chain | **`5e-16`** | `1`× on the bound | **`4.08817e-17`** |
| **B(S)** (seed-bounded) | this lane's `S_1` at `M_ref`, `θ = 1`, vs the shipped `S_last` | `2.5e-16` | `B(x)` × `∂ln S/∂ln x = ½` on the near-wall floor `S → √(2θx)` | **`5e-16`** | `2`× on the bound | **`2.04408e-17`** |

**The two numbers this lane computes, shipped in full:**

```
this lane's ell_node/r_sat (62 M_sun, dps 60) = 6.02389830902509844626713066887e-19
this lane's S_1            (M_ref, theta = 1) = 0.00000000109762455411903923395222956603
S_A from the SHIPPED seed  (dps 60, nstr 30)  = 0.00000000109762455411903921151585733431
```

**★ The third line is string-identical to the predecessor's shipped `S_last`.** Non-gated, per the
freeze — but it is the cleanest possible statement of what a seed-aware reproduction *is*: **feed the
source its own input and you get its own output back, character for character.**

### §2.3 Why this is a repair and not a retune, said in one paragraph

A retune moves a tolerance **to fit a number that has been seen**. This anchor was derived from
**digit counts of two strings** — `17` and `30` — which are properties of the artifacts and were
countable before any v2 code existed; it was **frozen and pushed** before the v2 driver was written;
and v1's measured `2.04408e-17` **appears in neither derivation**. The check that this is not
self-serving is arithmetical: had the derivation been reverse-engineered from `2.04408e-17`, LEG-A
would have been anchored near `1e-16` too. It is anchored at `1e-27`, **eleven orders tighter**, and
it passes at `7.74183e-31` — a place the seen number could not have suggested.

---

## §3 — THE NEGATIVE CONTROLS: COUNTS, AND THE ZERO-MISMATCH STATEMENT

### §3.1 The counts

| control | what was compared | count | mismatches |
|---|---|---|---|
| **`G-NC-REPRO`** | every leaf of the shipped v1 JSON, by `==` on the rendered string | **`1431`** compared (`1432` total, less `_runtime_sec`) | **`0`** |
| digest | recomputed vs shipped | `1` | **`0`** — `2af8acfe23aabb96` |
| **`NC-GATES`** | v1 gate blocks shipped `pass: true` | **`9`** | **`0`** |
| | v1 gate block shipped `pass: false` (v1's `G-NC-SLAST` at v1's own siting) | **`1`** — reproduced as `2.04408e-17`, byte-exact | **`0`** |
| | v1 gate blocks shipped `pass: null` | **`2`** | **`0`** |
| **`NC-FT`** | v1 self-tests shipped `fires: true` | **`6`** | **`0`** |
| **`NC-SCAN`** | tracked files scanned | **`4418`** | **`0`** |
| | patterns with both engines agreeing | **`5`** of `5` | **`0`** |
| **`NC-BYTES`** | read-only predecessor artifacts vs their blobs at the pinned v1 commit `f3607be8` (AMENDED — §9.1) | **`10`** | **`0`** |

> **THE ZERO-MISMATCH STATEMENT, PLAINLY.** **Across every comparison this lane makes against the v1
> record — `1431` JSON leaves at exact string equality, `9` passing gate verdicts, `1` failing gate
> verdict, `2` null verdicts, `6` firing self-tests, `4418` scanned files, `5` two-engine pattern
> agreements and `10` artifact blob hashes — the total number of mismatches is `0`.** The v1
> instrument is unchanged; only the anchor moved.

### §3.2 What the reproduction is, and what it is NOT — declared, not discovered

**It is NOT an independent re-derivation of the v1 physics.** This lane **imports the v1 driver
module and calls the v1 module's own `main()`**. Re-implementing the sweep would have produced a
second instrument and a second set of bugs, and would have tested the re-implementation rather than
the record. **What the reproduction certifies is exactly this: the v1 instrument, run again on this
branch, still produces the v1 record byte for byte.** Any claim beyond that is not licensed here, and
the `p`-bracket physics carries **v1's** provenance, not a second confirmation.

**Reproduction-class ledger:** `RECOMPUTED-VIA-V1-MODULE` for every gate and self-test above;
`FILE-HASH` for `NC-BYTES`; `REPLAYED-VERBATIM` for the v1 number-check's own three-mutation receipt.

### §3.3 The one declared intervention, and the fact that it is itself gated

The v1 scan surface is `git ls-files` over `manuscript/ research/ src/` **minus v1's own six
artifacts**. This lane adds five tracked files inside that tree, which would inflate the count for a
reason carrying **no information**. `v1._tracked_files` is therefore **wrapped** to drop this lane's
six as well — the pilot-5 self-reference repair applied to a second lane — **and nothing else in the
v1 module is touched.** **The wrapper is GATED, not assumed:** `n_files_scanned` must reproduce as
`4418`, and it does. Without the wrapper the delta is exactly `7` leaves, of which `n_files_scanned`
and `scan.P5` are pure self-reference (§6, `FLAG-SCANFRAG`).

---

## §4 — ★ THE ADJUDICATION (the predecessor's §7 bin definitions, VERBATIM)

**Bins:** `GAP-CLOSED` = `N_open = 0` at **every** row of the frozen sweep for the member.
`CHANNEL-OPENS` = `N_open ≥ 1` at **any** row. `SCALE-UNDERDETERMINED` and `UNDERDETERMINED-CANON`
may co-fire. **No boundary moved, no bin added, renamed or merged, no member preferred.**

| `p` | provenance of the member | `N_open` over the sweep | `log10(S_1/S_open)` | `ζ_max` | side of `p_crit` | **BIN** |
|---|---|---|---|---|---|---|
| `0.5` | **the DISPATCH's stated expectation** (`a=1, b=0`) | `[0]` | `24.33` – `28.54` | `4.67038827711388070441696359081e-25` | below | **`GAP-CLOSED`** |
| `1.0` | **the ENGINE's coded `a=2`**, `I_ω` ungraded | `[0]` | `8.058` – `9.738` | `7.64219872765688277388060621827e-17` | below | **`GAP-CLOSED`** |
| `1.5` | filler, so the below-knife arm is not two-point | `[0]` | `2.634` – `3.471` | `0.0000000125049992972797073610801916705` | below | **`GAP-CLOSED`** |
| `2.0` | `a=1` with the RHO-B **ANALOGY** for `I_ω` — **ANALOGY, NOT CANON** | `[0, 1]` | `-0.07774` – `0.3372` | `91.3379208100579910158046584733` | **ON** | **`CHANNEL-OPENS`** *(SPLIT overlay)* |
| `2.5` | the engine's `a=2` with the RHO-B **ANALOGY** — **ANALOGY, NOT CANON** | `485` … `3228` (`384` distinct) | `-1.905` – `-1.343` | `1.00000019302787476201778887731` | above | **`CHANNEL-OPENS`** |
| `3.0` | loosest member — **ANALOGY, NOT CANON** | `84316` … `881448` (`387` distinct) | `-3.123` – `-2.463` | `1.00000000000000166828253699831` | above | **`CHANNEL-OPENS`** |

### §4.1 The headline award, stated per the frozen bin-arithmetic

**The bracket does NOT agree, so there is no single headline bin, and none is reported.** Per the
frozen arithmetic, **BOTH** bins are reported with their members named:

> **`GAP-CLOSED` on `p ∈ {0.5, 1.0, 1.5}` — which includes EVERY member canon or the engine actually
> states — CO-FIRING with `UNDERDETERMINED-CANON`; and `CHANNEL-OPENS` on `p ∈ {2.0, 2.5, 3.0}`,
> every one of which requires the unwritten `I_ω(A)` law. `SCALE-UNDERDETERMINED` co-fires on the
> residual back-action prefactor and on that field alone.**

**The asymmetry between the two arms is the content.** The `GAP-CLOSED` arm is populated by members
the corpus **states**: `p = 1/2` is the dispatch's own arithmetic, `p = 1` is what
`cosserat_field_3d.py`:767 × `:761` actually codes. The `CHANNEL-OPENS` arm is populated **entirely**
by members that need a grading law for `I_ω(A)` that **appears nowhere in `4418` tracked files**.
**No member is preferred and none is dropped** — but the two arms do not have the same provenance
status, and saying so is not a preference, it is the receipt.

### §4.2 `p = 2.0`: the knife-edge member, and why the SPLIT is an overlay and not a boundary move

At `p = 2` the `x`-dependence cancels exactly and the verdict is **mass-independent**, decided by
`Ω < 4θ` alone. Disaggregating that member's `N_open` by `θ` — **through v1's own `N_open_count`**,
not a re-implementation — gives:

| `θ` | `N_open` distinct values over the whole sweep |
|---|---|
| `1.00` | `[0]` |
| `0.500` | `[0, 1]` |

**The frozen criterion firing, exactly.** At `θ = 1`, `4θ = 4` and the band top is `2.861`, so
`Ω < 4θ` everywhere. At `θ = 0.5`, `4θ = 2` and the upper band opens one cell.

> ★ **AND THE DISCIPLINE POINT, BECAUSE IT WOULD HAVE BEEN EASY TO GET WRONG.** This lane's own
> prereg §6.1(1) says a splitting member is *"reported as SPLIT … not collapsed to either bin"*.
> v1's frozen §7 says `CHANNEL-OPENS` = `N_open ≥ 1` at **any** row. **These are in tension, and the
> FROZEN BOUNDARY GOVERNS:** `p = 2.0` is awarded **`CHANNEL-OPENS`**, and SPLIT is recorded as an
> **annotation** in the shipped JSON beside it. **A reporting instruction in the successor's prereg
> does not get to move the predecessor's bin boundary**, and the alternative — inventing a fifth bin
> at adjudication time — is exactly the post-hoc criterion drift the freeze rule exists to prevent.

### §4.3 `UNDERDETERMINED-CANON`: the absence receipts, RE-VERIFIED not inherited

| id | target | METHOD A `git grep -P` | METHOD B Python `re` | agree | verdict |
|---|---|---|---|---|---|
| `P1` | `G_c(A)` written as a function | `4` | `4` | ✅ | hits exist; **all are statements of its ABSENCE** (v1 §3.1) |
| `P2` | `G_c` × a kernel | `4` | `4` | ✅ | **the only substantive hit is the ENGINE line itself** |
| `P3` | `I_ω(A)` written as a function | `0` | `0` | ✅ | **ABSENCE RECEIPT** |
| `P4` | `I_ω` / micro-inertia riding a kernel | `0` | `0` | ✅ | **ABSENCE RECEIPT** |
| `P5` | a **rotational** band top | `5` | `5` | ✅ | hits exist; **all are the vector/Cosserat-TRANSLATIONAL bracket** |

**`4418` tracked files, both engines named, no pattern uses `\b`, `5` of `5` agree.** **The two
missing laws, enumerated exactly:** (i) the `I_ω(A)` grading law — the exponent `b` — which
**`0` hits on `P3` and `P4` say does not exist anywhere; (ii) the `G_c(A)` grading law — the
exponent `a` — which no canon leaf states, the only substantive hit being an unratified engine line.
**Those two absences are what put `p` beyond determination, and they are re-measured here rather
than quoted from v1.**

### §4.4 `SCALE-UNDERDETERMINED`: quarantined to one field, exactly as v1 froze it

**Fires on `residual_backaction_QUARANTINED` — the prefactor `2(G_c/G)` — and on nothing else.**
A-008 pins `G_c/I_ω`; it does **not** pin `G_c/G`. **Every other number in this lane is ratio-only:**
`N_open` is an integer, `ζ_max` is a dimensionless amplitude ratio, and the whole gap-margin
arithmetic is a competition between two powers of `ℓ_node/r_sat`. **The bin is not extended to any
other field.**

### §4.5 The rotational-top bracket: MOOT, and reported as moot

On every below-knife member the drive never reaches the rotational band at all, so its top is never
consulted. **The three-member bracket is REPORTED and NONE is chosen**, and its mootness is stated
rather than silently dropped — as the v1 freeze requires. It becomes load-bearing only inside the
`CHANNEL-OPENS` arm, which is populated entirely by ANALOGY members.

---

## §5 — THE PROPAGATION CONSEQUENCE: **RECORDED, NOT EXECUTED**

The channel-scoped kernel-collapse ruling's leak clause
(`_orchestration/docket-entries/2026-08-05-ruling-kernel-collapse-rescope.md`:16-18), verbatim:

> *"Shear→rotation conversion cannot occur at the wall (the door closes with the strain kernel) and
> is confined to the graded approach where `G_c·S_ε` is finite — the leak is one computable number
> (a coupled two-channel scattering computation, routed as the approach-leak lane)."*

**On the adjudicated table, that clause resolves to the BOUNDED EVANESCENT FORM WITH THE KNIFE-EDGE
CAVEAT.** The resolved reading, recorded here for the gated propagation pass:

> *"Shear→rotation conversion cannot occur at the wall and is confined to the graded approach. On
> every grading exponent canon or the engine states, the confinement is not merely spatial but
> **spectral**: there is no propagating rotational state at the drive frequency at any radius on the
> approach, so the 'leak' is a purely reactive admixture, bounded by `ζ_max` and transporting exactly
> zero time-averaged power. **'One computable number' is answered: `ζ_max`. On the members canon or
> the engine actually states — `p = 0.5` and `p = 1.0` — it is bounded by
> `7.64219872765688277388060621827e-17`, i.e. below `1e-16`.** The answer is **conditional on a
> grading law for `I_ω(A)` that canon does not state** — at `p ≥ 2` the verdict inverts, and the
> members that invert it are analogies, not canon."*

> ★ **AND THE BOUND IS BOUND TO THOSE TWO MEMBERS, NOT TO THE BIN** *(AMENDED 2026-08-06 — §9.2(a);
> the earlier wording said "on every stated member", which is true but invites exactly the
> conflation below).* The `GAP-CLOSED` **bin** is `p ∈ {0.5, 1.0, 1.5}`. Its third member `p = 1.5`
> is **filler** — `canon_or_engine_stated` is **false** for it — and it carries
> `ζ_max = 0.0000000125049992972797073610801916705`, roughly eight orders **above** `1e-16`. It is
> nonetheless `GAP-CLOSED`, because **`GAP-CLOSED` is an `N_open = 0` statement — spectral — and
> never a `ζ`-magnitude statement.** Reading the `1e-16` bound across the whole bin is therefore
> wrong in one member out of three, and the two claims must not be collapsed: *no propagating
> rotational state at any swept row* is the bin; *how small the reactive admixture is* is a separate
> number that happens to be tiny on the two stated members and is not tiny on the filler one.

**★ THIS IS RECORDED, NOT EXECUTED.** This lane edits **no** KB leaf, **no** manuscript file, **no**
ruling docket entry, **no** solidity, **no** matrix row and **no** falsification ledger. **The
auditor lands corpus-state entries.** The single hinge is named rather than buried: **if an `I_ω(A)`
law is ever ruled at `b = 3` while the engine's `a = 2` stands, `p = 2.5` and the resolution
inverts.**

**Out of scope, one line as fenced:** the ROUTED rotational-penetration frontier item concerns a
cold-medium rotational wave at `≥ 1.022` MeV crossing `r_sat` — a different frequency regime by
roughly eighteen orders of magnitude from this lane's ringdown band. **MeV-scale rotational radiation
is OUT OF SCOPE here.**

---

## §6 — FLAGS

### §6.1 Carried forward BY POINTER — not restated, not re-litigated, not repaired

`FLAG-EXP`, `FLAG-IOMEGA`, `FLAG-MECH`, `FLAG-ROTTOP` — bodies at
[`research/2026-08-05_approach-leak_result.md`](2026-08-05_approach-leak_result.md) §7, **untouched
by this lane and gated as such (`NC-BYTES`)**. **The v1 bodies are the citable text.** This lane adds
nothing to them and removes nothing from them.

> **AMENDED 2026-08-06 — §9.2(b). Say it exactly, because "byte-untouched" is no longer the precise
> word for the FILE.** The four flag **bodies** in v1 §7 are unchanged, character for character. The
> **file** that carries them is **not** byte-identical to its `5e2694c0` blob: the ORCHESTRATOR's
> disclosed post-ship SCANFRAG repair **appended a dated note to the end of it** (and rewrote
> `research/drivers/approach_leak.py`'s scan surface). That is an extrinsic edit by another lane, and
> `NC-BYTES` is amended to pin at the repaired tip `f3607be8` accordingly (§9.1). **What this lane
> claims is the claim it always claimed: it wrote none of them.**

### §6.2 `FLAG-FREEZE` — DISCHARGED

v1's own freeze error and the repair it routed: *"extend the pre-freeze second-method check to
NEGATIVE-CONTROL tolerances, and gate a reproduction at the precision the source SHIPPED, not at the
precision the consumer computes in"* (`2026-08-05_approach-leak_result.md`:524-527). **Both halves
are executed in this lane's freeze** — prereg §2.4 runs the second-method check on both
negative-control tolerances, and §2 gates at the source's shipped precision. **The v1 body stays
byte-untouched (Rule 12); the discharge is recorded here, not written back into v1.** The routed SVA
row-9 amendment is **still routed and still not drafted** — the auditor lands SVA amendments.

### §6.3 `FLAG-RUNGPROV` — NEW, minted at freeze, surfaced and NOT repaired

v1's §1.3 attributes the last-bond rung to *"the float64 literal `6.0238983090250982e-19` (a
17-significant-figure `repr`)"*. **That attribution is not supported by any shipped artifact.** The
string is **not** the shortest round-tripping `repr` of any IEEE-754 double — Python's shortest repr
of the nearest double is `6.023898309025099e-19`, `16` digits — and no shipped artifact records how
the literal was produced. **v1 is correct in KIND (the limiting error is the source's input
precision) and unsupported in its specific attribution.**

**Consequence for this lane, and it is why the `10`× safety factor exists:** the only defensible
bound is the literal's **representation** precision, plus a declared factor for the chain nobody can
audit. **Not repaired:** the last-bond driver is not patched, the rung is not re-derived, and v1's
diagnosis is not edited. **ROUTED.**

### §6.4 `FLAG-SCANFRAG` — NEW, minted at freeze, surfaced and NOT repaired

v1's `verify-approach-leak-number-check` **machine-gates `G-DET`** by re-running the v1 driver and
requiring digest equality (`approach_leak_number_check.py`:172-189). The v1 driver's scan surface is
`git ls-files manuscript research src` minus v1's own artifacts — **so the shipped digest is a
function of how many tracked files exist under those three directories.**

**Measured at freeze-drafting time, with only the v2 prereg added to the tree:** `_digest`
`2af8acfe23aabb96` → `973458b3a1648c2a`; `n_files_scanned` `4418` → `4419`; `scan.P5` hits `5` → `6`
on **both** methods. **`make verify` goes RED on any tree that adds a single tracked file under those
directories** — this lane's, a concurrently-open lane's, or main's after the merge.

**The named structural repair, NOT executed:** pin the scan surface to a **commit** rather than to
the worktree (`git ls-tree -r <ship-commit>` restricted to the scan directories), which is
deterministic forever and immune to any later addition. **That belongs in the v1 driver, which this
lane may not edit. ROUTED to the orchestrator.**

**What this lane did instead, and it is disclosed rather than quiet:** wrapped its own reproduction
(§3.3, gated on `4418`), and in the `Makefile` **retained `verify-approach-leak-number-check`
verbatim as a target** while replacing it in the `verify:` prerequisite list with
`verify-approach-leak-v2-number-check`, **a strict superset that runs every check the v1 target ran**
— v1's doc-numeral registry, v1's gate reconciliations, v1's three-mutation receipt and v1's `G-DET`
— plus the v2 checks. **No check dropped, no tolerance moved, v1's number-check module
byte-untouched.**

> **⚑ AMENDED 2026-08-06 — §9.2(c). `FLAG-SCANFRAG` IS DISCHARGED, AND THE V1 TARGET IS BACK IN THE
> `verify:` CHAIN.** The orchestrator executed the named structural repair on the v1 branch — exactly
> the pin-to-a-commit fix routed above — landing v1 at `f3607be8`, which this branch has merged. The
> v1 driver's scan surface is now a function of a **commit**, not of the working tree. **Measured on
> this merged tree, whose live census under the scan directories is `10` above the pinned `4418`
> (`5` from the v1 lane, `5` from this one): the v1 target is GREEN and reproduces
> `2af8acfe23aabb96`** — and it stays green, at the same digest, with an eleventh tracked file
> deliberately added. The basis on which it was dropped from the prerequisite list
> is therefore **void**, and the drop is reverted: **both targets gate.** The superset relation is
> retained on purpose — it is now redundancy rather than substitution, on a gate that has already
> failed once in a way a same-tree live-fire could not see. **This lane surfaced the flag and did not
> repair it; the repair is the orchestrator's, on the v1 branch, and is cited here rather than
> claimed.**

### §6.5 `FLAG-FENCEBLIND` — NEW, found while building this lane's own checker; repaired HERE, surfaced THERE

The v1 number-check pairs back-ticks with ``r"`([^`]+)`"`` **over the whole document**. A fenced code
block is **three** back-ticks, so **every fence shifts the pairing by one** and silently moves real
numerals into the *gaps between* matched pairs, where they are never checked.

**Measured, on this lane's own doc, before the repair:** the fence-blind scan reached `32` distinct
numerals and **the entire §4 adjudication table — every `log10` margin, every `ζ_max`, every `N_open`
count — reached the registry not at all.** Stripping fences before scanning restores balanced
pairing; the registered-value count rose from `59` to `73`. **This is a strengthening, not a
relaxation: it can only ADD numerals to the checked set.** It is applied to **this lane's own
checker** and nowhere else.

**Measured, on the PREDECESSOR's doc, as a NON-GATED diagnostic:** running the fence-stripped scanner
over `2026-08-05_approach-leak_result.md` with v1's own registry and allow-list surfaces exactly
**one** escaped numeral — `520`, v1's §1.4 count of false mismatches manufactured by an
implementation detail it repaired *before* committing its driver. **It is not a physics number and
nothing rides on it**, which is the honest size of this finding: v1's gate had one numeral escape,
and it was a bookkeeping one.

> **NOT REPAIRED THERE, AND THE REASON IS NOT COURTESY.** v1's number-check is a predecessor artifact
> and is byte-untouched (`NC-BYTES`). And the strengthened scan is deliberately **NOT gated against
> v1's doc**: gating it would **add a gate to a predecessor's certification set**, which this lane's
> own freeze forbids in as many words. **Surfaced, measured, ROUTED — not fixed.**

---

## §7 — SVA v0.2, per-row fill notes (pilot case 9)

| row | fill | note |
|---|---|---|
| **1 · Sector / ownership** | FILLED | **Unusual fill, and it did real work.** The row was satisfied by declaring the re-measured object **sector-less** — a negative control's object is an artifact's representation precision, not a substrate quantity. Writing that down is what licensed the claim that re-anchoring cannot change a digit of physics, and forced that claim to be *receipted* (`1431` leaves) rather than asserted. **Proposal: row 1 should name "the object is not a substrate quantity" as an explicit valid fill for instrument-class lanes.** |
| **2 · Regime / phase-state** ★ | FILLED — **and this row IS the lane** | The pilot-8 discipline (state the domain of validity of the statement being re-measured, and where the prior measurement sat) is what converted a vague "the tolerance was too tight" into a *number*: the domain is bounded by the source's shipping precision, `30` and `17` digits, and v1 sat `10` and `23` orders outside it. **Without this row the repair would have been a retune with a story; with it, it is a regime correction with an arithmetic.** |
| **3 · Circuit statement** | FILLED | Inherited and re-declared, not re-derived. The one thing it forced: the explicit declaration that **no new circuit quantity is computed**, which is what made §3.2's "this is a reproduction, NOT an independent re-derivation" a *pre-committed* limitation rather than a caveat added at write-up. |
| **4 · Plane & projection** | FILLED | Unchanged; the re-anchored gate's plane (`n = 1`, `M_ref`, `θ = 1`) is explicitly **not moved**, which pre-empts the obvious suspicion that a passing rerun moved the probe as well as the tolerance. |
| **5 · Constitutive provenance** ★ | FILLED — **and it caught `FLAG-RUNGPROV`** | The row demanded a provenance tag for the rung literal. Attempting to write `float64-repr` as v1 did, and *checking it*, is what exposed that the string is not any double's shortest repr. **The row does not distinguish "provenance of a physical constant" from "provenance of a numeral in an artifact", and the second turned out to be load-bearing. Proposal: row 5 should name ARTIFACT-NUMERAL provenance as a distinct tag class with `REPRESENTATION-BOUNDED` as a valid value.** |
| **6 · Energy ledger** | FILLED | RIM, unchanged. Trivial for this lane by construction — a comparison of two decimal renderings crosses no port — but writing it down is what makes "trivial" a *checked* statement instead of an assumed one. |
| **7 · Calibratability** | FILLED | Both legs are **relative** separations and both tolerances derive from **digit counts**, so nothing in the re-anchor normalizes against an external standard. The row's demand is what produced the "derived from digit counts and nothing else" formulation that §2.3 leans on. |
| **8 · Discrimination class** ★ | FILLED — **and its tautology filter is the anti-retune guard** | The filter forced the explicit declaration that `2.04408e-17` is **not an input** to either derivation. That single sentence, frozen before the run, is what separates this from a retune — and §2.3's arithmetical check (LEG-A anchored `11` orders tighter than the seen number would suggest) is its receipt. **Highest-value row of this pilot after row 2.** |
| **9 · Certification plan** | FILLED — **and it discharged the predecessor's own routed repair** | The pre-freeze second-method check, **extended to negative-control tolerances** exactly as v1's `FLAG-FREEZE` routed. Both tolerances got two independent budget evaluations before the run. **The amendment itself is still routed to the auditor and still not drafted here.** |
| **10 · Adjudication routing** | FILLED | It kept the propagation consequence RECORDED and not EXECUTED under real pressure to just fix the ruling's wording, and it is what made §4.2's boundary-vs-overlay tension visible **as a decision** rather than resolved silently in favour of the newer document. |
| **11 · Numerical conditioning** ★ | FILLED — **and the NAMED-CANCELLATION sub-row paid off again** | Naming, before the run, that LEG-A compares two numbers agreeing to `~30` digits and therefore destroys `~30` of the `60` carried — leaving `3` decades below the tolerance — is what set `1e-27` rather than something tighter and prettier. The **NO-ITERATION** declaration (v1's pilot-7 proposal) is re-used verbatim and remains the right fill. |

**Amendment proposals from this pilot (ROUTED, NOT DRAFTED — the auditor lands SVA amendments):**
(a) row 5 should name **ARTIFACT-NUMERAL** provenance as a distinct tag class, with
`REPRESENTATION-BOUNDED (N significant digits)` a valid value — pilot 9 needed it and had to invent
it inline; (b) row 1 should name **"the object is not a substrate quantity"** as an explicit valid
fill for instrument-class lanes; (c) v1's three pilot-7 proposals (row 9 negative-control extension,
row 11 NO-ITERATION, row 4 plane-invariance) **all fired again here and are re-endorsed rather than
re-proposed**.

---

## §8 — CLASSIFICATION + FENCE

**Class: DERIVATION, CERTIFIED. Mints nothing, moves no solidity, adjudicates no physics fork.** The
FORM adjudicated here — the driven-tank `ζ`, the crossing condition, the integer `N_open`, the
knife-edge at `p = 2`, the `ζ_max < 1` identity — is an **axiom-manifestation, FORM-class**
consequence of the Ax-4 kernel plus lattice discreteness plus the A-008-ruled `G_c/I_ω = ω_C²`, and
it carries **v1's** provenance, reproduced. Every SI-scale quantity is **VALUE-CONSISTENCY class**,
riding `G`, `M`, the GR-imported `ν_vac` in `r_sat = 7GM/c²`, and the definitional
`ℓ_node = ħ/(m_ec)`. **The re-anchor itself is INSTRUMENT-class and carries no physics content.**

**This lane does NOT license:**

1. **Any claim that the v1 physics was independently re-derived.** It was **reproduced** (§3.2).
2. **Anything about the rotational channel AT or INSIDE `r_sat`.** MeV-scale rotational radiation is
   out of scope; one cross-reference line only.
3. **Any adjudication of the cross-grade aggregation fork** (L∞ vs normalized-L2), of FORK-3(b), of
   the `β` bracket, of the `K(A)` fork, of `FLAG-CAUSAL`, or of any predecessor's other bins.
4. **Any promotion of the engine's coded `a = 2` to canon**, and **no invention of an `I_ω(A)` law**.
   The `p ≥ 2` members exist to bracket; the RHO-B `1/S³` grading applied to the micro-inertia is an
   **ANALOGY and is labelled one at every site**.
5. **Any AVE-vs-competitor discrimination claim.** The ECO free-reflectivity degeneracy carried at
   `2026-08-05_echo-delay-v2-reach-through_result.md`'s headline applies unchanged.
6. **Any KB, manuscript, ruling-docket or `src/ave` edit; any predecessor-artifact edit.** All ten
   read-only artifacts are byte-identical to their blobs at the pinned v1 commit `f3607be8`, and
   that is **gated**. **AMENDED 2026-08-06 (§9.1):** `2` of the ten are not byte-identical to their
   `5e2694c0` blobs, because the ORCHESTRATOR rewrote them in its disclosed post-ship SCANFRAG
   repair. **This lane still wrote none of the ten** — which is the sentence this item makes and
   the purpose `NC-BYTES` exists to enforce.
7. **No claim minted.** No `clm-`/`def-`/`exp-`/`sup-`/`ilk-`. No solidity moved.
8. **No SVA amendment drafted.** Routed, as v1 routed its own.

---

## §9 — AMENDMENTS (dated 2026-08-06, PRE-MERGE, FULLY DISCLOSED)

**Everything in §9 was written and landed BEFORE PR #904 merged, on this branch, with receipts.**
Nothing here moves a physics number, drops a criterion, or converts a ❌ to a ✅. Docket:
[`_orchestration/docket-entries/2026-08-06-approach-leak-v2-correction.md`](../_orchestration/docket-entries/2026-08-06-approach-leak-v2-correction.md).

### §9.1 `AMENDMENT-NCBYTES-2026-08-06` — the read-only pin, re-sited onto the repaired v1 tip

**WHAT HAPPENED, AND IT IS NOT SOMETHING THIS LANE DID.** This branch was cut from the PRE-repair v1
ship commit `5e2694c0`. After that cut, the ORCHESTRATOR executed and disclosed the SCANFRAG repair
on the v1 branch — the repair this lane's own `FLAG-SCANFRAG` (§6.4) routed to it — landing v1 at
`f3607be8`. That repair rewrote exactly **`2`** of `NC-BYTES`'s **`10`** read-only artifacts:
`research/2026-08-05_approach-leak_result.md` (a dated note appended) and
`research/drivers/approach_leak.py` (the scan surface pinned to a commit). The merge that carries
`f3607be8` into this branch therefore turned `NC-BYTES` false — and because certification is a
conjunction, the whole v2 record collapsed to its `NOT ADJUDICATED` placeholder.

**WHY THAT IS A GATE DEFECT AND NOT A FINDING.** `NC-BYTES`'s frozen PURPOSE, in its own words, is
*"this lane wrote none of them"*. That proposition is **still true**. The un-amended gate could not
express it, because it encoded the purpose as *equality against one particular commit* — and so it
misreported an **extrinsic, disclosed, orchestrator-authored** event as a lane-authored write. The
amendment restores the purpose.

**THE RE-PIN, AND THE CHOICE MADE.** **ALL TEN artifacts are re-pinned at the repaired v1 tip
`f3607be8`** — a single pin, not a split pin. The reason is that the split is **not needed**:
`f3607be8` is a descendant of `5e2694c0` whose diff touches exactly `2` of the ten, so for the other
**`8`** the blob object is *the same object* at both commits and the re-pin is a **no-op in value**.
That no-op is **COMPUTED by the gate**, not asserted (`unmoved_artifacts_identical_at_both_commits`).
One pin means one truth-source and no standing two-commit bookkeeping to drift; and the repaired tip
is the predecessor state that will actually reach `main`, so the gate now tracks the mergeable
predecessor rather than a superseded intermediate. The superseded `5e2694c0` hash is **retained per
artifact** in the shipped JSON, so the delta stays readable forever.

**NOTHING WAS DROPPED — TWO CONJUNCTS WERE ADDED, AND BOTH GATE THE RE-PIN ITSELF.**

| conjunct | status | what it forbids |
|---|---|---|
| live blob == pinned blob, `10` of `10` | **RETAINED**, target re-sited | any lane-authored write to a predecessor |
| COMPUTED moved-set == DECLARED moved-set | **NEW** | an *undisclosed* extra rewrite hiding inside the re-pin |
| every unmoved artifact identical at BOTH commits | **NEW** | the "`8`-fold no-op" being a claim rather than a measurement |

**★ THE RECEIPT — AND IT IS A GATE, NOT A SENTENCE.** The v2 instrument was re-run post-amendment
(v2.1). Leaf-level diff against the shipped v2 JSON, taken with the driver's own `flatten`:

| bucket | leaves |
|---|---|
| pre-amendment (shipped v2) leaves total | **`297`** |
| post-amendment (v2.1) leaves total | **`350`** |
| CHANGED | **`5`** — `_digest`, `_runtime_sec`, `NC-BYTES/frozen`, and the two repaired artifacts' `blob_live` |
| ADDED | **`53`** — every one inside the `NC-BYTES` block |
| REMOVED | **`0`** |
| **changed/added/removed OUTSIDE `NC-BYTES` ∪ `_digest` ∪ `_runtime_sec`** | **`0`** |

**Every physics leaf is byte-identical to the shipped v2 record.** The `1431`-leaf v1 reproduction,
the three `G-NC-SLAST` legs, both `FT-SLAST` parts, the `NC-SCAN` counts and the entire §4
adjudication are **unchanged strings**. The digest moved `b38c6c269b5dd301` → `4da48b39074d9fbc`,
which is the digest doing its job.

**This receipt is RE-DERIVED ON EVERY `make verify`,** not quoted from a one-off run: the number
check reads the pre-amendment JSON **out of git by blob hash** and recomputes the bucketed delta,
failing hard if a single leaf outside the permitted set moves. Mutation `M6` moves one physics leaf
and requires the receipt to catch it, so the receipt cannot degrade into a no-op. Reproduce by hand:

```
git cat-file blob 25b02dfc1f963caeee0f307694ef4887af15ac90   # the shipped v2 JSON
# vs research/drivers/approach_leak_v2_results.json          # v2.1
python3 research/drivers/approach_leak_v2_number_check.py     # recomputes the receipt, gating
```

**What did NOT change:** the frozen prereg is **not edited** — `2026-08-06_approach-leak-v2_prereg-FROZEN.md`
§3.3 still reads `5e2694c0`, and it is left frozen deliberately. The amendment is disclosed **here**
and in the docket correction, which is where an amendment to a frozen instrument belongs; rewriting a
frozen pre-registration to match a later measurement is the exact move the freeze rule exists to
prevent.

### §9.2 Wording corrections (four), each sited at the sentence it repairs

**None of these moves a number.** Each is a place where a true sentence was phrased so that a
reasonable reader would carry away a false one, and the repair is written **at the sentence**, not
only here.

| # | site | the defect | the repair |
|---|---|---|---|
| **(a)** | §5, the resolved leak clause | the `ζ` bound was attached to "every stated member", one sentence away from the `GAP-CLOSED` **bin** — and a reader carries it to the bin | the bound is now bound to `p = 0.5` and `p = 1.0` explicitly, with `p = 1.5`'s much larger `ζ_max` named and the bin restated as an `N_open = 0` statement, never a `ζ`-magnitude one |
| **(b)** | §6.1 (and §8 item `6`, and the header line) | "byte-untouched" was the right word at freeze and the wrong word after the merge | the flag **bodies** are unchanged; the **file** is not byte-identical to its `5e2694c0` blob because of the ORCHESTRATOR's disclosed repair; **this lane wrote none of them** is what is actually claimed |
| **(c)** | `Makefile` (and §6.4) | the `FLAG-SCANFRAG` rationale comment asserted the fragility as **live**, which it stopped being when the repair landed; the v1 target had been dropped from `verify:` on that basis | comment rewritten as history; **`verify-approach-leak-number-check` RESTORED to the `verify:` chain** — measured green on this merged tree — so **both** targets gate |
| **(d)** | §1 and the HEADLINE | "ONE negative-control tolerance re-anchored" understates: a tolerance moved **and** a new comparand pair was added | `LEG-B` is v1's comparison re-anchored; **`LEG-A` is a NEW comparand pair** (shipped comparand vs a value recomputed from the source's own shipped seed). §2.2's leg table always disclosed it; the headline now does |

**(d) has one action this lane cannot take:** the phrase also heads the **FROZEN prereg** and **PR
#904's title**. The prereg stays frozen. **The PR title should pick up the same clause — orchestrator
action, named here and not performed here.**

### §9.3 Routed, not fixed — one line each

- **`METHOD-A` colon-hardening.** Post-repair, v1's `scan_method_a` parses `git grep` tree-ish output
  with `line.split(":", 3)` and takes `parts[1]`:`parts[2]`. Correct for the current roster; **wrong
  for any scanned path containing a colon**, which would silently mis-attribute a hit and move a
  pattern count. It is a v1-branch artifact and this lane may not edit it. **ROUTED.**
- **The `S_n`-monotonicity argument.** The sweep checks the band's **last** cell and treats that as
  sufficient. The reason is real — with `⟨P⟩ = 0` the reactive admixture is monotone in `n` across
  the band, so the last cell bounds the rest — but it is **implicit in the driver and written down
  nowhere**. An argument a reader must reconstruct is not a receipt. **ROUTED: write it at the site
  where the sweep is defined.**
