# MOND Kernel Adjudication — Two-Kernel SPARC Contrast (PREREG, frozen-by-push)

**Date:** 2026-07-20
**Branch:** `feat/mond-kernel-adjudication` (worktree off `origin/main` @ `64f1894d`)
**Lane:** implementer (MOND kernel adjudication)
**Status at freeze:** FROZEN. This document is pushed BEFORE the linear-vs-quadratic contrast is computed. The quadratic (canonical-engine) baseline is reproduced here solely to compute the frozen decision threshold; the LINEAR contrast number is not computed until after this prereg is pushed.

---

## §0 — Grant's ruling (verbatim [sic]) + interpretation split

**Verbatim [sic] (Grant, 2026-07-20):**

> "6. we fully adjudicate, keeping the one crack simulation in there and cleaning up all mentions of it and the KB and manuscript"

**Interpretation (tagged as interpretation, not verbatim):** run the two-kernel contrast through the identical SPARC pipeline; keep the correct simulation/kernel as canonical (the "one crack simulation" read as the single existing canonical galactic-rotation SPARC simulation — keep it in the repo, do not fork a second engine); then reconcile ("clean up") every stated kernel-form mention across the KB and the manuscript (tex) to the adjudicated form. The interpretation resolves an ambiguity in "the one crack simulation" — read as the one existing SPARC simulation to be retained, with the textual kernel-form mentions swept to match it. Where "crack" vs "correct" is at issue, the physics decision is made by the frozen tree in §4, not by the wording.

---

## §1 — The contradiction (content-verified receipts)

The MOND drag-kernel functional form appears in two mutually inconsistent shapes:

- **LINEAR-in-ratio** (KB leaf + manuscript tex): `manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/effective-galactic-acceleration-mond.md:15` (verbatim):
  `g_{eff} \;=\; g_N + \sqrt{g_N \cdot a_0}\; \sqrt{1 - \frac{g_N}{a_0}}` — kernel factor `√(1 − g_N/a_0)`.
- **QUADRATIC-in-ratio** (engine computation): the canonical Axiom-4 kernel `S(A)=√(1−(A/A_yield)²)`.

**Which engine actually produced the banked 11.5% Q=1 headline (content-verified):**
- The banked headline (`multi-galaxy-validation.md:12,14`) attributes the SPARC 135-galaxy / 11.5% Q=1 result to `src/scripts/vol_3_macroscopic/sparc_catalog_ingest.py`.
- `sparc_catalog_ingest.py:47-51,158` calls `ave.regime_3_saturated.galactic_rotation.ave_rotation_velocity`.
- `galactic_rotation.py:190,164` → `ave_saturation_acceleration` → `saturation_factor(g_N, a0)` (`scale_invariant.py:107,154`) → `universal_operators.universal_saturation` (`universal_operators.py:75,81,112,115`), which computes `S(A)=√(1−(A/A_yield)²)` — the **QUADRATIC**. Reproduced live 2026-07-20 (§3): Q=1 mean|residual| = 11.476% (≈ banked 11.5%).

**Flag-don't-fix note on the standing flag's cite (surfaced, not fixed):** the standing #738/S4-5 flag (`effective-galactic-acceleration-mond.md:20-24`, docket `_orchestration/2026-07-10_rulings-docket.md:2000`, branch-scrub `_orchestration/2026-07-19_branch-scrub-inventory.md:206-210`) cites the engine as `src/ave/gravity/galactic_mond_drag.py:49` (`np.sqrt(1.0 - r**2)`). That file is real and quadratic, but it is used by `simulate_galactic_rotation_curve.py` (5-galaxy demo) + `generate_manuscript_figures.py`, **not** by the SPARC headline pipeline. The SPARC headline rode `galactic_rotation.py`→`saturation_factor`→`universal_saturation` (also quadratic). Both quadratic engines exist; the flag's substance (leaf=linear, headline-engine=quadratic) holds under either cite. This prereg cites the actual SPARC path; the discrepancy is a cite-precision correction, not a change of substance.

---

## §2 — Contrast protocol (frozen)

1. **Both kernels through the IDENTICAL SPARC pipeline.** A research driver `src/scripts/vol_3_macroscopic/mond_kernel_contrast.py` **imports** `parse_sparc_table1`, `baryonic_mass_kg`, the `KPC`/`ML_RATIO_36`/`HE_CORRECTION` constants, and the `GalaxyModel` + `A0_LATTICE` from the existing pipeline (`sparc_catalog_ingest.py` + `ave.regime_3_saturated.galactic_rotation`). Same 135-galaxy parse, same M*/L=0.5, same 1.33× He, same r_eval = 5 R_disk, same single canonical `a_0 = c H_∞/(2π)`.
2. **QUADRATIC arm = canonical engine, byte-untouched.** Uses `ave_rotation_velocity` unchanged (the shipped `ave_saturation_acceleration` → quadratic `S`).
3. **LINEAR arm = research-only variant, engine byte-untouched.** The driver defines a local `_v_ave_linear()` that reuses the canonical `g_N = galaxy.newtonian_acceleration(r)` and the canonical `g_drag = √(g_N·a_0)·S`, but substitutes `S_lin = √(max(1 − g_N/a_0, 0))` for `S_quad`. No `src/ave/**` file is modified. This isolates the ONLY difference to the kernel factor `S_lin` vs `S_quad`.
4. **All diagnostics driver-computed** (no hand numbers). Output = a JSON + printed table banking both arms' full statistics.

