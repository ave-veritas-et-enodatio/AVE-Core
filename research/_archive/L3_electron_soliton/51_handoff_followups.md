# 51 — Handoff: Pair-Creation Follow-Up Hypotheses

**Status:** active handoff (2026-04-22) — for whichever agent/session picks this up
**Parent plan:** `~/.claude/plans/document-list-for-next-chat-compressed-thunder.md` (Stage 4 closeout)
**Most recent state:**
  - [46_vacuum_engine_scope.md §9](46_vacuum_engine_scope.md) — engine as-built summary
  - [50_autoresonant_pair_creation.md](50_autoresonant_pair_creation.md) — Phase III-B v2 final result (A²_cos = 1.009, no centroids)
  - [49_dark_wake_bemf_foc_synthesis.md](49_dark_wake_bemf_foc_synthesis.md) — mechanism synthesis

## 0. TL;DR for the next session

The `VacuumEngine3D` is complete and working. Phase III-B v1 and v2 have been
run. The v2 result reached **A²_cos = 1.009** (above the Axiom-4 rupture
boundary — first numerical instance in AVE-Core) but **no localized
pair-like structures were detected** (0 centroids at `threshold_frac=0.7`).

Three testable hypotheses for why pair creation didn't appear, listed by
cheapness and then expected informativeness. Pick one to start.

---

## 1. Hypothesis H1 — Measurement threshold too strict (CHEAP, ~1 hour)

**The claim:** `threshold_frac=0.7` for `find_soliton_centroids` filters out
real pair structures that exist below 70% of max |ω|². A distributed
"plateau" at max = 1.009 with narrow peaks 0.3-0.5·max would show 0
centroids at current threshold but clear pairs at 0.3 threshold.

**What to do:**

1. Re-run the final v2 sweep config (λ=3.5, amp=0.5, T=0.1) but vary
   `TopologyObserver(threshold_frac=...)` across {0.1, 0.2, 0.3, 0.5, 0.7}.
2. For each threshold, report: max #centroids, final #centroids, centroid
   spatial distribution (are they localized at the collision region x=N/2?
   or scattered across the lattice indicating thermal noise peaks?).
3. Accept H1 if centroids at low threshold are SPATIALLY LOCALIZED near x=N/2
   (= collision center). Reject H1 if low-threshold centroids are distributed
   uniformly (= thermal noise, not pairs).

**Files:**
- Existing: `src/scripts/vol_1_foundations/vacuum_engine_pair_creation_v2.py`
- Modify: change `threshold_frac=0.7` → parameterize + sweep, or just add
  a follow-up `sweep_threshold.py`

**Expected runtime:** ~3 min per config × 5 thresholds = 15 min total.

**If H1 is correct:** we already have pair creation, just couldn't see it.
Update `TopologyObserver` default, re-run v2 headline config with GIF
animation of centroid evolution to communicate the result.

**If H1 is wrong:** move to H2 or H3.

---

## 2. Hypothesis H2 — Spatial geometry matters (MEDIUM, ~4 hours)

**The claim:** Plane-CW sources produce DISTRIBUTED strain over the full
transverse plane. At A²=1, the whole x=N/2 plane saturates as a single
rupture cavity, not 2 distinct pair-core regions. Pair creation in AVE
requires the A²=1 region to be LOCALIZED (point-collision geometry) so that
topological closure can happen at a SPATIAL point, not a plane.

**What to do:**

1. Add a new source type: `PointCollisionSource` — Gaussian-profile point
   source (not a plane wave). Two of these counter-aimed at a central point.
   Keep other parameters identical to Phase III-B v2 (autoresonant, T=0.1).
2. Sweep: 4 λ values × 2 sigma_yz values (narrow beam σ=1, wide beam σ=3) =
   8 configs at amp=0.5, T=0.1.
3. Compare to v2 plane-wave result at matched (λ, amp, T). Does localized
   drive produce localized response?

**Key file edits:**
- `src/ave/topological/vacuum_engine.py`: add `PointCollisionSource` class
  (can subclass `PulsedSource` or `CWSource` with narrow sigma_yz — but
  note that sigma_yz=1 on N=40 lattice = ~2 active sites per plane, may
  have resolution issues)
- `src/scripts/vol_1_foundations/vacuum_engine_pair_creation_v3.py`: new
  sweep script

**Expected runtime:** 8 configs × ~3-5 min = 30-40 min total.

**If H2 is correct:** localized drive → localized rupture → pair creation.
This would be the first clean AVE pair formation demo. Write up doc 52_.

