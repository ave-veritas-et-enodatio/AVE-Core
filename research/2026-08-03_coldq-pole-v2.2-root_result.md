# The cold-Q pole v2.2 — RESULT: `ROOT-NOT-CERTIFIED`. Ten of eleven gates pass, all eleven self-tests fire, and the one failure is an order I put in my own ladder below the resolution my own prereg cited

**Date:** 2026-08-03
**Prereg-file**: research/2026-08-03_coldq-pole-v2.2-root_prereg-FROZEN.md
**Prereg-commit**: f15a6e4d (frozen and pushed ALONE, before any driver code and before any number produced by this instrument existed)
**Driver:** [`research/drivers/coldq_pole_v2p2_root.py`](drivers/coldq_pole_v2p2_root.py) → [`research/drivers/coldq_pole_v2p2_root_results.json`](drivers/coldq_pole_v2p2_root_results.json)
**Number check:** [`research/drivers/coldq_pole_v2p2_root_number_check.py`](drivers/coldq_pole_v2p2_root_number_check.py) — gating via `make verify`
**Class:** DERIVATION result (research-doc; **mints no `clm-`/`def-`; propagates to no KB/manuscript leaf; changes no solidity; edits no falsification ledger**). Engine `src/ave` byte-untouched.
**Provenance:** Grant's ruling of 2026-08-03 on the PR #854 audit's Q2 — **certify the located root, not the rectangle.** Written against `origin/main` = `184db4b6`.

---

## HEADLINE

> **Certification: `ROOT-NOT-CERTIFIED`. Frozen precedence therefore fires `BIN-F-ROOT`, and NO physics bin is adjudicated.**
>
> **One gate of eleven failed. All eleven self-tests fired.** G2 — `n`-independence over the frozen ladder — measured `1.2496816388248957e-10` against the frozen `1e-10`. **A factor of `1.25` outside, and it is entirely the `n = 32` rung.**
>
> **The failure is in MY OWN gate specification, it is knowable from my own frozen document against itself, and I am not repairing it here.** The prereg's own **§6** — the FT-2 non-vacuity column at `research/2026-08-03_coldq-pole-v2.2-root_prereg-FROZEN.md:337` — cites v2.1's measured Chebyshev coefficient tail as reaching `5.3e-16` only by `n = 40`, and the prereg then froze an independence ladder starting at `n = 32`, below that, at a `1e-10` tolerance. That is the audit's WARN-4 lesson (*"knowable at freeze, from the frozen file against itself"*) landing on this lane. **Per the frozen Rule-11 fence nothing is retuned; the negative is banked and routed to a successor with a new version number.**
>
> **★ AND THE GATE THE LANE WAS BUILT FOR PASSED, DECISIVELY.** G5 — isolation — returns **exactly one** pencil eigenvalue within `R_iso = 0.5` of the certified root **at every order of the ladder**: `[1, 1, 1, 1, 1]`. Pointed at the v2.1-banked discretization artifact by FT-5(a) the same measurement returns `[2, 1, 2, 3, 0]` with a `0.16191` relative drift; pointed at v2.1's own contaminated-edge C9 probe by FT-5(b) it returns `[1, 1, 0, 0, 0]`. **The PR #854 audit's migrating pseudo-spectrum is REPRODUCED at the pseudo-poles and ABSENT at the root, by one and the same measurement.**
>
> **The reimplementation lands on v1's root.** G6 measured `6.8032e-07` relative against the v1 shipped comparator — an independent transcription of the operator, sharing no line of code with either predecessor, agreeing with a *different-in-kind* instrument. FT-6 shows the same gate reads `5.8722e-04` under a `1e-3` coefficient corruption, so it is catching transcription error rather than rubber-stamping a known agreement.
>
> **And v2.1's `ν_vac`-exactness artifact cannot recur here.** G8 measures the `x_sat` spreads in mp end-to-end and reports `1.8619e-46` — honestly non-zero, where v2.1's `complex` cast reported `0.0` (audit WARN 7).

---

## §1 — THE GATE TABLE (measured against frozen; nothing dropped, widened or re-defined)

**Frozen:** `no gate, tolerance, frozen numeric parameter or method element in sections 4 and 5 may be changed after any gate result is seen; if this instrument fails certification the lane reports ROOT-NOT-CERTIFIED and routes to its own successor with a new version number, exactly as #845 routed to v2, v2 to v2.1 and v2.1 to v2.2`.

**No frozen criterion was dropped, widened, or re-defined. Every gate is reported at the tolerance it was frozen at.**

| gate | what it certifies | frozen tol | measured | verdict |
|---|---|---|---|---|
| **G0** | operator-transcription identity, `𝓛_η ≡ 4η²·𝓛_A` | `1e-13` | `1.0385e-15` | **PASS** |
| **G1** | residual of the certified eigenfunction at the certified root (mp, `dps = 50`) | `1e-20` | `4.7268e-50` | **PASS** |
| **G2** ★ | `n`-independence over `n ∈ {32, 48, 64, 80, 96}` | `1e-10` | `1.2496816388248957e-10` | **FAIL** |
| **G3** | hyperboloidal-gauge independence, `λ ∈ {−0.25, 0, +0.25}` | `1e-12` | `3.3323e-14` | **PASS** |
| **G4** | (a) precision `dps 50` vs `80`; (b) double-pencil vs mp at every order | `1e-25` / `1e-6` | `5.2778e-47` / `1.7559e-08` | **PASS** |
| **G5** ★ | **ISOLATION** — pencil-eigenvalue count within `R_iso = 0.5` at every order | exactly `1` | `[1, 1, 1, 1, 1]` | **PASS** |
| **G6** | two-instrument agreement vs the v1 shipped root | `1e-5` | `6.8032e-07` | **PASS** |
| **G7** | spin-2-vs-spin-1 at the root: (a) eigenvalue, (b) eigenfunction | `1e-3` both | `0.28424` / `0.19697` | **PASS** |
| **G8** | `ν_vac` cancellation at the root, **mp end-to-end** | `1e-9` | `1.8619e-46` | **PASS** |
| **G9** | determinism | identical digest | `a10f8aa906198605` twice | **PASS** |
| **G10** | Ax-3 (a) operator reality, (b) conjugate-mirror symmetry | `1e-40` / `1e-20` | `0.0` exactly / `9.2731e-47` | **PASS** |

