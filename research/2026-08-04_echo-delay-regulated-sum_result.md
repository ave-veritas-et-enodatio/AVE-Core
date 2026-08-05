# The LATTICE-REGULATED optical return delay to the `r_sat` wall — RESULT: **RHO-A `DELAY-CERTIFIED` and `BIN-DA-CLOSED`; RHO-B `DELAY-NOT-CERTIFIED` on two gates this lane's own §2.8 algebra got wrong.** The turning point is NODE-governed, the delay is ACHROMATIC, and the fork's timing signatures differ by ~50×

**Date:** 2026-08-04
**Prereg-file**: research/2026-08-04_echo-delay-regulated-sum_prereg-FROZEN.md
**Prereg-commit:** `1da06a90` (frozen and pushed **ALONE**, before any driver code and before any number produced by this instrument existed)
**Driver:** [`research/drivers/echo_delay_regulated_sum.py`](drivers/echo_delay_regulated_sum.py) → [`research/drivers/echo_delay_regulated_sum_results.json`](drivers/echo_delay_regulated_sum_results.json)
**Number check:** [`research/drivers/echo_delay_regulated_sum_number_check.py`](drivers/echo_delay_regulated_sum_number_check.py) — gating via `make verify`
**Class:** DERIVATION result (research-doc; **mints no `clm-`/`def-`; propagates to no KB/manuscript leaf; changes no solidity; edits no falsification ledger**). Engine `src/ave` byte-untouched.
**Provenance:** Grant's GO of 2026-08-04 (core session, "delay derivation first"), following his catch on PR #876 that the RHO-B optical divergence is a **continuum-limit** property and the physical path is a **finite node sum**. Written against `origin/main` = `2877eaa0`.
**SVA pilot case 2.** The per-row fill experience is logged in §9.

---

## REGIME HEADER (mandatory, restated at the point of reading)

**MODE** — small-signal AC transit time on a static DC bias, **shear (T2) channel**. **REGIME** — sub-yield lossless-reactive on `r > r_sat`; the Regime-IV interior is **not in the domain**. **PHASE-STATE** — cold lattice, Op14 ON as a static constitutive grade, `A(r) = r_sat/r`, `A = 1` exactly at `r_sat`. **No port is crossed and no loss word is used anywhere in this lane**: the delay is a pure reactive transit time on a lossless ladder.

---

## HEADLINE

> **★ THE NEGATIVE CONTROL PASSES BY THREE ORDERS OF HEADROOM.** This lane's independently mpmath-derived RHO-A tortoise delay reproduces the frozen 2026-06-17 predecessor driver at **every one of its own four** `r_out/r_sat` entries; worst relative separation `7.1262679104721422e-13` against a frozen `1e-10`. **Every RHO-B number below is produced by an instrument that provably reproduces the predecessor's RHO-A one.**
>
> **★ CFG-A IS `DELAY-CERTIFIED` AND `BIN-DA-CLOSED` IS ADJUDICATED.** Under RHO-A the excess round-trip delay is a **pure number times `r_sat/c₀`**, measured at `0.80185976526437822` against the closed form `2𝒥_A` with `𝒥_A = 1 − √π Γ(3/4)/Γ(1/4) = 0.4009298826322039`, agreeing to `3.68818e-14`. **It is ACHROMATIC and REGULATOR-FREE**: the full six-member regulator sweep spreads by `7.5252419456313015e-14`. **The predecessor's `3–10 ms` band was never an uncertainty in the substrate prediction — it was the free-flight term of an undeclared reference plane, and it is now removed by declaration.**
>
> **★ CFG-B IS `DELAY-NOT-CERTIFIED`, AND BOTH FAILURES ARE THIS LANE'S OWN FREEZE-TIME ALGEBRA.** `G-DISC` and `G-DECADE` FAIL. **No threshold is retuned and CFG-B adjudicates NO bin.** `G-DISC` fails because prereg §2.8 derived the discrete-minus-continuum offset as `γ` **per one-way pass** when it is `γ` per **round trip** — the derivation dropped the `1/2` in `v = c₀S² = 2c₀x/r_sat`. The instrument measures `0.28860783245078786` against the **corrected** `γ/2 = 0.2886078324507664`, agreeing to **thirteen significant digits**. `G-DECADE` fails because the frozen `1e-6` was sized for the asymptotic log law while the sweep's shallowest rung sits at `S = 1e-2`, where the derived `O(S²)` correction is `1.07492e-5`. **The five decades fall by exactly 100× each, which IS the `S²` signature — a stronger confirmation of the log law than a pass would have been, and still a failure as frozen.**
>
> **★ THE TURNING POINT IS NODE-GOVERNED, AND THERE IS NO CHIRP.** `S_turn/S_last = √(Ω/(2θβ))` contains **no mass**. Across both band-top bracket ends, both sub-cell placements and all four masses the ratio lies in `[0.2334174292085989, 0.58365895340449818]` — **always below 1, always by less than a factor of five.** The wave reaches the last intact lattice cell; the delay is **ACHROMATIC**; the chirped-echo branch does not fire. **This verdict was hand-evaluated at freeze and disclosed in prereg §7.7 — it is a CONFIRMED DERIVATION, not a discovery of the instrument.**
>
> **★ AND THE DERIVED OUTER PLANE THE PREDECESSOR SURVEY MISSED.** Because the local speed vanishes at the wall, the effective barrier `𝒱 = v²U` vanishes at BOTH ends and necessarily peaks in between — at `1.3850982140393763 r_sat` (RHO-A) and `1.7482084718166324 r_sat` (RHO-B), i.e. `9.6956874982756338` and `12.237459302716427` in `GM/c²`. **Both are OUTSIDE `r_sat`.** The 2026-06-17 prereg's *"there is no parameter-free outer reflector outside `r_sat`"* surveyed only imported GR radii; the profile builds its own. **Surfaced, not repaired.**
>
> **⚑ AND THE FLAG THAT IS MANDATORY IN THIS HEADLINE BY FREEZE.** The RHO-B log law is **STRUCTURALLY DEGENERATE** with the standard ECO / near-horizon-firewall echo law. A detected log-form echo delay does **NOT** select AVE. The only discriminating content is that AVE's cutoff length is fixed while the ECO offset is a free knob — **and the corpus sentence claiming AVE has "no log-divergence" is RHO-A-conditional and does not hold on the RHO-B branch.**

