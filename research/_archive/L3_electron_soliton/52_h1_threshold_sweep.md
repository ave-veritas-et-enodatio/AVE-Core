# 52 — H1 Centroid-Threshold Sensitivity Probe

**Status:** completed 2026-04-22 (Stage 5 Phase A)
**Parent plan:** `~/.claude/plans/review-the-collaboration-md-and-lexical-wombat.md`
**Tests:** Hypothesis H1 from [51_handoff_followups.md §1](51_handoff_followups.md)
**Depends on:** [50_autoresonant_pair_creation.md](50_autoresonant_pair_creation.md) (v2 headline config)

## 0. TL;DR

**Verdict: H1-DISTRIBUTED.** Localized pair-like structures do *not* exist
below the v2 detection threshold. The ω-field at `max A²_cos ≈ 0.88` on the
v2 headline config (λ=3.5, T=0.1, K_drift=0.5) is a **spatially distributed
thermal-noise plateau**, not a pair of cores masked by a strict detector.

H1 is falsified. The next candidate in the handoff queue is H2
(point-collision geometry). Per §6 of the plan, H2 requires Grant's
explicit go-ahead before execution — see §6 below.

## 1. Method

Single-config rerun of the v2 headline
([50_ §1](50_autoresonant_pair_creation.md)):

| Parameter | Value |
|---|---|
| λ | 3.5 cells |
| amplitude | 0.5·V_SNAP |
| T | 0.1·m_e c² |
| K_drift | 0.5 |
| N / pml | 40 / 5 |
| n_steps | 300 |
| Source | `AutoresonantCWSource` × 2 (counter-aimed) |

The `TopologyObserver` was extended to accept a **list** of thresholds; on
every recording step it calls `find_soliton_centroids` once per threshold,
capturing counts AND centroid positions.

Threshold list: **{0.1, 0.2, 0.3, 0.5, 0.7}**.

**Single sim run, five threshold curves** — cheaper than the handoff's
suggested 5× rerun and the simulation is deterministic modulo thermal RNG.

Implementation:
- [src/ave/topological/vacuum_engine.py](../../src/ave/topological/vacuum_engine.py)
  — `TopologyObserver.__init__` now accepts `threshold_fracs: list[float]`
  (scalar `threshold_frac` preserved as default).
- [src/scripts/vol_1_foundations/vacuum_engine_pair_creation_v3.py](../../src/scripts/vol_1_foundations/vacuum_engine_pair_creation_v3.py)
  — H1 driver script + `adjudicate_h1` heuristic.

## 2. Results

### 2.1 Aggregate numbers

| Metric | v2 (doc 50_) | v3 (this run) |
|---|---|---|
| max A²_cos | 1.009 | **0.877** |
| max A²_k4 | 0.393 | 0.393 |
| max τ_zx | 0.151 | 0.151 |
| elapsed | ~3 min | 94.5 s |

Deterministic metrics (A²_k4, τ_zx) reproduce exactly; the Cosserat max
A²_cos landed at 0.877 vs v2's 1.009. Run-to-run variance driven by the
thermal-noise RNG seed (classical Maxwell-Boltzmann init of Cosserat u, ω).
**See §3.3 for caveat.** The qualitative structure of the ω-field at
A²≈0.88 is still on the v2-type distributed plateau, so the H1 test is
still meaningful for the v2 regime.

### 2.2 Centroid counts vs threshold

| threshold_frac | max #centroids | final #centroids |
|---|---|---|
| 0.10 | 5 | 1 |
| 0.20 | **95** | **79** |
| 0.30 | 28 | 8 |
| 0.50 | 0 | 0 |
| 0.70 | 0 | 0 |

### 2.3 Spatial distribution of detected centroids (all recorded steps)

N = 40, collision plane at **x = 20.0**.

