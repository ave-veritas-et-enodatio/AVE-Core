# F6 field channel — prereg FROZEN (Grant-GO 2026-07-15)

**Date:** 2026-07-15  
**Charter:** [`2026-07-15_f6-field-channel_CHARTER.md`](2026-07-15_f6-field-channel_CHARTER.md)  
**Grant GO:** in-chat "2. proceed" (2026-07-15)  
**Class:** prereg — freeze-by-push BEFORE driver results.  
**Driver:** `src/scripts/vol_1_foundations/f6_field_channel.py`  
**Tests:** `src/tests/test_f6_field_channel.py`

> ★ **FROZEN.** §1–§4 below are locked before any RESULT append. Do not retune bins after fire.

---

## §1 Hypothesis

A **field-coupled one-way door** can attach to the live reversible lattice without detonating it: an ε-latent store (parallel to the reactive TLM Hamiltonian) drains into a T2 bath accumulator at a rate slaved to a live occupancy proxy read from the lattice, while the reactive interior stays positive-definite and Ax3-reversible when the channel is OFF.

**First rung (this prereg):** prove **BOUNDED transfer exists** (charter bin i) vs DETONATE / BIAS-MOVED / ELECTRON-DRAIN / NULL — not yet full in-Hamiltonian ε depletion of V_inc (that class killed once as `photon_deplete`; deferred to a later rung if bin i passes).

---

## §2 Frozen bins (charter §4 verbatim statuses)

| Bin | Name | Fire when |
|---|---|---|
| **(i)** | **CHANNEL-BOUNDED** | ON: `E_bath` rises, `E_latent` falls, `\|ΔE_latent+ΔE_bath\| ≤ tol_cons`; TLM energy finite every step; OFF recovers reversible baseline (TLM energy drift ≤ tol_off) |
| **(ii)** | **DETONATE** | any NaN/Inf or TLM/`E_latent` runaway (`max\|E\| > DETONATE_FLOOR`) under ON |
| **(iii)** | **BIAS-MOVED** | mean operating-point proxy (`mean S` or mean `z_local`) ON vs OFF differs by > `BIAS_TOL` |
| **(iv)** | **ELECTRON-DRAIN** | held high-A² blob TLM energy drops under ON by > `DRAIN_TOL` relative to OFF (channel must not steal reactive energy) |
| **(v)** | **NULL** | ON indistinguishable from OFF on `E_bath` (`ΔE_bath < NULL_FLOOR`) |

**Decision rule:** (ii)/(iii)/(iv) fail-closed. Only (i) licenses thermometer re-fire / deeper field-depletion rung. (v) = not implemented.

---

## §3 Method (frozen)

1. Platform: `CoupledK4Cosserat` (natural units), small N, no PML required for ledger rung.
2. Occupancy proxy: `n = clip(mean(A²_cos + A²_k4), 0, 1)` over interior (read-only).
3. Latent store: scalar `E_latent` (and optional per-site mirror for diagnostics) — **not** part of TLM energy.
4. Channel ON: each outer step `dE = κ · n · E_latent · dt_eff` with `dE ≤ E_latent`; `E_latent -= dE`; `E_bath += dE`.
5. Channel OFF: κ = 0.
6. Controls: clean OFF run; ON run; bias compare; high-A² seed for drain detector.
7. `classify()` in driver — single source of thresholds (mirrored in tests).

---

## §4 Tolerances (frozen)

```
TOL_CONS = 1e-9
TOL_OFF = 1e-6          # relative TLM energy drift OFF over run
DETONATE_FLOOR = 1e6    # |E| or |E_latent| blow-up
BIAS_TOL = 1e-3         # |mean_S_ON - mean_S_OFF|
DRAIN_TOL = 0.05        # relative TLM energy loss ON vs OFF on blob
NULL_FLOOR = 1e-12      # ΔE_bath
KAPPA = 0.1             # free transfer rate (CONSISTENCY-class; not derived)
N_STEPS = 200
```

---

## §5 Result (append only after freeze push)

**Fired 2026-07-15 (same session as freeze; classify frozen before run).**

```
VERDICT = CHANNEL-BOUNDED
  ON  E_bath ≈ 0.138   E_latent ≈ 0.862   ledger residual ~1e-15
  OFF E_bath = 0       mean_S ON = mean_S OFF (bias OK)
  blob TLM ON = OFF (electron-no-drain OK)
```

Driver: `src/scripts/vol_1_foundations/f6_field_channel.py`. Tests: 5 passed (`test_f6_field_channel.py`).

**Honest scope of this rung:** occupancy-slaved **parallel latent→bath ledger** on a live `CoupledK4Cosserat` — proves the door can attach without detonating / bias-moving / draining reactive TLM energy. **Does not** yet deplete in-Hamiltonian ε (V_inc); that deeper rung remains queued behind this CHANNEL-BOUNDED bank.
