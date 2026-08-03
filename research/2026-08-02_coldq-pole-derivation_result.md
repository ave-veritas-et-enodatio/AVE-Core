# The cold-Q pole derivation — RESULT: the instrument is NOT CERTIFIED, and the failures are properties of the instrument

**Date:** 2026-08-02
**Prereg-file**: research/2026-08-02_coldq-pole-derivation_prereg-FROZEN.md
**Driver:** [`research/drivers/coldq_pole_derivation.py`](drivers/coldq_pole_derivation.py) → [`research/drivers/coldq_pole_derivation_results.json`](drivers/coldq_pole_derivation_results.json)
**Number check:** [`research/drivers/coldq_pole_derivation_number_check.py`](drivers/coldq_pole_derivation_number_check.py) — gating via `make verify-lane-number-checks`
**Class:** DERIVATION result (research-doc; **mints no `clm-`/`def-`; propagates to no KB/manuscript leaf; changes no solidity; edits no falsification ledger**). Engine `src/ave` byte-untouched.
**Provenance:** Grant's GO, 2026-08-02, verbatim `[sic]`: `"6, GO"`. Written against `origin/main` = `ac165cf2`.

---

## HEADLINE

> **Certification: `SOLVER-NOT-CERTIFIED`. Frozen precedence therefore fires `BIN-F-SOLVER`, and NO physics bin is adjudicated.**
>
> Four of nine gates failed at their frozen tolerances (G4, G5, G7, G8) and one of six self-tests did not fire (FT-5). **All five outcomes are explained by TWO named mechanisms, and both are properties of the frozen INSTRUMENT — the prereg §4.2 real-`sigma` far-field matching method — not of the physics, and NOT of the controls, which did their job by firing:**
>
> - **M1 — the far-field matching is an ASYMPTOTIC (divergent) series**, so its truncation floor *falls* as `R_match` rises (§2.1);
> - **M2 — the ingoing-coefficient extraction is exponentially ill-conditioned as `exp(2|Im omega| R_match)`**, which *rises* as `R_match` rises (§2.2).
>
> The two run in **opposite directions in `R_match`**, which is why no single frozen `R_match` set can satisfy both. **Per-gate attribution: G4 and G5 are M1; G7 and FT-5 are M2; G8's residual spread is the non-cancelling remainder of M1 (§2.3).** A **third, independent** contamination source — a low-frequency divergence of the same series at the rectangle's left edge — was found by the PR #845 audit *after* this doc first shipped and is recorded in §2.4. The frozen tolerances (`1e-8`, `1e-9`) and the frozen search rectangle (`|omega_I| M_g` up to `1.00`) were written as if the far-field expansion were convergent and the extraction uniformly conditioned. Both assumptions are false, and the battery measured exactly that.
>
> **This is a clean instrument-failure result with a named mechanism — Rule 11's good shape, not a rescue candidate.** The physics numbers the battery produced are reported below as **NOT-ADJUDICATED DIAGNOSTICS** and carry **no bin verdict**, per the frozen precedence.
>
> **The five gates that DID pass are the load-bearing physics ones**, and two of them are new: the derived **spin-2** radial system reproduces the exact spherical-Hankel far field to `1.7688e-14` (G1), its **spin-2 energy weighting** reproduces the shot closed-cavity eigenvalue to `4.9220e-13` (G2) — and swapping in the **spin-1** weighting breaks that agreement by `21.7` percent (FT-6; the break is on the **recovered closed-cavity eigenfrequency**, not a measured `Q` shift on the open problem — see §5 item 1). **The #814 R7 spin-1-vs-spin-2 prerequisite is therefore not merely obeyed here; it is measured, and it is load-bearing.**

---

## §1 — What was frozen, and what the battery returned

**Frozen:** `any of G1..G9 FAILS, OR any of FT-1..FT-5 fails to fire` — the certification class `SOLVER-NOT-CERTIFIED`.
**Frozen:** `a gate that cannot fail is not a gate; if any self-test fails to fire, the certification is SOLVER-NOT-CERTIFIED regardless of how many gates passed`.
**Frozen:** `no adjudication criterion below may be dropped, widened or re-defined after any result is seen; no input in the section 3 ledger may be retuned; whatever the solver returns is banked`.

**No frozen criterion was dropped, widened, or re-defined. The gates are reported at the tolerances they were frozen at.**

### Gate table

| gate | what it certifies | frozen tol | measured | verdict |
|---|---|---|---|---|
| **G1** | spin-2 far-field series ↔ exact spherical Hankel at zero grade, 27 points | `1e-12` | `1.7688e-14` | **PASS** |
| **G2** | spin-2 energy functional ↔ shot closed-cavity eigenvalue (Rayleigh) | `1e-9` | `4.9220e-13` | **PASS** |
| **G3** | wall-terminus regularity + step convergence, `n_steps` 16000 → 64000 | `1e-8` | `3.5006e-10` | **PASS** |
| **G4** | matching-radius independence over `R_match` 25/40/60 | `1e-8` | `1.2377e-04` | **FAIL** |
| **G5** | series-order independence over `N` 12/20/28 | `1e-8` | `1.9488e-05` | **FAIL** |
| **G6** | Ax-3: CLOSED cavity spectrum is REAL; transfer coefficients real | `1e-10` | `0.0` exactly | **PASS** |
| **G7** | argument-principle count = number of located poles, refinement-stable | integer to `1e-3` | winding `28` (stable at all three samplings) vs `34` located | **FAIL** |
| **G8** | `nu_vac`-cancellation measured over `x_sat` 5/7/11 | `1e-9` | `Q` spread `1.1058e-08`; `Omega` spread `1.5560e-09` | **FAIL** |
| **G9** | determinism | identical digest | identical, `24bff544f53727ea` | **PASS** |

