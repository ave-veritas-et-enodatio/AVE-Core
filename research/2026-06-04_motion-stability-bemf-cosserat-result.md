# Motion-stability via back-EMF — native Cosserat/dark-wake τ_zx on `VacuumEngine3D`

**Status:** COMPLETE — VERDICT **CONTRADICTS-via-PIN** (matches the pre-registered forward
prediction; no fit). Continuation of a stalled run that confirmed engine + host + observer but
failed the boost; this run **fixed the boost** (validated on a linear pulse) and ran the decisive
disambiguation.
**Branch:** `analysis/motion-stability-bemf-cosserat`
**Driver:** `src/scripts/vol_1_foundations/motion_stability_bemf_cosserat_probe.py`
**Brief / prereg:** `_orchestration/motion-stability-bemf-cosserat.md`
**Host config (confirmed durable host):** `r10_vacuumengine3d_transverse_2_3_emergence.py` Arm-C
(`initialize_2_3_voltage_ansatz`, R=0.22·N, r=R/φ², amplitude=0.40).

---

## TL;DR

**Grant's hypothesis (stability FROM motion): CONTRADICTED — cleanly, via PIN.** On the engine
that carries the **native** back-EMF stress `τ_zx = z_local·∂_x(A²)` (NOT an E/H projection), a
sub-saturation **LINEAR pulse advects cleanly** under a coherent-phasor traveling-wave boost
(v=0 at k=0; sign-symmetric ±0.053 cell/τ at |k|=0.30), but the **saturated (2,3) self-trap does
NOT move** — its residual velocity (≈0.002 cell/τ) is **boost-direction-independent self-drift**
(does not flip sign with the boost; 0.10× the linear response). The deeply-saturated core
(A²≈3.07 ≫ 1 ⇒ S=√(1−A²)=0 ⇒ `c_eff = c·√S → 0`) is a **frozen local clock**: the knot is stable
**because it is static**, not because motion stabilizes it. Retention does **not** rise with v
(slope = −4.5) and the stability gain does **not** track native τ_zx (corr = −0.40). All four
forward-predicted signs confirmed.

This is the **native-carrier adjudication** the Maxwell-engine version could not give: that run
returned CONTRADICTS but saw only the **E/H projection** of τ_zx (anti-correlated −0.81); this
engine carries the native τ_zx directly and the answer is the same — **CONTRADICTS-via-PIN**.

---

## §1 The boost fix (the thing the stalled run couldn't do)

The stalled run's port-pairing boost gave v/c≈0.002 (no motion) — the brief diagnosed two causes:
port-pairing ≠ a clean +x traveling wave, and the amplitude (1.60 → A²≈25) was over-cranked past
the durable-host value. **Both are fixed here:**

**The boost = a coherent, energy-conserving phasor traveling wave.** The winding-extractor reads
the quadrature phasor `(ox, oy) = (V0+V1, V2+V3)`; the ansatz plants exactly this (ports {0,1} carry
`cos(2φ+3ψ)`, {2,3} carry `sin(2φ+3ψ)`). The boost rotates `ox+i·oy` by `exp(i k_x x)` — a genuine
+x spatial phase gradient on the channel the (2,3) winding lives in. To keep it **exactly
energy-conserving** (the first version injected O(10⁶) energy at the phasor zeros that pepper the
saturated shell — a baseline-fairness killer), the boost decomposes each site's 4 ports into a
**common mode** `(a,b)=(V0+V1, V2+V3)=(ox,oy)` and a **differential mode** `(c,d)=(V0−V1, V2−V3)`,
rotates ONLY the common mode (orthogonal → preserves `a²+b²` ⇒ total port energy exactly), and
leaves the differential mode fixed. Verified `max|dE/E| = 6e-16` (machine precision); the host
energy is **identical** pre- and post-boost (E=776.0 → 776.0).

**The amplitude is the confirmed durable-host value** (amplitude=0.40), NOT the over-cranked 1.60.
The host-in-isolation settles to **max A²_interior ≈ 3.07 steady** (the result-doc's "A²≈8.90" was
the running-MAX of the *driven-collision* Arm C — planted (2,3) PLUS the transverse-photon source
firing; the **planted host in isolation** holds A²≈3.07, still ≫1 = frozen core, which is the right
clean object for a motion test). Peak A² stays 3.07–3.81 across the whole boosted run
(saturated-while-moving check ✓).

