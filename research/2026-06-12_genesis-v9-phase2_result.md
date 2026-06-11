# Genesis v9 — Phase-2 Result (SMOKE scaffold — 2026-06-12)

> **Prereg:** `research/2026-06-12_genesis-v9-phase2-prereg_FROZEN.md`
> **Engine class:** discrete srs TLM + Op14 `z_local(A²)` + Op3 @ CONNECT
> **Run class:** **SMOKE-ONLY** (`--smoke`: L=8, P6 steps=200, P5 steps=300). Full L≥10 / 800-step
> battery **not yet executed** — do not promote bins to D1 adjudication.

## Implementation landed

| Artifact | Path |
|----------|------|
| Op14/Op3 vector-TLM | `src/ave/core/chiral_lattice_vector_sat.py` |
| Tests | `src/tests/test_chiral_lattice_phase2.py` (6/6) |
| Driver | `src/scripts/vol_1_foundations/chiral_lattice_phase2_genesis.py` |
| JSON | `assets/sim_outputs/genesis_v9_phase2_genesis.json` |

## P5 — hosting (planted `(2,3)` ansatz)

| Gate | Threshold | SMOKE result |
|------|-----------|--------------|
| P5-E | E/E₀ ∈ [0.5, 1.5] | **0.606** — PASS |
| P5-Q | \|ΔQ/Q₀\| ≤ 5% | **135%** — **FAIL** |
| P5-T | ≥500 steps | 300 steps (smoke) |

**P5 verdict (smoke): FAIL** — charge proxy drifts; hosting not demonstrated at smoke depth.

## P6 — genesis-by-precursor (smoke cells)

| Cell | Bin | plateau % | e_driveoff | θ concordant |
|------|-----|-----------|------------|--------------|
| srs-R:+z | SET-ACHIRAL | 0.23 | 0.86 | no |
| srs-R:-z | SET-ACHIRAL | 0.23 | 0.86 | no |
| srs-L:+z | CVR-SET* | 0.02 | 0.86 | yes |
| srs-L:-z | CVR-SET* | 0.02 | 0.86 | yes |
| srs-R Op3-OFF | TRANSIENT | 3.39 | — | (ablation capped) |

\*CVR-SET label on **smoke grid only** — missing diamond control, κ=0 ablation, amplitude sweep,
and full step count. **Not a genesis claim.**

**P6 verdict (smoke):** machinery runs; **no prereg-grade BIN assignment**. Partial localization
on srs-L under smoke parameters; srs-R lands SET-ACHIRAL (persists without geometry-handed θ).

## Op3 ablation

Op3-OFF capped at TRANSIENT (cannot be CVR-SET per freeze). Plateau 3.39% on smoke — Op3
discriminator not yet separating at this resolution.

## A-027 / honest closure

- One-step energy conservation with Op3: **≤ 1e−10** (keeper test).
- Multi-step / drive-on runs: **not** closed-system genesis tests (drive injects energy).
- Full BIN-D on discrete TLM remains **consistent with engine-class ceiling** until L≥10
  production run + Op3-ablation comparison complete.

## Next

1. Production driver (no `--smoke`): L≥10, 800 steps, four-cell × amp sweep + diamond + κ ablation.
2. Re-score P5 with documented `(2,3)` seed certificate.
3. Feed bins into D1 adjudication memo (after production run only).
