# The cold-Q pole derivation v2.1 — RESULT: the instrument PASSED the entry ticket by 22 orders and is NOT CERTIFIED, because three of its own gate SPECIFICATIONS were defective

**Date:** 2026-08-03
**Prereg-file**: research/2026-08-03_coldq-pole-v2.1_prereg-FROZEN.md
**Prereg-commit**: 7d8fe484 (frozen and pushed ALONE, before any driver code and before any number existed)
**Driver:** [`research/drivers/coldq_pole_v2.py`](drivers/coldq_pole_v2.py) → [`research/drivers/coldq_pole_v2_results.json`](drivers/coldq_pole_v2_results.json)
**Number check:** [`research/drivers/coldq_pole_v2_number_check.py`](drivers/coldq_pole_v2_number_check.py) — gating via `make verify`
**Class:** DERIVATION result (research-doc; **mints no `clm-`/`def-`; propagates to no KB/manuscript leaf; changes no solidity; edits no falsification ledger**). Engine `src/ave` byte-untouched.
**Provenance:** Grant's GO, 2026-08-03, verbatim `[sic]`: `"Go on cold-Q"`. Written against `origin/main` = `583d43dd`.

> **★ POST-REVIEW CORRECTION — 2026-08-03. THIS DOCUMENT'S CENTRAL ATTRIBUTION WAS REFUTED BY MEASUREMENT AND IS RETRACTED HERE.** Adversarial review of PR #854 at head `bdcfa678` returned BLOCKED. The original HEADLINE attributed **all three** failures to defective gate SPECIFICATIONS rather than to the instrument. **Review refuted that for two of the three — by building this lane's own proposed replacement and by sweeping this lane's own unfrozen parameters.** Every corrected passage below is quoted verbatim before its correction and dated. **Nothing in either frozen prereg and nothing in the driver `coldq_pole_v2.py` was touched by this repair; no gate outcome, no tolerance, no verdict and no bin moved.** The certification `SOLVER-NOT-CERTIFIED` is unchanged — the *reason* is now honest. **§10 states plainly what survives.**

---

## HEADLINE

> **Certification: `SOLVER-NOT-CERTIFIED`. Frozen precedence therefore fires `BIN-F-SOLVER`, and NO physics bin is adjudicated.**
>
> Two of eleven gates failed (**C1**, **C9**) and one of ten self-tests did not fire (**FT-B**).
>
> 🔴 **RETRACTED 2026-08-03 (post-review). Original text, verbatim:** *"**All three failures are defects in this prereg's own gate SPECIFICATIONS, not in the instrument** — and that is a materially different result from #845's, whose failures were in its instrument."*
>
> **REFUTED BY MEASUREMENT, for two of the three.** Review built the C9 replacement **this document itself proposed** — a homogeneous outgoing probe at identical normalization, grid and probe points — and it **fails the same 6 of 9 probes at the same magnitudes** (§3.2). Review swept C1's two unfrozen parameters over `n` from `32` to `128` and over both precisions, and the high-`ℓ` winding **never** equals the closed-form count at any order and gets **monotonically worse** with `n` (§3.3). **Corrected attribution: C9 and C1's high-`ℓ` rows are REAL INSTRUMENT DEGRADATION, and they share one mechanism — spurious in-box discrete spectrum carried by the discretization.** Only **FT-B** is a specification defect, and even there the *number* this document reported was mis-provenanced (§3.1). **The two gates v2.1 added to certify the instrument's corners and edges did exactly the job they were added for: they caught a real defect in the instrument.**
>
> **This correction is adverse to the lane's own reading and it does not change the verdict:** `SOLVER-NOT-CERTIFIED` stood before it and stands after it. What changed is which object is at fault.
>
> **★ THE ENTRY TICKET WAS PASSED, DECISIVELY.** C1's low-`ℓ` rows are the *exact* control #845's FT-5 failed at `15.000`. v2.1 returns the closed-form root count `1`/`1`/`2` for `ℓ = 1, 2, 3`, an argument-principle winding of **exactly `1.0`/`1.0`/`2.0` stable at all three contour samplings**, and located roots matching the closed-form roots to `2.97e-44`, `3.54e-46` and `5.78e-42` against a frozen tolerance of `1e-20` — **inside the gate by roughly 22 orders of magnitude.** The compactified formulation does what the prereg said it would.
>
> **What actually failed** (🔴 the original heading read *"What actually failed, and why none of it is the method"* — the second half is **RETRACTED 2026-08-03**; two of the three are the instrument):
> - **C1's high-`ℓ` rows — REAL DEGRADATION.** 🔴 **Original text, verbatim, RETRACTED 2026-08-03:** *"where the *mp location* path is still perfect (`5.18e-38`, `1.58e-38`) but the *double-precision* seeding and winding path breaks over the large high-`Ω` box. **The prereg never froze a Chebyshev order for the control runs, and never froze the winding's precision.** Both are unfrozen parameters the gate's outcome depends on."* The unfrozen-parameter statement is **true but not exculpatory**: review swept both and the failure survives every setting (§3.3). The discretization carries **spurious in-box zeros** of `det M_n` over the high-`|Ω|` box; the argument principle is faithfully counting them.
> - **C9 — REAL DEGRADATION.** 🔴 **Original text, verbatim, RETRACTED 2026-08-03:** *"the gate probes a **forced** solution `M(Ω)ψ = b` at an arbitrary `Ω`, which is **not guaranteed analytic**: it develops a boundary layer of width `~1/|Im Ω|` at the compactified infinity. The gate therefore tests an object **the method never uses.** The objects the method *does* use — the QNM eigenfunctions — are analytic by construction and converge (C2 `3.33e-14`, C3 `8.33e-14` against `1e-12`)."* The forced-vs-homogeneous distinction is **measured to be irrelevant**: the homogeneous outgoing probe fails identically (§3.2). The failure sits on the rectangle's **low-`Re Ω` edge** and is a migrating pseudo-spectrum, not a boundary layer.
> - **FT-B** — the mutation is **structurally vacuous**: it asks to apply the gauge `λ` to the interior but not to the wall-BC row, and the graded wall-BC row (`ψ_η(0) = 0`) **carries no `λ` at all.** A self-test that cannot fire.
>
> **Per the frozen Rule-11 fence, none of this is repaired here.** No gate, tolerance or method element was changed after a gate result was seen. The lane banks the honest negative and routes to a **v2.2** successor with a new version number and its own verification chain — exactly as #845 routed to v2 and v2 to v2.1.

