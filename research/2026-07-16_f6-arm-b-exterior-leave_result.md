# F6 mode-count Arm B (G0 exterior leave) — RESULT

**Date:** 2026-07-16  
**Prereg:** [`2026-07-16_f6-arm-b-exterior-leave_prereg_FROZEN.md`](2026-07-16_f6-arm-b-exterior-leave_prereg_FROZEN.md) (freeze commit `5bda8777` before driver)  
**Driver:** `src/scripts/vol_1_foundations/f6_arm_b_exterior_leave.py`  
**Charters:** mode-count door; frontier map (Tier-0 G0; Grant GO)

---

## Verdict

**BIAS-MOVED** (bin fire; Rule 11 stands)

**WRONG-OBJECT / CATEGORY-WRONG** (2026-07-16 circuit-first repair — does not retune bins)

Exterior **deposit path intact** (`ΔN_occ≥1`; magnitude = the `M_MODES` knob) — a code-flag self-test, **not** a physical mode-count measurement (see 🔴 mode-count demotion below). Bias knife still kills.

| Check | Outcome |
|---|---|
| Exterior `E_bath`↑ | yes (~5.78) |
| Exterior deposit path (`ΔN_occ≥1`) | yes — `ΔN_occ≡M_MODES` **by construction** (`M_MODES=64`; a code-flag self-test, not a mode-count measurement — see demotion) |
| Soft ledger (post-equilibration baseline) | **CLOSES ~1.4 %** — `|(E_equil−E_f)−E_bath| = 0.111` vs `E_equil = 2·E0 = 7.678`; PASSES the frozen `0.5·E_equil` tol; OFF ledger ≈ 0. The shipped ≈3.73 "messy" figure was a t=0 baseline artifact — see 🔴 E0 fix below |
| Core bias | **FAIL** (`|ΔS_core|≈0.017 ≫ 5e-3`) — the banked kill (bookkeeping-independent) |
| Core drain (co-fire) | **FAILS in substance** (`rel=(off−on)/off = 0.362 ≫ DRAIN_TOL=0.05`, 7.2× over) — the frozen `classify()` tests **BIAS-MOVED before ELECTRON-DRAIN**, so only BIAS-MOVED is *returned*, but the drain bin genuinely fires. Not a false pass (both fail-closed); recorded per the #711 reporting rule. |
| Sabotage friction | **FRICTION-RENAMED** — catches only the deliberate scalar-accounting sabotage plant (`credit_modes=False`); unreachable by production physics |
| Sponge control | **NEGATIVE CONTROL OK** (κ=0 → E_bath≡0 → NULL short-circuit; verified pml∈{0,2,4,6}) — verifies the κ-off branch; **not** a liveness demo (SPONGE-COSTUME is entailed-never; genuine mode-liveness = the FRICTION-RENAMED plant) |

