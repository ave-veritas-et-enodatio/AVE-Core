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
| Soft ledger | fail-adjacent (≈3.73 vs tol·E0) — would DETONATE if bias had passed |
| Core bias | **FAIL** (`|ΔS_core|≈0.017 ≫ 5e-3`) |
| Sabotage friction | **FRICTION-RENAMED** — catches only the deliberate scalar-accounting sabotage plant (`credit_modes=False`); unreachable by production physics |
| Sponge control | **OK** (NULL — not CHANNEL-BOUNDED) |

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
