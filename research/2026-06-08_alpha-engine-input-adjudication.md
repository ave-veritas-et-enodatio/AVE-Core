# Adjudication: α in engine dynamics vs snap-genesis instrumentation

**Date:** 2026-06-08  
**Prereg:** `research/2026-06-08_alpha-engine-input-prereg.md` (FROZEN)  
**Snap prereg:** `research/2026-06-08_electron-genesis-snap-prereg.md` (FROZEN)  
**Context:** electron-genesis / calibration-crux thread (observer bridge → native Γ ceiling → propagation → re-seed handoff)  
**Question:** Should we **remove α from the engine** before proceeding with snap genesis?

## Verdict: **NO wholesale removal — isolate α-free snap instrumentation instead**

| Category | Location | Action |
|----------|----------|--------|
| **KEEP (structural)** | `constants.py`: `V_YIELD = √α · V_SNAP` | Do not remove — Axiom-4 yield identity (INVARIANT-C1), not a tunable fit |
| **KEEP (structural)** | `vacuum_engine.py`: `_V_YIELD_FRAC = √α`, `amplitude_convention="V_YIELD"` | Regime-map / unit conversion only |
| **KEEP (structural)** | `k4_tlm.py`, `regime_map.py`, `saturation.py`, FDTD defaults | Comments + yield thresholds reference √α as operating-point geometry |
| **ISOLATE (snap tests)** | `PairNucleationGate.delta_lock_fraction` default `= ALPHA` | **Do not use default in forward snap drivers** — pass explicit geometry-derived lock width |
| **ISOLATE (snap tests)** | `PairNucleationGate` Beltrami injection path | Optional for Phase-5 pair nucleation; **snap genesis uses full re-seed**, not gate injection |
| **KEEP (drivers)** | `ALPHA_COLD` in scoring only | `alpha_used_as_input: false` — comparison post-hoc |

## Rationale

### 1. √α in `V_YIELD` is not “dialing α into dynamics”

`V_YIELD = √α · V_SNAP` is the **substrate yield voltage** from Axiom-4 self-saturation at the magic-angle operating point. It defines where Regime II begins relative to `V_SNAP`. Removing it would:

- Break the three-regime map (`k4_tlm.py` comments, `regime_map.py` benchmarks)
- Confuse `V_SNAP` vs `V_YIELD` amplitude conventions across 40+ drivers
- Contradict structural-closure framing (α derived from geometry at yield, not injected as a free knob)

The calibration crux is **not** that √α appears in yield definition. It is:

1. **Rest vs wall:** sub-yield `A² ≈ 0.23` propagates; wall `A² → 1` pins with TIR (`native_electron_propagation`, `native_k4_gamma_ceiling`)
2. **Projection vs native lane:** scalar projection Γ ≈ −0.35..−0.45 at wall; native coupled Γ ≈ −0.99 (`projection_native_gamma_gate`)

### 2. The α-as-input risk is `PairNucleationGate`, not `V_YIELD`

`PairNucleationGate` C2 autoresonant lock uses:

```
δ_lock = δ_lock_fraction · ω_drive   (default δ_lock_fraction = α)
```

That imports **CODATA α** as a **dynamics tolerance** for pair nucleation. Corpus doc 54_ §7 / doc 27_ justify `Q = 1/α` at **Γ = −1 TIR** — but forward snap tests must not **assume** α to **achieve** TIR.

**Forward-test discipline:**

- Compute `δ_lock` from **measured** local leak: `δ_lock = ω_drive · max(ε_local, ε_floor)` where `ε_local = 1 − Γ²` at the propagation core (substrate-native Q proxy)
- Or explicit override `delta_lock_fraction=0.02` (documented, not `ALPHA`)
- Never register `PairNucleationGate` with default constructor in alpha-free snap drivers

### 3. Session drivers are already α-free

All 2026-06-07/08 vol_1 genesis drivers set `alpha_used_as_input: false`. `ALPHA_COLD` appears only in:

- Post-hoc `|ε − α|` scoring
- Print labels / adjudication tables

