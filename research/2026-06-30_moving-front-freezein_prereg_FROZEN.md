# Moving-Front Freeze-In — FROZEN PREREG

**Date:** 2026-06-30
**Branch:** `analysis/moving-front-freezein` (off main `eaadeaf1`)
**Status:** FROZEN — SHA-pinned before any simulation. Make-or-break, framed falsification-first.
**Lane:** implementer. Adjudication trail for a LATER KB/manuscript promotion; `research/`-only now.

> **Freeze discipline:** this prereg is written and committed BEFORE the engine
> module and driver. The derived freeze-direction (§2), the pass/fail gates
> (§4), the falsifiers (§5), and the four barred controls (§6) are fixed here.
> No post-hoc gate movement (Rule 11). If the pre-registered prediction fails
> decisively, that is recorded as an honest negative (Rule 11) and retracted via
> Rule 12 — the slot is NOT refilled with a rescue hypothesis (Rule 12 / A47 v11b).

---

## §0 SECTOR / REGIME HEADER (stated before any standard-physics word)

- **MODE:** cosmological crystallization front.
- **REGIME:** a propagating yield-crossing (V through V_yield) sweeping through
  space at rate `v_front`, at/near saturation A → 1 at the front.
- **PHASE-STATE:** transitional (mid-order) — slipstream ahead of the front,
  re-solidified solid behind it.
- **SECTORS:** ε free-store; A1 dilatation (mass); the (2,3) Cosserat winding
  (real-space 0₁ defect); μ circulation (chirality); T2 transverse shear
  (latent-heat / CMB exhaust).
- **FORBIDDEN FRAMING WORD:** "Kibble-Zurek." The corpus is explicit this is
  NOT a KZ import (`manuscript/ave-kb/common/dark-wake-bemf-foc-synthesis.md:54`;
  `research/_archive/L3_electron_soliton/59_memristive_yield_crossing_derivation.md:14`).
  The native mechanism is BEMF-blocked unwinding via the diverging `L_eff` Lenz
  back-EMF near S → 0. Native language only throughout.

*(sections below filled incrementally in this same frozen doc; the SHA-pin is
the commit that lands the complete doc, before the engine/driver commits.)*

## §1 HYPOTHESIS AND THE GAP THIS CLOSES

**Hypothesis (H).** A spatially-PROPAGATING yield-crossing front, sweeping at
rate `v_front` through a region that already contains a pre-existing
topologically-nontrivial real-space ω-defect, FREEZES IN that defect behind the
front (via the BEMF-blocked-`dω/dt` mechanism) — where the *bare* c_eff²(ρ̄) EOS
crossing merely LOCKs/heals and does not persist the defect.

