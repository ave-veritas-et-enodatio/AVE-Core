# RESULT — X44 Komar / redshift-weighted source reconciliation

**Date:** 2026-07-12 · **Lane:** implementer · **Branch:** `analysis/x44-komar-source`
**Status:** engine + gates landed; **frozen bin (iii) UNRECONCILED**. **NOT merged**
(Grant / orchestrator merges via reviewed PR).
**FROZEN prereg:** `research/2026-07-12_x44-komar-source_prereg_FROZEN.md`
(freeze-by-push: prereg `b9f88823` BEFORE engine `4254034e` / this result).
**Class:** consistency / **CERTIFICATION-class reconciliation attempt** of the latent
`#86` M_eff-vs-far-field gap. **No chord.** α-CLEAN (gravity sector).

---

## 0 · One-paragraph summary

Grant RULED (c) 2026-07-12 authorized replacing the Picard source
`T₀₀^src = T₀₀^matter + u_field` with the redshift / Komar weight
`T₀₀^src = T₀₀^matter · √S(A)` (no separately-added `u_field`), expecting the
far-field Gauss flux to reconcile with the engine's own-labeled ADM mass
`M_eff = M − U_bind`. The weight is installed as the **default**
(`source_mode="komar"`); legacy ADD is retained behind `source_mode="add_field"`
(KEEP-BOTH). **Verdict: frozen bin (iii) UNRECONCILED.** Across the `#651`
fixed-rest-energy family, `η_mixed = slope(m_g/M_eff − 1 vs f)` is
**+1.048 (N=24), +1.049 (N=32), +1.050 (N=40)** — O(1), stable under resolution,
far above the reconcile tol `|η| < 1×10⁻³`. The fireable identity
`Δ_clock = ∫ T₀₀(1−√S)` vs `U_bind = ∫ ½g|∇ε₁₁|²` also FAILS MATCH
(relative mismatch ~93–97%; `Δ_clock/U_bind ~ 0.03–0.07`). Gauss flux ≡ ∫T₀₀^src
holds (install-tautology). No √S → S / 1/S retune was performed (prereg out-of-scope).
Escalation to Grant: the ruled Picard weight and the strain-energy ADM label are
**different functionals**; installing √S alone does not close the `#86` gap.

---

## 1 · STEP-0 (from frozen prereg; not re-litigated)

Authorized-open after `#651`. Current ADD source read M+U; designated ADM is M−U;
mixed η≈2.28 exposed the latent defect. RULED (c) = Komar √S weight as Picard
source. Diamond-K4 Grad/Div inherited from `#86` (D1 non-canonical; flag only).

## 2 · Substrate-native (walked; unchanged from prereg)

- **K4:** same `_build_native_grad_div` as `#86` / `#651`. Gauss residual on
  enclosed flux vs ∫T₀₀^src remains < 1×10⁻⁴ (measured ~10⁻⁶–10⁻⁷).
- **Sector:** A1 dilatation / gravity. Mass = A1 untouched.
- **Op14:** `S(A)=(1−A²)^{1/2}`, weight `√S` as ruled. No new kernel.
- **A46/A47:** real-space; certification / consistency. α-CLEAN.

## 3 · What shipped

| piece | change |
|---|---|
| `backreaction.komar_weight` / `build_picard_source` | √S weight; modes `komar` (default), `add_field`, `matter` (diagnostic bare control) |
| `solve_backreaction` | default `source_mode="komar"`; returns `Delta_clock` |
| `#86` suite | g_self=0 Stage-1 recovery pinned to `add_field`; check4 mode-aware |
| Nordtvedt LEG-1 | live gate = flux vs `M_eff`; records frozen bin (iii) |
| P11 | teeth = relative Δη recovery (baseline may be O(1)) |
| Legacy ADD mixed | KEEP-BOTH: η_mixed ≫ 1 still fires under `add_field` |

## 4 · LEG-1 / η_mixed family (N=24 live gate)

| σ | f | m_g | M_eff | (m_g−M_eff)/M_eff | Δ_clock/U | max A |
|---|---|---|---|---|---|---|
| 1.40 | 0.0561 | 3.98386 | 3.76225 | +5.89×10⁻² | 0.068 | 0.188 |
| 1.80 | 0.0397 | 3.99234 | 3.83443 | +4.12×10⁻² | 0.046 | 0.131 |
| 2.20 | 0.0300 | 3.99574 | 3.87645 | +3.08×10⁻² | 0.034 | 0.099 |
| 2.60 | 0.0234 | 3.99721 | 3.90423 | +2.38×10⁻² | 0.027 | 0.079 |