---

## §1 — DISCLOSED CODE-CORRECTNESS REPAIRS, and why they cannot have changed the verdict

**Three implementation defects were found by running, and repaired between run 1 and run 2. All three are the code failing to do what the prereg SAYS; no frozen criterion was touched.** This is the #845 precedent (its `scaled_geometry` repair), applied with the same disclosure.

| # | Defect | Effect | Repair |
|---|---|---|---|
| **B1** | The extended-precision polish ran mp arithmetic on a **double-precision operator**. The mp digits beyond the operator's own `~1e-16` accuracy were meaningless: the polish converged to the exact root of the *double* operator. | C1 location errors floored at `2.73e-10` … `8.67e-08`; C3 floored at `3.96e-12`. | Build the Chebyshev matrices and the whole operator in mp (`cheb_mp`, `graded_matrices_mp`, `flat_matrices_mp`). |
| **B2** | C9's right-hand side was `b = ones` on the **row-equilibrated** system, i.e. an unequilibrated RHS of `s_i`, and the row scales `s_i` grow like `n²`. **The boundary datum was resolution-dependent, so the BVP being solved changed with `n`.** | C9 measured `5.65` — meaningless. | Return the row scales and use `b = ones / s`. |
| **B3** | Both the polished root and the closed-form reference were cast to Python `complex`, truncating at `~1e-16`. **The frozen `1e-20` was unreachable by construction.** | C1 could not pass at any accuracy. | Keep mp end to end through C1's comparison. |

> **★ THE VERDICT WAS ALREADY FIXED BEFORE ANY REPAIR, AND THE REPAIRS DID NOT CHANGE IT.** FT-B's mutation is vacuous against the graded operator as a matter of the operator's *structure*, independent of any numerics — so `SOLVER-NOT-CERTIFIED` was determined the moment the battery first ran. **The repairs were made because a report that conflates "my code had a bug" with "the method cannot do this" is worth nothing to the successor**, not because they could rescue the certification. They could not, and they did not.

**Run 1 (pre-repair) is on the record:** `SOLVER-NOT-CERTIFIED`, failed gates `C1, C3, C9`, unfired `FT-B`, digest `8ed2738391046900`, runtime `408.73 s`.
**Run 2 (post-repair, shipped):** `SOLVER-NOT-CERTIFIED`, failed gates `C1, C9`, unfired `FT-B`, digest `e953f8882a4e675e`, runtime `445.26 s`. **C3 moved from FAIL to PASS purely by the B1 repair.**

A fourth, non-numerical change was also made: `fundamental()` is memoized on its exact argument tuple. This is a pure performance optimization with **zero** numerical effect (no RNG, no adaptivity: identical arguments deterministically produce identical results).

---

## §2 — THE GATE TABLE (measured vs frozen; nothing dropped, widened or re-defined)

**Frozen:** `no gate, tolerance, frozen numeric parameter or method element in sections 4 and 5 may be changed after any gate result is seen; if this instrument fails certification the lane reports SOLVER-NOT-CERTIFIED and routes to its own successor with a new version number, exactly as #845 routed to v2 and v2 routed to v2.1`.

| gate | what it certifies | frozen tol | measured | verdict |
|---|---|---|---|---|
| **C1** ★ | zero-grade closed-form control (the entry ticket) | count exact; loc `1e-20`; winding `1e-3` | **`ℓ=1,2,3` PASS** (see below); `ℓ=6,10,14,18` FAIL | **FAIL** |
| **C2** | hyperboloidal-gauge independence, `λ ∈ {−0.25, 0, +0.25}` | `1e-12` | `3.3268e-14` | **PASS** |
| **C3** | resolution convergence, `n ∈ {48, 56, 64}` | `1e-12` | `8.3318e-14` | **PASS** |
| **C4** | argument-principle consistency **+ count-vs-box-width scaling** | integer to `1e-3` | winding `2.0/2.0/2.0`, located `2`; width family all match | **PASS** |
| **C5** | `nu_vac`-cancellation across `x_sat ∈ {5,7,11}` | `1e-9` | `Q` spread **`0.0`**, `Omega` spread **`0.0`** | **PASS** |
| **C6** | spin-2 energy functional + spin-2-vs-spin-1 discrimination | resid `1e-9`; break `1e-3` | resid `5.7412e-12`; break `0.48017` | **PASS** |
| **C7** | Ax-3: closed doubly-traction-free cavity spectrum is REAL | `1e-10` | `1.7853e-27` over `63` modes | **PASS** |
| **C8** | determinism | identical digest | `e953f8882a4e675e` twice | **PASS** |
| **C9** ★ | graded-representation convergence at 9 rectangle probes | `1e-10` | `1.8993e+01` (5 of 9 probes pass) | **FAIL** |
| **C10** | outflow-row conditioning monitor | `rho_out·10^-dps ≤ 1e-15` | max `rho_out = 42.8037` → `4.28e-49`; margin over derived bound **36.37 orders** | **PASS** |
| **C11** | `η`-form ≡ `4η²`·`A`-form operator identity | `1e-13` | `8.9716e-16` | **PASS** |

