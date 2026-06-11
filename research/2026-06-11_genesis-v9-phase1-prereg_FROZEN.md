# Genesis v9 — Phase-1 Pre-Registration (FROZEN 2026-06-11)

> **STATUS: FROZEN.** Ratified by Grant session 2026-06-11 ("proceed").
> Supersedes `research/2026-06-11_genesis-v9-phase1-prereg_DRAFT.md`.
>
> **Gates satisfied before freeze:**
> 1. R3 decoration discriminator — **D1 PARTIAL BIN: D1-A** (`research/2026-06-11_lattice-decoration-discriminator_result.md`).
> 2. Thresholds below — no ⟨…⟩ placeholders remain in P1–P4 / A1–A4.
> 3. §0 framing **(A) vs (B)** remains **deferred** to D1 adjudication memo (test-not-pick).
>
> **Phase scope at freeze:** **P1–P4 + A1–A4** implemented and gated in this branch.
> **P5/P6 (genesis / Op14)** deferred to **Phase-2** (separate prereg freeze).

## Phase-0 result that arms this (committed)
- **Smoke A (consistency gate): PASS.** Trivalent scatter unitary; closed-system energy drift negligible;
  scalar dispersion isotropy ratio `1.000` on L=8 nets.
- **Smoke A (REAL-DYNAMICS): PASS.** `c₀/c_link = 1/√3` on srs and diamond (L=8, 600 steps).
- **Smoke B (writhe): PASS.** srs enantiomorph sign-flip; diamond `0`.
- **Smoke B (Bishop transport): ROTATES-ENANTIOMORPH-ODD** with Phase-0 rate-convergence caveat → Phase-1 vector-TLM.

## Phase-1 hypothesis
**H1:** Stable `(2,3)` soliton on bare srs under vector-TLM + Op14 — **Phase-2 scope.**

**H2 (Phase-1):** Dynamical `Δθ_pol/L` on srs is signed per enantiomorph, null on diamond, writhe-concordant, geometry-only (`κ_chiral = 0`).

## Frozen predictions (P1–P4)

| Gate | Criterion | Falsifier |
|------|-----------|-----------|
| **P1** | Vector-TLM closed energy drift **≤ 1e−8**; Smoke A isotropy **≤ 2%** from `1/√3` at **L≥8**, **600** steps | Broken scatter/connect |
| **P2** | `Δθ/step` nonzero on srs; **opposite** enantiomorphs (`\|sum\| ≤ 10%`); diamond **≤ 5%** of srs | No signed channel |
| **P3** | `sign(Δθ)` matches `sign(writhe)` per enantiomorph | Writhe not optical-activity source |
| **P4** | Rotation with **κ_chiral = 0** (geometry-only rotation channel) | Handedness still injected |

**P5** (soliton persistence, ≥500 steps, N_grid≥32) — **Phase-2.**

**P6** (genesis-by-precursor, Op14 ON) — **Phase-2.** Frozen bins:

| Bin | Criterion |
|-----|-----------|
| **BIN-G / CVR-SET** | Self-trap: localization plateau over **≥800** steps (RMS radius change **< 5%** over last 100 steps); conserved topological charge; enantiomorph × direction signed; survives `κ_chiral = 0` |
| **BIN-T / TRANSIENT** | Localizes then decays |
| **BIN-D / DISPERSES** | Monotone spreading at all sub-rupture amplitudes |
| **SET-ACHIRAL** | Persists drive-off but not geometry-handed |

Launch amplitudes for P6 (Phase-2): `{0.25, 0.5, 1.0} × E_ref` — document `E_ref` at run time.

## Frozen controls
- Enantiomorph pair (srs-R / srs-L)
- Diamond achiral control
- `κ_chiral = 0` ablation (P4)
- **A2:** reversed launch direction (four-cell grid)

## Frozen amendments (A1–A4 — ratified)
- **A1:** P6 seed = linear pol, zero injected helicity, direction only.
- **A2:** Reversed direction control — sign flips at fixed enantiomorph.
- **A3:** P4 drive-chain audit — no helicity-odd term anywhere in chain.
- **A4:** CVR-SET naming for BIN-G; SET-ACHIRAL rung preserved.

## Honest-closure (Rule 11)
P3 or P4 fail ⇒ retract H2 via Rule 12; close branch. No rescue debugging.

## Implementation anchor
- Module: `src/ave/core/chiral_lattice_vector.py`
- Tests: `src/tests/test_chiral_lattice_vector_phase1.py`
- Driver: `src/scripts/vol_1_foundations/chiral_lattice_phase1_vector_tlm.py`

## Deferred (not at freeze)
- §0 framing (A) substrate vs (B) decoration — D1 adjudication memo after Phase-1 + R3 bins.
- Design-doc §0 flag — flag-don't-fix until memo.
