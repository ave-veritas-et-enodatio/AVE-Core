# The cold-Q pole derivation — RESULT: the instrument is NOT CERTIFIED, and one mechanism explains every failure

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
> Four of nine gates failed at their frozen tolerances (G4, G5, G7, G8) and one of six self-tests did not fire (FT-5). **All five outcomes have a single named mechanism**, and it is a property of the frozen *controls*, not of the physics: **the far-field matching is an ASYMPTOTIC (divergent) series, and the ingoing-coefficient extraction is exponentially ill-conditioned as `exp(2|Im omega| R_match)`.** The frozen tolerances (`1e-8`, `1e-9`) and the frozen search rectangle (`|omega_I| M_g` up to `1.00`) were written as if the far-field expansion were convergent and the extraction uniformly conditioned. Both assumptions are false, and the battery measured exactly that.
>
> **This is a clean instrument-failure result with a named mechanism — Rule 11's good shape, not a rescue candidate.** The physics numbers the battery produced are reported below as **NOT-ADJUDICATED DIAGNOSTICS** and carry **no bin verdict**, per the frozen precedence.
>
> **The five gates that DID pass are the load-bearing physics ones**, and two of them are new: the derived **spin-2** radial system reproduces the exact spherical-Hankel far field to `1.7688e-14` (G1), its **spin-2 energy weighting** reproduces the shot closed-cavity eigenvalue to `4.9220e-13` (G2) — and swapping in the **spin-1** weighting breaks that agreement by `21.7` percent (FT-6). **The #814 R7 spin-1-vs-spin-2 prerequisite is therefore not merely obeyed here; it is measured, and it is load-bearing.**

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

## §2 — THE ONE MECHANISM behind all five failures

The four failing gates and the unfired self-test are **not five problems**. They are one, and the battery measured it directly.

### §2.1 The far-field expansion is asymptotic, not convergent

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

**G4 and G5 fail for exactly this reason and for no other.** G4's frozen set contains `R = 25`, whose floor is four orders above the frozen `1e-8`. G5's frozen set contains `N = 12`, which at `R = 40` is far from optimal truncation. **The controls were designed for a convergent expansion, where "more terms is better" and "any `R` in the set is equivalent". For an asymptotic expansion both statements are false.** G3 independently proves the *integrator* is not the limit: `n_steps` 16000 → 64000 moves the pole by `3.5006e-10`, and a separate sweep found 8000 → 128000 agreeing to `1e-11`.

### §2.2 The subdominant-coefficient extraction is exponentially ill-conditioned

With `Im omega < 0` the **outgoing** solution is the *dominant* one at large `r`, so the quasinormal condition asks for the *subdominant* ingoing coefficient to vanish. A relative integration error `delta` manufactures a spurious ingoing amplitude of order `delta * exp(2|Im omega| R_match)`. The prereg named this at §9 item 8 and froze `R_match` independence over a finite set rather than "arbitrarily large `R`" **because of it** — but it still froze a search rectangle reaching `|omega_I| M_g = 1.00`, where at `R_match = 40` the contamination factor is `exp(80)`. That region is pure roundoff.

The shipped `certified_omega_I_band` measures where the count is trustworthy:

| `wi_max` | 1.00 | 0.70 | 0.50 | 0.40 | 0.30 | 0.25 | 0.20 | 0.15 | 0.10 |
|---|---|---|---|---|---|---|---|---|---|
| winding | `28` | `27` | `27` | `5` | `4` | `4` | `4` | `4` | `3` |
| located inside | `34` | `34` | `34` | `2` | `1` | `1` | `1` | `1` | `0` |

**`largest_stable_wi_max` is `null`: no sub-rectangle in the frozen ladder satisfied "winding is a stable integer AND equals the located count".** The winding never drops to the located count even deep in the well-conditioned region, because the *contour itself* always includes the noise-dominated bottom edge.

**FT-5 is the clean proof, and it is why FT-5 not firing is the most informative single line in this battery.** On the zero-grade problem the traction-free condition reduces in closed form to a polynomial of degree exactly `ell+1`, so the root count inside the test box is known exactly: `1`, `1`, `2` for `ell = 1, 2, 3`. The measured winding is `15.000` for **all three** `ell`. That number is not random — it is the optical length `2*R_match - a = 15` in radians per unit `omega`, i.e. **on the noise-dominated part of the contour the phase of the objective tracks the phase of the cancelled large terms, not of the physical ingoing amplitude.** **Frozen:** `case (a) MUST return count 0 and case (b) MUST return count equal to the closed-form root count for ell in {1,2,3}` — case (a) returned `-2.5621e-16` (correct), case (b) did not. **FT-5 did its job: it detected that G7's instrument is untrustworthy, which is precisely what a fireability self-test exists to do.** G7's failure is the same fact seen from the other side: `34` located poles, of which all but one sit in the noise band.

### §2.3 G8 fails by a factor of 11 while CONFIRMING the physics it was built to test

