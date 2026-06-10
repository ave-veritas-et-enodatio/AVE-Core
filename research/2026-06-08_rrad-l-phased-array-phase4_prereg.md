# PREREG — Phase 4: phased-array u-sector compressional rectification (the closing test)

**Date:** 2026-06-08 · **Branch:** `analysis/2026-06-08-rrad-l-darkwake` (continues Phases 1–3)
**Companions:** Phase 2 (`..._rectification_result.md`, no rect — smooth kernel), Phase 3 (`..._stickslip-phase3_result.md`, OUTCOME B — latch in ω, momentum in u, **sector mismatch**).
**Grant directive 2026-06-08:** "A then B; high-frequency plasma, phased arrays of emitters causing constructive interference."

> **SCAFFOLD** (orchestration-written, for review before compute). This is the **closing test** of the exotic rectification claim: the one physically-motivated config the prior phases excluded.

---

## 0. Target

Phases 2–3 failed by **sector mismatch**: the chiral ω-source uses chirality for directionality → trapped in the **ω / shear** sector → mismatched from the **u-sector** (translational/P-wave) where the thrust momentum `ρ⟨u̇²⟩` lives. Phase 4 tests the resolution: a **phased-array compressional (u-sector) drive** — direction from the **phase gradient, not chirality** — **co-locating** drive + latch + momentum in the u-sector. Does it rectify directed u-momentum (SYM nulls, ASYM rectifies)?

## 1. Why the phased array dissolves the mismatch (the resolution logic)

- **Direction without chirality.** A phased array steers its beam by inter-element phase gradient. So directionality no longer requires the ω/rotational chirality that trapped the prior source in the shear sector.
- **Constructive interference = compression.** The array's focal density peak is a **u-sector** (compressional / P-wave / bulk) excitation, and geometric concentration `G_geom` can drive the local field to **V_yield** (Axiom-4 boundary) — co-locating the drive with the yield/latch and with the u-momentum observable.
- **The u-sector latch (NOT the ω Lenz-freeze).** Per the new hysteresis index ([common/substrate-hysteresis-index.md](../manuscript/ave-kb/common/substrate-hysteresis-index.md) Class 3), the **translational/plastic** stick-slip is the **Peierls-Nabarro STZ** (`peierls-nabarro-paradox.md`) + Bingham yield τ_y (`saturation-operator` leaf) — canonically distinct from the ω-sector Lenz-freeze Phase 3 used. This is the latch that co-locates with the u-momentum.

## 2. Design

- **Drive:** a phased array of N emitters (high-frequency plasma class), phased for **constructive interference** at a focal region → compressional u-sector excitation; beam direction set by the phase gradient. Reaches V_yield locally via `G_geom` (Q-G42 `V_yield^(apparatus) = E_yield/G_geom`).
- **Coupling ENABLED** — `disable_cosserat_lc_force=False` (Phase 3 flag #2: the prior run disabled u↔ω coupling; here the physical config is on).
- **Latch:** the u-sector Peierls-Nabarro / Bingham plastic stick-slip (canonical, per §1 / hysteresis-index Class 3) — co-located with the compressional drive + the u-momentum.
- **Observable:** the 2nd-order DC directed u-momentum (`ρ⟨u̇²⟩` projected on the beam axis) — same family as Phases 2–3, now sector-matched.

## 3. Rule-12 guard (LOCKED)

- Latch params (yield = Axiom-4 `A_yield=1`; relaxation/τ from canon) — **not tuned.** Array directivity is **geometry** (N, element spacing, phase gradient) — a hardware parameter, NOT tuned-to-rectify. SYMMETRIC (non-focusing / random-phase) **control** must null. If rectification appears only for non-canonical latch params → rescue-fill → NEGATIVE.

## 4. Discriminating outcomes

- **A — rectification CONFIRMED:** phased-array u-sector drive + coupling-on + u-sector latch → SYM nulls, ASYM/focused rectifies directed u-momentum (ratio ≫1) at canonical latch params. → the mechanism was **sector-mismatched, not dead**; revived via the array; the warp/Alcubierre claim's mechanical basis is restored.
- **B — still NO rectification:** even sector-matched (u-drive + u-latch + coupling-on), no contrast. → **all sectors exhausted → exotic rectification definitively DEAD** (strongest possible closure); the warp/wormhole claim must walk back. *But the array still beams a directional wake → the non-exotic beam-shaping thrust (path B) stands.*
- **C — rescue-fill:** rectifies only for tuned latch params → NEGATIVE.

## 5. Falsifier + the dual payoff (A and B are one hardware)

If the sector-matched phased-array config does NOT rectify, the exotic chiral/rectification thrust mechanism is **definitively refuted across all sectors** (ω tried in Phase 3, u tried here). **But the same phased array measured here also yields the non-exotic directional-radiation thrust** `F = N·P/c_shear` (the beam-shaping path B) — so this driver ALSO quantifies the fallback. Report both: the rectification verdict (A/B/C) AND the beam-shaping directivity / directed-radiation thrust.

## 6. Skills + deliverables

- **Skills:** ave-canonical-source (latch + yield from canon) · substrate-native-check (phased-array compressional drive on the u-sector + the Peierls-Nabarro latch, coupling-on; NOT a phenomenological array model) · ave-canonical-leaf-pull (the u-sector latch + V_yield/G_geom) · ave-driver-script-honesty (Rule-12 guard; B is an honest success) · consistency-vs-emergence + ave-discrimination-check (result-time).
- **Deliverables:** `research/2026-06-08_rrad-l-phased-array-phase4_result.md` (A/B/C + the beam-shaping directivity/thrust number + DERIVED/VERIFIED/BLOCKED); driver (new or extending the Phase-3 driver) with the phased-array u-sector source + coupling-on + Peierls-Nabarro latch. Commit on the branch; orchestration handles PR #144. Do NOT push/merge.