**If H2 is wrong:** spatial geometry doesn't fix it. Move to H3.

---

## 3. Hypothesis H3 — S1 coupling needs augmentation (EXPENSIVE, ~1-3 days)

**The claim:** S1-D coupling `(V²/V_SNAP²)·W_refl(u, ω)` is a MODULATION
coupling (quadratic in Cosserat variables). At (u, ω) near thermal noise
amplitude, the gradient ∂W_refl/∂(u,ω) is small. Even at A²_cos = 1.009,
the coupling drives Cosserat amplitude up but doesn't impose a TOPOLOGICAL
SEED — it only modulates existing structure. To create NEW topological
structure from vacuum, we need a term that's LINEAR in Cosserat variables
(a seed term), OR a boundary condition that imposes (2,3)-winding at the
collision point when A²→1.

**Original proposal location:** [44_pair_creation_from_photon_collision.md §5.2](44_pair_creation_from_photon_collision.md)
lists four options (A: augmented S1 linear term, B: vacuum ZP amplitude
derivation, C: reinterpret K4↔Cosserat identity, D: topological boundary
condition). H3 is Option A from that list.

**What to do:**

1. Re-adjudicate the S1 S-gate: this is a NEW coupling form, requires
   Grant's call. Read [S_GATES_OPEN.md](S_GATES_OPEN.md) for the original
   S1-D decision and doc 44_ §5.2 for augmentation options.
2. If approved: implement `L_c = (V²/V_SNAP²)·W_refl + β·V·(∇·ε_sym)` or
   similar linear term. The β prefactor is a new free parameter requiring
   calibration.
3. Re-run Phase III-B v3 at the final v2 config + new linear coupling.

**Key considerations:**
- **Adds a free parameter** β — violates the "zero new parameters" spirit
  of the S1-D choice. Need strong axiom-native justification.
- **May reopen Rule-6 concerns** — a linear V·(∇·ε) term looks like QED
  minimal coupling; doc 44_ §5.2 explicitly flagged this risk.
- **Alternative routes to the same effect:**
  - Point collision (H2) may give the same localization without new coupling
  - Topological boundary condition (Option D from doc 44_) — impose (2,3)
    winding at collision region when A²>0.9 for >N steps. Discrete "pair
    birth" rule; not Lagrangian-derived but axiomatically consistent with
    Axiom 2 (winding = charge).

**Expected runtime:** 1-3 days depending on depth (coupling implementation,
validation, new sweep, result documentation).

**If H3 is correct:** pair creation requires augmented Lagrangian; this is
a significant physics finding and would redirect the engine design.

**If H3 is wrong:** even augmented coupling doesn't produce pairs. AVE's
electron-creation mechanism is DIFFERENT from what the current engine can
simulate (may require separate machinery, see §5 below).

---

## 4. Recommended order: H1 → H2 → H3

**H1 is cheap insurance.** It's a measurement question, not a physics
question. Even if H1 doesn't solve pair creation on its own, doing it first
reveals WHERE the Cosserat strain localizes at A²=1.009 — which informs
whether H2 or H3 is more likely.

**H2 is the next most physical fix.** Point-collision geometry is what §37
and AVE-PONDER actually describe ("two photons collide LOCALLY"); plane
CW was a convenience of Phase III-B v1 design, not an AVE-native prescription.

**H3 is structural.** Only if H1 and H2 both fail should we consider
changing the coupling form — because that introduces new parameters and
potential Rule-6 risks.

---

## 5. If all three fail: scope broader investigation

If H1 (threshold), H2 (geometry), and H3 (coupling) all fail to produce
localized pair structures, the implication is:

**The current AVE-Core engine reaches A²=1 but not pair creation.**

At that point, the honest path forward is one of:

### 5a. Publish as null result + falsifiable prediction
The σ(ω) results from v1+v2 are already publishable as AVE-native
predictions. The failure to observe pair creation in the coupled K4⊗Cosserat
engine IS a finding — it tells us pair creation requires mechanisms not
currently in the engine. Write a summary paper / document.

### 5b. Consult the corpus for additional mechanisms
Search for AVE-native pair-creation physics we may have missed:
- Vol 2 Ch 5 electroweak / baryon physics (if referenced in corpus)
- Vol 5 organic circuitry (bond-formation mechanisms may be analogous)
- AVE-Fusion nucleosynthesis for early-universe pair physics
- AVE-Metamaterials for SBSL-bubble physics which may have pair creation

