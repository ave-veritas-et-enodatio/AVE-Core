# The cold-Q pole v2.4 — RESULT: `ROOT-CERTIFIED`. Twelve of twelve gates pass, twelve of twelve self-tests fire — and the certified cavity does **not** ring where GR rings

**Date:** 2026-08-03
**Prereg-file**: research/2026-08-03_coldq-pole-v2.4-root_prereg-FROZEN.md
**Prereg-commit**: 36186006 (frozen and pushed ALONE, before any driver code and before any number produced by this instrument existed)
**Driver:** [`research/drivers/coldq_pole_v2p4_root.py`](drivers/coldq_pole_v2p4_root.py) → [`research/drivers/coldq_pole_v2p4_root_results.json`](drivers/coldq_pole_v2p4_root_results.json)
**Number check:** [`research/drivers/coldq_pole_v2p4_root_number_check.py`](drivers/coldq_pole_v2p4_root_number_check.py) — gating via `make verify`
**Class:** DERIVATION result (research-doc; **mints no `clm-`/`def-`; propagates to no KB/manuscript leaf; changes no solidity; edits no falsification ledger**). Engine `src/ave` byte-untouched.
**Provenance:** Grant's standing ruling of 2026-08-03 — **certify the located root, not the rectangle.** Written against `origin/main` = `184db4b6`.

---

## HEADLINE

> **Certification: `ROOT-CERTIFIED`.** All twelve gates PASS; all twelve fireability self-tests FIRE. **The frozen precedence therefore reaches the physics bins for the first time in this arc, and they are adjudicated.**
>
> **★ AND THE PHYSICS RESULT IS A CLEAN, LARGE NEGATIVE.** The graded saturation cavity's `ℓ = 2` toroidal shear pole, computed with **zero free parameters**, sits at `ω_R M_g = 0.2648078872629827` and `Q = 0.9201502744197102`. Against the frozen GR comparators that is **`BIN-1-MISS`** (`D_omega = -0.2913322255921462`, a `29.1 %` shortfall) and **`BIN-2-MISS`** (`D_Q = -0.5618777615951112`, a `56.2 %` shortfall). **Neither is close. Both are reported plainly.**
>
> **The `(1+ν_vac)` rider FIRED.** Frozen in advance: `if BIN-1's derived omega_R*M_g deviates from 18/49 by more than 3 percent, the standing chain's r_eff = r_sat/(1+nu_vac) assertion is FALSIFIED as a derivation of the eigenfrequency, and that is a GOOD outcome recorded as such`. Measured deviation from `18/49`: **`-0.2791340846729915`**, i.e. `27.9 %` — nine times the trip level. **The rider fires and the assertion is falsified as a derivation of the eigenfrequency.**
>
> **`BIN-3` lands in the ill-posed bin that was reserved for it in advance: `BIN-3-MONOTONE`.** The mode-energy density has **no interior maximum** in the frozen window; both frozen measures put the maximum at the outer edge, `u_energy = u_kinetic = 2.0000000000000004`, with the wall holding `0.040561477092864194` of the window peak.
>
> **★ THE GATE THIS LANE WAS BUILT ON PASSED ON THE RIGHT LAW.** G2b fits the **root-exponential** law `E(n) = C·exp(−c·sqrt(n))` and measures `c = 6.216374478994577` inside the frozen band `[4.4, 7.6]`, with `max|residual| = 0.08484862390265135` against a frozen floor of `0.40`. **Pointed at the v2.1-banked pseudo-pole the identical routine returns `c = 0.25002341694486013` and would NOT pass** — the law discriminates the root from the artifact.
>
> **AND THE `n = 32` RUNG IS REPORTED, NOT HIDDEN.** Its measured error is `1.2496816369074884e-10`; the law — fitted on `{48, 64, 80}`, which never saw that rung — predicts `2.2779698805088156e-10` **out of sample**, a ratio of `1.822840164432575`. **Both exceed the frozen `1e-10`.** The law placed the ladder before the measurement confirmed it.

---

## §1 — THE GATE TABLE (measured against frozen; nothing dropped, widened or re-defined)

**Frozen:** `no gate, tolerance, band, frozen numeric parameter or method element in sections 4 and 5 may be changed after any gate result is seen; if this instrument fails certification the lane reports ROOT-NOT-CERTIFIED and routes to its own successor with a new version number`.

**No frozen criterion was dropped, widened, or re-defined. Every gate is reported at the tolerance it was frozen at.**

| gate | what it certifies | frozen tol | measured | verdict |
|---|---|---|---|---|
| **G0** | operator-transcription identity, `𝓛_η ≡ 4η²·𝓛_A` | `1e-13` | `1.038488291045556e-15` | **PASS** |
| **G1** | residual of the certified eigenfunction at the certified root (mp, `dps = 50`) | `1e-20` | `4.726832751705419e-50` | **PASS** |
| **G2** ★ | `n`-independence over the **certification ladder** `n ∈ {48, 64, 80, 96}`, shipped as `[48, 64, 80, 96]` | `1e-10` | `8.090607956292325e-14` | **PASS** |
| **G2b** ★ | the **root-exponential convergence law**, both parameters gated | `max\|resid\| ≤ 0.40` **and** `c ∈ [4.4, 7.6]` | `0.08484862390265135` and `c = 6.216374478994577` | **PASS** |
| **G3** | hyperboloidal-gauge independence, `λ ∈ {−0.25, 0, +0.25}` | `1e-12` | `3.332294747541498e-14` | **PASS** |
| **G4** | (a) precision `dps 50` vs `80`; (b) double-pencil vs mp at every FULL-ladder order | `1e-25` / `1e-6` | `5.277782707837865e-47` / `1.755941633596894e-08` | **PASS** |
| **G5** ★ | **ISOLATION** — pencil-eigenvalue count within `R_iso = 0.5`, **full ladder incl. `n = 32`** | exactly `1` | `[1, 1, 1, 1, 1]` | **PASS** |
| **G6** | two-instrument agreement vs the v1 shipped root | `1e-5` | `6.803231574438666e-07` | **PASS** |
| **G7** | spin-2-vs-spin-1 at the root: (a) eigenvalue, (b) eigenfunction | `1e-3` both | `0.28423799223517354` / `0.19696614906560894` | **PASS** |
| **G8** | `ν_vac` cancellation at the root, **mp end-to-end** | `1e-9` | `1.8618720608205777e-46` | **PASS** |
| **G9** | determinism | identical digest | `6cec005e0155513a` twice | **PASS** |
| **G10** | Ax-3 (a) operator reality, (b) conjugate-mirror symmetry | `1e-40` / `1e-20` | `0.0` exactly / `9.273121713408482e-47` | **PASS** |

### ★ The `n = 32` NON-GATED DIAGNOSTIC ROW — mandatory, and nothing about it is hidden

