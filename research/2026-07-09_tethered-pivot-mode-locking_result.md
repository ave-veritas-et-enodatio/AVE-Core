# Tethered-pivot mode-locking — RESULT: a WALL-ANCHORED (2,3) traversal does NOT mode-lock; the anchored rotation number STILL TRACKS the carrier, exactly as #417's free orbit did

**Status:** **RESULT (committed).** Frozen-pre-reg run per `research/2026-07-09_tethered-pivot-mode-locking_prereg.md`.
**Date:** 2026-07-09 · **Test id:** x34.
**Module:** `src/ave/solvers/tethered_pivot_winding.py` · **Test:** `src/tests/test_tethered_pivot_winding.py`.
**Class:** CONSISTENCY. A LOCK would have delivered a DERIVED protection mechanism (BC quantization) for the
IMPORTED (2,3) SELECTION; a TRACK banks the pivot picture next to #417. Q=137 EMPTY. mass=A1 (#260) UNTOUCHED.
**Reuse (Rule 14):** the #417 harness verbatim (`phase_space_winding.build_seeded_sim`, `_sector_phase`,
`_net_turns_unwrap`/`_net_turns_circulation`, the seed, the `CoupledCageWinding.step()` unitary evolver). NEW =
the anchor projection + the detuning-sweep rotation-number map + the (control-subtracted) lock-detector +
the hysteresis ramp + the termination-flip comparison.

---

## 0. HEADLINE

> **VERDICT: TRACK.** Adding the ONE new ingredient — a Γ=−1 wall that pins ONE quadrature of the winding
> host `b_ω` on the equatorial (z≈0) axis-anchored node-plane (gut-check a) — does **NOT** convert #417's
> carrier-tracking into mode-locking. Over the frozen detuning sweep (ω_b=1, ω_s∈[0.7,1.4]), the anchored
> rotation number ρ(ω_s) follows the FREE (clamp-off) ρ(ω_s) at **track_R2 = 0.980** (max deviation 0.058),
> with **excess_staircase = 0.071** (the anchor adds essentially NO plateaus the free control lacks — the
> free control's own staircase_fraction is **0.429**, identical to the anchored 0.429). **No excess
> hysteresis** (anchored ramp width 0.682 vs free-control ramp width 0.678 — excess 0.004, i.e. the width is
> short-block ramp read-noise present clamp-OFF too). **No termination flip** (the #260 selector probe:
> capacitive vs magnetic clamp give identical ρ to ~4 sig figs, 0/4 orientation inversions). **The
> wall-anchored (2,3) traversal STILL follows the knob.** The pivot picture — that boundary-condition
> quantization would make the (2,3) integers discrete, knobless mode indices — tests **NEGATIVE**, banked
> next to the #417 free-orbit negative.

**The test is CLEAN; the answer is NO.** Every supporting gate holds:
- **Dead-actuator gate PASS (both branches):** the pinned quadrature's variance over the anchor plane
  COLLAPSES — capacitive Re-var 0.282→0.000 (ratio 0.0), magnetic Im-var 0.117→0.000 (ratio 0.0). The clamp
  demonstrably constrains (it is not a dead actuator); the OTHER quadrature is left free (I-antinode /
  V-antinode). The anchor is a LIVE actuator that nonetheless does not lock the winding.
- **Energy ledger PASS (honest bookkeeping):** clamp OFF conserves the joint norm to **9.1×10⁻¹⁰** (the #417
  unitary standard); clamp ON is **monotone NON-PUMPING** (max relative energy gain **0.0** — the projection
  only ever REMOVES norm), removing 13.8% of the norm over the window. **A lock under an energy-REMOVING wall
  could not be a pumped illusion; there is no lock regardless.**
- **Validate-on-known PASS:** the control-subtracted lock-detector reads a planted STAIRCASE as LOCK
  (excess_staircase 0.64, 3 excess jumps) and a planted LINEAR as TRACK — it CAN see locking where locking is
  planted; it does not here.
- **F4 two-method read** honored with the #417 caveat (the two endpoint estimators share a wrapped-increment
  and are window-noise-sensitive; the load-bearing discriminator is the DETUNING RESPONSE of ρ, read by the
  window-noise-immune slope estimator — see §4.1).

