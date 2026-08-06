# echo-delay v2 — RESULT: **PART 1 fully re-certified on BOTH branches, `BIN-DISC` ADJUDICATED — the two inertia gradings ARE echo-discriminable by timing, by `38.6`–`43.2` ringdown damping times.** **PART 2 (Y8) `Y8-NOT-CERTIFIED`: the reach-through observable, as this lane posed it, is NOT WELL POSED — and its own gate is what says so**

**Date:** 2026-08-05
**Prereg-file**: research/2026-08-05_echo-delay-v2-reach-through_prereg-FROZEN.md
**Prereg-commit:** `db98550b` (frozen and pushed **ALONE**, before any driver code and before any number produced by this instrument existed)
**Driver:** [`research/drivers/echo_delay_v2_reach_through.py`](drivers/echo_delay_v2_reach_through.py) → [`research/drivers/echo_delay_v2_reach_through_results.json`](drivers/echo_delay_v2_reach_through_results.json)
**Number check:** [`research/drivers/echo_delay_v2_number_check.py`](drivers/echo_delay_v2_number_check.py) — gating via `make verify`
**Supersedes:** [`research/2026-08-04_echo-delay-regulated-sum_prereg-FROZEN.md`](2026-08-04_echo-delay-regulated-sum_prereg-FROZEN.md) (v1) as a **versioned successor**. **v1's `DELAY-NOT-CERTIFIED` verdict on `CFG-B` stands as a historical fact and is NOT converted by this document.**
**Class:** DERIVATION result (research-doc; **mints no `clm-`/`def-`/`exp-`/`sup-`/`ilk-`; propagates to no KB/manuscript leaf; changes no solidity; edits no falsification ledger**). Engine `src/ave` byte-untouched.
**SVA pilot case 3.** The per-row fill experience, including the two voluntarily-adopted pilot-2 amendments, is logged in §9.

---

## REGIME HEADER (mandatory, restated at the point of reading)

**MODE** — small-signal AC transit time **and small-signal AC reflection** on a static DC bias, **shear (T2) channel**; the drive is a **REAL** frequency (a scattering problem), not a complex eigenvalue. **REGIME** — sub-yield lossless-reactive on `r > r_sat`; the Regime-IV interior is **not in the domain**. **PHASE-STATE** — cold lattice, Op14 ON as a static constitutive grade, `A(r) = r_sat/r`, `A = 1` exactly at `r_sat`. **No port is crossed and no loss word is used anywhere in this lane.**

**Register, and its carves.** Y8 is written in the **SEMICONDUCTOR** register by ruling: *depletion edge*, *depletion width*, *junction two-port*, *reach-through*. What is depleted is **signal-band support, not charge**; the edge is **drive-frequency-indexed**; **no space-charge or built-in-field electrostatics rides along** — small-signal network topology only. **"Tunnelling" and bare "skin" are not used anywhere in this lane.**

---

## HEADLINE

> **★ PART 1 IS FULLY RE-CERTIFIED, AND THE NEGATIVE CONTROLS ARE THE RECEIPT.** `CFG-A` **and** `CFG-B` are both `DELAY-CERTIFIED`. **`208` v1 numbers were recomputed and reproduced to EXACT STRING EQUALITY at v1's own 17-significant-digit rendering** — `37` on the certified CFG-A set (`G-NC-V1A`) and `171` on the CFG-B diagnostics (`G-NC-V1B`) — **zero mismatches, `BIN-STOP-V1` not fired.** v1's diagnosis was right in the strongest available sense: **the gates were wrong and the numbers were not.**
>
> **★ THE TWO REPAIRED GATES PASS, AND THE REPAIRED LAW WAS RE-DERIVED, NOT IMPORTED.** `G-DISC` now compares the measured **one-way** discrete-minus-continuum offset against `K_disc(θ) = [ln θ − ψ(θ)]/2` evaluated from mpmath's digamma: `0.28860783245078786` against `0.28860783245076643` at `θ = 1`, a relative separation of `7.42451e-14` against the **CARRIED-UNCHANGED** `1 %` tolerance — **twelve orders of headroom.** `G-DECADE` limb (a) measures `1.07492e-5` against the resized `1e-4`, and the **new, strictly strengthening** residual limb (b) measures `3.78771e-5` against `1e-3`, confirming the derived `S²` **shape** and not merely its size.
>
> **★ AND THE THING v1 COULD NOT ADJUDICATE IS NOW ADJUDICATED: `BIN-DISC` FIRES.** With CFG-B certified, the branch separation `|T_B − T_A|` exceeds one substrate-native ringdown damping time at **every** mass on the frozen grid, by `38.572647555121522` to `43.211236462486767`, with the branch ratio running `48.757416585255579` to `54.500528268180376`. **FORK-3(b) is echo-discriminable by TIMING.** `BIN-DA-CLOSED`, `BIN-DB-NODE`, `BIN-CUTOFF-ROBUST` on both configurations and `BIN-EVAN-CLEAR` at both bracket ends are likewise adjudicated. **This is v1's one genuinely open question, answered.**
>
> **★ PART 2: THE DEPLETION WIDTH IS ZERO EVERYWHERE, EXACTLY, AND THAT PART IS A CONFIRMED DERIVATION.** Across the frozen ringdown band, both band-top bracket ends, both `θ` cutoffs and every variant, `W(ω) = 0` cells. The junction two-port is the `2×2` **identity to all digits**, `|T|²` through the depleted section is `1` **exactly**, and the depletion edge lies **inside the innermost intact cell**. The margin is honest and it is thin at the closest corner: the crossing `Ω = 2θβ` sits only `1.9019809107871689×` above the band top at `θ = 0.5`, `β = 5.4414`. **Hand-evaluated at freeze and disclosed in prereg §7Y.5 — reported as a confirmed derivation, not as a discovery.** Under RHO-A the edge is inside the last cell by `3.83653e-29` in `S`, and the reach-through question is **MOOT**.
>
> **★ AND THE REAL PART-2 RESULT, WHICH IS A NEGATIVE ONE: `Y8-NOT-CERTIFIED`, BECAUSE `Γ_in` AT A NEAR-WALL PLANE IS NOT A WELL-POSED OBSERVABLE UNDER RHO-B.** `G-KWIN` measures a window spread of `0.641547` against a frozen `1e-3`. The cause is derived exactly and it is not numerical: **the local reference impedance at the plane runs as `1/√K` without bound** — measured at `0.010000000000000047`, `0.0031622776601685281`, `0.0010000000000004532` for `K = 10⁴, 10⁵, 10⁶`, i.e. `1/√K` to eleven digits — so moving the plane outward changes what `Γ_in` is referenced to, without limit. **The freeze-time §2Y.6 convergence argument was about the reflection GENERATED per cell and did not cover the composite referenced to a moving plane. The gate caught a badly-posed observable, which is more useful than a number would have been.** `G-UNIT` also fails, at `4.72977e-12` against `1e-12`, on a second freeze-time error of a different kind (below). **No threshold is retuned; every Y8 bin is a NOT-ADJUDICATED DIAGNOSTIC.**
>
> **⚑ AND THE FLAG THAT IS MANDATORY IN THIS HEADLINE BY FREEZE.** The RHO-B log law is **STRUCTURALLY DEGENERATE** with the standard ECO / near-horizon-firewall echo law, and **Y8 makes the degeneracy WORSE, not better**: the ECO family carries a **free contact reflectivity**, so an ECO reproduces **any** `Γ_L` and therefore **any** reach-through verdict. **A detected log-form echo delay does not select AVE, and neither would a reach-through verdict.** The only structural difference remains that AVE's cutoff length is fixed where the ECO offset is a free knob — **and Y8 adds a second free knob on the ECO side.**

---

## §1 — THE GATE TABLES (measured against frozen; nothing dropped, widened or re-defined)

**Frozen:** `no gate, tolerance, band, frozen numeric parameter, bin boundary, regulator variant, self-test threshold or method element in sections 2P, 2Y, 4, 4Y, 5, 6, 7 and 7Y may be changed after any gate result is seen`.

**No frozen criterion was dropped, widened, or re-defined.**

### §1.1 PART 1 — the gates carried from v1 unchanged

