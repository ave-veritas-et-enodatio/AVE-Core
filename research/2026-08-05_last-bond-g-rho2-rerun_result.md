# `G-RHO2` rerun v2 — RESULT: the off-limit sensitivity exponent is `2` when the probe is placed inside the asymptotic regime, and TASK 2 of the last-bond lane is **`ROW-CERTIFIED`**

**Date:** 2026-08-05
**Prereg-file:** [`research/2026-08-05_last-bond-g-rho2-rerun_prereg-FROZEN.md`](2026-08-05_last-bond-g-rho2-rerun_prereg-FROZEN.md)
**Prereg-commit:** `503579b0` (frozen and pushed **ALONE**, before any v2 driver code existed and before any number produced by the v2 instrument existed)
**Driver:** [`research/drivers/last_bond_g_rho2_rerun.py`](drivers/last_bond_g_rho2_rerun.py) → [`research/drivers/last_bond_g_rho2_rerun_results.json`](drivers/last_bond_g_rho2_rerun_results.json) (driver committed at `47b66275`, **before** this result doc existed)
**Number check:** [`research/drivers/last_bond_g_rho2_rerun_number_check.py`](drivers/last_bond_g_rho2_rerun_number_check.py) — gating via `make verify`, with a mutation receipt
**Class:** DERIVATION result — a **VERSIONED SUPERSEDE of ONE GATE**. **Mints no `clm-`/`def-`; propagates to no KB/manuscript leaf; changes no solidity; edits no falsification ledger.** Engine `src/ave` byte-untouched and never imported.
**Predecessor (merged, BYTE-UNTOUCHED by this lane — gated, `NC-BYTES`):** [`research/2026-08-05_last-bond-kernel-collapse_result.md`](2026-08-05_last-bond-kernel-collapse_result.md) §1.3, which diagnosed the failure and **named this exact repair**. Written against `origin/main` = `c4fdced0`.
**SVA pilot case 8.** Per-row fill notes in §5.

---

## REGIME HEADER (mandatory, restated at the point of reading; full 11 rows in the prereg §0)

**MODE** — small-signal AC reflection at a terminal plane on a static DC bias; a scattering problem
at REAL frequency, **not** an eigenvalue problem. **REGIME** — sub-yield lossless-reactive on the
cold side `A < 1`; the `A ≥ 1` region enters ONLY as an arbitrary passive load. **PHASE-STATE** —
cold lattice, Op14 ON as a static constitutive grade. **★ AND THE REGIME THAT IS THE WHOLE POINT:**
Theorem 3(b) is an *asymptotic* statement and an asymptotic statement has a *domain*, here
`k_0 ≪ ω|Z_beyond|`. **v1 measured outside that domain.** A null measured where the effect cannot
exist is **ARTIFACT-class, not a falsification** — and this rerun's only content is moving the probe
inside the domain and asking again.

---

## HEADLINE

