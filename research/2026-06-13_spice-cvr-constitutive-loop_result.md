# RESULT — SPICE-CVR constitutive-loop test (L0/L1/L2 ladder)

**Date:** 2026-06-13  
**Branch:** `analysis/2026-06-13-spice-cvr-constitutive-loop` (off `origin/main`)  
**PR:** [#215](https://github.com/ave-veritas-et-enodatio/AVE-Core/pull/215) — **OPEN; do not merge as REMANENT-LOOP**  
**Prereg (frozen, committed alone first):** [`2026-06-13_spice-cvr-constitutive-loop_prereg.md`](2026-06-13_spice-cvr-constitutive-loop_prereg.md) (commit `036bc486`)  
**Harness:** [`src/ave/solvers/spice_cvr_loop.py`](../src/ave/solvers/spice_cvr_loop.py) — dimensionless $\omega\tau$ ODE ladder (**Python only**; ngspice transient not executed)  
**Driver:** [`src/scripts/vol_4_engineering/spice_cvr_loop_sweep.py`](../src/scripts/vol_4_engineering/spice_cvr_loop_sweep.py)  
**Data:** `src/scripts/vol_4_engineering/_output/spice_cvr_loop_sweep_results.json`  
**Figures:** `assets/sim_outputs/spice_cvr_loop_*.png`  
**`.lib`:** `AVE_MEMRISTOR_S_STATE`, `AVE_VACUUM_CELL_L1` — relaxation memristor only; **no latch in SPICE**

**Scope fence (carry):** local constitutive law only — **not** topology / winding / genesis.

---

## 🔴 AUDITOR ADDENDUM — verdict **RETRACTED** from REMANENT-LOOP → **DISSIPATIVE-ONLY** + **IMPOSED-LATCH** (Rule 12; PR #215 panel)

**Status:** L0/L1 physics **stand**. Original §0 REMANENT-LOOP text **superseded** by this header. **Do not merge #215 as loop-gap closure.**

**The tautology (one line):** `spice_cvr_loop.py:168` — `S = min(S, S_latched)`. That is a **one-way software ratchet**, not a double-well, not an EOS $\Gamma\to -1$ collapse, **not in the `.lib`**. The canonical substrate (Axiom-4 $S_{\mathrm{eq}}+\tau_{\mathrm{relax}}$ memristor that relaxes **back** to $S_{\mathrm{eq}}$) **predicts $B_r=0$**. Every bit of L2 "remanence" is the added clamp. Snap thresholds (`snap_r_min=0.55`, `snap_rate_thresh=0.15`) are **hardcoded literals** — not $\sqrt{\alpha}\approx 0.085$ from `V_YIELD/V_SNAP` via `constants.py` (prereg "no hardcoded yield" violated on L2).

**What remains genuinely good:**
- **L0** — exact null ($\oint=0$, $B_r=0$).
- **L1** — documented memristor opens a **pinched** loop; $B_r\approx 0$ at slow rates. Load-bearing physics: **dissipation alone does not retain.**
- Discipline: prereg-first, executable gates, scope fence, Q$=1/\alpha$ restraint, memristor `.lib` gap closed, stale path hygiene.

**R10 implication:** *Mass = remanence / loop gap* — **still open**. #215 was the demonstration attempt; it failed honestly (imposed latch). **D2 undecided** in sharpest form: does the vacuum constitutive law supply a loop, or must one be put in by hand?

---

## 0. VERDICT — **DISSIPATIVE-ONLY** (physics) + **IMPOSED-LATCH** (L2 emergence inconclusive)

> **L0** reads $\oint=0$, $B_r=0$. **L1** opens a rate-dependent **pinched** loop ($\oint$ grows with $\omega\tau$, peaks $\sim 0.099$ at $\omega\tau=1.0$) with **no honest remanence** at slow rates ($B_r<10^{-3}$ at $\omega\tau\leq 0.5$). **L2** shows elevated $B_r$ only because of the imposed `min(S,S_latched)` clamp — **not** substrate emergence.

| Arm | $\oint$ peak | $B_r$ peak | $\omega\tau$ at $B_r$ peak | Read |
|:---|:---:|:---:|:---:|:---|
| L0 | 0 | 0 | — | Harness null |
| L1 | 0.099 | 0.017 | 1.25 | Pinched dissipation |
| L2 | 0.132 | **0.288** | **0.7** | Imposed clamp (falls to 0.233 @ 1.25) |

**JSON-verified L2 $B_r$ sweep** (not "max at fastest rate"):

| $\omega\tau$ | $B_r$ (L2) |
|:---:|:---:|
| 0.7 | **0.288** (peak) |
| 0.9 | 0.264 |
| 1.0 | 0.254 |
| 1.25 | 0.233 |

**D2 synthesis:** **Not vindicated (b).** L0/L1 support **D2a** — lossy-reactive constitutive law, no $B_r$ memory. L2 does **not** decide D2; it demonstrates that **a latch imposed by hand retains**. Grant question logged: *does the substrate provide any canonical non-recovery mechanism, or is a latch necessarily an imposition?*

---

## 1. Executable gates (L0/L1 physics PASS; REMANENT-LOOP bin RETIRED)

| Gate | Result |
|:---|:---:|
| H0 L0 $\oint=0$, $B_r=0$ | PASS |
| H1 L1 $\oint$ grows with $\omega\tau$ (0.01 → 1.0) | PASS |
| H1 L1 pinched at slow rate ($\omega\tau=0.01$) | PASS |
| `bin_DISSIPATIVE_ONLY` | PASS |
| `bin_REMANENT_LOOP` | **FALSE** (auditor retract) |

---

## 2. What landed vs what did not

**Landed:**
1. Memristor `.lib` (`AVE_MEMRISTOR_S_STATE`, `AVE_VACUUM_CELL_L1`) — relaxation ODE only.
2. Python ODE harness + keeper tests (`test_spice_cvr_loop.py`).
3. KB path hygiene (`solvers/spice_models/`).

**Did not land:**
1. Canonical remanence / loop-gap closure (R10 still open).
2. ngspice transient validation (`spice_executed: false`; parse tests unrun in CI).
3. L2 emergence from substrate (double-well, $\Gamma\to -1$ bulk-$K$ collapse, thresholds from $\sqrt{\alpha}$).

---

## 3. Next implementor direction (not this PR)

To make L2 a **real** emergence test:
- Derive latch from **canonical mechanism** (saturable-EOS double-well, or v5-style bulk-$K$ $\Gamma\to -1$ collapse).
- Pull thresholds from `V_YIELD/V_SNAP` = $\sqrt{\alpha}$ via `constants.py` — no `min()` bookkeeping ratchet.
- Execute ngspice transient on scaled-$\tau$ arm; log `tau_scale` + `omega_tau`.

---

## 4. Caveats (do not promote)

1. $Q=1/\alpha$ — definitional calibration only.
2. $\tau_{\mathrm{relax}}\approx 1.3\times 10^{-21}$ s — slow SPICE frequency → $\oint\approx 0$ by construction.
3. **IMPOSED-LATCH $\neq$ electron** — topology / $(2,3)$ out of scope (`CVG-NAR-001`).
