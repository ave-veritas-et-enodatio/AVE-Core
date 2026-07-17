# F1 materiality report — does the corrected bond-Γ move any banked verdict?

**Date:** 2026-07-16 · **Class:** Materiality report (docs-only; report-only —
schedules flags, decides nothing, re-runs nothing). · **Lane:** F1 implementer. ·
**Parent:** [`2026-07-16_f1-v-active-consumer-audit_NOTE.md`](2026-07-16_f1-v-active-consumer-audit_NOTE.md). ·
**Standing-verdict guardrails preserved:** G-PERSIST ★RULED and the #706
MODE-SORTING verdict are **not** reopened on the strength of F1 (per
[`_orchestration/2026-07-15_f1-adjudication-package.md`](../_orchestration/2026-07-15_f1-adjudication-package.md)).

## The one-line materiality rule (derived in the audit §3)

> The F1 fix re-routes the V-sector **spatially** but **conserves V energy
> exactly** (power-conserving bond reflection, Γ²+T²=1). It bites a banked
> verdict only if that verdict's load-bearing quantity is a **V-sector spatial
> observable** AND the run had **both** sectors active. Energy-class verdicts and
> verdicts keyed on channels that read `V_sq`/`V_inc` directly (V→ω coupling,
> converter) are invariant to first order.

## Per-consumer materiality (six banked HIGH results)

| Banked doc | Load-bearing quantity | Materiality class | Plausibly moves the verdict? | Disposition |
|---|---|---|---|---|
| `2026-07-12_genesis-node-birth-discriminator_result.md` | `v_inc_peak` feeding **D1–D4 threshold gates** | V-spatial peak at a decision boundary | **Possibly** — a sub-% peak shift can cross a gate iff a gate sits on its boundary; needs the actual gate margins | **FLAG — gated re-run (priority 1)** |
| `2026-06-09_genesis-24-saturated-seed_result.md` | `max|V_inc|→1.08e4`; source-channel-FIRES (VERDICT B) | V-spatial peak in a **pumped runaway** (converter on → E_V not conserved) | Quantitative peak: **yes, may shift**; qualitative FIRES: **robust** (V grows regardless of routing) | **FLAG — gated re-run (priority 2), quantitative only** |
| `2026-07-14_gpersist-localization-observable_RESULT.md` | **localization meter / density-peak core fraction** | V-spatial — the exact class the fix touches | Qualitative LOOP-FILLING: **robust** (both fork cells, √α pump ⇒ A²_V~7e-3, sub-% shift); the meter is under ★RULED-protected fork | **FLAG — confirmation re-run only; do NOT reopen ★RULED (priority 3)** |
| `2026-06-04_full-electron-option-B-discrete-emergence-result.md` | `(V_inc,V_ref)` retention trajectory | V-spatial trajectory | Retention verdict likely **robust**; heavy prior adjudication already corrects driver auto-verdicts | **CAVEAT-IN-PROVENANCE — re-run low priority** |
| `2026-07-13_genesis-npersist-n14-battery_RESULT.md` | E/φ persist (G-PERSIST family) | **energy-class** (E-persist) + weak spatial (φ/Φ_link) | E-persist **invariant** by §3b; φ second-order | **CAVEAT-IN-PROVENANCE — family flag, low priority** |
| `2026-06-09_cross-sector-pump-confirmation_result.md` | **null**: V does not source ω (VERDICT B, FORM-BUT-NO-FIRE) | channel reads `V_sq`/converter force **not** `z_local` | **No** — the pump input is z_local-independent; the fix perturbs only V's spatial pattern by sub-% | **ROBUST — cheap-confirm optional, not required** |

## Flagged-for-gated-re-run list (priority order; this lane does NOT run them)

1. **`genesis_node_birth_discriminator.py`** — the only row where a *threshold
   gate* (D1–D4) sits on a V-spatial peak; a sub-% shift is verdict-relevant iff
   a gate margin is thin. Frozen prereg + wired driver ⇒ cheap. **Highest flip risk.**
2. **`genesis_24_saturated_seed.py`** — pumped runaway; re-run to confirm the
   *quantitative* `max|V_inc|` peak (the qualitative FIRES is mechanism-robust).
3. **`gpersist_localization_observable.py`** — confirmation only: verify the
   LOOP-FILLING localization meter is unmoved; explicitly **not** a reopening of
   G-PERSIST ★RULED (Grant-level call, out of F1 scope).

Rows 4–6 (option-B, npersist, cross-sector-pump) are **mechanism-robust**:
energy-class or z_local-independent channels. Provenance caveat suffices; no
re-run required.

## What this report does NOT claim

- **No banked verdict is flipped or edited here.** FLAG = scheduling only.
- The synthetic before/after (audit §4) shows ≤0.20 % `max|V|` shift and exact
  E_V invariance, but **under-samples the pumped-runaway regime** (the converter
  did not fire on synthetic seeds). The genesis re-runs above are exactly the
  configs where the pump *does* fire — that is why they are flagged rather than
  dispositioned from the synthetic evidence.
- Byte-parity for the immaterial classes is established three ways: V-quiet
  (V≡0), Cosserat-quiet (z_local identical to 6.97e−14), and the blob-ablation
  `--parity` datum reproducing at maxΔ = 0.00e+00 on the fixed engine
  (`blob_ablation_kernel_off.py::cmd_parity`, N=14 pml=3 pair smoke).

---
*Report-only. Grant / orchestrator adjudicates whether the three flagged re-runs
fire. Engine untouched by this document.*
