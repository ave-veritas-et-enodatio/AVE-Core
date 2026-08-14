---
id: p19-flyby-readjudication
title: P19 flyby anomaly — the label is settled, the claim is not; does it belong in the public table?
status: ROUTED-TO-GRANT
owner: grant
opened: 2026-08-13
source: manuscript/consistency-manifest.yaml
anchor: "THE LABEL IS SETTLED; THE CLAIM IS NOT"
---

Grant, 2026-08-13, ruling the label and opening this in the same breath: *"lets label it correctly
but add it to our followups/backlog to readjudicate"*.

**Settled and not reopening here:** `calibration_role: forward-prediction → consistency`, and
`type: derived_prediction → consistency_check`. P19 was the last row carrying the label struck off
P42 as *"wrong on all three axes"*.

**The open question is the claim, not its classification.** Correctly labelling a weak row does not
make it strong, and P19 is publicly displayed as row 19 of both master tables reading **1.6 % ✅**.

**What a re-adjudication has to weigh:**

| against the row | for the row |
|---|---|
| `clm-a71inj` solidity **0.50**, band **input-only**, `experimental_solidity: None` | the formula's geometric modulators *legitimately* predict null at specific geometries |
| Anderson 2008 six-spacecraft anchor: **2 of 6 within 1σ**, 3 of 6 within 2σ | so the nulls may be a **success** of the formula, not cherry-picking |
| already walked back once (2026-05-18) — the "13.4 mm/s" headline replaced with per-spacecraft framing plus outlier acknowledgment | the per-spacecraft table now exists (`src/scripts/verify/flyby_anomaly_anderson_anchor.py`) and `docs/framing_and_presentation.md` marks the anti-pattern **RESOLVED** |
| every one of the six flybys was measured **before** the formula was applied — postdiction by construction | the mechanism is Regime-IV stator-boundary, cross-referenced to the Gravitational Stator and geodynamo Back-EMF leaves |

**The question to answer:** is a green ✅ at 1.6 % an honest public presentation of a
solidity-0.50 input-only row that matches 2 of 6 anchors — or does the public table need a
qualifier, a different number, or the row removed? Note row 3 (g−2) already carries a public
⚠ *"postdiction — demoted from forward-falsifier"* qualifier, so the precedent for annotating
rather than deleting exists.

**Not urgent, and deliberately not bundled** with the labelling PR: the label change is mechanical
and reversible; this is a physics-presentation call.
