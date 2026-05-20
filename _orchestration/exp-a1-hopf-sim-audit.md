# EXP-A1-HOPF — Sim Audit (α + (p,q) + C8 cross-comparison vs AVE-Core canon)

**Parent epic**: [`exp-a1-hopf.md`](exp-a1-hopf.md)
**Phase A repo audit**: [`exp-a1-hopf-repo-audit.md`](exp-a1-hopf-repo-audit.md) (425 lines, 8-axis structural sweep)
**Audit type**: Read-only sim drift comparison — HOPF predictions vs current AVE-Core canon
**Audit date**: 2026-05-20 EOD+
**AVE-Core branch at audit**: `analysis/integration` @ `17602c3`
**AVE-HOPF branch at audit**: `analysis/a1-hopf-audit-walkback-2026-05-20` @ Phase B HEAD (6 commits, local, not pushed)
**Scope**: Core 3 axes per Grant adjudication 2026-05-20 — α + (p,q) + C8

## Verdict

**🟢 NO BLOCKING DRIFT.** HOPF-02a sim is current against AVE-Core canon on all 3 audited axes. Predicted Δf shifts hold; (p,q) assignments align with FI-13 RESOLVED; C8 PASS strengthens outcome interpretation without shifting formula. **Recommendation: PROCEED with Phase 0b fab submission.**

## Premise

Phase A repo audit + Phase B walk-back surfaced the need to verify HOPF-02a predictions against current AVE-Core canon BEFORE Grant submits Gerbers to JLCPCB. The Δf prediction formula is `Δf/f = α · pq/(p+q)` with L vs R handedness sign. Drift would happen if (a) α value in HOPF differs from `ave.core.constants.ALPHA`, (b) (p,q) assignments in HOPF use stale particle-ID per pre-FI-13 framing, or (c) C8-BARYON-LADDER PASS at PDG 2024 implies the formula needs revision.

Grant adjudicated scope: focus on the 3 axes most likely to affect numerical predictions; defer cosmological + theoretical-classifier axes (Class E, temporal regime, Q-G47, A-034, SPARC, C11) which don't enter the EE-scale Δf formula.

## Axis 1 — α numerical match

### Test
```bash
python3 -c "from ave.core.constants import ALPHA; print(f'{ALPHA!r}')"
# Output: 0.0072973525693

# Hardcoded value pre-Phase-B:
# scripts/hopf_02_nec2_run.py:88 (pre-fix):
# ALPHA = 7.2973525693e-3  # = 0.0072973525693
```

### Result
**Exact match** at all 13 significant figures. CODATA 2018 fine-structure constant unchanged. Phase B fix (`59dff6e`) replaced the hardcoded literal with `from ave.core.constants import ALPHA`; numerical predictions unchanged.

### Drift impact
**NONE.** The −7.92 / −11.91 / −55.29 MHz differentials at f_classical 380 / 680 / 2020 MHz hold to all relevant precision.

## Axis 2 — (p,q) assignments vs FI-13 RESOLVED canon

### HOPF AntennaSpec list (per [`scripts/hopf_02_nec2_run.py:113-121`](AVE-HOPF/scripts/hopf_02_nec2_run.py))

```python
ANTENNAS = [
    ("control", 0, 0,  0),
    ("k23_R",   2, 3, +1),
    ("k23_L",   2, 3, -1),
    ("k25_R",   2, 5, +1),
    ("k25_L",   2, 5, -1),
    ("k35_R",   3, 5, +1),
    ("k35_L",   3, 5, -1),
]
```

### Comparison with FI-13 RESOLVED canonical particle-ID

| HOPF antenna | (p,q) | FI-13 RESOLVED canonical assignment | Aligned? |
|---|---|---|---|
| `control` | (0,0) | Achiral baseline (no torus knot) | ✓ |
| `k23_R / k23_L` | (2,3) | Electron trefoil (lepton family single-loop; canonical Vol 2 Ch 6) | ✓ |
| `k25_R / k25_L` | (2,5) | Proton cinquefoil per-loop winding on Borromean N=3 baryon (canonical Vol 2 Ch 2 + C8 FULL PASS) | ✓ |
| `k35_R / k35_L` | (3,5) | Higher-winding test mode (no canonical particle; probe of formula extension) | ✓ (intentional test of formula generality) |

