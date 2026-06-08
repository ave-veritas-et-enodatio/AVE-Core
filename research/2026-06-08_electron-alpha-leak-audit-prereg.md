# Prereg: electron α leak proxy audit (Phase 2 / Workstream 1)

**Status:** FROZEN PREREG.
**Parent:** `2026-06-08_electron-genesis-finish-adjudication.md`, Theorem 3.1′ (`theorem-3-1-q-factor.md`).
**Driver:** `src/scripts/vol_1_foundations/electron_alpha_leak_audit.py`.

---

## §0 Question

On the **persistent native trap** (snap @ trap_amp=1.5, Γ≈−0.994), which dynamic observable equals **α ≈ 0.0073**?

Candidates (α-free computation, comparison-only scoring):

| ID | Proxy | Corpus basis |
|----|-------|--------------|
| P1 | `ε_Γ = 1 − Γ²` | Current driver convention |
| P2 | `ε_S = 1 − S²_combined` | Axiom-4 kernel at core |
| P3 | `ε_μ = 1 − S_μ²` | Meissner magnetic sector |
| P4 | `ε_ε = 1 − S_ε²` | Electric sector |
| P5 | `|ΔE_shell|/E_shell` per Compton window | Energy leak per cycle |
| P6 | `|ΔH|/H` per Compton window | Hamiltonian leak (lossless test) |
| P7 | `(1 − |Γ|)` at bond | Reflection short of unity |
| P8 | `1/Q_decay = |ΔE|/E` per cycle | Tank Q from decay |

Theorem 3.1′ target: **`1/Q = α`** per Compton cycle through **R = Z₀/(4π)** boundary.

---

## §1 Predictions

**Primary (A):** At least one proxy lands within **10% of α** (|proxy−α|/α < 0.1) without fitting.

**Alternative (B):** `ε_Γ` is correct but Γ not deep enough — best proxy still P1 with |ε−α|≈0.005.

**Null (C):** **No** proxy within 10%; all cluster ~0.012–0.013 or ~0 — implies **wrong measurement set** or **missing dissipative channel** (CAST).

**Falsifier for P5/P6 as α:** If H_total conserved (|ΔH/H| < 1e−4 per cycle) while ε_Γ≈0.013 — lossless engine cannot exhibit Theorem 3.1′ per-cycle leak.

---

## §2 Protocol

- Reuse genesis snap: amp 0.48 → trigger x≥14 → trap 1.5 → 800 post steps, zero drive.
- Sample at cadence 2 on shell around core.
- Compton window: `T = 2π/ω_yield`, `steps_per_cycle = T/dt`.
- `alpha_used_as_input: false`.

---

## §3 Outcomes

| Outcome | Criterion |
|---------|-----------|
| A | Best proxy within 10% of α |
| B | P1 best but >10% off |
| C | No proxy within 10%; lossless H conserved |

---

## §4 Result

```bash
PYTHONPATH=src python src/scripts/vol_1_foundations/electron_alpha_leak_audit.py
```

**JSON:** `src/scripts/vol_1_foundations/_output/electron_alpha_leak_audit_results.json`

## §5 Adjudication

**Verdict: `LEAK_PROXY_NONE_MATCH` (Outcome D) — no proxy within 10%**

| Proxy | Mean value | \|val−α\| | Q_proxy | Notes |
|-------|------------|----------|---------|-------|
| **P7** `(1−\|Γ\|)` | **0.00632** | **0.00097** | 158 | **Closest** (~13% rel err) |
| P6 `ΔH/H` per cycle | 0.00457 | 0.00273 | — | Integrator drift? not Z₀/4π load |
| P5 `ΔE_shell/E` per cycle | 0.00340 | 0.00390 | 294 | |
| **P1** `1−Γ²` | 0.01261 | 0.00531 | 79.3 | Previous scoring convention |
| P2–P4 `1−S²` | 0 | 0.00730 | — | Core fully saturated (S→0) |
| P9 `1/z²` | 1 | — | — | z large at wall; not α |

**Key reads:**

1. **`ε_Γ = 1−Γ²` is not the closest proxy** — `(1−|Γ|)` is nearer but still **~13% short of α** (algebraically ε ≈ 2(1−|Γ|) near TIR).
2. **S-sector proxies vanish** at core — Meissner already at S_μ,S_ε→0; they cannot encode α leak.
3. **H is not conserved** (P6 > 0) but per-cycle drift **≠ α** — not yet Theorem 3.1′ boundary load.
4. **Target Γ = −√(1−α)** would give ε=α and (1−|Γ|)≈0.0037 — still **not** α; perfect TIR shortfall is the wrong axis.

**Conclusion:** Gap is **not** fixed by re-scoring alone. **Workstream 2** (explicit **R = Z₀/(4π)** dissipative boundary / CAST→TUNE) is the mandated next step.
