# MOND Kernel Adjudication — Result (two-kernel SPARC contrast + form-level resolution)

**Date:** 2026-07-20
**Prereg:** [`2026-07-20_mond-kernel-adjudication_prereg.md`](2026-07-20_mond-kernel-adjudication_prereg.md) (frozen-by-push, this branch)
**Driver:** `src/scripts/vol_3_macroscopic/mond_kernel_contrast.py` (banked JSON: `mond_kernel_contrast_results.json`)
**Verdict:** **KERNEL-DEGENERATE-ON-SPARC → form-level resolution → QUADRATIC canonical.** Sweep FIRES.

---

## §0 — Grant's ruling (verbatim [sic]) + interpretation split (preserved)

**Verbatim [sic] (Grant, 2026-07-20):** "6. we fully adjudicate, keeping the one crack simulation in there and cleaning up all mentions of it and the KB and manuscript"

**Interpretation (tagged):** run the two-kernel contrast; keep the correct simulation/kernel as canonical (the one existing SPARC simulation, retained); reconcile every kernel-form mention across KB + manuscript to the adjudicated form. (See prereg §0 for the full split.)

---

## §1 — Verdict per the frozen decision tree

Both kernels run through the IDENTICAL SPARC pipeline (135 galaxies, single canonical `a_0 = c H_∞/(2π) = 1.0719e-10 m/s²`, M*/L=0.5, 1.33× He, r_eval = 5·R_disk). The two arms differ in EXACTLY one factor: `S_quad = √(1−(g_N/a_0)²)` (canonical engine, byte-untouched) vs `S_lin = √(1−g_N/a_0)` (research variant).

**PRIMARY (gating) = Q=1 mean |residual| (N=87):**

| Kernel | Q=1 mean\|res\| | Δ (lin − quad) | frozen τ | Gate |
|---|---|---|---|---|
| QUADRATIC (canonical) | **11.476%** | — | — | — |
| LINEAR (variant) | **10.834%** | **−0.642%** | 1.020% | \|Δ\| < τ |

`|Δ| = 0.642% < τ = 1.020%` → **KERNEL-DEGENERATE-ON-SPARC.** The primary metric does not resolve the two kernels against the Q=1 galaxy-to-galaxy scatter. Per the frozen tree (prereg §4), a DEGENERATE verdict routes to §5 form-level grounds. **The HARD GATE did NOT fire** — the linear arm did not win by ≥ τ (it is sub-threshold), so this is a degeneracy, not a linear win; no STOP-to-Grant is triggered.

**SECONDARY (disclosed, NON-gating) — full statistics, both arms:**

| Bin (n) | quad mean\|res\| | lin mean\|res\| | quad RMS | lin RMS |
|---|---|---|---|---|
| ALL (135) | 15.51% | 14.75% | 27.17% | 26.47% |
| Q=1 (87) | 11.48% | 10.83% | 14.90% | 14.28% |
| Q=2 (42) | 15.45% | 14.54% | 25.36% | 24.55% |
| Q=3 (6) | 74.30% | 73.11% | 94.40% | 92.86% |

Quadratic all-sample (15.51% / 27.17% / median +4.89%) reproduces the banked headline exactly. `r = g_N/a_0` at eval spans [0.0033, 1.2762] (mostly ≪ 1 — deep MOND).

---

## §2 — Form-level resolution (the decisive ground; frozen pre-run in prereg §5)

Because SPARC is DEGENERATE, adjudication is settled on which form the Axiom-4 derivation forces:

- **The leaf's own amplitude identification forces the QUADRATIC.** `effective-galactic-acceleration-mond.md:10` and `vol3/claim-quality.md:260` (clm-u86caq) both state `g_N` is the saturation amplitude and `a_0` the yield limit. Substituting A=g_N, A_yield=a_0 into the canonical Axiom-4 kernel `S(A)=√(1−(A/A_yield)²)` (INVARIANT-S2; `universal_operators.py:81`) gives `√(1−(g_N/a_0)²)` — the QUADRATIC. The displayed LINEAR equation at :15 contradicts the leaf's own setup.
- **Maxwell small-A discriminator kills the linear route** (`research/2026-07-02_axiom4-buckling-kernel_result.md:21`): the quadratic's `1−A²/2` small-amplitude onset recovers Maxwell; the linear's `1−A` would break Maxwell recovery. The only way to justify the linear form is to redefine the amplitude as A∝√g_N (strain∝√g_N narrative, `galactic_rotation.py:167`), which contradicts the leaf's explicit "g_N serves as the saturation amplitude."
- **The shipped engine already computes the quadratic** (`galactic_rotation.py`→`saturation_factor`→`universal_saturation`). Adopting the quadratic as canonical requires **zero engine change** — only the KB/tex text (which misstated the form) is corrected.

**Adjudicated canonical form:** `g_eff = g_N + √(g_N·a_0)·√(1 − (g_N/a_0)²)`.

---

## §3 — Honest nuance (flag-don't-fix; does NOT flip the verdict)

The linear arm is *nominally* lower than the quadratic across **every** bin (Q=1 −0.64%, all-sample −0.76%, Q=2 −0.91%, Q=3 −1.19%). This is sub-threshold (< τ) on the gating metric and is **not** clean evidence for the linear kernel shape, for a stated physical reason: `S_lin ≤ S_quad` on 0<r<1, so the linear kernel produces LESS drag → LOWER v_AVE. The quadratic over-predicts (all-sample mean residual +7.73%, median +4.89%), so *any* reduction in predicted velocity mechanically lowers |residual| here. The nominal linear edge is therefore **confounded with the overall normalization bias** (absorbable within M*/L and a_0 uncertainties), not a discrimination of kernel shape. This reinforces the DEGENERATE verdict: SPARC at 5·R_disk (deep MOND, r≪1, both kernels → 1) cannot separate kernel shape from normalization at this precision. The adjudication rests on §2 (axiom-forced quadratic), NOT on an empirical quadratic win — stated transparently so the reader does not mistake this for the quadratic beating the linear on the data (it did not).

---

## §4 — Corpus sweep (FIRED) — executed sites + NOT-SWEPT list + D7 closure

Sweep gated on verdict = DEGENERATE-with-form-level-resolution → QUADRATIC (per prereg §6). Rule-12 KEEP-BOTH dated corrections (original preserved; corrected form + dated note added) to the adjudicated QUADRATIC form.

**SWEPT — KB markdown (9 statement-sites across 8 files):**
1. `manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/effective-galactic-acceleration-mond.md:15` — leaf resultbox; co-located D7 flag closed with receipt (below).
2. `manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/dm-mechanism-unification.md:48`
3. `manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/asymptotic-limits.md:11` (form-specific parenthetical; qualitative evanescent claim at r≥1 preserved — both radicals vanish at r≥1)
4. `manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/index.md:19`
5. `manuscript/ave-kb/vol3/cosmology/index.md:23`
6. `manuscript/ave-kb/vol3/index.md:45`
7. `manuscript/ave-kb/vol3/claim-quality.md:260` (clm-u86caq) + `:265`
8. `manuscript/ave-kb/common/divergence-test-substrate-map.md:275` + `:486`

**SWEPT — manuscript tex (1 file):**
9. `manuscript/vol_3_macroscopic/chapters/05_cosmology_dark_sector.tex:43-44` (resultbox) + `:54` (parenthetical). pdflatex-rebuilt.

**FLAGGED, NOT SWEPT — engine-code (byte-untouched per discipline; routed):**
- `src/ave/regime_3_saturated/galactic_rotation.py:130-131,141,163,202` — docstrings/comments state LINEAR while the code computes QUADRATIC (via `saturation_factor`). Documentation-vs-computation mismatch; computation already correct. Left byte-untouched (engine-byte discipline); routed to a follow-on engine-docstring-hygiene pass.
- `src/scripts/vol_3_macroscopic/derive_bullet_cluster_offset.py:31` — docstring linear form (driver script docstring; same routing).
- `src/ave/gravity/galactic_mond_drag.py` — internally CONSISTENT (docstring :44 + code :49 both quadratic); no correction needed.