| gate | scope | frozen tol | measured | verdict |
|---|---|---|---|---|
| **G-NC** ★ | CFG-A | `1e-10` rel | `7.1262679104721422e-13` | **PASS** |
| **G-JA** | CFG-A | `1e-20` | `4.22103e-42` | **PASS** |
| **G-CF** | CFG-B | `1e-25` | exactly `0` | **PASS** |
| **G-SUM** | both | `1e-12` rel | `9.62997e-14` | **PASS** |
| **G-U** | both | `1e-30` | `5.34553e-50` | **PASS** |
| **G-DISP** | both | `1e-15` | `3.7711e-50` | **PASS** |
| **G-PEAK** | both | booleans | all hold (§3.2) | **PASS** |
| **G-CANON** | both | machine / exact | holds | **PASS** |

### §1.2 PART 1 — the two repairs and the two new negative controls

| gate | frozen tol | measured | verdict |
|---|---|---|---|
| **G-DISC** ★ (LAW repaired, tolerance **carried unchanged**) | `1 %` | `7.42451e-14` rel | **PASS** |
| **G-DECADE(a)** ★ (tolerance **resized** from the derived law) | `1e-4` | `1.07492e-5` | **PASS** |
| **G-DECADE(b)** ★ (**NEW**, strictly strengthening residual limb) | `1e-3` | `3.78771e-5` | **PASS** |
| **G-NC-V1A** ★★ | exact string equality | `37` compared, `0` mismatches | **PASS** |
| **G-NC-V1B** ★★ | exact string equality | `171` compared, `0` mismatches | **PASS** |

### §1.3 PART 2 — Y8's own gates

| gate | frozen tol | measured | verdict |
|---|---|---|---|
| **G-BAND** | `1e-15` rel | `2.58337e-18` | **PASS** |
| **G-DEP** | exact integers | all agree | **PASS** |
| **G-ABCD** | `1e-14` structural / `1e-12` two-route | `1.11022e-16` / `2.84495e-16` | **PASS** |
| **G-PREC** | `1e-12` | `2.02048e-15` | **PASS** |
| **G-XTIE** ★★ | `1e-10` rel | `1.5965e-13` | **PASS** |
| **G-MFREE** | `1e-6` | `1.44774e-11` | **PASS** |
| **G-UNIT** ✗ | `1e-12` | `4.72977e-12` | **FAIL** |
| **G-KWIN** ✗ | `1e-3` abs | `0.641547` | **FAIL** |

### §1.4 The self-tests — **all twenty-one FIRE**

| self-test | frozen threshold | measured | fired? |
|---|---|---|---|
| **FT-NC** | `≥ 1e-7` | `1.0e-6` | **FIRES** |
| **FT-JA** | `≥ 1e-10` | `4.0093e-10` | **FIRES** |
| **FT-CF** | `≥ 1e-13` | `4.95172e-12` | **FIRES** |
| **FT-SUM** | `≥ 1e-3` | `0.190451` | **FIRES** |
| **FT-U** | `≥ 1e-6` | `0.00694444` | **FIRES** |
| **FT-DISP** ★ | `≥ 1e-2` | `1.12595` | **FIRES** |
| **FT-PEAK** | `≥ 1e-4` | `0.103205` | **FIRES** |
| **FT-DECADE** | `≥ 0.1` | `0.999991` | **FIRES** |
| **FT-CUT** ★★ | spread `> 0.10` on CFG-SYN | `2.96043` | **FIRES** |
| **FT-EVAN** ★ | `ω_max/ω < 1` everywhere | `0.0487309` | **FIRES** |
| **FT-TURN** ★ | `S_turn > S_last` | `0.000453` vs `1.09762e-9` | **FIRES** |
| **FT-CANON** | `≥ 1e-15` | `1.00002e-12` | **FIRES** |
| **FT-DISC** ★ NEW | `G-DISC` fails under the mutation | gate separation `0.0196078` vs `1 %` (see §2.4) | **FIRES** |
| **FT-V1** ★★ NEW | the v1 controls must be fireable | `0.80185976526440779` → `0.80185976526520965` | **FIRES** |
| **FT-W** ★ NEW | `W ≥ 1` at both bracket ends | `170` and `54` cells | **FIRES** |
| **FT-RT-C** ★ NEW | classifier returns CONTACT-GOVERNED | `0.0049751243781094578` | **FIRES** |
| **FT-RT-I** ★ NEW | classifier returns INTERFERENCE | `0.5` | **FIRES** |
| **FT-RT-E** ★ NEW | classifier returns EDGE-GOVERNED | `0.99800199800199796` | **FIRES** |
| **FT-UNIT** NEW | `≥ 1e-3` | `0.0167407` | **FIRES** |
| **FT-XTIE** NEW | `≥ 1e-7` | `9.99999e-7` | **FIRES** |
| **FT-DEP** NEW | closed form `+1` must break `G-DEP` | `1` vs `0` | **FIRES** |

**★ The three `FT-RT-*` tests are the reason `BIN-RT` is a gate and not a checklist.** Each runs the **real** recursion and the **real** classifier on a two-cell ladder whose reflection is `(1−f)/(1+f)` in closed form, and the three frozen ratios put one result **strictly inside each frozen band, deterministically, every run**. `FT-W` does the same for `BIN-W` and simultaneously exercises the `G-ABCD` two-route comparison that `W = 0` makes vacuous on the unmutated band.

### §1.5 The scope split — RUN, N/A, UNRUN

| configuration | gates RUN | N/A by construction | N/A by outcome | UNRUN by omission |
|---|---|---|---|---|
| `CFG-A` | G-NC, G-JA, G-SUM, G-U, G-DISP, G-PEAK, G-CANON, G-NC-V1A | G-CF, G-DECADE, G-DISC, G-NC-V1B (RHO-B arithmetic) | — | **none** |
| `CFG-B` | G-CF, G-SUM, G-U, G-DISP, G-PEAK, G-CANON, G-DECADE, G-DISC, G-NC-V1B | G-NC, G-JA, G-NC-V1A (RHO-A arithmetic) | — | **none** |
| `CFG-SYN` | — (self-test vehicle only; **no physics is claimed for it and it appears in no bin**) | all | — | **none** |
| `Y8` | G-BAND, G-DEP, G-ABCD, G-UNIT, G-PREC, G-KWIN, G-XTIE, G-MFREE | — | `G-ABCD`'s **two-route limb** on the unmutated band, because `W = 0` makes both routes the identity — **exercised instead under `FT-W`, at `2.84495e-16`** | **none** |

**Frozen:** `a gate that was never run cannot be counted as passed`. **No gate in this lane is UNRUN by omission.**

### §1.6 Certification, per configuration

| configuration | certification | why |
|---|---|---|
| `CFG-A` | **`DELAY-CERTIFIED`** | eight gates in scope, none failed; every self-test in scope fires |
| `CFG-B` | **`DELAY-CERTIFIED`** | nine gates in scope, none failed; every self-test in scope fires |
| `Y8` | **`Y8-NOT-CERTIFIED`** | `G-UNIT` and `G-KWIN` FAIL |

**Honoured: every Y8 number in §5 is a NOT-ADJUDICATED DIAGNOSTIC and no line of this document may be quoted as a Y8 bin outcome.** The shipped JSON gates its own Y8 bins on that verdict.

---

## §2 — PART 1: THE TWO REPAIRS, AND THE CONTROLS THAT MAKE THEM CREDIBLE

### §2.1 `G-DISC` — the law re-derived, the tolerance untouched

Prereg §2P.1 re-derived, from the digamma sum-minus-log difference and the near-wall RHO-B excess `1/v − 1/c₀ → r_sat/(2c₀x)`:

```
K_disc(theta) = [ ln(theta) - psi(theta) ] / 2        PER ONE-WAY PASS
```

**The driver evaluates it from mpmath's `digamma`; no constant is transcribed.**

| `θ` | measured one-way | derived one-way | round trip `2K_disc` | relative separation |
|---|---|---|---|---|
| `1` | `0.28860783245078786` | `0.28860783245076643` | `0.57721566490153286` | `7.42451e-14` |
| `0.5` | `0.63518142273075926` | `0.63518142273073909` | `1.2703628454614782` | `3.17573e-14` |

