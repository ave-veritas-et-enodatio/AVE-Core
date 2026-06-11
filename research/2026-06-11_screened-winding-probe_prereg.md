# PREREG — THE SCREENED-WINDING PROBE: is `w_pol ≡ 0` a genuine absence or an APPARATUS SCREEN?

**Date frozen:** 2026-06-11
**Branch:** `analysis/2026-06-11-screened-winding-probe` (off `origin/analysis/2026-06-10-genesis-v6-transducer` @ `7484dd0b`)
**Engine:** `src/ave/core/unified_genesis_engine.py` (the v6 transducer build) + `src/ave/utils/fast_winding_extractor.py` (the `(2,3)` reader) + `src/ave/core/crystal_graft_v4.py::seed_omega_known_2_3` (the validated plant)
**Governing discipline:** `ave-apparatus-floor-attribution v1.1` — ORDERED BINS (floor-check gates every positive; the deflationary explanation is ruled OUT before the exciting bin is awarded); PROBE-CAPABILITY (the never-run KNOWN-POSITIVE: a validated `(2,3)` planted inside a real shell, read through the same apparatus); every knob inventoried + swept (§5). **§210-COMPLIANCE GATE: the run executes every sweep this prereg mandates, or states the deviation explicitly BEFORE running and re-bins. A positive whose governing knob was unswept is CLIP by this prereg's own law.**

**Skills fired at design time (recorded):**
- `substrate-native-check` (CP4 phase-space-vs-real-space + CP10 boundary-not-bulk — walked §2): the winding is read in PHASE-SPACE (the ω/π_ω phasor winding around torus contours), the snap erases REAL-SPACE `u_adv`. These are DIFFERENT coordinates — the crux of the screening question.
- `phase-space-coordinate-check` (A46): the corpus `(2,3)` claim lives in phasor coordinates; the extractor `extract_2_3_omega_fast` reads `arg((ω·ê)+i(π_ω·ê))` winding around the torus — coordinate-MATCHED. The screening test is therefore informative (it is NOT a real-space φ² mismatch). The hazard A46 names is INVERTED here: the snap acts in real-space, the read is phase-space, so a real-space clamp can only screen the phase-space read THROUGH the dynamics, not by direct erasure of the read channel — see the §1 inventory.
- `pre-test-physics-check` (one plumber question surfaced to Grant BEFORE design — §0.5).
- `ave-discipline-translate` Step-3.5 (the fluid vortex-ring / entrainment lens — §2.5).
- `consistency-vs-emergence`: this probe is **MANIFESTATION/consistency-class** — it asks whether the apparatus FAITHFULLY READS a KNOWN-PLANTED topological invariant through a shell. It does NOT promote any emergence claim; no CODATA/manuscript target is compared. (§6.)
- `verify-before-cite`: every engine line + prior-verdict anchor below is grep/JSON-confirmed this session against `7484dd0b`.
- `flag-don't-fix`: §1 surfaces a CHANNEL-MISMATCH between the apparatus confession as stated in the directive and what the engine actually does — surfaced verbatim, NOT silently reconciled.

---

## 0. THE PRIOR VERDICT BEING RE-SCOPED (verify-before-cite, grep-confirmed)

From `research/2026-06-10_genesis-v6-transducer_result.md` (the v6 MAIN product, N=48, `n_build=3200`, snap onset step 3396, K3 stop 4000):

> "`w_pol` does NOT become a quantized winding: it is **0 across the ENTIRE χ̃ ladder {0, 9e-4, 0.005, 0.02, 0.08} AND the entire ω-recipient ladder {0, 0.5, 1.0}**; the lone `w_pol=1` at the MAIN 3200-build sits AT the reliability floor (rel **0.109** vs the 0.1 gate), does NOT track the coupling, and **appears in the achiral arm too** — it is a floor-grazing read, not a coupling-driven `(2,3)`. The poloidal **"3" never forms.**"

That verdict was read from contours sampling the product field. **It has NEVER been validated that the apparatus can read a winding that is genuinely PRESENT inside a formed shell.** That is the gap this prereg closes: the never-run known-positive. The five FROZEN bins (§4) re-scope the prior verdict to exactly one of: {the apparatus screens interior reads (the verdict is unresolved-outside) / the apparatus reads faithfully and the verdict STANDS / the winding is genuinely absent even inside (the STRONGEST form of the verdict) / a phase-dependent structure the settled-average erased / UNRESOLVED}.