### Self-test table (each MUST fire)

| self-test | targets | frozen threshold | measured | fired? |
|---|---|---|---|---|
| **FT-0** `𝒞₀` corrupted `1e-12` | G0 | `≥ 1e-13` | `2.0668e-12` | **FIRES** |
| **FT-1** residual off-root at `Ω(1 + 1e-10)` | G1 | `≥ 1e-15` | `9.9464e-12` | **FIRES** |
| **FT-2** under-resolved `n = 8` | G2 | `≥ 1e-6` | `4.4038e-04` | **FIRES** |
| **FT-3** ★ correctly-specified half-applied gauge (`λ` omitted from `𝒞₂` only) | G3 | `≥ 1e-6` | `0.34859` | **FIRES** |
| **FT-4** (a) `dps = 20`; (b) double pencil at `n = 8` vs mp at `n = 48` | G4 | `≥ 1e-25` / `≥ 1e-6` | `4.3167e-17` / `4.4038e-04` | **FIRES** |
| **FT-5** ★ (a) centred on the v2.1 artifact; (b) centred on the v2.1 contaminated-edge probe | G5 | count `≠ 1` at ≥ 1 order (see §3) | `[2, 1, 2, 3, 0]` / `[1, 1, 0, 0, 0]` | **FIRES** |
| **FT-6** `𝒞₀` corrupted `1e-3`, compared to the v1 comparator | G6 | `≥ 1e-5` | `5.8722e-04` | **FIRES** |
| **FT-7** REVERSE — identical specifications on both axes | G7 | both `< 1e-3` | `0.0` / `0.0` | **FIRES** |
| **FT-8** `x_sat`-dependent profile perturbation | G8 | `≥ 1e-9` | `6.0137e-07` | **FIRES** |
| **FT-9** one gate value perturbed `1e-15` in a copy, re-digested | G9 | digest must change | `2bbf4ed56f88a49f` → `7fb7264003cde091` | **FIRES** |
| **FT-10** smuggled `Im(μ)/Re(μ) = 1e-3` | G10 | `≥ 1e-6` / `≥ 1e-5` | `0.031675` / `5.8360e-04` | **FIRES** |

**Frozen:** `a gate that cannot fail is not a gate; if any self-test fails to fire, the certification is ROOT-NOT-CERTIFIED regardless of how many gates passed`. **Every self-test fired. The certification fails on a gate, not on a dead gate.**

---

## §2 — THE ONE FAILURE: MECHANISM MEASURED, NOT ASSERTED

**Frozen:** `the maximum pairwise relative separation of Omega_star(n, 0.0, 7.0, 50) over the frozen ladder n in {32, 48, 64, 80, 96} is <= 1e-10`.

### §2.1 The located roots, order by order

| `n` | `Re Ω` | `Im Ω` |
|---|---|---|
| 32 | `1.8536552111039672` | `-1.007256783157842` |
| 48 | `1.8536552108408788` | `-1.0072567831433188` |
| 64 | `1.853655210840725` | `-1.0072567831433927` |
| 80 | `1.853655210840725` | `-1.0072567831433925` |
| 96 | `1.853655210840725` | `-1.0072567831433925` |

### §2.2 The diagnostic that tests the attribution rather than asserting it

> **⚑ DISCLOSED: this diagnostic was ADDED AFTER G2's outcome was seen.** It changes no frozen criterion, changes no verdict, enters no bin, and is tagged in the shipped JSON as `NOT-ADJUDICATED DIAGNOSTIC -- no gate, no bin, no verdict`. It exists because *"this is under-resolution, not the audit's pseudo-spectrum"* is a claim, and a claim of that shape is exactly what the PR #854 audit refuted the last time this arc asserted one (`0a7dec1f`, R1). **So it is measured.**

**The test.** If the ladder's spread is spectral under-resolution, the error against the highest order must fall **geometrically** in `n`. If it is a migrating pseudo-pole — the audit's mechanism — it must not.

| `n` | error vs `n = 96`, relative | ratio to the next rung |
|---|---|---|
| 32 | `1.2497e-10` | `1544.6` |
| 48 | `8.0906e-14` | `690.97` |
| 64 | `1.1709e-16` | `403.39` |
| 80 | `2.9026e-19` | — |
| 96 | `0.0` (reference) | — |

**Clean geometric convergence over four rungs.** The instrument is resolving, and it is resolving at a rate that puts `n = 32`'s error exactly where an exponentially-convergent spectral method puts it. **A migrating pseudo-pole does not do this** — FT-5(a) measures what one actually does (§3.2), and it is not this.

### §2.3 Why the failure is a specification defect, and why it was knowable at freeze

