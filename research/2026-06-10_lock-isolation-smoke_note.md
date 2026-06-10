# Crystal-Graft v4 — LOCK-ISOLATION SMOKE (companion note to the graft-v4 result)

**Date:** 2026-06-10 · **Branch:** `analysis/2026-06-10-graft-v4-photon-helicity` · **Lane:** implementer
**Parent result:** [`2026-06-10_graft-v4-photon-helicity_result.md`](2026-06-10_graft-v4-photon-helicity_result.md) (see the dated VERDICT ADDENDUM)
**Prereg (FROZEN):** [`2026-06-10_graft-v4-photon-helicity_prereg.md`](2026-06-10_graft-v4-photon-helicity_prereg.md) §2 (the LOCK SMOKE)
**Driver (new):** [`../src/scripts/vol_1_foundations/crystal_graft_v4_lock_isolation_smoke.py`](../src/scripts/vol_1_foundations/crystal_graft_v4_lock_isolation_smoke.py)
**Results:** `crystal_graft_v4_lock_isolation_results.json` · **Figure:** `crystal_graft_v4_lock_isolation_fig.png`

## Verdict — **NOT-DEMONSTRATED** (with **INERT** under the one destructive arm)

The v4 CHANGE-2 lock does **not** earn its keep. In **both** regimes tested, lock-ON and lock-OFF give the
**same** knot fate to within parts-per-billion — the lock makes no measurable difference to whether the
planted (2,3) survives.

## Why this smoke exists (the panel's highest-priority follow-up)

The v4 SMOKE-1 (planted-knot survival) PASSED, but with `read_tN_lockON == read_tN_lockOFF == [2,3]`
(`crystal_graft_v4_results.json: smoke_lock`). Both arms survived ⇒ that smoke never isolated the lock:
survival was not distinguished from the source simply being too gentle to destroy the knot. This bounded
diagnostic (NOT a v5) supplies the missing isolation: it applies a **v3-strength buckle** — the
frozen-Beltrami-template director that destroyed the planted knot in graft-v3 — to a resolvable planted
(2,3), in lock-ON vs lock-OFF arms with **everything else held identical (only `lock_eta` differs)**.

## Apparatus / config (verify-before-cite; v3 config via `git show 4627651a`)

- **v3-strength buckle reproduced in the v4 engine** via `photon_coupling=False`, which makes
  `CrystalGraftV4._buckle_forces()` defer to v3's frozen-Beltrami-template buckle
  ([`crystal_graft_v4.py:147-149`](../src/ave/core/crystal_graft_v4.py)) once `build_beltrami_director`
  has populated `self._b_dir`. The only engine difference vs graft-v3's destructive smoke is the v4 lock
  substep (`lock_eta>0`).
- **v3 config (verbatim from `git show 4627651a:src/scripts/vol_1_foundations/crystal_graft_v3_run.py`,
  `_make_engine` + `smoke_independence`):** N=44, `source_mode='abc'`, `lam_sign=+1`, p=2, q=3, S_min=2e-3,
  A_cap=0.999, ω_gap=1.0, wall_center=0.78, wall_width=0.16, κ̃=6/5, pml=5; `seed_bulk(σ=4.5, frac=0.9)`
  + `seed_photon(σ=5, λ=7, amp=0.35)` (decoupled — matches v3); `build_beltrami_director` at `wall_geometry(e)`.