---

## 0.5 PRE-TEST PHYSICS CHECK — the plumber question surfaced to Grant BEFORE design

**The question (Rule 16: asked BEFORE design, not after 30 commits):** the v6 product's D9 transducer deposits the extracted photon-helicity into TWO possible channels — the bulk `u_adv` orbital circulation (fraction `1 − omega_recipient_frac`) and the Cosserat ω micro-rotation (fraction `omega_recipient_frac`, DEFAULT 0.0). The `(2,3)` extractor reads ONLY ω/π_ω. The snap zeros ONLY `u_adv` (§1). **So at the MAIN build's `omega_recipient_frac=0.0`, the entire transduced winding went into the ONE channel the extractor does NOT read — AND that channel is the ONE the snap zeros inside the shell.** The "screening" hypothesis and the "wrong-channel" hypothesis are therefore CONFOUNDED in the product alone. Only ARM 1 — planting a validated `(2,3)` DIRECTLY into the ω channel the extractor reads, inside a real shell — separates them. **Plumber framing:** we are asking whether the shell is an opaque pipe wall (screens the gauge) or whether the gauge was simply plumbed to the wrong port the whole time. The known-positive plant tells us which.

---

## 1. THE APPARATUS CONFESSION + THE SNAP-ERASURE INVENTORY (the load-bearing section — this list IS the screening model of the apparatus)

**THE CONFESSION (verify-before-cite, exact cite @ `7484dd0b`):** the snap state machine zeroes interior advective velocity at every snapped cell, every step:

- `src/ave/core/unified_genesis_engine.py:396` — `self.u_adv[cm] = 0.0` (where `cm = self.snap_mask`, line 385). Any bulk advective circulation entering a snapped cell is **erased by bookkeeping** on the next snap substep.
- `src/ave/core/unified_genesis_engine.py:344` — `self.u_adv[newly] *= (1.0 - self.chi_shock)` (the crossing-KE removal on newly-snapped cells; `chi_shock=1.0` default ⇒ FULL removal).
- `src/ave/core/unified_genesis_engine.py:393` / `:395` — `self.rho_bar[cm] = self.snap_clamp_val[cm]` (conservative) / `= self.rho_cav` (legacy): the bulk density is clamped to the void floor (the `Z_bulk→0` reflector; the EOS hyperbolicity floor goes to `c2_floor=0` in snapped cells).

**WHAT THE SNAP ERASES (clamped/zeroed in snapped cells, EVERY step):**
| field | what happens | line |
|---|---|---|
| `u_adv` (bulk advective velocity, 3-vec) | **→ 0.0** at every snapped cell | `:396` (+ `:344` on newly-snapped) |
| `rho_bar` (bulk volumetric density) | **clamped to the void floor** | `:393` / `:395` |
| bulk EOS hyperbolicity `c_bulk²` | **→ 0** (the reflector BC) | `:110-113` (c2_floor override) |

