# PRE-REGISTRATION (FROZEN) — `G-RHO2` rerun v2: the off-limit sensitivity gate, re-sited BELOW its own crossover

**Date:** 2026-08-05
**Branch:** `research/last-bond-g-rho2-rerun`
**Written against `origin/main` =** `c4fdced0`
**Class:** DERIVATION prereg — a **VERSIONED SUPERSEDE of ONE GATE** of a merged lane. **Mints no `clm-`/`def-`; propagates to no KB/manuscript leaf; changes no solidity; edits no falsification ledger; engine `src/ave` byte-untouched and never imported.**
**SVA pilot case 8.**

**PREDECESSOR (merged, and the ONLY source of every parameter below):**

- prereg: [`research/2026-08-05_last-bond-kernel-collapse_prereg-FROZEN.md`](2026-08-05_last-bond-kernel-collapse_prereg-FROZEN.md)
- result: [`research/2026-08-05_last-bond-kernel-collapse_result.md`](2026-08-05_last-bond-kernel-collapse_result.md) — §1.1 gate table, §1.3 the `G-RHO2` diagnosis and the NAMED repair
- driver: [`research/drivers/last_bond_kernel_collapse.py`](drivers/last_bond_kernel_collapse.py) → [`research/drivers/last_bond_kernel_collapse_results.json`](drivers/last_bond_kernel_collapse_results.json)

**FREEZE RULE (inherited verbatim in force, restated):** *no gate, tolerance, bin boundary, frozen
numeric parameter, verdict wording or method element of §2–§7 may be changed after any number
produced by this lane's instrument is seen. If the certification fails, this lane reports the
failure, adjudicates nothing, and routes to a successor with a new version number.* **UNRUN ≠ PASSED.**

**WHAT THIS LANE MAY AND MAY NOT DO.** It may re-site ONE gate's injection points, in the regime the
predecessor's own §1.3 named. It may NOT move a tolerance, add a gate to the certification set,
drop a criterion, touch a bin boundary, or edit ANY predecessor artifact. **The v1 driver, the v1
results JSON, the v1 number-check and the v1 result doc are BYTE-UNTOUCHED by this lane** — that
is itself gated (§5, `NC-BYTES`).

---

