# The cold-Q AXIAL family under RHO-B — RESULT: `ROOT-NOT-CERTIFIED` on three self-tests this lane sized wrong at freeze. The **wall** is certified; the pole is located, gated and **NOT adjudicated**

**Date:** 2026-08-04
**Prereg-file**: research/2026-08-04_coldq-axial-rhob_prereg-FROZEN.md
**Prereg-commit:** `e3a4181d` (frozen and pushed **ALONE**, before any driver code and before any number produced by this instrument existed)
**Driver:** [`research/drivers/coldq_axial_rhob.py`](drivers/coldq_axial_rhob.py) → [`research/drivers/coldq_axial_rhob_results.json`](drivers/coldq_axial_rhob_results.json)
**Number check:** [`research/drivers/coldq_axial_rhob_number_check.py`](drivers/coldq_axial_rhob_number_check.py) — gating via `make verify`
**Class:** DERIVATION result (research-doc; **mints no `clm-`/`def-`; propagates to no KB/manuscript leaf; changes no solidity; edits no falsification ledger**). Engine `src/ave` byte-untouched.
**Provenance:** Grant's ruling of 2026-08-04 — the fork v2.4 fenced at `X6` is owed an **AXIAL** run before the `BIN-1`/`BIN-2` misses are read as profile falsification. Written against `origin/main` = `10213df3`.

---

## REGIME HEADER (mandatory, restated at the point of reading)

**MODE** — DC operating-point eigenproblem, **shear channel**. **REGIME** — sub-yield lossless-reactive; the wall is the `S → 0` level set under the RHO-B profile. **PHASE-STATE** — cold lattice, Op14 ON as a static constitutive grade. **A null in which the mode CANNOT exist under the frozen construction is an ARTIFACT-class finding, not a falsification**, and every null below is classified.

---

## HEADLINE

> **Certification: `ROOT-NOT-CERTIFIED` on every configuration that has a root.** Not one gate failed on the RHO-B primary. **Three self-tests failed to FIRE** — `FT-2`, `FT-2c` and `FT-W` — each because **this lane sized its firing threshold wrong at freeze**, and the frozen rule is unambiguous: *a gate that cannot fail is not a gate*. **The thresholds are NOT retuned. No physics bin is adjudicated.** The three sizing errors are diagnosed exactly and routed with their repairs named (§7).
>
> **★ THE NEGATIVE CONTROL PASSES, AND IT PASSES EXACTLY.** This lane's RHO-A operator is **entry-by-entry identical** to v2.4's certified one — `G-NC(a)` measures a maximum absolute difference of exactly zero over all three pencil blocks — and its polished root reproduces v2.4's certified root to `2.139211445202149e-40`. Four of v2.4's own published gate values come back **to all digits**: `G1` `4.726832751705419e-50`, `G3` `3.332294747541498e-14`, `G4(a)` `5.277782707837865e-47`, `G10(b)` `9.273121713408482e-47`. **Any RHO-B number below is produced by an instrument that provably reproduces the certified RHO-A one.**
>
> **★ THE WALL IS THE RESULT, AND IT IS CERTIFIED.** Under RHO-B the saturation wall is **not** the RHO-A short. Every one of the derived wall gates passes: the indicial identity `σ(σ-1) + Ω² = 0` holds **exactly** (`G-IND` measures `0.0`); the derived Frobenius row's bracket vanishes **linearly**, ratio `1.0000000003434282e-10` against a first-order zero's exact `1e-10`; and all four `G-W` limbs hold at the located root. **`FT-SHORT` FIRES at `0.2739562093388408`** — imposing the RHO-A traction-free row on the RHO-B operator moves the root by 27 per cent. **The wall row is load-bearing, not cosmetic.**
>
> **★ AND THE PHYSICAL CONTENT IS A CHANGE OF KIND.** `Z_shear = sqrt(μρ) = ρ c_shear = 1/S → ∞` where RHO-A gives `sqrt(S) → 0`; the travel-time integral `∫dr/c_shear` diverges logarithmically, so **the wall sits at INFINITE optical distance and a wave launched inward never arrives**; `η = 0` is a **regular singular point** where under RHO-A it is an **ordinary** point. **RHO-B converts the AVE saturation wall from a reflector at finite distance into a horizon-analogue.**
>
> **★ TWO NULLS, ONE MECHANISM, AND THEY ARE THE INFORMATIVE HALF.** The finite-energy branch (`ROW-BOUND`) has **no** `n`-stable physical-quadrant root under either instrument — `BIN-B-N` on both `CFG-BOUND-POLY` and `CFG-BOUND-FROB`. The **ingoing** branch (`ROW-IN`) has two. That asymmetry is the derived one: `ROW-BOUND` retains `η^{σ₊}`, which is the wave **emerging from** the wall — an acausal condition for a ringdown — while `ROW-IN` is the causal, Ax-3-licensed mirror of the port at infinity.
>
> **★ THE POLE, REPORTED AS A NOT-ADJUDICATED DIAGNOSTIC.** `1.021058710655384226893259908522031969379` and `-0.3138716383801338012812670641580672390478`, `n`-stable between `n = 48` and `n = 80` to `3.665073726334936e-13`. That gives `ω_R M_g = 0.1458655300936263` and `Q = 1.6265545939814532`. Against the frozen comparators the direction is **`BIN-B-P3-RESCUE-PARTIAL`**: `|D_Q|` **improves** from `0.561877761595111` to `0.2255289604164633`, while `|D_omega|` **worsens** from `0.2913322255921462` to `0.6096407790466821`. **`BIN-B-P3-RESCUE-DECISIVE` does NOT fire.** These numbers are diagnostics, not verdicts, because the frozen precedence put this configuration in `BIN-B-S`.

---

## §1 — THE GATE TABLES (measured against frozen; nothing dropped, widened or re-defined)

**Frozen:** `no gate, tolerance, band, frozen numeric parameter, bin boundary or method element in sections 4, 5, 6 and 7 may be changed after any gate result is seen; if a configuration fails certification this lane reports ROOT-NOT-CERTIFIED for that configuration, adjudicates NO physics bin for it, and routes to a successor with a new version number`.

**No frozen criterion was dropped, widened, or re-defined.**

### §1.1 The gates that apply to every configuration

