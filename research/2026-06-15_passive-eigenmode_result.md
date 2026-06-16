# Passive winding-protected electron eigenmode — the hybrid (V,ω) breather — RESULT

> **STATUS: COMPLETE (CORRECTED RE-RUN). BIN = NEGATIVE-A** (prereg §4), banked on the
> **F4 (winding) path** with **G1 (absolute known-positive) CERTIFIED** — at the
> **CO-RESOLVING** lattice N=26, R=5, r=2.5, dx=0.5, v_width=2.5, ~5 core cells.
>
> **This SUPERSEDES the first run's NEGATIVE-A** (banked on the F1 path / "the V-tank wall
> disperses"). An adversarial-verify panel REFUTED that as a **FALSE NEGATIVE** (two driver
> defects: under-resolution + a defective RELATIVE G1 gate). Grant ratified option (a): fix the
> defects, re-run at a co-resolving lattice. The defects are fixed; this is the corrected read.
> **The keystone was OPEN; this run closes it as a negative — but on a DIFFERENT mechanism than
> the first run, with two load-bearing flags surfaced for Grant (§5).**
>
> **Headline (the form, NOT the echo):** *at the corrected (co-resolving) resolution the V-tank
> wall-half DOES self-focus into a bounded, stable breather (F1+F2 PASS — the first run's F1
> negative was an under-resolution artifact, now certified by the absolute G1). But the
> winding-protected HYBRID breather does NOT stand: the (2,3) winding is NOT conserved on the
> ω-carrier (F4 FALSE) — so the winding-protected keystone object is absent.* **FLAG (§5): the
> F4 negative is dominated by an apparatus/framing floor — the winding was imposed as a SEEDED
> INITIAL CONDITION, not the HELD topological BC the prereg charters (§7.1); the bare ω-carrier
> disperses an un-enforced winding identically with or without the coupling.**
>
> Prereg (FROZEN): `research/2026-06-15_passive-eigenmode_prereg_FROZEN.md`.
> Driver: `src/scripts/vol_1_foundations/passive_eigenmode_driver.py`.
> JSON (SHA-pinned): `results/passive_eigenmode_coresolved_N26.json`.
> Build-step-zero G0 (PASSED, prior): `src/scripts/vol_1_foundations/g0_double_count_smoke.py`.
> Branch: `analysis/2026-06-15-eigenmode-driver` (NOT merged — Grant merges).

---

## 0 — The corrected re-run: what changed, and why (option (a))

