# (2,3)-Winding Extractor — Coordinate Fix + Validation (orchestration)

**Date:** 2026-06-05 · **Branch:** `analysis/2026-06-05-2-3-winding-extractor` (off `origin/main` `c1d7390f`, worktree `AVE-Core-2-3-wt`)
**Prereg (FROZEN):** [`research/2026-06-05_2-3-winding-extractor-coordinate-prereg.md`](../research/2026-06-05_2-3-winding-extractor-coordinate-prereg.md)
**Session:** orchestration (Grant in-session). Branch + reviewed PR; no direct-to-main.

## §0 What this is (and is NOT)

Resolves the prior run's **auditor #1 (BLOCKING)**: the (2,3)-winding extractor is unvalidated — it failed to recover even the **Arm-C known-imposed (2,3)** (read `(8,0)/c=16` on a planted bond). Root cause (Grant 2026-06-05 + code review): the extractor measured **(C↔L-phase port1, C↔L-phase port2)** → structurally ~1:1, blind. The (2,3) lives in **(n̂ field-direction winding "2", C↔L/U(1)-fibre-phase winding "3")**.

**NOT** an α-/R·r=¼-selection test (CLOSED, anti-pattern-marked) and **NOT** a (2,3)-nucleation test (CLOSED). This is **measurement-tool validation + structural characterization** of the already-hosted Arm-C bound state. Scope-fence in prereg §0.

## §1 Phase plan

- **P1 — Build + validate the extractor (PENDING; implementor).** New extractor in the (n̂-direction, C↔L/fibre-phase) coordinate. **GATE V0:** must recover the Arm-C imposed (2,3) (`c=3` / `(2,3)`) where the legacy read `(8,0)/c=16`. V1: null on the Arm-B baseline. See prereg §2–§4.
- **P2 — Characterize single-bond vs bond-pair (GATED on V0 pass).** Where does the n̂-direction "2" close — ≈1 ℓ_node (single-bond/midpoint, Grant) or ≈2 ℓ_node (bond-pair/node-centred, `l3:30`)? Structural read only.

## §2 Implementor dispatch spec (P1)

Engine `VacuumEngine3D` (`vacuum_engine.py:1622`); legacy driver `src/scripts/vol_1_foundations/r10_vacuumengine3d_transverse_2_3_emergence.py` (Arm-C `PairNucleationGate` imposed control + `*_capture.npz`/`*_results.json` present). Build the corrected extractor; validate against Arm-C (load capture if it carries `V_inc/V_ref/Phi_link/n̂` at the trap bond, else re-run Arm C — deterministic ~3 min). Full skill discipline per prereg §5; **honest INCONCLUSIVE if V0 fails** (do NOT report a single/pair verdict on an unvalidated tool — prereg C2). Constants from `ave.core.constants`.

## §3 Orchestrator audit-verification (on return)

Independently confirm **V0 genuinely passes** (the extractor recovers the *known-imposed* (2,3), not a fit) before accepting any P2 single/pair read. If V0 fails → the result is a clean INCONCLUSIVE + escalation (ansatz vs fibre-mapping), which is itself a valid outcome. Then synthesize → Grant adjudication → reviewed PR.

## §4 Outcome

_(filled on implementor return)_