**Only the `n = 32` rung puts the gate over.** Every rung from `n = 48` up sits within `8.0906e-14` of the `n = 96` reference, so by the triangle inequality the maximum pairwise separation over `{48, 64, 80, 96}` alone cannot exceed `1.6181e-13` — **three orders inside the frozen `1e-10`.**

**And the prereg contains the evidence that `n = 32` did not belong there.** It is in **§6**, the self-test table's non-vacuity column, at `research/2026-08-03_coldq-pole-v2.2-root_prereg-FROZEN.md:337` — the FT-2 row, verbatim: *"at `n = 8` the Chebyshev basis cannot represent the coefficient functions, whose measured tail (v2.1 §9 item 7) only reaches `5.3e-16` by `n = 40`"*. **An independence ladder whose lowest rung sits below the order at which the coefficient functions are resolved is not measuring the root's `n`-independence; it is measuring the basis's inadequacy at that rung.**

> **⚑ CORRECTED 2026-08-03 (post-review) — SECTION POINTER, at five sites.** This document, its docket fragment, the gating number check's reason string for `5.3e-16` and the PR body all cited the receipt as living in the prereg's **§9**. **It does not.** §9 is the tolerance-derivation table; its **G0** row (`:474`) cites a different v2.1 measurement — C11's `8.9716e-16` on the operator identity — which has nothing to do with the coefficient tail or with G2's ladder. The `5.3e-16`-by-`n = 40` receipt lives in **§6**'s FT-2 non-vacuity cell at `:337`, and the inner citation there is to **v2.1's** §9 item 7, which is the likely source of the slip. **The argument is unchanged and was never load-bearing on the pointer: the receipt is in the frozen file, it was knowable at freeze, and it says what this section says it says.** Original text of this paragraph, verbatim: *"Its own §9 justifies G0's tolerance by citing v2.1's measured Chebyshev coefficient tail, which reaches `5.3e-16` only by `n = 40`."* — **the clause "justifies G0's tolerance" is retracted as well as the section number**; the coefficient tail justifies nothing about G0. The prereg then compounded it by deriving the `1e-10` tolerance from a prior-lane characterization — *"n-stable to 12 digits over `n = 32 → 80`"* — that this reimplementation does not reproduce at `n = 32` (see FLAG-8, §6).

**This is the audit's WARN-4 finding landing on this lane.** WARN 4 (`6a93131a`) said of v2.1's FT-B: *"Two statements in one frozen document contradict each other and the self-test was frozen on the false one. The original 'discovered only by running' framing is too generous to this lane."* **The same sentence applies here, to G2's ladder, and it is written here rather than waiting for an auditor to write it.**

### §2.4 What is NOT repaired

**Per Rule 12 the slot is not refilled.** The obvious successor move — a ladder whose lowest rung is derived from the coefficient tail rather than chosen — is **stated so a successor does not have to rediscover it, and explicitly NOT adopted here**: it would be a post-hoc parameter selection under a frozen fence, which is exactly what Rule 11 forbids. A v2.3 needs a new prereg, a new version number and its own verification chain. **G2 stays banked as FAIL.**

### §2.5 ⚑ ADDED 2026-08-03 (post-review) — THE TOLERANCE'S PREMISE WAS MIS-ATTRIBUTED, AND IT WAS ALREADY STALE WHEN THE PREREG FROZE

> **This subsection changes NO frozen criterion, NO gate result and NO verdict.** `G2` remains **FAIL** at the tolerance it was frozen at, the certification remains **`ROOT-NOT-CERTIFIED`**, and the frozen prereg is **byte-untouched** — the defect is disclosed here, not edited there. It is written because the PR #856 review established that the failure is manufactured by a premise, and a reader is entitled to know that before a successor inherits the same derivation.

**What the prereg derived the `1e-10` from, verbatim** (`research/2026-08-03_coldq-pole-v2.2-root_prereg-FROZEN.md:476`, the §9 G2 row):

> *"the PR #854 audit measured this root stable to **12 digits** over `n = 32 → 80` (`0a7dec1f`: "only Omega = 1.853655 - 1.007257i is n-stable"). **`1e-10` is frozen two orders looser than the measured evidence supports**, as honest headroom for the two orders the audit did not sweep (`n = 96`, and this lane's own reimplementation)"*

**Defect 1 — the attribution is wrong.** Commit `0a7dec1f` **contains no digit count at all.** The review checked the whole commit — message and diff — and the string `digit` does not occur in it; what `0a7dec1f` actually measured, and what the quoted fragment actually says, is that the root is the only `n`-stable eigenvalue in the box, with **no** statement of how many digits. The *"12 digits"* characterization is not the audit's; it was the **#854 lane's own result-doc text**.

**Defect 2 — and that text had already been retracted by the lane that wrote it.** `cb2012af` (`2026-08-03T06:36:08-07:00`) carries the 🔴 restatement verbatim: *"stable to **12 digits across `n = 48 → 80` (~10 digits from `n = 32`)**"*, correcting an original that read *"stable to **12 digits across `n = 32 → 80`**"*. **This lane's FLAG-8 (§7) already reported the measurement half of this and credited `cb2012af`. What FLAG-8 did not report is the consequence for the tolerance itself, which is this:**

**Under the corrected premise, the prereg's OWN rule returns a tolerance this gate passes.** The rule the prereg states is *"two orders looser than the measured evidence supports"*:

| premise | evidence | prereg's own rule → tolerance | this battery's measurement | outcome |
|---|---|---|---|---|
| **as frozen** — 12 digits from `n = 32` | `1e-12` | `1e-10` | `1.2496816388248957e-10` over `{32, 48, 64, 80, 96}` | **FAIL by `1.25`×** |
| **as corrected** — ~10 digits from `n = 32` | `1e-10` | `1e-8` | the same `1.2496816388248957e-10` | **PASS by `80.02`×** |
| **as corrected, ladder from `n = 48`** — 12 digits from `n = 48` | `1e-12` | `1e-10` (the frozen value itself) | `8.0906e-14` over `{48, 64, 80, 96}` | **PASS by `1236`×** |

**So the FAIL is manufactured entirely by the stale premise.** Every route through the prereg's own derivation rule, run on a premise that was already corrected in the corpus twelve minutes after this file froze, returns a tolerance this instrument meets — in one case the *identical* `1e-10`, merely applied to a ladder whose lowest rung is resolved.

**The operational receipt, and it is a sharp one.** The review located the FAIL/PASS boundary by re-running this lane's own `root()` on shifted ladders: the frozen `1e-10` is crossed **between `n = 32` and the very next rungs above it**, and every ladder whose lowest rung is `n = 34` or higher PASSES. **The boundary sits immediately below the `n = 40` resolution receipt the prereg itself cites in §6** — which is the same statement §2.3 makes, now with the crossing measured rather than argued. The per-rung numbers are in the docket fragment; they are a post-result reproduction, they are not in the shipped JSON, and **they adjudicate nothing here.**

**What this does NOT do.** It does not retune, reinterpret or rescue `G2`. **The gate as frozen, measured as frozen, failed** — that is the banked result and it is what `BIN-F-ROOT` fired on. **A tolerance derived from a stale premise is still the tolerance this lane froze, and Rule 11 binds the lane to it.** The correction is routed **into the v2.3 prereg's tolerance derivation**, where it belongs: a successor must derive `G2`'s tolerance from the *corrected* stability characterization and from a ladder whose lowest rung is resolved, and must cite `cb2012af` rather than `0a7dec1f` for the digit count.

---

## §3 — WHAT THE LANE DID ESTABLISH

### §3.1 ★ The root is isolated — this is the finding Grant's ruling asked for

**Frozen:** `G5 counts the eigenvalues of the double-precision linearized quadratic pencil of the SAME operator at the SAME order, deduped at the frozen 1e-6 relative radius, that lie within R_iso of the polished root at that order; the count must be EXACTLY ONE at every order of the frozen ladder n in {32, 48, 64, 80, 96}`.

| `n` | 32 | 48 | 64 | 80 | 96 |
|---|---|---|---|---|---|
| **count within `R_iso = 0.5` of the certified root** | `1` | `1` | `1` | `1` | `1` |

**The isolation radius is derived, not picked** (prereg §4.3), and the driver reproduces all four receipts:

| receipt | measured |
|---|---|
| GR `ℓ=2` fundamental→first-overtone spacing in `Ω` units | `1.3083542634814167` |
| that spacing ÷ `R_iso` | `2.6167085269628334` |
| distance from the seed to the v2.1-banked artifact | `2.127881506829584` |
| that distance ÷ `R_iso` | `4.255763013659168` |
| `R_iso / |Ω|` | `0.23700665113790634` |
| `R_iso` ÷ the frozen dedupe radius | `237006.65113790636` |

**Read what that means.** A genuine overtone at GR-like `ℓ=2` spacing would sit `2.62×` outside the annulus and would **not** trip this gate — the gate excludes contamination, not physics. And the annulus is `2.37e5` times the dedupe radius, so `[1, 1, 1, 1, 1]` is not a restatement of dedupe.

### §3.2 ★ The audit's mechanism is reproduced — at the pseudo-poles, and only there

**Frozen:** `case (a) MUST return a count different from exactly one at at least one order of the frozen ladder, OR a polished n-drift above the G2 tolerance at those orders; AND case (b) MUST return a count different from exactly one at at least one order of the frozen ladder`.

The **same routine**, the **same radius**, the **same ladder**, pointed at three different places:

| centre | `n = 32` | `48` | `64` | `80` | `96` | `n`-drift of the polished centre |
|---|---|---|---|---|---|---|
| **the certified root** | `1` | `1` | `1` | `1` | `1` | `1.2496816388248957e-10` (G2) |
| **the v2.1-banked artifact** (I17) | `2` | `1` | `2` | `3` | `0` | `0.16191` |
| **the v2.1 contaminated-edge C9 probe** (I18) | `1` | `1` | `0` | `0` | `0` | — |

**This is the PR #854 audit's finding, independently reproduced by a different implementation, and localized.** `0a7dec1f` measured *"In-box pencil eigenvalue count grows 2 -> 9 as n goes 32 -> 80"* over the whole rectangle. Here the same instability is visible **inside a `0.5`-radius disc around a pseudo-pole** — the count walks `2 → 1 → 2 → 3 → 0` and the polished centre wanders by `16.191` percent — while the same disc around the certified root holds a flat `1` at every order and a centre that moves by `1.25e-10`. **Nine orders of magnitude separate the two behaviours, measured by one routine.**

### §3.3 The reimplementation lands on v1's root

**Frozen:** `the certified root agrees with the v1 root reconstructed programmatically from research/drivers/coldq_pole_derivation_results.json row x_sat = 7.0 as x_sat*(omega_R_M - i*omega_I_M) to <= 1e-5 relative`.

| quantity | value |
|---|---|
| v2.2 certified root | `1.8536552108408788` `-1.0072567831433188` i |
| v1 comparator, reconstructed programmatically | `1.8536565650028993` `-1.00725725871003` i |
| relative agreement | `6.8032e-07` |