**Frozen:** `the n = 32 rung is reported as a NON-GATED DIAGNOSTIC row of G2, shipping its polished root as mp strings, its relative separation from every rung of the certification ladder, the maximum pairwise relative separation over the FULL five-rung ladder, and the G2b-fitted law's own OUT-OF-SAMPLE prediction for e(32) printed beside the measured e(32); the result doc MUST print this row in its gate table, and the certification outcome does NOT depend on it`.

| quantity | value |
|---|---|
| `Ω(32)`, mp strings | `1.853655211103967150148849766702804665292` `-1.00725678315784204770526531401798871333` |
| measured `e(32)` vs the `n = 96` reference | `1.2496816369074884e-10` |
| **law's OUT-OF-SAMPLE prediction** for `e(32)` (fit never saw this rung) | `2.2779698805088156e-10` |
| predicted / measured | `1.822840164432575` |
| **both exceed the frozen `1e-10`?** | **`true`** |
| max pairwise over the FULL five-rung ladder (the quantity v2.2's G2 gated on) | `1.2496816389659964e-10` with `\|Ω_k\|` in the denominator (this doc's convention, the shipped `full_ladder_max_pairwise`) — **and `1.2496816388248957e-10` with `\|Ω_i\|`, which is the number v2.2 published**; both are the same `32 ↔ 80` separation under the **two orderings of the relative-separation denominator**, they differ in the 10th significant figure, and **the successor should freeze the symmetric form** `\|Ω_i − Ω_k\| / max(\|Ω_i\|, \|Ω_k\|)` so the quantity stops depending on which rung is named first |
| would that FULL-ladder quantity pass the `1e-10` tolerance? | **`false`** — under either denominator |

**Read plainly: `n = 32` still fails a `1e-10` `n`-independence test, exactly as v2.2 measured — and the convergence law, fitted without it, said so in advance to within a factor of `1.82`.** The rung is excluded from G2 because the law places it below the asymptotic regime, **not** because excluding it was convenient. It remains a **gated** rung of G4(b), G5, FT-5(a) and FT-5(b): **G4(b) and G5 PASS at that rung, and FT-5(a) and FT-5(b) FIRE at it** — a self-test does not "pass", it fires, and a rung that made a self-test *pass* would be a rung that broke it.

### Self-test table (each MUST fire)

| self-test | targets | frozen threshold | measured | fired? |
|---|---|---|---|---|
| **FT-0** `𝒞₀` corrupted `1e-12` | G0 | `≥ 1e-13` | `2.0668129728690202e-12` | **FIRES** |
| **FT-1** residual off-root at `Ω(1 + 1e-10)` | G1 | `≥ 1e-15` | `9.946402719819208e-12` | **FIRES** |
| **FT-2** under-resolved `n = 8` | G2 | `≥ 1e-6` | `0.000440375300940382` | **FIRES** |
| **FT-2b** ★ STAGNATION `+1e-12` on every non-reference rung | G2b | fitted `c` must fall below `4.4` | fitted `c` = `0.07345138526200583` | **FIRES** |
| **FT-3** correctly-specified half-applied gauge | G3 | `≥ 1e-6` | `0.3485948410197033` | **FIRES** |
| **FT-4** (a) `dps = 20`; (b) double pencil at `n = 8` vs mp at `n = 48` | G4 | `≥ 1e-25` / `≥ 1e-6` | `4.316731050519307e-17` / `0.0004403753009474462` | **FIRES** |
| **FT-5** ★ (a) on the v2.1 artifact; (b) on the v2.1 contaminated-edge probe | G5 | count `≠ 1` at ≥ 1 order | `[2, 1, 2, 3, 0]` / `[1, 1, 0, 0, 0]` | **FIRES** |
| **FT-6** `𝒞₀` corrupted `1e-3`, vs the v1 comparator | G6 | `≥ 1e-5` | `0.0005872196298821127` | **FIRES** |
| **FT-7** ★ **differently-coded EQUIVALENT** spin-2 spec on both axes | G7 | both `< 1e-3`, and an exact `0.0` must be reported | `1.5015831404915055e-46` / `4.440892098500626e-16` — **neither exactly zero** | **FIRES** |
| **FT-8** `x_sat`-dependent profile perturbation | G8 | `≥ 1e-9` | `6.013720615540751e-07` | **FIRES** |
| **FT-9** one gate value perturbed `1e-15` in a copy, re-digested | G9 | digest must change | `75d7fc892e625892` → `95676d738972694d` | **FIRES** |
| **FT-10** smuggled `Im(μ)/Re(μ) = 1e-3` | G10 | `≥ 1e-6` / `≥ 1e-5` | `0.03167549395692262` / `0.0005836018036712878` | **FIRES** |

**Frozen:** `a gate that cannot fail is not a gate; if any self-test fails to fire, the certification is ROOT-NOT-CERTIFIED regardless of how many gates passed`. **Every self-test fired.**

---

## §2 — THE CONVERGENCE LAW: GATED, AND IT DISCRIMINATES

**Frozen:** `G2b fits ln e(n) = lnC - c*sqrt(n) by ordinary least squares over the G2 certification rungs n in {48, 64, 80} with e(n) the relative separation of Omega_star(n, 0.0, 7.0, 50) from Omega_star(96, 0.0, 7.0, 50), and requires BOTH that the maximum absolute residual in ln e is <= 0.40 AND that the fitted c lies in the frozen band [4.4, 7.6]`.

### §2.1 The fit on the certified root

| rung `n` | `e(n)` vs the `n = 96` reference | residual in `ln e` |
|---|---|---|
| 48 | `8.090599741070316e-14` | `-0.039741` |
| 64 | `1.1708996452296386e-16` | `0.084849` |
| 80 | `2.9026479440283196e-19` | `-0.045108` |

```
fitted c    = 6.216374478994577          band [4.4, 7.6]        IN BAND
fitted lnC  = 12.962558101032272
max|resid|  = 0.08484862390265135        floor 0.40             INSIDE
```

