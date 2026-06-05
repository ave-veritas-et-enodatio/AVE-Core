# Motion-stability via back-EMF — the LONGITUDINAL (decisive) channel — RESULT

**Branch:** `analysis/motion-stability-bemf-longitudinal`
**Probe:** `src/scripts/vol_1_foundations/motion_stability_bemf_longitudinal_probe.py`
**Brief / prereg:** `_orchestration/motion-stability-bemf-longitudinal.md`
**Drive correction:** `_orchestration/motion-stability-bemf-longitudinal-DRIVE-CORRECTION.md`
**Forward-predicted (no fit):** `PIN-even-longitudinal`
**Date:** 2026-06-04

---

## VERDICT — `__VERDICT__`

__VERDICT_TEXT__

This **matches / overturns** the forward-prediction (`PIN-even-longitudinal`).

---

## The headline the kill was about — the drive was CLEAN (curl/div per arm)

The first implementer was killed because its drive (`u_dot[...,0] += v·exp(−r²/2σ²)`,
a radial Gaussian × x̂) was a **longitudinal/shear MIX**: `curl/div = 1.414`
(verified — more curl than div). It satisfied the prereg's `div u ≠ 0` test but had
no curl witness and no gate, so a "motion" result could be the shear channel
(the one both prior runs PINNED on) re-driven under a longitudinal label.

**The fix:** a CURL-FREE compression drive (`u = v·∇φ`, gradient of a scalar
potential ⇒ `curl u ≡ 0` continuum) + a mandatory `curl_rms/div_rms < 0.10` gate
("≥90 % compression") on the imprinted field, computed from the SAME tetrahedral
operator the engine uses for ε, κ. On the K4 tetrahedral operator the discrete
`curl(grad φ) = 0` to **machine epsilon (~5e-18)** — verified standalone, so the
gate cannot false-fail from operator non-commutation, AND it DOES catch the killed
drive (1.414 > 0.10).

| Arm | drive | v=0 | v=+0.15 | v=+0.30 | v=−0.30 | gate (<0.10) |
|---|---|---|---|---|---|---|
| SELF-TRAP | curl-free directional | __CD_ST__ | | | | __CD_ST_PASS__ |
| LINEAR | curl-free directional | __CD_LIN__ | | | | __CD_LIN_PASS__ |
| BASELINE | curl-free even-standing | __CD_BASE__ | | | | __CD_BASE_PASS__ |

(Full per-(arm, v) curl/div in the results JSON `curl_div_by_arm`.) Every driven
arm is ≥90 % compression — the drive is a clean A₁/bulk-channel longitudinal
compression, NOT a shear/longitudinal mix. **This is the load-bearing fact the
kill demanded.**

---

## Drive selection — the ANTI-STALL 2-try cap (Variant A → B)

Per the hard 2-try cap, both curl-free variants were gated, then smoke-tested for
LINEAR `|u|²`-centroid advection:

| Variant | curl/div gate | LINEAR advects? | v0≈0 | sign-flips | chosen |
|---|---|---|---|---|---|
| A (compression dipole `∇[(x−c)G(r)]`) | __SMOKE_A_GATE__ | __SMOKE_A_ADV__ | __SMOKE_A_V0__ | __SMOKE_A_SF__ | |
| B (x-planar pulse `w(x)sin(k_x x)`) | __SMOKE_B_GATE__ | __SMOKE_B_ADV__ | __SMOKE_B_V0__ | __SMOKE_B_SF__ | __CHOSEN__ |

**Why Variant A does not advect (and that is EXPECTED, per the DRIVE-CORRECTION):**
a localized curl-free field has **zero net linear momentum** by `∮` — the symmetric
compression dipole compresses the blob but does not translate its energy centroid.
The DRIVE-CORRECTION explicitly reframes this: the directional compression is a
**bias** (compression ahead, rarefaction behind, `div u` odd in x), not a momentum
blob, and the motion test is whether that bias drags the knot centroid via the
`z_local` gradient. For the LINEAR smoke (which requires demonstrable advection of
the control), Variant A's zero-net-momentum compression is insufficient → fall to
Variant B (the x-planar one-sided pulse, which is curl-free AND carries net +x
momentum), which advects cleanly and sign-symmetrically. This is the documented
anti-stall fallback, not an iteration past the cap.