**Frozen:** `G6 gates THIS lane's reimplementation against a prior-lane comparator and certifies NOTHING about PR #845, which remains SOLVER-NOT-CERTIFIED; a G6 pass may not be reported as corroboration of #845, and no #845 number enters any bin, any other gate, or any comparator in this lane`. **Honoured: #845 is unchanged, uncertified, and no number of its enters anything here but this one gate.**

**And the gate is live.** FT-6 corrupts one coefficient by `1e-3` relative and the same comparison reads `5.8722e-04` — `59×` outside the tolerance. G6 catches a transcription error.

### §3.4 The spin-2 discipline is load-bearing at the root, measured twice

**Frozen:** `(a) replacing the spin-2 traction-free wall row by the spin-1 wall condition W'(r_sat) = 0 MOVES the root by >= 1e-3 relative, AND (b) replacing the spin-2 (ell-1)(ell+2) angular weighting by the spin-1 ell(ell+1) weighting in the mode-energy functional evaluated on the CERTIFIED EIGENFUNCTION changes the window-integrated strain-to-kinetic energy ratio by >= 1e-3 relative`.

- **(a) on the eigenvalue:** `0.28424`. **Cross-lane, non-gating:** v2.1's FT-F(ii) applies the *identical* mutation — its driver's `spin1_wall` branch, transcribed here with attribution — and its result doc quotes `0.28424`. **Two implementations of one mutation, agreeing at the quoted precision.** (v2.1's full-precision value lives in a JSON on the PR #854 branch, which is not on `origin/main`, so the comparison is made only at the precision v2.1's doc quotes.)
- **(b) on the eigenfunction:** `0.19697`.
- **FT-7, the reverse fireability:** pointed at identical specifications on both axes the discriminator returns `0.0` and `0.0`. **It does not manufacture a difference where none exists.**

> **⚑ FLAG-9 — NEW, and it runs against the convenient reading. v1's `0.28430` is a DIFFERENT mutation and must not be added to this agreement.** v1's FT-2 is the **clamped** inner wall, `W(r_sat) = 0`, the `Γ = +1` alternative of #814 FORK-3(b) — verbatim from its frozen prereg at `research/2026-08-02_coldq-pole-derivation_prereg-FROZEN.md:229`: *"replace the traction-free inner condition by a **clamped** one (`W(r_sat) = 0`, the `Γ = +1` open/clamped alternative of #814 FORK-3(b)/CF-13)"*. In the compactified variables the clamped condition is `ψ(0) = 0`, whereas the spin-1 condition is `[1 + iΩ(λ−1)]ψ(0) − ψ_ηη(0)/2 = 0` — **two different rows, not one.** v2.1's result-doc §5.4 cross-lane table places them in a single row labelled *"spin-1 / clamped wall shift"* and reports their `2.1e-04` agreement as a cross-lane comparison. **That row compares two different mutations.** Whether the numerical closeness is a coincidence or a property of the cavity is **not resolved here**; it is surfaced with both file paths and both verbatim descriptions, and neither side is reframed to match the other. Routed to the auditor lane and to the #854 lane, whose files this lane does not touch.

### §3.5 The `ν_vac` cancellation, measured in mp end-to-end — and honestly non-zero

**Frozen:** `across x_sat in {5, 7, 11} the mp-computed relative spreads of Q = Re(Omega)/(2*abs(Im(Omega))) and of abs(Omega) are each <= 1e-9, and omega_R*M_g = Re(Omega)/x_sat scales as 1/x_sat to <= 1e-9 relative; no value on the path from the polished root to these spreads is cast to a double-precision complex`.

| quantity | measured |
|---|---|
| `Q` relative spread across `x_sat ∈ {5, 7, 11}` | `1.8619e-46` |
| `|Ω|` relative spread | `6.0633e-47` |
| `1/x_sat` scaling spread | `9.7741e-47` |

**This is the audit's WARN-7 defect closed at source rather than inherited.** v2.1 reported `0.0` here and its result doc said the cancellation was *"EXACT, to the last bit"*; `21981789` established that the `0.0` was an artifact of a `complex` cast at `research/drivers/coldq_pole_v2.py:612`. **This lane's G8 path carries mp from the polished root to the reported spread and reports what mp says.** The number is not zero, it is `1.8619e-46`, and the gate passes on the number rather than on a rounding.

### §3.6 Ax-3 is structural, and it is measured on the certified root's own operator

**Frozen:** `(a) the row-equilibrated mp operator at n = 48 and every lam in {-0.25, 0.0, +0.25} has max|Im M0|/max|M0|, max|Im M2|/max|M2| and max|Re M1|/max|M1| each <= 1e-40, AND (b) the conjugate-mirror root polished from the seed -conj(Omega_star) satisfies |Omega_mirror + conj(Omega_star)| / |Omega_star| <= 1e-20`.

- **(a) operator reality:** `0.0` — exactly, in mp, at all three gauges. `M0` and `M2` are real and `M1` is purely imaginary, which is the frequency-domain form of *"the medium stores and does not dissipate"*.
- **(b) conjugate-mirror symmetry at the root:** `9.2731e-47`.
- **FT-10:** a smuggled `Im(μ)/Re(μ) = 1e-3` drives (a) to `0.031675` and (b) to `5.8360e-04`. **Both halves of the Ax-3 gate detect a lossy medium.**

### §3.7 The eigenfunction residual

