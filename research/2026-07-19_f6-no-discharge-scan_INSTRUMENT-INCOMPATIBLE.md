# F6 NO-FULL-DISCHARGE calibration scan — Phase 0 — **INSTRUMENT-INCOMPATIBLE** (DO NOT FIRE)

**Date:** 2026-07-19 · **Class:** research finding — Phase-0 instrument calibration (pre-prereg; **DISCLOSED as calibration**). **No prereg was frozen and no grid was fired** — the scan returned outcome **(c)**, so per its own rails the lane **stops here**.
**Driver:** `src/scripts/vol_1_foundations/f6_no_discharge_scan.py` · **Data:** `2026-07-19_f6-no-discharge-scan_result.json`
**Instrument:** `src/ave/thermal/f6_bath_meter.py` (`LatticeBathCoupler`, `OscillatorBath` — **BYTE-UNTOUCHED**; only constructor args passed). **Reused BYTE-UNTOUCHED:** `f6_counting_arrow_arm.py` (#722 `_seed_lattice` / grid / `_m_for`).
**Certificate:** `METER-VALID-KAPPA-BAND[0.030,0.030]` @ MILD (PR #724, standalone-K4). **Origin:** the follow-on SPEC'd in PR #726 result §6 route-1 (`research/2026-07-18_f6-certified-kappa-sweep_result.md`, branch `feat/f6-certified-kappa-sweep`).

> ## ★ OUTCOME — **(c) INSTRUMENT-INCOMPATIBLE.** DO NOT FIRE.
>
> On the **certified instrument** (effective coupling `κ_eff = κ·g0 = 0.030` exactly) there is **NO operating cell** that reaches the counting regime **without** full discharge. The two conditions the follow-on must co-satisfy — **counting-regime-live** (fast transfer `t63/T_rec ≤ 0.5` **and** populated quasi-continuum `N_occ ≥ 10`) and **no-full-discharge** (`peak_frac ≤ 0.85` **and** the `scale=0` clamp never fires) — are governed by the **single effective coupling** `κ_eff` and are **mutually exclusive** on this instrument. Every in-scope quasi-continuum comb (`N_occ ≥ 10`) **fully discharges and clamps**; every clamp-free comb has `N_occ ≤ 3` (regime-not-reached). `USABLE cells = 0`.
>
> The **one** cell that trips the three raw transfer conditions (`g0=0.5`, `Δω=0.010`) is **doubly disqualified** on two **pre-existing** grounds: it runs at `κ_eff = 0.015` — the exact `(κ,g0)` degeneracy makes it **bit-identical** to `κ=0.015`, **outside** the certified single-point band and inside the region the task fenced out (`NOT κ ≠ 0.030`) — **and** it has `N_occ = 4 < 10`, which the prereg's own frozen regime gate scores as **REGIME-NOT-REACHED** (question **unasked**). It is reported for transparency, **not** frozen upon.
>
> **The clamp is not an engineerable artifact at the certified cell.** #726's §6 route-1 premise — "no meter-mechanism change is needed; an operating point that populates `N_occ ≥ 10` **without** driving `E_bath → E0` clears both blockers" — is **falsified by this scan**: no such in-scope operating point exists (§5, §7). The **argmax half** of #726's repair IS fixable (first-plateau; reimplemented here, §2) and survives; the **clamp half** is not, without either κ < 0.030 (out of the certified band) or a meter back-reaction edit — both explicitly fenced out (§8).
>
> **Nothing banked at emergence-class.** The counting-arrow question stays **OPEN** (undecided, not falsified) — this scan shows only that it **cannot be asked** on the existing instrument at the certified cell with the two artifacts removed by configuration alone. Depletion-rate rung (`Γ=3Hρ_latent`) and the #721/#724 certificates untouched. No meter/engine edit.

---

## 0 · Sector header + certificate scope + the FENCE

- **Sector:** E-sector ε-store (F6 ε→T2 candidate). **NOT** A1 dilatation-mass, **NOT** Cosserat (2,3) winding/charge. Bath = external Foster/Caldeira–Leggett oscillator comb (a T2 sink DOF; carries no winding/mass; sector-ownership respected).
- **Mode:** classical reactive K4 TLM lattice (z=3 srs, 4 ports) + external comb via a collar port; symmetric-leapfrog (the meter's `LatticeBathCoupler.step`).
- **Regime:** Regime I sub-yield, `A_max ≈ 0.10` MILD, at `κ = 0.030` (the certified point). `g0` (the uniform per-mode weight) is varied; `κ_eff = κ·g0`.
- **Phase-state:** driven-then-source-off, closed cavity (`pml=0`, energy-conserving).
- **Plant:** STANDALONE-K4 — within the meter certificate (#721 R-1 SCOPE CAVEAT; conservation is an algebraic identity on this junction).
- **★ HARD FENCE (stated and honored):** the scan measured **TRANSFER quantities ONLY** — `peak_frac` (first-plateau), `t63/T_rec`, clamp-fire, and the regime-side `N_occ` (a spectral occupancy read — the prereg's own "is the regime reached" gate, **not** the return/collapse answer). It **NEVER** computed `R_return`, return-timing, `x_50`, `R_cum`, or the cross-comb collapse. The collapse observable is not defined anywhere in the scan driver, so it **cannot** have been tuned on. (Verified by grep: the strings `R_return`, `x_50`, `r_cum`, `collapse` appear **only** in fence/comment prose in `f6_no_discharge_scan.py`, never as a computed quantity.)
- **Consistency-vs-emergence tag:** this is an **instrument-feasibility** finding (Class-4 consistency / calibration), not a physics claim. No CODATA input, no emergence claim, no headline VALUE.

---

## 1 · What was asked (the #726 §6 route-1 follow-on)

PR #726 fired the SUFFICIENT counting-arrow collapse test at the certified cell and returned **FOREIGN-EATER / question-not-decided**, with a post-review diagnosis (result §2–§7) that **two artifacts ate the signal**:

1. **The argmax observable (R-1).** `t_peak = argmax_t E_bath` landed on the **post-clamp plateau** (`E_bath ≡ E0`), so `R_return ≡ 0` over the whole run — erasing the recurrence-timed partial returns the raw trace actually held. Repaired by the **first-plateau** reading.
2. **The `scale=0` back-reaction clamp (R-2).** `scale = √(max((E_lat − d_e_bath)/E_lat, 0))` **hard-zeroes the lattice** when a step's `d_e_bath ≥ E_lat` — an **absorbing state** (`E_lat ≡ 0` thereafter). Two of the three dense combs clamp-died (`NO-INFORMATION`), driving `grid_return_min = 0`.

#726 §6 route-1 SPEC'd the cheapest decisive next lane: **the corrected observable + a NO-FULL-DISCHARGE operating point on the EXISTING instrument** — "weaker κ within/below the certified band, or a rate-limited/per-mode-capped back-reaction that never zeroes `E_lat`." This lane's task **fences both of those out** (`NOT κ ≠ 0.030`, `NOT engine/meter edits`) and asks: can a no-full-discharge cell be reached by **instrument-configuration** knobs alone (per-mode weights `g0`, comb bandwidth/placement, window design)?

**This scan answers that question. It cannot.**

---

## 2 · The scan design (knobs, grids, conditions) — fence honored

- **Knob scanned:** uniform per-mode coupling weight `g0` (`OscillatorBath.g0`, `f6_bath_meter.py:102`) — the meter is BYTE-UNTOUCHED (`g0` is a constructor arg). `G0_GRID = {1.0, 0.7, 0.5, 0.35, 0.25}` ⇒ `κ_eff ∈ {0.030, 0.021, 0.015, 0.0105, 0.0075}`.
- **Density grid (spanning a decade):** `Δω ∈ {0.008, 0.010, 0.013, 0.016, 0.020, 0.030, 0.050, 0.080}` (0.008→0.080 = a decade; ≥3/decade). Band top held at `ω_max ≈ 1.0`; `M = round(0.70/Δω)+1`; Nyquist `ω_max·dt < π` for every row.
- **Window:** the **full** `11·T_rec` (the clamp must **never** fire over the *whole* prereg window; runs early-stop the instant the clamp fires, since post-clamp is dead).
- **First-plateau observable (transfer health only):** `_first_plateau_idx` + `_clamp_onset` **reimplemented** from the PR #726 branch `feat/f6-certified-kappa-sweep` (cited; NOT cherry-picked). `peak_frac` = first-plateau `E_bath/E0` (the honest transfer, not the clamp-plateau artifact); `t63` = first step `E_bath ≥ (1−1/e)·E_bath_firstplateau`.
- **The three scan conditions (a cell "satisfies" iff ALL):** `transfer_live` (`t63/T_rec ≤ 0.5`), `no_full_discharge` (`peak_frac ≤ 0.85`), `clamp_never` (`E_lat` never `≤ 10⁻¹²` over the full window). `N_occ ≥ 10` is **reported** (the prereg regime floor), and folded into the **usable** call below.

---

## 3 · ★THE CENTRAL SCOPE FINDING — the `(κ, g0)` degeneracy (measured, bit-identical)

In the meter the coupling enters **only** as the product `κ·g` (`f6_bath_meter.py:198`, `self.p += dt * kappa * self.g * q`; `self.g = g0` flat). `κ` appears **nowhere else**. So `κ` and a uniform `g0` are **exactly degenerate** — the entire coupled `(lattice + bath)` trajectory is a function of `κ·g0` alone. Measured (`degeneracy_check()`):

| run | `κ` | `g0` | `κ_eff` | `E0` | `max|ΔE_bath|` vs ref | `N_occ` |
|---|---|---|---|---|---|---|
| A | 0.030 | 0.5 | 0.015 | 2.141433 | — | 4 |
| B | 0.015 | 1.0 | 0.015 | 2.141433 | **0.0 (bit-identical)** | 4 |

`(κ=0.030, g0=0.5)` is **bit-for-bit identical** to `(κ=0.015, g0=1.0)`: `max|ΔE_bath| = 0`, `max|ΔE_lat| = 0`, `N_occ` identical, `E0` identical.

**Consequence (flagged for review to adjudicate — task rail).** Scaling `g0` down to soften the discharge is **not** "gentler at fixed κ." It is a **reduction of the effective coupling `κ_eff = κ·g0` below the certified single-point band** `[0.030,0.030]`, and it lands **inside** the region the task explicitly fenced out (`NOT κ ≠ 0.030`). A "no-discharge cell" found via `g0 < 1.0` is a no-discharge cell at `κ_eff < 0.030` — **off the certified instrument**. The task's own framing ("weaker per-mode coupling at fixed κ = strictly gentler") is **in tension with the code reality** (the kick's `κ·g0` degeneracy); this scan surfaces the tension and does **not** resolve it by fiat. **Routed to the review / Grant.**

---

## 4 · The scan (full table; the in-scope reality boxed)

`peak` = first-plateau `E_bath/E0`. `t63/Trec` = transfer timescale. `minElat` = min `E_lat/E0` over the physical window. `clampx` = `x` at clamp onset (`--` = never). Flags: **T**ransfer-live (`t63/Trec≤0.5`), **P**artial (`peak≤0.85`), **C**lamp-never, **N**occ≥10.

**★ IN-SCOPE (`g0=1.0`, `κ_eff=0.030` — the certified instrument):**

| `Δω` | `M` | `peak` | `t63/Trec` | `N_occ` | `minElat/E0` | `clamp x` | flags |
|---|---|---|---|---|---|---|---|
| 0.008 | 88 | 1.000 | 0.124 | **18** | 1.6e-6 | 1.00 | `T--N` (clamps) |
| 0.010 | 71 | 0.995 | 0.193 | **15** | 1.8e-7 | 3.15 | `T--N` (clamps) |
| 0.013 | 55 | 0.992 | 0.323 | **12** | 3.4e-5 | 5.17 | `T--N` (clamps) |
| 0.016 | 45 | 1.000 | 0.489 | 9 | 2.9e-4 | 1.38 | `T---` (clamps) |
| 0.020 | 36 | 1.000 | 0.783 | 8 | 2.7e-5 | 1.72 | `----` (clamps) |
| 0.030 | 24 | 0.919 | 2.268 | 3 | 8.1e-2 | -- | `--C-` |
| 0.050 | 15 | 0.183 | 0.565 | 3 | 8.1e-1 | -- | `-PC-` |
| 0.080 | 10 | 0.169 | 1.324 | 1 | 8.3e-1 | -- | `-PC-` |

**In-scope: raw-satisfying = 0, USABLE = 0.** Every `N_occ ≥ 10` comb (`Δω ≤ 0.013`) has `peak → 1.0` **and** clamps. Every clamp-free comb (`Δω ≥ 0.030`) has `N_occ ≤ 3` **and** `t63/Trec > 0.5`. No cell is even `[T P C]`, let alone `[T P C N]`.

**OUT-OF-SCOPE (`g0 < 1.0`, `κ_eff < 0.030`; degeneracy = a κ-reduction):** the only cell tripping the three raw conditions anywhere is **`g0=0.5, Δω=0.010`** (`peak=0.732`, `t63/Trec=0.474`, clamp-never) — flags `[T P C -]`, **but** `N_occ = 4` and `κ_eff = 0.015`. Full per-cell rows are in `…_result.json`.

| `g0` | `κ_eff` | in-scope? | raw-satisfying | USABLE (+scope +N_occ≥10) |
|---|---|---|---|---|
| 1.00 | 0.030 | **yes** | 0 | 0 |
| 0.70 | 0.021 | no | 0 | 0 |
| 0.50 | 0.015 | no | 1 (`Δω=0.010`) | 0 |
| 0.35 | 0.0105 | no | 0 | 0 |
| 0.25 | 0.0075 | no | 0 | 0 |

---

## 5 · ★THE INCOMPATIBILITY — one mechanism, mutually-exclusive conditions

**One root (single effective coupling).** Because `(κ, g0)` collapse to the single knob `κ_eff = κ·g0` (§3), the three regime conditions are **all monotone in `κ_eff`** and pull in **opposite directions**:

- **`κ_eff` large enough for the quasi-continuum** (`N_occ ≥ 10` — the counting arrow needs many incommensurate phases to dephase) ⇒ the transfer is fast **and completes** (`peak → 1.0`) ⇒ `E_lat → 0` ⇒ a single step's `d_e_bath ≥ E_lat` ⇒ **the `scale=0` clamp fires**. (In-scope: `Δω ≤ 0.013`.)
- **`κ_eff` small enough for partial transfer** (`peak_frac ≤ 0.85`, clamp-never) ⇒ **under-populated** (`N_occ ≤ 4`, few-mode) ⇒ **REGIME-NOT-REACHED**; and the transfer is also **slow** (`t63/T_rec > 0.5`, gate fails).

**The threshold coincidence.** On the certified instrument the **quasi-continuum threshold** (`N_occ ≥ 10`) and the **full-discharge/clamp event** are crossed at the **same comb density** (`Δω ≈ 0.013`): `Δω = 0.013` reads `N_occ = 12` **and** clamps at `x=5.17`; `Δω = 0.016` drops to `N_occ = 9` and still clamps; `Δω = 0.020` is `N_occ = 8` and clamps; only by `Δω = 0.030` (`N_occ = 3`) is the clamp avoided. **There is no gap** between "populated" and "discharged." At `κ_eff = 0.030`, quasi-continuum transfer **is** full discharge — the clamp is the instrument **faithfully reporting** that the lattice fully drained, not a numerical pathology to be engineered around.

**This is honest closure (Rule 11): a single mechanism explains every scan cell.** The `(κ,g0)` degeneracy + the monotone coupling of `{N_occ, peak_frac, t63/T_rec}` in `κ_eff` forces the mutual exclusivity. No retune, no goalpost-move, no rescue.

---

## 6 · Outcome (c) — DO NOT FIRE (literal-vs-honest, disclosed)

The task's outcome triage: **(a)** a satisfying family (≥4 densities, ≥ a decade) → freeze + fire; **(b)** partial (fewer densities) → freeze on what exists; **(c)** NO cell satisfies → bank + stop.

**Literal reading:** exactly **one** cell trips the three transfer conditions (`g0=0.5, Δω=0.010`). Pedantically that is not "zero."

**Honest reading (the one banked):** that lone cell is **disqualified on two independent, pre-existing grounds** — **neither** is a post-hoc criterion:

1. **Out of certificate scope.** `κ_eff = 0.015` (via the §3 bit-identical degeneracy). The task fence is `NOT κ ≠ 0.030`; the certified band is the single point `[0.030,0.030]`. This is **the task's own κ fence**, not a new gate.
2. **REGIME-NOT-REACHED.** `N_occ = 4 < 10` — the **inherited #726 frozen regime gate** (`NOCC_GATE=10`). A fire there returns REGIME-NOT-REACHED by the frozen taxonomy: the counting-arrow question is **UNASKED**, not answered.

So **no cell satisfies the conditions AND stays on the certified instrument AND reaches the counting regime** (`USABLE = 0`). Freezing a prereg on the lone raw-satisfier would burn the freeze on a **guaranteed REGIME-NOT-REACHED, off the certified instrument** — the opposite of "freeze on what exists." **The finding is (c): INSTRUMENT-INCOMPATIBLE.** DO NOT FIRE. The literal-vs-honest tension is disclosed here and flagged for the review, per flag-don't-fix.

---

## 7 · Flag-don't-fix — correction to #726 §6 route-1 (surfaced, not silently resolved)

The #726 result §6 route-1 (and §3 corrected-mechanism) states, verbatim:

> "The amount channel demonstrably converts the recurrence into a return (R-1/R-3), so **no meter-mechanism change is needed to make progress** — the blockers were (a) the read and (b) the absorbing clamp, both cleared by an operating point that populates `N_occ ≥ 10` **without** driving `E_bath → E0` (weaker κ within/below the certified band, or a rate-limited / per-mode-capped back-reaction …)."

**This scan falsifies the "no meter change needed" claim under the task's fences.** There is **no** in-scope operating point that populates `N_occ ≥ 10` without driving `E_bath → E0` (§4/§5): the two are the **same event** at `κ_eff = 0.030`. #726's route-1 quietly relied on **exactly** the two escapes the task fences out — "weaker κ … below the certified band" (= the degenerate `g0 < 1.0`, out of the single-point band) and "a rate-limited / per-mode-capped back-reaction" (= a **meter edit**). Remove both and route-1 is **infeasible**. The **argmax half** of the #726 diagnosis stands and is reusable (first-plateau; reimplemented, §2); the **clamp half** is not clearable by configuration alone.

**Both file paths, verbatim, for adjudication** (per flag-don't-fix — surfaced, not reframed):
- #726 result claim: `research/2026-07-18_f6-certified-kappa-sweep_result.md` §6 route-1 (branch `feat/f6-certified-kappa-sweep`) — "no meter-mechanism change is needed."
- This scan's contradicting measurement: `research/2026-07-19_f6-no-discharge-scan_result.json` → `in_scope_quasicontinuum_all_clamp = true`, `totals.n_usable = 0`.

Routed to the auditor lane / Grant. **Not** silently edited into #726 (open PR).

---

## 8 · What would resolve it (SPEC only — routed, NOT built; each earns its own charter + verification chain)

The no-discharge quasi-continuum cell requires escaping the single-knob `κ_eff` bind. The only two mechanisms that do so are **exactly the two the task fences out**, so each is a genuine, scoped SPEC — not this lane's to build:

- **R1 — Re-certify the meter at a κ-band below 0.030 (own charter + full X-battery revalidation).** The degeneracy (§3) means the no-discharge quasi-continuum window, if it exists at all, lives at `κ_eff < 0.030` (e.g. the `g0=0.5, Δω=0.010` cell — but at `N_occ=4`, so a *wider* comb / lower `ω_min` may be needed to lift `N_occ` at fixed `κ_eff`). This is **not** in-scope here (the certified band is the single point `[0.030,0.030]`; #724 excluded `κ≥0.045`, and `κ<0.030` was never certified for the meter's discriminators). SPEC: a `κ`-descent re-certification (X1–X6 at each new point) to establish a `METER-VALID-KAPPA-BAND` that *contains* a no-discharge quasi-continuum cell — **if one exists**; the scan's monotone structure (§5) suggests `N_occ≥10` and `peak≤0.85` may **never** co-exist at any single `κ_eff`, in which case R1 also fails and the true resolution is R2.
- **R2 — Build + certify a rate-limited / per-mode-capped back-reaction primitive (a meter edit ⇒ breaks the #721 R-1 identity ⇒ full W/X-battery revalidation).** A back-reaction that **never zeroes `E_lat`** (caps `d_e_bath` per step at `< E_lat`, or returns phase not amount) removes the absorbing clamp **without** reducing `κ_eff` — so the quasi-continuum can populate at `κ=0.030` and still leave a live lattice to recur into. This is the physically-correct fix but is a **meter-mechanism change** (fenced out here), and it breaks the conservation identity, so it demands its own charter + the full W/X + A/B/C certificate chain. (This is #726 §6 route-1's *other* escape, made explicit.)
- **R3 — The argmax fix is done and reusable.** The first-plateau observable (`_first_plateau_idx`, reimplemented here + in the #726 repair) is the correct, unambiguous read and needs no further work; whichever of R1/R2 is pursued inherits it.

**Untouched:** the depletion-rate rung (`Γ=3Hρ_latent`); the #721/#724 meter certificates (byte-untouched; standalone-K4 identity intact); the meter module + K4 engine (byte-untouched).

---

## 9 · Independent re-derivation + gates + provenance

- **Independent re-derivation of the outcome from the raw banked series (the #726 F9 lesson — NOT the classifier's own booleans).** `src/tests/test_f6_no_discharge_scan.py` loads `…_result.json` and, using **only** the raw per-cell fields (`kappa_eff`, `peak_frac`, `t63_over_trec`, `n_occ`, `clamp_fires`) — **not** `satisfies_scan` / `n_usable` / `outcome` — re-derives: (i) `usable = (κ_eff==0.030) ∧ (t63/T_rec≤0.5) ∧ (peak≤0.85) ∧ ¬clamp ∧ (N_occ≥10)` count **= 0**; (ii) every in-scope `N_occ≥10` cell has `clamp_fires = True`; (iii) the lone raw-satisfier is out-of-scope AND N_occ<10. It **also** runs `degeneracy_check()` **live** and asserts bit-identity, and runs one **live** in-scope densest comb (short horizon) and asserts full discharge (`peak > 0.85`, `min E_lat/E0 < 0.05`). The independent re-derivation reproduces the driver's `C_INSTRUMENT_INCOMPATIBLE`.
- **Fence honored (re-verified).** No `R_return` / `x_50` / `R_cum` / collapse quantity is computed anywhere in the scan driver — only transfer quantities + the regime-side `N_occ`.
- **Diagnostics provenance (F9):** every scan number is computed by the shipped driver and banked in `…_result.json` (per-cell `peak_frac`, `t63_over_trec`, `n_occ`, `min_elat_frac`, `clamp_fires`, `clamp_x`, `frac_dead`, `max_cons_drift`; the degeneracy trajectories' max-abs-diff; per-`g0` raw/usable counts; the disqualified-raw-satisfiers list). Nothing prose-only.
- **Conservation:** every non-clamping cell conserves `E_lat+E_bath` to the identity floor (banked `max_cons_drift`); clamping cells' drift is clamp-created (the R-2 disclosure), not integrator error.
- **Gates:** `ruff check` clean; `make verify` green; the fast test suite green (`test_f6_no_discharge_scan.py`).

---

*Honest closure (Rule 11): the NO-FULL-DISCHARGE operating point does **not exist** on the certified instrument by configuration alone. A single mechanism — the `(κ,g0)` bit-identical degeneracy collapsing the knobs to one effective coupling `κ_eff`, in which the quasi-continuum threshold and the full-discharge/clamp event coincide — explains every scan cell. Outcome **(c) INSTRUMENT-INCOMPATIBLE**; the lane **stops** (no prereg frozen, no grid fired). The counting-arrow question stays **OPEN** (cannot be asked here), the argmax-observable half of #726's repair survives and is reusable, and the two mechanisms that would resolve it (a κ-band re-certification, or a rate-limited back-reaction primitive) are **SPEC only** — each the task explicitly fences out of this lane. Nothing banked at emergence-class.*