## §0 — Standard Vacuum Analysis header (SVA v0.2, 11 rows)

 1. SECTOR / OWNERSHIP:      Unchanged from the predecessor and re-declared, not inherited by silence. **T2-shear** owns the propagating observable (the terminal reflection) and the bond modulus `G`; the last-bond stiffness `k_0` is a T2-shear transport coupling. **Cosserat rotation-winding** owns `G_c`/`γ` and is NOT touched by this gate. **A1 dilatation** owns the DC bias `A(r)` that grades `S`. **EM/T2-transverse** is DECLARED OUT. `Z_beyond` is a passive terminal load of unstated sector by construction — it is *arbitrary*, which is the whole point of the theorem being gated. **Cross-wiring check run:** nothing in this lane uses mass language for the winding sector or gap language for `A1`; `ρ_beyond` enters ONLY through `|Z_beyond|` and never as an inertia in a solved domain.
 2. REGIME / PHASE-STATE:    **MODE** = small-signal AC reflection at a terminal plane on a static DC bias; a scattering problem at REAL frequency, **not** an eigenvalue problem. **REGIME** = sub-yield lossless-reactive on the cold side `A < 1`; `A ≥ 1` enters ONLY as an arbitrary passive load. **PHASE-STATE** = cold lattice, Op14 ON as a static constitutive grade. **★ AND THE ONE REGIME THIS LANE ADDS, WHICH IS THE ENTIRE REPAIR:** Theorem 3(b) is an **OFF-LIMIT ASYMPTOTIC** statement, and an asymptotic statement has a **domain of validity**. That domain is `k_0 ≪ ω|Z_beyond|` (derived in §2). **v1 measured outside it.** A gate evaluated outside its own asymptotic domain reports the WRONG-REGIME plateau correctly and says nothing about the theorem — **an ARTIFACT-class null, not a falsification**, exactly as the predecessor classified it. This lane's sole content is putting the probe inside the domain.
 3. CIRCUIT STATEMENT:       Before any framework word: **a shunt compliance `1/k_0` in parallel with an arbitrary passive load `Z_beyond`, that parallel combination terminating a line of characteristic impedance `Z_1`.** `Z_load = k_0 Z_beyond/(k_0 + jωZ_beyond)`. The observable is the **terminal reflection residual `Γ + 1 = 2Z_load/(Z_load + Z_1)` at PLANE-LB** — a TOTAL observable (a ratio of two amplitudes at one plane), never a per-element slot. The gated quantity is the **sensitivity of that total observable to the load**, `|Γ(Z_b1) − Γ(Z_b2)|`, and its scaling exponent in `k_0`. **Plumber-physical:** a spring so soft that the wall behind it is invisible — the gate asks how fast the wall disappears as the spring softens, and v1 asked it at a stiffness where the spring was still stiffer than the line could tell.
 4. PLANE & PROJECTION:      **PLANE-LB (PRIMARY and ONLY plane of this gate)** — the inner terminal of the last cold node, referenced to the local characteristic impedance `Z_1` of the last intact cell, identical to the predecessor. **PROJECTION: SHUNT** — the collapsing bond loads the shunt branch (compliance `1/k_0 → ∞` ⇒ `Z_load → 0`), inherited DERIVED from the predecessor §3.1 and not re-derived here. **No plane shift is measured by this gate**; PLANE-N0 is `G-PLANE`'s object and is reproduced unchanged as a negative control (§5).
 5. CONSTITUTIVE PROVENANCE: Every parameter of the gate's operating point is **READ VERBATIM from the v1 driver and unchanged**: `S = 1e-9`, `p = 0.5` (RHO-A branch), `ℓ/r_sat = 6.0238983090250982e-19`, `ω/ω_C = 1e-19`, `Z_1 = S^{1−p}`, `Z_beyond ∈ {Z_1, 2Z_1}` (the two probe loads), mpmath `dps = 60`. **The ONE thing this lane changes is the parametrization of the injected `k_0`: `ε·k_cold` (v1) → `ε·ω·Z_1` (v2).** That change is **NOT this lane's invention** — it is the repair NAMED in the merged predecessor result §1.3 verbatim: *"Repair, named and routed: inject `k_0 = ε·ω·Z_1`, not `ε·k_cold`."* Provenance of the repair: **PREDECESSOR-NAMED, Tier-2-verified** (the predecessor's own review block independently confirmed diagnosis and repair regime). The `ε` VALUES are **ENG-CHOICE, frozen here, and justified by a stated margin** (§3).
 6. ENERGY LEDGER:           **No port is crossed anywhere in this lane and no loss word is used.** `Re{Z} = 0` at every element by Ax 3. `k_0` is real, `Z_1` is real-positive, `u ≡ k_0/(jω)` is purely imaginary — the injected soft bond is a **reactive** element, not a leak. The injected `k_0 > 0` does NOT open a port: it re-couples a reactive load, and the whole gated effect is a **phase-front** effect at `|Γ| = 1`. `|Γ| = 1` is reproduced as a negative control (`G-UNIT`, §5).
 7. CALIBRATABILITY:         The gated output is a **dimensionless scaling exponent** — a log-ratio of two dimensionless residual differences over a log-ratio of two stiffnesses. Both the injection parametrization and the crossover are carried as the **same** dimensionless ratio `δ ≡ k_0/(ω Z_1)`, so the repair is literally "set the dimensionless probe coordinate to a stated value" and the margin is stated in decades of `δ`. **`α` appears nowhere in any chain of this lane.**
 8. DISCRIMINATION CLASS:    **DC-internal.** This lane produces no observable, no chord and no discriminator, and is FENCED from producing one (§7). **Tautology filter, run at freeze:** the *repair* is not the *result*. It would be circular to freeze a gate whose passing is guaranteed by the algebra used to site it — so the freeze states, in §2, the CLOSED FORM from which both the crossover and the expected exponent follow, states the predicted number, and declares that **any disagreement between the run and that prediction is a FINDING against this lane's own algebra**, reported, not absorbed. **SM/GR counterfactual:** GR has no last bond and no bond modulus; the question is unavailable in the continuum theory. **This lane surfaces no discriminator and headlines none.**
 9. CERTIFICATION PLAN:      Gates §4, fireability self-test §4.2, negative controls §5, all frozen here **before any line of v2 code exists and before any number produced by the v2 instrument exists**. **UNRUN ≠ PASSED.** The certification set for Task 2 is the predecessor's, unchanged, with `G-RHO2` re-sited and nothing else touched. Determinism by two-run digest (`G-DET-V2`). Negative controls: **byte-exact string equality** against the shipped v1 renderings for every v1-passing gate, plus a byte-exact reproduction of the v1 FAILING `G-RHO2` value at the v1 siting (`NC-RHO2-V1`) — the strongest available proof that the instrument is unchanged and only the siting moved.
10. ADJUDICATION ROUTING:    **This lane settles ONE thing: whether the predecessor's TASK 2 certifies.** On `G-RHO2` PASS with every negative control byte-exact and `FT-RHO2` firing ⇒ **TASK 2 = `ROW-CERTIFIED`**, and **NOTHING ELSE IS UPDATED**. TASK 1 remains `SCAN-NOT-CERTIFIED` and is not touched. TASK 3 remains CERTIFIED and is not touched. `BIN-C-DISJOINT` is not revisited. **The print-language consequence** — whether `ROW-NOT-CERTIFIED` licensed a "mechanism confirmed" phrasing anywhere — is **RECORDED for the propagation pass and NOT EXECUTED here**; this lane edits no KB leaf, no manuscript file, no falsification ledger and no docket other than its own fragment. On `G-RHO2` FAIL **in the correct regime**, that is a FINDING against Theorem 3(b) itself, reported plainly, **with no retuning, no re-siting, and no second attempt in this lane** (Rule 11).
11. ★ NUMERICAL CONDITIONING: **NAMED CANCELLATIONS, before the first line of v2 code.** (i) The gated difference `Δ ≡ (Γ+1)|_{Z_b1} − (Γ+1)|_{Z_b2}` is a **catastrophic cancellation by construction**: both residuals are `≈ 2u/Z_1 = O(δ)` while their difference is `O(δ²)`, so **`log₁₀(2/δ)` significant digits are destroyed** at probe coordinate `δ`. At the frozen `δ_min = 1e-10` that is `10.3` digits of the `60` carried — `49.7` digits survive, and the frozen margin is stated in §3. This is the reason the working precision is mpmath `dps = 60` and **the reason `δ` is not pushed further down**: the *only* floor on how deep the probe may go is this cancellation, and it is named here, before it is met. (ii) `Γ + 1` is NEVER formed by adding `1` to a computed `Γ` — inherited verbatim, and enforced by **calling the predecessor's own `gamma_from_zload`**, not by reimplementing it. (iii) `Z_beyond = ∞` does not arise in this gate (both probe loads are finite by v1's construction); no float `inf` arithmetic anywhere. (iv) `u = k_0/(jω)` is purely imaginary, so `|2u + Z_1| = √(Z_1² + 4|u|²)` is evaluated by mpmath complex arithmetic and never by a real-part shortcut. **DYNAMIC RANGE.** `δ ∈ [1e-10, 1e-6]` (gate) and `δ ∈ [1e+6, 1e+10]` (self-test); `Δ ∈ [1e-20, 1e-12]` (gate arm) — all far inside `dps = 60`. **WORKING PRECISION.** mpmath `dps = 60`, imported by **reusing the predecessor module's own `mp` configuration**, so the two instruments cannot silently diverge in precision.

