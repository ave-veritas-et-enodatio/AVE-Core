# Two-tank thermometer re-fire — prereg (GATED)

**Date:** 2026-07-15  
**Status:** **GATED — do not fire.** Requires an in-Hamiltonian F6 door that banks CHANNEL-BOUNDED without BIAS-MOVED / ELECTRON-DRAIN.  
**Prior:** #707 ADDITIVE-ARTIFACT; F6 rung-1 CHANNEL-BOUNDED (parallel ledger only — does not change clock dynamics); F6 rung-2 **BIAS-MOVED** (scale-down door failed).  
**Upstream gate:** next F6 door class after rung-2 kill-shape.

---

## §0 Why gated

Rung-1’s parallel latent→bath ledger never touches `V_inc` phase dynamics → re-firing two-tank with rung-1 ON is a **null instrument** (expected ADDITIVE-ARTIFACT again). Rung-2’s in-Hamiltonian scale-down moves operating point / drains cores → not a legal thermometer channel. Re-fire only after a door that (i) injects irreversibility into the V-sector bath the clocks see and (ii) passes bias≠release + electron-no-drain.

---

## §1 Hypothesis (frozen for when gate opens)

With a legal F6 door ON, the two-tank kernel-excess fraction rises above `EXCESS_MIN=0.50` (mechanism-gated criterion from #707), converting the verdict from ADDITIVE-ARTIFACT toward DIFFUSIVE-* under the same frozen classify contract in `two_tank_decoherence_check.py`.

---

## §2 Bins (reuse #707 classify)

`CONTROL-FAIL` · `ADDITIVE-ARTIFACT` · `BOUNDED-REVERSIBLE` · `DIFFUSIVE-LINEAR` · `DIFFUSIVE-NONLINEAR` — thresholds unchanged.

Additional F6 arm: door ON vs OFF at fixed kernel ON (isolates irreversibility from Op14).

---

## §3 Method (when ungated)

1. Import #707 driver unmodified for Op14 ON/OFF arms.
2. Add F6 door ON/OFF wrapper once the door API exists on `K4Lattice3D` / harness.
3. Freeze-by-push this note’s §1–§2 before any production sweep (re-affirm if amended).

---

*Charter-level gate record. Nothing fired.*
