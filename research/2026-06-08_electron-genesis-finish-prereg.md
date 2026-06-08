# Prereg: electron genesis finish (persistence + ε→α at TIR)

**Status:** FROZEN PREREG.
**Parent:** `2026-06-08_electron-genesis-snap-prereg.md`, `2026-06-07_theorem-31-alpha-identity-audit.md` §3 C2.
**Driver:** `src/scripts/vol_1_foundations/electron_genesis_finish.py`.

---

## §0 Question

After discrete snap (propagate 0.48 → full replace at wall amp), does the native trap:

1. **Persist** at Γ ≈ −1 (TIR held post-drive)?
2. **Read out** ε = 1−Γ² → α via Theorem 3.1′ target Γ² = 1−α (C2)?
3. **Pin** without translating (electron as localized object)?

---

## §1 Physical picture

- Snap protocol is **closed** (hybrid/position re-seed at trap_amp ≥ 1.5).
- Theorem 3.1′: at full TIR, per-cycle leak `1/Q = α` ↔ `ε = 1−Γ² = α` when `Γ = −√(1−α) ≈ −0.9964`.
- Session native wall: `Γ ≈ −0.994`, `ε ≈ 0.013` (~1.7× α) — gap may close with trap_amp sweep or post-snap equilibration.
- Finish = **native lane only** (projection lane deferred to bridge Meissner work).

---

## §2 Predictions

**Primary (A):** Post-snap Γ stays ≤ −0.99 for ≥200 steps; pinned (|Δx| < 0.5); `|ε−α|` best case < 0.01 at some trap_amp.

**Alternative (B):** TIR decays post-snap — trap is transient, not electron object.

**Null (C):** No trap_amp in [1.0, 2.5] reaches `|ε−α| < 0.003` — numerical α readout remains open on native lane.

**Falsifier:** Γ rises above −0.9 within 100 post-snap steps at trap_amp=1.5 → snap does not produce persistent wall.

---

## §3 Protocol

- Hybrid snap (same as `electron_genesis_snap.py` position trigger).
- Post-snap: `N_POST=600`, `V_DRIVE=0`.
- Trap amps: `[1.0, 1.25, 1.5, 1.75, 2.0, 2.5]`.
- Score: `gamma_min`, `eps`, `Q_eff_proxy = 1/eps`, `abs_eps_minus_alpha`, `gamma_target = -√(1−α)`.
- `alpha_used_as_input: false`.

---

## §4 Outcomes

| Outcome | Criterion |
|---------|-----------|
| A | Persistent TIR + best `|ε−α| < 0.01` |
| B | TIR decays post-snap |
| C | Persistent TIR but `|ε−α| ≥ 0.003` at all amps (α readout still open) |

---

## §5 Result

```bash
PYTHONPATH=src python src/scripts/vol_1_foundations/electron_genesis_finish.py
```

**JSON:** `src/scripts/vol_1_foundations/_output/electron_genesis_finish_results.json`

## §6 Adjudication

**Verdict: `FINISH_PERSISTENT_TRAP_PROTOCOL_COMPLETE` (native bench)**

| trap_amp | Post-snap | Γ_min | \|ε−α\| | Q_proxy | Notes |
|----------|-----------|-------|---------|---------|-------|
| 1.00 | **DECAYED** | −0.028 | 0.992 | ~1 | Below wall threshold |
| 1.25–2.5 | **HELD 600 steps** | −0.994 | **0.0053** | **~79.5** | Pinned, stable |

**Closed on native lane:**

1. **Minimum trap_amp = 1.25** for persistent TIR (1.0 decays to matched Γ).
2. **Snap protocol is stable** — Γ holds ≥600 steps post-drive at trap ≥ 1.25.
3. **Electron object = pinned localized trap** at motion site (|Δx_post| < 0.02).

**Still open (numerical α):**

- `ε ≈ 0.0126` not `α ≈ 0.0073` — stable **~1.7×** offset.
- `Q_proxy = 1/ε ≈ 79.5` not `1/α ≈ 137` — Theorem 3.1′ leak identity not numerically closed on sim.
- `Γ ≈ −0.994` vs target `−√(1−α) ≈ −0.9963` — gap `|ΔΓ| ≈ 0.0027`.

**Prereg outcome mapping:** aggregate `FINISH_NEAR_ALPHA_READOUT (A)` under loose `|ε−α| < 0.01` gate; **honest physics read = persistent trap yes, exact α readout no.**

**Genesis modeling status:** **bench protocol complete**; **corpus identity (α) not yet measured by engine**.