---

## §1 — REFERENTIAL INTEGRITY DECLARATION (frozen before code)

**UNCHANGED from v1, and reproduced byte-exact as negative controls (§5):**
`G-BOND`, `G-ROW`, `G-RHO`, `G-COLD`, `G-UNIT`, `G-PLANE`, `G-PREC`, `G-COND`, `G-NC-SIGN`,
`G-NC-ECHO`, `G-NC-ARITH`, `G-SCAN`, and the whole FT battery
(`FT-BOND`, `FT-ROW`, `FT-RHO`, `FT-PLANE`, `FT-ARITH`, `FT-COND`, `FT-SCAN`).
**Every tolerance, every bin boundary, every frozen numeric parameter, every sweep grid.**

**CHANGED — exactly one thing:** the `G-RHO2` injection siting, `k_0 = ε·k_cold` → `k_0 = ε·ω·Z_1`,
with frozen `ε` values (§3). **The `G-RHO2` acceptance interval `[1.9, 2.1]` is NOT moved.**

**ADDED — exactly two things, both mandated by the rerun brief and both declared here:**
`FT-RHO2` (the fireability self-test the repaired gate did not have in v1) and
`D-RHO2-PRED` (a **DIAGNOSTIC, explicitly NOT a gate** — see §4.3).

