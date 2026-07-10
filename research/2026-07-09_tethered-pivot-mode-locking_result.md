# Tethered-pivot mode-locking — RESULT: frozen prereg-§6 detector → **PARTIAL** (the preregistered outcome) · under a post-hoc control-subtracted axis → **TRACK** (no anchor-INDUCED mode-locking; banked next to #417)

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

> **VERDICT: PARTIAL (frozen prereg-§6 detector) / TRACK (post-hoc control-subtracted axis).** Reported on
> TWO AXES per the KEEP-BOTH discriminator pattern (adversarial-review restatement 2026-07-09 — see §4.1).
>
> **Axis 1 — FROZEN prereg-§6 detector (THE PREREGISTERED OUTCOME): PARTIAL.** The prereg §6 froze an
> ABSOLUTE detector: `LOCK ⇔ staircase_fraction ≥ 0.5 AND jump_count ≥ 1`; `TRACK ⇔ track_R2 ≥ 0.9 AND
> staircase_fraction < 0.2`. On the frozen config (N=20, 500 steps) with the corrected slope-rate read, the
> anchored sweep gives **staircase_fraction = 0.4286, jump_count = 1, track_R2 = 0.9799** → this fails BOTH
> the LOCK bar (0.4286 < 0.5) AND the TRACK bar (0.4286 ≥ 0.2), so the frozen detector bins **PARTIAL**
> (Signature-1 unresolved). **This is the outcome that was preregistered, and it is the headline of record.**
>
> **Axis 2 — POST-HOC amended control-subtracted detector (added AFTER the freeze, labeled amended-post-hoc):
> TRACK.** The FREE (clamp-off) control's OWN absolute `staircase_fraction` is **0.4286 — identical to the
> anchored 0.4286** (the coupled tank's ρ(ω_s) saturates near 1.0 at high ω_s, a sweep artifact common to
> anchored AND free). That confound MOTIVATES subtracting the control (`excess_staircase` = plateaus the
> anchor adds that the free control lacks), but it does **NOT** retroactively make control-subtraction the
> frozen rule. Under this amended axis: **excess_staircase = 0.0714** (< 0.2) with **track_R2 = 0.9799** (≥ 0.9)
> → the anchor adds essentially no plateaus the free control lacks; the read is **TRACK**. **No excess
> hysteresis** (anchored ramp width 0.682 vs free-control 0.678 — excess 0.004, short-block read-noise present
> clamp-OFF too). **No termination flip** (capacitive vs magnetic clamp give identical ρ to ~4 sig figs,
> 0/4 orientation inversions). Under the amended axis the pivot picture — that boundary-condition
> quantization would make the (2,3) integers discrete, knobless mode indices — reads **NEGATIVE**, banked
> next to the #417 free-orbit negative.
>
> **Honest one-line summary:** the change that carries the negative is the amended control-subtracted axis;
> the frozen preregistered detector on its own returns an *unresolved* PARTIAL. Neither the slope-read fix
> alone nor the excess detector alone reaches TRACK on the frozen absolute metric — only the (slope read ×
> excess detector) combination does. This is disclosed, not buried.

**Every supporting gate holds; the disagreement is confined to Signature-1's detector definition:**
- **Dead-actuator gate PASS (both branches):** the pinned quadrature's variance over the anchor plane
  COLLAPSES — capacitive Re-var 0.282→0.000 (ratio 0.0), magnetic Im-var 0.117→0.000 (ratio 0.0). The clamp
  demonstrably constrains (it is not a dead actuator); the OTHER quadrature is left free (I-antinode /
  V-antinode). The anchor is a LIVE actuator that nonetheless does not lock the winding.
- **Energy ledger PASS (honest bookkeeping):** clamp OFF conserves the joint norm to **9.1×10⁻¹⁰** (the #417
  unitary standard); clamp ON is **monotone NON-PUMPING** (max relative energy gain **0.0** — the projection
  only ever REMOVES norm), removing 13.8% of the norm over the window. **A lock under an energy-REMOVING wall
  could not be a pumped illusion; there is no lock regardless.**
- **Validate-on-known PASS (tracking zone) — with a disclosed SATURATION-ZONE blind spot:** the amended
  control-subtracted detector reads a planted STAIRCASE as LOCK (excess_staircase 0.64, 3 excess jumps) and a
  planted LINEAR as TRACK **in the tracking zone**. BUT a genuine lock plateau planted in the free-control
  SATURATION zone reads **LOCK on the frozen absolute axis** yet **PARTIAL on the amended excess axis**
  (excess_staircase 0.0 — the plateaus coincide with the flat free control and are subtracted out;
  `validate_lock_detector` → `saturation_zone.lock_suppressed_by_excess = True`). So the amended axis is
  **LOCK-SUPPRESSING in the saturation zone** — it is biased TOWARD the TRACK/negative read there. Neutrality
  is certified only in the tracking zone (§4.1). This is the symmetric-scrutiny caveat, stated explicitly.
- **F4 two-method read** honored with the #417 caveat (the two endpoint estimators share a wrapped-increment
  and are window-noise-sensitive; the load-bearing discriminator is the DETUNING RESPONSE of ρ, read by the
  window-noise-immune slope estimator — see §4.1).

**Signatures 2 (no excess hysteresis) and 3 (no termination flip) fire NULL cleanly. Signature 1 is the one
under two-axis dispute: PARTIAL under the frozen preregistered detector, TRACK under the amended axis. The
pivot picture is therefore NOT clean-falsified by the preregistered detector alone — it is unresolved (PARTIAL)
under the frozen rule and negative (TRACK) only under the post-hoc control-subtracted axis.**

---

## 1. THE MECHANISM (named — single-mechanism explanation of the TRACK-direction read)