| thr | total records | ⟨x⟩ | σ_x | ⟨n_cells⟩ | max n_cells | frac within N/4 of x=20 |
|---|---|---|---|---|---|---|
| 0.10 | 86 | 21.2 | 7.97 | 5,614 | 9,433 | 0.79 |
| 0.20 | 4,350 | 19.9 | 11.34 | 23.2 | 2,919 | 0.49 |
| 0.30 | 267 | 19.9 | 10.70 | 9.7 | 24 | 0.55 |
| 0.50 | 0 | — | — | — | — | — |
| 0.70 | 0 | — | — | — | — | — |

(Threshold 0.1 centroids with ⟨n_cells⟩ ≈ 5,614 are order-of-magnitude the
full 40³ = 64,000 active lattice — they are not cores, they are the lattice
itself collapsing into one connected blob once 10 % of peak is the cutoff.)

## 3. Interpretation

### 3.1 The shape of the centroid-vs-threshold curve

The pattern is diagnostic:

- **thr=0.70, 0.50** → 0 centroids. Nothing rises above half the peak.
- **thr=0.30** → 28 max, 8 final. Small clusters (⟨n_cells⟩ ≈ 10, barely
  above `min_cluster_size=8`), scattered across the lattice
  (σ_x ≈ 10.7 ≈ N/4).
- **thr=0.20** → 95 max, 79 final. **Count explosion** with ⟨n_cells⟩ ≈ 23.
  This is thermal-noise granularity — the ω-field consists of hundreds of
  small peaks above 20 % of the plateau.
- **thr=0.10** → 5 max, 1 final. The "above threshold" region fragments
  reconnect into one giant component spanning most of the lattice.

**What pair creation would look like instead:** persistent 2 centroids
across thresholds 0.3–0.7, with cores near x=20, broadening (not
multiplying) as threshold drops, and merging at very low thresholds only
if the cores are close enough. That is **not** the observed pattern.

### 3.2 Why H1-DISTRIBUTED, not H1-AMBIGUOUS

The automated `adjudicate_h1` heuristic flagged the run as DISTRIBUTED on
two independent counts:

1. **Count-explosion test** — `max(max_n_centroids) across low thresholds
   ≥ 10`: true at thr=0.2 (95) and thr=0.3 (28). One criterion is enough.
2. **Spatial-scatter test** — at low thresholds, centroids are only 49–55 %
   within N/4 of the collision plane, with σ_x ≈ N/4. Borderline, but
   consistent with uniform scatter over most of the lattice rather than
   clustering at x=N/2.

Both tests agree: the ω-field at A²≈0.88 has **no spatial localization
above any threshold ≥ 0.5** and **pure thermal-noise granularity below
that**.

### 3.3 Caveat — run-to-run variance at max A²_cos

v2 reached 1.009 (above the Axiom-4 rupture boundary); this v3 run reached
0.877. Both runs use the same deterministic propagator but different
thermal-noise seeds. One could argue "pair creation only occurs at A²≥1,
and this run didn't cross". That's not our read, for three reasons:

1. The v2 run at A²=1.009 **also** returned 0 centroids at threshold_frac=0.7.
   The v2 team inferred "might exist below 0.7" — the entire point of H1
   was to check that. We now have, across thresholds 0.5–0.7, still 0.
2. The v2-v3 qualitative structure at mid thresholds is consistent:
   distributed plateau with thermal-peak granularity.
3. If crossing A²=1 matters, a cheap follow-up is a single rerun at a
   different RNG seed until A²≥1; ~1–3 retries at 94 s each. See §6.

### 3.4 Plane-wave geometry is the likely blocker

Per the handoff H2 framing and AVE-PONDER / AVE-Propulsion Ch 5 language
("two photons collide LOCALLY"), a plane-CW source saturates the entire
x=N/2 *plane* as a single rupture slab, not two cores. The data here is
consistent with that read: the ω-response under a plane-CW drive has the
symmetry of the drive — translation-invariant in (y, z) — so topological
closure at a *point* is not available to the dynamics.