**NOT TOUCHED, and gated as such:** every predecessor artifact, byte-for-byte.

---

## §2 — THE REGIME DERIVATION (the crossover, from the shipped parameters, closed form)

### §2.1 The exact closed form

With `u ≡ k_0/(jω)` the shunt compliance's impedance, the predecessor's own two functions give

```
Z_load(Z_b) = k_0 Z_b/(k_0 + jω Z_b) = u Z_b/(u + Z_b)
(Γ+1)(Z_b)  = 2 Z_load/(Z_load + Z_1) = 2 u Z_b / (u Z_b + Z_1 u + Z_1 Z_b)
```

At the two probe loads v1 froze, `Z_b1 = Z_1` and `Z_b2 = 2 Z_1`, this collapses **exactly**:

```
(Γ+1)_1 = 2u/(2u + Z_1)                 (Γ+1)_2 = 4u/(3u + 2Z_1)

Δ ≡ (Γ+1)_1 − (Γ+1)_2 =  − 2u² / [ (2u + Z_1)(3u + 2Z_1) ]          [EXACT, no expansion]
```

`u` is purely imaginary, so with the **dimensionless probe coordinate**

```
δ  ≡  |u| / Z_1  =  k_0 / (ω Z_1)
```

the measured quantity has the **exact** closed form

```
|Δ|(δ)  =  2 δ² / [ √(1 + 4δ²) · √(4 + 9δ²) ]
```

### §2.2 The two regimes, and the crossover between them

```
δ ≪ 1 :  |Δ| → δ²        →  d(log|Δ|)/d(log k_0) → 2      THEOREM 3(b)'s ASYMPTOTIC REGIME
δ ≫ 1 :  |Δ| → 1/3       →  d(log|Δ|)/d(log k_0) → 0      THE PLATEAU
```

**The crossover is `δ = 1`, i.e. `k_0 = ω·Z_1`** — precisely the `k_0 ≈ ω|Z_beyond|` the predecessor
named, evaluated at the **binding** (smaller) of the two probe loads. Physically: the shunt
compliance stops being the small impedance the moment its reactance `k_0/ω` exceeds the load it is
shunting. Below that, the beyond-wall load is screened and enters at relative order `δ`, hence at
absolute order `δ²` in the difference — **which is the theorem**. Above it, the load IS the
termination and the exponent is genuinely `0` — **which is what v1 measured**.

### §2.3 Numerically, at the gate's own frozen operating point

Read verbatim from `last_bond_kernel_collapse.py` lines 441–445 (nothing here is chosen):

```
S = 1e-9   p = 0.5   ℓ/r_sat = 6.0238983090250982e-19   ω/ω_C = 1e-19

Z_1     = S^(1−p)  = 3.162277660168379332e-5
ω       = 1e-19/ℓ  = 0.16600545837597962708
k_cold  = S/ℓ      = 1660054583.7597962708

k_0^cross = ω·Z_1  = 5.2495535248837214353e-6        [≡ δ = 1]
```

which reproduces the predecessor's prose diagnosis (*"about five parts in a million"*) to its stated
precision. In v1's own `ε·k_cold` parametrization the crossover sits at
`ε^cross = k_0^cross/k_cold = 3.162277660168379332e-15`.

**The v1 injections, placed on this axis:**

| v1 `ε` | injected `k_0` | probe coordinate `δ = k_0/(ω Z_1)` | side of crossover |
|---|---|---|---|
| `1e-10` | `0.166005458376` | `31622.7766017` | **ABOVE** (plateau) |
| `1e-12` | `0.00166005458376` | `316.227766017` | **ABOVE** (plateau) |
| `1e-14` | `1.66005458376e-5` | `3.16227766017` | **ABOVE** (plateau) |

