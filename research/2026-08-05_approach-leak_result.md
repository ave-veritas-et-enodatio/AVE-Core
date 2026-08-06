# The APPROACH LEAK — RESULT: `LEAK-NOT-CERTIFIED` on ONE gate, which is this lane's own freeze error and is diagnosed to the digit. **NO BIN IS ADJUDICATED.** The physics is shipped in full as a NOT-ADJUDICATED DIAGNOSTIC — and it says the mirror's leak is decided by a single exponent canon does not state, with a knife-edge at exactly `p = 2`

**Date:** 2026-08-05 · **Branch:** `research/approach-leak`
Prereg-file: research/2026-08-05_approach-leak_prereg-FROZEN.md
(link: [`2026-08-05_approach-leak_prereg-FROZEN.md`](2026-08-05_approach-leak_prereg-FROZEN.md))
**Prereg-commit:** `bdb8b4a4` — frozen and pushed **ALONE**, before any driver code existed and
before any number produced by this instrument existed.
**Driver:** [`research/drivers/approach_leak.py`](drivers/approach_leak.py) → [`research/drivers/approach_leak_results.json`](drivers/approach_leak_results.json)
(driver committed at `48076793`, **before any result JSON was committed**; the frozen-formula
exponent fix at `68e46379`).
**Number check:** [`research/drivers/approach_leak_number_check.py`](drivers/approach_leak_number_check.py) — gating via `make verify`, with a mutation receipt.
**Class:** DERIVATION result (research-doc; **mints no `clm-`/`def-`/`exp-`/`sup-`/`ilk-`;
propagates to no KB/manuscript leaf; changes no solidity; edits no falsification ledger**). Engine
`src/ave` **byte-untouched and never imported**.
**Provenance:** the approach-leak lane, the last open number under the channel-scoped
kernel-collapse ruling (`_orchestration/docket-entries/2026-08-05-ruling-kernel-collapse-rescope.md`).
**SVA pilot case 7.** Per-row pilot notes in §8. **Written against `origin/main` = `c4fdced0`.**

---

## REGIME HEADER (mandatory, restated at the point of reading)

**MODE** — small-signal AC, a **scattering problem at REAL drive frequency**, not an eigenvalue
problem. **REGIME** — sub-yield lossless-reactive on `r > r_sat`; the `A ≥ 1` interior is Regime IV
and **is not in the domain**. **PHASE-STATE** — cold lattice, Op14 ON as a static constitutive
grade, `A(r) = r_sat/r`, `A = 1` exactly at `r_sat`. **SECTOR** — incident wave is **shear
(T2-translational, `G`-bond)**; converted quantity is the **Cosserat micro-rotation, channel 4**;
the conversion operator is the `G_c` antisymmetric-strain bond and nothing else. **No port is
crossed and no loss word is used anywhere in this lane.**

---

## HEADLINE

> **★ CERTIFICATION, STATED FIRST AND WITHOUT SOFTENING. `LEAK-NOT-CERTIFIED`.**
> Nine of ten gates PASS; all six fireability self-tests FIRE. **`G-NC-SLAST` FAILS**, and the
> failure is **this lane's own freeze error, of exactly the class the SVA row-9 sub-clause names**
> — a tolerance sized against a wrong-in-kind error model. This lane's frozen consequence
> (prereg `§5.3`) is **global**: *"any RUN gate FAILS … ⇒ this lane reports `LEAK-NOT-CERTIFIED`,
> adjudicates NO bin, and routes to a successor with a new version number."* **It is honoured.
> NO BIN IS ADJUDICATED. Everything below §2 is a NOT-ADJUDICATED DIAGNOSTIC**, shipped in full
> so a successor inherits a measurement rather than a silence.
>
> **★ AND THE DIAGNOSTIC HAS A CLEAN STRUCTURE, WHICH IS THE REAL CONTENT.** The whole question
> collapses onto ONE number — the exponent `p` with which the rotational gap rides the strain
> kernel, `ω_m(r) = 2ω_C·S(r)^p` — and there is an **exact knife-edge at `p = 2`**, derived at
> freeze and confirmed by the instrument: **`p < 2` ⇒ no intact cell is ever open; `p > 2` ⇒ cells
> are open; `p = 2` ⇒ the verdict becomes MASS-INDEPENDENT** and is decided by the pure numbers
> `Ω` and `θ` alone. `G-KNIFE` measures the mass-spread of `S_open/S_1` at `p = 2` as
> `7.77877e-62` — zero to the working precision — against `1.88778e-17` for the exact-`S_1`
> variant, which is the `O(ℓ_node/r_sat)` truncation and nothing else.
>
> **★ AND `p` IS NOT IN CANON. TWO-METHOD ABSENCE RECEIPT, BOTH ENGINES NAMED.** `p = (a+b)/2`
> with `a` the `G_c(A)` exponent and `b` the `I_ω(A)` exponent. Patterns `P3` and `P4` return
> **ZERO hits on `git grep -P` and on Python `re` alike** across `4418` tracked files: **canon
> states no `I_ω(A)` grading law at all.** `P1`'s four hits are all statements of `G_c(A)`'s
> ABSENCE; `P2`'s only substantive hit is the ENGINE line itself,
> `cosserat_field_3d.py:767` — `(W_cauchy * G + W_micropolar * G_c) * S_eps_sq` — verbatim.
> **No pattern in the battery uses `\b`**, so the FLAG-UNIWB divergence is avoided by construction:
> the two methods agree on `5` of `5`.
>
> **★ THE DIAGNOSTIC VERDICT, MEMBER BY MEMBER, NOT COLLAPSED.** On the three below-knife members
> — including **both** the dispatch's stated `p = 1/2` **and** the engine's own coded `p = 1` —
> `N_open = 0` at **every one of the 6240 swept rows**, with margins of `24.3`–`28.5`, `8.06`–`9.74`
> and `2.63`–`3.47` orders of magnitude in `S` respectively. On `p = 2.5` and `p = 3` cells ARE
> open, by `485`–`3228` and `84316`–`881448` cells. **At `p = 2` the answer splits on the
> sub-cell regulator alone** — `N_open = 0` at `θ = 1` and `N_open = 1` at `θ = 0.5` — exactly as
> the frozen criterion `Ω < 4θ` predicts, with the band top at `Ω = 2.86091199398419774092281290729`.
>
> **★ THE LEAK BOUND AND THE BIN ARE THE SAME INEQUALITY, AND THAT WAS DERIVED AT FREEZE.**
> `ζ_max = (S_open/S_1)^{2p}/|1−(S_open/S_1)^{2p}|`, so *no-open-cell* ⟺ `ζ_max < 1`. `G-ZID`
> confirms the two independent evaluations of `ζ_max` agree to `2.77978e-59`. At the engine's own
> `p = 1` the entire evanescent admixture on the whole approach is
> `ζ_max = 7.64219872765688277388060621827e-17` — **a dimensionless amplitude ratio carrying no
> absolute modulus**, because the same `G_c` sets both the drive strength and the gap.
>
> **★ AND THE ZERO-TRANSPORTED-POWER STATEMENT IS A THEOREM WITH A MEASURED INPUT, NOT AN
> ASSERTION.** `G-REAL` measures `min(ω_m² − ω²)` over every closed row at
> `1.13450335861760625511643046057e-38` in `ω_C²` units — **strictly positive**, so the transfer
> function is REAL, the rotational branch supplies no radiation resistance, and
> `⟨P⟩_period = 0` **exactly**. On the closed members the admixture is a reactive store on the
> Axiom-3 rim; no port is crossed.
>
> **⚑ AND THE FLAG THE DISPATCH ITSELF REQUIRES. The dispatch's stated expectation names the
> wrong exponent.** It states *"gap² = 4G_c·S_ε/I_ω ⇒ gap ∝ √S_ε"* (`a = 1`, `p = 1/2`). The
> engine multiplies `W_micropolar * G_c` by `S_eps_sq`, and `cosserat_field_3d.py:761` defines
> `S_eps_sq = jnp.clip(1.0 - eps_sq / epsilon_yield**2, 0.0, 1.0)` — which **is `S_ε²`, not
> `S_ε`** — so the engine's own coding gives `gap ∝ S_ε`, i.e. `p = 1`. **Declared at freeze
> (FLAG-EXP), not discovered after.** The expectation's *verdict* survives on both readings
> (§4.1); its *arithmetic* does not.

