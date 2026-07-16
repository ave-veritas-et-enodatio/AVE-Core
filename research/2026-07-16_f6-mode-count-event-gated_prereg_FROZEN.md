# F6 mode-count door — Arm A (event-gated occupancy) — prereg FROZEN

**Date:** 2026-07-16  
**Charter:** [`2026-07-15_f6-mode-count-door_CHARTER.md`](2026-07-15_f6-mode-count-door_CHARTER.md)  
**Prior kills:** rung-1 parallel ledger = CHANNEL-BOUNDED but V-dynamics-null; rung-2 global V scale-down = **BIAS-MOVED**.  
**Class:** prereg — **freeze-by-push BEFORE any driver exists** (ave-prereg Step 3.11).  
**Arm status:** **HYPOTHESIS under the discriminator** — not “the plan,” not Re(Z) absorb.

> ★ **FROZEN.** §1–§4 locked before RESULT. Do not retune after fire (Rule 11).

---

## §0 Arm identity (hypothesis)

**Name:** Arm A — event-gated occupancy → multi-mode bath credit + V-phase couple.

**Intended mechanism (substrate-native language):**
1. **Gate:** on unprotected active sites, when local occupancy proxy (energy density normalized to peak) exceeds `OCC_THRESH`, an event may fire (at most one packet per site per step).
2. **Packet:** remove energy `δ` from those gated sites by a **local** amplitude scale (not continuous global κ·E every step — distinct from rung-2’s always-on scale-down).
3. **Bath credit:** deposit `δ` into a **mode accumulator** `b[m]` (M slots), spreading each packet across `N_SPREAD` lowest-occupied slots so occupied mode-count can rise.
4. **V-phase couple (thermometer lineage):** on gated sites, apply an energy-preserving random **port-phase scramble** so the door touches `V_inc` phase structure (rung-1 did not).

**Explicitly not this arm:** matched-termination Re(Z) absorb, interior dump-R, STZ/plastic loss, ℏ/FD design constraints, continuous unprotected scale-down.

**How mode-count is supposed to enlarge without friction:** irreversibility claim = energy leaves the reactive field into a **growing set of occupied bath modes** (mode-count / phase-space slots), not a single scalar damper. FRICTION-RENAMED fires if field energy drops / `E_bath` rises **without** occupied-mode-count increase.

---

## §1 Hypothesis

Under Arm A ON vs OFF, the frozen `classify()` returns **CHANNEL-BOUNDED** *or* a fail-closed kill (BIAS-MOVED / ELECTRON-DRAIN / DETONATE / FRICTION-RENAMED / NULL). Analytic expectation is **fork-record-both**: this arm may fail the same bias≠release knife as rung-2 (scatter into protected core), or may pass if event-gating + mode credit separates transfer from continuous friction. **No claim that CHANNEL-BOUNDED is expected.**

---

## §2 Bins (charter §4; locked)

| Bin | Fire when |
|---|---|
| **CHANNEL-BOUNDED** | ON: `E_bath`↑, occupied bath modes ↑ (`ΔN_occ ≥ 1`), soft energy ledger within tol, finite, core bias & drain within tol |
| **DETONATE** | NaN/Inf/runaway / soft-ledger blow |
| **BIAS-MOVED** | `\|mean_S_core ON − OFF\| > BIAS_TOL` |
| **ELECTRON-DRAIN** | protected-core energy drop ON vs OFF > `DRAIN_TOL` |
| **NULL** | `E_bath < NULL_FLOOR` under ON (gate never effective) |
| **FRICTION-RENAMED** | `E_bath ≥ NULL_FLOOR` (or field drop) **but** `ΔN_occ < 1` — energy moved without mode-count increase |

Decision: fail-closed on DETONATE / BIAS-MOVED / ELECTRON-DRAIN / FRICTION-RENAMED. Only CHANNEL-BOUNDED ungates thermometer re-fire. NULL = build incomplete.

**Entailed-branch note (ave-prereg 3.10):** FRICTION-RENAMED is **not** entailed-never: a sabotage plant that credits a scalar bath without filling `b[m]` must be able to fire it (unit test). Production Arm A always spreads into `b[m]`; if it still fails FRICTION-RENAMED, that is an implementation bug, not a retune.

---

## §3 Method

1. Platform: native `K4Lattice3D` (`nonlinear=True`, `op3_bond_reflection=True`, `V_SNAP=1.0`) — same lineage as rung-2 / thermometer.
2. Seed: mild protected-core clock blob + unprotected traveling bath (same spirit as rung-2).
3. Protect mask: spherical core radius `CORE_R`; transfers only on `unprot = active & ~core`.
4. Each step: `lat.step()`; then Arm A gate+packet+mode-credit+phase-scramble if `kappa>0` (OFF: `kappa=0` disables gate).
5. Occupancy proxy: `occ = dens / (dens_unprot.max()+ε)` on unprotected sites; gate where `occ ≥ OCC_THRESH`.
6. Packet: `δ_site = min(PACKET * dens_site, dens_site * 0.5)`; global scale factor from total δ vs total gated energy (site-local scale of V_inc/V_ref).
7. Mode credit: add δ spread across `N_SPREAD` lowest `b[m]`; `N_occ = count(b[m] > MODE_FLOOR)`.
8. Phase scramble: on gated sites, multiply port vector by random SO(4)-lite phase (per-port random sign flip / port permutation with energy preserved — implementation freezes in driver as energy-norm preserving).
9. `classify(on, off)` frozen in driver before RESULT.

---

## §4 Tolerances / knobs (frozen — do not retune)

```
TOL_SOFT_LEDGER_FRAC = 0.5   # |ΔE_field − E_bath| > this·E0 → DETONATE-class
DETONATE_FLOOR = 1e6
BIAS_TOL = 5e-3
DRAIN_TOL = 0.05
NULL_FLOOR = 1e-12
MODE_FLOOR = 1e-15
OCC_THRESH = 0.35
PACKET = 0.08
N_SPREAD = 4
M_MODES = 64
KAPPA = 1.0          # master ON switch (0 = OFF); not a continuous drain rate
N_STEPS = 150
N = 12
CORE_R = 2.5
SEED = 1
```

**Analytic expectations (numbers):**
- OFF: `E_bath=0`, `ΔN_occ=0`, finite.
- ON: if gate fires, `E_bath > NULL_FLOOR` and `ΔN_occ ≥ 1` *by construction of mode credit* unless deposit path is broken.
- Bias/drain: unknown a priori; rung-2 failed bias at these core tolerances — Arm A may too.
- CHANNEL-BOUNDED requires all of: bath↑, ΔN_occ≥1, soft ledger, bias OK, drain OK, finite.

---

## §5 Result

*(empty until fire — fill after driver exists; Rule 11 honesty)*

---

*Prereg only. No driver in the freeze commit. Arm A = hypothesis under the mode-count discriminator.*
