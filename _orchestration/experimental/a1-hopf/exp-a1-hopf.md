# EXP-A1-HOPF: Chiral Antenna Resonance Shift (HOPF-02a)

**Parent epic**: [`experimental-arc.md`](../experimental-arc.md)
**Status**: **PHASE 0a ✓ COMPLETE (Phase B walk-back commits) + Sim-audit ✓ NO DRIFT** — Phase 0b ready for Grant fab submission
**Sibling repo owner**: AVE-HOPF (Grant)
**Established**: 2026-05-20 from Phase 2 cascade-emphasis ranking
**Phase A repo audit**: [`exp-a1-hopf-repo-audit.md`](exp-a1-hopf-repo-audit.md) (425 lines, 23 ✓ / 11 ⚠ / 3 🔴 — 2026-05-20)
**Sim audit (α + (p,q) + C8)**: [`exp-a1-hopf-sim-audit.md`](exp-a1-hopf-sim-audit.md) — NO BLOCKING DRIFT (2026-05-20 EOD+)
**Phase B walk-back**: AVE-HOPF branch `analysis/a1-hopf-audit-walkback-2026-05-20` (6 commits, local; closes BLOCKER-1 + BLOCKER-2 + R1.1 reorg + ALPHA fix + MAGIC_NUMBERS extension)

## Tier (per parent epic Phase 2 audit)

Cascade × Executability winner — only top-3 cascade candidate with hardware fab-ready. Composite Σ=12. R=2 (hardware design complete), D=3 (U-D, 60-400× NEC2 SNR), S=2 (M-severity), C=2 (~$123 BOM), X=3 (A1 family cascade C8 + C3 + C10).

## Premise

The AVE framework's `Δf/f = α · pq/(p+q)` chiral-antenna resonance-shift formula is the EE-scale test of the (2,q) torus-knot family. The same (p,q) classification underlies:

- **C8-BARYON-LADDER** (FULL PASS at -0.002% proton, 6/6 J^P per [`baryon_ladder_pdg_2024_anchor.py`](../../../src/scripts/verify/baryon_ladder_pdg_2024_anchor.py))
- **C3-MUON-DELTA** (PASS-conditional +502 per [`muon_g2_fermilab_anchor.py`](../../../src/scripts/verify/muon_g2_fermilab_anchor.py); awaits Fermilab Run-4/5)
- **C10-MUON-LIFE** (canonical (2,3)+Cosserat ladder per FI-13 resolution)

A1-HOPF tests the (p,q) coupling at EE scale — distinct from hadronic mass scale at C8 and lepton g-2 scale at C3 — providing cross-scale corroboration of (2,q) topological classification.

**Standard EE counterfactual**: free-space wire helix has NO chirality-dependent resonance shift. AVE predicts $\Delta f/f = \alpha \cdot pq/(p+q)$ because the chiral helix couples to K4 substrate's intrinsic chirality.

## Canonical prediction (verified against current corpus)

| (p,q) | Predicted shift | Topological identification (per FI-13 RESOLVED 2026-05-18) |
|---|---|---|
| (2,3) | −11.91 MHz | Electron trefoil (lepton family canonical) |
| (2,5) | −7.92 MHz | Proton cinquefoil (baryon family canonical) |
| (3,5) | −55.29 MHz | Higher-winding test mode |

**60-400× NEC2 SNR margin** per HOPF-02a NEC2 predictions at [`AVE-HOPF/docs/SESSION_STATE_2026-05-05.md:21`](../../AVE-HOPF/docs/SESSION_STATE_2026-05-05.md).

## Current state

