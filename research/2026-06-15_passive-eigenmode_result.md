# Passive winding-protected electron eigenmode — the hybrid (V,ω) breather — RESULT

> **STATUS: COMPLETE. BIN = NEGATIVE-A** (prereg §4). The coupled (V,ω) hybrid solve
> **disperses** — no bounded recurrent winding-protected breather exists on the (b′)
> `crystal_engine` V-tank ⊗ Cosserat-ω platform at the tested lattices/regime.
>
> **Headline (the form, NOT the echo):** *the passive winding-protected hybrid breather
> does NOT exist on this platform.* The V-tank renders a deep TIR wall only at the
> **seeded** amplitude and then disperses from it; it does not self-focus into a sustained
> breather, and the imposed (2,3) winding coupling does not rescue it.
>
> Prereg (FROZEN): `research/2026-06-15_passive-eigenmode_prereg_FROZEN.md`.
> Driver: `src/scripts/vol_1_foundations/passive_eigenmode_driver.py`.
> Build-step-zero G0 (PASSED, prior): `src/scripts/vol_1_foundations/g0_double_count_smoke.py`.
> Branch: `analysis/2026-06-15-eigenmode-driver` (NOT merged — Grant merges).

---

## 1 — The bin (prereg §4) + the headline

**BIN = NEGATIVE-A** — "coupled solve does not converge / disperses → no standing mode →
structure fails."

The verdict is decided by **F1 + F2 + F4** (the keystone primary; Q is secondary, §4).
The deciding falsifier is **F1 (existence) = FALSE**: the coupled hybrid solve disperses —
the V-tank breather does not sustain a self-focused core, the TRUE Γ=−1 wall vanishes over
the recording window, and the FWHM grows toward the box. **F4 (winding conserved) also
FALSE** corroborates (the (2,3) does not survive once the wall disperses).

This is a **clean negative with a single explanatory mechanism** (Rule 11 / honest closure):
*the passive `crystal_engine` V-tank does not self-focus into a sustained breather — it
disperses from whatever depth it is seeded at — and the winding-BC coupling does not change
that.* No knobs were tuned to force a result.

**Reproduced at two independent lattices** (N=48/R=10/r=4 and N=40/R=8.5/r=3.5), both
NEGATIVE-A, all gates PASS at both — the bin is robust to lattice choice (§6).

