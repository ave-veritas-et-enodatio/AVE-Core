# Genesis v9 — Phase-2 Result (PRODUCTION — 2026-06-12)

> **Prereg:** `research/2026-06-12_genesis-v9-phase2-prereg_FROZEN.md`
> **Engine class:** discrete srs TLM + Op14 `z_local(A²)` + Op3 @ CONNECT (instantaneous v1)
> **Run class:** **PRODUCTION** — P5: L=10, 500 steps; P6: L=10, 800 steps, N_drive=400,
> amp sweep `{0.25, 0.5, 1.0}`, four-cell + diamond + Op3/Op14 ablations, `κ_chiral = 0`.
> **Driver:** `python chiral_lattice_phase2_genesis.py` (no `--smoke`).

## Implementation

| Artifact | Path |
|----------|------|
| Op14/Op3 vector-TLM | `src/ave/core/chiral_lattice_vector_sat.py` |
| Tests | `src/tests/test_chiral_lattice_phase2.py` (6/6 smoke) |
| Driver | `src/scripts/vol_1_foundations/chiral_lattice_phase2_genesis.py` |
| JSON (local, gitignored) | `assets/sim_outputs/genesis_v9_phase2_genesis.json` |

**Platform notes:** `n_nodes = 8000` per srs L=10 cell; `n_nodes = 250` diamond L=10.
No `κ_chiral` injection anywhere (geometry rotation channel only). Memristive Op14 **not** used.

---

## P5 — hosting (planted `(2,3)` ansatz)

**Seed certificate (HOSTING not GENESIS):** `plant_23_ansatz` — Gaussian envelope along screw
axis (width 12% of box), phase `θ = 2·atan2(y−z₀, x−z₀) + 6π(z−z₀)/box` on transverse
components at port 0. Toroidal/poloidal winding (2,3) in **phase-space** (A46); no injected CP.

| Gate | Threshold | Production |
|------|-----------|------------|
| P5-E | E/E₀ ∈ [0.5, 1.5] | **0.434** — **FAIL** (decay below floor) |
| P5-Q | \|ΔQ/Q₀\| ≤ 5% | **5064%** — **FAIL** |
| P5-T | ≥500 steps | 500 steps — executed |
| P5-G | L ≥ 8 | L=10, n_nodes=8000 |

**P5 verdict: FAIL** — srs does not host the planted `(2,3)` ansatz under Op14+Op3 at
production depth. **H3 falsified** for this seed + integrator class.

---

## P6 — genesis-by-precursor (production cells)

Best bin per cell after amp sweep `{0.25, 0.5, 1.0}` (lowest amp wins ranking when tied):

| Cell | Best amp | Bin | plateau % | e_driveoff | θ concordant | \|Δθ\| |
|------|----------|-----|-----------|------------|--------------|--------|
| srs-R:+z | 0.25 | **CVR-SET** | 1.83 | 0.514 | yes | 1.64 |
| srs-R:-z | 0.25 | SET-ACHIRAL | 1.83 | 0.514 | **no** (A2) | 1.64 |
| srs-L:+z | 0.25 | **CVR-SET** | 1.47 | 0.514 | yes | 3.03 |
| srs-L:-z | 0.25 | **CVR-SET** | 1.47 | 0.514 | yes | 3.26 |
| diamond:+z | 0.25 | SET-ACHIRAL | 0.16 | 1.000 | no | 0.00 |
| diamond:-z | 0.25 | SET-ACHIRAL | 0.16 | 1.000 | no | 0.00 |
| srs-R:+z Op3-OFF | 0.25 | SET-ACHIRAL | 1.65 | 0.518 | no | 0.13 |
| srs-R:+z Op14-OFF | 0.25 | SET-ACHIRAL | 1.65 | 0.518 | no | 0.13 |

**P6-C controls:**
- Diamond \|Δθ\| / srs max = **0%** — achiral null satisfied (≤ 5%).
- `κ_chiral = 0` throughout — geometry channel only.
- A2 direction: srs-R:-z fails θ concordance while +z passes (same \|Δθ\|, opposite writhe×dir).

**Matched baseline (CP8):** srs-R:+z e_retention **0.514** vs Op3-OFF **0.518**, Op14-OFF
**0.518**, diamond **1.000**. **structure_driven_2x = FAIL** — srs Op14+Op3 does **not**
exceed controls by ≥2× on energy retention. Diamond retains *better* at same amp envelope.

**Op3 / Op14 ablation:** Both ablations still localize (plateau ~1.65%) without geometry-handed
θ — Op3 is **not uniquely load-bearing** for localization at amp=0.25; θ concordance requires
Op14+Op3 **and** correct enantiomorph×direction cell.

**Saturation diagnostics (last step):** srs cells `max(A²)` ≈ 13–14 (≫ 1 — deep past
`V_SNAP=1` apparatus floor); diamond `max(A²)` ≈ 38. Runs are in **saturated / post-rupture**
regime; interpret bins under A-027 engine-class ceiling.

---

## Honest closure (Rule 11 + A-027)

| Combination | Reading |
|-------------|---------|
| P5-fail + partial CVR-SET cells | **Hosting miss (H3)**; precursor localization on 3/4 srs cells at **sub-rupture amp only** |
| CVR-SET labels + matched-baseline fail | **Do not promote BIN-G / genesis** — retention not structure-driven vs diamond / ablations |
| Op3-OFF ≈ Op14-OFF ≈ srs ON (retention) | Trap channel **not isolated** to Op3 bond reflection alone at this resolution |
| Only amp=0.25 wins sweep | Higher amps (0.5, 1.0) do not improve bins — saturation-limited |

**Production verdict:**
- **P5: FAIL**
- **P6: INCONCLUSIVE for genesis** — machinery executes; 3/4 cells hit CVR-SET label at
  amp=0.25, but **matched baseline fails**, **P5 fails**, and **ablations still localize**
  without θ. Report as **partial precursor localization**, not CVR-SET genesis promotion.
- **H4:** Not confirmed at production depth. **BIN-D / SET-ACHIRAL / engine-gap** readings
  all remain live per prereg kill conditions.

**D1 memo input:** P5-fail is a **structural hit** on srs hosting; pair with D1-A partial bin
(R3) + Phase-1 P1–P4 PASS for adjudication. Does **not** auto-pick framing (A) or (B).

---

## Next

1. ~~**Phase 4 — D1 adjudication memo**~~ → **DONE:** `research/2026-06-12_lattice-d1-adjudication-memo.md`
2. ~~Corpus walk-back queue (memo §5)~~ → **P0–P1 executed** (`analysis/2026-06-12-lattice-d1-walkback`).
3. Optional Phase-2b: memristive Op14, Op10 crossing proxy, Master-Equation follow-on (A-027).
4. v10 spine — after walk-back greenlight.