### 5c. Return to scoping — is pair creation Phase-1-level work?
Per [00_scoping.md §4](00_scoping.md) and [32_phase3b_axiom_compliant_redesign.md](32_phase3b_axiom_compliant_redesign.md),
there are residual Phase-1 unknowns (n̂↔ω identity, augmented Lagrangian
derivation). Pair creation may require closing those first.

---

## 6. What NOT to do without adjudication

- ❌ Don't change S1 coupling form without Grant's adjudication (it's a
  resolved S-gate, re-opening requires justification)
- ❌ Don't lower centroid threshold below 0.3 without understanding WHY —
  below that, thermal noise peaks will dominate the count
- ❌ Don't use high K_drift (>2.0) without checking stability — autoresonant
  can go unstable at aggressive gains (Stage 4c verified stable through 2.0)
- ❌ Don't thermalize V_inc (`thermalize_V=True`) without T < 5.8×10⁻⁴ ·
  m_e c² (= 3.44×10⁶ K SI) — vacuum-thermal V exceeds V_SNAP above this
  and breaks the simulator physically

---

## 7. Useful existing infrastructure (reuse, don't reinvent)

When implementing H1, H2, or H3, lean on:

- `VacuumEngine3D.from_args(...)` — the top-level entry point
- `PulsedSource`, `CWSource`, `AutoresonantCWSource` — ready-made sources
- `RegimeClassifierObserver`, `TopologyObserver`, `EnergyBudgetObserver`,
  `DarkWakeObserver` — ready-made diagnostics
- `engine.initialize_thermal(T)` — proper thermal init per doc 47_
- `engine.history()` — aggregates all observer data
- `cosserat_field_3d.tetrahedral_gradient` — for K4-native gradients
  (use this instead of `np.gradient` on K4 fields!)
- Existing `saturation_heatmap.py` for spatial visualization of A²

When debugging:

- Check `VacuumEngine3D.snapshot()` — returns regime/topology/energy
  observations for one step
- Look at the K4 active mask — `(even,even,even) | (odd,odd,odd)`
- Use `dark_wake_validation.py` as a template for single-source diagnostic tests
- Use `autoresonant_tuning.py` pattern for parameter sweeps

---

## 8. Session context for the next picker-upper

The 2026-04-22 session took the "AVE Fundamental 3D Vacuum Engine" from
concept → delivered infrastructure → partial physics result in one day.
The commit trail on `research/l3-electron-soliton` branch is:

```
ed6ab8e  docs(Stage 5): update 40_modeling_roadmap.md
4ea5c8a  research(Stage 4d): Phase III-B v2 — doc 50_
aa6670b  feat(Stage 4c): AutoresonantCWSource + tuning
0fa0d7c  feat(Stage 4b): DarkWakeObserver + validation PASS
99e3d64  research(Stage 4a): doc 49_ dark-wake + BEMF + FOC synthesis
be617f1  research(Phase-III-B): σ(ω) sweep v1 — doc 48_
87b502c  fix(thermal): AVE Schwinger-vacuum T_V-rupt = 3.44 MK
afff853  feat(VacuumEngine): fundamental 3D vacuum engine (Stage 2)
fa89466  research(Phase-III): vacuum engine scope + thermal noise
7ad562f  docs: Phase II validation doc — 42_
f99b3b3  feat(AVE-ideal): coupled K4⊗Cosserat simulator — Phase I + II
```

**Branch:** `research/l3-electron-soliton` (working on main repo `AVE-Core`).
Not yet merged to `main`. If merging: `42_`, `46_`, `48_`, `50_` are the
headline research docs; `vacuum_engine.py` is the headline code artifact.

**Artifacts in `/tmp/`** (may not persist between sessions):
- `/tmp/phase_iiib_sweep.npz` — v1 raw data
- `/tmp/phase_iiib_v2_sweep.npz` — v2 raw data
- `/tmp/phase_iiib_sigma_omega.png` — v1 headline plot
- `/tmp/phase_iiib_v2_summary.png` — v2 headline plot
- `/tmp/dark_wake_validation.png` — Stage 4b validation plot
- `/tmp/autoresonant_tuning.png` — Stage 4c K_drift sweep

If these are gone, regenerate by re-running the scripts (they're deterministic
modulo thermal RNG seed).

---

## 9. One-line mission statement for the next session

**"Pair creation in AVE-Core: do the localized structures exist at lower
centroid threshold (H1) or do we need point-collision geometry (H2) before
considering coupling augmentation (H3)?"**

Start with H1. Commit each finding as a separate commit on this branch.
Update [40_modeling_roadmap.md](40_modeling_roadmap.md) log with any new
findings. Write doc 52_ if H1 or H2 produces pair creation.