**Classification (`consistency-vs-emergence`):** EXISTENCE + STABILITY was the **emergence
test** (the keystone). It returned a negative: the eigencavity structure is NOT a renderable
passive breather on this platform/regime. (Scope: this is "no stable passive hybrid breather
on THIS platform/regime," NOT "no electron" — prereg §9.)

---

## 2 — Gate outcomes (prereg §5 — ALL must pass before any production read is credible)

Run: `passive_eigenmode_driver.py --N 48 --R 10 --r 4 --steps 1500`.
**ALL FIVE GATES PASS** — so the NEGATIVE-A is a credible physics read, not a detector
artifact (this closes the t2-genesis "detector-can't-certify-the-known-positive" defect).

| Gate | Validates | Outcome | Numbers |
|:---|:---|:---|:---|
| **G0** | double-count orthogonality | **PASS** | w_pol stays nonzero (3,3,3,3) under coupling; no V_ref write path (coupling writes ω + scalar V only; full G0 smoke proved V_ref-leak ≤ 4.3e-16 prior) |
| **G1** | sech-converges / Gaussian-disperses detector | **PASS (marginal)** | sech retention 0.102 > Gaussian 0.090 (>1.1×). Detector *discriminates*, but **both ~10%** — the V-tank disperses substantially even for the sech (load-bearing: the F1 negative is foreshadowed in the gate) |
| **G2** | stability-eig (NEW BUILD; cycle-envelope decay rate) | **PASS** | known-stable λ=−0.099 ≤ 0 AND known-unstable λ=+5.0 > 0 — reads the sign correctly |
| **G3** | radiative-Q (NEW BUILD) | **PASS** | recovers Q_analytic=25.0 of a known damped resonator to **0.06%**; ω_C Nyquist-resolvable (ω_C·dt=0.017 ≪ π); TRUE n=√S used (§8 item 9) |
| **G4** | winding extractor plant-at-scale | **PASS** | plant (2,3) at (N=48,R=10,r=4) → reads back (2,3), is_2_3=True, rel (0.73, 0.94); r=4 cells clear of the r≈1.1 collapse zone |

**Unknot-envelope assertion (Grant's third-time wrong-object guard): PASS.**
`is_0_1_unknot_envelope = True` — the ω-carrier seed's real-space envelope is a single
genus-1 torus shell (central hole empty, single annular ring, 1 radial band = one closed
tube threading the hole once). So the (2,3) winding read is backed by "on the unknot =
electron": the winding is **internal** (polarization-2 + (ω,ω̇)-phasor-3), NOT a heavier
real-space envelope knot. The cos(qψ) winding nodes fragment the raw |ω| support — that
fragmentation IS the (2,3) phase structure, read on the phasor (after G4), not the envelope.

---

## 3 — Falsifier reads (F0–F5)

Production run N=48, R=10, r=4, 1500 steps, passive (NO drive). The CP6 reactance pair
(C-state AND L-state) was recorded for both sectors over the window.

| # | Falsifier | Read | Outcome |
|:---|:---|:---|:---|
| **F0** | decoupled (α=0) control | breather_exists = **False** | the V-tank disperses **on its own** — the coupling is not suppressing a mode that would otherwise exist. **The dispersion is intrinsic to the V-tank, not caused by the (b′) coupling.** |
| **F1** | existence (cyclic breather) | **FALSE** | V_peak tail/seed = **0.181** (core fades to ~18% of seed); Γ_true tail median = **−0.003** (the TRUE Γ=−1 wall **vanishes**); FWHM grows 64× to 14% of box. **No bounded recurrent breather** — the bin-deciding negative. |
| **F2** | stability (no decay/no gain) | not informative (F1 already fails) | envelope λ = +0.0085 — but the tail V_peak is a **noisy floor** (0.078–0.25, mean 0.147, no exponential trend), NOT a gain mode. The small +λ is late low-amplitude floor noise. F2 is moot when there is no mode to stabilize. |
| **F3** | radiative Q (SECONDARY) | Q = 363.8 | in **neither** band (137 / 114). Not bin-deciding (§4). See §4 below + the echo tag. |
| **F4** | winding conserved on the ω-carrier | **FALSE** | w_pol over the run: 3,3,3 (the planted (2,3)) for the first ~3 samples, then degrades to mostly **1 and 0**; frac_tail_reads_2_3 = **0.00**. Read on the **(ω, ω̇) phasor**, NEVER (V_inc,V_ref) (G0-clean, preserved). The winding does not survive once the V-tank energy disperses. |
| **F5** | conserved-not-pumped | keystone read is the **passive no-drive** run | F1/F2/F4 were read on the passive run; the drive run is the distinguishing control. No gain term, no autoresonant pump (energize-LOCK coupling). |

**The single mechanism (Rule 11 — one mechanism explains all failures):** the passive
`crystal_engine` V-tank does not self-focus into a sustained breather. It renders a deep TIR
wall **only at the seeded amplitude** and disperses from it; F1 (no breather) ⇒ F4 (the
winding has no wall to lock to) ⇒ F3 (no stored mode to leak from a fixed cavity). F0 shows
the coupling is not the culprit. **One mechanism, all reads consistent.**

---

## 4 — Radiative Q (F3) — SECONDARY, echo-tagged, NOT bin-deciding (prereg §6)

**Q_measured = 363.8** (ω_C on the Op16 shear clock c_shear = c₀(1−A²)^{1/4}, per-cycle
energy-decay envelope). This lands in **neither** the 137 (bare-α) nor the 114 (κ_chiral)
±5% band.

**This Q is NOT a credible electron Q** — and we say so honestly: it is the leak of a
**dispersing remnant**, not a bound-mode radiative leak, because **no bound mode exists**
(F1 = False). A Q-from-decay on a field that is dispersing measures the dispersal/PML rate,
not a cavity's radiative coupling. **Per §4 the Q does not decide the bin, and per the
keystone reframe (Grant 2026-06-15) the lane never rested on Q.** Reporting it for
completeness; it carries no weight.

**Coupling-binding declaration (prereg §6):** the driver imports **`KAPPA_TILDE = 6/5`
(α-FREE)** — ALPHA is imported ONLY to cross-check the Q targets and to **declare it is NOT
a coupling input**. **Echo tag:** `Q_TANK = 1/α` is a **calibration identity, not a
derivation**; the cross-lane chord is **contingent on Lane-1 Path C (not available)** — so
any Q here would be **ECHO**, never a chord input. With the mode itself absent, the Q is
doubly uninformative.

## 5 — Flag-don't-fix (surfaced for Grant adjudication; not silently resolved)

### FLAG 1 (load-bearing) — the production driver CONTRADICTS the V-tank pre-flight's "recurrent breather" claim

**The orchestration doc's pre-flight (the basis for the (b′) sign-off) claims a sustained
breather. The production driver finds pure dispersion. These conflict — surfaced, not reframed.**

- **Pre-flight claim** (`_orchestration/2026-06-15_passive-eigenmode-solve.md:84-86`, verbatim):
  > "`crystal_engine`'s V-tank self-focuses to a **GENUINE deep TIR wall** (Γ_TRUE≈−0.43 on
  > **fully-UNCLIPPED** cells; … with **ZERO clips ever**), **bounded, NO runaway** … **recurrent**
  > (re-focuses at steps 375–450)."
  and (`:411-417`): "a **genuine, bounded, recurrent BREATHING TIR wall**."

- **Production driver finding** (`passive_eigenmode_driver.py`, this run): across the entire
  seed-amplitude/width space (amp 0.85→0.99, width 1.2→3.0), the TRUE Γ minimum is **always at
  step 0** and **never deepens** (`deepens=False` in every case). At amp=0.99/w=1.8 the seed
  *starts* at Γ_true=−0.454 (the analytic floor) — i.e. the "−0.43 unclipped" figure is the
  **seeded** wall depth — and it relaxes monotonically to Γ_true≈−0.002. There is **no
  self-focusing and no recurrent re-focus**; the V-tank disperses from whatever depth it is seeded at.

- **Reconciliation hypothesis (for Grant, NOT asserted):** the pre-flight's "Γ_TRUE≈−0.43" is
  the **seed-time** wall depth (correct — the seed *is* that deep), and its "recurrent re-focus
  at steps 375–450" appears to be **transient ringing of the dispersing field** (the noisy floor
  this driver also sees: V_peak oscillates 0.08–0.25 in the tail), **mis-read as self-focusing**.
  If so, the (b′) "wall-half is real" premise holds only in the trivial sense that *a seeded deep
  wall is deep at t=0* — it does NOT establish a **self-sustaining** breather, which is what the
  keystone requires. **This does not change the bin** (NEGATIVE-A stands on F1 either way), but it
  bears on whether the (b′) platform was correctly characterized as a viable breather host.
  **Grant adjudicates;** the driver does not silently "fix" the pre-flight doc.