---

## §3 — Frozen metrics

- **PRIMARY (gating):** Q=1 mean |residual| — the banked headline's own metric. Banked/reproduced quadratic value = **0.114765 (11.476%)** on N=87 Q=1 galaxies (live-reproduced 2026-07-20 via the canonical driver — the headline's "11.5%").
- **SECONDARY (disclosed, NON-gating):** all-sample (135) mean |residual|, RMS residual, median residual; per-Q binning (Q=1/2/3). Reproduced quadratic all-sample = mean|res| 15.51%, RMS 27.17%, median +4.89% (matches banked). These are reported for both arms but do NOT enter the decision rule.

---

## §4 — Frozen decision rule (with DEGENERATE bin + HARD GATE)

**Threshold basis (computed INSIDE this prereg, on the quadratic baseline only, before the contrast):** the frozen degeneracy threshold **τ = jackknife (leave-one-out) SE of the Q=1 mean|residual| under the canonical quadratic kernel**. Computed 2026-07-20 (`scratchpad/threshold_basis.py`, quadratic pipeline only):

```
N (Q=1)                      = 87
Q=1 mean|residual| (quad)    = 0.114765  (11.476%)
jackknife SE of that mean    = 0.010198  (1.020%)   ← FROZEN τ
analytic SEM cross-check     = 0.010198  (1.020%)   (identical, as expected for a mean)
```

**τ = 1.020% (0.010198).** Rationale: τ is the sampling spread of the primary metric itself — a kernel-form change that moves the Q=1 mean|residual| by less than one jackknife-SE is not resolvable against galaxy-to-galaxy scatter on this dataset, so it is a genuine degeneracy, not a preference.

Let `Δ = Q1_linear − Q1_quadratic` (both = Q=1 mean|residual|; lower is better).

- **DEGENERATE bin:** if `|Δ| < τ (1.020%)` → verdict **KERNEL-DEGENERATE-ON-SPARC**. The primary metric does not discriminate; adjudication routes to §5 form-level grounds (which form the Axiom-4 derivation actually forces).
- **QUADRATIC wins:** if `Δ ≥ +τ` (linear has HIGHER mean|residual| by ≥ τ, i.e. quadratic is better) → **QUADRATIC canonical**; proceed to Stage-3 corpus sweep.
- **★HARD GATE — LINEAR wins:** if `Δ ≤ −τ` (linear has LOWER mean|residual| by ≥ τ, i.e. linear is better) → **STOP.** Bank the contrast, do NOT touch the engine, do NOT re-bank the 11.5% headline, do NOT run the sweep. Route to Grant: an engine change + headline re-bank is his call (the shipped engine computes the quadratic).

**A-priori structural note (fair to state pre-contrast; a property of the observable, not the contrast):** the SPARC benchmark evaluates at r_eval = 5·R_disk, deep in the MOND regime where g_N ≪ a_0, so r = g_N/a_0 ≪ 1. There, `S_quad = √(1−r²) ≈ 1 − r²/2` and `S_lin = √(1−r) ≈ 1 − r/2` both → 1, differing only at O(r). The two kernels are therefore expected to be nearly degenerate on the primary metric. This is stated to disclose the expectation honestly; the run in Stage 2 decides.

---

## §5 — Derivation-side check (which form is axiom-forced)

Traced the leaf's own derivation chain + the doc-48/#59 provenance context:

1. **The leaf's own amplitude identification forces the QUADRATIC.** `effective-galactic-acceleration-mond.md:10` (prose): "When local Newtonian acceleration `g_N` serves as the saturation amplitude (with `a_0` as the yield limit)". `vol3/claim-quality.md:260` (clm-u86caq): "the Axiom 4 saturation operator with `g_N` as the saturation amplitude and `a_0` as the yield limit." Substituting A = g_N, A_yield = a_0 into the canonical Axiom-4 kernel `S(A) = √(1 − (A/A_yield)²)` (`ave-kb/CLAUDE.md` INVARIANT-S2; `universal_operators.py:81`) gives `S = √(1 − (g_N/a_0)²)` — the **QUADRATIC**. The displayed LINEAR equation at :15 contradicts the leaf's own stated amplitude identification.
2. **The only route to the LINEAR form redefines the amplitude as A ∝ √g_N** (strain ∝ √g_N — the narrative in `galactic_rotation.py:167-168` docstring). That contradicts the leaf's explicit "g_N serves as the saturation amplitude" and the claim-quality entry. It is not the leaf's own stated setup.
3. **Corroborating discriminator (`research/2026-07-02_axiom4-buckling-kernel_result.md:21`):** the quadratic √(1−A²) is the geometrically-forced kernel (inextensible-rod tip projection); the Maxwell small-A limit (1 − A²/2) is a *discriminator that kills* the linear (Euler) route (1 − A would break Maxwell recovery). Applied with A = g_N/a_0: the quadratic gives Maxwell-recovery small-g_N onset; the linear would break it.
4. **#59 (Q-EMBED-SEL-1) provenance context** (`_orchestration/index.md:620`, `2026-05-31_q-embed-sel-1-evaluation.md`): the Axiom-4 self-saturation kernel used cross-particle is the quadratic `S(A)=√(1−A²)` throughout; no linear-in-ratio variant is a derived object anywhere in the #59 chain.