The fit's intercept is `12.962558101032272`. **The successive ratios are reported and are NOT gated on:** `690.9729432434473` and `403.39016918622724`. **Frozen:** `the convergence law of this instrument is ROOT-EXPONENTIAL, E(n) = C*exp(-c*sqrt(n)); the successive-error ratio therefore DECLINES with n by construction, and a declining ratio sequence is the law's signature rather than evidence of any defect`. **This is the repair of the defect that killed v2.3's freeze: those declining ratios are the law's signature, and a constant-ratio gate would have been testing a law this instrument does not obey.**

### §2.2 ★ The law discriminates the root from the pseudo-pole — a pre-registered, non-gating receipt

**Frozen:** `the artifact-centred convergence fit is a PRE-REGISTERED, NON-GATING DIAGNOSTIC; it is shipped and reported, it enters no gate and no bin, and no certification outcome depends on it`.

The **identical** fit routine, pointed at the v2.1-banked discretization artifact `Ω_art` over the **same** certification ladder:

| centre | `e(48)` | `e(64)` | `e(80)` | fitted `c` | `max\|resid\|` | would pass G2b? |
|---|---|---|---|---|---|---|
| **the certified root** | `8.090599741070316e-14` | `1.1708996452296386e-16` | `2.9026479440283196e-19` | `6.216374478994577` | `0.08484862390265135` | **yes** |
| **the v2.1-banked artifact** | `0.4634575039104712` | `0.4611632142706101` | `0.27680695848541004` | `0.25002341694486013` | `0.17911773057438807` | **no** |

**The pseudo-pole's error does not decay: it sits at `O(0.3–0.5)` at every order, and the fitted `c = 0.25002341694486013` is a factor of `17.6` below the frozen band's lower edge.** The certified root's `c` sits mid-band. **One routine, two objects, twenty-five-fold separation in the law's own parameter.** This is what G2b buys over a bare tolerance, and it is why the gate was worth adding.

### §2.3 What the law says about `n = 32`, and the honest limit of that statement

Fitted over the **full** five-rung ladder including `n = 32`, the law gives `c` = `6.043847309998414` with `max|resid|` = `0.18870776957898983` — **which would also pass G2b's `0.40` floor.**

**And the law itself is not exactly constant-`c`, which is the honest reason the out-of-sample prediction over-shot.** The three pairwise estimates the prereg fitted on drift **monotonically upward** — `5.775382`, then `6.100131`, then `6.354001` — so `c` is still creeping with `n` rather than having settled. A three-point fit over `{48, 64, 80}` therefore carries a slightly-too-large `c` when it is extrapolated one rung *downward* to `n = 32`, and it over-predicts `e(32)` by the factor `1.822840164432575` reported in §1. **That is a property of the fit, not a defect in the rung**, and the frozen band absorbs it by construction: the `±1.0` widening is far larger than the `0.578619` total drift across the whole pairwise sequence, and the G2 tolerance derivation is anchored at the band's **upper** edge `7.6` — the fastest-convergence corner, which yields the *smallest* worst-case error and is therefore the **conservative** choice against exactly this drift.

**Stated plainly, because it runs against the convenient reading: the `n = 32` rung is not an outlier to the LAW. It is pre-asymptotic in MAGNITUDE.** Its error obeys the same root-exponential decay; that error is simply still larger than `1e-10` at that order. **The prereg said this in advance** — `G2b gates the LAW, not the presence or absence of any rung` — and the ladder placement rests on the out-of-sample magnitude prediction of §1, not on `n = 32` violating anything.

---

## §3 — THE PRE-REGISTERED EXPECTATIONS, CHECKED

**Frozen:** `these six expectations are stated BEFORE the run so that agreement is recorded as a REGRESSION CHECK and any disagreement is recorded as a DEFECT and surfaced with both numbers; no expectation is a gate, none may be used to adjust a measurement, and a disagreement is reported rather than reconciled`.

| # | expectation, frozen at `36186006` | measured | verdict |
|---|---|---|---|
| 1 | the certified root reproduces `1.8536552108408788 − 1.0072567831433188i` | identical to all shown digits | **MET** |
| 2 | G2 measures `≈ 8.09e-14` | `8.090607956292325e-14` | **MET** |
| 3 | G2b's `c` lands near `6.2`, residual near `0.085` | `6.216374478994577` / `0.08484862390265135` | **MET** |
| 4 | the `n = 32` diagnostic reads `≈ 1.2497e-10` against an out-of-sample prediction of `2.277976e-10` | `1.2496816369074884e-10` / `2.2779698805088156e-10` | **MET** |
| 5 | every unchanged gate reproduces v2.2's published value | G0 `1.0385e-15`, G1 `4.7268e-50`, G3 `3.3323e-14`, G4 `5.2778e-47`/`1.7559e-08`, G5 `[1, 1, 1, 1, 1]`, G6 `6.8032e-07`, G7 `0.28424`/`0.19697`, G8 `1.8619e-46`, G10 `0.0`/`9.2731e-47` — **all reproduced at the precision v2.2 published** | **MET** — a REGRESSION CHECK, **not** corroboration (§6) |
| 6 | FT-7's differently-coded equivalent returns `~1e-16 … 1e-13`, **not** exactly `0.0` | `(b) = 4.440892098500626e-16` in range; **`(a) = 1.5015831404915055e-46`, non-zero but 30 orders BELOW the stated range** | **PARTIALLY MET — the deviation is DISCLOSED below, not smoothed** |

### ★ Expectation 6's deviation, reported as a defect in the expectation rather than explained away

**The expectation was wrong, and the reason is mine.** I wrote `~1e-16` for both axes as if both were double-precision paths. **They are not.** FT-7(b) — the reversed-association quadrature — *is* a double-precision path, and it returned `4.440892098500626e-16`, which is **two** units in the last place of a double near `1.0`, not one: a double's ULP at `1.0` is `2.220446049250313e-16`, and the measured value is exactly twice it. *(Corrected 2026-08-03 under adversarial review; the original read "exactly one unit in the last place of a double". The correction changes no measured value and no verdict.)* **FT-7(a) — the closed-form CGL corner entry versus the negative-sum diagonal — is built in `50`-digit mp, where the two analytically identical constructions agree to `~1e-46`, not `~1e-16`.** The measured `1.5015831404915055e-46` is therefore the *correct* magnitude for the arithmetic actually used, and my stated range was derived from the wrong precision.

> **🔴 ATTRIBUTION CORRECTION 2026-08-03 (added under adversarial review) — HALF OF FT-7(b)'s STATED MUTATION IS VACUOUS.** FT-7(b) has been described in the docket and the PR body as *"`ell**2+ell-2` weight with reversed-association quadrature"*, as though the re-written weight contributed arithmetic separation. **It contributes none.** The primary weight is `(ELL - 1) * (ELL + 2)` and the alternative is `ELL**2 + ELL - 2`; at `ℓ = 2` both are Python integers equal to `4`, computed exactly, so the two expressions are **bit-identical by construction** and cannot differ by any amount. **The reversed-association quadrature is the entire live path** — the whole of the measured `4.440892098500626e-16` comes from it. The self-test still fires and its purpose still holds, because a genuinely different summation order *is* a different arithmetic path; but the mutation is **one** change described as two, and the attribution is corrected rather than left to flatter the self-test.

**What matters for the gate is unaffected and is the point of the repair:** both values are **non-zero**, so the two code paths did **not** collapse, and FT-7 is now exercising a genuinely different implementation of the same mathematical specification rather than re-running the same branch. **Frozen:** `both differences between the differently-coded equivalent specification and the primary one MUST be below 1e-3; and if either returns EXACTLY 0.0 the result doc MUST record that the two code paths collapsed and that the intended arithmetic separation did not materialise`. **Neither axis returned exact zero; the collapse condition did not occur, and both differences are below `1e-3`.**

---
## §4 — THE BINS, ADJUDICATED — the first time in this arc that any of them has been

**Frozen:** `no adjudication criterion below may be dropped, widened or re-defined after any result is seen; no input in the section 3 ledger may be retuned; whatever the instrument returns is banked`.

The frozen precedence is `BIN-F-NOROOT` > `BIN-F-ROOT` > `BIN-F-PROFILE` > `BIN-1/2/3`. **None of the three failure bins fired**, so the physics bins are adjudicated.

| bin | outcome |
|---|---|
| **`BIN-F-NOROOT`** | **did not fire** — a root was located at every order of the full ladder |
| **`BIN-F-ROOT`** | **did not fire** — twelve of twelve gates PASS, twelve of twelve self-tests FIRE |
| **`BIN-F-PROFILE`** | **did not fire** — no canonical-input contradiction was encountered on the domain |
| **BIN-1** (`ω_R M_g`) | **`BIN-1-MISS`** |
| **BIN-2** (`Q`) | **`BIN-2-MISS`**; discriminator **`BIN-2-CLOSER-CONVENTION`** |
| **BIN-3** (radial localization / FORK-1) | **`BIN-3-MONOTONE`** |
| **BIN-4** (overtone ladder / completeness) | **`N/A BY CONSTRUCTION`** |

### §4.1 The certified root and its projections

| quantity | value |
|---|---|
| `Ω = ω·r_sat/c₀`, mp strings | `1.853655210840878848320699157729883961213` `-1.00725678314331889260211374956072904467` |
| the same root cast to double, `Re(Ω)` then `Im(Ω)` | `1.8536552108408788` `-1.0072567831433188` |
| `\|Ω\|` | `2.109645436528558` |
| `ω_R M_g = Re(Ω)/x_sat` | `0.2648078872629827` |
| `ω_I M_g = \|Im(Ω)\|/x_sat` | `0.14389382616333127` |
| `Q = Re(Ω)/(2\|Im Ω\|)` | `0.9201502744197102` |

### §4.2 BIN-1 — `ω_R M_g` against the frozen GR comparator

**Frozen:** `BIN-1-MISS` is `abs(D_omega) >= 0.10`.

| quantity | value |
|---|---|
| `ω_R M_g` derived (zero free parameters) | `0.2648078872629827` |
| `ω_R M_g` GR comparator (I11, read programmatically) | `0.37367` |
| `D_omega = derived/GR − 1` | `-0.2913322255921462` |
| **verdict** | **`BIN-1-MISS`** |

**Class line (mandatory, frozen):** `BIN-1 is VALUE-CONSISTENCY class, not emergence: omega_R*M_g carries the GR-imported nu_vac through the 7 in r_sat`.

**And the `(1+ν_vac)` rider FIRED.** **Frozen:** `if BIN-1's derived omega_R*M_g deviates from 18/49 by more than 3 percent, the standing chain's r_eff = r_sat/(1+nu_vac) assertion is FALSIFIED as a derivation of the eigenfrequency, and that is a GOOD outcome recorded as such`.

| quantity | value |
|---|---|
| corpus shortcut `18/49` | `0.3673469387755102` |
| `D_omega_shortcut = derived/(18/49) − 1` | `-0.2791340846729915` |
| trip level | `0.03` |
| **rider** | **FIRED — `nu_vac_rider_falsified = true`** |

**Read plainly.** The standing corpus chain asserts `r_eff = r_sat/(1 + ν_vac)` and thence `ω_R M_g = 18/49`. **The graded cavity's actual `ℓ = 2` toroidal pole, computed from the canonical profile with nothing to tune, is `27.9 %` below that.** Per the criterion frozen before the run, **that assertion is falsified as a derivation of the eigenfrequency.** This is recorded as the good outcome the prereg said it would be: a pre-registered criterion fired against the corpus, and the corpus is what moved.

**The advance identity, restated so one result is not presented as two.** **Frozen:** `k_0*r_sat = x_sat * omega_R M_g identically, so the 9/7-above-cutoff test IS the omega_R versus 18/49 comparison re-expressed and is NOT an independent axis`. `k₀·r_sat = 1.8536552108408788`, which is `x_sat · ω_R M_g` identically. **Not a second axis; the same number.**

### §4.3 BIN-2 — `Q`, the `ν_vac`-free axis

**Class line (mandatory, frozen):** `BIN-2 is the nu_vac-FREE axis: Q = Re(Omega)/(2*abs(Im(Omega))) contains no r_sat scale, so the GR-imported 7 cancels exactly`. **G8 measures that cancellation at `1.8618720608205777e-46`.**

| quantity | value |
|---|---|
| `Q` derived | `0.9201502744197102` |
| the two frozen GR comparator inputs (I11, read programmatically) | `0.37367` and `0.08896` |
| `Q_GR = 0.37367/(2·0.08896)` | `2.1002135791366907` |
| `D_Q = derived/Q_GR − 1` | `-0.5618777615951112` |
| **verdict** | **`BIN-2-MISS`** |

**The three-way discriminator.**

| quantity | value |
|---|---|
| `\|Q − Q_GR\|` | `1.1800633047169806` |
| `\|Q − 2.0\|` | `1.07984972558029` |
| **verdict** | **`BIN-2-CLOSER-CONVENTION`** |

> **⚑ FLAG-1 exercised, and it does NOT bite.** **Frozen:** `the BIN-2 three-way discriminator is robust to the FLAG-1 comparator ambiguity unless Q_derived lands inside the window between 2.0497191011235955 and 2.0501067895683455; the result doc MUST report whether it does, and if it does the discriminator is reported as AMBIGUOUS rather than adjudicated`. The measured window is `2.0497191011235953` to `2.0501067895683454`; `Q = 0.9201502744197102` is **far outside it** (`BIN_2_flag1_ambiguous = false`). **The discriminator is adjudicated, not ambiguous.**

**Read plainly, and read carefully — this is the axis where the honest reading is easiest to overstate in either direction.** `Q` is the **only** emergence-capable axis in this lane, and it **misses GR by `56.2 %`**. The three-way discriminator formally lands `CLOSER-CONVENTION`, but **that verdict must not be dressed up as support for `Q = ℓ = 2`**: `Q = 0.920` is `1.08` away from `2.0` and `1.18` away from `2.100`. **It is nearer to the corpus convention only in the sense that a number far from both is marginally nearer one of them.** The frozen criterion is a strict comparison and it has been applied strictly; the physical content is that **the cold graded cavity is a much lower-`Q` resonator than either standing value.**

### §4.4 BIN-3 — where the mode lives

**Frozen:** `BIN-3-MONOTONE` is `the energy density has no interior maximum in the frozen window (the maximum sits at an endpoint)`.

| quantity | value |
|---|---|
| `u_energy = r_peak/r_sat` (full spin-2 energy density) | `2.0000000000000004` |
| `u_kinetic` (kinetic term alone) | `2.0000000000000004` |
| interior maximum? | `false` |
| wall energy density as a fraction of the window peak | `0.040561477092864194` |
| frozen window | `1.0` to `2.0` |
| **verdict** | **`BIN-3-MONOTONE`** |

**Frozen:** `BIN-3-MONOTONE and BIN-3-DISCORDANT are preserved unchanged from v1, v2.1, v2.2 and v2.3 so that an ill-posed or discordant localization reading lands in a pre-registered bin rather than in prose`. **The bin reserved for "this question is ill-posed for this mode" is the bin that fired** — and the window was **not** widened to hunt for a peak (`X10`, frozen). The two frozen measures agree exactly, so `BIN-3-DISCORDANT` did not fire.

**This is the observable the §0 plumber question was about, and the question is now live rather than hypothetical.** The energy density rises monotonically outward to the edge of the window. Either the cavity genuinely stores its energy far out on the taper, **or** — the reading this lane cannot exclude from inside the numerics — the rise is the generic outward `exp(|ω_I| r)` growth of *any* leaky resonator's eigenfunction, in which case "where does the mode live" is the wrong question for a radiating cavity and the localization axis should be retired from this arc rather than re-measured. **Grant's plumber call is owed (§7).**

### §4.5 BIN-4

**Frozen:** `BIN-4 is N/A BY CONSTRUCTION in this lane and is not adjudicated at any precedence level including a full gate pass; no overtone, no ladder, no mode count and no completeness statement is computed, and the deferral is an open instrument-scope question awaiting a substrate-derived low-frequency cutoff, not a failure of this lane`. **This is a full gate pass, and `BIN-4` reads exactly the same as it would have on a failure. That is the point of declaring it in advance.**

**Frozen:** `this lane asserts the existence and location of THIS root; it asserts NOTHING about the absence or presence of other modes`. **Restated at the point a reader is most likely to over-read `[1, 1, 1, 1, 1]`: that row says nothing sits within `0.5` of this root. It says nothing whatever about what sits anywhere else — and in particular the `BIN-1`/`BIN-2` misses are misses for THIS mode, not for the spectrum.**

**Frozen:** `no argument-principle winding, no contour integral and no region count is computed anywhere in this lane; the pole-counting instrument the PR #854 audit impeached is not used, not repaired and not relied on`. **Verifiable by grep: the driver contains no winding, no contour and no argument-principle routine.**