No driver fits dynamics to α.

### 4. Snap genesis does not require engine surgery first

Best handoff so far (`native_electron_reseed_handoff`):

- Propagate sub-yield (`amp=0.48`) with longitudinal drive
- **Full replace** at motion site with `trap_amp ≥ 1.5`
- Outcome: `TRAP_AT_MOTION_SITE_PINNED_WITH_TIR` (Γ_post ≈ −0.994, ε ≈ 0.013)

This path uses native `VacuumEngine3D` with `axiom_4_enabled=True` (hence inherits √α yield) but **no α in snap trigger logic**. Engine surgery is unnecessary before automating the snap criterion.

## What would be wrong to do

| Proposed change | Why reject |
|-----------------|------------|
| Remove `sqrt(ALPHA)` from `V_YIELD` | Breaks substrate regime identity; conflates “no α input” with “no α in definitions” |
| Hard-code `V_YIELD` numeric without √α derivation | Hides structural provenance; fails canonical-source discipline |
| Use `PairNucleationGate()` default in snap driver | Smuggles α into lock tolerance before TIR is demonstrated |
| Remove α from `constants.py` entirely | Breaks observable battery, SPICE lib, regime map, 100+ corpus references |

## Recommended snap-driver contract (α-free instrumentation)

1. **Dynamics:** `VacuumEngine3D` native lane, `amplitude_convention="V_SNAP"`, `axiom_4_enabled=True` (inherits √α yield — acceptable)
2. **No** `PairNucleationGate` with default `delta_lock_fraction`
3. **Snap trigger:** geometry-only — motion + local strain / measured-ε lock + full `seed_sech_v_inc` replace at `trap_amp ≥ 1.5`
4. **Scoring:** `bond_gamma_min` on native `z_local_total`; compare `ε = 1 − Γ²` to `ALPHA_COLD` post-hoc only
5. **Explicit JSON flag:** `alpha_used_as_input: false`, `delta_lock_source: "measured_eps" | "explicit_fraction"`

## Follow-up (optional engine hygiene, not blocking snap)

- **Document** in `PairNucleationGate` docstring: default `ALPHA` is corpus-derived Q at TIR; forward tests should pass explicit override
- **Consider** changing default to `None` requiring explicit choice — **breaking change**; defer until Phase-5 gate audit; tests in `test_phase5_pair_nucleation_gate.py` lock current default
- **Bridge fix:** projection readout from native `z_local_total` (separate workstream)

## Proceed order

1. ✅ This adjudication  
2. ✅ **Snap driver** (`electron_genesis_snap.py`) — α-free triggers, inherit √α yield only  
3. Optional: ε proxy study (ε ≈ 0.013 vs α ≈ 0.0073 at native TIR)  
4. Commit + PR when Grant requests

## Snap driver results (2026-06-08)

**Driver:** `electron_genesis_snap.py`  
**JSON:** `src/scripts/vol_1_foundations/_output/electron_genesis_snap_results.json`  
**GIF:** `assets/sim_outputs/electron_genesis_snap.gif` (hybrid mode)

| Mode | Trigger | Verdict | Γ_post | Pre Δx |
|------|---------|---------|--------|--------|
| position | position @ step 16 | **SNAP_TRAP_PINNED_WITH_TIR (A)** | −0.994 | +8.1 |
| autoresonant | never fired | SNAP_NEVER_FIRED (C) | — | +10.0 |
| hybrid | position @ step 16 | **SNAP_TRAP_PINNED_WITH_TIR (A)** | −0.994 | +8.1 |

**Read:** Position/hybrid replicate `native_electron_reseed_handoff` without manual trigger constant in code path (same `trigger_x=14` criterion). Pure measured-ε autoresonant snap **does not fire** at sub-yield propagation — Meissner `A²_μ ≥ 0.85` never reached before motion completes. Confirms snap is a **discrete wall replace**, not gradual Duffing climb on the moving sub-yield packet.

**Engine α removal was correctly deferred:** identical TIR outcome with inherited √α yield only; no `PairNucleationGate` default used.