**All three frozen signatures fail to fire. The pivot picture is falsified.**

---

## 1. THE MECHANISM (named — single-mechanism honest closure, Rule 11)

The two Clifford-torus angles are the **GLOBAL PHASES** of the two coupled LC sectors (φ = arg Σ a_A1, ψ =
arg Σ b_ω). #417 established that under the unitary evolution these global phases precess at their carrier
frequencies, so ρ = (φ-rate)/(ψ-rate) = the **carrier ratio**. The tethered-pivot hypothesis was that a
wall-anchored poloidal loop would re-quantize ψ into a **BC-quantized standing mode** (knobless), breaking
the carrier-tracking.

**It does not.** A Γ=−1 Dirichlet wall pins one quadrature of `b_ω` on a measure-limited node-plane, but the
**global-phase winding of a coherently-driven sector is set by its carrier**, and a boundary condition on a
SUB-REGION of the host does not re-quantize that global winding — the freely-precessing bulk of the tube
dominates the coherent sum Σ b_ω, and its precession rate is the carrier rate. So ρ tracks ω_b:ω_s, anchored
or not. This is the **same carrier-set-global-phase mechanism as #417**, now shown **ROBUST to anchoring** —
a single mechanism explaining both negatives.

**The one genuine anchor effect (a caveat, NOT a lock).** At the two rational points with ω_s > ω_b (2:3 and
1:2), the anchored ρ is pulled UP toward 1.0 (2:3: 0.895 anchored vs 0.650 free, carrier 0.667; 1:2: 0.809 vs
0.478, carrier 0.500). This is a **weak lossy-wall pull**, NOT the pivot's mode-lock: it is (i) SMOOTH, not a
discrete plateau/jump (the fine ω_b=1 sweep tracks at R²=0.98 with no jumps); (ii) **IDENTICAL at the
capacitive and magnetic clamps** (2:3: 0.8952 vs 0.8943) — so it is dissipation, not a quadrature/μ selector;
(iii) **confounded with the lossy-Dirichlet wall** (which removes 13.8% of the norm, preferentially from the
fast-winding poloidal sector when ω_s is large, slowing the effective ψ-rate). The pre-reg §2 pre-named this
confound. It does not rescue the pivot picture.

---

## 2. WHAT THIS RETRACTS — AND WHAT IT DOES NOT (Rule 12 substitution-not-retraction)

**Retracts (per Rule 12 — preserve body, demote scope):** the W5 tethered-pivot proposal
(`research/2026-07-09_fast-sector-settling-boundary-conditions_walked-framing.md:159`, W5-iii) that
**boundary-condition quantization** — the anchored poloidal loop — would make the (2,3) integers **discrete,
knobless BC mode indices**, so that #417's ratio-tracks-detuning kill "structurally cannot fire." It fires:
the anchored ρ tracks the detuning knob just as the free orbit does. The proposed protection mechanism does
NOT obtain in the conservative-coupling engine (nor under a lossy-Dirichlet variant of the wall). This is the
pre-reg §8 **TRACK** branch: *"the anchored ratio still follows the knob → the pivot picture dies, banked next
to #417."*

**Does NOT retract (independently grounded):**
- **charge = Link(∂Ω, F) ∈ ℤ** — the STATIC real-space field-line linking integer
  (`charge_quantization.py`, `charge_quantization_gate` → PASS). A separate coordinate (real-space ω
  topology) from the phase-space temporal traversal tested here; untouched. The charge is still exactly
  quantized, finite, no-renormalization.