**No stale (2,q) assignments**:
- HOPF does NOT use the retracted "(2,5)=muon" framing per [FI-13 RESOLVED 2026-05-18](../manuscript/ave-kb/common/closure-roadmap.md)
- Lepton family stays at (2,3) trefoil; baryon climbs (2,q_odd) — HOPF correctly probes (2,3) electron + (2,5) proton independently
- (3,5) is intentionally non-particle: probes whether Δf formula generalizes beyond canonical assignments

### Drift impact
**NONE.** All (p,q) values match current FI-13 RESOLVED canonical assignments.

## Axis 3 — C8-BARYON-LADDER FULL PASS implications

### C8 result (per [`baryon_ladder_pdg_2024_anchor.py`](../src/scripts/verify/baryon_ladder_pdg_2024_anchor.py) commit `55b3317`)

- Proton mass via (2,5) cinquefoil = **938.254 MeV** vs PDG 938.272 → **−0.002%** (200× better than precision-rounding overclaim)
- 6/6 retrospective J^P-consistent
- Forward (2,17) → Δ(2750) at −0.30% (PDG **); (2,19) → Δ(2950) at +1.12% (PDG **)
- Single kernel S(A) = √(1−A²) + (2,q) winding produces entire spectrum
- C8 is hadronic-scale validation of (2,q) family

### Formula impact on HOPF

The Δf formula `Δf/f = α · pq/(p+q)` is **invariant to C8's quantitative result**. C8 confirms (2,q) topological classification at HADRONIC scale; HOPF measures (2,q) chiral coupling at EE scale. The two are independent observable channels of the same topological assignment.

| Question | Answer |
|---|---|
| Does C8 change the Δf numerical predictions? | NO. Formula unchanged; predictions hold. |
| Does C8 change HOPF outcome interpretation? | YES — strengthens. |

### Outcome interpretation update (per audit Axis 3 implications)

| HOPF outcome | Pre-C8 interpretation | Post-C8 interpretation |
|---|---|---|
| **A (PASS)** | (2,q) classification confirmed at EE scale | **Cross-scale corroboration** of (2,q) classification: now anchored at EE scale (HOPF) + hadronic scale (C8) — 30+ OOM cross-scale evidence |
| **B (partial)** | Chirality detected; magnitude needs revision | Same; chirality exists; coefficient needs structural revision |
| **C (null)** | (2,q) family falsified at EE scale | **Substantive structural finding** — (2,q) is hadronic-only at C8 PDG 2024 precision; does NOT generalize to EE scale; would force structural revision of (2,q) cross-scale claim despite C8 hadronic PASS |
| **D (confound)** | Re-design needed | Same — escalate to HOPF-02b cavity variant |

### Drift impact
**NONE on formula; significant on outcome adjudication framing.** Sub-epic Phase 3 outcome matrix updated per this audit.

## Numerical sanity check (Δf differentials arithmetic)

Verify Vol 4 matrix-row predictions reproduce from current α + canonical formula:

```
Δf_differential = 2 · α · pq/(p+q) · f_classical    (small-α approximation, L vs R sign flip)
α = 0.0072973525693
```

| (p,q) | tf = pq/(p+q) | f_classical (MHz) | Computed Δf (MHz) | Matrix value (MHz) | Match? |
|---|---|---|---|---|---|
| (2,5) | 10/7 ≈ 1.4286 | 380 | 0.0073 × 1.4286 × 380 × 2 = **7.92** | −7.92 | ✓ |
| (2,3) | 6/5 = 1.2000 | 680 | 0.0073 × 1.2 × 680 × 2 = **11.91** | −11.91 | ✓ |
| (3,5) | 15/8 = 1.8750 | 2020 | 0.0073 × 1.875 × 2020 × 2 = **55.29** | −55.29 | ✓ |

All three predicted Δf differentials reproduce to matrix-row precision. No re-computation needed.

## Other-axis spot-check (deferred axes per Grant's "Core 3" choice)

