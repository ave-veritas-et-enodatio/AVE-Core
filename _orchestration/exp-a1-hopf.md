# EXP-A1-HOPF: Chiral Antenna Resonance Shift (HOPF-02a)

**Parent epic**: [`experimental-arc.md`](experimental-arc.md)
**Status**: PHASE 0 — Grant fab decision pending
**Sibling repo owner**: AVE-HOPF (Grant)
**Established**: 2026-05-20 from Phase 2 cascade-emphasis ranking

## Tier (per parent epic Phase 2 audit)

Cascade × Executability winner — only top-3 cascade candidate with hardware fab-ready. Composite Σ=12. R=2 (hardware design complete), D=3 (U-D, 60-400× NEC2 SNR), S=2 (M-severity), C=2 (~$123 BOM), X=3 (A1 family cascade C8 + C3 + C10).

## Premise

The AVE framework's `Δf/f = α · pq/(p+q)` chiral-antenna resonance-shift formula is the EE-scale test of the (2,q) torus-knot family. The same (p,q) classification underlies:

- **C8-BARYON-LADDER** (FULL PASS at -0.002% proton, 6/6 J^P per [`baryon_ladder_pdg_2024_anchor.py`](../src/scripts/verify/baryon_ladder_pdg_2024_anchor.py))
- **C3-MUON-DELTA** (PASS-conditional +502 per [`muon_g2_fermilab_anchor.py`](../src/scripts/verify/muon_g2_fermilab_anchor.py); awaits Fermilab Run-4/5)
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

### Hardware substrate
- [`AVE-HOPF/hardware/hopf_02a.kicad_pcb`](../../AVE-HOPF/hardware/hopf_02a.kicad_pcb) — KiCad PCB ready
- [`AVE-HOPF/hardware/Gerbers/`](../../AVE-HOPF/hardware/Gerbers/) — production-ready Gerbers + drill files
- [`AVE-HOPF/hardware/BOM.md`](../../AVE-HOPF/hardware/BOM.md) — $123 BOM finalized
- [`AVE-HOPF/hardware/ORDERING.md`](../../AVE-HOPF/hardware/ORDERING.md) — JLCPCB ordering instructions
- [`AVE-HOPF/hardware/TEST_PROCEDURE.md`](../../AVE-HOPF/hardware/TEST_PROCEDURE.md) — VNA measurement protocol
- [`AVE-HOPF/hardware/assembly_guide/`](../../AVE-HOPF/hardware/assembly_guide/) — 3D-print mandrel + wire-winding guide
- [`AVE-HOPF/hardware/DESIGN_LOG.md`](../../AVE-HOPF/hardware/DESIGN_LOG.md) + [`DRC.rpt`](../../AVE-HOPF/hardware/DRC.rpt) — design rules + audit trail

### Software / prediction substrate
- NEC2 prediction at [`AVE-HOPF/docs/SESSION_STATE_2026-05-05.md:21`](../../AVE-HOPF/docs/SESSION_STATE_2026-05-05.md) — 60-400× SNR margin
- 89 fast tests passing per HOPF-02 geometry validation (SMA convention, z-values, hole counts, L↔R mirror exactness)
- Python KiCad emitter [`hopf_02_generate_kicad_pcb.py`](../../AVE-HOPF/hardware/hopf_02_generate_kicad_pcb.py) — canonical fab path (bypasses still-unblocked `ato build` layout-init issue)

### Walk-back targets (Phase 1 of parent epic)
Phase 1 surgical walk-back will refresh these load-bearing leaves:

| Leaf | Stale state | Refresh |
|---|---|---|
| [`torus-knot-baryon-predictions.md`](../manuscript/ave-kb/vol4/falsification/ch12-falsifiable-predictions/torus-knot-baryon-predictions.md) (2026-04-13) | proton at 0.00%; no J^P column; missing forward predictions; pre-FI-13 (2,q) framing | Refresh per [`torus-knot-ladder-baryons.md`](../manuscript/ave-kb/vol2/particle-physics/ch02-baryon-sector/torus-knot-ladder-baryons.md) Vol 2 anchor; add J^P column; add forward c=17/19 confirmations; cite FI-13 RESOLVED state |
| [`project-hopf-02.md`](../manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/project-hopf-02.md) (2026-04-13) | HOPF-02/03 namespace split missing; pre-FI-13 (2,q) framing | Reference HOPF-02/03 namespace split per AVE-HOPF 2026-05-06 reconciliation; cite FI-13 RESOLVED state for (2,q) canonical |

## Phase ladder

### Phase 0 (PENDING) — Grant fab decision

**Action**: Grant submits HOPF-02a Gerbers to JLCPCB; orders 3D-print mandrels.

**Cost**: ~$123 BOM
**Time**: 2 weeks fab turnaround (typical JLCPCB)
**Decision dependency**: Grant bench priority + cash flow

### Phase 1 (PENDING, gated on Phase 0) — Assembly

**Action**: Receive PCBA + mandrels; wind L-handed + R-handed enantiomer pair onto mandrels per [`AVE-HOPF/hardware/assembly_guide/`](../../AVE-HOPF/hardware/assembly_guide/); solder SMA connectors.

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
- [Universal Saturation Kernel Catalog A-034 row "Atomic / EM"](../manuscript/ave-kb/common/universal-saturation-kernel-catalog.md) — Ax 4 saturation governs E-field at substrate boundary
- [Four Universal Regimes — Regime I sub-yield substrate](../manuscript/ave-kb/vol1/operators-and-regimes/ch7-regime-map/four-regimes.md) — A1-HOPF operates in Regime I (small-signal $E \ll E_{yield}$)
- [Power-Domain Classification (orbital-friction-paradox)](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/orbital-friction-paradox.md) — antenna at S₁₁ resonance is reactive-cycling (θ → 90°, lossless LC tank)
- [Temporal Saturation Regime Classifier](../manuscript/ave-kb/common/temporal-saturation-regime-classifier.md) — A1-HOPF is in **lossless temporal regime** ($\delta_{AVE} \to 0$); high-Q resonator class

### Matrix + downstream cascade
- [Matrix row A1-HOPF (Predictions)](../manuscript/ave-kb/common/divergence-test-substrate-map.md) — full prediction matrix entry
- [C8-BARYON-LADDER FULL PASS](../manuscript/ave-kb/common/divergence-test-substrate-map.md) — hadronic-scale (2,q) confirmation
- [C3-MUON-DELTA PASS-conditional](../manuscript/ave-kb/common/divergence-test-substrate-map.md) — lepton-g-2 scale (2,q) confirmation
- [Torus-Knot Ladder Baryons (canonical Vol 2)](../manuscript/ave-kb/vol2/particle-physics/ch02-baryon-sector/torus-knot-ladder-baryons.md) — refreshed per C8 PDG anchor 2026-05-18; Vol 4 falsification leaf currently STALE (Phase 1 walk-back target)

### Hardware (sibling-repo)
- [`AVE-HOPF/.agents/HANDOFF.md`](../../AVE-HOPF/.agents/HANDOFF.md) — canonical hardware-state holder
- [`AVE-HOPF/hardware/`](../../AVE-HOPF/hardware/) — Gerbers + BOM + assembly guide + DRC report
- [`AVE-HOPF/docs/SESSION_STATE_2026-05-05.md`](../../AVE-HOPF/docs/SESSION_STATE_2026-05-05.md) — 60-400× NEC2 SNR prediction
- [`AVE-HOPF/docs/manuscript_reconciliation.md`](../../AVE-HOPF/docs/manuscript_reconciliation.md) — HOPF-02/03 namespace split + reconciliation closure

## Audit trail

- 2026-05-20 — Sub-epic established from Phase 2 cascade-emphasis ranking (Σ=12, cascade × executability winner). Phase 0 fab decision pending.