**Frozen:** `two independent full driver runs produce an identical results digest (SHA-256 over the results object minus timing fields)` — **two full runs were executed and their shipped objects are byte-identical apart from `_runtime_sec`.**

### Self-test table (each MUST fire)

| self-test | targets | frozen threshold | measured | fired? |
|---|---|---|---|---|
| **FT-1** corrupt one recursion coefficient by `1e-9` | G1 | `>= 1e-11` | `1.4191e-10` | **FIRES** |
| **FT-2** clamped inner wall instead of traction-free | the inner BC | `>= 1e-2` | `0.28430` | **FIRES** |
| **FT-3** smuggled loss `Im(mu)/Re(mu) = 1e-3` | G6 (Ax 3) | `>= 1e-5` | fires | **FIRES** |
| **FT-4** match at `R_match = 8` (inside the grade) | G4/G5 | `>= 1e-3` | `0.84243` | **FIRES** |
| **FT-5** winding on a pole-free box and on the closed-form zero-grade problem | G7 | box `0`, flat count exact | empty box `-2.5621e-16` ✓, flat-cavity winding `15.000` vs closed-form `1`/`1`/`2` ✗ | **DOES NOT FIRE** |
| **FT-6** *(ADDED — a strengthening, not a relaxation)* spin-**1** `l(l+1)` weighting in G2's Rayleigh quotient | G2 / the spin-2 discipline | `>= 1e-6` | `0.21729` | **FIRES** |

---

## §2 — THE MECHANISMS behind all five failures

The four failing gates and the unfired self-test are **not five independent problems**. They reduce to **two** mechanisms of the frozen instrument, M1 (§2.1) and M2 (§2.2), which the battery measured directly — plus a **third, independent** contamination source (§2.4) found by the PR #845 audit after this doc first shipped.

### §2.1 M1 — the far-field expansion is asymptotic, not convergent

The instrument's frozen far-field solution (prereg §4.2) is a series in `1/r` generated from the actual `mu(r)`, `rho(r)`. **That series is asymptotic: its error is minimised near an `R`-dependent optimal truncation and grows on BOTH sides of it.** The shipped `instrument_accuracy_map` measures this — deviation of the located pole from the best-available reference (`R_match = 60`, `N = 32`):

| `R_match` \ `N` | 8 | 12 | 16 | 20 | 24 | 28 | 32 | 36 |
|---|---|---|---|---|---|---|---|---|
| **25** | `5.9928e-04` | `9.1857e-05` | `6.5814e-05` | `1.2350e-04` | `5.0796e-04` | `4.0347e-03` | `5.5543e-02` | `2.3392e-01` |
| **40** | `7.0078e-04` | `1.8723e-05` | `2.1921e-06` | `8.1734e-07` | `4.3437e-07` | `4.9854e-07` | `1.4929e-06` | `5.2434e-06` |
| **60** | `5.2348e-03` | `3.2866e-05` | `7.7379e-07` | `4.6318e-08` | `1.2588e-08` | `5.6969e-09` | `0.0` | `7.4747e-09` |

Read the rows, not the cells:

- At `R_match = 25` the accuracy floor is `6.5814e-05` and the series then **diverges** — by `N = 36` the answer is `23` percent wrong. **No choice of `N` reaches `1e-8` at `R = 25`.**
- At `R_match = 40` the floor is `4.3437e-07`.
- At `R_match = 60` the floor reaches `1.2588e-08`–`5.6969e-09`.

**G4 and G5 fail for exactly this reason and for no other.** G4's frozen set contains `R = 25`, whose floor is four orders above the frozen `1e-8`. G5's frozen set contains `N = 12`, which at `R = 40` is far from optimal truncation. **The controls were designed for a convergent expansion, where "more terms is better" and "any `R` in the set is equivalent". For an asymptotic expansion both statements are false.** G3 independently proves the *integrator* is not the limit: `n_steps` 16000 → 64000 moves the pole by `3.5006e-10`, and a separate sweep found `8000` → `128000` agreeing to `1e-11`.

