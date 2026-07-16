# F1 consumer-audit — triage of banked numbers run under the DEFECT

**Date:** 2026-07-15 · **Class:** Orchestration audit doc (docs-only; engine untouched by this doc). · **Source:** `_orchestration/2026-07-15_f1-adjudication-package.md` HIGH/LOW tables. · **Companion:** `_orchestration/2026-07-15_hardware-ratings-map.md` §3 item 4 / R10.

## Status

**F1 is FIXED on the engine.** `K4Lattice3D.external_z_local=True` is now set under `CoupledK4Cosserat` (`src/ave/topological/k4_cosserat_coupling.py:312`), so `_scatter_all` (`src/ave/core/k4_tlm.py:311`) no longer overwrites the Cosserat-informed shared front with the V-only `1/√S(V)` recompute before `_connect_all` consumes it for bond Γ. Regression `src/tests/test_f1_shared_front_ordering.py` locks the ordering (4 tests, including an explicit `test_defect_control_overwrite_without_external_flag` documenting the pre-fix failure mode).

**This document is not a re-adjudication of any banked result.** It is a triage pass over the results that ran on the pre-fix engine (DEFECT window: V-only bond-Γ instead of the Cosserat shared front) — scheduling which need a cheap re-run, which get a provenance caveat, which are unaffected, and which remain untriaged. **No banked verdict is claimed to have flipped.** Any disposition below that says RE-RUN is a scheduling recommendation, not a result.

## Verification method (per HIGH row)

