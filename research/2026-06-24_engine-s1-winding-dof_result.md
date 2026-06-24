# S1 RESULT — The (2,3) Winding as a Separately-Conserved DOF: PASS-WITH-FLAGS

**Status:** RESULT (committed gate + acceptance test; branch-only, NOT merged — Grant merges).
**Date:** 2026-06-24
**Pre-reg (FROZEN):** [`2026-06-24_engine-s1-winding-dof_prereg.md`](2026-06-24_engine-s1-winding-dof_prereg.md) (commit `bed0b2d3`, frozen pre-run).
**Epic:** AVE engine RE-ROUTE — [`_orchestration/2026-06-24_engine-reroute-pathway.md`](../_orchestration/2026-06-24_engine-reroute-pathway.md) S1 row.
**Branch:** `analysis/engine-s1-winding-dof` off `bed0b2d3` (off origin/main `b33b3299`). 4 commits: `e67db026` → `955f5003` → `a35d62ee` → `8e38bd2f`.
**Gate code:** `src/ave/core/s1_winding_conservation_gate.py`. **Test:** `src/tests/engine_acceptance/test_s1_winding_conservation.py` (9 tests, all PASS; `make verify` PASS).
**Process:** built + run by an implementer against the frozen falsifier, then verified by 3 refute-by-default auditors + a synthesis (workflow `waw44a1os`).

---

## VERDICT: PASS-WITH-FLAGS — holds under all three adversarial audits.

All three refute-by-default auditors returned **CONFIRMED** with **`auto_void=false`**; synthesis `blocking_issues=[]`. The standalone gate prints `VERDICT: PASS` (exit 0).

