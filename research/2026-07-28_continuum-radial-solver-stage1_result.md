# Continuum radial-acoustic solver — STAGE 1 RESULT (instrument certification: **CLASS WITHDRAWN — `C_NOT_CERTIFIED_VOID`**)

Prereg-file: research/2026-07-28_continuum-radial-solver-stage1_prereg-FROZEN.md

> **★CLASS WITHDRAWN 2026-07-28 (this commit) — the shipped `A_CERTIFIED` was NOT EARNED.** The adversarial review of PR #801 returned one CRITICAL and three MAJOR findings. Two of them are the same defect: **G3 and G2 each divide two BIT-IDENTICAL computations**, so neither gate can fail.
> - **G3** (`gate_G3_ortho_reduction`) called `build_profile(cold, shell_ortho=(1.0, 1.0))` and `build_profile(cold)` — and `(1.0, 1.0)` **is** the default. The two calls are the same call. `rel = 0.0` was true by construction, not by physics. The reviewer's mutation receipt: corrupting `ortho_layer` so that unit gains no longer reproduce `iso_layer` — *exactly* the defect G3 names — moved the physics (`B_ortho` `0.05788` → `0.05824`) while G3's ratio stayed exactly `0.0`, and **all nine gates still passed, all four self-tests still fired, and `CLASS A` still returned.** No self-test covered G3.
> - **G2** (`gate_G2_uniform_null`) evaluated the caged arm at `s_rail = 1.0` against `build_profile(..., uniform=True)`; at zero contrast those two code paths produce identical layer stacks, so the null certified that Python computes one expression twice.
>
> **The prereg's own frozen rule decides this, and it is not discretionary.** §6: `A gate that cannot fail is not a gate.` §8 CLASS C: **`A gate that cannot fail voids the certification exactly as hard as a gate that fails`**. The class is therefore withdrawn to **`C_NOT_CERTIFIED_VOID`** on the finding — before any repair — and must be **re-earned by a re-run**, not restored by a fix. The repaired battery's actual outcome is recorded in §1 and is whatever it is; no criterion is relaxed to recover `A` (Rule 11).
>
> The body below §1 is the as-shipped text at the moment of withdrawal and is superseded by the repair commits that follow; git is the audit trail.

