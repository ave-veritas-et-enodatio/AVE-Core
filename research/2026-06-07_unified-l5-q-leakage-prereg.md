# Prereg: L5 alpha-free Q/leakage on unified projection lane

**Status:** FROZEN PREREG before driver run.
**Branch:** `analysis/2026-06-07-two-node-alpha-projection`.
**Parent:** `research/2026-06-07_electron-genesis-observer-bridge-prereg.md` §10.
**Sweep context:** `research/2026-06-07_unified-amplitude-gamma-sweep-prereg.md` §8.
**Driver:** `src/scripts/vol_1_foundations/unified_l5_q_leakage.py`.

---

## §0 Question

On the unified `MasterEquationFDTD + PhasorBridge` lane, does an **alpha-free** leakage/Q measurement land near **137** (fine structure), **4π** (geometry/radiation scale), or neither — at the two calibration-crux amplitudes?

| Case | Amplitude | Prior sweep finding |
|------|-----------|---------------------|
| Rest scale | 0.48 | `A²_peak ≈ 0.23`, `Γ_min ≈ −0.005` (matched bulk) |
| Wall window | 3.0 | `Γ_min ≈ −0.49`, bounded trap, no pump |

## §1 Classification

**Test class:** Class D emergence probe (alpha-free observables only).

**Inputs forbidden:** `alpha` as damping, Q target, loss coefficient, or fitted normalization.

**Inputs allowed:** scalar field `V`, projected `V_inc/V_ref`, bond `Γ` from `z_local(S(A))`, energy trace, geometry integrals (Λ-style decomposition).

**Comparison-only imports:** `ALPHA_COLD`, `ALPHA_COLD_INV`, `4π` — never enter computation.

## §2 Alpha-free observables (pre-registered)

1. **Bond leak fraction:** `ε_Γ = ⟨1 − Γ²⟩` on high-strain shell bonds (uncapped `S(A)` observer).
2. **Bond Q proxy:** `Q_Γ = π / ε_Γ` when `ε_Γ > 0` (one-bounce leakage scale).
3. **Phasor reflection ratio:** `ρ = Σ|V_ref|² / Σ|V_inc|²` in shell; `ε_ρ = ρ/(1+ρ)`; `Q_ρ = π/ε_ρ`.
4. **Λ decomposition:** `Q_Λ = L_vol + L_surf + L_line` from normalized `|V|²` (r10-style, alpha-free integral).
5. **Ring-down Q:** fit center-probe envelope post-transient; `Q_decay = π · f · τ` from decay time constant `τ` and estimated breathing frequency `f`.

## §3 Predictions before run

**Primary prediction:** **Outcome C — no alpha-scale signal at either amplitude.**

Reason: prior sweep shows rest scale has no short wall; wall scale has `Γ ≈ −0.5` not `Γ → −1`; Λ-sum on a planted sech blob without Golden-Torus geometry projection is not expected to reproduce Op21 mode-count **137**; bond/phasor Q proxies measure observer leakage, not Theorem 3.1' integrated TIR boundary.

**Secondary predictions:**

- Rest (0.48): lower `ε_Γ`, higher `Q_Γ` than wall (3.0) — matched bulk leaks less.
- Wall (3.0): `ε_Γ` rises as `|Γ|` approaches 0.5; still unlikely `ε_Γ ≈ α ≈ 0.0073` without `Γ → −1`.
- If any proxy lands within 15% of `4π`, classify as **geometry scale**, not fine structure.

## §4 Outcome table

| Outcome | Criterion | Interpretation |
|---------|-----------|----------------|
| A | Any alpha-free proxy within 15% of `137` at **both** amplitudes | Emergence candidate — auditor review |
| B | Proxy within 15% of `4π` at one amplitude | Geometry/radiation scale only |
| C | No proxy within 15% of `137` or `4π` | L5 negative; calibration/crux still open |
| D | Rest and wall proxies disagree on scale class | Amplitude-dependent leakage (expected partial) |

## §5 Honest scope limits