---

## §1 — THE GATE TABLES (measured against frozen; nothing dropped, widened or re-defined)

**Frozen:** `no gate, tolerance, band, frozen numeric parameter, bin boundary, regulator variant or method element in sections 2, 4, 5, 6 and 7 may be changed after any gate result is seen; if a configuration fails certification this lane reports DELAY-NOT-CERTIFIED for that configuration, adjudicates NO physics bin for it, and routes to a successor with a new version number`.

**No frozen criterion was dropped, widened, or re-defined.**

### §1.1 The gates

| gate | what it certifies | scope | frozen tol | measured | verdict |
|---|---|---|---|---|---|
| **G-NC** ★ | **NEGATIVE CONTROL** — this lane's RHO-A total delay vs the 2026-06-17 predecessor driver at all four of its own `r_out/r_sat` entries | CFG-A | `1e-10` rel | `7.1262679104721422e-13` | **PASS** |
| **G-JA** | the RHO-A closed form vs quadrature of its own integrand | CFG-A | `1e-20` | `4.22103e-42` | **PASS** |
| **G-CF** | the RHO-B `artanh` closed form vs quadrature of its own integrand | CFG-B | `1e-25` | exactly `0` | **PASS** |
| **G-SUM** | node-sum split-independence over `N_split ∈ {1e5, 1e6, 1e7}` | both | `1e-12` rel | `9.62997e-14` | **PASS** |
| **G-U** | the collected effective potential vs the raw transformation, 12 sampled `A` | both | `1e-30` | `5.34553e-50` | **PASS** |
| **G-DISP** | the arccos map on the `z = 2` radial cascade is exactly linear | both | `1e-15` | `3.7711e-50` | **PASS** |
| **G-PEAK** | bracketed barrier maximum, sign change, `𝒱″ < 0`, `0 < A_peak < 1`, per branch | both | booleans | all hold (§3) | **PASS** |
| **G-CANON** | every canonical constant is the imported symbol | both | machine | `1.53308e-17` / `4.73233e-17` / exactly `0` | **PASS** |
| **G-DECADE** ✗ | each decade of `S` contributes `ln 10 · (r_sat/c₀)` | CFG-B | `1e-6` rel | `1.07492e-5` | **FAIL** |
| **G-DISC** ✗ | the discrete-minus-continuum offset equals the §2.8-derived constant | CFG-B | `1 %` | `0.676507` | **FAIL** |

### §1.2 The self-tests — **all twelve FIRE**

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
| **FT-CUT** ★★ | spread `> 0.10` on `CFG-SYN` | `2.96043` | **FIRES** |
| **FT-EVAN** ★ | `ω_max/ω < 1` everywhere | `0.0487309` | **FIRES** |
| **FT-TURN** ★ | `S_turn > S_last` | `0.000453` vs `1.09762e-9` | **FIRES** |
| **FT-CANON** | `≥ 1e-15` | `1.00002e-12` | **FIRES** |

**★ The three starred self-tests are the reason the physics bins are gates and not checklists.** `FT-CUT` demonstrates every run that `BIN-CUTOFF-ARTIFACT` **can** fire, by exhibiting a profile (`p = 3`, whose continuum integral diverges as a power law rather than a log) on which the regulator spread reaches `2.96043`. `FT-EVAN` and `FT-TURN` do the same for `BIN-EVAN` and `BIN-DB-BAND`. **★ And `FT-DISP` is the receipt that the band-model adjudication is load-bearing rather than decorative:** substituting the REJECTED lumped map moves the dispersion by `1.12595` where the adjudicated arccos map is exact to `3.7711e-50`.

### §1.3 The scope split — RUN, N/A, UNRUN

| configuration | gates RUN | N/A by construction | UNRUN by omission |
|---|---|---|---|
| `CFG-A` | G-NC, G-JA, G-SUM, G-U, G-DISP, G-PEAK, G-CANON | G-CF, G-DECADE, G-DISC (RHO-B arithmetic) | **none** |
| `CFG-B` | G-CF, G-SUM, G-U, G-DISP, G-PEAK, G-CANON, G-DECADE, G-DISC | G-NC, G-JA (RHO-A arithmetic) | **none** |
| `CFG-SYN` | — (self-test vehicle only; **no physics is claimed for it and it appears in no bin**) | all | **none** |

**Frozen:** `a gate that was never run cannot be counted as passed`. **No gate in this lane is UNRUN by omission.**

### §1.4 Certification, per configuration

| configuration | certification | why |
|---|---|---|
| `CFG-A` | **`DELAY-CERTIFIED`** | seven gates in scope, none failed; every self-test in scope fires |
| `CFG-B` | **`DELAY-NOT-CERTIFIED`** | `G-DECADE` and `G-DISC` FAIL |