### Hardware substrate (HOPF-02a, post-Phase-B walk-back 2026-05-20)
- [`AVE-HOPF/hardware/hopf_02a.kicad_pcb`](../../AVE-HOPF/hardware/hopf_02a.kicad_pcb) — KiCad PCB source
- [`AVE-HOPF/hardware/Gerbers_hopf_02a/`](../../AVE-HOPF/hardware/Gerbers_hopf_02a/) — production-ready Gerbers + drill files (15 files: 9 Gerber layers + 2 drill + 2 drill maps + gbrjob + DRC report; exported via `kicad-cli pcb export` per Phase B commit `86d1a00`)
- [`AVE-HOPF/hardware/hopf_02a_BOM.md`](../../AVE-HOPF/hardware/hopf_02a_BOM.md) — $123 BOM (drafted per Phase B commit `de2aecf`)
- [`AVE-HOPF/hardware/hopf_02a_ORDERING.md`](../../AVE-HOPF/hardware/hopf_02a_ORDERING.md) — JLCPCB ordering instructions with v-score spec (250×185 mm panel, 4 v-score lines at 1/3 board thickness, ±0.1 mm drill tol)
- [`AVE-HOPF/hardware/hopf_02_ASSEMBLY_GUIDE.md`](../../AVE-HOPF/hardware/hopf_02_ASSEMBLY_GUIDE.md) — 3D-print mandrel + wire-winding guide (376 lines; Phase F-G measurement protocol embedded)
- [`AVE-HOPF/hardware/hopf_02a_DRC.rpt`](../../AVE-HOPF/hardware/hopf_02a_DRC.rpt) — DRC report (251 violations are `lib_footprint_issues` warnings, expected for Python emitter fab path; no copper/drill clearance issues)
- [`AVE-HOPF/hardware/DESIGN_LOG.md`](../../AVE-HOPF/hardware/DESIGN_LOG.md) — design rules + audit trail

**HOPF-01 historical artifacts** (renamed per R1.1 reorganization commit `8c118ef`):
- [`AVE-HOPF/hardware/hopf_01_BOM.md`](../../AVE-HOPF/hardware/hopf_01_BOM.md) (was `BOM.md`; $142 HOPF-01-pilot BOM)
- [`AVE-HOPF/hardware/hopf_01_ORDERING.md`](../../AVE-HOPF/hardware/hopf_01_ORDERING.md) (was `ORDERING.md`)
- [`AVE-HOPF/hardware/hopf_01_TEST_PROCEDURE.md`](../../AVE-HOPF/hardware/hopf_01_TEST_PROCEDURE.md) (was `TEST_PROCEDURE.md`)
- [`AVE-HOPF/hardware/hopf_01_assembly_guide/`](../../AVE-HOPF/hardware/hopf_01_assembly_guide/) (HOPF-01 antenna-winding PNGs; was `assembly_guide/`)
- [`AVE-HOPF/hardware/Gerbers_hopf_01/`](../../AVE-HOPF/hardware/Gerbers_hopf_01/) (was `Gerbers/`)

Phase 2 VNA measurement protocol: extract from `hopf_02_ASSEMBLY_GUIDE.md` Phase F-G, OR draft as part of ave-prereg-format pre-registration per Phase A audit BLOCKER-3 (~1 hr, gates Phase 2 not Phase 0b).

### Software / prediction substrate
- NEC2 prediction at [`AVE-HOPF/docs/SESSION_STATE_2026-05-05.md:21`](../../AVE-HOPF/docs/SESSION_STATE_2026-05-05.md) — 60-400× SNR margin
- 89 fast tests passing per HOPF-02 geometry validation (SMA convention, z-values, hole counts, L↔R mirror exactness)
- Python KiCad emitter [`hopf_02_generate_kicad_pcb.py`](../../AVE-HOPF/hardware/hopf_02_generate_kicad_pcb.py) — canonical fab path (bypasses still-unblocked `ato build` layout-init issue)

### Walk-back targets (Phase 1 of parent epic) — ✓ DONE 2026-05-20 via `6621dae`

Phase 1 surgical walk-back refreshed these load-bearing leaves (verified at-canon at audit time per [`exp-a1-hopf-repo-audit.md`](exp-a1-hopf-repo-audit.md) Axis 5):

| Leaf | Pre-walk-back state | Post-walk-back state |
|---|---|---|
| [`torus-knot-baryon-predictions.md`](../../../manuscript/ave-kb/vol4/falsification/ch12-falsifiable-predictions/torus-knot-baryon-predictions.md) | proton at 0.00%; no J^P column; missing forward predictions; pre-FI-13 (2,q) framing | ✓ DONE — refreshed per [`torus-knot-ladder-baryons.md`](../../../manuscript/ave-kb/vol2/particle-physics/ch02-baryon-sector/torus-knot-ladder-baryons.md) Vol 2 anchor; J^P column added; forward c=17/19 confirmations included; FI-13 RESOLVED state cited |
| [`project-hopf-02.md`](../../../manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/project-hopf-02.md) | HOPF-02/03 namespace split missing; pre-FI-13 (2,q) framing | ✓ DONE — HOPF-01/02/03 namespace clarification table per AVE-HOPF 2026-05-06 reconciliation; FI-13 (2,q) particle-id table; canonical AVE-HOPF cross-references |

