# RESULT — Flag-F three-form contrast battery (Stage 2, frozen-tree outcome)

> **SECTOR HEADER.** MODE: three-form 0D contrast on one `(V,I)` protocol. REGIME: near-yield Regime II→III. CLASS: **CONSISTENCY** (derived forms vs the `#735` engine-measured `0.911` datum, not CODATA). DISCIPLINE: frozen tree governs (Rule-11); engine BYTE-UNTOUCHED; deviations disclosed as findings.

**Date:** 2026-07-19 · **Lane:** implementer, Flag-F Stage 2 · **Branch:** `feat/flag-f-s-dynamics` · **Prereg (frozen-by-push):** `research/2026-07-19_flag-f-s-dynamics_prereg.md` · **Sidecar:** `research/2026-07-19_flag-f-s-dynamics_result.json` · **Derivation:** `research/2026-07-19_flag-f-s-dynamics-derivation.md`.

---

## 1. Headline

**The derivation ruled world (a) reactive at the near-yield crossing; Stage 2 confirms the derived `ζ`-family structure empirically and shows the `#735` `0.911` datum is DEGENERATE (does not discriminate reactive-vs-memristive).** The genuine discriminator is the **loop SHAPE CLASS**, not the peak location:

| Form | `ζ` | `(r,S)` peak | `(V,I)` peak | fundamental phase | **shape class** |
|---|---|---|---|---|---|
| **S** shipped Eq 2.1 (`k4_tlm.py:283,291`) | `∞` (1st-order) | **0.968** (pinned ~1) | **0.912** (= `#735` 0.911) | max **83.9°** (caps ~90°) | **DEBYE** |
| **R** reactive world-a | `0.1` | tracks `ω_S` | **tracks `ω_S`** (slope 1.01, corr 1.00) | **179.7°** (full 180°) | **RESONANT** |
| **T** transductive world-b | `1.0` | tracks `ω_S` | tracks `ω_S` (slope 0.51, corr 1.00) | 176.6° | **RESONANT** (broadened) |

- **Axis (iii) shape class (structural, parameter-robust — the real discriminator): all three forms land exactly where the derivation `ζ`-family predicts.** Form S is Debye (peak pinned at `ωτ≈1` — the F-B1 theorem-of-the-observable — and phase caps at 90°, as a first-order kernel must). Forms R/T are Resonant (`(V,I)` peak **tracks `ω_S`**, corr 1.00, and the phase sweeps the full **180°** through resonance — the `#735` F-B3 corrected signature). **The derivation's damped-bow-oscillator family is empirically confirmed.**
- **Axis (i) peak location (tunable): `DATUM-DOES-NOT-DISCRIMINATE`.** Form S reproduces `#735`'s `(V,I)` peak `0.912 ≈ 0.911` (inside legacy `[0.85,0.95]`); the derived reactive Form R **also** reaches `0.911` — at `ω_S ≈ 0.91`, an **O(1)** value fully consistent with the derived `ω_S ~ 1/τ_relax` (§2.4 of the derivation). Both the shipped-memristive form AND the derived-reactive form land on the datum ⇒ the single `0.911` peak is **degenerate**; it cannot tell reactive from memristive.
- **Axis (ii) origin-pinch: NO for all three forms** (drive `r∈[0.4,1.0]` never crosses `r=0`; the `#735` F-B2 finding confirmed across all forms).

