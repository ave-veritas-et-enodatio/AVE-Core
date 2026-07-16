# F1 adjudication package — Cosserat→V bond-short ordering (DEFECT-CANDIDATE)

**Date:** 2026-07-15 · **Class:** Grant adjudication package (orchestration; not a fix; nothing canonized). · **Source:** PR #706 blob ablation A2 (`research/2026-07-15_blob-ablation_NOTE.md`:496–537). · **Companion:** hardware-ratings-map R10 / §3 item 4; ratings-map anchor sweep same branch.

## The question for Grant

Is the shipped `CoupledK4Cosserat` update ordering a **DEFECT** (fix + regression + consumer re-check) or a **deliberate V-only master** (reconcile design comments; demote the shared-front claim)?

> **★RULED — DEFECT (Grant 2026-07-15, in-chat: "1. fix it").** Cosserat load must be able to set bond Γ for V-pulses. Fix landed: `K4Lattice3D.external_z_local=True` under `CoupledK4Cosserat` so `_scatter_all` does not overwrite the shared front; regression `src/tests/test_f1_shared_front_ordering.py`. Consumer-audit completion (HIGH rows + r7–r10 triage) remains registered follow-on — not blocking the fix.

## Mechanism (re-verified 2026-07-15, two-method)

| Step | What happens | File:line |
|---|---|---|
| 1 | Coupling writes Cosserat-informed shared front `Z_eff=√(S_μ/S_ε)` into `k4.z_local_field` | `k4_cosserat_coupling.py:874` (`_update_z_local_total`) |
| 2 | `k4.step()` → `_scatter_all()` first action, gated on `op3_bond_reflection` | `k4_tlm.py:298–304` |
| 3 | `_update_z_local_field()` recomputes `z_local = 1/√S(V)` from **V_inc only** and **overwrites** the coupling write | `k4_tlm.py:271–294` |
| 4 | `_connect_all()` consumes the (now V-only) `z_local` for bond Γ | after overwrite |

`op3_bond_reflection=True` is **hardwired** in the coupled constructor (`k4_cosserat_coupling.py:306`) — not a user toggle. Design comments at `:373–375`, `:866`, `:897` assert the shared front survives into the bond short; the ordering contradicts them. **No corpus comment supports V-only-as-master.**

**Symptom by regime:** V quiet → flat `z≡1.000`; V excited → wrong V-only `1/√S(V)` instead of the asymmetric shared front (does **not** self-heal).

**Empirically immaterial at the #706 config:** patched-ordering diagnostic reproduced the MODE-SORTING datum to **+0.0000%** (V-sector ~0 energy). Verdict MODE-SORTING stands either way at that config.

## Consumer-audit survey (first pass — registered follow-on ii)

Full inventory in session trail; durable HIGH/LOW summary:

### HIGH risk (V-active coupled runs; banked numbers may depend on wrong bond-Γ)

| Result | Why HIGH |
|---|---|
| `research/2026-06-09_genesis-24-saturated-seed_result.md` | `max\|V_inc\|→1.08×10⁴`; growing V-sector |
| `research/2026-07-14_gpersist-localization-observable_RESULT.md` | sustained `√α` V-pump every quiet step |
| `research/2026-07-12_genesis-node-birth-discriminator_result.md` | nonzero `v_inc_peak`; E/φ persist gates |
| `research/2026-07-13_genesis-npersist-n14-battery_RESULT.md` | same detector family (presumed; family flag) |
| `research/2026-06-04_full-electron-option-B-discrete-emergence-result.md` | `(V_inc,V_ref)` retention trajectory |
| `research/2026-06-09_cross-sector-pump-confirmation_result.md` | explicit sustained V-to-yield drive |

### LOW / immaterial (own diagnosis: V≈0 or diagnostic already neutral)

| Result | Why LOW |
|---|---|
| `research/2026-06-09_reflection-genesis-23-self-assembly_result.md` | `max\|V_inc\|=0` machine-precision, in-doc |
| `research/2026-07-15_blob-ablation_NOTE.md` | patched-ordering +0.0000% |

### Open gap (not exhaustively triaged this pass)

~90-file `r7`–`r10` `VacuumEngine3D` driver family — sampled V-active (`r10_path_alpha_v14_single_cell_boundary.py`); treat as **HIGH-priority survey debt**, not clear.

Platforms outside `CoupledK4Cosserat` / `VacuumEngine3D` (srs scalar, fdtd_3d, crystal_engine cage) = **N/A**.

## Registered follow-ons (do NOT fire until Grant rules)

1. **Ordering fix** — consume coupled shared-front short before V-only recompute, *or* reconcile the two kernels + update design comments — plus regression that F1 cannot recur.
2. **Consumer audit completion** — triage the `r7`–`r10` bucket; for each HIGH row, decide re-run / caveat / leave (expected verdict-neutral only where V was quiet).
3. **Blob re-run on fixed engine** — cheap; expected MODE-SORTING-neutral per diagnostic.

## Recommended ruling shape (orchestrator, non-binding)

**Lean DEFECT** — comments + "one front, both sectors (CP2)" design claim + hardwired flag with no deliberate-master receipt. Scope the fix narrowly (ordering / consume-before-overwrite); do **not** reopen G-PERSIST ★RULED or the #706 MODE-SORTING verdict on the strength of F1 alone.

**If FEATURE instead:** rewrite comments + demote the shared-front Cosserat→V short to "not implemented"; leave HIGH consumers flagged as V-only-Γ banked.

---
*Surfaces only. Grant adjudicates. Engine untouched on this branch.*