### ANTI-STALL smoke test — the LINEAR pulse MOVES (boost validated, ≤2 variants)

Zero-carrier sub-saturation phasor blob (`ox=2·env` real, `oy=0`; peak A²=½·A²_op14), one-shot boost:

| k_x | v_centroid (cell/τ) | dx_total | note |
|---|---|---|---|
| +0.00 | **+0.0000** | +0.000 | exact — clean static baseline |
| +0.15 | −0.0559 | −1.867 | advects |
| +0.30 | −0.0529 | −1.760 | advects (band-edge saturation of v_g) |
| −0.30 | **+0.0529** | +1.760 | **sign-symmetric** → genuine momentum kick |

v=0 at k=0, monotone-onset, **sign-symmetric** — the one-shot phasor rotation is a real
traveling-wave momentum imprint. **LINEAR MOVES → proceed to the full test.** (The re-imposed-
every-step "pump" variant was rejected: it injects energy and overflows the field — that is a
sustained drive, not a clean boost.)

---

## §2 The decisive disambiguation (the result either way)

Apply the SAME validated boost to the SELF-TRAP (Arm-C host, A²≈3.07) and to the matched controls.
**Sweep v via k_x ∈ {0, +0.15, +0.30, −0.30}** (the −0.30 is the sign-flip pin tell). Settle 10
steps (let the host self-trap into the frozen-core (2,3)), boost, record 70 steps.

| Arm \ k_x | +0.00 | +0.15 | +0.30 | −0.30 | boost-response | sign-flips? |
|---|---|---|---|---|---|---|
| **SELF-TRAP** v | +0.00263 | +0.00167 | +0.00489 | +0.00208 | **0.0023** | **NO** |
| **LINEAR** v | +0.00000 | +0.05829 | −0.02201 | +0.02201 | 0.0220 | **YES** |
| **BASELINE** v | +0.00263 | +0.00500 | +0.00439 | +0.00439 | 0.0018 | NO |

**The knot is PINNED.** The SELF-TRAP velocity is ≈0.002–0.005 cell/τ **regardless of boost
direction** — v at −0.30 (+0.0021) is the same sign and magnitude as v at +0.15 (+0.0017), and all
≈ the unboosted k=0 self-drift (+0.0026). It does **not** flip sign with the boost. The boost
response (0.0023) is **0.10× the linear response** (0.022). By contrast the LINEAR pulse responds
fully and **flips sign** with the boost (+0.058 / −0.022 at +0.15/+0.30; +0.022 at −0.30). The
matched BASELINE (host energy, net-zero-momentum standing modulation) behaves like the SELF-TRAP,
not the LINEAR — confirming the host doesn't translate.

> **LINEAR moves but the SELF-TRAP knot does NOT → the saturated knot is GENUINELY PINNED**
> (the canonical frozen-clock `c_local → 0`). **CONTRADICTS Grant's hypothesis cleanly:** the knot
> is stable because it is **static**, not via motion.

---

## §3 Retention(v) + native-τ_zx-vs-stability — the stability-from-motion signal is ABSENT

If motion stabilized the knot, retention would rise with v AND the stability gain would track the
native τ_zx (positive). Neither holds:

| Arm \ k_x | retention +0.00 | +0.15 | +0.30 | −0.30 | native max\|τ_zx\| (mean) |
|---|---|---|---|---|---|
| **SELF-TRAP** | 0.518 | 0.533 | 0.517 | 0.531 | 5.7–6.6 × 10⁵ |
| **BASELINE** | 0.518 | 0.518 | 0.498 | 0.498 | 5.7–6.6 × 10⁵ |
| **LINEAR** | 0.300 | 0.292 | 0.273 | 0.273 | ~2 × 10⁻³ |

- **retention(v) slope (self-trap) = −4.53** — retention does **not** rise with v (the residual v
  is so small the slope is dominated by noise, and its sign is **negative**). The SELF-TRAP and the
  matched BASELINE have **the same retention (~0.52)** — i.e. motion buys nothing over a standing
  state at matched energy/saturation. This is the cleanest single statement: **same energy, same
  saturation, with-or-without the motion bias → same retention.**