> **★ CERTIFICATION, STATED FIRST AND WITHOUT SOFTENING.**
> **`G-RHO2` PASSES. TASK 2 of the last-bond lane is `ROW-CERTIFIED`.** The fitted off-limit
> sensitivity exponent is `1.99999999999966070743940658186`, inside the **unchanged** v1 acceptance
> interval `[1.9, 2.1]` with a margin of eleven orders of magnitude. **Theorem 3(b) — the beyond-wall
> load enters the terminal row at SECOND order in the last-bond stiffness — is now measured, not
> assumed.**
>
> **★ AND THE NUMBER WAS PREDICTED BEFORE IT WAS MEASURED, TO EVERY DIGIT.** The prereg §3.2 derived
> the expected exponent `2` with a predicted deviation of `3.39333930000000000000000000000e-13` from
> a closed form written down before any v2 code existed. The measured deviation is
> `3.39292560593418140000000000000e-13`. The plateau self-test was predicted the same way and landed
> the same way. **Nothing here was fitted.**
>
> **★ AND THE DIAGNOSIS WAS THE WHOLE FIX — v1's INSTRUMENT WAS NEVER WRONG.** Re-running the **v1
> siting** through the **v2 code path** returns `0.00370115115631918737071374823881` and both shipped
> per-pair values, **byte-exact**. The instrument did not change; the probe moved. The failure was a
> freeze-time sizing error and nothing else, exactly as the predecessor said.
>
> **★ AND THE GATE CAN STILL FAIL.** `FT-RHO2` re-sites the same code into the plateau, six to ten
> decades **above** the crossover, and the exponent collapses to
> `3.76991733993251474861640528204e-14` — outside `[1.9, 2.1]`, gate FAILS, self-test FIRES. **Same
> code, same tolerance, probe coordinate moved across `δ = 1`, opposite verdicts.** That is the
> two-regime structure of §2 confirmed by an independent second measurement, and it is why the PASS
> is a measurement rather than a construction.
>
> **★ AND NOTHING ELSE MOVED.** `20` gate/self-test blocks and `80` fields reproduce the v1 shipped
> renderings under **exact string equality**, with **`0` mismatches** — including `G-RHO2`'s own v1
> FAILING record, which reproduces as FAIL. All `4` predecessor artifacts are byte-identical to
> `c4fdced0`. **TASK 1 remains `SCAN-NOT-CERTIFIED` and was not touched. TASK 3 was not touched.
> `BIN-C-DISJOINT` was not revisited. No KB leaf, manuscript file, solidity or ledger row was
> edited.**

---

## §1 — THE REGIME DERIVATION (frozen in the prereg §2, before code)

With `u ≡ k_0/(jω)`, the predecessor's own two functions give the **exact** load-sensitivity of the
terminal residual at the two probe loads `Z_b ∈ {Z_1, 2Z_1}` v1 froze:

```
Δ ≡ (Γ+1)|_{Z_1} − (Γ+1)|_{2Z_1}  =  − 2u² / [ (2u + Z_1)(3u + 2Z_1) ]      [EXACT]

δ ≡ |u|/Z_1 = k_0/(ω Z_1)   ⇒   |Δ|(δ) = 2δ² / [ √(1+4δ²) · √(4+9δ²) ]
```

```
δ ≪ 1 :  |Δ| → δ²      ⇒  exponent → 2      THEOREM 3(b)'s ASYMPTOTIC REGIME
δ ≫ 1 :  |Δ| → 1/3     ⇒  exponent → 0      THE PLATEAU
```

**The crossover is `δ = 1`, i.e. `k_0 = ω·Z_1`.** At the gate's frozen operating point
(`S = 1e-9`, `p = 0.5`, `ℓ/r_sat = 6.0238983090250982e-19`, `ω/ω_C = 1e-19` — all read verbatim from
the v1 driver and unchanged):

| quantity | measured |
|---|---|
| `Z_1` | `0.0000316227766016837933199889354443` |
| `ω` | `0.166005458375979627083141716449` |
| `k_cold` | `1660054583.75979627083141716449` |
| **`k_0^cross = ω·Z_1`** | **`0.00000524955352488372143529667589330`** |
| the same crossover in v1's `ε·k_cold` parametrization | `3.16227766016837933199889354443e-15` |

**v1's three injections sat at `δ = ` `31622.7766016837933199889354443`,
`316.227766016837933199889354443`, `3.16227766016837933199889354443` — all ABOVE the crossover, on
the plateau.** The predecessor's diagnosis is confirmed by independent re-derivation, and its prose
value ("about five parts in a million") is `k_0^cross` to its stated precision.

---

## §2 — THE GATE TABLE (measured against frozen; nothing dropped, widened or re-defined)

**No frozen criterion was dropped, widened, or re-defined. The `G-RHO2` acceptance interval
`[1.9, 2.1]` is v1's, character for character.**

### §2.1 The re-sited gate and its self-test

