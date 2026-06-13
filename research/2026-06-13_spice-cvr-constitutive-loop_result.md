# RESULT — SPICE-CVR constitutive-loop test (L0/L1/L2 ladder)

**Date:** 2026-06-13  
**Branch:** `analysis/2026-06-13-spice-cvr-constitutive-loop` (off `origin/main`)  
**Prereg (frozen, committed alone first):** [`2026-06-13_spice-cvr-constitutive-loop_prereg.md`](2026-06-13_spice-cvr-constitutive-loop_prereg.md) (commit `036bc486`)  
**Harness:** [`src/ave/solvers/spice_cvr_loop.py`](../src/ave/solvers/spice_cvr_loop.py) — dimensionless $\omega\tau$ ODE ladder  
**Driver:** [`src/scripts/vol_4_engineering/spice_cvr_loop_sweep.py`](../src/scripts/vol_4_engineering/spice_cvr_loop_sweep.py)  
**Data:** `src/scripts/vol_4_engineering/_output/spice_cvr_loop_sweep_results.json`  
**Figures:** `assets/sim_outputs/spice_cvr_loop_*.png`  
**`.lib`:** `AVE_MEMRISTOR_S_STATE`, `AVE_VACUUM_CELL_L1` in [`ave_vacuum_cell.lib`](../src/ave/solvers/spice_models/ave_vacuum_cell.lib) (scaled `TAU_REL`; canonical $\tau_{\mathrm{relax,SI}}\approx 1.288\times 10^{-21}$ s logged in JSON)

**Scope fence (carry):** local constitutive law only — **not** topology / winding / genesis. **REMANENT-LOOP** proves the retention mechanism exists in silico; **does not make an electron.**

---

## 0. VERDICT — **REMANENT-LOOP**

> **L0** reads $\oint=0$, $B_r=0$ (anhysteretic null). **L1** opens a rate-dependent pinched loop ($\oint$ grows with $\omega\tau$, peaks near $\omega\tau\sim 1$) but **does not latch** mass-memory at slow rates; at the fastest swept rate $B_r^{\max}_{\mathrm{L1}}\approx 0.017$ (residual lag before full dwell relaxation — flagged, not bin-changing). **L2** (memristor + rate-gated snap) gives **$B_r^{\max}\approx 0.29$** at $\omega\tau=1.25$ after zero-drive dwell → **frozen bin REMANENT-LOOP** → **D2(b) vindicated in silico** for the snap constitutive element.

| Arm | $\oint$ (max over grid) | $B_r$ (max over grid) | Read |
|:---|:---:|:---:|:---|
| L0 | 0 | 0 | Harness null |
| L1 | 0.099 @ $\omega\tau=1.0$ | 0.017 @ $\omega\tau=1.25$ | Dissipation; pinched at slow rates |
| L2 | 0.106 @ $\omega\tau=1.0$ | **0.288** @ $\omega\tau=1.25$ | Rate-gated remanence |

**D2 synthesis:** Anhysteretic varactor-only (L0) cannot supply remanence. Documented $\tau_{\mathrm{relax}}$ ODE alone (L1) supplies **loss tangent / reactive dissipation** without honest $B_r$ memory at $H\to 0$. Adding the **rate-gated snap latch** (L2) is the **discriminator** — remanence requires a bistable/latching element beyond the relaxation memristor.

---

## 1. Executable frozen gates (all H-gates PASS)

| Gate | Result |
|:---|:---:|
| H0 L0 $\oint=0$, $B_r=0$ | PASS |
| H1 L1 $\oint$ grows with $\omega\tau$ (0.01 → 1.0) | PASS |
| H1 L1 pinched at slow rate ($\omega\tau=0.01$) | PASS |
| H2 L2 $B_r\geq\epsilon_B$ when verdict REMANENT-LOOP | PASS |
| `bin_REMANENT_LOOP` | PASS |

**L1 surprise (logged, not promoted):** $B_r^{\max}_{\mathrm{L1}}=0.0167>\epsilon_B$ at $\omega\tau=1.25$ — incomplete dwell relaxation at the fastest grid point; L2 still dominates the bin.

---

## 2. Implementation notes

1. **Python harness** integrates $dS/dt=(S_{\mathrm{eq}}-S)/\tau$ with $S_{\mathrm{eq}}(r)=\sqrt{1-r^2}$; L2 adds rate-gated snap on down-crossing above $r>0.55$.
2. **`.lib` memristor** closes the documented-not-implemented gap via `AVE_MEMRISTOR_S_STATE` (VCCS + $C=1$ F state) and `AVE_VACUUM_CELL_L1`; ngspice uses **simulation-scaled** `TAU_REL` (default 1 ns). Keeper parse tests in `test_spice_vacuum_cell.py` (ngspice-gated).
3. **$\omega\tau$ pre-gate** logged per arm; canonical SI $\tau$ is below ngspice timestep — informative regime is $\omega\tau\sim 1$ in the ODE harness, not DC SPICE.
4. **Metric fix:** branch hysteresis area sorts down-r branch before `np.interp` (decreasing-$r$ leg was inflating area at slow rates).

---

## 3. Caveats (do not promote)

1. $Q=1/\alpha=\tan\delta$ is **definitional calibration**, not an AVE-distinct discovery — SPICE/ODE consistency only.
2. $\tau_{\mathrm{relax}}\approx 1.3\times 10^{-21}$ s — slow-frequency SPICE gives $\oint\approx 0$ by construction (harness null).
3. **REMANENT-LOOP $\neq$ electron** — retention mechanism only; topology / $(2,3)$ out of scope (`CVG-NAR-001`).

---

## 4. Hygiene landed

- Stale `.lib` paths `hardware/spice_models/` → `solvers/spice_models/` in KB leaves (`device-circuit-models.md`, `spice-subcircuit.md`, `index.md`, `appendix-spice-verification.md`).

---

## 5. Auditor surface

- **Verdict:** REMANENT-LOOP  
- **D2:** (b) rate-gated snap constitutive remanence confirmed in silico; (a) still true for L0/L1 without latch  
- **Parallel track:** LOOP GAP scalar-grade / rank-4 harness unchanged  
- **Next:** auditor read-only verify gates + figures against prereg bins