**#738 / S4-5 / D7 flag closure:**
- `effective-galactic-acceleration-mond.md:20-24` — the 2026-07-19 CONTRADICTION FLAG → RESOLVED-with-receipt closure note added, citing this contrast run + the form-level finding (landed at the leaf by implementer).
- `_orchestration/2026-07-10_rulings-docket.md:2000` + `_orchestration/2026-07-19_branch-scrub-inventory.md:206-210` — process record of the flag; closure pointer SURFACED for the orchestrator (not landed here — process-tracking lane).

---

## §5 — Deviations + contradictions (flag, don't fix)

- **DEVIATION (cite-precision, surfaced in prereg §1):** the standing flag + docket cite the headline engine as `galactic_mond_drag.py:49`; the SPARC headline actually rode `galactic_rotation.py`→`saturation_factor`→`universal_saturation` (also quadratic). Both engines compute the quadratic, so the flag's substance holds; the cite is corrected in the swept leaf.
- **DEVIATION (SPARC data provenance):** `data/SPARC/*.mrt` is gitignored/absent in the worktree; copied from the main checkout `/Users/grantlindblom/AVE-staging/AVE-Core/data/SPARC/` (identical file, byte-copy) to run. No data modified.
- **DEVIATION (engine docstrings not swept):** per the engine-byte-untouched discipline, the LINEAR docstrings in `galactic_rotation.py` + `derive_bullet_cluster_offset.py` are FLAGGED not edited, even though Grant's ruling says "clean up all mentions." Surfaced for a Grant/auditor call on whether a docstring-only (zero-computation) correction is in-scope.
- **CONTRADICTION (flagged, resolved by adjudication):** leaf-form LINEAR vs engine-computation QUADRATIC — resolved to QUADRATIC via the frozen tree (DEGENERATE-on-SPARC + axiom-forced form). Both original statements preserved (Rule-12 KEEP-BOTH); no engine kernel edited.
- **No adjudication-criterion drop:** τ, primary metric, and tree are exactly as frozen in the pushed prereg. The nominal sub-threshold linear edge was NOT used to convert the verdict.


---
**Errata + follow-on framing (2026-07-20, review repairs R2/R3 — the frozen prereg is NOT edited):**
- *R2 (cite erratum):* prereg §5.2 and §2 above cite `galactic_rotation.py:167-168` for the "strain ∝ √g_N narrative"; `:167-168` is the code line — the narrative sentence sits at `galactic_rotation.py:136`. Non-load-bearing (the narrative demonstrably exists); recorded here rather than editing the frozen prereg.
- *R3 (follow-on framing):* the routed engine-docstring-hygiene follow-on is a **physics reconciliation, not a typo fix** — the `:136` "strain proportional to √(g_N)" sentence encodes the COMPETING amplitude identification (A∝√g_N → the retired linear kernel). Per this adjudication the canonical identification is **A = g_N** (leaf-setup-forced + code-computed); the docstring corrects TOWARD g_N. A future "fix" aligning the equation to the √g_N narrative would silently re-introduce the linear kernel. The substrate-level question (is the drag keyed on the acceleration itself, or on a strain ∝ √g_N?) is SURFACED TO GRANT as an open walk item — this adjudication canonicalizes the leaf's own identification, it does not derive it.
- *Wording note:* the derived/index sites were corrected IN-PLACE (git carries the originals, per the audit-trail-in-git directive) — "Rule-12 KEEP-BOTH" applies strictly only at the leaf, where the retired form is quoted in the RESOLVED note.
- *Sweep scope disclosure (R1):* `research/` docs were outside the ruled sweep scope ("the KB and manuscript"); the known residual `research/2026-07-10_collapse-target-registry.md:260` now carries a dated adjudication pointer.