| gate | frozen | siting | measured | verdict |
|---|---|---|---|---|
| **G-RHO2** ★ | fitted exponent of `\|dΓ/dZ_beyond\|` vs `k_0` in `[1.9, 2.1]` *(v1 wording, unchanged)* | `k_0 = ε·ω·Z_1`, `ε ∈ {1e-6, 1e-8, 1e-10}` — **6/8/10 decades BELOW crossover** | `1.99999999999966070743940658186` | **PASS** |
| **G-DET-V2** | two full runs, identical digest, byte-identical apart from `_runtime_sec` | — | digest `a69cf1c2e710a473` twice; diff empty apart from `_runtime_sec` | **PASS** |

| self-test | frozen firing condition | measured | fired? |
|---|---|---|---|
| **FT-RHO2** ★ | re-siting the SAME instrument into the plateau (`ε ∈ {1e+6, 1e+8, 1e+10}`) must drive the exponent OUTSIDE `[1.9, 2.1]` | `3.76991733993251474861640528204e-14` | **FIRES** |

**Per-pair exponents, gate arm:** `1.99999999999932148273054010982` and
`1.99999999999999993214827305390`.
**Per-pair exponents, plateau arm:** `7.53908077178785057102736367851e-14` and
`7.53908077178926205446885568154e-18`.
**Injected stiffnesses, gate arm:** `5.24955352488372143529667589330e-12`,
`5.24955352488372143529667589330e-14`, `5.24955352488372143529667589330e-16`.
**Measured `|Δ|`, gate arm:** `9.99999999996875000000010148437e-13`,
`9.99999999999999687500000000000e-17`, `9.99999999999999999968750000000e-21` — i.e. `|Δ| = δ²` to
the digit, which is the theorem stated as a number.

### §2.2 The declared DIAGNOSTIC (explicitly NOT a gate; certification does not ride on it)

| diagnostic | frozen prediction | measured | verdict |
|---|---|---|---|
| **D-RHO2-PRED** | `\|exponent − 2\| ≤ 1e-11`, predicted deviation `3.39333930000000000000000000000e-13` from prereg §3.2 | `3.39292560593418140000000000000e-13` | **AGREES** |

The predicted and measured deviations agree to four significant figures — the residual difference is
the rounding of the `0.6786` coefficient stated in the prereg, not a discrepancy in the algebra.

### §2.3 Scope split — RUN, N/A, UNRUN