| gate | what it certifies | frozen tol | measured | verdict |
|---|---|---|---|---|
| **G-NC(a)** ★ | **NEGATIVE CONTROL, operator level** — this lane's RHO-A mp operator entry-by-entry against v2.4's `graded_matrices_mp`, imported read-only | `1e-40` | exactly `0` over all three blocks | **PASS** |
| **G-NC(b)** ★ | **NEGATIVE CONTROL, root level** — against v2.4's shipped certified mp root | `1e-30` | `2.139211445202149e-40` | **PASS** |
| **G0** | `𝓛_η ≡ 4η²·𝓛_A` for **both** inertia readings through one closed form | `1e-13` | `9.960790154561388e-14` | **PASS** |
| **G-AGREE** | two-instrument agreement on the `ROW-BOUND` pair | `1e-3` | **N/A BY OUTCOME** — `BIN-B-N` fired on both members | — |

### §1.2 `CFG-A-CONTROL` — the negative control (RHO-A, v2.4's wall row)

| gate | frozen tol | measured | verdict | v2.4's published value |
|---|---|---|---|---|
| **G1** | `1e-20` | `4.726832751705419e-50` | **PASS** | identical to all digits |
| **G2** ★ | `1e-10` | `1.2496816388248957e-10` | **FAIL** | identical to all digits (v2.2's `n = 32` number) |
| **G2c** | `c` >= `1.0`, resid <= `0.60` | `5.918368041595941` / `0.12473145492156945` | **PASS** | — |
| **G3** | `1e-10` | `3.332294747541498e-14` | **PASS** | identical to all digits |
| **G4(a)/(b)** | `1e-25` / `1e-6` | `5.277782707837865e-47` / `1.4856751378261543e-09` | **PASS** | (a) identical to all digits |
| **G5** | count `== 1` | `[1, 1, 1, 1]` | **PASS** | — |
| **G8** | `1e-9` | `9.132344757601747e-47` | **PASS** | — |
| **G10(a)/(b)** | `1e-40` / `1e-20` | exactly `0` / `9.273121713408482e-47` | **PASS** | (b) identical to all digits |

> **★ G2's FAILURE IS THIS LANE'S OWN FREEZE ERROR, AND IT IS ALSO AN INDEPENDENT CORROBORATION OF v2.4.** This lane froze its certification ladder as `n ∈ {32, 48, 64}` against `n = 80`. **v2.4 excluded `n = 32` from its own certification ladder**, on a root-exponential-law argument whose out-of-sample prediction said that rung could not pass `1e-10`. This lane did not carry that exclusion. The measured `n = 32` separation is `1.2496816388248957e-10` — **the exact value v2.2 published and v2.4 reproduced**, at a different reference rung and in a different lane. **Read plainly: the control fails a gate this lane sized wrong, and in failing it it re-measures v2.4's `n = 32` finding to all digits.** The tolerance is not moved and the rung is not dropped.

### §1.3 `CFG-IN-FROB` — the ingoing branch (RHO-B, Frobenius `σ₋`) — **every gate PASSES**

| gate | frozen tol | measured | verdict |
|---|---|---|---|
| **G-IND** ★ | `1e-30` | exactly `0` | **PASS** |
| **G-FROB** ★ | ratio `≤ 1e-9` | `1.0000000003434282e-10` | **PASS** |
| **G-W** ★ | four boolean limbs | all four hold (§2) | **PASS** |
| **G1** | `1e-20` | `1.6503104687572565e-50` | **PASS** |
| **G2** | `1e-3` (algebraic class) | `3.6140893550967903e-10` | **PASS** |
| **G2c** | `p` >= `1.0`, resid <= `0.60` | `18.695313410394075` / `0.48520667756680425` | **PASS** |
| **G3** | `1e-3` | `5.057619054190125e-14` | **PASS** |
| **G4(a)** | `1e-25` | `4.740753178069656e-49` | **PASS** |
| **G8** | `1e-9` | `5.629708455436147e-49` | **PASS** |
| **G10(a)/(b)** | `1e-40` / `1e-20` | exactly `0` / exactly `0` | **PASS** |

**★ The measured convergence is far better than the class this lane frozen-gated it in.** `G2`'s frozen tolerance for `CFG-IN-FROB` is the **algebraic** `1e-3`, derived in advance from §2.6's disclosure that `ROW-IN`'s rejected branch is *approximable rather than excluded*. The instrument measures `3.6140893550967903e-10` at `n = 32` and `7.840463472871456e-16` at `n = 64` — a fitted power-law exponent of `18.695313410394075`, which is spectral behaviour, not algebraic. **The pre-registered pessimism was wrong in the safe direction, it is reported as wrong, and the tolerance it produced is not tightened after the fact.**

### §1.4 The scope split — RUN, N/A, and UNRUN

| configuration | gates RUN | N/A **by construction, disclosed in the prereg** | N/A **by outcome** | **UNRUN by omission** |
|---|---|---|---|---|
| `CFG-A-CONTROL` | G-NC, G0, G1, G2, G2c, G3, G4, G5, G8, G10 | — | — | **none** |
| `CFG-BOUND-POLY` | G0 | — | all root-local gates (`BIN-B-N`) | **none** |
| `CFG-BOUND-FROB` | G0 | — | all root-local gates (`BIN-B-N`) | **none** |
| `CFG-IN-FROB` | G0, G-IND, G-FROB, G-W, G1, G2, G2c, G3, G4(a), G8, G10 | `G5`, `G4(b)` — prereg §4.1: the Frobenius operator admits no companion linearization, so **no isolation claim of any kind is made** | `G-AGREE` | **none** |

**Frozen:** `a gate that was never run cannot be counted as passed`. **No gate in this lane is UNRUN by omission.** Two are `N/A BY CONSTRUCTION` and were declared so **before** the run; one is `N/A BY OUTCOME` and the prereg had already frozen that `ROW-IN` carries **no** agreement gate at all.

### §1.5 The self-tests — three do NOT fire, and that is the certification verdict

| self-test | frozen threshold | measured | fired? |
|---|---|---|---|
| **FT-NC** ★ | `≥ 1e-30` | `0.281050872448155` | **FIRES** |
| **FT-0** | `≥ 1e-13` | `2.0668129844705777e-12` | **FIRES** |
| **FT-SHORT** ★★ | `≥ 1e-2` | `0.2739562093388408` | **FIRES** |
| **FT-1** (control / IN) | `≥ 1e-20` | `9.946402719819208e-12` / `9.91230144564457e-12` | **FIRES** |
| **FT-3** (control / IN) | `≥ 1e-3` | `0.1521820946917692` / `0.03667623351896569` | **FIRES** |
| **FT-4(a)** (control / IN) | `≥ 1e-25` | `4.316731050519307e-17` / `1.9013913017026223e-19` | **FIRES** |
| **FT-4(b)** (control) | `≥ 1e-6` | `0.0004403753009474462` | **FIRES** |
| **FT-5** (control) | count `≠ 1` at ≥ 1 order | `[2, 1, 2, 1]` | **FIRES** |
| **FT-8** (control / IN) | `≥ 1e-9` | `3.8343049675985186e-07` / `1.2354164130261005e-05` | **FIRES** |
| **FT-10** (control / IN) | `≥ 1e-6` | `0.0002919046996412571` / `0.013250813115859395` | **FIRES** |
| **FT-2** ✗ | `≥ 1e-3` | `0.00044024054986192525` / `0.00035819373665375967` | **DOES NOT FIRE** |
| **FT-2c** ✗ | parameter below its floor `1.0` | stagnated `2.115446629621273` / `8.845771752822197` | **DOES NOT FIRE** |
| **FT-W** ✗ | limbs **(iii)** and **(iv)** must both fail at `Ω = 0.5` | (iii) fails; **(iv) holds**, resonance distance `1.0` | **DOES NOT FIRE** |

**The prereg's §6 heading states the rule in its title — *THE FIREABILITY SELF-TESTS (each MUST fire; a gate that cannot fail is not a gate)* — and §7.1 turns it into a bin: frozen,** `any RUN gate FAILS, or any self-test fails to fire, or any gate is UNRUN, for that configuration` **is exactly the `BIN-B-S` condition. Three did not fire. Every configuration with a root is therefore `ROOT-NOT-CERTIFIED` and no physics bin is adjudicated.** The three causes are diagnosed in §7 and every one of them is a **threshold this lane sized wrong at freeze**, not a defect in the operator, the wall row, or the located root.

---

## §2 — ★ THE RHO-B WALL ROW, DERIVED AND THEN MEASURED — AND ITS DISAGREEMENT WITH RHO-A

**Everything in §2.1 is a THEOREM of the prereg's §2, available before the run. Frozen:** `the derived wall statements of section 2 are theorems available before the run and may NOT be presented in the result doc as discoveries of the instrument`. **They are restated here as derivations. What the instrument added is §2.2 and §2.3.**

### §2.1 The derivation, restated (not re-derived, not presented as a measurement)

`ρ` enters the toroidal radial system at exactly one place, the combination `ρ/μ`. With `μ = G_vac S` held (the `μ`-primary reading, frozen at §2.2 of the prereg and fenced against the `c`-primary alternative):

```
c_shear = sqrt(mu/rho_eff) = c_0 S^2                (RHO-A: c_0 sqrt(S))
Z_shear = sqrt(mu rho_eff) = rho_eff c_shear = 1/S  (RHO-A: sqrt(S))
int dr / c_shear ~ int d(eta)/eta  ->  LOG-DIVERGENT (RHO-A: finite)
Om^2 coefficient:  Om^2 (1 + S^2)/S^4               (RHO-A: Om^2/(S(1+S)))
eta = 0:  REGULAR SINGULAR point                    (RHO-A: ORDINARY point)
indicial:  sigma(sigma-1) + Om^2 = 0
```

**★ THE DISAGREEMENT WITH RHO-A, IN FULL, AS THE BRIEF REQUIRES.**

| axis | RHO-A (v2.4, certified) | RHO-B (this lane, derived) |
|---|---|---|
| `η = 0` classification | **ordinary point** | **regular singular point** |
| wall impedance `Z = sqrt(μρ)` | `sqrt(S) → 0` — a **SHORT** | `1/S → ∞` — diverges |
| naive interface `Γ_shear` | `-1` | `+1` |
| optical distance to the wall | **finite** | **infinite** |
| wall row | `dψ/dη\|₀ = 0` (traction-free) | `dφ/dη\|₀ = 0` on `φ = η^{-σ}ψ` (Frobenius analyticity) |
| is the row a boundary condition? | **yes** — it selects one of two regular solutions | **no** — it is an analyticity constraint; the physical selection is the branch exponent |
| corpus statement it honours | `vol3/claim-quality.md:123`, `Z_shear → 0` short, *"echoes are predicted"* | **none — it contradicts `:123` at the wall** |

**Frozen:** `the RHO-B wall row DISAGREES with the RHO-A row in kind and not only in value: RHO-A's is a boundary condition at an ordinary point selecting one of two regular solutions, RHO-B's is an analyticity constraint at a regular singular point whose physical content is carried by the branch exponent; the RHO-B impedance divergence contradicts vol3/claim-quality.md:123's Z_shear -> 0 short verbatim, that contradiction is SURFACED and not repaired, and no leaf is edited by this lane`. **Honoured: no leaf is edited.**

**The naive interface reading is recorded and then rejected, by derivation, not by preference.** Frozen: `the naive local-interface reading of that divergence is Gamma_shear = +1 (an OPEN) in place of RHO-A's Gamma_shear = -1 (a SHORT), and this lane records that reading and then REJECTS it as the wall row in favour of the graded-medium derivation of part (c), because there is no interface at r_sat — the medium's own impedance diverges continuously`. **This is the same substrate-native correction the polar lane applied to `Γ_bulk = +1` on its BRANCH-STIFF: a graded impedance divergence is not a second medium.**

### §2.2 What the instrument measured about the wall — the three derived-wall gates

| gate | what it measures | frozen | measured |
|---|---|---|---|
| **G-IND** | `\|σ(σ-1) + Ω²\|` at the located root, in mp, for **both** exponents | `1e-30` | exactly `0` |
| **G-FROB** | the derived bracket `(𝒜σ(σ-1) + η²𝒞)/η + σℬ` at `η = 1e-5` and `η = 1e-15` | ratio `≤ 1e-9` | `1.0000000003434282e-10` |
| **G-W** | the four wall limbs at the located root | booleans | all hold |

**`G-FROB` is worth reading twice.** A bracket with a **simple** zero at `η = 0` must shrink by exactly `1e-10` between those two abscissae. It shrinks by `1.0000000003434282e-10`. **The derived row is confirmed to ten significant figures as a first-order zero, which is precisely the statement `dφ/dη|₀ = 0` rests on.**

**`G-W`'s limbs at the located root:**

| limb | frozen condition | measured |
|---|---|---|
| `σ₊` | — | `0.8540436614074668` + `0.9052029603401721`i |
| `σ₋` | — | `0.14595633859253326` `-0.9052029603401721`i |
| **(i)** finite energy for `σ₊` | `Re σ₊ > 1/2` | holds |
| **(ii)** limit point | `Re σ₋ ≤ 1/2` | holds |
| **(iii)** ordering | `Re(σ₊ - σ₋) > 0` | holds |
| **(iv)** non-resonant | `min_k \|(σ₊-σ₋) - k\| > 1e-3`, `1 ≤ k ≤ 20` | `1.8337891396602275` |
| `\|σ₊ - σ₋\|` | reported | `1.9439540257849885` |

**★ AND THE NON-GATED TRACTION REPORT, which the prereg required and which is the sharpest single statement in this lane.** The prereg's `G-W` row requires the traction exponent Frozen: `Re σ − 1` to be **reported for both branches and not gated**. Measured: `-0.1459563385925332` for `σ₊` and `-0.8540436614074667` for `σ₋`. **Both are negative. The traction DIVERGES at the wall on BOTH branches at this root.** There is no finite-traction solution and *a fortiori* no traction-free one — which is the indicial theorem of prereg §2.4(d) turned into a measurement: **under RHO-B a free-surface wall condition is not merely a different condition, it is an unsatisfiable one.**

### §2.3 `FT-SHORT` — the wall row is LOAD-BEARING, measured

**Frozen:** `FT-SHORT exists to demonstrate that the RHO-B wall row is LOAD-BEARING rather than cosmetic: if imposing the rejected RHO-A traction-free row on the RHO-B operator moved the root by less than 1e-2 relative, then the wall-row derivation of section 2.5 would be doing no work`.

| quantity | value |
|---|---|
| root under the **rejected** RHO-A traction-free row, on the RHO-B operator | `1.0763874319332618` `-0.02415021827442051` |
| relative separation from the `ROW-IN` root | `0.2739562093388408` |
| frozen firing threshold | `1e-2` |
| **fires?** | **YES**, by a factor of 27 |

**Read plainly: importing RHO-A's wall row into RHO-B would have moved the answer by 27 per cent, to a root whose `Q` would be an order of magnitude above anything in this arc.** The brief's instruction — *do NOT import the RHO-A wall condition* — was not a formality.

---

## §3 — THE SEARCH, AND THE TWO NULLS

**The frozen seed rule, executed exactly.** Frozen: `the seed-selection rule and the independent physical-quadrant sweep are frozen here before any code exists; the sweep's output is REPORTED whether or not it agrees with the primary seed's root`.

### §3.1 The primary seed chain — reported, and it disagrees

| step | value |
|---|---|
| `Ω_A`, read programmatically from the merged v2.4 JSON | `1.8536552108408788` `-1.0072567831433188` |
| nearest `CFG-BOUND-POLY` pencil eigenvalue at `n = 48` | `2.169389621753286` `-0.46925128885615547` |
| its mp polish | `2.1693896217534925` `-0.46925128885126355` |
| `CFG-BOUND-FROB` polished from it | `-0.20536852387225474`i, **outside the physical quadrant** |
| `CFG-IN-FROB` polished from it | `-1.3445557174632785`i, **outside the physical quadrant** |

**The primary chain lands on the imaginary axis on both Frobenius branches, and the frozen physical-quadrant filter rejects both.** It is reported because the freeze requires it, not because it adjudicates anything.

### §3.2 The enumeration and the `n`-stability filter

The `CFG-BOUND-POLY` pencil at `n = 48` carries `96` eigenvalues after dedup, of which `19` lie in the physical quadrant with `|Ω| ≤ 8`. Those `19` are the frozen seed enumeration. **`BIN-B-N`'s frozen wording — `no root is located for that configuration, or no located root is n-stable between n = 48 and n = 80 at NSTABLE_REL` — applies the `n`-stability filter to LOCATED ROOTS, and that is how it is applied here.**

| configuration | roots located in the physical quadrant | `n`-stable | outcome |
|---|---|---|---|
| `CFG-BOUND-POLY` | `14` | `0` | **`BIN-B-N`** |
| `CFG-BOUND-FROB` | `1` | `0` | **`BIN-B-N`** |
| `CFG-IN-FROB` | `9` | `2` | root located |

### §3.3 ★ The two nulls are ARTIFACT-class and PHYSICS-class respectively, and the classification is stated

**`CFG-BOUND-POLY` — ARTIFACT-class, and it was disclosed in advance.** Frozen, before the run: `the unfactored instrument's wall row psi(0) = 0 ... its convergence is ALGEBRAIC because eta^(sigma_+) is not analytic`. The measurement is worse than that pessimism: the polished root wanders across the ladder and **no** located root survives the `n`-stability filter. **The polynomial function space does not contain `η^{σ₊}` with complex `σ₊`, so this null is a statement about the basis, not about the cavity, and §0's frozen artifact-class rule requires it to be said in the headline. It is.**

**`CFG-BOUND-FROB` — PHYSICS-class, and this is the more interesting null.** Here the function space **does** contain the endpoint behaviour exactly — that is what the Frobenius factoring buys, and `G-FROB` certifies it. The single located candidate `2.976013135309959` `-0.02673481415359522`i at `n = 48` collapses to `0.024370271722028894` `-0.19249955107351446`i at `n = 80`, a relative move of `2.956293886300157`. **No `n`-stable physical-quadrant root exists on the finite-energy branch.**

**And the mechanism is derived, not fitted.** With `η = e^{-τ}` in the optical-distance variable and the `e^{-iωt}` convention, `η^{σ₊} ~ e^{-(1/2 + iΩ)τ}` carries phase fronts at `t̂ + τ = const` — **propagating AWAY from the wall**. `ROW-BOUND` is therefore the *emerging-from-the-wall* branch, which for a ringdown is acausal; `ROW-IN`'s `σ₋` carries `t̂ - τ = const` — **into the wall** — and is the causal, Ax-3-licensed mirror of the outgoing port at infinity. **One branch radiates at both ends and has no resonance; the other is the standard quasinormal configuration and has two. This lane did not choose between the co-primary branches; the substrate did.**

> **⚑ AND THE LIMIT OF THAT SENTENCE, stated because it is easy to over-read.** `BIN-B-N` here means *this instrument, with this basis, in this coordinate, found no `n`-stable candidate among the `19` frozen seeds*. **It is not evidence of absence** and this document does not present it as any. **Frozen:** `it makes NO completeness claim and NO mode count`.

---

## §4 — THE BINS: NOT ADJUDICATED, AND THE PRECEDENCE THAT SAYS SO

The frozen precedence, per configuration, is `BIN-B-N` > `BIN-B-W` > `BIN-B-S` > `BIN-B-P1 / BIN-B-P2 / BIN-B-P3`.

| configuration | bin | certification |
|---|---|---|
| `CFG-A-CONTROL` | — (no physics bin by role) | **`ROOT-NOT-CERTIFIED`** — `G2` FAILS; `FT-2`, `FT-2c` do not fire |
| `CFG-BOUND-POLY` | **`BIN-B-N`** (ARTIFACT-class) | N/A — no located root |
| `CFG-BOUND-FROB` | **`BIN-B-N`** (PHYSICS-class) | N/A — no located root |
| `CFG-IN-FROB` | **`BIN-B-S`** | **`ROOT-NOT-CERTIFIED`** — every gate PASSES; `FT-2`, `FT-2c`, `FT-W` do not fire |
| **`BIN-B-STOP`** | **did not fire** — the negative control passed both limbs of `G-NC` | — |
| **`BIN-B-W`** | **did not fire** — all four `G-W` limbs hold at the located root | — |
| `BIN-B-4` | **`N/A BY CONSTRUCTION`** | declared in advance; unchanged by a pass or a failure |

**`BIN-B-P1`, `BIN-B-P2` and `BIN-B-P3` are `N/A — NOT ADJUDICATED` on every configuration.** No verdict language is used about them anywhere in this document.

---

## §5 — THE NOT-ADJUDICATED DIAGNOSTICS

**These are DIAGNOSTICS, not verdicts.** They are shipped for the same reason v2.2 shipped its `NOT-ADJUDICATED` diagnostics that v2.4 later certified: **so a successor inherits a measurement rather than a silence.** The frozen precedence banked `BIN-B-S`; nothing below is banked as a bin outcome, and no line of this document may be quoted as one.

### §5.1 The located `ROW-IN` root

| quantity | value |
|---|---|
| `Ω`, mp strings | `1.021058710655384226893259908522031969379` `-0.3138716383801338012812670641580672390478` |
| `n`-stability, `n = 48` against `n = 80` | `3.665073726334936e-13` |
| `\|Ω\|` | `1.0682117280692367` |
| `ω_R M_g = Re(Ω)/x_sat` | `0.1458655300936263` |
| `ω_I M_g = \|Im(Ω)\|/x_sat` | `0.04483880548287626` |
| `Q = Re(Ω)/(2\|Im Ω\|)` | `1.6265545939814532` |

**A second `n`-stable root exists** at `n`-stability `8.509638653899817e-08` with `Q` = `0.4197942558740729`; it is reported in the shipped `top_five` and is **not** the top by the frozen ordering. Nothing further is claimed about it, and **no mode count of any kind is made.**

### §5.2 The comparison, in the frozen coordinates

| quantity | RHO-A (v2.4, **certified**) | RHO-B `ROW-IN` (this lane, **not certified**) |
|---|---|---|
| `ω_R M_g` | `0.2648078872629827` | `0.1458655300936263` |
| `Q` | `0.9201502744197103` | `1.6265545939814532` |
| `D_omega` | `-0.2913322255921462` | `-0.6096407790466821` |
| `D_Q` | `-0.561877761595111` | `-0.2255289604164633` |
| sub-bin **had it been adjudicated** | `BIN-1-MISS` / `BIN-2-MISS` | `BIN-B-P1-MISS` / `BIN-B-P2-MISS` |

GR comparators, read programmatically: `0.37367` and `0.08896`, hence `Q_GR` = `2.1002135791366907`. The corpus convention is `Q = 2`.

### §5.3 ★ The fork discriminator's DIRECTION

| axis | RHO-A | RHO-B | direction |
|---|---|---|---|
| `\|D_omega\|` | `0.2913322255921462` | `0.6096407790466821` | **WORSE** |
| `\|D_Q\|` | `0.561877761595111` | `0.2255289604164633` | **BETTER** |

**Token: `BIN-B-P3-RESCUE-PARTIAL`. `BIN-B-P3-RESCUE-DECISIVE` does NOT fire** — the frozen decisive criterion requires **both** deviations below `0.10`, and `|D_omega|` is six times that.

**Frozen, and it applies:** `if BIN-B-P3 lands WORSE-BOTH or NEUTRAL, then FORK-3(b) is NOT the explanation of v2.4's BIN-1/BIN-2 misses`. **This lane landed neither of those tokens, so that frozen sentence does not fire, and the honest statement is the one the token itself carries: FORK-3(b) moves the two axes in OPPOSITE directions.** It roughly halves the `ν_vac`-free `Q` deficit and roughly doubles the `ν_vac`-carrying `ω_R` deficit. **It is not a rescue and it is not a clean refutation.**

**And the discriminator, reported without dressing.** `0.4736589851552375` against `0.3734454060185468` gives the token `BIN-B-P2-CLOSER-CONVENTION`. **That is not support for `Q = ℓ = 2`.** `Q` misses GR by 23 per cent and the convention by 19 per cent; it is nearer one of two values it misses. **The physical content is that the RHO-B ingoing-wall cavity is a substantially higher-`Q` resonator than the RHO-A short-wall cavity — and still not a GR one.**

---

## §6 — DISCRIMINATION NOTE: what this result does and does NOT mean

**Written under `consistency-vs-emergence` and `ave-discrimination-check`, to the standard the prereg fixed in advance rather than the standard the result invites.**

### §6.1 What is genuinely established

1. **The RHO-B axial operator and its wall row are DERIVED and correct.** `G-NC(a)` at exactly zero, `G-NC(b)` at `2.139211445202149e-40`, `G0` at `9.960790154561388e-14`, `G-IND` at exactly zero, `G-FROB` at `1.0000000003434282e-10`. **This is INSTRUMENT-CONSISTENCY class and it is not an emergence claim of any kind.**
2. **The wall's change of KIND is a theorem, not a measurement**, and it is the durable content: regular-singular in place of ordinary; `Z → ∞` in place of `Z → 0`; infinite optical distance in place of finite; **no satisfiable traction-free condition at all.**
3. **`FT-SHORT` establishes that the wall row is load-bearing** at `0.2739562093388408`.
4. **The `ROW-BOUND` / `ROW-IN` asymmetry is real and has a derived mechanism** (§3.3).

### §6.2 What is NOT established, without hedging

1. **No bin is adjudicated.** Three self-tests did not fire. `BIN-B-P1`, `BIN-B-P2` and `BIN-B-P3` are `N/A` and §5's numbers are diagnostics.
2. **Nothing about which inertia canon means.** Frozen: `this lane runs FORK-3(b); it does not adjudicate FORK-3, does not prefer RHO-B over RHO-A`. **The fork is exactly as open as it was.**
3. **Nothing about FLAG-W.** Frozen: `this lane is SHEAR-CHANNEL ONLY; it computes no bulk modulus, no dilatational speed, no polar/spheroidal branch and no coupled system, so it CANNOT and DOES NOT adjudicate FLAG-W; the section 9 appendix is a DERIVED-CONSEQUENCE FLAG for the core session's FLAG-W walk and repairs nothing, edits no leaf, and prefers no branch`. §8 is flag output.
4. **Nothing that rescues or deepens v2.4's misses.** v2.4 stands `ROOT-CERTIFIED` on the RHO-A operator it gated. Frozen: `whatever this lane measures, v2.4 stands ROOT-CERTIFIED on the RHO-A operator it gated`.
5. **Nothing about completeness.** `BIN-B-4` is `N/A BY CONSTRUCTION`. The `[1, 1, 1, 1]` isolation row on the **control** says nothing about the RHO-B spectrum, and **no isolation claim of any kind is made for either Frobenius configuration** (prereg §4.1).
6. **No cross-instrument corroboration for `ROW-IN`.** Frozen: `there is NO second instrument for ROW-IN, no agreement gate exists for it, and no ROW-IN number in this lane carries cross-instrument corroboration of any kind`. **`G-AGREE` is `N/A BY OUTCOME` and is not spent as anything.**
7. **No implementation independence.** The machinery is carried over from v2.4 by read-only import. Frozen: `it is NOT an independent reimplementation, it claims no reimplementation independence from v2.4`.
8. **Nothing Cosserat-complete, nothing polar, nothing about spin.**

### §6.3 The honest classification

**This is a DERIVATION result with a certified negative control, a certified wall analysis, two clean nulls with a derived mechanism, a located-but-uncertified pole, and three self-test sizing errors that cost the lane its certification.** The one thing in it that could ever become an AVE-distinct forward prediction — **an AVE saturation wall that behaves like a horizon rather than a mirror, and what that does to ringdown echoes** — is a *derived structural* statement whose *quantitative* consequence is **not** certified here. **This document is not a chord and does not present itself as one.**

---

## §7 — FLAG-DON'T-FIX: what is routed, and to whom

### §7.1 ★ The four freeze-time sizing errors — diagnosed exactly, NOT retuned, repairs named

**Rule 11 forbids dropping, widening or re-defining a frozen criterion after a result is seen. All four stand as frozen. Each is diagnosed here so a successor freezes the right number rather than re-discovering the wrong one.**

| # | defect | why it failed | the successor's repair |
|---|---|---|---|
| **S1** | **`FT-2` does not fire.** Threshold frozen at `1e-3`; measured `0.00044024054986192525` (control) and `0.00035819373665375967` (`ROW-IN`) | This lane set `FT-2`'s threshold **equal to `G2`'s loose algebraic tolerance**. The `n = 8` mutation genuinely moves the root — v2.4 measured the same `0.0004403753009474462` and **fired**, because v2.4 froze `1e-6`. **The mutation works; the threshold was mis-sized.** | freeze `FT-2` at `1e-6`, as v2.4 did, **decoupled from `G2`'s tolerance** — a self-test threshold must be sized against the mutation's measured effect, never against the gate's tolerance |
| **S2** | **`FT-2c` does not fire.** Stagnated fit gives `2.115446629621273` (control) and `8.845771752822197` (`ROW-IN`), both above the frozen floor `1.0` | Two compounding mis-sizings: the `1e-12` stagnation increment is far below the coarsest rung's own error, and the floor `1.0` is an *existence-of-decay* threshold with no discriminating power. v2.4's analogue froze the floor at its band's **lower edge** and measured `0.073` | freeze the stagnation increment at the **reference rung's own error scale**, and freeze the law floor as a genuine band edge rather than an existence threshold |
| **S3** | **`FT-W` does not fire.** At `Ω = 0.5` limb **(iii)** fails but limb **(iv)** holds, resonance distance `1.0` | The frozen mutation point makes the two exponents **equal** (`\|σ₊-σ₋\| = 0`), which is the `k = 0` resonance — and the frozen limb (iv) ranges over `1 ≤ k ≤ 20`, so it cannot see it. **The frozen firing condition demands two limbs fail and the mutation point can only fail one.** | either extend limb (iv) to `k = 0` **or** freeze `FT-W`'s firing condition as *"at least one limb fails"*; the second is the honest fix, because a mutation that breaks one limb has already demonstrated the gate can fail |
| **S4** | **`G2` FAILS on the control** at `1.2496816388248957e-10` against `1e-10` | This lane froze the certification ladder as `n ∈ {32, 48, 64}`. **v2.4 excluded `n = 32` from its own certification ladder on a fitted-law argument**, and this lane did not carry that exclusion forward | carry v2.4's ladder placement, or freeze a tolerance derived from the ladder actually used. **The failure is nonetheless a receipt: it re-measures v2.4's `n = 32` finding to all digits from a different lane** |

**Two implementation defects were found and repaired between the first execution and the shipped one. Both are TIGHTENINGS in the direction of more checking, and neither changes a frozen criterion; they are recorded rather than left for a reader to find.** **D1** — the certified root was taken at `N_REF` rather than `N_PRIMARY`, so `G1` evaluated the `n = 48` operator at the `n = 80` root and `G10(b)` mirrored across two different orders; both were measuring the **ladder separation** instead of what they were frozen to measure. After the repair `G1` reads `4.726832751705419e-50` and `G10(b)` reads `9.273121713408482e-47`, **both identical to v2.4's published values to all digits**, which is the receipt that the repair restored the frozen measurement rather than a convenient one. **D2** — `G-W` limb (iv) computed `||Δ| - k|` where the frozen text specifies the **complex** distance `|Δ - k|`; the implementation now matches the freeze, and **the limb's verdict is unchanged at the located root.**

### §7.2 The canon flags this lane raises and does NOT adjudicate

1. **★ `FLAG-CANON` — routed to Grant and the auditor lane.** [`vol3/claim-quality.md:122`](../manuscript/ave-kb/vol3/claim-quality.md) writes `$Z_{shear} = \rho\,c_{shear} \to 0 \Rightarrow \Gamma_{shear} = -1$` with an **unnamed** `ρ` (the #814 CF-7 gap), and **`:124` of the same bullet list** writes *"$\rho_{eff} \to \infty$ as $\varepsilon_{11} \to 1$"*. **Substituting the leaf's own `:124` density into the leaf's own `:122` impedance formula inverts `:122`'s conclusion from `Γ_shear = -1` to `Γ_shear = +1`** — this lane measures that substitution as `Z_shear ∝ 1/S`. Both lines verified two-method at freeze and again at result. **Neither is repaired. Neither is preferred.** **The downstream statement at `:123` — *"GW (transverse shear) modes therefore reflect off `r_sat` — gravitational ringdown echoes are predicted"* — is RHO-A-conditional, and this lane says so without proposing an edit.**
2. **★ `FLAG-MU` — the `μ`-primary vs `c`-primary fork inside RHO-B**, forced and disclosed at freeze (prereg §2.2). The `c`-primary reading was fenced because it makes `μ = G_vac/S²` **diverge**, contradicting `claim-quality.md:123`'s `G_shear → 0` verbatim. **An open fork, not a settled question.**
3. **★ `FLAG-ROWCLASS` — `ROW-IN`'s branch selection is imposed only to algebraic accuracy** (prereg §2.6). The measurement is far better than the disclosure predicted (§1.3), which **does not** discharge the flag: the successor still needs an instrument whose function space **excludes** rather than approximates the `η^{+Δ}` branch. **This is the same exterior-complex-scaling build the polar lane's §6 item 2 and v2.4's FLAG-10 both route. One build discharges three routings.**
4. **★ `FLAG-CAUSAL` — NEW, and it is the physics question this lane surfaces.** The two derived wall rows are not physically symmetric: `ROW-BOUND` is *emerging-from-the-wall* and `ROW-IN` is *into-the-wall* (§3.3). **The prereg froze them CO-PRIMARY on the strength of the mathematics; the run shows only one of them supports a resonance.** Whether an infinite-electrical-length lossless termination is a legitimate Ax-3 radiative port — the §0 plumber question — is **Grant's call and is still owed.** This lane does not answer it and does not retire either branch.
5. **`FLAG-3` carried forward.** The reflectionless Regime-I port is derived **for this profile** (prereg §2.3), not for the universe.
6. **`FLAG-5` carried forward, unresolved.** No substrate-derived low-frequency cutoff. `BIN-B-4` stays `N/A BY CONSTRUCTION`.
7. **`FLAG-W` NOT TOUCHED.** Under a live Grant walk in the core session. §8 is input to that walk, not a contribution to its adjudication.
8. **v2.4's `BIN-3` plumber question is still owed** and is neither re-asked nor answered here; **no localization observable is computed in this lane at all.**

---

## §8 — ★ THE DERIVED-CONSEQUENCE APPENDIX (FLAG OUTPUT ONLY — repairs nothing, prefers no branch)

**Frozen:** `the section 9 appendix repairs nothing, edits no KB leaf, mints no claim, prefers no FLAG-W branch and adjudicates nothing; it exists to feed the core session's FLAG-W walk with a derived arithmetic consequence and its every row is a two-line algebraic substitution that any reader can check`.

**The two canon-available bulk-modulus branches, both inertia readings, exact powers of `S` at the wall.** `BULK-STIFF` is the `D = 1/S` stiffening branch (`saturating-modulus-and-backreaction.md:59`, verbatim *"**BULK stiffens:** $D=1/S\to\infty$ at $A\to1$ (the modulus goes rigid, halting the collapse)."*); `BULK-SOFT` is the `K = 2G`-tracking branch (`bulk-impedance-at-saturation-boundary.md:31`, verbatim *"$c_{bulk} \to 0$ (bulk dilatational speed vanishes at snap / rupture)"*, with `Z_bulk = ρ_bulk c_bulk → 0`). The `SHEAR` row is this lane's own channel and is included so the reader sees all three together.

| channel | inertia | `K ∝` | `ρ ∝` | `c = sqrt(K/ρ) ∝` | `Z = sqrt(Kρ) ∝` | wall verdict |
|---|---|---|---|---|---|---|
| BULK-STIFF | RHO-A | `S^-1` | `S^0` | `S^-0.5` | `S^-0.5` | **JAMS** (`Z → ∞`) |
| BULK-STIFF | RHO-B | `S^-1` | `S^-3` | `S^1` | `S^-2` | **JAMS** (`Z → ∞`) |
| BULK-SOFT | RHO-A | `S^1` | `S^0` | `S^0.5` | `S^0.5` | **VENTS** (`Z → 0`) |
| BULK-SOFT | RHO-B | `S^1` | `S^-3` | `S^2` | `S^-1` | **JAMS** (`Z → ∞`) |
| SHEAR | RHO-A | `S^1` | `S^0` | `S^0.5` | `S^0.5` | **VENTS** (`Z → 0`) |
| SHEAR | RHO-B | `S^1` | `S^-3` | `S^2` | `S^-1` | **JAMS** (`Z → ∞`) |

The bulk rows carry a prefactor `sqrt(2)`; the shear rows carry `1`. Evaluated on the shipped grid `S ∈ {0.1, 0.01, 0.001}` every `Z` in a JAMS row grows and every `Z` in a VENTS row shrinks; the driver ships the numbers.

**Three flag-level statements, each a direct consequence of the table and none of them an adjudication:**

1. **RHO-B inverts `2` of the six rows' conclusions** — `BULK-SOFT` and `SHEAR` — and the shipped object names them. **The inversion is not a sign flip in the SPEED: `c → 0` in every RHO-B row. It is a flip in the IMPEDANCE**, because the inertia divergence `S^-3` beats every modulus grading canon carries, which is at most `S^+1`.
2. **★ THE FLAG-W SIGN SPLIT EXISTS UNDER RHO-A AND DISAPPEARS UNDER RHO-B.** The shipped object records `flag_w_sign_split_under_RHO_A = true` and `flag_w_sign_split_under_RHO_B = false`. Under RHO-A the two canonical voices genuinely disagree — `BULK-SOFT` vents, `BULK-STIFF` jams. **Under RHO-B they agree: both jam.** **This is offered to the FLAG-W walk as an arithmetic fact about canon's own formulas and NOTHING MORE — it does not tell Grant which voice is right, and this lane explicitly does not claim that RHO-B "resolves" FLAG-W.**
3. **`bulk-impedance-at-saturation-boundary.md:31`'s conclusion is RHO-A-conditional in its own notation.** That leaf writes `Z_bulk = ρ_bulk c_bulk` with the **constant** `ρ_bulk` and concludes `Γ_bulk = -1`. **The `interior-singularity-resolution.md:19` leaf, in the same volume and chapter, writes `ρ_eff = ρ_0/S_topo^3 → ∞` at the same wall.** Substituting the second into the first inverts the conclusion. **Recorded, both paths cited, no leaf edited, no preference expressed.**

---

## §9 — VALIDATION AND SCOPE DISCLOSURES

- **Determinism.** Two full runs, digest `49c8c09cea8491b2` twice, shipped objects byte-identical apart from `_runtime_sec`. **The driver emits NO `pass` field for `G9`** — frozen: `this driver emits NO pass field for G9; it ships the run digest and the note only, the certification tally cannot read a G9 pass flag because none exists, and G9's verdict is obtained solely by the external two-run diff recorded in the result doc`. Runtimes are written **without back-ticks and are NOT registered**: `_runtime_sec` is machine-dependent, so registering it would fail the gating number check on every honest re-run on another machine (the #801 R3 lesson).
- **The gating number check** implements all six frozen fixes from the first commit, per the prereg §11 frozen text.
- **Engine fence.** `src/ave` byte-untouched; `ave.core.*` imported read-only through the read-only v2.4 import.
- **Predecessor fence.** Every predecessor file named in prereg §P.1 is **byte-untouched**, discharged by an empty `git diff --stat` against the freeze base. `research/drivers/coldq_pole_v2p4_root.py` is **imported read-only** as the negative control's comparison object and is neither edited nor executed as a battery.
- **One structural disclosure, restated.** The Frobenius operator is **transcendental in `Ω`** and admits no companion linearization, so seeding and isolation run on the unfactored quadratic pencil and **`G5` certifies isolation for the POLY instrument only.** Frozen and declared in advance.
- **Scope, unchanged:** `ℓ = 2` is an input; `ν_vac`, `K = 2G` and the `7` in `r_sat` are GR-imported and untouched; spin is out of scope; the Cosserat microrotational channel is not built; the polar branch is not built; **no completeness or overtone statement of any kind is made.**

---

> **Result provenance.** Resolves the frozen gates and bins of `research/2026-08-04_coldq-axial-rhob_prereg-FROZEN.md` (commit `e3a4181d`, COMMIT 1 of this lane, pushed **ALONE** before any driver code existed and before any number produced by this instrument existed). All numbers above are read from the shipped `research/drivers/coldq_axial_rhob_results.json` and are machine-verified against it by `research/drivers/coldq_axial_rhob_number_check.py`, wired into `make verify`. **Mints no `clm-`/`def-`; propagates to no leaf; engine byte-untouched; falsification ledger untouched.** Companion: the docket fragment `_orchestration/docket-entries/2026-08-04-coldq-axial-rhob.md`.

---

> **⚑ CONTINUUM-VS-LATTICE CARVE (Grant catch, 2026-08-04, post-return orchestrator note — amends
> the FRAMING, not the derivation).** The infinite-optical-distance / no-reflection-event /
> horizon-analogue statements above are properties of the **continuum limit** this instrument
> solves: the divergence of the optical integral exists only because the continuum integrates all
> the way to the level set. On the physical lattice the optical path is a **finite node-sum cut at
> the last cell** — effectively infinite (log-enhanced), not infinite. The horizon reading is
> therefore the continuum's own theorem, imported with the limit (the Lorentzian causal structure
> of the effective metric degenerating at the wall — the lattice's characteristics never fully
> collapse). Lattice-regulated statement: **total return after a finite, log-enhanced delay** —
> port-like below the return time (a long lossless line presents a real input impedance until the
> round trip completes), reactive store above it; the transfer-cost arrow never fires because the
> line has an end. `FLAG-CAUSAL` dissolves into this carve accordingly; what remained for Grant was
> ratifying the carve, given 2026-08-04 ("Go on all three"). The regulated-sum delay derivation —
> including the band-edge turning-point question and cutoff-robustness — is dispatched as its own
> lane (`research/echo-delay-regulated-sum` branch; docket
> `2026-08-04-echo-delay-regulated-sum.md`). The echo consequence updates from "RHO-A-only" to:
> both branches predict echoes with **different timing structure** — pending that lane's frozen
> bins. This note preserves the lane's §body verbatim per Rule 12; the lane's derivation was
> honest in its continuum terms, and its `FLAG-CAUSAL` framing was superseded by the carve, not
> refuted.