---

## §1 — THE GATE TABLES (measured against frozen; nothing dropped, widened or re-defined)

**Frozen:** `No gate, tolerance, bin boundary, frozen numeric parameter,`
`pattern-battery entry, verdict wording or method element of §2–§8 may be changed after any result`

**No frozen criterion was dropped, widened, or re-defined.**

### §1.1 The gates

| gate | frozen tolerance | measured | verdict |
|---|---|---|---|
| **G-CANON** | `1e-40` on three canonical identities | `0.0` / `0.0` / `0.0` — all three exactly | **PASS** |
| **G-NC-BAND** ★ | band endpoints read PROGRAMMATICALLY from the v2.4 shipped JSON | `[0.846398427697559955718585408169, 2.86091199398419774092281290729]` | **PASS** |
| **G-NC-SLAST** ✗ | `1e-40` rel vs the predecessor's shipped `S_last` | `2.04408e-17` | **FAIL** |
| **G-COND** | naive float64 `1−A²` returns exactly `0.0`; cancellation-free `S² > 0` | `0.0` and `1.20477966180501968816480560865e-18` | **PASS** |
| **G-COUNT** ★ | `N_open` closed-form == direct count, every row, exact integers | `0` mismatches over `6240` rows | **PASS** |
| **G-ZID** ★ | `1e-45` rel between the two `ζ_max` evaluations | `2.77978e-59` | **PASS** |
| **G-REAL** ★ | `ω_m² − ω² > 0` strictly at every closed row; MINIMUM reported | `1.13450335861760625511643046057e-38` | **PASS** |
| **G-KNIFE** ★ | mass-spread of `S_open/S_1` at `p = 2` below `1e-45` | `7.77877e-62` | **PASS** |
| **G-SUM** | `1e-30` rel, summation-plus-tail vs `polygamma(1,θ)` | `0.0` exactly | **PASS** |
| **G-SCAN** | METHOD A and METHOD B hit sets identical per pattern | identical on `5` of `5`, over `4418` files | **PASS** |
| **G-DET** ★ | two full runs, identical digest, byte-identical apart from `_runtime_sec` | digest `2af8acfe23aabb96` twice; bodies identical | **PASS** |

### §1.2 The fireability self-tests (each MUST fire; a gate that cannot fail is not a gate)

| self-test | measured | fired? |
|---|---|---|
| **FT-COUNT** | drive × `1e30` ⇒ `N_open` = `UNBOUNDED (S_open ≥ 1)` | **FIRES** |
| **FT-ZID** | perturbing `ζ_max` by `1e-40` rel ⇒ separation `1.00000e-40` ≫ `1e-45` | **FIRES** |
| **FT-REAL** | injecting `p = 12` ⇒ `ω_m² − ω² = -1.24685e-36`, NEGATIVE | **FIRES** |
| **FT-KNIFE** ★ | spreads `0.00711997` (`p=1.99`) and `0.00861869` (`p=2.01`), both non-zero, mass-trends `-1.00` and `+1.00` — **OPPOSITE** | **FIRES** |
| **FT-COND** | naive float64 returns exactly `0.0` | **FIRES** |
| **FT-SCAN** | absent sentinel `0`/`0`; present sentinel `54`/`54`, identical sets | **FIRES** |

