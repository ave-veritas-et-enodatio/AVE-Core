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

### A3 — Soft-ledger convention bug: baseline captured off-shell; §5 physics-attribution corrected (findings 1 / 6 / 9 — MAJOR ×2 → one mechanism)

**The bug.** `E0 = float(lat.total_energy())` was captured **before** the first `lat.step()`, on an off-shell seed (V_ref = 0). The TLM connect mirrors V_inc into V_ref, and `get_energy_density = Σ_p V_inc² + V_ref²`, so the total energy **doubles exactly** at the first connect: `E0_seed = 3.83914` → `E1 = 7.67828`, ratio **2.0000000000** (reproduced two ways), then conserves to 1e-15. Hence

> soft = |(E0 − Ef) − E_bath| = |E0 − E1| = E0, **for ANY transfer** — the ledger measured the seed-doubling gap, not an accounting residual.

Consequences as shipped:
- Shipped `soft_ledger ≈ 3.760 ≈ E0`, vs tolerance `0.5·E0 = 1.920` — blown ~2×.
- The **lossless OFF control** (`kappa=0`) itself blew it: `off.soft_ledger = 3.839 = E0` exactly `> 1.920` — a gate its own control fails.
- **CHANNEL-BOUNDED — the only ungate bin — was structurally unreachable as shipped**: any run reaching the soft check returned DETONATE unconditionally. The pass bin fired only for the hand-built `test_classify_bounded` RunOut, never from a lattice run.

**The fix (this PR).** `E0` is now captured **after the first `lat.step()`** (on-shell). Re-run (fixed harness, two-method-verified):

| quantity | as shipped | repaired |
|---|---|---|
| `on.soft_ledger` | 3.760 | **7.899e-2** |
| balance | field drop 7.634 vs bath 7.555 → 0.079 = **1.03%** of on-shell E0 (7.678) | (same, now reported) |
| `off.soft_ledger` (lossless control) | 3.839 (**blows** 1.920) | 5.33e-15 (**passes**) |
| verdict | BIAS-MOVED | **BIAS-MOVED** (unchanged; bias fires before soft) |

CHANNEL-BOUNDED is now **reachable-in-principle** from a legal door (the soft-check no longer fires on a balanced run: 0.079 < 0.5·7.678 = 3.839).

**§5 correction (Rule-12 supersession).** §5 line 109 — "fails bias≠release at the same protected-core knife as rung-2 **(scatter / soft-ledger mismatch)**" — the parenthetical is **superseded**: the soft-ledger term was an E0-capture accounting artifact, not a physical mismatch. The BIAS-MOVED kill rests **solely** on the independent protected-core `ΔS_core` bias knife (`|ΔS_core| = 0.142 ≫ BIAS_TOL = 5e-3`), which is measured before the soft check and is unaffected by this bug.

### A4 — Multi-kill co-fire; classify precedence was never frozen (findings 3 / 8 — MINOR ×2)

The fired run satisfies **more than one** frozen fail-closed bin. All satisfied bins (two-method-verified on the repaired harness):

| bin | condition | fires? |
|---|---|---|
| **BIAS-MOVED** (reported) | `\|ΔS_core\| = 0.142 > BIAS_TOL 5e-3` (28×) | ✅ |
| **ELECTRON-DRAIN** | protected-core drain `(0.3131 − 0.0398)/0.3131 = 0.873` = **87.3%** > DRAIN_TOL 5% | ✅ |
| **DETONATE** (soft-ledger clause) | soft > 0.5·E0 | ⚠️ fired **as shipped** (soft 3.760 > 1.920) but that was the **cluster-3 E0-capture artifact** (it also fired on the lossless OFF control); **post-repair it no longer fires** (0.079 < 3.839) |

`classify()` returns only the first match, and its **precedence** (`DETONATE → NULL → FRICTION-RENAMED → BIAS-MOVED → ELECTRON-DRAIN → soft-DETONATE → CHANNEL-BOUNDED`) was **never frozen** — the prereg §2 froze bin *definitions* and a fail-closed *list*, not a tie-break order, and the precedence shipped in the same commit as the RESULT (finding 2 / A5). So **BIAS-MOVED was precedence-selected** among co-firing fail-closed bins. All satisfied bins are **co-directional** (protected-core corruption), so the kill stands and the physics conclusion is invariant — this is reporting completeness, not a verdict flip; the run is *more* dead than the single-bin report stated (genuine BIAS-MOVED **and** 87.3% ELECTRON-DRAIN).

> **Reporting rule (frozen for future arms, 2026-07-16):** report **ALL** satisfied bins, not just the precedence-selected one; and **classify() precedence MUST be frozen pre-fire** (in the prereg or a pushed driver preceding the result), so no tie-break is chosen with results in hand.

### A5 — Freeze-window honesty (finding 2 — MINOR)