For each HIGH row in the adjudication package: (1) confirmed the file still exists on the current branch (`Glob`); (2) grepped the result doc (or, where the doc itself doesn't carry the literal tokens, the driver script / engine module it imports) for `V_inc` / `CoupledK4Cosserat` / `VacuumEngine3D` to confirm the result is still coupled-engine relevant post-fix. Two rows matched only transitively (via one import hop) — flagged inline.

## HIGH rows — disposition

| Result | Risk (from adjudication pkg) | Verified coupled-engine relevant? | Disposition |
|---|---|---|---|
| [`research/2026-06-09_genesis-24-saturated-seed_result.md`](../research/2026-06-09_genesis-24-saturated-seed_result.md) | `max\|V_inc\|→1.08×10⁴`, growing V-sector; VERDICT B (source channel FIRES, winding NOT RESOLVED) | ✅ direct (23 matches; driver `genesis_24_saturated_seed.py`, engine `VacuumEngine3D` COUPLED K4⊗Cosserat) | **RE-RUN** — cheap (reuses genesis-23 machinery, N=24/40 steps), and the banked source-channel-FIRES number is exactly the kind of V-active bond-Γ-sensitive claim F1 touches |
| [`research/2026-07-14_gpersist-localization-observable_RESULT.md`](../research/2026-07-14_gpersist-localization-observable_RESULT.md) | sustained `√α` V-pump every quiet step | ✅ direct (2 matches) | **CAVEAT-IN-RESULT** — this doc sits under **G-PERSIST ★RULED** (explicitly stated untouched by this doc's own fork question); adjudication package's recommended ruling shape says do **not** reopen G-PERSIST on F1 alone. Add a provenance caveat pointing here; do not re-run to try to move the ★RULED verdict without a separate Grant call |
| [`research/2026-07-12_genesis-node-birth-discriminator_result.md`](../research/2026-07-12_genesis-node-birth-discriminator_result.md) | nonzero `v_inc_peak`; E/φ persist gates D1–D4 | ✅ direct (1 match; driver `genesis_node_birth_discriminator.py` exists) | **RE-RUN** — cheap (single driver, has a frozen prereg + driver already wired); D1–D4 gate numbers are exactly bond-Γ-sensitive |
| [`research/2026-07-13_genesis-npersist-n14-battery_RESULT.md`](../research/2026-07-13_genesis-npersist-n14-battery_RESULT.md) | same detector family as G-PERSIST (presumed; family flag in adjudication pkg) | ⚠️ **transitive only** — no literal token match in the doc itself; driver imports `ave.core.genesis_v18_coupled`, which wraps `CoupledK4Cosserat` and writes `sim.k4.V_inc` directly (`genesis_v18_coupled.py:93,134`) | **CAVEAT-IN-RESULT** — confirms the "family flag (presumed)" from the first pass was correct (now verified via the one-hop import chain, not a literal string match); tagged **G-PERSIST ★PROPOSED-RULED** in-doc, so treat like the G-PERSIST row above — caveat, not re-run, pending a separate ruling call |
| [`research/2026-06-04_full-electron-option-B-discrete-emergence-result.md`](../research/2026-06-04_full-electron-option-B-discrete-emergence-result.md) | `(V_inc,V_ref)` retention trajectory | ✅ direct (54 matches; driver `r10_vacuumengine3d_transverse_2_3_emergence.py`) | **CAVEAT-IN-RESULT** — already carries a heavy adjudication apparatus (§VERDICT written by a prior orchestration session correcting two driver auto-verdict errors); re-running is not cheap and would re-open an already-corrected writeup. Caveat the provenance; defer re-run priority behind the three cheaper rows below |
| [`research/2026-06-09_cross-sector-pump-confirmation_result.md`](../research/2026-06-09_cross-sector-pump-confirmation_result.md) | explicit sustained V-to-yield drive; VERDICT B — FORM-BUT-NO-FIRE (null: V does not source ω) | ✅ direct (via `Cosserat`/`k4_cosserat_coupling`/`couple_v_sector` — the literal `CoupledK4Cosserat`/`VacuumEngine3D` tokens don't appear verbatim, engine cited as lowercase `vacuum_engine.py` module + `_impedance_gamma_shared`) | **RE-RUN** — highest-value re-run of the six: this is a **null result on the exact shared-front channel** (`_impedance_gamma_shared` / `Z_eff=√(S_μ/S_ε)`) that F1's fix changes the delivery of. A null banked under a defect that suppressed the same channel is the row most worth confirming cheaply |

## The r7–r10 gap — single NEEDS-TRIAGE bucket

The adjudication package flagged an **~90-file `r7`–`r10` `VacuumEngine3D` driver family** (`src/scripts/vol_1_foundations/r{7,8,9,10}_*.py`) as "sampled V-active, not exhaustively triaged." Current-branch glob confirms **80 files** in that family still present (consistent with the "~90-file" estimate; the original pass didn't claim an exact count either).

**Sampled example (per adjudication package):** `src/scripts/vol_1_foundations/r10_path_alpha_v14_single_cell_boundary.py` — confirmed still present, confirmed coupled-engine relevant (49 matches: imports `ave.topological.vacuum_engine.VacuumEngine3D` at line 65, plants `V_inc` directly, references "the engine's internal CoupledK4Cosserat").

**Disposition for the bucket: NEEDS-TRIAGE.** One sample confirming relevance does not clear the other ~79 files — some may be V-quiet controls (LOW by the adjudication package's own criterion), some may be pre-F1-mechanism (standalone `K4Lattice3D`, not `CoupledK4Cosserat`), and some may be genuinely HIGH. This bucket is registered survey debt, not scheduled work in this pass.

## Explicit non-claims

- **No banked verdict is flipped by this document.** Not genesis-24's VERDICT B, not the node-birth D1–D4 rebin, not cross-sector-pump's FORM-BUT-NO-FIRE, and G-PERSIST ★RULED / ★PROPOSED-RULED are explicitly untouched.
- RE-RUN / CAVEAT-IN-RESULT / NEEDS-TRIAGE are **scheduling dispositions**, not outcomes. A RE-RUN can come back verdict-identical (as the blob-ablation A2 patched-ordering diagnostic already did, at +0.0000%, per the adjudication package).
- This pass does not touch engine code, does not re-run any driver, and does not edit any of the six HIGH result docs. It is scheduling only.

## Recommended next action — cheap re-run priority (top 3 of the six HIGH rows)

1. **`cross-sector-pump-confirmation`** — re-run `cross_sector_pump_confirmation.py` on the fixed engine. Highest value: a null result on the exact shared-front delivery channel F1's fix changes is the single most informative cheap check available.
2. **`genesis-24-saturated-seed`** — re-run `genesis_24_saturated_seed.py` (reuses genesis-23 machinery, N=24/40 steps — cheap). Confirms whether the VERDICT-B source-channel-FIRES number is bond-Γ-sensitive.
3. **`genesis-node-birth-discriminator`** — re-run `genesis_node_birth_discriminator.py` (frozen prereg + driver already wired). Confirms whether D1–D4 gate numbers move under the corrected ordering.

The two G-PERSIST-family rows (`gpersist-localization-observable`, `genesis-npersist-n14-battery`) and the option-B discrete-emergence row are intentionally **not** in this top-3 — they carry standing ★RULED/★PROPOSED-RULED gates or heavy prior adjudication, and reopening them is a Grant-level call, not a cheap re-run.

---
*Docs-only audit. Engine untouched by this document. Grant adjudicates any re-run scheduling or ruling reopening.*
