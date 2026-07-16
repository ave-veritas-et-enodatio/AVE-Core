# F6 mode-count door — Arm B (G0 exterior leave) — prereg FROZEN

**Date:** 2026-07-16  
**Charters:** [`2026-07-15_f6-mode-count-door_CHARTER.md`](2026-07-15_f6-mode-count-door_CHARTER.md) §4/§6; [`2026-07-16_f6-frontier-map_CHARTER.md`](2026-07-16_f6-frontier-map_CHARTER.md) §6 (Tier-0 **G0**; Grant GO 2026-07-16).  
**Prior kills:** rung-2 global V scale-down = **BIAS-MOVED**; Arm A event-gated occupancy = **BIAS-MOVED** (mode-count LIVE).  
**Class:** prereg — **freeze-by-push BEFORE any driver exists** (ave-prereg Step 3.11).  
**Arm status:** **HYPOTHESIS under the discriminator** — not “the plan,” not Re(Z) absorb, not orthogonal cosmology.

> ★ **FROZEN.** §1–§4 locked before RESULT. Do not retune after fire (Rule 11).

---

## §0 Arm identity (hypothesis)

**Name:** Arm B — face-port exterior leave → exterior multi-mode ledger (geometry fork **G0**).

**Intended mechanism (substrate-native language):**
1. **Ports:** on the discrete **box-face** sites of an active `K4Lattice3D` (`pml_thickness=0`), extract a packet of field energy each step when ports are ON.
2. **Exterior credit:** deposit that energy into an **exterior** mode accumulator `b[m]` (M slots), spreading each packet across `N_SPREAD` lowest-occupied slots so exterior occupied-mode-count can rise.
3. **Protected core:** spherical finished-A1 mask — bias≠release / electron-no-drain knives apply; ports do **not** extract from the core.
4. **OFF:** ports disabled — same stepper, closed box (no exterior leave). Periodic wrap at `pml=0` is recirculation, not an exterior ledger.

**Geometry fork:** **G0** — face ports are implementation convenience, **not** a claim of normal-to-frontier (G1) cosmology. No normal-weighted leave in pass criteria. G3 parked.

**Explicitly not this arm:** matched-termination Re(Z) absorb, matched stub, interior dump-R, STZ/plastic loss, PML sponge as T2, interior event-gated V scale-down (Arm A class), electron `radiation_leak` Q-leak, ℏ/FD design constraints, F6=frontier unification, DE lifecycle / `ρ_Λ` claims.

**How mode-count is supposed to enlarge without friction:** irreversibility claim = energy leaves the reactive interior into a **growing set of occupied exterior modes**, not a single scalar damper. FRICTION-RENAMED fires if exterior energy rises **without** exterior occupied-mode-count increase. Pairing amendment: exterior energy↑ alone is generic-consistent and does **not** count toward CHANNEL-BOUNDED.

---

## §1 Hypothesis

Under Arm B ON vs OFF, the frozen `classify()` returns **CHANNEL-BOUNDED** *or* a fail-closed kill (BIAS-MOVED / ELECTRON-DRAIN / DETONATE / FRICTION-RENAMED / NULL / SPONGE-COSTUME). Analytic expectation is **fork-record-both**: face leave may pass the exterior mode-count knife while still failing bias≠release (Arm A lineage), or may CHANNEL-BOUNDED if surface leave separates from core scatter. **No claim that CHANNEL-BOUNDED is expected.** Even CHANNEL-BOUNDED does **not** claim DE lifecycle, crystallization, F6 occupancy chord, or orthogonal geometry.

**Sector declaration (map charter):**  
- MODE: T2 / transverse exterior mode-count (entropic sink bookkeeping), not A1 mass cage.  
- REGIME: boundary leave at face ports; interior reactive Ax3 when OFF.  
- PHASE-STATE: toy box with exterior ledger — **not** cosmic horizon crystallization; **not** BH pre-geodesic.

---

## §2 Bins (mode-count charter §4 + map SPONGE-COSTUME; locked)