The prereg push (`17662232`, 08:35:34, FROZEN.md only, 100 insertions) preceded the result commit (`4a185d93`, 08:37:16, driver 287 lines + tests 68 lines + both fires + 4 doc edits) by **102 seconds**. So **freeze-by-push evidences the PREREG doc only**; the driver, `classify()` precedence, tests, and RESULT are **self-declared** (authored one commit later, not push-separated from the fire). The deciding bins/tolerances (§2/§4) *were* push-frozen first, so the fail-closed conclusion is robust — but "classify frozen before RESULT" carries no push evidence. **Recommendation for future arms:** adopt the standing margin convention — push the driver (with frozen `classify()`/precedence) as a separate artifact *before* running the fire, so the code freeze is push-evidenced, not self-declared.

### A6 — "(or field drop)" disjunct now IMPLEMENTED (finding 10 — MINOR)

The frozen §2 bin table (line 44) defines FRICTION-RENAMED as `E_bath ≥ NULL_FLOOR` **(or field drop)** `but ΔN_occ < 1`. The shipped `classify()` dropped the "(or field drop)" disjunct and checked `E_bath < NULL_FLOOR → NULL` first, so a pure renamed-friction defect (field energy removed with **no** bath credit and `ΔN_occ < 1`) mis-binned as NULL ("build incomplete") instead of the fail-closed FRICTION-RENAMED the frozen table assigns. **Repaired (code → frozen spec):** `classify()` now bins FRICTION-RENAMED when energy moved (`E_bath ≥ NULL_FLOOR` **or** `E_field_final < E_field_initial`) with `ΔN_occ < 1`, reserving NULL for a genuinely silent gate (no bath **and** no field drop). Two new unit tests (`test_classify_friction_renamed_field_drop`, `test_classify_null_silent_gate`) cover the disjunct; 6/6 tests pass; the shipped run is unaffected (production `E_bath=7.55 ≫ NULL_FLOOR`, `ΔN_occ=64` → still BIAS-MOVED; sabotage → still FRICTION-RENAMED). This is a fidelity fix toward the frozen spec, not a retune.

### A7 — What survives, banked plainly (Rule 11)

**Arm A = BIAS-MOVED. BANKED.** The verdict stands on the independent protected-core strain knife:

> `ΔS_core = 1.421e-1 ≫ BIAS_TOL = 5e-3` (**28×**), measured on the protected core (mean over 150 steps, ON 0.75136 vs OFF 0.60927), **before** every voided gate in `classify()`.

Event-gating + multi-mode credit did **not** evade the same protected-core bias knife that killed rung-2. The Arm A negative is **real and banked**; the arm is **NOT CHANNEL-BOUNDED**; the thermometer re-fire stays **GATED**.

**Rule 11 honored — no retune.** No tolerance/knob was moved to rescue a result. The two driver changes are fidelity repairs that leave the verdict invariant: (i) E0 baseline captured on-shell (A3 — corrects an accounting artifact, verdict unchanged); (ii) the `(or field drop)` disjunct implemented (A6 — code → frozen spec, shipped run unaffected).

**What is NOT banked** (awaits the detector-rebuild gate, A2): the "mode-count detector LIVE" claim (A1) and the FRICTION-RENAMED control as a physical discriminator (A2). Until the detector is rebuilt (real bath DOF + physical-quantity control), no arm may bank CHANNEL-BOUNDED or ungate the thermometer on the strength of `ΔN_occ`.

---

## Post-freeze correction-note — 2026-07-18 — Platform line `nonlinear=True` is a no-op (costume; FACT-1-unconditional)

**Append-only, dated; §3 method body byte-untouched (label corrected for the record, not the frozen plant).** Routed from the F6 bath-meter nonlinear-revalidation lane (`2026-07-17_f6-meter-nonlinear-reval_result.md` R-2; charter `2026-07-16_f6-bath-meter_CHARTER.md` §B1 FACT-1 / R-2) and landed here.

- **§3.1's `Platform: … nonlinear=True` is a no-op in `K4Lattice3D` — dead code.** Per PR #721 review **FACT-1-unconditional**, the `nonlinear` flag has **zero dynamical consequence**: the K4 4-port scattering matrix `build_scattering_matrix(z)` (`src/ave/core/k4_tlm.py:64`) reduces to `S[i,j] = 2y/(N·y) − δ = 0.5 − δ` for `N=4` — **z-independent** — so the nonlinear branch reproduces the linear scatter exactly (the reviewer's op3-OFF twin was bit-identical too, `~1e-15`). The flag is a no-op **regardless of `op3_bond_reflection`**.
- **What the plant actually was: weakly-nonlinear-via-op3 only.** The amplitude-dependent kernel `S(A)=√(1−A²) → z_local=(1−A²)^(−1/4)` flows through **op3's bond Γ** (ON here), not the flag; at the mild seed its amplitude dependence is second-order / negligible. The plant is **weakly-nonlinear-via-op3**, not a genuinely Op14-saturated lattice.
- **The Arm A verdict is UNAFFECTED.** **BIAS-MOVED** rests on the independent protected-core strain knife (`ΔS_core = 1.421e-1 ≫ BIAS_TOL`, A7) computed on the trajectory itself; the **bias knife did not consume the `nonlinear` flag**, so the no-op does not touch the verdict. Nothing is re-run or retuned.
- **Correction:** the frozen §3 platform label is **costume for `nonlinear=True`** to the same degree the meter lane's was pre-relabel. Recorded for the register; the frozen body is unchanged.