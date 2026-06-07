# Electron genesis Phase 2 — the moving bulk lattice (PREREG, FROZEN)

**Date:** 2026-06-06
**Branch:** `analysis/2026-06-06-genesis-phase2-moving-bulk` (off `origin/main` `16b6b6b5`)
**Status:** PREREG FROZEN — **GATED on Phase-1** (the at-rest two-colliding pair must form first; `2026-06-06_electron-genesis-drop-prereg.md`). Session: orchestration (Grant in-session).
**Origin:** Grant 2026-06-06 — *"make sure the CMB / mutual lattice inductance, bulk effects, all the kinematics δ(ω) of the lattice and its motion itself"* are in the genesis. The electron condenses inside a **moving, mutually-inductive, bulk substrate**, not a static box.

---

## §0 The pivot — the dark wake IS the inertia, and it's a motion response

Confirmed in-engine (`vacuum_engine.py:1458-1487`): the **`DarkWakeObserver`** measures the `τ_zx` longitudinal-shear **back-EMF** behind a moving soliton, and **`M_inertial ≡ L_drag`** — *the mutual-inductance drag is the soliton's inertia (mass).* So a soliton's wake = its mutual inductance = its mass — and a back-EMF is a **motion** response: **at rest there is no wake, no drag, no inertia to entrain.** That is "the electron can't be entrained without motion" made mechanical, and it's likely why the at-rest plant (V0) and the at-rest Phase-1 pair won't lock — *the entraining inductance never energizes.*

**Open goal (prove-or-disprove):** does putting the genesis pair **in motion relative to the bulk** energize the dark-wake (its inertial mutual inductance) → **entrain and STABILIZE** the pair where the at-rest one decayed → and reproduce the canonical kinematics (`δω`, `ω_C` shift, `ν_kin`/`δ_strain`)?

---

## §1 Canonical anchors (`ave-canonical-leaf-pull`)

- **Dark wake = mutual-inductance back-EMF = inertia** (`M_inertial ≡ L_drag`): `vacuum_engine.py:1458-1487`, `DarkWakeObserver`. Measured, not new.
- **`ν_kin`** kinematic mutual inductance (dark-sector / galactic rotation): `vol3/cosmology/ch05-dark-sector/`. **`κ_entrain`** drag-along (real-power, `ρ_matter/ρ_bulk`): `sagnac-rlve.md`. **`Ω_freeze`** cosmic chirality / CMB frame. **`δ_strain`** thermal α-vs-T. **`Op14`** local clock `ω_local=ω_global√(1−A²)`, **`Op16`** wave speed.
- **Scale caveat:** these are canonical at the **galactic/cosmic** scale; the base `VacuumEngine3D` is **at-rest** (no bulk drift). The dark-wake (the local mutual inductance) IS in the engine; the **bulk motion that energizes it is not** (for the cosmic embedding).

---

## §2 Two layers (cheap test first, then the cosmic embedding)

### Phase 2a — the entrainment test (NO engine change; uses the existing DarkWakeObserver)
Give the genesis pair **net momentum** (collide the two photons with unequal momenta, or boost the seed) so the pair **moves through the lattice** → energizes the dark-wake. **No bulk-drift engine work needed** — relative motion is relative motion; the back-EMF (`DarkWakeObserver`) switches on. Scan pair-velocity `0` (Phase-1 control) → finite.
- **HEADLINE check:** does the **moving** pair **stabilize** (ring forever, sub-V_yield, (2,3) intact) where the **at-rest** Phase-1 pair **decayed**? The at-rest-vs-moving contrast IS the demonstration.
- **Dark-wake drag:** `DarkWakeObserver` `τ_zx` back-EMF — does it scale with velocity, and equal the inertial `L_drag` (`M_inertial ≡ L_drag`)?

### Phase 2b — the cosmic embedding (engine addition: a bulk drift)
Add a **bulk drift velocity** to the lattice (the substrate moving at the CMB-frame `v ~ 10⁻³c` along the `Ω_freeze` axis) — a background advection / Galilean-boost on the K4-TLM (**KEEP-BOTH:** at-rest stays default). Then:
- **`δω` kinematics:** does `ω_C` (the ring) shift with the bulk velocity (`Op14` clock × the bulk Doppler)? Match the canonical `δω`.
- **`ν_kin` / `κ_entrain` match:** does the entrainment drag reproduce the canonical kinematic mutual inductance / drag-along?
- **`δ_strain`** at `T_CMB` if the thermal bath is included (the α-vs-T sign).

---

## §3 The check battery (forward reads, no fit)

1. **Entrainment-stabilization (HEADLINE):** moving pair rings/stays sub-V_yield where at-rest decayed? (the "can't entrain without motion" test).
2. **Dark-wake drag = inertia:** `DarkWakeObserver` `τ_zx` back-EMF vs velocity; `L_drag ≡ M_inertial`.
3. **`δω` / `ω_C` shift** with bulk velocity (Op14 + Doppler).
4. **`ν_kin`/`κ_entrain`** drag matches canonical.
5. Carry forward the Phase-1 gate (sub-V_yield ring / `ω_C` / `ℓ_node` / (2,3) / charge-conservation) — does the moving-bulk genesis still pass it (better)?

---

## §4 Honest outcomes (pre-committed)

- **(I)** motion **entrains + stabilizes** the pair (at-rest decays / moving rings) + kinematics match `ν_kin`/`δω` → **the electron is a drop that must move in the stream to hold together** (vindicates the dark-wake-is-inertia picture).
- **(II)** motion does NOT stabilize (decays regardless) → entrainment isn't the stabilizer; the instability is elsewhere (revisit the seed/structure).
- **(III)** Phase-2b engine drift can't be cleanly added / the dark-wake doesn't energize as `L_drag` → engine-capability finding (Phase 2a still stands on the moving-pair test).

`ave-evidence-framing`: report whichever honestly; (II)/(III) are valid. The at-rest-vs-moving contrast keeps it falsifiable.

---

## §5 Discipline + build plan

`substrate-native-check` (CP1 wave-not-min; the dark-wake IS the substrate's mutual inductance; CP5 `ω_local`×Doppler; CP6 reactance pair) · `ave-canonical-leaf-pull` (the `ν_kin`/`κ_entrain`/`Ω_freeze`/`δ_strain`/Op14-16 kinematic stack) · `phase-space-coordinate-check` · `consistency-vs-emergence` (kinematics `δω`/`ν_kin` = consistency; entrainment-stabilization = emergence) · `ave-canonical-source` (`ν_kin`, `Ω_freeze` velocity, `V_yield`, `ω_C` from `ave.core.constants`) · `ave-driver-script-honesty` · `ave-evidence-framing`.

**Build:** (1) Phase 2a — moving-pair genesis + `DarkWakeObserver` + the stabilization/drag checks (no engine change); (2) the at-rest-vs-moving contrast; (3) Phase 2b — the bulk-drift engine addition (KEEP-BOTH) + the `δω`/`ν_kin` cosmic checks. **Deliverable:** `research/2026-06-06_electron-genesis-phase2-result.md` + driver + (if 2b) the bulk-drift engine code. Reviewed PR; no merge. **Do NOT start until Phase-1 reports** (the at-rest pair is the baseline for the contrast).