| task | gates RUN by THIS lane | N/A by construction | UNRUN by omission | status after this lane |
|---|---|---|---|---|
| TASK 1 | **none** | — | **none** (G-SCAN, FT-SCAN are the predecessor's, **REPLAYED not re-run**, §3) | **`SCAN-NOT-CERTIFIED`** — unchanged, not touched |
| TASK 2 | G-RHO2, FT-RHO2, G-DET-V2 + the full v1 Task-2 set reproduced (§3) | — | **none** | **`ROW-CERTIFIED`** |
| TASK 3 | **none** (G-PREC, G-COND reproduced as controls only) | — | **none** | **CERTIFIED** — unchanged, not touched |

**`UNRUN ≠ PASSED`. No gate in this lane is UNRUN by omission.** `G-SCAN` and `FT-SCAN` are marked
**REPLAYED, not reproduced, and not re-run** — see §3, where that limit is declared rather than
discovered.

---

## §3 — NEGATIVE CONTROLS: the v1 record reproduces byte-exact, with ZERO mismatches

**Method:** the v2 driver **imports the v1 driver module unmodified** and calls its own
`run_task2()`, `run_task3()`, `build_gates()` and `build_self_tests()`. Every reproduced value is
compared to the shipped `last_bond_kernel_collapse_results.json` by **`==` on the rendered strings**
— exact string equality, not a numeric tolerance.

| control | frozen | measured | verdict |
|---|---|---|---|
| **NC-GATES+NC-FT** ★ | every field of every v1 gate and self-test reproduces the shipped rendering under exact string equality | `20` blocks, `80` fields compared, **`0` mismatches**; every `pass`/`fires` flag reproduces, including `G-RHO2` = FAIL and `G-SCAN` = FAIL | **PASS** |
| **NC-RHO2-V1** ★ | the v1 siting through the v2 code path reproduces the shipped failing exponent and both per-pair values, byte-exact | `0.00370115115631918737071374823881`; per-pair `0.000000753906665558065022906244826996` and `0.00740154840597281667640459023280` | **PASS** |
| **NC-ROWS** | `run_task2()` returns the shipped row count | `3360` = `3360` | **PASS** |
| **NC-BYTES** | each predecessor artifact's blob id equals its blob id at `c4fdced0` | `4` artifacts checked, **`0` modified** | **PASS** |

**ZERO-MISMATCH STATEMENT, stated plainly:** across `20` blocks and `80` fields of exact string
comparison, plus `3` further controls, **not one value differs from the v1 shipped record.**

**★ REPRODUCTION-CLASS LEDGER — declared at freeze so that no reproduction is over-claimed:**

- **RECOMPUTED** (`15`) — computed afresh from the frozen numerics by v1 code; the string equality is
  a real test: `G-BOND`, `G-ROW`, `G-RHO`, `G-COLD`, `G-UNIT`, `G-PLANE`, `G-PREC`, `G-COND`,
  `G-NC-ARITH`, `FT-BOND`, `FT-ROW`, `FT-RHO`, `FT-PLANE`, `FT-ARITH`, `FT-COND`.
- **FILE-READ** (`2`) — recomputed, but the input is a file read from the tree, so the reproduction
  also tests that those files have not drifted: `G-NC-SIGN`, `G-NC-ECHO`.
- **★ REPLAYED — NOT an independent reproduction** (`2`): `G-SCAN`, `FT-SCAN`. The v1 corpus scan is
  **tree-state-dependent by the predecessor's own §1.3** (its outputs live inside the scanned tree,
  and this lane adds three more files to it), so re-running it on this branch **cannot** reproduce
  the shipped numbers and its failure to do so would carry **no** information. The v2 driver replays
  the shipped `task1_scan` block instead of re-scanning. **The scan is NOT re-run, `G-SCAN` is NOT
  re-tested, TASK 1 remains `SCAN-NOT-CERTIFIED`, and those two entries are bookkeeping, not
  evidence.**

---

## §4 — WHAT THIS RESULT DOES AND DOES NOT SETTLE

**Settled:** TASK 2 of the last-bond lane certifies. Theorem 3(b) — that the beyond-wall load enters
the terminal row at **second** order in `k_0` — is now measured inside its own asymptotic domain,
with the domain derived, the probe sited with a stated `6`-decade minimum margin, and the gate's
falsifier demonstrated firing on the other side of the crossover.

**Not settled, and not touched:** TASK 1 remains `SCAN-NOT-CERTIFIED` and adjudicates no premise
bin; the ruling's routed premise is still unadjudicated. `FORK-3(b)` is untouched — note that
Theorem 3(a) (`G-RHO`, exact independence AT the limit, PASS at exactly zero in v1) is the load-
bearing one for the `ρ`-independence claim, and 3(b) is its off-limit companion; certifying 3(b)
adds no new licence to any `ρ`-independence statement beyond what 3(a) already carried. Nothing
observational. Nothing about `γ`/`G_c` VALUES. Nothing about Regime-IV interior physics.
`BIN-C-DISJOINT` is not revisited.

**★ THE PRINT-LANGUAGE CONSEQUENCE — RECORDED, NOT EXECUTED.** The question that motivated this
rerun — whether a `ROW-NOT-CERTIFIED` TASK 2 licensed a "mechanism confirmed" phrasing anywhere
downstream — **moots on this certification** and is **recorded for the propagation pass**. This lane
executes none of it: no KB leaf, no manuscript file, no solidity, no matrix row, no falsification
ledger and no docket other than its own fragment is edited here. **The predecessor's result doc is
not rewritten and not annotated** — the v1 record stands as the v1 record (Rule 12,
substitution-not-retraction: the v1 body is preserved intact; this is a new versioned document, not
an edit).