**Audit-surfaced follow-up walk-backs** (status post Phase B + sim-audit 2026-05-20):
- ✓ DONE — 4 misdirected citations in `exp-a1-hopf.md` (Hardware substrate section above) — refreshed to HOPF-02a sibling files; HOPF-01 historicals also explicitly cited
- ✓ DONE — 3 misdirected citations in `project-hopf-02.md` (engineering substrate table) — refreshed in same commit batch
- ⚠ DEFERRED — 18 explicit `AVE-HOPF/...` paths in PUBLIC AVE-Core — IP-divide opacity violation per `ave-ip-divide-discipline` Step 4 Class F; corpus-wide concern (not just A1-HOPF); requires `.ip-graph.yaml` seed + APP-XX opaque pointer migration per [`promotion-workflow-template.md`](../promotion-workflow-template.md) Step 5; multi-session work; NOT blocking Phase 0b fab

## Phase ladder

### Phase 0a — Artifact generation ✓ COMPLETE (Phase B walk-back commits 2026-05-20)

✓ **BLOCKER-1 closed** (commit `86d1a00` on AVE-HOPF `analysis/a1-hopf-audit-walkback-2026-05-20`): HOPF-02a Gerbers exported to `AVE-HOPF/hardware/Gerbers_hopf_02a/` (15 files including 9 Gerber layers + 2 drill + DRC report)

✓ **BLOCKER-2 closed** (commit `de2aecf`): `AVE-HOPF/hardware/hopf_02a_ORDERING.md` drafted with v-score spec (250×185 mm panel, 4 v-score lines at 1/3 board thickness ≈ 0.5 mm, ±0.1 mm drill tol); `AVE-HOPF/hardware/hopf_02a_BOM.md` extracted (~$123)

✓ **R1.1 closed** (commit `8c118ef`): hardware/ reorganized with `hopf_01_*` + `hopf_02a_*` + `Gerbers_hopf_01/` + `Gerbers_hopf_02a/` explicit-prefix scheme; 11 internal cross-refs updated in same commit; `tests/test_spec_compliance.py` path refs updated; 89/89 tests pass post-rename

✓ **ALPHA fix closed** (commit `59dff6e`): `scripts/hopf_02_nec2_run.py:88` now imports `ALPHA` from `ave.core.constants` per `ave-canonical-source` discipline; exact numerical match verified — predictions unchanged

✓ **MAGIC_NUMBERS extension closed** (commit `822b4d5`): `tests/verify_local_universe.py` whitelist extended with alpha-as-fraction (7.2973525693e-3) to catch future α hardcodes

✓ **HANDOFF.md update** (commit `7913a80`): AVE-HOPF `.agents/HANDOFF.md` reflects all 5 walk-back items + Active TODO #1 (fab order) updated with new canonical paths

### Sim audit — α + (p,q) + C8 axes ✓ NO DRIFT (per [`exp-a1-hopf-sim-audit.md`](exp-a1-hopf-sim-audit.md))

- ✓ α: exact numerical match (0.0072973525693 ≡ 0.0072973525693); no prediction shift
- ✓ (p,q) assignments: aligned with FI-13 RESOLVED canonical particle-ID; HOPF tests (2,3) electron trefoil + (2,5) proton cinquefoil + (3,5) formula-extension probe
- ✓ C8 PASS: no formula drift; outcome interpretation strengthened (Outcome A = cross-scale corroboration spanning 30+ OOM; Outcome C = substantive structural finding that (2,q) is hadronic-only)
- ✓ Numerical sanity: −7.92 / −11.91 / −55.29 MHz arithmetically consistent with current α + canonical formula
- ✓ Deferred axes spot-check (Q-G47, A-034, temporal regime, Class E, SPARC, C11, cosmic-axis): none enter EE-scale Δf formula; no drift

### Phase 0b — Grant fab submission (READY)

**Action**: Grant submits `AVE-HOPF/hardware/Gerbers_hopf_02a/` ZIP to JLCPCB per [`AVE-HOPF/hardware/hopf_02a_ORDERING.md`](../../AVE-HOPF/hardware/hopf_02a_ORDERING.md); orders 3D-print mandrels per `AVE-HOPF/hardware/hopf_02a_BOM.md` mandrel-print notes.