- **apparatus-floor (ave-apparatus-floor-attribution):** the planted (2,3) is at `Rk=0.22·N=9.68`,
  **`rk=Rk/φ²=3.697 cells ≥ 3`** (above the extractor's poloidal-resolution floor, prereg:92), amplitude 0.3.
  Every arm reads **`t0=(2,3)`, `is_2_3_t0=True`, `alias_clean_t0=True`** — the plant is genuinely above the
  floor, so a tN-collapse is a real destruction, not an extractor artifact. 600 live steps (> the 500 the
  prereg LOCK smoke and v3 used).

## Frozen resolution rule (Rule 11 — written before the run, applied to the data)

- lock-OFF collapses ((2,3)→(2,1)-style) **AND** lock-ON preserves (2,3) → **EARNS-ITS-KEEP**
- both arms survive (both read (2,3)) → **NOT-DEMONSTRATED** (the source matters, not the lock)
- both arms collapse (neither reads (2,3)) → **INERT** (the lock cannot save it at this strength)

## Result table

| arm | seed δ | lock η | t0 read | tN read | is(2,3) tN | H_bel t0→tN | H_bel peak | lock `\|drift\|` max | outcome |
|---|---|---|---|---|---|---|---|---|---|
| `v3seed_lockOFF` | 0.4 | 0.0 | (2,3) | **(2,2)** | False | +5.28 → **+4512.75** | +10904.0 | — (no lock substep) | knot destroyed |
| `v3seed_lockON` | 0.4 | 0.05 | (2,3) | **(2,2)** | False | +5.28 → **+4512.75** | +10904.0 | **4.19e-16** | knot destroyed |
| `v4seed_lockOFF` | 0.00775 | 0.0 | (2,3) | (2,3) | True | +5.28 → +35.79 | +282.4 | — (no lock substep) | knot survives |
| `v4seed_lockON` | 0.00775 | 0.05 | (2,3) | (2,3) | True | +5.28 → +35.79 | +282.4 | **5.97e-16** | knot survives |

**ON vs OFF are identical to parts-per-billion.** Exact `H_bel_tN`: v3-seed OFF `4512.752727945` vs ON
`4512.752753832` (Δ ≈ 2.6e-5, **rel 5.7e-9**); v4-seed OFF `35.79229734` vs ON `35.79224647`
(Δ ≈ 5.1e-5, **rel 1.4e-6**). The lock changes the planted knot's fate by ~6 ppb (destructive arm) /
~1.4 ppm (gentle arm) — i.e., not at all.

## The lock_helicity_drift canary (`crystal_graft_v4.py:348-352` — built, never called; wired here)

- **lock-ON arms:** per-substep `|ΔH_bel/H_bel|` max ≈ **4–6e-16** (machine epsilon). The lock substep
  **does conserve H_bel across itself to machine precision** — it is a faithful rigid-rotation removal.
- **lock-OFF arms:** canary = 0.0, but this is **N/A, not a real zero** — the lock substep never runs, so
  `_Hbel_pre_lock`/`_Hbel_post_lock` stay at their init (0.0). Reported as "no lock substep".

So the lock does exactly what it claims **across its own substep** (H_bel-neutral rigid-rotation removal),
yet that neutrality is **irrelevant to knot fate**: the destruction lives in a mode the lock does not touch.

## Mechanism (why the lock is inert) + a cross-cutting finding (flag-don't-fix)

1. **The lock removes only the net rigid rotation `L_ω = ∫r×π_ω`**, which is **orthogonal to both the
   poloidal winding and the topological charge `H_bel`**. The destruction here is a **local H_bel pump**
   (+5.28 → peak +10904 → +4512 in the v3-seed arms), not a rigid rotation — so the lock has no purchase on
   it. This is the same separability the engine docstring invokes to PROTECT the LC quadrature; the flip
   side is that the lock is powerless against any destruction carried in that quadrature.
2. **The v3 (2,3)→(2,1) collapse that motivated building the lock is SEED-driven, not buckle-driven.** The
   v3-seed and v4-seed arms use the **identical** v3-strength buckle (`photon_coupling=False` + the same
   director); the only difference is the plant phase advance δ. δ=0.4 (the v2/v3 hard-coded plant) pumps
   H_bel to +4512 and destroys the knot; δ=ω_gap·dt=0.00775 (v4's own rescaled plant) leaves it at +35.79
   and the knot survives. v4's own `seed_omega_known_2_3` docstring (`crystal_graft_v4.py:300-307`) already
   flags δ=0.4 as a **mis-scaled SEED artifact** (implied π_ω ≈ 50× amplitude). So the destruction the lock
   was built to prevent is most consistent with that seed artifact — **surfaced for Grant**, not resolved
   here. Either way the lock verdict is robust: lock-ON ≡ lock-OFF in **both** regimes.
3. **Open question (NOT run — bounded diagnostic, not a v5):** is there ANY buckle strength (e.g. cranked κ̃,
   or a near-yield bulk regime) that destroys a *well-scaled* planted knot via a mode the rigid-rotation lock
   *can* arrest? If not, the lock as-built guards a mode nothing here threatens. Surfaced for the next build.

## Bottom line

The lock-isolation smoke returns **NOT-DEMONSTRATED** as the headline (lock-ON ≡ lock-OFF, knot survives
regardless, in the well-posed regime) and **INERT** under the one arm where the source is actually
destructive (lock-ON ≡ lock-OFF, knot destroyed regardless). Combined with the failed saturation STOP gate
(parent result §4 / ADDENDUM: |L_ω| doubling ratio 5.03/3.97/5.19 ≫ 1.3), the v4 lock is **not** shown to
conserve topology against a destructive source. This is the empirical substrate for the parent result's
demotion to **LOCK-FAIL**.

**Skills fired:** `ave-conserved-vs-pumped` (the lock IS the subject — it neither conserves the knot against
a destructive source nor is needed for survival; it removes a mode orthogonal to the conserved invariant);
`ave-apparatus-floor-attribution` (plant rk=3.697 cells ≥ 3, alias-clean t0=(2,3) — destruction is real, not
extractor floor); `ave-driver-script-honesty` (every number from the EVOLVED field; the only inter-arm
difference is lock_eta; the seed-artifact confound surfaced not buried); `verify-before-cite` (v3 config via
`git show 4627651a`; canary line `crystal_graft_v4.py:348-352`; buckle-defer line `:147-149`);
`flag-don't-fix` (the v3-destruction-is-seed-driven finding + the orthogonal-mode mechanism surfaced for
Grant, not silently reconciled).

**Figure** (`crystal_graft_v4_lock_isolation_fig.png`, data-derived caption): LEFT — planted (2,3) readback,
t0 vs tN, all four arms: w_pol collapses 3→2 in both v3-seed arms (lock OFF and ON alike), holds at 3 in both
v4-seed arms. RIGHT — H_bel(t) (symlog): the lock-ON curve sits exactly on the lock-OFF curve in both regimes
(v3-seed solid, pumping to ~10⁴; v4-seed dashed, bounded ~10²·⁴); legend shows the per-substep lock `|drift|`
max ≈ 1e-16 (machine epsilon) for the lock-ON arms.
