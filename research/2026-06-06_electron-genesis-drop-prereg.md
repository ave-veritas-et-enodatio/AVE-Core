# Electron genesis — "a drop in water" (PREREG, FROZEN)

**Date:** 2026-06-06
**Branch:** `analysis/2026-06-06-electron-genesis-drop` (off `origin/main` `16b6b6b5`; worktree `AVE-Core-genesis-wt`)
**Status:** PREREG FROZEN — implementor build pending. Session: orchestration (Grant in-session). The capstone — every piece built this session (VacuumEngine3D, the coordinate-correct (2,3) extractor, the observable battery, the V_yield lens) working in one frame.
**Origin:** Grant 2026-06-06. Phase 0.5 (II) showed the *imposed* (2,3) can't be the electron — it's static, all-C (`Φ_link=0`, no ring), and 3–15× over `V_yield` (lossy). Grant: *"like a drop in water"* — the electron must **pinch off from a moving wave and ring**, not be planted. This is the `substrate-native-check` CP8 emergence test with a quantitative drop-physics gate.

---

## §0 Open goal + the CP8 framing

**Open goal (prove-or-disprove):** does the engine **autonomously host electron genesis** — a moving photon self-trapping (pinching off) into a **sub-V_yield ringing droplet of vacuum** that assembles the (2,3)? This is `substrate-native-check` **Checkpoint 8**: seed the **generative precursor** (the photon), NOT the finished (2,3); let the dynamics build it; each non-hostable layer is a structural-capability finding (not a failure).

**"A drop in water" — the physical mapping** (Grant 2026-06-06):

| water drop | electron genesis | grounded |
|---|---|---|
| surface tension | saturation kernel / the `A→1` `|Γ|=1` wall (the substrate "skin") | Ax 4; primer "pinch-off at A=1" (`:230`) |
| pinch-off (Rayleigh–Plateau) | the self-trap (moving wave drives `A→1`, pinches off) | CP8 self-trap, `2026-06-04_full-electron-transverse-selftrap-result.md` |
| ringing (surface-tension vs inertia) | the C↔L slosh (capacitance vs inductance) — the lossless reactive cycle | Ax 3 "rings forever"; bond-pair LC tank |
| stable sub-surface core, thin skin, **in motion** | sub-V_yield ringing core + thin `A→1` skin, from a **moving** photon | Phase 0.5 V_yield lens |

The electron is **vacuum that closed on itself** — a self-bound droplet of substrate within the substrate (mass-closure).

---

## §1 Canonical anchors (`ave-prereg` + `ave-canonical-leaf-pull`)

- **Self-trap is CP8-confirmed hostable** (photon → localization/mass, beat matched baseline 0.580 vs 0.389): `2026-06-04_full-electron-transverse-selftrap-result.md`. The (2,3)-winding layer is the OPEN question (needs discrete K4+Cosserat, not continuum FDTD).
- **The target layer structure** (what the (2,3) should self-assemble into — `electron-unknot-cosserat-seeder.md:57`): Layer 1 mass → Layer 2 spin/n̂ → **Layer 3 (2,3) winding** at the **bond-pair LC tank** (2 windings d-axis, 3 q-axis). NB: the seeder *plants* these; genesis must **grow** them (CP8) — the layers are the *target*, not the seed.
- **The ring frequency + size** (`mass-closure-theorem.md:89`): `m_e c² = (ℏ/c)·ℓ_node/c²` → the **unknot circumference = reduced Compton wavelength = ℓ_node**, and the ring is the bond-pair LC resonance `ω_C = c/ℓ_node`. These are the drop's Rayleigh-frequency + minimum-size, made canonical.
- **Engine:** `VacuumEngine3D` (K4-TLM + Cosserat) — the ONLY engine with the (2,3) carrier (the C↔L fibre "3" + Cosserat-ω "2"); continuum `fdtd_3d.py` has no (2,3) carrier (per the 2026-06-04 arc).

---