---

## §5 — DISCRIMINATION NOTE: what these bin outcomes DO and DO NOT mean

**Written under `consistency-vs-emergence` and `ave-discrimination-check`, and written to the standard the prereg fixed in advance rather than to the standard the result invites.**

### §5.1 The certification itself

**A `ROOT-CERTIFIED` verdict is a statement about an INSTRUMENT, not about the world.** It says: *this discretization's eigenvalue at this location is a property of the continuous problem and not of the discretization.* It does **not** say the substrate rings there. **Classification: INSTRUMENT-CONSISTENCY. It is not an emergence claim of any class and it cannot become one.**

### §5.2 ★ THE HONEST SIZE OF A `29 %` AND A `56 %` MISS

**Both `ω_R M_g` and `Q` are zero-free-input FORM tests, and that is their entire strength and their entire limit.** In units of `r_sat` the problem has **no adjustable parameter at all**: the profile is `A = r_sat/r`, the kernel is `S = sqrt(1 − A²)`, the speed is `c₀√S`, the inertia is `ρ₀`. `Ω` is a pure number forced by the profile SHAPE and `ℓ`. **Nothing can be tuned to move it.**

**What that buys.** A deviation of this size **cannot be attributed to a fitted parameter, because there is none.** The `29.1 %` and `56.2 %` shortfalls are real statements about the canonical profile as this lane consumed it. **They are reported as such, plainly, and they are not softened.**