Quick verification that the deferred axes don't have hidden drift:

| Axis | Drift impact on HOPF |
|---|---|
| **Q-G47 ξ_K1=8/3, ξ_K2=32** (substrate-scale Cosserat-Lagrangian closure 2026-05-18) | Cosserat back-reaction coefficients live in K4 substrate physics; **not in Δf formula** which uses Op14 saturation kernel + (p,q) topology only → no drift |
| **A-034 catalog 26 instances** | HOPF doesn't cite a specific A-034 row; the Δf formula draws from Ax1 (K4 substrate chirality) + Ax4 (saturation in α-suppression regime); **catalog rows are observational anchors, not derivation inputs** → no drift |
| **Temporal regime classifier** | HOPF operates in **lossless temporal regime** (sub-yield E-field; α-suppression is the regime characterization) — already implicit in the formula via α factor; the new classifier formalizes existing regime → no drift |
| **Class E projection** | Cosmological-constant context (ρ_Λ, H_∞ joint constraint at u₀* operating point); **not relevant** to EE-scale antenna |
| **SPARC 11.5% benchmark** | Galactic rotation curves; **not relevant** to EE-scale antenna |
| **C11 Mach-Zehnder ν_vac=2/7** | Triangulation context for ν_vac cascade (C1+C11+C12); **not in HOPF formula** which uses α not ν_vac |
| **Cosmic-axis cascade (C5 PROVISIONAL)** | Cosmological observables; **not relevant** |

## What this audit closes

- ✓ EXP-A1-HOPF sub-epic [`exp-a1-hopf.md`](exp-a1-hopf.md) Phase 0a artifact-generation **complete** via Phase B walk-back commit batch
- ✓ Pre-fab sim drift verification on 3 core axes — **NO drift on any**
- ✓ Phase 3 outcome adjudication matrix updated per C8 strengthening
- ✓ Verification that Phase B α-import fix preserves numerical predictions to all relevant precision

## What this audit does NOT close

- ⚠ Phase 2 ave-prereg-format pre-registration for VNA measurement (BLOCKER-3 from Phase A audit; ~1 hr to draft; NOT blocking Phase 0)
- ⚠ Phase 4 outcome paper-template drafting (IF Outcome A lands; deferred to post-measurement)
- ⚠ Pointer-opacity migration across AVE-Core (corpus-wide IP-divide concern; separate sub-epic if pursued)
- ⚠ Promotion-workflow first-fire (NEC2 ALPHA-post-processing extraction to AVE-Core per [`promotion-workflow-template.md`](promotion-workflow-template.md); gated on Outcome A)

## Phase 0b green-light

With α + (p,q) + C8 verified clean against current canon, the audit-gated Phase 0b fab submission can proceed.

**Grant action**: upload `AVE-HOPF/hardware/Gerbers_hopf_02a/` ZIP to JLCPCB per [`AVE-HOPF/hardware/hopf_02a_ORDERING.md`](AVE-HOPF/hardware/hopf_02a_ORDERING.md). Print 5 mandrels per [`AVE-HOPF/hardware/hopf_02a_BOM.md`](AVE-HOPF/hardware/hopf_02a_BOM.md) mandrel-print notes.

Per AVE-HOPF AGENTS.md §3 workflow: also consider pushing branch `analysis/a1-hopf-audit-walkback-2026-05-20` to origin + opening PR + squash-merging to main (or research/hopf-01-testing) before fab to preserve audit-walkback work in canonical branch state.

## Audit trail

- 2026-05-20 EOD+ — Sim audit landed. Phase A repo audit (`exp-a1-hopf-repo-audit.md`) found Phase 0a blockers + walk-back targets; Phase B implementor session (commit batch on AVE-HOPF analysis/a1-hopf-audit-walkback-2026-05-20) closed blockers + applied R1.1 reorg + ALPHA fix; this sim-audit verifies no drift on the 3 prediction axes that gate Phase 0b fab.
- Audit-trail commits referenced: `e3d79ad` Phase A audit + sub-epic walk-back; `17602c3` promotion-workflow template; Phase B 6 commits on AVE-HOPF branch (cfc5a40..HEAD).