**Net:** Stage 2 corroborates the derivation and sharpens the forward test. The reactive branch (Grant's lean) is **not** falsified by the `0.911` datum — it fits it as well as the memristive branch. The observable that DOES separate them is the **shape class**: a resonance that *tracks the operating point* and *inverts phase through 180°* (reactive) versus a Debye lag *pinned at `ωτ=1`* that *caps at 90°* (shipped Eq 2.1). `#735`'s single-point measurement sits exactly on the degeneracy.

## 2. Gates (fail-closed, checked FIRST — all fire)

| Gate | Result |
|---|---|
| **G0 regime** | drive reaches Regime III, `max r = 1.0` — fires |
| **G1 finite** | every swept point of all three forms finite — fires |
| **G2 byte-match (load-bearing)** | Form S per-step update **bit-identical** to a live `K4Lattice3D(use_memristive_saturation=True)` driven at one site, **`rel = 0.0`** (`test_flag_f_s_dynamics.py::TestG2ByteMatch`, `k4_tlm.py:291` verbatim) — fires |
| **G3 reactive audit** | reactive FFT steady-state ODE residual **machine-zero** (`<1e-10`); `ζ=0` off-harmonic loop area **machine-zero** (lossless world-a confirmed) — fires |

## 3. The decision tree, walked (frozen §6, precedence top-down)

1. Gates pass (§2).
2. **Axis (iii) shape class decided first (parameter-robust):** Form S = Debye ✓; Forms R/T = Resonant ✓. `all_as_derived = True`. **The driver does NOT contradict the derivation** — the `ζ`-family (`ζ=0 / 0<ζ<∞ / ζ→∞` = reactive / transductive / shipped) is realized as derived. No flag-to-Grant on this axis.
3. **Axis (i) peak-location discrimination:** `forms_in_window ≥ 2` (Form S at `0.912`; Form R at `ω_S≈0.91`) → **`DATUM-DOES-NOT-DISCRIMINATE`**. Banked as the honest outcome; the true discriminator is routed to Axis (iii).
4. **Axis (ii):** reported as a registration-quality caveat (no origin-pinch, all forms), not a gate.
5. **Precedence:** Axis (iii) structural **outranks** Axis (i) tunable. Final verdict: **the shape class separates the branches; the peak-location datum does not.**

## 4. What this means for the fork (routed to Grant; the derivation already ruled)

The derivation (`-derivation.md` §8) ruled **world (a) at the near-yield crossing** on structural grounds (the memristive loop is appreciable only at `ωτ~1`, exactly where the Markovian reduction producing Eq 2.1 fails). Stage 2 adds the *empirical* content the `#735` C-3 SPEC promised but never ran (the reactive second-order contrast):

- The reactive form is **real and well-defined** (bounded steady state, exact ODE solution) and carries the **resonant + 180°-phase-inversion signature** that a first-order Debye kernel structurally cannot (`#735` F-B3, now demonstrated not just asserted).
- The `0.911` `(V,I)` peak `#735` found "leaning toward the memristive window" is **degenerate** — the reactive branch reproduces it at an O(1) `ω_S`. So that datum does **not** weigh against Grant's reversible-reactive lean; it is consistent with both.
- **Forward discriminator (the real test, for a future driver/bench):** sweep the operating point (`r_0`) or the drive and ask whether the near-yield `(V,I)` loop-area peak **moves with a resonance** (reactive: peak tracks `ω_S`) or **stays pinned at `ωτ≈1`** (Debye/shipped); and whether the fundamental phase **inverts through 180°** (reactive) or **saturates at 90°** (first-order). These are parameter-robust and are what actually separate the branches.

## 5. Deviations disclosed (Rule-10 / Rule-11; frozen tree not retro-edited)

1. **Exact frequency-response (FFT) steady-state for Forms R/T** — instead of time-stepping with a settle. Discovered at build time (Rule-10): the reactive ODE is *linear* in `S` with periodic forcing, so its exact steady state is `irfft(rfft(S_eq)·H(Ω))`. This eliminates all transient/settle artifacts and the pure-`ζ=0` secular-resonance blow-up concern, and the G3 gate confirms it solves the ODE to machine precision. An improvement over the prereg's implied time-stepping; verdict-invariant.
2. **`ζ=0.1` (not exactly 0) for Form R** (prereg §2, anticipated) — a pure undamped `ζ=0` oscillator is secularly unbounded when a drive harmonic hits `ω_S` exactly; `ζ=0.1` is the physically-realized near-crossing underdamped form with a well-defined Lorentzian resonance. The `ζ=0` *lossless* property (zero loop) is separately confirmed off-harmonic (G3).
3. **Form S `(V,I)` peak fine-refit** — the 60-pt log grid lands the coarse argmax at `0.885`; the fine sub-grid refit (same method `#735` froze, `leg_b_loop_area.py:58`) gives **`0.912`**, matching `#735`'s `0.911`. Both coarse and fine land in `[0.85,0.95]`; verdict-invariant.
4. **Test location** — placed in `src/tests/` (pytest `testpaths`) not the research lane dir (prereg §8), following the `#735` convention so `make test`/`make test-engine` discover it. Disclosed; the prereg's intent (a passing byte-match + reactive-audit test) is satisfied.
5. **Sub-rupture (`Δr=0.25`) KEEP-BOTH** run for Form S (`peak_rS`) and Form R (`in_window_legacy`, peak-slope) — same shape-class conclusions; stored in the sidecar.

## 6. Status tags

- **DERIVED (Stage 1):** world (a) reactive at the crossing; Eq 2.1 = the `ωτ≪1` overdamped-Markovian slow-limit; the three forms as one `ζ`-family. (`-derivation.md`.)
- **VERIFIED (Stage 2):** G2 live-engine byte-match `rel=0`; G3 reactive ODE residual machine-zero + `ζ=0` lossless; the `ζ`-family shape classes (Debye vs Resonant) realized as derived; Form S reproduces `#735`'s `0.911`. `make verify` PASS; 11/11 tests pass.
- **BANKED (frozen bins):** Axis (iii) all-as-derived; Axis (i) `DATUM-DOES-NOT-DISCRIMINATE`; Axis (ii) no origin-pinch.
- **ROUTED TO GRANT:** the framing flag (rotation-wording vs canonical load-response, `-derivation.md` §9 Flag 1); the forward discriminator (§4) as the real reactive-vs-memristive test.

## 7. Owed follow-ons (NOT landed — collision fences honoured)

- **Doc #59 Flag F** → "RESOLVED: Eq 2.1 is the `ωτ≪1` overdamped-Markovian limit of the z=3-coupled node; near-yield (`ωτ≳1`) is world-(a) reactive; the `0.911` datum is degenerate between reactive and memristive." Owed post-merge pointer; **PR #738 owns #59 this session** — not edited here.
- **`tau-relax-derivation.md` / `#59` §10** "unbuilt" staleness (already flagged by `#735` §5) + Eq 2.1's regime-of-validity (`ωτ≪1`). Owed KB follow-on; **cleanup lanes own KB this session** — not touched here.
- **`axiom-register.md` Ax4** cross-link (load-response bifurcation also fixes the near-yield *dynamics* class = reactive). Owed; **auditor lands manual entries**.
- **Docket** continuation entry for this lane's ruling + firing (union driver, safe) — appended.

---

*Run 2026-07-19 by Opus 4.8 (implementer lane) per the yield-fork adjudicator dispatch. Frozen tree governed the verdict; deviations recorded as findings (Rule-11: no retro-edit). The derivation's world-(a) ruling stands; Stage 2 corroborated it and located the true (shape-class) discriminator.*