**What it does NOT buy, and all three limits must be stated together or not at all:**

1. **A miss is not automatically a falsification of AVE.** It is a falsification of **this chain**: canonical graded profile + Ax-4 kernel + Op16 shear projection + `Γ = −1` SHORT at `r_sat = 7GM/c²` + reflectionless Regime-I port ⇒ the `ℓ = 2` toroidal pole. **Any one of those inputs could be the thing that is wrong**, and two of them are flagged in the prereg as untested (`I7`/FLAG-3, the reflectionless port) or as carrying an unresolved naming gap (`I5`/FLAG-4, which `ρ`).
2. **`ω_R M_g` was never emergence-capable.** It rides the GR-imported `ν_vac = 2/7` through the `7` in `r_sat`. Its miss is a **VALUE-CONSISTENCY** failure of an imported-scale chain, not a value-level statement about the substrate.
3. **This lane sees one mode.** With `BIN-4` `N/A BY CONSTRUCTION`, a miss on one pole says nothing about whether some other mode of the same cavity sits at GR's value. **The completeness question is exactly what is unanswered, and it is unanswered because the substrate has not supplied a low-frequency cutoff (FLAG-5).**

**Where an AVE-distinct forward prediction would live, if any:** in the **overtone ladder** and the **spheroidal branch**, neither of which this lane computes. **This result, on its own, is a clean negative on one link of a standing corpus chain. It is not a chord, and this document does not present it as one.**

### §5.3 What is now falsified, and at what strength

| statement | status after this lane | strength |
|---|---|---|
| `r_eff = r_sat/(1+ν_vac)` **as a derivation of the `ℓ=2` eigenfrequency** | **FALSIFIED** by the pre-registered rider at `27.9 %` against a `3 %` trip level | **Strong within the chain.** Zero free parameters, gated instrument, criterion frozen before the run. **Conditional on the §5.2 input list.** |
| `ω_R M_g = 18/49` as the cold `ℓ=2` value | **MISSED** by `-27.9 %` | same |
| `Q = ℓ = 2` as the cold `ℓ=2` pole-`Q` | **MISSED**; `Q = 0.920` | same — and note the discriminator's `CLOSER-CONVENTION` verdict is **not** support for `Q = 2` (§4.3) |
| GR's cold `ℓ=2` fundamental as an output of this chain | **MISSED** on both `ω_R` (`-29.1 %`) and `Q` (`-56.2 %`) | same |
| the existence and location of this root | **CERTIFIED** | instrument-level only (§5.1) |
| whether the cavity has other modes, incl. one at GR's value | **UNTOUCHED** | `BIN-4` `N/A BY CONSTRUCTION` |

**Nothing above is propagated.** No `clm-`/`def-` is minted, no KB leaf is edited, no solidity is changed, no falsification-ledger row is written. **This document reports; the auditor lane adjudicates what, if anything, propagates.**

---
## §6 — WHAT THIS LANE'S OWN EVIDENCE DOES **NOT** SUPPORT