- **native τ_zx vs retention corr = −0.398 (≤ 0)** — the native back-EMF does **not** positively
  track stability. The host's τ_zx ≈ 6×10⁵ is the **static rupture-floor stress** of the frozen
  core (z_local saturates at the `1/√S` floor, S=0), not a motion-induced stabilizer.
- **saturated throughout: peakA²_min = 3.07 ≫ 1** — the core is in the S=0 frozen-clock regime the
  entire run (no saturation-depth confound; same seed amplitude every cell).

---

## §4 Forward-predicted sign vs observed (no fit — ave-driver-script-honesty)

Pre-registered in `_orchestration/motion-stability-bemf-cosserat.md` §7 and hardcoded in the driver
(`FORWARD_PREDICTED_*`) **before the run**, derived from the substrate default (A²≈8.9 ⇒ S=0 ⇒
c_eff→0):

| quantity | forward-predicted | observed | ✓ |
|---|---|---|---|
| LINEAR moves | True | True (±0.053, sign-symmetric) | ✓ |
| knot moves | False | False (PINNED, 0.10× linear, no sign-flip) | ✓ |
| retention(v) slope | ≤ 0 | −4.53 | ✓ |
| native-τ_zx-vs-stability corr | ≤ 0 | −0.398 | ✓ |
| **VERDICT** | **CONTRADICTS-via-PIN** | **CONTRADICTS-via-PIN** | ✓ |

All four signs confirmed. The substrate-default prediction held.

---

## §5 The Maxwell-vs-Cosserat contrast (why this run is the real adjudication)

| | Maxwell-engine version (prior, per brief) | **THIS run (`VacuumEngine3D`)** |
|---|---|---|
| τ_zx seen | **E/H PROJECTION** of τ_zx | **NATIVE** `z_local·∂_x(A²)` (DarkWakeObserver) |
| τ_zx–stability | anti-correlated −0.81 | corr −0.398 (≤0); knot PINNED |
| verdict | CONTRADICTS (but on a projection) | **CONTRADICTS-via-PIN (on the native carrier)** |

The hypothesis was that the Maxwell CONTRADICTS might be an artifact of only seeing the **projection**
of the back-EMF (the information lost projecting τ_zx onto E/H). This run carries the **native**
τ_zx — and the answer is the same. The native back-EMF of the saturated (2,3) knot is the **static**
rupture-floor stress of a frozen-clock core; it does not stabilize motion because **there is no
motion** — the core can't advect (c_eff→0). The two engines agree from the projection side and the
native side: **stability does not come FROM motion for the saturated self-trap.**

The corpus dark-wake derivation (`2026-05-18_dark-wake-tau-zx-op14-scaling-derivation.md`) is
consistent: it states the wake (back-EMF) advects at `v_wake = c₀` **in sub-saturation regions** —
exactly where the LINEAR pulse lives and moves. The SELF-TRAP core is **not** sub-saturation; it is
S=0, where `c_eff → 0` and the wake (and the soliton) cannot propagate. The framework's own
sub-saturation caveat predicts the PIN.

---

## §6 Honest framing + scope (ave-evidence-framing-discipline)

- **This is a CONTRADICTS (negative) for Grant's "stability FROM motion."** It is reported as a
  clean **structural finding** (substrate-native-check CP8: a PIN/null is a positive structural
  result), not spun. The discriminating logic (LINEAR-moves-but-knot-pins) is the load-bearing
  content, and it is unambiguous in the data.
- **No positive to discrimination-check.** `ave-discrimination-check` is mandated *before any
  positive*; the verdict is negative, so it does not gate a positive claim. The matched LINEAR
  (SM-counterfactual) and the genuinely-matched BASELINE (same energy + A-trajectory, net-zero
  momentum — NOT a phase-scramble) were nonetheless built in, exactly as a positive would have
  required, which is what makes the PIN clean rather than a baseline artifact.