**`FT-KNIFE` is the load-bearing self-test** and it does the job it was frozen for: the mass-trend
of `S_open/S_1` **reverses sign** across `p = 2`, so `G-KNIFE`'s zero is a genuine knife-edge and
not a coincidence of the mass grid.

### §1.3 The failure, diagnosed exactly — and it is this lane's own freeze error

**`G-NC-SLAST` — a tolerance sized against a wrong-in-kind error model.** The gate demands this
lane's `S_1` reproduce the predecessor's shipped `S_last` to `1e-40` relative. Measured:
`2.04408e-17`. The two values are

```
predecessor (shipped)  0.00000000109762455411903921151585733431
this lane              0.00000000109762455411903923395222956603
```

— **agreement to 17 significant digits, separating at float64-epsilon scale.** The cause is
arithmetic and complete: the predecessor's ladder rung is the float64 literal
`6.0238983090250982e-19` (a 17-significant-figure `repr`), and its exact-`mp` `S_last` was
**seeded from that rung**; this lane derives `ℓ_node/r_sat` from `M = 62 M_⊙` at `dps = 60` and
obtains `6.02389830902509844626713066887e-19`, a relative separation of `4.08817e-17`.
**No `mp`-precision reproduction of a float64-seeded rung is possible**, so `1e-40` could never
have been met by a correct instrument. The error model was wrong in kind: it was sized against
round-off when the actual limiting error is *the predecessor's input precision*.

**This is the SVA row-9 sub-clause's own named failure mode** — *"derived gate constants get a
pre-freeze second-method check … mechanism identified: novel-quantity tolerances from wrong-in-kind
error models"* — **reproduced on a lane that quotes it.** The tolerance is **NOT retuned**, the
gate FAILS, and the frozen global consequence is honoured.

**Repair, named and routed to the successor:** gate the reproduction at the precision the
predecessor SHIPPED its input at — `1e-16` relative — or, better, reproduce the predecessor's
`S_last` from *its own* rung value rather than from the mass, which makes the comparison
precision-exact.

### §1.4 Two implementation infidelities found and repaired BEFORE the driver was committed

Reported because a successor should know what the first run did.

1. **`N_open`'s direct count carried a `cap = 4096`** that was not a frozen parameter and that
   manufactured `520` false mismatches on the above-knife members. Repaired to an exact count with
   no cap, via exponential search plus bisection on the **proven-monotone** predicate `S_n ≤ S_open`
   (`S_n² = 1 − (r_sat/(r_sat+x_n))²` is strictly increasing), which returns the identical integer
   a linear scan would. **DISCLOSED as the one liberty against the frozen phrase "direct
   node-by-node count"**, and cross-checked against an actual linear scan on every row within
   `LINEAR_BUDGET = 4096` — which includes **every** closed row. `1040` rows (the `p = 2.5` and
   `p = 3` members) exceed the budget and carry the bisection result only.
2. **`G-KNIFE` mixed the exact `S_1` with the near-wall `S_open`.** The frozen §2.1 writes the
   last-cell floor with an arrow, `S_1 → sqrt(2θ ℓ_node/r_sat)`, and §2.4's knife-edge derivation
   is explicitly an `x → 0` argument, so the faithful evaluation uses the near-wall form on both
   sides. Repaired; the exact-`S_1` variant is shipped **beside** it as a non-gated diagnostic at
   `1.88778e-17`, which is the `O(ℓ_node/r_sat)` truncation and is largest at the smallest mass.
   **This is a fidelity repair, not a retune: the tolerance is untouched.**

### §1.5 Scope split — RUN, N/A, UNRUN

| scope | gates RUN | N/A by construction | UNRUN by omission |
|---|---|---|---|
| canon receipts | G-CANON, G-NC-BAND, G-NC-SLAST, G-SCAN, FT-SCAN | — | **none** |
| conditioning | G-COND, G-SUM, FT-COND | — | **none** |
| the sweep | G-COUNT, G-ZID, G-REAL, G-KNIFE, FT-COUNT, FT-ZID, FT-REAL, FT-KNIFE | — | **none** |
| reproducibility | G-DET | — | **none** |

**Frozen:** `UNRUN ≠ PASSED`. **No gate in this lane is UNRUN by omission.**

---

## §2 — ★ READ THIS ROW FIRST: EVERYTHING BELOW IS A NOT-ADJUDICATED DIAGNOSTIC

> **`LEAK-NOT-CERTIFIED` (§1.3). NO BIN IS ADJUDICATED.** Everything in §3 onward is shipped so a
> successor inherits a measurement rather than a silence, exactly as the last-bond and echo-delay
> lanes shipped theirs. **No sentence of §3–§7 may be quoted as a bin outcome.** Every cite below
> was verified at ship tip; the scan receipts are two-method with both engines named.
>
> The frozen bins — `GAP-CLOSED` / `CHANNEL-OPENS` / `SCALE-UNDERDETERMINED` /
> `UNDERDETERMINED-CANON` — are **not** awarded here. Where the diagnostic *points*, it is said
> plainly and labelled as pointing.

---

## §3 — THE STRUCTURE OF THE ANSWER: ONE EXPONENT, ONE KNIFE-EDGE

The rotational branch is gapped in the cold medium at `ω_m = 2ω_C` (A-008-pinned;
`cosserat-mass-gap.md`:59 for the form, `2026-08-05_a008-factor-propagation_note.md` §3.3 for the
scale and for the RULED ratio `G_c/I_ω = ω_C²`). Grading both moduli,

```
omega_m(r) = 2 omega_C S(r)^p ,     p == (a + b)/2 ,
   a = the G_c(A) exponent ,  b = the I_omega(A) exponent
```

