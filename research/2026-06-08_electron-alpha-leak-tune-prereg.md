# Prereg: CAST→TUNE — Z₀/(4π) radiation leak on electron trap shell

**Status:** FROZEN PREREG.
**Parent:** `2026-06-08_electron-alpha-leak-audit-prereg.md` (Workstream 1: no proxy within 10%).
**Driver:** `src/scripts/vol_1_foundations/electron_alpha_leak_tune.py`.

---

## §0 Question

Does adding a **substrate-native per-cycle leak** at the trapped shell — fraction **α per Compton cycle** (Theorem 3.1′, load **R = Z₀/(4π)**) — drive **ε_Γ → α** on the bond readout?

Workstream 1 showed re-scoring alone fails. This tests the **missing dissipative channel** hypothesis.

---

## §1 Mechanism (forward, α not a fit knob)

Per Theorem 3.1′: stored energy fraction leaking per Compton cycle = **1/Q = α**.

Implementation (natural units, driver-side shell drain):

```
steps_per_cycle = (2π/ω_yield) / dt_outer
leak_per_step   = 1 − (1 − α)^(1/steps_per_cycle)
scale           = √(1 − leak_per_step)   on shell V_inc, V_ref, ω
```

`α` imported only as **corpus target leak rate** (comparison discipline: leak rate = ALPHA_COLD, not fitted to ε).

---

## §2 Predictions

**Primary (A):** With leak enabled, time-averaged **P5/P6 per-cycle leak ≈ α** and **P1 ε_Γ moves toward α** (|ε−α| < 0.003).

**Alternative (B):** Leak rate matches α by construction but **ε_Γ unchanged** — energy drain decoupled from bond-Γ readout; need reactance-boundary coupling.

**Null (C):** Leak destabilizes trap (Γ leaves TIR).

---

## §3 Outcomes

| Outcome | Criterion |
|---------|-----------|
| A | Persistent TIR + \|ε_Γ−α\| < 0.003 with leak |
| B | TIR held, leak rate ≈ α, ε_Γ still ~0.0126 |
| C | TIR lost with leak |

---

## §4 Result

```bash
PYTHONPATH=src python src/scripts/vol_1_foundations/electron_alpha_leak_tune.py
```

**JSON:** `src/scripts/vol_1_foundations/_output/electron_alpha_leak_tune_results.json`

Runtime ~8.5 min (baseline + with-leak variants, 800 post-snap steps each).

## §5 Adjudication

**Verdict: `TUNE_DESTABILIZED_TRAP` (Outcome C) — explicit α/cycle shell drain collapses TIR**

| Variant | TIR held? | P1 ε_Γ | \|ε−α\| | P5 shell leak/cycle | P6 H leak/cycle | Γ_min post | Γ_final post |
|---------|-----------|--------|---------|---------------------|-----------------|------------|--------------|
| baseline (no leak) | yes | 0.01261 | 0.00531 | 0.00340 | 0.00457 | −0.994 | −0.994 |
| with α leak | **no** | **0.587** | **0.580** | 0.01546 | 0.01592 | −0.994 | **≈0** |

**Applied leak (forward, not fit):** `mean_leak_per_step = 0.002586` from `1−(1−α)^(1/steps_per_cycle)`; `α = ALPHA_COLD` only as corpus target rate.

**Key reads:**

1. **Null (C) wins.** Post-snap Γ_min still hits TIR briefly, but **Γ_final → 0** — trap does not persist under shell drain.
2. **ε_Γ does not move toward α** — it **explodes** (0.0126 → 0.587). Drain is not a gentle bond-readout correction; it **unpins** the Meissner/TIR bound state.
3. **Measured P5 ≈ 0.0155 is not α** — ~2× α, but this is a **post-collapse** slope artifact (shell energy redistributes as TIR is lost), not validation of Theorem 3.1′ coupling.
4. **Baseline unchanged** vs Workstream 1 — lossless trap still ε_Γ ≈ 0.0126, TIR held; Outcome D on baseline arm.

**Conclusion:** The **missing dissipative channel cannot be a naive per-step √(1−α/N) scale on the existing trap shell** without destroying the bound state. Next options (not in this prereg):

- **Couple leak to reactance boundary** (drain only radiative outward flux, not total shell phasor amplitude).
- **Self-consistent eigenmode** (Golden Torus / `tlm_electron_soliton_eigenmode`) where α leak is part of the closed orbit, not bolted onto a manually snapped trap.
- **Recalibrate leak geometry** — shell radius / load impedance matching before re-testing ε_Γ readout.
