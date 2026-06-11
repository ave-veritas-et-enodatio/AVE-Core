# RESULT — Genesis-v6 JOB 1 (D11): isolating + fixing the v5 +283% H_total pump

**Date:** 2026-06-10
**Prereg (frozen, committed alone):** `research/2026-06-10_genesis-v6-transducer_prereg.md` @ `fa4420c6`
**Driver:** `src/scripts/vol_1_foundations/genesis_v6_pump_isolation.py` (serial, deterministic, seed `20260610`)
**Raw numbers:** `research/2026-06-10_genesis-v6-pump-isolation_results.json` (every number below read FROM it — ave-driver-script-honesty)
**Engine:** `src/ave/core/unified_genesis_engine.py` (the v6 D11 additions; v5 path byte-identical by default — `src/tests/test_unified_snap_machine{,_v6}.py`)

---

## 0. HEADLINE (written from the numbers — Rule 11)

**The v5 +283% H_total pump is ISOLATED, NAMED, and FIXED.** Dominant mechanism: **GAP-C vent
re-injection triggering the genesis-24 seed-V breather.** Post-fix, the MAIN-config DRIVE-OFF ledger
shows a **max positive excursion of 0.0000 %** (≤ the measured floor F-CLOSE = +0.184 %) — energy is no
longer created; the pump gate PASSES.

---

## 1. THE BISECTION (the three suspects + the energy functional) — REAL NUMBERS

Each arm: build the MAIN config to step 3200, report H_total growth from the quiet plateau (step 2800,
pre-cascade) to built, in BOTH the naive `bulk_energy` functional and the master-equation-conserved
`bulk_energy_conserved` functional (CP2).

| arm | switched OFF | H_naive growth | H_cons growth | EV_naive built | max\|V\| | pocket | reading |
|---|---|---|---|---|---|---|---|
| **MAIN** | (none — v5 baseline) | **+371.8 %** | +71.4 % | **50 339** | **5.55** | 5968 | the v5 pump reproduced (H_built 64 835) |
| **VENT_OFF** | GAP-C vent (kick→sink) | **+5.6 %** | +5.6 % | **13** (flat) | **0.32** | 5968 | breather GONE; identical pocket cascade |
| **SEED_OFF** | the deep seed | +5.6 % | +5.6 % | 0 | 0.00 | 5968 | no V to detonate; same residual |
| **SNAP_OFF** | the snap machine | **−0.0 %** | −0.0 % | 13 | 0.32 | 0 | no cascade ⇒ NO pump at all |

**The isolation is unambiguous:**
1. **SNAP_OFF → −0.0 %:** the pump REQUIRES the snap cascade (no snap, no pump).
2. **VENT_OFF → +5.6 %** (from +371.8 %): with the snap cascade BYTE-IDENTICAL (pocket 5968, latent
   identical), turning the vent from a seed-V kick to a sink kills the EV detonation — `EV_naive` stays
   flat at 13, `max|V|` stays at 0.32. **The +283 %/+372 % is the vent → seed-V breather**, not the snap
   cascade. The vented shock (484 in v5) merely TRIGGERS the deep-saturated seed
   (`c_eff²=c₀²/√(1−A²)`, frac 0.85) over its stiffening singularity; the V-breather self-amplifies (the
   genesis-24 detonation). This is the forbidden CW pump into the standing-V (the Class-C detonation the
   v5 prereg §7 named).
3. **SEED_OFF confirms** the breather needs the seed substrate (EV→0 without it); the same +5.6 % residual
   remains.

**Two SECONDARY contributors, quantified:**
- **Wrong energy functional (CP2 / representation-capability):** at MAIN built `EV_naive/EV_cons = 5.56×`.
  The naive `bulk_energy = ½∫(∂_tV)² + ½c₀²∫(∇V)²` over-reports the saturated-core breather; the
  master-equation invariant `bulk_energy_conserved = ½∫(∂_tV)²/c_eff² + ½∫|∇V|²` down-weights the fast
  stiff-core slosh (H_cons MAIN grows +71 %, not +372 %). An SM-default (naive-Hamiltonian) leak.
- **Snap-accounting double-count (the +5.6 % residual):** the shock void-KE `χ·ke_void` was booked TWICE
  — held in `latent_ledger` AND sent to `E_diss_snap`/vent. Net effect: H over-counted by exactly the
  shock KE (`E_diss_snap ≈ 967` ≈ the residual). The held latent the v5 reported (968) was ~100 %
  double-booked shock KE, ~0 % reversible internal energy.

## 2. THE FIX

`vent_mode="absorbed"` (the shock KE drains to a conservative store `E_vent_absorbed`, no `∂_tV` kick →
no breather) + `snap_accounting="conservative"` (latent holds ONLY the reversible internal energy `d_eps`;
the shock KE booked ONCE; the per-step reflector-BC KE tallied to `E_reflect`). H_total reported in the
conserved functional. **All behind new params; v5 path byte-identical by default.**

## 3. POST-FIX CLOSURE (the D11 gate)

- **F-CLOSE (measured floor):** no-snap drive-off conservation canary → max positive excursion **+0.184 %**.
- **MAIN-config FIX demo, drive-off (P1, 1200 steps):** `EV_naive` built = **12.91** (bounded; the
  detonation is gone), `max|V|` = 0.324, pocket 5256. Drive-off **max positive excursion = 0.0000 %**
  (H_total is monotone non-increasing — NO energy creation), net residual **−4.085 %** (DISSIPATIVE).
- **PUMP GATE: PASS** (0.0000 % ≤ 0.184 %). The energy-creation pump is eliminated. The −4.1 % net is the
  physically-correct sign — the snap-reflector BC + open PML are one-way sinks draining the large (5256-cell)
  cascade void; it is tracked, bounded, and never positive.
- **Bonus corroboration of the v5 demotion:** under the corrected (payable) accounting the snap ledger now
  records `unsnap_events = 25944` and `E_latent_held = 0.52` (vs v5's `unsnap_events = 0`, `latent = 968`).
  The v5 "held latent" was unpayable-by-construction — exactly the SNAP-LOCKED demotion basis (JOB 3 sweeps it).

## 4. FLAGS (flag-don't-fix)

1. **The fix unblocks the pump-side gate only.** The NOT-ELECTRON verdict is unchanged; this is engine
   hygiene. The genesis arm (PHASE 2) still requires the D10 deflagration fix (JOB 2) and the D12 fail-fast
   transducer check before it runs.
2. **The −4.1 % drive-off dissipation is a property of the (non-electron) cascade object**, not a ledger
   bug — a 5256-cell void with a reflecting BC drains flow irreversibly. A genuine rest mass would settle;
   this transient does not. Reported, not polished.
3. **Corpus-state delta (auditor lands):** the v5 `energy_ledger` "+283 % pump / closure_resid −1.09"
   row is now MECHANISM-ATTRIBUTED (vent→breather + wrong-functional + double-count) and FIXED to a
   closing (dissipative) ledger above the measured floor.
