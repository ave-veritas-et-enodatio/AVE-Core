# F6 field channel — rung-2 prereg FROZEN (in-Hamiltonian ε→bath)

**Date:** 2026-07-15  
**Prior rung:** [`2026-07-15_f6-field-channel_prereg_FROZEN.md`](2026-07-15_f6-field-channel_prereg_FROZEN.md) — CHANNEL-BOUNDED (parallel latent ledger).  
**Charter:** [`2026-07-15_f6-field-channel_CHARTER.md`](2026-07-15_f6-field-channel_CHARTER.md)  
**Driver:** `src/scripts/vol_1_foundations/f6_field_channel_rung2.py`  
**Class:** prereg — freeze-by-push BEFORE results.

> ★ **FROZEN.** §1–§4 locked before RESULT.

---

## §1 Hypothesis

An **energy-conserving** one-way transfer can remove energy from the reactive V-field into a T2 bath accumulator **without** an indefinite Hamiltonian: scale unprotected `V_inc`/`V_ref` so ΔE_field = −δ and E_bath += δ. A protect-mask around a held core enforces electron-no-drain. This is the first *in-Hamiltonian* door (distinct from rung-1’s parallel latent store).

**Kill class avoided:** `photon_deplete`-style continuous loss with no bath credit (indefinite H). Here total `E_field + E_bath` is conserved by construction.

---

## §2 Bins (same names as charter)

| Bin | Fire when |
|---|---|
| **CHANNEL-BOUNDED** | ON: E_bath↑, field energy↓, `\|ΔE_field+ΔE_bath\|≤tol`; finite; protect-mask core energy ON≈OFF |
| **DETONATE** | NaN/Inf/runaway |
| **BIAS-MOVED** | mean S ON vs OFF > BIAS_TOL on protected core |
| **ELECTRON-DRAIN** | protected-core field energy drops ON vs OFF > DRAIN_TOL |
| **NULL** | E_bath < NULL_FLOOR under ON |

---

## §3 Method

1. Platform: native `K4Lattice3D` (V-sector; matches thermometer lineage).
2. Seed traveling bath energy outside a spherical protect core; core holds a mild clock blob.
3. Each step after `lat.step()`: compute field energy on unprotected sites; transfer `δ = min(κ·E_unprot·dt_fac, E_unprot)`; scale unprotected V by `√(1−δ/E_unprot)`; `E_bath += δ`.
4. OFF: κ=0.
5. `classify()` frozen in driver.

---

## §4 Tolerances

```
TOL_CONS = 1e-8
DETONATE_FLOOR = 1e6
BIAS_TOL = 5e-3
DRAIN_TOL = 0.05
NULL_FLOOR = 1e-12
KAPPA = 0.05
N_STEPS = 150
N = 12
CORE_R = 2.5
```

---

## §5 Result

**Fired 2026-07-15 (same session; classify frozen before run).**

```
VERDICT = BIAS-MOVED
  ON  bath≈7.57  field≈0.11  core≈0.059
  OFF bath=0     field≈7.68  core≈0.31
  soft_ledger |ΔE_field − bath| ≈ 3.8  (scatter redistributes; not a clean transfer)
```

**Honest closure (Rule 11):** the naive in-Hamiltonian scale-down of unprotected `V` **fails bias≠release** (and visibly couples into the protected core via scatter). This implementation class is **not** CHANNEL-BOUNDED as posed. Do **not** retune κ/mask to chase a pass — record the kill-shape. **Next door:** discriminator charter [`2026-07-15_f6-mode-count-door_CHARTER.md`](2026-07-15_f6-mode-count-door_CHARTER.md) (mode-count irreversibility without sub-yield friction). **Do not** pre-name “matched-termination Re(Z) absorb” as the plan (Grant 2026-07-15).

Thermometer re-fire remains **gated** on a CHANNEL-BOUNDED in-Hamiltonian door.