**Frozen:** `any RUN gate FAILS, or any self-test fails to fire, or any gate is UNRUN by omission, for that configuration` is exactly the `BIN-CERT-FAIL` condition, and the prereg's §7 precedence makes certification gate every physics bin. **Honoured: every CFG-B number in §4 and §5 is a NOT-ADJUDICATED DIAGNOSTIC and no line of this document may be quoted as a bin outcome for RHO-B.**

---

## §2 — ★ THE TWO FAILURES, DIAGNOSED EXACTLY, NOT RETUNED

**Rule 11 forbids dropping, widening or re-defining a frozen criterion after a result is seen. Both stand as frozen. Each is diagnosed here so a successor freezes the right number rather than re-discovering the wrong one.**

### §2.1 `G-DISC` — the derivation dropped a factor of two, and the instrument found it

Prereg §2.8 froze: `the discrete-sum-minus-continuum-integral difference under RHO-B is derived at freeze to be the Euler-Mascheroni constant gamma per one-way pass at theta = 1 (and gamma + 2 ln 2 at theta = 1/2)`.

**The near-wall speed is `v = c₀S² = 2c₀x/r_sat`, so `1/v = r_sat/(2c₀x)` — and the derivation used `r_sat/(c₀x)`.** The harmonic-sum-minus-log difference is `γ`, but it is multiplied by `r_sat/(2c₀)`, so in units of `r_sat/c₀` the one-way offset is `γ/2`. At `θ = 1/2` there is a second error: the continuum cut point also moves to `ℓ_node/2`, contributing `−ln 2` rather than nothing.

| `θ` | frozen "derived" | measured | **corrected derivation** | agreement with corrected |
|---|---|---|---|---|
| `1` | `0.57721566490153286` | `0.28860783245078786` | `γ/2 = 0.2886078324507664` | **13 significant digits** |
| `0.5` | `1.9635100260214235` | `0.63518142273075926` | `(γ + ln 2)/2 = 0.63518142273073908` | **13 significant digits** |

**The general corrected law, derived here and available to the successor:**

```
K_disc(theta)  =  [ ln(theta) - psi(theta) ] / 2        per ONE-WAY pass
K_disc(1) = gamma/2 ;   K_disc(1/2) = (gamma + ln 2)/2
```

using `Σ_{n=1}^{N} 1/(n−1+θ) = ψ(N+θ) − ψ(θ)` and `∫_{θℓ}^{Nℓ} dx/x = ln N − ln θ`. **Per ROUND TRIP at `θ = 1` the offset is exactly `γ`, which is what the CFG-B rows report** (`0.57721566490157572` at the reference mass) — so the frozen constant was right and its **per-pass attribution** was wrong.

**Successor's repair, named:** freeze `K_disc(θ) = [ln θ − ψ(θ)]/2` per one-way pass, and state the pass count on every discrete-correction constant.

### §2.2 `G-DECADE` — the tolerance was sized for the asymptotic law, the sweep started where it does not hold

Prereg §4.5 froze the tolerance at `1e-6` with the derivation `each decade of S must contribute ln 10 (r_sat/c_0) exactly under the log law; deviations are O(S^2)`. **The `O(S²)` disclosure is correct and the tolerance ignored it.**

| decade of `S` | rel. deviation from `ln 10` |
|---|---|
| `1e-2 → 1e-3` | `1.07492e-5` |
| `1e-3 → 1e-4` | `1.07488e-7` |
| `1e-4 → 1e-5` | `1.07488e-9` |
| `1e-5 → 1e-6` | `1.07488e-11` |
| `1e-6 → 1e-7` | `1.07488e-13` |

**Each rung is exactly 100× smaller than the one above it.** Expanding `artanh(A) = ln(2/S) − S²/4 + O(S⁴)` gives a decade deviation of `S_hi²/(4 ln 10)`, which at `S_hi = 1e-2` is `1.086e-5` — **the measured `1.07492e-5` matches the derived leading correction to one per cent.** The gate fails because its shallowest rung sits where the correction exceeds the tolerance, not because the law is wrong.

**Successor's repair, named:** either start the decade sweep at `S ≤ 1e-3`, or — better — gate the **residual against the derived `S²/4` form** rather than against zero, which makes the gate a test of the correction as well as of the leading term.

### §2.3 What these two failures do and do not cost

They cost **CFG-B its certification and therefore every RHO-B bin**. They cost **nothing** in the derivation: `G-CF` measures the RHO-B closed form against its own quadrature at exactly `0`, `G-SUM` measures split-independence at `9.62997e-14`, and both failing gates' own data confirm the log law more sharply than a pass would have. **This is a bookkeeping failure inside a correct calculation, and it is reported as a failure anyway.**

---

## §3 — WHAT THE INSTRUMENT MEASURED (theorems restated as derivations; measurements marked)

**Frozen:** `the derived statements of section 2 and the hand-evaluated turning-point verdict are available before the run and may NOT be presented in the result doc as discoveries of the instrument; only the quantities enumerated in the third bullet of section 7.7 may be presented as measurements`. **Honoured throughout this section.**

### §3.1 The derivations, restated (NOT presented as measurements)