The drive falls to the local gap at `S_open = (Ω x/2)^{1/p}` with `x ≡ ℓ_node/r_sat`; the innermost
intact cell sits at `S_1 → sqrt(2θ x)`. **No intact cell is open ⟺ `S_open < S_1` ⟺**

```
(Omega x / 2)^(1/p)  <  sqrt(2 theta x)
```

Both sides vanish as `x → 0`, the left as `x^{1/p}` and the right as `x^{1/2}`. **The competition
is between two powers of the same small number, and it turns over at exactly `p = 2`:**

| `p` | which side wins as `x → 0` | consequence |
|---|---|---|
| `p < 2` | left vanishes FASTER | no cell open; margin GROWS without bound as the mass grows |
| `p = 2` | the `x`-dependence CANCELS EXACTLY | **verdict is MASS-INDEPENDENT**, decided by `Ω < 4θ` alone |
| `p > 2` | right vanishes faster | cells open; the count grows with the mass |

**Measured confirmation.** `G-KNIFE` puts the mass-spread of `S_open/S_1` at `p = 2` at
`7.77877e-62` across a `100×` mass lever, against the closed form
`sqrt(Ω/4θ) = 0.680745035024288452636004066119` at band centre. `FT-KNIFE` shows the mass-trend
**reversing sign** between `p = 1.99` (`-1.00`) and `p = 2.01` (`+1.00`). **The knife-edge is real
and it is at `2`.**

### §3.1 — `p` IS NOT IN CANON — the two-method absence receipts, engines named

**METHOD A = `git grep -P` (PCRE, ASCII `\w`). METHOD B = Python `re` on `str` (Unicode `\w`).**
Scan surface = `git ls-files` over `manuscript/`, `research/`, `src/` = `4418` tracked files, with
this lane's own six artifacts excluded **by construction**. **No pattern uses `\b`**, so the
FLAG-UNIWB PCRE-vs-Unicode divergence cannot arise; the two methods agree on `5` of `5`.

| id | target | A | B | agree | verdict |
|---|---|---|---|---|---|
| `P1` | `G_c(A)` written as a function | `4` | `4` | ✅ | **all four hits are statements of its ABSENCE** |
| `P2` | `G_c` × a kernel | `4` | `4` | ✅ | **the only substantive hit is the ENGINE line itself** |
| `P3` | `I_ω(A)` written as a function | `0` | `0` | ✅ | **ABSENCE RECEIPT** |
| `P4` | `I_ω` / micro-inertia riding a kernel | `0` | `0` | ✅ | **ABSENCE RECEIPT** |
| `P5` | a **rotational** band top | `5` | `5` | ✅ | **all five are the vector/Cosserat-TRANSLATIONAL bracket** |

Every hit, quoted:

- `P1` — `last-bond…_prereg-FROZEN.md`:24 (*"`γ(A)` and `G_c(A)` grading laws: THE OBJECT OF TASK 1
  — provenance UNDETERMINED at freeze"*); `last-bond…_result.md`:117 (*"**NO GRADING LAW STATED.**
  … states no `G_c(A)`"*); `:172` (*"A grading law for `G_c(A)` — none stated."*); `:522` (the SVA
  row-5 pilot note). **Not one is a law.**
- `P2` — `cosserat_field_3d.py`:767, verbatim `(W_cauchy * G + W_micropolar * G_c) * S_eps_sq`, and
  its archived transcription at `research/_archive/L3_electron_soliton/75_cosserat_energy_conservation_violation.md`:30;
  plus `2026-07-14_tij-x44b_CHARTER.md`:74 (noting the saturated form is the live one) and the same
  absence statement. **The engine's `a = 2` is confirmed verbatim; no canon leaf carries it.**
- `P5` — `program-arc-map.md`:233 and `:386`, `x43-ringdown-port_result.md`:48 and `:62`,
  `echo-delay-regulated-sum_prereg-FROZEN.md`:50 — **every one is the vector /
  Cosserat-TRANSLATIONAL band top `[5.4414, 17.0111] ω_C`**, which is the SHEAR channel.
  **No micro-rotation band top exists in canon**, exactly as
  `srs-band-structure.md`:118 says: the true photon is *"the **T2 Cosserat MICROROTATION**, a
  **named follow-on** not surveyed at this Cauchy-translational level."*

**So `p` rests on: an engine coding choice for `a` (`= 2`) that canon has never ratified, and an
`I_ω(A)` law that does not exist anywhere.** That is the whole uncertainty, and it is enumerated
rather than papered over.

---

## §4 — THE MEASUREMENT, MEMBER BY MEMBER (NOT collapsed)

`6240` rows = `4` masses × `2` `θ` × `65` band points × `6` `p` × `2` `ρ`-branches. Band read
programmatically from the v2.4 shipped JSON: `Ω ∈ [0.846398427697559955718585408169,
2.86091199398419774092281290729]`.

| `p` | provenance of the member | `N_open` over the sweep | `log10(S_1/S_open)` | `ζ_max` | points to |
|---|---|---|---|---|---|
| `0.5` | **the DISPATCH's stated expectation** (`a=1, b=0`) | `{0}` | `24.33` – `28.54` | `4.67038827711388070441696359081e-25` | no cell open |
| `1.0` | **the ENGINE's coded `a=2`**, `I_ω` ungraded as canon's Lagrangian writes it | `{0}` | `8.058` – `9.738` | `7.64219872765688277388060621827e-17` | no cell open |
| `1.5` | filler, so the below-knife arm is not two-point | `{0}` | `2.634` – `3.471` | `0.0000000125049992972797073610801916705` | no cell open |
| `2.0` | `a=1` with the RHO-B **ANALOGY** for `I_ω` — **ANALOGY, NOT CANON** | `{0, 1}` | `-0.0777` – `+0.337` | `91.3379208100579910158046584733` | **splits on `θ` alone** |
| `2.5` | the engine's `a=2` with the RHO-B **ANALOGY** — **ANALOGY, NOT CANON** | `485` … `3228` | `-1.905` – `-1.343` | `1.00000019302787476201778887731` | cells open |
| `3.0` | loosest member | `84316` … `881448` | `-3.123` – `-2.463` | `1.00000000000000166828253699831` | cells open |