**Written because a full pass is exactly when a lane is most tempted to claim more than it earned.**

1. **This is NOT an independent confirmation of anything v2.2 measured.** **Frozen:** `agreement between this lane's unchanged gates and v2.2's is a REGRESSION CHECK on the carry-over and is not independent corroboration of any value`. Expectation 5 (§3) is a **regression check**: the instrument was carried over by copy-with-attribution precisely so the gate specification would be the only variable. **Nine gates reproducing v2.2's numbers is evidence the carry-over is faithful, and nothing more.**
2. **G6 adds NO new implementation independence.** **Frozen:** `G6 in this lane gates THIS file's transcription against v1's different-in-kind instrument and adds NO new implementation-independence beyond what v2.2 already reported; a G6 pass here may not be presented as a second independent confirmation`. The `6.803231574438666e-07` agreement with v1 is the **same** cross-lane agreement v2.2 reported, re-measured by a descendant of v2.2's own file.
3. **This lane makes no claim about any predecessor's independence either.** **Frozen:** `this lane claims no implementation independence for itself and makes NO claim about the degree of independence of any predecessor; the only genuinely different-in-kind instrument in this arc is v1's real-axis asymptotic matching, and it appears here solely as G6's comparator`.
4. **G2b's pass is not by itself the justification for the ladder.** The ladder placement rests on the law's out-of-sample magnitude prediction, not on G2b — **frozen:** `the G2 certification ladder is n in {48, 64, 80, 96}; its lowest rung is placed by the out-of-sample prediction of the root-exponential law fitted on rungs {48, 64, 80}, which predicts e(32) = 2.277976e-10 against a measured 1.249682e-10 with both above the frozen 1e-10 tolerance, corroborated by the v2.1 coefficient-tail receipt at n = 40 and by the orchestrator-relayed n = 32 / n = 36 boundary`. The driver carries the same caution at the G2b site, verbatim: *"G2b gates the LAW, not the presence or absence of any rung."* **§2.3 confirms it from the measurement: `n = 32` obeys the same law and would not have broken G2b.**
5. **A certification here does not revive v2.3 or re-score v2.2.** v2.2 stands `ROOT-NOT-CERTIFIED` on the ladder it froze; v2.3 stands superseded pre-measurement with zero numbers. **Frozen:** `a ROOT-CERTIFIED verdict in this lane does not certify, rescue, re-score or reverse v2.2, which stands ROOT-NOT-CERTIFIED on the ladder it froze, and does not revive v2.3, which is superseded pre-measurement`.
6. **The relayed PR #856 review findings were never depended on.** **Frozen:** `no gate, tolerance, ladder rung or bin in this lane depends on the orchestrator-relayed PR #856 findings`. They are corroboration only, and they were still not locatable in the repository record when this result was produced (FLAG-11). **The convergence law was fitted here, from an in-repo blob, and tested out of sample here.**

> **🔴 CORRECTION 2026-08-03 (added after the PR was opened, under adversarial review) — THE RESTATEMENT ABOVE IS TOO STRONG, AND THE FROZEN SENTENCE IT RESTATES IS CONTRADICTED BY THE PREREG'S OWN ARITHMETIC.** The distinction that has to be drawn, and was not:
>
> - **No gate OUTCOME depends on I22.** This is TRUE and it is now demonstrated rather than asserted. The prereg derives the G2b band as the union of this lane's own evidence with the relayed range, widened by `±1.0`. Struck of the relayed range entirely, the union collapses to this lane's own pairwise span and the **counterfactual lane-only band is `[4.775382, 7.354001]`**. Under it: the certified root's `c` = `6.216374478994577` still **PASSES**; the v2.1-banked artifact's `c` = `0.25002341694486013` still **FAILS**; FT-2b's mutated `c` = `0.07345138526200583` still fires. **Every gate verdict, every self-test, every bin and the certification itself are unchanged.**
> - **The band's stated ENDPOINTS do depend on I22.** The relayed range `5.4 … 6.6` **strictly contains** this lane's own span `5.775382 … 6.354001`, so the union *is* the relayed range and the frozen endpoints `4.4` and `7.6` *are* the relayed numbers ∓/± `1.0`. **A frozen sentence that reads "NO gate, tolerance, ladder rung or bin in this lane depends on the orchestrator-relayed PR #856 findings" is therefore contradicted by the prereg's own §4.4(c) derivation, at the word "tolerance".**
>
> **The prereg is frozen and is NOT edited.** The contradiction is recorded here, in the docket and in the PR body, and is **routed to the successor freeze**, which must either derive its bands from in-repo evidence alone or state plainly which frozen numbers a relayed, unverifiable receipt set. **This lane's certification does not turn on it** — that is the counterfactual above — **but "no gate depends on it" was the wrong sentence to freeze, and it is corrected rather than defended.**

---

## §7 — FLAG-DON'T-FIX: what is routed, and to whom

**Nothing below is repaired here.**

1. **★ FLAG-11 — the relayed-review receipt is STILL not in the repository record.** Re-checked at result time, after the battery ran: PR #856 shows no comments, no reviews, no inline review comments; its branch tip is unchanged. **This lane derived what it needed itself and tagged the relayed material `ORCHESTRATOR-RELAYED, UNVERIFIED` throughout.** Routed to the orchestrator, not to physics: **if that 12-rung sweep exists, it belongs in the repository so a successor can cite it rather than relay it.**
2. **★ FLAG-3 stands, and it is now the single biggest threat to the physics reading of this result.** `I7` — the reflectionless Regime-I port at infinity — is a **frozen canonical input, assumed and not tested**, and this lane's entire method divides out the corresponding analytic factor. **If the substrate carries any far-field reflector, the certified root moves and the `29 %`/`56 %` misses are misattributed.** A `ROOT-CERTIFIED` verdict does **not** touch this flag. **Routed as the highest-value follow-on to the negative.**
3. **★ FLAG-4 — #814 CF-7's naming gap is untouched, and it is now load-bearing on a falsification.** `manuscript/ave-kb/vol3/claim-quality.md:122` writes `Z_{shear} = \rho\,c_{shear}` and never names which `ρ`. This lane consumed the leading reading (`ρ₀`, `I5`). **The prereg's `X6` fences off FORK-3(b)'s alternative `ρ_eff = ρ₀/S³`, which is NOT run here — and which would move the eigenvalue.** Before the `BIN-1`/`BIN-2` misses are read as a falsification of the profile, that fork is owed a run. **Surfaced, not resolved.**
4. **★ FLAG-5 — the completeness question is the reason a miss cannot be read as "the cavity is wrong".** Until a **substrate-derived low-frequency cutoff** exists, no lane in this arc can say how many modes the graded shear cavity has, or whether one of them sits at GR's value. **Routed to Grant and to a successor; not attempted, not sketched, not assumed.**
5. **★ The BIN-3 plumber question is now live** (§4.4). Grant's call is owed on whether a leaky resonator's outward-growing eigenfunction makes localization ill-posed. **The window was not widened.**
6. **⚑ FLAG-1 — exercised and did not bite** (§4.3). The two corpus `Q_GR` values cannot flip any verdict here. Still routed to the auditor lane as a corpus-precision question.

    > **⚑ CITATION-PRECISION NOTE, 2026-08-03 (added under adversarial review; the frozen file is NOT edited).** The prereg attributes the rounded-prose comparator `2.099438202247191` to `research/2026-07-30_qlaw-derivation_scoping.md:401` with the word *"verbatim"*. **That line does not carry those sixteen digits.** `:401` carries the quotient to four significant figures, `2.0994`; the two INPUTS it was formed from, `0.3737` and `0.0890`, are at `:399` and `:400`. The 16-digit value is a *re-computation* from those inputs, not a verbatim quotation — a **verify-before-cite** miss of exactly the class this arc exists to catch. **Nothing turns on it**: FLAG-1 did not bite, the window was checked, and `Q` is nowhere near it. **Recorded, routed with FLAG-1 to the auditor lane, not repaired in the frozen file.**

    > **⚑ MENU NOTE, same date.** The driver can emit a BIN-2 discriminator token `BIN-2-AMBIGUOUS-UNDER-FLAG-1` (`research/drivers/coldq_pole_v2p4_root.py:1326`) that **appears nowhere in the frozen prereg's BIN-2 menu** — the frozen text says the discriminator *"is reported as AMBIGUOUS rather than adjudicated"* without minting a token for it. **It did not fire, so it has no consequence for any verdict in this lane**, and the driver is fenced and not edited. **Recorded so the successor either freezes the token or drops it, rather than shipping a verdict string no pre-registration contains.**
