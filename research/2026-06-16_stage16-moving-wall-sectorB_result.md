# RESULT — Stage-1.6 CP8-safe OPEN route: external moving Γ=−1 wall on Sector B

**Date:** 2026-06-16 · **Lane:** implementer · **Branch:** `analysis/2026-06-16-boundary-mqj-stage16-moving-wall-sectorB`
**Prereg (FROZEN, Rule-11):** [`research/2026-06-16_stage16-moving-wall-sectorB-prereg.md`](2026-06-16_stage16-moving-wall-sectorB-prereg.md)
**Driver:** [`src/scripts/vol_1_foundations/stage16_moving_wall_sectorB.py`](../src/scripts/vol_1_foundations/stage16_moving_wall_sectorB.py) · **Results JSON:** [`src/scripts/vol_1_foundations/stage16_moving_wall_sectorB_results.json`](../src/scripts/vol_1_foundations/stage16_moving_wall_sectorB_results.json)
**Engine:** `ave.core.a1_cosserat_moving_wall_engine.A1CosseratMovingWallEngine`
**Extends:** [`research/2026-06-16_stage15-alphafree-winding-emergence_result.md`](2026-06-16_stage15-alphafree-winding-emergence_result.md) §0/§3/§4 (Stage-1.5 (c) EMERGENCE-NEGATIVE).
**Verify panel:** `w9q6nv9gm` (the coupling-curl sublattice grid-registration diagnostic).

> **Recovery note.** This result doc was lost when the agent's final-commit was killed by a 500 *after* the artifacts (driver, results JSON, 5 figures) were already committed at `a233f9ed`. This doc is reconstructed verbatim from those committed artifacts. No re-run was performed — every number below is read directly from `stage16_moving_wall_sectorB_results.json` @ `a233f9ed`.

---

## §0 — One-line summary

The external moving Γ=−1 wall on Sector B **DOES confine the photon** (known-positive PASS,
Γ→−0.993 forms), but the gated `coupling_work=0` for the **entire trace** — and that zero is
a **CARTESIAN-vs-TETRAHEDRAL grid-registration ARTIFACT, not physics**. The run is therefore
**vacuous on loop-closure** (the energize-LOCK loop was never actually tested), while being the
**diagnostic source** that overturned the Stage-1.5 (c) "structural spectator" verdict. The raw
numerical verdict is **PUMPS** (the K=400 wall has no Op17 |ω| ceiling → |ω| diverges), but the
physical reading is **WALL-CONFINES-BUT-LOOP-INERT-by-disabled-flag**.

---

## §1 — RUN configuration