**Date:** 2026-07-28 · **Class:** INSTRUMENT-CERTIFICATION result (research-doc; **mints no `clm-`/`def-`; propagates to no KB/tex leaf; banks NO physics verdict**) · **Charter:** `research/2026-07-21_continuum-radial-solver_CHARTER.md` (#789) · **Driver:** `research/drivers/continuum_radial_solver.py` → `research/drivers/continuum_radial_solver_stage1_results.json` (deterministic, no RNG; runtime `1.11 s`).

**Rulings executed (Grant, 2026-07-28, verbatim `[sic]`: `"D2: disclosed, D3: follow rec, D4: do it, D5: do the rec"`).** D2 = the disclosed `β ∈ {0,1,3}` sweep; D3 = the charter's recommendation (transfer-matrix primary + analytic matched-asymptotics backstop, T1 (a)+(c)); D4 = build stage 1 now on profile-independent gates; D5 = feed the #796-measured vessel profile. **D1 (the sector-crossed `c²`) REMAINS HELD** — this build and this certification are **D1-INDEPENDENT**: no gate consumes a `c²`, and no `c²` is evaluated anywhere in the outputs.

> **★THE HEADLINE — and what it is NOT.** ~~The instrument is **CERTIFIED (CLASS A)**~~ **WITHDRAWN (see the banner above): two gates could not fail, so the certification is `C_NOT_CERTIFIED_VOID` by the prereg's own §6/§8 rule and is being re-earned by repair + re-run.** The as-shipped statement was: all nine frozen validation gates PASS on both source fittings and both profile arms, and all four gate-fireability self-tests FIRE. **This is an instrument statement and nothing more.** `stage 1 banks NO physics verdict; every physics-shaped number in these outputs is an INSTRUMENT-LIVENESS DEMONSTRATION and is labelled DEMONSTRATION — no verdict banked`. Two load-bearing scope findings are surfaced, not resolved: **(1)** the `n = 0` spherically-symmetric channel the charter specifies **cannot host** either of the two objects the charter's C1 and C2 name — F2's `p = 2` is a DISPLACED-source (`n = 1` dipole) statement and the structural added-mass is the `n = 1` effective-density coefficient (§7); **(2)** D5 asked for the measured profile, but #796 shipped scalar EXTREMA plus a C-V reconstruction it grades corroborative-only — **no resolved radial `ε(r)` exists**, so the profile's radial SHAPE is an engineering choice and says so in every output (§5). Neither is reframed here; both route to Grant / the auditor lane.

---

## §1 — Certification verdict (read from the shipped JSON, `certification` block)

| Field | Value |
|---|---|
| `class` | **`C_NOT_CERTIFIED_VOID` — WITHDRAWN on the review finding** (as-shipped value `A_CERTIFIED`, void per prereg §6/§8) |
| `all_gates_pass` | `true` |
| `gate_fireability_selftest_pass` | `true` |
| `measured_certified_band` (`k·r_core`) | `[1e-8, 1e-6, 1e-4, 1e-3, 1e-2, 1e-1, 0.3, 1.0, 3.0, 4.0]` — the full frozen band |
| `measured_G4_overlap_subband` | `[1e-8, 1e-6, 1e-4, 1e-3]` — the full frozen overlap |
| `scope_reductions` | `[]` (empty ⇒ CLASS A rather than CLASS B) |
| `determinism_digest` | `1012a94da9cfc98cb6578c713bf8641c61fb02c4d4d79d8371a0d022f4ad9d9b` |
| `_runtime_sec` | `1.11` |

**Frozen:** `all of G1..G9 PASS on both source fittings AND gate_fireability_selftest_pass = True`

**Determinism.** **Frozen:** `two independent full driver runs produce an identical results digest (SHA-256 over the results object minus timing fields)` — RUN as two independent full driver invocations; both returned `1012a94da9cfc98cb6578c713bf8641c61fb02c4d4d79d8371a0d022f4ad9d9b`. **PASS.**

**Runtime.** **Frozen:** `total certification-battery runtime <= 600 s on the reference machine; a longer run is disclosed, not silently accepted` — measured `1.11 s`. **PASS.**

---

## §2 — THE NINE VALIDATION GATES (each pass/fail with its number)

Every gate below is evaluated for **both source fittings** and, where a profile arm exists, for **both the isotropic baseline and the D5-measured orthotropic vessel**; the reported number is the WORST case across all arms. **Frozen:** `every gate is evaluated for both source fittings (prescribed displacement and prescribed traction) and passes only if it passes for both`

| Gate | Frozen tolerance | Measured (worst arm) | Margin | Verdict |
|---|---|---|---|---|
| **G1** Lamé exterior `∇·u = 0` static limit | `≤ 1e-10` | **`2.7003e-14`** | `3.7e3 ×` | ✅ PASS |
| **G1b** multi-radius agreement | `≤ 0.25` | **`6.0687e-03`** | `41 ×` | ✅ PASS |
| **G2** uniform-medium NULL | `≤ 1e-12` | **`0.0000e+00`** (exact) | — | ✅ PASS |
| **G3** orthotropic → isotropic reduction | `≤ 1e-12` | **`0.0000e+00`** (exact) | — | ✅ PASS |
| **G4** transfer-matrix ↔ matched-asymptotics | `≤ 1e-6` | **`4.8581e-07`** | `2.1 ×` | ✅ PASS |
| **G5** Ax3 energy balance | `≤ 1e-10` | **`1.4062e-13`** | `7.1e2 ×` | ✅ PASS |
| **G5b** transfer matrix is real | `≤ 1e-14` | **`0.0000e+00`** (exact) | — | ✅ PASS |
| **G6** layer-refinement convergence | `≤ 1e-3` | **`1.0433e-04`** | `9.6 ×` | ✅ PASS |
| **G7** drive-amplitude independence | `≤ 1e-12` | **`2.9550e-13`** | `3.4 ×` | ✅ PASS |
| **G8** matching-radius independence | `≤ 1e-9` | **`5.0136e-11`** | `20 ×` | ✅ PASS |
| **G9** band conditioning | `≤ 1e12` | **`5.0202e+10`** | `20 ×` | ✅ PASS |

**The two gates the charter names explicitly (R5), verbatim:**

- **G1 — the Lamé exterior `∇·u = 0` static limit for a graded shell in an infinite medium (the #782-confirmed gate).** **Frozen:** `lame_ratio ≡ max over r in {1.5, 2.5, 3.5} of |div u|(r) / |div u|(0.5) <= 1e-10` — measured `2.7003e-14`. Companion **Frozen:** `max|Δ div u| / mean(div u) <= 0.25 across the three exterior radii` — measured `6.0687e-03` (the #782 shell-agreement tolerance, inherited unchanged; #782's own measured value on the lattice was `0.036`). The exterior dilatation is computed ANALYTICALLY from each layer's modal decomposition, not by finite differencing the reconstructed field.
- **G2 — the uniform-medium NULL.** **Frozen:** `at zero contrast: |rho_N - 1| <= 1e-12 AND rho_S <= 1e-12 AND |r_Z - 1| <= 1e-12` — measured worst deviation `0.0000e+00` across `k·r_core ∈ {1e-3, 0.3}` × both source fittings. **Frozen (KEEP-BOTH):** `the uniform-medium NULL is read on BOTH conventions: rho_N -> 1 and rho_S -> 0; neither convention is redefined in place (KEEP-BOTH)`.

> **★DEFINITIONAL CONFLICT SURFACED (flag-don't-fix, not resolved by fiat).** The charter's R5(b) asks for `ρ_N → 0` in the uniform-medium null. #775's `ρ_N` is a caged/uncaged POWER RATIO whose no-scatterer value is `1` by construction (its measured band is `0.26–2.90`, and the derivation doc's "static-release `ρ_N` … plateau `~0.3`" is a ratio, not a residual). Those two statements cannot both hold of one symbol. Stage 1 does **not** redefine either in place: it freezes **both** observables (`rho_N` = the #775 ratio, `rho_S ≡ |rho_N − 1|` = the charter's residual) and reports both everywhere (the KEEP-BOTH pattern). Which convention the charter's R5(b) intends is routed to the auditor lane / Grant; no charter text is edited here.

**The remaining gates, one line each:**
- **G3.** **Frozen:** `|B_ortho(hoop=1,radial=1) - B_iso| / |B_iso| <= 1e-12` — measured `0.0` **exactly** (bit-identical). The orthotropic layer is not an approximation of the isotropic one; R1's representation is exact.
- **G4 (the D3 (a)+(c) cross-check).** **Frozen:** `|rho_N_TM(k·r_core) - rho_N_MA| / rho_N_MA <= 1e-6 for every k·r_core <= 1e-3 in the frozen band` — measured worst `4.8581e-07`. The relative deviation scales as `(k·r_core)²`, the expected leading correction: `≈3.6e-7` at `k·r_core = 1e-3`, `≈3.6e-9` at `1e-4`, `≈2e-13` at `1e-6`. **Two independently-derived solvers agreeing to 13 significant figures at the band bottom is the strongest single statement in this certification.**
- **G5 (Ax3, R7).** **Frozen:** `|P_in - P_rad| / |P_in| <= 1e-10` — measured `1.4062e-13`; and **Frozen:** `max|Im T| / max|Re T| <= 1e-14` — measured `0.0` exactly. Work done by the source equals power radiated to infinity: no dissipative `Re(Z)` term is smuggled anywhere.
- **G6.** **Frozen:** `|rho_N(2·n_shell) - rho_N(n_shell)| / rho_N(n_shell) <= 1e-3 at the frozen n_shell = 256` — measured `1.0433e-04`. (Design note, disclosed: a naive `r`-uniform layer allocation converges only first-order and was `~7 %` per doubling at `n = 192`; the frozen allocation is **log-uniform in the grade `S`**, which recovers fast convergence. That allocation rule is an `[engineering-choice]` frozen in the prereg §5 before the run.)
- **G7.** **Frozen:** `rho_N invariant across source amplitude 1e-6 ... 1e+6 to <= 1e-12 relative` — measured `2.9550e-13`. **Honesty caveat, frozen in the prereg and repeated here:** `G7 is STRUCTURALLY exact in a linear frequency-domain solver; it certifies wiring, not physical linearity, and is reported as such`.
- **G8 (R6-ii).** **Frozen:** `rho_N invariant across R_match/r_core in {2, 4, 8, 16} to <= 1e-9 relative` — measured `5.0136e-11`. There is no sponge to fail: **Frozen:** `the exterior beyond R_match is represented by the exact analytic outgoing solution; no sponge, no absorbing layer, no far-field truncation`.
- **G9.** **Frozen:** `cond(system matrix) <= 1e12 at every sampled k·r_core in the certified band k·r_core in [1e-8, 4]` — measured worst `5.0202e+10` (at the band bottom `k·r_core = 1e-8`, as expected). The band bottom is set by **matrix conditioning, not by a CFL floor** — the whole point of the D3 frequency-domain ruling.

---

## §3 — THE GATE-FIREABILITY SELF-TESTS (a gate that cannot fail is not a gate)

**Frozen:** `gate_fireability_selftest_pass = FT-1 AND FT-2 AND FT-3 AND FT-4 all FIRE at their frozen thresholds` — **`True`**. Every self-test is an actual run of the actual gate on a deliberately mis-specified input, shipped in the same JSON.

| # | Targets | Mis-specification | Frozen firing threshold | Measured | Outcome |
|---|---|---|---|---|---|
| **FT-1** | G1 | exterior carries a residual power-law grade `q = 0.10`; and (separately) exterior mistakenly carries the cage's orthotropy `(1.02, 0.99)` | `lame_ratio ≥ 1e-3` | `4.6477e-03` and `3.3669e-03` | ✅ **FIRES** |
| **FT-2** | G2 | a tiny cage contrast `S_rail = 0.99` | `rho_S ≥ 1e-5` | `1.0120e-04` | ✅ **FIRES** |
| **FT-3** | G5 | an ABSORBING shell, complex modulus `Im/Re = 1e-3` (a smuggled friction — exactly what R7 forbids) | imbalance `≥ 1e-2` | `2.9181e-01` | ✅ **FIRES** |
| **FT-4** | G4 | the same TM↔MA comparison evaluated OUT of the backstop's regime, at `k·r_core = 3.0` | rel `≥ 1e-1` | `6.2850e+00` | ✅ **FIRES** |

- **Frozen:** `both mis-specified profiles MUST return lame_ratio >= 1e-3` — the mis-specified profiles land `1.7e11 ×` above the G1 pass tolerance. A uniform stiffness change in the exterior does NOT break the Lamé gate (a homogeneous region is div-free at any modulus), so the mis-specification had to be a genuine INHOMOGENEITY or ANISOTROPY leaking past the cage contour — which is also the realistic profile-specification error given R1's orthotropic input.
- **Frozen:** `the contrast case MUST return rho_S >= 1e-5 at k·r_core = 1e-3` — this is the **structural-null lens**: it proves `rho_S` is a LIVE observable that a real contrast moves, not a quantity that is identically zero by construction. Without FT-2, G2's exact-zero pass would be indistinguishable from a disabled observable.
- **Frozen:** `the absorbing case MUST return |P_in - P_rad|/|P_in| >= 1e-2` — a `1e-3` imaginary modulus (0.1 % loss) produces a 29 % energy imbalance, so the Ax3 gate detects friction three orders of magnitude below the level at which it would matter physically.
- **Frozen:** `the out-of-regime comparison MUST return |rho_N_TM - rho_N_MA|/rho_N_MA >= 1e-1` — this proves G4's agreement is a **real, breakable agreement between two independent derivations**, not two evaluations of one code path. At `k·r_core = 3.0` (above the cage resonance) the two disagree by `6.3 ×`, exactly as the physics requires.

---

## §4 — HOW THE SYMBOLIC `c²` THREADS THROUGH THE OUTPUTS (D1 HELD)

**No `c²` is evaluated anywhere in stage 1.** The import is `ρ_contribution = E_trapped/c_x² · (participation)`, so the trapped-energy column depends on the held sector choice **only** through the factor `1/c_x²`. Two consequences, both shipped in `two_term_rho_report`:

**(a) The D2 sweep and the D1 choice lie on the SAME axis — which is what makes stage 1 D1-independent by construction.** `β` as defined carries the frozen symbolic label `beta = (u_trapped · P) / (rho_0 · c_x^2) — c_x SYMBOLIC, D1 HELD; no c^2 evaluated`, i.e. `β` is the PRODUCT of a magnitude and `1/c_x²`. A different sector choice does not add a degree of freedom — it relabels which member of the disclosed `β`-family is the physical one. Hence the D2 disclosed sweep is not a workaround for the held decision; it is the correct representation of it.

**(b) The LEVER LENGTH of D1 is reported as a pure dimensionless ratio, with no candidate designated.** **Frozen:** `the c^2 dependence is reported as the dimensionless candidate-swap ratio (c_i/c_j)^2 from the lattice-measured speeds, with NO candidate designated and c_EM carried as an unevaluated symbol`

| candidate swap | ratio (from I11 lattice-measured speeds) | reading |
|---|---|---|
| `c_P² → c_S²` | `(c_P/c_S)² = ` **`3.2864`** | swapping the divisor from the compression speed to the shear speed multiplies `β` by `3.29` |
| `c_S² → c_P²` | `(c_S/c_P)² = ` **`0.30429`** | the inverse |
| `c_EM` | **UNEVALUATED SYMBOL** | no lattice-measured value is on the ledger; carried symbolically |
| designated candidate | **`null`** | D1 is HELD; stage 1 picks nothing |

**Plumber-physical reading of the lever (why this number is the useful output of a held decision).** The D2 sweep spans `β ∈ {0, 1, 3}` — a factor of 3 across the whole disclosed family. The D1 swap between the two lattice-measured candidates is a factor of `3.29`. **So the sector choice alone moves `β` by more than the entire width of the disclosed sweep**: `β = 1` under one candidate is `β = 3.29` under the other, which lands just above the top of the family. That is the quantitative statement of why D1 cannot be defaulted, and it is exactly what the charter's I8 note ("`c_P` … gives the smallest inertia divisor and the largest loading; `c_S` … larger loading still") asserts qualitatively — now with the number attached, and still with nothing picked.

---

## §5 — THE R2 TWO-TERM DECOMPOSITION, kept SEPARABLE (and the R4 `r_Z` family)

Shipped as `two_term_rho_report.rows`, `columns_kept_separable = true`. **Never pre-summed**; the summed column exists only under the explicit key `rho_eff_over_rho0_if_summed_DOWNSTREAM_ONLY`.

| `β` (D2 disclosed scan) | `φ_sf` (lattice) | **term (i)** structural `ρ/ρ₀` | **term (ii)** trapped-energy `ρ/ρ₀` (symbolic `c_x²`) | `r_Z` family |
|---|---|---|---|---|
| `0` | `0.489462` | `1.0` | `0.000000` | `0.543577` |
| `1` | `0.489462` | `1.0` | `0.489462` | `0.663400` |
| `3` | `0.489462` | `1.0` | `1.468386` | `0.854019` |

- **term (i) carries its own honest flag:** `structural dipole term NOT BUILT (n=1 channel absent in stage 1)`. In the `n = 0` channel at leading order the structural effective density is the volume average, which for a pure STIFFNESS grade at uniform substrate inertia is exactly `1` — the same anchor #782/#796 carry. The DYNAMIC (dipole) part of the charter's C2 term-(i) is the `n = 1` object stage 1 does not build (§7).
- **term (ii) carries its symbolic-`c²` label in the column itself** (the frozen string above), so the D1 dependence is visible in every row rather than buried inside a single summed number.
- **The `K` factor is the lattice input, not a recomputation.** **Frozen (R4):** `r_Z must NOT recompute or perturb K_eff/K_0` — the `r_Z` family uses `K_tan/K_0 = 0.2954759` read from the #796 JSON, and the instrument's own static-compliance ratio (used only inside the G2 null check) is explicitly NOT presented as `K_eff/K_0`.
- **MIXED-provenance carried as #796 requires.** **Frozen:** `any stage-1 output that carries the #796 r_Z cites it as MIXED-provenance (K derived, rho assumed at rho_eff/rho_0 = 1); the #796 rho half is UNRESOLVED and stage 1 does not repair it`. The `β = 0` row (`r_Z = 0.543577`) IS #796's structural anchor, reproduced here as an arithmetic identity — not as an independent measurement.
- Every row is labelled `DEMONSTRATION — no verdict banked`.

**★The D5 profile input, and its disclosed gap.** **Frozen:** `the D5 profile gains are computed from the shipped vessel_state_rve_results.json fields (min_kse, peak_A, k_a_RHO_STAR, k_s_KS0) at driver runtime; no vessel-state number is retyped from prose`. Read at runtime: `min_kse = 0.35299364830704594`, `peak_A = 0.13946745063352736`, `k_a = 9.77337`, `k_s = 1.0` ⇒ `radial_gain = 0.352994` (radial-soften), `hoop_gain = 2.363067` (hoop-stiffen), i.e. `ε_radial = −0.0662009`, `ε_hoop = +0.1394675`. **Frozen:** `the D5 vessel-state EXTREMA are lattice-measured; the radial SHAPE between them is an ENGINEERING CHOICE — #796 shipped no resolved radial profile, and its C-V shell reconstruction is corroborative-only by its own grading`. This is a flag, not a fix: D5 said "feed the measured profile", and what exists to feed is two measured extrema, not a profile.

---

## §6 — INSTRUMENT-LIVENESS DEMONSTRATION (NOT a verdict)

`stage 1 banks NO physics verdict; every physics-shaped number in these outputs is an INSTRUMENT-LIVENESS DEMONSTRATION and is labelled DEMONSTRATION — no verdict banked`. Reported so the reader can see the observables move; **nothing below is banked, cited downstream, or compared to a corpus claim.**

| profile arm | source fitting | `rho_N` (matched-asymptotics, `k→0`) | fitted `p` over the sub-resonant tail | `rho_N` at `k·r_core = 0.3` | at `3.0` |
|---|---|---|---|---|---|
| isotropic baseline | displacement | `0.413549` | `3.2e-08` | `0.431136` | `3.012703` |
| isotropic baseline | traction | `0.439371` | `3.2e-08` | `0.457842` | `1.244858` |
| D5 orthotropic (measured) | displacement | `0.026520` | `5.1e-08` | `0.028321` | `0.232244` |
| D5 orthotropic (measured) | traction | `0.028433` | `4.8e-08` | `0.030268` | `1.159893` |

**Frozen (R6-iii):** `no exponent or quasistatic quantity is read above k·r_core = 1e-3; the resonant band is reported as characterization only`.

**★Why the fitted `p ≈ 0` is NOT a test of the charter's F2, and must not be read as one.** The `n = 0` **centred-source** channel is **analytically** `k`-independent in the deep-quasistatic limit: radiated power `∝ k⁴|B|²` for BOTH the caged and the uncaged arm, so the `k⁴` prefactor cancels identically in the ratio and `rho_N → |B_caged/B_uncaged|²`, a static-compliance ratio. The measured `p ~ 5e-8` is that theorem reproduced numerically to eight digits — a **channel property**, not a measurement of a physical exponent. The charter's frozen form F2 (`p = 2`) is derived in `research/2026-07-20_deep-rail-kscaling_derivation.md` §1 for a source **DISPLACED** from centre; that is an `n = 1` statement (§7). **No stage-1 output validates or refutes F2, and none is presented as doing so.**

**One consistency observation, reported not banked.** The cold medium built from the lattice-measured speeds implies `ν = 0.281313`, versus the canonical `ν_Hill = 2/7 = 0.285714` (`ave.core.constants.N_NU`) — a `−1.54 %` deviation. This is a property of the #796 shipped speeds, not of this instrument; it is recorded in `cold_medium.nu_rel_dev_vs_canon` so a downstream lane that needs the two to agree knows the size of the gap. **No claim is made about which is right.**

---

## §7 — THE C1/C2/C3 vs X1/X2/X3 FENCE: what stage 1 certifies and what it explicitly does NOT

**CERTIFIED (instrument-class only):**
- **S1** — the radial-channel machinery is correct against analytic limits: layer assembly, the static Lamé limit, the orthotropic layer (exact, not approximate), outgoing-radiation matching, and lossless-reactive bookkeeping, all to the §2 tolerances.
- **S2** — the deep-quasistatic band is REACHABLE and its floor is MEASURED: `k·r_core ∈ [1e-8, 4]` at `cond ≤ 5.02e10`, with the floor set by conditioning, **not** by a CFL limit. The lattice's `O(1)` confinement (`deep-rail-kscaling_derivation.md` §2) is cleared by **eight decades**.
- **S3** — the gates are FIREABLE: all four self-tests fire with `≥ 10 ×` margin on their thresholds.
- **S4** — the instrument ACCEPTS the R1 orthotropic profile and the D5-measured numbers, and produces the R2-separable outputs in the frozen format.

**NOT settled by stage 1:**

| | Statement |
|---|---|
| **C1 — the deep-quasistatic single-core exponent `p`** | **NOT delivered.** The band is reached (S2) and the observable is live, but the charter's F2 target `p = 2` is a DISPLACED-source (`n = 1` dipole) statement — see X5. The `n = 0` centred-source exponent is `0` **analytically**, so it is not the same question. |
| **C2 — the net acoustic `ρ_eff` sign with both terms present** | **NOT delivered.** Term (ii) is not evaluable while D1 is HELD (by design), and term (i)'s dynamic part is the `n = 1` object — see X5. Stage 1 delivers the SEPARABLE REPORTING FORMAT for C2, not C2's answer. |
| **C3 — `r_Z(φ)` with both `Z` factors** | **NOT delivered.** The `r_Z` family in §5 is an arithmetic composition of the lattice `K` input with the D2 sweep — its `β = 0` row is #796's structural anchor by identity. Both `Z` factors are still not independently measured anywhere in this corpus. |
| **X1 — derive `β`** | Unchanged from the charter: needs self-bound soliton dynamics. Stage 1 PROPAGATES the D2 sweep; it does not generate `β`. |
| **X2 — adjudicate the import's truth** | Unchanged; and stage-1-specific: **D1 is untouched**, so no trapped-energy magnitude is evaluated at all. |
| **X3 — ensemble aggregation (`N > 1`)** | Unchanged from the charter; not approached. |
| **X4 — any physics verdict of any class** | Explicitly NOT banked (§6). |

**★X5 — THE LOAD-BEARING SCOPE FINDING (flag-don't-fix; surfaced, not reframed).** The charter §2 specifies a **spherically-symmetric** instrument, and §4 assigns it C1 and C2. Building it exposes that the `n = 0` channel cannot host either object, and this is a property of the CHANNEL, not of the implementation:

- **C1's F2.** `research/2026-07-20_deep-rail-kscaling_derivation.md` §1 Step 1, spherical-cavity reading, verbatim: *"For a source at the exact center of a `p = 0` shell of radius `r_core`, the exterior compression is *perfectly* shielded below the fundamental cavity resonance … A source **displaced from center** by `~r_core` … leaks its leading uncancelled multipole with amplitude `∝ (k·r_core)`, hence radiated POWER `∝ (k·r_core)²`."* The `(k·r_core)²` — the frozen form F2, `p = 2` — is the DISPLACED-source result. A displaced source in a spherically-symmetric cage radiates through the **dipole (`n = 1`)** channel. A strictly spherically-symmetric instrument has no `n = 1` channel, so **F2 is not testable on the chartered object.**
- **C2's term (i).** The long-wavelength effective-DENSITY correction of an inclusion (the "soft inclusion trends DOWN, bubble-like" added-mass the charter names) is carried by the **dipole (`n = 1`)** scattering coefficient; the `n = 0` monopole coefficient carries the effective COMPRESSIBILITY. So the `n = 0` channel measures `K`-side physics, not `ρ`-side physics.

**Frozen disclosure carried by every stage-1 output:** `n=0 monopole channel only; the n=1 dipole channel (F2 displaced-source p, and the structural added-mass term of rho_eff) is NOT built in stage 1`.

**Disposition (routed, not decided here).** The `n = 1` (coupled P–S) radial channel is a tractable extension of the SAME certified machinery — a `4×4` transfer matrix on two potentials instead of a `2×2` on one — and it inherits every gate certified here. Whether stage 2 builds it, or whether the charter's §2 object should be amended to say so explicitly, is Grant's / the auditor lane's call. **This lane does not draft the charter amendment** (the auditor lands charter-level changes), and **does not silently redefine C1 or C2 to fit what the `n = 0` channel can do.**

---

## §8 — Deviations, disclosures, and the mutual-satisfiability record

1. **Tolerance scouting, disclosed.** The §5 frozen tolerances were feasibility-scouted on an **uncommitted scratch prototype** before the freeze, per the prereg §9. Only feasibility and headroom were scouted; **no physics observable was scouted, and no tolerance was moved after any gate ran.** **Frozen:** `no adjudication criterion may be dropped or relaxed post-hoc to convert a FAIL to a PASS` — nothing was relaxed; every gate passed on its first shipped run.
2. **The mutual-satisfiability check paid off (the #796 Protocol-E lesson applied).** #796's root cause was frozen preconditions that could not co-exist (`k·r_core ≪ 1` required, `k·r_core ≈ 2–4` realizable). The stage-1 prereg §9 ran that check BEFORE freezing and found the analogous conflict in advance: **a requirement that the TRANSFER MATRIX reach the physical constituent regime `k·r_core ~ 1e-25` is UNSATISFIABLE in double precision** (the two basis solutions differ by `~x^(−3) ~ 1e75`). It was therefore never frozen. **Frozen instead:** `below k·r_core = 1e-8 the matched-asymptotics backstop is the instrument of record; it is k-independent in that limit and is certified against the transfer matrix in the overlap band [1e-8, 1e-3]` — and the certification run confirms that overlap is real and five decades wide (G4). **This is the direct reason D3's ruling had to be (a)+(c) and not (a) alone.**
3. **Layer-allocation design note.** An `r`-uniform layer allocation converges only first-order on this grade (`~7 %` per doubling at `n = 192` in scouting); the frozen allocation is log-uniform in the grade `S`. Frozen in the prereg before the run; tagged `[engineering-choice]`.
4. **No figure shipped.** This lane produced no figure; the certification content is a gate table, which the result doc and the JSON carry directly. (Had a figure been produced it would follow the white house style via `ave.viz.style.apply`.)
5. **Wall-clock disclosure.** The lane exceeded the ~2 h wall-clock checkpoint during the driver build; disclosed rather than truncated. The certification run itself is `1.11 s`.
6. **Fences held.** Engine `src/ave` **BYTE-UNTOUCHED** (`git diff --stat origin/main -- src/ave` empty). No `manuscript/` or KB leaf edit. No port-register, no falsification-ledger, no charter edit. Mints no `clm-`/`def-`. `make verify` green; frozen-provenance gate 0-gating; docket-key lint green.

**Ledger tags (`consistency-vs-emergence`).** `lame_ratio`, `rho_N`, `rho_S`, `r_Z`, the gate residuals and the conditioning numbers are `[derived]` dimensionless ratios, **CONSISTENCY-class** (analytic-limit reproduction). `c_P`, `c_S` and the D5 gains are `[lattice-measured]`; the radial SHAPE is `[engineering-choice]`; `ν_Hill = 2/7` is `[canon]`, read-only. `β` is a `[disclosed-scan]` with an OPEN magnitude (`clm-m5swh9`); `c_x²` is `[OPEN — HELD]` and never evaluated; the E=mc² trapped-energy inertia law is `[TAGGED IMPORT — NOT DERIVED]` (charter I5) and is never promoted to derived. `α`-CLEAN. **Frozen:** `stage-1 outputs are CONSISTENCY-class (analytic-limit reproduction) or ENGINEERING-class (numerics); no manifestation- or emergence-class claim is made`.

---

## §9 — Consequences ROUTED (this lane surfaces; it does not land)

1. **X5 — the `n = 1` channel gap.** The charter's C1 and C2 are not reachable on the chartered `n = 0` object. Routed to Grant / the auditor lane as a charter-scope finding with the verbatim source quote (§7). No charter edit made here.
2. **The `ρ_N` convention conflict** between charter R5(b) (`ρ_N → 0`) and #775 (`ρ_N` = a ratio, `= 1` with no scatterer). Both observables frozen and shipped (KEEP-BOTH); the convention question is routed, not decided (§2).
3. **D5's missing radial profile.** #796 shipped extrema, not `ε(r)`. Whether a resolved profile is obtainable is #796's OWED-2 territory, already routed to Grant; stage 1 only records that D5's instruction is currently under-supplied by the corpus (§5).
4. **D1 remains HELD** and stage 1 has not consumed it. The §4 lever number (`(c_P/c_S)² = 3.286`, wider than the whole D2 sweep) is offered as input to Grant's walk, not as a nudge toward any candidate.
5. **The `ν` gap** (`0.281313` lattice-implied vs `2/7` canonical, `−1.54 %`) is recorded for whichever lane needs the two to agree. No claim made.

---

> **Result-doc provenance.** The stage-1 certification RUN of the frozen prereg `research/2026-07-28_continuum-radial-solver-stage1_prereg-FROZEN.md`, under Grant's 2026-07-28 rulings (`"D2: disclosed, D3: follow rec, D4: do it, D5: do the rec"` `[sic]`) with **D1 HELD**. Driver `research/drivers/continuum_radial_solver.py`; all numbers read from the shipped `research/drivers/continuum_radial_solver_stage1_results.json` (driver-generated, never hand-edited). **CLASS WITHDRAWN → `C_NOT_CERTIFIED_VOID`** (2026-07-28, on the PR #801 adversarial review): G3 and G2 each divided two bit-identical computations and therefore could not fail, which voids the certification exactly as hard as a failing gate (prereg §6/§8). The as-shipped claim was nine gates PASS / four self-tests FIRE; it is withdrawn, not restated, and is re-earned only by the repaired re-run recorded in §1. **Banks NO physics verdict.** Two flag-don't-fix surfaces routed unreframed: the `n = 0`-channel scope finding (X5, §7) and the `ρ_N` convention conflict (§2). Engine byte-untouched; mints no `clm-`/`def-`; no leaf, port-register, ledger or charter edit. Companions: the frozen prereg, the merged charter **#789**, merged **#796** (`research/2026-07-22_vessel-state-rve_result.md`, the D5 profile source and the Protocol-E mutual-satisfiability lesson), merged **#782** (`research/2026-07-21_rve-aggregation-bench_result.md`, the `r_Z` discriminator and the Lamé gate), merged **#775** (`research/2026-07-20_deep-rail-kscaling_derivation.md`, F2 and the regime gap), and the docket fragment `_orchestration/docket-entries/2026-07-28-continuum-radial-solver-stage1.md`.