**All three are above the crossover** — the smallest by a factor `3.16`, the largest by `3.16e4`.
The predecessor's diagnosis is confirmed by independent re-derivation.

### §2.4 The derivation is validated against the v1 FAILURE value, before freeze — disclosed

Feeding the three v1 `δ` values through the §2.1 closed form and running v1's own fit
(`log(|Δ|₂/|Δ|₁)/log(k₂/k₁)`, pairwise, then the mean) gives per-pair exponents
`7.53906665558065023e-7` and `0.00740154840597281668`, mean `0.00370115115631918737`.
The **shipped** v1 values are `0.000000753906665558065022906244826996`,
`0.00740154840597281667640459023280`, mean `0.00370115115631918737071374823881`.
**They agree to every digit shown.** This is disclosed as a pre-freeze design input: the closed
form of §2.1 is not a guess, it reproduces the merged failure exactly, and the ONLY free parameter
left in the gate is where on the `δ` axis the probe sits.

---

## §3 — THE v2 GATE SPEC (frozen)

### §3.1 The injection siting

**Frozen, and NOT to be moved after any v2 number is seen:**

```
k_0(ε) = ε · ω · Z_1          ⇒     δ = ε   EXACTLY, by construction

ε ∈ { 1e-6 , 1e-8 , 1e-10 }               [three points, as in v1; two pairwise exponents; mean]
```

**Margin below the crossover, stated:** `6`, `8` and `10` decades. The *minimum* margin is
**6 decades**, i.e. the stiffest v2 injection is `10⁶` times softer than the point at which the
beyond-wall load stops being screened. The probe span is `4` decades of `k_0`, identical to v1's.

**Why `1e-6` and not stiffer:** at `δ = 1e-6` the closed form's departure from the pure power law is
`≈ 0.679 δ²  = 6.8e-13` in the exponent — already `11` orders inside the tolerance half-width.
**Why `1e-10` and not softer:** the §0 row-11 cancellation destroys `log₁₀(2/δ)` digits, `10.3` at
`δ = 1e-10`; going to `δ = 1e-25` would destroy `25.3` and there is no gain, because the exponent
has already converged. **Both ends are set by a named quantity, not by taste.**

### §3.2 The expected exponent, from the derivation

From §2.1, expanding the exact `|Δ|(δ)` for the pair `(δ₁, δ₂ = δ₁/100)`:

```
exponent(δ₁,δ₂) = 2 + [ ½ln((1+4δ₁²)/(1+4δ₂²)) + ½ln((4+9δ₁²)/(4+9δ₂²)) ] / ln(δ₂/δ₁)
                ≈ 2 − (25/8)·δ₁² / ln(100)   =  2 − 0.6786·δ₁²
```

**EXPECTED EXPONENT = `2`, with a predicted deviation of `0.6786 δ₁²`.**

### §3.3 The tolerance, and its headroom

**`G-RHO2` acceptance interval: `[1.9, 2.1]` — UNCHANGED FROM v1, character for character.**
No tolerance is derived, moved or widened by this lane. What is derived is the **headroom**:

| quantity | value |
|---|---|
| tolerance half-width about `2` | `0.1` |
| predicted deviation, stiffest pair (`δ₁ = 1e-6`) | `6.785e-13` |
| predicted deviation, softest pair (`δ₁ = 1e-8`) | `6.785e-17` |
| predicted deviation of the reported MEAN | `3.393e-13` |
| **HEADROOM (half-width / predicted deviation of the mean)** | **`≈ 2.9e11` ×** |
| working precision `dps` | `60` |
| worst-case digits destroyed by the named cancellation | `10.3` |
| **PRECISION HEADROOM (digits surviving / digits needed for a 2-decimal verdict)** | **`≈ 49.7 / 2`** |

**The gate passes or fails on `[1.9, 2.1]` and on nothing else.**

---

## §4 — THE GATE TABLE (frozen; UNRUN ≠ PASSED)

### §4.1 The re-sited gate

| gate | frozen criterion | siting |
|---|---|---|
| **G-RHO2** | fitted exponent of `\|dΓ/dZ_beyond\|` vs `k_0` **in `[1.9, 2.1]`** *(v1 wording and interval, unchanged)* | `k_0 = ε·ω·Z_1`, `ε ∈ {1e-6, 1e-8, 1e-10}` — **v2, sub-crossover** |