**The `p = 2` split is the frozen criterion firing, not noise.** `Ω < 4θ` gives `N_open = 0` for
every `Ω` at `θ = 1` (since the band top `2.861 < 4`) and `N_open = 1` for `Ω > 2` at `θ = 0.5`
(since `4θ = 2`). The corner rows confirm it: at `M_ref`, `θ = 1`, band top, `p = 2`,
`N_open = 0` with `log10(S_1/S_open) = 0.0727777464388912982052857703942` — closed by a factor of
`1.18` in `S`, the thinnest non-negative margin anywhere in the sweep.

### §4.1 — The dispatch's stated expectation, adjudicated against its own numbers

The dispatch predicted **`GAP-CLOSED`** with *"even at the last node (`S_ε ~ 1e-9`-class) the local
gap should still sit many orders above the drive"*, on the arithmetic `gap ∝ √S_ε`.

- **`S_ε ~ 1e-9`-class at the last node: CONFIRMED.** `S_1 = 0.00000000109762455411903923395222956603` at
  `M_ref`, `θ = 1` — `1.0976e-9`.
- **The exponent: REFUTED as stated.** `gap ∝ √S_ε` is `p = 1/2`; the engine codes
  `G_c·S_eps_sq = G_c·S_ε²`, giving `gap ∝ S_ε`, `p = 1` (FLAG-EXP, declared at freeze).
- **The verdict: HELD on both readings, and on the third below-knife member too.** At `p = 1/2` the
  margin is `24.3`–`28.5` orders in `S`; at `p = 1` it is `8.06`–`9.74` orders. **The dispatch's
  "many orders" is right; its "~20 orders" reading of the frequency margin corresponds to the
  `p = 1/2` arm, and the engine's own arm gives roughly nine.**
- **What the expectation did not anticipate, and what the instrument found:** the verdict is *not*
  robust to the exponent. It **turns over at `p = 2`**, and one un-stated-but-plausible member —
  the engine's `a = 2` combined with the RHO-B `1/S³` grading applied by ANALOGY to the
  micro-inertia — lands at `p = 2.5` and **opens `485`–`3228` cells**. **The expectation is
  therefore CONFIRMED on every member canon or the engine actually states, and NOT ROBUST to a
  grading law nobody has written down.** That is the honest shape of it.

### §4.2 — The `ρ`-branch is an exact spectator, and it was MEASURED not asserted

The frozen sweep counts a `ρ`-branch factor. The rotational gap is built from `G_c`, `I_ω` and `S`
alone — the translational density enters the SHEAR impedance and speed, never the rotational
cutoff — so `RHO-A` and `RHO-B` must be exactly degenerate here. **Measured max separation across
the branch pair, over all `3120` physical rows: `0.0`.** Reported as a non-gated diagnostic
(`G-RHO-SPECTATOR`) because it was not a frozen gate, and reported at all because the freeze's
row-count would otherwise silently double-count a spectator.

---

## §5 — THE EVANESCENT PICTURE, ON THE MEMBERS WHERE NO CELL IS OPEN

### §5.1 — The leak bound `ζ_max`, and its identity with the verdict

From the `G_c` bond's own equation of motion (prereg §1.2, derived not asserted),

```
d2(omega_z)/dt2 + omega_m^2 omega_z = omega_m^2 A_z        [a driven tank whose resonance IS the gap]
zeta == |eps^A|/|A_z| = (omega/omega_m)^2 / |1 - (omega/omega_m)^2|
```

`ζ` is the fraction of the shear wave's own macro-rotation that appears as **relative**
micro-rotation — the only part that engages the `G_c` bond at all. Below the gap the micro-rotation
is **slaved** to the macro-rotation, the mutual element sees no differential, and nothing is tapped.

**`G-ZID` confirms the two independent evaluations agree to `2.77978e-59`**, so the frozen identity

```
zeta_max = u/|1-u| ,  u = (S_open/S_1)^(2p)      =>      no cell open  <=>  zeta_max < 1
```

holds numerically. **The bin and the leak bound are one inequality, and `ζ_max` is exactly how far
below unity it sits.** At the engine's own `p = 1`, `ζ_max = 7.64219872765688277388060621827e-17`
over the whole sweep, and `6.16306349004587257048169509438e-19` at the reference corner
(`M_ref`, `θ = 1`, band top). **This is a pure dimensionless amplitude ratio: no absolute modulus
appears, because the same `G_c` sets both the drive strength and the gap.**

### §5.2 — Decay depth of the converted near-field, in cells, at both ends

Below the gap `k = iκ` with `κ = sqrt(ω_m² − ω²)/c_R → ω_m(r)/c_R`, and with the Grant-ratified
`c_R = √2 c₀` (`cosserat-mass-gap.md`:104),

```
d_cells = 1 / (sqrt(2) * S^p)
```

| where | `p = 0.5` | `p = 1` | `p = 1.5` |
|---|---|---|---|
| far field (`S → 1`) | `0.707…` cells | `0.707…` cells | `0.707…` cells |
| last intact cell (`M_ref`, `θ = 1`) | `21343.1292944158822220036001696` | `644215527.552657683622522671906` | `19444835863339.4637566615788096` |

**In the cold far field the converted rotational near-field does not span one cell.** At the last
intact cell it spreads over `6.4e8` cells at `p = 1` — which is `2.5e-4` m against
`r_sat = 6.4e5` m, i.e. still nine orders below the wall radius. The near-field is **local to the
approach and never reaches anywhere**.

### §5.3 — Why no time-averaged power transports (the energy-ledger row, proved with a measured input)