**The gap being closed.** The freeze-in MECHANISM is already canonical
(clm-exjfai `dark-wake-bemf-foc-synthesis.md:54`; clm-n3un96
`tau-relax-derivation.md` §4; full derivation `59_memristive_yield_crossing_derivation.md`).
The corpus names an un-built "v5 mechanism slot" — the **transverse → longitudinal
transducer AT A MOVING PHASE FRONT** — at
`research/2026-06-10_matter-as-vapor-locked-pump_framing.md:280` (§11.5, item 3,
verbatim: *"the v5 design must supply a moving phase front for the transduction
to occur"*). The freeze-in has only ever been run as:
- a TEMPORAL amplitude-ramp at a FIXED seed (genesis-v15),
- a lone photon (genesis-23/24), or
- a STATIC front-gate valve (t2-selflock).
NEVER as a moving spatial front. This build closes exactly that gap: the first
dynamical sim of a *moving* front freezing in a *pre-existing* ω-defect.

**Make-or-break framing (falsification-first).** If arm B (memristive-engine
front) also merely LOCKs/heals — i.e. the defect does NOT persist behind the
moving front the way the canonical mechanism predicts — then the *moving-front
realization* of the canonical mechanism FAILS, and we report it as a clean
negative (Rule 11). The canonical clm-exjfai claim itself would then be flagged
as validated only in the temporal/static realizations, never the moving-spatial
one it is invoked for in the cosmological-lifecycle story.

## §2 DERIVE-FIRST — THE FREEZE-DIRECTION (load-bearing physics call)

Per the mission's DERIVE-FIRST directive: the freeze-DIRECTION of the
discriminator is DERIVED by reading the `L_eff(S)` / memristive-ODE form in the
three canonical docs, NOT guessed. `τ_relax = ℓ_node/c ≈ 1.288×10⁻²¹ s`
(clm-n3un96; `ave.core.constants.TAU_RELAX_SI`, verified `1.2880886674e-21`).

### §2.1 The mechanism, read from the actual ODE

The dynamic saturation state obeys a first-order relaxation ODE
(`tau-relax-derivation.md` §3; `59_` §2; and it is ALREADY IMPLEMENTED in
`src/ave/core/k4_tlm.py:283-284` backward-Euler, opt-in `use_memristive_saturation`):

```
dS/dt = (S_eq(r(t)) − S(t)) / τ_relax ,   S_eq(r) = √(1 − r²),   r = V/V_SNAP
```

The BEMF that blocks `dω/dt` scales as the diverging bond inductance
`L_eff ∝ Z_eff = Z_0/√S → ∞` as `S → 0` (`59_` §4.3, lines 175-182;
`tau-relax-derivation.md` §4). The block on `dω/dt` is therefore active
**precisely while S is small** (deep saturation / slipstream), and it lifts as
soon as S recovers toward its equilibrium value √(1−r²) > 0 in the re-solidified
phase.

The memristive LAG is the operative content (`59_` §3, line 103, verbatim):
> *"if `dr/dt < 0` (down-crossing), `S_eq` increases faster than `S` can follow
> → `S(t) < S_eq(r(t))` during transition (S lags below equilibrium)."*

### §2.2 The APPARENT CONFLICT

Two one-liners disagree on the freeze-direction:

- **dark-wake-bemf:54 (verbatim):** *"When V(t) drops through V_yield … at a rate
  ‖dV/dt‖ such that the crossing takes ≥ τ_relax, any topologically non-trivial ω
  configuration … FREEZES … blocks dω/dt during the τ_relax window."*
  → reads as **SLOW crossing (duration ≥ τ_relax) → FREEZE.**
- **grounding-pass recommendation (as reported to this lane):** *"faster than
  τ_relax → freeze, slower → heal."* → reads as **FAST crossing → FREEZE.**

These are literally opposite. Per **flag-don't-fix**, this is surfaced, not
silently reconciled — the resolution below is derived from the ODE, and one of
the two one-liners is BACKWARDS as literally stated.

### §2.3 RESOLUTION — derived from the memristive-lag ODE (FAST → FREEZE)

Trace `dω/dt` block persistence as a function of the local crossing-window
duration `Δt_cross ≈ ℓ_front / v_front` (the time a given cell spends transiting
r: 1⁺ → below-1 as the front passes over it):

- **FAST crossing (`Δt_cross ≲ τ_relax`):** the cell is swept out of the
  slipstream faster than S can relax. By the §2.1 lag (line 103), on a fast
  down-crossing `S(t) < S_eq(r(t))` — **S stays LOW even after r has dropped and
  S_eq has recovered.** A low S means `L_eff` (hence the Lenz back-EMF) stays
  large, so the `dω/dt` block PERSISTS through and beyond the geometric crossing.
  The winding has no open channel to unwind before it is locked into the solid.
  → **FREEZE.** Corroborated by `59_` §7.1 (high-frequency limit, verbatim:
  *"Drive oscillates faster than the lattice can respond … the lattice
  effectively freezes at the time-averaged state"*).

- **SLOW crossing (`Δt_cross ≫ τ_relax`):** the cell transits quasi-statically;
  `S(t) ≈ S_eq(r(t))` at all times (the lag is negligible). As soon as r drops
  below 1, S recovers to √(1−r²) > 0, `L_eff` drops back to its ground-state
  value, and the `dω/dt` block LIFTS while the cell is still mid-transition.
  The winding has an open, low-impedance channel and unwinds gradually.
  → **HEAL.** Corroborated by `59_` §7.2 (low-frequency limit: *"S(t) ≈ S_eq(r(t))
  at all times. Full yield-and-heal per cycle"*).

**DERIVED FREEZE-DIRECTION (the pre-registered prediction):**

> **FAST crossing (`Δt_cross = ℓ_front/v_front ≲ τ_relax`, i.e. high `v_front`)
> → FREEZE. SLOW crossing (`Δt_cross ≫ τ_relax`, low `v_front`) → HEAL.**
> The discriminator is `Δt_cross / τ_relax`; the transition sits near
> `Δt_cross ≈ τ_relax`.

**The grounding-pass one-liner (fast→freeze) is CORRECT; dark-wake-bemf:54
(slow→freeze) is BACKWARDS as literally stated** — it conflates "the block is
available for a duration τ_relax" with "the crossing must span τ_relax." The
operative discriminator on `dω/dt` is that the transit be SHORT compared to the
S-relaxation recovery, so the lagged-low S keeps `L_eff` large across the whole
transit. **FLAG (flag-don't-fix, for Grant/auditor adjudication):** clm-exjfai's
prose direction at `dark-wake-bemf-foc-synthesis.md:54` appears inconsistent
with the memristive-lag mechanism it cites; this prereg pre-registers the
mechanism-derived direction (fast→freeze) and the sim adjudicates. If the sim
confirms fast→freeze, the clm-exjfai prose is a candidate for a Rule-12 dated
correction (auditor lands it; not touched here).

**NOTE on the `n_defects ∝ τ_cool⁻¹` line (`59_` §5.2 / `tau-relax` §5).**
That is a claim about DEFECT COUNT DENSITY vs cooling rate (every coherence
volume that crosses freezes ≤ 1 defect, so total count scales with crossing-window
WIDTH, and `59_`:244 even says it does *not* depend on τ_cool to leading order).
It is a SEPARATE quantity from the per-defect PERSISTENCE-vs-`v_front` discriminator
tested here. This build tests PERSISTENCE of a single seeded defect, not count
density; the `τ_cool⁻¹` count-scaling is out of scope and NOT a gate here.

## §3 THE BUILD (minimal make-or-break, 1D-collapsed 3D)

**Reuse surface (anti-rebuild, Rule 14).** The engine pieces already exist:
- `CoupledK4Cosserat` (`src/ave/topological/k4_cosserat_coupling.py:185`) with
  `step()`, `total_topological_charge()` (→ `cos.extract_crossing_count()`),
  `use_memristive_saturation=` (per-cell S(t) lag in K4, ODE at `k4_tlm.py:283`),
  and `use_impedance_boundary=` (the Γ=−1 front-clamp on ω via
  `_freeze_clamp_omega0_shared`).
- Op14 relaxation ODE `dS/dt=(S_eq−S)/τ_relax` is ALREADY IMPLEMENTED
  (`k4_tlm.py:283-289`, backward Euler). This is the piece `59_`:28 flagged as
  not-yet-implemented; it is now present per-cell — but see the NEW PIECE below.

**The NEW engine piece (what is actually missing).** Two gaps:
1. **The front-clamp reads INSTANTANEOUS S_eq, not the memristive-lagged S(t).**
   `_freeze_clamp_omega0_shared` builds Ω₀(r) from `_update_saturation_kernels`
   (instantaneous S_eq), so the `dω/dt` block has NO MEMORY — it cannot exhibit
   the lagged-low-S persistence that §2.3 identifies as the freeze mechanism.
   NEW: a memristive front-clamp whose block strength is keyed to the LAGGED
   `S(t)` (the k4 `S_field` relaxation state), so the `L_eff(S(t))` divergence
   carries the fast→freeze / slow→heal asymmetry.
2. **The front is STATIC** (t2-selflock valve). NEW: a spatial yield boundary
   `x_front(t) = x_0 + v_front·t` that sweeps, driving each cell through a
   down-crossing r: >1 → <1 in a local window `Δt_cross ≈ ℓ_front/v_front`.

**New module:** `src/ave/topological/moving_front_freezein.py` — a thin
`MovingFrontFreezeIn` orchestration layer over `CoupledK4Cosserat` that (a) sets
a moving V(x,t) yield boundary, (b) drives the memristive-lagged front-clamp,
(c) seeds a pre-existing ω-defect ahead of the front, and (d) exposes the
freeze-in detector. Marked `engine_sim`.

**Two arms (the side-by-side control — Guard 2).**
- **Arm A (bare-EOS control):** `use_memristive_saturation=False` — instantaneous
  Op14 / bare c_eff²(ρ̄) EOS crossing. Prediction: LOCK/heal, defect does NOT
  persist (the bare EOS crossing was MEASURED reversible, `cavitation-core-probe`).
- **Arm B (memristive-engine):** `use_memristive_saturation=True` + memristive-lagged
  front-clamp. Prediction: FREEZE for fast `v_front`, defect persists.

**Discriminator sweep.** Vary `v_front` so that `Δt_cross/τ_relax` spans
≈ [0.1, 10] (native units, τ_relax=1). Confirm the §2.3 direction: persistence at
fast (`Δt_cross ≲ 1`), heal at slow (`Δt_cross ≫ 1`).

**Coordinates.** Real-space ω-defect only (Guard 3). The freeze detector is the
real-space winding `extract_crossing_count()` on the ω-field (a real-space
contour integral), NOT the phase-space (V_inc,V_ref) Clifford-torus portrait.

## §4 PASS / FAIL GATES

All gates fixed here; no post-hoc movement (Rule 11).

- **G1 (TRAP-not-CREATE, Guard 1).** Under LOSSLESS pre-front evolution
  (front off, conservative step), the seeded defect must be present with
  `Q_pre ≥ 1` AND the total energy must be conserved to `|ΔH|/H ≤ 1e-2` over the
  pre-front window (no net injection sourced the winding). PASS requires the
  defect to exist WITHOUT the front's energy input. FAIL → re-entered the barred
  self-formation slot; abort and report.
- **G2 (arm-A LOCK, Guard 2).** Arm A: after the front passes, `Q_A` must
  return toward 0 (defect does NOT persist) — heal within the recording window.
  Quant: `Q_A(t_end) < Q_pre` and trending to 0.
- **G3 (arm-B FREEZE).** Arm B, FAST `v_front` (`Δt_cross ≲ τ_relax`): the defect
  must PERSIST behind the front for ≥ 100 Compton periods (canonical
  `dark-wake:54` / `59_`:639; `T_Compton ≈ 2π·τ_relax`). Quant: `Q_B` held at
  `≥ Q_pre` (integer-stable) across ≥ 100 T_Compton post-front. PARTIAL if it
  persists but < 100 T_Compton (report the achieved count honestly).
- **G4 (the two-arm contrast IS the proof).** FREEZE in B AND its ABSENCE in A,
  together. Requires G2 ∧ G3.
- **G5 (discriminator direction).** The sweep must reproduce the §2.3
  pre-registered direction: persistence↑ as `v_front`↑ (Δt_cross↓). Monotone
  freeze-fraction vs `v_front` in the mechanism-predicted sense.

**Overall PASS** = G1 ∧ G2 ∧ G3 ∧ G4 ∧ G5. Anything less is reported at its
honest partial/negative class.

## §5 FALSIFIERS

- **F1.** Arm B also merely LOCKs/heals (defect does not persist beyond
  ≤ τ_relax of crossing) → the moving-front realization FAILS; clean negative
  (Rule 11). The BEMF argument does not carry into the moving-spatial regime.
- **F2.** Arm A also FREEZES (bare EOS persists the defect) → the freeze-in is
  NOT the memristive-relaxation mechanism; the two-arm discriminator is void and
  the attribution to `L_eff(S)` back-EMF is falsified.
- **F3.** The discriminator direction is REVERSED (slow→freeze / fast→heal)
  relative to §2.3 → the §2.3 mechanism-reading is wrong; re-open the conflict
  with Grant/auditor (this would instead vindicate dark-wake:54's literal prose).
  Recorded, not rescued.
- **F4 (guard breach).** G1 fails (winding appears only under front energy input)
  → barred self-formation re-entry; the whole result is void as a freeze-in test.
- **F5.** The defect "persists" only because `extract_crossing_count` is reading
  a frozen-absorbing PML artifact or a numerically-pinned clamp, not real interior
  physics → the persistence is an artifact (Rule-10 corollary: PML cell exclusion
  + density-peak sampling checks are mandatory in the driver).

## §6 THE FOUR NON-NEGOTIABLE GUARDS (barred controls)

1. **TRAP-not-CREATE.** The ω-defect PRE-EXISTS: it is seeded as a
   topologically-nontrivial ω fluctuation BEFORE the front arrives, and its
   existence is verified under LOSSLESS (conservative, front-off) evolution with
   energy conserved (G1). The front TRAPS it; it does NOT source it. A winding
   that appears only under the front's energy INPUT re-enters the barred
   self-formation slot ("pumps H at dt→0",
   `research/2026-06-24_engine-phase-space-winding_prereg.md:11-12`, verbatim
   *"A winding that appears only under energy injection is an ARTIFACT, not a
   charge"*). BARRED: precursor/convergence ICs; front-sourced winding.

2. **BEAT LOCK-not-FLASH (the side-by-side control).** The bare c_eff²(ρ̄) EOS
   crossing was MEASURED reversible — LOCK, not FLASH. The freeze-in
   irreversibility is NOT in the bare EOS; it requires the memristive relaxation
   ODE (the diverging `L_eff` → Lenz back-EMF blocking `dω/dt`). Two arms: (A)
   bare-EOS front must LOCK/heal; (B) memristive-engine front must FREEZE. The
   FREEZE in B and its ABSENCE in A together are the proof. If B also just LOCKs
   → moving-front realization FAILS (F1), reported honestly.

3. **COORDINATE DISCIPLINE (phase-space-coordinate-check).** The electron is a
   REAL-SPACE 0₁ unknot; "(2,3)" is the PHASE-SPACE winding portrait
   (`manuscript/ave-kb/CLAUDE.md:22`, def-kn0t01). This build tests persistence
   of a REAL-SPACE ω-defect ONLY — the detector is a real-space contour winding
   on the ω-field. BARRED: any claim this delivers the (2,3) phase-space winding
   — that is a SEPARATE, still-open "winder-primitive" gate (genesis-24
   localized the residual obstruction there,
   `research/2026-06-09_genesis-24-saturated-seed_result.md:333,388`). Scope is
   real-space defect persistence, full stop.

4. **NO OVER-CLAIM.** BARRED: any `m_e` claim (it is the imported calibration
   input; latent-heat=m_e c² is hypothesis-class with an adverse LOCK-not-FLASH
   prior — aspirational only, `matter-as-vapor-locked-pump_framing.md:198`).
   BARRED: any η-magnitude route (over-determination,
   `freeze-handedness-survey_note.md:47`, magnitude-link CONTRADICTED-soft,
   do-not-build). Chirality-at-freeze value is fiat-IC (relocated to J_parent),
   NOT derived — the sim fixes it by IC and reads persistence, not its magnitude.

## §7 CLASSIFICATION (consistency-vs-emergence, phase-space-coordinate-check)

- **Class of the freeze-mechanism itself:** CONSISTENCY-class. The `dS/dt`
  relaxation ODE, `S_eq=√(1−r²)`, `L_eff=Z_0/√S`, and Lenz's law are
  canonical/axiom-derived (Ax1+Ax3+Ax4+Op14); this build is a first DYNAMICAL
  DEMONSTRATION that the canonical mechanism behaves as derived when realized as
  a moving front. A confirmed FREEZE is a manifestation/consistency result — the
  engine exhibiting the axiom-forced behavior — NOT an emergence-class discovery
  of a new number.
- **`τ_relax` and V_yield inputs:** `τ_relax=ℓ_node/c` with `ℓ_node=ℏ/(m_e c)`,
  and `V_yield=√α·V_snap` — both CODATA/`m_e`-derived via the canonical chain
  (`ave.core.constants`). Any comparison to those targets is CONSISTENCY-class,
  not emergence (A47 SI-substitution caveat). The discriminator itself
  (`Δt_cross/τ_relax`) is a DIMENSIONLESS RATIO, so it divides out the calibration
  carrier — this is the correct, α-clean read (per the "chord must be a
  dimensionless ratio" lesson).
- **Coordinate class:** real-space (Cartesian-with-FCC-filter ω-field contour
  winding). Matches the claim coordinate (real-space 0₁ persistence). NOT
  compared against any phase-space φ² prediction (A46-clean).
- **What this build does NOT establish:** emergence of `m_e`, the (2,3)
  phase-space winding, or any η magnitude. Those stay OPEN.

## §8 CANONICAL SOURCES (verify-before-cite, all verified 2026-06-30)

- Mechanism (freeze, "≥ τ_relax" prose): `manuscript/ave-kb/common/dark-wake-bemf-foc-synthesis.md:54`
  (clm-exjfai). **FLAGGED §2.3: direction backwards vs mechanism.**
- τ_relax derivation + relaxation ODE + §4 BEMF freeze + §5 count-scaling:
  `manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/tau-relax-derivation.md`
  (clm-n3un96).
- Full derivation (§3 lag line 103, §4 heal branch, §5 density, §7 freq
  regimes): `research/_archive/L3_electron_soliton/59_memristive_yield_crossing_derivation.md`.
- v5 moving-front gap-slot: `research/2026-06-10_matter-as-vapor-locked-pump_framing.md:280`.
- Barred self-formation ("pumps H at dt→0"): `research/2026-06-24_engine-phase-space-winding_prereg.md:11-12`.
- m_e aspirational caveat: `research/2026-06-10_matter-as-vapor-locked-pump_framing.md:198`.
- η over-determination bar: `research/2026-06-10_freeze-handedness-survey_note.md:47`.
- (2,3) = phase-space vs real-space 0₁: `manuscript/ave-kb/CLAUDE.md:22` (def-kn0t01).
- winder-primitive still-open: `research/2026-06-09_genesis-24-saturated-seed_result.md:333,388`.
- Relaxation ODE implemented: `src/ave/core/k4_tlm.py:283-289`.
- Coupled engine + detectors: `src/ave/topological/k4_cosserat_coupling.py:185,861,948`.
- ODE / engine "not-yet-implemented" flag (now the relaxation ODE IS in
  `k4_tlm.py:283`; the moving-front + memristive-lagged clamp is the true
  remaining gap): `59_`:28 (verbatim *"no engine implementation … Op14
  relaxation-ODE extension — §10 scopes that work; it's deferred"*).
  NOTE (verify-before-cite): the mission-brief's `three-lane-genesis-context.md:129`
  is NOT present in this worktree (grep-zero) — dropped, not cited.
- Constants: `ave.core.constants` (TAU_RELAX_SI, L_NODE, V_SNAP, V_YIELD, ALPHA).