## §2 Design (CP8-correct)

1. **Seed = a MOVING transverse photon wavepacket** (≈c propagation; NOT static, NOT the finished (2,3)). Driven hard enough to drive `A→1` locally (hit saturation → pinch off). Per Grant Q2 (moving) + Q3 (hits saturation).
2. **Matched-distribution baseline** (CP8 step 2): same amplitude statistics, no coherence/topology. Genesis must out-perform it **because of structure**, not amplitude (guards the phase3f Factor-2 confound).
3. **Reuse** the 2026-06-04 self-trap driver scaffold + the observable battery channels + the coordinate-correct extractor.

---

## §3 The drop-physics quantitative gate (the headline pass/fail)

Measured live through the formation (forward reads, no fit):

1. **Sub-V_yield ring** — does the self-trapped **core drop below `V_yield`** and ring? Per-phasor `V/V_yield` trace for `V_inc`, `V_ref`, `Φ_link` (`A_yield = V_yield/V_snap ≈ 0.085`, `A²_yield ≈ α`). A drop that stays over-yield is lossy → not the electron.
2. **Rings at `ω_C`** — measure the slosh self-frequency (zero-crossings of `V_inc`↔`Φ_link`); does it converge to `ω_C = c/ℓ_node` (the substrate's "Rayleigh frequency")? (consistency-class check.)
3. **Size ≈ `ℓ_node`** — the soliton's spatial extent vs the reduced Compton wavelength (the minimum-droplet check).
4. **(2,3) assembles** — does the extractor see `w1→2, w2→3` emerge (the drop's internal circulation)? (the CP8 emergence layer.)

---

## §4 The animation (real + phase side-by-side)

- **Real-space panel:** `A²`/envelope over the K4 lattice — the photon propagating, hitting saturation, pinching off into a localized breathing droplet.
- **Phase-space panel:** the `(V_inc, V_ref)` phasor winding onto the Clifford torus — the (2,3) topology closing.
- **Overlaid channels animated through the genesis:** per-phasor `V/V_yield`, the measured ring-frequency vs `ω_C`, `Γ`→`|Γ|=1` (skin forming), the (2,3) confidence. The birth narrated in every coordinate at once; dark aesthetic per driver convention.

---

## §5 Honest outcomes (pre-committed)

- **(I) full genesis** — photon → sub-V_yield ringing droplet @ `ω_C`, `ℓ_node`-sized, (2,3) assembles → **electron born from light** (the capstone).
- **(II) mass-only** — droplet self-binds (mass) but the (2,3) does NOT assemble → structural-capability finding (engine carries the drop, not the winding self-assembly; localize which carrier).
- **(III) no-drop** — photon doesn't self-trap into a stable sub-V_yield droplet (disperses / stays lossy) → the self-trap regime not reached (pin why).

Pre-commit (`ave-evidence-framing`): report whichever honestly; **(II)/(III) are valid CP8 findings, NOT failures** — do NOT force a "genesis" claim. Matched-baseline + the 4-check gate keep it falsifiable.

---

## §6 Discipline

`substrate-native-check` CP8 (precursor-not-plant; matched baseline; layer-by-layer) + CP5 (saturation-modulated local clock `ω_local`) + CP6 (reactance pair — both `V_inc`/C AND `Φ_link`/L tracked, the slosh) + CP4 (phase-space coords for the (2,3)) · `phase-space-coordinate-check` · `consistency-vs-emergence` (checks 2/3 = consistency; check 4 = emergence-test) · `ave-canonical-source` (`ω_C`, `ℓ_node`, `V_yield`, `V_snap` from `ave.core.constants`) · `ave-driver-script-honesty` (forward, no fit) · `ave-evidence-framing`.

**Deliverable:** `research/2026-06-06_electron-genesis-drop-result.md` (the 4-check gate outcome + the I/II/III verdict + the matched-baseline comparison) + the driver + the animation (mp4/gif). Reviewed PR; no merge.