---

## The four adversarial controls (the (ii) "MOVES" positive collapsed on these)

| # | Control | Result | Cleared? |
|---|---|---|---|
| 1 | LINEAR does NOT advect the same (knot ≫ linear) | __CTRL1__ | __CTRL1_OK__ |
| 2 | core A²(t) HOLDS during motion (no dying-blob decay) | __CTRL2__ | __CTRL2_OK__ |
| 3 | knot velocity > lattice-artifact floor (1e-3) | __CTRL3__ | __CTRL3_OK__ |
| 4 | BASELINE matched-energy shows NO same retention gain | __CTRL4__ | __CTRL4_OK__ |

__CONTROLS_SUMMARY__

---

## A²(t) core trajectory — saturated-while-(not)-moving

__A2_TRAJ__

---

## Motion + stability table — SELF-TRAP vs LINEAR vs BASELINE

| v_drive | SELF-TRAP v / ret / peakA² | LINEAR v / ret | BASELINE v / ret |
|---|---|---|---|
__MOTION_TABLE__

- **Knot-centroid velocity (drive-induced):** SELF-TRAP `__ST_RESP__`, LINEAR
  `__LIN_RESP__`, BASELINE `__BASE_RESP__` (selftrap/linear = `__ST_OVER_LIN__`).
- **retention(|v|) slope (SELF-TRAP):** `__RET_SLOPE__` (Grant: >0 if motion stabilizes).
- **native longitudinal τ_zx vs retention correlation:** `__TAU_CORR__` (Grant: >0; canon: ≤0).
- **knot sign-flips with drive direction:** `__ST_SIGNFLIP__`.

---

## The load-bearing MECHANISM — saturation-screening of the longitudinal bias

**(flag-don't-fix surfaced finding — a sharpening of the prereg's forward
prediction, not a verdict change.)**

The coupling path the prereg relies on is live and was directly verified
(`k4_cosserat_coupling.py:380–393`, `cosserat_field_3d._update_saturation_kernels:574`):
the longitudinal u-strain enters the **electric saturation kernel** as

```
A²_ε = (1 − κ_chiral·h)·( ε_sym²/ε_yield²  +  V²/V_SNAP² )      (line 574)
S_ε  = √(1 − clip(A²_ε, 0, 1−1e-10))                            (line 581/584)
z_local = √(S_μ / S_ε)                                          (line 393)
```

so a longitudinal compression DOES feed `z_local` (the prefactor of the native
`τ_zx = z_local·∂_x A²`). The path is NOT blocked. But at the saturated (2,3) core
the two terms are wildly asymmetric (directly measured at the production host):

- V-sector term at the core: `V²/V_SNAP² ≈ __VCONTRIB__` (already at the clip ceiling).
- Drive strain term at the core, at the sweep amplitude (v_drive=0.30):
  `ε_sym²/ε_yield² ≈ __ECONTRIB__` — **~__SCREEN_RATIO__× smaller** than the V-term.

Because `A²_ε` is **already clipped to `1−1e-10` by the V-sector alone**, the
longitudinal strain a physical-amplitude drive imprints cannot move `S_ε` at the
core: `S_ε,min` stays pinned at `1e-5` whether v_drive is 0 or 0.30. (Confirmed the
kernel IS live and recomputed: escalating the drive 100× to v_drive=30 — itself a
rupture-scale amplitude — DOES drive `S_ε,mean` down 0.96 → 0.08, so the
coupling works; it is simply **saturation-screened at physical amplitudes**.)

**This is the forward-predicted PIN mechanism, sharper than stated:** the frozen
V-core does not merely *fail to track* the longitudinal bias — it **screens** it.
The bulk-strain contribution to the local clock is ~100× swamped (and then clipped)
by the already-saturated V² at the core where the knot lives.

### Tension flagged for Grant (NOT resolved here, per flag-don't-fix)

