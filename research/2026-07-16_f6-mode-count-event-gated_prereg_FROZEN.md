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

**Fired 2026-07-16** (prereg commit `17662232` pushed before driver; classify frozen).

```
VERDICT = BIAS-MOVED
  ON  bath≈7.55  field≈0.044  core≈0.040  N_occ=64  events≈27289
  OFF bath=0     field≈7.68   core≈0.313
  soft_ledger |ΔE_field − bath| ≈ 3.76
  ΔS_core ≈ +0.142  (≫ BIAS_TOL=5e-3)
  ΔN_occ = 64  (mode-count detector LIVE — not FRICTION-RENAMED)
```

**Sabotage (Discriminator 7):** `--sabotage-friction` (scalar bath, no `b[m]` credit) → **FRICTION-RENAMED** as required.

**Honest closure (Rule 11):** Arm A enlarges occupied bath mode-count and couples into V-phase, but **fails bias≠release** at the same protected-core knife as rung-2 (scatter / soft-ledger mismatch). Event-gating + multi-mode credit did **not** evade the BIAS-MOVED kill-shape. Do **not** retune `OCC_THRESH` / `PACKET` / `CORE_R`. This hypothesis arm is **not** CHANNEL-BOUNDED.

Thermometer re-fire remains **GATED**. Next hypothesis under the same discriminator (if pursued): boundary-radiation arm — still not Re(Z) absorb.

---

## Post-adversarial-review amendments — 2026-07-16 (append-only; §0–§5 body byte-untouched)

> 🔴 **Rule-12 supersession (2026-07-16, post-review).** PR #711's independent adversarial review (11 findings confirmed, 1 refuted) voided the **detector infrastructure** while the **verdict** survives untouched: Arm A is **BIAS-MOVED** on the independent protected-core `S_core` knife (ΔS_core = 1.421e-1 ≫ BIAS_TOL = 5e-3, 28×). Per the freeze discipline the §0–§5 body above is preserved **byte-for-byte**; the corrections below are dated amendments that supersede only the specific §5 claims they cite. The Arm A negative stands and is banked (see A7). The no-smuggle rail **passed** — see A2.

### A1 — Mode-count "detector LIVE" headline RETRACTED (findings 0 / 4 / 7 — CRITICAL, three lenses converged)

§5 line 104 — `ΔN_occ = 64  (mode-count detector LIVE — not FRICTION-RENAMED)` — is **superseded**. The review proved, and this session reproduced two ways (review probes at PR head + independent re-run), that

> **ΔN_occ = min(M_MODES, N_SPREAD × event-steps)** — a dynamics-free 64-slot accumulator (`bath_modes = np.zeros(M_MODES)`) credited by fiat, with no back-reaction onto the lattice.

Probes at PR head, only the array size varied: `M_MODES=48 → ΔN_occ=48`, `M_MODES=96 → ΔN_occ=96`, all with **identical** `bath=7.5548` and `events=27289`; PACKET 10× weaker → still 64 (bath 3.69); seed=7 → still 64. ΔN_occ tracks the accumulator dimension, is decoupled from the physical leave, and saturates at `M_MODES` after 16 of the 150 steps. The prereg's own §4 concession is the disclosed-but-under-weighted tell:

> "ON: if gate fires, `E_bath > NULL_FLOOR` and `ΔN_occ ≥ 1` *by construction of mode credit* unless deposit path is broken." (§4, line 88)

`ΔN_occ ≥ 1` being true *by construction* means the count carries no physical evidence.

**Relabel (verbatim — propagated to PR body, docket, ratings-map):**

> ΔN_occ is **bookkeeping liveness only** — it reads the accumulator dimension (`M_MODES = 64`), **NOT** a physical mode-count; the twin-64 across Arms A/B is the shared array size, not two independent doors corroborating a mode count.

The twin `ΔN_occ = 64` across #711 (Arm A) and #713 (Arm B) MUST NOT be cited as independent corroboration — both ship the byte-identical `M_MODES = 64` / `_credit_modes` detector machinery. (Correction to the finding as first written: the whole-file Arm B diff is *large* — only the detector machinery is identical; the twin-64 conclusion holds on that corrected ground.)

### A2 — The FRICTION-RENAMED control is a flag readback; no-smuggle rail PASSED; detector-rebuild GATE registered (finding 5 — CRITICAL)

§5's sabotage line — `--sabotage-friction ... → FRICTION-RENAMED as required` — is **relabeled, not banked as a physical control.** Reproduced this session: the production run and the `--sabotage-friction` run are **bit-identical** except the `credit_modes` side-array increment:

| field | production | `--sabotage-friction` |
|---|---|---|
| `bath` | 7.554826e+00 | 7.554826e+00 |
| `field` | 4.446578e-02 | 4.446578e-02 |
| `core` | 3.983927e-02 | 3.983927e-02 |
| `events` | 27289 | 27289 |
| `soft_ledger` | 3.760e+00 | 3.760e+00 |
| `ΔS_core` | 1.421e-01 | 1.421e-01 |
| **`N_occ`** | **64** | **0** |

The energy-removing op (`arr[gated] *= scale`) runs in **both** paths; `bath_modes` is never coupled back to the lattice (written only by `_credit_modes`, read only by `_n_occ`). So the control **verifies the credit path executes** — it **cannot fail on any energetic run** and is **vacuous as a physical discriminator**. The sabotage run is physically a BIAS-MOVED run (identical ΔS_core), relabeled FRICTION-RENAMED only because the flag check precedes the bias check.

**Good news, stated plainly — the no-smuggle rail PASSED.** The credit is conservative bookkeeping (energy-conserving `sqrt(max(1−δ/E_g,0))` rescale + bath credit, Ax3-clean); `_phase_scramble` preserves `Σ_p V_p²` sitewise; there is **no Re(Z)** resistive element and **no ℏ-as-FD** constant anywhere. **The void is the meter, not a hidden dissipator.**

> ★ **DETECTOR-REBUILD GATE (mandatory — 2026-07-16, post-#711-review).** Before any future F6 / R7 arm may bank **CHANNEL-BOUNDED** or ungate the thermometer re-fire, the mode-count detector MUST be rebuilt to satisfy **both**:
> 1. **A real bath DOF** — actual dynamics and frequencies with **back-reaction** onto the lattice (not a `np.zeros(M_MODES)` side-array written by `_credit_modes` and read only by `_n_occ`, with zero dynamical consequence).
> 2. **A FRICTION-RENAMED control that varies a physical quantity** — the sabotage must perturb an energetic/dynamical observable, not the `credit_modes` bookkeeping flag; the current control is bit-identical to production except the side-array increment, so it cannot fail on any energetic run.
>
> Until **both** are met, `ΔN_occ` is bookkeeping-liveness only and no arm may cite it (or the twin-64) as physical mode-count corroboration.