The first run banked NEGATIVE-A on **F1** ("the coupled solve disperses; the V-tank does not
self-focus"). The panel REFUTED it as a **false negative** on two driver defects:

1. **Under-resolution.** The first run used `dx=1.0`, `v_width=3.0` → **~3 core cells** across
   the sech, in a 4×-larger box. The A1/V-tank breather is a corpus-established POSITIVE at the
   **v14 eigen-resolution** (`dx=0.5`, `SEED_RADIUS=2.5`, `amp=0.85` → **~5 core cells**;
   `src/tests/test_master_equation_v14_mode_i.py:29-36`; `research/2026-06-13_cage-stiffening-wall_result.md:12`).
   At ~3 cells the sech UNDER-RESOLVES and disperses to ~0.18 — the false negative.
2. **Defective G1 gate.** G1 was coded **RELATIVE** (`sech_retention > gauss_retention*1.10`) →
   it banked PASS while the sech retained only ~0.10. That is the **t2-genesis
   "detector-can't-certify-the-known-positive" defect**: a detector that cannot see the known
   positive is not entitled to certify its absence.

**The fixes (option (a) — co-resolving re-run, defects fixed WITHIN the frozen prereg):**

| Fix | What | Where |
|:---|:---|:---|
| **G1 → ABSOLUTE** | PASS requires `sech_retention >= 0.60` (calibrated to the v14 known-positive ~0.68) AND still > Gaussian. If the sech can't reach 0.60 → G1 FAILS → **NEGATIVE not bankable** (the interlock). | `passive_eigenmode_driver.py` `gate_G1` + `G1_ABS_RETENTION_FLOOR=0.60` |
| **Eigen-resolution seed** | `dx=0.5`, `v_width=2.5`, `v_amp=0.85` → 5 core cells (the v14 config). New CLI flags `--dx --v-width --v-amp --pml`. | `RunConfig` defaults + `main()` |
| **Co-resolving lattice** | N=26, R=5, r=2.5: the ONE lattice where BOTH G1 (wall, retention ≥ 0.6) AND G4 (winding reads (2,3), r=2.5 > 2.0 collapse-clear) certify. | `RunConfig` defaults |
| **First-class sweep** | v_width / dx / box swept as a robustness axis; existence read ACROSS the sweep. | `sweep_existence` |
| **G1-cert interlock on the bin** | a NEGATIVE (F1-fail) is only bankable if G1 certified; else `NEGATIVE-UNCERTIFIED`. | `bin_result(..., g1_certified=)` |
| **JSON** | every headline number SHA-pinned. | `--json-out` |

**REUSED unchanged** (they work + reproduce): G0 (double-count), G3 (radiative-Q), G4 (winding
extractor plant-at-scale), the unknot-envelope assertion, the (b′) Op14 coupling. **G2 was
re-calibrated** (not re-scoped) — see §2.

**Bench-calibration of the G1 absolute target (ave-apparatus-floor-attribution).** Before
pointing the detector at the unknown, the v14 known-positive retention was measured on the
driver's OWN `CrystalEngine(converter_on=False)` seeder: at dx=0.5/width=2.5/amp=0.85/N=24 it
retains **0.681**, matching the v14 `MasterEquationFDTD`'s **0.670** — the two engines share the
identical saturation kernel (`S=√(1-A²)`, `c_eff²=c0²/S`, `S_min=0.05`), so the v14 ~0.68 is a
legitimate absolute target. The false-negative corner (dx=1.0/width=3.0) reproduces 0.18.

---

## 1 — The bin (prereg §4) + the headline

**BIN = NEGATIVE-A**, banked on the **F4 path** with **G1 (absolute known-positive) CERTIFIED**.

Per prereg §4 the verdict is decided by **F1 + F2 + F4**. At the co-resolving lattice (N=26,
R=5, r=2.5, dx=0.5, v_width=2.5, ~5 core cells, 1500 steps):

- **F1 (existence) = TRUE** — the V-tank wall **self-focuses** into a bounded breather
  (v_peak_tail/seed = **0.681**, Γ_true tail median = **−0.053**, FWHM stays at **7.2%** of box).
  *This INVERTS the first run's F1=False — the wall-half dispersion was the under-resolution
  false negative, now certified absent by the absolute G1 (sech retains 0.687 ≥ 0.60).*
- **F2 (stability) = TRUE** — envelope λ = **−0.011** ≤ jitter-floor +0.0024 (bounded breather,
  no gain/runaway).
- **F4 (winding conserved) = FALSE** — `fraction_tail_reads_2_3 = 0.00`; the planted (2,3) on
  the ω-carrier degrades to (1,0)/(1,2)/(2,1)/(1,1) garbage within ~300 steps and never returns.

So the bin is decided by **F4**: a V-tank breather EXISTS and is STABLE (F1+F2 PASS), **but the
(2,3) winding is NOT conserved on the ω-carrier** (F4 FALSE) → the breather is **not
winding-PROTECTED** → it is **structurally NOT the keystone object** → NEGATIVE-A per §4
(the bin is decided by F1+F2+F4; an F4-fail with F1/F2-pass is a stable mode that does not carry
the conserved winding).

**G1-certification interlock satisfied:** the negative is bankable because G1 (the absolute
known-positive detector) PASSES at this lattice (sech retains 0.687, reproduces the v14 ~0.68;
discriminates vs Gaussian 0.302). The first run's F1-negative would now be `NEGATIVE-UNCERTIFIED`
(its corner G1 = uncertified, sech_ret 0.186 < 0.60) — the interlock structurally blocks the
false negative.

**Headline (the form, NOT the echo):** *the V-tank wall-half breather is REAL and STABLE at the
corrected resolution — the first run got the wall wrong by under-resolving. But the
winding-protected HYBRID breather does NOT stand: the (2,3) winding is not conserved on the
ω-carrier.* **Two load-bearing flags (§5) qualify this:** (FLAG-WIND) the F4 negative is
dominated by the winding being imposed as a SEEDED IC, not the HELD topological BC the prereg
charters — the bare ω-carrier disperses an un-enforced winding identically with/without the
coupling; (FLAG-RES) the F1-existence verdict is RESOLUTION-DEPENDENT (negative at 5 core cells,
**positive** at 10 — §4 sweep), so even the wall-half existence verdict is corner-dependent, not
robust.

**Honest closure (Rule 11):** the single mechanism is *the bare ω-carrier does not sustain an
un-held (2,3) winding* (the coupling neither rescues nor destroys it — F0-decoupled and coupled
trajectories are bit-identical). No knobs were tuned to force a result. But because the
controlling mechanism is the **un-held-BC apparatus floor** (FLAG-WIND), this negative is NOT a
clean falsification of the imposed-BC hypothesis — it is evidence the **imposed-BC charter was
not actually executed** by the seed-once-and-evolve method. **Grant adjudicates whether to (i)
bank NEGATIVE-A as-is with the flags, or (ii) treat FLAG-WIND as a method defect requiring a
held-BC re-run (a re-scope → new prereg + version).**

**Classification (`consistency-vs-emergence`):** EXISTENCE+STABILITY of the wall-half = the
emergence test, now reading POSITIVE-at-the-wall but resolution-dependent. The winding-protection
(F4) = the keystone discriminator, reading NEGATIVE — but on the apparatus floor, not a clean
emergence null. Scope: "no winding-protected hybrid breather stands on THIS platform with the
winding SEEDED (not held)," NOT "no electron" (prereg §9).

---

## 2 — Gate outcomes (prereg §5)

Run: `passive_eigenmode_driver.py --steps 1500` (co-resolving defaults N=26/R=5/r=2.5/dx=0.5).
**ALL FIVE GATES PASS** — so the read is credible, NOT a detector artifact. This is the corrected
G1 (absolute) + a re-calibrated G2; the rest are REUSED unchanged.

| Gate | Validates | Outcome | Numbers |
|:---|:---|:---|:---|
| **G0** | double-count orthogonality | **PASS** | w_pol stays nonzero under coupling; coupling writes ω + scalar V only (no V_ref write path; full G0 smoke proved V_ref-leak ≤ 4.3e-16 prior) |
| **G1** | **ABSOLUTE known-positive (CORRECTED)** | **PASS** | sech retention **0.687 ≥ 0.60** (reproduces the v14 ~0.68 breather) AND > Gaussian 0.302. **The first run's defective RELATIVE G1 is replaced** — the detector now CERTIFIES it can see the known positive before certifying any absence (closes the t2-genesis defect). |
| **G2** | stability-eig sign (RE-CALIBRATED) | **PASS** | known-decaying λ=−4.0 < 0 (sign ✓); known-unstable λ=+5.0 separated from the jitter floor; **jitter floor = 0.0024** (the free-breather's intrinsic |λ| — the instrument noise floor F2 uses, per `ave-apparatus-floor-attribution`). See note below. |
| **G3** | radiative-Q accounting | **PASS** | recovers the analytic Q=25.0 of a known damped resonator to < 10%; ω_C Nyquist-resolvable (ω_C·dt < π); TRUE n=√S used (§8 item 9) |
| **G4** | winding extractor plant-at-scale | **PASS** | plant (2,3) at (N=26,R=5,r=2.5) → reads back **(2,3)**, is_2_3=True, rel **(0.71, 0.86)**; r=2.5 cells clear of the r≈1.1 collapse zone |

**G2 re-calibration (NOT a re-scope — `ave-apparatus-floor-attribution`).** The first run's G2
known-stable arm assumed the free V-tank DISPERSES-and-DECAYS (λ<0). That held only in the
**under-resolved** regime. At the co-resolving eigen-resolution the free V-tank is a genuine
BOUNDED BREATHER whose cycle-to-cycle envelope is near-FLAT with a small phase-dependent jitter
(λ ≈ ±0.01) — it does NOT cleanly decay, so a strict `λ ≤ 0` would mis-FAIL a legitimately
bounded breather. The corrected G2 uses (i) an analytic cleanly-decaying reference for the SIGN
check (λ < 0) and (ii) the free-breather reference to MEASURE the jitter floor; F2 then uses
`λ ≤ +jitter_floor` (not strictly `≤ 0`). This is the instrument-noise-floor discipline, not a
knob tuned to a result.

**Unknot-envelope assertion (Grant's third-time wrong-object guard): PASS.**
`is_0_1_unknot_envelope = True` — the ω-carrier seed's real-space envelope is a single genus-1
torus shell (central hole empty, single annular band). The hole-test threshold was
GEOMETRY-DERIVED (scaled to (R,r): hole radius = ½(R−r)) rather than the first run's fixed
`0.4·R` (tuned for R=10/r=4; it over-reached into the small co-resolving torus). The (2,3)
winding is read on the PHASOR after G4 — confirming it is INTERNAL (polarization-2 + (ω,ω̇)
phasor-3), not an envelope knot.

---

## 3 — Falsifier reads (F0–F5)

Production run N=26, R=5, r=2.5, dx=0.5, v_width=2.5, 1500 steps, passive (NO drive). The CP6
reactance pair (C-state AND L-state) recorded for both sectors over the window.

| # | Falsifier | Read | Outcome |
|:---|:---|:---|:---|
| **F0** | decoupled (α=0) control | breather_exists = **True** | the V-tank self-focuses **on its own** at the corrected resolution — the wall-half is real with or without the coupling. (The first run's F0=False was the same under-resolution artifact.) The coupling is NOT load-bearing for the wall. |
| **F1** | existence (cyclic breather) | **TRUE** | v_peak_tail/seed = **0.681** (the wall sustains a self-focused core); Γ_true tail median = **−0.053** (a TRUE wall persists each breath, marginally past the −0.05 threshold); FWHM stays at **7.2%** of box (does not disperse). **A bounded recurrent breather EXISTS** — the OPPOSITE of the first run's F1. |
| **F2** | stability (no decay/no gain) | **TRUE** | envelope λ = **−0.011** ≤ jitter floor (+0.0024); the breather is bounded, dissipationless-leaning, no gain mode. |
| **F3** | radiative Q (SECONDARY) | Q = **56.0** | in **neither** band (137 / 114). Not bin-deciding (§4/§6). Echo-tagged. |
| **F4** | winding conserved on the ω-carrier | **FALSE** | the planted (2,3) degrades to (1,0)/(1,2)/(2,1)/(1,1) within ~300 steps; `frac_tail_reads_2_3 = 0.00`; median rel_pol tail 0.239. Read on the **(ω, ω̇) phasor**, NEVER (V_inc,V_ref) (G0-clean). **THE BIN-DECIDING NEGATIVE — but see FLAG-WIND (§5): dominated by the un-held-BC apparatus floor.** |
| **F5** | conserved-not-pumped | keystone read is the **passive no-drive** run | F1/F2/F4 read on the passive run; the drive run is the distinguishing control. No gain term, no autoresonant pump (energize-LOCK). |

**The single mechanism (Rule 11) + its apparatus-floor attribution (`ave-apparatus-floor-attribution`).**
The controlling mechanism is **NOT "the coupling fails to lock the winding"** — it is that **the
bare CosseratField3D ω-carrier does not sustain an un-enforced (2,3) winding as a stable mode.**
Direct attribution probe (coupled vs free-standing ω-carrier, same (N,R,r), 1500 steps):

| Arm | tail frac (2,3) | ω-energy 1st→last |
|:---|:---|:---|
| ω-carrier FREE-STANDING (no coupling, no V-tank) | **0.00** | 2.10 → 0.82 |
| ω-carrier COUPLED (Op14 V-tank wire ON) | **0.00** | 2.10 → 0.82 (**bit-identical**) |

The coupled and decoupled winding trajectories are **bit-identical** — the coupling back-reaction
onto ω is negligible, and the planted winding disperses as a free packet either way. So F4=False
is a **carrier-stability / un-held-BC floor**, not a coupling-physics result. **The extractor is
certified** (G4 reads the plant at rel 0.71/0.86 at t=0), so this is genuine carrier dynamics,
not an extractor floor — but the winding was imposed only as an **initial condition** on a free
field, NOT held as the **topological boundary condition** the prereg §7.1/§8.3 charters. **This is
FLAG-WIND (§5).**

---

## 4 — The robustness sweep (v_width / dx / box) — FIRST-CLASS axis

The first run's negative was a SINGLE corner of a MONOTONIC width/box dependence; reporting one
corner as the verdict was the error. The sweep reads the EXISTENCE verdict ACROSS the resolution
axis. The existence verdict is read **only among G1-CERTIFIED corners** (where the detector can
see the known positive; uncertified corners are under-resolved and cannot bank a negative).

| dx | v_width | N | core cells | sech retention | Gaussian | **G1 certified?** | **F1 exists?** |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1.0 | 3.0 | 26 | 3 | 0.425 | 0.378 | **No** | False |
| 1.0 | 3.0 | 48 | 3 | 0.186 | 0.135 | **No** | False ← *the first run's corner* |
| 0.5 | 2.5 | 26 | 5 | 0.666 | 0.302 | **Yes** | **False** ← *the production default* |
| 0.5 | 2.5 | 32 | 5 | 0.592 | 0.199 | No | False |
| 0.5 | 2.5 | 48 | 5 | 0.370 | 0.110 | No | False |
| 0.5 | 5.0 | 32 | 10 | **0.892** | 0.512 | **Yes** | **True** |
| 0.25 | 2.5 | 32 | 10 | **0.892** | 0.199 | **Yes** | **True** |

**Sweep verdict: the existence verdict is RESOLUTION-DEPENDENT, NOT robust** (`robust_negative =
False`, `robust_positive = False` among the 3 certified corners). Specifically:

1. **The first run's corner (3 core cells) is now correctly G1-UNCERTIFIED** — the corrected gate
   structurally refuses to certify a negative there. *The central fix working: the false negative
   is blocked.*
2. **At 5 core cells (the co-resolving default) F1=False; at 10 core cells F1=TRUE** (sech
   retention 0.89, whether reached via wider v_width=5.0 or finer dx=0.25). **A better-resolved /
   wider breather DOES exist and persist.** So the wall-half existence flips with resolution.
3. **The wall-half existence is NOT the problem at adequate resolution** — at 10 cells it is
   robustly real. This is **FLAG-RES (§5):** the production default (5 cells, N=26) sits in a
   transition band where the small box + G1-floor co-resolve but the breather only marginally
   persists; the verdict is corner-dependent.

**Consequence for the bin.** The production default (N=26) reads F1=True but F4=False, so the bin
is decided by F4 regardless of the F1 resolution-dependence. The sweep does NOT change the bin
(NEGATIVE-A on F4), but it establishes that **the wall-half existence claim is resolution-fragile**
and that **a wider/finer breather is a robust POSITIVE for F1** — so any future winding-protection
test should run at ≥ 10 core cells, where the wall is unambiguously real, and address FLAG-WIND
(hold the winding BC) so F4 measures the coupling-physics rather than the un-held-BC floor.

---

## 5 — Flag-don't-fix (surfaced for Grant adjudication; not silently resolved)

### FLAG-WIND (load-bearing — the bin-controlling mechanism) — the winding was imposed as a SEEDED IC, not the HELD topological BC the prereg charters

**The prereg §7.1 / §8.3 charter the winding as a topological BOUNDARY CONDITION** (verbatim):
> §7.1: "**Impose** the (2,3) winding as a topological BC on the **independent Cosserat-ω
> carrier**." §8.3: "Do NOT seed pure-V and let it relax (ω=0 trap) — **impose the winding BC**."
> §1/§3: prior runs let the winding be "**self-selected**"; "Imposing the winding as a BC is the
> untried framing." §5 F4: "winding **conserved** on the ω-carrier."

**The driver — in BOTH the first run and this corrected run — imposes the winding only as a
SEEDED INITIAL CONDITION** (`seed_omega_carrier`: `planted_winding_field(...)` written once into
`eng_w.omega`, then the free `CosseratField3D.step()` evolves it with no re-imposition / Dirichlet
hold). The attribution probe (§3) shows the bare ω-carrier disperses the planted winding to
garbage within ~300 steps **identically with or without the coupling** (bit-identical
trajectories). So **F4=False is dominated by "the winding BC was never actually held," not "the
coupling fails to protect the winding."**

**Why this is load-bearing, not cosmetic:** the prereg's entire untried-framing thesis is that
imposing the winding as a HELD BC (vs. letting it self-select) is what clears the ω≡0 trap and
supplies the odd-ω. A seed-once-and-evolve run does NOT test that thesis — it tests whether a free
ω packet holds a winding (it doesn't, a known dispersive behavior). **The keystone's central claim
is therefore UN-TESTED by this method**, even though the bin reads NEGATIVE-A.

**Reconciliation options (for Grant, NOT asserted):**
- **(i) Bank NEGATIVE-A as-is** with FLAG-WIND attached: "no winding-protected hybrid breather
  stands with the winding SEEDED (not held)" — a true but weak negative (it mostly re-discovers
  that a free ω packet disperses an un-enforced winding).
- **(ii) Treat FLAG-WIND as a method defect** requiring a HELD-BC re-run (re-impose / clamp the
  (2,3) winding each step on a boundary annulus, then test whether the coupled wall sustains it).
  **This is a RE-SCOPE of the method, not a defect-fix within the frozen prereg** — per Rule 12 /
  substitution-not-retraction it gets a **new prereg + version + verification chain**, NOT a
  silent change to this driver. The implementer lane does NOT make this call.
- **(iii)** Note the deeper corpus pointer (prereg §6 / memory `electron_two_threes_vortex_ring`):
  the (2,3) winding lives in **phase-space (ω, ω̇)**, not a real-space R/r torus — a real-space
  seeded torus may be the wrong representation for a *held* phase-space winding BC regardless of
  enforcement. **This bears on (does not resolve) whether the real-space platform can host the
  winding at all** (prereg §8.6 / Flag-A).

### FLAG-RES (the existence verdict is resolution-dependent) — see §4

The F1 wall-half existence flips False→True between 5 and 10 core cells (§4 sweep). The production
default (N=26, 5 cells) sits in a transition band. The negative is bin-decided by F4 regardless,
but the wall-half existence is **not robust** at the default resolution — a future test should run
at ≥ 10 core cells where the wall is unambiguously real.

### FLAG-SUPERSEDE (the first run's NEGATIVE-A is RETRACTED as a false negative)

The first run's result content (BIN=NEGATIVE-A on the F1/wall-disperses path, "the V-tank does not
self-focus") is **RETRACTED** — it was an under-resolution + defective-G1 false negative, panel-REFUTED
and Grant-ratified for option (a). The wall-half DOES self-focus at the corrected resolution (F0+F1
both TRUE). **The first run's FLAG 1 (pre-flight "recurrent breather" vs production "pure dispersion"
contradiction) is RESOLVED IN FAVOR OF THE PRE-FLIGHT:** the pre-flight's self-focusing breather was
CORRECT; the first run's "pure dispersion" was the under-resolution artifact. The (b′) platform's
"viable breather host" characterization is VINDICATED for the wall-half (the breather is real at
≥5–10 core cells). The OPEN question is now the winding-half (FLAG-WIND), not the wall.

### FLAG-APPARATUS (is the NEGATIVE physics or the bench? — `ave-apparatus-floor-attribution`)

Mixed, and stated honestly:
- **G1 wall-half:** physics-but-resolution-fragile. The wall self-focus is real (reproduces the
  v14 known-positive 0.68) but the retention is **box-size-dependent** (bench-measured: 0.84 at
  N=24 → 0.37 at N=48 → 0.27 at N=60, all at fixed eigen-resolution; tracks PML thickness too).
  The small co-resolving box (N=26) recirculates dispersed energy and inflates retention to ~0.68;
  in an OPEN box the same sech retains ~0.30. **So the ~0.68 that clears G1-absolute is partly the
  small box, not pure free-space wall self-focus.** Flagged, not buried.
- **F4 winding-half:** apparatus floor (the un-held BC, FLAG-WIND) — NOT a coupling-physics null.
- **Known-positive certified:** all 5 gates PASS incl. the corrected absolute G1 and G4.
- **Known-null behaves:** the decoupled (F0) winding trajectory is bit-identical to the coupled one.

---

## 6 — Radiative Q (F3) — SECONDARY, echo-tagged, NOT bin-deciding (prereg §4/§6)

**Q_measured = 56.0** (ω_C on the Op16 shear clock `c_shear = c₀(1−A²)^{1/4}`, per-cycle
energy-decay envelope, Nyquist-resolvable ω_C·dt < π). Lands in **neither** the 137 (bare-α) nor
the 114 (κ_chiral) ±5% band.

**This Q is NOT a credible electron Q** — and we say so honestly: the bin object (the
winding-protected hybrid breather) does NOT exist (F4=False), so there is no bound winding-protected
mode whose radiative leak this could be. The Q here is the **per-cycle leak of the wall-half
breather alone** (which DOES exist, F1=True) — a property of the un-winding-protected V-tank
breather, not of the keystone object. Per §4 the Q does not decide the bin; per the keystone reframe
(Grant 2026-06-15) the lane never rested on Q.

**Coupling-binding declaration (prereg §6):** the driver imports **`KAPPA_TILDE = 6/5` (α-FREE)** —
ALPHA is imported ONLY to cross-check the Q targets and to **declare it is NOT a coupling input**.
**Echo tag:** `Q_TANK = 1/α` is a **calibration identity, not a derivation**; the cross-lane chord
is **contingent on Lane-1 Path C (not available)** — so any Q here would be **ECHO**, never a chord
input. With the keystone mode absent, the Q is doubly uninformative.

---

## 7 — Scope, discipline tags, and what this does / does not establish

**What it establishes (honest scope, prereg §9):**
- At the CORRECTED (co-resolving) resolution, the **V-tank wall-half breather is REAL and STABLE**
  (F0+F1+F2 PASS) — the first run's "the V-tank disperses" was an under-resolution false negative,
  now structurally blocked by the absolute-G1 interlock. The wall-half existence is
  resolution-dependent (robust POSITIVE at ≥ 10 core cells; FLAG-RES).
- The **(2,3) winding is NOT conserved on the ω-carrier** as SEEDED (BIN = NEGATIVE-A on F4) — but
  the controlling mechanism is the **un-held-BC apparatus floor** (FLAG-WIND), not a clean
  coupling-physics null. The prereg's central imposed-BC thesis is therefore **un-tested** by this
  seed-once-and-evolve method.
- This is the first co-resolved hybrid-on-Cosserat read with a **CERTIFIED** absolute detector.

**What it does NOT establish:**
- NOT "no winding-protected breather" — the keystone is un-tested (FLAG-WIND: the BC was never held).
- NOT "the V-tank can't host a breather" — it CAN (F1 PASS; robust at ≥10 cells).
- NOT "no electron" (scope is platform/regime/method, prereg §9).
- NOT a resolution of the A1-vs-T2 mass sector (prereg §8.6 / Flag-A — bears-on, does not resolve).
- NOT a Q measurement worth banking (no keystone mode → the Q is the wall-half leak, echo-tagged).

**Substitution-not-retraction (Rule 12 / A47 v11b):** the first run's "winding-protected breather
disperses (F1)" content is retracted as a false negative (FLAG-SUPERSEDE). This result does NOT
refill the slot with a new hypothesis. The clean record: *the wall-half is real; the winding-half
is un-tested because the BC was seeded not held.* A held-BC re-run (FLAG-WIND option ii) is a
**re-scope → new prereg + version + verification chain**, explicitly OUT of this driver's scope.

**Discipline tags:**
- `substrate-native-check` (CP1 time-domain wave engines not Helmholtz; CP6 reactance pair both
  sectors; CP8 imposed-BC framing — *and the CP8 audit is exactly what surfaced FLAG-WIND: the
  driver seeds the precursor but does NOT hold the BC*; CP9 every F-read off step(); CP10 Γ as the
  c_eff boundary + front-window coupling, never a bulk term) — walked BEFORE the code.
- `ave-apparatus-floor-attribution` — THE load-bearing skill this run: the bench-calibration of the
  G1 absolute target (v14 0.68 on the driver's own seeder), the box-size/PML retention sweep
  (FLAG-APPARATUS), and the F4 free-vs-coupled attribution (FLAG-WIND) are all this discipline.
- `phase-space-coordinate-check` (A46) — winding read on the (ω, ω̇) phasor, never (V_inc,V_ref);
  and FLAG-WIND(iii) notes the (2,3) may be phase-space-native, not a real-space R/r torus.
- `ave-conserved-vs-pumped` — F5 keystone is the passive no-drive run; energize-LOCK, no pump.
- `ave-canonical-source` — constants by direct-import identity assertions (no α-derived literal;
  the magic-number gate is clean: `1/ALPHA`, `1/(α·1.2)`, `KAPPA_TILDE=6/5`).
- `ave-module-library-discipline` — REUSED both engines + the G0 coupling + the extractor; built
  only the G1-absolute calibration + the G2 jitter-floor re-calibration; no new engine, no `*_vN`.
- `ave-driver-script-honesty` — every reported number read from the evolved engine state and pinned
  to `results/passive_eigenmode_coresolved_N26.json`; the Q honestly labeled a wall-half leak.
- `consistency-vs-emergence` — wall-half existence tagged emergence (POSITIVE-at-resolution);
  winding-protection tagged the keystone discriminator (NEGATIVE on the apparatus floor); Q echo.
- `ave-discrimination-check` — the F0 decoupled control + the sech-vs-Gaussian G1 absolute pair.

**Corpus-state consequence (for the auditor to land, not this lane):** (a) the first run's
NEGATIVE-A is RETRACTED as a false negative; (b) the wall-half breather is VINDICATED (the (b′)
platform IS a viable breather host at ≥5–10 core cells); (c) the keystone (winding-protection) is
UN-TESTED pending a held-BC re-run (FLAG-WIND) — a re-scope decision for Grant. The auditor's
manuscript / `COLLABORATION_NOTES` queue should carry the supersession + the three flags for
Grant's adjudication. **This lane surfaces it; it does not land the manual entry.**