7. **⚑ FLAG-9 carried forward, unresolved** — v1's `0.28430` is a **clamped**-wall mutation (`W(r_sat) = 0`), not the spin-1 one; v2.1's result-doc §5.4 places the two in a single row. **That row compares two different mutations.** Both other lanes' files byte-untouched.
8. **⚑ FLAG-10 — this lane's independence is weaker than v2.2's by design** (§6). The exterior-complex-rotation cross-check remains the genuinely independent third instrument and is **not built here**.
9. **⚑ FLAG-12 — the Makefile contact is a REAL two-line conflict**, not an append-only merge. **Frozen:** `the Makefile contact with PR #854 and PR #856 is a REAL two-line conflict on the .PHONY line and the verify: prerequisite line, is NOT append-only, and is NOT auto-resolved by any merge driver on the server side`. Mitigation as frozen: the number check is wired as its **own** target so no recipe body is shared, and this branch is **rebased onto a fresh `origin/main` immediately before the PR**. Every `research/` and `_orchestration/` file in this lane is new and shared with no open branch.
10. **`gates.G9.pass` is a driver-side placeholder.** Determinism is adjudicated **externally**, by running the driver twice and diffing the shipped objects. That was done: identical digests `6cec005e0155513a`, byte-identical apart from `_runtime_sec`. **Disclosed so the JSON flag is not mistaken for a self-measurement.**

    > **ROUTED TO THE SUCCESSOR, 2026-08-03 (added under adversarial review).** Disclosing the placeholder is not enough. **A gate that consumes a self-declared field is a checklist, not a gate** — the driver writes `"pass": true` into `gates.G9` and nothing in the battery can ever make it write anything else, so any consumer that reads the shipped object and tallies `pass` flags will count a gate that measured nothing. **The successor's driver MUST NOT EMIT a `pass` field for `G9` at all.** It should ship the digest and the note, and leave the verdict to the external two-run diff, so that the only way to obtain a G9 verdict is to actually perform the comparison.
    >
    > **This lane's G9 content is nevertheless discharged, and externally:** the adversarial review ran the driver a further two times itself and obtained the same digest `6cec005e0155513a`, independently of this lane's own two runs. **Recorded as the receipt that G9's content — not its flag — is satisfied here.** The placeholder is a defect in the *instrument's reporting*, not in the determinism it claims.

---

## §8 — VALIDATION AND SCOPE DISCLOSURES