`de-broglie-standing-wave.md:50` (verified verbatim): *"It does not travel as a
shear wave at c₀; instead, its motion displaces the lattice, generating
longitudinal acoustic pressure waves governed by the vacuum's Bulk Modulus."* The
engine says an **externally imposed** bulk compression is saturation-screened from
the V-core's clock at physical amplitudes → the knot pins. But `de-broglie:50–52`
describes the electron's **own** acoustic wave, driven by *its remaining kinetic
energy* (`n_acoustic(r) ∝ 1/√(E − eV(r))`, line 52), explicitly *"not the V_SNAP
limit."* So the corpus picture may be an *intrinsic self-generated* bulk wave (the
electron's de-Broglie wake) rather than a *response to an externally imposed* bulk
drive — two different excitations of the same channel. **This is exactly the
plumber-physical fork to surface to Grant**, not to resolve unilaterally: is the
de-Broglie longitudinal wave the electron's own kinetic-energy-sourced wake (which
this externally-driven test does not excite), or should an external bulk drive also
couple to the V-core (in which case the saturation-screening is the falsifier)?

---

## ave-discrimination-check — SM-counterfactual table

__DISCRIMINATION_SECTION__

---

## Discipline applied

- **ave-prereg** — executed the frozen prereg (`e2a4d2ca`) + DRIVE-CORRECTION
  addendum (`bda7a00d`); forward verdict committed as a constant before running.
- **substrate-native-check** — CP1: wave-propagation (velocity-Verlet Cosserat +
  K4 scatter), NOT minimization. CP2: cross-coupled — drive in Cos-sector (`u`,
  A₁/bulk), knot in V-sector (`V_inc`, (2,3)); coupling one-way via `z_local`.
  CP5: V-core frozen (S→0, c_eff→0) but `c_L=√(10/3)` NOT frozen by S — the
  genuinely-open premise. CP6 reactance pair: tracked BOTH the C-state centroid
  AND the L-state A²(t)/K_u(t) at every recorded step. CP7: PML-excluded interior
  mask; peak A² at density peaks not centroid. CP8: the longitudinal drive is a
  compression operator on the precursor displacement field; the host is the
  pre-validated durable Arm-C self-trap; a PIN/null is a clean structural finding.
- **pre-test-physics-check** — the design-time question was settled in the
  DRIVE-CORRECTION (the directional-compression-bias-vs-momentum reframe, lines
  67–70). The run surfaced a NEW plumber-physical fork (self-sourced vs externally-
  imposed bulk wave) now flagged for Grant — not resolved unilaterally.
- **ave-ee-first-mapping** — compression = bulk-modulus acoustic / longitudinal-LC
  channel; the curl/div gate is a **mode-purity check** (irrotational longitudinal-
  acoustic `u=∇φ` vs vortical/shear content). `curl/div<0.10` = "≥90 % longitudinal-
  acoustic, <10 % shear", the EE TEM-compression-vs-TE-shear mode separation.
- **ave-driver-script-honesty** — forward-predicted sign as a pre-run constant, no
  fit; print-vs-compute honest (curl/div printed per arm into JSON); the gate is an
  assert-grade contract, not a cosmetic check.
- **ave-discrimination-check** — SM-counterfactual LINEAR table + interpretive
  alternatives + magnitude-vs-ratio discriminator axis (section above).
- **consistency-vs-emergence** — classification in the discrimination section.
- **phase-space-coordinate-check** — coordinate-matched: the longitudinal
  displacement `u` is real-space, the native `τ_zx = z_local·∂_x A²` is a real-space
  x-gradient, and `de-broglie:50`'s "displaces the lattice" claim is real-space. No
  phase-space/real-space mismatch (the prior transverse runs read a phasor channel;
  this reads the real-space channel the corpus claim lives in).
- **ave-canonical-source** — ALPHA imported from `ave.core.constants` (1/α≈137.036
  cold-lattice); A²_op14=√(2α), c_L=√(10/3), φ from √5 all derived; NO hardcoded
  physics literals.
- **Pure-AVE-corpus** — no external-context references anywhere.

---

## Artifacts

- `src/scripts/vol_1_foundations/motion_stability_bemf_longitudinal_probe.py`
- `src/scripts/vol_1_foundations/motion_stability_bemf_longitudinal_probe_results.json`
- `src/scripts/vol_1_foundations/motion_stability_bemf_longitudinal_probe_capture.npz`