| Bin | Fire when |
|---|---|
| **CHANNEL-BOUNDED** | ON: exterior `E_bath`↑, exterior occupied modes ↑ (`ΔN_occ ≥ 1`), soft energy ledger within tol, finite, core bias & drain within tol; and (if PML control run) PML-without-ports does **not** score as pass |
| **DETONATE** | NaN/Inf/runaway / soft-ledger blow |
| **BIAS-MOVED** | `\|mean_S_core ON − OFF\| > BIAS_TOL` |
| **ELECTRON-DRAIN** | protected-core energy drop ON vs OFF > `DRAIN_TOL` |
| **NULL** | `E_bath < NULL_FLOOR` under ON (ports never effective) |
| **FRICTION-RENAMED** | `E_bath ≥ NULL_FLOOR` (or field drop) **but** `ΔN_occ < 1` — energy moved without exterior mode-count increase |
| **SPONGE-COSTUME** | Control: `pml_thickness>0` with ports OFF scores as if CHANNEL-BOUNDED (energy “leave” into sponge without exterior `b[m]`) — **fail closed** if that control is misread as pass; driver must report the control as non-pass |

Decision: fail-closed on DETONATE / BIAS-MOVED / ELECTRON-DRAIN / FRICTION-RENAMED / SPONGE-COSTUME. Only CHANNEL-BOUNDED ungates thermometer discussion. NULL = build incomplete.

**Entailed-branch note (ave-prereg 3.10):** FRICTION-RENAMED is **not** entailed-never: a sabotage plant that credits a scalar exterior bath without filling `b[m]` must be able to fire it. Production Arm B always spreads into `b[m]`. SPONGE-COSTUME control is a separate ON/OFF of PML without ports — must not be classified CHANNEL-BOUNDED by the production bins (no exterior modes).

---

## §3 Method

1. Platform: native `K4Lattice3D` (`nonlinear=True`, `op3_bond_reflection=True`, `V_SNAP=1.0`, **`pml_thickness=0`**).
2. Seed: mild protected-core clock blob + unprotected traveling bath (same spirit as Arm A / rung-2).
3. Masks: spherical core radius `CORE_R`; **face** = active sites with any index on `{0, N-1}` (depth-1 shell); ports extract only on `face & ~core`.
4. Each step: `lat.step()`; then if `ports_on` (kappa>0): extract packet on face sites; credit exterior modes.
5. Packet: prefer scaling outgoing `V_ref` (and `V_inc` as needed) on face sites so extracted δ matches soft ledger; `δ_site = min(PACKET * dens_site, dens_site * 0.5)`.
6. Mode credit: add δ spread across `N_SPREAD` lowest `b[m]`; `N_occ = count(b[m] > MODE_FLOOR)`.
7. OFF: `kappa=0` — no extract.
8. Sabotage: `--sabotage-friction` → scalar exterior energy, no `b[m]` fill.
9. Optional control (report-only): `pml_thickness>0`, ports OFF — must **not** CHANNEL-BOUNDED (no exterior modes); documents SPONGE-COSTUME detector liveness.
10. `classify(on, off)` frozen in driver before RESULT.

---

## §4 Tolerances / knobs (frozen — do not retune)

```
TOL_SOFT_LEDGER_FRAC = 0.5
DETONATE_FLOOR = 1e6
BIAS_TOL = 5e-3
DRAIN_TOL = 0.05
NULL_FLOOR = 1e-12
MODE_FLOOR = 1e-15
PACKET = 0.08
N_SPREAD = 4
M_MODES = 64
KAPPA = 1.0          # master ON switch (0 = OFF)
N_STEPS = 150
N = 12
CORE_R = 2.5
SEED = 1
```

**Analytic expectations (numbers):**
- OFF: `E_bath=0`, `ΔN_occ=0`, finite.
- ON: if face dens > 0 and ports fire, `E_bath > NULL_FLOOR` and `ΔN_occ ≥ 1` *by construction of mode credit* unless deposit path is broken.
- Bias/drain: unknown a priori; Arm A failed bias at these core tolerances — Arm B may too.
- CHANNEL-BOUNDED requires all of: exterior bath↑, ΔN_occ≥1, soft ledger, bias OK, drain OK, finite.
- Does **not** claim DE / crystallization / F6 / G1 even on CHANNEL-BOUNDED.

---

## §5 Result

*(empty until fire — fill after prereg push + driver; Rule 11)*