**Frozen:** `Q, r_peak/r_sat and the overtone ratios are invariant to <= 1e-9 relative across x_sat in {5, 7, 11}, while omega_R*M_g scales as 1/x_sat to <= 1e-9 relative`.

| `x_sat` | `R_match` | `omega_R M_g` | `omega_I M_g` | `Omega = omega*r_sat/c_0` | `Q` |
|---|---|---|---|---|---|
| `5` | `28.571428571428573` | `0.37073131303835555` | `0.20145145121677233` | `1.8536565651917778` | `0.9201505146751939` |
| `7` | `40.0` | `0.2648080807146999` | `0.14389389410143283` | `1.8536565650028993` | `0.9201505121823758` |
| `11` | `62.857142857142854` | `0.16851423344429386` | `0.09156884260787314` | `1.8536565678872325` | `0.9201505045003425` |

`Omega` spread `1.5560e-09`; `Q` spread `1.1058e-08`; `r_peak/r_sat` spread `1.7511e-13`. **The gate FAILS at its frozen `1e-9`.** But read what it measured: **the scale-free eigenvalue and `Q` are `x_sat`-invariant to eight and nine significant figures.** The prereg's structural claim — that `Q` is *exactly* `nu_vac`-free because `r_sat` divides out of the radial system identically — is **CONFIRMED to the instrument's own accuracy floor** (§2.1: `~1e-8` at `R = 60`). The gate's `1e-9` simply sits below that floor.

> **⚑ A real bug this battery found in ITS OWN first run, recorded rather than quietly fixed.** The first full battery returned `Q` spreads of `1.74` on this gate — a `174` percent violation. The cause was **mine, not the physics**: `R_match` and the search rectangle were held fixed in units of `M_g` while `x_sat` varied, which puts the far-field match *inside the grade* at `x_sat = 11` (`R/r_sat = 3.64`) and breaks the numerics' scale invariance even though the physics' scale invariance is exact. Fixed by scaling `R_match` and the rectangle with `x_sat` (`scaled_geometry()`), and re-run. **This is a code-correctness repair, not a criterion change — the frozen G8 string is untouched and the gate still fails at it.** The first-run numbers are on the record here so the repair is auditable.

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
- `Q` against the Op21 `2*pi`-convention `Q = ell = 2`: deviation `-54.0` percent. The measured `Q` is nearer the convention value than the GR value (distances `1.0798` and `1.1801`).
- `k_0*r_sat = 1.8537` against the standing chain's asserted `ell*(1+nu_vac) = 2.5714`.

> **★ The IDENTITY the prereg froze BEFORE any number existed, and it holds.** `k_0*r_sat = x_sat * omega_R M_g` identically, so the "9/7-above-cutoff" test **is** the `omega_R` vs `18/49` comparison re-expressed, not an independent axis. Both read `-27.91` percent. The prereg recorded this in advance precisely so it could not be presented afterwards as two corroborating results. **It is one.**

### §4.2 Radial localization

Both frozen measures agree exactly and both place the maximum at the **outer** edge of the frozen window `r/r_sat` in `[1.0, 2.0]`: `u_energy = 1.9997126071429716`, `u_kinetic = 1.9997126071429716`, `interior_max = false`. The mode-energy density at the wall is `0.04058976258552422` of the window maximum.

**Read honestly, this measurement is dominated by a generic property of quasinormal eigenfunctions, not by substrate physics:** a QNM amplitude grows as `exp(|omega_I| r)` outward, which over this window is a factor of `e^(1.007)` in amplitude before the `r^2` measure is applied. That is why the prereg reserved a `BIN-3-MONOTONE` sub-bin for "the maximum sits at an endpoint, so localization is not a well-posed observable for this mode" — **the reserved bin turned out to be the relevant one.** Had bins been adjudicated, this is where BIN-3 would have landed, and it would have said that the derived mode is **neither** a rim ring at `r_sat` **nor** a ramp mode at the `r*/r_sat = 1.2247` turning point.

### §4.3 Overtones

Within the region where the extraction is conditioned there is **one** pole. The next located pole, `omega M_g = 0.12509420853469172 - 0.3805502556171569i`, sits inside the band §2.2 shows is roundoff-dominated and **is not credible**. No overtone ratio is reported, because reporting one would require trusting a number this battery's own self-test says cannot be trusted.

### §4.4 Frozen sensitivities and diagnostics

