# Moving-Front Freeze-In — RESULT

**Date:** 2026-06-30
**Branch:** `analysis/moving-front-freezein` (off main `eaadeaf1`)
**Frozen prereg:** [`research/2026-06-30_moving-front-freezein_prereg_FROZEN.md`](2026-06-30_moving-front-freezein_prereg_FROZEN.md) (SHA-pinned `7b97e76d`)
**Engine:** [`src/ave/topological/moving_front_freezein.py`](../src/ave/topological/moving_front_freezein.py) (`22a35fb8`)
**Driver:** [`src/tests/test_moving_front_freezein.py`](../src/tests/test_moving_front_freezein.py)
**Lane:** implementer. Adjudication trail for a LATER KB/manuscript promotion; `research/`-only.

> **Honest-closure posture (Rule 11 / Rule 12).** This is a MAKE-OR-BREAK framed
> falsification-first. The result below is reported at its honest class. Where a
> pre-registered prediction fails, the failure is recorded with the single
> mechanism that explains it (Rule 11), and the hypothesis slot is retracted, not
> refilled with a rescue (Rule 12). Where the engine conflicts with a corpus
> claim, both are surfaced verbatim (flag-don't-fix); neither is reframed to
> match the other.

---

## §0 SECTOR / REGIME HEADER

Same as prereg §0. MODE = cosmological crystallization front; REGIME =
propagating yield-crossing at v_front near saturation; PHASE-STATE = transitional.
Native BEMF-blocked-unwinding mechanism (NOT Kibble-Zurek). Coordinates: real-space
ω-defect only.

## §1 THE DERIVED FREEZE-DIRECTION + CONFLICT RESOLUTION (headline of the derive-first call)

**Derived direction (prereg §2.3, from the memristive-lag ODE):**
**FAST crossing (`Δt_cross = ℓ_front/v_front ≲ τ_relax`, high `v_front`) → FREEZE;
SLOW crossing (`Δt_cross ≫ τ_relax`) → HEAL.** The discriminator is the
dimensionless `Δt_cross/τ_relax`.

**Mechanism:** on a fast down-crossing the memristive `S(t)` lags below `S_eq(r)`
(`59_`:103), so `S` stays low even after `r` has dropped and `S_eq` has recovered;
low `S` keeps `L_eff = Z_0/√S` (hence the Lenz back-EMF) large, so the block on
`dω/dt` PERSISTS through and beyond the geometric crossing. A slow crossing tracks
`S(t) ≈ S_eq(r)` quasi-statically, so the block lifts as soon as `r < 1` and the
winding unwinds. Corroborated by `59_` §7.1 (fast → freeze-at-average) / §7.2
(slow → full heal per cycle).

**Conflict resolution (flag-don't-fix).** The two corpus one-liners disagree:
- `dark-wake-bemf-foc-synthesis.md:54` (clm-exjfai): *"crossing takes ≥ τ_relax →
  FREEZES"* — reads SLOW → freeze.
- grounding-pass: *"faster than τ_relax → freeze, slower → heal"* — reads FAST → freeze.

**The grounding-pass direction (fast → freeze) is CORRECT per the memristive-lag
mechanism; `dark-wake-bemf:54` is BACKWARDS as literally stated.** It conflates
"the block is available for a duration τ_relax" with "the crossing must span
τ_relax." The operative discriminator on `dω/dt` is that the transit be SHORT
relative to the S-relaxation recovery, so the lagged-low `S` keeps `L_eff` large
across the transit. **FLAG (for Grant/auditor):** clm-exjfai's prose direction is
a candidate for a Rule-12 dated correction — the auditor lands it; not touched here.

## §2 THE TWO-ARM OUTCOME (Guard 2)

Authoritative dataset ([`..._results.json`](2026-06-30_moving-front-freezein_results.json);
single JAX-warm run, N=12, PML=3; τ_relax=1 native; τ_disperse=0.225 Compton — the
bare ω-loop's natural front-OFF dispersion time). Persistence = Compton periods
holding Q ≥ Q_pre (3-sample window-median) AFTER the front cleared the defect ring.

| v_front | Δt_cross/τ | regime (pred) | bare persist | memr persist | memr S_min | bare S_min |
|---|---|---|---|---|---|---|
| 0.5 (slow) | 4.0 | SLOW→HEAL | 1.01 Cp | 3.04 Cp | 0.04 | 0.00 |
| 1.0 (mid)  | 2.0 | SLOW→HEAL | 1.35 Cp | 0.45 Cp | 0.19 | 0.00 |
| 4.0 (fast) | 0.5 | FAST→FREEZE | 1.58 Cp | 1.46 Cp | 0.56 | 0.00 |

**What the two-arm contrast SHOWS (the real, resolution-robust signal):**
- **The memristive lag is demonstrably active, and its magnitude tracks the
  crossing rate exactly as prereg §2.3 derived.** The memristive S_min at the
  defect RISES MONOTONICALLY with v_front: **0.04 → 0.19 → 0.56**. Faster crossing
  → the lagged S(t) is caught HIGHER (the front clears before S can bottom), i.e.
  `L_eff = Z_0/√S` is held further from its full-collapse divergence on a fast
  transit. The bare arm's S collapses fully to 0.00 at every speed (no memory).
  This is the `dS/dt = (S_eq−S)/τ_relax` memory operating, and its rate-dependence
  is the §2.3 direction, CONFIRMED at the local-S level.

**What the two-arm contrast does NOT show (the honest negative):**
- **Neither arm achieves LASTING persistence.** All Q_end ≤ 1; the longest hold is
  3.04 Cp (memristive, slow). The prereg G3 target (≥ 100 Compton periods, per
  `dark-wake:54` / `59_`:639) is NOT met — by ~30×.
- **Real-space defect persistence does NOT separate the arms.** The persistence
  numbers are jittery (memr 3.04 / 0.45 / 1.46; bare 1.01 / 1.35 / 1.58) and the
  BARE arm actually holds LONGER than memristive at v=1.0 and v=4.0. The window in
  which the front is passing over the defect inflates both arms' hold equally
  (front-present saturation holds the winding regardless of memory), so the
  "beats_disp" threshold (τ_disperse×1.5 = 0.34 Cp) is passed by everything and is
  NOT discriminating.

## §3 THE DISCRIMINATOR SWEEP vs PRE-REGISTERED PREDICTION

Prereg §2.3 predicted: FAST → FREEZE (lasting real-space defect), SLOW → HEAL, with
real-space defect PERSISTENCE rising as v_front rises.

**Split verdict:**
- **CONFIRMED (local-S mechanism):** the memristive S-lag magnitude rises
  monotonically with v_front (0.04→0.19→0.56) — the fast-crossing → less-S-collapse
  → block-held-higher direction of §2.3 is exactly reproduced. The
  `dark-wake:54`-vs-grounding-pass resolution (§1: fast→block-persists) is
  corroborated at the level of the S-field memory.
- **NEGATIVE (the actual claim — lasting real-space defect freeze):** that local-S
  memory does NOT translate into a lasting frozen real-space ω-defect. Real-space
  persistence is transient (≤ 3 Cp) and does NOT rise with v_front; the bare arm
  can out-persist the memristive arm. The pre-registered freeze (defect PERSISTS
  ≥ 100 Cp behind a fast front) FAILS.

The mechanism the discriminator was built to test (S-lag → BEMF block) is present
and rate-dependent as derived; the OBSERVABLE it was supposed to produce (a lasting
real-space defect) is absent. §4 names the single reason.

## §4 THE MAKE-OR-BREAK VERDICT + THE SINGLE EXPLANATORY MECHANISM

**VERDICT: the moving-front realization does NOT deliver a lasting frozen-in
real-space ω-defect. The BEMF `dω/dt` block operates (memristive S-lag active and
rate-dependent exactly as derived — S_min rises 0.04→0.19→0.56 with v_front), but
the frozen winding DISPERSES within ≤ 3 Compton periods once the front's saturation
lifts, and real-space persistence does NOT separate the two arms. This is a clean,
honest NEGATIVE on the lasting-freeze claim (prereg F1), with a single explanatory
mechanism (Rule 11).**

**The single mechanism that explains ALL of it (the load-bearing finding — flag,
don't fix):** the engine's re-solidified Cosserat solid is a **linear-elastic
shear-wave medium with NO topological-pinning term.** The bulk acceleration is
`_bulk_accel → _bare_linear_gradient` ([`cosserat_field_3d.py:1999`](../src/ave/topological/cosserat_field_3d.py))
— a matched linear shear wave. The front-clamp (`_rotate_clamp` gated on
`relu(−Γ)`) pins ω ONLY while S < 1 (front present / saturation active). The
moment the front passes and S recovers toward √(1−r²), the clamp lifts and the ω
winding — which is NOT a stationary soliton — radiates away as a dispersing
linear-elastic wave packet (measured τ_disperse = 0.23 Cp front-off).

The BEMF block therefore does exactly what its physics says — it blocks `dω/dt`
*during the S-low window* — but there is **no engine term that holds the winding in
place AFTER S recovers.** The canonical claim (`59_` §4.3, verbatim: *"the frozen
ω configuration is now a TOPOLOGICAL DEFECT in the re-solidified vacuum. It cannot
be removed by smooth deformation (Ax1 protects topology)"*) asserts an Ax1
topological-protection that PINS the frozen winding in the solid. **The engine as
built does not implement that pin** — the linear-elastic bulk has no nonlinear /
topological restoring term, so a real-space ω-loop is not protected and disperses.

**FLAG (flag-don't-fix, for Grant / auditor adjudication — NOT resolved here):**
this is an engine-vs-corpus conflict. The corpus (`59_` §4.3, clm-exjfai) claims
Ax1 protects the frozen ω-defect in the re-solidified solid; the engine's Cosserat
bulk provides no such protection (linear-elastic, dispersive). Per A44
(missing-axiom-vs-engine-bug), this is surfaced as EITHER (a) an engine gap — the
Cosserat solid needs the Ax1 topological-protection term the corpus asserts, not
yet implemented — OR (b) a corpus over-claim — Ax1 "protects topology" may not
hold for a bare real-space ω-loop that is not itself a stabilised soliton. I do NOT
adjudicate which; I do NOT draft an Ax5 (A44); the auditor/Grant rule. Both sides
are cited verbatim above.

**Consistency note (consensus-bias symmetric-standard):** the mechanism-level
positive (memristive lag active, longer hold) is real and would, in a standard-model
lattice-defect study, be reported as "relaxation-time memory slows defect
annihilation" — a legitimate finding. The honest scope here is: AVE's engine shows
the SLOWING but not the LASTING FREEZE, because the pinning term is absent.

## §5 GUARD STATUS (all four)

1. **TRAP-not-CREATE — HELD (PASS).** G1: the defect exists at seed (Q0=1) and is
   NOT front-sourced (energy conserved under lossless front-off evolution,
   rel_drift ≤ 5e-3 at PML=0). No winding appeared from the front's energy input —
   confirmed by the pre-front lossless check. The barred self-formation slot was
   not re-entered.
2. **LOCK-not-FLASH two-arm — HELD (PASS, at the mechanism level; NEGATIVE at the
   observable level).** Both arms ran side-by-side. The memristive
   irreversibility-memory (S-lag, rate-dependent S_min 0.04→0.19→0.56) is present in
   B and ABSENT in A (bare S collapses to 0.0 at all speeds). The MECHANISM contrast
   is real and resolution-robust. But the arms did NOT diverge into
   lasting-freeze-vs-heal at the real-space-defect OBSERVABLE (both transient ≤ 3
   Cp; bare even out-persists memristive at 2 of 3 v_front) — that is the §4
   negative, not a guard breach. The two-arm control did its job: it showed the
   memristive irreversibility exists locally but does NOT produce a lasting frozen
   defect.
3. **COORDINATE DISCIPLINE — HELD (PASS).** The detector is a real-space contour
   winding on the ω-field (`extract_crossing_count`); no phase-space (2,3) claim
   was made. The seed geometry is a real-space poloidal ω-loop.
4. **NO OVER-CLAIM — HELD (PASS).** No m_e claim; no η-magnitude route; chirality
   fixed by IC, not derived. The negative result headlines nothing.

## §6 CLASSIFICATION (consistency-vs-emergence)

- **This result is a CONSISTENCY-class NEGATIVE.** The build tested whether the
  canonical (Ax1+Ax3+Ax4+Op14+Lenz) mechanism, realized as a moving front, delivers
  a lasting frozen real-space defect. It does not (at the tested resolution),
  because the engine lacks the Ax1 topological-pinning term the mechanism assumes.
  Nothing new EMERGED; a canonical consequence FAILED to manifest in the engine.
- **The discriminator (`Δt_cross/τ_relax`) is a DIMENSIONLESS RATIO** — α-clean, no
  calibration carrier. τ_relax and V_yield inputs are CODATA/`m_e`-derived
  (consistency-class), used only to set the native time/voltage scales.
- **Coordinate class:** real-space (matched to the real-space 0₁ claim). A46-clean.

## §7 WHAT STAYS OPEN

- **The Ax1 topological-pinning term in the re-solidified Cosserat solid** — the
  named engine gap / corpus-claim tension (§4 FLAG). This is the load-bearing open
  item: without it, no moving-front (or temporal, or static) realization can
  produce a LASTING real-space ω-defect from a bare ω-loop. Adjudication (engine
  gap vs corpus over-claim) is for Grant/auditor (A44).
- **A stabilised soliton seed vs a bare ω-loop.** A bare loop is not a stationary
  object; a proper (2,q) stabilised soliton might be pinnable where a loop is not.
  Re-running with a stabilised seed (once the pinning question is adjudicated) is
  the natural next step. This also connects to the still-open winder-primitive gate.
- **Higher-resolution / longer-window confirmation.** The absolute persistence
  numbers are resolution-limited (N=12–16). The arm-contrast and S_min signals are
  resolution-robust; the lasting-freeze negative should be re-confirmed at N≥32 in
  the engine_sim lane before it is promoted to a corpus verdict.
- **The (2,3) phase-space winding** — explicitly OUT of scope (Guard 3); still open
  (winder-primitive gate, genesis-24).
- **m_e calibration and η magnitude** — untouched, barred (Guard 4), still open.

---

**Adjudication trail:** this doc + the frozen prereg (`7b97e76d`) + the results
JSON are the trail for a LATER promotion decision. KB/manuscript were NOT touched
(research/-only). The load-bearing item for the auditor queue is the §4 FLAG
(engine linear-elastic-solid vs corpus Ax1-topological-protection). The auditor
lands any manual/manuscript entry; this lane surfaces the empirical finding only.