```
v(r) = c_0 S^p ,  S = sqrt(1 - A^2) ,  A = r_sat/r        p = 1/2 (RHO-A), 2 (RHO-B)
J(p) = 1 - sqrt(pi) Gamma(1 - p/2)/Gamma((1-p)/2)          both branches, ONE closed form
   -> finite at p = 1/2 ;  Gamma POLE at p = 2             the divergence IS a Gamma pole
Delta_T_1way^B = (r_sat/c_0) [ artanh(A_in) - artanh(A_out) ]     EXACT, elementary
Delta_T_return^B = (r_sat/c_0) ln( 2 r_sat / (theta l_node) )     the regulated law
omega(k) = omega_link arccos(cos k l) = c_link k                  EXACTLY linear
   -> v_group == v_phase identically up to the zone edge
S_turn/S_last = sqrt( Omega / (2 theta beta) )                    MASS-FREE
```

**`G-JA` reports the Gamma pole as a first-class receipt:** evaluating `Γ(1 − p/2)` at `p = 2` raises *"gamma function pole"*, which is the two-method statement that RHO-A's finiteness and RHO-B's divergence are one formula at two exponents.

**★ `G-DISP` is the substrate-native checkpoint that changed the answer.** `srs-band-structure.md` §2 adjudicates the **arccos transmission-line** map as substrate-native and shows the graph-Laplacian map FAILS the canonical `1/√3` velocity gate. On the `z = 2` radial cascade the arccos map is **exactly linear** (`3.7711e-50`), so the group and phase velocities coincide and **no group-velocity correction to the delay exists**. Had this lane defaulted to the tight-binding map it would have manufactured a band-edge group-velocity collapse that the substrate-native model does not have. **The rejected model is swept anyway, as variant `D2`.**

### §3.2 The barrier maximum — MEASURED (`G-PEAK`)

| branch | `A_peak` | `r_peak/r_sat` | `r_peak` in `GM/c²` | `𝒱_peak` | `𝒱″ < 0` |
|---|---|---|---|---|---|
| RHO-A | `0.72197046380103953` | `1.3850982140393763` | `9.6956874982756338` | `2.0396581806300946` | holds |
| RHO-B | `0.57201415970765805` | `1.7482084718166324` | `12.237459302716427` | `0.89840424332827051` | holds |

**Both peaks lie OUTSIDE `r_sat = 7 GM/c²`, and both are ω-independent.** This is the `PLANE-PEAK` reference plane, derived from the branch's own profile.

### §3.3 The turning point — the full sweep, and the margins

**Frozen reporting requirement:** `the BIN-DB verdict must be reported together with the measured ratio S_turn/S_last at every sweep point, because a verdict that holds by a factor of two is reported as holding by a factor of two and not as a clean separation`. **Honoured:**

| `β` (band top, `ω_C`) | `θ` | `S_turn/S_last` (RHO-B) | governed by |
|---|---|---|---|
| `5.4414` | `1` | `0.41270920385256384` | NODE |
| `5.4414` | `0.5` | `0.58365895340449818` | NODE |
| `17.0111` | `1` | `0.2334174292085989` | NODE |
| `17.0111` | `0.5` | `0.33010209408106238` | NODE |

**Identical at every mass on the grid, because the ratio contains no mass.** Under RHO-A the same ratio is ~`25` orders of magnitude smaller (`S_turn = 1.61873e-34` against `S_last = 8.6427e-9` at `1 M_⊙`) and the question is moot.

**★ The margin is honest and it is thin.** The node wins by a factor between `2.3` and `4.3` in `S`, i.e. by a factor between `5.87` and `18.4` in frequency headroom at the innermost cell. **This is why prereg §0.2 put the tunnelling question to Grant: a few-cell evanescent skin is exactly the regime where "does it tunnel to the end or reflect off cutoff" is a real question, and this lane computes no tunnelling amplitude (§1.3 Y8).**

---

## §4 — THE PHYSICS NUMBERS

### §4.1 `CFG-A` — RHO-A, `DELAY-CERTIFIED`, `BIN-DA-CLOSED` **ADJUDICATED**

`ΔT_return^A = 2𝒥_A (r_sat/c₀)`, `𝒥_A = 1 − √π Γ(3/4)/Γ(1/4)`.

| quantity | value |
|---|---|
| `𝒥_A` (closed form) | `0.4009298826322039` |
| `2𝒥_A` — the dimensionless delay | `0.80185976526440779` |
| measured `c₀ΔT/r_sat` at `62 M_⊙` | `0.80185976526437822` |
| relative separation from the closed form | `3.68818e-14` |
| regulator spread over all six variants | `7.5252419456313015e-14` |

| `M/M_⊙` | `ΔT_return^A` (PLANE-∞ excess) |
|---|---|
| `1` | `2.7655076269418782e-5` s |
| `10` | `0.0002765507626943731` s |
| `62` | `0.0017146147287052984` s |
| `100` | `0.0027655076269440605` s |

**PLANE-PEAK secondary at `62 M_⊙`:** total round trip `0.0024768687743196497` s = `1.1583368442579069 (r_sat/c₀)`.

**Frozen reporting requirement, honoured:** `BIN-DA-CLOSED means the RHO-A return is PROMPT, ACHROMATIC and REGULATOR-FREE, with the delay a fixed pure multiple of r_sat/c_0; the result doc must report that multiple, its SI-second value on the mass grid, and the explicit statement that the 2026-06-17 predecessor's 3-10 ms BAND is the free-flight term of an undeclared plane and NOT an uncertainty in the substrate prediction`. **The multiple is `2𝒥_A`; the SI values are tabled above; and the predecessor's band is the free-flight term of an undeclared plane, exactly as the frozen text requires this document to state.**