`G-REAL` measures `min(ω_m² − ω²)` over every closed row at
`1.13450335861760625511643046057e-38` in `ω_C²` units — **strictly positive everywhere**.
Therefore the transfer function `ω_z/A_z = ω_m²/(ω_m² − ω²)` is **REAL**; the gapped branch offers
**no propagating state at the drive frequency**, hence no radiation resistance, hence no imaginary
part. With `A_z ∝ cos ωt` the relative rotation is `∝ cos ωt` and `dω_z/dt ∝ −sin ωt`, so

```
<P>_period = <4 G_c (A_z - omega_z) d(omega_z)/dt>  =  0    EXACTLY
```

**No port is crossed.** The admixture is a reactive store on the Axiom-3 rim: it is cycled, not
delivered. The theorem's one empirical input is the SIGN of `ω_m² − ω²`, and the magnitude of the
minimum is reported rather than merely its sign, as the freeze requires.

### §5.4 — The residual observable, named — and QUARANTINED

The stored relative-rotation energy per cell against the shear energy is `2(G_c/G)ζ_n²`, with
`ζ_n = ζ_max(θ/(n−1+θ))^p`. Summed over the graded region (prereg §2.6, exponent `2p`):

| `p` | `Σ_n ζ_n²` at `M_ref`, `θ = 1`, band top | convergent? |
|---|---|---|
| `0.5` | `1.94626690700324501270290500488e-53` | **NO** — harmonic; the finite-window value over `N = r_sat/ℓ_node = 1660054583759796203` cells is reported |
| `1.0` | `6.24801089908586496601693316163e-37` | yes (`ψ'(1) = 1.64493406684822643647241516665`; second-method check `0.0` exactly) |
| `1.5` | `3.78975106182925705852355862445e-19` | yes |

**The residual phase perturbation on the reflected shear echo is `2(G_c/G)` times these numbers.**
At the engine's `p = 1` that is of order `1e-36` radians against the `≈ 27` radians of accumulated
round-trip phase the echo-delay lanes carry — **it would not perturb the certified delay at any
digit that instrument reports.** Declared **NIL as an observable**.

> ⚑ **`SCALE-UNDERDETERMINED` POINTS HERE, AND ONLY HERE.** The prefactor `2(G_c/G)` rides an
> **absolute-modulus ratio** which is an engine placeholder — A-008 pins `G_c/I_ω`, not `G_c/G`.
> Every other number in this lane is ratio-only: `N_open` is an integer, `ζ_max` is a dimensionless
> amplitude ratio, and the gap-margin arithmetic is a competition between two powers of
> `ℓ_node/r_sat`. **The magnitude of the residual field is placeholder-conditioned; the FORM and
> the margin are not.** (SVA row 7 satisfied by quarantine, as frozen.)

---

## §6 — CONSEQUENCE DOCUMENTATION (no claims minted; **no bin adjudicated**, so these are CONDITIONALS)

**Frozen fence:** this lane adjudicates nothing. The statements below say what EACH bin *would* do,
so the orchestrator can route without re-deriving. They are conditionals, not outcomes.

### §6.1 — What each bin would do to the ruling's leak clause

The ruled text, verbatim
(`_orchestration/docket-entries/2026-08-05-ruling-kernel-collapse-rescope.md`:18):

> *"Shear→rotation conversion cannot occur at the wall (the door closes with the strain kernel) and
> is confined to the graded approach where `G_c·S_ε` is finite — the leak is one computable number
> (a coupled two-channel scattering computation, routed as the approach-leak lane)."*

| bin (if adjudicated) | effect on the leak clause |
|---|---|
| `GAP-CLOSED` | the clause's *"confined to the graded approach"* stands, and gains a **quantitative closure**: the confinement is not merely spatial but **spectral** — there is no propagating rotational state at the drive frequency at ANY radius on the approach, so the "leak" is a purely reactive admixture bounded by `ζ_max` and transporting **exactly zero** time-averaged power. The mirror is TOTAL at ringdown frequencies. **"One computable number" would be answered: `ζ_max`, and it is `< 1e-16` on every member canon or the engine states.** |
| `CHANNEL-OPENS` | the clause would need a **second sentence**: conversion is confined to the approach *and* the approach contains a thin shell of open rotational states whose width is `N_open` cells, through which a coupled two-channel transfer must be computed. The mirror would be **total for the strain-kernel channels but not for the composite**, and Regime IV's fence would not be the only thing bounding the answer. |
| `SCALE-UNDERDETERMINED` | co-fires on the residual back-action field ONLY (§5.4). It does not touch the leak clause: the clause is about whether conversion occurs, and that is decided by ratio-only quantities. |
| `UNDERDETERMINED-CANON` | co-fires. The clause's *"the leak is one computable number"* would have to read *"one computable number **given a grading law for `G_c(A)` and `I_ω(A)`**"* — and canon states neither. |

**Where the diagnostic points, said plainly:** toward **`GAP-CLOSED` co-firing with
`UNDERDETERMINED-CANON`**, because every member canon or the engine actually states sits below the
knife-edge, and the members that open it require an `I_ω(A)` law that appears nowhere in the corpus.
**That is a pointing, not an adjudication.** A successor with correctly-sized tolerances awards it.

### §6.2 — Effect on the ROUTED rotational-penetration frontier item (one line, as fenced)

The ruling's routed walk-level item — *"the rotational channel behaves at `r_sat` like a penetrating
radiation"* — concerns a **cold-medium rotational wave at `ω ≥ 1.022` MeV** crossing the surface.
**That is a different frequency regime by roughly eighteen orders of magnitude from this lane's
ringdown band, and MeV-scale rotational radiation is OUT OF SCOPE here.** Cross-reference only:
this lane's `p` is the *same* exponent that frontier item's "gains headroom on approach" depends on,
so whoever scopes it inherits §3.1's absence receipts rather than needing to re-derive them.