**Frozen:** `the infinity-norm residual max_i |(M(Omega_star) psi)_i| / max_i |psi_i| of the CERTIFIED EIGENFUNCTION on the row-equilibrated mp operator at dps = 50 is <= 1e-20`. Measured `4.7268e-50` — at the arithmetic's own floor, `29` orders inside the gate. FT-1 moves the evaluation point by `1e-10` relative and the residual rises to `9.9464e-12`, so the gate is measuring the root and not a normalization.

---

## §4 — THE BINS: `BIN-F-ROOT` fired, so nothing is adjudicated

**Frozen:** `no adjudication criterion below may be dropped, widened or re-defined after any result is seen; no input in the section 3 ledger may be retuned; whatever the instrument returns is banked`.

The frozen precedence is `BIN-F-NOROOT` > `BIN-F-ROOT` > `BIN-F-PROFILE` > `BIN-1/2/3`, with the instruction that if an earlier bin fires the later ones are reported as `N/A — not adjudicated` and **no verdict language is used about them**.

| bin | outcome |
|---|---|
| **`BIN-F-NOROOT`** | **did not fire** — a root was located at every order of the ladder |
| **`BIN-F-ROOT`** | **FIRED** — G2 failed at its frozen tolerance |
| **`BIN-F-PROFILE`** | **did not fire** — no canonical-input contradiction was encountered on the domain |
| **BIN-1** (`ω_R M_g`) | **`N/A — not adjudicated`** |
| **BIN-2** (`Q`, and the three-way discriminator) | **`N/A — not adjudicated`** |
| **BIN-3** (radial localization / FORK-1) | **`N/A — not adjudicated`** |
| **BIN-4** (overtone ladder / completeness) | **`N/A BY CONSTRUCTION`** |

**Frozen:** `BIN-4 is N/A BY CONSTRUCTION in this lane and is not adjudicated at any precedence level including a full gate pass; no overtone, no ladder, no mode count and no completeness statement is computed, and the deferral is an open instrument-scope question awaiting a substrate-derived low-frequency cutoff, not a failure of this lane`. **`BIN-4`'s status here is NOT a consequence of the G2 failure. It would read the same on a full pass.**

**Frozen:** `this lane asserts the existence and location of THIS root; it asserts NOTHING about the absence or presence of other modes`. **Restated at the point where a reader is most likely to over-read the `[1, 1, 1, 1, 1]` of §3.1: that row says nothing sits within `0.5` of this root. It says nothing whatever about what sits anywhere else.**

**Frozen:** `no argument-principle winding, no contour integral and no region count is computed anywhere in this lane; the pole-counting instrument the PR #854 audit impeached is not used, not repaired and not relied on`. **Verifiable by grep: the driver contains no winding, no contour and no argument-principle routine.**

---

## §5 — NOT-ADJUDICATED DIAGNOSTICS (numbers, no verdicts, no comparisons)

These carry **no bin**, **no claim**, **no solidity** and **no comparison against any comparator**. The frozen precedence forbids verdict language about the unadjudicated bins, and a percentage deviation against a bin comparator is one keystroke from a verdict — **so the deviations are deliberately not computed in this document.** The comparator values themselves are shipped in the JSON for a successor.

### §5.1 The certified root and its projections

| quantity | measured |
|---|---|
| `Ω = ω·r_sat/c₀` (scale-free) | `1.8536552108408788` `-1.0072567831433188` i |
| `\|Ω\|` (mp, cast at report time) | `2.109645436528558` |
| `ω_R M_g` at `x_sat = 7` | `0.2648078872629827` |
| `Q = Re(Ω)/(2\|Im Ω\|)` | `0.9201502744197102` |

### §5.2 Radial localization (the object BIN-3 would have read)

Both frozen measures agree exactly and both place the maximum at the **outer** edge of the frozen window `r/r_sat ∈ [1.0, 2.0]`: `u_energy = u_kinetic =` `2.0000000000000004`, `interior_max = false`, wall energy density `0.040561477092864194` of the window maximum. **Reported as a number, not as a bin.** For reference, v2.1's independent extraction of the same quantity read `0.040561477093055825` — the two agree to `4.7e-12` relative, which is a cross-implementation check on the eigenfunction, not a physics statement.

---

## §6 — DISCRIMINATION NOTE: what a certified root and adjudicated bins WOULD and WOULD NOT mean

**Required by this lane's own discipline and written even though nothing was adjudicated, so that a successor cannot present a future pass as more than it is.** Classification per `consistency-vs-emergence`.

### §6.1 The certification itself

**A `ROOT-CERTIFIED` verdict is a statement about an INSTRUMENT, not about the world.** It says: *this discretization's eigenvalue at this location is a property of the continuous problem and not of the discretization.* It does **not** say the substrate rings there. That further step needs the canonical input set to be right, and **I7 — the reflectionless Regime-I port at infinity — is assumed, not tested** (FLAG-3). If the substrate carries any far-field reflector, the certified root is wrong in the same direction as every other number in this arc.

**Classification: the certification is an INSTRUMENT-CONSISTENCY result. It is not an emergence claim of any class, and it cannot become one.**

### §6.2 The bins, had they been adjudicated

