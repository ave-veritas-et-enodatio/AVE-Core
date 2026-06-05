# Motion-stability via back-EMF — the LONGITUDINAL (decisive) channel — RESULT

**Branch:** `analysis/motion-stability-bemf-longitudinal`
**Probe:** `src/scripts/vol_1_foundations/motion_stability_bemf_longitudinal_probe.py`
**Brief / prereg:** `_orchestration/motion-stability-bemf-longitudinal.md`
**Drive correction:** `_orchestration/motion-stability-bemf-longitudinal-DRIVE-CORRECTION.md`
**Forward-predicted (no fit):** `PIN-even-longitudinal`
**Date:** 2026-06-04

---

## VERDICT — `PIN-even-longitudinal`

**LINEAR advects but the SELF-TRAP knot does NOT** (drive-response ≪ linear, **no
sign-flip with drive direction**). The saturated (2,3) V-core (peak A²≈3.07 ⇒
S→0 ⇒ c_eff→0) does not track the `z_local` saturation-impedance bias enough to
translate — *even though* the bulk/longitudinal channel is NOT frozen by S and the
LINEAR sub-saturation compression advects cleanly at ~c_L. The knot is a
frozen-clock soliton, **PINNED even on the longitudinal channel the electron
physically moves in**. Grant's stability-FROM-motion hypothesis is **CONTRADICTED
on the decisive longitudinal channel** (the prior two transverse runs also PINNED;
this closes the genuinely-open third channel).

This **matches** the forward-prediction (`PIN-even-longitudinal`, committed as a
pre-run constant — no fit). The substrate default held: `observed == forward`.

This is a clean, publishable negative result with a single named mechanism
(saturation-screening, below) — the discipline working at full strength (Rule 11
honest closure). No rescue debugging; branch closes on a falsification with the
mechanism named.

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
| SELF-TRAP | curl-free x-planar (Variant B) | 0.0 | 0.0 | 0.0 | 0.0 | **PASS** |
| LINEAR | curl-free x-planar (Variant B) | 0.0 | 1.7e-16 | 1.1e-16 | 1.1e-16 | **PASS** |
| BASELINE | curl-free even-standing | 0.0 | 0.0 | 0.0 | 0.0 | **PASS** |

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
| A (compression dipole `∇[(x−c)G(r)]`) | 0.0000 PASS | **No** (v≈±5e-5) | yes | yes | |
| B (x-planar pulse `w(x)sin(k_x x)`) | 0.0000 PASS | **Yes** (v≈∓0.029, dx≈∓0.78) | yes | yes | **✓ B / displacement** |

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

| # | Control | Result | Cleared (for SUPPORTS)? |
|---|---|---|---|
| 1 | LINEAR-distinct (knot moves ≫ linear) | knot drive-response = **0**, linear = 0.0085 → knot does NOT move more | **No** |
| 2 | core A²(t) HOLDS during motion | A²_end/A²_start = **1.001** (held perfectly; peak A²≈3.07 throughout) | Yes |
| 3 | knot velocity > lattice floor (1e-3) | |v_knot| = 0.00263 > 1e-3 | Yes |
| 4 | BASELINE-distinct (no matched-energy gain) | selftrap retention-gain = **0.0**, baseline = **0.0** → identical, no differential | **No** |

**Interpretation (CRITICAL — these controls gate a SUPPORTS, and a SUPPORTS is NOT
the verdict):** controls 1 and 4 fail *because the knot does not move at all* —
there is no translation to be "more than linear" (control 1) and no retention gain
to attribute to directionality (control 4). For a PIN that is the CORRECT outcome:
the four controls are the gate that *would* admit a SUPPORTS, and they correctly
refuse to. Control 2 (A²-holds) and control 3 (above-floor) confirm the soliton is
a genuine stable trap throughout (NOT a dying blob, NOT sub-lattice jitter) — so
the PIN is the real "a stable soliton that refuses to translate," not "a blob that
fell apart." All four together: **clean PIN, no SUPPORTS, no CONTRADICTS-via-generic-
transport ambiguity.**

---

## A²(t) core trajectory — saturated-while-(not)-moving

The SELF-TRAP core peak A² (V-sector, at the density peak — NOT centroid) over the
recording window, `[start, min, end]`, is **identical across every v_drive**:

| v_drive | peak A² [start, min, end] |
|---|---|
| 0.00 | [3.0745, 3.0706, 3.0768] |
| +0.15 | [3.0745, 3.0706, 3.0768] |
| +0.30 | [3.0745, 3.0706, 3.0768] |
| −0.30 | [3.0745, 3.0706, 3.0768] |

The core stays at A²≈3.07 (well above 1 — S→0, c_eff→0, frozen clock) the whole
window, A²_end/A²_start = 1.001. This is **NOT** the transverse-run's (ii) failure
mode (A 0.85→0.4, a dying blob being pushed): it is a **fully stable, saturated
soliton that simply does not translate** under the longitudinal drive. The
byte-identical trajectories across v_drive ARE the PIN: the V-core evolution is
completely independent of the longitudinal drive.

---