---

## §7 — FLAGS (verbatim; flag-don't-fix — none silently resolved)

### FLAG-EXP — the dispatch's stated exponent disagrees with the engine's coding

**Declared at freeze** (prereg §1.3), not discovered after. Dispatch: *"gap² = 4G_c·S_ε/I_ω ⇒
gap ∝ √S_ε"*. Engine, `src/ave/topological/cosserat_field_3d.py`:761 verbatim:

```
S_eps_sq = jnp.clip(1.0 - eps_sq / epsilon_yield**2, 0.0, 1.0)
```

and `:767` verbatim:

```
(W_cauchy * G + W_micropolar * G_c) * S_eps_sq
```

`S_eps_sq` **is `S_ε²`**, so the engine's effective coupling is `G_c·S_ε²` and the engine's gap is
`∝ S_ε`, i.e. `p = 1`, not `p = 1/2`. **Both are run; the pointing is unchanged; the arithmetic is
not.** Not fixed here — the dispatch's expectation is quoted, not edited.

### FLAG-IOMEGA — the exponent that decides the answer does not exist in canon

Two-method absence receipt, both engines named, `4418` files, `0` hits on `P3` and `P4`: **canon
states no `I_ω(A)` grading law.** Yet the verdict turns over at `p = 2`, and `b = 3` (the RHO-B
`1/S³` grading applied by ANALOGY to the micro-inertia) is enough to push the engine's own `a = 2`
above the knife-edge. **This is a NEW canon gap, distinct from the five the last-bond lane
enumerated** (`2026-08-05_last-bond-kernel-collapse_result.md`:163-179, which lists the `G_c(A)`
law but not the `I_ω(A)` one). **Minted as a question, not filled with a default.** ROUTED.

### FLAG-MECH — the predecessor's §2.3 precision note names the mechanism for ONE fork member only

`2026-08-05_last-bond-kernel-collapse_result.md`:194-201, verbatim:

> *"It is a **BAND COLLAPSE, not a gap opening.** … If the curvature stiffness `γ` rides the same
> factor, the whole rotational dispersion `ω² = (2γ/I_ω)k² + 4G_c/I_ω` scales by it and **every**
> rotational frequency — band bottom and band top together — is driven to zero. A fixed finite
> drive frequency then finds no state because it is **above the local band top**, not because it is
> below a gap."*

**That mechanism is the normalized-L2 member.** Under the L∞ member — *"the wall is whichever grade
reaches `S→0` first"*, **which the same result records as the member the engine actually codes**
(`:152-155`) — `γ` rides `S_κ`, a **different kernel with a different argument**
(`cosserat_field_3d.py`:762 vs `:761`), and `S_κ` is untouched by a static strain grading. On that
member the band TOP does not descend and **the drive finds no state because it IS below a gap** —
the opposite mechanism, reaching the same conclusion. The predecessor's clause is conditional
(*"If …"*) and so is not wrong; but **quoted without its antecedent it names the wrong mechanism for
the member the engine codes.** Surfaced, not fixed; the predecessor's file is byte-untouched.

### FLAG-ROTTOP — there is no rotational band top in canon, and the corpus's five near-hits are all the SHEAR channel

`P5`'s five hits are all the vector / Cosserat-**translational** bracket `[5.4414, 17.0111] ω_C`.
`srs-band-structure.md`:118 says so in as many words: the true photon is *"the **T2 Cosserat
MICROROTATION**, a **named follow-on** not surveyed at this Cauchy-translational level."* This lane
therefore **brackets** the rotational top at three declared members and chooses none —
`T1 = 2√(π²+1) = 6.5938166189512303175 ω_C` (continuum-dispersion extrapolation to the srs Nyquist
wavevector, with the Grant-ratified `c_R = √2 c₀`), `T2 = 5.4414`, `T3 = 17.0111`. **On every
below-knife member the bracket is MOOT** — the drive never reaches the band at all, so its top is
never consulted — **and that is reported as moot rather than silently dropped**, as the freeze
requires. It becomes load-bearing only in the `CHANNEL-OPENS` arm.

### FLAG-FREEZE — this lane's own freeze error, and its exact class