**Against the CARRIED-UNCHANGED `1 %` tolerance this passes with twelve orders of headroom.** The pass-count discipline the v1 failure bought is honoured throughout: `K_disc` is a **one-way** constant, its round-trip value is `2K_disc`, and no bare Euler–Mascheroni constant appears anywhere in this document without a pass count.

### §2.2 `G-DECADE` — the tolerance re-derived from the correction law, plus a new limb that tests its shape

Prereg §2P.2 derived, from `artanh(A) = ln(2/S) − S²/4 + O(S⁴)` with `A = √(1−S²)`:

```
delta(S_hi) = (S_hi^2 - S_lo^2) / (4 ln 10)  =  0.99 * S_hi^2 / (4 ln 10)
```

| decade of `S` | measured rel. deviation | derived leading law | residual vs derived |
|---|---|---|---|
| `1e-2 → 1e-3` | `1.07492e-5` | `1.07488e-5` | `3.78771e-5` |
| `1e-3 → 1e-4` | `1.07488e-7` | `1.07488e-7` | `3.7875e-7` |
| `1e-4 → 1e-5` | `1.07488e-9` | `1.07488e-9` | `3.7875e-9` |
| `1e-5 → 1e-6` | `1.07488e-11` | `1.07488e-11` | `3.7875e-11` |
| `1e-6 → 1e-7` | `1.07488e-13` | `1.07488e-13` | `3.7875e-13` |

**The measured deviation and the derived leading law agree to all six shipped figures on four of the five rungs**, and the residual on the shallowest rung is `3.78771e-5`, matching the derived next-order term `(3/8)S_hi² = 3.75e-5` to one per cent. **Limb (b) is the receipt that the `S²` SHAPE is right, not merely that the leading size is small enough** — a law with a different power fails it by orders.

### §2.3 ★ THE NEGATIVE CONTROLS — `208` v1 numbers, exact string equality, zero mismatches

| control | scope | compared | mismatches |
|---|---|---|---|
| **`G-NC-V1A`** | `𝒥_A`, `2𝒥_A`, the CFG-A delay and its dimensionless value at every mass, the closed-form comparison and its separation, the CFG-A PLANE-PEAK totals, the full CFG-A regulator sweep, and `G-NC`'s own worst separation | `37` | `0` |
| **`G-NC-V1B`** | the CFG-B delay, its dimensionless value, the log law, the log argument and the round-trip `K_disc` at every mass; the CFG-B PLANE-PEAK totals; the full CFG-B **and** CFG-SYN regulator sweeps; both barrier peaks; every turning-point row; every `BIN-DISC` row; v1's own `G-DISC` measured values; and `G-SUM` / `G-U` / `G-DISP` | `171` | `0` |

**`BIN-STOP-V1` did not fire.** The frozen criterion was `EXACT STRING EQUALITY at v1's shipped rendering`, and it holds on every one of the `208`. **v1's central claim — that its two failures were bookkeeping inside a correct calculation — is now a machine-checked receipt rather than a diagnosis.**

### §2.4 ★ ONE FREEZE-TIME WORDING IMPRECISION IN THIS LANE'S OWN PREREG, SURFACED NOT RESOLVED

`FT-DISC`'s frozen row reads: `scale the derived K_disc(theta) by 1 + 0.02 | G-DISC fails, separation >= 0.02`. **Those two clauses read on different quantities.** The **introduced** perturbation is exactly `0.02`; the **resulting gate separation** is `|1/1.02 − 1| = 0.0196078`, which is *below* `0.02` while being `1.96×` *above* the frozen `1 %` tolerance the gate is measured against.

**The substantive fire condition — that `G-DISC` FAILS under the mutation — is unambiguous and is met.** The driver ships both numbers and the disclosure verbatim. **This lane does not resolve the ambiguity in its own favour by silently choosing the reading that passes; it reports both readings and flags the imprecision** (`FLAG-FT-WORDING`, §7). It is a small instance of exactly the pattern `FLAG-FREEZE-SIZING` names.

---

## §3 — PART 1: WHAT IS ADJUDICATED

**Frozen:** `the derived statements of sections 2P and 2Y and the hand-evaluated W verdict are available before the run and may NOT be presented in the result doc as discoveries of the instrument`. **Honoured throughout.**

### §3.1 `BIN-DA-CLOSED` — RHO-A, ADJUDICATED (as in v1)

`ΔT_return^A = 2𝒥_A (r_sat/c₀)` with `𝒥_A = 1 − √π Γ(3/4)/Γ(1/4) = 0.4009298826322039`, `2𝒥_A = 0.80185976526440779`, measured `0.80185976526437822` at `62 M_⊙` (`3.68818e-14` relative), six-variant regulator spread `7.5252419456313015e-14`. **PROMPT, ACHROMATIC, REGULATOR-FREE.** Values reproduce v1 exactly and are not restated further; see §2.3.

### §3.2 `G-PEAK` — the derived outer plane, both branches

| branch | `A_peak` | `r_peak/r_sat` | `r_peak` in `GM/c²` |
|---|---|---|---|
| RHO-A | `0.72197046380103953` | `1.3850982140393763` | `9.6956874982756338` |
| RHO-B | `0.57201415970765805` | `1.7482084718166324` | `12.237459302716427` |

Both outside `r_sat = 7 GM/c²`, both ω-independent, `𝒱″ < 0` at both roots. Reproduces v1 exactly.

### §3.3 `BIN-DB-NODE` — ADJUDICATED, and it is a CONFIRMED DERIVATION

`S_turn/S_last = √(Ω/(2θβ))` contains **no mass**. Across both bracket ends, both `θ` and all four masses the ratio lies in `[0.2334174292085989, 0.58365895340449818]` — always below `1`. **The wave reaches the last intact cell; the transit delay is ACHROMATIC; the chirped-echo branch does not fire.** Hand-evaluated at v1's freeze and disclosed there; **v2 adjudicates the bin that v1 could only report.**

### §3.4 `BIN-CUTOFF-ROBUST` and `BIN-EVAN-CLEAR` — ADJUDICATED on both configurations

Regulator spread `7.5252419456313015e-14` (CFG-A) and `0.055207950189327304` (CFG-B) against the frozen `0.10`; `CFG-SYN` spreads `2.9604330615961116`, demonstrating every run that the bin CAN fire. `BIN-EVAN-CLEAR` at both bracket ends on both branches; the RHO-B innermost margins are `5.8709947439811122` and `18.354114509011853`.

### §3.5 ★ `BIN-DISC` — **ADJUDICATED, AND IT FIRES.** The fork IS echo-discriminable by timing

`τ_ring(M) = (GM/c₀³)/(ω_I M_g)` with `ω_I M_g` read programmatically from the v2.4 shipped JSON.

| `M/M_⊙` | `T_B/T_A` | `\|T_B − T_A\|` (s) | `τ_ring` (s) | `\|ΔT\|/τ_ring` |
|---|---|---|---|---|
| `1` | `48.757416585255579` | `0.0013207349980956485` | `3.4240195625884296e-5` | `38.572647555121522` |
| `10` | `51.62897242670489` | `0.014001480939037623` | `0.00034240195625884296` | `40.891942008803921` |
| `62` | `53.904369411419553` | `0.090710611005686024` | `0.0021228921288048263` | `42.729731659401589` |
| `100` | `54.500528268180376` | `0.14795611897118914` | `0.0034240195625884296` | `43.211236462486767` |

**The frozen criterion is `abs(T_return^B - T_return^A) > tau_ring(M) at EVERY mass on the frozen grid`, and it holds at every mass by a factor of `38.6` to `43.2`.** `BIN-DEGEN` did not fire; `BIN-DISC-SPLIT` did not fire.

**What this does and does not mean, stated in the same breath.** It means the **timing route to FORK-3(b) is OPEN**: the two inertia gradings predict return delays separated by far more than one substrate-native ringdown damping time, so a timing measurement could in principle distinguish them. It does **not** prefer either branch, it does **not** claim an echo exists (that needs a reflectivity at an outer plane, which §5 shows this lane could not even pose well), and **`FLAG-ECO` applies in full**: the RHO-B log law is degenerate with the ECO family, whose cutoff length is a free knob.