**Cost**: ~$123 BOM (verified at [`AVE-HOPF/hardware/hopf_02a_BOM.md`](../../AVE-HOPF/hardware/hopf_02a_BOM.md))
**Time**: 2 weeks fab turnaround (typical JLCPCB)
**Decision dependency**: Grant bench priority + cash flow

**Optional pre-fab**: push AVE-HOPF branch `analysis/a1-hopf-audit-walkback-2026-05-20` to origin + open PR + squash-merge to `main` (or `research/hopf-01-testing`) per AVE-HOPF AGENTS.md §3 workflow to preserve audit-walkback work in canonical branch state before fab. ~5-10 min.

**BLOCKER-3** (Phase 2 gate, NOT blocking Phase 0b fab): draft `ave-prereg`-format pre-registration for HOPF-02a VNA measurement at `AVE-Core/research/2026-MM-DD_a1-hopf-hopf-02a-prereg.md` per `ave-handoff-canonical-locale`. ~1 hr. Includes SNR threshold (5σ for PASS), frozen Outcome A/B/C/D criteria, cable/ferrite/VNA serial documentation, date-of-execution commit.

### Phase 1 (PENDING, gated on Phase 0) — Assembly

**Action**: Receive PCBA + mandrels; wind L-handed + R-handed enantiomer pair onto mandrels per [`AVE-HOPF/hardware/hopf_02_ASSEMBLY_GUIDE.md`](../../AVE-HOPF/hardware/hopf_02_ASSEMBLY_GUIDE.md); solder SMA connectors.

**Time**: ~1 evening
**Skill**: Standard PCB assembly + manual wire-winding

### Phase 2 (PENDING, gated on Phase 1) — VNA measurement

**Action**: Connect to VNA; sweep 10-100 MHz; measure S₁₁ for both enantiomers; record differential.

**Predicted observable**: $\Delta f_{L \to R} = \alpha \cdot pq/(p+q) \cdot f_0$ — specific shifts per table above at 60-400× NEC2 SNR margin.

**Time**: ~1 hour measurement + ~1 day analysis
**Skill**: Standard VNA technique

### Phase 3 (CONDITIONAL on Phase 2 outcome) — Outcome adjudication

| Outcome | Interpretation |
|---|---|
| **A**: Δf matches AVE prediction within NEC2-class precision | (2,q) family confirmed at EE scale; cross-scale corroboration of C8 (hadronic) and C3 (lepton g-2) classifications |
| **B**: Δf detected but magnitude differs from prediction | Partial — confirms chiral-coupling exists; magnitude requires structural revision (Cosserat coefficient or (p,q) selection rule) |
| **C**: No Δf detected within NEC2 SNR | A1 family falsified at EE scale → cascade-impact on C8 + C3 + C10 (would force structural revision of (2,q) classification despite C8 PDG anchor confirmation at hadronic scale) |
| **D**: Confound (e.g., classical multi-antenna coupling à la HOPF-01) | Re-design needed; HOPF-02b cavity variant queued as escalation per `AVE-HOPF/.agents/HANDOFF.md` |

**Outcome A or B** → write canonical result doc + update matrix C8/C3/C10 with cross-scale corroboration cite + foreword "Fourth positive load-bearing empirical confirmation" if Outcome A.

**Outcome C** → walk-back across A1-HOPF cascade: C8 keeps PASS at hadronic but A1 EE-scale fails — implies (2,q) classification is hadronic-only and doesn't generalize. Major structural finding.

**Outcome D** → escalate to HOPF-02b (~$278 per AVE-HOPF roadmap) which adds cavity isolation.

### Phase 4 (CONDITIONAL on Phase 3 Outcome A) — HOPF-02b cavity extension

Per [`AVE-HOPF/.agents/HANDOFF.md`](../../AVE-HOPF/.agents/HANDOFF.md): HOPF-02b is the next-fab decision tree branch after HOPF-02a measurement lands. Adds full cavity + S21 measurement. ~$278 BOM.

### Phase 5 (CONDITIONAL, multi-session) — HOPF-03 Snell Parallax

Per AVE-HOPF 2026-05-06 namespace split: HOPF-03 is the spatial-domain Topological-Refraction-Snell-Parallax variant. Gated on HOPF-02a/b decision. Separate sub-epic if pursued.