### §4.2 The fireability self-test for the repaired gate (MANDATORY; a gate that cannot fail is not a gate)

| self-test | frozen firing condition |
|---|---|
| **FT-RHO2** | re-siting the SAME instrument into the **plateau**, `ε ∈ {1e+6, 1e+8, 1e+10}` (i.e. `6`–`10` decades ABOVE the crossover), must drive the fitted exponent **OUTSIDE `[1.9, 2.1]`** — i.e. `G-RHO2` must FAIL there. Predicted: exponent `→ 0`. |

**`FT-RHO2` is the gate's own falsifier AND an independent second confirmation of the §2.2 two-regime
structure: the same code, the same tolerance, the probe coordinate moved across `δ = 1`, opposite
verdicts.**

### §4.3 The declared DIAGNOSTIC (explicitly NOT a gate; certification does not ride on it)

| diagnostic | frozen prediction | status if it disagrees |
|---|---|---|
| **D-RHO2-PRED** | the measured `G-RHO2` mean exponent equals `2` to within `1e-11` (the §3.2 derivation) | **REPORTED AS A FLAG against this lane's own algebra.** It does NOT change the certification verdict, which rides on `[1.9, 2.1]`. It is frozen here so that a *lucky* pass cannot be reported as a *derived* pass. |

### §4.4 Determinism

| gate | frozen criterion |
|---|---|
| **G-DET-V2** | two full v2 runs, identical digest, byte-identical output apart from `_runtime_sec` |

---

## §5 — NEGATIVE CONTROLS (frozen): byte-exact reproduction of the v1 record

**Method, frozen:** the v2 driver **imports the v1 driver module unmodified** and calls its own
`run_task2()`, `run_task3()`, `build_gates()` and `build_self_tests()`. Every reproduced value is
compared to the shipped `last_bond_kernel_collapse_results.json` by **`==` on the rendered strings**
(exact string equality, not a numeric tolerance). **Any single mismatch ⇒ the rerun reports
NOT-CERTIFIED and adjudicates nothing.**

| control | frozen criterion | class |
|---|---|---|
| **NC-GATES** | every field of `G-BOND`, `G-ROW`, `G-RHO`, `G-COLD`, `G-UNIT`, `G-PLANE`, `G-PREC`, `G-COND`, `G-NC-SIGN`, `G-NC-ECHO`, `G-NC-ARITH`, `G-SCAN` reproduces the shipped rendering with **exact string equality**, and every `pass` flag reproduces | mixed (see below) |
| **NC-FT** | every field of `FT-BOND`, `FT-ROW`, `FT-RHO`, `FT-PLANE`, `FT-ARITH`, `FT-COND`, `FT-SCAN` reproduces with **exact string equality**, and every `fires` flag reproduces | mixed |
| **NC-RHO2-V1** | re-running the **v1 siting** (`ε·k_cold`, `ε ∈ {1e-10,1e-12,1e-14}`) through the v2 code path reproduces the shipped failing exponent `0.00370115115631918737071374823881` **and both shipped per-pair values**, byte-exact | RECOMPUTED |
| **NC-ROWS** | `run_task2()` returns `3360` rows, matching the shipped `n_rows` | RECOMPUTED |
| **NC-BYTES** | the SHA-256 of each of the four predecessor artifacts (v1 driver, v1 results JSON, v1 number-check, v1 result doc) equals its `origin/main` blob hash — **this lane touched none of them** | FILE-HASH |

**REPRODUCTION CLASS LEDGER — declared at freeze so that no reproduction is over-claimed:**

- **RECOMPUTED** (the value is computed afresh from the frozen numerics by v1 code, and the string
  equality is a real test): `G-BOND`, `G-ROW`, `G-RHO`, `G-COLD`, `G-UNIT`, `G-PLANE`, `G-PREC`,
  `G-COND`, `G-NC-ARITH`, `FT-BOND`, `FT-ROW`, `FT-RHO`, `FT-PLANE`, `FT-ARITH`, `FT-COND`.
- **FILE-READ** (recomputed, but the input is a file read from the tree — reproduction also tests
  that those files have not drifted): `G-NC-SIGN`, `G-NC-ECHO`.