**Fence:** this lane produces no observable, no chord, no discriminator and no claim-id, and
headlines none.

---

## §5 — SVA v0.2 pilot case 8: per-row fill notes

The 11-row header was filled in the prereg §0 before any v2 code existed. Notes per row, for the
pilot log:

1. **SECTOR / OWNERSHIP** — *low cost, non-zero value.* Forced the explicit statement that `k_0` is a
   T2-shear transport coupling while `Z_beyond` is deliberately sector-unstated, which is exactly why
   the theorem is worth gating. Caught nothing; the predecessor had already done the work.
2. **REGIME / PHASE-STATE** — **★ this row IS the repair.** Writing "an asymptotic statement has a
   domain of validity" as a *phase-state declaration* is what converted a vague "the injections were
   too coarse" into a derivable crossover. **Highest-value row in this lane by a wide margin.**
3. **CIRCUIT STATEMENT** — moderate value. Restating the gate as "a shunt compliance in parallel with
   an arbitrary load, terminating a line" made the crossover condition `k_0 ≪ ω|Z_b|` read as an
   obvious impedance comparison rather than as an algebraic accident.
4. **PLANE & PROJECTION** — low cost. Fixed that this gate lives at PLANE-LB only and that PLANE-N0
   is `G-PLANE`'s object, preventing a plane-mixing error in the negative-control comparison.
5. **CONSTITUTIVE PROVENANCE** — **high value, and it is where referential integrity got enforced.**
   Tagging every operating-point parameter READ-VERBATIM-UNCHANGED and the repair itself as
   PREDECESSOR-NAMED made the one-thing-changed claim auditable instead of asserted.
6. **ENERGY LEDGER** — low value here but cheap. Its one real catch: naming that the injected
   `k_0 > 0` is reactive and does **not** open a port, so `|Γ| = 1` must survive the injection.
7. **CALIBRATABILITY** — moderate. Pushed the whole lane onto the single dimensionless coordinate
   `δ = k_0/(ωZ_1)`, after which "site the probe with a stated margin" became a one-line instruction
   and the margin became decades of `δ`.
8. **DISCRIMINATION CLASS** — **★ the tautology filter did real work.** It flagged the circularity
   risk head-on: a gate sited by the same algebra that predicts its passing is not a test. The
   response — freeze the predicted number, and declare disagreement a finding against this lane's own
   algebra (`D-RHO2-PRED`) — is a direct product of this row.
9. **CERTIFICATION PLAN** — high value. Forced the negative-control method to be **exact string
   equality on the shipped renderings** rather than a numeric tolerance, before any comparison ran.
10. **ADJUDICATION ROUTING** — **★ high value.** Forced "on certification, update NOTHING else" into
    the freeze, so the scope of the rerun could not creep at write-up time, and forced the
    print-language consequence to be RECORDED-not-EXECUTED explicitly.
11. **NUMERICAL CONDITIONING** — **★ high value, and it set a frozen parameter.** Naming the
    `log₁₀(2/δ)`-digit cancellation BEFORE choosing `ε` is what fixed the soft end of the probe range
    at `1e-10` rather than at some arbitrarily smaller number. **Both ends of the frozen `ε` set are
    set by a named quantity — the crossover above, the cancellation below — and neither by taste.**

**Pilot verdict:** rows 2, 11, 8, 10 and 5 carried the lane. Rows 1, 4 and 6 were cheap insurance
that caught nothing here. **No row was found unfillable, and none was filled with a placeholder.**
One structural note for whoever lands SVA v0.2 formally: a *rerun* lane wants a row-2 sub-prompt
along the lines of *"if this lane re-measures a prior null, state the domain of validity of the
statement being measured and where the prior measurement sat relative to it"* — that single question
would have caught the v1 sizing error at v1's own freeze.
