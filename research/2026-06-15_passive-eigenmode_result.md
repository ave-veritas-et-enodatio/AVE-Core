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

## 5 — placeholder (flag-don't-fix) — filled next commit
## 6 — placeholder (scope + discipline tags) — filled next commit
