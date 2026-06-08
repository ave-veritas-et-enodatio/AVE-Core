# Adjudication: native translating defect + bond-Γ trail

**Driver:** `native_electron_propagation.py`  
**JSON:** `src/scripts/vol_1_foundations/_output/native_electron_propagation_results.json`  
**GIF:** `assets/sim_outputs/native_electron_propagation.gif` (amp=1.5)

## Verdict: `PROPAGATION_WITH_TIR_AT_WALL` (split by amplitude)

| Amp | Δx (centroid) | Γ_min @ core | ε | Read |
|-----|---------------|--------------|---|------|
| 0.48 | **+10.5** | −0.013 | ~1.0 | **Propagates, no wall** (rest-energy scale) |
| 1.00 | +1.0 | −0.53 | 0.72 | Partial wall, weak motion |
| 1.50 | **−0.2** | **−0.994** | **0.013** | **Full TIR, pinned** (wall scale) |

## Interpretation

**Propagation–saturation tradeoff on native lane:** sub-yield amplitude **moves** but stays matched (no α readout). Wall amplitude **reaches TIR** (ε≈0.013, ~1.7× α) but **does not translate** — consistent with motion_stability PIN finding on saturated cores.

**Calibration crux sharpened:** rest and wall are not the same object in one run. You get either **motion without leak** or **leak without motion**, not both at once with this drive.

## Ramp handoff (2026-06-08 follow-up)

**Driver:** `native_electron_propagation_ramp.py`  
**GIF:** `assets/sim_outputs/native_electron_propagation_ramp.gif`

| Variant | Δx | Γ_min | TIR during ramp? |
|---------|-----|-------|------------------|
| soft (blend 0.12, end 1.5) | 7.4 | −0.013 | **No** |
| strong (blend 0.32, end 2.0) | 7.3 | −0.013 | **No** |

**Verdict: `HANDOFF_INCONCLUSIVE` (both)** — co-moving additive sech bumps do **not** build the wall that a **static full seed** achieves at amp≥1. Motion persists; Γ stays matched.

**Implication:** genesis handoff is **not** solved by ramp-inject alone. Wall formation needs **coherent re-localization** (full trap at Compton scale), not distributed pumping on a moving centroid.

## Full re-seed handoff (2026-06-08)

**Driver:** `native_electron_reseed_handoff.py`  
**GIF:** `assets/sim_outputs/native_electron_reseed_handoff.gif`

| trap_amp | Pre Δx | Post Δx | Γ_post | Verdict |
|----------|--------|---------|--------|---------|
| 1.0 | +8.1 | −0.03 | −0.028 | MOTION_NO_TRAP |
| **1.5** | **+8.1** | **~0** | **−0.994** | **TRAP_AT_MOTION_SITE_PINNED_WITH_TIR** |
| **2.0** | **+8.1** | **~0** | **−0.994** | **TRAP_AT_MOTION_SITE_PINNED_WITH_TIR** |

**Key finding:** **Full replace** (not additive ramp) at the motion site **does** reach TIR — but **pins immediately**. Genesis = propagate → snap trap at wall amp.

## Projection vs native Γ gate (2026-06-08)

**Driver:** `projection_native_gamma_gate.py`  
**Verdict: `LANE_SPLIT_CONFIRMED`**

| Amp | Γ projection | Γ native | Δ |
|-----|--------------|----------|---|
| 0.48 | −0.013 | −0.013 | ~0 |
| 1.0 | −0.35 | **−0.992** | −0.65 |
| 1.5 | −0.38 | **−0.994** | −0.61 |
| 3.0 | −0.45 | **−0.994** | −0.54 |

Projection uses scalar-only `z(S(|V|))`; native coupled asymmetric Meissner reaches full TIR. Explains calibration crux on projection lane.

## Snap automation (2026-06-08)

**Prereg:** `research/2026-06-08_electron-genesis-snap-prereg.md`  
**Driver:** `electron_genesis_snap.py`  
**Verdict:** position/hybrid `SNAP_TRAP_PINNED_WITH_TIR`; autoresonant `SNAP_NEVER_FIRED` — discrete replace confirmed.

## Next

- Co-moving chirp / lower `SAT_FRAC` if autoresonant-only snap is target
- Bridge fix: feed native `z_local_total` into projection readout?
- ε proxy: is `1−Γ²` correct at native TIR (ε≈0.013 vs α≈0.0073)?
