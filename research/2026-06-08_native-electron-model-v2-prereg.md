# Prereg: Native electron model v2 — dissipative + back-EMF channels

**Status:** FROZEN PREREG.
**Parent:** `native_electron_model.py` (joint seed landed TIR 2/4, ω decay).
**Driver:** `src/scripts/vol_1_foundations/native_electron_model_v2.py`

---

## §0 Question

Do the three missing channels — **V_ref-only boundary leak**, **dark-wake back-EMF on u**, **Lagrangian EMF coupling** — improve 4-property identification + ω persistence on the canonical Golden-Torus seed @ amp=0.92?

WS2 naive total-phasor drain failed (Outcome C). This tests **reactance-boundary** + **reactive back-EMF** hypotheses.

---

## §1 Channels (forward)

| Channel | Implementation | α role |
|---------|----------------|--------|
| Boundary leak | `radiation_leak_boundary.py` — scale **V_ref** (+ partial ω) on shell only | target rate = ALPHA_COLD |
| Back-EMF | `back_emf_feedback.py` — τ_zx opposes `u` along propagation axis | none |
| Lagrangian EMF | `use_lagrangian_emf_coupling=True` on engine | none |

Seed: same as v1 (`quadrature_2_3` + `unknot_sector`), zero drive.

---

## §2 Predictions

**Primary (A):** ≥4/4 properties + ω persistence ≥ 0.5 on at least one channel arm.

**Alternative (B):** 4/4 properties but ω still decays — trap without flywheel.

**Null (C–E):** No improvement or TIR lost.

---

## §3 Outcomes

| Outcome | Criterion |
|---------|-----------|
| A | 4/4 + ω persist ≥ 0.5 |
| B | 4/4, ω persist < 0.5 |
| C | Partial trap (≥2 props + TIR) |
| D | TIR only |
| E | TIR lost |

---

## §4 Result

```bash
PYTHONPATH=src python src/scripts/vol_1_foundations/native_electron_model_v2.py
```

**JSON:** `src/scripts/vol_1_foundations/_output/native_electron_model_v2_results.json`

Runtime ~13 min (5 arms × 800 steps).

## §5 Adjudication

**Verdict: `V2_CHANNELS_NO_BREAKTHROUGH` (stable arms Outcome C; BEMF arms Outcome E)**

Only **baseline** and **boundary_leak** are physically stable (identical 2/4). BEMF/EMF arms are **runaway artifacts**, not circulation restoration.

| Arm | Stable? | Pass | ε̄ | ω persist | Notes |
|-----|---------|------|-----|-----------|-------|
| baseline | yes | 2/4 | 0.0127 | 0.034 | reference |
| boundary_leak | yes | 2/4 | 0.0127 | 0.033 | α/cycle on V_ref only — **no effect** |
| bemf (gain=0.12) | **no** | 2/4* | 0.995 | 1660× | *P3 lost at Γ_final=0 |
| leak+bemf | **no** | 2/4* | 0.995 | 1628× | same runaway |
| leak+bemf+EMF | **no** | 3/4* | 0.998 | 5×10¹¹× | shell R/r≈2.25 — runaway geometry |

**Gain discipline:** boundary leak rate was **forward-calculated** from `ALPHA_COLD`. BEMF `gain=0.12` was **not** derived from \(L_{\text{eff}}\), \(\rho\), or \(Z_0\) — it must not be swept; engine-native coupling required.

**Conclusion:** Tier-1 bolt-on channels **closed negative**. Next: derive feedback strength inside `CoupledK4Cosserat` before any further driver experiments.