### §3.6 The observational-pointer DIAGNOSTIC (frozen at v1 §7.5b; NOT a bin)

`0.29` s pointer / `T`: `169.13420557105463` (RHO-A), `3.1376715360522114` (RHO-B). **The `0.29` s Abedi–Dykaar–Afshordi spacing is a CONTESTED RETROSPECTIVE re-analysis of somebody else's data, is not an `exp-` node, and cannot strengthen any AVE claim. Both branches MISS it, and FLAG-ECO applies in full: any log-form model can be brought to any delay by moving its cutoff length.**

---

## §4 — PART 2 (Y8): THE DEPLETION WIDTH — a CONFIRMED DERIVATION, and every number below is a NOT-ADJUDICATED DIAGNOSTIC

### §4.1 The frozen band, read as a POINTER

The band is the **FWHM of the v2.4 certified axial pole**, both endpoints read **programmatically** from `research/drivers/coldq_pole_v2p4_root_results.json`:

```
Omega in [ 0.84639842769755996 , 2.8609119939841977 ]        65 points, linearly spaced
omega  in [ 395.82818996672425 , 1337.9391775494924 ] rad/s   at the 62 M_sun reference mass
```

`G-BAND` reads the same `Ω_I` two ways out of that JSON (`certified_root/Omega_im_mp` and `x_sat × adjudication/omega_I_M_g`) and they agree to `2.58337e-18`.

### §4.2 `W(ω) = 0` cells, everywhere on the frozen sweep

The derived closed form is `W = max(0, ⌊Ω/(2β) + 1 − θ⌋)` — **mass-free**, exactly as `S_turn/S_last` was. `G-DEP` confirms the exact inversion and the direct node-by-node count from the cancellation-free `S_n` agree as **exact integers** at every one of the `65 × 2 × 2` sweep points.

**`W = 0` at every band point, both bracket ends, both `θ`, and every variant.** The junction two-port is therefore the `2×2` identity **to all digits**, and `|T|²` through the depleted section is `1` **exactly**. **This is not an approximation to reach-through — the depleted section is empty.**

**The margin, reported because a verdict that holds by a factor of two is reported as holding by a factor of two:**

| `θ` | `β` | `Ω_crit = 2θβ` for `W ≥ 1` | `Ω_crit` / band top |
|---|---|---|---|
| `1` | `5.4414` | `10.8828` | `3.8039618215743379` |
| `1` | `17.0111` | `34.0222` | `11.892081990477307` |
| `0.5` | `5.4414` | `5.4414` | `1.9019809107871689` |
| `0.5` | `17.0111` | `17.0111` | `5.9460409952386536` |

**The closest corner clears by `1.90×` in `Ω`.** Prereg §7Y.5 hand-evaluated this at freeze and predicted `BIN-W-ZERO` with "a margin of roughly a factor of two in `Ω` at the closest corner". **It is reported as a confirmed derivation, not as a measurement.**

### §4.3 The RHO-A side, stated explicitly

Under RHO-A the depletion edge sits at `S_dep/S_last = 3.83653e-29` at the band centre, and `W = 0` at every band point, both bracket ends, both `θ` **and every mass on the frozen grid**. **No cell is depleted before the end; the reach-through question is MOOT under RHO-A.** v1's twenty-five-orders statement is **cross-referenced** (v1 result §3.3) and its values are not restated; the two quantities are the same inequality at different sweep points.

### §4.4 `FT-W` — the machinery on a case where `W ≥ 1`, and the two-route receipt

Driving `ω × 10³` at the reference mass depletes real cells, and the junction two-port becomes non-trivial:

| `β` | `W` (cells) | junction `A` | junction `B/Z₁` (imag) | junction `C·Z₁` (imag) | junction `D` | `\|T\|²` through the depleted section |
|---|---|---|---|---|---|---|
| `5.4414` | `170` | `0.12470968062705699` | `0.19595488353083484` | `3.5964571223467896` | `2.3675520776118169` | `0.96960978625117666` |
| `17.0111` | `54` | `0.38460541760664846` | `-0.21936446048145797` | `-1.0283538461528556` | `2.0135330338655648` | `0.96706167946642363` |

**`A` and `D` are real, `B` and `C` are pure imaginary, and `det = 1` — the exact lossless-reciprocal structure, `1.11022e-16` from ideal.** The `Γ` computed through the explicit `ABCD` product and through the Schur recursion agree to `2.84495e-16`, which is the receipt that `G-ABCD`'s two-route limb is **fireable** even though `W = 0` makes it N/A-by-outcome on the unmutated band.

---

## §5 — PART 2 (Y8): THE REACH-THROUGH COMPUTATION — `Y8-NOT-CERTIFIED`, and WHY that is the result

### §5.1 The two failures, diagnosed exactly, NOT retuned

**`G-KWIN` — the frozen observable is NOT WINDOW-CONVERGENT, and the reason is structural.**

| `K` (cells) | `\|Γ_in\|` at band centre, matched contact, primary configuration | local reference `z_K/z_1` at the plane |
|---|---|---|
| `10⁴` | `0.27889663204515402` | `0.010000000000000047` |
| `10⁵` | `0.21689588446181859` | `0.0031622776601685281` |
| `10⁶` | `0.087147754287058579` | `0.0010000000000004532` |

worst spread over the whole sweep: `0.641547`, against a frozen `1e-3`.

**The reference impedance column IS the diagnosis.** Under RHO-B, `Z ∝ 1/S` and `S_n ∝ √n` near the wall, so `z_K/z_1 = 1/√K`; the table's right-hand column reproduces `1/√K` to twelve digits at every rung. **`Γ_in` at the outer face of cell `K` is referenced to a local impedance that falls without bound as the plane moves outward, so `Γ_in` cannot converge in `K`: moving the plane changes what the reflection is measured against.** Prereg §2Y.6 derived that the reflection **GENERATED** per cell is summable (`O(Ω/4n²)`) and inferred convergence from it; **that inference does not cover the composite referenced to a moving plane, and the gate caught the gap.**

**This is the substantive Part-2 result and it is a negative one: `Γ_in` at a near-wall plane is not a well-posed observable on the RHO-B taper.** A successor must either declare a **fixed** plane in advance (and pay the `~1.2e18`-cell enumeration the no-WKB ruling then demands), or find a **plane-invariant** normalization — the reflection analogue of what v1's `PLANE-∞` excess did for the delay. **Naming that is worth more than a `Γ` number would have been.**

**`G-UNIT` — a freeze-time error model that was wrong in KIND, not only in size.**

| `K` | worst `\|\|Γ_in\| − 1\|` over the mirror contacts and the whole band |
|---|---|
| `10⁴` | `3.93019e-14` |
| `10⁵` | `1.39999e-13` |
| `10⁶` | `4.72977e-12` |

against a frozen `1e-12`. Prereg §4Y.5 sized that tolerance from *"the accumulation is at worst a random walk, `√(1e6)·1e-16 = 1e-13`"*. **The measured growth is not a random walk** — it is `3.56×` over the first decade of `K` and `33.8×` over the second, i.e. **super-diffusive**. The error in the freeze-time reasoning is identifiable: a Möbius map of the disc is non-expansive in the **hyperbolic** metric, **not** in the Euclidean modulus, and its Euclidean derivative on the unit circle reaches `(1+ρ)/(1−ρ) = 1.41` at the innermost step, so local amplification compounds. **`G-PREC` shows the arithmetic itself is sound** — the float64 recursion matches an mpmath `dps = 50` recursion at `K = 10⁴` to `2.02048e-15` — **so this is a tolerance-derivation failure, not a solver defect.** Frozen at `1e-12`, measured `4.72977e-12`, **NOT retuned.**

### §5.2 What the instrument nonetheless measured (DIAGNOSTICS, not adjudicated)

`R ≡ |Γ_in|` at `K = 10⁶` under the **matched** `CONTACT-PORT` reading, over the frozen band:

| variant | `R` min | `R` max | `\|T\|²` min | 3-way contact spread (max) | mirror `D` in `r_sat/c₀` | `CHIRP-MEASURE` in `r_sat/c₀` | classifier |
|---|---|---|---|---|---|---|---|
| `Y-NODE` | `0.024143643391219775` | `0.59977908389481405` | `0.64026505052229754` | `0.97585635660957626` | `9.6010822264111564` – `25.19290950500849` | `147.45550145435237` | INTERFERENCE |
| `Y-THETA` | `0.049373451650013084` | `0.60897740865752781` | `0.62914651574476244` | `0.9506265483502403` | `10.764560991913617` – `28.410321483614396` | `176.4903551176059` | INTERFERENCE |
| `Y-MID` | `0.0097563731927808699` | `0.55985042457310985` | `0.68656750210530859` | `0.9902436268074265` | `9.4838190349435383` – `25.109318900017641` | `146.5562313792023` | INTERFERENCE |
| `Y-PITCH` | `0.007833389253405541` | `0.58274452584183356` | `0.6604088176013766` | `0.99216661074696622` | `8.3316675133448825` – `22.66459827655336` | `123.93391710141162` | INTERFERENCE |
| `Y-E2-BLO` | `0.024786408263925783` | `0.96707204806830749` | `0.06477165384496919` | `0.97521359173624567` | `2.9730467331100634` – `25.509196883896756` | `209.4048218578591` | EDGE-GOVERNED |
| `Y-E2-BHI` | `0.93910239573572574` | `0.99745517665503836` | `0.0050831705640662639` | `0.060897604264343763` | `0.39672783364561331` – `0.8961659577662765` | `2.9339625207595943` | EDGE-GOVERNED |
| `Y-STEPSOFF` (control) | `0.0` | `0.0` | `1.0` | `1.0000000000000655` | `14.392726722864362` – `14.392726722868321` | `7.7050596147068955e-11` | — |

The token the classifier returns over the frozen §4Y.4 variant set is `BIN-RT-INTERFERENCE` (`R` spans `0.007833389253405541` to `0.99745517665503847`). **It is NOT ADJUDICATED**, because `Y8` is `Y8-NOT-CERTIFIED` and because the `G-KWIN` failure means the quantity it is computed from is window-dependent. **No reach-through verdict is issued by this lane.**

**Three things in that table are nonetheless durable, because they do not depend on the plane:**

1. **`Y-STEPSOFF` is the exact control and it behaves exactly.** With the impedance steps switched off, `R = 0` identically (a matched contact stays matched through a uniform delay line), the mirror group delay is constant at `14.392726722864362 r_sat/c₀` — **matching PART 1's node-sum round trip over the same `10⁶` cells to `1.5965e-13` (`G-XTIE`)** — and `CHIRP-MEASURE` is `7.7050596147068955e-11`, i.e. **zero to eleven digits.** **The transit delay is EXACTLY achromatic, confirming v1 §2.7's achromaticity statement at the level of the reflection phase.**
2. **Every bit of the dispersion therefore comes from the impedance staircase, not from the transit.** Turning the steps on moves `CHIRP-MEASURE` from `7.7050596147068955e-11` to `147.45550145435237` and turns a constant group delay into one swinging over `9.6010822264111564`–`25.19290950500849`. **The chirp question of v1 §2.7 is thereby relocated, not answered: the band-edge mechanism v1 tested is dead (`W = 0`), and a DIFFERENT, discreteness-driven dispersion mechanism is what a successor must quantify.** Cross-referenced to v1 §2.7; its values are not restated.
3. **The near-wall two-port is MASS-FREE, as derived.** `Y-MASS-1`, `Y-NODE` (`62 M_⊙`) and `Y-MASS-100` agree to `1.44774e-11` in `|Γ_in|` across a `100×` mass lever (`G-MFREE`, frozen `1e-6`). **The Y8 machinery is measuring lattice structure, not mass.**

### §5.3 The cost of the unresolved `FLAG-CAUSAL` fork, quantified — which is the deliverable of a lane that sweeps a fork

The three frozen far-contact readings give `|Γ_in| = 1` **exactly** for both mirror readings (Ax-3 losslessness) and `R` for the matched one, so the **three-way spread of `|Γ_in|` at the plane reaches `0.9921666107469662`** on `Y-PITCH` and stays above `0.95` on every `E1` variant. **The unresolved contact question controls essentially the entire dynamic range of the observable at that plane.** Under `Y-E2-BHI` — the stiffness-lifted bracket end — the spread collapses to `0.060897604264343763`, because there the staircase itself already reflects `~99 %` and screens the contact.

**Read plainly: on the primary reading the depleted section provides NO isolation between the observable and Grant's open `FLAG-CAUSAL` question.** That statement is a **diagnostic**, not a bin — it is computed at a plane the `G-KWIN` failure shows to be ill-defined — but its *sign* is robust, because a `W = 0` junction two-port is the identity **exactly**, and an identity two-port cannot screen anything.

### §5.4 The ripple period, reported whatever the bin (frozen requirement)

Derived in closed form from the digamma sum at the primary window and cross-checked against the directly accumulated one-way phase:

```
Delta_Omega_ripple = pi / [ (1/2)( psi(K + theta) - psi(theta) ) ]
   closed form : 0.43655281088589632
   direct sum  : 0.43655281088586906
   in rad/s at 62 M_sun : 204.15906185921684
   ripple periods across the frozen band : 4.6145930482009423
```

**The two methods agree to eleven digits, and the `65`-point sampling gives `≈ 14` samples per ripple period — the sizing frozen in prereg §4Y.2 from this derived period, before any curve existed.**

---

## §6 — DISCRIMINATION NOTE: what this result does and does NOT mean

**Written under `consistency-vs-emergence` and `ave-discrimination-check`, to the standard the prereg fixed in advance rather than the standard the result invites.**

### §6.1 What is genuinely established

