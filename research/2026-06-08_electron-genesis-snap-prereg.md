# Prereg: alpha-free electron snap genesis (automated wall replace)

**Status:** FROZEN PREREG (retroactive — driver run 2026-06-08).  
**Parent:** `2026-06-08_native-electron-propagation-adjudication.md`, `2026-06-08_alpha-engine-input-prereg.md`  
**Driver:** `src/scripts/vol_1_foundations/electron_genesis_snap.py`  
**Corpus-grep:** ave-corpus-grep session 2026-06-08 (snap = discrete replace vs Duffing climb)

---

## §0 Question

Can electron genesis be **automated** as: propagate sub-yield defect → **geometry-triggered full wall replace** → TIR trap at motion site — without manual `trigger_x` constant and without importing α into snap logic?

Does **autoresonant** snap (Meissner + measured-ε lock) fire on the moving sub-yield packet, or is genesis inherently a **discrete** event?

---

## §1 Physical picture

1. **Amp 0.48** (rest scale): longitudinal drive moves centroid; Γ ≈ matched (−0.013); no TIR.
2. **Amp ≥ 1.5** (wall scale): static full `seed_sech_v_inc` → Γ ≈ −0.99; core **pins** (motion_stability).
3. **Additive ramp** on moving centroid fails — does not build wall (`native_electron_propagation_ramp`, `HANDOFF_INCONCLUSIVE`).
4. **Full replace** at motion site succeeds (`native_electron_reseed_handoff`, `TRAP_AT_MOTION_SITE_PINNED_WITH_TIR`).
5. Corpus pair-production path: Duffing autoresonant gate is **rupture drive** (Regime III→IV), not bound-state finder on sub-yield packet (`67_lc_coupling_reciprocity_audit.md`).

---

## §2 Corpus state (grep)

| Topic | State | Key prior work |
|-------|-------|----------------|
| Propagate sub-yield | **Closed** | `native_electron_propagation_results.json` amp=0.48 |
| Ramp handoff | **Failed** | `native-electron-propagation-adjudication.md` §Ramp |
| Full re-seed handoff | **Closed** | `native_electron_reseed_handoff.py`, trap≥1.5 |
| Autoresonant as snap | **Contradicted** for this path | doc 54_ / Vol 9 Ch 8 = pair rupture; L3 audit: drive not finder |
| `seed_sech_v_inc` overwrite | **Closed** | `native_k4_gamma_ceiling.py:77-86` |

---

## §3 Predictions

**Primary (Outcome A):** **position** or **hybrid** mode replicates reseed handoff — `SNAP_TRAP_PINNED_WITH_TIR`, Γ_post ≤ −0.99, pre Δx > 6, post pinned.

**Alternative (Outcome B):** **autoresonant** mode fires before position fallback — Meissner `A²_μ ≥ 0.85` + measured-ε lock on moving packet → snap without `trigger_x`.

**Null (Outcome C):** **autoresonant** never fires; motion completes at matched Γ without reaching Meissner on packet → genesis requires **discrete wall replace**, not gradual Duffing climb.

**Falsifier:** If autoresonant mode reaches TIR **without** full replace (only drive) — would contradict discrete-snap picture and elevate PairNucleationGate path.

---

## §4 Protocol

Engine: `VacuumEngine3D`, `N=32`, `use_asymmetric_saturation=True`, `axiom_4_enabled=True`, `alpha_used_as_input: false`.

| Parameter | Value |
|-----------|-------|
| `AMP_START` | 0.48 × V_SNAP |
| `TRAP_AMP` | 1.5 × V_SNAP |
| `V_DRIVE_PRE` | 0.04 |
| `SAT_FRAC` | 0.85 (autoresonant Meissner gate) |
| `delta_lock` | measured `ω · max(1−Γ², 0.01)` |
| Modes | `position`, `autoresonant`, `hybrid` |

Snap action: full `seed_sech_v_inc` + `initialize_electron_unknot_sector` at core (not additive bump).

Scoring: `bond_gamma_min` on native `z_local_field`; compare ε to `ALPHA_COLD` post-hoc only.

---

## §5 Outcomes

| Outcome | Criterion |
|---------|-----------|
| A | position/hybrid: TIR + pinned + prior motion |
| B | autoresonant fires alone with TIR |
| C | autoresonant never fires; hybrid falls back to position |
| D | Snap fires but no TIR |
| E | Snap never fires (all modes) |

---

## §6 Result

```bash
MPLCONFIGDIR=/tmp/mpl PYTHONPATH=src python src/scripts/vol_1_foundations/electron_genesis_snap.py
```

**JSON:** `src/scripts/vol_1_foundations/_output/electron_genesis_snap_results.json`  
**GIF:** `assets/sim_outputs/electron_genesis_snap.gif` (hybrid)

## §7 Adjudication

| Mode | Trigger | Verdict | Γ_post | Pre Δx | Post Δx |
|------|---------|---------|--------|--------|---------|
| position | position @ step 16 | **SNAP_TRAP_PINNED_WITH_TIR (A)** | −0.994 | +8.1 | ~0 |
| hybrid | position @ step 16 | **SNAP_TRAP_PINNED_WITH_TIR (A)** | −0.994 | +8.1 | ~0 |
| autoresonant | never fired | **SNAP_NEVER_FIRED (C)** | — | +10.0 | — |

**Verdict: Outcome A + C (primary + null for autoresonant-only)**

- Automated snap **works** via position/hybrid (replicates manual reseed).
- Pure measured-ε autoresonant snap **does not fire** — `A²_μ` never reaches 0.85 on moving sub-yield packet before motion completes.
- Confirms genesis = **discrete wall replace at motion site**, not gradual Duffing/autoresonant climb on propagating packet.

**ε readout:** `|ε − α| ≈ 0.0053` (~1.7× α) — same as static wall seed; not exact Theorem 3.1′ match.

**Next levers (not preregistered here):**

- Lower `SAT_FRAC` or co-moving `AutoresonantCWSource` to test Outcome B
- Bridge fix: native `z_local_total` into projection readout
- ε proxy: is `1−Γ²` correct dynamic leak measure at TIR?