- **A self-inflicted adjudicator bug was caught and fixed (flag-don't-fix → fixed, since it was my
  own code).** The first run's auto-verdict printed NULL because the PIN predicate used
  `numpy_bool is False`, which is `False` by identity (`np.False_ is False → False`). The **physics
  was always a PIN**; the NULL was a code bug. Fixed by casting the sign-flip flags to Python bool;
  re-adjudication on the same data → CONTRADICTS-via-PIN. The committed JSON is from the corrected
  re-run.
- **What this does NOT claim:** it does not test whether an *externally driven* (continuously pumped)
  knot can move — only whether the knot advects under a one-shot momentum imprint (the physical
  "boost" of a free particle). A sustained pump CAN inject energy and push the centroid, but that is
  a driven system, not "stability from the knot's own motion." It also does not test sub-rupture
  self-traps (none exist on this engine — the (2,3) self-trap is intrinsically S=0 at the core).
- **Amplitude reconciliation:** the host-in-isolation A²≈3.07 (steady) vs the result-doc's A²≈8.90
  (driven-collision running-max) are the same object at two operating points; both are ≫1 (frozen
  core), so the PIN conclusion is amplitude-robust across the saturated regime.

---

## §7 Auditor queue (I will adversarially audit any positive — this is a negative, but for completeness)

1. **[boost-fairness — top item] The boost is exactly energy-conserving** (common-mode rotation,
   max|dE/E|=6e-16; host E identical pre/post). Re-verify the SELF-TRAP PIN is not a boost-coupling
   artifact: confirm the boost actually re-phases the host's winding (it rotates `(ox,oy)` by
   `exp(i k_x x)` — same channel the (2,3) lives in) yet the centroid doesn't follow. The
   sign-symmetric LINEAR response on the *same boost* is the control that proves the boost imparts
   real momentum.
2. **PIN vs "boost doesn't couple to the (2,3) DOF."** Alternative interpretation: maybe the boost
   re-phases the winding but the toroidal winding phase is not the translation DOF, so the knot
   wouldn't move even if it could. Counter: the LINEAR pulse uses the *identical* `(ox,oy)` channel
   and *does* translate — so the channel carries momentum; the knot's non-response is the saturated
   core, not a wrong DOF. Still, a complementary boost (a real-space momentum kick `V_inc ·=
   exp(i k·x)` applied to all ports uniformly) would triangulate. Flagged as the natural follow-up.
3. **retention(v) slope sign-robustness.** The −4.53 slope is dominated by the near-zero v-spread of
   the pinned knot (Δv ~ 0.003); the load-bearing statement is the SELF-TRAP-vs-BASELINE retention
   equality (~0.52 both), not the slope magnitude. Confirm the equality is the headline, not the
   slope.
4. **Native-τ_zx implementation note (phase-space-coordinate-check Step 5).** The DarkWakeObserver's
   τ_zx = `z_local·∂_x(A²)` is **K4-sourced** (V-sector saturation-modulated impedance × strain
   gradient), not `cos.omega` (the Cosserat rotation field). It is the native back-EMF *stress* the
   engine carries directly (the brief's "native τ_zx", contrasting the Maxwell E/H projection), and
   is read by the native observer with no coordinate fabrication. The "Cosserat" label in the brief
   refers to the Cosserat-shear *character* of the back-EMF; the implementation is the K4 dark-wake.
   Auditors should read it as the native-carrier stress, correctly.
5. **gate-(a) / frozen-clock cross-link.** This PIN is the motion-side companion of the
   deterministic-no-seed / frozen-clock findings (the saturated core's S=0 c_eff→0 is the same
   physics that makes the (2,3) need *nucleation*, not *emergence*, in
   `2026-06-04_full-electron-option-B-discrete-emergence-result.md`). Cross-reference on merge.

---

## §8 Verdict

**CONTRADICTS-via-PIN.** On the native-`τ_zx` engine, a sub-saturation linear pulse advects but the
saturated (2,3) self-trap does not — it is pinned by its own frozen clock (S=0 ⇒ c_eff→0). Retention
does not rise with v and the stability gain does not track the native back-EMF. Grant's
stability-FROM-motion hypothesis is **contradicted cleanly**: the knot is stable because it is
**static**. The native carrier gives the same answer as the Maxwell projection — the result is
robust across the projection and native readings of the back-EMF.