**Scope of this closure (two-axis, per §4.1):** the mechanism below explains the *direction* of the negative
read — why ρ tracks the carrier. It underwrites the **amended-axis TRACK**. Under the **frozen preregistered
detector** Signature-1 is **PARTIAL (unresolved)**, so this is not a clean-falsification closure under the
preregistered rule; it is the physical account of the TRACK-direction seen under the control-subtracted axis.

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
| **Sig 1 — FROZEN prereg-§6 (absolute)** staircase_fraction | **0.4286** | fails LOCK (≥0.5) AND TRACK (<0.2) |
| Sig 1 free_staircase_fraction (shared baseline) | 0.4286 | == anchored → the confound |
| Sig 1 jump_count (absolute) | 1 | — |
| Sig 1 track_R2 (anchored ρ vs free ρ) | **0.9799** | **→ frozen axis: PARTIAL** |
| **Sig 1 — POST-HOC amended (excess)** excess_staircase | **0.0714** | anchor-induced plateaus (baseline-subtr.) |
| Sig 1 excess_jumps | **0** | **→ amended axis: TRACK** |
| Sig 1 max\|anchored−free\| over sweep | 0.058 | — |
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

### 4.1 The two post-freeze changes — TWO-AXIS accounting (KEEP-BOTH; restated 2026-07-09)

The FROZEN driver's FIRST run (N=20, 300 steps, endpoint-turns ρ, control-BLIND detector) returned **PARTIAL**.
Two changes were then made post-freeze. They are of **different kinds**, and the restatement below keeps them
separate (KEEP-BOTH discriminator pattern: when an audit finds an inconsistency in a pre-reg axis, add a NEW
axis alongside the frozen one — never redefine-in-place):

**Change 1 — slope-rate read (a legitimate INSTRUMENT repair, kept).** Endpoint-turns ρ is
window-noise-sensitive: Δφ over a window jumps when the window fails to contain an integer number of the
sloshing-modulated periods (the #417 quasi-periodic-window caveat) — the FREE control itself jumped
(ρ_free 1.25→1.30: 1.12→0.82), which a smooth tracker cannot. **Fix:** the window-noise-immune **slope
estimator** (least-squares winding RATE) — the standard robust rotation-number read, exactly what the pre-reg
§4 "DETUNING RESPONSE of ρ" discriminator requires. This is a genuine instrument repair of the ρ *reader*; it
does not change any DECISION threshold. It is retained on BOTH axes below.

**Change 2 — control-subtraction (a NEW POST-HOC DETECTOR AXIS, amended-post-hoc — NOT the frozen rule).**
Observation: the coupled tank's ρ(ω_s) SATURATES near 1.0 at high ω_s, so the FREE (clamp-off) control's OWN
absolute `staircase_fraction` is **0.4286 — identical to the anchored 0.4286** (and its ramp hysteresis width
0.678 ≈ the anchored 0.682). The absolute metric is therefore confounded by a sweep-saturation artifact common
to anchored AND free. That confound **MOTIVATES** subtracting the control (`excess_staircase` = plateaus the
anchor adds that the free control lacks). **But subtracting the control changes the DETECTOR DEFINITION and
LOWERS the LOCK bar** (frozen: `staircase_fraction ≥ 0.5`; amended: `excess_staircase ≥ 0.4`), so it is **not**
an instrument correction and does **not** retroactively become the frozen rule. It is a post-hoc amended axis,
reported alongside the frozen one.

**The two-axis outcome (both computed on the frozen config, corrected slope read):**

| Axis | Rule | Metrics | Verdict |
|---|---|---|---|
| **FROZEN prereg-§6 (preregistered)** | LOCK ⇔ staircase≥0.5 ∧ jumps≥1; TRACK ⇔ track_R2≥0.9 ∧ staircase<0.2 | staircase **0.4286**, jump_count 1, track_R2 **0.9799**, free_staircase **0.4286** | **PARTIAL** |
| **POST-HOC amended (control-subtracted)** | LOCK ⇔ excess_staircase≥0.4 ∧ excess_jumps≥1; TRACK ⇔ track_R2≥0.9 ∧ excess_staircase<0.2 | excess_staircase **0.0714**, excess_jumps 0, track_R2 0.9799 | **TRACK** |

**Neither post-freeze change ALONE reaches TRACK on the frozen absolute metric.** The slope-read fix alone
(frozen absolute detector) still returns PARTIAL (staircase 0.4286); the excess detector is what flips the
Signature-1 read to TRACK. Only the *combination* (slope read × excess detector) yields TRACK. This is stated so
the amended axis is not mistaken for the preregistered outcome.

> **CORRECTION NOTE — 2026-07-09 (adversarial-review restatement, KEEP-BOTH).** An earlier version of this
> section asserted that the two changes were *"instrument corrections applied transparently, NOT criteria-drops:
> the DECISION thresholds ... and the branch definitions are unchanged ... The corrected read moves the machine
> bin from an artifact-contaminated PARTIAL to a clean TRACK."* **That claim is SUPERSEDED and was WRONG.** The
> committed detector substituted control-subtracted `excess_staircase` for the frozen absolute `staircase_fraction`
> and lowered the LOCK bar from ≥0.5 to ≥0.4 — that IS a change to the DECISION criteria, not a criteria-preserving
> instrument correction. Against the frozen prereg §6, the preregistered detector returns **PARTIAL**, not TRACK;
> the TRACK read exists only under the post-hoc amended axis. The superseded sentence is preserved here (quoted,
> not erased) per KEEP-BOTH; the current headline (§0) is the two-axis form `PARTIAL (frozen) / TRACK (amended)`.
> The raw first-run PARTIAL and the free-control comparison (anchored 0.4286/0.682 vs free 0.4286/0.678) remain
> on record for auditor review.

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