> **⚑ AS-RUN, NOT RE-DERIVABLE FROM THE SHIPPED ARTIFACTS (disclosed, PR #845 audit R8).** The `8000` → `128000` step sweep was run outside the shipped battery and its endpoints are **not** in `coldq_pole_derivation_results.json`; they are as-run prose. The gated number-check therefore allow-lists them rather than registering them. The G3 row in the gate table (`n_steps` 16000 → 64000, `3.5006e-10`) **is** shipped and registered, and it is the one that carries the gate.

### §2.2 M2 — the subdominant-coefficient extraction is exponentially ill-conditioned

With `Im omega < 0` the **outgoing** solution is the *dominant* one at large `r`, so the quasinormal condition asks for the *subdominant* ingoing coefficient to vanish. A relative integration error `delta` manufactures a spurious ingoing amplitude of order `delta * exp(2|Im omega| R_match)`. The prereg named this at §9 item 8 and froze `R_match` independence over a finite set rather than "arbitrarily large `R`" **because of it** — but it still froze a search rectangle reaching `|omega_I| M_g = 1.00`, where at `R_match = 40` the contamination factor is `exp(80)`. That region is pure roundoff.

The shipped `certified_omega_I_band` measures where the count is trustworthy:

| `wi_max` | 1.00 | 0.70 | 0.50 | 0.40 | 0.30 | 0.25 | 0.20 | 0.15 | 0.10 |
|---|---|---|---|---|---|---|---|---|---|
| winding | `28` | `27` | `27` | `5` | `4` | `4` | `4` | `4` | `3` |
| located inside | `34` | `34` | `34` | `2` | `1` | `1` | `1` | `1` | `0` |

**`largest_stable_wi_max` is `null`: no sub-rectangle in the frozen ladder satisfied "winding is a stable integer AND equals the located count".** The winding never drops to the located count even deep in the well-conditioned region, because the *contour itself* always includes the noise-dominated bottom edge.

**FT-5 is the clean proof, and it is why FT-5 not firing is the most informative single line in this battery.** On the zero-grade problem the traction-free condition reduces in closed form to a polynomial of degree exactly `ell+1`, so the root count inside the test box is known exactly: `1`, `1`, `2` for `ell = 1, 2, 3`. The measured winding is `15.000` for **all three** `ell`. That number is not random, and the PR #845 audit pinned down exactly what it is. **The identification is of a phase RATE, not of a count.** On the deep (noise-dominated) edge of the contour the objective's phase advances at `d(arg N)/d(omega_R) ≈ 2*R_match - a`, the optical length in radians per unit `omega` — measured to better than `4` percent across `R_match` in `{6, 8, 10, 12}`. The *count* is then `rate * Delta(omega_R) / (2*pi)`. **The count matched `2*R_match - a` only because the shipped FT-5 box happens to have `Delta(omega_R)` ≈ `2*pi`.** Audit receipts, as-run: widening the box at `R_match = 8` walks the winding through `8`, `12`, `15`, `20`; and at `R_match = 6` the winding is `10`, not the `11` that `2*R_match - a` would give. **A successor lane must therefore NOT treat `15` as a fixed signature of this artifact — the invariant is the phase rate `2*R_match - a`, and the count depends on the box width.** The physical content is unchanged: **on the noise-dominated part of the contour the phase of the objective tracks the phase of the cancelled large terms, not of the physical ingoing amplitude.** **Frozen:** `case (a) MUST return count 0 and case (b) MUST return count equal to the closed-form root count for ell in {1,2,3}` — case (a) returned `-2.5621e-16` (correct), case (b) did not. **FT-5 did its job: it detected that G7's instrument is untrustworthy, which is precisely what a fireability self-test exists to do.** G7's failure is the same fact seen from the other side: `34` located poles, of which all but one sit in the noise band.

### §2.3 G8 fails by a factor of 11 while CONFIRMING the physics it was built to test

**Frozen:** `Q, r_peak/r_sat and the overtone ratios are invariant to <= 1e-9 relative across x_sat in {5, 7, 11}, while omega_R*M_g scales as 1/x_sat to <= 1e-9 relative`.

| `x_sat` | `R_match` | `omega_R M_g` | `omega_I M_g` | `Omega = omega*r_sat/c_0` | `Q` |
|---|---|---|---|---|---|
| `5` | `28.571428571428573` | `0.37073131303835555` | `0.20145145121677233` | `1.8536565651917778` | `0.9201505146751939` |
| `7` | `40.0` | `0.2648080807146999` | `0.14389389410143283` | `1.8536565650028993` | `0.9201505121823758` |
| `11` | `62.857142857142854` | `0.16851423344429386` | `0.09156884260787314` | `1.8536565678872325` | `0.9201505045003425` |

`Omega` spread `1.5560e-09`; `Q` spread `1.1058e-08`; `r_peak/r_sat` spread `1.7511e-13`. **The gate FAILS at its frozen `1e-9`.** But read what it measured: **the scale-free eigenvalue and `Q` are `x_sat`-invariant to eight and nine significant figures.** The prereg's structural claim — that `Q` is *exactly* `nu_vac`-free because `r_sat` divides out of the radial system identically — is **CONFIRMED at the level this instrument can resolve.**

> **⚑ MIS-CITED FLOOR, corrected (PR #845 audit R5).** This paragraph originally cited the §2.1 map's `~1e-8` figure at `R_match = 60`. That is the wrong row. Under `scaled_geometry()` all three `x_sat` rows run at the **same scaled matching radius** `R_match/r_sat` = `5.714` — i.e. the `R_match = 40` row of the §2.1 map, whose floor is `4.3437e-07`, not `1e-8`. **The correction does not rescue the gate and does not change the reading:** because the three rows are the *same* scaled geometry, the truncation floor is **common-mode and largely cancels in the spread**, which is why the measured spread (`1.1058e-08`) sits more than an order BELOW the single-run floor. What survives the cancellation is the non-cancelling remainder of M1, and the frozen `1e-9` sits below *it*. **The gate still FAILS.**

> **⚑ A real bug this battery found in ITS OWN first run, recorded rather than quietly fixed.** The first full battery returned `Q` spreads of `1.74` on this gate — a `174` percent violation. The cause was **mine, not the physics**: `R_match` and the search rectangle were held fixed in units of `M_g` while `x_sat` varied, which puts the far-field match *inside the grade* at `x_sat = 11` (`R/r_sat = 3.64`) and breaks the numerics' scale invariance even though the physics' scale invariance is exact. Fixed by scaling `R_match` and the rectangle with `x_sat` (`scaled_geometry()`, [`coldq_pole_derivation.py:389-401`](drivers/coldq_pole_derivation.py)), and re-run. **This is a code-correctness repair, not a criterion change — the frozen G8 string is untouched and the gate still fails at it.** The first-run numbers are on the record here so the repair is auditable.
>
> **⚑ DISCLOSURE the audit is entitled to (PR #845 R5).** The prereg **did not freeze** how the geometry should follow `x_sat` — `scaled_geometry()`'s convention (hold `R_match` and the rectangle fixed in units of `r_sat`) is an **UNFROZEN implementation choice that was settled AFTER seeing G8 fail.** Post-failure settlement of an unfrozen degree of freedom is exactly the shape Rule 11 exists to police, so it is named here rather than left to inference. **Rule 11 is preserved not because the choice is defensible in the abstract, but because the frozen G8 criterion string is byte-untouched and the gate STILL FAILS at it: the continued failure, not the repair, is what keeps this clean.** Had the repair converted the FAIL into a PASS, this paragraph would be a rescue and the result would not be bankable.
>
> **⚑ AS-RUN, NOT RE-DERIVABLE FROM THE SHIPPED ARTIFACTS (PR #845 audit R8).** `1.74`, `174` and `3.64` are first-run (pre-repair) numbers. **The pre-repair driver was never committed**, so these three cannot be re-derived from anything in this branch and are not in the shipped JSON; they are as-run prose, allow-listed in the number check rather than registered. They are recorded for auditability of the repair, and nothing in the result depends on them.

### §2.4 M3 — a SECOND, INDEPENDENT contamination source at the rectangle's low-frequency edge (found by the PR #845 audit)

**Added after this doc first shipped. It does not change any gate verdict — every gate already FAILED — but it changes what a successor must fix, so it is recorded rather than left out.**

**M2 (§2.2) is not the only thing poisoning the contour.** The §4.2 far-field representation is generated by an asymptotic recursion in `1/(omega r)`, so its terms blow up as `omega_R -> 0` **at any `|omega_I|`, including zero**. The frozen scan rectangle's left edge is `omega_R M_g` = `0.02` (prereg §4.3), and the coefficient growth there is catastrophic: the audit measured the twentieth series coefficient at `|c_20| / R_match^20` = `5.06e+07` at `omega_R M_g` = `0.02`, `R_match` = `40` — the tail term is seven orders LARGER than the leading one, so the "solution" on that edge is not a solution at all.

**The receipt that this is independent of M2, as-run in the audit lane:** moving the contour's left edge from `0.02` to `0.20` — changing nothing else, and touching no part of the deep-`|omega_I|` edge that M2 owns — moves the winding from `3.0000` to `0.0000`, and both readings are stable across the frozen contour resolutions. **A count that is created and destroyed by the position of the LEFT edge is not counting poles.** M2's exponential contamination lives on the *bottom* edge and scales with `|omega_I|`; this one lives on the *left* edge and does not vanish as `|omega_I| -> 0`. Two different edges, two different scalings, two independent sources.

> **⚑ TWO DESIGN-TIME GAPS INSIDE THE FROZEN TEXT — disclosed, NOT edited.** The prereg is byte-untouchable and stays so. Both gaps are recorded here because a successor prereg that copies this one's shape would inherit them.
>
> 1. **G1's certification never covered the region the scan actually searches.** G1's frozen check set (prereg:205) has minimum `omega_R` = `0.4`; the frozen scan rectangle (prereg:193) reaches down to `omega_R M_g` = `0.02`. **That is a factor of twenty of uncovered frequency range, at the precise end where the series representation is worst.** G1 passed at `1.7688e-14` and certified nothing about where the instrument was about to be used. A certification set must cover the search domain, **including its corners**.
> 2. **The §9 feasibility check tested the wrong series.** §9 item 4 checks that "the `mu`, `rho` Taylor expansions converge at every frozen `R_match`" and measures `mu(z)` against its closed form to `2.2e-16`. **That series is convergent and irrelevant.** The series that failed is the *solution* series — the asymptotic far-field recursion built ON TOP of `mu(z)` — which is divergent by construction and was never exercised. **A feasibility check that exercises an input representation instead of the solution representation will pass while the instrument is broken.**

---

## §3 — THE FOUR FROZEN BINS: all four report `N/A — not adjudicated`

**Frozen:** `no adjudication criterion below may be dropped, widened or re-defined after any result is seen; no input in the section 3 ledger may be retuned; whatever the solver returns is banked`.

The frozen precedence is `BIN-F-SOLVER` > `BIN-F-PROFILE` > `BIN-F-NOPOLE` > `BIN-1/2/3/4`, with the instruction that if an earlier bin fires *"the later ones are reported as `N/A — not adjudicated` and no verdict language is used about them."* **`BIN-F-SOLVER` fired. Accordingly:**

| bin | frozen outcome |
|---|---|
| **BIN-1** (`omega_R M_g`) | **`N/A — not adjudicated`** |
| **BIN-2** (`Q`) | **`N/A — not adjudicated`** |
| **BIN-3** (radial localization / FORK-1) | **`N/A — not adjudicated`** |
| **BIN-4** (overtone ladder) | **`N/A — not adjudicated`** |
| **BIN-F-PROFILE** | did not fire — no canonical-input contradiction was encountered on the domain |
| **BIN-F-NOPOLE** | did not fire — a pole was located |
| **`nu_factor_verdict`** | **`N/A — not adjudicated`** (it is downstream of BIN-1) |

**No verdict language is used below.** The numbers in §4 are diagnostics.

---

## §4 — NOT-ADJUDICATED DIAGNOSTICS (numbers, no verdicts)

These are what the battery measured. They carry **no bin**, **no claim**, and **no solidity**. They are recorded so a successor lane with repaired controls has a target to confirm or refute, and so that nothing is lost by the honest closure.

### §4.1 The least-damped pole of the primary branch

Primary branch: `rho = rho_0`, `c_shear = c_0*sqrt(S)`, traction-free at `r_sat`, outgoing at infinity, `ell = 2`, zero free parameters.

| quantity | measured | numerical uncertainty (§2.1) |
|---|---|---|
| `omega_R M_g` | `0.2648080807146999` | `~4e-07` at the frozen `R_match = 40`; `~6e-09` at `R_match = 60` |
| `omega_I M_g` | `0.14389389410143283` | same |
| `Omega = omega*r_sat/c_0` (scale-free) | `1.8536565650028993` | same |
| `Q = omega_R/(2*abs(omega_I))` | `0.9201505121823758` | same |

Comparison quantities, computed from the shipped pole and the frozen comparators (**stated, not adjudicated**):

- against the frozen GR cold comparator `omega_R M = 0.37367` (read programmatically from `KERR_QNM[0.00]`): deviation `-29.13` percent.
- against the standing corpus shortcut `18/49`: deviation `-27.91` percent.
- `Q` against `Q_GR = 2.1002135791366907`: deviation `-56.19` percent.
- `Q` against the Op21 `2*pi`-convention `Q = ell = 2`: deviation `-54.0` percent. Distance to the convention value: `1.0798`. Distance to `Q_GR`: `1.1801`. **Which of the two the measured `Q` sits nearer is BIN-2's frozen discriminator, and it is NOT evaluated here** — `BIN-F-SOLVER` fired, so the two distances are recorded as diagnostics and are not compared.
- `k_0*r_sat = 1.8537` against the standing chain's asserted `ell*(1+nu_vac) = 2.5714`.

> **★ The IDENTITY the prereg froze BEFORE any number existed, and it holds.** **Attribution, corrected after review (PR #845 R8):** what the prereg froze (prereg:284) is the **literal-`7`** form, `k_0 r_sat = 7 * omega_R M_g`. The `x_sat`-generalized form `k_0*r_sat = x_sat * omega_R M_g` used elsewhere in this doc is **this document's trivial generalization of it**, not a frozen string, and it is the frozen literal-`7` form that carries the pre-registration. Either way the content is the same: the "9/7-above-cutoff" test **is** the `omega_R` vs `18/49` comparison re-expressed, not an independent axis. Both read `-27.91` percent. The prereg recorded this in advance precisely so it could not be presented afterwards as two corroborating results. **It is one.**

### §4.2 Radial localization

Both frozen measures agree exactly and both place the maximum at the **outer** edge of the frozen window `r/r_sat` in `[1.0, 2.0]`: `u_energy = 1.9997126071429716`, `u_kinetic = 1.9997126071429716`, `interior_max = false`. The mode-energy density at the wall is `0.04058976258552422` of the window maximum.

**Read honestly, this measurement is dominated by a generic property of quasinormal eigenfunctions, not by substrate physics:** a QNM amplitude grows as `exp(|omega_I| r)` outward, which over this window is a factor of `e^(1.007)` in amplitude before the `r^2` measure is applied. The prereg reserved a `BIN-3-MONOTONE` sub-bin for "the maximum sits at an endpoint, so localization is not a well-posed observable for this mode"; **whether that sub-bin applies is NOT adjudicated here, because `BIN-F-SOLVER` fired first.**

**FORK-1 is NOT adjudicated. The diagnostic that would have fed it is recorded above, and nothing more** — no statement is made or implied about where the mode lives, and the turning-point comparator `r*/r_sat = 1.2247` is listed in the prereg's frozen comparator set without being evaluated against anything here.

### §4.3 Overtones

Within the region where the extraction is conditioned there is **one** pole. The next located pole, `omega M_g = 0.12509420853469172 - 0.3805502556171569i`, sits inside the band §2.2 shows is roundoff-dominated and **is not credible**. No overtone ratio is reported, because reporting one would require trusting a number this battery's own self-test says cannot be trusted.

### §4.4 Frozen sensitivities and diagnostics

- **FORK-2 KEEP-BOTH (`S^{1/4}` Family-E counterfactual).** **Frozen:** `the S^{1/4} counterfactual is reported as a sensitivity, never as the primary result, and no bin is adjudicated on it`. Measured: `omega M_g = 0.06457835191289236 - 0.07921459609905164i`, `Omega = 0.45204846339024657`, `Q = 0.40761649426415175`. **Low confidence** — the same conditioning limits apply, and this branch was not separately gated.
- **`ell`-ladder.** **Frozen:** `DIAGNOSTIC — no bin, no verdict; FORK-12 is unanswered and this lane does not adjudicate it`. *(The shipped JSON carries the ASCII transliteration of the same tag, `DIAGNOSTIC - no bin, no verdict; ...`, because the driver writes plain-ASCII JSON; the frozen label above is the prereg's own bytes.)* Measured `Omega`: `ell = 2` → `1.8536565656172288`, `ell = 3` → `2.5138625055232238`, `ell = 4` → `0.5197786125250078`, `ell = 5` → `0.4852927998939722`. **The `ell = 4` and `ell = 5` rows are not credible** — they break the monotonic rise in `Omega` that `ell = 2, 3` show, which is the signature of the seed-selection having picked a noise root. Recorded, not interpreted. **FORK-12 remains unanswered and is not adjudicated here.**
- **Clamped-wall diagnostic (FT-2 by-product).** Replacing the canonical SHORT by a clamped terminus moves the pole by `0.28430` relative. **The canonical `Gamma_shear = -1` free surface is load-bearing in the answer, not decoration** — which is #814's CF-13 ("the sign is Q-neutral in the loss ledger and Q-relevant through the frequency") with a number attached for the first time.

---

## §5 — WHAT THIS LANE DID ESTABLISH (the gates that passed are not nothing)

1. **★ The spin-2 discipline is discharged AND measured.** The #814 R7 prerequisite was *"derive the spin-2 spherical-mode impedance; do NOT import the spin-1 one."* **Frozen:** `the radial system is the toroidal (odd-parity, exactly divergence-free) branch derived from the shear-channel continuum equations; the radial functions coincide with spherical Hankel functions in the homogeneous limit but the impedance relation T = mu(W' - W/r) and the (l-1)(l+2) stored-energy weighting are the spin-2 ones and no spin-1 vector-multipole impedance is imported anywhere in this lane`. G1 confirms the radial functions do coincide (`1.7688e-14`); G2 confirms the spin-2 energy weighting is the Euler–Lagrange partner of the integrated system (`4.9220e-13`); and **FT-6 shows the spin-1 `l(l+1)` weighting breaks that agreement by `0.21729`.** **Scope, tightened after review (PR #845 R8):** `0.21729` is the relative break in the **recovered closed-cavity eigenfrequency** that G2's Rayleigh quotient reproduces. It is **not** a measured `Q` shift on the open (radiating) problem — no such shift was computed by this battery, and none is claimed. Scoped that way the claim stands: the distinction is not bookkeeping, because substituting the spin-1 weighting moves the eigenfrequency that `Q` is *built from* by `22` percent.
2. **The wall terminus is reached exactly, with no regulator.** **Frozen:** `the wall is reached exactly via the r = r_sat + sigma^2 substitution, which makes the two-component system analytic at sigma = 0; the initial condition is exactly (W,T) = (1,0) and no offset, series start, or regularized modulus floor is used`. G3 measures `3.5006e-10`. **The `A = 1` point is handled as a regular singular point of the ODE whose indicial structure selects the traction-free branch — not by a floor on `S`.**
3. **Ax-3 losslessness is structural, not asserted.** G6: every closed-cavity eigenvalue is real to `0.0` exactly and the assembled transfer carries zero imaginary part; FT-3 shows a smuggled `Im(mu)/Re(mu) = 1e-3` is detected. **The only loss in the ledger is the radiative port** — #814's CF-11 instantiated.
4. **FORK-10 and FORK-11 are dissolved as designed.** **Frozen:** `no port-Q is computed and no port-to-pole transfer is performed; the reported Q is the pole-Q that the GR comparator is`. Neither disputed spin-1 estimator was used and the `50` percent estimator spread recorded in #814 §1.3 never entered.
5. **`Q`'s `nu_vac`-freedom carries a unit-covariance receipt** (§2.3) — the three `x_sat` runs agree on `Omega` and `Q` to eight and nine significant figures. **Downgraded after review (PR #845 R5):** this is *a unit-covariance receipt for a cancellation the prereg establishes analytically*, **not** an independent measurement of that cancellation. Under `scaled_geometry()` the three `x_sat` runs are **the same problem in scaled units by construction**, so what the agreement certifies is that the code respects the scaling it was told to respect. That is worth having — it would have caught the first-run bug — but it is weaker than the #808 §2.1 requirement (*"cancellation is the actual requirement"*) taken at full strength, and this doc no longer claims otherwise.

---

## §6 — FLAG-DON'T-FIX: what is routed, and to whom

**Nothing below is repaired here.**

1. **★ The frozen controls G4/G5/G7 and the frozen rectangle are mis-specified for this problem class — routed to Grant and the auditor lane.** Their *tolerances* assume a convergent far-field expansion and a uniformly conditioned subdominant extraction; neither holds. **This is a statement about what the controls would need to be to CERTIFY this instrument, not a complaint about them — as detectors they worked, which is why this lane returns a clean negative instead of a number.** **It is NOT a request to loosen them.** The correct successor controls are *different in kind*, not looser:
   - (i) **optimal-truncation** agreement (does the answer sit on the plateau of its own `N`-sweep at each `R`, and do the plateaux agree across `R`?) rather than fixed-order agreement;
   - (ii) a **measured** conditioned band rather than an assumed rectangle;
   - (iii) for the winding count, a contour that does not traverse the noise floor, or a method that does not require one;
   - (iv) **ADDED after the PR #845 audit (§2.4):** **bound the search rectangle's left edge away from `omega_R -> 0`, or adopt a representation with no low-frequency divergence at all.** The `1/(omega r)` asymptotic recursion is unusable at the frozen left edge `omega_R M_g` = `0.02` regardless of `|omega_I|`, so a rectangle that reaches it cannot be certified by any tolerance choice.
   - Two structural requirements on the *battery* itself, also from §2.4: **certification must cover the FULL search rectangle including its corners** (G1 certified down to `omega_R` = `0.4` while the scan ran to `0.02`), and **feasibility checks must exercise the SOLUTION representation, not an input representation** (§9 item 4 measured the convergent `mu(z)` Taylor series and never touched the divergent solution series that actually failed).
   - **Already transmitted.** All four controls and both structural requirements were passed to the in-flight successor (`v2`) lane by the orchestrator on 2026-08-03, so the successor does not have to rediscover them. **That transmission is a routing act, not an adoption: this lane adjudicates nothing about `v2` and `v2` inherits no certification from here.**

   Per Rule 12 the slot is **not refilled**: a successor lane needs a **new prereg with a new version number and its own verification chain**, not an edit to this one.
2. **A method upgrade that would reach deeper, deliberately NOT taken here.** Complex-rotating the radial contour (`r = r_sat + exp(i*theta)*s`) inverts the dominance so the quasinormal condition lands on the *dominant* solution and the extraction becomes well-conditioned. **It was not used, because the prereg froze the real-`sigma` method and changing the method mid-lane after seeing failures is the move the discipline exists to prevent.** Routed as the leading candidate for the successor prereg.
3. **#814 CF-7's naming gap stands, untouched.** `vol3/claim-quality.md:122` writes `Z_shear = rho c_shear` and never names which `rho`. This lane consumed the leading reading (`rho_0`, cold lattice inertia) as a frozen input and did **not** repair the leaf.
4. **FORK-3(b), FORK-5 (spheroidal branch), FORK-9's formal half and FORK-12 all remain open**, exactly as the prereg fenced them. **FORK-12 must be answered by Grant before any `ell`-ladder verdict is banked anywhere.**
5. **The `Q = ell` anchor is untouched.** **Frozen:** `a derived cold Q that disagrees with the B1-ratified Q = ell anchor is routed to Grant as a flag; no solidity, ruling or leaf is changed by this lane`. Since **no bin was adjudicated**, there is not even a disagreement on the record to route — only a non-adjudicated diagnostic. `qnm-quality-factor.md`, `op21-multi-mode-mode-counting.md` and `regime-eigenvalue-method.md` are byte-untouched.

---

## §7 — RUNTIME AND SCOPE DISCLOSURES

- **Frozen:** `total battery runtime <= 900 s on the reference machine; a longer run is disclosed, not silently accepted`. **Disclosed: the battery took longer than the frozen budget.** The shipped `_runtime_sec` records it. The budget is not an adjudication criterion and no result depends on it.
- **Disclosed implementation choices**, neither of which touches a frozen criterion: (i) seed refinement inside `find_poles` runs at the scan step count, and every reported pole is re-polished at the frozen `N_STEPS_POLISH = 64000` before it is used; (ii) the instrument-accuracy map runs at the scan step count, which G3 measures is not the accuracy limit.
- **`_runtime_sec` is machine-dependent and is deliberately NOT registered** in the number check (the #801 R3/WARN-4 lesson: registering a machine-dependent numeral makes the checker fail on every honest re-run).

---

## §8 — CORRECTIONS AFTER REVIEW (PR #845 audit, dated 2026-08-03)

**Nothing below changes a gate verdict, a bin, or the certification class.** The verdict was and remains `SOLVER-NOT-CERTIFIED` with all four physics bins `N/A — not adjudicated`. These are corrections to *this document's language and completeness*, landed in the repair pass. **The frozen prereg is byte-untouched, and so is the driver `coldq_pole_derivation.py`** — the only executable edited in the repair is the number check's allow-list.

| # | audit finding | what changed |
|---|---|---|
| **F1** | verdict language leaked into §4.2 despite `BIN-F-SOLVER` firing | the leaking clause **REMOVED** (quoted below); the FORK-1 routing restated as *not adjudicated* |
| **F2** | BIN-2's discriminator was evaluated in prose | the comparative sentence **REMOVED** (quoted below); both distances kept and tagged as the frozen, unevaluated discriminator |
| **F3** | a second contamination source, and two design-time gaps, were missing | **§2.4 ADDED**; §6 item 1 extended with a fourth successor control and two structural requirements |
| **F4** | FT-5's `15` was presented as a fixed signature | §2.2 restated as a phase-**rate** identification with its box-width dependence; the number check's allow-list reason for `15` corrected |
| **F5** | the `x_sat`-scaling convention's unfrozen status was undisclosed; §5 item 5 overclaimed; §2.3 cited the wrong accuracy-map row | disclosure added to the bug banner; §5 item 5 downgraded; the floor corrected to the `R_match/r_sat` = `5.714` row |
| **F6** | blame was assigned to the controls | headline and title retitled to the **instrument**; the single mechanism split into M1/M2 with per-gate attribution |
| **F7** | two commits lack the `Co-Authored-By` trailer | **recorded, NOT repaired** — see the docket fragment; rewriting would destroy the frozen-first SHA evidence chain |
| **F8** | prose-only numerals, coverage wording, an identity mis-attribution, FT-6 scope | as-run disclosures added; number-check wording fixed; the identity attributed to the result doc's generalization; FT-6 scoped to the closed-cavity eigenfrequency |

**Rule 12 — the withdrawn text, preserved verbatim so the correction is auditable.** Both passages are **WITHDRAWN**. They are reproduced here as history, not as content.

> **🔴 WITHDRAWN (F1, §4.2).** *"**the reserved bin turned out to be the relevant one.** Had bins been adjudicated, this is where BIN-3 would have landed, and it would have said that the derived mode is **neither** a rim ring at `r_sat` **nor** a ramp mode at the `r*/r_sat = 1.2247` turning point."*
> **Why withdrawn:** the frozen precedence says that when an earlier bin fires *"the later ones are reported as `N/A — not adjudicated` and no verdict language is used about them."* A counterfactual verdict is still a verdict. The measurement it rested on (no interior maximum; both measures agree at the outer window edge) and the QNM `exp(|omega_I| r)` caveat are **kept**, because they are diagnostics.

> **🔴 WITHDRAWN (F2, §4.1).** *"The measured `Q` is nearer the convention value than the GR value (distances `1.0798` and `1.1801`)."*
> **Why withdrawn:** "nearer which comparator" **is** BIN-2's frozen discriminator. Stating it in prose evaluates a bin the precedence forbids evaluating. Both distances are **kept** as unevaluated diagnostics.

> **🔴 SUPERSEDED (F6, headline).** *"**All five outcomes have a single named mechanism**, and it is a property of the frozen *controls*, not of the physics"* — and the original title, *"one mechanism explains every failure"*. **Why:** the failing behaviour is a property of the frozen **instrument** (the §4.2 real-`sigma` far-field method). The controls are what **detected** it. And there are two mechanisms, opposed in `R_match`, not one — with a third contamination source found later (§2.4).

> **🔴 SUPERSEDED (F5, §5 item 5).** Withdrawn verbatim, byte-for-byte as it stood: "to eight significant figures, which is the strongest form of the #808 §2.1 requirement (*"cancellation is the actual requirement"*) yet produced in this arc." **Why:** under `scaled_geometry()` the three `x_sat` runs are the same problem in scaled units by construction, so the agreement is a **unit-covariance receipt**, not an independent measurement of a cancellation the prereg already establishes analytically.

---

> **Result provenance.** Resolves the frozen bins of `research/2026-08-02_coldq-pole-derivation_prereg-FROZEN.md` (COMMIT 1, pushed before any driver code existed). All numbers above are read from the shipped `research/drivers/coldq_pole_derivation_results.json` and are machine-verified against it by `research/drivers/coldq_pole_derivation_number_check.py`, which is wired into `make verify`. Two full driver runs produced identical digests. Mints no `clm-`/`def-`; propagates to no leaf; engine byte-untouched; falsification ledger untouched. Companion: the docket fragment `_orchestration/docket-entries/2026-08-02-coldq-pole.md`.