### C1 in full — the entry ticket, row by row

| `ℓ` | `n` | closed-form count | located | max location error | winding @200/400/800 | verdict |
|---|---|---|---|---|---|---|
| **1** | 32 | 1 | **1** | **`2.971e-44`** | **`1.0 / 1.0 / 1.0`** | **PASS** |
| **2** | 32 | 1 | **1** | **`3.538e-46`** | **`1.0 / 1.0 / 1.0`** | **PASS** |
| **3** | 32 | 2 | **2** | **`5.778e-42`** | **`2.0 / 2.0 / 2.0`** | **PASS** |
| 6 | 40 | 3 | 3 | `5.177e-38` | `8.0 / 8.0 / 5.0` | FAIL (winding) |
| 10 | 40 | 5 | 4 | — | `6.0 / 10.0 / 8.0` | FAIL (count + winding) |
| 14 | 40 | 7 | 5 | — | `3.0 / 2.0 / 2.0` | FAIL (count + winding) |
| 18 | 40 | 4 | 4 | `1.577e-38` | `4.0 / 4.0 / 12.0` | FAIL (winding) |

> **★ Read the low-`ℓ` rows against #845.** This is the **same control problem, the same box, the same closed-form reference**. #845's FT-5 returned a winding of `15.000` for all three `ℓ`. **v2.1 returns `1.0`, `1.0`, `2.0` — the exact closed-form counts — identically at all three contour samplings, and locates the roots to within `3.538e-46` of the closed-form values.** Frozen: `on the zero-grade control, for ell in {1,2,3} over the frozen control box and for ell in {6,10,14,18} over the frozen high-Omega box, the number of located roots inside the box equals the closed-form root count computed at run time from the degree-(ell+1) polynomial, the located roots match the closed-form roots to <= 1e-20 absolute, and the argument-principle winding over the same box equals that same count exactly to <= 1e-3`. **The `ℓ ∈ {1,2,3}` half of that conjunction is satisfied with ~22 orders to spare; the `ℓ ∈ {6,10,14,18}` half is not, so the gate as a whole FAILS. It is reported that way and not split.**

### Self-test table (each MUST fire)

| self-test | targets | frozen threshold | measured | fired? |
|---|---|---|---|---|
| **FT-A** perturbed wall-BC row | C1 | `≥ 1e-15` | `3.7227e-09` | **FIRES** |
| **FT-B** gauge on interior but not the wall-BC row | C2 | `≥ 1e-12` | `1.8294e-14` | **DOES NOT FIRE** |
| **FT-C** under-resolved `n = 8` | C3 | `≥ 1e-6` | `4.4038e-04` | **FIRES** |
| **FT-D** empty box / closed-form box / single-pole box / **width family** | C4 | see prereg | all four cases correct; content saturates at `3` while width doubles `8 → 16` | **FIRES** |
| **FT-E** `x_sat`-dependent profile perturbation | C5 | `≥ 1e-9` | `6.0137e-07` | **FIRES** |
| **FT-F** spin-1 weighting **and** spin-1 wall condition | C6 | `≥ 1e-3` / `≥ 1e-2` | `0.48017` / `0.28424` | **FIRES** |
| **FT-G** smuggled loss `Im(μ)/Re(μ) = 1e-3` | C7 | `≥ 1e-5` | `5.0000e-04` | **FIRES** |
| **FT-H** probe at `Ω = 1e-36`; killed `ℬ(1)` | C10 | `> 1e-15` / `≥ 1e30` | `6e-14` / `inf` | **FIRES** |
| **FT-I** under-resolved graded probe `n = 8→16` | C9 | `≥ 1e-10` | `67.514` | **FIRES** |
| **FT-J** corrupted `η`-form coefficient | C11 | `≥ 1e-13` | `2.0668e-12` | **FIRES** |

**Frozen:** `a gate that cannot fail is not a gate; if any self-test fails to fire, the certification is SOLVER-NOT-CERTIFIED regardless of how many gates passed`. **FT-B did not fire. That alone is decisive, and it was decisive before any repair.**

---

## §3 — THE MECHANISM: three defective gate SPECIFICATIONS, named

### §3.1 FT-B is structurally vacuous against the object it targets

FT-B mutates by applying `λ` to the interior coefficients but **not** to the wall-BC row. In the **flat control** the wall row genuinely carries `λ` (`M1[n,n] = i(1−λ)`). In the **graded** operator the wall row is the exact SHORT

```
dψ/dη |_{η=0} = 0
```