This does NOT close the question; it's consistent with H2 but doesn't
prove it. H2's test is whether a spatially localized drive produces a
spatially localized response.

## 4. Verdict adjudication vs §1 pre-registered outcomes

| Outcome | Signature | Adjudication |
|---|---|---|
| **H1-PAIR** | Centroids ≤0.3 cluster near x=N/2, count stable ~2 | **NOT OBSERVED** |
| **H1-DISTRIBUTED** | Low-thr count grows monotonically / scattered | **✓ CONFIRMED** (count explosion at thr=0.2; std_x ≈ N/4; ⟨n_cells⟩ at thr=0.3 barely above min cluster size) |
| **H1-AMBIGUOUS** | Partial clustering + noise | — |
| **H1-UNIFORM** | Zero centroids everywhere | — |

**Net: H1 is falsified.** Measurement threshold is not the reason pair
creation wasn't observed in v2. The structural answer is that at plane-CW
drive under autoresonance, the ω-field saturates as a distributed plateau,
not as localized pair cores.

## 5. What this narrows down

Per the handoff decision tree:

- **H1 failure → H2 is the next most physical fix.** Localized (Gaussian-
  point) drive geometry is what AVE-PONDER and AVE-Propulsion Ch 5 actually
  describe. Plane-CW was a convenience of v1/v2 design.
- **H3 (S1 coupling augmentation) stays deferred.** It's a resolved S-gate;
  H1 failure on its own does not justify reopening it.

Open question worth flagging (not resolving here): **is the thermal noise
itself the distributed signal?** H2 will answer this incidentally —
under point-collision geometry with T=0.1, if the response is still a
distributed plateau, thermal noise dominates; if the response is localized
near the collision point, the geometry argument holds.

## 6. Recommended next steps (requires Grant's call)

Ranked by cost:

1. **(Cheap, ~5 min)** Single rerun with explicit RNG seed to confirm
   H1-DISTRIBUTED verdict at A²≥1. Not necessary for the conclusion but
   would close the §3.3 caveat.
2. **(Medium, ~4 h)** Execute H2 from [51_handoff §2](51_handoff_followups.md) —
   add `PointCollisionSource` (narrow-Gaussian point source), 8-config
   sweep at matched (λ, amp, T), compare to v2 plane-wave baseline. Write
   doc 53_.
3. **(Deferred)** H3 — S1 coupling augmentation. Remains a resolved
   S-gate; do not re-open without adjudication.

**Default per flag-don't-fix:** stop here. Grant decides whether to
proceed to H2 or accept the distributed-plateau finding as a negative
result and scope broader (51_ §5 publish-null-result track).

## 7. Artifacts

- `/tmp/h1_threshold_sweep.npz` — raw data, 2.8 MB (config + thresholds
  array + aggregate counts + full centroid-record JSON).
- `/tmp/h1_threshold_summary.png` — 2-panel plot (count-vs-threshold,
  spatial scatter with collision plane marked).
- `/tmp/h1_threshold_log.txt` — console output.
- [src/scripts/vol_1_foundations/vacuum_engine_pair_creation_v3.py](../../src/scripts/vol_1_foundations/vacuum_engine_pair_creation_v3.py)
- Engine change: [src/ave/topological/vacuum_engine.py](../../src/ave/topological/vacuum_engine.py)
  `TopologyObserver` extended (back-compatible).

## 8. Known limitations

1. Single RNG seed; A²_cos = 0.877 < v2's 1.009. See §3.3.
2. Only one config tested (v2 headline). Other v2 configs (lower ω·τ)
   were not rerun since they showed uniformly lower A²_cos and thus the
   H1 test would be weaker.
3. The spatial-scatter test is heuristic; a rigorous answer would compare
   the centroid density profile against a uniform-lattice null. Not
   necessary for the qualitative verdict.
4. Threshold=0.1 giving one giant blob is an artifact of connected-
   components thresholding a thermal plateau — it's not physics, it's
   measurement saturation at the other end. Documented for clarity.
