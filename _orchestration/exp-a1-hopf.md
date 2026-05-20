# EXP-A1-HOPF: Chiral Antenna Resonance Shift (HOPF-02a)

**Parent epic**: [`experimental-arc.md`](experimental-arc.md)
**Status**: PHASE 0a — Artifact-generation pending (Gerbers export + HOPF-02a ORDERING.md draft); Phase 0b fab-submission gated on 0a
**Sibling repo owner**: AVE-HOPF (Grant)
**Established**: 2026-05-20 from Phase 2 cascade-emphasis ranking
**Phase A repo audit**: [`exp-a1-hopf-repo-audit.md`](exp-a1-hopf-repo-audit.md) (425 lines, 23 ✓ / 11 ⚠ / 3 🔴 — 2026-05-20)

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

### Walk-back targets (Phase 1 of parent epic) — ✓ DONE 2026-05-20 via `6621dae`

Phase 1 surgical walk-back refreshed these load-bearing leaves (verified at-canon at audit time per [`exp-a1-hopf-repo-audit.md`](exp-a1-hopf-repo-audit.md) Axis 5):

| Leaf | Pre-walk-back state | Post-walk-back state |
|---|---|---|
| [`torus-knot-baryon-predictions.md`](../manuscript/ave-kb/vol4/falsification/ch12-falsifiable-predictions/torus-knot-baryon-predictions.md) | proton at 0.00%; no J^P column; missing forward predictions; pre-FI-13 (2,q) framing | ✓ DONE — refreshed per [`torus-knot-ladder-baryons.md`](../manuscript/ave-kb/vol2/particle-physics/ch02-baryon-sector/torus-knot-ladder-baryons.md) Vol 2 anchor; J^P column added; forward c=17/19 confirmations included; FI-13 RESOLVED state cited |
| [`project-hopf-02.md`](../manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/project-hopf-02.md) | HOPF-02/03 namespace split missing; pre-FI-13 (2,q) framing | ✓ DONE — HOPF-01/02/03 namespace clarification table per AVE-HOPF 2026-05-06 reconciliation; FI-13 (2,q) particle-id table; canonical AVE-HOPF cross-references |

**Audit-surfaced follow-up walk-backs** (NOT in original Phase 1 scope; flagged for Grant adjudication):
- 4 misdirected citations in `exp-a1-hopf.md` (lines 32, 46, 70, 85, 139-141) point at HOPF-01-pilot artifacts (BOM.md, TEST_PROCEDURE.md, assembly_guide/, Gerbers/) — root cause is AVE-HOPF directory structure (audit Axis 1 ATTN-2); gated on AVE-HOPF reorganization OR direct walk-back
- Same 3 misdirected citations in `project-hopf-02.md` (lines 82, 84, 85) — same root cause
- 18 explicit `AVE-HOPF/...` paths in PUBLIC AVE-Core — IP-divide opacity violation per `ave-ip-divide-discipline` Step 4 Class F; corpus-wide concern (not just A1-HOPF)

## Phase ladder

### Phase 0a (PENDING) — Artifact generation (3 BLOCKERS per repo audit)

**🔴 BLOCKER-1** (5 min, Grant action): export HOPF-02a Gerbers + drill files from `AVE-HOPF/hardware/hopf_02a.kicad_pcb`. Currently `AVE-HOPF/hardware/Gerbers/` contains HOPF-01 Gerbers only (12 files all named `hopf_01-*.gbr`); HOPF-02a equivalents do not exist as built artifacts. Run `kicad-cli pcb export gerbers ...` + `... export drill ...` per `AVE-HOPF/.agents/HANDOFF.md` TODO #1.

**🔴 BLOCKER-2** (15 min, drafting): write `AVE-HOPF/hardware/hopf_02a_ORDERING.md` with v-score spec. Current `AVE-HOPF/hardware/ORDERING.md` is titled "HOPF-01 JLCPCB Ordering Guide" with 160×120 mm dimensions, no v-score, 6 SMA layout — entirely HOPF-01-specific. HOPF-02a needs: 250×185 mm panel, 4 v-score lines at 1/3 board thickness (0.5 mm), ±0.1 mm drill tol. Draft from `AVE-HOPF/hardware/hopf_02_ASSEMBLY_GUIDE.md` lines 36-77.

These are AVE-HOPF-side work; either Grant inline OR Phase B implementor session on AVE-HOPF branch `analysis/a1-hopf-audit-walkback-2026-05-20` (or similar typed name per AGENTS.md §3) off `research/hopf-01-testing`.

### Phase 0b (PENDING, gated on 0a) — Grant fab submission

**Action**: Grant submits HOPF-02a Gerbers + ORDERING.md to JLCPCB; orders 3D-print mandrels.

**Cost**: ~$123 BOM (verified at `AVE-HOPF/hardware/hopf_02_ASSEMBLY_GUIDE.md:21-32`; **note**: top-level `AVE-HOPF/hardware/BOM.md` is the $142 HOPF-01 BOM — cite the assembly guide for HOPF-02a BOM)
**Time**: 2 weeks fab turnaround (typical JLCPCB)
**Decision dependency**: Grant bench priority + cash flow (post-Phase-0a artifact-completion)

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