which contains **no `λ` and no `Ω`**. The mutation is therefore indistinguishable from simply running at `λ = 0` — and by gauge invariance that returns the *same* eigenvalue (measured `1.83e-14`, i.e. C2's own agreement level). **The self-test cannot fire because there is nothing at the graded wall row for it to break.** This is a defect in the *prereg's* mutation design, discovered only by running — precisely what Rule 10 says empirical drivers are for.

### §3.2 C9 measures REAL instrument degradation on the frozen rectangle's low-`Re Ω` edge — the gate v2.1 added to certify corner accuracy WORKED

🔴 **THE ORIGINAL §3.2 IS RETRACTED IN FULL, 2026-08-03, REFUTED BY MEASUREMENT. Original heading, verbatim:** *"§3.2 C9 probes an object the method never uses"*. **Original mechanism paragraph, verbatim:**

> *"C9 solves the **forced** problem `M_n(Ω)ψ = b` at arbitrary `Ω` and requires resolution-doubling convergence. But the method's guarantee is that the **outgoing homogeneous** solution is analytic — the ingoing branch carries the essential singularity `e^{−2iΩ/A}`. A *forced* solution generically excites that branch, which for `Im Ω < 0` decays as `e^{2 Im(Ω)/A}`: a boundary layer at the compactified infinity of width `~1/|Im Ω|`. Chebyshev cannot resolve it at `n = 32/64` when `|Im Ω|` is large."*

**HOW IT WAS REFUTED — by building the replacement this document itself proposed.** Review implemented the **homogeneous outgoing probe** at identical normalization, identical grid and the identical nine probe points. **It fails the same 6 of 9 probes at the same magnitudes.** The forced-vs-homogeneous distinction the original paragraph rests on is therefore **measured to be irrelevant to the failure**. Two left-edge probes do not converge even under mpmath at `dps = 60` carried up to `n = 96`:

| probe `Ω` | homogeneous-probe diff | order pair |
|---|---|---|
| `0.14 − 3.5035i` | `6.963e-01` | `64 → 96` |
| `0.14 − 7i` | `5.620e+00` | `64 → 96` |

**THE MECHANISM, MEASURED.** The failure is a **migrating pseudo-spectrum adjacent to `Re Ω ≈ 0`**: the in-box pencil eigenvalue count grows from `2` to `9` as `n` goes `32 → 80`, and **only `Ω = 1.853655 - 1.007257i` is `n`-stable.** The discretization is manufacturing discrete spectrum on the rectangle's low-`Re Ω` edge, and every probe placed there sits in it. This is **not** a property of the boundary datum, of the forcing, or of arithmetic precision — it is the instrument.

**THE HONEST READING.** C9 is the gate v2.1 added to certify **corner accuracy on the frozen rectangle**. It found that the instrument is not accurate at the rectangle's left edge. **The gate worked.** The prereg pre-committed to exactly this reading at `research/2026-08-03_coldq-pole-v2.1_prereg-FROZEN.md:492`: *"if the graded solve nonetheless fails C9, that is an honest SOLVER-NOT-CERTIFIED and routes to a successor — it will NOT be retuned."* **That pre-committed reading is restored here.**

**WHAT A v2.2 HAS TO DECIDE — an instrument-SCOPE question, not a gate-wording repair.** Two honest routes, **neither taken here**: (i) **move the left edge**, with a *derivation* of where the spectral pollution threshold sits — not a fitted retreat from the failing probes; or (ii) **restrict the counting region** to the sub-rectangle the instrument can certify, and state plainly that the frozen rectangle is not it. **Both are decisions about what this instrument is for. They are routed to Grant, not resolved in this document.**

**The measured probe pattern (shipped JSON, retained as data):**

| probe `Ω` | `\|Im Ω\|` | diff `n = 32 → 64` |
|---|---|---|
| `14.0000 − 0.0070i` | 0.007 | `6.997e-14` ✓ |
| `7.0700 − 0.0070i` | 0.007 | `1.697e-13` ✓ |
| `14.0000 − 3.5035i` | 3.50 | `1.006e-11` ✓ |
| `7.0700 − 3.5035i` | 3.50 | `4.739e-09` |
| `0.1400 − 0.0070i` | 0.007 | `1.286e-08` |
| `14.0000 − 7.0000i` | 7.00 | `4.439e-08` |
| `7.0700 − 7.0000i` | 7.00 | `1.226e-03` |
| `0.1400 − 3.5035i` | 3.50 | `3.658e+00` |
| `0.1400 − 7.0000i` | 7.00 | `1.899e+01` |

🔴 **THE SIGNATURE CLAIMS ATTACHED TO THIS TABLE ARE RETRACTED, 2026-08-03. Original text, verbatim:** *"**The measured probe pattern is exactly that signature, and it is the cleanest evidence in this battery:**"* … *"Convergence degrades monotonically with `|Im Ω|/Re Ω` — the boundary-layer sharpness — and is at machine level wherever the layer is absent. **Meanwhile the physical eigenfunction, at `Ω = 1.8537 − 1.0073i`, is the analytic branch by construction, and C2 and C3 measure its convergence at `3.33e-14` and `8.33e-14`.** C9 as frozen tests the wrong object; the right object passes. **This is stated as a diagnosis, not as grounds to re-define C9, which the frozen fence forbids.**"*

**Three separate defects in that reading, all measured:**

1. **The monotonicity is FALSE in `|Im Ω|/Re Ω`.** One row of this lane's own table breaks it: `0.14 − 0.007i` has ratio `0.05` and diff `1.286e-08`, while `14 − 3.5035i` has ratio `0.2503` — five times larger — and diff `1.006e-11`, **three orders better.** The larger claimed "sharpness" converges better.
2. **The monotonicity is FALSE in `|Im Ω|` too.** The PR body stated the same claim in the bare-`|Im Ω|` variant; **the same pair violates it** (`0.007` → `1.286e-08` against `3.5035` → `1.006e-11`). Neither variable orders the data. **What orders it is `Re Ω`:** every failing probe has `Re Ω = 0.14` or sits at the extreme `|Im Ω| = 7`, and the two worst are both at the left edge.
3. **The `~1/|Im Ω|` layer width is DIMENSIONALLY INVERTED.** The recessive branch `e^{−2iΩ/A}` has magnitude `e^{−2|Im Ω|/A}` and transitions at `A ~ 2|Im Ω|`, so the layer width scales **`∝ |Im Ω|`, not `1/|Im Ω|`.** Larger `|Im Ω|` makes the layer **wider and easier** to resolve. The original paragraph inverted the very scaling it invoked, then read a false monotonicity as its confirmation.

**"The cleanest evidence in this battery" is retracted with it.** It was the least clean: a mechanism with the wrong scaling, supported by a monotonicity its own table falsifies.

**C2's and C3's convergence numbers (`3.33e-14`, `8.33e-14`) stand as measured** — but they are convergence *of one `n`-stable eigenvalue*, and they do **not** license the sentence they were used to support. **The right object does not "pass" in place of the wrong one: there was no wrong object.**

### §3.3 C1's high-`ℓ` rows: the discretization carries SPURIOUS IN-BOX ZEROS over the high-`|Ω|` box — the same mechanism as §3.2

🔴 **THE ATTRIBUTION IN THE ORIGINAL §3.3 IS CORRECTED, 2026-08-03. Original heading, verbatim:** *"§3.3 C1's high-`ℓ` rows depend on two parameters the prereg never froze"*. **Original attributing paragraph, verbatim:**

> *"**The prereg froze neither the Chebyshev order for the control runs nor the precision of the winding.** The driver used `n = 32` (low-`ℓ`) and `n = 40` (high-`ℓ`) with a double-precision winding, and those values are **not traceable to any frozen criterion**. Selecting them now — or promoting the winding to mp now — would be exactly the post-hoc parameter choice Rule 11 forbids. **They are left as they were at first run, the gate is banked as FAIL, and the parameters are routed to the successor prereg to be frozen with justification.**"*

**The two-unfrozen-parameters statement is TRUE. It is also MISLEADING, and review measured why.** Review swept both parameters — `n` from `32` to `128`, and mp against double:

- **The winding NEVER equals the closed-form count at any order.** There is no setting of the two unfrozen parameters at which this gate passes. It is not a parameter choice that was left open; it is a failure that has no parameter setting.
- **Raising `n` makes it monotonically WORSE.** At `ℓ = 6` the in-box **spurious** zeros grow `4 → 32` while the correctly-seeded **true** roots drop `2 → 1`. More resolution buys more pollution, not less.
- **The argument principle is faithful; the operator is not.** At `ℓ = 6`, `n = 40`, the double pencil finds **`8`** in-box eigenvalues against **`3`** closed-form roots, and the winding **correctly counts all `8`**. The counting instrument is doing its job exactly right: it is counting the zeros of `det M_n`, and **five of them are spurious.**
- **Precision is not the lever either.** mp reproduces **the same zeros**. Promoting the winding to mp — the candidate this document floated — does not remove them.

**CORRECTED ATTRIBUTION: the discretization carries spurious in-box zeros over the high-`|Ω|` box. This is the SAME PHENOMENON CLASS as §3.2** — the discrete operator manufactures spectrum that the continuous problem does not have, and the counting gates find it. **Two gates, one instrument defect.**

🔴 **The v2.2 candidate is STRUCK, 2026-08-03, MEASURED-REFUTED. Struck text, verbatim (from §8 item 1):** *"a frozen control order plus an mp winding at high `ℓ`"*. **It does not fix it:** no order passes, mp reproduces the same zeros, and higher orders are worse.

**What is retained from the original §3.3, as measured data:** at `ℓ = 6` and `ℓ = 18` the mp location path is perfect (`5.18e-38`, `1.58e-38` against `1e-20`) while the winding is unstable across contour samplings (`8/8/5`, `4/4/12`), and at `ℓ = 10, 14` the seeding misses roots (`4` of `5`, `5` of `7`). **The reading of those numbers is what changed:** the "misses" and the "instability" are both the discretization's own extra zeros moving with `n` and with the contour, not a precision floor. The run logs' `overflow`/`divide by zero` warnings from `slogdet` are a symptom of the same box, not the cause of the count.

**Rule 11 is untouched: nothing was retuned, no parameter was selected post-hoc, and the gate stays banked as FAIL.** The correction runs in the direction *against* this lane's interest — it removes the exculpatory reading, it does not supply one.

---

## §4 — THE FOUR FROZEN BINS: all four report `N/A — not adjudicated`

**Frozen:** `no adjudication criterion below may be dropped, widened or re-defined after any result is seen; no input in the section 3 ledger may be retuned; whatever the solver returns is banked`.

The frozen precedence is `BIN-F-SOLVER` > `BIN-F-PROFILE` > `BIN-F-NOPOLE` > `BIN-1/2/3/4`, with the instruction that if an earlier bin fires the later ones are reported as `N/A — not adjudicated` and **no verdict language is used about them.** **`BIN-F-SOLVER` fired.** Accordingly:

| bin | frozen outcome |
|---|---|
| **BIN-1** (`omega_R M_g`) | **`N/A — not adjudicated`** |
| **BIN-2** (`Q`) | **`N/A — not adjudicated`** |
| **BIN-3** (radial localization / FORK-1) | **`N/A — not adjudicated`** |
| **BIN-4** (overtone ladder) | **`N/A — not adjudicated`** |
| **BIN-F-PROFILE** | did not fire — no canonical-input contradiction was encountered on the domain |
| **BIN-F-NOPOLE** | did not fire — a pole was located |
| **`nu_factor_verdict`** | **`N/A — not adjudicated`** (downstream of BIN-1) |

**No verdict language is used below. The numbers in §5 are diagnostics.**

---

## §5 — NOT-ADJUDICATED DIAGNOSTICS (numbers, no verdicts)

These carry **no bin**, **no claim**, and **no solidity**. They are recorded so a successor lane with repaired gate specifications has a target to confirm or refute.

### §5.1 The least-damped physical root of the primary branch

Primary branch: `ρ = ρ₀`, `c_shear = c₀√S`, traction-free SHORT at `r_sat`, outgoing at infinity, `ℓ = 2`, `λ = 0`, `n = 48`, **zero free parameters**.

| quantity | measured |
|---|---|
| `Omega = omega*r_sat/c_0` (scale-free) | `1.8536552108408788 - 1.0072567831433188i` |
| `omega_R M_g` | `0.2648078872629827` |
| `omega_I M_g` | `0.14389382616333127` |
| `Q = omega_R/(2*abs(omega_I))` | `0.9201502744197103` |

Comparison quantities, computed from the shipped root and the frozen comparators (**stated, not adjudicated**):

- against the frozen GR cold comparator `omega_R M = 0.37367` (read programmatically from `KERR_QNM[0.00]`): `-29.13` percent.
- against the standing corpus shortcut `18/49`: `-27.91` percent.
- `Q` against `Q_GR = 2.1002135791366907`: `-56.19` percent. Against the rounded-prose `Q_GR = 2.099438202247191` (FLAG-1): `-56.17` percent.
- `Q` against the Op21 `2*pi`-convention `Q = ell = 2`: `-53.99` percent. Distances: `1.0798` to the convention value, `1.1801` to the GR value.
- `k_0*r_sat = 1.8536552108408788` against the standing chain's asserted `ell*(1+nu_vac) = 18/7 = 2.5714285714285716`.

> **★ The IDENTITY the prereg froze BEFORE any number existed, and it holds.** Frozen: `k_0*r_sat = x_sat * omega_R M_g identically, so the 9/7-above-cutoff test IS the omega_R versus 18/49 comparison re-expressed and is NOT an independent axis`. Both read `-27.91` percent. **It is one result, not two.**

**A second root was located and is EXCLUDED by the frozen physical criterion.** Frozen: `a located root is PHYSICAL only if it is present at every n in {48, 56, 64} within 1e-6 relative; roots failing this are reported as DISCRETIZATION ARTIFACTS and are excluded from every bin`. The root `0.30587571217415294 - 2.4674822214282157i` fails it and is banked as a **discretization artifact**, not an overtone. **No overtone ratio is computed.**

### §5.2 Radial localization

Both frozen measures agree exactly and both place the maximum at the **outer** edge of the frozen window `r/r_sat ∈ [1.0, 2.0]`: `u_energy = u_kinetic = 2.0000000000000004`, `interior_max = false`, wall energy density `0.040561477093055825` of the window maximum. The reserved `BIN-3-MONOTONE` sub-bin — *"localization is not a well-posed observable for this mode"* — is the one this would have landed in. As in #845, this reading is dominated by the generic outward `exp(|omega_I| r)` growth of any quasinormal eigenfunction rather than by substrate physics.

### §5.3 `ell`-ladder

**Frozen:** `DIAGNOSTIC — no bin, no verdict; FORK-12 is unanswered and this lane does not adjudicate it`. Measured `Omega`: `ell=2` → `1.8536552108408788 - 1.0072567831433188i`; `ell=3` → `2.513862504041755 - 0.8270827809320116i`; `ell=4` → `3.138966224667151 - 0.6935556956900625i`; `ell=5` → `3.7413481998279248 - 0.5832069991729377i`. **Unlike #845's ladder, all four rows rise monotonically in `Re Omega` and fall monotonically in `|Im Omega|`** — no seed-hit-noise signature. Recorded, **not interpreted**; FORK-12 remains unanswered.

### §5.4 Cross-lane comparison with #845 — REPORTED, NON-GATING

**Frozen (FLAG-2):** `the #845 FT-6 value 0.21729 is NOT-ADJUDICATED prior-lane data produced by a SOLVER-NOT-CERTIFIED instrument and therefore may not gate this lane; the spin-2-vs-spin-1 discrimination is gated instead on its OWN frozen thresholds (C6 and FT-F), and the comparison against 0.21729 is REPORTED as cross-lane corroboration with no gating power`.

| quantity | #845 (`SOLVER-NOT-CERTIFIED`, NOT-ADJUDICATED) | v2.1 (`SOLVER-NOT-CERTIFIED`, NOT-ADJUDICATED) | relative |
|---|---|---|---|
| `Omega` | `1.8536565650028993 - 1.00725725871003i` | `1.8536552108408788 - 1.0072567831433188i` | **`6.80e-07`** |
| `Q` | `0.9201505121823758` | `0.9201502744197103` | **`-2.58e-07`** |
| spin-1 weighting break | `0.21729` | `0.48017` | — |
| spin-1 / clamped wall shift | `0.28430` | `0.28424` | `2.1e-04` |

> **Two instruments that are different in kind — real-axis asymptotic matching with subdominant-coefficient extraction, versus compactified spectral with the outgoing wave divided out in closed form — agree on the scale-free eigenvalue to `6.8e-07` and on `Q` to `2.6e-07`.** That is a striking convergence and it is recorded as such. **It is NOT a verdict, NOT a bin, and NOT a certification:** both lanes are `SOLVER-NOT-CERTIFIED`, and two uncertified instruments agreeing does not certify either. It is offered as the single most useful pointer for the successor.
>
> **FLAG-2 is vindicated by measurement.** The spin-1 weighting break is `0.48017` here against #845's `0.21729` — they do **not** agree, exactly as the prereg predicted in advance, because the two lanes evaluate the Rayleigh quotient on **different objects** (#845 on a shot closed cavity at its own `R_wall`, v2.1 on this lane's frozen cavity at `R_wall = 8 r_sat`). **Had `0.21729` been made a gate, as the successor brief originally asked, it would have fired on a difference of setup rather than of physics.** The decision to gate the *discrimination* on its own thresholds and report the *number* as non-gating was the correct call, and the data now shows why.

---

## §6 — WHAT THIS LANE DID ESTABLISH

1. **★ The compactified formulation clears the entry ticket by ~22 orders.** On the exact control #845's FT-5 failed at `15.000`, v2.1 returns counts `1/1/2`, windings `1.0/1.0/2.0` stable at all three samplings, and locations to `3.538e-46`. **The named mechanism that killed #845 — asymptotic far-field series plus `exp(2|Im ω| R_match)` subdominant-coefficient extraction — is absent by construction, and the control now measures that.**
2. **The load-bearing algebra is verified as algebra.** C11: the `η`-form operator equals `4η²`·the `A`-form operator to `8.97e-16` on arbitrary analytic test functions that solve nothing.
3. **★ The `nu_vac` cancellation is EXACT, to the last bit.** C5 measures `Q` spread and `Omega` spread of **`0.0`** across `x_sat ∈ {5, 7, 11}` — not `1e-8`, not `1e-15`, but zero — while FT-E fires at `6.01e-07`, proving the gate is live and not dead. #845 measured `1.1058e-08` here and failed its own `1e-9`. The prereg's structural claim (§0) that the cancellation is exact **by construction** because the compactified coordinate *is* the Axiom-4 amplitude is confirmed at machine level.
4. **Ax-3 losslessness is structural.** C7: every one of `63` closed-cavity eigenvalues is real to `1.79e-27`; FT-G detects a smuggled `Im(μ)/Re(μ) = 1e-3` at `5.0e-04`.
5. **The counting instrument is now trustworthy in its certified range, and the box-width artifact class is excluded empirically.** C4's width family returns windings `0, 0, 1, 2, 3, 3` against run-time closed-form contents `0, 0, 1, 2, 3, 3` — **content saturates at `3` while the box width doubles from `8` to `16`, over a `32×` width span.** A count proportional to box width is decisively excluded. This is the direct empirical kill of the phase-rate artifact class §2.4 of the prereg describes.
6. **The spin-2 discipline is load-bearing and measured twice.** C6: spin-2 Rayleigh residual `5.74e-12`; spin-1 weighting break `0.48017`; spin-1 wall condition moves the fundamental by `0.28424`.
7. **Determinism.** Two full runs produced byte-identical shipped objects apart from `_runtime_sec`, digest `e953f8882a4e675e`.

---

## §7 — DISCRIMINATION NOTE: what a pass or fail in each bin would and would not mean

**Required by the lane's own discipline and written here even though no bin was adjudicated, so that the successor cannot present a future pass as more than it is.** Classification per `consistency-vs-emergence`.

| bin | class if it had been adjudicated | a PASS would mean | a PASS would **NOT** mean | a FAIL would mean |
|---|---|---|---|---|
| **BIN-1** `omega_R M_g` vs `0.37367` | **VALUE-CONSISTENCY**, never emergence | the graded-cavity eigenfrequency is numerically compatible with GR's `ℓ=2` fundamental | **anything about value-level emergence.** `omega_R M_g = Re(Omega)/x_sat` carries the GR-imported `nu_vac = 2/7` through the `7` in `r_sat = 7GM/c²`, whose provenance is closed as GR-import by PR #261/#506. A match here is a **consistency check on an imported scale** | the graded profile does not reproduce the GR fundamental — a clean negative on the standing chain's *value*, not on its form |
| **BIN-2** `Q` vs `2.10021` | **`nu_vac`-FREE — the only emergence-capable axis in this lane** | `Q = Re(Omega)/(2\|Im(Omega)\|)` contains no `r_sat` scale (C5 measures the cancellation as **exactly** `0.0`), so a match would be a **value-level result not inherited through the GR-imported `7`** | that AVE *derives* GR. It would mean the canonical profile + Ax-4 kernel + Op16 projection + `Γ=−1` SHORT produce GR's damping ratio with **zero free parameters** — a strong consistency result, and AVE-distinct only if the *form* differs from GR's own derivation | the substrate's cold `Q` differs from GR's. Given `Q = ℓ` is B1-ratified corpus, a fail would be routed to Grant as a **flag on the standing anchor**, not applied as a fix |
| **BIN-3** `r_peak/r_sat` | **FORM-class**, `nu_vac`-free | the mode localizes where one of the two standing pictures (rim vs ramp) says | much on its own — §5.2 shows the observable is dominated by the generic outward `exp(\|omega_I\|r)` growth of *any* QNM, which is why `BIN-3-MONOTONE` was reserved in advance | that the localization question is ill-posed for this mode — which is information, not failure |
| **BIN-4** overtone ladder | **FORM-class**, `nu_vac`-free ratios | the graded shear cavity has a radial-overtone structure matching GR's | that Op6's phase-matching condition is *derived* for this cavity — it is not, and FORK-9's formal half stays open | the cavity's ladder differs from GR's — a discriminating forward observable, and the most AVE-distinct thing in the bin set |

**Across all four: this lane can produce CONSISTENCY at best, never emergence at the value level for BIN-1, because the `7` is imported.** The `nu_vac`-free axes (BIN-2/3/4) are the only ones where a value-level claim could be made, and only BIN-2 has a sharp comparator.

---

## §8 — FLAG-DON'T-FIX: what is routed, and to whom

**Nothing below is repaired here.**

1. 🔴 **RETRACTED IN PART, 2026-08-03. Original text, verbatim:** *"**★ Three defective gate SPECIFICATIONS in this lane's own prereg — routed to a v2.2 successor, NOT repaired.** (i) FT-B's mutation is structurally vacuous against the graded wall row; (ii) C9 probes a forced solution that is not guaranteed analytic; (iii) C1's control Chebyshev order and the winding's precision were never frozen. **Per Rule 12 the slot is not refilled: v2.2 needs a new prereg with a new version number and its own verification chain, not an edit to this one.** Candidate replacements, stated so the successor does not have to rediscover them and **explicitly not adopted here**: a gauge mutation that targets a row that actually carries `λ`; a C9 replacement that probes the **homogeneous outgoing** solution (which the method guarantees analytic) rather than a forced one; and a frozen control order plus an mp winding at high `ℓ`."*

   **Corrected: ONE defective gate specification, not three, and TWO measured instrument defects.**
   - **(i) FT-B — SPECIFICATION DEFECT, stands** (§3.1), with its reported number's provenance corrected. Its candidate replacement — *a gauge mutation that targets a row that actually carries `λ`* — **stands, and review demonstrated it fires** at `6.4e-02` against `1e-12`.
   - **(ii) C9 — NOT a specification defect. REAL INSTRUMENT DEGRADATION** (§3.2). 🔴 **The candidate replacement is STRUCK, 2026-08-03, MEASURED-REFUTED. Struck text, verbatim:** *"a C9 replacement that probes the **homogeneous outgoing** solution (which the method guarantees analytic) rather than a forced one"*. Review **built it** — identical normalization, grid and probes — and it **fails the same 6 of 9 probes at the same magnitudes**, with two left-edge probes non-convergent at `dps = 60` up to `n = 96`. **It is not a replacement; it reproduces the defect.** What v2.2 must decide instead is an **instrument-scope** question — move the left edge with a derivation, or restrict the counting region — **routed to Grant, §3.2.**
   - **(iii) C1's high-`ℓ` rows — NOT a specification defect. The unfrozen-parameter statement is true but NOT the cause** (§3.3). 🔴 **The candidate replacement is STRUCK, 2026-08-03, MEASURED-REFUTED. Struck text, verbatim:** *"a frozen control order plus an mp winding at high `ℓ`"*. Review swept `n` from `32` to `128` and both precisions: **the winding never equals the closed-form count at any order, higher orders are monotonically worse, and mp reproduces the same zeros.** The discretization carries spurious in-box zeros of `det M_n`; the argument principle is faithfully counting them. **Same phenomenon class as (ii).**
   - **Per Rule 12 the slot is not refilled:** v2.2 needs a new prereg with a new version number and its own verification chain, not an edit to this one. **No v2.2 prereg is written here, and this repair does not write one.**
2. **⚑ FLAG-1 stands, and the review assertion attached to it remains falsified.** The frozen `Q_GR = 2.1002135791366907` is the programmatic `KERR_QNM[0.00]` value; the rounded-prose `2.099438202247191` is the same table at 3 s.f. A review claim that *nothing in the corpus reads 2.0994* is false — `research/2026-07-30_qlaw-derivation_scoping.md:401` reads it verbatim. **Routed to the auditor lane as a corpus-precision question.**
3. **⚑ FLAG-3 stands: I7 is assumed, not tested.** The reflectionless Regime-I port at infinity is a frozen canonical input, and this lane's entire method divides out the corresponding analytic factor. If the substrate carries any far-field reflector, every number here is wrong in the same direction. **Not tested; routed.**
4. **⚑ FLAG-4 stands: #814 CF-7's naming gap is untouched.** `vol3/claim-quality.md:122` writes `Z_{shear} = \rho\,c_{shear}` and never names which `ρ`.
5. **⚑ FLAG-5 stands: the `15.000` characterisation.** §2.4 of the prereg replaced the "optical length" reading with the phase-rate reading supplied by the concurrent #845 audit; this lane **cited** that refinement and did not re-derive it, and **no v2.1 gate depended on it** — the artifact class was excluded empirically by C4's width family instead. Correcting #845's own result-doc wording is that lane's move, not this one's.
6. **The `Q = ell` anchor is untouched.** Since **no bin was adjudicated**, there is not even a disagreement on the record to route — only a non-adjudicated diagnostic. `qnm-quality-factor.md`, `op21-multi-mode-mode-counting.md` and `regime-eigenvalue-method.md` are byte-untouched.
7. **`gates.C8.pass` is set by the driver as a placeholder.** Determinism is adjudicated **externally**, by running the driver twice and diffing the shipped objects. That was done: identical digests `e953f8882a4e675e`, byte-identical apart from `_runtime_sec`. **Disclosed so the JSON flag is not mistaken for a self-measurement.**

---

## §9 — RUNTIME AND SCOPE DISCLOSURES

- **Frozen:** `total battery runtime <= 3600 s on the reference machine; a longer run is disclosed, not silently accepted`. **Measured `445.26 s` and `450.74 s` — inside the budget.** The budget is not an adjudication criterion.
- **`_runtime_sec` is machine-dependent and is deliberately NOT registered** in the number check (the #801 R3/WARN-4 lesson).
- **Scope, unchanged:** `ℓ = 2` is an input, not derived; `nu_vac`, `K = 2G` and the `7` in `r_sat` are GR-imported and untouched; the spin (`a_* > 0`) mapping is out of scope; the spheroidal branch is not built; FORK-3(b) is not run; FORK-12 is not adjudicated.

---

> **Result provenance.** Resolves the frozen bins of `research/2026-08-03_coldq-pole-v2.1_prereg-FROZEN.md` (commit `7d8fe484`, COMMIT 2 of this lane, pushed ALONE before any driver code existed). All numbers above are read from the shipped `research/drivers/coldq_pole_v2_results.json` and are machine-verified against it by `research/drivers/coldq_pole_v2_number_check.py`, wired into `make verify`. Two full driver runs produced identical digests. Predecessor lanes, both unmodified: `research/2026-08-03_coldq-pole-v2_prereg-FROZEN.md` (commit `00724432`, superseded pre-measurement) and PR #845 (`SOLVER-NOT-CERTIFIED`). Mints no `clm-`/`def-`; propagates to no leaf; engine byte-untouched; falsification ledger untouched. Companion: the docket fragment `_orchestration/docket-entries/2026-08-03-coldq-pole-v2.md`.