> **Statistic note (`mean_S_core` is a CONTRAST, not saturation).** The `ΔS_core` that drives BIAS-MOVED is built from `_mean_S`, which normalizes A² by the **in-mask peak** density — so the hottest core site always reads `a2=1` (contrast `S=0`) at any amplitude. It is a peak-normalized density-profile-**shape** contrast, **not** the canonical Ax-4 saturation `S(A)=√(1−(A/A_yield)²)` referenced to `V_SNAP`. Measured true core saturation (canonical `A=|V_inc|/V_SNAP`, two-method) stays `S ≥ 0.99` (`A²_max≈0.021` vs `V_SNAP=1.0`) **everywhere in the run** — deep sub-yield, never near the wall (`S→0`). So **BIAS-MOVED gates a density-profile-shape change**, not an absolute saturation-bias move; any downstream regime-classification (e.g. §5b "cold/knee/wall" via `S`) must use the `V_SNAP`-referenced `S`, not this contrast. Same `_mean_S` is verbatim in Arm A (**#711**) — the relabel applies there too (cross-cite; that branch is not touched here).

---

## 🔴 Mode-count detector — DEMOTED (2026-07-16 adversarial-review repair)

> **Rule-12 demotion.** Prior banking of an **"exterior mode-count detector LIVE (`ΔN_occ=64`)"** as a measured leave signature is **superseded**. `ΔN_occ ≡ M_MODES` **by construction**: `_credit_modes` round-robins every packet into the `N_SPREAD=4` lowest slots of a pre-allocated `np.zeros(M_MODES)` array, which saturates to full occupancy in ~16 events (here 27 300 events fill it with certainty). Live-fire structural-parameter variation: `M_MODES` ∈ {16, 48, 64, 128, 256} → `ΔN_occ` = {16, 48, 64, 128, 256} with `E_bath = 5.776694` **invariant** — `ΔN_occ` tracks the declared array size, not any physical leave property. The `b[m]` ledger is **write-only** (zero back-reaction: `credit_modes=True` vs `False` give bit-identical lattice trajectories `field=1.790800006`, `core=0.199897610`; only the label flips BIAS-MOVED↔FRICTION-RENAMED).
>
> **Corrected reading:** deposit-path intact (`ΔN_occ ≥ 1`; magnitude = the `M_MODES` knob) — **a code-flag self-test, NOT a physical mode-count measurement.** This elevates the prereg's own disclosed tell (§4: "`ΔN_occ ≥ 1` *by construction of mode credit* unless deposit path is broken").
>
> **Twin-64 resolved (plainly):** Arm A's interior `ΔN_occ=64` and Arm B's exterior `ΔN_occ=64` are **the same constant printed twice** (`M_MODES=64` shared verbatim across both drivers), not two independent geometries converging on a measurement.
>
> **FRICTION-RENAMED** is reachable **only** by the deliberate scalar-accounting sabotage plant (`--sabotage-friction`, `credit_modes=False`); production physics (any positive δ with the flag on) always fills the slots, so the bin is **unreachable by production inputs** — a discriminator on the bookkeeping code-path, not on a physical irreversibility magnitude.
>
> **What survives, un-demoted:** the **BIAS-MOVED** kill rests on `ΔS_core = −0.017146` (`|ΔS_core| > BIAS_TOL=5e-3`), which is **bookkeeping-independent** (identical with crediting on or off). The bin fire and the WRONG-OBJECT closure stand; only the mode-count-LIVE *leg* is void.
>
> **MANDATORY GATE (detector rebuild).** Before any `CHANNEL-BOUNDED` bank or thermometer ungate, the mode-count observable must be rebuilt with **real bath DOF + back-reaction into the lattice + a physical control that can fail on physical inputs**. The `#711` (Arm A) repair registers the same gate — cross-cite; the two 64's fall together.

---

## 🔴 Soft ledger — E0 baseline bug FIXED (2026-07-16 adversarial-review repair)

> **Rule-12 supersession of "Soft ledger messy / fail-adjacent ≈3.73".** Adversarial review confirmed the ledger was booked against the **wrong baseline**: `E0` was measured on the raw **V_inc-only seed** (`3.839`), which is not a valid `V_inc/V_ref` equilibrium. The first `lat.step()` equilibrates the seed and the OFF energy **doubles EXACTLY 2.000000×** (`3.839 → 7.678`, then conserves to machine precision). Booking `|(E0−E_f)−E_bath|` against the un-equilibrated seed therefore returned `≈E0` **identically** (measured `0.971·E0`), so the soft sub-gate — a mandatory sub-condition of `CHANNEL-BOUNDED` — was **structurally unreachable**: the pass bin could never fire for any energy-conserving run, regardless of the substrate. The "soft ledger messy" banking was a **measurement artifact**, not a physical statement about the leave.
>
> **Fix (driver):** the baseline is now the **equilibrated** field `E_equil`, captured post-step-1 / pre-transfer (`RunOut.E_field_equil`; `classify()` uses it for the DETONATE threshold). The lattice trajectory is **byte-identical** — all survivors unchanged: `E_bath=5.776694382`, `E_field_final=1.790800006`, `E_core_final=0.199897610`, `ΔS_core=−0.017146406`, `ΔN_occ=64`.
>
> **Honest re-bank (two-method verified — driver `--json` + independent probe):** `soft = |(E_equil − E_f) − E_bath| = 0.110790` = **1.443 %** of `E_equil=7.678285`; PASSES the frozen `0.5·E_equil` tol (`0.0289 ≪ 1`). OFF ledger ≈ `5.3e-15`. The exterior ledger **closes** — the leave is honestly booked, and the pass bin is no longer foreclosed.
>
> This does **not** move the verdict: `classify()` returns **BIAS-MOVED** at step 4 (`|ΔS_core| > BIAS_TOL`), **upstream** of the soft-ledger DETONATE check, and the WRONG-OBJECT closure rests on the unsaturated-siphon argument (below), not on soft-ledger reachability. Same E0 baseline convention flagged to the **#711** (Arm A) repair — same bug class; coordinate wording.
>
> **Historical correction (for the record).** The superseded row read "fail-adjacent (≈3.73 vs tol·E0) — would DETONATE if bias had passed." Both halves were wrong even under the frozen tolerance: (1) against the shipped seed-`E0` tol it was an **outright FAIL**, `soft = 3.7284 > 0.5·3.8391 = 1.9196` (**1.94×** over), not "fail-adjacent"; (2) the counterfactual bin was **ELECTRON-DRAIN**, not DETONATE — `classify()` tests drain (`rel=0.362>0.05`) *before* the soft-ledger DETONATE branch, so had bias passed the fire would have been drain. The 2.000000× non-conservation of the ports-OFF baseline (`3.839→7.678` in 150 steps) is what "soft ledger messy" actually was — the exterior ledger booking **engine-pump-created** energy, echoing the known engine-pumps-at-dt→0 finding — not dissipation.

---

## WRONG-OBJECT fence (circuit-first)

> 🔴 **Rule-12 2026-07-16:** Prior framing of Arm B as a “necessary-door discriminator” for frontier / saturation physics is **superseded**. The bin fire (**BIAS-MOVED**) is preserved. The object tested was an **unsaturated face \(V\)-scale siphon** into an exterior `b[m]` ledger — **not** native K4 port refusal at the wall (\(|\Gamma|\to 1\), storage→boundary; [`../manuscript/ave-kb/common/envelope-anatomy.md`](../manuscript/ave-kb/common/envelope-anatomy.md) saturation anatomy). Siphon ≠ saturated-port wall. This RESULT does **not** constrain what native mirror ports do under \(S\to 0\).

Canonical repair map: [`2026-07-16_f6-circuit-first-door-map_CHARTER.md`](2026-07-16_f6-circuit-first-door-map_CHARTER.md). Fool-mode banked on mode-count + frontier charters: **unsaturated face extract ≠ saturated-port wall**.

---

## Scope fence (honest)

This fire kills the **siphon / face-ledger costume class** under the mode-count bins. It does **not**:
- prove or refute DE lifecycle or crystallization
- prove F6 occupancy chord
- bank orthogonal (G1) release geometry
- speak for native \(|\Gamma|\to 1\) port physics
- ungate the thermometer

Full frontier mint (`node_creation`) remains **out of scope** / **NO** per map charter.

---

## Rule 11

Do not retune `PACKET`, `CORE_R`, face mask, or `BIAS_TOL` to chase CHANNEL-BOUNDED. Arm B class joins rung-2 / Arm A as bias≠release kill under the same core knife — **and** is closed as WRONG-OBJECT for wall/frontier claims. No Arm C siphon.