1. **The v1 instrument re-certifies on BOTH branches with its two gate constants repaired, and `208` v1 numbers reproduce to exact string equality.** The repairs are re-derivations, not imports: `K_disc(θ) = [ln θ − ψ(θ)]/2` comes out of the digamma sum-minus-log difference, and the decade tolerance comes out of `artanh(A) = ln(2/S) − S²/4 + O(S⁴)`. **FORM-class**, both.
2. **`BIN-DISC` is adjudicated and fires: FORK-3(b) is echo-discriminable by TIMING**, by `38.6`–`43.2` substrate-native ringdown damping times at every mass on the frozen grid. **FORM-class on the ratio; VALUE-CONSISTENCY on every SI-second value**, which rides `G`, `M`, the GR-imported `ν_vac` and the definitional `ℓ_node`.
3. **`W(ω) = 0` exactly, everywhere on the frozen band, at both bracket ends and both `θ`, and the depleted section's two-port is the identity.** The reach-through limit is reached **exactly**, not approximately. Mass-free, derived, and confirmed. **The `1.90×` margin at the closest corner is reported, not smoothed.**
4. **The transit delay is EXACTLY achromatic at the level of the reflection phase** (`CHIRP-MEASURE` `= 7.7050596147068955e-11` on the steps-off control, and the mirror group delay reproduces PART 1's node sum to `1.5965e-13`). **This upgrades v1's turning-point inequality to a phase-level statement.**
5. **The near-wall two-port is mass-free to `1.44774e-11` across a `100×` mass lever** — derived at freeze, tested rather than asserted.
6. **A negative, and it is the useful kind: `Γ_in` at a near-wall plane is not a well-posed observable on the RHO-B taper**, because the local reference impedance runs as `1/√K`. **The lane's own gate is what established this, and the frozen tolerance was not moved to hide it.**

### §6.2 What is NOT established, without hedging

1. **No reach-through verdict.** `Y8` is `Y8-NOT-CERTIFIED`; `BIN-W`, `BIN-RT` and `BIN-RHOA-MOOT` are all reported as **NOT-ADJUDICATED DIAGNOSTICS**. The `BIN-RT-INTERFERENCE` token in the shipped JSON is a classifier output on an uncertified configuration and **may not be quoted as a verdict**.
2. **Nothing about which inertia grading canon means.** Frozen: `this lane computes under both branches; it does not prefer RHO-A over RHO-B or RHO-B over RHO-A, and a cleaner number on one branch is not evidence for that branch`. **`BIN-DISC` says the branches are DISTINGUISHABLE, not which one is right.** The fork is exactly as open as it was.
3. **Nothing about `FLAG-CAUSAL`.** Swept at `Γ_L ∈ {0, −1, +1}`; **not resolved**; no reading preferred. What the lane adds is the **cost**: the three-way spread reaches `0.9921666107469662`.
4. **Nothing about whether an echo TRAIN exists.** No reflectivity at any plane outside the frozen near-wall window is computed, and §5.1 shows this lane could not even pose that quantity well. **A location is not a mirror, and an inner reflection at an ill-posed plane is not an echo.**
5. **Nothing observational.** No dataset analysed. The `0.29` s number is a cited in-repo pointer.
6. **Nothing that discriminates AVE from ECO models.** `FLAG-ECO` applies in full and **Y8 widens it**: the ECO family's contact reflectivity is a free knob, so an ECO reproduces any reach-through outcome. **A reach-through verdict, had one been issued, would have discriminated nothing.**
7. **Nothing about the 3D-srs correction**, nothing about whether the lattice pitch is strained (`R4` / `Y-PITCH` sweep it), nothing about the band-top ruling (`β` swept), and nothing about the node-vs-bond impedance placement (`Y-MID` sweeps it; it moves `R` at the band centre from `0.087147754287058579` to `0.085629935420768133`, i.e. by about `2 %`, on a quantity that is itself ill-posed).
8. **Nothing Cosserat, nothing polar, nothing about spin, and no eigenvalue of any kind.**

### §6.3 The honest classification

**This is a DERIVATION result with two exact negative controls against a merged predecessor, one part fully re-certified and carrying four adjudicated bins including the one its predecessor could not reach, and one part that failed its own gates and returned a well-posedness finding instead of a number.** The thing in it that could ever become an AVE-distinct forward prediction — a `~50×` split in echo timing between the two inertia gradings at a fixed parameter-free cutoff length — **remains structurally degenerate with the ECO echo family**, and Y8 makes that degeneracy worse rather than better. **This document is not a chord and does not present itself as one.**

---

## §7 — FLAG-DON'T-FIX: what is routed, and to whom

1. **★ `FLAG-ECO`, EXTENDED BY Y8** — mandatory in the headline by freeze, and it is there. The ECO family carries a **free contact reflectivity**, so it reproduces any `Γ_L` and any reach-through outcome. **Y8 adds a second free knob on the ECO side.** Routed to the discrimination lane, unresolved.
2. **★ `FLAG-CAUSAL`, SHARPENED AND STILL GRANT'S** — is a termination of infinite continuum electrical length a port or a mirror? v1 made the electrical length finite; **v2 quantifies the cost of not answering: on the primary reading the three-way `|Γ_in|` spread reaches `0.9921666107469662`, i.e. the unresolved fork controls essentially the whole dynamic range of the observable, and a `W = 0` junction two-port — being the identity exactly — cannot screen it.** Swept at `Γ_L ∈ {0, −1, +1}`; **NOT resolved**. → **Grant.**
3. **★ `FLAG-PLANE-RT` — NEW, and it is the real Part-2 finding.** `Γ_in` at a near-wall plane on the RHO-B taper is **not window-convergent**, because the local reference impedance runs as `1/√K` without bound. **A successor must declare a fixed plane in advance — and then pay the `~1.2e18`-cell enumeration the no-WKB ruling demands — or construct a plane-invariant reflection observable, the `Γ` analogue of what v1's `PLANE-∞` excess did for the delay.** → **the orchestrator, as a scoping decision before any successor is dispatched.**
4. **★ `FLAG-PLACEMENT` — NEW.** Node-uniform vs bond-midpoint impedance placement differ only at the innermost cell, by the full `√2` step, which is exactly where the reflection is generated. Swept as `Y-MID`; it moves `R` at the band centre by about `2 %`. **Neither preferred; the constitutive question is left open.** → **Grant / a successor.**
5. **★ `FLAG-REGISTER` — NEW, a vocabulary flag rather than a physics one.** On the **adjudicated** distributed cell model the band top is a **Bragg / half-wave resonance**, not an evanescence onset, so the semiconductor register's *depletion-edge* connotation does **not** carry over. **This lane used the ruled vocabulary and carved the connotation out explicitly (prereg §0.4 and §0.1 item 2); it proposes no vocabulary change.** → **the auditor lane, if the register is to be reused.**
6. **★ `FLAG-FT-WORDING` — NEW, this lane's own prereg.** `FT-DISC`'s frozen row's two clauses read on different quantities (§2.4). **Surfaced, both readings reported, not resolved in this lane's favour.** → **the orchestrator, as a data point on freeze-time wording.**
7. **★ `FLAG-FREEZE-SIZING`, THIRD INSTANCE, AND NOW WITH A DIAGNOSIS OF WHY.** This is the **third consecutive lane in this arc** to land NOT-CERTIFIED on freeze-time sizing rather than on physics (the axial RHO-B lane logged four; v1 logged two; v2 logs two — **both in the half of the lane that had no predecessor to control against**). ★ **And that is the pattern worth the orchestrator's attention: PART 1, which had `208` predecessor numbers to reproduce, certified cleanly; PART 2, which had none, failed both of its novel tolerances.** The mechanism is now identifiable rather than merely recurrent: **a tolerance derived from an error MODEL fails when the model is wrong in kind** (`G-UNIT`: hyperbolic vs Euclidean non-expansiveness) **or when the derivation covers a different quantity than the gate measures** (`G-KWIN`: reflection generated vs composite at a moving plane). → **the orchestrator.** Raised, not answered.
8. **Carried forward BY POINTER ONLY, repaired nowhere, no edit proposed:** `FLAG-ECO-COROLLARY` (the corpus's no-log-divergence discriminator is RHO-A-conditional), `FLAG-PLANE-GAP` (the 2026-06-17 outer-reflector survey is incomplete), `FLAG-CITE-SHIFT` (`srs-band-structure.md` cites `constants.py:294` for `OMEGA_C`, which lives at `constants.py:305`), `FLAG-CANON` (the `Z_shear` sign tension at `vol3/claim-quality.md:122`/`:124`), `FLAG-PITCH`, `FLAG-BRACKET`.

---

## §8 — VALIDATION AND SCOPE DISCLOSURES

- **Determinism.** Two full runs, digest `4c7926fd9954dfc7` twice, shipped objects byte-identical apart from `_runtime_sec`. The driver emits **no** pass field for determinism; it ships the digest only, and the verdict is the external two-run diff recorded here. Runtimes are written **without back-ticks and are NOT registered**.
- **Numerical conditioning, declared in the prereg BEFORE the code and load-bearing here.** At the innermost node `ℓ_node/r_sat = 6.0238983090250982e-19`, so any float64 `1 − A²` by subtraction returns **exactly zero**; every near-wall quantity is computed from `S² = x(2r_sat + x)/(r_sat + x)²` and every `S^{-p} − 1` from `expm1(−p/2 · log S²)`. The decade sweep differences two `artanh` values of order `40` to expose a relative deviation of order `1e-13` — about **fourteen digits of cancellation** — and runs at mpmath `dps = 50`. **Every float64 path has a gate that measures its own error:** `G-SUM` and the two v1 controls for the node sum; `G-UNIT`, `G-PREC` and `G-KWIN` for the Schur recursion. **`G-PREC` is the receipt that the float64 recursion is sound (`2.02048e-15` against an mpmath `dps = 50` re-run), which is what makes the `G-UNIT` failure diagnosable as a tolerance-derivation error rather than a solver defect.** ★ **The conditioning row caught something real: the `1 + ρΓ` denominator of the Schur recursion was checked at freeze and shown bounded (`|ρ_n| ≤ 0.1716`), which is why the recursion was chosen over the `ABCD` route — and the `ABCD` route would have divided by zero on the two `|Γ_L| = 1` terminations that carry half the result.**
- **The gating number check** implements the six accumulated checker lessons, v1's seventh (**mutation receipt**) and v1's span-splitting fix.
- **Engine fence.** `src/ave` byte-untouched; `ave.core.constants` imported read-only.
- **Predecessor fence.** v1's prereg, result and three driver files; `research/drivers/coldq_pole_v2p4_root_results.json`; and `src/scripts/vol_3_macroscopic/bh_shear_echo_delay.py` are **imported READ-ONLY**, neither edited nor re-scored. **v1's `DELAY-NOT-CERTIFIED` verdict is neither edited nor withdrawn.** Discharged by an empty `git diff --stat` against the freeze base on each.
- **Scope fence.** `research/` and one docket fragment only, plus exactly one appended `Makefile` target; no manuscript or KB file edited; no fork adjudicated.
- **Makefile conflict disclosure.** The new target is its own recipe, but the `.PHONY` line and the `verify:` prerequisite line **ARE shared** with every other lane's number-check target and are a **REAL two-line union-conflict class** with any concurrent lane.
- **Canonical inputs, for the record:** `ℓ_node = 3.8615926772428334e-13` m, `ω_C = 7.76344071105011e+20` rad/s, `r_sat(62 M_⊙) = 641045.46244702291` m, `r_sat/c₀ = 0.0021382974966202216` s, `Ω_v24 = 1.8536552108408788`, `ω_ringdown = 866.88368375810832` rad/s.
- **Scope, unchanged:** `ℓ = 2` is an input; `ν_vac`, `K = 2G` and the `7` in `r_sat` are GR-imported and untouched; `ℓ_node` is definitional; spin is out of scope; no Cosserat channel, no polar branch, no eigenvalue, no reflectivity at any outer plane, and no completeness statement of any kind.

### §8.1 ROUTED FOLLOW-ONS (named, NOT started)

1. **A plane-invariant reflection observable for the RHO-B taper** — the `Γ` analogue of `PLANE-∞`. Without it, `FLAG-PLANE-RT` blocks any reach-through successor. **This is the gating item.**
2. **A `G-UNIT` tolerance derived from the correct (hyperbolic) contraction property**, or an mpmath recursion at the primary window, either of which would let a successor certify the losslessness receipt.
3. **The discreteness-driven dispersion mechanism** the steps-on `CHIRP-MEASURE` exposes — the chirp question of v1 §2.7 has moved from the band edge to the impedance staircase and needs its own instrument.
4. **A reflectivity at the derived barrier plane** (`r_peak = 1.7482084718166324 r_sat` under RHO-B), without which no echo TRAIN can be claimed on either branch.
5. **The auditor-lane disposition** of `FLAG-ECO-COROLLARY`, `FLAG-PLANE-GAP`, `FLAG-CITE-SHIFT` and `FLAG-CANON`, all carried forward unrepaired.

---

> **Result provenance.** Resolves the frozen gates and bins of `research/2026-08-05_echo-delay-v2-reach-through_prereg-FROZEN.md` (commit `db98550b`, COMMIT 1 of this lane, pushed **ALONE** before any driver code existed and before any number produced by this instrument existed). All numbers above are read from the shipped `research/drivers/echo_delay_v2_reach_through_results.json` and are machine-verified against it by `research/drivers/echo_delay_v2_number_check.py`, wired into `make verify`. **Mints no `clm-`/`def-`/`exp-`/`sup-`/`ilk-`; propagates to no leaf; engine byte-untouched; falsification ledger untouched.** Companion: the docket fragment `_orchestration/docket-entries/2026-08-05-echo-delay-v2-reach-through.md`.

---

## §9 — ★ SVA PILOT CASE 3: the per-row fill experience, plus the two pilot-2 amendments exercised

`manuscript/ave-kb/common/standard-vacuum-analysis.md` §3 asks each pilot to score every row **FILLED / FILLABLE-BUT-MISSING / NOT-APPLICABLE** and to log gaps. This lane filled the §0 header **before** §2P and §2Y existed. Scored honestly, including where a row did nothing.

| row | score | what filling it actually did **in this lane** |
|---|---|---|
| **1 · Sector / ownership** | **FILLED** | **Higher value than in pilot 2, and for a reason worth recording: the RULED REGISTER made it load-bearing.** A semiconductor vocabulary invites a charge owner; row 1 is where the sentence *"the depleted quantity is T2 signal-band support, NOT charge, NOT an A1 reservoir, NOT a Cosserat winding"* had to be written down. **On a borrowed-register problem, row 1 stops being cheap insurance and starts being the carve.** |
| **2 · Regime / phase-state** | **FILLED** | **High, and it added a regime axis v1 did not need.** Y8 is a **REAL-frequency scattering** problem, not a complex-eigenvalue mode problem. Declaring that in row 2 is what let §2Y.4 state — cleanly and without appearing to criticise the axial lane — that `Re(σ₊ − σ₋) = 0` at real `Ω` bears on **no** eigenvalue lane. **Without row 2 that would have read as a contradiction with a merged lane instead of a scope statement.** |
| **3 · Circuit statement** | **FILLED** | **HIGH VALUE, again, and it decided the algorithm.** Stating the object as a ladder terminated by an *unresolved contact* is what made `Γ_L` a **three-valued sweep** rather than a choice, and made *"how much does the unresolved fork cost the observable"* the deliverable of a lane that cannot resolve it. **§5.3 exists because of row 3.** |
| **4 · Plane & projection** | **FILLED** | **HIGHEST VALUE — and this time it produced the lane's central NEGATIVE.** Row 4 forced *"every `Γ` is referenced to the LOCAL characteristic impedance at its own plane"* into the freeze. That declaration is exactly what made the `1/√K` reference drift **visible and gateable** instead of silently absorbed. **A lane that had not declared its plane would have shipped a `Γ` number and called it reach-through.** |
| **5 · Constitutive provenance** | **FILLED** | High. Tagging `Z = ρ_bulk c₀ S^{1−p}` **DERIVED** (one line from `μ` and `p`) versus `Γ_L` **FORKED** versus the electrical-length reading **ENG-CHOICE** is what keeps §6.2 item 3 honest. See the two amendment notes below. |
| **6 · Energy ledger** | **FILLED** | **High and directly instrumental.** *"No port is crossed; `Re{Z} = 0` at every cell by Ax 3"* is what turns `\|Γ_in\| = 1` for a `\|Γ_L\| = 1` termination into a **gate** (`G-UNIT`) rather than an assumption — and it is why `\|Γ_in\|` under the matched contact is a clean measurement of the ladder alone. **The row generated a gate.** |
| **7 · Calibratability** | **FILLED** | Moderate. Confirmed every Y8 verdict-class output is already dimensionless (`\|Γ\|`, `\|T\|²`, an integer `W`, a slope in `r_sat/c₀`), so the α-cleanliness argument was two lines instead of a paragraph. |
| **8 · Discrimination class** | **FILLED** | **HIGH VALUE, and it cost the lane its most quotable result before the result existed.** Running the SM/GR counterfactual at freeze is what produced the sentence *"the ECO family carries a free contact reflectivity, so it reproduces any `Γ_L` and therefore any reach-through verdict"* — **before** any verdict. Had `BIN-RT` been adjudicated, that sentence would have been the hardest thing in the document to write afterwards. **The row converted a potential overclaim into a frozen headline requirement, for the second pilot running.** |
| **9 · Certification plan** | **FILLED** | **High — and it is the row that failed half the lane, correctly, twice.** Two gates caught two freeze-time errors, and the two negative controls it forced are what make PART 1's certification credible rather than self-reported. |
| **10 · Adjudication routing** | **FILLED** | **Higher than in pilot 2, because of the cross-part gate.** Naming in advance that *"Y8's bins are additionally gated on CFG-B being DELAY-CERTIFIED"* made the whole `Y8-NOT-CERTIFIED` cascade mechanical. **Nothing had to be decided at result time.** |
| **11 · Numerical conditioning** *(pilot-2 proposal, adopted voluntarily)* | **FILLED — and it CAUGHT SOMETHING, twice** | **see below** |

### §9.1 ★ Did the NUMERICAL CONDITIONING row earn its keep? — YES, with a named limitation

**It caught two things, and one of them changed the algorithm.**

1. **★ It selected the solver.** Row 11 required naming every cancellation *before writing the first expression*. Working through the `1 + ρΓ` denominator of the Schur recursion — bounded here, because the largest impedance step is the innermost `√2` and `|ρ_n| ≤ (√2−1)/(√2+1) = 0.1716` — is what surfaced that the **obvious** route, an explicit `ABCD` product with `Z_in = (A Z_L + B)/(C Z_L + D)`, **divides by zero on both `|Γ_L| = 1` terminations**, where `Z_L` is `0` or `∞`. **Those two terminations carry half the result** (`G-UNIT`, the achromaticity measurement, and the whole `FLAG-CAUSAL` cost estimate). Without row 11 the lane would have discovered that at integrator time and probably by patching an epsilon into a denominator. **The row picked the Möbius formulation, and the `ABCD` product survives as the ruling-mandated reporting form and a two-route cross-check.**
2. **It forced a physics fact to be stated as a numerical guarantee, with its own fence.** The accumulated phase over `10⁶` cells is only `≈ 27` radians round-trip — **because the delay law is logarithmic** — so no argument-reduction blow-up occurs. Row 11 required saying so **and** required flagging that this does **not** carry over to a power-law profile, which is exactly the `CFG-SYN` class a successor might reach for.
3. **★ AND THE LIMITATION, WHICH IS THE MOST USEFUL THING THIS PILOT CAN REPORT.** **Row 11 as proposed did NOT catch the `G-UNIT` failure, and could not have.** It asks for *cancellations, dynamic range, working precision* — i.e. the conditioning of individual **expressions**. `G-UNIT` failed because the freeze-time **error-PROPAGATION model over an iterated map** was wrong in kind: a Möbius map of the disc is non-expansive in the **hyperbolic** metric, not in the Euclidean modulus the gate measures. **Candidate refinement, offered as feedback and not as a change: row 11 should additionally require, for any iterated map or long accumulation, that the error-propagation model be named TOGETHER WITH THE METRIC IT CONTRACTS IN.** Three of this arc's freeze-time failures have now been tolerance-derivation errors rather than expression-conditioning errors.

### §9.2 ★ Did the `BRACKETED(pending-ruling)` tag earn its keep? — YES, and it did something the other tags could not

`β ∈ {5.4414, 17.0111} ω_C` is neither DERIVED nor IMPORTED nor FORKED-with-an-id nor ENG-CHOICE, and v1 had to write it as *"DERIVED-FORM, BRACKET OPEN"* in prose. **With the tag available, three things became sayable in one word each:**

1. `β` enters Y8 **only** through `W` under the primary `E1` reading — so the bracket's blast radius is **localized to one integer**, and that is a one-line statement instead of a paragraph.
2. Under the `E2` variant the bracket ends give **materially different behaviour** (`Y-E2-BLO` spans `R` from `0.024786408263925783` to `0.96707204806830749`; `Y-E2-BHI` sits at `0.93910239573572574`–`0.99745517665503836` with a three-way contact spread of only `0.060897604264343763`, i.e. the staircase screens the contact at the stiffness-lifted end). **The tag makes it unambiguous that this spread is a PENDING RULING and not a physical uncertainty.**
3. It stopped the temptation to quote a "central value". **There is no central value of a pending ruling.**

**One gap the tag does not close, offered as further feedback:** the far-contact condition `Γ_L ∈ {0, −1, +1}` is genuinely **FORKED**, but the fork has no `fork-` id — it is carried by a flag name (`FLAG-CAUSAL`). Row 5's `FORKED(fork-id)` slot therefore had to be filled with a flag name. **Suggest that a fork which a lane SWEEPS should get an id at the moment it is first swept, so the sweep is greppable.**

### §9.3 Friction, reported because the pilot asks for it

1. **Eleven rows still took under an hour and still preceded the derivation.** No row was un-fillable. **The header is still cheap.**
2. **★ The ordering matters more on a ruled-register problem than pilot 2 found.** Rows 1 and 4 did the heavy lifting here (the carve and the plane), where in pilot 2 row 1 caught nothing. **The variance is in the PROBLEM CLASS, not in the rows** — which is an argument for keeping all of them rather than pruning by average utility.
3. **The header has no row for CONTROLS AGAINST A PREDECESSOR**, and this lane's single most decisive discipline was the `208`-number exact-string-equality reproduction of v1. Row 9 mentions negative controls in passing. **On a rerun-class lane that is the whole game, and it is worth more than a clause.** Offered as feedback; **not proposed as a change.**

**Pilot verdict from this lane, and it is only one data point:** rows 1, 3, 4, 8 and the adopted row 11 each changed what this lane computed or how it reported it, before any number existed — and row 4 is directly responsible for the lane's central negative being **found** rather than **shipped as a number**. **Both pilot-2 amendments earned their keep on this problem, and row 11 earned it with a named limitation attached. The canonization decision is Grant's and this log is input to it, not a vote.**

---

> **⚑ ORCHESTRATOR REVIEW BLOCK (Tier-2 verify processed, 2026-08-05; body above preserved per
> Rule 12).** The independent audit CONFIRMED the load-bearing results — BIN-DISC re-derived
> 17-digit identical from canonical sources on the unchanged v1 criterion; the W=0 closed form
> re-derived and unbreakable (including the FT-W kill-test values); the K_disc law re-derived
> independently; the G-UNIT hyperbolic-vs-Euclidean diagnosis verified exactly (the innermost
> disc-automorphism derivative is exactly √2). Corrections from the audit, applied here:
>
> 1. **FT-DISC adjudication (orchestrator ruling, Grant-overridable).** The frozen row's two
>    clauses read on different quantities, and the literal sub-clause "separation ≥ 0.02" is
>    **arithmetically unsatisfiable by its own construction**: a 1.02 scaling yields
>    |1/1.02 − 1| = 0.0196078 < 0.02 for any inputs. A criterion impossible at freeze is
>    vacated, not failed (the vacated-cite principle applied to a frozen clause). The operative
>    fireability content — the perturbed law makes G-DISC FAIL (separation 1.96× the unchanged
>    1% tolerance) — is SATISFIED. CFG-B's certification therefore STANDS on the fireability
>    reading, with this receipt, not on a silent choice.
> 2. **G-KWIN scope softened:** the audited statement is that Γ_in at a near-wall plane is NOT
>    PLANE-INVARIANT / ill-posed as posed (the reference impedance runs as 1/√K); the docket's
>    "cannot converge" overstates — the shipped |Γ_in| sequence is monotone-decreasing and
>    consistent with a limit. Corrected in the companion docket correction file.
> 3. **FLAG-PLANE-RT gains a third option** (audit finding): fix the REFERENCE IMPEDANCE (e.g.
>    Z₁ or the asymptotic Z — the standard pseudo-wave/power-wave renormalization) and let the
>    plane move. The successor scoping decision now weighs three routes, not two.
> 4. **G-PREC caveat:** frozen at K=10⁴ only — the window where G-UNIT passes. It does not
>    certify the arithmetic at K=10⁶ where G-UNIT fails; "tolerance-derivation failure, not
>    solver defect" is the best-supported reading but carries this caveat (the lane's own routed
>    follow-on (b) concedes it).
> 5. **§2P.2 wording corrected:** G-DECADE's tolerance WAS widened (1e-6 → 1e-4) after v1's
>    result exposed the sizing error — legitimately, under the versioned-successor discipline
>    (frozen in db98550b before any v2 number), and the sentence claiming otherwise overstated.
>    Likewise: v1's prereg §4.5 pre-disclosed the O(S²) ORDER; the coefficient first appears in
>    v1's result. And G-DECADE(b) is strengthening RELATIVE TO LIMB (a) — the v2 decade gate
>    remains 100× looser than v1's unsatisfiable original at leading order.
> 6. **Disclosure repairs:** the checker shipped as `echo_delay_v2_number_check.py` while the
>    prereg froze the name `echo_delay_v2_reach_through_number_check.py` — frozen SUBSTANCE
>    honoured, artifact NAME silently changed; disclosed here. The Makefile `help:` echo line is
>    a third shared line in the union-conflict class. FT-V1's fireability receipt mutates a V1A
>    target only; "the negative controls are fireable" is over-general for V1B.
> 7. **FLAG-REGISTER upgraded to a ruled fourth carve** (audit-confirmed): the srs net has NO
>    internal stop-band — the band TOP is a Bragg/half-wave resonance, not a band-GAP edge; the
>    semiconductor register's depletion connotation must not be read onto band-top physics.
>    Landed as carve 4 in the translation leaf (PR #881).