- **Determinism.** Two full runs, digests `6cec005e0155513a` and `6cec005e0155513a`, shipped objects byte-identical apart from `_runtime_sec`.
- **Runtime.** **Frozen:** `total battery runtime <= 3600 s on the reference machine; a longer run is disclosed, not silently accepted`. Measured 262.19 s and 255.27 s — inside the budget. **These two numerals are deliberately written WITHOUT backticks and are NOT registered:** `_runtime_sec` is machine-dependent, so registering it would make the gating number check fail on every honest re-run on every other machine (the #801 R3 lesson).
- **The gating number check implements the three fixes and the narrowed scope**, all frozen pre-measurement. **Frozen:** `this lane's gating number check implements (i) a MINIMUM SIGNIFICANT-DIGITS FLOOR of 3, machine-enforced, below which a numeral token may NOT be registered against the shipped JSON and MUST be allow-listed with a stated reason; (ii) PER-SITE rather than global dedup, so every occurrence of a numeral is checked and the reported counts describe SITES rather than distinct tokens; and (iii) LIST-VALUED REGISTRATION, so that a bracketed count vector such as the G5 isolation counts or the FT-5 artifact counts is registered against the shipped JSON list as a whole rather than decomposed into single-digit tokens that the significant-digits floor would force onto the allow-list`. **Frozen:** `the gating number check scans the RESULT DOC only; the arithmetic of sections 4.3 and 4.4 of this prereg is reproduced by the driver and reported in the result doc, where it IS machine-checked, and no claim is made anywhere in this lane that the prereg itself is machine-checked`.

> **🔴 CORRECTION 2026-08-03 (added after the PR was opened, under adversarial review) — THE CHECKER DID NOT DO WHAT THE BULLET ABOVE SAYS IT DID, AND TWO STATEMENTS IN THIS DOCUMENT WERE FALSE WHEN THEY WERE MADE.**
>
> **The defect.** The checker's token pattern was `` `([^`]+)` ``. A negated character class matches newlines, so the fenced code block in §2.1 was consumed as one span that swallowed one of its own three closing back-ticks. From that point to the end of the file, **back-tick pairing was inverted**: opening delimiters were read as closing ones. The shipped instrument produced **111 newline-spanning phantom spans**, reported 71 sites where 151 exist, and **never exercised 34 of the 72 keys registered in its own file** — including **every `BIN-1`/`BIN-2` numeral**, G2b's fitted `c`, and the run digest.
>
> **The first false statement — the frozen §4.5 claim, quoted verbatim from the prereg:** *"(ii) PER-SITE rather than global dedup, so that every occurrence of a numeral is checked and the reported counts describe SITES rather than distinct tokens"*. **Every occurrence was not checked.** The frozen text is correct and is unchanged; the implementation did not meet it.
>
> **The second false statement — this document's own provenance line, quoted verbatim from §S below:** *"All numbers above are read from the shipped `research/drivers/coldq_pole_v2p4_root_results.json` and are machine-verified against it by `research/drivers/coldq_pole_v2p4_root_number_check.py`, wired into `make verify`."* **At ship, roughly half of them were not.** The sentence is true only after the repair recorded here.
>
> **The repair is a TIGHTENING, and it is recorded as one.** Rule 11 forbids dropping, widening or re-defining a frozen criterion after a result is seen. It does not forbid — it requires — making an implementation actually meet the criterion it was frozen to meet. **No gate, tolerance, band, bin, threshold, comparator or measured number is changed by this repair.** Three changes, all strictly in the direction of more checking: the token pattern excludes newlines; a **completeness guard** makes any registered key the document never exercises a hard configuration FAIL; and run digests are classified as checkable tokens rather than skipped. Where a registered numeral was unreachable because this document wrote it only inside a compound expression or a fenced block, **the document was edited to write that numeral where the machine reads it** — the honest direction, since the alternative (deleting the registration) would leave the same number unchecked while making the counter look clean.
>
> **Mutation receipts, run against the as-shipped instrument and the repaired one.** Drifting the last digit of G2b's fitted `c` at its §2.2 site, and one digit of `D_omega` at its §4.2 site: **the as-shipped checker returned exit 0 on both, with its site counts completely unchanged — it never saw either mutation.** The repaired checker fails both, naming the token and the line. Receipts are recorded in the docket entry.

- **mp strings.** **Frozen:** `the shipped results object carries Omega_re_mp and Omega_im_mp as 40-digit mp STRINGS for EVERY rung of the FULL ladder, for every gauge, for every dps and for every x_sat, so that no reported separation depends on a double-precision cast of the root`. **Honoured.**
- **Engine fence.** **Frozen:** `engine src/ave BYTE-UNTOUCHED; the instrument lives entirely in research/drivers/ and imports ave.core.* read-only`. **Honoured.**
- **Carry-over fence.** **Frozen:** `the v2.4 instrument CARRIES OVER v2.2's method into this lane's own file research/drivers/coldq_pole_v2p4_root.py by copy-with-attribution, so that the ONLY differences between the two batteries are the gate specifications of section S.4; it is NOT an independent third reimplementation, and this lane may not claim reimplementation independence from v2.2`. **Honoured — transcription sites are marked `[xcribe v2.2 ...]` and `[xcribe v2.1 ...]`, the chain preserved rather than collapsed.** **Frozen:** `the v2.4 driver is adapted from the UNCOMMITTED and NEVER-EXECUTED v2.3 driver, which produced no results object, no digest and no number; the adaptation is therefore pre-measurement and carries no contamination, and this lineage is disclosed rather than presented as a fresh authorship`. **Honoured.**
- **One disclosed double-precision cast.** The certified eigenfunction is computed in mp; for the localization argmax and the G7(b) energy ratio it is cast to double inside a single function, which says so at the cast site. **It does not touch G1, G2, G2b, G3, G4, G8 or G10, each of which is mp end-to-end.**
- **Scope, unchanged:** `ℓ = 2` is an input, not derived; `ν_vac`, `K = 2G` and the `7` in `r_sat` are GR-imported and untouched; the spin (`a_* > 0`) mapping is out of scope; the spheroidal branch is not built; FORK-3(b) is not run; **no completeness or overtone statement of any kind is made.**

---

> **Result provenance.** Resolves the frozen gates and bins of `research/2026-08-03_coldq-pole-v2.4-root_prereg-FROZEN.md` (commit `36186006`, COMMIT 1 of this lane, pushed ALONE before any driver code existed and before any number produced by this instrument existed). All numbers above are read from the shipped `research/drivers/coldq_pole_v2p4_root_results.json` and are machine-verified against it by `research/drivers/coldq_pole_v2p4_root_number_check.py`, wired into `make verify`. Two full driver runs produced identical digests. **Predecessor lanes, all unmodified and byte-untouched by this lane:** PR #845 (MERGED at `052ccbba`, `SOLVER-NOT-CERTIFIED`); `research/2026-08-03_coldq-pole-v2_prereg-FROZEN.md` (`00724432`); `research/2026-08-03_coldq-pole-v2.1_prereg-FROZEN.md` (`7d8fe484`) and its result doc (PR #854); `research/2026-08-03_coldq-pole-v2.2-root_prereg-FROZEN.md` (`f15a6e4d`) and `research/2026-08-03_coldq-pole-v2.2-root_result.md` (`982c4c9b`) and their driver (PR #856, `ROOT-NOT-CERTIFIED`); `research/2026-08-03_coldq-pole-v2.3-root_prereg-FROZEN.md` (`3e2c0c1c`, superseded PRE-MEASUREMENT, no retraction header, zero numbers produced). Mints no `clm-`/`def-`; propagates to no leaf; engine byte-untouched; falsification ledger untouched. Companion: the docket fragment `_orchestration/docket-entries/2026-08-03-coldq-v2p4-root.md`.

---

> **★ REBASE PROVENANCE DISCLOSURE (2026-08-03, added after the battery ran and before the PR was opened).** The frozen FLAG-12 mitigation required this branch to be **rebased onto a fresh `origin/main` immediately before the PR**, and doing so confirmed FLAG-12's own prediction: **PR #854 merged into `main` while this lane was running, and the Makefile conflicted on exactly the two shared lines FLAG-12 named** — the `.PHONY` list and the `verify:` prerequisite list — plus the `help` echo block. **It was a real textual conflict, not an append-only merge**, exactly as the superseded v2.3 characterization was corrected to say. Resolved as a **union**: `#854`'s `verify-coldq-v2-number-check` and this lane's `verify-coldq-v24-number-check` both run under `make verify`, and neither recipe body is shared. **The rebase rewrote this lane's commit SHAs, so both sets are recorded here and the freeze-before-code ordering is auditable under either.** The prereg **blob** is byte-identical across them (`894be984a41010f6f9629967464300fe023a2f3d`), as is v2.3's (`33432ac7fd20eb5c4a348c4b2428a799b5f4dd4b`):
>
> | freeze | ORIGINAL, pushed ALONE before any code | after the pre-PR rebase |
> |---|---|---|
> | v2.3 prereg | `3e2c0c1c` (2026-08-03T07:23:37-07:00) | `8e9fb03b` |
> | v2.4 prereg | `36186006` (2026-08-03T07:45:26-07:00) | `d5b9978b` |
>
> **The `Prereg-commit:` pointer at the top of this document deliberately still names `36186006`** — the commit that was actually pushed ALONE, before any driver code and before any number existed, which is the receipt that matters. The rebased commit carries the identical blob, so the frozen-provenance gate resolves against either.