- **FORK-2 KEEP-BOTH (`S^{1/4}` Family-E counterfactual).** **Frozen:** `the S^{1/4} counterfactual is reported as a sensitivity, never as the primary result, and no bin is adjudicated on it`. Measured: `omega M_g = 0.06457835191289236 - 0.07921459609905164i`, `Omega = 0.45204846339024657`, `Q = 0.40761649426415175`. **Low confidence** — the same conditioning limits apply, and this branch was not separately gated.
- **`ell`-ladder.** **Frozen:** `DIAGNOSTIC — no bin, no verdict; FORK-12 is unanswered and this lane does not adjudicate it`. *(The shipped JSON carries the ASCII transliteration of the same tag, `DIAGNOSTIC - no bin, no verdict; ...`, because the driver writes plain-ASCII JSON; the frozen label above is the prereg's own bytes.)* Measured `Omega`: `ell = 2` → `1.8536565656172288`, `ell = 3` → `2.5138625055232238`, `ell = 4` → `0.5197786125250078`, `ell = 5` → `0.4852927998939722`. **The `ell = 4` and `ell = 5` rows are not credible** — they break the monotonic rise in `Omega` that `ell = 2, 3` show, which is the signature of the seed-selection having picked a noise root. Recorded, not interpreted. **FORK-12 remains unanswered and is not adjudicated here.**
- **Clamped-wall diagnostic (FT-2 by-product).** Replacing the canonical SHORT by a clamped terminus moves the pole by `0.28430` relative. **The canonical `Gamma_shear = -1` free surface is load-bearing in the answer, not decoration** — which is #814's CF-13 ("the sign is Q-neutral in the loss ledger and Q-relevant through the frequency") with a number attached for the first time.

---

## §5 — WHAT THIS LANE DID ESTABLISH (the gates that passed are not nothing)

1. **★ The spin-2 discipline is discharged AND measured.** The #814 R7 prerequisite was *"derive the spin-2 spherical-mode impedance; do NOT import the spin-1 one."* **Frozen:** `the radial system is the toroidal (odd-parity, exactly divergence-free) branch derived from the shear-channel continuum equations; the radial functions coincide with spherical Hankel functions in the homogeneous limit but the impedance relation T = mu(W' - W/r) and the (l-1)(l+2) stored-energy weighting are the spin-2 ones and no spin-1 vector-multipole impedance is imported anywhere in this lane`. G1 confirms the radial functions do coincide (`1.7688e-14`); G2 confirms the spin-2 energy weighting is the Euler–Lagrange partner of the integrated system (`4.9220e-13`); and **FT-6 shows the spin-1 `l(l+1)` weighting breaks that agreement by `0.21729`.** The distinction is therefore not bookkeeping — it is worth `22` percent on the object `Q` is built from.
2. **The wall terminus is reached exactly, with no regulator.** **Frozen:** `the wall is reached exactly via the r = r_sat + sigma^2 substitution, which makes the two-component system analytic at sigma = 0; the initial condition is exactly (W,T) = (1,0) and no offset, series start, or regularized modulus floor is used`. G3 measures `3.5006e-10`. **The `A = 1` point is handled as a regular singular point of the ODE whose indicial structure selects the traction-free branch — not by a floor on `S`.**
3. **Ax-3 losslessness is structural, not asserted.** G6: every closed-cavity eigenvalue is real to `0.0` exactly and the assembled transfer carries zero imaginary part; FT-3 shows a smuggled `Im(mu)/Re(mu) = 1e-3` is detected. **The only loss in the ledger is the radiative port** — #814's CF-11 instantiated.
4. **FORK-10 and FORK-11 are dissolved as designed.** **Frozen:** `no port-Q is computed and no port-to-pole transfer is performed; the reported Q is the pole-Q that the GR comparator is`. Neither disputed spin-1 estimator was used and the `50` percent estimator spread recorded in #814 §1.3 never entered.
5. **`Q`'s `nu_vac`-freedom is measured, not argued** (§2.3) — to eight significant figures, which is the strongest form of the #808 §2.1 requirement (*"cancellation is the actual requirement"*) yet produced in this arc.

---

## §6 — FLAG-DON'T-FIX: what is routed, and to whom

**Nothing below is repaired here.**

1. **★ The frozen controls G4/G5/G7 and the frozen rectangle are mis-specified for this problem class — routed to Grant and the auditor lane.** They assume a convergent far-field expansion and a uniformly conditioned subdominant extraction. Neither holds. **This is NOT a request to loosen them.** The correct successor controls are *different in kind*, not looser: (i) **optimal-truncation** agreement (does the answer sit on the plateau of its own `N`-sweep at each `R`, and do the plateaux agree across `R`?) rather than fixed-order agreement; (ii) a **measured** conditioned band rather than an assumed rectangle; (iii) for the winding count, a contour that does not traverse the noise floor, or a method that does not require one. Per Rule 12 the slot is **not refilled**: a successor lane needs a **new prereg with a new version number and its own verification chain**, not an edit to this one.
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

> **Result provenance.** Resolves the frozen bins of `research/2026-08-02_coldq-pole-derivation_prereg-FROZEN.md` (COMMIT 1, pushed before any driver code existed). All numbers above are read from the shipped `research/drivers/coldq_pole_derivation_results.json` and are machine-verified against it by `research/drivers/coldq_pole_derivation_number_check.py`, which is wired into `make verify`. Two full driver runs produced identical digests. Mints no `clm-`/`def-`; propagates to no leaf; engine byte-untouched; falsification ledger untouched. Companion: the docket fragment `_orchestration/docket-entries/2026-08-02-coldq-pole.md`.