### FLAG 2 (apparatus-floor attribution — `ave-apparatus-floor-attribution`)

Is the NEGATIVE-A *physics* or *the bench*? The evidence says **physics floor (`WALL-physics`),
not a solver artifact:**
- **Known-positive certified:** all five gates PASS, including G1 (the sech-converges detector)
  and G4 (the extractor reads the planted (2,3) at rel 0.73/0.94). The detectors can see a mode
  if one is there.
- **Known-null behaves:** the decoupled (α=0) control (F0) disperses identically — the coupling
  is not masking a mode.
- **Free-drift / regularization sweep:** reproduced at two independent lattices (N=48/R=10/r=4 and
  N=40/R=8.5/r=3.5), both NEGATIVE-A; the dispersion is intrinsic across the seed-parameter sweep
  (no amp/width self-focuses). The Q read flips sign between lattices (363.8 vs −67.1) — the
  signature of a **non-bound, dispersing** field, not a stable cavity.
- **Honest residual:** the V-tank here is run with the engine's PML + its intrinsic c_eff trap and
  **no added confinement**. The prereg's whole hypothesis was that the **winding-BC coupling**
  would supply the missing confinement — it did not (F0 ≈ coupled, the coupling is ≲ load-bearing
  for the wall, echoing pre-flight #1's "chiral term <10%" finding). So the floor is "this passive
  platform/regime, with this coupling strength, does not bind a breather" — a genuine
  `WALL-physics` result, scoped to the platform (prereg §9), not "no electron."

### FLAG 3 (bears-on, does NOT resolve — prereg §8 item 6 / Flag-A)

The lane **bears on but does NOT resolve** the A1-vs-T2 mass-sector question (m_e c² hypothesis-
class). A NEGATIVE here is "no passive hybrid breather on the A1/V-tank ⊗ Cosserat-ω platform" —
it is **evidence the A1/V-tank scalar alone does not host the bound electron as a passive
fixed-point breather**, consistent with (but not proving) the open question of whether the mass
sector needs the T2 channel. **No resolution claimed.**

---

## 6 — Scope, discipline tags, and what this does / does not establish

**What it establishes (honest scope, prereg §9):**
- On the (b′) `crystal_engine` V-tank wall ⊗ Cosserat-ω carrier platform, with the G0
  double-count-clean Op14 coupling (KAPPA_TILDE=6/5, α-free), at the tested lattices/regime,
  **no stable passive winding-protected hybrid breather exists** (BIN = NEGATIVE-A). The
  V-tank disperses; the winding does not survive; the coupling does not rescue it.
- This is the **first hybrid-on-Cosserat** test of the imposed-BC (V,ω) mode (the prereg's
  "one untried residue"). The untried framing was tried; it returned a clean negative.

**What it does NOT establish:**
- NOT "no electron" (scope is platform/regime, prereg §9).
- NOT a resolution of the A1-vs-T2 mass sector (Flag 3 / prereg §8.6).
- NOT a Q measurement worth banking (no bound mode → the Q is a dispersing-remnant artifact;
  the headline never rested on Q — Grant 2026-06-15).

**Substitution-not-retraction (Rule 12):** this result does not refill the "winding-protected
breather exists" slot with a new hypothesis. The clean negative is recorded; any re-test on a
different engine/regime (e.g. a T2-native carrier per the open engine-pivot, or a driven/
autoresonant arm — explicitly OUT of this passive prereg's scope) gets its **own prereg + version
+ verification chain.**

**Robustness:** NEGATIVE-A reproduced at two independent lattices (N=48 and N=40), all gates
PASS at both. The bin is robust to lattice choice.

**Discipline tags:**
- `substrate-native-check` (CP1 time-domain wave engine not Helmholtz; CP6 reactance pair
  recorded both sectors; CP8 imposed-BC framing; CP9 every F-read off the engines' own step();
  CP10 Γ as the c_eff boundary + front-window coupling, never a bulk term) — walked BEFORE the code.
- `phase-space-coordinate-check` (A46) — winding read on the (ω, ω̇) phasor, never real-space
  Cartesian, never the (V_inc,V_ref) A1 phasor.
- `ave-conserved-vs-pumped` — F5 keystone is the passive no-drive run; energize-LOCK coupling,
  no gain/pump.
- `ave-representation-capability-check` — traveling-(2,3) seeder (NOT the z-flat rotor that fails
  G4); unknot-envelope asserted (the (2,3) is internal polarization+phasor, not an envelope knot).
- `ave-canonical-source` — constants by direct-import cross-check (NO verify_constants fn in this
  corpus; identities asserted: 1/ALPHA=137.036, 1/(α·1.2)=114.20, KAPPA_TILDE=6/5).
- `ave-module-library-discipline` — REUSED both engines + the G0 coupling + the extractor; no new
  engine, no `*_vN` file. Built only the G2 (stability) + G3 (radiative-Q) layers, each
  known-positive/known-negative validated.
- `ave-driver-script-honesty` — every reported number is read from the evolved engine state
  (print-what-you-compute); the Q is honestly labeled a dispersing-remnant artifact, not a Q.
- `consistency-vs-emergence` — existence/stability tagged emergence (the keystone, negative);
  the Q value tagged a separate (echo) characterization.
- `ave-discrimination-check` — the F0 decoupled control + the sech-vs-Gaussian G1 pair confirm
  the negative is structural, not an SM-default artifact.
- `ave-apparatus-floor-attribution` — Flag 2: physics floor (`WALL-physics`), not the bench.

**Corpus-state consequence (for the auditor to land, not this lane):** the (b′) platform's
"viable breather host" characterization (orchestration doc §1d/§0.5) is in tension with this
production result (Flag 1) — the auditor's manuscript / `COLLABORATION_NOTES` queue should carry
the NEGATIVE-A bin + the pre-flight-vs-production breather contradiction for Grant's adjudication.
This lane surfaces it; it does not land the manual entry.