**Derivation-side finding (decisive):** the QUADRATIC `√(1−(g_N/a_0)²)` is the axiom-forced form given the leaf's own amplitude identification + the canonical Axiom-4 kernel. The LINEAR form is a transcription that is inconsistent with the leaf's own prose and with INVARIANT-S2. This is stated pre-run so it cannot be tuned to the contrast; it is the resolution the DEGENERATE bin routes to.

---

## §6 — Stage-3 corpus sweep inventory (FROZEN; gated on §4 verdict = QUADRATIC-wins OR DEGENERATE-with-form-resolution)

Two-method enumeration (grep on both `1 - g_N/a_0` markdown and `1 - \frac{g_N}{a_0}` tex spellings + a `g_{eff} = g_N + \sqrt` structural grep). Sites carrying the LINEAR form to be Rule-12 dated-corrected to QUADRATIC:

**KB markdown (SWEEP scope):**
1. `manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/effective-galactic-acceleration-mond.md:15` — THE leaf resultbox (Rule-12 KEEP-BOTH; the co-located CONTRADICTION FLAG at :20-24 gets its RESOLVED-with-receipt closure citing this contrast).
2. `manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/dm-mechanism-unification.md:48`
3. `manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/asymptotic-limits.md:11` (the "(1 − g_N/a_0)" parenthetical; the qualitative evanescent claim at r≥1 survives — both radicals go imaginary at r≥1 — only the parenthetical form changes)
4. `manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/index.md:19`
5. `manuscript/ave-kb/vol3/cosmology/index.md:23`
6. `manuscript/ave-kb/vol3/index.md:45`
7. `manuscript/ave-kb/vol3/claim-quality.md:260` (clm-u86caq entry) + `:265` (radical form)
8. `manuscript/ave-kb/common/divergence-test-substrate-map.md:275` and `:486` (C13a row, twice)

**Manuscript tex (SWEEP scope):**
9. `manuscript/vol_3_macroscopic/chapters/05_cosmology_dark_sector.tex:43-44` (resultbox) + `:54` (evanescent parenthetical). pdflatex rebuild required after edit.

**FLAGGED, NOT SWEPT (engine-code — byte-untouched per discipline; routed to a separate engine-doc-hygiene pass / Grant):**
- `src/ave/regime_3_saturated/galactic_rotation.py:130-131,141,163,202` — docstrings/comments state the LINEAR form while the code computes the QUADRATIC (via `saturation_factor`). Documentation-vs-computation mismatch; computation is already correct. Not edited here (engine byte-untouched).
- `src/scripts/vol_3_macroscopic/derive_bullet_cluster_offset.py:31` — docstring linear form.
- `src/ave/gravity/galactic_mond_drag.py` — internally CONSISTENT (docstring :44 AND code :49 both quadratic); no correction needed.

**#738/S4-5/D7 flag closure sites (LIST; canonical closure lands at the leaf, process-tracker updates surfaced for orchestrator):**
- `effective-galactic-acceleration-mond.md:20-24` — CONTRADICTION FLAG blockquote → RESOLVED-with-receipt closure (implementer lands, at the leaf).
- `_orchestration/2026-07-10_rulings-docket.md:2000` and `_orchestration/2026-07-19_branch-scrub-inventory.md:206-210` — process record of the flag; closure pointer surfaced for the orchestrator (not landed by implementer — process-tracking lane).

Any site discovered during execution not on this list is added to the result doc's site inventory with an honest NOT-PRE-ENUMERATED tag.

---

## §7 — Precedence + Rule 11

- **Precedence:** the frozen §4 tree + §3 primary metric take precedence over any post-hoc reading. The §5 derivation finding is frozen pre-run and is the DEGENERATE-bin resolution; it is not permitted to override a HARD-GATE LINEAR-wins empirical result (that STOPs and routes to Grant regardless).
- **Rule 11 (honest closure):** if the HARD GATE fires (linear wins), that is a clean result — bank it, name the mechanism, STOP, route to Grant. No debugging toward a quadratic rescue.
- **Rule 12 (substitution-not-retraction):** the corpus sweep preserves each original LINEAR statement (KEEP-BOTH) and adds the dated correction; it does not delete the historical form.
- **No adjudication-criterion drop post-hoc:** τ, the primary metric, and the tree are frozen by this push.