- **η_mixed(N=24) = +1.048** ≥ 1×10⁻³ ⇒ **bin (iii) UNRECONCILED**.
- Δ_clock↔U_bind: max relative mismatch **0.973** (≥ 0.30) — MATCH fails.
- Converged, max A < 0.2, Gauss identity PASS, monopole plateau PASS.
- Picard contractive (bin iv does not fire).

### 4a · η_mixed-vs-N receipt (prereg gate #3)

| N | η_mixed | notes |
|---|---|---|
| 24 | +1.0479 | live gate |
| 32 | +1.0489 | |
| 40 | +1.0502 | |

**Not resolution-limited.** The O(1) slope is stable to ~0.2% across N∈{24,32,40}.
Banking basis for unreconciliation = the measured slope + the analytic mismatch
of functionals (§5), not an N=24 accident.

## 5 · Why √S did not close the gap (honest mechanism)

Under Komar:

```
m_g  = ∫ T₀₀^src = ∫ T₀₀^matter √S = M − Δ_clock ,   Δ_clock = ∫ T₀₀(1−√S)
M_eff = M − U_bind ,   U_bind = ∫ ½ g_self |∇ε₁₁|²
```

Weak-field: `√S ≈ 1 − A²/4` ⇒ `Δ_clock ∼ ∫ T₀₀ A²/4`, while `U_bind ∼ ∫ ½|∇ε|²`.
These are **different functionals** (prereg § analytic expectation #3, pre-declared
fireable). Measured `Δ_clock / U_bind ~ 0.03–0.07` in this band ⇒ flux sits near M
while `M_eff` deficits by a much larger U_bind ⇒ `m_g/M_eff − 1 ∼ O(f)` with
slope η_mixed ∼ +1.

**Additional structural fact (surfaced, not retuned):** under `source_mode="komar"`,
`g_self` does **not** enter the Picard source (only the U_bind / M_eff *ledger*).
The historical check4 g_self-ON/OFF discriminator is therefore vacuous under Komar
(engage_ratio ≡ 1 when comparing g_self). Legacy ADD still engages at **2.38×**
(KEEP-BOTH). A `matter` control mode isolates √S-vs-bare for future work.

**Not done (prereg forbid):** silent swap √S→S or 1/S; retuning `g_self` so
`U_bind ≈ Δ_clock` to force η→0.

## 6 · `#86` at-risk suite under default komar

| check | result under komar |
|---|---|
| α-clean | PASS |
| field energy / binding deficit definition | PASS |
| g_self=0 → Stage-1 | PASS (pinned to `add_field`) |
| komar default + Δ_clock ≥ 0 | PASS |
| weak converge / bind | PASS |
| recover-GR weak | PASS |
| 1/r monopole | PASS |
| S_min-independent M_eff | PASS |
| ray-trace 4GM | PASS |
| two-mass nonlinearity | mode-aware: ADD KEEP-BOTH PASS (2.38× g_self on/off); Komar komar-vs-matter PASS (2.24× — √S feedback engages) |
| boundedness / energy stationary | PASS |

## 7 · KEEP-BOTH / escalation

- **ADD convention** remains callable; mixed-register η_mixed ≫ 1 still exposes the
  pre-X44 gap under `add_field`.
- **Komar is installed as default** per RULED (c), even though reconciliation
  missed — the ruling was about the source *form*, and the fireable identity was
  pre-declared as a real risk. Bin (iii) means: do **not** claim the `#86` defect
  is closed; escalate options to Grant:
  1. redefine ADM label to `M − Δ_clock` (clock-native inertial mass);
  2. keep ADD for flux / Komar for clock diagnostics (split registers explicitly);
  3. charter a different weight only after a new ruled form (not silent retune);
  4. accept unreconciliation and fence M_eff as a strain-energy diagnostic only.

U6 / A7 freezes untouched (auditor/Grant-gated from `#651`).

## 8 · Deliverables checklist

- [x] FROZEN prereg pushed first (`b9f88823`)
- [x] Engine Komar default + `source_mode` kwarg
- [x] `#86` re-green (mode-aware check4) + Nordtvedt bin-(iii) recorder + η_mixed-vs-N
- [x] This result doc
- [x] Docket continuation row
- [ ] PR `[DO-NOT-MERGE][REVIEW: pending-orchestrator]` — no self-merge