| bin | class | a PASS would mean | a PASS would **NOT** mean | a FAIL would mean |
|---|---|---|---|---|
| **BIN-1** `ω_R M_g` vs the GR comparator | **VALUE-CONSISTENCY**, never emergence | the graded-cavity eigenfrequency is numerically compatible with GR's `ℓ=2` fundamental | **anything about value-level emergence.** `ω_R M_g = Re(Ω)/x_sat` carries the GR-imported `ν_vac = 2/7` through the `7` in `r_sat = 7GM/c²`, whose provenance is closed as GR-import by PR #261/#506. A match is a **consistency check on an imported scale** | the graded profile does not reproduce the GR fundamental — a clean negative on the standing chain's *value*, not on its form |
| **BIN-2** `Q` vs `Q_GR` | **`ν_vac`-FREE — the only emergence-capable axis in this lane** | `Q = Re(Ω)/(2\|Im Ω\|)` contains no `r_sat` scale (G8 measures the cancellation at `1.8619e-46`), so a match would be a value-level result **not inherited through the GR-imported `7`** | that AVE *derives* GR. It would mean the canonical profile + Ax-4 kernel + Op16 projection + `Γ=−1` SHORT produce GR's damping ratio with **zero free parameters** — a strong consistency result, and AVE-**distinct** only if the *form* of the derivation differs from GR's own, which this lane does not establish | the substrate's cold `Q` differs from GR's. Given `Q = ℓ` is B1-ratified corpus, a fail would be routed to Grant as a **flag on the standing anchor**, not applied as a fix |
| **BIN-3** `r_peak/r_sat` | **FORM-class**, `ν_vac`-free | the mode localizes where one of the two standing pictures (rim vs ramp) says | much on its own — §5.2's endpoint reading is dominated by the generic outward `exp(\|ω_I\|r)` growth of *any* quasinormal eigenfunction, which is why `BIN-3-MONOTONE` was reserved in advance | that the localization question is **ill-posed for this mode** — which is information, not failure |
| **BIN-4** | — | — | — | **unreachable by construction; see §4** |

### §6.3 ★ THE HONEST SIZE OF THE ω_R AND Q COMPARISONS, stated plainly

**Both are zero-free-input FORM tests against GR values, and that is their entire strength and their entire limit.** The problem in units of `r_sat` has no adjustable parameter at all: the profile is `A = r_sat/r`, the kernel is `S = sqrt(1 − A²)`, the speed is `c₀√S`, the inertia is `ρ₀`. So `Ω` is a pure number forced by the profile SHAPE and `ℓ`. **Nothing can be tuned to move it.**

**What that buys, and what it does not.** A *deviation of any magnitude* is therefore a real statement about the canonical profile — it cannot be attributed to a fitted parameter, because there is none. **But a deviation is NOT automatically a falsification of AVE, and an agreement is NOT automatically a confirmation of AVE**, for three reasons that must be stated together or not at all:

1. **The comparator is GR, and part of the input is GR.** `ω_R M_g` rides the imported `7`. Agreement there is partly an audit of the import chain, not of the substrate.
2. **The FORM is shared.** A graded elastic shear cavity with a soft inner terminus and a radiative outer port is a transmission-line problem; GR's Regge-Wheeler problem is a *different* potential in the *same* mathematical class. **Agreement of two eigenvalue problems in one class is weaker evidence than it feels.** `ave-discrimination-check`: the SM/GR counterfactual is not excluded by a numerical match here.
3. **This lane cannot see the whole spectrum.** With `BIN-4` `N/A BY CONSTRUCTION`, a match on one mode says nothing about whether the ladder matches — and the ladder is where an AVE-distinct forward prediction would actually live.

**Where the AVE-distinct content would be, if any:** in the **overtone ladder** and in the **spheroidal branch**, neither of which this lane computes. **The certified-root result, on its own, is peer-with-GR consistency at best. It is not a chord, and this document does not present it as one.**

---

## §7 — FLAG-DON'T-FIX: what is routed, and to whom

**Nothing below is repaired here.**