**WHAT THE SNAP PRESERVES (NEVER referenced by the snap machinery — grep of `_tally_latent_and_snap`, `_meissner_harden_neighbors`, `_snap_step`, lines 304–419, returns ZERO writes to these fields; they continue to evolve under the UNCHANGED parent `CrystalGraftV4.step()`, called at `:852`):**
| field | role | carried by |
|---|---|---|
| `omega` / `omega_prev` | the Cosserat micro-rotation = **the `(2,3)` WINDING the extractor reads** | parent `CrystalGraftV4` (`crystal_graft_v2.py:101-102`) |
| `pi_omega` = (ω−ω_prev)/dt | the ω LC-conjugate (the poloidal "3" phasor's imaginary axis) | parent |
| `w` / `w_prev` | the photon shear (helicity source) | parent |
| `V` / `V_prev` | the longitudinal scalar (dilatation mass) | parent |

**THE FLAG (flag-don't-fix — surfaced, NOT reconciled):** the directive's apparatus confession — *"any circulation entering the shell is erased by bookkeeping"* — is **EXACTLY TRUE for `u_adv`** (the bulk velocity circulation; `:396`). But the winding the `(2,3)` extractor reads is the **Cosserat ω**, and the snap **does NOT touch ω**. So the apparatus carries TWO homonymous "circulations" (cf. the electron's two homonymous "3"s):
  1. `u_adv` bulk-velocity circulation Γ = ∮u·dl — **ERASED inside the shell** (`:396`).
  2. ω Cosserat winding (the read channel) — **PRESERVED inside the shell**.

**The screening model that follows directly:** a planted ω ring inside a snapped shell is NOT directly erased (the snap never writes ω). It can only be screened INDIRECTLY — if the bulk discontinuity at the shell (the `u_adv→0`, `rho_bar→floor` step) perturbs the parent ω evolution near the shell, or degrades the extractor's trilinear-interpolation / reliability mask on contours that cross snapped cells. The arms measure exactly this. **The naive read of the directive ("the snap erases the winding") is FALSIFIABLE by this inventory and is the SCREENED-READ-CONFIRMED bin's burden of proof** — it must be SHOWN, against the inventory's prediction that ω survives, that the inside ω read is nonetheless suppressed at outside contours.

---

## 2. SUBSTRATE-NATIVE CHECKPOINTS WALKED (before the first line of probe code)

- **CP4 (phase-space vs real-space) — THE load-bearing one.** The winding is a PHASE-SPACE invariant: `extract_2_3_omega_fast` (`fast_winding_extractor.py:104-198`) computes the toroidal "2" = winding of `arg((ω·ê_R)+i(ω·ê_z))` around the major circle and the poloidal "3" = winding of `arg((ω·d̂)+i(π_ω·d̂))` around the minor circle. The read coordinate IS the corpus coordinate. The snap erases in real-space (`u_adv`, `rho_bar`). Measuring the phase-space read against a real-space clamp is informative ONLY because the question is precisely whether the real-space clamp screens the phase-space read — that is the experiment, not a coordinate error.
- **CP10 (boundary-not-bulk).** The snap is a per-cell boundary state machine (`:366-419`), not a bulk force — so its screening (if any) is a BOUNDARY-shell effect, localized to the snapped annulus. The contour-radius sweep (§5) resolves the shell boundary explicitly.
- **CP2 (coupled channels).** The probe does NOT add a solver or an objective; it READS the existing coupled `V ⊗ w ⊗ ω ⊗ (ρ̄,u)` field. No minimization, no new EOS.
- **CP7 (PML/interior-excluded sampling).** All contour samples and raw-field inspections are restricted to `interior_mask()`; density-peak / shell-locating uses `top-K |ω|²` with PML exclusion (A-Rule 10 corollary), NOT centroid+offset (the shell's centroid is the empty core).

---

## 2.5 STEP-3.5 — the fluid vortex-ring / entrainment lens (ave-discipline-translate v1.2)

*"What would Keith say?"* (Keith Mertens, co-author of the entrainment vortex-ring paper, arXiv 1110.3435; `research/2026-06-07_entrainment-vortex-trapping-deep-dive.md`). The shell is a **stratification interface** around a rarefied core; the planted ω ring is a vortex ring sitting in the stratified interior. The fluid lens supplies the FORM of the screening question: a vortex ring's circulation can be **reactively entrained** (added-mass = inertia — the ring drags its own circulation, which would survive the interface and read THROUGH it) OR **dissipatively confined** (viscous = the interface absorbs/reflects the circulation, screening the outside read). The snap's `u_adv→0` reflector is a HARD dissipative interface for the BULK circulation — but the ω winding is the reactive/inertial channel (the ring's own conserved micro-rotation), which the inventory (§1) shows the snap does NOT touch. **Honest ceiling (per the skill):** the fluid is a LENS (consistency-class) — it predicts the ω ring should read THROUGH the shell (reactive/inertial survives), i.e., it leans toward NO-SCREENING; it does NOT supply the number. The number comes from the arms. The lens is recorded as a PRIOR, NOT a bin-determinant — the frozen gates (§4) decide.

---

## 3. THE THREE ARMS (each gate EXECUTABLE — the v7 lesson: every gate gets an assertion in the driver)

**Probe-capability keeper (runs FIRST, before any arm):** `fast_winding_extractor.verify_equivalence()` asserts the reader returns `(2,3)` on a planted field, `(0,0)` on a null, and matches the reference reader to ≤1e-12 (`fast_winding_extractor.py:255-343`). If the keeper fails, ALL arms are CLIP (the reader is broken) → UNRESOLVED.

### ARM 1 — THE SCREENING CALIBRATION (the never-run known-positive)

Form a shell (the v6 snap recipe at MODEST scale — N and `n_build` reduced for tractability; the shell is the snapped annulus, located by `snap_mask`). Plant the validated `(2,3)` via `seed_omega_known_2_3(R, r, amplitude, p=2, q=3)` (`crystal_graft_v4.py:296`) INSIDE the shell. Read the winding from three contour families:
- **(a) OUTSIDE the shell** — torus contours at radii beyond the snapped annulus.
- **(b) INSIDE the shell** — torus contours between the core and the shell (the inter-shell annulus).
- **(c) NO-SHELL CONTROL** — the identical plant, snap OFF (the standard plant read).

**Plant-order procedure (document which fires):**
- **ATTEMPT-A (preferred):** form the shell, THEN `seed_omega_known_2_3` into the interior. Per §1 the snap does NOT write ω, so the plant should SURVIVE — A is expected to work and is the cleaner known-positive.
- **FALLBACK-B:** if A is impossible (the plant destabilizes the formed shell or the snap config forbids a post-form seed), plant FIRST then drive the bulk to form the shell around it. The result MUST state which fired (ave-driver-script-honesty).

**Screening transfer functions (the ARM-1 outputs):**
`T_a = read_a["w_pol_rel"] / read_c["w_pol_rel"]` and `T_b = read_b["w_pol_rel"] / read_c["w_pol_rel"]`.

**ARM-1 EXECUTABLE GATES (frozen thresholds §4.0):**
```
G-CAL  : assert read_c["is_2_3"] and read_c["w_pol_rel"] >= REL_MIN          # known-positive valid, else UNRESOLVED-CAL (HALT)
G-IN   : read_b["is_2_3"] and (T_b >= PASS_MIN)                              # inside read transmits the planted ring
G-OUT-S: (not read_a["is_2_3"]) and (T_a <= SCREEN_MAX)                      # outside read suppressed  -> screening
G-OUT-T: read_a["is_2_3"] and (T_a >= PASS_MIN)                             # outside read transmits   -> no screening
```

### ARM 2 — INTERIOR READS ON THE PRODUCT

The v6 MAIN product rebuilt (`UnifiedGenesisEngine` at the v6 transducer recipe — `bulk_density_on=True`, `snap_on=True`, `transducer_on=True`; `omega_recipient_frac` swept per §5 to cover the read channel). Extractor contours at SWEPT radii `r` (§5) from the core out THROUGH and BEYOND the shell. PLUS raw-field inspection inside: what do `ω`, `V`, `u_adv` actually look like in the inter-shell interior (FIGURES — `|ω|`, `|u_adv|`, `rho_bar` on a meridian slice; the snap_mask overlaid).

**ARM-2 EXECUTABLE GATES (frozen thresholds §4.0):**
```
G-PROD-RAW : omega_med_in = median(|omega| in inter-shell annulus, interior_mask)   # the field that IS there to read
G-PROD-RES : prod_best_rel = max over swept r of read_r["w_pol_rel"]                # best resolvable winding anywhere
G-PROD-NULL: (prod_best_rel < REL_MIN) and (omega_med_in <= OMEGA_FLOOR)            # nothing present to read inside
```
where `OMEGA_FLOOR = 3 * (median |omega| of the transducer-OFF baseline in the same annulus)` (the known-null field level; computed in-run, not hard-coded).

### ARM 3 — TIME-RESOLVED (phase-locked vs settled-average)

Phase-locked snapshot reads at `N_phase` phases (§5) of the dominant internal period `T₀ = 1/f₀`, `f₀ ≈ 0.052` (the self-oscillation class; the phase clock is locked to a measured internal oscillator — `wall_photon_intensity()` peaks or the ω-tank breathing, recorded in-run, NOT assumed). Compared to the settled-AVERAGE read (the `N_phase=1` baseline = the standard read the prior verdict used). A precessing/rotating interior structure shows phase-dependence the average erases.

**ARM-3 EXECUTABLE GATES (frozen thresholds §4.0):**
```
G-ENV : exists (r, p) such that read_phase[r][p]["is_2_3"] and (not read_avg[r]["is_2_3"])   # a phase resolves what the average hid
        and  ( max_p read_phase[r][p]["w_pol_rel"] - read_avg[r]["w_pol_rel"] ) >= ENV_DELTA
```

---

## 4. FROZEN BINS (ORDERED — floors first) + THE EXECUTABLE DECISION TREE (Rule 11; no post-hoc criterion drop)

### 4.0 FROZEN THRESHOLDS (set NOW, before any run artifact)
| symbol | value | provenance |
|---|---|---|
| `REL_MIN` | **0.10** | the extractor's own reliability gate — `fast_winding_extractor.py:50` ("rel>0.1 ⇒ a reliable contour") and the `is_2_3` definition `:198` |
| `SCREEN_MAX` | **0.30** | transfer ratio at/below which a contour read counts as SUPPRESSED |
| `PASS_MIN` | **0.70** | transfer ratio at/above which a contour read counts as TRANSMITTED |
| (gap 0.30–0.70) | — | deliberate dead-band ⇒ ambiguous partial transfer is forced to UNRESOLVED, never silently binned |
| `OMEGA_FLOOR` | **3× transducer-OFF baseline** | the known-null ω field level in the same annulus (computed in-run) |
| `ENV_DELTA` | **0.10** | min phase-vs-average `w_pol_rel` excursion to call ENVELOPE-STRUCTURE |

### 4.1 THE FIVE FROZEN BINS
1. **SCREENED-READ-CONFIRMED** — the planted interior ring is invisible from outside but visible inside → ALL prior external `w_pol≡0` verdicts re-scope to **unresolved-outside**.
2. **NO-SCREENING** — the planted ring reads fine from outside → the prior verdicts **STAND**.
3. **ENVELOPE-STRUCTURE** — phase-resolved reads show interior structure the average hides.
4. **ALL-NULL** — inside reads also empty → the winding is **genuinely absent** (the strongest form of the prior verdicts).
5. **UNRESOLVED** — calibration failed or ambiguous (dead-band / keeper fail).

### 4.2 THE EXECUTABLE DECISION TREE (floors-first — the deflationary explanation is ruled OUT before the exciting bin is awarded)

```
# FLOOR 0 — calibration / capability (evaluated FIRST)
if not keeper_passes:                       BIN = UNRESOLVED ; HALT      # reader broken
if not G-CAL:                               BIN = UNRESOLVED ; HALT      # known-positive failed -> no screening statement possible

# PRIMARY = ARM 1 (the calibration decides whether the apparatus screens AT ALL)
if   G-IN and G-OUT-S:                      ARM1 = SCREENED-READ-CONFIRMED
elif G-OUT-T:                               ARM1 = NO-SCREENING
else:                                       ARM1 = UNRESOLVED            # dead-band / inside-read failed

# FLOOR (ARM 2) — ALL-NULL may be awarded ONLY if ARM 1 proved the apparatus does NOT screen.
#   (You cannot call a null "genuinely absent" until "absent-because-screened" is ruled out — floors first.)
if ARM1 == NO-SCREENING and G-PROD-NULL:    BIN = ALL-NULL
elif ARM1 == SCREENED-READ-CONFIRMED:       BIN = SCREENED-READ-CONFIRMED   # product nulls re-scope to unresolved-outside
elif ARM1 == NO-SCREENING:                  BIN = NO-SCREENING              # apparatus faithful; product read is the real verdict
else:                                       BIN = UNRESOLVED

# OVERLAY (ARM 3) — independent modifier, reported alongside the primary BIN
if G-ENV:                                   BIN += ENVELOPE-STRUCTURE
```

Every line above is asserted in the driver (`assert`/explicit branch); the result doc writes the BIN FROM the evaluated booleans, not from prose. No criterion is dropped post-hoc to convert a negative (Rule 11). If the numbers land in the dead-band, the bin is UNRESOLVED — that is a permitted, recorded outcome, not a failure to be debugged toward a rescue.

---

## 5. MANDATED SWEEPS (every knob inventoried + swept; §210-COMPLIANCE GATE)

| sweep | grid (FROZEN) | arm | CLIP telltale |
|---|---|---|---|
| **contour radius `r`** | `{0.5, 0.7, 0.9, 1.0, 1.15, 1.3, 1.6} × R_shell` (core → inter-shell → at-shell → beyond) | 1, 2 | the verdict tracks `r` only at the shell boundary (expected — that IS the screening locus) vs everywhere (apparatus floor) |
| **phase count `N_phase`** | `{1, 4, 8, 16}` over one `T₀=1/f₀` (f₀≈0.052, clock locked in-run) | 3 | ENVELOPE appears only at high `N_phase` and vanishes at the convergent count (an aliasing artifact, not structure) |
| **shell thickness** | `{thin, nominal, thick}` snapped-annulus widths (via the snap recipe: drive amplitude / `n_build` / `meissner_harden`) | 1 | the transfer functions `T_a`, `T_b` track shell thickness monotonically (a real geometric screen) vs not-at-all (apparatus floor) |
| **`omega_recipient_frac`** (read-channel coverage) | `{0.0, 0.5, 1.0}` | 2 | the product interior read tracks the ω-routing fraction (the §0.5 channel-mismatch is real and separable) |

**§210 deviation policy:** the run executes EVERY sweep above, or states the deviation explicitly BEFORE running and re-bins. A positive whose governing knob was unswept is CLIP by this prereg's own law. (Scale reductions for tractability — N, `n_build` — are ENGINEERING choices, declared in the result, not goalpost moves; the FROZEN bins/thresholds do not change.)

---

## 6. CORPUS STATE + ADJUDICATION DISCIPLINE

- **OPEN.** This probe does NOT promote any candidate-claim. The NOT-ELECTRON verdict (the v5 panel) and the `w_pol≡0` product verdict (v6) STAND until this probe returns. The probe RE-SCOPES the `w_pol≡0` verdict to exactly one of the five bins.
- **consistency-vs-emergence tag: MANIFESTATION/consistency-class.** The probe tests whether the apparatus faithfully reads a KNOWN-PLANTED invariant through a shell. No emergence claim, no CODATA/manuscript-target comparison. A SCREENED-READ-CONFIRMED result is a statement about the APPARATUS (the reader's reach), not a new physics claim.
- **Rule 11 (honest closure):** the bins are frozen pre-run; the verdict is written from the evaluated gate booleans. If ARM 1 returns NO-SCREENING and ARM 2 returns ALL-NULL, that is the CLEAN strongest form of the prior verdict — recorded, branch closed, NOT debugged toward a screening rescue.
- **Rule 12 (substitution-not-retraction):** if SCREENED-READ-CONFIRMED fires, the prior `w_pol≡0` verdict docs get a 🔴 re-scope header (verdict→unresolved-outside); the slot is NOT refilled with a new winding claim — a positive interior winding read becomes its OWN new prereg with its own verification chain.
- **A44 discipline:** a SCREENED result is an APPARATUS-reach finding (the reader cannot see inside the shell), NOT a missing axiom and NOT an engine-violates-Ax3 bug. No Ax5 candidate is drafted from this probe.
- **Lane:** implementer surfaces the empirical finding + the §1 channel-mismatch flag; the auditor lands any manual/manuscript entry.

---

## 7. PHASE PLAN

- **PHASE 1 (this doc):** the prereg, committed ALONE. ✅ this commit.
- **PHASE 2:** the driver — keeper FIRST, then ARM 1 (the calibration), then ARM 2, then ARM 3; every §3 gate an `assert`/branch; every §5 sweep executed-or-deviation-declared; all numbers FROM the evolved field (ave-driver-script-honesty). FROZEN before any run artifact.
- **PHASE 3:** the result doc — the BIN written from the gate booleans; the raw-field figures (ARM 2); the transfer-function table (ARM 1); the phase-resolved table (ARM 3). Panel-clean before push + PR base `main`, review-gated.