**The (2,3) winding is a separately-conserved DOF on an isolated single knot.** This upgrades **"A1-sustains-rotation" from asserted-CLASS to derived-REAL** — **scoped** to (a) the declared **real-space ω director-phase** coordinate and (b) **single-knot conservation**. It is **CONSISTENCY-class, NOT the α-free chord** (that is S4); the **Q=137 slot stays EMPTY**; **mass=A1 (PR#260) untouched**. Two-soliton TRANSFER was **DEFERRED** (pre-reg §3(d)) and is **not built**.

### Make-or-break gates (pre-reg §3)

| Gate | Outcome | Evidence |
|---|---|---|
| (a) NON-VACUITY | PASS | ω evolves under its OWN wave eq `a_ω = c_ω²∇²ω − ω_gap²ω`, own momentum `π_ω` (max\|π_ω(0)\|≈0.35), max\|Δω\|≈0.51 over 400 steps; `real_dynamics_ran=True`. Not a frozen template. |
| (b) KNOWN-SIGNAL | PASS | `compute_Q_link` reads Q_link=3, w_tor=2 on the seeded canonical (2,3); ω≡0 null reads 0. |
| (c) CONSERVATION + LOCAL CONTINUITY | PASS | Winding integer (2,3) held across 6 raw-float checkpoints (600–1200 steps, N=40/48/56); `alias_frac=0.00–0.17 ≤ 0.34` (raw float, NOT snapped int); local continuity `∂_t W = source + flux` closes rel≈0.04–0.05 ≤ 0.35. |
| (e) LIVE NEGATIVE CONTROL | **FIRES** | lock-OFF `\|L_ω\|` pumps 9.5× (the v3 runaway the lock arrests) AND `unwind_topology` breaks the integer 3→0; the `photon_deplete` detonation arm breaks (2,3)→(2,1), alias 0.42 > canary. The gate genuinely discriminates. |
| (f) GENESIS-24 POSITIVE CONTROL | PASS | `slaved_omega` arm (ω:=F(V)) → independence=False (reachable-False PROVEN, NOT auto-void); real arm independent under a V-perturbation. |
| validate-on-known (§4 floor) | PASS | `compute_Q_link` recovers Q_link=3, w_tor=2 on `seed_pq_winding(2,3)` at N=32/40/48; null reads 0. |

**α-clean:** confirmed — readout through `_winding_host` (κ̃=6/5, guard triad live at `_winding_host.py:120/150/170`); no executable ALPHA on the chord path; no 137/0.00729 literal; Q=137 slot empty.

---

## HONEST FLAGS (all non-blocking; surfaced, not papered over)

1. **Two extractors on two known-goods (A46 "two 3s").** `compute_Q_link` reads the real-space ω **director-phase** winding (§4 floor; H_bel≡0 on its pure-transverse plant); `extract_2_3_omega_fast` reads the **LC-quadrature** winding (§3(c) conservation read; carries nonzero H_bel). They read **different objects**; each is validated on its own known-good. The PASS certifies two distinct reads, **not** a single-coordinate end-to-end chain. Both are named in the pre-reg; disclosed per the A46 coordinate-category guard.
2. **Controls run on the COUPLED arm, conservation subject on the ISOLATED arm.** The isolated single knot has `|L_ω|≡0` (zero-net-L poloidal pattern, buckle OFF) and V decoupled from ω, so the neg-control `|L_ω|`-pump and pos-control V-perturbation are dead there. The controls therefore use the coupled (buckle+photon ON) arm so the canary can fire and independence can be probed; the conservation subject (gate c) stays on the isolated knot. A falsifiability fix, not a tune-to-PASS.
3. **Continuity is the single-knot LOCAL current, not a two-body hop.** `∂_t h = 2π·(∇×ω)` [ω-tank LC breathing source] + `∇·(ω×π)` [boundary helicity-current flux, ≈0 for the isolated knot]. This is the pre-reg §3(c) substrate-native "winding is a conserved current" for ONE knot. Two-soliton transfer is DEFERRED.
4. **The lock-helicity-drift canary is redundant on the isolated arm.** `|ΔH_bel|/H_bel` pre/post the lock substep = 0.0 (lock conserves exactly), but it is **untrippable** on the isolated knot (~1e-20). Conservation is independently carried by integer-held + energy-flat + local-continuity, which DO have reachable-FAIL (see gate e). Recommend reframing this canary as "lock-injects-no-helicity" or dropping it from the PASS conjunction.
5. **Resolution measured ONCE at the static seed, not held-THROUGHOUT (pre-reg §4 deviation).** The gate reports cells/turn = 8.38 at the seed (r=4). The pre-reg §4 demanded re-verifying ≥~3–4 cells/turn **throughout** evolution. The auditor's ω²-weighted real-radius arithmetic gives true ~4.6–5.2 cells/turn (the Gaussian envelope concentrates at ~0.6·r), so **q=3 IS resolved** (> the 3.0 floor and Nyquist 2.0) and the conclusion holds — but the reported 8.38 **overstates the true margin ~1.8×**. The automated throughout-check was not implemented. Recommended hardening: implement the live ω²-weighted resolution-throughout measurement, or correct the reported number to ~4.6 cells/turn.

**Net:** the make-or-break verdict (winding = separately-conserved DOF) is robust to flags 1–5; none changes PASS→FAIL. Flags 4 and 5 are honest-reporting / hardening refinements for a follow-up.

---

## What this delivers to the pathway

- **S1 PASS** → the boundary/topological-localization re-route's load-bearing joint holds: the winding can be the conserved, handedness-carrying DOF that (per the post-Stage-2 hypothesis) pins the dispersing A1 core. The mutual-pinning hypothesis itself remains OPEN — tested progressively by S2 (`H_couple`) and S3 (Γ=−1 cavity).
- **NOT a chord.** S1 is the consistency gate that *enables* the parity-odd forward-prediction class (optical-activity sign-flip; the co-vs-anti-handed force ratio) — but the chord lives at S4 / the forward predictions, not here.

## Recommended follow-up (implementer-lane)

- Land the S1 row in `_orchestration/2026-06-24_engine-reroute-pathway.md` (done in this PR) and carry the two-extractor + coupled-controls + consistency-class qualifiers.
- Address flags 4 (canary reframe) and 5 (live resolution-throughout) — non-blocking hardening.
- Next stage = **S2 (`H_couple` keeping ω independent)** per the pathway critical path.

## Reproduce

```bash
cd <worktree>
PYTHONPATH=$PWD/src <repo>/.venv/bin/python -m pytest \
    src/tests/engine_acceptance/test_s1_winding_conservation.py -q     # 9 passed (~87s)
PYTHONPATH=$PWD/src <repo>/.venv/bin/python -m ave.core.s1_winding_conservation_gate   # prints VERDICT: PASS, exit 0
```