### §4.2 `CFG-B` — RHO-B, `DELAY-NOT-CERTIFIED`. **Everything below is a NOT-ADJUDICATED DIAGNOSTIC.**

| `M/M_⊙` | `ΔT_return^B` (PLANE-∞ excess) | `c₀ΔT/r_sat` | `ln(2r_sat/ℓ_node)` | `K_disc` (round trip) |
|---|---|---|---|---|
| `1` | `0.0013483900743650673` s | `39.096610617920122` | `38.519394953018544` | `0.57721566490157852` |
| `10` | `0.014278031701731996` s | `41.399195710914165` | `40.821980046012589` | `0.57721566490157584` |
| `62` | `0.092425225734391322` s | `43.223745002965211` | `42.646529338063635` | `0.57721566490157572` |
| `100` | `0.1507216265981332` s | `43.701780803908211` | `43.124565139006635` | `0.57721566490157602` |

**The round-trip discrete correction is `γ` to twelve significant digits at every mass** — the durable content of the `G-DISC` failure. **PLANE-PEAK secondary at `62 M_⊙`:** `0.091608777584212407` s = `42.841923412906116 (r_sat/c₀)`.

### §4.3 The regulator sweep — `BIN-CUTOFF`, NOT ADJUDICATED for CFG-B

| variant | `CFG-B` value (s, at `62 M_⊙`) |
|---|---|
| `R1` full node | `0.092425225734391322` |
| `R2` half node | `0.095389535496352708` |
| `R3` turning point, `β = 5.4414` | `0.092425225734391322` |
| `R3` turning point, `β = 17.0111` | `0.092425225734391322` |
| `R4` strained pitch | `0.0902869282377711` |
| `R5` continuum (no discrete sum) | `0.091190966923122306` |
| `D2` REJECTED lumped dispersion | `0.092747786022786503` |

| configuration | spread | token | adjudicated? |
|---|---|---|---|
| `CFG-A` | `7.5252419456313015e-14` | `BIN-CUTOFF-ROBUST` | **YES** |
| `CFG-B` | `0.055207950189327304` | `BIN-CUTOFF-ROBUST` | **NO — CFG-B is `DELAY-NOT-CERTIFIED`** |
| `CFG-SYN` (`p = 3`) | `2.9604330615961116` | (self-test vehicle; **no bin**) | — |

**★ The `R3` rows are the numerical statement of the turning-point verdict:** the band-edge cutoff lies **inside** the last node at both bracket ends, so `R3` collapses onto `R1` **exactly**, to all digits. **★ And `CFG-SYN` is the demonstration that the bin can fire:** the same sweep on a power-law-divergent profile spreads by `2.9604330615961116`, a factor of `54` above the frozen `0.10` threshold.

### §4.4 `BIN-EVAN` — CLEAR on both branches, at both bracket ends

| configuration | `ω_max/ω` at the innermost node | at the outermost radius | token | adjudicated? |
|---|---|---|---|---|
| `CFG-A`, `β = 5.4414` | `161447368613374.71` | `4.8730858679865402e+18` | `BIN-EVAN-CLEAR` | **YES** |
| `CFG-A`, `β = 17.0111` | `504722558940526.05` | `1.5234415960764846e+19` | `BIN-EVAN-CLEAR` | **YES** |
| `CFG-B`, `β = 5.4414` | `5.8709947439811122` | `4.8730858679828854e+18` | `BIN-EVAN-CLEAR` | **NO** |
| `CFG-B`, `β = 17.0111` | `18.354114509011853` | `1.5234415960753421e+19` | `BIN-EVAN-CLEAR` | **NO** |

**The RHO-B innermost margins are exactly `(S_last/S_turn)²`** — `1/0.41270920385256384² = 5.87` and `1/0.2334174292085989² = 18.4` — an internal consistency check between two independently computed quantities.

### §4.5 `BIN-DISC` — the token is `BIN-DISC` and it is **NOT ADJUDICATED** (it needs CFG-B)

| `M/M_⊙` | `T_B/T_A` | `\|T_B − T_A\|` (s) | `τ_ring` (s) | `\|ΔT\|/τ_ring` |
|---|---|---|---|---|
| `1` | `48.757416585255579` | `0.0013207349980956485` | `3.4240195625884296e-5` | `38.572647555121522` |
| `10` | `51.62897242670489` | `0.014001480939037623` | `0.00034240195625884296` | `40.891942008803921` |
| `62` | `53.904369411419553` | `0.090710611005686024` | `0.0021228921288048263` | `42.729731659401589` |
| `100` | `54.500528268180376` | `0.14795611897118914` | `0.0034240195625884296` | `43.211236462486767` |

`τ_ring = (GM/c³)/(ω_I M_g)` with `ω_I M_g = 0.14389382616333127` read programmatically from the v2.4 shipped JSON. **The separation exceeds one substrate-native ringdown damping time by a factor of `38.6` to `43.2` at every mass, and the branch ratio grows slowly with mass because the log's argument does.** `BIN-DEGEN` did **not** fire.

**But the token is not adjudicated.** `BIN-DISC` requires both configurations and CFG-B is `DELAY-NOT-CERTIFIED`. **The honest statement is: the two branches' timing signatures LOOK cleanly separated by a factor of ~50, on an instrument whose RHO-B half did not certify. A successor that repairs the two freeze-time constants inherits a measurement rather than a silence.**

### §4.6 §7.5b — the observational-pointer DIAGNOSTIC