1. **★ FLAG-9 is in §3.4 and is the one that runs hardest against this lane's own convenience** — v1's `0.28430` is a clamped-wall mutation, not the spin-1 one, and the cross-lane row that combines them compares two different objects. Stated there rather than repeated here.
2. **★ FLAG-8 — CONFIRMED BY MEASUREMENT, AND INDEPENDENTLY CONFIRMED BY THE CONCURRENT #854 LANE 12 MINUTES AFTER THIS PREREG WAS FROZEN.** This lane's G2 tolerance was derived from the prior-lane characterization *"stable to 12 digits, Chebyshev `n = 32 → 80`"*. **This reimplementation measures `n = 32` against `n = 96` at `1.2497e-10` — roughly 10 significant digits, not 12 — while reproducing ~13 digits over `n ∈ {48, 64, 80}` (`8.0906e-14`).**
>
>    **The #854 lane reached the identical conclusion from its own shipped data, on its own initiative, and has already landed the correction.** Its repair commit `cb2012af` (2026-08-03T06:36:08-07:00) reads verbatim: *"between n = 32 and n = 64 the root moves in the tenth significant digit, so n = 32 carries ~10 digits, not 12; 12 digits holds only from n = 48"*, and it restated the claim at all three of its sites as *"12 digits across n = 48 -> 80 (~10 digits from n = 32), the n = 80 endpoint from the review's sweep"*.
>
>    **The timeline matters and is stated rather than smoothed over.** This lane's prereg was frozen at `f15a6e4d`, 2026-08-03T06:23:52-07:00 — **before** `cb2012af` existed. **So G2's tolerance was derived, in good faith, from a characterization that a concurrent lane corrected twelve minutes later.** That does not rescue G2: the frozen fence binds regardless of when the underlying evidence moved, the gate is banked as FAIL, and nothing is retuned. **What it does establish is that two implementations sharing no code independently measure the same `~10`-digits-at-`n = 32` fact.** The `n`-stability *conclusion* is unchanged in both lanes — the located root is still the only `n`-stable object in the neighbourhood, which is what G5's `[1, 1, 1, 1, 1]` measures. **Nothing is routed as an open question; it is routed as a resolved one, with the other lane's correction credited and its files byte-untouched by this lane.**
3. **⚑ FLAG-1 stands.** Two `Q_GR` comparator values exist in the corpus; the programmatic `2.1002135791366907` is frozen and the rounded-prose value at `research/2026-07-30_qlaw-derivation_scoping.md:401` is reported alongside. The prereg froze the robustness as a criterion (its §7.3). **Not exercised: no bin was adjudicated.** Routed to the auditor lane as a corpus-precision question.
4. **⚑ FLAG-3 stands, and a `ROOT-CERTIFIED` verdict would not have touched it.** I7 — the reflectionless Regime-I port at infinity — is a frozen canonical input and this lane's entire method divides out the corresponding analytic factor. **Not tested; routed.**
5. **⚑ FLAG-4 stands: #814 CF-7's naming gap is untouched.** `manuscript/ave-kb/vol3/claim-quality.md:122` writes `Z_{shear} = \rho\,c_{shear}` and never names which `ρ`.
6. **★ FLAG-5 stands and is the biggest open item in this arc: the completeness question needs a SUBSTRATE low-frequency cutoff.** Until one exists, no lane in this arc can honestly say how many modes the graded shear cavity has. **Routed to Grant (prereg §0's plumber question) and to a successor lane; not attempted, not sketched, not assumed here.**
7. **⚑ FLAG-6 — v2.1's I13 provenance is stale and the correction is recorded, not propagated.** Since PR #845 merged, `ω_I M (ℓ=2, n=1) = 0.273915` has an in-repo carrier at `research/drivers/coldq_pole_derivation.py:106`. **The v2.1 prereg is frozen and byte-untouched.**
8. **⚑ FLAG-7 — the Makefile contact with the concurrent #854 branch.** This lane's gating number check is wired as its **own** target placed away from #854's insertion point; two single-line list appends (`.PHONY` and the `verify:` prerequisite list) are lines the #854 branch also appends to. **Append-only textual contact on two lines, disclosed before either lane merges, for the orchestrator to sequence.** No physics, gate or result depends on it.
9. **`gates.G9.pass` is set by the driver as a placeholder.** Determinism is adjudicated **externally**, by running the driver twice and diffing the shipped objects. That was done: identical digests `a10f8aa906198605`, byte-identical apart from `_runtime_sec`. **Disclosed so the JSON flag is not mistaken for a self-measurement.**

---

## §8 — VALIDATION AND SCOPE DISCLOSURES

- **Frozen:** `total battery runtime <= 3600 s on the reference machine; a longer run is disclosed, not silently accepted`. **Measured 256.15 s and 254.41 s — inside the budget.** The budget is not an adjudication criterion. **These two numerals are deliberately written WITHOUT backticks and are NOT registered:** `_runtime_sec` is machine-dependent, so registering it would make the gating number check fail on every honest re-run on every other machine (the #801 R3 lesson).
- **`_runtime_sec` is machine-dependent and is deliberately NOT registered** in the number check (the #801 R3 / WARN-4 lesson).
- **Frozen:** `engine src/ave BYTE-UNTOUCHED; the instrument lives entirely in research/drivers/ and imports ave.core.* read-only`. **Honoured.**
- **Frozen:** `the v2.2 instrument is an INDEPENDENT REIMPLEMENTATION; research/drivers/coldq_pole_v2.py is neither imported nor edited nor executed by this lane, and every algebraic form transcribed from it carries an attribution comment at the transcription site`. **Honoured — the transcription sites are marked `[xcribe v2.1 ...]` in the driver.**
- **One disclosed double-precision cast.** The certified eigenfunction is computed in mp; for the localization argmax and the G7(b) energy ratio it is cast to double inside a single function, which says so at the cast site. **It does not touch G1, G2, G3, G4, G8 or G10, each of which is mp end-to-end.** This is the v2.1 R6 defect quarantined by construction rather than by care.
- **Scope, unchanged:** `ℓ = 2` is an input, not derived; `ν_vac`, `K = 2G` and the `7` in `r_sat` are GR-imported and untouched; the spin (`a_* > 0`) mapping is out of scope; the spheroidal branch is not built; **no completeness or overtone statement of any kind is made.**

---

> **Result provenance.** Resolves the frozen gates and bins of `research/2026-08-03_coldq-pole-v2.2-root_prereg-FROZEN.md` (commit `f15a6e4d`, COMMIT 1 of this lane, pushed ALONE before any driver code existed and before any number produced by this instrument existed). All numbers above are read from the shipped `research/drivers/coldq_pole_v2p2_root_results.json` and are machine-verified against it by `research/drivers/coldq_pole_v2p2_root_number_check.py`, wired into `make verify`. Two full driver runs produced identical digests. **Predecessor lanes, all unmodified and byte-untouched by this lane:** PR #845 (MERGED at `052ccbba`, `SOLVER-NOT-CERTIFIED`); `research/2026-08-03_coldq-pole-v2_prereg-FROZEN.md` (commit `00724432`); `research/2026-08-03_coldq-pole-v2.1_prereg-FROZEN.md` (commit `7d8fe484`) and its result doc and driver (PR #854, OPEN, DO-NOT-MERGE, `SOLVER-NOT-CERTIFIED`). Mints no `clm-`/`def-`; propagates to no leaf; engine byte-untouched; falsification ledger untouched. Companion: the docket fragment `_orchestration/docket-entries/2026-08-03-coldq-v2p2-root.md`.