## Open questions

1. **Fab timing**: when does Grant submit to JLCPCB? Depends on bench priority queue + cash flow + 2-week fab clock.
2. **Phase 3 adjudication threshold**: at what SNR confidence does Outcome A vs Outcome B vs Outcome C land? Pre-register before measurement (per `ave-prereg` discipline).
3. **HOPF-02b decision timing**: spawn after HOPF-02a Outcome A confirmed, OR pre-order to overlap with measurement?

## Skill discipline

- `ave-prereg`: write pre-registration BEFORE running VNA measurement (Phase 2). Should land as `research/2026-MM-DD_a1-hopf-hopf-02a-prereg.md` per `ave-handoff-canonical-locale` discipline.
- `ave-evidence-framing-discipline`: precision claims on Δf magnitude vs NEC2 SNR vs prediction.
- `ave-discrimination-check`: enumerate Outcome A/B/C/D before adjudication (already drafted above in Phase 3).
- `ave-walk-back`: if Outcome C, propagation across C8 + C3 + C10 matrix rows + foreword (would walk back the "Third positive" foreword promotion).
- `verify-before-cite` v1.4: any cross-references to NEC2 SNR numbers or (p,q) values verified against AVE-HOPF source.

## Sibling-repo coordination

- **AVE-HOPF** ([`AVE-HOPF/.agents/HANDOFF.md`](../../AVE-HOPF/.agents/HANDOFF.md)) is the canonical state holder. This sub-epic mirrors HOPF-02a fab gate into AVE-Core orchestration tracking. No edits to AVE-HOPF state from here; cross-references only.

## Cross-references

### Canonical AVE physics
- [Universal Saturation Kernel Catalog A-034 row "Atomic / EM"](../../../manuscript/ave-kb/common/universal-saturation-kernel-catalog.md) — Ax 4 saturation governs E-field at substrate boundary
- [Four Universal Regimes — Regime I sub-yield substrate](../../../manuscript/ave-kb/vol1/operators-and-regimes/ch7-regime-map/four-regimes.md) — A1-HOPF operates in Regime I (small-signal $E \ll E_{yield}$)
- [Power-Domain Classification (orbital-friction-paradox)](../../../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/orbital-friction-paradox.md) — antenna at S₁₁ resonance is reactive-cycling (θ → 90°, lossless LC tank)
- [Temporal Saturation Regime Classifier](../../../manuscript/ave-kb/common/temporal-saturation-regime-classifier.md) — A1-HOPF is in **lossless temporal regime** ($\delta_{AVE} \to 0$); high-Q resonator class

### Matrix + downstream cascade
- [Matrix row A1-HOPF (Predictions)](../../../manuscript/ave-kb/common/divergence-test-substrate-map.md) — full prediction matrix entry
- [C8-BARYON-LADDER FULL PASS](../../../manuscript/ave-kb/common/divergence-test-substrate-map.md) — hadronic-scale (2,q) confirmation
- [C3-MUON-DELTA PASS-conditional](../../../manuscript/ave-kb/common/divergence-test-substrate-map.md) — lepton-g-2 scale (2,q) confirmation
- [Torus-Knot Ladder Baryons (canonical Vol 2)](../../../manuscript/ave-kb/vol2/particle-physics/ch02-baryon-sector/torus-knot-ladder-baryons.md) — refreshed per C8 PDG anchor 2026-05-18; Vol 4 falsification leaf currently STALE (Phase 1 walk-back target)

### Hardware (sibling-repo)
- [`AVE-HOPF/.agents/HANDOFF.md`](../../AVE-HOPF/.agents/HANDOFF.md) — canonical hardware-state holder
- [`AVE-HOPF/hardware/`](../../AVE-HOPF/hardware/) — Gerbers + BOM + assembly guide + DRC report
- [`AVE-HOPF/docs/SESSION_STATE_2026-05-05.md`](../../AVE-HOPF/docs/SESSION_STATE_2026-05-05.md) — 60-400× NEC2 SNR prediction
- [`AVE-HOPF/docs/manuscript_reconciliation.md`](../../AVE-HOPF/docs/manuscript_reconciliation.md) — HOPF-02/03 namespace split + reconciliation closure

## Audit trail

- 2026-05-20 — Sub-epic established from Phase 2 cascade-emphasis ranking (Σ=12, cascade × executability winner). Phase 0 fab decision pending.