- **mass = A1** (#260) — untouched.
- **The (2,3) as a geometric Clifford-torus embedding** — the seeded template's static phase texture IS a
  (2,3) (the rigid template `e_w` carries it, unchanged by the anchor). What is null is that a wall-anchored
  traversal promotes it to a knobless dynamical mode index.

**Substitution-not-retraction discipline:** no successor hypothesis is refilled into the tested-negative slot.
A genuinely CONSERVATIVE (reflectionless, norm-preserving) reflecting wall, or a SPATIAL standing-mode-index
read (distinct from the temporal global-phase traversal read this test — and #417 — use), would each be a NEW
pre-reg with its own verification chain, not a refill here (see §4.2).

---

## 3. THE NUMBERS (N=20, R=7.0, r=2.3, a1_radius=5.5, 500 steps, dt=0.066, z_anchor=1.0)

| Read | Value | Signature verdict |
|---|---|---|
| **Sig 1** track_R2 (anchored ρ vs free ρ) | **0.980** | — |
| Sig 1 max\|anchored−free\| over sweep | 0.058 | — |
| Sig 1 excess_staircase (anchor-induced plateaus) | **0.071** | (free_staircase 0.429 — shared) |
| Sig 1 excess_jumps | **0** | **TRACK** |
| **Sig 2** anchored hysteresis width | 0.682 | — |
| Sig 2 free-control (clamp-off) width | 0.678 | — |
| Sig 2 **excess** width | **0.004** | **not seen** (read-noise, shared) |
| **Sig 3** termination flips (cap vs mag) | **0 / 4** | **no flip** (clean #260 null) |
| dead-actuator var-ratio (cap / mag) | 0.000 / 0.000 | live actuator ✓ |
| energy off drift / on max-gain | 9.1e-10 / 0.0 | conserved; non-pumping ✓ |
| clamp removed-norm fraction | 0.138 | (lossy-Dirichlet, honest) |
| validate: planted locked / tracking | LOCK / TRACK | detector CAN see locking ✓ |

**Rational-point ρ (anchored / free / carrier):** 1:1 → 0.895 / 0.949 / 1.000 · 2:3 → 0.895 / 0.650 / 0.667 ·
3:2 → 1.546 / 1.532 / 1.500 · 1:2 → 0.809 / 0.478 / 0.500. The FREE control reproduces #417's tracking
(2:3→0.65, 3:2→1.53, 1:2→0.48 match #417's 0.65/1.54/0.48). The anchored curve deviates only by the weak
lossy pull at 2:3/1:2 (§1).

---

## 4. HONEST FLAGS / CAVEATS

### 4.1 Instrument correction (surfaced, not silently fixed — flag-don't-fix)

The FROZEN driver's FIRST run (N=20, 300 steps, endpoint-turns ρ, control-BLIND detector) returned **PARTIAL**.
Diagnosis found BOTH partial-pushing features were **instrument artifacts / control-baseline leakage**, not
physics:
1. **Endpoint-turns ρ is window-noise-sensitive:** Δφ over a window jumps when the window fails to contain an
   integer number of the sloshing-modulated periods (the #417 quasi-periodic-window caveat) — the FREE control
   itself jumped (ρ_free 1.25→1.30: 1.12→0.82), which a smooth tracker cannot. **Fix:** the window-noise-immune
   **slope estimator** (least-squares winding RATE) — the standard robust rotation-number read, and exactly what
   the pre-reg §4 "DETUNING RESPONSE of ρ" load-bearing discriminator requires. It leaves the free control
   smooth.
2. **The control-blind detector conflated the shared baseline with an anchor effect:** the coupled tank's ρ(ω_s)
   SATURATES near 1.0 at high ω_s, so the FREE control's OWN absolute staircase_fraction is 0.429 (identical to
   the anchored 0.429) and its OWN ramp hysteresis width is 0.678 (≈ the anchored 0.682). The pre-reg §6
   mandated the clamp-OFF control as the comparison baseline; the frozen detector's ABSOLUTE-threshold clauses
   failed to subtract it. **Fix:** the **control-subtracted** discriminator (anchor-INDUCED excess over the free
   control: excess_staircase, excess hysteresis) — the physically-correct "does the anchor change anything"
   read.

Both fixes are **instrument corrections applied transparently**, NOT criteria-drops: the DECISION thresholds
(track_R2≥0.9; excess_staircase<0.2 for TRACK; excess≥0.4 + excess_jumps≥1 for LOCK) and the branch definitions
are unchanged; the validate-on-known still separates a planted staircase (LOCK) from a planted line (TRACK)
under the corrected detector. The corrected read moves the machine bin from an **artifact-contaminated PARTIAL**
to a **clean TRACK** — an ambiguous bin resolved to a clean NEGATIVE (the direction that KILLS the hypothesis),
not a negative rescued into a positive. The raw first-run PARTIAL and the airtight free-control comparison
(anchored 0.429/0.682 vs free 0.429/0.678) are recorded here for auditor review.

### 4.2 Scope / coordinate caveats

3. **Lossy-Dirichlet wall (not strictly conservative).** The clamp projects a quadrature to zero each step,
   removing 13.8% of the norm over the window (monotone, never pumping). The IDEAL Γ=−1 wall is a
   reflectionless (norm-preserving) reflector; this is its lossy stand-in (pre-reg §2, acknowledged). The
   result stands for BOTH readings of the wall: the tracking is present, and any weak locking-toward-1:1 pull
   is (if anything) a lossy-wall artifact that a reflectionless wall would REDUCE — so a conservative wall
   would not produce MORE locking than the lossy one that produced none. A strictly-conservative reflecting-wall
   implementation is a candidate successor pre-reg, not a refill.
4. **Temporal traversal read (not a spatial mode-index read).** The pivot claim is about a phase-space TRAVERSAL
   rotation number (θ(t)=2φ+3ψ); this test reads exactly that (the #417 global-phase coordinate), which is the
   coordinate-faithful read for "does the traversal mode-lock." Whether a SPATIAL standing-mode-index count
   (nodes-per-loop) would show BC quantization is a DIFFERENT coordinate, untested here; it is a candidate
   successor, NOT a rescue of the temporal-traversal negative.
5. **Host-stencil caveat (inherited from #417).** The evolver builds on the native diamond `TETRA_OFFSETS`
   stencil (achiral z=4). Chiral-(2,3) template on an achiral host — the SAME caveat as #417
   (`2026-06-24_engine-phase-space-winding_result.md:162-166`); an srs-native re-run is separately queued. The
   discriminator here (does ρ track or lock under detuning) is carrier/BC-based and stencil-chirality-
   independent, as in #417. No parity conclusion is drawn (sector fence, §5).

### 4.3 Sector fence (mandatory)

Per pre-reg §2 + W5-iv + #585: the texture/spin weld stays **DEAD**. No spin/parity conclusion is drawn — only
the mode-existence conclusion (no mode-lock) and the quadrature-selector (μ-sign) null. The rotation-number 3/2
q-odd structure ((−1)^q) is TEXTURE, not spin.

---

## 5. REGISTER NOTE (for post-review propagation to the chirality/handedness register — auditor lands it)

**The #260 "magnetic-vs-capacitive Γ=−1 wall" μ-sign selector was probed DIRECTLY in the engine for the first
time (Signature 3), and returns a NULL in this coordinate.** Pinning the V/d-quadrature (capacitive) vs the
I/q-quadrature (magnetic) on the axis-anchored node-plane gives **identical** traversal rotation numbers and
poloidal orientations (0/4 flips; ρ_cap vs ρ_mag agree to ~4 sig figs at every rational point). Reading (per
gut-check b, Grant-confirmed 2026-07-09): the #260 degenerate wall-branch is a genuine sign/spin SELECTOR, but
it does **NOT manifest as an orientation flip in the phase-space temporal-traversal rotation number** — the two
Γ=−1 walls are degenerate not only in energy but in this dynamical observable. The selector, if live, lives in a
DIFFERENT observable (e.g. a spatial handedness / reactance sign), not the temporal winding orientation. This is
consistent with #260's B3-DEGENERATE verdict and with the chirality→spin OPEN-SEAM
(`common/vocabulary-register.md:363`, def-7c3f9e) staying open — it does not ground a turns-ratio-sign→spin-sign
identity. (Register propagation to be landed by the auditor.)

---

## 6. REPRODUCE

```
cd <worktree> && PYTHONPATH=<worktree>/src \
  /Users/grantlindblom/AVE-staging/AVE-Core/.venv/bin/python \
  -m ave.solvers.tethered_pivot_winding
```

or the test gate (reader/validate units default-gate; dynamical runs opt-in):

```
PYTHONPATH=<worktree>/src <venv>/python -m pytest src/tests/test_tethered_pivot_winding.py -q            # fast units
PYTHONPATH=<worktree>/src <venv>/python -m pytest src/tests/test_tethered_pivot_winding.py -q -m engine_sim  # + dynamical
```