- **Setup:** external moving Γ=−1 wall on **Sector B** (the photon's own Cosserat-ω sector), not Sector A (where the Stage-1.5 (c) internal spectator cage sat inert).
- **Seed:** generic transverse Gaussian ω-photon + sub-yield bulk, **UNCHANGED** from Stage-1.5 (c). No planted (2,3), no pre-co-location, no pre-winding. `seed_t0_closes_23=false`, `seed_is_generic_photon=true` (CP8-clean).
- **α-free:** `kappa_chiral=0` override routes around `KAPPA_CHIRAL_ELECTRON = α·κ̃_e`; `κ̃=6/5`, `V_yield=1.0`, `ω_yield=π`. **NO ALPHA in any update equation.** ALPHA appears only in `alpha_comparison_only` (provenance, never inserted): `ALPHA_inv_CODATA=137.0359990836958` vs `ALPHA_COLD_INV=137.0363037758784`.
- **Grid:** N=24, PML=4, `nsteps=3894`, long-window 12.0 Compton periods.
- **Operating point:** `photon_amp=2.0` (wall-formation drive level; the Stage-1.5 (c) frozen 0.3 is reported separately as the apparatus-floor read). Amplitude is a DRIVE LEVEL, not a topological/spatial plant.
- **Wall:** `K_wall=400`, reactive node-clamp via `_rotate_clamp` LC rotation.

---

## §2 — RAW VERDICT = PUMPS (numerical)

The frozen driver bins ([`stage16_moving_wall_sectorB.py:396-419`](../src/scripts/vol_1_foundations/stage16_moving_wall_sectorB.py), 4 frozen bins: LOOP-CLOSES / WALL-CONFINES-BUT-LOOP-INERT / WALL-ALSO-FAILS / PUMPS) route this run to **PUMPS** because the K=400 wall is **not Op17-bounded**: it has no |ω| ceiling, so |ω| **diverges**.

| | with-wall (`wall_True`) | no-wall (`wall_False`) |
|---|---|---|
| `omega_max_f` | **20032.56** | **20006.08** |
| `diverged` (step) | **2530** | **594** |
| `gamma_min_f` | −0.9932 | 0.0 |
| `loc_f` | 0.9114 | 0.1627 |

`"verdict": "PUMPS"`, `"verdict_reason": "the wall is not Op17-bounded (|ω| blow-up / divergence) — fix the BC"`. **BOTH** runs diverge — the no-wall run blows up *faster* (step 594 vs 2530). The diagnosis: **the photon at amp=2.0 is over-driven**; the wall slows but does not prevent divergence. The full-H ledger climbs monotonically (`H` from 2.4e3 → 1.0e10 with-wall; 1.1e7 → 5.3e7 no-wall), confirming the BC injects energy rather than storing it reactively (`_rotate_clamp` has no |ω| ceiling).

---

## §3 — PHYSICS = WALL-CONFINES-BUT-LOOP-INERT

Setting aside the numerical PUMPS divergence, the **physical** content of the gated test:

**The wall DOES confine** (apparatus-floor known-positive, `apparatus_floor.known_positive_PASS=true`):

| amp | wall | `loc_f` | `gamma_min_f` | `omega_max_f` |
|---|---|---|---|---|
| 0.3 (frozen) | True | 0.719 | −3.01e−5 | 0.088 (bounded) |
| 0.3 (frozen) | False | 0.771 | 0.0 | 0.123 (bounded) |
| 2.0 (operating) | True | **0.906** | **−0.9931** | 3.637 |
| 2.0 (operating) | False | 0.161 | 0.0 | **3954.09** |

At the operating point the wall holds the photon (`loc_f=0.906` with-wall vs `0.161` without; `gamma_min_f→−0.9931`, a Γ→−1 rim forms) and **bounds |ω| to 3.64 with the wall vs 3954 without** — a ~1000× confinement effect. `wall_forms_at_operating_point=true`, `wall_confines_at_operating_point=true`, `wall_below_floor_at_frozen_0.3=true` (at amp 0.3 the wall is below the formation floor — Γ≈0, an apparatus floor, not physics).

**But `coupling_work=0` the ENTIRE trace.** Both `wall_True` and `wall_False`: `coupling_work=0.0`, `fV_live_max=0.0`, `fV_live_frac=0.0`. The recorded `coupling_work` and `fV_live` trace arrays are **all-zero at every sample** (40 samples with-wall, 10 no-wall). `loop_fires=false`.

**INERT-EVERYWHERE.** The `generic_offset_sweep` (the CP8 plant discriminator) fires **0/6 offsets** (offsets `[-3,0,0], [-1,0,0], [0,0,0], [1,0,0], [3,0,0], [0,2,0]`): every offset returns `coupling_work=0.0`, `fV_live_max=0.0`, `loop_fires=false`. `n_offsets_fire=0`, `sweep_verdict="INERT-EVERYWHERE"`. The loop fires at NO offset — so this is not a hand-tuned-plant question (a plant would fire at exactly one offset); it is inert *everywhere*.

**CP8-spatial-provenance clean.** Seed is the generic photon (`seed_is_generic_photon=true`, `seed_amplitude=2.0` = drive level, not a plant). The wall position is the **α-free Γ-field argmin, recomputed from the focusing ω-field every sub-step** (generic rule, NOT hand-placed): wall front 12,12,12 → 11,19,19 (displacement 9.95 cells), photon peak 12,12,12 → 19,9,19 — they co-evolve under the generic rule.

---

## §4 — 🔴 THE LOAD-BEARING FINDING (verify panel `w9q6nv9gm`)

**This run's durable value is the diagnostic, not the verdict.** `coupling_work=0` is a
**CARTESIAN-vs-TETRAHEDRAL grid-registration ARTIFACT, NOT physics — a disabled flag.**

The coupling source `f_V` was computed via the **inherited Cartesian** `_cosserat_axial_curl`
(an `np.roll(±1)` single-axis curl). On the K4 lattice the alive sublattice is
`mask_alive = (all-even | all-odd)` parity; **every single-axis ±1 neighbor of an alive cell is
DEAD**. So the Cartesian curl registers the entire Ξ field **on the K4-DEAD sublattice**, while
`g` (the coupling gate) is masked to **ALIVE** — giving `g·Ξ ≡ 0` for **ANY** ω-field, confined
or not. The zero is structural to the stencil, independent of whether the photon is confined.

The `coupling_curl_sublattice_discriminator` (driver §3, flag-don't-fix, **a measurement**) makes
this exact and unambiguous (identical in both `wall_True` and `wall_False` `coupling_overlap` blocks):

| quantity | Cartesian curl | tetrahedral curl |
|---|---|---|
| `Xi_*_alive_max` | **0.0** | 2.9323 |
| `Xi_*_dead_max` | 2.9323 | **0.0** |
| `gXi_*_max` | **0.0** | 2.9207 |
| `overlap_cells` | **0** | **1024** (= full alive-interior) |

`g_alive_cells=1024`. The inherited Cartesian curl overlaps the alive gate at **0 cells**; the
substrate-native tetrahedral curl overlaps at **1024 cells** = the entire alive interior. The
coupling `f_V` was being read off **0** of its 1024 valid sites.

**Consequence: the energize-LOCK loop was NEVER actually tested.** `coupling_work=0` is forced by
the stencil before any physics enters — so this run is **VACUOUS on the gated question**
(loop-closure). The WALL-CONFINES-BUT-LOOP-INERT verdict cannot be read as "the obstruction is
deeper than confinement" — the loop was disabled by a grid-registration bug, not by physics.

**This diagnostic is the SOURCE that overturned the Stage-1.5 (c) "structural spectator" verdict.**
Stage-1.5 (c) concluded `f_V=0` meant the winding curl never co-locates with the cage core (a
structural null, adversarially "confirmed"). That `f_V=0` came from the **same** Cartesian-curl
stencil registering on the same dead sublattice — i.e. Stage-1.5 (c) read its spectator verdict off
0/1024 valid sites too. The Stage-1.5 (c) "structural spectator" conclusion is therefore
**overturned**: it measured a disabled flag, not a structural fact.

---

## §5 — SUPERSEDED-BY

This run is superseded by the corrected re-run on
**`analysis/2026-06-16-stage16-rerun-amendments`** (remote `2a83808c`), where the **two-sided
tetrahedral swap** closed the artifact — `f_omega` now fires on the **alive** sublattice
(`overlap_cells_tetrahedral=1024`). With the stencil corrected:

- **Q3 (the real loop-test) is HELD pending a bounded-wall build.** The corrected stencil exposes
  the next obstruction: the K=400 reactive node-clamp `_rotate_clamp` **has no |ω| ceiling**, and the
  **corrected-stencil wall-OFF baseline detonates at amp=2.0**. So the loop-closure question cannot
  yet be answered cleanly: a confined-but-diverging trace cannot distinguish energize-LOCK from
  numerical blow-up.
- The **K_wall sweep returned AMBIGUOUS-pending-stable-BC** — confinement strength and divergence
  onset trade off without a stable boundary condition to anchor the read.

**The clean loop-closure test requires a bounded (Op17-ceiling) wall** so the corrected-stencil
`f_omega` fires on a *non-diverging* confined photon. Until that build lands, Stage-1.6's gated
question (does the energize-LOCK loop close?) remains **OPEN** — neither LOOP-CLOSES nor a clean
WALL-CONFINES-BUT-LOOP-INERT is earned.

---

## §6 — Bin disposition (FROZEN bins, [`stage16_moving_wall_sectorB.py:396-419`](../src/scripts/vol_1_foundations/stage16_moving_wall_sectorB.py))

| Bin | This run |
|---|---|
| LOOP-CLOSES | **NO** — `coupling_work=0`, but VACUOUS (the loop was disabled by the Cartesian-curl stencil, never tested). |
| WALL-CONFINES-BUT-LOOP-INERT | physical reading, but the "INERT" is a **disabled flag**, not physics. |
| WALL-ALSO-FAILS | NO — the wall confines (`loc_f=0.906`, Γ→−0.993, |ω| held 3.64 vs 3954). |
| **PUMPS** | **RAW VERDICT** — the K=400 wall has no Op17 |ω| ceiling → |ω| diverges (step 2530 with-wall; 594 no-wall). |

`"verdict": "PUMPS"`, `"loop_fires": false`, `"wall_confines": true`.

---

## §7 — Figures (REAL data, [`research/figures/`](figures/))

1. [`stage16_fig1_moving_wall_tdr.png`](figures/stage16_fig1_moving_wall_tdr.png) — moving-wall TDR: wall front vs photon-peak co-evolution.
2. [`stage16_fig2_coupling_work_fV.png`](figures/stage16_fig2_coupling_work_fV.png) — coupling_work / f_V trajectory (flat-zero, overlaid on the Stage-1.5 (c) spectator baseline).
3. [`stage16_fig3_sectorB_gamma_smith.png`](figures/stage16_fig3_sectorB_gamma_smith.png) — Sector-B Γ-plane locus (Smith): center→rim migration under the wall.
4. [`stage16_fig4_winding_read.png`](figures/stage16_fig4_winding_read.png) — winding (2,3) read (w_tor, w_pol vs time).
5. [`stage16_fig5_apparatus_floor.png`](figures/stage16_fig5_apparatus_floor.png) — apparatus-floor known-positive (α-free wall confining a known photon vs no-wall dispersal).

---

## §8 — Honest framing (Rule 11 / Rule 16)

This run is **vacuous on loop-closure** — the gated number was forced to zero by a grid-registration
bug before any physics entered. It is **not** a clean negative on the loop-closure question, and it
must **not** be cited as "the propagating photon can't become a bound resonator even with an external
wall" (that would be reading a disabled flag as a substrate statement). Its **durable value** is the
diagnostic: the Cartesian-curl-on-dead-sublattice artifact, made exact by the
`coupling_curl_sublattice_discriminator` (0 vs 1024 overlap cells), which is the **source** of the
whole grid-registration correction and which **overturns** the Stage-1.5 (c) structural-spectator
verdict. The corrected re-run (`analysis/2026-06-16-stage16-rerun-amendments`) carries the loop-test
forward; Stage-1.6's gated question stays OPEN pending a bounded-wall build.

Do NOT: conclude chord/echo (orchestrator adjudicates); read m_e/e/ℏ/2 as success (echo); merge
(main is PROTECTED).