**Frozen:** `the observational-pointer ratio is a DIAGNOSTIC and not a bin; no sub-bin, no threshold and no adjudication of any kind attaches to it; a smaller ratio on one branch is NOT evidence for that branch, is NOT a detection, is NOT a validation, and the result doc must carry the sentence that the ~0.29 s spacing is a CONTESTED RETROSPECTIVE re-analysis of somebody else's data, is not an exp- node, and cannot strengthen any AVE claim; the FLAG-ECO degeneracy applies to this diagnostic in full, since any log-form model can be brought to any delay by moving its cutoff length`.

| branch | pointer / `T` (PLANE-∞) | pointer / `T` (PLANE-PEAK) |
|---|---|---|
| RHO-A | `169.13420557105463` | `117.08331220722732` |
| RHO-B | `3.1376715360522114` | `3.1656355171142221` |

**The ~`0.29` s Abedi–Dykaar–Afshordi spacing is a CONTESTED RETROSPECTIVE re-analysis of somebody else's data, is not an `exp-` node, and cannot strengthen any AVE claim.** Both branches MISS it. **The FLAG-ECO degeneracy applies in full: any log-form model can be brought to any delay by moving its cutoff length, so "RHO-B misses by 3× where RHO-A misses by 169×" is NOT evidence for RHO-B and this document does not present it as any.** It is recorded because the collision was foreseeable at freeze and was frozen there so it could not be constructed post-hoc.

---

## §5 — DISCRIMINATION NOTE: what this result does and does NOT mean

**Written under `consistency-vs-emergence` and `ave-discrimination-check`, to the standard the prereg fixed in advance rather than the standard the result invites.**

### §5.1 What is genuinely established

1. **The RHO-A delay is a parameter-free pure multiple of `r_sat/c₀`, and the predecessor's `3–10 ms` band was a plane artefact.** `BIN-DA-CLOSED`, adjudicated, on a `DELAY-CERTIFIED` configuration whose negative control reproduces the predecessor at `7.1262679104721422e-13`. **FORM-class**; the SI-second value is VALUE-CONSISTENCY class.
2. **The turning point is node-governed and the delay is achromatic — a CONFIRMED DERIVATION, disclosed at freeze.** The mass-independence of `S_turn/S_last` is the substantive structural content.
3. **Group and phase velocity coincide under the adjudicated substrate-native band model**, so the delay has no dispersive correction. **The model adjudication is load-bearing** (`FT-DISP`).
4. **A parameter-free outer reference plane exists outside `r_sat` on both branches**, derived from the profile rather than imported.
5. **The `γ` round-trip discrete correction is exact to twelve digits**, and the general law `K_disc(θ) = [ln θ − ψ(θ)]/2` is derived here.

### §5.2 What is NOT established, without hedging

1. **No RHO-B bin is adjudicated.** `CFG-B` is `DELAY-NOT-CERTIFIED`. `BIN-DB`, `BIN-DISC`, and CFG-B's `BIN-CUTOFF` and `BIN-EVAN` are `N/A` and §4.2–§4.6 are diagnostics.
2. **Nothing about which inertia grading canon means.** Frozen: `this lane computes the delay under both branches; it does not prefer RHO-A over RHO-B or RHO-B over RHO-A, and a cleaner number on one branch is not evidence for that branch`. **The fork is exactly as open as it was.**
3. **Nothing about whether an echo TRAIN exists.** Frozen: `an echo train requires an OUTER partial reflector with a computed reflectivity; this lane computes a barrier LOCATION but no reflectivity, no transmission coefficient and no amplitude of any kind`. **A location is not a mirror.**
4. **Nothing observational.** No dataset was analysed. The `0.29` s number is a cited in-repo pointer used as a comparison scale.
5. **Nothing that discriminates AVE from ECO models by the FORM of the delay.** `FLAG-ECO` applies in full.
6. **No tunnelling calculation.** The evanescent skin is a few cells thick and this lane computes no amplitude through it — which is exactly why the §0.2 plumber question is owed.
7. **Nothing about the 3D srs correction** to the 1D radial cascade, nothing about whether the lattice pitch is itself strained (`R4` sweeps it, nothing settles it), and nothing about the single-scale-vs-stiffness-lifted band-top ruling (`β` is swept).
8. **Nothing Cosserat, nothing polar, nothing about spin, and no eigenvalue of any kind.**

### §5.3 The honest classification

**This is a DERIVATION result with a certified negative control, one certified branch carrying one adjudicated bin, one uncertified branch carrying fully-diagnosed numbers, a confirmed turning-point derivation, and two freeze-time algebra errors that cost the RHO-B half its certification and were caught by the lane's own gates.** The thing in it that could ever become an AVE-distinct forward prediction — a `~50×` split in echo timing between the two inertia gradings, at a fixed parameter-free cutoff length — is **structurally degenerate with the ECO echo family** and is **not certified here**. **This document is not a chord and does not present itself as one.**

---

## §6 — FLAG-DON'T-FIX: what is routed, and to whom