- Planted sech seed, not rupture→pair chain.
- Projection bridge is read-only; not native K4-TLM dynamics.
- Λ decomposition here is a field integral proxy, not Op21 Nyquist mode-count.
- Does NOT close α-closure (epic §3); tests whether L5 channel exists on this lane.

---

## §6 Result

Executed with:

```bash
PYTHONPATH=src python src/scripts/vol_1_foundations/unified_l5_q_leakage.py
```

Output: `src/scripts/vol_1_foundations/_output/unified_l5_q_leakage_results.json`

Console summary:

```text
Unified L5 alpha-free Q/leakage
  pair verdict: L5_NEGATIVE_BOTH (C_negative_both)
  case=rest_scale    amp=0.48
    A_peak_trace=0.480  gamma_min_trace=-0.013
    leak_gamma=0.9998  Q_gamma=3.14  bond_q_valid=False
    Q_lambda=568.75  Q_decay=115.97
  case=wall_window   amp=3.00
    A_peak_trace=3.000  gamma_min_trace=-0.634
    leak_gamma=0.598  Q_gamma=5.25  bond_q_valid=True
    Q_lambda=246.67  Q_decay=None
  alpha: comparison-only; not inserted
```

## §7 Adjudication

**Verdict: `L5_NEGATIVE_BOTH` — primary prediction confirmed (Outcome C).**

### Rest scale (amp = 0.48)

- `A²_peak ≈ 0.23` on trace — matches calibration-crux reference.
- `Γ_min ≈ −0.013` — matched bulk; **bond-Q proxy ill-posed** (`bond_q_valid=False`, |Γ| ≪ 0.1).
- `Q_decay ≈ 116` — nearest proxy to 137, but **15.3% below** the preregistered 15% match band (not promoted).
- `Q_Λ ≈ 569` — cell-count integral artifact, not Op21 mode-count.

### Wall window (amp = 3.0)

- `A_peak_trace = 3.0`, `Γ_min ≈ −0.634` on trace — partial short, not `Γ → −1`.
- `ε_Γ ≈ 0.60`, `Q_Γ ≈ 5.25` — confinement weak; leak is O(1), not O(α).
- No ring-down fit (non-monotonic envelope at high amplitude).

### Comparison-only (not inputs)

| Proxy | Rest | Wall | vs 137 | vs 4π |
|-------|------|------|--------|-------|
| `Q_Γ` | 3.14 (ill-posed) | 5.25 | ~20× low | ~0.58× |
| `Q_Λ` | 569 | 247 | ~3–4× high | ~20–40× high |
| `Q_decay` | 116 | — | 15% low | ~9× high |
| `ε_Γ` | ~1.0 | 0.60 | ~80–140× high | — |

**Interpretation (honest):**

1. **No alpha-free proxy lands near 137** at either calibration-crux amplitude on this lane.
2. **Rest scale has no wall** → bond leakage channel is undefined (matched bulk), consistent with sweep.
3. **Wall window shows stronger short** (`Γ_min ≈ −0.63`) but still **O(1) leak**, not `ε ≈ α ≈ 0.0073`. Full TIR (`Γ → −1`) is not reached.
4. `Q_decay ≈ 116` at rest is a **single-channel curiosity**, not emergence — fails tolerance, no wall, no Theorem 3.1' geometry.
5. **L5 closes negative** on the unified projection lane for α emergence. α-closure remains a separate derivation push (epic §3), not a simulation readout here.

**Classification:** Class D emergence test → **negative**. Consistency with calibration crux: leakage/Q require `Γ → −1` + Op21 geometry; this lane has neither at rest scale, and only partial short at wall scale.

## §8 Next targets

1. **C3 phase-gate re-run** on coupled impose harness (FORK D, cheap).
2. **Native K4-TLM amplitude sweep** (not projection) — does pump return in wall band?
3. **Commit + PR** the 2026-06-07 genesis instrumentation branch.
4. **α-closure derivation push** (holonomy + cage leak geometry) — gated on Theorem 3.1' derived-vs-asserted check; not another scalar-lane Q sweep.