`G-NC-SLAST`'s `1e-40` was sized against a round-off error model when the limiting error is the
predecessor's float64-seeded input precision. **Wrong-in-kind, which is the exact mechanism the SVA
row-9 sub-clause names**, and it is the *fourth* consecutive occurrence of that class the arc has
logged. **Two contributing structural facts, both reported:** (i) the predecessor ships some fields
at 30 `mp` digits and others at float64 `repr`, and nothing in the JSON marks which is which; (ii)
this lane's own §5.2 pre-freeze second-method check covered `p_crit`, `ζ_max` and the `ψ'` sum — it
did **not** cover the negative-control tolerances, which is precisely where the error landed.
**Repair for the successor: extend the pre-freeze second-method check to NEGATIVE-CONTROL
tolerances, and gate a reproduction at the precision the source SHIPPED, not at the precision the
consumer computes in.** ROUTED as a candidate SVA row-9 amendment; **not drafted here** (the auditor
lands SVA amendments).

---

## §8 — SVA v0.2-pilot, per-row fill notes (pilot case 7)

| row | fill | note |
|---|---|---|
| **1 · Sector / ownership** | FILLED | **High value.** Naming channel 4 as the *converted* quantity and `G_c` as the *only* conversion operator is what kept the lane off the mass sector; `cosserat-mass-gap.md`:149's Rule-12 re-scope (the gap is the **flywheel clock gap**, not the rest-mass store) had to be quoted in the header or the lane would have read a 1.022 MeV number as a mass. |
| **2 · Regime / phase-state** | FILLED | Standard. The one thing it forced: declaring the DRIVE small and the BIAS large, so the bias is carried exactly and never linearized — which is why the `S_n` form is exact and not a series. |
| **3 · Circuit statement** | FILLED | **High value.** "Ladder 2 is a cutoff line; a tap into a cutoff line is a reactive stub" is the whole physics in one sentence, and it was written before any framework word. The **total-vs-slot** declaration (measure `ε^A = A_macro − ω_micro`, not the two rotations separately) is what made `ζ` the right observable. |
| **4 · Plane & projection** | FILLED | **Unusual fill: the row was satisfied by declaring NO Γ and NO Z.** Reporting only an amplitude ratio and an integer count made the lane plane-invariant by construction and inherited no sign convention — which is a *stronger* fill than picking a plane. Suggests the row could name "declare the observable plane-invariant" as an explicit third option. |
| **5 · Constitutive provenance** | FILLED | **The load-bearing row again.** Tagging `a` and `b` as `UNDETERMINED-CANON` **at freeze** is the only reason the engine's coded `a = 2` was bracketed instead of imported as canon. `BRACKETED(pending-ruling)` was exercised three times (β, the rotational top, and by extension `p`). |
| **6 · Energy ledger** | FILLED | **High value.** Forcing "is the rotational channel a continuum-counted port at `ω`?" to be the ANSWERED question rather than an assumption is what produced `G-REAL` — a gate on the SIGN of `ω_m² − ω²` — instead of a hand-wave. |
| **7 · Calibratability** | FILLED | **High value, and it caught something.** The row's demand that the target be a ratio is what surfaced that `2(G_c/G)` is the ONE place an absolute modulus enters, and got it quarantined into its own field and its own bin before any number existed. |
| **8 · Discrimination class** | FILLED | The **tautology filter** did real work: "does a gapped branch reject a below-gap drive" is a restatement of `ω < ω_gap` and would have been a non-result. Re-posing it as "does the bias ever drive the gap below the drive on cells that exist" is what produced the knife-edge. |
| **9 · Certification plan** | FILLED — **and its own sub-clause caught this lane** | The pre-freeze second-method check (§5.2) covered the derived constants and **not** the negative-control tolerances, and the failure landed exactly in the gap. **See FLAG-FREEZE; a row-9 extension is routed.** |
| **10 · Adjudication routing** | FILLED | The fence (prereg §8) is what kept the MeV-scale frontier item to one cross-reference line under pressure to say more. |
| **11 · Numerical conditioning** ★ | FILLED — **and the metric clause paid off in an unexpected direction** | Naming the error-propagation model AND its metric forced the statement *"this lane has no iterated map; the metric it contracts in is the trivial one"* — which is a **negative** fill, and it is exactly the fill a successor adding a cascade needs to see, because it tells them they inherit no contraction argument. **Proposal: row 11 should say a NO-ITERATION declaration is a valid and required fill, not a skipped row.** The named-cancellation sub-row caught the float64 `1−A²` (again) and the `Σ1/(n−1+θ)^{2p}` convergence boundary at `2p = 1`. |

**Amendment proposals from this pilot (routed, NOT drafted — the auditor lands SVA amendments):**
(a) row 9 sub-clause should extend the pre-freeze second-method check to **negative-control**
tolerances explicitly; (b) row 11 should name a NO-ITERATION declaration as a required positive
fill; (c) row 4 should name "declare the observable plane-invariant" as an explicit option.

---

## §9 — CLASSIFICATION + FENCE

**Class: DERIVATION, NOT CERTIFIED. Mints nothing, moves no solidity, adjudicates no physics fork,
awards no bin.** The FORM derived here — the driven-tank `ζ`, the crossing condition, the integer
`N_open`, the knife-edge at `p = 2`, the `ζ_max < 1` identity — is an **axiom-manifestation,
FORM-class** consequence of the Ax-4 kernel plus lattice discreteness plus the A-008-ruled
`G_c/I_ω = ω_C²`. Every SI-scale quantity it touches is **VALUE-CONSISTENCY class**, riding `G`,
`M`, the GR-imported `ν_vac` in `r_sat = 7GM/c²`, and the definitional `ℓ_node = ħ/(m_ec)`.

**This lane does NOT license:**

1. **Any bin.** `LEAK-NOT-CERTIFIED`. The §4 table is a diagnostic.
2. **Anything about the rotational channel AT or INSIDE `r_sat`.** The domain stops at the innermost
   intact cell. The ruling's carve-out and its ROUTED penetrating-radiation frontier item are
   untouched; **MeV-scale rotational radiation is out of scope** (§6.2, one line).
3. **Any adjudication of the cross-grade aggregation fork** (L∞ vs normalized-L2), of FORK-3(b), of
   the `β` bracket, of the `K(A)` fork, of `FLAG-CAUSAL`, or of any predecessor's bins.
4. **Any promotion of the engine's coded `a = 2` to canon**, and **no invention of an `I_ω(A) law`**.
   The `p ≥ 2` members exist to bracket. The RHO-B `1/S³` grading is applied to the micro-inertia
   **by ANALOGY and is labelled as an analogy at every site it appears.**
5. **Any AVE-vs-competitor discrimination claim.** The ECO free-reflectivity degeneracy carried at
   `2026-08-05_echo-delay-v2-reach-through_result.md`'s headline applies here unchanged: an ECO with
   a free contact reflectivity reproduces any conversion verdict, so **nothing here is a
   discriminator**.
6. **Any KB, manuscript or `src/ave` edit.** Every predecessor artifact read by this lane is
   **byte-untouched**; the receipts are the quotations above.

**The single hinge, stated plainly:** if a grading law for `I_ω(A)` is ever ruled at `b = 3` while
the engine's `a = 2` stands, `p = 2.5` and the diagnostic's pointing **inverts** — cells open, and
the leak clause needs its second sentence. **That is the only way this pointing moves**, and it is
named here rather than buried.