1. **★ `FLAG-ECO`** — mandatory in the headline by freeze, and it is there. Routed to the discrimination lane, unresolved.
2. **★ `FLAG-PLANE-GAP`** — [`research/2026-06-17_bh-shear-echo-forward-prereg.md:65`](2026-06-17_bh-shear-echo-forward-prereg.md) states verbatim *"there is no parameter-free outer reflector *outside* `r_sat`"*, surveying only the imported GR photon sphere and the corpus ringdown-cavity dimension. **§3.2 derives one from the profile itself, on both branches.** Surfaced with the line and the verbatim quote; **that frozen document is not edited and no edit is proposed.**
3. **★ `FLAG-ECO-COROLLARY` — the corpus's own discriminator sentence is RHO-A-conditional.** [`research/2026-06-17_bh-shear-echo-forward-prereg.md:73`](2026-06-17_bh-shear-echo-forward-prereg.md) reads *"**AVE has no such knob:** its reflector is at the *fixed, parameter-free* radius `r_sat = 7GM/c²`, **outside** `r_s`, with no log-divergence"*, and the KB banner at [`existing-experimental-signatures.md:42`](../manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/existing-experimental-signatures.md) repeats it. **Under RHO-B the AVE delay IS log-divergent in the continuum and log-enhanced on the lattice.** Both lines verified two-method at freeze and again at result. **Neither is repaired. Neither branch is preferred.** Routed to Grant and the auditor lane.
4. **★ `FLAG-CITE-SHIFT`** — [`srs-band-structure.md:145`](../manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/srs-band-structure.md) cites `constants.py:294` for `OMEGA_C`; at `origin/main` `2877eaa0` that symbol is defined at [`constants.py:305`](../src/ave/core/constants.py). Pure line-shift class, correct-when-written presumed. **NOT repaired** (KB edits are outside this lane's scope fence). Routed to the auditor lane.
5. **`FLAG-PITCH`** — whether the lattice pitch inherits `ε₁₁`. Swept as `R4`; **the constitutive question is left open** and the sweep shows it moves the RHO-B delay by about `2 %`.
6. **`FLAG-BRACKET`** — the vector band top is a bracket pending Grant. Swept, not resolved; the verdict is unchanged at both ends.
7. **`FLAG-CAUSAL` carried forward from the axial lane, NOT re-asked and NOT answered.** This lane makes the electrical length finite and calculable — about `43` radians of `ln` at the reference mass — but whether that termination is a port or a mirror is still Grant's.
8. **★ `FLAG-FREEZE-SIZING` — a lane-pattern worth the orchestrator's attention.** This is the **second consecutive lane** in this arc to land NOT-CERTIFIED on freeze-time sizing/derivation errors rather than on physics (the axial RHO-B lane logged four on 2026-08-04; this lane logs two). **Both times the gates worked exactly as designed and the physics survived.** Whether the freeze-time derivation of gate constants needs its own check step is a process question this lane raises and does not answer.

---

## §7 — VALIDATION AND SCOPE DISCLOSURES

- **Determinism.** Two full runs, digest `a788ac6080af4073` twice, shipped objects byte-identical apart from `_runtime_sec`. The driver emits **no** pass field for determinism; it ships the digest only, and the verdict is the external two-run diff recorded here. Runtimes are written **without back-ticks and are NOT registered**: `_runtime_sec` is machine-dependent and registering it would fail the gating number check on any honest re-run elsewhere (the #801 R3 lesson).
- **Numerical discipline, load-bearing.** At the innermost node `ℓ_node/r_sat = 6.0238983090250982e-19`, so any float64 evaluation of `1 − A²` by subtraction returns exactly zero. Every near-wall quantity is computed from `S² = x(2r_sat + x)/(r_sat + x)²` and every `S^{-p} − 1` from `expm1(−p/2 · log S²)`. **Without this the entire calculation returns silent nonsense rather than an error.**
- **The gating number check** implements the six accumulated checker lessons plus this lane's seventh, a **mutation receipt** (`--mutation-receipt`) demonstrating the checker itself can FAIL.
- **Engine fence.** `src/ave` byte-untouched; `ave.core.constants` imported read-only.
- **Predecessor fence.** `src/scripts/vol_3_macroscopic/bh_shear_echo_delay.py` and `research/drivers/coldq_pole_v2p4_root_results.json` are **imported read-only**, neither edited nor re-scored. Discharged by an empty `git diff --stat` against the freeze base.
- **Scope fence.** `research/` only; no manuscript or KB file edited; PR #876's branch untouched.
- **Canonical inputs, for the record:** `ℓ_node = 3.8615926772428334e-13` m, `ω_C = 7.76344071105011e+20` rad/s, `r_sat(62 M_⊙) = 641045.46244702291` m, `r_sat/c₀ = 0.0021382974966202216` s, `Ω_v24 = 1.8536552108408788`, `ω_ringdown = 866.88368375810832` rad/s.
- **Scope, unchanged:** `ℓ = 2` is an input; `ν_vac`, `K = 2G` and the `7` in `r_sat` are GR-imported and untouched; `ℓ_node` is definitional (rides `m_e`); spin is out of scope; no Cosserat channel, no polar branch, no eigenvalue, no reflectivity, no completeness statement of any kind.

---

## §8 — ROUTED FOLLOW-ONS (named, not started)

1. **A successor lane with the two constants repaired** — `K_disc(θ) = [ln θ − ψ(θ)]/2` and a `G-DECADE` gated against the derived `S²/4` residual — which would certify CFG-B and let `BIN-DB`, `BIN-DISC` and CFG-B's `BIN-CUTOFF` be adjudicated rather than inherited as diagnostics.
2. **The tunnelling amplitude through the few-cell evanescent skin** (§0.2's plumber question), which is what decides whether the thin node-vs-band margin is physically decisive.
3. **A reflectivity at the derived barrier**, without which no echo TRAIN can be claimed on either branch.
4. **The auditor-lane relabel of `FLAG-ECO-COROLLARY`** — the corpus's no-log-divergence discriminator needs an RHO-A conditionality qualifier that only a ruling can authorize.

---

> **Result provenance.** Resolves the frozen gates and bins of `research/2026-08-04_echo-delay-regulated-sum_prereg-FROZEN.md` (commit `1da06a90`, COMMIT 1 of this lane, pushed **ALONE** before any driver code existed and before any number produced by this instrument existed). All numbers above are read from the shipped `research/drivers/echo_delay_regulated_sum_results.json` and are machine-verified against it by `research/drivers/echo_delay_regulated_sum_number_check.py`, wired into `make verify`. **Mints no `clm-`/`def-`; propagates to no leaf; engine byte-untouched; falsification ledger untouched.** Companion: the docket fragment `_orchestration/docket-entries/2026-08-04-echo-delay-regulated-sum.md`.

---

## §9 — ★ SVA PILOT CASE 2: the per-row fill experience (input to the canonization decision, not a vote)

`manuscript/ave-kb/common/standard-vacuum-analysis.md` §3 asks each pilot to score every row **FILLED / FILLABLE-BUT-MISSING / NOT-APPLICABLE** and to log gaps. This lane filled the §0 header **before** §2's derivation existed. Scored honestly, including where the row did nothing:

| row | score | what filling it actually did |
|---|---|---|
| **1 · Sector / ownership** | **FILLED** | **Low value HERE, and that is worth recording.** A transit-time problem has one obvious owner and the cross-wiring risk was near zero. The row cost a paragraph and caught nothing. It is not evidence against the row — it is evidence that row 1 is cheap insurance, not a universal discovery engine. |
| **2 · Regime / phase-state** | **FILLED** | Moderate. Forced the explicit statement that `r < r_sat` is out of the domain, **which is the whole reason the node sum terminates**. The regulator is a REGIME statement and the row is where that surfaced. |
| **3 · Circuit statement** | **FILLED** | **HIGH VALUE — this row changed the calculation.** Stating the object as *"a lossless LC ladder whose per-section delay grows without bound, cut at the last physical section"* before any relativity word is what made "does a ladder section still pass my frequency?" an obvious question. **The band-edge turning point (§2.7, the whole ★ half of the brief) came out of row 3, not out of the physics literature.** |
| **4 · Plane & projection** | **FILLED** | **HIGHEST VALUE — this row produced a result.** Forced by wall-taxonomy §9, the plane declaration exposed that the predecessor's `3–10 ms` **band was a plane artefact**, produced the plane-INVARIANT excess-delay definition, and then forced the search for a legitimate outer plane, which produced the derived barrier maximum of §3.2. **Three deliverables from one row.** |
| **5 · Constitutive provenance** | **FILLED** | High. Tagging `ℓ_node` as **IMPORTED-VALUE / DEFINITIONAL** rather than derived is what keeps §0.3's honest classification honest — the log's argument rides `m_e`, and without row 5 "parameter-free" would have been written without its qualifier. |
| **6 · Energy ledger** | **FILLED** | Moderate, and **preventive**. It licensed the flat refusal to use "absorption" or "damping" about the wall anywhere in this lane, which is exactly the vocabulary a horizon-analogue invites. |
| **7 · Calibratability** | **FILLED** | Moderate. Confirmed the primary output is a dimensionless ratio and that the log's argument is a ratio of two lengths — i.e. self-calibratable — which is what makes the RHO-B law reportable at all. |
| **8 · Discrimination class** | **FILLED** | **HIGH VALUE, and it cost the lane its best-looking number.** Running the SM/GR counterfactual **at freeze** is what produced `FLAG-ECO` before any number existed. Without row 8 the ECO degeneracy would have been discovered at result time, next to a `3.14` ratio, and would have been much harder to state cleanly. **The row converted a potential overclaim into a frozen headline requirement.** |
| **9 · Certification plan** | **FILLED** | High — and it is the row that failed the lane, correctly. Two gates caught two freeze-time algebra errors. |
| **10 · Adjudication routing** | **FILLED** | Moderate. Naming in advance what propagates on each outcome made the "CFG-B adjudicates no bin" consequence mechanical rather than a judgement call at result time. |

**Gaps and friction, reported because the pilot asks for them:**

1. **★ The header has no row for NUMERICAL CONDITIONING, and this lane needed one.** The single largest failure mode here was not physical: at `ℓ_node/r_sat = 6.0238983090250982e-19`, a float64 `1 − A²` returns **exactly zero** and the whole calculation silently produces nonsense with no error. Nothing in the ten rows prompts that check. **Candidate row 11, or a row-9 sub-clause: "name the cancellation, the dynamic range, and the working precision before writing the first expression."** Offered as pilot feedback, not proposed as a change.
2. **Row 5 has no slot for a BRACKET.** The vector band top is `[5.4414, 17.0111] ω_C` pending a ruling — neither DERIVED nor IMPORTED nor FORKED-with-an-id nor ENG-CHOICE. This lane wrote it as "DERIVED-FORM, BRACKET OPEN" and swept both ends. **Suggest `BRACKETED(pending-ruling)` as a fifth provenance tag.**
3. **Rows 3 and 4 did the heavy lifting; row 1 did almost none.** On this problem class the ordering could be inverted with no loss. Recorded as a data point about row *utility variance*, not as an argument to drop any row.
4. **The header is cheap.** Filling all ten rows took well under an hour and preceded the derivation, as the fire-point intends. **No row was un-fillable.**

**Pilot verdict from this lane, and it is only one data point:** rows 3, 4 and 8 each changed what this lane computed or how it reported it, before any number existed. That is the fire-point working as designed. **The canonization decision is Grant's and this log is input to it, not a vote.**