- **★ REPLAYED, and therefore NOT an independent reproduction — DECLARED, NOT DISCOVERED:**
  `G-SCAN` and `FT-SCAN`. The v1 corpus scan is **tree-state-dependent by the predecessor's own
  §1.3** (its output JSON, number-check and result doc all live inside the scanned tree, and this
  lane adds three more files to it), so re-running it on this branch **cannot** reproduce the shipped
  numbers and its failure to do so would carry no information. The v2 driver therefore **replays the
  shipped `task1_scan` block** into `build_gates`/`build_self_tests` rather than re-scanning.
  **The scan is NOT re-run, `G-SCAN` is NOT re-tested, TASK 1 remains `SCAN-NOT-CERTIFIED`, and the
  reproduction of those two entries is bookkeeping, not evidence.** It is listed above only so that
  the ledger is complete.

---

## §6 — THE CERTIFICATION DECISION (frozen wording; applied mechanically)

**TASK 2 certifies as `ROW-CERTIFIED` if and ONLY if ALL of the following hold:**

1. `G-RHO2` (v2 siting) measured exponent ∈ `[1.9, 2.1]`;
2. `FT-RHO2` FIRES (plateau exponent outside `[1.9, 2.1]`);
3. every `NC-` control above passes with **zero mismatches**;
4. `G-DET-V2` passes;
5. every Task-2 gate of the predecessor reproduces as PASS and every Task-2 self-test as FIRING.

**Otherwise TASK 2 reports `ROW-NOT-CERTIFIED` and this lane adjudicates nothing.**

**On certification, this lane updates NOTHING ELSE.** TASK 1 stays `SCAN-NOT-CERTIFIED`; TASK 3
stays CERTIFIED; `BIN-C-DISJOINT` is not revisited; no KB leaf, manuscript file, solidity, matrix
row or falsification-ledger entry is edited; **the predecessor's result doc is not rewritten and not
annotated** — the v1 record stands as the v1 record, and this lane is a separate, later, versioned
document, per Rule 12 (substitution-not-retraction: the v1 body is preserved intact).

**The print-language question** — whether a `ROW-NOT-CERTIFIED` Task 2 licensed any "mechanism
confirmed" phrasing downstream — **MOOTS on certification and is RECORDED for the propagation pass.
It is NOT EXECUTED by this lane.**

---

## §7 — FENCE (frozen)

This lane produces **no observable, no chord, no discriminator, no claim-id, no solidity change and
no propagation**. It touches `src/ave` not at all and imports it not at all. It settles nothing
about FORK-3(b), nothing about `FLAG-ECO`, nothing about `γ`/`G_c` VALUES, nothing about Regime-IV
interior physics, nothing observational, and nothing about the ruling whose premise TASK 1 was to
audit — **TASK 1 remains unadjudicated and this lane does not touch it.**

Deliverables, and the complete list of files this lane may create or modify:

- this prereg (frozen, pushed **ALONE**, before any v2 code exists);
- `research/drivers/last_bond_g_rho2_rerun.py` + its results JSON;
- `research/drivers/last_bond_g_rho2_rerun_number_check.py` (gating, with a mutation receipt);
- `research/2026-08-05_last-bond-g-rho2-rerun_result.md`;
- `_orchestration/docket-entries/2026-08-05-last-bond-g-rho2-rerun.md`;
- `Makefile` — one appended target plus the two shared lines named in §8.

**Nothing else. Any file outside this list appearing in the diff is a freeze violation.**

---

## §8 — DISCLOSED CONFLICT CLASS (frozen, carried forward unchanged)

The `Makefile` `.PHONY` line and the `verify:` prerequisite line **ARE shared with every other
lane's number-check target** and are a **REAL two-line union-conflict class** with any concurrently
open lane — not an append-only merge. The correct resolution is the **UNION** of all lanes' targets,
never a pick-one. This lane touches exactly those two shared lines plus one appended recipe block,
and declares it here at freeze rather than discovering it at merge.

---

**END OF FROZEN PRE-REGISTRATION.** Committed and pushed ALONE. No v2 driver code exists at this
commit; no number produced by the v2 instrument exists at this commit.