## Motion + stability table — SELF-TRAP vs LINEAR vs BASELINE

| v_drive | SELF-TRAP v / ret / peakA² | LINEAR v / ret | BASELINE v / ret |
|---|---|---|---|
| 0.00 | +0.00263 / 0.518 / 3.07 | −0.00002 / 0.845 | +0.00263 / 0.518 |
| +0.15 | +0.00263 / 0.518 / 3.07 | +0.00555 / 0.748 | +0.00263 / 0.518 |
| +0.30 | +0.00263 / 0.518 / 3.07 | +0.00843 / 0.562 | +0.00263 / 0.518 |
| −0.30 | +0.00263 / 0.518 / 3.07 | −0.00848 / 0.562 | +0.00263 / 0.518 |

- **Knot-centroid velocity (drive-induced, v=0 corrected):** SELF-TRAP `0.000`,
  LINEAR `0.0085`, BASELINE `0.000` (selftrap/linear = `0.000`).
- **SELF-TRAP velocity is byte-identical (+0.00263) at every v_drive** — that
  +0.00263 is the knot's own intrinsic settling drift, completely **drive-
  independent**. LINEAR velocity scales with drive and **sign-flips cleanly**
  (+0.00843 at +0.30 → −0.00848 at −0.30): the control advects, the knot does not.
- **retention(|v|) slope (SELF-TRAP):** `nan` — degenerate (all retentions
  identical = 0.518, zero variance). NOT >0; the saturated knot's retention is
  drive-invariant, so there is NO motion-stabilization signal.
- **native longitudinal τ_zx vs retention correlation:** `nan` — degenerate (τ_zx
  byte-identical = 6.60e5 across the sweep; retention zero-variance). NOT >0.
- **knot sign-flips with drive direction:** `False` (the robust pin tell —
  v(+0.30) == v(−0.30) == +0.00263, so the residual drift is NOT a drive response).

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

- V-sector term at the core: `V²/V_SNAP² ≈ 3.07` (already above 1 → A²_ε pins at
  the clip ceiling `1−1e-10`, S_ε,min = 1e-5).
- Drive strain term at the core, at the sweep amplitude (v_drive=0.30):
  `ε_sym²/ε_yield² ≈ 1.90e-2` — **~162× smaller** than the V-term (measured at the
  production N=48 host).

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

**Nothing reads as a positive → no promotion to gate.** `ave-discrimination-check`
fires *before framing a positive as "AVE-distinct / STRONG POSITIVE / load-bearing
confirmation"*; the verdict here is a falsification (PIN), so there is no positive
claim to promote and the skill's promotion path does not apply. For completeness,
the SM-counterfactual is run on the two observables that DID move (so the negative
is honestly bounded), and the result is classified per `consistency-vs-emergence`:

| Observable | What moved | SM predicts same? | Class | Load-bearing? |
|---|---|---|---|---|
| LINEAR sub-saturation blob advects under a curl-free +x compression pulse | v ∝ drive, sign-symmetric | **YES** — a linear elastic medium advects a one-sided compression pulse at its bulk sound speed; pure classical acoustics | **C** (consistency / generic transport) | No — this is the SM-counterfactual control *by design*; it confirms the drive works, not that AVE is distinct |
| SELF-TRAP (2,3) knot does NOT translate under the same drive | nothing (drive-invariant) | partially — SM has no (2,3)-knotted soliton, but a generic "frozen heavy defect doesn't move under a weak bulk perturbation" is not AVE-specific | **negative result** (falsifies the AVE-distinct *positive* claim Grant proposed) | The NEGATIVE is load-bearing: it falsifies "stability-from-motion" on the decisive channel |

- **The would-be Class-D claim** (bemf-stabilized topological translation distinct
  from the linear control) **did not materialize** — the knot did not translate at
  all, so there is no emergence-class signal to claim. A SUPPORTS here would have
  had to clear the full Class-D bar (a dimensionless translation/retention coupling
  from primitives, distinct from the linear control); it does not even reach the
  starting line (zero knot translation).
- **Magnitude-vs-ratio discriminator axis (Step 2.5):** N/A — there is no positive
  AVE-distinct observable whose magnitude or ratio could discriminate. The only
  moving observable (LINEAR advection) shares BOTH form and scale with classical
  acoustics (it IS classical acoustics, by construction of the control).
- **Interpretive alternatives** for "knot doesn't move" (enumerated, not anchored):
  (A) genuine PIN — frozen V-core screens the bias [supported: mechanism measured,
  162× screening]; (B) coupling-blocked artifact — u never reaches z_local [refuted:
  S_ε responds monotonically to escalated drive, 0.96→0.08 at v_drive=30]; (C)
  drive too weak in absolute terms — would move at higher amplitude [true but
  physically irrelevant: the moving-electron-scale longitudinal compression IS this
  amplitude; reaching parity needs ~100× = rupture-scale]; (D) wrong channel — the
  electron's de-Broglie wake is self-sourced, not externally driven [OPEN — flagged
  for Grant above]. (A) is the operative mechanism; (D) is the live physics fork.

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
